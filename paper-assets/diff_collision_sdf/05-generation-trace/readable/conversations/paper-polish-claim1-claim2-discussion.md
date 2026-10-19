# paper polish claim1 claim2 discussion

**How Action Collapse Creates Illusory Safety in Diffusion-Based VLA Collision Avoidance Evaluation** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 69
- **Recorded user turns:** 0
- **Tool calls:** 34
- **Original source:** `logs/chats/worker_paper_polish_claim1_claim2_discussion_20260526T062303.jsonl`
- **Structured JSON:** [`206ed60d8a589659c070.json`](../../sessions/20/206ed60d8a589659c070.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

69 recorded events

### Tool call

_source line 1 · 2026-05-26T06:28:09.890249+00:00_

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
  "session": "worker_paper_polish_claim1_claim2_discussion_20260526T062303",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/agent-ml-research/skills/global/paper-writing-norms.skill.md"
  }
}
```

</details>

---

### Tool result

_source line 2 · 2026-05-26T06:28:09.890969+00:00_

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
  "session": "worker_paper_polish_claim1_claim2_discussion_20260526T062303",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-26T06:28:09.891162+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__read_project_file",
  "max_results": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_polish_claim1_claim2_discussion_20260526T062303",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__read_project_file",
    "max_results": "1"
  }
}
```

</details>

---

### Tool result

_source line 4 · 2026-05-26T06:28:09.891300+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_polish_claim1_claim2_discussion_20260526T062303",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-26T06:28:09.891467+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "diff_collision_sdf",
  "file": "paper_framing.md",
  "max_chars": "0"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_polish_claim1_claim2_discussion_20260526T062303",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "diff_collision_sdf",
    "file": "paper_framing.md",
    "max_chars": "0"
  }
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-26T06:28:09.891720+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/paper_framing.md\", \"content\": \"# ColliForce-VLA Paper Framing\\n\\n> 维护者: Director | 最后更新: 2026-05-26 UTC | D028: Claim 结构重组为 3 claims | Post-MVP research phase\\n\\n## Core Insight\\n\\nVLA safety 评估存在系统性缺陷：collision avoidance rate (CAR) 被 action collapse 和几何路径安全严重污染，导致 \\\"安全\\\" 指标虚高。我们通过大规模实证分析（70+ 实验, 6000+ episodes）揭示这一系统性缺陷，提出 EE displacement-filtered CAR 作为修正指标，并证明 SDF auxiliary loss 能产生真实碰撞避免——但代价极端。\\n\\n## Working Title\\n\\n\\\"Rethinking VLA Safety Evaluation: When 98% of Collision Avoidance is an Illusion\\\"\\n\\n> 聚焦评估方法论贡献（影响面广、scope-proof），SDF 作为验证工具而非主贡献\\n\\n## Target Venue\\n\\n**Primary**: CoRL 2026 Main / ICRA 2027 (用户明确要求主会)\\n**定位**: Diagnostic/evaluation methodology paper with positive method contribution\\n**Fit**: Robotics safety track — \\\"VLA safety metrics are fundamentally broken\\\" 对社区有直接影响\\n\\n## Core Claims (D028 重组: 4→3 claims)\\n\\n### Claim 1: CAR Metric Contaminated by Fake Safety (Primary — 证据强度 ★★★★★)\\n\\nStandard CAR metric is systematically contaminated by two distinct mechanisms: (a) action collapse producing frozen robots falsely counted as \\\"safe\\\", and (b) geometric path safety where capable robots happen to avoid obstacles without any avoidance behavior. \\\"Collision-free\\\" ≠ \\\"collision-avoiding.\\\"\\n\\n**Primary evidence — Action collapse (fake safety)**:\\n- 800 episodes A1 per-episode analysis: CAR=91.5%, but 99.6% of safe episodes show obstacle displacement < 0.1mm (~5nm median) — robot is frozen\\n- TSR=0% 独立确认 action collapse\\n- 术语修正 (D023): fake safety 判定以 TSR=0% + obstacle displacement < 0.1mm 双证据链为主\\n\\n**Supporting evidence — Capability-safety anti-correlation (原 Claim 2)**:\\n- Pi0.5 3-seed eval: TSR=74.7±1.5%, CAR=26.8±1.6% — 更强模型完成更多任务但碰撞更多\\n- Pi0 baseline: TSR≈0%, CAR=82% — \\\"高 CAR\\\" 来自 action collapse\\n- Capability↑ → motion↑ → collision↑; 表面安全要么是 
…[truncated 8228 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_polish_claim1_claim2_discussion_20260526T062303",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-26T06:28:09.891884+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "*.tex",
  "path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_polish_claim1_claim2_discussion_20260526T062303",
  "tool": "Glob",
  "tool_args": {
    "pattern": "*.tex",
    "path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper"
  }
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-26T06:28:09.892015+00:00_

docs/paper/_archive/method.tex
docs/paper/_archive/experiments.tex
docs/paper/_archive/conclusion_DEPRECATED.tex
docs/paper/analysis_claim4.tex
docs/paper/related_work.tex
docs/paper/appendix.tex
docs/paper/analysis_claim2.tex
docs/paper/analysis_claim3.tex
docs/paper/main.tex
docs/paper/experimental_framework.tex
docs/paper/discussion.tex
docs/paper/analysis_claim1.tex
docs/paper/introduction.tex
docs/paper/abstract.tex

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_polish_claim1_claim2_discussion_20260526T062303",
  "tool": "Glob",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-26T06:28:09.892168+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper/analysis_claim1.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_polish_claim1_claim2_discussion_20260526T062303",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper/analysis_claim1.tex"
  }
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-26T06:28:09.892355+00:00_

