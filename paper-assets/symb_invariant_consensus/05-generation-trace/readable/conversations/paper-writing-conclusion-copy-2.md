# paper writing conclusion

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 23
- **Recorded user turns:** 0
- **Tool calls:** 11
- **Original source:** `logs/chats/worker_paper_writing_conclusion_20260519T051953.jsonl`
- **Structured JSON:** [`62fd8db871d82641fd30.json`](../../sessions/62/62fd8db871d82641fd30.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

23 recorded events

### Tool call

_source line 1 · 2026-05-19T05:22:07.244985+00:00_

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
  "session": "worker_paper_writing_conclusion_20260519T051953",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/agent-ml-research/skills/global/latex-paper.skill.md"
  }
}
```

</details>

---

### Tool result

_source line 2 · 2026-05-19T05:22:07.245595+00:00_

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
  "session": "worker_paper_writing_conclusion_20260519T051953",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-19T05:22:07.245774+00:00_

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
  "session": "worker_paper_writing_conclusion_20260519T051953",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/agent-ml-research/skills/global/paper-writing-norms.skill.md"
  }
}
```

</details>

---

### Tool result

_source line 4 · 2026-05-19T05:22:07.246124+00:00_

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
  "session": "worker_paper_writing_conclusion_20260519T051953",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-19T05:22:07.246286+00:00_

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
  "session": "worker_paper_writing_conclusion_20260519T051953",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/abstract.tex"
  }
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-19T05:22:07.246415+00:00_

1	Self-Consistency (SC) majority voting over multiple chain-of-thought traces is the dominant test-time aggregation strategy for large language models (LLMs), but accuracy gains saturate as sample count grows. The Condorcet Jury Theorem (CJT) explains this plateau: same-model traces are correlated voters, so additional samples carry diminishing independent information. Symbolic constraints expressed in first-order logic (FOL) appear to offer a way forward, since formal validity is independent of the generative model. Yet when constraints are extracted by the same model that produces the traces, they inherit the traces' correlation structure. We term this the \emph{independence bottleneck}. We study this bottleneck through Symbolic Invariant Consensus Aggregation (SICA), which extracts FOL constraints from reasoning traces and selects answers via weighted partial MAX-SAT. Evaluating seven models (7B to 32B parameters) across four reasoning domains with over 2,400 instances and three-seed replication, we find that SICA gains are confined to a narrow accuracy regime around 50 to 55\% SC baseline. Outside this zone, constraints either echo the majority (confirmation bias) or amplify errors. Oracle controls with gold FOL annotations confirm the aggregation mechanism is sound, yet self-extraction captures only 35\% of the oracle ceiling. Nine remediation strategies spanning six intervention dimensions all fail to widen the effective zone. The bottleneck is structural: same-model self-extraction cannot supply the independent signal that CJT requires for aggregation to surpass majority voting.
2	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_conclusion_20260519T051953",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-19T05:22:07.246547+00:00_

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
  "session": "worker_paper_writing_conclusion_20260519T051953",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/introduction.tex"
  }
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-19T05:22:07.246712+00:00_

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
  "session": "worker_paper_writing_conclusion_20260519T051953",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-19T05:22:07.246853+00:00_

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
  "session": "worker_paper_writing_conclusion_20260519T051953",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/discussion.tex"
  }
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-19T05:22:07.247037+00:00_

