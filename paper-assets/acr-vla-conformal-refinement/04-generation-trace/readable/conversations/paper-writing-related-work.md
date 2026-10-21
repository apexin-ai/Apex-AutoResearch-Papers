# paper writing related work

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 35
- **Recorded user turns:** 0
- **Tool calls:** 17
- **Original source:** `logs/chats/worker_paper_writing_related_work_20260518T102014.jsonl`
- **Structured JSON:** [`0e4d2d72a5b43e458a87.json`](../../sessions/0e/0e4d2d72a5b43e458a87.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

35 recorded events

### Tool call

_source line 1 · 2026-05-18T10:23:49.798947+00:00_

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
  "session": "worker_paper_writing_related_work_20260518T102014",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/agent-ml-research/skills/global/latex-paper.skill.md"
  }
}
```

</details>

---

### Tool result

_source line 2 · 2026-05-18T10:23:49.799552+00:00_

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
  "session": "worker_paper_writing_related_work_20260518T102014",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-18T10:23:49.799746+00:00_

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
  "session": "worker_paper_writing_related_work_20260518T102014",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/agent-ml-research/skills/global/paper-writing-norms.skill.md"
  }
}
```

</details>

---

### Tool result

_source line 4 · 2026-05-18T10:23:49.800089+00:00_

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
…[truncated 4866 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_related_work_20260518T102014",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-18T10:23:49.800262+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/docs/paper/related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_related_work_20260518T102014",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/docs/paper/related_work.tex"
  }
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-18T10:23:49.800468+00:00_

1	\section{Related Work}\label{sec:related_work}
2	
3	\subsection{VLA Robustness}
4	
5	Methods for improving VLA robustness divide into training-time and inference-time approaches.
6	
7	\paragraph{Training-time methods.}
8	RobustVLA~\cite{robustvla2025} combines RL post-training with Jacobian regularization and smoothness regularization to stabilize action predictions under observation noise and action perturbations.
9	SRPO~\cite{srpo2025} applies self-referential RL fine-tuning, using the policy's own successful rollouts as references to shape rewards for failed trajectories via latent world model representations.
10	DiG-Flow~\cite{digflow2025} uses distributional discrepancy between observation and action embeddings as a gating signal to rebalance representation-level control, without modifying the flow-matching trajectory.
11	TT-VLA~\cite{liu2026ttvla} blurs the training/inference boundary by adapting VLA parameters at test time through RL with progress rewards, but still requires per-task reward design and gradient updates during deployment.
12	A shared limitation of these methods is the requirement for retraining, reward engineering, or per-task RL---making them difficult to apply as drop-in improvements to an arbitrary frozen VLA.
13	
14	\paragraph{Inference-time methods.}
15	ReconVLA~\cite{chen2026reconvla} applies conformal quantile regression to calibrate per-action uncertainty bounds and uses squared Mahalanobis distance for out-of-distribution detection, enabling uncertainty-guided action selection and proactive failure detection without retraining.
16	SC-VLA~\cite{liu2026scvla} performs online action refinement through sparse world imagination combined with residual RL, but requires task-level RL training for the correction policy.
17	VLA-Pilot~\cite{li2025vlapilot} applies evolutionary diffusion optimization guided by an MLLM verifier, achieving plug-and-play correction at the cost of 2.41\,s per control step---prohibitive for real-time manipulation.
18
…[truncated 7115 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_related_work_20260518T102014",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-18T10:23:49.800625+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/docs/paper/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_related_work_20260518T102014",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/docs/paper/introduction.tex"
  }
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-18T10:23:49.800830+00:00_

