# paper experiment section draft

**Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Factorial Analysis** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 21
- **Recorded user turns:** 0
- **Tool calls:** 10
- **Original source:** `logs/chats/worker_paper_experiment_section_draft_20260523T092013.jsonl`
- **Structured JSON:** [`79e491d3db4df133e6de.json`](../../sessions/79/79e491d3db4df133e6de.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

21 recorded events

### Tool call

_source line 1 · 2026-05-23T09:23:04.401427+00:00_

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
  "session": "worker_paper_experiment_section_draft_20260523T092013",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/agent-ml-research/skills/global/paper-writing-norms.skill.md"
  }
}
```

</details>

---

### Tool result

_source line 2 · 2026-05-23T09:23:04.402095+00:00_

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
  "session": "worker_paper_experiment_section_draft_20260523T092013",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-23T09:23:04.402324+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/docs/paper/experiments.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_experiment_section_draft_20260523T092013",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/docs/paper/experiments.tex"
  }
}
```

</details>

---

### Tool result

_source line 4 · 2026-05-23T09:23:04.402497+00:00_

1	\section{Experiments}
2	
3	\subsection{Benchmark and Tasks}
4	
5	We evaluate on the SafeLIBERO benchmark~\cite{hu2025vlsa}, which augments the LIBERO-Spatial suite with collision-aware evaluation. SafeLIBERO comprises 32 scenarios across 10 tabletop manipulation tasks organized into two difficulty levels: Level~I (basic spatial reasoning) and Level~II (complex multi-step manipulation). Each task requires the agent to reach, grasp, and place objects among surrounding obstacles. Several tasks deliberately position objects in close proximity (e.g., a bowl resting on a ramekin), creating natural collision challenges that test whether the agent can complete the instructed task without disturbing nearby objects.
6	
7	\subsection{Evaluation Protocol}
8	
9	We measure two complementary metrics aligned with the VLSA-AEGIS protocol~\cite{hu2025vlsa}. \textbf{Task Success Rate (TSR)} is the fraction of episodes in which the robot completes the instructed task. \textbf{Collision Avoidance Rate (CAR)} is the fraction of episodes with zero unintended object displacement, computed as $\text{CAR} = 1 - n_{\text{collide}} / N$, where $n_{\text{collide}}$ counts episodes whose maximum L1 \texttt{body\_xpos} displacement exceeds a threshold of $0.001$. For each of the 10 tasks, we run 50 rollouts per seed (500 episodes per seed). Seeds vary by condition (2--4 seeds; see Table~\ref{tab:main_results}). We report mean and standard deviation across seeds.
10	
11	\subsection{Experimental Conditions}
12	
13	We design six conditions that form a mechanism ablation chain, progressively isolating the role of occupancy-grounded gradient flow:
14	
15	\begin{itemize}[nosep,leftmargin=*]
16	  \item \textbf{Vanilla}: OpenVLA-OFT fine-tuned without any auxiliary supervision (baseline).
17	  \item \textbf{Full OCC}: BEV occupancy auxiliary head with gradients flowing into the vision encoder (\texttt{occ\_detach=False}).
18	  \item \textbf{Detach OCC}: Occupancy head with detached gradients (\texttt{o
…[truncated 2584 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_experiment_section_draft_20260523T092013",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-23T09:23:04.402696+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/docs/paper/discussion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_experiment_section_draft_20260523T092013",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/docs/paper/discussion.tex"
  }
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-23T09:23:04.402907+00:00_

1	
2	\section{Discussion}
3	\label{sec:discussion}
4	
5	\subsection{Why Does Gradient Flow Improve Collision Avoidance?}
6	\label{sec:why_gradient}
7	
8	The ablation results reveal a consistent pattern: conditions with auxiliary gradient flow through the vision encoder (Full OCC at 0.797 CAR, Random OCC at 0.789) remain comparable to Vanilla (0.780), while Detach OCC (0.746) falls well below all others. The dominant effect is not that gradient flow \emph{improves} CAR above Vanilla, but that its \emph{absence} degrades CAR below Vanilla. Three candidate mechanisms can explain this ``damage prevention'' pattern.
9	
10	\textbf{Hypothesis 1: Anti-overfitting regularization.}
11	Auxiliary gradients prevent the vision encoder from overfitting to the action prediction objective, preserving more general spatial features in the DINOv2 and SigLIP representations. Multi-task learning theory predicts this effect: shared representations trained on multiple objectives retain broader feature diversity than those specialized to a single task~\cite{caruana1997multitask, ruder2017overview}. Lippl and Lindsey~\cite{lippl2024implicit} show that multi-task training in overparameterized networks induces $\ell_{1,2}$ mixed-norm regularization that encourages feature sharing, while single-task fine-tuning exhibits nested feature selection that discards unused pretrained features. Under this hypothesis, Random OCC and Full OCC both regularize because both supply non-trivial gradients through the encoder---the label content matters less than the gradient signal itself. The observation that Full OCC (0.797) and Random OCC (0.789) achieve nearly identical CAR (0.8pp difference, 3 seeds each) is consistent with this account. However, the current data more strongly support a ``damage prevention'' framing than a ``positive regularization'' framing: gradient-flow conditions do not clearly exceed Vanilla, but their absence clearly harms performance.
12	
13	\textbf{Hypothesis 2: Optimization landsc
…[truncated 13535 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_experiment_section_draft_20260523T092013",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-23T09:23:04.403167+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/docs/paper/experiments.tex",
  "old_string": "\\noindent The chain Vanilla $\\to$ Random OCC $\\to$ Depth $\\to$ Detach OCC $\\to$ Full OCC isolates, in turn, auxiliary regularization, geometric supervision, and occupancy-specific gradient flow. The Cutoff condition additionally isolates the temporal requirement of auxiliary supervision.",
  "new_string": "\\noindent The chain Vanilla $\\to$ Random OCC $\\to$ Depth $\\to$ Detach OCC $\\to$ Full OCC isolates, in turn, auxiliary regularization, geometric supervision, and occupancy-specific gradient flow. The Cutoff condition additionally isolates the temporal requirement of auxiliary supervision.\n\nEach pairwise comparison isolates a single experimental factor. Vanilla vs.\\ Full OCC tests whether occupancy supervision affects collision behavior. Full OCC vs.\\ Detach OCC holds architecture and labels constant while toggling gradient flow, isolating the causal role of encoder-level gradient routing. Full OCC vs.\\ Random OCC preserves architecture and gradient flow while replacing structured labels with random binary targets, isolating the contribution of label content. Full OCC vs.\\ Depth substitutes the allocentric BEV reference frame with egocentric depth supervision, isolating the spatial representation. The Cutoff condition selectively disables gradient flow partway through training, isolating the temporal extent of auxiliary supervision. This factorial structure ensures that each mechanism (gradient flow, label content, spatial reference frame, temporal duration) is tested by exactly one controlled comparison."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_experiment_section_draft_20260523T092013",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/docs/paper/experiments.tex",
    "old_string": "\\noindent The chain Vanilla $\\to$ Random OCC $\\to$ Depth $\\to$ Detach OCC $\\to$ Full OCC isolates, in turn, auxiliary regularization, geometric supervision, and occupancy-specific gradient flow. The Cutoff condition additionally isolates the temporal requirement of auxiliary supervision.",
    "new_string": "\\noindent The chain Vanilla $\\to$ Random OCC $\\to$ Depth $\\to$ Detach OCC $\\to$ Full OCC isolates, in turn, auxiliary regularization, geometric supervision, and occupancy-specific gradient flow. The Cutoff condition additionally isolates the temporal requirement of auxiliary supervision.\n\nEach pairwise comparison isolates a single experimental factor. Vanilla vs.\\ Full OCC tests whether occupancy supervision affects collision behavior. Full OCC vs.\\ Detach OCC holds architecture and labels constant while toggling gradient flow, isolating the causal role of encoder-level gradient routing. Full OCC vs.\\ Random OCC preserves architecture and gradient flow while replacing structured labels with random binary targets, isolating the contribution of label content. Full OCC vs.\\ Depth substitutes the allocentric BEV reference frame with egocentric depth supervision, isolating the spatial representation. The Cutoff condition selectively disables gradient flow partway through training, isolating the temporal extent of auxiliary supervision. This factorial structure ensures that each mechanism (gradient flow, label content, spatial reference frame, temporal duration) is tested by exactly one controlled comparison."
  }
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-23T09:23:04.403351+00:00_

The file /home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/docs/paper/experiments.tex has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_experiment_section_draft_20260523T092013",
  "tool": "Edit",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-23T09:23:04.403482+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/docs/paper/discussion.tex",
  "old_string": "The TSR instability reveals a second consequence of gradient detachment.",
  "new_string": "Gradient analysis at convergence provides complementary evidence. In gradient-flow conditions (Full OCC, Random OCC, Depth, Cutoff), the action head's gradient norm at the encoder remains comparable to Vanilla; the auxiliary pathway does not suppress the primary learning signal. In the Detach condition, the action gradient norm is substantially lower than in all gradient-flow conditions. This pattern is consistent with the forward-pass interference account: the auxiliary head's BatchNorm layers perturb encoder feature statistics, and without compensating auxiliary gradients, the encoder converges to a region where action gradients are attenuated. Action and occupancy gradients are approximately orthogonal (cosine similarity near zero); this orthogonality implies that the auxiliary task provides an independent gradient direction rather than a competing signal for the action objective. Ongoing experiments replace the auxiliary head's BatchNorm with LayerNorm in the Detach configuration to disentangle the normalization artifact from the gradient-flow effect.\n\nThe TSR instability reveals a second consequence of gradient detachment."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_experiment_section_draft_20260523T092013",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/docs/paper/discussion.tex",
    "old_string": "The TSR instability reveals a second consequence of gradient detachment.",
    "new_string": "Gradient analysis at convergence provides complementary evidence. In gradient-flow conditions (Full OCC, Random OCC, Depth, Cutoff), the action head's gradient norm at the encoder remains comparable to Vanilla; the auxiliary pathway does not suppress the primary learning signal. In the Detach condition, the action gradient norm is substantially lower than in all gradient-flow conditions. This pattern is consistent with the forward-pass interference account: the auxiliary head's BatchNorm layers perturb encoder feature statistics, and without compensating auxiliary gradients, the encoder converges to a region where action gradients are attenuated. Action and occupancy gradients are approximately orthogonal (cosine similarity near zero); this orthogonality implies that the auxiliary task provides an independent gradient direction rather than a competing signal for the action objective. Ongoing experiments replace the auxiliary head's BatchNorm with LayerNorm in the Detach configuration to disentangle the normalization artifact from the gradient-flow effect.\n\nThe TSR instability reveals a second consequence of gradient detachment."
  }
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-23T09:23:04.403683+00:00_

The file /home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/docs/paper/discussion.tex has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_experiment_section_draft_20260523T092013",
  "tool": "Edit",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-23T09:23:04.403847+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/docs/paper/discussion.tex",
  "old_string": "The TSR--CAR dissociation further constrains the mechanism. Cutoff achieves the highest TSR among all conditions (0.915 vs.\\ 0.907 Vanilla), indicating that early-phase auxiliary training durably improves motor learning. Collision avoidance on the hardest tasks, however, appears sensitive to the temporal extent of gradient flow: Cutoff's aggregate CAR matches Vanilla (0.783 vs.\\ 0.780), but its Task~5 CAR collapses to 0.00. This temporal asymmetry suggests that task completion and collision avoidance depend on different aspects of encoder representation: motor skill may be encoded in features that stabilize early, while obstacle clearance depends on features that require ongoing auxiliary gradient support to maintain.\n\n\\subsection{Implications for VLA Safety}",
  "new_string": "The TSR--CAR dissociation further constrains the mechanism. Cutoff achieves the highest TSR among all conditions (0.915 vs.\\ 0.907 Vanilla), indicating that early-phase auxiliary training durably improves motor learning. Collision avoidance on the hardest tasks, however, appears sensitive to the temporal extent of gradient flow: Cutoff's aggregate CAR matches Vanilla (0.783 vs.\\ 0.780), but its Task~5 CAR collapses to 0.00. This temporal asymmetry suggests that task completion and collision avoidance depend on different aspects of encoder representation: motor skill may be encoded in features that stabilize early, while obstacle clearance depends on features that require ongoing auxiliary gradient support to maintain.\n\nThe current analysis tests a single temporal schedule (gradient flow for the first 35{,}000 of 50{,}000 steps). Two additional conditions are in progress to map the dose-response relationship more precisely. A Cutoff@25K condition disables gradient flow after 25{,}000 steps to identify the minimum exposure duration required for the auxiliary signal to take effect. A reverse cutoff condition withholds auxiliary gradients during early training and enables them only during the final phase; this tests whether late-stage gradient flow alone is sufficient. Together with the existing Cutoff@35K data, these conditions will trace the temporal sensitivity curve and determine whether the critical window lies in early training, late training, or spans the full schedule. \\textit{[Results to be added upon completion of 3-seed runs.]}\n\n\\subsection{Implications for VLA Safety}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_experiment_section_draft_20260523T092013",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/docs/paper/discussion.tex",
    "old_string": "The TSR--CAR dissociation further constrains the mechanism. Cutoff achieves the highest TSR among all conditions (0.915 vs.\\ 0.907 Vanilla), indicating that early-phase auxiliary training durably improves motor learning. Collision avoidance on the hardest tasks, however, appears sensitive to the temporal extent of gradient flow: Cutoff's aggregate CAR matches Vanilla (0.783 vs.\\ 0.780), but its Task~5 CAR collapses to 0.00. This temporal asymmetry suggests that task completion and collision avoidance depend on different aspects of encoder representation: motor skill may be encoded in features that stabilize early, while obstacle clearance depends on features that require ongoing auxiliary gradient support to maintain.\n\n\\subsection{Implications for VLA Safety}",
    "new_string": "The TSR--CAR dissociation further constrains the mechanism. Cutoff achieves the highest TSR among all conditions (0.915 vs.\\ 0.907 Vanilla), indicating that early-phase auxiliary training durably improves motor learning. Collision avoidance on the hardest tasks, however, appears sensitive to the temporal extent of gradient flow: Cutoff's aggregate CAR matches Vanilla (0.783 vs.\\ 0.780), but its Task~5 CAR collapses to 0.00. This temporal asymmetry suggests that task completion and collision avoidance depend on different aspects of encoder representation: motor skill may be encoded in features that stabilize early, while obstacle clearance depends on features that require ongoing auxiliary gradient support to maintain.\n\nThe current analysis tests a single temporal schedule (gradient flow for the first 35{,}000 of 50{,}000 steps). Two additional conditions are in progress to map the dose-response relationship more precisely. A Cutoff@25K condition disables gradient flow after 25{,}000 steps to identify the minimum exposure duration required for the auxiliary signal to take effect. A reverse cutoff condition withholds auxiliary gradients during early training and enables them only during the final phase; this tests whether late-stage gradient flow alone is sufficient. Together with the existing Cutoff@35K data, these conditions will trace the temporal sensitivity curve and determine whether the critical window lies in early training, late training, or spans the full schedule. \\textit{[Results to be added upon completion of 3-seed runs.]}\n\n\\subsection{Implications for VLA Safety}"
  }
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-23T09:23:04.404039+00:00_

The file /home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/docs/paper/discussion.tex has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_experiment_section_draft_20260523T092013",
  "tool": "Edit",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-23T09:23:04.404178+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/docs/paper/experiments.tex",
  "offset": "22",
  "limit": "10"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_experiment_section_draft_20260523T092013",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/docs/paper/experiments.tex",
    "offset": "22",
    "limit": "10"
  }
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-23T09:23:04.404318+00:00_