1	\section{Discussion}
2	\label{sec:discussion}
3	
4	The oracle experiments provide a causal identification of the failure source.
5	Holding all pipeline components fixed and varying only the constraint source, gold annotations yield $+14.22$\,pp on FOLIO and $+11.50$\,pp on ProofWriter (both $p < 0.001$; \S\ref{sec:oracle}).
6	Self-extraction captures only 34.5\% of this ceiling.
7	Because the aggregation mechanism is identical in both conditions, the gap between oracle and self-extracted performance localizes entirely to extraction quality, not to solver limitations or the MAX-SAT formulation.
8	The aggregation mechanism is sound; the constraints are not.
9	
10	The Condorcet Jury Theorem predicts that aggregation improves accuracy only when voters contribute independent information \citep{condorcet1785, ladha1992correlated}.
11	Eff-$K < 2$ for most conditions (Table~\ref{tab:independence}) confirms that same-model traces violate this requirement at $K = 12$.
12	Symbolic constraints, despite their formal appearance, do not escape this bound.
13	The extraction step maps natural language traces to FOL through the same model distribution, so constraints inherit the correlation structure of the traces that produced them.
14	Even symbolic representations, which appear to introduce a qualitatively different signal (formal logic rather than natural language votes), collapse back into the shared model distribution once the extraction is performed by the same model.
15	The independence bottleneck is not about symbolic reasoning as a formalism; it is about self-extraction being unable to introduce information that the model does not already encode in its traces.
16	
17	Nine interventions spanning six dimensions all fail to widen the Goldilocks zone (\S\ref{sec:remediation}).
18	Contrastive prompting reduces discriminativeness from 8.2\% to 6.0\%.
19	Cross-model extraction produces 0\% discriminative constraints.
20	Raising temperature to $T = 1.0$ collapses $\Delta$ from $+4
…[truncated 2215 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_conclusion_20260519T051953",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-19T05:22:07.247254+00:00_

called Write

<details open><summary>🔧 Tool call — Write</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/conclusion.tex",
  "content": "\\section{Conclusion}\\label{sec:conclusion}\n\nWe evaluated Symbolic Invariant Consensus Aggregation (SICA) across seven models (7B to 32B parameters), four reasoning domains, and over 2,400 instances with three-seed replication. Grounded in the Condorcet Jury Theorem, our analysis explains why Self-Consistency majority voting saturates and why symbolic constraint aggregation fails to break this plateau under same-model self-extraction.\n\nThe central finding is the independence bottleneck. Same-model traces produce Fleiss' $\\kappa$ values of $0.21$--$0.82$, and the effective sample size compresses to $1.20$--$3.63$ at $K = 12$. Self-extracted FOL constraints inherit this correlation structure. SICA gains are confined to a narrow Goldilocks zone of approximately 50--55\\% SC accuracy, where Mistral-7B on FOLIO achieves $+4.90$\\,pp ($p = 0.013$, significant in 2 of 3 seeds). Outside this zone, confirmation bias renders constraints non-discriminative (Type~A) or error amplification actively degrades accuracy by $-2.83$\\,pp (Type~C).\n\nOracle controls confirm that the aggregation mechanism is sound: gold FOL annotations yield $+14.22$\\,pp on FOLIO and $+11.50$\\,pp on ProofWriter (both $p < 0.001$), yet self-extraction captures only 35\\% of this ceiling. Nine remediation strategies spanning six intervention dimensions all fail to widen the effective zone. The uniform failure confirms the bottleneck is structural rather than an engineering artifact. Sensitivity analysis reinforces this conclusion: $K = 12$ marks the inverted-U peak, and the effect collapses at $T = 1.0$.\n\nFor deployment, $C_0$ combined with SC accuracy provides a zero-cost diagnostic for predicting when symbolic aggregation can help. Three paths forward trade simplicity for independence as CJT requires: trained extractors, external provers, and multi-model pipelines.\n\n\\paragraph{Limitations.} Our evaluation is limited to same-model self-extraction. We do not test trained FOL extractors, external solvers with verified grounding, or multi-model constraint pipelines, all of which may overcome the independence bottleneck.\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_conclusion_20260519T051953",
  "tool": "Write",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/conclusion.tex",
    "content": "\\section{Conclusion}\\label{sec:conclusion}\n\nWe evaluated Symbolic Invariant Consensus Aggregation (SICA) across seven models (7B to 32B parameters), four reasoning domains, and over 2,400 instances with three-seed replication. Grounded in the Condorcet Jury Theorem, our analysis explains why Self-Consistency majority voting saturates and why symbolic constraint aggregation fails to break this plateau under same-model self-extraction.\n\nThe central finding is the independence bottleneck. Same-model traces produce Fleiss' $\\kappa$ values of $0.21$--$0.82$, and the effective sample size compresses to $1.20$--$3.63$ at $K = 12$. Self-extracted FOL constraints inherit this correlation structure. SICA gains are confined to a narrow Goldilocks zone of approximately 50--55\\% SC accuracy, where Mistral-7B on FOLIO achieves $+4.90$\\,pp ($p = 0.013$, significant in 2 of 3 seeds). Outside this zone, confirmation bias renders constraints non-discriminative (Type~A) or error amplification actively degrades accuracy by $-2.83$\\,pp (Type~C).\n\nOracle controls confirm that the aggregation mechanism is sound: gold FOL annotations yield $+14.22$\\,pp on FOLIO and $+11.50$\\,pp on ProofWriter (both $p < 0.001$), yet self-extraction captures only 35\\% of this ceiling. Nine remediation strategies spanning six intervention dimensions all fail to widen the effective zone. The uniform failure confirms the bottleneck is structural rather than an engineering artifact. Sensitivity analysis reinforces this conclusion: $K = 12$ marks the inverted-U peak, and the effect collapses at $T = 1.0$.\n\nFor deployment, $C_0$ combined with SC accuracy provides a zero-cost diagnostic for predicting when symbolic aggregation can help. Three paths forward trade simplicity for independence as CJT requires: trained extractors, external provers, and multi-model pipelines.\n\n\\paragraph{Limitations.} Our evaluation is limited to same-model self-extraction. We do not test trained FOL extractors, external solvers with verified grounding, or multi-model constraint pipelines, all of which may overcome the independence bottleneck.\n"
  }
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-19T05:22:07.247400+00:00_

