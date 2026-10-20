# paper writing

**Instruction Routing in Fine-Tuned Vision-Language-Action Models: A Cross-Architecture Analysis** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 13
- **Recorded user turns:** 0
- **Tool calls:** 6
- **Original source:** `logs/chats/worker_paper_writing_20260522T061909.jsonl`
- **Structured JSON:** [`76a1cd79d93e1acda421.json`](../../sessions/76/76a1cd79d93e1acda421.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

13 recorded events

### Tool call

_source line 1 · 2026-05-22T06:22:12.816993+00:00_

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
  "session": "worker_paper_writing_20260522T061909",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/agent-ml-research/skills/global/paper-writing-norms.skill.md"
  }
}
```

</details>

---

### Tool result

_source line 2 · 2026-05-22T06:22:12.817584+00:00_

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
  "session": "worker_paper_writing_20260522T061909",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-22T06:22:12.817910+00:00_

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
  "session": "worker_paper_writing_20260522T061909",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/agent-ml-research/skills/global/latex-paper.skill.md"
  }
}
```

</details>

---

### Tool result

_source line 4 · 2026-05-22T06:22:12.818430+00:00_

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
  "session": "worker_paper_writing_20260522T061909",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-22T06:22:12.818600+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/method.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_20260522T061909",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/method.tex"
  }
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-22T06:22:12.818784+00:00_

