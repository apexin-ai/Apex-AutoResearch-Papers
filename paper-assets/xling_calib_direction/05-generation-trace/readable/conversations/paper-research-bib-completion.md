# paper research bib completion

**Shifting the Cross-Lingual Calibration Pareto Frontier: Probe-Based Calibration Transfer via CaCLR** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 115
- **Recorded user turns:** 0
- **Tool calls:** 57
- **Original source:** `logs/chats/worker_paper_research_bib_completion_20260521T073708.jsonl`
- **Structured JSON:** [`8822df3624945a809188.json`](../../sessions/88/8822df3624945a809188.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

115 recorded events

### Tool call

_source line 1 · 2026-05-21T07:42:36.381237+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/docs/paper/custom.bib"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_research_bib_completion_20260521T073708",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/docs/paper/custom.bib"
  }
}
```

</details>

---

### Tool result

_source line 2 · 2026-05-21T07:42:36.381582+00:00_

1	% Use this file for citations not found in the ACL Anthology (contained in "anthology.bib").
2	
3	@book{Aho:72,
4	    author  = {Alfred V. Aho and Jeffrey D. Ullman},
5	    title   = {The Theory of Parsing, Translation and Compiling},
6	    year    = "1972",
7	    volume  = "1",
8	    publisher = {Prentice-Hall},
9	    address = {Englewood Cliffs, NJ}
10	}
11	
12	@book{APA:83,
13	    author  = {{American Psychological Association}},
14	    title   = {Publications Manual},
15	    year    = "1983",
16	    publisher = {American Psychological Association},
17	    address = {Washington, DC}
18	}
19	
20	@article{Chandra:81,
21		author = {Ashok K. Chandra and Dexter C. Kozen and Larry J. Stockmeyer},
22		year = "1981",
23		title = {Alternation},
24		journal = {Journal of the Association for Computing Machinery},
25		volume = "28",
26		number = "1",
27		pages = "114--133",
28		doi = "10.1145/322234.322243",
29	}
30	
31	@inproceedings{andrew2007scalable,
32	  title={Scalable training of {L1}-regularized log-linear models},
33	  author={Andrew, Galen and Gao, Jianfeng},
34	  booktitle={Proceedings of the 24th International Conference on Machine Learning},
35	  pages={33--40},
36	  year={2007},
37	}
38	
39	@book{Gusfield:97,
40	    author  = {Dan Gusfield},
41	    title   = {Algorithms on Strings, Trees and Sequences},
42	    year    = "1997",
43	    publisher = {Cambridge University Press},
44	    address = {Cambridge, UK}
45	}
46	
47	@article{rasooli-tetrault-2015,
48	    author    = {Mohammad Sadegh Rasooli and Joel R. Tetreault},
49	    title     = {Yara Parser: {A} Fast and Accurate Dependency Parser},
50	    journal   = {Computing Research Repository},
51	    volume    = {arXiv:1503.06733},
52	    year      = {2015},
53	    url       = {http://arxiv.org/abs/1503.06733},
54	    note    = {version 2}
55	}
56	
57	@article{Ando2005,
58		Acmid = {1194905},
59		Author = {Ando, Rie Kubota and Zhang, Tong},
60		Issn = {1532-4435},
61		Issue_Date = {12/1/2005},
62		Journal = {J
…[truncated 1822 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_research_bib_completion_20260521T073708",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-21T07:42:36.381816+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/docs/paper/related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_research_bib_completion_20260521T073708",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/docs/paper/related_work.tex"
  }
}
```

</details>

---

### Tool result

_source line 4 · 2026-05-21T07:42:36.382028+00:00_

1	% Requires: \usepackage{pifont} \newcommand{\cmark}{\ding{51}} \newcommand{\xmark}{\ding{55}}
2	% Requires: \usepackage{booktabs}
3	
4	\section{Related Work}
5	
6	\subsection{LLM Calibration and Internal Representations}
7	
8	Post-hoc calibration methods such as temperature scaling \cite{guo2017calibration} and Platt scaling \cite{niculescu2005predicting} treat model confidence as a scalar output to be recalibrated after training. These approaches assume access to a held-out validation set from the target distribution and operate entirely on output logits without inspecting internal representations.
9	A complementary line of work examines whether models can self-assess correctness through verbalized confidence. \citet{kadavath2022language} demonstrate that larger language models produce well-calibrated probability estimates when asked to evaluate their own answers, establishing that calibration information exists within the model prior to output generation.
10	
11	Recent studies shift attention from output-level calibration to representation-level probing. \citet{miao2026closing} identify that correctness and verbalized confidence occupy nearly orthogonal subspaces in hidden states (cosine similarity below 0.04), suggesting that standard confidence elicitation fails to capture the full calibration signal. Building on this observation, CORAL \cite{miao2026coral} trains correctness probes that transfer across tasks within English, achieving approximately 50\% ECE improvement over verbalized confidence baselines. CCPS \cite{khanmohammadi2025ccps} takes a complementary approach by measuring representation stability under input perturbations as a proxy for correctness. The Confidence Manifold framework \cite{confidence_manifold2026} reveals that calibration-relevant information concentrates in a low-dimensional subspace (3 to 8 dimensions), with as few as 25 labeled examples sufficient for 89\% probing accuracy. \citet{ji2025calibrating} further demonstrate that verbal
…[truncated 8042 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_research_bib_completion_20260521T073708",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-21T07:42:36.382191+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/docs/paper/method.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_research_bib_completion_20260521T073708",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/docs/paper/method.tex"
  }
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-21T07:42:36.382376+00:00_

1	\section{Method}
2	\label{sec:method}
3	
4	\subsection{Problem Formulation}
5	\label{sec:problem}
6	
7	Given a multilingual large language model (LLM) and a multiple-choice question-answering (MCQA) instance, we extract the post-layer-norm residual stream representation $\mathbf{h}_l \in \mathbb{R}^d$ at layer $l$. A \emph{correctness probe} is a linear classifier
8	\begin{equation}
9	  f_l(\mathbf{h}_l) = \sigma(\mathbf{w}_l^\top \mathbf{h}_l + b_l)
10	  \label{eq:probe}
11	\end{equation}
12	trained to predict $p(\text{correct} \mid \mathbf{h}_l)$, the probability that the model's selected answer is correct. This target is output-dependent: it reflects the model's actual accuracy on each instance, not an intrinsic property of the input.
13	
14	We distinguish correctness probing from two related tasks. \emph{Knowledge boundary probing} \citep{xiao2025knowledge} classifies whether a question is answerable, an input-level property independent of model output. \emph{Difficulty probing} \citep{civelli2026shared} predicts item difficulty as a language-agnostic question property via Item Response Theory (IRT). Our central question is whether an English-trained probe $f_l$ can transfer zero-shot to a target language $t$ without any target-language correctness labels (zero-correctness-label transfer), and which alignment strategies improve this transfer.
15	
16	\subsection{Experimental Framework}
17	\label{sec:framework}
18	
19	\paragraph{Models.} We evaluate Qwen3-235B-A22B (GPTQ-Int4) and Llama 4 Scout 17B-16E (W4A16) as primary architectures (P0), with Qwen2.5-7B-Instruct and Llama-3.1-8B-Instruct for validation (MVP).
20	
21	\paragraph{Languages.} We test 20 languages (English as source, plus 19 target languages) spanning three resource tiers based on GlobalMMLU availability: \textsc{high} (zh, de, es, fr, ja, ko, pt, ru), \textsc{med} (ar, id, nl, pl, tr, uk, vi), and \textsc{low} (bn, hi, sw, te).
22	
23	\paragraph{Data.} We use the GlobalMMLU test split, partitione
…[truncated 8775 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_research_bib_completion_20260521T073708",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-21T07:42:36.382544+00:00_

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
  "session": "worker_paper_research_bib_completion_20260521T073708",
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

_source line 8 · 2026-05-21T07:42:36.382682+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_research_bib_completion_20260521T073708",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-21T07:42:36.382832+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Xiao \"knowledge boundary\" cross-lingual probe transfer ACL 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_research_bib_completion_20260521T073708",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Xiao \"knowledge boundary\" cross-lingual probe transfer ACL 2025"
  }
}
```

</details>

---

### Tool call

_source line 10 · 2026-05-21T07:42:36.382952+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Zhou LACE adaptive layer ensemble multilingual calibration 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_research_bib_completion_20260521T073708",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Zhou LACE adaptive layer ensemble multilingual calibration 2025"
  }
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-21T07:42:36.383066+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Miao Ungar \"correctness-confidence orthogonality\" 2026 LLM representations"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_research_bib_completion_20260521T073708",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Miao Ungar \"correctness-confidence orthogonality\" 2026 LLM representations"
  }
}
```

</details>

---

### Tool call

_source line 12 · 2026-05-21T07:42:36.383178+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Miao CORAL cross-task correctness probes 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_research_bib_completion_20260521T073708",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Miao CORAL cross-task correctness probes 2026"
  }
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-21T07:42:36.383305+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Khanmohammadi CCPS perturbation stability calibration 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_research_bib_completion_20260521T073708",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Khanmohammadi CCPS perturbation stability calibration 2025"
  }
}
```

</details>

---

### Tool call

_source line 14 · 2026-05-21T07:42:36.383446+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"Confidence Manifold\" framework LLM calibration low-dimensional subspace 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_research_bib_completion_20260521T073708",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"Confidence Manifold\" framework LLM calibration low-dimensional subspace 2026"
  }
}
```

</details>

---

### Tool result

_source line 15 · 2026-05-21T07:42:36.383613+00:00_

Web search results for query: "Zhou LACE adaptive layer ensemble multilingual calibration 2025"

Links: [{"title":"[2510.03136] Beyond the Final Layer: Intermediate Representations for Better Multilingual Calibration in Large Language Models","url":"https://arxiv.org/abs/2510.03136"},{"title":"Beyond the Final Layer: Intermediate Representations for Better Multilingual Calibration in Large Language Models","url":"https://arxiv.org/html/2510.03136v1"},{"title":"Beyond the Final Layer: Intermediate Representations for Better Multilingual Calibration in Large Language Models","url":"https://www.researchgate.net/publication/396223351_Beyond_the_Final_Layer_Intermediate_Representations_for_Better_Multilingual_Calibration_in_Large_Language_Models"},{"title":"Beyond the Final Layer: Intermediate Representations for Better Multilingual Calibration in Large Language Models","url":"https://arxiv.org/pdf/2510.03136"},{"title":"Beyond the Final Layer: Intermediate Representations for Better Multilingual Calibration in Large Language Models | OpenReview","url":"https://openreview.net/forum?id=CUS9OTCGdt"},{"title":"Post-Training Quantization Methods","url":"https://www.emergentmind.com/topics/post-training-quantization-methods"},{"title":"Ivan Vulić's research works | University of Cambridge and other places","url":"https://researchgate.net/scientific-contributions/2034162457_Ivan_Vulic"},{"title":"Accepted Submissions | MELT Workshop @ COLM 2025","url":"https://melt-workshop.github.io/papers/"}]

I found the research paper you're looking for. Here's what the search revealed:

Zhou's work introduces Language-Aware Confidence Ensemble (LACE), a training-free method that adaptively selects an optimal ensemble of layers for each specific language.

The research addresses an important problem: the study conducts large-scale, systematic studies of multilingual calibration across six model families and over 100 languages, revealing that non-English languages suffer from systematically
…[truncated 800 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_research_bib_completion_20260521T073708",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-21T07:42:36.383859+00:00_

Web search results for query: "Khanmohammadi CCPS perturbation stability calibration 2025"

Links: [{"title":"Calibrating LLM Confidence by Probing Perturbed Representation Stability - ACL Anthology","url":"https://aclanthology.org/2025.emnlp-main.530/"},{"title":"GitHub - Ledengary/CCPS: Calibrating LLM Confidence by Probing Perturbed Representation Stability","url":"https://github.com/ledengary/CCPS"},{"title":"Reza Khan Mohammadi","url":"https://www.khanmohammadi.me/"},{"title":"Reza KHANMOHAMMADI | Student | Doctor of Philosophy | Michigan State University, East Lansing | MSU | Department of Computer Science and Engineering | Research profile","url":"https://www.researchgate.net/profile/Reza-Khanmohammadi"},{"title":"Calibrating LLM Confidence by Probing Perturbed Representation Stability | Request PDF","url":"https://www.researchgate.net/publication/397423860_Calibrating_LLM_Confidence_by_Probing_Perturbed_Representation_Stability"},{"title":"Calibrating LLM Confidence by Probing Perturbed Representation Stability","url":"https://arxiv.org/html/2505.21772v1"},{"title":"CCPS: Calibrating LLM Confidence via Perturbation Stability – EMNLP 2025 | Hacker News","url":"https://news.ycombinator.com/item?id=45055315"},{"title":"[2505.21772] Calibrating LLM Confidence by Probing Perturbed Representation Stability","url":"https://arxiv.org/abs/2505.21772"}]

Based on the search results, here's what I found about this research:

## Overview

CCPS (Calibrating LLM Confidence by Probing Perturbed Representation Stability) is a novel method that analyzes internal representational stability in LLMs by applying targeted adversarial perturbations to final hidden states, extracting features reflecting the model's response to these perturbations, and using a lightweight classifier to predict answer correctness.

## Key Results

Across four LLMs and three MMLU variants, CCPS reduces Expected Calibration Error by approximately 55% and Brier score by 21%, while increasing accuracy by
…[truncated 724 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_research_bib_completion_20260521T073708",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 17 · 2026-05-21T07:42:36.384038+00:00_

Web search results for query: "Xiao "knowledge boundary" cross-lingual probe transfer ACL 2025"

Links: [{"title":"GitHub - DAMO-NLP-SG/LLM-Multilingual-Knowledge-Boundaries: [ACL 2025] Analyzing LLMs' Multilingual Knowledge Boundary Cognition Across Languages Through the Lens of Internal Representations","url":"https://github.com/DAMO-NLP-SG/LLM-Multilingual-Knowledge-Boundaries"},{"title":"Analyzing LLMs’ Knowledge Boundary Cognition Across Languages Through the Lens of Internal Representations - ACL Anthology","url":"https://aclanthology.org/2025.acl-long.1174/"},{"title":"Accepted Main Conference Papers - ACL 2025","url":"https://2025.aclweb.org/program/main_papers/"},{"title":"Analyzing LLMs' Knowledge Boundary Cognition Across ...","url":"https://aclanthology.org/2025.acl-long.1174.pdf"},{"title":"LiveCLKTBench: Towards Reliable Evaluation of Cross-Lingual Knowledge Transfer in Multilingual LLMs","url":"https://arxiv.org/pdf/2511.14774"}]

I found relevant information about your search query! Here are the key findings:

The paper "Analyzing LLMs' Knowledge Boundary Cognition Across Languages Through the Lens of Internal Representations" was authored by Chenghao Xiao, Hou Pong Chan, Hao Zhang, Mahani Aljunied, Lidong Bing, Noura Al Moubayed, and Yu Rong, and was published at ACL 2025.

The research constructs a multilingual evaluation suite comprising three representative types of knowledge boundary data to address the absence of standard testbeds for cross-lingual knowledge boundary analysis.

Key findings from the work include: Language differences in knowledge boundary perception follow a linear structure, which motivates a training-free alignment method that effectively transfers knowledge boundary perception ability across languages, thereby helping reduce hallucination risk in low-resource languages. Additionally, fine-tuning on bilingual question pair translation further enhances LLMs' recognition of knowledge boundaries across languages.

The code and d
…[truncated 206 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_research_bib_completion_20260521T073708",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-21T07:42:36.384211+00:00_

Web search results for query: "Miao CORAL cross-task correctness probes 2026"

Links: [{"title":"Miranda Muqing Miao","url":"https://mmiao2.github.io/"},{"title":"Correctness-Optimized Residual Activation Lens (CORAL):","url":"https://arxiv.org/pdf/2602.06022"},{"title":"[2602.06022] Correctness-Optimized Residual Activation Lens (CORAL): Transferrable and Calibration-Aware Inference-Time Steering","url":"https://arxiv.org/abs/2602.06022"},{"title":"Correctness-Optimized Residual Activation Lens (CORAL): Transferrable and Calibration-Aware Inference-Time Steering","url":"https://arxiv.org/html/2602.06022v1"},{"title":"GitHub - Human-Agent-Society/CORAL: CORAL is a robust, lightweight infrastructure for multi-agent autonomous self-evolution, built for autoresearch. Works with Claude Code, Codex, Cursor, OpenCode, Kiro, and more. · GitHub","url":"https://github.com/Human-Agent-Society/CORAL"},{"title":"Correctness-Optimized Residual Activation Lens (CORAL): Transferrable and Calibration-Aware Inference-Time Steering","url":"https://www.researchgate.net/publication/400505951_Correctness-Optimized_Residual_Activation_Lens_CORAL_Transferrable_and_Calibration-Aware_Inference-Time_Steering"},{"title":"CORAL: Towards Autonomous Multi-Agent Evolution for Open-Ended Discovery","url":"https://arxiv.org/html/2604.01658v1"}]

Based on the search results, I found information about Miranda Muqing Miao's CORAL research from 2026:

CORAL (Correctness-Optimized Residual Activation Lens) is a regularized inference-time steering method that captures distributed correctness signals from model internal activations using weight-decay MLP probes.

The method uses a mechanistic interpretability approach to inference-time steering that extracts distributed correctness signals from frozen LLM residual stream activations via auxiliary probes, improving accuracy and calibration with cross-task generalization.

**Performance Results:**

CORAL consistently improves accuracy by 10% and expected ca
…[truncated 531 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_research_bib_completion_20260521T073708",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 19 · 2026-05-21T07:42:36.384374+00:00_

Web search results for query: "Miao Ungar "correctness-confidence orthogonality" 2026 LLM representations"

Links: [{"title":"Know When You’re Wrong: Aligning Confidence with Correctness for LLM Error Detection","url":"https://arxiv.org/html/2603.06604"},{"title":"On LLMs' Internal Representation of Code Correctness","url":"https://arxiv.org/pdf/2512.07404"},{"title":"Are LLM Uncertainty and Correctness Encoded by the Same Features? A Functional Dissociation via Sparse Autoencoders","url":"https://arxiv.org/html/2604.19974"},{"title":"Calibrating LLM Confidence by Probing Perturbed Representation Stability","url":"https://arxiv.org/pdf/2505.21772"},{"title":"The Confidence Manifold: Geometric Structure of Correctness Representations in Language Models","url":"https://arxiv.org/pdf/2602.08159"},{"title":"Confidence Geometry Reveals Trace-Level Correctness in Large Language Model Reasoning","url":"https://arxiv.org/html/2605.16824"},{"title":"can llms express their uncertainty? an empirical evaluation ...","url":"https://arxiv.org/pdf/2306.13063"}]

Based on the search results, I found relevant research related to your query. The most directly related paper appears to be "Are LLM Uncertainty and Correctness Encoded by the Same Features?" which uses sparse autoencoders to test whether uncertainty and correctness are encoded by distinct or overlapping feature populations, introducing a 2×2 quadrant framework that partitions model predictions along two independent axes, correctness and confidence.

Additionally, there's research characterizing the geometry of correctness representations in transformer activations across 9 models from 5 architecture families, finding that the discriminative signal occupies 3–8 dimensions.

The search results also show other recent 2026 work on LLM confidence and correctness, including papers on calibrating confidence estimates and detecting when LLMs are wrong.

However, I should note that the search results mention a GitHub link referenc
…[truncated 520 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_research_bib_completion_20260521T073708",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-21T07:42:36.384552+00:00_

Web search results for query: ""Confidence Manifold" framework LLM calibration low-dimensional subspace 2026"

Links: [{"title":"The Confidence Manifold: Geometric Structure of Correctness Representations in Language Models","url":"https://arxiv.org/html/2602.08159v1"},{"title":"The Confidence Manifold - Seongland","url":"https://seongland.com/article/confidence-manifold/"},{"title":"Confidence Calibration in LLMs","url":"https://www.emergentmind.com/topics/confidence-calibration-in-llms"},{"title":"The Confidence Manifold: Geometric Structure of Correctness Representations in Language Models","url":"https://arxiv.org/pdf/2602.08159"},{"title":"Calibrating LLM Confidence by Probing Perturbed Representation Stability","url":"https://arxiv.org/pdf/2505.21772"},{"title":"COSPADI: COMPRESSING LLMS VIA CALIBRATION- GUIDED SPARSE DICTIONARY LEARNING","url":"https://arxiv.org/pdf/2509.22075"},{"title":"Calibration Across Layers: Understanding Calibration Evolution in LLMs","url":"https://arxiv.org/html/2511.00280v1"},{"title":"Calibrating LLM Confidence by Probing Perturbed Representation Stability","url":"https://arxiv.org/html/2505.21772v1"}]

Based on the search results, here's what I found about the Confidence Manifold framework:

## The Confidence Manifold Framework

Language models encode a rich correctness signal internally that lives in a surprisingly low-dimensional subspace of just 3 to 8 dimensions, called the confidence manifold.

**Key Findings:**

The research characterized the geometry of correctness representations across 9 models from 5 architecture families, finding that the discriminative signal occupies 3–8 dimensions, performance degrades with additional dimensions, and no nonlinear classifier improves over linear separation.

**Efficiency and Performance:**

A 7B model with 4096-dimensional hidden states encodes correctness in just 5 dimensions, 0.12% of its representational capacity. Additionally, centroid distance in the low-dimensional subspace mat
…[truncated 645 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_research_bib_completion_20260521T073708",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool call

_source line 21 · 2026-05-21T07:42:36.384743+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Ji 2025 \"verbal uncertainty\" \"linear direction\" LLM representation space calibration"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_research_bib_completion_20260521T073708",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Ji 2025 \"verbal uncertainty\" \"linear direction\" LLM representation space calibration"
  }
}
```

</details>

---

### Tool call

_source line 22 · 2026-05-21T07:42:36.384870+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Joshi 2025 \"calibration across layers\" LLM non-monotonic"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_research_bib_completion_20260521T073708",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Joshi 2025 \"calibration across layers\" LLM non-monotonic"
  }
}
```

</details>

---

### Tool call

_source line 23 · 2026-05-21T07:42:36.384984+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Liu Niehues 2025 \"middle layer\" cross-lingual alignment fine-tuned LLM"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_research_bib_completion_20260521T073708",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Liu Niehues 2025 \"middle layer\" cross-lingual alignment fine-tuned LLM"
  }
}
```

</details>

---

### Tool call

_source line 24 · 2026-05-21T07:42:36.385095+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Ravisankar 2026 DALI activation patching cross-lingual"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_research_bib_completion_20260521T073708",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Ravisankar 2026 DALI activation patching cross-lingual"
  }
}
```

</details>

---

### Tool call

_source line 25 · 2026-05-21T07:42:36.385211+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Civelli 2026 \"shared geometry\" difficulty IRT cross-lingual"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_research_bib_completion_20260521T073708",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Civelli 2026 \"shared geometry\" difficulty IRT cross-lingual"
  }
}
```

</details>

---

### Tool call

_source line 26 · 2026-05-21T07:42:36.385321+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Miao Ungar 2026 \"closing the gap\" correctness confidence orthogonal subspace LLM arXiv"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_research_bib_completion_20260521T073708",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Miao Ungar 2026 \"closing the gap\" correctness confidence orthogonal subspace LLM arXiv"
  }
}
```

