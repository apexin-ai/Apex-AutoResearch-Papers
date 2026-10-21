# paper writing experimental setup reframe

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 13
- **Recorded user turns:** 0
- **Tool calls:** 6
- **Original source:** `logs/chats/worker_paper_writing_experimental_setup_reframe_20260520T110930.jsonl`
- **Structured JSON:** [`74bda7c5362ca15625fd.json`](../../sessions/74/74bda7c5362ca15625fd.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

13 recorded events

### Tool call

_source line 1 · 2026-05-20T11:13:05.296267+00:00_

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
  "session": "worker_paper_writing_experimental_setup_reframe_20260520T110930",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/agent-ml-research/skills/global/paper-writing-norms.skill.md"
  }
}
```

</details>

---

### Tool result

_source line 2 · 2026-05-20T11:13:05.296876+00:00_

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
  "session": "worker_paper_writing_experimental_setup_reframe_20260520T110930",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-20T11:13:05.297104+00:00_

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
  "session": "worker_paper_writing_experimental_setup_reframe_20260520T110930",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/agent-ml-research/skills/global/latex-paper.skill.md"
  }
}
```

</details>

---

### Tool result

_source line 4 · 2026-05-20T11:13:05.297740+00:00_

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
  "session": "worker_paper_writing_experimental_setup_reframe_20260520T110930",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-20T11:13:05.297983+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/experimental_setup.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_experimental_setup_reframe_20260520T110930",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/experimental_setup.tex"
  }
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-20T11:13:05.298193+00:00_