1	\section{Method}
2	\label{sec:method}
3	
4	We investigate how action-relevant representations are organized across three VLA architectures using complementary probing, attention, and perturbation analyses.
5	
6	%------------------------------------------------------------------
7	\subsection{Architectures and Data}
8	\label{sec:arch_data}
9	
10	We study three VLAs that span distinct backbone families (Table~\ref{tab:arch_overview}).
11	\textbf{OpenVLA}~\cite{kim2024_openvla,karamcheti2024} chains a frozen DinoSigLIP vision backbone~\cite{zhai2023_siglip,oquab2024_dinov2} (DINOv2 ViT-L/14 + SigLIP-SO400M), an MLP projector (2{,}176-D $\to$ 4{,}096-D), and Llama-2-7B~\cite{touvron2023_llama2} (6.74B parameters, 32 layers, 32 multi-head attention [MHA] heads) for autoregressive 7-D action decoding.
12	Its base checkpoint is pretrained on Open X-Embodiment~\cite{padalkar2023_oxe} (OXE; 970K episodes across multiple robot platforms).
13	\textbf{TracVLA}~\cite{zheng2024tracevla} uses Phi-3-mini~\cite{abdin2024phi3} (32 layers, 32 MHA heads) with a SigLIP encoder augmented by spatial trace conditioning, trained on an OXE subset.
14	\textbf{NORA}~\cite{TODO_nora} uses Qwen2.5-VL-3B (36 layers, grouped-query attention [GQA] with 16 query heads and 2 KV heads) with its native vision encoder.
15	
16	Each architecture is evaluated in trained and untrained conditions.
17	A critical asymmetry distinguishes the untrained baselines: OpenVLA's untrained checkpoint is the OXE-pretrained VLA, already fine-tuned for action prediction on 970K episodes, while TracVLA and NORA untrained checkpoints are pure vision-language models (Phi-3-Vision and Qwen2.5-VL) with no action training.
18	OpenVLA trained-vs-untrained comparisons therefore measure a VLA-to-VLA transition; TracVLA and NORA comparisons measure VLM-to-VLA transitions.
19	This asymmetry affects the interpretation of all trained/untrained comparisons throughout the paper.
20	For OpenVLA, two additional conditions support deep-d
…[truncated 6869 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_20260522T061909",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-22T06:22:12.819107+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/method.tex",
  "old_string": "\\textbf{OpenVLA}~\\cite{kim2024_openvla,karamcheti2024} chains a frozen DinoSigLIP vision backbone~\\cite{zhai2023_siglip,oquab2024_dinov2} (DINOv2 ViT-L/14 + SigLIP-SO400M), an MLP projector (2{,}176-D $\\to$ 4{,}096-D), and Llama-2-7B~\\cite{touvron2023_llama2} (6.74B parameters, 32 layers, 32 multi-head attention [MHA] heads) for autoregressive 7-D action decoding.\nIts base checkpoint is pretrained on Open X-Embodiment~\\cite{padalkar2023_oxe} (OXE; 970K episodes across multiple robot platforms).\n\\textbf{TracVLA}~\\cite{zheng2024tracevla} uses Phi-3-mini~\\cite{abdin2024phi3} (32 layers, 32 MHA heads) with a SigLIP encoder augmented by spatial trace conditioning, trained on an OXE subset.\n\\textbf{NORA}~\\cite{TODO_nora} uses Qwen2.5-VL-3B (36 layers, grouped-query attention [GQA] with 16 query heads and 2 KV heads) with its native vision encoder.",
  "new_string": "\\textbf{OpenVLA}~\\cite{kim2024_openvla,karamcheti2024} chains a frozen DinoSigLIP vision backbone~\\cite{zhai2023_siglip,oquab2024_dinov2} (DINOv2 ViT-L/14 + SigLIP-SO400M), an MLP projector, and Llama-2-7B~\\cite{touvron2023_llama2} (6.74B parameters, 32 layers, 32 multi-head attention [MHA] heads) for autoregressive 7-D action decoding.\nIt is pretrained on Open X-Embodiment~\\cite{padalkar2023_oxe} (OXE; 970K episodes across multiple robot platforms).\n\\textbf{TracVLA}~\\cite{zheng2024tracevla} pairs a SigLIP encoder with Phi-3-mini~\\cite{abdin2024phi3} (3.8B parameters, 32 layers, 32 MHA heads).\nSpatial trace conditioning renders visual trajectory overlays on input images to provide spatial guidance for action prediction.\nTracVLA is trained on an OXE subset.\n\\textbf{NORA}~\\cite{TODO_nora} uses Qwen2.5-VL-3B ($\\sim$3B parameters, 36 layers, grouped-query attention [GQA] with 16 query heads and 2 KV heads) with the native Qwen2.5-VL vision encoder, which processes images at dynamic resolution without a separate projection stage."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_20260522T061909",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/method.tex",
    "old_string": "\\textbf{OpenVLA}~\\cite{kim2024_openvla,karamcheti2024} chains a frozen DinoSigLIP vision backbone~\\cite{zhai2023_siglip,oquab2024_dinov2} (DINOv2 ViT-L/14 + SigLIP-SO400M), an MLP projector (2{,}176-D $\\to$ 4{,}096-D), and Llama-2-7B~\\cite{touvron2023_llama2} (6.74B parameters, 32 layers, 32 multi-head attention [MHA] heads) for autoregressive 7-D action decoding.\nIts base checkpoint is pretrained on Open X-Embodiment~\\cite{padalkar2023_oxe} (OXE; 970K episodes across multiple robot platforms).\n\\textbf{TracVLA}~\\cite{zheng2024tracevla} uses Phi-3-mini~\\cite{abdin2024phi3} (32 layers, 32 MHA heads) with a SigLIP encoder augmented by spatial trace conditioning, trained on an OXE subset.\n\\textbf{NORA}~\\cite{TODO_nora} uses Qwen2.5-VL-3B (36 layers, grouped-query attention [GQA] with 16 query heads and 2 KV heads) with its native vision encoder.",
    "new_string": "\\textbf{OpenVLA}~\\cite{kim2024_openvla,karamcheti2024} chains a frozen DinoSigLIP vision backbone~\\cite{zhai2023_siglip,oquab2024_dinov2} (DINOv2 ViT-L/14 + SigLIP-SO400M), an MLP projector, and Llama-2-7B~\\cite{touvron2023_llama2} (6.74B parameters, 32 layers, 32 multi-head attention [MHA] heads) for autoregressive 7-D action decoding.\nIt is pretrained on Open X-Embodiment~\\cite{padalkar2023_oxe} (OXE; 970K episodes across multiple robot platforms).\n\\textbf{TracVLA}~\\cite{zheng2024tracevla} pairs a SigLIP encoder with Phi-3-mini~\\cite{abdin2024phi3} (3.8B parameters, 32 layers, 32 MHA heads).\nSpatial trace conditioning renders visual trajectory overlays on input images to provide spatial guidance for action prediction.\nTracVLA is trained on an OXE subset.\n\\textbf{NORA}~\\cite{TODO_nora} uses Qwen2.5-VL-3B ($\\sim$3B parameters, 36 layers, grouped-query attention [GQA] with 16 query heads and 2 KV heads) with the native Qwen2.5-VL vision encoder, which processes images at dynamic resolution without a separate projection stage."
  }
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-22T06:22:12.819338+00:00_

