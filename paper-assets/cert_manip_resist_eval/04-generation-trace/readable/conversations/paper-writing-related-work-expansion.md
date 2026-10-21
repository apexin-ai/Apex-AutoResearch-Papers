# paper writing related work expansion

**The Weakest Link Across Panel Sizes: Predictor Relevance Patterns in Multi-Judge LLM Evaluation under Adversarial Manipulation** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 21
- **Recorded user turns:** 0
- **Tool calls:** 10
- **Original source:** `logs/chats/worker_paper_writing_related_work_expansion_20260522T232439.jsonl`
- **Structured JSON:** [`18420b35c6605fb82ef3.json`](../../sessions/18/18420b35c6605fb82ef3.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

21 recorded events

### Tool call

_source line 1 · 2026-05-22T23:26:07.417020+00:00_

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
  "session": "worker_paper_writing_related_work_expansion_20260522T232439",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/agent-ml-research/skills/global/paper-writing-norms.skill.md"
  }
}
```

</details>

---

### Tool result

_source line 2 · 2026-05-22T23:26:07.417592+00:00_

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
  "session": "worker_paper_writing_related_work_expansion_20260522T232439",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-22T23:26:07.417810+00:00_

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
  "session": "worker_paper_writing_related_work_expansion_20260522T232439",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/agent-ml-research/skills/global/latex-paper.skill.md"
  }
}
```

</details>

---

### Tool result

_source line 4 · 2026-05-22T23:26:07.418161+00:00_

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
  "session": "worker_paper_writing_related_work_expansion_20260522T232439",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-22T23:26:07.418321+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/docs/paper/related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_related_work_expansion_20260522T232439",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/docs/paper/related_work.tex"
  }
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-22T23:26:07.418471+00:00_

