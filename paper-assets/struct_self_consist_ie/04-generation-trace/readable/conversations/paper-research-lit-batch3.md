# paper research lit batch3

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 49
- **Recorded user turns:** 0
- **Tool calls:** 24
- **Original source:** `logs/chats/worker_paper_research_lit_batch3_20260514T182744.jsonl`
- **Structured JSON:** [`aea31c7d2731f10db572.json`](../../sessions/ae/aea31c7d2731f10db572.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

49 recorded events

### Tool call

_source line 1 · 2026-05-14T18:31:18.146903+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/literature_map.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_research_lit_batch3_20260514T182744",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/literature_map.yaml"
  }
}
```

</details>

---

### Tool result

_source line 2 · 2026-05-14T18:31:18.147466+00:00_

1	meta:
2	  last_updated: '2026-05-14T18:10:52.000Z'
3	  total_papers: 30
4	categories: []
5	papers:
6	  wang2023selfconsistency:
7	    title: Self-Consistency Improves Chain of Thought Reasoning in Language Models
8	    authors:
9	    - Xuezhi Wang
10	    - Jason Wei
11	    - Dale Schuurmans
12	    - Quoc Le
13	    - Ed Chi
14	    - Sharan Narang
15	    - Aakanksha Chowdhery
16	    - Denny Zhou
17	    year: 2023
18	    venue: ICLR 2023
19	    url: https://arxiv.org/abs/2203.11171
20	    doi: ''
21	    bibtex_key: wang2023selfconsistency
22	    category: self_consistency_reasoning
23	    role: foundation
24	    relevance: 'Foundation paper: introduces self-consistency voting over diverse reasoning paths. We extend this paradigm
25	      from closed-form answers to structured IE outputs.'
26	    abstract: ''
27	    semantic_scholar_id: ''
28	    verified: true
29	    added_by: paper-research:cluster1
30	    added_at: '2026-05-14T15:47:22.188Z'
31	  taubenfeld2025cisc:
32	    title: Confidence Improves Self-Consistency in LLMs
33	    authors:
34	    - Amir Taubenfeld
35	    - Tom Sheffer
36	    - Eran Ofek
37	    - Amir Feder
38	    - Ariel Goldstein
39	    - Zorik Gekhman
40	    - Gal Yona
41	    year: 2025
42	    venue: ACL Findings 2025
43	    url: https://arxiv.org/abs/2502.06233
44	    doi: 10.18653/v1/2025.findings-acl.1030
45	    bibtex_key: taubenfeld2025cisc
46	    category: self_consistency_reasoning
47	    role: direct-competitor
48	    relevance: 'CISC: confidence-weighted majority vote reduces required samples by 40%. Direct competitor — we address the
49	      same "strong predictor, weak selector" gap but for structured outputs.'
50	    abstract: ''
51	    semantic_scholar_id: ''
52	    verified: true
53	    added_by: paper-research:cluster1
54	    added_at: '2026-05-14T15:47:22.188Z'
55	  kang2025selfcertainty:
56	    title: Scalable Best-of-N Selection for Large Language Models via Self-Certainty
57	    authors:
58	    - Zhewei Kang
59	    - Xuandong 
…[truncated 25142 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_research_lit_batch3_20260514T182744",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-14T18:31:18.147690+00:00_

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
  "session": "worker_paper_research_lit_batch3_20260514T182744",
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

_source line 4 · 2026-05-14T18:31:18.147838+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_research_lit_batch3_20260514T182744",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-14T18:31:18.147988+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Cobbe et al 2021 \"Training Verifiers to Solve Math Word Problems\" arXiv 2110.14168"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_research_lit_batch3_20260514T182744",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Cobbe et al 2021 \"Training Verifiers to Solve Math Word Problems\" arXiv 2110.14168"
  }
}
```

</details>

---

### Tool call

_source line 6 · 2026-05-14T18:31:18.148112+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Lightman et al 2023 \"Let's Verify Step by Step\" arXiv 2305.20050 ICLR 2024"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_research_lit_batch3_20260514T182744",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Lightman et al 2023 \"Let's Verify Step by Step\" arXiv 2305.20050 ICLR 2024"
  }
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-14T18:31:18.148261+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Snell et al 2024 \"Scaling LLM Test-Time Compute Optimally\" arXiv 2408.03314"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_research_lit_batch3_20260514T182744",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Snell et al 2024 \"Scaling LLM Test-Time Compute Optimally\" arXiv 2408.03314"
  }
}
```

</details>

---

### Tool call

_source line 8 · 2026-05-14T18:31:18.148379+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Brown et al 2024 \"Large Language Monkeys\" arXiv 2407.21787 test-time compute scaling"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_research_lit_batch3_20260514T182744",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Brown et al 2024 \"Large Language Monkeys\" arXiv 2407.21787 test-time compute scaling"
  }
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-14T18:31:18.148505+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Kuleshov Liang 2015 \"Calibrated Structured Prediction\" NeurIPS 2015"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_research_lit_batch3_20260514T182744",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Kuleshov Liang 2015 \"Calibrated Structured Prediction\" NeurIPS 2015"
  }
}
```

</details>

---

### Tool call

_source line 10 · 2026-05-14T18:31:18.148621+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Culotta McCallum 2004 \"Confidence Estimation for Information Extraction\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_research_lit_batch3_20260514T182744",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Culotta McCallum 2004 \"Confidence Estimation for Information Extraction\""
  }
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-14T18:31:18.148731+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Geifman El-Yaniv 2017 \"Selective Classification for Deep Neural Networks\" NeurIPS 2017"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_research_lit_batch3_20260514T182744",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Geifman El-Yaniv 2017 \"Selective Classification for Deep Neural Networks\" NeurIPS 2017"
  }
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-14T18:31:18.148898+00:00_

Web search results for query: "Lightman et al 2023 "Let's Verify Step by Step" arXiv 2305.20050 ICLR 2024"

Links: [{"title":"[2305.20050] Let's Verify Step by Step","url":"https://arxiv.org/abs/2305.20050"},{"title":"[PDF] Let's Verify Step by Step | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Let's-Verify-Step-by-Step-Lightman-Kosaraju/be8db99310602d66bba64bcf41a572c45816fbfc"},{"title":"Let's Verify Step by Step","url":"https://www.researchgate.net/publication/371175770_Let's_Verify_Step_by_Step"},{"title":"Paper page - Let's Verify Step by Step","url":"https://huggingface.co/papers/2305.20050"},{"title":"[2305.20050] Let's Verify Step by Step - ar5iv - arXiv","url":"https://ar5iv.labs.arxiv.org/html/2305.20050"},{"title":"[2305.20050] Let's Verify Step by Step","url":"http://export.arxiv.org/abs/2305.20050"},{"title":"Let's Verify Step by Step | OpenReview","url":"https://openreview.net/forum?id=v8L0pN6EOi"},{"title":"Let’s Verify Step by Step Hunter Lightman∗ Vineet Kosaraju∗ Yura Burda∗","url":"https://arxiv.org/pdf/2305.20050"},{"title":"[2305.20050v1] Let's Verify Step by Step","url":"https://arxiv.org/abs/2305.20050v1"},{"title":"Let’s Verify Step by Step (must-read to build OpenAI o1) - Paper Without Code","url":"https://paperwithoutcode.com/lets-verify-step-by-step-must-read-to-build-openai-o1/"}]

I found the paper successfully. Here's information about "Let's Verify Step by Step" by Lightman et al.:

## Paper Details

**Title:** Let's Verify Step by Step

**Authors:** Hunter Lightman, Vineet Kosaraju, Yura Burda, Harri Edwards, Bowen Baker, Teddy Lee, Jan Leike, John Schulman, Ilya Sutskever, Karl Cobbe

**arXiv ID:** 2305.20050

**Submission Date:** May 31, 2023

**Venue:** Published in International Conference on Learning Representations (ICLR) 2024

## Main Contribution

