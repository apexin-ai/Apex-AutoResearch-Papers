# paper writing abstract conclusion reframe

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 17
- **Recorded user turns:** 0
- **Tool calls:** 8
- **Original source:** `logs/chats/worker_paper_writing_abstract_conclusion_reframe_20260520T115027.jsonl`
- **Structured JSON:** [`91666f84ca0d9525743c.json`](../../sessions/91/91666f84ca0d9525743c.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

17 recorded events

### Tool call

_source line 1 · 2026-05-20T11:53:35.460193+00:00_

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
  "session": "worker_paper_writing_abstract_conclusion_reframe_20260520T115027",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/agent-ml-research/skills/global/paper-writing-norms.skill.md"
  }
}
```

</details>

---

### Tool result

_source line 2 · 2026-05-20T11:53:35.460751+00:00_

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
  "session": "worker_paper_writing_abstract_conclusion_reframe_20260520T115027",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-20T11:53:35.460945+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/abstract.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_abstract_conclusion_reframe_20260520T115027",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/abstract.tex"
  }
}
```

</details>

---

### Tool result

_source line 4 · 2026-05-20T11:53:35.461095+00:00_

1	\begin{abstract}
2	Vision token pruning reliably accelerates Vision Transformer (ViT) inference with negligible accuracy loss, prompting recent proposals to apply the same technique to Vision-Language-Action (VLA) models for faster robotic control. We conduct the first systematic comparison of how vision connector design affects token pruning sensitivity in closed-loop VLA control and find that compressibility is associated with the vision connector architecture. SmolVLA, whose pixel-shuffle connector spatially folds patches into high-density tokens, exhibits a cliff-edge failure: pruning collapses success rate from 59.2\% to 0\% on the official checkpoint, even at 5\% token removal. This failure is robust across seven pruning configurations and three mechanisms. OpenVLA, whose MLP projector maps patches independently, degrades gracefully under the same conditions. The divergence co-occurs with differences in token information density: pixel-shuffle produces tokens with near-uniform attention, while MLP-projected tokens develop progressively selective attention in deeper layers. A diagnostic experiment confirms that learned re-encoding succeeds where all deletion methods fail: both a cross-attention and a parameter-matched MLP module recover 60--63\% SR at 75\% token reduction where all deletion methods yield 0\%, and a passthrough control isolates re-encoding as the causal factor. These findings, consistent with independent results on CogACT, suggest that VLA token compressibility is architecture-dependent and that learned re-encoding can overcome failures that deletion-based methods share.
3	\end{abstract}
4	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_abstract_conclusion_reframe_20260520T115027",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-20T11:53:35.461307+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/conclusion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_abstract_conclusion_reframe_20260520T115027",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/conclusion.tex"
  }
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-20T11:53:35.461452+00:00_

1	\section{Conclusion}
2	\label{sec:conclusion}
3	
4	We presented the first systematic comparison of how vision connector design affects token pruning sensitivity in closed-loop VLA control. Compressibility is associated with the vision connector: pixel-shuffle connectors create spatially entangled tokens that collapse under any form of deletion (59.2\% $\to$ 0\% on the official checkpoint), while MLP projectors degrade gracefully (74.0\% $\to$ 37.4\%). The attention entropy ratio (0.95 vs.\ 0.64) captures this divergence, consistent with independent findings on CogACT (EfficientVLA~\cite{yang2025efficientvla}). For architectures where pruning fails, learned re-encoding recovers performance: both cross-attention and parameter-matched MLP modules raise SR from 44.8\% to 60--63\% at 75\% token reduction, where all deletion methods yield 0\%. The benefit depends on baseline feature quality, with larger gains on undertrained checkpoints. Re-encoding succeeds where deletion cannot, regardless of the specific module architecture. Standard offline metrics do not predict these closed-loop outcomes; closed-loop evaluation is essential for validating VLA compression. Code and evaluation scripts will be released upon publication.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_abstract_conclusion_reframe_20260520T115027",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-20T11:53:35.461582+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_abstract_conclusion_reframe_20260520T115027",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/introduction.tex"
  }
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-20T11:53:35.461733+00:00_