1	\subsection{The Fake Safety Problem}\label{sec:fake_safety}
2	
3	At first glance, the collision avoidance results for SDF-augmented VLA models appear compelling. Our A1-LoRA model (Pi0 fine-tuned with an SDF auxiliary loss) achieves a Collision Avoidance Rate (CAR) of 91.5\% across 800 evaluation episodes on the SafeLIBERO benchmark~\cite{hu2025vlsa}, a figure that would suggest reliable obstacle avoidance. Yet this headline metric conceals a fundamental problem. When we examine the end-effector displacement of the 732 episodes classified as ``safe,'' the picture changes entirely: 541 episodes (73.9\%) exhibit a maximum displacement below 1\,$\mu$m, and another 188 episodes (25.7\%) remain below 0.1\,mm. Only 3 episodes (0.4\%) show displacement above the 0.1\,mm threshold, the minimum we consider consistent with intentional motion. An independent measurement confirms the diagnosis: obstacle displacement across these episodes has a median of ${\sim}$5\,nm, consistent with numerical noise rather than physical contact. The remaining 99.6\% of safe episodes are artifacts of a robot that never moved.
4	
5	We define a safe episode as \emph{fake safe} when the maximum end-effector displacement stays below a threshold $\tau_d = 0.1$\,mm, the criterion used by the displacement-filtered CAR (Eq.~\ref{eq:car_f}). Under this definition, 729 of the 732 safe episodes produced by A1-LoRA are fake safe. An independent signal corroborates the diagnosis: TSR is 0\% across all 800 episodes, confirming that the model produces no meaningful task-directed behavior. The robot did not avoid obstacles; it avoided motion altogether. The displacement distribution, shown in Figure~\ref{fig:displacement}, clusters overwhelmingly near zero, with no meaningful spread toward the range that would indicate planned trajectories around obstacles. Table~\ref{tab:fake_safety} summarizes the fake safety statistics across all evaluated methods.
6	
7	\begin{table}[t]
8	\centering
9	\caption{Fake safety 
…[truncated 6108 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_polish_claim1_claim2_discussion_20260526T062303",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-26T06:28:09.892550+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper/analysis_claim2.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_polish_claim1_claim2_discussion_20260526T062303",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper/analysis_claim2.tex"
  }
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-26T06:28:09.892716+00:00_

1	\subsection{End-Effector-Only SDF Cannot Ensure Full-Body Safety}\label{sec:ee_only}
2	
3	The analysis in Section~\ref{sec:fake_safety} identifies action collapse and fake safety as pervasive problems, but leaves open a natural question: could a sufficiently accurate SDF prediction still enable effective runtime refinement? To isolate the SDF representation itself from prediction quality, we construct an oracle experiment. We replace the learned SDF network with the ground-truth signed distance field computed directly from the known obstacle geometry. This oracle represents the theoretical upper bound of end-effector-only SDF refinement: it eliminates prediction error entirely, providing the refinement module with a perfect distance signal at every timestep. If the SDF refinement paradigm is sound, oracle performance should exceed that of unrefined baselines by a wide margin.
4	
5	\begin{table}[t]
6	\centering
7	\caption{Oracle SDF refinement with ground-truth distance fields (160 episodes, 4 tasks $\times$ 40). All three variants achieve lower CAR than unrefined baselines (LoRA 82.0\%, Full-FT 83.0\%), and fake safe rates remain above 96\%.}
8	\label{tab:oracle}
9	\vspace{2pt}
10	\small
11	\begin{tabular}{lcccc}
12	\toprule
13	Method & TSR (\%) & CAR (\%) & Fake Safe (\%) & Refines/ep \\
14	\midrule
15	LoRA baseline (no refine) & 0.0 & 82.0 & 99.4 & -- \\
16	Full-FT baseline (no refine) & 0.5 & 83.0 & -- & -- \\
17	\midrule
18	Oracle-adaptive (GT, dyn.\ $\alpha$) & 0.0 & 75.0 & 98.3 & 14.2 \\
19	Oracle-fixed (GT, $\alpha{=}0.005$) & 0.0 & 73.1 & 98.3 & 14.8 \\
20	Oracle-feature (GT, feat.\ space) & 0.0 & 76.9 & 96.7 & 241.7 \\
21	\midrule
22	A3 learned SDF & 0.0 & 74.5 & -- & 0.0 \\
23	\bottomrule
24	\end{tabular}
25	\end{table}
26	
27	Table~\ref{tab:oracle} reports the results. All three oracle variants achieve CAR below that of the unrefined baselines. The best oracle (Oracle-feature, 76.9\%) falls 5.1 percentage points below the LoRA baseline (82.0\%) and 6.1 
…[truncated 4419 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_polish_claim1_claim2_discussion_20260526T062303",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-26T06:28:09.892868+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper/discussion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_polish_claim1_claim2_discussion_20260526T062303",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper/discussion.tex"
  }
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-26T06:28:09.893012+00:00_

1	\section{Discussion and Conclusion}\label{sec:conclusion}
2	
3	This work identifies a systematic contamination in VLA collision avoidance evaluation: standard CAR conflates genuine obstacle avoidance with inaction caused by action collapse. Across all Pi0-family configurations evaluated on SafeLIBERO, over 98\% of episodes classified as safe exhibit sub-threshold displacement, rendering raw CAR unreliable as a safety metric. Displacement-filtered CAR (CAR$_\text{f}$) separates these two behaviors by excluding episodes below a displacement threshold $\tau_d$, providing a metric that credits only active avoidance. Two structural findings reinforce this diagnosis: TSR and CAR are anti-correlated under current methods (Section~\ref{sec:fake_safety}), and end-effector-only SDF refinement fails to prevent full-body collisions even with ground-truth geometry (Section~\ref{sec:ee_only}). Fine-tuning on collision-free demonstrations produces non-zero CAR$_\text{f}$ with zero frozen rate, placing it in a region of the TSR-CAR plane that no other evaluated method occupies (Section~\ref{sec:avoidance_source}).
4	
5	\paragraph{Limitations.}
6	The empirical scope of this study is bounded in several respects. All experiments use the \texttt{object\_pudding} Level~I suite from SafeLIBERO (4 tasks). The fake safety mechanism is model-agnostic in principle: any action-collapsed VLA will receive inflated CAR. Direct verification, however, covers only the Pi0 and Pi0.5 model families; whether the same contamination pattern appears in OpenVLA, RT-2, or other VLA architectures requires additional experiments. Preliminary evaluation on the \texttt{spatial\_bowl} suite confirms this pattern: all Pi0 variants achieve 0\% CAR despite substantial end-effector displacement (0.2--0.3\,m), consistent with arm-body collisions dominating the failure mode. Pi0.5 achieves only 13\% CAR on this suite, suggesting that spatial tasks with narrow corridors pose additional challenges beyond those captur
…[truncated 2397 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_polish_claim1_claim2_discussion_20260526T062303",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-26T06:28:09.893155+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper/experimental_framework.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_polish_claim1_claim2_discussion_20260526T062303",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper/experimental_framework.tex"
  }
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-26T06:28:09.893313+00:00_

1	\section{Experimental Framework}\label{sec:framework}
2	
3	This section defines the evaluation platform, metrics, and model configurations that underpin the analyses in Sections~\ref{sec:fake_safety}--\ref{sec:avoidance_source}. Our primary methodological contribution is the displacement-filtered Collision Avoidance Rate (CAR$_\text{f}$), which separates genuine avoidance from action collapse.
4	
5	\subsection{Benchmark and Evaluation Protocol}
6	
7	We conduct all experiments on SafeLIBERO~\cite{hu2025vlsa}, a collision-aware evaluation extension of the LIBERO simulation platform~\cite{liu2023libero}. SafeLIBERO augments standard manipulation benchmarks with per-timestep collision detection and non-target obstacle annotations, enabling systematic measurement of both task completion and safety.
8	
9	We select the \textit{object\_pudding} Level~I suite, which comprises four tabletop manipulation tasks. In each task, a target object is surrounded by non-target obstacles that the robot must avoid during grasping and transport. The MuJoCo physics engine provides collision detection: any contact between the robot (end-effector or arm links) and a non-target object registers as a collision event.
10	
11	Each method is evaluated for 50 episodes per task (200 episodes total). For multi-seed experiments (Pi0.5), we run 3 seeds to produce 600 episodes per configuration. Initial object configurations are fixed across methods to ensure fair comparison.
12	
13	\subsection{Evaluation Metrics}\label{sec:metrics}
14	
15	\paragraph{Standard metrics.} We report two conventional metrics. The \emph{Task Success Rate} (TSR) is the fraction of episodes where the manipulation task reaches completion. The \emph{Collision Avoidance Rate} (CAR) is the fraction of episodes in which no collision occurs between the robot and any non-target object.
16	
17	\paragraph{Displacement-filtered CAR.} Standard CAR conflates two qualitatively distinct behaviors: a robot that plans a trajectory around ob
…[truncated 4599 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_polish_claim1_claim2_discussion_20260526T062303",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-26T06:28:09.893514+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper/main.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_polish_claim1_claim2_discussion_20260526T062303",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper/main.tex"
  }
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-26T06:28:09.893694+00:00_

1	\documentclass[10pt,letterpaper]{article}
2	
3	\usepackage[margin=1in]{geometry}
4	\usepackage{amsmath,amssymb}
5	\usepackage{booktabs}
6	\usepackage{graphicx}
7	\usepackage{hyperref}
8	\usepackage{natbib}
9	\usepackage{xcolor}
10	\usepackage{multirow}
11	\graphicspath{{../../artifacts/figures/}}
12	
13	\newcommand{\placeholder}[1]{\textcolor{red}{\textbf{[#1]}}}
14	
15	\bibliographystyle{plainnat}
16	
17	\title{The Safety Illusion: How Action Collapse Contaminates\\Collision Avoidance Metrics in Vision-Language-Action Models}
18	
19	\author{
20	  Anonymous Authors
21	}
22	
23	\date{}
24	
25	\begin{document}
26	
27	\maketitle
28	
29	\input{abstract}
30	
31	\input{introduction}
32	
33	\input{related_work}
34	
35	\input{experimental_framework}
36	
37	\section{Analysis}\label{sec:analysis}
38	
39	\input{analysis_claim1}
40	
41	\begin{figure}[t]
42	\centering
43	\fbox{\parbox{0.9\linewidth}{\centering\vspace{2em}[Displacement distribution histogram — pending]\vspace{2em}}}
44	\caption{End-effector displacement distribution for A1-LoRA. The overwhelming majority of safe episodes cluster below 1\,$\mu$m, indicating action collapse rather than planned avoidance.}
45	\label{fig:displacement}
46	\end{figure}
47	
48	\begin{figure}[t]
49	\centering
50	\includegraphics[width=\linewidth]{fig_tsr_car_scatter.pdf}
51	\caption{TSR vs.\ CAR for all evaluated methods. The shaded region in the upper-left marks the ``fake safety'' zone where high CAR reflects action collapse rather than obstacle avoidance. Pi0-family models (circles) and oracle variants (diamonds) cluster within this zone at near-zero TSR. Pi0.5 seeds (squares) occupy the lower-right with high TSR but low CAR. Pi0.5+A1 with SDF auxiliary training (stars) uniquely occupies the center region with both moderate TSR and meaningful CAR. The arrow indicates the effect of SDF auxiliary training, shifting from the Pi0.5 baseline toward higher CAR at moderate TSR cost. No evaluated method occupies the upper-right quadrant (hi
…[truncated 881 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_polish_claim1_claim2_discussion_20260526T062303",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-26T06:28:09.893848+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "Claim [0-9]|claim [0-9]|Claim~[0-9]",
  "path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper",
  "output_mode": "content",
  "glob": "*.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_polish_claim1_claim2_discussion_20260526T062303",
  "tool": "Grep",
  "tool_args": {
    "pattern": "Claim [0-9]|claim [0-9]|Claim~[0-9]",
    "path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper",
    "output_mode": "content",
    "glob": "*.tex"
  }
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-26T06:28:09.893980+00:00_

No matches found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_polish_claim1_claim2_discussion_20260526T062303",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 21 · 2026-05-26T06:28:09.894102+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "—|–",
  "path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper",
  "output_mode": "content",
  "glob": "*.tex",
  "-n": "True"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_polish_claim1_claim2_discussion_20260526T062303",
  "tool": "Grep",
  "tool_args": {
    "pattern": "—|–",
    "path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper",
    "output_mode": "content",
    "glob": "*.tex",
    "-n": "True"
  }
}
```

</details>

---

### Tool result

_source line 22 · 2026-05-26T06:28:09.894228+00:00_

docs/paper/main.tex:43:\fbox{\parbox{0.9\linewidth}{\centering\vspace{2em}[Displacement distribution histogram — pending]\vspace{2em}}}
docs/paper/analysis_claim1.tex:27:% TODO: pending Pi0.5 re-eval with EE displacement data — update fake safe characterization once available

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_polish_claim1_claim2_discussion_20260526T062303",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 23 · 2026-05-26T06:28:09.894362+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "---",
  "path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper",
  "output_mode": "content",
  "glob": "*.tex",
  "-n": "True"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_polish_claim1_claim2_discussion_20260526T062303",
  "tool": "Grep",
  "tool_args": {
    "pattern": "---",
    "path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper",
    "output_mode": "content",
    "glob": "*.tex",
    "-n": "True"
  }
}
```

</details>

---

### Tool result

_source line 24 · 2026-05-26T06:28:09.894505+00:00_

docs/paper/main.tex:60:\caption{Aggregate collision avoidance rate for oracle SDF refinement variants versus unrefined baselines (160 episodes). All three ground-truth oracle variants achieve lower CAR than both baselines (dashed line: baseline average), confirming that even perfect end-effector distance information---with zero prediction error---does not improve collision avoidance.}
docs/paper/analysis_claim1.tex:17:A1-LoRA (SDF) & 91.5 & 0.0 & 99.6 & 3 / 732 & ---$^\dagger$ \\
docs/paper/analysis_claim4.tex:29:[Omitted long matching line]
docs/paper/analysis_claim4.tex:33:[Omitted long matching line]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_polish_claim1_claim2_discussion_20260526T062303",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 25 · 2026-05-26T06:28:09.894628+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "claim.?4|sec:claim4|Claim 4",
  "path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper",
  "output_mode": "content",
  "glob": "*.tex",
  "-n": "True",
  "-i": "True"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_polish_claim1_claim2_discussion_20260526T062303",
  "tool": "Grep",
  "tool_args": {
    "pattern": "claim.?4|sec:claim4|Claim 4",
    "path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper",
    "output_mode": "content",
    "glob": "*.tex",
    "-n": "True",
    "-i": "True"
  }
}
```

</details>

---

### Tool result

_source line 26 · 2026-05-26T06:28:09.894749+00:00_

No matches found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_polish_claim1_claim2_discussion_20260526T062303",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 27 · 2026-05-26T06:28:09.894861+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "ing,|ing the |Furthermore|Moreover|Additionally|Notably|It is worth noting|delve|leverage|utilize|facilitate|myriad|plethora",
  "path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper",
  "output_mode": "content",
  "glob": "analysis_claim1.tex",
  "-n": "True"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_polish_claim1_claim2_discussion_20260526T062303",
  "tool": "Grep",
  "tool_args": {
    "pattern": "ing,|ing the |Furthermore|Moreover|Additionally|Notably|It is worth noting|delve|leverage|utilize|facilitate|myriad|plethora",
    "path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper",
    "output_mode": "content",
    "glob": "analysis_claim1.tex",
    "-n": "True"
  }
}
```

</details>

---

### Tool result

_source line 28 · 2026-05-26T06:28:09.894975+00:00_

docs/paper/analysis_claim1.tex:32:[Omitted long matching line]
docs/paper/analysis_claim1.tex:36:[Omitted long matching line]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_polish_claim1_claim2_discussion_20260526T062303",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 29 · 2026-05-26T06:28:09.895084+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "ing,|Furthermore|Moreover|Additionally|Notably|It is worth noting|delve|leverage|utilize|facilitate|myriad|plethora",
  "path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper",
  "output_mode": "content",
  "glob": "analysis_claim2.tex",
  "-n": "True"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_polish_claim1_claim2_discussion_20260526T062303",
  "tool": "Grep",
  "tool_args": {
    "pattern": "ing,|Furthermore|Moreover|Additionally|Notably|It is worth noting|delve|leverage|utilize|facilitate|myriad|plethora",
    "path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper",
    "output_mode": "content",
    "glob": "analysis_claim2.tex",
    "-n": "True"
  }
}
```

</details>

---

### Tool result

_source line 30 · 2026-05-26T06:28:09.895197+00:00_

No matches found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_polish_claim1_claim2_discussion_20260526T062303",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 31 · 2026-05-26T06:28:09.895306+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "ing,|Furthermore|Moreover|Additionally|Notably|It is worth noting|delve|leverage|utilize|facilitate|myriad|plethora",
  "path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper",
  "output_mode": "content",
  "glob": "discussion.tex",
  "-n": "True"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_polish_claim1_claim2_discussion_20260526T062303",
  "tool": "Grep",
  "tool_args": {
    "pattern": "ing,|Furthermore|Moreover|Additionally|Notably|It is worth noting|delve|leverage|utilize|facilitate|myriad|plethora",
    "path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper",
    "output_mode": "content",
    "glob": "discussion.tex",
    "-n": "True"
  }
}
```

</details>

---

### Tool result

_source line 32 · 2026-05-26T06:28:09.895434+00:00_

docs/paper/discussion.tex:6:[Omitted long matching line]
docs/paper/discussion.tex:12:[Omitted long matching line]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_polish_claim1_claim2_discussion_20260526T062303",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 33 · 2026-05-26T06:28:09.895553+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "ing,|Furthermore|Moreover|Additionally|Notably|It is worth noting|delve|leverage|utilize|facilitate|myriad|plethora",
  "path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper",
  "output_mode": "content",
  "glob": "experimental_framework.tex",
  "-n": "True"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_polish_claim1_claim2_discussion_20260526T062303",
  "tool": "Grep",
  "tool_args": {
    "pattern": "ing,|Furthermore|Moreover|Additionally|Notably|It is worth noting|delve|leverage|utilize|facilitate|myriad|plethora",
    "path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper",
    "output_mode": "content",
    "glob": "experimental_framework.tex",
    "-n": "True"
  }
}
```

</details>

---

### Tool result

_source line 34 · 2026-05-26T06:28:09.895667+00:00_

No matches found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_polish_claim1_claim2_discussion_20260526T062303",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 35 · 2026-05-26T06:28:09.895787+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "ing,|Furthermore|Moreover|Additionally|Notably",
  "path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper/discussion.tex",
  "output_mode": "content",
  "-n": "True",
  "context": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_polish_claim1_claim2_discussion_20260526T062303",
  "tool": "Grep",
  "tool_args": {
    "pattern": "ing,|Furthermore|Moreover|Additionally|Notably",
    "path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper/discussion.tex",
    "output_mode": "content",
    "-n": "True",
    "context": "1"
  }
}
```

</details>

---

### Tool result

_source line 36 · 2026-05-26T06:28:09.895901+00:00_

5-\paragraph{Limitations.}
6:[Omitted long matching line]
7-
--
11-\paragraph{Broader impact.}
12:[Omitted long matching line]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_polish_claim1_claim2_discussion_20260526T062303",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 37 · 2026-05-26T06:28:09.896010+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "rendering|filtering|logging|training|testing",
  "path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper/analysis_claim1.tex",
  "output_mode": "content",
  "-n": "True"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_polish_claim1_claim2_discussion_20260526T062303",
  "tool": "Grep",
  "tool_args": {
    "pattern": "rendering|filtering|logging|training|testing",
    "path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper/analysis_claim1.tex",
    "output_mode": "content",
    "-n": "True"
  }
}
```

</details>

---

### Tool result

_source line 38 · 2026-05-26T06:28:09.896127+00:00_

32:[Omitted long matching line]
36:[Omitted long matching line]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_polish_claim1_claim2_discussion_20260526T062303",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 39 · 2026-05-26T06:28:09.896238+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper/discussion.tex",
  "offset": "5",
  "limit": "2"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_polish_claim1_claim2_discussion_20260526T062303",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper/discussion.tex",
    "offset": "5",
    "limit": "2"
  }
}
```

</details>

---

### Tool result

_source line 40 · 2026-05-26T06:28:09.896359+00:00_

5	\paragraph{Limitations.}
6	The empirical scope of this study is bounded in several respects. All experiments use the \texttt{object\_pudding} Level~I suite from SafeLIBERO (4 tasks). The fake safety mechanism is model-agnostic in principle: any action-collapsed VLA will receive inflated CAR. Direct verification, however, covers only the Pi0 and Pi0.5 model families; whether the same contamination pattern appears in OpenVLA, RT-2, or other VLA architectures requires additional experiments. Preliminary evaluation on the \texttt{spatial\_bowl} suite confirms this pattern: all Pi0 variants achieve 0\% CAR despite substantial end-effector displacement (0.2--0.3\,m), consistent with arm-body collisions dominating the failure mode. Pi0.5 achieves only 13\% CAR on this suite, suggesting that spatial tasks with narrow corridors pose additional challenges beyond those captured by the \texttt{object\_pudding} benchmark. The EE-only SDF oracle (Section~\ref{sec:ee_only}) tests end-effector-level refinement exclusively; full-body SDF monitoring along the kinematic chain may yield different outcomes. The displacement threshold $\tau_d = 0.1$\,mm is empirically robust across four orders of magnitude (Appendix~\ref{sec:appendix_threshold}), but remains task-dependent in principle. Pi0.5+A1 results are reported at the 10K-step checkpoint (seed~0); the 30K checkpoint is pending, and the final magnitude of the TSR-CAR tradeoff is not yet determined. In narrow-corridor scenarios (Task~3), SDF gradients redistribute collisions between obstacles rather than eliminate them: the point-wise gradient pushes the end-effector away from the nearest surface, but in bilateral obstacle geometries this shifts the trajectory into the opposing obstacle (Section~\ref{sec:ee_only}). This collision transfer effect defines a boundary condition for training-time SDF supervision.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_polish_claim1_claim2_discussion_20260526T062303",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 41 · 2026-05-26T06:28:09.896507+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper/discussion.tex",
  "offset": "11",
  "limit": "2"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_polish_claim1_claim2_discussion_20260526T062303",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper/discussion.tex",
    "offset": "11",
    "limit": "2"
  }
}
```

</details>

---

### Tool result

_source line 42 · 2026-05-26T06:28:09.896625+00:00_

11	\paragraph{Broader impact.}
12	Metric reliability is a prerequisite for safe deployment of autonomous manipulation systems. Contaminated evaluation metrics create a risk that models with no genuine collision avoidance capability pass safety benchmarks and proceed to deployment. Displacement filtering is a low-cost correction: it requires only end-effector position logging, no additional data collection or model modification. The analysis in this work is conducted entirely in simulation; real-world deployment introduces additional safety considerations (sensor noise, sim-to-real transfer, dynamic obstacles) that fall outside the present scope.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_polish_claim1_claim2_discussion_20260526T062303",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 43 · 2026-05-26T06:28:09.896819+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "\\\\label",
  "path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper/analysis_claim3.tex",
  "output_mode": "content",
  "-n": "True"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_polish_claim1_claim2_discussion_20260526T062303",
  "tool": "Grep",
  "tool_args": {
    "pattern": "\\\\label",
    "path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper/analysis_claim3.tex",
    "output_mode": "content",
    "-n": "True"
  }
}
```

</details>

---

### Tool result

_source line 44 · 2026-05-26T06:28:09.896948+00:00_

1:\subsection{Collision Avoidance from Demonstrations, Not Geometry}\label{sec:avoidance_source}
8:\label{tab:avoidance_source}
35:\label{fig:lambda_car}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_polish_claim1_claim2_discussion_20260526T062303",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 45 · 2026-05-26T06:28:09.897065+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "\\\\ref\\{sec:avoidance_source\\}",
  "path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper",
  "output_mode": "content",
  "glob": "*.tex",
  "-n": "True"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_polish_claim1_claim2_discussion_20260526T062303",
  "tool": "Grep",
  "tool_args": {
    "pattern": "\\\\ref\\{sec:avoidance_source\\}",
    "path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper",
    "output_mode": "content",
    "glob": "*.tex",
    "-n": "True"
  }
}
```

</details>

---

### Tool result

_source line 46 · 2026-05-26T06:28:09.897184+00:00_

docs/paper/analysis_claim2.tex:37:[Omitted long matching line]
docs/paper/discussion.tex:3:[Omitted long matching line]
docs/paper/experimental_framework.tex:3:This section defines the evaluation platform, metrics, and model configurations that underpin the analyses in Sections~\ref{sec:fake_safety}--\ref{sec:avoidance_source}. Our primary methodological contribution is the displacement-filtered Collision Avoidance Rate (CAR$_\text{f}$), which separates genuine avoidance from action collapse.
docs/paper/analysis_claim1.tex:36:[Omitted long matching line]
docs/paper/introduction.tex:19:[Omitted long matching line]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_polish_claim1_claim2_discussion_20260526T062303",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 47 · 2026-05-26T06:28:09.897300+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "10K|10k|10,000",
  "path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper",
  "output_mode": "content",
  "glob": "*.tex",
  "-n": "True"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_polish_claim1_claim2_discussion_20260526T062303",
  "tool": "Grep",
  "tool_args": {
    "pattern": "10K|10k|10,000",
    "path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper",
    "output_mode": "content",
    "glob": "*.tex",
    "-n": "True"
  }
}
```

