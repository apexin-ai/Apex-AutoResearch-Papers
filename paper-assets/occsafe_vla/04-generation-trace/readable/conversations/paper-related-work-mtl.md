# paper related work mtl

**Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Factorial Analysis** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 27
- **Recorded user turns:** 0
- **Tool calls:** 13
- **Original source:** `logs/chats/worker_paper_related_work_mtl_20260523T065237.jsonl`
- **Structured JSON:** [`6e7a475dc44648ec7577.json`](../../sessions/6e/6e7a475dc44648ec7577.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

27 recorded events

### Tool call

_source line 1 · 2026-05-23T06:57:18.346069+00:00_

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
  "session": "worker_paper_related_work_mtl_20260523T065237",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/agent-ml-research/skills/global/paper-writing-norms.skill.md"
  }
}
```

</details>

---

### Tool result

_source line 2 · 2026-05-23T06:57:18.346705+00:00_

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
  "session": "worker_paper_related_work_mtl_20260523T065237",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-23T06:57:18.346927+00:00_

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
  "session": "worker_paper_related_work_mtl_20260523T065237",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/docs/paper/related_work.tex"
  }
}
```

</details>

---

### Tool result

_source line 4 · 2026-05-23T06:57:18.347123+00:00_

1	
2	\section{Related Work}
3	
4	\subsection{Safety in Vision-Language-Action Models}
5	
6	Vision-language-action (VLA) models achieve high task success rates on manipulation benchmarks~\cite{kim2024openvla, brohan2023rt2} % Kim et al., OpenVLA, arXiv:2406.09246; Brohan et al., RT-2, arXiv:2307.15818
7	but remain prone to collisions when obstacles occupy the manipulation workspace. Two strategies have emerged to address this gap between task completion and behavioral safety.
8	
9	The first strategy applies runtime constraints to filter or adjust unsafe actions. The AEGIS framework~\cite{hu2025vlsa} % Hu et al., "VLSA: Vision-Language-Action Models with Plug-and-Play Safety Constraint Layer", arXiv:2512.11891, 2025
10	adds a plug-and-play safety layer that identifies obstacles through a vision-language assessment module and enforces avoidance via a control barrier function (CBF) quadratic program, improving collision avoidance rate by 59.16 percentage points on SafeLIBERO, a benchmark of 32 safety-critical manipulation scenarios introduced in the same work. CoFreeVLA~\cite{zhai2026cofreevla} % Zhai et al., "CoFreeVLA: Collision-Free Dual-Arm Manipulation via VLA Model and Risk Estimation", arXiv:2601.21712, 2026
11	addresses a related problem in dual-arm settings by training a short-horizon collision risk estimator that gates risky commands and triggers recovery to safe configurations. Control barrier functions have also been applied directly to manipulation independently of VLAs. Morton and Pavone~\cite{morton2025oscbf} % Morton and Pavone, "Safe, Task-Consistent Manipulation with Operational Space Control Barrier Functions", IROS 2025, arXiv:2503.06736
12	formulate operational-space CBFs that scale to hundreds of simultaneous constraints at real-time control rates, and Raja et al.~\cite{raja2024ogmcbf} % Raja et al., "Safe Robot Control using Occupancy Grid Map-based Control Barrier Function (OGM-CBF)", arXiv:2405.10703, 2024
13	construct CBFs from occupancy grid m
…[truncated 8106 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_related_work_mtl_20260523T065237",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-23T06:57:18.347276+00:00_

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
  "session": "worker_paper_related_work_mtl_20260523T065237",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/docs/paper/references.bib"
  }
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-23T06:57:18.347509+00:00_

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
32	@article{yu2026safenightvla,
33	  author    = {Yu and others},
34	  title     = {{Safe-Night VLA}: Seeing the Unseen via Thermal-Perceptive Vision-Language-Action Models for Safety-Critical Manipulation},
35	  journal   = {arXiv preprint arXiv:2603.05754},
36	  year      = {2026},
37	  note      = {arXiv:2603.05754}
38	}
39	
40	@article{li2026vlasafety,
41	  author    = {Li and others},
42	  title     = {Vision-Language-Action Safety: Threats, Challenges, Evaluations, and Mechanisms},
43	  journal   = {arXiv preprint arXiv:2604.23775},
44	  year      = {2026},
45	  note      = {arXiv:2604.23775}
46	}
47	
48	% ============================================================
49	% Safety Mechanisms (barrier functions / occupancy-based sa
…[truncated 15506 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_related_work_mtl_20260523T065237",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-23T06:57:18.347743+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:WebSearch",
  "max_results": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_related_work_mtl_20260523T065237",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:WebSearch",
    "max_results": "1"
  }
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-23T06:57:18.347897+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_related_work_mtl_20260523T065237",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-23T06:57:18.348021+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "GradNorm Chen ICML 2018 gradient normalization multi-task learning"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_related_work_mtl_20260523T065237",
  "tool": "WebSearch",
  "tool_args": {
    "query": "GradNorm Chen ICML 2018 gradient normalization multi-task learning"
  }
}
```

</details>

---

### Tool call

_source line 10 · 2026-05-23T06:57:18.348139+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "PCGrad Yu NeurIPS 2020 gradient surgery multi-task learning"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_related_work_mtl_20260523T065237",
  "tool": "WebSearch",
  "tool_args": {
    "query": "PCGrad Yu NeurIPS 2020 gradient surgery multi-task learning"
  }
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-23T06:57:18.348254+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "CAGrad Liu NeurIPS 2021 conflict-averse gradient descent multi-task"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_related_work_mtl_20260523T065237",
  "tool": "WebSearch",
  "tool_args": {
    "query": "CAGrad Liu NeurIPS 2021 conflict-averse gradient descent multi-task"
  }
}
```

