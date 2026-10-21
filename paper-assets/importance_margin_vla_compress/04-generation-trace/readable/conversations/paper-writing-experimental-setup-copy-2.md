# paper writing experimental setup

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 41
- **Recorded user turns:** 0
- **Tool calls:** 20
- **Original source:** `logs/chats/worker_paper_writing_experimental_setup_20260521T120135.jsonl`
- **Structured JSON:** [`0a56184d91a9cc4fb73e.json`](../../sessions/0a/0a56184d91a9cc4fb73e.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

41 recorded events

### Tool call

_source line 1 · 2026-05-21T12:06:43.500676+00:00_

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
  "session": "worker_paper_writing_experimental_setup_20260521T120135",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/agent-ml-research/skills/global/paper-writing-norms.skill.md"
  }
}
```

</details>

---

### Tool result

_source line 2 · 2026-05-21T12:06:43.501299+00:00_

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
  "session": "worker_paper_writing_experimental_setup_20260521T120135",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-21T12:06:43.501510+00:00_

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
  "session": "worker_paper_writing_experimental_setup_20260521T120135",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/agent-ml-research/skills/global/latex-paper.skill.md"
  }
}
```

</details>

---

### Tool result

_source line 4 · 2026-05-21T12:06:43.501867+00:00_

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
  "session": "worker_paper_writing_experimental_setup_20260521T120135",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-21T12:06:43.502031+00:00_

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
  "session": "worker_paper_writing_experimental_setup_20260521T120135",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/experimental_setup.tex"
  }
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-21T12:06:43.502234+00:00_

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
…[truncated 3760 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_experimental_setup_20260521T120135",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-21T12:06:43.502408+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/results.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_experimental_setup_20260521T120135",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/results.tex"
  }
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-21T12:06:43.502632+00:00_