</details>

---

### Tool result

_source line 48 · 2026-05-26T06:28:09.897433+00:00_

docs/paper/discussion.tex:6:[Omitted long matching line]
docs/paper/introduction.tex:13:[Omitted long matching line]
docs/paper/introduction.tex:19:[Omitted long matching line]
docs/paper/analysis_claim4.tex:7:\caption{Results for Pi0.5 with training-time SDF auxiliary loss on SafeLIBERO (200 episodes per configuration). Frozen rate: fraction of episodes with $d_{\max} < \tau_d$ (action collapse; Section~\ref{sec:metrics}). Pi0.5+A1 produces 0\% frozen episodes at 10K steps, so CAR$_\text{f}$ equals raw CAR.}
docs/paper/analysis_claim4.tex:18:\multicolumn{6}{l}{\textit{10K-step checkpoint (seed~0)}} \\
docs/paper/analysis_claim4.tex:29:[Omitted long matching line]
docs/paper/analysis_claim4.tex:33:[Omitted long matching line]
docs/paper/analysis_claim4.tex:37:[Omitted long matching line]
docs/paper/analysis_claim4.tex:39:[Omitted long matching line]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_polish_claim1_claim2_discussion_20260526T062303",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 49 · 2026-05-26T06:28:09.897605+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_polish_claim1_claim2_discussion_20260526T062303",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper/introduction.tex"
  }
}
```

</details>

---

### Tool result

_source line 50 · 2026-05-26T06:28:09.897761+00:00_

1	\section{Introduction}
2	
3	A model that reports 91.5\% collision avoidance and completes zero tasks has not learned safety; it has learned to stop moving.
4	
5	Vision-Language-Action (VLA) models unify visual perception, language understanding, and continuous action generation in a single architecture. Models such as $\pi_0$~\cite{black2024pi0}, OpenVLA~\cite{kim2024openvla}, and RT-2~\cite{brohan2023rt2} can follow diverse natural language instructions across manipulation tasks. As these models move toward real-world deployment, a critical failure mode has emerged: frequent collisions with non-target objects in cluttered environments. The demonstration data used for training typically features unobstructed workspaces, and the resulting policies acquire no explicit incentive to maintain clearance from nearby surfaces. Collisions cause task failure, risk damage to the robot and its surroundings, and represent a central barrier to safe deployment. The SafeLIBERO benchmark~\cite{hu2025vlsa}, comprising 32 collision scenarios across 1,600 evaluation episodes, was introduced to systematically quantify this problem and confirms that even high-performing VLAs exhibit substantial collision rates when non-target objects surround the manipulation target.
6	
7	Several recent methods target collision avoidance in VLAs. AEGIS~\cite{hu2025vlsa} applies post-hoc Control Barrier Function (CBF) corrections to already-generated trajectories and reports an average Collision Avoidance Rate (CAR) of 77.85\% across SafeLIBERO scenarios without additional training. SafeVLA~\cite{zhang2025safevla} formulates safety as a constrained Markov Decision Process and reduces safety violations by 83.58\% through reward shaping during reinforcement learning. CoFreeVLA~\cite{cofreeevla2026} trains a risk estimator for dual-arm settings that halts execution when predicted collision risk exceeds a threshold. In our own experiments, a Pi0 model fine-tuned with an auxiliary Signed Distance Field (SDF)
…[truncated 6165 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_polish_claim1_claim2_discussion_20260526T062303",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 51 · 2026-05-26T06:28:09.897925+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper/analysis_claim3.tex",
  "limit": "15"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_polish_claim1_claim2_discussion_20260526T062303",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper/analysis_claim3.tex",
    "limit": "15"
  }
}
```

