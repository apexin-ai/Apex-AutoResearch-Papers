# paper research cluster4 irt

**Reproducibility Budgets for Open-Weight LLM Evaluation: A Generalizability Theory Study of 7–9B Instruction-Tuned Models** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 37
- **Recorded user turns:** 0
- **Tool calls:** 18
- **Original source:** `logs/chats/worker_paper_research_cluster4_irt_20260521T185524.jsonl`
- **Structured JSON:** [`dad604a32080dd9cffdb.json`](../../sessions/da/dad604a32080dd9cffdb.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

37 recorded events

### Tool call

_source line 1 · 2026-05-21T18:58:00.218211+00:00_

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
  "session": "worker_paper_research_cluster4_irt_20260521T185524",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/literature_map.yaml"
  }
}
```

</details>

---

### Tool result

_source line 2 · 2026-05-21T18:58:00.218624+00:00_

1	meta:
2	  last_updated: "2026-05-21T12:00:00Z"
3	  total_papers: 20
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
23	      - "Messing, S."
24	    year: 2026
25	    venue: "arXiv"
26	    url: "https://arxiv.org/abs/2604.11581"
27	    category: "gtheory_evaluation"
28	    role: "direct-competitor"
29	    relevance: "Closest methodological precedent: G-theory decomposition of 5 facets (item, prompt, temperature, judge model, replication) on AILuminate/MMLU/Chatbot Arena. Found judge model=43.8%, prompt×judge=12.4%. Critically excludes infrastructure factors — our work extends this by crossing infrastructure with methodology."
30	    verified: true
31	    added_by: "director"
32	    added_at: "2026-05-20T14:00:00Z"
33	
34	  brittlebench2026:
35	    title: "Brittlebench: Quantifying LLM Robustness via Prompt Sensitivity"
36	    authors:
37	      - "Romanou, A."
38	      - "Ibrahim, M."
39	      - "Ross, C."
40	      - "Shaib, C."
41	      - "Oktar, K."
42	      - "Bell, S.J."
43	      - "Ovalle, A."
44	      - "Dodge, J."
45	      - "Bosselut, A."
46	      - "Sinha, K."
47	      - "Williams, A."
48	    year: 2026
49	    
…[truncated 13999 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_research_cluster4_irt_20260521T185524",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-21T18:58:00.218841+00:00_

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
  "session": "worker_paper_research_cluster4_irt_20260521T185524",
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

_source line 4 · 2026-05-21T18:58:00.218982+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_research_cluster4_irt_20260521T185524",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-21T18:58:00.219124+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Polo et al 2024 \"tinyBenchmarks\" evaluating LLMs fewer examples IRT"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_research_cluster4_irt_20260521T185524",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Polo et al 2024 \"tinyBenchmarks\" evaluating LLMs fewer examples IRT"
  }
}
```

</details>

---

### Tool call

_source line 6 · 2026-05-21T18:58:00.219243+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Lalor 2019 NAACL \"Learning Latent Parameters without Human Response Patterns\" IRT NLP"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_research_cluster4_irt_20260521T185524",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Lalor 2019 NAACL \"Learning Latent Parameters without Human Response Patterns\" IRT NLP"
  }
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-21T18:58:00.219356+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Rodriguez 2021 ACL \"Evaluation Examples Are Not Equally Informative\" IRT NLP"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_research_cluster4_irt_20260521T185524",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Rodriguez 2021 ACL \"Evaluation Examples Are Not Equally Informative\" IRT NLP"
  }
}
```

</details>

---

### Tool call

_source line 8 · 2026-05-21T18:58:00.219495+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Perlitz 2023 \"Efficient Benchmarking\" LLM evaluation"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_research_cluster4_irt_20260521T185524",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Perlitz 2023 \"Efficient Benchmarking\" LLM evaluation"
  }
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-21T18:58:00.219616+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "item response theory LLM evaluation 2024 2025 computerized adaptive testing NLP benchmark"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_research_cluster4_irt_20260521T185524",
  "tool": "WebSearch",
  "tool_args": {
    "query": "item response theory LLM evaluation 2024 2025 computerized adaptive testing NLP benchmark"
  }
}
```

</details>

---

### Tool call

