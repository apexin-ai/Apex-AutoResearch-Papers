# paper research evidence docre

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 41
- **Recorded user turns:** 0
- **Tool calls:** 20
- **Original source:** `logs/chats/worker_paper_research_evidence_docre_20260517T152414.jsonl`
- **Structured JSON:** [`3e60ccc8ab6c8f5a68c2.json`](../../sessions/3e/3e60ccc8ab6c8f5a68c2.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

41 recorded events

### Tool call

_source line 1 · 2026-05-17T15:26:55.112153+00:00_

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
  "session": "worker_paper_research_evidence_docre_20260517T152414",
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

_source line 2 · 2026-05-17T15:26:55.112704+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_research_evidence_docre_20260517T152414",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-17T15:26:55.113018+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "DREEAM \"Guiding Attention with Evidence for Improving Document-Level Relation Extraction\" site:arxiv.org"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_research_evidence_docre_20260517T152414",
  "tool": "WebSearch",
  "tool_args": {
    "query": "DREEAM \"Guiding Attention with Evidence for Improving Document-Level Relation Extraction\" site:arxiv.org"
  }
}
```

</details>

---

### Tool call

_source line 4 · 2026-05-17T15:26:55.113249+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "SAIS \"Supervising and Augmenting Intermediate Steps for Document-Level Relation Extraction\" site:aclanthology.org"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_research_evidence_docre_20260517T152414",
  "tool": "WebSearch",
  "tool_args": {
    "query": "SAIS \"Supervising and Augmenting Intermediate Steps for Document-Level Relation Extraction\" site:aclanthology.org"
  }
}
```

</details>

---

### Tool result

_source line 5 · 2026-05-17T15:26:55.113491+00:00_

Web search results for query: "SAIS "Supervising and Augmenting Intermediate Steps for Document-Level Relation Extraction" site:aclanthology.org"

Links: [{"title":"SAIS: Supervising and Augmenting Intermediate Steps for Document-Level Relation Extraction - ACL Anthology","url":"https://aclanthology.org/2022.naacl-main.171/"}]

Perfect! I found the paper. Here are the results:

**SAIS: Supervising and Augmenting Intermediate Steps for Document-Level Relation Extraction** by Yuxin Xiao, Zecheng Zhang, Yuning Mao, Carl Yang, and Jiawei Han was published in 2022 in the Proceedings of the 2022 Conference of the North American Chapter of the Association for Computational Linguistics (NAACL).

The paper proposes to explicitly teach the model to capture relevant contexts and entity types by supervising and augmenting intermediate steps (SAIS) for relation extraction, which not only extracts relations of better quality due to more effective supervision, but also retrieves the corresponding supporting evidence more accurately. By assessing model uncertainty, SAIS further boosts the performance via evidence-based data augmentation and ensemble inference while reducing the computational cost.

The full paper is available at: https://aclanthology.org/2022.naacl-main.171/


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_research_evidence_docre_20260517T152414",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-17T15:26:55.113755+00:00_

Web search results for query: "DREEAM "Guiding Attention with Evidence for Improving Document-Level Relation Extraction" site:arxiv.org"

Links: [{"title":"[2302.08675] DREEAM: Guiding Attention with Evidence for Improving Document-Level Relation Extraction","url":"https://arxiv.org/abs/2302.08675"},{"title":"GEGA: Graph Convolutional Networks and Evidence Retrieval Guided Attention for Enhanced Document-level Relation Extraction","url":"https://arxiv.org/html/2407.21384v1"},{"title":"GLiDRE: Generalist Lightweight model for Document-level Relation Extraction","url":"https://arxiv.org/html/2508.00757v2"},{"title":"TTM-RE: Memory-Augmented Document-Level Relation Extraction","url":"https://arxiv.org/html/2406.05906v1"},{"title":"LLM with Relation Classifier for Document-Level Relation Extraction","url":"https://arxiv.org/html/2408.13889v1"},{"title":"A LayoutLMv3-Based Model for Enhanced Relation Extraction in Visually-Rich Documents","url":"https://arxiv.org/html/2404.10848v1"},{"title":"Building a Japanese Document-Level Relation Extraction Dataset Assisted by Cross-Lingual Transfer","url":"https://arxiv.org/html/2404.16506"},{"title":"CDER: Collaborative Evidence Retrieval for Document-level Relation Extraction","url":"https://arxiv.org/html/2504.06529"},{"title":"WISTERIA: Weak Implicit Signal-based Temporal Relation Extraction with Attention","url":"https://arxiv.org/html/2603.23319"},{"title":"Augmenting Document-level Relation Extraction with Efficient Multi-Supervision","url":"https://arxiv.org/html/2407.01026v1"}]

I found the paper! Here are the search results for DREEAM:

DREEAM is a memory-efficient approach that adopts evidence information as the supervisory signal, thereby guiding the attention modules of the DocRE system to assign high weights to evidence.

The paper is titled "DREEAM: Guiding Attention with Evidence for Improving Document-Level Relation Extraction" by Youmi Ma and 2 other authors.

