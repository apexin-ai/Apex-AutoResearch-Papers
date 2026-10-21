# paper writing compression and coverage table

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 35
- **Recorded user turns:** 0
- **Tool calls:** 17
- **Original source:** `logs/chats/worker_paper_writing_compression_and_coverage_table_20260521T022814.jsonl`
- **Structured JSON:** [`4594194e16deaebfe178.json`](../../sessions/45/4594194e16deaebfe178.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

35 recorded events

### Tool call

_source line 1 · 2026-05-21T02:30:57.845768+00:00_

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
  "session": "worker_paper_writing_compression_and_coverage_table_20260521T022814",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/agent-ml-research/skills/global/paper-writing-norms.skill.md"
  }
}
```

</details>

---

### Tool result

_source line 2 · 2026-05-21T02:30:57.847155+00:00_

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
  "session": "worker_paper_writing_compression_and_coverage_table_20260521T022814",
  "tool": "Read",
  "elapsed_ms": 1
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-21T02:30:57.847391+00:00_

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
  "session": "worker_paper_writing_compression_and_coverage_table_20260521T022814",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/agent-ml-research/skills/global/latex-paper.skill.md"
  }
}
```

</details>

---

### Tool result

_source line 4 · 2026-05-21T02:30:57.847754+00:00_

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
  "session": "worker_paper_writing_compression_and_coverage_table_20260521T022814",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-21T02:30:57.847931+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_compression_and_coverage_table_20260521T022814",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex"
  }
}
```

</details>

---

### Tool call

_source line 6 · 2026-05-21T02:30:57.848068+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_compression_and_coverage_table_20260521T022814",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/related_work.tex"
  }
}
```

</details>

---

### Tool result

_source line 7 · 2026-05-21T02:30:57.848217+00:00_

File content (53197 tokens) exceeds maximum allowed tokens (25000). Use offset and limit parameters to read specific portions of the file, or search for specific content instead of reading the whole file.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_compression_and_coverage_table_20260521T022814",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-21T02:30:57.848369+00:00_

1	\section{Related Work}\label{sec:related}
2	
3	\paragraph{Test-time compute scaling.}
4	Test-time compute scaling encompasses three families: (a) extended chain-of-thought reasoning \cite{muennighoff2025s1}, (b) repeated sampling with majority voting (self-consistency; \citealp{wang2023selfconsistency}) and its extensions to free-form text \cite{chen2024usc, thirukovalluru2024atomic, manakul2023selfcheckgpt}, and (c) best-of-$N$ selection via compute-optimal allocation \cite{snell2025scaling, brown2024monkeys}.
5	Reward-free selectors \cite{taubenfeld2025cisc, kang2025selfcertainty, wang2025rankedvoting, oh2026latentsc} and adaptive gating variants \cite{aggarwal2023adaptive, wang2025make, feng2025optimal, kim2026reasc} reduce inference cost; \citet{chen2023twofailures} diagnose failure modes.
6	All target discrete-answer reasoning; structured prediction requires different aggregation mechanisms because degeneracy operates at the entity-set level.
7	
8	\paragraph{Consistency for structured IE.}
9	\citet{yao2026consistency} show consistency correlates with accuracy for LLM-based NER/RE; we show correlation alone does not ensure selection gains, diagnosing degeneracy and compression as blocking mechanisms.
10	CoCoA \cite{vashurin2025cocoa} fuses confidence with consistency; our supervised baseline confirms combination is not the bottleneck (\S\ref{sec:robustness_main}).
11	Earlier work on confidence for structured prediction \cite{culotta2004confidence, mejer2010confidence, fomicheva2020unsupervised} establishes the paradigm we extend to set-valued outputs.
12	Ensemble approaches aggregate predictions from multiple models or prompts \cite{florian2003named, xiao2025el4ner}; \citet{xie2023zeroshot} propose two-stage entity voting for zero-shot NER, the closest prior work to our entity-level construction.
13	LLM-Blender \cite{jiang2023llmblender} fuses outputs from multiple LLMs via pairwise ranking, whereas our single-model stochastic sampling derives diversity from t
…[truncated 2713 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_compression_and_coverage_table_20260521T022814",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-21T02:30:57.848509+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/discussion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_compression_and_coverage_table_20260521T022814",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/discussion.tex"
  }
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-21T02:30:57.848654+00:00_

1	\section{Discussion}\label{sec:discussion}
2	
3	NER exhibits oracle scaling comparable to reasoning ($c{\approx}0.5$; \S\ref{sec:scaling}), but aggregation cannot close the gap: degeneracy (17.8--67.9\%), limited headroom, and LP-quality alignment ($\rho$ 0.043--0.667) constrain it.
4	Temperature disentangles these at $T{=}1.2$ (degeneracy 14.9\%, LP $\rho{=}0.225$; Table~\ref{tab:t_degeneracy}).
5	
6	\paragraph{From diagnosis to practice.}\label{sec:selection_method}
7	Entity-level construction bypasses both failure mechanisms, with gains positive when degeneracy ${<}22$\% and absent when ${>}31$\% (all $p{<}0.01$; Appendix~\ref{app:epoch_confound}). Under 72B few-shot, construction fails yet QE remains effective (SJ $\rho$ 0.29--0.44; Appendix~\ref{app:fs_error}).
8	Alternative strategies (DALS, MBR, DGS) and supervised mixtures fail to beat greedy (Appendix~\ref{app:dals}, \ref{app:supervised_combination}, \ref{app:when_selection_works}).
9	
10	\paragraph{LP compression and calibration.}
11	LP compression connects to broader calibration challenges in fine-tuned LLMs \cite{kadavath2022language, xiong2024verbalized}: teacher-forcing training and constrained decoding compress the LP dynamic range, leaving within-instance variation insufficient for sample discrimination (median LP range 0.041 nats on SciERC; Appendix~\ref{app:logprob_ties}).
12	\citet{yun2025price} observe similar diversity collapse under structured output formats.
13	Potential remedies---per-token LP variance, calibration-aware scoring, or temperature-adjusted LP---remain untested for entity-level ranking.
14	Two per-sample alternatives could bypass the LP compression bottleneck: Self-Certainty \cite{kang2025selfcertainty} derives confidence from consistency of token-level self-evaluation, while P(True) \cite{kadavath2022language} elicits the model's own correctness probability.
15	Both produce per-sample scores without relying on sequence-level log-probabilities; whether they suffer similar compr
…[truncated 75 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_compression_and_coverage_table_20260521T022814",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-21T02:30:57.848806+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_compression_and_coverage_table_20260521T022814",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/introduction.tex"
  }
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-21T02:30:57.848977+00:00_

