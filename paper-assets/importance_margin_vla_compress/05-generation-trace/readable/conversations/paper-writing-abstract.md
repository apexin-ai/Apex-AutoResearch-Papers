# paper writing abstract

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 17
- **Recorded user turns:** 0
- **Tool calls:** 8
- **Original source:** `logs/chats/worker_paper_writing_abstract_20260523T020351.jsonl`
- **Structured JSON:** [`f956074875d5be0546f6.json`](../../sessions/f9/f956074875d5be0546f6.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

17 recorded events

### Tool call

_source line 1 · 2026-05-23T02:08:30.716319+00:00_

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
  "session": "worker_paper_writing_abstract_20260523T020351",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/agent-ml-research/skills/global/paper-writing-norms.skill.md"
  }
}
```

</details>

---

### Tool result

_source line 2 · 2026-05-23T02:08:30.716947+00:00_

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
  "session": "worker_paper_writing_abstract_20260523T020351",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-23T02:08:30.717225+00:00_

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
  "session": "worker_paper_writing_abstract_20260523T020351",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/agent-ml-research/skills/global/latex-paper.skill.md"
  }
}
```

</details>

---

### Tool result

_source line 4 · 2026-05-23T02:08:30.717607+00:00_

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
  "session": "worker_paper_writing_abstract_20260523T020351",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-23T02:08:30.717783+00:00_

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
  "session": "worker_paper_writing_abstract_20260523T020351",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/introduction.tex"
  }
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-23T02:08:30.717944+00:00_

1	\section{Introduction}
2	\label{sec:introduction}
3	
4	Remove 5\% of vision tokens from SmolVLA and its success rate collapses from 59.2\% to 0.0\% across all task suites and pruning methods. Apply the same 5\% reduction to $\pi_0.5$ and it retains 98.2\%. Both are Vision-Language-Action (VLA) models built on a Vision Transformer (ViT) encoder feeding tokens through a connector into a language model backbone; the critical difference is not model scale (450M vs.\ 4B parameters) but the connector architecture. Token pruning is well-established for image classification, where DynamicViT~\cite{rao2021dynamicvit}, Token Merging~\cite{bolya2023tome}, and EViT~\cite{liang2022evit} reduce computation by 50\% or more with minimal accuracy loss. A growing body of work extends these techniques to VLAs: VLA-IAP~\cite{wang2026vlaiap}, VLA-Cache~\cite{hsu2025vlacache}, EfficientVLA~\cite{yang2025efficientvla}, and VLA-Pruner~\cite{liu2025vlapruner} each demonstrate efficiency gains on individual architectures.
5	
6	These methods implicitly assume that token pruning effectiveness transfers across VLA designs. Yet current VLAs employ fundamentally different vision connectors: linear projections~\cite{black2024pi0}, multi-layer MLP projectors~\cite{kim2024openvla}, pixel-shuffle spatial folding~\cite{shukor2025smolvla}, and learned encoders with cross-token self-attention~\cite{zheng2025xvla}. Each connector imposes distinct constraints on how visual information is distributed across tokens. Deploying a pruning method validated on one architecture to a different connector type risks silent degradation or, as the SmolVLA result above illustrates, complete loss of manipulation capability. No prior work systematically evaluates pruning robustness across both connector architectures and task complexity distributions, and the factor that determines whether a given VLA tolerates token removal remains uncharacterized.
7	
8	We propose a two-axis analysis of VLA token compressibility: prun
…[truncated 2829 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_abstract_20260523T020351",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-23T02:08:30.718097+00:00_

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
  "session": "worker_paper_writing_abstract_20260523T020351",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/conclusion.tex"
  }
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-23T02:08:30.718259+00:00_

1	\section{Conclusion}
2	\label{sec:conclusion}
3	
4	Vision token pruning in VLAs is not a uniform operation: its outcome depends on the interaction between connector architecture and task complexity. Evaluating six VLA models (450M to 7B parameters) across four LIBERO task suites, we find that connector coupling is the primary determinant of pruning robustness. Token-independent connectors (linear projections, MLP projectors) degrade proportionally to the fraction removed, while token-entangling connectors (pixel-shuffle folding, BART encoder) exhibit task-amplified collapse. SmolVLA's pixel-shuffle connector produces 0.0\% success rate when just 5\% of tokens are removed; X-VLA retains its full 99.2\% baseline on Object at $k{=}0.9$ but loses 27.8 percentage points on Goal at the same ratio. The coefficient of variation of post-connector token L2 norms captures this spectrum as a single-pass diagnostic: models with CV$\,{=}\,$0.055 show $15{\times}$ greater method sensitivity than those with CV$\,{\geq}\,$0.15, and this metric correlates with both pruning tolerance and the retention threshold at which method choice becomes critical. For architectures where all pruning strategies fail, Vision Token Re-encoder recovers pixel-shuffle VLAs from 0.0\% to over 60\% success rate at 75\% compression through learned re-encoding.
5	
6	These findings carry practical implications: computing CV before deployment can guide compression strategy selection without costly closed-loop evaluation. Two directions remain open. Real-robot validation is needed to confirm that the connector-complexity interaction observed in simulation transfers to physical manipulation. Adaptive per-task pruning schedules, where the retention ratio adjusts to estimated task complexity, could further close the gap between token-independent and token-entangling architectures.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_abstract_20260523T020351",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-23T02:08:30.718403+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/experiments.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_abstract_20260523T020351",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/experiments.tex"
  }
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-23T02:08:30.718611+00:00_

