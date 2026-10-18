# research r10 citation verify

**How Does Schema Complexity Predict Performance in Training-Free LLM Information Extraction?** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 17
- **Recorded user turns:** 0
- **Tool calls:** 8
- **Original source:** `logs/chats/worker_research_r10-citation-verify_20260517T075934.jsonl`
- **Structured JSON:** [`0d4fd5b08973e0ce202b.json`](../../sessions/0d/0d4fd5b08973e0ce202b.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

17 recorded events

### Tool call

_source line 1 · 2026-05-17T08:00:39.778404+00:00_

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
  "session": "worker_research_r10-citation-verify_20260517T075934",
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

_source line 2 · 2026-05-17T08:00:39.778727+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_r10-citation-verify_20260517T075934",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-17T08:00:39.778927+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "NuNER Bogdanov 2024 NER named entity recognition"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_r10-citation-verify_20260517T075934",
  "tool": "WebSearch",
  "tool_args": {
    "query": "NuNER Bogdanov 2024 NER named entity recognition"
  }
}
```

</details>

---

### Tool call

_source line 4 · 2026-05-17T08:00:39.779065+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Self-Improving LLM information extraction Zhang 2024"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_r10-citation-verify_20260517T075934",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Self-Improving LLM information extraction Zhang 2024"
  }
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-17T08:00:39.779186+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "LLMaAA Zhang 2024 annotation"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_r10-citation-verify_20260517T075934",
  "tool": "WebSearch",
  "tool_args": {
    "query": "LLMaAA Zhang 2024 annotation"
  }
}
```

</details>

---

### Tool call

_source line 6 · 2026-05-17T08:00:39.779302+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Lakens 2017 equivalence tests TOST"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_r10-citation-verify_20260517T075934",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Lakens 2017 equivalence tests TOST"
  }
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-17T08:00:39.779416+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Wellek 2010 equivalence testing book"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_r10-citation-verify_20260517T075934",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Wellek 2010 equivalence testing book"
  }
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-17T08:00:39.779578+00:00_

Web search results for query: "NuNER Bogdanov 2024 NER named entity recognition"

Links: [{"title":"NuNER: Entity Recognition Encoder Pre-training via LLM-Annotated Data - ACL Anthology","url":"https://aclanthology.org/2024.emnlp-main.660/"},{"title":"NuNER: Entity Recognition Encoder Pre-training via LLM-Annotated Data","url":"https://www.researchgate.net/publication/386198401_NuNER_Entity_Recognition_Encoder_Pre-training_via_LLM-Annotated_Data"},{"title":"[2402.15343] NuNER: Entity Recognition Encoder Pre-training via LLM-Annotated Data","url":"https://arxiv.org/abs/2402.15343"},{"title":"GitHub - Serega6678/NuNER: NuNER is the family of SOTA Foundation and Zero-shot for Entity Recognition · GitHub","url":"https://github.com/Serega6678/NuNER"},{"title":"[2402.15343v1] NuNER: Entity Recognition Encoder Pre-training via LLM-Annotated Data","url":"https://arxiv.org/abs/2402.15343v1"},{"title":"numind/NuNER_Zero · Hugging Face","url":"https://huggingface.co/numind/NuNER_Zero"},{"title":"[PDF] NuNER: Entity Recognition Encoder Pre-training via LLM-Annotated Data | Semantic Scholar","url":"https://www.semanticscholar.org/paper/NuNER:-Entity-Recognition-Encoder-Pre-training-via-Bogdanov-Constantin/c3b82c397e3bc30942a214b8aca7d861d453a74f"},{"title":"numind/NuNER-v0.1 · Hugging Face","url":"https://huggingface.co/numind/NuNER-v0.1"},{"title":"Familiarity: Better Evaluation of Zero-Shot Named Entity Recognition by Quantifying Label Shifts in Synthetic Training Data","url":"https://arxiv.org/html/2412.10121"},{"title":"Retrieval-Enhanced Named Entity Recognition","url":"https://arxiv.org/html/2410.13118v1"}]

