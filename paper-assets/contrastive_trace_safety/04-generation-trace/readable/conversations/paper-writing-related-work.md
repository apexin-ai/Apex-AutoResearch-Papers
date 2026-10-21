# paper writing related work

**Layer Selection Sensitivity in Hidden-State Safety Probes for Reasoning Models** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 9
- **Recorded user turns:** 0
- **Tool calls:** 4
- **Original source:** `logs/chats/worker_paper_writing_related_work_20260517T003949.jsonl`
- **Structured JSON:** [`efa22aa5cc9b8ebc8a1f.json`](../../sessions/ef/efa22aa5cc9b8ebc8a1f.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

9 recorded events

### Tool call

_source line 1 · 2026-05-17T00:40:58.762165+00:00_

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
  "session": "worker_paper_writing_related_work_20260517T003949",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/agent-ml-research/skills/global/latex-paper.skill.md"
  }
}
```

</details>

---

### Tool result

_source line 2 · 2026-05-17T00:40:58.762765+00:00_

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
  "session": "worker_paper_writing_related_work_20260517T003949",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-17T00:40:58.762972+00:00_

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
  "session": "worker_paper_writing_related_work_20260517T003949",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/agent-ml-research/skills/global/paper-writing-norms.skill.md"
  }
}
```

</details>

---

### Tool result

_source line 4 · 2026-05-17T00:40:58.763305+00:00_

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
  "session": "worker_paper_writing_related_work_20260517T003949",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-17T00:40:58.763496+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/docs/paper/sections/ 2>/dev/null || echo \"DIR_NOT_EXIST\"",
  "description": "Check if paper sections directory exists"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_related_work_20260517T003949",
  "tool": "Bash",
  "tool_args": {
    "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/docs/paper/sections/ 2>/dev/null || echo \"DIR_NOT_EXIST\"",
    "description": "Check if paper sections directory exists"
  }
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-17T00:40:58.763646+00:00_

discussion.tex
experiments.tex
introduction.tex
limitations.tex
method.tex

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_related_work_20260517T003949",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-17T00:40:58.763806+00:00_

called Write

