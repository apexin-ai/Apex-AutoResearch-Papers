# paper writing introduction

**How Does Schema Complexity Predict Performance in Training-Free LLM Information Extraction?** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 15
- **Recorded user turns:** 0
- **Tool calls:** 7
- **Original source:** `logs/chats/worker_paper_writing_introduction_20260515T183015.jsonl`
- **Structured JSON:** [`6f33b415963a34877fa4.json`](../../sessions/6f/6f33b415963a34877fa4.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

15 recorded events

### Tool call

_source line 1 · 2026-05-15T18:31:43.496313+00:00_

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
  "session": "worker_paper_writing_introduction_20260515T183015",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/agent-ml-research/skills/global/latex-paper.skill.md"
  }
}
```

</details>

---

### Tool result

_source line 2 · 2026-05-15T18:31:43.496976+00:00_

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
  "session": "worker_paper_writing_introduction_20260515T183015",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-15T18:31:43.497195+00:00_

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
  "session": "worker_paper_writing_introduction_20260515T183015",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/results.tex"
  }
}
```

</details>

---

### Tool result

_source line 4 · 2026-05-15T18:31:43.497416+00:00_

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
  "session": "worker_paper_writing_introduction_20260515T183015",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-15T18:31:43.497582+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/sdgd_negative.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_introduction_20260515T183015",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/sdgd_negative.tex"
  }
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-15T18:31:43.497751+00:00_

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
  "session": "worker_paper_writing_introduction_20260515T183015",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-15T18:31:43.497925+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_introduction_20260515T183015",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/related_work.tex"
  }
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-15T18:31:43.498094+00:00_

1	\section{Related Work}
2	\label{sec:related_work}
3	
4	\subsection{Training-Free LLM Information Extraction}
5	\label{sec:rw_training_free}
6	
7	Recent surveys categorize LLM-based IE along instruction-tuning and code-generation axes \cite{llm4ie-survey-2024}. \citet{instructuie-2023} pioneered multi-task instruction tuning for unified IE. On the generalist front, \citet{knowcoder-2024} encode structured knowledge into LLMs via code-style schemas, \citet{gollie-2024} leverage annotation guidelines for zero-shot IE, and \citet{codeie-2023} reformulate extraction as code generation. \citet{adelie-2024} align LLMs on IE through targeted instruction tuning, while \citet{oneke-2025} provide a dockerized schema-guided agent system. For structured output, \citet{slot-2025} propose schema-driven decoding that constrains LLM generation to valid extraction formats.
8	
9	For NER specifically, \citet{uniner-2024} distill open NER capability from ChatGPT into smaller models, \citet{gliner-2024} introduce a bidirectional transformer for generalist NER with \citet{gliner2-2025} extending it to multi-task IE, and \citet{nuner-2024} pre-train entity recognition encoders on LLM-annotated data. Zero-shot approaches include self-improving NER through iterative refinement \cite{self-improve-ner-2024}, type-description-driven recognition \cite{zeroner-2025}, reasoning-based NER paradigms \cite{reasoning-ner-2025}, and guided synthetic data generation \cite{guidex-2025}. For relation extraction, \citet{self-prompting-re-2024} use self-prompting to enable zero-shot relation classification, and \citet{code4uie-2024} augment code-generation IE with retrieval. \citet{familiarity-2025} highlight evaluation pitfalls in zero-shot NER by quantifying label shifts between synthetic training data and target schemas.
10	
11	These methods demonstrate strong performance on benchmarks with moderate schema sizes (typically 4--20 types). However, none systematically investigates how performance degrades
…[truncated 5563 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_introduction_20260515T183015",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-15T18:31:43.498233+00:00_

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
  "session": "worker_paper_writing_introduction_20260515T183015",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/experimental_setup.tex"
  }
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-15T18:31:43.498399+00:00_

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
  "session": "worker_paper_writing_introduction_20260515T183015",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-15T18:31:43.498547+00:00_

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
  "session": "worker_paper_writing_introduction_20260515T183015",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/references.bib"
  }
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-15T18:31:43.498781+00:00_

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
  "session": "worker_paper_writing_introduction_20260515T183015",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-15T18:31:43.499019+00:00_

