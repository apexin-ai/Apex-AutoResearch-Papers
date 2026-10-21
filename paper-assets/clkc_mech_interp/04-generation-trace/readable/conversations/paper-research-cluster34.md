# paper research cluster34

**English-Chinese Knowledge Conflict Signals Are Consistent With General Cross-Lingual Asymmetries** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 41
- **Recorded user turns:** 0
- **Tool calls:** 20
- **Original source:** `logs/chats/worker_paper_research_cluster34_20260522T134427.jsonl`
- **Structured JSON:** [`661bad70c4e9842e052d.json`](../../sessions/66/661bad70c4e9842e052d.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

41 recorded events

### Tool call

_source line 1 · 2026-05-22T13:49:18.764519+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/literature_map.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_research_cluster34_20260522T134427",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/literature_map.yaml"
  }
}
```

</details>

---

### Tool result

_source line 2 · 2026-05-22T13:49:18.764983+00:00_

1	categories: []
2	meta:
3	  last_updated: '2026-05-22T14:00:00Z'
4	  total_papers: 15
5	papers:
6	  basu2026interpretability:
7	    abstract: ''
8	    added_at: '2026-05-21T12:04:50.273Z'
9	    added_by: director-bootstrap
10	    authors:
11	    - Basu, S.
12	    - et al.
13	    bibtex_key: basu2026interpretability
14	    category: sae-steering
15	    doi: ''
16	    relevance: 'SAE steering failure in clinical triage despite 98.2% AUROC probes.
17	      Critical negative result: defines boundary conditions for when SAE steering
18	      works. Our Track 3 design addresses their methodological gaps.'
19	    role: direct-competitor
20	    semantic_scholar_id: ''
21	    title: 'Interpretability without actionability: mechanistic methods cannot correct
22	      language model errors despite near-perfect internal representations'
23	    url: https://arxiv.org/abs/2603.18353
24	    venue: arXiv
25	    verified: true
26	    year: 2026
27	  boer2026probing:
28	    abstract: ''
29	    added_at: '2026-05-21T12:04:50.273Z'
30	    added_by: director-bootstrap
31	    authors:
32	    - Boer, A.
33	    - Brink, I.
34	    - Ulmer, D.
35	    bibtex_key: boer2026probing
36	    category: probing
37	    doi: ''
38	    relevance: 0.96 Macro-F1 parametric-vs-contextual attribution probe on Llama/Mistral/Qwen.
39	      Monolingual performance ceiling for our Track 1. Cross-domain transfer 0.94-0.99
40	      F1.
41	    role: direct-competitor
42	    semantic_scholar_id: ''
43	    title: Probing for Knowledge Attribution in Large Language Models
44	    url: https://arxiv.org/abs/2602.22787
45	    venue: arXiv
46	    verified: true
47	    year: 2026
48	  ifergan2024beneath:
49	    added_at: '2026-05-22T14:00:00Z'
50	    added_by: paper-agent-lit-search
51	    authors:
52	    - Ifergan, M.
53	    - Choshen, L.
54	    - Aharoni, R.
55	    - Szpektor, I.
56	    - Abend, O.
57	    bibtex_key: ifergan2024beneath
58	    category: cross-lingual-conflict
59	    doi: ''
60	    relevance: Shows cross
…[truncated 9685 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_research_cluster34_20260522T134427",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-22T13:49:18.765197+00:00_

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
  "session": "worker_paper_research_cluster34_20260522T134427",
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

_source line 4 · 2026-05-22T13:49:18.765338+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_research_cluster34_20260522T134427",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-22T13:49:18.765492+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Conneau et al 2020 \"Emerging Cross-lingual Structure in Pretrained Language Models\" ACL"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_research_cluster34_20260522T134427",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Conneau et al 2020 \"Emerging Cross-lingual Structure in Pretrained Language Models\" ACL"
  }
}
```

</details>

---

### Tool call

_source line 6 · 2026-05-22T13:49:18.765670+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Belinkov 2022 probing classifiers survey \"Probing Classifiers\" computational linguistics"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_research_cluster34_20260522T134427",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Belinkov 2022 probing classifiers survey \"Probing Classifiers\" computational linguistics"
  }
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-22T13:49:18.765817+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "cross-lingual representation alignment multilingual transformer CKA layer-wise analysis 2022 2023 2024"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_research_cluster34_20260522T134427",
  "tool": "WebSearch",
  "tool_args": {
    "query": "cross-lingual representation alignment multilingual transformer CKA layer-wise analysis 2022 2023 2024"
  }
}
```

</details>

---

### Tool call

_source line 8 · 2026-05-22T13:49:18.765979+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "English-centric bias multilingual language models representations 2023 2024"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_research_cluster34_20260522T134427",
  "tool": "WebSearch",
  "tool_args": {
    "query": "English-centric bias multilingual language models representations 2023 2024"
  }
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-22T13:49:18.766111+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "linear probe expressiveness limitations selectivity probing NLP 2020 2021 2022"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_research_cluster34_20260522T134427",
  "tool": "WebSearch",
  "tool_args": {
    "query": "linear probe expressiveness limitations selectivity probing NLP 2020 2021 2022"
  }
}
```

</details>

---

### Tool call

