# research reference verification r22

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 87
- **Recorded user turns:** 0
- **Tool calls:** 43
- **Original source:** `logs/chats/worker_research_reference_verification_r22_20260519T040634.jsonl`
- **Structured JSON:** [`93fe89b176ed236cb056.json`](../../sessions/93/93fe89b176ed236cb056.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

87 recorded events

### Tool call

_source line 1 · 2026-05-19T04:13:04.849626+00:00_

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
  "session": "worker_research_reference_verification_r22_20260519T040634",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/references.bib"
  }
}
```

</details>

---

### Tool result

_source line 2 · 2026-05-19T04:13:04.850144+00:00_

1	% Auto-generated from literature_map.yaml — do not edit manually
2	
3	@inproceedings{vijayakumar2018diverse,
4	  title = {Diverse Beam Search for Improved Description of Complex Scenes},
5	  author = {Vijayakumar, Ashwin K. and Cogswell, Michael and Selvaraju, Ramprasaath R. and Sun, Qing and Lee, Stefan and Crandall, David J. and Batra, Dhruv},
6	  booktitle = {Proceedings of the AAAI Conference on Artificial Intelligence},
7	  year = {2018},
8	  url = {https://arxiv.org/abs/1610.02424}
9	}
10	
11	@inproceedings{shi2022mbr,
12	  title = {Natural Language to Code Translation with Execution},
13	  author = {Shi, Freda and Fried, Daniel and Ghazvininejad, Marjan and Zettlemoyer, Luke and Wang, Sida I.},
14	  booktitle = {Proceedings of the 2022 Conference on Empirical Methods in Natural Language Processing (EMNLP)},
15	  pages = {3533--3546},
16	  year = {2022},
17	  url = {https://arxiv.org/abs/2204.11454}
18	}
19	
20	@article{eisenstein2023helping,
21	  title = {Helping or Herding? Reward Model Ensembles Mitigate but do not Eliminate Reward Hacking},
22	  author = {Eisenstein, Jacob and Nagpal, Chirag and Agarwal, Alekh and Beirami, Ahmad and D'Amour, Alex and Dvijotham, DJ and Fisch, Adam and Heller, Katherine and Pfohl, Stephen and Ramachandran, Deepak and Shaw, Peter and Berant, Jonathan},
23	  journal = {arXiv preprint arXiv:2312.09244},
24	  year = {2023},
25	  url = {https://arxiv.org/abs/2312.09244}
26	}
27	
28	@article{brown2024monkeys,
29	  title = {Large Language Monkeys: Scaling Inference Compute with Repeated Sampling},
30	  author = {Brown, Bradley and Juravsky, Jordan and Ehrlich, Ryan and Clark, Ronald and Le, Quoc V. and Ré, Christopher and Mirhoseini, Azalia},
31	  journal = {arXiv preprint arXiv:2407.21787},
32	  year = {2024},
33	  url = {https://arxiv.org/abs/2407.21787}
34	}
35	
36	@inproceedings{chen2024usc,
37	  title = {Universal Self-Consistency for Large Language Model Generation},
38	  author = {Chen, Xinyun and Aksitov, Renat and Alon, 
…[truncated 28245 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_reference_verification_r22_20260519T040634",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-19T04:13:04.850374+00:00_

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
  "session": "worker_research_reference_verification_r22_20260519T040634",
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

_source line 4 · 2026-05-19T04:13:04.850520+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_reference_verification_r22_20260519T040634",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-19T04:13:04.850677+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Xie 2023 self-evaluation information extraction NLP"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_reference_verification_r22_20260519T040634",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Xie 2023 self-evaluation information extraction NLP"
  }
}
```

</details>

---

### Tool call

_source line 6 · 2026-05-19T04:13:04.850803+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Wan 2024 information extraction survey LLM"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_reference_verification_r22_20260519T040634",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Wan 2024 information extraction survey LLM"
  }
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-19T04:13:04.850924+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "ensemble NER entity-level aggregation voting multiple models"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_reference_verification_r22_20260519T040634",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ensemble NER entity-level aggregation voting multiple models"
  }
}
```

</details>

---

### Tool call

_source line 8 · 2026-05-19T04:13:04.851042+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Wang 2023 \"Self-Consistency Improves Chain of Thought\" ICLR"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_reference_verification_r22_20260519T040634",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Wang 2023 \"Self-Consistency Improves Chain of Thought\" ICLR"
  }
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-19T04:13:04.851195+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Cobbe 2021 \"Training Verifiers to Solve Math Word Problems\" arxiv"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_reference_verification_r22_20260519T040634",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Cobbe 2021 \"Training Verifiers to Solve Math Word Problems\" arxiv"
  }
}
```

</details>

---

### Tool call

_source line 10 · 2026-05-19T04:13:04.851345+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Eikema Aziz 2022 \"Sampling-Based Approximations to Minimum Bayes Risk\" EMNLP"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_reference_verification_r22_20260519T040634",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Eikema Aziz 2022 \"Sampling-Based Approximations to Minimum Bayes Risk\" EMNLP"
  }
}
```

</details>

---

### Tool result

_source line 11 · 2026-05-19T04:13:04.851487+00:00_

Web search results for query: "Xie 2023 self-evaluation information extraction NLP"

Links: [{"title":"A Survey on Open Information Extraction from Rule-based Model to Large Language Model","url":"https://arxiv.org/html/2208.08690v6"},{"title":"Assessing the quality of information extraction","url":"https://arxiv.org/html/2404.04068v1"},{"title":"Large language models for generative information extraction: a survey | Frontiers of Computer Science | Springer Nature Link","url":"https://link.springer.com/article/10.1007/s11704-024-40555-y"},{"title":"How To Implement Information Extraction Systems Made Simple","url":"https://spotintelligence.com/2023/10/10/information-extraction/"},{"title":"Large language models for generative information extraction: a survey","url":"https://journal.hep.com.cn/fcs/EN/10.1007/s11704-024-40555-y"},{"title":"Assessing the Performance of Chinese Open Source Large Language Models   in Information Extraction Tasks","url":"https://arxiv.org/pdf/2406.02079"},{"title":"Zero-shot information extraction from radiological reports using ChatGPT","url":"https://arxiv.org/pdf/2309.01398"},{"title":"Findings - EMNLP 2023","url":"https://2023.emnlp.org/program/accepted_findings/"}]

Based on the search results, I found relevant information about Xie et al. 2023 work on self-evaluation in NLP for information extraction:

Xie et al. proposed a training-free self-improving framework for information extraction tasks. The framework consists of three main steps: First, LLMs made predictions on unlabeled corpus, generating self-annotated dataset through self-consistency. Second, the authors explored different strategies to select reliable annotations. Finally, during inference, demonstrations from reliable self-annotated dataset were retrieved for in-context learning.

This approach was developed as part of efforts to employ LLMs for iterative self-verification and self-improvement, aiming to rectify the results when dealing with information extraction task
…[truncated 223 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_reference_verification_r22_20260519T040634",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-19T04:13:04.851654+00:00_

Web search results for query: "ensemble NER entity-level aggregation voting multiple models"

Links: [{"title":"EL4NER: Ensemble Learning for Named Entity Recognition via Multiple Small-Parameter Large Language Models","url":"https://arxiv.org/pdf/2505.23038"},{"title":"GitHub - chinhang0104/Ensemble-Learning-for-Named-Entity-Recognition: Utilize multiple Named Entity Recogniztion packages to detect human name and organization and # determine the final output by conducting a voting process among the NER packages.","url":"https://github.com/chinhang0104/Ensemble-Learning-for-Named-Entity-Recognition"},{"title":"EL4NER: Ensemble Learning for Named Entity Recognition via Multiple Small-Parameter Large Language Models","url":"https://arxiv.org/html/2505.23038"},{"title":"Combining multiple classifiers using vote based classifier ensemble technique for named entity recognition | Request PDF","url":"https://www.researchgate.net/publication/257026236_Combining_multiple_classifiers_using_vote_based_classifier_ensemble_technique_for_named_entity_recognition"},{"title":"Frontiers | Ensemble Named Entity Recognition (NER): Evaluating NER Tools in the Identification of Place Names in Historical Corpora","url":"https://www.frontiersin.org/journals/digital-humanities/articles/10.3389/fdigh.2018.00002/full"},{"title":"Combining multiple classifiers using vote based classifier ensemble technique for named entity recognition - ScienceDirect","url":"https://www.sciencedirect.com/science/article/abs/pii/S0169023X12000626"},{"title":"Local LLM Ensembles for Zero-shot Portuguese Named Entity Recognition","url":"https://arxiv.org/pdf/2512.10043"}]

I found relevant information about ensemble methods for Named Entity Recognition (NER) with entity-level aggregation and voting strategies. Here are the key findings:

## Ensemble NER Approaches

Ensemble learning for NER aims at aggregating the outputs of multiple open-source small-parameter LLMs to enhance overall performance in NER tasks.


…[truncated 1226 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_reference_verification_r22_20260519T040634",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 13 · 2026-05-19T04:13:04.851835+00:00_

Web search results for query: "Eikema Aziz 2022 "Sampling-Based Approximations to Minimum Bayes Risk" EMNLP"

Links: [{"title":"Sampling-Based Approximations to Minimum Bayes Risk Decoding for Neural Machine Translation - ACL Anthology","url":"https://aclanthology.org/2022.emnlp-main.754/"},{"title":"uncertainty-aware decoding with minimum bayes risk","url":"https://arxiv.org/pdf/2503.05318"},{"title":"GitHub - ZurichNLP/mbr: Minimum Bayes Risk Decoding for Hugging Face Transformers","url":"https://github.com/ZurichNLP/mbr"},{"title":"Re-evaluating Minimum Bayes Risk Decoding for ...","url":"https://openreview.net/pdf/25973aa13ecd7805ee8db1329de388d80a83054b.pdf"},{"title":"dblp: Bryan Eikema","url":"https://dblp.org/pid/223/9865.html"},{"title":"Sampling-Based Minimum Bayes Risk Decoding for Neural Machine Translation | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Sampling-Based-Minimum-Bayes-Risk-Decoding-for-Eikema-Aziz/994dbb06b970eb842b7782e4df75ca1633f83e4e"},{"title":"(PDF) Sampling-Based Approximations to Minimum Bayes Risk Decoding for Neural Machine Translation","url":"https://www.researchgate.net/publication/372923772_Sampling-Based_Approximations_to_Minimum_Bayes_Risk_Decoding_for_Neural_Machine_Translation"},{"title":"Publications · Bryan Eikema","url":"https://bryaneikema.com/publications/"},{"title":"[2108.04718] Sampling-Based Approximations to Minimum Bayes Risk Decoding for Neural Machine Translation","url":"https://arxiv.org/abs/2108.04718"}]

I found the paper you're looking for. "Sampling-Based Approximations to Minimum Bayes Risk Decoding for Neural Machine Translation" was published by Bryan Eikema and Wilker Aziz at EMNLP 2022 in Abu Dhabi, United Arab Emirates, appearing on pages 10978–10993.

The paper addresses problems with traditional decoding approaches in neural machine translation. The work notes that while NMT systems search for the mode of the model distribution, the mode and other high-probability translations fou
…[truncated 524 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_reference_verification_r22_20260519T040634",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-19T04:13:04.852006+00:00_

Web search results for query: "Cobbe 2021 "Training Verifiers to Solve Math Word Problems" arxiv"

Links: [{"title":"[2110.14168] Training Verifiers to Solve Math Word Problems","url":"https://arxiv.org/abs/2110.14168"},{"title":"Training Verifiers to Solve Math Word Problems","url":"https://matthiasplappert.com/publications/2021_Cobbe_Grade-School-Math.pdf"},{"title":"[2110.14168v2] Training Verifiers to Solve Math Word Problems","url":"https://arxiv.org/abs/2110.14168v2"},{"title":"[2110.14168v1] Training Verifiers to Solve Math Word Problems","url":"https://arxiv.org/abs/2110.14168v1"},{"title":"(Open Access) Training Verifiers to Solve Math Word Problems (2021) | Karl Cobbe | 2 Citations","url":"https://scispace.com/papers/training-verifiers-to-solve-math-word-problems-2jokilm0qa"},{"title":"[PDF] Training Verifiers to Solve Math Word Problems | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Training-Verifiers-to-Solve-Math-Word-Problems-Cobbe-Kosaraju/d6045d2ccc9c09ca1671348de86d07da6bc28eea"},{"title":"Training Verifiers to Solve Math Word Problems - ar5iv - arXiv","url":"https://ar5iv.labs.arxiv.org/html/2110.14168"},{"title":"Paper page - Training Verifiers to Solve Math Word Problems","url":"https://huggingface.co/papers/2110.14168"},{"title":"Training Verifiers to Solve Math Word Problems","url":"https://www.researchgate.net/publication/355698629_Training_Verifiers_to_Solve_Math_Word_Problems"}]

I found the paper you're looking for! Here's information about the Cobbe 2021 paper:

**Title:** Training Verifiers to Solve Math Word Problems

**Authors:** Karl Cobbe, Vineet Kosaraju, Mohammad Bavarian, Mark Chen, Heewoo Jun, Lukasz Kaiser, Matthias Plappert, Jerry Tworek, Jacob Hilton, Reiichiro Nakano, Christopher Hesse, and John Schulman

**arXiv ID:** 2110.14168

**Publication Date:** October 27, 2021

**Main Contributions:**

1. They introduce GSM8K, a dataset of 8.5K high quality linguistically diverse grade school math word problems

2. T
…[truncated 562 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_reference_verification_r22_20260519T040634",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 15 · 2026-05-19T04:13:04.852220+00:00_

Web search results for query: "Wang 2023 "Self-Consistency Improves Chain of Thought" ICLR"

Links: [{"title":"Self-Consistency Improves Chain of Thought Reasoning in Language Models","url":"https://www.cs.toronto.edu/~cmaddis/courses/csc2541_w25/presentations/self-consistency.pdf"},{"title":"Self-Consistency Improves Chain of Thought Reasoning in ...","url":"https://arxiv.org/pdf/2203.11171"},{"title":"Self-Consistency Improves Chain of Thought Reasoning in Language Models | OpenReview","url":"https://openreview.net/forum?id=1PL1NIMMrw"},{"title":"dblp: Self-Consistency Improves Chain of Thought Reasoning in Language Models.","url":"https://dblp.org/rec/conf/iclr/0002WSLCNCZ23.html"},{"title":"ICLR Poster Self-Consistency Improves Chain of Thought Reasoning in Language Models","url":"https://iclr.cc/virtual/2023/poster/11718"},{"title":"SELF-CONSISTENCY IMPROVES CHAIN OF THOUGHT ...","url":"http://webdocs.cs.ualberta.ca/~dale/papers/iclr23b.pdf"},{"title":"[2203.11171] Self-Consistency Improves Chain of Thought Reasoning in Language Models","url":"https://arxiv.org/abs/2203.11171"},{"title":"[PDF] Self-Consistency Improves Chain of Thought Reasoning in Language Models | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Self-Consistency-Improves-Chain-of-Thought-in-Wang-Wei/5f19ae1135a9500940978104ec15a5b8751bc7d2"},{"title":"Awesome-LLM-papers/00_Organizations/1_Google/2023 (Google) (ICLR) Self-Consistency Improves Chain of Thought Reasoning in Language Models.pdf at main · guyulongcs/Awesome-LLM-papers","url":"https://github.com/guyulongcs/Awesome-LLM-papers/blob/main/00_Organizations/1_Google/2023%20(Google)%20(ICLR)%20Self-Consistency%20Improves%20Chain%20of%20Thought%20Reasoning%20in%20Language%20Models.pdf"},{"title":"Self-Consistency Improves Chain of Thought Reasoning in Language Models","url":"https://iclr.cc/media/iclr-2023/Slides/11718.pdf"}]

I found the paper! Here's information about the Wang et al. 2023 "Self-Consistency Improves Chain of
…[truncated 1342 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_reference_verification_r22_20260519T040634",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-19T04:13:04.852408+00:00_

Web search results for query: "Wan 2024 information extraction survey LLM"

Links: [{"title":"Large language models for generative information extraction: a survey","url":"https://d-nb.info/1354655508/34"},{"title":"Large language models for generative information extraction: a survey","url":"https://journal.hep.com.cn/fcs/EN/10.1007/s11704-024-40555-y"},{"title":"Large language models for generative information extraction: a survey | Frontiers of Computer Science | Springer Nature Link","url":"https://link.springer.com/article/10.1007/s11704-024-40555-y"},{"title":"A Survey on Open Information Extraction from Rule-based ...","url":"https://aclanthology.org/2024.findings-emnlp.560.pdf"},{"title":"Large language models meet NLP: a survey | Frontiers of Computer Science | Springer Nature Link","url":"https://link.springer.com/article/10.1007/s11704-025-50472-3"},{"title":"[2312.17617] Large Language Models for Generative Information Extraction: A Survey","url":"https://arxiv.org/abs/2312.17617"},{"title":"Large Language Models for Generative Information Extraction: A Survey","url":"https://arxiv.org/html/2312.17617v3"},{"title":"(PDF) Large language models for generative information extraction: a survey","url":"https://www.researchgate.net/publication/385729624_Large_language_models_for_generative_information_extraction_a_survey"},{"title":"Large Language Models for Generative Information Extraction: A Survey","url":"https://arxiv.org/pdf/2312.17617"},{"title":"Large Language Model Applications for Health Information Extraction in Oncology: Scoping Review","url":"https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11970800/"}]

Based on the search results, I found comprehensive information about a 2024 survey on information extraction using Large Language Models (LLMs).

The survey covers Information Extraction (IE), which aims to extract structural knowledge from plain natural language texts, and demonstrates how generative Large Language Models (LLMs) have shown remarkable
…[truncated 1114 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_reference_verification_r22_20260519T040634",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-19T04:13:04.852584+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Xie 2023 \"self-consistency\" NER named entity recognition LLM"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_reference_verification_r22_20260519T040634",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Xie 2023 \"self-consistency\" NER named entity recognition LLM"
  }
}
```

