# paper writing discussion

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 17
- **Recorded user turns:** 0
- **Tool calls:** 8
- **Original source:** `logs/chats/worker_paper_writing_discussion_20260523T012433.jsonl`
- **Structured JSON:** [`0cd8fa1343f49f698f68.json`](../../sessions/0c/0cd8fa1343f49f698f68.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

17 recorded events

### Tool call

_source line 1 · 2026-05-23T01:27:09.048476+00:00_

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
  "session": "worker_paper_writing_discussion_20260523T012433",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/agent-ml-research/skills/global/paper-writing-norms.skill.md"
  }
}
```

</details>

---

### Tool result

_source line 2 · 2026-05-23T01:27:09.049111+00:00_

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
  "session": "worker_paper_writing_discussion_20260523T012433",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-23T01:27:09.049380+00:00_

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
  "session": "worker_paper_writing_discussion_20260523T012433",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/agent-ml-research/skills/global/latex-paper.skill.md"
  }
}
```

</details>

---

### Tool result

_source line 4 · 2026-05-23T01:27:09.049751+00:00_

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
  "session": "worker_paper_writing_discussion_20260523T012433",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-23T01:27:09.049927+00:00_

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
  "session": "worker_paper_writing_discussion_20260523T012433",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/experiments.tex"
  }
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-23T01:27:09.050168+00:00_

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
…[truncated 14895 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_discussion_20260523T012433",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-23T01:27:09.050341+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/method.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_discussion_20260523T012433",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/method.tex"
  }
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-23T01:27:09.050518+00:00_

