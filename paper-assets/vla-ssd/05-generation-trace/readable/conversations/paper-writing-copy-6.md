# paper writing

**Instruction Routing in Fine-Tuned Vision-Language-Action Models: A Cross-Architecture Analysis** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 71
- **Recorded user turns:** 0
- **Tool calls:** 35
- **Original source:** `logs/chats/worker_paper_writing_20260517T045531.jsonl`
- **Structured JSON:** [`82be2678375c4c4b66ca.json`](../../sessions/82/82be2678375c4c4b66ca.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

71 recorded events

### Tool call

_source line 1 · 2026-05-17T05:00:12.073180+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_20260517T045531",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/related_work.tex"
  }
}
```

</details>

---

### Tool result

_source line 2 · 2026-05-17T05:00:12.073568+00:00_

1	\section{Related Work}\label{sec:related_work}
2	
3	\paragraph{Vision-language-action models.}
4	VLAs fine-tune LLMs on robot demonstrations~\cite{brohan2023_rt2,kim2024_openvla,karamcheti2024}, assuming fine-tuning injects action-relevant knowledge.
5	We test this assumption at the representational level.
6	
7	\paragraph{Behavioral and mechanistic analysis.}
8	Behavioral studies show VLAs rely disproportionately on visual input, with language instructions largely ignored~\cite{grant2026,hou2026,fei2025}.
9	Mechanistic work has identified sparse semantic directions linked to action selection~\cite{haon2025}, memorized sequences via sparse autoencoders~\cite{swann2026,buurmeijer2026}, and probed for symbolic states and world models~\cite{lu2025,molinari2025}.
10	\cite{fang2025} showed fine-tuning erodes VLM reasoning.
11	These studies analyze individual components; we provide a systematic per-layer decomposition with trained-vs-untrained controls absent from prior work. This decomposition reveals a non-monotonic transformation profile invisible to whole-model analyses.
12	
13	\paragraph{Representation analysis.}
14	We adopt RSA~\cite{kriegeskorte2008} and MLP probes~\cite{alain2017,belinkov2022} as geometric and functional metrics, with CKA~\cite{kornblith2019} in the appendix.
15	We compare self-supervised (DINOv2~\cite{oquab2024_dinov2}), VL-pretrained (CLIP~\cite{radford2021_clip}), and fused (DinoSigLIP~\cite{zhai2023_siglip}) encoders at matched ViT-L/14 scale to test whether language grounding contributes to action-relevant structure.
16	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_20260517T045531",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-17T05:00:12.073762+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/references.bib"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_20260517T045531",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/references.bib"
  }
}
```

</details>

---

### Tool result

_source line 4 · 2026-05-17T05:00:12.073969+00:00_

1	% === VLA / Architecture ===
2	
3	@article{kim2024_openvla,
4	  title     = {{OpenVLA}: An Open-Source Vision-Language-Action Model},
5	  author    = {Kim, Moo Jin and Pertsch, Karl and Karamcheti, Siddharth and Xiao, Ted and Balakrishna, Ashwin and Nair, Suraj and Rafailov, Rafael and Foster, Ethan and Lam, Grace and Sanketi, Pannag and Lu, Quan and Kollar, Thomas and Burchfiel, Benjamin and Tedrake, Russ and Sadigh, Dorsa and Levine, Sergey and Liang, Percy and Finn, Chelsea},
6	  journal   = {arXiv preprint arXiv:2406.09246},
7	  year      = {2024},
8	}
9	
10	@article{karamcheti2024,
11	  title     = {Prismatic {VLMs}: Investigating the Design Space of Visually-Conditioned Language Models},
12	  author    = {Karamcheti, Siddharth and Nair, Suraj and Balakrishna, Ashwin and Liang, Percy and Kollar, Thomas and Sadigh, Dorsa},
13	  journal   = {arXiv preprint arXiv:2402.07865},
14	  year      = {2024},
15	}
16	
17	@article{brohan2023_rt2,
18	  title     = {{RT-2}: Vision-Language-Action Models Transfer Web Knowledge to Robotic Control},
19	  author    = {Brohan, Anthony and Brown, Noah and Carbajal, Justice and Chebotar, Yevgen and Chen, Xi and Choromanski, Krzysztof and Ding, Tianli and Driess, Danny and Dubey, Avinava and Finn, Chelsea and others},
20	  journal   = {arXiv preprint arXiv:2307.15818},
21	  year      = {2023},
22	}
23	
24	% === Benchmark ===
25	
26	@inproceedings{liu2023_libero,
27	  title     = {{LIBERO}: Benchmarking Knowledge Transfer for Lifelong Robot Learning},
28	  author    = {Liu, Bo and Zhu, Yifeng and Gao, Chongkai and Feng, Yihao and Liu, Qiang and Zhu, Yuke and Stone, Peter},
29	  booktitle = {Advances in Neural Information Processing Systems (NeurIPS)},
30	  year      = {2023},
31	}
32	
33	% === Representation Analysis Methods ===
34	
35	@article{kriegeskorte2008,
36	  title     = {Representational Similarity Analysis -- Connecting the Branches of Systems Neuroscience},
37	  author    = {Kriegeskorte, Nikolaus and Mur, Marieke and Ban
…[truncated 6159 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_20260517T045531",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-17T05:00:12.074142+00:00_

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
  "session": "worker_paper_writing_20260517T045531",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/agent-ml-research/skills/global/paper-writing-norms.skill.md"
  }
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-17T05:00:12.074484+00:00_

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
  "session": "worker_paper_writing_20260517T045531",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-17T05:00:12.074669+00:00_

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
  "session": "worker_paper_writing_20260517T045531",
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

_source line 8 · 2026-05-17T05:00:12.074800+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_20260517T045531",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-17T05:00:12.074963+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Olsson et al 2022 \"In-context learning and induction heads\" arxiv"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_20260517T045531",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Olsson et al 2022 \"In-context learning and induction heads\" arxiv"
  }
}
```

</details>

---

### Tool call

_source line 10 · 2026-05-17T05:00:12.075095+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Clark et al 2019 \"What Does BERT Look At? An Analysis of BERT's Attention\" arxiv"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_20260517T045531",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Clark et al 2019 \"What Does BERT Look At? An Analysis of BERT's Attention\" arxiv"
  }
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-17T05:00:12.075213+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Vig Belinkov 2019 \"Analyzing the Structure of Attention in a Transformer Language Model\" arxiv"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_20260517T045531",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Vig Belinkov 2019 \"Analyzing the Structure of Attention in a Transformer Language Model\" arxiv"
  }
}
```

</details>

---

### Tool call

