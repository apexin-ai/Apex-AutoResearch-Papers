# paper writing discussion

**Temporal Score Incomparability in LLM Benchmarks: A Large-Scale Psychometric Audit of 5,227 Models** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 29
- **Recorded user turns:** 0
- **Tool calls:** 14
- **Original source:** `logs/chats/worker_paper_writing_discussion_20260521T050016.jsonl`
- **Structured JSON:** [`24b4599c2304977c77c7.json`](../../sessions/24/24b4599c2304977c77c7.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

29 recorded events

### Tool call

_source line 1 · 2026-05-21T05:02:18.975506+00:00_

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
  "session": "worker_paper_writing_discussion_20260521T050016",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/agent-ml-research/skills/global/paper-writing-norms.skill.md"
  }
}
```

</details>

---

### Tool result

_source line 2 · 2026-05-21T05:02:18.976235+00:00_

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
  "session": "worker_paper_writing_discussion_20260521T050016",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-21T05:02:18.976458+00:00_

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
  "session": "worker_paper_writing_discussion_20260521T050016",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/agent-ml-research/skills/global/latex-paper.skill.md"
  }
}
```

</details>

---

### Tool result

_source line 4 · 2026-05-21T05:02:18.976833+00:00_

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
  "session": "worker_paper_writing_discussion_20260521T050016",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-21T05:02:18.977006+00:00_

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
  "session": "worker_paper_writing_discussion_20260521T050016",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/introduction.tex"
  }
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-21T05:02:18.977170+00:00_

1	\section{Introduction}
2	\label{sec:introduction}
3	
4	When we say ``Model B outperforms Model A on MMLU,'' we implicitly assume that the benchmark measures the same construct in the same way for both models. This assumption of temporal comparability underpins every cross-generation comparison published on leaderboards and in model reports, yet it is rarely tested. Applying Mantel-Haenszel Differential Item Functioning (MH-DIF) analysis~\citep{holland1988mh} with Educational Testing Service (ETS) severity classification to the METABENCH response matrix~\citep{kipnis2024metabench}, we find that 31\% of MMLU~\citep{hendrycks2021mmlu} items receive ETS Category~C classification ($|\Delta_{\mathrm{MH}}| \geq 1.5$, $p < 0.05$), indicating large shifts in item functioning between models released in 2023 and 2024. This is not statistical noise: a random-split control within the 2023 cohort yields only 0.18\% ETS~C items. The instability persists within every MMLU subject domain, with domain-level C\% ranging from 31\% to 45\% (mean 38.1\%), and item-level regression shows that 92.4\% of this instability is unrelated to aggregate domain-level accuracy gains. Nearly one in three MMLU items behaves differently depending on when the evaluated models were trained. Crucially, this instability does not threaten benchmark validity: Spearman rank correlation between model rankings computed on all items versus stable-only items is $\rho \approx 0.997$. The instability is diagnostic, not destructive; it reveals which capability dimensions shift across model generations rather than rendering MMLU scores unreliable.
5	
6	A growing body of contamination detection research has produced sophisticated item-level methods, from membership inference approaches such as Min-K\%~\citep{shi2024mink} to performance-based detectors such as ConStat~\citep{dekoninck2024constat}, DVD~\citep{liang2026dvd}, and Self-Critique~\citep{tao2026selfcritique}. These methods validate detection accuracy primar
…[truncated 5879 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_discussion_20260521T050016",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-21T05:02:18.977322+00:00_

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
  "session": "worker_paper_writing_discussion_20260521T050016",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/experiments.tex"
  }
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-21T05:02:18.977536+00:00_

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
  "session": "worker_paper_writing_discussion_20260521T050016",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-21T05:02:18.977688+00:00_

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
  "session": "worker_paper_writing_discussion_20260521T050016",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/method.tex"
  }
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-21T05:02:18.977889+00:00_

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
…[truncated 8923 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_discussion_20260521T050016",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-21T05:02:18.978059+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/*.tex",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_discussion_20260521T050016",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/*.tex",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper"
  }
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-21T05:02:18.978181+00:00_

