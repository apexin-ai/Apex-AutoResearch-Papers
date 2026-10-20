# paper writing conclusion abstract limitations

**Exposure Bias Collapses Auxiliary Attention Losses in Multi-Turn Dialogue** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 19
- **Recorded user turns:** 0
- **Tool calls:** 9
- **Original source:** `logs/chats/worker_paper_writing_conclusion_abstract_limitations_20260519T232714.jsonl`
- **Structured JSON:** [`ace14a7366d159578682.json`](../../sessions/ac/ace14a7366d159578682.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

19 recorded events

### Tool call

_source line 1 · 2026-05-19T23:28:34.949541+00:00_

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
  "session": "worker_paper_writing_conclusion_abstract_limitations_20260519T232714",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/agent-ml-research/skills/global/paper-writing-norms.skill.md"
  }
}
```

</details>

---

### Tool result

_source line 2 · 2026-05-19T23:28:34.950123+00:00_

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
  "session": "worker_paper_writing_conclusion_abstract_limitations_20260519T232714",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-19T23:28:34.950323+00:00_

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
  "session": "worker_paper_writing_conclusion_abstract_limitations_20260519T232714",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/agent-ml-research/skills/global/latex-paper.skill.md"
  }
}
```

</details>

---

### Tool result

_source line 4 · 2026-05-19T23:28:34.950729+00:00_

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
  "session": "worker_paper_writing_conclusion_abstract_limitations_20260519T232714",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-19T23:28:34.950897+00:00_

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
  "session": "worker_paper_writing_conclusion_abstract_limitations_20260519T232714",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/introduction.tex"
  }
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-19T23:28:34.951064+00:00_

1	\section{Introduction}\label{sec:introduction}
2	
3	Multi-turn dialogue is the dominant mode of interaction with large language models (LLMs), and system prompts that specify task goals form the foundation of instruction following. As conversations grow longer, however, models progressively lose track of these goal specifications. \citet{dongre2026attention} quantified this degradation across 12 models: the Goal Attention Ratio (GAR), which measures how much attention the model allocates to goal tokens in the system prompt, declines by an average of 70.8\% between early and mid-conversation turns. We replicate this finding on Qwen-2.5-7B-Instruct, where GAR drops from 0.0418 at turn~1 to 0.0122 at mid-conversation, consistent with the cross-model pattern. This attention decay represents a systematic failure of multi-turn models to maintain task coherence, and it grows worse with each additional turn.
4	
5	A striking aspect of this degradation is what it does \emph{not} affect. \citet{dongre2026attention} showed that goal-relevant information persists in the residual stream throughout the conversation: linear discriminant analysis probes recover goal content with AUC\,=\,0.98 even at late turns where attention to goal tokens has collapsed. The information is present in the hidden states, but the attention mechanism fails to route it toward the output computation. This dissociation between information availability and information utilization suggests a natural intervention: if the residual stream already carries goal information, a learnable gate on the residual pathway could amplify or attenuate layer contributions to recover goal attention. This reasoning motivates ThreadGate, which applies a per-layer sigmoid gate $g_l$ to each residual update: $x_{l+1} = x_l + g_l \cdot f_l(x_l)$, following the ReZero residual scaling principle \citep{bachlechner2021rezero}.
6	
7	\begin{figure*}[t]
8	  \centering
9	  \includegraphics[width=\textwidth]{fig1_overview.pdf}
10	  \ca
…[truncated 4284 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_conclusion_abstract_limitations_20260519T232714",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-19T23:28:34.951217+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/experiments.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_conclusion_abstract_limitations_20260519T232714",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/experiments.tex"
  }
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-19T23:28:34.951378+00:00_

