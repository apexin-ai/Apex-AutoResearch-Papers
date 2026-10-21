# paper reference augmentation

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 129
- **Recorded user turns:** 0
- **Tool calls:** 64
- **Original source:** `logs/chats/worker_paper_reference-augmentation_20260524T192339.jsonl`
- **Structured JSON:** [`5c120f18aac549d1411b.json`](../../sessions/5c/5c120f18aac549d1411b.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

129 recorded events

### Tool call

_source line 1 · 2026-05-24T19:35:53.970169+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/references.bib"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_reference-augmentation_20260524T192339",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/references.bib"
  }
}
```

</details>

---

### Tool result

_source line 2 · 2026-05-24T19:35:53.970628+00:00_

1	@inproceedings{autore2024,
2	  title     = {{AutoRE}: Document-Level Relation Extraction with Large Language Models},
3	  author    = {Xue, Lilong and Zhang, Dan and Dong, Yuxiao and Tang, Jie},
4	  booktitle = {Proceedings of the 62nd Annual Meeting of the Association for Computational Linguistics: System Demonstrations},
5	  year      = {2024},
6	  url       = {https://arxiv.org/abs/2403.14888}
7	}
8	
9	@inproceedings{chen2025docksrag,
10	  title     = {{DocKS-RAG}: Optimizing Document-Level Relation Extraction through {LLM}-Enhanced Hybrid Prompt Tuning},
11	  author    = {Xu, Xiaolong and Zhou, Yibo and Xiang, Haolong and Li, Xiaoyong and Zhang, Xuyun and Qi, Lianyong and Dou, Wanchun},
12	  booktitle = {Proceedings of the 42nd International Conference on Machine Learning},
13	  year      = {2025},
14	  url       = {https://proceedings.mlr.press/v267/xu25am.html}
15	}
16	
17	@article{dai2025r1re,
18	  title   = {{R1-RE}: Cross-Domain Relation Extraction with {RLVR}},
19	  author  = {Dai, Runpeng and Zheng, Tong and Yang, Run and Yu, Kaixian and Zhu, Hongtu},
20	  journal = {arXiv preprint arXiv:2507.04642},
21	  year    = {2025},
22	  url     = {https://arxiv.org/abs/2507.04642}
23	}
24	
25	@inproceedings{gao2023scaling,
26	  title     = {Scaling Laws for Reward Model Overoptimization},
27	  author    = {Gao, Leo and Schulman, John and Hilton, Jacob},
28	  booktitle = {Proceedings of the 40th International Conference on Machine Learning},
29	  year      = {2023},
30	  url       = {https://arxiv.org/abs/2210.10760}
31	}
32	
33	@inproceedings{hu2022lora,
34	  title     = {{LoRA}: Low-Rank Adaptation of Large Language Models},
35	  author    = {Hu, Edward J. and Shen, Yelong and Wallis, Phillip and Allen-Zhu, Zeyuan and Li, Yuanzhi and Wang, Shean and Wang, Lu and Chen, Weizhu},
36	  booktitle = {International Conference on Learning Representations},
37	  year      = {2022},
38	  url       = {https://arxiv.org/abs/2106.09685}
39	}
40	
41	@article{li2026qurl,
42	 
…[truncated 13268 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_reference-augmentation_20260524T192339",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-24T19:35:53.970835+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/sections/related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_reference-augmentation_20260524T192339",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/sections/related_work.tex"
  }
}
```

</details>

---

### Tool result

_source line 4 · 2026-05-24T19:35:53.971016+00:00_

1	\section{Related Work}
2	\label{sec:related_work}
3	
4	Document-level relation extraction (DocRE) requires reasoning across sentence boundaries to identify relations between entity pairs.
5	DocRED \citep{yao2019docred} established the first large-scale benchmark for this task, catalyzing a line of encoder-based methods that treat DocRE as classification over entity pair representations.
6	ATLOP \citep{zhou2021atlop} introduced adaptive thresholding for multi-label prediction and localized context pooling for entity representations.
7	A parallel thread incorporates sentence-level evidence into these architectures.
8	SAIS \citep{xiao2022sais} introduced evidence supervision as an auxiliary training signal and showed that joint evidence prediction improves extraction through data augmentation and ensemble inference.
9	DREEAM \citep{ma2023dreeam} extended this approach with dynamic memory-based evidence retrieval that guides attention to supporting sentences.
10	EIDER \citep{xie2022eider} jointly trains an evidence extractor and fuses evidence representations into the relation classifier.
11	In all three systems, evidence identification is binary sentence classification over a fixed candidate set, a formulation that adds no output complexity.
12	Recent work has recast DocRE for large language models.
13	AutoRE \citep{autore2024} fine-tunes LLMs with QLoRA using a relation-head-facts decomposition; \citet{xu2024lmrc} frame extraction as multi-choice reading comprehension; RelPrior \citep{wang2025relprior} uses relation priors to guide LLM-based extraction; GLiDRE \citep{zhang2025glidre} presents a generalist lightweight approach; Ru-LLM \citep{wang2025rullm} incorporates logical rule constraints; and \citet{chen2025docksrag} combine retrieval-augmented generation with structured knowledge.
14	These methods match or surpass encoder baselines but produce bare triplets without evidence. Among LLM-based generative methods at the 8B scale, our RSFT model (54.33 Ign-F1 on Do
…[truncated 3254 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_reference-augmentation_20260524T192339",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-24T19:35:53.971178+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/sections/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_reference-augmentation_20260524T192339",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/sections/introduction.tex"
  }
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-24T19:35:53.971360+00:00_

1	\section{Introduction}
2	
3	Document-level relation extraction (DocRE) requires identifying semantic relations between entity pairs across multiple sentences, a task where encoder-based methods such as \citet{zhou2021atlop} long dominated.
4	Recent LLM-based approaches have closed this gap: \citet{autore2024} fine-tune LLMs with structured decomposition, \citet{xu2024lmrc} frame it as multi-choice reading comprehension, and \citet{chen2025docksrag} combine retrieval-augmented generation with structured knowledge.
5	These methods approach or surpass encoder baselines on DocRED \citep{yao2019docred} and Re-DocRED \citep{tan2022redocred} in extraction accuracy, yet every one outputs bare relation triplets $(e_h, r, e_t)$ without indicating \emph{which sentences} support each prediction.
6	In deployment contexts---clinical knowledge bases, legal due-diligence pipelines, financial compliance systems---users cannot verify a prediction without manually locating its textual basis across a multi-page document.
7	
8	Encoder-based methods have partially addressed this need: \citet{xiao2022sais} introduce sentence-level evidence supervision as an auxiliary signal, and \citet{ma2023dreeam} extend this with dynamic evidence retrieval through memory attention.
9	Both produce evidence and improve extraction, but encoder methods now trail LLM-based approaches in accuracy.
10	The community faces a gap: the most accurate extractors provide no evidence, while evidence-capable methods are no longer competitive.
11	
12	This gap reflects a structural difference.
13	In encoder methods, evidence retrieval is classification that regularizes the encoder at negligible cost; in LLM-based DocRE, evidence requires the model to \emph{generate} additional output tokens per triple, increasing output length and decoding complexity.
14	The na\"{i}ve expectation is that this generation cost always harms extraction accuracy.
15	Our experiments show this expectation is wrong.
16	The evidence tax is not
…[truncated 2159 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_reference-augmentation_20260524T192339",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-24T19:35:53.971507+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/sections/method.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_reference-augmentation_20260524T192339",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/sections/method.tex"
  }
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-24T19:35:53.971686+00:00_

1	\section{Method}
2	\label{sec:method}
3	
4	\begin{figure*}[t]
5	\centering
6	\includegraphics[width=0.92\textwidth]{fig_overview.pdf}
7	\vspace{-2mm}
8	\caption{Overview of our approach. (Top) Standard DocRE outputs bare triples; evidence-grounded DocRE additionally generates supporting sentence indices for each prediction. (Bottom) RSFT pipeline: the SFT model samples $N$ candidate responses per document, scores them with CED/NLI, selects the top-$k$, and fine-tunes on the filtered set.}
9	\label{fig:overview}
10	\end{figure*}
11	
12	\subsection{Task: Evidence-Grounded Document-Level Relation Extraction}
13	\label{sec:task}
14	
15	Given a document $D = \{s_1, \ldots, s_n\}$ consisting of $n$ sentences and a set of entities $\mathcal{E}$ identified within $D$, the task of evidence-grounded document-level relation extraction (DocRE) requires predicting, for each entity pair $(e_h, e_t) \in \mathcal{E} \times \mathcal{E}$, a relation $r \in \mathcal{R} \cup \{\texttt{NA}\}$ together with a set of supporting evidence sentences $E \subseteq D$. Standard DocRE predicts only the triple $(e_h, r, e_t)$; the evidence-grounded formulation also requires $E$, which grounds each prediction in specific textual support (Figure~\ref{fig:overview}).
16	
17	In our LLM-based approach, the model generates structured outputs that jointly encode both components. For each predicted relation, the output follows the format \texttt{(head, relation, tail) | Evidence: [S$i$][S$j$]}, requiring the model to produce complete evidence references inline with each triple rather than as a separate retrieval step. This design contrasts with encoder-based evidence methods such as SAIS~\citep{xiao2022sais} and DREEAM~\citep{ma2023dreeam}, which frame evidence identification as sentence-level binary classification. Because classification over a fixed sentence set does not increase output length, these methods incur no generation overhead. Our LLM formulation requires additional tokens for each evidenc
…[truncated 9178 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_reference-augmentation_20260524T192339",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-24T19:35:53.971891+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:WebSearch,WebFetch",
  "max_results": "2"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_reference-augmentation_20260524T192339",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:WebSearch,WebFetch",
    "max_results": "2"
  }
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-24T19:35:53.972022+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_reference-augmentation_20260524T192339",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-24T19:35:53.972168+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "document-level relation extraction 2026 arXiv"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_reference-augmentation_20260524T192339",
  "tool": "WebSearch",
  "tool_args": {
    "query": "document-level relation extraction 2026 arXiv"
  }
}
```

</details>

---

### Tool call

_source line 12 · 2026-05-24T19:35:53.972308+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "GRPO reinforcement learning LLM 2026 arXiv"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_reference-augmentation_20260524T192339",
  "tool": "WebSearch",
  "tool_args": {
    "query": "GRPO reinforcement learning LLM 2026 arXiv"
  }
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-24T19:35:53.972425+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "evidence grounding faithfulness LLM 2026 arXiv"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_reference-augmentation_20260524T192339",
  "tool": "WebSearch",
  "tool_args": {
    "query": "evidence grounding faithfulness LLM 2026 arXiv"
  }
}
```

</details>

---

### Tool call

_source line 14 · 2026-05-24T19:35:53.972537+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "rejection sampling fine-tuning LLM 2026 arXiv"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_reference-augmentation_20260524T192339",
  "tool": "WebSearch",
  "tool_args": {
    "query": "rejection sampling fine-tuning LLM 2026 arXiv"
  }
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-24T19:35:53.972648+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "QLoRA Dettmers 2023 efficient finetuning quantized language models"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_reference-augmentation_20260524T192339",
  "tool": "WebSearch",
  "tool_args": {
    "query": "QLoRA Dettmers 2023 efficient finetuning quantized language models"
  }
}
```

</details>

---

### Tool call

_source line 16 · 2026-05-24T19:35:53.972758+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "KTO Ethayarajh 2024 model alignment prospect theoretic"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_reference-augmentation_20260524T192339",
  "tool": "WebSearch",
  "tool_args": {
    "query": "KTO Ethayarajh 2024 model alignment prospect theoretic"
  }
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-24T19:35:53.972878+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "GAIN graph aggregation inference network document relation extraction Zeng 2020"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_reference-augmentation_20260524T192339",
  "tool": "WebSearch",
  "tool_args": {
    "query": "GAIN graph aggregation inference network document relation extraction Zeng 2020"
  }
}
```

</details>

---

### Tool call