_source line 12 · 2026-05-17T05:00:12.075328+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Raghu et al 2017 \"SVCCA: Singular Vector Canonical Correlation Analysis\" arxiv NeurIPS"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_20260517T045531",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Raghu et al 2017 \"SVCCA: Singular Vector Canonical Correlation Analysis\" arxiv NeurIPS"
  }
}
```

</details>

---

### Tool result

_source line 13 · 2026-05-17T05:00:12.075472+00:00_

Web search results for query: "Olsson et al 2022 "In-context learning and induction heads" arxiv"

Links: [{"title":"[2209.11895] In-context Learning and Induction Heads","url":"https://arxiv.org/abs/2209.11895"},{"title":"[PDF] In-context Learning and Induction Heads | Semantic Scholar","url":"https://www.semanticscholar.org/paper/In-context-Learning-and-Induction-Heads-Olsson-Elhage/c90a99eeb57019732a6cc996bb9eaf13faedf00f"},{"title":"On the Emergence of Induction Heads for In-Context Learning Tiberiu Musat*","url":"https://arxiv.org/pdf/2511.01033"},{"title":"In-context Learning and Induction Heads","url":"https://transformer-circuits.pub/2022/in-context-learning-and-induction-heads/index.html"},{"title":"(PDF) In-context Learning and Induction Heads","url":"https://www.researchgate.net/publication/363859214_In-context_Learning_and_Induction_Heads"},{"title":"A circuit for predicting hierarchical structure in-context in Large Language Models","url":"https://arxiv.org/html/2509.21534v1"},{"title":"[2209.11895v1] In-context Learning and Induction Heads","url":"https://export.arxiv.org/abs/2209.11895v1"},{"title":"Which Attention Heads Matter for In-Context Learning?","url":"https://arxiv.org/pdf/2502.14010"},{"title":"In-Context Learning Without Copying","url":"https://arxiv.org/html/2511.05743"},{"title":"Beyond Induction Heads: In-Context Meta Learning Induces Multi-Phase Circuit Emergence","url":"https://arxiv.org/html/2505.16694v2"}]

I found the paper you're looking for! Here are the key details:

**Paper:** "Induction heads" are attention heads that implement a simple algorithm to complete token sequences like [A][B] ... [A] -> [B].

**Authors & Publication:** The paper was authored by Catherine Olsson, Nelson Elhage, Neel Nanda, Nicholas Joseph, Nova DasSarma, Tom Henighan, Ben Mann, Amanda Askell, Yuntao Bai, Anna Chen, and others, published in September 2022.

**ArXiv ID:** 2209.11895

**Main Finding:** Induction heads develop at precisely the same point a
…[truncated 678 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_20260517T045531",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-17T05:00:12.075652+00:00_

Web search results for query: "Raghu et al 2017 "SVCCA: Singular Vector Canonical Correlation Analysis" arxiv NeurIPS"

Links: [{"title":"[1706.05806] SVCCA: Singular Vector Canonical Correlation Analysis for Deep Learning Dynamics and Interpretability","url":"https://arxiv.org/abs/1706.05806"},{"title":"SVCCA: Singular Vector Canonical Correlation Analysis for Deep Learning Dynamics and Interpretability","url":"https://proceedings.neurips.cc/paper/2017/hash/dc6a7e655d7e5840e66733e9ee67cc69-Abstract.html"},{"title":"SVCCA: Singular Vector Canonical Correlation Analysis for ...","url":"https://proceedings.neurips.cc/paper_files/paper/2017/file/dc6a7e655d7e5840e66733e9ee67cc69-Paper.pdf"},{"title":"dblp: SVCCA: Singular Vector Canonical Correlation Analysis for Deep Learning Dynamics and Interpretability.","url":"https://dblp.org/rec/conf/nips/RaghuGYS17.html"},{"title":"SVCCA: Singular Vector Canonical Correlation Analysis for Deep Learning Dynamics and Interpretability · Issue #55 · kweonwooj/papers","url":"https://github.com/kweonwooj/papers/issues/55"},{"title":"[PDF] SVCCA: Singular Vector Canonical Correlation Analysis for Deep Understanding and Improvement | Semantic Scholar","url":"https://www.semanticscholar.org/paper/SVCCA:-Singular-Vector-Canonical-Correlation-for-Raghu-Gilmer/4f03aa472ff9a8ff4e1deda52cc4f504b130d115"},{"title":"SVCCA: Singular Vector Canonical Correlation Analysis for Deep Understanding and Improvement","url":"https://www.researchgate.net/publication/317675920_SVCCA_Singular_Vector_Canonical_Correlation_Analysis_for_Deep_Understanding_and_Improvement"},{"title":"[1706.05806v2] SVCCA: Singular Vector Canonical Correlation Analysis for Deep Learning Dynamics and Interpretability","url":"https://arxiv.org/abs/1706.05806v2"},{"title":"[1706.05806] SVCCA: Singular Vector Canonical Correlation Analysis for Deep Learning Dynamics and Interpretability","url":"https://arxiv-export1.library.cornell.edu/abs/1706.05806"},{"title":"[1706.05806v1] SVCCA
…[truncated 1309 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_20260517T045531",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 15 · 2026-05-17T05:00:12.075829+00:00_

Web search results for query: "Clark et al 2019 "What Does BERT Look At? An Analysis of BERT's Attention" arxiv"

Links: [{"title":"[1906.04341] What Does BERT Look At? An Analysis of BERT's Attention","url":"https://arxiv.org/abs/1906.04341"},{"title":"What Does BERT Look At? An Analysis of BERT’s Attention Kevin Clark†","url":"https://www-nlp.stanford.edu/pubs/clark2019what.pdf"},{"title":"Paper page - What Does BERT Look At? An Analysis of BERT's Attention","url":"https://huggingface.co/papers/1906.04341"},{"title":"A paper a day#2: What Does BERT Look At? An Analysis of BERT’s Attention | by Peratham Wiriyathammabhum | Medium","url":"https://peratham.medium.com/a-paper-a-day-2-what-does-bert-look-at-an-analysis-of-berts-attention-2f24d855302"},{"title":"[1906.04341v1] What Does BERT Look At? An Analysis of BERT's Attention","url":"https://arxiv.org/abs/1906.04341v1"},{"title":"What Does BERT Look at? An Analysis of BERT’s Attention - ACL Anthology","url":"https://aclanthology.org/W19-4828/"},{"title":"What Does BERT Look At? An Analysis of BERT's Attention","url":"https://www.summarizepaper.com/en/arxiv-id/1906.04341v1/"},{"title":"Behold: Papers are Neat: What Does BERT Look At?","url":"https://samuelstevens.me/writing/what-does-bert-look-at"},{"title":"What Does BERT Look At? An Analysis of BERT's Attention - ADS","url":"https://ui.adsabs.harvard.edu/abs/2019arXiv190604341C/abstract"},{"title":"Paper Review - What Does BERT Look At? An Analysis of BERT’s Attention | Liyan Tang","url":"https://www.tangliyan.com/blog/posts/bert_attn/"}]

I found the paper you were looking for! Here's the information about it:

**Title:** "What Does BERT Look At? An Analysis of BERT's Attention"

**Authors:** Kevin Clark, Urvashi Khandelwal, Omer Levy, Christopher D. Manning

**Publication:** Published in BlackBoxNLP 2019 (ACL-W)

**ArXiv:** arXiv:1906.04341 (submitted June 11, 2019)

**Main Contributions:**

The paper proposes methods for analyzing the attention mechanisms of pr
…[truncated 812 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_20260517T045531",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-17T05:00:12.076043+00:00_

Web search results for query: "Vig Belinkov 2019 "Analyzing the Structure of Attention in a Transformer Language Model" arxiv"

Links: [{"title":"[1906.04284] Analyzing the Structure of Attention in a Transformer Language Model","url":"https://arxiv.org/abs/1906.04284"},{"title":"Analyzing the Structure of Attention in a Transformer Language Model - ADS","url":"https://ui.adsabs.harvard.edu/abs/2019arXiv190604284V/abstract"},{"title":"Analyzing the Structure of Attention in a Transformer Language Model - ACL Anthology","url":"https://aclanthology.org/W19-4808/"},{"title":"🚧 2019: Analyzing the Structure of Attention in a Transformer Language Model · Issue #255 · jojonki/arXivNotes","url":"https://github.com/jojonki/arXivNotes/issues/255"},{"title":"LINEAR LOG-NORMAL ATTENTION WITH UNBIASED CONCENTRATION A PREPRINT","url":"https://arxiv.org/pdf/2311.13541"},{"title":"[PDF] Analyzing the Structure of Attention in a Transformer Language Model | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Analyzing-the-Structure-of-Attention-in-a-Language-Vig-Belinkov/a039ea239e37f53a2cb60c68e0a1967994353166"},{"title":"[1906.05714] A Multiscale Visualization of Attention in the Transformer Model","url":"https://ar5iv.labs.arxiv.org/html/1906.05714"},{"title":"A Multiscale Visualization of Attention in the Transformer Model Jesse Vig","url":"https://arxiv.org/pdf/1906.05714"},{"title":"Published as a conference paper at ICLR 2020 ARE TRANSFORMERS UNIVERSAL","url":"https://arxiv.org/pdf/1912.10077"},{"title":"Analyzing the Structure of Attention in a Transformer ...","url":"https://belinkov.com/assets/pdf/blackboxnlp2019.pdf"}]

I've found the paper you're looking for. Here are the key details:

**Paper Title:** Analyzing the Structure of Attention in a Transformer Language Model

**Authors:** Jesse Vig and Yonatan Belinkov

**Publication:** Proceedings of the 2019 ACL Workshop BlackboxNLP: Analyzing and Interpreting Neural Networks for NLP, pages 63–76, Florence, Ital
…[truncated 764 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_20260517T045531",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-17T05:00:12.076222+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Morcos et al 2018 \"Insights on representational similarity in neural networks with canonical correlation\" NeurIPS arxiv"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_20260517T045531",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Morcos et al 2018 \"Insights on representational similarity in neural networks with canonical correlation\" NeurIPS arxiv"
  }
}
```

</details>

---

### Tool call

_source line 18 · 2026-05-17T05:00:12.076389+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Darcet et al 2024 \"Vision Transformers Need Registers\" ICLR arxiv register tokens"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_20260517T045531",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Darcet et al 2024 \"Vision Transformers Need Registers\" ICLR arxiv register tokens"
  }
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-17T05:00:12.076550+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Voita et al 2019 \"Analyzing Multi-Head Self-Attention\" ACL arxiv specialized heads"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_20260517T045531",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Voita et al 2019 \"Analyzing Multi-Head Self-Attention\" ACL arxiv specialized heads"
  }
}
```

</details>

---

### Tool call

_source line 20 · 2026-05-17T05:00:12.076673+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Conmy et al 2023 \"Towards Automated Circuit Discovery for Mechanistic Interpretability\" arxiv"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_20260517T045531",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Conmy et al 2023 \"Towards Automated Circuit Discovery for Mechanistic Interpretability\" arxiv"
  }
}
```

</details>

---

### Tool result

_source line 21 · 2026-05-17T05:00:12.076821+00:00_

Web search results for query: "Morcos et al 2018 "Insights on representational similarity in neural networks with canonical correlation" NeurIPS arxiv"

Links: [{"title":"Insights on representational similarity in neural networks with canonical correlation","url":"https://proceedings.neurips.cc/paper/2018/hash/a7a3d70c6d17a73140918996d03c014f-Abstract.html"},{"title":"[1806.05759] Insights on representational similarity in neural networks with canonical correlation","url":"https://arxiv.org/abs/1806.05759"},{"title":"Reviews: Insights on representational similarity in neural networks with canonical correlation","url":"https://proceedings.neurips.cc/paper/2018/file/a7a3d70c6d17a73140918996d03c014f-Reviews.html"},{"title":"dblp: Insights on representational similarity in neural networks with canonical correlation.","url":"https://dblp.org/rec/conf/nips/MorcosRB18.html"},{"title":"Insights on representational similarity in neural networks with canonical correlation | Pillow Lab Blog","url":"https://pillowlab.wordpress.com/2019/01/21/insights-on-representational-similarity-in-neural-networks-with-canonical-correlation/"},{"title":"Insights on representational similarity in neural networks ...","url":"https://dl.acm.org/doi/pdf/10.5555/3327345.3327475"},{"title":"Reviews: Insights on representational similarity in neural networks with canonical correlation","url":"https://media.nips.cc/nipsbooks/nipspapers/paper_files/nips31/reviews/2770.html"},{"title":"Similarity of Neural Network Representations Revisited","url":"http://proceedings.mlr.press/v97/kornblith19a/kornblith19a.pdf"},{"title":"Insights on representational similarity in neural networks with canonical correlation","url":"https://research.google/pubs/pub47052/"},{"title":"Insights on representational similarity in neural networks with canonical correlation | Proceedings of the 32nd International Conference on Neural Information Processing Systems","url":"https://dl.acm.org/doi/10.5555/3327345.3327475"}]

