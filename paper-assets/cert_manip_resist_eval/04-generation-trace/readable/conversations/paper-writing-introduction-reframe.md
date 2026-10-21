# paper writing introduction reframe

**The Weakest Link Across Panel Sizes: Predictor Relevance Patterns in Multi-Judge LLM Evaluation under Adversarial Manipulation** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 13
- **Recorded user turns:** 0
- **Tool calls:** 6
- **Original source:** `logs/chats/worker_paper_writing_introduction_reframe_20260523T011835.jsonl`
- **Structured JSON:** [`793ddd6d54e74580a82f.json`](../../sessions/79/793ddd6d54e74580a82f.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

13 recorded events

### Tool call

_source line 1 · 2026-05-23T01:21:33.570790+00:00_

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
  "session": "worker_paper_writing_introduction_reframe_20260523T011835",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/agent-ml-research/skills/global/paper-writing-norms.skill.md"
  }
}
```

</details>

---

### Tool result

_source line 2 · 2026-05-23T01:21:33.571347+00:00_

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
  "session": "worker_paper_writing_introduction_reframe_20260523T011835",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-23T01:21:33.571542+00:00_

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
  "session": "worker_paper_writing_introduction_reframe_20260523T011835",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/agent-ml-research/skills/global/latex-paper.skill.md"
  }
}
```

</details>

---

### Tool result

_source line 4 · 2026-05-23T01:21:33.571956+00:00_

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
  "session": "worker_paper_writing_introduction_reframe_20260523T011835",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-23T01:21:33.572125+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/docs/paper/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_introduction_reframe_20260523T011835",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/docs/paper/introduction.tex"
  }
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-23T01:21:33.572278+00:00_