1	\section{Experiments}
2	\label{sec:experiments}
3	
4	\subsection{Setup}
5	
6	We fine-tune Qwen-2.5-7B-Instruct on 8K multi-turn conversations from the UltraChat training split, a dataset of naturalistic dialogues across diverse topics. LoRA adapters (rank 8) are applied to all linear layers. The combined loss $\mathcal{L} = \mathcal{L}_\text{NTP} + \lambda_\text{GAR}\mathcal{L}_\text{GAR} + \lambda_\text{div}\mathcal{L}_\text{div}$ uses $\lambda_\text{GAR} = \lambda_\text{div} = 1.0$ with MSE target $\tau = 0.5$ (\S\ref{sec:loss}). We train for 3 epochs with AdamW (lr $= 2 \times 10^{-4}$, batch size 1, gradient accumulation 8, seed 42); each variant requires approximately 6 hours on a single NVIDIA RTX PRO 6000 Blackwell Server Edition GPU (102\,GB). Full hyperparameters are provided in Appendix~A.
7	
8	To isolate the contribution of gating, we evaluate four configurations: (1)~\textbf{ThreadGate}: LoRA + per-layer learned gates + NTP + GAR loss; (2)~\textbf{Uniform Gate}: LoRA + a single shared gate across all layers + NTP + GAR loss; (3)~\textbf{LoRA-only}: LoRA + NTP + GAR loss, with gates fixed at 1.0 (no learned gating mechanism); (4)~\textbf{Base}: the pretrained model without any fine-tuning. Each configuration is evaluated under two teacher-forced protocols. \emph{IID evaluation} computes metrics on UltraChat text from the same distribution as training. \emph{Held-out evaluation} uses 50 non-overlapping conversations to test within-distribution generalization. We report three metrics: GAR-ours (attention to goal tokens at the last token of each assistant turn, as defined in \S\ref{sec:background}), GAR-Dongre \citep{dongre2026attention} (attention to goal tokens averaged across all response tokens, all layers, and all heads), and perplexity (PPL).
9	
10	\subsection{Main Results}
11	
12	Table~\ref{tab:four-way} presents the four-way ablation. The central finding is that all three fine-tuned variants converge to nearly identical performance across both eval
…[truncated 4184 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_conclusion_abstract_limitations_20260519T232714",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-19T23:28:34.951555+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/analysis.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_conclusion_abstract_limitations_20260519T232714",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/analysis.tex"
  }
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-19T23:28:34.951783+00:00_

1	\section{Analysis}\label{sec:analysis}
2	
3	The four-way ablation in \S\ref{sec:experiments} established that gating produces no measurable benefit over LoRA-only fine-tuning. This section investigates why. We first characterize the gradient dynamics between the two training objectives (\S\ref{subsec:gradient-conflict}), then show that the learned gates exhibit behavior opposite to the design intent (\S\ref{subsec:gate-conditioning}). A targeted causal experiment rules out gradient direction conflict as the explanation (\S\ref{subsec:pcgrad}), and a distribution shift analysis identifies the actual failure mode (\S\ref{subsec:dist-shift}).
4	
5	\subsection{Gradient Conflict Observation}\label{subsec:gradient-conflict}
6	
7	To understand how the two loss terms interact during training, we measure the cosine similarity between $\nabla_\theta \mathcal{L}_\text{NTP}$ and $\nabla_\theta \mathcal{L}_\text{GAR}$ at each transformer layer across three training epochs. Table~\ref{tab:grad-conflict} summarizes the results.
8	
9	\begin{table}[t]
10	\centering
11	\small
12	\caption{Gradient interaction between $\mathcal{L}_\text{NTP}$ and $\mathcal{L}_\text{GAR}$ across training epochs. \textit{cos\_sim}: mean cosine similarity across layers. \textit{neg\%}: percentage of layers with negative cosine similarity. \textit{mag\_ratio}: ratio of NTP to GAR gradient magnitudes.}
13	\label{tab:grad-conflict}
14	\begin{tabular}{lccc}
15	\toprule
16	\textbf{Epoch} & \textbf{cos\_sim} & \textbf{neg\%} & \textbf{mag\_ratio} \\
17	\midrule
18	0 & $-$0.089 & 78.6 & 7.5$\times$ \\
19	1 & $-$0.054 & 71.4 & 13.7$\times$ \\
20	2 & $-$0.042 & 67.9 & 14.7$\times$ \\
21	\bottomrule
22	\end{tabular}
23	\end{table}
24	
25	Two patterns are apparent. First, the NTP and GAR gradients point in opposing directions across 68--79\% of layers throughout training. The mean cosine similarity is negative at every epoch, though it attenuates slightly from $-$0.089 to $-$0.042 as training progresses. Second, t
…[truncated 7826 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_conclusion_abstract_limitations_20260519T232714",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-19T23:28:34.951955+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/discussion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_conclusion_abstract_limitations_20260519T232714",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/discussion.tex"
  }
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-19T23:28:34.952098+00:00_

