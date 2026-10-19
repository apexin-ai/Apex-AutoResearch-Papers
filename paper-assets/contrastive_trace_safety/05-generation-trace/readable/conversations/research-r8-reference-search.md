# research r8 reference search

**Layer Selection Sensitivity in Hidden-State Safety Probes for Reasoning Models** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 17
- **Recorded user turns:** 0
- **Tool calls:** 8
- **Original source:** `logs/chats/worker_research_r8_reference_search_20260518T070953.jsonl`
- **Structured JSON:** [`0eaed29804a5b3b27fea.json`](../../sessions/0e/0eaed29804a5b3b27fea.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

17 recorded events

### Tool call

_source line 1 · 2026-05-18T07:10:52.693867+00:00_

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
  "session": "worker_research_r8_reference_search_20260518T070953",
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

_source line 2 · 2026-05-18T07:10:52.694281+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_r8_reference_search_20260518T070953",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-18T07:10:52.694471+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Page 1954 \"Continuous inspection schemes\" Biometrika BibTeX"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_r8_reference_search_20260518T070953",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Page 1954 \"Continuous inspection schemes\" Biometrika BibTeX"
  }
}
```

</details>

---

### Tool call

_source line 4 · 2026-05-18T07:10:52.694642+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Reimers Gurevych 2019 \"Sentence-BERT\" EMNLP BibTeX"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_r8_reference_search_20260518T070953",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Reimers Gurevych 2019 \"Sentence-BERT\" EMNLP BibTeX"
  }
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-18T07:10:52.694987+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Xiao et al 2023 \"C-Pack\" BGE embedding BibTeX"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_r8_reference_search_20260518T070953",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Xiao et al 2023 \"C-Pack\" BGE embedding BibTeX"
  }
}
```

</details>

---

### Tool call

_source line 6 · 2026-05-18T07:10:52.695160+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Meng et al 2022 \"Locating and Editing Factual Associations in GPT\" NeurIPS BibTeX"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_r8_reference_search_20260518T070953",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Meng et al 2022 \"Locating and Editing Factual Associations in GPT\" NeurIPS BibTeX"
  }
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-18T07:10:52.695299+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Li et al \"Inference-Time Intervention\" ITI truthful language model BibTeX venue"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_r8_reference_search_20260518T070953",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Li et al \"Inference-Time Intervention\" ITI truthful language model BibTeX venue"
  }
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-18T07:10:52.695507+00:00_

Web search results for query: "Page 1954 "Continuous inspection schemes" Biometrika BibTeX"

Links: [{"title":"CONTINUOUS INSPECTION SCHEMES – ScienceOpen","url":"https://www.scienceopen.com/document?vid=224e2c81-6327-4838-b2e9-78a006610245"},{"title":"Page, E.S. (1954) Continuous Inspection Schemes. Biometrika, 41, 100-115. - References - Scientific Research Publishing","url":"https://www.scirp.org/reference/referencespapers?referenceid=1853242"},{"title":"CONTINUOUS INSPECTION SCHEMES | Biometrika | Oxford Academic","url":"https://academic.oup.com/biomet/article-abstract/41/1-2/100/456627"},{"title":"CONTINUOUS INSPECTION SCHEMES | Semantic Scholar","url":"https://www.semanticscholar.org/paper/CONTINUOUS-INSPECTION-SCHEMES-Page/ae3c60cf4066589d91256d52c6f568665f70568e"},{"title":"E. S. Page, “Continuous Inspection Schemes,” Biometrika, Vol. 41, No. 1-2, 1954, pp.100-114. doi10.1093/biomet/41.1-2.100 - References - Scientific Research Publishing","url":"https://www.scirp.org/(S(ny23rubfvg45z345vbrepxrl))/reference/referencespapers?referenceid=431059"},{"title":"Page, E. (1954) Continuous Inspection Schemes. Biometrika, 14, 100-115. - References - Scientific Research Publishing","url":"https://www.scirp.org/reference/referencespapers?referenceid=2246687"},{"title":"Vol. 41, No. 1/2, Jun., 1954 of Biometrika on JSTOR","url":"https://www.jstor.org/stable/i315422"},{"title":"CGR-CUSUM: a continuous time generalized rapid response cumulative sum chart | Biostatistics | Oxford Academic","url":"https://academic.oup.com/biostatistics/article/25/1/253/6705266"},{"title":"Ongetiteld","url":"https://hal.science/hal-00516996v1/html_references"},{"title":"PageHinkley — CapyMOA","url":"https://capymoa.org/api/modules/capymoa.drift.detectors.PageHinkley.html"}]