1	\section{Method}
2	\label{sec:method}
3	
4	\subsection{Models and Connectors}
5	\label{sec:models}
6	
7	We evaluate token pruning across six VLA models spanning three vision connector families (Table~\ref{tab:model_properties}). These connectors differ in whether they process ViT patches independently or create cross-token dependencies, a distinction we formalize as \emph{coupling}.
8	
9	\textbf{Linear projection} applies a single matrix multiplication per patch. $\pi_0$~\cite{black2024pi0} projects 256 patches through a linear layer; $\pi_0.5$~\cite{black2025pi05} uses a $\times\!\sqrt{d}$-scaled linear projection across 768 tokens from three cameras. Both produce tokens with near-uniform L2 norms (CV $< 0.06$).
10	
11	\textbf{MLP projector} maps each patch through a multi-layer perceptron. OpenVLA~\cite{kim2024openvla} and OFT~\cite{kim2025openoft} both use three-layer MLPs to produce 256 and 512 tokens respectively. Each patch is processed independently, and the resulting norms exhibit a clear importance gradient (CV $\approx 0.22$).
12	
13	\textbf{Token-entangling connectors} introduce cross-token dependencies through post-projection processing. X-VLA~\cite{zheng2025xvla} feeds linearly projected tokens through a 12-layer BART encoder~\cite{lewis2020bart} to produce 50 tokens with learned cross-token dependencies via self-attention. SmolVLA~\cite{shukor2025smolvla} applies pixel-shuffle $4{\times}4$ folding that concatenates 16 contiguous patches into the channel dimension of each output token, for a total of 128 tokens.
14	
15	We classify coupling as \emph{independent} when each output token depends on a single input patch, and \emph{entangling} when output tokens encode information from multiple patches. Four models ($\pi_0.5$, X-VLA, OpenVLA, SmolVLA) are evaluated in closed-loop robotic control on LIBERO~\cite{liu2023libero}; $\pi_0$ and OFT are analyzed via offline metrics only.
16	
17	\begin{table}[t]
18	\centering
19	\small
20	\caption{VLA models evalua
…[truncated 5023 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_discussion_20260523T012433",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-23T01:27:09.050698+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/references.bib"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_discussion_20260523T012433",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/references.bib"
  }
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-23T01:27:09.051006+00:00_

1	% References for: The Cliff Edge — Why Vision Token Reduction Fails
2	% Catastrophically in VLA Closed-Loop Control
3	% Auto-generated from literature_map.yaml (verified entries only)
4	% 2026-05-17
5	
6	% ============================================================
7	% VLA Token Compression (concurrent work)
8	% ============================================================
9	
10	@article{gao2025compressorvla,
11	  title={Compressor-VLA: Instruction-Guided Visual Token Compression for Efficient Robotic Manipulation},
12	  author={Gao, Juntao and Ye, Feiyang and Zhang, Jing and Qian, Wenjing},
13	  journal={arXiv preprint arXiv:2511.18950},
14	  year={2025},
15	  eprint={2511.18950},
16	  archivePrefix={arXiv}
17	}
18	
19	@article{wang2025specprunevla,
20	  title={SpecPrune-VLA: Accelerating Vision-Language-Action Models via Action-Aware Self-Speculative Pruning},
21	  author={Wang, Hanzhen and Xu, Jiaming and Xiang, Yushun and Pan, Jiayi and Zhou, Yongkang and Li, Yong-Lu and Dai, Guohao},
22	  journal={arXiv preprint arXiv:2509.05614},
23	  year={2025},
24	  eprint={2509.05614},
25	  archivePrefix={arXiv}
26	}
27	
28	@inproceedings{jiang2026lightvla,
29	  title={The Better You Learn, The Smarter You Prune: Towards Efficient Vision-Language-Action Models via Differentiable Token Pruning},
30	  author={Jiang, Titong and Jiang, Xuefeng and Ma, Yuan and Wen, Xin and Li, Bailin and Zhan, Kun and Jia, Peng and Liu, Yahui and Sun, Sheng and Lang, Xianpeng},
31	  booktitle={Proceedings of the IEEE International Conference on Robotics and Automation (ICRA)},
32	  year={2026},
33	  eprint={2509.12594},
34	  archivePrefix={arXiv}
35	}
36	
37	@inproceedings{feng2026seewhatmatters,
38	  title={See What Matters: Differentiable Grid Sample Pruning for Generalizable Vision-Language-Action Model},
39	  author={Feng, Yixu and Zhao, Zinan and Ma, Yanxiang and Xia, Chenghao and Du, Chengbin and Wang, Yunke and Xu, Chang},
40	  booktitle={Proceedings of the Forty-Third International C
…[truncated 23526 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_discussion_20260523T012433",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-23T01:27:09.051266+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls /home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/",
  "description": "List existing paper files"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_discussion_20260523T012433",
  "tool": "Bash",
  "tool_args": {
    "command": "ls /home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/",
    "description": "List existing paper files"
  }
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-23T01:27:09.051411+00:00_

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
  "session": "worker_paper_writing_discussion_20260523T012433",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-23T01:27:09.051546+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/discussion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_discussion_20260523T012433",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/discussion.tex"
  }
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-23T01:27:09.051723+00:00_

1	\section{Discussion}
2	\label{sec:discussion}
3	
4	\subsection{Disentangling Connector Design from Model Scale}
5	\label{sec:scale_confound}
6	
7	Our cross-architecture comparison confounds the vision connector design (pixel-shuffle vs.\ MLP projector) with model scale (0.5B vs.\ 7B parameters). A larger model has more capacity to absorb perturbations through its deeper and wider attention layers, raising the question of whether SmolVLA's cliff-edge reflects architectural fragility or simply insufficient model capacity.
8	
9	Four lines of evidence favor the connector-level explanation. First, the official SmolVLA checkpoint (59.2\% SR baseline) exhibits the same cliff-edge under 50\% random pruning (0/500, 0.0\% SR), ruling out the possibility that our fine-tuned model's lower baseline (44.8\%) reflects undertrained weights that are unusually fragile. Second, SmolVLA collapses at $k = 0.95$, where only 7 of 128 tokens (5.5\%) are removed. A capacity-limited model that can solve the task with all tokens should not fail catastrophically when 95\% of the input is preserved; the perturbation is too small relative to the model's demonstrated capability. Third, the attention entropy ratio difference (0.95 vs.\ 0.64) is an architectural measurement, not a capacity measurement. SmolVLA's near-uniform attention distribution reflects the pixel-shuffle connector's output structure: because each token encodes 16 patches via channel concatenation, the resulting tokens are uniformly information-dense, and the downstream LLM has no basis for developing selective attention. OpenVLA's sharply non-uniform attention in deep layers reflects the MLP projector's preservation of per-patch granularity, which allows the model to learn which spatial locations carry task-relevant information. Fourth, the pixel-shuffle operation itself provides a mechanistic explanation: $4 \times 4$ spatial folding creates tokens whose meaning depends on the complete $4 \times 4$ grid, and removing any toke
…[truncated 11730 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_discussion_20260523T012433",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-23T01:27:09.051907+00:00_

called Write

<details open><summary>🔧 Tool call — Write</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/discussion.tex",
  "content": "\\section{Discussion}\n\\label{sec:discussion}\n\n\\paragraph{Limitations.}\nAll closed-loop evaluations use the LIBERO simulation benchmark; real-robot validation is absent. The six models differ in backbone capacity, vision encoder, and fusion strategy beyond the connector, so the connector effect cannot be causally isolated. $\\pi_0$ is evaluated through offline metrics only, without closed-loop verification. The observed correlation between CV and pruning tolerance spans only three closed-loop models ($\\pi_0.5$, X-VLA, OpenVLA), too few to establish a general relationship. SmolVLA baselines (59.2\\% official, 44.8\\% LoRA reproduction) are substantially weaker than those of the other models; whether VTR recovery generalizes to stronger baselines is unknown.\n\n\\paragraph{Non-monotonicity as structural property.}\nX-VLA on Goal exhibits non-monotonic degradation: $k{=}0.95$ drops to 53.8\\% (L2) and 54.0\\% (random), while $k{=}0.9$ recovers to 70.2\\% under L2 selection (Table~\\ref{tab:main_results}). The 0.2\\,pp method gap at $k{=}0.95$ confirms that the anomaly is independent of the token scoring criterion. This pattern is consistent with position sensitivity in the 12-layer BART encoder~\\cite{lewis2020bart}, where specific token positions carry disproportionate structural importance regardless of content.\n\n\\paragraph{$\\pi_0.5$ random subsampling anomaly.}\nRandom selection on $\\pi_0.5$ Object collapses from 69.4\\% at $k{=}0.95$ to 12.0\\% at $k{=}0.9$, then recovers to 77.2\\% at $k{=}0.7$ (Table~\\ref{tab:main_results}). The V-shaped recovery at more aggressive pruning remains unexplained.\n\n\\paragraph{Small-$N$ interactions.}\nX-VLA operates with only 50 vision tokens. At $k{=}0.95$, removing 3 tokens produces $-$44.2\\,pp on Goal and $-$47.0\\,pp on Long. Absolute token count interacts with CV: identical retention ratios impose qualitatively different damage when the token budget is small.\n\n\\paragraph{Design implications.}\nPractitioners should compute importance CV before deploying token pruning, as low-CV and entangling-connector models require distinct compression strategies. Pixel-shuffle connectors need learned re-encoding rather than hard deletion. Task complexity must factor into pruning budget decisions: retention ratios safe for simple manipulation may fail on compositional tasks.\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_discussion_20260523T012433",
  "tool": "Write",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/discussion.tex",
    "content": "\\section{Discussion}\n\\label{sec:discussion}\n\n\\paragraph{Limitations.}\nAll closed-loop evaluations use the LIBERO simulation benchmark; real-robot validation is absent. The six models differ in backbone capacity, vision encoder, and fusion strategy beyond the connector, so the connector effect cannot be causally isolated. $\\pi_0$ is evaluated through offline metrics only, without closed-loop verification. The observed correlation between CV and pruning tolerance spans only three closed-loop models ($\\pi_0.5$, X-VLA, OpenVLA), too few to establish a general relationship. SmolVLA baselines (59.2\\% official, 44.8\\% LoRA reproduction) are substantially weaker than those of the other models; whether VTR recovery generalizes to stronger baselines is unknown.\n\n\\paragraph{Non-monotonicity as structural property.}\nX-VLA on Goal exhibits non-monotonic degradation: $k{=}0.95$ drops to 53.8\\% (L2) and 54.0\\% (random), while $k{=}0.9$ recovers to 70.2\\% under L2 selection (Table~\\ref{tab:main_results}). The 0.2\\,pp method gap at $k{=}0.95$ confirms that the anomaly is independent of the token scoring criterion. This pattern is consistent with position sensitivity in the 12-layer BART encoder~\\cite{lewis2020bart}, where specific token positions carry disproportionate structural importance regardless of content.\n\n\\paragraph{$\\pi_0.5$ random subsampling anomaly.}\nRandom selection on $\\pi_0.5$ Object collapses from 69.4\\% at $k{=}0.95$ to 12.0\\% at $k{=}0.9$, then recovers to 77.2\\% at $k{=}0.7$ (Table~\\ref{tab:main_results}). The V-shaped recovery at more aggressive pruning remains unexplained.\n\n\\paragraph{Small-$N$ interactions.}\nX-VLA operates with only 50 vision tokens. At $k{=}0.95$, removing 3 tokens produces $-$44.2\\,pp on Goal and $-$47.0\\,pp on Long. Absolute token count interacts with CV: identical retention ratios impose qualitatively different damage when the token budget is small.\n\n\\paragraph{Design implications.}\nPractitioners should compute importance CV before deploying token pruning, as low-CV and entangling-connector models require distinct compression strategies. Pixel-shuffle connectors need learned re-encoding rather than hard deletion. Task complexity must factor into pruning budget decisions: retention ratios safe for simple manipulation may fail on compositional tasks.\n"
  }
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-23T01:27:09.052150+00:00_

The file /home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/discussion.tex has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_discussion_20260523T012433",
  "tool": "Write",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 17 · 2026-05-23T01:27:09.052315+00:00_

Discussion section written to `docs/paper/discussion.tex`. ~290 words across five paragraphs: Limitations (honest, no hedging), Non-monotonicity (X-VLA Goal, BART encoder position sensitivity), $\pi_0.5$ random anomaly (V-shape recovery), Small-$N$ interactions (3-token catastrophe), and Design implications (CV diagnostic, re-encoding, task complexity).

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_paper_writing_discussion_20260523T012433"
}
```

</details>

---
