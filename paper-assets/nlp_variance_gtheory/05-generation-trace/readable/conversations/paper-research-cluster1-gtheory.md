# paper research cluster1 gtheory

**Reproducibility Budgets for Open-Weight LLM Evaluation: A Generalizability Theory Study of 7–9B Instruction-Tuned Models** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 57
- **Recorded user turns:** 0
- **Tool calls:** 28
- **Original source:** `logs/chats/worker_paper_research_cluster1_gtheory_20260521T180157.jsonl`
- **Structured JSON:** [`aee8353436bd8ed779f9.json`](../../sessions/ae/aee8353436bd8ed779f9.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

57 recorded events

### Tool call

_source line 1 · 2026-05-21T18:06:23.654253+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/literature_map.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_research_cluster1_gtheory_20260521T180157",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/literature_map.yaml"
  }
}
```

</details>

---

### Tool result

_source line 2 · 2026-05-21T18:06:23.654707+00:00_

1	meta:
2	  last_updated: "2026-05-20T14:00:00Z"
3	  total_papers: 10
4	
5	categories:
6	  - key: "gtheory_evaluation"
7	    name: "G-Theory & Evaluation Variance"
8	    narrative: "Applying Generalizability Theory and variance decomposition to LLM evaluation reliability"
9	  - key: "infrastructure_variance"
10	    name: "Infrastructure-Induced Variance"
11	    narrative: "Hardware, precision, and CUDA-level nondeterminism as variance sources in LLM inference"
12	  - key: "prompt_sensitivity"
13	    name: "Prompt Sensitivity & Methodological Variance"
14	    narrative: "Prompt phrasing, seed, temperature, and ordering as variance sources"
15	  - key: "evaluation_methodology"
16	    name: "Evaluation Methodology"
17	    narrative: "Scoring artifacts, benchmark design, and evaluation protocol considerations"
18	
19	papers:
20	  mesting2026hidden:
21	    title: "Hidden Measurement Error in LLM Pipelines Distorts Annotation, Evaluation, and Benchmarking"
22	    authors:
23	      - "Mesting, F."
24	    year: 2026
25	    venue: "arXiv"
26	    url: "https://arxiv.org/abs/2604.11581"
27	    category: "gtheory_evaluation"
28	    role: "direct-competitor"
29	    relevance: "Closest methodological precedent: G-theory decomposition of 5 facets (item, prompt, temperature, judge model, replication) on AILuminate/MMLU/Chatbot Arena. Found judge model=43.8%, prompt×judge=12.4%. Critically excludes infrastructure factors — our work extends this by crossing infrastructure with methodology."
30	    verified: false
31	    added_by: "director"
32	    added_at: "2026-05-20T14:00:00Z"
33	
34	  brittlebench2026:
35	    title: "Brittlebench: Quantifying LLM Robustness via Prompt Sensitivity"
36	    authors: []
37	    year: 2026
38	    venue: "arXiv"
39	    url: "https://arxiv.org/abs/2603.13285"
40	    category: "prompt_sensitivity"
41	    role: "direct-competitor"
42	    relevance: "Up to 50% performance variance from prompt perturbations, 63% of cases show ranking reversals from single pe
…[truncated 5240 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_research_cluster1_gtheory_20260521T180157",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-21T18:06:23.654920+00:00_

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
  "session": "worker_paper_research_cluster1_gtheory_20260521T180157",
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

_source line 4 · 2026-05-21T18:06:23.655057+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_research_cluster1_gtheory_20260521T180157",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-21T18:06:23.655202+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Mesting 2026 \"Hidden Measurement Error in LLM Pipelines\" arXiv 2604.11581"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_research_cluster1_gtheory_20260521T180157",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Mesting 2026 \"Hidden Measurement Error in LLM Pipelines\" arXiv 2604.11581"
  }
}
```

</details>

---

### Tool call

_source line 6 · 2026-05-21T18:06:23.655323+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "GeneralizIT Python generalizability theory computations arXiv 2411.17880"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_research_cluster1_gtheory_20260521T180157",
  "tool": "WebSearch",
  "tool_args": {
    "query": "GeneralizIT Python generalizability theory computations arXiv 2411.17880"
  }
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-21T18:06:23.655480+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Kunievsky Evans 2025 \"Measuring Intent Comprehension in LLMs\" variance decomposition arXiv 2506.16584"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_research_cluster1_gtheory_20260521T180157",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Kunievsky Evans 2025 \"Measuring Intent Comprehension in LLMs\" variance decomposition arXiv 2506.16584"
  }
}
```

</details>

---

### Tool call

_source line 8 · 2026-05-21T18:06:23.655608+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Bouthillier 2021 \"Accounting for Variance in Machine Learning Benchmarks\" JMLR"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_research_cluster1_gtheory_20260521T180157",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Bouthillier 2021 \"Accounting for Variance in Machine Learning Benchmarks\" JMLR"
  }
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-21T18:06:23.655730+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Shavelson Webb 1991 \"Generalizability Theory: A Primer\" textbook publisher ISBN"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_research_cluster1_gtheory_20260521T180157",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Shavelson Webb 1991 \"Generalizability Theory: A Primer\" textbook publisher ISBN"
  }
}
```

</details>

---

### Tool call