22	\end{itemize}
23	
24	\noindent The chain Vanilla $\to$ Random OCC $\to$ Depth $\to$ Detach OCC $\to$ Full OCC isolates, in turn, auxiliary regularization, geometric supervision, and occupancy-specific gradient flow. The Cutoff condition additionally isolates the temporal requirement of auxiliary supervision.
25	
26	Each pairwise comparison isolates a single experimental factor. Vanilla vs.\ Full OCC tests whether occupancy supervision affects collision behavior. Full OCC vs.\ Detach OCC holds architecture and labels constant while toggling gradient flow, isolating the causal role of encoder-level gradient routing. Full OCC vs.\ Random OCC preserves architecture and gradient flow while replacing structured labels with random binary targets, isolating the contribution of label content. Full OCC vs.\ Depth substitutes the allocentric BEV reference frame with egocentric depth supervision, isolating the spatial representation. The Cutoff condition selectively disables gradient flow partway through training, isolating the temporal extent of auxiliary supervision. This factorial structure ensures that each mechanism (gradient flow, label content, spatial reference frame, temporal duration) is tested by exactly one controlled comparison.
27	
28	\subsection{Implementation Details}
29	
30	All conditions share the same base model: OpenVLA-OFT 7B~\cite{kim2025oft}, pre-trained on Open X-Embodiment. We fine-tune with LoRA (rank 32, $\alpha{=}16$) for 50K steps using AdamW (weight decay $0.01$), a batch size of 8, a constant learning rate of $5 \times 10^{-4}$, and 2--4 random seeds per condition (see Table~\ref{tab:main_results}). The LoRA adapter adds 110.8M trainable parameters (1.45\% of 7.65B total).
31	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_experiment_section_draft_20260523T092013",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-23T09:23:04.404454+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/docs/paper/discussion.tex",
  "offset": "24",
  "limit": "12"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_experiment_section_draft_20260523T092013",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/docs/paper/discussion.tex",
    "offset": "24",
    "limit": "12"
  }
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-23T09:23:04.404592+00:00_