</details>

---

### Tool call

_source line 18 · 2026-05-19T04:13:04.852710+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Wan 2024 arxiv 2312.17617 \"Large Language Models for Generative Information Extraction\" authors"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_reference_verification_r22_20260519T040634",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Wan 2024 arxiv 2312.17617 \"Large Language Models for Generative Information Extraction\" authors"
  }
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-19T04:13:04.852831+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"EL4NER\" ensemble learning named entity recognition LLM 2025 authors venue"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_reference_verification_r22_20260519T040634",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"EL4NER\" ensemble learning named entity recognition LLM 2025 authors venue"
  }
}
```

</details>

---

### Tool call

_source line 20 · 2026-05-19T04:13:04.852948+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Venktesh 2025 \"Trust but Verify\" test-time scaling survey arxiv"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_reference_verification_r22_20260519T040634",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Venktesh 2025 \"Trust but Verify\" test-time scaling survey arxiv"
  }
}
```

</details>

---

### Tool result

_source line 21 · 2026-05-19T04:13:04.853098+00:00_

Web search results for query: "Wan 2024 arxiv 2312.17617 "Large Language Models for Generative Information Extraction" authors"

Links: [{"title":"[2312.17617] Large Language Models for Generative Information Extraction: A Survey","url":"https://arxiv.org/abs/2312.17617"},{"title":"[2312.17617v3] Large Language Models for Generative Information Extraction: A Survey","url":"https://arxiv.org/abs/2312.17617v3"},{"title":"Large Language Models for Generative Information Extraction: A Survey - ADS","url":"https://ui.adsabs.harvard.edu/abs/arXiv:2312.17617"},{"title":"arXiv:2312.17617v1 [cs.CL] 29 Dec 2023","url":"https://arxiv.org/pdf/2312.17617"},{"title":"Large Language Models for Generative Information Extraction: A Survey","url":"https://arxiv.org/html/2312.17617v3"},{"title":"Large Language Models For Generative Information Extraction: A Survey | PDF | Conceptual Model | Artificial Intelligence","url":"https://www.scribd.com/document/784919375/2312-17617v2"},{"title":"Large language models for generative information extraction: a survey | Frontiers of Computer Science | Springer Nature Link","url":"https://link.springer.com/article/10.1007/s11704-024-40555-y"},{"title":"dblp: Large Language Models for Generative Information Extraction: A Survey.","url":"https://dblp.org/rec/journals/corr/abs-2312-17617.html"}]

The authors of the arXiv paper 2312.17617 "Large Language Models for Generative Information Extraction: A Survey" are Derong Xu, Wei Chen, Wenjun Peng, Chao Zhang, Tong Xu, Xiangyu Zhao, Xian Wu, Yefeng Zheng, Yang Wang, and Enhong Chen. The paper was submitted on December 29, 2023, with the latest revision on October 31, 2024.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_reference_verification_r22_20260519T040634",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 22 · 2026-05-19T04:13:04.853289+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Snell 2025 \"Scaling LLM Test-Time Compute\" ICLR arxiv 2408.03314"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_reference_verification_r22_20260519T040634",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Snell 2025 \"Scaling LLM Test-Time Compute\" ICLR arxiv 2408.03314"
  }
}
```

</details>

---

### Tool call

_source line 23 · 2026-05-19T04:13:04.853417+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Willard Louf 2023 \"Efficient Guided Generation\" arxiv 2307.09702"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_reference_verification_r22_20260519T040634",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Willard Louf 2023 \"Efficient Guided Generation\" arxiv 2307.09702"
  }
}
```

</details>

---

### Tool result

_source line 24 · 2026-05-19T04:13:04.853564+00:00_

Web search results for query: "Xie 2023 "self-consistency" NER named entity recognition LLM"

Links: [{"title":"[PDF] Self-Improving for Zero-Shot Named Entity Recognition with Large Language Models | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Self-Improving-for-Zero-Shot-Named-Entity-with-Xie-Li/d36e2b1f3d06a732773ace7b9cd786247d563fa7"},{"title":"GitHub - Emma1066/Self-Improve-Zero-Shot-NER: This is the github repository for the paper at NAACL 2024: Self-Improving for Zero-Shot Named Entity Recognition with Large Language Models. · GitHub","url":"https://github.com/Emma1066/Self-Improve-Zero-Shot-NER"},{"title":"Self-Improving for Zero-Shot Named Entity Recognition with Large Language Models","url":"https://arxiv.org/html/2311.08921v3"},{"title":"OEMA: Ontology-Enhanced Multi-Agent Collaboration Framework for Zero-Shot Clinical Named Entity Recognition","url":"https://arxiv.org/html/2511.15211"},{"title":"Self-Improving for Zero-Shot Named Entity Recognition with Large Language Models - ACL Anthology","url":"https://aclanthology.org/2024.naacl-short.49/"},{"title":"[2311.08921] Self-Improving for Zero-Shot Named Entity Recognition with Large Language Models","url":"https://arxiv.org/abs/2311.08921"},{"title":"Self-Improving for Zero-Shot Named Entity Recognition with Large   Language Models","url":"https://arxiv.org/pdf/2311.08921"},{"title":"Recent Advances in Named Entity Recognition: A Comprehensive Survey and Comparative Study","url":"https://arxiv.org/html/2401.10825v3"},{"title":"ReverseNER: Enabling Large Language Models to Self-Hint for Named Entity Recognition via the Reversed Process","url":"https://arxiv.org/html/2411.00533v4"}]

Based on the search results, I found information about the Xie 2023 paper on self-consistency for NER with LLMs:

## Paper Overview

