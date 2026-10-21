# paper writing related work r5 revision

**The Weakest Link Across Panel Sizes: Predictor Relevance Patterns in Multi-Judge LLM Evaluation under Adversarial Manipulation** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 11
- **Recorded user turns:** 0
- **Tool calls:** 5
- **Original source:** `logs/chats/worker_paper_writing_related_work_r5_revision_20260524T044714.jsonl`
- **Structured JSON:** [`447e083ea0071e8bd9d2.json`](../../sessions/44/447e083ea0071e8bd9d2.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

11 recorded events

### Tool call

_source line 1 · 2026-05-24T04:48:35.739412+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/agent-ml-research/skills/global/paper-writing-norms.skill.md",
  "limit": "80"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_related_work_r5_revision_20260524T044714",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/agent-ml-research/skills/global/paper-writing-norms.skill.md",
    "limit": "80"
  }
}
```

</details>

---

### Tool result

_source line 2 · 2026-05-24T04:48:35.739986+00:00_

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
…[truncated 194 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_related_work_r5_revision_20260524T044714",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-24T04:48:35.740178+00:00_

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
  "session": "worker_paper_writing_related_work_r5_revision_20260524T044714",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/docs/paper/related_work.tex"
  }
}
```

</details>

---

### Tool result

_source line 4 · 2026-05-24T04:48:35.740352+00:00_

1	\section{Related Work}
2	
3	\paragraph{LLM-as-Judge and Multi-Judge Evaluation.}
4	LLM judges gained traction after \citet{zheng2023judging} established them as scalable alternatives to human annotation. \citet{wang2023fair} documented systematic failure modes (position bias, verbosity, sycophancy), motivating multi-judge panels; \citet{raina2024judgerobust} quantified robustness gaps under universal adversarial attacks, \citet{maloyan2025investigating} demonstrated prompt injection vulnerabilities in LLM-as-a-judge systems, and \citet{stureborg2024inconsistent} and \citet{ye2024justice} further catalogued inconsistency and bias in LLM evaluators. Aggregating noisy annotators traces back to \citet{dawid1979maximum}; \citet{verga2024replacing} showed diverse panels can match single large judges, and \citet{panickssery2024llm} identified self-preference bias driving within-family correlations. These frameworks assume benign conditions; we test whether aggregation benefits survive adversarial manipulation. \citet{almasoud2026security} reported that 7-model committees reduce ASR from 50--68\% to 10--19\%, but did not disentangle diversity from individual robustness. \citet{tamas2025benchmarking} benchmark adversarial risks in multi-agent LLM systems but focus on agent coordination rather than judge panel composition.
5	
6	\paragraph{Condorcet Jury Theorem.}
7	\citet{condorcet1785essai} proved that majority voting accuracy converges to 1 when per-voter accuracy exceeds 0.5; \citet{ladha1992condorcet} extended the theorem to correlated voters, showing that positive correlation weakens the convergence guarantee. CJT explicitly assumes independent, non-adversarial errors. Under adaptive adversaries, its predictions do not apply, a point well-established in adversarial ML \citep{tramer2018ensemble}. Our contribution is not the direction (diversity increases vulnerability, which follows from the wider attack surface argument), but the \emph{panel-size-dependent structure}: 
…[truncated 3519 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_related_work_r5_revision_20260524T044714",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-24T04:48:35.740564+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/docs/paper/related_work.tex",
  "old_string": "CJT explicitly assumes independent, non-adversarial errors. Under adaptive adversaries, its predictions do not apply, a point well-established in adversarial ML \\citep{tramer2018ensemble}. Our contribution is not the direction (diversity increases vulnerability, which follows from the wider attack surface argument), but the \\emph{panel-size-dependent structure}: the shift from both predictors contributing at $K{=}3$ to $K_{\\mathrm{eff}}$ dominance at $K{\\geq}5$.",
  "new_string": "CJT explicitly assumes independent, non-adversarial errors; its failure under adaptive adversaries is trivially expected, since the adversary optimizes against the aggregate decision boundary rather than individual voters---a point formalized in ensemble adversarial training \\citep{tramer2018ensemble} and gradient-diversity defenses \\citep{kariyappa2019improving,pang2019improving}. Our contribution is not this well-known direction (diversity widens the joint attack surface across heterogeneous models), but the \\emph{panel-size-dependent structure}: the predictor shift from both predictors contributing at $K{=}3$ to $K_{\\mathrm{eff}}$ dominance at $K{\\geq}5$."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_related_work_r5_revision_20260524T044714",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/docs/paper/related_work.tex",
    "old_string": "CJT explicitly assumes independent, non-adversarial errors. Under adaptive adversaries, its predictions do not apply, a point well-established in adversarial ML \\citep{tramer2018ensemble}. Our contribution is not the direction (diversity increases vulnerability, which follows from the wider attack surface argument), but the \\emph{panel-size-dependent structure}: the shift from both predictors contributing at $K{=}3$ to $K_{\\mathrm{eff}}$ dominance at $K{\\geq}5$.",
    "new_string": "CJT explicitly assumes independent, non-adversarial errors; its failure under adaptive adversaries is trivially expected, since the adversary optimizes against the aggregate decision boundary rather than individual voters---a point formalized in ensemble adversarial training \\citep{tramer2018ensemble} and gradient-diversity defenses \\citep{kariyappa2019improving,pang2019improving}. Our contribution is not this well-known direction (diversity widens the joint attack surface across heterogeneous models), but the \\emph{panel-size-dependent structure}: the predictor shift from both predictors contributing at $K{=}3$ to $K_{\\mathrm{eff}}$ dominance at $K{\\geq}5$."
  }
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-24T04:48:35.740791+00:00_

