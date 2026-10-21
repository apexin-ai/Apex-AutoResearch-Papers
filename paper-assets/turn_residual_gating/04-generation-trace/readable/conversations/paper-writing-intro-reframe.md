# paper writing intro reframe

**Exposure Bias Collapses Auxiliary Attention Losses in Multi-Turn Dialogue** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 15
- **Recorded user turns:** 0
- **Tool calls:** 7
- **Original source:** `logs/chats/worker_paper_writing_intro_reframe_20260520T040823.jsonl`
- **Structured JSON:** [`f3c7c304662af2bfde1b.json`](../../sessions/f3/f3c7c304662af2bfde1b.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

15 recorded events

### Tool call

_source line 1 · 2026-05-20T04:10:53.345696+00:00_

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
  "session": "worker_paper_writing_intro_reframe_20260520T040823",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/agent-ml-research/skills/global/paper-writing-norms.skill.md"
  }
}
```

</details>

---

### Tool result

_source line 2 · 2026-05-20T04:10:53.346310+00:00_

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
  "session": "worker_paper_writing_intro_reframe_20260520T040823",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-20T04:10:53.346544+00:00_

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
  "session": "worker_paper_writing_intro_reframe_20260520T040823",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/agent-ml-research/skills/global/latex-paper.skill.md"
  }
}
```

</details>

---

### Tool result

_source line 4 · 2026-05-20T04:10:53.346985+00:00_

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
  "session": "worker_paper_writing_intro_reframe_20260520T040823",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-20T04:10:53.347157+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_intro_reframe_20260520T040823",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/introduction.tex"
  }
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-20T04:10:53.347319+00:00_

1	\section{Introduction}\label{sec:introduction}
2	
3	Multi-turn dialogue is the dominant mode of interaction with large language models (LLMs), and system prompts that specify task goals form the foundation of instruction following. As conversations grow longer, however, models progressively lose track of these goal specifications. \citet{dongre2026attention} quantified this degradation across 12 models: the Goal Attention Ratio (GAR), which measures how much attention the model allocates to goal tokens in the system prompt, declines by 27--48\% between early and mid-conversation turns. We replicate and extend this finding on Qwen-2.5-7B-Instruct, observing a 70.8\% relative decline in GAR from 0.0418 at turn~1 to 0.0122 at mid-conversation. We attribute the steeper decline partly to our use of last-token GAR, which captures summary-position attention more sensitively than the all-token average of \citet{dongre2026attention}, and partly to Qwen-2.5-7B's stronger instruction-following fidelity in early turns. This attention decay represents a systematic failure of multi-turn models to maintain task coherence, and it grows worse with each additional turn.
4	
5	A striking aspect of this degradation is what it does \emph{not} affect. \citet{dongre2026attention} showed that goal-relevant information persists in the residual stream throughout the conversation: linear discriminant analysis probes recover goal content with AUC\,=\,0.98 even at late turns where attention to goal tokens has collapsed. The information is present in the hidden states, but the attention mechanism fails to route it toward the output computation. This dissociation between information availability and information utilization suggests a natural intervention: if the residual stream already carries goal information, a learnable gate on the residual pathway could amplify or attenuate layer contributions to recover goal attention. This reasoning motivates ThreadGate, which modulates each residual updat
…[truncated 3479 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_intro_reframe_20260520T040823",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-20T04:10:53.347652+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/introduction.tex",
  "old_string": "To isolate the contributions of gating and gradient conflict, we evaluate five configurations: ThreadGate (turn-conditioned gates), +PCGrad (ThreadGate with gradient conflict elimination), Uniform Gate (content-only gates), LoRA-only (gates fixed at 1.0), and the unmodified Base model. This factorial design supports four targeted comparisons that separate gradient conflict, turn conditioning, gating as a mechanism, and fine-tuning itself (\\S\\ref{sec:experiments}).",
  "new_string": "To diagnose why the auxiliary objective fails under generation, we construct a causal diagnostic framework built on a five-way factorial comparison: ThreadGate (turn-conditioned gates), +PCGrad (ThreadGate with gradient conflict elimination), Uniform Gate (content-only gates), LoRA-only (gates fixed at 1.0), and the unmodified Base model. Each adjacent pair isolates exactly one causal factor (gradient conflict, turn conditioning, gating mechanism, or fine-tuning) and produces four targeted causal contrasts (\\S\\ref{sec:experiments}). PCGrad \\citep{yu2020pcgrad} serves a dual role in this framework: beyond a training strategy, it functions as a causal exclusion tool that rules out gradient direction conflict as a candidate explanation."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_intro_reframe_20260520T040823",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/introduction.tex",
    "old_string": "To isolate the contributions of gating and gradient conflict, we evaluate five configurations: ThreadGate (turn-conditioned gates), +PCGrad (ThreadGate with gradient conflict elimination), Uniform Gate (content-only gates), LoRA-only (gates fixed at 1.0), and the unmodified Base model. This factorial design supports four targeted comparisons that separate gradient conflict, turn conditioning, gating as a mechanism, and fine-tuning itself (\\S\\ref{sec:experiments}).",
    "new_string": "To diagnose why the auxiliary objective fails under generation, we construct a causal diagnostic framework built on a five-way factorial comparison: ThreadGate (turn-conditioned gates), +PCGrad (ThreadGate with gradient conflict elimination), Uniform Gate (content-only gates), LoRA-only (gates fixed at 1.0), and the unmodified Base model. Each adjacent pair isolates exactly one causal factor (gradient conflict, turn conditioning, gating mechanism, or fine-tuning) and produces four targeted causal contrasts (\\S\\ref{sec:experiments}). PCGrad \\citep{yu2020pcgrad} serves a dual role in this framework: beyond a training strategy, it functions as a causal exclusion tool that rules out gradient direction conflict as a candidate explanation."
  }
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-20T04:10:53.347996+00:00_