The paper is titled "Self-Improving for Zero-Shot Named Entity Recognition with Large Language Models" by Tingyu Xie, Qi Li, Yan Zhang, Zuozhu Liu, and Hongwei Wang, published 
…[truncated 969 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_reference_verification_r22_20260519T040634",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 25 · 2026-05-19T04:13:04.853730+00:00_

Web search results for query: ""EL4NER" ensemble learning named entity recognition LLM 2025 authors venue"

Links: [{"title":"[2505.23038] EL4NER: Ensemble Learning for Named Entity Recognition via Multiple Small-Parameter Large Language Models","url":"https://arxiv.org/abs/2505.23038"},{"title":"EL4NER: Ensemble Learning for Named Entity Recognition ...","url":"https://bytez.com/docs/arxiv/2505.23038/paper"},{"title":"EL4NER: Ensemble Learning for Named Entity Recognition via Multiple Small-Parameter Large Language Models","url":"https://arxiv.org/html/2505.23038v1"},{"title":"EL4NER: Ensemble Learning for Named Entity ...","url":"https://arxiv.org/pdf/2505.23038"},{"title":"GitHub - junchenzhi/Awesome-LLM-Ensemble: A curated list of Awesome-LLM-Ensemble papers for the survey \"Harnessing Multiple Large Language Models: A Survey on LLM Ensemble\" · GitHub","url":"https://github.com/junchenzhi/Awesome-LLM-Ensemble"},{"title":"Ensemble Learning for Named Entity Recognition","url":"https://svn.aksw.org/papers/2014/ISWC_EL4NER/public.pdf"},{"title":"Local LLM Ensembles for Zero-shot Portuguese Named Entity Recognition","url":"https://arxiv.org/html/2512.10043v1"},{"title":"Ensemble of Deep Masked Language Models for Effective Named Entity Recognition in Health and Life Science Corpora","url":"https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8640190/"}]

Based on the search results, here's the information about EL4NER:

**Title:** EL4NER: Ensemble Learning for Named Entity Recognition via Multiple Small-Parameter Large Language Models

**Authors:** Yuzhen Xiao and 8 other authors

**Venue/Publication:** arXiv (paper 2505.23038), with a publication date of May 29, 2025

**Key Contributions:** The paper proposes a task decomposition-based pipeline that facilitates deep, multi-stage ensemble learning, a novel span-level sentence similarity algorithm for ICL demonstration retrieval, and a self-validation mechanism to mitigate noise during the ensemble process.

**Main Results:*
…[truncated 299 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_reference_verification_r22_20260519T040634",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 26 · 2026-05-19T04:13:04.853888+00:00_

Web search results for query: "Venktesh 2025 "Trust but Verify" test-time scaling survey arxiv"

Links: [{"title":"[2508.16665] Trust but Verify! A Survey on Verification Design for Test-time Scaling","url":"https://arxiv.org/abs/2508.16665"},{"title":"Trust but Verify! A Survey on Verification Design for Test-time Scaling","url":"https://arxiv.org/pdf/2508.16665"},{"title":"Trust but Verify! A Survey on Verification Design for Test-time Scaling","url":"https://openreview.net/pdf?id=sytEeAZYvf"},{"title":"Trust but Verify! A Survey on Verification Design for Test-time Scaling","url":"https://arxiv.org/html/2508.16665v3"},{"title":"Think Right, Not More: Test-Time Scaling for Numerical Claim Verification","url":"https://arxiv.org/pdf/2509.22101"}]

I found the paper you're looking for! Here's what I found:

"Trust but Verify! A Survey on Verification Design for Test-time Scaling" is authored by Venktesh V, Mandeep Rathee, and Avishek Anand. 

The survey focuses on test-time scaling (TTS) for Large Language Models, where by using more computational resources during inference, LLMs can improve their reasoning process and task performance. It examines approaches such as distilling reasoning traces from another model or exploring the decoding search space by employing a verifier, where verifiers serve as reward models that help score candidate outputs to explore the solution space and select the best outcome.

The paper is available on arXiv with identifier 2508.16665. The most recent version (v3) was updated on September 9, 2025.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_reference_verification_r22_20260519T040634",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 27 · 2026-05-19T04:13:04.854052+00:00_

Web search results for query: "Willard Louf 2023 "Efficient Guided Generation" arxiv 2307.09702"

Links: [{"title":"[2307.09702v2] Efficient Guided Generation for Large Language Models","url":"https://arxiv.org/abs/2307.09702v2"},{"title":"[PDF] Efficient Guided Generation for Large Language Models | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Efficient-Guided-Generation-for-Large-Language-Willard-Louf/c4ceaef35bca063815f50d90a087acbd07a65478"},{"title":"[2307.09702v1] Efficient Guided Generation for LLMs","url":"https://arxiv.org/abs/2307.09702v1"},{"title":"[2307.09702] Efficient Guided Generation for Large Language Models","url":"https://arxiv.org/abs/2307.09702"},{"title":"Efficient Guided Generation for Large Language Models","url":"https://www.researchhub.com/paper/1278292/efficient-guided-generation-for-large-language-models"},{"title":"Paper page - Efficient Guided Generation for Large Language Models","url":"https://huggingface.co/papers/2307.09702"},{"title":"[2307.09702v3] Efficient Guided Generation for Large Language Models","url":"https://arxiv.org/abs/2307.09702v3"},{"title":"Efficient Guided Generation for LLMs Brandon T. Willard1 and R´emi Louf2","url":"https://arxiv.org/pdf/2307.09702v1"},{"title":"Efficient Guided Generation for Large Language Models","url":"https://arxiv.org/pdf/2307.09702"},{"title":"(PDF) Efficient Guided Generation for LLMs","url":"https://www.researchgate.net/publication/372468267_Efficient_Guided_Generation_for_LLMs"}]

I found the paper! Here are the key details about the paper you searched for:

**Title:** "Efficient Guided Generation for Large Language Models"

**Authors:** Brandon T. Willard and Rémi Louf

**Publication:** Submitted on July 19, 2023

**Abstract:** The paper shows how the problem of neural text generation can be constructively reformulated in terms of transitions between the states of a finite-state machine. This framework leads to an efficient approach to guiding text generation with r
…[truncated 724 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_reference_verification_r22_20260519T040634",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 28 · 2026-05-19T04:13:04.854258+00:00_

Web search results for query: "Snell 2025 "Scaling LLM Test-Time Compute" ICLR arxiv 2408.03314"

Links: [{"title":"Published as a conference paper at ICLR 2025 LEARNING HOW HARD TO THINK:","url":"https://proceedings.iclr.cc/paper_files/paper/2025/file/ff414825df833edb8b1839e3d5d495e9-Paper-Conference.pdf"},{"title":"[2408.03314] Scaling LLM Test-Time Compute Optimally can be More Effective than Scaling Model Parameters","url":"https://arxiv.org/abs/2408.03314"},{"title":"GitHub - adikal25/Scaling-LLM-Test-Time-Compute-Optimally-can-be-More-Effective-than-Scaling-Model-Parameters · GitHub","url":"https://github.com/adikal25/Scaling-LLM-Test-Time-Compute-Optimally-can-be-More-Effective-than-Scaling-Model-Parameters"},{"title":"[2408.03314v1] Scaling LLM Test-Time Compute Optimally can be More Effective than Scaling Model Parameters","url":"https://arxiv.org/abs/2408.03314v1"},{"title":"Scaling LLM Test-Time Compute Optimally can be More Effective than Scaling Model Parameters","url":"https://arxiv.org/html/2408.03314v1"},{"title":"Paper page - Scaling LLM Test-Time Compute Optimally can be More Effective than Scaling Model Parameters","url":"https://huggingface.co/papers/2408.03314"},{"title":"(PDF) Scaling LLM Test-Time Compute Optimally can be More Effective than Scaling Model Parameters","url":"https://www.researchgate.net/publication/382914793_Scaling_LLM_Test-Time_Compute_Optimally_can_be_More_Effective_than_Scaling_Model_Parameters"},{"title":"Rethinking Fine-Tuning when Scaling Test-Time Compute: Limiting Confidence Improves Mathematical Reasoning","url":"https://arxiv.org/pdf/2502.07154"},{"title":"Scaling LLM Test-Time Compute Optimally Can be More Effective than Scaling Parameters for Reasoning | OpenReview","url":"https://openreview.net/forum?id=4FWAwZtd2n"}]

I found the paper you're looking for! Here are the key details:

**Paper Information:**
The paper is authored by Charlie Snell, Jaehoon Lee, Kelvin Xu, and Aviral Kumar. It was submitted to arXiv as 
…[truncated 922 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_reference_verification_r22_20260519T040634",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 29 · 2026-05-19T04:13:04.854436+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Xie 2023 self-evaluation beam search NER information extraction arxiv"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_reference_verification_r22_20260519T040634",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Xie 2023 self-evaluation beam search NER information extraction arxiv"
  }
}
```

</details>

---

### Tool call

_source line 30 · 2026-05-19T04:13:04.854562+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"Wan\" author 2024 information extraction survey NER RE EE"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_reference_verification_r22_20260519T040634",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"Wan\" author 2024 information extraction survey NER RE EE"
  }
}
```

</details>

---

### Tool call

_source line 31 · 2026-05-19T04:13:04.854681+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Zheng 2024 \"LlamaFactory\" ACL demo arxiv"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_reference_verification_r22_20260519T040634",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Zheng 2024 \"LlamaFactory\" ACL demo arxiv"
  }
}
```

</details>

---

### Tool call

_source line 32 · 2026-05-19T04:13:04.854797+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Luan 2018 \"Multi-Task Identification of Entities Relations Coreference\" SciERC EMNLP"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_reference_verification_r22_20260519T040634",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Luan 2018 \"Multi-Task Identification of Entities Relations Coreference\" SciERC EMNLP"
  }
}
```

</details>

---

### Tool call

_source line 33 · 2026-05-19T04:13:04.854912+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Derczynski 2017 \"WNUT2017 Shared Task Novel Emerging Entity Recognition\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_reference_verification_r22_20260519T040634",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Derczynski 2017 \"WNUT2017 Shared Task Novel Emerging Entity Recognition\""
  }
}
```

</details>

---

### Tool call

_source line 34 · 2026-05-19T04:13:04.855024+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "NER ensemble multiple models entity consensus aggregation 2023 2024 ACL EMNLP"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_reference_verification_r22_20260519T040634",
  "tool": "WebSearch",
  "tool_args": {
    "query": "NER ensemble multiple models entity consensus aggregation 2023 2024 ACL EMNLP"
  }
}
```

</details>

---

### Tool result

_source line 35 · 2026-05-19T04:13:04.855181+00:00_

Web search results for query: "Zheng 2024 "LlamaFactory" ACL demo arxiv"

Links: [{"title":"LlamaFactory: Unified Efficient Fine-Tuning of 100+ Language Models - ACL Anthology","url":"https://aclanthology.org/2024.acl-demos.38/"},{"title":"GitHub - hiyouga/LlamaFactory: Unified Efficient Fine-Tuning of 100+ LLMs & VLMs (ACL 2024) · GitHub","url":"https://github.com/hiyouga/LLaMAFactory"},{"title":"Accepted Demo Papers - ACL 2024","url":"https://2024.aclweb.org/program/demo_papers/"},{"title":"[PDF] LlamaFactory: Unified Efficient Fine-Tuning of 100+ Language Models | Semantic Scholar","url":"https://www.semanticscholar.org/paper/LlamaFactory:-Unified-Efficient-Fine-Tuning-of-100+-Zheng-Zhang/d5d7b26dbdf09737878644530b226a79c9f43bfb"},{"title":"KALE: Enhancing Knowledge Manipulation in Large Language Models via Knowledge-aware Learning","url":"https://arxiv.org/html/2601.07430v1"},{"title":"[2403.13372] LlamaFactory: Unified Efficient Fine-Tuning of 100+ Language Models","url":"https://arxiv.org/abs/2403.13372"},{"title":"Paper page - LlamaFactory: Unified Efficient Fine-Tuning of 100+ Language Models","url":"https://huggingface.co/papers/2403.13372"},{"title":"LlamaFactory: Unified Efficient Fine-Tuning of 100+ Language Models - ADS","url":"https://ui.adsabs.harvard.edu/abs/2024arXiv240313372Z/abstract"},{"title":"Unified Efficient Fine-Tuning of 100+ Language Models","url":"https://aclanthology.org/2024.acl-demos.38.pdf"}]

Based on the search results, I found the paper you're looking for:

**LlamaFactory: Unified Efficient Fine-Tuning of 100+ Language Models** by Yaowei Zheng, Richong Zhang, Junhao Zhang, Yanhan Ye, and Zheyan Luo was published in the Proceedings of the 62nd Annual Meeting of the Association for Computational Linguistics (Volume 3: System Demonstrations) in August 2024.

The paper was submitted to arXiv on March 20, 2024 (arxiv paper 2403.13372).