I foun
…[truncated 1484 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_20260517T045531",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 22 · 2026-05-17T05:00:12.077058+00:00_

Web search results for query: "Voita et al 2019 "Analyzing Multi-Head Self-Attention" ACL arxiv specialized heads"

Links: [{"title":"[1905.09418] Analyzing Multi-Head Self-Attention: Specialized Heads Do the Heavy Lifting, the Rest Can Be Pruned","url":"https://arxiv.org/abs/1905.09418"},{"title":"Analyzing Multi-Head Self-Attention: Specialized Heads Do the Heavy Lifting, the Rest Can Be Pruned - ACL Anthology","url":"https://aclanthology.org/P19-1580/"},{"title":"Analyzing Multi-Head Self-Attention: Specialized Heads Do the Heavy Lifting, the Rest Can Be Pruned","url":"https://bibbase.org/network/publication/voita-talbot-moiseev-sennrich-titov-analyzingmultiheadselfattentionspecializedheadsdotheheavyliftingtherestcanbepruned-2019"},{"title":"GitHub - lena-voita/the-story-of-heads: This is a repository with the code for the ACL 2019 paper \"Analyzing Multi-Head Self-Attention: Specialized Heads Do the Heavy Lifting, the Rest Can Be Pruned\" and the ACL 2021 paper \"Analyzing Source and Target Contributions to NMT Predictions\". · GitHub","url":"https://github.com/lena-voita/the-story-of-heads"},{"title":"Analyzing Multi-Head Self-Attention","url":"https://aclanthology.org/P19-1580.pdf"},{"title":"MoH: Multi-Head Attention as Mixture-of-Head Attention","url":"https://arxiv.org/html/2410.11842v1"},{"title":"Analyzing Multi-Head Self-Attention","url":"https://www.research.ed.ac.uk/files/106651234/Analyzing_Multi_Head_VOITA_DoA020819_VoR_CC_BY.pdf"},{"title":"Machine Translation Weekly 4: Analyzing Multi-Head Self-Attention | Jindřich’s blog","url":"https://jlibovicky.github.io/2019/05/27/MT-Weekly-Analyzing-Self-Attention.html"},{"title":"[PDF] Analyzing Multi-Head Self-Attention: Specialized Heads Do the Heavy Lifting, the Rest Can Be Pruned | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Analyzing-Multi-Head-Self-Attention:-Specialized-Do-Voita-Talbot/07a64686ce8e43ac475a8d820a8a9f1d87989583"},{"title":"[1905.09418v2] Analyzing Multi-Head Self-Atte
…[truncated 1337 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_20260517T045531",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 23 · 2026-05-17T05:00:12.077271+00:00_

Web search results for query: "Darcet et al 2024 "Vision Transformers Need Registers" ICLR arxiv register tokens"

Links: [{"title":"Published as a conference paper at ICLR 2024 VISION TRANSFORMERS NEED REGISTERS","url":"https://arxiv.org/pdf/2309.16588"},{"title":"[2309.16588] Vision Transformers Need Registers","url":"https://arxiv.org/abs/2309.16588"},{"title":"Vision Transformers Don’t Need Trained Registers","url":"https://arxiv.org/html/2506.08010v1"},{"title":"[2603.25803] Do All Vision Transformers Need Registers? A Cross-Architectural Reassessment","url":"https://arxiv.org/abs/2603.25803"},{"title":"[2506.08010] Vision Transformers Don't Need Trained Registers","url":"https://arxiv.org/abs/2506.08010"},{"title":"Do All Vision Transformers Need Registers? A Cross-Architectural Reassessment","url":"https://arxiv.org/html/2603.25803"},{"title":"Vision Transformers Need Registers","url":"https://proceedings.iclr.cc/paper_files/paper/2024/hash/0b408293619f725fd30162af057e531a-Abstract-Conference.html"},{"title":"ICLR 2024 — Best Papers & Talks (ImageGen, Vision, Transformers, State Space Models) ft. Durk Kingma, Christian Szegedy, Ilya Sutskever","url":"https://www.latent.space/p/iclr-2024-recap"},{"title":"Leveraging Registers in Vision Transformers for Robust Adaptation","url":"https://arxiv.org/html/2501.04784v1"},{"title":"Vision Transformers Need Registers","url":"https://arxiv.org/html/2309.16588v2"}]

I've found comprehensive information about the Darcet et al. 2024 paper "Vision Transformers Need Registers" from ICLR. Here's a summary of the key findings:

## Paper Overview

The paper "Vision Transformers Need Registers" was authored by Timothée Darcet, Maxime Oquab, Julien Mairal, and Piotr Bojanowski from FAIR at Meta and University of Grenoble Alpes, and received the ICLR Outstanding Paper Award.

## Main Problem Identified

The paper identifies and characterizes artifacts in feature maps of both supervised and self-supervised ViT networks. The artifa
…[truncated 1162 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_20260517T045531",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 24 · 2026-05-17T05:00:12.077487+00:00_

Web search results for query: "Conmy et al 2023 "Towards Automated Circuit Discovery for Mechanistic Interpretability" arxiv"

Links: [{"title":"[2304.14997] Towards Automated Circuit Discovery for Mechanistic Interpretability","url":"https://arxiv.org/abs/2304.14997"},{"title":"(PDF) Towards Automated Circuit Discovery for Mechanistic Interpretability","url":"https://www.researchgate.net/publication/370417693_Towards_Automated_Circuit_Discovery_for_Mechanistic_Interpretability"},{"title":"Towards Automated Circuit Discovery for Mechanistic Interpretability - ADS","url":"https://ui.adsabs.harvard.edu/abs/2023arXiv230414997C/abstract"},{"title":"[PDF] Towards Automated Circuit Discovery for Mechanistic Interpretability | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Towards-Automated-Circuit-Discovery-for-Mechanistic-Conmy-Mavor-Parker/eefbd8b384a58f464827b19e30a6920ba976def9"},{"title":"Towards Automated Circuit Discovery for Mechanistic Interpretability","url":"https://www.catalyzex.com/paper/arxiv:2304.14997"},{"title":"Circuit Insights: Towards Interpretability Beyond Activations","url":"https://arxiv.org/html/2510.14936"},{"title":"GitHub - ArthurConmy/Automatic-Circuit-Discovery · GitHub","url":"https://github.com/ArthurConmy/Automatic-Circuit-Discovery"},{"title":"Towards Automated Circuit Discovery for Mechanistic Interpretability","url":"https://papers.nips.cc/paper_files/paper/2023/hash/34e1dbe95d34d7ebaf99b9bcaeb5b2be-Abstract-Conference.html"},{"title":"🤘ACDC (not that one) - by Grigory Sapunov - Gonzo ML","url":"https://gonzoml.substack.com/p/acdc-towards-automated-circuit-discovery"},{"title":"Towards Automated Circuit Discovery for Mechanistic Interpretability","url":"https://proceedings.neurips.cc/paper_files/paper/2023/file/34e1dbe95d34d7ebaf99b9bcaeb5b2be-Paper-Conference.pdf"}]

I found the paper successfully. Here are the key results:

The paper is authored by Arthur Conmy, Augustine N. Mavor-Parker, Aengus Lynch, Stefan Heimershe
…[truncated 1295 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_20260517T045531",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 25 · 2026-05-17T05:00:12.077672+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Dosovitskiy et al 2021 \"An Image is Worth 16x16 Words\" ViT CLS token ICLR"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_20260517T045531",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Dosovitskiy et al 2021 \"An Image is Worth 16x16 Words\" ViT CLS token ICLR"
  }
}
```

</details>

---

### Tool call

_source line 26 · 2026-05-17T05:00:12.077804+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Elhage et al 2021 \"A Mathematical Framework for Transformer Circuits\" Anthropic residual stream"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_20260517T045531",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Elhage et al 2021 \"A Mathematical Framework for Transformer Circuits\" Anthropic residual stream"
  }
}
```

</details>

---

### Tool call

_source line 27 · 2026-05-17T05:00:12.077943+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Wang et al 2023 \"Interpretability in the Wild\" indirect object identification circuit NeurIPS arxiv"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_20260517T045531",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Wang et al 2023 \"Interpretability in the Wild\" indirect object identification circuit NeurIPS arxiv"
  }
}
```

</details>

---

### Tool call

_source line 28 · 2026-05-17T05:00:12.078072+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Hewitt Manning 2019 \"A Structural Probe for Finding Syntax in Word Representations\" NAACL arxiv"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_20260517T045531",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Hewitt Manning 2019 \"A Structural Probe for Finding Syntax in Word Representations\" NAACL arxiv"
  }
}
```

</details>

---

### Tool result

_source line 29 · 2026-05-17T05:00:12.078226+00:00_

Web search results for query: "Dosovitskiy et al 2021 "An Image is Worth 16x16 Words" ViT CLS token ICLR"

Links: [{"title":"[2010.11929] An Image is Worth 16x16 Words: Transformers for Image Recognition at Scale","url":"https://arxiv.org/abs/2010.11929"},{"title":"ViT: AN IMAGE IS WORTH 16X16 WORDS - Roger’s Blog","url":"https://kmsrogerkim.github.io/ai/vit/"},{"title":"An Image is Worth 16x16 Words: Transformers for Image Recognition at Scale","url":"https://research.google/pubs/an-image-is-worth-16x16-words-transformers-for-image-recognition-at-scale/"},{"title":"An Image is Worth 16x16 Words: Transformers for Image Recognition at Scale | OpenReview","url":"https://openreview.net/forum?id=YicbFdNTTy"},{"title":"[PDF] An Image is Worth 16x16 Words: Transformers for Image Recognition at Scale | Semantic Scholar","url":"https://www.semanticscholar.org/paper/An-Image-is-Worth-16x16-Words:-Transformers-for-at-Dosovitskiy-Beyer/268d347e8a55b5eb82fb5e7d2f800e33c75ab18a"},{"title":"Dosovitskiy et al (2021) An Image is Worth 16x16 Words","url":"https://www.adrian.idv.hk/2025-03-26-dbkwzudmhguh21-vit/"},{"title":"Published as a conference paper at ICLR 2021 AN IMAGE IS WORTH 16X16 WORDS:","url":"https://openreview.net/pdf?id=YicbFdNTTy"},{"title":"dblp: An Image is Worth 16x16 Words: Transformers for Image Recognition at Scale.","url":"https://dblp.org/rec/conf/iclr/DosovitskiyB0WZ21.html"},{"title":"An Image is Worth 16x16 Words: Transformers for Image Recognition at Scale | BibSonomy","url":"https://www.bibsonomy.org/bibtex/325eaaeb3466512b4b887cc143bde420"},{"title":"ViT: An Image is Worth 16x16 Words - ICLR 2021 Conference Paper - Studocu","url":"https://www.studocu.com/row/document/national-university-of-computer-and-emerging-sciences/computer-vision/vit-an-image-is-worth-16x16-words-iclr-2021-conference-paper/153395250"}]

The search has found relevant information about the paper. Here's a summary of the results:

## Paper Information

"An Image is Worth 16x16 Words:
…[truncated 1325 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_20260517T045531",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 30 · 2026-05-17T05:00:12.078402+00:00_

Web search results for query: "Elhage et al 2021 "A Mathematical Framework for Transformer Circuits" Anthropic residual stream"

Links: [{"title":"A Mathematical Framework for Transformer Circuits","url":"https://transformer-circuits.pub/2021/framework/index.html"},{"title":"A Mathematical Framework for Transformer Circuits","url":"https://www.anthropic.com/research/a-mathematical-framework-for-transformer-circuits"},{"title":"Arxiv Dives - A Mathematical Framework for Transformer Circuits - Part 1","url":"https://ghost.oxen.ai/arxiv-dives-a-mathematical-framework-for-transformer-circuits/"},{"title":"A Mathematical Framework for Transformer Circuits","url":"https://www.scribd.com/document/866284321/A-Mathematical-Framework-for-Transformer-Circuits"},{"title":"Transformer Circuits: A Mathematical Framework","url":"https://studylib.net/doc/27496897/transformer-circui...--1-"},{"title":"Structure and Interpretation of Deep Networks","url":"https://sidn.baulab.info/formulation/"},{"title":"Mechanistic Interpretability On the Internals of LLMs","url":"https://krmopuri.github.io/xml/static_files/presentations/MI-Pranav.pdf"},{"title":"1 Introduction","url":"https://arxiv.org/html/2402.02619v3"},{"title":"A Mathematical Framework for Transformer Circuits by Anthropic","url":"https://www.youtube.com/watch?v=wiu-a170qYU"},{"title":"Arxiv Dives - A Mathematical Framework for Transformer Circuits - Part 1 | Oxen.ai","url":"https://www.oxen.ai/blog/arxiv-dives-a-mathematical-framework-for-transformer-circuits"}]

I found the research you're looking for! Here's information about the Elhage et al. 2021 paper on "A Mathematical Framework for Transformer Circuits":

## Overview
The paper was published December 22, 2021, by Nelson Elhage, Neel Nanda, Catherine Olsson, Tom Henighan, and other researchers from Anthropic, with correspondence to Chris Olah.

## Key Concepts About the Residual Stream

The residual stream is the sum of the output of all previous layers and the original e
…[truncated 1057 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_20260517T045531",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 31 · 2026-05-17T05:00:12.078581+00:00_

Web search results for query: "Hewitt Manning 2019 "A Structural Probe for Finding Syntax in Word Representations" NAACL arxiv"

Links: [{"title":"A Structural Probe for Finding Syntax in Word Representations - ACL Anthology","url":"https://aclanthology.org/N19-1419/"},{"title":"A Structural Probe for Finding Syntax in Word Representations","url":"https://nlp.stanford.edu/pubs/hewitt2019structural.pdf"},{"title":"GitHub - john-hewitt/structural-probes: Codebase for testing whether hidden states of neural networks encode discrete structures. · GitHub","url":"https://github.com/john-hewitt/structural-probes"},{"title":"Finding Syntax with Structural Probes · John Hewitt","url":"https://www.cs.columbia.edu/~johnhew//structural-probe.html"},{"title":"A Structural Probe for Finding Syntax in Word ...","url":"https://www.cs.columbia.edu/~johnhew/public/hewitt2019structural_slides.pdf"},{"title":"[Quick Review] A Structural Probe for Finding Syntax in Word Representations","url":"https://liner.com/review/structural-probe-for-finding-syntax-in-word-representations"},{"title":"Papers with Code - A Structural Probe for Finding Syntax in Word Representations","url":"https://paperswithcode.com/paper/a-structural-probe-for-finding-syntax-in-word"},{"title":"Structural Probe for Syntax in Word Representations | PDF | Parsing | Norm (Mathematics)","url":"https://www.scribd.com/document/543349454/N19-1419-1"},{"title":"[PDF] A Structural Probe for Finding Syntax in Word Representations | Semantic Scholar","url":"https://www.semanticscholar.org/paper/A-Structural-Probe-for-Finding-Syntax-in-Word-Hewitt-Manning/455a8838cde44f288d456d01c76ede95b56dc675"},{"title":"A Structural Probe for Finding Syntax in Word Representations - Ethan Kim","url":"https://ethankim00.github.io/paper_review/AStructuralProbeforFindingSyntaxinWordRepresentations/"}]

I found the paper you're looking for! Here are the key details:

**"A Structural Probe for Finding Syntax in Word Representations"** by John He
…[truncated 1155 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_20260517T045531",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 32 · 2026-05-17T05:00:12.078763+00:00_

Web search results for query: "Wang et al 2023 "Interpretability in the Wild" indirect object identification circuit NeurIPS arxiv"

Links: [{"title":"[2211.00593] Interpretability in the Wild: a Circuit for Indirect Object Identification in GPT-2 small","url":"https://arxiv.org/abs/2211.00593"},{"title":"[PDF] Interpretability in the Wild: a Circuit for Indirect Object Identification in GPT-2 small | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Interpretability-in-the-Wild:-a-Circuit-for-Object-Wang-Variengien/6edd112383ad494f5f2eba72b6f4ffae122ce61f"},{"title":"A Walkthrough of Interpretability in the Wild (w/ authors Kevin Wang, Arthur Conmy & Alexandre Variengien) — Neel Nanda","url":"https://www.neelnanda.io/mechanistic-interpretability/walkthrough-ioi"},{"title":"INTERPRETABILITY IN THE WILD: A CIRCUIT FOR ...","url":"https://openreview.net/pdf?id=NpsVSN6o4ul"},{"title":"Interpretability in the Wild: a Circuit for Indirect Object Identification in GPT-2 Small | OpenReview","url":"https://openreview.net/forum?id=NpsVSN6o4ul"},{"title":"Investigating the Indirect Object Identification circuit in Mamba","url":"https://arxiv.org/html/2407.14008v1"},{"title":"[2211.00593] Interpretability in the Wild: a Circuit for Indirect Object Identification in GPT-2 small","url":"https://ar5iv.labs.arxiv.org/html/2211.00593"},{"title":"Tutorials","url":"https://projects.illc.uva.nl/indeep/tutorial/"},{"title":"GitHub - cx0/mech-interpretability: Exploring length generalization in the context of indirect object identification (IOI) task for mechanistic interpretability.","url":"https://github.com/cx0/mech-interpretability"},{"title":"(PDF) Interpretability in the Wild: a Circuit for Indirect Object Identification in GPT-2 small","url":"https://www.researchgate.net/publication/364987811_Interpretability_in_the_Wild_a_Circuit_for_Indirect_Object_Identification_in_GPT-2_small"}]

I've successfully found the paper you're looking for. Here are the key details:

**P
…[truncated 1074 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_20260517T045531",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 33 · 2026-05-17T05:00:12.078915+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Mu Jesse Andreas 2020 \"Compositional Explanations of Neurons\" NeurIPS arxiv functional specialization"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_20260517T045531",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Mu Jesse Andreas 2020 \"Compositional Explanations of Neurons\" NeurIPS arxiv functional specialization"
  }
}
```

</details>

---

### Tool call

_source line 34 · 2026-05-17T05:00:12.079068+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Geva et al 2021 \"Transformer Feed-Forward Layers Are Key-Value Memories\" EMNLP arxiv"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_20260517T045531",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Geva et al 2021 \"Transformer Feed-Forward Layers Are Key-Value Memories\" EMNLP arxiv"
  }
}
```

</details>

---

### Tool result

_source line 35 · 2026-05-17T05:00:12.079225+00:00_

Web search results for query: "Geva et al 2021 "Transformer Feed-Forward Layers Are Key-Value Memories" EMNLP arxiv"

Links: [{"title":"Transformer Feed-Forward Layers Are Key-Value Memories - ACL Anthology","url":"https://aclanthology.org/2021.emnlp-main.446/"},{"title":"Transformer Feed-Forward Layers Are Key-Value Memories","url":"https://aclanthology.org/2021.emnlp-main.446.pdf"},{"title":"GitHub - mega002/ff-layers: The accompanying code for \"Transformer Feed-Forward Layers Are Key-Value Memories\". Mor Geva, Roei Schuster, Jonathan Berant, and Omer Levy. EMNLP, 2021. · GitHub","url":"https://github.com/mega002/ff-layers"},{"title":"Transformer Feed-Forward Layers Are Key-Value Memories | Request PDF","url":"https://www.researchgate.net/publication/357126029_Transformer_Feed-Forward_Layers_Are_Key-Value_Memories"},{"title":"Transformer Feed-Forward Layers Are Key-Value Memories - Tel Aviv University","url":"https://cris.tau.ac.il/en/publications/transformer-feed-forward-layers-are-key-value-memories-2/"},{"title":"Transformer Feed-Forward Layers Are Key-Value Memories - Israeli Research Community Portal","url":"https://cris.iucc.ac.il/en/publications/transformer-feed-forward-layers-are-key-value-memories-2/"},{"title":"(PDF) Transformer Feed-Forward Layers Are Key-Value Memories","url":"https://www.researchgate.net/publication/348079179_Transformer_Feed-Forward_Layers_Are_Key-Value_Memories"},{"title":"[PDF] Transformer Feed-Forward Layers Are Key-Value Memories | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Transformer-Feed-Forward-Layers-Are-Key-Value-Geva-Schuster/4a54d58a4b20e4f3af25cea3c188a12082a95e02"},{"title":"Transformer Feed-Forward Layers Build Predictions by ...","url":"https://aclanthology.org/2022.emnlp-main.3.pdf"},{"title":"Transformer Feed-Forward Layers Are Key-Value Memories","url":"https://bibbase.org/network/publication/geva-schuster-berant-levy-transformerfeedforwardlayersarekeyvaluememories-2021"}]

I found the paper y
…[truncated 1087 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_20260517T045531",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 36 · 2026-05-17T05:00:12.079406+00:00_

Web search results for query: "Mu Jesse Andreas 2020 "Compositional Explanations of Neurons" NeurIPS arxiv functional specialization"

Links: [{"title":"Compositional Explanations of Neurons Jesse Mu Stanford University","url":"https://proceedings.neurips.cc/paper/2020/file/c74956ffb38ba48ed6ce977af6727275-Paper.pdf"},{"title":"[PDF] Compositional Explanations of Neurons | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Compositional-Explanations-of-Neurons-Mu-Andreas/56d1003fd02346e93354ab55cd204485c268512a"},{"title":"Compositional Explanations of Neurons","url":"https://proceedings.neurips.cc/paper/2020/hash/c74956ffb38ba48ed6ce977af6727275-Abstract.html"},{"title":"[2006.14032] Compositional Explanations of Neurons","url":"https://arxiv.org/abs/2006.14032"},{"title":"Compositional Explanations of Neurons - ADS","url":"https://ui.adsabs.harvard.edu/abs/2020arXiv200614032M/abstract"},{"title":"Jacob Andreas @ MIT > Papers","url":"https://www.mit.edu/~jda/pubs.html"},{"title":"Jesse Mu, Jacob Andreas · Compositional Explanations of Neurons","url":"https://slideslive.com/38938570/compositional-explanations-of-neurons"},{"title":"Google Scholar","url":"https://scholar.google.com/scholar?q=Jesse+Mu+and+Jacob+Andreas.+2020.+Compositional+explanations+of+neurons.+Advances+in+Neural+Information+Processing+Systems+33+(2020),+17153%E2%80%9317163."},{"title":"Review for NeurIPS paper: Compositional Explanations of Neurons","url":"https://proceedings.neurips.cc/paper/2020/file/c74956ffb38ba48ed6ce977af6727275-Review.html"},{"title":"Neuron Explanations | AIEA Lab","url":"https://aiea-lab.github.io/project/neuron_expl/"}]

I found the paper you're looking for! Here's what the search results show:

"Compositional Explanations of Neurons" is a paper by Jesse Mu and Jacob Andreas presented at NeurIPS 2020. The paper is available on arXiv with the ID 2006.14032.

**Paper Overview:**

The paper describes a procedure for explaining neurons in deep representations by 
…[truncated 1115 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_20260517T045531",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 37 · 2026-05-17T05:00:12.079567+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Tenney et al 2019 \"BERT Rediscovers the Classical NLP Pipeline\" ACL arxiv probing layers"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_20260517T045531",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Tenney et al 2019 \"BERT Rediscovers the Classical NLP Pipeline\" ACL arxiv probing layers"
  }
}
```

</details>

---

### Tool result

_source line 38 · 2026-05-17T05:00:12.079733+00:00_

Web search results for query: "Tenney et al 2019 "BERT Rediscovers the Classical NLP Pipeline" ACL arxiv probing layers"

Links: [{"title":"BERT Rediscovers the Classical NLP Pipeline - ACL Anthology","url":"https://aclanthology.org/P19-1452/"},{"title":"[1905.05950] BERT Rediscovers the Classical NLP Pipeline","url":"https://arxiv.org/abs/1905.05950"},{"title":"BERT Rediscovers the Classical NLP Pipeline","url":"https://aclanthology.org/P19-1452.pdf"},{"title":"BERT Rediscovers the Classical NLP Pipeline","url":"https://research.google/pubs/bert-rediscovers-the-classical-nlp-pipeline/"},{"title":"[PDF] BERT Rediscovers the Classical NLP Pipeline | Semantic Scholar","url":"https://www.semanticscholar.org/paper/BERT-Rediscovers-the-Classical-NLP-Pipeline-Tenney-Das/97906df07855b029b7aae7c2a1c6c5e8df1d531c"},{"title":"Tenney et al 2019 - BERT Rediscovers the Classical NLP Pipeline","url":"https://czlwang.com/zettel/20201031020627-tenney_et_al_2019_bert_rediscovers_the_classical_nlp_pipeline.html"},{"title":"BERT Rediscovers the Classical NLP Pipeline | Request PDF","url":"https://www.researchgate.net/publication/335778883_BERT_Rediscovers_the_Classical_NLP_Pipeline"},{"title":"BERT Rediscovers the Classical NLP Pipeline. | BibSonomy","url":"https://www.bibsonomy.org/bibtex/5e2beac70ab8fac60ac65bbc9c8d8c7c"},{"title":"BERT Rediscovers the Classical NLP Pipeline","url":"https://bibbase.org/network/publication/tenney-das-pavlick-bertrediscoverstheclassicalnlppipeline-2019"},{"title":"BERT Rediscovers the Classical NLP Pipeline Ian Tenney1 Dipanjan Das1","url":"https://arxiv.org/pdf/1905.05950"}]

I've successfully found the paper you're looking for. Here are the key details:

## Paper Information

**BERT Rediscovers the Classical NLP Pipeline** by Ian Tenney, Dipanjan Das, and Ellie Pavlick, published at ACL 2019 (Proceedings of the 57th Annual Meeting of the Association for Computational Linguistics, pages 4593–4601, Florence, Italy).

The arxiv version is available as 
…[truncated 1229 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_20260517T045531",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 39 · 2026-05-17T05:00:12.079993+00:00_

called Write

<details open><summary>🔧 Tool call — Write</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/related_work.tex",
  "content": "\\section{Related Work}\\label{sec:related_work}\n\n\\paragraph{Vision-language-action models.}\nVLAs fine-tune large language models on robot demonstrations to produce action tokens conditioned on visual observations and language instructions~\\cite{brohan2023_rt2,kim2024_openvla,karamcheti2024,black2024_pi0}.\nThis architecture family inherits the transformer backbone and its multi-modal fusion mechanisms from vision-language models, but repurposes them for continuous control.\nA central assumption is that fine-tuning injects action-relevant knowledge into pretrained representations.\nWe test this assumption at the representational level through per-layer, per-token-type decomposition.\n\n\\paragraph{Mechanistic interpretability in transformers.}\nA growing body of work analyzes transformer internals at the level of individual attention heads and circuits.\nElhage et al.~\\cite{elhage2021} introduced the residual stream framework, treating each layer as reading from and writing to a shared communication channel.\nBuilding on this, Olsson et al.~\\cite{olsson2022} identified induction heads as a mechanistic basis for in-context learning, with specific attention heads implementing token-copying algorithms.\nCircuit-level analyses have since traced complete computational subgraphs for tasks such as indirect object identification~\\cite{wang2023_ioi} and greater-than comparison~\\cite{conmy2023}.\nIn parallel, attention probing studies have shown that individual heads encode syntactic relations~\\cite{clark2019}, capture positional and structural patterns at different depths~\\cite{vig2019}, and that a small subset of specialized heads accounts for most model performance~\\cite{voita2019}.\nOur Layer-1 attention head analysis extends this tradition to the VLA domain, where we find that 25 of 32 heads become instruction-dominant after fine-tuning.\n\n\\paragraph{Behavioral and mechanistic analysis of VLAs.}\nBehavioral evaluations reveal that current VLAs rely disproportionately on visual input, with language instructions largely ignored during action generation~\\cite{grant2026,hou2026,fei2025}.\nAt the mechanistic level, H\\\"aon et al.~\\cite{haon2025} identified sparse semantic directions in VLA residual streams linked to action selection.\nSparse autoencoder studies have uncovered interpretable features and memorized action sequences~\\cite{swann2026,buurmeijer2026}, while probing work has tested for symbolic state representations and emergent world models~\\cite{lu2025,molinari2025}.\nFang et al.~\\cite{fang2025} showed that fine-tuning erodes general VLM reasoning capabilities.\nThese studies analyze individual components or aggregate statistics; we provide a systematic per-layer decomposition with trained-vs-untrained controls absent from prior work.\nThe closest work to ours is Grant et al.~\\cite{grant2026}, who performed a feature-level mechanistic study of VLAs and found visual dominance in internal representations.\nOur work differs in three respects: (1) we decompose at the token level rather than the feature level, identifying the readout token as the sole multimodal integration site; (2) we track representations across all 32 layers, revealing a non-monotonic transformation profile invisible to whole-model analyses; and (3) we include trained-vs-untrained factorial controls that isolate the effect of fine-tuning on attention routing mechanisms.\n\n\\paragraph{Token-level functional specialization in transformers.}\nEvidence for functional specialization among token positions has emerged across multiple architectures.\nIn Vision Transformers, the prepended CLS token aggregates global information for classification~\\cite{dosovitskiy2021}, and Darcet et al.~\\cite{darcet2024} showed that certain image patch positions are repurposed as implicit registers for internal computation.\nIn language models, feed-forward layers store factual associations in position-specific key-value memory patterns that differ by depth~\\cite{geva2021}, and probing studies have demonstrated that different layers encode a pipeline of increasingly abstract linguistic features~\\cite{tenney2019}.\nThese findings suggest that transformers allocate distinct computational roles to specific token positions and layers.\nOur results provide the first such evidence in VLAs: image tokens remain instruction-blind across all layers while the readout token serves as the exclusive multimodal hub from Layer~1 onward.\n\n\\paragraph{Representation similarity and probing methodology.}\nRepresentational Similarity Analysis (RSA)~\\cite{kriegeskorte2008}, originally developed in computational neuroscience, compares geometric structure between representation spaces via second-order isomorphism.\nSingular Vector Canonical Correlation Analysis (SVCCA)~\\cite{raghu2017} and projection-weighted CCA~\\cite{morcos2018} extended this approach to deep networks, enabling layer-wise comparison of learned representations across architectures and training stages.\nCentered Kernel Alignment (CKA)~\\cite{kornblith2019} provides a related but more robust similarity index.\nOn the functional side, linear probes~\\cite{alain2017,hewitt2019} and the broader probing methodology literature~\\cite{belinkov2022} test whether specific information is linearly decodable from intermediate representations, complementing geometric measures with task-oriented evaluation.\nWe adopt RSA as our primary geometric metric and MLP classification probes as our functional metric, with CKA reported in the appendix.\nThis combination allows us to distinguish between representational structure (what geometry is preserved) and information accessibility (what can be decoded for downstream use).\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_20260517T045531",
  "tool": "Write",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/related_work.tex",
    "content": "\\section{Related Work}\\label{sec:related_work}\n\n\\paragraph{Vision-language-action models.}\nVLAs fine-tune large language models on robot demonstrations to produce action tokens conditioned on visual observations and language instructions~\\cite{brohan2023_rt2,kim2024_openvla,karamcheti2024,black2024_pi0}.\nThis architecture family inherits the transformer backbone and its multi-modal fusion mechanisms from vision-language models, but repurposes them for continuous control.\nA central assumption is that fine-tuning injects action-relevant knowledge into pretrained representations.\nWe test this assumption at the representational level through per-layer, per-token-type decomposition.\n\n\\paragraph{Mechanistic interpretability in transformers.}\nA growing body of work analyzes transformer internals at the level of individual attention heads and circuits.\nElhage et al.~\\cite{elhage2021} introduced the residual stream framework, treating each layer as reading from and writing to a shared communication channel.\nBuilding on this, Olsson et al.~\\cite{olsson2022} identified induction heads as a mechanistic basis for in-context learning, with specific attention heads implementing token-copying algorithms.\nCircuit-level analyses have since traced complete computational subgraphs for tasks such as indirect object identification~\\cite{wang2023_ioi} and greater-than comparison~\\cite{conmy2023}.\nIn parallel, attention probing studies have shown that individual heads encode syntactic relations~\\cite{clark2019}, capture positional and structural patterns at different depths~\\cite{vig2019}, and that a small subset of specialized heads accounts for most model performance~\\cite{voita2019}.\nOur Layer-1 attention head analysis extends this tradition to the VLA domain, where we find that 25 of 32 heads become instruction-dominant after fine-tuning.\n\n\\paragraph{Behavioral and mechanistic analysis of VLAs.}\nBehavioral evaluations reveal that current VLAs rely disproportionately on visual input, with language instructions largely ignored during action generation~\\cite{grant2026,hou2026,fei2025}.\nAt the mechanistic level, H\\\"aon et al.~\\cite{haon2025} identified sparse semantic directions in VLA residual streams linked to action selection.\nSparse autoencoder studies have uncovered interpretable features and memorized action sequences~\\cite{swann2026,buurmeijer2026}, while probing work has tested for symbolic state representations and emergent world models~\\cite{lu2025,molinari2025}.\nFang et al.~\\cite{fang2025} showed that fine-tuning erodes general VLM reasoning capabilities.\nThese studies analyze individual components or aggregate statistics; we provide a systematic per-layer decomposition with trained-vs-untrained controls absent from prior work.\nThe closest work to ours is Grant et al.~\\cite{grant2026}, who performed a feature-level mechanistic study of VLAs and found visual dominance in internal representations.\nOur work differs in three respects: (1) we decompose at the token level rather than the feature level, identifying the readout token as the sole multimodal integration site; (2) we track representations across all 32 layers, revealing a non-monotonic transformation profile invisible to whole-model analyses; and (3) we include trained-vs-untrained factorial controls that isolate the effect of fine-tuning on attention routing mechanisms.\n\n\\paragraph{Token-level functional specialization in transformers.}\nEvidence for functional specialization among token positions has emerged across multiple architectures.\nIn Vision Transformers, the prepended CLS token aggregates global information for classification~\\cite{dosovitskiy2021}, and Darcet et al.~\\cite{darcet2024} showed that certain image patch positions are repurposed as implicit registers for internal computation.\nIn language models, feed-forward layers store factual associations in position-specific key-value memory patterns that differ by depth~\\cite{geva2021}, and probing studies have demonstrated that different layers encode a pipeline of increasingly abstract linguistic features~\\cite{tenney2019}.\nThese findings suggest that transformers allocate distinct computational roles to specific token positions and layers.\nOur results provide the first such evidence in VLAs: image tokens remain instruction-blind across all layers while the readout token serves as the exclusive multimodal hub from Layer~1 onward.\n\n\\paragraph{Representation similarity and probing methodology.}\nRepresentational Similarity Analysis (RSA)~\\cite{kriegeskorte2008}, originally developed in computational neuroscience, compares geometric structure between representation spaces via second-order isomorphism.\nSingular Vector Canonical Correlation Analysis (SVCCA)~\\cite{raghu2017} and projection-weighted CCA~\\cite{morcos2018} extended this approach to deep networks, enabling layer-wise comparison of learned representations across architectures and training stages.\nCentered Kernel Alignment (CKA)~\\cite{kornblith2019} provides a related but more robust similarity index.\nOn the functional side, linear probes~\\cite{alain2017,hewitt2019} and the broader probing methodology literature~\\cite{belinkov2022} test whether specific information is linearly decodable from intermediate representations, complementing geometric measures with task-oriented evaluation.\nWe adopt RSA as our primary geometric metric and MLP classification probes as our functional metric, with CKA reported in the appendix.\nThis combination allows us to distinguish between representational structure (what geometry is preserved) and information accessibility (what can be decoded for downstream use).\n"
  }
}
```

</details>

---

### Tool result

_source line 40 · 2026-05-17T05:00:12.080233+00:00_

The file /home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/related_work.tex has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_20260517T045531",
  "tool": "Write",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 41 · 2026-05-17T05:00:12.080396+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/references.bib",
  "old_string": "% === VLA Fine-tuning and Reasoning ===",
  "new_string": "% === Mechanistic Interpretability in Transformers ===\n\n@article{elhage2021,\n  title     = {A Mathematical Framework for Transformer Circuits},\n  author    = {Elhage, Nelson and Nanda, Neel and Olsson, Catherine and Henighan, Tom and Joseph, Nicholas and Mann, Ben and Askell, Amanda and Bai, Yuntao and Chen, Anna and Conerly, Tom and DasSarma, Nova and Drain, Dawn and Ganguli, Deep and Hatfield-Dodds, Zac and Hernandez, Danny and Jones, Andy and Kernion, Jackson and Lovitt, Liane and Ndousse, Kamal and Amodei, Dario and Brown, Tom and Clark, Jack and Kaplan, Jared and McCandlish, Sam and Olah, Chris},\n  journal   = {Transformer Circuits Thread},\n  year      = {2021},\n  url       = {https://transformer-circuits.pub/2021/framework/index.html},\n}\n\n@article{olsson2022,\n  title     = {In-context Learning and Induction Heads},\n  author    = {Olsson, Catherine and Elhage, Nelson and Nanda, Neel and Joseph, Nicholas and DasSarma, Nova and Henighan, Tom and Mann, Ben and Askell, Amanda and Bai, Yuntao and Chen, Anna and Conerly, Tom and Drain, Dawn and Ganguli, Deep and Hatfield-Dodds, Zac and Hernandez, Danny and Johnston, Scott and Jones, Andy and Kernion, Jackson and Lovitt, Liane and Ndousse, Kamal and Amodei, Dario and Brown, Tom and Clark, Jack and Kaplan, Jared and McCandlish, Sam and Olah, Chris},\n  journal   = {arXiv preprint arXiv:2209.11895},\n  year      = {2022},\n}\n\n@inproceedings{wang2023_ioi,\n  title     = {Interpretability in the Wild: a Circuit for Indirect Object Identification in {GPT-2} Small},\n  author    = {Wang, Kevin and Variengien, Alexandre and Conmy, Arthur and Shlegeris, Buck and Steinhardt, Jacob},\n  booktitle = {International Conference on Learning Representations (ICLR)},\n  year      = {2023},\n}\n\n@inproceedings{conmy2023,\n  title     = {Towards Automated Circuit Discovery for Mechanistic Interpretability},\n  author    = {Conmy, Arthur and Mavor-Parker, Augustine N. and Lynch, Aengus and Heimersheim, Stefan and Garriga-Alonso, Adri{\\`a}},\n  booktitle = {Advances in Neural Information Processing Systems (NeurIPS)},\n  year      = {2023},\n}\n\n% === Attention Analysis ===\n\n@inproceedings{clark2019,\n  title     = {What Does {BERT} Look At? {An} Analysis of {BERT}'s Attention},\n  author    = {Clark, Kevin and Khandelwal, Urvashi and Levy, Omer and Manning, Christopher D.},\n  booktitle = {Proceedings of the 2019 ACL Workshop BlackboxNLP},\n  year      = {2019},\n}\n\n@inproceedings{vig2019,\n  title     = {Analyzing the Structure of Attention in a Transformer Language Model},\n  author    = {Vig, Jesse and Belinkov, Yonatan},\n  booktitle = {Proceedings of the 2019 ACL Workshop BlackboxNLP},\n  year      = {2019},\n}\n\n@inproceedings{voita2019,\n  title     = {Analyzing Multi-Head Self-Attention: Specialized Heads Do the Heavy Lifting, the Rest Can Be Pruned},\n  author    = {Voita, Elena and Talbot, David and Moiseev, Fedor and Sennrich, Rico and Titov, Ivan},\n  booktitle = {Proceedings of the 57th Annual Meeting of the Association for Computational Linguistics (ACL)},\n  year      = {2019},\n}\n\n% === Token-Level Functional Specialization ===\n\n@inproceedings{dosovitskiy2021,\n  title     = {An Image is Worth 16x16 Words: Transformers for Image Recognition at Scale},\n  author    = {Dosovitskiy, Alexey and Beyer, Lucas and Kolesnikov, Alexander and Weissenborn, Dirk and Zhai, Xiaohua and Unterthiner, Thomas and Dehghani, Mostafa and Minderer, Matthias and Heigold, Georg and Gelly, Sylvain and Uszkoreit, Jakob and Houlsby, Neil},\n  booktitle = {International Conference on Learning Representations (ICLR)},\n  year      = {2021},\n}\n\n@inproceedings{darcet2024,\n  title     = {Vision Transformers Need Registers},\n  author    = {Darcet, Timoth{\\'e}e and Oquab, Maxime and Mairal, Julien and Bojanowski, Piotr},\n  booktitle = {International Conference on Learning Representations (ICLR)},\n  year      = {2024},\n}\n\n@inproceedings{geva2021,\n  title     = {Transformer Feed-Forward Layers Are Key-Value Memories},\n  author    = {Geva, Mor and Schuster, Roei and Berant, Jonathan and Levy, Omer},\n  booktitle = {Proceedings of the 2021 Conference on Empirical Methods in Natural Language Processing (EMNLP)},\n  year      = {2021},\n}\n\n@inproceedings{tenney2019,\n  title     = {{BERT} Rediscovers the Classical {NLP} Pipeline},\n  author    = {Tenney, Ian and Das, Dipanjan and Pavlick, Ellie},\n  booktitle = {Proceedings of the 57th Annual Meeting of the Association for Computational Linguistics (ACL)},\n  year      = {2019},\n}\n\n% === Representation Similarity Methods ===\n\n@inproceedings{raghu2017,\n  title     = {{SVCCA}: Singular Vector Canonical Correlation Analysis for Deep Learning Dynamics and Interpretability},\n  author    = {Raghu, Maithra and Gilmer, Justin and Yosinski, Jason and Sohl-Dickstein, Jascha},\n  booktitle = {Advances in Neural Information Processing Systems (NeurIPS)},\n  year      = {2017},\n}\n\n@inproceedings{morcos2018,\n  title     = {Insights on Representational Similarity in Neural Networks with Canonical Correlation},\n  author    = {Morcos, Ari S. and Raghu, Maithra and Bengio, Samy},\n  booktitle = {Advances in Neural Information Processing Systems (NeurIPS)},\n  year      = {2018},\n}\n\n@inproceedings{hewitt2019,\n  title     = {A Structural Probe for Finding Syntax in Word Representations},\n  author    = {Hewitt, John and Manning, Christopher D.},\n  booktitle = {Proceedings of the 2019 Conference of the North {A}merican Chapter of the Association for Computational Linguistics (NAACL)},\n  year      = {2019},\n}\n\n% === VLA Fine-tuning and Reasoning ==="
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_20260517T045531",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/references.bib",
    "old_string": "% === VLA Fine-tuning and Reasoning ===",
    "new_string": "% === Mechanistic Interpretability in Transformers ===\n\n@article{elhage2021,\n  title     = {A Mathematical Framework for Transformer Circuits},\n  author    = {Elhage, Nelson and Nanda, Neel and Olsson, Catherine and Henighan, Tom and Joseph, Nicholas and Mann, Ben and Askell, Amanda and Bai, Yuntao and Chen, Anna and Conerly, Tom and DasSarma, Nova and Drain, Dawn and Ganguli, Deep and Hatfield-Dodds, Zac and Hernandez, Danny and Jones, Andy and Kernion, Jackson and Lovitt, Liane and Ndousse, Kamal and Amodei, Dario and Brown, Tom and Clark, Jack and Kaplan, Jared and McCandlish, Sam and Olah, Chris},\n  journal   = {Transformer Circuits Thread},\n  year      = {2021},\n  url       = {https://transformer-circuits.pub/2021/framework/index.html},\n}\n\n@article{olsson2022,\n  title     = {In-context Learning and Induction Heads},\n  author    = {Olsson, Catherine and Elhage, Nelson and Nanda, Neel and Joseph, Nicholas and DasSarma, Nova and Henighan, Tom and Mann, Ben and Askell, Amanda and Bai, Yuntao and Chen, Anna and Conerly, Tom and Drain, Dawn and Ganguli, Deep and Hatfield-Dodds, Zac and Hernandez, Danny and Johnston, Scott and Jones, Andy and Kernion, Jackson and Lovitt, Liane and Ndousse, Kamal and Amodei, Dario and Brown, Tom and Clark, Jack and Kaplan, Jared and McCandlish, Sam and Olah, Chris},\n  journal   = {arXiv preprint arXiv:2209.11895},\n  year      = {2022},\n}\n\n@inproceedings{wang2023_ioi,\n  title     = {Interpretability in the Wild: a Circuit for Indirect Object Identification in {GPT-2} Small},\n  author    = {Wang, Kevin and Variengien, Alexandre and Conmy, Arthur and Shlegeris, Buck and Steinhardt, Jacob},\n  booktitle = {International Conference on Learning Representations (ICLR)},\n  year      = {2023},\n}\n\n@inproceedings{conmy2023,\n  title     = {Towards Automated Circuit Discovery for Mechanistic Interpretability},\n  author    = {Conmy, Arthur and Mavor-Parker, Augustine N. and Lynch, Aengus and Heimersheim, Stefan and Garriga-Alonso, Adri{\\`a}},\n  booktitle = {Advances in Neural Information Processing Systems (NeurIPS)},\n  year      = {2023},\n}\n\n% === Attention Analysis ===\n\n@inproceedings{clark2019,\n  title     = {What Does {BERT} Look At? {An} Analysis of {BERT}'s Attention},\n  author    = {Clark, Kevin and Khandelwal, Urvashi and Levy, Omer and Manning, Christopher D.},\n  booktitle = {Proceedings of the 2019 ACL Workshop BlackboxNLP},\n  year      = {2019},\n}\n\n@inproceedings{vig2019,\n  title     = {Analyzing the Structure of Attention in a Transformer Language Model},\n  author    = {Vig, Jesse and Belinkov, Yonatan},\n  booktitle = {Proceedings of the 2019 ACL Workshop BlackboxNLP},\n  year      = {2019},\n}\n\n@inproceedings{voita2019,\n  title     = {Analyzing Multi-Head Self-Attention: Specialized Heads Do the Heavy Lifting, the Rest Can Be Pruned},\n  author    = {Voita, Elena and Talbot, David and Moiseev, Fedor and Sennrich, Rico and Titov, Ivan},\n  booktitle = {Proceedings of the 57th Annual Meeting of the Association for Computational Linguistics (ACL)},\n  year      = {2019},\n}\n\n% === Token-Level Functional Specialization ===\n\n@inproceedings{dosovitskiy2021,\n  title     = {An Image is Worth 16x16 Words: Transformers for Image Recognition at Scale},\n  author    = {Dosovitskiy, Alexey and Beyer, Lucas and Kolesnikov, Alexander and Weissenborn, Dirk and Zhai, Xiaohua and Unterthiner, Thomas and Dehghani, Mostafa and Minderer, Matthias and Heigold, Georg and Gelly, Sylvain and Uszkoreit, Jakob and Houlsby, Neil},\n  booktitle = {International Conference on Learning Representations (ICLR)},\n  year      = {2021},\n}\n\n@inproceedings{darcet2024,\n  title     = {Vision Transformers Need Registers},\n  author    = {Darcet, Timoth{\\'e}e and Oquab, Maxime and Mairal, Julien and Bojanowski, Piotr},\n  booktitle = {International Conference on Learning Representations (ICLR)},\n  year      = {2024},\n}\n\n@inproceedings{geva2021,\n  title     = {Transformer Feed-Forward Layers Are Key-Value Memories},\n  author    = {Geva, Mor and Schuster, Roei and Berant, Jonathan and Levy, Omer},\n  booktitle = {Proceedings of the 2021 Conference on Empirical Methods in Natural Language Processing (EMNLP)},\n  year      = {2021},\n}\n\n@inproceedings{tenney2019,\n  title     = {{BERT} Rediscovers the Classical {NLP} Pipeline},\n  author    = {Tenney, Ian and Das, Dipanjan and Pavlick, Ellie},\n  booktitle = {Proceedings of the 57th Annual Meeting of the Association for Computational Linguistics (ACL)},\n  year      = {2019},\n}\n\n% === Representation Similarity Methods ===\n\n@inproceedings{raghu2017,\n  title     = {{SVCCA}: Singular Vector Canonical Correlation Analysis for Deep Learning Dynamics and Interpretability},\n  author    = {Raghu, Maithra and Gilmer, Justin and Yosinski, Jason and Sohl-Dickstein, Jascha},\n  booktitle = {Advances in Neural Information Processing Systems (NeurIPS)},\n  year      = {2017},\n}\n\n@inproceedings{morcos2018,\n  title     = {Insights on Representational Similarity in Neural Networks with Canonical Correlation},\n  author    = {Morcos, Ari S. and Raghu, Maithra and Bengio, Samy},\n  booktitle = {Advances in Neural Information Processing Systems (NeurIPS)},\n  year      = {2018},\n}\n\n@inproceedings{hewitt2019,\n  title     = {A Structural Probe for Finding Syntax in Word Representations},\n  author    = {Hewitt, John and Manning, Christopher D.},\n  booktitle = {Proceedings of the 2019 Conference of the North {A}merican Chapter of the Association for Computational Linguistics (NAACL)},\n  year      = {2019},\n}\n\n% === VLA Fine-tuning and Reasoning ==="
  }
}
```

</details>

---

### Tool result

_source line 42 · 2026-05-17T05:00:12.080626+00:00_

The file /home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/references.bib has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_20260517T045531",
  "tool": "Edit",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 43 · 2026-05-17T05:00:12.080774+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "grep -oP '\\\\\\\\cite\\{[^}]+\\}' related_work.tex | sed 's/\\\\\\\\cite{//;s/}//' | tr ',' '\\n' | sort -u",
  "description": "Extract all cite keys from related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_20260517T045531",
  "tool": "Bash",
  "tool_args": {
    "command": "grep -oP '\\\\\\\\cite\\{[^}]+\\}' related_work.tex | sed 's/\\\\\\\\cite{//;s/}//' | tr ',' '\\n' | sort -u",
    "description": "Extract all cite keys from related_work.tex"
  }
}
```

</details>

---

### Tool result

_source line 44 · 2026-05-17T05:00:12.080902+00:00_

(Bash completed with no output)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_20260517T045531",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 45 · 2026-05-17T05:00:12.081047+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "grep -oP '@\\w+\\{([^,]+),' references.bib | sed 's/@[^{]*{//;s/,//' | sort -u",
  "description": "Extract all bib keys from references.bib"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_20260517T045531",
  "tool": "Bash",
  "tool_args": {
    "command": "grep -oP '@\\w+\\{([^,]+),' references.bib | sed 's/@[^{]*{//;s/,//' | sort -u",
    "description": "Extract all bib keys from references.bib"
  }
}
```

</details>

---

### Tool result

_source line 46 · 2026-05-17T05:00:12.081175+00:00_

alain2017
belinkov2022
black2024_pi0
brohan2023_rt2
buurmeijer2026
clark2019
conmy2023
darcet2024
dosovitskiy2021
elhage2021
fang2025
fei2025
geva2021
grant2026
haon2025
hewitt2019
hou2026
karamcheti2024
kim2024_openvla
kornblith2019
kriegeskorte2008
liu2023_libero
lu2025
molinari2025
morcos2018
olsson2022
oquab2024_dinov2
radford2021_clip
raghu2017
swann2026
tenney2019
vig2019
voita2019
wang2023_ioi
zhai2023_siglip

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_20260517T045531",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 47 · 2026-05-17T05:00:12.081306+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "grep -oP '\\\\cite\\{[^}]+\\}' related_work.tex | sed 's/\\\\cite{//;s/}//' | tr ',' '\\n' | sort -u",
  "description": "Extract cite keys from related_work.tex with correct working directory"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_20260517T045531",
  "tool": "Bash",
  "tool_args": {
    "command": "grep -oP '\\\\cite\\{[^}]+\\}' related_work.tex | sed 's/\\\\cite{//;s/}//' | tr ',' '\\n' | sort -u",
    "description": "Extract cite keys from related_work.tex with correct working directory"
  }
}
```

</details>

---

### Tool result

_source line 48 · 2026-05-17T05:00:12.081447+00:00_

alain2017
belinkov2022
black2024_pi0
brohan2023_rt2
buurmeijer2026
clark2019
conmy2023
darcet2024
dosovitskiy2021
elhage2021
fang2025
fei2025
geva2021
grant2026
haon2025
hewitt2019
hou2026
karamcheti2024
kim2024_openvla
kornblith2019
kriegeskorte2008
lu2025
molinari2025
morcos2018
olsson2022
raghu2017
swann2026
tenney2019
vig2019
voita2019
wang2023_ioi

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_20260517T045531",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 49 · 2026-05-17T05:00:12.081619+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "grep -n \"—\\|–\" /home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/related_work.tex; grep -n \"ing,\" /home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/related_work.tex; grep -in \"Furthermore\\|Moreover\\|Additionally\\|delve\\|leverage\\|utilize\\|a myriad\" /home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/related_work.tex",
  "description": "Check for banned writing patterns in related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_20260517T045531",
  "tool": "Bash",
  "tool_args": {
    "command": "grep -n \"—\\|–\" /home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/related_work.tex; grep -n \"ing,\" /home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/related_work.tex; grep -in \"Furthermore\\|Moreover\\|Additionally\\|delve\\|leverage\\|utilize\\|a myriad\" /home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/related_work.tex",
    "description": "Check for banned writing patterns in related_work.tex"
  }
}
```

</details>

---

### Tool result

_source line 50 · 2026-05-17T05:00:12.081752+00:00_

12:Building on this, Olsson et al.~\cite{olsson2022} identified induction heads as a mechanistic basis for in-context learning, with specific attention heads implementing token-copying algorithms.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_20260517T045531",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 51 · 2026-05-17T05:00:12.081914+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/related_work.tex",
  "limit": "5",
  "offset": "10"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_20260517T045531",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/related_work.tex",
    "limit": "5",
    "offset": "10"
  }
}
```