_source line 18 · 2026-05-24T19:35:53.972996+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Hoffmann 2022 training compute-optimal large language models Chinchilla scaling"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_reference-augmentation_20260524T192339",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Hoffmann 2022 training compute-optimal large language models Chinchilla scaling"
  }
}
```

</details>

---

### Tool result

_source line 19 · 2026-05-24T19:35:53.973146+00:00_

Web search results for query: "document-level relation extraction 2026 arXiv"

Links: [{"title":"[2602.04320] A Domain-Specific Curated Benchmark for Entity and Document-Level Relation Extraction","url":"https://arxiv.org/abs/2602.04320"},{"title":"Document-level joint entity and relation extraction based on multi-task explicit interaction | Journal of King Saud University Computer and Information Sciences | Springer Nature Link","url":"https://link.springer.com/article/10.1007/s44443-026-00624-7"},{"title":"[2201.04826] Document-level Relation Extraction with Context Guided Mention Integration and Inter-pair Reasoning","url":"https://arxiv.org/abs/2201.04826"},{"title":"A Masked Image Reconstruction Network for Document-level Relation   Extraction","url":"https://arxiv.org/pdf/2204.09851"},{"title":"Enhanced Heterogeneous Graph Attention Network with a Novel Multilabel Focal Loss for Document-Level Relation Extraction","url":"https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10969296/"},{"title":"CLEF HIPE-2026: Evaluating Accurate and Efficient Person–Place Relation Extraction from Multilingual Historical Texts","url":"https://arxiv.org/html/2602.17663"},{"title":"Towards Better Document-level Relation Extraction via Iterative   Inference","url":"https://arxiv.org/pdf/2211.14470"},{"title":"Document-level Relation Extraction as Semantic Segmentation","url":"https://arxiv.org/pdf/2106.03618"}]

I found several relevant results for document-level relation extraction research. Here are the key findings:

## Recent 2026 arXiv Papers

A paper submitted on February 4, 2026 titled "A Domain-Specific Curated Benchmark for Entity and Document-Level Relation Extraction" addresses how Information Extraction, encompassing Named Entity Recognition, Named Entity Linking, and Relation Extraction, is critical for transforming scientific publications into structured knowledge.

The HIPE-2026 campaign builds on previous initiatives and extends toward semantic relation extraction by targ
…[truncated 1003 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_reference-augmentation_20260524T192339",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-24T19:35:53.973342+00:00_

Web search results for query: "QLoRA Dettmers 2023 efficient finetuning quantized language models"

Links: [{"title":"GitHub - artidoro/qlora: QLoRA: Efficient Finetuning of Quantized LLMs · GitHub","url":"https://github.com/artidoro/qlora"},{"title":"Paper page - QLoRA: Efficient Finetuning of Quantized LLMs","url":"https://huggingface.co/papers/2305.14314"},{"title":"[PDF] QLoRA: Efficient Finetuning of Quantized LLMs | Semantic Scholar","url":"https://www.semanticscholar.org/paper/QLoRA:-Efficient-Finetuning-of-Quantized-LLMs-Dettmers-Pagnoni/32ac52069e562d4f900afee70bdca63f53461481"},{"title":"QLoRA: Efficient Finetuning of Quantized LLMs","url":"https://proceedings.neurips.cc/paper_files/paper/2023/hash/1feb87871436031bdc0f2beaa62a049b-Abstract-Conference.html"},{"title":"QLoRA: Efficient Fine-Tuning of Quantized Language Models - Interactive | Michael Brenndoerfer | Michael Brenndoerfer","url":"https://mbrenndoerfer.com/writing/qlora-efficient-finetuning-quantized-language-models"},{"title":"[2305.14314] QLoRA: Efficient Finetuning of Quantized LLMs","url":"https://arxiv.org/abs/2305.14314"},{"title":"QLoRA: Efficient Finetuning of Quantized LLMs","url":"https://arxiv.org/pdf/2305.14314"},{"title":"QLoRA: Efficient Finetuning of Quantized LLMs | OpenReview","url":"https://openreview.net/forum?id=OUIFPHEgJU"},{"title":"QLORA: efficient finetuning of quantized LLMs","url":"https://dl.acm.org/doi/10.5555/3666122.3666563"},{"title":"LQ-LoRA: Low-rank Plus Quantized Matrix Decomposition for Efficient   Language Model Finetuning","url":"https://arxiv.org/pdf/2311.12023"}]

Based on the search results, here's information about QLoRA and the Dettmers 2023 paper:

## Overview

QLoRA enables efficient finetuning of large language models using 4-bit quantization and Low Rank Adapters. The paper was published by Tim Dettmers, Artidoro Pagnoni, Ari Holtzman, and Luke Zettlemoyer in 2023.

## Key Innovation

QLoRA is an efficient finetuning approach that reduces memory usag
…[truncated 962 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_reference-augmentation_20260524T192339",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 21 · 2026-05-24T19:35:53.973523+00:00_

Web search results for query: "evidence grounding faithfulness LLM 2026 arXiv"

Links: [{"title":"[2603.19532] EvidenceRL: Reinforcing Evidence Consistency for Trustworthy Language Models","url":"https://arxiv.org/abs/2603.19532"},{"title":"GSAR: Typed Grounding for Hallucination Detection and Recovery in Multi-Agent LLMs","url":"https://arxiv.org/html/2604.23366v1"},{"title":"EvidenceRL: Reinforcing Evidence Consistency for Trustworthy Language Models","url":"https://arxiv.org/html/2603.19532"},{"title":"Breaking the Chain: A Causal Analysis of LLM Faithfulness to Intermediate Structures","url":"https://arxiv.org/html/2603.16475v1"},{"title":"[2603.09988] Causally Grounded Mechanistic Interpretability for LLMs with Faithful Natural-Language Explanations","url":"https://arxiv.org/abs/2603.09988"},{"title":"PaperTrail: A Claim-Evidence Interface for Grounding Provenance in LLM-based Scholarly Q&A","url":"https://arxiv.org/html/2602.21045v1"},{"title":"Yale-DM-Lab at ArchEHR-QA 2026: Deterministic Grounding and Multi-Pass Evidence Alignment for EHR Question Answering","url":"https://arxiv.org/html/2604.07116"},{"title":"EvidenceRL: Reinforcing Evidence Consistency for Trustworthy Language Models","url":"https://arxiv.org/pdf/2603.19532"}]

I found several relevant 2026 arXiv papers on evidence grounding and faithfulness in Large Language Models. Here are the key results:

## Recent Papers on Evidence Grounding and Faithfulness (2026)

**EvidenceRL: Reinforcing Evidence Consistency for Trustworthy Language Models**
EvidenceRL scores candidate responses for grounding (entailment with retrieved evidence and context) and correctness (agreement with reference answers) and optimizes the generator using Group Relative Policy Optimization (GRPO). The method consistently improves evidence grounding and faithfulness across high-stakes domains like cardiac diagnosis and legal reasoning without sacrificing task accuracy. On legal reasoning, EvidenceRL raises Faithfulness from 32.
…[truncated 1161 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_reference-augmentation_20260524T192339",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 22 · 2026-05-24T19:35:53.973688+00:00_

Web search results for query: "rejection sampling fine-tuning LLM 2026 arXiv"

Links: [{"title":"Rejection Sampling & SFT in LLM Alignment","url":"https://www.emergentmind.com/topics/rejection-sampling-and-supervised-fine-tuning-sft"},{"title":"[2601.09253] RIFT: Repurposing Negative Samples via Reward-Informed Fine-Tuning","url":"https://arxiv.org/abs/2601.09253"},{"title":"Rejection Sampling | RLHF Book by Nathan Lambert","url":"https://rlhfbook.com/c/09-rejection-sampling"},{"title":"[2504.13145v1] Exploring Expert Failures Improves LLM Agent Tuning","url":"http://arxiv.org/abs/2504.13145v1"},{"title":"[2504.11343] A Minimalist Approach to LLM Reasoning: from Rejection Sampling to Reinforce","url":"https://arxiv.org/abs/2504.11343"},{"title":"[2308.01825] Scaling Relationship on Learning Mathematical Reasoning with Large Language Models","url":"https://arxiv.org/abs/2308.01825"},{"title":"Rejection Sampling Based Fine Tuning Secretly Performs PPO | OpenReview","url":"https://openreview.net/forum?id=yQ2UivKlir"},{"title":"Beyond Rejection Sampling: Trajectory Fusion for Scaling Mathematical Reasoning","url":"https://arxiv.org/pdf/2602.04391"},{"title":"arXiv:2308.01825v1 [cs.CL] 3 Aug 2023","url":"https://arxiv.org/pdf/2308.01825"},{"title":"A Minimalist Approach to LLM Reasoning: from Rejection Sampling to Reinforce","url":"https://arxiv.org/html/2504.11343v1"}]

Based on the search results, here are some recent 2026 arXiv papers and resources related to rejection sampling and LLM fine-tuning:

## Key Recent Papers (2026)

A notable recent paper is "RIFT: Repurposing Negative Samples via Reward-Informed Fine-Tuning" (submitted January 14, 2026), which proposes a framework that utilizes all self-generated samples to address data inefficiency in standard fine-tuning approaches that discard valuable negative samples. Unlike rejection sampling fine-tuning (RFT), RIFT repurposes negative trajectories by reweighting the loss with scalar rewards to learn from both posit
…[truncated 916 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_reference-augmentation_20260524T192339",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 23 · 2026-05-24T19:35:53.973860+00:00_

Web search results for query: "KTO Ethayarajh 2024 model alignment prospect theoretic"

Links: [{"title":"Paper Summary: KTO: Model Alignment as Prospect Theoretic Optimization","url":"https://queirozf.com/entries/paper-summary-kto-model-alignment-as-prospect-theoretic-optimization"},{"title":"[2402.01306] KTO: Model Alignment as Prospect Theoretic Optimization","url":"https://arxiv.org/abs/2402.01306"},{"title":"Model Alignment as Prospect Theoretic Optimization","url":"https://proceedings.mlr.press/v235/ethayarajh24a.html"},{"title":"[Paper Note] KTO: Model Alignment as Prospect Theoretic Optimization, Kawin Ethayarajh+, ICML'24, 2024.02 · Issue #1472 · AkihikoWatanabe/paper_notes","url":"https://github.com/AkihikoWatanabe/paper_notes/issues/1472"},{"title":"Paper page - KTO: Model Alignment as Prospect Theoretic Optimization","url":"https://huggingface.co/papers/2402.01306"},{"title":"[PDF] KTO: Model Alignment as Prospect Theoretic Optimization | Semantic Scholar","url":"https://www.semanticscholar.org/paper/KTO:-Model-Alignment-as-Prospect-Theoretic-Ethayarajh-Xu/c0d8e5ee66c279299012cc3b8d0519011b3f4998"},{"title":"KTO: Model Alignment as Prospect Theoretic Optimization","url":"https://arxiv.org/pdf/2402.01306"},{"title":"KTO: Model Alignment as Prospect Theoretic Optimization","url":"https://winniexu.ca/research/kto"},{"title":"KTO: Model Alignment as Prospect Theoretic Optimization","url":"https://cs294-43-fall2024.pages.dev/assets/presentations/kto.pdf"}]

Based on the search results, here's what I found about the KTO paper by Ethayarajh et al. (2024):

## Overview

The 2024 article "KTO: Model Alignment as Prospect Theoretic Optimization" is by Ethayarajh et al. KTO matches or exceeds the performance of preference-based methods at scales from 1B to 30B, despite only learning from a binary signal of whether an output is desirable.

## Key Concept

The authors develop a framework with HALOs (Human-Aware Losses), which add insights from Prospect Theory to loss
…[truncated 835 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_reference-augmentation_20260524T192339",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 24 · 2026-05-24T19:35:53.974034+00:00_

Web search results for query: "GAIN graph aggregation inference network document relation extraction Zeng 2020"

Links: [{"title":"(PDF) Double Graph Based Reasoning for Document-level Relation Extraction","url":"https://www.researchgate.net/publication/344422532_Double_Graph_Based_Reasoning_for_Document-level_Relation_Extraction"},{"title":"GitHub - DreamInvoker/GAIN: Source code for EMNLP 2020 paper: Double Graph Based Reasoning for Document-level Relation Extraction","url":"https://github.com/DreamInvoker/GAIN"},{"title":"Enhancing cross-evidence reasoning graph for document-level relation extraction - PMC","url":"https://pmc.ncbi.nlm.nih.gov/articles/PMC11232587/"},{"title":"[2009.13752] Double Graph Based Reasoning for Document-level Relation Extraction","url":"https://arxiv.org/abs/2009.13752"},{"title":"Double Graph Based Reasoning for Document-level Relation Extraction - ACL Anthology","url":"https://aclanthology.org/2020.emnlp-main.127/"},{"title":"Knowledge enhanced graph inference network based entity-relation extraction and knowledge graph construction for industrial domain","url":"https://journal.hep.com.cn/fem/EN/10.1007/s42524-023-0273-1"},{"title":"Graph-Augmented Relation Extraction Model with LLMs-Generated Support Document","url":"https://arxiv.org/html/2410.23452"},{"title":"Dependency-augmented graph aggregation networks for document-level relation extraction with cross-sentence semantics | Journal of King Saud University Computer and Information Sciences | Springer Nature Link","url":"https://link.springer.com/article/10.1007/s44443-025-00035-0"},{"title":"Mention-centered Graph Neural Network for Document-level Relation   Extraction","url":"https://arxiv.org/pdf/2103.08200"}]

Based on the search results, I found comprehensive information about GAIN (Graph Aggregation-and-Inference Network) by Zeng et al. 2020:

## Overview

Document-level relation extraction aims to extract relations among entities within a document. Different from sentence-l
…[truncated 1067 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_reference-augmentation_20260524T192339",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 25 · 2026-05-24T19:35:53.974214+00:00_

Web search results for query: "Hoffmann 2022 training compute-optimal large language models Chinchilla scaling"

Links: [{"title":"Chinchilla Scaling Laws: Compute-Optimal Training and Resource Allocation for Large Language Models - Interactive | Michael Brenndoerfer | Michael Brenndoerfer","url":"https://mbrenndoerfer.com/writing/chinchilla-scaling-laws-compute-optimal-training-resource-allocation"},{"title":"[PDF] Training Compute-Optimal Large Language Models | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Training-Compute-Optimal-Large-Language-Models-Hoffmann-Borgeaud/8342b592fe238f3d230e4959b06fd10153c45db1"},{"title":"Training Compute-Optimal Large Language Models","url":"https://www.researchgate.net/publication/359576828_Training_Compute-Optimal_Large_Language_Models"},{"title":"Evaluating the Robustness of Chinchilla Compute-Optimal Scaling","url":"https://arxiv.org/pdf/2509.23963"},{"title":"Training Compute-Optimal Large Language Models Jordan Hoffmann∗","url":"https://proceedings.neurips.cc/paper_files/paper/2022/file/c1e2faff6f588870935f114ebe04a3e5-Paper-Conference.pdf"},{"title":"[2203.15556] Training Compute-Optimal Large Language Models","url":"https://arxiv.org/abs/2203.15556"},{"title":"Training Compute-Optimal Large Language Models By Anika Maskara and Simon Park","url":"https://www.cs.princeton.edu/courses/archive/fall22/cos597G/lectures/lec12.pdf"},{"title":"Training Compute-Optimal Large Language Models","url":"https://arxiv.org/pdf/2203.15556"}]

I found the search results for the Hoffmann 2022 paper on training compute-optimal large language models. Here are the key findings:

## Overview

In 2022, a team of researchers at DeepMind led by Jordan Hoffmann published findings that fundamentally challenged the prevailing assumptions about how large language models should be trained.

## Key Finding: Compute-Optimal Scaling

By training over 400 language models ranging from 70 million to over 16 billion parameters on 5 to 500 bil
…[truncated 1073 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_reference-augmentation_20260524T192339",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 26 · 2026-05-24T19:35:53.974420+00:00_

Web search results for query: "GRPO reinforcement learning LLM 2026 arXiv"

Links: [{"title":"[2605.17570] How Off-Policy Can GRPO Be? Mu-GRPO for Efficient LLM Reinforcement Learning","url":"https://arxiv.org/abs/2605.17570"},{"title":"How Off-Policy Can GRPO Be? 𝝁-GRPO for Efficient LLM Reinforcement Learning","url":"https://arxiv.org/html/2605.17570"},{"title":"GitHub - AMAP-ML/Tree-GRPO: [ICLR 2026] Tree Search for LLM Agent Reinforcement Learning · GitHub","url":"https://github.com/AMAP-ML/Tree-GRPO"},{"title":"Can GRPO Help LLMs Transcend Their Pretraining Origin?","url":"https://arxiv.org/pdf/2510.15990"},{"title":"Reinforcement Learning with Verifiable Rewards: GRPO's Effective Loss, Dynamics, and Success Amplification","url":"https://arxiv.org/pdf/2503.06639"},{"title":"Prompt replay: speeding up grpo with on-policy reuse of high-signal prompts","url":"https://arxiv.org/pdf/2603.21177"},{"title":"CoRPO: Adding a Correctness Bias to GRPO Improves Generalization","url":"https://arxiv.org/pdf/2511.04439"}]

Based on the search results, here are some recent 2026 arXiv papers on GRPO (Group Relative Policy Optimization) for reinforcement learning with large language models:

## Key 2026 GRPO Papers:

**1. Mu-GRPO for Efficient LLM Reinforcement Learning**
Group Relative Policy Optimization (GRPO) has been a key driver of recent progress in reinforcement learning with verifiable rewards (RLVR) for large language models, but it is typically trained in a low-staleness, near-on-policy regime that incurs substantial system overhead. The paper proposes Mu-GRPO, an RL training framework that organizes training into a small number (e.g., four) of large sequential generation-optimization stages. Mu-GRPO matches or exceeds the performance of standard GRPO while achieving around 2x speedup in wall-clock training time.

**2. Tree-GRPO for LLM Agent RL**
Tree-GRPO adopts a tree-search rollout strategy in place of independent chain-based rollouts for LLM agent RL, carrying ou
…[truncated 653 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_reference-augmentation_20260524T192339",
  "tool": "WebSearch",
  "elapsed_ms": 2
}
```

</details>

---

### Tool call

_source line 27 · 2026-05-24T19:35:53.974609+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Ouyang 2022 \"Training language models to follow instructions\" InstructGPT NeurIPS"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_reference-augmentation_20260524T192339",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Ouyang 2022 \"Training language models to follow instructions\" InstructGPT NeurIPS"
  }
}
```

</details>

---

### Tool call

_source line 28 · 2026-05-24T19:35:53.974734+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Schulman 2017 \"Proximal Policy Optimization Algorithms\" PPO arXiv"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_reference-augmentation_20260524T192339",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Schulman 2017 \"Proximal Policy Optimization Algorithms\" PPO arXiv"
  }
}
```

</details>

---

### Tool call

_source line 29 · 2026-05-24T19:35:53.974850+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "He DeBERTa-v3 2021 \"DeBERTaV3 Improving DeBERTa using ELECTRA-Style\" arXiv"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_reference-augmentation_20260524T192339",
  "tool": "WebSearch",
  "tool_args": {
    "query": "He DeBERTa-v3 2021 \"DeBERTaV3 Improving DeBERTa using ELECTRA-Style\" arXiv"
  }
}
```

</details>

---

### Tool call

_source line 30 · 2026-05-24T19:35:53.974962+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "NLI natural language inference information extraction 2026 arXiv"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_reference-augmentation_20260524T192339",
  "tool": "WebSearch",
  "tool_args": {
    "query": "NLI natural language inference information extraction 2026 arXiv"
  }
}
```

</details>

---

### Tool call