1	\section{Discussion}\label{sec:discussion}
2	
3	The failure of ThreadGate traces to a fundamental incompatibility between teacher-forcing and auxiliary attention losses, not to the gating architecture itself. Under teacher-forcing, $\mathcal{L}_\text{GAR}$ optimizes attention patterns conditioned on ground-truth prefixes that never appear at inference time. The gate parameters, subject to NTP gradient pressure that grows from 7.5$\times$ to 14.7$\times$ the GAR gradient magnitude (\S\ref{subsec:gradient-conflict}), converge toward 1.0 and become passive. The resulting 2--7\% residual attenuation cannot compensate for the distributional mismatch between teacher-forced and autoregressive contexts, as the 30$\times$ GAR gap confirms (\S\ref{subsec:dist-shift}). Stronger gating (lower initial values, higher $\lambda_\text{GAR}$) would degrade NTP performance, while weaker gating is already ineffective. This dilemma is structural: any lightweight intervention trained jointly with NTP under teacher-forcing faces the same pressure toward passivity.
4	
5	Four directions follow from the experimental evidence. First, \textbf{inference-time attention intervention} sidesteps the training generalization problem entirely by rescaling or pruning attention heads at decoding time, operating on the actual autoregressive distribution rather than a teacher-forced proxy. Second, a \textbf{decoupled goal-processing pathway}, analogous to adapter modules but dedicated to goal tokens, could maintain goal information through a channel that NTP gradients do not dominate. Third, \textbf{GAR-aware decoding} would incorporate goal attention into the sampling or reranking stage rather than the training loss, avoiding exposure bias by construction. Fourth, \textbf{exposure bias mitigation for auxiliary losses} remains a viable direction: scheduled sampling \citep{bengio2015scheduled} or Professor Forcing \citep{lamb2016professor} applied specifically to $\mathcal{L}_\text{GAR}$ could reduce the
…[truncated 1639 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_conclusion_abstract_limitations_20260519T232714",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-19T23:28:34.952316+00:00_

called Write

<details open><summary>🔧 Tool call — Write</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/conclusion.tex",
  "content": "\\section{Conclusion}\\label{sec:conclusion}\n\nWe investigated whether lightweight residual gating can recover goal attention in multi-turn dialogue. ThreadGate applies per-layer sigmoid gates to the residual stream, trained jointly with an auxiliary Goal Attention Ratio (GAR) loss that targets attention to system prompt goal tokens. Training succeeds: teacher-forced GAR reaches 0.49 across all fine-tuned variants. The failure emerges at inference time. Under autoregressive generation, GAR drops to 0.016 for ThreadGate, a 30$\\times$ gap that the gating mechanism cannot bridge. A four-way ablation (ThreadGate, Uniform Gate, LoRA-only, Base) confirms that gating contributes zero measurable benefit, with GAR-ours varying by only 0.75 percentage points across fine-tuned variants on held-out data. A PCGrad causal exclusion experiment rules out gradient direction conflict between the NTP and GAR objectives as the cause: eliminating direction conflict does not rescue GAR convergence. The root cause is exposure bias. Attention patterns optimized under teacher-forced prefixes do not transfer to model-generated text, and the primary NTP objective's self-recovery from exposure bias does not extend to auxiliary attention losses. These results indicate that auxiliary attention losses face a fundamental generalization barrier under teacher-forcing. Future work should explore inference-time attention intervention or exposure bias mitigation strategies that operate on the autoregressive distribution directly.\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_conclusion_abstract_limitations_20260519T232714",
  "tool": "Write",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/conclusion.tex",
    "content": "\\section{Conclusion}\\label{sec:conclusion}\n\nWe investigated whether lightweight residual gating can recover goal attention in multi-turn dialogue. ThreadGate applies per-layer sigmoid gates to the residual stream, trained jointly with an auxiliary Goal Attention Ratio (GAR) loss that targets attention to system prompt goal tokens. Training succeeds: teacher-forced GAR reaches 0.49 across all fine-tuned variants. The failure emerges at inference time. Under autoregressive generation, GAR drops to 0.016 for ThreadGate, a 30$\\times$ gap that the gating mechanism cannot bridge. A four-way ablation (ThreadGate, Uniform Gate, LoRA-only, Base) confirms that gating contributes zero measurable benefit, with GAR-ours varying by only 0.75 percentage points across fine-tuned variants on held-out data. A PCGrad causal exclusion experiment rules out gradient direction conflict between the NTP and GAR objectives as the cause: eliminating direction conflict does not rescue GAR convergence. The root cause is exposure bias. Attention patterns optimized under teacher-forced prefixes do not transfer to model-generated text, and the primary NTP objective's self-recovery from exposure bias does not extend to auxiliary attention losses. These results indicate that auxiliary attention losses face a fundamental generalization barrier under teacher-forcing. Future work should explore inference-time attention intervention or exposure bias mitigation strategies that operate on the autoregressive distribution directly.\n"
  }
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-19T23:28:34.952485+00:00_

