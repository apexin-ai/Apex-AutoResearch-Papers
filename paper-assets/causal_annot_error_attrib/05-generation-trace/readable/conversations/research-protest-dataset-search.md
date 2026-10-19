# research protest dataset search

**Multi-Class Annotation Errors in Causal Inference: Topology-Dependent Bias, Sensitivity, and Correction** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 171
- **Recorded user turns:** 0
- **Tool calls:** 85
- **Original source:** `logs/chats/worker_research_protest-dataset-search_20260520T092905.jsonl`
- **Structured JSON:** [`bfc04dfa146bbd72bffe.json`](../../sessions/bf/bfc04dfa146bbd72bffe.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

171 recorded events

### Tool call

_source line 1 · 2026-05-20T09:35:08.147999+00:00_

called Agent

<details open><summary>🔧 Tool call — Agent</summary>

````json
{
  "description": "Search POLDEM dataset",
  "subagent_type": "general-purpose",
  "prompt": "Search the web for the \"POLDEM Protest Event Dataset\" and report on its public availability, number of categories, sample size, and whether it has gold-standard human labels.\n\nSpecifically search for:\n1. \"POLDEM protest event dataset\" — what it is, where to download\n2. Whether it's freely downloadable without application/approval\n3. Number of event type categories (K≥3?)\n4. Sample size\n5. License\n6. Citation paper\n\nUse WebSearch to actually verify — don't rely on memory. Try multiple search queries if needed.\n\nReport in this format:\n```\n数据集名称: xxx\n类别数 K: x\n类别列表: [...]\n样本量: xxx\nLicense: xxx\n下载方式: xxx (具体 URL 或命令)\nGold-standard human labels: 是/否 (标注方式说明)\n引用论文: xxx\n备注: xxx\n```"
}
````

</details>

<details><summary>Recorded metadata</summary>

````json
{
  "recorded_role": "tool",
  "session": "worker_research_protest-dataset-search_20260520T092905",
  "tool": "Agent",
  "tool_args": {
    "description": "Search POLDEM dataset",
    "subagent_type": "general-purpose",
    "prompt": "Search the web for the \"POLDEM Protest Event Dataset\" and report on its public availability, number of categories, sample size, and whether it has gold-standard human labels.\n\nSpecifically search for:\n1. \"POLDEM protest event dataset\" — what it is, where to download\n2. Whether it's freely downloadable without application/approval\n3. Number of event type categories (K≥3?)\n4. Sample size\n5. License\n6. Citation paper\n\nUse WebSearch to actually verify — don't rely on memory. Try multiple search queries if needed.\n\nReport in this format:\n```\n数据集名称: xxx\n类别数 K: x\n类别列表: [...]\n样本量: xxx\nLicense: xxx\n下载方式: xxx (具体 URL 或命令)\nGold-standard human labels: 是/否 (标注方式说明)\n引用论文: xxx\n备注: xxx\n```"
  }
}
````

</details>

---

### Tool call

_source line 2 · 2026-05-20T09:35:08.148431+00:00_

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
  "session": "worker_research_protest-dataset-search_20260520T092905",
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

_source line 3 · 2026-05-20T09:35:08.148638+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_protest-dataset-search_20260520T092905",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 4 · 2026-05-20T09:35:08.148804+00:00_

called Agent

<details open><summary>🔧 Tool call — Agent</summary>

````json
{
  "description": "Search MMD dataset",
  "subagent_type": "general-purpose",
  "prompt": "Search the web for the \"Mass Mobilization Project\" (also known as MMD or Mass Mobilization Data) and report on its public availability for NLP/ML use.\n\nSpecifically search for:\n1. \"Mass Mobilization Project dataset\" — what it is, where to download\n2. Whether it's freely downloadable without application/approval\n3. Number of event type categories — does it have K≥3 classification categories?\n4. Sample size\n5. License and terms of use — is it allowed for ML/NLP research?\n6. Citation paper\n\nUse WebSearch to actually verify — don't rely on memory. Try multiple search queries if needed.\n\nReport in this format:\n```\n数据集名称: xxx\n类别数 K: x\n类别列表: [...]\n样本量: xxx\nLicense: xxx\n下载方式: xxx (具体 URL 或命令)\nGold-standard human labels: 是/否 (标注方式说明)\n引用论文: xxx\n备注: xxx\n```"
}
````

</details>

<details><summary>Recorded metadata</summary>

````json
{
  "recorded_role": "tool",
  "session": "worker_research_protest-dataset-search_20260520T092905",
  "tool": "Agent",
  "tool_args": {
    "description": "Search MMD dataset",
    "subagent_type": "general-purpose",
    "prompt": "Search the web for the \"Mass Mobilization Project\" (also known as MMD or Mass Mobilization Data) and report on its public availability for NLP/ML use.\n\nSpecifically search for:\n1. \"Mass Mobilization Project dataset\" — what it is, where to download\n2. Whether it's freely downloadable without application/approval\n3. Number of event type categories — does it have K≥3 classification categories?\n4. Sample size\n5. License and terms of use — is it allowed for ML/NLP research?\n6. Citation paper\n\nUse WebSearch to actually verify — don't rely on memory. Try multiple search queries if needed.\n\nReport in this format:\n```\n数据集名称: xxx\n类别数 K: x\n类别列表: [...]\n样本量: xxx\nLicense: xxx\n下载方式: xxx (具体 URL 或命令)\nGold-standard human labels: 是/否 (标注方式说明)\n引用论文: xxx\n备注: xxx\n```"
  }
}
````

</details>

---

### Tool call

_source line 5 · 2026-05-20T09:35:08.149004+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "POLDEM Protest Event Dataset download categories"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_protest-dataset-search_20260520T092905",
  "tool": "WebSearch",
  "tool_args": {
    "query": "POLDEM Protest Event Dataset download categories"
  }
}
```

</details>

---

### Tool call

_source line 6 · 2026-05-20T09:35:08.149133+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "POLDEM protest event dataset citation paper sample size"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_protest-dataset-search_20260520T092905",
  "tool": "WebSearch",
  "tool_args": {
    "query": "POLDEM protest event dataset citation paper sample size"
  }
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-20T09:35:08.149319+00:00_

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
  "session": "worker_research_protest-dataset-search_20260520T092905",
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

_source line 8 · 2026-05-20T09:35:08.149447+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_protest-dataset-search_20260520T092905",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-20T09:35:08.149562+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Mass Mobilization Project dataset download MMP protest data"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_protest-dataset-search_20260520T092905",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Mass Mobilization Project dataset download MMP protest data"
  }
}
```

</details>

---

### Tool call

_source line 10 · 2026-05-20T09:35:08.149675+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"Mass Mobilization Data\" MMD dataset categories event types NLP"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_protest-dataset-search_20260520T092905",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"Mass Mobilization Data\" MMD dataset categories event types NLP"
  }
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-20T09:35:08.149809+00:00_

called Agent

<details open><summary>🔧 Tool call — Agent</summary>

````json
{
  "description": "Search protest NLP datasets",
  "subagent_type": "general-purpose",
  "prompt": "Search the web for publicly available protest/political event multi-class text classification datasets suitable for NLP research. I need datasets with K≥3 categories, gold-standard human labels, fully public download (no approval needed), English or multilingual, and sample size ≥1000.\n\nUse WebSearch with these queries (try at least 3-4 of them):\n1. \"protest event dataset NLP\" OR \"political event classification dataset\"\n2. \"contentious politics dataset annotation NLP\"\n3. \"event type classification benchmark\" protest\n4. Search Papers with Code for protest event or political event benchmarks\n5. \"protest news classification dataset\" github\n6. \"political event coding dataset\" public download\n\nFor each dataset found, report:\n```\n数据集名称: xxx\n类别数 K: x\n类别列表: [...]\n样本量: xxx\nLicense: xxx\n下载方式: xxx (具体 URL 或命令)\nGold-standard human labels: 是/否 (标注方式说明)\n引用论文: xxx\n备注: xxx\n```\n\nIf you find datasets from shared tasks (e.g., CLEF, SemEval) related to protest event detection, include those too. Also look for:\n- Indian Protest Event datasets\n- SPEED (Social, Political and Economic Event Database)\n- Any HuggingFace datasets related to protest classification\n- ProtestNews shared task datasets (CLEF)\n\nBe thorough — search multiple queries and report ALL candidates found."
}
````

</details>

<details><summary>Recorded metadata</summary>

````json
{
  "recorded_role": "tool",
  "session": "worker_research_protest-dataset-search_20260520T092905",
  "tool": "Agent",
  "tool_args": {
    "description": "Search protest NLP datasets",
    "subagent_type": "general-purpose",
    "prompt": "Search the web for publicly available protest/political event multi-class text classification datasets suitable for NLP research. I need datasets with K≥3 categories, gold-standard human labels, fully public download (no approval needed), English or multilingual, and sample size ≥1000.\n\nUse WebSearch with these queries (try at least 3-4 of them):\n1. \"protest event dataset NLP\" OR \"political event classification dataset\"\n2. \"contentious politics dataset annotation NLP\"\n3. \"event type classification benchmark\" protest\n4. Search Papers with Code for protest event or political event benchmarks\n5. \"protest news classification dataset\" github\n6. \"political event coding dataset\" public download\n\nFor each dataset found, report:\n```\n数据集名称: xxx\n类别数 K: x\n类别列表: [...]\n样本量: xxx\nLicense: xxx\n下载方式: xxx (具体 URL 或命令)\nGold-standard human labels: 是/否 (标注方式说明)\n引用论文: xxx\n备注: xxx\n```\n\nIf you find datasets from shared tasks (e.g., CLEF, SemEval) related to protest event detection, include those too. Also look for:\n- Indian Protest Event datasets\n- SPEED (Social, Political and Economic Event Database)\n- Any HuggingFace datasets related to protest classification\n- ProtestNews shared task datasets (CLEF)\n\nBe thorough — search multiple queries and report ALL candidates found."
  }
}
````

</details>

---

### Tool result

_source line 12 · 2026-05-20T09:35:08.149982+00:00_

Web search results for query: "POLDEM Protest Event Dataset download categories"

Links: [{"title":"1 PolDem – Protest Dataset on EU Issues - Version 1 - poldem-protest_eu","url":"https://poldem.eui.eu/downloads/pea/poldem-protest_eu_codebook.pdf"},{"title":"1 PolDem – Protest Event Dataset 30 - Version 1 - Please cite as:","url":"https://poldem.eui.eu/downloads/pea/PEA_documentation_v1.pdf"},{"title":"Data Overview - PolDem - European University Institute","url":"https://poldem.eui.eu/data-overview/"},{"title":"1 PolDem – Protest Dataset 30 European countries - Version 1 -","url":"https://poldem.eui.eu/downloads/pea/poldem-protest_30_codebook.pdf"},{"title":"Observatory for Political Conflict and Democracy in Europe","url":"https://discuss-data.net/dataset/c7e7af8f-fa6f-46d3-8ae5-41a4aad6e4b9/"},{"title":"Data Portal on Political Conflict and Democracy in Europe (PolDem) | WZB","url":"https://www.wzb.eu/en/research/dynamics-of-political-systems/center-for-civil-society-research/projects/daten-portal-zu-politischen-konflikten-und-protest-in-europa"},{"title":"PolDem - Observatory for Political Conflict and Democracy in Europe","url":"https://poldem.eui.eu/"},{"title":"GitHub - davidpomerenke/german-protest-registrations: Dataset on demonstrations in Germany","url":"https://github.com/davidpomerenke/german-protest-registrations"}]

Based on the search results, I found information about the POLDEM Protest Event Dataset:

The Observatory for Political Conflict and Democracy (PolDem) provides interactive data exploration and analysis tools, as well as the methodology and codebooks used for data generation and analysis, with a short overview of the main datasets provided.

PolDem includes data on protest events in 30 European countries obtained by coding media coverage. The data collection relies on semi-automated coding of newswire reports and covers 30 European countries and the time period from 2000 until 2015.

Regarding the download and categories, the website provi
…[truncated 678 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_protest-dataset-search_20260520T092905",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-20T09:35:08.150129+00:00_

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
  "session": "worker_research_protest-dataset-search_20260520T092905",
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

_source line 14 · 2026-05-20T09:35:08.150275+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_protest-dataset-search_20260520T092905",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 15 · 2026-05-20T09:35:08.150404+00:00_

Web search results for query: "POLDEM protest event dataset citation paper sample size"

Links: [{"title":"1 PolDem – Protest Dataset on EU Issues - Version 1 - poldem-protest_eu","url":"https://poldem.eui.eu/downloads/pea/poldem-protest_eu_codebook.pdf"},{"title":"1 PolDem – Protest Event Dataset 30 - Version 1 - Please cite as:","url":"https://poldem.eui.eu/downloads/pea/PEA_documentation_v1.pdf"},{"title":"Full article: Local protest event analysis: providing a more comprehensive picture?","url":"https://www.tandfonline.com/doi/full/10.1080/01402382.2024.2363709"},{"title":"1 PolDem – Protest Dataset 30 European countries - Version 1 -","url":"https://poldem.eui.eu/downloads/pea/poldem-protest_30_codebook.pdf"},{"title":"PolDem - Observatory for Political Conflict and Democracy in Europe","url":"https://poldem.eui.eu/"},{"title":"Data Portal on Political Conflict and Democracy in Europe (PolDem) | WZB","url":"https://www.wzb.eu/en/research/dynamics-of-political-systems/center-for-civil-society-research/projects/daten-portal-zu-politischen-konflikten-und-protest-in-europa"},{"title":"(PDF) Local protest event analysis: providing a more comprehensive picture?","url":"https://www.researchgate.net/publication/381615564_Local_protest_event_analysis_providing_a_more_comprehensive_picture"},{"title":"PolDem – Protest Dataset 30 European countries - Research output - Vrije Universiteit Amsterdam","url":"https://research.vu.nl/en/datasets/poldem-protest-dataset-30-european-countries/publications/"}]

Based on the search results, I found relevant information about the POLDEM protest event dataset:

## Citation Information

The main citation for the PolDem-Protest Dataset on EU issues is Maag, Simon 2020. PolDem-Protest Dataset on EU issues, Version 1. For the broader European dataset, the PolDem-Protest Dataset 30 European Countries, Version 1 is cited.

## Dataset Scope

The data collection relies on a semi-automated coding of newswire reports and covers 30 European count
…[truncated 709 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_protest-dataset-search_20260520T092905",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool call

_source line 16 · 2026-05-20T09:35:08.150550+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"protest event dataset NLP\" OR \"political event classification dataset\" multi-class"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_protest-dataset-search_20260520T092905",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"protest event dataset NLP\" OR \"political event classification dataset\" multi-class"
  }
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-20T09:35:08.150684+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"contentious politics dataset annotation NLP\" text classification"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_protest-dataset-search_20260520T092905",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"contentious politics dataset annotation NLP\" text classification"
  }
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-20T09:35:08.150807+00:00_

Web search results for query: ""Mass Mobilization Data" MMD dataset categories event types NLP"

Links: [{"title":"About the Mass Mobilization Project","url":"https://massmobilization.github.io/about.html"},{"title":"MMD (Mass Mobilization Database) from Clark and Regan (2018): 166... | Download Scientific Diagram","url":"https://www.researchgate.net/figure/MMD-Mass-Mobilization-Database-from-Clark-and-Regan-2018-166-countries-across-South_fig1_352664331"},{"title":"Mass Mobilization dataset - Harvard Dataverse","url":"https://dataverse.harvard.edu/dataverse/MMdata"},{"title":"Mass Mobilization Data Project - Data Catalog","url":"https://datacatalog.library.wayne.edu/dataset/mass-mobilization-data-project"},{"title":"Mass Mobilization Protest Data - dataset by government","url":"https://data.world/government/mass-mobilization-protest-data/activity"},{"title":"Mass Mobilization Protest Data - Mass Mobilization Data Project Dataverse","url":"https://dataverse.harvard.edu/dataset.xhtml?persistentId=doi:10.7910/DVN/HTTWYL"},{"title":"Mass Mobilization in Autocracies Database","url":"https://mmadatabase.org/"},{"title":"Creating Custom Event Data Without Dictionaries: A Bag-of-Tricks","url":"https://arxiv.org/pdf/2304.01331"},{"title":"Visualization Techniques to Enhance Automated Event Extraction","url":"https://arxiv.org/pdf/2106.06588"},{"title":"The Mass Mobilization Project","url":"https://massmobilization.github.io/"}]

Based on the search results, here's what I found about the Mass Mobilization Data (MMD) dataset:

## Overview
The Mass Mobilization (MM) data are an effort to understand citizen movements against governments, what citizens want when they demonstrate against governments, and how governments respond to citizens. The MM data cover 162 countries between 1990 and 2018. These data contain events where 50 or more protesters publicly demonstrate against government, resulting in more than 10,000 protest events.

## Demand Categories
For each event, the MM da
…[truncated 857 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_protest-dataset-search_20260520T092905",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 19 · 2026-05-20T09:35:08.150959+00:00_

Web search results for query: "Mass Mobilization Project dataset download MMP protest data"

Links: [{"title":"GitHub - KyleMackey/MassMobilization: Collection of applications that depict the Mass Mobilization Protest Dataset","url":"https://github.com/KyleMackey/MassMobilization"},{"title":"Mass Mobilization Protest Data - Mass Mobilization Data Project Dataverse","url":"https://dataverse.harvard.edu/dataset.xhtml?persistentId=doi:10.7910/DVN/HTTWYL"},{"title":"Mass Mobilization Data Project - Data Catalog","url":"https://datacatalog.library.wayne.edu/dataset/mass-mobilization-data-project"},{"title":"Mass Mobilization Data Project Dataverse","url":"https://dataverse.harvard.edu/dataverse/MMdata"},{"title":"About the Mass Mobilization Project","url":"https://massmobilization.github.io/about.html"},{"title":"Review of Clark/Regan (2016): Mass Mobilization Project","url":"https://discuss-data.net/dataset/4e6a40ff-4ae0-4cc8-89b3-dbe162be07c0/"},{"title":"Mass Mobilization Data Project Codebook and User’s Manual David H. Clark","url":"https://reed-statistics.github.io/math141s21/projects/mass_mobilization/MM_codebook.pdf"},{"title":"The Mass Mobilization Project","url":"https://massmobilization.github.io/"},{"title":"Mass Mobilization Protest Data - dataset by government","url":"https://data.world/government/mass-mobilization-protest-data"},{"title":"Mass Mobilization in Autocracies Database","url":"https://mmadatabase.org/"}]

Based on the search results, here's what I found about the Mass Mobilization Project dataset and how to download it:

## Dataset Overview

The Mass Mobilization Project codes protests against governments, covering 162 countries between 1990 and March 2020, and for each protest event records protester demands, government responses, protest location, and protester identities.

## Download Locations

The main sources for downloading the MMP protest data are:

1. **Harvard Dataverse** - The Mass Mobilization dataset can be found at https://dataverse
…[truncated 738 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_protest-dataset-search_20260520T092905",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool call

_source line 20 · 2026-05-20T09:35:08.151105+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "POLDEM protest event dataset \"event type\" categories codebook issue type"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_protest-dataset-search_20260520T092905",
  "tool": "WebSearch",
  "tool_args": {
    "query": "POLDEM protest event dataset \"event type\" categories codebook issue type"
  }
}
```

</details>

---

### Tool call

_source line 21 · 2026-05-20T09:35:08.151296+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"event type classification benchmark\" protest NLP dataset public"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_protest-dataset-search_20260520T092905",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"event type classification benchmark\" protest NLP dataset public"
  }
}
```

</details>

---

### Tool call

_source line 22 · 2026-05-20T09:35:08.151439+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "poldem.eui.eu protest dataset license download registration required"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_protest-dataset-search_20260520T092905",
  "tool": "WebSearch",
  "tool_args": {
    "query": "poldem.eui.eu protest dataset license download registration required"
  }
}
```

</details>

---

### Tool call

_source line 23 · 2026-05-20T09:35:08.151562+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "site:paperswithcode.com protest event OR political event classification benchmark dataset"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_protest-dataset-search_20260520T092905",
  "tool": "WebSearch",
  "tool_args": {
    "query": "site:paperswithcode.com protest event OR political event classification benchmark dataset"
  }
}
```

</details>

---

### Tool call

_source line 24 · 2026-05-20T09:35:08.151682+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Mass Mobilization Project codebook protest demand categories full list Clark Regan"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_protest-dataset-search_20260520T092905",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Mass Mobilization Project codebook protest demand categories full list Clark Regan"
  }
}
```

</details>

---

### Tool call

_source line 25 · 2026-05-20T09:35:08.151804+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Mass Mobilization Project citation paper Clark Regan license terms of use Harvard Dataverse"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_protest-dataset-search_20260520T092905",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Mass Mobilization Project citation paper Clark Regan license terms of use Harvard Dataverse"
  }
}
```

</details>

---

### Tool result

_source line 26 · 2026-05-20T09:35:08.151931+00:00_

Web search results for query: "poldem.eui.eu protest dataset license download registration required"

Links: [{"title":"PolDem - Observatory for Political Conflict and Democracy in Europe • Political Sociology • Department of Political and Social Sciences","url":"https://www.polsoz.fu-berlin.de/en/soziologie/arbeitsbereiche/politische-soziologie/ressourcen/research/dataportal.html"},{"title":"1 PolDem – Protest Dataset on EU Issues - Version 1 - poldem-protest_eu","url":"https://poldem.eui.eu/downloads/pea/poldem-protest_eu_codebook.pdf"},{"title":"National Election Campaign Dataset on EU issues","url":"https://poldem.eui.eu/downloads/cosa/poldem-election_eu_codebook.pdf"},{"title":"PolDem - Observatory for Political Conflict and Democracy in Europe","url":"https://poldem.eui.eu/"},{"title":"Eui","url":"https://poldem.eui.eu/downloads/pea/poldem-protest_eu.dta"},{"title":"1 PolDem – Protest Event Dataset 30 - Version 1 - Please cite as:","url":"https://poldem.eui.eu/downloads/pea/PEA_documentation_v1.pdf"},{"title":"1 PolDem – Protest Dataset 30 European countries - Version 1 -","url":"https://poldem.eui.eu/downloads/pea/poldem-protest_30_codebook.pdf"},{"title":"Platform for Protest and Conflict in Europe | WZB","url":"https://www.wzb.eu/en/news/platform-for-protest-and-conflict-in-europe"},{"title":"Data Portal on Political Conflict and Democracy in Europe (PolDem) | WZB","url":"https://www.wzb.eu/en/research/dynamics-of-political-systems/center-for-civil-society-research/projects/daten-portal-zu-politischen-konflikten-und-protest-in-europa"}]

Based on the search results, I found information about the PolDem protest dataset from the European University Institute. Here's what I found:

The Observatory for Political Conflict and Democracy (PolDem) is a platform that produces and maintains original data on protest events, election campaigns, and issue-specific public contestation covering Western, Southern, as well as Central-Eastern European countries over a large 
…[truncated 1040 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_protest-dataset-search_20260520T092905",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 27 · 2026-05-20T09:35:08.152079+00:00_

Web search results for query: ""protest event dataset NLP" OR "political event classification dataset" multi-class"

Links: [{"title":"Protest Event Analysis : American Behavioral Scientist","url":"https://www.ovid.com/journals/absc/fulltext/10.1177/00027642211021650~protest-event-analysis-developing-a-semiautomated-nlp"},{"title":"Protest Event Analysis: Developing a Semiautomated NLP Approach - Jasmine Lorenzini, Hanspeter Kriesi, Peter Makarov, Bruno Wüest, 2022","url":"https://journals.sagepub.com/doi/10.1177/00027642211021650"},{"title":"1 PolDem – Protest Event Dataset 30 - Version 1 - Please cite as:","url":"https://poldem.eui.eu/downloads/pea/PEA_documentation_v1.pdf"},{"title":"(PDF) Protest Event Analysis: Developing a Semiautomated NLP Approach","url":"https://www.researchgate.net/publication/352087597_Protest_Event_Analysis_Developing_a_Semiautomated_NLP_Approach"},{"title":"Emerging Markets Welfare – Work Package 2: Protest Events Database using NLP and Machine Learning","url":"https://emw.ku.edu.tr/project/work-packages/work-package-2-protest-events-database/"},{"title":"Collecting protest event data using natural language processing models: Post-Soviet Affairs: Vol 42 , No 1 - Get Access","url":"https://www.tandfonline.com/doi/full/10.1080/1060586X.2025.2600874"},{"title":"[2102.00917] Counting Protests in News Articles: A Dataset and Semi-Automated Data Collection Pipeline","url":"https://ar5iv.labs.arxiv.org/html/2102.00917"}]

Based on the search results, I found several relevant datasets and resources for protest event classification using NLP:

## Key Datasets and Research

**PolDem – Protest Event Dataset**: This dataset reports about protest events with probability scores above 0.90, and includes multi-class classification for different action forms.

**Russian Contentious Events Dataset (RCED)**: This is a comprehensive dataset of contentious events in Russia from 2010 to 2023, with a methodological workflow that includes event classification,
…[truncated 998 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_protest-dataset-search_20260520T092905",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 28 · 2026-05-20T09:35:08.152281+00:00_

Web search results for query: "POLDEM protest event dataset "event type" categories codebook issue type"

Links: [{"title":"1 PolDem – Protest Dataset on EU Issues - Version 1 - poldem-protest_eu","url":"https://poldem.eui.eu/downloads/pea/poldem-protest_eu_codebook.pdf"},{"title":"Full article: Local protest event analysis: providing a more comprehensive picture?","url":"https://www.tandfonline.com/doi/full/10.1080/01402382.2024.2363709"},{"title":"1 PolDem – Protest Dataset 30 European countries - Version 1 -","url":"https://poldem.eui.eu/downloads/pea/poldem-protest_30_codebook.pdf"},{"title":"PolDem - Observatory for Political Conflict and Democracy in Europe","url":"https://poldem.eui.eu/"},{"title":"1 PolDem – Protest Event Dataset 30 - Version 1 - Please cite as:","url":"https://poldem.eui.eu/downloads/pea/PEA_codebook_v1.pdf"},{"title":"Observatory for Political Conflict and Democracy in Europe","url":"https://discuss-data.net/dataset/c7e7af8f-fa6f-46d3-8ae5-41a4aad6e4b9/"},{"title":"ACLED Codebook | ACLED","url":"https://acleddata.com/methodology/acled-codebook"},{"title":"Full article: Protest in unlikely times: dynamics of collective mobilization in Europe during the COVID-19 crisis","url":"https://www.tandfonline.com/doi/full/10.1080/13501763.2022.2140819"}]

I found relevant information about the POLDEM protest event dataset. Here are the key findings:

## POLDEM Dataset Overview

The Observatory for Political Conflict and Democracy (PolDem) is a platform that produces and maintains original data on protest events, election campaigns, and issue-specific public contestation covering Western, Southern, as well as Central-Eastern European countries over a large time-span.

## Event Type and Issue Categories

The dataset includes issue categories labeled as 'issue_econ_private', 'issue_econ_public', 'issue_cult_lib', 'issue_environment', 'issue_political', 'issue_regional', 'issue_cult_cons', 'issue_xeno', 'issue_other', and 'issue_dontkno' (with the last o
…[truncated 634 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_protest-dataset-search_20260520T092905",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 29 · 2026-05-20T09:35:08.152445+00:00_

Web search results for query: ""contentious politics dataset annotation NLP" text classification"

Links: [{"title":"Large language models as a substitute for human experts in annotating political text - Michael Heseltine, Bernhard Clemm von Hohenberg, 2024","url":"https://journals.sagepub.com/doi/10.1177/20531680241236239"},{"title":"Global Contentious Politics Database (GLOCON) Annotation Manuals","url":"https://arxiv.org/pdf/2206.10299"},{"title":"Enhancing LLM-Based Text Classification in Political Science: Automatic Prompt Optimization and Dynamic Exemplar Selection for Few-Shot Learning","url":"https://arxiv.org/html/2409.01466v2"},{"title":"AgoraSpeech: A multi-annotated comprehensive dataset of political discourse through the lens of humans and AI","url":"https://arxiv.org/html/2501.06265v1"},{"title":"Benchmarking LLMs in Political Content Text-Annotation: Proof-of-Concept   with Toxicity and Incivility Data","url":"https://arxiv.org/pdf/2409.09741"},{"title":"Political Leaning and Politicalness Classification of Texts","url":"https://arxiv.org/html/2507.13913v1"}]

I found several relevant results on contentious politics, dataset annotation, and NLP text classification. Here are the key findings:

**Major Datasets and Projects:**

The Global Contentious Politics Database (GLOCON) is an annotation project developed by researchers at Koç University, funded by the European Research Council Starting Grant, which focuses on annotating contentious political events.

The AgoraSpeech dataset is a comprehensive annotated dataset of political discourse with annotations for six NLP tasks including text classification, topic identification, sentiment analysis, named entity recognition, and polarization and populism detection, using a two-step annotation process with ChatGPT-generated annotations followed by human-in-the-loop validation.

**Annotation Challenges:**

When dealing with contentious classifications, human-coded data can be problematic particularly due to t
…[truncated 678 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_protest-dataset-search_20260520T092905",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 30 · 2026-05-20T09:35:08.152592+00:00_

Web search results for query: "site:paperswithcode.com protest event OR political event classification benchmark dataset"

Links: [{"title":"Zachary C. Steinert-Threlkeld | Papers With Code","url":"https://paperswithcode.com/search?q=author:Zachary+C.+Steinert-Threlkeld"},{"title":"Cross-context News Corpus for Protest Events related Knowledge Base   Construction","url":"https://arxiv.org/pdf/2008.00351"},{"title":"Benchmarking LLMs in Political Content Text-Annotation: Proof-of-Concept   with Toxicity and Incivility Data","url":"https://arxiv.org/pdf/2409.09741"},{"title":"Papers with Code - Joanna Szwoch","url":"https://paperswithcode.com/search?q=author:Joanna+Szwoch"},{"title":"Papers with Code - Event-Stream Dataset Dataset","url":"https://paperswithcode.com/dataset/event-stream-dataset"},{"title":"Protest Activity Detection and Perceived Violence Estimation from Social   Media Images","url":"https://arxiv.org/pdf/1709.06204"},{"title":"Multitask Models for Supervised Protests Detection in Texts","url":"https://arxiv.org/pdf/2005.02954"}]

Based on the search results, here are some relevant protest event and political event classification benchmark datasets found on Papers with Code:

1. **UCLA Protest Image Dataset**: A novel dataset of 40,764 images (11,659 protest images and hard negatives) with various annotations of visual attributes and sentiments. This was used to train a multi-task convolutional neural network to automatically classify the presence of protesters in an image and predict its visual attributes, perceived violence and exhibited emotions.

2. **Cross-context News Corpus for Protest Events**: A gold standard corpus of protest events from various local and international sources across countries in English with document, sentence, and token level annotations. This corpus facilitates creating machine learning models that automatically classify news articles and extract protest event-related information.

3. **CLEF 2019 ProtestNews Lab**: This la
…[truncated 536 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_protest-dataset-search_20260520T092905",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 31 · 2026-05-20T09:35:08.152773+00:00_

Web search results for query: ""event type classification benchmark" protest NLP dataset public"

Links: [{"title":"Collecting protest event data using natural language processing models: Post-Soviet Affairs: Vol 42 , No 1 - Get Access","url":"https://doi.org/10.1080/1060586X.2025.2600874"},{"title":"CEHA: A Dataset of Conflict Events in the Horn of Africa","url":"https://arxiv.org/html/2412.13511v1"},{"title":"New Benchmark Corpus and Models for Fine-grained ...","url":"https://aclanthology.org/2020.coling-main.584.pdf"},{"title":"MPEDS: Automating the Generation of Protest Event Data | Request PDF","url":"https://www.researchgate.net/publication/326121293_MPEDS_Automating_the_Generation_of_Protest_Event_Data"},{"title":"(PDF) NSUT-NLP at CASE 2022 Task 1: Multilingual Protest Event Detection using Transformer-based Models","url":"https://www.academia.edu/110108255/NSUT_NLP_at_CASE_2022_Task_1_Multilingual_Protest_Event_Detection_using_Transformer_based_Models"},{"title":"[2102.00917] Counting Protests in News Articles: A Dataset and Semi-Automated Data Collection Pipeline","url":"https://ar5iv.labs.arxiv.org/html/2102.00917"},{"title":"(PDF) Protest Event Analysis: Developing a Semiautomated NLP Approach","url":"https://www.researchgate.net/publication/352087597_Protest_Event_Analysis_Developing_a_Semiautomated_NLP_Approach"},{"title":"Protest Event Analysis: Developing a Semiautomated NLP Approach - Jasmine Lorenzini, Hanspeter Kriesi, Peter Makarov, Bruno Wüest, 2022","url":"https://journals.sagepub.com/doi/10.1177/00027642211021650"}]

Based on the search results, here are several event type classification benchmarks and NLP datasets related to protests that are publicly available:

## Key Public Datasets

The Russian Contentious Events Dataset (RCED) is a comprehensive dataset of contentious events in Russia from 2010 to 2023, with the dataset, codebook, and samples available publicly on Zenodo. The dataset includes a methodological workflow for event classifi
…[truncated 1346 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_protest-dataset-search_20260520T092905",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 32 · 2026-05-20T09:35:08.152927+00:00_

Web search results for query: "Mass Mobilization Project codebook protest demand categories full list Clark Regan"

Links: [{"title":"Data Sources","url":"https://reed-statistics.github.io/math141s21/project_data.html"},{"title":"Mass Mobilization Data Project Codebook and User’s Manual David H. Clark","url":"https://reed-statistics.github.io/math141s21/projects/mass_mobilization/MM_codebook.pdf"},{"title":"Review of Clark/Regan (2016): Mass Mobilization Project","url":"https://discuss-data.net/dataset/4e6a40ff-4ae0-4cc8-89b3-dbe162be07c0/"},{"title":"Mass Mobilization Data Project - Data Catalog","url":"https://datacatalog.library.wayne.edu/dataset/mass-mobilization-data-project"},{"title":"About the Mass Mobilization Project","url":"https://massmobilization.github.io/about.html"},{"title":"Mass Mobilization Data Project Dataverse","url":"https://dataverse.harvard.edu/dataverse/MMdata"},{"title":"Data Is Plural — 2020.08.26 edition","url":"https://www.data-is-plural.com/archive/2020-08-26-edition/"},{"title":"DataCite Search","url":"https://search.datacite.org/works/10.7910/dvn/httwyl"},{"title":"Mass Mobilization Protest Data - Mass Mobilization Data Project Dataverse","url":"https://dataverse.harvard.edu/dataset.xhtml?persistentId=doi:10.7910/DVN/HTTWYL"},{"title":"Mass Mobilization Project - Political Science | Binghamton University","url":"https://www.binghamton.edu/political-science/massmobilization.html"}]

Based on the search results, I found information about the Mass Mobilization Project protest demand categories. The MM data itemize what protesters demand across as many as seven categories, including labor/wages, land, police brutality, political process, prices/taxes, removal of a politician, and social restrictions.

The search results reference the Principle Investigators for the Mass Mobilization project are David H. Clark (Binghamton University) and Patrick M. Regan (University of Notre Dame).

The complete codebook is available in the Mass Mobilizat
…[truncated 430 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_protest-dataset-search_20260520T092905",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool call

_source line 33 · 2026-05-20T09:35:08.153084+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "PolDem protest dataset 30 codebook \"action form\" categories list \"protest form\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_protest-dataset-search_20260520T092905",
  "tool": "WebSearch",
  "tool_args": {
    "query": "PolDem protest dataset 30 codebook \"action form\" categories list \"protest form\""
  }
}
```

</details>

---

### Tool result

_source line 34 · 2026-05-20T09:35:08.153240+00:00_

Web search results for query: "Mass Mobilization Project citation paper Clark Regan license terms of use Harvard Dataverse"

Links: [{"title":"DataCite Search","url":"https://search.datacite.org/works/10.7910/dvn/httwyl"},{"title":"Data innovations on protests in the United States - Cassy Dorff, Grace Adcox, Amanda Konet, 2023","url":"https://journals.sagepub.com/doi/abs/10.1177/00223433221143808"},{"title":"Data Sources","url":"https://reed-statistics.github.io/math141s21/project_data.html"},{"title":"Mass Mobilization dataset - Harvard Dataverse","url":"https://dataverse.harvard.edu/dataverse/MMdata"},{"title":"Review of Clark/Regan (2016): Mass Mobilization Project","url":"https://discuss-data.net/dataset/4e6a40ff-4ae0-4cc8-89b3-dbe162be07c0/"},{"title":"Mass Mobilization Data Project - Data Catalog","url":"https://datacatalog.library.wayne.edu/dataset/mass-mobilization-data-project"},{"title":"Mass Mobilization Data Project Codebook and User’s Manual David H. Clark","url":"https://reed-statistics.github.io/math141s21/projects/mass_mobilization/MM_codebook.pdf"},{"title":"Effect of Media Usage Selection on Social Mobilization Speed: Facebook vs E-Mail","url":"https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4589319/"},{"title":"Harvard Dataverse","url":"https://dataverse.harvard.edu/dataverse.xhtml?alias=MMdata"}]

Based on the search results, I found information about the Mass Mobilization Project:

The Mass Mobilization Data Project is authored by David Clark and Patrick Regan and was published in 2016 via Harvard Dataverse. The Principal Investigators for the Mass Mobilization project are David H. Clark (Binghamton University) and Patrick M. Regan (University of Notre Dame).

The Mass Mobilization (MM) data are an effort to understand citizen movements against governments, what citizens want when they demonstrate against governments, and how governments respond to citizens. The project codes protests against governments and the data cover 162 countries between 199
…[truncated 583 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_protest-dataset-search_20260520T092905",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool call

_source line 35 · 2026-05-20T09:35:08.153391+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "PolDem protest event dataset total number events observations sample size"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_protest-dataset-search_20260520T092905",
  "tool": "WebSearch",
  "tool_args": {
    "query": "PolDem protest event dataset total number events observations sample size"
  }
}
```

</details>

---

### Tool call

_source line 36 · 2026-05-20T09:35:08.153517+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"protest news classification dataset\" github huggingface download"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_protest-dataset-search_20260520T092905",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"protest news classification dataset\" github huggingface download"
  }
}
```

</details>

---

### Tool call

_source line 37 · 2026-05-20T09:35:08.153640+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "CLEF ProtestNews shared task dataset download \"event type\" classification"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_protest-dataset-search_20260520T092905",
  "tool": "WebSearch",
  "tool_args": {
    "query": "CLEF ProtestNews shared task dataset download \"event type\" classification"
  }
}
```

</details>

---

### Tool call

_source line 38 · 2026-05-20T09:35:08.153770+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "PolDem protest dataset \"creative commons\" OR \"CC BY\" OR license OR \"terms of use\" cite Kriesi Hutter"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_protest-dataset-search_20260520T092905",
  "tool": "WebSearch",
  "tool_args": {
    "query": "PolDem protest dataset \"creative commons\" OR \"CC BY\" OR license OR \"terms of use\" cite Kriesi Hutter"
  }
}
```

</details>

---

### Tool call

_source line 39 · 2026-05-20T09:35:08.153895+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "CASE shared task 2021 2022 \"socio-political event\" dataset download github"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_protest-dataset-search_20260520T092905",
  "tool": "WebSearch",
  "tool_args": {
    "query": "CASE shared task 2021 2022 \"socio-political event\" dataset download github"
  }
}
```

</details>

---

### Tool call

_source line 40 · 2026-05-20T09:35:08.154014+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "site:dataverse.harvard.edu \"Mass Mobilization\" license CC0 terms download"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_protest-dataset-search_20260520T092905",
  "tool": "WebSearch",
  "tool_args": {
    "query": "site:dataverse.harvard.edu \"Mass Mobilization\" license CC0 terms download"
  }
}
```

</details>

---

### Tool call

_source line 41 · 2026-05-20T09:35:08.154133+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"Mass Mobilization\" protest data sample size number of events rows 10000 17000"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_protest-dataset-search_20260520T092905",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"Mass Mobilization\" protest data sample size number of events rows 10000 17000"
  }
}
```

</details>

---

### Tool call

_source line 42 · 2026-05-20T09:35:08.154275+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "SPEED \"Social Political Economic Event Database\" dataset download NLP"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_protest-dataset-search_20260520T092905",
  "tool": "WebSearch",
  "tool_args": {
    "query": "SPEED \"Social Political Economic Event Database\" dataset download NLP"
  }
}
```

</details>

---

### Tool result

_source line 43 · 2026-05-20T09:35:08.154400+00:00_

Web search results for query: "PolDem protest event dataset total number events observations sample size"

Links: [{"title":"1 PolDem – Protest Dataset 30 European countries - Version 1 -","url":"https://poldem.eui.eu/downloads/pea/poldem-protest_30_codebook.pdf"},{"title":"1 PolDem – Protest Event Dataset 30 - Version 1 - Please cite as:","url":"https://poldem.eui.eu/downloads/pea/PEA_documentation_v1.pdf"},{"title":"1 PolDem – Protest Dataset on EU Issues - Version 1 - poldem-protest_eu","url":"https://poldem.eui.eu/downloads/pea/poldem-protest_eu_codebook.pdf"},{"title":"Data Portal on Political Conflict and Democracy in Europe (PolDem) | WZB","url":"https://www.wzb.eu/en/research/dynamics-of-political-systems/center-for-civil-society-research/projects/daten-portal-zu-politischen-konflikten-und-protest-in-europa"},{"title":"PolDem - Observatory for Political Conflict and Democracy in Europe","url":"https://poldem.eui.eu/"},{"title":"PolDem - Observatory for Political Conflict and Democracy in Europe • Political Sociology • Department of Political and Social Sciences","url":"https://www.polsoz.fu-berlin.de/en/soziologie/arbeitsbereiche/politische-soziologie/ressourcen/research/dataportal.html"},{"title":"Full article: Local protest event analysis: providing a more comprehensive picture?","url":"https://www.tandfonline.com/doi/full/10.1080/01402382.2024.2363709"},{"title":"How to Capture Global Protest Trends: Using Survey Data Recycling Data to Construct Cross-National Trends in Protest - J. Craig Jenkins, Joonghyun Kwak, 2022","url":"https://journals.sagepub.com/doi/full/10.1177/00027642211021627"}]

Based on the search results, I found information about the PolDem protest event dataset. However, the search results don't contain a specific total number of events or sample size. The documents reference the dataset covering protest events in 30 European countries obtained by coding media coverage, and the data covers the years 2000–2020.

One specific reference men
…[truncated 720 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_protest-dataset-search_20260520T092905",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 44 · 2026-05-20T09:35:08.154544+00:00_

Web search results for query: "PolDem protest dataset 30 codebook "action form" categories list "protest form""

Links: [{"title":"1 PolDem – Protest Event Dataset 30 - Version 1 - Please cite as:","url":"https://poldem.eui.eu/downloads/pea/PEA_documentation_v1.pdf"},{"title":"1 PolDem – Protest Dataset 30 European countries - Version 1 -","url":"https://poldem.eui.eu/downloads/pea/poldem-protest_30_codebook.pdf"},{"title":"1 PolDem – Protest Dataset on EU Issues - Version 1 - poldem-protest_eu","url":"https://poldem.eui.eu/downloads/pea/poldem-protest_eu_codebook.pdf"},{"title":"Data Portal on Political Conflict and Democracy in Europe (PolDem) | WZB","url":"https://www.wzb.eu/en/research/dynamics-of-political-systems/center-for-civil-society-research/projects/daten-portal-zu-politischen-konflikten-und-protest-in-europa"},{"title":"Observatory for Political Conflict and Democracy in Europe","url":"https://discuss-data.net/dataset/c7e7af8f-fa6f-46d3-8ae5-41a4aad6e4b9/"},{"title":"PolDem – Protest Dataset 30 European countries - Vrije Universiteit Amsterdam","url":"https://research.vu.nl/en/datasets/poldem-protest-dataset-30-european-countries"},{"title":"PolDem - Observatory for Political Conflict and Democracy in Europe","url":"https://poldem.eui.eu/"},{"title":"PolDem - Observatory for Political Conflict and Democracy in Europe • Political Sociology • Department of Political and Social Sciences","url":"https://www.polsoz.fu-berlin.de/en/soziologie/arbeitsbereiche/politische-soziologie/ressourcen/research/dataportal.html"}]

I found relevant resources for the PolDem Protest Dataset 30. The search results include links to the official codebook PDF (https://poldem.eui.eu/downloads/pea/poldem-protest_30_codebook.pdf) and documentation that contain information about the dataset structure.

Based on the search results, the dataset includes various protest-related activities such as petitions, campaigns, protests, demonstrations, marches, parades, rallies, pickets, human
…[truncated 755 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_protest-dataset-search_20260520T092905",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 45 · 2026-05-20T09:35:08.154689+00:00_

Web search results for query: "site:dataverse.harvard.edu "Mass Mobilization" license CC0 terms download"

Links: [{"title":"Mass Mobilization dataset - Harvard Dataverse","url":"https://dataverse.harvard.edu/dataverse/MMdata"},{"title":"Mass Mobilization Protest Data - Mass Mobilization Data Project Dataverse","url":"https://dataverse.harvard.edu/dataset.xhtml?persistentId=doi:10.7910/DVN/HTTWYL"},{"title":"Replication Data for: Unpopular Protest: Mass Mobilization and Attitudes to Democracy in Post-Mubarak Egypt - The Journal of Politics Dataverse","url":"https://dataverse.harvard.edu/dataset.xhtml;jsessionid=05dd6f02a13e27718e597bbbabd5?persistentId=doi:10.7910/DVN/NDHKSG&fileSortField=date&fileSortOrder=desc"},{"title":"Replication Data for: Regime Transformation From Below: Mobilization for Democracy and Autocracy From 1900 to 2021 - Comparative Political Studies Dataverse","url":"https://dataverse.harvard.edu/dataset.xhtml?persistentId=doi:10.7910/DVN/YQPN8D"},{"title":"Measuring and Predicting Speed of Social Mobilization","url":"https://arxiv.org/pdf/1303.3805"},{"title":"Effect of Media Usage Selection on Social Mobilization Speed: Facebook vs E-Mail","url":"https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4589319/"},{"title":"Homophily and the Speed of Social Mobilization: The Effect of Acquired   and Ascribed Traits","url":"https://arxiv.org/pdf/1404.6935"},{"title":"Homophily and the Speed of Social Mobilization: The Effect of Acquired and Ascribed Traits","url":"https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3989266/"}]

I found the search results for the Mass Mobilization dataset on Harvard Dataverse. Here's what I found:

The Mass Mobilization (MM) data are an effort to understand citizen movements against governments, what citizens want when they demonstrate against governments, and how governments respond to citizens. The Mass Mobilization Data project covers protests against governments across all countries from 1990-2020.

The main dataset appears to be
…[truncated 600 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_protest-dataset-search_20260520T092905",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 46 · 2026-05-20T09:35:08.154843+00:00_

Web search results for query: ""protest news classification dataset" github huggingface download"

Links: [{"title":"[Dataset requests] New datasets for Text Classification · Issue #353 · huggingface/datasets","url":"https://github.com/huggingface/datasets/issues/353"},{"title":"elnazrezaee/News-Classification-Dataset · Datasets at Hugging Face","url":"https://huggingface.co/datasets/elnazrezaee/News-Classification-Dataset"},{"title":"valurank/PoliticalBias · Datasets at Hugging Face","url":"https://huggingface.co/datasets/valurank/PoliticalBias"},{"title":"huggingface-datasets · GitHub Topics · GitHub","url":"https://github.com/topics/huggingface-datasets"},{"title":"okite97/news-data · Datasets at Hugging Face","url":"https://huggingface.co/datasets/okite97/news-data"},{"title":"Hate-speech-CNERG/hatexplain · Datasets at Hugging Face","url":"https://huggingface.co/datasets/Hate-speech-CNERG/hatexplain"},{"title":"AiresPucrs/News-Category-Dataset · Datasets at Hugging Face","url":"https://huggingface.co/datasets/AiresPucrs/News-Category-Dataset"},{"title":"Datasets – Hugging Face","url":"https://huggingface.co/datasets"},{"title":"Build software better, together","url":"https://github.com/topics/hate-speech-detection"},{"title":"mteb/NewsClassification · Datasets at Hugging Face","url":"https://huggingface.co/datasets/mteb/NewsClassification"}]

Based on the search results, I found several news classification datasets available on Hugging Face, though I didn't find a specific "protest news classification dataset." Here are the relevant resources:

## News Classification Datasets on Hugging Face:

1. **News-Classification-Dataset** - Available at elnazrezaee/News-Classification-Dataset on Hugging Face

2. **News-Category-Dataset** - The AiresPucrs/News-Category-Dataset can be loaded using: `from datasets import load_dataset` and `dataset = load_dataset("AiresPucrs/News-Category-Dataset", split = 'train')`

3. **News-Data** - The okite97/news-data dataset supports ne
…[truncated 921 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_protest-dataset-search_20260520T092905",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 47 · 2026-05-20T09:35:08.154984+00:00_

Web search results for query: ""Mass Mobilization" protest data sample size number of events rows 10000 17000"

Links: [{"title":"Mass Mobilization Project tracks protests around the world - Binghamton News","url":"https://www.binghamton.edu/news/story/3282/hit-the-streets-mass-mobilization-project-tracks-protests-around-the-world"},{"title":"About the Mass Mobilization Project","url":"https://massmobilization.github.io/about.html"},{"title":"Mass Mobilization Data Project Dataverse","url":"https://dataverse.harvard.edu/dataverse/MMdata"},{"title":"Mass Mobilization Protest Data - Mass Mobilization Data Project Dataverse","url":"https://dataverse.harvard.edu/dataset.xhtml?persistentId=doi:10.7910/DVN/HTTWYL"},{"title":"Mass Mobilization and Regime Change. Evidence From a New Measure of","url":"https://v-dem.net/media/publications/Working_Paper_128_final.pdf"},{"title":"Mass Mobilization in Autocracies Database","url":"https://mmadatabase.org/"},{"title":"Full article: Episodes of sustained protest: temporal patterns of online mobilization on X","url":"https://www.tandfonline.com/doi/full/10.1080/1369118X.2025.2585094"},{"title":"The Mass Mobilization Project","url":"https://massmobilization.github.io/"},{"title":"Data - PLSC 410: Political Protests - Yale University Library Research Guides at Yale University","url":"https://guides.library.yale.edu/c.php?g=956915&p=6961578"},{"title":"Few-Shot Upsampling for Protest Size Detection","url":"https://arxiv.org/pdf/2105.11260"}]

Based on the search results, I found information about the Mass Mobilization Project protest dataset:

The Mass Mobilization data contain events where 50 or more protesters publicly demonstrate against government, resulting in more than 10,000 protest events. More specifically, the data covers more than 15,000 events since 1990.

The MM data cover 162 countries between 1990 and 2018. Each event records location, protest size, protester demands, and government responses.

So the sample size falls 
…[truncated 248 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_protest-dataset-search_20260520T092905",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 48 · 2026-05-20T09:35:08.155131+00:00_

Web search results for query: "CLEF ProtestNews shared task dataset download "event type" classification"

Links: [{"title":"(PDF) Overview of CLEF 2019 Lab ProtestNews: Extracting Protests from News in a Cross-Context Setting","url":"https://www.researchgate.net/publication/335551147_Overview_of_CLEF_2019_Lab_ProtestNews_Extracting_Protests_from_News_in_a_Cross-Context_Setting"},{"title":"(PDF) Extraction of political event data from news articles in a cross-context setting","url":"https://www.academia.edu/40865598/Extraction_of_political_event_data_from_news_articles_in_a_cross_context_setting"},{"title":"(PDF) Automated Extraction of Socio-political Events from News (AESPEN): Workshop and Shared Task Report","url":"https://www.researchgate.net/publication/341369381_Automated_Extraction_of_Socio-political_Events_from_News_AESPEN_Workshop_and_Shared_Task_Report"},{"title":"(PDF) Multilingual Protest News Detection - Shared Task 1, CASE 2021","url":"https://www.academia.edu/64931265/Multilingual_Protest_News_Detection_Shared_Task_1_CASE_2021"},{"title":"IIITT at CASE 2021 Task 1: Leveraging Pretrained ...","url":"https://aclanthology.org/2021.case-1.13.pdf"},{"title":"Cross-Context News Corpus for Protest Event-Related Knowledge Base Construction | Data Intelligence | MIT Press","url":"https://direct.mit.edu/dint/article/3/2/308/100736/Cross-Context-News-Corpus-for-Protest-Event"},{"title":"Multitask Models for Supervised Protests Detection in Texts","url":"https://arxiv.org/pdf/2005.02954"},{"title":"Event Coreference Resolution for Contentious Politics Events","url":"https://arxiv.org/pdf/2203.10123"}]

Based on the search results, I found information about the CLEF ProtestNews shared task dataset:

## Overview

The CLEF 2019 Lab ProtestNews presented an overview on Extracting Protests from News in the context of generalizable natural language processing. The lab consisted of document, sentence, and token level information classification and extraction tasks.

## 
…[truncated 1069 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_protest-dataset-search_20260520T092905",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 49 · 2026-05-20T09:35:08.155298+00:00_

Web search results for query: "CASE shared task 2021 2022 "socio-political event" dataset download github"

Links: [{"title":"Call for Papers and Shared Task Participation (CASE @ EMNLP 2022): Challenges and Applications of Automated Extraction of Socio-political Events from Text","url":"https://groups.google.com/g/ml-news/c/24ZK--jfhV8"},{"title":"Final Call for Papers and Shared Task Participation (CASE @ EMNLP 2022): Challenges and Applications of Automated Extraction of Socio-political Events from Text | ACL Member Portal","url":"https://www.aclweb.org/portal/content/final-call-papers-and-shared-task-participation-case-emnlp-2022-challenges-and-applications"},{"title":"GitHub - emerging-welfare/case-2021-shared-task: Information and data related to the ProtestNews shared task at CASE @ ACL-IJCNLP 2021 workshop","url":"https://github.com/emerging-welfare/case-2021-shared-task"},{"title":"Call for Papers and Shared Task Participation (CASE @ EMNLP 2022): Challenges and Applications of Automated Extraction of Socio-political Events from Text | ACL Member Portal","url":"https://www.aclweb.org/portal/content/call-papers-and-shared-task-participation-case-emnlp-2022-challenges-and-applications"},{"title":"GitHub - furkan-celik/CASE21-SuNLP-Models: Models developed for task 1 of CASE21 by SuNLP Team · GitHub","url":"https://github.com/furkan-celik/CASE21-SuNLP-Models"},{"title":"Challenges and Applications of Automated Extraction of Socio-political   Events from Text (CASE 2021): Workshop and Shared Task Report","url":"https://arxiv.org/pdf/2108.07865"},{"title":"Challenges and Applications of Automated Extraction of Socio-political   Events from Text (CASE 2022): Workshop and Shared Task Report","url":"https://arxiv.org/pdf/2211.11359"}]

Based on the search results, here's what I found about the CASE shared task datasets for 2021-2022:

## CASE Shared Task Overview

The CASE workshop organized a Socio-political and Crisis Events Detection shared task at ACL-IJCNLP 20
…[truncated 901 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_protest-dataset-search_20260520T092905",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 50 · 2026-05-20T09:35:08.155455+00:00_

Web search results for query: "SPEED "Social Political Economic Event Database" dataset download NLP"

Links: [{"title":"Social Political Economic Event Dataset (SPEED): Liberia, Philippines, and Sierra Leone (1979-2008). Cline Center for Advanced Social Research. V1.0.0. August 29 - Illinois Experts","url":"https://experts.illinois.edu/en/datasets/social-political-economic-event-dataset-speed-liberia-philippines-2/"},{"title":"The Social, Political and Economic Event Database Project ...","url":"https://discuss-data.net/dataset/a47d51a9-6c5f-4bc4-827b-b310b083481e/"},{"title":"Social Political Economic Event Dataset (SPEED): Liberia ...","url":"https://databank.illinois.edu/datasets/IDB-7407320"},{"title":"Social, Political and Economic Event Database (SPEED) Project Data.","url":"https://staffblogs.le.ac.uk/socscilibrarians/2014/05/12/social-political-and-economic-event-database-speed-project-data/"},{"title":"(PDF) Social Political Economic Event Dataset (SPEED): Liberia, Philippines, and Sierra Leone (1979-2008) Codebook (v.1.0.0) About the Cline Center for Advanced Social Research | Dan Shalmon - Academia.edu","url":"https://www.academia.edu/40213536/Social_Political_Economic_Event_Dataset_SPEED_Liberia_Philippines_and_Sierra_Leone_1979_2008_Codebook_v_1_0_0_About_the_Cline_Center_for_Advanced_Social_Research"},{"title":"The Social, Political and Economic Event Database Project (SPEED) | Cline Center","url":"https://clinecenter.illinois.edu/project/human-loop-event-data-projects/SPEED"},{"title":"Data Download • Data on Armed Conflict and Security","url":"https://www.conflict-data.org/edacs/downloads/index.html"},{"title":"Distributions of Recorded Pain in Mental Health Records: A Natural Language Processing Based Study","url":"https://www.medrxiv.org/content/10.1101/2023.09.15.23295064.full.pdf"},{"title":"Automated Extraction of Mortality Information from Publicly Available Sources Using Language Models","url":"https://www.medrxiv.org/content/10.1101/2024.10.
…[truncated 1393 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_protest-dataset-search_20260520T092905",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool call

_source line 51 · 2026-05-20T09:35:08.155605+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Mass Mobilization Project codebook protester demand categories \"labor\" \"land\" \"police brutality\" \"political\" \"prices\" \"removal\" \"social\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_protest-dataset-search_20260520T092905",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Mass Mobilization Project codebook protester demand categories \"labor\" \"land\" \"police brutality\" \"political\" \"prices\" \"removal\" \"social\""
  }
}
```

</details>

---

### Tool call

_source line 52 · 2026-05-20T09:35:08.155734+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Clark Regan \"Mass Mobilization\" journal paper citation 2016 2018 \"International Interactions\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_protest-dataset-search_20260520T092905",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Clark Regan \"Mass Mobilization\" journal paper citation 2016 2018 \"International Interactions\""
  }
}
```

</details>

---

### Tool call

_source line 53 · 2026-05-20T09:35:08.155866+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Indian protest event dataset NLP annotation \"event type\" classification download"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_protest-dataset-search_20260520T092905",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Indian protest event dataset NLP annotation \"event type\" classification download"
  }
}
```

