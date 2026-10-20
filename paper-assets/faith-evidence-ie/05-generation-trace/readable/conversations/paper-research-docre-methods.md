# paper research docre methods

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 45
- **Recorded user turns:** 0
- **Tool calls:** 22
- **Original source:** `logs/chats/worker_paper_research_docre_methods_20260517T150401.jsonl`
- **Structured JSON:** [`dbfb879507395c76bd04.json`](../../sessions/db/dbfb879507395c76bd04.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

45 recorded events

### Tool call

_source line 1 · 2026-05-17T15:08:11.998249+00:00_

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
  "session": "worker_paper_research_docre_methods_20260517T150401",
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

_source line 2 · 2026-05-17T15:08:11.998739+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_research_docre_methods_20260517T150401",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-17T15:08:11.999060+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "DocRED \"A Large-Scale Document-Level Relation Extraction Dataset\" Yao et al ACL 2019 arxiv"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_research_docre_methods_20260517T150401",
  "tool": "WebSearch",
  "tool_args": {
    "query": "DocRED \"A Large-Scale Document-Level Relation Extraction Dataset\" Yao et al ACL 2019 arxiv"
  }
}
```

</details>

---

### Tool result

_source line 4 · 2026-05-17T15:08:11.999400+00:00_

Web search results for query: "DocRED "A Large-Scale Document-Level Relation Extraction Dataset" Yao et al ACL 2019 arxiv"

Links: [{"title":"GitHub - thunlp/DocRED: Dataset and codes for ACL 2019 DocRED: A Large-Scale Document-Level Relation Extraction Dataset. · GitHub","url":"https://github.com/thunlp/DocRED"},{"title":"DocRED: A Large-Scale Document-Level Relation Extraction Dataset - ACL Anthology","url":"https://aclanthology.org/P19-1074/"},{"title":"[1906.06127] DocRED: A Large-Scale Document-Level Relation Extraction Dataset","url":"https://arxiv.org/abs/1906.06127"},{"title":"dblp: DocRED: A Large-Scale Document-Level Relation Extraction Dataset.","url":"https://dblp.org/rec/conf/acl/YaoYLHLLLHZS19.html"},{"title":"[PDF] DocRED: A Large-Scale Document-Level Relation Extraction Dataset | Semantic Scholar","url":"https://www.semanticscholar.org/paper/DocRED:-A-Large-Scale-Document-Level-Relation-Yao-Ye/2745fc72e1dd53d1c30f17cf05841b163c2f63c9"},{"title":"DocRED: A Large-Scale Document-Level Relation Extraction Dataset | Request PDF","url":"https://www.researchgate.net/publication/335780641_DocRED_A_Large-Scale_Document-Level_Relation_Extraction_Dataset"},{"title":"(PDF) DocRED: A Large-Scale Document-Level Relation Extraction Dataset","url":"https://www.researchgate.net/publication/333815327_DocRED_A_Large-Scale_Document-Level_Relation_Extraction_Dataset"},{"title":"DocRED: A Large-Scale Document-Level Relation Extraction Dataset - Big Physics","url":"https://www.bigphysics.org/index.php/DocRED:_A_Large-Scale_Document-Level_Relation_Extraction_Dataset"},{"title":"thunlp/docred · Datasets at Hugging Face","url":"https://huggingface.co/datasets/thunlp/docred"},{"title":"[Quick Review] DocRED: A Large-Scale Document-Level Relation Extraction Dataset","url":"https://liner.com/review/docred-largescale-documentlevel-relation-extraction-dataset"}]

I've found the information about the DocRED paper. Here are the search results:

## Key Information Found:

**Paper Det
…[truncated 1433 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_research_docre_methods_20260517T150401",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-17T15:08:11.999668+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Re-DocRED Tan et al EMNLP 2022 re-annotated DocRED false negatives arxiv"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_research_docre_methods_20260517T150401",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Re-DocRED Tan et al EMNLP 2022 re-annotated DocRED false negatives arxiv"
  }
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-17T15:08:11.999944+00:00_

Web search results for query: "Re-DocRED Tan et al EMNLP 2022 re-annotated DocRED false negatives arxiv"

Links: [{"title":"[2205.12696] Revisiting DocRED -- Addressing the False Negative Problem in Relation Extraction","url":"https://arxiv.org/abs/2205.12696"},{"title":"GitHub - tonytan48/Re-DocRED","url":"https://github.com/tonytan48/Re-DocRED"},{"title":"Revisiting DocRED -- Addressing the False Negative Problem in Relation Extraction - ADS","url":"https://ui.adsabs.harvard.edu/abs/2022arXiv220512696T/abstract"},{"title":"Revisiting DocRED – Addressing the False Negative Problem in Relation Extraction","url":"https://arxiv.org/html/2205.12696"},{"title":"Revisiting DocRED – Addressing the False Negative Problem","url":"https://arxiv.org/pdf/2205.12696"},{"title":"Revisiting DocRED - Addressing the False Negative Problem in Relation Extraction - ACL Anthology","url":"https://aclanthology.org/2022.emnlp-main.580/"},{"title":"tonytan48/Re-DocRED · Datasets at Hugging Face","url":"https://huggingface.co/datasets/tonytan48/Re-DocRED"},{"title":"Revisiting DocRED – Addressing the False Negative ...","url":"https://aclanthology.org/2022.emnlp-main.580.pdf"},{"title":"[2205.12696v3] Revisiting DocRED -- Addressing the False Negative Problem in Relation Extraction","url":"http://arxiv.org/abs/2205.12696v3"},{"title":"README.md · tonytan48/Re-DocRED at main","url":"https://huggingface.co/datasets/tonytan48/Re-DocRED/blob/main/README.md"}]

I found the paper you're looking for! Here's what the search revealed:

## Re-DocRED: Revisiting DocRED - Addressing the False Negative Problem in Relation Extraction

This is a paper by Tan et al. published at EMNLP 2022, available on arXiv as paper 2205.12696.

**Key Details:**

- The paper identifies that the annotation of DocRED is incomplete with prevalent false negative samples, and analyzes the causes and effects of this overwhelming false negative problem.

- The researchers re-annotated 4,053 documents in the DocRED dataset by a
…[truncated 644 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_research_docre_methods_20260517T150401",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-17T15:08:12.000220+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "ATLOP \"Adaptive Thresholding and Localized Context Pooling\" Zhou et al AAAI 2021 document-level relation extraction arxiv"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_research_docre_methods_20260517T150401",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ATLOP \"Adaptive Thresholding and Localized Context Pooling\" Zhou et al AAAI 2021 document-level relation extraction arxiv"
  }
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-17T15:08:12.000528+00:00_

Web search results for query: "ATLOP "Adaptive Thresholding and Localized Context Pooling" Zhou et al AAAI 2021 document-level relation extraction arxiv"

Links: [{"title":"Document-Level Relation Extraction with Adaptive Thresholding and Localized Context Pooling | Proceedings of the AAAI Conference on Artificial Intelligence","url":"https://ojs.aaai.org/index.php/AAAI/article/view/17717"},{"title":"GitHub - wzhouad/ATLOP: Source code for paper \"Document-Level Relation Extraction with Adaptive Thresholding and Localized Context Pooling\", AAAI 2021","url":"https://github.com/wzhouad/ATLOP"},{"title":"ATLOP/README.md at main · wzhouad/ATLOP","url":"https://github.com/wzhouad/ATLOP/blob/main/README.md?plain=1"},{"title":"Document-Level Relation Extraction with Adaptive Thresholding and Localized Context Pooling | CoLab","url":"https://colab.ws/articles/10.1609/aaai.v35i16.17717"},{"title":"Document-Level Relation Extraction with Adaptive Thresholding and Localized Context Pooling","url":"https://papertalk.org/papertalks/29629"},{"title":"Document-Level Relation Extraction with Adaptive Thresholding and","url":"https://wzhouad.github.io/slides/ATLOP_AAAI21.pdf"},{"title":"Boosting Document-Level Relation Extraction by Mining ...","url":"https://aclanthology.org/2022.emnlp-main.704.pdf"},{"title":"Releases · wzhouad/ATLOP","url":"https://github.com/wzhouad/ATLOP/releases"},{"title":"ATLOP/evaluation.py at main · wzhouad/ATLOP","url":"https://github.com/wzhouad/ATLOP/blob/main/evaluation.py"},{"title":"ATLOP/model.py at main · wzhouad/ATLOP","url":"https://github.com/wzhouad/ATLOP/blob/main/model.py"}]

I found the paper you're looking for! Here are the key details:

## ATLOP Paper Information

The ATLOP (Adaptive Thresholding and Localized Context Pooling) model achieves an F1 score of 63.4 on document-level relation extraction, and significantly outperforms existing models on both CDR and GDA datasets.

### Technical Contributions

The paper proposes two novel techni
…[truncated 911 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_research_docre_methods_20260517T150401",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-17T15:08:12.000818+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "LMRC LLM document-level relation extraction Li et al 2023 arxiv"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_research_docre_methods_20260517T150401",
  "tool": "WebSearch",
  "tool_args": {
    "query": "LMRC LLM document-level relation extraction Li et al 2023 arxiv"
  }
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-17T15:08:12.001093+00:00_

Web search results for query: "LMRC LLM document-level relation extraction Li et al 2023 arxiv"

Links: [{"title":"LLM with Relation Classifier for Document-Level Relation Extraction","url":"https://arxiv.org/html/2408.13889v1"},{"title":"AutoRE: Document-Level Relation Extraction with Large Language Models","url":"https://arxiv.org/html/2403.14888v1"},{"title":"[2408.13889] LLM with Relation Classifier for Document-Level Relation Extraction","url":"https://arxiv.org/abs/2408.13889"},{"title":"GLiDRE: Generalist Lightweight model for Document-level Relation Extraction","url":"https://arxiv.org/html/2508.00757"},{"title":"Relation as a Prior: A Novel Paradigm for LLM-based Document-level Relation Extraction","url":"https://arxiv.org/html/2511.08143v1"},{"title":"LLM with Relation Classifier for Document-Level Relation Extraction | AI Research Paper Details","url":"https://www.aimodels.fyi/papers/arxiv/llm-relation-classifier-document-level-relation-extraction"},{"title":"[Literature Review] LLM with Relation Classifier for Document-Level Relation Extraction","url":"https://www.themoonlight.io/en/review/llm-with-relation-classifier-for-document-level-relation-extraction"},{"title":"(PDF) LLM with Relation Classifier for Document-Level Relation Extraction","url":"https://www.researchgate.net/publication/383428854_LLM_with_Relation_Classifier_for_Document-Level_Relation_Extraction"},{"title":"Enhancing Relation Extraction via Supervised Rationale Verification and Feedback","url":"https://arxiv.org/html/2412.07289v2"},{"title":"Document-Level In-Context Few-Shot Relation Extraction via Pre-Trained Language Models","url":"https://arxiv.org/html/2310.11085"}]

Based on the search results, I found information about the LMRC paper. Here's what I found:

## LMRC: LLM with Relation Classifier for Document-Level Relation Extraction

The paper is titled "LLM with Relation Classifier for Document-Level Relation Extraction" by Xingzuo Li and 3 other authors. However, it's importan
…[truncated 1066 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_research_docre_methods_20260517T150401",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-17T15:08:12.001371+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "DocKS-RAG \"document-level relation extraction\" RAG Xu et al 2024 arxiv"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_research_docre_methods_20260517T150401",
  "tool": "WebSearch",
  "tool_args": {
    "query": "DocKS-RAG \"document-level relation extraction\" RAG Xu et al 2024 arxiv"
  }
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-17T15:08:12.001641+00:00_

Web search results for query: "DocKS-RAG "document-level relation extraction" RAG Xu et al 2024 arxiv"

Links: [{"title":"DocKS-RAG: Optimizing Document-Level Relation Extraction through LLM-Enhanced Hybrid Prompt Tuning | OpenReview","url":"https://openreview.net/forum?id=SVl9tIADWV"},{"title":"RAKG:Document-level Retrieval Augmented Knowledge Graph Construction","url":"https://arxiv.org/html/2504.09823v1"},{"title":"Knowledge Graph-Guided Retrieval Augmented Generation","url":"https://arxiv.org/html/2502.06864v1"},{"title":"Relation Extraction with Fine-Tuned Large Language Models in Retrieval Augmented Generation Frameworks","url":"https://arxiv.org/html/2406.14745v2"},{"title":"ICML Poster DocKS-RAG: Optimizing Document-Level Relation Extraction through LLM-Enhanced Hybrid Prompt Tuning","url":"https://icml.cc/virtual/2025/poster/45220"},{"title":"Date of publication xxxx 00, 2024, date of current version Oct. 15, 2024.","url":"https://arxiv.org/pdf/2406.03790"},{"title":"A Comprehensive Survey of Document-level Relation ...","url":"https://arxiv.org/pdf/2309.16396"},{"title":"DocKS-RAG: Optimizing Document-Level Relation Extraction through LLM-Enhanced Hybrid Prompt Tuning","url":"https://proceedings.mlr.press/v267/xu25am.html"},{"title":"[2403.14888] AutoRE: Document-Level Relation Extraction with Large Language Models","url":"https://arxiv.org/abs/2403.14888"},{"title":"Synergizing RAG and Reasoning: A Systematic Review","url":"https://arxiv.org/html/2504.15909v1"}]

The search has found relevant results about DocKS-RAG. Here's what I found:

## DocKS-RAG Overview

DocKS-RAG: Optimizing Document-Level Relation Extraction through LLM-Enhanced Hybrid Prompt Tuning aims to extract comprehensive correlations between entities and relations from documents.

The paper was authored by Xiaolong Xu, Yibo Zhou, Haolong Xiang, Xiaoyong Li, Xuyun Zhang, Lianyong Qi, and Wanchun Dou.

## Publication Information

The paper was published in the Proceedings of the 42nd Intern
…[truncated 648 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_research_docre_methods_20260517T150401",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-17T15:08:12.001907+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "GenRES generative relation extraction evaluation arxiv"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_research_docre_methods_20260517T150401",
  "tool": "WebSearch",
  "tool_args": {
    "query": "GenRES generative relation extraction evaluation arxiv"
  }
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-17T15:08:12.002172+00:00_

Web search results for query: "GenRES generative relation extraction evaluation arxiv"

Links: [{"title":"[2402.10744] GenRES: Rethinking Evaluation for Generative Relation Extraction in the Era of Large Language Models","url":"https://arxiv.org/abs/2402.10744"},{"title":"GENRES: Rethinking Evaluation for Generative Relation Extraction in the","url":"https://arxiv.org/pdf/2402.10744"},{"title":"GENRES: Rethinking Evaluation for Generative Relation Extraction in the Era of Large Language Models - Illinois Experts","url":"https://experts.illinois.edu/en/publications/genres-rethinking-evaluation-for-generative-relation-extraction-i/"},{"title":"GenRES: Rethinking Evaluation for Generative Relation Extraction in the Era of Large Language Models","url":"https://www.emergentmind.com/papers/2402.10744"},{"title":"GitHub - pat-jj/GenRES: [NAACL'24] Evaluate Generative Relation Extraction","url":"https://github.com/pat-jj/genres"},{"title":"Rethinking Evaluation for Generative Relation Extraction in ...","url":"https://aclanthology.org/2024.naacl-long.155.pdf"},{"title":"GenRES: Rethinking Evaluation for Generative Relation Extraction in the Era of Large Language Models - ACL Anthology","url":"https://aclanthology.org/2024.naacl-long.155/"},{"title":"A Survey of Generative Information Extraction","url":"https://aclanthology.org/2025.coling-main.324.pdf"},{"title":"GenRE: A Generative Model for Relation Extraction | OpenReview","url":"https://openreview.net/forum?id=w0fxBD6tJbV"},{"title":"[2202.13229] A Generative Model for Relation Extraction and Classification","url":"https://arxiv.org/abs/2202.13229"}]

I found relevant research on GenRES. Here's what I discovered:

## GenRES: Rethinking Evaluation for Generative Relation Extraction

The field of relation extraction (RE) is experiencing a notable shift towards generative relation extraction (GRE), leveraging the capabilities of large language models (LLMs). However, traditional relation extraction (RE) metrics like precis
…[truncated 1274 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_research_docre_methods_20260517T150401",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-17T15:08:12.002472+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "DocuNet \"An Efficient Framework for Document-Level Relation Extraction\" Zhang et al 2021 arxiv"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_research_docre_methods_20260517T150401",
  "tool": "WebSearch",
  "tool_args": {
    "query": "DocuNet \"An Efficient Framework for Document-Level Relation Extraction\" Zhang et al 2021 arxiv"
  }
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-17T15:08:12.002746+00:00_

Web search results for query: "DocuNet "An Efficient Framework for Document-Level Relation Extraction" Zhang et al 2021 arxiv"

Links: [{"title":"Augmenting Document-level Relation Extraction with Efficient Multi-Supervision","url":"https://arxiv.org/html/2407.01026v1"},{"title":"[2106.03618] Document-level Relation Extraction as Semantic Segmentation","url":"https://arxiv.org/abs/2106.03618"},{"title":"COMM: Concentrated Margin Maximization for Robust Document-Level Relation Extraction","url":"https://arxiv.org/html/2503.13885"},{"title":"Did the Models Understand Documents? Benchmarking Models for Language Understanding in Document-Level Relation Extraction","url":"https://arxiv.org/html/2306.11386"},{"title":"Document-Level In-Context Few-Shot Relation Extraction via Pre-Trained Language Models","url":"https://arxiv.org/html/2310.11085v3"},{"title":"GitHub - zjunlp/DocuNet: [IJCAI 2021] Document-level Relation Extraction as Semantic Segmentation · GitHub","url":"https://github.com/zjunlp/DocuNet"},{"title":"Revisiting Document-Level Relation Extraction with ...","url":"https://ojs.aaai.org/index.php/AAAI/article/view/29792/31370"},{"title":"KnowRA: Knowledge Retrieval Augmented Method for Document-level Relation Extraction with Comprehensive Reasoning Abilities","url":"https://arxiv.org/html/2501.00571"},{"title":"DocuNet/README.md at main · zjunlp/DocuNet","url":"https://github.com/zjunlp/DocuNet/blob/main/README.md"},{"title":"REXEL: An End-to-end Model for Document-Level Relation Extraction and Entity Linking","url":"https://arxiv.org/html/2404.12788v1"}]

Based on the search results, I found information about the DocuNet paper you're looking for.

DocuNet (Zhang et al. 2021) regards the DocRE task as a semantic segmentation task, attempting to capture both local context information and global interdependency among triples.

More specifically, the paper proposes a Document U-shaped Network for document-level relation extraction by predicting an entity-level re
…[truncated 880 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_research_docre_methods_20260517T150401",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-17T15:08:12.003009+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "KD-DocRE \"Knowledge Distillation\" Tan et al 2022 document-level relation extraction arxiv"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_research_docre_methods_20260517T150401",
  "tool": "WebSearch",
  "tool_args": {
    "query": "KD-DocRE \"Knowledge Distillation\" Tan et al 2022 document-level relation extraction arxiv"
  }
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-17T15:08:12.003298+00:00_

Web search results for query: "KD-DocRE "Knowledge Distillation" Tan et al 2022 document-level relation extraction arxiv"

Links: [{"title":"[2203.10900] Document-Level Relation Extraction with Adaptive Focal Loss and Knowledge Distillation","url":"https://arxiv.org/abs/2203.10900"},{"title":"GitHub - tonytan48/KD-DocRE: Implementation of Document-level Relation Extraction with Knowledge Distillation and Adaptive Focal Loss · GitHub","url":"https://github.com/tonytan48/KD-DocRE"},{"title":"Document-Level Relation Extraction with Adaptive Focal Loss and Knowledge Distillation - ADS","url":"https://ui.adsabs.harvard.edu/abs/2022arXiv220310900T/abstract"},{"title":"Consistent Document-Level Relation Extraction via Counterfactuals","url":"https://arxiv.org/html/2407.06699v2"},{"title":"Augmenting Document-level Relation Extraction with Efficient Multi-Supervision","url":"https://arxiv.org/html/2407.01026v1"},{"title":"[2203.10900v1] Document-Level Relation Extraction with Adaptive Focal Loss and Knowledge Distillation","url":"https://arxiv.org/abs/2203.10900v1"},{"title":"On the Robustness of Document-Level Relation Extraction Models to Entity Name Variations","url":"https://arxiv.org/html/2406.07444v1"},{"title":"Document-Level Relation Extraction with Adaptive Focal Loss and Knowledge Distillation - ACL Anthology","url":"https://aclanthology.org/2022.findings-acl.132/"},{"title":"Rethinking Document-Level Relation Extraction: A Reality Check","url":"https://arxiv.org/html/2306.08953"},{"title":"LLM with Relation Classifier for Document-Level Relation Extraction","url":"https://arxiv.org/html/2408.13889v1"}]

I found the paper you were searching for! Here are the key details:

## KD-DocRE Paper Summary

**Title:** Document-Level Relation Extraction with Adaptive Focal Loss and Knowledge Distillation

**Authors:** Qingyu Tan, Ruidan He, Lidong Bing, and Hwee Tou Ng

**Publication:** Findings of ACL 2022

**arXiv ID:** 2203.10900 (posted March 21, 2022)

## Key Contribut
…[truncated 681 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_research_docre_methods_20260517T150401",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-17T15:08:12.003568+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "DocKS-RAG arxiv ID Xu 2024 document-level relation extraction LLM hybrid prompt tuning"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_research_docre_methods_20260517T150401",
  "tool": "WebSearch",
  "tool_args": {
    "query": "DocKS-RAG arxiv ID Xu 2024 document-level relation extraction LLM hybrid prompt tuning"
  }
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-17T15:08:12.003834+00:00_

Web search results for query: "DocKS-RAG arxiv ID Xu 2024 document-level relation extraction LLM hybrid prompt tuning"

Links: [{"title":"DocKS-RAG: Optimizing Document-Level Relation Extraction through LLM-Enhanced Hybrid Prompt Tuning","url":"https://proceedings.mlr.press/v267/xu25am.html"},{"title":"ICML Poster DocKS-RAG: Optimizing Document-Level Relation Extraction through LLM-Enhanced Hybrid Prompt Tuning","url":"https://icml.cc/virtual/2025/poster/45220"},{"title":"DocKS-RAG: Optimizing Document-Level Relation Extraction through LLM-Enhanced Hybrid Prompt Tuning | OpenReview","url":"https://openreview.net/forum?id=SVl9tIADWV"},{"title":"Unified Ranking for Multiple Retrieval-Augmented Large ...","url":"https://dl.acm.org/doi/pdf/10.1145/3626772.3657733"},{"title":"Relation Extraction with Fine-Tuned Large Language Models in Retrieval Augmented Generation Frameworks","url":"https://arxiv.org/html/2406.14745v2"},{"title":"[2403.14888] AutoRE: Document-Level Relation Extraction with Large Language Models","url":"https://arxiv.org/abs/2403.14888"},{"title":"Relation as a Prior: A Novel Paradigm for LLM-based Document-level Relation Extraction","url":"https://arxiv.org/html/2511.08143"},{"title":"1 Retrieval-Augmented Generation for Large Language Models: A Survey","url":"https://arxiv.org/pdf/2312.10997"},{"title":"AutoRE: Document-Level Relation Extraction with Large ...","url":"https://aclanthology.org/2024.acl-demos.20.pdf"},{"title":"A Survey of Graph Retrieval-Augmented Generation for ...","url":"https://arxiv.org/pdf/2501.13958"}]

Based on the search results, I found information about DocKS-RAG. Here's what the research paper contains:

## DocKS-RAG Paper Summary

DocKS-RAG is titled "Optimizing Document-Level Relation Extraction through LLM-Enhanced Hybrid Prompt Tuning" and focuses on document-level relation extraction (RE), which aims to extract comprehensive correlations between entities and relations from documents.

**Key Components:**

The framework
…[truncated 1025 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_research_docre_methods_20260517T150401",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 21 · 2026-05-17T15:08:12.004090+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "DocKS-RAG arxiv preprint 2024 Xiaolong Xu"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_research_docre_methods_20260517T150401",
  "tool": "WebSearch",
  "tool_args": {
    "query": "DocKS-RAG arxiv preprint 2024 Xiaolong Xu"
  }
}
```

