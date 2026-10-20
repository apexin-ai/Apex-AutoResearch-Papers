# paper writing discussion

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 25
- **Recorded user turns:** 0
- **Tool calls:** 12
- **Original source:** `logs/chats/worker_paper_writing_discussion_20260519T050915.jsonl`
- **Structured JSON:** [`8a8a566a2575c79b9a02.json`](../../sessions/8a/8a8a566a2575c79b9a02.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

25 recorded events

### Tool call

_source line 1 · 2026-05-19T05:10:57.474902+00:00_

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
  "session": "worker_paper_writing_discussion_20260519T050915",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/agent-ml-research/skills/global/paper-writing-norms.skill.md"
  }
}
```

</details>

---

### Tool result

_source line 2 · 2026-05-19T05:10:57.475410+00:00_

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
  "session": "worker_paper_writing_discussion_20260519T050915",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-19T05:10:57.475593+00:00_

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
  "session": "worker_paper_writing_discussion_20260519T050915",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/agent-ml-research/skills/global/latex-paper.skill.md"
  }
}
```

</details>

---

### Tool result

_source line 4 · 2026-05-19T05:10:57.475958+00:00_

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
  "session": "worker_paper_writing_discussion_20260519T050915",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-19T05:10:57.476137+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/references.bib"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_discussion_20260519T050915",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/references.bib"
  }
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-19T05:10:57.476409+00:00_