_source line 10 · 2026-05-22T13:49:18.766226+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "bootstrap confidence interval probing NLP statistical significance 2022 2023"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_research_cluster34_20260522T134427",
  "tool": "WebSearch",
  "tool_args": {
    "query": "bootstrap confidence interval probing NLP statistical significance 2022 2023"
  }
}
```

</details>

---

### Tool result

_source line 11 · 2026-05-22T13:49:18.766371+00:00_

Web search results for query: "Belinkov 2022 probing classifiers survey "Probing Classifiers" computational linguistics"

Links: [{"title":"Probing Classifiers: Promises, Shortcomings, and Advances | Computational Linguistics | MIT Press","url":"https://direct.mit.edu/coli/article/48/1/207/107571/Probing-Classifiers-Promises-Shortcomings-and"},{"title":"@article{belinkov-2022-probing,","url":"https://aclanthology.org/2022.cl-1.7.bib"},{"title":"[PDF] Probing Classifiers: Promises, Shortcomings, and Advances | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Probing-Classifiers:-Promises,-Shortcomings,-and-Belinkov/3dcfa05a1c162e6cab927c5b08d0444f7b6691f4"},{"title":"Probing Classifiers: Promises, Shortcomings, and Advances - ACL Anthology","url":"https://aclanthology.org/2022.cl-1.7/"},{"title":"Probing Classifiers: Promises, Shortcomings, and Advances - Technion - Israel Institute of Technology","url":"https://cris.technion.ac.il/en/publications/probing-classifiers-promises-shortcomings-and-advances/"},{"title":"Probing Classifiers: Promises, Shortcomings, and Advances - Israeli Research Community Portal","url":"https://cris.iucc.ac.il/en/publications/probing-classifiers-promises-shortcomings-and-advances/"},{"title":"Yonatan Belinkov | publications","url":"https://belinkov.com/publications/publicationstype/"},{"title":"[2102.12452] Probing Classifiers: Promises, Shortcomings, and Advances","url":"https://arxiv.org/abs/2102.12452"}]

I've found the paper you're looking for. Here are the key details:

**Title:** "Probing Classifiers: Promises, Shortcomings, and Advances"

**Author:** Yonatan Belinkov

**Publication:** Computational Linguistics, 48(1):207–219, 2022

**Overview:** Probing classifiers have emerged as one of the prominent methodologies for interpreting and analyzing deep neural network models of natural language processing. The basic idea is simple—a classifier is trained to predict some linguistic property from a model's representations—a
…[truncated 504 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_research_cluster34_20260522T134427",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-22T13:49:18.766548+00:00_

Web search results for query: "Conneau et al 2020 "Emerging Cross-lingual Structure in Pretrained Language Models" ACL"

Links: [{"title":"Emerging Cross-lingual Structure in Pretrained Language Models - ACL Anthology","url":"https://aclanthology.org/2020.acl-main.536/"},{"title":"Exploring the Data Efficiency of Cross-Lingual Post-Training in Pretrained Language Models","url":"https://www.mdpi.com/2076-3417/11/5/1974"},{"title":"GitHub - shijie-wu/crosslingual-nlp: This repo supports various cross-lingual transfer learning & multilingual NLP models. · GitHub","url":"https://github.com/shijie-wu/crosslingual-nlp"},{"title":"crosslingual-nlp/README.md at master · shijie-wu/crosslingual-nlp","url":"https://github.com/shijie-wu/crosslingual-nlp/blob/master/README.md"},{"title":"(PDF) Cross-lingual Language Model Pretraining for Retrieval","url":"https://www.researchgate.net/publication/352111504_Cross-lingual_Language_Model_Pretraining_for_Retrieval"},{"title":"Cross-lingual Language Model Pretraining for Retrieval | Proceedings of the Web Conference 2021","url":"https://dl.acm.org/doi/10.1145/3442381.3449830"},{"title":"ACL2020: Emerging Cross-lingual Structure in Pretrained Language Models","url":"https://virtual.acl2020.org/paper_main.536.html"},{"title":"[PDF] Emerging Cross-lingual Structure in Pretrained Language Models | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Emerging-Cross-lingual-Structure-in-Pretrained-Wu-Conneau/cfe8ec7a183ed548db1a862e38908343cefb94c7"},{"title":"[1911.01464] Emerging Cross-lingual Structure in Pretrained Language Models","url":"https://arxiv.org/abs/1911.01464"},{"title":"(PDF) Emerging Cross-lingual Structure in Pretrained Language Models","url":"https://www.researchgate.net/publication/337048070_Emerging_Cross-lingual_Structure_in_Pretrained_Language_Models"}]

Based on the search results, I found the paper you're looking for:

"Emerging Cross-lingual Structure in Pretrained Language Models" by Alexis Conneau, Shi
…[truncated 1062 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_research_cluster34_20260522T134427",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 13 · 2026-05-22T13:49:18.766725+00:00_

Web search results for query: "cross-lingual representation alignment multilingual transformer CKA layer-wise analysis 2022 2023 2024"

Links: [{"title":"Neither Here Nor There: Cross-Lingual Representation Dynamics of Code-Mixed Text in Multilingual Encoders","url":"https://arxiv.org/html/2603.19771"},{"title":"TRepLiNa: Layer-wise CKA+REPINA Alignment Improves Low-Resource Machine Translation in Aya-23 8B","url":"https://arxiv.org/pdf/2510.06249"},{"title":"MEXA: Multilingual Evaluation of English-Centric LLMs via Cross-Lingual Alignment | Request PDF","url":"https://www.researchgate.net/publication/394303914_MEXA_Multilingual_Evaluation_of_English-Centric_LLMs_via_Cross-Lingual_Alignment"},{"title":"Middle-Layer Representation Alignment for Cross-Lingual Transfer in Fine-Tuned LLMs","url":"https://arxiv.org/html/2502.14830v1"},{"title":"Cross-Lingual Continuous Pretraining","url":"https://www.emergentmind.com/topics/cross-lingual-continuous-pretraining"},{"title":"Cross-lingual Similarity of Multilingual Representations Revisited","url":"https://arxiv.org/pdf/2212.01924"},{"title":"Can you map it to English? The Role of Cross-Lingual Alignment in Multilingual Performance of LLMs","url":"https://arxiv.org/pdf/2504.09378"}]

I've successfully performed a web search for your query about cross-lingual representation alignment in multilingual transformers with CKA layer-wise analysis. Here's a summary of the relevant findings:

## Key Research Areas and Findings

**CKA for Cross-Lingual Analysis:**
CKA (Centered Kernel Alignment) and SVCCA are employed as complementary representation similarity measures to quantify layer-wise alignment between sentence representations across languages. CKA is invariant to isotropic scaling and orthogonal transformations, making it well-suited for comparing representations across layers, languages, and model architectures.

**Recent Applications (2024-2025):**
Recent work combines CKA with Representation Projection Invariance (REPINA),
…[truncated 995 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_research_cluster34_20260522T134427",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-22T13:49:18.766951+00:00_

Web search results for query: "bootstrap confidence interval probing NLP statistical significance 2022 2023"

Links: [{"title":"[2205.11134] Please, Don't Forget the Difference and the Confidence Interval when Seeking for the State-of-the-Art Status","url":"https://arxiv.org/abs/2205.11134"},{"title":"Please, Don't Forget the Difference and the Confidence Interval when   Seeking for the State-of-the-Art Status","url":"https://arxiv.org/pdf/2205.11134"},{"title":"(PDF) Confidence Intervals by Bootstrapping Approach: A Significance Review","url":"https://www.researchgate.net/publication/368809659_Confidence_Intervals_by_Bootstrapping_Approach_A_Significance_Review"},{"title":"Please, Don't Forget the Difference and the Confidence ...","url":"https://aclanthology.org/2022.lrec-1.640.pdf"},{"title":"Beyond statistical significance: Quantifying uncertainty and statistical variability in multilingual and multitask NLP evaluation","url":"https://arxiv.org/pdf/2509.22612"},{"title":"Appendix - Recommended Statistical Significance Tests for NLP Tasks","url":"https://arxiv.org/pdf/1809.01448"},{"title":"Using the bootstrap to establish statistical significance for relative validity comparisons among patient-reported outcome measures","url":"https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3681626/"}]

Based on the search results, I found several relevant resources on bootstrap confidence intervals, statistical significance, and NLP evaluation from 2022-2023:

**Key Finding:**

A 2022 paper argues for the widest possible use of bootstrap confidence intervals for comparing NLP system performances instead of the state-of-the-art status (SOTA) and statistical significance testing. The main benefits are to draw attention to the difference in performance between two systems and to help assess the degree of superiority of one system over another.

**Supporting Resources:**

- A python module for obtaining these confidence intervals as well as a function implementing the Fisher-Pitman te
…[truncated 602 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_research_cluster34_20260522T134427",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 15 · 2026-05-22T13:49:18.767154+00:00_

Web search results for query: "English-centric bias multilingual language models representations 2023 2024"

Links: [{"title":"Do Multilingual LLMs Think In English?","url":"https://arxiv.org/pdf/2502.15603"},{"title":"Cross-Language Bias Examination in Large Language Models Yuxuan Liang","url":"https://arxiv.org/pdf/2512.16029"},{"title":"PANGEA:AFULLY OPEN MULTILINGUAL MULTI","url":"https://proceedings.iclr.cc/paper_files/paper/2025/file/770b8cf7ef10b4aa7170d09b36b6bb6f-Paper-Conference.pdf"},{"title":"Beyond English-Centric LLMs: What Language Do Multilingual Language Models Think in?","url":"https://arxiv.org/html/2408.10811v1"},{"title":"MEXA: Multilingual Evaluation of English-Centric LLMs via ...","url":"https://arxiv.org/pdf/2410.05873"},{"title":"Tokenization and Representation Biases in Multilingual ...","url":"https://aclanthology.org/2025.emnlp-main.1224.pdf"},{"title":"What Language Do Non-English-Centric Large ...","url":"https://aclanthology.org/2025.findings-acl.1350.pdf"}]

I've found relevant research on English-centric bias in multilingual language models. Here are the key findings from recent 2023-2024 research:

## Performance and Fairness Issues

English-centric behavior of LLMs causes them to perform worse in other languages in downstream tasks and in fluency. Additionally, this impacts the fairness of these models—which currently exhibit cultural biases—and their robustness and reliability in diverse linguistic settings.

## Training Data Imbalances

Models suffer from English- and western-centric training and evaluation datasets, resulting in a lack of representation for the vast majority of the world's languages and diverse cultural contexts. Models predominately trained on such data exhibit diminished performance in multilingual settings with poor tokenization further leading to higher inference costs, generate outputs misaligned with the socio-cultural norms of underrepresented languages, and lack the ability to recognize objects from geo
…[truncated 784 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_research_cluster34_20260522T134427",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-22T13:49:18.767331+00:00_

Web search results for query: "linear probe expressiveness limitations selectivity probing NLP 2020 2021 2022"

Links: [{"title":"Linear Probes: Neural Network Diagnostics","url":"https://www.emergentmind.com/topics/linear-probes"},{"title":"Trustworthy AI: Validity, Fairness, Explainability, and Uncertainty Assessments: Explainability methods: Linear Probes","url":"https://carpentries-incubator.github.io/fair-explainable-ml/5c-probes.html"},{"title":"Probing for Labeled Dependency Trees","url":"https://arxiv.org/pdf/2203.12971"},{"title":"Designing and Interpreting Probes with Control Tasks John Hewitt","url":"https://nlp.stanford.edu/pubs/hewitt2019control.pdf"},{"title":"Probing Classifiers: Promises, Shortcomings, and Advances","url":"https://arxiv.org/pdf/2102.12452"},{"title":"Designing and Interpreting Probes with Control Tasks","url":"https://aclanthology.org/D19-1275.pdf"},{"title":"Probing Classifiers: Decoding What Language Models Learn - Interactive | Michael Brenndoerfer | Michael Brenndoerfer","url":"https://mbrenndoerfer.com/writing/probing-classifiers"},{"title":"Designing and Interpreting Probes · John Hewitt","url":"https://www.cs.columbia.edu/~johnhew/interpreting-probes.html"},{"title":"Linguistics Wisdom of NLP Models | Towards Data Science","url":"https://towardsdatascience.com/linguistics-wisdom-of-nlp-models-8c8554bc8c66/"},{"title":"Interventional Probing in High Dimensions: An NLI Case Study","url":"https://arxiv.org/pdf/2304.10346"}]

Based on the search results, here's what I found regarding linear probe expressiveness limitations and selectivity probing in NLP:

## Key Findings on Linear Probes and Selectivity

Linear probes tend to have high selectivity, while non-linear probes tend to have low selectivity. This is a crucial distinction in probing methodology. Linear probes reveal only linearly accessible structure; non-linear phenomena remain invisible unless more expressive probes are used, though these introduce interpretability trad
…[truncated 1317 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_research_cluster34_20260522T134427",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-22T13:49:18.767522+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Wendler et al 2024 \"Do Multilingual LLMs Think in English\" arxiv multilingual internal representations pivot"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_research_cluster34_20260522T134427",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Wendler et al 2024 \"Do Multilingual LLMs Think in English\" arxiv multilingual internal representations pivot"
  }
}
```