1	\section{Methods and Experimental Setup}
2	\label{sec:experimental_setup}
3	
4	\subsection{Architectures and Benchmark}
5	\label{sec:setup_overview}
6	
7	We study two VLA architectures whose vision connectors differ in how they map encoder patches to language model input tokens (Figure~\ref{fig:architecture}). SmolVLA~\cite{shukor2025smolvla} (451.5M parameters) encodes each camera image with SigLIP~\cite{zhai2023siglip} into 1024 patches on a $32 \times 32$ grid, then applies a pixel-shuffle connector that folds each $4 \times 4$ block into one token by channel concatenation, producing 64 tokens per camera (128 total from two cameras). Each token encodes 16 spatially contiguous patches; removing one eliminates an entire $4 \times 4$ receptive field with no redundancy. The 128 tokens enter a Qwen2-0.5B backbone~\cite{yang2024qwen2} that generates continuous 7-DoF actions via flow matching~\cite{lipman2023flow}. OpenVLA~\cite{kim2024openvla} (7B parameters) uses DINOv2~\cite{oquab2023dinov2} and SigLIP encoders with a three-layer MLP projector (GELU activations) that maps each patch independently into a Llama-2 backbone, producing 256 tokens that preserve per-token independence.
8	
9	\begin{figure}[t]
10	\centering
11	\includegraphics[width=\linewidth]{figures/paper/fig_architecture.pdf}
12	\caption{Vision connector comparison. SmolVLA's pixel-shuffle folds $4{\times}4$ patches into single tokens (128 total, spatially entangled). OpenVLA's MLP projector maps each patch independently (256 tokens, per-token independence).}
13	\label{fig:architecture}
14	\end{figure}
15	
16	We evaluate on LIBERO~\cite{liu2023libero}, a suite of language-conditioned tabletop manipulation tasks with three suites: Object (10 manipulation tasks), Spatial (10 spatial reasoning tasks), and Goal (10 goal-conditioned tasks). Each condition uses 50 episodes per task (500 per suite), evaluated by closed-loop Success Rate (SR) with Wilson 95\% confidence intervals. SmolVLA baselines: 44.8\% (Obj
…[truncated 2308 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_experimental_setup_reframe_20260520T110930",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-20T11:13:05.298560+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/experimental_setup.tex",
  "old_string": "We study two VLA architectures whose vision connectors differ in how they map encoder patches to language model input tokens (Figure~\\ref{fig:architecture}). SmolVLA~\\cite{shukor2025smolvla} (451.5M parameters) encodes each camera image with SigLIP~\\cite{zhai2023siglip} into 1024 patches on a $32 \\times 32$ grid, then applies a pixel-shuffle connector that folds each $4 \\times 4$ block into one token by channel concatenation, producing 64 tokens per camera (128 total from two cameras). Each token encodes 16 spatially contiguous patches; removing one eliminates an entire $4 \\times 4$ receptive field with no redundancy. The 128 tokens enter a Qwen2-0.5B backbone~\\cite{yang2024qwen2} that generates continuous 7-DoF actions via flow matching~\\cite{lipman2023flow}. OpenVLA~\\cite{kim2024openvla} (7B parameters) uses DINOv2~\\cite{oquab2023dinov2} and SigLIP encoders with a three-layer MLP projector (GELU activations) that maps each patch independently into a Llama-2 backbone, producing 256 tokens that preserve per-token independence.\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\linewidth]{figures/paper/fig_architecture.pdf}\n\\caption{Vision connector comparison. SmolVLA's pixel-shuffle folds $4{\\times}4$ patches into single tokens (128 total, spatially entangled). OpenVLA's MLP projector maps each patch independently (256 tokens, per-token independence).}\n\\label{fig:architecture}\n\\end{figure}\n\nWe evaluate on LIBERO~\\cite{liu2023libero}, a suite of language-conditioned tabletop manipulation tasks with three suites: Object (10 manipulation tasks), Spatial (10 spatial reasoning tasks), and Goal (10 goal-conditioned tasks). Each condition uses 50 episodes per task (500 per suite), evaluated by closed-loop Success Rate (SR) with Wilson 95\\% confidence intervals. SmolVLA baselines: 44.8\\% (Object), 51.8\\% (Spatial), 63.0\\% (Goal); OpenVLA baseline: 74.0\\% (Object).",
  "new_string": "We study five VLA architectures spanning three vision connector families (Figure~\\ref{fig:architecture}).\n\n\\textbf{Linear projection.} $\\pi_0$~\\cite{black2024pi0} (3.3B parameters, 256 tokens) maps SigLIP~\\cite{zhai2023siglip} patches through a linear layer into a PaliGemma backbone and generates actions via flow matching~\\cite{lipman2023flow}. X-VLA~\\cite{zheng2025xvla} (880M parameters, 50 tokens) augments its linear projection with a 12-layer BART encoder~\\cite{lewis2020bart}; self-attention in these layers introduces cross-token mixing that makes the effective pipeline more complex than the nominal ``linear projection'' label suggests.\n\n\\textbf{MLP projector.} OpenVLA~\\cite{kim2024openvla} (7B parameters, 256 tokens) fuses DINOv2~\\cite{oquab2023dinov2} and SigLIP encoders through a three-layer MLP (GELU activations) that maps each patch independently into a Llama-2 backbone. OFT~\\cite{kim2025openoft} shares this architecture with an optimized fine-tuning action head; we include it for attention entropy comparison only.\n\n\\textbf{Spatial folding.} SmolVLA~\\cite{shukor2025smolvla} (450M parameters, 128 tokens from two cameras) encodes each camera image with SigLIP into 1024 patches, then applies a pixel-shuffle connector that folds each $4{\\times}4$ block into one token by channel concatenation (64 per camera). Each token encodes 16 spatially contiguous patches; removing one eliminates an entire $4{\\times}4$ receptive field. The tokens enter a Qwen2-0.5B backbone~\\cite{yang2024qwen2} with flow matching action generation.\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\linewidth]{figures/paper/fig_architecture.pdf}\n\\caption{Vision connector comparison. SmolVLA's pixel-shuffle folds $4{\\times}4$ patches into single tokens (128 total, spatially entangled). OpenVLA's MLP projector maps each patch independently (256 tokens, per-token independence).}\n\\label{fig:architecture}\n\\end{figure}\n\nWe evaluate on LIBERO~\\cite{liu2023libero}, a suite of language-conditioned tabletop manipulation tasks organized into three suites: Object (10 tasks), Spatial (10 tasks), and Goal (10 tasks). Each suite uses 50 episodes per task (500 total), evaluated by closed-loop Success Rate (SR) with Wilson 95\\% confidence intervals. Full fine-tuning baselines on Object: SmolVLA 44.8\\%, OpenVLA 74.0\\%, X-VLA 99.2\\%."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_experimental_setup_reframe_20260520T110930",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/experimental_setup.tex",
    "old_string": "We study two VLA architectures whose vision connectors differ in how they map encoder patches to language model input tokens (Figure~\\ref{fig:architecture}). SmolVLA~\\cite{shukor2025smolvla} (451.5M parameters) encodes each camera image with SigLIP~\\cite{zhai2023siglip} into 1024 patches on a $32 \\times 32$ grid, then applies a pixel-shuffle connector that folds each $4 \\times 4$ block into one token by channel concatenation, producing 64 tokens per camera (128 total from two cameras). Each token encodes 16 spatially contiguous patches; removing one eliminates an entire $4 \\times 4$ receptive field with no redundancy. The 128 tokens enter a Qwen2-0.5B backbone~\\cite{yang2024qwen2} that generates continuous 7-DoF actions via flow matching~\\cite{lipman2023flow}. OpenVLA~\\cite{kim2024openvla} (7B parameters) uses DINOv2~\\cite{oquab2023dinov2} and SigLIP encoders with a three-layer MLP projector (GELU activations) that maps each patch independently into a Llama-2 backbone, producing 256 tokens that preserve per-token independence.\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\linewidth]{figures/paper/fig_architecture.pdf}\n\\caption{Vision connector comparison. SmolVLA's pixel-shuffle folds $4{\\times}4$ patches into single tokens (128 total, spatially entangled). OpenVLA's MLP projector maps each patch independently (256 tokens, per-token independence).}\n\\label{fig:architecture}\n\\end{figure}\n\nWe evaluate on LIBERO~\\cite{liu2023libero}, a suite of language-conditioned tabletop manipulation tasks with three suites: Object (10 manipulation tasks), Spatial (10 spatial reasoning tasks), and Goal (10 goal-conditioned tasks). Each condition uses 50 episodes per task (500 per suite), evaluated by closed-loop Success Rate (SR) with Wilson 95\\% confidence intervals. SmolVLA baselines: 44.8\\% (Object), 51.8\\% (Spatial), 63.0\\% (Goal); OpenVLA baseline: 74.0\\% (Object).",
    "new_string": "We study five VLA architectures spanning three vision connector families (Figure~\\ref{fig:architecture}).\n\n\\textbf{Linear projection.} $\\pi_0$~\\cite{black2024pi0} (3.3B parameters, 256 tokens) maps SigLIP~\\cite{zhai2023siglip} patches through a linear layer into a PaliGemma backbone and generates actions via flow matching~\\cite{lipman2023flow}. X-VLA~\\cite{zheng2025xvla} (880M parameters, 50 tokens) augments its linear projection with a 12-layer BART encoder~\\cite{lewis2020bart}; self-attention in these layers introduces cross-token mixing that makes the effective pipeline more complex than the nominal ``linear projection'' label suggests.\n\n\\textbf{MLP projector.} OpenVLA~\\cite{kim2024openvla} (7B parameters, 256 tokens) fuses DINOv2~\\cite{oquab2023dinov2} and SigLIP encoders through a three-layer MLP (GELU activations) that maps each patch independently into a Llama-2 backbone. OFT~\\cite{kim2025openoft} shares this architecture with an optimized fine-tuning action head; we include it for attention entropy comparison only.\n\n\\textbf{Spatial folding.} SmolVLA~\\cite{shukor2025smolvla} (450M parameters, 128 tokens from two cameras) encodes each camera image with SigLIP into 1024 patches, then applies a pixel-shuffle connector that folds each $4{\\times}4$ block into one token by channel concatenation (64 per camera). Each token encodes 16 spatially contiguous patches; removing one eliminates an entire $4{\\times}4$ receptive field. The tokens enter a Qwen2-0.5B backbone~\\cite{yang2024qwen2} with flow matching action generation.\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\linewidth]{figures/paper/fig_architecture.pdf}\n\\caption{Vision connector comparison. SmolVLA's pixel-shuffle folds $4{\\times}4$ patches into single tokens (128 total, spatially entangled). OpenVLA's MLP projector maps each patch independently (256 tokens, per-token independence).}\n\\label{fig:architecture}\n\\end{figure}\n\nWe evaluate on LIBERO~\\cite{liu2023libero}, a suite of language-conditioned tabletop manipulation tasks organized into three suites: Object (10 tasks), Spatial (10 tasks), and Goal (10 tasks). Each suite uses 50 episodes per task (500 total), evaluated by closed-loop Success Rate (SR) with Wilson 95\\% confidence intervals. Full fine-tuning baselines on Object: SmolVLA 44.8\\%, OpenVLA 74.0\\%, X-VLA 99.2\\%."
  }
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-20T11:13:05.298802+00:00_

The file /home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/experimental_setup.tex has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_experimental_setup_reframe_20260520T110930",
  "tool": "Edit",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-20T11:13:05.298948+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/experimental_setup.tex",
  "old_string": "\\subsection{OpenVLA Cross-Architecture Evaluation}\n\\label{sec:openvla_eval_setup}\n\nWe evaluate OpenVLA-7B on LIBERO-Object under random token removal (true removal) at $k \\in \\{0.30, 0.50, 0.70, 0.90, 0.95\\}$, retaining 30\\%--95\\% of 256 vision tokens. No learned scorer is used; the comparison isolates the vision connector's influence under the simplest pruning strategy.",
  "new_string": "\\subsection{Cross-Model Pruning Protocol}\n\\label{sec:openvla_eval_setup}\n\nFor cross-model comparison, we apply a unified pruning protocol: compute each vision token's L2 norm, rank tokens, and set the bottom $(1{-}k)$ fraction to zero. OpenVLA is evaluated on LIBERO-Object with random token removal (true removal) at $k \\in \\{0.30, 0.50, 0.70, 0.90, 0.95\\}$. X-VLA uses random token removal at $k \\in \\{0.1, 0.2, 0.3, 0.5, 0.7, 0.9, 0.95\\}$; results at $k \\leq 0.5$ cover 4 of 10 tasks. $\\pi_0$ is evaluated offline only, reporting normalized L1 action loss at $k \\in \\{0.1, 0.5\\}$. OFT provides diagnostic measurements without pruning evaluation.\n\nTwo metrics characterize each model's vision token structure from a single forward pass on task-relevant frames. \\emph{Attention entropy ratio}: normalized Shannon entropy of attention weights over vision tokens, where low entropy indicates concentrated attention on few tokens. \\emph{Token importance CV}: coefficient of variation of L2 norms across vision tokens, where high CV signals uneven importance favorable to pruning."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_experimental_setup_reframe_20260520T110930",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/experimental_setup.tex",
    "old_string": "\\subsection{OpenVLA Cross-Architecture Evaluation}\n\\label{sec:openvla_eval_setup}\n\nWe evaluate OpenVLA-7B on LIBERO-Object under random token removal (true removal) at $k \\in \\{0.30, 0.50, 0.70, 0.90, 0.95\\}$, retaining 30\\%--95\\% of 256 vision tokens. No learned scorer is used; the comparison isolates the vision connector's influence under the simplest pruning strategy.",
    "new_string": "\\subsection{Cross-Model Pruning Protocol}\n\\label{sec:openvla_eval_setup}\n\nFor cross-model comparison, we apply a unified pruning protocol: compute each vision token's L2 norm, rank tokens, and set the bottom $(1{-}k)$ fraction to zero. OpenVLA is evaluated on LIBERO-Object with random token removal (true removal) at $k \\in \\{0.30, 0.50, 0.70, 0.90, 0.95\\}$. X-VLA uses random token removal at $k \\in \\{0.1, 0.2, 0.3, 0.5, 0.7, 0.9, 0.95\\}$; results at $k \\leq 0.5$ cover 4 of 10 tasks. $\\pi_0$ is evaluated offline only, reporting normalized L1 action loss at $k \\in \\{0.1, 0.5\\}$. OFT provides diagnostic measurements without pruning evaluation.\n\nTwo metrics characterize each model's vision token structure from a single forward pass on task-relevant frames. \\emph{Attention entropy ratio}: normalized Shannon entropy of attention weights over vision tokens, where low entropy indicates concentrated attention on few tokens. \\emph{Token importance CV}: coefficient of variation of L2 norms across vision tokens, where high CV signals uneven importance favorable to pruning."
  }
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-20T11:13:05.299198+00:00_