_source line 10 · 2026-05-21T18:58:00.219729+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "benchmark subsampling efficiency large language model evaluation IRT 2024 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_research_cluster4_irt_20260521T185524",
  "tool": "WebSearch",
  "tool_args": {
    "query": "benchmark subsampling efficiency large language model evaluation IRT 2024 2025"
  }
}
```

</details>

---

### Tool result

_source line 11 · 2026-05-21T18:58:00.219864+00:00_

Web search results for query: "Polo et al 2024 "tinyBenchmarks" evaluating LLMs fewer examples IRT"

Links: [{"title":"tinyBenchmarks: evaluating LLMs with fewer examples | AI Research Paper Details","url":"https://www.aimodels.fyi/papers/arxiv/tinybenchmarks-evaluating-llms-fewer-examples"},{"title":"tinyBenchmarks: evaluating LLMs with fewer examples for ICLR 2024 - IBM Research","url":"https://research.ibm.com/publications/tinybenchmarks-evaluating-llms-with-fewer-examples"},{"title":"(PDF) tinyBenchmarks: evaluating LLMs with fewer examples","url":"https://www.researchgate.net/publication/383238265_tinyBenchmarks_evaluating_LLMs_with_fewer_examples"},{"title":"GitHub - felipemaiapolo/tinyBenchmarks: Evaluating LLMs with fewer examples · GitHub","url":"https://github.com/felipemaiapolo/tinyBenchmarks"},{"title":"tinyBenchmarks: evaluating LLMs with fewer examples for ICML 2024 - IBM Research","url":"https://research.ibm.com/publications/tinybenchmarks-evaluating-llms-with-fewer-examples--1"},{"title":"[2402.14992] tinyBenchmarks: evaluating LLMs with fewer examples","url":"https://arxiv.org/abs/2402.14992"},{"title":"tinyBenchmarks: evaluating LLMs with fewer examples","url":"https://proceedings.mlr.press/v235/maia-polo24a.html"},{"title":"tinyBenchmarks: evaluating LLMs with fewer examples","url":"https://arxiv.org/pdf/2402.14992"}]

I found the paper you're looking for! Here are the key details:

**Paper Title:** tinyBenchmarks: evaluating LLMs with fewer examples

**Authors:** Felipe Maia Polo, Lucas Weber, Leshem Choshen, Yuekai Sun, Gongjun Xu, Mikhail Yurochkin

**Publication:** Proceedings of the 41st International Conference on Machine Learning, PMLR 235:34303-34326, 2024

**Main Contribution:** The paper proposes tinyBenchmarks, an efficient evaluation method that uses IRT to model the discriminative power of benchmark examples, allowing the selection of a small yet representative subset of items that can accurately estimate performance.

**Core Problem:
…[truncated 528 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_research_cluster4_irt_20260521T185524",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-21T18:58:00.220023+00:00_

Web search results for query: "Lalor 2019 NAACL "Learning Latent Parameters without Human Response Patterns" IRT NLP"

Links: [{"title":"Learning Latent Parameters without Human Response Patterns: Item Response Theory with Artificial Crowds - ACL Anthology","url":"https://aclanthology.org/D19-1434/"},{"title":"Learning Latent Parameters without Human Response Patterns: Item Response Theory with Artificial Crowds | Request PDF","url":"https://www.researchgate.net/publication/336999016_Learning_Latent_Parameters_without_Human_Response_Patterns_Item_Response_Theory_with_Artificial_Crowds"},{"title":"[PDF] Learning Latent Parameters without Human Response Patterns: Item Response Theory with Artificial Crowds | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Learning-Latent-Parameters-without-Human-Response-Lalor-Wu/df6cd8a8d836e75690141deb732f6d19f0176a2e"},{"title":"Learning Latent Parameters without Human Response Patterns: Item Response Theory with Artificial Crowds - PubMed","url":"https://pubmed.ncbi.nlm.nih.gov/31803865/"},{"title":"[1908.11421] Learning Latent Parameters without Human Response Patterns: Item Response Theory with Artificial Crowds","url":"https://arxiv.org/abs/1908.11421"},{"title":"Learning Latent Parameters without Human Response Patterns: Item Response Theory with Artificial Crowds - PMC","url":"https://pmc.ncbi.nlm.nih.gov/articles/PMC6892593/"},{"title":"Learning Latent Parameters without Human Response Patterns: Item   Response Theory with Artificial Crowds","url":"https://arxiv.org/pdf/1908.11421"},{"title":"[1908.11421v1] Learning Latent Parameters without Human Response Patterns: Item Response Theory with Artificial Crowds","url":"https://arxiv.org/abs/1908.11421v1"},{"title":"John P. Lalor University of Notre Dame 338B Mendoza College of Business","url":"https://d23loykajbcndr.cloudfront.net/jlalor1/pci/cv-1.pdf"}]

I found the paper! Here are the key details about the Lalor et al. 2019 work:

**Paper Title:** "Learning La
…[truncated 1032 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_research_cluster4_irt_20260521T185524",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 13 · 2026-05-21T18:58:00.220184+00:00_

Web search results for query: "Rodriguez 2021 ACL "Evaluation Examples Are Not Equally Informative" IRT NLP"

Links: [{"title":"Evaluation Examples are not Equally Informative: How should that change NLP Leaderboards? - ACL Anthology","url":"https://aclanthology.org/2021.acl-long.346/"},{"title":"Evaluation Examples Are Not Equally Informative: How Should That Change NLP Leaderboards?","url":"https://www.pedro.ai/leaderboard-acl2021"},{"title":"Evaluation Examples are not Equally Informative: How should that change NLP Leaderboards? | Request PDF","url":"https://www.researchgate.net/publication/353488536_Evaluation_Examples_are_not_Equally_Informative_How_should_that_change_NLP_Leaderboards"},{"title":"Figure 2 from Evaluation Examples are not Equally Informative: How should that change NLP Leaderboards? | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Evaluation-Examples-are-not-Equally-Informative:-Rodriguez-Barrow/30f233eecca2239ee1dd754914324092e53f8f19/figure/2"},{"title":"GitHub - facebookresearch/irt-leaderboard: Leaderboards are widely used in NLP and push the field forward. While leaderboards are a straightforward ranking of NLP models, this simplicity can mask nuances in evaluation items (examples) and subjects (NLP models). Rather than replace leaderboards, we advocate a re-imagining so that they better highlight if and where progress is made. Building on educational testing, we create a Bayesian leaderboard where latent subject skill and latent item difficulty predict","url":"https://github.com/facebookresearch/irt-leaderboard"},{"title":"Evaluation Examples Are Not Equally Informative:","url":"https://par.nsf.gov/servlets/purl/10309824"},{"title":"[PDF] Evaluation Examples are not Equally Informative: How should that change NLP Leaderboards? | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Evaluation-Examples-are-not-Equally-Informative:-Rodriguez-Barrow/30f233eecca2239ee1dd754914324092e53f8f19"},{"title":"Evaluation Exam
…[truncated 1484 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_research_cluster4_irt_20260521T185524",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-21T18:58:00.220337+00:00_

Web search results for query: "Perlitz 2023 "Efficient Benchmarking" LLM evaluation"

Links: [{"title":"Active Evaluation Acquisition for Efficient LLM Benchmarking","url":"https://arxiv.org/html/2410.05952v1"},{"title":"Do These LLM Benchmarks Agree? Fixing Benchmark Evaluation with BenchBench","url":"https://arxiv.org/html/2407.13696v2"},{"title":"EVALUATING LLMS WITH FEWER EXAMPLES","url":"https://openreview.net/pdf/25ac9459dd5b345badfd3d9a2c5e56b32fd89b07.pdf"},{"title":"Evaluate your LLM using 99% less compute - IBM Research","url":"https://research.ibm.com/blog/efficient-llm-benchmarking"},{"title":"Efficient multi-prompt evaluation of LLMs","url":"https://arxiv.org/pdf/2405.17202"},{"title":"Efficient Evaluation of LLM Performance with Statistical Guarantees","url":"https://arxiv.org/html/2601.20251v3"},{"title":"Efficient Evaluation of Large Language Models via Collaborative   Filtering","url":"https://arxiv.org/pdf/2504.08781"}]

Based on the search results, I found information about the Perlitz et al. 2023 work on efficient benchmarking of language models:

## Perlitz et al. 2023 - Efficient Benchmarking

Yotam Perlitz and colleagues published "Efficient benchmarking (of language models)" as an arXiv preprint (arXiv:2308.11696) in 2023.

### Key Findings

Perlitz et al. found that the model rankings on HELM can be accurately obtained by evaluating only a fraction of the examples. More specifically, Perlitz et al. found that evaluation on HELM relies on diversity across datasets, but the number of examples currently used is excessive.

### Impact and Application

Working closely with Yotam Perlitz, an IBM researcher who specializes in LLM evaluation, the research first introduced efficient benchmarking in a pre-print paper on arXiv and caught the eye of AI researchers who were organizing an efficient LLM contest at NeurIPS 2023.

### Methods and Approach

The stratified sampling approach proposed in this work has been verified as effective on HELM benchmark
…[truncated 450 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_research_cluster4_irt_20260521T185524",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 15 · 2026-05-21T18:58:00.220515+00:00_

Web search results for query: "benchmark subsampling efficiency large language model evaluation IRT 2024 2025"

Links: [{"title":"Published as a conference paper at ICLR 2025 RELIABLE AND EFFICIENT","url":"https://openreview.net/pdf/397ca770a66185f7a77339189f2a6f4dc7beaf50.pdf"},{"title":"Resampling Benchmark for Efficient Comprehensive Evaluation of Large   Vision-Language Models","url":"https://arxiv.org/pdf/2504.09979"},{"title":"Reliable and Efficient Amortized Model-based Evaluation","url":"https://arxiv.org/html/2503.13335v1"},{"title":"metabench A Sparse Benchmark of Reasoning and Knowledge in Large Language Models","url":"https://arxiv.org/html/2407.12844v2"},{"title":"Efficient Evaluation of LLM Performance with Statistical Guarantees","url":"https://arxiv.org/pdf/2601.20251"},{"title":"Lost in Benchmarks? Rethinking Large Language Model Benchmarking with Item Response Theory","url":"https://arxiv.org/html/2505.15055v2"},{"title":"An Interpretable and Scalable Framework for Evaluating Large Language Models","url":"https://arxiv.org/html/2605.07046"}]

I found several relevant results about benchmark subsampling efficiency and large language model evaluation using Item Response Theory (IRT) from 2024-2025. Here are the key findings:

## Efficient LLM Evaluation with IRT

Recent work tackles large-scale generative model evaluation with a model-based approach grounded in IRT, substantially improving the reliability and efficiency of current common practices at a fraction of the cost. The growing size of generative models and benchmarking datasets has significantly increased evaluation costs, leading to a search for efficient LLM evaluation methods.

## Recent Approaches and Research

One approach leverages IRT to reduce the number of examples needed for evaluating LLMs, minimizing computational costs while maintaining performance accuracy. Another approach filters prompts in a data-driven manner by first sub-sampling benchmark items and then characterizing ite
…[truncated 976 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_research_cluster4_irt_20260521T185524",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-21T18:58:00.220679+00:00_

Web search results for query: "item response theory LLM evaluation 2024 2025 computerized adaptive testing NLP benchmark"

Links: [{"title":"(PDF) Lost in Benchmarks? Rethinking Large Language Model Benchmarking with Item Response Theory","url":"https://www.researchgate.net/publication/391954139_Lost_in_Benchmarks_Rethinking_Large_Language_Model_Benchmarking_with_Item_Response_Theory"},{"title":"Confident Rankings with Fewer Items: Adaptive LLM Evaluation with Continuous Scores","url":"https://arxiv.org/html/2601.13885"},{"title":"Confident Rankings with Fewer Items: Adaptive LLM Evaluation with","url":"https://arxiv.org/pdf/2601.13885"},{"title":"Lost in Benchmarks? Rethinking Large Language Model Benchmarking with Item Response Theory","url":"https://arxiv.org/html/2505.15055v2"},{"title":"Adaptive Testing for LLM Evaluation: A Psychometric Alternative to Static Benchmarks","url":"https://arxiv.org/html/2511.04689"},{"title":"Leveraging Computerized Adaptive Testing for Cost-effective Evaluation of Large Language Models in Medical Benchmarking","url":"https://arxiv.org/pdf/2603.23506"},{"title":"Adaptive Testing for LLM Evaluation: A Psychometric Alternative to Static Benchmarks","url":"https://arxiv.org/pdf/2511.04689"},{"title":"Lost in Benchmarks? Rethinking Large Language Model Benchmarking with Item Response Theory","url":"https://arxiv.org/pdf/2505.15055"}]

Based on the search results, here's what I found regarding item response theory (IRT), LLM evaluation, and computerized adaptive testing:

## Key Research Areas (2024-2025)

**Item Response Theory in LLM Benchmarking:**
Item Response Theory offers a psychometric framework for finer-grained, item-level analysis, and within NLP has been utilized to diagnose fundamental item properties such as difficulty and discriminability, and more recently to inspire methods for improving evaluation efficiency through optimized item selection or adaptive testing paradigms.

**Computerized Adaptive Testing (CAT) for LLMs
…[truncated 1115 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_research_cluster4_irt_20260521T185524",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-21T18:58:00.220849+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Perlitz \"Efficient Benchmarking of Language Models\" arXiv 2308.11696 authors"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_research_cluster4_irt_20260521T185524",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Perlitz \"Efficient Benchmarking of Language Models\" arXiv 2308.11696 authors"
  }
}
```