</details>

---

### Tool call

_source line 18 · 2026-05-22T13:49:18.767651+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Hewitt Liang 2019 \"Designing and Interpreting Probes with Control Tasks\" EMNLP selectivity"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_research_cluster34_20260522T134427",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Hewitt Liang 2019 \"Designing and Interpreting Probes with Control Tasks\" EMNLP selectivity"
  }
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-22T13:49:18.767768+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "MEXA \"Multilingual Evaluation of English-Centric LLMs via Cross-Lingual Alignment\" 2024 arxiv"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_research_cluster34_20260522T134427",
  "tool": "WebSearch",
  "tool_args": {
    "query": "MEXA \"Multilingual Evaluation of English-Centric LLMs via Cross-Lingual Alignment\" 2024 arxiv"
  }
}
```

</details>

---

### Tool call

_source line 20 · 2026-05-22T13:49:18.767925+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Muller et al \"cross-lingual alignment multilingual BERT representations\" 2021 2022 layer CKA probing"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_research_cluster34_20260522T134427",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Muller et al \"cross-lingual alignment multilingual BERT representations\" 2021 2022 layer CKA probing"
  }
}
```

</details>

---

### Tool result

_source line 21 · 2026-05-22T13:49:18.768108+00:00_

Web search results for query: "Hewitt Liang 2019 "Designing and Interpreting Probes with Control Tasks" EMNLP selectivity"

Links: [{"title":"Designing and Interpreting Probes with Control Tasks - ACL Anthology","url":"https://aclanthology.org/D19-1275/"},{"title":"Designing and Interpreting Probes with Control Tasks","url":"https://bibbase.org/network/publication/hewitt-liang-designingandinterpretingprobeswithcontroltasks-2019"},{"title":"Designing and Interpreting Probes with Control Tasks | papers_we_read","url":"https://vlgiitr.github.io/papers_we_read/summaries/control_tasks.html"},{"title":"Designing and Interpreting Probes · John Hewitt","url":"https://www.cs.columbia.edu/~johnhew/interpreting-probes.html"},{"title":"[1909.03368] Designing and Interpreting Probes with Control Tasks","url":"https://arxiv.org/abs/1909.03368"},{"title":"Designing and Interpreting Probes with Control Tasks","url":"https://www.researchgate.net/publication/335713697_Designing_and_Interpreting_Probes_with_Control_Tasks"},{"title":"Designing and Interpreting Probes with Control Tasks","url":"https://arxiv.org/pdf/1909.03368"},{"title":"[PDF] Designing and Interpreting Probes with Control Tasks | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Designing-and-Interpreting-Probes-with-Control-Hewitt-Liang/199ff73d2f728e997f860b62a2322823d3e3d9e8"},{"title":"Designing and Interpreting Probes with Control Tasks","url":"https://aclanthology.org/D19-1275.pdf"},{"title":"Designing and Interpreting Probes with Control Tasks John Hewitt","url":"https://nlp.stanford.edu/pubs/hewitt2019control.pdf"}]

I found the paper! Here's what the search results show:

"Designing and Interpreting Probes with Control Tasks" was published in the Proceedings of the 2019 Conference on Empirical Methods in Natural Language Processing and the 9th International Joint Conference on Natural Language Processing (EMNLP-IJCNLP) by John Hewitt and Percy Liang, with pages 2733–2743.

