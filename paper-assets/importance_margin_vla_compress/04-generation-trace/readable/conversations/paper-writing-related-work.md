# paper writing related work

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 19
- **Recorded user turns:** 0
- **Tool calls:** 9
- **Original source:** `logs/chats/worker_paper_writing_related_work_20260523T011325.jsonl`
- **Structured JSON:** [`a7a00dfd08632a077dd3.json`](../../sessions/a7/a7a00dfd08632a077dd3.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

19 recorded events

### Tool call

_source line 1 · 2026-05-23T01:16:34.022294+00:00_

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
  "session": "worker_paper_writing_related_work_20260523T011325",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/agent-ml-research/skills/global/paper-writing-norms.skill.md"
  }
}
```

</details>

---

### Tool result

_source line 2 · 2026-05-23T01:16:34.023162+00:00_

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
  "session": "worker_paper_writing_related_work_20260523T011325",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-23T01:16:34.023474+00:00_

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
  "session": "worker_paper_writing_related_work_20260523T011325",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/agent-ml-research/skills/global/latex-paper.skill.md"
  }
}
```

</details>

---

### Tool result

_source line 4 · 2026-05-23T01:16:34.024027+00:00_

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
  "session": "worker_paper_writing_related_work_20260523T011325",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-23T01:16:34.024317+00:00_

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
  "session": "worker_paper_writing_related_work_20260523T011325",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/references.bib"
  }
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-23T01:16:34.024859+00:00_

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
  "session": "worker_paper_writing_related_work_20260523T011325",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-23T01:16:34.025128+00:00_

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
  "session": "worker_paper_writing_related_work_20260523T011325",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/introduction.tex"
  }
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-23T01:16:34.025405+00:00_