called Write

<details open><summary>🔧 Tool call — Write</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/introduction.tex",
  "content": "\\section{Introduction}\n\\label{sec:introduction}\n\nTraining-free LLM information extraction---prompting a large language model with a target schema and asking it to extract structured information without any task-specific fine-tuning---enables rapid deployment across new domains and ontologies. This zero-shot paradigm eliminates the need for labeled data, making it attractive for applications where annotation is expensive or schemas evolve frequently \\cite{llm4ie-survey-2024}. Yet the paradigm carries a critical limitation: performance degrades sharply as the number of candidate types in the prompt schema grows. On named entity recognition, recall drops from 0.72 with a single candidate type to 0.42 with 64 types, a 42\\% relative decline. On relation extraction, accuracy falls from 85.7\\% with one relation to 50.4\\% with 80 relations---near halving. This degradation is not academic: real-world ontologies routinely define 50--200+ types, placing them squarely in the regime where training-free extraction becomes unreliable.\n\nWhat causes this schema-induced degradation? Prior work has proposed decomposition strategies that implicitly assume different answers. \\citet{uniner-2024} extract each type independently, assuming types can be treated as separable. \\citet{llm-pee-2025} partition large event schemas by type embedding similarity before extraction, assuming that semantic overlap between co-presented types drives errors. \\citet{parse-2025} rewrite and optimize schema definitions, assuming that description quality is the bottleneck. Each approach improves extraction under certain conditions, but none isolates \\emph{why} schemas degrade performance in the first place. The closest work, LLM-PEE \\cite{llm-pee-2025}, reduces both the number of co-presented types and their inter-type similarity simultaneously, making it impossible to determine which factor---or what combination---accounts for the observed gains. More broadly, all prior approaches conflate two distinct mechanisms that could independently degrade extraction: having more types to discriminate among (count) and having semantically similar types to confuse (confusability). Without disentangling these factors, decomposition strategies cannot be principled: they optimize a black-box objective without understanding its components.\n\nWe ask three questions. \\textbf{RQ1}: Does type confusability independently predict extraction degradation beyond the effect of type count? \\textbf{RQ2}: Through what mechanisms do count and confusability each degrade performance? \\textbf{RQ3}: Can confusability-aware schema decomposition improve extraction quality?\n\nTo answer these questions, we conduct the first controlled empirical study that isolates type confusability from type count across three IE tasks: named entity recognition (NER), relation extraction (RE), and event detection (ED). We introduce the \\emph{Schema Confusability Score} (SCS), which quantifies pairwise semantic overlap between types using embedding cosine similarity, and its batch-level aggregation, the \\emph{Batch Confusability Score} (BCS). We design two complementary experimental paradigms: \\emph{count curves} that vary schema size while randomizing confusability, and \\emph{BCS-controlled experiments} that fix schema size while varying confusability. We evaluate on three datasets spanning diverse schema structures: Few-NERD \\cite{PLACEHOLDER_fewnerd} (66 entity types across 8 domains), FewRel \\cite{PLACEHOLDER_fewrel} (80 relation types), and MAVEN \\cite{PLACEHOLDER_maven} (168 event types from a single ontology). All experiments use Qwen3-32B in a zero-shot prompting setup with bootstrap confidence intervals.\n\nFive findings emerge from our experiments.\n\nFirst, schema-induced degradation operates through two orthogonal channels. \\textbf{Channel~1} (count $\\to$ recall decline): increasing the number of types in the prompt reduces recall for NER and RE, as more candidate types compete for the model's attention. \\textbf{Channel~2} (confusability $\\to$ type confusion): semantically similar types trigger intra-batch substitution errors (IntraSub), where the model assigns an entity or relation to a neighboring type in embedding space. These channels are mechanistically distinct---Channel~1 reflects capacity limitations, Channel~2 reflects semantic indistinguishability---and both contribute to the overall degradation pattern.\n\nSecond, pairwise SCS is a robust predictor of type confusion. Across Few-NERD (Pearson $r = 0.112$, $p < 10^{-12}$) and MAVEN ($r = 0.129$, $p < 10^{-10}$), embedding similarity between type pairs correlates with confusion rates, and this signal replicates across two unrelated embedding spaces (Qwen3 hidden states and MiniLM sentence embeddings). The effect is modest in magnitude: pairwise confusability explains roughly 1.3--1.7\\% of the variance in type confusion ($r^2 \\approx 0.013\\text{--}0.017$). Entity frequency, prompt position effects \\cite{lost-in-middle-2024}, and type definition quality jointly account for the remainder. Nevertheless, this is the first factor to be empirically isolated in controlled zero-shot IE experiments, and the signal survives bootstrap resampling with confidence intervals bounded well above zero.\n\nThird, confusability effects amplify with schema scale. In BCS-controlled FewRel experiments, switching from low-confusability to high-confusability type batches reduces accuracy by 9.1 percentage points at the 16-relation scale, but the gap widens to 31.2\\,pp at 80 relations (95\\% CI: [17.7, 42.7])---a $3.4\\times$ amplification. Larger type pools provide more opportunities for semantically similar types to co-occur, expanding the confusion space.\n\nFourth, per-type confusability aggregation is confounded on homogeneous schemas. On MAVEN, whose 168 event types all derive from the FrameNet ontology, the correlation between mean BCS and per-type error rate reverses sign ($\\rho = +0.189$, $p = 0.021$), opposite to the predicted direction. This centrality confound arises because, in single-cluster embedding spaces \\cite{cai-isotropy-clusters-2021}, a type's mean similarity conflates confusability with centrality---a property associated with well-represented types that LLMs extract reliably. The pairwise SCS signal remains intact ($r = 0.129$, CI: [0.104, 0.156]), confirming that the confound lies in the aggregation step, not in the underlying pairwise relationship. Few-NERD, whose types span multiple domains, does not exhibit this confound ($\\rho = -0.293$, $p = 0.02$).\n\nFifth, confusability-aware schema decomposition fails to improve extraction. Our Schema-DAG-Guided Decomposition (SDGD) successfully separates confusable types into different batches, yet every decomposition mode---including random batching and per-type extraction---produces lower F1 than single-pass extraction (best decomposition F1 = 0.320 vs.\\ single-pass F1 = 0.445). The bottleneck is \\emph{merge amplification}: when the same text is processed across multiple extraction passes, the union merge step accumulates contradictory predictions, destroying precision. This structural limitation applies to any decompose-then-merge pipeline, including the partitioning approach of \\citet{llm-pee-2025}.\n\nOur contributions are:\n\\begin{enumerate}[leftmargin=*,itemsep=2pt,topsep=2pt]\n    \\item \\textbf{Multi-channel degradation model.} We provide the first empirical decomposition of schema-induced degradation into count and confusability channels across NER, RE, and ED, showing that these channels are mechanistically distinct.\n    \\item \\textbf{Pairwise confusability as a robust predictor.} We demonstrate that pairwise SCS predicts type confusion across tasks and embedding models, while identifying a centrality confound that invalidates per-type aggregation on homogeneous schemas.\n    \\item \\textbf{Cross-task controlled experiments.} We present BCS-controlled experiments with bootstrap confidence intervals on three datasets, establishing that confusability effects amplify $3.4\\times$ as schema size grows from 16 to 80 types.\n    \\item \\textbf{Informative negative result.} Our SDGD experiments identify merge amplification as a structural bottleneck for decompose-then-merge approaches, with direct implications for the design of schema decomposition methods.\n\\end{enumerate}\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_introduction_20260515T183015",
  "tool": "Write",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/introduction.tex",
    "content": "\\section{Introduction}\n\\label{sec:introduction}\n\nTraining-free LLM information extraction---prompting a large language model with a target schema and asking it to extract structured information without any task-specific fine-tuning---enables rapid deployment across new domains and ontologies. This zero-shot paradigm eliminates the need for labeled data, making it attractive for applications where annotation is expensive or schemas evolve frequently \\cite{llm4ie-survey-2024}. Yet the paradigm carries a critical limitation: performance degrades sharply as the number of candidate types in the prompt schema grows. On named entity recognition, recall drops from 0.72 with a single candidate type to 0.42 with 64 types, a 42\\% relative decline. On relation extraction, accuracy falls from 85.7\\% with one relation to 50.4\\% with 80 relations---near halving. This degradation is not academic: real-world ontologies routinely define 50--200+ types, placing them squarely in the regime where training-free extraction becomes unreliable.\n\nWhat causes this schema-induced degradation? Prior work has proposed decomposition strategies that implicitly assume different answers. \\citet{uniner-2024} extract each type independently, assuming types can be treated as separable. \\citet{llm-pee-2025} partition large event schemas by type embedding similarity before extraction, assuming that semantic overlap between co-presented types drives errors. \\citet{parse-2025} rewrite and optimize schema definitions, assuming that description quality is the bottleneck. Each approach improves extraction under certain conditions, but none isolates \\emph{why} schemas degrade performance in the first place. The closest work, LLM-PEE \\cite{llm-pee-2025}, reduces both the number of co-presented types and their inter-type similarity simultaneously, making it impossible to determine which factor---or what combination---accounts for the observed gains. More broadly, all prior approaches conflate two distinct mechanisms that could independently degrade extraction: having more types to discriminate among (count) and having semantically similar types to confuse (confusability). Without disentangling these factors, decomposition strategies cannot be principled: they optimize a black-box objective without understanding its components.\n\nWe ask three questions. \\textbf{RQ1}: Does type confusability independently predict extraction degradation beyond the effect of type count? \\textbf{RQ2}: Through what mechanisms do count and confusability each degrade performance? \\textbf{RQ3}: Can confusability-aware schema decomposition improve extraction quality?\n\nTo answer these questions, we conduct the first controlled empirical study that isolates type confusability from type count across three IE tasks: named entity recognition (NER), relation extraction (RE), and event detection (ED). We introduce the \\emph{Schema Confusability Score} (SCS), which quantifies pairwise semantic overlap between types using embedding cosine similarity, and its batch-level aggregation, the \\emph{Batch Confusability Score} (BCS). We design two complementary experimental paradigms: \\emph{count curves} that vary schema size while randomizing confusability, and \\emph{BCS-controlled experiments} that fix schema size while varying confusability. We evaluate on three datasets spanning diverse schema structures: Few-NERD \\cite{PLACEHOLDER_fewnerd} (66 entity types across 8 domains), FewRel \\cite{PLACEHOLDER_fewrel} (80 relation types), and MAVEN \\cite{PLACEHOLDER_maven} (168 event types from a single ontology). All experiments use Qwen3-32B in a zero-shot prompting setup with bootstrap confidence intervals.\n\nFive findings emerge from our experiments.\n\nFirst, schema-induced degradation operates through two orthogonal channels. \\textbf{Channel~1} (count $\\to$ recall decline): increasing the number of types in the prompt reduces recall for NER and RE, as more candidate types compete for the model's attention. \\textbf{Channel~2} (confusability $\\to$ type confusion): semantically similar types trigger intra-batch substitution errors (IntraSub), where the model assigns an entity or relation to a neighboring type in embedding space. These channels are mechanistically distinct---Channel~1 reflects capacity limitations, Channel~2 reflects semantic indistinguishability---and both contribute to the overall degradation pattern.\n\nSecond, pairwise SCS is a robust predictor of type confusion. Across Few-NERD (Pearson $r = 0.112$, $p < 10^{-12}$) and MAVEN ($r = 0.129$, $p < 10^{-10}$), embedding similarity between type pairs correlates with confusion rates, and this signal replicates across two unrelated embedding spaces (Qwen3 hidden states and MiniLM sentence embeddings). The effect is modest in magnitude: pairwise confusability explains roughly 1.3--1.7\\% of the variance in type confusion ($r^2 \\approx 0.013\\text{--}0.017$). Entity frequency, prompt position effects \\cite{lost-in-middle-2024}, and type definition quality jointly account for the remainder. Nevertheless, this is the first factor to be empirically isolated in controlled zero-shot IE experiments, and the signal survives bootstrap resampling with confidence intervals bounded well above zero.\n\nThird, confusability effects amplify with schema scale. In BCS-controlled FewRel experiments, switching from low-confusability to high-confusability type batches reduces accuracy by 9.1 percentage points at the 16-relation scale, but the gap widens to 31.2\\,pp at 80 relations (95\\% CI: [17.7, 42.7])---a $3.4\\times$ amplification. Larger type pools provide more opportunities for semantically similar types to co-occur, expanding the confusion space.\n\nFourth, per-type confusability aggregation is confounded on homogeneous schemas. On MAVEN, whose 168 event types all derive from the FrameNet ontology, the correlation between mean BCS and per-type error rate reverses sign ($\\rho = +0.189$, $p = 0.021$), opposite to the predicted direction. This centrality confound arises because, in single-cluster embedding spaces \\cite{cai-isotropy-clusters-2021}, a type's mean similarity conflates confusability with centrality---a property associated with well-represented types that LLMs extract reliably. The pairwise SCS signal remains intact ($r = 0.129$, CI: [0.104, 0.156]), confirming that the confound lies in the aggregation step, not in the underlying pairwise relationship. Few-NERD, whose types span multiple domains, does not exhibit this confound ($\\rho = -0.293$, $p = 0.02$).\n\nFifth, confusability-aware schema decomposition fails to improve extraction. Our Schema-DAG-Guided Decomposition (SDGD) successfully separates confusable types into different batches, yet every decomposition mode---including random batching and per-type extraction---produces lower F1 than single-pass extraction (best decomposition F1 = 0.320 vs.\\ single-pass F1 = 0.445). The bottleneck is \\emph{merge amplification}: when the same text is processed across multiple extraction passes, the union merge step accumulates contradictory predictions, destroying precision. This structural limitation applies to any decompose-then-merge pipeline, including the partitioning approach of \\citet{llm-pee-2025}.\n\nOur contributions are:\n\\begin{enumerate}[leftmargin=*,itemsep=2pt,topsep=2pt]\n    \\item \\textbf{Multi-channel degradation model.} We provide the first empirical decomposition of schema-induced degradation into count and confusability channels across NER, RE, and ED, showing that these channels are mechanistically distinct.\n    \\item \\textbf{Pairwise confusability as a robust predictor.} We demonstrate that pairwise SCS predicts type confusion across tasks and embedding models, while identifying a centrality confound that invalidates per-type aggregation on homogeneous schemas.\n    \\item \\textbf{Cross-task controlled experiments.} We present BCS-controlled experiments with bootstrap confidence intervals on three datasets, establishing that confusability effects amplify $3.4\\times$ as schema size grows from 16 to 80 types.\n    \\item \\textbf{Informative negative result.} Our SDGD experiments identify merge amplification as a structural bottleneck for decompose-then-merge approaches, with direct implications for the design of schema decomposition methods.\n\\end{enumerate}\n"
  }
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-15T18:31:43.499237+00:00_

File created successfully at: /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/introduction.tex

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_introduction_20260515T183015",
  "tool": "Write",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 15 · 2026-05-15T18:31:43.499399+00:00_

已写入 `introduction.tex`。约 1200 words，覆盖全部 5 个 outline 段落。关键处理：

- **Effect size 诚实**：r²≈1.3-1.7% 在 Finding 2 中 upfront 标注为 "modest in magnitude"，随后 argue "first factor empirically isolated" + bootstrap CI bounded above zero
- **MAVEN 反向趋势**：Hook 段和 Finding 1 中 count degradation 限定为 "NER and RE"，未 claim universal
- **所有数字**与 results.tex 精确一致（0.72→0.42, 85.7%→50.4%, r=0.112/0.129, 9.1pp→31.2pp, 3.4×, F1=0.445 vs 0.320）
- **引用**全部使用 references.bib 中已有的 key

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_paper_writing_introduction_20260515T183015"
}
```

</details>

---