1	\section{Introduction}
2	
3	Multi-judge panels have emerged as the dominant defense against bias and manipulation in LLM-based evaluation. After \citet{zheng2023judging} demonstrated that individual LLM judges can rival human annotators, subsequent work revealed systematic vulnerabilities: position bias, verbosity preferences, and sycophancy compromise the reliability of any single judge \citep{wang2023fair}. The natural response has been to aggregate decisions across diverse models, drawing inspiration from Byzantine fault tolerance (BFT), where majority voting among independent nodes aggregates away faulty responses \citep{lamport1982byzantine,castro1999practical}. A recent systematization of LLM-judge security reinforces this assumption, reporting that 7-model committees reduce attack success rates from 50--68\% to 10--19\% \citep{almasoud2026security}. Diversity, by this logic, is the key ingredient for secure evaluation.
4	
5	Yet the evidence for diversity as a causal defense mechanism is weaker than it appears. The observed ASR reduction in multi-judge panels \citep{almasoud2026security} conflates two distinct factors: the diversity of the panel (how independently judges respond to attacks) and the individual robustness of the strongest members. No existing work disentangles these contributions. We draw inspiration from BFT, though the settings differ: BFT adversaries control faulty nodes internally, while evaluation adversaries manipulate inputs externally. The strong data-processing inequality (SDPI) bounds joint failure in terms of effective independence, but assumes non-adaptive faults and does not model adversaries that observe panel composition and strategically select attacks \citep{schneier2000secrets}.
6	
7	In our experiments, panel vulnerability under adaptive attack is dominated by the weakest individual judge, not by panel diversity. An adaptive adversary who observes panel composition identifies the most vulnerable member and selects the exploit
…[truncated 3051 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_introduction_reframe_20260523T011835",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-23T01:21:33.572510+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "\\\\label\\{sec:",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/docs/paper",
  "output_mode": "content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_introduction_reframe_20260523T011835",
  "tool": "Grep",
  "tool_args": {
    "pattern": "\\\\label\\{sec:",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/docs/paper",
    "output_mode": "content"
  }
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-23T01:21:33.572670+00:00_

docs/paper/threat_model.tex:2:\label{sec:threat_model}
docs/paper/results.tex:2:\label{sec:results}
docs/paper/results.tex:5:\label{sec:dominance}
docs/paper/results.tex:47:\label{sec:robustness}
docs/paper/results.tex:77:\label{sec:rf_contrast}
docs/paper/results.tex:89:\label{sec:gam_taxonomy}
docs/paper/results.tex:96:\label{sec:aggregation}
docs/paper/methodology.tex:2:\label{sec:experiments}
docs/paper/methodology.tex:61:\label{sec:stat_framework}
docs/paper/methodology.tex:75:\label{sec:robustness_method}
docs/paper/analysis.tex:2:\label{sec:analysis}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_introduction_reframe_20260523T011835",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-23T01:21:33.572862+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/docs/paper/introduction.tex",
  "old_string": "\\section{Introduction}\n\nMulti-judge panels have emerged as the dominant defense against bias and manipulation in LLM-based evaluation. After \\citet{zheng2023judging} demonstrated that individual LLM judges can rival human annotators, subsequent work revealed systematic vulnerabilities: position bias, verbosity preferences, and sycophancy compromise the reliability of any single judge \\citep{wang2023fair}. The natural response has been to aggregate decisions across diverse models, drawing inspiration from Byzantine fault tolerance (BFT), where majority voting among independent nodes aggregates away faulty responses \\citep{lamport1982byzantine,castro1999practical}. A recent systematization of LLM-judge security reinforces this assumption, reporting that 7-model committees reduce attack success rates from 50--68\\% to 10--19\\% \\citep{almasoud2026security}. Diversity, by this logic, is the key ingredient for secure evaluation.\n\nYet the evidence for diversity as a causal defense mechanism is weaker than it appears. The observed ASR reduction in multi-judge panels \\citep{almasoud2026security} conflates two distinct factors: the diversity of the panel (how independently judges respond to attacks) and the individual robustness of the strongest members. No existing work disentangles these contributions. We draw inspiration from BFT, though the settings differ: BFT adversaries control faulty nodes internally, while evaluation adversaries manipulate inputs externally. The strong data-processing inequality (SDPI) bounds joint failure in terms of effective independence, but assumes non-adaptive faults and does not model adversaries that observe panel composition and strategically select attacks \\citep{schneier2000secrets}.\n\nIn our experiments, panel vulnerability under adaptive attack is dominated by the weakest individual judge, not by panel diversity. An adaptive adversary who observes panel composition identifies the most vulnerable member and selects the exploit that corrupts that member's vote \\citep{goodfellow2015adversarial,papernot2016transferability}. Panel diversity shows a directional but statistically fragile association with increased vulnerability; significance collapses from 8/12 conditions to 0--1/12 after correcting for the non-independence inherent in combinatorial panel designs (455 panels from 15 shared judges). We term this asymmetry the \\emph{weakest-link effect}: panel security is primarily an individual-judge quality problem, not a diversity problem.\n\nControlled experiments across 15 models from 6 families, 455 panels, 6 attack types, and 2 benchmarks (MMLU, ARC) confirm this asymmetry. The weakest-judge vulnerability $\\eta_{\\max}$ is robustly significant across multiple non-independence corrections, while $K_{\\mathrm{eff}}$, a pairwise-MI-based diversity metric, falls below the detectable threshold (minimum detectable effect $\\beta_{\\mathrm{std}} = 0.14$). A contrast between adaptive and random faults sharpens the finding: under random faults, panel composition is highly predictive ($R^2 = 0.73$--$0.81$, surviving all corrections), but this predictability breaks down under adaptive attack. GAM analysis reveals the directional structure masked by this collapse: $K_{\\mathrm{eff}}$'s partial effect splits cleanly by attack mechanism, positive (diversity harmful) for targeted attacks and negative (diversity protective) for shared-bias attacks. Aggregation rule choice further modulates vulnerability: Bayesian calibration reverses $K_{\\mathrm{eff}}$'s direction, while robustness-first panel selection dominates in all conditions.\n\nThese findings yield three contributions:\n\\begin{enumerate}\n\\item \\textbf{Weakest-link dominance with informative null.} The first large-scale empirical decomposition of panel vulnerability into individual weakness ($\\eta_{\\max}$) and structural diversity ($K_{\\mathrm{eff}}$) in LLM evaluation. $\\eta_{\\max}$ is robustly significant across correction methods; $K_{\\mathrm{eff}}$'s non-significance is an informative null (the study has power to detect $\\beta_{\\mathrm{std}} \\geq 0.14$), bounding any true diversity effect as small (\\S\\ref{sec:results}).\n\\item \\textbf{Adaptive-vs-random fault contrast.} Under random faults, panel composition is highly predictive ($R^2 = 0.73$--$0.81$, surviving all corrections); under adaptive attack, this predictability collapses. The contrast establishes that diversity's association with vulnerability is genuine under non-adaptive noise but inflated under strategic manipulation (\\S\\ref{sec:rf_contrast}).\n\\item \\textbf{Attack-type taxonomy and aggregation control.} GAM analysis reveals a clean split by attack mechanism (targeted vs.\\ shared-bias), explaining the directional structure that linear regression obscures. Aggregation rule choice modulates both channels: Bayesian calibration reverses $K_{\\mathrm{eff}}$'s direction; robustness-first selection dominates diversity-maximizing strategies (\\S\\ref{sec:aggregation}, \\S\\ref{sec:analysis}).\n\\end{enumerate}",
  "new_string": "\\section{Introduction}\n\nMulti-judge panels have emerged as the dominant defense against bias and manipulation in LLM-based evaluation. After \\citet{zheng2023judging} demonstrated that individual LLM judges can rival human annotators, subsequent work exposed systematic vulnerabilities: position bias, verbosity preferences, and sycophancy compromise the reliability of any single judge \\citep{wang2023fair}. The natural response has been to aggregate decisions across diverse models, drawing inspiration from Byzantine fault tolerance (BFT), where majority voting among independent nodes tolerates faulty responses \\citep{lamport1982byzantine,castro1999practical}. A recent systematization of LLM-judge security reports that 7-model committees reduce attack success rates from 50--68\\% to 10--19\\% \\citep{almasoud2026security}. Diversity, by this logic, is the key ingredient for secure evaluation.\n\nYet the evidence for diversity as a causal defense is weaker than it appears. The observed ASR reduction in multi-judge panels conflates two distinct factors: the diversity of the panel (how independently judges respond to attacks) and the individual robustness of its strongest members. No existing work disentangles these contributions across panel sizes. The BFT settings differ from the evaluation setting in a critical way: BFT adversaries control faulty nodes internally, whereas evaluation adversaries manipulate inputs externally. The strong data-processing inequality (SDPI) bounds joint failure probability but assumes non-adaptive faults and does not model adversaries who observe panel composition \\citep{schneier2000secrets}.\n\nIn our experiments, we discover a panel-size-dependent vulnerability regime transition. At $K{=}3$, panel vulnerability is dominated by individual judge weakness ($\\eta_{\\max}$), not diversity ($K_{\\mathrm{eff}}$): the weakest link is the bottleneck. At $K{\\geq}5$, this completely reverses: $K_{\\mathrm{eff}}$ becomes the dominant predictor while $\\eta_{\\max}$ collapses to non-significance. The surprise is that diversity is harmful in both regimes ($K_{\\mathrm{eff}}$ coefficient positive throughout): independent judges enable per-judge adversarial targeting \\citep{goodfellow2015adversarial,papernot2016transferability}, while correlated judges share robust consensus. The transition threshold lies between $K{=}3$ and $K{=}5$: at $K{=}3$, one weak judge suffices to flip the majority ($2/3$); at $K{\\geq}5$, the adversary must flip more judges, and independence becomes the vulnerability.\n\nControlled experiments across 15 models from 6 families, $K \\in \\{3,5,7\\}$, 6 attack types, and 2 benchmarks confirm this transition. Wild cluster bootstrap shows an $\\eta_{\\max}$ significance cliff: 5/12 $\\to$ 0/12 $\\to$ 0/12 across $K$ values, while $K_{\\mathrm{eff}}$ emerges: 1/12 $\\to$ 7/12 $\\to$ 5/12. A contrast between adaptive and random faults sharpens the finding: under random faults, panel composition is highly predictive ($R^2 = 0.73$--$0.81$, $K_{\\mathrm{eff}}$ significant 2/2), but this predictability breaks down under adaptive attack. GAM analysis reveals a clean 6:6 split by attack mechanism (targeted vs.\\ shared-bias). Aggregation rule choice modulates both vulnerability channels: Bayesian calibration reverses $K_{\\mathrm{eff}}$'s direction, while robustness-first selection dominates at all $K$ values.\n\nThese findings yield three contributions:\n\\begin{enumerate}\n\\item \\textbf{K-dependent vulnerability regime transition.} The first large-scale empirical study of panel vulnerability across panel sizes $K \\in \\{3,5,7\\}$. $\\eta_{\\max}$ dominates at $K{=}3$ (bootstrap significant 5/12, $K_{\\mathrm{eff}}$ 1/12, informative null with MDE${=}0.14$); complete reversal at $K{\\geq}5$ ($K_{\\mathrm{eff}}$ 7/12, $\\eta_{\\max}$ 0/12). Diversity coefficient positive in both regimes (\\S\\ref{sec:dominance}, \\S\\ref{sec:robustness}).\n\\item \\textbf{Adaptive-vs-random fault contrast.} Under random faults, panel composition is highly predictive ($R^2 = 0.73$--$0.81$, surviving all corrections); under adaptive attack, predictability collapses. This establishes that diversity's association is genuine under non-adaptive noise but inflated under strategic manipulation (\\S\\ref{sec:rf_contrast}).\n\\item \\textbf{Attack-type taxonomy and aggregation control.} GAM reveals a clean 6:6 split by attack mechanism (targeted vs.\\ shared-bias). Aggregation modulates both vulnerability channels: Bayesian calibration reverses $K_{\\mathrm{eff}}$'s direction; robustness-first selection dominates diversity-maximizing strategies (\\S\\ref{sec:gam_taxonomy}, \\S\\ref{sec:aggregation}).\n\\end{enumerate}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_introduction_reframe_20260523T011835",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/docs/paper/introduction.tex",
    "old_string": "\\section{Introduction}\n\nMulti-judge panels have emerged as the dominant defense against bias and manipulation in LLM-based evaluation. After \\citet{zheng2023judging} demonstrated that individual LLM judges can rival human annotators, subsequent work revealed systematic vulnerabilities: position bias, verbosity preferences, and sycophancy compromise the reliability of any single judge \\citep{wang2023fair}. The natural response has been to aggregate decisions across diverse models, drawing inspiration from Byzantine fault tolerance (BFT), where majority voting among independent nodes aggregates away faulty responses \\citep{lamport1982byzantine,castro1999practical}. A recent systematization of LLM-judge security reinforces this assumption, reporting that 7-model committees reduce attack success rates from 50--68\\% to 10--19\\% \\citep{almasoud2026security}. Diversity, by this logic, is the key ingredient for secure evaluation.\n\nYet the evidence for diversity as a causal defense mechanism is weaker than it appears. The observed ASR reduction in multi-judge panels \\citep{almasoud2026security} conflates two distinct factors: the diversity of the panel (how independently judges respond to attacks) and the individual robustness of the strongest members. No existing work disentangles these contributions. We draw inspiration from BFT, though the settings differ: BFT adversaries control faulty nodes internally, while evaluation adversaries manipulate inputs externally. The strong data-processing inequality (SDPI) bounds joint failure in terms of effective independence, but assumes non-adaptive faults and does not model adversaries that observe panel composition and strategically select attacks \\citep{schneier2000secrets}.\n\nIn our experiments, panel vulnerability under adaptive attack is dominated by the weakest individual judge, not by panel diversity. An adaptive adversary who observes panel composition identifies the most vulnerable member and selects the exploit that corrupts that member's vote \\citep{goodfellow2015adversarial,papernot2016transferability}. Panel diversity shows a directional but statistically fragile association with increased vulnerability; significance collapses from 8/12 conditions to 0--1/12 after correcting for the non-independence inherent in combinatorial panel designs (455 panels from 15 shared judges). We term this asymmetry the \\emph{weakest-link effect}: panel security is primarily an individual-judge quality problem, not a diversity problem.\n\nControlled experiments across 15 models from 6 families, 455 panels, 6 attack types, and 2 benchmarks (MMLU, ARC) confirm this asymmetry. The weakest-judge vulnerability $\\eta_{\\max}$ is robustly significant across multiple non-independence corrections, while $K_{\\mathrm{eff}}$, a pairwise-MI-based diversity metric, falls below the detectable threshold (minimum detectable effect $\\beta_{\\mathrm{std}} = 0.14$). A contrast between adaptive and random faults sharpens the finding: under random faults, panel composition is highly predictive ($R^2 = 0.73$--$0.81$, surviving all corrections), but this predictability breaks down under adaptive attack. GAM analysis reveals the directional structure masked by this collapse: $K_{\\mathrm{eff}}$'s partial effect splits cleanly by attack mechanism, positive (diversity harmful) for targeted attacks and negative (diversity protective) for shared-bias attacks. Aggregation rule choice further modulates vulnerability: Bayesian calibration reverses $K_{\\mathrm{eff}}$'s direction, while robustness-first panel selection dominates in all conditions.\n\nThese findings yield three contributions:\n\\begin{enumerate}\n\\item \\textbf{Weakest-link dominance with informative null.} The first large-scale empirical decomposition of panel vulnerability into individual weakness ($\\eta_{\\max}$) and structural diversity ($K_{\\mathrm{eff}}$) in LLM evaluation. $\\eta_{\\max}$ is robustly significant across correction methods; $K_{\\mathrm{eff}}$'s non-significance is an informative null (the study has power to detect $\\beta_{\\mathrm{std}} \\geq 0.14$), bounding any true diversity effect as small (\\S\\ref{sec:results}).\n\\item \\textbf{Adaptive-vs-random fault contrast.} Under random faults, panel composition is highly predictive ($R^2 = 0.73$--$0.81$, surviving all corrections); under adaptive attack, this predictability collapses. The contrast establishes that diversity's association with vulnerability is genuine under non-adaptive noise but inflated under strategic manipulation (\\S\\ref{sec:rf_contrast}).\n\\item \\textbf{Attack-type taxonomy and aggregation control.} GAM analysis reveals a clean split by attack mechanism (targeted vs.\\ shared-bias), explaining the directional structure that linear regression obscures. Aggregation rule choice modulates both channels: Bayesian calibration reverses $K_{\\mathrm{eff}}$'s direction; robustness-first selection dominates diversity-maximizing strategies (\\S\\ref{sec:aggregation}, \\S\\ref{sec:analysis}).\n\\end{enumerate}",
    "new_string": "\\section{Introduction}\n\nMulti-judge panels have emerged as the dominant defense against bias and manipulation in LLM-based evaluation. After \\citet{zheng2023judging} demonstrated that individual LLM judges can rival human annotators, subsequent work exposed systematic vulnerabilities: position bias, verbosity preferences, and sycophancy compromise the reliability of any single judge \\citep{wang2023fair}. The natural response has been to aggregate decisions across diverse models, drawing inspiration from Byzantine fault tolerance (BFT), where majority voting among independent nodes tolerates faulty responses \\citep{lamport1982byzantine,castro1999practical}. A recent systematization of LLM-judge security reports that 7-model committees reduce attack success rates from 50--68\\% to 10--19\\% \\citep{almasoud2026security}. Diversity, by this logic, is the key ingredient for secure evaluation.\n\nYet the evidence for diversity as a causal defense is weaker than it appears. The observed ASR reduction in multi-judge panels conflates two distinct factors: the diversity of the panel (how independently judges respond to attacks) and the individual robustness of its strongest members. No existing work disentangles these contributions across panel sizes. The BFT settings differ from the evaluation setting in a critical way: BFT adversaries control faulty nodes internally, whereas evaluation adversaries manipulate inputs externally. The strong data-processing inequality (SDPI) bounds joint failure probability but assumes non-adaptive faults and does not model adversaries who observe panel composition \\citep{schneier2000secrets}.\n\nIn our experiments, we discover a panel-size-dependent vulnerability regime transition. At $K{=}3$, panel vulnerability is dominated by individual judge weakness ($\\eta_{\\max}$), not diversity ($K_{\\mathrm{eff}}$): the weakest link is the bottleneck. At $K{\\geq}5$, this completely reverses: $K_{\\mathrm{eff}}$ becomes the dominant predictor while $\\eta_{\\max}$ collapses to non-significance. The surprise is that diversity is harmful in both regimes ($K_{\\mathrm{eff}}$ coefficient positive throughout): independent judges enable per-judge adversarial targeting \\citep{goodfellow2015adversarial,papernot2016transferability}, while correlated judges share robust consensus. The transition threshold lies between $K{=}3$ and $K{=}5$: at $K{=}3$, one weak judge suffices to flip the majority ($2/3$); at $K{\\geq}5$, the adversary must flip more judges, and independence becomes the vulnerability.\n\nControlled experiments across 15 models from 6 families, $K \\in \\{3,5,7\\}$, 6 attack types, and 2 benchmarks confirm this transition. Wild cluster bootstrap shows an $\\eta_{\\max}$ significance cliff: 5/12 $\\to$ 0/12 $\\to$ 0/12 across $K$ values, while $K_{\\mathrm{eff}}$ emerges: 1/12 $\\to$ 7/12 $\\to$ 5/12. A contrast between adaptive and random faults sharpens the finding: under random faults, panel composition is highly predictive ($R^2 = 0.73$--$0.81$, $K_{\\mathrm{eff}}$ significant 2/2), but this predictability breaks down under adaptive attack. GAM analysis reveals a clean 6:6 split by attack mechanism (targeted vs.\\ shared-bias). Aggregation rule choice modulates both vulnerability channels: Bayesian calibration reverses $K_{\\mathrm{eff}}$'s direction, while robustness-first selection dominates at all $K$ values.\n\nThese findings yield three contributions:\n\\begin{enumerate}\n\\item \\textbf{K-dependent vulnerability regime transition.} The first large-scale empirical study of panel vulnerability across panel sizes $K \\in \\{3,5,7\\}$. $\\eta_{\\max}$ dominates at $K{=}3$ (bootstrap significant 5/12, $K_{\\mathrm{eff}}$ 1/12, informative null with MDE${=}0.14$); complete reversal at $K{\\geq}5$ ($K_{\\mathrm{eff}}$ 7/12, $\\eta_{\\max}$ 0/12). Diversity coefficient positive in both regimes (\\S\\ref{sec:dominance}, \\S\\ref{sec:robustness}).\n\\item \\textbf{Adaptive-vs-random fault contrast.} Under random faults, panel composition is highly predictive ($R^2 = 0.73$--$0.81$, surviving all corrections); under adaptive attack, predictability collapses. This establishes that diversity's association is genuine under non-adaptive noise but inflated under strategic manipulation (\\S\\ref{sec:rf_contrast}).\n\\item \\textbf{Attack-type taxonomy and aggregation control.} GAM reveals a clean 6:6 split by attack mechanism (targeted vs.\\ shared-bias). Aggregation modulates both vulnerability channels: Bayesian calibration reverses $K_{\\mathrm{eff}}$'s direction; robustness-first selection dominates diversity-maximizing strategies (\\S\\ref{sec:gam_taxonomy}, \\S\\ref{sec:aggregation}).\n\\end{enumerate}"
  }
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-23T01:21:33.573134+00:00_

The file /home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/docs/paper/introduction.tex has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_introduction_reframe_20260523T011835",
  "tool": "Edit",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-23T01:21:33.573278+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/docs/paper/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_introduction_reframe_20260523T011835",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/docs/paper/introduction.tex"
  }
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-23T01:21:33.573428+00:00_