1	\section{Introduction}
2	\label{sec:intro}
3	
4	% --- Para 1: VLAs are impressive but fragile under distribution shift ---
5	Vision-Language-Action models (VLAs) that generate actions via flow matching~\cite{black2024pi0,shukor2025smolvla,lipman2023flow} have reached near-saturation on in-distribution benchmarks such as LIBERO~\cite{liu2023libero}.
6	Yet this performance masks severe fragility: visual and physical perturbations common in deployment (camera viewpoint shifts, object layout changes, robot initial-state variation) routinely degrade success by over 65 percentage points.
7	On the LIBERO+ benchmark~\cite{fei2025liberoplus}, $\pi_0$ drops from 94.2\% to 6.6\% under initial-state perturbation, and UniVLA drops from 95.2\% to 4.3\% under viewpoint changes.
8	Closing this robustness gap without retraining the base policy is a prerequisite for deploying VLAs outside tightly controlled laboratory settings.
9	
10	% --- Para 2: Existing approaches and the gap ---
11	Two lines of work address this challenge.
12	Training-time methods improve the base policy through robustness-aware objectives~\cite{srpo2025,robustvla2025,digflow2025} or test-time reinforcement learning~\cite{liu2026ttvla}, but require retraining or per-task RL and remain bounded by the training distribution.
13	Inference-time methods leave the policy frozen: ReconVLA~\cite{chen2026reconvla} applies conformal quantile regression for uncertainty quantification and out-of-distribution detection, but does not learn corrective residuals; A2C2~\cite{a2c2_2025} trains a per-step correction head on frozen VLA action chunks, but applies correction unconditionally without multi-sample selection or explicit magnitude control; VLA-Pilot~\cite{li2025vlapilot} applies evolutionary optimization over action samples, but incurs 2.41\,s per control step.
14	Despite growing interest in inference-time action refinement, fundamental design questions remain unanswered: how much does candidate selection contribute relat
…[truncated 5203 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_related_work_20260518T102014",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-18T10:23:49.800999+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/docs/paper/method.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_related_work_20260518T102014",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/docs/paper/method.tex"
  }
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-18T10:23:49.801194+00:00_

