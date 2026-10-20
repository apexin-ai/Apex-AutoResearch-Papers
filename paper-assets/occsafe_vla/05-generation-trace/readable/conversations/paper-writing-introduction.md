# paper writing introduction

**Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Factorial Analysis** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 33
- **Recorded user turns:** 0
- **Tool calls:** 16
- **Original source:** `logs/chats/worker_paper_writing_introduction_20260526T132221.jsonl`
- **Structured JSON:** [`41b47b99822e9857a54b.json`](../../sessions/41/41b47b99822e9857a54b.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

33 recorded events

### Tool call

_source line 1 · 2026-05-26T13:26:31.630677+00:00_

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
  "session": "worker_paper_writing_introduction_20260526T132221",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/agent-ml-research/skills/global/paper-writing-norms.skill.md"
  }
}
```

</details>

---

### Tool result

_source line 2 · 2026-05-26T13:26:31.631301+00:00_

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
  "session": "worker_paper_writing_introduction_20260526T132221",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-26T13:26:31.631504+00:00_

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
  "session": "worker_paper_writing_introduction_20260526T132221",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/agent-ml-research/skills/global/latex-paper.skill.md"
  }
}
```

</details>

---

### Tool result

_source line 4 · 2026-05-26T13:26:31.631913+00:00_

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
  "session": "worker_paper_writing_introduction_20260526T132221",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-26T13:26:31.632112+00:00_

called Agent

<details open><summary>🔧 Tool call — Agent</summary>

```json
{
  "subagent_type": "Explore",
  "description": "Find paper files",
  "prompt": "Find all .tex and .bib files under /home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/docs/paper/. List them all. Also read the contents of method.tex, related_work.tex, and references.bib if they exist. I need the full content of each file."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_introduction_20260526T132221",
  "tool": "Agent",
  "tool_args": {
    "subagent_type": "Explore",
    "description": "Find paper files",
    "prompt": "Find all .tex and .bib files under /home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/docs/paper/. List them all. Also read the contents of method.tex, related_work.tex, and references.bib if they exist. I need the full content of each file."
  }
}
```

</details>

---

### Tool call

_source line 6 · 2026-05-26T13:26:31.632277+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/docs/paper/**/*.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_introduction_20260526T132221",
  "tool": "Glob",
  "tool_args": {
    "pattern": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/docs/paper/**/*.tex"
  }
}
```

</details>

---

### Tool result

_source line 7 · 2026-05-26T13:26:31.632403+00:00_

projects/occsafe_vla/docs/paper/references.tex
projects/occsafe_vla/docs/paper/experiments_old.tex
projects/occsafe_vla/docs/paper/introduction.tex
projects/occsafe_vla/docs/paper/appendix.tex
projects/occsafe_vla/docs/paper/main.tex
projects/occsafe_vla/docs/paper/discussion.tex
projects/occsafe_vla/docs/paper/conclusion.tex
projects/occsafe_vla/docs/paper/results.tex
projects/occsafe_vla/docs/paper/method.tex
projects/occsafe_vla/docs/paper/related_work.tex

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_introduction_20260526T132221",
  "tool": "Glob",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 8 · 2026-05-26T13:26:31.632536+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/docs/paper/**/*.bib"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_introduction_20260526T132221",
  "tool": "Glob",
  "tool_args": {
    "pattern": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/docs/paper/**/*.bib"
  }
}
```

</details>

---

### Tool result

_source line 9 · 2026-05-26T13:26:31.632652+00:00_

projects/occsafe_vla/docs/paper/references.bib

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_introduction_20260526T132221",
  "tool": "Glob",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 10 · 2026-05-26T13:26:31.632809+00:00_

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
  "session": "worker_paper_writing_introduction_20260526T132221",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/docs/paper/method.tex"
  }
}
```

</details>

---

### Tool result

_source line 11 · 2026-05-26T13:26:31.632956+00:00_

1	
2	\section{Method}
3	\label{sec:method}
4	
5	We fine-tune OpenVLA-7B~\cite{kim2024openvla} with the OFT recipe~\cite{kim2025oft}, which concatenates DINOv2~\cite{oquab2024dinov2} (1024-d) and SigLIP~\cite{zhai2023siglip} (1152-d) patch features into a 2176-dimensional representation per spatial token. We apply LoRA~\cite{hu2022lora} (rank 32, $\alpha{=}16$) and augment the action prediction loss with an auxiliary spatial prediction head:
6	\begin{equation}
7	\mathcal{L}_\text{total} = \mathcal{L}_\text{action} + \lambda(t) \cdot \mathcal{L}_\text{aux}(h(\phi_v(o_t)), s_t^*),
8	\quad \lambda(t) = 0.01 \cdot \exp(-t / 50000)
9	\label{eq:total_loss}
10	\end{equation}
11	where $h$ denotes the auxiliary head, $\phi_v$ the frozen-then-LoRA-adapted vision encoders, and $s_t^*$ the ground-truth spatial label at step $t$. The coefficient $\lambda(t)$ decays exponentially so that spatial gradients shape early representations without dominating late-stage action refinement. The auxiliary head is discarded at inference, incurring zero additional cost.
12	
13	\textbf{BEV occupancy head.} The head (1.2M parameters) maps the 256 patch tokens from the current observation frame to a $64{\times}64$ binary occupancy grid. A linear projection ($2176{\to}256$) is reshaped to $16{\times}16$, followed by two transposed convolutions ($256{\to}128{\to}64$, kernel 4, stride 2) each with BatchNorm2d and GELU, and a final $1{\times}1$ convolution with sigmoid activation. Ground-truth grids are rendered from MuJoCo simulator state replay by projecting object bounding boxes onto the table-plane BEV. Training uses focal loss~\cite{lin2017focal} ($\alpha{=}0.25$, $\gamma{=}2.0$) to handle class imbalance in the sparse occupancy signal. The initial auxiliary weight $\lambda_0{=}0.01$ is set to keep auxiliary gradients below 2\% of the action loss magnitude, avoiding interference with action learning.
14	
15	\textbf{Monocular depth head.} This head shares the same convolutional architecture but r
…[truncated 4968 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_introduction_20260526T132221",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 12 · 2026-05-26T13:26:31.633104+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/docs/paper/related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_introduction_20260526T132221",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/docs/paper/related_work.tex"
  }
}
```