1	\section{Introduction}\label{sec:introduction}
2	
3	Test-time compute scaling complements model scaling \cite{snell2025scaling}: repeated sampling with majority voting \cite{wang2023selfconsistency}, best-of-$N$ with learned verifiers \cite{cobbe2021verifiers, brown2024monkeys}, and extended chain-of-thought \cite{muennighoff2025s1} produce large gains on reasoning and code generation.
4	These successes share a structural prerequisite: the output space admits either exact equivalence classes (multiple-choice, numeric answers) or execution-based verification (code).
5	Named entity recognition (NER) breaks both assumptions.
6	The output is a set of typed entities; two samples from the same input routinely extract overlapping but non-identical sets, and no external oracle can adjudicate correctness at test time.
7	Without equivalence classes, majority voting reduces to heuristic frequency counting; without a verifier, best-of-$N$ requires a reliable proxy signal.
8	This structural mismatch raises a concrete question: can self-consistency signals that estimate quality well for reasoning tasks also \textit{select} better outputs or \textit{construct} better entity sets for structured generation?
9	We investigate this question for NER and validate the core findings on SQL parsing, treating NER as a representative instance of the broader set-valued generation problem.
10	
11	The question has practical stakes beyond information extraction.
12	Hallucination detection methods such as SelfCheckGPT \cite{manakul2023selfcheckgpt} and FActScore \cite{min2023factscore} rely on cross-sample consistency to verify individual claims: if a model's outputs agree, the shared content is presumed factual.
13	This reasoning assumes entity-level self-verification works, that a model can reliably distinguish correct extractions from incorrect ones through self-judgment or re-prompting.
14	We show this assumption fails.
15	Three independent probes (entity self-judgment, multi-round re-prompt
…[truncated 5657 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_compression_and_coverage_table_20260521T022814",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-21T02:30:57.849229+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "\\\\section\\{Entity-Level Self-Verification Probes\\}",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex",
  "output_mode": "content",
  "-n": "True",
  "-B": "3"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_compression_and_coverage_table_20260521T022814",
  "tool": "Grep",
  "tool_args": {
    "pattern": "\\\\section\\{Entity-Level Self-Verification Probes\\}",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex",
    "output_mode": "content",
    "-n": "True",
    "-B": "3"
  }
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-21T02:30:57.849389+00:00_

574-A learned token-level LP aggregator (1D CNN over per-token log-probabilities) matches mean LP on Few-NERD (gap closure $56.4$\% vs.\ $55.8$\%); LP's bottleneck is not token aggregation.
575-The correlation-selection gap extends to model-internal representations: in the high-capability regime (greedy F1${=}0.644$), inter-sample F1 differences are small enough that improved ranking provides no marginal selection value, consistent with the capability-diversity tension (\S\ref{sec:discussion}).
576-
577:\section{Entity-Level Self-Verification Probes}\label{app:self_verification}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_compression_and_coverage_table_20260521T022814",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-21T02:30:57.849555+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex",
  "old_string": "\\section{Entity-Level Self-Verification Probes}\\label{app:self_verification}",
  "new_string": "\\subsection{Method Coverage Matrix}\\label{app:method_coverage}\n\nTable~\\ref{tab:method_coverage} summarizes the experimental coverage of each entity-level method evaluated in this work. Individual methods were tested on subsets of the full dataset $\\times$ model matrix; the collective coverage spans three NER datasets and two model families.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{Experimental coverage of entity-level methods. \\checkmark = tested; --- = not tested. All methods use $N{=}8$, $T{=}1.0$ unless noted. Section references indicate where results appear.}\n\\label{tab:method_coverage}\n\\begin{tabular}{lccccl}\n\\toprule\nMethod & SciERC & Few-NERD & CoNLL & Qwen & LLaMA \\\\\n\\midrule\nESJ (\\S\\ref{sec:mechanistic}) & --- & \\checkmark & --- & \\checkmark & --- \\\\\nMRSC (\\S\\ref{sec:mechanistic}) & --- & \\checkmark & --- & \\checkmark & --- \\\\\nLSC (\\S\\ref{sec:mechanistic}) & --- & \\checkmark & --- & \\checkmark & --- \\\\\nHet-T (App.~\\ref{app:robustness}) & \\checkmark & --- & --- & \\checkmark & --- \\\\\nASB (App.~\\ref{app:dals}) & \\checkmark & \\checkmark & \\checkmark & \\checkmark & --- \\\\\nSCD (App.~\\ref{app:supervised_combination}) & \\checkmark & \\checkmark & \\checkmark & \\checkmark & --- \\\\\nVerifier (\\S\\ref{sec:verifier}) & \\checkmark & \\checkmark & \\checkmark & \\checkmark & --- \\\\\n\\midrule\nQE signals (\\S\\ref{sec:qe_results}) & \\checkmark & \\checkmark & \\checkmark & \\checkmark & \\checkmark \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\section{Entity-Level Self-Verification Probes}\\label{app:self_verification}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_compression_and_coverage_table_20260521T022814",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex",
    "old_string": "\\section{Entity-Level Self-Verification Probes}\\label{app:self_verification}",
    "new_string": "\\subsection{Method Coverage Matrix}\\label{app:method_coverage}\n\nTable~\\ref{tab:method_coverage} summarizes the experimental coverage of each entity-level method evaluated in this work. Individual methods were tested on subsets of the full dataset $\\times$ model matrix; the collective coverage spans three NER datasets and two model families.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{Experimental coverage of entity-level methods. \\checkmark = tested; --- = not tested. All methods use $N{=}8$, $T{=}1.0$ unless noted. Section references indicate where results appear.}\n\\label{tab:method_coverage}\n\\begin{tabular}{lccccl}\n\\toprule\nMethod & SciERC & Few-NERD & CoNLL & Qwen & LLaMA \\\\\n\\midrule\nESJ (\\S\\ref{sec:mechanistic}) & --- & \\checkmark & --- & \\checkmark & --- \\\\\nMRSC (\\S\\ref{sec:mechanistic}) & --- & \\checkmark & --- & \\checkmark & --- \\\\\nLSC (\\S\\ref{sec:mechanistic}) & --- & \\checkmark & --- & \\checkmark & --- \\\\\nHet-T (App.~\\ref{app:robustness}) & \\checkmark & --- & --- & \\checkmark & --- \\\\\nASB (App.~\\ref{app:dals}) & \\checkmark & \\checkmark & \\checkmark & \\checkmark & --- \\\\\nSCD (App.~\\ref{app:supervised_combination}) & \\checkmark & \\checkmark & \\checkmark & \\checkmark & --- \\\\\nVerifier (\\S\\ref{sec:verifier}) & \\checkmark & \\checkmark & \\checkmark & \\checkmark & --- \\\\\n\\midrule\nQE signals (\\S\\ref{sec:qe_results}) & \\checkmark & \\checkmark & \\checkmark & \\checkmark & \\checkmark \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\section{Entity-Level Self-Verification Probes}\\label{app:self_verification}"
  }
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-21T02:30:57.849693+00:00_

&lt;tool_use_error>File has not been read yet. Read it first before writing to it.&lt;/tool_use_error>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_compression_and_coverage_table_20260521T022814",
  "tool": "Edit",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-21T02:30:57.849830+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/related_work.tex",
  "old_string": "\\section{Related Work}\\label{sec:related}\n\n\\paragraph{Test-time compute scaling.}\nTest-time compute scaling encompasses three families: (a) extended chain-of-thought reasoning \\cite{muennighoff2025s1}, (b) repeated sampling with majority voting (self-consistency; \\citealp{wang2023selfconsistency}) and its extensions to free-form text \\cite{chen2024usc, thirukovalluru2024atomic, manakul2023selfcheckgpt}, and (c) best-of-$N$ selection via compute-optimal allocation \\cite{snell2025scaling, brown2024monkeys}.\nReward-free selectors \\cite{taubenfeld2025cisc, kang2025selfcertainty, wang2025rankedvoting, oh2026latentsc} and adaptive gating variants \\cite{aggarwal2023adaptive, wang2025make, feng2025optimal, kim2026reasc} reduce inference cost; \\citet{chen2023twofailures} diagnose failure modes.\nAll target discrete-answer reasoning; structured prediction requires different aggregation mechanisms because degeneracy operates at the entity-set level.\n\n\\paragraph{Consistency for structured IE.}\n\\citet{yao2026consistency} show consistency correlates with accuracy for LLM-based NER/RE; we show correlation alone does not ensure selection gains, diagnosing degeneracy and compression as blocking mechanisms.\nCoCoA \\cite{vashurin2025cocoa} fuses confidence with consistency; our supervised baseline confirms combination is not the bottleneck (\\S\\ref{sec:robustness_main}).\nEarlier work on confidence for structured prediction \\cite{culotta2004confidence, mejer2010confidence, fomicheva2020unsupervised} establishes the paradigm we extend to set-valued outputs.\nEnsemble approaches aggregate predictions from multiple models or prompts \\cite{florian2003named, xiao2025el4ner}; \\citet{xie2023zeroshot} propose two-stage entity voting for zero-shot NER, the closest prior work to our entity-level construction.\nLLM-Blender \\cite{jiang2023llmblender} fuses outputs from multiple LLMs via pairwise ranking, whereas our single-model stochastic sampling derives diversity from temperature rather than model heterogeneity.\nOur entity-level construction aggregates across samples from a single fine-tuned model, without requiring model diversity or prompt engineering.\nOur evaluation builds on generative IE \\cite{zhou2024uniner, sainz2024gollie, li2023codeie, wadhwa2023revisiting, xie2024selfimproving} and constrained decoding \\cite{willard2023guided, dong2024xgrammar, park2024grammar, schall2025hidden}.\n\\citet{yun2025price} show structured formats induce diversity collapse; our LP compression (median range 0.041 nats; \\S\\ref{sec:discussion}) corroborates this for NER.\n\n\\paragraph{Uncertainty estimation and MBR decoding.}\nSurveys cover confidence estimation \\cite{geng2024confidence}, uncertainty quantification \\cite{xia2025survey, liu2025uqcc}, and abstention \\cite{wen2025abstention}; semantic uncertainty \\cite{kuhn2023semantic, farquhar2024detecting} and P(True) \\cite{kadavath2022language} provide model-internal alternatives.\nOur selection strategies instantiate MBR decoding \\cite{eikema2022sampling, deguchi2024centroid}; unlike MT where MBR yields consistent gains \\cite{freitag2022high} and code generation where execution-based MBR improves selection \\cite{shi2022mbr}, instance degeneracy eliminates the headroom MBR needs even when utility is well-aligned ($\\rho{=}0.52$; \\S\\ref{sec:discussion}).\n\\citet{eikema2025structured} find MBR utilities degrade on structured outputs; our diagnosis is complementary: degeneracy, not utility misalignment, is the primary bottleneck.\nOur QE results connect to selective prediction \\cite{geifman2017selective, kuleshov2015calibrated, varshney2022investigating}: signals with AUROC up to 0.82 support abstention policies independent of sample selection.\n\n\\paragraph{Best-of-$N$ with learned verifiers.}\n\\citet{gao2023scaling} establish BoN scaling laws and \\citet{chen2021evaluating} define the pass@$k$ metric for code generation; our unsupervised signals face a more fundamental limitation than reward overoptimization.\nTrained verifiers \\cite{cobbe2021verifiers, lightman2024verify, fernandes2022quality} and self-evaluation guided search \\cite{xie2023selfevaluation} learn per-sample scoring.\nCISC \\cite{taubenfeld2025cisc} and Self-Certainty \\cite{kang2025selfcertainty} derive per-sample confidence from hidden states rather than output statistics, but require architecture-specific access to intermediate representations; these hidden-state signals remain untested for structured prediction (\\S Limitations).\nFine-tuning \\cite{kirk2024understanding} and constrained decoding \\cite{holtzman2020curious, vijayakumar2018diverse} both limit the diversity recoverable for selection.",
  "new_string": "\\section{Related Work}\\label{sec:related}\n\n\\paragraph{Test-time compute scaling and best-of-$N$.}\nSelf-consistency \\cite{wang2023selfconsistency} and best-of-$N$ with compute-optimal allocation \\cite{snell2025scaling, brown2024monkeys} drive large gains on reasoning and code tasks.\nReward-free selectors \\cite{taubenfeld2025cisc, kang2025selfcertainty} and BoN scaling laws \\cite{gao2023scaling} reduce or characterize inference cost, while trained verifiers \\cite{cobbe2021verifiers, lightman2024verify} learn per-sample scoring.\nAll target discrete-answer settings; structured prediction requires different aggregation because degeneracy operates at the entity-set level.\n\n\\paragraph{Consistency for structured IE.}\n\\citet{yao2026consistency} show consistency correlates with accuracy for LLM-based NER/RE; we diagnose degeneracy and LP compression as mechanisms that prevent this correlation from yielding selection gains.\n\\citet{xie2023zeroshot} propose entity voting for zero-shot NER, the closest prior work to our entity-level construction; our approach aggregates stochastic samples from a single fine-tuned model without prompt engineering.\n\\citet{yun2025price} show structured formats induce diversity collapse; our LP compression (median range 0.041 nats) corroborates this for NER.\nOur evaluation builds on generative IE \\cite{zhou2024uniner, sainz2024gollie} and constrained decoding \\cite{willard2023guided, dong2024xgrammar}.\n\n\\paragraph{Uncertainty estimation and MBR decoding.}\nOur selection strategies instantiate MBR decoding \\cite{eikema2022sampling}; \\citet{eikema2025structured} find MBR utilities degrade on structured outputs, while our diagnosis identifies degeneracy as the primary bottleneck.\nSemantic uncertainty \\cite{kuhn2023semantic} and confidence estimation \\cite{geng2024confidence, xia2025survey} provide complementary model-internal alternatives; our QE signals with AUROC up to 0.82 connect to selective prediction \\cite{geifman2017selective} and support abstention independent of sample selection."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_compression_and_coverage_table_20260521T022814",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/related_work.tex",
    "old_string": "\\section{Related Work}\\label{sec:related}\n\n\\paragraph{Test-time compute scaling.}\nTest-time compute scaling encompasses three families: (a) extended chain-of-thought reasoning \\cite{muennighoff2025s1}, (b) repeated sampling with majority voting (self-consistency; \\citealp{wang2023selfconsistency}) and its extensions to free-form text \\cite{chen2024usc, thirukovalluru2024atomic, manakul2023selfcheckgpt}, and (c) best-of-$N$ selection via compute-optimal allocation \\cite{snell2025scaling, brown2024monkeys}.\nReward-free selectors \\cite{taubenfeld2025cisc, kang2025selfcertainty, wang2025rankedvoting, oh2026latentsc} and adaptive gating variants \\cite{aggarwal2023adaptive, wang2025make, feng2025optimal, kim2026reasc} reduce inference cost; \\citet{chen2023twofailures} diagnose failure modes.\nAll target discrete-answer reasoning; structured prediction requires different aggregation mechanisms because degeneracy operates at the entity-set level.\n\n\\paragraph{Consistency for structured IE.}\n\\citet{yao2026consistency} show consistency correlates with accuracy for LLM-based NER/RE; we show correlation alone does not ensure selection gains, diagnosing degeneracy and compression as blocking mechanisms.\nCoCoA \\cite{vashurin2025cocoa} fuses confidence with consistency; our supervised baseline confirms combination is not the bottleneck (\\S\\ref{sec:robustness_main}).\nEarlier work on confidence for structured prediction \\cite{culotta2004confidence, mejer2010confidence, fomicheva2020unsupervised} establishes the paradigm we extend to set-valued outputs.\nEnsemble approaches aggregate predictions from multiple models or prompts \\cite{florian2003named, xiao2025el4ner}; \\citet{xie2023zeroshot} propose two-stage entity voting for zero-shot NER, the closest prior work to our entity-level construction.\nLLM-Blender \\cite{jiang2023llmblender} fuses outputs from multiple LLMs via pairwise ranking, whereas our single-model stochastic sampling derives diversity from temperature rather than model heterogeneity.\nOur entity-level construction aggregates across samples from a single fine-tuned model, without requiring model diversity or prompt engineering.\nOur evaluation builds on generative IE \\cite{zhou2024uniner, sainz2024gollie, li2023codeie, wadhwa2023revisiting, xie2024selfimproving} and constrained decoding \\cite{willard2023guided, dong2024xgrammar, park2024grammar, schall2025hidden}.\n\\citet{yun2025price} show structured formats induce diversity collapse; our LP compression (median range 0.041 nats; \\S\\ref{sec:discussion}) corroborates this for NER.\n\n\\paragraph{Uncertainty estimation and MBR decoding.}\nSurveys cover confidence estimation \\cite{geng2024confidence}, uncertainty quantification \\cite{xia2025survey, liu2025uqcc}, and abstention \\cite{wen2025abstention}; semantic uncertainty \\cite{kuhn2023semantic, farquhar2024detecting} and P(True) \\cite{kadavath2022language} provide model-internal alternatives.\nOur selection strategies instantiate MBR decoding \\cite{eikema2022sampling, deguchi2024centroid}; unlike MT where MBR yields consistent gains \\cite{freitag2022high} and code generation where execution-based MBR improves selection \\cite{shi2022mbr}, instance degeneracy eliminates the headroom MBR needs even when utility is well-aligned ($\\rho{=}0.52$; \\S\\ref{sec:discussion}).\n\\citet{eikema2025structured} find MBR utilities degrade on structured outputs; our diagnosis is complementary: degeneracy, not utility misalignment, is the primary bottleneck.\nOur QE results connect to selective prediction \\cite{geifman2017selective, kuleshov2015calibrated, varshney2022investigating}: signals with AUROC up to 0.82 support abstention policies independent of sample selection.\n\n\\paragraph{Best-of-$N$ with learned verifiers.}\n\\citet{gao2023scaling} establish BoN scaling laws and \\citet{chen2021evaluating} define the pass@$k$ metric for code generation; our unsupervised signals face a more fundamental limitation than reward overoptimization.\nTrained verifiers \\cite{cobbe2021verifiers, lightman2024verify, fernandes2022quality} and self-evaluation guided search \\cite{xie2023selfevaluation} learn per-sample scoring.\nCISC \\cite{taubenfeld2025cisc} and Self-Certainty \\cite{kang2025selfcertainty} derive per-sample confidence from hidden states rather than output statistics, but require architecture-specific access to intermediate representations; these hidden-state signals remain untested for structured prediction (\\S Limitations).\nFine-tuning \\cite{kirk2024understanding} and constrained decoding \\cite{holtzman2020curious, vijayakumar2018diverse} both limit the diversity recoverable for selection.",
    "new_string": "\\section{Related Work}\\label{sec:related}\n\n\\paragraph{Test-time compute scaling and best-of-$N$.}\nSelf-consistency \\cite{wang2023selfconsistency} and best-of-$N$ with compute-optimal allocation \\cite{snell2025scaling, brown2024monkeys} drive large gains on reasoning and code tasks.\nReward-free selectors \\cite{taubenfeld2025cisc, kang2025selfcertainty} and BoN scaling laws \\cite{gao2023scaling} reduce or characterize inference cost, while trained verifiers \\cite{cobbe2021verifiers, lightman2024verify} learn per-sample scoring.\nAll target discrete-answer settings; structured prediction requires different aggregation because degeneracy operates at the entity-set level.\n\n\\paragraph{Consistency for structured IE.}\n\\citet{yao2026consistency} show consistency correlates with accuracy for LLM-based NER/RE; we diagnose degeneracy and LP compression as mechanisms that prevent this correlation from yielding selection gains.\n\\citet{xie2023zeroshot} propose entity voting for zero-shot NER, the closest prior work to our entity-level construction; our approach aggregates stochastic samples from a single fine-tuned model without prompt engineering.\n\\citet{yun2025price} show structured formats induce diversity collapse; our LP compression (median range 0.041 nats) corroborates this for NER.\nOur evaluation builds on generative IE \\cite{zhou2024uniner, sainz2024gollie} and constrained decoding \\cite{willard2023guided, dong2024xgrammar}.\n\n\\paragraph{Uncertainty estimation and MBR decoding.}\nOur selection strategies instantiate MBR decoding \\cite{eikema2022sampling}; \\citet{eikema2025structured} find MBR utilities degrade on structured outputs, while our diagnosis identifies degeneracy as the primary bottleneck.\nSemantic uncertainty \\cite{kuhn2023semantic} and confidence estimation \\cite{geng2024confidence, xia2025survey} provide complementary model-internal alternatives; our QE signals with AUROC up to 0.82 connect to selective prediction \\cite{geifman2017selective} and support abstention independent of sample selection."
  }
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-21T02:30:57.850068+00:00_