_source line 31 · 2026-05-24T19:35:53.975071+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "scaling law LLM fine-tuning 2026 arXiv"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_reference-augmentation_20260524T192339",
  "tool": "WebSearch",
  "tool_args": {
    "query": "scaling law LLM fine-tuning 2026 arXiv"
  }
}
```

</details>

---

### Tool call

_source line 32 · 2026-05-24T19:35:53.975182+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Tree-GRPO ICLR 2026 tree search LLM agent reinforcement learning"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_reference-augmentation_20260524T192339",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Tree-GRPO ICLR 2026 tree search LLM agent reinforcement learning"
  }
}
```

</details>

---

### Tool result

_source line 33 · 2026-05-24T19:35:53.975341+00:00_

Web search results for query: "Schulman 2017 "Proximal Policy Optimization Algorithms" PPO arXiv"

Links: [{"title":"Proximal Policy Optimization Algorithms","url":"https://www.summarizepaper.com/en/arxiv-id/1707.06347v2/"},{"title":"Paper page - Proximal Policy Optimization Algorithms","url":"https://huggingface.co/papers/1707.06347"},{"title":"Proximal Policy Optimization Algorithms | Request PDF","url":"https://www.researchgate.net/publication/318584439_Proximal_Policy_Optimization_Algorithms"},{"title":"[1707.06347] Proximal Policy Optimization Algorithms","url":"https://arxiv.org/abs/1707.06347"},{"title":"16. (Schulman 2017 arxiv) Proximal Policy Optimization Algorithms | JG_blog","url":"https://leejungi.github.io/posts/PPO/"},{"title":"[PDF] Proximal Policy Optimization Algorithms | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Proximal-Policy-Optimization-Algorithms-Schulman-Wolski/dce6f9d4017b1785979e7520fd0834ef8cf02f4b"},{"title":"(Open Access) Proximal Policy Optimization Algorithms (2017) | John Schulman | 17846 Citations","url":"https://scispace.com/papers/proximal-policy-optimization-algorithms-4doda01ow2"},{"title":"Proximal Policy Optimization Algorithms | by Eleventh Hour Enthusiast | Medium","url":"https://medium.com/@EleventhHourEnthusiast/proximal-policy-optimization-algorithms-8b8e6596c713"},{"title":"Proximal Policy Optimization Algorithms","url":"https://arxiv.org/pdf/1707.06347"},{"title":"Preprint. Under Review. BEYOND THE BOUNDARIES OF PROXIMAL POLICY OPTIMIZATION","url":"https://arxiv.org/pdf/2411.00666"}]

Here are the search results for the Schulman 2017 paper on Proximal Policy Optimization Algorithms:

## Paper Details

The paper was published on July 20, 2017, with authors John Schulman, Filip Wolski, Prafulla Dhariwal, Alec Radford, and Oleg Klimov. The arXiv identifier is **1707.06347**.

## Overview

The paper proposes a new family of policy gradient methods for reinforcement learning that alternate between sampli
…[truncated 1057 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_reference-augmentation_20260524T192339",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 34 · 2026-05-24T19:35:53.975525+00:00_

Web search results for query: "Ouyang 2022 "Training language models to follow instructions" InstructGPT NeurIPS"

Links: [{"title":"[Quick Review] Training language models to follow instructions with human feedback","url":"https://liner.com/review/training-language-models-to-follow-instructions-with-human-feedback"},{"title":"A Review of Ouyang et al.’s 2022 Paper aka “InstructGPT” | Educational Technology and Change Journal","url":"https://etcjournal.com/2025/07/29/a-review-of-ouyang-et-al-s-2022-paper-aka-instructgpt/"},{"title":"Training language models to follow instructions with human feedback, Long Ouyang+, N/A, NeurIPS'22 · Issue #1296 · AkihikoWatanabe/paper_notes","url":"https://github.com/AkihikoWatanabe/paper_notes/issues/1296"},{"title":"Training language models to follow instructions with human feedback","url":"https://proceedings.neurips.cc/paper_files/paper/2022/hash/b1efde53be364a73914f58805a001731-Abstract-Conference.html"},{"title":"[2203.02155] Training language models to follow instructions with human feedback","url":"https://arxiv.org/abs/2203.02155"},{"title":"Training Language Models to Follow Instructions with Human Feedback: A Comprehensive Review | by ALEENA TREESA LEEJOY | Medium","url":"https://medium.com/@aleenatleejoy/training-language-models-to-follow-instructions-with-human-feedback-a-comprehensive-review-267a30344028"},{"title":"[PDF] Training language models to follow instructions with human feedback | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Training-language-models-to-follow-instructions-Ouyang-Wu/d766bffc357127e0dc86dd69561d5aeb520d6f4c"},{"title":"(PDF) Training language models to follow instructions with human feedback","url":"https://www.researchgate.net/publication/359054867_Training_language_models_to_follow_instructions_with_human_feedback"},{"title":"Training language models to follow instructions with human feedback","url":"https://arxiv.org/pdf/2203.02155"},{"title":"Training language models to fol
…[truncated 1554 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_reference-augmentation_20260524T192339",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 35 · 2026-05-24T19:35:53.975698+00:00_

Web search results for query: "He DeBERTa-v3 2021 "DeBERTaV3 Improving DeBERTa using ELECTRA-Style" arXiv"

Links: [{"title":"[2111.09543] DeBERTaV3: Improving DeBERTa using ELECTRA-Style Pre-Training with Gradient-Disentangled Embedding Sharing","url":"https://arxiv.org/abs/2111.09543"},{"title":"[2111.09543v1] DeBERTaV3: Improving DeBERTa using ELECTRA-Style Pre-Training with Gradient-Disentangled Embedding Sharing","url":"https://arxiv.org/abs/2111.09543v1"},{"title":"[2111.09543v2] DeBERTaV3: Improving DeBERTa using ELECTRA-Style Pre-Training with Gradient-Disentangled Embedding Sharing","url":"https://arxiv.org/abs/2111.09543v2"},{"title":"[2111.09543v4] DeBERTaV3: Improving DeBERTa using ELECTRA-Style Pre-Training with Gradient-Disentangled Embedding Sharing","url":"https://arxiv.org/abs/2111.09543v4"},{"title":"[2111.09543] DeBERTaV3: Improving DeBERTa using ELECTRA-Style Pre-Training with Gradient-Disentangled Embedding Sharing","url":"https://ar5iv.labs.arxiv.org/html/2111.09543"},{"title":"[PDF] DeBERTaV3: Improving DeBERTa using ELECTRA-Style Pre-Training with Gradient-Disentangled Embedding Sharing | Semantic Scholar","url":"https://www.semanticscholar.org/paper/DeBERTaV3:-Improving-DeBERTa-using-ELECTRA-Style-He-Gao/972706306f85b1bfb40c7d35c796ad5174eb0c9c"},{"title":"DeBERTaV3: Improving DeBERTa using ELECTRA-Style Pre-Training with Gradient-Disentangled Embedding Sharing | OpenReview","url":"https://openreview.net/forum?id=sE7-XhLxHA"},{"title":"Work in progress DeBERTaV3: Improving DeBERTa using ELECTRA-","url":"https://arxiv.org/pdf/2111.09543v1"},{"title":"Debertav3: Improving deberta using electra-style pre- ...","url":"https://arxiv.org/pdf/2111.09543"}]

I found the paper you're looking for! Here are the key details:

**Paper Title:** DeBERTaV3: Improving DeBERTa using ELECTRA-Style Pre-Training with Gradient-Disentangled Embedding Sharing

**Authors:** Pengcheng He and co-authors

**arXiv ID:** 2111.09543

**Key Contributions:**

The paper pres
…[truncated 1039 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_reference-augmentation_20260524T192339",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 36 · 2026-05-24T19:35:53.975861+00:00_

Web search results for query: "NLI natural language inference information extraction 2026 arXiv"

Links: [{"title":"[2601.05170] Reverse-engineering NLI: A study of the meta-inferential properties of Natural Language Inference","url":"https://arxiv.org/abs/2601.05170"},{"title":"Natural Language Inference (NLI)","url":"https://www.emergentmind.com/topics/natural-language-inference-nli"},{"title":"Natural Language Inference Model","url":"https://www.emergentmind.com/topics/natural-language-inference-nli-model"},{"title":"[2601.06528] Atomic-SNLI: Fine-Grained Natural Language Inference through Atomic Fact Decomposition","url":"https://arxiv.org/abs/2601.06528"},{"title":"[2505.06607v1] Boosting Neural Language Inference via Cascaded Interactive Reasoning","url":"https://arxiv.org/abs/2505.06607v1"},{"title":"The geometry of meaning: evaluating sentence embeddings from diverse transformer-based models for natural language inference","url":"https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12193426/"},{"title":"Natural language inference for clinical registry curation","url":"https://www.medrxiv.org/content/10.1101/2021.06.14.21258493.full.pdf"},{"title":"NILE : Natural Language Inference with Faithful Natural Language   Explanations","url":"https://arxiv.org/pdf/2005.12116"},{"title":"Natural Language Inference over Interaction Space","url":"https://arxiv.org/pdf/1709.04348"}]

Here are the search results for "NLI natural language inference information extraction 2026 arXiv":

## Recent 2026 arXiv Papers on NLI

**1. Reverse-engineering NLI: A study of the meta-inferential properties of Natural Language Inference**
- Natural Language Inference (NLI) has been an important task for evaluating language models for Natural Language Understanding, but the logical properties of the task are poorly understood and often mischaracterized.
- The paper formulates three possible readings of the NLI label set and performs a comprehensive analysis of the meta-inferential properties they 
…[truncated 976 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_reference-augmentation_20260524T192339",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 37 · 2026-05-24T19:35:53.976025+00:00_

Web search results for query: "scaling law LLM fine-tuning 2026 arXiv"

Links: [{"title":"LLM Scaling Laws Explained: Will Bigger AI Models Always Win? (2026)","url":"https://www.buildfastwithai.com/blogs/llm-scaling-laws-explained"},{"title":"[2505.06150] A Scaling Law for Token Efficiency in LLM Fine-Tuning Under Fixed Compute Budgets","url":"https://arxiv.org/abs/2505.06150"},{"title":"A Scaling Law for Token Efficiency in LLM Fine-Tuning Under Fixed Compute Budgets","url":"https://arxiv.org/pdf/2505.06150"},{"title":"Scaling Laws Meet Model Architecture: Toward Inference-Efficient LLMs","url":"https://arxiv.org/html/2510.18245v3"},{"title":"A Scaling Law for Token Efficiency in LLM Fine-Tuning Under Fixed Compute Budgets","url":"https://arxiv.org/html/2505.06150v1"},{"title":"[2510.18245] Scaling Laws Meet Model Architecture: Toward Inference-Efficient LLMs","url":"https://arxiv.org/abs/2510.18245"},{"title":"[2402.17193] When Scaling Meets LLM Finetuning: The Effect of Data, Model and Finetuning Method","url":"https://arxiv.org/abs/2402.17193"},{"title":"[2402.02314] Selecting Large Language Model to Fine-tune via Rectified Scaling Law","url":"https://arxiv.org/abs/2402.02314"}]

Based on the search results, I found several recent arXiv papers on scaling laws for LLM fine-tuning:

## Key Recent Research (2025-2026)

**A Scaling Law for Token Efficiency in LLM Fine-Tuning Under Fixed Compute Budgets** (May 2025)

This paper introduces a scaling law for fine-tuning LLMs under fixed compute budgets that explicitly accounts for data composition, showing that the number of examples and their average token length play a decisive role in model performance. The research reveals that data composition significantly affects token efficiency.

**Scaling Laws Meet Model Architecture: Toward Inference-Efficient LLMs** (Updated May 2026)

This paper introduces a conditional scaling law that augments the Chinchilla framework with architectural information, along with a search 
…[truncated 734 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_reference-augmentation_20260524T192339",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 38 · 2026-05-24T19:35:53.976187+00:00_

Web search results for query: "Tree-GRPO ICLR 2026 tree search LLM agent reinforcement learning"

Links: [{"title":"GitHub - AMAP-ML/Tree-GRPO: [ICLR 2026] Tree Search for LLM Agent Reinforcement Learning · GitHub","url":"https://github.com/AMAP-ML/Tree-GRPO"},{"title":"TREE SEARCH FOR LLM AGENT REINFORCEMENT ...","url":"https://openreview.net/pdf?id=ZpQwAFhU13"},{"title":"[2509.21240] Tree Search for LLM Agent Reinforcement Learning","url":"https://arxiv.org/abs/2509.21240"},{"title":"Tree Search for LLM Agent Reinforcement Learning | alphaXiv","url":"https://www.alphaxiv.org/overview/2509.21240v1"},{"title":"[Literature Review] Tree Search for LLM Agent Reinforcement Learning","url":"https://www.themoonlight.io/en/review/tree-search-for-llm-agent-reinforcement-learning"},{"title":"Tree Search for LLM Agent Reinforcement Learning | Takara TLDR","url":"https://tldr.takara.ai/p/2509.21240"},{"title":"Paper page - Tree Search for LLM Agent Reinforcement Learning","url":"https://huggingface.co/papers/2509.21240"},{"title":"Tree Search for LLM Agent Reinforcement Learning","url":"https://arxiv.org/pdf/2509.21240"}]

Based on the search results, here's what I found about Tree-GRPO:

## Overview

Tree-GRPO adopts a tree-search rollout strategy in place of independent chain-based rollouts for LLM agent RL. The paper was accepted by ICLR 2026 on January 27, 2026.

## Key Problem and Solution

In long-term and multi-turn agent tasks, existing approaches driven solely by outcome rewards often suffer from the problem of sparse supervision. Tree-GRPO is a grouped agent RL method based on tree search, where each tree node represents the complete agent interaction step.

## Core Advantages

By sharing common prefixes, the tree search sampling increases the number of rollouts achievable within a fixed budget of tokens or tool calls. Moreover, the tree-structured trajectory naturally allows the construction of step-wise process supervised signals even using only the outcome reward.
…[truncated 505 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_reference-augmentation_20260524T192339",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool call

_source line 39 · 2026-05-24T19:35:53.976386+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://arxiv.org/abs/2603.19532",
  "prompt": "Extract: title, all authors, year, arXiv ID. Is this a 2026 paper about evidence consistency and GRPO?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_reference-augmentation_20260524T192339",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://arxiv.org/abs/2603.19532",
    "prompt": "Extract: title, all authors, year, arXiv ID. Is this a 2026 paper about evidence consistency and GRPO?"
  }
}
```

</details>

---

### Tool call

_source line 40 · 2026-05-24T19:35:53.976512+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://arxiv.org/abs/2601.09253",
  "prompt": "Extract: title, all authors, year, arXiv ID. Is this a 2026 paper about rejection sampling fine-tuning?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_reference-augmentation_20260524T192339",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://arxiv.org/abs/2601.09253",
    "prompt": "Extract: title, all authors, year, arXiv ID. Is this a 2026 paper about rejection sampling fine-tuning?"
  }
}
```

</details>

---

### Tool call

_source line 41 · 2026-05-24T19:35:53.976628+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://arxiv.org/abs/2602.04391",
  "prompt": "Extract: title, all authors, year, arXiv ID. Is this a 2026 paper about rejection sampling / trajectory fusion?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_reference-augmentation_20260524T192339",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://arxiv.org/abs/2602.04391",
    "prompt": "Extract: title, all authors, year, arXiv ID. Is this a 2026 paper about rejection sampling / trajectory fusion?"
  }
}
```

</details>

---

### Tool call

_source line 42 · 2026-05-24T19:35:53.976742+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://arxiv.org/abs/2605.17570",
  "prompt": "Extract: title, all authors, year, arXiv ID. Is this a 2026 paper about Mu-GRPO?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_reference-augmentation_20260524T192339",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://arxiv.org/abs/2605.17570",
    "prompt": "Extract: title, all authors, year, arXiv ID. Is this a 2026 paper about Mu-GRPO?"
  }
}
```

</details>

---

### Tool result

_source line 43 · 2026-05-24T19:35:53.976871+00:00_

# Paper Information

**Title:** "EvidenceRL: Reinforcing Evidence Consistency for Trustworthy Language Models"

**Authors:** J. Ben Tamo, Yuxing Lu, Benoit L. Marteau, Micky C. Nnamdi, May D. Wang

**Year:** 2026

**arXiv ID:** 2603.19532

**Regarding your question:** Yes, this is a 2026 paper addressing evidence consistency. The abstract confirms it employs "Group Relative Policy Optimization (GRPO)" as part of the reinforcement learning framework, which directly answers your inquiry about whether the paper focuses on both evidence consistency and GRPO methodology.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_reference-augmentation_20260524T192339",
  "tool": "WebFetch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 44 · 2026-05-24T19:35:53.976995+00:00_

# Paper Details

**Title:** "RIFT: Repurposing Negative Samples via Reward-Informed Fine-Tuning"

**Authors:** Zehua Liu, Shuqi Liu, Tao Zhong, Mingxuan Yuan

**Year:** 2026

**arXiv ID:** 2601.09253

---

## Is this about rejection sampling fine-tuning?

Yes, this paper addresses rejection sampling fine-tuning (RFT). The abstract states that "While Supervised Fine-Tuning (SFT) and Rejection Sampling Fine-Tuning (RFT) are standard for LLM alignment, they either rely on costly expert data or discard valuable negative samples." The proposed RIFT method improves upon RFT by repurposing negative trajectories rather than discarding them, making it a data-efficient alternative to traditional RFT approaches.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_reference-augmentation_20260524T192339",
  "tool": "WebFetch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 45 · 2026-05-24T19:35:53.977118+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Coste 2023 \"Reward Model Ensembles Help Mitigate Overoptimization\" best-of-N arXiv"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_reference-augmentation_20260524T192339",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Coste 2023 \"Reward Model Ensembles Help Mitigate Overoptimization\" best-of-N arXiv"
  }
}
```

</details>

---

### Tool call

_source line 46 · 2026-05-24T19:35:53.977246+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "relation extraction reinforcement learning reward 2026 arXiv structured prediction"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_reference-augmentation_20260524T192339",
  "tool": "WebSearch",
  "tool_args": {
    "query": "relation extraction reinforcement learning reward 2026 arXiv structured prediction"
  }
}
```

</details>

---

### Tool result

_source line 47 · 2026-05-24T19:35:53.977370+00:00_

# Paper Details

**Title:** "Beyond Rejection Sampling: Trajectory Fusion for Scaling Mathematical Reasoning"

**Authors:** Jie Deng, Hanshuang Tong, Jun Li, Shining Liang, Ning Wu, Hongzhi Li, Yutao Xie

**Year:** 2026

**arXiv ID:** 2602.04391

## Is this a 2026 paper about rejection sampling/trajectory fusion?

Yes. The paper proposes TrajFusion, described as "a fine-tuning strategy that reframes rejection sampling as a structured supervision construction process" by "interleaving selected incorrect trajectories with reflection prompts and correct trajectories." The submission date is February 4, 2026.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_reference-augmentation_20260524T192339",
  "tool": "WebFetch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 48 · 2026-05-24T19:35:53.977488+00:00_

**Title:** "How Off-Policy Can GRPO Be? Mu-GRPO for Efficient LLM Reinforcement Learning"

**Authors:** Minghao Tian, Yunfei Xie, Chen Wei

**Year:** 2026

**arXiv ID:** 2605.17570

**Is this a 2026 paper about Mu-GRPO?** Yes. The paper was submitted on May 17, 2026, and directly addresses Mu-GRPO as its primary focus, proposing this framework as an approach for efficient reinforcement learning in large language models.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_reference-augmentation_20260524T192339",
  "tool": "WebFetch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 49 · 2026-05-24T19:35:53.977620+00:00_

Web search results for query: "Coste 2023 "Reward Model Ensembles Help Mitigate Overoptimization" best-of-N arXiv"

Links: [{"title":"Reward Model Ensembles Help Mitigate Overoptimization.","url":"https://bibbase.org/network/publication/coste-anwar-kirk-krueger-rewardmodelensembleshelpmitigateoveroptimization-2023"},{"title":"[2310.02743v1] Reward Model Ensembles Help Mitigate Overoptimization","url":"https://arxiv.org/abs/2310.02743v1"},{"title":"Helping or Herding? Reward Model Ensembles Mitigate but do not Eliminate Reward Hacking","url":"https://arxiv.org/html/2312.09244v3"},{"title":"[2310.02743] Reward Model Ensembles Help Mitigate Overoptimization","url":"https://arxiv.org/abs/2310.02743"},{"title":"Reward Model Ensembles Help Mitigate Overoptimization","url":"https://arxiv.org/pdf/2310.02743"},{"title":"Reward Model Ensembles Help Mitigate Overoptimization | OpenReview","url":"https://openreview.net/forum?id=dcjtMYkpXx"},{"title":"Improving Reinforcement Learning from Human Feedback with Efficient Reward Model Ensemble","url":"https://arxiv.org/html/2401.16635v3"},{"title":"Provably Mitigating Overoptimization in RLHF: Your SFT Loss is Implicitly an Adversarial Regularizer","url":"https://arxiv.org/html/2405.16436v3"},{"title":"Reward Model Ensembles Help Mitigate Overoptimization - ADS","url":"https://ui.adsabs.harvard.edu/abs/2023arXiv231002743C/abstract"}]

I found the paper! Here's the key information about the Coste et al. 2023 paper:

**Title:** Reward Model Ensembles Help Mitigate Overoptimization

**Authors:** Coste, T., Anwar, U., Kirk, R., & Krueger, D.

**Publication:** CoRR, 2023 (arXiv:2310.02743)

**Main Research Focus:** The paper evaluates the efficacy of using ensemble-based conservative optimization objectives, specifically worst-case optimization (WCO) and uncertainty-weighted optimization (UWO), for mitigating reward model overoptimization when using best-of-n sampling (BoN) and proximal policy optimization (PPO).

**Key Findings:** Both 
…[truncated 560 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_reference-augmentation_20260524T192339",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 50 · 2026-05-24T19:35:53.977791+00:00_

Web search results for query: "relation extraction reinforcement learning reward 2026 arXiv structured prediction"

Links: [{"title":"[2510.06198] Peeking inside the Black-Box: Reinforcement Learning for Explainable and Accurate Relation Extraction","url":"https://arxiv.org/abs/2510.06198"},{"title":"A Hierarchical Framework for Relation Extraction with Reinforcement   Learning","url":"https://arxiv.org/pdf/1811.03925"},{"title":"Peeking inside the Black-Box: Reinforcement Learning for Explainable and Accurate Relation Extraction","url":"https://arxiv.org/html/2510.06198v1"},{"title":"Reinforcement Learning for Explainable and Accurate ...","url":"https://arxiv.org/pdf/2510.06198"},{"title":"Joint Extraction of Entities and Relations Using Reinforcement Learning and Deep Learning","url":"https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5574273/"},{"title":"Relation Mention Extraction from Noisy Data with Hierarchical   Reinforcement Learning","url":"https://arxiv.org/pdf/1811.01237"},{"title":"Hallucination-Resistant Relation Extraction via Dependency-Aware Sentence Simplification and Two-tiered Hierarchical Refinement","url":"https://arxiv.org/pdf/2508.14391"}]

I found several relevant papers on arXiv about relation extraction using reinforcement learning with reward functions. Here are the key findings:

## Recent 2026 Work

The most recent work is CogRE, a novel framework for relation extraction that enhances both accuracy and explainability through a reasoning mechanism that formulates relation extraction as a series of text-processing steps inspired by cognitive science, and an optimization process driven by reinforcement learning with a novel reward function. Optimizing this approach with RL using the proposed reward further improves performance by +23.46% (absolute).

The framework uses a credit dictionary during RL training to assign rewards by counting occurrences of relation keywords in model outputs, offering a fine-grained signal that reinforces the model's
…[truncated 774 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_reference-augmentation_20260524T192339",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 51 · 2026-05-24T19:35:53.977961+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://arxiv.org/abs/2305.14314",
  "prompt": "Extract exact: title, all authors (full list), year, venue (NeurIPS 2023?), arXiv ID"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_reference-augmentation_20260524T192339",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://arxiv.org/abs/2305.14314",
    "prompt": "Extract exact: title, all authors (full list), year, venue (NeurIPS 2023?), arXiv ID"
  }
}
```

</details>

---

### Tool call

_source line 52 · 2026-05-24T19:35:53.978081+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://arxiv.org/abs/2203.02155",
  "prompt": "Extract: title, first 5 authors, year, venue (NeurIPS 2022?), arXiv ID"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_reference-augmentation_20260524T192339",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://arxiv.org/abs/2203.02155",
    "prompt": "Extract: title, first 5 authors, year, venue (NeurIPS 2022?), arXiv ID"
  }
}
```

</details>

---

### Tool result

_source line 53 · 2026-05-24T19:35:53.978196+00:00_

# QLoRA Paper Details

**Title:** "QLoRA: Efficient Finetuning of Quantized LLMs"

**Authors:** Tim Dettmers, Artidoro Pagnoni, Ari Holtzman, Luke Zettlemoyer

**Year:** 2023

**Venue:** Extended NeurIPS submission (not confirmed as published in NeurIPS 2023)

**arXiv ID:** 2305.14314

**Submission Date:** May 23, 2023

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_reference-augmentation_20260524T192339",
  "tool": "WebFetch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 54 · 2026-05-24T19:35:53.978332+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://arxiv.org/abs/2009.13752",
  "prompt": "Extract: title, all authors, year, venue (EMNLP 2020?), arXiv ID"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_reference-augmentation_20260524T192339",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://arxiv.org/abs/2009.13752",
    "prompt": "Extract: title, all authors, year, venue (EMNLP 2020?), arXiv ID"
  }
}
```

</details>

---

### Tool call

_source line 55 · 2026-05-24T19:35:53.978454+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://arxiv.org/abs/2402.01306",
  "prompt": "Extract: title, all authors, year, venue (ICML 2024?), arXiv ID"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_reference-augmentation_20260524T192339",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://arxiv.org/abs/2402.01306",
    "prompt": "Extract: title, all authors, year, venue (ICML 2024?), arXiv ID"
  }
}
```