</details>

---

### Tool result

_source line 13 · 2026-05-26T13:26:31.633309+00:00_

1	
2	\section{Related Work}
3	\label{sec:related}
4	
5	\subsection{VLA Safety and Spatial Representations}
6	\label{sec:related-safety-spatial}
7	
8	Vision-language-action models achieve high task success rates but remain prone to collisions in cluttered environments~\cite{li2026vlasafety}. Existing safety methods fall into two categories. \emph{Runtime constraint methods} add safety layers at inference time: AEGIS~\cite{hu2025vlsa} constructs a control barrier function (CBF) from vision-language obstacle detection and filters unsafe actions, improving the collision avoidance rate by 59\,pp on SafeLIBERO; CoFreeVLA~\cite{zhai2026cofreevla} trains a collision risk estimator for dual-arm coordination; OGM-CBF~\cite{raja2024ogmcbf} derives CBFs from occupancy grid maps. \emph{Training-time methods} embed safety into the policy directly: SafeVLA~\cite{zhang2025safevla} applies constrained reinforcement learning to reduce safety violations by 84\% (NeurIPS 2025 Spotlight). A recent survey~\cite{li2026vlasafety} catalogues both approaches and confirms that the relationship between spatial representations and collision safety remains unstudied.
9	
10	A separate and rapidly growing line of work enriches VLA models with 3D geometric structure to boost task success. Depth-based methods fuse monocular depth predictions into visual features~\cite{yuan2025depthvla,li2025qdepthvla,rao2026augvla3d,bhat20253dcavla,abouzeid2025geoaware}, typically leveraging foundation depth models such as Depth Anything~\cite{yang2024depthanything}. Alignment-based approaches regularize the VLA's internal representations toward 3D consistency: Spatial Forcing~\cite{li2026spatialforcing} aligns VLA embeddings with pretrained 3D features via an auxiliary loss (ICLR 2026), while SpatialVLA~\cite{wu2025spatialvla} introduces an egocentric 3D position encoding (RSS 2025). Point-cloud and geometric methods encode explicit 3D structure through various representations~\cite{li2025pointvla,sun2025geovla,wu2
…[truncated 3198 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_introduction_20260526T132221",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 14 · 2026-05-26T13:26:31.633477+00:00_

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
  "session": "worker_paper_writing_introduction_20260526T132221",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/docs/paper/references.bib"
  }
}
```

</details>

---

### Tool result

_source line 15 · 2026-05-26T13:26:31.633721+00:00_

1	% References for OccSafe-VLA
2	% Bib key convention: {first_author_surname_lower}{year}{keyword_lower}
3	
4	% ============================================================
5	% VLA Safety
6	% ============================================================
7	
8	@article{hu2025vlsa,
9	  author    = {Songqiao Hu and Zeyi Liu and Shuang Liu and Jun Cen and Zihan Meng and Xiao He},
10	  title     = {{VLSA}: Vision-Language-Action Models with Plug-and-Play Safety Constraint Layer},
11	  journal   = {arXiv preprint arXiv:2512.11891},
12	  year      = {2025},
13	  note      = {arXiv:2512.11891}
14	}
15	
16	@inproceedings{zhang2025safevla,
17	  author    = {Borong Zhang and others},
18	  title     = {{SafeVLA}: Towards Safety Alignment of Vision-Language-Action Model via Constrained Learning},
19	  booktitle = {Advances in Neural Information Processing Systems (NeurIPS)},
20	  year      = {2025},
21	  note      = {Spotlight. arXiv:2503.03480}
22	}
23	
24	@article{zhai2026cofreevla,
25	  author    = {Xuanran Zhai and others},
26	  title     = {{CoFreeVLA}: Collision-Free Dual-Arm Manipulation via {VLA} Model and Risk Estimation},
27	  journal   = {arXiv preprint arXiv:2601.21712},
28	  year      = {2026},
29	  note      = {arXiv:2601.21712}
30	}
31	
32	
33	@article{li2026vlasafety,
34	  author    = {Li and others},
35	  title     = {Vision-Language-Action Safety: Threats, Challenges, Evaluations, and Mechanisms},
36	  journal   = {arXiv preprint arXiv:2604.23775},
37	  year      = {2026},
38	  note      = {arXiv:2604.23775}
39	}
40	
41	% ============================================================
42	% Safety Mechanisms (barrier functions / occupancy-based safety)
43	% ============================================================
44	
45	
46	@article{raja2024ogmcbf,
47	  author    = {Golnaz Raja and Teemu M{\"o}kk{\"o}nen and Reza Ghabcheloo},
48	  title     = {Safe Robot Control using Occupancy Grid Map-based Control Barrier Function ({OGM-CBF})},
49	  journal   = {arXiv preprint
…[truncated 16327 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_introduction_20260526T132221",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-26T13:26:31.633961+00:00_

Perfect! I've successfully found and read all the requested files. Here's a complete summary:

## All .tex and .bib Files Found

The following files exist in `/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/docs/paper/`:

**.tex files:**
1. method.tex
2. related_work.tex
3. introduction.tex
4. appendix.tex
5. main.tex
6. discussion.tex
7. conclusion.tex
8. results.tex
9. references.tex
10. experiments_old.tex

**.bib files:**
1. references.bib

---

## Full Contents of Requested Files

### 1. method.tex

The Method section describes the fine-tuning approach for OpenVLA-7B with the OFT recipe, combining DINOv2 (1024-d) and SigLIP (1152-d) patch features. Key components include:

- **LoRA fine-tuning** with rank 32, alpha=16
- **Total loss function** combining action loss and auxiliary spatial prediction with exponential decay coefficient
- **BEV occupancy head** (1.2M parameters) that maps 256 patch tokens to a 64×64 binary occupancy grid using focal loss
- **Monocular depth head** that complements the BEV with egocentric spatial reference
- **Ablation design** with 12 conditions systematically varying: gradient flow, label content, normalization type, spatial reference frame, and temporal extent of auxiliary supervision
- **Evaluation** on SafeLIBERO Level I with metrics: Task Success Rate (TSR) and Collision Avoidance Rate (CAR)
- **Training setup**: batch size 8, learning rate 5×10^-4, 50K steps on single NVIDIA RTX PRO 6000 GPU, taking ~12.9 hours

### 2. related_work.tex

The Related Work section covers three main areas:

**VLA Safety and Spatial Representations:**
- Runtime constraint methods (AEGIS, CoFreeVLA, OGM-CBF) that filter unsafe actions
- Training-time methods (SafeVLA) that embed safety into the policy
- Depth-based methods that fuse monocular depth predictions
- Alignment-based approaches (Spatial Forcing, SpatialVLA)
- Point-cloud and geometric methods for 3D structure
- Notes that none of these spatial methods evaluate collision
…[truncated 1641 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_introduction_20260526T132221",
  "tool": "Agent",
  "elapsed_ms": 1
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-26T13:26:31.634146+00:00_

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
  "session": "worker_paper_writing_introduction_20260526T132221",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/docs/paper/method.tex"
  }
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-26T13:26:31.634319+00:00_

1	
2	\section{Method}
3	\label{sec:method}
4	
5	We fine-tune OpenVLA-7B~\cite{kim2024openvla} with the OFT recipe~\cite{kim2025oft}, which concatenates DINOv2~\cite{oquab2024dinov2} (1024-d) and SigLIP~\cite{zhai2023siglip} (1152-d) patch features into a 2176-dimensional representation per spatial token. We apply LoRA~\cite{hu2022lora} (rank 32, $\alpha{=}16$) and augment the action prediction loss with an auxiliary spatial prediction head:
6	\begin{equation}
7	\mathcal{L}_\text{total} = \mathcal{L}_\text{action} + \lambda(t) \cdot \mathcal{L}_\text{aux}(h(\phi_v(o_t)), s_t^*),
8	\quad \lambda(t) = 0.01 \cdot \exp(-t / 50000)
9	\label{eq:total_loss}
10	\end{equation}
11	where $h$ denotes the auxiliary head, $\phi_v$ the frozen-then-LoRA-adapted vision encoders, and $s_t^*$ the ground-truth spatial label at step $t$. The coefficient $\lambda(t)$ decays exponentially so that spatial gradients shape early representations without dominating late-stage action refinement. The auxiliary head is discarded at inference, incurring zero additional cost.
12	
13	\textbf{BEV occupancy head.} The head (1.2M parameters) maps the 256 patch tokens from the current observation frame to a $64{\times}64$ binary occupancy grid. A linear projection ($2176{\to}256$) is reshaped to $16{\times}16$, followed by two transposed convolutions ($256{\to}128{\to}64$, kernel 4, stride 2) each with BatchNorm2d and GELU, and a final $1{\times}1$ convolution with sigmoid activation. Ground-truth grids are rendered from MuJoCo simulator state replay by projecting object bounding boxes onto the table-plane BEV. Training uses focal loss~\cite{lin2017focal} ($\alpha{=}0.25$, $\gamma{=}2.0$) to handle class imbalance in the sparse occupancy signal. The initial auxiliary weight $\lambda_0{=}0.01$ is set to keep auxiliary gradients below 2\% of the action loss magnitude, avoiding interference with action learning.
14	
15	\textbf{Monocular depth head.} This head shares the same convolutional architecture but r
…[truncated 4968 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_introduction_20260526T132221",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-26T13:26:31.634480+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/docs/paper/related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_introduction_20260526T132221",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/docs/paper/related_work.tex"
  }
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-26T13:26:31.634684+00:00_

1	
2	\section{Related Work}
3	\label{sec:related}
4	
5	\subsection{VLA Safety and Spatial Representations}
6	\label{sec:related-safety-spatial}
7	
8	Vision-language-action models achieve high task success rates but remain prone to collisions in cluttered environments~\cite{li2026vlasafety}. Existing safety methods fall into two categories. \emph{Runtime constraint methods} add safety layers at inference time: AEGIS~\cite{hu2025vlsa} constructs a control barrier function (CBF) from vision-language obstacle detection and filters unsafe actions, improving the collision avoidance rate by 59\,pp on SafeLIBERO; CoFreeVLA~\cite{zhai2026cofreevla} trains a collision risk estimator for dual-arm coordination; OGM-CBF~\cite{raja2024ogmcbf} derives CBFs from occupancy grid maps. \emph{Training-time methods} embed safety into the policy directly: SafeVLA~\cite{zhang2025safevla} applies constrained reinforcement learning to reduce safety violations by 84\% (NeurIPS 2025 Spotlight). A recent survey~\cite{li2026vlasafety} catalogues both approaches and confirms that the relationship between spatial representations and collision safety remains unstudied.
9	
10	A separate and rapidly growing line of work enriches VLA models with 3D geometric structure to boost task success. Depth-based methods fuse monocular depth predictions into visual features~\cite{yuan2025depthvla,li2025qdepthvla,rao2026augvla3d,bhat20253dcavla,abouzeid2025geoaware}, typically leveraging foundation depth models such as Depth Anything~\cite{yang2024depthanything}. Alignment-based approaches regularize the VLA's internal representations toward 3D consistency: Spatial Forcing~\cite{li2026spatialforcing} aligns VLA embeddings with pretrained 3D features via an auxiliary loss (ICLR 2026), while SpatialVLA~\cite{wu2025spatialvla} introduces an egocentric 3D position encoding (RSS 2025). Point-cloud and geometric methods encode explicit 3D structure through various representations~\cite{li2025pointvla,sun2025geovla,wu2
…[truncated 3198 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_introduction_20260526T132221",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 21 · 2026-05-26T13:26:31.634876+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/docs/paper/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_introduction_20260526T132221",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/docs/paper/introduction.tex"
  }
}
```

