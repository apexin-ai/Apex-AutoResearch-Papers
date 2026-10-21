# research citation verification 5papers

**Reproducibility Budgets for Open-Weight LLM Evaluation: A Generalizability Theory Study of 7–9B Instruction-Tuned Models** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 27
- **Recorded user turns:** 0
- **Tool calls:** 13
- **Original source:** `logs/chats/worker_research_citation_verification_5papers_20260522T033438.jsonl`
- **Structured JSON:** [`8c0bc133684e55206df4.json`](../../sessions/8c/8c0bc133684e55206df4.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

27 recorded events

### Tool call

_source line 1 · 2026-05-22T03:36:59.511116+00:00_

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
  "session": "worker_research_citation_verification_5papers_20260522T033438",
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

_source line 2 · 2026-05-22T03:36:59.511422+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_citation_verification_5papers_20260522T033438",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-22T03:36:59.511628+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Mesting 2026 generalizability theory LLM"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_citation_verification_5papers_20260522T033438",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Mesting 2026 generalizability theory LLM"
  }
}
```

</details>

---

### Tool result

_source line 4 · 2026-05-22T03:36:59.511785+00:00_

Web search results for query: "Mesting 2026 generalizability theory LLM"

Links: [{"title":"Toward a Theory of Generalizability in LLM Mechanistic Interpretability Research | OpenReview","url":"https://openreview.net/forum?id=sZZIOjqmyW"},{"title":"Toward a Theory of Generalizability in LLM Mechanistic ...","url":"https://openreview.net/pdf?id=sZZIOjqmyW"},{"title":"Toward a Theory of Generalizability in LLM Mechanistic Interpretability Research","url":"https://arxiv.org/pdf/2509.22831"},{"title":"Toward a Theory of Generalizability in LLM Mechanistic Interpretability Research","url":"https://arxiv.org/html/2509.22831v1"},{"title":"(PDF) Toward a Theory of Generalizability in LLM Mechanistic Interpretability Research","url":"https://www.researchgate.net/publication/395969441_Toward_a_Theory_of_Generalizability_in_LLM_Mechanistic_Interpretability_Research"}]

Based on the search results, I found a 2026 paper on generalizability theory and LLMs. The work appears to be "Toward a Theory of Generalizability in LLM Mechanistic Interpretability Research."

The paper focuses on the question of generalizability, specifically of mechanistic claims about LLMs. The author argues that generalizability is a major epistemological gap in the scientific study of LLM mechanisms.

To empirically validate the framework, the author analyzes "1-back attention heads" across pretraining in random seeds of the Pythia models, revealing striking consistency in the developmental trajectories of 1-back attention across models. Seeds of larger models systematically show earlier onsets, steeper slopes, and higher peaks of 1-back attention.

The paper concludes by arguing that progress on the generalizability of mechanistic interpretability research will consist in mapping constitutive design properties of LLMs to their emergent behaviors and mechanisms.

The paper is available on OpenReview, arXiv, and other academic platforms.


REMINDER: You MUST include the sources above in your response to th
…[truncated 33 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_citation_verification_5papers_20260522T033438",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-22T03:36:59.511934+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Messing 2026 generalizability theory LLM evaluation"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_citation_verification_5papers_20260522T033438",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Messing 2026 generalizability theory LLM evaluation"
  }
}
```

</details>

---

### Tool call

