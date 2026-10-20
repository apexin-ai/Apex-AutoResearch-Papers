# paper writing method d097

**Instruction Routing in Fine-Tuned Vision-Language-Action Models: A Cross-Architecture Analysis** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 13
- **Recorded user turns:** 0
- **Tool calls:** 6
- **Original source:** `logs/chats/worker_paper_writing_method_d097_20260522T051809.jsonl`
- **Structured JSON:** [`e674acfc2dd0a9abf9bb.json`](../../sessions/e6/e674acfc2dd0a9abf9bb.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

13 recorded events

### Tool call

_source line 1 · 2026-05-22T05:24:14.912414+00:00_

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
  "session": "worker_paper_writing_method_d097_20260522T051809",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/agent-ml-research/skills/global/paper-writing-norms.skill.md"
  }
}
```

</details>

---

### Tool result

_source line 2 · 2026-05-22T05:24:14.913008+00:00_

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
  "session": "worker_paper_writing_method_d097_20260522T051809",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-22T05:24:14.913216+00:00_

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
  "session": "worker_paper_writing_method_d097_20260522T051809",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/agent-ml-research/skills/global/latex-paper.skill.md"
  }
}
```

</details>

---

### Tool result

_source line 4 · 2026-05-22T05:24:14.913569+00:00_

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
  "session": "worker_paper_writing_method_d097_20260522T051809",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-22T05:24:14.913735+00:00_

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
  "session": "worker_paper_writing_method_d097_20260522T051809",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/method.tex"
  }
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-22T05:24:14.913907+00:00_