The file /home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/experimental_setup.tex has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_experimental_setup_reframe_20260520T110930",
  "tool": "Edit",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-20T11:13:05.299400+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/experimental_setup.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_experimental_setup_reframe_20260520T110930",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/experimental_setup.tex"
  }
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-20T11:13:05.299586+00:00_

1	\section{Methods and Experimental Setup}
2	\label{sec:experimental_setup}
3	
4	\subsection{Architectures and Benchmark}
5	\label{sec:setup_overview}
6	
7	We study five VLA architectures spanning three vision connector families (Figure~\ref{fig:architecture}).
8	
9	\textbf{Linear projection.} $\pi_0$~\cite{black2024pi0} (3.3B parameters, 256 tokens) maps SigLIP~\cite{zhai2023siglip} patches through a linear layer into a PaliGemma backbone and generates actions via flow matching~\cite{lipman2023flow}. X-VLA~\cite{zheng2025xvla} (880M parameters, 50 tokens) augments its linear projection with a 12-layer BART encoder~\cite{lewis2020bart}; self-attention in these layers introduces cross-token mixing that makes the effective pipeline more complex than the nominal ``linear projection'' label suggests.
10	
11	\textbf{MLP projector.} OpenVLA~\cite{kim2024openvla} (7B parameters, 256 tokens) fuses DINOv2~\cite{oquab2023dinov2} and SigLIP encoders through a three-layer MLP (GELU activations) that maps each patch independently into a Llama-2 backbone. OFT~\cite{kim2025openoft} shares this architecture with an optimized fine-tuning action head; we include it for attention entropy comparison only.
12	
13	\textbf{Spatial folding.} SmolVLA~\cite{shukor2025smolvla} (450M parameters, 128 tokens from two cameras) encodes each camera image with SigLIP into 1024 patches, then applies a pixel-shuffle connector that folds each $4{\times}4$ block into one token by channel concatenation (64 per camera). Each token encodes 16 spatially contiguous patches; removing one eliminates an entire $4{\times}4$ receptive field. The tokens enter a Qwen2-0.5B backbone~\cite{yang2024qwen2} with flow matching action generation.
14	
15	\begin{figure}[t]
16	\centering
17	\includegraphics[width=\linewidth]{figures/paper/fig_architecture.pdf}
18	\caption{Vision connector comparison. SmolVLA's pixel-shuffle folds $4{\times}4$ patches into single tokens (128 total, spatially entangled). OpenVLA's MLP projecto
…[truncated 3475 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_experimental_setup_reframe_20260520T110930",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 13 · 2026-05-20T11:13:05.299792+00:00_

完成。修改内容：

- **§3.1**: 从 2 模型扩展到 5 模型，按 connector 类型分三组（linear projection: π0 + X-VLA; MLP projector: OpenVLA + OFT; spatial folding: SmolVLA），baselines 加入 X-VLA 99.2%
- **§3.3**: 标题改为 "Cross-Model Pruning Protocol"，加入统一 L2 norm-based zero-out 方法描述、X-VLA/π0/OFT 各自的评测协议、两个 diagnostic metrics（attention entropy ratio, token importance CV）
- **§3.2, §3.4**: 未修改

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_paper_writing_experimental_setup_reframe_20260520T110930"
}
```

</details>

---