</details>

---

### Tool result

_source line 27 · 2026-05-21T07:42:36.385449+00:00_

Web search results for query: "Ji 2025 "verbal uncertainty" "linear direction" LLM representation space calibration"

Links: [{"title":"[2503.14477] Calibrating Verbal Uncertainty as a Linear Feature to Reduce Hallucinations","url":"https://arxiv.org/abs/2503.14477"},{"title":"Calibrating Verbal Uncertainty as a Linear Feature to Reduce Hallucinations - ACL Anthology","url":"https://aclanthology.org/2025.emnlp-main.187/"},{"title":"Calibrating Verbal Uncertainty as a Linear Feature to Reduce Hallucinations","url":"https://www.researchgate.net/publication/397424902_Calibrating_Verbal_Uncertainty_as_a_Linear_Feature_to_Reduce_Hallucinations"},{"title":"Calibrating Verbal Uncertainty as a Linear Feature to Reduce Hallucinations","url":"https://arxiv.org/html/2503.14477v1"},{"title":"Calibrating Verbal Uncertainty as a Linear Feature to Reduce   Hallucinations","url":"https://arxiv.org/pdf/2503.14477"},{"title":"(PDF) Calibrating Verbal Uncertainty as a Linear Feature to Reduce Hallucinations","url":"https://www.researchgate.net/publication/389947447_Calibrating_Verbal_Uncertainty_as_a_Linear_Feature_to_Reduce_Hallucinations"},{"title":"Calibrating LLM Judges: Linear Probes for Fast and Reliable Uncertainty Estimation","url":"https://arxiv.org/html/2512.22245"},{"title":"Calibrating LLM Judges: Linear Probes for Fast and Reliable Uncertainty Estimation","url":"https://arxiv.org/pdf/2512.22245"}]

I found the research you're looking for. The paper finds that "verbal uncertainty" is governed by a single linear feature in the representation space of LLMs, and shows that this has only moderate correlation with the actual "semantic uncertainty" of the model.

The paper is by Ziwei Ji and colleagues, published in 2025. The researchers show that the degree of uncertainty expressed by a model is mediated by a single direction, which they call the "Verbal Uncertainty Feature" (VUF). 

They apply this insight and show that (1) the mismatch between semantic and verbal uncertainty 
…[truncated 451 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_research_bib_completion_20260521T073708",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 28 · 2026-05-21T07:42:36.385599+00:00_

Web search results for query: "Ravisankar 2026 DALI activation patching cross-lingual"

Links: [{"title":"Can you map it to English? The Role of Cross-Lingual Alignment in the Multilingual Performance of LLMs - ACL Anthology","url":"https://aclanthology.org/2026.eacl-long.225/"},{"title":"[2504.09378] Can you map it to English? The Role of Cross-Lingual Alignment in Multilingual Performance of LLMs","url":"https://arxiv.org/abs/2504.09378"},{"title":"Can you map it to English? The Role of Cross-Lingual Alignment in Multilingual Performance of LLMs","url":"https://arxiv.org/pdf/2504.09378"},{"title":"Can you map it to English? The Role of Cross-Lingual Alignment in Multilingual Performance of LLMs","url":"https://arxiv.org/html/2504.09378v1"},{"title":"Separating Tongue from Thought: Activation Patching Reveals Language-Agnostic Concept Representations in Transformers","url":"https://arxiv.org/pdf/2411.08745"},{"title":"(PDF) Can you map it to English? The Role of Cross-Lingual Alignment in Multilingual Performance of LLMs","url":"https://www.researchgate.net/publication/390773780_Can_you_map_it_to_English_The_Role_of_Cross-Lingual_Alignment_in_Multilingual_Performance_of_LLMs"}]

The search results show relevant research on this topic. Here's what I found:

Kartik Ravisankar and colleagues published research in 2026 at the 19th Conference of the European Chapter of the Association for Computational Linguistics. They introduced the Discriminative Alignment Index (DALI) to quantify instance-level alignment across 24 languages other than English and three distinct NLU tasks.

Through activation patching, the researchers showed that incorrect predictions in languages other than English can be fixed by patching their parallel English activations in the middle layers, thereby demonstrating the causal role of representation (mis)alignment in cross-lingual correctness. Results show that incorrect NLU predictions are strongly associated with lower representation alignment wi
…[truncated 378 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_research_bib_completion_20260521T073708",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 29 · 2026-05-21T07:42:36.385791+00:00_

Web search results for query: "Joshi 2025 "calibration across layers" LLM non-monotonic"

Links: [{"title":"Calibration Across Layers: Understanding Calibration Evolution in LLMs","url":"https://arxiv.org/html/2511.00280v1"},{"title":"Calibration Across Layers: Understanding Calibration Evolution in LLMs - ACL Anthology","url":"https://aclanthology.org/2025.emnlp-main.742/"},{"title":"GitHub - Exploration-Lab/LLM-Calibration-Mechanism · GitHub","url":"https://github.com/Exploration-Lab/LLM-Calibration-Mechanism"},{"title":"(PDF) Calibration Across Layers: Understanding Calibration Evolution in LLMs","url":"https://www.researchgate.net/publication/397231243_Calibration_Across_Layers_Understanding_Calibration_Evolution_in_LLMs"},{"title":"Calibration Across Layers: Understanding Calibration Evolution in LLMs | Request PDF","url":"https://www.researchgate.net/publication/397421796_Calibration_Across_Layers_Understanding_Calibration_Evolution_in_LLMs"},{"title":"Computation and Language 2025","url":"https://arxiv.org/list/cs.CL/2025?skip=22850&show=2000"},{"title":"[2511.00280] Calibration Across Layers: Understanding Calibration Evolution in LLMs","url":"https://arxiv.org/abs/2511.00280"},{"title":"Detecting LLM Hallucination Through Layer-wise ...","url":"https://aclanthology.org/2025.emnlp-main.1644.pdf"}]

I found relevant research on this topic. Here are the search results:

The paper "Calibration Across Layers: Understanding Calibration Evolution in LLMs" was authored by Abhinav Joshi, Areeb Ahmad, and Ashutosh Modi in 2025.

The work investigates how calibration evolves throughout the network's depth, and analyzing multiple open-weight models on the MMLU benchmark, the authors uncovered a distinct confidence correction phase in the upper/later layers, where model confidence is actively recalibrated after decision certainty has been reached.

The research identifies a low-dimensional calibration direction in the residual stream whose perturbation significantly imp
…[truncated 653 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_research_bib_completion_20260521T073708",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 30 · 2026-05-21T07:42:36.385950+00:00_

Web search results for query: "Civelli 2026 "shared geometry" difficulty IRT cross-lingual"

Links: [{"title":"A Shared Geometry of Difficulty in Multilingual Language Models","url":"https://arxiv.org/html/2601.12731"},{"title":"[2601.12731] A Shared Geometry of Difficulty in Multilingual Language Models","url":"https://arxiv.org/abs/2601.12731"},{"title":"[Literature Review] A Shared Geometry of Difficulty in Multilingual Language Models","url":"https://www.themoonlight.io/en/review/a-shared-geometry-of-difficulty-in-multilingual-language-models"},{"title":"A Shared Geometry of Difficulty in Multilingual Language Models","url":"https://arxiv.org/pdf/2601.12731"},{"title":"(PDF) A Shared Geometry of Difficulty in Multilingual Language Models","url":"https://www.researchgate.net/publication/399930732_A_Shared_Geometry_of_Difficulty_in_Multilingual_Language_Models"}]

The search returned results for the paper "A Shared Geometry of Difficulty in Multilingual Language Models" by Civelli et al. from 2026. Here's what I found:

The paper, authored by Stefano Civelli and colleagues, studies the multilingual geometry of problem-difficulty in LLMs by training linear probes using the AMC subset of the Easy2Hard benchmark, translated into 21 languages.

Difficulty is estimated via Item Response Theory (IRT) from human success rates.

Key findings include:

Difficulty-related signals emerge at two distinct stages of the model internals, corresponding to shallow (early-layers) and deep (later-layers) internal representations, that exhibit functionally different behaviors.

Probes trained on deep representations achieve high accuracy when evaluated on the same language but exhibit poor cross-lingual generalization. In contrast, probes trained on shallow representations generalize substantially better across languages, despite achieving lower within-language performance.

The results suggest that LLMs first form a language-agnostic representation of problem difficulty, which subse
…[truncated 137 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_research_bib_completion_20260521T073708",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 31 · 2026-05-21T07:42:36.386152+00:00_

Web search results for query: "Miao Ungar 2026 "closing the gap" correctness confidence orthogonal subspace LLM arXiv"

Links: [{"title":"Closing the Confidence-Faithfulness Gap in Large Language Models","url":"https://arxiv.org/html/2603.25052"},{"title":"Miranda Muqing Miao","url":"https://mmiao2.github.io/"},{"title":"[2603.25052] Closing the Confidence-Faithfulness Gap in Large Language Models","url":"https://arxiv.org/abs/2603.25052"},{"title":"Bridging the Knowledge-Prediction Gap in LLMs on Multiple-Choice Questions","url":"https://arxiv.org/pdf/2509.23782"},{"title":"On the Fundamental Limits of LLMs at Scale","url":"https://arxiv.org/html/2511.12869v2"},{"title":"GRADE: Probing Knowledge Gaps in LLMs through Gradient Subspace Dynamics","url":"https://arxiv.org/pdf/2604.02830"}]

I found the paper you're looking for! The research by Miao and Ungar presents a mechanistic interpretability analysis of verbalized confidence, using linear probes and contrastive activation addition (CAA) steering to show that calibration and verbalized confidence signals are encoded linearly but are orthogonal to one another — a finding consistent across three open-weight models and four datasets.

When models are prompted to simultaneously reason through a problem and verbalize a confidence score, the reasoning process disrupts the verbalized confidence direction, exacerbating miscalibration (termed the "Reasoning Contamination Effect"), and the researchers introduce a two-stage adaptive steering pipeline that reads the model's internal accuracy estimate and steers verbalized output to match it.

The paper is titled "Closing the Confidence-Faithfulness Gap in Large Language Models" and appears on arXiv as paper 2603.25052, dated April 1, 2026.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_research_bib_completion_20260521T073708",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 32 · 2026-05-21T07:42:36.386396+00:00_

Web search results for query: "Liu Niehues 2025 "middle layer" cross-lingual alignment fine-tuned LLM"

Links: [{"title":"Middle-Layer Representation Alignment for Cross-Lingual Transfer in Fine-Tuned LLMs - ACL Anthology","url":"https://aclanthology.org/2025.acl-long.778/"},{"title":"Probing the Emergence of Cross-lingual Alignment during LLM Training","url":"https://www.researchgate.net/publication/384219551_Probing_the_Emergence_of_Cross-lingual_Alignment_during_LLM_Training"},{"title":"Middle-Layer Representation Alignment for Cross-Lingual Transfer in Fine-Tuned LLMs | Request PDF","url":"https://www.researchgate.net/publication/394303200_Middle-Layer_Representation_Alignment_for_Cross-Lingual_Transfer_in_Fine-Tuned_LLMs"},{"title":"[Literature Review] Middle-Layer Representation Alignment for Cross-Lingual Transfer in Fine-Tuned LLMs","url":"https://www.themoonlight.io/en/review/middle-layer-representation-alignment-for-cross-lingual-transfer-in-fine-tuned-llms"},{"title":"Middle-Layer Representation Alignment for Cross-Lingual Transfer in Fine-Tuned LLMs","url":"https://arxiv.org/pdf/2502.14830"},{"title":"[2502.14830] Middle-Layer Representation Alignment for Cross-Lingual Transfer in Fine-Tuned LLMs","url":"https://arxiv.org/abs/2502.14830"},{"title":"Middle-Layer Representation Alignment for Cross-Lingual Transfer in Fine-Tuned LLMs","url":"https://arxiv.org/html/2502.14830v1"},{"title":"Middle-Layer Representation Alignment for Cross-Lingual Transfer in Fine-Tuned LLMs - haebom","url":"https://slashpage.com/haebom/y9e1xp2xyyx54m7k35vz?lang=en&tl=en"}]

Based on the search results, here's what I found about the Liu and Niehues 2025 paper on middle-layer cross-lingual alignment in fine-tuned LLMs:

## Paper Overview

The paper is titled "Middle-Layer Representation Alignment for Cross-Lingual Transfer in Fine-Tuned LLMs" and was published at the 63rd Annual Meeting of the Association for Computational Linguistics (ACL 2025) in Vienna, Austria.

## Key Findi
…[truncated 931 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_research_bib_completion_20260521T073708",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool call

_source line 33 · 2026-05-21T07:42:36.386590+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Guo \"On Calibration of Modern Neural Networks\" ICML 2017 doi"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_research_bib_completion_20260521T073708",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Guo \"On Calibration of Modern Neural Networks\" ICML 2017 doi"
  }
}
```

</details>

---

### Tool call

_source line 34 · 2026-05-21T07:42:36.386777+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Conneau \"Unsupervised Cross-lingual Representation Learning at Scale\" XLM-R ACL 2020 doi"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_research_bib_completion_20260521T073708",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Conneau \"Unsupervised Cross-lingual Representation Learning at Scale\" XLM-R ACL 2020 doi"
  }
}
```

</details>

---

### Tool call

_source line 35 · 2026-05-21T07:42:36.386911+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Fedus \"Switch Transformers\" JMLR 2022 doi trillion parameter"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_research_bib_completion_20260521T073708",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Fedus \"Switch Transformers\" JMLR 2022 doi trillion parameter"
  }
}
```

</details>

---

### Tool call

_source line 36 · 2026-05-21T07:42:36.387027+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Lord 1980 \"Applications of Item Response Theory to Practical Testing Problems\" ISBN Erlbaum"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_research_bib_completion_20260521T073708",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Lord 1980 \"Applications of Item Response Theory to Practical Testing Problems\" ISBN Erlbaum"
  }
}
```

</details>

---

### Tool call

_source line 37 · 2026-05-21T07:42:36.387140+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Kornblith \"Similarity of Neural Network Representations Revisited\" CKA ICML 2019 doi"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_research_bib_completion_20260521T073708",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Kornblith \"Similarity of Neural Network Representations Revisited\" CKA ICML 2019 doi"
  }
}
```

</details>

---

### Tool call

_source line 38 · 2026-05-21T07:42:36.387250+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Ben-David \"A Theory of Learning from Different Domains\" Machine Learning 2010 doi"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_research_bib_completion_20260521T073708",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Ben-David \"A Theory of Learning from Different Domains\" Machine Learning 2010 doi"
  }
}
```