1	\section{Results}
2	\label{sec:results}
3	
4	We evaluate token pruning across six VLA models spanning three connector families on LIBERO-Object~\cite{liu2023libero} (10 tasks, 50 episodes each, 500 total). All success rates report Wilson 95\% confidence intervals for single-seed results and mean $\pm$ standard deviation for multi-seed results.
5	
6	\subsection{Taxonomy Overview}
7	\label{sec:taxonomy_overview}
8	
9	Table~\ref{tab:taxonomy} organizes seven models into four response classes. The taxonomy reveals that effective vision-to-LLM pipeline complexity, not the nominal connector label or model scale, determines pruning tolerance. Token importance CV tracks this ordering continuously across an 8$\times$ parameter range (450M to 7B): uniformly critical models cluster at CV $< 0.06$, threshold-graded at $\sim$0.15, smooth graded at $\sim$0.22, and catastrophic cliff at $>$0.3. A controlled comparison between $\pi_0$ and OpenVLA (both using 256 SigLIP~\cite{zhai2023siglip} tokens, differing only in connector) yields a 63\,pp gap at $k{=}0.1$, isolating the pipeline as causal (Section~\ref{sec:linear_results}).
10	
11	The four classes differ qualitatively in their failure mode. Uniformly critical models ($\pi_0$, $\pi_0.5$~\cite{black2025pi05}) distribute importance so evenly that no scoring method can identify dispensable tokens; pruning either preserves random spatial coverage (and survives) or removes a clustered patch (and fails). Threshold-graded models (X-VLA) tolerate removal up to a sharp onset point. Smooth graded models (OpenVLA, OFT, CogACT) degrade proportionally to the fraction removed. Catastrophic cliff models (SmolVLA) collapse at any removal level.
12	
13	\begin{table*}[t]
14	\centering
15	\small
16	\caption{Seven-model connector taxonomy. CV = coefficient of variation of vision token L2 norms. $^\dagger\pi_0$ reports offline normalized L1 action loss (pending closed-loop evaluation). $^\ddagger$X-VLA uses a linear projection followed by a 12-lay
…[truncated 15966 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_experimental_setup_20260521T120135",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-21T12:06:43.502883+00:00_

called Write

<details open><summary>🔧 Tool call — Write</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/experimental_setup.tex",
  "content": "\\section{Methods and Experimental Setup}\n\\label{sec:experimental_setup}\n\n\\subsection{Architectures and Benchmark}\n\\label{sec:setup_overview}\n\nSeven VLA architectures spanning three vision connector families provide the testbed for our pruning study (Figure~\\ref{fig:architecture}).\n\n\\textbf{Linear projection.} $\\pi_0$~\\cite{black2024pi0} (3.3B parameters, 256 tokens) maps SigLIP~\\cite{zhai2023siglip} patches through a linear layer into a PaliGemma backbone and generates actions via flow matching~\\cite{lipman2023flow}. $\\pi_0.5$~\\cite{black2025pi05} (4B parameters, 768 vision tokens from three cameras: left wrist, right wrist, base) applies a linear projection with $\\times\\!\\sqrt{d}$ scaling into the same PaliGemma backbone with flow matching action generation. X-VLA~\\cite{zheng2025xvla} (880M parameters, 50 tokens) augments its linear projection with a 12-layer BART encoder~\\cite{lewis2020bart}; self-attention in these layers introduces cross-token mixing that makes the effective pipeline more complex than the nominal ``linear projection'' label suggests.\n\n\\textbf{MLP projector.} OpenVLA~\\cite{kim2024openvla} (7B parameters, 256 tokens) fuses DINOv2~\\cite{oquab2023dinov2} and SigLIP encoders through a three-layer MLP (GELU activations) that maps each patch independently into a Llama-2 backbone. OFT~\\cite{kim2025openoft} shares this MLP connector with an optimized fine-tuning action head; we include OFT for attention entropy comparison only, as both metrics match OpenVLA and confirm the connector determines token importance structure. CogACT~\\cite{li2024cogact} uses an MLP projector and retains 74.2\\% SR under 78\\% pruning as reported by EfficientVLA~\\cite{yang2025efficientvla}; we cite this result as literature corroboration of the graded response pattern rather than from our own evaluation.\n\n\\textbf{Spatial folding.} SmolVLA~\\cite{shukor2025smolvla} (450M parameters, 128 tokens from two cameras) encodes each camera image with SigLIP into 1024 patches, then applies a pixel-shuffle connector that folds each $4{\\times}4$ block into one token by channel concatenation (64 per camera). Each token encodes 16 spatially contiguous patches; removing one eliminates an entire $4{\\times}4$ receptive field. The tokens enter a Qwen2-0.5B backbone~\\cite{yang2024qwen2} with flow matching action generation.\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\linewidth]{figures/paper/fig_architecture.pdf}\n\\caption{Vision connector comparison. SmolVLA's pixel-shuffle folds $4{\\times}4$ patches into single tokens (128 total, spatially entangled). OpenVLA's MLP projector maps each patch independently (256 tokens, per-token independence).}\n\\label{fig:architecture}\n\\end{figure}\n\nWe evaluate on LIBERO~\\cite{liu2023libero}, a suite of language-conditioned tabletop manipulation tasks organized into three suites: Object (10 tasks, 50 episodes each, 500 total), Spatial (10 tasks), and Goal (10 tasks). Object serves as the primary evaluation; Spatial and Goal provide cross-suite validation. Closed-loop success rate (SR) with Wilson 95\\% confidence intervals is the primary metric. Full fine-tuning baselines on Object: SmolVLA 44.8\\%, OpenVLA 74.0\\%, X-VLA 99.2\\%, $\\pi_0.5$ 98.2\\%.\n\n\\subsection{Pruning Protocol}\n\\label{sec:pruning_protocol}\n\nTwo complementary pruning methods bracket each model's robustness from above and below.\n\n\\textbf{L2 norm-based removal} (importance scoring) ranks vision tokens by their L2 norm and physically removes the lowest-norm fraction. Norm ranking preserves the most informative tokens by construction, so L2 removal provides a more favorable test of pruning tolerance.\n\n\\textbf{Random removal} (uniform selection) selects tokens uniformly at random and physically removes the unselected ones. Random removal provides a conservative lower bound because it makes no attempt to preserve high-importance tokens.\n\nModel-specific retention ratios reflect each architecture's token count and expected sensitivity. $\\pi_0$ is evaluated offline only ($k{=}0.1$, normalized L1 action loss) because its deployment environment precludes closed-loop testing. $\\pi_0.5$ uses $k \\in \\{0.3, 0.5, 0.7\\}$ under both L2 and random removal in closed-loop evaluation. X-VLA spans $k \\in \\{0.1, 0.2, 0.3, 0.5, 0.7, 0.8, 0.85, 0.9, 0.95\\}$ with L2 removal across three seeds, providing the finest-grained retention sweep in our study. OpenVLA uses $k \\in \\{0.3, 0.5, 0.7, 0.9, 0.95\\}$ with random removal as the primary protocol and L2 for direct comparison. SmolVLA tests seven configurations varying scoring (learned ACIS vs.\\ random), retention ratio ($k \\in \\{0.5, 0.7, 0.9, 0.95\\}$), and mechanism (zero-masking, true removal, token merging via ToMe~\\cite{bolya2023tome}).\n\nThe $\\pi_0$--OpenVLA pair forms a controlled natural experiment: both consume 256 SigLIP tokens from the same encoder lineage, differing only in their connector (linear projection vs.\\ three-layer MLP). Any performance gap at matched retention ratios isolates the connector as the causal factor rather than encoder capacity or token count.\n\n\\subsection{Vision Token Re-encoder (VTR)}\n\\label{sec:smart_compress_setup}\n\nA cross-attention pooling module (22.2M parameters, $\\sim$5\\% of SmolVLA) is inserted between the pixel-shuffle connector and the LLM backbone. $M$ learned queries attend over all 128 source tokens, producing $M$ compressed representations. The compression sweep covers $M \\in \\{16, 32, 64, 96, 128\\}$, where $M{=}128$ serves as a passthrough control that adds parameters without reducing tokens.\n\nA parameter-matched MLP adapter (22.14M parameters) serves as an architecture control, testing whether the benefit comes from cross-attention specifically or from re-encoding in general. Both VTR and the baseline train from the same SmolVLA-Base checkpoint for 100K steps with identical hyperparameters. An extended training control (same procedure without the compressor) achieves 45.0\\% SR, statistically indistinguishable from the 44.8\\% baseline ($p > 0.9$); any gain from VTR is therefore architectural, not from additional optimization steps. Training details appear in Appendix~\\ref{app:smart_compress_details}.\n\n\\subsection{Diagnostic Metrics}\n\\label{sec:diagnostic_metrics}\n\nTwo metrics computed from a single forward pass on task-relevant frames characterize each model's vision token structure at zero additional cost.\n\n\\textbf{Token importance CV} is the coefficient of variation of L2 norms across all vision tokens. High CV signals a heterogeneous importance distribution where some tokens carry substantially more information than others; low CV indicates near-uniform norms. CV tracks pruning tolerance continuously across the seven-model taxonomy (Section~\\ref{sec:taxonomy_overview}): uniformly critical models cluster at CV $< 0.06$, threshold-graded at $\\sim$0.15, smooth graded at $\\sim$0.22, and catastrophic cliff at $> 0.3$.\n\n\\textbf{Attention entropy ratio} is the normalized Shannon entropy of attention weights over vision tokens. Low entropy indicates concentrated attention on a few tokens, while high entropy reflects diffuse attention across the full token set. CV measures the input-side importance gradient; entropy captures how the downstream LLM allocates attention, providing a complementary view of the same structural property.\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_experimental_setup_20260521T120135",
  "tool": "Write",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/experimental_setup.tex",
    "content": "\\section{Methods and Experimental Setup}\n\\label{sec:experimental_setup}\n\n\\subsection{Architectures and Benchmark}\n\\label{sec:setup_overview}\n\nSeven VLA architectures spanning three vision connector families provide the testbed for our pruning study (Figure~\\ref{fig:architecture}).\n\n\\textbf{Linear projection.} $\\pi_0$~\\cite{black2024pi0} (3.3B parameters, 256 tokens) maps SigLIP~\\cite{zhai2023siglip} patches through a linear layer into a PaliGemma backbone and generates actions via flow matching~\\cite{lipman2023flow}. $\\pi_0.5$~\\cite{black2025pi05} (4B parameters, 768 vision tokens from three cameras: left wrist, right wrist, base) applies a linear projection with $\\times\\!\\sqrt{d}$ scaling into the same PaliGemma backbone with flow matching action generation. X-VLA~\\cite{zheng2025xvla} (880M parameters, 50 tokens) augments its linear projection with a 12-layer BART encoder~\\cite{lewis2020bart}; self-attention in these layers introduces cross-token mixing that makes the effective pipeline more complex than the nominal ``linear projection'' label suggests.\n\n\\textbf{MLP projector.} OpenVLA~\\cite{kim2024openvla} (7B parameters, 256 tokens) fuses DINOv2~\\cite{oquab2023dinov2} and SigLIP encoders through a three-layer MLP (GELU activations) that maps each patch independently into a Llama-2 backbone. OFT~\\cite{kim2025openoft} shares this MLP connector with an optimized fine-tuning action head; we include OFT for attention entropy comparison only, as both metrics match OpenVLA and confirm the connector determines token importance structure. CogACT~\\cite{li2024cogact} uses an MLP projector and retains 74.2\\% SR under 78\\% pruning as reported by EfficientVLA~\\cite{yang2025efficientvla}; we cite this result as literature corroboration of the graded response pattern rather than from our own evaluation.\n\n\\textbf{Spatial folding.} SmolVLA~\\cite{shukor2025smolvla} (450M parameters, 128 tokens from two cameras) encodes each camera image with SigLIP into 1024 patches, then applies a pixel-shuffle connector that folds each $4{\\times}4$ block into one token by channel concatenation (64 per camera). Each token encodes 16 spatially contiguous patches; removing one eliminates an entire $4{\\times}4$ receptive field. The tokens enter a Qwen2-0.5B backbone~\\cite{yang2024qwen2} with flow matching action generation.\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\linewidth]{figures/paper/fig_architecture.pdf}\n\\caption{Vision connector comparison. SmolVLA's pixel-shuffle folds $4{\\times}4$ patches into single tokens (128 total, spatially entangled). OpenVLA's MLP projector maps each patch independently (256 tokens, per-token independence).}\n\\label{fig:architecture}\n\\end{figure}\n\nWe evaluate on LIBERO~\\cite{liu2023libero}, a suite of language-conditioned tabletop manipulation tasks organized into three suites: Object (10 tasks, 50 episodes each, 500 total), Spatial (10 tasks), and Goal (10 tasks). Object serves as the primary evaluation; Spatial and Goal provide cross-suite validation. Closed-loop success rate (SR) with Wilson 95\\% confidence intervals is the primary metric. Full fine-tuning baselines on Object: SmolVLA 44.8\\%, OpenVLA 74.0\\%, X-VLA 99.2\\%, $\\pi_0.5$ 98.2\\%.\n\n\\subsection{Pruning Protocol}\n\\label{sec:pruning_protocol}\n\nTwo complementary pruning methods bracket each model's robustness from above and below.\n\n\\textbf{L2 norm-based removal} (importance scoring) ranks vision tokens by their L2 norm and physically removes the lowest-norm fraction. Norm ranking preserves the most informative tokens by construction, so L2 removal provides a more favorable test of pruning tolerance.\n\n\\textbf{Random removal} (uniform selection) selects tokens uniformly at random and physically removes the unselected ones. Random removal provides a conservative lower bound because it makes no attempt to preserve high-importance tokens.\n\nModel-specific retention ratios reflect each architecture's token count and expected sensitivity. $\\pi_0$ is evaluated offline only ($k{=}0.1$, normalized L1 action loss) because its deployment environment precludes closed-loop testing. $\\pi_0.5$ uses $k \\in \\{0.3, 0.5, 0.7\\}$ under both L2 and random removal in closed-loop evaluation. X-VLA spans $k \\in \\{0.1, 0.2, 0.3, 0.5, 0.7, 0.8, 0.85, 0.9, 0.95\\}$ with L2 removal across three seeds, providing the finest-grained retention sweep in our study. OpenVLA uses $k \\in \\{0.3, 0.5, 0.7, 0.9, 0.95\\}$ with random removal as the primary protocol and L2 for direct comparison. SmolVLA tests seven configurations varying scoring (learned ACIS vs.\\ random), retention ratio ($k \\in \\{0.5, 0.7, 0.9, 0.95\\}$), and mechanism (zero-masking, true removal, token merging via ToMe~\\cite{bolya2023tome}).\n\nThe $\\pi_0$--OpenVLA pair forms a controlled natural experiment: both consume 256 SigLIP tokens from the same encoder lineage, differing only in their connector (linear projection vs.\\ three-layer MLP). Any performance gap at matched retention ratios isolates the connector as the causal factor rather than encoder capacity or token count.\n\n\\subsection{Vision Token Re-encoder (VTR)}\n\\label{sec:smart_compress_setup}\n\nA cross-attention pooling module (22.2M parameters, $\\sim$5\\% of SmolVLA) is inserted between the pixel-shuffle connector and the LLM backbone. $M$ learned queries attend over all 128 source tokens, producing $M$ compressed representations. The compression sweep covers $M \\in \\{16, 32, 64, 96, 128\\}$, where $M{=}128$ serves as a passthrough control that adds parameters without reducing tokens.\n\nA parameter-matched MLP adapter (22.14M parameters) serves as an architecture control, testing whether the benefit comes from cross-attention specifically or from re-encoding in general. Both VTR and the baseline train from the same SmolVLA-Base checkpoint for 100K steps with identical hyperparameters. An extended training control (same procedure without the compressor) achieves 45.0\\% SR, statistically indistinguishable from the 44.8\\% baseline ($p > 0.9$); any gain from VTR is therefore architectural, not from additional optimization steps. Training details appear in Appendix~\\ref{app:smart_compress_details}.\n\n\\subsection{Diagnostic Metrics}\n\\label{sec:diagnostic_metrics}\n\nTwo metrics computed from a single forward pass on task-relevant frames characterize each model's vision token structure at zero additional cost.\n\n\\textbf{Token importance CV} is the coefficient of variation of L2 norms across all vision tokens. High CV signals a heterogeneous importance distribution where some tokens carry substantially more information than others; low CV indicates near-uniform norms. CV tracks pruning tolerance continuously across the seven-model taxonomy (Section~\\ref{sec:taxonomy_overview}): uniformly critical models cluster at CV $< 0.06$, threshold-graded at $\\sim$0.15, smooth graded at $\\sim$0.22, and catastrophic cliff at $> 0.3$.\n\n\\textbf{Attention entropy ratio} is the normalized Shannon entropy of attention weights over vision tokens. Low entropy indicates concentrated attention on a few tokens, while high entropy reflects diffuse attention across the full token set. CV measures the input-side importance gradient; entropy captures how the downstream LLM allocates attention, providing a complementary view of the same structural property.\n"
  }
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-21T12:06:43.503237+00:00_

The file /home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/experimental_setup.tex has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_experimental_setup_20260521T120135",
  "tool": "Write",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-21T12:06:43.503419+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "wc -w /home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/experimental_setup.tex",
  "description": "Count words in the new file"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_experimental_setup_20260521T120135",
  "tool": "Bash",
  "tool_args": {
    "command": "wc -w /home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/experimental_setup.tex",
    "description": "Count words in the new file"
  }
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-21T12:06:43.503551+00:00_

911 /home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/experimental_setup.tex

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_experimental_setup_20260521T120135",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-21T12:06:43.503711+00:00_

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
  "session": "worker_paper_writing_experimental_setup_20260521T120135",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/experimental_setup.tex"
  }
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-21T12:06:43.503875+00:00_