</details>

---

### Tool result

_source line 52 · 2026-05-17T05:00:12.082073+00:00_

10	A growing body of work analyzes transformer internals at the level of individual attention heads and circuits.
11	Elhage et al.~\cite{elhage2021} introduced the residual stream framework, treating each layer as reading from and writing to a shared communication channel.
12	Building on this, Olsson et al.~\cite{olsson2022} identified induction heads as a mechanistic basis for in-context learning, with specific attention heads implementing token-copying algorithms.
13	Circuit-level analyses have since traced complete computational subgraphs for tasks such as indirect object identification~\cite{wang2023_ioi} and greater-than comparison~\cite{conmy2023}.
14	In parallel, attention probing studies have shown that individual heads encode syntactic relations~\cite{clark2019}, capture positional and structural patterns at different depths~\cite{vig2019}, and that a small subset of specialized heads accounts for most model performance~\cite{voita2019}.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_20260517T045531",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 53 · 2026-05-17T05:00:12.082220+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/related_work.tex",
  "old_string": "Elhage et al.~\\cite{elhage2021} introduced the residual stream framework, treating each layer as reading from and writing to a shared communication channel.\nBuilding on this, Olsson et al.~\\cite{olsson2022} identified induction heads as a mechanistic basis for in-context learning, with specific attention heads implementing token-copying algorithms.",
  "new_string": "Elhage et al.~\\cite{elhage2021} introduced the residual stream framework, in which each layer reads from and writes to a shared communication channel.\nBuilding on this, Olsson et al.~\\cite{olsson2022} identified induction heads as a mechanistic basis for in-context learning; these specialized attention heads implement token-copying algorithms."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_20260517T045531",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/related_work.tex",
    "old_string": "Elhage et al.~\\cite{elhage2021} introduced the residual stream framework, treating each layer as reading from and writing to a shared communication channel.\nBuilding on this, Olsson et al.~\\cite{olsson2022} identified induction heads as a mechanistic basis for in-context learning, with specific attention heads implementing token-copying algorithms.",
    "new_string": "Elhage et al.~\\cite{elhage2021} introduced the residual stream framework, in which each layer reads from and writes to a shared communication channel.\nBuilding on this, Olsson et al.~\\cite{olsson2022} identified induction heads as a mechanistic basis for in-context learning; these specialized attention heads implement token-copying algorithms."
  }
}
```

</details>

---

### Tool result

_source line 54 · 2026-05-17T05:00:12.082379+00:00_

The file /home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/related_work.tex has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_20260517T045531",
  "tool": "Edit",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 55 · 2026-05-17T05:00:12.082515+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_20260517T045531",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/related_work.tex"
  }
}
```