</details>

---

### Tool result

_source line 39 · 2026-05-21T07:42:36.387461+00:00_

Web search results for query: "Guo "On Calibration of Modern Neural Networks" ICML 2017 doi"

Links: [{"title":"[1706.04599] On Calibration of Modern Neural Networks","url":"https://arxiv.org/abs/1706.04599"},{"title":"\"On Calibration of Modern Neural Networks\", Guo et al. • David Stutz","url":"https://davidstutz.de/on-calibration-of-modern-neural-networks-guo-et-al/"},{"title":"On Calibration of Modern Neural Networks","url":"https://github.com/vlgiitr/papers_we_read/blob/master/summaries/Calibration_of_Neural_Nets.md"},{"title":"On Calibration of Modern Neural Networks","url":"https://arxiv.org/pdf/1706.04599"},{"title":"(Open Access) On Calibration of Modern Neural Networks (2017) | Chuan Guo | 4418 Citations","url":"https://scispace.com/papers/on-calibration-of-modern-neural-networks-5cc9ha8ohx"},{"title":"On Calibration of Modern Neural Networks","url":"https://proceedings.mlr.press/v70/guo17a/guo17a.pdf"},{"title":"Revisiting the Calibration of Modern Neural Networks","url":"https://arxiv.org/pdf/2106.07998"},{"title":"[PDF] On Calibration of Modern Neural Networks | Semantic Scholar","url":"https://www.semanticscholar.org/paper/On-Calibration-of-Modern-Neural-Networks-Guo-Pleiss/d65ce2b8300541414bfe51d03906fca72e93523c"},{"title":"On calibration of modern neural networks | Proceedings of the 34th International Conference on Machine Learning - Volume 70","url":"https://dl.acm.org/doi/10.5555/3305381.3305518"}]

Based on the search results, here is the information about the paper:

**Citation Information:**

The paper "On Calibration of Modern Neural Networks" was authored by Chuan Guo, Geoff Pleiss, Yu Sun, and Kilian Q. Weinberger and published at ICML 2017.

**Available DOI/Identifiers:**

- ArXiv ID: 1706.04599
- Published in Proceedings of the 34th International Conference on Machine Learning (PMLR 70), 2017
- ACM DOI reference: Available through the ACM Digital Library for ICML'17

**Paper Summary:**