**Key Details:**
- **Paper ID:** arXiv:2302.08675
- *
…[truncated 478 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_research_evidence_docre_20260517T152414",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-17T15:26:55.114047+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "DREEAM \"Youmi Ma\" EACL 2023 document relation extraction"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_research_evidence_docre_20260517T152414",
  "tool": "WebSearch",
  "tool_args": {
    "query": "DREEAM \"Youmi Ma\" EACL 2023 document relation extraction"
  }
}
```

</details>

---

### Tool call

_source line 8 · 2026-05-17T15:26:55.114272+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "SAIS Xiao NAACL 2022 arxiv document relation extraction"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_research_evidence_docre_20260517T152414",
  "tool": "WebSearch",
  "tool_args": {
    "query": "SAIS Xiao NAACL 2022 arxiv document relation extraction"
  }
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-17T15:26:55.114482+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "EACL 2023 DREEAM \"Youmi Ma\" site:aclanthology.org"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_research_evidence_docre_20260517T152414",
  "tool": "WebSearch",
  "tool_args": {
    "query": "EACL 2023 DREEAM \"Youmi Ma\" site:aclanthology.org"
  }
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-17T15:26:55.114738+00:00_

Web search results for query: "DREEAM "Youmi Ma" EACL 2023 document relation extraction"

Links: [{"title":"DREEAM: Guiding Attention with Evidence for Improving Document-Level Relation Extraction - ACL Anthology","url":"https://aclanthology.org/2023.eacl-main.145/"},{"title":"GitHub - YoumiMa/dreeam: source code for {D}ocument-level {R}elation {E}xtraction with {E}vidence-guided {A}ttention {M}echanism · GitHub","url":"https://github.com/YoumiMa/dreeam"},{"title":"DREEAM: Guiding Attention with Evidence for Improving ...","url":"https://aclanthology.org/2023.eacl-main.145.pdf"},{"title":"dreeam/README.md at main · YoumiMa/dreeam","url":"https://github.com/YoumiMa/dreeam/blob/main/README.md"},{"title":"DREEAM: Guiding Attention with Evidence for Improving Document-Level Relation Extraction","url":"https://www.researchgate.net/publication/373811777_DREEAM_Guiding_Attention_with_Evidence_for_Improving_Document-Level_Relation_Extraction"},{"title":"Youmi Ma","url":"https://www.catalyzex.com/author/Youmi%20Ma"},{"title":"dblp: Youmi Ma","url":"https://dblp.org/pid/268/1357.html"},{"title":"(PDF) Until the Completion of “Incorporating Evidence Retrieval into Document-Level Relation Extraction”「文書レベル関係抽出における根拠認識の統合」の完成まで","url":"https://www.researchgate.net/publication/373932566_Until_the_Completion_of_Incorporating_Evidence_Retrieval_into_Document-Level_Relation_Extractionwenshureberuguanxichouchuniokerugenjurenshinotonghenowanchengmade"},{"title":"[2302.08675] DREEAM: Guiding Attention with Evidence for Improving Document-Level Relation Extraction","url":"https://arxiv.org/abs/2302.08675"},{"title":"Main Conference Accepted Papers - EACL 2023","url":"https://2023.eacl.org/program/accepted/"}]

I found comprehensive information about the DREEAM paper. Here are the key details:

## Paper Overview

DREEAM: Guiding Attention with Evidence for Improving Document-Level Relation Extraction is authored by Youmi Ma, An Wang, and Naoaki Okazaki and was published at EACL 2023.

##
…[truncated 1290 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_research_evidence_docre_20260517T152414",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 11 · 2026-05-17T15:26:55.115011+00:00_

Web search results for query: "SAIS Xiao NAACL 2022 arxiv document relation extraction"

Links: [{"title":"SAIS: Supervising and Augmenting Intermediate Steps for Document-Level Relation Extraction - ACL Anthology","url":"https://aclanthology.org/2022.naacl-main.171/"},{"title":"GitHub - xiaoyuxin1002/SAIS: SAIS: Supervising and Augmenting Intermediate Steps for Document-Level Relation Extraction","url":"https://github.com/xiaoyuxin1002/SAIS"},{"title":"[2109.12093] SAIS: Supervising and Augmenting Intermediate Steps for Document-Level Relation Extraction","url":"https://arxiv.org/abs/2109.12093"},{"title":"A survey on cutting-edge relation extraction techniques based on language models | Artificial Intelligence Review | Springer Nature Link","url":"https://link.springer.com/article/10.1007/s10462-025-11280-0"},{"title":"Rethinking Document-Level Relation Extraction: A Reality Check","url":"https://arxiv.org/html/2306.08953"},{"title":"A survey on cutting-edge relation extraction techniques based on language models","url":"https://arxiv.org/html/2411.18157v1"},{"title":"SAIS: Supervising and Augmenting Intermediate Steps for ...","url":"https://aclanthology.org/2022.naacl-main.171.pdf"},{"title":"document-level in-context few-shot relation extraction via ...","url":"https://arxiv.org/pdf/2310.11085"},{"title":"Document-Level Relation Extraction Based on Fine-Grained Information Guidance | Advanced Intelligent Computing Technology and Applications","url":"https://dl.acm.org/doi/10.1007/978-981-97-5669-8_31"},{"title":"Few-Shot Document-Level Relation Extraction","url":"https://aclanthology.org/anthology-files/pdf/naacl/2022.naacl-main.421.pdf"}]

I found comprehensive information about the SAIS paper. Here's what I discovered:

SAIS: Supervising and Augmenting Intermediate Steps for Document-Level Relation Extraction is a paper by Yuxin Xiao, Zecheng Zhang, Yuning Mao, Carl Yang, and Jiawei Han, published at NAACL 2022. The paper is also available on arXiv as arXiv:2
…[truncated 1124 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_research_evidence_docre_20260517T152414",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-17T15:26:55.115316+00:00_

Web search results for query: "EACL 2023 DREEAM "Youmi Ma" site:aclanthology.org"

Links: [{"title":"DREEAM: Guiding Attention with Evidence for Improving Document-Level Relation Extraction - ACL Anthology","url":"https://aclanthology.org/2023.eacl-main.145/"},{"title":"DREEAM: Guiding Attention with Evidence for Improving ...","url":"https://aclanthology.org/2023.eacl-main.145.pdf"},{"title":"Youmi Ma - ACL Anthology","url":"https://aclanthology.org/people/y/youmi-ma/"},{"title":"Improving Cross-Lingual Transfer for Open Information Extraction with Linguistic Feature Projection - ACL Anthology","url":"https://aclanthology.org/2023.mrl-1.11/"},{"title":"Generative Data Augmentation for Aspect Sentiment Quad Prediction - ACL Anthology","url":"https://aclanthology.org/2023.starsem-1.12/"},{"title":"Proceedings of the 3rd Workshop on Multi-lingual Representation Learning (MRL) - ACL Anthology","url":"https://aclanthology.org/volumes/2023.mrl-1/"},{"title":"EACL 2026 The 19th Conference of the European Chapter of the","url":"https://aclanthology.org/2026.eacl-short.0.pdf"}]

The search returned results about the paper "DREEAM: Guiding Attention with Evidence for Improving Document-Level Relation Extraction" from EACL 2023 with Youmi Ma as an author.

Here are the key findings:

## Paper Details

The paper "DREEAM: Guiding Attention with Evidence for Improving Document-Level Relation Extraction" was authored by Youmi Ma, An Wang, and Naoaki Okazaki and presented at EACL 2023.

## Paper Content

Document-level relation extraction (DocRE) is the task of identifying all relations between each entity pair in a document. Evidence, defined as sentences containing clues for the relationship between an entity pair, has been shown to help DocRE systems focus on relevant texts, thus improving relation extraction.

## Key Contribution

DREEAM is a memory-efficient approach that adopts evidence information as the supervisory signal, thereby guiding the attention modules of the DocRE
…[truncated 467 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_research_evidence_docre_20260517T152414",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-17T15:26:55.115607+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "GEGA \"Graph Convolutional Networks and Evidence Retrieval Guided Attention\" document relation extraction arxiv"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_research_evidence_docre_20260517T152414",
  "tool": "WebSearch",
  "tool_args": {
    "query": "GEGA \"Graph Convolutional Networks and Evidence Retrieval Guided Attention\" document relation extraction arxiv"
  }
}
```

</details>

---

### Tool call