Based on the search results, here's what I found about NuNER by Bogdanov et al. 2024:

## Overview

NuNER is a compact language representation model specialized in the Named Entity Recognition (NER) task created using LLMs. The research was presented at the 2024 Conference on Empirical Methods in Natural Language Processing.

## Key Features

NuNER can be fine-tuned to
…[truncated 934 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_r10-citation-verify_20260517T075934",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 9 · 2026-05-17T08:00:39.779756+00:00_

Web search results for query: "Self-Improving LLM information extraction Zhang 2024"

Links: [{"title":"Exploring LLMs for Scientific Information Extraction using the SciEx Framework","url":"https://arxiv.org/html/2512.10004v2"},{"title":"LLM-based AI agents for automated extraction of material properties and structural features - ScienceDirect","url":"https://www.sciencedirect.com/science/article/abs/pii/S0927025626000406"},{"title":"A Simple but Effective Approach to Improve Structured Language Model Output for Information Extraction - ACL Anthology","url":"https://aclanthology.org/2024.findings-emnlp.295/"},{"title":"Reflect then Learn: Active Prompting for Information Extraction Guided by Introspective Confusion","url":"https://arxiv.org/html/2508.10036v1"},{"title":"Large language models for generative information extraction: a survey | Frontiers of Computer Science | Springer Nature Link","url":"https://link.springer.com/article/10.1007/s11704-024-40555-y"},{"title":"A Survey of Generative Information Extraction","url":"https://aclanthology.org/2025.coling-main.324.pdf"},{"title":"A Survey on Efficient Large Language Model Training: From Data-centric Perspectives","url":"https://arxiv.org/html/2510.25817v1"},{"title":"LMDX: Language Model-based Document Information Extraction and Localization - ACL Anthology","url":"https://aclanthology.org/2024.findings-acl.899/"},{"title":"CTI-Thinker: an LLM-driven system for CTI knowledge graph construction and attack reasoning | Cybersecurity | Springer Nature Link","url":"https://link.springer.com/article/10.1186/s42400-025-00505-y"},{"title":"Large Language Models for Generative Information Extraction: A Survey","url":"https://arxiv.org/html/2312.17617v3"}]

I found several relevant results related to self-improving LLMs and information extraction from 2024. Here are the key findings:

## Self-Improving LLM Information Extraction (Zhang 2024)

Xie et al. published work on "Self-improving for zero-shot named entity recog
…[truncated 1312 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_r10-citation-verify_20260517T075934",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-17T08:00:39.780009+00:00_

Web search results for query: "Lakens 2017 equivalence tests TOST"

Links: [{"title":"Equivalence Tests - Daniël Lakens, 2017","url":"https://journals.sagepub.com/doi/10.1177/1948550617697177"},{"title":"Equivalence Tests: A Practical Primer for t Tests, Correlations, and Meta-Analyses - PubMed","url":"https://pubmed.ncbi.nlm.nih.gov/28736600/"},{"title":"GitHub - Lakens/TOSTER: TOST equivalence test and power functions · GitHub","url":"https://github.com/Lakens/TOSTER"},{"title":"Equivalence Tests: A Practical Primer for t Tests, Correlations, and Meta-Analyses - PMC","url":"https://pmc.ncbi.nlm.nih.gov/articles/PMC5502906/"},{"title":"Cornell Statistical Consulting Unit Equivalence Testing","url":"https://cscu.cornell.edu/wp-content/uploads/equiv.pdf"},{"title":"(PDF) Equivalence Tests: A Practical Primer for t Tests, Correlations, and Meta-Analyses","url":"https://www.researchgate.net/publication/316752481_Equivalence_Tests_A_Practical_Primer_for_t_Tests_Correlations_and_Meta-Analyses"},{"title":"TOSTER: Two One-Sided Tests (TOST) Equivalence Testing","url":"https://cran.r-project.org/web/packages/TOSTER/index.html"},{"title":"Equivalence Testing (TOST)","url":"https://real-statistics.com/students-t-distribution/equivalence-testing-tost/"},{"title":"TOSTER: Two One-Sided Tests (TOST) Equivalence Testing version 0.8.6 from CRAN","url":"https://rdrr.io/cran/TOSTER/"},{"title":"Equivalence Testing for Psychological Research: A Tutorial - Daniël Lakens, Anne M. Scheel, Peder M. Isager, 2018","url":"https://journals.sagepub.com/doi/10.1177/2515245918770963"}]

I've successfully found information about Lakens 2017 and equivalence tests using TOST. Here's what the search returned:

## Overview

Daniël Lakens published "Equivalence Tests: A Practical Primer for t Tests, Correlations, and Meta-Analyses" in Social Psychological and Personality Science in 2017.

## What is TOST?

The TOST procedure entails performing two one-sided tests to examine whether the observed data 
…[truncated 1206 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_r10-citation-verify_20260517T075934",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 11 · 2026-05-17T08:00:39.780208+00:00_

Web search results for query: "LLMaAA Zhang 2024 annotation"

Links: [{"title":"[2310.19596] LLMaAA: Making Large Language Models as Active Annotators","url":"https://arxiv.org/abs/2310.19596"},{"title":"Human-LLM Collaborative Annotation Through Effective Verification of LLM Labels | Proceedings of the 2024 CHI Conference on Human Factors in Computing Systems","url":"https://dl.acm.org/doi/10.1145/3613904.3641960"},{"title":"LLMaAA: Making Large Language Models as Active Annotators - ACL Anthology","url":"https://aclanthology.org/2023.findings-emnlp.872/"},{"title":"LLMaAA: Making Large Language Models as Active Annotators | Request PDF","url":"https://www.researchgate.net/publication/376394522_LLMaAA_Making_Large_Language_Models_as_Active_Annotators"},{"title":"GitHub - Zhen-Tan-dmml/LLM4Annotation · GitHub","url":"https://github.com/Zhen-Tan-dmml/LLM4Annotation"},{"title":"AnnoLLM: Making Large Language Models to Be Better Crowdsourced Annotators - ACL Anthology","url":"https://aclanthology.org/2024.naacl-industry.15/"},{"title":"A Survey of LLM-based Active Learning","url":"https://aclanthology.org/2025.acl-long.708.pdf"},{"title":"Large Language Models for Data Annotation and Synthesis","url":"https://aclanthology.org/2024.emnlp-main.54.pdf"},{"title":"Large language models for generative information extraction: a survey | Frontiers of Computer Science | Springer Nature Link","url":"https://link.springer.com/article/10.1007/s11704-024-40555-y"},{"title":"Exploring LLM Annotation for Adaptation of Clinical ...","url":"https://aclanthology.org/2025.findings-acl.757.pdf"}]

Based on the search results, here's what I found about LLMaAA Zhang 2024 annotation:

## LLMaAA Overview

LLMaAA: Making Large Language Models as Active Annotators was published in the Findings of the Association for Computational Linguistics: EMNLP 2023, by authors Ruoyu Zhang, Yanzeng Li, Yongliang Ma, Ming Zhou, and Lei Zou.

## Key Concept

LLMaAA takes LLMs as annotators and puts them into
…[truncated 1076 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_r10-citation-verify_20260517T075934",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-17T08:00:39.780397+00:00_

Web search results for query: "Wellek 2010 equivalence testing book"

Links: [{"title":"Testing Statistical Hypotheses of Equivalence and Noninferiority - 2nd","url":"https://www.routledge.com/Testing-Statistical-Hypotheses-of-Equivalence-and-Noninferiority/Wellek/p/book/9781439808184"},{"title":"Testing Statistical Hypotheses of Equivalence and Noninferiority | Ste","url":"https://www.taylorfrancis.com/books/mono/10.1201/EBK1439808184/testing-statistical-hypotheses-equivalence-noninferiority-stefan-wellek"},{"title":"Testing statistical hypotheses of equivalence and noninferiority / Stefan Wellek - Penn State University Libraries Catalog","url":"https://catalog.libraries.psu.edu/catalog/6427383"},{"title":"Testing Statistical Hypotheses of Equivalence and Noninferiority : Stefan Wellek : 9781439808184 : Blackwell's","url":"https://blackwells.co.uk/bookshop/product/Testing-Statistical-Hypotheses-of-Equivalence-and-Noninferiority-by-Stefan-Wellek/9781439808184"},{"title":"Testing Statistical Hypotheses of Equivalence and Noninferiority - Stefan Wellek - Google Books","url":"https://books.google.com/books/about/Testing_Statistical_Hypotheses_of_Equiva.html?id=4WitzyJFkyoC"},{"title":"Testing Statistical Hypotheses of Equivalence and Noninferiority, Second Edition 2nd edition by Wellek, Stefan (2010) Hardcover: Stefan Wellek: Amazon.com: Books","url":"https://www.amazon.com/Statistical-Hypotheses-Equivalence-Noninferiority-Hardcover/dp/B010WETCFC"},{"title":"Testing statistical hypotheses of equivalence and noninferiority, 2nd edition Stefan Wellek (2010) ISBN: 978-1439808184; 431 pages; $109.95 Chapman & Hall/CRC; http://www.crcpress.com | Request PDF","url":"https://www.researchgate.net/publication/264378219_Testing_statistical_hypotheses_of_equivalence_and_noninferiority_2nd_edition_Stefan_Wellek_2010_ISBN_978-1439808184_431_pages_10995_Chapman_HallCRC_httpwwwcrcpresscom"},{"title":"Testing Statistical Hypotheses of Equivalence and Noninferiority by Stefan Wellek | 
…[truncated 2148 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_r10-citation-verify_20260517T075934",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-17T08:00:39.780634+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"Self-Improving for zero-shot named entity recognition\" Xie 2024 NAACL"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_r10-citation-verify_20260517T075934",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"Self-Improving for zero-shot named entity recognition\" Xie 2024 NAACL"
  }
}
```

</details>

---

### Tool call

_source line 14 · 2026-05-17T08:00:39.780800+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "LLMaAA \"Ruoyu Zhang\" 2023 EMNLP findings NER relation extraction"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_r10-citation-verify_20260517T075934",
  "tool": "WebSearch",
  "tool_args": {
    "query": "LLMaAA \"Ruoyu Zhang\" 2023 EMNLP findings NER relation extraction"
  }
}
```

</details>

---

### Tool result

_source line 15 · 2026-05-17T08:00:39.781001+00:00_

Web search results for query: "LLMaAA "Ruoyu Zhang" 2023 EMNLP findings NER relation extraction"

Links: [{"title":"LLMaAA: Making Large Language Models as Active Annotators | Request PDF","url":"https://www.researchgate.net/publication/376394522_LLMaAA_Making_Large_Language_Models_as_Active_Annotators"},{"title":"Making Large Language Models as Active Annotators","url":"https://aclanthology.org/anthology-files/pdf/findings/2023.findings-emnlp.872.pdf"},{"title":"LLMaAA: Making Large Language Models as Active Annotators - ACL Anthology","url":"https://aclanthology.org/2023.findings-emnlp.872/"},{"title":"Large language models for generative information extraction: a survey | Frontiers of Computer Science | Springer Nature Link","url":"https://link.springer.com/article/10.1007/s11704-024-40555-y"},{"title":"A Survey on Open Information Extraction from Rule-based Model to Large Language Model","url":"https://arxiv.org/html/2208.08690v7"},{"title":"Findings - EMNLP 2023","url":"https://2023.emnlp.org/program/accepted_findings/"},{"title":"A Comprehensive Survey on Relation Extraction: Recent Advances and New Frontiers | ACM Computing Surveys","url":"https://dl.acm.org/doi/10.1145/3674501"},{"title":"Large Language Models for Generative Information Extraction: A Survey","url":"https://arxiv.org/html/2312.17617v3"},{"title":"GitHub - thunlp/NREPapers: Must-read papers on neural relation extraction (NRE)","url":"https://github.com/thunlp/NREPapers"},{"title":"GitHub - quqxui/Awesome-LLM4IE-Papers: Awesome papers about generative Information Extraction (IE) using Large Language Models (LLMs) · GitHub","url":"https://github.com/quqxui/Awesome-LLM4IE-Papers"}]

Based on the search results, I found comprehensive information about the LLMaAA paper:

## LLMaAA: Making Large Language Models as Active Annotators

LLMaAA was published in the Findings of the Association for Computational Linguistics: EMNLP 2023 by Ruoyu Zhang, Yanzeng Li, Yongliang Ma, Ming Zhou, and Lei Zou from W
…[truncated 1032 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_r10-citation-verify_20260517T075934",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-17T08:00:39.781193+00:00_

Web search results for query: ""Self-Improving for zero-shot named entity recognition" Xie 2024 NAACL"

Links: [{"title":"Self-Improving for Zero-Shot Named Entity Recognition with Large Language Models - ACL Anthology","url":"https://aclanthology.org/2024.naacl-short.49/"},{"title":"GitHub - Emma1066/Self-Improve-Zero-Shot-NER: This is the github repository for the paper at NAACL 2024: Self-Improving for Zero-Shot Named Entity Recognition with Large Language Models. · GitHub","url":"https://github.com/Emma1066/Self-Improve-Zero-Shot-NER"},{"title":"[2311.08921] Self-Improving for Zero-Shot Named Entity Recognition with Large Language Models","url":"https://arxiv.org/abs/2311.08921"},{"title":"Self-Improving for Zero-Shot Named Entity Recognition ...","url":"https://aclanthology.org/2024.naacl-short.49.pdf"},{"title":"[PDF] Self-Improving for Zero-Shot Named Entity Recognition with Large Language Models | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Self-Improving-for-Zero-Shot-Named-Entity-with-Xie-Li/d36e2b1f3d06a732773ace7b9cd786247d563fa7"},{"title":"Self-Improving for Zero-Shot Named Entity Recognition with Large Language Models","url":"https://arxiv.org/html/2311.08921v3"},{"title":"Self-Improving for Zero-Shot Named Entity Recognition with Large Language Models | Request PDF","url":"https://www.researchgate.net/publication/382631623_Self-Improving_for_Zero-Shot_Named_Entity_Recognition_with_Large_Language_Models"},{"title":"ReverseNER: A Self-Generated Example-Driven Framework for Zero-Shot Named Entity Recognition with Large Language Models","url":"https://arxiv.org/html/2411.00533v1"},{"title":"[2311.08921v3] Self-Improving for Zero-Shot Named Entity Recognition with Large Language Models","url":"https://arxiv.org/abs/2311.08921v3"},{"title":"A Zero-Shot Clinical Named Entity Recognition Framework","url":"https://aclanthology.org/2025.naacl-long.150.pdf"}]

I found the paper you're looking for! Here are the details:

**Paper Title:** "Self
…[truncated 1302 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_r10-citation-verify_20260517T075934",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 17 · 2026-05-17T08:00:39.781431+00:00_

## 验证结果

### 1. NuNER (Bogdanov et al., 2024) ✅ 确认存在

- **完整标题**: NuNER: Entity Recognition Encoder Pre-training via LLM-Annotated Data
- **作者**: Sergei Bogdanov, Alexandre Constantin, Timothée Bernard, Benoit Crabbé, Etienne Bernard
- **年份**: 2024
- **Venue**: EMNLP 2024 (Main Conference)
- **BibTeX**:
```bibtex
@inproceedings{bogdanov2024nuner,
  title={NuNER: Entity Recognition Encoder Pre-training via LLM-Annotated Data},
  author={Bogdanov, Sergei and Constantin, Alexandre and Bernard, Timoth{\'e}e and Crabb{\'e}, Benoit and Bernard, Etienne},
  booktitle={Proceedings of the 2024 Conference on Empirical Methods in Natural Language Processing},
  pages={11586--11600},
  year={2024}
}
```

---

### 2. Self-Improving LLM IE (Zhang et al., 2024) ⚠️ 作者归属错误

- **完整标题**: Self-Improving for Zero-Shot Named Entity Recognition with Large Language Models
- **作者**: Tingyu **Xie**, Qi Li, Yan Zhang, Zuozhu Liu, Hongwei Wang
- **年份**: 2024
- **Venue**: NAACL 2024 (Short Papers)
- **问题**: 第一作者是 **Xie**，不是 Zhang。Zhang 只是第三作者。引用应写为 **(Xie et al., 2024)**，不是 (Zhang et al., 2024)。
- **BibTeX**:
```bibtex
@inproceedings{xie2024selfimproving,
  title={Self-Improving for Zero-Shot Named Entity Recognition with Large Language Models},
  author={Xie, Tingyu and Li, Qi and Zhang, Yan and Liu, Zuozhu and Wang, Hongwei},
  booktitle={Proceedings of the 2024 Conference of the North American Chapter of the Association for Computational Linguistics: Human Language Technologies (Volume 2: Short Papers)},
  pages={583--593},
  year={2024}
}
```

---

### 3. LLMaAA (Zhang et al., 2024) ⚠️ 年份错误

- **完整标题**: LLMaAA: Making Large Language Models as Active Annotators
- **作者**: Ruoyu Zhang, Yanzeng Li, Yongliang Ma, Ming Zhou, Lei Zou
- **年份**: **2023**（不是 2024）
- **Venue**: Findings of EMNLP 2023
- **问题**: 引用年份应为 **2023**。正确写法为 **(Zhang et al., 2023)**。
- **BibTeX**:
```bibtex
@inproceedings{zhang2023llmaaa,
  title={LLMaAA: Making Large Language Models as Active Annotators},
  author={Zhang, Ruoyu and Li, Yanzeng and Ma, Yongliang and Zhou, Ming and Zou, Lei},
  booktitle={Findings of the Association for Computational Linguistics: EMNLP 2023},
  year={2023}
}
```

---

### 4. Lakens (2017) ✅ 确认存在

- **完整标题**: Equivalence Tests: A Practical Primer for t Tests, Correlations, and Meta-Analyses
- **作者**: Daniël Lakens
- **年份**: 2017
- **Venue**: *Social Psychological and Personality Science*, 8(4), 355–362
- **DOI**: 10.1177/1948550617697177
- **BibTeX**:
```bibtex
@article{lakens2017equivalence,
  title={Equivalence Tests: A Practical Primer for t Tests, Correlations, and Meta-Analyses},
  author={Lakens, Dani{\"e}l},
  journal={Social Psychological and Personality Science},
  volume={8},
  number={4},
  pages={355--362},
  year={2017},
  doi={10.1177/1948550617697177}
}
```

---

### 5. Wellek (2010) ✅ 确认存在

- **完整标题**: Testing Statistical Hypotheses of Equivalence and Noninferiority (2nd Edition)
- **作者**: Stefan Wellek
- **年份**: 2010
- **Venue**: Chapman & Hall/CRC (书籍)
- **ISBN**: 978-1439808184, 431 pages
- **BibTeX**:
```bibtex
@book{wellek2010testing,
  title={Testing Statistical Hypotheses of Equivalence and Noninferiority},
  author={Wellek, Stefan},
  edition={2nd},
  year={2010},
  publisher={Chapman \& Hall/CRC},
  isbn={978-1439808184}
}
```

---

## 总结

| # | 引用 | 状态 | 问题 |
|---|------|------|------|
| 1 | NuNER (Bogdanov et al., 2024) | ✅ | — |
| 2 | Self-Improving (Zhang et al., 2024) | ⚠️ | 应为 **Xie et al., 2024** |
| 3 | LLMaAA (Zhang et al., 2024) | ⚠️ | 年份应为 **2023** |
| 4 | Lakens (2017) | ✅ | — |
| 5 | Wellek (2010) | ✅ | — |

**需修正**：引用 #2 的作者归属和引用 #3 的年份。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_research_r10-citation-verify_20260517T075934"
}
```

</details>

---