_source line 10 · 2026-05-21T18:06:23.655844+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Brennan 2001 \"Generalizability Theory\" textbook Springer publisher ISBN"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_research_cluster1_gtheory_20260521T180157",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Brennan 2001 \"Generalizability Theory\" textbook Springer publisher ISBN"
  }
}
```

</details>

---

### Tool result

_source line 11 · 2026-05-21T18:06:23.655976+00:00_

Web search results for query: "GeneralizIT Python generalizability theory computations arXiv 2411.17880"

Links: [{"title":"[2411.17880] GeneralizIT: A Python Solution for Generalizability Theory Computations","url":"https://arxiv.org/abs/2411.17880"},{"title":"GeneralizIT: A Python Solution for Generalizability Theory Computations","url":"https://arxiv.org/pdf/2411.17880"},{"title":"GeneralizIT: A Python Solution for Generalizability Theory Computations - ScienceDirect","url":"https://www.sciencedirect.com/science/article/pii/S235271102500202X"},{"title":"GeneralizIT: A Python Solution for Generalizability Theory Computations Citation:","url":"https://arxiv.org/html/2411.17880v1"},{"title":"GitHub - tylerjsmith111/GeneralizIT: GeneralizIT python package for calculating generalizability and dependability coefficients","url":"https://github.com/tylerjsmith111/GeneralizIT"}]

Based on the search results, here's what I found about the arXiv paper 2411.17880:

GeneralizIT is a Python package designed to streamline the application of Generalizability Theory (G-Theory) in research and practice. G-Theory extends classical test theory by estimating multiple sources of error variance, providing a more flexible and detailed approach to reliability assessment.

GeneralizIT addresses the challenge of G-Theory's complexity by offering an intuitive, user-friendly mechanism to calculate variance components, generalizability coefficients E*rho^2 and dependability Phi and to perform decision (D) studies. D-Studies allow users to make decisions about potential study designs and target improvements in the reliability of certain facets. The package supports both fully crossed and nested designs, enabling users to perform in-depth reliability analysis with minimal coding effort.

The paper was authored by Tyler J. Smith, Theresa Kline, and Adrienne Kline, and was submitted on November 26, 2024 with a revision on December 6, 2024. GeneralizIT includes built-in visualization tools and det
…[truncated 239 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_research_cluster1_gtheory_20260521T180157",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-21T18:06:23.656128+00:00_

Web search results for query: "Mesting 2026 "Hidden Measurement Error in LLM Pipelines" arXiv 2604.11581"

Links: [{"title":"[2604.11581] Hidden Measurement Error in LLM Pipelines Distorts Annotation, Evaluation, and Benchmarking","url":"https://arxiv.org/abs/2604.11581"},{"title":"Hidden Measurement Error in LLM Pipelines Distorts Annotation, Evaluation, and Benchmarking","url":"https://arxiv.org/html/2604.11581v4"},{"title":"Hidden Measurement Error in LLM Pipelines Distorts Annotation,","url":"https://arxiv.org/pdf/2604.11581"},{"title":"To Err Is Human; To Annotate, SILICON? Reducing Measurement Error in LLM Annotation","url":"https://arxiv.org/pdf/2412.14461"},{"title":"From Stochasticity to Signal: A Bayesian Latent State Model for Reliable Measurement with LLMs","url":"https://arxiv.org/pdf/2510.23874"},{"title":"Do LLMs Know about Hallucination? An Empirical Investigation of LLM's   Hidden States","url":"https://arxiv.org/pdf/2402.09733"}]

I found the paper you're looking for! Here's what I found:

The paper "Hidden Measurement Error in LLM Pipelines Distorts Annotation, Evaluation, and Benchmarking" by Solomon Messing is arXiv:2604.11581, submitted on April 13, 2026, with the latest version (v4) revised on April 29, 2026.

**Key findings:**

The paper highlights that standard confidence intervals ignore variability from prompt phrasing, model temperature, and judge model choice, producing under-coverage that worsens with more data. The omitted variance can shift results enough to reverse conclusions and opens benchmarks to exploitation.

The paper decomposes LLM pipeline uncertainty into its sources, distinguishes variance that shrinks with more data from sensitivity to researcher design choices, and uses design-study projections to reduce total evaluation error (TEE).

Across the demonstrations, naive standard errors are 40-60% smaller than the TEE-corrected standard error. Using Chatbot Arena data, naive 95% confidence interval coverage drops as the numb
…[truncated 231 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_research_cluster1_gtheory_20260521T180157",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 13 · 2026-05-21T18:06:23.656288+00:00_

Web search results for query: "Shavelson Webb 1991 "Generalizability Theory: A Primer" textbook publisher ISBN"

Links: [{"title":"Generalizability Theory: A Primer by Shavelson, Richard J.; Webb, Noreen M. 9780803937451| eBay","url":"https://www.ebay.com/itm/146560018512"},{"title":"Generalizability Theory: A Primer (Measurement Methods for the Social Science) - Shavelson, Richard J.; Webb, Noreen M.: 9780803937444 - AbeBooks","url":"https://www.abebooks.com/9780803937444/Generalizability-Theory-Primer-Measurement-Methods-080393744X/plp"},{"title":"(PDF) Generalizability Theory: A Primer","url":"https://www.researchgate.net/publication/235726254_Generalizability_Theory_A_Primer"},{"title":"Generalizability Theory: A Primer","url":"https://us.sagepub.com/en-us/nam/generalizability-theory/book3375"},{"title":"Generalizability Theory A Primer","url":"https://uk.sagepub.com/en-gb/eur/generalizability-theory/book3375"},{"title":"Generalizability Theory: Overview - Webb - Major Reference Works - Wiley Online Library","url":"https://onlinelibrary.wiley.com/doi/abs/10.1002/9781118445112.stat06729"},{"title":"Generalizability Theory: A Primer - Richard J. Shavelson, Noreen M. Webb - Google Books","url":"https://books.google.com/books/about/Generalizability_Theory.html?id=gzyKRZWrm9EC"},{"title":"Amazon.com: Generalizability Theory: A Primer (Measurement Methods for the Social Science): 9780803937444: Shavelson, Richard J., Webb, Noreen M.: Books","url":"https://www.amazon.com/Generalizability-Theory-Measurement-Methods-Science/dp/080393744X"},{"title":"Amazon.com: Generalizability Theory: A Primer (Measurement Methods for the Social Science): 9780803937451: Shavelson, Richard J., Webb, Noreen M.: Books","url":"https://www.amazon.com/SHAVELSON-GENERALIZABILITY-Measurement-Methods-Science/dp/0803937458"}]

Based on the search results, here is the information for the Shavelson and Webb 1991 textbook:

**Title:** Generalizability Theory: A Primer

**Authors:** Richard J. Shavel
…[truncated 409 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_research_cluster1_gtheory_20260521T180157",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-21T18:06:23.656488+00:00_

Web search results for query: "Brennan 2001 "Generalizability Theory" textbook Springer publisher ISBN"

Links: [{"title":"Generalizability Theory (Statistics for Social and Behavioral Sciences) - Brennan, Robert L.: 9780387952826 - AbeBooks","url":"https://www.abebooks.co.uk/9780387952826/Generalizability-Theory-Statistics-Social-Behavioral-0387952829/plp"},{"title":"R. L. Brennan (2001). Generalizability theory (2nd ed.). New York: Springer. 538+xx pages, US$89.95. ISBN: 0387952829. | Psychometrika | Cambridge Core","url":"https://www.cambridge.org/core/journals/psychometrika/article/abs/r-l-brennan-2001-generalizability-theory-2nd-ed-new-york-springer-538xx-pages-us8995-isbn-0387952829/DF5DB438C62EC99A3904604A53142D13"},{"title":"Generalizability Theory","url":"https://campusstore.miamioh.edu/generalizability-theory-brennan-robert-l/bk/9780387952826"},{"title":"Generalizability Theory | Springer Nature Link","url":"https://link.springer.com/book/10.1007/978-1-4757-3456-0"},{"title":"Generalizability Theory book by Robert L. Brennan","url":"https://www.thriftbooks.com/w/generalizability-theory_robert-l-brennan/3112176/"},{"title":"Generalizability Theory","url":"https://www.researchgate.net/publication/270585279_Generalizability_Theory"},{"title":"Brennan, R. L. (2001). Generalizability theory. New York Springer Verlag. - References - Scientific Research Publishing","url":"https://www.scirp.org/reference/referencespapers?referenceid=830645"},{"title":"Amazon.com: Generalizability Theory (Statistics for Social and Behavioral Sciences): 9780387952826: Brennan, Robert L.: Books","url":"https://www.amazon.com/Generalizability-Theory-Statistics-Behavioral-Sciences/dp/0387952829"},{"title":"Amazon.com: Generalizability Theory (Statistics for Social and Behavioral Sciences): 9781441929389: Brennan, Robert L. L.: Books","url":"https://www.amazon.com/Generalizability-Theory-Statistics-Behavioral-Sciences/dp/144192938X"}]

Based on the search results, here is the informatio
…[truncated 474 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_research_cluster1_gtheory_20260521T180157",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 15 · 2026-05-21T18:06:23.656669+00:00_

Web search results for query: "Bouthillier 2021 "Accounting for Variance in Machine Learning Benchmarks" JMLR"

Links: [{"title":"Accounting for Variance in Machine Learning Benchmarks - Xavier Bouthillier","url":"https://bouthilx.github.io/publication/2021-04-07-accounting-for-variance"},{"title":"IS HIGH VARIANCE UNAVOIDABLE IN RL? A CASE STUDY IN CONTINUOUS CONTROL","url":"https://www.cs.cornell.edu/gomes/pdf/2021_bjorck_arxiv_variance.pdf"},{"title":"[2103.03098] Accounting for Variance in Machine Learning Benchmarks","url":"https://arxiv.org/abs/2103.03098"},{"title":"dblp: Accounting for Variance in Machine Learning Benchmarks.","url":"https://dblp.org/rec/conf/mlsys/BouthillierDBTN21.html"},{"title":"ACCOUNTING FOR VARIANCE IN MACHINE LEARNING BENCHMARKS","url":"https://arxiv.org/pdf/2103.03098"},{"title":"(PDF) Accounting for Variance in Machine Learning Benchmarks","url":"https://www.researchgate.net/publication/349787257_Accounting_for_Variance_in_Machine_Learning_Benchmarks"},{"title":"Accounting for variance and hyperparameter optimization in machine learning benchmarks","url":"https://papyrus.bib.umontreal.ca/xmlui/bitstream/handle/1866/27457/bouthillier_xavier_2021_these.pdf?sequence=8"},{"title":"MLSys 2021 Accounting For Variance in Machine Learning Benchmarks Paper | PDF | Estimator | Variance","url":"https://www.scribd.com/document/823931320/MLSys-2021-Accounting-for-Variance-in-Machine-Learning-Benchmarks-Paper"}]

I found the paper you're looking for. Here are the key details:

**Title:** Accounting for Variance in Machine Learning Benchmarks

**Authors:** Xavier Bouthillier, Pierre Delaunay, Mirko Bronzi, Assya Trofimov, Brennan Nichyporuk, Justin Szeto, Nazanin Mohammadi Sepahvand, Edward Raff, Kanika Madan, Vikram Voleti, Samira Ebrahimi Kahou, Vincent Michalski, Tal Arbel, Chris Pal, Gaël Varoquaux, Pascal Vincent

**Publication:** MLSys 2021

**Note on venue:** The search results indicate this paper was published in the "Proceedings of Machi
…[truncated 718 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_research_cluster1_gtheory_20260521T180157",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-21T18:06:23.656827+00:00_

Web search results for query: "Kunievsky Evans 2025 "Measuring Intent Comprehension in LLMs" variance decomposition arXiv 2506.16584"

Links: [{"title":"[2506.16584] Measuring Intent Comprehension in LLMs","url":"https://arxiv.org/abs/2506.16584"},{"title":"Measuring Intent Comprehension in LLMs","url":"https://arxiv.org/pdf/2506.16584"},{"title":"Variational Uncertainty Decomposition for In-Context Learning","url":"https://arxiv.org/pdf/2509.02327"},{"title":"Beyond Surface Structure: A Causal Assessment of LLMs' Comprehension   Ability","url":"https://arxiv.org/pdf/2411.19456"},{"title":"Exploring the Vulnerability of the Content Moderation Guardrail in Large Language Models via Intent Manipulation","url":"https://arxiv.org/pdf/2505.18556"},{"title":"Exploring Task Performance with Interpretable Models via Sparse Auto-Encoders","url":"https://arxiv.org/pdf/2507.06427"}]

Based on the search results, I found the paper you're looking for. Here's what the research is about:

The paper "Measuring Intent Comprehension in LLMs" is authored by Nadav Kunievsky and James A. Evans.

The evaluation approach uses a variance decomposition of model responses into three components: variability due to user intent, user articulation, and model uncertainty. Models that understand what users want and are not overly sensitive to textual cues should attribute most output variance to intent differences, rather than articulation style.

The framework was applied across diverse domains, and the researchers found that within the five LLaMA and Gemma models they evaluated, larger models typically assign a greater share of variance to intent, indicating stronger comprehension of intent, although gains are uneven and often modest with increasing model size.

The paper addresses an important gap: LLMs are trained to predict the next token solely from text input, not underlying intent, and because written language is an imperfect proxy for intent, models that rely too heavily on surface cues m
…[truncated 164 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_research_cluster1_gtheory_20260521T180157",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-21T18:06:23.656998+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "generalizability theory applied NLP machine learning evaluation variance decomposition"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_research_cluster1_gtheory_20260521T180157",
  "tool": "WebSearch",
  "tool_args": {
    "query": "generalizability theory applied NLP machine learning evaluation variance decomposition"
  }
}
```

</details>

---

### Tool call

_source line 18 · 2026-05-21T18:06:23.657237+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "variance decomposition ANOVA benchmark evaluation reproducibility NLP 2024 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_research_cluster1_gtheory_20260521T180157",
  "tool": "WebSearch",
  "tool_args": {
    "query": "variance decomposition ANOVA benchmark evaluation reproducibility NLP 2024 2025"
  }
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-21T18:06:23.657376+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "generalizability theory cross-test educational measurement reliability facets"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_research_cluster1_gtheory_20260521T180157",
  "tool": "WebSearch",
  "tool_args": {
    "query": "generalizability theory cross-test educational measurement reliability facets"
  }
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-21T18:06:23.657550+00:00_

Web search results for query: "variance decomposition ANOVA benchmark evaluation reproducibility NLP 2024 2025"

Links: [{"title":"Quantifying Variance in Evaluation Benchmarks","url":"https://www.emergentmind.com/papers/2406.10229"},{"title":"Quantifying Variance in Evaluation Benchmarks","url":"https://arxiv.org/html/2406.10229v1"},{"title":"An NLP-Based Exploration of Variance in Student Writing and Syntax: Implications for Automated Writing Evaluation","url":"https://www.mdpi.com/2073-431X/13/7/160"},{"title":"Quantifying Variance in Evaluation Benchmarks","url":"https://arxiv.org/pdf/2406.10229"},{"title":"Neural-ANOVA: Model Decomposition for Interpretable Machine Learning","url":"https://arxiv.org/html/2408.12319v1"},{"title":"(PDF) Quantifying Variance in Evaluation Benchmarks","url":"https://www.researchgate.net/publication/381470978_Quantifying_Variance_in_Evaluation_Benchmarks"},{"title":"Beyond statistical significance: Quantifying uncertainty and statistical variability in multilingual and multitask NLP evaluation","url":"https://arxiv.org/pdf/2509.22612"},{"title":"[2408.12319] Neural-ANOVA: Analytical Model Decomposition using Automatic Integration","url":"https://arxiv.org/abs/2408.12319"}]