</details>

---

### Tool result

_source line 22 · 2026-05-17T15:08:12.004367+00:00_

Web search results for query: "DocKS-RAG arxiv preprint 2024 Xiaolong Xu"

Links: [{"title":"arXiv.org e-Print archive","url":"https://arxiv.org/"},{"title":"DoTA-RAG: Dynamic of Thought Aggregation RAG","url":"https://arxiv.org/html/2506.12571v1"},{"title":"CodeRAG: Supportive Code Retrieval on Bigraph for Real-World Code Generation","url":"https://arxiv.org/html/2504.10046v1"},{"title":"Preprint. SELF-RAG: LEARNING TO RETRIEVE, GENERATE, AND","url":"https://arxiv.org/pdf/2310.11511"},{"title":"Arxiv","url":"https://arxiv.org/pdf/2502.01477"},{"title":"[2410.12837] A Comprehensive Survey of Retrieval-Augmented Generation (RAG): Evolution, Current Landscape and Future Directions","url":"https://arxiv.org/abs/2410.12837"},{"title":"A Survey of Graph Retrieval-Augmented Generation for Customized Large Language Models","url":"https://arxiv.org/html/2501.13958v1"},{"title":"A Survey of RAG-Reasoning Systems in LLMs","url":"https://arxiv.org/pdf/2507.09477"},{"title":"Retrieval-Augmented Generation for AI-Generated Content: A Survey","url":"https://arxiv.org/html/2402.19473v2"},{"title":"HM-RAG: Hierarchical Multi-Agent Multimodal Retrieval Augmented Generation","url":"https://arxiv.org/html/2504.12330v1"}]

