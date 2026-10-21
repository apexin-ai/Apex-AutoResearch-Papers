# paper writing introduction

**Temporal Score Incomparability in LLM Benchmarks: A Large-Scale Psychometric Audit of 5,227 Models** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 51
- **Recorded user turns:** 0
- **Tool calls:** 25
- **Original source:** `logs/chats/worker_paper_writing_introduction_20260521T042708.jsonl`
- **Structured JSON:** [`3f3ec718415cb9379029.json`](../../sessions/3f/3f3ec718415cb9379029.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

51 recorded events

### Tool call

_source line 1 · 2026-05-21T04:32:55.850912+00:00_

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
  "session": "worker_paper_writing_introduction_20260521T042708",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/agent-ml-research/skills/global/paper-writing-norms.skill.md"
  }
}
```

</details>

---

### Tool result

_source line 2 · 2026-05-21T04:32:55.851534+00:00_

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
  "session": "worker_paper_writing_introduction_20260521T042708",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-21T04:32:55.851754+00:00_

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
  "session": "worker_paper_writing_introduction_20260521T042708",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/agent-ml-research/skills/global/latex-paper.skill.md"
  }
}
```

</details>

---

### Tool result

_source line 4 · 2026-05-21T04:32:55.852149+00:00_

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
  "session": "worker_paper_writing_introduction_20260521T042708",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-21T04:32:55.852405+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/experiments.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_introduction_20260521T042708",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/experiments.tex"
  }
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-21T04:32:55.852780+00:00_

1	\section{Experiments}
2	\label{sec:experiments}
3	
4	We apply MH-DIF to the METABENCH dataset~\citep{kipnis2024metabench}, which provides sparse response matrices for 5,227 models evaluated on 12,508 MMLU items~\citep{hendrycks2021mmlu}. All temporal analyses define reference and focal cohorts by model release date (2023 vs.\ 2024). We validate detection power through simulation, characterize temporal instability across multiple cohort designs, evaluate the relationship between DIF flags and existing contamination labels, and assess downstream consequences for benchmark rankings. Replication on GSM8K with cross-benchmark contamination validation appears in \Cref{sec:gsm8k}.
5	
6	\subsection{Validation: DIF Detection Power}
7	\label{sec:validation}
8	
9	To confirm that MH-DIF detects differential item functioning at the sample sizes available in METABENCH, we conduct a power analysis using empirical MMLU IRT parameters. We simulate item response matrices where a controlled subset of items has injected DIF of varying magnitude ($|\Delta_{\mathrm{MH}}| \geq 1.4$) and evaluate ETS~C classification across sample sizes $N \in \{40, 80, 160, 320\}$ per cohort. At $N \geq 80$, ETS~C achieves true positive rates of 0.68--0.80 with false positive rates of 0.036--0.042 and AUC of 0.93--0.94. The temporal cohort sizes in our analysis ($N_{\mathrm{ref}} = 1{,}080$, $N_{\mathrm{focal}} = 807$) far exceed this threshold, and statistical power is not a limiting factor for the results reported below. Full simulation results with confidence intervals appear in Appendix~Table~A1.
10	
11	\subsection{Temporal Comparability: 31\% Item Instability}
12	\label{sec:temporal}
13	
14	The central finding of this paper is that a substantial fraction of MMLU items behave differently across model generations. Comparing models released in 2023 ($N = 1{,}080$) against models released in 2024 ($N = 807$), 31.3\% of items receive ETS~C classification ($|\Delta_{\mathrm{MH}}| \geq 1.5$). Applying Ben
…[truncated 17629 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_introduction_20260521T042708",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-21T04:32:55.853034+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/method.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_introduction_20260521T042708",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/method.tex"
  }
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-21T04:32:55.853304+00:00_

1	\section{Method}
2	\label{sec:method}
3	
4	We adopt Differential Item Functioning (DIF) analysis from educational measurement to assess whether individual benchmark items behave consistently across groups of LLMs. The procedure requires only a binary response matrix and group labels, with no access to model internals or training data. Below we define the data, the statistical test, the cohort designs, a semi-synthetic validation framework, diagnostic checks, and statistical controls.
5	
6	\subsection{Data}
7	\label{sec:data}
8	
9	The primary dataset is the METABENCH response matrix~\citep{kipnis2024metabench}, which records binary outcomes (1~=~correct, 0~=~incorrect) for 5,227 models evaluated on 12,508 MMLU items~\citep{hendrycks2021mmlu}. Models span release dates from 2023 to 2024, drawn from the Open LLM Leaderboard. MMLU covers 57 subjects grouped into five broad domains (STEM, Humanities, Social Sciences, Other, and a mixed category). We supplement the response matrix with the web-overlap contamination labels of \citet{li2024contamination}, which classify 9,229 of 12,508 items (73.8\% coverage) as ``contaminated'' or ``clean'' based on verbatim matches in publicly accessible web corpora. These labels serve as an external reference for evaluating the relationship between DIF flags and existing contamination indicators.
10	
11	\subsection{Mantel-Haenszel DIF and ETS Classification}
12	\label{sec:mhdif}
13	
14	In educational testing, Differential Item Functioning (DIF) occurs when an item's statistical relationship to the latent trait $\theta$ differs between two groups after conditioning on ability level. An item with DIF is not merely harder for one group; it functions differently relative to what the group's overall ability would predict. The standard terminology refers to test-takers as ``examinees'' and questions as ``items.'' In our setting, examinees are LLMs and items are benchmark questions.
15	
16	The Mantel-Haenszel (MH) procedure~\citep{holland1988
…[truncated 7751 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_introduction_20260521T042708",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-21T04:32:55.853569+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/*.bib",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_introduction_20260521T042708",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/*.bib",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper"
  }
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-21T04:32:55.853791+00:00_

paper/references.bib

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_introduction_20260521T042708",
  "tool": "Glob",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-21T04:32:55.853977+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/main.tex",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_introduction_20260521T042708",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/main.tex",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper"
  }
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-21T04:32:55.854153+00:00_