1	\section{Introduction}
2	\label{sec:introduction}
3	
4	Remove 5\% of vision tokens from SmolVLA and its success rate collapses from 59.2\% to 0.0\% across all task suites and pruning methods. Apply the same 5\% reduction to $\pi_0.5$ and it retains 98.2\%. Both are Vision-Language-Action (VLA) models built on a Vision Transformer (ViT) encoder feeding tokens through a connector into a language model backbone; the critical difference is not model scale (450M vs.\ 4B parameters) but the connector architecture. Token pruning is well-established for image classification, where DynamicViT~\cite{rao2021dynamicvit}, Token Merging~\cite{bolya2023tome}, and EViT~\cite{liang2022evit} reduce computation by 50\% or more with minimal accuracy loss. A growing body of work extends these techniques to VLAs: VLA-IAP~\cite{wang2026vlaiap}, VLA-Cache~\cite{hsu2025vlacache}, EfficientVLA~\cite{yang2025efficientvla}, and VLA-Pruner~\cite{liu2025vlapruner} each demonstrate efficiency gains on individual architectures.
5	
6	These methods implicitly assume that token pruning effectiveness transfers across VLA designs. Yet current VLAs employ fundamentally different vision connectors: linear projections~\cite{black2024pi0}, multi-layer MLP projectors~\cite{kim2024openvla}, pixel-shuffle spatial folding~\cite{shukor2025smolvla}, and learned encoders with cross-token self-attention~\cite{zheng2025xvla}. Each connector imposes distinct constraints on how visual information is distributed across tokens. Deploying a pruning method validated on one architecture to a different connector type risks silent degradation or, as the SmolVLA result above illustrates, complete loss of manipulation capability. No prior work systematically evaluates pruning robustness across both connector architectures and task complexity distributions, and the factor that determines whether a given VLA tolerates token removal remains uncharacterized.
7	
8	We propose a two-axis analysis of VLA token compressibility: prun
…[truncated 2818 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_related_work_20260523T011325",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-23T01:16:34.025800+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls -d /home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/ 2>/dev/null && echo \"EXISTS\" || echo \"NO\"",
  "description": "Check paper directory exists"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_related_work_20260523T011325",
  "tool": "Bash",
  "tool_args": {
    "command": "ls -d /home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/ 2>/dev/null && echo \"EXISTS\" || echo \"NO\"",
    "description": "Check paper directory exists"
  }
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-23T01:16:34.026014+00:00_

/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/
EXISTS

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_related_work_20260523T011325",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-23T01:16:34.026257+00:00_

called Write

<details open><summary>🔧 Tool call — Write</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/related_work.tex",
  "content": "\\section{Related Work}\n\\label{sec:related_work}\n\n\\paragraph{Vision Transformer token reduction.}\nToken pruning and merging for ViTs reduce inference cost by removing redundant patches.\nDynamicViT~\\cite{rao2021dynamicvit} learns binary masks to identify uninformative tokens,\nEViT~\\cite{liang2022evit} uses attention scores to fuse or discard low-salience patches,\nand A-ViT~\\cite{yin2022avit} introduces adaptive per-token halting depth.\nToken Merging~\\cite{bolya2023tome} takes a training-free approach, applying bipartite matching to merge similar tokens.\nThese methods remove 50--66\\% of tokens with less than 0.5 percentage points of ImageNet accuracy loss.\nTheir effectiveness rests on a property specific to image classification: spatial layout contributes minimally to category identity, so discarding patches incurs little information loss.\nRobotic manipulation inverts this assumption.\nGrasping and placement tasks depend on the spatial arrangement of objects, and the same token removal rates may destroy task-critical geometric information that classification can safely ignore.\n\n\\paragraph{Token efficiency in VLMs and VLAs.}\nExtending token reduction to vision-language models introduces a new importance signal: the language model's attention over image tokens.\nFastV~\\cite{chen2024fastv} observes that image token attention drops sharply after early layers and prunes accordingly.\nPruMerge~\\cite{shang2024prumerge} clusters and merges spatially adjacent tokens before they enter the language backbone.\nThese VLM-level methods transfer naturally to VLAs that share the same backbone architecture.\nVLA-specific compression methods have emerged in parallel:\nVLA-IAP~\\cite{wang2026vlaiap} aligns pruning with action-prediction importance,\nVLA-Cache~\\cite{hsu2025vlacache} compresses at the KV-cache level,\nEfficientVLA~\\cite{yang2025efficientvla} combines pruning with merging,\nand VLA-Pruner~\\cite{liu2025vlapruner} learns a pruning policy jointly with the action head.\nEach method validates on a single VLA architecture and demonstrates bounded performance loss on that specific model.\nNo study compares pruning robustness across connector designs, so whether a method validated on one connector type transfers to another remains untested.\n\n\\paragraph{Vision connectors and token structure.}\nThe connector between a ViT encoder and a language backbone determines how spatial information is distributed across the tokens that downstream pruning must operate on.\nLLaVA~\\cite{liu2023llava} projects each patch independently through an MLP, preserving per-token locality.\nBLIP-2~\\cite{li2023blip2} uses cross-attention with learned queries to aggregate patch information into a fixed set of output tokens.\nPixel shuffle~\\cite{shi2016subpixel}, originally designed for super-resolution, folds spatial neighborhoods into channel dimensions and has been adopted by VLAs such as SmolVLA~\\cite{shukor2025smolvla} to compress patch groups into single tokens.\nThese designs create qualitatively different token dependencies: independent connectors (MLP, linear projection) leave patch information separable, while entangling connectors (pixel-shuffle, cross-attention encoders) distribute spatial content across multiple token representations.\nThe pruning consequences of this distinction have not been characterized.\n\nOur work provides the first cross-architecture analysis of how connector coupling and task complexity jointly determine VLA token compressibility.\nWhere prior methods optimize pruning for one model, we identify which architectural properties govern pruning tolerance and introduce a single-pass diagnostic (CV of token norms) that correlates with compressibility without requiring closed-loop evaluation.\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_related_work_20260523T011325",
  "tool": "Write",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/related_work.tex",
    "content": "\\section{Related Work}\n\\label{sec:related_work}\n\n\\paragraph{Vision Transformer token reduction.}\nToken pruning and merging for ViTs reduce inference cost by removing redundant patches.\nDynamicViT~\\cite{rao2021dynamicvit} learns binary masks to identify uninformative tokens,\nEViT~\\cite{liang2022evit} uses attention scores to fuse or discard low-salience patches,\nand A-ViT~\\cite{yin2022avit} introduces adaptive per-token halting depth.\nToken Merging~\\cite{bolya2023tome} takes a training-free approach, applying bipartite matching to merge similar tokens.\nThese methods remove 50--66\\% of tokens with less than 0.5 percentage points of ImageNet accuracy loss.\nTheir effectiveness rests on a property specific to image classification: spatial layout contributes minimally to category identity, so discarding patches incurs little information loss.\nRobotic manipulation inverts this assumption.\nGrasping and placement tasks depend on the spatial arrangement of objects, and the same token removal rates may destroy task-critical geometric information that classification can safely ignore.\n\n\\paragraph{Token efficiency in VLMs and VLAs.}\nExtending token reduction to vision-language models introduces a new importance signal: the language model's attention over image tokens.\nFastV~\\cite{chen2024fastv} observes that image token attention drops sharply after early layers and prunes accordingly.\nPruMerge~\\cite{shang2024prumerge} clusters and merges spatially adjacent tokens before they enter the language backbone.\nThese VLM-level methods transfer naturally to VLAs that share the same backbone architecture.\nVLA-specific compression methods have emerged in parallel:\nVLA-IAP~\\cite{wang2026vlaiap} aligns pruning with action-prediction importance,\nVLA-Cache~\\cite{hsu2025vlacache} compresses at the KV-cache level,\nEfficientVLA~\\cite{yang2025efficientvla} combines pruning with merging,\nand VLA-Pruner~\\cite{liu2025vlapruner} learns a pruning policy jointly with the action head.\nEach method validates on a single VLA architecture and demonstrates bounded performance loss on that specific model.\nNo study compares pruning robustness across connector designs, so whether a method validated on one connector type transfers to another remains untested.\n\n\\paragraph{Vision connectors and token structure.}\nThe connector between a ViT encoder and a language backbone determines how spatial information is distributed across the tokens that downstream pruning must operate on.\nLLaVA~\\cite{liu2023llava} projects each patch independently through an MLP, preserving per-token locality.\nBLIP-2~\\cite{li2023blip2} uses cross-attention with learned queries to aggregate patch information into a fixed set of output tokens.\nPixel shuffle~\\cite{shi2016subpixel}, originally designed for super-resolution, folds spatial neighborhoods into channel dimensions and has been adopted by VLAs such as SmolVLA~\\cite{shukor2025smolvla} to compress patch groups into single tokens.\nThese designs create qualitatively different token dependencies: independent connectors (MLP, linear projection) leave patch information separable, while entangling connectors (pixel-shuffle, cross-attention encoders) distribute spatial content across multiple token representations.\nThe pruning consequences of this distinction have not been characterized.\n\nOur work provides the first cross-architecture analysis of how connector coupling and task complexity jointly determine VLA token compressibility.\nWhere prior methods optimize pruning for one model, we identify which architectural properties govern pruning tolerance and introduce a single-pass diagnostic (CV of token norms) that correlates with compressibility without requiring closed-loop evaluation.\n"
  }
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-23T01:16:34.026515+00:00_