Based on the search results, I was unable to find a specific arxiv preprint titled "DocKS-RAG" from 2024 by Xiaolong Xu. The search returned various RAG (Retrieval-Augmented Generation) related papers and surveys from 2024-2025, but none matching the exact title and author you specified.

The results included papers on related RAG topics such as:
- DoTA-RAG (Dynamic of Thought Aggregation RAG)
- CodeRAG (Code Retrieval)
- Self-RAG
- Various RAG surveys and applications

If you're looking for information about a specific paper, you might want to:
1. Try searching directly on arxiv.org with different keywords
2. Verify the exact spelling of the paper title
3. Check if the author name might be spelled differently
4. Search for the arxiv ID if you have it

Would you like
…[truncated 157 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_research_docre_methods_20260517T150401",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 23 · 2026-05-17T15:08:12.004633+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "site:arxiv.org \"DocKS-RAG\" OR \"document-level relation extraction\" \"hybrid prompt tuning\" Xu 2024"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_research_docre_methods_20260517T150401",
  "tool": "WebSearch",
  "tool_args": {
    "query": "site:arxiv.org \"DocKS-RAG\" OR \"document-level relation extraction\" \"hybrid prompt tuning\" Xu 2024"
  }
}
```

</details>

---

### Tool result

_source line 24 · 2026-05-17T15:08:12.004889+00:00_

Web search results for query: "site:arxiv.org "DocKS-RAG" OR "document-level relation extraction" "hybrid prompt tuning" Xu 2024"

No links found.

The search was processed, but it appears that the web search tool doesn't support the special search operators like "site:" that you included in your query. Unfortunately, no results were returned for this search.

To help you find this content more effectively, I'd recommend:

1. **Visit arxiv.org directly** and use their search interface with your keywords
2. **Try a simpler search** without the "site:" operator, such as: "DocKS-RAG hybrid prompt tuning Xu 2024" or "document-level relation extraction hybrid prompt tuning"
3. **Browse by category** on arxiv.org if you know the relevant research area (e.g., cs.CL for natural language processing)

Would you like me to perform a web search with a simplified version of this query?


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_research_docre_methods_20260517T150401",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 25 · 2026-05-17T15:08:12.005121+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "LLM document-level relation extraction 2024 2025 state-of-the-art DocRED Re-DocRED new methods"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_research_docre_methods_20260517T150401",
  "tool": "WebSearch",
  "tool_args": {
    "query": "LLM document-level relation extraction 2024 2025 state-of-the-art DocRED Re-DocRED new methods"
  }
}
```