File created successfully at: /home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/conclusion.tex

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_conclusion_abstract_limitations_20260519T232714",
  "tool": "Write",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-19T23:28:34.952614+00:00_

called Write

<details open><summary>🔧 Tool call — Write</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/abstract.tex",
  "content": "\\begin{abstract}\nMulti-turn dialogue with Large Language Models (LLMs) suffers from progressive attention decay toward system prompt goal tokens. The Goal Attention Ratio (GAR) declines by 70.8\\% between early and mid-conversation turns, yet linear probes recover goal content from the residual stream with AUC\\,=\\,0.98, indicating that goal information persists but the attention mechanism fails to route it. We introduce ThreadGate, a per-layer sigmoid gate on the residual stream ($x_{l+1} = x_l + g_l \\cdot f_l(x_l)$), trained jointly with next-token prediction (NTP) and an auxiliary GAR loss. A four-way ablation (ThreadGate, Uniform Gate, LoRA-only, Base) on Qwen-2.5-7B-Instruct reveals that training succeeds (teacher-forced GAR\\,=\\,0.49) but generalization fails: autoregressive GAR drops to 0.016, a 30$\\times$ gap. Gating contributes zero measurable benefit, with only 0.75 percentage points separating all fine-tuned variants on held-out data. A PCGrad experiment rules out gradient direction conflict as the cause. The failure traces to exposure bias: attention patterns optimized under teacher-forced prefixes do not transfer to model-generated text, and the NTP objective's token-level self-recovery does not extend to auxiliary attention losses. These findings provide the first empirical characterization of how exposure bias selectively destroys auxiliary objective generalization while leaving the primary objective intact.\n\\end{abstract}\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_conclusion_abstract_limitations_20260519T232714",
  "tool": "Write",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/abstract.tex",
    "content": "\\begin{abstract}\nMulti-turn dialogue with Large Language Models (LLMs) suffers from progressive attention decay toward system prompt goal tokens. The Goal Attention Ratio (GAR) declines by 70.8\\% between early and mid-conversation turns, yet linear probes recover goal content from the residual stream with AUC\\,=\\,0.98, indicating that goal information persists but the attention mechanism fails to route it. We introduce ThreadGate, a per-layer sigmoid gate on the residual stream ($x_{l+1} = x_l + g_l \\cdot f_l(x_l)$), trained jointly with next-token prediction (NTP) and an auxiliary GAR loss. A four-way ablation (ThreadGate, Uniform Gate, LoRA-only, Base) on Qwen-2.5-7B-Instruct reveals that training succeeds (teacher-forced GAR\\,=\\,0.49) but generalization fails: autoregressive GAR drops to 0.016, a 30$\\times$ gap. Gating contributes zero measurable benefit, with only 0.75 percentage points separating all fine-tuned variants on held-out data. A PCGrad experiment rules out gradient direction conflict as the cause. The failure traces to exposure bias: attention patterns optimized under teacher-forced prefixes do not transfer to model-generated text, and the NTP objective's token-level self-recovery does not extend to auxiliary attention losses. These findings provide the first empirical characterization of how exposure bias selectively destroys auxiliary objective generalization while leaving the primary objective intact.\n\\end{abstract}\n"
  }
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-19T23:28:34.952754+00:00_