paper/main.tex

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_introduction_20260521T042708",
  "tool": "Glob",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-21T04:32:55.854319+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/*.tex",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_introduction_20260521T042708",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/*.tex",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections"
  }
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-21T04:32:55.854489+00:00_

paper/sections/experiments.tex
paper/sections/introduction.tex
paper/sections/appendix.tex
paper/sections/abstract.tex
paper/sections/discussion.tex
paper/sections/conclusion.tex
paper/sections/related_work.tex
paper/sections/method.tex

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_introduction_20260521T042708",
  "tool": "Glob",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-21T04:32:55.854657+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/references.bib"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_introduction_20260521T042708",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/references.bib"
  }
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-21T04:32:55.855020+00:00_

1	% ============================================================
2	% Benchmark Contamination Detection
3	% ============================================================
4	
5	@inproceedings{balloccu2024leak,
6	  title     = {Leak, Cheat, Repeat: Data Contamination and Evaluation Malpractices in Closed-Source {LLMs}},
7	  author    = {Balloccu, Simone and Schmidtova, Patrícia and Lango, Mateusz and Dusek, Ondrej},
8	  booktitle = {Proceedings of the 18th Conference of the European Chapter of the Association for Computational Linguistics (EACL)},
9	  year      = {2024},
10	  doi       = {10.18653/v1/2024.eacl-long.5},
11	  url       = {https://arxiv.org/abs/2402.03927}
12	}
13	
14	@inproceedings{dekoninck2024constat,
15	  title     = {{ConStat}: Performance-Based Contamination Detection in Large Language Models},
16	  author    = {Dekoninck, Jasper and Mueller, Mark Niklas and Vechev, Martin},
17	  booktitle = {Advances in Neural Information Processing Systems (NeurIPS)},
18	  year      = {2024},
19	  url       = {https://arxiv.org/abs/2405.16281}
20	}
21	
22	@inproceedings{golchin2024timetravel,
23	  title     = {Time Travel in {LLMs}: Tracing Data Contamination in Large Language Models},
24	  author    = {Golchin, Shahriar and Surdeanu, Mihai},
25	  booktitle = {Proceedings of the International Conference on Learning Representations (ICLR)},
26	  year      = {2024},
27	  url       = {https://arxiv.org/abs/2308.08493}
28	}
29	
30	@inproceedings{li2024contamination,
31	  title     = {An Open-Source Data Contamination Report for Large Language Models},
32	  author    = {Li, Yucheng and Guo, Yunhao and Guerin, Frank and Lin, Chenghua},
33	  booktitle = {Findings of the Association for Computational Linguistics: EMNLP 2024},
34	  year      = {2024},
35	  doi       = {10.18653/v1/2024.findings-emnlp.30},
36	  url       = {https://aclanthology.org/2024.findings-emnlp.30/}
37	}
38	
39	@misc{liang2026dvd,
40	  title         = {{DVD}: Detection via Variance of Generation Distri
…[truncated 19059 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_introduction_20260521T042708",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-21T04:32:55.855269+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_introduction_20260521T042708",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/introduction.tex"
  }
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-21T04:32:55.855459+00:00_

1	% Placeholder for introduction
2	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_introduction_20260521T042708",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-21T04:32:55.855638+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/main.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_introduction_20260521T042708",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/main.tex"
  }
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-21T04:32:55.855860+00:00_

1	\documentclass{article}
2	\usepackage{iclr2026_conference,times}
3	\input{math_commands.tex}
4	
5	\usepackage{hyperref}
6	\usepackage{url}
7	\usepackage{booktabs}
8	\usepackage{graphicx}
9	\usepackage{xcolor}
10	\usepackage{microtype}
11	\usepackage{multirow}
12	\usepackage{subcaption}
13	\usepackage{cleveref}
14	
15	\graphicspath{{../figures/paper/}}
16	
17	\title{Psychometric Instability of LLM Benchmarks:\\Differential Item Functioning Reveals 31\% of MMLU Items\\Behave Differently Across Model Generations}
18	
19	%\iclrfinalcopy
20	
21	\newcommand{\fix}{\marginpar{FIX}}
22	\newcommand{\new}{\marginpar{NEW}}
23	
24	\begin{document}
25	
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
36	\bibliography{references}
37	\bibliographystyle{iclr2026_conference}
38	
39	\appendix
40	\input{sections/appendix}
41	
42	\end{document}
43	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_introduction_20260521T042708",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 21 · 2026-05-21T04:32:55.856035+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/abstract.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_introduction_20260521T042708",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/abstract.tex"
  }
}
```

</details>

---

### Tool result

_source line 22 · 2026-05-21T04:32:55.856191+00:00_

1	% Placeholder for abstract
2	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_introduction_20260521T042708",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 23 · 2026-05-21T04:32:55.856316+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_introduction_20260521T042708",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/related_work.tex"
  }
}
```

</details>

---

### Tool result

_source line 24 · 2026-05-21T04:32:55.856437+00:00_

1	% Placeholder for related_work
2	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_introduction_20260521T042708",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 25 · 2026-05-21T04:32:55.856766+00:00_

called Write

<details open><summary>🔧 Tool call — Write</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/introduction.tex",
  "content": "\\section{Introduction}\n\\label{sec:introduction}\n\nWhen we say ``Model B outperforms Model A on MMLU,'' we implicitly assume that the benchmark measures the same construct in the same way for both models. This assumption of temporal comparability underpins every cross-generation comparison published on leaderboards and in model reports, yet it is rarely tested. Applying Mantel-Haenszel Differential Item Functioning (MH-DIF) analysis~\\citep{holland1988mh} with Educational Testing Service (ETS) severity classification to the METABENCH response matrix~\\citep{kipnis2024metabench}, we find that 31\\% of MMLU~\\citep{hendrycks2021mmlu} items receive ETS Category~C classification ($|\\Delta_{\\mathrm{MH}}| \\geq 1.5$, $p < 0.05$), indicating large shifts in item functioning between models released in 2023 and 2024. This is not statistical noise: a random-split control within the 2023 cohort yields only 0.18\\% ETS~C items. The instability persists within every MMLU subject domain, with domain-level C\\% ranging from 31\\% to 45\\% (mean 38.1\\%), and item-level regression shows that 92.4\\% of this instability is unrelated to aggregate domain-level accuracy gains. Nearly one in three MMLU items behaves differently depending on when the evaluated models were trained.\n\nA growing body of contamination detection research has produced sophisticated item-level methods, from membership inference approaches such as Min-K\\%~\\citep{shi2024mink} to performance-based detectors such as ConStat~\\citep{dekoninck2024constat}, DVD~\\citep{liang2026dvd}, and Self-Critique~\\citep{tao2026selfcritique}. These methods validate detection accuracy primarily against web-overlap labels such as those of \\citet{li2024contamination}, which classify benchmark items as contaminated based on verbatim or near-verbatim matches in publicly accessible training corpora. Such labels measure \\emph{global exposure}: whether an item exists in the data ecosystem that all training pipelines can access. They do not measure \\emph{differential item functioning}: whether an item behaves differently across model cohorts that may have had varying degrees of exposure or different training methodologies. \\Cref{fig:global_vs_differential} illustrates the distinction. Most MMLU items are globally contaminated in the sense that they exist in web-accessible text, so all model cohorts encounter them and no differential signal arises. The items that function differentially are those where exposure or training methodology changed asymmetrically across cohorts. Validating differential detectors against global-exposure labels therefore conflates two phenomena, and the near-chance enrichment (0.96) between DIF flags and web-overlap labels is the expected outcome of this mismatch.\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{fig_1_global_vs_differential.pdf}\n\\caption{Global vs.\\ differential contamination, illustrated via Item Characteristic Curves (ICCs). \\textbf{Left}: global contamination produces no DIF; both cohorts encounter the item, and their ICCs overlap. \\textbf{Right}: differential contamination produces DIF; the focal cohort's ICC shifts because only that cohort was disproportionately exposed during training. The enrichment ratio of $\\approx 1.0$ between DIF flags and web-overlap labels is expected because most MMLU items fall into the left category.}\n\\label{fig:global_vs_differential}\n\\end{figure}\n\nWe apply classical MH-DIF with ETS classification to the full METABENCH response matrix (5,227 models $\\times$ 12,508 MMLU items), the largest-scale DIF analysis on LLM benchmarks to date. This psychometric approach is motivated by recent findings that contamination detectors are fragile under post-training~\\citep{wang2026fragility} and by concurrent work using anchor-item calibration for score comparability~\\citep{habba2026growingpains}, which addresses a complementary question (equating scores across cohorts) to ours (characterizing temporal item stability). We initially hypothesized that DIF could identify differentially contaminated items: benchmark questions whose statistical properties shifted because newer models had been trained on them. Semi-synthetic injection experiments confirmed detection capability ($\\Delta\\mathrm{TPR} = {+}0.508$ at exploitation rate $p = 0.5$), and our cross-subject matching protocol eliminated false positive inflation ($\\Delta\\mathrm{FPR} = 0.000$). Three structural refinements (matched-ability quintile analysis, IRT $\\theta$-conditioning, and within-subject bifactor pre-checks) all failed to reduce the temporal C\\% below 31\\%, however. The persistent non-reduction shifted our research question: from whether DIF detects contamination, to what the persistent 31\\% instability reveals about how benchmarks interact with evolving model populations.\n\nA natural tension arises between our headline finding and its practical consequences. On one hand, 31\\% of items are functionally unstable across model generations. On the other, Spearman rank correlation between model rankings computed on all 12,508 items versus stable-only items is $\\rho \\approx 0.997$. The resolution lies in measurement redundancy: MMLU's 12,508 items provide sufficient statistical mass that removing nearly a third does not alter rank order. This is precisely why DIF should be understood as a diagnostic lens (which items changed and for which model families) rather than a quality filter (remove bad items to improve the benchmark). Despite aggregate stability, DIF-flagged items concentrate discriminative signal that differentiates model generations: removing DIF items degrades ranking discriminability more than removing an equal number of random items ($z = -8$ to $-49\\sigma$ across 21 conditions). Individual model families show distinctive DIF profiles: Phi-3 and Llama-3 gain ${+}700$ to ${+}850$ rank positions under stable-item evaluation, while Mistral-based merges lose $-400$ to $-587$ positions.\n\nWe do not modify the MH-DIF procedure itself. The contributions of this work lie in applying it at a scale and in a context where its standard assumptions face new challenges, and in the empirical findings that emerge. At 5,227 models, the analysis exceeds typical educational testing applications by orders of magnitude, requiring careful attention to stratification and matching. Cross-subject matching, a protocol we introduce for semi-synthetic evaluation on multi-subject benchmarks, eliminates false positive inflation entirely ($\\Delta\\mathrm{FPR} = 0.000$). The ground truth analysis exposes a fundamental validation methodology gap: web-overlap labels cannot serve as ground truth for item-level differential detectors because global exposure and differential functioning are distinct phenomena. Cross-benchmark replication on GSM8K with independent contamination validation through the GSM1K held-out set~\\citep{zhang2024gsm1k} confirms that the findings generalize beyond MMLU. We make the following contributions:\n\n\\begin{enumerate}\n\\item \\textbf{Benchmark temporal comparability} (Claim 1): 31\\% of MMLU items are functionally unstable across model generations under ETS~C classification, with the instability persisting within every subject domain (mean C\\% $= 38.1\\%$) and confirmed non-random by random-split control at 0.18\\% (\\Cref{sec:temporal}).\n\n\\item \\textbf{Ground truth meta-critique} (Claim 2): Web-overlap contamination labels~\\citep{li2024contamination} cannot evaluate item-level differential detectors. The enrichment between DIF flags and web-overlap labels is 0.96 (chance level), exposing a validation methodology gap in the contamination detection literature (\\Cref{sec:groundtruth}).\n\n\\item \\textbf{Semi-synthetic validation framework} (Claim 3): Controlled injection with cross-subject matching achieves $\\Delta\\mathrm{FPR} = 0.000$ while preserving detection power ($\\Delta\\mathrm{TPR} = {+}0.508$ at $p = 0.5$); cross-benchmark replication on GSM8K confirms generality (\\Cref{sec:semisynthetic,sec:gsm8k}).\n\n\\item \\textbf{DIF as diagnostic lens} (Claim 4): DIF-flagged items concentrate discriminative information ($z = -8$ to $-49\\sigma$ vs.\\ random removal) and anti-correlate with the GSM1K contamination gap ($r = -0.478$, suggestive at $N = 33$), indicating that DIF captures item-level behavioral change distinct from simple memorization (\\Cref{sec:downstream,sec:gsm8k}).\n\\end{enumerate}\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_introduction_20260521T042708",
  "tool": "Write",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/introduction.tex",
    "content": "\\section{Introduction}\n\\label{sec:introduction}\n\nWhen we say ``Model B outperforms Model A on MMLU,'' we implicitly assume that the benchmark measures the same construct in the same way for both models. This assumption of temporal comparability underpins every cross-generation comparison published on leaderboards and in model reports, yet it is rarely tested. Applying Mantel-Haenszel Differential Item Functioning (MH-DIF) analysis~\\citep{holland1988mh} with Educational Testing Service (ETS) severity classification to the METABENCH response matrix~\\citep{kipnis2024metabench}, we find that 31\\% of MMLU~\\citep{hendrycks2021mmlu} items receive ETS Category~C classification ($|\\Delta_{\\mathrm{MH}}| \\geq 1.5$, $p < 0.05$), indicating large shifts in item functioning between models released in 2023 and 2024. This is not statistical noise: a random-split control within the 2023 cohort yields only 0.18\\% ETS~C items. The instability persists within every MMLU subject domain, with domain-level C\\% ranging from 31\\% to 45\\% (mean 38.1\\%), and item-level regression shows that 92.4\\% of this instability is unrelated to aggregate domain-level accuracy gains. Nearly one in three MMLU items behaves differently depending on when the evaluated models were trained.\n\nA growing body of contamination detection research has produced sophisticated item-level methods, from membership inference approaches such as Min-K\\%~\\citep{shi2024mink} to performance-based detectors such as ConStat~\\citep{dekoninck2024constat}, DVD~\\citep{liang2026dvd}, and Self-Critique~\\citep{tao2026selfcritique}. These methods validate detection accuracy primarily against web-overlap labels such as those of \\citet{li2024contamination}, which classify benchmark items as contaminated based on verbatim or near-verbatim matches in publicly accessible training corpora. Such labels measure \\emph{global exposure}: whether an item exists in the data ecosystem that all training pipelines can access. They do not measure \\emph{differential item functioning}: whether an item behaves differently across model cohorts that may have had varying degrees of exposure or different training methodologies. \\Cref{fig:global_vs_differential} illustrates the distinction. Most MMLU items are globally contaminated in the sense that they exist in web-accessible text, so all model cohorts encounter them and no differential signal arises. The items that function differentially are those where exposure or training methodology changed asymmetrically across cohorts. Validating differential detectors against global-exposure labels therefore conflates two phenomena, and the near-chance enrichment (0.96) between DIF flags and web-overlap labels is the expected outcome of this mismatch.\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{fig_1_global_vs_differential.pdf}\n\\caption{Global vs.\\ differential contamination, illustrated via Item Characteristic Curves (ICCs). \\textbf{Left}: global contamination produces no DIF; both cohorts encounter the item, and their ICCs overlap. \\textbf{Right}: differential contamination produces DIF; the focal cohort's ICC shifts because only that cohort was disproportionately exposed during training. The enrichment ratio of $\\approx 1.0$ between DIF flags and web-overlap labels is expected because most MMLU items fall into the left category.}\n\\label{fig:global_vs_differential}\n\\end{figure}\n\nWe apply classical MH-DIF with ETS classification to the full METABENCH response matrix (5,227 models $\\times$ 12,508 MMLU items), the largest-scale DIF analysis on LLM benchmarks to date. This psychometric approach is motivated by recent findings that contamination detectors are fragile under post-training~\\citep{wang2026fragility} and by concurrent work using anchor-item calibration for score comparability~\\citep{habba2026growingpains}, which addresses a complementary question (equating scores across cohorts) to ours (characterizing temporal item stability). We initially hypothesized that DIF could identify differentially contaminated items: benchmark questions whose statistical properties shifted because newer models had been trained on them. Semi-synthetic injection experiments confirmed detection capability ($\\Delta\\mathrm{TPR} = {+}0.508$ at exploitation rate $p = 0.5$), and our cross-subject matching protocol eliminated false positive inflation ($\\Delta\\mathrm{FPR} = 0.000$). Three structural refinements (matched-ability quintile analysis, IRT $\\theta$-conditioning, and within-subject bifactor pre-checks) all failed to reduce the temporal C\\% below 31\\%, however. The persistent non-reduction shifted our research question: from whether DIF detects contamination, to what the persistent 31\\% instability reveals about how benchmarks interact with evolving model populations.\n\nA natural tension arises between our headline finding and its practical consequences. On one hand, 31\\% of items are functionally unstable across model generations. On the other, Spearman rank correlation between model rankings computed on all 12,508 items versus stable-only items is $\\rho \\approx 0.997$. The resolution lies in measurement redundancy: MMLU's 12,508 items provide sufficient statistical mass that removing nearly a third does not alter rank order. This is precisely why DIF should be understood as a diagnostic lens (which items changed and for which model families) rather than a quality filter (remove bad items to improve the benchmark). Despite aggregate stability, DIF-flagged items concentrate discriminative signal that differentiates model generations: removing DIF items degrades ranking discriminability more than removing an equal number of random items ($z = -8$ to $-49\\sigma$ across 21 conditions). Individual model families show distinctive DIF profiles: Phi-3 and Llama-3 gain ${+}700$ to ${+}850$ rank positions under stable-item evaluation, while Mistral-based merges lose $-400$ to $-587$ positions.\n\nWe do not modify the MH-DIF procedure itself. The contributions of this work lie in applying it at a scale and in a context where its standard assumptions face new challenges, and in the empirical findings that emerge. At 5,227 models, the analysis exceeds typical educational testing applications by orders of magnitude, requiring careful attention to stratification and matching. Cross-subject matching, a protocol we introduce for semi-synthetic evaluation on multi-subject benchmarks, eliminates false positive inflation entirely ($\\Delta\\mathrm{FPR} = 0.000$). The ground truth analysis exposes a fundamental validation methodology gap: web-overlap labels cannot serve as ground truth for item-level differential detectors because global exposure and differential functioning are distinct phenomena. Cross-benchmark replication on GSM8K with independent contamination validation through the GSM1K held-out set~\\citep{zhang2024gsm1k} confirms that the findings generalize beyond MMLU. We make the following contributions:\n\n\\begin{enumerate}\n\\item \\textbf{Benchmark temporal comparability} (Claim 1): 31\\% of MMLU items are functionally unstable across model generations under ETS~C classification, with the instability persisting within every subject domain (mean C\\% $= 38.1\\%$) and confirmed non-random by random-split control at 0.18\\% (\\Cref{sec:temporal}).\n\n\\item \\textbf{Ground truth meta-critique} (Claim 2): Web-overlap contamination labels~\\citep{li2024contamination} cannot evaluate item-level differential detectors. The enrichment between DIF flags and web-overlap labels is 0.96 (chance level), exposing a validation methodology gap in the contamination detection literature (\\Cref{sec:groundtruth}).\n\n\\item \\textbf{Semi-synthetic validation framework} (Claim 3): Controlled injection with cross-subject matching achieves $\\Delta\\mathrm{FPR} = 0.000$ while preserving detection power ($\\Delta\\mathrm{TPR} = {+}0.508$ at $p = 0.5$); cross-benchmark replication on GSM8K confirms generality (\\Cref{sec:semisynthetic,sec:gsm8k}).\n\n\\item \\textbf{DIF as diagnostic lens} (Claim 4): DIF-flagged items concentrate discriminative information ($z = -8$ to $-49\\sigma$ vs.\\ random removal) and anti-correlate with the GSM1K contamination gap ($r = -0.478$, suggestive at $N = 33$), indicating that DIF captures item-level behavioral change distinct from simple memorization (\\Cref{sec:downstream,sec:gsm8k}).\n\\end{enumerate}\n"
  }
}
```

</details>

---

### Tool result

_source line 26 · 2026-05-21T04:32:55.857051+00:00_

The file /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/introduction.tex has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_introduction_20260521T042708",
  "tool": "Write",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 27 · 2026-05-21T04:32:55.857209+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "—",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/introduction.tex",
  "output_mode": "content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_introduction_20260521T042708",
  "tool": "Grep",
  "tool_args": {
    "pattern": "—",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/introduction.tex",
    "output_mode": "content"
  }
}
```

</details>

---

### Tool result

_source line 28 · 2026-05-21T04:32:55.857342+00:00_

No matches found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_introduction_20260521T042708",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 29 · 2026-05-21T04:32:55.857467+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": " – ",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/introduction.tex",
  "output_mode": "content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_introduction_20260521T042708",
  "tool": "Grep",
  "tool_args": {
    "pattern": " – ",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/introduction.tex",
    "output_mode": "content"
  }
}
```

</details>

---

### Tool result

_source line 30 · 2026-05-21T04:32:55.857589+00:00_

No matches found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_introduction_20260521T042708",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 31 · 2026-05-21T04:32:55.857734+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "(Furthermore|Moreover|Additionally|Notably|It is worth noting|delve|leverage)",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/introduction.tex",
  "output_mode": "content",
  "-i": "True"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_introduction_20260521T042708",
  "tool": "Grep",
  "tool_args": {
    "pattern": "(Furthermore|Moreover|Additionally|Notably|It is worth noting|delve|leverage)",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/introduction.tex",
    "output_mode": "content",
    "-i": "True"
  }
}
```

</details>

---

### Tool result

_source line 32 · 2026-05-21T04:32:55.857880+00:00_

No matches found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_introduction_20260521T042708",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 33 · 2026-05-21T04:32:55.858001+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "ing,|ing\\.",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/introduction.tex",
  "output_mode": "content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_introduction_20260521T042708",
  "tool": "Grep",
  "tool_args": {
    "pattern": "ing,|ing\\.",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/introduction.tex",
    "output_mode": "content"
  }
}
```

</details>

---

### Tool result

_source line 34 · 2026-05-21T04:32:55.858118+00:00_

11:[Omitted long matching line]
15:[Omitted long matching line]
19:[Omitted long matching line]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_introduction_20260521T042708",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 35 · 2026-05-21T04:32:55.858233+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "ing,|ing\\.",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/introduction.tex",
  "output_mode": "content",
  "-n": "True"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_introduction_20260521T042708",
  "tool": "Grep",
  "tool_args": {
    "pattern": "ing,|ing\\.",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/introduction.tex",
    "output_mode": "content",
    "-n": "True"
  }
}
```

</details>

---

### Tool result

_source line 36 · 2026-05-21T04:32:55.858348+00:00_

11:[Omitted long matching line]
15:[Omitted long matching line]
19:[Omitted long matching line]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_introduction_20260521T042708",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 37 · 2026-05-21T04:32:55.858461+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/introduction.tex",
  "offset": "9",
  "limit": "12"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_introduction_20260521T042708",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/introduction.tex",
    "offset": "9",
    "limit": "12"
  }
}
```

</details>

---

### Tool result

_source line 38 · 2026-05-21T04:32:55.858597+00:00_

9	\centering
10	\includegraphics[width=\columnwidth]{fig_1_global_vs_differential.pdf}
11	\caption{Global vs.\ differential contamination, illustrated via Item Characteristic Curves (ICCs). \textbf{Left}: global contamination produces no DIF; both cohorts encounter the item, and their ICCs overlap. \textbf{Right}: differential contamination produces DIF; the focal cohort's ICC shifts because only that cohort was disproportionately exposed during training. The enrichment ratio of $\approx 1.0$ between DIF flags and web-overlap labels is expected because most MMLU items fall into the left category.}
12	\label{fig:global_vs_differential}
13	\end{figure}
14	
15	We apply classical MH-DIF with ETS classification to the full METABENCH response matrix (5,227 models $\times$ 12,508 MMLU items), the largest-scale DIF analysis on LLM benchmarks to date. This psychometric approach is motivated by recent findings that contamination detectors are fragile under post-training~\citep{wang2026fragility} and by concurrent work using anchor-item calibration for score comparability~\citep{habba2026growingpains}, which addresses a complementary question (equating scores across cohorts) to ours (characterizing temporal item stability). We initially hypothesized that DIF could identify differentially contaminated items: benchmark questions whose statistical properties shifted because newer models had been trained on them. Semi-synthetic injection experiments confirmed detection capability ($\Delta\mathrm{TPR} = {+}0.508$ at exploitation rate $p = 0.5$), and our cross-subject matching protocol eliminated false positive inflation ($\Delta\mathrm{FPR} = 0.000$). Three structural refinements (matched-ability quintile analysis, IRT $\theta$-conditioning, and within-subject bifactor pre-checks) all failed to reduce the temporal C\% below 31\%, however. The persistent non-reduction shifted our research question: from whether DIF detects contamination, to what the persistent 31\% instability revea
…[truncated 2246 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_introduction_20260521T042708",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 39 · 2026-05-21T04:32:55.858808+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/introduction.tex",
  "old_string": "At 5,227 models, the analysis exceeds typical educational testing applications by orders of magnitude, requiring careful attention to stratification and matching.",
  "new_string": "At 5,227 models, the analysis exceeds typical educational testing applications by orders of magnitude and requires careful attention to stratification and matching."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_introduction_20260521T042708",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/introduction.tex",
    "old_string": "At 5,227 models, the analysis exceeds typical educational testing applications by orders of magnitude, requiring careful attention to stratification and matching.",
    "new_string": "At 5,227 models, the analysis exceeds typical educational testing applications by orders of magnitude and requires careful attention to stratification and matching."
  }
}
```

</details>

---

### Tool result

_source line 40 · 2026-05-21T04:32:55.858977+00:00_

The file /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/introduction.tex has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_introduction_20260521T042708",
  "tool": "Edit",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 41 · 2026-05-21T04:32:55.859119+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/introduction.tex | sed 's/\\\\[a-zA-Z]*{//g; s/\\\\[a-zA-Z]*//g; s/[{}$~]//g; s/%.*//g' | wc -w",
  "description": "Approximate word count of introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_introduction_20260521T042708",
  "tool": "Bash",
  "tool_args": {
    "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/introduction.tex | sed 's/\\\\[a-zA-Z]*{//g; s/\\\\[a-zA-Z]*//g; s/[{}$~]//g; s/%.*//g' | wc -w",
    "description": "Approximate word count of introduction.tex"
  }
}
```

</details>

---

### Tool result

_source line 42 · 2026-05-21T04:32:55.859242+00:00_

571

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_introduction_20260521T042708",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 43 · 2026-05-21T04:32:55.859373+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "wc -w /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/introduction.tex",
  "description": "Raw word count of introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_introduction_20260521T042708",
  "tool": "Bash",
  "tool_args": {
    "command": "wc -w /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/introduction.tex",
    "description": "Raw word count of introduction.tex"
  }
}
```