1	
2	\section{Method}
3	\label{sec:method}
4	
5	\textbf{ACR-VLA} improves actions from a frozen flow-matching VLA at inference time through a sample-then-correct pipeline (Figure~\ref{fig:pipeline}): draw $K$ action samples, select the candidate closest to the sample mean, and apply a learned residual correction bounded in magnitude. The base VLA is never retrained.
6	
7	\subsection{Problem Setup}
8	\label{sec:problem_setup}
9	
10	Let $\pi_\theta$ be a frozen flow-matching VLA that, given an observation $o_t$ (image, language instruction, proprioceptive state), generates action chunks of length $C{=}50$ in $\mathbb{R}^{d \times C}$ with $d{=}6$ (3 translation + 3 rotation). Under receding-horizon execution, only the first $H{=}5$ steps of each chunk influence the robot before re-planning, so we discard the remainder. The gripper dimension is handled separately via direct thresholding and is excluded from the pipeline.
11	
12	We instantiate ACR-VLA on SmolVLA~\cite{shukor2025smolvla}, a 450M-parameter flow-matching VLA that generates actions via learned flow matching~\cite{lipman2023flow}. Each forward pass produces a stochastic action sample, so querying $\pi_\theta$ independently $K$ times yields $K$ candidate action chunks. Our goal is to produce a single action more accurate than any individual sample, with no changes to~$\pi_\theta$. The method applies to any flow-matching VLA that supports repeated sampling.
13	
14	\subsection{Multi-Sample Selection}
15	\label{sec:selection}
16	
17	We draw $K{=}10$ action chunks from $\pi_\theta$ via independent flow-matching rollouts and truncate each to $H{=}5$ steps, yielding samples $\{a_h^{(k)}\}_{k=1}^K$ with $a_h^{(k)} \in \mathbb{R}^d$ for horizon step $h = 1, \dots, H$. For each step, we compute the sample mean $\boldsymbol{\mu}_h = \frac{1}{K}\sum_{k=1}^K a_h^{(k)}$ and select the sample with the smallest total $L_2$ distance to the mean across all horizon steps:
18	\begin{equation}
19	  a_{\mathrm{base}} = \argmin_{k
…[truncated 8064 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_related_work_20260518T102014",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-18T10:23:49.801485+00:00_

called Write

<details open><summary>🔧 Tool call — Write</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/docs/paper/related_work.tex",
  "content": "\\section{Related Work}\\label{sec:related_work}\n\n\\subsection{VLA Robustness}\n\nMethods for improving VLA robustness divide into training-time and inference-time approaches.\n\n\\paragraph{Training-time methods.}\nSRPO~\\cite{srpo2025} applies self-referential RL fine-tuning, using the policy's own successful rollouts as reward references for failed trajectories.\nRobustVLA~\\cite{robustvla2025} combines RL post-training with Jacobian and smoothness regularization to stabilize predictions under observation noise.\nDiG-Flow~\\cite{digflow2025} uses distributional discrepancy between observation and action embeddings as a gating signal to rebalance representation-level control.\nTT-VLA~\\cite{liu2026ttvla} adapts VLA parameters at test time through RL with progress rewards, but requires per-task reward design and gradient updates during deployment.\nAll four methods require retraining, reward engineering, or per-task RL, and cannot serve as drop-in improvements to an arbitrary frozen VLA.\n\n\\paragraph{Inference-time methods.}\nReconVLA~\\cite{chen2026reconvla} applies conformal quantile regression to calibrate per-action uncertainty bounds and Mahalanobis distance for out-of-distribution detection, but does not learn corrective residuals.\nSC-VLA~\\cite{liu2026scvla} performs online action refinement through sparse world imagination combined with residual RL, which still requires task-level RL training for the correction policy.\nVLA-Pilot~\\cite{li2025vlapilot} applies evolutionary diffusion optimization guided by an MLLM verifier at the cost of 2.41\\,s per control step, prohibitive for real-time manipulation.\nA2C2~\\cite{a2c2_2025} learns a lightweight correction head that corrects each action within a pre-generated chunk at every control step to restore closed-loop responsiveness. It applies correction unconditionally, without first selecting a high-quality starting action or controlling correction magnitude.\n\nA2C2 is the closest concurrent work to ACR-VLA: both attach a lightweight correction module to a frozen VLA without retraining the base policy. The key differences are threefold.\nFirst, ACR-VLA operates as a two-stage pipeline, where multi-sample selection (choosing the candidate closest to the sample mean by $L_2$ distance) precedes bounded residual correction, whereas A2C2 applies per-step correction directly without a selection stage.\nSecond, ACR-VLA enforces explicit magnitude control via $L_2$ norm clipping, which our ablations show is critical for preventing compounding correction errors (Section~\\ref{sec:magnitude_results}).\nThird, ACR-VLA conditions the correction module on the frozen VLA's observation embedding rather than temporal action features.\nOur perdof ablation variant additionally conditions on conformal uncertainty features~\\cite{braun2025cgs,angelopoulos2023gentle}, but observation-only conditioning proves sufficient and more robust across magnitude bounds (Section~\\ref{sec:ablation}).\n\n\\subsection{Residual Policy Learning}\n\nResidual policy learning augments a base controller with a learned additive correction.\nSilver et al.~\\cite{silver2018residual} introduced the framework for classical controllers with zero-initialization to ensure the learned residual starts from the base policy's behavior.\nSubsequent work has focused on controlling residual magnitude, since unconstrained corrections lead to compounding error and policy collapse.\nTRANSIC~\\cite{jiang2024transic} uses a learned binary gate conditioned on the current state to selectively enable sim-to-real residual actions; ungated correction causes model collapse.\nPLD~\\cite{xiao2026pld} freezes the VLA backbone and trains lightweight residual actors with bounded corrections ($[-\\xi, \\xi]$) via off-policy RL, then distills improved trajectories back into the base model.\nDRC~\\cite{pan2025drc} applies exponential decay to each expert correction event, allowing corrective signals to persist and fade over time.\n\nMagnitude control is the key connection to ACR-VLA.\nSilver et al.\\ use zero-initialization, TRANSIC uses binary gating, PLD uses fixed action bounds, and DRC uses exponential decay.\nACR-VLA uses fixed $L_2$ norm clipping, the simplest possible scheme, yet our ablations show that the choice of clipping threshold $\\varepsilon$ has an outsized effect on performance, with the optimal value varying across task suites (Section~\\ref{sec:experiments}).\nThis suggests that magnitude control in VLA inference-time correction is an underexplored design axis.\nA second distinction separates ACR-VLA from all four methods: each requires RL training (reward functions, environment interaction, or on-policy rollouts), whereas ACR-VLA's correction module is trained with supervised $L_2$ loss on offline demonstration data, with no need for reward design or environment access.\n\n\\subsection{Inference-Time Compute Scaling}\n\nTest-time compute scaling has emerged as a powerful axis for improving language model performance without additional training.\nSnell et al.~\\cite{snell2024scaling} show that allocating more compute at inference time through best-of-N sampling with a verifier can match or exceed the gains from larger models, establishing a compute-optimal framework for test-time scaling.\nRoVer~\\cite{dai2025rover} extends this to reward-free settings by using self-verification to select among multiple candidate responses without an explicit reward model.\nDA-SIP~\\cite{chun2025dasip} introduces decision-aware sample importance weighting that connects optimal sample selection to downstream task loss rather than generic quality metrics.\n\nThis paradigm is beginning to transfer to embodied AI, where drawing multiple action samples from a stochastic policy is analogous to repeated sampling from a language model.\nACR-VLA instantiates this connection: at each control step, it draws $K{=}10$ samples from the frozen VLA and selects the candidate closest to the sample mean.\nThe K-value curve shows monotonic improvement from $K{=}1$ to $K{=}5$ to $K{=}10$ (Section~\\ref{sec:experiments}), consistent with the scaling behavior observed in language model test-time compute.\nThe key difference from language model settings is the absence of a learned verifier.\nACR-VLA replaces the verifier with a statistical selection criterion ($L_2$ argmin) followed by a learned correction step, a design point that may prove relevant as multi-sample VLA inference becomes more common.\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_related_work_20260518T102014",
  "tool": "Write",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/docs/paper/related_work.tex",
    "content": "\\section{Related Work}\\label{sec:related_work}\n\n\\subsection{VLA Robustness}\n\nMethods for improving VLA robustness divide into training-time and inference-time approaches.\n\n\\paragraph{Training-time methods.}\nSRPO~\\cite{srpo2025} applies self-referential RL fine-tuning, using the policy's own successful rollouts as reward references for failed trajectories.\nRobustVLA~\\cite{robustvla2025} combines RL post-training with Jacobian and smoothness regularization to stabilize predictions under observation noise.\nDiG-Flow~\\cite{digflow2025} uses distributional discrepancy between observation and action embeddings as a gating signal to rebalance representation-level control.\nTT-VLA~\\cite{liu2026ttvla} adapts VLA parameters at test time through RL with progress rewards, but requires per-task reward design and gradient updates during deployment.\nAll four methods require retraining, reward engineering, or per-task RL, and cannot serve as drop-in improvements to an arbitrary frozen VLA.\n\n\\paragraph{Inference-time methods.}\nReconVLA~\\cite{chen2026reconvla} applies conformal quantile regression to calibrate per-action uncertainty bounds and Mahalanobis distance for out-of-distribution detection, but does not learn corrective residuals.\nSC-VLA~\\cite{liu2026scvla} performs online action refinement through sparse world imagination combined with residual RL, which still requires task-level RL training for the correction policy.\nVLA-Pilot~\\cite{li2025vlapilot} applies evolutionary diffusion optimization guided by an MLLM verifier at the cost of 2.41\\,s per control step, prohibitive for real-time manipulation.\nA2C2~\\cite{a2c2_2025} learns a lightweight correction head that corrects each action within a pre-generated chunk at every control step to restore closed-loop responsiveness. It applies correction unconditionally, without first selecting a high-quality starting action or controlling correction magnitude.\n\nA2C2 is the closest concurrent work to ACR-VLA: both attach a lightweight correction module to a frozen VLA without retraining the base policy. The key differences are threefold.\nFirst, ACR-VLA operates as a two-stage pipeline, where multi-sample selection (choosing the candidate closest to the sample mean by $L_2$ distance) precedes bounded residual correction, whereas A2C2 applies per-step correction directly without a selection stage.\nSecond, ACR-VLA enforces explicit magnitude control via $L_2$ norm clipping, which our ablations show is critical for preventing compounding correction errors (Section~\\ref{sec:magnitude_results}).\nThird, ACR-VLA conditions the correction module on the frozen VLA's observation embedding rather than temporal action features.\nOur perdof ablation variant additionally conditions on conformal uncertainty features~\\cite{braun2025cgs,angelopoulos2023gentle}, but observation-only conditioning proves sufficient and more robust across magnitude bounds (Section~\\ref{sec:ablation}).\n\n\\subsection{Residual Policy Learning}\n\nResidual policy learning augments a base controller with a learned additive correction.\nSilver et al.~\\cite{silver2018residual} introduced the framework for classical controllers with zero-initialization to ensure the learned residual starts from the base policy's behavior.\nSubsequent work has focused on controlling residual magnitude, since unconstrained corrections lead to compounding error and policy collapse.\nTRANSIC~\\cite{jiang2024transic} uses a learned binary gate conditioned on the current state to selectively enable sim-to-real residual actions; ungated correction causes model collapse.\nPLD~\\cite{xiao2026pld} freezes the VLA backbone and trains lightweight residual actors with bounded corrections ($[-\\xi, \\xi]$) via off-policy RL, then distills improved trajectories back into the base model.\nDRC~\\cite{pan2025drc} applies exponential decay to each expert correction event, allowing corrective signals to persist and fade over time.\n\nMagnitude control is the key connection to ACR-VLA.\nSilver et al.\\ use zero-initialization, TRANSIC uses binary gating, PLD uses fixed action bounds, and DRC uses exponential decay.\nACR-VLA uses fixed $L_2$ norm clipping, the simplest possible scheme, yet our ablations show that the choice of clipping threshold $\\varepsilon$ has an outsized effect on performance, with the optimal value varying across task suites (Section~\\ref{sec:experiments}).\nThis suggests that magnitude control in VLA inference-time correction is an underexplored design axis.\nA second distinction separates ACR-VLA from all four methods: each requires RL training (reward functions, environment interaction, or on-policy rollouts), whereas ACR-VLA's correction module is trained with supervised $L_2$ loss on offline demonstration data, with no need for reward design or environment access.\n\n\\subsection{Inference-Time Compute Scaling}\n\nTest-time compute scaling has emerged as a powerful axis for improving language model performance without additional training.\nSnell et al.~\\cite{snell2024scaling} show that allocating more compute at inference time through best-of-N sampling with a verifier can match or exceed the gains from larger models, establishing a compute-optimal framework for test-time scaling.\nRoVer~\\cite{dai2025rover} extends this to reward-free settings by using self-verification to select among multiple candidate responses without an explicit reward model.\nDA-SIP~\\cite{chun2025dasip} introduces decision-aware sample importance weighting that connects optimal sample selection to downstream task loss rather than generic quality metrics.\n\nThis paradigm is beginning to transfer to embodied AI, where drawing multiple action samples from a stochastic policy is analogous to repeated sampling from a language model.\nACR-VLA instantiates this connection: at each control step, it draws $K{=}10$ samples from the frozen VLA and selects the candidate closest to the sample mean.\nThe K-value curve shows monotonic improvement from $K{=}1$ to $K{=}5$ to $K{=}10$ (Section~\\ref{sec:experiments}), consistent with the scaling behavior observed in language model test-time compute.\nThe key difference from language model settings is the absence of a learned verifier.\nACR-VLA replaces the verifier with a statistical selection criterion ($L_2$ argmin) followed by a learned correction step, a design point that may prove relevant as multi-sample VLA inference becomes more common.\n"
  }
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-18T10:23:49.801767+00:00_

The file /home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/docs/paper/related_work.tex has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_related_work_20260518T102014",
  "tool": "Write",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-18T10:23:49.801930+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "grep -n \"—\\|---\" /home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/docs/paper/related_work.tex",
  "description": "Check for em-dashes in the new file"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_related_work_20260518T102014",
  "tool": "Bash",
  "tool_args": {
    "command": "grep -n \"—\\|---\" /home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/docs/paper/related_work.tex",
    "description": "Check for em-dashes in the new file"
  }
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-18T10:23:49.802061+00:00_

(Bash completed with no output)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_related_work_20260518T102014",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-18T10:23:49.802181+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "grep -n \" -- \" /home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/docs/paper/related_work.tex",
  "description": "Check for explanatory en-dashes"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_related_work_20260518T102014",
  "tool": "Bash",
  "tool_args": {
    "command": "grep -n \" -- \" /home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/docs/paper/related_work.tex",
    "description": "Check for explanatory en-dashes"
  }
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-18T10:23:49.802316+00:00_

(Bash completed with no output)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_related_work_20260518T102014",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-18T10:23:49.802436+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "grep -nE \"ing[.,;]?\\s*$\" /home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/docs/paper/related_work.tex",
  "description": "Check for -ing phrase endings at end of lines"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_related_work_20260518T102014",
  "tool": "Bash",
  "tool_args": {
    "command": "grep -nE \"ing[.,;]?\\s*$\" /home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/docs/paper/related_work.tex",
    "description": "Check for -ing phrase endings at end of lines"
  }
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-18T10:23:49.802553+00:00_

43:Test-time compute scaling has emerged as a powerful axis for improving language model performance without additional training.
44:Snell et al.~\cite{snell2024scaling} show that allocating more compute at inference time through best-of-N sampling with a verifier can match or exceed the gains from larger models, establishing a compute-optimal framework for test-time scaling.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_related_work_20260518T102014",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-18T10:23:49.802675+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "grep -niE \"(delve|leverage|utilize|facilitate|myriad|plethora|paradigm shift|in the realm|notably|it is worth noting)\" /home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/docs/paper/related_work.tex",
  "description": "Check for AI-style word blacklist"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_related_work_20260518T102014",
  "tool": "Bash",
  "tool_args": {
    "command": "grep -niE \"(delve|leverage|utilize|facilitate|myriad|plethora|paradigm shift|in the realm|notably|it is worth noting)\" /home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/docs/paper/related_work.tex",
    "description": "Check for AI-style word blacklist"
  }
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-18T10:23:49.802791+00:00_

(Bash completed with no output)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_related_work_20260518T102014",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 21 · 2026-05-18T10:23:49.802938+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/docs/paper/related_work.tex",
  "old_string": "Snell et al.~\\cite{snell2024scaling} show that allocating more compute at inference time through best-of-N sampling with a verifier can match or exceed the gains from larger models, establishing a compute-optimal framework for test-time scaling.",
  "new_string": "Snell et al.~\\cite{snell2024scaling} show that allocating more compute at inference time through best-of-N sampling with a verifier can match or exceed the gains from larger models and establish a compute-optimal framework for test-time scaling."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_related_work_20260518T102014",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/docs/paper/related_work.tex",
    "old_string": "Snell et al.~\\cite{snell2024scaling} show that allocating more compute at inference time through best-of-N sampling with a verifier can match or exceed the gains from larger models, establishing a compute-optimal framework for test-time scaling.",
    "new_string": "Snell et al.~\\cite{snell2024scaling} show that allocating more compute at inference time through best-of-N sampling with a verifier can match or exceed the gains from larger models and establish a compute-optimal framework for test-time scaling."
  }
}
```

</details>

---

### Tool result

_source line 22 · 2026-05-18T10:23:49.803085+00:00_

The file /home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/docs/paper/related_work.tex has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_related_work_20260518T102014",
  "tool": "Edit",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 23 · 2026-05-18T10:23:49.803215+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "grep -n \", [a-z]*ing \" /home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/docs/paper/related_work.tex | grep -v \"\\\\\\\\cite\\|clipping\\|conditioning\\|matching\\|missing\\|existing\\|gating\\|string\"",
  "description": "Check for comma + -ing participial phrase patterns"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_related_work_20260518T102014",
  "tool": "Bash",
  "tool_args": {
    "command": "grep -n \", [a-z]*ing \" /home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/docs/paper/related_work.tex | grep -v \"\\\\\\\\cite\\|clipping\\|conditioning\\|matching\\|missing\\|existing\\|gating\\|string\"",
    "description": "Check for comma + -ing participial phrase patterns"
  }
}
```