paper/math_commands.tex
paper/main.tex
paper/sections/experiments.tex
paper/sections/appendix.tex
paper/sections/abstract.tex
paper/sections/discussion.tex
paper/sections/conclusion.tex
paper/sections/introduction.tex
paper/sections/related_work.tex
paper/sections/method.tex

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_discussion_20260521T050016",
  "tool": "Glob",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-21T05:02:18.978300+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/discussion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_discussion_20260521T050016",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/discussion.tex"
  }
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-21T05:02:18.978421+00:00_

1	% Placeholder for discussion
2	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_discussion_20260521T050016",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-21T05:02:18.978578+00:00_

called Write

<details open><summary>🔧 Tool call — Write</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/discussion.tex",
  "content": "\\section{Discussion}\n\\label{sec:discussion}\n\n\\subsection{Implications for Benchmark Temporal Comparability}\n\\label{sec:disc_temporal}\n\nThe 31\\% ETS~C instability rate is robust across thresholds (10\\% at $|\\Delta_{\\mathrm{MH}}| \\geq 2.5$, rising to 49\\% at $\\geq 1.0$), and three structural controls (\\Cref{sec:structural}) confirm it is not a methodological artifact. This means that cross-generation MMLU score comparisons carry uncontrolled item-level variance: nearly one in three items functions differently depending on when the evaluated model was trained. The instability decomposition (\\Cref{sec:temporal}) sharpens this interpretation. Domain-level accuracy improvement explains only 2.4 percentage points of the 31.3\\% C\\% (pseudo $R^2 = 0.0007$), so 92.4\\% of the instability is unrelated to aggregate capability gains. The items that change are not simply the ones that newer models answer correctly because they are better at a domain; instead, they change in item-specific ways that domain-level trends do not predict.\n\nThis instability does not invalidate MMLU as a ranking instrument. Spearman $\\rho \\approx 0.997$ between full and stable-item rankings confirms that aggregate model ordering is preserved. The instability is diagnostic, not destructive: it identifies which measurement units shift across model generations without rendering the overall score unreliable. Benchmark designers should therefore consider monitoring DIF as a quality diagnostic alongside accuracy metrics. An item pool where C\\% grows over successive model cohorts signals that the benchmark's measurement properties are drifting, even if rank ordering remains intact.\n\n\\subsection{Ground Truth Meta-Critique}\n\\label{sec:disc_groundtruth}\n\nThe near-chance enrichment (0.96) between DIF flags and web-overlap labels raises a question that extends beyond our specific analysis. All prior work that validates item-level contamination detectors against web-overlap or $n$-gram labels faces the same methodological gap: these labels measure whether an item exists in publicly accessible training corpora, not whether exposure differentially affects model behavior. Global exposure is a property of the data ecosystem; differential functioning is a property of how model cohorts interact with individual items. Most MMLU items are globally contaminated in the sense that they appear in web text, so web-overlap labels identify a condition shared by nearly all items rather than one that differentiates model cohorts. Validating differential detectors against such labels conflates two distinct phenomena.\n\nThis observation constitutes a meta-contribution to the contamination detection literature. The enrichment ratio of $\\approx 1.0$ is not evidence that DIF fails; it is the expected outcome when a differential method is evaluated against a global-exposure reference. Semi-synthetic injection confirms that DIF detects differential contamination when present ($\\Delta\\mathrm{TPR} = {+}0.508$ at $p = 0.5$; \\Cref{sec:semisynthetic}). The field needs validation methodologies that match the granularity of the detection task: item-level differential detectors require item-level differential ground truth, not item-level global-exposure labels.\n\n\\subsection{DIF as Diagnostic Lens}\n\\label{sec:disc_diagnostic}\n\n\\paragraph{Capability diagnostic.} The GSM1K correlation ($r = -0.478$, $p = 0.005$, $N = 33$; \\Cref{sec:gsm8k}) provides evidence that DIF-flagged items capture behavioral change distinct from memorization. Models with larger contamination gaps (higher GSM8K minus GSM1K accuracy) benefit \\emph{less} from DIF-C items, the opposite of what a pure memorization account would predict. Of the 249 focal-favoring DIF-C items, 171 have discrimination $\\alpha < 1$, and the negative correlation concentrates in this low-discrimination subset. This pattern suggests that contamination produces a ``shallow'' performance boost on items that DIF does not flag, while DIF-C items capture genuine capability differences that contamination does not confer. Partial correlation ($r = -0.385$, $p = 0.027$) after controlling for overall accuracy confirms that the effect is not an artifact of general model quality. Several caveats apply: the confidence interval is wide (95\\% CI $= [-0.71, -0.16]$), item difficulty as a confound is not fully excluded, and $N = 33$ limits generalizability. This result is suggestive and warrants replication with larger model populations.\n\n\\paragraph{Structural constraints on DIF applicability.} Systematic experimentation reveals three structural constraints that jointly limit DIF utility in LLM benchmarks. First, 1D IRT model fit is imperfect: MMLU's multi-domain structure produces mild local dependence (11.3\\% of within-subject item pairs exceed $|Q3| > 0.20$; \\Cref{sec:structural}), which elevates within-subject DIF rates relative to cross-subject baselines. Second, the power analysis (\\Cref{sec:validation}) establishes minimum requirements of $N \\geq 80$ per cohort and $|\\Delta_{\\mathrm{MH}}| \\geq 1.4$ for reliable detection. Benchmarks with small model populations or modest effect sizes will lack statistical power for DIF analysis. Third, ability differences between temporal cohorts confound the DIF signal: the within-family comparison (Llama-2 vs.\\ Llama-3) produces 61.3\\% C\\%, elevated above the 31.3\\% temporal rate by the large ability gap between model generations. These are structural constraints revealed by our experimentation, not fundamental impossibilities. Higher-level methods (MIMIC models, propensity-score matching, multidimensional IRT) may address individual constraints, and their investigation on LLM benchmark data is a natural next step.\n\n\\subsection{Limitations}\n\\label{sec:disc_limitations}\n\n\\paragraph{(a) Ecological vs.\\ item-level decomposition.} The ecological correlation between subject-level C\\% and accuracy improvement is $\\rho = 0.307$ ($p = 0.02$), but item-level decomposition shows that domain improvement explains only 2.4 percentage points (7.6\\%) of 31.3\\% C\\%. The remaining 92.4\\% cannot be fully attributed to contamination; other sources of capability change (training methodology, data composition, optimization procedures) may contribute, and our analysis does not isolate these factors.\n\n\\paragraph{(b) Instability attribution.} The 31\\% C\\% measures items that function differently across cohorts, but the method does not distinguish contamination from legitimate capability change. DIF identifies \\emph{that} items changed, not \\emph{why}. The semi-synthetic framework validates detection power for one specific mechanism (differential exposure), but real-world instability likely reflects multiple interacting causes.\n\n\\paragraph{(c) Semi-synthetic injection fidelity.} The injection procedure flips incorrect responses to correct at a specified rate, simulating an idealized contamination scenario. Real contamination may manifest as partial knowledge, format memorization, or selective retrieval rather than wholesale answer flipping. The gap between our injection model and realistic contamination mechanisms is unknown.\n\n\\paragraph{(d) Benchmark scope.} The primary analysis covers MMLU with cross-benchmark validation on GSM8K (\\Cref{sec:gsm8k}). GSM8K replication confirms framework portability and provides the GSM1K contamination correlation ($N = 33$), but full temporal DIF characterization on diverse benchmarks (code generation, long-form reasoning, multimodal tasks) has not been conducted. The GSM1K sample ($N = 33$) produces wide confidence intervals that limit the precision of the negative correlation estimate.\n\n\\paragraph{(e) Cross-subject baseline false positive rate.} The cross-subject matching protocol achieves $\\Delta\\mathrm{FPR} = 0.000$ for injected contamination but does not reduce the baseline temporal FPR of 33--53\\% across subjects. This rate is stable across injection levels, confirming it reflects genuine temporal instability rather than methodological error, but it means that a large fraction of flagged items in temporal comparisons are not attributable to the specific contamination mechanism under test.\n\n\\paragraph{(f) RL model robustness.} Reinforcement learning from human feedback may alter item-level response patterns in ways that differ from pretraining-based contamination. The theoretical motivation for DIF robustness to RL (RL modifies the ability distribution rather than item parameters) is plausible but empirically unvalidated with adequate sample size: METABENCH contains only $N = 13$ models with documented reasoning-RL training.\n\n\\paragraph{(g) Model family coverage.} Downstream impact analysis is limited to families with $N \\geq 20$ models (Llama, Mistral, Qwen, Phi). Among the top 50 rank movers, 49 of 50 belong to the ``unknown'' family category in METABENCH, precluding interpretation of what training choices produce large rank shifts.\n\n\\paragraph{(h) Future directions.} Cross-benchmark generalization to code, multimodal, and long-form reasoning benchmarks would test DIF applicability beyond factual knowledge tasks. RL model cohorts with adequate $N$ would enable empirical validation of the RL robustness hypothesis. MIMIC models and propensity-score matching could address the ability confounding that the current MH-DIF framework does not fully resolve.\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_discussion_20260521T050016",
  "tool": "Write",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/discussion.tex",
    "content": "\\section{Discussion}\n\\label{sec:discussion}\n\n\\subsection{Implications for Benchmark Temporal Comparability}\n\\label{sec:disc_temporal}\n\nThe 31\\% ETS~C instability rate is robust across thresholds (10\\% at $|\\Delta_{\\mathrm{MH}}| \\geq 2.5$, rising to 49\\% at $\\geq 1.0$), and three structural controls (\\Cref{sec:structural}) confirm it is not a methodological artifact. This means that cross-generation MMLU score comparisons carry uncontrolled item-level variance: nearly one in three items functions differently depending on when the evaluated model was trained. The instability decomposition (\\Cref{sec:temporal}) sharpens this interpretation. Domain-level accuracy improvement explains only 2.4 percentage points of the 31.3\\% C\\% (pseudo $R^2 = 0.0007$), so 92.4\\% of the instability is unrelated to aggregate capability gains. The items that change are not simply the ones that newer models answer correctly because they are better at a domain; instead, they change in item-specific ways that domain-level trends do not predict.\n\nThis instability does not invalidate MMLU as a ranking instrument. Spearman $\\rho \\approx 0.997$ between full and stable-item rankings confirms that aggregate model ordering is preserved. The instability is diagnostic, not destructive: it identifies which measurement units shift across model generations without rendering the overall score unreliable. Benchmark designers should therefore consider monitoring DIF as a quality diagnostic alongside accuracy metrics. An item pool where C\\% grows over successive model cohorts signals that the benchmark's measurement properties are drifting, even if rank ordering remains intact.\n\n\\subsection{Ground Truth Meta-Critique}\n\\label{sec:disc_groundtruth}\n\nThe near-chance enrichment (0.96) between DIF flags and web-overlap labels raises a question that extends beyond our specific analysis. All prior work that validates item-level contamination detectors against web-overlap or $n$-gram labels faces the same methodological gap: these labels measure whether an item exists in publicly accessible training corpora, not whether exposure differentially affects model behavior. Global exposure is a property of the data ecosystem; differential functioning is a property of how model cohorts interact with individual items. Most MMLU items are globally contaminated in the sense that they appear in web text, so web-overlap labels identify a condition shared by nearly all items rather than one that differentiates model cohorts. Validating differential detectors against such labels conflates two distinct phenomena.\n\nThis observation constitutes a meta-contribution to the contamination detection literature. The enrichment ratio of $\\approx 1.0$ is not evidence that DIF fails; it is the expected outcome when a differential method is evaluated against a global-exposure reference. Semi-synthetic injection confirms that DIF detects differential contamination when present ($\\Delta\\mathrm{TPR} = {+}0.508$ at $p = 0.5$; \\Cref{sec:semisynthetic}). The field needs validation methodologies that match the granularity of the detection task: item-level differential detectors require item-level differential ground truth, not item-level global-exposure labels.\n\n\\subsection{DIF as Diagnostic Lens}\n\\label{sec:disc_diagnostic}\n\n\\paragraph{Capability diagnostic.} The GSM1K correlation ($r = -0.478$, $p = 0.005$, $N = 33$; \\Cref{sec:gsm8k}) provides evidence that DIF-flagged items capture behavioral change distinct from memorization. Models with larger contamination gaps (higher GSM8K minus GSM1K accuracy) benefit \\emph{less} from DIF-C items, the opposite of what a pure memorization account would predict. Of the 249 focal-favoring DIF-C items, 171 have discrimination $\\alpha < 1$, and the negative correlation concentrates in this low-discrimination subset. This pattern suggests that contamination produces a ``shallow'' performance boost on items that DIF does not flag, while DIF-C items capture genuine capability differences that contamination does not confer. Partial correlation ($r = -0.385$, $p = 0.027$) after controlling for overall accuracy confirms that the effect is not an artifact of general model quality. Several caveats apply: the confidence interval is wide (95\\% CI $= [-0.71, -0.16]$), item difficulty as a confound is not fully excluded, and $N = 33$ limits generalizability. This result is suggestive and warrants replication with larger model populations.\n\n\\paragraph{Structural constraints on DIF applicability.} Systematic experimentation reveals three structural constraints that jointly limit DIF utility in LLM benchmarks. First, 1D IRT model fit is imperfect: MMLU's multi-domain structure produces mild local dependence (11.3\\% of within-subject item pairs exceed $|Q3| > 0.20$; \\Cref{sec:structural}), which elevates within-subject DIF rates relative to cross-subject baselines. Second, the power analysis (\\Cref{sec:validation}) establishes minimum requirements of $N \\geq 80$ per cohort and $|\\Delta_{\\mathrm{MH}}| \\geq 1.4$ for reliable detection. Benchmarks with small model populations or modest effect sizes will lack statistical power for DIF analysis. Third, ability differences between temporal cohorts confound the DIF signal: the within-family comparison (Llama-2 vs.\\ Llama-3) produces 61.3\\% C\\%, elevated above the 31.3\\% temporal rate by the large ability gap between model generations. These are structural constraints revealed by our experimentation, not fundamental impossibilities. Higher-level methods (MIMIC models, propensity-score matching, multidimensional IRT) may address individual constraints, and their investigation on LLM benchmark data is a natural next step.\n\n\\subsection{Limitations}\n\\label{sec:disc_limitations}\n\n\\paragraph{(a) Ecological vs.\\ item-level decomposition.} The ecological correlation between subject-level C\\% and accuracy improvement is $\\rho = 0.307$ ($p = 0.02$), but item-level decomposition shows that domain improvement explains only 2.4 percentage points (7.6\\%) of 31.3\\% C\\%. The remaining 92.4\\% cannot be fully attributed to contamination; other sources of capability change (training methodology, data composition, optimization procedures) may contribute, and our analysis does not isolate these factors.\n\n\\paragraph{(b) Instability attribution.} The 31\\% C\\% measures items that function differently across cohorts, but the method does not distinguish contamination from legitimate capability change. DIF identifies \\emph{that} items changed, not \\emph{why}. The semi-synthetic framework validates detection power for one specific mechanism (differential exposure), but real-world instability likely reflects multiple interacting causes.\n\n\\paragraph{(c) Semi-synthetic injection fidelity.} The injection procedure flips incorrect responses to correct at a specified rate, simulating an idealized contamination scenario. Real contamination may manifest as partial knowledge, format memorization, or selective retrieval rather than wholesale answer flipping. The gap between our injection model and realistic contamination mechanisms is unknown.\n\n\\paragraph{(d) Benchmark scope.} The primary analysis covers MMLU with cross-benchmark validation on GSM8K (\\Cref{sec:gsm8k}). GSM8K replication confirms framework portability and provides the GSM1K contamination correlation ($N = 33$), but full temporal DIF characterization on diverse benchmarks (code generation, long-form reasoning, multimodal tasks) has not been conducted. The GSM1K sample ($N = 33$) produces wide confidence intervals that limit the precision of the negative correlation estimate.\n\n\\paragraph{(e) Cross-subject baseline false positive rate.} The cross-subject matching protocol achieves $\\Delta\\mathrm{FPR} = 0.000$ for injected contamination but does not reduce the baseline temporal FPR of 33--53\\% across subjects. This rate is stable across injection levels, confirming it reflects genuine temporal instability rather than methodological error, but it means that a large fraction of flagged items in temporal comparisons are not attributable to the specific contamination mechanism under test.\n\n\\paragraph{(f) RL model robustness.} Reinforcement learning from human feedback may alter item-level response patterns in ways that differ from pretraining-based contamination. The theoretical motivation for DIF robustness to RL (RL modifies the ability distribution rather than item parameters) is plausible but empirically unvalidated with adequate sample size: METABENCH contains only $N = 13$ models with documented reasoning-RL training.\n\n\\paragraph{(g) Model family coverage.} Downstream impact analysis is limited to families with $N \\geq 20$ models (Llama, Mistral, Qwen, Phi). Among the top 50 rank movers, 49 of 50 belong to the ``unknown'' family category in METABENCH, precluding interpretation of what training choices produce large rank shifts.\n\n\\paragraph{(h) Future directions.} Cross-benchmark generalization to code, multimodal, and long-form reasoning benchmarks would test DIF applicability beyond factual knowledge tasks. RL model cohorts with adequate $N$ would enable empirical validation of the RL robustness hypothesis. MIMIC models and propensity-score matching could address the ability confounding that the current MH-DIF framework does not fully resolve.\n"
  }
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-21T05:02:18.978844+00:00_