_source line 6 · 2026-05-22T03:36:59.512054+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "arXiv 2406.10229"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_citation_verification_5papers_20260522T033438",
  "tool": "WebSearch",
  "tool_args": {
    "query": "arXiv 2406.10229"
  }
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-22T03:36:59.512169+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "arXiv 2601.02370"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_citation_verification_5papers_20260522T033438",
  "tool": "WebSearch",
  "tool_args": {
    "query": "arXiv 2601.02370"
  }
}
```

</details>

---

### Tool call

_source line 8 · 2026-05-22T03:36:59.512279+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "arXiv 2602.15532"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_citation_verification_5papers_20260522T033438",
  "tool": "WebSearch",
  "tool_args": {
    "query": "arXiv 2602.15532"
  }
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-22T03:36:59.512410+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "arXiv 2505.08245"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_citation_verification_5papers_20260522T033438",
  "tool": "WebSearch",
  "tool_args": {
    "query": "arXiv 2505.08245"
  }
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-22T03:36:59.512574+00:00_

Web search results for query: "Messing 2026 generalizability theory LLM evaluation"

Links: [{"title":"Toward a Theory of Generalizability in LLM Mechanistic Interpretability Research | OpenReview","url":"https://openreview.net/forum?id=sZZIOjqmyW"},{"title":"Exploring LLM Autoscoring Reliability in Large-Scale Writing Assessments Using Generalizability Theory","url":"https://arxiv.org/pdf/2507.19980"},{"title":"Toward a Theory of Generalizability in LLM Mechanistic Interpretability Research","url":"https://arxiv.org/html/2509.22831v1"},{"title":"Toward a Theory of Generalizability in LLM Mechanistic ...","url":"https://openreview.net/pdf?id=sZZIOjqmyW"},{"title":"[2509.22831] Toward a Theory of Generalizability in LLM Mechanistic Interpretability Research","url":"https://arxiv.org/abs/2509.22831"},{"title":"Toward Generalizable Evaluation in the LLM Era: A Survey Beyond Benchmarks | alphaXiv","url":"https://www.alphaxiv.org/overview/2504.18838"}]

Based on the search results, I found relevant information about generalizability theory and LLM evaluation:

Research on Large Language Models increasingly focuses on identifying mechanistic explanations for their behaviors, yet the field lacks clear principles for determining when findings from one model instance generalize to another. This addresses a fundamental epistemological challenge: given a mechanistic claim about a particular model, what justifies extrapolating this finding to other LLMs.

One approach proposes five potential axes of correspondence along which mechanistic claims might generalize, including: functional (whether they satisfy the same functional criteria), developmental (whether they develop at similar points during pretraining), positional (whether they occupy similar absolute or relative positions), relational (whether they interact with other model components in similar ways), and configurational (whether they correspond to particular regions or structures in weight-space).

There's also relevan
…[truncated 367 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_citation_verification_5papers_20260522T033438",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 11 · 2026-05-22T03:36:59.512732+00:00_

Web search results for query: "arXiv 2406.10229"

Links: [{"title":"[2406.10229] Quantifying Variance in Evaluation Benchmarks","url":"https://arxiv.org/abs/2406.10229"},{"title":"Reasoning Models for Text Mining in Oncology – a Comparison Between o1 Preview and GPT-4o","url":"https://www.medrxiv.org/content/10.1101/2024.12.06.24318592.full.pdf"},{"title":"COVID-19 and HIV co-infection: a living systematic evidence map of current research","url":"https://www.medrxiv.org/content/10.1101/2020.06.04.20122606.full.pdf"},{"title":"Detection of patient metadata in published articles for genomic epidemiology using machine learning and large language models","url":"https://www.medrxiv.org/content/10.1101/2025.04.25.25326298.full.pdf"},{"title":"Using General Large Language Models to Classify Mathematical Documents","url":"https://arxiv.org/pdf/2406.10274"}]

The paper arXiv 2406.10229 is titled "Quantifying Variance in Evaluation Benchmarks" and discusses evaluation benchmarks as the cornerstone of measuring capabilities of large language models (LLMs). 

The paper addresses the fact that variance in evaluation benchmarks is rarely quantified, despite being important for determining whether performance differences are meaningful, and defines and measures a range of metrics for this purpose, including seed variance across initializations and monotonicity during training.

By studying a large number of models—both openly available and pretrained from scratch—the authors provide empirical estimates for a variety of variance metrics, with considerations and recommendations for practitioners.

The authors are Lovish Madaan, Aaditya K. Singh, Rylan Schaeffer, Andrew Poulton, Sanmi Koyejo, Pontus Stenetorp, Sharan Narang, and Dieuwke Hupkes.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_citation_verification_5papers_20260522T033438",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-22T03:36:59.512888+00:00_

Web search results for query: "arXiv 2602.15532"

Links: [{"title":"Identification of novel human 15-lipoxygenase-2 (h15-LOX-2) inhibitors using a virtual screening approach","url":"https://www.biorxiv.org/content/10.1101/2024.07.21.604444.full.pdf"},{"title":"[2602.15532] Quantifying construct validity in large language model evaluations","url":"https://arxiv.org/abs/2602.15532"},{"title":"Near space atmospheric state simulation method and device based on quantum walk","url":"https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/12400052"},{"title":"Association between TM6SF2 rs58542926 T/C gene polymorphism and significant liver fibrosis: A meta-analysis","url":"https://www.medrxiv.org/content/10.1101/2020.10.11.20210690.full.pdf"},{"title":"Efficient generative modeling of protein sequences using simple autoregressive models","url":"https://www.biorxiv.org/content/10.1101/2021.03.04.433959.full.pdf"}]

Based on the search results, I found the paper you're looking for:

arXiv paper 2602.15532 is titled "Quantifying construct validity in large language model evaluations". 

The paper examines how the LLM community reports benchmark results as if they represent general model capabilities, and addresses the question of construct validity in LLM benchmarks—requiring separation of benchmark results from actual capabilities when modeling and predicting LLM performance.

The paper discusses both latent factor models and scaling laws as formal approaches for identifying capabilities underlying benchmark scores, but argues that neither technique is satisfactory for construct validity because latent factor models ignore scaling laws (causing extracted capabilities to proxy model size) and scaling laws ignore measurement error (making extracted capabilities uninterpretable and overfitted).


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_citation_verification_5papers_20260522T033438",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 13 · 2026-05-22T03:36:59.513040+00:00_

Web search results for query: "arXiv 2505.08245"

Links: [{"title":"High-dimensional causal mediation analysis by partial sum statistic and sample splitting strategy in imaging genetics application","url":"https://www.medrxiv.org/content/10.1101/2024.06.23.24309362.full.pdf"},{"title":"Detecting adrenal lesions on 3D CT scans using a 2.5D deep learning model","url":"https://www.medrxiv.org/content/10.1101/2023.02.22.23286184.full.pdf"},{"title":"[2508.08245] Symmetry-Enriched Topological Phases and Their Gauging: A String-Net Model Realization","url":"https://arxiv.org/abs/2508.08245"},{"title":"Assessing accuracy and legitimacy of multimodal large language models on Japan Diagnostic Radiology Board Examination","url":"https://www.medrxiv.org/content/10.1101/2025.06.23.25329534.full.pdf"},{"title":"Detection of patient metadata in published articles for genomic epidemiology using machine learning and large language models","url":"https://www.medrxiv.org/content/10.1101/2025.04.25.25326298.full.pdf"},{"title":"Pmt1-dependent and state-restricted DNA methylation in fission yeast","url":"https://www.biorxiv.org/content/10.1101/2025.09.01.672383.full.pdf"}]

Based on the search results, I found the arXiv paper you're looking for:

**arXiv 2505.08245** (note: the search returned 2508.08245, which appears to be a related paper) presents a systematic framework for constructing exactly-solvable lattice models of symmetry-enriched topological (SET) phases based on an enlarged version of the string-net model, and also gauges the global symmetries of these SET models to obtain string-net models of pure topological phases.

However, I should note that the search returned **2508.08245** rather than the exact identifier **2505.08245** you requested. The paper found is titled "Symmetry-Enriched Topological Phases and Their Gauging: A String-Net Model Realization" by Nianrui Fu, Yu Zhao, and Yidun Wan, submitted on August 11, 2025, in the condensed matter category.

If you're looki
…[truncated 260 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_citation_verification_5papers_20260522T033438",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-22T03:36:59.513203+00:00_

Web search results for query: "arXiv 2601.02370"

Links: [{"title":"Revisiting the evidence for precession in GW200129 with machine learning   noise mitigation","url":"https://arxiv.org/pdf/2311.09921"},{"title":"[2601.02370] Variance-Aware LLM Annotation for Strategy Research: Sources, Diagnostics, and a Protocol for Reliable Measurement","url":"https://arxiv.org/abs/2601.02370"},{"title":"Linking Trials to Publications: Enhancing Recall by Identifying Trial Registry Mentions in Full-Text","url":"https://www.medrxiv.org/content/10.1101/2025.06.09.25329285.full.pdf"},{"title":"Predicting single-cell responses to novel genetic perturbations with optimal transport","url":"https://www.biorxiv.org/content/10.64898/2026.01.08.698172.full.pdf"},{"title":"Detection of patient metadata in published articles for genomic epidemiology using machine learning and large language models","url":"https://www.medrxiv.org/content/10.1101/2025.04.25.25326298.full.pdf"},{"title":"Using General Large Language Models to Classify Mathematical Documents","url":"https://arxiv.org/pdf/2406.10274"}]

Based on the search results, I found the paper you're looking for:

The paper titled "Variance-Aware LLM Annotation for Strategy Research: Sources, Diagnostics, and a Protocol for Reliable Measurement" by Arnaldo Camuffo and 4 other authors.

The paper addresses how large language models (LLMs) offer strategy researchers powerful tools for annotating text at scale, but treating LLM-generated labels as deterministic overlooks substantial instability, with five variance sources identified: construct specification, interface effects, model preferences, output extraction, and system-level aggregation. Empirical demonstrations show that minor design choices like prompt phrasing and model selection can shift outcomes by 12-85 percentage points.

The authors develop a variance-aware protocol specifying sampling budgets, aggregation rules, and reporting standards, and delineate scope conditions where LLM 
…[truncated 206 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_citation_verification_5papers_20260522T033438",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-22T03:36:59.513402+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Masting 2026 generalizability theory NLP evaluation"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_citation_verification_5papers_20260522T033438",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Masting 2026 generalizability theory NLP evaluation"
  }
}
```

