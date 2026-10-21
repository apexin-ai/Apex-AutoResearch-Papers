# research ma2024 author verify

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 7
- **Recorded user turns:** 0
- **Tool calls:** 3
- **Original source:** `logs/chats/worker_research_ma2024_author_verify_20260521T174435.jsonl`
- **Structured JSON:** [`4a3b13cab5bb2cc5d8e8.json`](../../sessions/4a/4a3b13cab5bb2cc5d8e8.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

7 recorded events

### Tool call

_source line 1 · 2026-05-21T17:45:10.643120+00:00_

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
  "session": "worker_research_ma2024_author_verify_20260521T174435",
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

_source line 2 · 2026-05-21T17:45:10.643447+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_ma2024_author_verify_20260521T174435",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-21T17:45:10.643614+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "ma2024selfimproving self-improving LLM information extraction 2024"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_ma2024_author_verify_20260521T174435",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ma2024selfimproving self-improving LLM information extraction 2024"
  }
}
```

</details>

---

### Tool result

_source line 4 · 2026-05-21T17:45:10.643786+00:00_

Web search results for query: "ma2024selfimproving self-improving LLM information extraction 2024"

Links: [{"title":"GitHub - quqxui/Awesome-LLM4IE-Papers: Awesome papers about generative Information Extraction (IE) using Large Language Models (LLMs) · GitHub","url":"https://github.com/quqxui/Awesome-LLM4IE-Papers"},{"title":"5 steps to improve information extraction using trustworthy generative AI - The SAS Data Science Blog","url":"https://blogs.sas.com/content/subconsciousmusings/2024/05/01/five-steps-to-improve-information-extraction-using-trustworthy-generative-ai/"},{"title":"Large language models for generative information extraction: a survey | Frontiers of Computer Science | Springer Nature Link","url":"https://link.springer.com/article/10.1007/s11704-024-40555-y"},{"title":"Leveraging large language models for structured information extraction from pathology reports - ScienceDirect","url":"https://www.sciencedirect.com/science/article/pii/S2153353925001075"},{"title":"Improving LLM-based relation extraction from RNA- ...","url":"https://vldb.org/workshops/2024/proceedings/LLM+KG/LLM+KG-12.pdf"},{"title":"LLM-AIx: An open source pipeline for Information Extraction from unstructured medical text based on privacy preserving Large Language Models - PubMed","url":"https://pubmed.ncbi.nlm.nih.gov/39281753/"},{"title":"Clinical Information Extraction with Large Language Models: A Case Study on Organ Procurement - PMC","url":"https://pmc.ncbi.nlm.nih.gov/articles/PMC12099322/"},{"title":"Self-Verification Improves Few-Shot Clinical Information Extraction","url":"https://arxiv.org/pdf/2306.00024"}]

Based on the search results, here are the key findings about self-improving LLMs and information extraction in 2024:

## Self-Improving LLMs for Information Extraction

Research in 2024 at the Conference of the North American Chapter of the Association for Computational Linguistics presented work on "Self-improving for zero-shot named entity recognition with large lang
…[truncated 1382 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_ma2024_author_verify_20260521T174435",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-21T17:45:10.643945+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"self-improving\" \"zero-shot named entity recognition\" Ma Xie 2024 arXiv"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_ma2024_author_verify_20260521T174435",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"self-improving\" \"zero-shot named entity recognition\" Ma Xie 2024 arXiv"
  }
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-21T17:45:10.644108+00:00_

Web search results for query: ""self-improving" "zero-shot named entity recognition" Ma Xie 2024 arXiv"

Links: [{"title":"ReverseNER: A Self-Generated Example-Driven Framework for Zero-Shot Named Entity Recognition with Large Language Models","url":"https://arxiv.org/html/2411.00533v1"},{"title":"Self-Improving for Zero-Shot Named Entity Recognition with Large Language Models - ACL Anthology","url":"https://aclanthology.org/2024.naacl-short.49/"},{"title":"[2311.08921v3] Self-Improving for Zero-Shot Named Entity Recognition with Large Language Models","url":"https://arxiv.org/abs/2311.08921v3"},{"title":"[2311.08921] Self-Improving for Zero-Shot Named Entity Recognition with Large Language Models","url":"https://arxiv.org/abs/2311.08921"},{"title":"GitHub - Emma1066/Self-Improve-Zero-Shot-NER: This is the github repository for the paper at NAACL 2024: Self-Improving for Zero-Shot Named Entity Recognition with Large Language Models. · GitHub","url":"https://github.com/Emma1066/Self-Improve-Zero-Shot-NER"},{"title":"Self-Improving for Zero-Shot Named Entity Recognition with Large   Language Models","url":"https://arxiv.org/pdf/2311.08921"},{"title":"[PDF] Self-Improving for Zero-Shot Named Entity Recognition with Large Language Models | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Self-Improving-for-Zero-Shot-Named-Entity-with-Xie-Li/d36e2b1f3d06a732773ace7b9cd786247d563fa7"},{"title":"Self-Improving for Zero-Shot Named Entity Recognition with Large Language Models","url":"https://arxiv.org/html/2311.08921v3"},{"title":"Self-Improving for Zero-Shot Named Entity Recognition with Large Language Models | Request PDF","url":"https://www.researchgate.net/publication/382631623_Self-Improving_for_Zero-Shot_Named_Entity_Recognition_with_Large_Language_Models"}]

I found the research you're looking for. The work proposes a training-free self-improving framework for zero-shot NER with LLMs, which utilizes an unlabeled corpus to stimulate the self-learning abi
…[truncated 935 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_ma2024_author_verify_20260521T174435",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 7 · 2026-05-21T17:45:10.644377+00:00_

结果明确：

- **论文完整标题**: Self-Improving for Zero-Shot Named Entity Recognition with Large Language Models
- **作者列表**: Tingyu Xie, Qi Li, Yan Zhang, Zuozhu Liu, Hongwei Wang
- **第一作者**: **Xie (Tingyu Xie)**，不是 Ma
- **arXiv ID**: 2311.08921
- **发表venue**: NAACL 2024
- **建议 bib key 修正**: `ma2024selfimproving` → `xie2024selfimproving`

Sources:
- [ACL Anthology](https://aclanthology.org/2024.naacl-short.49/)
- [arXiv 2311.08921](https://arxiv.org/abs/2311.08921)
- [Semantic Scholar](https://www.semanticscholar.org/paper/Self-Improving-for-Zero-Shot-Named-Entity-with-Xie-Li/d36e2b1f3d06a732773ace7b9cd786247d563fa7)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_research_ma2024_author_verify_20260521T174435"
}
```

</details>

---