</details>

---

### Tool result

_source line 56 · 2026-05-17T05:00:12.082665+00:00_

1	\section{Related Work}\label{sec:related_work}
2	
3	\paragraph{Vision-language-action models.}
4	VLAs fine-tune large language models on robot demonstrations to produce action tokens conditioned on visual observations and language instructions~\cite{brohan2023_rt2,kim2024_openvla,karamcheti2024,black2024_pi0}.
5	This architecture family inherits the transformer backbone and its multi-modal fusion mechanisms from vision-language models, but repurposes them for continuous control.
6	A central assumption is that fine-tuning injects action-relevant knowledge into pretrained representations.
7	We test this assumption at the representational level through per-layer, per-token-type decomposition.
8	
9	\paragraph{Mechanistic interpretability in transformers.}
10	A growing body of work analyzes transformer internals at the level of individual attention heads and circuits.
11	Elhage et al.~\cite{elhage2021} introduced the residual stream framework, in which each layer reads from and writes to a shared communication channel.
12	Building on this, Olsson et al.~\cite{olsson2022} identified induction heads as a mechanistic basis for in-context learning; these specialized attention heads implement token-copying algorithms.
13	Circuit-level analyses have since traced complete computational subgraphs for tasks such as indirect object identification~\cite{wang2023_ioi} and greater-than comparison~\cite{conmy2023}.
14	In parallel, attention probing studies have shown that individual heads encode syntactic relations~\cite{clark2019}, capture positional and structural patterns at different depths~\cite{vig2019}, and that a small subset of specialized heads accounts for most model performance~\cite{voita2019}.
15	Our Layer-1 attention head analysis extends this tradition to the VLA domain, where we find that 25 of 32 heads become instruction-dominant after fine-tuning.
16	
17	\paragraph{Behavioral and mechanistic analysis of VLAs.}
18	Behavioral evaluations reveal that current VLAs rel
…[truncated 3762 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_20260517T045531",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 57 · 2026-05-17T05:00:12.082872+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/related_work.tex",
  "old_string": "Singular Vector Canonical Correlation Analysis (SVCCA)~\\cite{raghu2017} and projection-weighted CCA~\\cite{morcos2018} extended this approach to deep networks, enabling layer-wise comparison of learned representations across architectures and training stages.",
  "new_string": "Singular Vector Canonical Correlation Analysis (SVCCA)~\\cite{raghu2017} and projection-weighted CCA~\\cite{morcos2018} extended this approach to deep networks and enabled layer-wise comparison of learned representations across architectures and training stages."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_20260517T045531",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/related_work.tex",
    "old_string": "Singular Vector Canonical Correlation Analysis (SVCCA)~\\cite{raghu2017} and projection-weighted CCA~\\cite{morcos2018} extended this approach to deep networks, enabling layer-wise comparison of learned representations across architectures and training stages.",
    "new_string": "Singular Vector Canonical Correlation Analysis (SVCCA)~\\cite{raghu2017} and projection-weighted CCA~\\cite{morcos2018} extended this approach to deep networks and enabled layer-wise comparison of learned representations across architectures and training stages."
  }
}
```

</details>

---

### Tool result

_source line 58 · 2026-05-17T05:00:12.083134+00:00_

The file /home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/related_work.tex has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_20260517T045531",
  "tool": "Edit",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 59 · 2026-05-17T05:00:12.083283+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/related_work.tex",
  "old_string": "On the functional side, linear probes~\\cite{alain2017,hewitt2019} and the broader probing methodology literature~\\cite{belinkov2022} test whether specific information is linearly decodable from intermediate representations, complementing geometric measures with task-oriented evaluation.",
  "new_string": "On the functional side, linear probes~\\cite{alain2017,hewitt2019} and the broader probing methodology literature~\\cite{belinkov2022} test whether specific information is linearly decodable from intermediate representations. These functional measures complement the geometric approaches by providing task-oriented evaluation."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_20260517T045531",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/related_work.tex",
    "old_string": "On the functional side, linear probes~\\cite{alain2017,hewitt2019} and the broader probing methodology literature~\\cite{belinkov2022} test whether specific information is linearly decodable from intermediate representations, complementing geometric measures with task-oriented evaluation.",
    "new_string": "On the functional side, linear probes~\\cite{alain2017,hewitt2019} and the broader probing methodology literature~\\cite{belinkov2022} test whether specific information is linearly decodable from intermediate representations. These functional measures complement the geometric approaches by providing task-oriented evaluation."
  }
}
```