</details>

---

### Tool result

_source line 52 · 2026-05-26T06:28:09.898114+00:00_

1	\subsection{Collision Avoidance from Demonstrations, Not Geometry}\label{sec:avoidance_source}
2	
3	Sections~\ref{sec:fake_safety} and~\ref{sec:ee_only} establish that standard CAR is contaminated by action collapse and that end-effector-only SDF refinement fails structurally. A constructive question remains: when collision avoidance does improve in fine-tuned models, where does the signal originate? We isolate the contribution of explicit SDF geometric supervision from that of LoRA fine-tuning on collision-free demonstration data by comparing models trained with and without the SDF auxiliary loss.
4	
5	\begin{table}[t]
6	\centering
7	\caption{Avoidance source attribution on SafeLIBERO (200 episodes per seed). LoRA fine-tuning without SDF produces CAR comparable to SDF-augmented variants; the SDF contribution is $0 \pm 3.5$ percentage points at $\lambda \in \{0.005, 0.01\}$. All fine-tuned models exhibit 0\% frozen rate, confirming active collision avoidance.}
8	\label{tab:avoidance_source}
9	\vspace{2pt}
10	\small
11	\begin{tabular}{lccccc}
12	\toprule
13	Method & Seeds & TSR (\%) & CAR (\%) & EE Disp (m) & Frozen (\%) \\
14	\midrule
15	Pi0.5 baseline & 3 & 74.7\,$\pm$\,1.5 & 26.8\,$\pm$\,1.6 & \placeholder{X.XX} & ${\sim}$26 \\

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_polish_claim1_claim2_discussion_20260526T062303",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 53 · 2026-05-26T06:28:09.898351+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper/discussion.tex",
  "old_string": "over 98\\% of episodes classified as safe exhibit sub-threshold displacement, rendering raw CAR unreliable as a safety metric.",
  "new_string": "over 98\\% of episodes classified as safe exhibit sub-threshold displacement; raw CAR is therefore unreliable as a safety metric."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_polish_claim1_claim2_discussion_20260526T062303",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper/discussion.tex",
    "old_string": "over 98\\% of episodes classified as safe exhibit sub-threshold displacement, rendering raw CAR unreliable as a safety metric.",
    "new_string": "over 98\\% of episodes classified as safe exhibit sub-threshold displacement; raw CAR is therefore unreliable as a safety metric."
  }
}
```

</details>

---

### Tool result

_source line 54 · 2026-05-26T06:28:09.898574+00:00_

The file /home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper/discussion.tex has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_polish_claim1_claim2_discussion_20260526T062303",
  "tool": "Edit",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 55 · 2026-05-26T06:28:09.898720+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper/discussion.tex",
  "old_string": "Fine-tuning on collision-free demonstrations produces non-zero CAR$_\\text{f}$ with zero frozen rate, placing it in a region of the TSR-CAR plane that no other evaluated method occupies (Section~\\ref{sec:avoidance_source}).",
  "new_string": "Fine-tuning on collision-free demonstrations produces non-zero CAR$_\\text{f}$ with zero frozen rate but suffers catastrophic TSR collapse, placing it in a region of the TSR-CAR plane that no other evaluated method occupies (Section~\\ref{sec:avoidance_source})."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_polish_claim1_claim2_discussion_20260526T062303",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper/discussion.tex",
    "old_string": "Fine-tuning on collision-free demonstrations produces non-zero CAR$_\\text{f}$ with zero frozen rate, placing it in a region of the TSR-CAR plane that no other evaluated method occupies (Section~\\ref{sec:avoidance_source}).",
    "new_string": "Fine-tuning on collision-free demonstrations produces non-zero CAR$_\\text{f}$ with zero frozen rate but suffers catastrophic TSR collapse, placing it in a region of the TSR-CAR plane that no other evaluated method occupies (Section~\\ref{sec:avoidance_source})."
  }
}
```