</details>

---

### Tool call

_source line 18 · 2026-05-21T18:58:00.220968+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"Lost in Benchmarks? Rethinking Large Language Model Benchmarking with Item Response Theory\" authors venue 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_research_cluster4_irt_20260521T185524",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"Lost in Benchmarks? Rethinking Large Language Model Benchmarking with Item Response Theory\" authors venue 2025"
  }
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-21T18:58:00.221081+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"Adaptive Testing for LLM Evaluation: A Psychometric Alternative to Static Benchmarks\" arXiv 2511.04689 authors"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_research_cluster4_irt_20260521T185524",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"Adaptive Testing for LLM Evaluation: A Psychometric Alternative to Static Benchmarks\" arXiv 2511.04689 authors"
  }
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-21T18:58:00.221201+00:00_

Web search results for query: "Perlitz "Efficient Benchmarking of Language Models" arXiv 2308.11696 authors"

Links: [{"title":"[2308.11696] Efficient Benchmarking of Language Models","url":"https://arxiv.org/abs/2308.11696"},{"title":"[2308.11696v5] Efficient Benchmarking of Language Models","url":"http://arxiv.org/abs/2308.11696v5"},{"title":"Paper page - Efficient Benchmarking (of Language Models)","url":"https://huggingface.co/papers/2308.11696"},{"title":"Data Efficient Evaluation of Large Language Models and Text-to-Image Models via Adaptive Sampling","url":"https://arxiv.org/html/2406.15527v1"},{"title":"Efficient Benchmarking of Language Models - ADS","url":"https://ui.adsabs.harvard.edu/abs/2023arXiv230811696P/abstract"},{"title":"Efficient Benchmarking of Language Models","url":"https://arxiv.org/pdf/2308.11696"}]

Based on the search results, the authors of the paper "Efficient Benchmarking of Language Models" (arXiv:2308.11696) are: Yotam Perlitz, Elron Bandel, Ariel Gera, Ofir Arviv, Liat Ein-Dor, Eyal Shnarch, Noam Slonim, Michal Shmueli-Scheuer, and Leshem Choshen.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_research_cluster4_irt_20260521T185524",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 21 · 2026-05-21T18:58:00.221370+00:00_

Web search results for query: ""Lost in Benchmarks? Rethinking Large Language Model Benchmarking with Item Response Theory" authors venue 2025"

Links: [{"title":"[2505.15055] Lost in Benchmarks? Rethinking Large Language Model Benchmarking with Item Response Theory","url":"https://arxiv.org/abs/2505.15055"},{"title":"Paper page - Lost in Benchmarks? Rethinking Large Language Model Benchmarking with Item Response Theory","url":"https://huggingface.co/papers/2505.15055"},{"title":"Lost in Benchmarks? Rethinking Large Language Model Benchmarking with Item Response Theory | Proceedings of the AAAI Conference on Artificial Intelligence","url":"https://ojs.aaai.org/index.php/AAAI/article/view/40814"},{"title":"[Literature Review] Lost in Benchmarks? Rethinking Large Language Model Benchmarking with Item Response Theory","url":"https://www.themoonlight.io/en/review/lost-in-benchmarks-rethinking-large-language-model-benchmarking-with-item-response-theory"},{"title":"GitHub - Joe-Hall-Lee/PSN-IRT: [AAAI 2026 Oral] Lost in Benchmarks? Rethinking Large Language Model Benchmarking with Item Response Theory · GitHub","url":"https://github.com/Joe-Hall-Lee/PSN-IRT"},{"title":"Lost in Benchmarks? Rethinking Large Language Model Benchmarking with Item Response Theory","url":"https://chatpaper.com/paper/139423"},{"title":"Lost in Benchmarks? Rethinking Large Language Model Benchmarking with Item Response Theory","url":"https://arxiv.org/html/2505.15055v1"},{"title":"(PDF) Lost in Benchmarks? Rethinking Large Language Model Benchmarking with Item Response Theory","url":"https://www.researchgate.net/publication/391954139_Lost_in_Benchmarks_Rethinking_Large_Language_Model_Benchmarking_with_Item_Response_Theory"}]

Based on the search results, here's the information about this paper:

**Title:** Lost in Benchmarks? Rethinking Large Language Model Benchmarking with Item Response Theory

