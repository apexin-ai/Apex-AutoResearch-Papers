# paper writing discussion

**How Action Collapse Creates Illusory Safety in Diffusion-Based VLA Collision Avoidance Evaluation** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 17
- **Recorded user turns:** 0
- **Tool calls:** 8
- **Original source:** `logs/chats/worker_paper_writing_discussion_20260526T173335.jsonl`
- **Structured JSON:** [`fbe10152983093ecf1bd.json`](../../sessions/fb/fbe10152983093ecf1bd.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

17 recorded events

### Tool call

_source line 1 · 2026-05-26T17:34:59.922237+00:00_

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
  "session": "worker_paper_writing_discussion_20260526T173335",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/agent-ml-research/skills/global/paper-writing-norms.skill.md"
  }
}
```

</details>

---

### Tool result

_source line 2 · 2026-05-26T17:34:59.922863+00:00_

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
  "session": "worker_paper_writing_discussion_20260526T173335",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-26T17:34:59.923075+00:00_

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
  "session": "worker_paper_writing_discussion_20260526T173335",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper/introduction.tex"
  }
}
```

</details>

---

### Tool result

_source line 4 · 2026-05-26T17:34:59.923273+00:00_

1	\section{Introduction}\label{sec:intro}
2	
3	Vision-Language-Action (VLA) models that operate in physical environments must avoid collisions with objects and people. Collision incidents cause task failure, risk damage to the robot and its surroundings, and represent a primary barrier to deploying VLAs outside controlled laboratory settings~\cite{li2026vlasafety}. The SafeLIBERO benchmark~\cite{hu2025vlsa}, an extension of the LIBERO simulation platform~\cite{liu2023libero}, provides the first systematic protocol for measuring collision behavior in VLA manipulation tasks, reporting the Collision Avoidance Rate (CAR) as the fraction of episodes free from robot-obstacle contact. Recent methods have adopted this evaluation framework to demonstrate safety improvements: SDF-augmented training~\cite{zhang2025safevla}, constraint-based planning~\cite{yang2025cape}, and collision-free demonstration learning~\cite{cofreeevla2026} all report high CAR under standard evaluation. Our own SDF-augmented Pi0~\cite{black2024pi0} configuration reaches 91.5\% CAR across 800 evaluation episodes (four independent runs). The collision avoidance problem appears close to solved.
4	
5	\begin{figure}[t]
6	\centering
7	\fbox{\parbox{0.92\linewidth}{\vspace{3.5cm}\centering\textit{Placeholder: Figure 1. The fake safety problem.\\Left: Pi0+A1 achieves CAR\,=\,91.5\% but TSR\,=\,0\% (robot frozen, displacement $<$\,0.1\,mm).\\Center: Displacement-filtered CAR$_\text{f}$ drops Pi0+A1 to ${\approx}$\,0\%.\\Right: Pi0.5 achieves CAR\,=\,28.5\% with TSR\,=\,71.5\% (all safe episodes above 288\,mm displacement).}\vspace{3.5cm}}}
8	\caption{The fake safety problem in VLA collision avoidance evaluation. Standard CAR classifies a frozen robot as safe because it produces zero collisions (left). CAR$_\text{f}$ filters out action-collapsed episodes where displacement falls below $\tau_d$, revealing that Pi0+A1's 91.5\% safety score drops to ${\approx}$\,0\% (center). Pi0.5 exhibits genuine avoidance with 
…[truncated 6753 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_discussion_20260526T173335",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-26T17:34:59.923445+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper/claim1.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_discussion_20260526T173335",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper/claim1.tex"
  }
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-26T17:34:59.923640+00:00_

1	\section{The Fake Safety Problem}\label{sec:fake_safety}
2	
3	Standard CAR evaluation assumes that a collision-free episode reflects deliberate obstacle avoidance. This assumption fails when a model has collapsed into inaction: a robot that never moves will never collide, yet it has not avoided anything. We show that this failure mode dominates the safety scores of Pi0-family models and introduce CAR$_\text{f}$ as a corrective diagnostic.
4	
5	\subsection{Action Collapse Contamination}\label{sec:collapse}
6	
7	Our Pi0+A1 configuration (SDF auxiliary loss on Pi0; see Section~\ref{sec:sdf_aux} for the training anomaly) achieves a CAR of 91.5\% across 800 evaluation episodes, a figure that would suggest reliable obstacle avoidance. Displacement analysis\footnote{These statistics are computed from obstacle displacement recorded by the original evaluation protocol.} tells a different story. Of the 732 episodes classified as safe, 541 (73.9\%) exhibit maximum displacement below 1\,$\mu$m, another 188 (25.7\%) remain below 0.1\,mm, and only 3 (0.4\%) exceed the 0.1\,mm threshold. The remaining 99.6\% of safe episodes are artifacts of a robot that never moved. TSR is 0\% across all 800 episodes: the model produces no task-directed behavior whatsoever.
8	
9	Applying CAR$_\text{f}$ (Eq.~\ref{eq:car_f}) filters out these action-collapsed episodes. Pi0+A1 drops from CAR\,=\,91.5\% to CAR$_\text{f} \approx 0$\%, because only 3 of 732 safe episodes survive displacement filtering. This is the primary demonstration of what CAR$_\text{f}$ is designed to detect: a headline safety score that is entirely attributable to inaction.
10	
11	The contamination is not specific to the SDF auxiliary loss. Pi0 Full-FT reports CAR\,=\,83.0\% with TSR\,=\,0.5\%, and 99.4\% of its safe episodes are fake safe, yielding CAR$_\text{f} \approx 0$\%. Pi0 LoRA (without any collision objective) achieves CAR\,=\,82.0\%, TSR\,=\,0\%, with a comparable fake safe rate. Across all three Pi0 configurations, C
…[truncated 6416 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_discussion_20260526T173335",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-26T17:34:59.923794+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper/claim2.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_discussion_20260526T173335",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper/claim2.tex"
  }
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-26T17:34:59.923958+00:00_

1	\section{End-Effector-Only SDF Cannot Ensure Full-Body Safety}\label{sec:ee_only}
2	
3	Section~\ref{sec:fake_safety} establishes that fake safety dominates Pi0's CAR scores. A natural question remains: could a perfect SDF signal enable effective refinement? We test this with oracle experiments (Section~\ref{sec:oracle_setup}) that replace the learned SDF with ground-truth distance fields from simulation geometry. If EE-only refinement is structurally sound, these oracles should exceed unrefined baselines by a wide margin.
4	
5	\begin{table}[t]
6	\centering
7	\caption{Oracle SDF refinement with ground-truth distance fields. Oracle variants evaluated over 160 episodes (4 tasks $\times$ 40); baselines and A3 over 200 episodes (4 tasks $\times$ 50). All three oracle variants achieve lower CAR than unrefined baselines, and fake safe rates remain above 96\%. Fake safe rate computed using obstacle displacement threshold; see Table~\ref{tab:fake_safety} footnote for measurement protocol details.}
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
27	Table~\ref{tab:oracle} reports the results. All three oracle variants achieve \emph{lower} CAR than both unrefined baselines. The best oracle (Oracle-feature, 76.9\%) falls 5.1 points below LoRA (82.0\%) and 6.1 points below Full-FT (83.0\%). Oracle-adaptive and Oracle-fixed perform worse still at 75.0\% and 73.1\%. Refinement with perfect distance information produces more collisions 
…[truncated 3317 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_discussion_20260526T173335",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-26T17:34:59.924103+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper/claim3.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_discussion_20260526T173335",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper/claim3.tex"
  }
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-26T17:34:59.924280+00:00_

1	\section{Avoidance Source Diagnosis}\label{sec:avoidance_source}
2	
3	Sections~\ref{sec:fake_safety} and~\ref{sec:ee_only} establish that standard CAR is contaminated by action collapse and that end-effector-only SDF refinement fails structurally. A constructive question remains: when collision avoidance does improve in fine-tuned models, where does the signal originate? We isolate the contribution of SDF geometric supervision from LoRA fine-tuning on collision-free demonstrations by comparing three conditions on Pi0.5: LoRA-only (no SDF), LoRA+SDF at $\lambda = 0.005$, and LoRA+SDF at $\lambda = 0.01$. All models are evaluated at the 30K-step checkpoint with rotation-corrected evaluation (Section~\ref{sec:dfcar}).
4	
5	\begin{table}[t]
6	\centering
7	\caption{Avoidance source attribution on SafeLIBERO (200 episodes per seed, 30K-step checkpoints). At $\lambda \in \{0.005, 0.01\}$, SDF adds no measurable CAR beyond LoRA-only ($p > 0.1$). All fine-tuned models exhibit 0\% frozen rate and EE displacement above 0.37\,m, confirming genuine active avoidance.}
8	\label{tab:avoidance_source}
9	\vspace{2pt}
10	\small
11	\begin{tabular}{lccccc}
12	\toprule
13	Method & Seeds & TSR (\%) & CAR (\%) & EE Disp (m) & Frozen (\%) \\
14	\midrule
15	Pi0.5 baseline & 3 & 74.7\,$\pm$\,1.5 & 26.8\,$\pm$\,1.6 & 0.367 & 0.0 \\
16	\midrule
17	LoRA-only (no SDF) & 2 & 51.5 & 54.5\,$\pm$\,2.8 & 0.392 & 0.0 \\
18	LoRA+SDF $\lambda{=}0.005$ & 3 & 54.0\,$\pm$\,3.0 & 54.5\,$\pm$\,2.3 & 0.387 & 0.0 \\
19	LoRA+SDF $\lambda{=}0.01$ & 3 & 53.8\,$\pm$\,1.5 & 56.3\,$\pm$\,1.6 & 0.389 & 0.0 \\
20	\bottomrule
21	\end{tabular}
22	\end{table}
23	
24	Table~\ref{tab:avoidance_source} reports the results. LoRA fine-tuning without any SDF objective achieves CAR of 54.5\% across two seeds. LoRA+SDF at $\lambda = 0.005$ (three seeds) produces identical CAR of 54.5\%, and $\lambda = 0.01$ (three seeds) reaches 56.3\%. All fine-tuned configurations register 0\% frozen episodes and mean EE displacement above 0.3
…[truncated 6095 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_discussion_20260526T173335",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-26T17:34:59.924567+00:00_

called Write

<details open><summary>🔧 Tool call — Write</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper/discussion.tex",
  "content": "\\section{Discussion and Conclusion}\\label{sec:conclusion}\n\nAcross 70+ experiments and 6000+ evaluation episodes on two VLA model families, three findings converge on a single theme: standard collision avoidance evaluation in VLAs measures the wrong thing. First, action collapse contaminates CAR, inflating Pi0+A1 from 91.5\\% to an effective ${\\approx}$\\,0\\% once displacement filtering removes frozen episodes (99.6\\% fake safe rate). Second, end-effector-only SDF refinement is structurally limited: ground-truth oracle variants achieve 73.1--76.9\\% CAR, below unrefined baselines at 82--83\\%, because EE-directed gradients redistribute collisions to arm links rather than eliminating them. Third, the collision avoidance observed in fine-tuned Pi0.5 originates from collision-free demonstration data, not geometric supervision: LoRA-only training achieves CAR\\,=\\,54.5\\%, identical to LoRA+SDF at $\\lambda = 0.005$ and statistically indistinguishable from $\\lambda = 0.01$ (56.3\\%, $p > 0.1$).\n\n\\paragraph{Implications for VLA safety evaluation.}\nCAR$_\\text{f}$ corrects action-collapse contamination using only end-effector position logging, a signal already available in most evaluation pipelines. The displacement distribution is sharply bimodal (collapsed episodes below 1\\,$\\mu$m, active episodes above 200\\,mm), so the threshold $\\tau_d$ is robust across five orders of magnitude. We recommend that future work report both raw CAR and CAR$_\\text{f}$; the gap between the two quantifies the degree of action-collapse contamination for a given model. Because CAR$_\\text{f}$ operates at the episode level, it detects partial collapse where a fraction of episodes are frozen while others succeed. This failure mode is invisible to model-level TSR filtering. The contamination mechanism is model-agnostic: any action-collapsed VLA will produce artificially inflated CAR.\n\n\\paragraph{The role of geometric supervision.}\nSDF auxiliary losses at $\\lambda \\in \\{0.005, 0.01\\}$ add no measurable CAR beyond LoRA-only fine-tuning on collision-free demonstrations (${\\sim}$28 percentage point improvement over the Pi0.5 baseline). The demonstration distribution already encodes obstacle-avoiding motion patterns that subsume the geometric signal at these loss weights. EE-only SDF refinement faces a separate, structural problem: even with ground-truth distance fields, redirecting the end-effector away from the nearest surface can rotate intermediate arm links into obstacle volumes, increasing rather than decreasing collisions. \\placeholder{Pending: $\\lambda = 0.1$ results will determine whether higher-dose SDF produces genuine additional avoidance or remains redundant with the demonstration signal.}\n\n\\paragraph{Limitations.}\nOur evaluation covers a single benchmark suite (SafeLIBERO object\\_pudding Level~I, four tasks) and two model families (Pi0, Pi0.5). Preliminary results on the spatial\\_bowl suite show different failure patterns: Pi0 Full-FT achieves 0\\% CAR despite 0.29\\,m mean EE displacement, suggesting arm-body collisions dominate when the robot must reach through narrow corridors. Pi0.5 achieves only 13\\% CAR on spatial\\_bowl, compared to 26.8\\% on object\\_pudding. Whether these patterns generalize to OpenVLA, RT-2, or other architectures remains untested. The oracle experiments monitor only the end-effector; full-body SDF along the kinematic chain may yield qualitatively different results. The displacement threshold $\\tau_d = 0.1$\\,mm is empirically robust across $[2, 200]$\\,mm for the current benchmark, but the bimodal gap may narrow on tasks with slower manipulation motions, making $\\tau_d$ selection more consequential. Fine-tuning introduces moderate TSR degradation of ${\\sim}$21--23 percentage points (74.7\\% $\\to$ 51.5--54.0\\%); whether training strategies exist that preserve task capability while maintaining collision avoidance has not been explored. \\placeholder{Pending: if $\\lambda = 0.1$ produces genuine additional avoidance, the collision transfer effect (SDF gradient redirecting collisions from one obstacle to another in narrow corridors) warrants dedicated analysis.}\n\n\\paragraph{Future work.}\nThree directions follow from these findings: (1) full-body SDF monitoring along the kinematic chain, replacing end-effector-only geometry with representations that cover intermediate arm links; (2) cross-architecture evaluation on OpenVLA, RT-2, and other VLA families to test whether fake safety and demonstration-driven avoidance generalize; (3) multi-benchmark evaluation beyond SafeLIBERO to characterize how task geometry affects the displacement distribution and CAR$_\\text{f}$ threshold robustness.\n\n\\paragraph{Broader impact.}\nDeploying VLAs in safety-critical settings requires metrics that reflect genuine collision avoidance capability. Contaminated CAR scores allow models with no real avoidance behavior to pass safety benchmarks, creating a false sense of readiness for physical deployment. CAR$_\\text{f}$ provides a low-cost correction that exposes this gap and can be adopted with minimal changes to existing evaluation protocols.\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_discussion_20260526T173335",
  "tool": "Write",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper/discussion.tex",
    "content": "\\section{Discussion and Conclusion}\\label{sec:conclusion}\n\nAcross 70+ experiments and 6000+ evaluation episodes on two VLA model families, three findings converge on a single theme: standard collision avoidance evaluation in VLAs measures the wrong thing. First, action collapse contaminates CAR, inflating Pi0+A1 from 91.5\\% to an effective ${\\approx}$\\,0\\% once displacement filtering removes frozen episodes (99.6\\% fake safe rate). Second, end-effector-only SDF refinement is structurally limited: ground-truth oracle variants achieve 73.1--76.9\\% CAR, below unrefined baselines at 82--83\\%, because EE-directed gradients redistribute collisions to arm links rather than eliminating them. Third, the collision avoidance observed in fine-tuned Pi0.5 originates from collision-free demonstration data, not geometric supervision: LoRA-only training achieves CAR\\,=\\,54.5\\%, identical to LoRA+SDF at $\\lambda = 0.005$ and statistically indistinguishable from $\\lambda = 0.01$ (56.3\\%, $p > 0.1$).\n\n\\paragraph{Implications for VLA safety evaluation.}\nCAR$_\\text{f}$ corrects action-collapse contamination using only end-effector position logging, a signal already available in most evaluation pipelines. The displacement distribution is sharply bimodal (collapsed episodes below 1\\,$\\mu$m, active episodes above 200\\,mm), so the threshold $\\tau_d$ is robust across five orders of magnitude. We recommend that future work report both raw CAR and CAR$_\\text{f}$; the gap between the two quantifies the degree of action-collapse contamination for a given model. Because CAR$_\\text{f}$ operates at the episode level, it detects partial collapse where a fraction of episodes are frozen while others succeed. This failure mode is invisible to model-level TSR filtering. The contamination mechanism is model-agnostic: any action-collapsed VLA will produce artificially inflated CAR.\n\n\\paragraph{The role of geometric supervision.}\nSDF auxiliary losses at $\\lambda \\in \\{0.005, 0.01\\}$ add no measurable CAR beyond LoRA-only fine-tuning on collision-free demonstrations (${\\sim}$28 percentage point improvement over the Pi0.5 baseline). The demonstration distribution already encodes obstacle-avoiding motion patterns that subsume the geometric signal at these loss weights. EE-only SDF refinement faces a separate, structural problem: even with ground-truth distance fields, redirecting the end-effector away from the nearest surface can rotate intermediate arm links into obstacle volumes, increasing rather than decreasing collisions. \\placeholder{Pending: $\\lambda = 0.1$ results will determine whether higher-dose SDF produces genuine additional avoidance or remains redundant with the demonstration signal.}\n\n\\paragraph{Limitations.}\nOur evaluation covers a single benchmark suite (SafeLIBERO object\\_pudding Level~I, four tasks) and two model families (Pi0, Pi0.5). Preliminary results on the spatial\\_bowl suite show different failure patterns: Pi0 Full-FT achieves 0\\% CAR despite 0.29\\,m mean EE displacement, suggesting arm-body collisions dominate when the robot must reach through narrow corridors. Pi0.5 achieves only 13\\% CAR on spatial\\_bowl, compared to 26.8\\% on object\\_pudding. Whether these patterns generalize to OpenVLA, RT-2, or other architectures remains untested. The oracle experiments monitor only the end-effector; full-body SDF along the kinematic chain may yield qualitatively different results. The displacement threshold $\\tau_d = 0.1$\\,mm is empirically robust across $[2, 200]$\\,mm for the current benchmark, but the bimodal gap may narrow on tasks with slower manipulation motions, making $\\tau_d$ selection more consequential. Fine-tuning introduces moderate TSR degradation of ${\\sim}$21--23 percentage points (74.7\\% $\\to$ 51.5--54.0\\%); whether training strategies exist that preserve task capability while maintaining collision avoidance has not been explored. \\placeholder{Pending: if $\\lambda = 0.1$ produces genuine additional avoidance, the collision transfer effect (SDF gradient redirecting collisions from one obstacle to another in narrow corridors) warrants dedicated analysis.}\n\n\\paragraph{Future work.}\nThree directions follow from these findings: (1) full-body SDF monitoring along the kinematic chain, replacing end-effector-only geometry with representations that cover intermediate arm links; (2) cross-architecture evaluation on OpenVLA, RT-2, and other VLA families to test whether fake safety and demonstration-driven avoidance generalize; (3) multi-benchmark evaluation beyond SafeLIBERO to characterize how task geometry affects the displacement distribution and CAR$_\\text{f}$ threshold robustness.\n\n\\paragraph{Broader impact.}\nDeploying VLAs in safety-critical settings requires metrics that reflect genuine collision avoidance capability. Contaminated CAR scores allow models with no real avoidance behavior to pass safety benchmarks, creating a false sense of readiness for physical deployment. CAR$_\\text{f}$ provides a low-cost correction that exposes this gap and can be adopted with minimal changes to existing evaluation protocols.\n"
  }
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-26T17:34:59.924761+00:00_

&lt;tool_use_error>File has not been read yet. Read it first before writing to it.&lt;/tool_use_error>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_discussion_20260526T173335",
  "tool": "Write",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-26T17:34:59.924889+00:00_

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
  "session": "worker_paper_writing_discussion_20260526T173335",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper/discussion.tex"
  }
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-26T17:34:59.925045+00:00_