_source line 14 · 2026-05-17T15:26:55.115812+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "DocGNRE \"document-level relation extraction\" evidence generation arxiv"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_research_evidence_docre_20260517T152414",
  "tool": "WebSearch",
  "tool_args": {
    "query": "DocGNRE \"document-level relation extraction\" evidence generation arxiv"
  }
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-17T15:26:55.116008+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "CDER \"Collaborative Evidence Retrieval\" document-level relation extraction arxiv"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_research_evidence_docre_20260517T152414",
  "tool": "WebSearch",
  "tool_args": {
    "query": "CDER \"Collaborative Evidence Retrieval\" document-level relation extraction arxiv"
  }
}
```

</details>

---

### Tool call

_source line 16 · 2026-05-17T15:26:55.116199+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "ERID \"Evidence Retrieval for Document-Level Relation Extraction\" arxiv OR aclanthology"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_research_evidence_docre_20260517T152414",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ERID \"Evidence Retrieval for Document-Level Relation Extraction\" arxiv OR aclanthology"
  }
}
```

</details>

---

### Tool result

_source line 17 · 2026-05-17T15:26:55.116482+00:00_

Web search results for query: "GEGA "Graph Convolutional Networks and Evidence Retrieval Guided Attention" document relation extraction arxiv"

Links: [{"title":"[2407.21384] GEGA: Graph Convolutional Networks and Evidence Retrieval Guided Attention for Enhanced Document-level Relation Extraction","url":"https://arxiv.org/abs/2407.21384"},{"title":"GEGA: Graph Convolutional Networks and Evidence Retrieval Guided Attention for Enhanced Document-level Relation Extraction","url":"https://arxiv.org/html/2407.21384v1"},{"title":"GEGA: Graph Convolutional Networks and Evidence Retrieval Guided Attention for Enhanced Document-level Relation Extraction | IEEE Conference Publication | IEEE Xplore","url":"https://ieeexplore.ieee.org/document/10889649/"},{"title":"GEGA: Graph Convolutional Networks and Evidence Retrieval Guided Attention for Enhanced Document-level Relation Extraction | OpenReview","url":"https://openreview.net/forum?id=oUMKv7Nlav"},{"title":"[1906.07510] Attention Guided Graph Convolutional Networks for Relation Extraction","url":"https://arxiv.org/abs/1906.07510"},{"title":"Revisiting Document-Level Relation Extraction with Context-Guided Link Prediction","url":"https://www.emergentmind.com/papers/2401.11800"},{"title":"GitHub - Cartus/AGGCN: Attention Guided Graph Convolutional Networks for Relation Extraction (authors' PyTorch implementation for the ACL19 paper) · GitHub","url":"https://github.com/Cartus/AGGCN"},{"title":"Attention Guided Graph Convolutional Networks for Relation Extraction","url":"https://arxiv.org/pdf/1906.07510"},{"title":"Document-level relation extraction model guided by global information and external contextual knowledge | The Journal of Supercomputing | Springer Nature Link","url":"https://link.springer.com/article/10.1007/s11227-025-07467-5"},{"title":"(PDF) Attention Guided Graph Convolutional Networks for Relation Extraction","url":"https://www.researchgate.net/publication/333865746_Attention_Guided_Graph_Convolutional_Networks_
…[truncated 1536 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_research_evidence_docre_20260517T152414",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-17T15:26:55.116783+00:00_

Web search results for query: "CDER "Collaborative Evidence Retrieval" document-level relation extraction arxiv"

Links: [{"title":"[2504.06529] CDER: Collaborative Evidence Retrieval for Document-level Relation Extraction","url":"https://arxiv.org/abs/2504.06529"},{"title":"CDER: Collaborative Evidence Retrieval for Document-level Relation Extraction","url":"https://arxiv.org/html/2504.06529"},{"title":"CDER: Collaborative Evidence Retrieval for Document-Level Relation Extraction | Springer Nature Link","url":"https://link.springer.com/chapter/10.1007/978-981-97-4982-9_3"},{"title":"[PDF] CDER: Collaborative Evidence Retrieval for Document-Level Relation Extraction | Semantic Scholar","url":"https://www.semanticscholar.org/paper/CDER:-Collaborative-Evidence-Retrieval-for-Relation-Tran-Li/07f36e6f29c07f0edce7465f4d005bd34ac659ce"},{"title":"(PDF) CDER: Collaborative Evidence Retrieval for Document-level Relation Extraction","url":"https://www.researchgate.net/publication/390638674_CDER_Collaborative_Evidence_Retrieval_for_Document-level_Relation_Extraction"},{"title":"CDER: Collaborative Evidence Retrieval for Document- ...","url":"https://www.researchgate.net/publication/382280635_CDER_Collaborative_Evidence_Retrieval_for_Document-Level_Relation_Extraction"},{"title":"open source AI","url":"https://bytez.com/docs/arxiv/2504.06529/paper"},{"title":"CDER: Collaborative evidence retrieval for document-level ...","url":"https://espace.library.uq.edu.au/view/UQ:f699039"},{"title":"CDER: Collaborative Evidence Retrieval for Document-level ...","url":"https://ui.adsabs.harvard.edu/abs/arXiv:2504.06529"},{"title":"publications | Khai Tran - GitHub Pages","url":"https://khaitran22.github.io/publications/"}]

I found the paper you're looking for! Here are the key details:

## CDER: Collaborative Evidence Retrieval for Document-level Relation Extraction

**Paper Location:** arxiv.org/abs/2504.06529 (published April 9, 2025)

**Authors:** Khai Phan Tran and Xue Li

**Overview:
…[truncated 1323 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_research_evidence_docre_20260517T152414",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 19 · 2026-05-17T15:26:55.117100+00:00_

Web search results for query: "ERID "Evidence Retrieval for Document-Level Relation Extraction" arxiv OR aclanthology"

Links: [{"title":"EIDER: Empowering Document-level Relation Extraction ...","url":"https://aclanthology.org/2022.findings-acl.23.pdf"},{"title":"Eider: Empowering Document-level Relation Extraction with Efficient Evidence Extraction and Inference-stage Fusion - ACL Anthology","url":"https://aclanthology.org/2022.findings-acl.23/"},{"title":"CDER: Collaborative Evidence Retrieval for Document-level Relation Extraction","url":"https://arxiv.org/html/2504.06529"},{"title":"DREEAM: Guiding Attention with Evidence for Improving Document-Level Relation Extraction - ACL Anthology","url":"https://aclanthology.org/2023.eacl-main.145/"},{"title":"A survey on cutting-edge relation extraction techniques based on language models","url":"https://arxiv.org/html/2411.18157v1"},{"title":"Entity and Evidence Guided Document-Level Relation Extraction - ACL Anthology","url":"https://aclanthology.org/2021.repl4nlp-1.30/"},{"title":"[2106.08657] Eider: Empowering Document-level Relation Extraction with Efficient Evidence Extraction and Inference-stage Fusion","url":"https://arxiv.org/abs/2106.08657"},{"title":"DocRED: A Large-Scale Document-Level Relation Extraction Dataset - ACL Anthology","url":"https://aclanthology.org/P19-1074/"},{"title":"[2303.03912] Document-level Relation Extraction with Cross-sentence Reasoning Graph","url":"https://arxiv.org/abs/2303.03912"},{"title":"A Comprehensive Survey on Document-Level Information ...","url":"https://aclanthology.org/2024.futured-1.6.pdf"}]

Based on the search results, I found several papers related to evidence retrieval for document-level relation extraction, though I did not find a paper specifically titled "ERID: Evidence Retrieval for Document-Level Relation Extraction."

The search results show related work in this area:

1. **EIDER** - Eider is an evidence-enhanced framework that empowers DocRE by efficiently extr
…[truncated 1125 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_research_evidence_docre_20260517T152414",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-17T15:26:55.117416+00:00_

Web search results for query: "DocGNRE "document-level relation extraction" evidence generation arxiv"

Links: [{"title":"[2106.08657] Eider: Empowering Document-level Relation Extraction with Efficient Evidence Extraction and Inference-stage Fusion","url":"https://arxiv.org/abs/2106.08657"},{"title":"[2302.08675] DREEAM: Guiding Attention with Evidence for Improving Document-Level Relation Extraction","url":"https://arxiv.org/abs/2302.08675"},{"title":"Document-Level Relation Extraction with Relation Correlation Enhancement","url":"https://arxiv.org/html/2310.13000"},{"title":"A Comprehensive Survey of Document-level Relation Extraction (2016-2023)","url":"https://web3.arxiv.org/pdf/2309.16396v2"},{"title":"GEGA: Graph Convolutional Networks and Evidence Retrieval Guided Attention for Enhanced Document-level Relation Extraction","url":"https://arxiv.org/html/2407.21384"},{"title":"CDER: Collaborative Evidence Retrieval for Document-level Relation Extraction","url":"https://arxiv.org/html/2504.06529"},{"title":"[2407.21384] GEGA: Graph Convolutional Networks and Evidence Retrieval Guided Attention for Enhanced Document-level Relation Extraction","url":"https://arxiv.org/abs/2407.21384"},{"title":"[2008.12283] Entity and Evidence Guided Relation Extraction for DocRED","url":"https://arxiv.org/abs/2008.12283"},{"title":"[2204.12679] Document-Level Relation Extraction with Sentences Importance Estimation and Focusing","url":"https://arxiv.org/abs/2204.12679"},{"title":"Consistent Document-Level Relation Extraction via Counterfactuals","url":"https://arxiv.org/html/2407.06699v2"}]

Based on the search results, I found several relevant papers on document-level relation extraction with evidence generation on arXiv. Here are the key findings:

## Main Results

The search didn't return a specific paper titled "DocGNRE" with that exact name, but it did reveal several closely related papers on document-level relation extraction (DocRE) with evidence generation:

### Key Paper
…[truncated 1471 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_research_evidence_docre_20260517T152414",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool call

_source line 21 · 2026-05-17T15:26:55.117714+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "EIDER \"Empowering Document-level Relation Extraction with Efficient Evidence Extraction\" Xie ACL 2022"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_research_evidence_docre_20260517T152414",
  "tool": "WebSearch",
  "tool_args": {
    "query": "EIDER \"Empowering Document-level Relation Extraction with Efficient Evidence Extraction\" Xie ACL 2022"
  }
}
```

</details>

---

### Tool call

_source line 22 · 2026-05-17T15:26:55.117914+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "DocGNRE \"document relation extraction\" evidence generation natural language explanation"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_research_evidence_docre_20260517T152414",
  "tool": "WebSearch",
  "tool_args": {
    "query": "DocGNRE \"document relation extraction\" evidence generation natural language explanation"
  }
}
```

</details>

---

### Tool call

_source line 23 · 2026-05-17T15:26:55.118097+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "COREX document-level relation extraction evidence arxiv aclanthology"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_research_evidence_docre_20260517T152414",
  "tool": "WebSearch",
  "tool_args": {
    "query": "COREX document-level relation extraction evidence arxiv aclanthology"
  }
}
```

</details>

---

### Tool call

_source line 24 · 2026-05-17T15:26:55.118309+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"Entity and Evidence Guided Relation Extraction for DocRED\" arxiv 2008.12283"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_research_evidence_docre_20260517T152414",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"Entity and Evidence Guided Relation Extraction for DocRED\" arxiv 2008.12283"
  }
}
```

</details>

---

### Tool result

_source line 25 · 2026-05-17T15:26:55.118572+00:00_

Web search results for query: "EIDER "Empowering Document-level Relation Extraction with Efficient Evidence Extraction" Xie ACL 2022"

Links: [{"title":"Eider: Empowering Document-level Relation Extraction with Efficient Evidence Extraction and Inference-stage Fusion - ACL Anthology","url":"https://aclanthology.org/2022.findings-acl.23/"},{"title":"EIDER: Empowering Document-level Relation Extraction ...","url":"https://aclanthology.org/2022.findings-acl.23.pdf"},{"title":"[2106.08657] Eider: Empowering Document-level Relation Extraction with Efficient Evidence Extraction and Inference-stage Fusion","url":"https://arxiv.org/abs/2106.08657"},{"title":"GitHub - yiqingxyq/Eider: Source code for paper \"EIDER: Empowering Document-level Relation Extraction with Efficient Evidence Extraction and Inference-stage Fusion\", ACL Findings, 2022","url":"https://github.com/yiqingxyq/Eider"},{"title":"[PDF] Eider: Empowering Document-level Relation Extraction with Efficient Evidence Extraction and Inference-stage Fusion | Semantic Scholar","url":"https://www.semanticscholar.org/paper/dbf1e5a17b3adead7016eb52ddc3007673ed382f"},{"title":"Eider: Empowering Document-level Relation Extraction with Efficient Evidence Extraction and Inference-stage Fusion | Request PDF","url":"https://www.researchgate.net/publication/361056993_Eider_Empowering_Document-level_Relation_Extraction_with_Efficient_Evidence_Extraction_and_Inference-stage_Fusion"},{"title":"EIDER: Empowering Document-level Relation Extraction ...","url":"https://par.nsf.gov/servlets/purl/10633878"},{"title":"Eider: Empowering Document-level Relation Extraction with Efficient Evidence Extraction and Inference-stage Fusion. | BibSonomy","url":"https://www.bibsonomy.org/bibtex/27f08f257f990b9db00aa60922f7eef1c/dblp"},{"title":"EIDER: Evidence-enhanced Document-level Relation Extraction","url":"https://research.google/pubs/eider-evidence-enhanced-document-level-relation-extraction/"},{"title":"Eider: Empowering Document-level Rela
…[truncated 1641 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_research_evidence_docre_20260517T152414",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 26 · 2026-05-17T15:26:55.118862+00:00_

Web search results for query: ""Entity and Evidence Guided Relation Extraction for DocRED" arxiv 2008.12283"

Links: [{"title":"[2008.12283] Entity and Evidence Guided Relation Extraction for DocRED","url":"https://arxiv.org/abs/2008.12283"},{"title":"Entity and Evidence Guided Relation Extraction for DocRED | Request PDF","url":"https://www.researchgate.net/publication/343931511_Entity_and_Evidence_Guided_Relation_Extraction_for_DocRED"},{"title":"[2008.12283v1] Entity and Evidence Guided Relation Extraction for DocRED","url":"https://arxiv.org/abs/2008.12283v1"},{"title":"Entity and Evidence Guided Relation Extraction for DocRED - ADS","url":"https://ui.adsabs.harvard.edu/abs/2020arXiv200812283H/abstract"},{"title":"Entity and Evidence Guided Relation Extraction for DocRED","url":"https://www.catalyzex.com/paper/arxiv:2008.12283"},{"title":"[PDF] Entity and Evidence Guided Relation Extraction for DocRED | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Entity-and-Evidence-Guided-Relation-Extraction-for-Huang-Qi/172678d3fb74bc56c9ac58f024b4eb43e0470e78"},{"title":"Entity and Evidence Guided Relation Extraction for DocRED - Paper Detail","url":"https://deeplearn.org/arxiv/153393/entity-and-evidence-guided-relation-extraction-for-docred"},{"title":"(PDF) Entity and Evidence Guided Relation Extraction for DocRED","url":"https://www.academia.edu/103732963/Entity_and_Evidence_Guided_Relation_Extraction_for_DocRED"},{"title":"Evidence-aware Document-level Relation Extraction | Proceedings of the 31st ACM International Conference on Information & Knowledge Management","url":"https://dl.acm.org/doi/10.1145/3511808.3557313"},{"title":"Entity and Evidence Guided Relation Extraction for DocRED | DeepAI","url":"https://deepai.org/publication/entity-and-evidence-guided-relation-extraction-for-docred"}]

I found the paper! Here's a summary of the search results for arxiv 2008.12283:

**Title:** Entity and Evidence Guided Relation Extraction for DocRED

**Authors:*
…[truncated 1181 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_research_evidence_docre_20260517T152414",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 27 · 2026-05-17T15:26:55.119158+00:00_

Web search results for query: "DocGNRE "document relation extraction" evidence generation natural language explanation"

Links: [{"title":"Evidence and Axial Attention Guided Document-level Relation Extraction - ScienceDirect","url":"https://www.sciencedirect.com/science/article/abs/pii/S0885230824001116"},{"title":"(PDF) Enhancing Document-Level Relation Extraction with Relation-Specific Entity Representation and Evidence Sentence Augmentation","url":"https://www.researchgate.net/publication/374298993_Enhancing_Document-Level_Relation_Extraction_with_Relation-Specific_Entity_Representation_and_Evidence_Sentence_Augmentation"},{"title":"Document-Level Relation Extraction with Path Reasoning | ACM Transactions on Asian and Low-Resource Language Information Processing","url":"https://dl.acm.org/doi/10.1145/3572898"},{"title":"Document-Level Relation Extraction with Reconstruction | Request PDF","url":"https://www.researchgate.net/publication/363410025_Document-Level_Relation_Extraction_with_Reconstruction"},{"title":"Document-level multiple relations extraction method via evidence guidance and relation correlation - ScienceDirect","url":"https://www.sciencedirect.com/science/article/abs/pii/S1568494624011657"},{"title":"A survey on cutting-edge relation extraction techniques based on language models | Artificial Intelligence Review | Springer Nature Link","url":"https://link.springer.com/article/10.1007/s10462-025-11280-0"},{"title":"Document-level relation extraction with entity mentions deep attention - ScienceDirect","url":"https://www.sciencedirect.com/science/article/abs/pii/S0885230823000931"},{"title":"Document-level relation extraction based on sememe knowledge-enhanced abstract meaning representation and reasoning | Complex & Intelligent Systems","url":"https://link.springer.com/article/10.1007/s40747-023-01084-6"},{"title":"Document-Level Relation Extraction with Sentences Importance Estimation and Focusing - ACL Anthology","url":"https://aclanthology.org/20
…[truncated 2089 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_research_evidence_docre_20260517T152414",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 28 · 2026-05-17T15:26:55.119467+00:00_

Web search results for query: "COREX document-level relation extraction evidence arxiv aclanthology"

Links: [{"title":"A Comprehensive Survey on Document-Level Information ...","url":"https://aclanthology.org/2024.futured-1.6.pdf"},{"title":"[2303.03912] Document-level Relation Extraction with Cross-sentence Reasoning Graph","url":"https://arxiv.org/abs/2303.03912"},{"title":"EIDER: Empowering Document-level Relation Extraction ...","url":"https://aclanthology.org/2022.findings-acl.23.pdf"},{"title":"Document-Level Relation Extraction with Global ...","url":"https://aclanthology.org/2025.findings-acl.1002.pdf"},{"title":"COREX: Document-level Relation Extraction Framework with Consistent Two-Hop Reasoning and Evidence Sentence Prediction | IEEE Conference Publication | IEEE Xplore","url":"https://ieeexplore.ieee.org/document/10650330/"},{"title":"A survey on cutting-edge relation extraction techniques based on language models","url":"https://arxiv.org/html/2411.18157v1"},{"title":"Entity and Evidence Guided Document-Level Relation Extraction - ACL Anthology","url":"https://aclanthology.org/2021.repl4nlp-1.30/"},{"title":"A systematic review of relation extraction task since the emergence of","url":"https://arxiv.org/pdf/2511.03610"},{"title":"Rethinking Document-Level Relation Extraction","url":"https://aclanthology.org/2023.findings-acl.353.pdf"},{"title":"Multidisciplinary End-to-End Document-Level Relation Extraction from Scientific Literature | Springer Nature Link","url":"https://link.springer.com/chapter/10.1007/978-3-032-04627-7_15"}]

Based on the search results, I found information about COREX, a document-level relation extraction framework. Here are the key findings:

## COREX: Document-Level Relation Extraction Framework

COREX focuses on document-level relation extraction (DocRE), which involves identifying relationships between entities within a document and understanding relationships over longer distances, including across sentences or paragraphs.

#
…[truncated 1018 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_research_evidence_docre_20260517T152414",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool call

_source line 29 · 2026-05-17T15:26:55.119780+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"Evidence-aware Document-level Relation Extraction\" CIKM 2022 arxiv"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_research_evidence_docre_20260517T152414",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"Evidence-aware Document-level Relation Extraction\" CIKM 2022 arxiv"
  }
}
```

</details>

---

### Tool call

_source line 30 · 2026-05-17T15:26:55.119985+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "GEGA \"Yanxu Mao\" document relation extraction venue conference 2024"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_research_evidence_docre_20260517T152414",
  "tool": "WebSearch",
  "tool_args": {
    "query": "GEGA \"Yanxu Mao\" document relation extraction venue conference 2024"
  }
}
```

</details>

---

### Tool call

_source line 31 · 2026-05-17T15:26:55.120180+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "COREX \"Consistent Two-Hop Reasoning and Evidence Sentence Prediction\" document relation extraction authors venue"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_research_evidence_docre_20260517T152414",
  "tool": "WebSearch",
  "tool_args": {
    "query": "COREX \"Consistent Two-Hop Reasoning and Evidence Sentence Prediction\" document relation extraction authors venue"
  }
}
```

</details>

---

### Tool call

_source line 32 · 2026-05-17T15:26:55.120406+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "CDER \"Khai Phan Tran\" collaborative evidence retrieval venue PRICAI 2024"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_research_evidence_docre_20260517T152414",
  "tool": "WebSearch",
  "tool_args": {
    "query": "CDER \"Khai Phan Tran\" collaborative evidence retrieval venue PRICAI 2024"
  }
}
```

</details>

---

### Tool result

_source line 33 · 2026-05-17T15:26:55.120648+00:00_

Web search results for query: ""Evidence-aware Document-level Relation Extraction" CIKM 2022 arxiv"

Links: [{"title":"Evidence-aware Document-level Relation Extraction | Proceedings of the 31st ACM International Conference on Information & Knowledge Management","url":"https://dl.acm.org/doi/10.1145/3511808.3557313"},{"title":"Evidence-aware Document-level Relation Extraction - PolyU Scholars Hub","url":"https://research.polyu.edu.hk/en/publications/evidence-aware-document-level-relation-extraction"},{"title":"Document-Level In-Context Few-Shot Relation Extraction via Pre-Trained Language Models","url":"https://arxiv.org/html/2310.11085v4"},{"title":"CDER: Collaborative Evidence Retrieval for Document-level Relation Extraction","url":"https://arxiv.org/html/2504.06529"},{"title":"Rethinking Document-Level Relation Extraction: A Reality Check","url":"https://arxiv.org/html/2306.08953"},{"title":"[2106.08657] Eider: Empowering Document-level Relation Extraction with Efficient Evidence Extraction and Inference-stage Fusion","url":"https://arxiv.org/abs/2106.08657"},{"title":"Document-Level Relation Extraction Based on Heterogeneous Graph Reasoning | Proceedings of the 33rd ACM International Conference on Information and Knowledge Management","url":"https://dl.acm.org/doi/10.1145/3627673.3679899"},{"title":"Evidence-aware Document-level Relation Extraction | OpenReview","url":"https://openreview.net/forum?id=JMyPmI06JN"},{"title":"Document-Level Relation Extraction with Additional Evidence and Entity Type Information | SpringerLink","url":"https://link.springer.com/chapter/10.1007/978-981-97-5669-8_19"},{"title":"Improving Graph-based Document-Level Relation Extraction Model with Novel Graph Structure | Proceedings of the 31st ACM International Conference on Information & Knowledge Management","url":"https://dl.acm.org/doi/10.1145/3511808.3557615"}]

Based on the search results, I found information about the "Evidence-aware Document-level Relation Extraction" paper pres
…[truncated 957 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_research_evidence_docre_20260517T152414",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 34 · 2026-05-17T15:26:55.120963+00:00_

Web search results for query: "GEGA "Yanxu Mao" document relation extraction venue conference 2024"

Links: [{"title":"[2407.21384] GEGA: Graph Convolutional Networks and Evidence Retrieval Guided Attention for Enhanced Document-level Relation Extraction","url":"https://arxiv.org/abs/2407.21384"},{"title":"A Comprehensive Survey on Document-Level Information ...","url":"https://aclanthology.org/2024.futured-1.6.pdf"},{"title":"Anaphor Assisted Document-Level Relation Extraction | Request PDF","url":"https://www.researchgate.net/publication/376393382_Anaphor_Assisted_Document-Level_Relation_Extraction"},{"title":"GEGA: Graph Convolutional Networks and Evidence Retrieval Guided Attention for Enhanced Document-level Relation Extraction | IEEE Conference Publication | IEEE Xplore","url":"https://ieeexplore.ieee.org/document/10889649/"},{"title":"Dual reasoning enhanced document-level relation extraction | Neural Computing and Applications | Springer Nature Link","url":"https://link.springer.com/article/10.1007/s00521-026-12099-8"},{"title":"Document-level relation extraction model guided by global information and external contextual knowledge | The Journal of Supercomputing | Springer Nature Link","url":"https://link.springer.com/article/10.1007/s11227-025-07467-5"},{"title":"GraphFormer: Document-Level Relation Extractor for Open Source Cyber Threat Intelligence by Peipei Liu, Yanxu Mao, Kaixiang Liu, Hongsong Zhu, Limin Sun :: SSRN","url":"https://papers.ssrn.com/sol3/papers.cfm?abstract_id=6660730"},{"title":"A Comprehensive Survey on Relation Extraction: Recent Advances and New Frontiers | ACM Computing Surveys","url":"https://dl.acm.org/doi/10.1145/3674501"},{"title":"Large language models for generative information extraction: a survey | Frontiers of Computer Science | Springer Nature Link","url":"https://link.springer.com/article/10.1007/s11704-024-40555-y"},{"title":"Text2NKG: Fine-Grained N-ary Relation Extraction for ... - NIPS","url":"https://proceedings.neur
…[truncated 1150 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_research_evidence_docre_20260517T152414",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 35 · 2026-05-17T15:26:55.121273+00:00_

Web search results for query: "COREX "Consistent Two-Hop Reasoning and Evidence Sentence Prediction" document relation extraction authors venue"

Links: [{"title":"COREX: Document-level Relation Extraction Framework with Consistent Two-Hop Reasoning and Evidence Sentence Prediction | IEEE Conference Publication | IEEE Xplore","url":"https://ieeexplore.ieee.org/document/10650330/"},{"title":"Knowledge enhancement and full utilization of document information for document-level biomedical relation extraction | Scientific Reports","url":"https://www.nature.com/articles/s41598-025-32931-w"},{"title":"Multi-Relation Extraction in Entity Pairs using Global Context","url":"https://arxiv.org/html/2507.22926"},{"title":"Document-Level Relation Extraction with Adaptive Focal Loss and Knowledge Distillation | Request PDF","url":"https://www.researchgate.net/publication/361058021_Document-Level_Relation_Extraction_with_Adaptive_Focal_Loss_and_Knowledge_Distillation"},{"title":"MRN: A Locally and Globally Mention-Based Reasoning Network for Document-Level Relation Extraction | Request PDF","url":"https://www.researchgate.net/publication/353492714_MRN_A_Locally_and_Globally_Mention-Based_Reasoning_Network_for_Document-Level_Relation_Extraction"},{"title":"[2303.03912] Document-level Relation Extraction with Cross-sentence Reasoning Graph","url":"https://arxiv.org/abs/2303.03912"},{"title":"Enhancing cross-evidence reasoning graph for document-level relation extraction - PMC","url":"https://pmc.ncbi.nlm.nih.gov/articles/PMC11232587/"},{"title":"Document-Level Relation Extraction with Sentences ...","url":"https://aclanthology.org/2022.naacl-main.212.pdf"},{"title":"Document-Level Relation Extraction with Cross-sentence Reasoning Graph | Request PDF","url":"https://www.researchgate.net/publication/371085966_Document-Level_Relation_Extraction_with_Cross-sentence_Reasoning_Graph"},{"title":"Document-Level Relation Extraction","url":"https://www.emergentmind.com/topics/document-level-r
…[truncated 918 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_research_evidence_docre_20260517T152414",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 36 · 2026-05-17T15:26:55.121555+00:00_

Web search results for query: "CDER "Khai Phan Tran" collaborative evidence retrieval venue PRICAI 2024"

Links: [{"title":"CDER: Collaborative Evidence Retrieval for Document-level Relation Extraction","url":"https://arxiv.org/html/2504.06529v1"},{"title":"CDER: Collaborative Evidence Retrieval for Document-Level Relation Extraction | Springer Nature Link","url":"https://link.springer.com/content/pdf/10.1007/978-981-97-4982-9_3"},{"title":"[2504.06529] CDER: Collaborative Evidence Retrieval for Document-level Relation Extraction","url":"https://arxiv.org/abs/2504.06529"},{"title":"dblp: Khai Phan Tran","url":"https://dblp.org/pid/316/8206.html"},{"title":"[PDF] CDER: Collaborative Evidence Retrieval for Document-Level Relation Extraction | Semantic Scholar","url":"https://www.semanticscholar.org/paper/CDER:-Collaborative-Evidence-Retrieval-for-Relation-Tran-Li/07f36e6f29c07f0edce7465f4d005bd34ac659ce"},{"title":"(PDF) CDER: Collaborative Evidence Retrieval for Document-level Relation Extraction","url":"https://www.researchgate.net/publication/390638674_CDER_Collaborative_Evidence_Retrieval_for_Document-level_Relation_Extraction"}]

Based on the search results, I found information about CDER and Khai Phan Tran, though I should note that the venue mentioned in the results differs slightly from what you specified:

CDER: Collaborative Evidence Retrieval for Document-Level Relation Extraction was authored by Khai Phan Tran and Xue Li. However, the paper was published in 2024 at ACIIDS 2024 (the 16th Asian Conference on Intelligent Information and Database Systems), not PRICAI 2024.

CDER is a novel evidence retrieval framework that employs an attentional graph-based architecture to capture collaborative patterns and incorporates a dynamic sub-structure for additional robustness in evidence retrieval. The framework addresses Document-level Relation Extraction (DocRE), which involves identifying relations between entities across multiple sentences in a document, with evi
…[truncated 186 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_research_evidence_docre_20260517T152414",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool call

_source line 37 · 2026-05-17T15:26:55.121871+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"Evidence-aware Document-level Relation Extraction\" Xu Hua Qu CIKM 2022 authors full list"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_research_evidence_docre_20260517T152414",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"Evidence-aware Document-level Relation Extraction\" Xu Hua Qu CIKM 2022 authors full list"
  }
}
```

</details>

---

### Tool call

_source line 38 · 2026-05-17T15:26:55.124363+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "EIDER \"Yiqing Xie\" \"Jiaming Shen\" Findings ACL 2022 arxiv 2106.08657"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_research_evidence_docre_20260517T152414",
  "tool": "WebSearch",
  "tool_args": {
    "query": "EIDER \"Yiqing Xie\" \"Jiaming Shen\" Findings ACL 2022 arxiv 2106.08657"
  }
}
```

</details>

---

### Tool result

_source line 39 · 2026-05-17T15:26:55.124772+00:00_

Web search results for query: ""Evidence-aware Document-level Relation Extraction" Xu Hua Qu CIKM 2022 authors full list"

Links: [{"title":"Evidence-aware Document-level Relation Extraction - PolyU Scholars Hub","url":"https://research.polyu.edu.hk/en/publications/evidence-aware-document-level-relation-extraction"},{"title":"Evidence-aware Document-level Relation Extraction | Proceedings of the 31st ACM International Conference on Information & Knowledge Management","url":"https://dl.acm.org/doi/10.1145/3511808.3557313"},{"title":"Enhancing cross-evidence reasoning graph for document-level relation extraction - PMC","url":"https://pmc.ncbi.nlm.nih.gov/articles/PMC11232587/"},{"title":"Evidence-aware Document-level Relation Extraction | OpenReview","url":"https://openreview.net/forum?id=JMyPmI06JN"},{"title":"Document-level relation extraction via commonsense knowledge enhanced graph representation learning | Applied Intelligence | Springer Nature Link","url":"https://link.springer.com/article/10.1007/s10489-024-05985-y"},{"title":"[PDF] Entity and Evidence Guided Relation Extraction for DocRED | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Entity-and-Evidence-Guided-Relation-Extraction-for-Huang-Qi/172678d3fb74bc56c9ac58f024b4eb43e0470e78"},{"title":"Evidence Reasoning and Curriculum Learning for Document-Level Relation Extraction | IEEE Journals & Magazine | IEEE Xplore","url":"https://ieeexplore.ieee.org/document/10174655/"},{"title":"Document-Level Relation Extraction","url":"https://www.emergentmind.com/topics/document-level-relation-extraction"},{"title":"Document-level relation extraction via commonsense knowledge enhanced graph representation learning: Document-level relation extraction via commonsense knowledge...: Applied Intelligence: Vol 55, No 2","url":"https://dl.acm.org/doi/10.1007/s10489-024-05985-y"},{"title":"Document-level relation extraction using evidence reasoning on RST-GRAPH | Request PDF","url":"https://www.researchgate.net
…[truncated 448 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_research_evidence_docre_20260517T152414",
  "tool": "WebSearch",
  "elapsed_ms": 2
}
```

</details>

---

### Tool result

_source line 40 · 2026-05-17T15:26:55.125102+00:00_

Web search results for query: "EIDER "Yiqing Xie" "Jiaming Shen" Findings ACL 2022 arxiv 2106.08657"

Links: [{"title":"[2106.08657] Eider: Empowering Document-level Relation Extraction with Efficient Evidence Extraction and Inference-stage Fusion","url":"https://arxiv.org/abs/2106.08657"},{"title":"Jiaming Shen - ACL Anthology","url":"https://aclanthology.org/people/jiaming-shen/"},{"title":"Eider: Evidence-enhanced Document-level Relation Extraction | Request PDF","url":"https://www.researchgate.net/publication/352477694_Eider_Evidence-enhanced_Document-level_Relation_Extraction"},{"title":"GitHub - yiqingxyq/Eider: Source code for paper \"EIDER: Empowering Document-level Relation Extraction with Efficient Evidence Extraction and Inference-stage Fusion\", ACL Findings, 2022","url":"https://github.com/yiqingxyq/Eider"},{"title":"Eider: Empowering Document-level Relation Extraction with Efficient Evidence Extraction and Inference-stage Fusion - ACL Anthology","url":"https://aclanthology.org/2022.findings-acl.23/"},{"title":"[PDF] Eider: Empowering Document-level Relation Extraction with Efficient Evidence Extraction and Inference-stage Fusion | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Eider:-Empowering-Document-level-Relation-with-and-Xie-Shen/dbf1e5a17b3adead7016eb52ddc3007673ed382f"},{"title":"Eider: Empowering Document-level Relation Extraction with Efficient Evidence Extraction and Inference-stage Fusion | Request PDF","url":"https://www.researchgate.net/publication/361056993_Eider_Empowering_Document-level_Relation_Extraction_with_Efficient_Evidence_Extraction_and_Inference-stage_Fusion"},{"title":"Arxiv","url":"https://arxiv.org/pdf/2204.01320"},{"title":"arXiv.org e-Print archive","url":"https://arxiv.org/"},{"title":"Computer Science","url":"https://arxiv.org/list/cs/pastweek?skip=235&show=1000"}]

Based on the search results, I found information about the EIDER paper:

## Overview
EIDER is an evidence-enhanced framework that empowers d
…[truncated 1196 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_research_evidence_docre_20260517T152414",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 41 · 2026-05-17T15:26:55.125703+00:00_

所有论文验证完毕。以下是 6 篇验证结果：

---

## [DREEAM]
- title: DREEAM: Guiding Attention with Evidence for Improving Document-Level Relation Extraction
- authors: Youmi Ma, An Wang, Naoaki Okazaki
- venue: EACL 2023
- year: 2023
- arxiv: 2302.08675
- doi: 10.18653/v1/2023.eacl-main.145
- bibtex_key: ma2023dreeam
- verified: true
- relevance: 首次将 evidence 作为监督信号引导 attention 模块，并提出 evidence retrieval 自训练策略
- verification_note: 预期信息全部正确，第一作者 Youmi Ma (not Tan)，原始预期 "Tan et al." 有误

## [SAIS]
- title: SAIS: Supervising and Augmenting Intermediate Steps for Document-Level Relation Extraction
- authors: Yuxin Xiao, Zecheng Zhang, Yuning Mao, Carl Yang, Jiawei Han
- venue: NAACL 2022
- year: 2022
- arxiv: 2109.12093
- doi: 10.18653/v1/2022.naacl-main.171
- bibtex_key: xiao2022sais
- verified: true
- relevance: 通过监督中间步骤（evidence retrieval + entity typing）提升 DocRE，并利用 evidence 做数据增强和 ensemble 推理
- verification_note: 预期信息全部正确，第一作者 Xiao 确认

## [EIDER]
- title: Eider: Empowering Document-level Relation Extraction with Efficient Evidence Extraction and Inference-stage Fusion
- authors: Yiqing Xie, Jiaming Shen, Sha Li, Yuning Mao, Jiawei Han
- venue: Findings of ACL 2022
- year: 2022
- arxiv: 2106.08657
- doi: 10.18653/v1/2022.findings-acl.23
- bibtex_key: xie2022eider
- verified: true
- relevance: 联合训练轻量 evidence extraction 模型，推理阶段融合 evidence 预测与全文预测，是 evidence-enhanced DocRE 的代表工作
- verification_note: 不在原始候选列表中，但与 evidence-based DocRE 高度相关且发表于 top venue，替换未找到的 DocGNRE

## [Evidence-aware DocRE]
- title: Evidence-aware Document-level Relation Extraction
- authors: Tianyu Xu, Wen Hua, Jianfeng Qu, Zhixu Li, Jiajie Xu, An Liu, Lei Zhao
- venue: CIKM 2022
- year: 2022
- arxiv: not found
- doi: 10.1145/3511808.3557313
- bibtex_key: xu2022evidenceaware
- verified: true
- relevance: 直接将 evidence awareness 融入 DocRE 模型设计，evidence sentence 子集即可预测 entity pair 关系
- verification_note: 原始候选列表中的 "Evidence-aware Document-level RE"，无 arXiv 预印本，仅在 ACM DL 发表

## [GEGA]
- title: GEGA: Graph Convolutional Networks and Evidence Retrieval Guided Attention for Enhanced Document-level Relation Extraction
- authors: Yanxu Mao, Xiaolin Chen, Peipei Liu, Tiehan Cui, Zibo Yue, Zhixiao Li
- venue: ICASSP 2025
- year: 2025
- arxiv: 2407.21384
- doi: 10.1109/ICASSP49660.2025.10889649
- bibtex_key: mao2025gega
- verified: true
- relevance: 构建于 DREEAM 之上，用 GCN 构造多权重矩阵引导 attention 到 evidence sentences，在 DocRED/Re-DocRED 上超越 DREEAM
- verification_note: 原始候选列表中的 GEGA，arXiv 预印本 2024 年 7 月，正式发表于 ICASSP 2025

## [CDER]
- title: CDER: Collaborative Evidence Retrieval for Document-level Relation Extraction
- authors: Khai Phan Tran, Xue Li
- venue: ACIIDS 2024 (Springer LNCS)
- year: 2024
- arxiv: 2504.06529
- doi: 10.1007/978-981-97-4982-9_3
- bibtex_key: tran2024cder
- verified: true
- relevance: 将文档建模为二部图捕捉 entity pair 间的协作 evidence 检索模式，专注于 evidence retrieval 子任务
- verification_note: 原始候选列表中的 CDER，arXiv 版本为 2025 年 4 月更新版，会议发表于 ACIIDS 2024

---

**汇总**：
- 6/6 全部 verified
- DREEAM 预期作者 "Tan et al." 有误，实际为 Ma et al.
- DocGNRE 未能检索到对应论文，用 EIDER (Findings of ACL 2022) 替换，该论文与 evidence-based DocRE 直接相关且 venue 更强
- COREX (IJCNN 2024) 和 E2GRE (arXiv 2020) 也与 evidence 相关但 venue 较弱或未正式发表，未纳入最终 6 篇

Sources:
- [DREEAM - arXiv](https://arxiv.org/abs/2302.08675)
- [DREEAM - ACL Anthology](https://aclanthology.org/2023.eacl-main.145/)
- [SAIS - ACL Anthology](https://aclanthology.org/2022.naacl-main.171/)
- [SAIS - arXiv](https://arxiv.org/abs/2109.12093)
- [EIDER - ACL Anthology](https://aclanthology.org/2022.findings-acl.23/)
- [EIDER - arXiv](https://arxiv.org/abs/2106.08657)
- [Evidence-aware DocRE - ACM DL](https://dl.acm.org/doi/10.1145/3511808.3557313)
- [GEGA - arXiv](https://arxiv.org/abs/2407.21384)
- [GEGA - IEEE Xplore](https://ieeexplore.ieee.org/document/10889649/)
- [CDER - arXiv](https://arxiv.org/abs/2504.06529)
- [CDER - Springer](https://link.springer.com/chapter/10.1007/978-981-97-4982-9_3)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_paper_research_evidence_docre_20260517T152414"
}
```

</details>

---
