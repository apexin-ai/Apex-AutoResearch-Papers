# writing related work completeness

**Generational Depth Estimation of Recursive Synthetic Text: Measuring the Discrimination Boundary** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 35
- **Recorded user turns:** 0
- **Tool calls:** 17
- **Original source:** `logs/chats/worker_writing_related-work-completeness_20260514T054916.jsonl`
- **Structured JSON:** [`f5cd6afbcc86088e38bf.json`](../../sessions/f5/f5cd6afbcc86088e38bf.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

35 recorded events

### Tool call

_source line 1 · 2026-05-14T05:52:24.786468+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/*.tex",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_writing_related-work-completeness_20260514T054916",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/*.tex",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper"
  }
}
```

</details>

---

### Tool result

_source line 2 · 2026-05-14T05:52:24.786851+00:00_

docs/paper/experiments_c1.tex
docs/paper/introduction.tex
docs/paper/conclusion.tex
docs/paper/related_work.tex
docs/paper/method.tex
docs/paper/appendix.tex
docs/paper/main.tex
docs/paper/discussion.tex

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_writing_related-work-completeness_20260514T054916",
  "tool": "Glob",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-14T05:52:24.787043+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/*.bib",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_writing_related-work-completeness_20260514T054916",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/*.bib",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper"
  }
}
```

</details>

---

### Tool result

_source line 4 · 2026-05-14T05:52:24.787182+00:00_

docs/paper/references.bib

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_writing_related-work-completeness_20260514T054916",
  "tool": "Glob",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-14T05:52:24.787306+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "\\\\cite[pt]?\\{[^}]+\\}",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper",
  "output_mode": "content",
  "glob": "*.tex",
  "-n": "True",
  "head_limit": "0"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_writing_related-work-completeness_20260514T054916",
  "tool": "Grep",
  "tool_args": {
    "pattern": "\\\\cite[pt]?\\{[^}]+\\}",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper",
    "output_mode": "content",
    "glob": "*.tex",
    "-n": "True",
    "head_limit": "0"
  }
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-14T05:52:24.787467+00:00_

docs/paper/related_work.tex:6:Shumailov et al.~\cite{shumailov2024collapse} showed that iteratively training language models on their own outputs leads to irreversible tail-distribution degradation, with minority modes vanishing across generations.
docs/paper/related_work.tex:7:Alemohammad et al.~\cite{alemohammad2024selfconsuming} formalized this for self-consuming generative models, proving convergence to a fixed point under mild regularity conditions.
docs/paper/related_work.tex:8:Dohmatob et al.~\cite{dohmatob2024model} derived scaling laws for collapse, demonstrating that tail probability mass is lost at rates predictable from model and data scale.
docs/paper/related_work.tex:9:Schaeffer et al.~\cite{schaeffer2025position} organized the fragmented literature into a taxonomy of eight definitions across three families.
docs/paper/related_work.tex:11:Kazdan et al.~\cite{kazdan2025collapse} distinguished \emph{replace} and \emph{accumulate} regimes: in the replace regime each generation completely supplants its predecessor, producing faster collapse.
docs/paper/related_work.tex:13:Shi et al.~\cite{shi2025generalization} identified a generalization-to-memorization transition in recursively trained models, providing cross-modal evidence that information loss is progressive.
docs/paper/related_work.tex:14:Gerstgrasser et al.~\cite{gerstgrasser2024inevitable} proved that collapse is avoidable when sufficient original data is retained alongside synthetic samples, a condition that depth-aware curation can enforce by construction.
docs/paper/related_work.tex:19:Early statistical approaches such as GLTR~\cite{gehrmann2019gltr} visualized per-token likelihood ranks to help human annotators spot generated text, establishing that token-level distributional cues are informative for detection.
docs/paper/related_work.tex:20:Zellers et al.~\cite{zellers2019grover} demonstrated that the generating model itself is an effective detector, while Ippolito et al.~\cite{ippolito2020dete
…[truncated 6536 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_writing_related-work-completeness_20260514T054916",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-14T05:52:24.787622+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/references.bib"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_writing_related-work-completeness_20260514T054916",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/references.bib"
  }
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-14T05:52:24.787855+00:00_

1	% === References for gen-depth-contamination ===
2	% Source: literature_map.yaml — verified 2026-05-14
3	
4	% === Must-Cite ===
5	
6	@inproceedings{drayson2025,
7	  title={Machine-Generated Text Detection Prevents Language Model Collapse},
8	  author={Drayson, George and Yilmaz, Emine and Lampos, Vasileios},
9	  booktitle={Proceedings of EMNLP},
10	  year={2025},
11	  url={https://arxiv.org/abs/2502.15654}
12	}
13	
14	@inproceedings{schaeffer2025position,
15	  title={Position: Model Collapse Does Not Mean What You Think},
16	  author={Schaeffer, Rylan and Kazdan, Joshua and Arulandu, Anirudh and Koyejo, Sanmi},
17	  booktitle={Proceedings of ICML},
18	  year={2025},
19	  url={https://arxiv.org/abs/2503.03150}
20	}
21	
22	@inproceedings{kazdan2025collapse,
23	  title={Collapse or Thrive? Perils and Promises of Synthetic Data in a Self-Generating World},
24	  author={Kazdan, Joshua and Schaeffer, Rylan and Dey, Apratim and Gerstgrasser, Matthias and Rafailov, Rafael and Donoho, David and Koyejo, Sanmi},
25	  booktitle={Proceedings of ICML},
26	  year={2025},
27	  url={https://arxiv.org/abs/2410.16713}
28	}
29	
30	@inproceedings{shi2025generalization,
31	  title={A Closer Look at Model Collapse: From a Generalization-to-Memorization Perspective},
32	  author={Shi, Lianghe and Wu, Meng and Zhang, Huijie and Zhang, Zekai and Tao, Molei and Qu, Qing},
33	  booktitle={Advances in NeurIPS},
34	  year={2025},
35	  note={Spotlight},
36	  url={https://arxiv.org/abs/2509.16499}
37	}
38	
39	@inproceedings{mitchell2023detectgpt,
40	  title={{DetectGPT}: Zero-Shot Machine-Generated Text Detection using Probability Curvature},
41	  author={Mitchell, Eric and Lee, Yoonho and Khazatsky, Alexander and Manning, Christopher D. and Finn, Chelsea},
42	  booktitle={Proceedings of ICML},
43	  year={2023}
44	}
45	
46	% === Should-Cite ===
47	
48	@article{basani2026diveye,
49	  title={{DivEye}: Diversity Boosts {AI}-Generated Text Detection},
50	  author={Basani, Advik Raj and Chen, Pin-Yu}
…[truncated 6933 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_writing_related-work-completeness_20260514T054916",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-14T05:52:24.788024+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_writing_related-work-completeness_20260514T054916",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/related_work.tex"
  }
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-14T05:52:24.788192+00:00_

1	\section{Related Work}
2	\label{sec:related_work}
3	
4	\paragraph{Model Collapse and Recursive Generation.}
5	Training on model-generated data can cause progressive distribution shift known as \emph{model collapse}.
6	Shumailov et al.~\cite{shumailov2024collapse} showed that iteratively training language models on their own outputs leads to irreversible tail-distribution degradation, with minority modes vanishing across generations.
7	Alemohammad et al.~\cite{alemohammad2024selfconsuming} formalized this for self-consuming generative models, proving convergence to a fixed point under mild regularity conditions.
8	Dohmatob et al.~\cite{dohmatob2024model} derived scaling laws for collapse, demonstrating that tail probability mass is lost at rates predictable from model and data scale.
9	Schaeffer et al.~\cite{schaeffer2025position} organized the fragmented literature into a taxonomy of eight definitions across three families.
10	Our $\Kstar$ aligns with their Family~B (distributional deformation), specifically D4 (collapsing variance) and D6 (mode entanglement)---the features that degrade most rapidly in our experiments are precisely variance-based surprisal measures.
11	Kazdan et al.~\cite{kazdan2025collapse} distinguished \emph{replace} and \emph{accumulate} regimes: in the replace regime each generation completely supplants its predecessor, producing faster collapse.
12	Our prompt-chain protocol operates in the replace regime, so $\Kempirical = 2$ is a conservative lower bound; the accumulate regime would yield slower degradation and higher $\Kstar$.
13	Shi et al.~\cite{shi2025generalization} identified a generalization-to-memorization transition in recursively trained models, providing cross-modal evidence that information loss is progressive.
14	Gerstgrasser et al.~\cite{gerstgrasser2024inevitable} proved that collapse is avoidable when sufficient original data is retained alongside synthetic samples, a condition that depth-aware curation can enforce by constru
…[truncated 6904 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_writing_related-work-completeness_20260514T054916",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-14T05:52:24.788374+00:00_

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
  "session": "worker_writing_related-work-completeness_20260514T054916",
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

_source line 12 · 2026-05-14T05:52:24.788500+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_writing_related-work-completeness_20260514T054916",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-14T05:52:24.788617+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "model collapse recursive LLM generation depth 2024 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_writing_related-work-completeness_20260514T054916",
  "tool": "WebSearch",
  "tool_args": {
    "query": "model collapse recursive LLM generation depth 2024 2025 2026"
  }
}
```

</details>

---

### Tool call

_source line 14 · 2026-05-14T05:52:24.788732+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "synthetic text detection benchmark machine-generated text 2024 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_writing_related-work-completeness_20260514T054916",
  "tool": "WebSearch",
  "tool_args": {
    "query": "synthetic text detection benchmark machine-generated text 2024 2025 2026"
  }
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-14T05:52:24.788898+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "data contamination depth iterative paraphrase detection 2024 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_writing_related-work-completeness_20260514T054916",
  "tool": "WebSearch",
  "tool_args": {
    "query": "data contamination depth iterative paraphrase detection 2024 2025 2026"
  }
}
```

</details>

---

### Tool call

_source line 16 · 2026-05-14T05:52:24.789024+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "generational depth estimation recursive text generation detection 2024 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_writing_related-work-completeness_20260514T054916",
  "tool": "WebSearch",
  "tool_args": {
    "query": "generational depth estimation recursive text generation detection 2024 2025"
  }
}
```

</details>

---

### Tool result

_source line 17 · 2026-05-14T05:52:24.789165+00:00_

Web search results for query: "synthetic text detection benchmark machine-generated text 2024 2025 2026"

Links: [{"title":"Diversity Boosts AI-Generated Text Detection","url":"https://arxiv.org/pdf/2509.18880"},{"title":"AI Text Detection Benchmarks 2025: Top Performance Metrics","url":"https://hastewire.com/blog/ai-text-detection-benchmarks-2025-top-performance-metrics"},{"title":"DetectRL: Benchmarking LLM-Generated Text Detection in Real-World Scenarios | OpenReview","url":"https://openreview.net/forum?id=ZGMkOikEyv"},{"title":"Beyond Easy Wins: A Text Hardness-Aware Benchmark for LLM-generated Text Detection","url":"https://arxiv.org/html/2507.15286v1"},{"title":"Benchmarking AI Text Detection: Assessing Detectors ...","url":"https://aclanthology.org/2025.genaidetect-1.4.pdf"},{"title":"MGTBench: Benchmarking Machine-Generated Text Detection | Proceedings of the 2024 on ACM SIGSAC Conference on Computer and Communications Security","url":"https://dl.acm.org/doi/10.1145/3658644.3670344"},{"title":"Spotlights and Blindspots: Evaluating Machine-Generated Text Detection","url":"https://arxiv.org/html/2604.16607v1"},{"title":"A Comprehensive Dataset for Human vs. AI Generated Text Detection","url":"https://arxiv.org/html/2510.22874v1"},{"title":"DetectRL: Benchmarking LLM-Generated Text Detection in Real-World Scenarios","url":"https://proceedings.neurips.cc/paper_files/paper/2024/file/b61bdf7e9f64c04ec75a26e781e2ad51-Paper-Datasets_and_Benchmarks_Track.pdf"},{"title":"AI Detection Benchmark 2025: Top Accuracy Results","url":"https://hastewire.com/blog/ai-detection-benchmark-2025-top-accuracy-results"}]

Based on the web search results, here's what I found about synthetic text detection benchmarks and machine-generated text detection from 2024-2026:

## Key Benchmarks

DetectRL is a new benchmark that includes popular LLMs, abuse-prone domains, well-designed attacks, and varying text lengths. Even state-of-the-art (SOTA) detection techniques still underperformed in 
…[truncated 1092 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_writing_related-work-completeness_20260514T054916",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-14T05:52:24.789349+00:00_

Web search results for query: "model collapse recursive LLM generation depth 2024 2025 2026"

Links: [{"title":"AI models collapse when trained on recursively generated data | Nature","url":"https://www.nature.com/articles/s41586-024-07566-y"},{"title":"AI models collapse when trained on recursively generated data - PubMed","url":"https://pubmed.ncbi.nlm.nih.gov/39048682/"},{"title":"Model collapse - Wikipedia","url":"https://en.wikipedia.org/wiki/Model_collapse"},{"title":"Future of AI Models: A Computational perspective on Model collapse","url":"https://arxiv.org/pdf/2511.05535"},{"title":"The AI Model Collapse Risk is Not Solved in 2025","url":"https://www.winssolutions.org/ai-model-collapse-2025-recursive-training/"},{"title":"AI models collapse when trained on recursively generated data","url":"https://vittoriodublinoblog.org/wp-content/uploads/2025/07/ai-models-collapse-when-trained-on-recursively-generated-data.pdf"},{"title":"[2511.05535] Future of AI Models: A Computational perspective on Model collapse","url":"https://arxiv.org/abs/2511.05535"},{"title":"BEYOND MODEL COLLAPSE: SCALING UP WITH SYN","url":"https://openreview.net/pdf?id=MQXrTMonT1"},{"title":"[2305.17493] The Curse of Recursion: Training on Generated Data Makes Models Forget","url":"https://arxiv.org/abs/2305.17493"},{"title":"Model Collapse Demystified: The Case of Regression","url":"https://arxiv.org/html/2402.07712v1"}]

I've found comprehensive information about model collapse and recursive LLM generation. Here are the key findings:

## What is Model Collapse?

Model collapse can occur in LLMs as well as in variational autoencoders (VAEs) and Gaussian mixture models (GMMs). Training generative artificial intelligence on real and generated content can lead to a collapse in the ability of the models to generate diverse high-quality output.

## How It Works

Model collapse is a degenerative process whereby, over time, models forget the true underlying data distribution when learning indiscri
…[truncated 1252 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_writing_related-work-completeness_20260514T054916",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 19 · 2026-05-14T05:52:24.789524+00:00_

Web search results for query: "data contamination depth iterative paraphrase detection 2024 2025 2026"

Links: [{"title":"A Comprehensive Survey of Contamination Detection Methods in Large Language Models","url":"https://arxiv.org/html/2404.00699v4"},{"title":"A Survey on Data Contamination for Large Language Models","url":"https://arxiv.org/html/2502.14425v1"},{"title":"Perturb Your Data: Paraphrase-Guided Training Data Watermarking","url":"https://arxiv.org/pdf/2512.17075"},{"title":"Detecting Data Contamination in LLMs via In-Context Learning","url":"https://arxiv.org/html/2510.27055v1"},{"title":"Benchmarking Large Language Models Under Data Contamination: A Survey from Static to Dynamic Evaluation","url":"https://arxiv.org/html/2502.17521v2"},{"title":"GitHub - lyy1994/awesome-data-contamination: The Paper List on Data Contamination for Large Language Models Evaluation. · GitHub","url":"https://github.com/lyy1994/awesome-data-contamination"},{"title":"Evading Data Contamination Detection for Language Models is (too) Easy | OpenReview","url":"https://openreview.net/forum?id=Nk1MegaPuG"},{"title":"A Survey on Data Contamination for Large Language Models","url":"https://openreview.net/pdf?id=O3rnGt7DK7"},{"title":"A Deep Learning Approach for Paragraph-Level Paraphrase Generation for Plagiarism Detection | Neural Processing Letters | Springer Nature Link","url":"https://link.springer.com/article/10.1007/s11063-025-11771-9"},{"title":"Published as a conference paper at ICLR 2024","url":"https://openreview.net/pdf?id=zWqr3MQuNs"}]

I found several highly relevant research results on data contamination and paraphrase detection in Large Language Models from 2024-2026. Here are the key findings:

## Recent Surveys and Comprehensive Reviews

A comprehensive survey from early 2025 focuses on contamination detection methodologies in LLMs, providing an overview of current research in the field. Additionally, data contamination—the unintended overlap between training and te
…[truncated 1330 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_writing_related-work-completeness_20260514T054916",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-14T05:52:24.789701+00:00_

Web search results for query: "generational depth estimation recursive text generation detection 2024 2025"

Links: [{"title":"Machine-generated text detection prevents language model collapse","url":"https://arxiv.org/html/2502.15654"},{"title":"(PDF) Machine-generated text detection prevents language model collapse","url":"https://www.researchgate.net/publication/397412242_Machine-generated_text_detection_prevents_language_model_collapse"},{"title":"Breaking the Generator Barrier: Disentangled Representation for Generalizable AI-Text Detection","url":"https://arxiv.org/html/2604.13692v1"},{"title":"Diversity Boosts AI-Generated Text Detection","url":"https://arxiv.org/pdf/2509.18880"},{"title":"GitHub - RUC-NLPIR/GenIR-Survey: [TOIS 2025] This is the official repository for the generative information retrieval survey. · GitHub","url":"https://github.com/RUC-NLPIR/GenIR-Survey"},{"title":"Robust AI-Generated Text Detection by Restricted ...","url":"https://aclanthology.org/2024.findings-emnlp.992.pdf"},{"title":"GitHub - 52CV/CVPR-2024-Papers · GitHub","url":"https://github.com/52CV/CVPR-2024-Papers"},{"title":"Detecting AI-Generated Text: Factors Influencing Detectability with Current Methods","url":"https://arxiv.org/html/2406.15583v1"},{"title":"GitHub - 52CV/CVPR-2025-Papers · GitHub","url":"https://github.com/52CV/CVPR-2025-Papers"},{"title":"1 Retrieval-Augmented Generation for Large Language Models: A Survey","url":"https://www.rivista.ai/wp-content/uploads/2025/09/2312.10997v5.pdf"}]

Based on the web search results, here are the key findings related to generational depth estimation, recursive text generation, and detection in 2024-2025:

## Machine-Generated Text Detection and Model Collapse

Research in 2025 proposes methods for preventing model collapse by guided resampling of training data using confidence estimates from machine-generated text detectors. Model collapse is a degenerative process in which models recursively trained on generational data ex
…[truncated 1416 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_writing_related-work-completeness_20260514T054916",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 21 · 2026-05-14T05:52:24.789884+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "MGTBench machine generated text detection benchmark 2024 ACM CCS"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_writing_related-work-completeness_20260514T054916",
  "tool": "WebSearch",
  "tool_args": {
    "query": "MGTBench machine generated text detection benchmark 2024 ACM CCS"
  }
}
```

</details>

---

### Tool call

_source line 22 · 2026-05-14T05:52:24.790007+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "DetectRL benchmark LLM generated text detection NeurIPS 2024"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_writing_related-work-completeness_20260514T054916",
  "tool": "WebSearch",
  "tool_args": {
    "query": "DetectRL benchmark LLM generated text detection NeurIPS 2024"
  }
}
```

</details>

---

### Tool call

_source line 23 · 2026-05-14T05:52:24.790121+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"beyond model collapse\" scaling synthetic data 2025 ICLR"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_writing_related-work-completeness_20260514T054916",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"beyond model collapse\" scaling synthetic data 2025 ICLR"
  }
}
```

</details>

---

### Tool call

_source line 24 · 2026-05-14T05:52:24.790239+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "intrinsic dimension AI text detection 2024 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_writing_related-work-completeness_20260514T054916",
  "tool": "WebSearch",
  "tool_args": {
    "query": "intrinsic dimension AI text detection 2024 2025"
  }
}
```

</details>

---

### Tool result

_source line 25 · 2026-05-14T05:52:24.790396+00:00_

Web search results for query: "MGTBench machine generated text detection benchmark 2024 ACM CCS"

Links: [{"title":"MGTBench: Benchmarking Machine-Generated Text Detection | Proceedings of the 2024 on ACM SIGSAC Conference on Computer and Communications Security","url":"https://dl.acm.org/doi/10.1145/3658644.3670344"},{"title":"MGTBench: Benchmarking Machine-Generated Text Detection Xinlei He","url":"https://xinyueshen.me/papers/CCS24-MGTBench.pdf"},{"title":"GitHub - xinleihe/MGTBench","url":"https://github.com/xinleihe/MGTBench"},{"title":"MGTBench: Benchmarking Machine-Generated Text Detection | Proceedings of the 2024 on ACM SIGSAC Conference on Computer and Communications Security","url":"https://doi.org/10.1145/3658644.3670344"},{"title":"[PDF] MGTBench: Benchmarking Machine-Generated Text Detection | Semantic Scholar","url":"https://www.semanticscholar.org/paper/MGTBench:-Benchmarking-Machine-Generated-Text-He-Shen/e7ba478aad9b9534a9f632b85ad87177f5587189"},{"title":"IMGTB: A Framework for Machine-Generated Text ...","url":"https://aclanthology.org/2024.acl-demos.17.pdf"},{"title":"MGTBench: Benchmarking Machine-Generated Text Detection Xinlei He Xinyue Shen","url":"https://arxiv.org/pdf/2303.14822"},{"title":"[2303.14822] MGTBench: Benchmarking Machine-Generated Text Detection","url":"https://arxiv.org/abs/2303.14822"},{"title":"MGTBench: Benchmarking Machine-Generated Text Detection | Request PDF","url":"https://www.researchgate.net/publication/386590289_MGTBench_Benchmarking_Machine-Generated_Text_Detection"},{"title":"(PDF) MGTBench: Benchmarking Machine-Generated Text Detection","url":"https://www.researchgate.net/publication/369556294_MGTBench_Benchmarking_Machine-Generated_Text_Detection"}]

I've found comprehensive information about MGTBench. Here are the key findings:

## MGTBench Overview

MGTBench is the first benchmark framework for machine-generated text (MGT) detection against powerful LLMs. The paper was published in the Proceedings of the 2024
…[truncated 1435 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_writing_related-work-completeness_20260514T054916",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 26 · 2026-05-14T05:52:24.790571+00:00_

Web search results for query: "DetectRL benchmark LLM generated text detection NeurIPS 2024"

Links: [{"title":"GitHub - NLP2CT/DetectRL: [NeurIPS 2024 D&B] DetectRL: Benchmarking LLM-Generated Text Detection in Real-World Scenarios","url":"https://github.com/NLP2CT/DetectRL"},{"title":"DetectRL: Benchmarking LLM-Generated Text Detection in Real-World Scenarios","url":"https://proceedings.neurips.cc/paper_files/paper/2024/file/b61bdf7e9f64c04ec75a26e781e2ad51-Paper-Datasets_and_Benchmarks_Track.pdf"},{"title":"DetectRL: Benchmarking LLM-Generated Text Detection in Real-World Scenarios | OpenReview","url":"https://openreview.net/forum?id=ZGMkOikEyv"},{"title":"GitHub - junchaoIU/DetectRL: [NeurIPS 2024 D&B] DetectRL: Benchmarking LLM-Generated Text Detection in Real-World Scenarios","url":"https://github.com/junchaoIU/DetectRL"},{"title":"NeurIPS Poster DetectRL: Benchmarking LLM-Generated Text Detection in Real-World Scenarios","url":"https://neurips.cc/virtual/2024/poster/97633"},{"title":"[2410.23746] DetectRL: Benchmarking LLM-Generated Text Detection in Real-World Scenarios","url":"https://arxiv.org/abs/2410.23746"},{"title":"DetectRL: Benchmarking LLM-Generated Text Detection in Real-World Scenarios","url":"https://neurips.cc/media/neurips-2024/Slides/97633.pdf"},{"title":"GitHub - NLP2CT/LLM-generated-Text-Detection: A survey and reflection on the latest research breakthroughs in LLM-generated Text detection, including data, detectors, metrics, current issues and future directions. · GitHub","url":"https://github.com/nlp2ct/llm-generated-text-detection"},{"title":"DetectRL: Benchmarking LLM-Generated Text Detection in Real-World Scenarios - ADS","url":"https://ui.adsabs.harvard.edu/abs/2024arXiv241023746W/abstract"},{"title":"(PDF) DetectRL: Benchmarking LLM-Generated Text Detection in Real-World Scenarios","url":"https://www.researchgate.net/publication/385443385_DetectRL_Benchmarking_LLM-Generated_Text_Detection_in_Real-World_Scenarios"}]

Based on the searc
…[truncated 1489 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_writing_related-work-completeness_20260514T054916",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 27 · 2026-05-14T05:52:24.790756+00:00_

Web search results for query: ""beyond model collapse" scaling synthetic data 2025 ICLR"

Links: [{"title":"Strong Model Collapse | OpenReview","url":"https://openreview.net/forum?id=et5l9qPUhm"},{"title":"Beyond Model Collapse: Scaling Up with Synthesized Data Requires Verification | OpenReview","url":"https://openreview.net/forum?id=MQXrTMonT1"},{"title":"[2406.07515] Beyond Model Collapse: Scaling Up with Synthesized Data Requires Verification","url":"https://arxiv.org/abs/2406.07515"},{"title":"Published as a conference paper at ICLR 2025 STRONG MODEL COLLAPSE","url":"https://proceedings.iclr.cc/paper_files/paper/2025/file/284afdc2309f9667d2d4fb9290235b0c-Paper-Conference.pdf"},{"title":"Beyond Model Collapse: Scaling Up with Synthesized Data Requires Verification","url":"https://iclr.cc/media/iclr-2025/Slides/29933.pdf"},{"title":"[PDF] Beyond Model Collapse: Scaling Up with Synthesized Data Requires Verification | Semantic Scholar","url":"https://www.semanticscholar.org/paper/6404e954b18c3677c52937b0be2e12daba035c29"},{"title":"Published as a conference paper at ICLR 2025 STRONG MODEL COLLAPSE","url":"https://par.nsf.gov/servlets/purl/10649434"},{"title":"GitHub - pengr/LLM-Synthetic-Data: A live reading list for LLM data synthesis (Updated to July, 2025). · GitHub","url":"https://github.com/pengr/LLM-Synthetic-Data"},{"title":"ICML Beyond Model Collapse: Scaling Up with Synthesized Data Requires Reinforcement","url":"https://icml.cc/virtual/2024/37844"},{"title":"ICLR Poster Strong Model Collapse","url":"https://iclr.cc/virtual/2025/poster/32070"}]

Based on the search results, I found two relevant papers from ICLR 2025 that address scaling synthetic data and model collapse:

## 1. "Beyond Model Collapse: Scaling Up with Synthesized Data Requires Verification"

Large Language Models are increasingly trained on data generated by other LLMs, raising concerns about model collapse—a drop in model performance when training sets include generated data. The paper in
…[truncated 1428 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_writing_related-work-completeness_20260514T054916",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 28 · 2026-05-14T05:52:24.791177+00:00_

Web search results for query: "intrinsic dimension AI text detection 2024 2025"

Links: [{"title":"NeurIPS Poster Intrinsic Dimension Estimation for Robust Detection of AI-Generated Texts","url":"https://neurips.cc/virtual/2023/poster/72624"},{"title":"Intrinsic Dimension Estimation for Robust Detection of AI-Generated Texts | OpenReview","url":"https://openreview.net/forum?id=8uOZ0kNji6"},{"title":"[2306.04723] Intrinsic Dimension Estimation for Robust Detection of AI-Generated Texts","url":"https://arxiv.org/abs/2306.04723"},{"title":"[PDF] Intrinsic Dimension Estimation for Robust Detection of AI-Generated Texts | Semantic Scholar","url":"https://www.semanticscholar.org/paper/a5fab19553e623e8787383cb3da76b8a3c42a8f4"},{"title":"[Quick Review] Intrinsic Dimension Estimation for Robust Detection of AI-Generated Texts","url":"https://liner.com/review/intrinsic-dimension-estimation-for-robust-detection-of-aigenerated-texts"},{"title":"(PDF) Intrinsic Dimension Estimation for Robust Detection of AI-Generated Texts","url":"https://www.researchgate.net/publication/371414255_Intrinsic_Dimension_Estimation_for_Robust_Detection_of_AI-Generated_Texts"},{"title":"Detecting AI-Generated Text: : Factors Influencing ...","url":"https://dl.acm.org/doi/pdf/10.1613/jair.1.16665"},{"title":"Intrinsic Dimension Estimation for Robust Detection of AI-Generated Texts","url":"https://openreview.net/pdf?id=8uOZ0kNji6"},{"title":"Enhancing the Robustness of AI-Generated Text Detectors: A Survey","url":"https://www.mdpi.com/2227-7390/13/13/2145"},{"title":"Intrinsic dimension estimation for robust detection of AI-generated texts | Proceedings of the 37th International Conference on Neural Information Processing Systems","url":"https://dl.acm.org/doi/10.5555/3666122.3667828"}]

Based on the search results, I found comprehensive information about intrinsic dimension as a method for AI-generated text detection. Here's what the research shows:

## Key Findings

Researchers proposed intrinsic d
…[truncated 1626 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_writing_related-work-completeness_20260514T054916",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 29 · 2026-05-14T05:52:24.791360+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Fast-DetectGPT improved detection machine generated text ICLR 2024"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_writing_related-work-completeness_20260514T054916",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Fast-DetectGPT improved detection machine generated text ICLR 2024"
  }
}
```

</details>

---

### Tool call

_source line 30 · 2026-05-14T05:52:24.791486+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"strong model collapse\" Dohmatob ICLR 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_writing_related-work-completeness_20260514T054916",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"strong model collapse\" Dohmatob ICLR 2025"
  }
}
```

</details>

---

### Tool call

_source line 31 · 2026-05-14T05:52:24.791612+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "ordinal regression deep learning survey 2024 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_writing_related-work-completeness_20260514T054916",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ordinal regression deep learning survey 2024 2025"
  }
}
```

</details>

---

### Tool result

_source line 32 · 2026-05-14T05:52:24.791760+00:00_

Web search results for query: "Fast-DetectGPT improved detection machine generated text ICLR 2024"

Links: [{"title":"GitHub - baoguangsheng/fast-detect-gpt: Code base for ICLR 2024 \"Fast-DetectGPT: Efficient Zero-Shot Detection of Machine-Generated Text via Conditional Probability Curvature\". · GitHub","url":"https://github.com/baoguangsheng/fast-detect-gpt"},{"title":"Fast-DetectGPT: Efficient Zero-Shot Detection of Machine-Generated Text via Conditional Probability Curvature | OpenReview","url":"https://openreview.net/forum?id=Bpcgcr8E8Z"},{"title":"Published as a conference paper at ICLR 2024","url":"https://proceedings.iclr.cc/paper_files/paper/2024/file/6b8c6f846c3575e1d1ad496abea28826-Paper-Conference.pdf"},{"title":"ICLR Poster Fast-DetectGPT: Efficient Zero-Shot Detection of Machine-Generated Text via Conditional Probability Curvature","url":"https://iclr.cc/virtual/2024/poster/19201"},{"title":"(PDF) FAST-DETECTGPT: EFFICIENT ZERO-SHOT DETEC- TION OF MACHINE-GENERATED TEXT VIA CONDI- TIONAL PROBABILITY CURVATURE","url":"https://www.researchgate.net/publication/388188914_FAST-DETECTGPT_EFFICIENT_ZERO-SHOT_DETEC-_TION_OF_MACHINE-GENERATED_TEXT_VIA_CONDI-_TIONAL_PROBABILITY_CURVATURE"},{"title":"[2310.05130] Fast-DetectGPT: Efficient Zero-Shot Detection of Machine-Generated Text via Conditional Probability Curvature","url":"https://arxiv.org/abs/2310.05130"},{"title":"Fast-DetectGPT: Efficient Zero-Shot Detection of Machine-Generated Text via Conditional Probability Curvature","url":"https://proceedings.iclr.cc/paper_files/paper/2024/hash/6b8c6f846c3575e1d1ad496abea28826-Abstract-Conference.html"},{"title":"TRAINING-FREE LLM-GENERATED TEXT DETECTION","url":"https://openreview.net/pdf?id=vo4AHjowKi"},{"title":"Releases · baoguangsheng/fast-detect-gpt","url":"https://github.com/baoguangsheng/fast-detect-gpt/releases"},{"title":"ICLR 2024 | Fast-DetectGPT: Efficient Zero-Shot Detection of Machine-Generated Text - YouTube","url":"https://www.youtube.com/watch?v
…[truncated 1396 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_writing_related-work-completeness_20260514T054916",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 33 · 2026-05-14T05:52:24.791964+00:00_

Web search results for query: ""strong model collapse" Dohmatob ICLR 2025"

Links: [{"title":"Published as a conference paper at ICLR 2025 STRONG MODEL COLLAPSE","url":"https://proceedings.iclr.cc/paper_files/paper/2025/file/284afdc2309f9667d2d4fb9290235b0c-Paper-Conference.pdf"},{"title":"Strong Model Collapse | OpenReview","url":"https://openreview.net/forum?id=et5l9qPUhm"},{"title":"Published as a conference paper at ICLR 2025 STRONG MODEL COLLAPSE","url":"https://par.nsf.gov/servlets/purl/10649434"},{"title":"[2410.04840] Strong Model Collapse","url":"https://arxiv.org/abs/2410.04840"},{"title":"ICLR Poster Strong Model Collapse","url":"https://iclr.cc/virtual/2025/poster/32070"},{"title":"Published as a conference paper at ICLR 2025","url":"https://openreview.net/pdf?id=MQXrTMonT1"},{"title":"Escaping Model Collapse via Synthetic Data Verification: Near-term Improvements and Long-term ConvergenceThis project is supported by the AI2050 program at Schmidt Sciences (Grant G-24-66104) and Army Research Office Award W911NF-23-1-0030. We also thank Cong Ma from UChicago, Hongning Wang and Bo Li from Tsinghua, Pinyan Lu and Gavin Tang from Shanghai University of Finance and Economics for helpful discussions and suggestions.","url":"https://arxiv.org/html/2510.16657v1"},{"title":"Elvis DOHMATOB's Post","url":"https://www.linkedin.com/posts/elvis-dohmatob-53bba979_papers-accepted-at-iclr-2025-an-effective-activity-7307242348252442624-vT2L"},{"title":"dblp: Elvis Dohmatob","url":"https://dblp.org/pid/134/9794.html"},{"title":"Strong Model Collapse - ADS","url":"https://ui.adsabs.harvard.edu/abs/2024arXiv241004840D/abstract"}]

I found the paper! Here are the search results for "Strong Model Collapse" by Dohmatob and colleagues, published at ICLR 2025:

## Overview

The paper establishes a strong form of the model collapse phenomenon, a critical performance degradation due to synthetic data in the training corpus, within the scaling laws paradigm that underpins large neur
…[truncated 1122 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_writing_related-work-completeness_20260514T054916",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 34 · 2026-05-14T05:52:24.792155+00:00_

Web search results for query: "ordinal regression deep learning survey 2024 2025"

Links: [{"title":"A Survey on Ordinal Regression: Applications, Advances, and Prospects","url":"https://arxiv.org/html/2503.00952v1"},{"title":"A Deep Learning Ordinal Classifier","url":"https://thesai.org/Downloads/Volume16No3/Paper_30-A_Deep_Learning_Ordinal_Classifier.pdf"},{"title":"[2503.00952] A Survey on Ordinal Regression: Applications, Advances and Prospects","url":"https://arxiv.org/abs/2503.00952"},{"title":"Deep and interpretable regression models for ordinal outcomes - ScienceDirect","url":"https://www.sciencedirect.com/science/article/abs/pii/S003132032100443X"},{"title":"1 Tackling Ordinal Regression Problem for Heterogeneous Data: Sparse and Deep","url":"https://arxiv.org/pdf/1907.12508"},{"title":"A Survey on Ordinal Regression: Applications, Advances and Prospects | AI Research Paper Details","url":"https://www.aimodels.fyi/papers/arxiv/survey-ordinal-regression-applications-advances-prospects"},{"title":"A novel deep ordinal classification approach for aesthetic quality control classification | Neural Computing and Applications | Springer Nature Link","url":"https://link.springer.com/article/10.1007/s00521-022-07050-6"},{"title":"[1901.07884] Rank consistent ordinal regression for neural networks with application to age estimation","url":"https://arxiv.org/abs/1901.07884"},{"title":"GitHub - ayrna/orca: Ordinal Regression and Classification Algorithms · GitHub","url":"https://github.com/ayrna/orca"},{"title":"Active learning for ordinal classification based on expected cost minimization | Scientific Reports","url":"https://www.nature.com/articles/s41598-022-26844-1"}]

Based on the web search results, here are the key findings on ordinal regression and deep learning in 2024-2025:

## Recent Survey (2025)

A comprehensive survey on ordinal regression presents an examination of advances and applications, systematically classifying techniques into three categories: Con
…[truncated 1691 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_writing_related-work-completeness_20260514T054916",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 35 · 2026-05-14T05:52:24.792416+00:00_

---

## 1. Cite-Bib 一致性

**27 个 cite key，27 个 bib entry，完全匹配。**

- 缺失的 bib entry：**无**
- 孤立的 bib entry（未被引用）：**无**

---

## 2. 近期文献遗漏

以下论文在搜索中被发现具有较高相关性，但未出现在 related_work.tex 中：

| 论文 | Venue | Year | 与本工作的关系 |
|------|-------|------|----------------|
| **Fast-DetectGPT: Efficient Zero-Shot Detection via Conditional Probability Curvature** (Bao et al.) | ICLR | 2024 | 已引 DetectGPT 的直接后继，速度提升 340x、准确率相对提升 75%。作为 binary detection 段落的重要方法缺席 |
| **Strong Model Collapse** (Dohmatob, Feng, Subramonian, Kempe) | ICLR | 2025 | 与已引的 dohmatob2024model 同一作者，证明即使极小比例（1/1000）合成数据也导致 collapse，且更大模型会放大 collapse。直接强化本文动机 |
| **Beyond Model Collapse: Scaling Up with Synthesized Data Requires Verification** (Feng et al.) | ICLR | 2025 | 证明外部验证器可防止 collapse——depth estimation 本质上就是一种验证信号，与本文 curation 框架直接对接 |
| **DetectRL: Benchmarking LLM-Generated Text Detection in Real-World Scenarios** (Wu et al.) | NeurIPS D&B | 2024 | 展示 SOTA 检测器在真实场景下性能显著下降，为本文 depth estimation 的实用价值提供背景支撑 |
| **MGTBench: Benchmarking Machine-Generated Text Detection** (He et al.) | ACM CCS | 2024 | 首个系统性 MGT 检测基准，含 text attribution 任务（多类别归属），与 depth 分类有方法论交叉 |
| **Intrinsic Dimension Estimation for Robust Detection of AI-Generated Texts** (Tulchinskii et al.) | NeurIPS | 2023 | 用内在维度作为 zero-shot 检测特征，AI 文本的内在维度系统性低于人类文本约 1.5，可作为 depth 特征的潜在补充 |

**优先级建议**：Strong Model Collapse 和 Beyond Model Collapse 与本文动机最直接相关（model collapse + curation），建议优先补充。Fast-DetectGPT 作为 DetectGPT 的重要后继也应提及。

---

## 3. Bib 格式问题

| 条目 | 问题 |
|------|------|
| `shumailov2024collapse` | Nature 文章缺少 `volume={631}` 和 `pages={755--759}`，应补全 |
| `alain2017understanding` | 类型为 `@article`，journal 为 arXiv preprint，但该论文实际是 ICLR 2017 Workshop 论文。建议改为 `@inproceedings` 并注明 workshop，或保留 `@article` 但 year 与 arXiv ID (1610.01644, 2016年) 不完全对应 |
| `shi2025generalization` | `note={Spotlight}` 为非标准字段，部分 citation style 会将其直接输出到正文中，建议删除或移入注释 |
| Venue 命名 | NeurIPS 统一用 `Advances in NeurIPS`，其余用 `Proceedings of X` — 风格一致，可接受。但 `Advances in NeurIPS` 是非正式缩写（全称为 `Advances in Neural Information Processing Systems`），严格场合建议统一用全称或纯缩写 |
| Author 格式 | 全部 `{Last, First and ...}` 格式，一致 ✓ |
| Year 字段 | 全部完整 ✓ |

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_writing_related-work-completeness_20260514T054916"
}
```

</details>

---
