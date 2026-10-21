# paper writing method polish

**Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Factorial Analysis** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 15
- **Recorded user turns:** 0
- **Tool calls:** 7
- **Original source:** `logs/chats/worker_paper_writing_method_polish_20260528T005026.jsonl`
- **Structured JSON:** [`7890c48fcd7ffb391ce1.json`](../../sessions/78/7890c48fcd7ffb391ce1.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

15 recorded events

### Tool call

_source line 1 · 2026-05-28T00:52:41.883558+00:00_

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
  "session": "worker_paper_writing_method_polish_20260528T005026",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/agent-ml-research/skills/global/paper-writing-norms.skill.md"
  }
}
```

</details>

---

### Tool result

_source line 2 · 2026-05-28T00:52:41.884304+00:00_

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
  "session": "worker_paper_writing_method_polish_20260528T005026",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-28T00:52:41.884495+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/docs/paper/method.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_method_polish_20260528T005026",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/docs/paper/method.tex"
  }
}
```

</details>

---

### Tool result

_source line 4 · 2026-05-28T00:52:41.884695+00:00_

1	
2	\section{Method}
3	
4	We fine-tune OpenVLA-7B~\cite{kim2024openvla} with the OFT recipe~\cite{kim2025oft}, which concatenates DINOv2~\cite{oquab2024dinov2} (1024-d) and SigLIP~\cite{zhai2023siglip} (1152-d) patch features into a 2176-dimensional representation per spatial token. We apply LoRA~\cite{hu2022lora} (rank 32, $\alpha{=}16$) and augment the action prediction loss with an auxiliary spatial prediction head:
5	\begin{equation}
6	\mathcal{L}_\text{total} = \mathcal{L}_\text{action} + \lambda(t) \cdot \mathcal{L}_\text{aux}(h(\phi_v(o_t)), s_t^*),
7	\quad \lambda(t) = 0.01 \cdot \exp(-t / 50000)
8	\end{equation}
9	where $h$ denotes the auxiliary head, $\phi_v$ the frozen-then-LoRA-adapted vision encoders, and $s_t^*$ the ground-truth spatial label at step $t$. The coefficient $\lambda(t)$ decays exponentially so that spatial gradients shape early representations without dominating late-stage action refinement. The auxiliary head is discarded at inference, incurring zero additional cost.
10	
11	\textbf{BEV occupancy head.} The head (1.2M parameters) maps the 256 patch tokens from the current observation frame to a $64{\times}64$ binary occupancy grid. A linear projection ($2176{\to}256$) is reshaped to $16{\times}16$, followed by two transposed convolutions ($256{\to}128{\to}64$, kernel 4, stride 2) each with BatchNorm2d and GELU, and a final $1{\times}1$ convolution with sigmoid activation. Ground-truth grids are rendered from MuJoCo simulator state replay by projecting object bounding boxes onto the table-plane BEV. Training uses focal loss~\cite{lin2017focal} ($\alpha{=}0.25$, $\gamma{=}2.0$) to handle class imbalance in the sparse occupancy signal. The initial auxiliary weight $\lambda_0{=}0.01$ is set to keep auxiliary gradients below 2\% of the action loss magnitude, avoiding interference with action learning.
12	
13	\textbf{Monocular depth head.} This head shares the same convolutional architecture but replaces the sigmoid with ReLU and uses smooth-L
…[truncated 3587 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_method_polish_20260528T005026",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-28T00:52:41.884961+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "lambda.*exp\\|\\\\lambda.*decay\\|50000\\|50,?000",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/docs/paper",
  "output_mode": "content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_method_polish_20260528T005026",
  "tool": "Grep",
  "tool_args": {
    "pattern": "lambda.*exp\\|\\\\lambda.*decay\\|50000\\|50,?000",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/docs/paper",
    "output_mode": "content"
  }
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-28T00:52:41.885103+00:00_

No matches found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_method_polish_20260528T005026",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-28T00:52:41.885226+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "lambda|50000|decay",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/docs/paper",
  "output_mode": "content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_method_polish_20260528T005026",
  "tool": "Grep",
  "tool_args": {
    "pattern": "lambda|50000|decay",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/docs/paper",
    "output_mode": "content"
  }
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-28T00:52:41.885358+00:00_

docs/paper/main.log:636: 655787 words of memory out of 5000000
docs/paper/main.log:661: 103 named destinations out of 1000 (max. 500000)
docs/paper/method.tex:6:\mathcal{L}_\text{total} = \mathcal{L}_\text{action} + \lambda(t) \cdot \mathcal{L}_\text{aux}(h(\phi_v(o_t)), s_t^*),
docs/paper/method.tex:7:\quad \lambda(t) = 0.01 \cdot \exp(-t / 50000)
docs/paper/method.tex:9:where $h$ denotes the auxiliary head, $\phi_v$ the frozen-then-LoRA-adapted vision encoders, and $s_t^*$ the ground-truth spatial label at step $t$. The coefficient $\lambda(t)$ decays exponentially so that spatial gradients shape early representations without dominating late-stage action refinement. The auxiliary head is discarded at inference, incurring zero additional cost.
docs/paper/method.tex:11:[Omitted long matching line]
docs/paper/appendix.tex:55:Aux.\ loss weight $\lambda_0$ & 0.01 \\
docs/paper/appendix.tex:56:Aux.\ loss decay & $\exp(-t / 50{,}000)$ \\
docs/paper/appendix.tex:72:\textbf{Cutoff implementation.} As described in Section~\ref{sec:ablation}, setting $\lambda(t){=}0$ does not disable the auxiliary head's forward pass; the post-cutoff phase operates in Detach mode with BatchNorm statistics continuing to update (see the Cutoff description therein for details).
docs/paper/appendix.tex:191:[Omitted long matching line]
docs/paper/experiments_old.tex:30:All conditions share the same base model: OpenVLA-OFT 7B~\cite{kim2025oft}, pre-trained on Open X-Embodiment. We fine-tune with LoRA (rank 32, $\alpha{=}16$) for 50K steps using AdamW (weight decay $0.01$), a batch size of 8, a constant learning rate of $5 \times 10^{-4}$, and 2--4 random seeds per condition (see Table~\ref{tab:main_results}). The LoRA adapter adds 110.8M trainable parameters (1.45\% of 7.65B total).
docs/paper/experiments_old.tex:32:[Omitted long matching line]
docs/paper/figures/fig1_overview.py:117:ax_a.text(8.7, 7.3, r'$\lambda(t) \cdot \mathcal{L}_{\mathrm{aux}}$',

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_method_polish_20260528T005026",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-28T00:52:41.885511+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/docs/paper/appendix.tex",
  "offset": "65",
  "limit": "20"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_method_polish_20260528T005026",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/docs/paper/appendix.tex",
    "offset": "65",
    "limit": "20"
  }
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-28T00:52:41.885650+00:00_

65	\end{table}
66	
67	\textbf{Evaluation protocol.} Each condition uses 3+ seeds (Depth uses 4; Cutoff@15K, Cutoff@25K, and Reverse Cutoff use 2; Cutoff@45K uses 1) with 50 rollouts per task per seed (500 episodes per seed). A collision is registered when the L1 displacement of the obstacle's \texttt{body\_xpos} exceeds $10^{-3}$. Bootstrap 95\% CIs are computed via 10{,}000 resamples (percentile method).
68	
69	\textbf{Statistical tests.} Pairwise comparisons against Vanilla use two-tailed permutation tests on per-seed mean CARs with Cohen's $d$ for effect size. With $n{=}3$ seeds, statistical power is limited; we report $p$-values and effect sizes for transparency.
70	\textbf{CKA analysis.} Centered Kernel Alignment~\cite{kornblith2019similarity} measures representational similarity between fine-tuned and pretrained encoder features. We extract patch token activations from the final layer of DINOv2 and SigLIP for 1{,}000 validation images, compute linear CKA per layer, and report the mean across layers. Higher CKA indicates better preservation of pretrained representations.
71	
72	\textbf{Cutoff implementation.} As described in Section~\ref{sec:ablation}, setting $\lambda(t){=}0$ does not disable the auxiliary head's forward pass; the post-cutoff phase operates in Detach mode with BatchNorm statistics continuing to update (see the Cutoff description therein for details).
73	
74	\section{Extended Analysis}
75	
76	\begin{figure}[h]
77	\centering
78	\includegraphics[width=\textwidth]{figures/gradient_analysis_v2_combined.pdf}
79	\caption{Gradient dynamics during VLA fine-tuning (v2 codebase; seed 42, 200 batches at 50K checkpoint). Five conditions: Vanilla, Full OCC (BN), Full OCC+LN, Detach OCC (BN), Detach+LN. (a)~Action loss gradient norms per encoder layer: all conditions maintain comparable norms, ruling out gradient amplification. (b)~Auxiliary loss gradient norms in the shared encoder (Detach conditions excluded; no auxiliary gradients by design). (c)~Action--
…[truncated 719 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_method_polish_20260528T005026",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-28T00:52:41.885900+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/docs/paper/method.tex",
  "old_string": "The $2{\\times}2$ factorial core crosses gradient flow (ON/OFF) with normalization (BN/LN): \\textbf{Vanilla} (no auxiliary head), \\textbf{Full OCC} (BEV occupancy, gradient flow, BatchNorm), \\textbf{Detach OCC} (gradients blocked via \\texttt{stop\\_gradient}), and their LN variants (\\textbf{Full OCC+LN}, \\textbf{Detach+LN}). Seven supplementary conditions probe label content (\\textbf{Random OCC}), reference frame (\\textbf{Depth}), and temporal extent (\\textbf{Cutoff@\\{15K--45K\\}}, \\textbf{Reverse Cutoff}; details in Appendix~\\ref{app:training}). Table~\\ref{tab:ablation_design} summarizes all twelve conditions and nine pairwise comparisons.\n\n\\begin{table}[t]",
  "new_string": "The $2{\\times}2$ factorial core crosses gradient flow (ON/OFF) with normalization (BN/LN): \\textbf{Vanilla} (no auxiliary head), \\textbf{Full OCC} (BEV occupancy, gradient flow, BatchNorm), \\textbf{Detach OCC} (gradients blocked via \\texttt{stop\\_gradient}), and their LN variants (\\textbf{Full OCC+LN}, \\textbf{Detach+LN}). Seven supplementary conditions probe label content (\\textbf{Random OCC}), reference frame (\\textbf{Depth}), and temporal extent (\\textbf{Cutoff@\\{15K--45K\\}}, \\textbf{Reverse Cutoff}; details in Appendix~\\ref{app:training}). Table~\\ref{tab:ablation_design} summarizes all twelve conditions and nine pairwise comparisons.\n\nFormally, let $\\text{sg}(\\cdot)$ denote the stop-gradient operator. Full conditions compute $\\mathcal{L}_\\text{aux}(h(\\phi_v(o_t)), s_t^*)$, so auxiliary gradients flow back through $\\phi_v$. Detach conditions compute $\\mathcal{L}_\\text{aux}(h(\\text{sg}(\\phi_v(o_t))), s_t^*)$: the head $h$ trains on encoder features, but no gradient reaches $\\phi_v$. This distinction separates bidirectional coupling (spatial and action objectives jointly shape encoder representations) from unidirectional readout (the head reads encoder features but does not influence encoder weight updates).\n\n\\begin{table}[t]"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_method_polish_20260528T005026",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/docs/paper/method.tex",
    "old_string": "The $2{\\times}2$ factorial core crosses gradient flow (ON/OFF) with normalization (BN/LN): \\textbf{Vanilla} (no auxiliary head), \\textbf{Full OCC} (BEV occupancy, gradient flow, BatchNorm), \\textbf{Detach OCC} (gradients blocked via \\texttt{stop\\_gradient}), and their LN variants (\\textbf{Full OCC+LN}, \\textbf{Detach+LN}). Seven supplementary conditions probe label content (\\textbf{Random OCC}), reference frame (\\textbf{Depth}), and temporal extent (\\textbf{Cutoff@\\{15K--45K\\}}, \\textbf{Reverse Cutoff}; details in Appendix~\\ref{app:training}). Table~\\ref{tab:ablation_design} summarizes all twelve conditions and nine pairwise comparisons.\n\n\\begin{table}[t]",
    "new_string": "The $2{\\times}2$ factorial core crosses gradient flow (ON/OFF) with normalization (BN/LN): \\textbf{Vanilla} (no auxiliary head), \\textbf{Full OCC} (BEV occupancy, gradient flow, BatchNorm), \\textbf{Detach OCC} (gradients blocked via \\texttt{stop\\_gradient}), and their LN variants (\\textbf{Full OCC+LN}, \\textbf{Detach+LN}). Seven supplementary conditions probe label content (\\textbf{Random OCC}), reference frame (\\textbf{Depth}), and temporal extent (\\textbf{Cutoff@\\{15K--45K\\}}, \\textbf{Reverse Cutoff}; details in Appendix~\\ref{app:training}). Table~\\ref{tab:ablation_design} summarizes all twelve conditions and nine pairwise comparisons.\n\nFormally, let $\\text{sg}(\\cdot)$ denote the stop-gradient operator. Full conditions compute $\\mathcal{L}_\\text{aux}(h(\\phi_v(o_t)), s_t^*)$, so auxiliary gradients flow back through $\\phi_v$. Detach conditions compute $\\mathcal{L}_\\text{aux}(h(\\text{sg}(\\phi_v(o_t))), s_t^*)$: the head $h$ trains on encoder features, but no gradient reaches $\\phi_v$. This distinction separates bidirectional coupling (spatial and action objectives jointly shape encoder representations) from unidirectional readout (the head reads encoder features but does not influence encoder weight updates).\n\n\\begin{table}[t]"
  }
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-28T00:52:41.886085+00:00_

The file /home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/docs/paper/method.tex has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_method_polish_20260528T005026",
  "tool": "Edit",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-28T00:52:41.886212+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/docs/paper/method.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_method_polish_20260528T005026",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/docs/paper/method.tex"
  }
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-28T00:52:41.886369+00:00_

1	
2	\section{Method}
3	
4	We fine-tune OpenVLA-7B~\cite{kim2024openvla} with the OFT recipe~\cite{kim2025oft}, which concatenates DINOv2~\cite{oquab2024dinov2} (1024-d) and SigLIP~\cite{zhai2023siglip} (1152-d) patch features into a 2176-dimensional representation per spatial token. We apply LoRA~\cite{hu2022lora} (rank 32, $\alpha{=}16$) and augment the action prediction loss with an auxiliary spatial prediction head:
5	\begin{equation}
6	\mathcal{L}_\text{total} = \mathcal{L}_\text{action} + \lambda(t) \cdot \mathcal{L}_\text{aux}(h(\phi_v(o_t)), s_t^*),
7	\quad \lambda(t) = 0.01 \cdot \exp(-t / 50000)
8	\end{equation}
9	where $h$ denotes the auxiliary head, $\phi_v$ the frozen-then-LoRA-adapted vision encoders, and $s_t^*$ the ground-truth spatial label at step $t$. The coefficient $\lambda(t)$ decays exponentially so that spatial gradients shape early representations without dominating late-stage action refinement. The auxiliary head is discarded at inference, incurring zero additional cost.
10	
11	\textbf{BEV occupancy head.} The head (1.2M parameters) maps the 256 patch tokens from the current observation frame to a $64{\times}64$ binary occupancy grid. A linear projection ($2176{\to}256$) is reshaped to $16{\times}16$, followed by two transposed convolutions ($256{\to}128{\to}64$, kernel 4, stride 2) each with BatchNorm2d and GELU, and a final $1{\times}1$ convolution with sigmoid activation. Ground-truth grids are rendered from MuJoCo simulator state replay by projecting object bounding boxes onto the table-plane BEV. Training uses focal loss~\cite{lin2017focal} ($\alpha{=}0.25$, $\gamma{=}2.0$) to handle class imbalance in the sparse occupancy signal. The initial auxiliary weight $\lambda_0{=}0.01$ is set to keep auxiliary gradients below 2\% of the action loss magnitude, avoiding interference with action learning.
12	
13	\textbf{Monocular depth head.} This head shares the same convolutional architecture but replaces the sigmoid with ReLU and uses smooth-L
…[truncated 4176 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_method_polish_20260528T005026",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 15 · 2026-05-28T00:52:41.886560+00:00_

编辑完成。改动总结：

1. **sg() 形式化** (line 22): 用 $\text{sg}(\cdot)$ 算子明确定义 Full vs Detach 的数学区别，直接复用主损失公式中的符号。

2. **直觉解释** (line 22 末句): "bidirectional coupling" vs "unidirectional readout" 一句话概括两种条件下 auxiliary head 与 encoder 的耦合方向。

3. **λ(t) 和 focal loss 一致性**: 已验证 method.tex 的 $\lambda(t) = 0.01 \cdot \exp(-t/50000)$ 与 appendix.tex 的 $\lambda_0=0.01$, decay $\exp(-t/50{,}000)$ 完全一致；focal loss 参数 ($\alpha=0.25, \gamma=2.0$) 引用正确，无需修改。

新增约 4 行正文，不超出 1.75 页约束。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_paper_writing_method_polish_20260528T005026"
}
```

</details>

---