</details>

---

### Tool result

_source line 44 · 2026-05-21T04:32:55.859499+00:00_

1041 /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/introduction.tex

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_introduction_20260521T042708",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 45 · 2026-05-21T04:32:55.859617+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/introduction.tex | perl -pe 's/\\\\(?:begin|end|label|Cref|cref|citep?|textbf|emph|includegraphics|caption|centering|section)\\{[^}]*\\}//g; s/\\\\[a-zA-Z]+//g; s/\\$[^$]*\\$//g; s/[{}%~]//g; s/\\s+/ /g' | wc -w",
  "description": "Better word count stripping LaTeX markup"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_introduction_20260521T042708",
  "tool": "Bash",
  "tool_args": {
    "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/introduction.tex | perl -pe 's/\\\\(?:begin|end|label|Cref|cref|citep?|textbf|emph|includegraphics|caption|centering|section)\\{[^}]*\\}//g; s/\\\\[a-zA-Z]+//g; s/\\$[^$]*\\$//g; s/[{}%~]//g; s/\\s+/ /g' | wc -w",
    "description": "Better word count stripping LaTeX markup"
  }
}
```

</details>

---

### Tool result

_source line 46 · 2026-05-21T04:32:55.859754+00:00_

Unmatched [ in regex; marked by <-- HERE in m/\$[ <-- HERE ^5.040001*\$/ at -e line 1, <> line 1.
0

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_introduction_20260521T042708",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 47 · 2026-05-21T04:32:55.859877+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "detex /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/introduction.tex 2>/dev/null | wc -w || echo \"detex not available; using texcount\"; texcount -1 -sum /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/introduction.tex 2>/dev/null || echo \"texcount not available\"",
  "description": "Count words using detex or texcount"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_introduction_20260521T042708",
  "tool": "Bash",
  "tool_args": {
    "command": "detex /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/introduction.tex 2>/dev/null | wc -w || echo \"detex not available; using texcount\"; texcount -1 -sum /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/introduction.tex 2>/dev/null || echo \"texcount not available\"",
    "description": "Count words using detex or texcount"
  }
}
```