The paper addresses confidence calibration – the pro
…[truncated 475 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_research_bib_completion_20260521T073708",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 40 · 2026-05-21T07:42:36.387694+00:00_

Web search results for query: "Conneau "Unsupervised Cross-lingual Representation Learning at Scale" XLM-R ACL 2020 doi"

Links: [{"title":"Unsupervised Cross-lingual Representation Learning at Scale - ACL Anthology","url":"https://aclanthology.org/2020.acl-main.747/"},{"title":"(PDF) Unsupervised Cross-lingual Representation Learning at Scale (2020) | Alexis Conneau | 6886 Citations","url":"https://scispace.com/papers/unsupervised-cross-lingual-representation-learning-at-scale-2o09354dx5"},{"title":"[1911.02116] Unsupervised Cross-lingual Representation Learning at Scale","url":"https://arxiv.org/abs/1911.02116"},{"title":"ACL2020: Unsupervised Cross-lingual Representation Learning at Scale","url":"https://virtual.acl2020.org/paper_main.747.html"},{"title":"Conneau, A., et al. (2020) Unsupervised Cross-Lingual Representation Learning at Scale. Proceedings of ACL 2020, 5-10 July 2020, 8440-8451. - References - Scientific Research Publishing","url":"https://www.scirp.org/reference/referencespapers?referenceid=4031261"},{"title":"Unsupervised Cross-lingual Representation Learning at Scale","url":"https://arxiv.org/pdf/1911.02116"},{"title":"[PDF] Unsupervised Cross-lingual Representation Learning at Scale | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Unsupervised-Cross-lingual-Representation-Learning-Conneau-Khandelwal/6fec3e579c7cd4f13bdabbee2b6ac2e8ff5941c6"},{"title":"Unsupervised Cross-lingual Representation Learning at Scale","url":"https://www.researchgate.net/publication/343298778_Unsupervised_Cross-lingual_Representation_Learning_at_Scale"},{"title":"Brief Review — XLM-R: Unsupervised Cross-lingual Representation Learning at Scale | by Sik-Ho Tsang | Medium","url":"https://sh-tsang.medium.com/brief-review-xlm-r-unsupervised-cross-lingual-representation-learning-at-scale-0a51dc980900"}]

Based on the search results, I found the paper you're looking for:

**Paper:** "Unsupervised Cross-lingual Representation Learning at Scale" by Alexis Connea
…[truncated 691 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_research_bib_completion_20260521T073708",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 41 · 2026-05-21T07:42:36.387881+00:00_

Web search results for query: "Fedus "Switch Transformers" JMLR 2022 doi trillion parameter"

Links: [{"title":"Switch Transformers: Scaling to Trillion Parameter Models with Simple and Efficient Sparsity","url":"https://jmlr.org/papers/v23/21-0998.html"},{"title":"Switch transformers: scaling to trillion parameter models with simple and efficient sparsity: The Journal of Machine Learning Research: Vol 23, No 1","url":"https://dl.acm.org/doi/abs/10.5555/3586589.3586709"},{"title":"GitHub - kyegomez/SwitchTransformers: Implementation of Switch Transformers from the paper: \"Switch Transformers: Scaling to Trillion Parameter Models with Simple and Efficient Sparsity\" · GitHub","url":"https://github.com/kyegomez/SwitchTransformers"},{"title":"[2101.03961] Switch Transformers: Scaling to Trillion Parameter Models with Simple and Efficient Sparsity","url":"https://arxiv.org/abs/2101.03961"},{"title":"Switch Transformers: Scaling to Trillion Parameter Models with Simple and Efficient Sparsity | Request PDF","url":"https://www.researchgate.net/publication/348403003_Switch_Transformers_Scaling_to_Trillion_Parameter_Models_with_Simple_and_Efficient_Sparsity"},{"title":"Switch transformers: Scaling to trillion parameter models with simple and efficient sparsity","url":"https://alastairreid.github.io/RelatedWork/papers/fedus:arxiv:2021/"},{"title":"[PDF] Switch Transformers: Scaling to Trillion Parameter Models with Simple and Efficient Sparsity | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Switch-Transformers:-Scaling-to-Trillion-Parameter-Fedus-Zoph/fdacf2a732f55befdc410ea927091cad3b791f13"},{"title":"Switch Transformers: Scaling to Trillion Parameter Models ...","url":"https://www.cs.princeton.edu/courses/archive/fall22/cos597G/lectures/lec16.pdf"},{"title":"Switch Transformers: Scaling to Trillion Parameter Models ...","url":"https://www.jmlr.org/papers/volume23/21-0998/21-0998.pdf"}]

Based on the search results, I found the paper you're looking for:


…[truncated 1044 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_research_bib_completion_20260521T073708",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 42 · 2026-05-21T07:42:36.388051+00:00_

Web search results for query: "Lord 1980 "Applications of Item Response Theory to Practical Testing Problems" ISBN Erlbaum"

Links: [{"title":"Boekbesprekingen: Applications of item response theory to practical testing problems / F.M. Lord. - Hillsdale, N.J : Erlbaum Associates, 1980. - ISBN 0-89859-006-X - University of Twente Research Information","url":"https://research.utwente.nl/en/publications/boekbesprekingen-fm-lord-applications-of-item-response-theory-to-/"},{"title":"Applications Of Item Response Theory To Practical Testing Problems 089859006X, 9780898590067 - DOKUMEN.PUB","url":"https://dokumen.pub/applications-of-item-response-theory-to-practical-testing-problems-089859006x-9780898590067.html"},{"title":"Applications of Item Response Theory To Practical Testing Problems: Frederic M. Lord: 9780898590067: Amazon.com: Books","url":"https://www.amazon.com/Applications-Response-Practical-Testing-Problems/dp/089859006X"},{"title":"(PDF) Some Applications of Item Response Theory to Testing","url":"https://www.researchgate.net/publication/265667091_Some_Applications_of_Item_Response_Theory_to_Testing"},{"title":"ERIC - ED312280 - Applications of Item Response Theory to Practical Testing Problems., 1980","url":"https://eric.ed.gov/?id=ED312280"},{"title":"Applications of Item Response Theory To Practical Testing Problems - Frederic M. Lord: 9780898590067 - AbeBooks","url":"https://www.abebooks.com/9780898590067/Applications-Item-Response-Theory-Practical-089859006X/plp"},{"title":"Applications of Item Response Theory to Practical Testing Problems - Frederic M. Lord - Google Books","url":"https://books.google.com/books/about/Applications_of_Item_Response_Theory_to.html?id=_qu8YGkdTvwC"},{"title":"Lord, F. M. (1980). &lt;i>Applications of item response theory to practical testing problems&lt;/i>. Hillsdale, New Jersey: Lawrence Erlbaum Associates.","url":"https://www.sciepub.com/reference/304019"},{"title":"Applications of Item Response Theory To Practical Testing Proble
…[truncated 904 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_research_bib_completion_20260521T073708",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 43 · 2026-05-21T07:42:36.388280+00:00_

Web search results for query: "Ben-David "A Theory of Learning from Different Domains" Machine Learning 2010 doi"

Links: [{"title":"A theory of learning from different domains","url":"https://www.mendeley.com/catalogue/8c104c01-e1b3-32e9-a56a-a1f6221c4b31/"},{"title":"A theory of learning from different domains | Machine Learning | Springer Nature Link","url":"https://link.springer.com/article/10.1007/s10994-009-5152-4"},{"title":"[PDF] A theory of learning from different domains | Semantic Scholar","url":"https://www.semanticscholar.org/paper/A-theory-of-learning-from-different-domains-Ben-David-Blitzer/66d398aeaeb7ec24ededb1adaa4b4f09a6c1bcde"},{"title":"Ben-David 2010 - A Theory of Learning From Different Domains PDF | PDF | Statistical Classification | Bias Of An Estimator","url":"https://www.scribd.com/document/320914333/Ben-David-2010-A-theory-of-learning-from-different-domains-pdf"},{"title":"A theory of learning from different domains","url":"https://escholarship.org/uc/item/2nv1j9sc"},{"title":"Shai Ben-David","url":"https://cs.uwaterloo.ca/~shai/da.html"},{"title":"(PDF) A theory of learning from different domains","url":"https://www.researchgate.net/publication/220343859_A_theory_of_learning_from_different_domains"},{"title":"A theory of learning from different domains","url":"https://research.google/pubs/pub36364/"},{"title":"A theory of learning from different domains | Machine Language","url":"https://dl.acm.org/doi/10.1007/s10994-009-5152-4"}]

Based on the search results, I found the complete citation information for the Ben-David paper:

Ben-David, S., Blitzer, J., Crammer, K., Kulesza, A., Pereira, F., & Vaughan, J. W. (2010). A theory of learning from different domains. Machine Learning, 79(1–2), 151–175. https://doi.org/10.1007/s10994-009-5152-4

The paper addresses the problem of learning classifiers that generalize across different domains, investigating conditions under which source domain classifiers perform well on target domains and how to
…[truncated 153 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_research_bib_completion_20260521T073708",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 44 · 2026-05-21T07:42:36.388454+00:00_

Web search results for query: "Kornblith "Similarity of Neural Network Representations Revisited" CKA ICML 2019 doi"

Links: [{"title":"Similarity of Neural Network Representations Revisited","url":"https://vitalab.github.io/article/2021/01/28/SimilarityNeuralNets.html"},{"title":"Similarity of Neural Network Representations Revisited","url":"https://cka-similarity.github.io/"},{"title":"Simon Kornblith, Mohammad Norouzi, Honglak Lee, Geoffrey Hinton","url":"https://icml.cc/media/Slides/icml/2019/halla(13-11-00)-13-12-15-4871-similarity_of_n.pdf"},{"title":"Similarity of Neural Network Representations Revisited","url":"https://icml.cc/media/icml-2019/Slides/4871.pdf"},{"title":"Similarity of Neural Network Representations Revisited | Request PDF","url":"https://www.researchgate.net/publication/332799564_Similarity_of_Neural_Network_Representations_Revisited"},{"title":"SIMILARITY OF NEURAL NETWORK REPRESENTA","url":"https://debug-ml-iclr2019.github.io/cameraready/DebugML-19_paper_9.pdf"},{"title":"[1905.00414] Similarity of Neural Network Representations Revisited","url":"https://arxiv.org/abs/1905.00414"},{"title":"[PDF] Similarity of Neural Network Representations Revisited | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Similarity-of-Neural-Network-Representations-Kornblith-Norouzi/726320cdbd04804ffa8f3a78c095bd1b55a2a695"},{"title":"Similarity of Neural Network Representations Revisited","url":"http://proceedings.mlr.press/v97/kornblith19a/kornblith19a.pdf"},{"title":"Similarity of Neural Network Representations Revisited","url":"https://arxiv.org/pdf/1905.00414"}]

Based on the search results, I found comprehensive information about this paper. The paper is by Simon Kornblith, Mohammad Norouzi, Honglak Lee, and Geoffrey Hinton from ICML 2019.

The paper introduces a similarity index that measures the relationship between representational similarity matrices and does not suffer from limitations of CCA, which is equivalent to centered kernel alig
…[truncated 619 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_research_bib_completion_20260521T073708",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool call

_source line 45 · 2026-05-21T07:42:36.388628+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Hewitt Liang \"Designing and Interpreting Probes with Control Tasks\" EMNLP 2019 doi"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_research_bib_completion_20260521T073708",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Hewitt Liang \"Designing and Interpreting Probes with Control Tasks\" EMNLP 2019 doi"
  }
}
```

</details>

---

### Tool call

_source line 46 · 2026-05-21T07:42:36.388801+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Voita Titov \"Information-Theoretic Probing with Minimum Description Length\" EMNLP 2020 doi"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_research_bib_completion_20260521T073708",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Voita Titov \"Information-Theoretic Probing with Minimum Description Length\" EMNLP 2020 doi"
  }
}
```

</details>

---

### Tool call

_source line 47 · 2026-05-21T07:42:36.388922+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Karandikar \"Soft Calibration Objectives for Neural Networks\" NeurIPS 2021 doi"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_research_bib_completion_20260521T073708",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Karandikar \"Soft Calibration Objectives for Neural Networks\" NeurIPS 2021 doi"
  }
}
```

</details>

---

### Tool call

_source line 48 · 2026-05-21T07:42:36.389035+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Angelopoulos Bates \"Conformal Prediction: A Gentle Introduction\" 2023 arxiv"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_research_bib_completion_20260521T073708",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Angelopoulos Bates \"Conformal Prediction: A Gentle Introduction\" 2023 arxiv"
  }
}
```

</details>

---

### Tool call

_source line 49 · 2026-05-21T07:42:36.389151+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"Confidence Manifold\" \"Geometric Structure\" correctness representations language models 2026 authors arxiv"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_research_bib_completion_20260521T073708",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"Confidence Manifold\" \"Geometric Structure\" correctness representations language models 2026 authors arxiv"
  }
}
```

</details>

---

### Tool call

_source line 50 · 2026-05-21T07:42:36.389260+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Zhao \"On Learning Invariant Representations for Domain Adaptation\" ICML 2019 authors doi"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_research_bib_completion_20260521T073708",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Zhao \"On Learning Invariant Representations for Domain Adaptation\" ICML 2019 authors doi"
  }
}
```

</details>

---

### Tool result

_source line 51 · 2026-05-21T07:42:36.389400+00:00_

Web search results for query: "Hewitt Liang "Designing and Interpreting Probes with Control Tasks" EMNLP 2019 doi"

Links: [{"title":"Designing and Interpreting Probes with Control Tasks","url":"https://bibbase.org/network/publication/hewitt-liang-designingandinterpretingprobeswithcontroltasks-2019"},{"title":"Designing and Interpreting Probes with Control Tasks - ACL Anthology","url":"https://aclanthology.org/D19-1275/"},{"title":"Designing and Interpreting Probes with Control Tasks. | BibSonomy","url":"https://www.bibsonomy.org/bibtex/1c7c8f6e4720c00cfb0b395c4827d7155"},{"title":"Designing and Interpreting Probes with Control Tasks | papers_we_read","url":"https://vlgiitr.github.io/papers_we_read/summaries/control_tasks.html"},{"title":"Designing and Interpreting Probes · John Hewitt","url":"https://www.cs.columbia.edu/~johnhew/interpreting-probes.html"},{"title":"Designing and Interpreting Probes with Control Tasks","url":"https://arxiv.org/pdf/1909.03368"},{"title":"[1909.03368] Designing and Interpreting Probes with Control Tasks","url":"https://arxiv.org/abs/1909.03368"},{"title":"Designing and Interpreting Probes with Control Tasks Percy Liang John Hewitt","url":"https://www.cs.columbia.edu/~johnhew/public/hewitt2019control_slides.pdf"},{"title":"[PDF] Designing and Interpreting Probes with Control Tasks | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Designing-and-Interpreting-Probes-with-Control-Hewitt-Liang/199ff73d2f728e997f860b62a2322823d3e3d9e8"}]

Based on the search results, here is the information about the paper:

**"Designing and Interpreting Probes with Control Tasks"** by John Hewitt and Percy Liang was published in the Proceedings of the 2019 Conference on Empirical Methods in Natural Language Processing and the 9th International Joint Conference on Natural Language Processing (EMNLP-IJCNLP), pages 2733–2743.

**DOI:** 10.18653/v1/D19-1275

**arXiv ID:** arXiv:1909.03368

The paper proposes control tasks that help identify wheth
…[truncated 321 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_research_bib_completion_20260521T073708",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 52 · 2026-05-21T07:42:36.389577+00:00_

Web search results for query: "Voita Titov "Information-Theoretic Probing with Minimum Description Length" EMNLP 2020 doi"

Links: [{"title":"Information-Theoretic Probing with Minimum Description Length - ACL Anthology","url":"https://aclanthology.org/2020.emnlp-main.14/"},{"title":"[Quick Review] Information-Theoretic Probing with Minimum Description Length","url":"https://liner.com/review/informationtheoretic-probing-with-minimum-description-length"},{"title":"Information-Theoretic Probing with Minimum Description Length | Request PDF","url":"https://www.researchgate.net/publication/347232984_Information-Theoretic_Probing_with_Minimum_Description_Length"},{"title":"Information-Theoretic Probing with MDL","url":"https://lena-voita.github.io/posts/mdl_probes.html"},{"title":"[PDF] Information-Theoretic Probing with Minimum Description Length | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Information-Theoretic-Probing-with-Minimum-Length-Voita-Titov/f4b585c9a79dfce0807b445a09036ea0f9cbcdce"},{"title":"GitHub - lena-voita/description-length-probing: This is a repository with the code for the EMNLP 2020 paper \"Information-Theoretic Probing with Minimum Description Length\"","url":"https://github.com/lena-voita/description-length-probing"},{"title":"Notes on: Information-Theoretic Probing with Minimum Description Length by Voita, E., & Titov, I. (2020) - Hugo Cisneros","url":"https://hugocisneros.com/notes/voitainformationtheoreticprobingminimum2020/"},{"title":"File Finder · lena-voita/description-length-probing","url":"https://github.com/lena-voita/description-length-probing/find/master"},{"title":"dblp: Elena Voita","url":"https://dblp.org/pid/220/4162.html"},{"title":"description-length-probing/control_tasks/example/config/emnlp19-cluster/error-analysis/ptb-pos-c0-rank1000-1hid-ELMo1-run2.yaml at master · lena-voita/description-length-probing","url":"https://github.com/lena-voita/description-length-probing/blob/master/control_tasks/example/config
…[truncated 935 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_research_bib_completion_20260521T073708",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 53 · 2026-05-21T07:42:36.389783+00:00_

Web search results for query: "Angelopoulos Bates "Conformal Prediction: A Gentle Introduction" 2023 arxiv"

Links: [{"title":"A Gentle Introduction to Conformal Time Series Forecasting","url":"https://arxiv.org/pdf/2511.13608"},{"title":"Conformal Prediction: A Gentle Introduction | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Conformal-Prediction:-A-Gentle-Introduction-Angelopoulos-Bates/ed112ef477d496a3b45f79fc5ef466d3fe77d066"},{"title":"Publications - Anastasios Angelopoulos","url":"https://people.eecs.berkeley.edu/~angelopoulos/publications/"},{"title":"A Gentle Introduction to Conformal Prediction and Distribution-Free Uncertainty Quantification","url":"https://arxiv.org/html/2107.07511v6"},{"title":"[2107.07511] A Gentle Introduction to Conformal Prediction and Distribution-Free Uncertainty Quantification","url":"https://arxiv.org/abs/2107.07511"},{"title":"A Gentle Introduction to Conformal Prediction and Distribution-Free Uncertainty Quantification","url":"https://www.researchgate.net/publication/353284898_A_Gentle_Introduction_to_Conformal_Prediction_and_Distribution-Free_Uncertainty_Quantification"},{"title":"A Gentle Introduction to Conformal Prediction and Distribution-Free Uncertainty Quantification - ADS","url":"https://ui.adsabs.harvard.edu/abs/2021arXiv210707511A/abstract"},{"title":"Conformal Prediction: : A Gentle Introduction: Foundations and Trends® in Machine Learning: Vol 16, No 4","url":"https://dl.acm.org/doi/10.1561/2200000101"}]

I found the paper you're looking for. The paper "Conformal Prediction: A Gentle Introduction" by Anastasios N. Angelopoulos and Stephen Bates was published in March 2023. 

It was published in Foundations and Trends in Machine Learning, volume 16, pages 494-591. The paper is available through Now Publishers, Inc.

Additionally, there is an earlier arxiv version of a related work: Angelopoulos and Bates also published "A Gentle Introduction to Conformal Prediction and Distribution-Free Uncertaint
…[truncated 205 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_research_bib_completion_20260521T073708",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 54 · 2026-05-21T07:42:36.389964+00:00_

Web search results for query: "Karandikar "Soft Calibration Objectives for Neural Networks" NeurIPS 2021 doi"

Links: [{"title":"[Quick Review] Soft Calibration Objectives for Neural Networks","url":"https://liner.com/review/soft-calibration-objectives-for-neural-networks"},{"title":"Soft Calibration Objectives for Neural Networks - researchr publication","url":"https://researchr.org/publication/KarandikarCTLSM21"},{"title":"Soft Calibration Objectives for Neural Networks","url":"https://proceedings.neurips.cc/paper/2021/hash/f8905bd3df64ace64a68e154ba72f24c-Abstract.html"},{"title":"Soft Calibration Objectives for Neural Networks","url":"https://research.google/pubs/pub50844/"},{"title":"[2108.00106] Soft Calibration Objectives for Neural Networks","url":"https://arxiv.org/abs/2108.00106"},{"title":"Soft Calibration Objectives for Neural Networks Archit Karandikar∗","url":"https://openreview.net/pdf?id=-tVD13hOsQ3"},{"title":"[PDF] Soft Calibration Objectives for Neural Networks | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Soft-Calibration-Objectives-for-Neural-Networks-Karandikar-Cain/7416930f69bec3d0b712b9dd3b5e7aa6d3dfec58"},{"title":"Soft Calibration Objectives for Neural Networks Archit Karandikar∗","url":"https://proceedings.neurips.cc/paper/2021/file/f8905bd3df64ace64a68e154ba72f24c-Paper.pdf"},{"title":"Soft calibration objectives for neural networks | Proceedings of the 35th International Conference on Neural Information Processing Systems","url":"https://dl.acm.org/doi/10.5555/3540261.3542539"}]

Based on the search results, here's what I found about this paper:

The paper "Soft Calibration Objectives for Neural Networks" was authored by Archit Karandikar, Nicholas Cain, Dustin Tran, Balaji Lakshminarayanan, Jonathon Shlens, Michael C. Mozer, and Becca Roelofs, and was published in Advances in Neural Information Processing Systems 34 (NeurIPS 2021) in December 2021.

The paper proposes Soft Calibration Objectives, SB-ECE and S-AvUC, wh
…[truncated 647 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_research_bib_completion_20260521T073708",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 55 · 2026-05-21T07:42:36.390134+00:00_

Web search results for query: "Zhao "On Learning Invariant Representations for Domain Adaptation" ICML 2019 authors doi"

Links: [{"title":"On learning invariant representations for domain adaptation - Illinois Experts","url":"https://experts.illinois.edu/en/publications/on-learning-invariant-representations-for-domain-adaptation/"},{"title":"On Learning Invariant Representations for Domain Adaptation. | BibSonomy","url":"https://www.bibsonomy.org/bibtex/17f7e62074e77e75ad75658cb31495002"},{"title":"dblp: On Learning Invariant Representations for Domain Adaptation.","url":"https://dblp.org/rec/conf/icml/0002CZG19.html"},{"title":"On Learning Invariant Representation for Domain Adaptation","url":"https://arxiv.org/pdf/1901.09453"},{"title":"On Learning Invariant Representations for Domain Adaptation","url":"http://proceedings.mlr.press/v97/zhao19a/zhao19a.pdf"},{"title":"On Learning Invariant Representations for Domain Adaptation","url":"https://hanzhaoml.github.io/papers/ICML2019/poster.pdf"},{"title":"On Learning Invariant Representations for Domain Adaptation – Machine Learning Blog | ML@CMU | Carnegie Mellon University","url":"https://blog.ml.cmu.edu/2019/09/13/on-learning-invariant-representations-for-domain-adaptation/"},{"title":"Class-Imbalanced Domain Adaptation: An Empirical Odyssey | Computer Vision – ECCV 2020 Workshops","url":"https://dl.acm.org/doi/10.1007/978-3-030-66415-2_38"},{"title":"ICML 2019 On Learning Invariant Representations for Domain Adaptation Oral","url":"https://icml.cc/virtual/2019/oral/4357"}]

Based on the search results, here is the information about the paper:

**Authors:** Zhao, H., des Combes, R. T., Zhang, K., & Gordon, G. J.

**Full Citation:** On learning invariant representations for domain adaptation. In 36th International Conference on Machine Learning, ICML 2019 (pp. 12985-12999)

**DOI/Pages:** Pages 7523-7532 in Proceedings of Machine Learning Research, volume 97

**Additional Details:**
- Authors are from Carnegie Mellon
…[truncated 295 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_research_bib_completion_20260521T073708",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 56 · 2026-05-21T07:42:36.390305+00:00_

Web search results for query: ""Confidence Manifold" "Geometric Structure" correctness representations language models 2026 authors arxiv"

Links: [{"title":"The Confidence Manifold: Geometric Structure of Correctness Representations in Language Models","url":"https://arxiv.org/html/2602.08159v1"},{"title":"The Confidence Manifold - Seongland","url":"https://seongland.com/article/confidence-manifold/"},{"title":"Confidence Geometry Reveals Trace-Level Correctness in Large Language Model Reasoning","url":"https://arxiv.org/html/2605.16824"},{"title":"[2605.16824] Confidence Geometry Reveals Trace-Level Correctness in Large Language Model Reasoning","url":"https://arxiv.org/abs/2605.16824"},{"title":"The Confidence Manifold:","url":"https://www.arxiv.org/pdf/2602.08159"},{"title":"Trust in One Round: Confidence Estimation for Large Language Models via Structural Signals","url":"https://arxiv.org/html/2602.00977"},{"title":"Trust in One Round: Confidence Estimation for Large Language Models via Structural Signals","url":"https://arxiv.org/pdf/2602.00977"},{"title":"Latent Trajectory Dynamics in Large Language Models: A Manifold Evolution Framework with Empirical Validation","url":"https://arxiv.org/html/2505.20340"},{"title":"A Geometric Perspective on Next-Token Prediction in Large Language Models: Three Emerging Phases","url":"https://arxiv.org/html/2605.09011v1"}]

I found a paper matching your query! Here are the results:

## Primary Result

The paper "The Confidence Manifold: Geometric Structure of Correctness Representations in Language Models" demonstrates that the discriminative signal for correctness concentrates in 3–8 dimensions, substantially lower than the high-dimensional activation space. The paper was published on February 8, 2026.

The research studied 9 models across 5 architecture families, from 124M-parameter GPT-2 to 7B-parameter Mistral. A 7B model with 4096-dimensional hidden states encodes correctness in just 5 dimensions, 0.12% of its represent
…[truncated 762 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_research_bib_completion_20260521T073708",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool call

_source line 57 · 2026-05-21T07:42:36.390478+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "arxiv 2602.08159 \"Confidence Manifold\" authors list"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_research_bib_completion_20260521T073708",
  "tool": "WebSearch",
  "tool_args": {
    "query": "arxiv 2602.08159 \"Confidence Manifold\" authors list"
  }
}
```

</details>

---

### Tool call

_source line 58 · 2026-05-21T07:42:36.390601+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Pires \"How Multilingual is Multilingual BERT\" ACL 2019 doi authors"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_research_bib_completion_20260521T073708",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Pires \"How Multilingual is Multilingual BERT\" ACL 2019 doi authors"
  }
}
```

</details>

---

### Tool call

_source line 59 · 2026-05-21T07:42:36.390757+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Wu Dredze \"Beto Bentz Becas\" cross-lingual BERT EMNLP 2019 doi"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_research_bib_completion_20260521T073708",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Wu Dredze \"Beto Bentz Becas\" cross-lingual BERT EMNLP 2019 doi"
  }
}
```

</details>

---

### Tool call

_source line 60 · 2026-05-21T07:42:36.390876+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Belinkov \"Probing Classifiers: Promises Shortcomings Advances\" Computational Linguistics 2022 doi"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_research_bib_completion_20260521T073708",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Belinkov \"Probing Classifiers: Promises Shortcomings Advances\" Computational Linguistics 2022 doi"
  }
}
```

</details>

---

### Tool call

_source line 61 · 2026-05-21T07:42:36.390988+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Xiao 2025 ACL \"knowledge boundary\" multilingual LLM authors full list doi aclanthology"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_research_bib_completion_20260521T073708",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Xiao 2025 ACL \"knowledge boundary\" multilingual LLM authors full list doi aclanthology"
  }
}
```

</details>

---

### Tool result

_source line 62 · 2026-05-21T07:42:36.391124+00:00_

Web search results for query: "Pires "How Multilingual is Multilingual BERT" ACL 2019 doi authors"

Links: [{"title":"How Multilingual is Multilingual BERT? - ACL Anthology","url":"https://aclanthology.org/P19-1493/"},{"title":"Machine Translation Weekly 15: How Multilingual is Multiligual BERT? | Jindřich’s blog","url":"https://jlibovicky.github.io/2019/10/18/MT-Weekly-Multilingual-BERT.html"},{"title":"[1906.01502] How multilingual is Multilingual BERT?","url":"https://arxiv.org/abs/1906.01502"},{"title":"[Quick Review] How Multilingual is Multilingual BERT?","url":"https://liner.com/review/how-multilingual-is-multilingual-bert"},{"title":"Multilingual BERT","url":"https://www.summarizepaper.com/en/arxiv-id/1906.01502v1/"},{"title":"Paper page - How multilingual is Multilingual BERT?","url":"https://paperswithcode.com/paper/how-multilingual-is-multilingual-bert"},{"title":"[PDF] How Multilingual is Multilingual BERT? | Semantic Scholar","url":"https://www.semanticscholar.org/paper/How-Multilingual-is-Multilingual-BERT-Pires-Schlinger/809cc93921e4698bde891475254ad6dfba33d03b"},{"title":"How Multilingual is Multilingual BERT? | Request PDF","url":"https://www.researchgate.net/publication/335783767_How_Multilingual_is_Multilingual_BERT"},{"title":"How multilingual is Multilingual BERT? Telmo Pires∗ Eva Schlinger Dan Garrette","url":"http://www.dhgarrette.com/papers/pires_multilingual_bert_acl2019.pdf"},{"title":"How multilingual is Multilingual BERT?","url":"https://arxiv.org/pdf/1906.01502"}]

Based on the search results, here is the information about the paper:

**Title:** How Multilingual is Multilingual BERT?

**Authors:** Telmo Pires, Eva Schlinger, and Dan Garrette

**Conference:** Proceedings of the 57th Annual Meeting of the Association for Computational Linguistics, July 2019, Florence, Italy

**DOI:** 10.18653/v1/P19-1493

**Pages:** 4996–5001


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_research_bib_completion_20260521T073708",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 63 · 2026-05-21T07:42:36.391260+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Zhou LACE \"Beyond the Final Layer\" arxiv 2510.03136 authors full list"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_research_bib_completion_20260521T073708",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Zhou LACE \"Beyond the Final Layer\" arxiv 2510.03136 authors full list"
  }
}
```

</details>

---

### Tool result

_source line 64 · 2026-05-21T07:42:36.391403+00:00_

Web search results for query: "Wu Dredze "Beto Bentz Becas" cross-lingual BERT EMNLP 2019 doi"

Links: [{"title":"Beto, Bentz, Becas: The Surprising Cross-Lingual Effectiveness of BERT - researchr publication","url":"https://researchr.org/publication/WuD19-8"},{"title":"Beto, Bentz, Becas: The surprising cross-lingual effectiveness of Bert - Johns Hopkins University","url":"https://pure.johnshopkins.edu/en/publications/beto-bentz-becas-the-surprising-cross-lingual-effectiveness-of-be/"},{"title":"Beto, Bentz, Becas: The Surprising Cross-Lingual Effectiveness of BERT - ACL Anthology","url":"https://aclanthology.org/D19-1077/"},{"title":"CROSS-LINGUAL ABILITY OF MULTILINGUAL BERT","url":"https://openreview.net/pdf?id=HJeT3yrtDr"},{"title":"dblp: Beto, Bentz, Becas: The Surprising Cross-Lingual Effectiveness of BERT.","url":"https://dblp.org/rec/conf/emnlp/WuD19.html"},{"title":"[PDF] Beto, Bentz, Becas: The Surprising Cross-Lingual Effectiveness of BERT | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Beto,-Bentz,-Becas:-The-Surprising-Cross-Lingual-of-Wu-Dredze/2fa3f7ce620a1c7155daef6620dd6bb0e01934f3"},{"title":"(PDF) Beto, Bentz, Becas: The Surprising Cross-Lingual Effectiveness of BERT","url":"https://www.researchgate.net/publication/336997478_Beto_Bentz_Becas_The_Surprising_Cross-Lingual_Effectiveness_of_BERT"},{"title":"GitHub - shijie-wu/crosslingual-nlp: This repo supports various cross-lingual transfer learning & multilingual NLP models. · GitHub","url":"https://github.com/shijie-wu/crosslingual-nlp"},{"title":"[1904.09077] Beto, Bentz, Becas: The Surprising Cross-Lingual Effectiveness of BERT","url":"https://arxiv.org/abs/1904.09077"},{"title":"Beto, Bentz, Becas: The Surprising Cross-Lingual Effectiveness of BERT","url":"https://arxiv.org/pdf/1904.09077"}]

Based on the search results, here is the information about the paper:

**Title:** "Beto, Bentz, Becas: The Surprising Cross-Lingual Effectiveness of BERT" by Shijie Wu and Mark Dredze, pu
…[truncated 674 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_research_bib_completion_20260521T073708",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 65 · 2026-05-21T07:42:36.391592+00:00_

Web search results for query: "Belinkov "Probing Classifiers: Promises Shortcomings Advances" Computational Linguistics 2022 doi"

Links: [{"title":"@article{belinkov-2022-probing,","url":"https://aclanthology.org/2022.cl-1.7.bib"},{"title":"Probing Classifiers: Promises, Shortcomings, and Advances - ACL Anthology","url":"https://aclanthology.org/2022.cl-1.7/"},{"title":"Probing Classifiers: Promises, Shortcomings, and Advances - Technion - Israel Institute of Technology","url":"https://cris.technion.ac.il/en/publications/probing-classifiers-promises-shortcomings-and-advances/"},{"title":"Probing Classifiers: Promises, Shortcomings, and Advances - Israeli Research Community Portal","url":"https://cris.iucc.ac.il/en/publications/probing-classifiers-promises-shortcomings-and-advances/"},{"title":"Probing Classifiers: Promises, Shortcomings, and Advances | Computational Linguistics | MIT Press","url":"https://direct.mit.edu/coli/article/48/1/207/107571/Probing-Classifiers-Promises-Shortcomings-and"},{"title":"Yonatan Belinkov | publications","url":"https://belinkov.com/publications/publicationstype/"},{"title":"(PDF) Probing Classifiers: Promises, Shortcomings, and Advances","url":"https://www.researchgate.net/publication/355072709_Probing_Classifiers_Promises_Shortcomings_and_Advances"},{"title":"[2102.12452] Probing Classifiers: Promises, Shortcomings, and Advances","url":"https://arxiv.org/abs/2102.12452"}]

Based on the search results, here is the information for the paper:

**Publication Details:**

Title: "Probing Classifiers: Promises, Shortcomings, and Advances"
Author: Yonatan Belinkov
Journal: Computational Linguistics
Volume: 48, Issue: 1
Month: March
Year: 2022
Pages: 207–219
DOI: 10.1162/coli_a_00422
Publisher: MIT Press

The paper discusses how probing classifiers have emerged as a prominent methodology for interpreting deep neural network models in NLP, with the basic idea being that a classifier is trained to predict linguistic properties from a model's
…[truncated 120 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_research_bib_completion_20260521T073708",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 66 · 2026-05-21T07:42:36.391789+00:00_

Web search results for query: "Zhou LACE "Beyond the Final Layer" arxiv 2510.03136 authors full list"

Links: [{"title":"[2510.03136] Beyond the Final Layer: Intermediate Representations for Better Multilingual Calibration in Large Language Models","url":"https://arxiv.org/abs/2510.03136"},{"title":"Layer by Layer: Uncovering Hidden Representations in Language Models","url":"https://arxiv.org/pdf/2502.02013"},{"title":"Beyond the Final Layer: Intermediate Representations for Better Multilingual Calibration in Large Language Models","url":"https://arxiv.org/html/2510.03136"},{"title":"Suppressing Final Layer Hidden State Jumps in Transformer Pretraining","url":"https://arxiv.org/pdf/2601.18302"},{"title":"Multimodal Language Models See Better When They Look Shallower","url":"https://arxiv.org/pdf/2504.21447"}]

Based on the search results, the authors of the paper "Beyond the Final Layer: Intermediate Representations for Better Multilingual Calibration in Large Language Models" (arXiv 2510.03136) are: Ej Zhou, Caiqi Zhang, Tiancheng Hu, Chengzu Li, Nigel Collier, Ivan Vulić, and Anna Korhonen.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_research_bib_completion_20260521T073708",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 67 · 2026-05-21T07:42:36.391946+00:00_

Web search results for query: "Xiao 2025 ACL "knowledge boundary" multilingual LLM authors full list doi aclanthology"

Links: [{"title":"GitHub - DAMO-NLP-SG/LLM-Multilingual-Knowledge-Boundaries: [ACL 2025] Analyzing LLMs' Multilingual Knowledge Boundary Cognition Across Languages Through the Lens of Internal Representations","url":"https://github.com/DAMO-NLP-SG/LLM-Multilingual-Knowledge-Boundaries"},{"title":"Analyzing LLMs’ Knowledge Boundary Cognition Across Languages Through the Lens of Internal Representations - ACL Anthology","url":"https://aclanthology.org/2025.acl-long.1174/"},{"title":"Knowledge Boundary of Large Language Models: A Survey - ACL Anthology","url":"https://aclanthology.org/2025.acl-long.256/"},{"title":"The 2025 Conference on Empirical Methods in Natural Language Processing - ACL Anthology","url":"https://aclanthology.org/events/emnlp-2025/"},{"title":"Accepted Main Conference Papers - ACL 2025","url":"https://2025.aclweb.org/program/main_papers/"},{"title":"Analyzing LLMs' Knowledge Boundary Cognition Across ...","url":"https://aclanthology.org/2025.acl-long.1174.pdf"},{"title":"Accepted Papers - NAACL-HLT 2025","url":"https://2025.naacl.org/program/accepted_papers/"}]

Based on the search results, I found the paper you're looking for:

**Paper Title:** Analyzing LLMs' Knowledge Boundary Cognition Across Languages Through the Lens of Internal Representations

**Full Author List:** Chenghao Xiao, Hou Pong Chan, Hao Zhang, Mahani Aljunied, Lidong Bing, Noura Al Moubayed, and Yu Rong

**DOI:** 10.18653/v1/2025.acl-long.1174

**ACL Anthology URL:** https://aclanthology.org/2025.acl-long.1174/

**Conference:** Proceedings of the 63rd Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers)

**Year:** 2025

The paper presents the first study to analyze how LLMs recognize knowledge boundaries across different languages by probing their internal representations when processing known and unknown questions in multiple
…[truncated 114 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_research_bib_completion_20260521T073708",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 68 · 2026-05-21T07:42:36.392141+00:00_

Web search results for query: "arxiv 2602.08159 "Confidence Manifold" authors list"

Links: [{"title":"The Confidence Manifold:","url":"https://www.arxiv.org/pdf/2602.08159"},{"title":"The Confidence Manifold: Geometric Structure of Correctness Representations in Language Models","url":"https://arxiv.org/html/2602.08159v1"},{"title":"The Confidence Manifold - Seongland","url":"https://seongland.com/article/confidence-manifold/"},{"title":"The folded X-pattern is not necessarily a statistical signature of decision confidence","url":"https://www.biorxiv.org/content/10.1101/426635.full.pdf"},{"title":"A low-dimensional approximation of optimal confidence","url":"https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11299811/"},{"title":"EEG-MACS: Manifold Attention and Confidence Stratification for EEG-based Cross-Center Brain Disease Diagnosis under Unreliable Annotations","url":"https://arxiv.org/html/2405.00734v2"},{"title":"A low-dimensional approximation of optimal confidence","url":"https://www.biorxiv.org/content/10.1101/2023.03.15.532729.full.pdf"}]

I found information about the arxiv paper 2602.08159 titled "The Confidence Manifold: Geometric Structure of Correctness Representations in Language Models", but the search results don't include the complete authors list. The PDF and HTML versions are available on arxiv.org, but the search snippets don't display the author names.

Let me search more specifically for the authors:

Links: [{"title":"The Confidence Manifold: Geometric Structure of Correctness Representations in Language Models","url":"https://arxiv.org/html/2602.08159v1"},{"title":"The Confidence Manifold:","url":"https://www.arxiv.org/pdf/2602.08159"},{"title":"The Confidence Manifold - Seongland","url":"https://seongland.com/article/confidence-manifold/"},{"title":"Trust in One Round: Confidence Estimation for Large Language Models via Structural Signals","url":"https://arxiv.org/pdf/2602.00977"},{"title":"Attributing authorship via the perplexity of authori
…[truncated 2865 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_research_bib_completion_20260521T073708",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool call

_source line 69 · 2026-05-21T07:42:36.392314+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "arxiv 2601.12731 Civelli \"Shared Geometry of Difficulty\" authors full list"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_research_bib_completion_20260521T073708",
  "tool": "WebSearch",
  "tool_args": {
    "query": "arxiv 2601.12731 Civelli \"Shared Geometry of Difficulty\" authors full list"
  }
}
```

</details>

---

### Tool call

_source line 70 · 2026-05-21T07:42:36.392436+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Ravisankar DALI \"Can you map it to English\" EACL 2026 authors full list doi"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_research_bib_completion_20260521T073708",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Ravisankar DALI \"Can you map it to English\" EACL 2026 authors full list doi"
  }
}
```

</details>

---

### Tool call

_source line 71 · 2026-05-21T07:42:36.392550+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Ji \"Calibrating Verbal Uncertainty as a Linear Feature\" EMNLP 2025 authors doi arxiv 2503.14477"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_research_bib_completion_20260521T073708",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Ji \"Calibrating Verbal Uncertainty as a Linear Feature\" EMNLP 2025 authors doi arxiv 2503.14477"
  }
}
```

</details>

---

### Tool call

_source line 72 · 2026-05-21T07:42:36.392679+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Joshi Ahmad Modi \"Calibration Across Layers\" EMNLP 2025 doi arxiv 2511.00280"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_research_bib_completion_20260521T073708",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Joshi Ahmad Modi \"Calibration Across Layers\" EMNLP 2025 doi arxiv 2511.00280"
  }
}
```

</details>

---

### Tool call

_source line 73 · 2026-05-21T07:42:36.392795+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Liu Niehues \"Middle-Layer Representation Alignment\" ACL 2025 doi authors full list"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_research_bib_completion_20260521T073708",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Liu Niehues \"Middle-Layer Representation Alignment\" ACL 2025 doi authors full list"
  }
}
```

</details>

---

### Tool result

_source line 74 · 2026-05-21T07:42:36.392924+00:00_

Web search results for query: "arxiv 2601.12731 Civelli "Shared Geometry of Difficulty" authors full list"

Links: [{"title":"[2601.12731] A Shared Geometry of Difficulty in Multilingual Language Models","url":"https://arxiv.org/abs/2601.12731"},{"title":"Computer Science","url":"https://www.arxiv.org/list/cs/pastweek?skip=1688&show=50"},{"title":"A Shared Geometry of Difficulty in Multilingual Language Models","url":"https://arxiv.org/html/2601.12731"},{"title":"GeoLaux: A Benchmark for Evaluating MLLMs' Geometry Performance on Long-Step Problems Requiring Auxiliary Lines","url":"https://arxiv.org/pdf/2508.06226"},{"title":"Geometrical congruence, greedy navigability and myopic transfer in complex networks and brain connectomes","url":"https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9701786/"},{"title":"Guidewire Morphology as a Predictor of Vascular Tortuosity and Advancement Difficulties During Right Upper Limb Coronary Angiography","url":"https://www.medrxiv.org/content/10.64898/2025.12.21.25342793.full.pdf"}]

The full list of authors for arxiv 2601.12731 "A Shared Geometry of Difficulty in Multilingual Language Models" is:

1. Stefano Civelli (The University of Queensland)
2. Pietro Bernardelle (The University of Queensland)
3. Nicolò Brunello (Polytechnic University of Milan)
4. Gianluca Demartini (The University of Queensland)


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_research_bib_completion_20260521T073708",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 75 · 2026-05-21T07:42:36.393057+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Miao CORAL arxiv 2602.06022 authors \"Correctness-Optimized Residual Activation Lens\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_research_bib_completion_20260521T073708",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Miao CORAL arxiv 2602.06022 authors \"Correctness-Optimized Residual Activation Lens\""
  }
}
```

</details>

---

### Tool result

_source line 76 · 2026-05-21T07:42:36.393195+00:00_

Web search results for query: "Ravisankar DALI "Can you map it to English" EACL 2026 authors full list doi"

Links: [{"title":"Can you map it to English? The Role of Cross-Lingual Alignment in the Multilingual Performance of LLMs - ACL Anthology","url":"https://aclanthology.org/2026.eacl-long.225/"},{"title":"Kartik Ravisankar's research works","url":"https://www.researchgate.net/scientific-contributions/Kartik-Ravisankar-2310395112"},{"title":"[2504.09378] Can you map it to English? The Role of Cross-Lingual Alignment in Multilingual Performance of LLMs","url":"https://arxiv.org/abs/2504.09378"},{"title":"(PDF) Can you map it to English? The Role of Cross-Lingual Alignment in Multilingual Performance of LLMs","url":"https://www.researchgate.net/publication/390773780_Can_you_map_it_to_English_The_Role_of_Cross-Lingual_Alignment_in_Multilingual_Performance_of_LLMs"},{"title":"Social media text analytics of Malayalam–English code-mixed using deep learning","url":"https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9041283/"},{"title":"Similar does not mean same: ERP correlates of processing mental and physical experiencer verbs in Malayalam complex constructions","url":"https://www.biorxiv.org/content/10.1101/2025.05.21.655344.full.pdf"},{"title":"System and method for writing Indian languages using English alphabet","url":"https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/7177794"}]

Based on the search results, I found the paper you're looking for. Here are the details:

**Paper:** "Can you map it to English? The Role of Cross-Lingual Alignment in the Multilingual Performance of LLMs"

**Authors:** Kartik Ravisankar, HyoJung Han, Sarah Wiegreffe, and Marine Carpuat

**Conference:** Proceedings of the 19th Conference of the European Chapter of the Association for Computational Linguistics (Volume 1: Long Papers), pages 4854–4872, Rabat, Morocco

**Year:** 2026

**DOI:** The ACL Anthology link is: https://aclanthology.org/2026.eacl-long.225/

**arXiv identifie
…[truncated 309 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_research_bib_completion_20260521T073708",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 77 · 2026-05-21T07:42:36.393353+00:00_

Web search results for query: "Ji "Calibrating Verbal Uncertainty as a Linear Feature" EMNLP 2025 authors doi arxiv 2503.14477"

Links: [{"title":"Calibrating Verbal Uncertainty as a Linear Feature to Reduce Hallucinations","url":"https://arxiv.org/pdf/2503.14477"},{"title":"Calibrating Verbal Uncertainty as a Linear Feature to Reduce Hallucinations - ACL Anthology","url":"https://aclanthology.org/2025.emnlp-main.187/"},{"title":"[2503.14477] Calibrating Verbal Uncertainty as a Linear Feature to Reduce Hallucinations","url":"https://arxiv.org/abs/2503.14477"},{"title":"(PDF) Calibrating Verbal Uncertainty as a Linear Feature to Reduce Hallucinations","url":"https://www.researchgate.net/publication/389947447_Calibrating_Verbal_Uncertainty_as_a_Linear_Feature_to_Reduce_Hallucinations"},{"title":"arXiv:2505.23854v1 [cs.CL] 29 May 2025","url":"https://arxiv.org/pdf/2505.23854"},{"title":"dblp: Calibrating Verbal Uncertainty as a Linear Feature to Reduce Hallucinations.","url":"https://dblp.org/rec/journals/corr/abs-2503-14477.html"},{"title":"Teaching Language Models to Faithfully Express their Uncertainty","url":"https://arxiv.org/pdf/2510.12587"}]

Based on the search results, here's the information about the paper:

**Paper Title:** Calibrating Verbal Uncertainty as a Linear Feature to Reduce Hallucinations

**Authors:** Ziwei Ji, Lei Yu, Yeskendir Koishekenov, Yejin Bang, Anthony Hartshorn, Alan Schelten, Cheng Zhang, Pascale Fung, and Nicola Cancedda

**Venue:** Proceedings of the 2025 Conference on Empirical Methods in Natural Language Processing, pages 3769–3793, Suzhou, China

**DOI:** 10.18653/v1/2025.emnlp-main.187

**arXiv ID:** 2503.14477

**Main Contribution:** The paper discovers a linear verbal uncertainty feature (VUF) that controls model expression of uncertainty, and applies this insight to: (1) detect hallucinations arising from the miscalibration between high semantic uncertainty (SU) and low verbal uncertainty (VU); (2) mitigate hallucinations by in
…[truncated 210 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_research_bib_completion_20260521T073708",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 78 · 2026-05-21T07:42:36.393516+00:00_

Web search results for query: "Liu Niehues "Middle-Layer Representation Alignment" ACL 2025 doi authors full list"

Links: [{"title":"Middle-Layer Representation Alignment for Cross-Lingual Transfer in Fine-Tuned LLMs - ACL Anthology","url":"https://aclanthology.org/2025.acl-long.778/"},{"title":"Middle-Layer Representation Alignment for Cross-Lingual Transfer in Fine-Tuned LLMs | Request PDF","url":"https://www.researchgate.net/publication/394303200_Middle-Layer_Representation_Alignment_for_Cross-Lingual_Transfer_in_Fine-Tuned_LLMs"},{"title":"[2502.14830] Middle-Layer Representation Alignment for Cross-Lingual Transfer in Fine-Tuned LLMs","url":"https://arxiv.org/abs/2502.14830"},{"title":"Middle-Layer Representation Alignment for Cross-Lingual Transfer in Fine-Tuned LLMs","url":"https://arxiv.org/html/2502.14830v2"},{"title":"Middle-Layer Representation Alignment for Cross-Lingual Transfer in","url":"https://openreview.net/pdf/165a4c42ede4fa7182ef5ba60ec0669f5606b9b8.pdf"},{"title":"[Literature Review] Middle-Layer Representation Alignment for Cross-Lingual Transfer in Fine-Tuned LLMs","url":"https://www.themoonlight.io/en/review/middle-layer-representation-alignment-for-cross-lingual-transfer-in-fine-tuned-llms"},{"title":"Middle-Layer Representation Alignment for Cross-Lingual Transfer in Fine-Tuned LLMs","url":"https://arxiv.org/pdf/2502.14830"}]

Based on the search results, here is the information about the paper:

## Paper Details

**Title:** Middle-Layer Representation Alignment for Cross-Lingual Transfer in Fine-Tuned LLMs

**Authors:** Danni Liu and Jan Niehues

**Conference:** Proceedings of the 63rd Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers), pages 15979–15996, Vienna, Austria

**Year:** 2025

**DOI/ISBN:** 979-8-89176-251-0

**arXiv Version:** The paper is also available on arXiv as 2502.14830

**Affiliation:** Karlsruhe Institute of Technology, Germany

Note: The search results show this as a 2-author pape
…[truncated 286 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_research_bib_completion_20260521T073708",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 79 · 2026-05-21T07:42:36.393711+00:00_

Web search results for query: "Joshi Ahmad Modi "Calibration Across Layers" EMNLP 2025 doi arxiv 2511.00280"

Links: [{"title":"GitHub - Exploration-Lab/LLM-Calibration-Mechanism · GitHub","url":"https://github.com/Exploration-Lab/LLM-Calibration-Mechanism"},{"title":"Calibration Across Layers: Understanding Calibration Evolution in LLMs | Request PDF","url":"https://www.researchgate.net/publication/397421796_Calibration_Across_Layers_Understanding_Calibration_Evolution_in_LLMs"},{"title":"[2511.00280] Calibration Across Layers: Understanding Calibration Evolution in LLMs","url":"https://arxiv.org/abs/2511.00280"},{"title":"(PDF) Calibration Across Layers: Understanding Calibration Evolution in LLMs","url":"https://www.researchgate.net/publication/397231243_Calibration_Across_Layers_Understanding_Calibration_Evolution_in_LLMs"},{"title":"Beyond the Final Layer: Intermediate Representations for Better Multilingual Calibration in Large Language Models","url":"https://arxiv.org/pdf/2510.03136"},{"title":"Calibration Across Layers: Understanding Calibration Evolution in LLMs","url":"https://arxiv.org/pdf/2511.00280"}]

I found the paper you're looking for. Here are the details:

**Title:** "Calibration Across Layers: Understanding Calibration Evolution in LLMs"

**Authors:** Abhinav Joshi, Areeb Ahmad, and Ashutosh Modi

**Conference:** Proceedings of the 2025 Conference on Empirical Methods in Natural Language Processing (EMNLP 2025)

**ArXiv ID:** 2511.00280

**DOI:** 10.18653/v1/2025.emnlp-main.742

**Key Contributions:** The paper analyzes multiple open-weight models on the MMLU benchmark and uncovers a distinct confidence correction phase in the upper/later layers, where model confidence is actively recalibrated after decision certainty has been reached. Additionally, the researchers identify a low-dimensional calibration direction in the residual stream whose perturbation significantly improves calibration metrics (ECE and MCE) without harming accuracy.

The paper
…[truncated 241 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_research_bib_completion_20260521T073708",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 80 · 2026-05-21T07:42:36.393890+00:00_

Web search results for query: "Miao CORAL arxiv 2602.06022 authors "Correctness-Optimized Residual Activation Lens""

Links: [{"title":"[2602.06022] Correctness-Optimized Residual Activation Lens (CORAL): Transferrable and Calibration-Aware Inference-Time Steering","url":"https://arxiv.org/abs/2602.06022"},{"title":"Correctness-Optimized Residual Activation Lens (CORAL): Transferrable and Calibration-Aware Inference-Time Steering","url":"https://www.researchgate.net/publication/400505951_Correctness-Optimized_Residual_Activation_Lens_CORAL_Transferrable_and_Calibration-Aware_Inference-Time_Steering"},{"title":"Correctness-Optimized Residual Activation Lens : Transferrable and Calibration-Aware Inference-Time Steering","url":"http://paperreading.club/page?id=374945"},{"title":"Correctness-Optimized Residual Activation Lens (CORAL):","url":"https://arxiv.org/pdf/2602.06022"},{"title":"[Literature Review] Correctness-Optimized Residual Activation Lens (CORAL): Transferrable and Calibration-Aware Inference-Time Steering","url":"https://www.themoonlight.io/en/review/correctness-optimized-residual-activation-lens-coral-transferrable-and-calibration-aware-inference-time-steering"},{"title":"Correctness-Optimized Residual Activation Lens (CORAL): Transferrable and Calibration-Aware Inference-Time Steering","url":"https://arxiv.org/html/2602.06022v1"},{"title":"Correctness-Optimized Residual Activation Lens (CORAL): Transferrable and Calibration-Aware Inference-Time Steering | Cool Papers - Immersive Paper Discovery","url":"https://papers.cool/arxiv/2602.06022"},{"title":"The Reversible Residual Network: Backpropagation Without Storing   Activations","url":"https://arxiv.org/pdf/1707.04585"}]

Based on the search results, here's what I found about the paper:

## CORAL: Correctness-Optimized Residual Activation Lens (arXiv 2602.06022)

**Authors:** Miranda Muqing Miao, Young-Min Cho, and Lyle Ungar

**Overview:**
CORAL is a regularized inference-time steering method that capt
…[truncated 1271 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_research_bib_completion_20260521T073708",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 81 · 2026-05-21T07:42:36.394068+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Miao \"Closing the Confidence-Faithfulness Gap\" arxiv 2603.25052 authors full list"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_research_bib_completion_20260521T073708",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Miao \"Closing the Confidence-Faithfulness Gap\" arxiv 2603.25052 authors full list"
  }
}
```

</details>

---

### Tool call

_source line 82 · 2026-05-21T07:42:36.394188+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Khanmohammadi \"Calibrating LLM Confidence by Probing Perturbed Representation Stability\" EMNLP 2025 authors doi"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_research_bib_completion_20260521T073708",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Khanmohammadi \"Calibrating LLM Confidence by Probing Perturbed Representation Stability\" EMNLP 2025 authors doi"
  }
}
```

</details>

---

### Tool call

_source line 83 · 2026-05-21T07:42:36.394309+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Conneau XLM-RoBERTa ACL 2020 full authors list Khandelwal Goyal"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_research_bib_completion_20260521T073708",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Conneau XLM-RoBERTa ACL 2020 full authors list Khandelwal Goyal"
  }
}
```

</details>

---

### Tool result

_source line 84 · 2026-05-21T07:42:36.394438+00:00_

Web search results for query: "Miao "Closing the Confidence-Faithfulness Gap" arxiv 2603.25052 authors full list"

Links: [{"title":"Fugu-MT 論文翻訳(概要): Closing the Confidence-Faithfulness Gap in Large Language Models","url":"https://fugumt.com/fugumt/paper_check/2603.25052v1"},{"title":"[2603.25052v1] Closing the Confidence-Faithfulness Gap in Large Language Models","url":"https://arxiv.org/abs/2603.25052v1"},{"title":"[2603.25052] Closing the Confidence-Faithfulness Gap in Large Language Models","url":"https://arxiv.org/abs/2603.25052"},{"title":"Closing the Confidence-Faithfulness Gap in Large Language Models","url":"https://arxiv.org/html/2603.25052"},{"title":"Closing the Confidence-Faithfulness Gap in Large ...","url":"https://arxiv.org/pdf/2603.25052"},{"title":"Teaching Language Models to Faithfully Express their Uncertainty","url":"https://arxiv.org/pdf/2510.12587"},{"title":"Closing the Confidence-Faithfulness Gap in Large ...","url":"https://x.com/HEI/status/2037535763399651595"}]

Based on the search results, the authors of "Closing the Confidence-Faithfulness Gap in Large Language Models" (arXiv:2603.25052) are Miranda Muqing Miao and Lyle Ungar from University of Pennsylvania.

The paper appears to have only these two authors listed in the full author list.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_research_bib_completion_20260521T073708",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 85 · 2026-05-21T07:42:36.394595+00:00_

Web search results for query: "Khanmohammadi "Calibrating LLM Confidence by Probing Perturbed Representation Stability" EMNLP 2025 authors doi"

Links: [{"title":"Calibrating LLM Confidence by Probing Perturbed Representation Stability | Request PDF","url":"https://www.researchgate.net/publication/397423860_Calibrating_LLM_Confidence_by_Probing_Perturbed_Representation_Stability"},{"title":"Calibrating LLM Confidence by Probing Perturbed Representation Stability - ACL Anthology","url":"https://aclanthology.org/2025.emnlp-main.530/"},{"title":"[2505.21772] Calibrating LLM Confidence by Probing Perturbed Representation Stability","url":"https://arxiv.org/abs/2505.21772"},{"title":"Calibrating LLM Confidence by Probing Perturbed Representation Stability | AI Research Paper Details","url":"https://www.aimodels.fyi/papers/arxiv/calibrating-llm-confidence-by-probing-perturbed-representation"},{"title":"Calibrating LLM Confidence by Probing Perturbed Representation Stability","url":"https://arxiv.org/html/2505.21772v1"},{"title":"Calibrating LLM Confidence by Probing Perturbed Representation Stability","url":"https://arxiv.org/pdf/2505.21772"},{"title":"GitHub - Ledengary/CCPS: Calibrating LLM Confidence by Probing Perturbed Representation Stability","url":"https://github.com/ledengary/CCPS"},{"title":"Confidence-Guided Probing Methods","url":"https://www.emergentmind.com/topics/confidence-guided-probing-method"},{"title":"(PDF) Calibrating LLM Confidence by Probing Perturbed Representation Stability","url":"https://www.researchgate.net/publication/392168633_Calibrating_LLM_Confidence_by_Probing_Perturbed_Representation_Stability"},{"title":"dblp: Kundan Thind","url":"https://dblp.org/pid/359/8694.html"}]

Based on the search results, here is the information for the paper:

**Title:** Calibrating LLM Confidence by Probing Perturbed Representation Stability

**Authors:** Reza Khanmohammadi, Erfan Miahi, Mehrsa Mardikoraem, Simerjot Kaur, Ivan Brugere, Charese Smiley, Kundan
…[truncated 321 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_research_bib_completion_20260521T073708",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 86 · 2026-05-21T07:42:36.394779+00:00_

Web search results for query: "Conneau XLM-RoBERTa ACL 2020 full authors list Khandelwal Goyal"

Links: [{"title":"XLM-RoBERTa - Hugo Cisneros","url":"https://hugocisneros.com/notes/xlm_roberta/"},{"title":"Unsupervised Cross-lingual Representation Learning at Scale - ACL Anthology","url":"https://aclanthology.org/2020.acl-main.747/"},{"title":"Cross-Language Language Model (XLM) - GM-RKB","url":"https://www.gabormelli.com/RKB/Cross-Language_Language_Model_(XLM)"},{"title":"(PDF) Unsupervised Cross-lingual Representation Learning at Scale (2020) | Alexis Conneau | 6886 Citations","url":"https://scispace.com/papers/unsupervised-cross-lingual-representation-learning-at-scale-2o09354dx5"},{"title":"[PDF] Unsupervised Cross-lingual Representation Learning at Scale | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Unsupervised-Cross-lingual-Representation-Learning-Conneau-Khandelwal/6fec3e579c7cd4f13bdabbee2b6ac2e8ff5941c6"},{"title":"Unsupervised Cross-lingual Representation Learning at Scale","url":"https://www.researchgate.net/publication/343298778_Unsupervised_Cross-lingual_Representation_Learning_at_Scale"},{"title":"Conneau, A., et al. (2020) Unsupervised Cross-Lingual Representation Learning at Scale. Proceedings of ACL 2020, 5-10 July 2020, 8440-8451. - References - Scientific Research Publishing","url":"https://www.scirp.org/reference/referencespapers?referenceid=4031261"},{"title":"Cross-lingual Inductive Transfer to Detect Offensive Language","url":"https://arxiv.org/pdf/2007.03771"}]

Based on the search results, here is the full authors list for the XLM-RoBERTa paper published at ACL 2020:

Alexis Conneau, Kartikay Khandelwal, Naman Goyal, Vishrav Chaudhary, Guillaume Wenzek, Francisco Guzmán, Edouard Grave, Myle Ott, Luke Zettlemoyer, and Veselin Stoyanov.

The paper is titled "Unsupervised Cross-lingual Representation Learning at Scale" and was published in the Proceedings of the 58th Annual Meeting of the Association for Computational Lingu
…[truncated 110 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_research_bib_completion_20260521T073708",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 87 · 2026-05-21T07:42:36.394943+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "site:arxiv.org 2602.08159 \"Confidence Manifold\" authors"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_research_bib_completion_20260521T073708",
  "tool": "WebSearch",
  "tool_args": {
    "query": "site:arxiv.org 2602.08159 \"Confidence Manifold\" authors"
  }
}
```

</details>

---

### Tool result

_source line 88 · 2026-05-21T07:42:36.395093+00:00_

Web search results for query: "site:arxiv.org 2602.08159 "Confidence Manifold" authors"

Links: [{"title":"The Confidence Manifold:","url":"https://www.arxiv.org/pdf/2602.08159"},{"title":"The Confidence Manifold: Geometric Structure of Correctness Representations in Language Models","url":"https://arxiv.org/html/2602.08159v1"},{"title":"The Confidence Manifold - Seongland","url":"https://seongland.com/article/confidence-manifold/"},{"title":"Point Mass in the Confidence Distribution: Is it a Drawback or an   Advantage?","url":"https://arxiv.org/pdf/2310.09960"},{"title":"The folded X-pattern is not necessarily a statistical signature of decision confidence","url":"https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6822779/"},{"title":"The folded X-pattern is not necessarily a statistical signature of decision confidence","url":"https://www.biorxiv.org/content/10.1101/426635.full.pdf"},{"title":"Oracle complexities of augmented Lagrangian methods for nonsmooth   manifold optimization","url":"https://arxiv.org/pdf/2404.05121"},{"title":"A low-dimensional approximation of optimal confidence","url":"https://www.biorxiv.org/content/10.1101/2023.03.15.532729.full.pdf"},{"title":"The positive evidence bias in perceptual confidence is not post-decisional","url":"https://www.biorxiv.org/content/10.1101/2020.03.15.991513.full.pdf"}]

Based on the search results, I found information about the paper with arXiv ID 2602.08159, but the author names are not clearly visible in the snippets provided. The search results show that "The Confidence Manifold" characterizes the geometry of correctness representations across 9 models from 5 architecture families, with a structure where the discriminative signal occupies 3–8 dimensions and performance degrades with additional dimensions.

However, the specific author names are not displayed in these search result snippets. You can access the full paper with complete author information directly at arxiv.org/abs/2602.08159 or arxiv.org/pdf/2602.081
…[truncated 106 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_research_bib_completion_20260521T073708",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 89 · 2026-05-21T07:42:36.395245+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:WebFetch",
  "max_results": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_research_bib_completion_20260521T073708",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:WebFetch",
    "max_results": "1"
  }
}
```

</details>

---

### Tool result

_source line 90 · 2026-05-21T07:42:36.395363+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_research_bib_completion_20260521T073708",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 91 · 2026-05-21T07:42:36.395475+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://arxiv.org/abs/2602.08159",
  "prompt": "What are the full author names of this paper? Return just the author names."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_research_bib_completion_20260521T073708",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://arxiv.org/abs/2602.08159",
    "prompt": "What are the full author names of this paper? Return just the author names."
  }
}
```

</details>

---

### Tool result

_source line 92 · 2026-05-21T07:42:36.395612+00:00_

Based on the paper, the full author names are:

1. Seonglae Cho
2. Zekun Wu
3. Kleyton Da Costa
4. Adriano Koshiyama

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_research_bib_completion_20260521T073708",
  "tool": "WebFetch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 93 · 2026-05-21T07:42:36.395911+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/docs/paper/custom.bib",
  "old_string": "@inproceedings{artetxe2018vecmap,\n    title={A Robust Self-Learning Method for Fully Unsupervised Cross-Lingual Mappings of Word Embeddings},\n    author={Artetxe, Mikel and Labaka, Gorka and Agirre, Eneko},\n    booktitle={Proceedings of the 56th Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers)},\n    pages={789--798},\n    year={2018}\n}",
  "new_string": "@inproceedings{artetxe2018vecmap,\n    title={A Robust Self-Learning Method for Fully Unsupervised Cross-Lingual Mappings of Word Embeddings},\n    author={Artetxe, Mikel and Labaka, Gorka and Agirre, Eneko},\n    booktitle={Proceedings of the 56th Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers)},\n    pages={789--798},\n    year={2018}\n}\n\n% ============================================================\n% Missing citations referenced in .tex files\n% ============================================================\n\n@inproceedings{guo2017calibration,\n    title={On Calibration of Modern Neural Networks},\n    author={Guo, Chuan and Pleiss, Geoff and Sun, Yu and Weinberger, Kilian Q.},\n    booktitle={Proceedings of the 34th International Conference on Machine Learning},\n    series={PMLR},\n    volume={70},\n    pages={1321--1330},\n    year={2017},\n    url={https://proceedings.mlr.press/v70/guo17a.html}\n}\n\n@inproceedings{hewitt2019control,\n    title={Designing and Interpreting Probes with Control Tasks},\n    author={Hewitt, John and Liang, Percy},\n    booktitle={Proceedings of the 2019 Conference on Empirical Methods in Natural Language Processing and the 9th International Joint Conference on Natural Language Processing},\n    pages={2733--2743},\n    year={2019},\n    doi={10.18653/v1/D19-1275}\n}\n\n@inproceedings{kornblith2019cka,\n    title={Similarity of Neural Network Representations Revisited},\n    author={Kornblith, Simon and Norouzi, Mohammad and Lee, Honglak and Hinton, Geoffrey},\n    booktitle={Proceedings of the 36th International Conference on Machine Learning},\n    series={PMLR},\n    volume={97},\n    pages={3519--3529},\n    year={2019},\n    url={https://proceedings.mlr.press/v97/kornblith19a.html}\n}\n\n@inproceedings{pires2019multilingual,\n    title={How Multilingual is Multilingual {BERT}?},\n    author={Pires, Telmo and Schlinger, Eva and Garrette, Dan},\n    booktitle={Proceedings of the 57th Annual Meeting of the Association for Computational Linguistics},\n    pages={4996--5001},\n    year={2019},\n    doi={10.18653/v1/P19-1493}\n}\n\n@inproceedings{wu2019beto,\n    title={Beto, Bentz, Becas: The Surprising Cross-Lingual Effectiveness of {BERT}},\n    author={Wu, Shijie and Dredze, Mark},\n    booktitle={Proceedings of the 2019 Conference on Empirical Methods in Natural Language Processing and the 9th International Joint Conference on Natural Language Processing},\n    pages={833--844},\n    year={2019},\n    doi={10.18653/v1/D19-1077}\n}\n\n@inproceedings{voita2020mdl,\n    title={Information-Theoretic Probing with Minimum Description Length},\n    author={Voita, Elena and Titov, Ivan},\n    booktitle={Proceedings of the 2020 Conference on Empirical Methods in Natural Language Processing},\n    pages={183--196},\n    year={2020},\n    doi={10.18653/v1/2020.emnlp-main.14}\n}\n\n@inproceedings{karandikar2021sbece,\n    title={Soft Calibration Objectives for Neural Networks},\n    author={Karandikar, Archit and Cain, Nicholas and Tran, Dustin and Lakshminarayanan, Balaji and Shlens, Jonathon and Mozer, Michael C. and Roelofs, Becca},\n    booktitle={Advances in Neural Information Processing Systems},\n    volume={34},\n    pages={29768--29779},\n    year={2021}\n}\n\n@article{belinkov2022probing,\n    title={Probing Classifiers: Promises, Shortcomings, and Advances},\n    author={Belinkov, Yonatan},\n    journal={Computational Linguistics},\n    volume={48},\n    number={1},\n    pages={207--219},\n    year={2022},\n    publisher={MIT Press},\n    doi={10.1162/coli_a_00422}\n}\n\n@article{bendavid2010theory,\n    title={A Theory of Learning from Different Domains},\n    author={Ben-David, Shai and Blitzer, John and Crammer, Koby and Kulesza, Alex and Pereira, Fernando and Vaughan, Jennifer Wortman},\n    journal={Machine Learning},\n    volume={79},\n    number={1--2},\n    pages={151--175},\n    year={2010},\n    doi={10.1007/s10994-009-5152-4}\n}\n\n@inproceedings{zhao2019invariant,\n    title={On Learning Invariant Representations for Domain Adaptation},\n    author={Zhao, Han and des Combes, Remi Tachet and Zhang, Kun and Gordon, Geoffrey J.},\n    booktitle={Proceedings of the 36th International Conference on Machine Learning},\n    series={PMLR},\n    volume={97},\n    pages={7523--7532},\n    year={2019},\n    url={https://proceedings.mlr.press/v97/zhao19a.html}\n}\n\n@article{angelopoulos2023conformal,\n    title={Conformal Prediction: A Gentle Introduction},\n    author={Angelopoulos, Anastasios N. and Bates, Stephen},\n    journal={Foundations and Trends in Machine Learning},\n    volume={16},\n    number={4},\n    pages={494--591},\n    year={2023},\n    doi={10.1561/2200000101}\n}\n\n@inproceedings{xiao2025knowledge,\n    title={Analyzing {LLMs}' Knowledge Boundary Cognition Across Languages Through the Lens of Internal Representations},\n    author={Xiao, Chenghao and Chan, Hou Pong and Zhang, Hao and Aljunied, Mahani and Bing, Lidong and Al Moubayed, Noura and Rong, Yu},\n    booktitle={Proceedings of the 63rd Annual Meeting of the Association for Computational Linguistics},\n    year={2025},\n    doi={10.18653/v1/2025.acl-long.1174}\n}\n\n@article{zhou2025lace,\n    title={Beyond the Final Layer: Intermediate Representations for Better Multilingual Calibration in Large Language Models},\n    author={Zhou, Ej and Zhang, Caiqi and Hu, Tiancheng and Li, Chengzu and Collier, Nigel and Vuli{\\'c}, Ivan and Korhonen, Anna},\n    journal={arXiv preprint arXiv:2510.03136},\n    year={2025}\n}\n\n@article{miao2026closing,\n    title={Closing the Confidence-Faithfulness Gap in Large Language Models},\n    author={Miao, Miranda Muqing and Ungar, Lyle},\n    journal={arXiv preprint arXiv:2603.25052},\n    year={2026}\n}\n\n@inproceedings{miao2026coral,\n    title={Correctness-Optimized Residual Activation Lens ({CORAL}): Transferrable and Calibration-Aware Inference-Time Steering},\n    author={Miao, Miranda Muqing and Cho, Young-Min and Ungar, Lyle},\n    booktitle={Proceedings of the 43rd International Conference on Machine Learning},\n    year={2026},\n    url={https://arxiv.org/abs/2602.06022}\n}\n\n@inproceedings{khanmohammadi2025ccps,\n    title={Calibrating {LLM} Confidence by Probing Perturbed Representation Stability},\n    author={Khanmohammadi, Reza and Miahi, Erfan and Mardikoraem, Mehrsa and Kaur, Simerjot and Brugere, Ivan and Smiley, Charese and Thind, Kundan S. and Ghassemi, Mohammad M.},\n    booktitle={Proceedings of the 2025 Conference on Empirical Methods in Natural Language Processing},\n    pages={10448--10514},\n    year={2025},\n    doi={10.18653/v1/2025.emnlp-main.530}\n}\n\n@article{confidence_manifold2026,\n    title={The Confidence Manifold: Geometric Structure of Correctness Representations in Language Models},\n    author={Cho, Seonglae and Wu, Zekun and Da Costa, Kleyton and Koshiyama, Adriano},\n    journal={arXiv preprint arXiv:2602.08159},\n    year={2026}\n}\n\n@inproceedings{ji2025calibrating,\n    title={Calibrating Verbal Uncertainty as a Linear Feature to Reduce Hallucinations},\n    author={Ji, Ziwei and Yu, Lei and Koishekenov, Yeskendir and Bang, Yejin and Hartshorn, Anthony and Schelten, Alan and Zhang, Cheng and Fung, Pascale and Cancedda, Nicola},\n    booktitle={Proceedings of the 2025 Conference on Empirical Methods in Natural Language Processing},\n    pages={3769--3793},\n    year={2025},\n    doi={10.18653/v1/2025.emnlp-main.187}\n}\n\n@inproceedings{joshi2025calibration,\n    title={Calibration Across Layers: Understanding Calibration Evolution in {LLMs}},\n    author={Joshi, Abhinav and Ahmad, Areeb and Modi, Ashutosh},\n    booktitle={Proceedings of the 2025 Conference on Empirical Methods in Natural Language Processing},\n    year={2025},\n    doi={10.18653/v1/2025.emnlp-main.742}\n}\n\n@inproceedings{liu2025middle,\n    title={Middle-Layer Representation Alignment for Cross-Lingual Transfer in Fine-Tuned {LLMs}},\n    author={Liu, Danni and Niehues, Jan},\n    booktitle={Proceedings of the 63rd Annual Meeting of the Association for Computational Linguistics},\n    pages={15979--15996},\n    year={2025},\n    url={https://arxiv.org/abs/2502.14830}\n}\n\n@inproceedings{ravisankar2026dali,\n    title={Can You Map It to {English}? {T}he Role of Cross-Lingual Alignment in the Multilingual Performance of {LLMs}},\n    author={Ravisankar, Kartik and Han, HyoJung and Wiegreffe, Sarah and Carpuat, Marine},\n    booktitle={Proceedings of the 19th Conference of the European Chapter of the Association for Computational Linguistics},\n    pages={4854--4872},\n    year={2026},\n    url={https://arxiv.org/abs/2504.09378}\n}\n\n@article{civelli2026shared,\n    title={A Shared Geometry of Difficulty in Multilingual Language Models},\n    author={Civelli, Stefano and Bernardelle, Pietro and Brunello, Nicol{\\`o} and Demartini, Gianluca},\n    journal={arXiv preprint arXiv:2601.12731},\n    year={2026}\n}\n\n% ============================================================\n% Newly added citations\n% ============================================================\n\n@inproceedings{conneau2020xlmr,\n    title={Unsupervised Cross-lingual Representation Learning at Scale},\n    author={Conneau, Alexis and Khandelwal, Kartikay and Goyal, Naman and Chaudhary, Vishrav and Wenzek, Guillaume and Guzm{\\'a}n, Francisco and Grave, Edouard and Ott, Myle and Zettlemoyer, Luke and Stoyanov, Veselin},\n    booktitle={Proceedings of the 58th Annual Meeting of the Association for Computational Linguistics},\n    pages={8440--8451},\n    year={2020},\n    doi={10.18653/v1/2020.acl-main.747}\n}\n\n@book{lord1980irt,\n    title={Applications of Item Response Theory to Practical Testing Problems},\n    author={Lord, Frederic M.},\n    year={1980},\n    publisher={Lawrence Erlbaum Associates},\n    address={Hillsdale, NJ},\n    isbn={978-0898590067}\n}\n\n@article{fedus2022switch,\n    title={Switch Transformers: Scaling to Trillion Parameter Models with Simple and Efficient Sparsity},\n    author={Fedus, William and Zoph, Barret and Shazeer, Noam},\n    journal={Journal of Machine Learning Research},\n    volume={23},\n    number={120},\n    pages={1--39},\n    year={2022},\n    url={https://jmlr.org/papers/v23/21-0998.html}\n}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_research_bib_completion_20260521T073708",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/docs/paper/custom.bib",
    "old_string": "@inproceedings{artetxe2018vecmap,\n    title={A Robust Self-Learning Method for Fully Unsupervised Cross-Lingual Mappings of Word Embeddings},\n    author={Artetxe, Mikel and Labaka, Gorka and Agirre, Eneko},\n    booktitle={Proceedings of the 56th Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers)},\n    pages={789--798},\n    year={2018}\n}",
    "new_string": "@inproceedings{artetxe2018vecmap,\n    title={A Robust Self-Learning Method for Fully Unsupervised Cross-Lingual Mappings of Word Embeddings},\n    author={Artetxe, Mikel and Labaka, Gorka and Agirre, Eneko},\n    booktitle={Proceedings of the 56th Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers)},\n    pages={789--798},\n    year={2018}\n}\n\n% ============================================================\n% Missing citations referenced in .tex files\n% ============================================================\n\n@inproceedings{guo2017calibration,\n    title={On Calibration of Modern Neural Networks},\n    author={Guo, Chuan and Pleiss, Geoff and Sun, Yu and Weinberger, Kilian Q.},\n    booktitle={Proceedings of the 34th International Conference on Machine Learning},\n    series={PMLR},\n    volume={70},\n    pages={1321--1330},\n    year={2017},\n    url={https://proceedings.mlr.press/v70/guo17a.html}\n}\n\n@inproceedings{hewitt2019control,\n    title={Designing and Interpreting Probes with Control Tasks},\n    author={Hewitt, John and Liang, Percy},\n    booktitle={Proceedings of the 2019 Conference on Empirical Methods in Natural Language Processing and the 9th International Joint Conference on Natural Language Processing},\n    pages={2733--2743},\n    year={2019},\n    doi={10.18653/v1/D19-1275}\n}\n\n@inproceedings{kornblith2019cka,\n    title={Similarity of Neural Network Representations Revisited},\n    author={Kornblith, Simon and Norouzi, Mohammad and Lee, Honglak and Hinton, Geoffrey},\n    booktitle={Proceedings of the 36th International Conference on Machine Learning},\n    series={PMLR},\n    volume={97},\n    pages={3519--3529},\n    year={2019},\n    url={https://proceedings.mlr.press/v97/kornblith19a.html}\n}\n\n@inproceedings{pires2019multilingual,\n    title={How Multilingual is Multilingual {BERT}?},\n    author={Pires, Telmo and Schlinger, Eva and Garrette, Dan},\n    booktitle={Proceedings of the 57th Annual Meeting of the Association for Computational Linguistics},\n    pages={4996--5001},\n    year={2019},\n    doi={10.18653/v1/P19-1493}\n}\n\n@inproceedings{wu2019beto,\n    title={Beto, Bentz, Becas: The Surprising Cross-Lingual Effectiveness of {BERT}},\n    author={Wu, Shijie and Dredze, Mark},\n    booktitle={Proceedings of the 2019 Conference on Empirical Methods in Natural Language Processing and the 9th International Joint Conference on Natural Language Processing},\n    pages={833--844},\n    year={2019},\n    doi={10.18653/v1/D19-1077}\n}\n\n@inproceedings{voita2020mdl,\n    title={Information-Theoretic Probing with Minimum Description Length},\n    author={Voita, Elena and Titov, Ivan},\n    booktitle={Proceedings of the 2020 Conference on Empirical Methods in Natural Language Processing},\n    pages={183--196},\n    year={2020},\n    doi={10.18653/v1/2020.emnlp-main.14}\n}\n\n@inproceedings{karandikar2021sbece,\n    title={Soft Calibration Objectives for Neural Networks},\n    author={Karandikar, Archit and Cain, Nicholas and Tran, Dustin and Lakshminarayanan, Balaji and Shlens, Jonathon and Mozer, Michael C. and Roelofs, Becca},\n    booktitle={Advances in Neural Information Processing Systems},\n    volume={34},\n    pages={29768--29779},\n    year={2021}\n}\n\n@article{belinkov2022probing,\n    title={Probing Classifiers: Promises, Shortcomings, and Advances},\n    author={Belinkov, Yonatan},\n    journal={Computational Linguistics},\n    volume={48},\n    number={1},\n    pages={207--219},\n    year={2022},\n    publisher={MIT Press},\n    doi={10.1162/coli_a_00422}\n}\n\n@article{bendavid2010theory,\n    title={A Theory of Learning from Different Domains},\n    author={Ben-David, Shai and Blitzer, John and Crammer, Koby and Kulesza, Alex and Pereira, Fernando and Vaughan, Jennifer Wortman},\n    journal={Machine Learning},\n    volume={79},\n    number={1--2},\n    pages={151--175},\n    year={2010},\n    doi={10.1007/s10994-009-5152-4}\n}\n\n@inproceedings{zhao2019invariant,\n    title={On Learning Invariant Representations for Domain Adaptation},\n    author={Zhao, Han and des Combes, Remi Tachet and Zhang, Kun and Gordon, Geoffrey J.},\n    booktitle={Proceedings of the 36th International Conference on Machine Learning},\n    series={PMLR},\n    volume={97},\n    pages={7523--7532},\n    year={2019},\n    url={https://proceedings.mlr.press/v97/zhao19a.html}\n}\n\n@article{angelopoulos2023conformal,\n    title={Conformal Prediction: A Gentle Introduction},\n    author={Angelopoulos, Anastasios N. and Bates, Stephen},\n    journal={Foundations and Trends in Machine Learning},\n    volume={16},\n    number={4},\n    pages={494--591},\n    year={2023},\n    doi={10.1561/2200000101}\n}\n\n@inproceedings{xiao2025knowledge,\n    title={Analyzing {LLMs}' Knowledge Boundary Cognition Across Languages Through the Lens of Internal Representations},\n    author={Xiao, Chenghao and Chan, Hou Pong and Zhang, Hao and Aljunied, Mahani and Bing, Lidong and Al Moubayed, Noura and Rong, Yu},\n    booktitle={Proceedings of the 63rd Annual Meeting of the Association for Computational Linguistics},\n    year={2025},\n    doi={10.18653/v1/2025.acl-long.1174}\n}\n\n@article{zhou2025lace,\n    title={Beyond the Final Layer: Intermediate Representations for Better Multilingual Calibration in Large Language Models},\n    author={Zhou, Ej and Zhang, Caiqi and Hu, Tiancheng and Li, Chengzu and Collier, Nigel and Vuli{\\'c}, Ivan and Korhonen, Anna},\n    journal={arXiv preprint arXiv:2510.03136},\n    year={2025}\n}\n\n@article{miao2026closing,\n    title={Closing the Confidence-Faithfulness Gap in Large Language Models},\n    author={Miao, Miranda Muqing and Ungar, Lyle},\n    journal={arXiv preprint arXiv:2603.25052},\n    year={2026}\n}\n\n@inproceedings{miao2026coral,\n    title={Correctness-Optimized Residual Activation Lens ({CORAL}): Transferrable and Calibration-Aware Inference-Time Steering},\n    author={Miao, Miranda Muqing and Cho, Young-Min and Ungar, Lyle},\n    booktitle={Proceedings of the 43rd International Conference on Machine Learning},\n    year={2026},\n    url={https://arxiv.org/abs/2602.06022}\n}\n\n@inproceedings{khanmohammadi2025ccps,\n    title={Calibrating {LLM} Confidence by Probing Perturbed Representation Stability},\n    author={Khanmohammadi, Reza and Miahi, Erfan and Mardikoraem, Mehrsa and Kaur, Simerjot and Brugere, Ivan and Smiley, Charese and Thind, Kundan S. and Ghassemi, Mohammad M.},\n    booktitle={Proceedings of the 2025 Conference on Empirical Methods in Natural Language Processing},\n    pages={10448--10514},\n    year={2025},\n    doi={10.18653/v1/2025.emnlp-main.530}\n}\n\n@article{confidence_manifold2026,\n    title={The Confidence Manifold: Geometric Structure of Correctness Representations in Language Models},\n    author={Cho, Seonglae and Wu, Zekun and Da Costa, Kleyton and Koshiyama, Adriano},\n    journal={arXiv preprint arXiv:2602.08159},\n    year={2026}\n}\n\n@inproceedings{ji2025calibrating,\n    title={Calibrating Verbal Uncertainty as a Linear Feature to Reduce Hallucinations},\n    author={Ji, Ziwei and Yu, Lei and Koishekenov, Yeskendir and Bang, Yejin and Hartshorn, Anthony and Schelten, Alan and Zhang, Cheng and Fung, Pascale and Cancedda, Nicola},\n    booktitle={Proceedings of the 2025 Conference on Empirical Methods in Natural Language Processing},\n    pages={3769--3793},\n    year={2025},\n    doi={10.18653/v1/2025.emnlp-main.187}\n}\n\n@inproceedings{joshi2025calibration,\n    title={Calibration Across Layers: Understanding Calibration Evolution in {LLMs}},\n    author={Joshi, Abhinav and Ahmad, Areeb and Modi, Ashutosh},\n    booktitle={Proceedings of the 2025 Conference on Empirical Methods in Natural Language Processing},\n    year={2025},\n    doi={10.18653/v1/2025.emnlp-main.742}\n}\n\n@inproceedings{liu2025middle,\n    title={Middle-Layer Representation Alignment for Cross-Lingual Transfer in Fine-Tuned {LLMs}},\n    author={Liu, Danni and Niehues, Jan},\n    booktitle={Proceedings of the 63rd Annual Meeting of the Association for Computational Linguistics},\n    pages={15979--15996},\n    year={2025},\n    url={https://arxiv.org/abs/2502.14830}\n}\n\n@inproceedings{ravisankar2026dali,\n    title={Can You Map It to {English}? {T}he Role of Cross-Lingual Alignment in the Multilingual Performance of {LLMs}},\n    author={Ravisankar, Kartik and Han, HyoJung and Wiegreffe, Sarah and Carpuat, Marine},\n    booktitle={Proceedings of the 19th Conference of the European Chapter of the Association for Computational Linguistics},\n    pages={4854--4872},\n    year={2026},\n    url={https://arxiv.org/abs/2504.09378}\n}\n\n@article{civelli2026shared,\n    title={A Shared Geometry of Difficulty in Multilingual Language Models},\n    author={Civelli, Stefano and Bernardelle, Pietro and Brunello, Nicol{\\`o} and Demartini, Gianluca},\n    journal={arXiv preprint arXiv:2601.12731},\n    year={2026}\n}\n\n% ============================================================\n% Newly added citations\n% ============================================================\n\n@inproceedings{conneau2020xlmr,\n    title={Unsupervised Cross-lingual Representation Learning at Scale},\n    author={Conneau, Alexis and Khandelwal, Kartikay and Goyal, Naman and Chaudhary, Vishrav and Wenzek, Guillaume and Guzm{\\'a}n, Francisco and Grave, Edouard and Ott, Myle and Zettlemoyer, Luke and Stoyanov, Veselin},\n    booktitle={Proceedings of the 58th Annual Meeting of the Association for Computational Linguistics},\n    pages={8440--8451},\n    year={2020},\n    doi={10.18653/v1/2020.acl-main.747}\n}\n\n@book{lord1980irt,\n    title={Applications of Item Response Theory to Practical Testing Problems},\n    author={Lord, Frederic M.},\n    year={1980},\n    publisher={Lawrence Erlbaum Associates},\n    address={Hillsdale, NJ},\n    isbn={978-0898590067}\n}\n\n@article{fedus2022switch,\n    title={Switch Transformers: Scaling to Trillion Parameter Models with Simple and Efficient Sparsity},\n    author={Fedus, William and Zoph, Barret and Shazeer, Noam},\n    journal={Journal of Machine Learning Research},\n    volume={23},\n    number={120},\n    pages={1--39},\n    year={2022},\n    url={https://jmlr.org/papers/v23/21-0998.html}\n}"
  }
}
```

</details>

---

### Tool result

_source line 94 · 2026-05-21T07:42:36.396218+00:00_

The file /home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/docs/paper/custom.bib has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_research_bib_completion_20260521T073708",
  "tool": "Edit",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 95 · 2026-05-21T07:42:36.396378+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/docs/paper/related_work.tex",
  "old_string": "Foundational cross-lingual transfer studies on multilingual BERT established that zero-shot transfer works surprisingly well between typologically similar languages \\cite{pires2019multilingual} and across diverse NLP tasks covering 39 languages \\cite{wu2019beto}. % [TO_ADD_BIB]",
  "new_string": "Foundational cross-lingual transfer studies on multilingual BERT established that zero-shot transfer works surprisingly well between typologically similar languages \\cite{pires2019multilingual} and across diverse NLP tasks covering 39 languages \\cite{wu2019beto}, while XLM-RoBERTa \\cite{conneau2020xlmr} demonstrated that scaling unsupervised multilingual pretraining yields strong cross-lingual transfer across 100 languages."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_research_bib_completion_20260521T073708",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/docs/paper/related_work.tex",
    "old_string": "Foundational cross-lingual transfer studies on multilingual BERT established that zero-shot transfer works surprisingly well between typologically similar languages \\cite{pires2019multilingual} and across diverse NLP tasks covering 39 languages \\cite{wu2019beto}. % [TO_ADD_BIB]",
    "new_string": "Foundational cross-lingual transfer studies on multilingual BERT established that zero-shot transfer works surprisingly well between typologically similar languages \\cite{pires2019multilingual} and across diverse NLP tasks covering 39 languages \\cite{wu2019beto}, while XLM-RoBERTa \\cite{conneau2020xlmr} demonstrated that scaling unsupervised multilingual pretraining yields strong cross-lingual transfer across 100 languages."
  }
}
```

</details>

---

### Tool result

_source line 96 · 2026-05-21T07:42:36.396542+00:00_

The file /home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/docs/paper/related_work.tex has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_research_bib_completion_20260521T073708",
  "tool": "Edit",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 97 · 2026-05-21T07:42:36.396681+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/docs/paper/related_work.tex",
  "old_string": "\\citet{civelli2026shared} probe item difficulty using IRT-derived labels and report shared geometric structure across 7 languages;",
  "new_string": "\\citet{civelli2026shared} probe item difficulty using IRT-derived labels \\cite{lord1980irt} and report shared geometric structure across 7 languages;"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_research_bib_completion_20260521T073708",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/docs/paper/related_work.tex",
    "old_string": "\\citet{civelli2026shared} probe item difficulty using IRT-derived labels and report shared geometric structure across 7 languages;",
    "new_string": "\\citet{civelli2026shared} probe item difficulty using IRT-derived labels \\cite{lord1980irt} and report shared geometric structure across 7 languages;"
  }
}
```

</details>

---

### Tool result

_source line 98 · 2026-05-21T07:42:36.396848+00:00_

The file /home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/docs/paper/related_work.tex has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_research_bib_completion_20260521T073708",
  "tool": "Edit",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 99 · 2026-05-21T07:42:36.396979+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/docs/paper/method.tex",
  "offset": "17",
  "limit": "5"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_research_bib_completion_20260521T073708",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/docs/paper/method.tex",
    "offset": "17",
    "limit": "5"
  }
}
```