1	% References for SICA Capability Trap paper
2	% Generated from literature_map.yaml — 2026-05-17
3	
4	%%% Theoretical Foundations %%%
5	
6	@book{condorcet1785,
7	  title={Essai sur l'application de l'analyse \`a la probabilit\'e des d\'ecisions rendues \`a la pluralit\'e des voix},
8	  author={de Condorcet, Marie Jean Antoine Nicolas de Caritat},
9	  year={1785},
10	  publisher={Imprimerie Royale},
11	  address={Paris}
12	}
13	
14	@article{austensmith1996,
15	  title={Information Aggregation, Rationality, and the {C}ondorcet Jury Theorem},
16	  author={Austen-Smith, David and Banks, Jeffrey S.},
17	  journal={American Political Science Review},
18	  volume={90},
19	  number={1},
20	  pages={34--45},
21	  year={1996}
22	}
23	
24	@article{ladha1992correlated,
25	  title={The {C}ondorcet Jury Theorem, Free Speech, and Correlated Votes},
26	  author={Ladha, Krishna K.},
27	  journal={American Journal of Political Science},
28	  volume={36},
29	  number={3},
30	  pages={617--634},
31	  year={1992}
32	}
33	
34	@article{fleiss1971kappa,
35	  title={Measuring Nominal Scale Agreement Among Many Raters},
36	  author={Fleiss, Joseph L.},
37	  journal={Psychological Bulletin},
38	  volume={76},
39	  number={5},
40	  pages={378--382},
41	  year={1971}
42	}
43	
44	%%% Self-Consistency and Variants %%%
45	
46	@inproceedings{wang2023sc,
47	  title={Self-Consistency Improves Chain of Thought Reasoning in Language Models},
48	  author={Wang, Xuezhi and Wei, Jason and Schuurmans, Dale and Le, Quoc and Chi, Ed and Narang, Sharan and Chowdhery, Aakanksha and Zhou, Denny},
49	  booktitle={ICLR},
50	  year={2023}
51	}
52	
53	@inproceedings{chen2024usc,
54	  title={Universal Self-Consistency for Large Language Model Generation},
55	  author={Chen, Xinyun and Aksitov, Renat and Alon, Uri and Ren, Jie and Xiao, Kefan and Yin, Pengcheng and Prakash, Sushant and Sutton, Charles and Wang, Xuezhi and Zhou, Denny},
56	  booktitle={ICML},
57	  year={2024}
58	}
59	
60	@inproceedings{taubenfeld2025
…[truncated 14449 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_discussion_20260519T050915",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-19T05:10:57.476600+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "*.tex",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_discussion_20260519T050915",
  "tool": "Glob",
  "tool_args": {
    "pattern": "*.tex",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper"
  }
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-19T05:10:57.476726+00:00_

docs/paper/limitations_content.tex
docs/paper/appendix.tex
docs/paper/abstract.tex
docs/paper/discussion.tex
docs/paper/conclusion.tex
docs/paper/main.tex
docs/paper/experiments.tex
docs/paper/method.tex
docs/paper/related_work.tex
docs/paper/analysis.tex
docs/paper/introduction.tex

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_discussion_20260519T050915",
  "tool": "Glob",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-19T05:10:57.476844+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/discussion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_discussion_20260519T050915",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/discussion.tex"
  }
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-19T05:10:57.477012+00:00_

1	\section{Discussion}
2	\label{sec:discussion}
3	
4	The oracle experiments causally isolate the failure source: replacing only the constraint source while holding all pipeline components fixed yields $+14.22$\,pp on FOLIO ($p = 2.0 \times 10^{-7}$) and $+11.50$\,pp on ProofWriter ($p = 9.21 \times 10^{-15}$). Aggregation is not the bottleneck; constraint extraction quality is. Three failure modes explain why self-extraction works only in a narrow band. Type A (SC $\geq$ $\sim$60\%): consistent traces produce constraints that mirror model answers. Confirmation bias reaches 62.3\% (Qwen2.5-14B), override precision drops to 28.6\%, and only 8.2\% of constraints are Z3-discriminative (95\% CI [7.6, 8.8]). Even ICL with gold FOL examples cannot break this pattern ($\Delta = +0.54$\,pp, n.s.), because the high-accuracy traces themselves lack the diversity that constraints need to exploit. Type C (SC $\leq$ $\sim$40\%): traces are predominantly wrong, so constraints encode incorrect reasoning as formal rules. The solver amplifies rather than corrects these errors ($\Delta = -4.67$\,pp on PW-D5). Type B: domains that resist FOL formalization yield non-discriminative constraints regardless of accuracy. The Goldilocks zone ($\sim$50--55\% SC) requires both sufficient diversity (traces disagree) and partial correctness (some constraints are right). Six remediation strategies all fail to widen this zone (\S\ref{sec:interventions}), confirming the boundaries are structural. Published methods achieving positive results \citep{xu2026dylos, li2025aristotle, wang2025fover, luo2025logicagent} each introduce capabilities beyond the reasoning model itself; trained extractors and external provers remain viable paths to the oracle ceiling.
5	
6	For practitioners, $C_0$ and SC accuracy form a two-dimensional diagnostic. Low $C_0$ ($< 5\%$) indicates degenerate conditions. High $C_0$ with high SC ($\geq$ 60\%) activates the Type A trap. High $C_0$ with very low SC ($\leq$ 40\%) risks Type
…[truncated 291 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_discussion_20260519T050915",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-19T05:10:57.477159+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/abstract.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_discussion_20260519T050915",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/abstract.tex"
  }
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-19T05:10:57.477284+00:00_

1	\begin{abstract}
2	Neuro-symbolic methods extract first-order logic (FOL) constraints from Large Language Model (LLM) reasoning traces to improve answer aggregation beyond majority voting. Whether the reasoning model itself can produce useful constraints through self-extraction remains an open question. We evaluate Symbolic Invariant Consensus Aggregation (SICA), which formulates a weighted partial Maximum Satisfiability (MAX-SAT) problem over self-extracted FOL constraints, across seven models from four base architectures (7B to 32B parameters) on four reasoning domains with more than 2,400 total instances. SICA benefits exist only in a narrow Goldilocks zone ($\sim$50--55\% Self-Consistency): Mistral-7B achieves $+4.90$ percentage points on FOLIO ($p = 0.013$). Outside this band, SICA fails in three distinct ways. Above $\sim$60\% Self-Consistency, confirmation bias causes constraints to mirror model answers, reducing SICA to majority voting (eight conditions, all nonsignificant). Below $\sim$40\%, predominantly incorrect traces produce noisy constraints that actively hurt performance (Mistral-7B on ProofWriter-D5: $\Delta = -4.67$ pp). When domain structure resists formalization, extraction yields no discriminative signal regardless of accuracy. Oracle controls substituting gold FOL annotations yield $+14.22$ and $+11.50$ percentage points (both $p < 0.001$), confirming that aggregation works with discriminative constraints and localizing the bottleneck to extraction quality. Six remediation strategies, including in-context learning with gold FOL examples, all fail to widen this zone. The multi-candidate rate $C_0$ combined with Self-Consistency accuracy provides a two-dimensional deployment diagnostic.
3	\end{abstract}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_discussion_20260519T050915",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-19T05:10:57.477410+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_discussion_20260519T050915",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/introduction.tex"
  }
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-19T05:10:57.477604+00:00_

1	\section{Introduction}\label{sec:introduction}
2	
3	Test-time computation scaling through multiple reasoning samples has emerged as a practical alternative to scaling model parameters \citep{snell2025scaling, guo2025deepseekr1}.
4	The dominant aggregation strategy, Self-Consistency (SC) \citep{wang2023sc}, samples $K$ chain-of-thought traces and selects the majority answer.
5	SC is simple, model-agnostic, and effective across tasks without additional training.
6	It is also hitting a ceiling.
7	\citet{loo2025reevaluating} demonstrate that gains from increasing $K$ plateau and even decline for strong models, a pattern consistent across model families and reasoning tasks.
8	The plateau is consequential: test-time compute is the primary knob available to practitioners who cannot retrain or scale model parameters, and if additional samples stop helping, aggregation-based scaling faces a hard limit.
9	The gap between SC's theoretical promise (independent correct voters converge to truth) and its practical behavior (saturating gains) points to a structural mismatch between the independence assumption underlying majority voting and the correlated nature of same-model traces.
10	
11	Confidence-weighted \citep{taubenfeld2025cisc} and universal \citep{chen2024usc} extensions of SC alleviate this to a degree, but the core limitation persists.
12	Traces sampled from the same model carry correlated errors.
13	When most traces converge on the same (possibly wrong) answer, additional samples provide no new information, and majority voting has no mechanism to correct the shared bias.
14	Trained reward models \citep{lightman2024prm, wang2024mathshepherd} and diversity-aware sampling \citep{diverseaware2026} break this plateau by injecting external signal or controlling trace diversity, but require either trained verifiers or modifications to the sampling procedure.
15	A more fundamental question remains: can \emph{structured aggregation} over symbolic representations extract inform
…[truncated 8763 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_discussion_20260519T050915",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-19T05:10:57.477782+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/experiments.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_discussion_20260519T050915",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/experiments.tex"
  }
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-19T05:10:57.477997+00:00_

1	\section{Experiments}
2	\label{sec:experiments}
3	
4	\subsection{Experimental Setup}
5	\label{sec:exp-setup}
6	
7	We evaluate SICA against Self-Consistency (SC) across seven instruction-tuned and reasoning-specialized models on four reasoning domains, with more than 2,400 evaluation instances.
8	
9	\paragraph{Models.} Qwen2.5-14B-Instruct, Qwen2.5-7B-Instruct, and Qwen3-14B (non-thinking mode)~\citep{yang2024qwen25}, Mistral-7B-Instruct-v0.3~\citep{jiang2023mistral}, LLaMA-3.1-8B-Instruct~\citep{dubey2024llama3}, DeepSeek-R1-Distill-Qwen-7B~\citep{guo2025deepseekr1}, and QwQ-32B~\citep{qwen2024qwq}. Parameter counts range from 7B to 32B.
10	
11	\paragraph{Datasets.} FOLIO~\citep{han2022folio} ($n=204$) provides formal logic problems with gold first-order logic (FOL) annotations for the oracle control (\S\ref{sec:oracle}). ProofWriter~\citep{tafjord2021proofwriter} ($n=600$) tests multi-step deductive reasoning at depth~5. LogiQA~\citep{liu2020logiqa} ($n=200$) evaluates logical reasoning from standardized examinations. StrategyQA~\citep{geva2021strategyqa} ($n=200$) covers commonsense multi-hop reasoning. GSM8K~\citep{cobbe2021gsm8k} ($n=30$) and AIME 2024 ($n=22$) serve as operating-regime probes for the degenerate case ($C_0 < 5\%$).
12	
13	\paragraph{Parameters.} $K=12$ traces at sampling temperature $T=0.7$. Constraint extraction at $T_{\text{ext}}=0.3$ (Appendix~\ref{app:prompts}). Z3~\citep{demoura2008z3} timeout: 10 seconds per problem. Penalty weight $\alpha = 0.5$ in all experiments.
14	
15	\paragraph{Metrics.} Accuracy (\%), $\Delta = \text{SICA} - \text{SC}$ in percentage points (pp). Statistical significance via McNemar exact test at $\alpha = 0.05$; 95\% bootstrap confidence intervals from 10{,}000 resamples for datasets with $n \geq 200$.
16	
17	
18	\subsection{Main Results: A Regime-Dependent Effect}
19	\label{sec:main-results}
20	
21	Table~\ref{tab:main_results} reports accuracy across all model-dataset conditions sorted by SC baseline. SICA effect
…[truncated 10589 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_discussion_20260519T050915",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-19T05:10:57.478152+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/analysis.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_discussion_20260519T050915",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/analysis.tex"
  }
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-19T05:10:57.478334+00:00_

1	\section{Analysis}
2	\label{sec:analysis}
3	
4	The regime-dependent pattern in \S\ref{sec:main-results} and the failure modes in \S\ref{sec:failure-modes} establish \emph{where} SICA succeeds and fails. This section investigates \emph{why}, through six quantitative lenses: trace correlation (\S\ref{sec:effective-k}), extraction quality (\S\ref{sec:extraction-taxonomy}), hyperparameter sensitivity (\S\ref{sec:k-sensitivity}, \S\ref{sec:t-sensitivity}), the entropy structure of gains (\S\ref{sec:entropy}), solver contribution (\S\ref{sec:ablation}), and remediation failure (\S\ref{sec:remediation}).
5	
6	\subsection{Condorcet Effective-K}
7	\label{sec:effective-k}
8	
9	Table~\ref{tab:independence} reports Fleiss' $\kappa$ and the resulting Effective-K (Eq.~\ref{eq:effk}) across model-dataset conditions with $K = 12$ traces. $\kappa$ ranges from 0.21 to 0.82, and the resulting $K_{\text{eff}}$ spans $1.20\text{--}3.63$. The strongest model-dataset pair (Qwen2.5-14B on LogiQA, $\kappa = 0.82$) retains $K_{\text{eff}} = 1.20$: twelve traces carry barely more information than a single sample. Mistral-7B on FOLIO produces moderate agreement ($\kappa = 0.50$ for seed 42, $K_{\text{eff}} = 1.85$), consistent with its position in the Goldilocks zone. Mistral-7B on ProofWriter has the lowest agreement ($\kappa = 0.21$, $K_{\text{eff}} = 3.63$), yet SICA hurts ($\Delta = -2.83$\,pp) because trace quality is too low (SC $= 39.33\%$). High $K_{\text{eff}}$ alone does not guarantee improvement; the model must also produce sufficiently accurate traces. Qwen2.5-14B on FOLIO reaches 58.3\% unanimous problems and 63.0\% on LogiQA; Mistral-7B on FOLIO has only 14.2\%. Unanimous problems leave zero room for constraint-based reranking, and models with high unanimity rates offer SICA a vanishingly small operating window.
10	
11	\begin{table}[t]
12	\centering
13	\small
14	\caption{Trace independence metrics ($K = 12$). $\kappa$: Fleiss' Kappa. $K_{\text{eff}}$: Effective-K (Eq.~\ref{eq:e
…[truncated 9111 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_discussion_20260519T050915",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-19T05:10:57.478501+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/conclusion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_discussion_20260519T050915",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/conclusion.tex"
  }
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-19T05:10:57.478628+00:00_

1	\section{Conclusion}\label{sec:conclusion}
2	
3	We evaluated SICA across seven models (7B--32B) on four reasoning domains ($N > 2{,}400$). Self-extracted constraints help only in a narrow Goldilocks zone ($\sim$50--55\% SC), with three failure modes outside it: confirmation bias at high accuracy (Type A, eight conditions, all n.s.), harmful noise at very low accuracy (Type C, $\Delta = -4.67$\,pp), and non-formalizable domains (Type B). Oracle experiments ($+14.22$\,pp FOLIO, $+11.50$\,pp ProofWriter) confirm aggregation works with discriminative constraints. Six remediation strategies, including ICL with gold FOL examples, all fail to widen this zone.
4	
5	For deployment, $C_0$ and SC accuracy form a two-dimensional diagnostic: low $C_0$ renders SICA degenerate; high $C_0$ with high SC triggers Type A; high $C_0$ with very low SC risks Type C; only moderate SC ($\sim$50--55\%) is favorable, capturing 34.5\% of the oracle ceiling. Trained extractors and external provers remain viable paths to close this gap.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_discussion_20260519T050915",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 21 · 2026-05-19T05:10:57.478829+00:00_

called Write

<details open><summary>🔧 Tool call — Write</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/discussion.tex",
  "content": "\\section{Discussion}\n\\label{sec:discussion}\n\nThe oracle experiments provide a causal identification of the failure source.\nHolding all pipeline components fixed and varying only the constraint source, gold annotations yield $+14.22$\\,pp on FOLIO and $+11.50$\\,pp on ProofWriter (both $p < 0.001$; \\S\\ref{sec:oracle}).\nSelf-extraction captures only 34.5\\% of this ceiling.\nBecause the aggregation mechanism is identical in both conditions, the gap between oracle and self-extracted performance localizes entirely to extraction quality, not to solver limitations or the MAX-SAT formulation.\nThe aggregation mechanism is sound; the constraints are not.\n\nThe Condorcet Jury Theorem predicts that aggregation improves accuracy only when voters contribute independent information \\citep{condorcet1785, ladha1992correlated}.\nEff-$K < 2$ for most conditions (Table~\\ref{tab:independence}) confirms that same-model traces violate this requirement at $K = 12$.\nSymbolic constraints, despite their formal appearance, do not escape this bound.\nThe extraction step maps natural language traces to FOL through the same model distribution, so constraints inherit the correlation structure of the traces that produced them.\nEven symbolic representations, which appear to introduce a qualitatively different signal (formal logic rather than natural language votes), collapse back into the shared model distribution once the extraction is performed by the same model.\nThe independence bottleneck is not about symbolic reasoning as a formalism; it is about self-extraction being unable to introduce information that the model does not already encode in its traces.\n\nNine interventions spanning six dimensions all fail to widen the Goldilocks zone (\\S\\ref{sec:remediation}).\nContrastive prompting reduces discriminativeness from 8.2\\% to 6.0\\%.\nCross-model extraction produces 0\\% discriminative constraints.\nRaising temperature to $T = 1.0$ collapses $\\Delta$ from $+4.90$\\,pp to $+0.49$\\,pp.\nEven in-context learning with gold FOL examples ($\\Delta = +0.50$\\,pp, n.s.) cannot break the confirmation bias pattern.\nThe consistent failure across orthogonal intervention strategies constitutes the strongest evidence that the bottleneck is structural, not an artifact of prompt design or solver configuration.\nIf any single dimension had succeeded, the bottleneck could be attributed to engineering; the uniform failure across all six implicates the self-extraction paradigm itself.\n\nPublished systems that report positive results on logical reasoning each bypass same-model self-extraction.\nDyLoS \\citep{xu2026dylos} composes specialized solvers, Aristotle \\citep{li2025aristotle} applies logic-complete decomposition, FoVer \\citep{wang2025fover} trains dedicated FOL verifiers, and Logic-LM \\citep{pan2023logiclm} routes problems to external provers.\nOur oracle result is consistent with their success: when constraints are discriminative (by whatever mechanism), symbolic aggregation works.\nThe critical difference is the source of constraints, not the aggregation procedure.\nThese systems trade the simplicity of self-extraction for architectures that introduce genuinely independent signal, exactly the property that CJT requires \\citep{ladha1992correlated}.\n\nFor practitioners, $C_0$ (multi-candidate rate) combined with SC accuracy forms a zero-cost deployment diagnostic before any constraint extraction is attempted.\nWhen $C_0 < 5\\%$, SICA reduces to SC by construction (degenerate).\nWhen SC exceeds ${\\sim}60\\%$, confirmation bias renders constraints non-discriminative (Type~A).\nWhen SC falls below ${\\sim}40\\%$, error amplification makes constraints actively harmful (Type~C).\nOnly the narrow band around 50--55\\% SC is favorable, and even there, self-extraction captures barely a third of the oracle ceiling.\nThree paths forward trade simplicity for independence, as CJT predicts is necessary: trained extractors (data-driven), external provers (tool-augmented), and multi-model pipelines (ensemble-based).\nEach introduces a constraint source that is not a deterministic function of the reasoning model's own distribution.\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_discussion_20260519T050915",
  "tool": "Write",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/discussion.tex",
    "content": "\\section{Discussion}\n\\label{sec:discussion}\n\nThe oracle experiments provide a causal identification of the failure source.\nHolding all pipeline components fixed and varying only the constraint source, gold annotations yield $+14.22$\\,pp on FOLIO and $+11.50$\\,pp on ProofWriter (both $p < 0.001$; \\S\\ref{sec:oracle}).\nSelf-extraction captures only 34.5\\% of this ceiling.\nBecause the aggregation mechanism is identical in both conditions, the gap between oracle and self-extracted performance localizes entirely to extraction quality, not to solver limitations or the MAX-SAT formulation.\nThe aggregation mechanism is sound; the constraints are not.\n\nThe Condorcet Jury Theorem predicts that aggregation improves accuracy only when voters contribute independent information \\citep{condorcet1785, ladha1992correlated}.\nEff-$K < 2$ for most conditions (Table~\\ref{tab:independence}) confirms that same-model traces violate this requirement at $K = 12$.\nSymbolic constraints, despite their formal appearance, do not escape this bound.\nThe extraction step maps natural language traces to FOL through the same model distribution, so constraints inherit the correlation structure of the traces that produced them.\nEven symbolic representations, which appear to introduce a qualitatively different signal (formal logic rather than natural language votes), collapse back into the shared model distribution once the extraction is performed by the same model.\nThe independence bottleneck is not about symbolic reasoning as a formalism; it is about self-extraction being unable to introduce information that the model does not already encode in its traces.\n\nNine interventions spanning six dimensions all fail to widen the Goldilocks zone (\\S\\ref{sec:remediation}).\nContrastive prompting reduces discriminativeness from 8.2\\% to 6.0\\%.\nCross-model extraction produces 0\\% discriminative constraints.\nRaising temperature to $T = 1.0$ collapses $\\Delta$ from $+4.90$\\,pp to $+0.49$\\,pp.\nEven in-context learning with gold FOL examples ($\\Delta = +0.50$\\,pp, n.s.) cannot break the confirmation bias pattern.\nThe consistent failure across orthogonal intervention strategies constitutes the strongest evidence that the bottleneck is structural, not an artifact of prompt design or solver configuration.\nIf any single dimension had succeeded, the bottleneck could be attributed to engineering; the uniform failure across all six implicates the self-extraction paradigm itself.\n\nPublished systems that report positive results on logical reasoning each bypass same-model self-extraction.\nDyLoS \\citep{xu2026dylos} composes specialized solvers, Aristotle \\citep{li2025aristotle} applies logic-complete decomposition, FoVer \\citep{wang2025fover} trains dedicated FOL verifiers, and Logic-LM \\citep{pan2023logiclm} routes problems to external provers.\nOur oracle result is consistent with their success: when constraints are discriminative (by whatever mechanism), symbolic aggregation works.\nThe critical difference is the source of constraints, not the aggregation procedure.\nThese systems trade the simplicity of self-extraction for architectures that introduce genuinely independent signal, exactly the property that CJT requires \\citep{ladha1992correlated}.\n\nFor practitioners, $C_0$ (multi-candidate rate) combined with SC accuracy forms a zero-cost deployment diagnostic before any constraint extraction is attempted.\nWhen $C_0 < 5\\%$, SICA reduces to SC by construction (degenerate).\nWhen SC exceeds ${\\sim}60\\%$, confirmation bias renders constraints non-discriminative (Type~A).\nWhen SC falls below ${\\sim}40\\%$, error amplification makes constraints actively harmful (Type~C).\nOnly the narrow band around 50--55\\% SC is favorable, and even there, self-extraction captures barely a third of the oracle ceiling.\nThree paths forward trade simplicity for independence, as CJT predicts is necessary: trained extractors (data-driven), external provers (tool-augmented), and multi-model pipelines (ensemble-based).\nEach introduces a constraint source that is not a deterministic function of the reasoning model's own distribution.\n"
  }
}
```

</details>

---

### Tool result

_source line 22 · 2026-05-19T05:10:57.479046+00:00_

The file /home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/discussion.tex has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_discussion_20260519T050915",
  "tool": "Write",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 23 · 2026-05-19T05:10:57.479197+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "file=\"/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/discussion.tex\" && echo \"=== em-dash ===\" && grep -n \"—\" \"$file\" || echo \"None\" && echo \"=== explanatory en-dash ===\" && grep -n \" – \" \"$file\" || echo \"None\" && echo \"=== -ing phrase endings ===\" && grep -n \"ing\\.\" \"$file\" | grep -v \"\\\\\\\\ref\\|\\\\\\\\cite\\|\\\\\\\\label\\|Goldilocks\\|string\\|sampling\\|reasoning\\|scoring\" || echo \"None\" && echo \"=== Furthermore/Moreover/Additionally ===\" && grep -ni \"furthermore\\|moreover\\|additionally\" \"$file\" || echo \"None\" && echo \"=== Notably/It is worth ===\" && grep -ni \"notably\\|it is worth\" \"$file\" || echo \"None\" && echo \"=== leverage/utilize/delve ===\" && grep -ni \"leverage\\|utilize\\|delve\" \"$file\" || echo \"None\" && echo \"=== Word count ===\" && cat \"$file\" | sed 's/\\\\[a-zA-Z]*{[^}]*}//g; s/[{}$\\\\]//g; s/%.*//g' | wc -w",
  "description": "Check style rules and word count"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_discussion_20260519T050915",
  "tool": "Bash",
  "tool_args": {
    "command": "file=\"/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/discussion.tex\" && echo \"=== em-dash ===\" && grep -n \"—\" \"$file\" || echo \"None\" && echo \"=== explanatory en-dash ===\" && grep -n \" – \" \"$file\" || echo \"None\" && echo \"=== -ing phrase endings ===\" && grep -n \"ing\\.\" \"$file\" | grep -v \"\\\\\\\\ref\\|\\\\\\\\cite\\|\\\\\\\\label\\|Goldilocks\\|string\\|sampling\\|reasoning\\|scoring\" || echo \"None\" && echo \"=== Furthermore/Moreover/Additionally ===\" && grep -ni \"furthermore\\|moreover\\|additionally\" \"$file\" || echo \"None\" && echo \"=== Notably/It is worth ===\" && grep -ni \"notably\\|it is worth\" \"$file\" || echo \"None\" && echo \"=== leverage/utilize/delve ===\" && grep -ni \"leverage\\|utilize\\|delve\" \"$file\" || echo \"None\" && echo \"=== Word count ===\" && cat \"$file\" | sed 's/\\\\[a-zA-Z]*{[^}]*}//g; s/[{}$\\\\]//g; s/%.*//g' | wc -w",
    "description": "Check style rules and word count"
  }
}
```

</details>

---

### Tool result

_source line 24 · 2026-05-19T05:10:57.479330+00:00_

=== em-dash ===
None
=== explanatory en-dash ===
None
=== -ing phrase endings ===
6:Self-extraction captures only 34.5\% of this ceiling.
35:Only the narrow band around 50--55\% SC is favorable, and even there, self-extraction captures barely a third of the oracle ceiling.
=== Furthermore/Moreover/Additionally ===
None
=== Notably/It is worth ===
None
=== leverage/utilize/delve ===
None
=== Word count ===
477

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_discussion_20260519T050915",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 25 · 2026-05-19T05:10:57.479483+00:00_

All style checks pass. The "ceiling" matches are nouns, not participial phrases. 477 words, within the ~500 budget.

Written `discussion.tex` with 5 paragraphs: (1) oracle causal isolation, (2) Condorcet/Eff-K interpretation, (3) remediation failure evidence, (4) why published neuro-symbolic methods succeed, (5) deployment diagnostic and paths forward. All citation keys verified against `references.bib`. No em-dashes, no -ing phrase endings, no banned transitions or words.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_paper_writing_discussion_20260519T050915"
}
```

</details>

---