</details>

---

### Tool result

_source line 56 · 2026-05-26T06:28:09.898871+00:00_

The file /home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper/discussion.tex has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_polish_claim1_claim2_discussion_20260526T062303",
  "tool": "Edit",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 57 · 2026-05-26T06:28:09.898994+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper/discussion.tex",
  "old_string": "Pi0.5+A1 results are reported at the 10K-step checkpoint (seed~0); the 30K checkpoint is pending, and the final magnitude of the TSR-CAR tradeoff is not yet determined.",
  "new_string": "All fine-tuned models at 30K steps exhibit catastrophic TSR collapse (from 74.7\\% baseline to $<$7\\%), and whether alternative training schedules or regularization can retain task capability while preserving collision avoidance remains untested."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_polish_claim1_claim2_discussion_20260526T062303",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper/discussion.tex",
    "old_string": "Pi0.5+A1 results are reported at the 10K-step checkpoint (seed~0); the 30K checkpoint is pending, and the final magnitude of the TSR-CAR tradeoff is not yet determined.",
    "new_string": "All fine-tuned models at 30K steps exhibit catastrophic TSR collapse (from 74.7\\% baseline to $<$7\\%), and whether alternative training schedules or regularization can retain task capability while preserving collision avoidance remains untested."
  }
}
```

</details>

---

### Tool result

_source line 58 · 2026-05-26T06:28:09.899143+00:00_

The file /home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper/discussion.tex has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_polish_claim1_claim2_discussion_20260526T062303",
  "tool": "Edit",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 59 · 2026-05-26T06:28:09.899262+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper/discussion.tex",
  "old_string": "Four directions follow from this analysis.",
  "new_string": "Five directions follow from this analysis."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_polish_claim1_claim2_discussion_20260526T062303",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper/discussion.tex",
    "old_string": "Four directions follow from this analysis.",
    "new_string": "Five directions follow from this analysis."
  }
}
```

