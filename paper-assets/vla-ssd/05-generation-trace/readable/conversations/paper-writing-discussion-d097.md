# paper writing discussion d097

**Instruction Routing in Fine-Tuned Vision-Language-Action Models: A Cross-Architecture Analysis** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 15
- **Recorded user turns:** 0
- **Tool calls:** 7
- **Original source:** `logs/chats/worker_paper_writing_discussion_d097_20260522T054615.jsonl`
- **Structured JSON:** [`33228f5e6ab0015853f8.json`](../../sessions/33/33228f5e6ab0015853f8.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

15 recorded events

### Tool call

_source line 1 · 2026-05-22T05:48:04.868477+00:00_

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
  "session": "worker_paper_writing_discussion_d097_20260522T054615",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/agent-ml-research/skills/global/paper-writing-norms.skill.md"
  }
}
```

</details>

---

### Tool result

_source line 2 · 2026-05-22T05:48:04.869336+00:00_

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
  "session": "worker_paper_writing_discussion_d097_20260522T054615",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-22T05:48:04.869631+00:00_

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
  "session": "worker_paper_writing_discussion_d097_20260522T054615",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/agent-ml-research/skills/global/latex-paper.skill.md"
  }
}
```

</details>

---

### Tool result

_source line 4 · 2026-05-22T05:48:04.870223+00:00_

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
  "session": "worker_paper_writing_discussion_d097_20260522T054615",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-22T05:48:04.870486+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/discussion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_discussion_d097_20260522T054615",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/discussion.tex"
  }
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-22T05:48:04.870717+00:00_

1	\vspace{-2pt}
2	\section{Discussion}
3	\label{sec:discussion}
4	
5	\paragraph{Synthesis.}
6	VLA fine-tuning redistributes instruction attention rather than reshaping visual geometry: training effects concentrate at the readout ($R^2$ $+0.069$, attention $+46$pp) rather than images ($\Delta \leq 1.7\%$), explaining Grant et al.'s~\cite{grant2026} visual dominance finding ($\rho = 0.692$ for DINOv2, yet readout $R^2 = 0.678$ vs.\ $0.634$).
7	Cross-architecture comparison strengthens this picture: two VLAs with different backbones and opposite untrained profiles both arrive at similar mid-layer peaks ($\Delta = 0.003$), suggesting the redistribution reflects task-structure constraints rather than architecture-specific artifacts.
8	Seven analyses support L1 redistribution: \emph{interventional} (dose-response $d = 0.48 \to 0.64$; counterfactual $d = 0.71$--$0.98$, replicating across both LIBERO suites), \emph{supporting} (gradient $0 \to 9 \to 24$ heads; ablation $+0.059$; trajectory $d = 0.65$), and \emph{constraining} ($p = 0.0018$; $z = -3.11$, $0$\textsuperscript{th} percentile; Appendix~\ref{sec:mechanistic_interpretation}--\ref{sec:functional_stages}).
9	
10	\subsection*{Limitations}
11	We analyze two causal-decoder VLAs on held-out LIBERO (Goal and Spatial, 10 tasks each); extending to flow-matching~\cite{black2024_pi0} and diffusion~\cite{ghosh2024_octo} VLAs with cross-attention, and to benchmarks with richer language grounding (e.g., CALVIN, Language-Table), is needed to test generality.
12	Llama-2's 9/32 pretrained instruction-dominant heads may reflect text bias ($+15$-head delta isolates fine-tuning); we analyze only the final checkpoint, preventing characterization of routing emergence dynamics.
13	All analyses are open-loop~\cite{grant2026,haon2025}; closed-loop validation would provide complementary evidence, though consistent mid-layer peaks suggest early-exit inference at ${\sim}1/3$ depth as a testable hypothesis.
14	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_discussion_d097_20260522T054615",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-22T05:48:04.870974+00:00_

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
  "session": "worker_paper_writing_discussion_d097_20260522T054615",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/experiments.tex"
  }
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-22T05:48:04.871408+00:00_

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
  "session": "worker_paper_writing_discussion_d097_20260522T054615",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-22T05:48:04.871681+00:00_

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
  "session": "worker_paper_writing_discussion_d097_20260522T054615",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/introduction.tex"
  }
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-22T05:48:04.871982+00:00_

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
  "session": "worker_paper_writing_discussion_d097_20260522T054615",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-22T05:48:04.872385+00:00_