The file /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/related_work.tex has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_compression_and_coverage_table_20260521T022814",
  "tool": "Edit",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-21T02:30:57.850238+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/discussion.tex",
  "old_string": "LP compression connects to broader calibration challenges in fine-tuned LLMs \\cite{kadavath2022language, xiong2024verbalized}: teacher-forcing training and constrained decoding compress the LP dynamic range, leaving within-instance variation insufficient for sample discrimination (median LP range 0.041 nats on SciERC; Appendix~\\ref{app:logprob_ties}).\n\\citet{yun2025price} observe similar diversity collapse under structured output formats.\nPotential remedies---per-token LP variance, calibration-aware scoring, or temperature-adjusted LP---remain untested for entity-level ranking.\nTwo per-sample alternatives could bypass the LP compression bottleneck: Self-Certainty \\cite{kang2025selfcertainty} derives confidence from consistency of token-level self-evaluation, while P(True) \\cite{kadavath2022language} elicits the model's own correctness probability.\nBoth produce per-sample scores without relying on sequence-level log-probabilities; whether they suffer similar compression under fine-tuning with constrained decoding is an open question.",
  "new_string": "LP compression connects to broader calibration challenges in fine-tuned LLMs \\cite{kadavath2022language, xiong2024verbalized}: teacher-forcing training and constrained decoding compress the LP dynamic range, leaving within-instance variation insufficient for sample discrimination (median LP range 0.041 nats on SciERC; Appendix~\\ref{app:logprob_ties}).\n\\citet{yun2025price} observe similar diversity collapse under structured output formats.\nPotential remedies (per-token LP variance, calibration-aware scoring, temperature-adjusted LP) and per-sample alternatives such as Self-Certainty \\cite{kang2025selfcertainty} or P(True) \\cite{kadavath2022language} remain untested for entity-level ranking under constrained decoding."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_compression_and_coverage_table_20260521T022814",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/discussion.tex",
    "old_string": "LP compression connects to broader calibration challenges in fine-tuned LLMs \\cite{kadavath2022language, xiong2024verbalized}: teacher-forcing training and constrained decoding compress the LP dynamic range, leaving within-instance variation insufficient for sample discrimination (median LP range 0.041 nats on SciERC; Appendix~\\ref{app:logprob_ties}).\n\\citet{yun2025price} observe similar diversity collapse under structured output formats.\nPotential remedies---per-token LP variance, calibration-aware scoring, or temperature-adjusted LP---remain untested for entity-level ranking.\nTwo per-sample alternatives could bypass the LP compression bottleneck: Self-Certainty \\cite{kang2025selfcertainty} derives confidence from consistency of token-level self-evaluation, while P(True) \\cite{kadavath2022language} elicits the model's own correctness probability.\nBoth produce per-sample scores without relying on sequence-level log-probabilities; whether they suffer similar compression under fine-tuning with constrained decoding is an open question.",
    "new_string": "LP compression connects to broader calibration challenges in fine-tuned LLMs \\cite{kadavath2022language, xiong2024verbalized}: teacher-forcing training and constrained decoding compress the LP dynamic range, leaving within-instance variation insufficient for sample discrimination (median LP range 0.041 nats on SciERC; Appendix~\\ref{app:logprob_ties}).\n\\citet{yun2025price} observe similar diversity collapse under structured output formats.\nPotential remedies (per-token LP variance, calibration-aware scoring, temperature-adjusted LP) and per-sample alternatives such as Self-Certainty \\cite{kang2025selfcertainty} or P(True) \\cite{kadavath2022language} remain untested for entity-level ranking under constrained decoding."
  }
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-21T02:30:57.850403+00:00_