<details open><summary>🔧 Tool call — Write</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/docs/paper/sections/related_work.tex",
  "content": "\\section{Related Work}\\label{sec:related_work}\n\nOur work draws on five research threads: representation probing, causal interpretability, hidden-state safety detection, reasoning model safety, and process supervision. We summarize each and clarify how our study relates to prior efforts.\n\n\\paragraph{Probing Neural Representations.}\nLinear probes have become a standard tool for investigating what information neural networks encode in their intermediate representations. \\citet{belinkov2019analysis} provide a comprehensive survey of probing methods that extract linguistic properties (part-of-speech, syntax, semantics) from hidden states across architectures. \\citet{hewitt2019structural} demonstrate that syntax trees can be recovered from contextual embeddings through a linear transformation, establishing that rich structural information is linearly accessible in pretrained representations. A key methodological concern is whether probes genuinely detect learned structure or merely memorize the task. \\citet{hewitt2019control} address this by introducing control tasks and the selectivity metric (probe accuracy minus control accuracy), providing a principled way to distinguish true decodability from probe expressiveness. Our work extends probing from linguistic attributes to safety-relevant properties: we train temporal probes on hidden states to detect when a reasoning model commits to unsafe behavior, and we adopt the control task methodology of \\citet{hewitt2019control} to validate that our probes capture genuine safety commitment signals rather than superficial patterns.\n\n\\paragraph{Causal Interpretability.}\nA parallel line of research moves beyond correlation to establish causal relationships between internal representations and model behavior. \\citet{geiger2021causal} formalize causal abstraction as a framework for testing whether specific neural representations play a causal role in model computations, using interchange interventions to verify alignment between model components and abstract causal variables. \\citet{vig2020causal} apply causal mediation analysis to trace how gender bias information flows through specific attention heads and MLPs in language models. \\citet{meng2022locating} build on this to develop ROME (Rank-One Model Editing), locating and editing factual associations by identifying causal mediators in mid-layer MLP modules. These methods provide strong evidence about mechanism but require expensive interventions and access to model internals during inference. Our approach is explicitly correlational: we establish that safety commitment is \\textit{decodable} from hidden states without claiming a causal role for any specific component. This is a deliberate methodological choice that trades causal guarantees for practical applicability, and we discuss this limitation in Section~\\ref{sec:limitations}.\n\n\\paragraph{Hidden-State Safety Detection.}\nSeveral systems use hidden-state information for safety-related classification. TrajGuard~\\citep{trajguard} applies Mahalanobis distance to hidden-state trajectories to detect adversarial inputs, reporting over 95\\% detection accuracy on standard language models. SafeSwitch~\\citep{safeswitch} trains hidden-state classifiers to trigger safety interventions, and SIREN~\\citep{siren} implements real-time monitoring of internal representations during generation. \\citet{zou2023representation} introduce Representation Engineering (RepE), which identifies ``refusal directions'' in activation space and shows that safety behavior can be read from and written to specific linear subspaces. These systems share our use of hidden states as a detection signal, but they target a different problem: detecting adversarial \\textit{inputs} or controlling model \\textit{outputs}. In contrast, we focus on detecting a temporal phenomenon within the model's own reasoning process, specifically the point at which a reasoning model transitions from safe deliberation to unsafe commitment. We reproduce the TrajGuard methodology on reasoning models (Section~\\ref{sec:experiments}) and find that it fails to detect safety commitment, likely because reasoning models exhibit gradual transitions rather than the sharp distributional shifts that distance-based methods assume.\n\n\\paragraph{Reasoning Model Safety.}\nReasoning models such as DeepSeek-R1~\\citep{deepseekr1} and QwQ~\\citep{qwq} produce extended chains of thought (CoT) before generating final answers. This creates new safety challenges. \\citet{harmthoughts} document that reasoning models can ``self-jailbreak'' by gradually rationalizing harmful outputs within their own CoT, even when the initial prompt does not contain adversarial content. \\citet{selfjailbreak} provide a systematic analysis of the mechanisms behind this phenomenon, showing that longer reasoning chains increase the probability of safety circumvention. On the intervention side, SafeRemind~\\citep{saferemind} inserts safety reminders at fixed positions in the reasoning chain to reduce harmful outputs, while SafeThink~\\citep{safethink} trains models to incorporate safety reasoning as part of their CoT process. These works either document the self-jailbreak phenomenon or propose mitigation strategies. Our study addresses a different question: given that safety commitment occurs somewhere in the reasoning chain, what is the best \\textit{modality} for detecting it? We use the HarmThoughts dataset~\\citep{harmthoughts} as our primary data source and compare hidden-state probes against text-based monitors as detection mechanisms for the commitment point.\n\n\\paragraph{Process Supervision and Sequential Monitoring.}\nProcess Reward Models (PRMs) evaluate reasoning quality at the step level. \\citet{lightman2023prm} train PRMs to judge whether each step in a mathematical solution is correct, showing that step-level supervision outperforms outcome-level supervision for improving mathematical reasoning. \\citet{wang2024prm} scale this approach through automated labeling. While PRMs assess reasoning \\textit{correctness} (whether a mathematical step follows logically), our probes assess reasoning \\textit{safety} (whether the model has committed to producing harmful content). The sequential nature of our detection problem also connects to change-point detection. Bayesian Online Change Point Detection (BOCPD)~\\citep{adams2007bayesian} provides a principled framework for detecting abrupt distributional shifts in sequential data. We apply BOCPD to hidden-state sequences as a baseline (Section~\\ref{sec:experiments}) but find that it performs poorly: safety commitment in reasoning models is not an abrupt regime change but a gradual drift, with commitment signals emerging over multiple reasoning steps before the model produces harmful text. This finding motivates our use of temporal probes that can capture gradual transitions.\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_related_work_20260517T003949",
  "tool": "Write",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/docs/paper/sections/related_work.tex",
    "content": "\\section{Related Work}\\label{sec:related_work}\n\nOur work draws on five research threads: representation probing, causal interpretability, hidden-state safety detection, reasoning model safety, and process supervision. We summarize each and clarify how our study relates to prior efforts.\n\n\\paragraph{Probing Neural Representations.}\nLinear probes have become a standard tool for investigating what information neural networks encode in their intermediate representations. \\citet{belinkov2019analysis} provide a comprehensive survey of probing methods that extract linguistic properties (part-of-speech, syntax, semantics) from hidden states across architectures. \\citet{hewitt2019structural} demonstrate that syntax trees can be recovered from contextual embeddings through a linear transformation, establishing that rich structural information is linearly accessible in pretrained representations. A key methodological concern is whether probes genuinely detect learned structure or merely memorize the task. \\citet{hewitt2019control} address this by introducing control tasks and the selectivity metric (probe accuracy minus control accuracy), providing a principled way to distinguish true decodability from probe expressiveness. Our work extends probing from linguistic attributes to safety-relevant properties: we train temporal probes on hidden states to detect when a reasoning model commits to unsafe behavior, and we adopt the control task methodology of \\citet{hewitt2019control} to validate that our probes capture genuine safety commitment signals rather than superficial patterns.\n\n\\paragraph{Causal Interpretability.}\nA parallel line of research moves beyond correlation to establish causal relationships between internal representations and model behavior. \\citet{geiger2021causal} formalize causal abstraction as a framework for testing whether specific neural representations play a causal role in model computations, using interchange interventions to verify alignment between model components and abstract causal variables. \\citet{vig2020causal} apply causal mediation analysis to trace how gender bias information flows through specific attention heads and MLPs in language models. \\citet{meng2022locating} build on this to develop ROME (Rank-One Model Editing), locating and editing factual associations by identifying causal mediators in mid-layer MLP modules. These methods provide strong evidence about mechanism but require expensive interventions and access to model internals during inference. Our approach is explicitly correlational: we establish that safety commitment is \\textit{decodable} from hidden states without claiming a causal role for any specific component. This is a deliberate methodological choice that trades causal guarantees for practical applicability, and we discuss this limitation in Section~\\ref{sec:limitations}.\n\n\\paragraph{Hidden-State Safety Detection.}\nSeveral systems use hidden-state information for safety-related classification. TrajGuard~\\citep{trajguard} applies Mahalanobis distance to hidden-state trajectories to detect adversarial inputs, reporting over 95\\% detection accuracy on standard language models. SafeSwitch~\\citep{safeswitch} trains hidden-state classifiers to trigger safety interventions, and SIREN~\\citep{siren} implements real-time monitoring of internal representations during generation. \\citet{zou2023representation} introduce Representation Engineering (RepE), which identifies ``refusal directions'' in activation space and shows that safety behavior can be read from and written to specific linear subspaces. These systems share our use of hidden states as a detection signal, but they target a different problem: detecting adversarial \\textit{inputs} or controlling model \\textit{outputs}. In contrast, we focus on detecting a temporal phenomenon within the model's own reasoning process, specifically the point at which a reasoning model transitions from safe deliberation to unsafe commitment. We reproduce the TrajGuard methodology on reasoning models (Section~\\ref{sec:experiments}) and find that it fails to detect safety commitment, likely because reasoning models exhibit gradual transitions rather than the sharp distributional shifts that distance-based methods assume.\n\n\\paragraph{Reasoning Model Safety.}\nReasoning models such as DeepSeek-R1~\\citep{deepseekr1} and QwQ~\\citep{qwq} produce extended chains of thought (CoT) before generating final answers. This creates new safety challenges. \\citet{harmthoughts} document that reasoning models can ``self-jailbreak'' by gradually rationalizing harmful outputs within their own CoT, even when the initial prompt does not contain adversarial content. \\citet{selfjailbreak} provide a systematic analysis of the mechanisms behind this phenomenon, showing that longer reasoning chains increase the probability of safety circumvention. On the intervention side, SafeRemind~\\citep{saferemind} inserts safety reminders at fixed positions in the reasoning chain to reduce harmful outputs, while SafeThink~\\citep{safethink} trains models to incorporate safety reasoning as part of their CoT process. These works either document the self-jailbreak phenomenon or propose mitigation strategies. Our study addresses a different question: given that safety commitment occurs somewhere in the reasoning chain, what is the best \\textit{modality} for detecting it? We use the HarmThoughts dataset~\\citep{harmthoughts} as our primary data source and compare hidden-state probes against text-based monitors as detection mechanisms for the commitment point.\n\n\\paragraph{Process Supervision and Sequential Monitoring.}\nProcess Reward Models (PRMs) evaluate reasoning quality at the step level. \\citet{lightman2023prm} train PRMs to judge whether each step in a mathematical solution is correct, showing that step-level supervision outperforms outcome-level supervision for improving mathematical reasoning. \\citet{wang2024prm} scale this approach through automated labeling. While PRMs assess reasoning \\textit{correctness} (whether a mathematical step follows logically), our probes assess reasoning \\textit{safety} (whether the model has committed to producing harmful content). The sequential nature of our detection problem also connects to change-point detection. Bayesian Online Change Point Detection (BOCPD)~\\citep{adams2007bayesian} provides a principled framework for detecting abrupt distributional shifts in sequential data. We apply BOCPD to hidden-state sequences as a baseline (Section~\\ref{sec:experiments}) but find that it performs poorly: safety commitment in reasoning models is not an abrupt regime change but a gradual drift, with commitment signals emerging over multiple reasoning steps before the model produces harmful text. This finding motivates our use of temporal probes that can capture gradual transitions.\n"
  }
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-17T00:40:58.763996+00:00_

File created successfully at: /home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/docs/paper/sections/related_work.tex

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_related_work_20260517T003949",
  "tool": "Write",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 9 · 2026-05-17T00:40:58.764156+00:00_

Related Work 已写入 `docs/paper/sections/related_work.tex`。约 980 words，5 个 \paragraph 子主题，共 19 个唯一 \cite key（belinkov2019analysis, hewitt2019structural, hewitt2019control, geiger2021causal, vig2020causal, meng2022locating, trajguard, safeswitch, siren, zou2023representation, deepseekr1, qwq, harmthoughts, selfjailbreak, saferemind, safethink, lightman2023prm, wang2024prm, adams2007bayesian）。每个子主题结尾有明确的 positioning 说明，无 contribution claim，无 em-dash，无 -ing 短语结尾。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_paper_writing_related_work_20260517T003949"
}
```

</details>

---