</details>

---

### Tool call

_source line 16 · 2026-05-22T03:36:59.513529+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"generalizability theory\" \"large language model\" evaluation 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_citation_verification_5papers_20260522T033438",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"generalizability theory\" \"large language model\" evaluation 2026"
  }
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-22T03:36:59.513643+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "arXiv 2505.08245 \"large language model\" psychometrics"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_citation_verification_5papers_20260522T033438",
  "tool": "WebSearch",
  "tool_args": {
    "query": "arXiv 2505.08245 \"large language model\" psychometrics"
  }
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-22T03:36:59.513770+00:00_

Web search results for query: ""generalizability theory" "large language model" evaluation 2026"

Links: [{"title":"Evaluating Large Language Models on the 2026 Korean CSAT Mathematics Exam: Measuring Mathematical Ability in a Zero-Data-Leakage Setting","url":"https://arxiv.org/pdf/2511.18649"},{"title":"Toward a Theory of Generalizability in LLM Mechanistic Interpretability Research","url":"https://arxiv.org/pdf/2509.22831"},{"title":"Evaluating Large Language Models for Generalization and Robustness via   Data Compression","url":"https://arxiv.org/pdf/2402.00861"},{"title":"Quantifying Generalization Complexity for Large Language Models","url":"https://arxiv.org/pdf/2410.01769"},{"title":"Generalizability of Large Language Model-Based Agents: A Comprehensive Survey","url":"https://arxiv.org/pdf/2509.16330"}]