</details>

---

### Tool result

_source line 56 · 2026-05-24T19:35:53.978569+00:00_

# Paper Information Extract

**Title:** "Training language models to follow instructions with human feedback"

**First 5 Authors:** Long Ouyang, Jeff Wu, Xu Jiang, Diogo Almeida, Carroll L. Wainwright

**Year:** 2022

**Venue:** Not specified in the document. The submission date is March 4, 2022, but no conference venue is listed. (Note: While you reference NeurIPS 2022, this information does not appear on the arXiv page provided.)

**arXiv ID:** 2203.02155

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_reference-augmentation_20260524T192339",
  "tool": "WebFetch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 57 · 2026-05-24T19:35:53.978684+00:00_

# Paper Extract

**Title:** "Double Graph Based Reasoning for Document-level Relation Extraction"

**Authors:** Shuang Zeng, Runxin Xu, Baobao Chang, Lei Li

**Year:** 2020

**Venue:** EMNLP 2020 (accepted as long paper to main conference)

**arXiv ID:** 2009.13752

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_reference-augmentation_20260524T192339",
  "tool": "WebFetch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 58 · 2026-05-24T19:35:53.978797+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://arxiv.org/abs/2203.15556",
  "prompt": "Extract: title, all authors (first 5 is fine), year, venue (NeurIPS 2022?), arXiv ID"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_reference-augmentation_20260524T192339",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://arxiv.org/abs/2203.15556",
    "prompt": "Extract: title, all authors (first 5 is fine), year, venue (NeurIPS 2022?), arXiv ID"
  }
}
```

</details>

---

### Tool call

_source line 59 · 2026-05-24T19:35:53.978910+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://arxiv.org/abs/2111.09543",
  "prompt": "Extract: title, all authors, year, venue (ICLR 2023?), arXiv ID"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_reference-augmentation_20260524T192339",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://arxiv.org/abs/2111.09543",
    "prompt": "Extract: title, all authors, year, venue (ICLR 2023?), arXiv ID"
  }
}
```

</details>

---

### Tool result

_source line 60 · 2026-05-24T19:35:53.979021+00:00_

# Paper Information

**Title:** KTO: Model Alignment as Prospect Theoretic Optimization

**Authors:** Kawin Ethayarajh, Winnie Xu, Niklas Muennighoff, Dan Jurafsky, Douwe Kiela

**Year:** 2024

**Venue:** ICML 2024

**arXiv ID:** 2402.01306

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_reference-augmentation_20260524T192339",
  "tool": "WebFetch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 61 · 2026-05-24T19:35:53.979130+00:00_

# DeBERTaV3 Paper Details

**Title:** "DeBERTaV3: Improving DeBERTa using ELECTRA-Style Pre-Training with Gradient-Disentangled Embedding Sharing"

**Authors:** Pengcheng He, Jianfeng Gao, Weizhu Chen

**Year:** 2021 (submitted November 18, 2021)

**Venue:** ICLR 2023

**arXiv ID:** 2111.09543

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_reference-augmentation_20260524T192339",
  "tool": "WebFetch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 62 · 2026-05-24T19:35:53.979257+00:00_

# Paper Details

**Title:** "Training Compute-Optimal Large Language Models"

**Authors (first 5):** Jordan Hoffmann, Sebastian Borgeaud, Arthur Mensch, Elena Buchatskaya, Trevor Cai

**Year:** 2022

**Venue:** Not specified in this document (submitted March 29, 2022 to arXiv)

**arXiv ID:** 2203.15556

**Note:** The webpage does not indicate a specific conference venue like NeurIPS 2022. It only shows the arXiv submission date and classification as a computer science paper in the Computation and Language category.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_reference-augmentation_20260524T192339",
  "tool": "WebFetch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 63 · 2026-05-24T19:35:53.979452+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://arxiv.org/abs/2509.21240",
  "prompt": "Extract: title, all authors, year, arXiv ID. This was accepted at ICLR 2026?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_reference-augmentation_20260524T192339",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://arxiv.org/abs/2509.21240",
    "prompt": "Extract: title, all authors, year, arXiv ID. This was accepted at ICLR 2026?"
  }
}
```

</details>

---

### Tool call

_source line 64 · 2026-05-24T19:35:53.979585+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"document relation extraction\" LLM RL reward 2026 arXiv 2601 2602 2603 2604 2605"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_reference-augmentation_20260524T192339",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"document relation extraction\" LLM RL reward 2026 arXiv 2601 2602 2603 2604 2605"
  }
}
```

</details>

---

### Tool call