**Authors:** Hongli Zhou, Hui Huang, Ziqing Zhao, Lvyuan Han, Huicheng Wang, Kehai Chen, Muyun Yang, 
…[truncated 553 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_research_cluster4_irt_20260521T185524",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 22 · 2026-05-21T18:58:00.221545+00:00_

Web search results for query: ""Adaptive Testing for LLM Evaluation: A Psychometric Alternative to Static Benchmarks" arXiv 2511.04689 authors"

Links: [{"title":"[2511.04689] Adaptive Testing for LLM Evaluation: A Psychometric Alternative to Static Benchmarks","url":"https://arxiv.org/abs/2511.04689"},{"title":"Adaptive Testing for LLM Evaluation: A Psychometric Alternative to Static Benchmarks","url":"https://arxiv.org/html/2511.04689"},{"title":"Adaptive Testing for LLM Evaluation: A Psychometric Alternative to Static Benchmarks | OpenReview","url":"https://openreview.net/forum?id=iX39LhePyd"},{"title":"ADAPTIVE TESTING FOR LLM EVALUATION: A","url":"https://arxiv.org/pdf/2511.04689"},{"title":"Leveraging Computerized Adaptive Testing for Cost-effective Evaluation of Large Language Models in Medical Benchmarking","url":"https://arxiv.org/pdf/2603.23506"},{"title":"Adaptive Testing for LLM Evaluation: A Psychometric Alternative to Static Benchmarks | Request PDF","url":"https://www.researchgate.net/publication/397441932_Adaptive_Testing_for_LLM_Evaluation_A_Psychometric_Alternative_to_Static_Benchmarks"},{"title":"From Static Benchmarks to Adaptive Testing: Psychometrics in AI Evaluation","url":"https://arxiv.org/html/2306.10512v3"}]

Based on the search results, here's the information about the paper:

**Title:** Adaptive Testing for LLM Evaluation: A Psychometric Alternative to Static Benchmarks

**arXiv ID:** 2511.04689

**Authors:** Peiyu Li, Xiuxiu Tang, Si Chen, Ying Cheng, Ronald Metoyer, Ting Hua, Nitesh V. Chawla

**Key Contribution:** The paper introduces ATLAS, an adaptive testing framework based on Item Response Theory (IRT) that estimates model ability using Fisher information-guided item selection. ATLAS reduces the number of required items by up to 90% while maintaining measurement precision.

**Validation:** The framework was validated across five major benchmarks (WinoGrande, TruthfulQA, HellaSwag, GSM8K, ARC).


REMINDER: You MUST include the sour
…[truncated 65 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_research_cluster4_irt_20260521T185524",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 23 · 2026-05-21T18:58:00.221734+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "site:arxiv.org 2511.04689 \"Adaptive Testing for LLM Evaluation\" venue accepted conference 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_research_cluster4_irt_20260521T185524",
  "tool": "WebSearch",
  "tool_args": {
    "query": "site:arxiv.org 2511.04689 \"Adaptive Testing for LLM Evaluation\" venue accepted conference 2026"
  }
}
```

</details>

---

### Tool result

_source line 24 · 2026-05-21T18:58:00.221869+00:00_

Web search results for query: "site:arxiv.org 2511.04689 "Adaptive Testing for LLM Evaluation" venue accepted conference 2026"

Links: [{"title":"ADAPTIVE TESTING FOR LLM EVALUATION: A","url":"https://arxiv.org/pdf/2511.04689"},{"title":"[2511.04689] Adaptive Testing for LLM Evaluation: A Psychometric Alternative to Static Benchmarks","url":"https://arxiv.org/abs/2511.04689"},{"title":"Confident Rankings with Fewer Items: Adaptive LLM Evaluation with Continuous Scores","url":"https://arxiv.org/html/2601.13885"},{"title":"Adaptive Testing for LLM Evaluation: A Psychometric Alternative to Static Benchmarks","url":"https://arxiv.org/html/2511.04689"},{"title":"Confident Rankings with Fewer Items: Adaptive LLM Evaluation with Continuous Scores","url":"https://arxiv.org/pdf/2601.13885"},{"title":"Adaptive Testing for LLM-Based Applications: A Diversity-based Approach","url":"https://arxiv.org/html/2501.13480v1"}]

Based on the search results, I found information about the arXiv paper 2511.04689:

The paper is titled "Adaptive Testing for LLM Evaluation: A Psychometric Alternative to Static Benchmarks" by Peiyu Li and 6 other authors.

The paper introduces ATLAS, an adaptive testing framework based on Item Response Theory (IRT) that estimates model ability using Fisher information-guided item selection, and reduces the number of required items by up to 90% while maintaining measurement precision.

However, the search results do not contain information about the paper being accepted to a specific conference venue for 2026. The document itself appears to be a preprint from arXiv (posted October 26, 2025), but conference acceptance status is not mentioned in the available search results.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_research_cluster4_irt_20260521T185524",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 25 · 2026-05-21T18:58:00.222032+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/literature_map.yaml",
  "old_string": "  total_papers: 20",
  "new_string": "  total_papers: 26"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_research_cluster4_irt_20260521T185524",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/literature_map.yaml",
    "old_string": "  total_papers: 20",
    "new_string": "  total_papers: 26"
  }
}
```

</details>

---

### Tool result

_source line 26 · 2026-05-21T18:58:00.222208+00:00_

The file /home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/literature_map.yaml has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_research_cluster4_irt_20260521T185524",
  "tool": "Edit",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 27 · 2026-05-21T18:58:00.222331+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/literature_map.yaml",
  "old_string": "  - key: \"evaluation_methodology\"\n    name: \"Evaluation Methodology\"\n    narrative: \"Scoring artifacts, benchmark design, and evaluation protocol considerations\"",
  "new_string": "  - key: \"evaluation_methodology\"\n    name: \"Evaluation Methodology\"\n    narrative: \"Scoring artifacts, benchmark design, and evaluation protocol considerations\"\n  - key: \"irt_benchmarking\"\n    name: \"IRT & Efficient Benchmarking\"\n    narrative: \"Item Response Theory and efficient evaluation design for LLM benchmarks\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_research_cluster4_irt_20260521T185524",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/literature_map.yaml",
    "old_string": "  - key: \"evaluation_methodology\"\n    name: \"Evaluation Methodology\"\n    narrative: \"Scoring artifacts, benchmark design, and evaluation protocol considerations\"",
    "new_string": "  - key: \"evaluation_methodology\"\n    name: \"Evaluation Methodology\"\n    narrative: \"Scoring artifacts, benchmark design, and evaluation protocol considerations\"\n  - key: \"irt_benchmarking\"\n    name: \"IRT & Efficient Benchmarking\"\n    narrative: \"Item Response Theory and efficient evaluation design for LLM benchmarks\""
  }
}
```

</details>

---

### Tool result

_source line 28 · 2026-05-21T18:58:00.222537+00:00_

The file /home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/literature_map.yaml has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_research_cluster4_irt_20260521T185524",
  "tool": "Edit",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 29 · 2026-05-21T18:58:00.222704+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/literature_map.yaml",
  "old_string": "    added_at: \"2026-05-21T14:00:00Z\"",
  "new_string": "    added_at: \"2026-05-21T14:00:00Z\"\n\n  polo2024tinybenchmarks:\n    title: \"tinyBenchmarks: evaluating LLMs with fewer examples\"\n    authors:\n      - \"Maia Polo, F.\"\n      - \"Weber, L.\"\n      - \"Choshen, L.\"\n      - \"Sun, Y.\"\n      - \"Xu, G.\"\n      - \"Yurochkin, M.\"\n    year: 2024\n    venue: \"ICML 2024\"\n    url: \"https://arxiv.org/abs/2402.14992\"\n    category: \"irt_benchmarking\"\n    role: \"method-component\"\n    relevance: \"Uses IRT to model item discriminative power and select small representative subsets for efficient LLM evaluation. Demonstrates accurate benchmark estimation with drastically fewer examples. Core reference for IRT-based subsampling approach our D-study projections relate to.\"\n    verified: true\n    added_by: \"worker\"\n    added_at: \"2026-05-21T16:00:00Z\"\n\n  lalor2019irt:\n    title: \"Learning Latent Parameters without Human Response Patterns: Item Response Theory with Artificial Crowds\"\n    authors:\n      - \"Lalor, J.P.\"\n      - \"Wu, H.\"\n      - \"Yu, H.\"\n    year: 2019\n    venue: \"EMNLP-IJCNLP 2019\"\n    url: \"https://aclanthology.org/D19-1434/\"\n    category: \"irt_benchmarking\"\n    role: \"foundational\"\n    relevance: \"Pioneering work applying IRT to NLP evaluation without human response data, using artificial crowds of DNN models to estimate item parameters. Establishes the feasibility of IRT-based item analysis for NLP benchmarks that our work builds upon.\"\n    verified: true\n    added_by: \"worker\"\n    added_at: \"2026-05-21T16:00:00Z\"\n\n  rodriguez2021leaderboards:\n    title: \"Evaluation Examples are not Equally Informative: How should that change NLP Leaderboards?\"\n    authors:\n      - \"Rodriguez, P.\"\n      - \"Barrow, J.\"\n      - \"Hoyle, A.\"\n      - \"Lalor, J.P.\"\n      - \"Jia, R.\"\n      - \"Boyd-Graber, J.\"\n    year: 2021\n    venue: \"ACL 2021\"\n    url: \"https://aclanthology.org/2021.acl-long.346/\"\n    category: \"irt_benchmarking\"\n    role: \"foundational\"\n    relevance: \"Creates Bayesian IRT-based leaderboard jointly inferring item difficulty, discriminability, and model skill. Shows IRT can identify annotation errors, detect overfitting, and guide annotation. Foundational work connecting IRT to NLP benchmark design.\"\n    verified: true\n    added_by: \"worker\"\n    added_at: \"2026-05-21T16:00:00Z\"\n\n  perlitz2023efficient:\n    title: \"Efficient Benchmarking of Language Models\"\n    authors:\n      - \"Perlitz, Y.\"\n      - \"Bandel, E.\"\n      - \"Gera, A.\"\n      - \"Arviv, O.\"\n      - \"Ein-Dor, L.\"\n      - \"Shnarch, E.\"\n      - \"Slonim, N.\"\n      - \"Shmueli-Scheuer, M.\"\n      - \"Choshen, L.\"\n    year: 2023\n    venue: \"arXiv\"\n    url: \"https://arxiv.org/abs/2308.11696\"\n    category: \"irt_benchmarking\"\n    role: \"method-component\"\n    relevance: \"Shows HELM model rankings can be accurately recovered from a fraction of examples via stratified subsampling. Demonstrates evaluation relies on dataset diversity, not example count. Complements IRT-based approaches with sampling-theoretic efficiency methods.\"\n    verified: true\n    added_by: \"worker\"\n    added_at: \"2026-05-21T16:00:00Z\"\n\n  zhou2026irt:\n    title: \"Lost in Benchmarks? Rethinking Large Language Model Benchmarking with Item Response Theory\"\n    authors:\n      - \"Zhou, H.\"\n      - \"Huang, H.\"\n      - \"Zhao, Z.\"\n      - \"Han, L.\"\n      - \"Wang, H.\"\n      - \"Chen, K.\"\n      - \"Yang, M.\"\n      - \"Bao, W.\"\n      - \"Dong, J.\"\n      - \"Xu, B.\"\n      - \"Zhu, C.\"\n      - \"Cao, H.\"\n      - \"Zhao, T.\"\n    year: 2026\n    venue: \"AAAI 2026 (Oral)\"\n    url: \"https://arxiv.org/abs/2505.15055\"\n    category: \"irt_benchmarking\"\n    role: \"direct-competitor\"\n    relevance: \"Proposes PSN-IRT, an enhanced IRT framework with rich item parameters for LLM benchmarking. AAAI 2026 oral — represents state-of-the-art in IRT-based LLM evaluation. Directly relevant as concurrent work applying psychometric models to benchmark analysis.\"\n    verified: true\n    added_by: \"worker\"\n    added_at: \"2026-05-21T16:00:00Z\"\n\n  li2025atlas:\n    title: \"Adaptive Testing for LLM Evaluation: A Psychometric Alternative to Static Benchmarks\"\n    authors:\n      - \"Li, P.\"\n      - \"Tang, X.\"\n      - \"Chen, S.\"\n      - \"Cheng, Y.\"\n      - \"Metoyer, R.\"\n      - \"Hua, T.\"\n      - \"Chawla, N.V.\"\n    year: 2025\n    venue: \"arXiv\"\n    url: \"https://arxiv.org/abs/2511.04689\"\n    category: \"irt_benchmarking\"\n    role: \"method-component\"\n    relevance: \"Introduces ATLAS, an IRT-based computerized adaptive testing framework using Fisher information-guided item selection. Reduces required items by up to 90% while maintaining precision. Demonstrates CAT as a practical alternative to static benchmarks for LLM evaluation.\"\n    verified: true\n    added_by: \"worker\"\n    added_at: \"2026-05-21T16:00:00Z\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_research_cluster4_irt_20260521T185524",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/literature_map.yaml",
    "old_string": "    added_at: \"2026-05-21T14:00:00Z\"",
    "new_string": "    added_at: \"2026-05-21T14:00:00Z\"\n\n  polo2024tinybenchmarks:\n    title: \"tinyBenchmarks: evaluating LLMs with fewer examples\"\n    authors:\n      - \"Maia Polo, F.\"\n      - \"Weber, L.\"\n      - \"Choshen, L.\"\n      - \"Sun, Y.\"\n      - \"Xu, G.\"\n      - \"Yurochkin, M.\"\n    year: 2024\n    venue: \"ICML 2024\"\n    url: \"https://arxiv.org/abs/2402.14992\"\n    category: \"irt_benchmarking\"\n    role: \"method-component\"\n    relevance: \"Uses IRT to model item discriminative power and select small representative subsets for efficient LLM evaluation. Demonstrates accurate benchmark estimation with drastically fewer examples. Core reference for IRT-based subsampling approach our D-study projections relate to.\"\n    verified: true\n    added_by: \"worker\"\n    added_at: \"2026-05-21T16:00:00Z\"\n\n  lalor2019irt:\n    title: \"Learning Latent Parameters without Human Response Patterns: Item Response Theory with Artificial Crowds\"\n    authors:\n      - \"Lalor, J.P.\"\n      - \"Wu, H.\"\n      - \"Yu, H.\"\n    year: 2019\n    venue: \"EMNLP-IJCNLP 2019\"\n    url: \"https://aclanthology.org/D19-1434/\"\n    category: \"irt_benchmarking\"\n    role: \"foundational\"\n    relevance: \"Pioneering work applying IRT to NLP evaluation without human response data, using artificial crowds of DNN models to estimate item parameters. Establishes the feasibility of IRT-based item analysis for NLP benchmarks that our work builds upon.\"\n    verified: true\n    added_by: \"worker\"\n    added_at: \"2026-05-21T16:00:00Z\"\n\n  rodriguez2021leaderboards:\n    title: \"Evaluation Examples are not Equally Informative: How should that change NLP Leaderboards?\"\n    authors:\n      - \"Rodriguez, P.\"\n      - \"Barrow, J.\"\n      - \"Hoyle, A.\"\n      - \"Lalor, J.P.\"\n      - \"Jia, R.\"\n      - \"Boyd-Graber, J.\"\n    year: 2021\n    venue: \"ACL 2021\"\n    url: \"https://aclanthology.org/2021.acl-long.346/\"\n    category: \"irt_benchmarking\"\n    role: \"foundational\"\n    relevance: \"Creates Bayesian IRT-based leaderboard jointly inferring item difficulty, discriminability, and model skill. Shows IRT can identify annotation errors, detect overfitting, and guide annotation. Foundational work connecting IRT to NLP benchmark design.\"\n    verified: true\n    added_by: \"worker\"\n    added_at: \"2026-05-21T16:00:00Z\"\n\n  perlitz2023efficient:\n    title: \"Efficient Benchmarking of Language Models\"\n    authors:\n      - \"Perlitz, Y.\"\n      - \"Bandel, E.\"\n      - \"Gera, A.\"\n      - \"Arviv, O.\"\n      - \"Ein-Dor, L.\"\n      - \"Shnarch, E.\"\n      - \"Slonim, N.\"\n      - \"Shmueli-Scheuer, M.\"\n      - \"Choshen, L.\"\n    year: 2023\n    venue: \"arXiv\"\n    url: \"https://arxiv.org/abs/2308.11696\"\n    category: \"irt_benchmarking\"\n    role: \"method-component\"\n    relevance: \"Shows HELM model rankings can be accurately recovered from a fraction of examples via stratified subsampling. Demonstrates evaluation relies on dataset diversity, not example count. Complements IRT-based approaches with sampling-theoretic efficiency methods.\"\n    verified: true\n    added_by: \"worker\"\n    added_at: \"2026-05-21T16:00:00Z\"\n\n  zhou2026irt:\n    title: \"Lost in Benchmarks? Rethinking Large Language Model Benchmarking with Item Response Theory\"\n    authors:\n      - \"Zhou, H.\"\n      - \"Huang, H.\"\n      - \"Zhao, Z.\"\n      - \"Han, L.\"\n      - \"Wang, H.\"\n      - \"Chen, K.\"\n      - \"Yang, M.\"\n      - \"Bao, W.\"\n      - \"Dong, J.\"\n      - \"Xu, B.\"\n      - \"Zhu, C.\"\n      - \"Cao, H.\"\n      - \"Zhao, T.\"\n    year: 2026\n    venue: \"AAAI 2026 (Oral)\"\n    url: \"https://arxiv.org/abs/2505.15055\"\n    category: \"irt_benchmarking\"\n    role: \"direct-competitor\"\n    relevance: \"Proposes PSN-IRT, an enhanced IRT framework with rich item parameters for LLM benchmarking. AAAI 2026 oral — represents state-of-the-art in IRT-based LLM evaluation. Directly relevant as concurrent work applying psychometric models to benchmark analysis.\"\n    verified: true\n    added_by: \"worker\"\n    added_at: \"2026-05-21T16:00:00Z\"\n\n  li2025atlas:\n    title: \"Adaptive Testing for LLM Evaluation: A Psychometric Alternative to Static Benchmarks\"\n    authors:\n      - \"Li, P.\"\n      - \"Tang, X.\"\n      - \"Chen, S.\"\n      - \"Cheng, Y.\"\n      - \"Metoyer, R.\"\n      - \"Hua, T.\"\n      - \"Chawla, N.V.\"\n    year: 2025\n    venue: \"arXiv\"\n    url: \"https://arxiv.org/abs/2511.04689\"\n    category: \"irt_benchmarking\"\n    role: \"method-component\"\n    relevance: \"Introduces ATLAS, an IRT-based computerized adaptive testing framework using Fisher information-guided item selection. Reduces required items by up to 90% while maintaining precision. Demonstrates CAT as a practical alternative to static benchmarks for LLM evaluation.\"\n    verified: true\n    added_by: \"worker\"\n    added_at: \"2026-05-21T16:00:00Z\""
  }
}
```