1	\section{Methods and Experimental Setup}
2	\label{sec:experimental_setup}
3	
4	\subsection{Architectures and Benchmark}
5	\label{sec:setup_overview}
6	
7	Seven VLA architectures spanning three vision connector families provide the testbed for our pruning study (Figure~\ref{fig:architecture}).
8	
9	\textbf{Linear projection.} $\pi_0$~\cite{black2024pi0} (3.3B parameters, 256 tokens) maps SigLIP~\cite{zhai2023siglip} patches through a linear layer into a PaliGemma backbone and generates actions via flow matching~\cite{lipman2023flow}. $\pi_0.5$~\cite{black2025pi05} (4B parameters, 768 vision tokens from three cameras: left wrist, right wrist, base) applies a linear projection with $\times\!\sqrt{d}$ scaling into the same PaliGemma backbone with flow matching action generation. X-VLA~\cite{zheng2025xvla} (880M parameters, 50 tokens) augments its linear projection with a 12-layer BART encoder~\cite{lewis2020bart}; self-attention in these layers introduces cross-token mixing that makes the effective pipeline more complex than the nominal ``linear projection'' label suggests.
10	
11	\textbf{MLP projector.} OpenVLA~\cite{kim2024openvla} (7B parameters, 256 tokens) fuses DINOv2~\cite{oquab2023dinov2} and SigLIP encoders through a three-layer MLP (GELU activations) that maps each patch independently into a Llama-2 backbone. OFT~\cite{kim2025openoft} shares this MLP connector with an optimized fine-tuning action head; we include OFT for attention entropy comparison only, as both metrics match OpenVLA and confirm the connector determines token importance structure. CogACT~\cite{li2024cogact} uses an MLP projector and retains 74.2\% SR under 78\% pruning as reported by EfficientVLA~\cite{yang2025efficientvla}; we cite this result as literature corroboration of the graded response pattern rather than from our own evaluation.
12	
13	\textbf{Spatial folding.} SmolVLA~\cite{shukor2025smolvla} (450M parameters, 128 tokens from two cameras) encodes each camera image with SigLIP int
…[truncated 5450 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_experimental_setup_20260521T120135",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-21T12:06:43.504061+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/experimental_setup.tex",
  "old_string": "\\textbf{Linear projection.} $\\pi_0$~\\cite{black2024pi0} (3.3B parameters, 256 tokens) maps SigLIP~\\cite{zhai2023siglip} patches through a linear layer into a PaliGemma backbone and generates actions via flow matching~\\cite{lipman2023flow}. $\\pi_0.5$~\\cite{black2025pi05} (4B parameters, 768 vision tokens from three cameras: left wrist, right wrist, base) applies a linear projection with $\\times\\!\\sqrt{d}$ scaling into the same PaliGemma backbone with flow matching action generation. X-VLA~\\cite{zheng2025xvla} (880M parameters, 50 tokens) augments its linear projection with a 12-layer BART encoder~\\cite{lewis2020bart}; self-attention in these layers introduces cross-token mixing that makes the effective pipeline more complex than the nominal ``linear projection'' label suggests.",
  "new_string": "\\textbf{Linear projection.} $\\pi_0$~\\cite{black2024pi0} (3.3B parameters, 256 tokens) maps SigLIP~\\cite{zhai2023siglip} patches through a single linear layer into a PaliGemma backbone and generates actions via flow matching~\\cite{lipman2023flow}. $\\pi_0.5$~\\cite{black2025pi05} (4B parameters, 768 vision tokens from three cameras: left wrist, right wrist, base) applies a linear projection with learned $\\times\\!\\sqrt{d}$ scaling into the same PaliGemma backbone with flow matching action generation; the larger token count arises from processing three camera views rather than one. X-VLA~\\cite{zheng2025xvla} (880M parameters, 50 tokens) augments its linear projection with a 12-layer BART encoder~\\cite{lewis2020bart}; self-attention in these layers introduces cross-token mixing that makes the effective pipeline more complex than the nominal ``linear projection'' label suggests. All three models share the linear projection label, yet their post-projection processing spans a spectrum from no additional computation ($\\pi_0$) to a full transformer encoder (X-VLA)."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_experimental_setup_20260521T120135",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/experimental_setup.tex",
    "old_string": "\\textbf{Linear projection.} $\\pi_0$~\\cite{black2024pi0} (3.3B parameters, 256 tokens) maps SigLIP~\\cite{zhai2023siglip} patches through a linear layer into a PaliGemma backbone and generates actions via flow matching~\\cite{lipman2023flow}. $\\pi_0.5$~\\cite{black2025pi05} (4B parameters, 768 vision tokens from three cameras: left wrist, right wrist, base) applies a linear projection with $\\times\\!\\sqrt{d}$ scaling into the same PaliGemma backbone with flow matching action generation. X-VLA~\\cite{zheng2025xvla} (880M parameters, 50 tokens) augments its linear projection with a 12-layer BART encoder~\\cite{lewis2020bart}; self-attention in these layers introduces cross-token mixing that makes the effective pipeline more complex than the nominal ``linear projection'' label suggests.",
    "new_string": "\\textbf{Linear projection.} $\\pi_0$~\\cite{black2024pi0} (3.3B parameters, 256 tokens) maps SigLIP~\\cite{zhai2023siglip} patches through a single linear layer into a PaliGemma backbone and generates actions via flow matching~\\cite{lipman2023flow}. $\\pi_0.5$~\\cite{black2025pi05} (4B parameters, 768 vision tokens from three cameras: left wrist, right wrist, base) applies a linear projection with learned $\\times\\!\\sqrt{d}$ scaling into the same PaliGemma backbone with flow matching action generation; the larger token count arises from processing three camera views rather than one. X-VLA~\\cite{zheng2025xvla} (880M parameters, 50 tokens) augments its linear projection with a 12-layer BART encoder~\\cite{lewis2020bart}; self-attention in these layers introduces cross-token mixing that makes the effective pipeline more complex than the nominal ``linear projection'' label suggests. All three models share the linear projection label, yet their post-projection processing spans a spectrum from no additional computation ($\\pi_0$) to a full transformer encoder (X-VLA)."
  }
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-21T12:06:43.504305+00:00_