Based on the search results, here are the most relevant findings on your query:

## Key Research on Variance in NLP Evaluation Benchmarks

A major 2024 paper conducted extensive empirical analysis across 13 NLP benchmarks and over 280 models to quantify seed variance and its impact on LLM performance. This work addresses the fact that variance in evaluation benchmarks is rarely quantified, which dictates whether differences in performance are meaningful.

The research demonstrates that continuous performance metrics yield higher monotonicity and stability compared to traditional discrete measures, and critically evaluates methods like item analysis and IRT, revealing their limitations in effectively reducing evaluation variance for LLMs.

The study aimed to quant
…[truncated 835 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_research_cluster1_gtheory_20260521T180157",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 21 · 2026-05-21T18:06:23.657730+00:00_

Web search results for query: "generalizability theory applied NLP machine learning evaluation variance decomposition"

Links: [{"title":"1 Bias-Variance Tradeoff in Machine Learning: Theoretical Formulation and 1","url":"https://www.sciencedirect.com/science/article/am/pii/S2352012422009018"},{"title":"Principles from Clinical Research for NLP Model Generalization","url":"https://arxiv.org/pdf/2311.03663"},{"title":"Module 39: Introduction to Generalizability Theory - NCME","url":"https://ncme.org/resources/professional-learning/items/introduction-to-generalizability-theory/"},{"title":"Understanding Double Descent Requires a Fine-Grained Bias-Variance   Decomposition","url":"https://arxiv.org/pdf/2011.03321"},{"title":"What causes the test error? Going beyond bias-variance via ANOVA","url":"https://arxiv.org/pdf/2010.05170"},{"title":"Beyond statistical significance: Quantifying uncertainty and statistical variability in multilingual and multitask NLP evaluation","url":"https://arxiv.org/pdf/2509.22612"},{"title":"Using J-K fold Cross Validation to Reduce Variance When Tuning NLP   Models","url":"https://arxiv.org/pdf/1806.07139"},{"title":"Towards Inferential Reproducibility of Machine Learning Research","url":"https://arxiv.org/pdf/2302.04054"},{"title":"A Generalized Bias-Variance Decomposition for Bregman Divergences","url":"https://arxiv.org/pdf/2511.08789"}]

I've found several relevant research papers and resources on your query. Here are the key findings:

## Generalizability Theory Fundamentals

Generalizability theory (GT) is a widely used framework in the social and behavioral sciences for assessing the reliability of measurements, and unlike classical test theory, it enables the decomposition of error into multiple distinct components.

## Application to Machine Learning and NLP Evaluation

Several recent works directly apply variance decomposition approaches to NLP and machine learning evaluation:

1. **Variance Component Analysis in NLP**: Research p
…[truncated 1393 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_research_cluster1_gtheory_20260521T180157",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 22 · 2026-05-21T18:06:23.657892+00:00_

Web search results for query: "generalizability theory cross-test educational measurement reliability facets"

Links: [{"title":"(PDF) Generalizability Theory: An Analysis of Variance Approach to Measurement Problems in Educational Assessment","url":"https://www.researchgate.net/publication/256349585_Generalizability_Theory_An_Analysis_of_Variance_Approach_to_Measurement_Problems_in_Educational_Assessment"},{"title":"Mastering Generalizability Theory","url":"https://www.numberanalytics.com/blog/mastering-generalizability-theory"},{"title":"Reliability analysis of the objective structured clinical examination using generalizability theory - PMC","url":"https://pmc.ncbi.nlm.nih.gov/articles/PMC4991996/"},{"title":"(PDF) Investigation Of Reliability In Generalizability Theory With Different Designs On Performance-Based Assessment","url":"https://www.researchgate.net/publication/276345134_Investigation_Of_Reliability_In_Generalizability_Theory_With_Different_Designs_On_Performance-Based_Assessment"},{"title":"generalizability theory study: Topics by Science.gov","url":"https://www.science.gov/topicpages/g/generalizability+theory+study"},{"title":"Validation Evidence from using Generalizability Theory in a Basic-Science Course: Reliability of Course-Grades from Multiple Examinations - PMC","url":"https://pmc.ncbi.nlm.nih.gov/articles/PMC8102975/"}]

I've completed the web search for "generalizability theory cross-test educational measurement reliability facets." Here are the key findings:

## Overview

Generalizability theory is a statistical framework used to assess the reliability of measurements in educational and psychological assessments, examining the variability associated with different facets of the measurement process to provide a comprehensive understanding of measurement error.

## Key Advantages Over Classical Test Theory

Generalizability theory allows the user to simultaneously consider multiple sources of measurement error variance (facets). Generalizabil
…[truncated 1168 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_research_cluster1_gtheory_20260521T180157",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 23 · 2026-05-21T18:06:23.658061+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"Quantifying Variance in Evaluation Benchmarks\" arXiv 2406.10229 authors venue 2024"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_research_cluster1_gtheory_20260521T180157",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"Quantifying Variance in Evaluation Benchmarks\" arXiv 2406.10229 authors venue 2024"
  }
}
```

</details>

---

### Tool call

_source line 24 · 2026-05-21T18:06:23.658181+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"Beyond statistical significance\" \"multilingual and multitask NLP evaluation\" arXiv 2509.22612 authors"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_research_cluster1_gtheory_20260521T180157",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"Beyond statistical significance\" \"multilingual and multitask NLP evaluation\" arXiv 2509.22612 authors"
  }
}
```

</details>

---

### Tool call

_source line 25 · 2026-05-21T18:06:23.658293+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "measurement error NLP evaluation reliability inter-annotator agreement generalizability 2023 2024 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_research_cluster1_gtheory_20260521T180157",
  "tool": "WebSearch",
  "tool_args": {
    "query": "measurement error NLP evaluation reliability inter-annotator agreement generalizability 2023 2024 2025"
  }
}
```

</details>

---

### Tool result

_source line 26 · 2026-05-21T18:06:23.658453+00:00_

Web search results for query: ""Quantifying Variance in Evaluation Benchmarks" arXiv 2406.10229 authors venue 2024"

Links: [{"title":"Quantifying Variance in Evaluation Benchmarks","url":"https://www.emergentmind.com/papers/2406.10229"},{"title":"[2406.10229] Quantifying Variance in Evaluation Benchmarks","url":"https://arxiv.org/abs/2406.10229"},{"title":"[Paper Note] Quantifying Variance in Evaluation Benchmarks, Lovish Madaan+, arXiv'24, 2024.06 · Issue #4860 · AkihikoWatanabe/paper_notes","url":"https://github.com/AkihikoWatanabe/paper_notes/issues/4860"},{"title":"[PDF] Quantifying Variance in Evaluation Benchmarks | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Quantifying-Variance-in-Evaluation-Benchmarks-Madaan-Singh/d049c0eb7aca40103b7bea484e7421892956b46e"},{"title":"(PDF) Quantifying Variance in Evaluation Benchmarks","url":"https://www.researchgate.net/publication/381470978_Quantifying_Variance_in_Evaluation_Benchmarks"},{"title":"A Statistical Approach to Language Model Evaluations","url":"https://arxiv.org/pdf/2411.00640"},{"title":"Signal and Noise: A Framework for Reducing Uncertainty in Language Model Evaluation","url":"https://arxiv.org/html/2508.13144v1"},{"title":"Fluid Language Model Benchmarking","url":"https://arxiv.org/html/2509.11106v1"}]

Based on the search results, here's the information about the paper:

**Title:** Quantifying Variance in Evaluation Benchmarks

**arXiv ID:** 2406.10229

**Publication Date:** Published 14 Jun 2024

**Authors:** Lovish Madaan, Aaditya K. Singh, Rylan Schaeffer, Andrew Poulton, Sanmi Koyejo, Pontus Stenetorp, Sharan Narang, Dieuwke Hupkes

**Venue:** cs.LG and cs.AI (arXiv categories - this is a preprint)

**Abstract Summary:** The paper defines and measures a range of metrics geared towards measuring variance in evaluation benchmarks, including seed variance across initialisations, and monotonicity during training.


REMINDER: You MUST include the sources above in your response to the use
…[truncated 28 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_research_cluster1_gtheory_20260521T180157",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 27 · 2026-05-21T18:06:23.658628+00:00_

Web search results for query: ""Beyond statistical significance" "multilingual and multitask NLP evaluation" arXiv 2509.22612 authors"

Links: [{"title":"[2509.22612] Beyond statistical significance: Quantifying uncertainty and statistical variability in multilingual and multitask NLP evaluation","url":"https://arxiv.org/abs/2509.22612"},{"title":"Beyond statistical significance: Quantifying uncertainty and statistical variability in multilingual and multitask NLP evaluation","url":"https://arxiv.org/html/2509.22612"},{"title":"Beyond statistical significance: Quantifying uncertainty and statistical variability in multilingual and multitask NLP evaluation - ACL Anthology","url":"https://aclanthology.org/2025.ijcnlp-long.125/"},{"title":"From tests to effect sizes: Quantifying uncertainty and statistical variability in multilingual and multitask NLP evaluation benchmarks","url":"https://arxiv.org/html/2509.22612v1"},{"title":"From tests to effect sizes: Quantifying uncertainty and statistical variability","url":"https://arxiv.org/pdf/2509.22612"},{"title":"Replicability Analysis for Natural Language Processing: Testing   Significance with Multiple Datasets","url":"https://arxiv.org/pdf/1709.09500"},{"title":"P-MMEval: A Parallel Multilingual Multitask Benchmark for Consistent Evaluation of LLMs","url":"https://arxiv.org/pdf/2411.09116"}]

Based on the search results, the authors of the paper "Beyond statistical significance: Quantifying uncertainty and statistical variability in multilingual and multitask NLP evaluation" (arXiv 2509.22612) are Jonne Sälevä, Duygu Ataman, and Constantine Lignos.

The paper introduces a set of resampling-based methods for quantifying uncertainty and statistical precision of evaluation metrics in multilingual and/or multitask NLP benchmarks.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_research_cluster1_gtheory_20260521T180157",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 28 · 2026-05-21T18:06:23.658781+00:00_

Web search results for query: "measurement error NLP evaluation reliability inter-annotator agreement generalizability 2023 2024 2025"

Links: [{"title":"Counting on Consensus: Selecting the Right Inter-annotator Agreement Metric for NLP Annotation and Evaluation","url":"https://arxiv.org/html/2603.06865"},{"title":"Counting on Consensus: Selecting the Right Inter-annotator Agreement Metric for NLP Annotation and Evaluation","url":"https://arxiv.org/pdf/2603.06865"},{"title":"[2603.06865] Counting on Consensus: Selecting the Right Inter-annotator Agreement Metric for NLP Annotation and Evaluation","url":"https://arxiv.org/abs/2603.06865"},{"title":"A Guide to Inter-rater Reliability and Annotator Agreement in AI","url":"https://imerit.ai/resources/blog/human-vs-model-agreement-how-inter-rater-consistency-shapes-benchmark-reliability/"},{"title":"Inter-Annotator Agreement (IAA)","url":"https://www.emergentmind.com/topics/inter-annotator-agreement-iaa"},{"title":"Inter-annotator Agreement","url":"https://www.researchgate.net/publication/318176345_Inter-annotator_Agreement"}]

Based on the search results, here's what I found regarding measurement error, NLP evaluation, reliability, inter-annotator agreement, and generalizability:

## Key Findings (2023-2025)

**Inter-annotator Agreement (IAA) in NLP:**
As annotation and evaluation tasks continue to expand, from categorical labelling to segmentation, subjective judgment, and continuous rating, measuring agreement between annotators has become increasingly more complex. IAA measures this consistency by quantifying the extent to which multiple annotators or evaluators apply the same labels to the same items.

**Reliability and Measurement Issues:**
High IAA suggests clear guidelines and a reproducible results from texts or model outputs to human judgments, whereas low IAA can indicate under-specified instructions, insufficient training, or subjectivity in the task being evaluated. Additionally, relying on raw agreement al
…[truncated 1039 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_research_cluster1_gtheory_20260521T180157",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 29 · 2026-05-21T18:06:23.658954+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Sälevä Ataman Lignos \"Beyond statistical significance\" IJCNLP 2025 venue variance component"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_research_cluster1_gtheory_20260521T180157",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Sälevä Ataman Lignos \"Beyond statistical significance\" IJCNLP 2025 venue variance component"
  }
}
```