</details>

---

### Tool result

_source line 30 · 2026-05-21T18:58:00.222875+00:00_

&lt;tool_use_error>Found 2 matches of the string to replace, but replace_all is false. To replace all occurrences, set replace_all to true. To replace only one occurrence, please provide more context to uniquely identify the instance.
String:     added_at: "2026-05-21T14:00:00Z"&lt;/tool_use_error>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_research_cluster4_irt_20260521T185524",
  "tool": "Edit",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 31 · 2026-05-21T18:58:00.223016+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/literature_map.yaml",
  "offset": "365"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_research_cluster4_irt_20260521T185524",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/literature_map.yaml",
    "offset": "365"
  }
}
```

</details>

---

### Tool result

_source line 32 · 2026-05-21T18:58:00.223145+00:00_

365	    title: "Large Language Models Sensitivity to The Order of Options in Multiple-Choice Questions"
366	    authors:
367	      - "Pezeshkpour, P."
368	      - "Hruschka, E."
369	    year: 2024
370	    venue: "NAACL 2024 Findings"
371	    url: "https://aclanthology.org/2024.findings-naacl.130/"
372	    category: "prompt_sensitivity"
373	    role: "background"
374	    relevance: "Documents 13-75% performance gap from answer option reordering in MC benchmarks. Shows LLMs exhibit systematic positional bias favoring certain option identifiers. Demonstrates option ordering as a methodological variance source our G-study framework captures."
375	    verified: true
376	    added_by: "worker"
377	    added_at: "2026-05-21T14:00:00Z"
378	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_research_cluster4_irt_20260521T185524",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 33 · 2026-05-21T18:58:00.223297+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/literature_map.yaml",
  "old_string": "    relevance: \"Documents 13-75% performance gap from answer option reordering in MC benchmarks. Shows LLMs exhibit systematic positional bias favoring certain option identifiers. Demonstrates option ordering as a methodological variance source our G-study framework captures.\"\n    verified: true\n    added_by: \"worker\"\n    added_at: \"2026-05-21T14:00:00Z\"",
  "new_string": "    relevance: \"Documents 13-75% performance gap from answer option reordering in MC benchmarks. Shows LLMs exhibit systematic positional bias favoring certain option identifiers. Demonstrates option ordering as a methodological variance source our G-study framework captures.\"\n    verified: true\n    added_by: \"worker\"\n    added_at: \"2026-05-21T14:00:00Z\"\n\n  polo2024tinybenchmarks:\n    title: \"tinyBenchmarks: evaluating LLMs with fewer examples\"\n    authors:\n      - \"Maia Polo, F.\"\n      - \"Weber, L.\"\n      - \"Choshen, L.\"\n      - \"Sun, Y.\"\n      - \"Xu, G.\"\n      - \"Yurochkin, M.\"\n    year: 2024\n    venue: \"ICML 2024\"\n    url: \"https://arxiv.org/abs/2402.14992\"\n    category: \"irt_benchmarking\"\n    role: \"method-component\"\n    relevance: \"Uses IRT to model item discriminative power and select small representative subsets for efficient LLM evaluation. Demonstrates accurate benchmark estimation with drastically fewer examples. Core reference for IRT-based subsampling approach our D-study projections relate to.\"\n    verified: true\n    added_by: \"worker\"\n    added_at: \"2026-05-21T16:00:00Z\"\n\n  lalor2019irt:\n    title: \"Learning Latent Parameters without Human Response Patterns: Item Response Theory with Artificial Crowds\"\n    authors:\n      - \"Lalor, J.P.\"\n      - \"Wu, H.\"\n      - \"Yu, H.\"\n    year: 2019\n    venue: \"EMNLP-IJCNLP 2019\"\n    url: \"https://aclanthology.org/D19-1434/\"\n    category: \"irt_benchmarking\"\n    role: \"foundational\"\n    relevance: \"Pioneering work applying IRT to NLP evaluation without human response data, using artificial crowds of DNN models to estimate item parameters. Establishes the feasibility of IRT-based item analysis for NLP benchmarks that our work builds upon.\"\n    verified: true\n    added_by: \"worker\"\n    added_at: \"2026-05-21T16:00:00Z\"\n\n  rodriguez2021leaderboards:\n    title: \"Evaluation Examples are not Equally Informative: How should that change NLP Leaderboards?\"\n    authors:\n      - \"Rodriguez, P.\"\n      - \"Barrow, J.\"\n      - \"Hoyle, A.\"\n      - \"Lalor, J.P.\"\n      - \"Jia, R.\"\n      - \"Boyd-Graber, J.\"\n    year: 2021\n    venue: \"ACL 2021\"\n    url: \"https://aclanthology.org/2021.acl-long.346/\"\n    category: \"irt_benchmarking\"\n    role: \"foundational\"\n    relevance: \"Creates Bayesian IRT-based leaderboard jointly inferring item difficulty, discriminability, and model skill. Shows IRT can identify annotation errors, detect overfitting, and guide annotation. Foundational work connecting IRT to NLP benchmark design.\"\n    verified: true\n    added_by: \"worker\"\n    added_at: \"2026-05-21T16:00:00Z\"\n\n  perlitz2023efficient:\n    title: \"Efficient Benchmarking of Language Models\"\n    authors:\n      - \"Perlitz, Y.\"\n      - \"Bandel, E.\"\n      - \"Gera, A.\"\n      - \"Arviv, O.\"\n      - \"Ein-Dor, L.\"\n      - \"Shnarch, E.\"\n      - \"Slonim, N.\"\n      - \"Shmueli-Scheuer, M.\"\n      - \"Choshen, L.\"\n    year: 2023\n    venue: \"arXiv\"\n    url: \"https://arxiv.org/abs/2308.11696\"\n    category: \"irt_benchmarking\"\n    role: \"method-component\"\n    relevance: \"Shows HELM model rankings can be accurately recovered from a fraction of examples via stratified subsampling. Demonstrates evaluation relies on dataset diversity, not example count. Complements IRT-based approaches with sampling-theoretic efficiency methods.\"\n    verified: true\n    added_by: \"worker\"\n    added_at: \"2026-05-21T16:00:00Z\"\n\n  zhou2026irt:\n    title: \"Lost in Benchmarks? Rethinking Large Language Model Benchmarking with Item Response Theory\"\n    authors:\n      - \"Zhou, H.\"\n      - \"Huang, H.\"\n      - \"Zhao, Z.\"\n      - \"Han, L.\"\n      - \"Wang, H.\"\n      - \"Chen, K.\"\n      - \"Yang, M.\"\n      - \"Bao, W.\"\n      - \"Dong, J.\"\n      - \"Xu, B.\"\n      - \"Zhu, C.\"\n      - \"Cao, H.\"\n      - \"Zhao, T.\"\n    year: 2026\n    venue: \"AAAI 2026 (Oral)\"\n    url: \"https://arxiv.org/abs/2505.15055\"\n    category: \"irt_benchmarking\"\n    role: \"direct-competitor\"\n    relevance: \"Proposes PSN-IRT, an enhanced IRT framework with rich item parameters for LLM benchmarking. AAAI 2026 oral — represents state-of-the-art in IRT-based LLM evaluation. Directly relevant as concurrent work applying psychometric models to benchmark analysis.\"\n    verified: true\n    added_by: \"worker\"\n    added_at: \"2026-05-21T16:00:00Z\"\n\n  li2025atlas:\n    title: \"Adaptive Testing for LLM Evaluation: A Psychometric Alternative to Static Benchmarks\"\n    authors:\n      - \"Li, P.\"\n      - \"Tang, X.\"\n      - \"Chen, S.\"\n      - \"Cheng, Y.\"\n      - \"Metoyer, R.\"\n      - \"Hua, T.\"\n      - \"Chawla, N.V.\"\n    year: 2025\n    venue: \"arXiv\"\n    url: \"https://arxiv.org/abs/2511.04689\"\n    category: \"irt_benchmarking\"\n    role: \"method-component\"\n    relevance: \"Introduces ATLAS, an IRT-based computerized adaptive testing framework using Fisher information-guided item selection. Reduces required items by up to 90% while maintaining precision. Demonstrates CAT as a practical alternative to static benchmarks for LLM evaluation.\"\n    verified: true\n    added_by: \"worker\"\n    added_at: \"2026-05-21T16:00:00Z\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_research_cluster4_irt_20260521T185524",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/literature_map.yaml",
    "old_string": "    relevance: \"Documents 13-75% performance gap from answer option reordering in MC benchmarks. Shows LLMs exhibit systematic positional bias favoring certain option identifiers. Demonstrates option ordering as a methodological variance source our G-study framework captures.\"\n    verified: true\n    added_by: \"worker\"\n    added_at: \"2026-05-21T14:00:00Z\"",
    "new_string": "    relevance: \"Documents 13-75% performance gap from answer option reordering in MC benchmarks. Shows LLMs exhibit systematic positional bias favoring certain option identifiers. Demonstrates option ordering as a methodological variance source our G-study framework captures.\"\n    verified: true\n    added_by: \"worker\"\n    added_at: \"2026-05-21T14:00:00Z\"\n\n  polo2024tinybenchmarks:\n    title: \"tinyBenchmarks: evaluating LLMs with fewer examples\"\n    authors:\n      - \"Maia Polo, F.\"\n      - \"Weber, L.\"\n      - \"Choshen, L.\"\n      - \"Sun, Y.\"\n      - \"Xu, G.\"\n      - \"Yurochkin, M.\"\n    year: 2024\n    venue: \"ICML 2024\"\n    url: \"https://arxiv.org/abs/2402.14992\"\n    category: \"irt_benchmarking\"\n    role: \"method-component\"\n    relevance: \"Uses IRT to model item discriminative power and select small representative subsets for efficient LLM evaluation. Demonstrates accurate benchmark estimation with drastically fewer examples. Core reference for IRT-based subsampling approach our D-study projections relate to.\"\n    verified: true\n    added_by: \"worker\"\n    added_at: \"2026-05-21T16:00:00Z\"\n\n  lalor2019irt:\n    title: \"Learning Latent Parameters without Human Response Patterns: Item Response Theory with Artificial Crowds\"\n    authors:\n      - \"Lalor, J.P.\"\n      - \"Wu, H.\"\n      - \"Yu, H.\"\n    year: 2019\n    venue: \"EMNLP-IJCNLP 2019\"\n    url: \"https://aclanthology.org/D19-1434/\"\n    category: \"irt_benchmarking\"\n    role: \"foundational\"\n    relevance: \"Pioneering work applying IRT to NLP evaluation without human response data, using artificial crowds of DNN models to estimate item parameters. Establishes the feasibility of IRT-based item analysis for NLP benchmarks that our work builds upon.\"\n    verified: true\n    added_by: \"worker\"\n    added_at: \"2026-05-21T16:00:00Z\"\n\n  rodriguez2021leaderboards:\n    title: \"Evaluation Examples are not Equally Informative: How should that change NLP Leaderboards?\"\n    authors:\n      - \"Rodriguez, P.\"\n      - \"Barrow, J.\"\n      - \"Hoyle, A.\"\n      - \"Lalor, J.P.\"\n      - \"Jia, R.\"\n      - \"Boyd-Graber, J.\"\n    year: 2021\n    venue: \"ACL 2021\"\n    url: \"https://aclanthology.org/2021.acl-long.346/\"\n    category: \"irt_benchmarking\"\n    role: \"foundational\"\n    relevance: \"Creates Bayesian IRT-based leaderboard jointly inferring item difficulty, discriminability, and model skill. Shows IRT can identify annotation errors, detect overfitting, and guide annotation. Foundational work connecting IRT to NLP benchmark design.\"\n    verified: true\n    added_by: \"worker\"\n    added_at: \"2026-05-21T16:00:00Z\"\n\n  perlitz2023efficient:\n    title: \"Efficient Benchmarking of Language Models\"\n    authors:\n      - \"Perlitz, Y.\"\n      - \"Bandel, E.\"\n      - \"Gera, A.\"\n      - \"Arviv, O.\"\n      - \"Ein-Dor, L.\"\n      - \"Shnarch, E.\"\n      - \"Slonim, N.\"\n      - \"Shmueli-Scheuer, M.\"\n      - \"Choshen, L.\"\n    year: 2023\n    venue: \"arXiv\"\n    url: \"https://arxiv.org/abs/2308.11696\"\n    category: \"irt_benchmarking\"\n    role: \"method-component\"\n    relevance: \"Shows HELM model rankings can be accurately recovered from a fraction of examples via stratified subsampling. Demonstrates evaluation relies on dataset diversity, not example count. Complements IRT-based approaches with sampling-theoretic efficiency methods.\"\n    verified: true\n    added_by: \"worker\"\n    added_at: \"2026-05-21T16:00:00Z\"\n\n  zhou2026irt:\n    title: \"Lost in Benchmarks? Rethinking Large Language Model Benchmarking with Item Response Theory\"\n    authors:\n      - \"Zhou, H.\"\n      - \"Huang, H.\"\n      - \"Zhao, Z.\"\n      - \"Han, L.\"\n      - \"Wang, H.\"\n      - \"Chen, K.\"\n      - \"Yang, M.\"\n      - \"Bao, W.\"\n      - \"Dong, J.\"\n      - \"Xu, B.\"\n      - \"Zhu, C.\"\n      - \"Cao, H.\"\n      - \"Zhao, T.\"\n    year: 2026\n    venue: \"AAAI 2026 (Oral)\"\n    url: \"https://arxiv.org/abs/2505.15055\"\n    category: \"irt_benchmarking\"\n    role: \"direct-competitor\"\n    relevance: \"Proposes PSN-IRT, an enhanced IRT framework with rich item parameters for LLM benchmarking. AAAI 2026 oral — represents state-of-the-art in IRT-based LLM evaluation. Directly relevant as concurrent work applying psychometric models to benchmark analysis.\"\n    verified: true\n    added_by: \"worker\"\n    added_at: \"2026-05-21T16:00:00Z\"\n\n  li2025atlas:\n    title: \"Adaptive Testing for LLM Evaluation: A Psychometric Alternative to Static Benchmarks\"\n    authors:\n      - \"Li, P.\"\n      - \"Tang, X.\"\n      - \"Chen, S.\"\n      - \"Cheng, Y.\"\n      - \"Metoyer, R.\"\n      - \"Hua, T.\"\n      - \"Chawla, N.V.\"\n    year: 2025\n    venue: \"arXiv\"\n    url: \"https://arxiv.org/abs/2511.04689\"\n    category: \"irt_benchmarking\"\n    role: \"method-component\"\n    relevance: \"Introduces ATLAS, an IRT-based computerized adaptive testing framework using Fisher information-guided item selection. Reduces required items by up to 90% while maintaining precision. Demonstrates CAT as a practical alternative to static benchmarks for LLM evaluation.\"\n    verified: true\n    added_by: \"worker\"\n    added_at: \"2026-05-21T16:00:00Z\""
  }
}
```