&lt;tool_use_error>File has not been read yet. Read it first before writing to it.&lt;/tool_use_error>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_conclusion_20260519T051953",
  "tool": "Write",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-19T05:22:07.247517+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/conclusion.tex 2>&1 || echo \"FILE_NOT_EXISTS\"",
  "description": "Check if conclusion.tex exists"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_conclusion_20260519T051953",
  "tool": "Bash",
  "tool_args": {
    "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/conclusion.tex 2>&1 || echo \"FILE_NOT_EXISTS\"",
    "description": "Check if conclusion.tex exists"
  }
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-19T05:22:07.247628+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/conclusion.tex

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_conclusion_20260519T051953",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-19T05:22:07.247737+00:00_

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
  "session": "worker_paper_writing_conclusion_20260519T051953",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/conclusion.tex"
  }
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-19T05:22:07.247859+00:00_

1	\section{Conclusion}\label{sec:conclusion}
2	
3	We evaluated Symbolic Invariant Consensus Aggregation (SICA) across seven models (7B to 32B parameters), four reasoning domains, and more than 2,400 instances with three-seed replication. The Condorcet Jury Theorem provides a precise diagnostic for Self-Consistency's plateau: same-model traces produce Fleiss' $\kappa = 0.21$--$0.82$, compressing the effective ensemble size to $K_{\text{eff}} = 1.20$--$3.63$ for nominal $K = 12$. At $K_{\text{eff}} \approx 1$, additional traces carry almost no new information, and no aggregation method operating on those traces alone can escape the plateau.
4	
5	Self-extracted symbolic constraints do not resolve this bottleneck. SICA gains are confined to a narrow Goldilocks zone (${\sim}$50--55\% SC accuracy), where Mistral-7B achieves $+4.90$\,pp on FOLIO ($p = 0.013$, significant in 2 of 3 seeds). Three failure modes explain the regime boundaries: confirmation bias above ${\sim}$60\% SC (Type~A), error amplification below ${\sim}$40\% ($\Delta = -2.83$\,pp, Type~C), and non-formalizable domains (Type~B). Oracle controls substituting gold FOL annotations yield $+14.22$\,pp on FOLIO and $+11.50$\,pp on ProofWriter (both $p < 0.001$), proving the aggregation mechanism is sound. Self-extraction captures only 35\% of this oracle ceiling. Nine remediation strategies spanning six intervention dimensions all fail to widen the effective zone.
6	
7	The multi-candidate rate $C_0$ combined with SC accuracy provides practitioners a zero-cost deployment diagnostic: when both fall outside the Goldilocks zone, SICA offers no benefit over majority voting. Closing the oracle gap requires constraint sources that are not deterministic functions of the reasoning model's own distribution: trained extractors, external provers, or multi-model pipelines.
8	
9	\paragraph{Limitations.} Our evaluation is restricted to same-model self-extraction. Trained extractors and multi-model ensembles may achieve higher 
…[truncated 218 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_conclusion_20260519T051953",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-19T05:22:07.248070+00:00_

called Write

<details open><summary>🔧 Tool call — Write</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/conclusion.tex",
  "content": "\\section{Conclusion}\\label{sec:conclusion}\n\nWe evaluated Symbolic Invariant Consensus Aggregation (SICA) across seven models (7B to 32B parameters), four reasoning domains, and over 2,400 instances with three-seed replication. Grounded in the Condorcet Jury Theorem, our analysis explains why Self-Consistency majority voting saturates and why symbolic constraint aggregation fails to break this plateau under same-model self-extraction.\n\nThe central finding is the independence bottleneck. Same-model traces produce Fleiss' $\\kappa$ values of $0.21$--$0.82$, and the effective sample size compresses to Eff-$K = 1.20$--$3.63$ at $K = 12$. Self-extracted FOL constraints inherit this correlation structure. SICA gains are confined to a narrow Goldilocks zone of approximately 50--55\\% SC accuracy, where Mistral-7B on FOLIO achieves $+4.90$\\,pp ($p = 0.013$, significant in 2 of 3 seeds). Outside this zone, confirmation bias renders constraints non-discriminative (Type~A) or error amplification actively degrades accuracy by $-2.83$\\,pp (Type~C).\n\nOracle controls confirm that the aggregation mechanism is sound: gold FOL annotations yield $+14.22$\\,pp on FOLIO and $+11.50$\\,pp on ProofWriter (both $p < 0.001$), yet self-extraction captures only 35\\% of this ceiling. Nine remediation strategies spanning six intervention dimensions all fail to widen the effective zone. The uniform failure confirms the bottleneck is structural rather than an engineering artifact. Sensitivity analysis reinforces this conclusion: $K = 12$ marks the inverted-U peak, and the effect collapses at $T = 1.0$.\n\nThe multi-candidate rate $C_0$ combined with SC accuracy provides a zero-cost deployment diagnostic for predicting when symbolic aggregation can help. Three paths forward trade simplicity for independence as CJT requires: trained extractors, external provers, and multi-model pipelines.\n\n\\paragraph{Limitations.} Our evaluation is limited to same-model self-extraction. We do not test trained FOL extractors, external solvers with verified grounding, or multi-model constraint pipelines, all of which may overcome the independence bottleneck.\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_conclusion_20260519T051953",
  "tool": "Write",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/conclusion.tex",
    "content": "\\section{Conclusion}\\label{sec:conclusion}\n\nWe evaluated Symbolic Invariant Consensus Aggregation (SICA) across seven models (7B to 32B parameters), four reasoning domains, and over 2,400 instances with three-seed replication. Grounded in the Condorcet Jury Theorem, our analysis explains why Self-Consistency majority voting saturates and why symbolic constraint aggregation fails to break this plateau under same-model self-extraction.\n\nThe central finding is the independence bottleneck. Same-model traces produce Fleiss' $\\kappa$ values of $0.21$--$0.82$, and the effective sample size compresses to Eff-$K = 1.20$--$3.63$ at $K = 12$. Self-extracted FOL constraints inherit this correlation structure. SICA gains are confined to a narrow Goldilocks zone of approximately 50--55\\% SC accuracy, where Mistral-7B on FOLIO achieves $+4.90$\\,pp ($p = 0.013$, significant in 2 of 3 seeds). Outside this zone, confirmation bias renders constraints non-discriminative (Type~A) or error amplification actively degrades accuracy by $-2.83$\\,pp (Type~C).\n\nOracle controls confirm that the aggregation mechanism is sound: gold FOL annotations yield $+14.22$\\,pp on FOLIO and $+11.50$\\,pp on ProofWriter (both $p < 0.001$), yet self-extraction captures only 35\\% of this ceiling. Nine remediation strategies spanning six intervention dimensions all fail to widen the effective zone. The uniform failure confirms the bottleneck is structural rather than an engineering artifact. Sensitivity analysis reinforces this conclusion: $K = 12$ marks the inverted-U peak, and the effect collapses at $T = 1.0$.\n\nThe multi-candidate rate $C_0$ combined with SC accuracy provides a zero-cost deployment diagnostic for predicting when symbolic aggregation can help. Three paths forward trade simplicity for independence as CJT requires: trained extractors, external provers, and multi-model pipelines.\n\n\\paragraph{Limitations.} Our evaluation is limited to same-model self-extraction. We do not test trained FOL extractors, external solvers with verified grounding, or multi-model constraint pipelines, all of which may overcome the independence bottleneck.\n"
  }
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-19T05:22:07.248205+00:00_