</details>

---

### Tool result

_source line 60 · 2026-05-26T06:28:09.899400+00:00_

The file /home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper/discussion.tex has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_polish_claim1_claim2_discussion_20260526T062303",
  "tool": "Edit",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 61 · 2026-05-26T06:28:09.899545+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper/discussion.tex",
  "old_string": "Fourth, we recommend that future VLA safety evaluations report both raw CAR and CAR$_\\text{f}$; the gap between the two quantifies the degree of action-collapse contamination in a given model.",
  "new_string": "Fourth, we recommend that future VLA safety evaluations report both raw CAR and CAR$_\\text{f}$; the gap between the two quantifies the degree of action-collapse contamination in a given model. Fifth, the catastrophic TSR collapse observed during fine-tuning (Section~\\ref{sec:avoidance_source}) motivates investigation into training strategies that preserve task capability while retaining collision avoidance learned from demonstrations."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_polish_claim1_claim2_discussion_20260526T062303",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper/discussion.tex",
    "old_string": "Fourth, we recommend that future VLA safety evaluations report both raw CAR and CAR$_\\text{f}$; the gap between the two quantifies the degree of action-collapse contamination in a given model.",
    "new_string": "Fourth, we recommend that future VLA safety evaluations report both raw CAR and CAR$_\\text{f}$; the gap between the two quantifies the degree of action-collapse contamination in a given model. Fifth, the catastrophic TSR collapse observed during fine-tuning (Section~\\ref{sec:avoidance_source}) motivates investigation into training strategies that preserve task capability while retaining collision avoidance learned from demonstrations."
  }
}
```

</details>

---

### Tool result

_source line 62 · 2026-05-26T06:28:09.899705+00:00_

The file /home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper/discussion.tex has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_polish_claim1_claim2_discussion_20260526T062303",
  "tool": "Edit",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 63 · 2026-05-26T06:28:09.899825+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper/main.tex",
  "old_string": "confirming that even perfect end-effector distance information---with zero prediction error---does not improve collision avoidance.",
  "new_string": "confirming that even perfect end-effector distance information (zero prediction error) does not improve collision avoidance."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_polish_claim1_claim2_discussion_20260526T062303",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper/main.tex",
    "old_string": "confirming that even perfect end-effector distance information---with zero prediction error---does not improve collision avoidance.",
    "new_string": "confirming that even perfect end-effector distance information (zero prediction error) does not improve collision avoidance."
  }
}
```