LlamaFactory is a unified framework that integrates a suite of cutting-edge efficient training method
…[truncated 382 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_reference_verification_r22_20260519T040634",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 36 · 2026-05-19T04:13:04.855362+00:00_

Web search results for query: ""Wan" author 2024 information extraction survey NER RE EE"

Links: [{"title":"Large language models for generative information extraction: a survey","url":"https://d-nb.info/1354655508/34"},{"title":"GitHub - zjunlp/Low-resource-KEPapers: A Paper List of Low-resource Information Extraction","url":"https://github.com/zjunlp/Low-resource-KEPapers"},{"title":"Large Language Models for Generative Information Extraction: A Survey","url":"https://arxiv.org/html/2312.17617v3"},{"title":"GitHub - quqxui/Awesome-LLM4IE-Papers: Awesome papers about generative Information Extraction (IE) using Large Language Models (LLMs) · GitHub","url":"https://github.com/quqxui/Awesome-LLM4IE-Papers"},{"title":"Information Extraction in Low-Resource Scenarios: Survey and Perspective","url":"https://arxiv.org/html/2202.08063v6"},{"title":"A Study of Recent Contributions on Information Extraction","url":"https://arxiv.org/pdf/1803.05667"},{"title":"A Comprehensive Survey on Document-Level Information ...","url":"https://aclanthology.org/2024.futured-1.6.pdf"},{"title":"(PDF) Large language models for generative information extraction: a survey","url":"https://www.researchgate.net/publication/385729624_Large_language_models_for_generative_information_extraction_a_survey"},{"title":"Recent Advances in Named Entity Recognition: A Comprehensive Survey and Comparative Study","url":"https://arxiv.org/html/2401.10825v3"}]

Based on the search results, I found relevant information about a 2024 information extraction survey. The survey "Large language models for generative information extraction: A survey" was authored by Xu, Derong, Chen, Wei, Peng, Wenjun, Zhang, Chao, Xu, Tong, Zhao, Xiangyu, Wu, Xian, Zheng, Yefeng, Wang, Yang, and Chen, Enhong, published in Frontiers of Computer Science in 2024.

The survey focuses on how Information Extraction (IE) aims to extract structural knowledge from plain natural language texts, and how generative Large Language Models (LLMs
…[truncated 495 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_reference_verification_r22_20260519T040634",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 37 · 2026-05-19T04:13:04.855536+00:00_

Web search results for query: "Xie 2023 self-evaluation beam search NER information extraction arxiv"

Links: [{"title":"[PDF] Self-Evaluation Guided Beam Search for Reasoning | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Self-Evaluation-Guided-Beam-Search-for-Reasoning-Xie-Kawaguchi/ef018d9fad6167cfddb7d6654c5422df1e953730"},{"title":"Self-Evaluation Guided Beam Search for Reasoning","url":"https://proceedings.neurips.cc/paper_files/paper/2023/hash/81fde95c4dc79188a69ce5b24d63010b-Abstract-Conference.html"},{"title":"[2305.00633] Self-Evaluation Guided Beam Search for Reasoning","url":"https://arxiv.org/abs/2305.00633"},{"title":"Self-Evaluation Guided Beam Search for Reasoning Yuxi Xie1∗ Kenji Kawaguchi1","url":"https://arxiv.org/pdf/2305.00633"},{"title":"Large Language Models for Generative Information Extraction: A Survey","url":"https://arxiv.org/html/2312.17617v3"},{"title":"Self-Evaluation Guided Beam Search for Reasoning","url":"https://papers.nips.cc/paper_files/paper/2023/hash/81fde95c4dc79188a69ce5b24d63010b-Abstract-Conference.html"},{"title":"Speaker: Yuxi Xie Self-Evaluation Guided Beam Search for Reasoning","url":"https://neurips.cc/media/neurips-2023/Slides/72456.pdf"},{"title":"Self-evaluation guided beam search for reasoning | Proceedings of the 37th International Conference on Neural Information Processing Systems","url":"https://dl.acm.org/doi/10.5555/3666122.3667924"},{"title":"Recent Advances in Named Entity Recognition: A Comprehensive Survey and Comparative Study","url":"https://arxiv.org/html/2401.10825v3"}]

Based on the search results, I found information about Xie et al. 2023, though the primary paper appears to focus on reasoning rather than NER directly:

## Primary Paper: Self-Evaluation Guided Beam Search for Reasoning

The main Xie et al. 2023 paper introduces a stepwise self-evaluation mechanism to guide and calibrate the reasoning process of LLMs, proposing a decoding algorithm integrating self-evaluation guidan
…[truncated 1059 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_reference_verification_r22_20260519T040634",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 38 · 2026-05-19T04:13:04.855714+00:00_

Web search results for query: "Luan 2018 "Multi-Task Identification of Entities Relations Coreference" SciERC EMNLP"

Links: [{"title":"Multi-Task Identification of Entities, Relations, and Coreference for Scientific Knowledge Graph Construction - ACL Anthology","url":"https://aclanthology.org/D18-1360/"},{"title":"[PDF] Multi-Task Identification of Entities, Relations, and Coreference for Scientific Knowledge Graph Construction | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Multi-Task-Identification-of-Entities,-Relations,-Luan-He/b21b927c251c415b601b6d7f785a42cc5c292635"},{"title":"Evaluating LLMs for Named Entity Recognition in Scientific ...","url":"https://oro.open.ac.uk/105348/1/105348.pdf"},{"title":"Multi-Task Identification of Entities, Relations, and Coreference for Scientific Knowledge Graph Construction - Consensus","url":"https://k8s.consensus.app/papers/details/ce11b64546755e678612cfea3b404121/"},{"title":"[1808.09602] Multi-Task Identification of Entities, Relations, and Coreference for Scientific Knowledge Graph Construction","url":"https://arxiv.org/abs/1808.09602"},{"title":"[1808.09602v1] Multi-Task Identification of Entities, Relations, and Coreference for Scientific Knowledge Graph Construction","url":"https://arxiv.org/abs/1808.09602v1"},{"title":"Multi-Task Identification of Entities, Relations, and Coreference for   Scientific Knowledge Graph Construction","url":"https://arxiv.org/pdf/1808.09602"},{"title":"SciERC/README.md at master · YerevaNN/SciERC","url":"https://github.com/YerevaNN/SciERC/blob/master/README.md"},{"title":"Multi-Task Identification of Entities, Relations, and Coreference for Scientific Knowledge Graph Construction","url":"https://www.researchgate.net/publication/334115742_Multi-Task_Identification_of_Entities_Relations_and_Coreference_for_Scientific_Knowledge_Graph_Construction"},{"title":"dblp: Multi-Task Identification of Entities, Relations, and Coreference for Scientific Knowledge Graph Construction.
…[truncated 1398 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_reference_verification_r22_20260519T040634",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 39 · 2026-05-19T04:13:04.855892+00:00_

Web search results for query: "Derczynski 2017 "WNUT2017 Shared Task Novel Emerging Entity Recognition""

Links: [{"title":"Results of the WNUT2017 Shared Task on Novel and Emerging Entity Recognition - Royal Netherlands Academy of Arts and Sciences (KNAW)","url":"https://pure.knaw.nl/portal/en/publications/results-of-the-wnut2017-shared-task-on-novel-and-emerging-entity-"},{"title":"leondz/wnut_17 · Datasets at Hugging Face","url":"https://huggingface.co/datasets/leondz/wnut_17"},{"title":"[PDF] Results of the WNUT2017 Shared Task on Novel and Emerging Entity Recognition | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Results-of-the-WNUT2017-Shared-Task-on-Novel-and-Derczynski-Nichols/72e87913632d0f1295fbcfa46795c5bb26d0a422"},{"title":"Emerging and Rare Entity Recognition","url":"http://noisy-text.github.io/2017/emerging-rare-entities.html"},{"title":"Results of the WNUT2017 Shared Task on Novel and Emerging Entity Recognition - ACL Anthology","url":"https://aclanthology.org/W17-4418/"},{"title":"GitHub - leondz/emerging_entities_17: Dataset for the Emerging & Novel Entity NER task (WNUT '17) · GitHub","url":"https://github.com/leondz/emerging_entities_17"},{"title":"Results of the WNUT2017 Shared Task on Novel and Emerging Entity Recognition | Request PDF","url":"https://www.researchgate.net/publication/322590094_Results_of_the_WNUT2017_Shared_Task_on_Novel_and_Emerging_Entity_Recognition"},{"title":"Results of the WNUT2017 Shared Task on Novel and Emerging Entity Recognition | Papers With Code","url":"https://paperswithcode.com/paper/results-of-the-wnut2017-shared-task-on-novel"},{"title":"Results of the WNUT2017 Shared Task on Novel and Emerging Entity Recognition","url":"https://noisy-text.github.io/2017/pdf/WNUT18.pdf"},{"title":"Results of the WNUT2017 Shared Task on Novel and Emerging Entity Recognition","url":"https://www.derczynski.com/sheffield/papers/emerging-wnut.pdf"}]

I found the paper you're looking for. Here's the information abou
…[truncated 1170 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_reference_verification_r22_20260519T040634",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 40 · 2026-05-19T04:13:04.856061+00:00_

Web search results for query: "NER ensemble multiple models entity consensus aggregation 2023 2024 ACL EMNLP"

Links: [{"title":"Exploring Nested Named Entity Recognition with Large Language Models: Methods, Challenges, and Insights - ACL Anthology","url":"https://aclanthology.org/2024.emnlp-main.492/"},{"title":"The 2024 Conference on Empirical Methods in Natural Language Processing - ACL Anthology","url":"https://aclanthology.org/events/emnlp-2024/"},{"title":"EL4NER: Ensemble Learning for Named Entity Recognition via Multiple Small-Parameter Large Language Models","url":"https://arxiv.org/pdf/2505.23038"},{"title":"EL4NER: Ensemble Learning for Named Entity Recognition via Multiple Small-Parameter Large Language Models","url":"https://arxiv.org/html/2505.23038"},{"title":"Ensemble of Deep Masked Language Models for Effective Named Entity Recognition in Health and Life Science Corpora","url":"https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8640190/"}]

Based on the web search results, here are some relevant papers on NER ensemble and consensus aggregation approaches from recent conferences:

## Key Papers Found:

1. **EL4NER: Ensemble Learning for Named Entity Recognition via Multiple Small-Parameter Large Language Models**
   
   This paper proposes an ensemble learning method for NER that aggregates the outputs of multiple open-source, small-parameter LLMs to enhance overall performance in NER tasks at less deployment and inference cost. The method comprises three key components: a task decomposition-based pipeline for multi-stage ensemble learning, a novel span-level sentence similarity algorithm for demonstration retrieval, and a self-validation mechanism to mitigate noise during the ensemble process. The results indicate that EL4NER surpasses most closed-source, large-parameter LLM-based methods at a lower parameter cost and attains state-of-the-art performance among in-context learning-based methods on certain datasets.

2. **Exploring Nested Named Entity Recog
…[truncated 932 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_reference_verification_r22_20260519T040634",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool call

_source line 41 · 2026-05-19T04:13:04.856253+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"Wan\" first author 2024 survey \"information extraction\" LLM arxiv"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_reference_verification_r22_20260519T040634",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"Wan\" first author 2024 survey \"information extraction\" LLM arxiv"
  }
}
```

</details>

---

### Tool call

_source line 42 · 2026-05-19T04:13:04.856380+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Xie Kawaguchi 2023 \"Self-Evaluation Guided Beam Search\" NeurIPS authors"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_reference_verification_r22_20260519T040634",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Xie Kawaguchi 2023 \"Self-Evaluation Guided Beam Search\" NeurIPS authors"
  }
}
```

</details>

---

### Tool call

_source line 43 · 2026-05-19T04:13:04.856506+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"multi-sample\" OR \"multiple outputs\" NER entity aggregation voting LLM 2023 2024"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_reference_verification_r22_20260519T040634",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"multi-sample\" OR \"multiple outputs\" NER entity aggregation voting LLM 2023 2024"
  }
}
```

</details>

---

### Tool call

_source line 44 · 2026-05-19T04:13:04.856625+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "entity-level ensemble NER majority vote span aggregation recent paper"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_reference_verification_r22_20260519T040634",
  "tool": "WebSearch",
  "tool_args": {
    "query": "entity-level ensemble NER majority vote span aggregation recent paper"
  }
}
```

</details>

---

### Tool result

_source line 45 · 2026-05-19T04:13:04.856772+00:00_

Web search results for query: "Xie Kawaguchi 2023 "Self-Evaluation Guided Beam Search" NeurIPS authors"

Links: [{"title":"Self-Evaluation Guided Beam Search for Reasoning","url":"https://proceedings.neurips.cc/paper_files/paper/2023/hash/81fde95c4dc79188a69ce5b24d63010b-Abstract-Conference.html"},{"title":"Self-Evaluation Guided Beam Search for Reasoning","url":"https://papers.nips.cc/paper_files/paper/2023/hash/81fde95c4dc79188a69ce5b24d63010b-Abstract-Conference.html"},{"title":"[Quick Review] Self-Evaluation Guided Beam Search for Reasoning","url":"https://liner.com/review/selfevaluation-guided-beam-search-for-reasoning"},{"title":"[PDF] Self-Evaluation Guided Beam Search for Reasoning | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Self-Evaluation-Guided-Beam-Search-for-Reasoning-Xie-Kawaguchi/ef018d9fad6167cfddb7d6654c5422df1e953730"},{"title":"Self-Evaluation Guided Beam Search for Reasoning | OpenReview","url":"https://openreview.net/forum?id=Bw82hwg5Q3"},{"title":"[2305.00633] Self-Evaluation Guided Beam Search for Reasoning","url":"https://arxiv.org/abs/2305.00633"},{"title":"Self-Evaluation Guided Beam Search for Reasoning Yuxi Xie1∗ Kenji Kawaguchi1","url":"https://proceedings.neurips.cc/paper_files/paper/2023/file/81fde95c4dc79188a69ce5b24d63010b-Paper-Conference.pdf"},{"title":"Self-Evaluation Guided Beam Search for Reasoning","url":"https://arxiv.org/pdf/2305.00633"}]

Based on the search results, I found the paper "Self-Evaluation Guided Beam Search for Reasoning" published at NeurIPS 2023.

**Authors:** Yuxi Xie, Kenji Kawaguchi, Yiran Zhao, James Xu Zhao, Min-Yen Kan, Junxian He, and Michael Xie

**Publication:** Advances in Neural Information Processing Systems 36 (NeurIPS 2023) Main Conference Track

**Main Contribution:** The paper proposes a decoding algorithm integrating self-evaluation guidance via stochastic beam search, where the self-evaluation guidance serves as a better-calibrated automatic criterion, facilitating an eff
…[truncated 314 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_reference_verification_r22_20260519T040634",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 46 · 2026-05-19T04:13:04.856938+00:00_

Web search results for query: ""Wan" first author 2024 survey "information extraction" LLM arxiv"

Links: [{"title":"Large language models for generative information extraction: a survey","url":"https://journal.hep.com.cn/fcs/EN/10.1007/s11704-024-40555-y"},{"title":"Reflect then Learn: Active Prompting for Information Extraction Guided by Introspective Confusion","url":"https://arxiv.org/html/2508.10036v1"},{"title":"A Survey on Open Information Extraction from Rule-based Model to Large Language Model","url":"https://arxiv.org/html/2208.08690v7"},{"title":"[2312.17617] Large Language Models for Generative Information Extraction: A Survey","url":"https://arxiv.org/abs/2312.17617"},{"title":"Large Language Models for Generative Information Extraction: A Survey","url":"https://arxiv.org/html/2312.17617v3"},{"title":"[2402.02420] Factuality of Large Language Models: A Survey","url":"https://arxiv.org/abs/2402.02420"},{"title":"Large Language Models for Generative Information Extraction: A Survey","url":"https://arxiv.org/pdf/2312.17617"},{"title":"From Automation to Autonomy: A Survey on Large Language Models in Scientific Discovery","url":"https://arxiv.org/html/2505.13259v1"},{"title":"Large language models for generative information extraction: a survey | Frontiers of Computer Science | Springer Nature Link","url":"https://link.springer.com/article/10.1007/s11704-024-40555-y"}]

Based on the search results, I found a relevant 2024 survey on information extraction with LLMs. The most prominent match appears to be:

"Large Language Models for Generative Information Extraction: A Survey" authored by Derong Xu, Wei Chen, Wenjun Peng, Chao Zhang, Tong Xu, Xiangyu Zhao, Xian Wu, Yefeng Zheng, Yang Wang, and Enhong Chen, published on arXiv (2312.17617).

However, this paper's first author is Derong Xu, not "Wan". 

I also found a reference in the search results to Han et al. (2024) including Wan, X. as a co-author, with the paper titled "An Empirical Study on Information E
…[truncated 458 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_reference_verification_r22_20260519T040634",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 47 · 2026-05-19T04:13:04.857141+00:00_

Web search results for query: "entity-level ensemble NER majority vote span aggregation recent paper"

Links: [{"title":"Combining multiple classifiers using vote based classifier ensemble technique for named entity recognition | Request PDF","url":"https://www.researchgate.net/publication/257026236_Combining_multiple_classifiers_using_vote_based_classifier_ensemble_technique_for_named_entity_recognition"},{"title":"Local LLM Ensembles for Zero-shot Portuguese Named Entity Recognition","url":"https://arxiv.org/html/2512.10043"},{"title":"EL4NER: Ensemble Learning for Named Entity Recognition via Multiple Small-Parameter Large Language Models","url":"https://arxiv.org/pdf/2505.23038"},{"title":"SpanNER: Named Entity Re-/Recognition as Span Prediction","url":"https://arxiv.org/pdf/2106.00641"},{"title":"The majority voting strategy to ensemble NER models. BERT:... | Download Scientific Diagram","url":"https://www.researchgate.net/figure/The-majority-voting-strategy-to-ensemble-NER-models-BERT-bidirectional-encoder_fig1_347087784"},{"title":"A Weighted Majority Voting Ensemble Approach for Classification | Request PDF","url":"https://www.researchgate.net/publication/337509150_A_Weighted_Majority_Voting_Ensemble_Approach_for_Classification"},{"title":"Ensemble of Deep Masked Language Models for Effective Named Entity Recognition in Health and Life Science Corpora","url":"https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8640190/"}]

I found several relevant papers on entity-level ensemble NER with majority voting and span aggregation. Here are the most recent findings:

**Recent Papers:**

1. **Local LLM Ensembles for Zero-shot Portuguese Named Entity Recognition (December 2025)**: This paper describes a method where LLMs vote on whether entities are correct, with majority vote determining correct entities, and majority vote also used to decide on the best fit for entity spans.

2. **EL4NER: Ensemble Learning for Named Entity Recognition via Multiple Small-Parameter Large La
…[truncated 1090 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_reference_verification_r22_20260519T040634",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 48 · 2026-05-19T04:13:04.857322+00:00_

Web search results for query: ""multi-sample" OR "multiple outputs" NER entity aggregation voting LLM 2023 2024"

Links: [{"title":"Beyond Majority Voting: LLM Aggregation by Leveraging Higher-Order Information","url":"https://arxiv.org/html/2510.01499v1"},{"title":"Cost-aware LLM-based Online Dataset Annotation","url":"http://users.ece.cmu.edu/~oyagan/Journals/LLMRouting.pdf"},{"title":"EL4NER: Ensemble Learning for Named Entity Recognition via Multiple Small-Parameter Large Language Models","url":"https://arxiv.org/pdf/2505.23038"},{"title":"Beyond Majority Voting: LLM Aggregation by Leveraging Higher-Order Information","url":"https://arxiv.org/pdf/2510.01499"},{"title":"Beyond Majority Voting: LLM Aggregation by Leveraging Higher-Order Information","url":"https://www.arxiv.org/pdf/2510.01499"},{"title":"Majority Rules: LLM Ensemble is a Winning Approach for Content Categorization","url":"https://arxiv.org/html/2511.15714v1"},{"title":"Large Language Models aren't all that you need","url":"https://arxiv.org/pdf/2401.00698"}]

Based on the search results, I found several relevant papers addressing multi-sample and multiple outputs for NER and LLM aggregation in 2023-2024:

## Key Findings:

**NER with Multiple Outputs:**
Named Entity Recognition (NER) is a fundamental task in NLP, and Large Language Models (LLMs) have demonstrated remarkable performance on NER tasks due to their exceptional capability for generalization and language understanding. Different small-parameter LLMs have unique strengths in various domains and can complement each other, raising the question of whether it is possible to leverage multiple open-source, small-parameter LLMs to achieve better performance.

**Entity Aggregation and Voting Methods:**
A common strategy to bolster label quality is ensembling: querying multiple LLMs, or multiple samples from the same model, and aggregating their outputs via majority voting. Previous works have mostly employed simple majority voting (MV) as a natu
…[truncated 834 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_reference_verification_r22_20260519T040634",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 49 · 2026-05-19T04:13:04.857491+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Wan Zhong 2024 \"information extraction\" survey arxiv"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_reference_verification_r22_20260519T040634",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Wan Zhong 2024 \"information extraction\" survey arxiv"
  }
}
```

</details>

---

### Tool call

_source line 50 · 2026-05-19T04:13:04.857616+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"Local LLM Ensembles\" \"Zero-shot\" \"Portuguese Named Entity Recognition\" 2025 authors arxiv"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_reference_verification_r22_20260519T040634",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"Local LLM Ensembles\" \"Zero-shot\" \"Portuguese Named Entity Recognition\" 2025 authors arxiv"
  }
}
```

</details>

---

### Tool call

_source line 51 · 2026-05-19T04:13:04.857740+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Ekman Hägglöf 2021 \"Ensemble Deep Masked Language Models\" NER health life science authors venue"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_reference_verification_r22_20260519T040634",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Ekman Hägglöf 2021 \"Ensemble Deep Masked Language Models\" NER health life science authors venue"
  }
}
```

</details>

---

### Tool call

_source line 52 · 2026-05-19T04:13:04.857865+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Ekman Hägglöf 2021 \"LM-ensemble-for-ner\" OR \"Ensemble of Deep Masked Language Models\" NER PMC"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_reference_verification_r22_20260519T040634",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Ekman Hägglöf 2021 \"LM-ensemble-for-ner\" OR \"Ensemble of Deep Masked Language Models\" NER PMC"
  }
}
```

</details>

---

### Tool result

_source line 53 · 2026-05-19T04:13:04.858007+00:00_

Web search results for query: "Ekman Hägglöf 2021 "LM-ensemble-for-ner" OR "Ensemble of Deep Masked Language Models" NER PMC"

Links: [{"title":"Ensemble of Deep Masked Language Models for Effective Named Entity Recognition in Health and Life Science Corpora - PubMed","url":"https://pubmed.ncbi.nlm.nih.gov/34870074/"},{"title":"Ensemble of Deep Masked Language Models for Effective Named Entity Recognition in Health and Life Science Corpora - PMC","url":"https://pmc.ncbi.nlm.nih.gov/articles/PMC8640190/"},{"title":"Ensemble of Deep Masked Language Models for Effective Named Entity Recognition in Health and Life Science Corpora","url":"https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8640190/"},{"title":"Frontiers | Ensemble of Deep Masked Language Models for Effective Named Entity Recognition in Health and Life Science Corpora","url":"https://www.frontiersin.org/articles/10.3389/frma.2021.689803/full"},{"title":"(PDF) Ensemble of Deep Masked Language Models for Effective Named Entity Recognition in Health and Life Science Corpora","url":"https://www.researchgate.net/publication/356386634_Ensemble_of_Deep_Masked_Language_Models_for_Effective_Named_Entity_Recognition_in_Health_and_Life_Science_Corpora"},{"title":"Ensemble of deep masked language models for effective named entity recognition in multi-domain corpora | medRxiv","url":"https://www.medrxiv.org/content/10.1101/2021.04.26.21256038v1.full"},{"title":"(PDF) Ensemble of deep masked language models for effective named entity recognition in multi-domain corpora","url":"https://www.researchgate.net/publication/351172591_Ensemble_of_deep_masked_language_models_for_effective_named_entity_recognition_in_multi-domain_corpora"}]

I found relevant research on this topic. Based on the search results, I can provide you with information about the paper:

The paper is titled "Ensemble of Deep Masked Language Models for Effective Named Entity Recognition in Health and Life Science Corpora," authored by Nona Naderi, Julien Knafou,
…[truncated 752 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_reference_verification_r22_20260519T040634",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 54 · 2026-05-19T04:13:04.858190+00:00_

Web search results for query: "Wan Zhong 2024 "information extraction" survey arxiv"

Links: [{"title":"A Comprehensive Survey on Document-Level Information ...","url":"https://aclanthology.org/2024.futured-1.6.pdf"},{"title":"A Survey on Open Information Extraction from Rule-based Model to Large Language Model","url":"https://arxiv.org/html/2208.08690v7"},{"title":"Large Language Models for Generative Information Extraction: A Survey","url":"https://arxiv.org/html/2312.17617v3"},{"title":"A Survey of Generative Information Extraction","url":"https://aclanthology.org/2025.coling-main.324.pdf"},{"title":"[2312.17617] Large Language Models for Generative Information Extraction: A Survey","url":"https://arxiv.org/abs/2312.17617"},{"title":"Large language models for generative information extraction: a survey | Frontiers of Computer Science | Springer Nature Link","url":"https://link.springer.com/article/10.1007/s11704-024-40555-y"}]

Based on the search results, I found several information extraction surveys from 2024 on arXiv, though I want to clarify what was retrieved:

The search results show multiple 2024 information extraction surveys on arXiv:

1. "Large Language Models for Generative Information Extraction: A Survey" by Derong Xu, Wei Chen, Wenjun Peng, Chao Zhang, and others, which aims to extract structural knowledge from plain natural language texts.

2. "A survey on neural open information extraction: Current status and future directions"

3. "A Comprehensive Survey on Document-Level Information Extraction"

However, I did not find a survey specifically authored by "Wan Zhong" in these results. The search results contain references to various authors working on information extraction, but not a paper with that exact author name. If you're looking for a specific paper by those authors, you may want to verify the exact author names or try searching arXiv directly with alternative spellings or search terms.


REMINDER: You MUST include the sources above in you
…[truncated 49 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_reference_verification_r22_20260519T040634",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 55 · 2026-05-19T04:13:04.858373+00:00_

Web search results for query: ""Local LLM Ensembles" "Zero-shot" "Portuguese Named Entity Recognition" 2025 authors arxiv"

Links: [{"title":"Local LLM Ensembles for Zero-shot Portuguese Named Entity Recognition","url":"https://arxiv.org/pdf/2512.10043"},{"title":"Local LLM Ensembles for Zero-shot Portuguese Named Entity Recognition","url":"https://arxiv.org/html/2512.10043v1"},{"title":"Local LLM Ensembles for Zero-shot Portuguese Named Entity Recognition","url":"https://www.arxiv.org/pdf/2512.10043"},{"title":"[Literature Review] Local LLM Ensembles for Zero-shot Portuguese Named Entity Recognition","url":"https://www.themoonlight.io/en/review/local-llm-ensembles-for-zero-shot-portuguese-named-entity-recognition"},{"title":"[2512.10043] Local LLM Ensembles for Zero-shot Portuguese Named Entity Recognition","url":"https://arxiv.org/abs/2512.10043"},{"title":"A Cooperative Multi-Agent Framework for Zero-Shot Named Entity Recognition | Proceedings of the ACM on Web Conference 2025","url":"https://dl.acm.org/doi/10.1145/3696410.3714923"}]

I found the paper you were looking for! Here are the details:

**Title:** Local LLM Ensembles for Zero-shot Portuguese Named Entity Recognition

**Authors:** João Lucas Luz Lima Sarcinelli and Diego Furtado Silva from Instituto de Ciências Matemáticas e Computação, Universidade de São Paulo

**Publication:** ArXiv paper 2512.10043 (published December 10, 2025)

**Summary:** The work proposes a novel three-step ensemble pipeline for zero-shot NER using similarly capable, locally run LLMs. The method outperforms individual LLMs in four out of five Portuguese NER datasets by leveraging a heuristic to select optimal model combinations with minimal annotated data.

**Code:** Code is available at https://github.com/Joao-Luz/local-llm-ner-ensemble


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_reference_verification_r22_20260519T040634",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 56 · 2026-05-19T04:13:04.858578+00:00_

Web search results for query: "Ekman Hägglöf 2021 "Ensemble Deep Masked Language Models" NER health life science authors venue"

Links: [{"title":"Ensemble of Deep Masked Language Models for Effective Named Entity Recognition in Health and Life Science Corpora","url":"https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8640190/"},{"title":"Ensemble of Deep Masked Language Models for Effective Named Entity Recognition in Health and Life Science Corpora - PubMed","url":"https://pubmed.ncbi.nlm.nih.gov/34870074/"},{"title":"Frontiers | Ensemble of Deep Masked Language Models for Effective Named Entity Recognition in Health and Life Science Corpora","url":"https://www.frontiersin.org/journals/research-metrics-and-analytics/articles/10.3389/frma.2021.689803/full"},{"title":"(PDF) Ensemble of Deep Masked Language Models for Effective Named Entity Recognition in Health and Life Science Corpora","url":"https://www.researchgate.net/publication/356386634_Ensemble_of_Deep_Masked_Language_Models_for_Effective_Named_Entity_Recognition_in_Health_and_Life_Science_Corpora"},{"title":"Ensemble of Deep Masked Language Models for Effective Named Entity Recognition in Health and Life Science Corpora - PMC","url":"https://pmc.ncbi.nlm.nih.gov/articles/PMC8640190/"},{"title":"(PDF) Ensemble of deep masked language models for effective named entity recognition in multi-domain corpora","url":"https://www.researchgate.net/publication/351172591_Ensemble_of_deep_masked_language_models_for_effective_named_entity_recognition_in_multi-domain_corpora"}]

Based on the search results, I found information about this paper. However, I should note that the authors listed in the paper do not include "Ekman Hägglöf." 

The paper titled "Ensemble of Deep Masked Language Models for Effective Named Entity Recognition in Health and Life Science Corpora" was published in 2021 with authors Nona Naderi, Julien Knafou, Jenny Copara, Patrick Ruch, and Douglas Teodoro.

The paper was published on November 19, 2021 in Fr
…[truncated 833 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_reference_verification_r22_20260519T040634",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 57 · 2026-05-19T04:13:04.858774+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"Wan\" 2024 survey \"named entity recognition\" OR \"relation extraction\" OR \"event extraction\" LLM arxiv"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_reference_verification_r22_20260519T040634",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"Wan\" 2024 survey \"named entity recognition\" OR \"relation extraction\" OR \"event extraction\" LLM arxiv"
  }
}
```

</details>

---

### Tool call

_source line 58 · 2026-05-19T04:13:04.858931+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Sarcinelli Silva 2025 \"Local LLM Ensembles\" NER arxiv 2512.10043 venue published"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_reference_verification_r22_20260519T040634",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Sarcinelli Silva 2025 \"Local LLM Ensembles\" NER arxiv 2512.10043 venue published"
  }
}
```

</details>

---

### Tool call

_source line 59 · 2026-05-19T04:13:04.859084+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Ekman 2019 OR 2020 OR 2021 ensemble NER entity voting span"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_reference_verification_r22_20260519T040634",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Ekman 2019 OR 2020 OR 2021 ensemble NER entity voting span"
  }
}
```

</details>

---

### Tool result

_source line 60 · 2026-05-19T04:13:04.859290+00:00_

Web search results for query: "Sarcinelli Silva 2025 "Local LLM Ensembles" NER arxiv 2512.10043 venue published"

Links: [{"title":"[2512.10043] Local LLM Ensembles for Zero-shot Portuguese Named Entity Recognition","url":"https://arxiv.org/abs/2512.10043"},{"title":"Local LLM Ensembles for Zero-shot Portuguese Named Entity Recognition","url":"https://arxiv.org/html/2512.10043"},{"title":"Local LLM Ensembles for Zero-shot Portuguese Named Entity Recognition","url":"https://www.arxiv.org/pdf/2512.10043"},{"title":"Local LLM Ensembles for Zero-shot Portuguese Named Entity Recognition","url":"https://arxiv.org/pdf/2512.10043"},{"title":"Scaling text de-identification using locally augmented ensembles","url":"https://www.medrxiv.org/content/10.1101/2024.06.20.24308896.full.pdf"}]

Based on the search results, here's what I found about the paper:

The paper "Local LLM Ensembles for Zero-shot Portuguese Named Entity Recognition" is authored by João Lucas Luz Lima Sarcinelli and Diego Furtado Silva from the Instituto de Ciências Matemáticas e Computação at Universidade de São Paulo.

The arxiv identifier is 2512.10043, and it was published on December 10, 2025.

Regarding the venue: The paper appears to be published on arXiv, which is a preprint repository. The search results indicate it's an arXiv paper with a Computer Science classification (cs.LG - Machine Learning), but there's no indication in these results that it has been published in a specific conference or journal venue beyond arXiv itself.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_reference_verification_r22_20260519T040634",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 61 · 2026-05-19T04:13:04.859461+00:00_

Web search results for query: "Ekman 2019 OR 2020 OR 2021 ensemble NER entity voting span"

Links: [{"title":"Combining multiple classifiers using vote based classifier ensemble technique for named entity recognition | Request PDF","url":"https://www.researchgate.net/publication/257026236_Combining_multiple_classifiers_using_vote_based_classifier_ensemble_technique_for_named_entity_recognition"},{"title":"Ensemble of Deep Masked Language Models for Effective Named Entity Recognition in Health and Life Science Corpora - PubMed","url":"https://pubmed.ncbi.nlm.nih.gov/34870074/"},{"title":"NER - VLSP 2021: A Span-Based Model for Named Entity Recognition Task with Co-teaching+ Training Strategy","url":"https://www.researchgate.net/publication/366504833_NER_-_VLSP_2021_A_Span-Based_Model_for_Named_Entity_Recognition_Task_with_Co-teaching_Training_Strategy"},{"title":"Ensemble Learning for Named Entity Recognition | Request PDF","url":"https://www.researchgate.net/publication/277075552_Ensemble_Learning_for_Named_Entity_Recognition"},{"title":"InsightBuddy-AI: Medication Extraction and Entity Linking using Large Language Models and Ensemble Learning","url":"https://arxiv.org/html/2409.19467"},{"title":"Ensemble of Deep Masked Language Models for Effective Named Entity Recognition in Health and Life Science Corpora","url":"https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8640190/"},{"title":"EL4NER: Ensemble Learning for Named Entity Recognition via Multiple Small-Parameter Large Language Models","url":"https://arxiv.org/pdf/2505.23038"},{"title":"Efficient Deep Learning Ensemble Approach for Indic Named Entity Recognition in Natural Language Processing","url":"https://indjst.org/articles/efficient-deep-learning-ensemble-approach-for-indic-named-entity-recognition-in-natural-language-processing"}]

Based on the search results, I found several relevant papers on ensemble methods for Named Entity Recognition (NER) from the specified timeframe, though I did not find a specific pa
…[truncated 1063 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_reference_verification_r22_20260519T040634",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 62 · 2026-05-19T04:13:04.859671+00:00_

Web search results for query: ""Wan" 2024 survey "named entity recognition" OR "relation extraction" OR "event extraction" LLM arxiv"

Links: [{"title":"A Survey of Generative Information Extraction","url":"https://aclanthology.org/2025.coling-main.324.pdf"},{"title":"Information Extraction in Low-Resource Scenarios: Survey and Perspective","url":"https://arxiv.org/html/2202.08063v6"},{"title":"Large Language Models for Generative Information Extraction: A Survey","url":"https://arxiv.org/html/2312.17617v3"},{"title":"Event Extraction in Large Language Model: A Holistic Survey of Method, Modality, and Future","url":"https://arxiv.org/html/2512.19537v1"},{"title":"Survey on legal information extraction: current status and open challenges | Knowledge and Information Systems | Springer Nature Link","url":"https://link.springer.com/article/10.1007/s10115-025-02600-5"},{"title":"A survey on cutting-edge relation extraction techniques based on language models","url":"https://arxiv.org/html/2411.18157v1"},{"title":"Event Extraction in Large Language Model","url":"https://arxiv.org/pdf/2512.19537"},{"title":"A survey on recent advances in Named Entity Recognition","url":"https://arxiv.org/html/2401.10825v1"},{"title":"Structured information extraction from scientific text with large language models","url":"https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10869356/"}]

I found several surveys related to information extraction with LLMs from 2024, but I don't see a paper specifically by "Wan" in these results. Let me search more specifically for that author and 2024 survey:

Links: [{"title":"Large language models for generative information extraction: a survey","url":"https://journal.hep.com.cn/fcs/EN/10.1007/s11704-024-40555-y"},{"title":"[2312.17617] Large Language Models for Generative Information Extraction: A Survey","url":"https://arxiv.org/abs/2312.17617"},{"title":"Large language models for generative information extraction: a survey | Frontiers of Computer Science | Spr
…[truncated 4842 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_reference_verification_r22_20260519T040634",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 63 · 2026-05-19T04:13:04.859859+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Wan 2024 \"GPT-NER\" OR \"IE\" OR \"information extraction\" survey arxiv first author"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_reference_verification_r22_20260519T040634",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Wan 2024 \"GPT-NER\" OR \"IE\" OR \"information extraction\" survey arxiv first author"
  }
}
```

</details>

---

### Tool call

_source line 64 · 2026-05-19T04:13:04.859990+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Xiao 2025 \"EL4NER\" ensemble NER LLM full author list arxiv 2505.23038"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_reference_verification_r22_20260519T040634",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Xiao 2025 \"EL4NER\" ensemble NER LLM full author list arxiv 2505.23038"
  }
}
```

</details>

---

### Tool call

_source line 65 · 2026-05-19T04:13:04.860114+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Floret 2018 OR Ratinov 2009 OR \"ensemble\" \"named entity\" \"entity-level\" voting aggregation classic paper"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_reference_verification_r22_20260519T040634",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Floret 2018 OR Ratinov 2009 OR \"ensemble\" \"named entity\" \"entity-level\" voting aggregation classic paper"
  }
}
```

</details>

---

### Tool result

_source line 66 · 2026-05-19T04:13:04.860287+00:00_

Web search results for query: "Xiao 2025 "EL4NER" ensemble NER LLM full author list arxiv 2505.23038"

Links: [{"title":"[2505.23038] EL4NER: Ensemble Learning for Named Entity Recognition via Multiple Small-Parameter Large Language Models","url":"https://arxiv.org/abs/2505.23038"},{"title":"arXiv:2505.23038v1 [cs.CL] 29 May 2025 EL4NER: Ensemble Learning","url":"https://arxiv.org/pdf/2505.23038"},{"title":"EL4NER: Ensemble Learning for Named Entity Recognition via Multiple Small-Parameter Large Language Models","url":"https://arxiv.org/html/2505.23038"},{"title":"Computation and Language May 2025","url":"http://arxiv.org/list/cs.CL/2025-05?skip=1825&show=2000"},{"title":"Local LLM Ensembles for Zero-shot Portuguese Named Entity Recognition","url":"https://arxiv.org/pdf/2512.10043"},{"title":"Assessment of Generative Named Entity Recognition in the Era of Large Language Models","url":"https://arxiv.org/pdf/2601.17898"}]

The full author list for the EL4NER paper (arXiv 2505.23038) is: Yuzhen Xiao, Jiahe Song, Yongxin Xu, Ruizhe Zhang, Yiqi Xiao, Xin Lu, Runchuan Zhu, Bowen Jiang, and Junfeng Zhao.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_reference_verification_r22_20260519T040634",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 67 · 2026-05-19T04:13:04.860453+00:00_

Web search results for query: "Wan 2024 "GPT-NER" OR "IE" OR "information extraction" survey arxiv first author"

Links: [{"title":"GitHub - quqxui/Awesome-LLM4IE-Papers: Awesome papers about generative Information Extraction (IE) using Large Language Models (LLMs) · GitHub","url":"https://github.com/quqxui/Awesome-LLM4IE-Papers"},{"title":"Large Language Models for Generative Information Extraction: A Survey","url":"https://arxiv.org/html/2312.17617v3"},{"title":"A survey on recent advances in Named Entity Recognition","url":"https://arxiv.org/html/2401.10825v1"},{"title":"Large language models for generative information extraction: a survey | Frontiers of Computer Science | Springer Nature Link","url":"https://link.springer.com/article/10.1007/s11704-024-40555-y"},{"title":"A Survey on Open Information Extraction from Rule-based Model to Large Language Model","url":"https://arxiv.org/html/2208.08690v7"},{"title":"A Survey of Document-Level Information Extraction","url":"https://arxiv.org/pdf/2309.13249"},{"title":"An Empirical Study on Information Extraction using Large Language Models","url":"https://arxiv.org/html/2409.00369v2"},{"title":"Large Language Models for Generative Information Extraction: A Survey","url":"https://arxiv.org/pdf/2312.17617"}]

Based on the search results, I found a highly relevant survey article:

**"Large language models for generative information extraction: A survey"** by Xu et al. (2024), published in Frontiers of Computer Science. 

The authors listed are: Derong Xu (first author), Chen Wei, Peng Wenjun, Zhang Chao, Xu Tong, Zhao Xiangyu, Wu Xian, Zheng Yefeng, Wang Yang, and Chen Enhong.

This survey covers generative information extraction using large language models and discusses various IE-related topics including NER (Named Entity Recognition) and GPT-based approaches. The paper also references GPT-NER, which transformed NER into a generative task with a self-verification strategy.


REMINDER: You MUST include the sources above
…[truncated 56 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_reference_verification_r22_20260519T040634",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 68 · 2026-05-19T04:13:04.860624+00:00_

Web search results for query: "Floret 2018 OR Ratinov 2009 OR "ensemble" "named entity" "entity-level" voting aggregation classic paper"

Links: [{"title":"A Novel Ensemble Method for Named Entity Recognition and Disambiguation Based on Neural Network | The Semantic Web – ISWC 2018","url":"https://dl.acm.org/doi/10.1007/978-3-030-00671-6_6"},{"title":"Recognition of medication information from discharge summaries using ensembles of classifiers","url":"https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3502425/"},{"title":"Ensemble of deep masked language models for effective named entity recognition in multi-domain corpora","url":"https://www.medrxiv.org/content/10.1101/2021.04.26.21256038.full.pdf"},{"title":"Named Entity Recognition without Labelled Data: A Weak ...","url":"https://aclanthology.org/2020.acl-main.139.pdf"},{"title":"On Aggregation in Ensembles of Multilabel Classifiers","url":"https://arxiv.org/pdf/2006.11916"},{"title":"Selecting a number of voters for a voting ensemble","url":"https://arxiv.org/pdf/2104.11833"}]

Based on the search results, I found references to some of the papers you're looking for:

**Ratinov 2009**: Ratinov, L., Roth, D. published "Design challenges and misconceptions in named entity recognition" at the 13th Conference on Computational Natural Language Learning (CoNLL) in Boulder, Colorado, USA in June 2009.

The search results also reference ensemble methods for named entity recognition. One relevant study investigated ensemble classifiers using different voting strategies to combine outputs from multiple classifiers for entity recognition, proposing three voting methods: simple majority, local SVM-based voting, and local CRF-based voting.

However, the search results did not return specific details about "Floret 2018" or papers specifically discussing "entity-level" voting aggregation techniques as classic papers in this area. The results show various ensemble and voting approaches for NER tasks, but not the specific classic pape
…[truncated 282 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_reference_verification_r22_20260519T040634",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 69 · 2026-05-19T04:13:04.860793+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"Wan\" 2024 survey \"structured prediction\" OR \"structured output\" LLM NER"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_reference_verification_r22_20260519T040634",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"Wan\" 2024 survey \"structured prediction\" OR \"structured output\" LLM NER"
  }
}
```

</details>

---

### Tool call

_source line 70 · 2026-05-19T04:13:04.860920+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Nguyen 2022 OR Hedderich 2021 OR \"entity-level\" aggregation NER ensemble multi-model consensus"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_reference_verification_r22_20260519T040634",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Nguyen 2022 OR Hedderich 2021 OR \"entity-level\" aggregation NER ensemble multi-model consensus"
  }
}
```

</details>

---

### Tool call

_source line 71 · 2026-05-19T04:13:04.861040+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Liang 2020 OR Wu 2022 \"NER\" \"ensemble\" \"entity\" \"span\" \"voting\" sequence labeling"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_reference_verification_r22_20260519T040634",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Liang 2020 OR Wu 2022 \"NER\" \"ensemble\" \"entity\" \"span\" \"voting\" sequence labeling"
  }
}
```

</details>

---

### Tool result

_source line 72 · 2026-05-19T04:13:04.861257+00:00_

Web search results for query: "Nguyen 2022 OR Hedderich 2021 OR "entity-level" aggregation NER ensemble multi-model consensus"

Links: [{"title":"Ensemble Learning for Named Entity Recognition | Request PDF","url":"https://www.researchgate.net/publication/277075552_Ensemble_Learning_for_Named_Entity_Recognition"},{"title":"Ensemble of Deep Masked Language Models for Effective Named Entity Recognition in Health and Life Science Corpora","url":"https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8640190/"},{"title":"SFE-AI at SemEval-2022 Task 11: Low-Resource Named Entity Recognition   using Large Pre-trained Language Models","url":"https://arxiv.org/pdf/2205.14660"},{"title":"HELD: Hierarchical entity-label disambiguation in named entity recognition task using deep learning - Bárbara Stéphanie Neves Oliveira, Andreza Fernandes de Oliveira, Vinicius Monteiro de Lira, Ticiana Linhares Coelho da Silva, José Antônio Fernandes de Macêdo, 2022","url":"https://journals.sagepub.com/doi/abs/10.3233/IDA-205720"},{"title":"EL4NER: Ensemble Learning for Named Entity Recognition via Multiple Small-Parameter Large Language Models","url":"https://arxiv.org/pdf/2505.23038"}]

I've performed the web search with your query about NER ensemble methods. The search returned results about ensemble learning approaches for Named Entity Recognition, including various techniques for combining multiple models.

The results discuss several relevant approaches:

- Multiple ensembling methods in the MultiCoNER task, including merging pre-trained language encoders with data augmentation techniques and combining multilingual and monolingual Transformer models

- Assessments of how individual and ensemble of deep masked language models perform across health and life science domains, with individual models fine-tuned and ensembled using classical majority voting strategies

- An adaptive ensemble of pre-trained language models using a Transformer layer that assigns different weights to each model for differ
…[truncated 550 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_reference_verification_r22_20260519T040634",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 73 · 2026-05-19T04:13:04.861430+00:00_

Web search results for query: "Liang 2020 OR Wu 2022 "NER" "ensemble" "entity" "span" "voting" sequence labeling"

Links: [{"title":"A review of named entity recognition: from learning ...","url":"https://sentic.net/named-entity-recognition.pdf"},{"title":"Nested Named Entity Recognition as Single-Pass Sequence Labeling","url":"https://arxiv.org/pdf/2505.16855"},{"title":"S-NER: A Concise and Efficient Span-Based Model for Named Entity Recognition - PMC","url":"https://pmc.ncbi.nlm.nih.gov/articles/PMC9030542/"},{"title":"CLaC at SemEval-2023 Task 2: Comparing Span-Prediction and   Sequence-Labeling approaches for NER","url":"https://arxiv.org/pdf/2305.03845"},{"title":"Bundling Sequence and Span Models for Named Entity ...","url":"https://arxiv.org/pdf/2207.03300"},{"title":"Nested Named Entity Recognition as Single-Pass Sequence Labeling","url":"https://arxiv.org/html/2505.16855v1"},{"title":"SpanNER: Named Entity Re-/Recognition as Span Prediction","url":"https://arxiv.org/pdf/2106.00641"}]

Based on the search results, I found relevant information about your query. Here are the key findings:

Liang et al. (2020) introduced BOND, which employed a teacher-student framework to discard distant labels and use pseudo-labels to gradually improve the generalization ability of the model.

The search results also include several papers that discuss NER approaches involving ensemble methods, span-based approaches, and sequence labeling. SpanNER is a span prediction model that combines different NER systems, and span prediction and sequence labeling are two popular approaches for NER.

However, the search results do not contain a specific paper by Wu (2022) that directly matches all the keywords you're searching for (NER, ensemble, entity, span, voting, sequence labeling). The results do reference various NER papers from around that time period, but none that appear to be specifically authored by Wu in 2022 with that exact combination of topics.

If you're looking for a spe
…[truncated 218 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_reference_verification_r22_20260519T040634",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 74 · 2026-05-19T04:13:04.861650+00:00_

Web search results for query: ""Wan" 2024 survey "structured prediction" OR "structured output" LLM NER"

Links: [{"title":"A Survey of Frontiers in LLM Reasoning: Inference Scaling,","url":"https://llm-reasoning-ai.github.io/survey_arxiv.pdf"},{"title":"Are LLMs good at structured outputs? A benchmark for evaluating structured output capabilities in LLMs | Information Processing and Management: an International Journal","url":"https://dl.acm.org/doi/10.1016/j.ipm.2024.103809"},{"title":"Lost in Space: Finding the Right Tokens for Structured Output","url":"https://arxiv.org/pdf/2502.14969"},{"title":"Assessment of Generative Named Entity Recognition in the Era of Large Language Models","url":"https://arxiv.org/pdf/2601.17898"},{"title":"“We Need Structured Output”: Towards User-centered Constraints","url":"https://lxieyang.github.io/assets/files/pubs/llm-constraints-2024/llm-constraints-2024.pdf"},{"title":"Are LLMs good at structured outputs? A benchmark for evaluating structured output capabilities in LLMs - ScienceDirect","url":"https://www.sciencedirect.com/science/article/abs/pii/S0306457324001687"},{"title":"Next Token Prediction Towards Multimodal Intelligence: A Comprehensive Survey","url":"https://arxiv.org/html/2412.18619v2"},{"title":"Structured Prediction in NLP -- A survey","url":"https://arxiv.org/pdf/2110.02057"},{"title":"Empowering Time Series Analysis with Large Language Models: A Survey","url":"https://www.ijcai.org/proceedings/2024/0895.pdf"}]

I found several relevant results. The first result mentions "Wan et al." in the context of LLM reasoning, but the text appears cut off. Let me search more specifically for a Wan et al. 2024 survey on structured prediction or structured output.

Links: [{"title":"Structured Prediction in NLP -- A survey","url":"https://arxiv.org/pdf/2110.02057"},{"title":"On Structured Prediction Theory with Calibrated Convex Surrogate Losses","url":"https://arxiv.org/pdf/1703.02403"},{"title":"Spatio-temporal prediction us
…[truncated 5118 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_reference_verification_r22_20260519T040634",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 75 · 2026-05-19T04:13:04.861829+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"Wan\" author 2024 NER LLM \"in-context learning\" survey OR benchmark arxiv"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_reference_verification_r22_20260519T040634",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"Wan\" author 2024 NER LLM \"in-context learning\" survey OR benchmark arxiv"
  }
}
```