1	\section{Related Work}
2	
3	\paragraph{LLM-as-Judge and Multi-Judge Evaluation.}
4	LLM judges gained traction after \citet{zheng2023judging} established them as scalable alternatives to human annotation. \citet{wang2023fair} documented systematic failure modes (position bias, verbosity preferences, sycophancy), motivating multi-judge panels. \citet{verga2024replacing} showed that diverse panels can match single large judges, and \citet{panickssery2024llm} identified self-preference bias as a mechanism for within-family correlations. \citet{almasoud2026security} reported that 7-model committees reduce attack success rates from 50--68\% to 10--19\%, but did not disentangle diversity from individual robustness, precisely the gap we address.
5	
6	\paragraph{Condorcet Jury Theorem.}
7	\citet{condorcet1785essai} proved that majority voting accuracy converges to 1 when per-voter accuracy exceeds 0.5, and to 0 otherwise; \citet{austensmith1996information} showed that strategic voting under incomplete information weakens this guarantee. Our results instantiate the CJT failure mode empirically: when adaptive attacks push individual judges below the critical threshold, panel expansion amplifies error.
8	
9	\paragraph{Ensemble Diversity Theory.}
10	\citet{krogh1995neural} proved that ensemble error equals average member error minus a diversity term, and \citet{brown2005managing} extended this via bias-variance-covariance decomposition. However, \citet{kuncheva2003measures} found that no single diversity metric reliably predicts ensemble improvement, consistent with our finding that $K_{\mathrm{eff}}$'s association with vulnerability is statistically fragile under correction. Recent information-theoretic frameworks \citep{yang2026diversity,turkmen2026ensemble} characterize diversity under benign evaluation; we provide the adversarial complement.
11	
12	\paragraph{Adversarial Robustness and Transferability.}
13	Adversarial vulnerability was formalized by \citet{goodfellow2015ad
…[truncated 1874 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_related_work_expansion_20260522T232439",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-22T23:26:07.418654+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "dawid1979|li2023alpacaeval|ye2024flask",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/docs/paper/references.bib",
  "output_mode": "content",
  "-C": "2"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_related_work_expansion_20260522T232439",
  "tool": "Grep",
  "tool_args": {
    "pattern": "dawid1979|li2023alpacaeval|ye2024flask",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/docs/paper/references.bib",
    "output_mode": "content",
    "-C": "2"
  }
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-22T23:26:07.418791+00:00_

396-% ============================================================
397-
398:@article{dawid1979maximum,
399-  author    = {Alexander Philip Dawid and Allan M. Skene},
400-  title     = {Maximum Likelihood Estimation of Observer Error-Rates Using the {EM} Algorithm},
--
407-}
408-
409:@article{li2023alpacaeval,
410-  author    = {Xuechen Li and Tianyi Zhang and Yann Dubois and Rohan Taori and Ishaan Gulrajani and Carlos Guestrin and Percy Liang and Tatsunori B. Hashimoto},
411-  title     = {{AlpacaEval}: An Automatic Evaluator of Instruction-following Models},
--
415-}
416-
417:@inproceedings{ye2024flask,
418-  author    = {Seonghyeon Ye and Doyoung Kim and Sungdong Kim and Hyeonbin Hwang and Seungone Kim and Yongrae Jo and James Thorne and Juho Kim and Minjoon Seo},
419-  title     = {{FLASK}: Fine-grained Language Model Evaluation based on Alignment Skill Sets},

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_related_work_expansion_20260522T232439",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-22T23:26:07.418931+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/docs/paper/related_work.tex",
  "old_string": "\\paragraph{LLM-as-Judge and Multi-Judge Evaluation.}\nLLM judges gained traction after \\citet{zheng2023judging} established them as scalable alternatives to human annotation. \\citet{wang2023fair} documented systematic failure modes (position bias, verbosity preferences, sycophancy), motivating multi-judge panels. \\citet{verga2024replacing} showed that diverse panels can match single large judges, and \\citet{panickssery2024llm} identified self-preference bias as a mechanism for within-family correlations. \\citet{almasoud2026security} reported that 7-model committees reduce attack success rates from 50--68\\% to 10--19\\%, but did not disentangle diversity from individual robustness, precisely the gap we address.",
  "new_string": "\\paragraph{LLM-as-Judge and Multi-Judge Evaluation.}\nLLM judges gained traction after \\citet{zheng2023judging} established them as scalable alternatives to human annotation. \\citet{wang2023fair} documented systematic failure modes (position bias, verbosity preferences, sycophancy), motivating multi-judge panels as a mitigation strategy. The idea of aggregating multiple noisy annotators traces back to \\citet{dawid1979maximum}, who derived EM-based estimation of individual error rates from disagreement patterns; LLM judge panels inherit this multi-annotator structure but introduce correlated failure modes absent in classical settings. \\citet{verga2024replacing} showed that diverse panels can match single large judges, and \\citet{panickssery2024llm} identified self-preference bias as a mechanism for within-family correlations. On the evaluation design side, \\citet{li2023alpacaeval} operationalized multi-judge comparison through automated win-rate estimation across model pairs, while \\citet{ye2024flask} decomposed holistic judgment into fine-grained skill dimensions, enabling per-capability diagnosis. These frameworks assume benign evaluation conditions; we test whether their aggregation benefits survive adversarial manipulation. \\citet{almasoud2026security} reported that 7-model committees reduce attack success rates from 50--68\\% to 10--19\\%, but did not disentangle diversity from individual robustness, precisely the gap we address."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_related_work_expansion_20260522T232439",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/docs/paper/related_work.tex",
    "old_string": "\\paragraph{LLM-as-Judge and Multi-Judge Evaluation.}\nLLM judges gained traction after \\citet{zheng2023judging} established them as scalable alternatives to human annotation. \\citet{wang2023fair} documented systematic failure modes (position bias, verbosity preferences, sycophancy), motivating multi-judge panels. \\citet{verga2024replacing} showed that diverse panels can match single large judges, and \\citet{panickssery2024llm} identified self-preference bias as a mechanism for within-family correlations. \\citet{almasoud2026security} reported that 7-model committees reduce attack success rates from 50--68\\% to 10--19\\%, but did not disentangle diversity from individual robustness, precisely the gap we address.",
    "new_string": "\\paragraph{LLM-as-Judge and Multi-Judge Evaluation.}\nLLM judges gained traction after \\citet{zheng2023judging} established them as scalable alternatives to human annotation. \\citet{wang2023fair} documented systematic failure modes (position bias, verbosity preferences, sycophancy), motivating multi-judge panels as a mitigation strategy. The idea of aggregating multiple noisy annotators traces back to \\citet{dawid1979maximum}, who derived EM-based estimation of individual error rates from disagreement patterns; LLM judge panels inherit this multi-annotator structure but introduce correlated failure modes absent in classical settings. \\citet{verga2024replacing} showed that diverse panels can match single large judges, and \\citet{panickssery2024llm} identified self-preference bias as a mechanism for within-family correlations. On the evaluation design side, \\citet{li2023alpacaeval} operationalized multi-judge comparison through automated win-rate estimation across model pairs, while \\citet{ye2024flask} decomposed holistic judgment into fine-grained skill dimensions, enabling per-capability diagnosis. These frameworks assume benign evaluation conditions; we test whether their aggregation benefits survive adversarial manipulation. \\citet{almasoud2026security} reported that 7-model committees reduce attack success rates from 50--68\\% to 10--19\\%, but did not disentangle diversity from individual robustness, precisely the gap we address."
  }
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-22T23:26:07.419096+00:00_

The file /home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/docs/paper/related_work.tex has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_related_work_expansion_20260522T232439",
  "tool": "Edit",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-22T23:26:07.419216+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/docs/paper/related_work.tex",
  "old_string": "\\paragraph{Condorcet Jury Theorem.}\n\\citet{condorcet1785essai} proved that majority voting accuracy converges to 1 when per-voter accuracy exceeds 0.5, and to 0 otherwise; \\citet{austensmith1996information} showed that strategic voting under incomplete information weakens this guarantee. Our results instantiate the CJT failure mode empirically: when adaptive attacks push individual judges below the critical threshold, panel expansion amplifies error.",
  "new_string": "\\paragraph{Condorcet Jury Theorem.}\n\\citet{condorcet1785essai} proved that majority voting accuracy converges to 1 when per-voter accuracy exceeds 0.5, and to 0 otherwise; \\citet{austensmith1996information} showed that strategic voting under incomplete information weakens this guarantee. The theorem's optimistic prediction rests on voter independence, a condition that correlated LLM outputs systematically violate. Our results instantiate the CJT failure mode empirically: when adaptive attacks push individual judges below the critical threshold, panel expansion amplifies rather than corrects error."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_related_work_expansion_20260522T232439",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/docs/paper/related_work.tex",
    "old_string": "\\paragraph{Condorcet Jury Theorem.}\n\\citet{condorcet1785essai} proved that majority voting accuracy converges to 1 when per-voter accuracy exceeds 0.5, and to 0 otherwise; \\citet{austensmith1996information} showed that strategic voting under incomplete information weakens this guarantee. Our results instantiate the CJT failure mode empirically: when adaptive attacks push individual judges below the critical threshold, panel expansion amplifies error.",
    "new_string": "\\paragraph{Condorcet Jury Theorem.}\n\\citet{condorcet1785essai} proved that majority voting accuracy converges to 1 when per-voter accuracy exceeds 0.5, and to 0 otherwise; \\citet{austensmith1996information} showed that strategic voting under incomplete information weakens this guarantee. The theorem's optimistic prediction rests on voter independence, a condition that correlated LLM outputs systematically violate. Our results instantiate the CJT failure mode empirically: when adaptive attacks push individual judges below the critical threshold, panel expansion amplifies rather than corrects error."
  }
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-22T23:26:07.419364+00:00_

The file /home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/docs/paper/related_work.tex has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_related_work_expansion_20260522T232439",
  "tool": "Edit",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-22T23:26:07.419491+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/docs/paper/related_work.tex",
  "old_string": "\\paragraph{Ensemble Diversity Theory.}\n\\citet{krogh1995neural} proved that ensemble error equals average member error minus a diversity term, and \\citet{brown2005managing} extended this via bias-variance-covariance decomposition. However, \\citet{kuncheva2003measures} found that no single diversity metric reliably predicts ensemble improvement, consistent with our finding that $K_{\\mathrm{eff}}$'s association with vulnerability is statistically fragile under correction. Recent information-theoretic frameworks \\citep{yang2026diversity,turkmen2026ensemble} characterize diversity under benign evaluation; we provide the adversarial complement.",
  "new_string": "\\paragraph{Ensemble Diversity Theory.}\n\\citet{krogh1995neural} proved that ensemble error equals average member error minus a diversity term, establishing the theoretical basis for diversity as a source of ensemble gain. \\citet{brown2005managing} refined this through bias-variance-covariance decomposition, showing that diversity reduces ensemble error by lowering the covariance among members, but only when individual members maintain sufficiently low bias. In our setting, weaker judges introduce bias large enough to offset any diversity benefit, explaining why heterogeneous panels do not outperform homogeneous strong-judge panels under attack. \\citet{kuncheva2003measures} tested ten pairwise diversity measures across multiple classifier ensembles and found that none reliably predicted ensemble improvement. Our $K_{\\mathrm{eff}}$ metric exhibits a similar pattern: it reaches OLS significance as a predictor of panel vulnerability but loses significance after multiple-testing correction, corroborating their conclusion that diversity metrics are poor proxies for ensemble performance. Recent information-theoretic frameworks \\citep{yang2026diversity,turkmen2026ensemble} characterize diversity under benign evaluation; we provide the adversarial complement."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_related_work_expansion_20260522T232439",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/docs/paper/related_work.tex",
    "old_string": "\\paragraph{Ensemble Diversity Theory.}\n\\citet{krogh1995neural} proved that ensemble error equals average member error minus a diversity term, and \\citet{brown2005managing} extended this via bias-variance-covariance decomposition. However, \\citet{kuncheva2003measures} found that no single diversity metric reliably predicts ensemble improvement, consistent with our finding that $K_{\\mathrm{eff}}$'s association with vulnerability is statistically fragile under correction. Recent information-theoretic frameworks \\citep{yang2026diversity,turkmen2026ensemble} characterize diversity under benign evaluation; we provide the adversarial complement.",
    "new_string": "\\paragraph{Ensemble Diversity Theory.}\n\\citet{krogh1995neural} proved that ensemble error equals average member error minus a diversity term, establishing the theoretical basis for diversity as a source of ensemble gain. \\citet{brown2005managing} refined this through bias-variance-covariance decomposition, showing that diversity reduces ensemble error by lowering the covariance among members, but only when individual members maintain sufficiently low bias. In our setting, weaker judges introduce bias large enough to offset any diversity benefit, explaining why heterogeneous panels do not outperform homogeneous strong-judge panels under attack. \\citet{kuncheva2003measures} tested ten pairwise diversity measures across multiple classifier ensembles and found that none reliably predicted ensemble improvement. Our $K_{\\mathrm{eff}}$ metric exhibits a similar pattern: it reaches OLS significance as a predictor of panel vulnerability but loses significance after multiple-testing correction, corroborating their conclusion that diversity metrics are poor proxies for ensemble performance. Recent information-theoretic frameworks \\citep{yang2026diversity,turkmen2026ensemble} characterize diversity under benign evaluation; we provide the adversarial complement."
  }
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-22T23:26:07.419680+00:00_