</details>

---

### Tool call

_source line 54 · 2026-05-20T09:35:08.155992+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "GLOCON \"Global Contentious Politics\" dataset download categories event types"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_protest-dataset-search_20260520T092905",
  "tool": "WebSearch",
  "tool_args": {
    "query": "GLOCON \"Global Contentious Politics\" dataset download categories event types"
  }
}
```

</details>

---

### Tool call

_source line 55 · 2026-05-20T09:35:08.156113+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "huggingface dataset protest event classification \"event type\" categories"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_protest-dataset-search_20260520T092905",
  "tool": "WebSearch",
  "tool_args": {
    "query": "huggingface dataset protest event classification \"event type\" categories"
  }
}
```

</details>

---

### Tool result

_source line 56 · 2026-05-20T09:35:08.156272+00:00_

Web search results for query: "PolDem protest dataset "creative commons" OR "CC BY" OR license OR "terms of use" cite Kriesi Hutter"

Links: [{"title":"PolDem - Observatory for Political Conflict and Democracy in Europe","url":"https://poldem.eui.eu/"},{"title":"PolDem – Protest Dataset 30 European countries - Vrije Universiteit Amsterdam","url":"https://research.vu.nl/en/datasets/poldem-protest-dataset-30-european-countries"},{"title":"1 PolDem – Protest Dataset on EU Issues - Version 1 - poldem-protest_eu","url":"https://poldem.eui.eu/downloads/pea/poldem-protest_eu_codebook.pdf"},{"title":"GitHub - davidpomerenke/german-protest-registrations: Dataset on demonstrations in Germany","url":"https://github.com/davidpomerenke/german-protest-registrations"},{"title":"Data Portal on Political Conflict and Democracy in Europe (PolDem) | WZB","url":"https://www.wzb.eu/en/research/dynamics-of-political-systems/center-for-civil-society-research/projects/daten-portal-zu-politischen-konflikten-und-protest-in-europa"},{"title":"Databases | WZB","url":"https://www.wzb.eu/en/publications/databases"},{"title":"1 PolDem – Protest Event Dataset 30 - Version 1 - Please cite as:","url":"https://poldem.eui.eu/downloads/pea/PEA_codebook_v1.pdf"},{"title":"News - PolDem","url":"https://poldem.eui.eu/news/"},{"title":"1 PolDem – Protest Dataset 30 European countries - Version 1 -","url":"https://poldem.eui.eu/downloads/pea/poldem-protest_30_codebook.pdf"},{"title":"Platform for Protest and Conflict in Europe | WZB","url":"https://www.wzb.eu/en/news/platform-for-protest-and-conflict-in-europe"}]

Let me search more specifically for the licensing and terms of use information for the PolDem dataset.

Links: [{"title":"Data - Creative Commons","url":"https://wiki.creativecommons.org/wiki/data"},{"title":"Common license types for datasets and what they mean - Get Help","url":"https://libanswers.ucalgary.ca/faq/200582"},{"title":"Common license types for datasets - Documentation","url":"https:/
…[truncated 4886 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_protest-dataset-search_20260520T092905",
  "tool": "WebSearch",
  "elapsed_ms": 2
}
```

</details>

---

### Tool result

_source line 57 · 2026-05-20T09:35:08.156420+00:00_

Web search results for query: "Clark Regan "Mass Mobilization" journal paper citation 2016 2018 "International Interactions""

Links: [{"title":"MMD (Mass Mobilization Database) from Clark and Regan (2018): 166... | Download Scientific Diagram","url":"https://www.researchgate.net/figure/MMD-Mass-Mobilization-Database-from-Clark-and-Regan-2018-166-countries-across-South_fig1_352664331"},{"title":"Dynamics of Political Protests | International Organization | Cambridge Core","url":"https://www.cambridge.org/core/journals/international-organization/article/abs/dynamics-of-political-protests/FF34963F17453C36ACC88B5C880E156D"},{"title":"Review of Clark/Regan (2016): Mass Mobilization Project","url":"https://discuss-data.net/dataset/4e6a40ff-4ae0-4cc8-89b3-dbe162be07c0/"},{"title":"Mass Mobilization dataset - Harvard Dataverse","url":"https://dataverse.harvard.edu/dataverse/MMdata"},{"title":"Mass Mobilization Project - Political Science | Binghamton University","url":"https://www.binghamton.edu/massmobilization/about.html"},{"title":"Homophily and the Speed of Social Mobilization: The Effect of Acquired   and Ascribed Traits","url":"https://arxiv.org/pdf/1404.6935"},{"title":"DataCite Search","url":"https://search.datacite.org/works/10.7910/dvn/httwyl"},{"title":"About the Mass Mobilization Project","url":"https://massmobilization.github.io/about.html"},{"title":"Measuring and Predicting Speed of Social Mobilization","url":"https://arxiv.org/pdf/1303.3805"}]

Based on the search results, I found information about the Clark and Regan Mass Mobilization project:

Clark and Regan published Mass Mobilization Data in 2016. The MM data cover 162 countries between 1990 and 2018 and contain events where 50 or more protesters publicly demonstrate against government, resulting in more than 10,000 protest events, with each event recording location, protest size, protester demands, and government responses.

The dataset was published in 2016 via Harvard Dataverse. However, the search 
…[truncated 514 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_protest-dataset-search_20260520T092905",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 58 · 2026-05-20T09:35:08.156570+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "poldem protest dataset discuss-data.net license access"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_protest-dataset-search_20260520T092905",
  "tool": "WebSearch",
  "tool_args": {
    "query": "poldem protest dataset discuss-data.net license access"
  }
}
```

</details>

---

### Tool call

_source line 59 · 2026-05-20T09:35:08.156710+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "ACLED \"Armed Conflict Location Event Data\" text classification NLP dataset public download categories"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_protest-dataset-search_20260520T092905",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ACLED \"Armed Conflict Location Event Data\" text classification NLP dataset public download categories"
  }
}
```

</details>

---

### Tool call

_source line 60 · 2026-05-20T09:35:08.156838+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "PolDem protest 30 dataset \"issue\" categories \"action_form\" number of events N= observations"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_protest-dataset-search_20260520T092905",
  "tool": "WebSearch",
  "tool_args": {
    "query": "PolDem protest 30 dataset \"issue\" categories \"action_form\" number of events N= observations"
  }
}
```

</details>

---

### Tool result

_source line 61 · 2026-05-20T09:35:08.156965+00:00_

Web search results for query: "Mass Mobilization Project codebook protester demand categories "labor" "land" "police brutality" "political" "prices" "removal" "social""

Links: [{"title":"Data Sources","url":"https://reed-statistics.github.io/math141s21/project_data.html"},{"title":"Mass Mobilization Data Project Codebook and User’s Manual David H. Clark","url":"https://reed-statistics.github.io/math141s21/projects/mass_mobilization/MM_codebook.pdf"},{"title":"About the Mass Mobilization Project","url":"https://massmobilization.github.io/about.html"},{"title":"Mass Mobilization Data Project - Data Catalog","url":"https://datacatalog.library.wayne.edu/dataset/mass-mobilization-data-project"},{"title":"Review of Clark/Regan (2016): Mass Mobilization Project","url":"https://discuss-data.net/dataset/4e6a40ff-4ae0-4cc8-89b3-dbe162be07c0/"},{"title":"Mass Mobilization Data Project Dataverse","url":"https://dataverse.harvard.edu/dataverse/MMdata"},{"title":"Mass Mobilization in the Modern Era: Introducing the Opposition Movements and Groups (OMG) Dataset, 1789–2019 - Marianne Dahl, Sirianne Dahlum, Hanne Fjelde, Haakon Gjerløw, Carl Henrik Knutsen, Carina Strøm-Sedgwick, Tore Wig, 2025","url":"https://journals.sagepub.com/doi/10.1177/00104140251369330"},{"title":"The Mass Mobilization Project","url":"https://massmobilization.github.io/"},{"title":"Full article: Episodes of sustained protest: temporal patterns of online mobilization on X","url":"https://www.tandfonline.com/doi/full/10.1080/1369118X.2025.2585094"}]

I found information about the Mass Mobilization Project codebook and its protester demand categories. Here's what the search revealed:

The Mass Mobilization Project identifies seven categories of protester demands that describe the types of issues that motivate protest behavior. For each event, the MM data itemize what protesters demand across these seven categories, including labor/wages, land, police brutality, political process, prices/taxes, removal of a pol
…[truncated 957 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_protest-dataset-search_20260520T092905",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 62 · 2026-05-20T09:35:08.157121+00:00_

Web search results for query: "GLOCON "Global Contentious Politics" dataset download categories event types"

Links: [{"title":"New Dataset Collects Instances of 'Contentious Politics ...","url":"https://www.socialsciencespace.com/2023/12/new-dataset-collects-instances-of-contentious-politics-around-the-world/"},{"title":"Global Contentious Politics Dataset (GLOCON)","url":"https://glocon.ku.edu.tr/"},{"title":"Global Contentious Politics Database (GLOCON) Annotation Manuals","url":"https://zenodo.org/records/6540579"},{"title":"[PDF] Global Contentious Politics Database (GLOCON ...","url":"https://www.semanticscholar.org/paper/Global-Contentious-Politics-Database-(GLOCON)-Duru%C5%9Fan-Hurriyetoglu/dd035f2dc20a8aa29d33b31a293d7d3eebd0852c"},{"title":"(PDF) Global Contentious Politics Database (GLOCON) Annotation Manuals","url":"https://www.academia.edu/79307023/Global_Contentious_Politics_Database_GLOCON_Annotation_Manuals"},{"title":"Global Contentious Politics Dataset (GLOCON) - YouTube","url":"https://www.youtube.com/watch?v=NLHUjYXUSu0"},{"title":"Global Contentious Politics Database (GLOCON) Annotation Manuals","url":"https://explore.openaire.eu/search/other?pid=10.5281/zenodo.6540579"},{"title":"Global Contentious Politics Database (GLOCON) Annotation Manuals | Zenodo","url":"https://zenodo.org/record/6540579/export/hx"},{"title":"[2206.10299] Global Contentious Politics Database (GLOCON) Annotation Manuals","url":"https://arxiv.org/abs/2206.10299"},{"title":"Emerging Markets Welfare – Data","url":"https://emw.ku.edu.tr/data/"}]

Based on the search results, here's information about the GLOCON dataset:

## Overview
GLOCON is the first multi-country protest event database for the Global South that uses local sources for automated data collection. The database features event data for India, Brazil, South Africa, Turkey, and Argentina.

## Event Types
GLOCON records diverse types of events, including but not limited to demonstrations, rallies, strikes, clashes, a
…[truncated 818 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_protest-dataset-search_20260520T092905",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool call

_source line 63 · 2026-05-20T09:35:08.157290+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Harvard Dataverse doi:10.7910/DVN/HTTWYL license \"CC0\" OR \"public domain\" OR \"terms of use\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_protest-dataset-search_20260520T092905",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Harvard Dataverse doi:10.7910/DVN/HTTWYL license \"CC0\" OR \"public domain\" OR \"terms of use\""
  }
}
```

</details>

---

### Tool result

_source line 64 · 2026-05-20T09:35:08.157420+00:00_

Web search results for query: "huggingface dataset protest event classification "event type" categories"

Links: [{"title":"Introductory Guide to using HuggingFace for your Modelling Needs | by Louis D'hulst | Medium","url":"https://medium.com/@louisdhulst/introductory-guide-to-using-huggingface-for-your-modelling-needs-e4e9907cf6b4"},{"title":"Methodology of the dataset of detentions at protests from 2012 to 2023 | OVD-Info","url":"https://ovd.info/en/methodology-dataset-detentions-protests-2012-2023"},{"title":"QCRI/HumAID-event-type · Datasets at Hugging Face","url":"https://huggingface.co/datasets/QCRI/HumAID-event-type"},{"title":"Deep Learning based Multi-Label Image Classification of Protest   Activities","url":"https://arxiv.org/pdf/2301.04212"},{"title":"Protest Activity Detection and Perceived Violence Estimation from Social   Media Images","url":"https://arxiv.org/pdf/1709.06204"},{"title":"Ontology-driven Event Type Classification in Images","url":"https://arxiv.org/pdf/2011.04714"}]

Based on the search results, I found relevant information about HuggingFace datasets and protest event classification:

## HuggingFace Event Classification Datasets

The search results reveal several relevant datasets available on HuggingFace for event classification:

1. **HumAID-event-type Dataset**: The HumAID Twitter dataset consists of several thousands of manually annotated tweets collected during 19 major natural disaster events including earthquakes, hurricanes, wildfires, and floods from 2016 to 2019. The resulting annotated dataset consists of 11 labels.

2. **Protest Activity Detection**: The UCLA Protest Image Dataset consists of 40,764 images (11,659 protest images and hard negatives) with various annotations of visual attributes and sentiments.

## Event Type Categories for Protest Events

For protest event classification specifically, research has identified several categorization approaches:

- **Event Organizer Types**: Institutional protest is a category o
…[truncated 607 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_protest-dataset-search_20260520T092905",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 65 · 2026-05-20T09:35:08.157573+00:00_

Web search results for query: "Indian protest event dataset NLP annotation "event type" classification download"

Links: [{"title":"arXiv:2008.00351v1 [cs.CL] 1 Aug 2020","url":"https://arxiv.org/pdf/2008.00351"},{"title":"Cross-context News Corpus for Protest Events related ...","url":"https://openreview.net/pdf?id=7NZkNhLCjp"},{"title":"Enhancing Event Extraction from Short Stories through Contextualized Prompts","url":"https://arxiv.org/html/2412.10745"},{"title":"1 PolDem – Protest Event Dataset 30 - Version 1 - Please cite as:","url":"https://poldem.eui.eu/downloads/pea/PEA_documentation_v1.pdf"},{"title":"Fine-grained Narrative Classification in Biased News Articles","url":"https://www.arxiv.org/pdf/2512.03582"},{"title":"Protest Event Analysis: Developing a Semiautomated NLP Approach - Jasmine Lorenzini, Hanspeter Kriesi, Peter Makarov, Bruno Wüest, 2022","url":"https://journals.sagepub.com/doi/10.1177/00027642211021650"},{"title":"(PDF) Protest Event Analysis: Developing a Semiautomated NLP Approach","url":"https://www.researchgate.net/publication/352087597_Protest_Event_Analysis_Developing_a_Semiautomated_NLP_Approach"},{"title":"(PDF) NSUT-NLP at CASE 2022 Task 1: Multilingual Protest Event Detection using Transformer-based Models","url":"https://www.academia.edu/110108255/NSUT_NLP_at_CASE_2022_Task_1_Multilingual_Protest_Event_Detection_using_Transformer_based_Models"}]

Based on the search results, here are the relevant findings about Indian protest event datasets with NLP annotation for event type classification:

## Key Datasets Found

Content from Indian Express (IEX), New Indian Express (NIEX), The Hindu (TH), Times of India (ToI) and other sources has been downloaded for labelling and annotation for protest event analysis.

Terms like "bandh" and "idol immersion" are event types that are specific to India and not covered by any general-purpose protest key terms list, highlighting the importance of India-specific datasets for protest event classifica
…[truncated 1046 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_protest-dataset-search_20260520T092905",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool call

_source line 66 · 2026-05-20T09:35:08.157722+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Clark Regan \"Mass Mobilization in Civil War\" OR \"Mass Mobilization\" protest dataset journal article published"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_protest-dataset-search_20260520T092905",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Clark Regan \"Mass Mobilization in Civil War\" OR \"Mass Mobilization\" protest dataset journal article published"
  }
}
```

</details>

---

### Tool result

_source line 67 · 2026-05-20T09:35:08.157854+00:00_

Web search results for query: "PolDem protest 30 dataset "issue" categories "action_form" number of events N= observations"

Links: [{"title":"1 PolDem – Protest Dataset 30 European countries - Version 1 -","url":"https://poldem.eui.eu/downloads/pea/poldem-protest_30_codebook.pdf"},{"title":"1 PolDem – Protest Event Dataset 30 - Version 1 - Please cite as:","url":"https://poldem.eui.eu/downloads/pea/PEA_documentation_v1.pdf"},{"title":"PolDem - Observatory for Political Conflict and Democracy in Europe","url":"https://poldem.eui.eu/"},{"title":"1 PolDem – Protest Dataset on EU Issues - Version 1 - poldem-protest_eu","url":"https://poldem.eui.eu/downloads/pea/poldem-protest_eu_codebook.pdf"},{"title":"PolDem - Observatory for Political Conflict and Democracy in Europe • Political Sociology • Department of Political and Social Sciences","url":"https://www.polsoz.fu-berlin.de/en/soziologie/arbeitsbereiche/politische-soziologie/ressourcen/research/dataportal.html"},{"title":"Data Portal on Political Conflict and Democracy in Europe (PolDem) | WZB","url":"https://www.wzb.eu/en/research/dynamics-of-political-systems/center-for-civil-society-research/projects/daten-portal-zu-politischen-konflikten-und-protest-in-europa"},{"title":"News - PolDem","url":"https://poldem.eui.eu/news/"},{"title":"Full article: Local protest event analysis: providing a more comprehensive picture?","url":"https://www.tandfonline.com/doi/full/10.1080/01402382.2024.2363709"}]

Based on the search results, I found information about the PolDem Protest 30 dataset and its variables. Here's what the search results reveal:

Peaceful demonstrations are most prevalent among the different action forms (indicator: 'action_form'), and violent protests and strikes are rather frequent as well, but nevertheless, their share is less than half than the share of demonstrations.