1	\section{Method}
2	\label{sec:method}
3	
4	We investigate how action-relevant structure is distributed across a VLA by combining four complementary analyses: cross-instruction probes, attention pattern analysis, RSA, and functional probes.
5	
6	%------------------------------------------------------------------
7	\subsection{Model and Data}
8	\label{sec:model_data}
9	
10	We study OpenVLA-7B~\cite{kim2024_openvla,karamcheti2024}, chaining a frozen DinoSigLIP vision backbone~\cite{zhai2023_siglip,oquab2024_dinov2} (DINOv2 ViT-L/14 + SigLIP-SO400M), an MLP projector (2{,}176-D $\to$ 4{,}096-D), and Llama-2 7B~\cite{touvron2023_llama2} (6.74B parameters) that autoregressively decodes 7-D actions.
11	We use the base checkpoint pretrained on Open X-Embodiment~\cite{padalkar2023_oxe} (970K episodes spanning multiple robot platforms and task types) and evaluate on LIBERO-Goal~\cite{liu2023_libero} (10 tasks, 50 demonstrations each), which was not part of the pretraining mixture.
12	We compare three LLM conditions: (1)~VLA-trained (released checkpoint), (2)~Llama-2 base (pretrained backbone, no VLA fine-tuning), and (3)~untrained (6.74B parameters reinitialized via \texttt{from\_config()}); a fourth condition (task-specific fine-tuning on LIBERO) is compared in \S\ref{sec:learned_routing}.
13	All three share the same frozen vision encoder and projector.
14	
15	%------------------------------------------------------------------
16	\subsection{Representation Extraction}
17	\label{sec:repr_extraction}
18	
19	We extract representations from six sources spanning the VLA pipeline:
20	(a)~\textbf{DinoSigLIP+Projector}, the projector output (4{,}096-D), immediately before LLM processing;
21	(b)~\textbf{LLM image\_mean}, the mean image-token activation at each of 32 layers;
22	(c)~\textbf{LLM readout}, the hidden state at the final pre-action token position at each layer (located after both image and instruction tokens in the causal sequence, it can attend to all preceding context 
…[truncated 4345 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_method_d097_20260522T051809",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-22T05:24:14.914091+00:00_

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
  "session": "worker_paper_writing_method_d097_20260522T051809",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/experiments.tex"
  }
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-22T05:24:14.914361+00:00_

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
  "session": "worker_paper_writing_method_d097_20260522T051809",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-22T05:24:14.914732+00:00_

called Write

<details open><summary>🔧 Tool call — Write</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/method.tex",
  "content": "\\section{Method}\n\\label{sec:method}\n\nWe investigate how action-relevant representations are organized across three VLA architectures using complementary probing, attention, and perturbation analyses.\n\n%------------------------------------------------------------------\n\\subsection{Architectures and Data}\n\\label{sec:arch_data}\n\nWe study three VLAs that span distinct backbone families (Table~\\ref{tab:arch_overview}).\n\\textbf{OpenVLA}~\\cite{kim2024_openvla,karamcheti2024} chains a frozen DinoSigLIP vision backbone~\\cite{zhai2023_siglip,oquab2024_dinov2} (DINOv2 ViT-L/14 + SigLIP-SO400M), an MLP projector (2{,}176-D $\\to$ 4{,}096-D), and Llama-2-7B~\\cite{touvron2023_llama2} (6.74B parameters, 32 layers, 32 multi-head attention [MHA] heads) for autoregressive 7-D action decoding.\nIts base checkpoint is pretrained on Open X-Embodiment~\\cite{padalkar2023_oxe} (OXE; 970K episodes across multiple robot platforms).\n\\textbf{TracVLA}~\\cite{zheng2024tracevla} uses Phi-3-mini~\\cite{abdin2024phi3} (32 layers, 32 MHA heads) with a SigLIP encoder augmented by spatial trace conditioning, trained on an OXE subset.\n\\textbf{NORA}~\\cite{TODO_nora} uses Qwen2.5-VL-3B (36 layers, grouped-query attention [GQA] with 16 query heads and 2 KV heads) with its native vision encoder.\n\nEach architecture is evaluated in trained and untrained conditions.\nA critical asymmetry distinguishes the untrained baselines: OpenVLA's untrained checkpoint is the OXE-pretrained VLA, already fine-tuned for action prediction on 970K episodes, while TracVLA and NORA untrained checkpoints are pure vision-language models (Phi-3-Vision and Qwen2.5-VL) with no action training.\nOpenVLA trained-vs-untrained comparisons therefore measure a VLA-to-VLA transition; TracVLA and NORA comparisons measure VLM-to-VLA transitions.\nThis asymmetry affects the interpretation of all trained/untrained comparisons throughout the paper.\nFor OpenVLA, two additional conditions support deep-dive analyses (\\S\\ref{sec:openvla_routing}): the Llama-2 base language model (no VLA fine-tuning) and a random-weight initialization via \\texttt{from\\_config()}.\n\nWe evaluate on LIBERO~\\cite{liu2023_libero}, comprising four task suites (Goal, Spatial, Object, Long-Horizon) with 10 tasks and 50 demonstrations each.\nThe three architectures and four suites form a $3 \\times 4$ matrix; 10 of 12 cells are filled (NORA Object and Long-Horizon lack available checkpoints).\n\n\\begin{table}[t]\n\\centering\n\\caption{Architectures studied. The untrained baselines differ in kind: OpenVLA's baseline is an OXE-pretrained VLA that produces actions; TracVLA and NORA baselines are pure VLMs with no action training.}\n\\label{tab:arch_overview}\n\\footnotesize\n\\setlength{\\tabcolsep}{3pt}\n\\begin{tabular}{@{}llccll@{}}\n\\toprule\nArch. & Backbone & Layers & Attention & Vision Enc. & Untrained Baseline \\\\\n\\midrule\nOpenVLA & Llama-2-7B & 32 & 32 MHA & DinoSigLIP $\\to$ MLP proj. & OXE-pret.\\ VLA \\\\\nTracVLA & Phi-3-mini & 32 & 32 MHA & SigLIP + spatial trace & Phi-3-Vision (VLM) \\\\\nNORA & Qwen2.5-VL-3B & 36 & 16q/2kv GQA & Qwen2.5-VL native & Qwen2.5-VL (VLM) \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n%------------------------------------------------------------------\n\\subsection{Representation Extraction}\n\\label{sec:repr_extraction}\n\nFrom each architecture, we extract hidden states at every transformer layer from two token positions: (a)~\\textbf{image\\_mean}, the mean activation over image tokens, and (b)~\\textbf{readout}, the hidden state at the final pre-action token, which follows both image and instruction tokens in the causal sequence and can attend to all preceding context.\nL0 denotes the embedding layer output, L1 through L$N$ the hidden states after each transformer layer ($N = 32$ for OpenVLA and TracVLA, $N = 36$ for NORA), with the final layer including the output layer norm.\nIn all three architectures, image tokens precede instruction tokens; the causal mask prevents image tokens from attending to instructions by construction.\n\nWe cross two factors in a $2 \\times 2$ factorial design: \\emph{training status} (trained vs.\\ untrained) and \\emph{instruction presence} (with vs.\\ without task description), applied to all 10 available cells in the cross-architecture matrix.\nOpenVLA additionally provides representations from the DinoSigLIP projector output (4{,}096-D), DINOv2 and CLIP external baselines, and the branch-split before fusion; these sources support the OpenVLA deep-dive analyses (\\S\\ref{sec:openvla_routing}).\n\n%------------------------------------------------------------------\n\\subsection{Cross-Architecture Analyses}\n\\label{sec:cross_arch_analyses}\n\nThree analyses are applied to every available cell in the $3 \\times 4$ matrix.\n\n\\paragraph{$R^2$ action probes.}\nTwo-layer MLP probes~\\cite{alain2017} ($d_\\text{in} \\to 256 \\to 7$, ReLU) are trained to predict 7-D action vectors from frozen representations at each layer (Adam, lr${}=10^{-3}$, batch size 256, 50 epochs, early stopping patience 5).\nTrain/test splits follow demonstration boundaries (demos 0--39 vs.\\ 40--49) to prevent within-trajectory leakage.\nWe report per-task macro-averaged $R^2$ with bootstrap paired comparisons (10{,}000 resamples).\n\n\\paragraph{L1 attention head profiling.}\nAt L1, each attention head is classified as instruction-dominant ($>50\\%$ of readout-token attention allocated to instruction tokens) or image-dominant.\nResults are reported as $k/N$ instruction-dominant heads, where $N$ is the total L1 head count: 32 for OpenVLA and TracVLA (MHA), 16 for NORA (GQA query heads).\nSensitivity analysis at thresholds from $30\\%$ to $70\\%$ confirms ordering robustness (Appendix~\\ref{sec:threshold_sensitivity}).\n\n\\paragraph{Counterfactual instruction perturbation.}\nThe instruction is replaced with four conditions: empty string, wrong task from the same suite, shuffled tokens, and paraphrased instruction.\nA metric constraint arises from the trained/untrained asymmetry.\nTrained models produce action outputs; their sensitivity is measured via Cohen's $d$ on action MSE (OpenVLA, TracVLA) or cosine distance on action representations (NORA).\nUntrained VLMs (Phi-3-Vision, Qwen2.5-VL) do not generate actions; their sensitivity is measured via cosine distance on hidden representations, a metric with different scale and distributional properties.\nCross-metric ratios between Cohen's $d$ and cosine distance are therefore invalid (\\S\\ref{sec:cf_sensitivity}).\nOpenVLA's OXE-pretrained untrained checkpoint is the exception: because it produces actions, same-metric (Cohen's $d$) trained-vs-untrained comparison is possible for that condition.\n\n%------------------------------------------------------------------\n\\subsection{OpenVLA-Specific Analyses}\n\\label{sec:openvla_analyses}\n\nThree additional analyses are applied to OpenVLA to characterize instruction encoding and representational geometry.\n\n\\paragraph{Cross-instruction probes.}\nEach visual frame is paired with all 10 LIBERO-Goal task instructions, producing 10 representation vectors per frame per layer.\nA 10-way linear classifier identifies which instruction was present, applied separately to image\\_mean and readout positions, with leave-one-out cross-validation (LOOCV) over 10 folds.\n\n\\paragraph{Representational similarity analysis (RSA).}\nRSA~\\cite{kriegeskorte2008} quantifies geometric alignment between representations and the action space.\nFor each task, we compute pairwise representational dissimilarity matrices (RDMs) using cosine distances for representations and Euclidean distances for 7-D action vectors, from within-task observation pairs across 50 demonstrations.\nAlignment is measured via Spearman $\\rho$ between upper-triangular RDM entries; we report mean $\\rho$ across 10 tasks with 95\\% confidence intervals from 10{,}000 bootstrap resamples at the task level~\\cite{nili2014toolbox}.\nWe prefer RSA over CKA~\\cite{kornblith2019}: RSA captures relative distance structure via scale-invariant rank correlation, suited to comparing high- and low-dimensional spaces (4{,}096-D vs.\\ 7-D), while CKA measures global subspace overlap that can remain high when geometric structure differs.\nBoth metrics are reported in Appendix~\\ref{sec:cka_appendix}; their divergence (\\S\\ref{sec:nonmonotonic}) confirms that neither alone fully characterizes representational structure.\n\n\\paragraph{External baselines.}\nDINOv2 ViT-L/14~\\cite{oquab2024_dinov2} (\\texttt{cls\\_token}/\\texttt{patch\\_mean}) and CLIP ViT-L/14~\\cite{radford2021_clip} (\\texttt{patch\\_mean}) provide self-supervised and vision-language pretrained reference points for probing and RSA.\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_method_d097_20260522T051809",
  "tool": "Write",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/method.tex",
    "content": "\\section{Method}\n\\label{sec:method}\n\nWe investigate how action-relevant representations are organized across three VLA architectures using complementary probing, attention, and perturbation analyses.\n\n%------------------------------------------------------------------\n\\subsection{Architectures and Data}\n\\label{sec:arch_data}\n\nWe study three VLAs that span distinct backbone families (Table~\\ref{tab:arch_overview}).\n\\textbf{OpenVLA}~\\cite{kim2024_openvla,karamcheti2024} chains a frozen DinoSigLIP vision backbone~\\cite{zhai2023_siglip,oquab2024_dinov2} (DINOv2 ViT-L/14 + SigLIP-SO400M), an MLP projector (2{,}176-D $\\to$ 4{,}096-D), and Llama-2-7B~\\cite{touvron2023_llama2} (6.74B parameters, 32 layers, 32 multi-head attention [MHA] heads) for autoregressive 7-D action decoding.\nIts base checkpoint is pretrained on Open X-Embodiment~\\cite{padalkar2023_oxe} (OXE; 970K episodes across multiple robot platforms).\n\\textbf{TracVLA}~\\cite{zheng2024tracevla} uses Phi-3-mini~\\cite{abdin2024phi3} (32 layers, 32 MHA heads) with a SigLIP encoder augmented by spatial trace conditioning, trained on an OXE subset.\n\\textbf{NORA}~\\cite{TODO_nora} uses Qwen2.5-VL-3B (36 layers, grouped-query attention [GQA] with 16 query heads and 2 KV heads) with its native vision encoder.\n\nEach architecture is evaluated in trained and untrained conditions.\nA critical asymmetry distinguishes the untrained baselines: OpenVLA's untrained checkpoint is the OXE-pretrained VLA, already fine-tuned for action prediction on 970K episodes, while TracVLA and NORA untrained checkpoints are pure vision-language models (Phi-3-Vision and Qwen2.5-VL) with no action training.\nOpenVLA trained-vs-untrained comparisons therefore measure a VLA-to-VLA transition; TracVLA and NORA comparisons measure VLM-to-VLA transitions.\nThis asymmetry affects the interpretation of all trained/untrained comparisons throughout the paper.\nFor OpenVLA, two additional conditions support deep-dive analyses (\\S\\ref{sec:openvla_routing}): the Llama-2 base language model (no VLA fine-tuning) and a random-weight initialization via \\texttt{from\\_config()}.\n\nWe evaluate on LIBERO~\\cite{liu2023_libero}, comprising four task suites (Goal, Spatial, Object, Long-Horizon) with 10 tasks and 50 demonstrations each.\nThe three architectures and four suites form a $3 \\times 4$ matrix; 10 of 12 cells are filled (NORA Object and Long-Horizon lack available checkpoints).\n\n\\begin{table}[t]\n\\centering\n\\caption{Architectures studied. The untrained baselines differ in kind: OpenVLA's baseline is an OXE-pretrained VLA that produces actions; TracVLA and NORA baselines are pure VLMs with no action training.}\n\\label{tab:arch_overview}\n\\footnotesize\n\\setlength{\\tabcolsep}{3pt}\n\\begin{tabular}{@{}llccll@{}}\n\\toprule\nArch. & Backbone & Layers & Attention & Vision Enc. & Untrained Baseline \\\\\n\\midrule\nOpenVLA & Llama-2-7B & 32 & 32 MHA & DinoSigLIP $\\to$ MLP proj. & OXE-pret.\\ VLA \\\\\nTracVLA & Phi-3-mini & 32 & 32 MHA & SigLIP + spatial trace & Phi-3-Vision (VLM) \\\\\nNORA & Qwen2.5-VL-3B & 36 & 16q/2kv GQA & Qwen2.5-VL native & Qwen2.5-VL (VLM) \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n%------------------------------------------------------------------\n\\subsection{Representation Extraction}\n\\label{sec:repr_extraction}\n\nFrom each architecture, we extract hidden states at every transformer layer from two token positions: (a)~\\textbf{image\\_mean}, the mean activation over image tokens, and (b)~\\textbf{readout}, the hidden state at the final pre-action token, which follows both image and instruction tokens in the causal sequence and can attend to all preceding context.\nL0 denotes the embedding layer output, L1 through L$N$ the hidden states after each transformer layer ($N = 32$ for OpenVLA and TracVLA, $N = 36$ for NORA), with the final layer including the output layer norm.\nIn all three architectures, image tokens precede instruction tokens; the causal mask prevents image tokens from attending to instructions by construction.\n\nWe cross two factors in a $2 \\times 2$ factorial design: \\emph{training status} (trained vs.\\ untrained) and \\emph{instruction presence} (with vs.\\ without task description), applied to all 10 available cells in the cross-architecture matrix.\nOpenVLA additionally provides representations from the DinoSigLIP projector output (4{,}096-D), DINOv2 and CLIP external baselines, and the branch-split before fusion; these sources support the OpenVLA deep-dive analyses (\\S\\ref{sec:openvla_routing}).\n\n%------------------------------------------------------------------\n\\subsection{Cross-Architecture Analyses}\n\\label{sec:cross_arch_analyses}\n\nThree analyses are applied to every available cell in the $3 \\times 4$ matrix.\n\n\\paragraph{$R^2$ action probes.}\nTwo-layer MLP probes~\\cite{alain2017} ($d_\\text{in} \\to 256 \\to 7$, ReLU) are trained to predict 7-D action vectors from frozen representations at each layer (Adam, lr${}=10^{-3}$, batch size 256, 50 epochs, early stopping patience 5).\nTrain/test splits follow demonstration boundaries (demos 0--39 vs.\\ 40--49) to prevent within-trajectory leakage.\nWe report per-task macro-averaged $R^2$ with bootstrap paired comparisons (10{,}000 resamples).\n\n\\paragraph{L1 attention head profiling.}\nAt L1, each attention head is classified as instruction-dominant ($>50\\%$ of readout-token attention allocated to instruction tokens) or image-dominant.\nResults are reported as $k/N$ instruction-dominant heads, where $N$ is the total L1 head count: 32 for OpenVLA and TracVLA (MHA), 16 for NORA (GQA query heads).\nSensitivity analysis at thresholds from $30\\%$ to $70\\%$ confirms ordering robustness (Appendix~\\ref{sec:threshold_sensitivity}).\n\n\\paragraph{Counterfactual instruction perturbation.}\nThe instruction is replaced with four conditions: empty string, wrong task from the same suite, shuffled tokens, and paraphrased instruction.\nA metric constraint arises from the trained/untrained asymmetry.\nTrained models produce action outputs; their sensitivity is measured via Cohen's $d$ on action MSE (OpenVLA, TracVLA) or cosine distance on action representations (NORA).\nUntrained VLMs (Phi-3-Vision, Qwen2.5-VL) do not generate actions; their sensitivity is measured via cosine distance on hidden representations, a metric with different scale and distributional properties.\nCross-metric ratios between Cohen's $d$ and cosine distance are therefore invalid (\\S\\ref{sec:cf_sensitivity}).\nOpenVLA's OXE-pretrained untrained checkpoint is the exception: because it produces actions, same-metric (Cohen's $d$) trained-vs-untrained comparison is possible for that condition.\n\n%------------------------------------------------------------------\n\\subsection{OpenVLA-Specific Analyses}\n\\label{sec:openvla_analyses}\n\nThree additional analyses are applied to OpenVLA to characterize instruction encoding and representational geometry.\n\n\\paragraph{Cross-instruction probes.}\nEach visual frame is paired with all 10 LIBERO-Goal task instructions, producing 10 representation vectors per frame per layer.\nA 10-way linear classifier identifies which instruction was present, applied separately to image\\_mean and readout positions, with leave-one-out cross-validation (LOOCV) over 10 folds.\n\n\\paragraph{Representational similarity analysis (RSA).}\nRSA~\\cite{kriegeskorte2008} quantifies geometric alignment between representations and the action space.\nFor each task, we compute pairwise representational dissimilarity matrices (RDMs) using cosine distances for representations and Euclidean distances for 7-D action vectors, from within-task observation pairs across 50 demonstrations.\nAlignment is measured via Spearman $\\rho$ between upper-triangular RDM entries; we report mean $\\rho$ across 10 tasks with 95\\% confidence intervals from 10{,}000 bootstrap resamples at the task level~\\cite{nili2014toolbox}.\nWe prefer RSA over CKA~\\cite{kornblith2019}: RSA captures relative distance structure via scale-invariant rank correlation, suited to comparing high- and low-dimensional spaces (4{,}096-D vs.\\ 7-D), while CKA measures global subspace overlap that can remain high when geometric structure differs.\nBoth metrics are reported in Appendix~\\ref{sec:cka_appendix}; their divergence (\\S\\ref{sec:nonmonotonic}) confirms that neither alone fully characterizes representational structure.\n\n\\paragraph{External baselines.}\nDINOv2 ViT-L/14~\\cite{oquab2024_dinov2} (\\texttt{cls\\_token}/\\texttt{patch\\_mean}) and CLIP ViT-L/14~\\cite{radford2021_clip} (\\texttt{patch\\_mean}) provide self-supervised and vision-language pretrained reference points for probing and RSA.\n"
  }
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-22T05:24:14.915071+00:00_