</details>

---

### Tool result

_source line 60 · 2026-05-17T05:00:12.083435+00:00_

The file /home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/related_work.tex has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_20260517T045531",
  "tool": "Edit",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 61 · 2026-05-17T05:00:12.083581+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "grep -n \"—\\|–\" related_work.tex; grep -nP \"ing[,.]\" related_work.tex | grep -v \"\\\\\\\\cite\\|string\\|thing\\|bring\\|during\\|using\" ; grep -in \"Furthermore\\|Moreover\\|Additionally\\|delve\\|leverage\\|utilize\" related_work.tex",
  "description": "Final check for banned patterns"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_20260517T045531",
  "tool": "Bash",
  "tool_args": {
    "command": "grep -n \"—\\|–\" related_work.tex; grep -nP \"ing[,.]\" related_work.tex | grep -v \"\\\\\\\\cite\\|string\\|thing\\|bring\\|during\\|using\" ; grep -in \"Furthermore\\|Moreover\\|Additionally\\|delve\\|leverage\\|utilize\" related_work.tex",
    "description": "Final check for banned patterns"
  }
}
```

</details>

---

### Tool result

_source line 62 · 2026-05-17T05:00:12.083710+00:00_

15:Our Layer-1 attention head analysis extends this tradition to the VLA domain, where we find that 25 of 32 heads become instruction-dominant after fine-tuning.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_20260517T045531",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 63 · 2026-05-17T05:00:12.083851+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "grep -nP \", (identifying|revealing|isolating|enabling|providing|demonstrating|showing|indicating|suggesting|highlighting)\" related_work.tex",
  "description": "Check for trailing participial -ing phrases after commas"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_20260517T045531",
  "tool": "Bash",
  "tool_args": {
    "command": "grep -nP \", (identifying|revealing|isolating|enabling|providing|demonstrating|showing|indicating|suggesting|highlighting)\" related_work.tex",
    "description": "Check for trailing participial -ing phrases after commas"
  }
}
```

