# paper writing introduction d097

**Instruction Routing in Fine-Tuned Vision-Language-Action Models: A Cross-Architecture Analysis** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 19
- **Recorded user turns:** 0
- **Tool calls:** 9
- **Original source:** `logs/chats/worker_paper_writing_introduction_d097_20260522T052631.jsonl`
- **Structured JSON:** [`ea7a520d5077ca67c5da.json`](../../sessions/ea/ea7a520d5077ca67c5da.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

19 recorded events

### Tool call

_source line 1 · 2026-05-22T05:33:03.436739+00:00_

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
  "session": "worker_paper_writing_introduction_d097_20260522T052631",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/agent-ml-research/skills/global/paper-writing-norms.skill.md"
  }
}
```

</details>

---

### Tool result

_source line 2 · 2026-05-22T05:33:03.437352+00:00_

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
  "session": "worker_paper_writing_introduction_d097_20260522T052631",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-22T05:33:03.437552+00:00_

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
  "session": "worker_paper_writing_introduction_d097_20260522T052631",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/agent-ml-research/skills/global/latex-paper.skill.md"
  }
}
```

</details>

---

### Tool result

_source line 4 · 2026-05-22T05:33:03.437909+00:00_

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
  "session": "worker_paper_writing_introduction_d097_20260522T052631",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-22T05:33:03.438098+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_introduction_d097_20260522T052631",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/introduction.tex"
  }
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-22T05:33:03.438260+00:00_

1	\section{Introduction}
2	\label{sec:introduction}
3	
4	What does fine-tuning change inside a Vision-Language-Action model (VLA)?
5	VLAs fine-tune large language models on robot demonstrations to produce actions from visual observations and language instructions~\cite{brohan2023_rt2,kim2024_openvla}, but the decoder-only causal mask prevents image tokens from attending to instructions~\cite{wang2025seeing,pei2025rethinking}.
6	Instruction information must reach action-generating positions through learned attention patterns, yet how fine-tuning reshapes these patterns remains uncharacterized.
7	
8	Recent behavioral studies reveal that VLAs rely disproportionately on visual input~\cite{grant2026}, with language instructions largely ignored by the action pathway~\cite{haon2025}.
9	These findings suggest internal specialization but do not explain \emph{how} instruction information reaches the action-generating readout token, \emph{what} attention strategy fine-tuning learns compared to language pretraining alone, or \emph{whether} training creates new representational structure or reconfigures inherited geometry.
10	Existing analyses have not combined systematic per-layer probing with factorial trained/pretrained/untrained controls, leaving the representational mechanisms of VLA fine-tuning opaque.
11	
12	We address this gap by decomposing OpenVLA-7B~\cite{kim2024_openvla,karamcheti2024}, a VLA chaining a frozen DinoSigLIP vision backbone~\cite{zhai2023_siglip,oquab2024_dinov2}, an MLP projector, and Llama-2 7B~\cite{touvron2023_llama2}.
13	We extract representations from each of 32 LLM layers at both image-token and readout-token positions, and from external baselines (DINOv2~\cite{oquab2024_dinov2}, CLIP~\cite{radford2021_clip}).
14	We compare three LLM conditions (VLA-trained, pretrained Llama-2 base, and randomly initialized) crossed with instruction presence, and apply four complementary analyses: cross-instruction probes for token-level specialization, L1 attenti
…[truncated 2540 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_introduction_d097_20260522T052631",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-22T05:33:03.438413+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/experiments.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_introduction_d097_20260522T052631",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/experiments.tex"
  }
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-22T05:33:03.438668+00:00_