The file /home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/introduction.tex has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_intro_reframe_20260520T040823",
  "tool": "Edit",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-20T04:10:53.348186+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/introduction.tex",
  "old_string": "Training succeeds: teacher-forced GAR-ours reaches 0.50 across all fine-tuned variants. The failure emerges under autoregressive generation, where GAR-ours drops to 0.015--0.025, a 20--33$\\times$ gap that persists across all training strategies. All four fine-tuned variants achieve indistinguishable performance (0.75\\,pp spread on GAR-ours, identical PPL at 2.78), confirming that gating contributes zero measurable benefit. A PCGrad \\citep{yu2020pcgrad} experiment eliminates gradient direction conflict without altering any outcome, establishing that conflict is neither necessary nor sufficient for the failure. The root failure is exposure bias \\citep{bengio2015scheduled}: attention patterns optimized under teacher-forced prefixes do not transfer to model-generated text (Figure~\\ref{fig:overview}).",
  "new_string": "Training succeeds: teacher-forced GAR-ours reaches 0.50 across all fine-tuned variants. The factorial comparison reveals that the failure is specific to autoregressive generation, where GAR-ours drops to 0.015--0.025, a 20--33$\\times$ gap that persists across all training strategies. All four fine-tuned variants achieve indistinguishable performance (0.75\\,pp spread on GAR-ours, identical PPL at 2.78); the gating contrast confirms that gates contribute zero measurable benefit. The PCGrad causal exclusion eliminates gradient direction conflict without altering any outcome, establishing that conflict is neither necessary nor sufficient for the failure. These four contrasts converge on a single root cause: exposure bias \\citep{bengio2015scheduled}, where attention patterns optimized under teacher-forced prefixes do not transfer to model-generated text (Figure~\\ref{fig:overview})."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_intro_reframe_20260520T040823",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/introduction.tex",
    "old_string": "Training succeeds: teacher-forced GAR-ours reaches 0.50 across all fine-tuned variants. The failure emerges under autoregressive generation, where GAR-ours drops to 0.015--0.025, a 20--33$\\times$ gap that persists across all training strategies. All four fine-tuned variants achieve indistinguishable performance (0.75\\,pp spread on GAR-ours, identical PPL at 2.78), confirming that gating contributes zero measurable benefit. A PCGrad \\citep{yu2020pcgrad} experiment eliminates gradient direction conflict without altering any outcome, establishing that conflict is neither necessary nor sufficient for the failure. The root failure is exposure bias \\citep{bengio2015scheduled}: attention patterns optimized under teacher-forced prefixes do not transfer to model-generated text (Figure~\\ref{fig:overview}).",
    "new_string": "Training succeeds: teacher-forced GAR-ours reaches 0.50 across all fine-tuned variants. The factorial comparison reveals that the failure is specific to autoregressive generation, where GAR-ours drops to 0.015--0.025, a 20--33$\\times$ gap that persists across all training strategies. All four fine-tuned variants achieve indistinguishable performance (0.75\\,pp spread on GAR-ours, identical PPL at 2.78); the gating contrast confirms that gates contribute zero measurable benefit. The PCGrad causal exclusion eliminates gradient direction conflict without altering any outcome, establishing that conflict is neither necessary nor sufficient for the failure. These four contrasts converge on a single root cause: exposure bias \\citep{bengio2015scheduled}, where attention patterns optimized under teacher-forced prefixes do not transfer to model-generated text (Figure~\\ref{fig:overview})."
  }
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-20T04:10:53.348380+00:00_