The file /home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/docs/paper/related_work.tex has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_related_work_r5_revision_20260524T044714",
  "tool": "Edit",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-24T04:48:35.740933+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/docs/paper/related_work.tex",
  "old_string": "\\citet{kuai2026independent} propose difficulty-based entanglement indexing (DBEI) to measure judge correlation; $K_{\\mathrm{eff}}$ differs by using Gaussian copula MI for pairwise independence, connecting to the SDPI vulnerability bound. De-entangled reweighting \\citep{kuai2026independent} and credibility scoring \\citep{ebrahimi2025adversary} are promising aggregation strategies that may complement our Bayesian calibration baseline.",
  "new_string": "\\citet{kuai2026independent} propose the Difficulty-Weighted Behavioral Entanglement Index (DBEI) to measure judge correlation, weighting agreement patterns by item difficulty so that correlated failures on hard items are penalized more heavily. $K_{\\mathrm{eff}}$ captures a complementary dimension: Gaussian copula MI quantifies pairwise statistical independence regardless of item difficulty, connecting directly to the SDPI vulnerability bound. Their de-entangled reweighting and our Bayesian calibration baseline both mitigate judge correlation, but through different mechanisms: reweighting decomposes correlation along a difficulty axis and downweights entangled judges, whereas Bayesian calibration shrinks each judge's influence toward a clean-accuracy prior. Credibility scoring \\citep{ebrahimi2025adversary} offers a third complementary strategy by penalizing judges whose scores deviate from consensus."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_related_work_r5_revision_20260524T044714",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/docs/paper/related_work.tex",
    "old_string": "\\citet{kuai2026independent} propose difficulty-based entanglement indexing (DBEI) to measure judge correlation; $K_{\\mathrm{eff}}$ differs by using Gaussian copula MI for pairwise independence, connecting to the SDPI vulnerability bound. De-entangled reweighting \\citep{kuai2026independent} and credibility scoring \\citep{ebrahimi2025adversary} are promising aggregation strategies that may complement our Bayesian calibration baseline.",
    "new_string": "\\citet{kuai2026independent} propose the Difficulty-Weighted Behavioral Entanglement Index (DBEI) to measure judge correlation, weighting agreement patterns by item difficulty so that correlated failures on hard items are penalized more heavily. $K_{\\mathrm{eff}}$ captures a complementary dimension: Gaussian copula MI quantifies pairwise statistical independence regardless of item difficulty, connecting directly to the SDPI vulnerability bound. Their de-entangled reweighting and our Bayesian calibration baseline both mitigate judge correlation, but through different mechanisms: reweighting decomposes correlation along a difficulty axis and downweights entangled judges, whereas Bayesian calibration shrinks each judge's influence toward a clean-accuracy prior. Credibility scoring \\citep{ebrahimi2025adversary} offers a third complementary strategy by penalizing judges whose scores deviate from consensus."
  }
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-24T04:48:35.741096+00:00_