</details>

---

### Tool call

_source line 12 · 2026-05-23T06:57:18.348368+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "NashMTL Navon ICML 2022 Nash bargaining multi-task learning"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_related_work_mtl_20260523T065237",
  "tool": "WebSearch",
  "tool_args": {
    "query": "NashMTL Navon ICML 2022 Nash bargaining multi-task learning"
  }
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-23T06:57:18.348479+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "EWC Kirkpatrick 2017 elastic weight consolidation catastrophic forgetting"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_related_work_mtl_20260523T065237",
  "tool": "WebSearch",
  "tool_args": {
    "query": "EWC Kirkpatrick 2017 elastic weight consolidation catastrophic forgetting"
  }
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-23T06:57:18.348627+00:00_

Web search results for query: "PCGrad Yu NeurIPS 2020 gradient surgery multi-task learning"

Links: [{"title":"Yu Et Al. - 2020 - Gradient Surgery for Multi-Task Learning","url":"https://www.scribd.com/document/558287008/Yu-Et-Al-2020-Gradient-Surgery-for-Multi-Task-Learning"},{"title":"[Quick Review] Gradient Surgery for Multi-Task Learning","url":"https://liner.com/review/gradient-surgery-for-multitask-learning"},{"title":"Implement PCGrad (Projecting Conflicting Gradients) for Multi-Task Optimization · Issue #51 · 0-5788719150923125/praxis","url":"https://github.com/0-5788719150923125/praxis/issues/51"},{"title":"Gradient Surgery for Multi-Task Learning","url":"https://proceedings.neurips.cc/paper/2020/file/3fe78a8acf5fda99de95303940a2420c-Paper.pdf"},{"title":"GradAttention: Attention-Based Gradient Surgery for Multitask Fine-Tuning","url":"https://web.stanford.edu/class/archive/cs/cs224n/cs224n.1244/final-projects/AnilYildiz.pdf"},{"title":"Gradient Descent in Multi-Task Learning Stanford CS224N Default Project","url":"https://web.stanford.edu/class/archive/cs/cs224n/cs224n.1244/final-projects/DavidSaykinKfirShmuelDolev.pdf"},{"title":"GitHub - tianheyu927/PCGrad: Code for \"Gradient Surgery for Multi-Task Learning\" · GitHub","url":"https://github.com/tianheyu927/PCGrad"},{"title":"Gradient Surgery for Multi-Task Learning","url":"https://arxiv.org/pdf/2001.06782"},{"title":"Review for NeurIPS paper: Gradient Surgery for Multi-Task Learning","url":"https://proceedings.neurips.cc/paper_files/paper/2020/file/3fe78a8acf5fda99de95303940a2420c-Review.html"},{"title":"[2001.06782] Gradient Surgery for Multi-Task Learning","url":"https://arxiv.org/abs/2001.06782"}]

Based on the search results, here's information about the PCGrad paper:

## Overview