The file /home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/introduction.tex has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_intro_reframe_20260520T040823",
  "tool": "Edit",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-20T04:10:53.348542+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/introduction.tex",
  "old_string": "Our contributions: (1)~the first empirical characterization of how exposure bias selectively destroys auxiliary attention loss generalization (20--33$\\times$ gap across all training strategies) while leaving NTP robust, showing that token-level self-recovery \\citep{he2019exposure} does not extend to auxiliary objectives; (2)~a PCGrad causal exclusion establishing that gradient direction conflict is neither necessary nor sufficient for the failure (\\S\\ref{sec:analysis}); (3)~ThreadGate and a five-way comparison providing a principled negative baseline, with seven loss formulations and four training configurations ruled out (\\S\\ref{sec:method}, \\S\\ref{sec:experiments}).",
  "new_string": "Our contributions: (1)~a systematic causal diagnostic framework for analyzing auxiliary objective failures in multi-turn dialogue, comprising a five-way factorial comparison that isolates four causal factors (turn conditioning, gating mechanism, gradient conflict, and fine-tuning), PCGrad-based causal exclusion via gradient surgery \\citep{yu2020pcgrad}, and per-layer gradient conflict quantification; this framework generalizes to other auxiliary objective analyses (\\S\\ref{sec:method}, \\S\\ref{sec:experiments}, \\S\\ref{sec:analysis}); (2)~using this framework, the first empirical characterization of how exposure bias selectively destroys auxiliary attention loss generalization (20--33$\\times$ gap) while leaving NTP robust, with evidence that token-level self-recovery \\citep{he2019exposure} does not extend to auxiliary objectives; (3)~a principled negative baseline for future attention steering research: ThreadGate with seven loss formulations and four training configurations ruled out (\\S\\ref{sec:method}, \\S\\ref{sec:experiments})."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_intro_reframe_20260520T040823",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/introduction.tex",
    "old_string": "Our contributions: (1)~the first empirical characterization of how exposure bias selectively destroys auxiliary attention loss generalization (20--33$\\times$ gap across all training strategies) while leaving NTP robust, showing that token-level self-recovery \\citep{he2019exposure} does not extend to auxiliary objectives; (2)~a PCGrad causal exclusion establishing that gradient direction conflict is neither necessary nor sufficient for the failure (\\S\\ref{sec:analysis}); (3)~ThreadGate and a five-way comparison providing a principled negative baseline, with seven loss formulations and four training configurations ruled out (\\S\\ref{sec:method}, \\S\\ref{sec:experiments}).",
    "new_string": "Our contributions: (1)~a systematic causal diagnostic framework for analyzing auxiliary objective failures in multi-turn dialogue, comprising a five-way factorial comparison that isolates four causal factors (turn conditioning, gating mechanism, gradient conflict, and fine-tuning), PCGrad-based causal exclusion via gradient surgery \\citep{yu2020pcgrad}, and per-layer gradient conflict quantification; this framework generalizes to other auxiliary objective analyses (\\S\\ref{sec:method}, \\S\\ref{sec:experiments}, \\S\\ref{sec:analysis}); (2)~using this framework, the first empirical characterization of how exposure bias selectively destroys auxiliary attention loss generalization (20--33$\\times$ gap) while leaving NTP robust, with evidence that token-level self-recovery \\citep{he2019exposure} does not extend to auxiliary objectives; (3)~a principled negative baseline for future attention steering research: ThreadGate with seven loss formulations and four training configurations ruled out (\\S\\ref{sec:method}, \\S\\ref{sec:experiments})."
  }
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-20T04:10:53.348717+00:00_