</details>

---

### Tool result

_source line 26 · 2026-05-17T15:08:12.005433+00:00_

Web search results for query: "LLM document-level relation extraction 2024 2025 state-of-the-art DocRED Re-DocRED new methods"

Links: [{"title":"LLM with Relation Classifier for Document-Level Relation Extraction","url":"https://arxiv.org/html/2408.13889v1"},{"title":"[PDF] DocRED: A Large-Scale Document-Level Relation Extraction Dataset | Semantic Scholar","url":"https://www.semanticscholar.org/paper/DocRED:-A-Large-Scale-Document-Level-Relation-Yao-Ye/2745fc72e1dd53d1c30f17cf05841b163c2f63c9"},{"title":"Leveraging Large Language Models for Document-Level Complex Relation Extraction Through Self-Verification and Tool-Assisted Relational Reasoning | Springer Nature Link","url":"https://link.springer.com/chapter/10.1007/978-981-96-9812-7_32"},{"title":"AutoRE: Document-Level Relation Extraction with Large Language Models","url":"https://arxiv.org/html/2403.14888v1"},{"title":"[2403.14888] AutoRE: Document-Level Relation Extraction with Large Language Models","url":"https://arxiv.org/abs/2403.14888"},{"title":"Logical Rule-Constrained Large Language Models for Document-Level Relation Extraction | Springer Nature Link","url":"https://link.springer.com/chapter/10.1007/978-981-95-3343-5_11"},{"title":"Document-level Relation Extraction with Relation Correlations - ScienceDirect","url":"https://www.sciencedirect.com/science/article/abs/pii/S0893608023006883"},{"title":"Document-Level Relation Extraction","url":"https://www.emergentmind.com/topics/document-level-relation-extraction"},{"title":"LLM with Relation Classifier for Document-Level Relation Extraction","url":"https://openreview.net/pdf?id=SOWcC2cCMT"},{"title":"A Temporal Knowledge Graph Generation Dataset Supervised Distantly by Large Language Models | Scientific Data","url":"https://www.nature.com/articles/s41597-025-05062-0"}]