Based on the search results, I found the bibliographic information for the article "Continuous Inspection Schemes" published in 1954:

The article is by E. S. Page, titled "Continuous Inspection Schemes," published in Bio
…[truncated 482 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_r8_reference_search_20260518T070953",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 9 · 2026-05-18T07:10:52.695743+00:00_

Web search results for query: "Reimers Gurevych 2019 "Sentence-BERT" EMNLP BibTeX"

Links: [{"title":"Sentence-BERT: Sentence Embeddings using Siamese BERT-Networks - ACL Anthology","url":"https://aclanthology.org/D19-1410/"},{"title":"Sentence-BERT: Sentence Embeddings using Siamese BERT-Networks | BibSonomy","url":"https://www.bibsonomy.org/bibtex/292afb49328e6651f17dc1e1b8c304aae/nosebrain"},{"title":"Reimers, N. and Gurevych, I. (2019) Sentence-BERT Sentence Embeddings Using Siamese BERT-Networks. Proceedings of the 2019 Conference on Empirical Methods in Natural Language Processing and the 9th International Joint Conference on Natural Language Pro-cessing (EMNLP-IJCNLP), Hong Kong, November 2019, 3982-3992. - References - Scientific Research Publishing","url":"https://www.scirp.org/reference/referencespapers?referenceid=3422225"},{"title":"[1908.10084] Sentence-BERT: Sentence Embeddings using Siamese BERT-Networks","url":"https://arxiv.org/abs/1908.10084"},{"title":"[PDF] Sentence-BERT: Sentence Embeddings using Siamese BERT-Networks | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Sentence-BERT:-Sentence-Embeddings-using-Siamese-Reimers-Gurevych/93d63ec754f29fa22572615320afe0521f7ec66d"},{"title":"Sentence-BERT: Sentence Embeddings using Siamese BERT-Networks | Request PDF","url":"https://www.researchgate.net/publication/336996965_Sentence-BERT_Sentence_Embeddings_using_Siamese_BERT-Networks"},{"title":"Google Scholar","url":"https://scholar.google.com/scholar_lookup?title=Sentence-BERT:+Sentence+Embeddings+Using+Siamese+BERT-Networks&conference=Proceedings+of+the+2019+Conference+on+Empirical+Methods+in+Natural+Language+Processing+and+the+9th+International+Joint+Conference+on+Natural+Language+Processing+(EMNLP-IJCNLP)&author=Reimers,+N.&author=Gurevych,+I.&publication_year=2019&pages=3982%E2%80%933992&doi=10.18653/v1/D19-1410"},{"title":"Sentence-BERT: Sentence Embeddings using Siamese BERT-Networks","url":"https://arxiv.org/pdf/1908.10084"},{"
…[truncated 1141 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_r8_reference_search_20260518T070953",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-18T07:10:52.695951+00:00_

Web search results for query: "Xiao et al 2023 "C-Pack" BGE embedding BibTeX"

Links: [{"title":"C-Pack: Packed Resources For General Chinese Embeddings Shitao Xiao†","url":"https://arxiv.org/pdf/2309.07597"},{"title":"[2309.07597] C-Pack: Packed Resources For General Chinese Embeddings","url":"https://arxiv.org/abs/2309.07597"},{"title":"C-Pack: Packed Resources For General Chinese Embeddings | Request PDF","url":"https://www.researchgate.net/publication/382190819_C-Pack_Packed_Resources_For_General_Chinese_Embeddings"},{"title":"C-Pack: Packed Resources For General Chinese Embeddings","url":"https://arxiv.org/html/2309.07597v5"},{"title":"C-Pack: Packaged Resources To Advance General Chinese Embedding","url":"https://arxiv.org/html/2309.07597v2"},{"title":"BGE M3-Embedding: Multi-Lingual, Multi-Functionality, Multi-Granularity Text Embeddings Through Self-Knowledge Distillation","url":"https://arxiv.org/html/2402.03216v3"},{"title":"BAAI/bge-large-en · Hugging Face","url":"https://huggingface.co/BAAI/bge-large-en"},{"title":"[2309.07597v5] C-Pack: Packed Resources For General Chinese Embeddings","url":"https://arxiv.org/abs/2309.07597v5"},{"title":"Extending Embedding Models for Long Context Retrieval","url":"https://aclanthology.org/2024.emnlp-main.47.pdf"},{"title":"2309.07597 - C-Pack: Packaged Resources To Advance ...","url":"https://www.emergentmind.com/papers/2309.07597"}]

Based on the search results, I found the BibTeX citation for the Xiao et al. 2023 "C-Pack" paper. The BibTeX entry is:

```
@misc{bge_embedding, 
  title={C-Pack: Packaged Resources To Advance General Chinese Embedding}, 
  author={Shitao Xiao and Zheng Liu and Peitian Zhang and Niklas Muennighoff}, 
  year={2023}, 
  eprint={2309.07597}, 
  archivePrefix={arXiv}, 
  primaryClass={cs.CL}
}
```


This is the official BibTeX citation found on the Hugging Face model card for the BGE embeddings, which are the models described in the C-Pack paper.


REMINDER: You MUST include the sources above
…[truncated 56 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_r8_reference_search_20260518T070953",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 11 · 2026-05-18T07:10:52.696215+00:00_

Web search results for query: "Li et al "Inference-Time Intervention" ITI truthful language model BibTeX venue"

Links: [{"title":"[2306.03341] Inference-Time Intervention: Eliciting Truthful Answers from a Language Model","url":"https://arxiv.org/abs/2306.03341"},{"title":"Inference-time intervention: eliciting truthful answers from ...","url":"https://dl.acm.org/doi/10.5555/3666122.3667919"},{"title":"Inference-Time Intervention: Eliciting Truthful Answers from a Language Model","url":"https://arxiv.org/pdf/2306.03341"},{"title":"[PDF] Inference-Time Intervention: Eliciting Truthful Answers from a Language Model | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Inference-Time-Intervention:-Eliciting-Truthful-a-Li-Patel/405f8f5f1c6df1b3343c812832479aad5180b65f"},{"title":"Inference-Time Intervention (ITI)","url":"https://www.emergentmind.com/topics/inference-time-intervention-iti"},{"title":"GitHub - likenneth/honest_llama: Inference-Time Intervention: Eliciting Truthful Answers from a Language Model · GitHub","url":"https://github.com/likenneth/honest_llama"},{"title":"Inference-Time Intervention: Eliciting Truthful Answers from a Language Model | OpenReview","url":"https://openreview.net/forum?id=aLLuYpn83y"},{"title":"Inference-Time Intervention: Eliciting Truthful Answers from ...","url":"https://www.lesswrong.com/posts/kuQfnotjkQA4Kkfou/inference-time-intervention-eliciting-truthful-answers-from"},{"title":"(PDF) Inference-Time Intervention: Eliciting Truthful Answers from a Language Model","url":"https://www.researchgate.net/publication/371347185_Inference-Time_Intervention_Eliciting_Truthful_Answers_from_a_Language_Model"},{"title":"[2306.03341v6] Inference-Time Intervention: Eliciting Truthful Answers from a Language Model","url":"https://arxiv.org/abs/2306.03341v6"}]

Based on the search results, here is the information about the Li et al. "Inference-Time Intervention" paper:

## Paper Details

**Title:** Inference-Time Intervention: Eliciti
…[truncated 946 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_r8_reference_search_20260518T070953",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-18T07:10:52.696575+00:00_

Web search results for query: "Meng et al 2022 "Locating and Editing Factual Associations in GPT" NeurIPS BibTeX"

Links: [{"title":"Locating and Editing Factual Associations in GPT Kevin Meng⇤ MIT CSAIL","url":"https://proceedings.neurips.cc/paper_files/paper/2022/file/6f1d43d5a82a37e89b0665b33bf3a182-Paper-Conference.pdf"},{"title":"Locating and Editing Factual Associations in GPT","url":"https://proceedings.neurips.cc/paper_files/paper/2022/hash/6f1d43d5a82a37e89b0665b33bf3a182-Abstract-Conference.html"},{"title":"[2202.05262] Locating and Editing Factual Associations in GPT","url":"https://arxiv.org/abs/2202.05262"},{"title":"Locating and Editing Factual Associations in GPT","url":"https://neurips.cc/media/neurips-2022/Slides/53864.pdf"},{"title":"Locating and Editing Factual Associations in GPT | OpenReview","url":"https://openreview.net/forum?id=-h6WAS6eE4"},{"title":"[PDF] Locating and Editing Factual Associations in GPT | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Locating-and-Editing-Factual-Associations-in-GPT-Meng-Bau/996445d847f06e99b0bd259345408a0cf1bce87e"},{"title":"Locating and Editing Factual Associations in GPT","url":"https://bibbase.org/network/publication/meng-bau-andonian-belinkov-locatingandeditingfactualassociationsingpt-2022"},{"title":"Locating and Editing Factual Associations in GPT","url":"https://rome.baulab.info/"},{"title":"Locating and Editing Factual Associations in GPT Kevin Meng∗ MIT CSAIL","url":"https://arxiv.org/pdf/2202.05262"},{"title":"Locating and Editing Factual Associations in GPT - ar5iv - arXiv","url":"https://ar5iv.labs.arxiv.org/html/2202.05262"}]

I found the paper and BibTeX information! Here's what I found:

## Paper Details

The paper "Locating and Editing Factual Associations in GPT" by Kevin Meng, David Bau, Alex Andonian, and Yonatan Belinkov was published at Advances in Neural Information Processing Systems 35 (NeurIPS 2022).

## BibTeX Citation

The BibTeX entry is:

```
@inproceedings{DBLP
…[truncated 878 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_r8_reference_search_20260518T070953",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-18T07:10:52.696899+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "C-Pack BGE embedding SIGIR 2024 Shitao Xiao venue published"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_r8_reference_search_20260518T070953",
  "tool": "WebSearch",
  "tool_args": {
    "query": "C-Pack BGE embedding SIGIR 2024 Shitao Xiao venue published"
  }
}
```

</details>

---

### Tool call

_source line 14 · 2026-05-18T07:10:52.697108+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Li Kenneth \"Inference-Time Intervention\" NeurIPS 2023 proceedings volume pages"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_r8_reference_search_20260518T070953",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Li Kenneth \"Inference-Time Intervention\" NeurIPS 2023 proceedings volume pages"
  }
}
```

</details>

---

### Tool result

_source line 15 · 2026-05-18T07:10:52.697350+00:00_

Web search results for query: "C-Pack BGE embedding SIGIR 2024 Shitao Xiao venue published"

Links: [{"title":"C-Pack: Packed Resources For General Chinese Embeddings Shitao Xiao†","url":"https://arxiv.org/pdf/2309.07597"},{"title":"C-Pack: Packed Resources For General Chinese Embeddings | Request PDF","url":"https://www.researchgate.net/publication/382190819_C-Pack_Packed_Resources_For_General_Chinese_Embeddings"},{"title":"C-Pack: Packed Resources For General Chinese Embeddings | Proceedings of the 47th International ACM SIGIR Conference on Research and Development in Information Retrieval","url":"https://doi.org/10.1145/3626772.3657878"},{"title":"C-Pack: Packed Resources For General Chinese Embeddings","url":"https://arxiv.org/html/2309.07597v3"},{"title":"[PDF] C-Pack: Packed Resources For General Chinese Embeddings | Semantic Scholar","url":"https://www.semanticscholar.org/paper/C-Pack:-Packed-Resources-For-General-Chinese-Xiao-Liu/95dda1571f1a33245726fb53e9d5060ac7a0af25"},{"title":"Making Text Embedders Few-Shot Learners","url":"https://arxiv.org/html/2409.15700v1"},{"title":"[2309.07597] C-Pack: Packed Resources For General Chinese Embeddings","url":"https://arxiv.org/abs/2309.07597"},{"title":"Google Scholar","url":"https://scholar.google.com/scholar_lookup?doi=10.1145/3626772.3657878"},{"title":"BGE M3-Embedding: Multi-Lingual, Multi-Functionality, Multi-Granularity Text Embeddings Through Self-Knowledge Distillation","url":"https://arxiv.org/html/2402.03216v3"},{"title":"BAAI/bge-small-en-v1.5 · Hugging Face","url":"https://huggingface.co/BAAI/bge-small-en-v1.5"}]

Based on the search results, here's the information about the C-Pack BGE embedding paper:

**Venue:** The paper was published in the Proceedings of the 47th International ACM Conference on Research and Development in Information Retrieval (SIGIR '24), July 14–18, 2024, Washington, DC, USA.

**Published:** SIGIR '24, July 14–18, 2024, Washington, DC, USA

**Author:** Shitao Xiao et al.

**Paper
…[truncated 607 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_r8_reference_search_20260518T070953",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-18T07:10:52.697663+00:00_

Web search results for query: "Li Kenneth "Inference-Time Intervention" NeurIPS 2023 proceedings volume pages"

Links: [{"title":"Inference-Time Intervention: Eliciting Truthful Answers from a Language Model","url":"https://proceedings.neurips.cc/paper_files/paper/2023/hash/81b8390039b7302c909cb769f8b6cd93-Abstract-Conference.html"},{"title":"NeurIPS Poster Inference-Time Intervention: Eliciting Truthful Answers from a Language Model","url":"https://neurips.cc/virtual/2023/poster/71200"},{"title":"Inference-time intervention | Proceedings of the 37th International Conference on Neural Information Processing Systems","url":"https://dl.acm.org/doi/10.5555/3666122.3667919"},{"title":"[2306.03341] Inference-Time Intervention: Eliciting Truthful Answers from a Language Model","url":"https://arxiv.org/abs/2306.03341"},{"title":"Inference-Time Intervention: Eliciting Truthful Answers from a Language Model | OpenReview","url":"https://openreview.net/forum?id=aLLuYpn83y"},{"title":"GitHub - likenneth/honest_llama: Inference-Time Intervention: Eliciting Truthful Answers from a Language Model · GitHub","url":"https://github.com/likenneth/honest_llama"},{"title":"Inference-Time Intervention: Eliciting Truthful Answers from a Language Model - ADS","url":"https://ui.adsabs.harvard.edu/abs/2023arXiv230603341L/abstract"},{"title":"[Quick Review] Inference-Time Intervention: Eliciting Truthful Answers from a Language Model","url":"https://liner.com/review/inferencetime-intervention-eliciting-truthful-answers-from-a-language-model"},{"title":"NeurIPS Poster Inference-Time Intervention: Eliciting Truthful Answers from a Language Model","url":"https://nips.cc/virtual/2023/poster/71200"},{"title":"[PDF] Inference-Time Intervention: Eliciting Truthful Answers from a Language Model | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Inference-Time-Intervention:-Eliciting-Truthful-a-Li-Patel/405f8f5f1c6df1b3343c812832479aad5180b65f"}]

Based on the search results, here is the 
…[truncated 962 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_r8_reference_search_20260518T070953",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 17 · 2026-05-18T07:10:52.698004+00:00_

确认完毕。C-Pack 发表于 SIGIR 2024，ITI 发表于 NeurIPS 2023。以下是 5 篇论文的完整 BibTeX：

```bibtex
@article{page1954cusum,
  title={Continuous Inspection Schemes},
  author={Page, E. S.},
  journal={Biometrika},
  volume={41},
  number={1-2},
  pages={100--115},
  year={1954},
  url={https://doi.org/10.1093/biomet/41.1-2.100}
}

@inproceedings{reimers2019sentencebert,
  title={Sentence-{BERT}: Sentence Embeddings using Siamese {BERT}-Networks},
  author={Reimers, Nils and Gurevych, Iryna},
  booktitle={Proceedings of the 2019 Conference on Empirical Methods in Natural Language Processing and the 9th International Joint Conference on Natural Language Processing (EMNLP-IJCNLP)},
  pages={3982--3992},
  year={2019},
  publisher={Association for Computational Linguistics},
  url={https://doi.org/10.18653/v1/D19-1410}
}

@inproceedings{xiao2024cpack,
  title={C-Pack: Packed Resources For General Chinese Embeddings},
  author={Xiao, Shitao and Liu, Zheng and Zhang, Peitian and Muennighoff, Niklas},
  booktitle={Proceedings of the 47th International ACM SIGIR Conference on Research and Development in Information Retrieval},
  year={2024},
  url={https://doi.org/10.1145/3626772.3657878}
}

@inproceedings{meng2022locating,
  title={Locating and Editing Factual Associations in {GPT}},
  author={Meng, Kevin and Bau, David and Andonian, Alex and Belinkov, Yonatan},
  booktitle={Advances in Neural Information Processing Systems 35 (NeurIPS)},
  year={2022},
  url={https://proceedings.neurips.cc/paper_files/paper/2022/hash/6f1d43d5a82a37e89b0665b33bf3a182-Abstract-Conference.html}
}

@inproceedings{li2023iti,
  title={Inference-Time Intervention: Eliciting Truthful Answers from a Language Model},
  author={Li, Kenneth and Patel, Oam and Vi{\'e}gas, Fernanda and Pfister, Hanspeter and Wattenberg, Martin},
  booktitle={Advances in Neural Information Processing Systems 36 (NeurIPS)},
  year={2023},
  url={https://proceedings.neurips.cc/paper_files/paper/2023/hash/81b8390039b7302c909cb769f8b6cd93-Abstract-Conference.html}
}
```

关键确认：
- **Page 1954**: Biometrika, Vol 41(1-2), pp 100-115
- **Sentence-BERT**: EMNLP-IJCNLP 2019, pp 3982-3992
- **C-Pack/BGE**: SIGIR 2024（arXiv preprint 2023，正式发表 SIGIR 2024）
- **Meng et al. (ROME)**: NeurIPS 2022
- **Li et al. (ITI)**: NeurIPS 2023（不是 ICLR 2024）

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_research_r8_reference_search_20260518T070953"
}
```

</details>

---