1	\section{Experiments}
2	\label{sec:experiments}
3	
4	\subsection{Experimental Setup}
5	\label{sec:setup}
6	
7	We analyze three VLA architectures across four LIBERO~\cite{liu2023_libero} task suites (Goal, Spatial, Object, Long-Horizon) in a $3 \times 4$ cross-architecture matrix (Table~\ref{tab:cross_arch_matrix}).
8	The architectures span distinct backbone families: OpenVLA~\cite{kim2024_openvla,karamcheti2024} (Llama-2-7B~\cite{touvron2023_llama2}, 32 layers, 32 MHA heads), TracVLA~\cite{zheng2024tracevla} (Phi-3-mini~\cite{abdin2024phi3}, 32 layers, 32 heads), and NORA~\cite{TODO_nora} (Qwen2.5-VL-3B, 36 layers, GQA with 16 query heads and 2 KV heads).
9	Of the 12 matrix cells, 10 are filled; NORA Object and Long-Horizon lack available checkpoints.
10	Each architecture is compared in trained and untrained conditions, with a critical asymmetry between untrained baselines: OpenVLA's untrained checkpoint is the OXE-pretrained~\cite{padalkar2023_oxe} VLA (already fine-tuned for action prediction on 970K episodes), while TracVLA and NORA untrained checkpoints are pure vision-language models (Phi-3-Vision and Qwen2.5-VL) with no action training.
11	Three analyses are applied to each cell (\S\ref{sec:method}): $R^2$ action probes at all layers, L1 attention head profiling for instruction dominance, and counterfactual instruction perturbation.
12	For OpenVLA LIBERO-Goal, $N = 63{,}228$ observations; other cells are at comparable scale.
13	For trained models that produce action outputs, counterfactual sensitivity is measured via Cohen's $d$ on action MSE.
14	For untrained VLMs (Phi-3-Vision, Qwen2.5-VL) that do not produce actions, sensitivity is measured via cosine distance on hidden representations; these metrics operate on different scales and are not directly comparable (\S\ref{sec:cf_sensitivity}).
15	OpenVLA's OXE-pretrained checkpoint produces actions, permitting same-metric (Cohen's $d$) comparison in that condition.
16	Bonferroni correction details appear in Ap
…[truncated 22247 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_introduction_d097_20260522T052631",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-22T05:33:03.438833+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/method.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_introduction_d097_20260522T052631",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/method.tex"
  }
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-22T05:33:03.439034+00:00_

1	\section{Method}
2	\label{sec:method}
3	
4	We investigate how action-relevant representations are organized across three VLA architectures using complementary probing, attention, and perturbation analyses.
5	
6	%------------------------------------------------------------------
7	\subsection{Architectures and Data}
8	\label{sec:arch_data}
9	
10	We study three VLAs that span distinct backbone families (Table~\ref{tab:arch_overview}).
11	\textbf{OpenVLA}~\cite{kim2024_openvla,karamcheti2024} chains a frozen DinoSigLIP vision backbone~\cite{zhai2023_siglip,oquab2024_dinov2} (DINOv2 ViT-L/14 + SigLIP-SO400M), an MLP projector (2{,}176-D $\to$ 4{,}096-D), and Llama-2-7B~\cite{touvron2023_llama2} (6.74B parameters, 32 layers, 32 multi-head attention [MHA] heads) for autoregressive 7-D action decoding.
12	Its base checkpoint is pretrained on Open X-Embodiment~\cite{padalkar2023_oxe} (OXE; 970K episodes across multiple robot platforms).
13	\textbf{TracVLA}~\cite{zheng2024tracevla} uses Phi-3-mini~\cite{abdin2024phi3} (32 layers, 32 MHA heads) with a SigLIP encoder augmented by spatial trace conditioning, trained on an OXE subset.
14	\textbf{NORA}~\cite{TODO_nora} uses Qwen2.5-VL-3B (36 layers, grouped-query attention [GQA] with 16 query heads and 2 KV heads) with its native vision encoder.
15	
16	Each architecture is evaluated in trained and untrained conditions.
17	A critical asymmetry distinguishes the untrained baselines: OpenVLA's untrained checkpoint is the OXE-pretrained VLA, already fine-tuned for action prediction on 970K episodes, while TracVLA and NORA untrained checkpoints are pure vision-language models (Phi-3-Vision and Qwen2.5-VL) with no action training.
18	OpenVLA trained-vs-untrained comparisons therefore measure a VLA-to-VLA transition; TracVLA and NORA comparisons measure VLM-to-VLA transitions.
19	This asymmetry affects the interpretation of all trained/untrained comparisons throughout the paper.
20	For OpenVLA, two additional conditions support deep-d
…[truncated 6869 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_introduction_d097_20260522T052631",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-22T05:33:03.439187+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/abstract.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_introduction_d097_20260522T052631",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/abstract.tex"
  }
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-22T05:33:03.439320+00:00_