1	\section{Experiments}
2	\label{sec:experiments}
3	
4	\subsection{Experimental Setup}
5	\label{sec:exp_setup}
6	
7	We evaluate vision token pruning across six VLA models spanning three connector families on the LIBERO benchmark~\cite{liu2023libero}. LIBERO provides four task suites of increasing complexity: Object (object manipulation), Spatial (spatial reasoning), Goal (goal-conditioned tasks), and Long (long-horizon multi-step tasks). Each suite contains 10 tasks evaluated over 50 episodes, yielding 500 episodes per condition.
8	
9	Four models are evaluated in closed-loop robotic control: $\pi_0.5$~\cite{black2025pi05} (4B parameters, linear projection with $\times\!\sqrt{d}$ scaling, 768 tokens from three cameras, CV$\,{=}\,$0.055), X-VLA~\cite{zheng2025xvla} (880M, linear projection followed by a 12-layer BART encoder~\cite{lewis2020bart}, 50 tokens, CV$\,{=}\,$0.151), OpenVLA~\cite{kim2024openvla} (7B, three-layer MLP projector, 256 tokens, CV$\,{=}\,$0.215), and SmolVLA~\cite{shukor2025smolvla} (450M, pixel-shuffle $4{\times}4$ folding, 128 tokens, CV$\,{=}\,$0.314). Two additional models are analyzed via offline metrics only: $\pi_0$~\cite{black2024pi0} (3.3B, linear projection, 256 tokens, CV$\,{=}\,$0.038) and OFT~\cite{kim2025openoft} (7B, MLP projector, 512 tokens, CV$\,{=}\,$0.219). Table~\ref{tab:model_properties} summarizes model properties and connector details.
10	
11	The pruning protocol applies post-connector token pruning at retention ratios $k \in \{0.3, 0.5, 0.7, 0.85, 0.9, 0.95\}$. Two strategies bracket the robustness range: \textbf{L2 norm selection} ranks tokens by L2 norm and retains the top-$k$ fraction, providing an importance-based favorable test; \textbf{random subsampling} selects tokens uniformly at random, providing a conservative lower bound. Both strategies physically remove tokens and re-index position IDs. All results report mean success rate (SR) over 500 episodes with Wilson 95\% confidence intervals for single-seed conditions
…[truncated 14888 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_abstract_20260523T020351",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-23T02:08:30.718872+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls /home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/",
  "description": "List paper directory"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_abstract_20260523T020351",
  "tool": "Bash",
  "tool_args": {
    "command": "ls /home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/",
    "description": "List paper directory"
  }
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-23T02:08:30.719013+00:00_

_pdf_images
abstract.tex
analysis.tex
appendix.tex
background.tex
conclusion.tex
corl_2026.sty
corlabbrvnat.bst
discussion.tex
experimental_setup.tex
experiments.tex
experiments_deprecated.tex
figures
introduction.tex
main.aux
main.bbl
main.blg
main.fdb_latexmk
main.fls
main.log
main.out
main.pdf
main.tex
method.tex
notes
references.bib
references.bib.prev
related_work.tex
results.tex
results_v2.tex
sections

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_abstract_20260523T020351",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-23T02:08:30.719152+00:00_

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
  "session": "worker_paper_writing_abstract_20260523T020351",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/abstract.tex"
  }
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-23T02:08:30.719300+00:00_