The file /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/discussion.tex has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_discussion_20260521T050016",
  "tool": "Write",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-21T05:02:18.979004+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections && cat discussion.tex | sed 's/\\\\[a-zA-Z]*{[^}]*}//g; s/\\\\[a-zA-Z]*//g; s/[{}$~]//g; s/%.*//g' | wc -w",
  "description": "Count words in discussion.tex (approximate, stripping LaTeX commands)"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_discussion_20260521T050016",
  "tool": "Bash",
  "tool_args": {
    "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections && cat discussion.tex | sed 's/\\\\[a-zA-Z]*{[^}]*}//g; s/\\\\[a-zA-Z]*//g; s/[{}$~]//g; s/%.*//g' | wc -w",
    "description": "Count words in discussion.tex (approximate, stripping LaTeX commands)"
  }
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-21T05:02:18.979128+00:00_

709

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_discussion_20260521T050016",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-21T05:02:18.979251+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "—|–",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/discussion.tex",
  "output_mode": "content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_discussion_20260521T050016",
  "tool": "Grep",
  "tool_args": {
    "pattern": "—|–",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/discussion.tex",
    "output_mode": "content"
  }
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-21T05:02:18.979371+00:00_

No matches found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_discussion_20260521T050016",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 21 · 2026-05-21T05:02:18.979483+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "ing[.?!]\\s*$|ing\\.\\s*\\\\|ing,\\s*(which|and|or|but|so)",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/discussion.tex",
  "output_mode": "content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_discussion_20260521T050016",
  "tool": "Grep",
  "tool_args": {
    "pattern": "ing[.?!]\\s*$|ing\\.\\s*\\\\|ing,\\s*(which|and|or|but|so)",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/discussion.tex",
    "output_mode": "content"
  }
}
```

</details>

---

### Tool result

_source line 22 · 2026-05-21T05:02:18.979598+00:00_

38:\paragraph{(f) RL model robustness.} Reinforcement learning from human feedback may alter item-level response patterns in ways that differ from pretraining-based contamination. The theoretical motivation for DIF robustness to RL (RL modifies the ability distribution rather than item parameters) is plausible but empirically unvalidated with adequate sample size: METABENCH contains only $N = 13$ models with documented reasoning-RL training.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_discussion_20260521T050016",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 23 · 2026-05-21T05:02:18.979786+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "detex discussion.tex 2>/dev/null | wc -w || (cat discussion.tex | grep -v '^\\s*\\\\' | grep -v '^\\s*%' | sed 's/\\\\[a-zA-Z]*//g; s/[{}$~^]//g; s/\\\\//g' | wc -w)",
  "description": "More accurate word count for discussion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_discussion_20260521T050016",
  "tool": "Bash",
  "tool_args": {
    "command": "detex discussion.tex 2>/dev/null | wc -w || (cat discussion.tex | grep -v '^\\s*\\\\' | grep -v '^\\s*%' | sed 's/\\\\[a-zA-Z]*//g; s/[{}$~^]//g; s/\\\\//g' | wc -w)",
    "description": "More accurate word count for discussion.tex"
  }
}
```