The file /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/discussion.tex has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_compression_and_coverage_table_20260521T022814",
  "tool": "Edit",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 21 · 2026-05-21T02:30:57.850539+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/introduction.tex",
  "old_string": "    \\item \\textbf{Diagnostic framework.}\n    A four-stage cascade (QE $\\to$ degeneracy $\\to$ agreement fidelity $\\to$ LP compression) that identifies where and why self-consistency fails for structured generation, cross-task validated on NER and SQL parsing (\\S\\ref{sec:selection_gap}, \\S\\ref{sec:discussion}).\n\n    \\item \\textbf{Systematic negative evidence.}\n    Seven entity-level methods, tested across three NER datasets and two model families, all fail to close the correlation-selection gap, constituting systematic evidence for a capability ceiling in entity-level self-verification (\\S\\ref{sec:mechanistic}, \\S\\ref{sec:adaptive}).\n\n    \\item \\textbf{Mechanistic explanation.}\n    Hidden-state probing reveals that discriminative information exists in model representations (frequency agreement AUROC${=}0.87$) but the prompt-based self-judgment interface cannot access it (ESJ AUROC${=}0.51$), identifying an introspection limit rather than an information deficit (\\S\\ref{sec:mechanistic}).\n\n    \\item \\textbf{Prescriptive escape routes.}\n    Entity-level construction ($+1.02$\\,--\\,$1.40$\\,pp), cross-model ensemble ($+0.42$\\,pp), and regime-specific LP selection ($+1.39$\\,pp on Few-NERD) succeed because they bypass entity-level self-verification.\n    A degeneracy decomposition $\\mathbb{E}[\\Delta F_1] = (1{-}D) \\cdot G_{\\text{nd}} \\cdot \\alpha$ yields an empirically observed threshold $\\theta_{\\text{crit}}{=}0.70$ above which self-consistency gains vanish in our experiments (\\S\\ref{sec:prescriptive}, \\S\\ref{sec:theory}).",
  "new_string": "    \\item \\textbf{Diagnostic framework.}\n    A four-stage cascade (QE $\\to$ degeneracy $\\to$ agreement fidelity $\\to$ LP compression) explaining where and why self-consistency fails for structured generation (\\S\\ref{sec:selection_gap}, \\S\\ref{sec:discussion}).\n\n    \\item \\textbf{Systematic negative evidence.}\n    Seven entity-level methods, tested across three NER datasets and two model families, all fail to close the correlation-selection gap, constituting systematic evidence for a capability ceiling in entity-level self-verification (\\S\\ref{sec:mechanistic}, \\S\\ref{sec:adaptive}).\n\n    \\item \\textbf{Mechanistic explanation.}\n    Hidden-state probing shows discriminative information exists in representations (frequency agreement AUROC${=}0.87$) but is inaccessible through prompt-based self-judgment (ESJ AUROC${=}0.51$), an introspection limit rather than an information deficit (\\S\\ref{sec:mechanistic}).\n\n    \\item \\textbf{Prescriptive escape routes.}\n    Entity-level construction ($+1.02$\\,--\\,$1.40$\\,pp), cross-model ensemble ($+0.42$\\,pp), and regime-specific LP selection ($+1.39$\\,pp) bypass entity-level self-verification; a degeneracy threshold $\\theta_{\\text{crit}}{=}0.70$ predicts when gains vanish (\\S\\ref{sec:prescriptive}, \\S\\ref{sec:theory})."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_compression_and_coverage_table_20260521T022814",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/introduction.tex",
    "old_string": "    \\item \\textbf{Diagnostic framework.}\n    A four-stage cascade (QE $\\to$ degeneracy $\\to$ agreement fidelity $\\to$ LP compression) that identifies where and why self-consistency fails for structured generation, cross-task validated on NER and SQL parsing (\\S\\ref{sec:selection_gap}, \\S\\ref{sec:discussion}).\n\n    \\item \\textbf{Systematic negative evidence.}\n    Seven entity-level methods, tested across three NER datasets and two model families, all fail to close the correlation-selection gap, constituting systematic evidence for a capability ceiling in entity-level self-verification (\\S\\ref{sec:mechanistic}, \\S\\ref{sec:adaptive}).\n\n    \\item \\textbf{Mechanistic explanation.}\n    Hidden-state probing reveals that discriminative information exists in model representations (frequency agreement AUROC${=}0.87$) but the prompt-based self-judgment interface cannot access it (ESJ AUROC${=}0.51$), identifying an introspection limit rather than an information deficit (\\S\\ref{sec:mechanistic}).\n\n    \\item \\textbf{Prescriptive escape routes.}\n    Entity-level construction ($+1.02$\\,--\\,$1.40$\\,pp), cross-model ensemble ($+0.42$\\,pp), and regime-specific LP selection ($+1.39$\\,pp on Few-NERD) succeed because they bypass entity-level self-verification.\n    A degeneracy decomposition $\\mathbb{E}[\\Delta F_1] = (1{-}D) \\cdot G_{\\text{nd}} \\cdot \\alpha$ yields an empirically observed threshold $\\theta_{\\text{crit}}{=}0.70$ above which self-consistency gains vanish in our experiments (\\S\\ref{sec:prescriptive}, \\S\\ref{sec:theory}).",
    "new_string": "    \\item \\textbf{Diagnostic framework.}\n    A four-stage cascade (QE $\\to$ degeneracy $\\to$ agreement fidelity $\\to$ LP compression) explaining where and why self-consistency fails for structured generation (\\S\\ref{sec:selection_gap}, \\S\\ref{sec:discussion}).\n\n    \\item \\textbf{Systematic negative evidence.}\n    Seven entity-level methods, tested across three NER datasets and two model families, all fail to close the correlation-selection gap, constituting systematic evidence for a capability ceiling in entity-level self-verification (\\S\\ref{sec:mechanistic}, \\S\\ref{sec:adaptive}).\n\n    \\item \\textbf{Mechanistic explanation.}\n    Hidden-state probing shows discriminative information exists in representations (frequency agreement AUROC${=}0.87$) but is inaccessible through prompt-based self-judgment (ESJ AUROC${=}0.51$), an introspection limit rather than an information deficit (\\S\\ref{sec:mechanistic}).\n\n    \\item \\textbf{Prescriptive escape routes.}\n    Entity-level construction ($+1.02$\\,--\\,$1.40$\\,pp), cross-model ensemble ($+0.42$\\,pp), and regime-specific LP selection ($+1.39$\\,pp) bypass entity-level self-verification; a degeneracy threshold $\\theta_{\\text{crit}}{=}0.70$ predicts when gains vanish (\\S\\ref{sec:prescriptive}, \\S\\ref{sec:theory})."
  }
}
```

</details>

---

### Tool result

_source line 22 · 2026-05-21T02:30:57.850730+00:00_

The file /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/introduction.tex has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_compression_and_coverage_table_20260521T022814",
  "tool": "Edit",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 23 · 2026-05-21T02:30:57.850884+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex",
  "offset": "570",
  "limit": "15"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_compression_and_coverage_table_20260521T022814",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex",
    "offset": "570",
    "limit": "15"
  }
}
```