&lt;tool_use_error>File has been modified since read, either by the user or by a linter. Read it again before attempting to write it.&lt;/tool_use_error>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_conclusion_20260519T051953",
  "tool": "Write",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-19T05:22:07.248316+00:00_

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
  "session": "worker_paper_writing_conclusion_20260519T051953",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/conclusion.tex"
  }
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-19T05:22:07.248434+00:00_

1	\section{Conclusion}\label{sec:conclusion}
2	
3	We evaluated Symbolic Invariant Consensus Aggregation (SICA) across seven models (7B to 32B parameters), four reasoning domains, and more than 2,400 instances with three-seed replication. The Condorcet Jury Theorem provides a precise diagnostic for Self-Consistency's plateau: same-model traces produce Fleiss' $\kappa = 0.21$--$0.82$, compressing the effective ensemble size to $K_{\text{eff}} = 1.20$--$3.63$ for nominal $K = 12$. At $K_{\text{eff}} \approx 1$, additional traces carry almost no new information, and no aggregation method operating on those traces alone can escape the plateau.
4	
5	Self-extracted symbolic constraints do not resolve this bottleneck. SICA gains are confined to a narrow Goldilocks zone (${\sim}$50--55\% SC accuracy), where Mistral-7B achieves $+4.90$\,pp on FOLIO ($p = 0.013$, significant in 2 of 3 seeds). Three failure modes explain the regime boundaries: confirmation bias above ${\sim}$60\% SC (Type~A), error amplification below ${\sim}$40\% ($\Delta = -2.83$\,pp, Type~C), and non-formalizable domains (Type~B). Oracle controls substituting gold FOL annotations yield $+14.22$\,pp on FOLIO and $+11.50$\,pp on ProofWriter (both $p < 0.001$), proving the aggregation mechanism is sound. Self-extraction captures only 35\% of this oracle ceiling. Nine remediation strategies spanning six intervention dimensions all fail to widen the effective zone.
6	
7	The multi-candidate rate $C_0$ combined with SC accuracy provides practitioners a zero-cost deployment diagnostic: when both fall outside the Goldilocks zone, SICA offers no benefit over majority voting. Closing the oracle gap requires constraint sources that are not deterministic functions of the reasoning model's own distribution: trained extractors, external provers, or multi-model pipelines.
8	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_conclusion_20260519T051953",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 21 · 2026-05-19T05:22:07.248567+00:00_