1	\begin{abstract}
2	Vision token pruning accelerates Vision Transformer inference with negligible accuracy loss, but whether this robustness transfers to Vision-Language-Action (VLA) models remains untested across architectures. We study seven VLA models (450M--7B parameters) spanning three vision connector families, evaluating four in closed-loop robotic manipulation (LIBERO) and analyzing three via offline metrics or literature. The vision connector is strongly associated with pruning behavior along a four-class compressibility spectrum. Uniformly critical models ($\pi_0$, $\pi_0.5$; CV $< 0.06$) tolerate random subsampling but collapse under importance-based selection: $\pi_0.5$ retains 69.4\% success rate with random removal at 50\% retention but drops to 33.4\% under L2 norm selection, a 36 percentage-point gap demonstrating that offline pruning tolerance does not guarantee closed-loop robustness. Threshold-graded models (X-VLA; CV $= 0.151$) maintain $97.8 \pm 0.4$\% through 90\% retention before cliffing at 85\% ($-$31\,pp). Smooth graded models (OpenVLA, OFT; CV $\approx 0.22$) degrade proportionally. Catastrophic cliff models (SmolVLA; CV $= 0.314$) collapse to 0\% at 5\% removal across all seven tested configurations. The coefficient of variation (CV) of token L2 norms serves as a zero-cost diagnostic metric that correlates with both the tolerance class and the optimal pruning strategy from a single forward pass. The gap between random and L2 norm selection scales monotonically with CV at both 50\% and 70\% retention across three models. For catastrophic-cliff architectures, Vision Token Re-encoder (VTR) recovers 60\%+ success rate at 75\% compression where all deletion methods yield 0\%, with a relatively stable M-curve ($M{=}16 \approx M{=}128$) confirming learned re-encoding as the key factor. CV diagnosis followed by connector-appropriate compression forms a diagnostic protocol for safe VLA token reduction.
3	\end{abstract}
4	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_abstract_20260523T020351",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-23T02:08:30.719499+00:00_

called Write

<details open><summary>🔧 Tool call — Write</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/abstract.tex",
  "content": "\\begin{abstract}\nRemoving 5\\% of vision tokens collapses SmolVLA from 59.2\\% to 0.0\\% success rate, while the same reduction on $\\pi_0.5$ retains 98.2\\%. Token pruning, well-established for Vision Transformers, transfers unpredictably across Vision-Language-Action (VLA) models because the vision connector governs token compressibility. We analyze this sensitivity along two axes: connector coupling (token-independent vs.\\ token-entangling) and task complexity (single-step vs.\\ multi-step manipulation). The coefficient of variation (CV) of post-connector token L2 norms, ranging from 0.038 to 0.314 across models, serves as a single-pass diagnostic that correlates with both pruning tolerance and method sensitivity. Token-entangling connectors exhibit task-amplified collapse: X-VLA retains its full 99.2\\% baseline on single-step Object manipulation at 90\\% retention but loses 27.8 percentage points on multi-step Goal tasks at the same ratio. Low-CV models show 15$\\times$ greater sensitivity to pruning method choice than higher-CV models, and at aggressive compression random selection outperforms L2 norm ranking by 36 percentage points for low-CV architectures. For pixel-shuffle connectors where all pruning strategies yield 0.0\\%, Vision Token Re-encoder (VTR), a lightweight cross-attention module, recovers over 60\\% success rate at 75\\% compression through learned re-encoding. Evaluation spans six VLAs (450M to 7B parameters), three connector families, and four LIBERO task suites.\n\\end{abstract}\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_abstract_20260523T020351",
  "tool": "Write",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/abstract.tex",
    "content": "\\begin{abstract}\nRemoving 5\\% of vision tokens collapses SmolVLA from 59.2\\% to 0.0\\% success rate, while the same reduction on $\\pi_0.5$ retains 98.2\\%. Token pruning, well-established for Vision Transformers, transfers unpredictably across Vision-Language-Action (VLA) models because the vision connector governs token compressibility. We analyze this sensitivity along two axes: connector coupling (token-independent vs.\\ token-entangling) and task complexity (single-step vs.\\ multi-step manipulation). The coefficient of variation (CV) of post-connector token L2 norms, ranging from 0.038 to 0.314 across models, serves as a single-pass diagnostic that correlates with both pruning tolerance and method sensitivity. Token-entangling connectors exhibit task-amplified collapse: X-VLA retains its full 99.2\\% baseline on single-step Object manipulation at 90\\% retention but loses 27.8 percentage points on multi-step Goal tasks at the same ratio. Low-CV models show 15$\\times$ greater sensitivity to pruning method choice than higher-CV models, and at aggressive compression random selection outperforms L2 norm ranking by 36 percentage points for low-CV architectures. For pixel-shuffle connectors where all pruning strategies yield 0.0\\%, Vision Token Re-encoder (VTR), a lightweight cross-attention module, recovers over 60\\% success rate at 75\\% compression through learned re-encoding. Evaluation spans six VLAs (450M to 7B parameters), three connector families, and four LIBERO task suites.\n\\end{abstract}\n"
  }
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-23T02:08:30.719656+00:00_

The file /home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/abstract.tex has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_abstract_20260523T020351",
  "tool": "Write",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 17 · 2026-05-23T02:08:30.719820+00:00_

Abstract written (~195 words). Opens with the SmolVLA vs. $\pi_0.5$ finding, covers all required numbers (59.2% → 0.0%, 98.2%, 99.2%, -27.8pp, 15×, 36pp, 60%+, CV 0.038-0.314, 6 VLAs 450M-7B), uses "correlates with" for CV, no em-dashes, no banned words, no citations.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_paper_writing_abstract_20260523T020351"
}
```

</details>

---