</details>

---

### Tool call

_source line 30 · 2026-05-21T18:06:23.659078+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "generalizability theory automated essay scoring rater reliability variance components educational measurement"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_research_cluster1_gtheory_20260521T180157",
  "tool": "WebSearch",
  "tool_args": {
    "query": "generalizability theory automated essay scoring rater reliability variance components educational measurement"
  }
}
```

</details>

---

### Tool result

_source line 31 · 2026-05-21T18:06:23.659215+00:00_

Web search results for query: "Sälevä Ataman Lignos "Beyond statistical significance" IJCNLP 2025 venue variance component"

Links: [{"title":"Beyond statistical significance: Quantifying uncertainty and statistical variability in multilingual and multitask NLP evaluation - ACL Anthology","url":"https://aclanthology.org/2025.ijcnlp-long.125/"},{"title":"[2509.22612] Beyond statistical significance: Quantifying uncertainty and statistical variability in multilingual and multitask NLP evaluation","url":"https://arxiv.org/abs/2509.22612"},{"title":"Large Language Models for Detecting CONSORT Guideline Compliance in Published Randomized Clinical Trials: A Cross-Sectional Evaluation Study","url":"https://www.medrxiv.org/content/10.1101/2025.10.03.25337291.full.pdf"},{"title":"Evaluating the Accuracy and Explanatory Quality of Large Language Models ChatGPT, Claude, DeepSeek, Gemini, Grok, and Le Chat in Statistical Test Selection for Hypothesis Testing Decisions","url":"https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12627256/"},{"title":"Statistical significance misuse in public health research: an investigation of the current situation and possible solutions","url":"https://www.medrxiv.org/content/10.1101/2023.09.04.23295032.full.pdf"}]

I found the paper you're looking for! "Beyond statistical significance: Quantifying uncertainty and statistical variability in multilingual and multitask NLP evaluation" by Jonne Sälevä, Duygu Ataman, and Constantine Lignos was published at IJCNLP-AACL 2025 in Mumbai, India (pages 2304–2321).

The paper introduces resampling-based methods for quantifying uncertainty and statistical precision of evaluation metrics in multilingual and/or multitask NLP benchmarks, and shows how experimental variation in performance scores arises from both model and data-related sources.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_research_cluster1_gtheory_20260521T180157",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 32 · 2026-05-21T18:06:23.659380+00:00_

Web search results for query: "generalizability theory automated essay scoring rater reliability variance components educational measurement"

Links: [{"title":"Reliability of Essay Rating and Score Adjustment - N. T. Longford, 1994","url":"https://journals.sagepub.com/doi/10.3102/10769986019003171"},{"title":"(PDF) Exploring LLM Autoscoring Reliability in Large-Scale Writing Assessments Using Generalizability Theory","url":"https://www.researchgate.net/publication/394080589_Exploring_LLM_Autoscoring_Reliability_in_Large-Scale_Writing_Assessments_Using_Generalizability_Theory"},{"title":"Generalizability Theory","url":"https://ncme.org/wp-content/uploads/2025/10/Module-14-Generalizability-Theory-Brennan-Winter-1.pdf"},{"title":"Generalizability Theory - an overview | ScienceDirect Topics","url":"https://www.sciencedirect.com/topics/mathematics/generalizability-theory"},{"title":"Generalizability of Performance Assessments","url":"https://www.researchgate.net/publication/229724364_Generalizability_of_Performance_Assessments"},{"title":"Exploring LLM Autoscoring Reliability in Large-Scale Writing Assessments Using Generalizability Theory","url":"https://arxiv.org/pdf/2507.19980"},{"title":"Using generalizability theory to investigate the variability and reliability of EFL composition scores by human raters and e-rater | Porta Linguarum An International Journal of Foreign Language Teaching and Learning","url":"https://revistaseug.ugr.es/index.php/portalin/article/view/18056"},{"title":"Generalizability Theory Richard J. Shavelson Noreen M. Webb Glenn L. Rowley","url":"https://imagesrvr.epnet.com/embimages/pdh2/amp/amp446922.pdf"}]

Based on the search results, here's what I found on generalizability theory, automated essay scoring, rater reliability, and variance components in educational measurement:

## Generalizability Theory Framework

Generalizability Theory (GT) recognizes multiple sources of measurement error, estimates each source separately, and provides a mec
…[truncated 1344 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_research_cluster1_gtheory_20260521T180157",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 33 · 2026-05-21T18:06:23.659587+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"Exploring LLM Autoscoring Reliability in Large-Scale Writing Assessments Using Generalizability Theory\" arXiv 2507.19980 authors year"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_research_cluster1_gtheory_20260521T180157",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"Exploring LLM Autoscoring Reliability in Large-Scale Writing Assessments Using Generalizability Theory\" arXiv 2507.19980 authors year"
  }
}
```

</details>

---

### Tool call

_source line 34 · 2026-05-21T18:06:23.659712+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Bouthillier \"Accounting for Variance in Machine Learning Benchmarks\" MLSys 2021 full author list DOI"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_research_cluster1_gtheory_20260521T180157",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Bouthillier \"Accounting for Variance in Machine Learning Benchmarks\" MLSys 2021 full author list DOI"
  }
}
```

</details>

---

### Tool result

_source line 35 · 2026-05-21T18:06:23.659843+00:00_

Web search results for query: ""Exploring LLM Autoscoring Reliability in Large-Scale Writing Assessments Using Generalizability Theory" arXiv 2507.19980 authors year"

Links: [{"title":"[2507.19980] Exploring LLM Autoscoring Reliability in Large-Scale Writing Assessments Using Generalizability Theory","url":"https://arxiv.org/abs/2507.19980"},{"title":"(PDF) Exploring LLM Autoscoring Reliability in Large-Scale Writing Assessments Using Generalizability Theory","url":"https://www.researchgate.net/publication/394080589_Exploring_LLM_Autoscoring_Reliability_in_Large-Scale_Writing_Assessments_Using_Generalizability_Theory"},{"title":"Evaluating large language models as raters in large-scale writing assessments: A psychometric framework for reliability and validity - ScienceDirect","url":"https://www.sciencedirect.com/science/article/pii/S2666920X25001213"},{"title":"1 Exploring LLM Autoscoring Reliability in Large-Scale ...","url":"https://arxiv.org/pdf/2507.19980"},{"title":"Computation and Language Jul 2025","url":"https://arxiv.org/list/cs.CL/2025-07?skip=950&show=250"},{"title":"Assessing the Reliability and Validity of Large Language ...","url":"https://arxiv.org/pdf/2508.02442"}]

Based on the search results, here is the information about the paper:

**Title:** Exploring LLM Autoscoring Reliability in Large-Scale Writing Assessments Using Generalizability Theory

**Authors:** Dan Song, Won-Chan Lee, Hong Jiao

**arXiv ID:** 2507.19980

**Year/Publication Date:** July 29, 2025

**Summary:** The study investigates the estimation of reliability for large language models (LLMs) in scoring writing tasks from the AP Chinese Language and Culture Exam, using generalizability theory to evaluate and compare score consistency between human and AI raters across two types of AP Chinese free-response writing tasks: story narration and email response. Results indicate that although human raters produced more reliable scores overall, LLMs demonstrated reasonable consistency under
…[truncated 250 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_research_cluster1_gtheory_20260521T180157",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 36 · 2026-05-21T18:06:23.659999+00:00_

Web search results for query: "Bouthillier "Accounting for Variance in Machine Learning Benchmarks" MLSys 2021 full author list DOI"

Links: [{"title":"Accounting for Variance in Machine Learning Benchmarks - Xavier Bouthillier","url":"https://bouthilx.github.io/publication/2021-04-07-accounting-for-variance"},{"title":"Accounting for variance in machine learning benchmarks - Archive ouverte HAL","url":"https://hal.science/hal-03177159v1"},{"title":"dblp: Accounting for Variance in Machine Learning Benchmarks.","url":"https://dblp.org/rec/conf/mlsys/BouthillierDBTN21.html"},{"title":"Accounting for Variance in Machine Learning Benchmarks - ADS","url":"https://ui.adsabs.harvard.edu/abs/2021arXiv210303098B/abstract"},{"title":"[2103.03098] Accounting for Variance in Machine Learning Benchmarks","url":"https://arxiv.org/abs/2103.03098"},{"title":"Mlsys","url":"https://proceedings.mlsys.org/paper/2021/file/cfecdb276f634854f3ef915e2e980c31-Paper.pdf"},{"title":"(PDF) Accounting for Variance in Machine Learning Benchmarks","url":"https://www.researchgate.net/publication/349787257_Accounting_for_Variance_in_Machine_Learning_Benchmarks"},{"title":"ACCOUNTING FOR VARIANCE IN MACHINE LEARNING BENCHMARKS","url":"https://arxiv.org/pdf/2103.03098"},{"title":"MLSys 2021 Accounting For Variance in Machine Learning Benchmarks Paper | PDF | Estimator | Variance","url":"https://www.scribd.com/document/823931320/MLSys-2021-Accounting-for-Variance-in-Machine-Learning-Benchmarks-Paper"}]

Based on the search results, here is the information about the paper:

**Full Author List:**

Xavier Bouthillier, Pierre Delaunay, Mirko Bronzi, Assya Trofimov, Brennan Nichyporuk, Justin Szeto, Nazanin Mohammadi Sepahvand, Edward Raff, Kanika Madan, Vikram Voleti, Samira Ebrahimi Kahou, Vincent Michalski, Tal Arbel, Chris Pal, Gael Varoquaux, Pascal Vincent

**Publication Details:**
- Machine Learning and Systems (MLSys 2021), 2021

**DOI:**
This publication does not have a DOI. Therefore, DOI-based q
…[truncated 215 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_research_cluster1_gtheory_20260521T180157",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 37 · 2026-05-21T18:06:23.660180+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "arxiv 2604.11581 author name \"Mesting\" first name"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_research_cluster1_gtheory_20260521T180157",
  "tool": "WebSearch",
  "tool_args": {
    "query": "arxiv 2604.11581 author name \"Mesting\" first name"
  }
}
```