The dataset includes variables for action forms, issues and actors. The codebook and documentation files reference tables that describe th
…[truncated 695 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_protest-dataset-search_20260520T092905",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 68 · 2026-05-20T09:35:08.157998+00:00_

Web search results for query: "poldem protest dataset discuss-data.net license access"

Links: [{"title":"1 PolDem – Protest Dataset on EU Issues - Version 1 - poldem-protest_eu","url":"https://poldem.eui.eu/downloads/pea/poldem-protest_eu_codebook.pdf"},{"title":"PolDem - Observatory for Political Conflict and Democracy in Europe","url":"https://poldem.eui.eu/"},{"title":"Discuss-data","url":"https://discuss-data.net/dataset/2cb6c216-7d34-4b94-9992-2748c5c6a110/"},{"title":"Review of the World Protests dataset","url":"https://zenodo.org/records/18484516"},{"title":"PolDem – Protest Dataset 30 European countries - Research output - Vrije Universiteit Amsterdam","url":"https://research.vu.nl/en/datasets/poldem-protest-dataset-30-european-countries/publications/"},{"title":"Data Portal on Political Conflict and Democracy in Europe (PolDem) | WZB","url":"https://www.wzb.eu/en/research/dynamics-of-political-systems/center-for-civil-society-research/projects/daten-portal-zu-politischen-konflikten-und-protest-in-europa"},{"title":"1 PolDem – Protest Event Dataset 30 - Version 1 - Please cite as:","url":"https://poldem.eui.eu/downloads/pea/PEA_documentation_v1.pdf"},{"title":"PolDem - Observatory for Political Conflict and Democracy in Europe • Political Sociology • Department of Political and Social Sciences","url":"https://www.polsoz.fu-berlin.de/en/soziologie/arbeitsbereiche/politische-soziologie/ressourcen/research/dataportal.html"}]

Based on the search results, here's what I found about the PolDem protest dataset:

## Overview

The Observatory for Political Conflict and Democracy (PolDem) is a platform that produces and maintains original data on protest events, election campaigns, and issue-specific public contestation covering Western, Southern, as well as Central-Eastern European countries over a large time-span.

## Dataset Details

The core of PolDem includes data on protest events in 30 European countries obtained by coding media coverage. The PolDem-Protest Da
…[truncated 927 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_protest-dataset-search_20260520T092905",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool call

_source line 69 · 2026-05-20T09:35:08.158143+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:WebFetch",
  "max_results": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_protest-dataset-search_20260520T092905",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:WebFetch",
    "max_results": "1"
  }
}
```

</details>

---

### Tool result

_source line 70 · 2026-05-20T09:35:08.158282+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_protest-dataset-search_20260520T092905",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 71 · 2026-05-20T09:35:08.158406+00:00_

Web search results for query: "Harvard Dataverse doi:10.7910/DVN/HTTWYL license "CC0" OR "public domain" OR "terms of use""

Links: [{"title":"Harvard Dataverse | Data Management","url":"https://datamanagement.hms.harvard.edu/share-publish/data-repositories/harvard-dataverse"},{"title":"Harvard Dataverse General Terms of Use — Dataverse.org","url":"http://best-practices.dataverse.org/harvard-policies/harvard-terms-of-use.html"},{"title":"Data Repositories | Data Management","url":"https://datamanagement.hms.harvard.edu/share-publish/data-repositories"},{"title":"General Terms of Use - Harvard Dataverse Support","url":"https://support.dataverse.harvard.edu/harvard-dataverse-general-terms-use"},{"title":"Dataverse Community Norms | The Dataverse Project","url":"https://dataverse.org/best-practices/dataverse-community-norms"},{"title":"Establishment of an open data policy for Journal of Educational Evaluation for Health Professions, appreciation for invited reviewers, and acknowledgement of volunteers who made audio recordings","url":"https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5801429/"},{"title":"A large-scale study on research code quality and execution","url":"https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8861064/"},{"title":"Multiple license update turned the terms of some datasets with only CC0 licenses into \"custom licenses\" · Issue #9081 · IQSS/dataverse","url":"https://github.com/IQSS/dataverse/issues/9081"}]

Based on the search results, I can provide you with information about Harvard Dataverse's licensing practices:

Harvard Dataverse's default data usage license agreement for all uploaded materials is a Creative Commons Zero ("CC0") Public Domain Dedication Waiver. Harvard Dataverse strongly encourages use of a Creative Commons Zero (CC0) waiver for all public datasets, but dataset owners can specify other terms of use and restrict access to data.

By default, all datasets added in a Dataverse repository are granted the CC0 Public Domain Dedication, as t
…[truncated 689 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_protest-dataset-search_20260520T092905",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 72 · 2026-05-20T09:35:08.158550+00:00_

Web search results for query: "Clark Regan "Mass Mobilization in Civil War" OR "Mass Mobilization" protest dataset journal article published"

Links: [{"title":"Dynamics of Political Protests | International Organization | Cambridge Core","url":"https://www.cambridge.org/core/journals/international-organization/article/abs/dynamics-of-political-protests/FF34963F17453C36ACC88B5C880E156D"},{"title":"Review of Clark/Regan (2016): Mass Mobilization Project","url":"https://discuss-data.net/dataset/4e6a40ff-4ae0-4cc8-89b3-dbe162be07c0/"},{"title":"DataCite Search","url":"https://search.datacite.org/works/10.7910/dvn/httwyl"},{"title":"Mass Mobilization Data Project - Data Catalog","url":"https://datacatalog.library.wayne.edu/dataset/mass-mobilization-data-project"},{"title":"Data Is Plural — 2020.08.26 edition","url":"https://www.data-is-plural.com/archive/2020-08-26-edition/"},{"title":"Mass Mobilization dataset - Harvard Dataverse","url":"https://dataverse.harvard.edu/dataverse/MMdata"},{"title":"MMD (Mass Mobilization Database) from Clark and Regan (2018): 166... | Download Scientific Diagram","url":"https://www.researchgate.net/figure/MMD-Mass-Mobilization-Database-from-Clark-and-Regan-2018-166-countries-across-South_fig1_352664331"},{"title":"Mass Mobilization Protest Data - Mass Mobilization Data Project Dataverse","url":"https://dataverse.harvard.edu/dataset.xhtml?persistentId=doi:10.7910/DVN/HTTWYL"},{"title":"About the Mass Mobilization Project","url":"https://massmobilization.github.io/about.html"}]

Based on the search results, I found information about Clark and Regan's Mass Mobilization Project:

The Mass Mobilization project is led by David H. Clark (Binghamton University) and Patrick M. Regan (University of Notre Dame). The project's dataset covers more than 14,000 protests in more than 160 countries between 1990 and early 2017.

The Mass Mobilization (MM) data are an effort to understand citizen movements against governments, what citizens want when they d
…[truncated 677 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_protest-dataset-search_20260520T092905",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 73 · 2026-05-20T09:35:08.158704+00:00_

Web search results for query: "ACLED "Armed Conflict Location Event Data" text classification NLP dataset public download categories"

Links: [{"title":"Introducing ACLED: An Armed Conflict Location and Events Dataset – Peace Research Institute Oslo (PRIO)","url":"https://www.prio.org/publications/3236"},{"title":"Introducing ACLED: An Armed Conflict Location and Event Dataset: Special Data Feature – Peace Research Institute Oslo (PRIO)","url":"https://www.prio.org/publications/4772"},{"title":"Introducing ACLED: An Armed Conflict Location and Event Dataset - Clionadh Raleigh, rew Linke, Håvard Hegre, Joakim Karlsen, 2010","url":"https://journals.sagepub.com/doi/10.1177/0022343310378914"},{"title":"Armed Conflict Location and Event Data - Wikipedia","url":"https://en.wikipedia.org/wiki/Armed_Conflict_Location_and_Event_Data"},{"title":"Armed Conflict Location & Event Data Project CODEBOOK","url":"https://acleddata.com/sites/default/files/wp-content-archive/uploads/dlm_uploads/2023/06/ACLED_Codebook_2023.pdf"},{"title":"Introducing ACLED: An Armed Conflict Location and Event Dataset: Special Data Feature | Request PDF","url":"https://www.researchgate.net/publication/227574688_Introducing_ACLED_An_Armed_Conflict_Location_and_Event_Dataset_Special_Data_Feature"},{"title":"Armed Conflict Location and Event Data Project (ACLED) |","url":"https://terrorismresearch.uark.edu/acled/"},{"title":"1 Armed Conflict Location and Event Data Project (ACLED) Codebook 2015","url":"https://www.strausscenter.org/wp-content/uploads/ACLED_Codebook_2015.pdf"}]

Now let me search specifically for information about the public download and event categories:

Links: [{"title":"ACLED Codebook | ACLED","url":"https://acleddata.com/methodology/acled-codebook"},{"title":"What types of events does ACLED code? | ACLED","url":"https://acleddata.com/faq/what-types-events-does-acled-code"},{"title":"ACLED Introduces New Event Types and Sub-Event Types | ACLED","url":"https://acleddata.com/2019/03/14/a
…[truncated 3447 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_protest-dataset-search_20260520T092905",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool call

_source line 74 · 2026-05-20T09:35:08.158850+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "massmobilization.github.io about protest demand categories government response categories complete list"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_protest-dataset-search_20260520T092905",
  "tool": "WebSearch",
  "tool_args": {
    "query": "massmobilization.github.io about protest demand categories government response categories complete list"
  }
}
```

</details>

---

### Tool call

_source line 75 · 2026-05-20T09:35:08.158978+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"Mass Mobilization\" Clark Regan 2021 \"International Studies Quarterly\" OR \"Journal of Conflict Resolution\" OR \"International Interactions\" cite paper"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_protest-dataset-search_20260520T092905",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"Mass Mobilization\" Clark Regan 2021 \"International Studies Quarterly\" OR \"Journal of Conflict Resolution\" OR \"International Interactions\" cite paper"
  }
}
```

</details>

---

### Tool call

_source line 76 · 2026-05-20T09:35:08.159109+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://poldem.eui.eu/downloads/pea/poldem-protest_30_codebook.pdf",
  "prompt": "Extract ALL information about: 1) The list of issue categories (issue_econ_private, issue_econ_public, etc.) and their descriptions. 2) The list of action_form categories and their descriptions. 3) Total number of observations/events in the dataset. 4) License or terms of use. 5) Citation information. 6) Any mention of human annotation / gold standard labels / intercoder reliability."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_protest-dataset-search_20260520T092905",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://poldem.eui.eu/downloads/pea/poldem-protest_30_codebook.pdf",
    "prompt": "Extract ALL information about: 1) The list of issue categories (issue_econ_private, issue_econ_public, etc.) and their descriptions. 2) The list of action_form categories and their descriptions. 3) Total number of observations/events in the dataset. 4) License or terms of use. 5) Citation information. 6) Any mention of human annotation / gold standard labels / intercoder reliability."
  }
}
```

</details>

---

### Tool call

_source line 77 · 2026-05-20T09:35:08.159260+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "github \"emerging-welfare\" case-2021-shared-task data subtask event type categories labels"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_protest-dataset-search_20260520T092905",
  "tool": "WebSearch",
  "tool_args": {
    "query": "github \"emerging-welfare\" case-2021-shared-task data subtask event type categories labels"
  }
}
```

</details>

---

### Tool call

_source line 78 · 2026-05-20T09:35:08.159386+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "CEHA \"Conflict Events Horn of Africa\" dataset download event types categories github zenodo"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_protest-dataset-search_20260520T092905",
  "tool": "WebSearch",
  "tool_args": {
    "query": "CEHA \"Conflict Events Horn of Africa\" dataset download event types categories github zenodo"
  }
}
```

</details>

---

### Tool call

_source line 79 · 2026-05-20T09:35:08.159505+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://poldem.eui.eu/downloads/pea/PEA_documentation_v1.pdf",
  "prompt": "Extract ALL information about: 1) Total number of events/observations in the dataset. 2) Issue categories and their full list. 3) Action form categories and their full list. 4) Human annotation methodology - was manual coding used? Intercoder reliability? Gold standard labels? 5) License or terms of use. 6) Full citation. 7) Sample size per country or total."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_protest-dataset-search_20260520T092905",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://poldem.eui.eu/downloads/pea/PEA_documentation_v1.pdf",
    "prompt": "Extract ALL information about: 1) Total number of events/observations in the dataset. 2) Issue categories and their full list. 3) Action form categories and their full list. 4) Human annotation methodology - was manual coding used? Intercoder reliability? Gold standard labels? 5) License or terms of use. 6) Full citation. 7) Sample size per country or total."
  }
}
```

</details>

---

### Tool call

_source line 80 · 2026-05-20T09:35:08.159629+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"political event coding\" dataset public download \"event type\" multi-class classification NLP benchmark 2023 2024 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_protest-dataset-search_20260520T092905",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"political event coding\" dataset public download \"event type\" multi-class classification NLP benchmark 2023 2024 2025"
  }
}
```

</details>

---

### Tool call

_source line 81 · 2026-05-20T09:35:08.159747+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://poldem.eui.eu/data-overview/",
  "prompt": "Extract all information about: 1) How to download the PolDem protest event dataset. 2) Whether registration or approval is needed. 3) License information. 4) List of available datasets and their sizes. 5) Any download links or instructions."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_protest-dataset-search_20260520T092905",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://poldem.eui.eu/data-overview/",
    "prompt": "Extract all information about: 1) How to download the PolDem protest event dataset. 2) Whether registration or approval is needed. 3) License information. 4) List of available datasets and their sizes. 5) Any download links or instructions."
  }
}
```

</details>

---

### Tool call

_source line 82 · 2026-05-20T09:35:08.159869+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "MPEDS \"Machine-learning Protest Event Data System\" dataset download github categories"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_protest-dataset-search_20260520T092905",
  "tool": "WebSearch",
  "tool_args": {
    "query": "MPEDS \"Machine-learning Protest Event Data System\" dataset download github categories"
  }
}
```

</details>

---

### Tool result

_source line 83 · 2026-05-20T09:35:08.159992+00:00_

Web search results for query: "massmobilization.github.io about protest demand categories government response categories complete list"

Links: [{"title":"About the Mass Mobilization Project","url":"https://massmobilization.github.io/about.html"},{"title":"The Mass Mobilization Project","url":"https://massmobilization.github.io/"},{"title":"GitHub - EmFib/Mass-Protests","url":"https://github.com/EmFib/Mass-Protests"},{"title":"GitHub - KyleMackey/MassMobilization: Collection of applications that depict the Mass Mobilization Protest Dataset","url":"https://github.com/KyleMackey/MassMobilization"},{"title":"Mass Mobilization Data Project Codebook and User’s Manual David H. Clark","url":"https://reed-statistics.github.io/math141s21/projects/mass_mobilization/MM_codebook.pdf"},{"title":"Analysis of Changepoints in Mass Mobilization Data","url":"https://massmobilization.github.io/mmChangepoint.html"},{"title":"The Mass Mobilization Project","url":"https://wt.social/post/1a7so955328518710844/history"},{"title":"Mass Mobilization dataset - Harvard Dataverse","url":"https://dataverse.harvard.edu/dataverse/MMdata"},{"title":"Mass Mobilization Protest Data - Mass Mobilization Data Project Dataverse","url":"https://dataverse.harvard.edu/dataset.xhtml?persistentId=doi:10.7910/DVN/HTTWYL"},{"title":"MassMobilization (Mass Mobilization Data Project) · GitHub","url":"https://github.com/MassMobilization"}]

Based on the search results from massmobilization.github.io, here are the complete lists of protest demand and government response categories:

## Protest Demand Categories

The Mass Mobilization data itemize what protesters demand across seven categories: labor/wages, land, police brutality, political process, prices/taxes, removal of a politician, and social restrictions.

## Government Response Categories

The dataset records up to seven types of government responses: accommodation, arrests, beatings, crowd dispersal, ignore, killings, and shootings.


REMINDER: You MUST incl
…[truncated 77 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_protest-dataset-search_20260520T092905",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 84 · 2026-05-20T09:35:08.160132+00:00_

I cannot extract the requested information from this PDF document. The content provided is a binary/compressed PDF file structure (indicated by the "%PDF-1.3" header and encoded stream data), not readable plain text.

To help you, I would need:

1. **A text-extracted version** of the PDF document, or
2. **The original document file** that can be properly processed

The current format shows only PDF metadata, font references, and compressed image/content streams that cannot be meaningfully parsed for substantive information about:
- Issue categories
- Action form classifications
- Dataset size
- Licensing terms
- Citation details
- Annotation methodology

**Recommendation:** Please provide either a `.txt` file extracted from this PDF or share the document through an OCR service to convert it to readable text format.

[Binary content (application/pdf, 1.8MB) also saved to /home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-prod-0510-projects-causal-annot-error-attrib/f4e2217a-b32c-4a8a-a616-c19348792700/tool-results/webfetch-1779269428379-yy4ryl.pdf]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_protest-dataset-search_20260520T092905",
  "tool": "WebFetch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 85 · 2026-05-20T09:35:08.160328+00:00_

# PolDem Protest Event Dataset Information

Based on the provided content, here's what I found:

## 1) How to Download
The page mentions a **"Download"** section exists at poldem.eui.eu/download/, but specific download instructions aren't detailed in this overview page.

## 2) Registration or Approval Requirements
No information about registration or approval processes appears in this content.

## 3) License Information
No license details are provided in the material shown.

## 4) Available Protest Datasets
Three protest event datasets are listed:

- **poldem-protest_30**: "Protest events in 30 countries" (2000-2015)
- **poldem-protest_6**: "Protest events in 6 countries" (1975-2011)
- **poldem-protest_eu**: "Protest events in 6 countries, EU issues only" (1995-2010)

No file sizes are specified in this overview.

## 5) Download Links or Instructions
The content references online tools exist but provides no direct download links or detailed procedural steps. The page directs users to explore.poldem.eui.eu and mentions "R tools" for analysis support.

**Contact:** poldem@eui.eu or poldem@wzb.eu for additional details about access and download procedures.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_protest-dataset-search_20260520T092905",
  "tool": "WebFetch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 86 · 2026-05-20T09:35:08.160551+00:00_

Web search results for query: "github "emerging-welfare" case-2021-shared-task data subtask event type categories labels"

Links: [{"title":"Call for Shared Task Participation at CASE @ ACL-IJCNLP: Socio-political and Crisis Events Detection","url":"https://groups.google.com/g/automated-political-event-collection/c/yArzXzv7cZQ"},{"title":"Emerging Markets Welfare – CASE 2021","url":"https://emw.ku.edu.tr/case-2021/"},{"title":"GitHub - emerging-welfare/case-2021-shared-task: Information and data related to the ProtestNews shared task at CASE @ ACL-IJCNLP 2021 workshop","url":"https://github.com/emerging-welfare/case-2021-shared-task"},{"title":"Call for Participation, Shared Task at the Workshop CASE @ ACL-IJCNLP 2021: Socio-Political and Crisis Events Detection | ACL Member Portal","url":"https://www.aclweb.org/portal/content/call-participation-shared-task-socio-political-and-crisis-events-detection"},{"title":"GitHub - emerging-welfare/case-2022-multilingual-event: The repository for the shared tasks Task 1 and Task 3 at CASE 2022 (to be held at EMNLP)","url":"https://github.com/emerging-welfare/case-2022-multilingual-event"},{"title":"(PDF) Discovering Black Lives Matter Events in the United States: Shared Task 3, CASE 2021","url":"https://www.researchgate.net/publication/353485828_Discovering_Black_Lives_Matter_Events_in_the_United_States_Shared_Task_3_CASE_2021"},{"title":"case-2021-shared-task/task2/test_dataset/test_set_final_release_with_labels.tsv at main · emerging-welfare/case-2021-shared-task","url":"https://github.com/emerging-welfare/case-2021-shared-task/blob/main/task2/test_dataset/test_set_final_release_with_labels.tsv"},{"title":"emerging-welfare · GitHub","url":"https://github.com/emerging-welfare"},{"title":"Challenges and Applications of Automated Extraction of Socio-political   Events from Text (CASE 2021): Workshop and Shared Task Report","url":"https://arxiv.org/pdf/2108.07865"}]

Based on the search results, I found information about the Git
…[truncated 1182 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_protest-dataset-search_20260520T092905",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 87 · 2026-05-20T09:35:08.160716+00:00_

# PDF Content Extraction Issues

I cannot extract the requested information from the provided content. The file appears to be a **corrupted or improperly formatted PDF** containing:

- Binary image data (JPEG streams) rather than readable text
- Flate-compressed streams that don't decompress to meaningful content
- PDF structural elements without legible extracted text

## What I Can Observe:
- The document includes **3 image objects** (Im1, Im2, Im3) with dimensions suggesting charts/tables
- References to fonts and color spaces indicate this was originally a formatted document
- The file structure suggests it may be a research paper or dataset documentation

## Required Actions:

To help you extract this information, please provide:

1. **A text-based PDF** or converted document (DOCX, TXT)
2. **A readable image** of the relevant pages
3. **The original source document** if this is published research

Once you provide readable source material, I can extract:
- Dataset event counts
- Issue/action category taxonomies
- Annotation methodologies
- Licensing information
- Complete citations
- Sample sizes by region

Would you like to provide an alternative version of this document?

[Binary content (application/pdf, 1.3MB) also saved to /home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-prod-0510-projects-causal-annot-error-attrib/f4e2217a-b32c-4a8a-a616-c19348792700/tool-results/webfetch-1779269429750-rcfwgc.pdf]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_protest-dataset-search_20260520T092905",
  "tool": "WebFetch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 88 · 2026-05-20T09:35:08.160867+00:00_

Web search results for query: "MPEDS "Machine-learning Protest Event Data System" dataset download github categories"

Links: [{"title":"GitHub - MPEDS/mpeds: Machine-learning Protest Event Data System · GitHub","url":"https://github.com/MPEDS/mpeds"},{"title":"mpeds/README.md at master · MPEDS/mpeds","url":"https://github.com/MPEDS/mpeds/blob/master/README.md"},{"title":"Coding Protest Event Data & Studying Black Protest | Pamela E. Oliver","url":"https://www.ssc.wisc.edu/~oliver/protest-research/mpeds/"},{"title":"MPEDS · GitHub","url":"https://github.com/MPEDS"},{"title":"MPEDS - Automated Coding of Protest Event Data by MPEDS","url":"https://mpeds.github.io/"},{"title":"mpeds/cliff/Dockerfile at master · MPEDS/mpeds","url":"https://github.com/MPEDS/mpeds/blob/master/cliff/Dockerfile"},{"title":"MPEDS: Machine-Learning Protest Event Data System","url":"https://zenodo.org/records/886459"},{"title":"MPEDS: Automating the Generation of Protest Event Data | Request PDF","url":"https://www.researchgate.net/publication/326121293_MPEDS_Automating_the_Generation_of_Protest_Event_Data"},{"title":"Coding Protest Event Data & Studying Black Protest","url":"https://users.ssc.wisc.edu/~oliver/protest-research/mpeds/"},{"title":"GitHub - MPEDS/mpeds-coder: MPEDS Annotation Interface","url":"https://github.com/MPEDS/mpeds-coder"}]

Based on the search results, here's what I found about MPEDS:

## Overview

MPEDS is a tool for facilitating the creation of protest event data using recent innovations from machine learning and natural language processing to generate protest event data with little to no human intervention.

## GitHub Repository

The main repository is located at **https://github.com/MPEDS/mpeds**. You will need to install Git LFS to properly download the large classifier and vectorizer files from this repository.

## Related Tools

The MPEDS system includes the MPEDS Annotation Interface (MAI), a browser-based coding interface that is available on GitHub as mpeds/mp
…[truncated 745 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_protest-dataset-search_20260520T092905",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 89 · 2026-05-20T09:35:08.161019+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://poldem.eui.eu/downloads/pea/PEA_codebook_v1.pdf",
  "prompt": "Extract ALL information: 1) Full list of issue categories with descriptions. 2) Full list of action_form categories with descriptions. 3) Total number of events. 4) Human annotation / coding methodology. 5) License. 6) Citation. Report everything you can read from this document."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_protest-dataset-search_20260520T092905",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://poldem.eui.eu/downloads/pea/PEA_codebook_v1.pdf",
    "prompt": "Extract ALL information: 1) Full list of issue categories with descriptions. 2) Full list of action_form categories with descriptions. 3) Total number of events. 4) Human annotation / coding methodology. 5) License. 6) Citation. Report everything you can read from this document."
  }
}
```

</details>

---

### Tool result

_source line 90 · 2026-05-20T09:35:08.161224+00:00_

Web search results for query: ""Mass Mobilization" Clark Regan 2021 "International Studies Quarterly" OR "Journal of Conflict Resolution" OR "International Interactions" cite paper"

Links: [{"title":"Mobilization: An International Quarterly","url":"https://mobilization.kglmeridian.com/"},{"title":"Dynamics of Political Protests | International Organization | Cambridge Core","url":"https://www.cambridge.org/core/journals/international-organization/article/abs/dynamics-of-political-protests/FF34963F17453C36ACC88B5C880E156D"},{"title":"About this Journal - Mobilization: An International Quarterly","url":"https://mobilization.kglmeridian.com/page/about"},{"title":"MMD (Mass Mobilization Database) from Clark and Regan (2018): 166... | Download Scientific Diagram","url":"https://www.researchgate.net/figure/MMD-Mass-Mobilization-Database-from-Clark-and-Regan-2018-166-countries-across-South_fig1_352664331"},{"title":"About the Mass Mobilization Project","url":"https://massmobilization.github.io/about.html"},{"title":"Opportunities to Fight - David H. Clark, Patrick M. Regan, 2003","url":"https://journals.sagepub.com/doi/10.1177/0022002702239513"},{"title":"DataCite Search","url":"https://search.datacite.org/works/10.7910/dvn/httwyl"}]

The search results show references to the Mass Mobilization Database created by Clark and Regan, but I haven't found a specific 2021 publication in one of the three journals you mentioned. Let me search more specifically for a 2021 paper by Clark and Regan in these journals.

Links: [{"title":"International Studies Quarterly","url":"https://www.scimagojr.com/journalsearch.php?q=25848&tip=sid&clean=0"},{"title":"Issues | International Studies Quarterly | Oxford Academic","url":"https://academic.oup.com/isq/issue"},{"title":"International Studies Quarterly | JSTOR","url":"https://www.jstor.org/journal/intestudquar"},{"title":"Presence of Ecuador in the Web of Science from open access in post-pandemic period 2019-2021: A multivariate analysis",
…[truncated 6025 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_protest-dataset-search_20260520T092905",
  "tool": "WebSearch",
  "elapsed_ms": 2
}
```

</details>

---

### Tool call

_source line 91 · 2026-05-20T09:35:08.161406+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://discuss-data.net/dataset/c7e7af8f-fa6f-46d3-8ae5-41a4aad6e4b9/",
  "prompt": "Extract all information about: 1) License of the PolDem dataset. 2) Number of observations. 3) Download method and whether registration is required. 4) Citation. 5) Any metadata about categories or variables."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_protest-dataset-search_20260520T092905",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://discuss-data.net/dataset/c7e7af8f-fa6f-46d3-8ae5-41a4aad6e4b9/",
    "prompt": "Extract all information about: 1) License of the PolDem dataset. 2) Number of observations. 3) Download method and whether registration is required. 4) Citation. 5) Any metadata about categories or variables."
  }
}
```

</details>

---

### Tool call

_source line 92 · 2026-05-20T09:35:08.161544+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://research.vu.nl/en/datasets/poldem-protest-dataset-30-european-countries",
  "prompt": "Extract all information: 1) License or access rights. 2) Citation. 3) Dataset description, size, number of events. 4) Authors. 5) Any DOI. 6) Keywords or categories."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_protest-dataset-search_20260520T092905",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://research.vu.nl/en/datasets/poldem-protest-dataset-30-european-countries",
    "prompt": "Extract all information: 1) License or access rights. 2) Citation. 3) Dataset description, size, number of events. 4) Authors. 5) Any DOI. 6) Keywords or categories."
  }
}
```