</details>

---

### Tool result

_source line 34 · 2026-05-21T18:58:00.223612+00:00_

The file /home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/literature_map.yaml has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_research_cluster4_irt_20260521T185524",
  "tool": "Edit",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 35 · 2026-05-21T18:58:00.223756+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "python3 -c \"import yaml; data = yaml.safe_load(open('/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/literature_map.yaml')); papers = data['papers']; cats = [c['key'] for c in data['categories']]; irt = [k for k,v in papers.items() if v.get('category')=='irt_benchmarking']; print(f'total_papers meta: {data[\\\"meta\\\"][\\\"total_papers\\\"]}'); print(f'actual papers: {len(papers)}'); print(f'categories: {cats}'); print(f'irt_benchmarking papers: {irt}')\"",
  "description": "Validate YAML structure and counts"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_research_cluster4_irt_20260521T185524",
  "tool": "Bash",
  "tool_args": {
    "command": "python3 -c \"import yaml; data = yaml.safe_load(open('/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/literature_map.yaml')); papers = data['papers']; cats = [c['key'] for c in data['categories']]; irt = [k for k,v in papers.items() if v.get('category')=='irt_benchmarking']; print(f'total_papers meta: {data[\\\"meta\\\"][\\\"total_papers\\\"]}'); print(f'actual papers: {len(papers)}'); print(f'categories: {cats}'); print(f'irt_benchmarking papers: {irt}')\"",
    "description": "Validate YAML structure and counts"
  }
}
```

</details>

---

### Tool result

_source line 36 · 2026-05-21T18:58:00.223896+00:00_

total_papers meta: 26
actual papers: 26
categories: ['gtheory_evaluation', 'infrastructure_variance', 'prompt_sensitivity', 'evaluation_methodology', 'irt_benchmarking']
irt_benchmarking papers: ['polo2024tinybenchmarks', 'lalor2019irt', 'rodriguez2021leaderboards', 'perlitz2023efficient', 'zhou2026irt', 'li2025atlas']

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_research_cluster4_irt_20260521T185524",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 37 · 2026-05-21T18:58:00.224045+00:00_

Cluster 4 完成。6 篇论文已添加到 `literature_map.yaml`，category `irt_benchmarking`，total_papers 更新为 26。

| key | paper | venue | role |
|-----|-------|-------|------|
| `polo2024tinybenchmarks` | tinyBenchmarks: evaluating LLMs with fewer examples | ICML 2024 | method-component |
| `lalor2019irt` | Learning Latent Parameters without Human Response Patterns: IRT with Artificial Crowds | EMNLP-IJCNLP 2019 | foundational |
| `rodriguez2021leaderboards` | Evaluation Examples are not Equally Informative | ACL 2021 | foundational |
| `perlitz2023efficient` | Efficient Benchmarking of Language Models | arXiv 2023 | method-component |
| `zhou2026irt` | Lost in Benchmarks? Rethinking LLM Benchmarking with IRT (PSN-IRT) | AAAI 2026 Oral | direct-competitor |
| `li2025atlas` | Adaptive Testing for LLM Evaluation (ATLAS) | arXiv 2025 | method-component |

注：Lalor 2019 实际发表于 EMNLP-IJCNLP 2019（非 NAACL）。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_paper_research_cluster4_irt_20260521T185524"
}
```

</details>

---