1	\section{Introduction}
2	
3	Multi-judge panels have emerged as the dominant defense against bias and manipulation in LLM-based evaluation. After \citet{zheng2023judging} demonstrated that individual LLM judges can rival human annotators, subsequent work exposed systematic vulnerabilities: position bias, verbosity preferences, and sycophancy compromise the reliability of any single judge \citep{wang2023fair}. The natural response has been to aggregate decisions across diverse models, drawing inspiration from Byzantine fault tolerance (BFT), where majority voting among independent nodes tolerates faulty responses \citep{lamport1982byzantine,castro1999practical}. A recent systematization of LLM-judge security reports that 7-model committees reduce attack success rates from 50--68\% to 10--19\% \citep{almasoud2026security}. Diversity, by this logic, is the key ingredient for secure evaluation.
4	
5	Yet the evidence for diversity as a causal defense is weaker than it appears. The observed ASR reduction in multi-judge panels conflates two distinct factors: the diversity of the panel (how independently judges respond to attacks) and the individual robustness of its strongest members. No existing work disentangles these contributions across panel sizes. The BFT settings differ from the evaluation setting in a critical way: BFT adversaries control faulty nodes internally, whereas evaluation adversaries manipulate inputs externally. The strong data-processing inequality (SDPI) bounds joint failure probability but assumes non-adaptive faults and does not model adversaries who observe panel composition \citep{schneier2000secrets}.
6	
7	In our experiments, we discover a panel-size-dependent vulnerability regime transition. At $K{=}3$, panel vulnerability is dominated by individual judge weakness ($\eta_{\max}$), not diversity ($K_{\mathrm{eff}}$): the weakest link is the bottleneck. At $K{\geq}5$, this completely reverses: $K_{\mathrm{eff}}$ becomes the dominant predictor whil
…[truncated 2681 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_introduction_reframe_20260523T011835",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 13 · 2026-05-23T01:21:33.573630+00:00_

Introduction rewritten. Key changes from old version:

- **Framing**: "weakest-link dominance" → "K-dependent vulnerability regime transition" (η_max dominates at K=3, K_eff dominates at K≥5)
- **Diversity direction**: corrected to "harmful in both regimes" (K_eff coefficient positive throughout), not protective at any K
- **Mechanism**: added the 2/3 majority-flip explanation for the K=3→K≥5 transition
- **Evidence**: updated bootstrap counts (5/12→0/12 for η_max, 1/12→7/12 for K_eff) and K∈{3,5,7} scope
- **Section refs**: updated to actual labels (sec:dominance, sec:robustness, sec:gam_taxonomy, sec:aggregation)
- **Style**: no em-dashes, no -ing endings, no AI vocabulary

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_paper_writing_introduction_reframe_20260523T011835"
}
```

</details>

---