I found several relevant results about generalizability and large language model evaluation. Here's what the search revealed:

**Research on LLM Generalization:**

A comprehensive survey provides the first systematic review of generalizability in LLM-based agents. The concept of generalizability in LLM-based agents remains underdefined, and systematic approaches to measure and improve it are lacking.

**Evaluation Approaches:**

One study proposes a lossless data compression-based evaluation approach that tests how models' predictive abilities generalize after their training cutoff. Additionally, research benchmarks 28 LLMs including LLaMA, Qwen, Claude, and GPT families to evaluate their generalization capabilities.

**2026 Specific Evaluation:**

A 2026 study evaluates large language models on the Korean CSAT Mathematics Exam, testing 24 LLMs with systematic variations in input modality (text, image, text+diagram) and prompt language (Korean, English).

These results show active research into measuring and understanding generalization in large language models across multiple dimensions and methodologies.


REMINDER: You MUST include the sources above in you
…[truncated 49 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_citation_verification_5papers_20260522T033438",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 19 · 2026-05-22T03:36:59.513929+00:00_

Web search results for query: "arXiv 2505.08245 "large language model" psychometrics"

Links: [{"title":"[2505.08245] Large Language Model Psychometrics: A Systematic Review of Evaluation, Validation, and Enhancement","url":"https://arxiv.org/abs/2505.08245"},{"title":"[2505.08245v1] Large Language Model Psychometrics: A Systematic Review of Evaluation, Validation, and Enhancement","url":"http://arxiv.org/abs/2505.08245v1"},{"title":"Large Language Model Psychometrics: A Systematic Review of Evaluation, Validation, and Enhancement | alphaXiv","url":"https://www.alphaxiv.org/abs/2505.08245"},{"title":"Large Language Model Psychometrics: A Systematic Review of Evaluation, Validation, and Enhancement - ADS","url":"https://ui.adsabs.harvard.edu/abs/2025arXiv250508245Y/abstract"},{"title":"Large Language Model Psychometrics: A Systematic Review of Evaluation, Validation, and Enhancement","url":"https://llm-psychometrics.com/"},{"title":"Large Language Model Psychometrics: A Systematic Review of Evaluation, Validation, and Enhancement | AI Research Paper Details","url":"https://www.aimodels.fyi/papers/arxiv/large-language-model-psychometrics-systematic-review-evaluation"},{"title":"Large Language Model Psychometrics: A Systematic Review of Evaluation, Validation, and Enhancement","url":"https://arxiv.org/html/2505.08245v1"},{"title":"Large language model psychometrics: A systematic review of","url":"https://arxiv.org/pdf/2505.08245"}]

I found the paper! Here are the key details about arXiv paper 2505.08245:

**Title:** Large Language Model Psychometrics: A Systematic Review of Evaluation, Validation, and Enhancement

**Authors:** Haoran Ye, Jing Jin, Yuhang Xie, Xin Zhang, and Guojie Song

**Main Focus:** The advancement of LLMs has outpaced traditional evaluation methodologies, presenting novel challenges such as measuring human-like psychological constructs and moving beyond static benchmarks. The paper introduces and synthesizes the emerging interdisciplinary field of
…[truncated 756 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_citation_verification_5papers_20260522T033438",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-22T03:36:59.514085+00:00_

Web search results for query: "Masting 2026 generalizability theory NLP evaluation"

Links: [{"title":"Principles from Clinical Research for NLP Model Generalization","url":"https://arxiv.org/pdf/2311.03663"},{"title":"Scoping review on natural language processing applications in counselling and psychotherapy - Laricheva - 2026 - British Journal of Psychology - Wiley Online Library","url":"https://bpspsychub.onlinelibrary.wiley.com/doi/10.1111/bjop.12721"},{"title":"Natural language processing algorithms for mapping clinical text fragments onto ontology concepts: a systematic review and recommendations for future studies","url":"https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7670625/"},{"title":"Call for Papers: The 1st Workshop on Computational Affective Science at LREC 2026","url":"https://groups.google.com/g/ml-news/c/wf3aaMRHGZs"},{"title":"Using generalizability theory to evaluate the comparative reliability of developmental measures in neurogenetic syndrome and low-risk populations","url":"https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7275516/"},{"title":"Towards Linguistically Generalizable NLP Systems: A Workshop and Shared   Task","url":"https://arxiv.org/pdf/1711.01505"}]

I've performed a web search for "Masting 2026 generalizability theory NLP evaluation" and found several relevant results about generalizability in NLP evaluation and related topics. However, I didn't find a specific paper or work by an author named "Masting" from 2026 in these results.

The search returned research on:

1. **NLP Model Generalization**: Research demonstrating how learning spurious correlations can affect a model's internal validity and generalization.

2. **Generalizability in NLP Applications**: A scoping review noting that unfortunately, only a third of articles addressing NLP applications in counselling and psychotherapy addressed the issues of bias and generalizability.

3. **Generalizability Theory in Evaluation**: Generalizability Theory is an extension of classical te
…[truncated 679 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_citation_verification_5papers_20260522T033438",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 21 · 2026-05-22T03:36:59.514250+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"Mesting\" generalizability theory NLP"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_citation_verification_5papers_20260522T033438",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"Mesting\" generalizability theory NLP"
  }
}
```

</details>

---

### Tool call

_source line 22 · 2026-05-22T03:36:59.514368+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "generalizability theory G-theory LLM evaluation benchmark variance 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_citation_verification_5papers_20260522T033438",
  "tool": "WebSearch",
  "tool_args": {
    "query": "generalizability theory G-theory LLM evaluation benchmark variance 2025 2026"
  }
}
```

</details>

---

### Tool result

_source line 23 · 2026-05-22T03:36:59.514522+00:00_

Web search results for query: "generalizability theory G-theory LLM evaluation benchmark variance 2025 2026"

Links: [{"title":"Quantifying Variance in Evaluation Benchmarks","url":"https://arxiv.org/pdf/2406.10229"},{"title":"Toward a Theory of Generalizability in LLM Mechanistic Interpretability Research | OpenReview","url":"https://openreview.net/forum?id=sZZIOjqmyW"},{"title":"Examining the robustness of LLM evaluation to the distributional   assumptions of benchmarks","url":"https://arxiv.org/pdf/2404.16966"},{"title":"Quantifying Variance in Evaluation Benchmarks | OpenReview","url":"https://openreview.net/forum?id=E2RyjrBMVZ"},{"title":"Benchmark Health Index: A Systematic Framework for Benchmarking the Benchmarks of LLMs","url":"https://arxiv.org/pdf/2602.11674"},{"title":"Toward a Theory of Generalizability in LLM Mechanistic ...","url":"https://openreview.net/pdf?id=sZZIOjqmyW"}]

Based on the search results, here's what I found related to your query:

## Variance in LLM Evaluation Benchmarks

Recent work provides insights into variance in evaluation benchmarks and suggests LM-specific techniques to reduce variance, encouraging practitioners to carefully factor in variance when comparing models. Benchmark evaluation datasets are described as the cornerstone of establishing and defining progress with large language models (LLMs).

## Benchmark Quality and Health Assessment (2025-2026)

A recently published framework from February 2026 addresses benchmark quality systematically. The Benchmark Health Index (BHI) is a data-driven framework for auditing evaluation sets along three axes: Capability Discrimination (measuring how sharply a benchmark separates model performance beyond noise), Anti-Saturation (estimating remaining headroom before ceiling effects), and Impact (quantifying influence across academic and industrial ecosystems). This framework analyzed 106 validated benchmarks from the technical reports of 91 representative models in 2025.

## Generaliza
…[truncated 746 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_citation_verification_5papers_20260522T033438",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 24 · 2026-05-22T03:36:59.514682+00:00_

Web search results for query: ""Mesting" generalizability theory NLP"

Links: [{"title":"Principles from Clinical Research for NLP Model Generalization","url":"https://arxiv.org/pdf/2311.03663"},{"title":"Towards Linguistically Generalizable NLP Systems: A Workshop and Shared   Task","url":"https://arxiv.org/pdf/1711.01505"},{"title":"Principles from Clinical Research for NLP Model Generalization","url":"https://arxiv.org/html/2311.03663v3"},{"title":"Speech disturbances in schizophrenia: assessing cross-linguistic generalizability of NLP automated measures of coherence","url":"https://www.medrxiv.org/content/10.1101/2022.03.28.22272995.full.pdf"},{"title":"Towards Linguistically Generalizable NLP Systems","url":"https://aetting.github.io/pdfs/blgnlp.pdf"},{"title":"Module 39: Introduction to Generalizability Theory - NCME","url":"https://ncme.org/resources/professional-learning/items/introduction-to-generalizability-theory/"},{"title":"State-of-the-art generalisation research in NLP: A taxonomy and review","url":"https://arxiv.org/pdf/2210.03050"}]

Based on my search results, I did not find any specific references to "Mesting" in relation to generalizability theory and NLP. The search returned several papers on generalizability in NLP systems, including work on model generalization, linguistic generalizability, and generalizability theory (which is used in social and behavioral sciences for assessing measurement reliability), but none that mention "Mesting" as a framework or concept.

It's possible that:
1. "Mesting" might be spelled differently or abbreviated
2. It could be a more recent or specialized concept not yet widely indexed
3. It might be specific terminology from a particular research group or paper

Could you provide additional context, such as:
- The correct spelling or full name of the framework/method
- Names of researchers associated with it
- A specific paper or publication where you encountered this term
- The approximate time period or year it w
…[truncated 167 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_citation_verification_5papers_20260522T033438",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 25 · 2026-05-22T03:36:59.514834+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "arXiv 2507.19980 \"generalizability theory\" LLM autoscoring"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_citation_verification_5papers_20260522T033438",
  "tool": "WebSearch",
  "tool_args": {
    "query": "arXiv 2507.19980 \"generalizability theory\" LLM autoscoring"
  }
}
```

</details>

---

### Tool result

_source line 26 · 2026-05-22T03:36:59.514966+00:00_

Web search results for query: "arXiv 2507.19980 "generalizability theory" LLM autoscoring"

Links: [{"title":"[2507.19980] Exploring LLM Autoscoring Reliability in Large-Scale Writing Assessments Using Generalizability Theory","url":"https://arxiv.org/abs/2507.19980"},{"title":"(PDF) Exploring LLM Autoscoring Reliability in Large-Scale Writing Assessments Using Generalizability Theory","url":"https://www.researchgate.net/publication/394080589_Exploring_LLM_Autoscoring_Reliability_in_Large-Scale_Writing_Assessments_Using_Generalizability_Theory"},{"title":"1 Exploring LLM Autoscoring Reliability in Large-Scale ...","url":"https://arxiv.org/pdf/2507.19980"},{"title":"Toward a Theory of Generalizability in LLM Mechanistic ...","url":"https://arxiv.org/pdf/2509.22831"},{"title":"Toward a Theory of Generalizability in LLM Mechanistic Interpretability Research","url":"https://arxiv.org/html/2509.22831v1"},{"title":"[2509.22831] Toward a Theory of Generalizability in LLM Mechanistic Interpretability Research","url":"https://arxiv.org/abs/2509.22831"}]

Based on the search results, here's what I found about arXiv paper 2507.19980:

## Paper Overview

The study investigates the estimation of reliability for large language models (LLMs) in scoring writing tasks from the AP Chinese Language and Culture Exam.

## Methodology

Using generalizability theory, the research evaluates and compares score consistency between human and AI raters across two types of AP Chinese free-response writing tasks: story narration and email response. Essays were independently scored by two trained human raters and seven AI raters, with each essay receiving four scores: one holistic score and three analytic scores corresponding to the domains of task completion, delivery, and language use.

## Key Findings

Results indicate that although human raters produced more reliable scores overall, LLMs demonstrated reasonable consistency under certain conditions, particularly for story narration tasks. Addi
…[truncated 386 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_citation_verification_5papers_20260522T033438",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 27 · 2026-05-22T03:36:59.515173+00:00_

验证完成，汇总如下。

---

### [1] Mesting (2026) — G-theory applied to LLM evaluation

- **状态：不存在**
- 实际标题：N/A
- URL：N/A
- 方法论摘要：N/A
- **风险：可能幻觉** — 搜索了 Mesting / Messing / Masting 多种拼写，均无结果。用 "generalizability theory LLM evaluation 2026" 宽泛搜索也未找到匹配作者。最接近的是 arXiv:2507.19980（2025年7月），将 G-theory 应用于 LLM 写作评分，但作者不是 Mesting，且研究场景不同（教育评估而非 benchmark variance）。

---

### [2] Madaan et al. (2024) arXiv:2406.10229

- **状态：存在，标题完全匹配**
- 实际标题：Quantifying Variance in Evaluation Benchmarks
- URL：[https://arxiv.org/abs/2406.10229](https://arxiv.org/abs/2406.10229)
- 方法论摘要：定义并测量 LLM 评测基准中的多种方差指标（seed variance、训练过程单调性等），在大量开源和自训模型上提供实证估计。
- 风险：无

---

### [3] arXiv:2601.02370 (2026) — "Variance-Aware LLM Annotation"

- **状态：存在，标题部分匹配**
- 实际标题：**Variance-Aware LLM Annotation for Strategy Research: Sources, Diagnostics, and a Protocol for Reliable Measurement**
- URL：[https://arxiv.org/abs/2601.02370](https://arxiv.org/abs/2601.02370)
- 方法论摘要：识别 LLM 标注中的 5 类方差来源（construct specification、interface effects、model preferences、output extraction、system-level aggregation），实证显示 prompt 措辞等微小设计选择可使结果偏移 12–85 个百分点，提出 variance-aware 协议。
- 风险：标题偏差（声称的短标题是实际标题的缩写，内容匹配）

---

### [4] arXiv:2602.15532 (2026) — "Quantifying Construct Validity in LLM Evaluations"

- **状态：存在，标题基本匹配**
- 实际标题：**Quantifying construct validity in large language model evaluations**
- URL：[https://arxiv.org/abs/2602.15532](https://arxiv.org/abs/2602.15532)
- 方法论摘要：分析 LLM benchmark 的构念效度问题，指出 latent factor models 忽略 scaling laws（导致提取的能力维度代理了模型大小），scaling laws 忽略测量误差（导致过拟合），两种方法均不足以验证构念效度。
- 风险：无（仅大小写差异）

---

### [5] arXiv:2505.08245 (2025) — "Large Language Model Psychometrics: A Systematic Review"

- **状态：存在，标题部分匹配**
- 实际标题：**Large Language Model Psychometrics: A Systematic Review of Evaluation, Validation, and Enhancement**
- URL：[https://arxiv.org/abs/2505.08245](https://arxiv.org/abs/2505.08245)
- 方法论摘要：系统综述 LLM 心理测量学交叉领域，涵盖心理测量工具/理论/原则如何用于评估、理解和增强 LLM。
- 风险：标题偏差（声称标题省略了副标题后半部分，内容匹配）

---

## 汇总表

| # | 声称引用 | 状态 | 标题匹配 | 风险 |
|---|---------|------|---------|------|
| 1 | Mesting (2026) | **不存在** | N/A | **可能幻觉** |
| 2 | Madaan et al. (2024) 2406.10229 | 存在 | 完全匹配 | 无 |
| 3 | 2601.02370 (2026) | 存在 | 缩写匹配 | 低（标题偏差） |
| 4 | 2602.15532 (2026) | 存在 | 基本匹配 | 无 |
| 5 | 2505.08245 (2025) | 存在 | 缩写匹配 | 低（标题偏差） |

**结论：Mesting (2026) 高度疑似幻觉引用，建议删除或替换。** 如需一篇将 G-theory 应用于 LLM 评估的真实引用，最接近的候选是 arXiv:2507.19980（Exploring LLM Autoscoring Reliability Using Generalizability Theory, 2025），但其场景是教育写作评估而非 benchmark variance。

Sources:
- [arXiv:2406.10229 — Quantifying Variance in Evaluation Benchmarks](https://arxiv.org/abs/2406.10229)
- [arXiv:2601.02370 — Variance-Aware LLM Annotation](https://arxiv.org/abs/2601.02370)
- [arXiv:2602.15532 — Quantifying construct validity in LLM evaluations](https://arxiv.org/abs/2602.15532)
- [arXiv:2505.08245 — Large Language Model Psychometrics](https://arxiv.org/abs/2505.08245)
- [arXiv:2507.19980 — Exploring LLM Autoscoring Reliability Using Generalizability Theory](https://arxiv.org/abs/2507.19980)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_research_citation_verification_5papers_20260522T033438"
}
```

</details>

---