</details>

---

### Tool result

_source line 24 · 2026-05-18T10:23:49.803357+00:00_

(Bash completed with no output)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_related_work_20260518T102014",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 25 · 2026-05-18T10:23:49.803471+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": ", [a-z]+ing ",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/docs/paper/related_work.tex",
  "output_mode": "content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_related_work_20260518T102014",
  "tool": "Grep",
  "tool_args": {
    "pattern": ", [a-z]+ing ",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/docs/paper/related_work.tex",
    "output_mode": "content"
  }
}
```

</details>

---

### Tool result

_source line 26 · 2026-05-18T10:23:49.803585+00:00_

8:SRPO~\cite{srpo2025} applies self-referential RL fine-tuning, using the policy's own successful rollouts as reward references for failed trajectories.
33:DRC~\cite{pan2025drc} applies exponential decay to each expert correction event, allowing corrective signals to persist and fade over time.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_related_work_20260518T102014",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 27 · 2026-05-18T10:23:49.803728+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/docs/paper/related_work.tex",
  "old_string": "SRPO~\\cite{srpo2025} applies self-referential RL fine-tuning, using the policy's own successful rollouts as reward references for failed trajectories.",
  "new_string": "SRPO~\\cite{srpo2025} applies self-referential RL fine-tuning and uses the policy's own successful rollouts as reward references for failed trajectories."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_related_work_20260518T102014",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/docs/paper/related_work.tex",
    "old_string": "SRPO~\\cite{srpo2025} applies self-referential RL fine-tuning, using the policy's own successful rollouts as reward references for failed trajectories.",
    "new_string": "SRPO~\\cite{srpo2025} applies self-referential RL fine-tuning and uses the policy's own successful rollouts as reward references for failed trajectories."
  }
}
```