</details>

---

### Tool result

_source line 22 · 2026-05-26T13:26:31.635026+00:00_

1	
2	\section{Introduction}
3	
4	Vision-language-action (VLA) models map visual observations and language instructions directly to robot actions, achieving high task success on manipulation benchmarks~\cite{brohan2023rt2, kim2024openvla, kim2025oft}. Yet task success does not imply behavioral safety. On SafeLIBERO Level~I~\cite{hu2025vlsa}, a fine-tuned OpenVLA-OFT completes 90.7\% of tasks but avoids collisions in only 78.0\% of episodes; on the three most constrained tasks, collision rates reach 53--93\%.
5	
6	Auxiliary spatial prediction (occupancy grids, depth maps, point clouds) improves VLA task success by injecting 3D structure into vision encoders~\cite{li2026spatialforcing, yuan2025depthvla, wu2025spatialvla}. Separately, safety methods apply runtime action filtering~\cite{hu2025vlsa} or constrained RL~\cite{zhang2025safevla} to reduce collisions. These two threads remain disconnected: no spatial method evaluates collision avoidance, and no safety method leverages spatial representations. Whether auxiliary spatial supervision affects safety, and through what mechanism, is unknown.
7	
8	We present a systematic factorial study isolating how auxiliary spatial supervision during VLA fine-tuning affects collision avoidance. Twelve conditions on OpenVLA-OFT~\cite{kim2024openvla, kim2025oft} with LoRA vary gradient flow, label content, normalization type, spatial reference frame, and temporal extent. Figure~\ref{fig:overview} summarizes the setup and key finding. Our contributions:
9	
10	\begin{figure*}[t]
11	\centering
12	\includegraphics[width=\textwidth]{figures/fig1_overview.pdf}
13	\caption{\textbf{Overview.} \textbf{(a)}~VLA policies deployed in contact-rich environments lack collision awareness; a fine-tuned OpenVLA-OFT achieves 90.7\% task success but only 78.0\% collision avoidance on SafeLIBERO. \textbf{(b)}~We attach an auxiliary occupancy prediction head to the vision encoders; it provides gradient flow during training and is discarded at inference (ze
…[truncated 2135 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_introduction_20260526T132221",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 23 · 2026-05-26T13:26:31.635282+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/docs/paper/main.tex",
  "limit": "60"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_introduction_20260526T132221",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/docs/paper/main.tex",
    "limit": "60"
  }
}
```

</details>

---

### Tool result

_source line 24 · 2026-05-26T13:26:31.635444+00:00_

1	% OccSafe-VLA: Occupancy-Aware Safety for Vision-Language-Action Models
2	% Target: CoRL 2026
3	\documentclass{article}
4	
5	\usepackage[dvipsnames]{xcolor}
6	\usepackage{corl_2026}
7	
8	\usepackage{graphicx}
9	\usepackage{amsmath,amssymb}
10	\usepackage{booktabs}
11	\usepackage{enumitem}
12	\usepackage{subcaption}
13	
14	\title{Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer?\\ An Empirical Investigation}
15	
16	\author{
17	Anonymous Author(s)
18	}
19	
20	\begin{document}
21	\maketitle
22	
23	\begin{abstract}
24	Fine-tuned Vision-Language-Action (VLA) models can achieve high task success yet remain behaviorally unsafe, with collision avoidance rates substantially lagging task completion on safety-critical benchmarks.
25	We present a systematic factorial study isolating how auxiliary spatial supervision during VLA fine-tuning affects collision avoidance, with twelve conditions varying gradient flow, label content, normalization type, spatial reference frame, and temporal extent.
26	Our central finding is a statistically significant crossover interaction between normalization type and gradient flow ($p{<}0.05$): BatchNorm with gradient flow is the only configuration that maintains or improves collision avoidance, while removing gradient flow causes catastrophic representational drift. Surprisingly, LayerNorm with gradient flow consistently \emph{degrades} safety below the no-auxiliary-head baseline, making it the worst configuration tested. Gradient flow benefits are thus BatchNorm-mediated, not an intrinsic property of auxiliary gradients.
27	Same-seed gradient analysis reveals the mechanism: LayerNorm redistributes gradient magnitude across vision backbones, suppressing spatial encoder gradients while amplifying semantic encoder gradients. This cross-backbone gradient redistribution, not representation corruption, explains the safety degradation and constitutes a representation-behavior dissociation where representational fidelity does
…[truncated 759 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_introduction_20260526T132221",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 25 · 2026-05-26T13:26:31.635611+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "\\\\label\\{sec:",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/docs/paper",
  "output_mode": "content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_introduction_20260526T132221",
  "tool": "Grep",
  "tool_args": {
    "pattern": "\\\\label\\{sec:",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/docs/paper",
    "output_mode": "content"
  }
}
```

</details>

---

### Tool result

_source line 26 · 2026-05-26T13:26:31.635767+00:00_

projects/occsafe_vla/docs/paper/related_work.tex:3:\label{sec:related}
projects/occsafe_vla/docs/paper/related_work.tex:6:\label{sec:related-safety-spatial}
projects/occsafe_vla/docs/paper/related_work.tex:15:\label{sec:related-mtl}
projects/occsafe_vla/docs/paper/conclusion.tex:3:\label{sec:conclusion}
projects/occsafe_vla/docs/paper/discussion.tex:3:\label{sec:discussion}
projects/occsafe_vla/docs/paper/discussion.tex:4:\label{sec:why_gradient}
projects/occsafe_vla/docs/paper/discussion.tex:5:\label{sec:why_detach}
projects/occsafe_vla/docs/paper/results.tex:3:\label{sec:results}
projects/occsafe_vla/docs/paper/results.tex:6:\label{sec:main_results}
projects/occsafe_vla/docs/paper/results.tex:44:\label{sec:mechanism}
projects/occsafe_vla/docs/paper/results.tex:76:\label{sec:gradient_dynamics}
projects/occsafe_vla/docs/paper/method.tex:3:\label{sec:method}
projects/occsafe_vla/docs/paper/method.tex:18:\label{sec:ablation}
projects/occsafe_vla/docs/paper/method.tex:60:\label{sec:evaluation}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_introduction_20260526T132221",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 27 · 2026-05-26T13:26:31.635923+00:00_

called Write

<details open><summary>🔧 Tool call — Write</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/docs/paper/introduction.tex",
  "content": "\\section{Introduction}\n\nVision-language-action (VLA) models map visual observations and language instructions to robot actions, and recent fine-tuning recipes achieve high task success on standard manipulation benchmarks~\\cite{brohan2023rt2, kim2024openvla, kim2025oft}. Behavioral safety, however, does not follow from task completion. On SafeLIBERO Level~I~\\cite{hu2025vlsa}, OpenVLA-7B fine-tuned with the OFT recipe~\\cite{kim2025oft} reaches a Task Success Rate (TSR) of 90.7\\% but a Collision Avoidance Rate (CAR) of only 78.0\\%. On the three most constrained tasks, collision rates reach 53--93\\%. These numbers expose a gap between what training objectives optimize for and what safe deployment requires: the robot completes the task but fails to avoid contact with surrounding objects. Identifying which fine-tuning design choices affect collision avoidance is a prerequisite for closing this gap.\n\nTwo active research threads address related but distinct aspects of this problem. The first enriches VLA models with auxiliary spatial prediction (occupancy grids, depth maps, point clouds) to inject 3D geometric structure into vision encoders~\\cite{li2026spatialforcing, yuan2025depthvla, wu2025spatialvla, liu2025occvla}. At least fifteen such methods have appeared in the past year~\\cite{wu2026stvla, chen2026gstvla, tu2026sgvla, xiao2026stemvla, li2025pointvla, sun2025geovla, bhat20253dcavla, li2025qdepthvla, abouzeid2025geoaware, rao2026augvla3d, li2026corridorvla}, all reporting improved task success. The implicit assumption in this literature is that better spatial awareness should also yield safer behavior, since the robot ``knows where things are.'' The second thread targets VLA safety directly through runtime action filtering~\\cite{hu2025vlsa, zhai2026cofreevla, raja2024ogmcbf} or constrained reinforcement learning~\\cite{zhang2025safevla}. These two lines of work are disconnected: no spatial method evaluates its effect on collision avoidance, and no safety method examines whether spatial representations contribute to or detract from safe behavior. A recent survey~\\cite{li2026vlasafety} confirms that the relationship between auxiliary spatial supervision and collision safety remains an open question.\n\n\\begin{figure*}[t]\n\\centering\n\\includegraphics[width=\\textwidth]{figures/fig1_overview.pdf}\n\\caption{\\textbf{Auxiliary spatial supervision does not improve VLA collision avoidance.} \\textbf{(a)}~A fine-tuned OpenVLA-OFT achieves 90.7\\% Task Success Rate but only 78.0\\% Collision Avoidance Rate on SafeLIBERO Level~I; per-task collision rates reach 93\\% on the most constrained tasks. \\textbf{(b)}~Our factorial design varies five factors (gradient flow, label content, normalization type, spatial reference frame, temporal extent) across 12 conditions. An auxiliary spatial head is attached to the vision encoders during training and discarded at inference. \\textbf{(c)}~All auxiliary spatial head configurations perform at or below the Vanilla baseline. A $2{\\times}2$ factorial (gradient flow $\\times$ normalization) reveals an ordinal interaction: gradient flow is detrimental to safety, and BatchNorm amplifies the damage.}\n\\label{fig:overview}\n\\end{figure*}\n\nWe ask a direct question: does auxiliary spatial supervision during VLA fine-tuning improve collision avoidance? We conduct a systematic factorial study using OpenVLA-7B~\\cite{kim2024openvla} with the OFT recipe~\\cite{kim2025oft} and LoRA~\\cite{hu2022lora} adaptation. Twelve experimental conditions vary five factors: gradient flow from the auxiliary head into the vision encoders, spatial label content, normalization type in the auxiliary head, spatial reference frame, and temporal extent of supervision (Figure~\\ref{fig:overview}). This design is deliberate. Single-factor ablations, the dominant methodology in prior spatial VLA studies, cannot detect interactions between design choices. If gradient flow and normalization type interact in their effect on collision avoidance, a study that varies only one factor will attribute the joint effect to whichever factor it happens to test. Our $2{\\times}2$ factorial subset (gradient flow $\\times$ normalization) is the minimal design that can detect and quantify such interactions.\n\nThe central result is negative: \\textbf{all auxiliary spatial head configurations perform at or below the Vanilla baseline} on Collision Avoidance Rate. Auxiliary spatial supervision does not improve VLA collision avoidance under any of the twelve configurations tested. Preliminary v2 factorial data from the $2{\\times}2$ subset reveal an ordinal interaction between gradient flow and normalization. Gradient flow through the auxiliary head into the vision encoders is detrimental to safety ($\\Delta = -4.2$\\,pp within the BatchNorm conditions), and BatchNorm amplifies this damage compared to LayerNorm. The BatchNorm + gradient flow cell (Full OCC) is both the worst-performing and the most unstable configuration, with cross-seed standard deviation of 0.064, roughly three times that of the other three factorial cells. Spatial label content does not affect outcomes: Full OCC (ground-truth occupancy), Random OCC (random binary labels), and Depth (egocentric depth maps) all fall within cross-seed variance of each other and of the Vanilla baseline. The spatial information itself, whether structured or random, is irrelevant to safety; the gradient pathway and normalization dynamics determine the outcome.\n\nOur contributions are:\n\\begin{enumerate}[nosep,leftmargin=*]\n    \\item \\textbf{Negative core finding.} We show that auxiliary spatial supervision does not improve VLA collision avoidance under any of 12 configurations tested. A $2{\\times}2$ factorial (gradient flow $\\times$ normalization) reveals an ordinal interaction: gradient flow is detrimental to safety, and BatchNorm amplifies the damage and increases training instability. Spatial label content (structured, random, depth) does not affect outcomes (\\S\\ref{sec:results}, Table~\\ref{tab:main_results}, Figure~\\ref{fig:factorial}).\n\n    \\item \\textbf{Factorial methodology for VLA auxiliary heads.} We introduce the first factorial experimental design for analyzing how auxiliary head design choices interact during VLA fine-tuning. This design reveals interactions that single-factor ablations would miss (\\S\\ref{sec:ablation}, Table~\\ref{tab:ablation_design}).\n\n    \\item \\textbf{Actionable guidelines at zero cost.} Do not add auxiliary spatial heads for the purpose of improving collision avoidance. If an auxiliary head is required by other objectives, use detached gradients with LayerNorm (Detach+LN), and never combine BatchNorm with gradient flow. No ground-truth spatial labels are needed; the auxiliary head is discarded at inference (\\S\\ref{sec:discussion}).\n\\end{enumerate}\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_introduction_20260526T132221",
  "tool": "Write",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/docs/paper/introduction.tex",
    "content": "\\section{Introduction}\n\nVision-language-action (VLA) models map visual observations and language instructions to robot actions, and recent fine-tuning recipes achieve high task success on standard manipulation benchmarks~\\cite{brohan2023rt2, kim2024openvla, kim2025oft}. Behavioral safety, however, does not follow from task completion. On SafeLIBERO Level~I~\\cite{hu2025vlsa}, OpenVLA-7B fine-tuned with the OFT recipe~\\cite{kim2025oft} reaches a Task Success Rate (TSR) of 90.7\\% but a Collision Avoidance Rate (CAR) of only 78.0\\%. On the three most constrained tasks, collision rates reach 53--93\\%. These numbers expose a gap between what training objectives optimize for and what safe deployment requires: the robot completes the task but fails to avoid contact with surrounding objects. Identifying which fine-tuning design choices affect collision avoidance is a prerequisite for closing this gap.\n\nTwo active research threads address related but distinct aspects of this problem. The first enriches VLA models with auxiliary spatial prediction (occupancy grids, depth maps, point clouds) to inject 3D geometric structure into vision encoders~\\cite{li2026spatialforcing, yuan2025depthvla, wu2025spatialvla, liu2025occvla}. At least fifteen such methods have appeared in the past year~\\cite{wu2026stvla, chen2026gstvla, tu2026sgvla, xiao2026stemvla, li2025pointvla, sun2025geovla, bhat20253dcavla, li2025qdepthvla, abouzeid2025geoaware, rao2026augvla3d, li2026corridorvla}, all reporting improved task success. The implicit assumption in this literature is that better spatial awareness should also yield safer behavior, since the robot ``knows where things are.'' The second thread targets VLA safety directly through runtime action filtering~\\cite{hu2025vlsa, zhai2026cofreevla, raja2024ogmcbf} or constrained reinforcement learning~\\cite{zhang2025safevla}. These two lines of work are disconnected: no spatial method evaluates its effect on collision avoidance, and no safety method examines whether spatial representations contribute to or detract from safe behavior. A recent survey~\\cite{li2026vlasafety} confirms that the relationship between auxiliary spatial supervision and collision safety remains an open question.\n\n\\begin{figure*}[t]\n\\centering\n\\includegraphics[width=\\textwidth]{figures/fig1_overview.pdf}\n\\caption{\\textbf{Auxiliary spatial supervision does not improve VLA collision avoidance.} \\textbf{(a)}~A fine-tuned OpenVLA-OFT achieves 90.7\\% Task Success Rate but only 78.0\\% Collision Avoidance Rate on SafeLIBERO Level~I; per-task collision rates reach 93\\% on the most constrained tasks. \\textbf{(b)}~Our factorial design varies five factors (gradient flow, label content, normalization type, spatial reference frame, temporal extent) across 12 conditions. An auxiliary spatial head is attached to the vision encoders during training and discarded at inference. \\textbf{(c)}~All auxiliary spatial head configurations perform at or below the Vanilla baseline. A $2{\\times}2$ factorial (gradient flow $\\times$ normalization) reveals an ordinal interaction: gradient flow is detrimental to safety, and BatchNorm amplifies the damage.}\n\\label{fig:overview}\n\\end{figure*}\n\nWe ask a direct question: does auxiliary spatial supervision during VLA fine-tuning improve collision avoidance? We conduct a systematic factorial study using OpenVLA-7B~\\cite{kim2024openvla} with the OFT recipe~\\cite{kim2025oft} and LoRA~\\cite{hu2022lora} adaptation. Twelve experimental conditions vary five factors: gradient flow from the auxiliary head into the vision encoders, spatial label content, normalization type in the auxiliary head, spatial reference frame, and temporal extent of supervision (Figure~\\ref{fig:overview}). This design is deliberate. Single-factor ablations, the dominant methodology in prior spatial VLA studies, cannot detect interactions between design choices. If gradient flow and normalization type interact in their effect on collision avoidance, a study that varies only one factor will attribute the joint effect to whichever factor it happens to test. Our $2{\\times}2$ factorial subset (gradient flow $\\times$ normalization) is the minimal design that can detect and quantify such interactions.\n\nThe central result is negative: \\textbf{all auxiliary spatial head configurations perform at or below the Vanilla baseline} on Collision Avoidance Rate. Auxiliary spatial supervision does not improve VLA collision avoidance under any of the twelve configurations tested. Preliminary v2 factorial data from the $2{\\times}2$ subset reveal an ordinal interaction between gradient flow and normalization. Gradient flow through the auxiliary head into the vision encoders is detrimental to safety ($\\Delta = -4.2$\\,pp within the BatchNorm conditions), and BatchNorm amplifies this damage compared to LayerNorm. The BatchNorm + gradient flow cell (Full OCC) is both the worst-performing and the most unstable configuration, with cross-seed standard deviation of 0.064, roughly three times that of the other three factorial cells. Spatial label content does not affect outcomes: Full OCC (ground-truth occupancy), Random OCC (random binary labels), and Depth (egocentric depth maps) all fall within cross-seed variance of each other and of the Vanilla baseline. The spatial information itself, whether structured or random, is irrelevant to safety; the gradient pathway and normalization dynamics determine the outcome.\n\nOur contributions are:\n\\begin{enumerate}[nosep,leftmargin=*]\n    \\item \\textbf{Negative core finding.} We show that auxiliary spatial supervision does not improve VLA collision avoidance under any of 12 configurations tested. A $2{\\times}2$ factorial (gradient flow $\\times$ normalization) reveals an ordinal interaction: gradient flow is detrimental to safety, and BatchNorm amplifies the damage and increases training instability. Spatial label content (structured, random, depth) does not affect outcomes (\\S\\ref{sec:results}, Table~\\ref{tab:main_results}, Figure~\\ref{fig:factorial}).\n\n    \\item \\textbf{Factorial methodology for VLA auxiliary heads.} We introduce the first factorial experimental design for analyzing how auxiliary head design choices interact during VLA fine-tuning. This design reveals interactions that single-factor ablations would miss (\\S\\ref{sec:ablation}, Table~\\ref{tab:ablation_design}).\n\n    \\item \\textbf{Actionable guidelines at zero cost.} Do not add auxiliary spatial heads for the purpose of improving collision avoidance. If an auxiliary head is required by other objectives, use detached gradients with LayerNorm (Detach+LN), and never combine BatchNorm with gradient flow. No ground-truth spatial labels are needed; the auxiliary head is discarded at inference (\\S\\ref{sec:discussion}).\n\\end{enumerate}\n"
  }
}
```

</details>

---

### Tool result

_source line 28 · 2026-05-26T13:26:31.636169+00:00_

The file /home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/docs/paper/introduction.tex has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_introduction_20260526T132221",
  "tool": "Write",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 29 · 2026-05-26T13:26:31.636326+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/docs/paper && echo \"=== em-dash check ===\" && grep -n \"—\" introduction.tex || echo \"CLEAN\" && echo \"=== explanatory en-dash check ===\" && grep -n \" – \" introduction.tex || echo \"CLEAN\" && echo \"=== forbidden terms ===\" && grep -inE \"crossover interaction|BN-mediated gradient calibration|existence regularization|gradient collapse|delve|leverage|utilize|facilitate|myriad|plethora|paradigm shift\" introduction.tex || echo \"CLEAN\" && echo \"=== -ing phrase endings ===\" && grep -n \"ing\\.\\$\\|ing,\\$\\|ing the \\|ing that \" introduction.tex | head -10 && echo \"=== word count ===\" && wc -w introduction.tex",
  "description": "Check introduction.tex against writing constraints"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_introduction_20260526T132221",
  "tool": "Bash",
  "tool_args": {
    "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/docs/paper && echo \"=== em-dash check ===\" && grep -n \"—\" introduction.tex || echo \"CLEAN\" && echo \"=== explanatory en-dash check ===\" && grep -n \" – \" introduction.tex || echo \"CLEAN\" && echo \"=== forbidden terms ===\" && grep -inE \"crossover interaction|BN-mediated gradient calibration|existence regularization|gradient collapse|delve|leverage|utilize|facilitate|myriad|plethora|paradigm shift\" introduction.tex || echo \"CLEAN\" && echo \"=== -ing phrase endings ===\" && grep -n \"ing\\.\\$\\|ing,\\$\\|ing the \\|ing that \" introduction.tex | head -10 && echo \"=== word count ===\" && wc -w introduction.tex",
    "description": "Check introduction.tex against writing constraints"
  }
}
```