The file /home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/docs/paper/related_work.tex has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_related_work_expansion_20260522T232439",
  "tool": "Edit",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-22T23:26:07.419810+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/docs/paper/related_work.tex",
  "old_string": "\\paragraph{Adversarial Robustness and Transferability.}\nAdversarial vulnerability was formalized by \\citet{goodfellow2015adversarial}, with transferability demonstrated by \\citet{papernot2016transferability,papernot2017practical}. \\citet{tramer2018ensemble} showed ensemble adversarial training improves but does not eliminate cross-model vulnerability. Controlled diversity via uncorrelated gradients \\citep{kariyappa2019improving} or adaptive diversity regularization \\citep{pang2019improving} can improve robustness in vision models, but LLM judge panels lack such training coordination; their diversity arises incidentally from architectural differences.",
  "new_string": "\\paragraph{Adversarial Robustness and Transferability.}\nAdversarial vulnerability was formalized by \\citet{goodfellow2015adversarial}, with transferability demonstrated by \\citet{papernot2016transferability,papernot2017practical}. \\citet{tramer2018ensemble} introduced ensemble adversarial training, incorporating adversarial examples from held-out models during training. This improved robustness over single-model defenses but did not eliminate cross-model vulnerability: attacks crafted against one ensemble member still transferred to others at reduced but non-negligible rates. Controlled diversity via uncorrelated gradients \\citep{kariyappa2019improving} or adaptive diversity regularization \\citep{pang2019improving} further strengthens ensemble robustness in vision models, but both methods require coordinating member training to explicitly decorrelate loss surfaces. LLM judge panels lack this training-time control entirely: judges are selected post hoc from independently developed model families, and their diversity arises incidentally from architectural and data differences rather than from any robustness-oriented objective."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_related_work_expansion_20260522T232439",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/docs/paper/related_work.tex",
    "old_string": "\\paragraph{Adversarial Robustness and Transferability.}\nAdversarial vulnerability was formalized by \\citet{goodfellow2015adversarial}, with transferability demonstrated by \\citet{papernot2016transferability,papernot2017practical}. \\citet{tramer2018ensemble} showed ensemble adversarial training improves but does not eliminate cross-model vulnerability. Controlled diversity via uncorrelated gradients \\citep{kariyappa2019improving} or adaptive diversity regularization \\citep{pang2019improving} can improve robustness in vision models, but LLM judge panels lack such training coordination; their diversity arises incidentally from architectural differences.",
    "new_string": "\\paragraph{Adversarial Robustness and Transferability.}\nAdversarial vulnerability was formalized by \\citet{goodfellow2015adversarial}, with transferability demonstrated by \\citet{papernot2016transferability,papernot2017practical}. \\citet{tramer2018ensemble} introduced ensemble adversarial training, incorporating adversarial examples from held-out models during training. This improved robustness over single-model defenses but did not eliminate cross-model vulnerability: attacks crafted against one ensemble member still transferred to others at reduced but non-negligible rates. Controlled diversity via uncorrelated gradients \\citep{kariyappa2019improving} or adaptive diversity regularization \\citep{pang2019improving} further strengthens ensemble robustness in vision models, but both methods require coordinating member training to explicitly decorrelate loss surfaces. LLM judge panels lack this training-time control entirely: judges are selected post hoc from independently developed model families, and their diversity arises incidentally from architectural and data differences rather than from any robustness-oriented objective."
  }
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-22T23:26:07.419974+00:00_