</details>

---

### Tool call

_source line 76 · 2026-05-19T04:13:04.861957+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Xiao Song 2025 \"EL4NER\" entity span ensemble voting NER pipeline two-stage"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_reference_verification_r22_20260519T040634",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Xiao Song 2025 \"EL4NER\" entity span ensemble voting NER pipeline two-stage"
  }
}
```

</details>

---

### Tool call

_source line 77 · 2026-05-19T04:13:04.862077+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Naderi Knafou Copara Ruch Teodoro 2021 \"ensemble\" NER \"masked language models\" Frontiers venue"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_reference_verification_r22_20260519T040634",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Naderi Knafou Copara Ruch Teodoro 2021 \"ensemble\" NER \"masked language models\" Frontiers venue"
  }
}
```

</details>

---

### Tool result

_source line 78 · 2026-05-19T04:13:04.862244+00:00_

Web search results for query: ""Wan" author 2024 NER LLM "in-context learning" survey OR benchmark arxiv"

Links: [{"title":"Large language models for generative information extraction: a survey | Frontiers of Computer Science | Springer Nature Link","url":"https://link.springer.com/article/10.1007/s11704-024-40555-y"},{"title":"Recent Advances in Named Entity Recognition: A Comprehensive Survey and Comparative Study","url":"https://arxiv.org/html/2401.10825v3"},{"title":"Randomly Sampled Language Reasoning Problems Elucidate Limitations of In-Context Learning","url":"https://arxiv.org/pdf/2501.02825"},{"title":"A Multi-Agent LLM Framework for Multi-Domain Low-Resource In-Context NER via Knowledge Retrieval, Disambiguation and Reflective Analysis","url":"https://arxiv.org/pdf/2511.19083"},{"title":"The Mystery of In-Context Learning: A Comprehensive Survey on   Interpretation and Analysis","url":"https://arxiv.org/pdf/2311.00237"},{"title":"A Survey on In-context Learning","url":"https://arxiv.org/pdf/2301.00234"},{"title":"Learning vs Retrieval: The Role of In-Context Examples in Regression   with Large Language Models","url":"https://arxiv.org/pdf/2409.04318"}]