</details>

---

### Tool call

_source line 93 · 2026-05-20T09:35:08.161673+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"Mass Mobilization\" dataset freely downloadable no registration Harvard Dataverse CSV format rows columns"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_protest-dataset-search_20260520T092905",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"Mass Mobilization\" dataset freely downloadable no registration Harvard Dataverse CSV format rows columns"
  }
}
```

</details>

---

### Tool call

_source line 94 · 2026-05-20T09:35:08.161799+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Clark Regan \"Mass Mobilization\" \"how to cite\" OR citation recommended 2016 dataset Dataverse"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_protest-dataset-search_20260520T092905",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Clark Regan \"Mass Mobilization\" \"how to cite\" OR citation recommended 2016 dataset Dataverse"
  }
}
```

</details>

---

### Tool result

_source line 95 · 2026-05-20T09:35:08.161916+00:00_

# Document Analysis: Event Data Codebook

I cannot reliably extract the requested information from this PDF document. The content appears to be heavily compressed and encoded (PDF binary format with FlateDecode compression), making direct text extraction impossible through my current processing capabilities.

## What I Can Determine:

**Document Structure:** This is a multi-page PDF containing what appears to be a codebook or reference guide, with embedded images and formatted text content spanning approximately 8 pages.

**Limitations:**
- The compressed stream data prevents accurate parsing of issue categories, action form categories, methodology details, license information, and citation format
- Text content is fragmented across encoded sections that require proper PDF decompression and rendering
- Image-based content (potentially containing tables or charts) cannot be analyzed

## Recommendation:

To extract the specific information you need, please:
1. Provide the document in plain text format
2. Supply an OCR-processed version
3. Share a text export from the PDF
4. Describe the document title/source so I can help you locate it in another format

If you have access to the original source document in text or structured format, I can provide comprehensive extraction of all requested categories, methodologies, and citations.

[Binary content (application/pdf, 422.4KB) also saved to /home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-prod-0510-projects-causal-annot-error-attrib/f4e2217a-b32c-4a8a-a616-c19348792700/tool-results/webfetch-1779269440361-0b2vz1.pdf]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_protest-dataset-search_20260520T092905",
  "tool": "WebFetch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 96 · 2026-05-20T09:35:08.162048+00:00_

# PolDem – Protest Dataset 30 European Countries

## 1) License or Access Rights
No specific license details provided. Access available at: https://poldem.eui.eu/data-overview/

## 2) Citation
Kriesi, H., Wüest, B., Lorenzini, J., Makarov, P., Enggist, M., Rothenhäusler, K., Kurer, T., Häusermann, S., Wangen, P., Altiparmakis, A., Borbáth, E., Bremer, B., Gessler, T., Hunger, S., Hutter, S., Schulte-Cloos, J., & Wang, C. (2020). PolDem – Protest Dataset 30 European countries. Cambridge University Press.

## 3) Dataset Description
Comprehensive protest event data spanning "1 Jan 2000 - 31 Dec 2015" across 30 European countries. Specific counts of events or dataset size not disclosed in provided material.

## 4) Authors
17 creators listed, including Hanspeter Kriesi (lead), Bruno Wüest, Jasmine Lorenzini, and Chendi Wang among others affiliated with Vrije Universiteit Amsterdam.

## 5) DOI
Not provided in the available content.

## 6) Keywords/Categories
- Economic grievances and political grievances
- Protest analysis
- European political systems
- Economic recession impacts
- Political contention

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_protest-dataset-search_20260520T092905",
  "tool": "WebFetch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 97 · 2026-05-20T09:35:08.162230+00:00_

Web search results for query: "CEHA "Conflict Events Horn of Africa" dataset download event types categories github zenodo"

Links: [{"title":"CEHA: A Dataset of Conflict Events in the Horn of Africa","url":"https://arxiv.org/html/2412.13511v1"},{"title":"CEHA: A Dataset of Conflict Events in the Horn of Africa","url":"https://arxiv.org/pdf/2412.13511"},{"title":"CEHA: A Dataset of Conflict Events in the Horn of Africa - ACL Anthology","url":"https://aclanthology.org/2025.coling-main.99/"},{"title":"[2412.13511] CEHA: A Dataset of Conflict Events in the Horn of Africa","url":"https://arxiv.org/abs/2412.13511"},{"title":"CEHA: A Dataset of Conflict Events in the Horn of Africa","url":"https://aclanthology.org/2025.coling-main.99.pdf"}]

Let me search more specifically for where the dataset can be accessed on GitHub or Zenodo:

Links: [{"title":"Zenodo - A universal repository for all your research outcomes","url":"https://www.openaire.eu/zenodo-guide"},{"title":"Zenodo - Wikipedia","url":"https://en.wikipedia.org/wiki/Zenodo"},{"title":"GitHub - ICAERUS-EU/Zenodo_Datasets: This repository includes the links and information for Zenodo datasets of each ICAERUS Use Case. · GitHub","url":"https://github.com/ICAERUS-EU/Zenodo_Datasets"},{"title":"GitHub - zenodo/zenodo: Research. Shared. · GitHub","url":"https://github.com/zenodo/zenodo"},{"title":"GitHub - rokibulroni/zenodo-datasets-index: API URL · GitHub","url":"https://github.com/rokibulroni/zenodo-datasets-index"},{"title":"GitHub - zenodo/zenodo-classifier","url":"https://github.com/zenodo/zenodo-classifier"},{"title":"Zenodo | Data Management","url":"https://datamanagement.hms.harvard.edu/share-publish/data-repositories/zenodo"},{"title":"osbm/zenodo · Datasets at Hugging Face","url":"https://huggingface.co/datasets/osbm/zenodo"},{"title":"Zenodo","url":"https://zenodo.org/"}]

Let me search more specifically for the CEHA dataset with event types and categories:

Links: [{"title":"CEHA: A Dataset of Conflict Event
…[truncated 3801 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_protest-dataset-search_20260520T092905",
  "tool": "WebSearch",
  "elapsed_ms": 2
}
```

</details>

---

### Tool result

_source line 98 · 2026-05-20T09:35:08.162386+00:00_

Web search results for query: ""Mass Mobilization" dataset freely downloadable no registration Harvard Dataverse CSV format rows columns"

Links: [{"title":"Mass Mobilization dataset - Harvard Dataverse","url":"https://dataverse.harvard.edu/dataverse/MMdata"},{"title":"Data Sources","url":"https://reed-statistics.github.io/math141s21/project_data.html"},{"title":"GitHub - KyleMackey/MassMobilization: Collection of applications that depict the Mass Mobilization Protest Dataset","url":"https://github.com/KyleMackey/MassMobilization"},{"title":"Mass Mobilization Protest Data - Mass Mobilization Data Project Dataverse","url":"https://dataverse.harvard.edu/dataset.xhtml?persistentId=doi:10.7910/DVN/HTTWYL"},{"title":"Replication Data for: Regime Transformation From Below: Mobilization for Democracy and Autocracy From 1900 to 2021 - Comparative Political Studies Dataverse","url":"https://dataverse.harvard.edu/dataset.xhtml?persistentId=doi:10.7910/DVN/YQPN8D"},{"title":"Replication Data for: Unpopular Protest: Mass Mobilization and Attitudes to Democracy in Post-Mubarak Egypt - The Journal of Politics Dataverse","url":"https://dataverse.harvard.edu/dataset.xhtml;jsessionid=05dd6f02a13e27718e597bbbabd5?persistentId=doi:10.7910/DVN/NDHKSG&fileSortField=date&fileSortOrder=desc"},{"title":"Exploring Economic Sectoral Dynamics Through High-resolution Mobility Data","url":"https://arxiv.org/pdf/2506.13985"},{"title":"Effect of Media Usage Selection on Social Mobilization Speed: Facebook vs E-Mail","url":"https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4589319/"},{"title":"Harvard Dataverse","url":"https://dataverse.harvard.edu/dataverse.xhtml?alias=MMdata"}]

Based on my search results, here's what I found about the Mass Mobilization dataset:

## Dataset Overview

The Mass Mobilization (MM) data are an effort to understand citizen movements against governments, what citizens want when they demonstrate against governments, and how governments respond to citizens. The data cover 162
…[truncated 1019 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_protest-dataset-search_20260520T092905",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 99 · 2026-05-20T09:35:08.162539+00:00_

Web search results for query: "Clark Regan "Mass Mobilization" "how to cite" OR citation recommended 2016 dataset Dataverse"

Links: [{"title":"Data Sources","url":"https://reed-statistics.github.io/math141s21/project_data.html"},{"title":"DataCite Search","url":"https://search.datacite.org/works/10.7910/dvn/httwyl"},{"title":"How do I cite a dataset in Dataverse? - Ask Us!","url":"https://askalibrarian.library.txstate.edu/faq/199438"},{"title":"Data Citation — Dataverse.org","url":"http://best-practices.dataverse.org/data-citation/"},{"title":"Data Citation | The Dataverse Project","url":"https://dataverse.org/best-practices/data-citation"},{"title":"Academic Credit | The Dataverse Project","url":"https://dataverse.org/best-practices/academic-credit"},{"title":"14- Data Citation in the Dataverse Network | For Attribution: Developing Data Attribution and Citation Practices and Standards: Summary of an International Workshop | The National Academies Press","url":"https://nap.nationalacademies.org/read/13564/chapter/15"},{"title":"Data Citation - Essential Resources for Locating and Using Numeric Data - Research Guides at Harvard Library","url":"https://guides.library.harvard.edu/c.php?g=310097&p=9720164"},{"title":"Cite Dataset - Queen's Dataverse Collection Data Deposit Guidelines - Research Guides at Queen's University Library","url":"https://guides.library.queensu.ca/dv-deposit-guidelines/steps-for-deposit/cite"}]

Based on the search results, I found information about the Mass Mobilization dataset:

The Mass Mobilization Data project was published in 2016 via Harvard Dataverse by David Clark & Patrick Regan and covers protests against governments across all countries from 1990-2020.

The DOI for the dataset is https://doi.org/10.7910/DVN/HTTWYL.

The standard citation for the dataset is: "Mass Mobilization Protest Data." Harvard Dataverse 2 (2016).

The Mass Mobilization data document citizen movements against governments, covering 162 countries between 1990 and 
…[truncated 487 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_protest-dataset-search_20260520T092905",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 100 · 2026-05-20T09:35:08.162689+00:00_

# PolDem Dataset Information

**1) License**
Not specified in the provided content.

**2) Number of Observations**
The dataset contains "30.000+ total entries" overall, with "1.655 events listed" for Estonia, Latvia, and Lithuania specifically.

**3) Download Method & Registration**
The content indicates the dataset is "available as a free download" from the "official Observatory for Political Conflict and Democracy in Europe website." Registration requirements are not mentioned.

**4) Citation**
"Nathalie Rathkamp (2025): Review of European University Institute/Center for Civil Society Research and WZB Berlin Social Science Center (2020): Observatory for Political Conflict and Democracy in Europe (published on Discuss Data), v. 1.0, Discuss Data, https://doi.org/10.48320/C7E7AF8F-FA6F-46D3-8AE5-41A4AAD6E4B9"

**5) Metadata - Categories & Variables**
The dataset covers protest events, election campaigns, public debates, and contentious episodes across 30 European countries (2000-2015). Keywords include: protests, strikes, demonstrations, environment, political issues, violent protests, confrontations, blockades, petitions, symbolic actions, and organizational actors (parties, unions, social groups).

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_protest-dataset-search_20260520T092905",
  "tool": "WebFetch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 101 · 2026-05-20T09:35:08.162847+00:00_

Web search results for query: ""political event coding" dataset public download "event type" multi-class classification NLP benchmark 2023 2024 2025"

Links: [{"title":"Tracking the 2024 US Presidential Election Chatter on TikTok: A Public   Multimodal Dataset","url":"https://arxiv.org/pdf/2412.15583"},{"title":"A Public Dataset Tracking Social Media Discourse about the 2024 U.S.   Presidential Election on Twitter/X","url":"https://arxiv.org/pdf/2411.00376"},{"title":"Unearthing a Billion Telegram Posts about the 2024 U.S. Presidential   Election: Development of a Public Dataset","url":"https://arxiv.org/pdf/2410.23638"},{"title":"Comparative Agendas","url":"https://www.comparativeagendas.net/project/us/datasets"},{"title":"Indonesian presidential election sentiment: Dataset of response public before 2024","url":"https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10788203/"}]

Let me search more specifically for NLP benchmark datasets focused on event classification:

Links: [{"title":"Generative Approaches to Event Extraction: Survey and ...","url":"https://aclanthology.org/2024.futured-1.7.pdf"},{"title":"15 Must-Know NLP Benchmark Datasets to Master in 2025 🚀 - ChatBench","url":"https://www.chatbench.org/nlp-benchmark-datasets/"},{"title":"Ontology-driven Event Type Classification in Images","url":"https://arxiv.org/pdf/2011.04714"},{"title":"Multi-Label Classification Model From Scratch: Step-by-Step Tutorial","url":"https://huggingface.co/blog/Valerii-Knowledgator/multi-label-classification"},{"title":"Ensemble Detection of Single & Multiple Events at Sentence-Level","url":"https://arxiv.org/pdf/1403.6023"},{"title":"Multimodal Classification of Events in Social Media","url":"https://arxiv.org/pdf/1601.00599"}]

Let me search specifically for ACLED or other political event coding datasets:

Links: [{"title":"ACLED Codebook | ACLED","url":"https://acleddata.com/methodology/acled-codebook"},{"title":"1 Armed Conflict Location and Event Data Project (ACLED) Codebook 201
…[truncated 4971 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_protest-dataset-search_20260520T092905",
  "tool": "WebSearch",
  "elapsed_ms": 3
}
```

</details>

---

### Tool call

_source line 102 · 2026-05-20T09:35:08.163013+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Kriesi protest event analysis Europe \"issue categories\" \"economic\" \"cultural\" coding scheme semi-automated"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_protest-dataset-search_20260520T092905",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Kriesi protest event analysis Europe \"issue categories\" \"economic\" \"cultural\" coding scheme semi-automated"
  }
}
```

</details>

---

### Tool call

_source line 103 · 2026-05-20T09:35:08.163147+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Mass Mobilization data.world download protest data 17000 events protester_demand government_response columns"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_protest-dataset-search_20260520T092905",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Mass Mobilization data.world download protest data 17000 events protester_demand government_response columns"
  }
}
```

</details>

---

### Tool call

_source line 104 · 2026-05-20T09:35:08.163297+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"Mass Mobilization\" protest data NLP text classification annotation label news article source"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_protest-dataset-search_20260520T092905",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"Mass Mobilization\" protest data NLP text classification annotation label news article source"
  }
}
```

</details>

---

### Tool call

_source line 105 · 2026-05-20T09:35:08.163425+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "CASE 2021 task 2 \"fine-grained classification\" socio-political event types 25 subtypes dataset download"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_protest-dataset-search_20260520T092905",
  "tool": "WebSearch",
  "tool_args": {
    "query": "CASE 2021 task 2 \"fine-grained classification\" socio-political event types 25 subtypes dataset download"
  }
}
```

</details>

---

### Tool call

_source line 106 · 2026-05-20T09:35:08.163549+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"poldem\" OR \"protest event\" dataset Kriesi Hutter \"30,000\" OR \"30000\" OR \"number of events\" coding reliability"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_protest-dataset-search_20260520T092905",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"poldem\" OR \"protest event\" dataset Kriesi Hutter \"30,000\" OR \"30000\" OR \"number of events\" coding reliability"
  }
}
```

</details>

---

### Tool call

_source line 107 · 2026-05-20T09:35:08.163673+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "MAVEN event detection dataset 168 event types download huggingface github protest political"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_protest-dataset-search_20260520T092905",
  "tool": "WebSearch",
  "tool_args": {
    "query": "MAVEN event detection dataset 168 event types download huggingface github protest political"
  }
}
```

</details>

---

### Tool call

_source line 108 · 2026-05-20T09:35:08.163794+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"CrisisNLP\" OR \"CrisisLex\" OR \"HumAID\" event type classification dataset download categories labels"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_protest-dataset-search_20260520T092905",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"CrisisNLP\" OR \"CrisisLex\" OR \"HumAID\" event type classification dataset download categories labels"
  }
}
```

</details>

---

### Tool call

_source line 109 · 2026-05-20T09:35:08.163915+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"Crowd Counting Consortium\" OR \"ACLED\" protest classification dataset NLP text multi-class"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_protest-dataset-search_20260520T092905",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"Crowd Counting Consortium\" OR \"ACLED\" protest classification dataset NLP text multi-class"
  }
}
```

</details>

---

### Tool result

_source line 110 · 2026-05-20T09:35:08.164036+00:00_

Web search results for query: "Mass Mobilization data.world download protest data 17000 events protester_demand government_response columns"

Links: [{"title":"About the Mass Mobilization Project","url":"https://massmobilization.github.io/about.html"},{"title":"Mass Mobilization Protest Data - dataset by government","url":"https://data.world/government/mass-mobilization-protest-data"},{"title":"Review of Clark/Regan (2016): Mass Mobilization Project","url":"https://discuss-data.net/dataset/4e6a40ff-4ae0-4cc8-89b3-dbe162be07c0/"},{"title":"Mass Mobilization Data Project - Data Catalog","url":"https://datacatalog.library.wayne.edu/dataset/mass-mobilization-data-project"},{"title":"Mass Mobilization Protest Data - Mass Mobilization Data Project Dataverse","url":"https://dataverse.harvard.edu/dataset.xhtml?persistentId=doi:10.7910/DVN/HTTWYL"},{"title":"Mass Mobilization Project tracks protests around the world - Binghamton News","url":"https://www.binghamton.edu/news/story/3282/hit-the-streets-mass-mobilization-project-tracks-protests-around-the-world"},{"title":"Mass Mobilization Data Project Dataverse","url":"https://dataverse.harvard.edu/dataverse/MMdata"},{"title":"The Mass Mobilization Project","url":"https://massmobilization.github.io/"},{"title":"Mass Mobilization in Autocracies Database","url":"https://mmadatabase.org/"},{"title":"Data - PLSC 410: Political Protests - Yale University Library Research Guides at Yale University","url":"https://guides.library.yale.edu/c.php?g=956915&p=6961578"}]

Based on the search results, I found information about the Mass Mobilization protest data:

The Mass Mobilization dataset contains over 17,000 total entries, and provides information on protester demands and government responses. 

The data cover 162 countries between 1990 and 2018, and include events where 50 or more protesters publicly demonstrate against government, with each event recording location, protest size, protester demands, and government responses.