File created successfully at: /home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/abstract.tex

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_conclusion_abstract_limitations_20260519T232714",
  "tool": "Write",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-19T23:28:34.952876+00:00_

called Write

<details open><summary>🔧 Tool call — Write</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/limitations.tex",
  "content": "\\section{Limitations}\\label{sec:limitations}\n\nOur experiments use a single random seed (seed\\,=\\,42). While the four-way convergence across ThreadGate, Uniform Gate, and LoRA-only provides indirect evidence of robustness (three independent configurations reaching indistinguishable performance is unlikely to result from seed-specific artifacts), multi-seed validation would strengthen this conclusion.\n\nWe test only one type of auxiliary attention loss (GAR with MSE target $\\tau = 0.5$). Other attention steering objectives, such as head-specific or layer-specific attention losses, may exhibit different sensitivity to exposure bias. Our negative result applies to the GAR family; it does not rule out all auxiliary attention interventions.\n\nTraining uses 8K conversations from UltraChat. Larger-scale training could alter gate dynamics, particularly if the model encounters sufficient distributional diversity to reduce the training-inference mismatch.\n\nCross-model validation on Llama-3.1-8B-Instruct is in progress (\\S\\ref{sec:cross-model}). Until those results are available, our conclusions rest on a single model family (Qwen-2.5-7B-Instruct).\n\nThe PCGrad causal exclusion addresses gradient direction conflict only. Magnitude imbalance (GradNorm; \\citealp{chen2018gradnorm}) and Nash equilibrium approaches (Nash-MTL; \\citealp{navon2022nash}) remain untested and could reveal additional failure modes or interaction effects.\n\nAll three fine-tuned variants share the same GAR auxiliary loss. This design isolates the gating mechanism but does not test whether gating could be effective without an auxiliary attention loss or under a different training objective.\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_conclusion_abstract_limitations_20260519T232714",
  "tool": "Write",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/limitations.tex",
    "content": "\\section{Limitations}\\label{sec:limitations}\n\nOur experiments use a single random seed (seed\\,=\\,42). While the four-way convergence across ThreadGate, Uniform Gate, and LoRA-only provides indirect evidence of robustness (three independent configurations reaching indistinguishable performance is unlikely to result from seed-specific artifacts), multi-seed validation would strengthen this conclusion.\n\nWe test only one type of auxiliary attention loss (GAR with MSE target $\\tau = 0.5$). Other attention steering objectives, such as head-specific or layer-specific attention losses, may exhibit different sensitivity to exposure bias. Our negative result applies to the GAR family; it does not rule out all auxiliary attention interventions.\n\nTraining uses 8K conversations from UltraChat. Larger-scale training could alter gate dynamics, particularly if the model encounters sufficient distributional diversity to reduce the training-inference mismatch.\n\nCross-model validation on Llama-3.1-8B-Instruct is in progress (\\S\\ref{sec:cross-model}). Until those results are available, our conclusions rest on a single model family (Qwen-2.5-7B-Instruct).\n\nThe PCGrad causal exclusion addresses gradient direction conflict only. Magnitude imbalance (GradNorm; \\citealp{chen2018gradnorm}) and Nash equilibrium approaches (Nash-MTL; \\citealp{navon2022nash}) remain untested and could reveal additional failure modes or interaction effects.\n\nAll three fine-tuned variants share the same GAR auxiliary loss. This design isolates the gating mechanism but does not test whether gating could be effective without an auxiliary attention loss or under a different training objective.\n"
  }
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-19T23:28:34.953007+00:00_

File created successfully at: /home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/limitations.tex

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_conclusion_abstract_limitations_20260519T232714",
  "tool": "Write",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 19 · 2026-05-19T23:28:34.953162+00:00_

三个文件已写入。数字与 Introduction/Experiments 一致（30× gap, GAR 0.49 vs 0.016, 0.75pp spread, 70.8% decline, probe AUC=0.98）。Abstract 内 LLM/GAR/NTP 均已定义。六项 Limitations 全部覆盖。无破折号、无 AI 风格用词、无 -ing 短语结尾。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_paper_writing_conclusion_abstract_limitations_20260519T232714"
}
```

</details>

---