The file /home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/introduction.tex has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_intro_reframe_20260520T040823",
  "tool": "Edit",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-20T04:10:53.348855+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_intro_reframe_20260520T040823",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/introduction.tex"
  }
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-20T04:10:53.349006+00:00_

1	\section{Introduction}\label{sec:introduction}
2	
3	Multi-turn dialogue is the dominant mode of interaction with large language models (LLMs), and system prompts that specify task goals form the foundation of instruction following. As conversations grow longer, however, models progressively lose track of these goal specifications. \citet{dongre2026attention} quantified this degradation across 12 models: the Goal Attention Ratio (GAR), which measures how much attention the model allocates to goal tokens in the system prompt, declines by 27--48\% between early and mid-conversation turns. We replicate and extend this finding on Qwen-2.5-7B-Instruct, observing a 70.8\% relative decline in GAR from 0.0418 at turn~1 to 0.0122 at mid-conversation. We attribute the steeper decline partly to our use of last-token GAR, which captures summary-position attention more sensitively than the all-token average of \citet{dongre2026attention}, and partly to Qwen-2.5-7B's stronger instruction-following fidelity in early turns. This attention decay represents a systematic failure of multi-turn models to maintain task coherence, and it grows worse with each additional turn.
4	
5	A striking aspect of this degradation is what it does \emph{not} affect. \citet{dongre2026attention} showed that goal-relevant information persists in the residual stream throughout the conversation: linear discriminant analysis probes recover goal content with AUC\,=\,0.98 even at late turns where attention to goal tokens has collapsed. The information is present in the hidden states, but the attention mechanism fails to route it toward the output computation. This dissociation between information availability and information utilization suggests a natural intervention: if the residual stream already carries goal information, a learnable gate on the residual pathway could amplify or attenuate layer contributions to recover goal attention. This reasoning motivates ThreadGate, which modulates each residual updat
…[truncated 4203 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_intro_reframe_20260520T040823",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 15 · 2026-05-20T04:10:53.349217+00:00_

修改完成。三处变更：

**段落3**（line 14）：将 "To isolate the contributions..." 重写为 "To diagnose why the auxiliary objective fails under generation, we construct a causal diagnostic framework..."。强调 five-way comparison 是 factorial causal design，每对相邻配置隔离一个因果因素。新增 PCGrad 双重角色的阐述（训练策略 + 因果排除工具）。

**段落4**（line 16）：四处措辞微调，将被动观察语气转为框架产出语气：
- "The failure emerges" → "The factorial comparison reveals that the failure is specific to"
- "confirming that gating contributes" → "the gating contrast confirms that gates contribute"
- "A PCGrad experiment eliminates" → "The PCGrad causal exclusion eliminates"
- "The root failure is" → "These four contrasts converge on a single root cause:"

**Contribution list**（line 18）：重排为框架→发现→negative baseline 三条：
1. 方法论框架（five-way factorial + PCGrad causal exclusion + gradient conflict quantification，可复用）
2. 核心发现（exposure bias 选择性摧毁 auxiliary loss，前缀 "using this framework"）
3. Negative baseline（ThreadGate + 7 loss + 4 config ruled out）

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_paper_writing_intro_reframe_20260520T040823"
}
```

</details>

---