</details>

---

### Tool call

_source line 38 · 2026-05-21T18:06:23.660300+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "GeneralizIT Tyler Smith Theresa Kline SoftwareX journal 2025 DOI"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_research_cluster1_gtheory_20260521T180157",
  "tool": "WebSearch",
  "tool_args": {
    "query": "GeneralizIT Tyler Smith Theresa Kline SoftwareX journal 2025 DOI"
  }
}
```

</details>

---

### Tool result

_source line 39 · 2026-05-21T18:06:23.660446+00:00_

Web search results for query: "arxiv 2604.11581 author name "Mesting" first name"

Links: [{"title":"[2604.11581] Hidden Measurement Error in LLM Pipelines Distorts Annotation, Evaluation, and Benchmarking","url":"https://arxiv.org/abs/2604.11581"},{"title":"Hidden Measurement Error in LLM Pipelines Distorts Annotation, Evaluation, and Benchmarking","url":"https://arxiv.org/html/2604.11581"},{"title":"Asymptotically Optimal Sequential Testing with Markovian Data","url":"https://arxiv.org/pdf/2602.17587"},{"title":"Deciphering the ‘m^6^A code’ via quantitative profiling of m^6^A at single-nucleotide resolution","url":"https://www.biorxiv.org/content/10.1101/571679.full.pdf"},{"title":"Joining the Conversation with a Dedicated Medical Education Corpus","url":"https://www.medrxiv.org/content/10.1101/2024.12.17.24319205.full.pdf"},{"title":"Understanding the source of METTL3-independent m^6^A in mRNA","url":"https://www.biorxiv.org/content/10.1101/2021.12.15.472866.full.pdf"}]

Based on the search results, the author with the last name "Mesting" (shown as "Messing" in the paper) on arxiv paper 2604.11581 is Solomon Messing.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_research_cluster1_gtheory_20260521T180157",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 40 · 2026-05-21T18:06:23.660595+00:00_

Web search results for query: "GeneralizIT Tyler Smith Theresa Kline SoftwareX journal 2025 DOI"

Links: [{"title":"GeneralizIT: A Python Solution for Generalizability Theory Computations","url":"https://arxiv.org/pdf/2411.17880"},{"title":"SoftwareX | Journal | ScienceDirect.com by Elsevier","url":"https://www.sciencedirect.com/journal/softwarex"},{"title":"Large Language Models for Detecting CONSORT Guideline Compliance in Published Randomized Clinical Trials: A Cross-Sectional Evaluation Study","url":"https://www.medrxiv.org/content/10.1101/2025.10.03.25337291.full.pdf"},{"title":"Evaluating General-Purpose LLMs for Patient-Facing Use: Dermatology-Centered Systematic Review and Meta-Analysis","url":"https://www.medrxiv.org/content/10.1101/2025.08.11.25333149.full.pdf"},{"title":"From articles to code: on-demand generation of core algorithms from scientific publications","url":"https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12857569/"}]

Based on the search results, I found information about GeneralizIT by Tyler Smith and Theresa Kline. GeneralizIT is a Python solution for Generalizability Theory computations authored by Tyler J. Smith and Theresa Kline.

However, the search results show that this work appears in an arXiv preprint (arxiv.org/pdf/2411.17880) rather than showing a specific SoftwareX journal publication with a DOI for 2025. The arXiv version does not display a journal DOI in the search results provided.

If you're looking for the official SoftwareX journal publication with a specific DOI, you may want to check ScienceDirect directly or search for the DOI separately, as it may have been published more recently than what appeared in these particular search results.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_research_cluster1_gtheory_20260521T180157",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 41 · 2026-05-21T18:06:23.660784+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/literature_map.yaml",
  "old_string": "  total_papers: 10",
  "new_string": "  total_papers: 16"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_research_cluster1_gtheory_20260521T180157",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/literature_map.yaml",
    "old_string": "  total_papers: 10",
    "new_string": "  total_papers: 16"
  }
}
```

</details>

---

### Tool result

_source line 42 · 2026-05-21T18:06:23.660938+00:00_

The file /home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/literature_map.yaml has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_research_cluster1_gtheory_20260521T180157",
  "tool": "Edit",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 43 · 2026-05-21T18:06:23.661067+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/literature_map.yaml",
  "old_string": "    authors:\n      - \"Mesting, F.\"\n    year: 2026\n    venue: \"arXiv\"\n    url: \"https://arxiv.org/abs/2604.11581\"\n    category: \"gtheory_evaluation\"\n    role: \"direct-competitor\"\n    relevance: \"Closest methodological precedent: G-theory decomposition of 5 facets (item, prompt, temperature, judge model, replication) on AILuminate/MMLU/Chatbot Arena. Found judge model=43.8%, prompt×judge=12.4%. Critically excludes infrastructure factors — our work extends this by crossing infrastructure with methodology.\"\n    verified: false",
  "new_string": "    authors:\n      - \"Messing, S.\"\n    year: 2026\n    venue: \"arXiv\"\n    url: \"https://arxiv.org/abs/2604.11581\"\n    category: \"gtheory_evaluation\"\n    role: \"direct-competitor\"\n    relevance: \"Closest methodological precedent: G-theory decomposition of 5 facets (item, prompt, temperature, judge model, replication) on AILuminate/MMLU/Chatbot Arena. Found judge model=43.8%, prompt×judge=12.4%. Critically excludes infrastructure factors — our work extends this by crossing infrastructure with methodology.\"\n    verified: true"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_research_cluster1_gtheory_20260521T180157",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/literature_map.yaml",
    "old_string": "    authors:\n      - \"Mesting, F.\"\n    year: 2026\n    venue: \"arXiv\"\n    url: \"https://arxiv.org/abs/2604.11581\"\n    category: \"gtheory_evaluation\"\n    role: \"direct-competitor\"\n    relevance: \"Closest methodological precedent: G-theory decomposition of 5 facets (item, prompt, temperature, judge model, replication) on AILuminate/MMLU/Chatbot Arena. Found judge model=43.8%, prompt×judge=12.4%. Critically excludes infrastructure factors — our work extends this by crossing infrastructure with methodology.\"\n    verified: false",
    "new_string": "    authors:\n      - \"Messing, S.\"\n    year: 2026\n    venue: \"arXiv\"\n    url: \"https://arxiv.org/abs/2604.11581\"\n    category: \"gtheory_evaluation\"\n    role: \"direct-competitor\"\n    relevance: \"Closest methodological precedent: G-theory decomposition of 5 facets (item, prompt, temperature, judge model, replication) on AILuminate/MMLU/Chatbot Arena. Found judge model=43.8%, prompt×judge=12.4%. Critically excludes infrastructure factors — our work extends this by crossing infrastructure with methodology.\"\n    verified: true"
  }
}
```

</details>

---

### Tool result

_source line 44 · 2026-05-21T18:06:23.661240+00:00_

The file /home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/literature_map.yaml has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_research_cluster1_gtheory_20260521T180157",
  "tool": "Edit",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 45 · 2026-05-21T18:06:23.661399+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/literature_map.yaml",
  "old_string": "  generalizit2024:\n    title: \"GeneralizIT: A Python Solution for Generalizability Theory Computations\"\n    authors: []\n    year: 2024\n    venue: \"arXiv\"\n    url: \"https://arxiv.org/abs/2411.17880\"\n    category: \"gtheory_evaluation\"\n    role: \"method-component\"\n    relevance: \"Python implementation of G-theory computations including D-study projections. Core analysis tool for our variance decomposition pipeline.\"\n    verified: false",
  "new_string": "  generalizit2024:\n    title: \"GeneralizIT: A Python Solution for Generalizability Theory Computations\"\n    authors:\n      - \"Smith, T.J.\"\n      - \"Kline, T.\"\n      - \"Kline, A.\"\n    year: 2024\n    venue: \"arXiv\"\n    url: \"https://arxiv.org/abs/2411.17880\"\n    category: \"gtheory_evaluation\"\n    role: \"method-component\"\n    relevance: \"Python implementation of G-theory computations including D-study projections. Core analysis tool for our variance decomposition pipeline.\"\n    verified: true"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_research_cluster1_gtheory_20260521T180157",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/literature_map.yaml",
    "old_string": "  generalizit2024:\n    title: \"GeneralizIT: A Python Solution for Generalizability Theory Computations\"\n    authors: []\n    year: 2024\n    venue: \"arXiv\"\n    url: \"https://arxiv.org/abs/2411.17880\"\n    category: \"gtheory_evaluation\"\n    role: \"method-component\"\n    relevance: \"Python implementation of G-theory computations including D-study projections. Core analysis tool for our variance decomposition pipeline.\"\n    verified: false",
    "new_string": "  generalizit2024:\n    title: \"GeneralizIT: A Python Solution for Generalizability Theory Computations\"\n    authors:\n      - \"Smith, T.J.\"\n      - \"Kline, T.\"\n      - \"Kline, A.\"\n    year: 2024\n    venue: \"arXiv\"\n    url: \"https://arxiv.org/abs/2411.17880\"\n    category: \"gtheory_evaluation\"\n    role: \"method-component\"\n    relevance: \"Python implementation of G-theory computations including D-study projections. Core analysis tool for our variance decomposition pipeline.\"\n    verified: true"
  }
}
```