24	Detach OCC produces the lowest CAR (0.746) among all conditions, falling 3.4 percentage points below Vanilla (0.780), and exhibits uniquely high TSR variance ($\sigma = 0.163$ vs.\ $< 0.050$ for all other conditions). This result may appear surprising: the Detach condition has identical architecture and forward computation to Full OCC, differing only in gradient routing.
25	
26	The primary mechanism is forward-pass interference without compensating gradient signal. The auxiliary head contains BatchNorm2d layers that consume encoder feature statistics during the forward pass, modifying the batch-level statistics that the encoder representations are conditioned on. In the Full OCC and Random OCC conditions, the auxiliary loss sends gradients back through the encoder that allow it to adapt to these statistics---effectively co-optimizing the shared representations. With \texttt{stop\_gradient}, the encoder receives gradients from $\mathcal{L}_\text{action}$ alone and cannot adapt to the statistical perturbation introduced by the auxiliary head's forward computation. The encoder bears the cost of the auxiliary pathway (altered batch statistics, additional forward computation) without receiving the auxiliary-task training benefit that gradient flow provides. The 3.4pp CAR deficit relative to Vanilla, consistent across 3 seeds ($\sigma = 0.002$), confirms that gradient flow is a necessary condition for the auxiliary task to avoid harming performance.
27	
28	Gradient analysis at convergence provides complementary evidence. In gradient-flow conditions (Full OCC, Random OCC, Depth, Cutoff), the action head's gradient norm at the encoder remains comparable to Vanilla; the auxiliary pathway does not suppress the primary learning signal. In the Detach condition, the action gradient norm is substantially lower than in all gradient-flow conditions. This pattern is consistent with the forward-pass interference account: the auxiliary head's BatchNorm layers perturb encoder featur
…[truncated 1966 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_experiment_section_draft_20260523T092013",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-23T09:23:04.404805+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/docs/paper/discussion.tex",
  "offset": "42",
  "limit": "12"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_experiment_section_draft_20260523T092013",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/docs/paper/discussion.tex",
    "offset": "42",
    "limit": "12"
  }
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-23T09:23:04.404959+00:00_