</details>

---

### Tool result

_source line 48 · 2026-05-21T04:32:55.859996+00:00_

1010
texcount not available

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_introduction_20260521T042708",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 49 · 2026-05-21T04:32:55.860160+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_introduction_20260521T042708",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/introduction.tex"
  }
}
```

</details>

---

### Tool result

_source line 50 · 2026-05-21T04:32:55.860334+00:00_

1	\section{Introduction}
2	\label{sec:introduction}
3	
4	When we say ``Model B outperforms Model A on MMLU,'' we implicitly assume that the benchmark measures the same construct in the same way for both models. This assumption of temporal comparability underpins every cross-generation comparison published on leaderboards and in model reports, yet it is rarely tested. Applying Mantel-Haenszel Differential Item Functioning (MH-DIF) analysis~\citep{holland1988mh} with Educational Testing Service (ETS) severity classification to the METABENCH response matrix~\citep{kipnis2024metabench}, we find that 31\% of MMLU~\citep{hendrycks2021mmlu} items receive ETS Category~C classification ($|\Delta_{\mathrm{MH}}| \geq 1.5$, $p < 0.05$), indicating large shifts in item functioning between models released in 2023 and 2024. This is not statistical noise: a random-split control within the 2023 cohort yields only 0.18\% ETS~C items. The instability persists within every MMLU subject domain, with domain-level C\% ranging from 31\% to 45\% (mean 38.1\%), and item-level regression shows that 92.4\% of this instability is unrelated to aggregate domain-level accuracy gains. Nearly one in three MMLU items behaves differently depending on when the evaluated models were trained.
5	
6	A growing body of contamination detection research has produced sophisticated item-level methods, from membership inference approaches such as Min-K\%~\citep{shi2024mink} to performance-based detectors such as ConStat~\citep{dekoninck2024constat}, DVD~\citep{liang2026dvd}, and Self-Critique~\citep{tao2026selfcritique}. These methods validate detection accuracy primarily against web-overlap labels such as those of \citet{li2024contamination}, which classify benchmark items as contaminated based on verbatim or near-verbatim matches in publicly accessible training corpora. Such labels measure \emph{global exposure}: whether an item exists in the data ecosystem that all training pipelines can access. They do not me
…[truncated 6468 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_introduction_20260521T042708",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 51 · 2026-05-21T04:32:55.860533+00:00_

Introduction written to `paper/sections/introduction.tex` (~1010 words). Structure:

1. **Hook** (P1): 31% MMLU instability finding with random-split control (0.18%) and within-domain persistence (38.1%)
2. **Gap** (P2): Web-overlap labels measure global exposure, not differential functioning; Figure 1 placed here with ICC illustration
3. **Discovery narrative** (P3): Honest pivot from contamination detection hypothesis to benchmark characterization, citing Wang et al. fragility and Habba et al. as motivation/complement
4. **Tension resolution** (P4): 31% instability vs. ρ=0.997 ranking stability, resolved via measurement redundancy; DIF as diagnostic lens with model-family-specific rank shifts
5. **Novelty statement** (P5): Scale, cross-subject matching, ground truth meta-critique, cross-benchmark replication
6. **Contributions list**: 4 numbered claims with section references

All style constraints verified: no em-dashes, no -ing phrase endings, no banned transition words, no LaTeX comments, paragraphs 5-8 sentences, `\centering` instead of `\begin{center}`.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_paper_writing_introduction_20260521T042708"
}
```

</details>

---