The file /home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/experimental_setup.tex has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_experimental_setup_20260521T120135",
  "tool": "Edit",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-21T12:06:43.504447+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/experimental_setup.tex",
  "old_string": "We evaluate on LIBERO~\\cite{liu2023libero}, a suite of language-conditioned tabletop manipulation tasks organized into three suites: Object (10 tasks, 50 episodes each, 500 total), Spatial (10 tasks), and Goal (10 tasks). Object serves as the primary evaluation; Spatial and Goal provide cross-suite validation. Closed-loop success rate (SR) with Wilson 95\\% confidence intervals is the primary metric. Full fine-tuning baselines on Object: SmolVLA 44.8\\%, OpenVLA 74.0\\%, X-VLA 99.2\\%, $\\pi_0.5$ 98.2\\%.",
  "new_string": "We evaluate on LIBERO~\\cite{liu2023libero}, a suite of language-conditioned tabletop manipulation tasks organized into three suites that test complementary skills: Object (10 tasks requiring correct object identification), Spatial (10 tasks requiring spatial reasoning about relative positions), and Goal (10 tasks requiring goal-state recognition). Each task uses 50 evaluation episodes (500 total per suite). Object serves as the primary evaluation; Spatial and Goal provide cross-suite validation of findings. Closed-loop success rate (SR) with Wilson 95\\% confidence intervals is the primary metric for single-seed results; multi-seed evaluations report mean $\\pm$ standard deviation. Full fine-tuning baselines on Object: SmolVLA 44.8\\%, OpenVLA 74.0\\%, X-VLA 99.2\\%, $\\pi_0.5$ 98.2\\%."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_experimental_setup_20260521T120135",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/experimental_setup.tex",
    "old_string": "We evaluate on LIBERO~\\cite{liu2023libero}, a suite of language-conditioned tabletop manipulation tasks organized into three suites: Object (10 tasks, 50 episodes each, 500 total), Spatial (10 tasks), and Goal (10 tasks). Object serves as the primary evaluation; Spatial and Goal provide cross-suite validation. Closed-loop success rate (SR) with Wilson 95\\% confidence intervals is the primary metric. Full fine-tuning baselines on Object: SmolVLA 44.8\\%, OpenVLA 74.0\\%, X-VLA 99.2\\%, $\\pi_0.5$ 98.2\\%.",
    "new_string": "We evaluate on LIBERO~\\cite{liu2023libero}, a suite of language-conditioned tabletop manipulation tasks organized into three suites that test complementary skills: Object (10 tasks requiring correct object identification), Spatial (10 tasks requiring spatial reasoning about relative positions), and Goal (10 tasks requiring goal-state recognition). Each task uses 50 evaluation episodes (500 total per suite). Object serves as the primary evaluation; Spatial and Goal provide cross-suite validation of findings. Closed-loop success rate (SR) with Wilson 95\\% confidence intervals is the primary metric for single-seed results; multi-seed evaluations report mean $\\pm$ standard deviation. Full fine-tuning baselines on Object: SmolVLA 44.8\\%, OpenVLA 74.0\\%, X-VLA 99.2\\%, $\\pi_0.5$ 98.2\\%."
  }
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-21T12:06:43.504669+00:00_