The file /home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/docs/paper/related_work.tex has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_related_work_r5_revision_20260524T044714",
  "tool": "Edit",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-24T04:48:35.741218+00:00_

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
  "session": "worker_paper_writing_related_work_r5_revision_20260524T044714",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/docs/paper/related_work.tex"
  }
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-24T04:48:35.741366+00:00_

1	\section{Related Work}
2	
3	\paragraph{LLM-as-Judge and Multi-Judge Evaluation.}
4	LLM judges gained traction after \citet{zheng2023judging} established them as scalable alternatives to human annotation. \citet{wang2023fair} documented systematic failure modes (position bias, verbosity, sycophancy), motivating multi-judge panels; \citet{raina2024judgerobust} quantified robustness gaps under universal adversarial attacks, \citet{maloyan2025investigating} demonstrated prompt injection vulnerabilities in LLM-as-a-judge systems, and \citet{stureborg2024inconsistent} and \citet{ye2024justice} further catalogued inconsistency and bias in LLM evaluators. Aggregating noisy annotators traces back to \citet{dawid1979maximum}; \citet{verga2024replacing} showed diverse panels can match single large judges, and \citet{panickssery2024llm} identified self-preference bias driving within-family correlations. These frameworks assume benign conditions; we test whether aggregation benefits survive adversarial manipulation. \citet{almasoud2026security} reported that 7-model committees reduce ASR from 50--68\% to 10--19\%, but did not disentangle diversity from individual robustness. \citet{tamas2025benchmarking} benchmark adversarial risks in multi-agent LLM systems but focus on agent coordination rather than judge panel composition.
5	
6	\paragraph{Condorcet Jury Theorem.}
7	\citet{condorcet1785essai} proved that majority voting accuracy converges to 1 when per-voter accuracy exceeds 0.5; \citet{ladha1992condorcet} extended the theorem to correlated voters, showing that positive correlation weakens the convergence guarantee. CJT explicitly assumes independent, non-adversarial errors; its failure under adaptive adversaries is trivially expected, since the adversary optimizes against the aggregate decision boundary rather than individual voters---a point formalized in ensemble adversarial training \citep{tramer2018ensemble} and gradient-diversity defenses \citep{kariyappa2019improving,
…[truncated 4196 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_related_work_r5_revision_20260524T044714",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 11 · 2026-05-24T04:48:35.741545+00:00_

全部修改完成。总结：

- **Task 1 (M4)**: CJT paragraph — 将 CJT 在 adaptive adversary 下的失效标记为 "trivially expected"，并将 "wider attack surface argument" 具体连接到 Tramèr 2018 ensemble adversarial training 和 Kariyappa/Pang gradient-diversity defenses；使用 "predictor shift" 术语。
- **Task 2 (M4)**: Adversarial Robustness paragraph — 3 个差异已完整列出，保持不变。
- **Task 3 (S6)**: Kuai et al. 讨论从 2 句扩展到 4 句，增加了 DBEI 的 difficulty-weighting 机制说明、K_eff 与 DBEI 衡量不同维度的对比、de-entangled reweighting 与 Bayesian calibration 的机制差异。
- **S5 确认**: 3 篇新引用 (maloyan2025, tamas2025, ebrahimi2025) 均已存在。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_paper_writing_related_work_r5_revision_20260524T044714"
}
```

</details>

---