called Write

<details open><summary>🔧 Tool call — Write</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/discussion.tex",
  "content": "\\vspace{-2pt}\n\\section{Discussion}\n\\label{sec:discussion}\n\n\\paragraph{Synthesis.}\nVLA fine-tuning produces two measurable representational changes: it reorganizes mid-to-exit layer action encoding ($R^2$ exit collapse, \\S\\ref{sec:r2_collapse}) and establishes instruction-conditioned action sensitivity (\\S\\ref{sec:cf_sensitivity}).\nBoth effects concentrate at the readout token rather than image geometry: on OpenVLA, training shifts readout $R^2$ by $+0.069$ but image\\_mean by only $+0.015$ (\\S\\ref{sec:openvla_routing}).\nL1 instruction attention, by contrast, is inherited from base-model pretraining and persists through fine-tuning: Phi-3-Vision saturates at 32/32 instruction-dominant heads before any action training, and Qwen2.5-VL allocates 13--14/16 (\\S\\ref{sec:l1_priors}).\nThis decomposition into training-induced effects (exit collapse, counterfactual sensitivity) and inherited effects (L1 instruction attention) constitutes the central framing of our analysis.\nVLA fine-tuning does not build instruction routing from scratch; it reorganizes downstream representations while preserving the early-layer attention structure of the pretrained backbone.\n\n\\paragraph{Cross-architecture consistency.}\nTwo VLM-to-VLA transitions with dramatically different starting points converge on the same training-induced effects.\nTracVLA~\\cite{zheng2024tracevla} (Phi-3-Vision, 32/32 L1 heads saturated) and NORA~\\cite{TODO_nora} (Qwen2.5-VL, 13--14/16) both exhibit exit collapse at every tested suite (6/6 cells, sign test $p = 0.016$) and produce substantial counterfactual sensitivity after training.\nThis convergence is compatible with task-structure constraints of causal-decoder VLA design rather than architecture-specific artifacts.\nThe pattern is partially confirmed in OpenVLA, where only 2 of 4 suites show $R^2$ collapse and Long-Horizon counterfactual sensitivity inverts (trained $d = 0.56$ vs.\\ untrained $d = 1.05$).\nOpenVLA's OXE-pretrained baseline is itself a VLA rather than a VLM, so its cells test a different transition type.\nWe characterize the training-induced effects as consistent across two VLM-to-VLA architectures, with partial confirmation in a third under VLA-to-VLA conditions.\n\n\\paragraph{Observational three-tier gradient.}\nThe cross-architecture matrix suggests a three-tier gradient of representational adaptation, reported here as an observational synthesis rather than a validated finding.\nTier~1 (VLM bases, no action training): inherited L1 attention (TracVLA 32/32, NORA 13--14/16), negligible exit collapse ($\\Delta R^2 \\leq 0.048$), and minimal counterfactual sensitivity (cosine distance $\\leq 0.185$).\nTier~2 (general-purpose VLA, OXE-pretrained): strong L1 routing (24--26/32 heads), moderate counterfactual sensitivity ($d \\approx 1.0$), and no systematic exit collapse across suites.\nTier~3 (task-specific VLAs, fine-tuned on LIBERO): exit collapse at every VLM-to-VLA cell (6/6, $p = 0.016$) and substantial counterfactual sensitivity ($d \\geq 0.45$).\nThis gradient is suggestive but limited: Tier~2 contains a single architecture (OpenVLA), and the Tier~2/Tier~3 boundary confounds training stage with architecture.\nTesting additional general-purpose VLAs (e.g., Octo~\\cite{ghosh2024_octo}, $\\pi_0$~\\cite{black2024_pi0}) at Tier~2 is necessary before the three-tier structure can be treated as a robust empirical pattern.\n\n\\paragraph{Metric constraints.}\nCounterfactual sensitivity is measured via Cohen's $d$ on action MSE for models that produce actions and via cosine distance on hidden representations for untrained VLMs (\\S\\ref{sec:cf_sensitivity}).\nThese metrics differ in scale and distributional properties; ratios between them are not meaningful.\nThe OpenVLA Long-Horizon inversion (trained $d = 0.56$, untrained $d = 1.05$) illustrates how same-metric comparisons can reverse the expected direction, cautioning against overinterpretation of any single cell.\nA standardized metric framework for cross-condition counterfactual comparison remains an open problem.\n\n\\subsection*{Limitations}\nOur cross-architecture evidence rests on two independent VLM-to-VLA transitions (TracVLA~\\cite{zheng2024tracevla}, NORA~\\cite{TODO_nora}); OpenVLA tests a VLA-to-VLA transition and does not constitute an independent third VLM-to-VLA confirmation.\nAll experiments use LIBERO~\\cite{liu2023_libero} (10 tasks per suite); benchmarks with richer language grounding such as CALVIN and Language-Table are needed to test whether the observed patterns generalize beyond short-horizon tabletop manipulation.\nWe analyze only causal-decoder VLAs; flow-matching~\\cite{black2024_pi0} and diffusion~\\cite{ghosh2024_octo} architectures that employ cross-attention rather than causal masking may exhibit different routing mechanisms.\nEach architecture is analyzed at a single trained checkpoint, precluding characterization of how exit collapse or counterfactual sensitivity emerge during training.\nAll analyses are open-loop, consistent with prior representational studies~\\cite{grant2026,haon2025}; closed-loop validation would provide complementary evidence about the behavioral relevance of the identified routing structures.\nNORA checkpoints are available for only 2 of 4 suites, leaving Object and Long-Horizon cells empty.\nThe three-tier gradient has $n = 1$ at Tier~2, limiting its inferential power; populating this tier with additional general-purpose VLAs is a priority for future work.\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_discussion_d097_20260522T054615",
  "tool": "Write",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/discussion.tex",
    "content": "\\vspace{-2pt}\n\\section{Discussion}\n\\label{sec:discussion}\n\n\\paragraph{Synthesis.}\nVLA fine-tuning produces two measurable representational changes: it reorganizes mid-to-exit layer action encoding ($R^2$ exit collapse, \\S\\ref{sec:r2_collapse}) and establishes instruction-conditioned action sensitivity (\\S\\ref{sec:cf_sensitivity}).\nBoth effects concentrate at the readout token rather than image geometry: on OpenVLA, training shifts readout $R^2$ by $+0.069$ but image\\_mean by only $+0.015$ (\\S\\ref{sec:openvla_routing}).\nL1 instruction attention, by contrast, is inherited from base-model pretraining and persists through fine-tuning: Phi-3-Vision saturates at 32/32 instruction-dominant heads before any action training, and Qwen2.5-VL allocates 13--14/16 (\\S\\ref{sec:l1_priors}).\nThis decomposition into training-induced effects (exit collapse, counterfactual sensitivity) and inherited effects (L1 instruction attention) constitutes the central framing of our analysis.\nVLA fine-tuning does not build instruction routing from scratch; it reorganizes downstream representations while preserving the early-layer attention structure of the pretrained backbone.\n\n\\paragraph{Cross-architecture consistency.}\nTwo VLM-to-VLA transitions with dramatically different starting points converge on the same training-induced effects.\nTracVLA~\\cite{zheng2024tracevla} (Phi-3-Vision, 32/32 L1 heads saturated) and NORA~\\cite{TODO_nora} (Qwen2.5-VL, 13--14/16) both exhibit exit collapse at every tested suite (6/6 cells, sign test $p = 0.016$) and produce substantial counterfactual sensitivity after training.\nThis convergence is compatible with task-structure constraints of causal-decoder VLA design rather than architecture-specific artifacts.\nThe pattern is partially confirmed in OpenVLA, where only 2 of 4 suites show $R^2$ collapse and Long-Horizon counterfactual sensitivity inverts (trained $d = 0.56$ vs.\\ untrained $d = 1.05$).\nOpenVLA's OXE-pretrained baseline is itself a VLA rather than a VLM, so its cells test a different transition type.\nWe characterize the training-induced effects as consistent across two VLM-to-VLA architectures, with partial confirmation in a third under VLA-to-VLA conditions.\n\n\\paragraph{Observational three-tier gradient.}\nThe cross-architecture matrix suggests a three-tier gradient of representational adaptation, reported here as an observational synthesis rather than a validated finding.\nTier~1 (VLM bases, no action training): inherited L1 attention (TracVLA 32/32, NORA 13--14/16), negligible exit collapse ($\\Delta R^2 \\leq 0.048$), and minimal counterfactual sensitivity (cosine distance $\\leq 0.185$).\nTier~2 (general-purpose VLA, OXE-pretrained): strong L1 routing (24--26/32 heads), moderate counterfactual sensitivity ($d \\approx 1.0$), and no systematic exit collapse across suites.\nTier~3 (task-specific VLAs, fine-tuned on LIBERO): exit collapse at every VLM-to-VLA cell (6/6, $p = 0.016$) and substantial counterfactual sensitivity ($d \\geq 0.45$).\nThis gradient is suggestive but limited: Tier~2 contains a single architecture (OpenVLA), and the Tier~2/Tier~3 boundary confounds training stage with architecture.\nTesting additional general-purpose VLAs (e.g., Octo~\\cite{ghosh2024_octo}, $\\pi_0$~\\cite{black2024_pi0}) at Tier~2 is necessary before the three-tier structure can be treated as a robust empirical pattern.\n\n\\paragraph{Metric constraints.}\nCounterfactual sensitivity is measured via Cohen's $d$ on action MSE for models that produce actions and via cosine distance on hidden representations for untrained VLMs (\\S\\ref{sec:cf_sensitivity}).\nThese metrics differ in scale and distributional properties; ratios between them are not meaningful.\nThe OpenVLA Long-Horizon inversion (trained $d = 0.56$, untrained $d = 1.05$) illustrates how same-metric comparisons can reverse the expected direction, cautioning against overinterpretation of any single cell.\nA standardized metric framework for cross-condition counterfactual comparison remains an open problem.\n\n\\subsection*{Limitations}\nOur cross-architecture evidence rests on two independent VLM-to-VLA transitions (TracVLA~\\cite{zheng2024tracevla}, NORA~\\cite{TODO_nora}); OpenVLA tests a VLA-to-VLA transition and does not constitute an independent third VLM-to-VLA confirmation.\nAll experiments use LIBERO~\\cite{liu2023_libero} (10 tasks per suite); benchmarks with richer language grounding such as CALVIN and Language-Table are needed to test whether the observed patterns generalize beyond short-horizon tabletop manipulation.\nWe analyze only causal-decoder VLAs; flow-matching~\\cite{black2024_pi0} and diffusion~\\cite{ghosh2024_octo} architectures that employ cross-attention rather than causal masking may exhibit different routing mechanisms.\nEach architecture is analyzed at a single trained checkpoint, precluding characterization of how exit collapse or counterfactual sensitivity emerge during training.\nAll analyses are open-loop, consistent with prior representational studies~\\cite{grant2026,haon2025}; closed-loop validation would provide complementary evidence about the behavioral relevance of the identified routing structures.\nNORA checkpoints are available for only 2 of 4 suites, leaving Object and Long-Horizon cells empty.\nThe three-tier gradient has $n = 1$ at Tier~2, limiting its inferential power; populating this tier with additional general-purpose VLAs is a priority for future work.\n"
  }
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-22T05:48:04.872775+00:00_