The file /home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/experimental_setup.tex has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_experimental_setup_20260521T120135",
  "tool": "Edit",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-21T12:06:43.504819+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/experimental_setup.tex",
  "old_string": "Two complementary pruning methods bracket each model's robustness from above and below.\n\n\\textbf{L2 norm-based removal} (importance scoring) ranks vision tokens by their L2 norm and physically removes the lowest-norm fraction. Norm ranking preserves the most informative tokens by construction, so L2 removal provides a more favorable test of pruning tolerance.\n\n\\textbf{Random removal} (uniform selection) selects tokens uniformly at random and physically removes the unselected ones. Random removal provides a conservative lower bound because it makes no attempt to preserve high-importance tokens.\n\nModel-specific retention ratios reflect each architecture's token count and expected sensitivity. $\\pi_0$ is evaluated offline only ($k{=}0.1$, normalized L1 action loss) because its deployment environment precludes closed-loop testing. $\\pi_0.5$ uses $k \\in \\{0.3, 0.5, 0.7\\}$ under both L2 and random removal in closed-loop evaluation. X-VLA spans $k \\in \\{0.1, 0.2, 0.3, 0.5, 0.7, 0.8, 0.85, 0.9, 0.95\\}$ with L2 removal across three seeds, providing the finest-grained retention sweep in our study. OpenVLA uses $k \\in \\{0.3, 0.5, 0.7, 0.9, 0.95\\}$ with random removal as the primary protocol and L2 for direct comparison. SmolVLA tests seven configurations varying scoring (learned ACIS vs.\\ random), retention ratio ($k \\in \\{0.5, 0.7, 0.9, 0.95\\}$), and mechanism (zero-masking, true removal, token merging via ToMe~\\cite{bolya2023tome}).\n\nThe $\\pi_0$--OpenVLA pair forms a controlled natural experiment: both consume 256 SigLIP tokens from the same encoder lineage, differing only in their connector (linear projection vs.\\ three-layer MLP). Any performance gap at matched retention ratios isolates the connector as the causal factor rather than encoder capacity or token count.",
  "new_string": "Two complementary pruning methods bracket each model's robustness from above and below. Both methods physically remove unselected tokens from the sequence (reducing the actual input length to the LLM), rather than zeroing them out; the distinction matters because zero-masking preserves positional structure while physical removal does not.\n\n\\textbf{L2 norm-based removal} (importance scoring) ranks vision tokens by their L2 norm and physically removes the lowest-norm fraction. Norm ranking preserves the most informative tokens by construction, so L2 removal provides a more favorable test of pruning tolerance. The underlying assumption is that higher-norm tokens carry more task-relevant information; Section~\\ref{sec:scaling_law} examines when this assumption holds and when it fails.\n\n\\textbf{Random removal} (uniform selection) selects tokens uniformly at random and physically removes the unselected ones. Random removal provides a conservative lower bound because it makes no attempt to preserve high-importance tokens. For models with near-uniform token norms, however, random selection can outperform L2 by preserving spatial coverage rather than clustering on correlated patches.\n\nModel-specific retention ratios reflect each architecture's token count and expected sensitivity. $\\pi_0$ is evaluated offline only ($k{=}0.1$, normalized L1 action loss) because its deployment environment precludes closed-loop testing. $\\pi_0.5$ uses $k \\in \\{0.3, 0.5, 0.7\\}$ under both L2 and random removal in closed-loop evaluation, enabling direct method comparison within a single architecture. X-VLA spans $k \\in \\{0.1, 0.2, 0.3, 0.5, 0.7, 0.8, 0.85, 0.9, 0.95\\}$ with L2 removal across three seeds, providing the finest-grained retention sweep in our study and sufficient resolution to locate sharp onset thresholds. OpenVLA uses $k \\in \\{0.3, 0.5, 0.7, 0.9, 0.95\\}$ with random removal as the primary protocol and L2 for direct comparison. SmolVLA tests seven configurations varying scoring (learned ACIS vs.\\ random), retention ratio ($k \\in \\{0.5, 0.7, 0.9, 0.95\\}$), and mechanism (zero-masking, true removal, token merging via ToMe~\\cite{bolya2023tome}).\n\nThe $\\pi_0$--OpenVLA pair forms a controlled natural experiment: both consume 256 SigLIP tokens from the same encoder lineage, differing only in their connector (linear projection vs.\\ three-layer MLP). Any performance gap at matched retention ratios isolates the connector as the causal factor rather than encoder capacity or token count. Comparing OpenVLA (random removal, harder test) against X-VLA (L2 removal, easier test) further strengthens architecture-dependent conclusions, because any observed fragility in X-VLA cannot be attributed to an unfavorable scoring method."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_experimental_setup_20260521T120135",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/experimental_setup.tex",
    "old_string": "Two complementary pruning methods bracket each model's robustness from above and below.\n\n\\textbf{L2 norm-based removal} (importance scoring) ranks vision tokens by their L2 norm and physically removes the lowest-norm fraction. Norm ranking preserves the most informative tokens by construction, so L2 removal provides a more favorable test of pruning tolerance.\n\n\\textbf{Random removal} (uniform selection) selects tokens uniformly at random and physically removes the unselected ones. Random removal provides a conservative lower bound because it makes no attempt to preserve high-importance tokens.\n\nModel-specific retention ratios reflect each architecture's token count and expected sensitivity. $\\pi_0$ is evaluated offline only ($k{=}0.1$, normalized L1 action loss) because its deployment environment precludes closed-loop testing. $\\pi_0.5$ uses $k \\in \\{0.3, 0.5, 0.7\\}$ under both L2 and random removal in closed-loop evaluation. X-VLA spans $k \\in \\{0.1, 0.2, 0.3, 0.5, 0.7, 0.8, 0.85, 0.9, 0.95\\}$ with L2 removal across three seeds, providing the finest-grained retention sweep in our study. OpenVLA uses $k \\in \\{0.3, 0.5, 0.7, 0.9, 0.95\\}$ with random removal as the primary protocol and L2 for direct comparison. SmolVLA tests seven configurations varying scoring (learned ACIS vs.\\ random), retention ratio ($k \\in \\{0.5, 0.7, 0.9, 0.95\\}$), and mechanism (zero-masking, true removal, token merging via ToMe~\\cite{bolya2023tome}).\n\nThe $\\pi_0$--OpenVLA pair forms a controlled natural experiment: both consume 256 SigLIP tokens from the same encoder lineage, differing only in their connector (linear projection vs.\\ three-layer MLP). Any performance gap at matched retention ratios isolates the connector as the causal factor rather than encoder capacity or token count.",
    "new_string": "Two complementary pruning methods bracket each model's robustness from above and below. Both methods physically remove unselected tokens from the sequence (reducing the actual input length to the LLM), rather than zeroing them out; the distinction matters because zero-masking preserves positional structure while physical removal does not.\n\n\\textbf{L2 norm-based removal} (importance scoring) ranks vision tokens by their L2 norm and physically removes the lowest-norm fraction. Norm ranking preserves the most informative tokens by construction, so L2 removal provides a more favorable test of pruning tolerance. The underlying assumption is that higher-norm tokens carry more task-relevant information; Section~\\ref{sec:scaling_law} examines when this assumption holds and when it fails.\n\n\\textbf{Random removal} (uniform selection) selects tokens uniformly at random and physically removes the unselected ones. Random removal provides a conservative lower bound because it makes no attempt to preserve high-importance tokens. For models with near-uniform token norms, however, random selection can outperform L2 by preserving spatial coverage rather than clustering on correlated patches.\n\nModel-specific retention ratios reflect each architecture's token count and expected sensitivity. $\\pi_0$ is evaluated offline only ($k{=}0.1$, normalized L1 action loss) because its deployment environment precludes closed-loop testing. $\\pi_0.5$ uses $k \\in \\{0.3, 0.5, 0.7\\}$ under both L2 and random removal in closed-loop evaluation, enabling direct method comparison within a single architecture. X-VLA spans $k \\in \\{0.1, 0.2, 0.3, 0.5, 0.7, 0.8, 0.85, 0.9, 0.95\\}$ with L2 removal across three seeds, providing the finest-grained retention sweep in our study and sufficient resolution to locate sharp onset thresholds. OpenVLA uses $k \\in \\{0.3, 0.5, 0.7, 0.9, 0.95\\}$ with random removal as the primary protocol and L2 for direct comparison. SmolVLA tests seven configurations varying scoring (learned ACIS vs.\\ random), retention ratio ($k \\in \\{0.5, 0.7, 0.9, 0.95\\}$), and mechanism (zero-masking, true removal, token merging via ToMe~\\cite{bolya2023tome}).\n\nThe $\\pi_0$--OpenVLA pair forms a controlled natural experiment: both consume 256 SigLIP tokens from the same encoder lineage, differing only in their connector (linear projection vs.\\ three-layer MLP). Any performance gap at matched retention ratios isolates the connector as the causal factor rather than encoder capacity or token count. Comparing OpenVLA (random removal, harder test) against X-VLA (L2 removal, easier test) further strengthens architecture-dependent conclusions, because any observed fragility in X-VLA cannot be attributed to an unfavorable scoring method."
  }
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-21T12:06:43.505028+00:00_