</details>

---

### Tool result

_source line 100 · 2026-05-21T07:42:36.397099+00:00_

17	\label{sec:framework}
18	
19	\paragraph{Models.} We evaluate Qwen3-235B-A22B (GPTQ-Int4) and Llama 4 Scout 17B-16E (W4A16) as primary architectures (P0), with Qwen2.5-7B-Instruct and Llama-3.1-8B-Instruct for validation (MVP).
20	
21	\paragraph{Languages.} We test 20 languages (English as source, plus 19 target languages) spanning three resource tiers based on GlobalMMLU availability: \textsc{high} (zh, de, es, fr, ja, ko, pt, ru), \textsc{med} (ar, id, nl, pl, tr, uk, vi), and \textsc{low} (bn, hi, sw, te).

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_research_bib_completion_20260521T073708",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 101 · 2026-05-21T07:42:36.397242+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/docs/paper/method.tex",
  "old_string": "\\paragraph{Models.} We evaluate Qwen3-235B-A22B (GPTQ-Int4) and Llama 4 Scout 17B-16E (W4A16) as primary architectures (P0), with Qwen2.5-7B-Instruct and Llama-3.1-8B-Instruct for validation (MVP).",
  "new_string": "\\paragraph{Models.} We evaluate two mixture-of-experts (MoE) architectures \\cite{fedus2022switch}: Qwen3-235B-A22B (GPTQ-Int4) and Llama 4 Scout 17B-16E (W4A16) as primary architectures (P0), with Qwen2.5-7B-Instruct and Llama-3.1-8B-Instruct as dense validation models (MVP)."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_research_bib_completion_20260521T073708",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/docs/paper/method.tex",
    "old_string": "\\paragraph{Models.} We evaluate Qwen3-235B-A22B (GPTQ-Int4) and Llama 4 Scout 17B-16E (W4A16) as primary architectures (P0), with Qwen2.5-7B-Instruct and Llama-3.1-8B-Instruct for validation (MVP).",
    "new_string": "\\paragraph{Models.} We evaluate two mixture-of-experts (MoE) architectures \\cite{fedus2022switch}: Qwen3-235B-A22B (GPTQ-Int4) and Llama 4 Scout 17B-16E (W4A16) as primary architectures (P0), with Qwen2.5-7B-Instruct and Llama-3.1-8B-Instruct as dense validation models (MVP)."
  }
}
```

</details>

---

### Tool result

_source line 102 · 2026-05-21T07:42:36.397393+00:00_

The file /home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/docs/paper/method.tex has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_research_bib_completion_20260521T073708",
  "tool": "Edit",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 103 · 2026-05-21T07:42:36.397518+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "grep -c '@' /home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/docs/paper/custom.bib | head -1",
  "description": "Count bib entries"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_research_bib_completion_20260521T073708",
  "tool": "Bash",
  "tool_args": {
    "command": "grep -c '@' /home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/docs/paper/custom.bib | head -1",
    "description": "Count bib entries"
  }
}
```