</details>

---

### Tool result

_source line 64 · 2026-05-26T06:28:09.899970+00:00_

The file /home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper/main.tex has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_polish_claim1_claim2_discussion_20260526T062303",
  "tool": "Edit",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 65 · 2026-05-26T06:28:09.900102+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper/discussion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_polish_claim1_claim2_discussion_20260526T062303",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper/discussion.tex"
  }
}
```

</details>

---

### Tool result

_source line 66 · 2026-05-26T06:28:09.900243+00:00_

1	\section{Discussion and Conclusion}\label{sec:conclusion}
2	
3	This work identifies a systematic contamination in VLA collision avoidance evaluation: standard CAR conflates genuine obstacle avoidance with inaction caused by action collapse. Across all Pi0-family configurations evaluated on SafeLIBERO, over 98\% of episodes classified as safe exhibit sub-threshold displacement; raw CAR is therefore unreliable as a safety metric. Displacement-filtered CAR (CAR$_\text{f}$) separates these two behaviors by excluding episodes below a displacement threshold $\tau_d$, providing a metric that credits only active avoidance. Two structural findings reinforce this diagnosis: TSR and CAR are anti-correlated under current methods (Section~\ref{sec:fake_safety}), and end-effector-only SDF refinement fails to prevent full-body collisions even with ground-truth geometry (Section~\ref{sec:ee_only}). Fine-tuning on collision-free demonstrations produces non-zero CAR$_\text{f}$ with zero frozen rate but suffers catastrophic TSR collapse, placing it in a region of the TSR-CAR plane that no other evaluated method occupies (Section~\ref{sec:avoidance_source}).
4	
5	\paragraph{Limitations.}
6	The empirical scope of this study is bounded in several respects. All experiments use the \texttt{object\_pudding} Level~I suite from SafeLIBERO (4 tasks). The fake safety mechanism is model-agnostic in principle: any action-collapsed VLA will receive inflated CAR. Direct verification, however, covers only the Pi0 and Pi0.5 model families; whether the same contamination pattern appears in OpenVLA, RT-2, or other VLA architectures requires additional experiments. Preliminary evaluation on the \texttt{spatial\_bowl} suite confirms this pattern: all Pi0 variants achieve 0\% CAR despite substantial end-effector displacement (0.2--0.3\,m), consistent with arm-body collisions dominating the failure mode. Pi0.5 achieves only 13\% CAR on this suite, suggesting that spatial tasks with narrow corridors pose 
…[truncated 2761 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_polish_claim1_claim2_discussion_20260526T062303",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 67 · 2026-05-26T06:28:09.900387+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper/main.tex",
  "offset": "57",
  "limit": "8"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_polish_claim1_claim2_discussion_20260526T062303",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper/main.tex",
    "offset": "57",
    "limit": "8"
  }
}
```