The file /home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/experimental_setup.tex has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_experimental_setup_20260521T120135",
  "tool": "Edit",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 21 · 2026-05-21T12:06:43.505196+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/experimental_setup.tex",
  "old_string": "A cross-attention pooling module (22.2M parameters, $\\sim$5\\% of SmolVLA) is inserted between the pixel-shuffle connector and the LLM backbone. $M$ learned queries attend over all 128 source tokens, producing $M$ compressed representations. The compression sweep covers $M \\in \\{16, 32, 64, 96, 128\\}$, where $M{=}128$ serves as a passthrough control that adds parameters without reducing tokens.\n\nA parameter-matched MLP adapter (22.14M parameters) serves as an architecture control, testing whether the benefit comes from cross-attention specifically or from re-encoding in general. Both VTR and the baseline train from the same SmolVLA-Base checkpoint for 100K steps with identical hyperparameters. An extended training control (same procedure without the compressor) achieves 45.0\\% SR, statistically indistinguishable from the 44.8\\% baseline ($p > 0.9$); any gain from VTR is therefore architectural, not from additional optimization steps. Training details appear in Appendix~\\ref{app:smart_compress_details}.",
  "new_string": "A cross-attention pooling module (22.2M parameters, $\\sim$5\\% of SmolVLA) is inserted between the pixel-shuffle connector and the LLM backbone. $M$ learned queries attend over all 128 source tokens via standard scaled dot-product attention, producing $M$ compressed representations that replace the original 128 tokens as input to the LLM. The compression sweep covers $M \\in \\{16, 32, 64, 96, 128\\}$; $M{=}16$ represents 87.5\\% token reduction while $M{=}128$ serves as a passthrough control that adds parameters without reducing tokens.\n\nA parameter-matched MLP adapter (22.14M parameters) serves as an architecture control, testing whether the benefit comes from cross-attention specifically or from re-encoding in general. Both VTR and the baseline train from the same SmolVLA-Base checkpoint for 100K steps with identical hyperparameters. An extended training control (same procedure without the compressor) achieves 45.0\\% SR, statistically indistinguishable from the 44.8\\% baseline ($p > 0.9$); any gain from VTR is therefore architectural, not from additional optimization steps. VTR results are evaluated with three seeds per configuration to ensure reproducibility. Training details appear in Appendix~\\ref{app:smart_compress_details}."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_experimental_setup_20260521T120135",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/experimental_setup.tex",
    "old_string": "A cross-attention pooling module (22.2M parameters, $\\sim$5\\% of SmolVLA) is inserted between the pixel-shuffle connector and the LLM backbone. $M$ learned queries attend over all 128 source tokens, producing $M$ compressed representations. The compression sweep covers $M \\in \\{16, 32, 64, 96, 128\\}$, where $M{=}128$ serves as a passthrough control that adds parameters without reducing tokens.\n\nA parameter-matched MLP adapter (22.14M parameters) serves as an architecture control, testing whether the benefit comes from cross-attention specifically or from re-encoding in general. Both VTR and the baseline train from the same SmolVLA-Base checkpoint for 100K steps with identical hyperparameters. An extended training control (same procedure without the compressor) achieves 45.0\\% SR, statistically indistinguishable from the 44.8\\% baseline ($p > 0.9$); any gain from VTR is therefore architectural, not from additional optimization steps. Training details appear in Appendix~\\ref{app:smart_compress_details}.",
    "new_string": "A cross-attention pooling module (22.2M parameters, $\\sim$5\\% of SmolVLA) is inserted between the pixel-shuffle connector and the LLM backbone. $M$ learned queries attend over all 128 source tokens via standard scaled dot-product attention, producing $M$ compressed representations that replace the original 128 tokens as input to the LLM. The compression sweep covers $M \\in \\{16, 32, 64, 96, 128\\}$; $M{=}16$ represents 87.5\\% token reduction while $M{=}128$ serves as a passthrough control that adds parameters without reducing tokens.\n\nA parameter-matched MLP adapter (22.14M parameters) serves as an architecture control, testing whether the benefit comes from cross-attention specifically or from re-encoding in general. Both VTR and the baseline train from the same SmolVLA-Base checkpoint for 100K steps with identical hyperparameters. An extended training control (same procedure without the compressor) achieves 45.0\\% SR, statistically indistinguishable from the 44.8\\% baseline ($p > 0.9$); any gain from VTR is therefore architectural, not from additional optimization steps. VTR results are evaluated with three seeds per configuration to ensure reproducibility. Training details appear in Appendix~\\ref{app:smart_compress_details}."
  }
}
```

</details>

---

### Tool result

_source line 22 · 2026-05-21T12:06:43.505418+00:00_

The file /home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/experimental_setup.tex has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_experimental_setup_20260521T120135",
  "tool": "Edit",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 23 · 2026-05-21T12:06:43.505550+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "wc -w /home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/experimental_setup.tex",
  "description": "Count words in updated file"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_experimental_setup_20260521T120135",
  "tool": "Bash",
  "tool_args": {
    "command": "wc -w /home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/experimental_setup.tex",
    "description": "Count words in updated file"
  }
}
```

</details>

---

### Tool result

_source line 24 · 2026-05-21T12:06:43.505671+00:00_

1143 /home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/experimental_setup.tex

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_experimental_setup_20260521T120135",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 25 · 2026-05-21T12:06:43.505815+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/experimental_setup.tex",
  "old_string": "\\textbf{Attention entropy ratio} is the normalized Shannon entropy of attention weights over vision tokens. Low entropy indicates concentrated attention on a few tokens, while high entropy reflects diffuse attention across the full token set. CV measures the input-side importance gradient; entropy captures how the downstream LLM allocates attention, providing a complementary view of the same structural property.",
  "new_string": "\\textbf{Attention entropy ratio} is the normalized Shannon entropy of attention weights over vision tokens, computed from the final LLM layer's cross-attention distribution. Low entropy indicates concentrated attention on a few tokens, while high entropy reflects diffuse attention across the full token set. CV measures the input-side importance gradient; entropy captures how the downstream LLM allocates attention, providing a complementary view of the same structural property. OFT and OpenVLA share nearly identical entropy values (0.667 vs.\\ 0.661), confirming that the connector, not the action head, determines token utilization patterns. Section~\\ref{sec:scaling_law} demonstrates that CV also predicts the optimal pruning strategy: low-CV models require coverage-preserving methods (random selection), while higher-CV models can benefit from importance-based scoring."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_experimental_setup_20260521T120135",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/experimental_setup.tex",
    "old_string": "\\textbf{Attention entropy ratio} is the normalized Shannon entropy of attention weights over vision tokens. Low entropy indicates concentrated attention on a few tokens, while high entropy reflects diffuse attention across the full token set. CV measures the input-side importance gradient; entropy captures how the downstream LLM allocates attention, providing a complementary view of the same structural property.",
    "new_string": "\\textbf{Attention entropy ratio} is the normalized Shannon entropy of attention weights over vision tokens, computed from the final LLM layer's cross-attention distribution. Low entropy indicates concentrated attention on a few tokens, while high entropy reflects diffuse attention across the full token set. CV measures the input-side importance gradient; entropy captures how the downstream LLM allocates attention, providing a complementary view of the same structural property. OFT and OpenVLA share nearly identical entropy values (0.667 vs.\\ 0.661), confirming that the connector, not the action head, determines token utilization patterns. Section~\\ref{sec:scaling_law} demonstrates that CV also predicts the optimal pruning strategy: low-CV models require coverage-preserving methods (random selection), while higher-CV models can benefit from importance-based scoring."
  }
}
```

</details>

---

### Tool result

_source line 26 · 2026-05-21T12:06:43.505976+00:00_

The file /home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/experimental_setup.tex has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_experimental_setup_20260521T120135",
  "tool": "Edit",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 27 · 2026-05-21T12:06:43.506098+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "wc -w /home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/experimental_setup.tex",
  "description": "Final word count"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_experimental_setup_20260521T120135",
  "tool": "Bash",
  "tool_args": {
    "command": "wc -w /home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/experimental_setup.tex",
    "description": "Final word count"
  }
}
```