</details>

---

### Tool result

_source line 104 · 2026-05-21T07:42:36.397628+00:00_

36

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_research_bib_completion_20260521T073708",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 105 · 2026-05-21T07:42:36.397759+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "grep -oP '\\\\cite\\{[^}]+\\}' /home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/docs/paper/related_work.tex /home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/docs/paper/method.tex 2>/dev/null | grep -oP '\\{[^}]+\\}' | tr -d '{}' | tr ',' '\\n' | sort -u",
  "description": "Extract all cite keys from tex files"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_research_bib_completion_20260521T073708",
  "tool": "Bash",
  "tool_args": {
    "command": "grep -oP '\\\\cite\\{[^}]+\\}' /home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/docs/paper/related_work.tex /home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/docs/paper/method.tex 2>/dev/null | grep -oP '\\{[^}]+\\}' | tr -d '{}' | tr ',' '\\n' | sort -u",
    "description": "Extract all cite keys from tex files"
  }
}
```

</details>

---

### Tool result

_source line 106 · 2026-05-21T07:42:36.397874+00:00_

angelopoulos2023conformal
artetxe2018vecmap
confidence_manifold2026
conneau2018muse
conneau2020xlmr
fedus2022switch
guo2017calibration
khanmohammadi2025ccps
kornblith2019cka
lord1980irt
miao2026coral
niculescu2005predicting
pires2019multilingual
ravisankar2026dali
wu2019beto

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_research_bib_completion_20260521T073708",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 107 · 2026-05-21T07:42:36.398004+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "grep -oP '\\\\cite[tp]?\\{[^}]+\\}' /home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/docs/paper/related_work.tex /home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/docs/paper/method.tex 2>/dev/null | grep -oP '\\{[^}]+\\}' | tr -d '{}' | tr ',' '\\n' | sort -u",
  "description": "Extract all cite/citet/citep keys"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_research_bib_completion_20260521T073708",
  "tool": "Bash",
  "tool_args": {
    "command": "grep -oP '\\\\cite[tp]?\\{[^}]+\\}' /home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/docs/paper/related_work.tex /home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/docs/paper/method.tex 2>/dev/null | grep -oP '\\{[^}]+\\}' | tr -d '{}' | tr ',' '\\n' | sort -u",
    "description": "Extract all cite/citet/citep keys"
  }
}
```