_source line 65 · 2026-05-24T19:35:53.979703+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "multi-task learning negative transfer LLM fine-tuning 2026 arXiv"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_reference-augmentation_20260524T192339",
  "tool": "WebSearch",
  "tool_args": {
    "query": "multi-task learning negative transfer LLM fine-tuning 2026 arXiv"
  }
}
```

</details>

---

### Tool result

_source line 66 · 2026-05-24T19:35:53.979819+00:00_

# Paper Information

**Title:** "Tree Search for LLM Agent Reinforcement Learning"

**Authors:** Yuxiang Ji, Ziyu Ma, Yong Wang, Guanhua Chen, Xiangxiang Chu, Liaoni Wu

**Year:** 2025 (submitted September 25, 2025; last revised March 18, 2026)

**arXiv ID:** 2509.21240

**ICLR 2026 Acceptance:** Yes, the paper indicates "ICLR 2026" in the comments section, confirming it was accepted at that venue.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_reference-augmentation_20260524T192339",
  "tool": "WebFetch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 67 · 2026-05-24T19:35:53.979959+00:00_

Web search results for query: ""document relation extraction" LLM RL reward 2026 arXiv 2601 2602 2603 2604 2605"

Links: [{"title":"Relation as a Prior: A Novel Paradigm for LLM-based Document-level Relation Extraction","url":"https://arxiv.org/pdf/2511.08143"},{"title":"[2601.07271] Document-Level Zero-Shot Relation Extraction with Entity Side Information","url":"https://arxiv.org/abs/2601.07271"},{"title":"Consistency Guided Knowledge Retrieval and Denoising in LLMs for   Zero-shot Document-level Relation Triplet Extraction","url":"https://arxiv.org/pdf/2401.13598"},{"title":"LLM with Relation Classifier for Document-Level Relation Extraction","url":"https://arxiv.org/pdf/2408.13889"},{"title":"LLM with Relation Classifier for Document-Level Relation Extraction","url":"https://arxiv.org/html/2408.13889v1"},{"title":"Zero-Shot Document-Level Biomedical Relation Extraction via Scenario-based Prompt Design in Two-Stage with LLM","url":"https://arxiv.org/pdf/2505.01077"},{"title":"[2408.13889] LLM with Relation Classifier for Document-Level Relation Extraction","url":"https://arxiv.org/abs/2408.13889"}]

I found several relevant papers on document-level relation extraction with LLMs. Here are the results:

## Recent Papers (2026 and Late 2025)

**Document-Level Zero-Shot Relation Extraction with Entity Side Information (arXiv 2601.07271)**: This paper addresses Document-Level Zero-Shot Relation Extraction (DocZSRE) to predict unseen relation labels in documents without prior training on specific relations. Existing approaches rely on LLMs to generate synthetic data for unseen labels, and this new approach introduces an alternative framework.

**Relation as a Prior: A Novel Paradigm for LLM-based Document-level Relation Extraction**: This paper addresses performance gaps in Document-level Relation Extraction (DocRE) requiring fine-grained comprehension. The paper proposes a "Relation as a Prior" paradigm that transforms relation filtering into a binary classification t
…[truncated 773 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_reference-augmentation_20260524T192339",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 68 · 2026-05-24T19:35:53.980117+00:00_

Web search results for query: "multi-task learning negative transfer LLM fine-tuning 2026 arXiv"

Links: [{"title":"Synergy over Discrepancy: A Partition-Based Approach to Multi-Domain LLM Fine-Tuning","url":"https://arxiv.org/pdf/2511.07198"},{"title":"Mitigating Negative Transfer in Multi-Task Learning with Exponential   Moving Average Loss Weighting Strategies","url":"https://arxiv.org/pdf/2211.12999"},{"title":"ForkMerge: Mitigating Negative Transfer in Auxiliary-Task Learning","url":"https://arxiv.org/pdf/2301.12618"},{"title":"Identification of Negative Transfers in Multitask Learning Using   Surrogate Models","url":"https://arxiv.org/pdf/2303.14582"},{"title":"Mixing It Up:The Cocktail Effect of Multi-Task Fine-Tuning on LLM Performance - A Case Study in Finance","url":"https://arxiv.org/html/2410.01109v1"},{"title":"Donors and Recipients: On Asymmetric Transfer Across Tasks and Languages with Parameter-Efficient Fine-Tuning","url":"https://arxiv.org/pdf/2511.13368"},{"title":"Towards Understanding Multi-Task Learning (Generalization) of LLMs via   Detecting and Exploring Task-Specific Neurons","url":"https://arxiv.org/pdf/2407.06488"}]

I found several relevant research papers on arXiv related to multi-task learning, negative transfer, and LLM fine-tuning. Here are the key findings:

**Recent 2026 Papers:**

A recent study addresses how domain-specific features may negatively interfere in multi-domain LLM fine-tuning, with one domain potentially overshadowing others or impairing generalization, and proposes approaches to exploit inter-domain synergies while mitigating negative interference.

**Negative Transfer in Multi-Task Learning:**

Learning multiple tasks simultaneously often results in worse performance than learning them independently, which is known as negative transfer. One approach, ForkMerge, periodically forks the model into multiple branches with different task weights and merges dynamically to filter out detrimental parameter updates to avoid 
…[truncated 821 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_reference-augmentation_20260524T192339",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 69 · 2026-05-24T19:35:53.980312+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://arxiv.org/abs/2308.01825",
  "prompt": "Extract: title, all authors, year, venue, arXiv ID. Is this about rejection sampling fine-tuning (RFT) for mathematical reasoning?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_reference-augmentation_20260524T192339",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://arxiv.org/abs/2308.01825",
    "prompt": "Extract: title, all authors, year, venue, arXiv ID. Is this about rejection sampling fine-tuning (RFT) for mathematical reasoning?"
  }
}
```

</details>

---

### Tool call

_source line 70 · 2026-05-24T19:35:53.980444+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://arxiv.org/abs/2601.07271",
  "prompt": "Extract: title, all authors, year, arXiv ID. Is this about document-level zero-shot relation extraction in 2026?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_reference-augmentation_20260524T192339",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://arxiv.org/abs/2601.07271",
    "prompt": "Extract: title, all authors, year, arXiv ID. Is this about document-level zero-shot relation extraction in 2026?"
  }
}
```

</details>

---

### Tool call

_source line 71 · 2026-05-24T19:35:53.980564+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://arxiv.org/abs/2310.02743",
  "prompt": "Extract: title, all authors, year, venue (published at ICLR 2024?), arXiv ID"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_reference-augmentation_20260524T192339",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://arxiv.org/abs/2310.02743",
    "prompt": "Extract: title, all authors, year, venue (published at ICLR 2024?), arXiv ID"
  }
}
```

</details>

---

### Tool result

_source line 72 · 2026-05-24T19:35:53.980686+00:00_

# Paper Extraction

**Title:** Scaling Relationship on Learning Mathematical Reasoning with Large Language Models

**Authors:** Zheng Yuan, Hongyi Yuan, Chengpeng Li, Guanting Dong, Keming Lu, Chuanqi Tan, Chang Zhou, Jingren Zhou

**Year:** 2023

**Venue:** arXiv (cs.CL - Computation and Language)

**arXiv ID:** 2308.01825

---

## RFT Focus

Yes, this paper substantially addresses rejection sampling fine-tuning. The authors "propose to apply Rejection sampling Fine-Tuning (RFT)" and explore how it generates augmented datasets from supervised models to enhance mathematical reasoning performance in LLMs, demonstrating notable improvements over standard supervised fine-tuning approaches.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_reference-augmentation_20260524T192339",
  "tool": "WebFetch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 73 · 2026-05-24T19:35:53.980808+00:00_

# Paper Details

**Title:** Reward Model Ensembles Help Mitigate Overoptimization

**Authors:** Thomas Coste, Usman Anwar, Robert Kirk, David Krueger

**Year:** 2023 (submitted October 4, 2023; revised March 10, 2024)

**Venue:** ICLR 2024 (accepted)

**arXiv ID:** 2310.02743

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_reference-augmentation_20260524T192339",
  "tool": "WebFetch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 74 · 2026-05-24T19:35:53.980980+00:00_

# Paper Details

**Title:** "Document-Level Zero-Shot Relation Extraction with Entity Side Information"

**Authors:** Mohan Raj Chanthran, Soon Lay Ki, Ong Huey Fang, Bhawani Selvaretnam

**Year:** 2026

**arXiv ID:** 2601.07271

## Is this about document-level zero-shot relation extraction in 2026?

Yes. The paper addresses "Document-Level Zero-Shot Relation Extraction" and proposes a framework called DocZSRE-SI that operates without relying on synthetic data from large language models, focusing on low-resource languages like Malaysian English. The submission was made in January 2026.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_reference-augmentation_20260524T192339",
  "tool": "WebFetch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 75 · 2026-05-24T19:35:53.981343+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/references.bib",
  "old_string": "@inproceedings{wang2023selfconsistency,\n  title     = {Self-Consistency Improves Chain of Thought Reasoning in Language Models},\n  author    = {Wang, Xuezhi and Wei, Jason and Schuurmans, Dale and Le, Quoc and Chi, Ed and Narang, Sharan and Chowdhery, Aakanksha and Zhou, Denny},\n  booktitle = {The Eleventh International Conference on Learning Representations},\n  year      = {2023},\n  url       = {https://arxiv.org/abs/2203.11171}\n}",
  "new_string": "@inproceedings{wang2023selfconsistency,\n  title     = {Self-Consistency Improves Chain of Thought Reasoning in Language Models},\n  author    = {Wang, Xuezhi and Wei, Jason and Schuurmans, Dale and Le, Quoc and Chi, Ed and Narang, Sharan and Chowdhery, Aakanksha and Zhou, Denny},\n  booktitle = {The Eleventh International Conference on Learning Representations},\n  year      = {2023},\n  url       = {https://arxiv.org/abs/2203.11171}\n}\n\n@inproceedings{ouyang2022instructgpt,\n  title     = {Training Language Models to Follow Instructions with Human Feedback},\n  author    = {Ouyang, Long and Wu, Jeff and Jiang, Xu and Almeida, Diogo and Wainwright, Carroll L. and Mishkin, Pamela and Zhang, Chong and Agarwal, Sandhini and Slama, Katarina and Ray, Alex and Schulman, John and Hilton, Jacob and Kelton, Fraser and Miller, Luke and Simens, Maddie and Askell, Amanda and Welinder, Peter and Christiano, Paul F. and Leike, Jan and Lowe, Ryan},\n  booktitle = {Advances in Neural Information Processing Systems},\n  year      = {2022},\n  url       = {https://arxiv.org/abs/2203.02155}\n}\n\n@article{schulman2017ppo,\n  title   = {Proximal Policy Optimization Algorithms},\n  author  = {Schulman, John and Wolski, Filip and Dhariwal, Prafulla and Radford, Alec and Klimov, Oleg},\n  journal = {arXiv preprint arXiv:1707.06347},\n  year    = {2017},\n  url     = {https://arxiv.org/abs/1707.06347}\n}\n\n@inproceedings{zeng2020gain,\n  title     = {Double Graph Based Reasoning for Document-level Relation Extraction},\n  author    = {Zeng, Shuang and Xu, Runxin and Chang, Baobao and Li, Lei},\n  booktitle = {Proceedings of the 2020 Conference on Empirical Methods in Natural Language Processing},\n  year      = {2020},\n  url       = {https://aclanthology.org/2020.emnlp-main.127/}\n}\n\n@inproceedings{ethayarajh2024kto,\n  title     = {{KTO}: Model Alignment as Prospect Theoretic Optimization},\n  author    = {Ethayarajh, Kawin and Xu, Winnie and Muennighoff, Niklas and Jurafsky, Dan and Kiela, Douwe},\n  booktitle = {Proceedings of the 41st International Conference on Machine Learning},\n  year      = {2024},\n  url       = {https://arxiv.org/abs/2402.01306}\n}\n\n@inproceedings{coste2024reward,\n  title     = {Reward Model Ensembles Help Mitigate Overoptimization},\n  author    = {Coste, Thomas and Anwar, Usman and Kirk, Robert and Krueger, David},\n  booktitle = {International Conference on Learning Representations},\n  year      = {2024},\n  url       = {https://arxiv.org/abs/2310.02743}\n}\n\n@inproceedings{he2023debertav3,\n  title     = {{DeBERTaV3}: Improving {DeBERTa} using {ELECTRA}-Style Pre-Training with Gradient-Disentangled Embedding Sharing},\n  author    = {He, Pengcheng and Gao, Jianfeng and Chen, Weizhu},\n  booktitle = {International Conference on Learning Representations},\n  year      = {2023},\n  url       = {https://arxiv.org/abs/2111.09543}\n}\n\n@inproceedings{dettmers2023qlora,\n  title     = {{QLoRA}: Efficient Finetuning of Quantized {LLMs}},\n  author    = {Dettmers, Tim and Pagnoni, Artidoro and Holtzman, Ari and Zettlemoyer, Luke},\n  booktitle = {Advances in Neural Information Processing Systems},\n  year      = {2023},\n  url       = {https://arxiv.org/abs/2305.14314}\n}\n\n@inproceedings{hoffmann2022chinchilla,\n  title     = {Training Compute-Optimal Large Language Models},\n  author    = {Hoffmann, Jordan and Borgeaud, Sebastian and Mensch, Arthur and Buchatskaya, Elena and Cai, Trevor and Rutherford, Eliza and de Las Casas, Diego and Hendricks, Lisa Anne and Welbl, Johannes and Clark, Aidan and Hennigan, Tom and Noland, Eric and Millican, Katie and van den Driessche, George and Damoc, Bogdan and Guy, Aurelia and Osindero, Simon and Simonyan, Karen and Elsen, Erich and Rae, Jack W. and Vinyals, Oriol and Sifre, Laurent},\n  booktitle = {Advances in Neural Information Processing Systems},\n  year      = {2022},\n  url       = {https://arxiv.org/abs/2203.15556}\n}\n\n@article{yuan2023rft,\n  title   = {Scaling Relationship on Learning Mathematical Reasoning with Large Language Models},\n  author  = {Yuan, Zheng and Yuan, Hongyi and Li, Chengpeng and Dong, Guanting and Lu, Keming and Tan, Chuanqi and Zhou, Chang and Zhou, Jingren},\n  journal = {arXiv preprint arXiv:2308.01825},\n  year    = {2023},\n  url     = {https://arxiv.org/abs/2308.01825}\n}\n\n@article{tamo2026evidencerl,\n  title   = {{EvidenceRL}: Reinforcing Evidence Consistency for Trustworthy Language Models},\n  author  = {Tamo, J. Ben and Lu, Yuxing and Marteau, Benoit L. and Nnamdi, Micky C. and Wang, May D.},\n  journal = {arXiv preprint arXiv:2603.19532},\n  year    = {2026},\n  url     = {https://arxiv.org/abs/2603.19532}\n}\n\n@article{liu2026rift,\n  title   = {{RIFT}: Repurposing Negative Samples via Reward-Informed Fine-Tuning},\n  author  = {Liu, Zehua and Liu, Shuqi and Zhong, Tao and Yuan, Mingxuan},\n  journal = {arXiv preprint arXiv:2601.09253},\n  year    = {2026},\n  url     = {https://arxiv.org/abs/2601.09253}\n}\n\n@article{deng2026trajfusion,\n  title   = {Beyond Rejection Sampling: Trajectory Fusion for Scaling Mathematical Reasoning},\n  author  = {Deng, Jie and Tong, Hanshuang and Li, Jun and Liang, Shining and Wu, Ning and Li, Hongzhi and Xie, Yutao},\n  journal = {arXiv preprint arXiv:2602.04391},\n  year    = {2026},\n  url     = {https://arxiv.org/abs/2602.04391}\n}\n\n@article{tian2026mugrpo,\n  title   = {How Off-Policy Can {GRPO} Be? {$\\mu$-GRPO} for Efficient {LLM} Reinforcement Learning},\n  author  = {Tian, Minghao and Xie, Yunfei and Wei, Chen},\n  journal = {arXiv preprint arXiv:2605.17570},\n  year    = {2026},\n  url     = {https://arxiv.org/abs/2605.17570}\n}\n\n@inproceedings{ji2026treegrpo,\n  title     = {Tree Search for {LLM} Agent Reinforcement Learning},\n  author    = {Ji, Yuxiang and Ma, Ziyu and Wang, Yong and Chen, Guanhua and Chu, Xiangxiang and Wu, Liaoni},\n  booktitle = {International Conference on Learning Representations},\n  year      = {2026},\n  url       = {https://arxiv.org/abs/2509.21240}\n}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_reference-augmentation_20260524T192339",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/references.bib",
    "old_string": "@inproceedings{wang2023selfconsistency,\n  title     = {Self-Consistency Improves Chain of Thought Reasoning in Language Models},\n  author    = {Wang, Xuezhi and Wei, Jason and Schuurmans, Dale and Le, Quoc and Chi, Ed and Narang, Sharan and Chowdhery, Aakanksha and Zhou, Denny},\n  booktitle = {The Eleventh International Conference on Learning Representations},\n  year      = {2023},\n  url       = {https://arxiv.org/abs/2203.11171}\n}",
    "new_string": "@inproceedings{wang2023selfconsistency,\n  title     = {Self-Consistency Improves Chain of Thought Reasoning in Language Models},\n  author    = {Wang, Xuezhi and Wei, Jason and Schuurmans, Dale and Le, Quoc and Chi, Ed and Narang, Sharan and Chowdhery, Aakanksha and Zhou, Denny},\n  booktitle = {The Eleventh International Conference on Learning Representations},\n  year      = {2023},\n  url       = {https://arxiv.org/abs/2203.11171}\n}\n\n@inproceedings{ouyang2022instructgpt,\n  title     = {Training Language Models to Follow Instructions with Human Feedback},\n  author    = {Ouyang, Long and Wu, Jeff and Jiang, Xu and Almeida, Diogo and Wainwright, Carroll L. and Mishkin, Pamela and Zhang, Chong and Agarwal, Sandhini and Slama, Katarina and Ray, Alex and Schulman, John and Hilton, Jacob and Kelton, Fraser and Miller, Luke and Simens, Maddie and Askell, Amanda and Welinder, Peter and Christiano, Paul F. and Leike, Jan and Lowe, Ryan},\n  booktitle = {Advances in Neural Information Processing Systems},\n  year      = {2022},\n  url       = {https://arxiv.org/abs/2203.02155}\n}\n\n@article{schulman2017ppo,\n  title   = {Proximal Policy Optimization Algorithms},\n  author  = {Schulman, John and Wolski, Filip and Dhariwal, Prafulla and Radford, Alec and Klimov, Oleg},\n  journal = {arXiv preprint arXiv:1707.06347},\n  year    = {2017},\n  url     = {https://arxiv.org/abs/1707.06347}\n}\n\n@inproceedings{zeng2020gain,\n  title     = {Double Graph Based Reasoning for Document-level Relation Extraction},\n  author    = {Zeng, Shuang and Xu, Runxin and Chang, Baobao and Li, Lei},\n  booktitle = {Proceedings of the 2020 Conference on Empirical Methods in Natural Language Processing},\n  year      = {2020},\n  url       = {https://aclanthology.org/2020.emnlp-main.127/}\n}\n\n@inproceedings{ethayarajh2024kto,\n  title     = {{KTO}: Model Alignment as Prospect Theoretic Optimization},\n  author    = {Ethayarajh, Kawin and Xu, Winnie and Muennighoff, Niklas and Jurafsky, Dan and Kiela, Douwe},\n  booktitle = {Proceedings of the 41st International Conference on Machine Learning},\n  year      = {2024},\n  url       = {https://arxiv.org/abs/2402.01306}\n}\n\n@inproceedings{coste2024reward,\n  title     = {Reward Model Ensembles Help Mitigate Overoptimization},\n  author    = {Coste, Thomas and Anwar, Usman and Kirk, Robert and Krueger, David},\n  booktitle = {International Conference on Learning Representations},\n  year      = {2024},\n  url       = {https://arxiv.org/abs/2310.02743}\n}\n\n@inproceedings{he2023debertav3,\n  title     = {{DeBERTaV3}: Improving {DeBERTa} using {ELECTRA}-Style Pre-Training with Gradient-Disentangled Embedding Sharing},\n  author    = {He, Pengcheng and Gao, Jianfeng and Chen, Weizhu},\n  booktitle = {International Conference on Learning Representations},\n  year      = {2023},\n  url       = {https://arxiv.org/abs/2111.09543}\n}\n\n@inproceedings{dettmers2023qlora,\n  title     = {{QLoRA}: Efficient Finetuning of Quantized {LLMs}},\n  author    = {Dettmers, Tim and Pagnoni, Artidoro and Holtzman, Ari and Zettlemoyer, Luke},\n  booktitle = {Advances in Neural Information Processing Systems},\n  year      = {2023},\n  url       = {https://arxiv.org/abs/2305.14314}\n}\n\n@inproceedings{hoffmann2022chinchilla,\n  title     = {Training Compute-Optimal Large Language Models},\n  author    = {Hoffmann, Jordan and Borgeaud, Sebastian and Mensch, Arthur and Buchatskaya, Elena and Cai, Trevor and Rutherford, Eliza and de Las Casas, Diego and Hendricks, Lisa Anne and Welbl, Johannes and Clark, Aidan and Hennigan, Tom and Noland, Eric and Millican, Katie and van den Driessche, George and Damoc, Bogdan and Guy, Aurelia and Osindero, Simon and Simonyan, Karen and Elsen, Erich and Rae, Jack W. and Vinyals, Oriol and Sifre, Laurent},\n  booktitle = {Advances in Neural Information Processing Systems},\n  year      = {2022},\n  url       = {https://arxiv.org/abs/2203.15556}\n}\n\n@article{yuan2023rft,\n  title   = {Scaling Relationship on Learning Mathematical Reasoning with Large Language Models},\n  author  = {Yuan, Zheng and Yuan, Hongyi and Li, Chengpeng and Dong, Guanting and Lu, Keming and Tan, Chuanqi and Zhou, Chang and Zhou, Jingren},\n  journal = {arXiv preprint arXiv:2308.01825},\n  year    = {2023},\n  url     = {https://arxiv.org/abs/2308.01825}\n}\n\n@article{tamo2026evidencerl,\n  title   = {{EvidenceRL}: Reinforcing Evidence Consistency for Trustworthy Language Models},\n  author  = {Tamo, J. Ben and Lu, Yuxing and Marteau, Benoit L. and Nnamdi, Micky C. and Wang, May D.},\n  journal = {arXiv preprint arXiv:2603.19532},\n  year    = {2026},\n  url     = {https://arxiv.org/abs/2603.19532}\n}\n\n@article{liu2026rift,\n  title   = {{RIFT}: Repurposing Negative Samples via Reward-Informed Fine-Tuning},\n  author  = {Liu, Zehua and Liu, Shuqi and Zhong, Tao and Yuan, Mingxuan},\n  journal = {arXiv preprint arXiv:2601.09253},\n  year    = {2026},\n  url     = {https://arxiv.org/abs/2601.09253}\n}\n\n@article{deng2026trajfusion,\n  title   = {Beyond Rejection Sampling: Trajectory Fusion for Scaling Mathematical Reasoning},\n  author  = {Deng, Jie and Tong, Hanshuang and Li, Jun and Liang, Shining and Wu, Ning and Li, Hongzhi and Xie, Yutao},\n  journal = {arXiv preprint arXiv:2602.04391},\n  year    = {2026},\n  url     = {https://arxiv.org/abs/2602.04391}\n}\n\n@article{tian2026mugrpo,\n  title   = {How Off-Policy Can {GRPO} Be? {$\\mu$-GRPO} for Efficient {LLM} Reinforcement Learning},\n  author  = {Tian, Minghao and Xie, Yunfei and Wei, Chen},\n  journal = {arXiv preprint arXiv:2605.17570},\n  year    = {2026},\n  url     = {https://arxiv.org/abs/2605.17570}\n}\n\n@inproceedings{ji2026treegrpo,\n  title     = {Tree Search for {LLM} Agent Reinforcement Learning},\n  author    = {Ji, Yuxiang and Ma, Ziyu and Wang, Yong and Chen, Guanhua and Chu, Xiangxiang and Wu, Liaoni},\n  booktitle = {International Conference on Learning Representations},\n  year      = {2026},\n  url       = {https://arxiv.org/abs/2509.21240}\n}"
  }
}
```

</details>

---

### Tool result

_source line 76 · 2026-05-24T19:35:53.981622+00:00_

The file /home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/references.bib has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_reference-augmentation_20260524T192339",
  "tool": "Edit",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 77 · 2026-05-24T19:35:53.981776+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/sections/related_work.tex",
  "old_string": "ATLOP \\citep{zhou2021atlop} introduced adaptive thresholding for multi-label prediction and localized context pooling for entity representations.",
  "new_string": "ATLOP \\citep{zhou2021atlop} introduced adaptive thresholding with localized context pooling, and graph-based methods such as GAIN \\citep{zeng2020gain} model inter-sentence reasoning through heterogeneous mention-level and entity-level graphs."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_reference-augmentation_20260524T192339",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/sections/related_work.tex",
    "old_string": "ATLOP \\citep{zhou2021atlop} introduced adaptive thresholding for multi-label prediction and localized context pooling for entity representations.",
    "new_string": "ATLOP \\citep{zhou2021atlop} introduced adaptive thresholding with localized context pooling, and graph-based methods such as GAIN \\citep{zeng2020gain} model inter-sentence reasoning through heterogeneous mention-level and entity-level graphs."
  }
}
```