The file /home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/method.tex has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_20260522T061909",
  "tool": "Edit",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-22T06:22:12.819488+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/method.tex",
  "old_string": "applied separately to image\\_mean and readout positions, with",
  "new_string": "applied separately at image\\_mean and readout, with"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_20260522T061909",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/method.tex",
    "old_string": "applied separately to image\\_mean and readout positions, with",
    "new_string": "applied separately at image\\_mean and readout, with"
  }
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-22T06:22:12.819675+00:00_

The file /home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/method.tex has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_20260522T061909",
  "tool": "Edit",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-22T06:22:12.819996+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/method.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_20260522T061909",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/method.tex"
  }
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-22T06:22:12.820185+00:00_

1	\section{Method}
2	\label{sec:method}
3	
4	We investigate how action-relevant representations are organized across three VLA architectures using complementary probing, attention, and perturbation analyses.
5	
6	%------------------------------------------------------------------
7	\subsection{Architectures and Data}
8	\label{sec:arch_data}
9	
10	We study three VLAs that span distinct backbone families (Table~\ref{tab:arch_overview}).
11	\textbf{OpenVLA}~\cite{kim2024_openvla,karamcheti2024} chains a frozen DinoSigLIP vision backbone~\cite{zhai2023_siglip,oquab2024_dinov2} (DINOv2 ViT-L/14 + SigLIP-SO400M), an MLP projector, and Llama-2-7B~\cite{touvron2023_llama2} (6.74B parameters, 32 layers, 32 multi-head attention [MHA] heads) for autoregressive 7-D action decoding.
12	It is pretrained on Open X-Embodiment~\cite{padalkar2023_oxe} (OXE; 970K episodes across multiple robot platforms).
13	\textbf{TracVLA}~\cite{zheng2024tracevla} pairs a SigLIP encoder with Phi-3-mini~\cite{abdin2024phi3} (3.8B parameters, 32 layers, 32 MHA heads).
14	Spatial trace conditioning renders visual trajectory overlays on input images to provide spatial guidance for action prediction.
15	TracVLA is trained on an OXE subset.
16	\textbf{NORA}~\cite{TODO_nora} uses Qwen2.5-VL-3B ($\sim$3B parameters, 36 layers, grouped-query attention [GQA] with 16 query heads and 2 KV heads) with the native Qwen2.5-VL vision encoder, which processes images at dynamic resolution without a separate projection stage.
17	
18	Each architecture is evaluated in trained and untrained conditions.
19	A critical asymmetry distinguishes the untrained baselines: OpenVLA's untrained checkpoint is the OXE-pretrained VLA, already fine-tuned for action prediction on 970K episodes, while TracVLA and NORA untrained checkpoints are pure vision-language models (Phi-3-Vision and Qwen2.5-VL) with no action training.
20	OpenVLA trained-vs-untrained comparisons therefore measure a VLA-to-VLA transition; TracVLA and NORA comparisons
…[truncated 7052 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_20260522T061909",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 13 · 2026-05-22T06:22:12.820391+00:00_

修改完成。两处变更：

1. **§3.1 架构描述平衡**：OpenVLA 删除了 MLP projector 维度细节 `(2,176-D → 4,096-D)`；TracVLA 补充了 3.8B 参数量和 spatial trace conditioning 的作用（视觉轨迹叠加提供空间引导）；NORA 补充了 ~3B 参数量和 native vision encoder 特征（动态分辨率处理、无独立投影层）。三个架构各约 2-2.5 行，密度均衡。

2. **术语一致性**：line 87 `readout positions` → `readout`，与 §3.2 定义的 `\textbf{readout}` 术语一致。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_paper_writing_20260522T061909"
}
```

</details>

---