The research found that process supervision significantly outperforms outcome supervision for training models to solve problems from the challenging MATH dataset. 
…[truncated 606 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_research_lit_batch3_20260514T182744",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 13 · 2026-05-14T18:31:18.149114+00:00_

Web search results for query: "Cobbe et al 2021 "Training Verifiers to Solve Math Word Problems" arXiv 2110.14168"

Links: [{"title":"[2110.14168] Training Verifiers to Solve Math Word Problems","url":"https://arxiv.org/abs/2110.14168"},{"title":"[PDF] Training Verifiers to Solve Math Word Problems | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Training-Verifiers-to-Solve-Math-Word-Problems-Cobbe-Kosaraju/d6045d2ccc9c09ca1671348de86d07da6bc28eea"},{"title":"Training Verifiers to Solve Math Word Problems","url":"https://www.researchgate.net/publication/355698629_Training_Verifiers_to_Solve_Math_Word_Problems"},{"title":"arXiv:2110.14168v2 [cs.LG] 18 Nov 2021","url":"https://arxiv.org/pdf/2110.14168"},{"title":"Paper page - Training Verifiers to Solve Math Word Problems","url":"https://huggingface.co/papers/2110.14168"},{"title":"dblp: Training Verifiers to Solve Math Word Problems.","url":"https://dblp.org/rec/journals/corr/abs-2110-14168.html"},{"title":"[2110.14168v1] Training Verifiers to Solve Math Word Problems","url":"https://arxiv.org/abs/2110.14168v1"},{"title":"Google Scholar","url":"https://scholar.google.com/scholar_lookup?title=Training+verifiers+to+solve+math+word+problems&amp=&author=K.+Cobbe&amp=&publication_year=2021"},{"title":"[2110.14168v2] Training Verifiers to Solve Math Word Problems","url":"https://arxiv.org/abs/2110.14168v2"},{"title":"Improve Mathematical Reasoning in Language Models by ...","url":"https://arxiv.org/pdf/2406.06592"}]

I found the paper! Here's information about it:

**Title:** Training Verifiers to Solve Math Word Problems

**Authors:** Karl Cobbe, Vineet Kosaraju, Mohammad Bavarian, Mark Chen, Heewoo Jun, Lukasz Kaiser, Matthias Plappert, Jerry Tworek, Jacob Hilton, Reiichiro Nakano, Christopher Hesse, and John Schulman

**arXiv ID:** 2110.14168

**Submission Date:** Submitted on 27 Oct 2021 (v1), last revised 18 Nov 2021 (v2)

**Summary:** 

State-of-the-art language models can match human performance on m
…[truncated 1002 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_research_lit_batch3_20260514T182744",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-14T18:31:18.149330+00:00_

Web search results for query: "Snell et al 2024 "Scaling LLM Test-Time Compute Optimally" arXiv 2408.03314"

Links: [{"title":"[2408.03314] Scaling LLM Test-Time Compute Optimally can be More Effective than Scaling Model Parameters","url":"https://arxiv.org/abs/2408.03314"},{"title":"Scaling LLM Test-Time Compute Optimally can be More Effective than Scaling Model Parameters","url":"https://arxiv.org/html/2408.03314v1"},{"title":"2024-8-7 Scaling LLM Test-Time Compute Optimally can","url":"https://arxiv.org/pdf/2408.03314"},{"title":"Scaling LLM Test-Time Compute Optimally Can be More Effective than Scaling Parameters for Reasoning | OpenReview","url":"https://openreview.net/forum?id=4FWAwZtd2n"},{"title":"(PDF) Scaling LLM Test-Time Compute Optimally can be More Effective than Scaling Model Parameters","url":"https://www.researchgate.net/publication/382914793_Scaling_LLM_Test-Time_Compute_Optimally_can_be_More_Effective_than_Scaling_Model_Parameters"},{"title":"Paper page - Scaling LLM Test-Time Compute Optimally can be More Effective than Scaling Model Parameters","url":"https://huggingface.co/papers/2408.03314"},{"title":"[2408.03314v1] Scaling LLM Test-Time Compute Optimally can be More Effective than Scaling Model Parameters","url":"https://arxiv.org/abs/2408.03314v1"},{"title":"Scaling LLM Test-Time Compute Optimally can be More Effective than Scaling Model Parameters | by Eleventh Hour Enthusiast | Medium","url":"https://medium.com/@EleventhHourEnthusiast/scaling-llm-test-time-compute-optimally-can-be-more-effective-than-scaling-model-parameters-19a0c9fb7c44"},{"title":"What is Test Time Compute? | CSA","url":"https://cloudsecurityalliance.org/blog/2024/12/13/test-time-compute"},{"title":"Scaling LLM Test-Time Compute Optimally can be More Effective than Scaling Model Parameters, Charlie Snell+, arXiv'24 · Issue #1501 · AkihikoWatanabe/paper_notes","url":"https://github.com/AkihikoWatanabe/paper_notes/issues/1501"}]

I found the paper! Here's information about
…[truncated 1344 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_research_lit_batch3_20260514T182744",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 15 · 2026-05-14T18:31:18.149514+00:00_

Web search results for query: "Brown et al 2024 "Large Language Monkeys" arXiv 2407.21787 test-time compute scaling"

Links: [{"title":"[2407.21787] Large Language Monkeys: Scaling Inference Compute with Repeated Sampling","url":"https://arxiv.org/abs/2407.21787"},{"title":"Large Language Monkeys: Scaling Inference Compute with Repeated Sampling","url":"https://arxiv.org/pdf/2407.21787"},{"title":"GitHub - ScalingIntelligence/large_language_monkeys","url":"https://github.com/ScalingIntelligence/large_language_monkeys"},{"title":"(PDF) Large Language Monkeys: Scaling Inference Compute with Repeated Sampling","url":"https://www.researchgate.net/publication/382739350_Large_Language_Monkeys_Scaling_Inference_Compute_with_Repeated_Sampling"},{"title":"Large Language Monkeys: Scaling Inference Compute with Repeated Sampling | Scaling Intelligence Lab at Stanford University","url":"https://scalingintelligence.stanford.edu/pubs/large_language_monkeys/"},{"title":"[Research Paper Summary] Large Language Monkeys: Scaling Inference Compute with Repeated Sampling | by Himanshu Bamoria | Athina AI | Medium","url":"https://medium.com/athina-ai/large-language-monkeys-scaling-inference-compute-with-repeated-sampling-4de85a3e1384"},{"title":"[2407.21787v1] Large Language Monkeys: Scaling Inference Compute with Repeated Sampling","url":"https://arxiv.org/abs/2407.21787v1"},{"title":"ScalingIntelligence/monkey_business · Datasets at Hugging Face","url":"https://huggingface.co/datasets/ScalingIntelligence/monkey_business"},{"title":"Large Language Monkeys: Scaling Inference Compute with Repeated Sampling | OpenReview","url":"https://openreview.net/forum?id=0xUEBQV54B"},{"title":"Large Language Monkeys: Scaling Inference Compute with Repeated Sampling - ADS","url":"https://ui.adsabs.harvard.edu/abs/2024arXiv240721787B/abstract"}]

I found the paper you're looking for. Here are the key findings:

## Large Language Monkeys: Scaling Inference Compute with Repeated Sampling

The paper is au
…[truncated 1122 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_research_lit_batch3_20260514T182744",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-14T18:31:18.149694+00:00_

Web search results for query: "Kuleshov Liang 2015 "Calibrated Structured Prediction" NeurIPS 2015"

Links: [{"title":"Calibrated Structured Prediction","url":"https://proceedings.neurips.cc/paper/2015/hash/52d2752b150f9c35ccb6869cbf074e48-Abstract.html"},{"title":"Calibrated Structured Prediction","url":"https://papers.nips.cc/paper/5658-calibrated-structured-prediction"},{"title":"Calibrated structured prediction | Proceedings of the 29th International Conference on Neural Information Processing Systems - Volume 2","url":"https://dl.acm.org/citation.cfm?id=2969627"},{"title":"[PDF] Calibrated Structured Prediction | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Calibrated-Structured-Prediction-Kuleshov-Liang/a068b2dc837ed925a6f4724467572c05cbeb5f98"},{"title":"Calibrated Structured Prediction Volodymyr Kuleshov, Percy Liang","url":"https://ai.stanford.edu/~kuleshov/papers/nips2015-poster.pdf"},{"title":"[2004.04361] Calibrating Structured Output Predictors for Natural Language Processing","url":"https://ar5iv.labs.arxiv.org/html/2004.04361"},{"title":"Online Calibrated and Conformal Prediction Improves Bayesian Optimization - PMC","url":"https://pmc.ncbi.nlm.nih.gov/articles/PMC11482741/"},{"title":"Calibrating Structured Output Predictors for Natural Language Processing - PMC","url":"https://pmc.ncbi.nlm.nih.gov/articles/PMC7890517/"},{"title":"Calibrated Structured Prediction Volodymyr Kuleshov","url":"https://cs.stanford.edu/~pliang/papers/calibration-nips2015.pdf"},{"title":"Accurate Uncertainties for Deep Learning Using Calibrated Regression","url":"https://proceedings.mlr.press/v80/kuleshov18a/kuleshov18a.pdf"}]

I found the paper you were looking for. Here's what I can tell you about it:

"Calibrated Structured Prediction" was published by Volodymyr Kuleshov and Percy Liang at Advances in Neural Information Processing Systems 28 (NIPS 2015).

The paper addresses an important problem: in user-facing applications, displaying calibrated confid
…[truncated 958 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_research_lit_batch3_20260514T182744",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 17 · 2026-05-14T18:31:18.149869+00:00_

Web search results for query: "Culotta McCallum 2004 "Confidence Estimation for Information Extraction""

Links: [{"title":"Confidence Estimation for Information Extraction - ACL Anthology","url":"https://aclanthology.org/N04-4028/"},{"title":"Confidence Estimation for Information Extraction - ACL Anthology","url":"https://www.aclweb.org/anthology/N04-4028/"},{"title":"Confidence estimation for information extraction","url":"https://tapilab.github.io/information%20extraction/2004/01/01/confidence"},{"title":"Confidence Estimation for Information Extraction | Request PDF","url":"https://www.researchgate.net/publication/2605436_Confidence_Estimation_for_Information_Extraction"},{"title":"[PDF] Confidence Estimation for Information Extraction | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Confidence-Estimation-for-Information-Extraction-Culotta-McCallum/e2ca689c4eb4284ec10f27cc8c6e5bae73569140"},{"title":"(PDF) Confidence Estimation for Information Extraction","url":"https://www.academia.edu/158606/Confidence_Estimation_for_Information_Extraction"},{"title":"Confidence estimation for NLP applications | ACM Transactions on Speech and Language Processing","url":"https://dl.acm.org/doi/10.1145/1177055.1177057"},{"title":"Confidence Estimation for Information Extraction","url":"https://cs.tulane.edu/~aculotta/pubs/culotta04confidence.pdf"},{"title":"Confidence Estimation for Information Extraction | OpenReview","url":"https://openreview.net/forum?id=SkEs0zZuZr"},{"title":"(PDF) Corrective Feedback and Persistent Learning for Information Extraction","url":"https://www.academia.edu/158390/Corrective_Feedback_and_Persistent_Learning_for_Information_Extraction"}]

I've found the paper you're looking for. Here are the key details:

Aron Culotta and Andrew McCallum published "Confidence Estimation for Information Extraction" in 2004 in the Proceedings of HLT-NAACL 2004: Short Papers, pages 109–112, Boston, Massachusetts, USA, published by the Association for Co
…[truncated 813 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_research_lit_batch3_20260514T182744",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-14T18:31:18.150043+00:00_

Web search results for query: "Geifman El-Yaniv 2017 "Selective Classification for Deep Neural Networks" NeurIPS 2017"

Links: [{"title":"[1705.08500] Selective Classification for Deep Neural Networks","url":"https://arxiv.org/abs/1705.08500"},{"title":"[PDF] Selective Classification for Deep Neural Networks | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Selective-Classification-for-Deep-Neural-Networks-Geifman-El-Yaniv/2ed7cc027367295b1a7d7cd49406acfa5c580138"},{"title":"(PDF) Selective Classification for Deep Neural Networks","url":"https://www.researchgate.net/publication/317100919_Selective_Classification_for_Deep_Neural_Networks"},{"title":"Selective Classification for Deep Neural Networks","url":"https://proceedings.neurips.cc/paper_files/paper/2017/hash/4a8423d5e91fda00bb7e46540e2b0cf1-Abstract.html"},{"title":"GitHub - geifmany/selective_deep_learning: Code for the paper \"Selective Classification for Deep Neural Networks\" · GitHub","url":"https://github.com/geifmany/selective_deep_learning"},{"title":"Selective Classification for Deep Neural Networks - NIPS papers","url":"https://papers.nips.cc/paper/7073-selective-classification-for-deep-neural-networks"},{"title":"ICML oral selectivenet_pdf","url":"https://geifmany.github.io/papers/icml_oral.pdf"},{"title":"Selective Classification for Deep Neural Networks [Quick Review]","url":"https://liner.com/review/selective-classification-for-deep-neural-networks"},{"title":"Selective classification for deep neural networks | Proceedings of the 31st International Conference on Neural Information Processing Systems","url":"https://dl.acm.org/doi/10.5555/3295222.3295241"},{"title":"Yonatan Geifman Technion","url":"https://geifmany.github.io/papers/selective_pdf.pdf"}]

I found the paper you're looking for! Here's the information about it:

**Paper Details:**

The paper "Selective Classification for Deep Neural Networks" by Yonatan Geifman and Ran El-Yaniv was published in Advances in Neural Informat
…[truncated 1036 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_research_lit_batch3_20260514T182744",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-14T18:31:18.150250+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "outcome reward model process reward model 2023 2024 math reasoning verification survey"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_research_lit_batch3_20260514T182744",
  "tool": "WebSearch",
  "tool_args": {
    "query": "outcome reward model process reward model 2023 2024 math reasoning verification survey"
  }
}
```

</details>

---

### Tool call

_source line 20 · 2026-05-14T18:31:18.150381+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "test-time compute scaling 2024 2025 compute-optimal inference LLM reasoning recent work"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_research_lit_batch3_20260514T182744",
  "tool": "WebSearch",
  "tool_args": {
    "query": "test-time compute scaling 2024 2025 compute-optimal inference LLM reasoning recent work"
  }
}
```

</details>

---

### Tool call

_source line 21 · 2026-05-14T18:31:18.150509+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Jagannatha Yu 2022 NER confidence estimation calibration information extraction"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_research_lit_batch3_20260514T182744",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Jagannatha Yu 2022 NER confidence estimation calibration information extraction"
  }
}
```

</details>

---

### Tool call

_source line 22 · 2026-05-14T18:31:18.150624+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "selective prediction learning to abstain NLP 2023 2024 language model"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_research_lit_batch3_20260514T182744",
  "tool": "WebSearch",
  "tool_args": {
    "query": "selective prediction learning to abstain NLP 2023 2024 language model"
  }
}
```

</details>

---

### Tool result

_source line 23 · 2026-05-14T18:31:18.150769+00:00_

Web search results for query: "Jagannatha Yu 2022 NER confidence estimation calibration information extraction"

Links: [{"title":"Calibrated Interpretation: Confidence Estimation in Semantic Parsing | Transactions of the Association for Computational Linguistics | MIT Press","url":"https://direct.mit.edu/tacl/article/doi/10.1162/tacl_a_00598/117737/Calibrated-Interpretation-Confidence-Estimation-in"},{"title":"A Survey of Confidence Estimation and Calibration in ...","url":"https://aclanthology.org/2024.naacl-long.366.pdf"},{"title":"[2104.04318] Noisy-Labeled NER with Confidence Estimation","url":"https://arxiv.org/abs/2104.04318"},{"title":"Calibrating Structured Output Predictors for Natural Language Processing - PMC","url":"https://pmc.ncbi.nlm.nih.gov/articles/PMC7890517/"},{"title":"A study of calibration as a measurement of trustworthiness of large language models in biomedical natural language processing - PMC","url":"https://pmc.ncbi.nlm.nih.gov/articles/PMC12249208/"},{"title":"Calibrating Structured Output Predictors for Natural ...","url":"https://aclanthology.org/2020.acl-main.188.pdf"},{"title":"Calibrated Interpretation: Confidence Estimation in Semantic Parsing","url":"https://aclanthology.org/2023.tacl-1.69.pdf"},{"title":"Confidence Estimation for Information Extraction | Request PDF","url":"https://www.researchgate.net/publication/2605436_Confidence_Estimation_for_Information_Extraction"},{"title":"Named Entity Recognition using Neural Networks for Clinical ...","url":"http://proceedings.mlr.press/v90/florez18a/florez18a.pdf"},{"title":"GitHub - ShiyuNee/Awesome-Calibration-Papers: A curated list of awesome papers about calibration · GitHub","url":"https://github.com/ShiyuNee/Awesome-Calibration-Papers"}]

Based on the web search results, I found relevant information about Jagannatha and Yu's work on confidence estimation and calibration:

## Key Findings

Jagannatha and Yu addressed the problem of calibrating prediction confidence for output ent
…[truncated 1101 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_research_lit_batch3_20260514T182744",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 24 · 2026-05-14T18:31:18.151158+00:00_

Web search results for query: "test-time compute scaling 2024 2025 compute-optimal inference LLM reasoning recent work"

Links: [{"title":"[2408.03314] Scaling LLM Test-Time Compute Optimally can be More Effective than Scaling Model Parameters","url":"https://arxiv.org/abs/2408.03314"},{"title":"Scaling LLM Test-Time Compute Optimally Can be More Effective than Scaling Parameters for Reasoning | OpenReview","url":"https://openreview.net/forum?id=4FWAwZtd2n"},{"title":"Scaling LLM Test-Time Compute Optimally can be More Effective than Scaling Model Parameters","url":"https://arxiv.org/html/2408.03314v1"},{"title":"The Art of Scaling Test-Time Compute for Large Language Models","url":"https://arxiv.org/html/2512.02008v1"},{"title":"A brief history of LLM Scaling Laws and what to expect in 2025","url":"https://www.jonvet.com/blog/llm-scaling-in-2025"},{"title":"Inference Scaling Laws: An Empirical Analysis of Compute-Optimal Inference for LLM Problem-Solving | OpenReview","url":"https://openreview.net/forum?id=VNckp7JEHn"},{"title":"[2512.02008] The Art of Scaling Test-Time Compute for Large Language Models","url":"https://arxiv.org/abs/2512.02008"},{"title":"[2408.00724] Inference Scaling Laws: An Empirical Analysis of Compute-Optimal Inference for Problem-Solving with Language Models","url":"https://arxiv.org/abs/2408.00724"},{"title":"ICLR 2025 Scaling LLM Test-Time Compute Optimally Can be More Effective than Scaling Parameters for Reasoning Oral","url":"https://iclr.cc/virtual/2025/oral/31924"},{"title":"Scaling Test-time Compute for LLM Agents","url":"https://arxiv.org/html/2506.12928v1"}]

Based on the search results, here's what recent research shows about test-time compute scaling for LLM reasoning:

## Key Recent Work

**2024 Foundational Research:**

Enabling LLMs to improve their outputs by using more test-time computation is a critical step towards building generally self-improving agents that can operate on open-ended natural language. A prominent August 
…[truncated 1695 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_research_lit_batch3_20260514T182744",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 25 · 2026-05-14T18:31:18.151363+00:00_

Web search results for query: "selective prediction learning to abstain NLP 2023 2024 language model"

Links: [{"title":"Know Your Limits: A Survey of Abstention in Large Language Models | Transactions of the Association for Computational Linguistics | MIT Press","url":"https://direct.mit.edu/tacl/article/doi/10.1162/tacl_a_00754/131566/Know-Your-Limits-A-Survey-of-Abstention-in-Large"},{"title":"Selective prediction for extracting unstructured clinical data | Journal of the American Medical Informatics Association | Oxford Academic","url":"https://academic.oup.com/jamia/article/31/1/188/7285661"},{"title":"SelectLLM – Calibrating LLMs for Selective Prediction: Balancing Coverage and Risk | OpenReview","url":"https://openreview.net/forum?id=JJPAy8mvrQ"},{"title":"Know Your Limits: A Survey of Abstention in Large Language Models Bingbing Wen1","url":"https://www.llwang.net/assets/pdf/2025_wen_abstention-survey_tacl.pdf"},{"title":"Selective Prediction in Natural Language Processing | by Neeraj Varshney | Medium","url":"https://medium.com/@nvarshney97/selective-prediction-in-natural-language-processing-838244f1e8e1"},{"title":"Know Your Limits: A Survey of Abstention in Large Language Models Bingbing Wen1","url":"https://arxiv.org/pdf/2407.18418"},{"title":"Towards Reliably Re-Attempting the Abstained Instances ...","url":"https://aclanthology.org/2023.acl-long.55.pdf"},{"title":"The Art of Abstention: Selective Prediction and Error Regularization for Natural Language Processing - ACL Anthology","url":"https://aclanthology.org/2021.acl-long.84/"},{"title":"Know Your Limits: A Survey of Abstention in Large Language Models Bingbing Wen1","url":"https://aclanthology.org/2025.tacl-1.26.pdf"},{"title":"Selective Prediction: Maximize the Accuracy of powerful LLMs","url":"https://datasciencedojo.com/blog/selective-prediction-llms/"}]

I've successfully performed the web search for selective prediction learning to abstain in NLP for 2023-2024 language models. Here are the key
…[truncated 1817 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_research_lit_batch3_20260514T182744",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 26 · 2026-05-14T18:31:18.151554+00:00_

Web search results for query: "outcome reward model process reward model 2023 2024 math reasoning verification survey"

Links: [{"title":"[2510.08049] A Survey of Process Reward Models: From Outcome Signals to Process Supervisions for Large Language Models","url":"https://arxiv.org/abs/2510.08049"},{"title":"A Survey of Process Reward Models: From Outcome Signals to Process Supervisions for Large Language Models","url":"https://arxiv.org/html/2510.08049v3"},{"title":"The Lessons of Developing Process Reward Models in ...","url":"https://arxiv.org/pdf/2501.07301"},{"title":"A Survey of Process Reward Models: From Outcome Signals to Process","url":"https://arxiv.org/pdf/2510.08049"},{"title":"[2305.20050] Let's Verify Step by Step","url":"https://arxiv.org/abs/2305.20050"},{"title":"GitHub - bobxwu/learning-from-rewards-llm-papers: A comrephensive collection of learning from rewards in the post-training and test-time scaling of LLMs, with a focus on both reward models and learning strategies across training, inference, and post-inference stages. · GitHub","url":"https://github.com/bobxwu/learning-from-rewards-llm-papers"},{"title":"Generalizable Process Reward Models via Formally Verified Training Data","url":"https://arxiv.org/pdf/2505.15960"},{"title":"Process Reward Models That Think","url":"https://arxiv.org/pdf/2504.16828"},{"title":"Math-Shepherd: Verify and Reinforce LLMs Step-by- ...","url":"https://aclanthology.org/2024.acl-long.510.pdf"},{"title":"Published as a conference paper at ICLR 2024 LET’S VERIFY STEP BY STEP","url":"https://proceedings.iclr.cc/paper_files/paper/2024/file/aca97732e30bcf1303bc22ac3924fd16-Paper-Conference.pdf"}]

Based on the search results, here's a comprehensive overview of outcome reward models, process reward models, and their application to math reasoning verification:

## Key Overview

Outcome Reward Models (ORMs) judge only final answers, while Process Reward Models (PRMs) address this gap by evaluating and guiding reasoning at
…[truncated 2139 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_research_lit_batch3_20260514T182744",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool call

_source line 27 · 2026-05-14T18:31:18.151729+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Wang et al 2024 \"Math-Shepherd\" verify reinforce LLMs step-by-step ACL 2024 arXiv"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_research_lit_batch3_20260514T182744",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Wang et al 2024 \"Math-Shepherd\" verify reinforce LLMs step-by-step ACL 2024 arXiv"
  }
}
```

</details>

---

### Tool call

_source line 28 · 2026-05-14T18:31:18.151857+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "arXiv 2408.00724 \"Inference Scaling Laws\" compute-optimal inference problem-solving language models"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_research_lit_batch3_20260514T182744",
  "tool": "WebSearch",
  "tool_args": {
    "query": "arXiv 2408.00724 \"Inference Scaling Laws\" compute-optimal inference problem-solving language models"
  }
}
```

</details>

---

### Tool call

_source line 29 · 2026-05-14T18:31:18.151977+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Jagannatha Yu 2020 \"Calibrating Structured Output Predictors for Natural Language Processing\" ACL 2020"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_research_lit_batch3_20260514T182744",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Jagannatha Yu 2020 \"Calibrating Structured Output Predictors for Natural Language Processing\" ACL 2020"
  }
}
```

</details>

---

### Tool call

_source line 30 · 2026-05-14T18:31:18.152093+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Varshney et al 2023 selective prediction NLP \"Art of Saying No\" OR \"selective prediction\" ACL EMNLP 2023 language model abstain"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_research_lit_batch3_20260514T182744",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Varshney et al 2023 selective prediction NLP \"Art of Saying No\" OR \"selective prediction\" ACL EMNLP 2023 language model abstain"
  }
}
```

</details>

---

### Tool result

_source line 31 · 2026-05-14T18:31:18.152263+00:00_

Web search results for query: "arXiv 2408.00724 "Inference Scaling Laws" compute-optimal inference problem-solving language models"

Links: [{"title":"[2408.00724] Inference Scaling Laws: An Empirical Analysis of Compute-Optimal Inference for Problem-Solving with Language Models","url":"https://arxiv.org/abs/2408.00724"},{"title":"Inference Scaling Laws: An Empirical Analysis of Compute-Optimal Inference for Problem-Solving with Language Models","url":"https://thu-wyz.github.io/inference-scaling/"},{"title":"Inference Scaling Laws: An Empirical Analysis of Compute-Optimal Inference for LLM Problem-Solving","url":"https://arxiv.org/html/2408.00724v2"},{"title":"Inference Scaling Laws: An Empirical Analysis of Compute-Optimal Inference for LLM Problem-Solving | OpenReview","url":"https://openreview.net/forum?id=VNckp7JEHn"},{"title":"[2408.00724v2] Inference Scaling Laws: An Empirical Analysis of Compute-Optimal Inference for Problem-Solving with Language Models","url":"https://arxiv.org/abs/2408.00724v2"},{"title":"Compute-Optimal Inference Scaling Laws","url":"https://www.emergentmind.com/papers/2408.00724"},{"title":"(PDF) An Empirical Analysis of Compute-Optimal Inference for Problem-Solving with Language Models","url":"https://www.researchgate.net/publication/382797048_An_Empirical_Analysis_of_Compute-Optimal_Inference_for_Problem-Solving_with_Language_Models"},{"title":"An Empirical Analysis of Compute-Optimal Inference for Problem-Solving with Language Models","url":"https://arxiv.org/html/2408.00724v1"},{"title":"Inference Scaling Laws: An Empirical Analysis of Compute-Optimal Inference for Problem-Solving with Language Models - ADS","url":"https://ui.adsabs.harvard.edu/abs/2024arXiv240800724W/abstract"},{"title":"GitHub - thu-wyz/inference_scaling","url":"https://github.com/thu-wyz/rebase"}]

I found the arXiv paper 2408.00724 for you. Here are the key details:

**Paper Title:** Inference Scaling Laws: An Empirical Analysis of Compute-Optimal Inference for Pr
…[truncated 1277 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_research_lit_batch3_20260514T182744",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 32 · 2026-05-14T18:31:18.152446+00:00_

Web search results for query: "Jagannatha Yu 2020 "Calibrating Structured Output Predictors for Natural Language Processing" ACL 2020"

Links: [{"title":"Calibrating Structured Output Predictors for Natural Language Processing - ACL Anthology","url":"https://aclanthology.org/2020.acl-main.188/"},{"title":"Calibrating Structured Output Predictors for Natural Language Processing - PMC","url":"https://pmc.ncbi.nlm.nih.gov/articles/PMC7890517/"},{"title":"[2004.04361] Calibrating Structured Output Predictors for Natural Language Processing","url":"https://arxiv.org/abs/2004.04361"},{"title":"[PDF] Calibrating Structured Output Predictors for Natural Language Processing | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Calibrating-Structured-Output-Predictors-for-Jagannatha-Yu/37710e4b0dd851bd0d9bc4994c3b32cb10279151"},{"title":"Calibrating Structured Output Predictors for Natural ...","url":"https://aclanthology.org/2020.acl-main.188.pdf"},{"title":"Calibrating Structured Output Predictors for Natural Language Processing | DeepAI","url":"https://deepai.org/publication/calibrating-structured-output-predictors-for-natural-language-processing"},{"title":"Reducing Conversational Agents’ Overconfidence Through Linguistic Calibration | Transactions of the Association for Computational Linguistics | MIT Press","url":"https://direct.mit.edu/tacl/article/doi/10.1162/tacl_a_00494/112606/Reducing-Conversational-Agents-Overconfidence"},{"title":"GitHub - ShiyuNee/Awesome-Calibration-Papers: A curated list of awesome papers about calibration · GitHub","url":"https://github.com/ShiyuNee/Awesome-Calibration-Papers"},{"title":"Modified reliability plots (Accuracy -Confidence vs Confidence) on MADE... | Download Scientific Diagram","url":"https://www.researchgate.net/figure/Modified-reliability-plots-Accuracy-Confidence-vs-Confidence-on-MADE-10-QA-test-The_fig3_340541539"},{"title":"(PDF) Unsupervised Calibration through Prior Adaptation for Text Classification using Larg
…[truncated 1509 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_research_lit_batch3_20260514T182744",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 33 · 2026-05-14T18:31:18.152627+00:00_

Web search results for query: "Wang et al 2024 "Math-Shepherd" verify reinforce LLMs step-by-step ACL 2024 arXiv"

Links: [{"title":"Math-Shepherd: Verify and Reinforce LLMs Step-by-step without Human Annotations - ACL Anthology","url":"https://aclanthology.org/2024.acl-long.510/"},{"title":"[2312.08935] Math-Shepherd: Verify and Reinforce LLMs Step-by-step without Human Annotations","url":"https://arxiv.org/abs/2312.08935"},{"title":"MATH-SHEPHERD: VERIFY AND REINFORCE LLMS STEP-BY-STEP WITHOUT HUMAN ANNOTATIONS","url":"https://arxiv.org/pdf/2312.08935"},{"title":"Math-Shepherd: Verify and Reinforce LLMs Step-by-step without Human Annotations | Request PDF","url":"https://www.researchgate.net/publication/384216875_Math-Shepherd_Verify_and_Reinforce_LLMs_Step-by-step_without_Human_Annotations"},{"title":"awesome-o1 | A bibliography and survey of the papers surrounding o1","url":"https://srush.github.io/awesome-o1/"},{"title":"arXiv:2501.07301v2 [cs.CL] 5 Jun 2025 2025-06-12","url":"https://arxiv.org/pdf/2501.07301"},{"title":"Improve Mathematical Reasoning in Language Models by ...","url":"https://arxiv.org/pdf/2406.06592"},{"title":"Improve Mathematical Reasoning in Language Models by Automated Process Supervision","url":"https://arxiv.org/html/2406.06592v2"},{"title":"[2312.08935v3] Math-Shepherd: Verify and Reinforce LLMs Step-by-step without Human Annotations","url":"https://arxiv.org/abs/2312.08935v3"},{"title":"Safe: Enhancing Mathematical Reasoning in Large Language Models via Retrospective Step-aware Formal Verification","url":"https://arxiv.org/html/2506.04592v1"}]

I found the paper! Here's the information about Wang et al. 2024 "Math-Shepherd":

## Paper Details

The paper "Math-Shepherd: Verify and Reinforce LLMs Step-by-step without Human Annotations" was authored by Peiyi Wang, Lei Li, Zhihong Shao, Runxin Xu, Damai Dai, Yifei Li, Deli Chen, Yu Wu, and Zhifang Sui in 2024, and published in the Proceedings of the 62nd Annual Meeting of the Association f
…[truncated 1208 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_research_lit_batch3_20260514T182744",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 34 · 2026-05-14T18:31:18.152791+00:00_

Web search results for query: "Varshney et al 2023 selective prediction NLP "Art of Saying No" OR "selective prediction" ACL EMNLP 2023 language model abstain"

Links: [{"title":"Selective Prediction in Natural Language Processing | by Neeraj Varshney | Medium","url":"https://medium.com/@nvarshney97/selective-prediction-in-natural-language-processing-838244f1e8e1"},{"title":"Selective-LAMA: Selective Prediction for Confidence-Aware Evaluation of Language Models","url":"https://www.researchgate.net/publication/373809616_Selective-LAMA_Selective_Prediction_for_Confidence-Aware_Evaluation_of_Language_Models"},{"title":"Towards Improving Selective Prediction Ability of NLP Systems - ACL Anthology","url":"https://aclanthology.org/2022.repl4nlp-1.23/"},{"title":"Neeraj Varshney","url":"https://nrjvarshney.github.io/"},{"title":"[PDF] Towards Improving Selective Prediction Ability of NLP Systems | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Towards-Improving-Selective-Prediction-Ability-of-Varshney-Mishra/a6449a63008bdc7d18db330322b3de293426f53b"},{"title":"arXiv:2305.01812v1 [cs.CL] 2 May 2023","url":"https://arxiv.org/pdf/2305.01812"},{"title":"Neeraj Varshney | Publications","url":"https://nrjvarshney.github.io/publications/index.html"},{"title":"[2203.00211] Investigating Selective Prediction Approaches Across Several Tasks in IID, OOD, and Adversarial Settings","url":"https://arxiv.org/abs/2203.00211"},{"title":"Adaptation with Self-Evaluation to Improve Selective Prediction in LLMs","url":"https://arxiv.org/pdf/2310.11689"},{"title":"[2008.09371] Towards Improving Selective Prediction Ability of NLP Systems","url":"https://arxiv.org/abs/2008.09371"}]

Based on the search results, I found relevant information about Varshney et al.'s work on selective prediction in NLP. Here are the key findings:

## Varshney et al. 2023 Publications on Selective Prediction

Varshney and Baral published "Post-Abstention: Towards Reliably Re-Attempting the Abstained I
…[truncated 1239 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_research_lit_batch3_20260514T182744",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 35 · 2026-05-14T18:31:18.152992+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Yoshikawa Okazaki 2023 \"Selective Prediction for Extractive Question Answering\" OR \"selective prediction\" EMNLP 2023 LLM confidence abstain NER"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_research_lit_batch3_20260514T182744",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Yoshikawa Okazaki 2023 \"Selective Prediction for Extractive Question Answering\" OR \"selective prediction\" EMNLP 2023 LLM confidence abstain NER"
  }
}
```

</details>

---

### Tool result

_source line 36 · 2026-05-14T18:31:18.153364+00:00_

Web search results for query: "Yoshikawa Okazaki 2023 "Selective Prediction for Extractive Question Answering" OR "selective prediction" EMNLP 2023 LLM confidence abstain NER"

Links: [{"title":"Findings - EMNLP 2023","url":"https://2023.emnlp.org/program/accepted_findings/"},{"title":"Selective-LAMA: Selective Prediction for Confidence-Aware Evaluation of Language Models","url":"https://www.researchgate.net/publication/373809616_Selective-LAMA_Selective_Prediction_for_Confidence-Aware_Evaluation_of_Language_Models"},{"title":"[PDF] Selective-LAMA: Selective Prediction for Confidence-Aware Evaluation of Language Models | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Selective-LAMA:-Selective-Prediction-for-Evaluation-Yoshikawa-Okazaki/b195b707dc54fab51ae22a0cd7511e151b6533f4"},{"title":"Selective-LAMA: Selective Prediction for Confidence-Aware Evaluation of Language Models - ACL Anthology","url":"https://aclanthology.org/2023.findings-eacl.150/"},{"title":"Paper at EMNLP 2023 | Okazaki Laboratory at Tokyo Institute of Technology","url":"https://www.nlp.c.titech.ac.jp/news/2023/10/09/emnlp2023.en.html"},{"title":"Know Your Limits: A Survey of Abstention in Large Language Models | Transactions of the Association for Computational Linguistics | MIT Press","url":"https://direct.mit.edu/tacl/article/doi/10.1162/tacl_a_00754/131566/Know-Your-Limits-A-Survey-of-Abstention-in-Large"},{"title":"Causal Reasoning through Two Cognition Layers for Improving Generalization in Visual Question Answering - ACL Anthology","url":"https://aclanthology.org/2023.emnlp-main.573/"},{"title":"Publications | Okazaki Laboratory at Tokyo Institute of Technology","url":"https://www.nlp.c.titech.ac.jp/publications.en.html"},{"title":"Adaptation with Self-Evaluation to Improve Selective ...","url":"https://aclanthology.org/2023.findings-emnlp.345.pdf"},{"title":"Google at EMNLP 2023","url":"https://research.google/blog/google-at-emnlp-2023/"}]

Based on the search results, I foun
…[truncated 1239 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_research_lit_batch3_20260514T182744",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 37 · 2026-05-14T18:31:18.153537+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Ren et al 2023 \"self-evaluation improves selective generation\" OR Kadavath selective prediction LLM 2023 2024 NeurIPS ICLR"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_research_lit_batch3_20260514T182744",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Ren et al 2023 \"self-evaluation improves selective generation\" OR Kadavath selective prediction LLM 2023 2024 NeurIPS ICLR"
  }
}
```

</details>

---

### Tool result

_source line 38 · 2026-05-14T18:31:18.153718+00:00_

Web search results for query: "Ren et al 2023 "self-evaluation improves selective generation" OR Kadavath selective prediction LLM 2023 2024 NeurIPS ICLR"

Links: [{"title":"Self-Evaluation Improves Selective Generation in Large Language Models","url":"https://proceedings.mlr.press/v239/ren23a.html"},{"title":"Self-Evaluation Improves Selective Generation in Large Language Models","url":"https://arxiv.org/pdf/2312.09300"},{"title":"[PDF] Self-Evaluation Improves Selective Generation in Large Language Models | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Self-Evaluation-Improves-Selective-Generation-in-Ren-Zhao/04365f0f1db4c659c3297cb8e70c39b38ed3b487"},{"title":"[2312.09300] Self-Evaluation Improves Selective Generation in Large Language Models","url":"https://arxiv.org/abs/2312.09300"},{"title":"Self-Alignment for Factuality: Mitigating Hallucinations in LLMs via Self-Evaluation","url":"https://arxiv.org/html/2402.09267v2"},{"title":"NeurIPS Self-Evaluation Improves Selective Generation in Large Language Models","url":"https://neurips.cc/virtual/2023/76522"},{"title":"Self-Evaluation Improves Selective Generation in Large Language Models - ADS","url":"https://ui.adsabs.harvard.edu/abs/2023arXiv231209300R/abstract"},{"title":"fly51fly on X: \"[CL] Self-Evaluation Improves Selective Generation in Large Language Models J Ren, Y Zhao, T Vu, P J. Liu, B Lakshminarayanan [Google DeepMind &amp; Google Research] (2023) https://t.co/S2SygkPsUW - Large language models (LLMs) like GPT-3 have limitations in using sequence-level https://t.co/H2zOLbA0tO\" / X","url":"https://x.com/fly51fly/status/1736616954163548326"},{"title":"Steering Large Language Models to Evaluate and Amplify Creativity","url":"https://arxiv.org/html/2412.06060v1"},{"title":"A Survey of Calibration Process for Black-Box LLMs","url":"https://arxiv.org/html/2412.12767v1"}]

Links: [{"title":"Under review as a conference paper at ICLR 2024 GENERATING WITH CONFIDENCE:","url":"https://openrevi
…[truncated 3619 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_research_lit_batch3_20260514T182744",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 39 · 2026-05-14T18:31:18.153948+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/literature_map.yaml",
  "old_string": "  last_updated: '2026-05-14T18:10:52.000Z'\n  total_papers: 30",
  "new_string": "  last_updated: '2026-05-14T19:30:00.000Z'\n  total_papers: 41"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_research_lit_batch3_20260514T182744",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/literature_map.yaml",
    "old_string": "  last_updated: '2026-05-14T18:10:52.000Z'\n  total_papers: 30",
    "new_string": "  last_updated: '2026-05-14T19:30:00.000Z'\n  total_papers: 41"
  }
}
```

</details>

---

### Tool result

_source line 40 · 2026-05-14T18:31:18.154182+00:00_

The file /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/literature_map.yaml has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_research_lit_batch3_20260514T182744",
  "tool": "Edit",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 41 · 2026-05-14T18:31:18.154359+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/literature_map.yaml",
  "old_string": "    added_by: paper-research:lit_batch2\n    added_at: '2026-05-14T18:10:52.000Z'",
  "new_string": "    added_by: paper-research:lit_batch2\n    added_at: '2026-05-14T18:10:52.000Z'\n  cobbe2021verifiers:\n    title: Training Verifiers to Solve Math Word Problems\n    authors:\n    - Karl Cobbe\n    - Vineet Kosaraju\n    - Mohammad Bavarian\n    - Mark Chen\n    - Heewoo Jun\n    - Lukasz Kaiser\n    - Matthias Plappert\n    - Jerry Tworek\n    - Jacob Hilton\n    - Reiichiro Nakano\n    - Christopher Hesse\n    - John Schulman\n    year: 2021\n    venue: arXiv preprint\n    url: https://arxiv.org/abs/2110.14168\n    doi: ''\n    bibtex_key: cobbe2021verifiers\n    category: verifier_reward_models\n    role: foundation\n    relevance: 'Foundation paper: introduces training outcome-based verifiers (ORM) for math word problems and the GSM8K benchmark.\n      Establishes the verify-then-select paradigm our method builds upon.'\n    abstract: ''\n    semantic_scholar_id: ''\n    verified: true\n    added_by: paper-research:lit_batch3\n    added_at: '2026-05-14T19:30:00.000Z'\n  lightman2024verify:\n    title: Let's Verify Step by Step\n    authors:\n    - Hunter Lightman\n    - Vineet Kosaraju\n    - Yura Burda\n    - Harri Edwards\n    - Bowen Baker\n    - Teddy Lee\n    - Jan Leike\n    - John Schulman\n    - Ilya Sutskever\n    - Karl Cobbe\n    year: 2024\n    venue: ICLR 2024\n    url: https://arxiv.org/abs/2305.20050\n    doi: ''\n    bibtex_key: lightman2024verify\n    category: verifier_reward_models\n    role: foundation\n    relevance: 'Foundation paper: demonstrates process reward models (PRMs) with step-level supervision outperform outcome-based\n      verification. Key motivation for fine-grained quality signals in our structured IE aggregation.'\n    abstract: ''\n    semantic_scholar_id: ''\n    verified: true\n    added_by: paper-research:lit_batch3\n    added_at: '2026-05-14T19:30:00.000Z'\n  wang2024mathshepherd:\n    title: 'Math-Shepherd: Verify and Reinforce LLMs Step-by-step without Human Annotations'\n    authors:\n    - Peiyi Wang\n    - Lei Li\n    - Zhihong Shao\n    - Runxin Xu\n    - Damai Dai\n    - Yifei Li\n    - Deli Chen\n    - Yu Wu\n    - Zhifang Sui\n    year: 2024\n    venue: ACL 2024\n    url: https://arxiv.org/abs/2312.08935\n    doi: ''\n    bibtex_key: wang2024mathshepherd\n    category: verifier_reward_models\n    role: background\n    relevance: Automated process reward model construction without human annotations, enabling step-level verification at scale.\n      Demonstrates ORM/PRM effectiveness for both reranking and reinforcement learning.\n    abstract: ''\n    semantic_scholar_id: ''\n    verified: true\n    added_by: paper-research:lit_batch3\n    added_at: '2026-05-14T19:30:00.000Z'\n  snell2024scaling:\n    title: Scaling LLM Test-Time Compute Optimally can be More Effective than Scaling Model Parameters\n    authors:\n    - Charlie Snell\n    - Jaehoon Lee\n    - Kelvin Xu\n    - Aviral Kumar\n    year: 2024\n    venue: ICLR 2025\n    url: https://arxiv.org/abs/2408.03314\n    doi: ''\n    bibtex_key: snell2024scaling\n    category: tts_scaling\n    role: foundation\n    relevance: 'Foundation paper: introduces compute-optimal test-time scaling, showing adaptive per-prompt compute allocation\n      improves efficiency 4x over best-of-N. Directly motivates our adaptive sampling strategy.'\n    abstract: ''\n    semantic_scholar_id: ''\n    verified: true\n    added_by: paper-research:lit_batch3\n    added_at: '2026-05-14T19:30:00.000Z'\n  brown2024monkeys:\n    title: 'Large Language Monkeys: Scaling Inference Compute with Repeated Sampling'\n    authors:\n    - Bradley Brown\n    - Jordan Juravsky\n    - Ryan Ehrlich\n    - Ronald Clark\n    - Quoc V. Le\n    - Christopher Ré\n    - Azalia Mirhoseini\n    year: 2024\n    venue: arXiv preprint\n    url: https://arxiv.org/abs/2407.21787\n    doi: ''\n    bibtex_key: brown2024monkeys\n    category: tts_scaling\n    role: foundation\n    relevance: 'Foundation paper: demonstrates log-linear scaling of coverage with repeated sampling across tasks, establishing\n      inference-time scaling laws. Motivates our multi-sample approach for structured IE.'\n    abstract: ''\n    semantic_scholar_id: ''\n    verified: true\n    added_by: paper-research:lit_batch3\n    added_at: '2026-05-14T19:30:00.000Z'\n  wu2024inference:\n    title: 'Inference Scaling Laws: An Empirical Analysis of Compute-Optimal Inference for Problem-Solving with Language Models'\n    authors:\n    - Yangzhen Wu\n    - Zhiqing Sun\n    - Shanda Li\n    - Sean Welleck\n    - Yiming Yang\n    year: 2024\n    venue: arXiv preprint\n    url: https://arxiv.org/abs/2408.00724\n    doi: ''\n    bibtex_key: wu2024inference\n    category: tts_scaling\n    role: background\n    relevance: Empirical analysis of compute-optimal inference strategies showing smaller models with advanced inference algorithms\n      achieve Pareto-optimal cost-performance trade-offs. Complements our efficiency analysis.\n    abstract: ''\n    semantic_scholar_id: ''\n    verified: true\n    added_by: paper-research:lit_batch3\n    added_at: '2026-05-14T19:30:00.000Z'\n  kuleshov2015calibrated:\n    title: Calibrated Structured Prediction\n    authors:\n    - Volodymyr Kuleshov\n    - Percy Liang\n    year: 2015\n    venue: NeurIPS 2015\n    url: https://proceedings.neurips.cc/paper/2015/hash/52d2752b150f9c35ccb6869cbf074e48-Abstract.html\n    doi: ''\n    bibtex_key: kuleshov2015calibrated\n    category: structured_calibration_ie\n    role: foundation\n    relevance: 'Foundation paper: extends calibration to structured prediction with formal guarantees, proposing recalibration\n      methods for marginal and conditional queries. Theoretical basis for calibrated structured IE.'\n    abstract: ''\n    semantic_scholar_id: ''\n    verified: true\n    added_by: paper-research:lit_batch3\n    added_at: '2026-05-14T19:30:00.000Z'\n  culotta2004confidence:\n    title: Confidence Estimation for Information Extraction\n    authors:\n    - Aron Culotta\n    - Andrew McCallum\n    year: 2004\n    venue: HLT-NAACL 2004\n    url: https://aclanthology.org/N04-4028/\n    doi: ''\n    bibtex_key: culotta2004confidence\n    category: structured_calibration_ie\n    role: foundation\n    relevance: 'Foundation paper: pioneers confidence estimation for CRF-based information extraction at both field and record\n      levels. Establishes the problem setting our LLM-based approach addresses.'\n    abstract: ''\n    semantic_scholar_id: ''\n    verified: true\n    added_by: paper-research:lit_batch3\n    added_at: '2026-05-14T19:30:00.000Z'\n  jagannatha2020calibrating:\n    title: Calibrating Structured Output Predictors for Natural Language Processing\n    authors:\n    - Abhyuday Jagannatha\n    - Hong Yu\n    year: 2020\n    venue: ACL 2020\n    url: https://aclanthology.org/2020.acl-main.188/\n    doi: ''\n    bibtex_key: jagannatha2020calibrating\n    category: structured_calibration_ie\n    role: background\n    relevance: Proposes general calibration scheme for neural structured prediction models in NLP including NER and QA. Bridges\n      classical calibration methods to modern neural IE, directly relevant to our structured output calibration.\n    abstract: ''\n    semantic_scholar_id: ''\n    verified: true\n    added_by: paper-research:lit_batch3\n    added_at: '2026-05-14T19:30:00.000Z'\n  geifman2017selective:\n    title: Selective Classification for Deep Neural Networks\n    authors:\n    - Yonatan Geifman\n    - Ran El-Yaniv\n    year: 2017\n    venue: NeurIPS 2017\n    url: https://arxiv.org/abs/1705.08500\n    doi: ''\n    bibtex_key: geifman2017selective\n    category: selective_prediction\n    role: foundation\n    relevance: 'Foundation paper: introduces selective classification framework for DNNs with guaranteed risk control at specified\n      coverage levels. Theoretical foundation for our consistency-based selective prediction in IE.'\n    abstract: ''\n    semantic_scholar_id: ''\n    verified: true\n    added_by: paper-research:lit_batch3\n    added_at: '2026-05-14T19:30:00.000Z'\n  ren2023selfevaluation:\n    title: Self-Evaluation Improves Selective Generation in Large Language Models\n    authors:\n    - Jie Ren\n    - Yao Zhao\n    - Tu Vu\n    - Peter J. Liu\n    - Balaji Lakshminarayanan\n    year: 2023\n    venue: NeurIPS 2023 Workshop\n    url: https://arxiv.org/abs/2312.09300\n    doi: ''\n    bibtex_key: ren2023selfevaluation\n    category: selective_prediction\n    role: background\n    relevance: Proposes LLM self-evaluation for selective generation, reformulating open-ended tasks into token-level predictions\n      to leverage better calibration. Directly relevant to our confidence-aware abstention mechanism for structured IE.\n    abstract: ''\n    semantic_scholar_id: ''\n    verified: true\n    added_by: paper-research:lit_batch3\n    added_at: '2026-05-14T19:30:00.000Z'"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_research_lit_batch3_20260514T182744",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/literature_map.yaml",
    "old_string": "    added_by: paper-research:lit_batch2\n    added_at: '2026-05-14T18:10:52.000Z'",
    "new_string": "    added_by: paper-research:lit_batch2\n    added_at: '2026-05-14T18:10:52.000Z'\n  cobbe2021verifiers:\n    title: Training Verifiers to Solve Math Word Problems\n    authors:\n    - Karl Cobbe\n    - Vineet Kosaraju\n    - Mohammad Bavarian\n    - Mark Chen\n    - Heewoo Jun\n    - Lukasz Kaiser\n    - Matthias Plappert\n    - Jerry Tworek\n    - Jacob Hilton\n    - Reiichiro Nakano\n    - Christopher Hesse\n    - John Schulman\n    year: 2021\n    venue: arXiv preprint\n    url: https://arxiv.org/abs/2110.14168\n    doi: ''\n    bibtex_key: cobbe2021verifiers\n    category: verifier_reward_models\n    role: foundation\n    relevance: 'Foundation paper: introduces training outcome-based verifiers (ORM) for math word problems and the GSM8K benchmark.\n      Establishes the verify-then-select paradigm our method builds upon.'\n    abstract: ''\n    semantic_scholar_id: ''\n    verified: true\n    added_by: paper-research:lit_batch3\n    added_at: '2026-05-14T19:30:00.000Z'\n  lightman2024verify:\n    title: Let's Verify Step by Step\n    authors:\n    - Hunter Lightman\n    - Vineet Kosaraju\n    - Yura Burda\n    - Harri Edwards\n    - Bowen Baker\n    - Teddy Lee\n    - Jan Leike\n    - John Schulman\n    - Ilya Sutskever\n    - Karl Cobbe\n    year: 2024\n    venue: ICLR 2024\n    url: https://arxiv.org/abs/2305.20050\n    doi: ''\n    bibtex_key: lightman2024verify\n    category: verifier_reward_models\n    role: foundation\n    relevance: 'Foundation paper: demonstrates process reward models (PRMs) with step-level supervision outperform outcome-based\n      verification. Key motivation for fine-grained quality signals in our structured IE aggregation.'\n    abstract: ''\n    semantic_scholar_id: ''\n    verified: true\n    added_by: paper-research:lit_batch3\n    added_at: '2026-05-14T19:30:00.000Z'\n  wang2024mathshepherd:\n    title: 'Math-Shepherd: Verify and Reinforce LLMs Step-by-step without Human Annotations'\n    authors:\n    - Peiyi Wang\n    - Lei Li\n    - Zhihong Shao\n    - Runxin Xu\n    - Damai Dai\n    - Yifei Li\n    - Deli Chen\n    - Yu Wu\n    - Zhifang Sui\n    year: 2024\n    venue: ACL 2024\n    url: https://arxiv.org/abs/2312.08935\n    doi: ''\n    bibtex_key: wang2024mathshepherd\n    category: verifier_reward_models\n    role: background\n    relevance: Automated process reward model construction without human annotations, enabling step-level verification at scale.\n      Demonstrates ORM/PRM effectiveness for both reranking and reinforcement learning.\n    abstract: ''\n    semantic_scholar_id: ''\n    verified: true\n    added_by: paper-research:lit_batch3\n    added_at: '2026-05-14T19:30:00.000Z'\n  snell2024scaling:\n    title: Scaling LLM Test-Time Compute Optimally can be More Effective than Scaling Model Parameters\n    authors:\n    - Charlie Snell\n    - Jaehoon Lee\n    - Kelvin Xu\n    - Aviral Kumar\n    year: 2024\n    venue: ICLR 2025\n    url: https://arxiv.org/abs/2408.03314\n    doi: ''\n    bibtex_key: snell2024scaling\n    category: tts_scaling\n    role: foundation\n    relevance: 'Foundation paper: introduces compute-optimal test-time scaling, showing adaptive per-prompt compute allocation\n      improves efficiency 4x over best-of-N. Directly motivates our adaptive sampling strategy.'\n    abstract: ''\n    semantic_scholar_id: ''\n    verified: true\n    added_by: paper-research:lit_batch3\n    added_at: '2026-05-14T19:30:00.000Z'\n  brown2024monkeys:\n    title: 'Large Language Monkeys: Scaling Inference Compute with Repeated Sampling'\n    authors:\n    - Bradley Brown\n    - Jordan Juravsky\n    - Ryan Ehrlich\n    - Ronald Clark\n    - Quoc V. Le\n    - Christopher Ré\n    - Azalia Mirhoseini\n    year: 2024\n    venue: arXiv preprint\n    url: https://arxiv.org/abs/2407.21787\n    doi: ''\n    bibtex_key: brown2024monkeys\n    category: tts_scaling\n    role: foundation\n    relevance: 'Foundation paper: demonstrates log-linear scaling of coverage with repeated sampling across tasks, establishing\n      inference-time scaling laws. Motivates our multi-sample approach for structured IE.'\n    abstract: ''\n    semantic_scholar_id: ''\n    verified: true\n    added_by: paper-research:lit_batch3\n    added_at: '2026-05-14T19:30:00.000Z'\n  wu2024inference:\n    title: 'Inference Scaling Laws: An Empirical Analysis of Compute-Optimal Inference for Problem-Solving with Language Models'\n    authors:\n    - Yangzhen Wu\n    - Zhiqing Sun\n    - Shanda Li\n    - Sean Welleck\n    - Yiming Yang\n    year: 2024\n    venue: arXiv preprint\n    url: https://arxiv.org/abs/2408.00724\n    doi: ''\n    bibtex_key: wu2024inference\n    category: tts_scaling\n    role: background\n    relevance: Empirical analysis of compute-optimal inference strategies showing smaller models with advanced inference algorithms\n      achieve Pareto-optimal cost-performance trade-offs. Complements our efficiency analysis.\n    abstract: ''\n    semantic_scholar_id: ''\n    verified: true\n    added_by: paper-research:lit_batch3\n    added_at: '2026-05-14T19:30:00.000Z'\n  kuleshov2015calibrated:\n    title: Calibrated Structured Prediction\n    authors:\n    - Volodymyr Kuleshov\n    - Percy Liang\n    year: 2015\n    venue: NeurIPS 2015\n    url: https://proceedings.neurips.cc/paper/2015/hash/52d2752b150f9c35ccb6869cbf074e48-Abstract.html\n    doi: ''\n    bibtex_key: kuleshov2015calibrated\n    category: structured_calibration_ie\n    role: foundation\n    relevance: 'Foundation paper: extends calibration to structured prediction with formal guarantees, proposing recalibration\n      methods for marginal and conditional queries. Theoretical basis for calibrated structured IE.'\n    abstract: ''\n    semantic_scholar_id: ''\n    verified: true\n    added_by: paper-research:lit_batch3\n    added_at: '2026-05-14T19:30:00.000Z'\n  culotta2004confidence:\n    title: Confidence Estimation for Information Extraction\n    authors:\n    - Aron Culotta\n    - Andrew McCallum\n    year: 2004\n    venue: HLT-NAACL 2004\n    url: https://aclanthology.org/N04-4028/\n    doi: ''\n    bibtex_key: culotta2004confidence\n    category: structured_calibration_ie\n    role: foundation\n    relevance: 'Foundation paper: pioneers confidence estimation for CRF-based information extraction at both field and record\n      levels. Establishes the problem setting our LLM-based approach addresses.'\n    abstract: ''\n    semantic_scholar_id: ''\n    verified: true\n    added_by: paper-research:lit_batch3\n    added_at: '2026-05-14T19:30:00.000Z'\n  jagannatha2020calibrating:\n    title: Calibrating Structured Output Predictors for Natural Language Processing\n    authors:\n    - Abhyuday Jagannatha\n    - Hong Yu\n    year: 2020\n    venue: ACL 2020\n    url: https://aclanthology.org/2020.acl-main.188/\n    doi: ''\n    bibtex_key: jagannatha2020calibrating\n    category: structured_calibration_ie\n    role: background\n    relevance: Proposes general calibration scheme for neural structured prediction models in NLP including NER and QA. Bridges\n      classical calibration methods to modern neural IE, directly relevant to our structured output calibration.\n    abstract: ''\n    semantic_scholar_id: ''\n    verified: true\n    added_by: paper-research:lit_batch3\n    added_at: '2026-05-14T19:30:00.000Z'\n  geifman2017selective:\n    title: Selective Classification for Deep Neural Networks\n    authors:\n    - Yonatan Geifman\n    - Ran El-Yaniv\n    year: 2017\n    venue: NeurIPS 2017\n    url: https://arxiv.org/abs/1705.08500\n    doi: ''\n    bibtex_key: geifman2017selective\n    category: selective_prediction\n    role: foundation\n    relevance: 'Foundation paper: introduces selective classification framework for DNNs with guaranteed risk control at specified\n      coverage levels. Theoretical foundation for our consistency-based selective prediction in IE.'\n    abstract: ''\n    semantic_scholar_id: ''\n    verified: true\n    added_by: paper-research:lit_batch3\n    added_at: '2026-05-14T19:30:00.000Z'\n  ren2023selfevaluation:\n    title: Self-Evaluation Improves Selective Generation in Large Language Models\n    authors:\n    - Jie Ren\n    - Yao Zhao\n    - Tu Vu\n    - Peter J. Liu\n    - Balaji Lakshminarayanan\n    year: 2023\n    venue: NeurIPS 2023 Workshop\n    url: https://arxiv.org/abs/2312.09300\n    doi: ''\n    bibtex_key: ren2023selfevaluation\n    category: selective_prediction\n    role: background\n    relevance: Proposes LLM self-evaluation for selective generation, reformulating open-ended tasks into token-level predictions\n      to leverage better calibration. Directly relevant to our confidence-aware abstention mechanism for structured IE.\n    abstract: ''\n    semantic_scholar_id: ''\n    verified: true\n    added_by: paper-research:lit_batch3\n    added_at: '2026-05-14T19:30:00.000Z'"
  }
}
```

</details>

---

### Tool result

_source line 42 · 2026-05-14T18:31:18.154563+00:00_

&lt;tool_use_error>Found 9 matches of the string to replace, but replace_all is false. To replace all occurrences, set replace_all to true. To replace only one occurrence, please provide more context to uniquely identify the instance.
String:     added_by: paper-research:lit_batch2
    added_at: '2026-05-14T18:10:52.000Z'&lt;/tool_use_error>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_research_lit_batch3_20260514T182744",
  "tool": "Edit",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 43 · 2026-05-14T18:31:18.154712+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/literature_map.yaml",
  "offset": "690",
  "limit": "20"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_research_lit_batch3_20260514T182744",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/literature_map.yaml",
    "offset": "690",
    "limit": "20"
  }
}
```

</details>

---

### Tool result

_source line 44 · 2026-05-14T18:31:18.154842+00:00_

690	    year: 2020
691	    venue: TACL 2020
692	    url: https://arxiv.org/abs/2005.10608
693	    doi: 10.1162/tacl_a_00330
694	    bibtex_key: fomicheva2020unsupervised
695	    category: ensemble_mc_dropout
696	    role: background
697	    relevance: Applies MC dropout and ensemble-based uncertainty to NLP (MT quality estimation) without supervision, achieving
698	      strong correlation with human judgments. Key precedent for unsupervised uncertainty signals in NLP generation tasks.
699	    abstract: ''
700	    semantic_scholar_id: ''
701	    verified: true
702	    added_by: paper-research:lit_batch2
703	    added_at: '2026-05-14T18:10:52.000Z'
704	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_research_lit_batch3_20260514T182744",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 45 · 2026-05-14T18:31:18.155000+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/literature_map.yaml",
  "old_string": "    bibtex_key: fomicheva2020unsupervised\n    category: ensemble_mc_dropout\n    role: background\n    relevance: Applies MC dropout and ensemble-based uncertainty to NLP (MT quality estimation) without supervision, achieving\n      strong correlation with human judgments. Key precedent for unsupervised uncertainty signals in NLP generation tasks.\n    abstract: ''\n    semantic_scholar_id: ''\n    verified: true\n    added_by: paper-research:lit_batch2\n    added_at: '2026-05-14T18:10:52.000Z'",
  "new_string": "    bibtex_key: fomicheva2020unsupervised\n    category: ensemble_mc_dropout\n    role: background\n    relevance: Applies MC dropout and ensemble-based uncertainty to NLP (MT quality estimation) without supervision, achieving\n      strong correlation with human judgments. Key precedent for unsupervised uncertainty signals in NLP generation tasks.\n    abstract: ''\n    semantic_scholar_id: ''\n    verified: true\n    added_by: paper-research:lit_batch2\n    added_at: '2026-05-14T18:10:52.000Z'\n  cobbe2021verifiers:\n    title: Training Verifiers to Solve Math Word Problems\n    authors:\n    - Karl Cobbe\n    - Vineet Kosaraju\n    - Mohammad Bavarian\n    - Mark Chen\n    - Heewoo Jun\n    - Lukasz Kaiser\n    - Matthias Plappert\n    - Jerry Tworek\n    - Jacob Hilton\n    - Reiichiro Nakano\n    - Christopher Hesse\n    - John Schulman\n    year: 2021\n    venue: arXiv preprint\n    url: https://arxiv.org/abs/2110.14168\n    doi: ''\n    bibtex_key: cobbe2021verifiers\n    category: verifier_reward_models\n    role: foundation\n    relevance: 'Foundation paper: introduces training outcome-based verifiers (ORM) for math word problems and the GSM8K benchmark.\n      Establishes the verify-then-select paradigm our method builds upon.'\n    abstract: ''\n    semantic_scholar_id: ''\n    verified: true\n    added_by: paper-research:lit_batch3\n    added_at: '2026-05-14T19:30:00.000Z'\n  lightman2024verify:\n    title: Let's Verify Step by Step\n    authors:\n    - Hunter Lightman\n    - Vineet Kosaraju\n    - Yura Burda\n    - Harri Edwards\n    - Bowen Baker\n    - Teddy Lee\n    - Jan Leike\n    - John Schulman\n    - Ilya Sutskever\n    - Karl Cobbe\n    year: 2024\n    venue: ICLR 2024\n    url: https://arxiv.org/abs/2305.20050\n    doi: ''\n    bibtex_key: lightman2024verify\n    category: verifier_reward_models\n    role: foundation\n    relevance: 'Foundation paper: demonstrates process reward models (PRMs) with step-level supervision outperform outcome-based\n      verification. Key motivation for fine-grained quality signals in our structured IE aggregation.'\n    abstract: ''\n    semantic_scholar_id: ''\n    verified: true\n    added_by: paper-research:lit_batch3\n    added_at: '2026-05-14T19:30:00.000Z'\n  wang2024mathshepherd:\n    title: 'Math-Shepherd: Verify and Reinforce LLMs Step-by-step without Human Annotations'\n    authors:\n    - Peiyi Wang\n    - Lei Li\n    - Zhihong Shao\n    - Runxin Xu\n    - Damai Dai\n    - Yifei Li\n    - Deli Chen\n    - Yu Wu\n    - Zhifang Sui\n    year: 2024\n    venue: ACL 2024\n    url: https://arxiv.org/abs/2312.08935\n    doi: ''\n    bibtex_key: wang2024mathshepherd\n    category: verifier_reward_models\n    role: background\n    relevance: Automated process reward model construction without human annotations, enabling step-level verification at scale.\n      Demonstrates ORM/PRM effectiveness for both reranking and reinforcement learning.\n    abstract: ''\n    semantic_scholar_id: ''\n    verified: true\n    added_by: paper-research:lit_batch3\n    added_at: '2026-05-14T19:30:00.000Z'\n  snell2024scaling:\n    title: Scaling LLM Test-Time Compute Optimally can be More Effective than Scaling Model Parameters\n    authors:\n    - Charlie Snell\n    - Jaehoon Lee\n    - Kelvin Xu\n    - Aviral Kumar\n    year: 2024\n    venue: ICLR 2025\n    url: https://arxiv.org/abs/2408.03314\n    doi: ''\n    bibtex_key: snell2024scaling\n    category: tts_scaling\n    role: foundation\n    relevance: 'Foundation paper: introduces compute-optimal test-time scaling, showing adaptive per-prompt compute allocation\n      improves efficiency 4x over best-of-N. Directly motivates our adaptive sampling strategy.'\n    abstract: ''\n    semantic_scholar_id: ''\n    verified: true\n    added_by: paper-research:lit_batch3\n    added_at: '2026-05-14T19:30:00.000Z'\n  brown2024monkeys:\n    title: 'Large Language Monkeys: Scaling Inference Compute with Repeated Sampling'\n    authors:\n    - Bradley Brown\n    - Jordan Juravsky\n    - Ryan Ehrlich\n    - Ronald Clark\n    - Quoc V. Le\n    - Christopher Ré\n    - Azalia Mirhoseini\n    year: 2024\n    venue: arXiv preprint\n    url: https://arxiv.org/abs/2407.21787\n    doi: ''\n    bibtex_key: brown2024monkeys\n    category: tts_scaling\n    role: foundation\n    relevance: 'Foundation paper: demonstrates log-linear scaling of coverage with repeated sampling across tasks, establishing\n      inference-time scaling laws. Motivates our multi-sample approach for structured IE.'\n    abstract: ''\n    semantic_scholar_id: ''\n    verified: true\n    added_by: paper-research:lit_batch3\n    added_at: '2026-05-14T19:30:00.000Z'\n  wu2024inference:\n    title: 'Inference Scaling Laws: An Empirical Analysis of Compute-Optimal Inference for Problem-Solving with Language Models'\n    authors:\n    - Yangzhen Wu\n    - Zhiqing Sun\n    - Shanda Li\n    - Sean Welleck\n    - Yiming Yang\n    year: 2024\n    venue: arXiv preprint\n    url: https://arxiv.org/abs/2408.00724\n    doi: ''\n    bibtex_key: wu2024inference\n    category: tts_scaling\n    role: background\n    relevance: Empirical analysis of compute-optimal inference strategies showing smaller models with advanced inference algorithms\n      achieve Pareto-optimal cost-performance trade-offs. Complements our efficiency analysis.\n    abstract: ''\n    semantic_scholar_id: ''\n    verified: true\n    added_by: paper-research:lit_batch3\n    added_at: '2026-05-14T19:30:00.000Z'\n  kuleshov2015calibrated:\n    title: Calibrated Structured Prediction\n    authors:\n    - Volodymyr Kuleshov\n    - Percy Liang\n    year: 2015\n    venue: NeurIPS 2015\n    url: https://proceedings.neurips.cc/paper/2015/hash/52d2752b150f9c35ccb6869cbf074e48-Abstract.html\n    doi: ''\n    bibtex_key: kuleshov2015calibrated\n    category: structured_calibration_ie\n    role: foundation\n    relevance: 'Foundation paper: extends calibration to structured prediction with formal guarantees, proposing recalibration\n      methods for marginal and conditional queries. Theoretical basis for calibrated structured IE.'\n    abstract: ''\n    semantic_scholar_id: ''\n    verified: true\n    added_by: paper-research:lit_batch3\n    added_at: '2026-05-14T19:30:00.000Z'\n  culotta2004confidence:\n    title: Confidence Estimation for Information Extraction\n    authors:\n    - Aron Culotta\n    - Andrew McCallum\n    year: 2004\n    venue: HLT-NAACL 2004\n    url: https://aclanthology.org/N04-4028/\n    doi: ''\n    bibtex_key: culotta2004confidence\n    category: structured_calibration_ie\n    role: foundation\n    relevance: 'Foundation paper: pioneers confidence estimation for CRF-based information extraction at both field and record\n      levels. Establishes the problem setting our LLM-based approach addresses.'\n    abstract: ''\n    semantic_scholar_id: ''\n    verified: true\n    added_by: paper-research:lit_batch3\n    added_at: '2026-05-14T19:30:00.000Z'\n  jagannatha2020calibrating:\n    title: Calibrating Structured Output Predictors for Natural Language Processing\n    authors:\n    - Abhyuday Jagannatha\n    - Hong Yu\n    year: 2020\n    venue: ACL 2020\n    url: https://aclanthology.org/2020.acl-main.188/\n    doi: ''\n    bibtex_key: jagannatha2020calibrating\n    category: structured_calibration_ie\n    role: background\n    relevance: Proposes general calibration scheme for neural structured prediction models in NLP including NER and QA. Bridges\n      classical calibration methods to modern neural IE, directly relevant to our structured output calibration.\n    abstract: ''\n    semantic_scholar_id: ''\n    verified: true\n    added_by: paper-research:lit_batch3\n    added_at: '2026-05-14T19:30:00.000Z'\n  geifman2017selective:\n    title: Selective Classification for Deep Neural Networks\n    authors:\n    - Yonatan Geifman\n    - Ran El-Yaniv\n    year: 2017\n    venue: NeurIPS 2017\n    url: https://arxiv.org/abs/1705.08500\n    doi: ''\n    bibtex_key: geifman2017selective\n    category: selective_prediction\n    role: foundation\n    relevance: 'Foundation paper: introduces selective classification framework for DNNs with guaranteed risk control at specified\n      coverage levels. Theoretical foundation for our consistency-based selective prediction in IE.'\n    abstract: ''\n    semantic_scholar_id: ''\n    verified: true\n    added_by: paper-research:lit_batch3\n    added_at: '2026-05-14T19:30:00.000Z'\n  ren2023selfevaluation:\n    title: Self-Evaluation Improves Selective Generation in Large Language Models\n    authors:\n    - Jie Ren\n    - Yao Zhao\n    - Tu Vu\n    - Peter J. Liu\n    - Balaji Lakshminarayanan\n    year: 2023\n    venue: NeurIPS 2023 Workshop\n    url: https://arxiv.org/abs/2312.09300\n    doi: ''\n    bibtex_key: ren2023selfevaluation\n    category: selective_prediction\n    role: background\n    relevance: Proposes LLM self-evaluation for selective generation, reformulating open-ended tasks into token-level predictions\n      to leverage better calibration. Directly relevant to our confidence-aware abstention mechanism for structured IE.\n    abstract: ''\n    semantic_scholar_id: ''\n    verified: true\n    added_by: paper-research:lit_batch3\n    added_at: '2026-05-14T19:30:00.000Z'"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_research_lit_batch3_20260514T182744",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/literature_map.yaml",
    "old_string": "    bibtex_key: fomicheva2020unsupervised\n    category: ensemble_mc_dropout\n    role: background\n    relevance: Applies MC dropout and ensemble-based uncertainty to NLP (MT quality estimation) without supervision, achieving\n      strong correlation with human judgments. Key precedent for unsupervised uncertainty signals in NLP generation tasks.\n    abstract: ''\n    semantic_scholar_id: ''\n    verified: true\n    added_by: paper-research:lit_batch2\n    added_at: '2026-05-14T18:10:52.000Z'",
    "new_string": "    bibtex_key: fomicheva2020unsupervised\n    category: ensemble_mc_dropout\n    role: background\n    relevance: Applies MC dropout and ensemble-based uncertainty to NLP (MT quality estimation) without supervision, achieving\n      strong correlation with human judgments. Key precedent for unsupervised uncertainty signals in NLP generation tasks.\n    abstract: ''\n    semantic_scholar_id: ''\n    verified: true\n    added_by: paper-research:lit_batch2\n    added_at: '2026-05-14T18:10:52.000Z'\n  cobbe2021verifiers:\n    title: Training Verifiers to Solve Math Word Problems\n    authors:\n    - Karl Cobbe\n    - Vineet Kosaraju\n    - Mohammad Bavarian\n    - Mark Chen\n    - Heewoo Jun\n    - Lukasz Kaiser\n    - Matthias Plappert\n    - Jerry Tworek\n    - Jacob Hilton\n    - Reiichiro Nakano\n    - Christopher Hesse\n    - John Schulman\n    year: 2021\n    venue: arXiv preprint\n    url: https://arxiv.org/abs/2110.14168\n    doi: ''\n    bibtex_key: cobbe2021verifiers\n    category: verifier_reward_models\n    role: foundation\n    relevance: 'Foundation paper: introduces training outcome-based verifiers (ORM) for math word problems and the GSM8K benchmark.\n      Establishes the verify-then-select paradigm our method builds upon.'\n    abstract: ''\n    semantic_scholar_id: ''\n    verified: true\n    added_by: paper-research:lit_batch3\n    added_at: '2026-05-14T19:30:00.000Z'\n  lightman2024verify:\n    title: Let's Verify Step by Step\n    authors:\n    - Hunter Lightman\n    - Vineet Kosaraju\n    - Yura Burda\n    - Harri Edwards\n    - Bowen Baker\n    - Teddy Lee\n    - Jan Leike\n    - John Schulman\n    - Ilya Sutskever\n    - Karl Cobbe\n    year: 2024\n    venue: ICLR 2024\n    url: https://arxiv.org/abs/2305.20050\n    doi: ''\n    bibtex_key: lightman2024verify\n    category: verifier_reward_models\n    role: foundation\n    relevance: 'Foundation paper: demonstrates process reward models (PRMs) with step-level supervision outperform outcome-based\n      verification. Key motivation for fine-grained quality signals in our structured IE aggregation.'\n    abstract: ''\n    semantic_scholar_id: ''\n    verified: true\n    added_by: paper-research:lit_batch3\n    added_at: '2026-05-14T19:30:00.000Z'\n  wang2024mathshepherd:\n    title: 'Math-Shepherd: Verify and Reinforce LLMs Step-by-step without Human Annotations'\n    authors:\n    - Peiyi Wang\n    - Lei Li\n    - Zhihong Shao\n    - Runxin Xu\n    - Damai Dai\n    - Yifei Li\n    - Deli Chen\n    - Yu Wu\n    - Zhifang Sui\n    year: 2024\n    venue: ACL 2024\n    url: https://arxiv.org/abs/2312.08935\n    doi: ''\n    bibtex_key: wang2024mathshepherd\n    category: verifier_reward_models\n    role: background\n    relevance: Automated process reward model construction without human annotations, enabling step-level verification at scale.\n      Demonstrates ORM/PRM effectiveness for both reranking and reinforcement learning.\n    abstract: ''\n    semantic_scholar_id: ''\n    verified: true\n    added_by: paper-research:lit_batch3\n    added_at: '2026-05-14T19:30:00.000Z'\n  snell2024scaling:\n    title: Scaling LLM Test-Time Compute Optimally can be More Effective than Scaling Model Parameters\n    authors:\n    - Charlie Snell\n    - Jaehoon Lee\n    - Kelvin Xu\n    - Aviral Kumar\n    year: 2024\n    venue: ICLR 2025\n    url: https://arxiv.org/abs/2408.03314\n    doi: ''\n    bibtex_key: snell2024scaling\n    category: tts_scaling\n    role: foundation\n    relevance: 'Foundation paper: introduces compute-optimal test-time scaling, showing adaptive per-prompt compute allocation\n      improves efficiency 4x over best-of-N. Directly motivates our adaptive sampling strategy.'\n    abstract: ''\n    semantic_scholar_id: ''\n    verified: true\n    added_by: paper-research:lit_batch3\n    added_at: '2026-05-14T19:30:00.000Z'\n  brown2024monkeys:\n    title: 'Large Language Monkeys: Scaling Inference Compute with Repeated Sampling'\n    authors:\n    - Bradley Brown\n    - Jordan Juravsky\n    - Ryan Ehrlich\n    - Ronald Clark\n    - Quoc V. Le\n    - Christopher Ré\n    - Azalia Mirhoseini\n    year: 2024\n    venue: arXiv preprint\n    url: https://arxiv.org/abs/2407.21787\n    doi: ''\n    bibtex_key: brown2024monkeys\n    category: tts_scaling\n    role: foundation\n    relevance: 'Foundation paper: demonstrates log-linear scaling of coverage with repeated sampling across tasks, establishing\n      inference-time scaling laws. Motivates our multi-sample approach for structured IE.'\n    abstract: ''\n    semantic_scholar_id: ''\n    verified: true\n    added_by: paper-research:lit_batch3\n    added_at: '2026-05-14T19:30:00.000Z'\n  wu2024inference:\n    title: 'Inference Scaling Laws: An Empirical Analysis of Compute-Optimal Inference for Problem-Solving with Language Models'\n    authors:\n    - Yangzhen Wu\n    - Zhiqing Sun\n    - Shanda Li\n    - Sean Welleck\n    - Yiming Yang\n    year: 2024\n    venue: arXiv preprint\n    url: https://arxiv.org/abs/2408.00724\n    doi: ''\n    bibtex_key: wu2024inference\n    category: tts_scaling\n    role: background\n    relevance: Empirical analysis of compute-optimal inference strategies showing smaller models with advanced inference algorithms\n      achieve Pareto-optimal cost-performance trade-offs. Complements our efficiency analysis.\n    abstract: ''\n    semantic_scholar_id: ''\n    verified: true\n    added_by: paper-research:lit_batch3\n    added_at: '2026-05-14T19:30:00.000Z'\n  kuleshov2015calibrated:\n    title: Calibrated Structured Prediction\n    authors:\n    - Volodymyr Kuleshov\n    - Percy Liang\n    year: 2015\n    venue: NeurIPS 2015\n    url: https://proceedings.neurips.cc/paper/2015/hash/52d2752b150f9c35ccb6869cbf074e48-Abstract.html\n    doi: ''\n    bibtex_key: kuleshov2015calibrated\n    category: structured_calibration_ie\n    role: foundation\n    relevance: 'Foundation paper: extends calibration to structured prediction with formal guarantees, proposing recalibration\n      methods for marginal and conditional queries. Theoretical basis for calibrated structured IE.'\n    abstract: ''\n    semantic_scholar_id: ''\n    verified: true\n    added_by: paper-research:lit_batch3\n    added_at: '2026-05-14T19:30:00.000Z'\n  culotta2004confidence:\n    title: Confidence Estimation for Information Extraction\n    authors:\n    - Aron Culotta\n    - Andrew McCallum\n    year: 2004\n    venue: HLT-NAACL 2004\n    url: https://aclanthology.org/N04-4028/\n    doi: ''\n    bibtex_key: culotta2004confidence\n    category: structured_calibration_ie\n    role: foundation\n    relevance: 'Foundation paper: pioneers confidence estimation for CRF-based information extraction at both field and record\n      levels. Establishes the problem setting our LLM-based approach addresses.'\n    abstract: ''\n    semantic_scholar_id: ''\n    verified: true\n    added_by: paper-research:lit_batch3\n    added_at: '2026-05-14T19:30:00.000Z'\n  jagannatha2020calibrating:\n    title: Calibrating Structured Output Predictors for Natural Language Processing\n    authors:\n    - Abhyuday Jagannatha\n    - Hong Yu\n    year: 2020\n    venue: ACL 2020\n    url: https://aclanthology.org/2020.acl-main.188/\n    doi: ''\n    bibtex_key: jagannatha2020calibrating\n    category: structured_calibration_ie\n    role: background\n    relevance: Proposes general calibration scheme for neural structured prediction models in NLP including NER and QA. Bridges\n      classical calibration methods to modern neural IE, directly relevant to our structured output calibration.\n    abstract: ''\n    semantic_scholar_id: ''\n    verified: true\n    added_by: paper-research:lit_batch3\n    added_at: '2026-05-14T19:30:00.000Z'\n  geifman2017selective:\n    title: Selective Classification for Deep Neural Networks\n    authors:\n    - Yonatan Geifman\n    - Ran El-Yaniv\n    year: 2017\n    venue: NeurIPS 2017\n    url: https://arxiv.org/abs/1705.08500\n    doi: ''\n    bibtex_key: geifman2017selective\n    category: selective_prediction\n    role: foundation\n    relevance: 'Foundation paper: introduces selective classification framework for DNNs with guaranteed risk control at specified\n      coverage levels. Theoretical foundation for our consistency-based selective prediction in IE.'\n    abstract: ''\n    semantic_scholar_id: ''\n    verified: true\n    added_by: paper-research:lit_batch3\n    added_at: '2026-05-14T19:30:00.000Z'\n  ren2023selfevaluation:\n    title: Self-Evaluation Improves Selective Generation in Large Language Models\n    authors:\n    - Jie Ren\n    - Yao Zhao\n    - Tu Vu\n    - Peter J. Liu\n    - Balaji Lakshminarayanan\n    year: 2023\n    venue: NeurIPS 2023 Workshop\n    url: https://arxiv.org/abs/2312.09300\n    doi: ''\n    bibtex_key: ren2023selfevaluation\n    category: selective_prediction\n    role: background\n    relevance: Proposes LLM self-evaluation for selective generation, reformulating open-ended tasks into token-level predictions\n      to leverage better calibration. Directly relevant to our confidence-aware abstention mechanism for structured IE.\n    abstract: ''\n    semantic_scholar_id: ''\n    verified: true\n    added_by: paper-research:lit_batch3\n    added_at: '2026-05-14T19:30:00.000Z'"
  }
}
```

</details>

---

### Tool result

_source line 46 · 2026-05-14T18:31:18.155390+00:00_

The file /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/literature_map.yaml has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_research_lit_batch3_20260514T182744",
  "tool": "Edit",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 47 · 2026-05-14T18:31:18.155563+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "python3 -c \"\nimport yaml\nwith open('literature_map.yaml') as f:\n    data = yaml.safe_load(f)\npapers = data['papers']\nprint(f'total_papers in meta: {data[\\\"meta\\\"][\\\"total_papers\\\"]}')\nprint(f'actual paper count: {len(papers)}')\nbatch3 = [k for k,v in papers.items() if v.get('added_by') == 'paper-research:lit_batch3']\nprint(f'batch3 papers ({len(batch3)}):')\nfor k in batch3:\n    print(f'  {k}: [{papers[k][\\\"category\\\"]}] {papers[k][\\\"role\\\"]}')\n\"\n",
  "description": "Validate YAML and count papers"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_research_lit_batch3_20260514T182744",
  "tool": "Bash",
  "tool_args": {
    "command": "python3 -c \"\nimport yaml\nwith open('literature_map.yaml') as f:\n    data = yaml.safe_load(f)\npapers = data['papers']\nprint(f'total_papers in meta: {data[\\\"meta\\\"][\\\"total_papers\\\"]}')\nprint(f'actual paper count: {len(papers)}')\nbatch3 = [k for k,v in papers.items() if v.get('added_by') == 'paper-research:lit_batch3']\nprint(f'batch3 papers ({len(batch3)}):')\nfor k in batch3:\n    print(f'  {k}: [{papers[k][\\\"category\\\"]}] {papers[k][\\\"role\\\"]}')\n\"\n",
    "description": "Validate YAML and count papers"
  }
}
```

</details>

---

### Tool result

_source line 48 · 2026-05-14T18:31:18.155707+00:00_

total_papers in meta: 41
actual paper count: 41
batch3 papers (11):
  cobbe2021verifiers: [verifier_reward_models] foundation
  lightman2024verify: [verifier_reward_models] foundation
  wang2024mathshepherd: [verifier_reward_models] background
  snell2024scaling: [tts_scaling] foundation
  brown2024monkeys: [tts_scaling] foundation
  wu2024inference: [tts_scaling] background
  kuleshov2015calibrated: [structured_calibration_ie] foundation
  culotta2004confidence: [structured_calibration_ie] foundation
  jagannatha2020calibrating: [structured_calibration_ie] background
  geifman2017selective: [selective_prediction] foundation
  ren2023selfevaluation: [selective_prediction] background

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_research_lit_batch3_20260514T182744",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 49 · 2026-05-14T18:31:18.155870+00:00_

11 篇全部写入，YAML 验证通过。

| Cluster | 条目 |
|---|---|
| verifier_reward_models (3) | Cobbe 2021 (foundation), Lightman 2024 (foundation), Wang 2024 Math-Shepherd (background) |
| tts_scaling (3) | Snell 2024 (foundation), Brown 2024 Large Language Monkeys (foundation), Wu 2024 Inference Scaling Laws (background) |
| structured_calibration_ie (3) | Kuleshov & Liang 2015 (foundation), Culotta & McCallum 2004 (foundation), Jagannatha & Yu 2020 (background) |
| selective_prediction (2) | Geifman & El-Yaniv 2017 (foundation), Ren et al. 2023 (background) |

meta.total_papers 已从 30 更新为 41。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_paper_research_lit_batch3_20260514T182744"
}
```

</details>

---