</details>

---

### Tool result

_source line 78 · 2026-05-24T19:35:53.981910+00:00_

&lt;tool_use_error>File has been modified since read, either by the user or by a linter. Read it again before attempting to write it.&lt;/tool_use_error>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_reference-augmentation_20260524T192339",
  "tool": "Edit",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 79 · 2026-05-24T19:35:53.982031+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/sections/related_work.tex",
  "old_string": "Group Relative Policy Optimization (GRPO; \\citealt{shao2024deepseekmath}) eliminates the separate value network by computing advantages within groups.",
  "new_string": "Group Relative Policy Optimization (GRPO; \\citealt{shao2024deepseekmath}) replaces the value network of PPO \\citep{schulman2017ppo} by computing advantages within groups."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_reference-augmentation_20260524T192339",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/sections/related_work.tex",
    "old_string": "Group Relative Policy Optimization (GRPO; \\citealt{shao2024deepseekmath}) eliminates the separate value network by computing advantages within groups.",
    "new_string": "Group Relative Policy Optimization (GRPO; \\citealt{shao2024deepseekmath}) replaces the value network of PPO \\citep{schulman2017ppo} by computing advantages within groups."
  }
}
```

</details>

---

### Tool result

_source line 80 · 2026-05-24T19:35:53.982152+00:00_

&lt;tool_use_error>File has been modified since read, either by the user or by a linter. Read it again before attempting to write it.&lt;/tool_use_error>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_reference-augmentation_20260524T192339",
  "tool": "Edit",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 81 · 2026-05-24T19:35:53.982289+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/sections/related_work.tex",
  "old_string": "Subsequent work addresses failure modes: DAPO \\citep{yu2025dapo} prevents entropy collapse, Dr.\\ GRPO \\citep{liu2025drgrpo} corrects length bias, and multi-objective variants \\citep{liu2026gdpo,ito2025mogrpo} handle competing reward signals.",
  "new_string": "Subsequent work addresses failure modes: DAPO \\citep{yu2025dapo} prevents entropy collapse, Dr.\\ GRPO \\citep{liu2025drgrpo} corrects length bias, $\\mu$-GRPO \\citep{tian2026mugrpo} improves off-policy efficiency, Tree-GRPO \\citep{ji2026treegrpo} extends GRPO to agentic settings, and multi-objective variants \\citep{liu2026gdpo,ito2025mogrpo} handle competing reward signals."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_reference-augmentation_20260524T192339",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/sections/related_work.tex",
    "old_string": "Subsequent work addresses failure modes: DAPO \\citep{yu2025dapo} prevents entropy collapse, Dr.\\ GRPO \\citep{liu2025drgrpo} corrects length bias, and multi-objective variants \\citep{liu2026gdpo,ito2025mogrpo} handle competing reward signals.",
    "new_string": "Subsequent work addresses failure modes: DAPO \\citep{yu2025dapo} prevents entropy collapse, Dr.\\ GRPO \\citep{liu2025drgrpo} corrects length bias, $\\mu$-GRPO \\citep{tian2026mugrpo} improves off-policy efficiency, Tree-GRPO \\citep{ji2026treegrpo} extends GRPO to agentic settings, and multi-objective variants \\citep{liu2026gdpo,ito2025mogrpo} handle competing reward signals."
  }
}
```

</details>

---

### Tool result

_source line 82 · 2026-05-24T19:35:53.982416+00:00_

&lt;tool_use_error>File has been modified since read, either by the user or by a linter. Read it again before attempting to write it.&lt;/tool_use_error>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_reference-augmentation_20260524T192339",
  "tool": "Edit",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 83 · 2026-05-24T19:35:53.982531+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/sections/related_work.tex",
  "old_string": "Direct Preference Optimization \\citep{rafailov2023direct} reformulates Reinforcement Learning from Human Feedback (RLHF) as implicit reward maximization.",
  "new_string": "Direct Preference Optimization \\citep{rafailov2023direct} reformulates Reinforcement Learning from Human Feedback \\citep[RLHF;][]{ouyang2022instructgpt} as implicit reward maximization; KTO \\citep{ethayarajh2024kto} further simplifies alignment by learning from binary desirability signals without paired preferences."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_reference-augmentation_20260524T192339",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/sections/related_work.tex",
    "old_string": "Direct Preference Optimization \\citep{rafailov2023direct} reformulates Reinforcement Learning from Human Feedback (RLHF) as implicit reward maximization.",
    "new_string": "Direct Preference Optimization \\citep{rafailov2023direct} reformulates Reinforcement Learning from Human Feedback \\citep[RLHF;][]{ouyang2022instructgpt} as implicit reward maximization; KTO \\citep{ethayarajh2024kto} further simplifies alignment by learning from binary desirability signals without paired preferences."
  }
}
```

</details>

---

### Tool result

_source line 84 · 2026-05-24T19:35:53.982649+00:00_

&lt;tool_use_error>File has been modified since read, either by the user or by a linter. Read it again before attempting to write it.&lt;/tool_use_error>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_reference-augmentation_20260524T192339",
  "tool": "Edit",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 85 · 2026-05-24T19:35:53.982768+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/sections/related_work.tex",
  "old_string": "amplified by QLoRA's constrained parameter space \\citep{gao2023scaling,moskovitz2024constrained}.",
  "new_string": "amplified by QLoRA's \\citep{dettmers2023qlora} constrained parameter space and capacity-dependent scaling dynamics \\citep{hoffmann2022chinchilla,gao2023scaling,moskovitz2024constrained,coste2024reward}."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_reference-augmentation_20260524T192339",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/sections/related_work.tex",
    "old_string": "amplified by QLoRA's constrained parameter space \\citep{gao2023scaling,moskovitz2024constrained}.",
    "new_string": "amplified by QLoRA's \\citep{dettmers2023qlora} constrained parameter space and capacity-dependent scaling dynamics \\citep{hoffmann2022chinchilla,gao2023scaling,moskovitz2024constrained,coste2024reward}."
  }
}
```

</details>

---

### Tool result

_source line 86 · 2026-05-24T19:35:53.982885+00:00_