Here's a comprehensive summary of recent state-of-the-art developments in LLM-based document-level relation extraction (2024-2025):

## Key Recent Methods

### AutoRE (2024)
AutoRE is a
…[truncated 1903 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_research_docre_methods_20260517T150401",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 27 · 2026-05-17T15:08:12.005701+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "AutoRE \"Document-Level Relation Extraction with Large Language Models\" arxiv 2403.14888 authors venue"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_research_docre_methods_20260517T150401",
  "tool": "WebSearch",
  "tool_args": {
    "query": "AutoRE \"Document-Level Relation Extraction with Large Language Models\" arxiv 2403.14888 authors venue"
  }
}
```

</details>

---

### Tool result

_source line 28 · 2026-05-17T15:08:12.006094+00:00_

Web search results for query: "AutoRE "Document-Level Relation Extraction with Large Language Models" arxiv 2403.14888 authors venue"

Links: [{"title":"[2403.14888] AutoRE: Document-Level Relation Extraction with Large Language Models","url":"https://arxiv.org/abs/2403.14888"},{"title":"AutoRE: Document-Level Relation Extraction with Large Language Models","url":"https://arxiv.org/html/2403.14888v1"},{"title":"[2403.14888] AutoRE: Document-Level Relation Extraction with Large Language Models","url":"http://export.arxiv.org/abs/2403.14888"},{"title":"AutoRE: Document-Level Relation Extraction with Large Language Models | alphaXiv","url":"https://www.alphaxiv.org/abs/2403.14888v1"},{"title":"GitHub - THUDM/AutoRE","url":"https://github.com/THUDM/AutoRE"},{"title":"[Literature Review] AutoRE: Document-Level Relation Extraction with Large Language Models","url":"https://www.themoonlight.io/en/review/autore-document-level-relation-extraction-with-large-language-models"},{"title":"AutoRE: Document-Level Relation Extraction with Large ...","url":"https://www.aimodels.fyi/papers/arxiv/autore-document-level-relation-extraction-large-language"},{"title":"AutoRE/README_EN.md at main · THUDM/AutoRE","url":"https://github.com/THUDM/AutoRE/blob/main/README_EN.md"},{"title":"AutoRE: Document-Level Relation Extraction with Large Language Models","url":"https://yiyibooks.cn/__trs__/arxiv/2403.14888v1/index.html"},{"title":"(PDF) LLM with Relation Classifier for Document-Level Relation Extraction","url":"https://www.researchgate.net/publication/383428854_LLM_with_Relation_Classifier_for_Document-Level_Relation_Extraction"}]

Based on the search results, here's the information about AutoRE:

**Authors:** Lilong Xue, Dan Zhang, Yuxiao Dong, and Jie Tang

**Title:** AutoRE: Document-Level Relation Extraction with Large Language Models

**ArXiv ID:** 2403.14888

**Venue:** The Knowledge Engineering Group (KEG), Tsinghua University

The paper was submitted on 21 Mar 2024 (v1), last revis
…[truncated 137 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_research_docre_methods_20260517T150401",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 29 · 2026-05-17T15:08:12.006379+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "AutoRE Xue Zhang Dong Tang ACL 2024 accepted venue conference document-level relation extraction"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_research_docre_methods_20260517T150401",
  "tool": "WebSearch",
  "tool_args": {
    "query": "AutoRE Xue Zhang Dong Tang ACL 2024 accepted venue conference document-level relation extraction"
  }
}
```

</details>

---

### Tool result

_source line 30 · 2026-05-17T15:08:12.006662+00:00_

Web search results for query: "AutoRE Xue Zhang Dong Tang ACL 2024 accepted venue conference document-level relation extraction"

Links: [{"title":"AutoRE: Document-Level Relation Extraction with Large Language Models - ACL Anthology","url":"https://aclanthology.org/2024.acl-demos.20/"},{"title":"Accepted Demo Papers - ACL 2024","url":"https://2024.aclweb.org/program/demo_papers/"},{"title":"GitHub - THUDM/AutoRE","url":"https://github.com/THUDM/AutoRE"},{"title":"[2403.14888] AutoRE: Document-Level Relation Extraction with Large Language Models","url":"https://arxiv.org/abs/2403.14888"},{"title":"AutoRE: Document-Level Relation Extraction with Large ...","url":"https://aclanthology.org/2024.acl-demos.20.pdf"},{"title":"Logical Rule-Constrained Large Language Models for Document-Level Relation Extraction | Springer Nature Link","url":"https://link.springer.com/chapter/10.1007/978-981-95-3343-5_11"},{"title":"(PDF) AutoRE: Document-Level Relation Extraction with Large Language Models","url":"https://www.researchgate.net/publication/384197797_AutoRE_Document-Level_Relation_Extraction_with_Large_Language_Models"},{"title":"AutoRE: Document-Level Relation Extraction with Large Language Models","url":"https://arxiv.org/html/2403.14888v1"},{"title":"A Survey of Generative Information Extraction","url":"https://aclanthology.org/2025.coling-main.324.pdf"},{"title":"CaDRL: Document-level Relation Extraction via Context- ...","url":"https://aclanthology.org/2025.coling-main.551.pdf"}]

Based on the search results, here's what I found about the AutoRE paper:

## AutoRE: Document-Level Relation Extraction with Large Language Models

The paper "AutoRE: Document-Level Relation Extraction with Large Language Models" by Lilong Xue, Dan Zhang, Yuxiao Dong, and Jie Tang was accepted at the 62nd Annual Meeting of the Association for Computational Linguistics (ACL 2024) in the Volume 3: System Demonstrations track, held in Bangkok, Thailand.

### Key Details:

- **Venue**: ACL 2024 Sys
…[truncated 825 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_research_docre_methods_20260517T150401",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 31 · 2026-05-17T15:08:12.006923+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "LMRC arxiv 2408.13889 authors full list Li et al venue accepted conference"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_research_docre_methods_20260517T150401",
  "tool": "WebSearch",
  "tool_args": {
    "query": "LMRC arxiv 2408.13889 authors full list Li et al venue accepted conference"
  }
}
```

</details>

---

### Tool result

_source line 32 · 2026-05-17T15:08:12.007178+00:00_

Web search results for query: "LMRC arxiv 2408.13889 authors full list Li et al venue accepted conference"

Links: [{"title":"[2408.13889] LLM with Relation Classifier for Document-Level Relation Extraction","url":"https://arxiv.org/abs/2408.13889"},{"title":"LLM with Relation Classifier for Document-Level Relation Extraction","url":"https://arxiv.org/html/2408.13889"},{"title":"arXiv:2311.08213v1 [cs.CV] 14 Nov 2023","url":"https://arxiv.org/pdf/2311.08213"},{"title":"Computation and Language","url":"https://www.arxiv.org/list/cs.CL/pastweek?skip=4&show=500"},{"title":"Authorship Attribution in the Era of LLMs: Problems, Methodologies, and Challenges","url":"https://arxiv.org/html/2408.08946v2"},{"title":"Large Language Models: A Survey","url":"https://arxiv.org/html/2402.06196v3"},{"title":"Contrastive Preference Optimization: Pushing the Boundaries of LLM Performance in Machine Translation","url":"https://arxiv.org/html/2401.08417v3"},{"title":"arXiv:2408.14134v3 [cs.LG] 15 Feb 2025","url":"http://shichuan.org/doc/192.pdf"},{"title":"Computer Science","url":"https://arxiv.org/list/cs/pastweek?skip=235&show=1000"},{"title":"arXiv:2408.12088v2 [cs.CY] 4 Feb 2025","url":"https://arxiv.org/pdf/2408.12088"}]

Based on the search results, here is the information about the arxiv paper 2408.13889:

**Title:** LLM with Relation Classifier for Document-Level Relation Extraction

**Full Author List:** Xingzuo Li, Kehai Chen, Yunfei Long, Min Zhang

**Method/Acronym:** LMRC (LLM with Relation Classifier)

**Submission Information:** Submitted on 25 Aug 2024 (v1), last revised 7 Dec 2024 (this version, v2)

However, the search results do not contain information about the specific venue or conference where this paper was accepted. The results show it is an arXiv preprint, but details about conference acceptance are not available in these sources.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_research_docre_methods_20260517T150401",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 33 · 2026-05-17T15:08:12.007453+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "LMRC \"LLM with Relation Classifier\" accepted AAAI EMNLP ACL 2025 Xingzuo Li"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_research_docre_methods_20260517T150401",
  "tool": "WebSearch",
  "tool_args": {
    "query": "LMRC \"LLM with Relation Classifier\" accepted AAAI EMNLP ACL 2025 Xingzuo Li"
  }
}
```

</details>

---

### Tool result

_source line 34 · 2026-05-17T15:08:12.007729+00:00_

Web search results for query: "LMRC "LLM with Relation Classifier" accepted AAAI EMNLP ACL 2025 Xingzuo Li"

Links: [{"title":"[Literature Review] LLM with Relation Classifier for Document-Level Relation Extraction","url":"https://www.themoonlight.io/en/review/llm-with-relation-classifier-for-document-level-relation-extraction"},{"title":"LLM with Relation Classifier for Document-Level Relation Extraction","url":"https://arxiv.org/html/2408.13889v2"},{"title":"LLM with Relation Classifier for Document-Level Relation Extraction","url":"https://openreview.net/pdf?id=SOWcC2cCMT"},{"title":"Accepted Main Conference Papers - ACL 2025","url":"https://2025.aclweb.org/program/main_papers/"},{"title":"The 2025 Conference on Empirical Methods in Natural Language Processing - ACL Anthology","url":"https://aclanthology.org/events/emnlp-2025/"},{"title":"LLM with Relation Classifier for Document-Level Relation Extraction | AI Research Paper Details","url":"https://www.aimodels.fyi/papers/arxiv/llm-relation-classifier-document-level-relation-extraction"},{"title":"Generation-Augmented Retrieval: Rethinking the Role of ...","url":"https://aclanthology.org/2025.findings-emnlp.974.pdf"},{"title":"Zhuosheng Zhang, Shanghai Jiao Tong University - BCMI Lab","url":"https://bcmi.sjtu.edu.cn/home/zhangzs/"},{"title":"BYOKG-RAG: Multi-Strategy Graph Retrieval for ...","url":"https://aclanthology.org/2025.emnlp-main.1417.pdf"},{"title":"Paper Digest: ACL 2025 Papers & Highlights – Paper Digest","url":"https://www.paperdigest.org/2025/07/acl-2025-papers-highlights/"}]

Based on the search results, I found information about the LMRC paper by Xingzuo Li and colleagues:

The paper presents a novel approach to document-level relation extraction (DocRE) by utilizing large language models (LLMs) structured around a composite method that integrates a relation classifier, authored by Xingzuo Li, Kehai Chen, Yunfei Long, and Min Zhang.

The method named LMRC (LLM with Relation Classifier) aims at bri
…[truncated 1144 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_research_docre_methods_20260517T150401",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 35 · 2026-05-17T15:08:12.008130+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "GenRES NAACL 2024 Pengcheng Jiang authors full venue proceedings"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_research_docre_methods_20260517T150401",
  "tool": "WebSearch",
  "tool_args": {
    "query": "GenRES NAACL 2024 Pengcheng Jiang authors full venue proceedings"
  }
}
```

</details>

---

### Tool result

_source line 36 · 2026-05-17T15:08:12.008438+00:00_

Web search results for query: "GenRES NAACL 2024 Pengcheng Jiang authors full venue proceedings"

Links: [{"title":"GenRES: Rethinking Evaluation for Generative Relation Extraction in the Era of Large Language Models - ACL Anthology","url":"https://aclanthology.org/2024.naacl-long.155/"},{"title":"Accepted Papers - NAACL-HLT 2024","url":"https://2024.naacl.org/program/accepted_papers/"},{"title":"GENRES: Rethinking Evaluation for Generative Relation Extraction in the Era of Large Language Models - Illinois Experts","url":"https://experts.illinois.edu/en/publications/genres-rethinking-evaluation-for-generative-relation-extraction-i/"},{"title":"Second Call for Main Conference Papers - NAACL-HLT 2024","url":"https://2024.naacl.org/calls/papers/"},{"title":"NAACL 2024 - Amazon Science","url":"https://www.amazon.science/conferences-and-events/naacl-2024"},{"title":"Paper Digest: NAACL 2024 Papers & Highlights – Resources | Paper Digest","url":"https://resources.paperdigest.org/2024/06/naacl-2024-highlights/"},{"title":"2024 Annual Conference of the North American Chapter of the Association for Computational Linguistics - NAACL-HLT 2024","url":"https://2024.naacl.org/"},{"title":"Nations of the Americas Chapter of the Association for Computational Linguistics - ACL Anthology","url":"https://aclanthology.org/venues/naacl/"},{"title":"NAACL 2024 The 2024 Conference of the North American ...","url":"https://aclanthology.org/2024.naacl-tutorials.pdf"},{"title":"First Call for Main Conference Papers - NAACL-HLT 2024","url":"https://2024.naacl.org/calls/first_call_for_papers/"}]

Based on the search results, here's the information about the GenRES paper at NAACL 2024:

**Paper Title:** GenRES: Rethinking Evaluation for Generative Relation Extraction in the Era of Large Language Models

**Authors:** Pengcheng Jiang, Jiacheng Lin, Zifeng Wang, Jimeng Sun, and Jiawei Han

**Venue & Proceedings:** Proceedings of the 2024 Conference of the North American Chapter of the Association 
…[truncated 463 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_research_docre_methods_20260517T150401",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 37 · 2026-05-17T15:08:12.008756+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "openreview.net \"DocKS-RAG\" SVl9tIADWV arxiv preprint"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_research_docre_methods_20260517T150401",
  "tool": "WebSearch",
  "tool_args": {
    "query": "openreview.net \"DocKS-RAG\" SVl9tIADWV arxiv preprint"
  }
}
```

</details>

---

### Tool result

_source line 38 · 2026-05-17T15:08:12.009016+00:00_

Web search results for query: "openreview.net "DocKS-RAG" SVl9tIADWV arxiv preprint"