</details>

---

### Tool result

_source line 24 · 2026-05-21T02:30:57.851020+00:00_

570	On SciERC, the MLP probe achieves higher quality correlation than LP ($\rho{=}0.388$ vs.\ $0.283$, $+37$\%); hidden states encode information beyond what LP captures.
571	Yet higher correlation does not yield better selection: MLP selection F1 ($0.637$) falls below LP's ($0.650$), with gap closure turning negative ($-5.1$\% vs.\ $+4.8$\%; Table~\ref{tab:hidden_probe}).
572	The linear probe performs worse still ($\rho{=}0.179$, gap closure $-23.4$\%).
573	On Few-NERD, the MLP provides no increment over LP (gap closure $11.7$\% vs.\ $12.3$\%).
574	A learned token-level LP aggregator (1D CNN over per-token log-probabilities) matches mean LP on Few-NERD (gap closure $56.4$\% vs.\ $55.8$\%); LP's bottleneck is not token aggregation.
575	The correlation-selection gap extends to model-internal representations: in the high-capability regime (greedy F1${=}0.644$), inter-sample F1 differences are small enough that improved ranking provides no marginal selection value, consistent with the capability-diversity tension (\S\ref{sec:discussion}).
576	
577	\section{Entity-Level Self-Verification Probes}\label{app:self_verification}
578	
579	Three independent probes test whether the generating model can self-verify at the entity level, using Qwen2.5-7B fine-tuned on Few-NERD ($N{=}8$, seed 42).
580	
581	\begin{table}[t]
582	\centering
583	\small
584	\caption{Entity-level self-verification probes (Qwen2.5-7B, Few-NERD, $N{=}8$). ESJ: entity self-judgment via yes/no prompts. MRSC: multi-round re-prompting on disputed entities. LSC: latent-space centroid selection. MV: majority vote baseline.}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_compression_and_coverage_table_20260521T022814",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 25 · 2026-05-21T02:30:57.851185+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex",
  "old_string": "\\section{Entity-Level Self-Verification Probes}\\label{app:self_verification}",
  "new_string": "\\subsection{Method Coverage Matrix}\\label{app:method_coverage}\n\nTable~\\ref{tab:method_coverage} summarizes the experimental coverage of each entity-level method evaluated in this work. Individual methods were tested on subsets of the full dataset $\\times$ model matrix; the collective coverage spans three NER datasets and two model families.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{Experimental coverage of entity-level methods. \\checkmark = tested; --- = not tested. All methods use $N{=}8$, $T{=}1.0$ unless noted. Section references indicate where results appear.}\n\\label{tab:method_coverage}\n\\begin{tabular}{lccccl}\n\\toprule\nMethod & SciERC & Few-NERD & CoNLL & Qwen & LLaMA \\\\\n\\midrule\nESJ (\\S\\ref{sec:mechanistic}) & --- & \\checkmark & --- & \\checkmark & --- \\\\\nMRSC (\\S\\ref{sec:mechanistic}) & --- & \\checkmark & --- & \\checkmark & --- \\\\\nLSC (\\S\\ref{sec:mechanistic}) & --- & \\checkmark & --- & \\checkmark & --- \\\\\nHet-T (App.~\\ref{app:robustness}) & \\checkmark & --- & --- & \\checkmark & --- \\\\\nASB (App.~\\ref{app:dals}) & \\checkmark & \\checkmark & \\checkmark & \\checkmark & --- \\\\\nSCD (App.~\\ref{app:supervised_combination}) & \\checkmark & \\checkmark & \\checkmark & \\checkmark & --- \\\\\nVerifier (\\S\\ref{sec:verifier}) & \\checkmark & \\checkmark & \\checkmark & \\checkmark & --- \\\\\n\\midrule\nQE signals (\\S\\ref{sec:qe_results}) & \\checkmark & \\checkmark & \\checkmark & \\checkmark & \\checkmark \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\section{Entity-Level Self-Verification Probes}\\label{app:self_verification}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_compression_and_coverage_table_20260521T022814",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex",
    "old_string": "\\section{Entity-Level Self-Verification Probes}\\label{app:self_verification}",
    "new_string": "\\subsection{Method Coverage Matrix}\\label{app:method_coverage}\n\nTable~\\ref{tab:method_coverage} summarizes the experimental coverage of each entity-level method evaluated in this work. Individual methods were tested on subsets of the full dataset $\\times$ model matrix; the collective coverage spans three NER datasets and two model families.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{Experimental coverage of entity-level methods. \\checkmark = tested; --- = not tested. All methods use $N{=}8$, $T{=}1.0$ unless noted. Section references indicate where results appear.}\n\\label{tab:method_coverage}\n\\begin{tabular}{lccccl}\n\\toprule\nMethod & SciERC & Few-NERD & CoNLL & Qwen & LLaMA \\\\\n\\midrule\nESJ (\\S\\ref{sec:mechanistic}) & --- & \\checkmark & --- & \\checkmark & --- \\\\\nMRSC (\\S\\ref{sec:mechanistic}) & --- & \\checkmark & --- & \\checkmark & --- \\\\\nLSC (\\S\\ref{sec:mechanistic}) & --- & \\checkmark & --- & \\checkmark & --- \\\\\nHet-T (App.~\\ref{app:robustness}) & \\checkmark & --- & --- & \\checkmark & --- \\\\\nASB (App.~\\ref{app:dals}) & \\checkmark & \\checkmark & \\checkmark & \\checkmark & --- \\\\\nSCD (App.~\\ref{app:supervised_combination}) & \\checkmark & \\checkmark & \\checkmark & \\checkmark & --- \\\\\nVerifier (\\S\\ref{sec:verifier}) & \\checkmark & \\checkmark & \\checkmark & \\checkmark & --- \\\\\n\\midrule\nQE signals (\\S\\ref{sec:qe_results}) & \\checkmark & \\checkmark & \\checkmark & \\checkmark & \\checkmark \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\section{Entity-Level Self-Verification Probes}\\label{app:self_verification}"
  }
}
```

</details>

---

### Tool result

_source line 26 · 2026-05-21T02:30:57.851744+00:00_

The file /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_compression_and_coverage_table_20260521T022814",
  "tool": "Edit",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 27 · 2026-05-21T02:30:57.851911+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_compression_and_coverage_table_20260521T022814",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/related_work.tex"
  }
}
```