</details>

---

### Tool result

_source line 64 · 2026-05-17T05:00:12.084007+00:00_

24:Our work differs in three respects: (1) we decompose at the token level rather than the feature level, identifying the readout token as the sole multimodal integration site; (2) we track representations across all 32 layers, revealing a non-monotonic transformation profile invisible to whole-model analyses; and (3) we include trained-vs-untrained factorial controls that isolate the effect of fine-tuning on attention routing mechanisms.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_20260517T045531",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 65 · 2026-05-17T05:00:12.084159+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/related_work.tex",
  "old_string": "Our work differs in three respects: (1) we decompose at the token level rather than the feature level, identifying the readout token as the sole multimodal integration site; (2) we track representations across all 32 layers, revealing a non-monotonic transformation profile invisible to whole-model analyses; and (3) we include trained-vs-untrained factorial controls that isolate the effect of fine-tuning on attention routing mechanisms.",
  "new_string": "Our work differs in three respects: (1) we decompose at the token level rather than the feature level and identify the readout token as the sole multimodal integration site; (2) we track representations across all 32 layers and reveal a non-monotonic transformation profile invisible to whole-model analyses; and (3) we include trained-vs-untrained factorial controls that isolate the effect of fine-tuning on attention routing mechanisms."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_20260517T045531",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/related_work.tex",
    "old_string": "Our work differs in three respects: (1) we decompose at the token level rather than the feature level, identifying the readout token as the sole multimodal integration site; (2) we track representations across all 32 layers, revealing a non-monotonic transformation profile invisible to whole-model analyses; and (3) we include trained-vs-untrained factorial controls that isolate the effect of fine-tuning on attention routing mechanisms.",
    "new_string": "Our work differs in three respects: (1) we decompose at the token level rather than the feature level and identify the readout token as the sole multimodal integration site; (2) we track representations across all 32 layers and reveal a non-monotonic transformation profile invisible to whole-model analyses; and (3) we include trained-vs-untrained factorial controls that isolate the effect of fine-tuning on attention routing mechanisms."
  }
}
```

</details>

---

### Tool result

_source line 66 · 2026-05-17T05:00:12.084403+00:00_

The file /home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/related_work.tex has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_20260517T045531",
  "tool": "Edit",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 67 · 2026-05-17T05:00:12.084598+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "grep -nP \", (identifying|revealing|isolating|enabling|providing|demonstrating|showing|indicating|suggesting|highlighting|implementing|treating)\" related_work.tex",
  "description": "Final check for trailing -ing participial phrases"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_20260517T045531",
  "tool": "Bash",
  "tool_args": {
    "command": "grep -nP \", (identifying|revealing|isolating|enabling|providing|demonstrating|showing|indicating|suggesting|highlighting|implementing|treating)\" related_work.tex",
    "description": "Final check for trailing -ing participial phrases"
  }
}
```