The paper received the 
…[truncated 714 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_research_cluster34_20260522T134427",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 22 · 2026-05-22T13:49:18.768290+00:00_

Web search results for query: "Wendler et al 2024 "Do Multilingual LLMs Think in English" arxiv multilingual internal representations pivot"

Links: [{"title":"Improving Multilingual Language Models by Aligning Representations through Steering","url":"https://arxiv.org/html/2505.12584v1"},{"title":"arXiv:2506.09890v1 [cs.CL] 11 Jun 2025","url":"https://www.arxiv.org/pdf/2506.09890"},{"title":"MEXA: Multilingual Evaluation of English-Centric LLMs via ...","url":"https://arxiv.org/pdf/2410.05873"},{"title":"Quantifying Multilingual Performance of Large Language Models Across Languages","url":"https://arxiv.org/html/2404.11553v2"},{"title":"Do Multilingual LLMs Think In English?","url":"https://arxiv.org/html/2502.15603v1"},{"title":"Can you map it to English? The Role of Cross-Lingual Alignment in Multilingual Performance of LLMs","url":"https://arxiv.org/html/2504.09378v1"},{"title":"Do Large Language Models Have an English “Accent”? Evaluating and Improving the Naturalness of Multilingual LLMs","url":"https://arxiv.org/html/2410.15956"},{"title":"Lens: Rethinking Multilingual Enhancement for Large Language Models","url":"https://arxiv.org/html/2410.04407v1"},{"title":"Continually Adding New Languages to Multilingual Language Models","url":"https://arxiv.org/html/2509.11414v1"},{"title":"GitHub - tjunlp-lab/Awesome-Multilingual-LLMs-Papers: Awesome-Multilingual-LLMs-Papers · GitHub","url":"https://github.com/tjunlp-lab/Awesome-Multilingual-LLMs-Papers"}]

Based on the search results, I found the paper you're looking for:

The paper by Wendler et al. (2024) is titled "Do llamas work in English? On the latent language of multilingual transformers" and was published in the Proceedings of the 62nd Annual Meeting of the Association for Computational Linguistics in August 2024.

The key findings of this research include:

1. **English as an internal pivot language**: Wendler et al. (2024) found that for Llama 2, an English-centric LLM, English could be seen as a kind of "p
…[truncated 925 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_research_cluster34_20260522T134427",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 23 · 2026-05-22T13:49:18.768468+00:00_

Web search results for query: "MEXA "Multilingual Evaluation of English-Centric LLMs via Cross-Lingual Alignment" 2024 arxiv"

Links: [{"title":"[Literature Review] MEXA: Multilingual Evaluation of English-Centric LLMs via Cross-Lingual Alignment","url":"https://www.themoonlight.io/en/review/mexa-multilingual-evaluation-of-english-centric-llms-via-cross-lingual-alignment"},{"title":"Mexa: Multilingual Evaluation of English-Centric LLMs via Cross-Lingual Alignment | OpenReview","url":"https://openreview.net/forum?id=hsMkpzr9Oy"},{"title":"GitHub - cisnlp/MEXA: 🔍 Multilingual Evaluation of English-Centric LLMs via Cross-Lingual Alignment","url":"https://github.com/cisnlp/MEXA"},{"title":"Paper page - MEXA: Multilingual Evaluation of English-Centric LLMs via Cross-Lingual Alignment","url":"https://huggingface.co/papers/2410.05873"},{"title":"MEXA: Multilingual Evaluation of English-Centric LLMs via Cross-Lingual Alignment_国家预印本平台","url":"https://sinoxiv.napstic.cn/article/10967125"},{"title":"[2410.05873] MEXA: Multilingual Evaluation of English-Centric LLMs via Cross-Lingual Alignment","url":"https://arxiv.org/abs/2410.05873"},{"title":"(PDF) MEXA: Multilingual Evaluation of English-Centric LLMs via Cross-Lingual Alignment","url":"https://www.researchgate.net/publication/384771337_MEXA_Multilingual_Evaluation_of_English-Centric_LLMs_via_Cross-Lingual_Alignment"},{"title":"Mexa: Multilingual Evaluation of English-Centric LLMs via Cross-Lingual Alignment","url":"https://arxiv.org/html/2410.05873v1"},{"title":"Can you map it to English? The Role of Cross-Lingual Alignment in Multilingual Performance of LLMs","url":"https://arxiv.org/html/2504.09378v1"},{"title":"MEXA: Multilingual Evaluation of English-Centric LLMs via ...","url":"https://arxiv.org/pdf/2410.05873"}]

Based on the search results, here's information about the MEXA paper:

## Overview

MEXA is a method for assessing the multilingual capabilities of pre-trained English-centric LLMs using parallel sentences, 
…[truncated 1013 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_research_cluster34_20260522T134427",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 24 · 2026-05-22T13:49:18.768647+00:00_

Web search results for query: "Muller et al "cross-lingual alignment multilingual BERT representations" 2021 2022 layer CKA probing"

Links: [{"title":"First Align, then Predict: Understanding the Cross-Lingual Ability of Multilingual BERT | Request PDF","url":"https://www.researchgate.net/publication/355434439_First_Align_then_Predict_Understanding_the_Cross-Lingual_Ability_of_Multilingual_BERT"},{"title":"(PDF) Cross-lingual Similarity of Multilingual Representations Revisited","url":"https://www.researchgate.net/publication/366027168_Cross-lingual_Similarity_of_Multilingual_Representations_Revisited"},{"title":"First Align, then Predict: Understanding the Cross-Lingual Ability of Multilingual BERT | Paper to HTML | Allen Institute for AI","url":"https://a11y2.apps.allenai.org/paper?id=1cfd0f08bb7ab449bbccc3d69a62ffbf43a7eb7f"},{"title":"Probing the Emergence of Cross-lingual Alignment during LLM Training","url":"https://arxiv.org/html/2406.13229v1"},{"title":"[2101.11109] First Align, then Predict: Understanding the Cross-Lingual Ability of Multilingual BERT","url":"https://arxiv.org/abs/2101.11109"},{"title":"Cross-lingual Similarity of Multilingual Representations Revisited","url":"https://arxiv.org/pdf/2212.01924"},{"title":"Probing Multilingual Sentence Representations With X-Probe","url":"https://arxiv.org/pdf/1906.05061"}]

The search has returned results related to the Muller et al. work on cross-lingual alignment in multilingual BERT. Here's what I found:

The key paper is "First Align, then Predict: Understanding the Cross-Lingual Ability of Multilingual BERT" by Benjamin Muller, Yanai Elazar, Benoît Sagot, and Djamé Seddah (2021).

The research focuses on understanding how multilingual BERT achieves zero-shot cross-lingual transfer. Using CKA and behavior analysis, Muller et al. (2021) demonstrated that language representations align with network depth, and representations first converge towards language neutrality and then recover some language-specifi
…[truncated 618 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_research_cluster34_20260522T134427",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 25 · 2026-05-22T13:49:18.768917+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Wendler Veselovsky Flagg Alam West 2024 \"Do Llamas Work in English\" latent language multilingual transformers ACL arxiv"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_research_cluster34_20260522T134427",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Wendler Veselovsky Flagg Alam West 2024 \"Do Llamas Work in English\" latent language multilingual transformers ACL arxiv"
  }
}
```

</details>

---

### Tool call

_source line 26 · 2026-05-22T13:49:18.769058+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Ulmer et al 2022 \"deep-significance\" bootstrap statistical testing NLP probing confidence interval arxiv"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_research_cluster34_20260522T134427",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Ulmer et al 2022 \"deep-significance\" bootstrap statistical testing NLP probing confidence interval arxiv"
  }
}
```

</details>

---

### Tool result

_source line 27 · 2026-05-22T13:49:18.769207+00:00_

Web search results for query: "Ulmer et al 2022 "deep-significance" bootstrap statistical testing NLP probing confidence interval arxiv"

Links: [{"title":"deep-significance: Easy and Better Significance Testing for Deep Neural Networks — deep-significance 1.2.5 documentation","url":"https://deep-significance.readthedocs.io/"},{"title":"[PDF] deep-significance - Easy and Meaningful Statistical Significance Testing in the Age of Neural Networks | Semantic Scholar","url":"https://www.semanticscholar.org/paper/deep-significance-Easy-and-Meaningful-Statistical-Ulmer-Hardmeier/bcef143c672029431c316fe40235671879827aa7"},{"title":"(PDF) deep-significance - Easy and Meaningful Statistical Significance Testing in the Age of Neural Networks","url":"https://www.researchgate.net/publication/359971291_deep-significance_-_Easy_and_Meaningful_Statistical_Significance_Testing_in_the_Age_of_Neural_Networks"},{"title":"GitHub - Kaleidophon/deep-significance: Enabling easy statistical significance testing for deep neural networks. · GitHub","url":"https://github.com/Kaleidophon/deep-significance"},{"title":"[2204.06815v1] deep-significance - Easy and Meaningful Statistical Significance Testing in the Age of Neural Networks","url":"https://arxiv.org/abs/2204.06815v1"},{"title":"Predicting Fine-Tuning Performance with Probing","url":"https://arxiv.org/pdf/2210.07352"},{"title":"Statistical Significance Tests in NLP | by Sudhanva Savyasachi S | Medium","url":"https://sudhanvaiitr.medium.com/statistical-significance-tests-in-nlp-313ad69cc57a"},{"title":"Please, Don't Forget the Difference and the Confidence Interval when   Seeking for the State-of-the-Art Status","url":"https://arxiv.org/pdf/2205.11134"}]

Based on the search results, I found the relevant paper:

The paper "deep-significance - Easy and Meaningful Statistical Significance Testing in the Age of Neural Networks" was authored by Dennis Ulmer, Christian Hardmeier, and Jes Frellsen and published on arXiv in 2022 (arxiv:2204.068
…[truncated 660 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_research_cluster34_20260522T134427",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 28 · 2026-05-22T13:49:18.769377+00:00_

Web search results for query: "Wendler Veselovsky Flagg Alam West 2024 "Do Llamas Work in English" latent language multilingual transformers ACL arxiv"

Links: [{"title":"Do Llamas Work in English? On the Latent Language of Multilingual Transformers - ACL Anthology","url":"https://aclanthology.org/2024.acl-long.820/"},{"title":"[PDF] Do Llamas Work in English? On the Latent Language of Multilingual Transformers | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Do-Llamas-Work-in-English-On-the-Latent-Language-of-Wendler-Veselovsky/e88efdfc05d0d8832b2ded7af9c8ececdd03e58d"},{"title":"Do Llamas Work in English? On the Latent Language of Multilingual Transformers | Artificial Intelligence Hub","url":"https://aicitta.com/posts/do-llamas-work-in-english/"},{"title":"Do Llamas Work in English? On the Latent Language of Multilingual Transformers - Consensus","url":"https://consensus.app/papers/details/b8aa720cd459550191960afe5413d726/"},{"title":"[2402.10588] Do Llamas Work in English? On the Latent Language of Multilingual Transformers","url":"https://arxiv.org/abs/2402.10588"},{"title":"Do Llamas Work in English? On the Latent Language of Multilingual   Transformers","url":"https://arxiv.org/pdf/2402.10588"},{"title":"Do Llamas Work in English? On the Latent Language of Multilingual Transformers - Paper Detail","url":"https://deeplearn.org/arxiv/459055/do-llamas-work-in-english"},{"title":"[2402.10588] Do Llamas Work in English? On the Latent Language of Multilingual Transformers","url":"https://ar5iv.labs.arxiv.org/html/2402.10588"},{"title":"dblp: Do Llamas Work in English? On the Latent Language of Multilingual Transformers.","url":"https://dblp.org/rec/journals/corr/abs-2402-10588.html"}]

I found the paper you're looking for! Here's the information:

"Do Llamas Work in English? On the Latent Language of Multilingual Transformers" was published by Wendler, Veselovsky, Giovanni Monea, and Robert West at ACL 2024. The paper is available as arXiv preprint 
…[truncated 901 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_research_cluster34_20260522T134427",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 29 · 2026-05-22T13:49:18.769578+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Muller Elazar Sagot Seddah 2021 \"First Align then Predict\" EACL arxiv:2101.11109 venue"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_research_cluster34_20260522T134427",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Muller Elazar Sagot Seddah 2021 \"First Align then Predict\" EACL arxiv:2101.11109 venue"
  }
}
```

</details>

---

### Tool call

_source line 30 · 2026-05-22T13:49:18.769708+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Kargaran Modarressi \"MEXA\" 2024 2025 venue EMNLP NAACL accepted conference"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_research_cluster34_20260522T134427",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Kargaran Modarressi \"MEXA\" 2024 2025 venue EMNLP NAACL accepted conference"
  }
}
```

</details>

---

### Tool result

_source line 31 · 2026-05-22T13:49:18.769869+00:00_

Web search results for query: "Muller Elazar Sagot Seddah 2021 "First Align then Predict" EACL arxiv:2101.11109 venue"

Links: [{"title":"Main Conference Accepted Papers - EACL 2021","url":"https://2021.eacl.org/program/accepted/"},{"title":"First Align, then Predict: Understanding the Cross-Lingual Ability of Multilingual BERT - ACL Anthology","url":"https://aclanthology.org/2021.eacl-main.189/"},{"title":"First Align, then Predict: Understanding the Cross-Lingual Ability of Multilingual BERT - Inria - Institut national de recherche en sciences et technologies du numérique","url":"https://inria.hal.science/hal-03239087"},{"title":"GitHub - benjamin-mlr/first-align-then-predict · GitHub","url":"https://github.com/benjamin-mlr/first-align-then-predict"},{"title":"First Align, then Predict: Understanding the Cross-Lingual Ability of Multilingual BERT | Request PDF","url":"https://www.researchgate.net/publication/355434439_First_Align_then_Predict_Understanding_the_Cross-Lingual_Ability_of_Multilingual_BERT"},{"title":"[PDF] First Align, then Predict: Understanding the Cross-Lingual Ability of Multilingual BERT | Semantic Scholar","url":"https://www.semanticscholar.org/paper/First-Align,-then-Predict:-Understanding-the-of-Muller-Elazar/1cfd0f08bb7ab449bbccc3d69a62ffbf43a7eb7f"},{"title":"Figure 5 from First Align, then Predict: Understanding the Cross-Lingual Ability of Multilingual BERT | Semantic Scholar","url":"https://www.semanticscholar.org/paper/First-Align,-then-Predict:-Understanding-the-of-Muller-Elazar/1cfd0f08bb7ab449bbccc3d69a62ffbf43a7eb7f/figure/9"},{"title":"[2101.11109] First Align, then Predict: Understanding the Cross-Lingual Ability of Multilingual BERT","url":"https://arxiv.org/abs/2101.11109"},{"title":"First Align, then Predict: Understanding the Cross-Lingual Ability of Multilingual BERT - ADS","url":"https://ui.adsabs.harvard.edu/abs/2021arXiv210111109M/abstract"}]

Based on the search results, I found comprehensive information about this paper:
…[truncated 965 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_research_cluster34_20260522T134427",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 32 · 2026-05-22T13:49:18.770046+00:00_

Web search results for query: "Kargaran Modarressi "MEXA" 2024 2025 venue EMNLP NAACL accepted conference"

Links: [{"title":"[Quick Review] MEXA: Multilingual Evaluation of English-Centric LLMs via Cross-Lingual Alignment","url":"https://liner.com/review/mexa-multilingual-evaluation-englishcentric-llms-via-crosslingual-alignment"},{"title":"GitHub - cisnlp/MEXA: 🔍 Multilingual Evaluation of English-Centric LLMs via Cross-Lingual Alignment","url":"https://github.com/cisnlp/MEXA"},{"title":"MEXA: Multilingual Evaluation of English-Centric LLMs via Cross-Lingual Alignment - ACL Anthology","url":"https://aclanthology.org/2025.findings-acl.1385/"},{"title":"publications | Amir Hossein Kargaran","url":"https://kargaranamir.github.io/publications/"},{"title":"MEXA: Multilingual Evaluation of English-Centric LLMs via Cross-Lingual Alignment | Request PDF","url":"https://www.researchgate.net/publication/394303914_MEXA_Multilingual_Evaluation_of_English-Centric_LLMs_via_Cross-Lingual_Alignment"},{"title":"MEXA: Multilingual Evaluation of English-Centric LLMs via ...","url":"https://arxiv.org/pdf/2410.05873"},{"title":"[2410.05873] MEXA: Multilingual Evaluation of English-Centric LLMs via Cross-Lingual Alignment","url":"https://arxiv.org/abs/2410.05873"},{"title":"(PDF) MEXA: Multilingual Evaluation of English-Centric LLMs via Cross-Lingual Alignment","url":"https://www.researchgate.net/publication/384771337_MEXA_Multilingual_Evaluation_of_English-Centric_LLMs_via_Cross-Lingual_Alignment"}]

Based on the search results, here's what I found about the MEXA paper by Kargaran and Modarressi:

The MEXA paper by Kargaran et al. (including Ali Modarressi) was accepted to the Findings of the Association for Computational Linguistics: ACL 2025, with the conference held in Vienna, Austria.

The paper is titled "MEXA: Multilingual Evaluation of English-Centric LLMs via Cross-Lingual Alignment."

The paper introduces MEXA, a method for assessing the multilingual capabilities of pre-train
…[truncated 338 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_research_cluster34_20260522T134427",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 33 · 2026-05-22T13:49:18.770257+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "site:aclanthology.org \"2020.acl-main.536\" \"Emerging Cross-lingual Structure\" authors"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_research_cluster34_20260522T134427",
  "tool": "WebSearch",
  "tool_args": {
    "query": "site:aclanthology.org \"2020.acl-main.536\" \"Emerging Cross-lingual Structure\" authors"
  }
}
```

</details>

---

### Tool result

_source line 34 · 2026-05-22T13:49:18.770397+00:00_

Web search results for query: "site:aclanthology.org "2020.acl-main.536" "Emerging Cross-lingual Structure" authors"

Links: [{"title":"Emerging Cross-lingual Structure in Pretrained Language Models - ACL Anthology","url":"https://aclanthology.org/2020.acl-main.536/"},{"title":"Emerging Cross-lingual Structure in Pretrained Language Models","url":"https://arxiv.org/pdf/1911.01464"},{"title":"Addressing Issues of Cross-Linguality in Open-Retrieval Question   Answering Systems For Emergent Domains","url":"https://arxiv.org/pdf/2201.11153"},{"title":"Cross-Lingual Ability of Multilingual Masked Language Models: A Study of   Language Structure","url":"https://arxiv.org/pdf/2203.08430"},{"title":"Crosslingual Structural Priming and the Pre-Training Dynamics of   Bilingual Language Models","url":"https://arxiv.org/pdf/2310.07929"}]

Based on the search results, I found the paper you're looking for. The authors of "Emerging Cross-lingual Structure in Pretrained Language Models" are Shijie Wu, Alexis Conneau, Haoran Li, Luke Zettlemoyer, and Veselin Stoyanov. 

Shijie Wu is from the Department of Computer Science at Johns Hopkins University, while Alexis Conneau, Haoran Li, Luke Zettlemoyer, and Veselin Stoyanov are from Facebook AI.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_research_cluster34_20260522T134427",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 35 · 2026-05-22T13:49:18.770590+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/literature_map.yaml",
  "old_string": "meta:\n  last_updated: '2026-05-22T14:00:00Z'\n  total_papers: 15",
  "new_string": "meta:\n  last_updated: '2026-05-22T14:30:00Z'\n  total_papers: 22"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_research_cluster34_20260522T134427",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/literature_map.yaml",
    "old_string": "meta:\n  last_updated: '2026-05-22T14:00:00Z'\n  total_papers: 15",
    "new_string": "meta:\n  last_updated: '2026-05-22T14:30:00Z'\n  total_papers: 22"
  }
}
```

</details>

---

### Tool result

_source line 36 · 2026-05-22T13:49:18.770751+00:00_

The file /home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/literature_map.yaml has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_research_cluster34_20260522T134427",
  "tool": "Edit",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 37 · 2026-05-22T13:49:18.770915+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/literature_map.yaml",
  "old_string": "    title: 'When Abundance Conceals Weakness: Knowledge Conflict in Multilingual Models'\n    url: https://arxiv.org/abs/2601.07041\n    venue: arXiv\n    verified: true\n    year: 2026",
  "new_string": "    title: 'When Abundance Conceals Weakness: Knowledge Conflict in Multilingual Models'\n    url: https://arxiv.org/abs/2601.07041\n    venue: arXiv\n    verified: true\n    year: 2026\n  wu2020emerging:\n    added_at: '2026-05-22T14:30:00Z'\n    added_by: paper-agent-lit-search\n    authors:\n    - Wu, S.\n    - Conneau, A.\n    - Li, H.\n    - Zettlemoyer, L.\n    - Stoyanov, V.\n    bibtex_key: wu2020emerging\n    category: cross-lingual-repr\n    doi: 10.18653/v1/2020.acl-main.536\n    relevance: Shows mid-layer cross-lingual alignment emerges from shared parameters\n      alone; monolingual representations can be aligned post-hoc. Foundation for understanding\n      language-agnostic concept space our probing hypotheses build on. MUST CITE.\n    role: foundation\n    title: Emerging Cross-lingual Structure in Pretrained Language Models\n    url: https://aclanthology.org/2020.acl-main.536/\n    venue: ACL 2020\n    verified: true\n    year: 2020\n  wendler2024llamas:\n    added_at: '2026-05-22T14:30:00Z'\n    added_by: paper-agent-lit-search\n    authors:\n    - Wendler, C.\n    - Veselovsky, V.\n    - Monea, G.\n    - West, R.\n    bibtex_key: wendler2024llamas\n    category: cross-lingual-repr\n    doi: ''\n    relevance: Demonstrates English-centric LLMs implicitly pivot through English representations\n      in middle layers. Three-phase pattern (input language -> English pivot -> output\n      language) supports hypothesis that conflict signals may route through English-aligned\n      subspace.\n    role: foundation\n    title: 'Do Llamas Work in English? On the Latent Language of Multilingual Transformers'\n    url: https://arxiv.org/abs/2402.10588\n    venue: ACL 2024\n    verified: true\n    year: 2024\n  muller2021first:\n    added_at: '2026-05-22T14:30:00Z'\n    added_by: paper-agent-lit-search\n    authors:\n    - Muller, B.\n    - Elazar, Y.\n    - Sagot, B.\n    - Seddah, D.\n    bibtex_key: muller2021first\n    category: cross-lingual-repr\n    doi: ''\n    relevance: CKA-based layer-wise analysis showing mBERT decomposes into multilingual\n      encoder + language-agnostic predictor. Representations first converge to language\n      neutrality then recover language specificity. Methodological precedent for our\n      layer-wise analysis.\n    role: methodology\n    title: 'First Align, then Predict: Understanding the Cross-Lingual Ability of Multilingual\n      BERT'\n    url: https://aclanthology.org/2021.eacl-main.189/\n    venue: EACL 2021\n    verified: true\n    year: 2021\n  kargaran2024mexa:\n    added_at: '2026-05-22T14:30:00Z'\n    added_by: paper-agent-lit-search\n    authors:\n    - Kargaran, A.H.\n    - Modarressi, A.\n    - Nikeghbal, N.\n    - Diesner, J.\n    - Yvon, F.\n    - \"Sch\\xFCtze, H.\"\n    bibtex_key: kargaran2024mexa\n    category: cross-lingual-repr\n    doi: ''\n    relevance: Cross-lingual alignment metric leveraging English pivot hypothesis, 0.90\n      Pearson correlation with downstream tasks. Provides evaluation methodology for\n      measuring English-centric alignment relevant to our cross-lingual transfer analysis.\n    role: methodology\n    title: 'MEXA: Multilingual Evaluation of English-Centric LLMs via Cross-Lingual\n      Alignment'\n    url: https://arxiv.org/abs/2410.05873\n    venue: Findings of ACL 2025\n    verified: true\n    year: 2024\n  belinkov2022probing:\n    added_at: '2026-05-22T14:30:00Z'\n    added_by: paper-agent-lit-search\n    authors:\n    - Belinkov, Y.\n    bibtex_key: belinkov2022probing\n    category: probing-methodology\n    doi: ''\n    relevance: Comprehensive survey of probing classifier promises, shortcomings, and\n      advances. Defines the methodological framework our linear probes follow. MUST\n      CITE for probing methodology justification.\n    role: foundation\n    title: 'Probing Classifiers: Promises, Shortcomings, and Advances'\n    url: https://arxiv.org/abs/2102.12452\n    venue: Computational Linguistics 48(1)\n    verified: true\n    year: 2022\n  hewitt2019designing:\n    added_at: '2026-05-22T14:30:00Z'\n    added_by: paper-agent-lit-search\n    authors:\n    - Hewitt, J.\n    - Liang, P.\n    bibtex_key: hewitt2019designing\n    category: probing-methodology\n    doi: ''\n    relevance: Introduces selectivity metric (linguistic accuracy - control accuracy)\n      to distinguish genuine representation encoding from probe memorization. Our probing\n      design uses control tasks following this framework. EMNLP 2019 Best Paper Runner\n      Up.\n    role: methodology\n    title: Designing and Interpreting Probes with Control Tasks\n    url: https://aclanthology.org/D19-1275/\n    venue: EMNLP 2019\n    verified: true\n    year: 2019\n  ulmer2022deep:\n    added_at: '2026-05-22T14:30:00Z'\n    added_by: paper-agent-lit-search\n    authors:\n    - Ulmer, D.\n    - Hardmeier, C.\n    - Frellsen, J.\n    bibtex_key: ulmer2022deep\n    category: probing-methodology\n    doi: ''\n    relevance: Bootstrap-based statistical testing framework for neural network comparisons,\n      including Almost Stochastic Order (ASO). Provides the bootstrap CI methodology\n      we use for probing accuracy significance testing.\n    role: methodology\n    title: 'deep-significance: Easy and Meaningful Statistical Significance Testing\n      in the Age of Neural Networks'\n    url: https://arxiv.org/abs/2204.06815\n    venue: arXiv\n    verified: true\n    year: 2022"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_research_cluster34_20260522T134427",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/literature_map.yaml",
    "old_string": "    title: 'When Abundance Conceals Weakness: Knowledge Conflict in Multilingual Models'\n    url: https://arxiv.org/abs/2601.07041\n    venue: arXiv\n    verified: true\n    year: 2026",
    "new_string": "    title: 'When Abundance Conceals Weakness: Knowledge Conflict in Multilingual Models'\n    url: https://arxiv.org/abs/2601.07041\n    venue: arXiv\n    verified: true\n    year: 2026\n  wu2020emerging:\n    added_at: '2026-05-22T14:30:00Z'\n    added_by: paper-agent-lit-search\n    authors:\n    - Wu, S.\n    - Conneau, A.\n    - Li, H.\n    - Zettlemoyer, L.\n    - Stoyanov, V.\n    bibtex_key: wu2020emerging\n    category: cross-lingual-repr\n    doi: 10.18653/v1/2020.acl-main.536\n    relevance: Shows mid-layer cross-lingual alignment emerges from shared parameters\n      alone; monolingual representations can be aligned post-hoc. Foundation for understanding\n      language-agnostic concept space our probing hypotheses build on. MUST CITE.\n    role: foundation\n    title: Emerging Cross-lingual Structure in Pretrained Language Models\n    url: https://aclanthology.org/2020.acl-main.536/\n    venue: ACL 2020\n    verified: true\n    year: 2020\n  wendler2024llamas:\n    added_at: '2026-05-22T14:30:00Z'\n    added_by: paper-agent-lit-search\n    authors:\n    - Wendler, C.\n    - Veselovsky, V.\n    - Monea, G.\n    - West, R.\n    bibtex_key: wendler2024llamas\n    category: cross-lingual-repr\n    doi: ''\n    relevance: Demonstrates English-centric LLMs implicitly pivot through English representations\n      in middle layers. Three-phase pattern (input language -> English pivot -> output\n      language) supports hypothesis that conflict signals may route through English-aligned\n      subspace.\n    role: foundation\n    title: 'Do Llamas Work in English? On the Latent Language of Multilingual Transformers'\n    url: https://arxiv.org/abs/2402.10588\n    venue: ACL 2024\n    verified: true\n    year: 2024\n  muller2021first:\n    added_at: '2026-05-22T14:30:00Z'\n    added_by: paper-agent-lit-search\n    authors:\n    - Muller, B.\n    - Elazar, Y.\n    - Sagot, B.\n    - Seddah, D.\n    bibtex_key: muller2021first\n    category: cross-lingual-repr\n    doi: ''\n    relevance: CKA-based layer-wise analysis showing mBERT decomposes into multilingual\n      encoder + language-agnostic predictor. Representations first converge to language\n      neutrality then recover language specificity. Methodological precedent for our\n      layer-wise analysis.\n    role: methodology\n    title: 'First Align, then Predict: Understanding the Cross-Lingual Ability of Multilingual\n      BERT'\n    url: https://aclanthology.org/2021.eacl-main.189/\n    venue: EACL 2021\n    verified: true\n    year: 2021\n  kargaran2024mexa:\n    added_at: '2026-05-22T14:30:00Z'\n    added_by: paper-agent-lit-search\n    authors:\n    - Kargaran, A.H.\n    - Modarressi, A.\n    - Nikeghbal, N.\n    - Diesner, J.\n    - Yvon, F.\n    - \"Sch\\xFCtze, H.\"\n    bibtex_key: kargaran2024mexa\n    category: cross-lingual-repr\n    doi: ''\n    relevance: Cross-lingual alignment metric leveraging English pivot hypothesis, 0.90\n      Pearson correlation with downstream tasks. Provides evaluation methodology for\n      measuring English-centric alignment relevant to our cross-lingual transfer analysis.\n    role: methodology\n    title: 'MEXA: Multilingual Evaluation of English-Centric LLMs via Cross-Lingual\n      Alignment'\n    url: https://arxiv.org/abs/2410.05873\n    venue: Findings of ACL 2025\n    verified: true\n    year: 2024\n  belinkov2022probing:\n    added_at: '2026-05-22T14:30:00Z'\n    added_by: paper-agent-lit-search\n    authors:\n    - Belinkov, Y.\n    bibtex_key: belinkov2022probing\n    category: probing-methodology\n    doi: ''\n    relevance: Comprehensive survey of probing classifier promises, shortcomings, and\n      advances. Defines the methodological framework our linear probes follow. MUST\n      CITE for probing methodology justification.\n    role: foundation\n    title: 'Probing Classifiers: Promises, Shortcomings, and Advances'\n    url: https://arxiv.org/abs/2102.12452\n    venue: Computational Linguistics 48(1)\n    verified: true\n    year: 2022\n  hewitt2019designing:\n    added_at: '2026-05-22T14:30:00Z'\n    added_by: paper-agent-lit-search\n    authors:\n    - Hewitt, J.\n    - Liang, P.\n    bibtex_key: hewitt2019designing\n    category: probing-methodology\n    doi: ''\n    relevance: Introduces selectivity metric (linguistic accuracy - control accuracy)\n      to distinguish genuine representation encoding from probe memorization. Our probing\n      design uses control tasks following this framework. EMNLP 2019 Best Paper Runner\n      Up.\n    role: methodology\n    title: Designing and Interpreting Probes with Control Tasks\n    url: https://aclanthology.org/D19-1275/\n    venue: EMNLP 2019\n    verified: true\n    year: 2019\n  ulmer2022deep:\n    added_at: '2026-05-22T14:30:00Z'\n    added_by: paper-agent-lit-search\n    authors:\n    - Ulmer, D.\n    - Hardmeier, C.\n    - Frellsen, J.\n    bibtex_key: ulmer2022deep\n    category: probing-methodology\n    doi: ''\n    relevance: Bootstrap-based statistical testing framework for neural network comparisons,\n      including Almost Stochastic Order (ASO). Provides the bootstrap CI methodology\n      we use for probing accuracy significance testing.\n    role: methodology\n    title: 'deep-significance: Easy and Meaningful Statistical Significance Testing\n      in the Age of Neural Networks'\n    url: https://arxiv.org/abs/2204.06815\n    venue: arXiv\n    verified: true\n    year: 2022"
  }
}
```

</details>

---

### Tool result

_source line 38 · 2026-05-22T13:49:18.771160+00:00_

The file /home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/literature_map.yaml has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_research_cluster34_20260522T134427",
  "tool": "Edit",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 39 · 2026-05-22T13:49:18.771318+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "python3 -c \"\nimport yaml\nwith open('literature_map.yaml') as f:\n    data = yaml.safe_load(f)\nprint(f'Total papers in meta: {data[\\\"meta\\\"][\\\"total_papers\\\"]}')\nprint(f'Actual paper count: {len(data[\\\"papers\\\"])}')\nprint()\nnew_keys = ['wu2020emerging','wendler2024llamas','muller2021first','kargaran2024mexa','belinkov2022probing','hewitt2019designing','ulmer2022deep']\nfor k in new_keys:\n    p = data['papers'][k]\n    print(f'{k}: {p[\\\"title\\\"][:60]}... | {p[\\\"venue\\\"]} | {p[\\\"year\\\"]} | verified={p[\\\"verified\\\"]}')\n\"\n",
  "description": "Verify YAML integrity and new paper entries"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_research_cluster34_20260522T134427",
  "tool": "Bash",
  "tool_args": {
    "command": "python3 -c \"\nimport yaml\nwith open('literature_map.yaml') as f:\n    data = yaml.safe_load(f)\nprint(f'Total papers in meta: {data[\\\"meta\\\"][\\\"total_papers\\\"]}')\nprint(f'Actual paper count: {len(data[\\\"papers\\\"])}')\nprint()\nnew_keys = ['wu2020emerging','wendler2024llamas','muller2021first','kargaran2024mexa','belinkov2022probing','hewitt2019designing','ulmer2022deep']\nfor k in new_keys:\n    p = data['papers'][k]\n    print(f'{k}: {p[\\\"title\\\"][:60]}... | {p[\\\"venue\\\"]} | {p[\\\"year\\\"]} | verified={p[\\\"verified\\\"]}')\n\"\n",
    "description": "Verify YAML integrity and new paper entries"
  }
}
```

</details>

---

### Tool result

_source line 40 · 2026-05-22T13:49:18.771452+00:00_

Total papers in meta: 22
Actual paper count: 22

wu2020emerging: Emerging Cross-lingual Structure in Pretrained Language Mode... | ACL 2020 | 2020 | verified=True
wendler2024llamas: Do Llamas Work in English? On the Latent Language of Multili... | ACL 2024 | 2024 | verified=True
muller2021first: First Align, then Predict: Understanding the Cross-Lingual A... | EACL 2021 | 2021 | verified=True
kargaran2024mexa: MEXA: Multilingual Evaluation of English-Centric LLMs via Cr... | Findings of ACL 2025 | 2024 | verified=True
belinkov2022probing: Probing Classifiers: Promises, Shortcomings, and Advances... | Computational Linguistics 48(1) | 2022 | verified=True
hewitt2019designing: Designing and Interpreting Probes with Control Tasks... | EMNLP 2019 | 2019 | verified=True
ulmer2022deep: deep-significance: Easy and Meaningful Statistical Significa... | arXiv | 2022 | verified=True

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_research_cluster34_20260522T134427",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 41 · 2026-05-22T13:49:18.771620+00:00_

22 篇，YAML 完整。汇总：

**Cluster 3: Cross-lingual Representations (+4)**
| Key | Title | Venue |
|-----|-------|-------|
| `wu2020emerging` | Emerging Cross-lingual Structure in Pretrained Language Models | ACL 2020 **(MUST CITE)** |
| `wendler2024llamas` | Do Llamas Work in English? On the Latent Language of Multilingual Transformers | ACL 2024 |
| `muller2021first` | First Align, then Predict: Understanding the Cross-Lingual Ability of Multilingual BERT | EACL 2021 |
| `kargaran2024mexa` | MEXA: Multilingual Evaluation of English-Centric LLMs via Cross-Lingual Alignment | Findings of ACL 2025 |

**Cluster 4: Probing Methodology (+3)**
| Key | Title | Venue |
|-----|-------|-------|
| `belinkov2022probing` | Probing Classifiers: Promises, Shortcomings, and Advances | Computational Linguistics 48(1) **(MUST CITE)** |
| `hewitt2019designing` | Designing and Interpreting Probes with Control Tasks | EMNLP 2019 |
| `ulmer2022deep` | deep-significance: Easy and Meaningful Statistical Significance Testing in the Age of Neural Networks | arXiv 2022 |

所有 URL 已通过 WebSearch 确认指向真实论文。literature_map.yaml 已从 15 篇更新至 22 篇。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_paper_research_cluster34_20260522T134427"
}
```

</details>

---