&lt;tool_use_error>File has not been read yet. Read it first before writing to it.&lt;/tool_use_error>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_related_work_20260523T011325",
  "tool": "Write",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-23T01:16:34.026715+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls /home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/related_work.tex 2>/dev/null && echo \"EXISTS\" || echo \"NEW_FILE\"",
  "description": "Check if related_work.tex exists"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_related_work_20260523T011325",
  "tool": "Bash",
  "tool_args": {
    "command": "ls /home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/related_work.tex 2>/dev/null && echo \"EXISTS\" || echo \"NEW_FILE\"",
    "description": "Check if related_work.tex exists"
  }
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-23T01:16:34.026908+00:00_

/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/related_work.tex
EXISTS

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_related_work_20260523T011325",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-23T01:16:34.027098+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_related_work_20260523T011325",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/related_work.tex"
  }
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-23T01:16:34.027370+00:00_

1	\section{Related Work}
2	\label{sec:related_work}
3	
4	\paragraph{Vision token efficiency.}
5	Token pruning in ViTs removes 30--60\% of tokens with $<$1\% accuracy loss on classification, via learned masks~\cite{rao2021dynamicvit}, attention-guided reorganization~\cite{liang2022evit}, bipartite matching~\cite{bolya2023tome}, window-level sparsity~\cite{chen2023sparsevit}, adaptive halting~\cite{yin2022avit,meng2022adavit}, or learned spatial selection~\cite{ryoo2021tokenlearner}. For VLMs, pruning extends to the language backbone: FastV~\cite{chen2024fastv} removes tokens after early LLM layers, LLaVA-PruMerge~\cite{shang2024prumerge} and FasterVLM~\cite{zhang2024fastervlm} use CLS-token attention as an importance signal, FitPrune~\cite{ye2025fitprune} minimizes attention-distribution divergence without training, and CrossGET~\cite{shi2024crossget} applies cross-modal token merging; TokenPacker~\cite{li2024tokenpacker} re-encodes compressed representations. All evaluate on classification or VQA benchmarks; we test whether these results transfer to closed-loop VLA control, where action errors compound across timesteps.
6	
7	\paragraph{VLA-specific token reduction.}
8	VLA-Cache~\cite{xu2025vlacache} caches vision KV states across timesteps for 1.7$\times$ speedup without removing tokens. VLA-IAP~\cite{cheng2026vlaiap} uses interaction-aligned pruning on OpenVLA; EfficientVLA~\cite{yang2025efficientvla} combines layer pruning and token selection on CogACT~\cite{li2024cogact}; VLA-Pruner~\cite{liu2025vlapruner} uses dual-level importance criteria for temporal-aware pruning. All evaluate on MLP-projector architectures. None reports the cliff-edge failure we observe on pixel-shuffle VLAs; their positive results may not generalize to spatially entangled connectors.
9	
10	\paragraph{Vision connectors.}
11	Linear projections~\cite{black2024pi0,black2025pi05} apply no cross-token mixing, producing independently addressable tokens; $\pi_{0.5}$~\cite{black2025pi05} adds a lea
…[truncated 2850 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_related_work_20260523T011325",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-23T01:16:34.027743+00:00_

called Write

<details open><summary>🔧 Tool call — Write</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/related_work.tex",
  "content": "\\section{Related Work}\n\\label{sec:related_work}\n\n\\paragraph{ViT token pruning and merging.}\nToken reduction methods for Vision Transformers consistently remove 50--66\\% of tokens with less than 0.5 percentage points of ImageNet accuracy loss.\nDynamicViT~\\cite{rao2021dynamicvit} learns binary masks to identify uninformative tokens,\nEViT~\\cite{liang2022evit} uses attention scores to fuse or discard low-salience patches,\nA-ViT~\\cite{yin2022avit} introduces adaptive per-token halting depth,\nand Token Merging~\\cite{bolya2023tome} applies training-free bipartite matching to merge similar tokens.\nTheir effectiveness rests on a property specific to classification: spatial layout contributes minimally to category identity, so discarding patches incurs little information loss.\nRobotic manipulation inverts this assumption.\nGrasping and placement tasks depend on the spatial arrangement of objects, and the same token removal rates may destroy task-critical geometric information that classification safely ignores.\nNone of these methods has been evaluated in closed-loop VLA control.\n\n\\paragraph{Token efficiency in VLMs and VLAs.}\nExtending token reduction to vision-language models introduces a new importance signal: the language backbone's attention over image tokens.\nFastV~\\cite{chen2024fastv} observes that image token attention drops sharply after early layers and prunes accordingly.\nPruMerge~\\cite{shang2024prumerge} clusters and merges spatially adjacent tokens before they enter the language backbone.\nThese VLM-level methods transfer naturally to VLAs that share the same backbone architecture.\nVLA-specific compression has emerged in parallel:\nVLA-IAP~\\cite{wang2026vlaiap} aligns pruning with action-prediction importance,\nVLA-Cache~\\cite{hsu2025vlacache} compresses at the KV-cache level,\nEfficientVLA~\\cite{yang2025efficientvla} combines pruning with merging,\nand VLA-Pruner~\\cite{liu2025vlapruner} learns a pruning policy jointly with the action head.\nEach method validates on a single VLA architecture and demonstrates bounded performance loss on that model.\nNo study compares pruning robustness across connector designs, so whether a method validated on one connector type transfers to another remains untested.\n\n\\paragraph{Vision connectors and token structure.}\nThe connector between a ViT encoder and a language backbone determines how spatial information is distributed across the tokens that downstream pruning must operate on.\nLLaVA~\\cite{liu2023llava} projects each patch independently through an MLP, preserving per-token locality.\nBLIP-2~\\cite{li2023blip2} uses cross-attention with learned queries to aggregate patch information into a fixed set of output tokens.\nPixel shuffle~\\cite{shi2016subpixel}, originally designed for super-resolution, folds spatial neighborhoods into channel dimensions and has been adopted by VLAs such as SmolVLA~\\cite{shukor2025smolvla} to compress patch groups into single tokens.\nThese designs create qualitatively different token dependencies: independent connectors (MLP, linear projection) leave patch information separable, while entangling connectors (pixel-shuffle, cross-attention encoders) distribute spatial content across multiple token representations.\nThe pruning consequences of this distinction have not been characterized.\n\nOur work provides the first cross-architecture analysis of how connector coupling and task complexity jointly determine VLA token compressibility.\nWhere prior methods optimize pruning for one model, we identify which architectural properties govern pruning tolerance and introduce a single-pass diagnostic (CV of token norms) that correlates with compressibility without requiring closed-loop evaluation.\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_related_work_20260523T011325",
  "tool": "Write",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/related_work.tex",
    "content": "\\section{Related Work}\n\\label{sec:related_work}\n\n\\paragraph{ViT token pruning and merging.}\nToken reduction methods for Vision Transformers consistently remove 50--66\\% of tokens with less than 0.5 percentage points of ImageNet accuracy loss.\nDynamicViT~\\cite{rao2021dynamicvit} learns binary masks to identify uninformative tokens,\nEViT~\\cite{liang2022evit} uses attention scores to fuse or discard low-salience patches,\nA-ViT~\\cite{yin2022avit} introduces adaptive per-token halting depth,\nand Token Merging~\\cite{bolya2023tome} applies training-free bipartite matching to merge similar tokens.\nTheir effectiveness rests on a property specific to classification: spatial layout contributes minimally to category identity, so discarding patches incurs little information loss.\nRobotic manipulation inverts this assumption.\nGrasping and placement tasks depend on the spatial arrangement of objects, and the same token removal rates may destroy task-critical geometric information that classification safely ignores.\nNone of these methods has been evaluated in closed-loop VLA control.\n\n\\paragraph{Token efficiency in VLMs and VLAs.}\nExtending token reduction to vision-language models introduces a new importance signal: the language backbone's attention over image tokens.\nFastV~\\cite{chen2024fastv} observes that image token attention drops sharply after early layers and prunes accordingly.\nPruMerge~\\cite{shang2024prumerge} clusters and merges spatially adjacent tokens before they enter the language backbone.\nThese VLM-level methods transfer naturally to VLAs that share the same backbone architecture.\nVLA-specific compression has emerged in parallel:\nVLA-IAP~\\cite{wang2026vlaiap} aligns pruning with action-prediction importance,\nVLA-Cache~\\cite{hsu2025vlacache} compresses at the KV-cache level,\nEfficientVLA~\\cite{yang2025efficientvla} combines pruning with merging,\nand VLA-Pruner~\\cite{liu2025vlapruner} learns a pruning policy jointly with the action head.\nEach method validates on a single VLA architecture and demonstrates bounded performance loss on that model.\nNo study compares pruning robustness across connector designs, so whether a method validated on one connector type transfers to another remains untested.\n\n\\paragraph{Vision connectors and token structure.}\nThe connector between a ViT encoder and a language backbone determines how spatial information is distributed across the tokens that downstream pruning must operate on.\nLLaVA~\\cite{liu2023llava} projects each patch independently through an MLP, preserving per-token locality.\nBLIP-2~\\cite{li2023blip2} uses cross-attention with learned queries to aggregate patch information into a fixed set of output tokens.\nPixel shuffle~\\cite{shi2016subpixel}, originally designed for super-resolution, folds spatial neighborhoods into channel dimensions and has been adopted by VLAs such as SmolVLA~\\cite{shukor2025smolvla} to compress patch groups into single tokens.\nThese designs create qualitatively different token dependencies: independent connectors (MLP, linear projection) leave patch information separable, while entangling connectors (pixel-shuffle, cross-attention encoders) distribute spatial content across multiple token representations.\nThe pruning consequences of this distinction have not been characterized.\n\nOur work provides the first cross-architecture analysis of how connector coupling and task complexity jointly determine VLA token compressibility.\nWhere prior methods optimize pruning for one model, we identify which architectural properties govern pruning tolerance and introduce a single-pass diagnostic (CV of token norms) that correlates with compressibility without requiring closed-loop evaluation.\n"
  }
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-23T01:16:34.028110+00:00_

The file /home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/related_work.tex has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_related_work_20260523T011325",
  "tool": "Write",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 19 · 2026-05-23T01:16:34.028406+00:00_

Related Work 写完。3 个 cluster + 定位段，约 420 words。所有 `\cite{}` 均对应 `references.bib` 中已有的 key。叙事线：ViT pruning 在分类上有效但未测 VLA → VLM/VLA 方法各验证单一架构无跨 connector 对比 → connector 设计决定 token 依赖结构但 pruning 影响未被研究 → 我们的定位。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_paper_writing_related_work_20260523T011325"
}
```

</details>

---