</details>

---

### Tool result

_source line 28 · 2026-05-18T10:23:49.803878+00:00_

The file /home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/docs/paper/related_work.tex has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_related_work_20260518T102014",
  "tool": "Edit",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 29 · 2026-05-18T10:23:49.803997+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/docs/paper/related_work.tex",
  "old_string": "DRC~\\cite{pan2025drc} applies exponential decay to each expert correction event, allowing corrective signals to persist and fade over time.",
  "new_string": "DRC~\\cite{pan2025drc} applies exponential decay to each expert correction event so that corrective signals persist and fade over time."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_related_work_20260518T102014",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/docs/paper/related_work.tex",
    "old_string": "DRC~\\cite{pan2025drc} applies exponential decay to each expert correction event, allowing corrective signals to persist and fade over time.",
    "new_string": "DRC~\\cite{pan2025drc} applies exponential decay to each expert correction event so that corrective signals persist and fade over time."
  }
}
```

</details>

---

### Tool result

_source line 30 · 2026-05-18T10:23:49.804137+00:00_

The file /home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/docs/paper/related_work.tex has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_related_work_20260518T102014",
  "tool": "Edit",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 31 · 2026-05-18T10:23:49.804279+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/docs/paper/related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_related_work_20260518T102014",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/docs/paper/related_work.tex"
  }
}
```