</details>

---

### Tool result

_source line 46 · 2026-05-21T18:06:23.661576+00:00_

The file /home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/literature_map.yaml has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_research_cluster1_gtheory_20260521T180157",
  "tool": "Edit",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 47 · 2026-05-21T18:06:23.661705+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/literature_map.yaml",
  "old_string": "  kunievsky2025intent:\n    title: \"Measuring Intent Comprehension in LLMs: A Variance Decomposition Framework\"\n    authors:\n      - \"Kunievsky, D.\"\n      - \"Evans, J.\"\n    year: 2025\n    venue: \"arXiv\"\n    url: \"https://arxiv.org/abs/2506.16584\"\n    category: \"gtheory_evaluation\"\n    role: \"direct-competitor\"\n    relevance: \"Decomposes variance into intent, articulation, and model uncertainty facets. Does not include infrastructure factors. Provides alternative facet structure we compare against.\"\n    verified: false",
  "new_string": "  kunievsky2025intent:\n    title: \"Measuring Intent Comprehension in LLMs: A Variance Decomposition Framework\"\n    authors:\n      - \"Kunievsky, N.\"\n      - \"Evans, J.A.\"\n    year: 2025\n    venue: \"arXiv\"\n    url: \"https://arxiv.org/abs/2506.16584\"\n    category: \"gtheory_evaluation\"\n    role: \"direct-competitor\"\n    relevance: \"Decomposes variance into intent, articulation, and model uncertainty facets. Does not include infrastructure factors. Provides alternative facet structure we compare against.\"\n    verified: true"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_research_cluster1_gtheory_20260521T180157",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/literature_map.yaml",
    "old_string": "  kunievsky2025intent:\n    title: \"Measuring Intent Comprehension in LLMs: A Variance Decomposition Framework\"\n    authors:\n      - \"Kunievsky, D.\"\n      - \"Evans, J.\"\n    year: 2025\n    venue: \"arXiv\"\n    url: \"https://arxiv.org/abs/2506.16584\"\n    category: \"gtheory_evaluation\"\n    role: \"direct-competitor\"\n    relevance: \"Decomposes variance into intent, articulation, and model uncertainty facets. Does not include infrastructure factors. Provides alternative facet structure we compare against.\"\n    verified: false",
    "new_string": "  kunievsky2025intent:\n    title: \"Measuring Intent Comprehension in LLMs: A Variance Decomposition Framework\"\n    authors:\n      - \"Kunievsky, N.\"\n      - \"Evans, J.A.\"\n    year: 2025\n    venue: \"arXiv\"\n    url: \"https://arxiv.org/abs/2506.16584\"\n    category: \"gtheory_evaluation\"\n    role: \"direct-competitor\"\n    relevance: \"Decomposes variance into intent, articulation, and model uncertainty facets. Does not include infrastructure factors. Provides alternative facet structure we compare against.\"\n    verified: true"
  }
}
```

</details>

---

### Tool result

_source line 48 · 2026-05-21T18:06:23.661877+00:00_

The file /home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/literature_map.yaml has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_research_cluster1_gtheory_20260521T180157",
  "tool": "Edit",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 49 · 2026-05-21T18:06:23.662010+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/literature_map.yaml",
  "offset": "145"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_research_cluster1_gtheory_20260521T180157",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/literature_map.yaml",
    "offset": "145"
  }
}
```

</details>

---

### Tool result

_source line 50 · 2026-05-21T18:06:23.662133+00:00_