The data
…[truncated 592 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_protest-dataset-search_20260520T092905",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 111 · 2026-05-20T09:35:08.164204+00:00_

Web search results for query: "CASE 2021 task 2 "fine-grained classification" socio-political event types 25 subtypes dataset download"

Links: [{"title":"CASE 2021 Task 2 Socio-political Fine-grained Event Classification using Fine-tuned RoBERTa Document Embeddings - ACL Anthology","url":"https://aclanthology.org/2021.case-1.26/"},{"title":"CASE 2021 Task 2: Zero-Shot Classification of Fine-Grained Sociopolitical Events with Transformer Models - ACL Anthology","url":"https://aclanthology.org/2021.case-1.25/"},{"title":"CASE 2021 Task 2 – Benjamin J. Radford","url":"https://www.benradford.com/publications/2021-06-20/case-task-2.html"},{"title":"CASE 2021 Task 2 Socio-political Fine-grained Event ...","url":"https://aclanthology.org/2021.case-1.26.pdf"},{"title":"CASE 2021 Task 2: Zero-Shot Classiﬁcation of Fine-Grained","url":"https://aclanthology.org/2021.case-1.25.pdf"},{"title":"Proceedings of the 4th Workshop on Challenges and Applications of Automated Extraction of Socio-political Events from Text (CASE 2021) - ACL Anthology","url":"https://aclanthology.org/volumes/2021.case-1/"},{"title":"Fine-grained Event Classification in News-like Text Snippets - Shared Task 2, CASE 2021 - ACL Anthology","url":"https://aclanthology.org/2021.case-1.23/"},{"title":"Call for Participation, Shared Task at the Workshop CASE @ ACL-IJCNLP 2021: Socio-Political and Crisis Events Detection | ACL Member Portal","url":"https://www.aclweb.org/portal/content/call-participation-shared-task-socio-political-and-crisis-events-detection"},{"title":"Challenges and Applications of Automated Extraction of Socio-political   Events from Text (CASE 2021): Workshop and Shared Task Report","url":"https://arxiv.org/pdf/2108.07865"}]

Based on the search results, I found information about CASE 2021 Task 2 on fine-grained classification of socio-political events:

## Task Overview

CASE 2021 Task 2 is a shared task on fine-grained event classification in news-like text snippets, divided into three sub
…[truncated 1265 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_protest-dataset-search_20260520T092905",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 112 · 2026-05-20T09:35:08.164357+00:00_

Web search results for query: "MAVEN event detection dataset 168 event types download huggingface github protest political"

Links: [{"title":"MAVEN","url":"https://thukeg.gitee.io/maven/"},{"title":"MAVEN: A Massive General Domain Event Detection Dataset | Request PDF","url":"https://www.researchgate.net/publication/347236490_MAVEN_A_Massive_General_Domain_Event_Detection_Dataset"},{"title":"MAVEN: A Massive General Domain Event Detection Dataset - ACL Anthology","url":"https://aclanthology.org/2020.emnlp-main.129/"},{"title":"MAVEN: A Massive General Domain Event Detection Dataset","url":"https://papertalk.org/papertalks/11458"},{"title":"MAVEN: A Massive General Domain Event Detection Dataset - Xiaozhi Wang 王晓智","url":"https://bakser.github.io/publication/2020-11-17-MAVEN"},{"title":"MAVEN: A Massive General Domain Event Detection Dataset","url":"https://arxiv.org/pdf/2004.13590"},{"title":"[2004.13590] MAVEN: A Massive General Domain Event Detection Dataset","url":"https://arxiv.org/abs/2004.13590"},{"title":"KG-NLP-Papers/EMNLP/2020/EE/8. MAVEN_A Massive General Domain Event Detection Dataset.md at main · Clearailhc/KG-NLP-Papers","url":"https://github.com/Clearailhc/KG-NLP-Papers/blob/main/EMNLP/2020/EE/8.%20MAVEN_A%20Massive%20General%20Domain%20Event%20Detection%20Dataset.md"},{"title":"MAVEN: A Massive General Domain Event Detection Dataset","url":"https://bakser.github.io/files/EMNLP20-MAVEN/MAVEN.pdf"}]

Based on the search results, here's information about the MAVEN event detection dataset:

## Overview
MAVEN is an event detection dataset with massive general domain human annotated data containing 4,480 documents, 118,732 event mentions and 168 event types. It was collected by researchers at Tsinghua University and WeChat AI.

## Download Locations
The source code and dataset can be obtained from https://github.com/THU-KEG/MAVEN-dataset.

## Dataset Details
The dataset contains 4,480 Wikipedia documents, 118,732 event mention instances, and 168 event typ
…[truncated 453 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_protest-dataset-search_20260520T092905",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 113 · 2026-05-20T09:35:08.164508+00:00_

Web search results for query: "Kriesi protest event analysis Europe "issue categories" "economic" "cultural" coding scheme semi-automated"

Links: [{"title":"(PDF) Restructuring protest politics: the terrain of cultural winners","url":"https://www.researchgate.net/publication/307937428_Restructuring_protest_politics_the_terrain_of_cultural_winners"},{"title":"1 PolDem – Protest Dataset 30 European countries - Version 1 -","url":"https://poldem.eui.eu/downloads/pea/poldem-protest_30_codebook.pdf"},{"title":"1 PolDem – Protest Dataset on EU Issues - Version 1 - poldem-protest_eu","url":"https://poldem.eui.eu/downloads/pea/poldem-protest_eu_codebook.pdf"},{"title":"Dynamics of protest mobilisation in the European poly-crisis","url":"https://cadmus.eui.eu/server/api/core/bitstreams/03312d5a-4f6e-5fdc-b0a8-cfdb82f0cd97/content"},{"title":"Protest Event Analysis: Developing a Semiautomated NLP Approach - Jasmine Lorenzini, Hanspeter Kriesi, Peter Makarov, Bruno Wüest, 2022","url":"https://journals.sagepub.com/doi/10.1177/00027642211021650"},{"title":"Political Conflict in Western Europe - Hanspeter Kriesi - Google Books","url":"https://books.google.com/books/about/Political_Conflict_in_Western_Europe.html?id=6_zivrfDd3AC"},{"title":"(PDF) Local protest event analysis: providing a more comprehensive picture?","url":"https://www.researchgate.net/publication/381615564_Local_protest_event_analysis_providing_a_more_comprehensive_picture"},{"title":"Full article: Dynamics of protest mobilisation in the European poly-crisis","url":"https://www.tandfonline.com/doi/full/10.1080/13501763.2024.2366388"}]

Based on the search results, I found relevant information about Kriesi's protest event analysis methodology and coding schemes in Europe:

Protest event analysis aims at retrieving and describing protest events so as to allow for cross-sectional and longitudinal analyses. A simplified version of the PEA approach established by Kriesi et al. (1995) and further elaborated by Hutter (
…[truncated 1093 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_protest-dataset-search_20260520T092905",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 114 · 2026-05-20T09:35:08.164653+00:00_

Web search results for query: ""Mass Mobilization" protest data NLP text classification annotation label news article source"

Links: [{"title":"Protest Event Analysis: Developing a Semiautomated NLP Approach - Jasmine Lorenzini, Hanspeter Kriesi, Peter Makarov, Bruno Wüest, 2022","url":"https://journals.sagepub.com/doi/10.1177/00027642211021650"},{"title":"About the Mass Mobilization Project","url":"https://massmobilization.github.io/about.html"},{"title":"MPEDS: Automating the Generation of Protest Event Data | Request PDF","url":"https://www.researchgate.net/publication/326121293_MPEDS_Automating_the_Generation_of_Protest_Event_Data"},{"title":"Protest Event Analysis : American Behavioral Scientist","url":"https://www.ovid.com/journals/absc/fulltext/10.1177/00027642211021650~protest-event-analysis-developing-a-semiautomated-nlp"},{"title":"Mass Mobilization Protest Data - Mass Mobilization Data Project Dataverse","url":"https://dataverse.harvard.edu/dataset.xhtml?persistentId=doi:10.7910/DVN/HTTWYL"},{"title":"Cross-context News Corpus for Protest Events related Knowledge Base   Construction","url":"https://arxiv.org/pdf/2008.00351"},{"title":"Mass Mobilization Protest Data - dataset by government","url":"https://data.world/government/mass-mobilization-protest-data"},{"title":"When a Nation Speaks: Machine Learning and NLP in People's Sentiment Analysis During Bangladesh's 2024 Mass Uprising","url":"https://arxiv.org/pdf/2512.15547"}]

Based on the search results, here's what I found about Mass Mobilization protest data and NLP text classification:

## Mass Mobilization Project Overview

The Mass Mobilization (MM) data are an effort to understand citizen movements against governments, what citizens want when they demonstrate against governments, and how governments respond to citizens. The MM data cover 162 countries between 1990 and 2018 and contain events where 50 or more protesters publicly demonstrate against government, resulting in more than 10,000 protest 
…[truncated 1121 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_protest-dataset-search_20260520T092905",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 115 · 2026-05-20T09:35:08.164818+00:00_

Web search results for query: ""poldem" OR "protest event" dataset Kriesi Hutter "30,000" OR "30000" OR "number of events" coding reliability"

Links: [{"title":"GitHub - davidpomerenke/german-protest-registrations: Dataset on demonstrations in Germany","url":"https://github.com/davidpomerenke/german-protest-registrations"},{"title":"1 PolDem – Protest Dataset on EU Issues - Version 1 - poldem-protest_eu","url":"https://poldem.eui.eu/downloads/pea/poldem-protest_eu_codebook.pdf"},{"title":"(PDF) Local protest event analysis: providing a more comprehensive picture?","url":"https://www.researchgate.net/publication/381615564_Local_protest_event_analysis_providing_a_more_comprehensive_picture"},{"title":"Full article: Local protest event analysis: providing a more comprehensive picture?","url":"https://www.tandfonline.com/doi/full/10.1080/01402382.2024.2363709"},{"title":"1 PolDem – Protest Event Dataset 30 - Version 1 - Please cite as:","url":"https://poldem.eui.eu/downloads/pea/PEA_documentation_v1.pdf"},{"title":"1 PolDem – Protest Dataset 30 European countries - Version 1 -","url":"https://poldem.eui.eu/downloads/pea/poldem-protest_30_codebook.pdf"},{"title":"PolDem - Observatory for Political Conflict and Democracy in Europe","url":"https://poldem.eui.eu/"},{"title":"Data Portal on Political Conflict and Democracy in Europe (PolDem) | WZB","url":"https://www.wzb.eu/en/research/dynamics-of-political-systems/center-for-civil-society-research/projects/daten-portal-zu-politischen-konflikten-und-protest-in-europa"},{"title":"News - PolDem","url":"https://poldem.eui.eu/news/"},{"title":"Protest Event Analysis: Developing a Semiautomated NLP Approach - Jasmine Lorenzini, Hanspeter Kriesi, Peter Makarov, Bruno Wüest, 2022","url":"https://journals.sagepub.com/doi/10.1177/00027642211021650"}]

Based on the search results, I found relevant information about the PolDem dataset and protest event analysis. Here's what I found:

## PolDem Dataset Overview

PolDem (Kriesi et al. 2
…[truncated 1525 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_protest-dataset-search_20260520T092905",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool call

_source line 116 · 2026-05-20T09:35:08.164972+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"Mass Mobilization\" dataset human coded annotated news sources codebook \"hand-coded\" OR \"human-coded\" OR \"manually coded\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_protest-dataset-search_20260520T092905",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"Mass Mobilization\" dataset human coded annotated news sources codebook \"hand-coded\" OR \"human-coded\" OR \"manually coded\""
  }
}
```

</details>

---

### Tool result

_source line 117 · 2026-05-20T09:35:08.165105+00:00_

Web search results for query: ""Crowd Counting Consortium" OR "ACLED" protest classification dataset NLP text multi-class"

Links: [{"title":"CONSTRUCTING RELATIONAL AND VERIFIABLE PROTEST EVENT DATA:","url":"https://par.nsf.gov/servlets/purl/10417072"},{"title":"Protest and Conflict - Datasets - Washington and Lee University Research Guides at Washington and Lee University","url":"https://libguides.wlu.edu/c.php?g=99391&p=10563637"},{"title":"Few-Shot Upsampling for Protest Size Detection","url":"https://arxiv.org/pdf/2105.11260"},{"title":"GitHub - rexdouglass/crowd-counting-consortium: Data for the Crowd Counting Consortium Data Dashboard · GitHub","url":"https://github.com/rexdouglass/crowd-counting-consortium"},{"title":"About – Counting Crowds","url":"https://countingcrowds.org/about/"},{"title":"Crowd Counting Consortium U.S. Protest Event Data, 2017 ...","url":"https://dataverse.harvard.edu/dataset.xhtml?persistentId=doi%3A10.7910%2FDVN%2F6OPP7H"},{"title":"Counting Protests in News Articles: A Dataset and Semi-Automated Data   Collection Pipeline","url":"https://arxiv.org/pdf/2102.00917"},{"title":"Crowd Counting Consortium - Ash Center - Harvard University","url":"https://ash.harvard.edu/programs/crowd-counting-consortium/"}]

I found relevant search results about the Crowd Counting Consortium and ACLED datasets. Here's what the search reveals:

**Crowd Counting Consortium (CCC):**
The Crowd Counting Consortium is a joint project of Harvard Kennedy School and the University of Connecticut that collects publicly available data on political protest events reported in the United States, including rallies, marches, demonstrations, and acts of civil disobedience. The data covers political crowds in the United States, including marches, protests, demonstrations, strikes, riots, and similar actions.

The dataset includes manually labeled news article URLs, dates, locations, crowd size estimates, and 494 discrete descriptive tags corresponding to 42,347 reported p
…[truncated 998 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_protest-dataset-search_20260520T092905",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 118 · 2026-05-20T09:35:08.165278+00:00_

Web search results for query: ""CrisisNLP" OR "CrisisLex" OR "HumAID" event type classification dataset download categories labels"

Links: [{"title":"HumAID: Human-Annotated Disaster Incidents Data from Twitter with Deep Learning Benchmarks | Request PDF","url":"https://www.researchgate.net/publication/365035740_HumAID_Human-Annotated_Disaster_Incidents_Data_from_Twitter_with_Deep_Learning_Benchmarks"},{"title":"(PDF) HumAID: Human-Annotated Disaster Incidents Data from Twitter","url":"https://www.researchgate.net/publication/350720422_HumAID_Human-Annotated_Disaster_Incidents_Data_from_Twitter"},{"title":"README.md · QCRI/HumAID-all at 1843be7","url":"https://huggingface.co/datasets/QCRI/HumAID-all/commit/1843be77b41a2913a7919c780a0a7d8b463b827a"},{"title":"HumAID: Human-Annotated Disaster Incidents Data from ...","url":"https://ojs.aaai.org/index.php/ICWSM/article/download/18116/17919/21611"},{"title":"HumAID: Human-Annotated Disaster Incidents Data from Twitter with Deep Learning Benchmarks - Mendeley Data","url":"https://data.mendeley.com/datasets/zppcyk2fdt/1"},{"title":"CrisisNLP","url":"https://crisisnlp.qcri.org/"},{"title":"GitHub - firojalam/crisis_datasets_benchmarks: Crisis Dataset for Benchmarks Experiments · GitHub","url":"https://github.com/firojalam/crisis_datasets_benchmarks"},{"title":"Natural Disaster Tweets Classification Using Multimodal Data","url":"https://aclanthology.org/2023.emnlp-main.471.pdf"},{"title":"Information Type Classification with Contrastive Task-Specialized   Sentence Encoders","url":"https://arxiv.org/pdf/2312.11020"},{"title":"A Lightweight LLM Framework for Disaster Humanitarian Information Classification","url":"https://arxiv.org/pdf/2602.12284"}]

Based on the search results, here's information about these crisis-related event classification datasets:

## HumAID Dataset

The HumAID Twitter dataset consists of several thousands of manually annotated tweets collected during 19 major natural disaster events including earthqu
…[truncated 1309 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_protest-dataset-search_20260520T092905",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool call

_source line 119 · 2026-05-20T09:35:08.165451+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://journals.sagepub.com/doi/10.1177/00027642211021650",
  "prompt": "Extract all information about: 1) The semi-automated NLP approach for protest event analysis. 2) Issue categories used and their full list. 3) Action form categories. 4) Total number of events in the dataset. 5) Human annotation methodology and intercoder reliability. 6) Whether annotations are gold-standard human labels. 7) Dataset size. 8) Citation information."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_protest-dataset-search_20260520T092905",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://journals.sagepub.com/doi/10.1177/00027642211021650",
    "prompt": "Extract all information about: 1) The semi-automated NLP approach for protest event analysis. 2) Issue categories used and their full list. 3) Action form categories. 4) Total number of events in the dataset. 5) Human annotation methodology and intercoder reliability. 6) Whether annotations are gold-standard human labels. 7) Dataset size. 8) Citation information."
  }
}
```

</details>

---

### Tool call

_source line 120 · 2026-05-20T09:35:08.165591+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Lorenzini Kriesi Makarov Wüest 2022 \"Protest Event Analysis\" \"semiautomated\" NLP issue categories action form intercoder"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_protest-dataset-search_20260520T092905",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Lorenzini Kriesi Makarov Wüest 2022 \"Protest Event Analysis\" \"semiautomated\" NLP issue categories action form intercoder"
  }
}
```

</details>

---

### Tool call

_source line 121 · 2026-05-20T09:35:08.165719+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "github emerging-welfare case-2021-shared-task task2 event subtypes list data format download"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_protest-dataset-search_20260520T092905",
  "tool": "WebSearch",
  "tool_args": {
    "query": "github emerging-welfare case-2021-shared-task task2 event subtypes list data format download"
  }
}
```

</details>

---

### Tool call

_source line 122 · 2026-05-20T09:35:08.165844+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"cross-context news corpus\" protest event \"gold standard\" download zenodo github categories"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_protest-dataset-search_20260520T092905",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"cross-context news corpus\" protest event \"gold standard\" download zenodo github categories"
  }
}
```

</details>

---

### Tool call

_source line 123 · 2026-05-20T09:35:08.165964+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "POLDEM protest event dataset 30 download categories action forms license"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_protest-dataset-search_20260520T092905",
  "tool": "WebSearch",
  "tool_args": {
    "query": "POLDEM protest event dataset 30 download categories action forms license"
  }
}
```

</details>

---

### Tool call

_source line 124 · 2026-05-20T09:35:08.166084+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"INDI-PROP\" dataset protest India NLP classification download categories labels"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_protest-dataset-search_20260520T092905",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"INDI-PROP\" dataset protest India NLP classification download categories labels"
  }
}
```

</details>

---

### Tool result

_source line 125 · 2026-05-20T09:35:08.166228+00:00_

Web search results for query: ""Mass Mobilization" dataset human coded annotated news sources codebook "hand-coded" OR "human-coded" OR "manually coded""

Links: [{"title":"Documentation – Mass Mobilization in Autocracies Database","url":"https://mmadatabase.org/about/documentation/"},{"title":"Mass Mobilization Data Project Codebook and User’s Manual David H. Clark","url":"https://reed-statistics.github.io/math141s21/projects/mass_mobilization/MM_codebook.pdf"},{"title":"Mass Mobilization in Autocracies Database","url":"https://mmadatabase.org/"},{"title":"Mass Mobilization dataset - Harvard Dataverse","url":"https://dataverse.harvard.edu/dataverse/MMdata"},{"title":"Review of Clark/Regan (2016): Mass Mobilization Project","url":"https://discuss-data.net/dataset/4e6a40ff-4ae0-4cc8-89b3-dbe162be07c0/"},{"title":"Download the MMAD – Mass Mobilization in Autocracies Database","url":"https://mmadatabase.org/get/"},{"title":"Mass Mobilization Data Project - Data Catalog","url":"https://datacatalog.library.wayne.edu/dataset/mass-mobilization-data-project"},{"title":"About the Mass Mobilization Project","url":"https://massmobilization.github.io/about.html"},{"title":"Mass Mobilization Protest Data - Mass Mobilization Data Project Dataverse","url":"https://dataverse.harvard.edu/dataset.xhtml?persistentId=doi:10.7910/DVN/HTTWYL"}]

Based on the search results, I found information about the Mass Mobilization datasets and their coding methodology:

## Mass Mobilization in Autocracies Database (MMAD)

The data is coded based on news reports obtained from AP, the AFP and BBC Monitoring. The project pre-filters news reports using machine learning techniques. A codebook for the current version (MMAD Codebook for Version 4.0) is available, along with codebooks for previous versions.

## Mass Mobilization Data Project

The earlier version of the Mass Mobilization project used a different approach. Coders search Lexis-Nexis, "All News," using "advanced options" which permit selectio
…[truncated 577 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_protest-dataset-search_20260520T092905",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 126 · 2026-05-20T09:35:08.166385+00:00_

Web search results for query: "github emerging-welfare case-2021-shared-task task2 event subtypes list data format download"

Links: [{"title":"Emerging Markets Welfare – CASE 2021","url":"https://emw.ku.edu.tr/case-2021/"},{"title":"GitHub - emerging-welfare/case-2021-shared-task: Information and data related to the ProtestNews shared task at CASE @ ACL-IJCNLP 2021 workshop","url":"https://github.com/emerging-welfare/case-2021-shared-task"},{"title":"Emerging Markets Welfare – CASE 2022","url":"https://emw.ku.edu.tr/case-2022/"},{"title":"case-2021-shared-task/task2/test_dataset/test_set_final_release_with_labels.tsv at main · emerging-welfare/case-2021-shared-task","url":"https://github.com/emerging-welfare/case-2021-shared-task/blob/main/task2/test_dataset/test_set_final_release_with_labels.tsv"},{"title":"(PDF) Discovering Black Lives Matter Events in the United States: Shared Task 3, CASE 2021","url":"https://www.researchgate.net/publication/353485828_Discovering_Black_Lives_Matter_Events_in_the_United_States_Shared_Task_3_CASE_2021"},{"title":"GitHub - emerging-welfare/case-2022-multilingual-event: The repository for the shared tasks Task 1 and Task 3 at CASE 2022 (to be held at EMNLP)","url":"https://github.com/emerging-welfare/case-2022-multilingual-event"},{"title":"Challenges and Applications of Automated Extraction of Socio-political   Events from Text (CASE 2021): Workshop and Shared Task Report","url":"https://arxiv.org/pdf/2108.07865"},{"title":"emerging-welfare · GitHub","url":"https://github.com/emerging-welfare"}]

Based on the search results, I found information about the CASE 2021 shared task Task 2:

Task 2 focuses on evaluating generalized zero-shot learning event classification approaches to classify short text snippets reporting socio-political events with fine-grained event types using the Armed Conflict Location & Event Data Project (ACLED) event taxonomy, which consists of 25 event subtypes pertaining to political violence, demonstrations (
…[truncated 859 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_protest-dataset-search_20260520T092905",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 127 · 2026-05-20T09:35:08.166532+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"Mass Mobilization\" Clark Regan dataset \"news text\" OR \"article text\" OR \"text column\" OR \"notes\" OR \"source text\" variables columns"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_protest-dataset-search_20260520T092905",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"Mass Mobilization\" Clark Regan dataset \"news text\" OR \"article text\" OR \"text column\" OR \"notes\" OR \"source text\" variables columns"
  }
}
```

</details>

---

### Tool result

_source line 128 · 2026-05-20T09:35:08.166704+00:00_

Web search results for query: ""cross-context news corpus" protest event "gold standard" download zenodo github categories"

Links: [{"title":"(PDF) Cross-Context News Corpus for Protest Event-Related Knowledge Base Construction","url":"https://www.researchgate.net/publication/352372953_Cross-Context_News_Corpus_for_Protest_Event-Related_Knowledge_Base_Construction"},{"title":"Cross-context News Corpus for Protest Events related Knowledge Base Construction | OpenReview","url":"https://openreview.net/forum?id=7NZkNhLCjp"},{"title":"Cross-Context News Corpus for Protest Event-Related Knowledge Base Construction | Data Intelligence | MIT Press","url":"https://direct.mit.edu/dint/article/3/2/308/100736/Cross-Context-News-Corpus-for-Protest-Event"},{"title":"Cross-context News Corpus for Protest Events related Knowledge Base   Construction","url":"https://arxiv.org/pdf/2008.00351"},{"title":"(PDF) Cross-context News Corpus for Protest Events related Knowledge Base Construction","url":"https://www.researchgate.net/publication/343414342_Cross-context_News_Corpus_for_Protest_Events_related_Knowledge_Base_Construction"},{"title":"Cross-context News Corpus for Protest Events related ...","url":"https://openreview.net/pdf?id=7NZkNhLCjp"},{"title":"GitHub - emerging-welfare/glocongold: The repo is about how to get access to the gold standard corpus that is created and exploited to generate the Global Contention Dataset (GLOCON) · GitHub","url":"https://github.com/emerging-welfare/glocongold"}]

Based on the search results, I found information about the Cross-Context News Corpus for Protest Events:

## Overview

The corpus is a gold standard collection of protest events comprising various local and international English language sources from various countries, with document-, sentence-, and token-level annotations. The corpus consists of English news articles from various local and international sources from India, China, and South Africa.

## Purpose