</details>

---

### Tool result

_source line 108 · 2026-05-21T07:42:36.398123+00:00_

angelopoulos2023conformal
artetxe2018vecmap
belinkov2022probing
bendavid2010theory
civelli2026shared
confidence_manifold2026
conneau2018muse
conneau2020xlmr
fedus2022switch
guo2017calibration
hewitt2019control
ji2025calibrating
joshi2025calibration
kadavath2022language
karandikar2021sbece
khanmohammadi2025ccps
kornblith2019cka
liu2025middle
lord1980irt
miao2026closing
miao2026coral
niculescu2005predicting
pires2019multilingual
ravisankar2026dali
voita2020mdl
wu2019beto
xiao2025knowledge
zhao2019invariant
zhou2025lace

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_research_bib_completion_20260521T073708",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 109 · 2026-05-21T07:42:36.398235+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "grep -oP '@\\w+\\{([^,]+),' /home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/docs/paper/custom.bib | grep -oP '\\{[^,]+' | tr -d '{' | sort -u",
  "description": "Extract all bib keys from custom.bib"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_research_bib_completion_20260521T073708",
  "tool": "Bash",
  "tool_args": {
    "command": "grep -oP '@\\w+\\{([^,]+),' /home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/docs/paper/custom.bib | grep -oP '\\{[^,]+' | tr -d '{' | sort -u",
    "description": "Extract all bib keys from custom.bib"
  }
}
```

</details>

---

### Tool result

_source line 110 · 2026-05-21T07:42:36.398350+00:00_

APA:83
Aho:72
Ando2005
Chandra:81
Gusfield:97
andrew2007scalable
angelopoulos2023conformal
artetxe2018vecmap
belinkov2022probing
bendavid2010theory
civelli2026shared
confidence_manifold2026
conneau2018muse
conneau2020xlmr
fedus2022switch
guo2017calibration
hewitt2019control
ji2025calibrating
joshi2025calibration
kadavath2022language
karandikar2021sbece
khanmohammadi2025ccps
kornblith2019cka
liu2025middle
lord1980irt
miao2026closing
miao2026coral
niculescu2005predicting
pires2019multilingual
rasooli-tetrault-2015
ravisankar2026dali
voita2020mdl
wu2019beto
xiao2025knowledge
zhao2019invariant
zhou2025lace

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_research_bib_completion_20260521T073708",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 111 · 2026-05-21T07:42:36.398463+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "comm -23 <(grep -oP '\\\\cite[tp]?\\{[^}]+\\}' /home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/docs/paper/related_work.tex /home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/docs/paper/method.tex 2>/dev/null | grep -oP '\\{[^}]+\\}' | tr -d '{}' | tr ',' '\\n' | sort -u) <(grep -oP '@\\w+\\{([^,]+),' /home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/docs/paper/custom.bib | grep -oP '\\{[^,]+' | tr -d '{' | sort -u)",
  "description": "Find cite keys missing from bib"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_research_bib_completion_20260521T073708",
  "tool": "Bash",
  "tool_args": {
    "command": "comm -23 <(grep -oP '\\\\cite[tp]?\\{[^}]+\\}' /home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/docs/paper/related_work.tex /home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/docs/paper/method.tex 2>/dev/null | grep -oP '\\{[^}]+\\}' | tr -d '{}' | tr ',' '\\n' | sort -u) <(grep -oP '@\\w+\\{([^,]+),' /home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/docs/paper/custom.bib | grep -oP '\\{[^,]+' | tr -d '{' | sort -u)",
    "description": "Find cite keys missing from bib"
  }
}
```