</details>

---

### Tool result

_source line 68 · 2026-05-17T05:00:12.084802+00:00_

(Bash completed with no output)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_20260517T045531",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 69 · 2026-05-17T05:00:12.085035+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "wc -l related_work.tex; echo \"---\"; echo \"New bib keys added:\"; comm -23 <(grep -oP '\\\\cite\\{[^}]+\\}' related_work.tex | sed 's/\\\\cite{//;s/}//' | tr ',' '\\n' | sort -u) <(echo -e \"brohan2023_rt2\\nkim2024_openvla\\nkaramcheti2024\\ngrant2026\\nhou2026\\nfei2025\\nhaon2025\\nswann2026\\nbuurmeijer2026\\nlu2025\\nmolinari2025\\nfang2025\\nkriegeskorte2008\\nalain2017\\nbelinkov2022\\nkornblith2019\\noquab2024_dinov2\\nradford2021_clip\\nzhai2023_siglip\\nblack2024_pi0\" | sort -u)",
  "description": "Count lines and identify new citations"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_20260517T045531",
  "tool": "Bash",
  "tool_args": {
    "command": "wc -l related_work.tex; echo \"---\"; echo \"New bib keys added:\"; comm -23 <(grep -oP '\\\\cite\\{[^}]+\\}' related_work.tex | sed 's/\\\\cite{//;s/}//' | tr ',' '\\n' | sort -u) <(echo -e \"brohan2023_rt2\\nkim2024_openvla\\nkaramcheti2024\\ngrant2026\\nhou2026\\nfei2025\\nhaon2025\\nswann2026\\nbuurmeijer2026\\nlu2025\\nmolinari2025\\nfang2025\\nkriegeskorte2008\\nalain2017\\nbelinkov2022\\nkornblith2019\\noquab2024_dinov2\\nradford2021_clip\\nzhai2023_siglip\\nblack2024_pi0\" | sort -u)",
    "description": "Count lines and identify new citations"
  }
}
```

</details>

---

### Tool result

_source line 70 · 2026-05-17T05:00:12.085235+00:00_

39 related_work.tex
---
New bib keys added:
clark2019
conmy2023
darcet2024
dosovitskiy2021
elhage2021
geva2021
hewitt2019
morcos2018
olsson2022
raghu2017
tenney2019
vig2019
voita2019
wang2023_ioi

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_20260517T045531",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 71 · 2026-05-17T05:00:12.085476+00:00_

Done. The expanded Related Work now has:

- **5 paragraphs** (from 3), covering all 4 required new areas
- **14 new verified citations** (exceeds the 8-10 minimum): olsson2022, clark2019, vig2019, voita2019, conmy2023, elhage2021, wang2023_ioi, darcet2024, dosovitskiy2021, geva2021, tenney2019, raghu2017, morcos2018, hewitt2019
- **39 lines** (from 16), roughly ~1.5 pages when typeset
- All cite keys have matching bib entries
- No em-dashes, no trailing -ing phrases, no banned transitions or vocabulary

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_paper_writing_20260517T045531"
}
```

</details>

---