</details>

---

### Tool result

_source line 24 · 2026-05-21T05:02:18.979964+00:00_

1156

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_discussion_20260521T050016",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 25 · 2026-05-21T05:02:18.980108+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "ing[.,]?\\s*$",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/discussion.tex",
  "output_mode": "content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_discussion_20260521T050016",
  "tool": "Grep",
  "tool_args": {
    "pattern": "ing[.,]?\\s*$",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/discussion.tex",
    "output_mode": "content"
  }
}
```

</details>

---

### Tool result

_source line 26 · 2026-05-21T05:02:18.980244+00:00_

38:\paragraph{(f) RL model robustness.} Reinforcement learning from human feedback may alter item-level response patterns in ways that differ from pretraining-based contamination. The theoretical motivation for DIF robustness to RL (RL modifies the ability distribution rather than item parameters) is plausible but empirically unvalidated with adequate sample size: METABENCH contains only $N = 13$ models with documented reasoning-RL training.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_discussion_20260521T050016",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 27 · 2026-05-21T05:02:18.980374+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "(?<!\\\\)%",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/discussion.tex",
  "output_mode": "content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_discussion_20260521T050016",
  "tool": "Grep",
  "tool_args": {
    "pattern": "(?<!\\\\)%",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/discussion.tex",
    "output_mode": "content"
  }
}
```

</details>

---

### Tool result

_source line 28 · 2026-05-21T05:02:18.980487+00:00_

No matches found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_discussion_20260521T050016",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 29 · 2026-05-21T05:02:18.980635+00:00_

Discussion 章节已写入 `paper/sections/discussion.tex`。

验证结果：
- 约 1,156 words（detex 统计），略超 1000 目标，主要因为 Limitations 8 个子段按要求全部展开
- 无 em-dash / en-dash
- 无 -ing 分词短语结尾句
- 无 LaTeX comments
- 4 个 subsection 结构完整：§5.1 Temporal Comparability, §5.2 Ground Truth Meta-Critique, §5.3 DIF as Diagnostic Lens, §5.4 Limitations (a)-(h)
- 所有关键数字与 introduction.tex / experiments.tex 保持一致
- "instability ≠ invalidity" 在 §5.1 明确强化
- 无 pivot 叙事，全程从 benchmark temporal comparability 视角

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_paper_writing_discussion_20260521T050016"
}
```

</details>

---