The file /home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/method.tex has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_method_d097_20260522T051809",
  "tool": "Write",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-22T05:24:14.915255+00:00_

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
  "session": "worker_paper_writing_method_d097_20260522T051809",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/method.tex"
  }
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-22T05:24:14.915437+00:00_

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
…[truncated 6864 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_method_d097_20260522T051809",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 13 · 2026-05-22T05:24:14.915676+00:00_

文件已写入。结构：

- **§3.1 Architectures and Data**: 三架构描述 + Table 1 (arch_overview) + trained/untrained 不对称性说明 + LIBERO 3×4 矩阵 (10/12 cells)
- **§3.2 Representation Extraction**: readout + image_mean 双位点提取，层标记泛化 (L0-L32/L36)，2×2 factorial 扩展到全部 10 cells，OpenVLA 额外表征源指向 §4.2
- **§3.3 Cross-Architecture Analyses**: R² probes、L1 attention profiling (k/N notation, N=32 or 16)、counterfactual perturbation + metric constraint (Cohen's d vs cosine distance 不可比)
- **§3.4 OpenVLA-Specific Analyses**: cross-instruction probes、RSA + Why RSA over CKA、DINOv2/CLIP external baselines

D097 约束全部遵守：无 "architecture-independent"、无 cross-metric ratio 暗示、NORA 用 `\cite{TODO_nora}`、TracVLA 用 `\cite{zheng2024tracevla}`、无 "significantly"/"state-of-the-art"。无 em-dash、无 -ing 短语结尾、无 AI 腔调用词。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_paper_writing_method_d097_20260522T051809"
}
```

</details>

---