1	Vision-language-action models (VLAs) convert pretrained vision-language backbones into robot controllers through fine-tuning, yet whether the resulting representational changes reflect general training dynamics or architecture-specific artifacts remains unknown.
2	We conduct a systematic cross-architecture analysis of three VLAs built on distinct backbones (Llama-2-7B, Phi-3-mini, Qwen2.5-VL-3B) across four LIBERO task suites, comparing trained and untrained checkpoints with cross-instruction probes, attention profiling, $R^2$ action probes, and counterfactual instruction perturbation.
3	We identify two training effects that generalize across architectures.
4	First, $R^2$ exit collapse, where action-relevant information is selectively discarded at exit layers, consistently emerges when vision-language models are first fine-tuned into VLAs (6/6 cells across two architectures) but does not intensify with further task-specific training of already-pretrained VLAs (1/3 cells), revealing exit collapse as a one-time reorganization at the VLM-to-VLA transition.
5	Second, all trained VLAs exhibit substantial counterfactual sensitivity to instruction perturbation (Cohen's $d \geq 0.45$ across two architectures and eight suite combinations), though metric incomparability between trained (action MSE) and untrained (cosine distance) conditions precludes quantifying the trained--untrained gap as a single amplification factor.
6	In contrast, early-layer instruction-dominant attention patterns trace to base-model priors rather than VLA training; one backbone exhibits saturated instruction attention even before fine-tuning.
7	Together, these findings distinguish training-induced routing effects (exit collapse, counterfactual sensitivity) from inherited base-model priors (early-layer instruction attention), and their consistency across two VLM-to-VLA transitions with dramatically different starting points is compatible with VLA fine-tuning discovering shared functional organization
…[truncated 45 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_introduction_d097_20260522T052631",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-22T05:33:03.439793+00:00_

called Write

<details open><summary>🔧 Tool call — Write</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/introduction.tex",
  "content": "\\section{Introduction}\n\\label{sec:introduction}\n\nVision-language-action models (VLAs) fine-tune pretrained language models on robot demonstrations to produce actions from visual observations and language instructions~\\cite{brohan2023_rt2,kim2024_openvla}.\nIn these decoder-only architectures, image tokens precede instruction tokens in the input sequence, and the causal attention mask prevents image tokens from attending to any token that follows them~\\cite{wang2025seeing,pei2025rethinking}.\nInstruction information can reach action-generating positions only through later attention layers, where the readout token (the final position before action decoding) integrates context from all preceding tokens.\nThe readout is thus the sole multimodal integration point by construction.\nHow fine-tuning creates or reshapes the attention patterns at this position, and whether the resulting routing reflects training dynamics or inherited backbone structure, remains unknown.\n\nBehavioral studies provide indirect evidence that this question matters.\nVLAs exhibit visual dominance, relying disproportionately on image input~\\cite{grant2026}, and language instructions appear largely unused by the action pathway~\\cite{haon2025}.\nThese observations establish that VLAs underweight instructions but do not explain \\emph{how} instruction information reaches action-generating positions, \\emph{what} routing structure training creates versus what it inherits from the pretrained backbone, or \\emph{whether} observed patterns hold across architectures.\nAll existing representational analyses of VLAs target a single architecture.\nNo prior work tests whether instruction routing mechanisms are consistent across backbone families, and none decomposes training-induced effects from inherited base-model priors.\nAbsent cross-architecture evidence, it is impossible to distinguish training dynamics that reflect the causal-decoder structure from architecture-specific artifacts of a particular language model.\n\nWe address this gap with a systematic cross-architecture analysis of three VLAs built on distinct backbones: OpenVLA~\\cite{kim2024_openvla,karamcheti2024} (Llama-2-7B~\\cite{touvron2023_llama2}, 32 layers), TracVLA~\\cite{zheng2024tracevla} (Phi-3-mini~\\cite{abdin2024phi3}, 32 layers), and NORA~\\cite{TODO_nora} (Qwen2.5-VL-3B, 36 layers).\nEach architecture is evaluated across four LIBERO~\\cite{liu2023_libero} task suites (Goal, Spatial, Object, Long-Horizon), forming a $3 \\times 4$ matrix with 10 of 12 cells filled (\\S\\ref{sec:setup}).\nA critical asymmetry structures the trained/untrained comparison: OpenVLA's untrained checkpoint is the OXE-pretrained~\\cite{padalkar2023_oxe} VLA, already fine-tuned on 970K episodes for action prediction, while TracVLA and NORA untrained checkpoints are pure vision-language models (Phi-3-Vision, Qwen2.5-VL) with no action training.\nThe six TracVLA and NORA cells therefore test VLM-to-VLA transitions; the three OpenVLA cells test VLA-to-VLA transitions.\nThis design enables two types of inference: within-architecture trained/untrained contrasts identify what training changes, and cross-architecture comparisons test whether those changes are backbone-specific.\nWe apply five complementary analyses: cross-instruction probes, L1 attention head profiling, $R^2$ action probes, representational similarity analysis (RSA)~\\cite{kriegeskorte2008}, and counterfactual instruction perturbation (\\S\\ref{sec:method}).\nA single-architecture deep dive on OpenVLA (\\S\\ref{sec:openvla_routing}) establishes core phenomena before the cross-architecture comparisons.\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=0.88\\linewidth,height=2in,keepaspectratio]{figures/fig_teaser.pdf}\n\\vspace{-4pt}\n\\caption{\\textbf{VLA fine-tuning reorganizes action-relevant representations in a pattern consistent across two VLM-to-VLA transitions but absent before action training.}\nThree architectures are compared in trained and untrained conditions.\nTraining-induced effects ($R^2$ exit collapse, counterfactual sensitivity) emerge at the VLM-to-VLA transition, while L1 instruction attention reflects inherited base-model priors.}\n\\label{fig:teaser}\n\\end{figure}\n\nThree findings emerge from this cross-architecture comparison (Figure~\\ref{fig:teaser}).\n\\emph{First}, $R^2$ exit collapse, the drop in action-probe $R^2$ from peak layer to exit layer, consistently marks VLM-to-VLA transitions.\nAll six TracVLA and NORA cells show larger trained $\\Delta R^2$ than untrained $\\Delta R^2$: TracVLA trained collapse ranges from $0.138$ to $0.294$ (untrained: $0.009$--$0.048$), and NORA trained collapse reaches $0.691$ on Goal, where exit-layer $R^2$ drops below zero (untrained: $0.044$).\nA one-sided sign test confirms this direction across all six cells ($p = 0.016$).\nIn contrast, only one of three VLA-to-VLA cells (OpenVLA Object) shows the same pattern.\nThe 6/6 versus 1/3 contrast identifies exit collapse as a one-time reorganization that occurs when a vision-language model is first fine-tuned into a VLA (\\S\\ref{sec:r2_collapse}).\n\n\\emph{Second}, all trained VLAs exhibit substantial counterfactual sensitivity to instruction perturbation.\nAcross eight cells where Cohen's $d$ is applicable (OpenVLA and TracVLA, four suites each), every perturbation condition produces $d \\geq 0.45$, with empty-instruction perturbation ranking first in seven of eight cells ($d = 0.94$--$1.52$).\nParaphrased instructions preserve meaning while changing surface tokens, yet they rank last in seven of eight cells; VLAs thus encode instruction content beyond token-level matching.\nA metric constraint limits trained/untrained comparison: untrained VLMs do not produce actions, so their sensitivity is measured via cosine distance on hidden representations rather than Cohen's $d$ on action MSE.\nThese metrics operate on different scales; cross-metric ratios are invalid and we do not report amplification factors (\\S\\ref{sec:cf_sensitivity}).\n\n\\emph{Third}, L1 instruction-dominant attention reflects base-model language pretraining rather than VLA fine-tuning.\nTracVLA's untrained checkpoint (Phi-3-Vision) allocates 32/32 attention heads to instruction dominance across all four suites before any action training; VLA training slightly \\emph{reduces} this count to 27--30/32.\nNORA untrained (Qwen2.5-VL) shows 13--14 of 16 heads instruction-dominant, unchanged by training.\nIf VLA training were the primary driver of L1 instruction routing, untrained VLMs should show low instruction attention that increases after training, as observed in OpenVLA's random-weight condition (0/32 heads).\nThe saturation before training provides direct evidence that L1 patterns are inherited priors (\\S\\ref{sec:l1_priors}).\n\nOur contributions are:\n\\begin{enumerate}\n\\item An empirical cross-architecture representational analysis framework for VLAs, combining factorial trained/untrained controls with token-level probing across a $3 \\times 4$ architecture-suite matrix.\n\\item Identification of $R^2$ exit collapse as a marker of the VLM-to-VLA transition, consistent across two VLM-to-VLA architectures (TracVLA, NORA) with partial confirmation in OpenVLA (2/4 suites).\n\\item A decomposition of VLA instruction routing into training-induced effects (exit collapse, counterfactual sensitivity) and inherited base-model priors (L1 instruction attention), grounded in cross-architecture trained/untrained contrasts.\n\\end{enumerate}\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_introduction_d097_20260522T052631",
  "tool": "Write",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/introduction.tex",
    "content": "\\section{Introduction}\n\\label{sec:introduction}\n\nVision-language-action models (VLAs) fine-tune pretrained language models on robot demonstrations to produce actions from visual observations and language instructions~\\cite{brohan2023_rt2,kim2024_openvla}.\nIn these decoder-only architectures, image tokens precede instruction tokens in the input sequence, and the causal attention mask prevents image tokens from attending to any token that follows them~\\cite{wang2025seeing,pei2025rethinking}.\nInstruction information can reach action-generating positions only through later attention layers, where the readout token (the final position before action decoding) integrates context from all preceding tokens.\nThe readout is thus the sole multimodal integration point by construction.\nHow fine-tuning creates or reshapes the attention patterns at this position, and whether the resulting routing reflects training dynamics or inherited backbone structure, remains unknown.\n\nBehavioral studies provide indirect evidence that this question matters.\nVLAs exhibit visual dominance, relying disproportionately on image input~\\cite{grant2026}, and language instructions appear largely unused by the action pathway~\\cite{haon2025}.\nThese observations establish that VLAs underweight instructions but do not explain \\emph{how} instruction information reaches action-generating positions, \\emph{what} routing structure training creates versus what it inherits from the pretrained backbone, or \\emph{whether} observed patterns hold across architectures.\nAll existing representational analyses of VLAs target a single architecture.\nNo prior work tests whether instruction routing mechanisms are consistent across backbone families, and none decomposes training-induced effects from inherited base-model priors.\nAbsent cross-architecture evidence, it is impossible to distinguish training dynamics that reflect the causal-decoder structure from architecture-specific artifacts of a particular language model.\n\nWe address this gap with a systematic cross-architecture analysis of three VLAs built on distinct backbones: OpenVLA~\\cite{kim2024_openvla,karamcheti2024} (Llama-2-7B~\\cite{touvron2023_llama2}, 32 layers), TracVLA~\\cite{zheng2024tracevla} (Phi-3-mini~\\cite{abdin2024phi3}, 32 layers), and NORA~\\cite{TODO_nora} (Qwen2.5-VL-3B, 36 layers).\nEach architecture is evaluated across four LIBERO~\\cite{liu2023_libero} task suites (Goal, Spatial, Object, Long-Horizon), forming a $3 \\times 4$ matrix with 10 of 12 cells filled (\\S\\ref{sec:setup}).\nA critical asymmetry structures the trained/untrained comparison: OpenVLA's untrained checkpoint is the OXE-pretrained~\\cite{padalkar2023_oxe} VLA, already fine-tuned on 970K episodes for action prediction, while TracVLA and NORA untrained checkpoints are pure vision-language models (Phi-3-Vision, Qwen2.5-VL) with no action training.\nThe six TracVLA and NORA cells therefore test VLM-to-VLA transitions; the three OpenVLA cells test VLA-to-VLA transitions.\nThis design enables two types of inference: within-architecture trained/untrained contrasts identify what training changes, and cross-architecture comparisons test whether those changes are backbone-specific.\nWe apply five complementary analyses: cross-instruction probes, L1 attention head profiling, $R^2$ action probes, representational similarity analysis (RSA)~\\cite{kriegeskorte2008}, and counterfactual instruction perturbation (\\S\\ref{sec:method}).\nA single-architecture deep dive on OpenVLA (\\S\\ref{sec:openvla_routing}) establishes core phenomena before the cross-architecture comparisons.\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=0.88\\linewidth,height=2in,keepaspectratio]{figures/fig_teaser.pdf}\n\\vspace{-4pt}\n\\caption{\\textbf{VLA fine-tuning reorganizes action-relevant representations in a pattern consistent across two VLM-to-VLA transitions but absent before action training.}\nThree architectures are compared in trained and untrained conditions.\nTraining-induced effects ($R^2$ exit collapse, counterfactual sensitivity) emerge at the VLM-to-VLA transition, while L1 instruction attention reflects inherited base-model priors.}\n\\label{fig:teaser}\n\\end{figure}\n\nThree findings emerge from this cross-architecture comparison (Figure~\\ref{fig:teaser}).\n\\emph{First}, $R^2$ exit collapse, the drop in action-probe $R^2$ from peak layer to exit layer, consistently marks VLM-to-VLA transitions.\nAll six TracVLA and NORA cells show larger trained $\\Delta R^2$ than untrained $\\Delta R^2$: TracVLA trained collapse ranges from $0.138$ to $0.294$ (untrained: $0.009$--$0.048$), and NORA trained collapse reaches $0.691$ on Goal, where exit-layer $R^2$ drops below zero (untrained: $0.044$).\nA one-sided sign test confirms this direction across all six cells ($p = 0.016$).\nIn contrast, only one of three VLA-to-VLA cells (OpenVLA Object) shows the same pattern.\nThe 6/6 versus 1/3 contrast identifies exit collapse as a one-time reorganization that occurs when a vision-language model is first fine-tuned into a VLA (\\S\\ref{sec:r2_collapse}).\n\n\\emph{Second}, all trained VLAs exhibit substantial counterfactual sensitivity to instruction perturbation.\nAcross eight cells where Cohen's $d$ is applicable (OpenVLA and TracVLA, four suites each), every perturbation condition produces $d \\geq 0.45$, with empty-instruction perturbation ranking first in seven of eight cells ($d = 0.94$--$1.52$).\nParaphrased instructions preserve meaning while changing surface tokens, yet they rank last in seven of eight cells; VLAs thus encode instruction content beyond token-level matching.\nA metric constraint limits trained/untrained comparison: untrained VLMs do not produce actions, so their sensitivity is measured via cosine distance on hidden representations rather than Cohen's $d$ on action MSE.\nThese metrics operate on different scales; cross-metric ratios are invalid and we do not report amplification factors (\\S\\ref{sec:cf_sensitivity}).\n\n\\emph{Third}, L1 instruction-dominant attention reflects base-model language pretraining rather than VLA fine-tuning.\nTracVLA's untrained checkpoint (Phi-3-Vision) allocates 32/32 attention heads to instruction dominance across all four suites before any action training; VLA training slightly \\emph{reduces} this count to 27--30/32.\nNORA untrained (Qwen2.5-VL) shows 13--14 of 16 heads instruction-dominant, unchanged by training.\nIf VLA training were the primary driver of L1 instruction routing, untrained VLMs should show low instruction attention that increases after training, as observed in OpenVLA's random-weight condition (0/32 heads).\nThe saturation before training provides direct evidence that L1 patterns are inherited priors (\\S\\ref{sec:l1_priors}).\n\nOur contributions are:\n\\begin{enumerate}\n\\item An empirical cross-architecture representational analysis framework for VLAs, combining factorial trained/untrained controls with token-level probing across a $3 \\times 4$ architecture-suite matrix.\n\\item Identification of $R^2$ exit collapse as a marker of the VLM-to-VLA transition, consistent across two VLM-to-VLA architectures (TracVLA, NORA) with partial confirmation in OpenVLA (2/4 suites).\n\\item A decomposition of VLA instruction routing into training-induced effects (exit collapse, counterfactual sensitivity) and inherited base-model priors (L1 instruction attention), grounded in cross-architecture trained/untrained contrasts.\n\\end{enumerate}\n"
  }
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-22T05:33:03.440135+00:00_

The file /home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/introduction.tex has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_introduction_d097_20260522T052631",
  "tool": "Write",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-22T05:33:03.440360+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_introduction_d097_20260522T052631",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/introduction.tex"
  }
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-22T05:33:03.440541+00:00_