PCGrad is a gradient surgery method mitigating detrimental gradient interference in multi-task learning presented at NeurIPS 2020. The paper was authored by Tianhe Yu, Saurabh Kumar, Abhishek Gupta, Sergey Levine, Karol H
…[truncated 1176 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_related_work_mtl_20260523T065237",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 15 · 2026-05-23T06:57:18.348835+00:00_

Web search results for query: "GradNorm Chen ICML 2018 gradient normalization multi-task learning"

Links: [{"title":"GradNorm: Adaptive Loss Balancing for Multitask Networks","url":"https://www.emergentmind.com/papers/1711.02257"},{"title":"Gradnorm: Gradient Normalization For Adaptive Loss Balancing in Deep Multitask Networks | PDF | Image Segmentation | Computer Science","url":"https://www.scribd.com/document/615850392/1711-02257"},{"title":"(PDF) GradNorm: Gradient Normalization for Adaptive Loss Balancing in Deep Multitask Networks","url":"https://www.researchgate.net/publication/320920333_GradNorm_Gradient_Normalization_for_Adaptive_Loss_Balancing_in_Deep_Multitask_Networks"},{"title":"GitHub - hosseinshn/GradNorm: This in my Demo of Chen et al. \"GradNorm: Gradient Normalization for Adaptive Loss Balancing in Deep Multitask Networks\" ICML 2018 · GitHub","url":"https://github.com/hosseinshn/GradNorm"},{"title":"GradNorm: Gradient Normalization for Adaptive Loss Balancing in Deep Multitask Networks","url":"https://proceedings.mlr.press/v80/chen18a.html"},{"title":"models/grad-norm/README.md at master · chainer/models","url":"https://github.com/chainer/models/blob/master/grad-norm/README.md"},{"title":"[1711.02257] GradNorm: Gradient Normalization for Adaptive Loss Balancing in Deep Multitask Networks","url":"https://arxiv.org/abs/1711.02257"},{"title":"Under review as a conference paper at ICLR 2018 GRADNORM: GRADIENT","url":"https://openreview.net/pdf?id=H1bM1fZCW"},{"title":"GradNorm: Gradient Normalization for Adaptive Loss ...","url":"https://arxiv.org/pdf/1711.02257"}]

I found comprehensive information about GradNorm. Here's what the search revealed:

## Overview

GradNorm is a gradient normalization algorithm that automatically balances training in deep multitask models by dynamically tuning gradient magnitudes. The paper was authored by Zhao Chen, Vijay Badrinarayanan, Chen-Yu Lee, and Andrew Rabinovich and was published in the Proceedings of the 35th 
…[truncated 1132 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_related_work_mtl_20260523T065237",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-23T06:57:18.349016+00:00_

Web search results for query: "CAGrad Liu NeurIPS 2021 conflict-averse gradient descent multi-task"

Links: [{"title":"Conflict-Averse Gradient Descent for Multi-task Learning [Quick Review]","url":"https://liner.com/review/conflictaverse-gradient-descent-for-multitask-learning"},{"title":"Conflict-Averse Gradient Descent for Multi-task Learning","url":"https://www.cs.utexas.edu/~pstone/Papers/bib2html-links/NeurIPS2021-Liu.pdf"},{"title":"Conflict-Averse Gradient Descent for Multi-task learning","url":"https://proceedings.neurips.cc/paper/2021/hash/9d27fdf2477ffbff837d73ef7ae23db9-Abstract.html"},{"title":"Peter Stone: Conflict-Averse Gradient Descent for Multi-task learning","url":"https://www.cs.utexas.edu/~pstone/Papers/bib2html/b2hd-NeurIPS2021-Liu.html"},{"title":"[2110.14048] Conflict-Averse Gradient Descent for Multi-task Learning","url":"https://arxiv.org/abs/2110.14048"},{"title":"Conflict-Averse Gradient Descent for Multi-task Learning","url":"https://arxiv.org/pdf/2110.14048"},{"title":"GitHub - Cranial-XIX/CAGrad: Official PyTorch Implementation for Conflict-Averse Gradient Descent (CAGrad) · GitHub","url":"https://github.com/Cranial-XIX/CAGrad"},{"title":"(PDF) Conflict-Averse Gradient Descent for Multi-task Learning","url":"https://www.researchgate.net/publication/355698823_Conflict-Averse_Gradient_Descent_for_Multi-task_Learning"},{"title":"Conflict-Averse Gradient Descent for Multi-task Learning","url":"https://oamonitor.ireland.openaire.eu/rpo/rcsi/search/publication?pid=10.48550/arxiv.2110.14048"},{"title":"NeurIPS Poster Conflict-Averse Gradient Descent for Multi-task learning","url":"https://neurips.cc/virtual/2021/poster/27328"}]

Based on the search results, here's information about the CAGrad paper presented at NeurIPS 2021:

## Overview

CAGrad (Conflict-Averse Gradient Descent) was authored by Bo Liu, Xingchao Liu, Xiaojie Jin, Peter Stone, and Qiang Liu from The University of Texas at Austin, Sony AI, and Bytedance Research, and was presen
…[truncated 1346 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_related_work_mtl_20260523T065237",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 17 · 2026-05-23T06:57:18.349190+00:00_

Web search results for query: "NashMTL Navon ICML 2022 Nash bargaining multi-task learning"

Links: [{"title":"Releases · AvivNavon/nash-mtl","url":"https://github.com/AvivNavon/nash-mtl/releases"},{"title":"Multi-Task Learning as a Bargaining Game [Quick Review]","url":"https://liner.com/review/multitask-learning-as-bargaining-game?entry-type=quick_review_inventory"},{"title":"Multi-Task Learning as a Bargaining Game - Bar-Ilan University","url":"https://cris.biu.ac.il/en/publications/multi-task-learning-as-a-bargaining-game/"},{"title":"GitHub - AvivNavon/nash-mtl: Official implementation of \"Multi-Task Learning as a Bargaining Game\" [ICML 2022]","url":"https://github.com/AvivNavon/nash-mtl"},{"title":"Multi-Task Learning as a Bargaining Game","url":"https://arxiv.org/pdf/2202.01017"},{"title":"(PDF) Multi-Task Learning as a Bargaining Game","url":"https://www.researchgate.net/publication/358306683_Multi-Task_Learning_as_a_Bargaining_Game"},{"title":"[2202.01017] Multi-Task Learning as a Bargaining Game","url":"https://arxiv.org/abs/2202.01017"},{"title":"Multi-Task Learning as a Bargaining Game A. Navon1 A. Shamsian1 I. Achituve1","url":"https://icml.cc/media/icml-2022/Slides/17114.pdf"}]

The search has found comprehensive information about NashMTL and the Navon paper from ICML 2022. Here's what I found:

## Overview

NashMTL is the official implementation of "Multi-Task Learning as a Bargaining Game" presented at ICML 2022. The paper was authored by Aviv Navon and colleagues, and the conference took place from July 17-23, 2022.

## Core Concept

The paper proposes viewing the gradients combination step as a bargaining game, where tasks negotiate to reach an agreement on a joint direction of parameter update. Under certain assumptions, the bargaining problem has a unique solution, known as the Nash Bargaining Solution, which is proposed as a principled approach to multi-task learning.

## Key Features

NashMTL utilizes the Nash Bargaining Solution as a princip
…[truncated 749 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_related_work_mtl_20260523T065237",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-23T06:57:18.349360+00:00_

Web search results for query: "EWC Kirkpatrick 2017 elastic weight consolidation catastrophic forgetting"

Links: [{"title":"[1712.03847] On Quadratic Penalties in Elastic Weight Consolidation","url":"https://arxiv.org/abs/1712.03847"},{"title":"On Quadratic Penalties in Elastic Weight Consolidation","url":"https://www.researchgate.net/publication/321745400_On_Quadratic_Penalties_in_Elastic_Weight_Consolidation"},{"title":"Overcoming Catastrophic Forgetting: A Simple Guide to Elastic Weight Consolidation | Towards AI","url":"https://towardsai.net/p/l/overcoming-catastrophic-forgetting-a-simple-guide-to-elastic-weight-consolidation"},{"title":"Overcoming Catastrophic Forgetting: Elastic Weight Consolidation And Replay Buffers For Lifelong AI - American Technology Consulting","url":"https://blog.american-technology.net/overcoming-catastrophic-forgetting/"},{"title":"Overcoming Catastrophic Forgetting: A Simple Guide to Elastic Weight Consolidation | by Yunzhe Wang | Towards AI","url":"https://pub.towardsai.net/overcoming-catastrophic-forgetting-a-simple-guide-to-elastic-weight-consolidation-122d7ac54328?gi=af55bbc9fc4f"},{"title":"[Regular] Elastic Weight Consolidation for Knowledge ...","url":"https://openreview.net/pdf?id=crDZvvvZi6"},{"title":"On Quadratic Penalties in Elastic Weight Consolidation","url":"https://arxiv.org/pdf/1712.03847"},{"title":"Note on the quadratic penalties in elastic weight consolidation - PMC","url":"https://pmc.ncbi.nlm.nih.gov/articles/PMC5856534/"},{"title":"Overcoming Catastrophic Forgetting - Rylan Schaeffer","url":"https://rylanschaeffer.github.io/content/research/elastic_weight_consolidation/main.html"}]

I found comprehensive information about EWC and Kirkpatrick's 2017 work. Here are the key findings:

## Overview

Elastic weight consolidation (EWC, Kirkpatrick et al, 2017) is a novel algorithm designed to safeguard against catastrophic forgetting in neural networks.

## The Problem: Catastrophic Forgetting

The naive approach of 
…[truncated 1170 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_related_work_mtl_20260523T065237",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-23T06:57:18.349717+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/docs/paper/related_work.tex",
  "old_string": ". These results predict that auxiliary objectives during fine-tuning should help preserve the diversity of the pretrained representation.\n\nFor VLA fine-tuning,",
  "new_string": ". These results predict that auxiliary objectives during fine-tuning should help preserve the diversity of the pretrained representation.\n\n\\paragraph{Multi-Task Gradient Dynamics.}\nA parallel line of work in multi-task optimization focuses on resolving gradient conflicts between co-trained objectives. A family of methods manipulates task gradients at each update step: GradNorm~\\cite{chen2018gradnorm} dynamically reweights loss magnitudes, PCGrad~\\cite{yu2020pcgrad} projects conflicting gradient pairs onto each other's normal planes, and more recent approaches seek provably convergent update rules through worst-case optimization~\\cite{liu2021cagrad} or Nash bargaining~\\cite{navon2022nashmtl}. These methods share a common premise: task gradients conflict, and the optimizer must resolve that conflict to avoid performance degradation. Our gradient analysis reveals that this premise does not hold for auxiliary spatial supervision in VLA fine-tuning. Action and occupancy gradients remain nearly orthogonal (cosine similarity $\\approx 0$) throughout training, with per-parameter conflict rates of 42--57\\%, close to the 50\\% random baseline. This places our setting in a benign regime where gradient projection or reweighting has little to act on. The more consequential phenomenon is not gradient conflict but gradient amplification: occupancy supervision increases the magnitude of action-aligned gradients by 8--69$\\times$ relative to action-only training. This indicates that the auxiliary task's primary benefit operates through gradient flow rather than conflict resolution.\n\nThis observation also connects to catastrophic forgetting in continual learning. Elastic Weight Consolidation (EWC)~\\cite{kirkpatrick2017ewc} prevents forgetting by adding quadratic penalties that protect parameters important for previous tasks. Auxiliary occupancy supervision achieves a functionally analogous outcome: the continuous spatial gradient signal maintains encoder feature diversity and counteracts the representation drift that accompanies single-task fine-tuning. Where EWC requires explicit regularization terms, multi-task training provides implicit protection through shared gradient flow.\n\nFor VLA fine-tuning,"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_related_work_mtl_20260523T065237",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/docs/paper/related_work.tex",
    "old_string": ". These results predict that auxiliary objectives during fine-tuning should help preserve the diversity of the pretrained representation.\n\nFor VLA fine-tuning,",
    "new_string": ". These results predict that auxiliary objectives during fine-tuning should help preserve the diversity of the pretrained representation.\n\n\\paragraph{Multi-Task Gradient Dynamics.}\nA parallel line of work in multi-task optimization focuses on resolving gradient conflicts between co-trained objectives. A family of methods manipulates task gradients at each update step: GradNorm~\\cite{chen2018gradnorm} dynamically reweights loss magnitudes, PCGrad~\\cite{yu2020pcgrad} projects conflicting gradient pairs onto each other's normal planes, and more recent approaches seek provably convergent update rules through worst-case optimization~\\cite{liu2021cagrad} or Nash bargaining~\\cite{navon2022nashmtl}. These methods share a common premise: task gradients conflict, and the optimizer must resolve that conflict to avoid performance degradation. Our gradient analysis reveals that this premise does not hold for auxiliary spatial supervision in VLA fine-tuning. Action and occupancy gradients remain nearly orthogonal (cosine similarity $\\approx 0$) throughout training, with per-parameter conflict rates of 42--57\\%, close to the 50\\% random baseline. This places our setting in a benign regime where gradient projection or reweighting has little to act on. The more consequential phenomenon is not gradient conflict but gradient amplification: occupancy supervision increases the magnitude of action-aligned gradients by 8--69$\\times$ relative to action-only training. This indicates that the auxiliary task's primary benefit operates through gradient flow rather than conflict resolution.\n\nThis observation also connects to catastrophic forgetting in continual learning. Elastic Weight Consolidation (EWC)~\\cite{kirkpatrick2017ewc} prevents forgetting by adding quadratic penalties that protect parameters important for previous tasks. Auxiliary occupancy supervision achieves a functionally analogous outcome: the continuous spatial gradient signal maintains encoder feature diversity and counteracts the representation drift that accompanies single-task fine-tuning. Where EWC requires explicit regularization terms, multi-task training provides implicit protection through shared gradient flow.\n\nFor VLA fine-tuning,"
  }
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-23T06:57:18.349946+00:00_

The file /home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/docs/paper/related_work.tex has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_related_work_mtl_20260523T065237",
  "tool": "Edit",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 21 · 2026-05-23T06:57:18.350091+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/docs/paper/references.bib",
  "old_string": "@inproceedings{foret2021sam,\n  author    = {Pierre Foret and Ariel Kleiner and Hossein Mobahi and Behnam Neyshabur},\n  title     = {Sharpness-Aware Minimization for Efficiently Improving Generalization},\n  booktitle = {International Conference on Learning Representations (ICLR)},\n  year      = {2021},\n  note      = {arXiv:2010.01412}\n}\n\n% ============================================================\n% Parameter-Efficient Fine-Tuning",
  "new_string": "@inproceedings{foret2021sam,\n  author    = {Pierre Foret and Ariel Kleiner and Hossein Mobahi and Behnam Neyshabur},\n  title     = {Sharpness-Aware Minimization for Efficiently Improving Generalization},\n  booktitle = {International Conference on Learning Representations (ICLR)},\n  year      = {2021},\n  note      = {arXiv:2010.01412}\n}\n\n@inproceedings{chen2018gradnorm,\n  author    = {Zhao Chen and Vijay Badrinarayanan and Chen-Yu Lee and Andrew Rabinovich},\n  title     = {{GradNorm}: Gradient Normalization for Adaptive Loss Balancing in Deep Multitask Networks},\n  booktitle = {International Conference on Machine Learning (ICML)},\n  year      = {2018},\n  note      = {arXiv:1711.02257}\n}\n\n@inproceedings{yu2020pcgrad,\n  author    = {Tianhe Yu and Saurabh Kumar and Abhishek Gupta and Sergey Levine and Karol Hausman and Chelsea Finn},\n  title     = {Gradient Surgery for Multi-Task Learning},\n  booktitle = {Advances in Neural Information Processing Systems (NeurIPS)},\n  year      = {2020},\n  note      = {arXiv:2001.06782}\n}\n\n@inproceedings{liu2021cagrad,\n  author    = {Bo Liu and Xingchao Liu and Xiaojie Jin and Peter Stone and Qiang Liu},\n  title     = {Conflict-Averse Gradient Descent for Multi-task Learning},\n  booktitle = {Advances in Neural Information Processing Systems (NeurIPS)},\n  year      = {2021},\n  note      = {arXiv:2110.14048}\n}\n\n@inproceedings{navon2022nashmtl,\n  author    = {Aviv Navon and Aviv Shamsian and Idan Achituve and Haggai Maron and Kenji Kawaguchi and Gal Chechik and Ethan Fetaya},\n  title     = {Multi-Task Learning as a Bargaining Game},\n  booktitle = {International Conference on Machine Learning (ICML)},\n  year      = {2022},\n  note      = {arXiv:2202.01017}\n}\n\n@article{kirkpatrick2017ewc,\n  author    = {James Kirkpatrick and others},\n  title     = {Overcoming Catastrophic Forgetting in Neural Networks},\n  journal   = {Proceedings of the National Academy of Sciences (PNAS)},\n  volume    = {114},\n  number    = {13},\n  pages     = {3521--3526},\n  year      = {2017},\n  note      = {arXiv:1612.00796}\n}\n\n% ============================================================\n% Parameter-Efficient Fine-Tuning"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_related_work_mtl_20260523T065237",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/docs/paper/references.bib",
    "old_string": "@inproceedings{foret2021sam,\n  author    = {Pierre Foret and Ariel Kleiner and Hossein Mobahi and Behnam Neyshabur},\n  title     = {Sharpness-Aware Minimization for Efficiently Improving Generalization},\n  booktitle = {International Conference on Learning Representations (ICLR)},\n  year      = {2021},\n  note      = {arXiv:2010.01412}\n}\n\n% ============================================================\n% Parameter-Efficient Fine-Tuning",
    "new_string": "@inproceedings{foret2021sam,\n  author    = {Pierre Foret and Ariel Kleiner and Hossein Mobahi and Behnam Neyshabur},\n  title     = {Sharpness-Aware Minimization for Efficiently Improving Generalization},\n  booktitle = {International Conference on Learning Representations (ICLR)},\n  year      = {2021},\n  note      = {arXiv:2010.01412}\n}\n\n@inproceedings{chen2018gradnorm,\n  author    = {Zhao Chen and Vijay Badrinarayanan and Chen-Yu Lee and Andrew Rabinovich},\n  title     = {{GradNorm}: Gradient Normalization for Adaptive Loss Balancing in Deep Multitask Networks},\n  booktitle = {International Conference on Machine Learning (ICML)},\n  year      = {2018},\n  note      = {arXiv:1711.02257}\n}\n\n@inproceedings{yu2020pcgrad,\n  author    = {Tianhe Yu and Saurabh Kumar and Abhishek Gupta and Sergey Levine and Karol Hausman and Chelsea Finn},\n  title     = {Gradient Surgery for Multi-Task Learning},\n  booktitle = {Advances in Neural Information Processing Systems (NeurIPS)},\n  year      = {2020},\n  note      = {arXiv:2001.06782}\n}\n\n@inproceedings{liu2021cagrad,\n  author    = {Bo Liu and Xingchao Liu and Xiaojie Jin and Peter Stone and Qiang Liu},\n  title     = {Conflict-Averse Gradient Descent for Multi-task Learning},\n  booktitle = {Advances in Neural Information Processing Systems (NeurIPS)},\n  year      = {2021},\n  note      = {arXiv:2110.14048}\n}\n\n@inproceedings{navon2022nashmtl,\n  author    = {Aviv Navon and Aviv Shamsian and Idan Achituve and Haggai Maron and Kenji Kawaguchi and Gal Chechik and Ethan Fetaya},\n  title     = {Multi-Task Learning as a Bargaining Game},\n  booktitle = {International Conference on Machine Learning (ICML)},\n  year      = {2022},\n  note      = {arXiv:2202.01017}\n}\n\n@article{kirkpatrick2017ewc,\n  author    = {James Kirkpatrick and others},\n  title     = {Overcoming Catastrophic Forgetting in Neural Networks},\n  journal   = {Proceedings of the National Academy of Sciences (PNAS)},\n  volume    = {114},\n  number    = {13},\n  pages     = {3521--3526},\n  year      = {2017},\n  note      = {arXiv:1612.00796}\n}\n\n% ============================================================\n% Parameter-Efficient Fine-Tuning"
  }
}
```

</details>

---

### Tool result

_source line 22 · 2026-05-23T06:57:18.350302+00:00_

The file /home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/docs/paper/references.bib has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_related_work_mtl_20260523T065237",
  "tool": "Edit",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 23 · 2026-05-23T06:57:18.350463+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/docs/paper/related_work.tex",
  "offset": "40",
  "limit": "35"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_related_work_mtl_20260523T065237",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/docs/paper/related_work.tex",
    "offset": "40",
    "limit": "35"
  }
}
```

</details>

---

### Tool result

_source line 24 · 2026-05-23T06:57:18.350647+00:00_

40	\subsection{Auxiliary Tasks and Regularization in Fine-Tuning}
41	
42	Multi-task learning improves generalization by training on related objectives through a shared representation~\cite{caruana1997multitask} % Caruana, "Multitask Learning", Machine Learning 28:41-75, 1997
43	. Auxiliary tasks act as inductive biases that prevent the shared encoder from overfitting to the primary objective~\cite{ruder2017overview} % Ruder, "An Overview of Multi-Task Learning in Deep Neural Networks", arXiv:1706.05098, 2017
44	. Recent theoretical work by Lippl and Lindsey~\cite{lippl2024implicit} % Lippl and Lindsey, "Implicit Regularization of Multi-Task Learning and Finetuning in Overparameterized Neural Networks", ICLR 2024, arXiv:2310.02396
45	shows that multi-task learning in overparameterized networks induces an $\ell_{1,2}$ mixed-norm implicit regularization that encourages feature sharing across tasks, while fine-tuning exhibits ``nested feature selection'' that retains sparse subsets of pretrained features. These results predict that auxiliary objectives during fine-tuning should help preserve the diversity of the pretrained representation.
46	
47	\paragraph{Multi-Task Gradient Dynamics.}
48	A parallel line of work in multi-task optimization focuses on resolving gradient conflicts between co-trained objectives. A family of methods manipulates task gradients at each update step: GradNorm~\cite{chen2018gradnorm} dynamically reweights loss magnitudes, PCGrad~\cite{yu2020pcgrad} projects conflicting gradient pairs onto each other's normal planes, and more recent approaches seek provably convergent update rules through worst-case optimization~\cite{liu2021cagrad} or Nash bargaining~\cite{navon2022nashmtl}. These methods share a common premise: task gradients conflict, and the optimizer must resolve that conflict to avoid performance degradation. Our gradient analysis reveals that this premise does not hold for auxiliary spatial supervision in VLA fine-tuning. Action and occupa
…[truncated 2488 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_related_work_mtl_20260523T065237",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 25 · 2026-05-23T06:57:18.350820+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/docs/paper/references.bib",
  "offset": "380",
  "limit": "60"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_related_work_mtl_20260523T065237",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/docs/paper/references.bib",
    "offset": "380",
    "limit": "60"
  }
}
```

</details>

---

### Tool result

_source line 26 · 2026-05-23T06:57:18.350965+00:00_

380	
381	@inproceedings{foret2021sam,
382	  author    = {Pierre Foret and Ariel Kleiner and Hossein Mobahi and Behnam Neyshabur},
383	  title     = {Sharpness-Aware Minimization for Efficiently Improving Generalization},
384	  booktitle = {International Conference on Learning Representations (ICLR)},
385	  year      = {2021},
386	  note      = {arXiv:2010.01412}
387	}
388	
389	@inproceedings{chen2018gradnorm,
390	  author    = {Zhao Chen and Vijay Badrinarayanan and Chen-Yu Lee and Andrew Rabinovich},
391	  title     = {{GradNorm}: Gradient Normalization for Adaptive Loss Balancing in Deep Multitask Networks},
392	  booktitle = {International Conference on Machine Learning (ICML)},
393	  year      = {2018},
394	  note      = {arXiv:1711.02257}
395	}
396	
397	@inproceedings{yu2020pcgrad,
398	  author    = {Tianhe Yu and Saurabh Kumar and Abhishek Gupta and Sergey Levine and Karol Hausman and Chelsea Finn},
399	  title     = {Gradient Surgery for Multi-Task Learning},
400	  booktitle = {Advances in Neural Information Processing Systems (NeurIPS)},
401	  year      = {2020},
402	  note      = {arXiv:2001.06782}
403	}
404	
405	@inproceedings{liu2021cagrad,
406	  author    = {Bo Liu and Xingchao Liu and Xiaojie Jin and Peter Stone and Qiang Liu},
407	  title     = {Conflict-Averse Gradient Descent for Multi-task Learning},
408	  booktitle = {Advances in Neural Information Processing Systems (NeurIPS)},
409	  year      = {2021},
410	  note      = {arXiv:2110.14048}
411	}
412	
413	@inproceedings{navon2022nashmtl,
414	  author    = {Aviv Navon and Aviv Shamsian and Idan Achituve and Haggai Maron and Kenji Kawaguchi and Gal Chechik and Ethan Fetaya},
415	  title     = {Multi-Task Learning as a Bargaining Game},
416	  booktitle = {International Conference on Machine Learning (ICML)},
417	  year      = {2022},
418	  note      = {arXiv:2202.01017}
419	}
420	
421	@article{kirkpatrick2017ewc,
422	  author    = {James Kirkpatrick and others},
423	  title     = {Overcoming Catastrop
…[truncated 777 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_related_work_mtl_20260523T065237",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 27 · 2026-05-23T06:57:18.351152+00:00_

已完成。

**related_work.tex** (lines 47-50): 在 "Auxiliary Tasks and Regularization" 子节中插入了 `\paragraph{Multi-Task Gradient Dynamics.}` 段落（12 句），结构为：
1. 介绍 GradNorm/PCGrad/CAGrad/NashMTL 的共同前提（gradient conflict）
2. 用实验数据（cosine ≈ 0, conflict rate 42-57%）说明本文处于 benign regime，conflict management 不适用
3. 核心论点：gradient amplification (8-69×) 而非 conflict resolution
4. EWC 连接：auxiliary supervision 通过 shared gradient flow 隐式实现类似 EWC 的 feature protection

**references.bib**: 新增 6 条 bib 条目（chen2018gradnorm, yu2020pcgrad, liu2021cagrad, navon2022nashmtl, kirkpatrick2017ewc），放在 Multi-Task Learning / Regularization 分区内。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_paper_related_work_mtl_20260523T065237"
}
```

</details>

---