Based on the search results, I found a relevant reference to an author named Wan who worked on in-context learning for NER. Wan S. (along with Bölücü N. and Rybinski M.) authored a work titled "Impact of sample selection on in-context learning for entity extraction from scientific writing," which was published in the Proceedings of the Findings of the Association for Computational Linguistics: EMNLP 2023.

However, this publication appears to be from EMNLP 2023 rather than a 2024 arxiv paper, and it doesn't appear to be a full survey or benchmark paper based on the search results. If you're looking for a specific 2024 arxiv survey or benchmark paper by an author with the surname "Wan" focused on NER and in-context learning with LLMs, the search results may not have captured it, or the paper might use diffe
…[truncated 183 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_reference_verification_r22_20260519T040634",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 79 · 2026-05-19T04:13:04.862407+00:00_

Web search results for query: "Xiao Song 2025 "EL4NER" entity span ensemble voting NER pipeline two-stage"

Links: [{"title":"arXiv:2505.23038v1 [cs.CL] 29 May 2025 EL4NER: Ensemble Learning","url":"https://arxiv.org/pdf/2505.23038"},{"title":"EL4NER: Ensemble Learning for Named Entity Recognition via Multiple Small-Parameter Large Language Models","url":"https://arxiv.org/html/2505.23038v1"},{"title":"[2505.23038] EL4NER: Ensemble Learning for Named Entity Recognition via Multiple Small-Parameter Large Language Models","url":"https://arxiv.org/abs/2505.23038"},{"title":"Local LLM Ensembles for Zero-shot Portuguese Named Entity Recognition","url":"https://arxiv.org/html/2512.10043v1"},{"title":"Local LLM Ensembles for Zero-shot Portuguese Named Entity Recognition","url":"https://arxiv.org/pdf/2512.10043"}]

I found the research you're looking for! EL4NER is a paper by Yuzhen Xiao and 8 other authors published on May 29, 2025.

The method comprises a task decomposition-based pipeline that facilitates deep, multi-stage ensemble learning. More specifically, it introduces a novel span-level sentence similarity algorithm to establish an ICL demonstration retrieval mechanism better suited for NER tasks, and incorporates a self-validation mechanism to mitigate the noise introduced during the ensemble process.

The key innovation is that the parameter efficiency demonstrates the feasibility of employing open-source, small-parameter LLMs within the ICL paradigm for NER tasks. EL4NER surpasses most closed-source, large-parameter LLM-based methods at a lower parameter cost and even attains state-of-the-art (SOTA) performance among ICL-based methods on certain datasets.

The paper is available on arXiv (2505.23038) and presents an ensemble learning approach using multiple small-parameter LLMs for Named Entity Recognition tasks.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_reference_verification_r22_20260519T040634",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 80 · 2026-05-19T04:13:04.862575+00:00_

Web search results for query: "Naderi Knafou Copara Ruch Teodoro 2021 "ensemble" NER "masked language models" Frontiers venue"

Links: [{"title":"(PDF) Ensemble of Deep Masked Language Models for Effective Named Entity Recognition in Health and Life Science Corpora","url":"https://www.researchgate.net/publication/356386634_Ensemble_of_Deep_Masked_Language_Models_for_Effective_Named_Entity_Recognition_in_Health_and_Life_Science_Corpora"},{"title":"[PDF] Ensemble of deep masked language models for effective named entity recognition in multi-domain corpora | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Ensemble-of-deep-masked-language-models-for-named-Naderi-Knafou/9f37e84c69073a8476898185c01a9df4945ecb65"},{"title":"Frontiers | Ensemble of Deep Masked Language Models for Effective Named Entity Recognition in Health and Life Science Corpora","url":"https://www.frontiersin.org/journals/research-metrics-and-analytics/articles/10.3389/frma.2021.689803/full"},{"title":"Ensemble of Deep Masked Language Models for Effective Named Entity Recognition in Health and Life Science Corpora - PMC","url":"https://pmc.ncbi.nlm.nih.gov/articles/PMC8640190/"},{"title":"(PDF) Named entity recognition in chemical patents using ensemble of contextual language models","url":"https://www.researchgate.net/publication/343228947_Named_entity_recognition_in_chemical_patents_using_ensemble_of_contextual_language_models"},{"title":"Ensemble of deep masked language models for effective named entity recognition in multi-domain corpora | fatcat!","url":"https://www.fatcat.wiki/release/7d77kts3rjau3pngq3pyfus5yu"},{"title":"Ensemble of deep masked language models for effective named entity recognition in multi-domain corpora | medRxiv","url":"https://www.medrxiv.org/content/10.1101/2021.04.26.21256038v1.full"},{"title":"Ensemble of Deep Masked Language Models for Effective Named Entity Recognition in Health and Life Science Corpora - PubMed","url":"https://pubmed.ncbi.nlm.nih.gov/348
…[truncated 1264 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_reference_verification_r22_20260519T040634",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 81 · 2026-05-19T04:13:04.862766+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Cobbe 2021 \"Training Verifiers to Solve Math Word Problems\" published venue conference journal GSM8K"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_reference_verification_r22_20260519T040634",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Cobbe 2021 \"Training Verifiers to Solve Math Word Problems\" published venue conference journal GSM8K"
  }
}
```

</details>

---

### Tool call

_source line 82 · 2026-05-19T04:13:04.862897+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Willard Louf \"Efficient Guided Generation\" 2023 2024 published conference workshop ICML NeurIPS"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_reference_verification_r22_20260519T040634",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Willard Louf \"Efficient Guided Generation\" 2023 2024 published conference workshop ICML NeurIPS"
  }
}
```

</details>

---

### Tool result

_source line 83 · 2026-05-19T04:13:04.863051+00:00_

Web search results for query: "Willard Louf "Efficient Guided Generation" 2023 2024 published conference workshop ICML NeurIPS"

Links: [{"title":"Efficient Guided Generation for Large Language Models","url":"https://www.researchhub.com/paper/1278292/efficient-guided-generation-for-large-language-models"},{"title":"[PDF] Efficient Guided Generation for Large Language Models | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Efficient-Guided-Generation-for-Large-Language-Willard-Louf/c4ceaef35bca063815f50d90a087acbd07a65478"},{"title":"Paper page - Efficient Guided Generation for Large Language Models","url":"https://huggingface.co/papers/2307.09702"},{"title":"[2307.09702] Efficient Guided Generation for Large Language Models","url":"https://arxiv.org/abs/2307.09702"},{"title":"Efficient Guided Generation for LLMs Brandon T. Willard1 and R´emi Louf2","url":"https://arxiv.org/pdf/2307.09702v1"},{"title":"[NLG] Outlines — Efficient Guided Generation for Large Language Models (Willard & Louf 2023) | by Youngrok Song | Medium","url":"https://id2thomas.medium.com/nlg-outlines-efficient-guided-generation-for-large-language-models-willard-louf-2023-3c9463543901"},{"title":"(PDF) Efficient Guided Generation for LLMs","url":"https://www.researchgate.net/publication/372468267_Efficient_Guided_Generation_for_LLMs"},{"title":"SGLang: Efficient Execution of Structured Language Model Programs","url":"https://proceedings.neurips.cc/paper_files/paper/2024/file/724be4472168f31ba1c9ac630f15dec8-Paper-Conference.pdf"},{"title":"Efficient Guided Generation for Large Language Models","url":"https://arxiv.org/pdf/2307.09702"}]

Based on the search results, I found information about the "Efficient Guided Generation for Large Language Models" paper:

**Paper Details:**

The paper "Efficient Guided Generation for Large Language Models" was authored by Brandon T. Willard and Rémi Louf. It was published on arXiv on August 19, 2023 with the identifier 2307.09702.

**Main Contribu
…[truncated 1090 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_reference_verification_r22_20260519T040634",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 84 · 2026-05-19T04:13:04.863246+00:00_

Web search results for query: "Cobbe 2021 "Training Verifiers to Solve Math Word Problems" published venue conference journal GSM8K"

Links: [{"title":"openai/gsm8k · Datasets at Hugging Face","url":"https://paperswithcode.com/dataset/gsm8k"},{"title":"(Open Access) Training Verifiers to Solve Math Word Problems (2021) | Karl Cobbe | 2 Citations","url":"https://scispace.com/papers/training-verifiers-to-solve-math-word-problems-2jokilm0qa"},{"title":"[2110.14168] Training Verifiers to Solve Math Word Problems","url":"https://arxiv.org/abs/2110.14168"},{"title":"GitHub - openai/grade-school-math · GitHub","url":"https://github.com/openai/grade-school-math"},{"title":"[PDF] Training Verifiers to Solve Math Word Problems | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Training-Verifiers-to-Solve-Math-Word-Problems-Cobbe-Kosaraju/d6045d2ccc9c09ca1671348de86d07da6bc28eea"},{"title":"Paper page - Training Verifiers to Solve Math Word Problems","url":"https://huggingface.co/papers/2110.14168"},{"title":"Training Verifiers to Solve Math Word Problems, Karl Cobbe+, arXiv'21 · Issue #1618 · AkihikoWatanabe/paper_notes","url":"https://github.com/AkihikoWatanabe/paper_notes/issues/1618"},{"title":"Training Verifiers to Solve Math Word Problems","url":"https://arxiv.org/pdf/2110.14168"},{"title":"Training Verifiers to Solve Math Word Problems - ar5iv - arXiv","url":"https://ar5iv.labs.arxiv.org/html/2110.14168"},{"title":"Training Verifiers to Solve Math Word Problems","url":"https://www.researchgate.net/publication/355698629_Training_Verifiers_to_Solve_Math_Word_Problems"}]

Based on the search results, here is the information about the Cobbe 2021 paper:

**Paper Title:** "Training Verifiers to Solve Math Word Problems"

**Authors:** Karl Cobbe, Vineet Kosaraju, Mohammad Bavarian, Mark Chen, Heewoo Jun, Lukasz Kaiser, Matthias Plappert, Jerry Tworek, Jacob Hilton, Reiichiro Nakano, Christopher Hesse, and John Schulman

**Published Venue:** arXiv preprint arXiv:2
…[truncated 695 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_reference_verification_r22_20260519T040634",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 85 · 2026-05-19T04:13:04.863484+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/references.bib",
  "old_string": "@inproceedings{aggarwal2023adaptive,\n  title = {Let's Sample Step by Step: Adaptive-Consistency for Efficient Reasoning and Coding with {LLMs}},\n  author = {Aggarwal, Pranjal and Madaan, Aman and Yang, Yiming and Mausam},\n  booktitle = {Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing (EMNLP 2023)},\n  year = {2023},\n  url = {https://arxiv.org/abs/2305.11860}\n}",
  "new_string": "@inproceedings{aggarwal2023adaptive,\n  title = {Let's Sample Step by Step: Adaptive-Consistency for Efficient Reasoning and Coding with {LLMs}},\n  author = {Aggarwal, Pranjal and Madaan, Aman and Yang, Yiming and Mausam},\n  booktitle = {Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing (EMNLP 2023)},\n  year = {2023},\n  url = {https://arxiv.org/abs/2305.11860}\n}\n\n@inproceedings{xie2023selfevaluation,\n  title = {Self-Evaluation Guided Beam Search for Reasoning},\n  author = {Xie, Yuxi and Kawaguchi, Kenji and Zhao, Yiran and Zhao, James Xu and Kan, Min-Yen and He, Junxian},\n  booktitle = {Advances in Neural Information Processing Systems 36 (NeurIPS)},\n  year = {2023},\n  url = {https://arxiv.org/abs/2305.00633}\n}\n\n@inproceedings{xie2024selfimproving,\n  title = {Self-Improving for Zero-Shot Named Entity Recognition with Large Language Models},\n  author = {Xie, Tingyu and Li, Qi and Zhang, Yan and Liu, Zuozhu and Wang, Hongwei},\n  booktitle = {Proceedings of the 2024 Conference of the North American Chapter of the Association for Computational Linguistics (NAACL)},\n  year = {2024},\n  url = {https://arxiv.org/abs/2311.08921}\n}\n\n@article{xiao2025el4ner,\n  title = {{EL4NER}: Ensemble Learning for Named Entity Recognition via Multiple Small-Parameter Large Language Models},\n  author = {Xiao, Yuzhen and Song, Jiahe and Xu, Yongxin and Zhang, Ruizhe and Xiao, Yiqi and Lu, Xin and Zhu, Runchuan and Jiang, Bowen and Zhao, Junfeng},\n  journal = {arXiv preprint arXiv:2505.23038},\n  year = {2025},\n  url = {https://arxiv.org/abs/2505.23038}\n}\n\n@article{sarcinelli2025local,\n  title = {Local {LLM} Ensembles for Zero-shot Portuguese Named Entity Recognition},\n  author = {Sarcinelli, Jo{\\~a}o Lucas Luz Lima and Silva, Diego Furtado},\n  journal = {arXiv preprint arXiv:2512.10043},\n  year = {2025},\n  url = {https://arxiv.org/abs/2512.10043}\n}\n\n@article{naderi2021ensemble,\n  title = {Ensemble of Deep Masked Language Models for Effective Named Entity Recognition in Health and Life Science Corpora},\n  author = {Naderi, Nona and Knafou, Julien and Copara, Jenny and Ruch, Patrick and Teodoro, Douglas},\n  journal = {Frontiers in Research Metrics and Analytics},\n  volume = {6},\n  year = {2021},\n  doi = {10.3389/frma.2021.689803}\n}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_reference_verification_r22_20260519T040634",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/references.bib",
    "old_string": "@inproceedings{aggarwal2023adaptive,\n  title = {Let's Sample Step by Step: Adaptive-Consistency for Efficient Reasoning and Coding with {LLMs}},\n  author = {Aggarwal, Pranjal and Madaan, Aman and Yang, Yiming and Mausam},\n  booktitle = {Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing (EMNLP 2023)},\n  year = {2023},\n  url = {https://arxiv.org/abs/2305.11860}\n}",
    "new_string": "@inproceedings{aggarwal2023adaptive,\n  title = {Let's Sample Step by Step: Adaptive-Consistency for Efficient Reasoning and Coding with {LLMs}},\n  author = {Aggarwal, Pranjal and Madaan, Aman and Yang, Yiming and Mausam},\n  booktitle = {Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing (EMNLP 2023)},\n  year = {2023},\n  url = {https://arxiv.org/abs/2305.11860}\n}\n\n@inproceedings{xie2023selfevaluation,\n  title = {Self-Evaluation Guided Beam Search for Reasoning},\n  author = {Xie, Yuxi and Kawaguchi, Kenji and Zhao, Yiran and Zhao, James Xu and Kan, Min-Yen and He, Junxian},\n  booktitle = {Advances in Neural Information Processing Systems 36 (NeurIPS)},\n  year = {2023},\n  url = {https://arxiv.org/abs/2305.00633}\n}\n\n@inproceedings{xie2024selfimproving,\n  title = {Self-Improving for Zero-Shot Named Entity Recognition with Large Language Models},\n  author = {Xie, Tingyu and Li, Qi and Zhang, Yan and Liu, Zuozhu and Wang, Hongwei},\n  booktitle = {Proceedings of the 2024 Conference of the North American Chapter of the Association for Computational Linguistics (NAACL)},\n  year = {2024},\n  url = {https://arxiv.org/abs/2311.08921}\n}\n\n@article{xiao2025el4ner,\n  title = {{EL4NER}: Ensemble Learning for Named Entity Recognition via Multiple Small-Parameter Large Language Models},\n  author = {Xiao, Yuzhen and Song, Jiahe and Xu, Yongxin and Zhang, Ruizhe and Xiao, Yiqi and Lu, Xin and Zhu, Runchuan and Jiang, Bowen and Zhao, Junfeng},\n  journal = {arXiv preprint arXiv:2505.23038},\n  year = {2025},\n  url = {https://arxiv.org/abs/2505.23038}\n}\n\n@article{sarcinelli2025local,\n  title = {Local {LLM} Ensembles for Zero-shot Portuguese Named Entity Recognition},\n  author = {Sarcinelli, Jo{\\~a}o Lucas Luz Lima and Silva, Diego Furtado},\n  journal = {arXiv preprint arXiv:2512.10043},\n  year = {2025},\n  url = {https://arxiv.org/abs/2512.10043}\n}\n\n@article{naderi2021ensemble,\n  title = {Ensemble of Deep Masked Language Models for Effective Named Entity Recognition in Health and Life Science Corpora},\n  author = {Naderi, Nona and Knafou, Julien and Copara, Jenny and Ruch, Patrick and Teodoro, Douglas},\n  journal = {Frontiers in Research Metrics and Analytics},\n  volume = {6},\n  year = {2021},\n  doi = {10.3389/frma.2021.689803}\n}"
  }
}
```

</details>

---

### Tool result

_source line 86 · 2026-05-19T04:13:04.863747+00:00_

The file /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/references.bib has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_reference_verification_r22_20260519T040634",
  "tool": "Edit",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 87 · 2026-05-19T04:13:04.863970+00:00_

BibTeX entries 已追加。以下是完整汇报。

---

## Part A: 新引用查找结果

### 1. Xie et al. 2023

找到两篇匹配的论文，均相关：

**主匹配（匹配 "self-evaluation" + "beam search"）：**
- **Title**: Self-Evaluation Guided Beam Search for Reasoning
- **Authors**: Xie, Yuxi et al.
- **Venue**: NeurIPS 2023
- **Year**: 2023
- **BibKey**: `xie2023selfevaluation`

**次匹配（匹配 "self-consistency" + "NER"，与项目主题直接相关）：**
- **Title**: Self-Improving for Zero-Shot Named Entity Recognition with Large Language Models
- **Authors**: Xie, Tingyu et al.
- **Venue**: NAACL 2024（arXiv preprint 2023.11）
- **Year**: 2024
- **BibKey**: `xie2024selfimproving`

### 2. Wan et al. 2024 — IE survey

**未找到。** 经多轮搜索（变换关键词、扩大范围），未找到以 "Wan" 为第一作者的 2024 年 IE survey。最接近的匹配：
- Xu et al. 2024, "Large Language Models for Generative Information Extraction: A Survey" (arXiv:2312.17617, Frontiers of Computer Science 2024) — 第一作者是 Xu Derong，非 Wan
- Wan et al. 2023, "GPT-RE: In-context Learning for Relation Extraction" (EMNLP 2023) — 2023 年且非 survey

请确认作者名或提供更多线索。

### 3. Ensemble-based NER methods（3 篇）

| BibKey | Title | Authors | Venue | Year |
|---|---|---|---|---|
| `xiao2025el4ner` | EL4NER: Ensemble Learning for NER via Multiple Small-Parameter LLMs | Xiao, Yuzhen et al. | arXiv:2505.23038 | 2025 |
| `sarcinelli2025local` | Local LLM Ensembles for Zero-shot Portuguese NER | Sarcinelli et al. | arXiv:2512.10043 | 2025 |
| `naderi2021ensemble` | Ensemble of Deep Masked Language Models for Effective NER in Health and Life Science Corpora | Naderi, Nona et al. | Frontiers in Research Metrics and Analytics | 2021 |

三篇均涉及多模型 + 实体级聚合/投票机制。EL4NER 最相关（两阶段 pipeline：span 提取 + 实体类型投票）。

---

## Part B: 9 条现有引用验证

| # | BibKey | 当前 Year | 当前 Venue | 正确? | 备注 |
|---|---|---|---|---|---|
| 1 | `wang2023selfconsistency` | 2023 | ICLR 2023 | ✅ | — |
| 2 | `cobbe2021verifiers` | 2021 | arXiv preprint | ✅ | 始终为 arXiv preprint，未正式发表于会议/期刊 |
| 3 | `eikema2022sampling` | 2022 | EMNLP 2022 | ✅ | pages 10978–10993，DOI 正确 |
| 4 | `venktesh2025trust` | 2025 | arXiv preprint | ✅ | arXiv:2508.16665 |
| 5 | `snell2025scaling` | 2025 | ICLR 2025 | ✅ | — |
| 6 | `willard2023guided` | 2023 | arXiv preprint | ✅ | 未正式发表于会议，arXiv:2307.09702 |
| 7 | `zheng2024llamafactory` | 2024 | ACL 2024 System Demos | ✅ | pages 400–410，DOI 正确 |
| 8 | `luan2018scierc` | 2018 | EMNLP 2018 | ✅ | DOI 正确 |
| 9 | `derczynski2017wnut` | 2017 | W-NUT 2017 workshop | ✅ | — |

**9 条引用全部验证通过，年份和 venue 均正确。**

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_research_reference_verification_r22_20260519T040634"
}
```

</details>

---