</details>

---

### Tool result

_source line 32 · 2026-05-18T10:23:49.804441+00:00_

1	\section{Related Work}\label{sec:related_work}
2	
3	\subsection{VLA Robustness}
4	
5	Methods for improving VLA robustness divide into training-time and inference-time approaches.
6	
7	\paragraph{Training-time methods.}
8	SRPO~\cite{srpo2025} applies self-referential RL fine-tuning and uses the policy's own successful rollouts as reward references for failed trajectories.
9	RobustVLA~\cite{robustvla2025} combines RL post-training with Jacobian and smoothness regularization to stabilize predictions under observation noise.
10	DiG-Flow~\cite{digflow2025} uses distributional discrepancy between observation and action embeddings as a gating signal to rebalance representation-level control.
11	TT-VLA~\cite{liu2026ttvla} adapts VLA parameters at test time through RL with progress rewards, but requires per-task reward design and gradient updates during deployment.
12	All four methods require retraining, reward engineering, or per-task RL, and cannot serve as drop-in improvements to an arbitrary frozen VLA.
13	
14	\paragraph{Inference-time methods.}
15	ReconVLA~\cite{chen2026reconvla} applies conformal quantile regression to calibrate per-action uncertainty bounds and Mahalanobis distance for out-of-distribution detection, but does not learn corrective residuals.
16	SC-VLA~\cite{liu2026scvla} performs online action refinement through sparse world imagination combined with residual RL, which still requires task-level RL training for the correction policy.
17	VLA-Pilot~\cite{li2025vlapilot} applies evolutionary diffusion optimization guided by an MLLM verifier at the cost of 2.41\,s per control step, prohibitive for real-time manipulation.
18	A2C2~\cite{a2c2_2025} learns a lightweight correction head that corrects each action within a pre-generated chunk at every control step to restore closed-loop responsiveness. It applies correction unconditionally, without first selecting a high-quality starting action or controlling correction magnitude.
19	
20	A2C2 is the closest concu
…[truncated 4552 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_related_work_20260518T102014",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 33 · 2026-05-18T10:23:49.804582+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__send_progress",
  "max_results": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_related_work_20260518T102014",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__send_progress",
    "max_results": "1"
  }
}
```

</details>

---

### Tool result

_source line 34 · 2026-05-18T10:23:49.804725+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_related_work_20260518T102014",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 35 · 2026-05-18T10:23:49.804899+00:00_

File written. Summary of changes:

**Structure**: 4 subsections → 3 subsections
- **VLA Robustness** (~0.4 page): Training-time (SRPO, RobustVLA, DiG-Flow, TT-VLA) and inference-time (ReconVLA, SC-VLA, VLA-Pilot, A2C2) methods, with A2C2 positioned as closest concurrent work via threefold comparison
- **Residual Policy Learning** (~0.3 page): Silver 2018, TRANSIC, PLD, DRC; magnitude control as underexplored axis; ACR-VLA's supervised L2 loss vs RL distinction
- **Inference-Time Compute Scaling** (~0.3 page): Snell et al., RoVer, DA-SIP; ACR-VLA's K-value curve as embodied AI instantiation

**D058 corrections applied**:
- All references to "Mahalanobis scoring" and "conformal selection" removed from ACR-VLA's selection description → replaced with "L2 argmin" / "candidate closest to the sample mean by L2 distance"
- Removed "Conformal Prediction in Robotics" standalone section entirely
- Removed "Uncertainty Quantification for VLAs" standalone section entirely
- Conformal features mentioned only once, as perdof ablation (line 24)
- No claim that ACR-VLA "builds upon" CGS

**Style compliance**: zero em-dashes, zero explanatory en-dashes, zero -ing participial phrase endings, zero blacklisted AI words.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_paper_writing_related_work_20260518T102014"
}
```

</details>

---