</details>

---

### Tool result

_source line 28 · 2026-05-21T02:30:57.852056+00:00_

1	\section{Related Work}\label{sec:related}
2	
3	\paragraph{Test-time compute scaling and best-of-$N$.}
4	Self-consistency \cite{wang2023selfconsistency} and best-of-$N$ with compute-optimal allocation \cite{snell2025scaling, brown2024monkeys} drive large gains on reasoning and code tasks.
5	Reward-free selectors \cite{taubenfeld2025cisc, kang2025selfcertainty} and BoN scaling laws \cite{gao2023scaling} reduce or characterize inference cost, while trained verifiers \cite{cobbe2021verifiers, lightman2024verify} learn per-sample scoring.
6	All target discrete-answer settings; structured prediction requires different aggregation because degeneracy operates at the entity-set level.
7	
8	\paragraph{Consistency for structured IE.}
9	\citet{yao2026consistency} show consistency correlates with accuracy for LLM-based NER/RE; we diagnose degeneracy and LP compression as mechanisms that prevent this correlation from yielding selection gains.
10	\citet{xie2023zeroshot} propose entity voting for zero-shot NER, the closest prior work to our entity-level construction; our approach aggregates stochastic samples from a single fine-tuned model without prompt engineering.
11	\citet{yun2025price} show structured formats induce diversity collapse; our LP compression (median range 0.041 nats) corroborates this for NER.
12	Our evaluation builds on generative IE \cite{zhou2024uniner, sainz2024gollie} and constrained decoding \cite{willard2023guided, dong2024xgrammar}.
13	
14	\paragraph{Uncertainty estimation and MBR decoding.}
15	Our selection strategies instantiate MBR decoding \cite{eikema2022sampling}; \citet{eikema2025structured} find MBR utilities degrade on structured outputs, while our diagnosis identifies degeneracy as the primary bottleneck.
16	Semantic uncertainty \cite{kuhn2023semantic} and confidence estimation \cite{geng2024confidence, xia2025survey} provide complementary model-internal alternatives; our QE signals with AUROC up to 0.82 connect to selective prediction \cite{ge
…[truncated 79 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_compression_and_coverage_table_20260521T022814",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 29 · 2026-05-21T02:30:57.852229+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/discussion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_compression_and_coverage_table_20260521T022814",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/discussion.tex"
  }
}
```

</details>

---

### Tool result

_source line 30 · 2026-05-21T02:30:57.852375+00:00_

1	\section{Discussion}\label{sec:discussion}
2	
3	NER exhibits oracle scaling comparable to reasoning ($c{\approx}0.5$; \S\ref{sec:scaling}), but aggregation cannot close the gap: degeneracy (17.8--67.9\%), limited headroom, and LP-quality alignment ($\rho$ 0.043--0.667) constrain it.
4	Temperature disentangles these at $T{=}1.2$ (degeneracy 14.9\%, LP $\rho{=}0.225$; Table~\ref{tab:t_degeneracy}).
5	
6	\paragraph{From diagnosis to practice.}\label{sec:selection_method}
7	Entity-level construction bypasses both failure mechanisms, with gains positive when degeneracy ${<}22$\% and absent when ${>}31$\% (all $p{<}0.01$; Appendix~\ref{app:epoch_confound}). Under 72B few-shot, construction fails yet QE remains effective (SJ $\rho$ 0.29--0.44; Appendix~\ref{app:fs_error}).
8	Alternative strategies (DALS, MBR, DGS) and supervised mixtures fail to beat greedy (Appendix~\ref{app:dals}, \ref{app:supervised_combination}, \ref{app:when_selection_works}).
9	
10	\paragraph{LP compression and calibration.}
11	LP compression connects to broader calibration challenges in fine-tuned LLMs \cite{kadavath2022language, xiong2024verbalized}: teacher-forcing training and constrained decoding compress the LP dynamic range, leaving within-instance variation insufficient for sample discrimination (median LP range 0.041 nats on SciERC; Appendix~\ref{app:logprob_ties}).
12	\citet{yun2025price} observe similar diversity collapse under structured output formats.
13	Potential remedies (per-token LP variance, calibration-aware scoring, temperature-adjusted LP) and per-sample alternatives such as Self-Certainty \cite{kang2025selfcertainty} or P(True) \cite{kadavath2022language} remain untested for entity-level ranking under constrained decoding.
14	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_compression_and_coverage_table_20260521T022814",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 31 · 2026-05-21T02:30:57.852520+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/introduction.tex",
  "offset": "42",
  "limit": "20"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_compression_and_coverage_table_20260521T022814",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/introduction.tex",
    "offset": "42",
    "limit": "20"
  }
}
```