1	\section{Introduction}
2	\label{sec:introduction}
3	
4	Vision-language-action models (VLAs) fine-tune pretrained language models on robot demonstrations to produce actions from visual observations and language instructions~\cite{brohan2023_rt2,kim2024_openvla}.
5	In these decoder-only architectures, image tokens precede instruction tokens in the input sequence, and the causal attention mask prevents image tokens from attending to any token that follows them~\cite{wang2025seeing,pei2025rethinking}.
6	Instruction information can reach action-generating positions only through later attention layers, where the readout token (the final position before action decoding) integrates context from all preceding tokens.
7	The readout is thus the sole multimodal integration point by construction.
8	How fine-tuning creates or reshapes the attention patterns at this position, and whether the resulting routing reflects training dynamics or inherited backbone structure, remains unknown.
9	
10	Behavioral studies provide indirect evidence that this question matters.
11	VLAs exhibit visual dominance, relying disproportionately on image input~\cite{grant2026}, and language instructions appear largely unused by the action pathway~\cite{haon2025}.
12	These observations establish that VLAs underweight instructions but do not explain \emph{how} instruction information reaches action-generating positions, \emph{what} routing structure training creates versus what it inherits from the pretrained backbone, or \emph{whether} observed patterns hold across architectures.
13	All existing representational analyses of VLAs target a single architecture.
14	No prior work tests whether instruction routing mechanisms are consistent across backbone families, and none decomposes training-induced effects from inherited base-model priors.
15	Absent cross-architecture evidence, it is impossible to distinguish training dynamics that reflect the causal-decoder structure from architecture-specific artifacts o
…[truncated 5597 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_introduction_d097_20260522T052631",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-22T05:33:03.440701+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper && grep -n \"—\" introduction.tex; grep -n \" – \" introduction.tex; grep -cn \"architecture-independent\\|state-of-the-art\\|consistently outperforms\\|delve\\|leverage\\|notably\\|crucial\" introduction.tex; grep -n \"sec:learned_routing\\|sec:nonmonotonic\\|sec:token_specialization\" introduction.tex; echo \"--- checks done ---\"",
  "description": "Check for style violations in introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_introduction_d097_20260522T052631",
  "tool": "Bash",
  "tool_args": {
    "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper && grep -n \"—\" introduction.tex; grep -n \" – \" introduction.tex; grep -cn \"architecture-independent\\|state-of-the-art\\|consistently outperforms\\|delve\\|leverage\\|notably\\|crucial\" introduction.tex; grep -n \"sec:learned_routing\\|sec:nonmonotonic\\|sec:token_specialization\" introduction.tex; echo \"--- checks done ---\"",
    "description": "Check for style violations in introduction.tex"
  }
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-22T05:33:03.440880+00:00_

0
--- checks done ---

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_introduction_d097_20260522T052631",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 19 · 2026-05-22T05:33:03.441100+00:00_

Introduction 重写完成。文件已写入 `introduction.tex`。

验证通过：无 em-dash、无禁用词、无旧 section labels、无 -ing 短语结尾。

结构：Hook+Gap（2段） → 方法概述（1段） → Teaser figure → 三个 Findings（R² exit collapse / CF sensitivity / L1 inherited priors） → 三条 Contributions。所有 section 引用使用新 labels（`sec:r2_collapse`, `sec:cf_sensitivity`, `sec:l1_priors`, `sec:setup`, `sec:method`, `sec:openvla_routing`）。D097 约束全部遵守：无 "architecture-independent"、无 CF amplification ratio、无无统计支持的 "significantly"。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_paper_writing_introduction_d097_20260522T052631"
}
```

</details>

---