&lt;tool_use_error>File has been modified since read, either by the user or by a linter. Read it again before attempting to write it.&lt;/tool_use_error>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_reference-augmentation_20260524T192339",
  "tool": "Edit",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 87 · 2026-05-24T19:35:53.982997+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/sections/related_work.tex",
  "old_string": "and \\citet{zhang2024infuse} introduce fine-grained NLI-based faithfulness metrics for summarization.",
  "new_string": "\\citet{zhang2024infuse} introduce fine-grained NLI-based faithfulness metrics for summarization, and EvidenceRL \\citep{tamo2026evidencerl} reinforces evidence consistency through GRPO-based optimization with grounding rewards."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_reference-augmentation_20260524T192339",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/sections/related_work.tex",
    "old_string": "and \\citet{zhang2024infuse} introduce fine-grained NLI-based faithfulness metrics for summarization.",
    "new_string": "\\citet{zhang2024infuse} introduce fine-grained NLI-based faithfulness metrics for summarization, and EvidenceRL \\citep{tamo2026evidencerl} reinforces evidence consistency through GRPO-based optimization with grounding rewards."
  }
}
```

</details>

---

### Tool result

_source line 88 · 2026-05-24T19:35:53.983110+00:00_

&lt;tool_use_error>File has been modified since read, either by the user or by a linter. Read it again before attempting to write it.&lt;/tool_use_error>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_reference-augmentation_20260524T192339",
  "tool": "Edit",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 89 · 2026-05-24T19:35:53.983222+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/sections/related_work.tex",
  "old_string": "\\citet{zelikman2022star} introduced STaR for iterative self-improvement; \\citet{dong2023raft} generalize this with reward-model-based sample filtering; recent analysis shows rejection sampling implicitly performs PPO-like optimization \\citep{tang2025rsftppo}.",
  "new_string": "\\citet{zelikman2022star} introduced STaR for iterative self-improvement; \\citet{yuan2023rft} demonstrate the scaling properties of rejection sampling fine-tuning; \\citet{dong2023raft} generalize with reward-model-based sample filtering; and recent analysis shows rejection sampling implicitly performs PPO-like optimization \\citep{tang2025rsftppo}. Extensions include RIFT \\citep{liu2026rift}, which repurposes rejected samples, and TrajFusion \\citep{deng2026trajfusion}, which fuses trajectories beyond simple selection."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_reference-augmentation_20260524T192339",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/sections/related_work.tex",
    "old_string": "\\citet{zelikman2022star} introduced STaR for iterative self-improvement; \\citet{dong2023raft} generalize this with reward-model-based sample filtering; recent analysis shows rejection sampling implicitly performs PPO-like optimization \\citep{tang2025rsftppo}.",
    "new_string": "\\citet{zelikman2022star} introduced STaR for iterative self-improvement; \\citet{yuan2023rft} demonstrate the scaling properties of rejection sampling fine-tuning; \\citet{dong2023raft} generalize with reward-model-based sample filtering; and recent analysis shows rejection sampling implicitly performs PPO-like optimization \\citep{tang2025rsftppo}. Extensions include RIFT \\citep{liu2026rift}, which repurposes rejected samples, and TrajFusion \\citep{deng2026trajfusion}, which fuses trajectories beyond simple selection."
  }
}
```

</details>

---

### Tool result

_source line 90 · 2026-05-24T19:35:53.983364+00:00_

&lt;tool_use_error>File has been modified since read, either by the user or by a linter. Read it again before attempting to write it.&lt;/tool_use_error>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_reference-augmentation_20260524T192339",
  "tool": "Edit",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 91 · 2026-05-24T19:35:53.983500+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/sections/related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_reference-augmentation_20260524T192339",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/sections/related_work.tex"
  }
}
```

</details>

---

### Tool result

_source line 92 · 2026-05-24T19:35:53.983651+00:00_

1	\section{Related Work}
2	\label{sec:related_work}
3	
4	Document-level relation extraction (DocRE) requires reasoning across sentence boundaries to identify relations between entity pairs.
5	DocRED \citep{yao2019docred} established the first large-scale benchmark for this task, catalyzing a line of encoder-based methods that treat DocRE as classification over entity pair representations.
6	ATLOP \citep{zhou2021atlop} introduced adaptive thresholding for multi-label prediction and localized context pooling for entity representations.
7	A parallel thread incorporates sentence-level evidence into these architectures.
8	SAIS \citep{xiao2022sais} introduced evidence supervision as an auxiliary training signal and showed that joint evidence prediction improves extraction through data augmentation and ensemble inference.
9	DREEAM \citep{ma2023dreeam} extended this approach with dynamic memory-based evidence retrieval that guides attention to supporting sentences.
10	EIDER \citep{xie2022eider} jointly trains an evidence extractor and fuses evidence representations into the relation classifier.
11	In all three systems, evidence identification is binary sentence classification over a fixed candidate set, a formulation that adds no output complexity.
12	Recent work has recast DocRE for large language models.
13	AutoRE \citep{autore2024} fine-tunes LLMs with QLoRA using a relation-head-facts decomposition; \citet{xu2024lmrc} frame extraction as multi-choice reading comprehension; RelPrior \citep{wang2025relprior} uses relation priors to guide LLM-based extraction; GLiDRE \citep{zhang2025glidre} presents a generalist lightweight approach; Ru-LLM \citep{wang2025rullm} incorporates logical rule constraints; and \citet{chen2025docksrag} combine retrieval-augmented generation with structured knowledge.
14	These methods match or surpass encoder baselines but produce bare triplets without evidence. Among LLM-based generative methods at the 8B scale, our RSFT model (54.33 Ign-F1 on Do
…[truncated 3251 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_reference-augmentation_20260524T192339",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 93 · 2026-05-24T19:35:53.983797+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/sections/method.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_reference-augmentation_20260524T192339",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/sections/method.tex"
  }
}
```

</details>

---

### Tool result

_source line 94 · 2026-05-24T19:35:53.983970+00:00_

1	\section{Method}
2	\label{sec:method}
3	
4	\begin{figure*}[t]
5	\centering
6	\includegraphics[width=0.92\textwidth]{fig_overview.pdf}
7	\vspace{-2mm}
8	\caption{Evidence-grounded DocRE produces relation triples with supporting sentence indices, unlike standard DocRE which outputs bare triples. RSFT selects the top-$k$ of $N$ CED-scored candidates per document for fine-tuning.}
9	\label{fig:overview}
10	\end{figure*}
11	
12	\subsection{Task: Evidence-Grounded Document-Level Relation Extraction}
13	\label{sec:task}
14	
15	Given a document $D = \{s_1, \ldots, s_n\}$ consisting of $n$ sentences and a set of entities $\mathcal{E}$ identified within $D$, the task of evidence-grounded document-level relation extraction (DocRE) requires predicting, for each entity pair $(e_h, e_t) \in \mathcal{E} \times \mathcal{E}$, a relation $r \in \mathcal{R} \cup \{\texttt{NA}\}$ together with a set of supporting evidence sentences $E \subseteq D$. Standard DocRE predicts only the triple $(e_h, r, e_t)$; the evidence-grounded formulation also requires $E$, which grounds each prediction in specific textual support (Figure~\ref{fig:overview}).
16	
17	In our LLM-based approach, the model generates structured outputs that jointly encode both components. For each predicted relation, the output follows the format \texttt{(head, relation, tail) | Evidence: [S$i$][S$j$]}, requiring the model to produce complete evidence references inline with each triple rather than as a separate retrieval step. This design contrasts with encoder-based evidence methods such as SAIS~\citep{xiao2022sais} and DREEAM~\citep{ma2023dreeam}, which frame evidence identification as sentence-level binary classification. Because classification over a fixed sentence set does not increase output length, these methods incur no generation overhead. Our LLM formulation requires additional tokens for each evidence reference, creating a generation burden that scales with the number of predicted triples and their evidence sent
…[truncated 9061 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_reference-augmentation_20260524T192339",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 95 · 2026-05-24T19:35:53.984147+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/sections/related_work.tex",
  "old_string": "ATLOP \\citep{zhou2021atlop} introduced adaptive thresholding for multi-label prediction and localized context pooling for entity representations.",
  "new_string": "ATLOP \\citep{zhou2021atlop} introduced adaptive thresholding with localized context pooling, and graph-based methods such as GAIN \\citep{zeng2020gain} model inter-sentence reasoning through heterogeneous mention-level and entity-level graphs."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_reference-augmentation_20260524T192339",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/sections/related_work.tex",
    "old_string": "ATLOP \\citep{zhou2021atlop} introduced adaptive thresholding for multi-label prediction and localized context pooling for entity representations.",
    "new_string": "ATLOP \\citep{zhou2021atlop} introduced adaptive thresholding with localized context pooling, and graph-based methods such as GAIN \\citep{zeng2020gain} model inter-sentence reasoning through heterogeneous mention-level and entity-level graphs."
  }
}
```

</details>

---

### Tool result

_source line 96 · 2026-05-24T19:35:53.984317+00:00_

The file /home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/sections/related_work.tex has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_reference-augmentation_20260524T192339",
  "tool": "Edit",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 97 · 2026-05-24T19:35:53.984447+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/sections/related_work.tex",
  "old_string": "Group Relative Policy Optimization (GRPO) \\citep{shao2024deepseekmath} eliminates the separate value network by computing advantages within groups.",
  "new_string": "Group Relative Policy Optimization (GRPO) \\citep{shao2024deepseekmath} replaces the value network of PPO \\citep{schulman2017ppo} by computing advantages within groups."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_reference-augmentation_20260524T192339",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/sections/related_work.tex",
    "old_string": "Group Relative Policy Optimization (GRPO) \\citep{shao2024deepseekmath} eliminates the separate value network by computing advantages within groups.",
    "new_string": "Group Relative Policy Optimization (GRPO) \\citep{shao2024deepseekmath} replaces the value network of PPO \\citep{schulman2017ppo} by computing advantages within groups."
  }
}
```

</details>

---

### Tool result

_source line 98 · 2026-05-24T19:35:53.984596+00:00_

The file /home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/sections/related_work.tex has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_reference-augmentation_20260524T192339",
  "tool": "Edit",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 99 · 2026-05-24T19:35:53.984718+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/sections/related_work.tex",
  "old_string": "Subsequent work addresses failure modes: DAPO \\citep{yu2025dapo} prevents entropy collapse, Dr.\\ GRPO \\citep{liu2025drgrpo} corrects length bias, and multi-objective variants \\citep{liu2026gdpo,ito2025mogrpo} handle competing reward signals.",
  "new_string": "Subsequent work addresses failure modes: DAPO \\citep{yu2025dapo} prevents entropy collapse, Dr.\\ GRPO \\citep{liu2025drgrpo} corrects length bias, $\\mu$-GRPO \\citep{tian2026mugrpo} improves off-policy efficiency, Tree-GRPO \\citep{ji2026treegrpo} extends GRPO to agentic settings, and multi-objective variants \\citep{liu2026gdpo,ito2025mogrpo} handle competing reward signals."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_reference-augmentation_20260524T192339",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/sections/related_work.tex",
    "old_string": "Subsequent work addresses failure modes: DAPO \\citep{yu2025dapo} prevents entropy collapse, Dr.\\ GRPO \\citep{liu2025drgrpo} corrects length bias, and multi-objective variants \\citep{liu2026gdpo,ito2025mogrpo} handle competing reward signals.",
    "new_string": "Subsequent work addresses failure modes: DAPO \\citep{yu2025dapo} prevents entropy collapse, Dr.\\ GRPO \\citep{liu2025drgrpo} corrects length bias, $\\mu$-GRPO \\citep{tian2026mugrpo} improves off-policy efficiency, Tree-GRPO \\citep{ji2026treegrpo} extends GRPO to agentic settings, and multi-objective variants \\citep{liu2026gdpo,ito2025mogrpo} handle competing reward signals."
  }
}
```

</details>

---

### Tool result

_source line 100 · 2026-05-24T19:35:53.984877+00:00_

The file /home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/sections/related_work.tex has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_reference-augmentation_20260524T192339",
  "tool": "Edit",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 101 · 2026-05-24T19:35:53.985008+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/sections/related_work.tex",
  "old_string": "Direct Preference Optimization \\citep{rafailov2023direct} reformulates Reinforcement Learning from Human Feedback (RLHF) as implicit reward maximization.",
  "new_string": "Direct Preference Optimization \\citep{rafailov2023direct} reformulates Reinforcement Learning from Human Feedback \\citep[RLHF;][]{ouyang2022instructgpt} as implicit reward maximization; KTO \\citep{ethayarajh2024kto} further simplifies alignment by learning from binary desirability signals without paired preferences."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_reference-augmentation_20260524T192339",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/sections/related_work.tex",
    "old_string": "Direct Preference Optimization \\citep{rafailov2023direct} reformulates Reinforcement Learning from Human Feedback (RLHF) as implicit reward maximization.",
    "new_string": "Direct Preference Optimization \\citep{rafailov2023direct} reformulates Reinforcement Learning from Human Feedback \\citep[RLHF;][]{ouyang2022instructgpt} as implicit reward maximization; KTO \\citep{ethayarajh2024kto} further simplifies alignment by learning from binary desirability signals without paired preferences."
  }
}
```

</details>

---

### Tool result

_source line 102 · 2026-05-24T19:35:53.985155+00:00_

The file /home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/sections/related_work.tex has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_reference-augmentation_20260524T192339",
  "tool": "Edit",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 103 · 2026-05-24T19:35:53.985296+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/sections/related_work.tex",
  "old_string": "amplified by QLoRA's constrained parameter space \\citep{gao2023scaling,moskovitz2024constrained}.",
  "new_string": "amplified by QLoRA's \\citep{dettmers2023qlora} constrained parameter space and capacity-dependent scaling dynamics \\citep{hoffmann2022chinchilla,gao2023scaling,moskovitz2024constrained,coste2024reward}."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_reference-augmentation_20260524T192339",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/sections/related_work.tex",
    "old_string": "amplified by QLoRA's constrained parameter space \\citep{gao2023scaling,moskovitz2024constrained}.",
    "new_string": "amplified by QLoRA's \\citep{dettmers2023qlora} constrained parameter space and capacity-dependent scaling dynamics \\citep{hoffmann2022chinchilla,gao2023scaling,moskovitz2024constrained,coste2024reward}."
  }
}
```

</details>

---

### Tool result

_source line 104 · 2026-05-24T19:35:53.985446+00:00_

The file /home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/sections/related_work.tex has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_reference-augmentation_20260524T192339",
  "tool": "Edit",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 105 · 2026-05-24T19:35:53.985567+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/sections/related_work.tex",
  "old_string": "and \\citet{zhang2024infuse} introduce fine-grained NLI-based faithfulness metrics for summarization.",
  "new_string": "\\citet{zhang2024infuse} introduce fine-grained NLI-based faithfulness metrics for summarization, and EvidenceRL \\citep{tamo2026evidencerl} reinforces evidence consistency through GRPO-based optimization with grounding rewards."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_reference-augmentation_20260524T192339",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/sections/related_work.tex",
    "old_string": "and \\citet{zhang2024infuse} introduce fine-grained NLI-based faithfulness metrics for summarization.",
    "new_string": "\\citet{zhang2024infuse} introduce fine-grained NLI-based faithfulness metrics for summarization, and EvidenceRL \\citep{tamo2026evidencerl} reinforces evidence consistency through GRPO-based optimization with grounding rewards."
  }
}
```

</details>

---

### Tool result

_source line 106 · 2026-05-24T19:35:53.985710+00:00_

The file /home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/sections/related_work.tex has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_reference-augmentation_20260524T192339",
  "tool": "Edit",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 107 · 2026-05-24T19:35:53.985833+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/sections/related_work.tex",
  "old_string": "\\citet{zelikman2022star} introduced STaR for iterative self-improvement; \\citet{dong2023raft} generalize this with reward-model-based sample filtering; recent analysis shows rejection sampling implicitly performs PPO-like optimization \\citep{tang2025rsftppo}.",
  "new_string": "\\citet{zelikman2022star} introduced STaR for iterative self-improvement; \\citet{yuan2023rft} demonstrate the scaling properties of rejection sampling fine-tuning; \\citet{dong2023raft} generalize with reward-model-based sample filtering; and recent analysis shows rejection sampling implicitly performs PPO-like optimization \\citep{tang2025rsftppo}. Extensions include RIFT \\citep{liu2026rift}, which repurposes rejected samples, and TrajFusion \\citep{deng2026trajfusion}, which fuses trajectories beyond simple selection."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_reference-augmentation_20260524T192339",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/sections/related_work.tex",
    "old_string": "\\citet{zelikman2022star} introduced STaR for iterative self-improvement; \\citet{dong2023raft} generalize this with reward-model-based sample filtering; recent analysis shows rejection sampling implicitly performs PPO-like optimization \\citep{tang2025rsftppo}.",
    "new_string": "\\citet{zelikman2022star} introduced STaR for iterative self-improvement; \\citet{yuan2023rft} demonstrate the scaling properties of rejection sampling fine-tuning; \\citet{dong2023raft} generalize with reward-model-based sample filtering; and recent analysis shows rejection sampling implicitly performs PPO-like optimization \\citep{tang2025rsftppo}. Extensions include RIFT \\citep{liu2026rift}, which repurposes rejected samples, and TrajFusion \\citep{deng2026trajfusion}, which fuses trajectories beyond simple selection."
  }
}
```

</details>

---

### Tool result

_source line 108 · 2026-05-24T19:35:53.985988+00:00_

The file /home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/sections/related_work.tex has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_reference-augmentation_20260524T192339",
  "tool": "Edit",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 109 · 2026-05-24T19:35:53.986128+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/sections/method.tex",
  "old_string": "We test two configurations: QLoRA (quantized LoRA) with $G{=}4$ groups under 4-bit quantization",
  "new_string": "We test two configurations: QLoRA \\citep{dettmers2023qlora} with $G{=}4$ groups under 4-bit quantization"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_reference-augmentation_20260524T192339",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/sections/method.tex",
    "old_string": "We test two configurations: QLoRA (quantized LoRA) with $G{=}4$ groups under 4-bit quantization",
    "new_string": "We test two configurations: QLoRA \\citep{dettmers2023qlora} with $G{=}4$ groups under 4-bit quantization"
  }
}
```