1	\section{Introduction}
2	\label{sec:introduction}
3	
4	Vision token pruning is among the most reliable efficiency techniques for Vision Transformers: DynamicViT~\cite{rao2021dynamicvit} removes 66\% of tokens with $<$0.5\% accuracy loss, ToMe~\cite{bolya2023tome} merges 40\% at $>$99\% accuracy, and EViT~\cite{liang2022evit} discards 50\% with negligible degradation. Vision-Language-Action (VLA) models~\cite{brohan2023rt1,brohan2023rt2,kim2024openvla,black2024pi0,ghosh2024octo,shukor2025smolvla} use the same ViT encoders, producing hundreds of tokens that dominate the LLM backbone's input. For real-time robotic control at 5--10\,Hz, reducing these tokens would directly accelerate the quadratic attention computation. Several recent works explore this direction~\cite{chen2024fastv,xu2025vlacache,cheng2026vlaiap}, but they share an untested assumption: that pruning behaves consistently across VLA architectures.
5	
6	VLAs differ in a critical component, the vision connector that transforms ViT patches into tokens for the language backbone. Pixel-shuffle connectors~\cite{shukor2025smolvla,chen2024internvl} fold spatial patches via channel concatenation; MLP projectors~\cite{liu2023llava,kim2024openvla} map each patch independently; linear projections pass each patch through directly. No prior work has systematically tested how these connector designs affect pruning sensitivity in closed-loop robotic control, where a single wrong action compounds irrecoverably.
7	
8	We conduct the first cross-architecture study of vision token pruning across five VLA models (450M--7B parameters) spanning three connector families. The results reveal a spectrum governed by effective vision-to-LLM pipeline complexity. $\pi_0$~\cite{black2024pi0} (linear projection, 3.3B): offline action loss \emph{improves} by 2.4\% at 90\% token removal. X-VLA~\cite{zheng2025xvla} (linear projection + BART encoder~\cite{lewis2020bart}, 880M): robust at $k \geq 0.9$ (97.6\% SR), then drops to 56.2\% at $k{
…[truncated 1804 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_abstract_conclusion_reframe_20260520T115027",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-20T11:53:35.461878+00:00_

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
  "session": "worker_paper_writing_abstract_conclusion_reframe_20260520T115027",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/results.tex"
  }
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-20T11:53:35.462077+00:00_

1	\section{Results}
2	\label{sec:results}
3	
4	We evaluate token pruning across five VLA models spanning three connector families on LIBERO-Object~\cite{liu2023libero} (10 tasks, 50 episodes each, 500 total). All success rates include Wilson 95\% confidence intervals for single-seed results and mean $\pm$ standard deviation for multi-seed results.
5	
6	\subsection{Taxonomy Overview}
7	\label{sec:taxonomy_overview}
8	
9	Table~\ref{tab:taxonomy} summarizes the five models and their pruning responses. The effective vision-to-LLM pipeline complexity, rather than the nominal connector label, determines pruning tolerance. A pure linear projection ($\pi_0$) is immune; a linear projection followed by a deep encoder (X-VLA) is threshold-graded (robust above a retention threshold, then graded decline); a multi-layer MLP degrades smoothly; and pixel-shuffle collapses catastrophically. Token importance heterogeneity (CV) tracks this ordering continuously: 0.038, 0.151, 0.215, 0.314. The pattern holds across a 16$\times$ range in model size (450M to 7B parameters), which suggests scale alone does not explain it.
10	
11	A controlled comparison isolates the vision-to-LLM pipeline as the causal factor. $\pi_0$ and OpenVLA share the same token count (256), the same vision encoder lineage (SigLIP~\cite{zhai2023siglip}), and differ only in the connector: linear projection versus 3-layer MLP. At $k{=}0.1$ (retaining 10\% of tokens), $\pi_0$'s action loss \emph{improves} by 2.4\% while OpenVLA's degrades by 61\%. This 63-percentage-point gap is attributable to pipeline architecture alone. X-VLA's threshold-graded pattern (robust at $k \geq 0.9$, then degradation at $k{=}0.7$) further demonstrates that the \emph{effective} pipeline complexity---not just the connector label---determines pruning tolerance (Section~\ref{sec:linear_results}). OFT~\cite{kim2025openoft}, which replaces OpenVLA's action head but retains its 3-layer MLP connector, produces nearly identical attention entropy (0.6
…[truncated 13061 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_abstract_conclusion_reframe_20260520T115027",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-20T11:53:35.462252+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/analysis.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_abstract_conclusion_reframe_20260520T115027",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/analysis.tex"
  }
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-20T11:53:35.462432+00:00_

1	\section{Analysis and Discussion}
2	\label{sec:analysis}
3	
4	\subsection{Effective Pipeline Complexity Determines Token Independence}
5	\label{sec:pixel_shuffle}
6	
7	A controlled comparison between $\pi_0$ and OpenVLA isolates the vision connector as the causal factor behind compressibility differences. Both models process 256 vision tokens from SigLIP encoders, yet at $k{=}0.1$, $\pi_0$'s offline action loss improves by 2.4\% while OpenVLA's closed-loop SR degrades by 61\%. This 63 percentage-point gap, with token count and encoder held constant, can only be attributed to the connector. We note that $\pi_0$'s result is offline; X-VLA's offline-to-closed-loop divergence (Section~\ref{sec:metric_disconnect}) cautions against treating offline immunity as definitive.
8	
9	The vision-to-LLM pipeline creates fundamentally different token structures depending on its effective complexity. Pixel-shuffle connectors (SmolVLA) apply $4 \times 4$ spatial folding: each of 128 tokens encodes 16 patches via channel concatenation (Figure~\ref{fig:pixel_shuffle}). Removing any token eliminates an entire receptive field with no redundancy from neighbors. The folding is fixed and non-learned, so no downstream layer can recover discarded information.
10	
11	\begin{figure}[t]
12	\centering
13	\includegraphics[width=0.85\linewidth]{figures/paper/fig_pixel_shuffle.pdf}
14	\caption{Pixel-shuffle folding: each $4{\times}4$ block of SigLIP patches is channel-concatenated into one token. Removing any token eliminates its receptive field (gray) with no redundancy.}
15	\label{fig:pixel_shuffle}
16	\end{figure}
17	
18	Pure linear projection connectors ($\pi_0$) apply a single linear layer that maps each patch independently. No cross-token interaction occurs during projection, so tokens are genuinely independent. Removing one token loses approximately $1/N$ of the visual field, and the loss is spatially uniform.
19	
20	X-VLA complicates this picture. Its connector is nominally a linear projec
…[truncated 10745 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_abstract_conclusion_reframe_20260520T115027",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-20T11:53:35.462692+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/abstract.tex",
  "old_string": "\\begin{abstract}\nVision token pruning reliably accelerates Vision Transformer (ViT) inference with negligible accuracy loss, prompting recent proposals to apply the same technique to Vision-Language-Action (VLA) models for faster robotic control. We conduct the first systematic comparison of how vision connector design affects token pruning sensitivity in closed-loop VLA control and find that compressibility is associated with the vision connector architecture. SmolVLA, whose pixel-shuffle connector spatially folds patches into high-density tokens, exhibits a cliff-edge failure: pruning collapses success rate from 59.2\\% to 0\\% on the official checkpoint, even at 5\\% token removal. This failure is robust across seven pruning configurations and three mechanisms. OpenVLA, whose MLP projector maps patches independently, degrades gracefully under the same conditions. The divergence co-occurs with differences in token information density: pixel-shuffle produces tokens with near-uniform attention, while MLP-projected tokens develop progressively selective attention in deeper layers. A diagnostic experiment confirms that learned re-encoding succeeds where all deletion methods fail: both a cross-attention and a parameter-matched MLP module recover 60--63\\% SR at 75\\% token reduction where all deletion methods yield 0\\%, and a passthrough control isolates re-encoding as the causal factor. These findings, consistent with independent results on CogACT, suggest that VLA token compressibility is architecture-dependent and that learned re-encoding can overcome failures that deletion-based methods share.\n\\end{abstract}",
  "new_string": "\\begin{abstract}\nVision token pruning accelerates Vision Transformer inference with negligible accuracy loss, but whether this robustness transfers to Vision-Language-Action (VLA) models remains untested across architectures. We evaluate five VLA models (450M--7B parameters) spanning three connector families and identify four response classes governed by effective pipeline complexity. $\\pi_0$ (linear projection) is \\emph{immune}: offline action loss improves 2.4\\% at 90\\% removal. X-VLA (linear projection + encoder) is \\emph{threshold-graded}: 97.6\\% Success Rate (SR) at $k{=}0.9$, onset at $k{=}0.7$ (56.2\\%). OpenVLA (MLP projector) degrades \\emph{smoothly}: 74.0\\% $\\to$ 37.4\\% SR at 50\\% removal. SmolVLA (pixel-shuffle) hits a \\emph{catastrophic cliff}: 0\\% SR at 5\\% removal. The coefficient of variation (CV) of token importance predicts this ordering continuously ($0.038 \\to 0.151 \\to 0.215 \\to 0.314$) from a single forward pass. For cliff-edge architectures, a Vision Token Re-encoder (VTR) recovers 60\\%+ SR at 75\\% compression where all deletion methods yield 0\\%. VLA compressibility is architecture-dependent; CV diagnostic combined with VTR forms a Diagnose-then-Compress framework for safe token reduction.\n\\end{abstract}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_abstract_conclusion_reframe_20260520T115027",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/abstract.tex",
    "old_string": "\\begin{abstract}\nVision token pruning reliably accelerates Vision Transformer (ViT) inference with negligible accuracy loss, prompting recent proposals to apply the same technique to Vision-Language-Action (VLA) models for faster robotic control. We conduct the first systematic comparison of how vision connector design affects token pruning sensitivity in closed-loop VLA control and find that compressibility is associated with the vision connector architecture. SmolVLA, whose pixel-shuffle connector spatially folds patches into high-density tokens, exhibits a cliff-edge failure: pruning collapses success rate from 59.2\\% to 0\\% on the official checkpoint, even at 5\\% token removal. This failure is robust across seven pruning configurations and three mechanisms. OpenVLA, whose MLP projector maps patches independently, degrades gracefully under the same conditions. The divergence co-occurs with differences in token information density: pixel-shuffle produces tokens with near-uniform attention, while MLP-projected tokens develop progressively selective attention in deeper layers. A diagnostic experiment confirms that learned re-encoding succeeds where all deletion methods fail: both a cross-attention and a parameter-matched MLP module recover 60--63\\% SR at 75\\% token reduction where all deletion methods yield 0\\%, and a passthrough control isolates re-encoding as the causal factor. These findings, consistent with independent results on CogACT, suggest that VLA token compressibility is architecture-dependent and that learned re-encoding can overcome failures that deletion-based methods share.\n\\end{abstract}",
    "new_string": "\\begin{abstract}\nVision token pruning accelerates Vision Transformer inference with negligible accuracy loss, but whether this robustness transfers to Vision-Language-Action (VLA) models remains untested across architectures. We evaluate five VLA models (450M--7B parameters) spanning three connector families and identify four response classes governed by effective pipeline complexity. $\\pi_0$ (linear projection) is \\emph{immune}: offline action loss improves 2.4\\% at 90\\% removal. X-VLA (linear projection + encoder) is \\emph{threshold-graded}: 97.6\\% Success Rate (SR) at $k{=}0.9$, onset at $k{=}0.7$ (56.2\\%). OpenVLA (MLP projector) degrades \\emph{smoothly}: 74.0\\% $\\to$ 37.4\\% SR at 50\\% removal. SmolVLA (pixel-shuffle) hits a \\emph{catastrophic cliff}: 0\\% SR at 5\\% removal. The coefficient of variation (CV) of token importance predicts this ordering continuously ($0.038 \\to 0.151 \\to 0.215 \\to 0.314$) from a single forward pass. For cliff-edge architectures, a Vision Token Re-encoder (VTR) recovers 60\\%+ SR at 75\\% compression where all deletion methods yield 0\\%. VLA compressibility is architecture-dependent; CV diagnostic combined with VTR forms a Diagnose-then-Compress framework for safe token reduction.\n\\end{abstract}"
  }
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-20T11:53:35.462935+00:00_

The file /home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/abstract.tex has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_abstract_conclusion_reframe_20260520T115027",
  "tool": "Edit",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-20T11:53:35.463484+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/conclusion.tex",
  "old_string": "\\section{Conclusion}\n\\label{sec:conclusion}\n\nWe presented the first systematic comparison of how vision connector design affects token pruning sensitivity in closed-loop VLA control. Compressibility is associated with the vision connector: pixel-shuffle connectors create spatially entangled tokens that collapse under any form of deletion (59.2\\% $\\to$ 0\\% on the official checkpoint), while MLP projectors degrade gracefully (74.0\\% $\\to$ 37.4\\%). The attention entropy ratio (0.95 vs.\\ 0.64) captures this divergence, consistent with independent findings on CogACT (EfficientVLA~\\cite{yang2025efficientvla}). For architectures where pruning fails, learned re-encoding recovers performance: both cross-attention and parameter-matched MLP modules raise SR from 44.8\\% to 60--63\\% at 75\\% token reduction, where all deletion methods yield 0\\%. The benefit depends on baseline feature quality, with larger gains on undertrained checkpoints. Re-encoding succeeds where deletion cannot, regardless of the specific module architecture. Standard offline metrics do not predict these closed-loop outcomes; closed-loop evaluation is essential for validating VLA compression. Code and evaluation scripts will be released upon publication.",
  "new_string": "\\section{Conclusion}\n\\label{sec:conclusion}\n\nWe studied vision token pruning across five VLA models spanning three connector families. Five findings emerge. (1)~Compressibility is architecture-dependent: effective pipeline complexity, not model scale, determines pruning tolerance across a 16$\\times$ parameter range, producing four response classes. (2)~Pixel-shuffle connectors create irreversible spatial entanglement: SmolVLA collapses to 0\\% SR at 5\\% token removal, robust across seven pruning configurations and three mechanisms. (3)~Token importance CV predicts degradation onset continuously ($0.038 \\to 0.151 \\to 0.215 \\to 0.314$) from a single forward pass, at zero additional cost. (4)~VTR re-encoding overcomes the cliff-edge: both cross-attention and MLP modules recover 60\\%+ SR at 75\\% compression where deletion yields 0\\%, with a flat M-curve ($M{=}16 \\approx M{=}128$). (5)~Offline metrics underestimate closed-loop failure; $\\pi_0$'s offline immunity (2.4\\% improvement at $k{=}0.1$) requires closed-loop verification.\n\nThese results carry design implications. VLA architectures that require token efficiency should avoid pixel-shuffle connectors or include re-encoding modules. CV provides a zero-cost, single-forward-pass diagnostic that identifies vulnerability before deployment. Closed-loop evaluation remains essential for validating VLA compression. Code and evaluation scripts will be released upon publication."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_abstract_conclusion_reframe_20260520T115027",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/conclusion.tex",
    "old_string": "\\section{Conclusion}\n\\label{sec:conclusion}\n\nWe presented the first systematic comparison of how vision connector design affects token pruning sensitivity in closed-loop VLA control. Compressibility is associated with the vision connector: pixel-shuffle connectors create spatially entangled tokens that collapse under any form of deletion (59.2\\% $\\to$ 0\\% on the official checkpoint), while MLP projectors degrade gracefully (74.0\\% $\\to$ 37.4\\%). The attention entropy ratio (0.95 vs.\\ 0.64) captures this divergence, consistent with independent findings on CogACT (EfficientVLA~\\cite{yang2025efficientvla}). For architectures where pruning fails, learned re-encoding recovers performance: both cross-attention and parameter-matched MLP modules raise SR from 44.8\\% to 60--63\\% at 75\\% token reduction, where all deletion methods yield 0\\%. The benefit depends on baseline feature quality, with larger gains on undertrained checkpoints. Re-encoding succeeds where deletion cannot, regardless of the specific module architecture. Standard offline metrics do not predict these closed-loop outcomes; closed-loop evaluation is essential for validating VLA compression. Code and evaluation scripts will be released upon publication.",
    "new_string": "\\section{Conclusion}\n\\label{sec:conclusion}\n\nWe studied vision token pruning across five VLA models spanning three connector families. Five findings emerge. (1)~Compressibility is architecture-dependent: effective pipeline complexity, not model scale, determines pruning tolerance across a 16$\\times$ parameter range, producing four response classes. (2)~Pixel-shuffle connectors create irreversible spatial entanglement: SmolVLA collapses to 0\\% SR at 5\\% token removal, robust across seven pruning configurations and three mechanisms. (3)~Token importance CV predicts degradation onset continuously ($0.038 \\to 0.151 \\to 0.215 \\to 0.314$) from a single forward pass, at zero additional cost. (4)~VTR re-encoding overcomes the cliff-edge: both cross-attention and MLP modules recover 60\\%+ SR at 75\\% compression where deletion yields 0\\%, with a flat M-curve ($M{=}16 \\approx M{=}128$). (5)~Offline metrics underestimate closed-loop failure; $\\pi_0$'s offline immunity (2.4\\% improvement at $k{=}0.1$) requires closed-loop verification.\n\nThese results carry design implications. VLA architectures that require token efficiency should avoid pixel-shuffle connectors or include re-encoding modules. CV provides a zero-cost, single-forward-pass diagnostic that identifies vulnerability before deployment. Closed-loop evaluation remains essential for validating VLA compression. Code and evaluation scripts will be released upon publication."
  }
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-20T11:53:35.463693+00:00_

The file /home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/conclusion.tex has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_abstract_conclusion_reframe_20260520T115027",
  "tool": "Edit",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 17 · 2026-05-20T11:53:35.463867+00:00_

Both files rewritten. Key changes:

**Abstract** (~160 words): Reframed from 2-model (SmolVLA vs OpenVLA) to 5-model taxonomy with all four response classes listed explicitly (immune, threshold-graded, smooth graded, catastrophic cliff). CV spectrum and VTR as Diagnose-then-Compress framework. π0 marked offline.

**Conclusion** (~175 words): Structured as 5 enumerated claims (C1-C5) plus design implications paragraph. Numbers verified against Introduction/Results (CV values, SR figures, M-curve, 16× parameter range). Retained "Code and evaluation scripts will be released upon publication."

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_paper_writing_abstract_conclusion_reframe_20260520T115027"
}
```

</details>

---
