# paper writing related work

**How Does Schema Complexity Predict Performance in Training-Free LLM Information Extraction?** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 25
- **Recorded user turns:** 0
- **Tool calls:** 12
- **Original source:** `logs/chats/worker_paper_writing_related_work_20260515T181022.jsonl`
- **Structured JSON:** [`c41f499e437c6e782e30.json`](../../sessions/c4/c41f499e437c6e782e30.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

25 recorded events

### Tool call

_source line 1 · 2026-05-15T18:12:54.137657+00:00_

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
  "session": "worker_paper_writing_related_work_20260515T181022",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/agent-ml-research/skills/global/latex-paper.skill.md"
  }
}
```

</details>

---

### Tool result

_source line 2 · 2026-05-15T18:12:54.138261+00:00_

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
  "session": "worker_paper_writing_related_work_20260515T181022",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-15T18:12:54.138454+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/references.bib"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_related_work_20260515T181022",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/references.bib"
  }
}
```

</details>

---

### Tool result

_source line 4 · 2026-05-15T18:12:54.138702+00:00_

1	% References for Schema-DAG-Extraction
2	% Generated: 2026-05-15
3	% Sources: literature_map.yaml + references_survey.md
4	
5	% =============================================================================
6	% DIRECT COMPETITORS
7	% =============================================================================
8	
9	@inproceedings{llm-pee-2025,
10	    title     = {Towards Event Extraction with Massive Types: {LLM}-based Collaborative Annotation and Partitioning Extraction},
11	    author    = {Liu, Wenxuan and Li, Zixuan and Bai, Long and Zuo, Yuxin and Xu, Daozhu and Jin, Xiaolong and Guo, Jiafeng and Cheng, Xueqi},
12	    booktitle = {Proceedings of the 2025 Conference on Empirical Methods in Natural Language Processing},
13	    year      = {2025},
14	    url       = {https://aclanthology.org/2025.emnlp-main.1743/},
15	}
16	
17	@article{parse-2025,
18	    title   = {{PARSE}: {LLM} Driven Schema Optimization for Reliable Entity Extraction},
19	    author  = {Shrimal, Anubhav and Jain, Aryan and Chowdhury, Soumyajit and Yenigalla, Promod},
20	    journal = {arXiv preprint arXiv:2510.08623},
21	    year    = {2025},
22	    url     = {https://arxiv.org/abs/2510.08623},
23	}
24	
25	@inproceedings{dee-2024,
26	    title     = {Decompose, Enrich, and Extract! Schema-aware Event Extraction using {LLM}s},
27	    author    = {Shiri, Fatemeh and Nguyen, Van and Moghimifar, Farhad and Yoo, John and Haffari, Gholamreza and Li, Yuan-Fang},
28	    booktitle = {Proceedings of the IEEE International Conference on Tools with Artificial Intelligence},
29	    year      = {2024},
30	    url       = {https://arxiv.org/abs/2406.01045},
31	}
32	
33	@inproceedings{crossagentie-2025,
34	    title     = {{CROSSAGENTIE}: Cross-Type and Cross-Task Multi-Agent {LLM} Collaboration for Zero-Shot Information Extraction},
35	    author    = {Lu, Meng and Xie, Yuzhang and Bi, Zhenyu and Cao, Shuxiang and Wang, Xuan},
36	    booktitle = {Findings of the Association for Computational Linguistics: ACL
…[truncated 19521 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_related_work_20260515T181022",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-15T18:12:54.138888+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/experimental_setup.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_related_work_20260515T181022",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/experimental_setup.tex"
  }
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-15T18:12:54.139072+00:00_

1	\section{Experimental Setup}
2	\label{sec:experimental_setup}
3	
4	We evaluate how prompt schema size and inter-type confusability affect zero-shot LLM extraction across three information extraction tasks: named entity recognition (NER), relation extraction (RE), and event detection (ED).
5	
6	\subsection{Tasks and Datasets}
7	\label{sec:datasets}
8	
9	\paragraph{Few-NERD (NER).}
10	Few-NERD \cite{PLACEHOLDER_fewnerd} provides 66 fine-grained entity types organized into 8 coarse categories (person, location, organization, building, art, product, event, other). The dataset spans diverse domains, making it suitable for cross-domain evaluation. We sample 1{,}000 test instances and evaluate with token-level text matching.
11	
12	\paragraph{FewRel (RE).}
13	FewRel \cite{PLACEHOLDER_fewrel} contains 80 relation types sourced from Wikidata. We combine the training and validation splits to obtain the full set of 80 relations and sample 1{,}000 balanced instances. Each instance provides a sentence with marked head and tail entities; the task is to classify the relation.
14	
15	\paragraph{MAVEN (ED).}
16	MAVEN \cite{PLACEHOLDER_maven} defines 168 event types derived from the FrameNet ontology, making it a same-domain schema. We use the validation set (8{,}042 sentences containing 18{,}904 event mentions) for evaluation, as test set labels are not publicly available. The task requires both trigger identification and event type classification.
17	
18	Table~\ref{tab:datasets} summarizes the dataset statistics, including the Schema Confusability Score (SCS) ranges defined in \S\ref{sec:scs}.
19	
20	\begin{table}[t]
21	\centering
22	\small
23	\begin{tabular}{llrrlll}
24	\toprule
25	\textbf{Dataset} & \textbf{Task} & \textbf{\# Types} & \textbf{\# Samples} & \textbf{Domain} & \textbf{SCS Range} & \textbf{Embedding} \\
26	\midrule
27	Few-NERD & NER & 66 & 1{,}000 & Cross & 0.77--0.93 & Qwen3-32B \\
28	FewRel & RE & 80 & 1{,}000 & Cross & 0.42--0.97 & MiniLM \\
29	MAVEN & ED & 168 
…[truncated 5012 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_related_work_20260515T181022",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-15T18:12:54.139223+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/results.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_related_work_20260515T181022",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/results.tex"
  }
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-15T18:12:54.139410+00:00_

1	\section{Results}
2	\label{sec:results}
3	
4	\subsection{Count-Degradation Curves}
5	\label{sec:count_curves}
6	
7	We first examine how extraction performance changes as the number of types in the prompt schema increases (Experiment~1). Figure~\ref{fig:count_curves} plots per-task metrics across count levels.
8	
9	\paragraph{NER (Few-NERD).}
10	Recall declines monotonically from 0.72 at count${}\,=\,1$ to 0.42 at count${}\,=\,64$, a 42\% relative drop. Precision moves in the opposite direction, rising from 0.11 to 0.52, reflecting a shift from over-prediction to under-prediction as more candidate types compete in the prompt. F1 exhibits an inverted-U shape, peaking at intermediate counts where the precision--recall trade-off is most balanced.
11	
12	\paragraph{RE (FewRel).}
13	Accuracy drops monotonically from 85.7\% at count${}\,=\,1$ to 50.4\% at count${}\,=\,80$, a near-halving when the model must discriminate among all 80 relation types simultaneously.
14	
15	\paragraph{ED (MAVEN).}
16	In contrast to NER and RE, MAVEN relaxed F1 \emph{increases} from 0.106 at count${}\,=\,1$ to 0.247 at count${}\,=\,44$. This reversal arises from three properties of the MAVEN setup: (i)~trigger-level relaxed matching, which requires only token overlap rather than exact span match; (ii)~MAVEN's 168 event types derive from the FrameNet ontology, forming a same-domain hierarchy where co-presented types provide disambiguating context; and (iii)~extreme class imbalance---rare event types benefit from being presented alongside related types that prime the model toward the correct semantic region. We return to this mechanism in \S\ref{sec:centrality_confound}.
17	
18	\paragraph{Summary.}
19	Schema size degrades extraction quality for NER and RE (Channel~1: count $\to$ recall decline), but this pattern does not hold universally. MAVEN's reversed trend demonstrates that task structure and evaluation protocol mediate the count--performance relationship.
20	
21	\subsection{Pairwise Confu
…[truncated 8986 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_related_work_20260515T181022",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-15T18:12:54.139585+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/related_work.tex",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_related_work_20260515T181022",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/related_work.tex",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper"
  }
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-15T18:12:54.139703+00:00_

No files found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_related_work_20260515T181022",
  "tool": "Glob",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-15T18:12:54.139813+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/*.tex",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_related_work_20260515T181022",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/*.tex",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper"
  }
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-15T18:12:54.139947+00:00_

docs/paper/experimental_setup.tex
docs/paper/results.tex
docs/paper/sdgd_negative.tex

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_related_work_20260515T181022",
  "tool": "Glob",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-15T18:12:54.140065+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/sdgd_negative.tex",
  "limit": "80"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_related_work_20260515T181022",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/sdgd_negative.tex",
    "limit": "80"
  }
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-15T18:12:54.140214+00:00_

1	\section{Why Naive Decomposition Fails}
2	\label{sec:sdgd}
3	
4	The multi-channel degradation model (\S\ref{sec:results}) raises an interventional question: if confusability drives type confusion, can we decompose the schema so that confusable types never co-occur in the same prompt?  We test this idea with \textbf{Schema-DAG-Guided Decomposition} (SDGD), a method that uses the pairwise SCS matrix to partition types into low-confusability batches, runs extraction independently on each batch, and merges the results.
5	
6	\paragraph{Decomposition protocol.}
7	We compute hierarchical clustering over the SCS matrix and cut the dendrogram so that highly similar types fall into separate batches. Each batch is presented to the LLM as an independent extraction prompt; predictions are then merged via set union. We compare four modes: (i)~\textbf{single\_pass}, the undecomposed baseline; (ii)~\textbf{sdgd\_zero}, SCS-guided partitioning; (iii)~\textbf{random\_batch}, random partitioning with matched batch sizes; and (iv)~\textbf{per\_type}, the extreme case where each type is extracted in isolation, following the strategy of \citet{uniner-2024}. Figure~\ref{fig:sdgd_comparison} summarizes the results on Few-NERD.
8	
9	\paragraph{All decomposition modes degrade F1.}
10	Table~\ref{tab:sdgd_results} reports the outcome.  Single-pass extraction achieves F1\,=\,0.445 (P\,=\,0.563, R\,=\,0.368).  SDGD obtains F1\,=\,0.251 (P\,=\,0.210, R\,=\,0.314), a 44\% relative drop.  Random batching reaches F1\,=\,0.320 (P\,=\,0.249, R\,=\,0.446), and per-type extraction yields F1\,=\,0.292 (P\,=\,0.194, R\,=\,0.586).  Every decomposition mode falls below the single-pass baseline.
11	
12	\begin{table}[t]
13	\centering
14	\small
15	\begin{tabular}{lccc}
16	\toprule
17	\textbf{Mode} & \textbf{Precision} & \textbf{Recall} & \textbf{F1} \\
18	\midrule
19	single\_pass & 0.563 & 0.368 & 0.445 \\
20	\midrule
21	sdgd\_zero (v1) & 0.210 & 0.314 & 0.251 \\
22	random\_batch (v1) & 0.249 & 0.446 & 0.320
…[truncated 3164 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_related_work_20260515T181022",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-15T18:12:54.140435+00:00_

called Write

<details open><summary>🔧 Tool call — Write</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/related_work.tex",
  "content": "\\section{Related Work}\n\\label{sec:related_work}\n\n\\subsection{Training-Free LLM Information Extraction}\n\\label{sec:rw_training_free}\n\nRecent surveys categorize LLM-based IE along instruction-tuning and code-generation axes \\cite{llm4ie-survey-2024}. \\citet{instructuie-2023} pioneered multi-task instruction tuning for unified IE. On the generalist front, \\citet{knowcoder-2024} encode structured knowledge into LLMs via code-style schemas, \\citet{gollie-2024} leverage annotation guidelines for zero-shot IE, and \\citet{codeie-2023} reformulate extraction as code generation. \\citet{adelie-2024} align LLMs on IE through targeted instruction tuning, while \\citet{oneke-2025} provide a dockerized schema-guided agent system. For structured output, \\citet{slot-2025} propose schema-driven decoding that constrains LLM generation to valid extraction formats.\n\nFor NER specifically, \\citet{uniner-2024} distill open NER capability from ChatGPT into smaller models, \\citet{gliner-2024} introduce a bidirectional transformer for generalist NER with \\citet{gliner2-2025} extending it to multi-task IE, and \\citet{nuner-2024} pre-train entity recognition encoders on LLM-annotated data. Zero-shot approaches include self-improving NER through iterative refinement \\cite{self-improve-ner-2024}, type-description-driven recognition \\cite{zeroner-2025}, reasoning-based NER paradigms \\cite{reasoning-ner-2025}, and guided synthetic data generation \\cite{guidex-2025}. For relation extraction, \\citet{self-prompting-re-2024} use self-prompting to enable zero-shot relation classification, and \\citet{code4uie-2024} augment code-generation IE with retrieval. \\citet{familiarity-2025} highlight evaluation pitfalls in zero-shot NER by quantifying label shifts between synthetic training data and target schemas.\n\nThese methods demonstrate strong performance on benchmarks with moderate schema sizes (typically 4--20 types). However, none systematically investigates how performance degrades as schema complexity scales---either in the number of candidate types or in inter-type semantic similarity. Our work addresses this gap with controlled experiments isolating the effects of schema size and type confusability on training-free LLM extraction.\n\n\\subsection{Schema Complexity in IE}\n\\label{sec:rw_schema}\n\nThe most directly related work is LLM-PEE \\cite{llm-pee-2025}, which addresses event extraction with massive type inventories by partitioning schemas based on type embedding similarity. LLM-PEE clusters event types and assigns each cluster to a separate extraction prompt, demonstrating improved performance on schemas with hundreds of types. Our work is complementary in three respects. First, whereas LLM-PEE develops an engineering solution---partition to improve extraction---we conduct controlled empirical analysis to understand \\emph{why} extraction degrades. Second, LLM-PEE does not disentangle the effects of type count from type confusability; their partitioning simultaneously reduces both. Our BCS-controlled experiments (\\S\\ref{sec:bcs_controlled}) isolate these as independent degradation channels. Third, our pairwise SCS analysis provides a theoretical explanation for why their similarity-based partitioning works: it reduces Batch Confusability Scores, directly targeting the Channel~2 degradation mechanism. Our SDGD experiments (\\S\\ref{sec:sdgd}) further reveal that the merge step---not partitioning quality---is the bottleneck in decompose-then-merge pipelines, a limitation that applies to LLM-PEE's approach as well.\n\nSeveral other approaches address schema complexity from different angles. \\citet{iepile-2024} construct a large-scale IE corpus using hard negative mining during training, where confusable types are deliberately included to improve robustness---related to our confusability analysis but in a supervised setting. \\citet{parse-2025} rewrite and optimize schema definitions to improve extraction reliability, addressing the quality rather than the structure of type descriptions. \\citet{dee-2024} decompose event schemas into sub-components before enriching and extracting, treating schema complexity through structural decomposition rather than confusability analysis. \\citet{crossagentie-2025} employ multi-agent debate for cross-type IE, resolving errors \\emph{post hoc} through reactive discussion rather than our proactive analysis of degradation causes. \\citet{cmas-ner-2025} similarly use cooperative multi-agent frameworks for zero-shot NER. \\citet{spt-2025} parameterize schemas as callable tools, abstracting complexity behind a tool-use interface, while \\citet{dlisc-2025} target on-device schema-aware IE under efficiency constraints. \\citet{kggen-2025} generate knowledge graphs under schema constraints, facing analogous scaling challenges when the target ontology grows.\n\nAll these methods treat schema complexity as an engineering problem to mitigate. We instead treat it as a scientific question: what are the independent mechanisms by which schema properties degrade extraction, and how can they be quantified?\n\n\\subsection{Representation Degeneration and Embedding Anisotropy}\n\\label{sec:rw_anisotropy}\n\nOur centrality confound analysis (\\S\\ref{sec:centrality_confound}) connects to the representation degeneration literature. \\citet{gao-repr-degen-2019} showed that word embeddings trained with language modeling objectives degenerate into a narrow cone, occupying only a subset of available directions. \\citet{ethayarajh-contextual-2019} extended this to contextual representations, demonstrating that BERT, ELMo, and GPT-2 embeddings are highly anisotropic, with upper layers occupying increasingly narrow cones.\n\nCrucially, \\citet{cai-isotropy-clusters-2021} showed that while the global embedding space is anisotropic, local clusters can be approximately isotropic. This cluster-level analysis directly explains our MAVEN results: when all 168 event types derive from a single ontology (FrameNet), their embeddings form one dense cluster where a type's mean confusability conflates semantic similarity with centrality. \\citet{godey-anisotropy-inherent-2024} proved that anisotropy is mathematically inherent to self-attention, not merely a training artifact, suggesting the centrality confound will persist across architectures. \\citet{rajaee-cluster-isotropy-2021} proposed removing dominant directions to improve isotropy, a technique that could inform centrality correction for same-domain schemas.\n\nOur work provides the first empirical demonstration that representation anisotropy creates a measurable confound in IE schema analysis, manifesting as a sign reversal in the confusability--error correlation for homogeneous ontologies.\n\n\\subsection{Context Length and Position Effects}\n\\label{sec:rw_position}\n\n\\citet{lost-in-middle-2024} demonstrated that LLMs attend preferentially to information at the beginning and end of long contexts, with retrieval accuracy degrading for items positioned in the middle. This positional bias has direct implications for IE schema prompts: when dozens of type definitions are listed sequentially, types in the middle positions may receive reduced attention. While we control for type ordering through random batching across trials, we do not fully investigate positional effects as an independent degradation channel. Disentangling positional attention decay from confusability-driven type confusion in large-schema IE prompts remains an open direction for future work.\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_related_work_20260515T181022",
  "tool": "Write",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/related_work.tex",
    "content": "\\section{Related Work}\n\\label{sec:related_work}\n\n\\subsection{Training-Free LLM Information Extraction}\n\\label{sec:rw_training_free}\n\nRecent surveys categorize LLM-based IE along instruction-tuning and code-generation axes \\cite{llm4ie-survey-2024}. \\citet{instructuie-2023} pioneered multi-task instruction tuning for unified IE. On the generalist front, \\citet{knowcoder-2024} encode structured knowledge into LLMs via code-style schemas, \\citet{gollie-2024} leverage annotation guidelines for zero-shot IE, and \\citet{codeie-2023} reformulate extraction as code generation. \\citet{adelie-2024} align LLMs on IE through targeted instruction tuning, while \\citet{oneke-2025} provide a dockerized schema-guided agent system. For structured output, \\citet{slot-2025} propose schema-driven decoding that constrains LLM generation to valid extraction formats.\n\nFor NER specifically, \\citet{uniner-2024} distill open NER capability from ChatGPT into smaller models, \\citet{gliner-2024} introduce a bidirectional transformer for generalist NER with \\citet{gliner2-2025} extending it to multi-task IE, and \\citet{nuner-2024} pre-train entity recognition encoders on LLM-annotated data. Zero-shot approaches include self-improving NER through iterative refinement \\cite{self-improve-ner-2024}, type-description-driven recognition \\cite{zeroner-2025}, reasoning-based NER paradigms \\cite{reasoning-ner-2025}, and guided synthetic data generation \\cite{guidex-2025}. For relation extraction, \\citet{self-prompting-re-2024} use self-prompting to enable zero-shot relation classification, and \\citet{code4uie-2024} augment code-generation IE with retrieval. \\citet{familiarity-2025} highlight evaluation pitfalls in zero-shot NER by quantifying label shifts between synthetic training data and target schemas.\n\nThese methods demonstrate strong performance on benchmarks with moderate schema sizes (typically 4--20 types). However, none systematically investigates how performance degrades as schema complexity scales---either in the number of candidate types or in inter-type semantic similarity. Our work addresses this gap with controlled experiments isolating the effects of schema size and type confusability on training-free LLM extraction.\n\n\\subsection{Schema Complexity in IE}\n\\label{sec:rw_schema}\n\nThe most directly related work is LLM-PEE \\cite{llm-pee-2025}, which addresses event extraction with massive type inventories by partitioning schemas based on type embedding similarity. LLM-PEE clusters event types and assigns each cluster to a separate extraction prompt, demonstrating improved performance on schemas with hundreds of types. Our work is complementary in three respects. First, whereas LLM-PEE develops an engineering solution---partition to improve extraction---we conduct controlled empirical analysis to understand \\emph{why} extraction degrades. Second, LLM-PEE does not disentangle the effects of type count from type confusability; their partitioning simultaneously reduces both. Our BCS-controlled experiments (\\S\\ref{sec:bcs_controlled}) isolate these as independent degradation channels. Third, our pairwise SCS analysis provides a theoretical explanation for why their similarity-based partitioning works: it reduces Batch Confusability Scores, directly targeting the Channel~2 degradation mechanism. Our SDGD experiments (\\S\\ref{sec:sdgd}) further reveal that the merge step---not partitioning quality---is the bottleneck in decompose-then-merge pipelines, a limitation that applies to LLM-PEE's approach as well.\n\nSeveral other approaches address schema complexity from different angles. \\citet{iepile-2024} construct a large-scale IE corpus using hard negative mining during training, where confusable types are deliberately included to improve robustness---related to our confusability analysis but in a supervised setting. \\citet{parse-2025} rewrite and optimize schema definitions to improve extraction reliability, addressing the quality rather than the structure of type descriptions. \\citet{dee-2024} decompose event schemas into sub-components before enriching and extracting, treating schema complexity through structural decomposition rather than confusability analysis. \\citet{crossagentie-2025} employ multi-agent debate for cross-type IE, resolving errors \\emph{post hoc} through reactive discussion rather than our proactive analysis of degradation causes. \\citet{cmas-ner-2025} similarly use cooperative multi-agent frameworks for zero-shot NER. \\citet{spt-2025} parameterize schemas as callable tools, abstracting complexity behind a tool-use interface, while \\citet{dlisc-2025} target on-device schema-aware IE under efficiency constraints. \\citet{kggen-2025} generate knowledge graphs under schema constraints, facing analogous scaling challenges when the target ontology grows.\n\nAll these methods treat schema complexity as an engineering problem to mitigate. We instead treat it as a scientific question: what are the independent mechanisms by which schema properties degrade extraction, and how can they be quantified?\n\n\\subsection{Representation Degeneration and Embedding Anisotropy}\n\\label{sec:rw_anisotropy}\n\nOur centrality confound analysis (\\S\\ref{sec:centrality_confound}) connects to the representation degeneration literature. \\citet{gao-repr-degen-2019} showed that word embeddings trained with language modeling objectives degenerate into a narrow cone, occupying only a subset of available directions. \\citet{ethayarajh-contextual-2019} extended this to contextual representations, demonstrating that BERT, ELMo, and GPT-2 embeddings are highly anisotropic, with upper layers occupying increasingly narrow cones.\n\nCrucially, \\citet{cai-isotropy-clusters-2021} showed that while the global embedding space is anisotropic, local clusters can be approximately isotropic. This cluster-level analysis directly explains our MAVEN results: when all 168 event types derive from a single ontology (FrameNet), their embeddings form one dense cluster where a type's mean confusability conflates semantic similarity with centrality. \\citet{godey-anisotropy-inherent-2024} proved that anisotropy is mathematically inherent to self-attention, not merely a training artifact, suggesting the centrality confound will persist across architectures. \\citet{rajaee-cluster-isotropy-2021} proposed removing dominant directions to improve isotropy, a technique that could inform centrality correction for same-domain schemas.\n\nOur work provides the first empirical demonstration that representation anisotropy creates a measurable confound in IE schema analysis, manifesting as a sign reversal in the confusability--error correlation for homogeneous ontologies.\n\n\\subsection{Context Length and Position Effects}\n\\label{sec:rw_position}\n\n\\citet{lost-in-middle-2024} demonstrated that LLMs attend preferentially to information at the beginning and end of long contexts, with retrieval accuracy degrading for items positioned in the middle. This positional bias has direct implications for IE schema prompts: when dozens of type definitions are listed sequentially, types in the middle positions may receive reduced attention. While we control for type ordering through random batching across trials, we do not fully investigate positional effects as an independent degradation channel. Disentangling positional attention decay from confusability-driven type confusion in large-schema IE prompts remains an open direction for future work.\n"
  }
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-15T18:12:54.140643+00:00_

File created successfully at: /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/related_work.tex

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_related_work_20260515T181022",
  "tool": "Write",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-15T18:12:54.140812+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper && grep -oP '\\\\\\\\cite[tp]?\\{[^}]+\\}' related_work.tex | tr ',' '\\n' | sed 's/.*{//;s/}.*//' | sort -u | wc -l && echo \"---\" && grep -oP '\\\\\\\\cite[tp]?\\{[^}]+\\}' related_work.tex | tr ',' '\\n' | sed 's/.*{//;s/}.*//' | sort -u && echo \"---\" && wc -w related_work.tex",
  "description": "Count distinct citations and word count"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_related_work_20260515T181022",
  "tool": "Bash",
  "tool_args": {
    "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper && grep -oP '\\\\\\\\cite[tp]?\\{[^}]+\\}' related_work.tex | tr ',' '\\n' | sed 's/.*{//;s/}.*//' | sort -u | wc -l && echo \"---\" && grep -oP '\\\\\\\\cite[tp]?\\{[^}]+\\}' related_work.tex | tr ',' '\\n' | sed 's/.*{//;s/}.*//' | sort -u && echo \"---\" && wc -w related_work.tex",
    "description": "Count distinct citations and word count"
  }
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-15T18:12:54.140986+00:00_

0
---
---
864 related_work.tex

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_related_work_20260515T181022",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-15T18:12:54.141106+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "grep -oE '\\\\cite[tp]?\\{[^}]+\\}' related_work.tex | sed 's/\\\\cite[tp]\\{//;s/\\\\cite\\{//;s/\\}//g' | tr ',' '\\n' | sed 's/^ *//;s/ *$//' | sort -u",
  "description": "Extract distinct citation keys"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_related_work_20260515T181022",
  "tool": "Bash",
  "tool_args": {
    "command": "grep -oE '\\\\cite[tp]?\\{[^}]+\\}' related_work.tex | sed 's/\\\\cite[tp]\\{//;s/\\\\cite\\{//;s/\\}//g' | tr ',' '\\n' | sed 's/^ *//;s/ *$//' | sort -u",
    "description": "Extract distinct citation keys"
  }
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-15T18:12:54.141218+00:00_

sed: -e expression #1, char 17: Unmatched \{

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_related_work_20260515T181022",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 21 · 2026-05-15T18:12:54.141334+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "grep -oP 'cite[tp]?\\{[^}]+\\}' /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/related_work.tex | sed 's/cite[tp]\\{//;s/cite\\{//;s/}//g' | tr ',' '\\n' | sed 's/^ *//;s/ *$//' | sort -u",
  "description": "Extract distinct citation keys"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_related_work_20260515T181022",
  "tool": "Bash",
  "tool_args": {
    "command": "grep -oP 'cite[tp]?\\{[^}]+\\}' /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/related_work.tex | sed 's/cite[tp]\\{//;s/cite\\{//;s/}//g' | tr ',' '\\n' | sed 's/^ *//;s/ *$//' | sort -u",
    "description": "Extract distinct citation keys"
  }
}
```

</details>

---

### Tool result

_source line 22 · 2026-05-15T18:12:54.141450+00:00_

sed: -e expression #1, char 15: Unmatched \{

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_related_work_20260515T181022",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 23 · 2026-05-15T18:12:54.141560+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "python3 -c \"\nimport re\ntext = open('/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/related_work.tex').read()\nkeys = set()\nfor m in re.findall(r'\\\\\\\\cite[tp]?{([^}]+)}', text):\n    for k in m.split(','):\n        keys.add(k.strip())\nprint(f'Distinct citations: {len(keys)}')\nfor k in sorted(keys):\n    print(f'  {k}')\n# word count (strip latex commands roughly)\nclean = re.sub(r'\\\\\\\\[a-zA-Z]+({[^}]*})?', '', text)\nclean = re.sub(r'[{}\\\\\\\\~]', ' ', clean)\nwords = len(clean.split())\nprint(f'Approx words: {words}')\n\"",
  "description": "Count citations and words via Python"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_related_work_20260515T181022",
  "tool": "Bash",
  "tool_args": {
    "command": "python3 -c \"\nimport re\ntext = open('/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/related_work.tex').read()\nkeys = set()\nfor m in re.findall(r'\\\\\\\\cite[tp]?{([^}]+)}', text):\n    for k in m.split(','):\n        keys.add(k.strip())\nprint(f'Distinct citations: {len(keys)}')\nfor k in sorted(keys):\n    print(f'  {k}')\n# word count (strip latex commands roughly)\nclean = re.sub(r'\\\\\\\\[a-zA-Z]+({[^}]*})?', '', text)\nclean = re.sub(r'[{}\\\\\\\\~]', ' ', clean)\nwords = len(clean.split())\nprint(f'Approx words: {words}')\n\"",
    "description": "Count citations and words via Python"
  }
}
```

</details>

---

### Tool result

_source line 24 · 2026-05-15T18:12:54.141680+00:00_

Distinct citations: 34
  adelie-2024
  cai-isotropy-clusters-2021
  cmas-ner-2025
  code4uie-2024
  codeie-2023
  crossagentie-2025
  dee-2024
  dlisc-2025
  ethayarajh-contextual-2019
  familiarity-2025
  gao-repr-degen-2019
  gliner-2024
  gliner2-2025
  godey-anisotropy-inherent-2024
  gollie-2024
  guidex-2025
  iepile-2024
  instructuie-2023
  kggen-2025
  knowcoder-2024
  llm-pee-2025
  llm4ie-survey-2024
  lost-in-middle-2024
  nuner-2024
  oneke-2025
  parse-2025
  rajaee-cluster-isotropy-2021
  reasoning-ner-2025
  self-improve-ner-2024
  self-prompting-re-2024
  slot-2025
  spt-2025
  uniner-2024
  zeroner-2025
Approx words: 809

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_related_work_20260515T181022",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 25 · 2026-05-15T18:12:54.141827+00:00_

文件已写入 `related_work.tex`。

- **34 个不同引用**（要求 25+）
- **~810 正文词**（去除 LaTeX 命令后；含命令的原始文件 864 词，编译后 ~1000 词左右）
- 4 个小节结构完整，每节末尾有定位句
- LLM-PEE 获得最详细的三段式比较（engineering vs. analysis、count/confusability 未分离、merge bottleneck）
- 全部引用均使用 `references.bib` 中存在的 key，无编造

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_paper_writing_related_work_20260515T181022"
}
```

</details>

---