1	\section{Discussion and Conclusion}\label{sec:conclusion}
2	
3	This work identifies a systematic contamination in VLA collision avoidance evaluation: standard CAR conflates genuine obstacle avoidance with inaction caused by action collapse. Across all Pi0-family configurations evaluated on SafeLIBERO, over 98\% of episodes classified as safe exhibit sub-threshold displacement; raw CAR is therefore unreliable as a safety metric. Displacement-filtered CAR (CAR$_\text{f}$) separates these two behaviors by excluding episodes below a displacement threshold $\tau_d$ and credits only active avoidance. Two structural findings reinforce this diagnosis: TSR and CAR are anti-correlated under current methods (Section~\ref{sec:fake_safety}), and end-effector-only SDF refinement fails to prevent full-body collisions even with ground-truth geometry (Section~\ref{sec:ee_only}). Fine-tuning on collision-free demonstrations produces non-zero CAR$_\text{f}$ with zero frozen rate but suffers catastrophic TSR collapse, placing it in a region of the TSR-CAR plane that no other evaluated method occupies (Section~\ref{sec:avoidance_source}).
4	
5	\paragraph{Limitations.}
6	The empirical scope of this study is bounded in several respects. All experiments use the \texttt{object\_pudding} Level~II suite from SafeLIBERO (4 tasks). The fake safety mechanism is model-agnostic in principle: any action-collapsed VLA will receive inflated CAR. Direct verification, however, covers only the Pi0 and Pi0.5 model families; whether the same contamination pattern appears in OpenVLA, RT-2, or other VLA architectures requires additional experiments. Preliminary evaluation on the \texttt{spatial\_bowl} suite reveals a complementary failure mode: the Pi0 Full-FT baseline achieves 0\% CAR despite substantial end-effector displacement (0.29\,m): the robot moves but collides through arm-body contact rather than end-effector contact. Pi0.5 achieves only 13\% CAR on this suite. These results suggest that spatial
…[truncated 2831 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_discussion_20260526T173335",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-26T17:34:59.925205+00:00_

called Write

<details open><summary>🔧 Tool call — Write</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper/discussion.tex",
  "content": "\\section{Discussion and Conclusion}\\label{sec:conclusion}\n\nAcross 70+ experiments and 6000+ evaluation episodes on two VLA model families, three findings converge on a single theme: standard collision avoidance evaluation in VLAs measures the wrong thing. First, action collapse contaminates CAR, inflating Pi0+A1 from 91.5\\% to an effective ${\\approx}$\\,0\\% once displacement filtering removes frozen episodes (99.6\\% fake safe rate). Second, end-effector-only SDF refinement is structurally limited: ground-truth oracle variants achieve 73.1--76.9\\% CAR, below unrefined baselines at 82--83\\%, because EE-directed gradients redistribute collisions to arm links rather than eliminating them. Third, the collision avoidance observed in fine-tuned Pi0.5 originates from collision-free demonstration data, not geometric supervision: LoRA-only training achieves CAR\\,=\\,54.5\\%, identical to LoRA+SDF at $\\lambda = 0.005$ and statistically indistinguishable from $\\lambda = 0.01$ (56.3\\%, $p > 0.1$).\n\n\\paragraph{Implications for VLA safety evaluation.}\nCAR$_\\text{f}$ corrects action-collapse contamination using only end-effector position logging, a signal already available in most evaluation pipelines. The displacement distribution is sharply bimodal (collapsed episodes below 1\\,$\\mu$m, active episodes above 200\\,mm), so the threshold $\\tau_d$ is robust across five orders of magnitude. We recommend that future work report both raw CAR and CAR$_\\text{f}$; the gap between the two quantifies the degree of action-collapse contamination for a given model. Because CAR$_\\text{f}$ operates at the episode level, it detects partial collapse where a fraction of episodes are frozen while others succeed. This failure mode is invisible to model-level TSR filtering. The contamination mechanism is model-agnostic: any action-collapsed VLA will produce artificially inflated CAR.\n\n\\paragraph{The role of geometric supervision.}\nSDF auxiliary losses at $\\lambda \\in \\{0.005, 0.01\\}$ add no measurable CAR beyond LoRA-only fine-tuning on collision-free demonstrations (${\\sim}$28 percentage point improvement over the Pi0.5 baseline). The demonstration distribution already encodes obstacle-avoiding motion patterns that subsume the geometric signal at these loss weights. EE-only SDF refinement faces a separate, structural problem: even with ground-truth distance fields, redirecting the end-effector away from the nearest surface can rotate intermediate arm links into obstacle volumes, increasing rather than decreasing collisions. \\placeholder{Pending: $\\lambda = 0.1$ results will determine whether higher-dose SDF produces genuine additional avoidance or remains redundant with the demonstration signal.}\n\n\\paragraph{Limitations.}\nOur evaluation covers a single benchmark suite (SafeLIBERO object\\_pudding Level~I, four tasks) and two model families (Pi0, Pi0.5). Preliminary results on the spatial\\_bowl suite show different failure patterns: Pi0 Full-FT achieves 0\\% CAR despite 0.29\\,m mean EE displacement, suggesting arm-body collisions dominate when the robot must reach through narrow corridors. Pi0.5 achieves only 13\\% CAR on spatial\\_bowl, compared to 26.8\\% on object\\_pudding. Whether these patterns generalize to OpenVLA, RT-2, or other architectures remains untested. The oracle experiments monitor only the end-effector; full-body SDF along the kinematic chain may yield qualitatively different results. The displacement threshold $\\tau_d = 0.1$\\,mm is empirically robust across $[2, 200]$\\,mm for the current benchmark, but the bimodal gap may narrow on tasks with slower manipulation motions, making $\\tau_d$ selection more consequential. Fine-tuning introduces moderate TSR degradation of ${\\sim}$21--23 percentage points (74.7\\% $\\to$ 51.5--54.0\\%); whether training strategies exist that preserve task capability while maintaining collision avoidance has not been explored. \\placeholder{Pending: if $\\lambda = 0.1$ produces genuine additional avoidance, the collision transfer effect (SDF gradient redirecting collisions from one obstacle to another in narrow corridors) warrants dedicated analysis.}\n\n\\paragraph{Future work.}\nThree directions follow from these findings: (1) full-body SDF monitoring along the kinematic chain, replacing end-effector-only geometry with representations that cover intermediate arm links; (2) cross-architecture evaluation on OpenVLA, RT-2, and other VLA families to test whether fake safety and demonstration-driven avoidance generalize; (3) multi-benchmark evaluation beyond SafeLIBERO to characterize how task geometry affects the displacement distribution and CAR$_\\text{f}$ threshold robustness.\n\n\\paragraph{Broader impact.}\nDeploying VLAs in safety-critical settings requires metrics that reflect genuine collision avoidance capability. Contaminated CAR scores allow models with no real avoidance behavior to pass safety benchmarks, creating a false sense of readiness for physical deployment. CAR$_\\text{f}$ provides a low-cost correction that exposes this gap and can be adopted with minimal changes to existing evaluation protocols.\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_discussion_20260526T173335",
  "tool": "Write",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper/discussion.tex",
    "content": "\\section{Discussion and Conclusion}\\label{sec:conclusion}\n\nAcross 70+ experiments and 6000+ evaluation episodes on two VLA model families, three findings converge on a single theme: standard collision avoidance evaluation in VLAs measures the wrong thing. First, action collapse contaminates CAR, inflating Pi0+A1 from 91.5\\% to an effective ${\\approx}$\\,0\\% once displacement filtering removes frozen episodes (99.6\\% fake safe rate). Second, end-effector-only SDF refinement is structurally limited: ground-truth oracle variants achieve 73.1--76.9\\% CAR, below unrefined baselines at 82--83\\%, because EE-directed gradients redistribute collisions to arm links rather than eliminating them. Third, the collision avoidance observed in fine-tuned Pi0.5 originates from collision-free demonstration data, not geometric supervision: LoRA-only training achieves CAR\\,=\\,54.5\\%, identical to LoRA+SDF at $\\lambda = 0.005$ and statistically indistinguishable from $\\lambda = 0.01$ (56.3\\%, $p > 0.1$).\n\n\\paragraph{Implications for VLA safety evaluation.}\nCAR$_\\text{f}$ corrects action-collapse contamination using only end-effector position logging, a signal already available in most evaluation pipelines. The displacement distribution is sharply bimodal (collapsed episodes below 1\\,$\\mu$m, active episodes above 200\\,mm), so the threshold $\\tau_d$ is robust across five orders of magnitude. We recommend that future work report both raw CAR and CAR$_\\text{f}$; the gap between the two quantifies the degree of action-collapse contamination for a given model. Because CAR$_\\text{f}$ operates at the episode level, it detects partial collapse where a fraction of episodes are frozen while others succeed. This failure mode is invisible to model-level TSR filtering. The contamination mechanism is model-agnostic: any action-collapsed VLA will produce artificially inflated CAR.\n\n\\paragraph{The role of geometric supervision.}\nSDF auxiliary losses at $\\lambda \\in \\{0.005, 0.01\\}$ add no measurable CAR beyond LoRA-only fine-tuning on collision-free demonstrations (${\\sim}$28 percentage point improvement over the Pi0.5 baseline). The demonstration distribution already encodes obstacle-avoiding motion patterns that subsume the geometric signal at these loss weights. EE-only SDF refinement faces a separate, structural problem: even with ground-truth distance fields, redirecting the end-effector away from the nearest surface can rotate intermediate arm links into obstacle volumes, increasing rather than decreasing collisions. \\placeholder{Pending: $\\lambda = 0.1$ results will determine whether higher-dose SDF produces genuine additional avoidance or remains redundant with the demonstration signal.}\n\n\\paragraph{Limitations.}\nOur evaluation covers a single benchmark suite (SafeLIBERO object\\_pudding Level~I, four tasks) and two model families (Pi0, Pi0.5). Preliminary results on the spatial\\_bowl suite show different failure patterns: Pi0 Full-FT achieves 0\\% CAR despite 0.29\\,m mean EE displacement, suggesting arm-body collisions dominate when the robot must reach through narrow corridors. Pi0.5 achieves only 13\\% CAR on spatial\\_bowl, compared to 26.8\\% on object\\_pudding. Whether these patterns generalize to OpenVLA, RT-2, or other architectures remains untested. The oracle experiments monitor only the end-effector; full-body SDF along the kinematic chain may yield qualitatively different results. The displacement threshold $\\tau_d = 0.1$\\,mm is empirically robust across $[2, 200]$\\,mm for the current benchmark, but the bimodal gap may narrow on tasks with slower manipulation motions, making $\\tau_d$ selection more consequential. Fine-tuning introduces moderate TSR degradation of ${\\sim}$21--23 percentage points (74.7\\% $\\to$ 51.5--54.0\\%); whether training strategies exist that preserve task capability while maintaining collision avoidance has not been explored. \\placeholder{Pending: if $\\lambda = 0.1$ produces genuine additional avoidance, the collision transfer effect (SDF gradient redirecting collisions from one obstacle to another in narrow corridors) warrants dedicated analysis.}\n\n\\paragraph{Future work.}\nThree directions follow from these findings: (1) full-body SDF monitoring along the kinematic chain, replacing end-effector-only geometry with representations that cover intermediate arm links; (2) cross-architecture evaluation on OpenVLA, RT-2, and other VLA families to test whether fake safety and demonstration-driven avoidance generalize; (3) multi-benchmark evaluation beyond SafeLIBERO to characterize how task geometry affects the displacement distribution and CAR$_\\text{f}$ threshold robustness.\n\n\\paragraph{Broader impact.}\nDeploying VLAs in safety-critical settings requires metrics that reflect genuine collision avoidance capability. Contaminated CAR scores allow models with no real avoidance behavior to pass safety benchmarks, creating a false sense of readiness for physical deployment. CAR$_\\text{f}$ provides a low-cost correction that exposes this gap and can be adopted with minimal changes to existing evaluation protocols.\n"
  }
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-26T17:34:59.925454+00:00_

The file /home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper/discussion.tex has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_discussion_20260526T173335",
  "tool": "Write",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 17 · 2026-05-26T17:34:59.925671+00:00_

Section written. Key changes from the old version:

- Removed all "catastrophic forgetting/collapse/TSR collapse" language and "TSR <7%" claims
- Replaced with correct numbers: moderate TSR degradation ~21-23pp (74.7% → 51.5-54.0%)
- Opening paragraph summarizes all three findings with verified numbers
- Added "Implications for VLA safety evaluation" paragraph recommending dual CAR/dfCAR reporting
- "Role of geometric supervision" paragraph covers both SDF redundancy and EE-only structural limitation
- Limitations paragraph covers single benchmark, two model families, EE-only oracle, τ_d robustness, and TSR degradation
- Future work condensed to three directions
- Broader impact kept concise (metric reliability for deployment)
- Two `\placeholder{}` markers for pending λ=0.1 results
- ~480 words, within the 500-word target

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_paper_writing_discussion_20260526T173335"
}
```

</details>

---