This corpus facilitates cr
…[truncated 1054 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_protest-dataset-search_20260520T092905",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 129 · 2026-05-20T09:35:08.166911+00:00_

Web search results for query: ""INDI-PROP" dataset protest India NLP classification download categories labels"

Links: [{"title":"Fine-grained Narrative Classification in Biased News Articles","url":"https://www.arxiv.org/pdf/2512.03582"},{"title":"Stance Prediction of Tweets on Farmers Protests in India","url":"https://www.ijraset.com/research-paper/stance-prediction-of-tweets-on-farmers-protests-in-india"},{"title":"H-Prop and H-Prop-News: Computational Propaganda Datasets in Hindi","url":"https://www.mdpi.com/2306-5729/7/3/29"},{"title":"Protest Event Analysis: Developing a Semiautomated NLP Approach - Jasmine Lorenzini, Hanspeter Kriesi, Peter Makarov, Bruno Wüest, 2022","url":"https://journals.sagepub.com/doi/10.1177/00027642211021650"},{"title":"bigscience-data/roots_indic-or_indic_nlp_corpus · Datasets at Hugging Face","url":"https://huggingface.co/datasets/bigscience-data/roots_indic-or_indic_nlp_corpus"},{"title":"Sentiment analysis and classification of Indian farmers’ protest using twitter data - ScienceDirect","url":"https://www.sciencedirect.com/science/article/pii/S2667096821000124"}]

Based on the web search results, here's what I found about the INDI-PROP dataset:

## INDI-PROP Dataset Overview

The INDI-PROP dataset comprises 1,266 articles focusing on two polarizing socio-political events in recent times: CAA and the Farmers' protest.

## Annotation Structure

Each article is annotated at two hierarchical levels: (i) ideological article-bias (pro-government, pro-opposition, neutral) and (ii) event-specific fine-grained narrative frames anchored in ideological polarity and communicative intent.

## Purpose and Application

The dataset is a narrative dataset with multi-level annotation for analyzing propaganda in Indian news media. A GPT-4o-mini guided multi-hop prompt-based reasoning framework called FANTA is proposed for bias and narrative classification.

The dataset appears to be designed for NLP tasks related to detecting propaganda and bias in
…[truncated 613 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_protest-dataset-search_20260520T092905",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 130 · 2026-05-20T09:35:08.167068+00:00_

Web search results for query: "POLDEM protest event dataset 30 download categories action forms license"

Links: [{"title":"1 PolDem – Protest Dataset on EU Issues - Version 1 - poldem-protest_eu","url":"https://poldem.eui.eu/downloads/pea/poldem-protest_eu_codebook.pdf"},{"title":"1 PolDem – Protest Event Dataset 30 - Version 1 - Please cite as:","url":"https://poldem.eui.eu/downloads/pea/PEA_documentation_v1.pdf"},{"title":"PolDem - Observatory for Political Conflict and Democracy in Europe","url":"https://poldem.eui.eu/"},{"title":"1 PolDem – Protest Dataset 30 European countries - Version 1 -","url":"https://poldem.eui.eu/downloads/pea/poldem-protest_30_codebook.pdf"},{"title":"Data Portal on Political Conflict and Democracy in Europe (PolDem) | WZB","url":"https://www.wzb.eu/en/research/dynamics-of-political-systems/center-for-civil-society-research/projects/daten-portal-zu-politischen-konflikten-und-protest-in-europa"},{"title":"GitHub - davidpomerenke/german-protest-registrations: Dataset on demonstrations in Germany","url":"https://github.com/davidpomerenke/german-protest-registrations"}]

Based on the search results, here's information about the POLDEM Protest Event Dataset 30:

## Overview
PolDem-Protest Dataset 30 covers 30 European countries with data collection relying on semi-automated coding of newswire reports, covering the time period from 2000 until 2015.

## Data Collection and Methodology
Protest event analysis is a form of content analysis that allows to systematically collect, quantify, and process large amounts of information on political protest across time and countries. The dataset includes 45,680 documents with about 642 working days invested in annotating the dataset.

## Categories and Variables
The dataset includes information on:
- Categories indicating whether an event is linked to other protest events that take place in the same country or in Europe
- Action forms and protest activities
- Organizations involved in protest events, cod
…[truncated 577 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_protest-dataset-search_20260520T092905",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 131 · 2026-05-20T09:35:08.167274+00:00_

Web search results for query: "Lorenzini Kriesi Makarov Wüest 2022 "Protest Event Analysis" "semiautomated" NLP issue categories action form intercoder"

Links: [{"title":"A modular pipeline for the automation of protest event analysis","url":"https://www.cambridge.org/core/services/aop-cambridge-core/content/view/90205C53AAAAA675F21AC19178418E68/S2049847025100137a.pdf/papea_a_modular_pipeline_for_the_automation_of_protest_event_analysis.pdf"},{"title":"Protest Event Analysis: Developing a Semiautomated NLP Approach - Jasmine Lorenzini, Hanspeter Kriesi, Peter Makarov, Bruno Wüest, 2022","url":"https://journals.sagepub.com/doi/10.1177/00027642211021650"},{"title":"Protest Event Analysis: Developing a Semiautomated NLP Approach | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Protest-Event-Analysis:-Developing-a-Semiautomated-Lorenzini-Kriesi/0d5d4aa04657300bf641b01243d556a192bac7c1"},{"title":"(PDF) Protest Event Analysis: Developing a Semiautomated NLP Approach","url":"https://www.researchgate.net/publication/352087597_Protest_Event_Analysis_Developing_a_Semiautomated_NLP_Approach"},{"title":"Peter Makarov's research works | University of Zurich and other places","url":"https://www.researchgate.net/scientific-contributions/2119894272_Peter_Makarov"},{"title":"Protest Event Analysis: Developing a Semiautomated NLP Approach","url":"https://agris.fao.org/search/en/providers/122535/records/65dfd44763b8185d9caf4ba9"},{"title":"PAPEA: A modular pipeline for the automation of protest event analysis | Political Science Research and Methods | Cambridge Core","url":"https://www.cambridge.org/core/journals/political-science-research-and-methods/article/papea-a-modular-pipeline-for-the-automation-of-protest-event-analysis/90205C53AAAAA675F21AC19178418E68"},{"title":"Protest event analysis: developin... | Archive ouverte UNIGE","url":"https://archive-ouverte.unige.ch/unige:152063"},{"title":"Protest Event Analysis : American Behavioral Scientist","url":"https://
…[truncated 1512 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_protest-dataset-search_20260520T092905",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool call

_source line 132 · 2026-05-20T09:35:08.167444+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "CASE 2021 task2 ACLED 25 event subtypes full list categories \"Armed Clash\" \"Violent demonstration\" \"Peaceful protest\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_protest-dataset-search_20260520T092905",
  "tool": "WebSearch",
  "tool_args": {
    "query": "CASE 2021 task2 ACLED 25 event subtypes full list categories \"Armed Clash\" \"Violent demonstration\" \"Peaceful protest\""
  }
}
```

</details>

---

### Tool result

_source line 133 · 2026-05-20T09:35:08.167579+00:00_

# Protest Event Analysis: NLP Approach & Dataset Summary

## 1) Semi-Automated NLP Approach

The researchers developed a **multistep pipeline combining automated and manual methods**. The process includes:

- **Keyword searching** across 10 English-language newswire agencies (5.2M initial documents)
- **Duplicate removal** using SpotSigs algorithm (Jaccard similarity ≥0.75)
- **Location-based filtering** to retain only European events
- **Document classifier** trained on 7,500 manually classified documents (94% accuracy)
- **Event-trigger classifier** using 518 annotated documents to identify protest mentions
- **Manual coding** of remaining documents by human coders

Final dataset reduced to approximately 45,680 documents for manual coding, yielding 33,655 coded events.

## 2) Issue Categories

Complete list from Table 2:

- Economics (private) – firm/employer claims
- Economics (public) – public institution claims
- Environment – environmental protection, energy, infrastructure
- Cultural liberalism – peace, women's rights, LGBTQ, international solidarity, antiracism, migrants' rights
- Regionalism – separatism, regional independence
- Cultural conservatism – countermobilization to cultural liberalism
- Xenophobia – right-wing extremism, racist mobilization, anti-immigration
- Political – representation, corruption, electoral reforms
- Others – uncategorized issues

## 3) Action Form Categories

From Table 2:

- Strikes – industrial action, work stoppages, pickets
- Demonstrations – marches, rallies, camps, meetings, vigils, gatherings
- Petitions and related activities – consumer activism, boycotts, symbolic protests
- Violent protests – sabotage, riots, destruction, clashes with police
- Other protests – remaining action forms

## 4) Total Number of Events

The dataset contains **33,655 unique protest events** across 30 European countries from 2000-2015 (after removing duplicates and irrelevant documents).

## 5) Human Annotation Methodology & Intercoder Reliabi
…[truncated 1827 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_protest-dataset-search_20260520T092905",
  "tool": "WebFetch",
  "elapsed_ms": 2
}
```

</details>

---

### Tool call

_source line 134 · 2026-05-20T09:35:08.167728+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "GLOCON dataset download access \"event type\" categories number samples size statistics"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_protest-dataset-search_20260520T092905",
  "tool": "WebSearch",
  "tool_args": {
    "query": "GLOCON dataset download access \"event type\" categories number samples size statistics"
  }
}
```

</details>

---

### Tool result

_source line 135 · 2026-05-20T09:35:08.167857+00:00_

Web search results for query: ""Mass Mobilization" Clark Regan dataset "news text" OR "article text" OR "text column" OR "notes" OR "source text" variables columns"

Links: [{"title":"Review of Clark/Regan (2016): Mass Mobilization Project","url":"https://discuss-data.net/dataset/4e6a40ff-4ae0-4cc8-89b3-dbe162be07c0/"},{"title":"Mass Mobilization Data Project - Data Catalog","url":"https://datacatalog.library.wayne.edu/dataset/mass-mobilization-data-project"},{"title":"MMD (Mass Mobilization Database) from Clark and Regan (2018): 166... | Download Scientific Diagram","url":"https://www.researchgate.net/figure/MMD-Mass-Mobilization-Database-from-Clark-and-Regan-2018-166-countries-across-South_fig1_352664331"},{"title":"Mass Mobilization dataset - Harvard Dataverse","url":"https://dataverse.harvard.edu/dataverse/MMdata"},{"title":"About the Mass Mobilization Project","url":"https://massmobilization.github.io/about.html"},{"title":"Mass Mobilization Protest Data - dataset by government","url":"https://data.world/government/mass-mobilization-protest-data"},{"title":"Dynamics of Political Protests | International Organization | Cambridge Core","url":"https://www.cambridge.org/core/journals/international-organization/article/abs/dynamics-of-political-protests/FF34963F17453C36ACC88B5C880E156D"},{"title":"DataCite Search","url":"https://search.datacite.org/works/10.7910/dvn/httwyl"},{"title":"Mass Mobilization Protest Data - Mass Mobilization Data Project Dataverse","url":"https://dataverse.harvard.edu/dataset.xhtml?persistentId=doi:10.7910/DVN/HTTWYL"}]

Based on the search results, I found information about the Mass Mobilization dataset by Clark and Regan. Here's what the search revealed:

## Overview
The Mass Mobilization (MM) data are an effort to understand citizen movements against governments, what citizens want when they demonstrate against governments, and how governments respond to citizens. The MM data cover 162 countries between 1990 and 2018, containing events 
…[truncated 1314 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_protest-dataset-search_20260520T092905",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool call

_source line 136 · 2026-05-20T09:35:08.168007+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "SPEED dataset Cline Center download event categories \"civil unrest\" \"political violence\" number of events format"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_protest-dataset-search_20260520T092905",
  "tool": "WebSearch",
  "tool_args": {
    "query": "SPEED dataset Cline Center download event categories \"civil unrest\" \"political violence\" number of events format"
  }
}
```

</details>

---

### Tool call

_source line 137 · 2026-05-20T09:35:08.168132+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://poldem.eui.eu/",
  "prompt": "Extract: 1) Any download links for protest datasets (.dta, .csv, .xlsx). 2) Whether login/registration is required. 3) Terms of use or license mentioned anywhere on the page. 4) Any mention of \"free download\" or \"open access\". 5) All available dataset versions and links."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_protest-dataset-search_20260520T092905",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://poldem.eui.eu/",
    "prompt": "Extract: 1) Any download links for protest datasets (.dta, .csv, .xlsx). 2) Whether login/registration is required. 3) Terms of use or license mentioned anywhere on the page. 4) Any mention of \"free download\" or \"open access\". 5) All available dataset versions and links."
  }
}
```

</details>

---

### Tool call

_source line 138 · 2026-05-20T09:35:08.168280+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "poldem protest dataset download .dta .csv free open access no registration"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_protest-dataset-search_20260520T092905",
  "tool": "WebSearch",
  "tool_args": {
    "query": "poldem protest dataset download .dta .csv free open access no registration"
  }
}
```

</details>

---

### Tool result

_source line 139 · 2026-05-20T09:35:08.168410+00:00_

Web search results for query: "CASE 2021 task2 ACLED 25 event subtypes full list categories "Armed Clash" "Violent demonstration" "Peaceful protest""

Links: [{"title":"ACLED Codebook | ACLED","url":"https://acleddata.com/methodology/acled-codebook"},{"title":"Call for Shared Task Participation at CASE @ ACL-IJCNLP: Socio-political and Crisis Events Detection","url":"https://groups.google.com/g/automated-political-event-collection/c/yArzXzv7cZQ"},{"title":"Call for Participation, Shared Task at the Workshop CASE @ ACL-IJCNLP 2021: Socio-Political and Crisis Events Detection | ACL Member Portal","url":"https://www.aclweb.org/portal/content/call-participation-shared-task-socio-political-and-crisis-events-detection"},{"title":"GitHub - emerging-welfare/case-2021-shared-task: Information and data related to the ProtestNews shared task at CASE @ ACL-IJCNLP 2021 workshop","url":"https://github.com/emerging-welfare/case-2021-shared-task"},{"title":"ACLED Introduces New Event Types and Sub-Event Types | ACLED","url":"https://acleddata.com/2019/03/14/acled-introduces-new-event-types-and-sub-event-types/"},{"title":"IBM MNLP IE at CASE 2021 Task 2: NLI Reranking for Zero ...","url":"https://aclanthology.org/2021.case-1.24.pdf"},{"title":"FAQ: ACLED’s new data structure, terms, and platforms | ACLED","url":"https://acleddata.com/faq-codebook-tools"},{"title":"Emerging Markets Welfare – CASE 2021","url":"https://emw.ku.edu.tr/case-2021/"},{"title":"Classification of ACLED events by type. | Download Scientific Diagram","url":"https://www.researchgate.net/figure/Classification-of-ACLED-events-by-type_tbl1_356786131"},{"title":"What types of events does ACLED code? | ACLED","url":"https://acleddata.com/faq/what-types-events-does-acled-code"}]

Based on the search results, I found information about the CASE 2021 Task 2 and the ACLED 25 event subtypes:

The objective of Task 2 is to evaluate zero-shot learning event classification approaches to classify short text snippets reporting
…[truncated 1302 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_protest-dataset-search_20260520T092905",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 140 · 2026-05-20T09:35:08.168562+00:00_

Web search results for query: "SPEED dataset Cline Center download event categories "civil unrest" "political violence" number of events format"

Links: [{"title":"Social Political Economic Event Dataset (SPEED): Liberia ...","url":"https://databank.illinois.edu/datasets/IDB-7407320"},{"title":"The Social, Political and Economic Event Database Project (SPEED) | Cline Center","url":"https://clinecenter.illinois.edu/project/human-loop-event-data-projects/SPEED"},{"title":"Human-in-the-loop Event Data Projects | Cline Center","url":"https://clinecenter.illinois.edu/project/human-loop-event-data-projects"},{"title":"(PDF) Social Political Economic Event Dataset (SPEED): Liberia, Philippines, and Sierra Leone (1979-2008) Codebook (v.1.0.0) About the Cline Center for Advanced Social Research | Dan Shalmon - Academia.edu","url":"https://www.academia.edu/40213536/Social_Political_Economic_Event_Dataset_SPEED_Liberia_Philippines_and_Sierra_Leone_1979_2008_Codebook_v_1_0_0_About_the_Cline_Center_for_Advanced_Social_Research"},{"title":"Cline Center Historical Phoenix Event Data. Cline Center for Advanced Social Research. v1.3.0. May 4 - Illinois Experts","url":"https://experts.illinois.edu/en/datasets/cline-center-historical-phoenix-event-data-cline-center-for-advan-4/"},{"title":"Civil Unrest Event Data - dataset by history","url":"https://data.world/history/civil-unrest-event-data"},{"title":"Cline Center Coup d’État Project Dataset - Illinois Experts","url":"https://experts.illinois.edu/en/datasets/cline-center-coup-d%C3%A9tat-project-dataset-10/"}]

Based on the search results, here's what I found about the SPEED dataset:

The SPEED (Social, Political and Economic Event Database) project is part of the Cline Center's ongoing work. Each observation represents an event involving civil unrest, repression, or political violence.

The protocols used in SPEED are category-specific electronic documents tailored to the information needs of particular event categories including ci
…[truncated 945 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_protest-dataset-search_20260520T092905",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 141 · 2026-05-20T09:35:08.168720+00:00_

Web search results for query: "GLOCON dataset download access "event type" categories number samples size statistics"

Links: [{"title":"GLOCON – About GLOCON","url":"https://glocon.ku.edu.tr/about-glocon/"},{"title":"Global Contentious Politics Dataset (GLOCON)","url":"https://glocon.ku.edu.tr/"},{"title":"New Dataset Collects Instances of ‘Contentious Politics’ Around the World - Social Science Space","url":"https://www.socialsciencespace.com/2023/12/new-dataset-collects-instances-of-contentious-politics-around-the-world/"},{"title":"GLOCON – Methodology","url":"https://glocon.ku.edu.tr/method/"},{"title":"GLOCON Database: Design Decisions and User Manual (v1.0)","url":"https://arxiv.org/pdf/2405.18613"},{"title":"Socio-political Events of Conflict and Unrest: A Survey of ...","url":"https://aclanthology.org/2024.case-1.5.pdf"},{"title":"GitHub - emerging-welfare/glocongold: The repo is about how to get access to the gold standard corpus that is created and exploited to generate the Global Contention Dataset (GLOCON) · GitHub","url":"https://github.com/emerging-welfare/glocongold"},{"title":"[2405.18613] GLOCON Database: Design Decisions and User Manual (v1.0)","url":"https://arxiv.org/abs/2405.18613"}]

Based on the web search results, here's information about the GLOCON dataset:

## Overview
GLOCON is the first multi-country protest event database for the Global South that uses local sources for automated data collection. It records diverse types of events, including but not limited to demonstrations, rallies, strikes, clashes, and political violence.

## Coverage and Size
The dataset currently contains protest event data from India, South Africa, Argentina, Brazil, and Turkey. As of the inauguration of the website, it contains 621,290 events from 9,509,193 news documents.

## Event Type Categories
Event categories are automatically predicted and include categories such as "Demonstration." The dataset includes various event types as indicators of contentious pol
…[truncated 783 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_protest-dataset-search_20260520T092905",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 142 · 2026-05-20T09:35:08.168873+00:00_

Web search results for query: "poldem protest dataset download .dta .csv free open access no registration"

Links: [{"title":"Data Portal on Political Conflict and Democracy in Europe (PolDem) | WZB","url":"https://www.wzb.eu/en/research/dynamics-of-political-systems/center-for-civil-society-research/projects/daten-portal-zu-politischen-konflikten-und-protest-in-europa"},{"title":"1 PolDem – Protest Dataset on EU Issues - Version 1 - poldem-protest_eu","url":"https://poldem.eui.eu/downloads/pea/poldem-protest_eu_codebook.pdf"},{"title":"1 PolDem – Protest Dataset 30 European countries - Version 1 -","url":"https://poldem.eui.eu/downloads/pea/poldem-protest_30_codebook.pdf"},{"title":"1 PolDem – Protest Event Dataset 30 - Version 1 - Please cite as:","url":"https://poldem.eui.eu/downloads/pea/PEA_documentation_v1.pdf"},{"title":"PolDem - Observatory for Political Conflict and Democracy in Europe","url":"https://poldem.eui.eu/"},{"title":"PolDem - Observatory for Political Conflict and Democracy in Europe • Political Sociology • Department of Political and Social Sciences","url":"https://www.polsoz.fu-berlin.de/en/soziologie/arbeitsbereiche/politische-soziologie/ressourcen/research/dataportal.html"},{"title":"PolData/PolData.csv at master · erikgahner/PolData","url":"https://github.com/erikgahner/PolData/blob/master/PolData.csv"},{"title":"Protest Events - PolDem","url":"https://poldem.eui.eu/download/protest-events/"},{"title":"Data Overview - PolDem - European University Institute","url":"https://poldem.eui.eu/data-overview/"}]

Based on the search results, here's what I found about the PolDem protest dataset:

The PolDem (Observatory for Political Conflict and Democracy) is a platform that produces and houses data on protest events, election campaigns, and issue-specific public contestation covering a wide-range of European countries over a long period of time. The core of PolDem includes data on protest events in 30 European countries obtained by coding media cove
…[truncated 887 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_protest-dataset-search_20260520T092905",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 143 · 2026-05-20T09:35:08.169021+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "ACLED sub-event types full list 25 \"Armed clash\" \"Government regains territory\" \"Non-state actor overtakes territory\" \"Peaceful protest\" \"Protest with intervention\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_protest-dataset-search_20260520T092905",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ACLED sub-event types full list 25 \"Armed clash\" \"Government regains territory\" \"Non-state actor overtakes territory\" \"Peaceful protest\" \"Protest with intervention\""
  }
}
```

</details>

---

### Tool call

_source line 144 · 2026-05-20T09:35:08.169153+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "CASE 2022 task1 subtask document classification protest dataset languages sample size train test split"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_protest-dataset-search_20260520T092905",
  "tool": "WebSearch",
  "tool_args": {
    "query": "CASE 2022 task1 subtask document classification protest dataset languages sample size train test split"
  }
}
```

</details>

---

### Tool result

_source line 145 · 2026-05-20T09:35:08.169297+00:00_

# PolDem Data Access Analysis

Based on the webpage content provided, here's what I found:

## 1. Download Links for Protest Datasets
The page references a "Download" section at `https://poldem.eui.eu/download/`, but **no direct file links (.dta, .csv, .xlsx) are displayed** on this homepage.

## 2. Login/Registration Requirements
**No information provided** about whether authentication is needed to access datasets.

## 3. Terms of Use or License
**Not mentioned** on this page. The footer only states "© 2026 - EUI & WZB. All rights reserved."

## 4. "Free Download" or "Open Access" Language
**Not present** on the homepage. The page uses neutral phrasing like "Download" and "Data Overview" without explicitly stating access restrictions or cost.

## 5. Dataset Versions Available
The page mentions these datasets:
- **poldem-protest_30** (Protest Event Dataset covering 30 European countries)
- **poldem-election_all** (Election Campaigns Dataset)

However, **no version numbers, dates, or direct download links are provided** on this page.

## Recommendation
To obtain actual dataset files and access terms, you would need to visit the linked "Download" or "Explore" pages directly.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_protest-dataset-search_20260520T092905",
  "tool": "WebFetch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool call

_source line 146 · 2026-05-20T09:35:08.169432+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://poldem.eui.eu/download/protest-events/",
  "prompt": "Extract ALL information from this page: 1) All download links and file formats available. 2) Whether login/registration is required. 3) Terms of use or license. 4) Dataset versions. 5) Any instructions for downloading. 6) Direct URLs to data files."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_protest-dataset-search_20260520T092905",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://poldem.eui.eu/download/protest-events/",
    "prompt": "Extract ALL information from this page: 1) All download links and file formats available. 2) Whether login/registration is required. 3) Terms of use or license. 4) Dataset versions. 5) Any instructions for downloading. 6) Direct URLs to data files."
  }
}
```

</details>

---

### Tool result

_source line 147 · 2026-05-20T09:35:08.169563+00:00_

Web search results for query: "ACLED sub-event types full list 25 "Armed clash" "Government regains territory" "Non-state actor overtakes territory" "Peaceful protest" "Protest with intervention""

Links: [{"title":"ACLED Introduces New Event Types and Sub-Event Types | ACLED","url":"https://acleddata.com/2019/03/14/acled-introduces-new-event-types-and-sub-event-types/"},{"title":"ACLED Codebook | ACLED","url":"https://acleddata.com/methodology/acled-codebook"},{"title":"FAQ: ACLED’s new data structure, terms, and platforms | ACLED","url":"https://acleddata.com/faq-codebook-tools"},{"title":"What types of events does ACLED code? | ACLED","url":"https://acleddata.com/faq/what-types-events-does-acled-code"},{"title":"Armed Conflict Location & Event Data Project CODEBOOK","url":"https://acleddata.com/sites/default/files/wp-content-archive/uploads/dlm_uploads/2023/06/ACLED_Codebook_2023.pdf"},{"title":"1 ACLED Definitions of Political Violence and Protest","url":"https://acleddata.com/sites/default/files/wp-content-archive/uploads/2021/11/ACLED_Event-Definitions_v1_April-2019.pdf"},{"title":"1 Armed Conflict Location and Event Data Project (ACLED) Codebook 2015","url":"https://www.strausscenter.org/wp-content/uploads/ACLED_Codebook_2015.pdf"},{"title":"Armed Conflict Location & Event Data CODEBOOK","url":"https://acleddata.com/sites/default/files/wp-content-archive/uploads/dlm_uploads/2024/10/ACLED-Codebook-2024-7-Oct.-2024.pdf"},{"title":"Classification of ACLED events by type. | Download Scientific Diagram","url":"https://www.researchgate.net/figure/Classification-of-ACLED-events-by-type_tbl1_356786131"},{"title":"Armed Conflict Location & Event Data Project (ACLED) Humanitarian Data | 246 Datasets | HDX","url":"https://data.humdata.org/organization/acled"}]

Based on the search results, I found information about ACLED's sub-event types. ACLED currently records six event types and 25 sub-event types, both violent and non-violent. Sub-event types are also categorized b
…[truncated 1039 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_protest-dataset-search_20260520T092905",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 148 · 2026-05-20T09:35:08.169704+00:00_

# PolDem Protest Events Dataset - Information Summary

## Download Links & File Formats
Three dataset versions are available with both CSV and Stata (.DTA) formats:

1. **poldem-protest_30**: [CSV](https://poldem.eui.eu/downloads/pea/poldem-protest_30.csv) | [DTA](https://poldem.eui.eu/downloads/pea/poldem-protest_30.dta)
2. **poldem-protest_6**: [CSV](https://poldem.eui.eu/downloads/pea/poldem-protest_6.csv) | [DTA](https://poldem.eui.eu/downloads/pea/poldem-protest_6.dta)
3. **poldem-protest_eu**: [CSV](https://poldem.eui.eu/downloads/pea/poldem-protest_eu.csv) | [DTA](https://poldem.eui.eu/downloads/pea/poldem-protest_eu.dta)

## Login/Registration Requirement
**Not specified** - The page contains no mention of authentication requirements.

## Terms of Use or License
**Not provided** - No explicit license or terms of use are detailed on this page.

## Download Instructions
**None given** - The page offers direct download links without step-by-step guidance.

## Additional Information
- Contact: poldem@eui.eu (EUI) and poldem@wzb.eu (WZB Berlin)
- Related resources include codebooks, citation guidelines, and data exploration tools accessible through the main navigation

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_protest-dataset-search_20260520T092905",
  "tool": "WebFetch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 149 · 2026-05-20T09:35:08.169876+00:00_

Based on comprehensive web searches, here is the report:

```
数据集名称: Mass Mobilization Data Project (MMD / MMP)
         作者: David H. Clark (Binghamton University) & Patrick M. Regan (University of Notre Dame)

类别数 K: 
  - 抗议者诉求 (protester demand): 7 类
  - 政府响应 (government response): 7 类

类别列表:
  Protester demands: [labor/wages, land, police brutality, political process, prices/taxes, removal of politician, social restrictions]
  Government responses: [accommodation, arrests, beatings, crowd dispersal, ignore, killings, shootings]
  注意：每个事件可以同时有多个 demand 和多个 response（multi-label）

样本量: ~17,000+ 事件（162 个国家，1990–2020），每条记录对应一次 50 人以上的抗议事件

License: Harvard Dataverse 默认 CC0 Public Domain Dedication（该数据集未见特殊限制说明），可用于学术/ML 研究

下载方式: 
  - Harvard Dataverse: https://dataverse.harvard.edu/dataset.xhtml?persistentId=doi:10.7910/DVN/HTTWYL
  - 官网: https://massmobilization.github.io/
  - data.world 镜像: https://data.world/government/mass-mobilization-protest-data
  - 无需申请/审批，直接下载

Gold-standard human labels: 是
  标注方式：人工编码员从 Lexis-Nexis 检索新闻报道（主要来源为 NYT、Washington Post、Christian Science Monitor、Times of London），
  按 codebook 标准对每起抗议事件的诉求类型、政府响应、规模、地点等进行手工编码。

引用论文: 
  - 数据集引用: Clark, David H.; Regan, Patrick M., 2016, "Mass Mobilization Protest Data", 
    https://doi.org/10.7910/DVN/HTTWYL, Harvard Dataverse
  - 相关分析论文: Klein, Graig R. and Patrick M. Regan. 2018. "Dynamics of Political Protests." 
    International Organization 72(2): 485-521.

备注:
  1. 该数据集是结构化事件数据（tabular），不含原始新闻文本。变量为编码后的分类标签（demand/response 为 0/1 二值列）、
     数值（protest size）和元数据（country, date, location）。如果用于 NLP 文本分类任务，
     需要自行匹配/获取原始新闻文本——数据集本身不提供 article text。
  2. Demand 和 response 都是 multi-label 设定（K=7 但非互斥），不是单标签 K 分类。
     作为 K>=3 的分类任务可行，但需注意 multi-label 性质。
  3. 另有 Mass Mobilization in Autocracies Database (MMAD, mmadatabase.org) 是独立扩展版，
     覆盖独裁国家，使用 AP/AFP/BBC Monitoring + ML 预筛选 + 人工编码，与 Clark/Regan 的 MMD 是不同数据集。
```
agentId: a8e25cafc895a96c2 (use SendMessage with to: 'a8e25cafc895a96c2' to co
…[truncated 87 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_protest-dataset-search_20260520T092905",
  "tool": "Agent",
  "elapsed_ms": 21
}
```

</details>

---

### Tool call

_source line 150 · 2026-05-20T09:35:08.170035+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "curl -sI \"https://poldem.eui.eu/downloads/pea/poldem-protest_30.csv\" 2>&1 | head -20",
  "description": "Check HTTP headers to verify if CSV file is freely downloadable without auth"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_protest-dataset-search_20260520T092905",
  "tool": "Bash",
  "tool_args": {
    "command": "curl -sI \"https://poldem.eui.eu/downloads/pea/poldem-protest_30.csv\" 2>&1 | head -20",
    "description": "Check HTTP headers to verify if CSV file is freely downloadable without auth"
  }
}
```

</details>

---

### Tool result

_source line 151 · 2026-05-20T09:35:08.170154+00:00_

HTTP/1.1 200 OK
Date: Wed, 20 May 2026 09:31:55 GMT
Server: Apache/2.4.29 (Ubuntu)
Last-Modified: Fri, 03 Apr 2020 11:32:14 GMT
ETag: "8899af-5a26144d6ab80"
Accept-Ranges: bytes
Content-Length: 8952239
Content-Type: text/csv
Set-Cookie: [REDACTED];Expires=Thu, 20 May 2027 09:31:56 GMT;Path=/;HttpOnly

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_protest-dataset-search_20260520T092905",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 152 · 2026-05-20T09:35:08.170300+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "curl -s \"https://poldem.eui.eu/downloads/pea/poldem-protest_30.csv\" 2>&1 | head -5",
  "description": "Download first 5 lines of CSV to check column names and content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_protest-dataset-search_20260520T092905",
  "tool": "Bash",
  "tool_args": {
    "command": "curl -s \"https://poldem.eui.eu/downloads/pea/poldem-protest_30.csv\" 2>&1 | head -5",
    "description": "Download first 5 lines of CSV to check column names and content"
  }
}
```

</details>

---

### Tool result

_source line 153 · 2026-05-20T09:35:08.170449+00:00_

Web search results for query: "CASE 2022 task1 subtask document classification protest dataset languages sample size train test split"

Links: [{"title":"NSUT-NLP at CASE 2022 Task 1: Multilingual Protest Event Detection using Transformer-based Models - ACL Anthology","url":"https://aclanthology.org/2022.case-1.23/"},{"title":"Extended Multilingual Protest News Detection - Shared Task 1, CASE 2021 and 2022 - ACL Anthology","url":"https://aclanthology.org/2022.case-1.31/"},{"title":"CEIA-NLP at CASE 2022 Task 1: Protest News Detection ...","url":"https://aclanthology.org/2022.case-1.26.pdf"},{"title":"ClassBases at the CASE-2022 Multilingual Protest Event Detection Task: Multilingual Protest News Detection and Automatically Replicating Manually Created Event Datasets - ACL Anthology","url":"https://aclanthology.org/2022.case-1.21/"},{"title":"ClassBases at the CASE-2022 Multilingual Protest Event ...","url":"https://aclanthology.org/2022.case-1.21.pdf"},{"title":"[2211.11360] Extended Multilingual Protest News Detection -- Shared Task 1, CASE 2021 and 2022","url":"https://arxiv.org/abs/2211.11360"},{"title":"[2301.06617] ClassBases at CASE-2022 Multilingual Protest Event Detection Tasks: Multilingual Protest News Detection and Automatically Replicating Manually Created Event Datasets","url":"https://arxiv.org/abs/2301.06617"},{"title":"GitHub - emerging-welfare/case-2021-shared-task: Information and data related to the ProtestNews shared task at CASE @ ACL-IJCNLP 2021 workshop","url":"https://github.com/emerging-welfare/case-2021-shared-task"}]

Let me search for more specific information about the dataset details, including languages, sample size, and train/test split.

Links: [{"title":"Extended Multilingual Protest News Detection -- Shared Task 1, CASE 2021   and 2022","url":"https://arxiv.org/pdf/2211.11360"},{"title":"Investigating data partitioning strategies for crosslinguistic   low-resource ASR evaluation","url":"https://arxiv.org/pdf/2208.12888"},{"title":"
…[truncated 5753 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_protest-dataset-search_20260520T092905",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 154 · 2026-05-20T09:35:08.170592+00:00_

id_doc,id_coder,id_event,entry_time,doc_country,doc_publdate,doc_source,doc_probability,event_index,event_n,country_name,country_size,community,date,month,year,period,action_form,radical_action,part_all,big_event,issue_econ_private,issue_econ_public,issue_cult_lib,issue_environment,issue_political,issue_regional,issue_cult_cons,issue_xeno,issue_other,issue_dontknow,issue_missing,actor_party_left,actor_party_right,actor_party_unknown,actor_union_private,actor_union_public,actor_union_both,actor_union_unknown,actor_group_pens,actor_group_stud,actor_group_occup,actor_group_other,actor_other,actor_dontknow,actor_missing,weight_sample,weight_newswire,weight_country,weighted_event,weighted_part_all
924,13,3930,2016-05-03 19:59:46,norway,2000-09-12,DPA,.71601903,3,1,austria,8.6000004,vienna,2000-01-01,1,2000,normal times,demonstrations,not radical,1250,no,no,no,no,no,yes,no,no,no,no,no,no,no,no,no,no,no,no,no,no,no,no,no,no,no,yes,.5,1,3.1517622,.63456565,793.20703
2072,30,19716,2016-05-07 18:26:15,austria,2001-06-20,CTK,.96823615,1,1,austria,8.6000004,austria (entire country),2000-01-01,1,2000,normal times,"petitions, symbolic actions",not radical,60000,no,no,no,no,yes,no,no,no,no,no,no,no,no,no,no,no,no,no,no,no,no,no,no,no,no,yes,.25 sample,1,3.1517622,.31728283,19036.969
2490,30,19781,2016-05-08 21:44:48,austria,2001-10-21,CTK,.91951966,1,1,austria,8.6000004,weigetschlag,2000-01-01,1,2000,normal times,demonstrations,not radical,100,no,no,no,no,yes,no,no,no,no,no,no,no,no,no,no,no,no,no,no,no,no,no,no,no,no,yes,.25 sample,1,3.1517622,.31728283,31.728281
30,1,10347,2016-04-21 23:15:29,slovenia,2000-01-13,CTK,.80277473,1,1,austria,8.6000004,vienna,2000-01-13,1,2000,normal times,"petitions, symbolic actions",not radical,4096,no,no,no,no,no,no,yes,no,no,no,no,no,no,no,no,no,no,no,no,no,no,no,no,yes,no,no,.25 sample,1,3.1517622,.31728283,1299.5905

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_protest-dataset-search_20260520T092905",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 155 · 2026-05-20T09:35:08.170726+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "curl -s \"https://poldem.eui.eu/downloads/pea/poldem-protest_30.csv\" 2>&1 | wc -l",
  "description": "Count total rows in the poldem-protest_30 CSV"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_protest-dataset-search_20260520T092905",
  "tool": "Bash",
  "tool_args": {
    "command": "curl -s \"https://poldem.eui.eu/downloads/pea/poldem-protest_30.csv\" 2>&1 | wc -l",
    "description": "Count total rows in the poldem-protest_30 CSV"
  }
}
```

</details>

---

### Tool call

_source line 156 · 2026-05-20T09:35:08.170852+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "CASE 2021 shared task data statistics \"number of documents\" OR \"sample size\" task1 subtask1 English Hindi"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_protest-dataset-search_20260520T092905",
  "tool": "WebSearch",
  "tool_args": {
    "query": "CASE 2021 shared task data statistics \"number of documents\" OR \"sample size\" task1 subtask1 English Hindi"
  }
}
```

</details>

---

### Tool call

_source line 157 · 2026-05-20T09:35:08.170976+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "huggingface \"protest\" OR \"political event\" dataset text classification multi-class labels",
  "allowed_domains": "['huggingface.co']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_protest-dataset-search_20260520T092905",
  "tool": "WebSearch",
  "tool_args": {
    "query": "huggingface \"protest\" OR \"political event\" dataset text classification multi-class labels",
    "allowed_domains": "['huggingface.co']"
  }
}
```

</details>

---

### Tool result

_source line 158 · 2026-05-20T09:35:08.171106+00:00_

Web search results for query: "CASE 2021 shared task data statistics "number of documents" OR "sample size" task1 subtask1 English Hindi"

Links: [{"title":"GitHub - emerging-welfare/case-2021-shared-task: Information and data related to the ProtestNews shared task at CASE @ ACL-IJCNLP 2021 workshop","url":"https://github.com/emerging-welfare/case-2021-shared-task"},{"title":"Multilingual Protest News Detection - Shared Task 1, CASE 2021 | Request PDF","url":"https://www.researchgate.net/publication/353490567_Multilingual_Protest_News_Detection_-_Shared_Task_1_CASE_2021"},{"title":"Call for Participation, Shared Task at the Workshop CASE @ ACL-IJCNLP 2021: Socio-Political and Crisis Events Detection | ACL Member Portal","url":"https://www.aclweb.org/portal/content/call-participation-shared-task-socio-political-and-crisis-events-detection"},{"title":"(PDF) Multilingual Protest News Detection - Shared Task 1, CASE 2021","url":"https://www.academia.edu/64931265/Multilingual_Protest_News_Detection_Shared_Task_1_CASE_2021"},{"title":"Call for Shared Task Participation at CASE @ ACL-IJCNLP: Socio-political and Crisis Events Detection","url":"https://groups.google.com/g/automated-political-event-collection/c/yArzXzv7cZQ"},{"title":"(PDF) Discovering Black Lives Matter Events in the United States: Shared Task 3, CASE 2021","url":"https://www.academia.edu/64357373/Discovering_Black_Lives_Matter_Events_in_the_United_States_Shared_Task_3_CASE_2021"},{"title":"Shared Task on Multilingual protest news detection CASE ...","url":"https://competitions.codalab.org/competitions/31247"},{"title":"Handshakes AI Research at CASE 2021 Task 1: Exploring different   approaches for multilingual tasks","url":"https://arxiv.org/pdf/2110.15599"},{"title":"CALCS 2021 Shared Task: Machine Translation for Code-Switched Data","url":"https://arxiv.org/pdf/2202.09625"}]

Based on the search results, I found relevant information about the CASE 2021 shared task. The results show information about Task
…[truncated 1060 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_protest-dataset-search_20260520T092905",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 159 · 2026-05-20T09:35:08.171269+00:00_

30853

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_protest-dataset-search_20260520T092905",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 160 · 2026-05-20T09:35:08.171394+00:00_

Web search results for query: "huggingface "protest" OR "political event" dataset text classification multi-class labels"

Links: [{"title":"cjerzak/TextQuantificationDatasets · Datasets at Hugging Face","url":"https://huggingface.co/datasets/cjerzak/TextQuantificationDatasets"},{"title":"valurank/PoliticalBias · Datasets at Hugging Face","url":"https://huggingface.co/datasets/valurank/PoliticalBias"},{"title":"cajcodes/political-bias · Datasets at Hugging Face","url":"https://huggingface.co/datasets/cajcodes/political-bias"},{"title":"fmplaza/offendes · Datasets at Hugging Face","url":"https://huggingface.co/datasets/fmplaza/offendes"},{"title":"Multitask Models for Supervised Protests Detection in Texts","url":"https://arxiv.org/pdf/2005.02954"},{"title":"README.md · cajcodes/political-bias at main","url":"https://huggingface.co/datasets/cajcodes/political-bias/blob/main/README.md"},{"title":"ethos · Datasets at Hugging Face","url":"https://huggingface.co/datasets/ethos"},{"title":"Cross-context News Corpus for Protest Events related Knowledge Base   Construction","url":"https://arxiv.org/pdf/2008.00351"},{"title":"mlburnham/Political_DEBATE_base_v1.0 · Hugging Face","url":"https://huggingface.co/mlburnham/Political_DEBATE_base_v1.0"}]

Based on my search results, here are some relevant Hugging Face datasets and resources for protest/political event text classification:

## Datasets Found:

1. **TextQuantificationDatasets** - A multi-class classification dataset tagged with text-classification, social-science, and politics.

2. **Political Bias Dataset** (cajcodes/political-bias) - Contains 658 synthetic statements annotated with bias ratings from 0 to 4, representing a spectrum from highly conservative to highly liberal.

3. **Offensive Language Detection** (fmplaza/offendes) - Intended for multi-class offensive classification and binary offensive classification, with categories including political ideology.

## Related Research:

The search also revealed academi
…[truncated 772 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_protest-dataset-search_20260520T092905",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 161 · 2026-05-20T09:35:08.171540+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "curl -s \"https://poldem.eui.eu/downloads/pea/poldem-protest_30.csv\" 2>&1 | head -1 | tr ',' '\\n' | grep -n \"action_form\\|issue_\"",
  "description": "List action_form and issue columns with their positions"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_protest-dataset-search_20260520T092905",
  "tool": "Bash",
  "tool_args": {
    "command": "curl -s \"https://poldem.eui.eu/downloads/pea/poldem-protest_30.csv\" 2>&1 | head -1 | tr ',' '\\n' | grep -n \"action_form\\|issue_\"",
    "description": "List action_form and issue columns with their positions"
  }
}
```

</details>

---

### Tool result

_source line 162 · 2026-05-20T09:35:08.171656+00:00_

18:action_form
22:issue_econ_private
23:issue_econ_public
24:issue_cult_lib
25:issue_environment
26:issue_political
27:issue_regional
28:issue_cult_cons
29:issue_xeno
30:issue_other
31:issue_dontknow
32:issue_missing

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_protest-dataset-search_20260520T092905",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 163 · 2026-05-20T09:35:08.171774+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "curl -s \"https://poldem.eui.eu/downloads/pea/poldem-protest_30.csv\" 2>&1 | cut -d',' -f18 | sort | uniq -c | sort -rn",
  "description": "Count unique values in action_form column (column 18)"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_protest-dataset-search_20260520T092905",
  "tool": "Bash",
  "tool_args": {
    "command": "curl -s \"https://poldem.eui.eu/downloads/pea/poldem-protest_30.csv\" 2>&1 | cut -d',' -f18 | sort | uniq -c | sort -rn",
    "description": "Count unique values in action_form column (column 18)"
  }
}
```

</details>

---

### Tool result

_source line 164 · 2026-05-20T09:35:08.171892+00:00_

  13327 demonstrations
   6224 violent protest
   5176 strikes
   2594 "confrontations
   2447 "petitions
   1080 other protest
      3 2006
      1 action_form
      1  baia mare

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_protest-dataset-search_20260520T092905",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 165 · 2026-05-20T09:35:08.172008+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "curl -s \"https://poldem.eui.eu/downloads/pea/poldem-protest_30.csv\" 2>&1 | awk -F',' '{print $18}' | sed 's/^\"//;s/\"$//' | sort | uniq -c | sort -rn | head -20",
  "description": "Get clean action_form values with proper CSV parsing"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_protest-dataset-search_20260520T092905",
  "tool": "Bash",
  "tool_args": {
    "command": "curl -s \"https://poldem.eui.eu/downloads/pea/poldem-protest_30.csv\" 2>&1 | awk -F',' '{print $18}' | sed 's/^\"//;s/\"$//' | sort | uniq -c | sort -rn | head -20",
    "description": "Get clean action_form values with proper CSV parsing"
  }
}
```

</details>

---

### Tool result

_source line 166 · 2026-05-20T09:35:08.172126+00:00_

  13327 demonstrations
   6224 violent protest
   5176 strikes
   2594 confrontations
   2447 petitions
   1080 other protest
      3 2006
      1 action_form
      1  baia mare

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_protest-dataset-search_20260520T092905",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 167 · 2026-05-20T09:35:08.172267+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "# Check the issue columns: each is binary (yes/no), count how many events have each issue\ncurl -s \"https://poldem.eui.eu/downloads/pea/poldem-protest_30.csv\" 2>&1 | python3 -c \"\nimport csv, sys\nreader = csv.DictReader(sys.stdin)\nissue_cols = ['issue_econ_private','issue_econ_public','issue_cult_lib','issue_environment','issue_political','issue_regional','issue_cult_cons','issue_xeno','issue_other','issue_dontknow','issue_missing']\ncounts = {c:0 for c in issue_cols}\ntotal = 0\nfor row in reader:\n    total += 1\n    for c in issue_cols:\n        if row.get(c,'').strip().lower() == 'yes':\n            counts[c] += 1\nprint(f'Total rows: {total}')\nfor c in issue_cols:\n    print(f'{c}: {counts[c]} ({100*counts[c]/total:.1f}%)')\n\"",
  "description": "Count binary issue category distributions"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_protest-dataset-search_20260520T092905",
  "tool": "Bash",
  "tool_args": {
    "command": "# Check the issue columns: each is binary (yes/no), count how many events have each issue\ncurl -s \"https://poldem.eui.eu/downloads/pea/poldem-protest_30.csv\" 2>&1 | python3 -c \"\nimport csv, sys\nreader = csv.DictReader(sys.stdin)\nissue_cols = ['issue_econ_private','issue_econ_public','issue_cult_lib','issue_environment','issue_political','issue_regional','issue_cult_cons','issue_xeno','issue_other','issue_dontknow','issue_missing']\ncounts = {c:0 for c in issue_cols}\ntotal = 0\nfor row in reader:\n    total += 1\n    for c in issue_cols:\n        if row.get(c,'').strip().lower() == 'yes':\n            counts[c] += 1\nprint(f'Total rows: {total}')\nfor c in issue_cols:\n    print(f'{c}: {counts[c]} ({100*counts[c]/total:.1f}%)')\n\"",
    "description": "Count binary issue category distributions"
  }
}
```

</details>

---

### Tool result

_source line 168 · 2026-05-20T09:35:08.172392+00:00_

Total rows: 30852
issue_econ_private: 3769 (12.2%)
issue_econ_public: 9247 (30.0%)
issue_cult_lib: 5240 (17.0%)
issue_environment: 2051 (6.6%)
issue_political: 4678 (15.2%)
issue_regional: 2212 (7.2%)
issue_cult_cons: 903 (2.9%)
issue_xeno: 1806 (5.9%)
issue_other: 3339 (10.8%)
issue_dontknow: 21 (0.1%)
issue_missing: 1304 (4.2%)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_protest-dataset-search_20260520T092905",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 169 · 2026-05-20T09:35:08.172555+00:00_

Now I have all the information needed. Here is the report:

---

```
数据集名称: PolDem – Protest Dataset 30 European Countries (poldem-protest_30), Version 1
类别数 K: 
  - action_form (抗议形式): 6 类
  - issue (议题): 9 实质类 + 2 缺失/不知道类 = 11 列 (binary multi-label)