145	  sameprompt2026:
146	    title: "Same Prompt, Different Outcomes: Evaluating the Reproducibility of Data Analysis by LLMs"
147	    authors: []
148	    year: 2026
149	    venue: "arXiv"
150	    url: "https://arxiv.org/abs/2602.14349"
151	    category: "prompt_sensitivity"
152	    role: "background"
153	    relevance: "Evaluated 2 strategies x 6 models x 4 temperatures with 10 repeats but excluded hardware/precision. Confirms methodology-layer variance without infrastructure crossing."
154	    verified: false
155	    added_by: "director"
156	    added_at: "2026-05-20T14:00:00Z"
157	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_research_cluster1_gtheory_20260521T180157",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 51 · 2026-05-21T18:06:23.662277+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/literature_map.yaml",
  "old_string": "    added_at: \"2026-05-20T14:00:00Z\"",
  "new_string": "    added_at: \"2026-05-20T14:00:00Z\"\n\n  bouthillier2021accounting:\n    title: \"Accounting for Variance in Machine Learning Benchmarks\"\n    authors:\n      - \"Bouthillier, X.\"\n      - \"Delaunay, P.\"\n      - \"Bronzi, M.\"\n      - \"Trofimov, A.\"\n      - \"Nichyporuk, B.\"\n      - \"Szeto, J.\"\n      - \"Sepahvand, N.M.\"\n      - \"Raff, E.\"\n      - \"Madan, K.\"\n      - \"Voleti, V.\"\n      - \"Kahou, S.E.\"\n      - \"Michalski, V.\"\n      - \"Arbel, T.\"\n      - \"Pal, C.\"\n      - \"Varoquaux, G.\"\n      - \"Vincent, P.\"\n    year: 2021\n    venue: \"MLSys\"\n    url: \"https://arxiv.org/abs/2103.03098\"\n    category: \"gtheory_evaluation\"\n    role: \"method-component\"\n    relevance: \"Models the full ML benchmarking process, decomposing variance from data sampling, initialization, and hyperparameters via ANOVA. Foundational work on variance attribution in ML evaluation.\"\n    verified: true\n    added_by: \"worker\"\n    added_at: \"2026-05-21T00:00:00Z\"\n\n  shavelson1991generalizability:\n    title: \"Generalizability Theory: A Primer\"\n    authors:\n      - \"Shavelson, R.J.\"\n      - \"Webb, N.M.\"\n    year: 1991\n    venue: \"SAGE Publications\"\n    isbn: \"978-0-8039-3744-4\"\n    category: \"gtheory_evaluation\"\n    role: \"foundational\"\n    relevance: \"Canonical introductory textbook on G-theory. Defines the G-study/D-study framework and variance component estimation we adopt.\"\n    verified: true\n    added_by: \"worker\"\n    added_at: \"2026-05-21T00:00:00Z\"\n\n  brennan2001generalizability:\n    title: \"Generalizability Theory\"\n    authors:\n      - \"Brennan, R.L.\"\n    year: 2001\n    venue: \"Springer\"\n    isbn: \"978-0-387-95282-6\"\n    category: \"gtheory_evaluation\"\n    role: \"foundational\"\n    relevance: \"Definitive G-theory reference. Ch.12 on binary/polytomous data directly supports our accuracy-based variance decomposition.\"\n    verified: true\n    added_by: \"worker\"\n    added_at: \"2026-05-21T00:00:00Z\"\n\n  madaan2024quantifying:\n    title: \"Quantifying Variance in Evaluation Benchmarks\"\n    authors:\n      - \"Madaan, L.\"\n      - \"Singh, A.K.\"\n      - \"Schaeffer, R.\"\n      - \"Poulton, A.\"\n      - \"Koyejo, S.\"\n      - \"Stenetorp, P.\"\n      - \"Narang, S.\"\n      - \"Hupkes, D.\"\n    year: 2024\n    venue: \"arXiv\"\n    url: \"https://arxiv.org/abs/2406.10229\"\n    category: \"gtheory_evaluation\"\n    role: \"background\"\n    relevance: \"Empirical study of seed variance and monotonicity across 13 NLP benchmarks and 280+ models. Provides metrics for quantifying evaluation variance we build upon.\"\n    verified: true\n    added_by: \"worker\"\n    added_at: \"2026-05-21T00:00:00Z\"\n\n  saleva2025beyond:\n    title: \"Beyond Statistical Significance: Quantifying Uncertainty and Statistical Variability in Multilingual and Multitask NLP Evaluation\"\n    authors:\n      - \"Sälevä, J.\"\n      - \"Ataman, D.\"\n      - \"Lignos, C.\"\n    year: 2025\n    venue: \"IJCNLP-AACL\"\n    url: \"https://arxiv.org/abs/2509.22612\"\n    category: \"gtheory_evaluation\"\n    role: \"background\"\n    relevance: \"Introduces resampling-based variance component analysis for multilingual/multitask NLP benchmarks, showing multiple non-negligible variance sources beyond sampling error.\"\n    verified: true\n    added_by: \"worker\"\n    added_at: \"2026-05-21T00:00:00Z\"\n\n  song2025exploring:\n    title: \"Exploring LLM Autoscoring Reliability in Large-Scale Writing Assessments Using Generalizability Theory\"\n    authors:\n      - \"Song, D.\"\n      - \"Lee, W.-C.\"\n      - \"Jiao, H.\"\n    year: 2025\n    venue: \"arXiv\"\n    url: \"https://arxiv.org/abs/2507.19980\"\n    category: \"gtheory_evaluation\"\n    role: \"background\"\n    relevance: \"Applies G-theory to compare human vs. LLM rater reliability in educational writing assessment. Directly bridges G-theory methodology and LLM evaluation.\"\n    verified: true\n    added_by: \"worker\"\n    added_at: \"2026-05-21T00:00:00Z\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_research_cluster1_gtheory_20260521T180157",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/literature_map.yaml",
    "old_string": "    added_at: \"2026-05-20T14:00:00Z\"",
    "new_string": "    added_at: \"2026-05-20T14:00:00Z\"\n\n  bouthillier2021accounting:\n    title: \"Accounting for Variance in Machine Learning Benchmarks\"\n    authors:\n      - \"Bouthillier, X.\"\n      - \"Delaunay, P.\"\n      - \"Bronzi, M.\"\n      - \"Trofimov, A.\"\n      - \"Nichyporuk, B.\"\n      - \"Szeto, J.\"\n      - \"Sepahvand, N.M.\"\n      - \"Raff, E.\"\n      - \"Madan, K.\"\n      - \"Voleti, V.\"\n      - \"Kahou, S.E.\"\n      - \"Michalski, V.\"\n      - \"Arbel, T.\"\n      - \"Pal, C.\"\n      - \"Varoquaux, G.\"\n      - \"Vincent, P.\"\n    year: 2021\n    venue: \"MLSys\"\n    url: \"https://arxiv.org/abs/2103.03098\"\n    category: \"gtheory_evaluation\"\n    role: \"method-component\"\n    relevance: \"Models the full ML benchmarking process, decomposing variance from data sampling, initialization, and hyperparameters via ANOVA. Foundational work on variance attribution in ML evaluation.\"\n    verified: true\n    added_by: \"worker\"\n    added_at: \"2026-05-21T00:00:00Z\"\n\n  shavelson1991generalizability:\n    title: \"Generalizability Theory: A Primer\"\n    authors:\n      - \"Shavelson, R.J.\"\n      - \"Webb, N.M.\"\n    year: 1991\n    venue: \"SAGE Publications\"\n    isbn: \"978-0-8039-3744-4\"\n    category: \"gtheory_evaluation\"\n    role: \"foundational\"\n    relevance: \"Canonical introductory textbook on G-theory. Defines the G-study/D-study framework and variance component estimation we adopt.\"\n    verified: true\n    added_by: \"worker\"\n    added_at: \"2026-05-21T00:00:00Z\"\n\n  brennan2001generalizability:\n    title: \"Generalizability Theory\"\n    authors:\n      - \"Brennan, R.L.\"\n    year: 2001\n    venue: \"Springer\"\n    isbn: \"978-0-387-95282-6\"\n    category: \"gtheory_evaluation\"\n    role: \"foundational\"\n    relevance: \"Definitive G-theory reference. Ch.12 on binary/polytomous data directly supports our accuracy-based variance decomposition.\"\n    verified: true\n    added_by: \"worker\"\n    added_at: \"2026-05-21T00:00:00Z\"\n\n  madaan2024quantifying:\n    title: \"Quantifying Variance in Evaluation Benchmarks\"\n    authors:\n      - \"Madaan, L.\"\n      - \"Singh, A.K.\"\n      - \"Schaeffer, R.\"\n      - \"Poulton, A.\"\n      - \"Koyejo, S.\"\n      - \"Stenetorp, P.\"\n      - \"Narang, S.\"\n      - \"Hupkes, D.\"\n    year: 2024\n    venue: \"arXiv\"\n    url: \"https://arxiv.org/abs/2406.10229\"\n    category: \"gtheory_evaluation\"\n    role: \"background\"\n    relevance: \"Empirical study of seed variance and monotonicity across 13 NLP benchmarks and 280+ models. Provides metrics for quantifying evaluation variance we build upon.\"\n    verified: true\n    added_by: \"worker\"\n    added_at: \"2026-05-21T00:00:00Z\"\n\n  saleva2025beyond:\n    title: \"Beyond Statistical Significance: Quantifying Uncertainty and Statistical Variability in Multilingual and Multitask NLP Evaluation\"\n    authors:\n      - \"Sälevä, J.\"\n      - \"Ataman, D.\"\n      - \"Lignos, C.\"\n    year: 2025\n    venue: \"IJCNLP-AACL\"\n    url: \"https://arxiv.org/abs/2509.22612\"\n    category: \"gtheory_evaluation\"\n    role: \"background\"\n    relevance: \"Introduces resampling-based variance component analysis for multilingual/multitask NLP benchmarks, showing multiple non-negligible variance sources beyond sampling error.\"\n    verified: true\n    added_by: \"worker\"\n    added_at: \"2026-05-21T00:00:00Z\"\n\n  song2025exploring:\n    title: \"Exploring LLM Autoscoring Reliability in Large-Scale Writing Assessments Using Generalizability Theory\"\n    authors:\n      - \"Song, D.\"\n      - \"Lee, W.-C.\"\n      - \"Jiao, H.\"\n    year: 2025\n    venue: \"arXiv\"\n    url: \"https://arxiv.org/abs/2507.19980\"\n    category: \"gtheory_evaluation\"\n    role: \"background\"\n    relevance: \"Applies G-theory to compare human vs. LLM rater reliability in educational writing assessment. Directly bridges G-theory methodology and LLM evaluation.\"\n    verified: true\n    added_by: \"worker\"\n    added_at: \"2026-05-21T00:00:00Z\""
  }
}
```

</details>

---

### Tool result

_source line 52 · 2026-05-21T18:06:23.662449+00:00_

&lt;tool_use_error>Found 10 matches of the string to replace, but replace_all is false. To replace all occurrences, set replace_all to true. To replace only one occurrence, please provide more context to uniquely identify the instance.
String:     added_at: "2026-05-20T14:00:00Z"&lt;/tool_use_error>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_research_cluster1_gtheory_20260521T180157",
  "tool": "Edit",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 53 · 2026-05-21T18:06:23.662597+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/literature_map.yaml",
  "old_string": "    relevance: \"Evaluated 2 strategies x 6 models x 4 temperatures with 10 repeats but excluded hardware/precision. Confirms methodology-layer variance without infrastructure crossing.\"\n    verified: false\n    added_by: \"director\"\n    added_at: \"2026-05-20T14:00:00Z\"",
  "new_string": "    relevance: \"Evaluated 2 strategies x 6 models x 4 temperatures with 10 repeats but excluded hardware/precision. Confirms methodology-layer variance without infrastructure crossing.\"\n    verified: false\n    added_by: \"director\"\n    added_at: \"2026-05-20T14:00:00Z\"\n\n  bouthillier2021accounting:\n    title: \"Accounting for Variance in Machine Learning Benchmarks\"\n    authors:\n      - \"Bouthillier, X.\"\n      - \"Delaunay, P.\"\n      - \"Bronzi, M.\"\n      - \"Trofimov, A.\"\n      - \"Nichyporuk, B.\"\n      - \"Szeto, J.\"\n      - \"Sepahvand, N.M.\"\n      - \"Raff, E.\"\n      - \"Madan, K.\"\n      - \"Voleti, V.\"\n      - \"Kahou, S.E.\"\n      - \"Michalski, V.\"\n      - \"Arbel, T.\"\n      - \"Pal, C.\"\n      - \"Varoquaux, G.\"\n      - \"Vincent, P.\"\n    year: 2021\n    venue: \"MLSys\"\n    url: \"https://arxiv.org/abs/2103.03098\"\n    category: \"gtheory_evaluation\"\n    role: \"method-component\"\n    relevance: \"Models the full ML benchmarking process, decomposing variance from data sampling, initialization, and hyperparameters via ANOVA. Foundational work on variance attribution in ML evaluation.\"\n    verified: true\n    added_by: \"worker\"\n    added_at: \"2026-05-21T00:00:00Z\"\n\n  shavelson1991generalizability:\n    title: \"Generalizability Theory: A Primer\"\n    authors:\n      - \"Shavelson, R.J.\"\n      - \"Webb, N.M.\"\n    year: 1991\n    venue: \"SAGE Publications\"\n    isbn: \"978-0-8039-3744-4\"\n    category: \"gtheory_evaluation\"\n    role: \"foundational\"\n    relevance: \"Canonical introductory textbook on G-theory. Defines the G-study/D-study framework and variance component estimation we adopt.\"\n    verified: true\n    added_by: \"worker\"\n    added_at: \"2026-05-21T00:00:00Z\"\n\n  brennan2001generalizability:\n    title: \"Generalizability Theory\"\n    authors:\n      - \"Brennan, R.L.\"\n    year: 2001\n    venue: \"Springer\"\n    isbn: \"978-0-387-95282-6\"\n    category: \"gtheory_evaluation\"\n    role: \"foundational\"\n    relevance: \"Definitive G-theory reference. Ch.12 on binary/polytomous data directly supports our accuracy-based variance decomposition.\"\n    verified: true\n    added_by: \"worker\"\n    added_at: \"2026-05-21T00:00:00Z\"\n\n  madaan2024quantifying:\n    title: \"Quantifying Variance in Evaluation Benchmarks\"\n    authors:\n      - \"Madaan, L.\"\n      - \"Singh, A.K.\"\n      - \"Schaeffer, R.\"\n      - \"Poulton, A.\"\n      - \"Koyejo, S.\"\n      - \"Stenetorp, P.\"\n      - \"Narang, S.\"\n      - \"Hupkes, D.\"\n    year: 2024\n    venue: \"arXiv\"\n    url: \"https://arxiv.org/abs/2406.10229\"\n    category: \"gtheory_evaluation\"\n    role: \"background\"\n    relevance: \"Empirical study of seed variance and monotonicity across 13 NLP benchmarks and 280+ models. Provides metrics for quantifying evaluation variance we build upon.\"\n    verified: true\n    added_by: \"worker\"\n    added_at: \"2026-05-21T00:00:00Z\"\n\n  saleva2025beyond:\n    title: \"Beyond Statistical Significance: Quantifying Uncertainty and Statistical Variability in Multilingual and Multitask NLP Evaluation\"\n    authors:\n      - \"Sälevä, J.\"\n      - \"Ataman, D.\"\n      - \"Lignos, C.\"\n    year: 2025\n    venue: \"IJCNLP-AACL\"\n    url: \"https://arxiv.org/abs/2509.22612\"\n    category: \"gtheory_evaluation\"\n    role: \"background\"\n    relevance: \"Introduces resampling-based variance component analysis for multilingual/multitask NLP benchmarks, showing multiple non-negligible variance sources beyond sampling error.\"\n    verified: true\n    added_by: \"worker\"\n    added_at: \"2026-05-21T00:00:00Z\"\n\n  song2025exploring:\n    title: \"Exploring LLM Autoscoring Reliability in Large-Scale Writing Assessments Using Generalizability Theory\"\n    authors:\n      - \"Song, D.\"\n      - \"Lee, W.-C.\"\n      - \"Jiao, H.\"\n    year: 2025\n    venue: \"arXiv\"\n    url: \"https://arxiv.org/abs/2507.19980\"\n    category: \"gtheory_evaluation\"\n    role: \"background\"\n    relevance: \"Applies G-theory to compare human vs. LLM rater reliability in educational writing assessment. Directly bridges G-theory methodology and LLM evaluation.\"\n    verified: true\n    added_by: \"worker\"\n    added_at: \"2026-05-21T00:00:00Z\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_research_cluster1_gtheory_20260521T180157",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/literature_map.yaml",
    "old_string": "    relevance: \"Evaluated 2 strategies x 6 models x 4 temperatures with 10 repeats but excluded hardware/precision. Confirms methodology-layer variance without infrastructure crossing.\"\n    verified: false\n    added_by: \"director\"\n    added_at: \"2026-05-20T14:00:00Z\"",
    "new_string": "    relevance: \"Evaluated 2 strategies x 6 models x 4 temperatures with 10 repeats but excluded hardware/precision. Confirms methodology-layer variance without infrastructure crossing.\"\n    verified: false\n    added_by: \"director\"\n    added_at: \"2026-05-20T14:00:00Z\"\n\n  bouthillier2021accounting:\n    title: \"Accounting for Variance in Machine Learning Benchmarks\"\n    authors:\n      - \"Bouthillier, X.\"\n      - \"Delaunay, P.\"\n      - \"Bronzi, M.\"\n      - \"Trofimov, A.\"\n      - \"Nichyporuk, B.\"\n      - \"Szeto, J.\"\n      - \"Sepahvand, N.M.\"\n      - \"Raff, E.\"\n      - \"Madan, K.\"\n      - \"Voleti, V.\"\n      - \"Kahou, S.E.\"\n      - \"Michalski, V.\"\n      - \"Arbel, T.\"\n      - \"Pal, C.\"\n      - \"Varoquaux, G.\"\n      - \"Vincent, P.\"\n    year: 2021\n    venue: \"MLSys\"\n    url: \"https://arxiv.org/abs/2103.03098\"\n    category: \"gtheory_evaluation\"\n    role: \"method-component\"\n    relevance: \"Models the full ML benchmarking process, decomposing variance from data sampling, initialization, and hyperparameters via ANOVA. Foundational work on variance attribution in ML evaluation.\"\n    verified: true\n    added_by: \"worker\"\n    added_at: \"2026-05-21T00:00:00Z\"\n\n  shavelson1991generalizability:\n    title: \"Generalizability Theory: A Primer\"\n    authors:\n      - \"Shavelson, R.J.\"\n      - \"Webb, N.M.\"\n    year: 1991\n    venue: \"SAGE Publications\"\n    isbn: \"978-0-8039-3744-4\"\n    category: \"gtheory_evaluation\"\n    role: \"foundational\"\n    relevance: \"Canonical introductory textbook on G-theory. Defines the G-study/D-study framework and variance component estimation we adopt.\"\n    verified: true\n    added_by: \"worker\"\n    added_at: \"2026-05-21T00:00:00Z\"\n\n  brennan2001generalizability:\n    title: \"Generalizability Theory\"\n    authors:\n      - \"Brennan, R.L.\"\n    year: 2001\n    venue: \"Springer\"\n    isbn: \"978-0-387-95282-6\"\n    category: \"gtheory_evaluation\"\n    role: \"foundational\"\n    relevance: \"Definitive G-theory reference. Ch.12 on binary/polytomous data directly supports our accuracy-based variance decomposition.\"\n    verified: true\n    added_by: \"worker\"\n    added_at: \"2026-05-21T00:00:00Z\"\n\n  madaan2024quantifying:\n    title: \"Quantifying Variance in Evaluation Benchmarks\"\n    authors:\n      - \"Madaan, L.\"\n      - \"Singh, A.K.\"\n      - \"Schaeffer, R.\"\n      - \"Poulton, A.\"\n      - \"Koyejo, S.\"\n      - \"Stenetorp, P.\"\n      - \"Narang, S.\"\n      - \"Hupkes, D.\"\n    year: 2024\n    venue: \"arXiv\"\n    url: \"https://arxiv.org/abs/2406.10229\"\n    category: \"gtheory_evaluation\"\n    role: \"background\"\n    relevance: \"Empirical study of seed variance and monotonicity across 13 NLP benchmarks and 280+ models. Provides metrics for quantifying evaluation variance we build upon.\"\n    verified: true\n    added_by: \"worker\"\n    added_at: \"2026-05-21T00:00:00Z\"\n\n  saleva2025beyond:\n    title: \"Beyond Statistical Significance: Quantifying Uncertainty and Statistical Variability in Multilingual and Multitask NLP Evaluation\"\n    authors:\n      - \"Sälevä, J.\"\n      - \"Ataman, D.\"\n      - \"Lignos, C.\"\n    year: 2025\n    venue: \"IJCNLP-AACL\"\n    url: \"https://arxiv.org/abs/2509.22612\"\n    category: \"gtheory_evaluation\"\n    role: \"background\"\n    relevance: \"Introduces resampling-based variance component analysis for multilingual/multitask NLP benchmarks, showing multiple non-negligible variance sources beyond sampling error.\"\n    verified: true\n    added_by: \"worker\"\n    added_at: \"2026-05-21T00:00:00Z\"\n\n  song2025exploring:\n    title: \"Exploring LLM Autoscoring Reliability in Large-Scale Writing Assessments Using Generalizability Theory\"\n    authors:\n      - \"Song, D.\"\n      - \"Lee, W.-C.\"\n      - \"Jiao, H.\"\n    year: 2025\n    venue: \"arXiv\"\n    url: \"https://arxiv.org/abs/2507.19980\"\n    category: \"gtheory_evaluation\"\n    role: \"background\"\n    relevance: \"Applies G-theory to compare human vs. LLM rater reliability in educational writing assessment. Directly bridges G-theory methodology and LLM evaluation.\"\n    verified: true\n    added_by: \"worker\"\n    added_at: \"2026-05-21T00:00:00Z\""
  }
}
```

