# review related work completeness

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 41
- **Recorded user turns:** 0
- **Tool calls:** 20
- **Original source:** `logs/chats/worker_review_related-work-completeness_20260524T023100.jsonl`
- **Structured JSON:** [`582ef74d6cb10ba7e315.json`](../../sessions/58/582ef74d6cb10ba7e315.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

41 recorded events

### Tool call

_source line 1 · 2026-05-24T02:34:09.194268+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_review_related-work-completeness_20260524T023100",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/related_work.tex"
  }
}
```

</details>

---

### Tool result

_source line 2 · 2026-05-24T02:34:09.194621+00:00_

1	\section{Related Work}\label{sec:related}
2	
3	\paragraph{Test-time compute scaling and best-of-$N$.}
4	Self-consistency \cite{wang2023selfconsistency} and best-of-$N$ with compute-optimal allocation \cite{snell2025scaling, brown2024monkeys} drive large gains on reasoning and code tasks.
5	Reward-free selectors \cite{taubenfeld2025cisc, kang2025selfcertainty} and BoN scaling laws \cite{gao2023scaling} reduce or characterize inference cost, while trained verifiers \cite{cobbe2021verifiers, lightman2024verify} learn per-sample scoring.
6	All target discrete-answer settings; structured prediction requires different aggregation because degeneracy operates at the entity-set level.
7	
8	\paragraph{Consistency for structured IE.}
9	\citet{yao2026consistency} show consistency correlates with accuracy for LLM-based NER/RE; we diagnose degeneracy and LP compression as conditions associated with the failure of this correlation to yield selection gains.
10	\citet{xie2023zeroshot} propose entity voting for zero-shot NER, the closest prior work to our entity-level construction; our approach aggregates stochastic samples from a single fine-tuned model without prompt engineering.
11	\citet{yun2025price} show structured formats induce diversity collapse; our LP compression (median range 0.041 nats) corroborates this for NER.
12	Our evaluation builds on generative IE \cite{zhou2024uniner, sainz2024gollie} and constrained decoding \cite{willard2023guided, dong2024xgrammar}.
13	
14	\paragraph{Uncertainty estimation and MBR decoding.}
15	Our selection strategies instantiate MBR decoding \cite{eikema2022sampling}; \citet{eikema2025structured} find MBR utilities degrade on structured outputs, while our diagnosis identifies degeneracy as the primary bottleneck.
16	Semantic uncertainty \cite{kuhn2023semantic} and confidence estimation \cite{geng2024confidence, xia2025survey} provide complementary model-internal alternatives; our QE signals with AUROC up to 0.82 connect to selective predic
…[truncated 92 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_review_related-work-completeness_20260524T023100",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-24T02:34:09.194830+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/references.bib"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_review_related-work-completeness_20260524T023100",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/references.bib"
  }
}
```

</details>

---

### Tool result

_source line 4 · 2026-05-24T02:34:09.195203+00:00_