</details>

---

### Tool result

_source line 28 · 2026-05-21T12:06:43.506269+00:00_

1199 /home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/experimental_setup.tex

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_experimental_setup_20260521T120135",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 29 · 2026-05-21T12:06:43.506418+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "echo \"=== Em-dash check ===\" && grep -n \"—\" /home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/experimental_setup.tex || echo \"PASS: no em-dash\" && echo \"=== En-dash check ===\" && grep -n \" – \" /home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/experimental_setup.tex || echo \"PASS: no explanatory en-dash\" && echo \"=== -ing ending check ===\" && grep -n \"ing\\.$\\|ing,$\" /home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/experimental_setup.tex || echo \"PASS\" && echo \"=== Notably/Importantly/Interestingly ===\" && grep -ni \"Importantly\\|Notably\\|Interestingly\" /home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/experimental_setup.tex || echo \"PASS\" && echo \"=== Paragraph starting with This/These/It ===\" && grep -n \"^\\\\\\\\\\\\|^This \\|^These \\|^It \" /home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/experimental_setup.tex | grep -v \"^.*\\\\\\\\[a-z]\" || echo \"PASS\"",
  "description": "Style compliance checks for paper norms"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_experimental_setup_20260521T120135",
  "tool": "Bash",
  "tool_args": {
    "command": "echo \"=== Em-dash check ===\" && grep -n \"—\" /home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/experimental_setup.tex || echo \"PASS: no em-dash\" && echo \"=== En-dash check ===\" && grep -n \" – \" /home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/experimental_setup.tex || echo \"PASS: no explanatory en-dash\" && echo \"=== -ing ending check ===\" && grep -n \"ing\\.$\\|ing,$\" /home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/experimental_setup.tex || echo \"PASS\" && echo \"=== Notably/Importantly/Interestingly ===\" && grep -ni \"Importantly\\|Notably\\|Interestingly\" /home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/experimental_setup.tex || echo \"PASS\" && echo \"=== Paragraph starting with This/These/It ===\" && grep -n \"^\\\\\\\\\\\\|^This \\|^These \\|^It \" /home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/experimental_setup.tex | grep -v \"^.*\\\\\\\\[a-z]\" || echo \"PASS\"",
    "description": "Style compliance checks for paper norms"
  }
}
```

</details>

---

### Tool result

_source line 30 · 2026-05-21T12:06:43.506563+00:00_

=== Em-dash check ===
PASS: no em-dash
=== En-dash check ===
PASS: no explanatory en-dash
=== -ing ending check ===
51:\textbf{Attention entropy ratio} is the normalized Shannon entropy of attention weights over vision tokens, computed from the final LLM layer's cross-attention distribution. Low entropy indicates concentrated attention on a few tokens, while high entropy reflects diffuse attention across the full token set. CV measures the input-side importance gradient; entropy captures how the downstream LLM allocates attention, providing a complementary view of the same structural property. OFT and OpenVLA share nearly identical entropy values (0.667 vs.\ 0.661), confirming that the connector, not the action head, determines token utilization patterns. Section~\ref{sec:scaling_law} demonstrates that CV also predicts the optimal pruning strategy: low-CV models require coverage-preserving methods (random selection), while higher-CV models can benefit from importance-based scoring.
=== Notably/Importantly/Interestingly ===
PASS
=== Paragraph starting with This/These/It ===
PASS

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_experimental_setup_20260521T120135",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 31 · 2026-05-21T12:06:43.506727+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "grep -n \"ing\\. \\|ing\\.\\$\\|ing,\\|ing;\" /home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/experimental_setup.tex",
  "description": "Find all -ing phrase patterns"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_experimental_setup_20260521T120135",
  "tool": "Bash",
  "tool_args": {
    "command": "grep -n \"ing\\. \\|ing\\.\\$\\|ing,\\|ing;\" /home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/experimental_setup.tex",
    "description": "Find all -ing phrase patterns"
  }
}
```

</details>

---

### Tool result

_source line 32 · 2026-05-21T12:06:43.506857+00:00_