Links: [{"title":"DocKS-RAG: Optimizing Document-Level Relation Extraction through LLM-Enhanced Hybrid Prompt Tuning | OpenReview","url":"https://openreview.net/forum?id=SVl9tIADWV"},{"title":"OpenReview Archive | OpenReview","url":"https://openreview.net/group?id=OpenReview.net%2FArchive"},{"title":"RankRAG: Unifying Context Ranking with Retrieval-Augmented Generation in LLMs","url":"https://openreview.net/pdf?id=S1fc92uemC"},{"title":"Venues | OpenReview","url":"https://openreview.net/"},{"title":"[2501.00309] Retrieval-Augmented Generation with Graphs (GraphRAG)","url":"https://arxiv.org/abs/2501.00309"},{"title":"000 001 002 003 004 005 006 007 008 009 010 011 012 013 014 015 016 017 018 019","url":"https://openreview.net/pdf/655bb056e30116388ec938c1db7ccd6ffdddec17.pdf"},{"title":"SELF-RAG: LEARNING TO RETRIEVE, GENERATE, AND ...","url":"https://openreview.net/pdf?id=hSyW5go0v8"},{"title":"Enhancing RAG Reasoning through Test-Time Critique ...","url":"https://openreview.net/pdf?id=cnUq7GkS6d"},{"title":"EnterpriseRAG-Bench: A RAG Benchmark for Company Internal Knowledge","url":"https://arxiv.org/html/2605.05253v1"},{"title":"A Survey of Graph Retrieval-Augmented Generation for ...","url":"https://openreview.net/pdf?id=9FJiOMuZkr"}]

I found the paper you were looking for. DocKS-RAG is a novel and effective framework which introduces extra structural knowledge and semantic information to further enhance the performance of document-level relation extraction.

More specifically, DocKS-RAG is a framework for document-level relation extraction that enhances structural and semantic understanding by integrating a Document-level Knowledge Graph and a Sentence-level Semantic Retrieval-Augmented Generation mechanism. Additionally, the framework designs a hybrid-prompt tuning method on large language models, and experiments on benchmark datasets show significant improvements over existin
…[truncated 228 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_research_docre_methods_20260517T150401",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 39 · 2026-05-17T15:08:12.011367+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"DocKS-RAG\" Xiaolong Xu arxiv.org 2024 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_research_docre_methods_20260517T150401",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"DocKS-RAG\" Xiaolong Xu arxiv.org 2024 2025"
  }
}
```

</details>

---

### Tool result

_source line 40 · 2026-05-17T15:08:12.011749+00:00_

Web search results for query: ""DocKS-RAG" Xiaolong Xu arxiv.org 2024 2025"

Links: [{"title":"privacy challenges and solutions in rag-enhanced llms for ...","url":"https://arxiv.org/pdf/2511.11347"},{"title":"A Survey of RAG-Reasoning Systems in LLMs","url":"https://arxiv.org/pdf/2507.09477"},{"title":"A Survey on Retrieval And Structuring Augmented Generation","url":"https://arxiv.org/pdf/2509.10697"},{"title":"Published as a conference paper at COLM 2025","url":"https://arxiv.org/pdf/2504.13079"},{"title":"RAGOps: Operating and Managing Retrieval-Augmented Generation Pipelines","url":"https://arxiv.org/html/2506.03401v1"},{"title":"Engineering the RAG Stack: A Comprehensive Review of the Architecture and Trust Frameworks for Retrieval Augmented Generation Systems","url":"https://arxiv.org/html/2601.05264v1"},{"title":"REFRAG: Rethinking RAG based Decoding","url":"https://arxiv.org/pdf/2509.01092"},{"title":"Artificial Intelligence 2025","url":"https://www.arxiv.org/list/cs.AI/2025?skip=23750&show=2000"},{"title":"[2410.12837] A Comprehensive Survey of Retrieval-Augmented Generation (RAG): Evolution, Current Landscape and Future Directions","url":"https://arxiv.org/abs/2410.12837"},{"title":"Advancements in RAG [Retrieval-Augmented Generation] Systems by Mid-2025 | by Martinagrafsvw | Medium","url":"https://medium.com/@martinagrafsvw25/advancements-in-rag-retrieval-augmented-generation-systems-by-mid-2025-935a39c15ae9"}]

Based on my web search results, I found a reference to work by Xiaolong Xu related to RAG systems. Xu et al. leverage knowledge graphs for retrieval by parsing issue tickets into tree structures with interconnected relationships, then using entity matching and graph traversal to locate relevant information instead of relying on text-chunk similarity search.

However, I did not find a specific paper titled "DocKS-RAG" by Xiaolong Xu in the search results. The search returned various RAG-related papers from 2024-2025, but this particular paper titl
…[truncated 597 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_research_docre_methods_20260517T150401",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 41 · 2026-05-17T15:08:12.012029+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "DREEAM document-level relation extraction 2023 2024 arxiv Ma et al"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_research_docre_methods_20260517T150401",
  "tool": "WebSearch",
  "tool_args": {
    "query": "DREEAM document-level relation extraction 2023 2024 arxiv Ma et al"
  }
}
```

</details>

---

### Tool result

_source line 42 · 2026-05-17T15:08:12.012343+00:00_

Web search results for query: "DREEAM document-level relation extraction 2023 2024 arxiv Ma et al"

Links: [{"title":"[2302.08675] DREEAM: Guiding Attention with Evidence for Improving Document-Level Relation Extraction","url":"https://arxiv.org/abs/2302.08675"},{"title":"DREEAM: Guiding Attention with Evidence for Improving Document-Level Relation Extraction - ACL Anthology","url":"https://aclanthology.org/2023.eacl-main.145/"},{"title":"DREEAM: Guiding Attention with Evidence for Improving Document-Level Relation Extraction","url":"https://www.researchgate.net/publication/373811777_DREEAM_Guiding_Attention_with_Evidence_for_Improving_Document-Level_Relation_Extraction"},{"title":"Three-stage document-level entity relation extraction | The Journal of Supercomputing | Springer Nature Link","url":"https://link.springer.com/article/10.1007/s11227-025-07068-2"},{"title":"GLiDRE: Generalist Lightweight model for Document-level Relation Extraction","url":"https://arxiv.org/html/2508.00757v1"},{"title":"Augmenting Document-level Relation Extraction with Efficient Multi-Supervision","url":"https://arxiv.org/html/2407.01026v1"},{"title":"GitHub - YoumiMa/dreeam: source code for {D}ocument-level {R}elation {E}xtraction with {E}vidence-guided {A}ttention {M}echanism · GitHub","url":"https://github.com/YoumiMa/dreeam"},{"title":"LLM with Relation Classifier for Document-Level Relation Extraction","url":"https://arxiv.org/html/2408.13889v1"},{"title":"[PDF] DREEAM: Guiding Attention with Evidence for Improving Document-Level Relation Extraction | Semantic Scholar","url":"https://www.semanticscholar.org/paper/DREEAM:-Guiding-Attention-with-Evidence-for-Ma-Wang/51237757750c4618bf114ff329dacb9c997b771a"},{"title":"Evidence and Axial Attention Guided Document-level Relation Extraction | Computer Speech and Language","url":"https://dl.acm.org/doi/10.1016/j.csl.2024.101728"}]

I found the paper you were looking for! Here are the key details:

DREEAM: Guiding Attention with Evidence f
…[truncated 1402 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_research_docre_methods_20260517T150401",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 43 · 2026-05-17T15:08:12.012619+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "GLiDRE \"Generalist Lightweight model for Document-level Relation Extraction\" 2025 arxiv"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_research_docre_methods_20260517T150401",
  "tool": "WebSearch",
  "tool_args": {
    "query": "GLiDRE \"Generalist Lightweight model for Document-level Relation Extraction\" 2025 arxiv"
  }
}
```

</details>

---

### Tool result

_source line 44 · 2026-05-17T15:08:12.012912+00:00_

Web search results for query: "GLiDRE "Generalist Lightweight model for Document-level Relation Extraction" 2025 arxiv"

Links: [{"title":"[2508.00757] GLiDRE: Generalist Lightweight model for Document-level Relation Extraction","url":"https://arxiv.org/abs/2508.00757"},{"title":"GLiDRE: Generalist Lightweight model for Document-level Relation Extraction","url":"https://arxiv.org/html/2508.00757v2"},{"title":"GLiDRE: Generalist Lightweight model for Document-level Relation Extraction - ADS","url":"https://ui.adsabs.harvard.edu/abs/2025arXiv250800757A/abstract"},{"title":"GitHub - robinarmingaud/glidre: Zero and Few-shot document level relation extraction / ⚠️ Development moved to: https://github.com/cea-list-lasti/glidre","url":"https://github.com/robinarmingaud/glidre"},{"title":"(PDF) GLiDRE: Generalist Lightweight model for Document-level Relation Extraction","url":"https://www.researchgate.net/publication/394262622_GLiDRE_Generalist_Lightweight_model_for_Document-level_Relation_Extraction"},{"title":"GLiClass: Generalist Lightweight Model for Sequence Classification Tasks","url":"https://arxiv.org/html/2508.07662v1"},{"title":"Paper page - GLiClass: Generalist Lightweight Model for Sequence Classification Tasks","url":"https://huggingface.co/papers/2508.07662"},{"title":"(PDF) GLiClass: Generalist Lightweight Model for Sequence Classification Tasks","url":"https://www.researchgate.net/publication/394439683_GLiClass_Generalist_Lightweight_Model_for_Sequence_Classification_Tasks"},{"title":"GLiNER2: An Efficient Multi-Task Information Extraction System with Schema-Driven Interface","url":"https://arxiv.org/html/2507.18546v1"},{"title":"GitHub - jackboyla/GLiREL: Generalist and Lightweight Model for Relation Extraction (Extract any relationship types from text) · GitHub","url":"https://github.com/jackboyla/GLiREL"}]

I found the paper you were looking for! Here's what I found about GLiDRE:

## Paper Details

GLiDRE: Generalist Lightweight model for Document-level R
…[truncated 1144 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_research_docre_methods_20260517T150401",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 45 · 2026-05-17T15:08:12.014373+00:00_

Now I have all the information needed. Here are the results:

---

```
VERIFICATION RESULTS:

1. DocRED: ✅ VERIFIED
   Title: "DocRED: A Large-Scale Document-Level Relation Extraction Dataset"
   Authors: Yuan Yao, Deming Ye, Peng Li, Xu Han, Yankai Lin, Zhenghao Liu, Zhiyuan Liu, Lixin Huang, Jie Zhou, Maosong Sun
   Venue: ACL 2019 (P19-1074)
   arXiv: 1906.06127
   ACL Anthology: https://aclanthology.org/P19-1074/

2. Re-DocRED: ✅ VERIFIED
   Title: "Revisiting DocRED -- Addressing the False Negative Problem in Relation Extraction"
   Authors: Qingyu Tan, Lu Xu, Lidong Bing, Hwee Tou Ng
   Venue: EMNLP 2022 (2022.emnlp-main.580)
   arXiv: 2205.12696
   ACL Anthology: https://aclanthology.org/2022.emnlp-main.580/

3. ATLOP: ✅ VERIFIED
   Title: "Document-Level Relation Extraction with Adaptive Thresholding and Localized Context Pooling"
   Authors: Wenxuan Zhou, Kevin Huang, Tengyu Ma, Jing Huang
   Venue: AAAI 2021
   arXiv: 2010.11304
   DOI: 10.1609/aaai.v35i16.17717

4. LMRC: ✅ VERIFIED (年份需修正)
   Title: "LLM with Relation Classifier for Document-Level Relation Extraction"
   Authors: Xingzuo Li, Kehai Chen, Yunfei Long, Min Zhang
   Venue: arXiv preprint (未确认正式会议录用)
   arXiv: 2408.13889
   ⚠️ 注意: 原始记录标注 "Li et al., 2023" 有误，arXiv 提交日期为 2024年8月，应修正为 2024

5. DocKS-RAG: ✅ VERIFIED (venue需修正)
   Title: "DocKS-RAG: Optimizing Document-Level Relation Extraction through LLM-Enhanced Hybrid Prompt Tuning"
   Authors: Xiaolong Xu, Yibo Zhou, Haolong Xiang, Xiaoyong Li, Xuyun Zhang, Lianyong Qi, Wanchun Dou
   Venue: ICML 2025 (Proceedings of Machine Learning Research vol. 267)
   arXiv: ❌ 未找到 arXiv ID（论文通过 OpenReview 提交，ID: SVl9tIADWV）
   PMLR: https://proceedings.mlr.press/v267/xu25am.html
   ⚠️ 注意: 原始记录标注 "Xu et al., 2024"，实际发表于 ICML 2025。无 arXiv preprint。

6. GenRES: ✅ VERIFIED
   Title: "GenRES: Rethinking Evaluation for Generative Relation Extraction in the Era of Large Language Models"
   Authors: Pengcheng Jiang, Jiacheng Lin, Zifeng Wang, Jimeng Sun, Jiawei Han
   Venue: NAACL 2024 (Long Papers, pages 2820-2837)
   arXiv: 2402.10744
   ACL Anthology: https://aclanthology.org/2024.naacl-long.155/
   DOI: 10.18653/v1/2024.naacl-long.155


GAP-FILL (建议补充的论文):

- [docunet] "Document-level Relation Extraction as Semantic Segmentation"
  Authors: Ningyu Zhang, Xiang Chen, Xin Xie, Shumin Deng, Chuanqi Tan, Mosha Chen, Fei Huang, Luo Si, Huajun Chen
  Venue: IJCAI 2021 | arXiv: 2106.03618

- [kd_docre] "Document-Level Relation Extraction with Adaptive Focal Loss and Knowledge Distillation"
  Authors: Qingyu Tan, Ruidan He, Lidong Bing, Hwee Tou Ng
  Venue: Findings of ACL 2022 | arXiv: 2203.10900

- [dreeam] "DREEAM: Guiding Attention with Evidence for Improving Document-Level Relation Extraction"
  Authors: Youmi Ma, An Wang, Naoaki Okazaki
  Venue: EACL 2023 | arXiv: 2302.08675
  备注: 当前 DocRE SOTA 之一，与本项目 evidence-guided 主题高度相关

- [autore] "AutoRE: Document-Level Relation Extraction with Large Language Models"
  Authors: Lilong Xue, Dan Zhang, Yuxiao Dong, Jie Tang
  Venue: ACL 2024 Demo | arXiv: 2403.14888
  备注: LLM-based DocRE 代表性工作，RHF 范式，在 Re-DocRED 上 SOTA


ISSUES SUMMARY:
- LMRC: 年份从 2023 修正为 2024
- DocKS-RAG: 无 arXiv ID（仅 OpenReview + ICML 2025 proceedings），venue 从 2024 修正为 2025
- 无 FAKE 论文，6 篇全部真实存在
```

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_paper_research_docre_methods_20260517T150401"
}
```

</details>

---