1	% Auto-generated from literature_map.yaml — do not edit manually
2	
3	@article{landesberg2026bon,
4	  title = {When {LLM} Judge Scores Look Good but Best-of-{N} Decisions Fail},
5	  author = {Landesberg, Eddie},
6	  journal = {arXiv preprint arXiv:2603.12520},
7	  year = {2026},
8	}
9	
10	
11	@article{holm1979simple,
12	  title = {A Simple Sequentially Rejective Multiple Test Procedure},
13	  author = {Holm, Sture},
14	  journal = {Scandinavian Journal of Statistics},
15	  volume = {6},
16	  number = {2},
17	  pages = {65--70},
18	  year = {1979},
19	}
20	
21	
22	@article{brown2024monkeys,
23	  title = {Large Language Monkeys: Scaling Inference Compute with Repeated Sampling},
24	  author = {Brown, Bradley and Juravsky, Jordan and Ehrlich, Ryan and Clark, Ronald and Le, Quoc V. and Ré, Christopher and Mirhoseini, Azalia},
25	  journal = {arXiv preprint arXiv:2407.21787},
26	  year = {2024},
27	  url = {https://arxiv.org/abs/2407.21787}
28	}
29	
30	@inproceedings{chen2024usc,
31	  title = {Universal Self-Consistency for Large Language Model Generation},
32	  author = {Chen, Xinyun and Aksitov, Renat and Alon, Uri and Ren, Jie and Xiao, Kefan and Yin, Pengcheng and Prakash, Sushant and Sutton, Charles and Wang, Xuezhi and Zhou, Denny},
33	  booktitle = {ICML 2024 Workshop on In-Context Learning},
34	  year = {2024},
35	  url = {https://arxiv.org/abs/2311.17311}
36	}
37	
38	@article{cobbe2021verifiers,
39	  title = {Training Verifiers to Solve Math Word Problems},
40	  author = {Cobbe, Karl and Kosaraju, Vineet and Bavarian, Mohammad and Chen, Mark and Jun, Heewoo and Kaiser, Lukasz and Plappert, Matthias and Tworek, Jerry and Hilton, Jacob and Nakano, Reiichiro and Hesse, Christopher and Schulman, John},
41	  journal = {arXiv preprint arXiv:2110.14168},
42	  year = {2021},
43	  url = {https://arxiv.org/abs/2110.14168}
44	}
45	
46	@inproceedings{derczynski2017wnut,
47	  title = {Results of the WNUT2017 Shared Task on Novel and Emerging Entity Recognition},
48	  autho
…[truncated 23771 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_review_related-work-completeness_20260524T023100",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-24T02:34:09.195445+00:00_

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
  "session": "worker_review_related-work-completeness_20260524T023100",
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

_source line 6 · 2026-05-24T02:34:09.195589+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_review_related-work-completeness_20260524T023100",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-24T02:34:09.195723+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "test-time compute scaling inference-time NLP 2025 2026 survey"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_review_related-work-completeness_20260524T023100",
  "tool": "WebSearch",
  "tool_args": {
    "query": "test-time compute scaling inference-time NLP 2025 2026 survey"
  }
}
```

</details>

---

### Tool call

_source line 8 · 2026-05-24T02:34:09.195842+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "self-consistency structured prediction NER information extraction 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_review_related-work-completeness_20260524T023100",
  "tool": "WebSearch",
  "tool_args": {
    "query": "self-consistency structured prediction NER information extraction 2025 2026"
  }
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-24T02:34:09.195958+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "LLM named entity recognition structured output 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_review_related-work-completeness_20260524T023100",
  "tool": "WebSearch",
  "tool_args": {
    "query": "LLM named entity recognition structured output 2025 2026"
  }
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-24T02:34:09.196096+00:00_

Web search results for query: "test-time compute scaling inference-time NLP 2025 2026 survey"

Links: [{"title":"Trust but Verify! A Survey on Verification Design for Test-time Scaling","url":"https://arxiv.org/html/2508.16665v3"},{"title":"A Survey of Test-Time Compute: From Intuitive Inference to Deliberate Reasoning","url":"https://arxiv.org/pdf/2501.02497"},{"title":"The Art of Scaling Test-Time Compute for Large Language Models","url":"https://arxiv.org/pdf/2512.02008"},{"title":"(PDF) Revisiting Test-Time Scaling: A Survey and a Diversity-Aware Method for Efficient Reasoning","url":"https://www.researchgate.net/publication/392466011_Revisiting_Test-Time_Scaling_A_Survey_and_a_Diversity-Aware_Method_for_Efficient_Reasoning"},{"title":"Trust but Verify! A Survey on Verification Design for Test-time Scaling","url":"https://arxiv.org/pdf/2508.16665"},{"title":"Scaling LLM Test-Time Compute Optimally Can be More Effective than Scaling Parameters for Reasoning | OpenReview","url":"https://openreview.net/forum?id=4FWAwZtd2n"}]

The search has found several highly relevant recent surveys and papers on test-time compute scaling and inference-time NLP. Here are the key findings:

## Recent Surveys

The central idea behind test-time scaling (TTS) is that increasing the compute budget at inference can yield substantial gains in model performance.

**Key 2025 Surveys:**

1. "Trust but Verify! A Survey on Verification Design for Test-time Scaling" (September 2025) conducted a comprehensive search focusing on NLP venues such as ACL, EMNLP, NAACL, COLM and journals like TACL.

2. "A Survey of Test-Time Compute: From Intuitive Inference to Deliberate Reasoning" organizes its coverage according to the trend of System-1 to System-2 thinking, highlighting the key role of test-time compute in the transition from System-1 models to weak System-2 models, and then to strong System-2 models.

## Recent Developments

Test-time scaling (TTS) has emerged as an effective method to enhance
…[truncated 659 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_review_related-work-completeness_20260524T023100",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 11 · 2026-05-24T02:34:09.196337+00:00_

Web search results for query: "self-consistency structured prediction NER information extraction 2025 2026"

Links: [{"title":"Self-Adaptive Named Entity Recognition by Retrieving Unstructured   Knowledge","url":"https://arxiv.org/pdf/2210.07523"},{"title":"Consistency enhancement of model prediction on document-level named entity recognition","url":"https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10272703/"},{"title":"Large language models for generative information extraction: a survey","url":"https://journal.hep.com.cn/fcs/EN/10.1007/s11704-024-40555-y"},{"title":"A review of named entity recognition: from learning methods to modelling paradigms and tasks | Artificial Intelligence Review | Springer Nature Link","url":"https://link.springer.com/article/10.1007/s10462-025-11321-8"},{"title":"Enhancing Label Consistency on Document-level Named Entity Recognition","url":"https://arxiv.org/pdf/2210.12949"},{"title":"Self-Improving for Zero-Shot Named Entity Recognition with Large   Language Models","url":"https://arxiv.org/pdf/2311.08921"},{"title":"A Simple but Effective Approach to Improve Structured Language Model   Output for Information Extraction","url":"https://arxiv.org/pdf/2402.13364"}]

Based on the web search results, here's what I found regarding self-consistency, structured prediction, NER (Named Entity Recognition), and information extraction in recent work:

## Key Findings

**Self-Consistency in NER and Information Extraction:**

Self-consistency methods have been proposed where prompts with inconsistent predictions are discarded. LLMs make predictions on unlabeled corpus, generating self-annotated dataset through self-consistency. Additionally, self-consistency can be combined with other strategies to further elevate LLM capabilities in various structured text generation tasks.

**Structured Prediction for Information Extraction:**

LLMs are asked to organize output into the desired structure, using intermediate responses as context, effectively separati
…[truncated 810 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_review_related-work-completeness_20260524T023100",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-24T02:34:09.196530+00:00_

Web search results for query: "LLM named entity recognition structured output 2025 2026"

Links: [{"title":"A novel large-language-model-driven framework for named entity recognition - ScienceDirect","url":"https://www.sciencedirect.com/science/article/abs/pii/S0306457324004138"},{"title":"[2508.15801] LingVarBench: Benchmarking LLMs on Entity Recognitions and Linguistic Verbalization Patterns in Phone-Call Transcripts","url":"https://arxiv.org/abs/2508.15801"},{"title":"NER - Named Entities via LLM(OpenAI) and smart chunking | by Sobhan Hota | Medium","url":"https://medium.com/@sobhan.hota/ner-recognize-namedentity-via-openai-llms-and-smart-chunking-c067e020393c"},{"title":"Improving few-shot named entity recognition for large language models using structured dynamic prompting with retrieval augmented generation | npj Artificial Intelligence","url":"https://www.nature.com/articles/s44387-025-00062-2"},{"title":"Assessment of Generative Named Entity Recognition in the Era of Large Language Models","url":"https://arxiv.org/pdf/2601.17898"},{"title":"GPT-NER: Named Entity Recognition via Large Language Models - ACL Anthology","url":"https://aclanthology.org/2025.findings-naacl.239/"},{"title":"Comparative analysis of generative LLMs for labeling entities in clinical notes","url":"https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11804004/"},{"title":"Modern Named Entity Recognition: Beyond Traditional NLP with Transformers and LLMs — 2026 | by akanksha sharma | Medium","url":"https://akankshaonearth.medium.com/modern-named-entity-recognition-beyond-traditional-nlp-with-transformers-and-llms-2026-c935ef31e692"}]

Based on the search results, here's what I found about LLM named entity recognition with structured output in 2025-2026:

## Recent Developments

The development of large language models is shifting traditional NER toward a unified generative paradigm, where LLMs sequentially generate sentences along with their corresponding entity labels in textual form.

Recent r
…[truncated 1195 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_review_related-work-completeness_20260524T023100",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-24T02:34:09.196722+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "best-of-N sampling scaling laws structured generation 2025 2026 arxiv"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_review_related-work-completeness_20260524T023100",
  "tool": "WebSearch",
  "tool_args": {
    "query": "best-of-N sampling scaling laws structured generation 2025 2026 arxiv"
  }
}
```

</details>

---

### Tool call

_source line 14 · 2026-05-24T02:34:09.196856+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"test-time scaling\" \"structured prediction\" OR \"information extraction\" OR \"NER\" 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_review_related-work-completeness_20260524T023100",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"test-time scaling\" \"structured prediction\" OR \"information extraction\" OR \"NER\" 2025 2026"
  }
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-24T02:34:09.196976+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "GPT-NER LLM NER survey generative 2025 2026 arxiv ACL EMNLP"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_review_related-work-completeness_20260524T023100",
  "tool": "WebSearch",
  "tool_args": {
    "query": "GPT-NER LLM NER survey generative 2025 2026 arxiv ACL EMNLP"
  }
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-24T02:34:09.197121+00:00_

Web search results for query: ""test-time scaling" "structured prediction" OR "information extraction" OR "NER" 2025 2026"

Links: [{"title":"Structured Language Generation Model: Loss Calibration and Formatted Decoding for Robust Structure Prediction and Knowledge Retrieval","url":"https://arxiv.org/html/2402.08971"},{"title":"A Survey on Test-Time Scaling. This blog is based a comprehensive… | by Yanan Chen | Medium","url":"https://medium.com/@yananchen1116/a-survey-on-test-time-scaling-04b1c1dadb9d"},{"title":"Predicting and improving test-time scaling laws via reward tail-guided search","url":"https://arxiv.org/pdf/2602.01485"},{"title":"1 Introduction","url":"https://arxiv.org/html/2602.01485"},{"title":"Understanding the Role of Training Data in Test-Time Scaling","url":"https://arxiv.org/pdf/2510.03605"}]

I found several relevant results about test-time scaling in relation to structured prediction, information extraction, and NER from 2025-2026:

## Key Findings:

**Test-time Scaling Performance on Structured Tasks:**
Large language models underperform smaller fine-tuned models for information extraction and other structure-related tasks even with test-time scaling methods like in-context learning and chain-of-thought reasoning. GPT-4 falls short against smaller models in CoNLL04 joint entity and relation extraction, even when equipped with detailed instructions and examples.

**Test-Time Scaling Strategies:**
Test-time scaling strategies leverage the stochastic nature of LLM outputs to enhance performance without necessitating further model training. The "best-of-N" (BoN) approach has emerged as a simple yet effective method, demonstrating significant performance gains across various tasks.

**Training Data and Test-Time Scaling:**
Recent research explores how training data properties enable test-time scaling. Training on diverse and difficult data has shown to be beneficial to enable test-time scaling on complex reasoning tasks, such as mathematical compet
…[truncated 467 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_review_related-work-completeness_20260524T023100",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 17 · 2026-05-24T02:34:09.197329+00:00_

Web search results for query: "best-of-N sampling scaling laws structured generation 2025 2026 arxiv"

Links: [{"title":"Published as a conference paper at ICLR 2026 PRETRAINING SCALING LAWS FOR","url":"https://arxiv.org/pdf/2509.24012"},{"title":"1 Introduction","url":"https://arxiv.org/html/2602.01485"},{"title":"Scalable Best-of-N Selection for Large Language Models via Self-Certainty","url":"https://arxiv.org/pdf/2502.18581"},{"title":"Predictive Scaling Laws for Efficient GRPO Training of Large Reasoning Models","url":"https://arxiv.org/html/2507.18014v1"},{"title":"Iterative Deepening Sampling as Efficient Test-Time Scaling","url":"https://arxiv.org/html/2502.05449"},{"title":"arXiv:2502.05449v2 [cs.CL] 1 Jun 2025","url":"https://www.arxiv.org/pdf/2502.05449"},{"title":"Predicting and improving test-time scaling laws via reward tail-guided search","url":"https://arxiv.org/pdf/2602.01485"},{"title":"Scaling Laws for Optimal Data Mixtures","url":"https://arxiv.org/html/2507.09404v1"},{"title":"INFERENCE-AWARE FINE-TUNING FOR BEST-OF-N ...","url":"https://openreview.net/pdf?id=77gQUdQhE7"}]

The search found several relevant recent papers on best-of-N sampling and scaling laws from arXiv in 2025-2026:

**Key Papers:**

1. **Predicting and Improving Test-Time Scaling Laws via Reward Tail-Guided Search** (Feb 2026): Addresses gaps in scaling laws for test-time strategies like BoN by introducing a framework for predicting test-time scaling laws via tail extrapolation of reward distributions. The paper proposes Scaling-Law Guided (SLG) Search, an adaptive algorithm that dynamically allocates computational resources based on predicted rewards.

2. **Iterative Deepening Sampling as Efficient Test-Time Scaling** (June 2025): Shows that ID-sampling yields performance gains with increasing sample size (N) under a Best-of-N selection strategy, and theoretically demonstrates that ID-Sampling effectively balances computational efficiency and response quality on MATH-500 and 
…[truncated 680 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_review_related-work-completeness_20260524T023100",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-24T02:34:09.197495+00:00_

Web search results for query: "GPT-NER LLM NER survey generative 2025 2026 arxiv ACL EMNLP"

Links: [{"title":"GPT-NER: Named Entity Recognition via Large Language Models","url":"https://arxiv.org/pdf/2304.10428"},{"title":"Large language models for generative information extraction: a survey | Frontiers of Computer Science | Springer Nature Link","url":"https://link.springer.com/article/10.1007/s11704-024-40555-y"},{"title":"Assessment of Generative Named Entity Recognition in the Era of Large Language Models","url":"https://arxiv.org/pdf/2601.17898"},{"title":"Improving large language models for clinical named entity recognition via prompt engineering","url":"https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11339492/"},{"title":"A Survey of Reinforcement Learning for Large Language Models under Data Scarcity: Challenges and Solutions","url":"https://arxiv.org/html/2604.17312v1"},{"title":"Large Language Models Meet NLP: A Survey","url":"https://arxiv.org/html/2405.12819v2"}]

I found several relevant results for your search on GPT-NER, LLM-based NER, and generative approaches to named entity recognition. Here's what the search revealed:

## Key Papers and Resources

1. **GPT-NER Paper (2023)** - The original GPT-NER work leverages the in-context learning capabilities of large language models, showing that LLMs can achieve promising results on various NLP tasks including named entity extraction. However, LLMs' performance on NER tasks were still below supervised baselines at that time.

2. **Assessment of Generative NER (2025-2026)** - A recent comprehensive assessment across eight LLMs and four standard NER datasets found that with parameter-efficient finetuning and structured formats, open-source LLMs achieve performance competitive with traditional encoder-based models. These findings demonstrate that generative NER with LLMs is a promising, user-friendly alternative to traditional methods.

3. **Survey on Generative Information Extraction (2024)** - A Frontiers of 
…[truncated 568 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_review_related-work-completeness_20260524T023100",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-24T02:34:09.197649+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "minimum Bayes risk decoding structured output 2025 2026 arxiv"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_review_related-work-completeness_20260524T023100",
  "tool": "WebSearch",
  "tool_args": {
    "query": "minimum Bayes risk decoding structured output 2025 2026 arxiv"
  }
}
```

</details>

---

### Tool call

_source line 20 · 2026-05-24T02:34:09.197775+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "diversity collapse LLM structured generation format constraint 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_review_related-work-completeness_20260524T023100",
  "tool": "WebSearch",
  "tool_args": {
    "query": "diversity collapse LLM structured generation format constraint 2025 2026"
  }
}
```

</details>

---

### Tool call

_source line 21 · 2026-05-24T02:34:09.197894+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"inference-aware fine-tuning\" best-of-N ICLR 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_review_related-work-completeness_20260524T023100",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"inference-aware fine-tuning\" best-of-N ICLR 2026"
  }
}
```

</details>

---

### Tool result

_source line 22 · 2026-05-24T02:34:09.198050+00:00_

Web search results for query: ""inference-aware fine-tuning" best-of-N ICLR 2026"

Links: [{"title":"Inference-Aware Fine-Tuning for Best-of-N Sampling in Large Language Models | OpenReview","url":"https://openreview.net/forum?id=77gQUdQhE7"},{"title":"Inference-Aware Fine-Tuning for Best-of-N Sampling in Large Language Models","url":"https://arxiv.org/html/2412.15287v1"},{"title":"Inference-Aware Fine-Tuning for Best-of-N Sampling in Large Language Models","url":"https://proceedings.iclr.cc/paper_files/paper/2025/hash/c40bed606c51c8e827c1ba75aa2da054-Abstract-Conference.html"},{"title":"ICLR Poster Inference-Aware Fine-Tuning for Best-of-N Sampling in Large Language Models","url":"https://iclr.cc/virtual/2025/poster/30849"},{"title":"Inference-Aware Fine-Tuning for Best-of-N Sampling in Large Language Models | Cool Papers - Immersive Paper Discovery","url":"https://papers.cool/venue/77gQUdQhE7@OpenReview"},{"title":"Inference-Aware Fine-Tuning for Best-of-N Sampling in ...","url":"https://arxiv.org/pdf/2412.15287"},{"title":"INFERENCE-AWARE FINE-TUNING FOR BEST-OF-N ...","url":"https://openreview.net/pdf?id=77gQUdQhE7"},{"title":"[2412.15287] Inference-Aware Fine-Tuning for Best-of-N Sampling in Large Language Models","url":"https://arxiv.org/abs/2412.15287"}]

I found results for your search query. Here's what I found:

"Inference-Aware Fine-Tuning for Best-of-N Sampling in Large Language Models" is a paper that develops a novel inference-aware fine-tuning paradigm, with the Best-of-N (BoN) inference strategy at its core, devising the first imitation learning and reinforcement learning methods for fine-tuning LLMs using BoN.

The Best-of-N inference strategy involves an LLM generating multiple responses and a verifier selecting the best. The BoN-aware models implicitly learn a per-example "meta-strategy" that interleaves best responses with more diverse responses that might be better suited to a test-time input.

The experiments show that the methods improve the B
…[truncated 338 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_review_related-work-completeness_20260524T023100",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 23 · 2026-05-24T02:34:09.198247+00:00_

Web search results for query: "minimum Bayes risk decoding structured output 2025 2026 arxiv"

Links: [{"title":"[2510.20700] Structure-Conditional Minimum Bayes Risk Decoding","url":"https://arxiv.org/abs/2510.20700"},{"title":"[2502.12685] Theoretical Guarantees for Minimum Bayes Risk Decoding","url":"https://arxiv.org/abs/2502.12685"},{"title":"[2512.01316] Agreement-Constrained Probabilistic Minimum Bayes Risk Decoding","url":"https://arxiv.org/abs/2512.01316"},{"title":"Structure-Conditional Minimum Bayes Risk Decoding","url":"https://arxiv.org/html/2510.20700"},{"title":"Uncertainty-Aware Decoding with Minimum Bayes Risk","url":"https://arxiv.org/html/2503.05318v1"},{"title":"[2503.05318] Uncertainty-Aware Decoding with Minimum Bayes Risk","url":"https://arxiv.org/abs/2503.05318"},{"title":"Structure-Conditional Minimum Bayes Risk Decoding","url":"https://arxiv.org/pdf/2510.20700"},{"title":"Re-evaluating Minimum Bayes Risk Decoding for Automated Speech Recognition Tasks","url":"https://arxiv.org/html/2510.19471"},{"title":"mbrs: A Library for Minimum Bayes Risk Decoding","url":"https://arxiv.org/pdf/2408.04167"},{"title":"[2512.07540] Minimum Bayes Risk Decoding for Error Span Detection in Reference-Free Automatic Machine Translation Evaluation","url":"https://arxiv.org/abs/2512.07540"}]

I found several recent arXiv papers on minimum Bayes risk (MBR) decoding with structured output and related topics from 2025-2026:

## Key Papers

1. **Structure-Conditional Minimum Bayes Risk Decoding** (October 2025)
   Introduces three lightweight adaptations to the utility function, designed to make MBR more sensitive to structural variability in the outcome space. MBR has proven effective in machine translation, but may face challenges in more open-ended tasks such as dialogue or instruction-following, where applying MBR with standard similarity-based utility functions may select responses that are broadly representative of the model's distribution, yet sub-optimal with
…[truncated 1397 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_review_related-work-completeness_20260524T023100",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 24 · 2026-05-24T02:34:09.198416+00:00_

Web search results for query: "diversity collapse LLM structured generation format constraint 2025 2026"

Links: [{"title":"[2505.18949] The Price of Format: Diversity Collapse in LLMs","url":"https://arxiv.org/abs/2505.18949"},{"title":"Chenyang An","url":"https://chenyang-an.github.io/"},{"title":"The Price of Format: Diversity Collapse in LLMs","url":"https://arxiv.org/pdf/2505.18949"},{"title":"The Price of Format: Diversity Collapse in LLMs - ACL Anthology","url":"https://aclanthology.org/2025.findings-emnlp.836/"},{"title":"The Price of Format: Diversity Collapse in LLMs","url":"https://arxiv.org/html/2505.18949v1"},{"title":"[Literature Review] The Price of Format: Diversity Collapse in LLMs","url":"https://www.themoonlight.io/en/review/the-price-of-format-diversity-collapse-in-llms"}]

Based on the search results, I found relevant recent research on this topic:

## Key Findings

Instruction-tuned large language models employ structured templates with role markers and special tokens to enforce format consistency during inference. However, this formatting induces diversity collapse, where models generate semantically similar outputs for open-ended inputs, undermining creativity and variability.

Diversity collapse persists even under high-temperature sampling, and structural tokens in templates significantly constrain the model's output space.

## Research Evidence

Experiments with five diverse instruction-tuned models on tasks like commonsense reasoning, story completion, and open-ended generation show that full chat templates yield significantly lower semantic and label diversity compared to simple, structure-free prompts. This effect persists even at higher decoding temperatures, suggesting it's an inherent constraint imposed by the template structure rather than a sampling artifact.

## Implications

Output diversity is primarily governed by the presence or absence of structural tokens, with minimal formatting yielding the most diverse outputs. Current pr
…[truncated 401 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_review_related-work-completeness_20260524T023100",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 25 · 2026-05-24T02:34:09.198560+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "entity voting aggregation NER multiple samples LLM 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_review_related-work-completeness_20260524T023100",
  "tool": "WebSearch",
  "tool_args": {
    "query": "entity voting aggregation NER multiple samples LLM 2025 2026"
  }
}
```

</details>

---

### Tool call

_source line 26 · 2026-05-24T02:34:09.198688+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "constrained decoding structured generation LLM 2025 2026 grammar guided"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_review_related-work-completeness_20260524T023100",
  "tool": "WebSearch",
  "tool_args": {
    "query": "constrained decoding structured generation LLM 2025 2026 grammar guided"
  }
}
```

</details>

---

### Tool call

_source line 27 · 2026-05-24T02:34:09.198806+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "uncertainty estimation NER sequence labeling calibration 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_review_related-work-completeness_20260524T023100",
  "tool": "WebSearch",
  "tool_args": {
    "query": "uncertainty estimation NER sequence labeling calibration 2025 2026"
  }
}
```

</details>

---

### Tool result

_source line 28 · 2026-05-24T02:34:09.198942+00:00_

Web search results for query: "uncertainty estimation NER sequence labeling calibration 2025 2026"

Links: [{"title":"[2311.08726] Uncertainty Estimation on Sequential Labeling via Uncertainty Transmission","url":"https://arxiv.org/abs/2311.08726"},{"title":"Uncertainty Estimation on Sequential Labeling via Uncertainty Transmission","url":"https://arxiv.org/html/2311.08726"},{"title":"Uncertainty Estimation on Sequential Labeling via Uncertainty   Transmission","url":"https://arxiv.org/pdf/2311.08726"},{"title":"Uncertainty Quantification for Named Entity Recognition via Full-Sequence and Subsequence Conformal Prediction","url":"https://arxiv.org/html/2601.16999"},{"title":"Uncertainty-aware Self-training for Low-resource Neural Sequence   Labeling","url":"https://arxiv.org/pdf/2302.08659"},{"title":"A Monte Carlo Framework for Calibrated Uncertainty Estimation in   Sequence Prediction","url":"https://arxiv.org/pdf/2410.23272"}]

Based on the search results, here are some recent findings on uncertainty estimation, NER (Named Entity Recognition), sequence labeling, and calibration:

## Recent Research (2025-2026)

A recent framework (January 2026) introduces methods for adapting sequence-labeling-based NER models to produce uncertainty-aware prediction sets that are guaranteed to contain the correct labeling with a user-specified confidence level. This approach leverages conformal prediction to generate confidence-calibrated sets of plausible labels that guarantee finite-sample coverage.

## Earlier Research (2023-2024)

Although previous works have shown great progress in improving NER performance, uncertainty estimation on NER (UE-NER) is still underexplored but essential. 

One approach proposes a Sequential Labeling Posterior Network (SLPN) to estimate uncertainty scores for extracted entities, considering uncertainty transmitted from other tokens, with a defined evaluation strategy to address wrong-span cases.

A Monte Carlo framework for sequence prediction sho
…[truncated 515 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_review_related-work-completeness_20260524T023100",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 29 · 2026-05-24T02:34:09.199102+00:00_

Web search results for query: "entity voting aggregation NER multiple samples LLM 2025 2026"

Links: [{"title":"The Majority is not always right: RL training for solution aggregation","url":"https://arxiv.org/pdf/2509.06870"},{"title":"Beyond Majority Voting: LLM Aggregation by Leveraging Higher-Order Information","url":"https://arxiv.org/html/2510.01499v1"},{"title":"Beyond Majority Voting: LLM Aggregation by Leveraging Higher-Order Information","url":"https://www.arxiv.org/pdf/2510.01499"},{"title":"[2510.01499] Beyond Majority Voting: LLM Aggregation by Leveraging Higher-Order Information","url":"https://arxiv.org/abs/2510.01499"},{"title":"Beyond Majority Voting: LLM Aggregation by Leveraging Higher-Order Information | OpenReview","url":"https://openreview.net/forum?id=H1s6SBhzlg"},{"title":"EL4NER: Ensemble Learning for Named Entity Recognition via Multiple Small-Parameter Large Language Models","url":"https://arxiv.org/pdf/2505.23038"},{"title":"Local LLM Ensembles for Zero-shot Portuguese Named Entity Recognition","url":"https://arxiv.org/pdf/2512.10043"},{"title":"Aggregating results from named entity recognition services","url":"https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/9721002"}]

I found several relevant research papers related to your query. Here are the key findings:

## LLM Aggregation Methods (2025-2026)

Sampling multiple generated solutions has become a predominant way to improve large language models on challenging reasoning tasks. A central design choice involves how to aggregate answers, with standard practice being majority voting or weighted majority voting, optionally guided by reward models or verifiers.

However, research is moving beyond simple majority voting. Previous works have mostly employed simple majority voting as a first approach, but majority voting can be viewed as a zero-order aggregation method that only depends on observed answers and fails to account for heterogeneity and correlation among models, which
…[truncated 931 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_review_related-work-completeness_20260524T023100",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 30 · 2026-05-24T02:34:09.199292+00:00_

Web search results for query: "constrained decoding structured generation LLM 2025 2026 grammar guided"

Links: [{"title":"Constrained Decoding: Grammar-Guided Generation for Structured LLM Output - Interactive | Michael Brenndoerfer | Michael Brenndoerfer","url":"https://mbrenndoerfer.com/writing/constrained-decoding-structured-llm-output"},{"title":"[2503.24191] When Grammar Guides the Attack: Uncovering Control-Plane Vulnerabilities in LLMs with Structured Output","url":"https://arxiv.org/abs/2503.24191"},{"title":"Draft-Conditioned Constrained Decoding for Structured Generation in LLMs","url":"https://arxiv.org/pdf/2603.03305"},{"title":"How Structured Outputs and Constrained Decoding Work | Let's Data Science","url":"https://letsdatascience.com/blog/structured-outputs-making-llms-return-reliable-json"},{"title":"Beyond Free-Form Text: How Constrained Decoding is Reshaping Structured Generation in LLMs | by Brijesh Nambiar | Medium","url":"https://medium.com/@brijeshrn/beyond-free-form-text-how-constrained-decoding-is-reshaping-structured-generation-in-llms-5f7a38bef259"},{"title":"Guiding LLMs The Right Way: Fast, Non-Invasive Constrained Generation","url":"https://arxiv.org/pdf/2403.06988"},{"title":"Flexible and Efficient Grammar-Constrained Decoding","url":"https://arxiv.org/pdf/2502.05111"}]

Here are the search results for constrained decoding, structured generation, and grammar-guided techniques for LLMs in 2025-2026:

## Key Concepts and Current Approaches

Constrained decoding forces language models to generate valid JSON, SQL, and regex-matching text through token masking and grammar-guided generation. Constrained decoding guides the output of Large Language Models by enforcing user-given constraints in highly structured settings, with grammar-constrained decoding referring to the specific case where the constraint is given as a formal grammar that the LLM's output must conform to.

## Leading Implementations (2025-2026)

XGrammar is the default struct
…[truncated 1228 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_review_related-work-completeness_20260524T023100",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 31 · 2026-05-24T02:34:09.199451+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"conformal prediction\" \"named entity recognition\" 2025 2026 arxiv"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_review_related-work-completeness_20260524T023100",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"conformal prediction\" \"named entity recognition\" 2025 2026 arxiv"
  }
}
```

</details>

---

### Tool call

_source line 32 · 2026-05-24T02:34:09.199572+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "repeated sampling coverage scaling LLM code math 2025 pass@k best-of-N verifier"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_review_related-work-completeness_20260524T023100",
  "tool": "WebSearch",
  "tool_args": {
    "query": "repeated sampling coverage scaling LLM code math 2025 pass@k best-of-N verifier"
  }
}
```

</details>

---

### Tool result

_source line 33 · 2026-05-24T02:34:09.199727+00:00_

Web search results for query: ""conformal prediction" "named entity recognition" 2025 2026 arxiv"

Links: [{"title":"[2601.16999] Uncertainty Quantification for Named Entity Recognition via Full-Sequence and Subsequence Conformal Prediction","url":"https://arxiv.org/abs/2601.16999"},{"title":"Uncertainty Quantification for Named Entity Recognition via Full-Sequence and Subsequence Conformal Prediction","url":"https://arxiv.org/html/2601.16999"},{"title":"Uncertainty-Aware Transformers: Conformal Prediction for Language Models","url":"https://arxiv.org/html/2604.08885"},{"title":"[2603.00924] Conformal Prediction for Risk-Controlled Medical Entity Extraction Across Clinical Domains","url":"https://arxiv.org/abs/2603.00924"},{"title":"Conformal Prediction for Natural Language Processing: A Survey","url":"https://arxiv.org/pdf/2405.01976"},{"title":"Conformal Prediction: A Data Perspective","url":"https://arxiv.org/html/2410.06494v3"}]

Here are the search results for "conformal prediction" "named entity recognition" 2025 2026 arxiv:

## Recent arXiv Papers

1. **Uncertainty Quantification for Named Entity Recognition via Full-Sequence and Subsequence Conformal Prediction** (January 13, 2026)
   - Uses conformal prediction, which offers finite-sample coverage guarantees under minimal assumptions
   - Designs nonconformity scoring functions to construct efficient, well-calibrated prediction sets that support both unconditional and class-conditional coverage
   - Accounts for heterogeneity across sentence length, language, entity type, and number of entities within a sentence

2. **Conformal Prediction for Risk-Controlled Medical Entity Extraction Across Clinical Domains** (March 1, 2026)
   - Presents a conformal prediction framework that provides finite-sample coverage guarantees for LLM-based extraction across two clinical domains
   - Achieves target coverage (≥90%) in both settings with manageable rejection rates (9-13%)

3. **Uncertainty-Aware Transformers: Conform
…[truncated 559 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_review_related-work-completeness_20260524T023100",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 34 · 2026-05-24T02:34:09.199898+00:00_

Web search results for query: "repeated sampling coverage scaling LLM code math 2025 pass@k best-of-N verifier"

Links: [{"title":"[2502.11027] Diversified Sampling Improves Scaling LLM inference","url":"https://ar5iv.labs.arxiv.org/html/2502.11027"},{"title":"Best-of-Majority: Minimax-Optimal Strategy for Pass@$k$ Inference Scaling","url":"https://arxiv.org/pdf/2510.03199"},{"title":"Pass@k Metrics for LLM Evaluation","url":"https://www.emergentmind.com/topics/pass-k-metrics-2508a3b6-8dc0-488f-a854-891fb35d80b0"},{"title":"Large Language Monkeys: Scaling Inference Compute with Repeated Sampling","url":"https://scalingintelligence.stanford.edu/pubs/large_language_monkeys.pdf"},{"title":"Large Language Monkeys: Scaling Inference Compute with Repeated Sampling","url":"https://arxiv.org/pdf/2407.21787"},{"title":"How pass@k is used to evaluate LLM coding performance | by Garrett Fincke | Medium","url":"https://medium.com/@ggfincke/how-pass-k-is-used-to-evaluate-llm-coding-performance-296e5c4565bc"},{"title":"Published as a conference paper at ICLR 2025 LEARNING HOW HARD TO THINK:","url":"https://proceedings.iclr.cc/paper_files/paper/2025/file/ff414825df833edb8b1839e3d5d495e9-Paper-Conference.pdf"}]

Based on the search results, here's what I found related to repeated sampling, coverage scaling, and LLM code/math evaluation:

## Key Findings

**Repeated Sampling and Coverage:**
In MATH, coverage with Llama-3 models grows to over 95% with 10,000 samples. However, common methods to pick correct solutions from a sample collection, such as majority voting or reward models, plateau beyond several hundred samples and fail to fully scale with the sample budget.

**Best-of-Majority Strategy:**
Researchers proposed a new inference strategy called Best-of-Majority (BoM), with a pivotal step that restricts the candidates to the responses with high frequency in the N samples before selecting the top-k rewards. Unlike majority voting and BoN, BoM's performance does not degrade when 
…[truncated 689 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_review_related-work-completeness_20260524T023100",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 35 · 2026-05-24T02:34:09.200075+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__register_artifact",
  "max_results": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_review_related-work-completeness_20260524T023100",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__register_artifact",
    "max_results": "1"
  }
}
```

</details>

---

### Tool result

_source line 36 · 2026-05-24T02:34:09.200225+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_review_related-work-completeness_20260524T023100",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 37 · 2026-05-24T02:34:09.200363+00:00_

called Write

<details open><summary>🔧 Tool call — Write</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/related_work_review.md",
  "content": "# Related Work 完整性审查\n\n**审查日期**: 2026-05-24\n**论文**: Structured Self-Consistency for Information Extraction\n\n## 当前覆盖情况\n\n- **已引用论文数量**: 约 40 篇（bib 文件中），Related Work 正文直接引用约 20 篇\n- **覆盖的主题领域**:\n  1. Test-time compute scaling / Best-of-N（Wang 2023, Snell 2025, Brown 2024）\n  2. Reward-free selectors / BoN scaling laws（Taubenfeld 2025, Kang 2025, Gao 2023）\n  3. Trained verifiers（Cobbe 2021, Lightman 2024）\n  4. Consistency for structured IE（Yao 2026, Xie 2023, Yun 2025）\n  5. Generative IE / constrained decoding（Zhou 2024 UniversalNER, Sainz 2024 GoLLIE, Willard 2023, Dong 2024 XGrammar）\n  6. MBR decoding（Eikema 2022, Eikema 2025）\n  7. Uncertainty / confidence estimation（Kuhn 2023, Geng 2024, Xia 2025 survey）\n  8. Selective prediction（Geifman 2017）\n\n## 建议补充的引用（按优先级排序）\n\n### P0（强烈建议）\n\n- **\"Uncertainty Quantification for Named Entity Recognition via Full-Sequence and Subsequence Conformal Prediction\"** (arXiv 2601.16999, Jan 2026) — 理由：直接针对 NER 的不确定性量化，使用 conformal prediction 提供有限样本覆盖保证，与本文的 QE 信号和 selective prediction 高度互补。本文声称 QE 信号可支持 abstention，该工作提供了更强的统计保证框架作为对比。\n\n- **\"Inference-Aware Fine-Tuning for Best-of-N Sampling in Large Language Models\"** (Chakraborty et al., ICLR 2025, arXiv 2412.15287) — 理由：提出针对 BoN 推理策略的训练方法，让模型在训练时就感知 BoN 选择过程。与本文的 \"fine-tuned model + stochastic sampling + selection\" 范式直接相关——本文在推理端做 selection，该工作在训练端优化 BoN，是互补方向。\n\n- **\"Beyond Majority Voting: LLM Aggregation by Leveraging Higher-Order Information\"** (arXiv 2510.01499, EMNLP 2025) — 理由：超越简单多数投票的 LLM 输出聚合方法，利用高阶信息（模型间相关性、预期准确率）。本文的 entity-level voting 是一种聚合策略，该工作提供了更系统的聚合理论框架。\n\n- **\"Assessment of Generative Named Entity Recognition in the Era of Large Language Models\"** (arXiv 2601.17898, Jan 2026) — 理由：对生成式 NER 在 LLM 时代的系统评估，覆盖 8 个 LLM 和 4 个标准 NER 数据集，展示 parameter-efficient finetuning + structured format 的竞争力。与本文使用 fine-tuned LLM 做生成式 NER 的实验设置直接对应。\n\n### P1（建议）\n\n- **\"Theoretical Guarantees for Minimum Bayes Risk Decoding\"** (arXiv 2502.12685, Jun 2025) — 理由：为 MBR 解码提供理论分析，解释其有效性。本文已引用 Eikema 2022/2025 的 MBR 工作，该理论分析可以加强 MBR 相关讨论的理论基础。\n\n- **\"Diversified Sampling Improves Scaling LLM Inference\"** (arXiv 2502.11027, 2025) — 理由：证明多样化采样改善推理扩展效果。与本文发现的 diversity collapse / LP compression 问题直接相关——如果采样多样性不足，扩展收益受限。\n\n- **\"s1: Simple Test-Time Scaling\"** (Muennighoff et al., EMNLP 2025) — 理由：已在 bib 中但未在 Related Work 正文中引用。作为简单有效的 test-time scaling 方法，值得在第一段提及。\n\n- **\"Draft-Conditioned Constrained Decoding for Structured Generation in LLMs\"** (arXiv 2603.03305, Mar 2026) — 理由：constrained decoding 的最新进展，与本文使用 XGrammar 做 constrained decoding 相关，但优先级较低因为本文的重点不在 decoding 方法本身。\n\n- **\"Conformal Prediction for Risk-Controlled Medical Entity Extraction Across Clinical Domains\"** (arXiv 2603.00924, Mar 2026) — 理由：将 conformal prediction 应用于 LLM-based entity extraction 的具体案例，与本文的 QE + abstention 方向相关。\n\n### P2（可选）\n\n- **\"EL4NER: Ensemble Learning for Named Entity Recognition via Multiple Small-Parameter Large Language Models\"** (arXiv 2505.23038, 2025) — 理由：多个小参数 LLM 的 NER 集成方法，与本文的单模型多采样方法形成对比，但方法论差异较大。\n\n- **\"Uncertainty-Aware Decoding with Minimum Bayes Risk\"** (arXiv 2503.05318, Mar 2025) — 理由：将 MBR 扩展为不确定性感知解码，与本文的 uncertainty estimation + MBR 结合有概念联系。\n\n- **\"Best-of-Majority: Minimax-Optimal Strategy for Pass@k Inference Scaling\"** (arXiv 2510.03199, 2025) — 理由：提出 BoM 策略（先多数投票过滤再 reward 选择），对本文的 selection 策略设计有参考价值，但针对的是 reasoning/code 而非 structured prediction。\n\n- **\"Iterative Deepening Sampling as Efficient Test-Time Scaling\"** (arXiv 2502.05449, Jun 2025) — 理由：提出 ID-sampling 提升 BoN 效率，与本文的采样效率问题相关但场景不同。\n\n- **Trust but Verify! A Survey on Verification Design for Test-time Scaling** (arXiv 2508.16665, Sep 2025) — 理由：test-time scaling 中 verifier 设计的综述，本文的 QE 信号可视为一种 verification 机制，但该综述主要面向 reasoning 任务。\n\n## 当前 Related Work 的优势和不足\n\n### 优势\n- **结构清晰**：三段式组织（test-time compute → structured IE consistency → uncertainty/MBR），逻辑递进\n- **定位精准**：每段末尾都明确指出本文与已有工作的区别（\"structured prediction requires different aggregation\"、\"without prompt engineering\"、\"degeneracy as the primary bottleneck\"）\n- **核心文献覆盖良好**：self-consistency 原始论文、Snell 2025 test-time scaling、Yao 2026 consistency-accuracy、Xie 2023 entity voting、Eikema MBR 系列均已引用\n- **篇幅控制得当**：约半页，符合 EMNLP long paper Related Work 的典型长度\n\n### 不足\n- **缺少 2025-2026 生成式 NER 评估文献**：本文在 fine-tuned LLM 上做生成式 NER，但未引用最新的生成式 NER 系统性评估（如 arXiv 2601.17898），使得实验设置的定位不够完整\n- **MBR 理论基础薄弱**：引用了 Eikema 2022/2025 但缺少 MBR 的理论保证文献，而本文的 selection 策略本质上是 MBR 的实例化\n- **缺少训练端优化的对比视角**：本文在推理端做 selection，但未提及 inference-aware fine-tuning（ICLR 2025）这一互补方向，读者可能质疑为何不在训练时直接优化 BoN\n- **聚合方法讨论不够系统**：entity-level voting 是核心贡献之一，但未引用 2025 年关于超越多数投票的聚合理论工作\n- **NER 不确定性量化的最新进展未覆盖**：conformal prediction for NER（2026）与本文的 QE + selective prediction 高度相关但未引用\n- **bib 中已有但正文未引用的遗漏**：`muennighoff2025s1`（s1: Simple Test-Time Scaling）在 bib 中存在但 Related Work 未提及\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_review_related-work-completeness_20260524T023100",
  "tool": "Write",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/related_work_review.md",
    "content": "# Related Work 完整性审查\n\n**审查日期**: 2026-05-24\n**论文**: Structured Self-Consistency for Information Extraction\n\n## 当前覆盖情况\n\n- **已引用论文数量**: 约 40 篇（bib 文件中），Related Work 正文直接引用约 20 篇\n- **覆盖的主题领域**:\n  1. Test-time compute scaling / Best-of-N（Wang 2023, Snell 2025, Brown 2024）\n  2. Reward-free selectors / BoN scaling laws（Taubenfeld 2025, Kang 2025, Gao 2023）\n  3. Trained verifiers（Cobbe 2021, Lightman 2024）\n  4. Consistency for structured IE（Yao 2026, Xie 2023, Yun 2025）\n  5. Generative IE / constrained decoding（Zhou 2024 UniversalNER, Sainz 2024 GoLLIE, Willard 2023, Dong 2024 XGrammar）\n  6. MBR decoding（Eikema 2022, Eikema 2025）\n  7. Uncertainty / confidence estimation（Kuhn 2023, Geng 2024, Xia 2025 survey）\n  8. Selective prediction（Geifman 2017）\n\n## 建议补充的引用（按优先级排序）\n\n### P0（强烈建议）\n\n- **\"Uncertainty Quantification for Named Entity Recognition via Full-Sequence and Subsequence Conformal Prediction\"** (arXiv 2601.16999, Jan 2026) — 理由：直接针对 NER 的不确定性量化，使用 conformal prediction 提供有限样本覆盖保证，与本文的 QE 信号和 selective prediction 高度互补。本文声称 QE 信号可支持 abstention，该工作提供了更强的统计保证框架作为对比。\n\n- **\"Inference-Aware Fine-Tuning for Best-of-N Sampling in Large Language Models\"** (Chakraborty et al., ICLR 2025, arXiv 2412.15287) — 理由：提出针对 BoN 推理策略的训练方法，让模型在训练时就感知 BoN 选择过程。与本文的 \"fine-tuned model + stochastic sampling + selection\" 范式直接相关——本文在推理端做 selection，该工作在训练端优化 BoN，是互补方向。\n\n- **\"Beyond Majority Voting: LLM Aggregation by Leveraging Higher-Order Information\"** (arXiv 2510.01499, EMNLP 2025) — 理由：超越简单多数投票的 LLM 输出聚合方法，利用高阶信息（模型间相关性、预期准确率）。本文的 entity-level voting 是一种聚合策略，该工作提供了更系统的聚合理论框架。\n\n- **\"Assessment of Generative Named Entity Recognition in the Era of Large Language Models\"** (arXiv 2601.17898, Jan 2026) — 理由：对生成式 NER 在 LLM 时代的系统评估，覆盖 8 个 LLM 和 4 个标准 NER 数据集，展示 parameter-efficient finetuning + structured format 的竞争力。与本文使用 fine-tuned LLM 做生成式 NER 的实验设置直接对应。\n\n### P1（建议）\n\n- **\"Theoretical Guarantees for Minimum Bayes Risk Decoding\"** (arXiv 2502.12685, Jun 2025) — 理由：为 MBR 解码提供理论分析，解释其有效性。本文已引用 Eikema 2022/2025 的 MBR 工作，该理论分析可以加强 MBR 相关讨论的理论基础。\n\n- **\"Diversified Sampling Improves Scaling LLM Inference\"** (arXiv 2502.11027, 2025) — 理由：证明多样化采样改善推理扩展效果。与本文发现的 diversity collapse / LP compression 问题直接相关——如果采样多样性不足，扩展收益受限。\n\n- **\"s1: Simple Test-Time Scaling\"** (Muennighoff et al., EMNLP 2025) — 理由：已在 bib 中但未在 Related Work 正文中引用。作为简单有效的 test-time scaling 方法，值得在第一段提及。\n\n- **\"Draft-Conditioned Constrained Decoding for Structured Generation in LLMs\"** (arXiv 2603.03305, Mar 2026) — 理由：constrained decoding 的最新进展，与本文使用 XGrammar 做 constrained decoding 相关，但优先级较低因为本文的重点不在 decoding 方法本身。\n\n- **\"Conformal Prediction for Risk-Controlled Medical Entity Extraction Across Clinical Domains\"** (arXiv 2603.00924, Mar 2026) — 理由：将 conformal prediction 应用于 LLM-based entity extraction 的具体案例，与本文的 QE + abstention 方向相关。\n\n### P2（可选）\n\n- **\"EL4NER: Ensemble Learning for Named Entity Recognition via Multiple Small-Parameter Large Language Models\"** (arXiv 2505.23038, 2025) — 理由：多个小参数 LLM 的 NER 集成方法，与本文的单模型多采样方法形成对比，但方法论差异较大。\n\n- **\"Uncertainty-Aware Decoding with Minimum Bayes Risk\"** (arXiv 2503.05318, Mar 2025) — 理由：将 MBR 扩展为不确定性感知解码，与本文的 uncertainty estimation + MBR 结合有概念联系。\n\n- **\"Best-of-Majority: Minimax-Optimal Strategy for Pass@k Inference Scaling\"** (arXiv 2510.03199, 2025) — 理由：提出 BoM 策略（先多数投票过滤再 reward 选择），对本文的 selection 策略设计有参考价值，但针对的是 reasoning/code 而非 structured prediction。\n\n- **\"Iterative Deepening Sampling as Efficient Test-Time Scaling\"** (arXiv 2502.05449, Jun 2025) — 理由：提出 ID-sampling 提升 BoN 效率，与本文的采样效率问题相关但场景不同。\n\n- **Trust but Verify! A Survey on Verification Design for Test-time Scaling** (arXiv 2508.16665, Sep 2025) — 理由：test-time scaling 中 verifier 设计的综述，本文的 QE 信号可视为一种 verification 机制，但该综述主要面向 reasoning 任务。\n\n## 当前 Related Work 的优势和不足\n\n### 优势\n- **结构清晰**：三段式组织（test-time compute → structured IE consistency → uncertainty/MBR），逻辑递进\n- **定位精准**：每段末尾都明确指出本文与已有工作的区别（\"structured prediction requires different aggregation\"、\"without prompt engineering\"、\"degeneracy as the primary bottleneck\"）\n- **核心文献覆盖良好**：self-consistency 原始论文、Snell 2025 test-time scaling、Yao 2026 consistency-accuracy、Xie 2023 entity voting、Eikema MBR 系列均已引用\n- **篇幅控制得当**：约半页，符合 EMNLP long paper Related Work 的典型长度\n\n### 不足\n- **缺少 2025-2026 生成式 NER 评估文献**：本文在 fine-tuned LLM 上做生成式 NER，但未引用最新的生成式 NER 系统性评估（如 arXiv 2601.17898），使得实验设置的定位不够完整\n- **MBR 理论基础薄弱**：引用了 Eikema 2022/2025 但缺少 MBR 的理论保证文献，而本文的 selection 策略本质上是 MBR 的实例化\n- **缺少训练端优化的对比视角**：本文在推理端做 selection，但未提及 inference-aware fine-tuning（ICLR 2025）这一互补方向，读者可能质疑为何不在训练时直接优化 BoN\n- **聚合方法讨论不够系统**：entity-level voting 是核心贡献之一，但未引用 2025 年关于超越多数投票的聚合理论工作\n- **NER 不确定性量化的最新进展未覆盖**：conformal prediction for NER（2026）与本文的 QE + selective prediction 高度相关但未引用\n- **bib 中已有但正文未引用的遗漏**：`muennighoff2025s1`（s1: Simple Test-Time Scaling）在 bib 中存在但 Related Work 未提及\n"
  }
}
```

</details>

---

### Tool result

_source line 38 · 2026-05-24T02:34:09.200563+00:00_

File created successfully at: /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/related_work_review.md

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_review_related-work-completeness_20260524T023100",
  "tool": "Write",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 39 · 2026-05-24T02:34:09.200694+00:00_

called mcp__agent-ml-research__register_artifact

<details open><summary>🔧 Tool call — mcp__agent-ml-research__register_artifact</summary>

```json
{
  "name": "related_work_review",
  "type": "report",
  "description": "Related Work 完整性审查报告：检查论文是否遗漏 2025-2026 关键相关工作，按 P0/P1/P2 优先级列出建议补充的引用",
  "project": "struct_self_consist_ie",
  "source_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/related_work_review.md",
  "tags": "['paper', 'related-work', 'review']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_review_related-work-completeness_20260524T023100",
  "tool": "mcp__agent-ml-research__register_artifact",
  "tool_args": {
    "name": "related_work_review",
    "type": "report",
    "description": "Related Work 完整性审查报告：检查论文是否遗漏 2025-2026 关键相关工作，按 P0/P1/P2 优先级列出建议补充的引用",
    "project": "struct_self_consist_ie",
    "source_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/related_work_review.md",
    "tags": "['paper', 'related-work', 'review']"
  }
}
```

</details>

---

### Tool result

_source line 40 · 2026-05-24T02:34:09.200845+00:00_

{"result":"{\"success\": true, \"data\": {\"artifact\": {\"id\": \"art_20260524_b09291\", \"name\": \"related_work_review\", \"type\": \"report\", \"description\": \"Related Work 完整性审查报告：检查论文是否遗漏 2025-2026 关键相关工作，按 P0/P1/P2 优先级列出建议补充的引用\", \"path\": \"projects/struct_self_consist_ie/artifacts/_project/report/related_work_review.md\", \"url\": null, \"project\": \"struct_self_consist_ie\", \"exp_id\": null, \"skill\": \"\", \"created_at\": \"2026-05-24T02:34:00.591030+00:00\", \"tags\": [\"paper\", \"related-work\", \"review\"]}, \"manifest\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/manifest.yaml\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_review_related-work-completeness_20260524T023100",
  "tool": "mcp__agent-ml-research__register_artifact",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 41 · 2026-05-24T02:34:09.201051+00:00_

审查完成。报告已写入 `artifacts/related_work_review.md`。

核心发现：

**P0 建议补充 4 篇**：
1. Conformal prediction for NER（arXiv 2601.16999）— 与本文 QE + selective prediction 直接互补
2. Inference-aware fine-tuning for BoN（ICLR 2025）— 训练端优化 BoN 的互补方向，reviewer 可能质疑
3. Beyond majority voting（EMNLP 2025）— 聚合理论框架，与 entity-level voting 直接相关
4. Assessment of generative NER（arXiv 2601.17898）— 生成式 NER 系统评估，与实验设置对应

**主要不足**：缺少训练端 BoN 优化的对比视角、NER 不确定性量化最新进展未覆盖、bib 中 `muennighoff2025s1` 已存在但正文未引用。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_review_related-work-completeness_20260524T023100"
}
```

</details>

---