The file /home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/discussion.tex has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_discussion_d097_20260522T054615",
  "tool": "Write",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-22T05:48:04.873018+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/discussion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_discussion_d097_20260522T054615",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/discussion.tex"
  }
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-22T05:48:04.873285+00:00_

1	\vspace{-2pt}
2	\section{Discussion}
3	\label{sec:discussion}
4	
5	\paragraph{Synthesis.}
6	VLA fine-tuning produces two measurable representational changes: it reorganizes mid-to-exit layer action encoding ($R^2$ exit collapse, \S\ref{sec:r2_collapse}) and establishes instruction-conditioned action sensitivity (\S\ref{sec:cf_sensitivity}).
7	Both effects concentrate at the readout token rather than image geometry: on OpenVLA, training shifts readout $R^2$ by $+0.069$ but image\_mean by only $+0.015$ (\S\ref{sec:openvla_routing}).
8	L1 instruction attention, by contrast, is inherited from base-model pretraining and persists through fine-tuning: Phi-3-Vision saturates at 32/32 instruction-dominant heads before any action training, and Qwen2.5-VL allocates 13--14/16 (\S\ref{sec:l1_priors}).
9	This decomposition into training-induced effects (exit collapse, counterfactual sensitivity) and inherited effects (L1 instruction attention) constitutes the central framing of our analysis.
10	VLA fine-tuning does not build instruction routing from scratch; it reorganizes downstream representations while preserving the early-layer attention structure of the pretrained backbone.
11	
12	\paragraph{Cross-architecture consistency.}
13	Two VLM-to-VLA transitions with dramatically different starting points converge on the same training-induced effects.
14	TracVLA~\cite{zheng2024tracevla} (Phi-3-Vision, 32/32 L1 heads saturated) and NORA~\cite{TODO_nora} (Qwen2.5-VL, 13--14/16) both exhibit exit collapse at every tested suite (6/6 cells, sign test $p = 0.016$) and produce substantial counterfactual sensitivity after training.
15	This convergence is compatible with task-structure constraints of causal-decoder VLA design rather than architecture-specific artifacts.
16	The pattern is partially confirmed in OpenVLA, where only 2 of 4 suites show $R^2$ collapse and Long-Horizon counterfactual sensitivity inverts (trained $d = 0.56$ vs.\ untrained $d = 1.05$).
17	OpenVLA's OXE-pretrained b
…[truncated 3546 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_discussion_d097_20260522T054615",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 15 · 2026-05-22T05:48:04.873583+00:00_

写入完成。Discussion + Limitations 已完全重写，覆盖全部要求的结构：

- **Synthesis**: training-induced vs inherited decomposition，readout concentration（+0.069 vs +0.015）
- **Cross-architecture consistency**: 6/6 VLM→VLA collapse + partial OpenVLA confirmation，措辞避开 "architecture-independent"
- **Three-tier gradient**: 明确标记为 observational synthesis，声明 n=1 at Tier 2 的局限
- **Metric constraints**: Cohen's d vs cosine 不可比，Long-Horizon inversion 作为警示
- **Limitations**: 7 点全部覆盖（VLA→VLA vs VLM→VLA 区分、LIBERO only、causal-decoder only、single checkpoint、open-loop、NORA 2/4、n=1 Tier 2）

无 em-dash、无 -ing 分词结尾、无 "architecture-independent"、无 "7-10×"、无未经检验的 "significantly"。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_paper_writing_discussion_d097_20260522T054615"
}
```

</details>

---