</details>

---

### Tool result

_source line 110 · 2026-05-24T19:35:53.986300+00:00_

The file /home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/sections/method.tex has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_reference-augmentation_20260524T192339",
  "tool": "Edit",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 111 · 2026-05-24T19:35:53.986427+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/sections/method.tex",
  "old_string": "An NLI model (\\texttt{cross-encoder/nli-deberta-v3-base}) produces an entailment probability $p^+$ for this pair.",
  "new_string": "An NLI model based on DeBERTaV3 \\citep{he2023debertav3} (\\texttt{cross-encoder/nli-deberta-v3-base}) produces an entailment probability $p^+$ for this pair."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_reference-augmentation_20260524T192339",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/sections/method.tex",
    "old_string": "An NLI model (\\texttt{cross-encoder/nli-deberta-v3-base}) produces an entailment probability $p^+$ for this pair.",
    "new_string": "An NLI model based on DeBERTaV3 \\citep{he2023debertav3} (\\texttt{cross-encoder/nli-deberta-v3-base}) produces an entailment probability $p^+$ for this pair."
  }
}
```

</details>

---

### Tool result

_source line 112 · 2026-05-24T19:35:53.986581+00:00_

The file /home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/sections/method.tex has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_reference-augmentation_20260524T192339",
  "tool": "Edit",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 113 · 2026-05-24T19:35:53.986702+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/sections/method.tex",
  "old_string": "Direct Preference Optimization~\\citep{rafailov2023direct} reformulates RLHF as a classification problem over preference pairs, without explicit reward models.",
  "new_string": "Direct Preference Optimization~\\citep{rafailov2023direct} reformulates RLHF~\\citep{ouyang2022instructgpt} as a classification problem over preference pairs, without explicit reward models."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_reference-augmentation_20260524T192339",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/sections/method.tex",
    "old_string": "Direct Preference Optimization~\\citep{rafailov2023direct} reformulates RLHF as a classification problem over preference pairs, without explicit reward models.",
    "new_string": "Direct Preference Optimization~\\citep{rafailov2023direct} reformulates RLHF~\\citep{ouyang2022instructgpt} as a classification problem over preference pairs, without explicit reward models."
  }
}
```

</details>

---

### Tool result

_source line 114 · 2026-05-24T19:35:53.986858+00:00_

The file /home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/sections/method.tex has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_reference-augmentation_20260524T192339",
  "tool": "Edit",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 115 · 2026-05-24T19:35:53.986988+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper && pdflatex -interaction=nonstopmode main.tex 2>&1 | tail -30",
  "description": "First pdflatex pass"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_reference-augmentation_20260524T192339",
  "tool": "Bash",
  "tool_args": {
    "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper && pdflatex -interaction=nonstopmode main.tex 2>&1 | tail -30",
    "description": "First pdflatex pass"
  }
}
```

</details>

---

### Tool result

_source line 116 · 2026-05-24T19:35:53.987117+00:00_

Package natbib Warning: There were undefined citations.

[18] (./main.aux)

LaTeX Warning: Label(s) may have changed. Rerun to get cross-references right.

 )
(see the transcript file for additional information)&lt;/usr/share/texlive/texmf-d
ist/fonts/type1/public/inconsolata/Inconsolata-zi4r.pfb>&lt;/usr/share/texlive/tex
mf-dist/fonts/type1/public/amsfonts/cm/cmex10.pfb>&lt;/usr/share/texlive/texmf-dis
t/fonts/type1/public/amsfonts/cm/cmmi10.pfb>&lt;/usr/share/texlive/texmf-dist/font
s/type1/public/amsfonts/cm/cmmi6.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1
/public/amsfonts/cm/cmmi7.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public
/amsfonts/cm/cmmi8.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfon
ts/cm/cmmi9.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/c
mr10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr6.pfb
>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr7.pfb>&lt;/usr/s
hare/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr8.pfb>&lt;/usr/share/tex
live/texmf-dist/fonts/type1/public/amsfonts/cm/cmr9.pfb>&lt;/usr/share/texlive/tex
mf-dist/fonts/type1/public/amsfonts/cm/cmsy10.pfb>&lt;/usr/share/texlive/texmf-dis
t/fonts/type1/public/amsfonts/cm/cmsy6.pfb>&lt;/usr/share/texlive/texmf-dist/fonts
/type1/public/amsfonts/cm/cmsy7.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/
public/amsfonts/cm/cmsy8.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/
amsfonts/cm/cmsy9.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/urw/helvetic/u
hvb8a.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/urw/times/utmb8a.pfb>&lt;/usr
/share/texlive/texmf-dist/fonts/type1/urw/times/utmr8a.pfb>&lt;/usr/share/texlive/
texmf-dist/fonts/type1/urw/times/utmri8a.pfb>
Output written on main.pdf (18 pages, 811523 bytes).
Transcript written on main.log.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_reference-augmentation_20260524T192339",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 117 · 2026-05-24T19:35:53.987265+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "bibtex main 2>&1",
  "description": "Run bibtex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_reference-augmentation_20260524T192339",
  "tool": "Bash",
  "tool_args": {
    "command": "bibtex main 2>&1",
    "description": "Run bibtex"
  }
}
```

</details>

---

### Tool result

_source line 118 · 2026-05-24T19:35:53.987389+00:00_

This is BibTeX, Version 0.99d (TeX Live 2025/Debian)
The top-level auxiliary file: main.aux
The style file: acl_natbib.bst
Database file #1: references.bib

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_reference-augmentation_20260524T192339",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 119 · 2026-05-24T19:35:53.987505+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "pdflatex -interaction=nonstopmode main.tex 2>&1 | grep -i \"warning\\|error\\|undefined\" | head -20",
  "description": "Second pdflatex pass checking for warnings"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_reference-augmentation_20260524T192339",
  "tool": "Bash",
  "tool_args": {
    "command": "pdflatex -interaction=nonstopmode main.tex 2>&1 | grep -i \"warning\\|error\\|undefined\" | head -20",
    "description": "Second pdflatex pass checking for warnings"
  }
}
```

</details>

---

### Tool result

_source line 120 · 2026-05-24T19:35:53.987629+00:00_

Package natbib Warning: Citation `zeng2020gain' on page 2 undefined on input li
Package natbib Warning: Citation `schulman2017ppo' on page 2 undefined on input
Package natbib Warning: Citation `tian2026mugrpo' on page 2 undefined on input 
Package natbib Warning: Citation `ji2026treegrpo' on page 2 undefined on input 
Package natbib Warning: Citation `ouyang2022instructgpt' on page 2 undefined on
Package natbib Warning: Citation `ethayarajh2024kto' on page 2 undefined on inp
Package natbib Warning: Citation `dettmers2023qlora' on page 2 undefined on inp
Package natbib Warning: Citation `hoffmann2022chinchilla' on page 2 undefined o
Package natbib Warning: Citation `coste2024reward' on page 2 undefined on input
Package natbib Warning: Citation `tamo2026evidencerl' on page 3 undefined on in
Package natbib Warning: Citation `yuan2023rft' on page 3 undefined on input lin
Package natbib Warning: Citation `liu2026rift' on page 3 undefined on input lin
Package natbib Warning: Citation `deng2026trajfusion' on page 3 undefined on in
Package natbib Warning: Citation `dettmers2023qlora' on page 4 undefined on inp
Package natbib Warning: Citation `ouyang2022instructgpt' on page 4 undefined on
Package natbib Warning: Citation `he2023debertav3' on page 5 undefined on input
Package lineno Warning: Line number reference failed, re-run to get it right.
Package natbib Warning: There were undefined citations.
Package natbib Warning: Citation(s) may have changed.
LaTeX Warning: Label(s) may have changed. Rerun to get cross-references right.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_reference-augmentation_20260524T192339",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 121 · 2026-05-24T19:35:53.987786+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "pdflatex -interaction=nonstopmode main.tex > /dev/null 2>&1 && bibtex main 2>&1 && pdflatex -interaction=nonstopmode main.tex > /dev/null 2>&1 && pdflatex -interaction=nonstopmode main.tex 2>&1 | grep -iE \"warning|error|undefined\" | head -20",
  "description": "Full LaTeX compile cycle"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_reference-augmentation_20260524T192339",
  "tool": "Bash",
  "tool_args": {
    "command": "pdflatex -interaction=nonstopmode main.tex > /dev/null 2>&1 && bibtex main 2>&1 && pdflatex -interaction=nonstopmode main.tex > /dev/null 2>&1 && pdflatex -interaction=nonstopmode main.tex 2>&1 | grep -iE \"warning|error|undefined\" | head -20",
    "description": "Full LaTeX compile cycle"
  }
}
```

</details>

---

### Tool result

_source line 122 · 2026-05-24T19:35:53.987918+00:00_

This is BibTeX, Version 0.99d (TeX Live 2025/Debian)
The top-level auxiliary file: main.aux
The style file: acl_natbib.bst
Database file #1: references.bib

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_reference-augmentation_20260524T192339",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 123 · 2026-05-24T19:35:53.988034+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "pdflatex -interaction=nonstopmode main.tex 2>&1 | grep -ciE \"undefined citation\"",
  "description": "Final check for undefined citations"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_reference-augmentation_20260524T192339",
  "tool": "Bash",
  "tool_args": {
    "command": "pdflatex -interaction=nonstopmode main.tex 2>&1 | grep -ciE \"undefined citation\"",
    "description": "Final check for undefined citations"
  }
}
```

</details>

---

### Tool result

_source line 124 · 2026-05-24T19:35:53.988147+00:00_

0

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_reference-augmentation_20260524T192339",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 125 · 2026-05-24T19:35:53.988285+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "grep -c \"^@\" /home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/references.bib",
  "description": "Count bib entries"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_reference-augmentation_20260524T192339",
  "tool": "Bash",
  "tool_args": {
    "command": "grep -c \"^@\" /home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/references.bib",
    "description": "Count bib entries"
  }
}
```

</details>

---

### Tool result

_source line 126 · 2026-05-24T19:35:53.988402+00:00_

50

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_reference-augmentation_20260524T192339",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 127 · 2026-05-24T19:35:53.988522+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/sections/related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_reference-augmentation_20260524T192339",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/sections/related_work.tex"
  }
}
```

</details>

---

### Tool result

_source line 128 · 2026-05-24T19:35:53.988668+00:00_

1	\section{Related Work}
2	\label{sec:related_work}
3	
4	Document-level relation extraction (DocRE) requires reasoning across sentence boundaries to identify relations between entity pairs.
5	DocRED \citep{yao2019docred} established the first large-scale benchmark for this task, catalyzing a line of encoder-based methods that treat DocRE as classification over entity pair representations.
6	ATLOP \citep{zhou2021atlop} introduced adaptive thresholding with localized context pooling, and graph-based methods such as GAIN \citep{zeng2020gain} model inter-sentence reasoning through heterogeneous mention-level and entity-level graphs.
7	A parallel thread incorporates sentence-level evidence into these architectures.
8	SAIS \citep{xiao2022sais} introduced evidence supervision as an auxiliary training signal and showed that joint evidence prediction improves extraction through data augmentation and ensemble inference.
9	DREEAM \citep{ma2023dreeam} extended this approach with dynamic memory-based evidence retrieval that guides attention to supporting sentences.
10	EIDER \citep{xie2022eider} jointly trains an evidence extractor and fuses evidence representations into the relation classifier.
11	In all three systems, evidence identification is binary sentence classification over a fixed candidate set, a formulation that adds no output complexity.
12	Recent work has recast DocRE for large language models.
13	AutoRE \citep{autore2024} fine-tunes LLMs with QLoRA using a relation-head-facts decomposition; \citet{xu2024lmrc} frame extraction as multi-choice reading comprehension; RelPrior \citep{wang2025relprior} uses relation priors to guide LLM-based extraction; GLiDRE \citep{zhang2025glidre} presents a generalist lightweight approach; Ru-LLM \citep{wang2025rullm} incorporates logical rule constraints; and \citet{chen2025docksrag} combine retrieval-augmented generation with structured knowledge.
14	These methods match or surpass encoder baselines but produce bare triplets without
…[truncated 4158 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_reference-augmentation_20260524T192339",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 129 · 2026-05-24T19:35:53.988879+00:00_

All edits applied cleanly. Compilation succeeded with 0 undefined citations and 50 total bib entries.

**Summary of 14 added references:**

**Classic/Important (9):**
| # | Bib Key | Paper | Year | Venue |
|---|---------|-------|------|-------|
| 1 | `ouyang2022instructgpt` | Training Language Models to Follow Instructions with Human Feedback | 2022 | NeurIPS |
| 2 | `schulman2017ppo` | Proximal Policy Optimization Algorithms | 2017 | arXiv |
| 3 | `zeng2020gain` | Double Graph Based Reasoning for Document-level Relation Extraction (GAIN) | 2020 | EMNLP |
| 4 | `ethayarajh2024kto` | KTO: Model Alignment as Prospect Theoretic Optimization | 2024 | ICML |
| 5 | `coste2024reward` | Reward Model Ensembles Help Mitigate Overoptimization | 2024 | ICLR |
| 6 | `he2023debertav3` | DeBERTaV3: Improving DeBERTa using ELECTRA-Style Pre-Training | 2023 | ICLR |
| 7 | `dettmers2023qlora` | QLoRA: Efficient Finetuning of Quantized LLMs | 2023 | NeurIPS |
| 8 | `hoffmann2022chinchilla` | Training Compute-Optimal Large Language Models (Chinchilla) | 2022 | NeurIPS |
| 9 | `yuan2023rft` | Scaling Relationship on Learning Mathematical Reasoning with LLMs | 2023 | arXiv |

**2026 (5):**
| # | Bib Key | Paper | Year | Source |
|---|---------|-------|------|--------|
| 10 | `tamo2026evidencerl` | EvidenceRL: Reinforcing Evidence Consistency for Trustworthy LMs | 2026 | arXiv 2603.19532 |
| 11 | `liu2026rift` | RIFT: Repurposing Negative Samples via Reward-Informed Fine-Tuning | 2026 | arXiv 2601.09253 |
| 12 | `deng2026trajfusion` | Beyond Rejection Sampling: Trajectory Fusion for Scaling Mathematical Reasoning | 2026 | arXiv 2602.04391 |
| 13 | `tian2026mugrpo` | How Off-Policy Can GRPO Be? Mu-GRPO for Efficient LLM RL | 2026 | arXiv 2605.17570 |
| 14 | `ji2026treegrpo` | Tree Search for LLM Agent Reinforcement Learning | 2026 | ICLR |

**Citation locations:**
- **Related Work**: GAIN, PPO, Mu-GRPO, Tree-GRPO, RLHF/InstructGPT, KTO, QLoRA, Chinchilla, Coste, EvidenceRL, Yuan RFT, RIFT, TrajFusion
- **Method**: QLoRA (GRPO paragraph), DeBERTaV3 (CED/NLI model), RLHF/InstructGPT (DPO paragraph)

Total references: 36 → 50. All 14 papers verified via WebSearch/WebFetch. Compilation clean with no undefined citations.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_paper_reference-augmentation_20260524T192339"
}
```

</details>

---