</details>

---

### Tool result

_source line 68 · 2026-05-26T06:28:09.900536+00:00_

57	\begin{figure}[t]
58	\centering
59	\includegraphics[width=\linewidth]{fig_oracle_bar.pdf}
60	\caption{Aggregate collision avoidance rate for oracle SDF refinement variants versus unrefined baselines (160 episodes). All three ground-truth oracle variants achieve lower CAR than both baselines (dashed line: baseline average), confirming that even perfect end-effector distance information (zero prediction error) does not improve collision avoidance.}
61	\label{fig:oracle_bar}
62	\end{figure}
63	
64	\input{analysis_claim3}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_polish_claim1_claim2_discussion_20260526T062303",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 69 · 2026-05-26T06:28:09.900703+00:00_

All edits verified. Here's the complete change log:

### 改动汇总

**discussion.tex** (5 处):
1. **Line 3**: `rendering raw CAR unreliable` → `; raw CAR is therefore unreliable` — 消除 trailing -ing 分词短语（AI 风格标志）
2. **Line 3**: Claim 3 summary 补充 `but suffers catastrophic TSR collapse` — 开篇总结漏提 TSR collapse 这一关键发现
3. **Line 6 (Limitations)**: `Pi0.5+A1 results are reported at the 10K-step checkpoint (seed~0); the 30K checkpoint is pending...` → 更新为 30K 已完成的 TSR collapse 事实 — 原文与 C3 数据已改为 30K 矛盾
4. **Line 9 (Future work)**: `Four` → `Five`
5. **Line 9 (Future work)**: 新增第五个方向：TSR collapse → 训练策略研究 — 原文缺失此方向

**main.tex** (1 处):
6. **Line 60 (oracle figure caption)**: `---with zero prediction error---` → `(zero prediction error)` — 消除解释性 em-dash

### 检查通过（无需改动）

- **analysis_claim1.tex**: 数据全部与 paper_framing.md 一致（A1 99.6%, Pi0.5 26.8±1.6/74.7±1.5, LoRA 82%, threshold [2,200]mm, 239mm minimum）；Pi0.5 pending‡ 标注一致；dfCAR 描述清晰；Figure/Table 交叉引用正确（`eq:car_f` → experimental_framework, `fig:displacement`/`fig:tsr_car_scatter` → main.tex, `sec:avoidance_source` → analysis_claim3）
- **analysis_claim2.tex**: 3 oracle 数据完整（75.0/73.1/76.9 vs baselines 82.0/83.0）；arm-body collision 机制描述清晰（定性，无显式比例数据）；标题和 label 反映 EE-only limitation 定位
- **experimental_framework.tex**: 无旧 claim 编号残留；dfCAR 定义与 analysis_claim1 一致
- 全文无 Claim 4 引用残留，无旧 section label

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_paper_polish_claim1_claim2_discussion_20260526T062303"
}
```

</details>

---