42	
43	\subsection{Implications for VLA Safety}
44	\label{sec:implications}
45	
46	\textbf{Practical recommendation.} The central finding is a necessary condition rather than a benefit: if practitioners attach an auxiliary head to the vision encoder during VLA fine-tuning, gradients \emph{must} flow through the encoder. Blocking gradient flow (Detach) degrades CAR by 3.4pp below the no-auxiliary baseline and destabilizes task execution. With gradient flow maintained, the auxiliary head does not significantly improve CAR beyond Vanilla (differences of 0.0--1.7pp, within cross-seed variance), but it does not harm it either---and no ground-truth spatial labels are required (Random OCC matches Full OCC at 0.8pp difference). The auxiliary head is discarded after training, adding zero inference cost.
47	
48	\textbf{Complementarity with runtime safety.} Our approach modifies the training signal to produce policies that collide less frequently, but provides no formal safety guarantee for any individual episode. Runtime constraint methods such as CBF-based action filtering~\cite{hu2025vlsa, raja2024ogmcbf} offer per-step guarantees but add inference cost and require access to obstacle geometry. These two strategies are complementary: auxiliary-task training reduces the frequency of unsafe action proposals, while runtime filtering can catch the remaining violations. A natural extension is to construct a barrier function that operates on the spatial features already learned by the occupancy-trained encoder, avoiding the need for explicit geometric representations at test time.
49	
50	\textbf{Zero inference cost.} Unlike existing VLA safety methods that add modules at inference~\cite{hu2025vlsa, zhang2025safevla, zhai2026cofreevla}, auxiliary spatial supervision modifies only the training phase. The auxiliary head is discarded after training, so the deployed model has identical latency, memory footprint, and computational cost to the Vanilla baseline.
51	
52	\subsection{Limitat
…[truncated 32 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_experiment_section_draft_20260523T092013",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-23T09:23:04.405115+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/docs/paper/discussion.tex",
  "offset": "37",
  "limit": "8"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_experiment_section_draft_20260523T092013",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/docs/paper/discussion.tex",
    "offset": "37",
    "limit": "8"
  }
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-23T09:23:04.405250+00:00_

37	This pattern connects to the candidate mechanisms in Section~\ref{sec:why_gradient}. Under the anti-overfitting hypothesis, removing auxiliary gradients after 35{,}000 steps allows the encoder to re-specialize toward action prediction during the final 15{,}000 steps, losing the feature diversity that continuous gradient flow preserves. Under the optimization landscape hypothesis, the loss surface may sharpen once the auxiliary loss is removed, allowing the encoder to settle into a sharper minimum during late training. Both accounts predict that collision avoidance on the most physically constrained tasks---where the policy must maintain precise clearance---would be most sensitive to late-stage gradient withdrawal, consistent with the Task~5 result.
38	
39	The TSR--CAR dissociation further constrains the mechanism. Cutoff achieves the highest TSR among all conditions (0.915 vs.\ 0.907 Vanilla), indicating that early-phase auxiliary training durably improves motor learning. Collision avoidance on the hardest tasks, however, appears sensitive to the temporal extent of gradient flow: Cutoff's aggregate CAR matches Vanilla (0.783 vs.\ 0.780), but its Task~5 CAR collapses to 0.00. This temporal asymmetry suggests that task completion and collision avoidance depend on different aspects of encoder representation: motor skill may be encoded in features that stabilize early, while obstacle clearance depends on features that require ongoing auxiliary gradient support to maintain.
40	
41	The current analysis tests a single temporal schedule (gradient flow for the first 35{,}000 of 50{,}000 steps). Two additional conditions are in progress to map the dose-response relationship more precisely. A Cutoff@25K condition disables gradient flow after 25{,}000 steps to identify the minimum exposure duration required for the auxiliary signal to take effect. A reverse cutoff condition withholds auxiliary gradients during early training and enables them only during the final phase; this
…[truncated 411 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_experiment_section_draft_20260523T092013",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 21 · 2026-05-23T09:23:04.405431+00:00_

三处编辑全部到位：

1. **experiments.tex** (line 26): 添加了 factorial design rationale 段落，逐一说明每个 pairwise comparison 隔离的单一变量（gradient flow / label content / spatial reference frame / temporal duration）。

2. **discussion.tex §5.2** (line 28): 在 BN interference 机制和 TSR instability 之间插入梯度分析证据段落。包含：gradient-flow 条件的 action gradient norm 与 Vanilla 可比、Detach 条件 substantially lower、action/OCC 梯度正交（cosine≈0）、Detach+LN 实验作为 ongoing work。措辞用 "at convergence"，未用具体倍数。

3. **discussion.tex §5.3** (line 41): 添加 dose-response 框架段落，描述 Cutoff@25K 和 reverse cutoff 两个计划实验，末尾用 `\textit{[Results to be added]}` 占位。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_paper_experiment_section_draft_20260523T092013"
}
```

</details>

---
