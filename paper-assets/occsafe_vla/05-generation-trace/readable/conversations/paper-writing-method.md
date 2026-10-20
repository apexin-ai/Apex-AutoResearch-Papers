# paper writing method

**Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Factorial Analysis** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 49
- **Recorded user turns:** 0
- **Tool calls:** 24
- **Original source:** `logs/chats/worker_paper_writing_method_20260520T201906.jsonl`
- **Structured JSON:** [`b64b4355a4238f774836.json`](../../sessions/b6/b64b4355a4238f774836.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

49 recorded events

### Tool call

_source line 1 · 2026-05-20T20:25:13.634466+00:00_

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
  "session": "worker_paper_writing_method_20260520T201906",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/agent-ml-research/skills/global/paper-writing-norms.skill.md"
  }
}
```

</details>

---

### Tool result

_source line 2 · 2026-05-20T20:25:13.635158+00:00_

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
  "session": "worker_paper_writing_method_20260520T201906",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-20T20:25:13.635359+00:00_

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
  "session": "worker_paper_writing_method_20260520T201906",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/agent-ml-research/skills/global/latex-paper.skill.md"
  }
}
```

</details>

---

### Tool result

_source line 4 · 2026-05-20T20:25:13.635750+00:00_

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
  "session": "worker_paper_writing_method_20260520T201906",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-20T20:25:13.635931+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/*",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/docs/paper"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_method_20260520T201906",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/*",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/docs/paper"
  }
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-20T20:25:13.636060+00:00_

docs/paper/references.bib
docs/paper/experiments.tex

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_method_20260520T201906",
  "tool": "Glob",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-20T20:25:13.636209+00:00_

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
  "session": "worker_paper_writing_method_20260520T201906",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/docs/paper/experiments.tex"
  }
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-20T20:25:13.636356+00:00_

1	\section{Experiments}
2	
3	\subsection{Benchmark and Tasks}
4	
5	We evaluate on the SafeLIBERO benchmark~\cite{hu2025aegis}, which augments the LIBERO-Spatial suite with collision-aware evaluation. SafeLIBERO comprises 32 scenarios across 10 tabletop manipulation tasks organized into two difficulty levels: Level~I (basic spatial reasoning) and Level~II (complex multi-step manipulation). Each task requires the agent to reach, grasp, and place objects among surrounding obstacles. Several tasks deliberately position objects in close proximity (e.g., a bowl resting on a ramekin), creating natural collision challenges that test whether the agent can complete the instructed task without disturbing nearby objects.
6	
7	\subsection{Evaluation Protocol}
8	
9	We measure two complementary metrics aligned with the VLSA-AEGIS protocol~\cite{hu2025aegis}. \textbf{Task Success Rate (TSR)} is the fraction of episodes in which the robot completes the instructed task. \textbf{Collision Avoidance Rate (CAR)} is the fraction of episodes with zero unintended object displacement, computed as $\text{CAR} = 1 - n_{\text{collide}} / N$, where $n_{\text{collide}}$ counts episodes whose maximum L1 \texttt{body\_xpos} displacement exceeds a threshold of $0.001$. For each of the 10 tasks, we run 20 rollouts per random seed across 3 seeds (42, 43, 44), yielding 60 rollouts per task and 600 total. We report mean and 95\% confidence intervals, with paired $t$-tests and Cohen's $d$ effect sizes for pairwise comparisons.
10	
11	\subsection{Experimental Conditions}
12	
13	We design five conditions that form a mechanism ablation chain, progressively isolating the role of occupancy-grounded gradient flow:
14	
15	\begin{itemize}[nosep,leftmargin=*]
16	  \item \textbf{Vanilla}: OpenVLA-OFT fine-tuned without any auxiliary supervision (baseline).
17	  \item \textbf{+Occ}: BEV occupancy auxiliary head with gradients flowing into the vision encoder (\texttt{occ\_detach=False}).
18	  \item \textbf{+Occ-Det
…[truncated 1509 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_method_20260520T201906",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-20T20:25:13.636495+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/docs/paper/references.bib"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_method_20260520T201906",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/docs/paper/references.bib"
  }
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-20T20:25:13.636697+00:00_

1	% References for OccSafe-VLA (AAAI 2027)
2	% Auto-generated from literature_map.yaml
3	
4	% ============================================================
5	% Direct Competitors (spatial-safety intersection)
6	% ============================================================
7	
8	@article{liu2025occvla,
9	  author    = {Liu and others},
10	  title     = {{OccVLA}: Vision-Language-Action Model with Implicit 3D Occupancy Supervision},
11	  journal   = {arXiv preprint arXiv:2509.05578},
12	  year      = {2025},
13	  note      = {arXiv:2509.05578}
14	}
15	
16	@article{hu2025aegis,
17	  author    = {Hu and others},
18	  title     = {{VLSA}: Vision-Language-Action Models with Plug-and-Play Safety Constraint Layer},
19	  journal   = {arXiv preprint arXiv:2512.11891},
20	  year      = {2025},
21	  note      = {arXiv:2512.11891}
22	}
23	
24	@inproceedings{zhan2025safevla,
25	  author    = {Zhan and others},
26	  title     = {{SafeVLA}: Towards Safety Alignment of Vision-Language-Action Model via Constrained Learning},
27	  booktitle = {Advances in Neural Information Processing Systems (NeurIPS)},
28	  year      = {2025},
29	  note      = {Spotlight. arXiv:2503.03480}
30	}
31	
32	@article{chen2026cofreevla,
33	  author    = {Chen and others},
34	  title     = {{CoFreeVLA}: Collision-Free Dual-Arm Manipulation via {VLA} Model and Risk Estimation},
35	  journal   = {arXiv preprint arXiv:2601.21712},
36	  year      = {2026},
37	  note      = {arXiv:2601.21712}
38	}
39	
40	@article{safenightvla2026,
41	  author    = {Yu and others},
42	  title     = {{Safe-Night VLA}: Seeing the Unseen via Thermal-Perceptive Vision-Language-Action Models for Safety-Critical Manipulation},
43	  journal   = {arXiv preprint arXiv:2603.05754},
44	  year      = {2026},
45	  note      = {arXiv:2603.05754}
46	}
47	
48	@article{vlasafetysurvey2026,
49	  author    = {Li and others},
50	  title     = {Vision-Language-Action Safety: Threats, Challenges, Evaluations, and Mechanisms},
51	  journal   = {arXiv pre
…[truncated 7743 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_method_20260520T201906",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-20T20:25:13.637045+00:00_

called Write

<details open><summary>🔧 Tool call — Write</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/docs/paper/method.tex",
  "content": "\\section{Method}\n\\label{sec:method}\n\nWe present OccSafe-VLA, a framework that improves collision safety in Vision-Language-Action models through two complementary mechanisms. The first is a BEV occupancy auxiliary head that injects spatial awareness into the vision encoder at zero inference cost (Section~\\ref{sec:occ_head}). The second is OCC-CBF, a conceptual framework for explicit safety guarantees conditioned on learned spatial features (Section~\\ref{sec:occ_cbf}). We begin by formalizing the problem setting and evaluation metrics.\n\n\\subsection{Problem Formulation}\n\\label{sec:formulation}\n\nWe consider a \\textbf{Vision-Language-Action (VLA)} policy $\\pi(a_t \\mid o_t, l)$ that maps a visual observation $o_t$ and a language instruction $l$ to a 7-DOF action $a_t$ (delta end-effector pose) at each timestep $t$. The policy is parameterized by a large pretrained vision-language model fine-tuned on robot demonstration data. We evaluate performance along two complementary axes. \\textbf{Task Success Rate (TSR)} measures the fraction of episodes in which the robot completes the instructed task:\n\\begin{equation}\n  \\text{TSR} = \\frac{n_{\\text{success}}}{N},\n\\end{equation}\nwhere $n_{\\text{success}}$ is the number of successful episodes out of $N$ total rollouts. \\textbf{Collision Avoidance Rate (CAR)} measures the fraction of episodes free of unintended object displacement:\n\\begin{equation}\n  \\text{CAR} = 1 - \\frac{n_{\\text{collide}}}{N},\n\\end{equation}\nwhere $n_{\\text{collide}}$ counts episodes whose maximum L1 \\texttt{body\\_xpos} displacement exceeds a threshold of $0.001$, following the VLSA/AEGIS protocol~\\cite{hu2025aegis}. Our objective is to improve CAR without degrading TSR. A policy that avoids collisions by refusing to act is not useful; a practical safe manipulation policy must maintain high task completion while reducing unintended contact with surrounding objects.\n\n\\subsection{BEV Occupancy Auxiliary Head}\n\\label{sec:occ_head}\n\nModern VLA models such as OpenVLA~\\cite{kim2024openvla} and OpenVLA-OFT~\\cite{kim2025openvlaoft} rely on 2D pretrained vision encoders (DINOv2, SigLIP) that excel at semantic understanding and language grounding. These encoders learn effective semantic-to-action mappings through fine-tuning, yet they lack explicit reasoning about 3D object boundaries and free space. When a robot must navigate tight clearances between objects in cluttered scenes, this gap becomes critical. A policy that cannot distinguish occupied from free regions of the workspace will collide with obstacles even when it correctly identifies the target object. The challenge is to inject 3D spatial structure into the vision encoder without adding inference cost or sacrificing the benefits of large-scale 2D pretraining.\n\nWe address this challenge with a \\textbf{BEV occupancy auxiliary head} that predicts a bird's-eye-view occupancy grid of the workspace. The BEV representation encodes object boundaries in a view-independent, allocentric coordinate frame, providing a natural supervisory signal for spatial structure. Unlike depth maps, which remain tied to the camera viewpoint, BEV occupancy offers an explicit top-down decomposition of occupied and free space that directly corresponds to the robot's planning geometry. The head itself is a lightweight two-layer MLP with 256 hidden units that takes DINOv2 patch features as input and produces a $64 \\times 64$ binary occupancy grid. We train this head with Focal Loss to handle the class imbalance between occupied and free cells:\n\\begin{equation}\n  \\mathcal{L}_{\\text{occ}} = -\\alpha\\,(1 - p_t)^{\\gamma}\\,\\log(p_t),\n\\end{equation}\nwhere $\\alpha = 0.75$ and $\\gamma = 2.0$ are the balancing and focusing parameters, $p_t$ is the predicted probability for the ground-truth class, and the occupancy loss is weighted by $\\lambda = 0.1$ relative to the action loss.\n\nThe critical design principle is \\textbf{zero inference cost}. During training, the occupancy head forces the vision encoder to internalize spatial structure: accurate occupancy prediction requires the encoder to represent where objects begin and end in 3D space. At inference time, we discard the occupancy head entirely, and the spatial awareness acquired during training persists as an emergent property of the encoder's learned features. This paradigm of training with auxiliary geometric supervision and deploying without it has been validated in autonomous driving by OccVLA~\\cite{liu2025occvla}, which uses volumetric occupancy prediction to enhance a VLA's spatial understanding for navigation. Our work applies the same principle to tabletop manipulation, where the spatial scale and task geometry differ but the core insight holds: auxiliary occupancy supervision reshapes encoder representations to encode spatial boundaries that transfer to safer action prediction.\n\n\\subsection{Training Pipeline}\n\\label{sec:training}\n\nWe build on OpenVLA-OFT 7B~\\cite{kim2025openvlaoft} as the base model, which combines a Llama~2 language backbone with DINOv2 and SigLIP as dual vision encoders. The total training objective combines the action prediction loss with the occupancy auxiliary loss:\n\\begin{equation}\n  \\mathcal{L}_{\\text{total}} = \\mathcal{L}_{\\text{action}} + \\lambda \\cdot \\mathcal{L}_{\\text{occ}},\n\\end{equation}\nwhere $\\mathcal{L}_{\\text{action}}$ is the L1 action regression loss from OpenVLA-OFT and $\\lambda = 0.1$. The mechanism that makes occupancy supervision effective is \\textbf{gradient flow}: with \\texttt{occ\\_detach=False}, gradients from $\\mathcal{L}_{\\text{occ}}$ propagate through the occupancy head back into the DINOv2 vision encoder. This forces the encoder to develop internal representations that encode spatial structure, because producing accurate occupancy predictions requires features that capture object boundaries and spatial layout. If we instead detach the gradients (\\texttt{occ\\_detach=True}), the occupancy head becomes a passive observer that reads encoder features without modifying them, and the auxiliary loss functions as a multi-task regularizer rather than a representation shaper. This is not a subtle distinction: as we show in our ablation study (Section~4), detaching gradients eliminates the safety benefit entirely, confirming that the encoder must be directly shaped by the occupancy objective.\n\nWe fine-tune all conditions with LoRA at rank~32 for 50K steps, using a batch size of 8 and a learning rate of $5 \\times 10^{-4}$ with cosine decay. Training data consists of approximately 25K demonstration episodes from the LIBERO-Spatial suite. All hyperparameters are shared across experimental conditions to ensure fair comparison; only the auxiliary head configuration varies between conditions. Each training run completes in approximately 17 hours on a single A100 GPU.\n\n\\subsection{OCC-CBF: Occupancy-Conditioned Control Barrier Function}\n\\label{sec:occ_cbf}\n\nThe BEV occupancy auxiliary head provides implicit safety by reshaping the encoder's spatial representations at zero inference cost. In certain dense clutter scenarios, however, implicit spatial awareness alone may not guarantee collision avoidance. For such cases, we outline \\textbf{OCC-CBF}, a second line of defense that constructs an explicit safety constraint from the spatial features learned by the occupancy-trained encoder.\n\nOCC-CBF defines a learned barrier function conditioned on occupancy features. Let $z_{\\text{occ}}$ denote the spatial features extracted from the occupancy-trained vision encoder and let $x_{\\text{robot}}$ denote the robot's current state. The occupancy-conditioned barrier function takes the form:\n\\begin{equation}\n  h_{\\text{occ}}(x) = f_\\theta(z_{\\text{occ}},\\, x_{\\text{robot}}),\n\\end{equation}\nwhere $f_\\theta$ is a learned function that maps the combined feature-state pair to a scalar safety value. States satisfying $h_{\\text{occ}}(x) \\geq 0$ are considered safe, and the control barrier constraint modifies the VLA's proposed action to maintain this invariant.\n\nOCC-CBF differs from existing barrier function approaches in its use of learned volumetric features rather than hand-crafted geometric representations. The Euclidean-distance barrier in AEGIS~\\cite{hu2025aegis} operates on explicit object positions from a world model, restricting its applicability to scenarios where object states are directly observable. OGM-CBF~\\cite{ji2024ogmcbf} constructs barriers from discrete occupancy grids via signed distance fields, but relies on accurate grid-level occupancy at test time rather than learned continuous features. Learning to Nudge~\\cite{kwon2026learningnudge} trains object-centric barrier functions (DCBF) that reason about individual objects, requiring explicit object decomposition that may not scale to highly cluttered scenes. Neural CS-BF~\\cite{neuralcsbf2025} learns barriers in configuration space for manipulation planning, but operates on geometric state representations independently of a VLA's perceptual features. In contrast, OCC-CBF operates in the VLA's continuous learned feature space and can perform semantic collision reasoning without explicit object segmentation, distance computation, or a separate perception pipeline.\n\n\\textit{We defer the detailed formulation, training procedure, and experimental validation of OCC-CBF to the extended version of this paper. The experiments in Section~4 evaluate the occupancy auxiliary head in isolation, which already yields substantial safety improvements without runtime overhead.}\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_method_20260520T201906",
  "tool": "Write",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/docs/paper/method.tex",
    "content": "\\section{Method}\n\\label{sec:method}\n\nWe present OccSafe-VLA, a framework that improves collision safety in Vision-Language-Action models through two complementary mechanisms. The first is a BEV occupancy auxiliary head that injects spatial awareness into the vision encoder at zero inference cost (Section~\\ref{sec:occ_head}). The second is OCC-CBF, a conceptual framework for explicit safety guarantees conditioned on learned spatial features (Section~\\ref{sec:occ_cbf}). We begin by formalizing the problem setting and evaluation metrics.\n\n\\subsection{Problem Formulation}\n\\label{sec:formulation}\n\nWe consider a \\textbf{Vision-Language-Action (VLA)} policy $\\pi(a_t \\mid o_t, l)$ that maps a visual observation $o_t$ and a language instruction $l$ to a 7-DOF action $a_t$ (delta end-effector pose) at each timestep $t$. The policy is parameterized by a large pretrained vision-language model fine-tuned on robot demonstration data. We evaluate performance along two complementary axes. \\textbf{Task Success Rate (TSR)} measures the fraction of episodes in which the robot completes the instructed task:\n\\begin{equation}\n  \\text{TSR} = \\frac{n_{\\text{success}}}{N},\n\\end{equation}\nwhere $n_{\\text{success}}$ is the number of successful episodes out of $N$ total rollouts. \\textbf{Collision Avoidance Rate (CAR)} measures the fraction of episodes free of unintended object displacement:\n\\begin{equation}\n  \\text{CAR} = 1 - \\frac{n_{\\text{collide}}}{N},\n\\end{equation}\nwhere $n_{\\text{collide}}$ counts episodes whose maximum L1 \\texttt{body\\_xpos} displacement exceeds a threshold of $0.001$, following the VLSA/AEGIS protocol~\\cite{hu2025aegis}. Our objective is to improve CAR without degrading TSR. A policy that avoids collisions by refusing to act is not useful; a practical safe manipulation policy must maintain high task completion while reducing unintended contact with surrounding objects.\n\n\\subsection{BEV Occupancy Auxiliary Head}\n\\label{sec:occ_head}\n\nModern VLA models such as OpenVLA~\\cite{kim2024openvla} and OpenVLA-OFT~\\cite{kim2025openvlaoft} rely on 2D pretrained vision encoders (DINOv2, SigLIP) that excel at semantic understanding and language grounding. These encoders learn effective semantic-to-action mappings through fine-tuning, yet they lack explicit reasoning about 3D object boundaries and free space. When a robot must navigate tight clearances between objects in cluttered scenes, this gap becomes critical. A policy that cannot distinguish occupied from free regions of the workspace will collide with obstacles even when it correctly identifies the target object. The challenge is to inject 3D spatial structure into the vision encoder without adding inference cost or sacrificing the benefits of large-scale 2D pretraining.\n\nWe address this challenge with a \\textbf{BEV occupancy auxiliary head} that predicts a bird's-eye-view occupancy grid of the workspace. The BEV representation encodes object boundaries in a view-independent, allocentric coordinate frame, providing a natural supervisory signal for spatial structure. Unlike depth maps, which remain tied to the camera viewpoint, BEV occupancy offers an explicit top-down decomposition of occupied and free space that directly corresponds to the robot's planning geometry. The head itself is a lightweight two-layer MLP with 256 hidden units that takes DINOv2 patch features as input and produces a $64 \\times 64$ binary occupancy grid. We train this head with Focal Loss to handle the class imbalance between occupied and free cells:\n\\begin{equation}\n  \\mathcal{L}_{\\text{occ}} = -\\alpha\\,(1 - p_t)^{\\gamma}\\,\\log(p_t),\n\\end{equation}\nwhere $\\alpha = 0.75$ and $\\gamma = 2.0$ are the balancing and focusing parameters, $p_t$ is the predicted probability for the ground-truth class, and the occupancy loss is weighted by $\\lambda = 0.1$ relative to the action loss.\n\nThe critical design principle is \\textbf{zero inference cost}. During training, the occupancy head forces the vision encoder to internalize spatial structure: accurate occupancy prediction requires the encoder to represent where objects begin and end in 3D space. At inference time, we discard the occupancy head entirely, and the spatial awareness acquired during training persists as an emergent property of the encoder's learned features. This paradigm of training with auxiliary geometric supervision and deploying without it has been validated in autonomous driving by OccVLA~\\cite{liu2025occvla}, which uses volumetric occupancy prediction to enhance a VLA's spatial understanding for navigation. Our work applies the same principle to tabletop manipulation, where the spatial scale and task geometry differ but the core insight holds: auxiliary occupancy supervision reshapes encoder representations to encode spatial boundaries that transfer to safer action prediction.\n\n\\subsection{Training Pipeline}\n\\label{sec:training}\n\nWe build on OpenVLA-OFT 7B~\\cite{kim2025openvlaoft} as the base model, which combines a Llama~2 language backbone with DINOv2 and SigLIP as dual vision encoders. The total training objective combines the action prediction loss with the occupancy auxiliary loss:\n\\begin{equation}\n  \\mathcal{L}_{\\text{total}} = \\mathcal{L}_{\\text{action}} + \\lambda \\cdot \\mathcal{L}_{\\text{occ}},\n\\end{equation}\nwhere $\\mathcal{L}_{\\text{action}}$ is the L1 action regression loss from OpenVLA-OFT and $\\lambda = 0.1$. The mechanism that makes occupancy supervision effective is \\textbf{gradient flow}: with \\texttt{occ\\_detach=False}, gradients from $\\mathcal{L}_{\\text{occ}}$ propagate through the occupancy head back into the DINOv2 vision encoder. This forces the encoder to develop internal representations that encode spatial structure, because producing accurate occupancy predictions requires features that capture object boundaries and spatial layout. If we instead detach the gradients (\\texttt{occ\\_detach=True}), the occupancy head becomes a passive observer that reads encoder features without modifying them, and the auxiliary loss functions as a multi-task regularizer rather than a representation shaper. This is not a subtle distinction: as we show in our ablation study (Section~4), detaching gradients eliminates the safety benefit entirely, confirming that the encoder must be directly shaped by the occupancy objective.\n\nWe fine-tune all conditions with LoRA at rank~32 for 50K steps, using a batch size of 8 and a learning rate of $5 \\times 10^{-4}$ with cosine decay. Training data consists of approximately 25K demonstration episodes from the LIBERO-Spatial suite. All hyperparameters are shared across experimental conditions to ensure fair comparison; only the auxiliary head configuration varies between conditions. Each training run completes in approximately 17 hours on a single A100 GPU.\n\n\\subsection{OCC-CBF: Occupancy-Conditioned Control Barrier Function}\n\\label{sec:occ_cbf}\n\nThe BEV occupancy auxiliary head provides implicit safety by reshaping the encoder's spatial representations at zero inference cost. In certain dense clutter scenarios, however, implicit spatial awareness alone may not guarantee collision avoidance. For such cases, we outline \\textbf{OCC-CBF}, a second line of defense that constructs an explicit safety constraint from the spatial features learned by the occupancy-trained encoder.\n\nOCC-CBF defines a learned barrier function conditioned on occupancy features. Let $z_{\\text{occ}}$ denote the spatial features extracted from the occupancy-trained vision encoder and let $x_{\\text{robot}}$ denote the robot's current state. The occupancy-conditioned barrier function takes the form:\n\\begin{equation}\n  h_{\\text{occ}}(x) = f_\\theta(z_{\\text{occ}},\\, x_{\\text{robot}}),\n\\end{equation}\nwhere $f_\\theta$ is a learned function that maps the combined feature-state pair to a scalar safety value. States satisfying $h_{\\text{occ}}(x) \\geq 0$ are considered safe, and the control barrier constraint modifies the VLA's proposed action to maintain this invariant.\n\nOCC-CBF differs from existing barrier function approaches in its use of learned volumetric features rather than hand-crafted geometric representations. The Euclidean-distance barrier in AEGIS~\\cite{hu2025aegis} operates on explicit object positions from a world model, restricting its applicability to scenarios where object states are directly observable. OGM-CBF~\\cite{ji2024ogmcbf} constructs barriers from discrete occupancy grids via signed distance fields, but relies on accurate grid-level occupancy at test time rather than learned continuous features. Learning to Nudge~\\cite{kwon2026learningnudge} trains object-centric barrier functions (DCBF) that reason about individual objects, requiring explicit object decomposition that may not scale to highly cluttered scenes. Neural CS-BF~\\cite{neuralcsbf2025} learns barriers in configuration space for manipulation planning, but operates on geometric state representations independently of a VLA's perceptual features. In contrast, OCC-CBF operates in the VLA's continuous learned feature space and can perform semantic collision reasoning without explicit object segmentation, distance computation, or a separate perception pipeline.\n\n\\textit{We defer the detailed formulation, training procedure, and experimental validation of OCC-CBF to the extended version of this paper. The experiments in Section~4 evaluate the occupancy auxiliary head in isolation, which already yields substantial safety improvements without runtime overhead.}\n"
  }
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-20T20:25:13.637300+00:00_

File created successfully at: /home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/docs/paper/method.tex

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_method_20260520T201906",
  "tool": "Write",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-20T20:25:13.637445+00:00_

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
  "session": "worker_paper_writing_method_20260520T201906",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/docs/paper/method.tex"
  }
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-20T20:25:13.637716+00:00_

1	\section{Method}
2	\label{sec:method}
3	
4	We present OccSafe-VLA, a framework that improves collision safety in Vision-Language-Action models through two complementary mechanisms. The first is a BEV occupancy auxiliary head that injects spatial awareness into the vision encoder at zero inference cost (Section~\ref{sec:occ_head}). The second is OCC-CBF, a conceptual framework for explicit safety guarantees conditioned on learned spatial features (Section~\ref{sec:occ_cbf}). We begin by formalizing the problem setting and evaluation metrics.
5	
6	\subsection{Problem Formulation}
7	\label{sec:formulation}
8	
9	We consider a \textbf{Vision-Language-Action (VLA)} policy $\pi(a_t \mid o_t, l)$ that maps a visual observation $o_t$ and a language instruction $l$ to a 7-DOF action $a_t$ (delta end-effector pose) at each timestep $t$. The policy is parameterized by a large pretrained vision-language model fine-tuned on robot demonstration data. We evaluate performance along two complementary axes. \textbf{Task Success Rate (TSR)} measures the fraction of episodes in which the robot completes the instructed task:
10	\begin{equation}
11	  \text{TSR} = \frac{n_{\text{success}}}{N},
12	\end{equation}
13	where $n_{\text{success}}$ is the number of successful episodes out of $N$ total rollouts. \textbf{Collision Avoidance Rate (CAR)} measures the fraction of episodes free of unintended object displacement:
14	\begin{equation}
15	  \text{CAR} = 1 - \frac{n_{\text{collide}}}{N},
16	\end{equation}
17	where $n_{\text{collide}}$ counts episodes whose maximum L1 \texttt{body\_xpos} displacement exceeds a threshold of $0.001$, following the VLSA/AEGIS protocol~\cite{hu2025aegis}. Our objective is to improve CAR without degrading TSR. A policy that avoids collisions by refusing to act is not useful; a practical safe manipulation policy must maintain high task completion while reducing unintended contact with surrounding objects.
18	
19	\subsection{BEV Occupancy Auxiliary Head}
20	\label
…[truncated 7648 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_method_20260520T201906",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-20T20:25:13.637941+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "—",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/docs/paper/method.tex",
  "output_mode": "content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_method_20260520T201906",
  "tool": "Grep",
  "tool_args": {
    "pattern": "—",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/docs/paper/method.tex",
    "output_mode": "content"
  }
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-20T20:25:13.638115+00:00_

No matches found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_method_20260520T201906",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-20T20:25:13.638251+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": " – ",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/docs/paper/method.tex",
  "output_mode": "content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_method_20260520T201906",
  "tool": "Grep",
  "tool_args": {
    "pattern": " – ",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/docs/paper/method.tex",
    "output_mode": "content"
  }
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-20T20:25:13.638374+00:00_

No matches found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_method_20260520T201906",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-20T20:25:13.638489+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "ing[,.]",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/docs/paper/method.tex",
  "output_mode": "content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_method_20260520T201906",
  "tool": "Grep",
  "tool_args": {
    "pattern": "ing[,.]",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/docs/paper/method.tex",
    "output_mode": "content"
  }
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-20T20:25:13.638603+00:00_

22:[Omitted long matching line]
30:[Omitted long matching line]
54:[Omitted long matching line]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_method_20260520T201906",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 21 · 2026-05-20T20:25:13.638753+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "Furthermore|Moreover|Additionally|delve|leverage|utilize",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/docs/paper/method.tex",
  "output_mode": "content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_method_20260520T201906",
  "tool": "Grep",
  "tool_args": {
    "pattern": "Furthermore|Moreover|Additionally|delve|leverage|utilize",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/docs/paper/method.tex",
    "output_mode": "content"
  }
}
```

</details>

---

### Tool result

_source line 22 · 2026-05-20T20:25:13.638875+00:00_

No matches found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_method_20260520T201906",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 23 · 2026-05-20T20:25:13.638998+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "ing[,.]",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/docs/paper/method.tex",
  "output_mode": "content",
  "-n": "True"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_method_20260520T201906",
  "tool": "Grep",
  "tool_args": {
    "pattern": "ing[,.]",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/docs/paper/method.tex",
    "output_mode": "content",
    "-n": "True"
  }
}
```

</details>

---

### Tool result

_source line 24 · 2026-05-20T20:25:13.639111+00:00_

22:[Omitted long matching line]
30:[Omitted long matching line]
54:[Omitted long matching line]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_method_20260520T201906",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 25 · 2026-05-20T20:25:13.639227+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "ing[,.]",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/docs/paper/method.tex",
  "output_mode": "content",
  "head_limit": "20",
  "context": "0"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_method_20260520T201906",
  "tool": "Grep",
  "tool_args": {
    "pattern": "ing[,.]",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/docs/paper/method.tex",
    "output_mode": "content",
    "head_limit": "20",
    "context": "0"
  }
}
```

</details>

---

### Tool result

_source line 26 · 2026-05-20T20:25:13.639341+00:00_

22:[Omitted long matching line]
30:[Omitted long matching line]
54:[Omitted long matching line]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_method_20260520T201906",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 27 · 2026-05-20T20:25:13.639463+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/docs/paper/method.tex",
  "offset": "21",
  "limit": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_method_20260520T201906",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/docs/paper/method.tex",
    "offset": "21",
    "limit": "1"
  }
}
```

</details>

---

### Tool result

_source line 28 · 2026-05-20T20:25:13.639576+00:00_

&lt;system-reminder>Warning: the file exists but is shorter than the provided offset (21). The file has 57 lines.&lt;/system-reminder>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_method_20260520T201906",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 29 · 2026-05-20T20:25:13.639704+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/docs/paper/method.tex",
  "offset": "29",
  "limit": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_method_20260520T201906",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/docs/paper/method.tex",
    "offset": "29",
    "limit": "1"
  }
}
```

</details>

---

### Tool result

_source line 30 · 2026-05-20T20:25:13.639820+00:00_

&lt;system-reminder>Warning: the file exists but is shorter than the provided offset (29). The file has 57 lines.&lt;/system-reminder>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_method_20260520T201906",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 31 · 2026-05-20T20:25:13.639929+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/docs/paper/method.tex",
  "offset": "53",
  "limit": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_method_20260520T201906",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/docs/paper/method.tex",
    "offset": "53",
    "limit": "1"
  }
}
```

</details>

---

### Tool result

_source line 32 · 2026-05-20T20:25:13.640036+00:00_

&lt;system-reminder>Warning: the file exists but is shorter than the provided offset (53). The file has 57 lines.&lt;/system-reminder>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_method_20260520T201906",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 33 · 2026-05-20T20:25:13.640158+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/docs/paper/method.tex",
  "offset": "20",
  "limit": "3"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_method_20260520T201906",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/docs/paper/method.tex",
    "offset": "20",
    "limit": "3"
  }
}
```

</details>

---

### Tool result

_source line 34 · 2026-05-20T20:25:13.640271+00:00_

20	\label{sec:occ_head}
21	
22	Modern VLA models such as OpenVLA~\cite{kim2024openvla} and OpenVLA-OFT~\cite{kim2025openvlaoft} rely on 2D pretrained vision encoders (DINOv2, SigLIP) that excel at semantic understanding and language grounding. These encoders learn effective semantic-to-action mappings through fine-tuning, yet they lack explicit reasoning about 3D object boundaries and free space. When a robot must navigate tight clearances between objects in cluttered scenes, this gap becomes critical. A policy that cannot distinguish occupied from free regions of the workspace will collide with obstacles even when it correctly identifies the target object. The challenge is to inject 3D spatial structure into the vision encoder without adding inference cost or sacrificing the benefits of large-scale 2D pretraining.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_method_20260520T201906",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 35 · 2026-05-20T20:25:13.640403+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/docs/paper/method.tex",
  "offset": "28",
  "limit": "3"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_method_20260520T201906",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/docs/paper/method.tex",
    "offset": "28",
    "limit": "3"
  }
}
```

</details>

---

### Tool result

_source line 36 · 2026-05-20T20:25:13.640527+00:00_

28	where $\alpha = 0.75$ and $\gamma = 2.0$ are the balancing and focusing parameters, $p_t$ is the predicted probability for the ground-truth class, and the occupancy loss is weighted by $\lambda = 0.1$ relative to the action loss.
29	
30	The critical design principle is \textbf{zero inference cost}. During training, the occupancy head forces the vision encoder to internalize spatial structure: accurate occupancy prediction requires the encoder to represent where objects begin and end in 3D space. At inference time, we discard the occupancy head entirely, and the spatial awareness acquired during training persists as an emergent property of the encoder's learned features. This paradigm of training with auxiliary geometric supervision and deploying without it has been validated in autonomous driving by OccVLA~\cite{liu2025occvla}, which uses volumetric occupancy prediction to enhance a VLA's spatial understanding for navigation. Our work applies the same principle to tabletop manipulation, where the spatial scale and task geometry differ but the core insight holds: auxiliary occupancy supervision reshapes encoder representations to encode spatial boundaries that transfer to safer action prediction.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_method_20260520T201906",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 37 · 2026-05-20T20:25:13.640646+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/docs/paper/method.tex",
  "offset": "52",
  "limit": "3"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_method_20260520T201906",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/docs/paper/method.tex",
    "offset": "52",
    "limit": "3"
  }
}
```

</details>

---

### Tool result

_source line 38 · 2026-05-20T20:25:13.640786+00:00_

52	where $f_\theta$ is a learned function that maps the combined feature-state pair to a scalar safety value. States satisfying $h_{\text{occ}}(x) \geq 0$ are considered safe, and the control barrier constraint modifies the VLA's proposed action to maintain this invariant.
53	
54	OCC-CBF differs from existing barrier function approaches in its use of learned volumetric features rather than hand-crafted geometric representations. The Euclidean-distance barrier in AEGIS~\cite{hu2025aegis} operates on explicit object positions from a world model, restricting its applicability to scenarios where object states are directly observable. OGM-CBF~\cite{ji2024ogmcbf} constructs barriers from discrete occupancy grids via signed distance fields, but relies on accurate grid-level occupancy at test time rather than learned continuous features. Learning to Nudge~\cite{kwon2026learningnudge} trains object-centric barrier functions (DCBF) that reason about individual objects, requiring explicit object decomposition that may not scale to highly cluttered scenes. Neural CS-BF~\cite{neuralcsbf2025} learns barriers in configuration space for manipulation planning, but operates on geometric state representations independently of a VLA's perceptual features. In contrast, OCC-CBF operates in the VLA's continuous learned feature space and can perform semantic collision reasoning without explicit object segmentation, distance computation, or a separate perception pipeline.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_method_20260520T201906",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 39 · 2026-05-20T20:25:13.640964+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/docs/paper/method.tex",
  "old_string": "The BEV representation encodes object boundaries in a view-independent, allocentric coordinate frame, providing a natural supervisory signal for spatial structure.",
  "new_string": "The BEV representation encodes object boundaries in a view-independent, allocentric coordinate frame and serves as a natural supervisory signal for spatial structure."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_method_20260520T201906",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/docs/paper/method.tex",
    "old_string": "The BEV representation encodes object boundaries in a view-independent, allocentric coordinate frame, providing a natural supervisory signal for spatial structure.",
    "new_string": "The BEV representation encodes object boundaries in a view-independent, allocentric coordinate frame and serves as a natural supervisory signal for spatial structure."
  }
}
```

</details>

---

### Tool result

_source line 40 · 2026-05-20T20:25:13.641126+00:00_

The file /home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/docs/paper/method.tex has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_method_20260520T201906",
  "tool": "Edit",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 41 · 2026-05-20T20:25:13.641248+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/docs/paper/method.tex",
  "old_string": "operates on explicit object positions from a world model, restricting its applicability to scenarios where object states are directly observable.",
  "new_string": "operates on explicit object positions from a world model, which limits its applicability to scenarios where object states are directly observable."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_method_20260520T201906",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/docs/paper/method.tex",
    "old_string": "operates on explicit object positions from a world model, restricting its applicability to scenarios where object states are directly observable.",
    "new_string": "operates on explicit object positions from a world model, which limits its applicability to scenarios where object states are directly observable."
  }
}
```

</details>

---

### Tool result

_source line 42 · 2026-05-20T20:25:13.641401+00:00_

The file /home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/docs/paper/method.tex has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_method_20260520T201906",
  "tool": "Edit",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 43 · 2026-05-20T20:25:13.641520+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/docs/paper/method.tex",
  "old_string": "trains object-centric barrier functions (DCBF) that reason about individual objects, requiring explicit object decomposition that may not scale to highly cluttered scenes.",
  "new_string": "trains object-centric barrier functions (DCBF) that reason about individual objects and require explicit object decomposition, which may not scale to highly cluttered scenes."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_method_20260520T201906",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/docs/paper/method.tex",
    "old_string": "trains object-centric barrier functions (DCBF) that reason about individual objects, requiring explicit object decomposition that may not scale to highly cluttered scenes.",
    "new_string": "trains object-centric barrier functions (DCBF) that reason about individual objects and require explicit object decomposition, which may not scale to highly cluttered scenes."
  }
}
```

</details>

---

### Tool result

_source line 44 · 2026-05-20T20:25:13.641687+00:00_

The file /home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/docs/paper/method.tex has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_method_20260520T201906",
  "tool": "Edit",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 45 · 2026-05-20T20:25:13.641826+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "grep -n \"ing[,.]\" /home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/docs/paper/method.tex | grep -E \", [a-z]+ing \" || echo \"No -ing participial endings found\"",
  "description": "Check for remaining -ing participial phrase endings"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_method_20260520T201906",
  "tool": "Bash",
  "tool_args": {
    "command": "grep -n \"ing[,.]\" /home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/docs/paper/method.tex | grep -E \", [a-z]+ing \" || echo \"No -ing participial endings found\"",
    "description": "Check for remaining -ing participial phrase endings"
  }
}
```

</details>

---

### Tool result

_source line 46 · 2026-05-20T20:25:13.641944+00:00_

No -ing participial endings found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_method_20260520T201906",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 47 · 2026-05-20T20:25:13.642057+00:00_

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
  "session": "worker_paper_writing_method_20260520T201906",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/docs/paper/method.tex"
  }
}
```

</details>

---

### Tool result

_source line 48 · 2026-05-20T20:25:13.642220+00:00_

1	\section{Method}
2	\label{sec:method}
3	
4	We present OccSafe-VLA, a framework that improves collision safety in Vision-Language-Action models through two complementary mechanisms. The first is a BEV occupancy auxiliary head that injects spatial awareness into the vision encoder at zero inference cost (Section~\ref{sec:occ_head}). The second is OCC-CBF, a conceptual framework for explicit safety guarantees conditioned on learned spatial features (Section~\ref{sec:occ_cbf}). We begin by formalizing the problem setting and evaluation metrics.
5	
6	\subsection{Problem Formulation}
7	\label{sec:formulation}
8	
9	We consider a \textbf{Vision-Language-Action (VLA)} policy $\pi(a_t \mid o_t, l)$ that maps a visual observation $o_t$ and a language instruction $l$ to a 7-DOF action $a_t$ (delta end-effector pose) at each timestep $t$. The policy is parameterized by a large pretrained vision-language model fine-tuned on robot demonstration data. We evaluate performance along two complementary axes. \textbf{Task Success Rate (TSR)} measures the fraction of episodes in which the robot completes the instructed task:
10	\begin{equation}
11	  \text{TSR} = \frac{n_{\text{success}}}{N},
12	\end{equation}
13	where $n_{\text{success}}$ is the number of successful episodes out of $N$ total rollouts. \textbf{Collision Avoidance Rate (CAR)} measures the fraction of episodes free of unintended object displacement:
14	\begin{equation}
15	  \text{CAR} = 1 - \frac{n_{\text{collide}}}{N},
16	\end{equation}
17	where $n_{\text{collide}}$ counts episodes whose maximum L1 \texttt{body\_xpos} displacement exceeds a threshold of $0.001$, following the VLSA/AEGIS protocol~\cite{hu2025aegis}. Our objective is to improve CAR without degrading TSR. A policy that avoids collisions by refusing to act is not useful; a practical safe manipulation policy must maintain high task completion while reducing unintended contact with surrounding objects.
18	
19	\subsection{BEV Occupancy Auxiliary Head}
20	\label
…[truncated 7655 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_method_20260520T201906",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 49 · 2026-05-20T20:25:13.642407+00:00_

文件已写入 `/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/docs/paper/method.tex`。

验证清单:
- **参数一致性**: LoRA rank 32, 50K steps, batch 8, lr 5e-4, cosine decay, 2-layer MLP 256 hidden, 64×64 BEV, Focal Loss α=0.75 γ=2.0, λ=0.1 均与 experiments.tex 完全一致
- **Notation 统一**: π(a|o,l), o_t, l, a_t, L_occ, λ, z_occ, h_occ 全部按规范使用
- **引用**: kim2025openvlaoft, kim2024openvla, liu2025occvla, hu2025aegis, ji2024ogmcbf, kwon2026learningnudge, neuralcsbf2025 (均在 references.bib 中)
- **风格检查**: 无 em-dash/en-dash, 无 -ing 分词短语结尾, 无 Furthermore/Moreover/Additionally 连用, 无黑名单用词
- **§3.4**: 标注为 conceptual framework, 末尾用 \textit{} 声明 defer detailed formulation

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_paper_writing_method_20260520T201906"
}
```

</details>

---