</details>

---

### Tool result

_source line 112 · 2026-05-21T07:42:36.398573+00:00_

(Bash completed with no output)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_research_bib_completion_20260521T073708",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 113 · 2026-05-21T07:42:36.398717+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/docs/paper/ -name '*.tex' -exec grep -oP '\\\\cite[tp]?\\{[^}]+\\}' {} + 2>/dev/null | grep -oP '\\{[^}]+\\}' | tr -d '{}' | tr ',' '\\n' | sort -u | comm -23 - <(grep -oP '@\\w+\\{([^,]+),' /home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/docs/paper/custom.bib | grep -oP '\\{[^,]+' | tr -d '{' | sort -u)",
  "description": "Check all tex files for missing bib entries"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_research_bib_completion_20260521T073708",
  "tool": "Bash",
  "tool_args": {
    "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/docs/paper/ -name '*.tex' -exec grep -oP '\\\\cite[tp]?\\{[^}]+\\}' {} + 2>/dev/null | grep -oP '\\{[^}]+\\}' | tr -d '{}' | tr ',' '\\n' | sort -u | comm -23 - <(grep -oP '@\\w+\\{([^,]+),' /home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/docs/paper/custom.bib | grep -oP '\\{[^,]+' | tr -d '{' | sort -u)",
    "description": "Check all tex files for missing bib entries"
  }
}
```

</details>

---

### Tool result

_source line 114 · 2026-05-21T07:42:36.398840+00:00_

(Bash completed with no output)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_research_bib_completion_20260521T073708",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 115 · 2026-05-21T07:42:36.398988+00:00_

Zero missing citations across all tex files.

**Summary of changes:**

**custom.bib** — Added 25 BibTeX entries:
- 11 classic papers (guo2017calibration, hewitt2019control, kornblith2019cka, pires2019multilingual, wu2019beto, voita2020mdl, karandikar2021sbece, belinkov2022probing, bendavid2010theory, zhao2019invariant, angelopoulos2023conformal)
- 11 recent 2025-2026 papers (xiao2025knowledge, zhou2025lace, miao2026closing, miao2026coral, khanmohammadi2025ccps, confidence_manifold2026, ji2025calibrating, joshi2025calibration, liu2025middle, ravisankar2026dali, civelli2026shared) — all verified via web search, no [TO_VERIFY] needed
- 3 newly added citations (conneau2020xlmr, lord1980irt, fedus2022switch)

**related_work.tex** — 2 insertions:
- `\cite{conneau2020xlmr}` in §Cross-Lingual Probing, after Pires/Wu&Dredze
- `\cite{lord1980irt}` next to Civelli's IRT-derived labels mention

**method.tex** — 1 insertion:
- `\cite{fedus2022switch}` in §Models paragraph, noting both primary models are MoE architectures

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_paper_research_bib_completion_20260521T073708"
}
```

</details>

---