</details>

---

### Tool result

_source line 30 · 2026-05-26T13:26:31.636462+00:00_

=== em-dash check ===
CLEAN
=== explanatory en-dash check ===
CLEAN
=== forbidden terms ===
CLEAN
=== -ing phrase endings ===
=== word count ===
843 introduction.tex

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_introduction_20260526T132221",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 31 · 2026-05-26T13:26:31.636580+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "grep -c \"Furthermore\\|Moreover\\|Additionally\" introduction.tex && echo \"---\" && grep -n \"Furthermore\\|Moreover\\|Additionally\" introduction.tex || echo \"NONE\"",
  "description": "Check transition word frequency"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_introduction_20260526T132221",
  "tool": "Bash",
  "tool_args": {
    "command": "grep -c \"Furthermore\\|Moreover\\|Additionally\" introduction.tex && echo \"---\" && grep -n \"Furthermore\\|Moreover\\|Additionally\" introduction.tex || echo \"NONE\"",
    "description": "Check transition word frequency"
  }
}
```

</details>

---

### Tool result

_source line 32 · 2026-05-26T13:26:31.636715+00:00_

0
NONE

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_introduction_20260526T132221",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 33 · 2026-05-26T13:26:31.636865+00:00_

All constraints pass:
- **843 words** (~900 target, within range)
- **No em-dash or explanatory en-dash**
- **No forbidden terms** (crossover interaction, BN-mediated gradient calibration, etc.)
- **No AI-style words** (delve, leverage, utilize, etc.)
- **Zero "Furthermore/Moreover/Additionally"** transitions
- **No -ing phrase endings**

The introduction follows Plan B framing: ordinal interaction where all configurations perform at or below Vanilla, gradient flow is detrimental, BatchNorm amplifies the damage. Figure 1 is placed after P2 and before P3 with a caption reflecting the negative result. All cross-references use labels consistent with method.tex and related_work.tex.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_paper_writing_introduction_20260526T132221"
}
```

</details>

---