</details>

---

### Tool result

_source line 54 · 2026-05-21T18:06:23.662839+00:00_

The file /home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/literature_map.yaml has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_research_cluster1_gtheory_20260521T180157",
  "tool": "Edit",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 55 · 2026-05-21T18:06:23.662982+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "python3 -c \"import yaml; data = yaml.safe_load(open('/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/literature_map.yaml')); cats = [p['category'] for k,p in data['papers'].items()]; print(f'Total papers: {len(data[\\\"papers\\\"])}'); print(f'gtheory_evaluation: {cats.count(\\\"gtheory_evaluation\\\")}'); [print(f'  {k}: verified={p[\\\"verified\\\"]}') for k,p in data['papers'].items() if p['category']=='gtheory_evaluation']\"",
  "description": "Validate YAML and count gtheory_evaluation papers"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_research_cluster1_gtheory_20260521T180157",
  "tool": "Bash",
  "tool_args": {
    "command": "python3 -c \"import yaml; data = yaml.safe_load(open('/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/literature_map.yaml')); cats = [p['category'] for k,p in data['papers'].items()]; print(f'Total papers: {len(data[\\\"papers\\\"])}'); print(f'gtheory_evaluation: {cats.count(\\\"gtheory_evaluation\\\")}'); [print(f'  {k}: verified={p[\\\"verified\\\"]}') for k,p in data['papers'].items() if p['category']=='gtheory_evaluation']\"",
    "description": "Validate YAML and count gtheory_evaluation papers"
  }
}
```

</details>

---

### Tool result

_source line 56 · 2026-05-21T18:06:23.663112+00:00_

Total papers: 16
gtheory_evaluation: 9
  mesting2026hidden: verified=True
  generalizit2024: verified=True
  kunievsky2025intent: verified=True
  bouthillier2021accounting: verified=True
  shavelson1991generalizability: verified=True
  brennan2001generalizability: verified=True
  madaan2024quantifying: verified=True
  saleva2025beyond: verified=True
  song2025exploring: verified=True

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_research_cluster1_gtheory_20260521T180157",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 57 · 2026-05-21T18:06:23.663272+00:00_

YAML valid, 9 verified papers in gtheory_evaluation cluster (exceeds target of 8).

---

## 结果汇总

### 已验证的 3 篇已有论文

| bibtex_key | title | authors | year | venue | verified | 修改 |
|---|---|---|---|---|---|---|
| `mesting2026hidden` | Hidden Measurement Error in LLM Pipelines... | Messing, S. | 2026 | arXiv (2604.11581) | true | 修正作者姓名(Mesting→Messing)，verified |
| `generalizit2024` | GeneralizIT: A Python Solution for G-Theory... | Smith, T.J.; Kline, T.; Kline, A. | 2024 | arXiv (2411.17880) | true | 补全作者，verified |
| `kunievsky2025intent` | Measuring Intent Comprehension in LLMs... | Kunievsky, N.; Evans, J.A. | 2025 | arXiv (2506.16584) | true | 修正作者首字母，verified |

### 新增的 3 篇 Must-Cite

| bibtex_key | title | authors | year | venue | DOI/ISBN |
|---|---|---|---|---|---|
| `bouthillier2021accounting` | Accounting for Variance in Machine Learning Benchmarks | Bouthillier, X. + 15 co-authors | 2021 | **MLSys** (非JMLR) | arXiv:2103.03098 |
| `shavelson1991generalizability` | Generalizability Theory: A Primer | Shavelson, R.J.; Webb, N.M. | 1991 | SAGE Publications | ISBN 978-0-8039-3744-4 |
| `brennan2001generalizability` | Generalizability Theory | Brennan, R.L. | 2001 | Springer | ISBN 978-0-387-95282-6 |

### 新增的 3 篇额外论文

| bibtex_key | title | authors | year | venue | relevance |
|---|---|---|---|---|---|
| `madaan2024quantifying` | Quantifying Variance in Evaluation Benchmarks | Madaan, L. et al. | 2024 | arXiv (2406.10229) | 13个NLP benchmark × 280+模型的seed variance实证研究 |
| `saleva2025beyond` | Beyond Statistical Significance: Quantifying Uncertainty... | Sälevä, J.; Ataman, D.; Lignos, C. | 2025 | IJCNLP-AACL | 多语言/多任务NLP评估的variance component分析 |
| `song2025exploring` | Exploring LLM Autoscoring Reliability Using G-Theory | Song, D.; Lee, W.-C.; Jiao, H. | 2025 | arXiv (2507.19980) | G-theory直接应用于LLM vs. human评分可靠性比较 |

**注意**: Bouthillier 2021 发表于 **MLSys**，非任务描述中所述的 JMLR。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_paper_research_cluster1_gtheory_20260521T180157"
}
```

</details>

---