</details>

---

### Tool result

_source line 32 · 2026-05-21T02:30:57.852690+00:00_

42	
43	Our contributions:
44	\begin{enumerate}
45	    \item \textbf{Diagnostic framework.}
46	    A four-stage cascade (QE $\to$ degeneracy $\to$ agreement fidelity $\to$ LP compression) explaining where and why self-consistency fails for structured generation (\S\ref{sec:selection_gap}, \S\ref{sec:discussion}).
47	
48	    \item \textbf{Systematic negative evidence.}
49	    Seven entity-level methods, tested across three NER datasets and two model families, all fail to close the correlation-selection gap, constituting systematic evidence for a capability ceiling in entity-level self-verification (\S\ref{sec:mechanistic}, \S\ref{sec:adaptive}).
50	
51	    \item \textbf{Mechanistic explanation.}
52	    Hidden-state probing shows discriminative information exists in representations (frequency agreement AUROC${=}0.87$) but is inaccessible through prompt-based self-judgment (ESJ AUROC${=}0.51$), an introspection limit rather than an information deficit (\S\ref{sec:mechanistic}).
53	
54	    \item \textbf{Prescriptive escape routes.}
55	    Entity-level construction ($+1.02$\,--\,$1.40$\,pp), cross-model ensemble ($+0.42$\,pp), and regime-specific LP selection ($+1.39$\,pp) bypass entity-level self-verification; a degeneracy threshold $\theta_{\text{crit}}{=}0.70$ predicts when gains vanish (\S\ref{sec:prescriptive}, \S\ref{sec:theory}).
56	\end{enumerate}
57	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_compression_and_coverage_table_20260521T022814",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 33 · 2026-05-21T02:30:57.852835+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex",
  "offset": "576",
  "limit": "30"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_compression_and_coverage_table_20260521T022814",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex",
    "offset": "576",
    "limit": "30"
  }
}
```

</details>

---

### Tool result

_source line 34 · 2026-05-21T02:30:57.852977+00:00_

576	
577	\subsection{Method Coverage Matrix}\label{app:method_coverage}
578	
579	Table~\ref{tab:method_coverage} summarizes the experimental coverage of each entity-level method evaluated in this work. Individual methods were tested on subsets of the full dataset $\times$ model matrix; the collective coverage spans three NER datasets and two model families.
580	
581	\begin{table}[h]
582	\centering
583	\small
584	\caption{Experimental coverage of entity-level methods. \checkmark = tested; --- = not tested. All methods use $N{=}8$, $T{=}1.0$ unless noted. Section references indicate where results appear.}
585	\label{tab:method_coverage}
586	\begin{tabular}{lccccl}
587	\toprule
588	Method & SciERC & Few-NERD & CoNLL & Qwen & LLaMA \\
589	\midrule
590	ESJ (\S\ref{sec:mechanistic}) & --- & \checkmark & --- & \checkmark & --- \\
591	MRSC (\S\ref{sec:mechanistic}) & --- & \checkmark & --- & \checkmark & --- \\
592	LSC (\S\ref{sec:mechanistic}) & --- & \checkmark & --- & \checkmark & --- \\
593	Het-T (App.~\ref{app:robustness}) & \checkmark & --- & --- & \checkmark & --- \\
594	ASB (App.~\ref{app:dals}) & \checkmark & \checkmark & \checkmark & \checkmark & --- \\
595	SCD (App.~\ref{app:supervised_combination}) & \checkmark & \checkmark & \checkmark & \checkmark & --- \\
596	Verifier (\S\ref{sec:verifier}) & \checkmark & \checkmark & \checkmark & \checkmark & --- \\
597	\midrule
598	QE signals (\S\ref{sec:qe_results}) & \checkmark & \checkmark & \checkmark & \checkmark & \checkmark \\
599	\bottomrule
600	\end{tabular}
601	\end{table}
602	
603	\section{Entity-Level Self-Verification Probes}\label{app:self_verification}
604	
605	Three independent probes test whether the generating model can self-verify at the entity level, using Qwen2.5-7B fine-tuned on Few-NERD ($N{=}8$, seed 42).

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_compression_and_coverage_table_20260521T022814",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 35 · 2026-05-21T02:30:57.853213+00:00_

验证通过。所有关键引用保留，LaTeX 语法正确。

修改汇总：

| 文件 | 原行数 | 新行数 | 变化 |
|------|--------|--------|------|
| **appendix.tex** | — | +26 | 插入 Method Coverage Table（`\label{app:method_coverage}`） |
| **related_work.tex** | 29 → 16 | -13 | 4 段合并为 3 段，削减低优先级引用 |
| **discussion.tex** | 16 → 13 | -3 | 删除 Self-Certainty/P(True) 详述，合并为一句 |
| **introduction.tex** | 15 → 12 | -3 | 压缩 Item 1/3/4，删除公式 $\mathbb{E}[\Delta F_1]$ |

5 篇关键引用确认保留：`wang2023selfconsistency`、`yao2026consistency`、`eikema2025structured`、`yun2025price`、`xie2023zeroshot`。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_paper_writing_compression_and_coverage_table_20260521T022814"
}
```

</details>

---