类别列表:
  action_form:
    1. demonstrations (13,327 events, 43.2%)
    2. violent protest (6,224, 20.2%)
    3. strikes (5,176, 16.8%)
    4. confrontations (2,594, 8.4%)
    5. petitions, symbolic actions (2,447, 7.9%)
    6. other protest (1,080, 3.5%)
  issue (multi-label binary columns):
    1. issue_econ_private — 企业/雇主相关经济议题 (12.2%)
    2. issue_econ_public — 公共机构相关经济议题 (30.0%)
    3. issue_cult_lib — 文化自由主义 (和平/女权/LGBTQ/反种族主义/移民权利) (17.0%)
    4. issue_environment — 环境/能源/基础设施 (6.6%)
    5. issue_political — 政治议题 (腐败/选举改革/代表权) (15.2%)
    6. issue_regional — 地区主义/分离主义 (7.2%)
    7. issue_cult_cons — 文化保守主义 (2.9%)
    8. issue_xeno — 仇外/右翼极端主义/反移民 (5.9%)
    9. issue_other — 其他 (10.8%)
    10. issue_dontknow (0.1%)
    11. issue_missing (4.2%)
样本量: 30,852 行 (对应约 33,655 coded events，论文原文数字；CSV 去重后 30,852 条记录)
License: 未在网站明确标注。但方法论论文 (Lorenzini et al., 2022) 以 CC BY 4.0 发表。数据集本身在 poldem.eui.eu 上无登录即可直接下载，无明确 license 声明，页脚标注 "© EUI & WZB. All rights reserved."
下载方式: 免费直接下载，无需注册/登录/申请
  - CSV: https://poldem.eui.eu/downloads/pea/poldem-protest_30.csv (约 8.5 MB)
  - Stata: https://poldem.eui.eu/downloads/pea/poldem-protest_30.dta
  - Codebook: https://poldem.eui.eu/downloads/pea/poldem-protest_30_codebook.pdf
  - Documentation: https://poldem.eui.eu/downloads/pea/PEA_documentation_v1.pdf
  - 下载页面: https://poldem.eui.eu/download/protest-events/
Gold-standard human labels: 部分是，质量中等
  - 标注方式: 半自动流程 (semi-automated NLP pipeline)。先用关键词检索 520 万新闻文档，经去重/过滤/分类器筛选后，由 35 名研究生人工编码 45,680 篇文档（耗时 642 个工作日）
  - Intercoder reliability: 事件识别 F1 = 0.60 (SD 0.06)；议题 Cohen's κ = 0.53 (SD 0.13)；行动者 κ = 0.57；参与人数 κ = 0.45
  - 作者明确指出任务对人类编码者来说也"困难"，标注一致性属于 "fair to good"，并非高一致性 gold standard
引用论文:
  - 数据集: Kriesi, H., Wüest, B., Lorenzini,
…[truncated 1947 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_protest-dataset-search_20260520T092905",
  "tool": "Agent",
  "elapsed_ms": 24
}
```

</details>

---

### Tool result

_source line 170 · 2026-05-20T09:35:08.172813+00:00_

Now I have enough information to compile a thorough report. Here are my findings:

---

## Protest/Political Event Multi-Class Text Classification Datasets

### 1. CASE 2021 Task 2 -- Fine-Grained Socio-Political Event Classification

```
数据集名称: CASE 2021 Shared Task 2 (Fine-Grained Event Classification)
类别数 K: 25 (main task) + 3 zero-shot + 2 surprise = 30 total
类别列表: ACLED 25 sub-event types, including Armed Clash, Government Regains Territory, 
  Non-state Actor Overtakes Territory, Violent Demonstration, Peaceful Protest, 
  Protest with Intervention, Excessive Force Against Protesters, Mob Violence, 
  Chemical Weapon, Air/Drone Strike, Suicide Bomb, Shelling/Artillery/Missile Attack, 
  Remote Explosive/Landmine/IED, Grenade, Sexual Violence, Attack, Abduction/Forced 
  Disappearance, Agreement, Arrests, Change to Group Activity, Disrupted Weapons Use, 
  Headquarters or Base Established, Looting/Property Destruction, 
  Non-violent Transfer of Territory, Other
样本量: ~600K short event descriptions (from ACLED text snippets)
License: 学术用途（需通过 ACLED 获取原始数据）
下载方式: https://github.com/emerging-welfare/case-2021-shared-task (task2 文件夹含测试集 TSV)；
  训练数据需从 ACLED https://acleddata.com/ 获取
Gold-standard human labels: 是 (ACLED 专业编码员标注)
引用论文: Haneczok et al. "Fine-grained Event Classification in News-like Text Snippets - 
  Shared Task 2, CASE 2021" (ACL Anthology 2021.case-1.23)
备注: 测试集含标签可直接下载；训练数据建议从 ACLED 导出工具获取。K=25 是核心类别，
  非常适合多分类研究。涵盖政治暴力、示威、战略发展三大类。
```

### 2. CASE 2021/2022 Task 1 -- Multilingual Protest News Detection

```
数据集名称: CASE Shared Task 1 (Multilingual Protest News Detection)
类别数 K: Subtask 1 为二分类 (protest-related / not)；Subtask 2 为句子级二分类
类别列表: [protest-related, not protest-related] (文档级)；[event sentence, non-event sentence] (句子级)
样本量: Subtask 2 句子分类约 26,208 sentences；文档级数据涵盖多语言
License: 公开（GitHub 直接下载）
下载方式: https://github.com/emerging-welfare/case-2021-shared-task (task1 文件夹)
  CASE 2022: https://github.com/emerging-welfare/case-2022-multilingual-eve
…[truncated 10762 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_protest-dataset-search_20260520T092905",
  "tool": "Agent",
  "elapsed_ms": 23
}
```

</details>

---

### Assistant

_source line 171 · 2026-05-20T09:35:08.173057+00:00_

## 搜索结果汇总

**关键前提**：ACLED ToS 禁止 ML 用途，因此 ACLED 本身和依赖 ACLED 训练数据的 CASE 2021 Task 2 均排除。

---

### 符合条件的候选

#### 1. PolDem Protest Dataset 30
```
数据集名称: PolDem-Protest Dataset 30 (poldem-protest_30)
类别数 K: action_form = 6 (单标签); issue = 9 (多标签)
类别列表 (action_form): [demonstrations, violent protest, strikes, confrontations, 
  petitions/symbolic actions, other protest]
样本量: 30,852 events (30 European countries, 2000-2015)
License: 未明确标注，页脚 "© EUI & WZB. All rights reserved."
下载方式: 直接下载，无需注册
  CSV: https://poldem.eui.eu/downloads/pea/poldem-protest_30.csv
Gold-standard human labels: 半自动流程 + 35名编码员人工标注
  intercoder: 事件识别 F1=0.60, 议题 κ=0.53
引用论文: Lorenzini et al. (2022) American Behavioral Scientist
备注: 
  ⚠️ 结构化事件数据，不含原始新闻全文（来源为通讯社 newswire，但 CSV 中可能只有编码字段）
  ⚠️ License 模糊，"All rights reserved" 有风险
  ✅ action_form K=6 单标签分类，标注质量中等，适合研究标注噪声
```

#### 2. Mass Mobilization Project (MMD)
```
数据集名称: Mass Mobilization Data Project
类别数 K: protester demand = 7 (多标签); government response = 7 (多标签)
类别列表 (demand): [labor/wages, land, police brutality, political process, 
  prices/taxes, removal of politician, social restrictions]
样本量: ~17,000 events (162 countries, 1990-2020)
License: Harvard Dataverse (CC0 Public Domain)
下载方式: https://dataverse.harvard.edu/dataset.xhtml?persistentId=doi:10.7910/DVN/HTTWYL
Gold-standard human labels: 是，人工编码员从 Lexis-Nexis 新闻编码
引用论文: Clark & Regan (2016), Harvard Dataverse
备注:
  ⚠️ 结构化事件数据，不含原始新闻文本
  ⚠️ Demand/response 为多标签 (0/1 binary columns)，非单标签多分类
  ✅ License 好 (CC0)，完全公开
```

#### 3. SPEED (Social Political Economic Event Database)
```
数据集名称: SPEED
类别数 K: 4 Tier-1 categories
类别列表: [Political Expression Events, Politically Motivated Attacks, 
  Disruptive State Acts, Political Power Reconfigurations]
样本量: 覆盖 3 国 (1979-2008)，具体数量待确认
License: 公开
下载方式: https://databank.illinois.edu/datasets/IDB-7407320
Gold-standard human labels: 是 (Cline Center 编码员)
引用论文: Cline Center for Advanced Social Research, UIUC
备注: ⚠️ 同样是结构化事件数据，非 NLP 文本分类格式
```

---

### 不满足条件的排除项

| 数据集 | 排除原因 |
|--------|---------|
| ACLED / CASE 2021 Task 2 | ToS 禁止 ML 用途（训练数据来自 ACLED） |
| GLOCON Gold | 需邮件申请 |
| CEHA | 样本量仅 500 |
| CCC | 494 多标签 tags，无原始文本 |
| CASE Task 1 | K=2 二分类 |
| MPEDS | 工具/系统，非固定数据集 |

---

### 核心问题

**protest/political event 领域没有理想的公开 NLP 文本分类数据集。** 上述候选全部是结构化编码数据（tabular），不含可直接用于文本分类的原始新闻文本。要做 NLP 实验需要自行匹配/爬取新闻，这引入额外复杂度和版权问题。

---

### 建议

如果坚持 protest 领域确实困难，建议考虑换到有成熟公开 NLP 数据集的任务类型：

| 替代方向 | 数据集 | K | 样本量 | 特点 |
|---------|--------|---|--------|------|
| **危机事件分类** | HumAID | 11 | ~77K tweets | CC-BY-NC, HuggingFace 直接下载，gold labels |
| **情感分类** | GoEmotions | 27/28 | 58K | Reddit 文本，多标签，Google 标注 |
| **意图分类** | CLINC150 / BANKING77 | 150/77 | 23K/13K | 对话意图，完全公开 |
| **新闻主题** | AG News | 4 | 120K | 经典 benchmark |

其中 **HumAID** 最接近 protest 领域（crisis/disaster events），K=11，标注质量好，且项目本身研究标注错误归因，crisis event 分类的标注难度和噪声模式与 protest 类似。

是否要：(1) 用 PolDem action_form 做实验（接受 license 风险 + 无原始文本限制），(2) 转向 HumAID 等 crisis 数据集，还是 (3) 申请 GLOCON？

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_research_protest-dataset-search_20260520T092905"
}
```

</details>

---