The file /home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/docs/paper/related_work.tex has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_related_work_expansion_20260522T232439",
  "tool": "Edit",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-22T23:26:07.420104+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/docs/paper/related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_related_work_expansion_20260522T232439",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/docs/paper/related_work.tex"
  }
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-22T23:26:07.420250+00:00_

1	\section{Related Work}
2	
3	\paragraph{LLM-as-Judge and Multi-Judge Evaluation.}
4	LLM judges gained traction after \citet{zheng2023judging} established them as scalable alternatives to human annotation. \citet{wang2023fair} documented systematic failure modes (position bias, verbosity preferences, sycophancy), motivating multi-judge panels as a mitigation strategy. The idea of aggregating multiple noisy annotators traces back to \citet{dawid1979maximum}, who derived EM-based estimation of individual error rates from disagreement patterns; LLM judge panels inherit this multi-annotator structure but introduce correlated failure modes absent in classical settings. \citet{verga2024replacing} showed that diverse panels can match single large judges, and \citet{panickssery2024llm} identified self-preference bias as a mechanism for within-family correlations. On the evaluation design side, \citet{li2023alpacaeval} operationalized multi-judge comparison through automated win-rate estimation across model pairs, while \citet{ye2024flask} decomposed holistic judgment into fine-grained skill dimensions, enabling per-capability diagnosis. These frameworks assume benign evaluation conditions; we test whether their aggregation benefits survive adversarial manipulation. \citet{almasoud2026security} reported that 7-model committees reduce attack success rates from 50--68\% to 10--19\%, but did not disentangle diversity from individual robustness, precisely the gap we address.
5	
6	\paragraph{Condorcet Jury Theorem.}
7	\citet{condorcet1785essai} proved that majority voting accuracy converges to 1 when per-voter accuracy exceeds 0.5, and to 0 otherwise; \citet{austensmith1996information} showed that strategic voting under incomplete information weakens this guarantee. The theorem's optimistic prediction rests on voter independence, a condition that correlated LLM outputs systematically violate. Our results instantiate the CJT failure mode empirically: when adaptive attacks push ind
…[truncated 3868 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_related_work_expansion_20260522T232439",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-22T23:26:07.420385+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "wc -w /home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/docs/paper/related_work.tex",
  "description": "Count words in related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_related_work_expansion_20260522T232439",
  "tool": "Bash",
  "tool_args": {
    "command": "wc -w /home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/docs/paper/related_work.tex",
    "description": "Count words in related_work.tex"
  }
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-22T23:26:07.420496+00:00_

636 /home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/docs/paper/related_work.tex

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_related_work_expansion_20260522T232439",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 21 · 2026-05-22T23:26:07.420664+00:00_

636 词（含 LaTeX 命令），目标范围内。各段扩展完成：

1. **LLM-as-Judge**: 加入 Dawid & Skene（多标注者聚合渊源）、AlpacaEval（win-rate 自动化）、FLASK（fine-grained 评估），并加了一句过渡将这些 benign 框架与我们的 adversarial 测试连接。
2. **Condorcet**: 加了一句关于 voter independence 条件被 LLM 相关性违反的说明。
3. **Ensemble Diversity**: 展开了 Brown et al. 的 bias-variance-covariance 分解（弱模型 bias 抵消多样性收益），展开了 Kuncheva & Whitaker 的十种度量测试结果与我们 $K_{\mathrm{eff}}$ 的对应关系。
4. **Adversarial Robustness**: 展开了 Tramer et al. 的结果（提升但未消除跨模型漏洞），明确了 Kariyappa/Pang 依赖训练时协调而 LLM 面板缺乏这种控制。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_paper_writing_related_work_expansion_20260522T232439"
}
```

</details>

---