33:Model-specific retention ratios reflect each architecture's token count and expected sensitivity. $\pi_0$ is evaluated offline only ($k{=}0.1$, normalized L1 action loss) because its deployment environment precludes closed-loop testing. $\pi_0.5$ uses $k \in \{0.3, 0.5, 0.7\}$ under both L2 and random removal in closed-loop evaluation, enabling direct method comparison within a single architecture. X-VLA spans $k \in \{0.1, 0.2, 0.3, 0.5, 0.7, 0.8, 0.85, 0.9, 0.95\}$ with L2 removal across three seeds, providing the finest-grained retention sweep in our study and sufficient resolution to locate sharp onset thresholds. OpenVLA uses $k \in \{0.3, 0.5, 0.7, 0.9, 0.95\}$ with random removal as the primary protocol and L2 for direct comparison. SmolVLA tests seven configurations varying scoring (learned ACIS vs.\ random), retention ratio ($k \in \{0.5, 0.7, 0.9, 0.95\}$), and mechanism (zero-masking, true removal, token merging via ToMe~\cite{bolya2023tome}).
51:\textbf{Attention entropy ratio} is the normalized Shannon entropy of attention weights over vision tokens, computed from the final LLM layer's cross-attention distribution. Low entropy indicates concentrated attention on a few tokens, while high entropy reflects diffuse attention across the full token set. CV measures the input-side importance gradient; entropy captures how the downstream LLM allocates attention, providing a complementary view of the same structural property. OFT and OpenVLA share nearly identical entropy values (0.667 vs.\ 0.661), confirming that the connector, not the action head, determines token utilization patterns. Section~\ref{sec:scaling_law} demonstrates that CV also predicts the optimal pruning strategy: low-CV models require coverage-preserving methods (random selection), while higher-CV models can benefit from importance-based scoring.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_experimental_setup_20260521T120135",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 33 · 2026-05-21T12:06:43.507026+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/experimental_setup.tex",
  "old_string": "$\\pi_0.5$ uses $k \\in \\{0.3, 0.5, 0.7\\}$ under both L2 and random removal in closed-loop evaluation, enabling direct method comparison within a single architecture. X-VLA spans $k \\in \\{0.1, 0.2, 0.3, 0.5, 0.7, 0.8, 0.85, 0.9, 0.95\\}$ with L2 removal across three seeds, providing the finest-grained retention sweep in our study and sufficient resolution to locate sharp onset thresholds.",
  "new_string": "$\\pi_0.5$ uses $k \\in \\{0.3, 0.5, 0.7\\}$ under both L2 and random removal in closed-loop evaluation; the dual-method design enables direct comparison within a single architecture. X-VLA spans $k \\in \\{0.1, 0.2, 0.3, 0.5, 0.7, 0.8, 0.85, 0.9, 0.95\\}$ with L2 removal across three seeds; this is the finest-grained retention sweep in our study and provides sufficient resolution to locate sharp onset thresholds."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_experimental_setup_20260521T120135",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/experimental_setup.tex",
    "old_string": "$\\pi_0.5$ uses $k \\in \\{0.3, 0.5, 0.7\\}$ under both L2 and random removal in closed-loop evaluation, enabling direct method comparison within a single architecture. X-VLA spans $k \\in \\{0.1, 0.2, 0.3, 0.5, 0.7, 0.8, 0.85, 0.9, 0.95\\}$ with L2 removal across three seeds, providing the finest-grained retention sweep in our study and sufficient resolution to locate sharp onset thresholds.",
    "new_string": "$\\pi_0.5$ uses $k \\in \\{0.3, 0.5, 0.7\\}$ under both L2 and random removal in closed-loop evaluation; the dual-method design enables direct comparison within a single architecture. X-VLA spans $k \\in \\{0.1, 0.2, 0.3, 0.5, 0.7, 0.8, 0.85, 0.9, 0.95\\}$ with L2 removal across three seeds; this is the finest-grained retention sweep in our study and provides sufficient resolution to locate sharp onset thresholds."
  }
}
```

</details>

---

### Tool result

_source line 34 · 2026-05-21T12:06:43.507227+00:00_

The file /home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/experimental_setup.tex has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_experimental_setup_20260521T120135",
  "tool": "Edit",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 35 · 2026-05-21T12:06:43.507371+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/experimental_setup.tex",
  "old_string": "CV measures the input-side importance gradient; entropy captures how the downstream LLM allocates attention, providing a complementary view of the same structural property. OFT and OpenVLA share nearly identical entropy values (0.667 vs.\\ 0.661), confirming that the connector, not the action head, determines token utilization patterns.",
  "new_string": "CV measures the input-side importance gradient; entropy captures how the downstream LLM allocates attention and provides a complementary view of the same structural property. OFT and OpenVLA share nearly identical entropy values (0.667 vs.\\ 0.661); the match confirms that the connector, not the action head, determines token utilization patterns."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_experimental_setup_20260521T120135",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/experimental_setup.tex",
    "old_string": "CV measures the input-side importance gradient; entropy captures how the downstream LLM allocates attention, providing a complementary view of the same structural property. OFT and OpenVLA share nearly identical entropy values (0.667 vs.\\ 0.661), confirming that the connector, not the action head, determines token utilization patterns.",
    "new_string": "CV measures the input-side importance gradient; entropy captures how the downstream LLM allocates attention and provides a complementary view of the same structural property. OFT and OpenVLA share nearly identical entropy values (0.667 vs.\\ 0.661); the match confirms that the connector, not the action head, determines token utilization patterns."
  }
}
```

</details>

---

### Tool result

_source line 36 · 2026-05-21T12:06:43.507529+00:00_

The file /home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/experimental_setup.tex has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_experimental_setup_20260521T120135",
  "tool": "Edit",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 37 · 2026-05-21T12:06:43.507661+00:00_

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
  "session": "worker_paper_writing_experimental_setup_20260521T120135",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/experimental_setup.tex"
  }
}
```

</details>

---

### Tool result

_source line 38 · 2026-05-21T12:06:43.507825+00:00_

1	\section{Methods and Experimental Setup}
2	\label{sec:experimental_setup}
3	
4	\subsection{Architectures and Benchmark}
5	\label{sec:setup_overview}
6	
7	Seven VLA architectures spanning three vision connector families provide the testbed for our pruning study (Figure~\ref{fig:architecture}).
8	
9	\textbf{Linear projection.} $\pi_0$~\cite{black2024pi0} (3.3B parameters, 256 tokens) maps SigLIP~\cite{zhai2023siglip} patches through a single linear layer into a PaliGemma backbone and generates actions via flow matching~\cite{lipman2023flow}. $\pi_0.5$~\cite{black2025pi05} (4B parameters, 768 vision tokens from three cameras: left wrist, right wrist, base) applies a linear projection with learned $\times\!\sqrt{d}$ scaling into the same PaliGemma backbone with flow matching action generation; the larger token count arises from processing three camera views rather than one. X-VLA~\cite{zheng2025xvla} (880M parameters, 50 tokens) augments its linear projection with a 12-layer BART encoder~\cite{lewis2020bart}; self-attention in these layers introduces cross-token mixing that makes the effective pipeline more complex than the nominal ``linear projection'' label suggests. All three models share the linear projection label, yet their post-projection processing spans a spectrum from no additional computation ($\pi_0$) to a full transformer encoder (X-VLA).
10	
11	\textbf{MLP projector.} OpenVLA~\cite{kim2024openvla} (7B parameters, 256 tokens) fuses DINOv2~\cite{oquab2023dinov2} and SigLIP encoders through a three-layer MLP (GELU activations) that maps each patch independently into a Llama-2 backbone. OFT~\cite{kim2025openoft} shares this MLP connector with an optimized fine-tuning action head; we include OFT for attention entropy comparison only, as both metrics match OpenVLA and confirm the connector determines token importance structure. CogACT~\cite{li2024cogact} uses an MLP projector and retains 74.2\% SR under 78\% pruning as reported by EfficientVLA~\cite{yang2025ef
…[truncated 7697 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_experimental_setup_20260521T120135",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 39 · 2026-05-21T12:06:43.507973+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "wc -w /home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/experimental_setup.tex",
  "description": "Final word count after style fixes"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_experimental_setup_20260521T120135",
  "tool": "Bash",
  "tool_args": {
    "command": "wc -w /home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/experimental_setup.tex",
    "description": "Final word count after style fixes"
  }
}
```

</details>

---

### Tool result

_source line 40 · 2026-05-21T12:06:43.508093+00:00_

1206 /home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/experimental_setup.tex

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_experimental_setup_20260521T120135",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 41 · 2026-05-21T12:06:43.508290+00:00_

1206 raw words (~1050 rendered). Final checks pass: no em-dash, no explanatory en-dash, no "Importantly/Notably/Interestingly", no paragraph-initial "This/These/It", no -ing participle endings after the fixes.

Changes from the previous version:
- **§3.1**: Added π0.5 (4B, 768 tokens, 3 cameras, ×√d scaling) and CogACT (literature corroboration, 74.2% SR under 78% pruning). Expanded LIBERO suite descriptions. Added π0.5 98.2% baseline.
- **§3.2**: Merged the old §3.2 (SmolVLA ablation) and §3.3 (cross-model protocol) into a unified pruning protocol section. Two methods (L2 norm-based vs. random) with model-specific k ranges. Added the OpenVLA-vs-X-VLA cross-method reasoning.
- **§3.3**: VTR setup retained, minor additions (scaled dot-product attention, M=16 compression ratio, 3-seed evaluation).
- **§3.4**: New standalone section for diagnostic metrics (CV + attention entropy), moved out of the old §3.3. Added CV ranges for each taxonomy class and the OFT/OpenVLA entropy comparison.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_paper_writing_experimental_setup_20260521T120135"
}
```

</details>

---