called Write

<details open><summary>🔧 Tool call — Write</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/conclusion.tex",
  "content": "\\section{Conclusion}\\label{sec:conclusion}\n\nWe evaluated Symbolic Invariant Consensus Aggregation (SICA) across seven models (7B to 32B parameters), four reasoning domains, and over 2,400 instances with three-seed replication. Grounded in the Condorcet Jury Theorem, our analysis explains why Self-Consistency majority voting saturates and why symbolic constraint aggregation fails to break this plateau under same-model self-extraction.\n\nThe central finding is the independence bottleneck. Same-model traces produce Fleiss' $\\kappa$ values of $0.21$--$0.82$, and the effective sample size compresses to Eff-$K = 1.20$--$3.63$ at $K = 12$. Self-extracted FOL constraints inherit this correlation structure. SICA gains are confined to a narrow Goldilocks zone of approximately 50--55\\% SC accuracy, where Mistral-7B on FOLIO achieves $+4.90$\\,pp ($p = 0.013$, significant in 2 of 3 seeds). Outside this zone, confirmation bias renders constraints non-discriminative (Type~A) or error amplification actively degrades accuracy by $-2.83$\\,pp (Type~C).\n\nOracle controls confirm that the aggregation mechanism is sound: gold FOL annotations yield $+14.22$\\,pp on FOLIO and $+11.50$\\,pp on ProofWriter (both $p < 0.001$), yet self-extraction captures only 35\\% of this ceiling. Nine remediation strategies spanning six intervention dimensions all fail to widen the effective zone. The uniform failure confirms the bottleneck is structural rather than an engineering artifact. Sensitivity analysis reinforces this conclusion: $K = 12$ marks the inverted-U peak, and the effect collapses at $T = 1.0$.\n\nThe multi-candidate rate $C_0$ combined with SC accuracy provides a zero-cost deployment diagnostic for predicting when symbolic aggregation can help. Three paths forward trade simplicity for independence as CJT requires: trained extractors, external provers, and multi-model pipelines.\n\n\\paragraph{Limitations.} Our evaluation is limited to same-model self-extraction. We do not test trained FOL extractors, external solvers with verified grounding, or multi-model constraint pipelines, all of which may overcome the independence bottleneck.\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_conclusion_20260519T051953",
  "tool": "Write",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/conclusion.tex",
    "content": "\\section{Conclusion}\\label{sec:conclusion}\n\nWe evaluated Symbolic Invariant Consensus Aggregation (SICA) across seven models (7B to 32B parameters), four reasoning domains, and over 2,400 instances with three-seed replication. Grounded in the Condorcet Jury Theorem, our analysis explains why Self-Consistency majority voting saturates and why symbolic constraint aggregation fails to break this plateau under same-model self-extraction.\n\nThe central finding is the independence bottleneck. Same-model traces produce Fleiss' $\\kappa$ values of $0.21$--$0.82$, and the effective sample size compresses to Eff-$K = 1.20$--$3.63$ at $K = 12$. Self-extracted FOL constraints inherit this correlation structure. SICA gains are confined to a narrow Goldilocks zone of approximately 50--55\\% SC accuracy, where Mistral-7B on FOLIO achieves $+4.90$\\,pp ($p = 0.013$, significant in 2 of 3 seeds). Outside this zone, confirmation bias renders constraints non-discriminative (Type~A) or error amplification actively degrades accuracy by $-2.83$\\,pp (Type~C).\n\nOracle controls confirm that the aggregation mechanism is sound: gold FOL annotations yield $+14.22$\\,pp on FOLIO and $+11.50$\\,pp on ProofWriter (both $p < 0.001$), yet self-extraction captures only 35\\% of this ceiling. Nine remediation strategies spanning six intervention dimensions all fail to widen the effective zone. The uniform failure confirms the bottleneck is structural rather than an engineering artifact. Sensitivity analysis reinforces this conclusion: $K = 12$ marks the inverted-U peak, and the effect collapses at $T = 1.0$.\n\nThe multi-candidate rate $C_0$ combined with SC accuracy provides a zero-cost deployment diagnostic for predicting when symbolic aggregation can help. Three paths forward trade simplicity for independence as CJT requires: trained extractors, external provers, and multi-model pipelines.\n\n\\paragraph{Limitations.} Our evaluation is limited to same-model self-extraction. We do not test trained FOL extractors, external solvers with verified grounding, or multi-model constraint pipelines, all of which may overcome the independence bottleneck.\n"
  }
}
```

</details>

---

### Tool result

_source line 22 · 2026-05-19T05:22:07.248717+00:00_

The file /home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/conclusion.tex has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_conclusion_20260519T051953",
  "tool": "Write",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 23 · 2026-05-19T05:22:07.248916+00:00_

已写入 `conclusion.tex`。相比原版的主要改动：

1. **Eff-$K$ 记号统一** — 原版用 `$K_{\text{eff}}$`，与 introduction/discussion 的 `Eff-$K$` 不一致，已修正
2. **补充 sensitivity 证据** — 加入 inverted-U peak ($K=12$) 和 $T=1.0$ collapse，对应任务要求的"结构性瓶颈"段
3. **补充 Limitations 段** — 原版缺失，现为独立 `\paragraph{Limitations.}`
4. **去掉 $K_{\text{eff}} \approx 1$ 展开** — 压缩篇幅，该细节已在 introduction 充分铺垫

全文约 285 words，无破折号、无 -ing 短语结尾、数字与 abstract/introduction/discussion 一致。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_paper_writing_conclusion_20260519T051953"
}
```

</details>

---
