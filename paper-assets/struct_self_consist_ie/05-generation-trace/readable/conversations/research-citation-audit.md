# research citation audit

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 143
- **Recorded user turns:** 0
- **Tool calls:** 71
- **Original source:** `logs/chats/worker_research_citation_audit_20260517T085237.jsonl`
- **Structured JSON:** [`70cfd5ca5463e322f99e.json`](../../sessions/70/70cfd5ca5463e322f99e.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

143 recorded events

### Tool call

_source line 1 · 2026-05-17T08:58:22.618481+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__ssh_read_only,WebSearch",
  "max_results": "2"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_citation_audit_20260517T085237",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__ssh_read_only,WebSearch",
    "max_results": "2"
  }
}
```

</details>

---

### Tool result

_source line 2 · 2026-05-17T08:58:22.618816+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_citation_audit_20260517T085237",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-17T08:58:22.618990+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "autodl-5090",
  "command": "find /root/autodl-tmp/struct_self_consist_ie -name \"*.bib\" -not -path \"./.*\"",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_citation_audit_20260517T085237",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "autodl-5090",
    "command": "find /root/autodl-tmp/struct_self_consist_ie -name \"*.bib\" -not -path \"./.*\"",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 4 · 2026-05-17T08:58:22.619150+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.85}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_citation_audit_20260517T085237",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-17T08:58:22.619328+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/*.bib"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_citation_audit_20260517T085237",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/*.bib"
  }
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-17T08:58:22.619457+00:00_

artifacts/dream_reports/dream_20260515T092545/worst/custom.bib
docs/paper/references.bib

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_citation_audit_20260517T085237",
  "tool": "Glob",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-17T08:58:22.619577+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "autodl-5090",
  "command": "find /root/autodl-tmp -name \"*.bib\" -maxdepth 5",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_citation_audit_20260517T085237",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "autodl-5090",
    "command": "find /root/autodl-tmp -name \"*.bib\" -maxdepth 5",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-17T08:58:22.619703+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.36}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_citation_audit_20260517T085237",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-17T08:58:22.619831+00:00_

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
  "session": "worker_research_citation_audit_20260517T085237",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/references.bib"
  }
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-17T08:58:22.620090+00:00_

1	% Auto-generated from literature_map.yaml — do not edit manually
2	
3	@article{brown2024monkeys,
4	  title = {Large Language Monkeys: Scaling Inference Compute with Repeated Sampling},
5	  author = {Brown, Bradley and Juravsky, Jordan and Ehrlich, Ryan and Clark, Ronald and Le, Quoc V. and Ré, Christopher and Mirhoseini, Azalia},
6	  journal = {arXiv preprint arXiv:2407.21787},
7	  year = {2024},
8	  url = {https://arxiv.org/abs/2407.21787}
9	}
10	
11	@inproceedings{chen2024usc,
12	  title = {Universal Self-Consistency for Large Language Model Generation},
13	  author = {Chen, Xinyun and Aksitov, Renat and Alon, Uri and Ren, Jie and Xiao, Kefan and Yin, Pengcheng and Prakash, Sushant and Sutton, Charles and Wang, Xuezhi and Zhou, Denny},
14	  booktitle = {arXiv preprint (ICML 2024 Workshop ICL)},
15	  year = {2024},
16	  url = {https://arxiv.org/abs/2311.17311}
17	}
18	
19	@article{cobbe2021verifiers,
20	  title = {Training Verifiers to Solve Math Word Problems},
21	  author = {Cobbe, Karl and Kosaraju, Vineet and Bavarian, Mohammad and Chen, Mark and Jun, Heewoo and Kaiser, Lukasz and Plappert, Matthias and Tworek, Jerry and Hilton, Jacob and Nakano, Reiichiro and Hesse, Christopher and Schulman, John},
22	  journal = {arXiv preprint arXiv:2110.14168},
23	  year = {2021},
24	  url = {https://arxiv.org/abs/2110.14168}
25	}
26	
27	@inproceedings{culotta2004confidence,
28	  title = {Confidence Estimation for Information Extraction},
29	  author = {Culotta, Aron and McCallum, Andrew},
30	  booktitle = {HLT-NAACL 2004},
31	  year = {2004},
32	  url = {https://aclanthology.org/N04-4028/}
33	}
34	
35	@inproceedings{derczynski2017wnut,
36	  title = {Results of the WNUT2017 Shared Task on Novel and Emerging Entity Recognition},
37	  author = {Derczynski, Leon and Nichols, Eric and Erp, Marieke van and Limsopatham, Nut},
38	  booktitle = {W-NUT Workshop at EMNLP 2017},
39	  year = {2017},
40	  url = {https://aclanthology.org/W17-4418/}
41	}
42	
43	@inproceedings{ding2021fe
…[truncated 22515 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_citation_audit_20260517T085237",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-17T08:58:22.620357+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Oh Jungsuk Lee Jay-Yoon \"Latent Self-Consistency\" arXiv 2508.18395"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_citation_audit_20260517T085237",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Oh Jungsuk Lee Jay-Yoon \"Latent Self-Consistency\" arXiv 2508.18395"
  }
}
```

</details>

---

### Tool call

_source line 12 · 2026-05-17T08:58:22.620498+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Bhattacharyya Khanna \"Beyond Confidence Rethinking Self-Assessments\" arXiv 2605.07806"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_citation_audit_20260517T085237",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Bhattacharyya Khanna \"Beyond Confidence Rethinking Self-Assessments\" arXiv 2605.07806"
  }
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-17T08:58:22.620624+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Yao Xinzhi Nédellec \"Consistency accuracy correlation hard-prompted LLMs entity relation extraction plant-health\" Genomics Informatics 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_citation_audit_20260517T085237",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Yao Xinzhi Nédellec \"Consistency accuracy correlation hard-prompted LLMs entity relation extraction plant-health\" Genomics Informatics 2026"
  }
}
```

</details>

---

### Tool call

_source line 14 · 2026-05-17T08:58:22.620744+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Kim Junseok Yang Nakyeong \"Reliability-Aware Adaptive Self-Consistency\" arXiv 2601.02970"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_citation_audit_20260517T085237",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Kim Junseok Yang Nakyeong \"Reliability-Aware Adaptive Self-Consistency\" arXiv 2601.02970"
  }
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-17T08:58:22.620861+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Feng Austin Alonso Marius Odonnat \"Optimal Self-Consistency Efficient Reasoning\" arXiv 2511.12309"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_citation_audit_20260517T085237",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Feng Austin Alonso Marius Odonnat \"Optimal Self-Consistency Efficient Reasoning\" arXiv 2511.12309"
  }
}
```

</details>

---

### Tool call

_source line 16 · 2026-05-17T08:58:22.620975+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Venktesh Rathee Anand \"Trust but Verify Survey Verification Test-time Scaling\" arXiv 2508.16665"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_citation_audit_20260517T085237",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Venktesh Rathee Anand \"Trust but Verify Survey Verification Test-time Scaling\" arXiv 2508.16665"
  }
}
```

</details>

---

### Tool result

_source line 17 · 2026-05-17T08:58:22.621227+00:00_

Web search results for query: "Oh Jungsuk Lee Jay-Yoon "Latent Self-Consistency" arXiv 2508.18395"

Links: [{"title":"[2508.18395] Latent Self-Consistency for Reliable Majority-Set Selection in Short- and Long-Answer Reasoning","url":"https://arxiv.org/abs/2508.18395"},{"title":"Latent Self-Consistency for Reliable Majority‑Set Selection in Short‑ and Long‑Answer Reasoning","url":"https://arxiv.org/html/2508.18395"},{"title":"Latent Self-Consistency for Reliable Majority-Set Selection in Short- and","url":"https://arxiv.org/pdf/2508.18395"},{"title":"Latent Self-Consistency for Reliable Majority-Set Selection in Short- and Long-Answer Reasoning","url":"https://arxiv.org/html/2508.18395v1"},{"title":"(PDF) Latent Self-Consistency for Reliable Majority-Set Selection in Short- and Long-Answer Reasoning","url":"https://www.researchgate.net/publication/394978774_Latent_Self-Consistency_for_Reliable_Majority-Set_Selection_in_Short-_and_Long-Answer_Reasoning"},{"title":"Latent Self-Consistency for Reliable Majority-Set Selection in Short- and Long-Answer Reasoning | Proceedings of the AAAI Conference on Artificial Intelligence","url":"https://ojs.aaai.org/index.php/AAAI/article/view/40536"},{"title":"Internal Consistency and Self-Feedback in Large Language Models: A Survey","url":"https://arxiv.org/html/2407.14507v3"},{"title":"HYU NLP Lab. - Publications","url":"https://nlp.hanyang.ac.kr/home/publications"},{"title":"How Effective Is Self-Consistency for Long-Context Problems?","url":"https://arxiv.org/html/2411.01101v1"},{"title":"Dynamics-Aligned Latent Imagination in Contextual World Models for Zero-Shot Generalization","url":"https://arxiv.org/html/2508.20294v2"}]

I found the paper you were searching for. Here's what the search returned:

"Latent Self-Consistency for Reliable Majority-Set Selection in Short- and Long-Answer Reasoning" is a paper by Jungsuk Oh and Jay-Yoon Lee (arXiv:2508.18395).

The paper addresses the problem that probabilistic decoding in Large La
…[truncated 824 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_citation_audit_20260517T085237",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-17T08:58:22.621442+00:00_

Web search results for query: "Bhattacharyya Khanna "Beyond Confidence Rethinking Self-Assessments" arXiv 2605.07806"

Links: [{"title":"[2605.07806] Beyond Confidence: Rethinking Self-Assessments for Performance Prediction in LLMs","url":"https://arxiv.org/abs/2605.07806"},{"title":"The Confidence Trap: Gender Bias and Predictive Certainty in LLMs","url":"https://arxiv.org/pdf/2601.07806"},{"title":"Tuesday 22nd July 2008 - 2008 - International Journal of Psychology - Wiley Online Library","url":"https://onlinelibrary.wiley.com/doi/10.1080/00207594.2008.10108484"},{"title":"[2303.02970] Rethinking Confidence Calibration for Failure Prediction","url":"https://arxiv.org/abs/2303.02970"},{"title":"Audio for 2605.05242v1","url":"https://arxiv.org/audio/2605.05242"},{"title":"[2605.11284] Rethinking external validation for the target population: Capturing patient-level similarity with a generative model","url":"https://arxiv.org/abs/2605.11284"},{"title":"Bhattacharyya - an overview | ScienceDirect Topics","url":"https://www.sciencedirect.com/topics/computer-science/bhattacharyya"},{"title":"Rethinking Confidence Calibration for Failure Prediction | Request PDF","url":"https://www.researchgate.net/publication/364417107_Rethinking_Confidence_Calibration_for_Failure_Prediction"},{"title":"[quant-ph/0611182] Bhattacharyya inequality for quantum state estimation","url":"https://arxiv.org/abs/quant-ph/0611182"},{"title":"[2605.05242] Beyond Semantic Similarity: Rethinking Retrieval for Agentic Search via Direct Corpus Interaction","url":"https://arxiv.org/abs/2605.05242"}]

Based on the search results, I found the paper you're looking for:

"Beyond Confidence: Rethinking Self-Assessments for Performance Prediction in LLMs" (arXiv 2605.07806) is authored by Sree Bhattacharyya, Samarth Khanna, Leona Chen, Lucas Craig, Tharun Dilliraj, and James Z. Wang.

The paper focuses on Large Language Models (LLMs) used in settings where reliable self-assessment is critical. The authors n
…[truncated 557 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_citation_audit_20260517T085237",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 19 · 2026-05-17T08:58:22.621627+00:00_

Web search results for query: "Yao Xinzhi Nédellec "Consistency accuracy correlation hard-prompted LLMs entity relation extraction plant-health" Genomics Informatics 2026"

Links: [{"title":"Consistency–accuracy correlation in hard-prompted LLMs for entity and relation extraction: empirical findings from plant-health data - PMC","url":"https://pmc.ncbi.nlm.nih.gov/articles/PMC12888769/"},{"title":"Bioregulatory event extraction using large language models: a case study of rice literature - PMC","url":"https://pmc.ncbi.nlm.nih.gov/articles/PMC11529424/"},{"title":"Benchmarking LLM-based Information Extraction Tools for ...","url":"https://www.medrxiv.org/content/10.64898/2026.01.19.26344287v1.full.pdf"},{"title":"Benchmarking LLM-based Information Extraction Tools for Medical Documents | medRxiv","url":"https://www.medrxiv.org/content/10.64898/2026.01.19.26344287v1.full"},{"title":"Using large language models for temporal relation extraction ...","url":"https://pmc.ncbi.nlm.nih.gov/articles/PMC12640238/"},{"title":"Extracting Oncology Insights with John Snow Labs’ Medical Language Models - John Snow Labs","url":"https://www.johnsnowlabs.com/extracting-oncology-insights-with-john-snow-labs-medical-language-models/"},{"title":"Scientific Large Language Models: A Survey on Biological & Chemical Domains | ACM Computing Surveys","url":"https://dl.acm.org/doi/10.1145/3715318"},{"title":"Bioregulatory event extraction using large language models: a case study of rice literature - R Discovery","url":"https://discovery.researcher.life/article/bioregulatory-event-extraction-using-large-language-models-a-case-study-of-rice-literature/76e6ed506a663546b0282302a25fed0a"},{"title":"Toward an Understanding of the Self-Coherence and the Cross-Coherence of LLMs An Empirical Investigation | Springer Nature Link","url":"https://link.springer.com/chapter/10.1007/978-3-032-06757-9_12"},{"title":"Leveraging large language models for the deidentification and temporal normalization of sensit
…[truncated 1046 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_citation_audit_20260517T085237",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-17T08:58:22.621788+00:00_

Web search results for query: "Feng Austin Alonso Marius Odonnat "Optimal Self-Consistency Efficient Reasoning" arXiv 2511.12309"

No links found.

The search returned no results. This could mean that the paper with the exact arXiv ID 2511.12309 and those specific author names may not be indexed by web search, or the paper details might be slightly different. 

If you're looking for information about this paper, you might try:
1. Visiting arXiv directly at https://arxiv.org/abs/2511.12309
2. Searching for just the arXiv ID (2511.12309) alone
3. Searching for the paper title without the author names

Would you like me to try a different search query?


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_citation_audit_20260517T085237",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 21 · 2026-05-17T08:58:22.621938+00:00_

Web search results for query: "Kim Junseok Yang Nakyeong "Reliability-Aware Adaptive Self-Consistency" arXiv 2601.02970"

Links: [{"title":"[2601.02970] Reliability-Aware Adaptive Self-Consistency for Efficient Sampling in LLM Reasoning","url":"https://arxiv.org/abs/2601.02970"},{"title":"Reliability-Aware Adaptive Self-Consistency for Efficient Sampling in LLM","url":"https://arxiv.org/pdf/2601.02970"},{"title":"Reliability-Aware Adaptive Self-Consistency for Efficient Sampling in LLM Reasoning","url":"https://arxiv.org/html/2601.02970"}]

I found the paper you're looking for! Here's what I found:

The paper "Reliability-Aware Adaptive Self-Consistency for Efficient Sampling in LLM Reasoning" (arXiv:2601.02970) was submitted on January 6, 2026, with authors Junseok Kim, Nakyeong Yang, Kyungmin Min, and Kyomin Jung.

The paper proposes Reliability-Aware Adaptive Self-Consistency (ReASC), which reframes adaptive sampling from response counting to evidence sufficiency, leveraging response-level confidence for principled information aggregation. ReASC operates in two stages: a single-sample decision stage that resolves instances confidently answerable from a single response, and a reliability-aware accumulation stage that aggregates responses by jointly leveraging their frequency and confidence.

Across five models and four datasets, ReASC consistently achieves the best accuracy-cost trade-off compared to existing baselines.

The paper is available on arXiv at https://arxiv.org/abs/2601.02970


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_citation_audit_20260517T085237",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 22 · 2026-05-17T08:58:22.622085+00:00_

Web search results for query: "Venktesh Rathee Anand "Trust but Verify Survey Verification Test-time Scaling" arXiv 2508.16665"

No links found.

The search didn't return any results for that specific query. This could be because:

1. The arXiv paper identifier (2508.16665) may not exist or may be incorrectly formatted
2. The paper may not yet be indexed by search engines
3. The exact quote or author names may be slightly different than provided

If you're looking for information about this paper, you could try:
- Visiting arXiv.org directly and searching for the paper ID: 2508.16665
- Searching with just the author names or a shorter version of the title
- Checking if the date format is correct (arXiv IDs follow a YYMM.##### format, so 2508 would be August 2025)

Would you like me to search with different parameters or help you find this paper in another way?


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_citation_audit_20260517T085237",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool call

_source line 23 · 2026-05-17T08:58:22.622285+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "arXiv 2511.12309 \"Optimal Self-Consistency\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_citation_audit_20260517T085237",
  "tool": "WebSearch",
  "tool_args": {
    "query": "arXiv 2511.12309 \"Optimal Self-Consistency\""
  }
}
```

</details>

---

### Tool call

_source line 24 · 2026-05-17T08:58:22.622415+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "arXiv 2508.16665 \"Trust but Verify\" verification test-time scaling survey"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_citation_audit_20260517T085237",
  "tool": "WebSearch",
  "tool_args": {
    "query": "arXiv 2508.16665 \"Trust but Verify\" verification test-time scaling survey"
  }
}
```

</details>

---

### Tool call

_source line 25 · 2026-05-17T08:58:22.622533+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Hobelsberger Winner Nawroth \"Systematic Evaluation Uncertainty Estimation Methods\" arXiv 2510.20460"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_citation_audit_20260517T085237",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Hobelsberger Winner Nawroth \"Systematic Evaluation Uncertainty Estimation Methods\" arXiv 2510.20460"
  }
}
```

</details>

---

### Tool call

_source line 26 · 2026-05-17T08:58:22.622647+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Wang Weiqin Wang Yile Huang Hui \"Ranked Voting Self-Consistency\" arXiv 2505.10772"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_citation_audit_20260517T085237",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Wang Weiqin Wang Yile Huang Hui \"Ranked Voting Self-Consistency\" arXiv 2505.10772"
  }
}
```

</details>

---

### Tool call

_source line 27 · 2026-05-17T08:58:22.622761+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Eikema Rutkiewicz Giulianelli \"Structure-Conditional Minimum Bayes Risk Decoding\" arXiv 2510.20700"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_citation_audit_20260517T085237",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Eikema Rutkiewicz Giulianelli \"Structure-Conditional Minimum Bayes Risk Decoding\" arXiv 2510.20700"
  }
}
```

</details>

---

### Tool call

_source line 28 · 2026-05-17T08:58:22.622873+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Vashurin Goloburda \"Uncertainty Quantification LLMs Minimum Bayes Risk\" arXiv 2502.04964"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_citation_audit_20260517T085237",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Vashurin Goloburda \"Uncertainty Quantification LLMs Minimum Bayes Risk\" arXiv 2502.04964"
  }
}
```

</details>

---

### Tool result

_source line 29 · 2026-05-17T08:58:22.623009+00:00_

Web search results for query: "arXiv 2511.12309 "Optimal Self-Consistency""

Links: [{"title":"[2511.12309] Optimal Self-Consistency for Efficient Reasoning with Large Language Models","url":"https://arxiv.org/abs/2511.12309"},{"title":"Optimal Self-Consistency for Efficient Reasoning with Large Language Models","url":"https://arxiv.org/pdf/2511.12309"},{"title":"(PDF) Optimal Self-Consistency for Efficient Reasoning with Large Language Models","url":"https://www.researchgate.net/publication/397700719_Optimal_Self-Consistency_for_Efficient_Reasoning_with_Large_Language_Models"},{"title":"Optimal Self-Consistency for Efficient Reasoning with ...","url":"https://www.aimodels.fyi/papers/arxiv/optimal-self-consistency-efficient-reasoning-large-language"},{"title":"Papers citing 'Optimal Self-Consistency for Efficient Reasoning with Large Language Models'","url":"https://www.researchtrend.ai/papers/2511.12309/cited-by"},{"title":"Self-Consistency Improves Chain of Thought Reasoning in Language Models | OpenReview","url":"https://openreview.net/forum?id=1PL1NIMMrw"},{"title":"Confidence Improves Self-Consistency in LLMs | by Ema Ilic | Medium","url":"https://medium.com/@ema.ilic9/confidence-improves-self-consistency-in-llms-313e80467168"},{"title":"[2203.11171] Self-Consistency Improves Chain of Thought Reasoning in Language Models","url":"https://ar5iv.labs.arxiv.org/html/2203.11171?fallback=original"},{"title":"Confidence Improves Self-Consistency in LLMs","url":"https://arxiv.org/pdf/2502.06233"},{"title":"Self-Consistency Decoding Strategy","url":"https://www.emergentmind.com/topics/self-consistency-decoding-strategy"}]

Based on the search results, here's what I found about arXiv paper 2511.12309:

## Paper Overview

The paper is titled "Optimal Self-Consistency for Efficient Reasoning with Large Language Models" by Austin Feng and 2 other authors.

## Main Content

Self-consistency (SC) is a widely used test-time inference technique for improving performance in chai
…[truncated 948 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_citation_audit_20260517T085237",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 30 · 2026-05-17T08:58:22.623203+00:00_

Web search results for query: "arXiv 2508.16665 "Trust but Verify" verification test-time scaling survey"

Links: [{"title":"[2508.16665] Trust but Verify! A Survey on Verification Design for Test-time Scaling","url":"https://arxiv.org/abs/2508.16665"},{"title":"Trust but Verify! A Survey on Verification Design for Test-time Scaling","url":"https://arxiv.org/html/2508.16665v1"},{"title":"Trust but Verify! A Survey on Verification Design for Test-time Scaling","url":"https://openreview.net/pdf?id=sytEeAZYvf"},{"title":"SETS: Leveraging Self-Verification and Self-Correction for Improved Test-Time Scaling","url":"https://arxiv.org/html/2501.19306v3"},{"title":"Rethinking Optimal Verification Granularity for Compute-Efficient Test-Time Scaling","url":"https://arxiv.org/html/2505.11730v2"},{"title":"[2505.11730] Rethinking Optimal Verification Granularity for Compute-Efficient Test-Time Scaling","url":"https://arxiv.org/abs/2505.11730"},{"title":"Trust but Verify: Programmatic VLM Evaluation in the Wild","url":"https://arxiv.org/html/2410.13121"},{"title":"Trust, But Verify: A Self-Verification Approach to Reinforcement Learning with Verifiable Rewards","url":"https://arxiv.org/html/2505.13445"},{"title":"Revision History for SETS: Leveraging Self-Verification...","url":"https://openreview.net/revisions?id=5Ih5CDlmgQ"},{"title":"[PDF] SETS: Leveraging Self-Verification and Self-Correction for Improved Test-Time Scaling | Semantic Scholar","url":"https://www.semanticscholar.org/paper/af2e6ab6612f985b3a801da73e37df1578dc2eec"}]

I found the paper! Here's what I located:

The paper is titled "Trust but Verify! A Survey on Verification Design for Test-time Scaling" with the arXiv identifier 2508.16665.

**Paper Details:**
- Authors: V Venktesh, Mandeep Rathee, Avishek Anand
- Submitted on August 20, 2025 (v1), last revised September 9, 2025 (v3)

**Content Summary:**
The paper surveys test-time scaling (TTS), which has emerged as a new frontier for scaling the performance of
…[truncated 574 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_citation_audit_20260517T085237",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 31 · 2026-05-17T08:58:22.623383+00:00_

Web search results for query: "Hobelsberger Winner Nawroth "Systematic Evaluation Uncertainty Estimation Methods" arXiv 2510.20460"

Links: [{"title":"[2510.20460] Systematic Evaluation of Uncertainty Estimation Methods in Large Language Models","url":"https://arxiv.org/abs/2510.20460"},{"title":"Systematic Evaluation of Uncertainty Estimation Methods in Large Language Models","url":"https://arxiv.org/html/2510.20460"},{"title":"(PDF) Systematic Evaluation of Uncertainty Estimation Methods in Large Language Models","url":"https://www.researchgate.net/publication/396847893_Systematic_Evaluation_of_Uncertainty_Estimation_Methods_in_Large_Language_Models"},{"title":"Methodology Oct 2025","url":"https://arxiv.org/list/stat.ME/2025-10?skip=400&show=25"},{"title":"[2510.19586] Uncertainty evaluation of segmentation models for Earth observation","url":"https://arxiv.org/abs/2510.19586"},{"title":"Efficient Uncertainty Estimation for LLM-based Entity Linking in Tabular Data","url":"https://arxiv.org/html/2510.01251v1"},{"title":"[2510.01251] Efficient Uncertainty Estimation for LLM-based Entity Linking in Tabular Data","url":"https://arxiv.org/abs/2510.01251"},{"title":"[2510.02279] Addressing Pitfalls in the Evaluation of Uncertainty Estimation Methods for Natural Language Generation","url":"https://arxiv.org/abs/2510.02279"},{"title":"A Survey on Uncertainty Quantification Methods for Deep Learning","url":"https://arxiv.org/html/2302.13425v5"},{"title":"A survey of uncertainty in deep neural networks | Artificial Intelligence Review | Springer Nature Link","url":"https://link.springer.com/article/10.1007/s10462-023-10562-9"}]

I found the paper you're looking for! Here are the search results:

The paper "Systematic Evaluation of Uncertainty Estimation Methods in Large Language Models" was authored by Christian Hobelsberger, Theresa Winner, Andreas Nawroth, Oliver Mitevski, and Anna-Carolina Haensch.

The paper addresses how large language models produce outputs with varyi
…[truncated 662 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_citation_audit_20260517T085237",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 32 · 2026-05-17T08:58:22.623540+00:00_

Web search results for query: "Vashurin Goloburda "Uncertainty Quantification LLMs Minimum Bayes Risk" arXiv 2502.04964"

No links found.

The search did not return any results for that specific query. This could be because:

1. The arXiv paper identifier (2502.04964) may be very recent or not yet widely indexed
2. The exact title or author names might be slightly different from what was searched
3. The paper may not have been published yet or the identifier may be incorrect

You might try:
- Visiting arXiv directly at https://arxiv.org/abs/2502.04964 to access the paper
- Searching for just the authors' names: "Vashurin Goloburda"
- Searching for the main topic: "Uncertainty Quantification LLMs Minimum Bayes Risk"
- Checking if the paper ID format is correct (arXiv papers from February 2025 would have IDs starting with 2502)

Would you like me to try a different search approach?


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_citation_audit_20260517T085237",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 33 · 2026-05-17T08:58:22.623692+00:00_

Web search results for query: "Wang Weiqin Wang Yile Huang Hui "Ranked Voting Self-Consistency" arXiv 2505.10772"

No links found.

The search didn't return specific results for that exact paper. Let me try a more targeted search:

Links: [{"title":"[2505.10772] Ranked Voting based Self-Consistency of Large Language Models","url":"https://arxiv.org/abs/2505.10772"},{"title":"Ranked Voting based Self-Consistency of Large Language ...","url":"https://arxiv.org/pdf/2505.10772"},{"title":"Ranked Voting based Self-Consistency of Large Language Models","url":"https://arxiv.org/html/2505.10772v1"},{"title":"GitHub - szu-tera/RankedVotingSC: RankedVotingSC (Ranked Voting based Self-Consistency) is a method that generates ranked answers in each reasoning attempt and aggregates them using ranked voting across multiple responses, aiming to select the most reliable final answer and enhance the reasoning performance of large language models.","url":"https://github.com/szu-tera/RankedVotingSC"},{"title":"Ranked Voting based Self-Consistency of Large Language ...","url":"https://ylwangy.github.io/pub/ACL_2025_RVSC.pdf"},{"title":"Ranked Voting based Self-Consistency of Large Language ...","url":"https://aclanthology.org/2025.findings-acl.744.pdf"},{"title":"Ranked Voting based Self-Consistency of Large Language Models - ACL Anthology","url":"https://aclanthology.org/2025.findings-acl.744/"},{"title":"Weiqin Wang","url":"https://www.catalyzex.com/author/Weiqin%20Wang"},{"title":"Ranked Voting based Self-Consistency of Large Language Models","url":"https://www.researchgate.net/publication/394270401_Ranked_Voting_based_Self-Consistency_of_Large_Language_Models"},{"title":"Aclanthology","url":"https://aclanthology.org/2025.findings-acl.744.bib"}]

I found the paper! Here are the details about it:

**Title:** Ranked Voting based Self-Consistency of Large Language Models

**Authors:** Weiqin Wang, Yile Wang, and Hui Huang

**ArXiv ID:** 2505.10772

**Submission Date:** May 16, 2025

**S
…[truncated 1296 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_citation_audit_20260517T085237",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 34 · 2026-05-17T08:58:22.623862+00:00_

Web search results for query: "Eikema Rutkiewicz Giulianelli "Structure-Conditional Minimum Bayes Risk Decoding" arXiv 2510.20700"

Links: [{"title":"[2510.20700] Structure-Conditional Minimum Bayes Risk Decoding","url":"https://arxiv.org/abs/2510.20700"},{"title":"Structure-Conditional Minimum Bayes Risk Decoding","url":"https://arxiv.org/html/2510.20700"},{"title":"Structure-Conditional Minimum Bayes Risk Decoding - ACL Anthology","url":"https://aclanthology.org/2025.emnlp-main.1616/"},{"title":"GitHub - Roxot/structure-conditional-mbr: Structure-conditional minimum Bayes risk decoding. · GitHub","url":"https://github.com/Roxot/structure-conditional-mbr"},{"title":"Structure-Conditional Minimum Bayes Risk Decoding","url":"https://aclanthology.org/2025.emnlp-main.1616.pdf"}]

I found the paper! Here's what I found:

"Structure-Conditional Minimum Bayes Risk Decoding" is authored by Bryan Eikema, Anna Rutkiewicz, and Mario Giulianelli. It was submitted to arXiv as paper 2510.20700 on October 23, 2025.

The paper addresses Minimum Bayes Risk (MBR) decoding as an alternative to traditional generation strategies. While MBR has proven effective in machine translation, where the variability of a language model's outcome space is naturally constrained, it may face challenges in more open-ended tasks such as dialogue or instruction-following.

The authors hypothesize that applying MBR with standard similarity-based utility functions may result in selecting responses that are broadly representative of the model's distribution, yet sub-optimal with respect to any particular grouping of generations that share an underlying latent structure. They introduce three lightweight adaptations to the utility function, designed to make MBR more sensitive to structural variability in the outcome space.

The paper was published in the Proceedings of the 2025 Conference on Empirical Methods in Natural Language Processing, pages 31706–31723, in Suzhou, China.


REMINDER: You MUST include t
…[truncated 72 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_citation_audit_20260517T085237",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool call

_source line 35 · 2026-05-17T08:58:22.624030+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Vashurin Roman \"Uncertainty Quantification LLMs\" \"Bridging Confidence and Consistency\" cocoa NeurIPS 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_citation_audit_20260517T085237",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Vashurin Roman \"Uncertainty Quantification LLMs\" \"Bridging Confidence and Consistency\" cocoa NeurIPS 2025"
  }
}
```

</details>

---

### Tool call

_source line 36 · 2026-05-17T08:58:22.624171+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Kang Zhewei Zhao Xuandong Song Dawn \"Scalable Best-of-N Selection Self-Certainty\" arXiv 2502.18581"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_citation_audit_20260517T085237",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Kang Zhewei Zhao Xuandong Song Dawn \"Scalable Best-of-N Selection Self-Certainty\" arXiv 2502.18581"
  }
}
```

</details>

---

### Tool call

_source line 37 · 2026-05-17T08:58:22.624297+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Li Zichong Feng Xinyu \"LLMs Can Generate Better Answer Aggregating Own Responses\" arXiv 2503.04104"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_citation_audit_20260517T085237",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Li Zichong Feng Xinyu \"LLMs Can Generate Better Answer Aggregating Own Responses\" arXiv 2503.04104"
  }
}
```

</details>

---

### Tool call

_source line 38 · 2026-05-17T08:58:22.624420+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Taubenfeld Sheffer Ofek \"Confidence Improves Self-Consistency LLMs\" ACL 2025 Findings"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_citation_audit_20260517T085237",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Taubenfeld Sheffer Ofek \"Confidence Improves Self-Consistency LLMs\" ACL 2025 Findings"
  }
}
```

</details>

---

### Tool call

_source line 39 · 2026-05-17T08:58:22.624534+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Wang Xinglin \"Make Every Penny Count Difficulty-Adaptive Self-Consistency\" NAACL 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_citation_audit_20260517T085237",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Wang Xinglin \"Make Every Penny Count Difficulty-Adaptive Self-Consistency\" NAACL 2025"
  }
}
```

</details>

---

### Tool call

_source line 40 · 2026-05-17T08:58:22.624645+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Xia Zhiqiu Xu Jinxuan \"Survey Uncertainty Estimation Methods Large Language Models\" ACL Findings 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_citation_audit_20260517T085237",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Xia Zhiqiu Xu Jinxuan \"Survey Uncertainty Estimation Methods Large Language Models\" ACL Findings 2025"
  }
}
```

</details>

---

### Tool result

_source line 41 · 2026-05-17T08:58:22.624788+00:00_

Web search results for query: "Kang Zhewei Zhao Xuandong Song Dawn "Scalable Best-of-N Selection Self-Certainty" arXiv 2502.18581"

Links: [{"title":"[2502.18581] Scalable Best-of-N Selection for Large Language Models via Self-Certainty","url":"https://arxiv.org/abs/2502.18581"},{"title":"Scalable Best-of-N Selection for Large Language Models via Self-Certainty","url":"https://arxiv.org/pdf/2502.18581"},{"title":"GitHub - backprop07/Self-Certainty: Implementation of self-certainty as an extention of ZeroEval Project · GitHub","url":"https://github.com/backprop07/Self-Certainty"},{"title":"Scalable Best-of-N Selection for Large Language Models via Self-Certainty","url":"https://www.researchgate.net/publication/389392014_Scalable_Best-of-N_Selection_for_Large_Language_Models_via_Self-Certainty?_tp=eyJjb250ZXh0Ijp7InBhZ2UiOiJzY2llbnRpZmljQ29udHJpYnV0aW9ucyIsInByZXZpb3VzUGFnZSI6bnVsbH19"},{"title":"dblp: Scalable Best-of-N Selection for Large Language Models via Self-Certainty.","url":"https://dblp.org/rec/journals/corr/abs-2502-18581.html"},{"title":"Scalable Best-of-N Selection for Large Language Models via Self-Certainty | alphaXiv","url":"https://www.alphaxiv.org/overview/2502.18581v2"},{"title":"NeurIPS Poster Scalable Best-of-N Selection for Large Language Models via Self-Certainty","url":"https://neurips.cc/virtual/2025/poster/120166"},{"title":"Scalable Best-of-N Selection for Large Language Models via Self-Certainty | AI Research Paper Details","url":"https://www.aimodels.fyi/papers/arxiv/scalable-best-n-selection-large-language-models"},{"title":"Deep Think with Confidence DEEP THINK WITH CONFIDENCE","url":"https://jiaweizzhao.github.io/deepconf/static/pdfs/deepconf_arxiv.pdf"},{"title":"[Literature Review] Scalable Best-of-N Selection for Large Language Models via Self-Certainty","url":"https://www.themoonlight.io/en/review/scalable-best-of-n-selection-for-large-language-models-via-self-certainty"}]

I found the paper you're looking for! Here's what I found:

…[truncated 1108 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_citation_audit_20260517T085237",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 42 · 2026-05-17T08:58:22.624954+00:00_

Web search results for query: "Vashurin Roman "Uncertainty Quantification LLMs" "Bridging Confidence and Consistency" cocoa NeurIPS 2025"

Links: [{"title":"[2502.04964v3] Uncertainty Quantification for LLMs through Minimum Bayes Risk: Bridging Confidence and Consistency","url":"https://arxiv.org/abs/2502.04964v3"},{"title":"[2502.04964] Uncertainty Quantification for LLMs through Minimum Bayes Risk: Bridging Confidence and Consistency","url":"https://arxiv.org/abs/2502.04964"},{"title":"NeurIPS Poster CoCoA: A Minimum Bayes Risk Framework Bridging Confidence and Consistency for Uncertainty Quantification in LLMs","url":"https://neurips.cc/virtual/2025/loc/san-diego/poster/118918"},{"title":"Uncertainty Quantification for LLMs through Minimum Bayes Risk: Bridging Confidence and Consistency","url":"https://arxiv.org/html/2502.04964v3"},{"title":"NeurIPS Poster Uncertainty Quantification for LLMs through Minimum Bayes Risk: Bridging Confidence and Consistency","url":"https://neurips.cc/virtual/2025/poster/118918"},{"title":"Benchmarking Uncertainty Quantification Methods for Large Language Models with LM-Polygraph | Transactions of the Association for Computational Linguistics | MIT Press","url":"https://direct.mit.edu/tacl/article/doi/10.1162/tacl_a_00737/128713/Benchmarking-Uncertainty-Quantification-Methods"},{"title":"Uncertainty Quantification and Confidence Calibration in Large Language Models: A Survey | Proceedings of the 31st ACM SIGKDD Conference on Knowledge Discovery and Data Mining V.2","url":"https://dl.acm.org/doi/10.1145/3711896.3736569"},{"title":"CoCoA: A Minimum Bayes Risk Framework Bridging Confidence and Consistency for Uncertainty Quantification in LLMs | OpenReview","url":"https://openreview.net/forum?id=H1NGlLNaVC"},{"title":"[2406.15627] Benchmarking Uncertainty Quantification Methods for Large Language Models with LM-Polygraph","url":"https://arxiv.org/abs/2406.15627"},{"title":"Benchmarking Uncertainty Quantification Methods for Large Langua
…[truncated 1422 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_citation_audit_20260517T085237",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 43 · 2026-05-17T08:58:22.625175+00:00_

Web search results for query: "Wang Xinglin "Make Every Penny Count Difficulty-Adaptive Self-Consistency" NAACL 2025"

No links found.

The search returned no results for that specific query. This could mean:

1. The paper may not yet be publicly indexed online
2. The exact title or author name might be slightly different
3. The paper details (venue, year) might be different from what was searched
4. The paper might not be published yet or not widely distributed

Would you like me to try a modified search? For example, I could search for:
- Just the author name and conference: "Wang Xinglin NAACL 2025"
- Just the paper title with different wording
- The topic area (e.g., "difficulty-adaptive self-consistency")

Let me know which approach would be most helpful!


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_citation_audit_20260517T085237",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 44 · 2026-05-17T08:58:22.625349+00:00_

Web search results for query: "Li Zichong Feng Xinyu "LLMs Can Generate Better Answer Aggregating Own Responses" arXiv 2503.04104"

Links: [{"title":"[2503.04104] LLMs Can Generate a Better Answer by Aggregating Their Own Responses","url":"https://arxiv.org/abs/2503.04104"},{"title":"LLMs Can Generate a Better Answer by Aggregating Their Own Responses","url":"https://arxiv.org/html/2503.04104"},{"title":"(PDF) LLMs Can Generate a Better Answer by Aggregating Their Own Responses","url":"https://www.researchgate.net/publication/389648493_LLMs_Can_Generate_a_Better_Answer_by_Aggregating_Their_Own_Responses"},{"title":"LLMs Can Generate a Better Answer by Aggregating Their Own Responses","url":"https://www.arxiv.org/pdf/2503.04104v1"},{"title":"Computation and Language Mar 2025","url":"https://arxiv.org/list/cs.CL/2025-03?skip=200&show=2000"},{"title":"A Survey of Large Language Models","url":"https://arxiv.org/html/2303.18223v16"},{"title":"GitHub - mtuann/llm-updated-papers: Papers related to Large Language Models in all top venues · GitHub","url":"https://github.com/mtuann/llm-updated-papers"},{"title":"Let LLMs Take on the Latest Challenges ! A Chinese Dynamic Question Answering Benchmark","url":"https://arxiv.org/html/2402.19248v2"},{"title":"A Survey on Large Language Model based Autonomous Agents","url":"https://arxiv.org/html/2308.11432v6"},{"title":"Search-R1: Training LLMs to Reason and Leverage ...","url":"https://arxiv.org/pdf/2503.09516"}]

I found the paper you're looking for! Here are the key details:

**Title:** LLMs Can Generate a Better Answer by Aggregating Their Own Responses

**Authors:** Zichong Li, Xinyu Feng, and others

**arXiv ID:** 2503.04104

**Main Contribution:** The authors propose Generative Self-Aggregation (GSA), a novel prompting method that improves answer quality without requiring the model's discriminative capabilities. GSA first samples multiple diverse responses from the LLM, then aggregates them to obtain an improved solution.

*
…[truncated 680 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_citation_audit_20260517T085237",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 45 · 2026-05-17T08:58:22.625532+00:00_

Web search results for query: "Taubenfeld Sheffer Ofek "Confidence Improves Self-Consistency LLMs" ACL 2025 Findings"

Links: [{"title":"Confidence Improves Self-Consistency in LLMs - ACL Anthology","url":"https://aclanthology.org/2025.findings-acl.1030/"},{"title":"[2502.06233] Confidence Improves Self-Consistency in LLMs","url":"https://arxiv.org/abs/2502.06233"},{"title":"GitHub - taubenfeld/CISC: Official implementation for the Confidence Improves Self-Consistency in LLMs paper (ACL 2025, Finding)","url":"https://github.com/taubenfeld/CISC"},{"title":"[PDF] Confidence Improves Self-Consistency in LLMs | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Confidence-Improves-Self-Consistency-in-LLMs-Taubenfeld-Sheffer/36b203d5fee14d34853021cb4bdcfa0d8e988986"},{"title":"Confidence Improves Self-Consistency in LLMs | Request PDF","url":"https://www.researchgate.net/publication/394271906_Confidence_Improves_Self-Consistency_in_LLMs"},{"title":"Confidence Improves Self-Consistency in LLMs","url":"https://aclanthology.org/2025.findings-acl.1030.pdf"},{"title":"Confidence Improves Self-Consistency in LLMs","url":"https://research.google/pubs/confidence-improves-self-consistency-in-llms/"},{"title":"Confidence Improves Self-Consistency in LLMs - The Hebrew University of Jerusalem","url":"https://cris.huji.ac.il/en/publications/confidence-improves-self-consistency-in-llms/"},{"title":"Confidence Improves Self-Consistency in LLMs","url":"https://arxiv.org/html/2502.06233v1"},{"title":"Confidence Improves Self-Consistency in LLMs - Consensus","url":"https://www.consensus.app/papers/details/425ec6bdbe0d5ca581bf388c30078b75/"}]

I found the paper you're looking for! Here's what I found:

## Publication Details

"Confidence Improves Self-Consistency in LLMs" was published by Amir Taubenfeld, Tom Sheffer, Eran Ofek, Amir Feder, Ariel Goldstein, Zorik Gekhman, and Gal Yona in the Findings of the Association for Computational Linguistics: ACL 2025, pages 20090–20111,
…[truncated 1068 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_citation_audit_20260517T085237",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 46 · 2026-05-17T08:58:22.625706+00:00_

Web search results for query: "Xia Zhiqiu Xu Jinxuan "Survey Uncertainty Estimation Methods Large Language Models" ACL Findings 2025"

Links: [{"title":"A Survey of Uncertainty Estimation Methods on Large Language Models - ACL Anthology","url":"https://aclanthology.org/2025.findings-acl.1101/"},{"title":"A Survey of Uncertainty Estimation Methods on Large ...","url":"https://aclanthology.org/2025.findings-acl.1101.pdf"},{"title":"A Survey of Uncertainty Estimation Methods on Large Language Models","url":"https://www.researchgate.net/publication/394272040_A_Survey_of_Uncertainty_Estimation_Methods_on_Large_Language_Models"},{"title":"A Survey of Uncertainty Estimation Methods on Large Language Models","url":"https://arxiv.org/html/2503.00172v2"},{"title":"[2503.00172] A Survey of Uncertainty Estimation Methods on Large Language Models","url":"https://arxiv.org/abs/2503.00172"},{"title":"[Quick Review] A Survey of Uncertainty Estimation Methods on Large Language Models","url":"https://liner.com/review/survey-uncertainty-estimation-methods-on-large-language-models"},{"title":"(PDF) A Survey of Uncertainty Estimation Methods on Large Language Models","url":"https://www.researchgate.net/publication/389548375_A_Survey_of_Uncertainty_Estimation_Methods_on_Large_Language_Models"},{"title":"[PDF] A Survey of Uncertainty Estimation in LLMs: Theory Meets Practice | Semantic Scholar","url":"https://www.semanticscholar.org/paper/A-Survey-of-Uncertainty-Estimation-in-LLMs:-Theory-Huang-Yang/2f96cd7e2437200c375cf9d5e953e40d643a51c7"},{"title":"Computation and Language Mar 2025","url":"https://www.arxiv.org/list/cs.CL/2025-03?skip=0&show=1000"},{"title":"Accepted Findings Papers - ACL 2025","url":"https://2025.aclweb.org/program/find_papers/"}]

I found the paper you're looking for! Here are the results:

"A Survey of Uncertainty Estimation Methods on Large Language Models" by Zhiqiu Xia, Jinxuan Xu, Yuqian Zhang, and Hang Liu was published in Findings of the Association for Comput
…[truncated 770 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_citation_audit_20260517T085237",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool call

_source line 47 · 2026-05-17T08:58:22.625873+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"Make Every Penny Count\" \"Difficulty-Adaptive Self-Consistency\" NAACL 2025 self-consistency reasoning"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_citation_audit_20260517T085237",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"Make Every Penny Count\" \"Difficulty-Adaptive Self-Consistency\" NAACL 2025 self-consistency reasoning"
  }
}
```

</details>

---

### Tool call

_source line 48 · 2026-05-17T08:58:22.625998+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Snell Lee Xu Kumar \"Scaling LLM Test-Time Compute Optimally\" arXiv 2408.03314 ICLR 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_citation_audit_20260517T085237",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Snell Lee Xu Kumar \"Scaling LLM Test-Time Compute Optimally\" arXiv 2408.03314 ICLR 2025"
  }
}
```

</details>

---

### Tool call

_source line 49 · 2026-05-17T08:58:22.626118+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Zhang Botong Li Shuo Bastani Osbert \"Conformal Structured Prediction\" arXiv 2410.06296 ICLR 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_citation_audit_20260517T085237",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Zhang Botong Li Shuo Bastani Osbert \"Conformal Structured Prediction\" arXiv 2410.06296 ICLR 2025"
  }
}
```

</details>

---

### Tool call

_source line 50 · 2026-05-17T08:58:22.626257+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Schall Maximilian de Melo Gerard \"Hidden Cost Structure Constrained Decoding\" RANLP 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_citation_audit_20260517T085237",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Schall Maximilian de Melo Gerard \"Hidden Cost Structure Constrained Decoding\" RANLP 2025"
  }
}
```

</details>

---

### Tool call

_source line 51 · 2026-05-17T08:58:22.626372+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Yun Longfei An Chenyang \"Price of Format Diversity Collapse LLMs\" EMNLP Findings 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_citation_audit_20260517T085237",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Yun Longfei An Chenyang \"Price of Format Diversity Collapse LLMs\" EMNLP Findings 2025"
  }
}
```

</details>

---

### Tool result

_source line 52 · 2026-05-17T08:58:22.626518+00:00_

Web search results for query: "Snell Lee Xu Kumar "Scaling LLM Test-Time Compute Optimally" arXiv 2408.03314 ICLR 2025"

Links: [{"title":"[2408.03314] Scaling LLM Test-Time Compute Optimally can be More Effective than Scaling Model Parameters","url":"https://arxiv.org/abs/2408.03314"},{"title":"Scaling LLM Test-Time Compute Optimally can be More Effective than Scaling Model Parameters","url":"https://arxiv.org/html/2408.03314v1"},{"title":"Scaling LLM Test-Time Compute Optimally Can be More Effective than Scaling Parameters for Reasoning | OpenReview","url":"https://openreview.net/forum?id=4FWAwZtd2n"},{"title":"Paper page - Scaling LLM Test-Time Compute Optimally can be More Effective than Scaling Model Parameters","url":"https://huggingface.co/papers/2408.03314"},{"title":"Scaling LLM Test-Time Compute Optimally can be More Efective …","url":"https://arxiv.org/pdf/2408.03314"},{"title":"(PDF) Scaling LLM Test-Time Compute Optimally can be More Effective than Scaling Model Parameters","url":"https://www.researchgate.net/publication/382914793_Scaling_LLM_Test-Time_Compute_Optimally_can_be_More_Effective_than_Scaling_Model_Parameters"},{"title":"[2408.03314v1] Scaling LLM Test-Time Compute Optimally can be More Effective than Scaling Model Parameters","url":"https://arxiv.org/abs/2408.03314v1"},{"title":"Scaling LLM Test-Time Compute Optimally can be More Effective than Scaling Model Parameters | alphaXiv","url":"https://www.alphaxiv.org/abs/2408.03314"},{"title":"SCALING LLM TEST-TIME COMPUTE OPTIMALLY CAN ...","url":"https://proceedings.iclr.cc/paper_files/paper/2025/file/1b623663fd9b874366f3ce019fdfdd44-Paper-Conference.pdf"},{"title":"ICLR 2025 Scaling LLM Test-Time Compute Optimally Can be More Effective than Scaling Parameters for Reasoning Oral","url":"https://iclr.cc/virtual/2025/oral/31924"}]

I found the paper you're looking for! Here are the key details:

**Paper Title:** Scaling LLM Test-Time Compute Optimally can be More Effective than Scaling Model Par
…[truncated 1022 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_citation_audit_20260517T085237",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 53 · 2026-05-17T08:58:22.626667+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Thirukovalluru Huang Dhingra \"Atomic Self-Consistency Better Long Form Generations\" EMNLP 2024"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_citation_audit_20260517T085237",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Thirukovalluru Huang Dhingra \"Atomic Self-Consistency Better Long Form Generations\" EMNLP 2024"
  }
}
```

</details>

---

### Tool result

_source line 54 · 2026-05-17T08:58:22.626808+00:00_

Web search results for query: "Zhang Botong Li Shuo Bastani Osbert "Conformal Structured Prediction" arXiv 2410.06296 ICLR 2025"

Links: [{"title":"[2410.06296] Conformal Structured Prediction","url":"https://arxiv.org/abs/2410.06296"},{"title":"Conformal Structured Prediction","url":"https://www.researchgate.net/publication/384769274_Conformal_Structured_Prediction"},{"title":"Conformal Structured Prediction - ADS","url":"https://ui.adsabs.harvard.edu/abs/2024arXiv241006296Z/abstract"},{"title":"Conformal Structured Prediction | OpenReview","url":"https://openreview.net/forum?id=f8onX1abP2"},{"title":"[Literature Review] Conformal Structured Prediction","url":"https://www.themoonlight.io/en/review/conformal-structured-prediction"},{"title":"Trustworthy Machine Learning Group","url":"https://trustml.github.io/publications"},{"title":"Search | arXiv e-print repository","url":"https://arxiv.org/search/cs?searchtype=author&query=Bastani,+O"},{"title":"Published as a conference paper at ICLR 2025 CONFORMAL STRUCTURED PREDICTION","url":"https://proceedings.iclr.cc/paper_files/paper/2025/file/1868a3c73d0d2a44c42458575fa8514c-Paper-Conference.pdf"},{"title":"TRAQ: Trustworthy Retrieval Augmented Question Answering via Conformal Prediction | Request PDF","url":"https://www.researchgate.net/publication/382630302_TRAQ_Trustworthy_Retrieval_Augmented_Question_Answering_via_Conformal_Prediction"},{"title":"ICLR Conformal Structured Prediction","url":"https://iclr.cc/virtual/2025/32866"}]

Based on the search results, I found information about the paper "Conformal Structured Prediction" by Zhang, Botong, Li, Shuo, and Bastani, Osbert:

The paper, arXiv:2410.06296, was submitted on October 8, 2024 and last revised on March 9, 2025. The paper was accepted to ICLR 2025.

**Overview:**

The paper proposes a general framework for conformal prediction in the structured prediction setting, that modifies existing conformal prediction algorithms to output structured prediction sets that 
…[truncated 882 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_citation_audit_20260517T085237",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 55 · 2026-05-17T08:58:22.626971+00:00_

Web search results for query: ""Make Every Penny Count" "Difficulty-Adaptive Self-Consistency" NAACL 2025 self-consistency reasoning"

Links: [{"title":"Make Every Penny Count: Difficulty-Adaptive Self-Consistency for Cost-Efficient Reasoning - ACL Anthology","url":"https://aclanthology.org/2025.findings-naacl.383/"},{"title":"[2408.13457] Make Every Penny Count: Difficulty-Adaptive Self-Consistency for Cost-Efficient Reasoning","url":"https://arxiv.org/abs/2408.13457"},{"title":"Difficulty-Adaptive Self-Consistency for Cost-Efficient ...","url":"https://aclanthology.org/2025.findings-naacl.383.pdf"},{"title":"Make Every Penny Count: Difficulty-Adaptive Self-Consistency for Cost-Efficient Reasoning","url":"https://arxiv.org/html/2408.13457v3"},{"title":"Reliability-Aware Adaptive Self-Consistency for Efficient Sampling in LLM Reasoning","url":"https://arxiv.org/html/2601.02970v1"},{"title":"[Literature Review] Make Every Penny Count: Difficulty-Adaptive Self-Consistency for Cost-Efficient Reasoning","url":"https://www.themoonlight.io/en/review/make-every-penny-count-difficulty-adaptive-self-consistency-for-cost-efficient-reasoning"},{"title":"Make Every Penny Count: Difficulty-Adaptive Self-Consistency for Cost-Efficient Reasoning | alphaXiv","url":"https://www.alphaxiv.org/abs/2408.13457"},{"title":"[PDF] Make Every Penny Count: Difficulty-Adaptive Self-Consistency for Cost-Efficient Reasoning | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Make-Every-Penny-Count:-Difficulty-Adaptive-for-Wang-Feng/19e00674c3b767f5388a7a9e080b2b97485099a4"},{"title":"Make Every Penny Count: Difficulty-Adaptive Self-Consistency for Cost-Efficient Reasoning | Request PDF","url":"https://www.researchgate.net/publication/392505057_Make_Every_Penny_Count_Difficulty-Adaptive_Self-Consistency_for_Cost-Efficient_Reasoning"},{"title":"Difficulty-Adaptive Self-Consistency for Cost-Efficient ...","url":"https://dblp.org/rec/journals/corr/abs-2408-13457"}]

Based on the search 
…[truncated 1761 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_citation_audit_20260517T085237",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 56 · 2026-05-17T08:58:22.627146+00:00_

Web search results for query: "Thirukovalluru Huang Dhingra "Atomic Self-Consistency Better Long Form Generations" EMNLP 2024"

No links found.

I performed the web search but the results didn't return any specific information about this paper. The search query with the exact paper title and author names didn't yield results in my search. 

This could mean:
1. The paper may not yet be indexed by search engines
2. The title or author names might have a slight variation
3. The paper information might not be widely available online yet

If you're looking for this paper, I'd recommend:
- Checking the EMNLP 2024 conference proceedings directly on the ACL Anthology (aclanthology.org)
- Searching on arXiv.org for recent papers by these authors
- Visiting the authors' institutional websites or research profiles

Would you like me to try a different search approach, such as searching for just the paper title, or searching for the authors separately?


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_citation_audit_20260517T085237",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 57 · 2026-05-17T08:58:22.627318+00:00_

Web search results for query: "Schall Maximilian de Melo Gerard "Hidden Cost Structure Constrained Decoding" RANLP 2025"

Links: [{"title":"The Hidden Cost of Structure: How Constrained Decoding Affects Language Model Performance - ACL Anthology","url":"https://aclanthology.org/2025.ranlp-1.124/"},{"title":"The Hidden Cost of Structure: How Constrained Decoding ...","url":"https://acl-bg.org/proceedings/2025/RANLP%202025/pdf/2025.ranlp-1.124.pdf"},{"title":"How Constrained Decoding Affects Language Model ...","url":"https://aclanthology.org/2025.ranlp-1.124.pdf"},{"title":"Accepted papers","url":"https://ranlp.org/ranlp2025/index.php/accepted-papers/"},{"title":"RANLP 2025 Programme","url":"https://ranlp.org/ranlp2025/wp-content/uploads/2025/10/Full_RANLP_2025_Programme.pdf"},{"title":"Proceedings of Recent Advances in Natural Language Processing,pages 807–821","url":"https://acl-bg.org/proceedings/2025/RANLP%202025/pdf/2025.ranlp-1.93.pdf"},{"title":"Accepted Findings Papers - ACL 2025","url":"https://2025.aclweb.org/program/find_papers/"},{"title":"(PDF) Towards neuro-symbolic constrained decoding for ...","url":"https://www.researchgate.net/publication/401703058_Towards_neuro-symbolic_constrained_decoding_for_reliable_code_generation_with_LLMs"},{"title":"Constrained Decoding with Speculative Lookaheads","url":"https://aclanthology.org/2025.naacl-long.239.pdf"},{"title":"Logically Constrained Decoding - ACL Anthology","url":"https://aclanthology.org/2025.mathnlp-main.11/"}]

I found the paper! Here's what the search returned:

The paper "The Hidden Cost of Structure: How Constrained Decoding Affects Language Model Performance" was authored by Maximilian Schall and Gerard de Melo and was published in the Proceedings of the 15th International Conference on Recent Advances in Natural Language Processing (RANLP 2025) in Varna, Bulgaria.

The paper investigates how large language models that excel at generating fluent text perform when real-world applications require 
…[truncated 675 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_citation_audit_20260517T085237",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 58 · 2026-05-17T08:58:22.627499+00:00_

Web search results for query: "Yun Longfei An Chenyang "Price of Format Diversity Collapse LLMs" EMNLP Findings 2025"

Links: [{"title":"The Price of Format: Diversity Collapse in LLMs - ACL Anthology","url":"https://aclanthology.org/2025.findings-emnlp.836/"},{"title":"The Price of Format: Diversity Collapse in LLMs | Request PDF","url":"https://www.researchgate.net/publication/397426577_The_Price_of_Format_Diversity_Collapse_in_LLMs"},{"title":"[2505.18949] The Price of Format: Diversity Collapse in LLMs","url":"https://arxiv.org/abs/2505.18949"},{"title":"The Price of Format: Diversity Collapse in LLMs | AI Research Paper Details","url":"https://www.aimodels.fyi/papers/arxiv/price-format-diversity-collapse-llms"},{"title":"The Price of Format: Diversity Collapse in LLMs","url":"https://arxiv.org/html/2505.18949v1"},{"title":"The Price of Format: Diversity Collapse in LLMs","url":"https://aclanthology.org/2025.findings-emnlp.836.pdf"},{"title":"Chenyang An - ACL Anthology","url":"https://aclanthology.org/people/chenyang-an/unverified/"},{"title":"Longfei Yun - ACL Anthology","url":"https://aclanthology.org/people/longfei-yun/"},{"title":"Longfei Yun","url":"https://scholar.google.com/citations?user=lOuw-MAAAAAJ&hl=en"},{"title":"Verbalized Sampling: How to Mitigate Mode Collapse and Unlock LLM Diversity","url":"https://arxiv.org/html/2510.01171v1"}]

I found the paper! Here are the search results for "The Price of Format: Diversity Collapse in LLMs" by Yun Longfei, An Chenyang, and colleagues:

## Publication Details

The paper "The Price of Format: Diversity Collapse in LLMs" was authored by Longfei Yun, Chenyang An, Zilong Wang, Letian Peng, and Jingbo Shang and appeared in Findings of the Association for Computational Linguistics: EMNLP 2025, pages 15454–15468, in Suzhou, China.

## Main Finding

Instruction-tuned large language models (LLMs) employ structured templates, such as role markers and special tokens, to enforce format consistency during inference. Ho
…[truncated 1107 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_citation_audit_20260517T085237",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool call

_source line 59 · 2026-05-17T08:58:22.627662+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"Atomic Self-Consistency\" Thirukovalluru EMNLP 2024 long form generations"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_citation_audit_20260517T085237",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"Atomic Self-Consistency\" Thirukovalluru EMNLP 2024 long form generations"
  }
}
```

</details>

---

### Tool call

_source line 60 · 2026-05-17T08:58:22.627789+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Sainz García-Ferrero \"GoLLIE Annotation Guidelines Zero-Shot Information Extraction\" ICLR 2024"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_citation_audit_20260517T085237",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Sainz García-Ferrero \"GoLLIE Annotation Guidelines Zero-Shot Information Extraction\" ICLR 2024"
  }
}
```

</details>

---

### Tool call

_source line 61 · 2026-05-17T08:58:22.627911+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Brown Juravsky Ehrlich \"Large Language Monkeys Scaling Inference Compute Repeated Sampling\" arXiv 2407.21787"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_citation_audit_20260517T085237",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Brown Juravsky Ehrlich \"Large Language Monkeys Scaling Inference Compute Repeated Sampling\" arXiv 2407.21787"
  }
}
```

</details>

---

### Tool call

_source line 62 · 2026-05-17T08:58:22.628033+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Chen Xinyun Aksitov \"Universal Self-Consistency Large Language Model Generation\" arXiv 2311.17311"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_citation_audit_20260517T085237",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Chen Xinyun Aksitov \"Universal Self-Consistency Large Language Model Generation\" arXiv 2311.17311"
  }
}
```

</details>

---

### Tool call

_source line 63 · 2026-05-17T08:58:22.628167+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Lightman Kosaraju Burda \"Let's Verify Step by Step\" ICLR 2024 arXiv 2305.20050"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_citation_audit_20260517T085237",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Lightman Kosaraju Burda \"Let's Verify Step by Step\" ICLR 2024 arXiv 2305.20050"
  }
}
```

</details>

---

### Tool result

_source line 64 · 2026-05-17T08:58:22.628315+00:00_

Web search results for query: "Sainz García-Ferrero "GoLLIE Annotation Guidelines Zero-Shot Information Extraction" ICLR 2024"

Links: [{"title":"[2310.03668] GoLLIE: Annotation Guidelines improve Zero-Shot Information-Extraction","url":"https://arxiv.org/abs/2310.03668"},{"title":"GOLLIE : ANNOTATION GUIDELINES IMPROVE ZERO- ...","url":"https://proceedings.iclr.cc/paper_files/paper/2024/file/cda04d7ea67ea1376bf8c6962d8541e0-Paper-Conference.pdf"},{"title":"GoLLIE: Annotation Guidelines improve Zero-Shot Information-Extraction | OpenReview","url":"https://openreview.net/forum?id=Y3wpuxd7u9"},{"title":"ICLR Poster GoLLIE: Annotation Guidelines improve Zero-Shot Information-Extraction","url":"https://iclr.cc/virtual/2024/poster/18435"},{"title":"GOLLIE: ANNOTATION GUIDELINES IMPROVE ZERO-SHOT INFORMATION-EXTRACTION | Documents - Universidad del País Vasco / Euskal Herriko Unibertsitatea","url":"https://ekoizpen-zientifikoa.ehu.eus/documentos/66cb8eeac7cd8e0cebf21fbb"},{"title":"GoLLIE : Annotation Guidelines improve Zero-Shot Information-Extraction","url":"https://arxiv.org/html/2310.03668v5"},{"title":"[PDF] GoLLIE: Annotation Guidelines improve Zero-Shot Information-Extraction | Semantic Scholar","url":"https://www.semanticscholar.org/paper/GoLLIE:-Annotation-Guidelines-improve-Zero-Shot-Sainz-Garc%C3%ADa-Ferrero/3f40edfcafc018b2cb54612a9aaa9d6b43a11a26"},{"title":"GOLLIE : ANNOTATION GUIDELINES IMPROVE ZERO- ...","url":"https://openreview.net/pdf?id=Y3wpuxd7u9"},{"title":"gollie : annotation guidelines improve zero-shot ...","url":"https://arxiv.org/pdf/2310.03668"},{"title":"GOLLIE : ANNOTATION GUIDELINES IMPROVE ZERO-SHOT ...","url":"https://openreview.net/notes/edits/attachment?id=x345y4wtJb&name=pdf"}]

I found the paper you're looking for. The paper "GoLLIE: Annotation Guidelines improve Zero-Shot Information-Extraction" was authored by Oscar Sainz and Iker García-Ferrero along with Rodrigo Agerri, Oier Lopez de Lacalle, German Rigau, and Eneko Agirre from the
…[truncated 710 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_citation_audit_20260517T085237",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 65 · 2026-05-17T08:58:22.628455+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Zhou Wenxuan Zhang Sheng \"UniversalNER Targeted Distillation Open Named Entity Recognition\" ICLR 2024"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_citation_audit_20260517T085237",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Zhou Wenxuan Zhang Sheng \"UniversalNER Targeted Distillation Open Named Entity Recognition\" ICLR 2024"
  }
}
```

</details>

---

### Tool result

_source line 66 · 2026-05-17T08:58:22.628605+00:00_

Web search results for query: ""Atomic Self-Consistency" Thirukovalluru EMNLP 2024 long form generations"

Links: [{"title":"Atomic Self-Consistency for Better Long Form Generations - ACL Anthology","url":"https://aclanthology.org/2024.emnlp-main.706/"},{"title":"Atomic Self-Consistency for Better Long Form Generations","url":"https://aclanthology.org/2024.emnlp-main.706.pdf"},{"title":"Yukun Huang - Homepage","url":"https://kkkevinkkkkk.github.io/"},{"title":"Papers - DukeNLP","url":"https://nlplab.cs.duke.edu/papers/"},{"title":"Raghuveer Thirukovalluru | Duke University","url":"https://raghavlite.github.io/"},{"title":"Proceedings of the 2024 Conference on Empirical Methods in Natural Language Processing - ACL Anthology","url":"https://aclanthology.org/volumes/2024.emnlp-main/"},{"title":"The 2024 Conference on Empirical Methods in Natural Language Processing - ACL Anthology","url":"https://aclanthology.org/events/emnlp-2024/"},{"title":"Atomic Consistency Preference Optimization for Long-Form ...","url":"https://www.semanticscholar.org/paper/Atomic-Consistency-Preference-Optimization-for-Chen-Thirukovalluru/2fcc2a4fa9ac9ca02d626f52d69795299fb6a5bf"},{"title":"EMNLP 2024 (@emnlpmeeting) / X","url":"https://twitter.com/emnlpmeeting?lang=en"},{"title":"Findings - EMNLP 2024","url":"https://2024.emnlp.org/program/accepted_findings/"}]

Based on the search results, here's what I found about "Atomic Self-Consistency" from EMNLP 2024:

## Overview

"Atomic Self-Consistency for Better Long Form Generations" was published in the Proceedings of the 2024 Conference on Empirical Methods in Natural Language Processing, pages 12681–12694, Miami, Florida, USA.

## Authors

The paper was authored by Raghuveer Thirukovalluru, Yukun Huang, and Bhuwan Dhingra.

## Research Problem and Approach

Recent work has aimed to improve LLM generations by filtering out hallucinations to improve precision, but correctness of a long-form response also depends on the recall of multiple pieces 
…[truncated 925 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_citation_audit_20260517T085237",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 67 · 2026-05-17T08:58:22.628774+00:00_

Web search results for query: "Chen Xinyun Aksitov "Universal Self-Consistency Large Language Model Generation" arXiv 2311.17311"

Links: [{"title":"[2311.17311] Universal Self-Consistency for Large Language Model Generation","url":"https://arxiv.org/abs/2311.17311"},{"title":"Paper page - Universal Self-Consistency for Large Language Model Generation","url":"https://huggingface.co/papers/2311.17311"},{"title":"[PDF] Universal Self-Consistency for Large Language Model Generation | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Universal-Self-Consistency-for-Large-Language-Model-Chen-Aksitov/5f66d1a667eec13b5d337c3fc5619bcef95092bd"},{"title":"Universal Self-Consistency for Large Language Model Generation - ADS","url":"https://ui.adsabs.harvard.edu/abs/2023arXiv231117311C/abstract"},{"title":"dblp: Universal Self-Consistency for Large Language Model Generation.","url":"https://dblp.org/rec/journals/corr/abs-2311-17311.html"},{"title":"Universal Self-Consistency for Large Language Model Generation | alphaXiv","url":"https://www.alphaxiv.org/abs/2311.17311"},{"title":"universal self-consistency for large lan","url":"https://arxiv.org/pdf/2311.17311"},{"title":"Atomic Self-Consistency for Better Long Form Generations","url":"https://southnlp.github.io/southnlp2024/papers/southnlp2024-oral-07.pdf"},{"title":"Xinyun Chen on X: \"New preprint: Universal Self-Consistency for Large Language Model Generation https://t.co/SfdYQmUVYw We propose Universal Self-Consistency (USC) to aggregate free-form responses, such as code generation and summarization, where the original SC is not applicable. https://t.co/egvetQHGqp\" / X","url":"https://x.com/xinyun_chen_/status/1730308706620076480"},{"title":"Soft Self-Consistency Improves Language Model Agents","url":"https://arxiv.org/html/2402.13212v2"}]

I found the paper you're looking for! Here are the key details:

**Paper Title:** Universal Self-Consistency for Large Language Model Generation

**Authors:** Xinyun Chen,
…[truncated 1019 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_citation_audit_20260517T085237",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 68 · 2026-05-17T08:58:22.628948+00:00_

Web search results for query: "Brown Juravsky Ehrlich "Large Language Monkeys Scaling Inference Compute Repeated Sampling" arXiv 2407.21787"

No links found.

I wasn't able to find results for that specific query. Let me try a more targeted search using the arXiv identifier:

Links: [{"title":"[2407.21787] Large Language Monkeys: Scaling Inference Compute with Repeated Sampling","url":"https://arxiv.org/abs/2407.21787"},{"title":"Large Language Monkeys: Scaling Inference Compute with Repeated Sampling","url":"https://arxiv.org/pdf/2407.21787"},{"title":"(PDF) Large Language Monkeys: Scaling Inference Compute with Repeated Sampling","url":"https://www.researchgate.net/publication/382739350_Large_Language_Monkeys_Scaling_Inference_Compute_with_Repeated_Sampling"},{"title":"Large Language MonkeysTitle inspired by https://en.m.wikipedia.org/wiki/Infinite_monkey_theorem.: Scaling Inference Compute with Repeated Sampling","url":"https://arxiv.org/html/2407.21787"},{"title":"Quantum Physics Jul 2025","url":"https://arxiv.org/list/quant-ph/2025-07?skip=900"},{"title":"[2504.21787] Estimation of discrete distributions in relative entropy, and the deviations of the missing mass","url":"https://arxiv.org/abs/2504.21787"},{"title":"[2604.21787] Agentic AI-Enabled Framework for Thermal Comfort and Building Energy Assessment in Tropical Urban Neighborhoods","url":"https://arxiv.org/abs/2604.21787"},{"title":"Statistics Apr 2025","url":"https://www.arxiv.org/list/stat/2025-04?skip=550&show=250"},{"title":"Dynamical Implicit Neural Representations","url":"https://arxiv.org/html/2511.21787"},{"title":"Machine Learning Jul 2024","url":"https://web3.arxiv.org/list/cs.LG/2024-07?skip=230&show=2000"}]

Perfect! I found the paper. Here's what I found about arXiv 2407.21787:

## "Large Language Monkeys: Scaling Inference Compute with Repeated Sampling"

The paper is authored by Bradley Brown, Jordan Juravsky, Ryan Ehrlich, Ronald Clark, Quoc V. Le, Christopher Ré, and Azalia Mirhoseini.


…[truncated 754 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_citation_audit_20260517T085237",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 69 · 2026-05-17T08:58:22.629157+00:00_

Web search results for query: "Zhou Wenxuan Zhang Sheng "UniversalNER Targeted Distillation Open Named Entity Recognition" ICLR 2024"

Links: [{"title":"[2308.03279] UniversalNER: Targeted Distillation from Large Language Models for Open Named Entity Recognition","url":"https://arxiv.org/abs/2308.03279"},{"title":"UniversalNER: Targeted Distillation from Large Language Models for Open Named Entity Recognition | OpenReview","url":"https://openreview.net/forum?id=r65xfUb76p"},{"title":"UniversalNER: Targeted Distillation from Large Language Models for Open Named Entity Recognition - Microsoft Research","url":"https://www.microsoft.com/en-us/research/publication/universalner-targeted-distillation-from-large-language-models-for-open-named-entity-recognition/"},{"title":"UniversalNER: Targeted Distillation from Large Language Models for Open Named Entity Recognition [Quick Review]","url":"https://liner.com/review/universalner-targeted-distillation-from-large-language-models-for-open-named"},{"title":"UniversalNER: Targeted Distillation from Large Language Models for Open Named Entity Recognition - ADS","url":"https://ui.adsabs.harvard.edu/abs/2023arXiv230803279Z/abstract"},{"title":"UniversalNER: targeted distillation from large language models for open named entity recognition","url":"https://arxiv.org/html/2308.03279v2"},{"title":"[PDF] UniversalNER: Targeted Distillation from Large Language Models for Open Named Entity Recognition | Semantic Scholar","url":"https://www.semanticscholar.org/paper/UniversalNER:-Targeted-Distillation-from-Large-for-Zhou-Zhang/76b99439d524ae1813c30edc4bcad487a30a1f8c"},{"title":"UniversalNER: TARGETED DISTILLATION FROM","url":"https://arxiv.org/pdf/2308.03279"},{"title":"[2308.03279v2] UniversalNER: Targeted Distillation from Large Language Models for Open Named Entity Recognition","url":"https://arxiv.org/abs/2308.03279v2"},{"title":"UniversalNER: Targeted Distillation from Large Language Models for Open Named Entity Recognition | Request
…[truncated 1637 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_citation_audit_20260517T085237",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 70 · 2026-05-17T08:58:22.629350+00:00_

Web search results for query: "Lightman Kosaraju Burda "Let's Verify Step by Step" ICLR 2024 arXiv 2305.20050"

Links: [{"title":"Published as a conference paper at ICLR 2024 LET’S VERIFY STEP BY STEP","url":"https://proceedings.iclr.cc/paper_files/paper/2024/file/aca97732e30bcf1303bc22ac3924fd16-Paper-Conference.pdf"},{"title":"dblp: Let's Verify Step by Step.","url":"https://dblp.org/rec/conf/iclr/LightmanKBEBLLS24.html"},{"title":"[PDF] Let's Verify Step by Step | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Let's-Verify-Step-by-Step-Lightman-Kosaraju/be8db99310602d66bba64bcf41a572c45816fbfc"},{"title":"Let's Verify Step by Step","url":"https://proceedings.iclr.cc/paper_files/paper/2024/hash/aca97732e30bcf1303bc22ac3924fd16-Abstract-Conference.html"},{"title":"[2305.20050] Let's Verify Step by Step","url":"https://arxiv.org/abs/2305.20050"},{"title":"Let's Verify Step by Step | OpenReview","url":"https://openreview.net/forum?id=v8L0pN6EOi"},{"title":"Let’s Verify Step by Step (must-read to build OpenAI o1) - Paper Without Code","url":"https://paperwithoutcode.com/lets-verify-step-by-step-must-read-to-build-openai-o1/"},{"title":"Let’s Verify Step by Step Hunter Lightman∗ Vineet Kosaraju∗ Yura Burda∗","url":"https://arxiv.org/pdf/2305.20050"},{"title":"Let's Verify Step by Step","url":"https://www.researchgate.net/publication/371175770_Let's_Verify_Step_by_Step"},{"title":"Let's Verify Step by Step","url":"https://www.connectedpapers.com/main/be8db99310602d66bba64bcf41a572c45816fbfc/Let's-Verify-Step-by-Step/graph"}]

I found the paper! Here are the results:

## "Let's Verify Step by Step"

The paper was authored by Hunter Lightman, Vineet Kosaraju, Yura Burda, Harri Edwards, Bowen Baker, Teddy Lee, Jan Leike, John Schulman, Ilya Sutskever, and Karl Cobbe.

**Publication Details:**
- Published at the International Conference on Learning Representations 2024 (ICLR 2024)
- arXiv identifier: 2305.20050

**Summary:**
The paper compares outcome superv
…[truncated 764 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_citation_audit_20260517T085237",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool call

_source line 71 · 2026-05-17T08:58:22.629525+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Geng Jiahui Cai Fengyu \"Survey Confidence Estimation Calibration Large Language Models\" NAACL 2024"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_citation_audit_20260517T085237",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Geng Jiahui Cai Fengyu \"Survey Confidence Estimation Calibration Large Language Models\" NAACL 2024"
  }
}
```

</details>

---

### Tool call

_source line 72 · 2026-05-17T08:58:22.629651+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Jinnai Yuu Morimura \"Model-Based Minimum Bayes Risk Decoding Text Generation\" ICML 2024 arXiv 2311.05263"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_citation_audit_20260517T085237",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Jinnai Yuu Morimura \"Model-Based Minimum Bayes Risk Decoding Text Generation\" ICML 2024 arXiv 2311.05263"
  }
}
```

</details>

---

### Tool call

_source line 73 · 2026-05-17T08:58:22.629770+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Deguchi Hiroyuki Kamigaito \"Centroid-Based Efficient Minimum Bayes Risk Decoding\" EMNLP 2024"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_citation_audit_20260517T085237",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Deguchi Hiroyuki Kamigaito \"Centroid-Based Efficient Minimum Bayes Risk Decoding\" EMNLP 2024"
  }
}
```

</details>

---

### Tool call

_source line 74 · 2026-05-17T08:58:22.629883+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Xie Jie Lu Kai \"Self-Evaluation Improves Selective Generation Large Language Models\" NeurIPS 2024"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_citation_audit_20260517T085237",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Xie Jie Lu Kai \"Self-Evaluation Improves Selective Generation Large Language Models\" NeurIPS 2024"
  }
}
```

</details>

---

### Tool call

_source line 75 · 2026-05-17T08:58:22.629995+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Park Kanghee Wang Jiayu \"Grammar-Aligned Decoding\" NeurIPS 2024"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_citation_audit_20260517T085237",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Park Kanghee Wang Jiayu \"Grammar-Aligned Decoding\" NeurIPS 2024"
  }
}
```

</details>

---

### Tool result

_source line 76 · 2026-05-17T08:58:22.630162+00:00_

Web search results for query: "Geng Jiahui Cai Fengyu "Survey Confidence Estimation Calibration Large Language Models" NAACL 2024"

Links: [{"title":"A Survey of Confidence Estimation and Calibration in Large Language Models - ACL Anthology","url":"https://aclanthology.org/2024.naacl-long.366/"},{"title":"A Survey of Confidence Estimation and Calibration in ...","url":"https://aclanthology.org/2024.naacl-long.366.pdf"},{"title":"A Survey of Confidence Estimation and Calibration in Large Language Models","url":"https://www.researchgate.net/publication/382633391_A_Survey_of_Confidence_Estimation_and_Calibration_in_Large_Language_Models"},{"title":"[PDF] A Survey of Confidence Estimation and Calibration in Large Language Models | Semantic Scholar","url":"https://www.semanticscholar.org/paper/A-Survey-of-Confidence-Estimation-and-Calibration-Geng-Cai/6aa6003c7d7b3d275ae981aa6200014968c32430"},{"title":"[2311.08298] A Survey of Confidence Estimation and Calibration in Large Language Models","url":"https://arxiv.org/abs/2311.08298"},{"title":"A Survey of Confidence Estimation and Calibration in Large Language Models","url":"https://arxiv.org/html/2311.08298v2"},{"title":"A Survey of Confidence Estimation and Calibration ...","url":"https://lingo.iitgn.ac.in/nlpexplorer/paper/2024.naacl-long.366"},{"title":"Accepted Papers - NAACL-HLT 2024","url":"https://2024.naacl.org/program/accepted_papers/"},{"title":"A Survey of Uncertainty Estimation Methods on Large ...","url":"https://aclanthology.org/2025.findings-acl.1101.pdf"},{"title":"[2311.08298v2] A Survey of Confidence Estimation and Calibration in Large Language Models","url":"https://arxiv.org/abs/2311.08298v2"}]

I found the paper! Here are the search results for the paper by Geng Jiahui and Cai Fengyu:

## Paper Details

**A Survey of Confidence Estimation and Calibration in Large Language Models** by Jiahui Geng, Fengyu Cai, Yuxia Wang, Heinz Koeppl, Preslav Nakov, and Iryna Gurevych was published in the Proceedings o
…[truncated 968 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_citation_audit_20260517T085237",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 77 · 2026-05-17T08:58:22.630315+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Zheng Yaowei Zhang Richong \"LlamaFactory Unified Efficient Fine-Tuning 100+ Language Models\" ACL 2024"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_citation_audit_20260517T085237",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Zheng Yaowei Zhang Richong \"LlamaFactory Unified Efficient Fine-Tuning 100+ Language Models\" ACL 2024"
  }
}
```

</details>

---

### Tool result

_source line 78 · 2026-05-17T08:58:22.630467+00:00_

Web search results for query: "Jinnai Yuu Morimura "Model-Based Minimum Bayes Risk Decoding Text Generation" ICML 2024 arXiv 2311.05263"

Links: [{"title":"Model-Based Minimum Bayes Risk Decoding for Text Generation","url":"https://proceedings.mlr.press/v235/jinnai24a.html"},{"title":"[2311.05263] Model-Based Minimum Bayes Risk Decoding for Text Generation","url":"https://arxiv.org/abs/2311.05263"},{"title":"GitHub - CyberAgentAILab/model-based-mbr: Code of \"Model-Based Minimum Bayes Risk Decoding for Text Generation\" 2024","url":"https://github.com/CyberAgentAILab/model-based-mbr"},{"title":"[ICML 2024] Model-Based Minimum Bayes-Risk Decoding for Text Generation - YouTube","url":"https://www.youtube.com/watch?v=w8_rLLPkE5A"},{"title":"ICML Poster Model-Based Minimum Bayes Risk Decoding for Text Generation","url":"https://icml.cc/virtual/2024/poster/33005"},{"title":"Generating Diverse and High-Quality Texts by Minimum Bayes Risk Decoding - ACL Anthology","url":"https://aclanthology.org/2024.findings-acl.503/"},{"title":"陣内 佑 (Yuu Jinnai) | Yuu David Jinnai","url":"https://jinnaiyuu.github.io/ja/"},{"title":"Model-Based Minimum Bayes Risk Decoding for Text Generation | AI Research Paper Details","url":"https://www.aimodels.fyi/papers/arxiv/model-based-minimum-bayes-risk-decoding-text"},{"title":"[2401.05054] Generating Diverse and High-Quality Texts by Minimum Bayes Risk Decoding","url":"https://arxiv.org/abs/2401.05054"},{"title":"[PDF] Model-Based Minimum Bayes Risk Decoding","url":"https://www.semanticscholar.org/paper/Model-Based-Minimum-Bayes-Risk-Decoding-Jinnai-Morimura/9d7a77218a3fc53d821e20a89ab6be750aca9154"}]

I found the paper you're looking for! Here's what I found:

"Model-Based Minimum Bayes Risk Decoding for Text Generation" by Jinnai, Yuu, Morimura, Tetsuro, Honda, Ukyo, Ariu, Kaito, and Abe, Kenshi was published in the Proceedings of the 41st International Conference on Machine Learning (ICML 2024), pages 22326-22347.

The paper was submitted on 
…[truncated 904 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_citation_audit_20260517T085237",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 79 · 2026-05-17T08:58:22.630644+00:00_

Web search results for query: "Xie Jie Lu Kai "Self-Evaluation Improves Selective Generation Large Language Models" NeurIPS 2024"

Links: [{"title":"NeurIPS Self-Evaluation Improves Selective Generation in Large Language Models","url":"https://neurips.cc/virtual/2023/76522"},{"title":"Self-Evaluation Improves Selective Generation in Large Language Models","url":"https://proceedings.mlr.press/v239/ren23a.html"},{"title":"Self-Evaluation Improves Selective Generation in Large Language Models","url":"https://arxiv.org/html/2312.09300v1"},{"title":"[2312.09300] Self-Evaluation Improves Selective Generation in Large Language Models","url":"https://arxiv.org/abs/2312.09300"},{"title":"Paper page - Self-Evaluation Improves Selective Generation in Large Language Models","url":"https://huggingface.co/papers/2312.09300"},{"title":"NYU NeurIPS 2024 Papers | ai @ NYU","url":"https://cims.nyu.edu/ai/nyu-neurips-2024-papers/?edit=&language=en"},{"title":"Adaptation with Self-Evaluation to Improve Selective Prediction in LLMs - ACL Anthology","url":"https://aclanthology.org/2023.findings-emnlp.345/"},{"title":"Evaluating Large Language Models","url":"https://neurips.cc/media/neurips-2024/Slides/99524.pdf"},{"title":"Selective Generation for Controllable Language Models Minjae Lee∗ GSAI POSTECH","url":"https://proceedings.neurips.cc/paper_files/paper/2024/file/5a6815122f533193a022cbc41786c1cc-Paper-Conference.pdf"},{"title":"LLM Evaluators Recognize and Favor Their Own Generations","url":"https://proceedings.neurips.cc/paper_files/paper/2024/hash/7f1f0218e45f5414c79c0679633e47bc-Abstract-Conference.html"}]

Based on the search results, I found information about a paper titled "Self-Evaluation Improves Selective Generation in Large Language Models," but there's an important note about the author names and publication venue:

The paper was authored by Jie Ren, Yao Zhao, Tu Vu, Peter J. Liu, and Balaji Lakshminarayanan, and published in the Proceedings on "I Can't Believe It's Not Bet
…[truncated 848 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_citation_audit_20260517T085237",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 80 · 2026-05-17T08:58:22.630815+00:00_

Web search results for query: "Park Kanghee Wang Jiayu "Grammar-Aligned Decoding" NeurIPS 2024"

Links: [{"title":"Grammar-Aligned Decoding Kanghee Park1∗ Jiayu Wang1∗ Taylor Berg-Kirkpatrick2","url":"https://proceedings.neurips.cc/paper_files/paper/2024/file/2bdc2267c3d7d01523e2e17ac0a754f3-Paper-Conference.pdf"},{"title":"Grammar-Aligned Decoding","url":"https://papers.nips.cc/paper_files/paper/2024/hash/2bdc2267c3d7d01523e2e17ac0a754f3-Abstract-Conference.html"},{"title":"Grammar-Aligned Decoding","url":"https://proceedings.neurips.cc/paper_files/paper/2024/hash/2bdc2267c3d7d01523e2e17ac0a754f3-Abstract-Conference.html"},{"title":"NeurIPS Poster Grammar-Aligned Decoding","url":"https://neurips.cc/virtual/2024/poster/96599"},{"title":"Grammar-Aligned Decoding","url":"https://arxiv.org/html/2405.21047v3"},{"title":"(PDF) Grammar-Aligned Decoding","url":"https://www.researchgate.net/publication/381108984_Grammar-Aligned_Decoding"},{"title":"[2405.21047] Grammar-Aligned Decoding","url":"https://arxiv.org/abs/2405.21047"},{"title":"NeurIPS Poster Grammar-Aligned Decoding","url":"https://nips.cc/virtual/2024/poster/96599"},{"title":"Grammar-aligned decoding | Proceedings of the 38th International Conference on Neural Information Processing Systems","url":"https://dl.acm.org/doi/10.5555/3737916.3738690"},{"title":"Grammar-Aligned Decoding | OpenReview","url":"https://openreview.net/forum?id=5G7ve8E1Lu"}]

I found comprehensive information about the "Grammar-Aligned Decoding" paper. Here are the key details:

## Paper Overview

The paper is authored by Kanghee Park and Jiayu Wang from University of Wisconsin-Madison, along with Taylor Berg-Kirkpatrick and Nadia Polikarpova from University of California San Diego, and Loris D'Antoni from University of Wisconsin-Madison.

## Publication Venue

The paper was presented as part of the Main Conference Track at NeurIPS 2024 (Advances in Neural Information Processing Systems 37).

## Research Focus

The paper addresses the probl
…[truncated 1039 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_citation_audit_20260517T085237",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 81 · 2026-05-17T08:58:22.630988+00:00_

Web search results for query: "Deguchi Hiroyuki Kamigaito "Centroid-Based Efficient Minimum Bayes Risk Decoding" EMNLP 2024"

Links: [{"title":"Centroid-Based Efficient Minimum Bayes Risk Decoding - ACL Anthology","url":"https://aclanthology.org/2024.findings-acl.654/"},{"title":"[2402.11197] Centroid-Based Efficient Minimum Bayes Risk Decoding","url":"https://arxiv.org/abs/2402.11197"},{"title":"Centroid-Based Efficient Minimum Bayes Risk Decoding | Request PDF","url":"https://www.researchgate.net/publication/384210977_Centroid-Based_Efficient_Minimum_Bayes_Risk_Decoding"},{"title":"Centroid-Based Efficient Minimum Bayes Risk Decoding - ADS","url":"https://ui.adsabs.harvard.edu/abs/2024arXiv240211197D/abstract"},{"title":"[Quick Review] Centroid-Based Efficient Minimum Bayes Risk Decoding","url":"https://liner.com/review/centroidbased-efficient-minimum-bayes-risk-decoding"},{"title":"出口 祥之 / Hiroyuki Deguchi","url":"https://sites.google.com/view/hdeguchi"},{"title":"Re-evaluating Minimum Bayes Risk Decoding for Automatic Speech Recognition","url":"https://arxiv.org/html/2510.19471v1"},{"title":"Diversity Explains Inference Scaling Laws: Through a Case Study of Minimum Bayes Risk Decoding","url":"https://arxiv.org/html/2410.15021v2"},{"title":"Centroid-Based Efficient Minimum Bayes Risk Decoding","url":"https://arxiv.org/pdf/2402.11197v1"},{"title":"Hiroyuki Deguchi - Home (Ja)","url":"https://sites.google.com/view/hdeguchi/home-ja"}]

I found the paper. Here are the search results:

The paper "Centroid-Based Efficient Minimum Bayes Risk Decoding" by Hiroyuki Deguchi, Yusuke Sakai, Hidetaka Kamigaito, Taro Watanabe, Hideki Tanaka, and Masao Utiyama was published in Findings of the Association for Computational Linguistics: ACL 2024, pages 11009–11018, Bangkok, Thailand.

Note: The paper was published at **ACL 2024**, not EMNLP 2024. The paper addresses Minimum Bayes Risk (MBR) decoding, which achieved state-of-the-art translation performance using COMET, a neural me
…[truncated 488 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_citation_audit_20260517T085237",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 82 · 2026-05-17T08:58:22.631179+00:00_

Web search results for query: "Zheng Yaowei Zhang Richong "LlamaFactory Unified Efficient Fine-Tuning 100+ Language Models" ACL 2024"

Links: [{"title":"LlamaFactory: Unified Efficient Fine-Tuning of 100+ Language Models - ACL Anthology","url":"https://aclanthology.org/2024.acl-demos.38/"},{"title":"[2403.13372] LlamaFactory: Unified Efficient Fine-Tuning of 100+ Language Models","url":"https://arxiv.org/abs/2403.13372"},{"title":"LlamaFactory: Unified Efficient Fine-Tuning of 100+ Language Models - ADS","url":"https://ui.adsabs.harvard.edu/abs/2024arXiv240313372Z/abstract"},{"title":"Unified Efficient Fine-Tuning of 100+ Language Models","url":"https://aclanthology.org/2024.acl-demos.38.pdf"},{"title":"GitHub - hiyouga/LlamaFactory: Unified Efficient Fine-Tuning of 100+ LLMs & VLMs (ACL 2024) · GitHub","url":"https://github.com/hiyouga/LlamaFactory"},{"title":"Accepted Demo Papers - ACL 2024","url":"https://2024.aclweb.org/program/demo_papers/"},{"title":"[PDF] LlamaFactory: Unified Efficient Fine-Tuning of 100+ Language Models | Semantic Scholar","url":"https://www.semanticscholar.org/paper/LlamaFactory:-Unified-Efficient-Fine-Tuning-of-100+-Zheng-Zhang/d5d7b26dbdf09737878644530b226a79c9f43bfb"},{"title":"Google Scholar","url":"https://scholar.google.com/scholar?q=Yaowei+Zheng%2C+Richong+Zhang%2C+Junhao+Zhang%2C+Yanhan+Ye%2C+Zheyan+Luo%2C+Zhangchi+Feng%2C+and+Yongqiang+Ma.+2024.+Llamafactory%3A+Unified+efficient+fine-tuning+of+100++language+models.+arXiv+preprint+arXiv%3A2403.13372+%282024%29."},{"title":"GitHub - hmilyzhang/llama-factory: Unified Efficient Fine-Tuning of 100+ LLMs & VLMs (ACL 2024) · GitHub","url":"https://github.com/hmilyzhang/llama-factory"},{"title":"GitHub - toininoi/llama-factory: Unified Efficient Fine-Tuning of 100+ LLMs & VLMs (ACL 2024)","url":"https://github.com/toininoi/llama-factory"}]

I found comprehensive information about this paper. Here are the search results:

## Paper Details

The paper "LlamaFactory: Unified Efficient Fine-Tu
…[truncated 956 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_citation_audit_20260517T085237",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 83 · 2026-05-17T08:58:22.631364+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "arXiv 2312.09300 \"Self-Evaluation\" selective generation authors"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_citation_audit_20260517T085237",
  "tool": "WebSearch",
  "tool_args": {
    "query": "arXiv 2312.09300 \"Self-Evaluation\" selective generation authors"
  }
}
```

</details>

---

### Tool call

_source line 84 · 2026-05-17T08:58:22.631491+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Kirk Mediratta Nalmpantis \"Understanding Effects RLHF LLM Generalisation Diversity\" ICLR 2024"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_citation_audit_20260517T085237",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Kirk Mediratta Nalmpantis \"Understanding Effects RLHF LLM Generalisation Diversity\" ICLR 2024"
  }
}
```

</details>

---

### Tool call

_source line 85 · 2026-05-17T08:58:22.631609+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Cobbe Kosaraju Bavarian \"Training Verifiers Solve Math Word Problems\" arXiv 2110.14168"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_citation_audit_20260517T085237",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Cobbe Kosaraju Bavarian \"Training Verifiers Solve Math Word Problems\" arXiv 2110.14168"
  }
}
```

</details>

---

### Tool call

_source line 86 · 2026-05-17T08:58:22.631722+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Wang Xuezhi Wei Jason \"Self-Consistency Improves Chain of Thought Reasoning\" ICLR 2023"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_citation_audit_20260517T085237",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Wang Xuezhi Wei Jason \"Self-Consistency Improves Chain of Thought Reasoning\" ICLR 2023"
  }
}
```

</details>

---

### Tool result

_source line 87 · 2026-05-17T08:58:22.631854+00:00_

Web search results for query: "arXiv 2312.09300 "Self-Evaluation" selective generation authors"

Links: [{"title":"[2312.09300] Self-Evaluation Improves Selective Generation in Large Language Models","url":"https://arxiv.org/abs/2312.09300"},{"title":"Self-Evaluation Improves Selective Generation in Large Language Models","url":"https://arxiv.org/html/2312.09300"},{"title":"Paper page - Self-Evaluation Improves Selective Generation in Large Language Models","url":"https://huggingface.co/papers/2312.09300"},{"title":"\\abrPANDA (Pedantic ANswer-correctness Determination and Adjudication):Improving Automatic Evaluation for Question Answering","url":"https://arxiv.org/html/2402.11161v1"},{"title":"Steering Large Language Models to Evaluate and Amplify Creativity","url":"https://arxiv.org/html/2412.06060v1"},{"title":"Self-Alignment for Factuality: Mitigating Hallucinations in LLMs via Self-Evaluation","url":"https://arxiv.org/html/2402.09267v2"},{"title":"[2310.11689] Adaptation with Self-Evaluation to Improve Selective Prediction in LLMs","url":"https://arxiv.org/abs/2310.11689"},{"title":"LLMs-as-Judges: A Comprehensive Survey on LLM-based Evaluation Methods","url":"https://arxiv.org/html/2412.05579v1"},{"title":"Machine Learning Sep 2024","url":"https://arxiv.org/list/cs.LG/2024-09?skip=1600&show=2000"},{"title":"Machine Learning Oct 2024","url":"https://arxiv.org/list/cs.LG/2024-10?skip=1050&show=1000"}]

Based on the search results, I found the information about arXiv paper 2312.09300:

The paper "Self-Evaluation Improves Selective Generation in Large Language Models" (arXiv:2312.09300) was submitted on December 14, 2023, and has the following authors: Jie Ren, Yao Zhao, Tu Vu, Peter J. Liu, and Balaji Lakshminarayanan.

The paper reformulates open-ended generation tasks into token-level prediction tasks and instructs an LLM to self-evaluate its answers, employing either a multi-way comparison or a point-wise evaluation approach, with the option to include a "None
…[truncated 160 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_citation_audit_20260517T085237",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 88 · 2026-05-17T08:58:22.631999+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Kuhn Lorenz Gal Yarin Farquhar \"Semantic Uncertainty Linguistic Invariances\" ICLR 2023 arXiv 2302.09664"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_citation_audit_20260517T085237",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Kuhn Lorenz Gal Yarin Farquhar \"Semantic Uncertainty Linguistic Invariances\" ICLR 2023 arXiv 2302.09664"
  }
}
```

</details>

---

### Tool call

_source line 89 · 2026-05-17T08:58:22.632161+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Willard Brandon Louf Rémi \"Efficient Guided Generation Large Language Models\" arXiv 2307.09702"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_citation_audit_20260517T085237",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Willard Brandon Louf Rémi \"Efficient Guided Generation Large Language Models\" arXiv 2307.09702"
  }
}
```

</details>

---

### Tool result

_source line 90 · 2026-05-17T08:58:22.632324+00:00_

Web search results for query: "Kirk Mediratta Nalmpantis "Understanding Effects RLHF LLM Generalisation Diversity" ICLR 2024"

Links: [{"title":"[2310.06452] Understanding the Effects of RLHF on LLM Generalisation and Diversity","url":"https://arxiv.org/abs/2310.06452"},{"title":"[PDF] Understanding the Effects of RLHF on LLM Generalisation and Diversity | Semantic Scholar","url":"https://www.semanticscholar.org/paper/cb3968152f7d93f53d24b00279a90d5071ddc85a"},{"title":"Understanding the Effects of RLHF on LLM Generalisation ...","url":"https://iclr.cc/media/iclr-2024/Slides/18704.pdf"},{"title":"Understanding the Effects of RLHF on LLM Generalisation ...","url":"https://arxiv.org/pdf/2310.06452"},{"title":"[2310.06452v1] Understanding the Effects of RLHF on LLM Generalisation and Diversity","url":"https://arxiv.org/abs/2310.06452v1"},{"title":"Understanding the Effects of RLHF on LLM Generalisation and Diversity","url":"https://arxiv.org/html/2310.06452v2"},{"title":"Understanding the Effects of RLHF on LLM Generalisation and Diversity | OpenReview","url":"https://openreview.net/forum?id=PXD3FAVHJT"},{"title":"[Quick Review] Understanding the Effects of RLHF on LLM Generalisation and Diversity","url":"https://liner.com/review/understanding-the-effects-of-rlhf-on-llm-generalisation-and-diversity"},{"title":"ICLR Poster Understanding the Effects of RLHF on LLM Generalisation and Diversity","url":"https://iclr.cc/virtual/2024/poster/18704"},{"title":"[2310.06452] Understanding the Effects of RLHF on LLM Generalisation and Diversity","url":"https://ar5iv.labs.arxiv.org/html/2310.06452"}]

I found the paper! Here's what I discovered:

The paper "Understanding the Effects of RLHF on LLM Generalisation and Diversity" has authors Robert Kirk, Ishita Mediratta, Christoforos Nalmpantis, Jelena Luketina, Eric Hambro, Edward Grefenstette, and Roberta Raileanu.

The paper presents an extensive analysis of how each stage of the RLHF process (supervised fine-tuning, reward modell
…[truncated 914 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_citation_audit_20260517T085237",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 91 · 2026-05-17T08:58:22.632494+00:00_

Web search results for query: "Cobbe Kosaraju Bavarian "Training Verifiers Solve Math Word Problems" arXiv 2110.14168"

Links: [{"title":"[2110.14168] Training Verifiers to Solve Math Word Problems","url":"https://arxiv.org/abs/2110.14168"},{"title":"[PDF] Training Verifiers to Solve Math Word Problems | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Training-Verifiers-to-Solve-Math-Word-Problems-Cobbe-Kosaraju/d6045d2ccc9c09ca1671348de86d07da6bc28eea"},{"title":"Paper page - Training Verifiers to Solve Math Word Problems","url":"https://huggingface.co/papers/2110.14168"},{"title":"[2110.14168v2] Training Verifiers to Solve Math Word Problems","url":"https://arxiv.org/abs/2110.14168v2"},{"title":"[2110.14168v1] Training Verifiers to Solve Math Word Problems","url":"https://arxiv.org/abs/2110.14168v1"},{"title":"Google Scholar","url":"https://scholar.google.com/scholar?q=Cobbe%2C+K.%2C+Kosaraju%2C+V.%2C+Bavarian%2C+M.%2C+Chen%2C+M.%2C+Jun%2C+H.%2C+Kaiser%2C+L.%2C+Plappert%2C+M.%2C+Tworek%2C+J.%2C+Hilton%2C+J.%2C+Nakano%2C+R.%2C+et+al.+Training+verifiers+to+solve+math+word+problems.+arXiv+preprint+arXiv%3A2110.14168+%282021%29."},{"title":"Training Verifiers to Solve Math Word Problems","url":"https://www.researchgate.net/publication/355698629_Training_Verifiers_to_Solve_Math_Word_Problems"},{"title":"Training Verifiers to Solve Math Word Problems, Karl Cobbe+, arXiv'21 · Issue #1618 · AkihikoWatanabe/paper_notes","url":"https://github.com/AkihikoWatanabe/paper_notes/issues/1618"},{"title":"arXiv:2110.14168v2 [cs.LG] 18 Nov 2021","url":"https://arxiv.org/pdf/2110.14168"},{"title":"Training Verifiers to Solve Math Word Pr...","url":"https://axi.lims.ac.uk/paper/2110.14168"}]

I found the paper you're looking for. Here are the key details:

**Title:** Training Verifiers to Solve Math Word Problems

**Authors:** Karl Cobbe, Vineet Kosaraju, Mohammad Bavarian, Mark Chen, Heewoo Jun, Lukasz Kaiser, Matthias Plappert, Jerry Tworek, Jacob Hilton, Reiichiro Na
…[truncated 795 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_citation_audit_20260517T085237",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 92 · 2026-05-17T08:58:22.632658+00:00_

Web search results for query: "Wang Xuezhi Wei Jason "Self-Consistency Improves Chain of Thought Reasoning" ICLR 2023"

Links: [{"title":"[2203.11171] Self-Consistency Improves Chain of Thought Reasoning in Language Models","url":"https://arxiv.org/abs/2203.11171"},{"title":"Self-Consistency Improves Chain of Thought Reasoning in Language Models","url":"https://iclr.cc/media/iclr-2023/Slides/11718.pdf"},{"title":"dblp: Self-Consistency Improves Chain of Thought Reasoning in Language Models.","url":"https://dblp.org/rec/conf/iclr/0002WSLCNCZ23.html"},{"title":"ICLR Poster Self-Consistency Improves Chain of Thought Reasoning in Language Models","url":"https://iclr.cc/virtual/2023/poster/11718"},{"title":"Self-Consistency Improves Chain of Thought Reasoning in Language Models","url":"https://www.cs.toronto.edu/~cmaddis/courses/csc2541_w25/presentations/self-consistency.pdf"},{"title":"[PDF] Self-Consistency Improves Chain of Thought Reasoning in Language Models | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Self-Consistency-Improves-Chain-of-Thought-in-Wang-Wei/5f19ae1135a9500940978104ec15a5b8751bc7d2"},{"title":"SELF-CONSISTENCY IMPROVES CHAIN OF THOUGHT ...","url":"http://webdocs.cs.ualberta.ca/~dale/papers/iclr23b.pdf"},{"title":"Self-Consistency Improves Chain of Thought Reasoning in Language Models | OpenReview","url":"https://openreview.net/forum?id=1PL1NIMMrw"},{"title":"Self-Consistency Improves Chain of Thought Reasoning in ...","url":"https://summarizepaper.com/en/arxiv-id/2203.11171v4/"},{"title":"Self-Consistency Improves Chain of Thought Reasoning in Language Models","url":"https://research.google/pubs/pub52081/"}]

Based on the search results, I found the paper you're looking for. Here are the details:

**Paper Title:** Self-Consistency Improves Chain of Thought Reasoning in Language Models

**Authors:** Xuezhi Wang, Jason Wei, Dale Schuurmans, Quoc Le, Ed Chi, Sharan Narang, Aakanksha Chowdhery, Denny Zhou

**Venue:** ICLR 2023

**Overv
…[truncated 868 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_citation_audit_20260517T085237",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 93 · 2026-05-17T08:58:22.632837+00:00_

Web search results for query: "Kuhn Lorenz Gal Yarin Farquhar "Semantic Uncertainty Linguistic Invariances" ICLR 2023 arXiv 2302.09664"

Links: [{"title":"[2302.09664] Semantic Uncertainty: Linguistic Invariances for Uncertainty Estimation in Natural Language Generation","url":"https://arxiv.org/abs/2302.09664"},{"title":"(PDF) Semantic Uncertainty: Linguistic Invariances for Uncertainty Estimation in Natural Language Generation","url":"https://www.researchgate.net/publication/368664708_Semantic_Uncertainty_Linguistic_Invariances_for_Uncertainty_Estimation_in_Natural_Language_Generation"},{"title":"Paper page - Semantic Uncertainty: Linguistic Invariances for Uncertainty Estimation in Natural Language Generation","url":"https://huggingface.co/papers/2302.09664"},{"title":"ICLR Oral Semantic Uncertainty: Linguistic Invariances for Uncertainty Estimation in Natural Language Generation","url":"https://iclr.cc/virtual/2023/oral/12609"},{"title":"[PDF] Semantic Uncertainty: Linguistic Invariances for Uncertainty Estimation in Natural Language Generation | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Semantic-Uncertainty:-Linguistic-Invariances-for-in-Kuhn-Gal/507465f8d46489a68a527cb5304d76bdb6c31ed9"},{"title":"Semantic Uncertainty: Linguistic Invariances for Uncertainty Estimation in Natural Language Generation [Quick Review]","url":"https://liner.com/review/semantic-uncertainty-linguistic-invariances-for-uncertainty-estimation-in-natural-language"},{"title":"Semantic Uncertainty: Linguistic Invariances for","url":"https://sebastianfarquhar.com/assets/papers/kuhnSemantic2023.pdf"},{"title":"ICLR Poster Semantic Uncertainty: Linguistic Invariances for Uncertainty Estimation in Natural Language Generation","url":"https://iclr.cc/virtual/2023/poster/11013"},{"title":"Semantic Uncertainty: Linguistic Invariances for Uncertainty Estimation in Natural Language Generation - ADS","url":"https://ui.adsabs.harvard.edu/abs/2023arXiv230209664K/abstract"},{"title":
…[truncated 1415 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_citation_audit_20260517T085237",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 94 · 2026-05-17T08:58:22.633005+00:00_

Web search results for query: "Willard Brandon Louf Rémi "Efficient Guided Generation Large Language Models" arXiv 2307.09702"

Links: [{"title":"[2307.09702] Efficient Guided Generation for Large Language Models","url":"https://arxiv.org/abs/2307.09702"},{"title":"Efficient Guided Generation for Large Language Models","url":"https://arxiv.org/pdf/2307.09702"},{"title":"Paper page - Efficient Guided Generation for Large Language Models","url":"https://huggingface.co/papers/2307.09702"},{"title":"(PDF) Efficient Guided Generation for LLMs","url":"https://www.researchgate.net/publication/372468267_Efficient_Guided_Generation_for_LLMs"},{"title":"[PDF] Efficient Guided Generation for Large Language Models | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Efficient-Guided-Generation-for-Large-Language-Willard-Louf/c4ceaef35bca063815f50d90a087acbd07a65478"},{"title":"[2307.09702v3] Efficient Guided Generation for Large Language Models","url":"https://arxiv.org/abs/2307.09702v3"},{"title":"[2307.09702v2] Efficient Guided Generation for Large Language Models","url":"https://arxiv.org/abs/2307.09702v2"},{"title":"Efficient Guided Generation for Large Language Models - ADS","url":"https://ui.adsabs.harvard.edu/abs/2023arXiv230709702W/abstract"},{"title":"[2307.09702v1] Efficient Guided Generation for LLMs","url":"https://arxiv.org/abs/2307.09702v1"},{"title":"Efficient Guided Generation for LLMs Brandon T. Willard1 and R´emi Louf2","url":"https://arxiv.org/pdf/2307.09702v1"}]

I found the paper you're looking for. Here's what I found:

**Paper Title:** Efficient Guided Generation for Large Language Models

**Authors:** Brandon T. Willard and Rémi Louf

**ArXiv Identifier:** 2307.09702

**Publication Date:** Submitted on 19 Jul 2023

**Overview:**

The paper shows how neural text generation can be reformulated in terms of transitions between states of a finite-state machine, leading to an efficient approach to guiding text generation with regular expressions an
…[truncated 692 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_citation_audit_20260517T085237",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 95 · 2026-05-17T08:58:22.633246+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Culotta Aron McCallum \"Confidence Estimation Information Extraction\" HLT-NAACL 2004"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_citation_audit_20260517T085237",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Culotta Aron McCallum \"Confidence Estimation Information Extraction\" HLT-NAACL 2004"
  }
}
```

</details>

---

### Tool call

_source line 96 · 2026-05-17T08:58:22.633381+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Derczynski Nichols van Erp Limsopatham \"WNUT2017 Shared Task Novel Emerging Entity Recognition\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_citation_audit_20260517T085237",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Derczynski Nichols van Erp Limsopatham \"WNUT2017 Shared Task Novel Emerging Entity Recognition\""
  }
}
```

</details>

---

### Tool call

_source line 97 · 2026-05-17T08:58:22.633501+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Li Peng Sun Tianxiang \"CodeIE Large Code Generation Models Few-Shot Information Extractors\" ACL 2023"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_citation_audit_20260517T085237",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Li Peng Sun Tianxiang \"CodeIE Large Code Generation Models Few-Shot Information Extractors\" ACL 2023"
  }
}
```

</details>

---

### Tool call

_source line 98 · 2026-05-17T08:58:22.633616+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Wadhwa Somin Amir Silvio Wallace \"Revisiting Relation Extraction era Large Language Models\" ACL 2023"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_citation_audit_20260517T085237",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Wadhwa Somin Amir Silvio Wallace \"Revisiting Relation Extraction era Large Language Models\" ACL 2023"
  }
}
```

</details>

---

### Tool call

_source line 99 · 2026-05-17T08:58:22.633728+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Malinin Andrey Gales Mark \"Uncertainty Estimation Autoregressive Structured Prediction\" ICLR 2021"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_citation_audit_20260517T085237",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Malinin Andrey Gales Mark \"Uncertainty Estimation Autoregressive Structured Prediction\" ICLR 2021"
  }
}
```

</details>

---

### Tool call

_source line 100 · 2026-05-17T08:58:22.633838+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Gao Leo Schulman John Hilton Jacob \"Scaling Laws Reward Model Overoptimization\" ICML 2023"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_citation_audit_20260517T085237",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Gao Leo Schulman John Hilton Jacob \"Scaling Laws Reward Model Overoptimization\" ICML 2023"
  }
}
```

</details>

---

### Tool result

_source line 101 · 2026-05-17T08:58:22.633957+00:00_

Web search results for query: "Derczynski Nichols van Erp Limsopatham "WNUT2017 Shared Task Novel Emerging Entity Recognition""

No links found.

I performed the web search for that query. Unfortunately, the search did not return any results. This could mean that:

1. The exact combination of those names and the title may not have an indexed web presence
2. The paper or resource might be available through academic databases (like ACL Anthology, arXiv, or ResearchGate) that may not be fully indexed by standard search engines
3. The title or author names might need slight variations to find the resource

If you're looking for this paper, I'd recommend:
- Checking the ACL Anthology directly (aclanthology.org) for WNUT 2017 workshop papers
- Searching on arXiv or Google Scholar
- Visiting the WNUT 2017 workshop website directly

Would you like me to try a modified search with different terms?


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_citation_audit_20260517T085237",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 102 · 2026-05-17T08:58:22.634107+00:00_

Web search results for query: "Culotta Aron McCallum "Confidence Estimation Information Extraction" HLT-NAACL 2004"

Links: [{"title":"Confidence Estimation for Information Extraction - ACL Anthology","url":"https://www.aclweb.org/anthology/N04-4028/"},{"title":"Conﬁdence Estimation for Information Extraction Aron Culotta","url":"https://people.cs.umass.edu/~mccallum/papers/crfcp-hlt04.pdf"},{"title":"Confidence estimation for information extraction","url":"https://tapilab.github.io/information%20extraction/2004/01/01/confidence"},{"title":"Confidence Estimation for Information Extraction | OpenReview","url":"https://openreview.net/forum?id=SkEs0zZuZr"},{"title":"[PDF] Confidence Estimation for Information Extraction | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Confidence-Estimation-for-Information-Extraction-Culotta-McCallum/1bb9aaeb2b600a4e93e453228ed8844ffd45f6b6"},{"title":"(PDF) Confidence Estimation for Information Extraction","url":"https://www.academia.edu/158491/Confidence_Estimation_for_Information_Extraction"},{"title":"CIIR publications authored by Aron Culotta","url":"https://ciir-publications.cs.umass.edu/search_authors_results.php?id=2160&fname=Aron&lname=Culotta"},{"title":"Adjusting the Recall-Precision Trade-off for Entity Extraction","url":"https://www.cs.cmu.edu/~einat/HLT-NAACL-06.pdf"},{"title":"Confidence Estimation for Information Extraction | Request PDF","url":"https://www.researchgate.net/publication/2605436_Confidence_Estimation_for_Information_Extraction"},{"title":"Human Language Technology Conf. (2004) - ACL Anthology","url":"https://www.aclweb.org/anthology/events/hlt-2004/"}]

I found the paper you're looking for! Here are the search results:

"Confidence Estimation for Information Extraction" by Aron Culotta and Andrew McCallum was published in the Proceedings of HLT-NAACL 2004 as a short paper, with pages 109-112, held May 2-7, 2004 in Boston, Massachusetts, USA.

The paper evaluates an information extraction sy
…[truncated 723 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_citation_audit_20260517T085237",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 103 · 2026-05-17T08:58:22.634309+00:00_

Web search results for query: "Li Peng Sun Tianxiang "CodeIE Large Code Generation Models Few-Shot Information Extractors" ACL 2023"

Links: [{"title":"CodeIE: Large Code Generation Models are Better Few-Shot Information Extractors - ACL Anthology","url":"https://aclanthology.org/2023.acl-long.855/"},{"title":"[2305.05711] CodeIE: Large Code Generation Models are Better Few-Shot Information Extractors","url":"https://arxiv.org/abs/2305.05711"},{"title":"CODEIE: Large Code Generation Models are Better Few- ...","url":"https://aclanthology.org/2023.acl-long.855.pdf"},{"title":"GitHub - artpli/CodeIE: [ACL 23] CodeIE: Large Code Generation Models are Better Few-Shot Information Extractors · GitHub","url":"https://github.com/artpli/CodeIE"},{"title":"[Quick Review] CodeIE: Large Code Generation Models are Better Few-Shot Information Extractors","url":"https://liner.com/review/codeie-large-code-generation-models-are-better-fewshot-information-extractors"},{"title":"dblp: CodeIE: Large Code Generation Models are Better Few-Shot Information Extractors.","url":"https://dblp.uni-trier.de/rec/journals/corr/abs-2305-05711.html"},{"title":"[PDF] CodeIE: Large Code Generation Models are Better Few-Shot Information Extractors | Semantic Scholar","url":"https://www.semanticscholar.org/paper/CodeIE:-Large-Code-Generation-Models-are-Better-Li-Sun/a86dd6c62d3dc9c7989c98a3e4ace3fd8000e515"},{"title":"[2305.05711v2] CodeIE: Large Code Generation Models are Better Few-Shot Information Extractors","url":"https://arxiv.org/abs/2305.05711v2"},{"title":"Main Conference - ACL 2023","url":"https://2023.aclweb.org/program/accepted_main_conference/"},{"title":"CodeIE: Large Code Generation Models are Better Few-Shot Information Extractors | Request PDF","url":"https://www.researchgate.net/publication/372919086_CodeIE_Large_Code_Generation_Models_are_Better_Few-Shot_Information_Extractors"}]

I found the paper successfully! Here are the search results:

## CodeIE: Large Code Generation Models ar
…[truncated 1136 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_citation_audit_20260517T085237",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 104 · 2026-05-17T08:58:22.634490+00:00_

Web search results for query: "Wadhwa Somin Amir Silvio Wallace "Revisiting Relation Extraction era Large Language Models" ACL 2023"

Links: [{"title":"Revisiting Relation Extraction in the era of Large Language Models - ACL Anthology","url":"https://aclanthology.org/2023.acl-long.868/"},{"title":"Revisiting Relation Extraction in the era of Large Language ...","url":"https://aclanthology.org/2023.acl-long.868.pdf"},{"title":"Revisiting Relation Extraction in the era of Large Language Models - PMC","url":"https://pmc.ncbi.nlm.nih.gov/articles/PMC10482322/"},{"title":"[2305.05003] Revisiting Relation Extraction in the era of Large Language Models","url":"https://arxiv.org/abs/2305.05003"},{"title":"Revisiting Relation Extraction in the era of Large Language Models - PubMed","url":"https://pubmed.ncbi.nlm.nih.gov/37674787/"},{"title":"Revisiting Relation Extraction in the era of Large Language Models | NSF Public Access Repository","url":"https://par.nsf.gov/biblio/10523775-revisiting-relation-extraction-era-large-language-models"},{"title":"[PDF] Revisiting Relation Extraction in the era of Large Language Models | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Revisiting-Relation-Extraction-in-the-era-of-Large-Wadhwa-Amir/97782a67971c4ff1a74bf07e82fe20b2c4bf86c4"},{"title":"[Quick Review] Revisiting Relation Extraction in the era of Large Language Models","url":"https://liner.com/review/revisiting-relation-extraction-in-era-large-language-models"},{"title":"dblp: Somin Wadhwa","url":"https://dblp.org/pid/265/5925.html"},{"title":"Somin Wadhwa - ACL Anthology","url":"https://aclanthology.org/people/somin-wadhwa/"}]

I found the paper you were searching for! Here are the results:

## Paper Information

**Title:** Revisiting Relation Extraction in the era of Large Language Models

**Authors:** Somin Wadhwa, Silvio Amir, and Byron Wallace

**Conference:** Proceedings of the 61st Annual Meeting of the Association for Computational Linguistics (Volume 1: Lo
…[truncated 967 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_citation_audit_20260517T085237",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 105 · 2026-05-17T08:58:22.634662+00:00_

Web search results for query: "Malinin Andrey Gales Mark "Uncertainty Estimation Autoregressive Structured Prediction" ICLR 2021"

Links: [{"title":"Uncertainty Estimation in Autoregressive Structured Prediction | OpenReview","url":"https://openreview.net/forum?id=jN5y-zb5Q7m"},{"title":"Uncertainty Estimation in Autoregressive Structured Prediction | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Uncertainty-Estimation-in-Autoregressive-Structured-Malinin-Gales/0921322cf6ea34d1852f13cb67eeac9d1f863518"},{"title":"Andrey Malinin, Mark Gales · Uncertainty Estimation in Autoregressive Structured Prediction","url":"https://slideslive.com/38953932/uncertainty-estimation-in-autoregressive-structured-prediction"},{"title":"[2002.07650] Uncertainty Estimation in Autoregressive Structured Prediction","url":"https://arxiv.org/abs/2002.07650"},{"title":"Published as a conference paper at ICLR 2021 UNCERTAINTY ESTIMATION IN","url":"https://openreview.net/pdf?id=jN5y-zb5Q7m"},{"title":"UNCERTAINTY ESTIMATION IN AUTOREGRESSIVE STRUCTURED PREDICTION","url":"https://www.repository.cam.ac.uk/items/c98871de-7bff-410b-948a-f951dd90716e"},{"title":"GitHub - yandex-research/proxy-dirichlet-distillation: Implementation of \"Scaling Ensemble Distribution Distillation to Many Classes with Proxy Targets\" (NeurIPS 2021) and \"Uncertainty Estimation in Autoregressive Structured Prediction\" (ICLR 2021)","url":"https://github.com/yandex-research/proxy-dirichlet-distillation"},{"title":"dblp: Andrey Malinin","url":"https://dblp.org/pid/174/5705.html"},{"title":"Uncertainty Estimation in Autoregressive Structured Prediction","url":"https://papertalk.org/papertalks/29066"},{"title":"Uncertainty Estimation in Autoregressive Structured Prediction | Papers With Code","url":"https://paperswithcode.com/paper/uncertainty-in-structured-prediction"}]

I've found information about the paper "Uncertainty Estimation in Autoregressive Structured Prediction" by Malinin and Gales.

## Key Fin
…[truncated 1147 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_citation_audit_20260517T085237",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 106 · 2026-05-17T08:58:22.634832+00:00_

Web search results for query: "Gao Leo Schulman John Hilton Jacob "Scaling Laws Reward Model Overoptimization" ICML 2023"

Links: [{"title":"Scaling Laws for Reward Model Overoptimization","url":"https://proceedings.mlr.press/v202/gao23h.html"},{"title":"Scaling laws for reward model overoptimization | Proceedings of the 40th International Conference on Machine Learning","url":"https://dl.acm.org/doi/10.5555/3618408.3618845"},{"title":"ICML Poster Scaling Laws for Reward Model Overoptimization","url":"https://icml.cc/virtual/2023/poster/24924"},{"title":"[PDF] Scaling Laws for Reward Model Overoptimization | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Scaling-Laws-for-Reward-Model-Overoptimization-Gao-Schulman/fb3dc5e20e0a71134ca916f0d6d8d41f01225b4b"},{"title":"[2210.10760] Scaling Laws for Reward Model Overoptimization","url":"https://arxiv.org/abs/2210.10760"},{"title":"Scaling Laws for Reward Model Overoptimization - researchr publication","url":"https://researchr.org/publication/GaoSH23"},{"title":"Scaling Laws for Reward Model Overoptimization - ADS","url":"https://ui.adsabs.harvard.edu/abs/2022arXiv221010760G/abstract"},{"title":"Published as a conference paper at ICLR 2025","url":"https://arxiv.org/pdf/2410.05584"},{"title":"Scaling Laws for Reward Model Overoptimization","url":"https://www.researchgate.net/publication/364436070_Scaling_Laws_for_Reward_Model_Overoptimization"},{"title":"Scaling Laws for Reward Model Overoptimization","url":"https://www.alignmentforum.org/posts/shcSdHGPhnLQkpSbX/scaling-laws-for-reward-model-overoptimization"}]

I found the research paper you were looking for! Here's what I found:

## Paper Details

The paper "Scaling Laws for Reward Model Overoptimization" by Leo Gao, John Schulman, and Jacob Hilton was published in the Proceedings of the 40th International Conference on Machine Learning (ICML 2023), with pages 10835-10866.

## Overview

In reinforcement learning from human feedback, it is common to optimi
…[truncated 1078 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_citation_audit_20260517T085237",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 107 · 2026-05-17T08:58:22.635000+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Derczynski Leon \"Results WNUT2017 Shared Task Novel Emerging Entity Recognition\" EMNLP 2017 W-NUT"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_citation_audit_20260517T085237",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Derczynski Leon \"Results WNUT2017 Shared Task Novel Emerging Entity Recognition\" EMNLP 2017 W-NUT"
  }
}
```

</details>

---

### Tool call

_source line 108 · 2026-05-17T08:58:22.635140+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Ding Ning Xu Guangwei \"Few-NERD Few-shot Named Entity Recognition Dataset\" ACL 2021"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_citation_audit_20260517T085237",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Ding Ning Xu Guangwei \"Few-NERD Few-shot Named Entity Recognition Dataset\" ACL 2021"
  }
}
```

</details>

---

### Tool call

_source line 109 · 2026-05-17T08:58:22.635267+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Kadavath Saurav \"Language Models Mostly Know What They Know\" arXiv 2207.05221 Anthropic"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_citation_audit_20260517T085237",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Kadavath Saurav \"Language Models Mostly Know What They Know\" arXiv 2207.05221 Anthropic"
  }
}
```

</details>

---

### Tool call

_source line 110 · 2026-05-17T08:58:22.635416+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Luan Yi He Luheng \"Multi-Task Identification Entities Relations Coreference Scientific Knowledge Graph\" EMNLP 2018"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_citation_audit_20260517T085237",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Luan Yi He Luheng \"Multi-Task Identification Entities Relations Coreference Scientific Knowledge Graph\" EMNLP 2018"
  }
}
```

</details>

---

### Tool result

_source line 111 · 2026-05-17T08:58:22.635589+00:00_

Web search results for query: "Derczynski Leon "Results WNUT2017 Shared Task Novel Emerging Entity Recognition" EMNLP 2017 W-NUT"

Links: [{"title":"Results of the WNUT2017 Shared Task on Novel and Emerging Entity Recognition - ACL Anthology","url":"https://aclanthology.org/W17-4418/"},{"title":"Results of the WNUT2017 Shared Task on Novel and Emerging Entity Recognition | Request PDF","url":"https://www.researchgate.net/publication/322590094_Results_of_the_WNUT2017_Shared_Task_on_Novel_and_Emerging_Entity_Recognition"},{"title":"Results of the WNUT2017 Shared Task on Novel and Emerging Entity Recognition","url":"https://www.derczynski.com/sheffield/papers/emerging-wnut.pdf"},{"title":"Results of the WNUT2017 Shared Task on Novel and Emerging Entity Recognition - Royal Netherlands Academy of Arts and Sciences (KNAW)","url":"https://pure.knaw.nl/portal/en/publications/results-of-the-wnut2017-shared-task-on-novel-and-emerging-entity-"},{"title":"[PDF] Results of the WNUT2017 Shared Task on Novel and Emerging Entity Recognition | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Results-of-the-WNUT2017-Shared-Task-on-Novel-and-Derczynski-Nichols/72e87913632d0f1295fbcfa46795c5bb26d0a422"},{"title":"GitHub - leondz/emerging_entities_17: Dataset for the Emerging & Novel Entity NER task (WNUT '17) · GitHub","url":"https://github.com/leondz/emerging_entities_17"},{"title":"Emerging and Rare Entity Recognition","url":"http://noisy-text.github.io/2017/emerging-rare-entities.html"},{"title":"Results of the WNUT2017 Shared Task on Novel and Emerging Entity Recognition | Papers With Code","url":"https://paperswithcode.com/paper/results-of-the-wnut2017-shared-task-on-novel"},{"title":"W-NUT 2017: Workshop on Noisy User-generated Text (at EMNLP)","url":"https://noisy-text.github.io/2017/"},{"title":"Proceedings of the 3rd Workshop on Noisy User-generated Text - ACL Anthology","url":"https://aclanthology.org/volumes/W17-44/"}]

I've successfully found the paper you're 
…[truncated 769 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_citation_audit_20260517T085237",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 112 · 2026-05-17T08:58:22.635737+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Manakul Potsawee Liusie Gales \"SelfCheckGPT Zero-Resource Black-Box Hallucination Detection\" EMNLP 2023"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_citation_audit_20260517T085237",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Manakul Potsawee Liusie Gales \"SelfCheckGPT Zero-Resource Black-Box Hallucination Detection\" EMNLP 2023"
  }
}
```

</details>

---

### Tool call

_source line 113 · 2026-05-17T08:58:22.635859+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Tian Katherine Mitchell Eric \"Just Ask for Calibration Strategies Eliciting Calibrated Confidence\" EMNLP 2023"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_citation_audit_20260517T085237",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Tian Katherine Mitchell Eric \"Just Ask for Calibration Strategies Eliciting Calibrated Confidence\" EMNLP 2023"
  }
}
```

</details>

---

### Tool result

_source line 114 · 2026-05-17T08:58:22.636000+00:00_

Web search results for query: "Kadavath Saurav "Language Models Mostly Know What They Know" arXiv 2207.05221 Anthropic"

Links: [{"title":"[2207.05221] Language Models (Mostly) Know What They Know","url":"https://arxiv.org/abs/2207.05221"},{"title":"Language Models (Mostly) Know What They Know","url":"https://arxiv.org/pdf/2207.05221"},{"title":"(PDF) Language Models (Mostly) Know What They Know","url":"https://www.researchgate.net/publication/361949621_Language_Models_Mostly_Know_What_They_Know"},{"title":"Language Models (Mostly) Know What They Know - ADS","url":"https://ui.adsabs.harvard.edu/abs/2022arXiv220705221K/abstract"},{"title":"(PDF) Language Models (Mostly) Know What They Know (2022) | Saurav Kadavath | 413 Citations","url":"https://scispace.com/papers/language-models-mostly-know-what-they-know-zkg0pou4"},{"title":"[PDF] Language Models (Mostly) Know What They Know | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Language-Models-(Mostly)-Know-What-They-Know-Kadavath-Conerly/142ebbf4760145f591166bde2564ac70c001e927"},{"title":"Language Models (Mostly) Know What They Know | alphaXiv","url":"https://www.alphaxiv.org/overview/2207.05221v4"},{"title":"Language Models (Mostly) Know What They Know \\ Anthropic","url":"https://www.anthropic.com/research/language-models-mostly-know-what-they-know"},{"title":"Language Models (Mostly) Know What They Know","url":"https://bibbase.org/network/publication/kadavath-conerly-askell-henighan-drain-perez-schiefer-hatfielddodds-etal-languagemodelsmostlyknowwhattheyknow-2022"},{"title":"[2207.05221v4] Language Models (Mostly) Know What They Know","url":"https://arxiv.org/abs/2207.05221v4"}]

I found comprehensive information about the paper you searched for. Here are the key details:

## Paper Overview

"Language Models (Mostly) Know What They Know" is authored by Saurav Kadavath, Tom Conerly, Amanda Askell, Tom Henighan, Dawn Drain, Ethan Perez, Nicholas Schiefer, Zac Hatfield-Dodds, Nova DasSarma, Eli Tran-J
…[truncated 1407 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_citation_audit_20260517T085237",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 115 · 2026-05-17T08:58:22.636211+00:00_

Web search results for query: "Luan Yi He Luheng "Multi-Task Identification Entities Relations Coreference Scientific Knowledge Graph" EMNLP 2018"

Links: [{"title":"Multi-Task Identification of Entities, Relations, and Coreference for Scientific Knowledge Graph Construction - ACL Anthology","url":"https://aclanthology.org/D18-1360/"},{"title":"Multi-Task Identification of Entities, Relations, and Coreference for Scientific Knowledge Graph Construction","url":"https://www.researchgate.net/publication/334115742_Multi-Task_Identification_of_Entities_Relations_and_Coreference_for_Scientific_Knowledge_Graph_Construction"},{"title":"[1808.09602] Multi-Task Identification of Entities, Relations, and Coreference for Scientific Knowledge Graph Construction","url":"https://arxiv.org/abs/1808.09602"},{"title":"dblp: Multi-Task Identification of Entities, Relations, and Coreference for Scientific Knowledge Graph Construction.","url":"https://dblp.org/rec/conf/emnlp/LuanHOH18.html"},{"title":"[PDF] Multi-Task Identification of Entities, Relations, and Coreference for Scientific Knowledge Graph Construction | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Multi-Task-Identification-of-Entities,-Relations,-Luan-He/b21b927c251c415b601b6d7f785a42cc5c292635"},{"title":"Multi-Task Identification of Entities, Relations, and Coreference for Scientific Knowledge Graph Construction - ADS","url":"https://ui.adsabs.harvard.edu/abs/2018arXiv180809602L/abstract"},{"title":"Multi-Task Identification of Entities, Relations, and Coreferencefor Scientific Knowledge Graph Construction","url":"https://nlp.cs.washington.edu/sciIE/"},{"title":"Multi-Task Identification of Entities, Relations, and Coreference for Scientific Knowledge Graph Construction - Consensus","url":"https://k8s.consensus.app/papers/details/ce11b64546755e678612cfea3b404121/"},{"title":"[1808.09602v1] Multi-Task Identification of Entities, Relations, and Coreference for Scientific Knowledge Graph Construction","url
…[truncated 1526 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_citation_audit_20260517T085237",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 116 · 2026-05-17T08:58:22.636405+00:00_

Web search results for query: "Ding Ning Xu Guangwei "Few-NERD Few-shot Named Entity Recognition Dataset" ACL 2021"

Links: [{"title":"Few-NERD: A Few-shot Named Entity Recognition Dataset - ACL Anthology","url":"https://aclanthology.org/2021.acl-long.248/"},{"title":"GitHub - thunlp/Few-NERD: Code and data of ACL 2021 paper \"Few-NERD: A Few-shot Named Entity Recognition Dataset\" · GitHub","url":"https://github.com/thunlp/Few-NERD"},{"title":"Few-NERD","url":"https://ningding97.github.io/fewnerd/"},{"title":"FEW-NERD: A Few-shot Named Entity Recognition Dataset","url":"https://aclanthology.org/2021.acl-long.248.pdf"},{"title":"[2105.07464] Few-NERD: A Few-Shot Named Entity Recognition Dataset","url":"https://arxiv.org/abs/2105.07464"},{"title":"Few-NERD: A Few-shot Named Entity Recognition Dataset | Performance Analytics","url":"https://www.scinapse.io/papers/3177312484"},{"title":"Few-NERD: A Few-Shot Named Entity Recognition Dataset - ADS","url":"https://ui.adsabs.harvard.edu/abs/2021arXiv210507464D/abstract"},{"title":"Papers with Code - Few-NERD: A Few-Shot Named Entity Recognition Dataset","url":"https://paperswithcode.com/paper/few-nerd-a-few-shot-named-entity-recognition"},{"title":"[2105.07464v5] Few-NERD: A Few-Shot Named Entity Recognition Dataset","url":"https://arxiv.org/abs/2105.07464v5"},{"title":"Few-NERD: A Few-shot Named Entity Recognition Dataset | Request PDF","url":"https://www.researchgate.net/publication/353490454_Few-NERD_A_Few-shot_Named_Entity_Recognition_Dataset"}]

I found the paper you're looking for! Here are the key details:

## Few-NERD: A Few-shot Named Entity Recognition Dataset

The paper "Few-NERD: A Few-shot Named Entity Recognition Dataset" was authored by Ning Ding, Guangwei Xu, Yulin Chen, Xiaobin Wang, Xu Han, Pengjun Xie, Haitao Zheng, and Zhiyuan Liu, published at ACL-IJCNLP 2021. It appears in the Proceedings of the 59th Annual Meeting of the Association for Computational Linguistics and the 11th International Joint Confe
…[truncated 725 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_citation_audit_20260517T085237",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 117 · 2026-05-17T08:58:22.636593+00:00_

Web search results for query: "Manakul Potsawee Liusie Gales "SelfCheckGPT Zero-Resource Black-Box Hallucination Detection" EMNLP 2023"

Links: [{"title":"GitHub - potsawee/selfcheckgpt: SelfCheckGPT: Zero-Resource Black-Box Hallucination Detection for Generative Large Language Models · GitHub","url":"https://github.com/potsawee/selfcheckgpt"},{"title":"[2303.08896] SelfCheckGPT: Zero-Resource Black-Box Hallucination Detection for Generative Large Language Models","url":"https://arxiv.org/abs/2303.08896"},{"title":"SelfCheckGPT: Zero-Resource Black-Box Hallucination Detection for Generative Large Language Models - ACL Anthology","url":"https://aclanthology.org/2023.emnlp-main.557/"},{"title":"SELFCHECKGPT: Zero-Resource Black-Box Hallucination ...","url":"https://aclanthology.org/2023.emnlp-main.557.pdf"},{"title":"EMNLP2023: SelfCheckGPT: Zero-Resource Black-Box Hallucination Detection for Generative Large Language Models","url":"https://virtual2023.emnlp.org/paper_349.html"},{"title":"[PDF] SelfCheckGPT: Zero-Resource Black-Box Hallucination Detection for Generative Large Language Models | Semantic Scholar","url":"https://www.semanticscholar.org/paper/SelfCheckGPT:-Zero-Resource-Black-Box-Hallucination-Manakul-Liusie/7c1707db9aafd209aa93db3251e7ebd593d55876"},{"title":"Paper page - SelfCheckGPT: Zero-Resource Black-Box Hallucination Detection for Generative Large Language Models","url":"https://huggingface.co/papers/2303.08896"},{"title":"(PDF) SelfCheckGPT: Zero-Resource Black-Box Hallucination Detection for Generative Large Language Models","url":"https://www.researchgate.net/publication/376402462_SelfCheckGPT_Zero-Resource_Black-Box_Hallucination_Detection_for_Generative_Large_Language_Models"},{"title":"SelfCheckGPT: Zero-Resource Black-Box Hallucination Detection for Generative Large Language Models | OpenReview","url":"https://openreview.net/forum?id=RwzFNbJ3Ez"},{"title":"[Quick Review] SelfCheckGPT: Zero-Resource Black-Box Hallucination Detection for Gener
…[truncated 1951 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_citation_audit_20260517T085237",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 118 · 2026-05-17T08:58:22.636775+00:00_

Web search results for query: "Tian Katherine Mitchell Eric "Just Ask for Calibration Strategies Eliciting Calibrated Confidence" EMNLP 2023"

No links found.

I was unable to find results for that exact query. Let me try a more focused search:

Links: [{"title":"Just Ask for Calibration: Strategies for Eliciting Calibrated Confidence Scores from Language Models Fine-Tuned with Human Feedback - ACL Anthology","url":"https://aclanthology.org/2023.emnlp-main.330/"},{"title":"Strategies for Eliciting Calibrated Confidence Scores from ...","url":"https://aclanthology.org/2023.emnlp-main.330.pdf"},{"title":"[Quick Review] Just Ask for Calibration: Strategies for Eliciting Calibrated Confidence Scores from Language Models Fine-Tuned with Human Feedback","url":"https://liner.com/review/just-ask-for-calibration-strategies-for-eliciting-calibrated-confidence-scores"},{"title":"[2305.14975] Just Ask for Calibration: Strategies for Eliciting Calibrated Confidence Scores from Language Models Fine-Tuned with Human Feedback","url":"https://arxiv.org/abs/2305.14975"},{"title":"Just Ask for Calibration: Strategies for Eliciting Calibrated Confidence Scores from Language Models Fine-Tuned with Human Feedback | OpenReview","url":"https://openreview.net/forum?id=g3faCfrwm7"},{"title":"[2305.14975] Just Ask for Calibration: Strategies for Eliciting Calibrated Confidence Scores from Language Models Fine-Tuned with Human Feedback","url":"https://ar5iv.labs.arxiv.org/html/2305.14975"},{"title":"GitHub - ShiyuNee/Awesome-Calibration-Papers: A curated list of awesome papers about calibration · GitHub","url":"https://github.com/ShiyuNee/Awesome-Calibration-Papers"},{"title":"Just Ask for Calibration: Strategies for Eliciting Calibrated Confidence Scores from Language Models Fine-Tuned with Human Feedback","url":"https://www.researchgate.net/publication/376394186_Just_Ask_for_Calibration_Strategies_for_Eliciting_Calibrated_Confidence_Scores_from_Language_Models_Fine-Tuned_with_Human_Feedback"
…[truncated 1676 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_citation_audit_20260517T085237",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 119 · 2026-05-17T08:58:22.636955+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Eikema Bryan Aziz Wilker \"Sampling-Based Approximations Minimum Bayes Risk Decoding Neural Machine Translation\" EMNLP 2022"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_citation_audit_20260517T085237",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Eikema Bryan Aziz Wilker \"Sampling-Based Approximations Minimum Bayes Risk Decoding Neural Machine Translation\" EMNLP 2022"
  }
}
```

</details>

---

### Tool call

_source line 120 · 2026-05-17T08:58:22.637102+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Freitag Markus Grangier \"High Quality Rather than High Model Probability Minimum Bayes Risk Neural Metrics\" TACL 2022"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_citation_audit_20260517T085237",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Freitag Markus Grangier \"High Quality Rather than High Model Probability Minimum Bayes Risk Neural Metrics\" TACL 2022"
  }
}
```

</details>

---

### Tool call

_source line 121 · 2026-05-17T08:58:22.637253+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Fernandes Patrick Farinhas Rei \"Quality-Aware Decoding Neural Machine Translation\" NAACL 2022"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_citation_audit_20260517T085237",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Fernandes Patrick Farinhas Rei \"Quality-Aware Decoding Neural Machine Translation\" NAACL 2022"
  }
}
```

</details>

---

### Tool call

_source line 122 · 2026-05-17T08:58:22.637372+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Holtzman Ari Buys Jan \"Curious Case Neural Text Degeneration\" nucleus sampling ICLR 2020"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_citation_audit_20260517T085237",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Holtzman Ari Buys Jan \"Curious Case Neural Text Degeneration\" nucleus sampling ICLR 2020"
  }
}
```

</details>

---

### Tool result

_source line 123 · 2026-05-17T08:58:22.637521+00:00_

Web search results for query: "Eikema Bryan Aziz Wilker "Sampling-Based Approximations Minimum Bayes Risk Decoding Neural Machine Translation" EMNLP 2022"

Links: [{"title":"Sampling-Based Approximations to Minimum Bayes Risk Decoding for Neural Machine Translation - ACL Anthology","url":"https://aclanthology.org/2022.emnlp-main.754/"},{"title":"[2108.04718] Sampling-Based Approximations to Minimum Bayes Risk Decoding for Neural Machine Translation","url":"https://arxiv.org/abs/2108.04718"},{"title":"Sampling-Based Approximations to Minimum Bayes Risk Decoding for","url":"https://arxiv.org/pdf/2108.04718"},{"title":"(PDF) Sampling-Based Approximations to Minimum Bayes Risk Decoding for Neural Machine Translation","url":"https://www.researchgate.net/publication/372923772_Sampling-Based_Approximations_to_Minimum_Bayes_Risk_Decoding_for_Neural_Machine_Translation"},{"title":"Papers - Wilker Aziz","url":"https://wilkeraziz.github.io/papers/"},{"title":"Sampling-Based Minimum Bayes Risk Decoding for Neural Machine Translation | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Sampling-Based-Minimum-Bayes-Risk-Decoding-for-Eikema-Aziz/994dbb06b970eb842b7782e4df75ca1633f83e4e"},{"title":"dblp: Wilker Aziz","url":"https://dblp.org/pid/51/10489.html"},{"title":"dblp: Bryan Eikema","url":"https://dblp.org/pid/223/9865.html"},{"title":"Publications · Bryan Eikema","url":"https://bryaneikema.com/publications/"},{"title":"Generating Diverse and High-Quality Texts by Minimum Bayes Risk Decoding","url":"https://www.emergentmind.com/papers/2401.05054"}]

I found the paper you're looking for! 

**"Sampling-Based Approximations to Minimum Bayes Risk Decoding for Neural Machine Translation"** by Bryan Eikema and Wilker Aziz was published in the Proceedings of the 2022 Conference on Empirical Methods in Natural Language Processing, pages 10978–10993, in Abu Dhabi, United Arab Emirates.

The paper analyzes an approximation to minimum Bayes risk (MBR) decoding as an alterna
…[truncated 517 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_citation_audit_20260517T085237",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 124 · 2026-05-17T08:58:22.637673+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Müller Mathias Sennrich Rico \"Understanding Properties Minimum Bayes Risk Decoding Neural Machine Translation\" ACL 2021"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_citation_audit_20260517T085237",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Müller Mathias Sennrich Rico \"Understanding Properties Minimum Bayes Risk Decoding Neural Machine Translation\" ACL 2021"
  }
}
```

</details>

---

### Tool call

_source line 125 · 2026-05-17T08:58:22.637803+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Fomicheva Marina Sun Shuo \"Unsupervised Quality Estimation Neural Machine Translation\" TACL 2020"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_citation_audit_20260517T085237",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Fomicheva Marina Sun Shuo \"Unsupervised Quality Estimation Neural Machine Translation\" TACL 2020"
  }
}
```

</details>

---

### Tool result

_source line 126 · 2026-05-17T08:58:22.637948+00:00_

Web search results for query: "Fernandes Patrick Farinhas Rei "Quality-Aware Decoding Neural Machine Translation" NAACL 2022"

Links: [{"title":"Quality-Aware Decoding for Neural Machine Translation - ACL Anthology","url":"https://aclanthology.org/2022.naacl-main.100/"},{"title":"Quality-Aware Decoding for Neural Machine Translation | Request PDF","url":"https://www.researchgate.net/publication/362261547_Quality-Aware_Decoding_for_Neural_Machine_Translation"},{"title":"Patrick Fernandes*, António Farinhas*, Ricardo Rei,","url":"https://antonio-farinhas.github.io/documents/2022_NAACL_Poster.pdf"},{"title":"[2205.00978] Quality-Aware Decoding for Neural Machine Translation","url":"https://arxiv.org/abs/2205.00978"},{"title":"Quality-Aware Decoding for Neural Machine Translation | CoLab","url":"https://colab.ws/articles/10.18653/v1/2022.naacl-main.100"},{"title":"Accepted Papers - NAACL-HLT 2022","url":"https://2022.naacl.org/program/accepted_papers/"},{"title":"Publications - António Farinhas","url":"https://antonio-farinhas.github.io/publications/"},{"title":"[PDF] Quality-Aware Decoding for Neural Machine Translation | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Quality-Aware-Decoding-for-Neural-Machine-Fernandes-Farinhas/0cceebb6b796c210b55ebf6b98032b5c631db0e1"},{"title":"Papers with Code - António Farinhas","url":"https://paperswithcode.com/author/antonio-farinhas"},{"title":"Publications - André F. T. Martins","url":"https://andre-martins.github.io/pages/publications.html"}]

I found the paper you're looking for! Here are the key details:

**Quality-Aware Decoding for Neural Machine Translation** was published by Patrick Fernandes, António Farinhas, Ricardo Rei, José G. C. de Souza, Perez Ogayo, Graham Neubig, and Andre Martins at the 2022 Conference of the North American Chapter of the Association for Computational Linguistics: Human Language Technologies (NAACL 2022) in Seattle, United States.

**Paper Overview:**

The paper addresses how de
…[truncated 960 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_citation_audit_20260517T085237",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 127 · 2026-05-17T08:58:22.638142+00:00_

Web search results for query: "Holtzman Ari Buys Jan "Curious Case Neural Text Degeneration" nucleus sampling ICLR 2020"

Links: [{"title":"[Paper Note] The Curious Case of Neural Text Degeneration, Ari Holtzman+, ICLR'20 · Issue #1889 · AkihikoWatanabe/paper_notes","url":"https://github.com/AkihikoWatanabe/paper_notes/issues/1889"},{"title":"[1904.09751] The Curious Case of Neural Text Degeneration","url":"https://arxiv.org/abs/1904.09751"},{"title":"ICLR: The Curious Case of Neural Text Degeneration","url":"https://iclr.cc/virtual_2020/poster_rygGQyrFvH.html"},{"title":"THE CURIOUS CASE OF NEURAL TEXT DeGENERATION","url":"https://openreview.net/pdf?id=rygGQyrFvH"},{"title":"The Curious Case of Neural Text Degeneration","url":"https://www.researchgate.net/publication/332590110_The_Curious_Case_of_Neural_Text_Degeneration"},{"title":"The Curious Case of Neural Text Degeneration - UCT Computer Science Research Document Archive","url":"https://pubs.cs.uct.ac.za/id/eprint/1407/"},{"title":"(PDF) The Curious Case of Neural Text Degeneration (2020) | Ari Holtzman | 689 Citations","url":"https://scispace.com/papers/the-curious-case-of-neural-text-degeneration-2xplgl0dw1"},{"title":"[SNLP2020] The Curious Case of Neural Text Degeneration - Speaker Deck","url":"https://speakerdeck.com/butsugiri/snlp2020-the-curious-case-of-neural-text-degeneration"},{"title":"The Curious Case of Neural Text Degeneration","url":"https://hyunyoung2.github.io/2020/06/04/The_Curious_Case_of_Neural_Text_Degeneration/"},{"title":"CLOSING THE CURIOUS CASE OF NEURAL TEXT DEGENERATION Matthew Finlayson∗","url":"https://proceedings.iclr.cc/paper_files/paper/2024/file/34899013589ef41aea4d7b2f0ef310c1-Paper-Conference.pdf"}]

Based on the search results, I found comprehensive information about the paper you're interested in:

The paper "The Curious Case of Neural Text Degeneration" was authored by Ari Holtzman, Jan Buys, Li Du, Maxwell Forbes, and Yejin Choi and was presented at the International Confe
…[truncated 1365 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_citation_audit_20260517T085237",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 128 · 2026-05-17T08:58:22.638330+00:00_

Web search results for query: "Freitag Markus Grangier "High Quality Rather than High Model Probability Minimum Bayes Risk Neural Metrics" TACL 2022"

No links found.

The search returned no results for that exact query. Let me try a more focused search:

Links: [{"title":"High Quality Rather than High Model Probability: Minimum Bayes Risk Decoding with Neural Metrics - ACL Anthology","url":"https://aclanthology.org/2022.tacl-1.47/"},{"title":"High Quality Rather than High Model Probability: Minimum Bayes Risk Decoding with Neural Metrics | Transactions of the Association for Computational Linguistics | MIT Press","url":"https://direct.mit.edu/tacl/article/doi/10.1162/tacl_a_00491/112497/High-Quality-Rather-than-High-Model-Probability"},{"title":"[2111.09388] High Quality Rather than High Model Probability: Minimum Bayes Risk Decoding with Neural Metrics","url":"https://arxiv.org/abs/2111.09388"},{"title":"High Quality Rather than High Model Probability: Minimum Bayes Risk Decoding with Neural Metrics | Transactions of the Association for Computational Linguistics","url":"https://transacl.org/index.php/tacl/article/view/3735"},{"title":"High Quality Rather than High Model Probability: Minimum Bayes Risk Decoding with Neural Metrics","url":"https://ouci.dntb.gov.ua/en/works/4KXgDQol/"},{"title":"[2111.09388v1] Minimum Bayes Risk Decoding with Neural Metrics of Translation Quality","url":"https://arxiv.org/abs/2111.09388v1"},{"title":"(PDF) High Quality Rather than High Model Probability: Minimum Bayes Risk Decoding with Neural Metrics","url":"https://www.researchgate.net/publication/362424330_High_Quality_Rather_than_High_Model_Probability_Minimum_Bayes_Risk_Decoding_with_Neural_Metrics"},{"title":"Theoretical Aspects of Bias and Diversity in Minimum Bayes Risk Decoding","url":"https://arxiv.org/html/2410.15021v1"},{"title":"Efficient Minimum Bayes Risk Decoding using Low-Rank Matrix Completion Algorithms","url":"https://arxiv.org/html/2406.02832v1"},{"title":"Source
…[truncated 1553 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_citation_audit_20260517T085237",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 129 · 2026-05-17T08:58:22.638510+00:00_

Web search results for query: "Fomicheva Marina Sun Shuo "Unsupervised Quality Estimation Neural Machine Translation" TACL 2020"

Links: [{"title":"Unsupervised Quality Estimation for Neural Machine Translation - ACL Anthology","url":"https://aclanthology.org/2020.tacl-1.35/"},{"title":"Unsupervised Quality Estimation for Neural Machine Translation | Transactions of the Association for Computational Linguistics | MIT Press","url":"https://direct.mit.edu/tacl/article/doi/10.1162/tacl_a_00330/96475/Unsupervised-Quality-Estimation-for-Neural-Machine"},{"title":"[2005.10608] Unsupervised Quality Estimation for Neural Machine Translation","url":"https://arxiv.org/abs/2005.10608"},{"title":"Unsupervised Quality Estimation for Neural Machine Translation | Transactions of the Association for Computational Linguistics","url":"https://transacl.org/ojs/index.php/tacl/article/view/1997"},{"title":"Unsupervised Quality Estimation for Neural Machine Translation - Tilburg University Research Portal","url":"https://research.tilburguniversity.edu/en/publications/unsupervised-quality-estimation-for-neural-machine-translation-2"},{"title":"Unsupervised Quality Estimation for Neural Machine Translation","url":"https://aclanthology.org/2020.tacl-1.35.pdf"},{"title":"Unsupervised Quality Estimation for Neural Machine Translation | ScienceGate","url":"https://www.sciencegate.app/document/10.1162/tacl_a_00330"},{"title":"(PDF) Unsupervised Quality Estimation for Neural Machine Translation","url":"https://www.researchgate.net/publication/344763694_Unsupervised_Quality_Estimation_for_Neural_Machine_Translation"},{"title":"[PDF] Unsupervised Quality Estimation for Neural Machine Translation | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Unsupervised-Quality-Estimation-for-Neural-Machine-Fomicheva-Sun/8ae3421420ec57d551ef2f524b48dcc78f9337fc"},{"title":"Unsupervised quality estimation for neural machine translation","url":"https://spiral.imperial.ac.uk/entities/publication/a2
…[truncated 1295 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_citation_audit_20260517T085237",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 130 · 2026-05-17T08:58:22.638690+00:00_

Web search results for query: "Müller Mathias Sennrich Rico "Understanding Properties Minimum Bayes Risk Decoding Neural Machine Translation" ACL 2021"

No links found.

The search didn't return any results for that exact query. Let me try a more focused search:

Links: [{"title":"Understanding the Properties of Minimum Bayes Risk Decoding in Neural Machine Translation - ACL Anthology","url":"https://aclanthology.org/2021.acl-long.22/"},{"title":"Understanding the Properties of Minimum Bayes Risk Decoding in Neural Machine Translation - ADS","url":"https://ui.adsabs.harvard.edu/abs/2021arXiv210508504M/abstract"},{"title":"[2105.08504] Understanding the Properties of Minimum Bayes Risk Decoding in Neural Machine Translation","url":"https://arxiv.org/abs/2105.08504"},{"title":"High Quality Rather than High Model Probability: Minimum Bayes Risk Decoding with Neural Metrics | Transactions of the Association for Computational Linguistics | MIT Press","url":"https://direct.mit.edu/tacl/article/doi/10.1162/tacl_a_00491/112497/High-Quality-Rather-than-High-Model-Probability"},{"title":"Understanding the Properties of Minimum Bayes Risk Decoding in Neural Machine Translation | DeepAI","url":"https://deepai.org/publication/understanding-the-properties-of-minimum-bayes-risk-decoding-in-neural-machine-translation"},{"title":"(PDF) Understanding the Properties of Minimum Bayes Risk Decoding in Neural Machine Translation","url":"https://www.researchgate.net/publication/351686312_Understanding_the_Properties_of_Minimum_Bayes_Risk_Decoding_in_Neural_Machine_Translation"},{"title":"Understanding the Properties of Minimum Bayes Risk Decoding in Neural Machine Translation | Underline","url":"https://underline.io/lecture/25373-understanding-the-properties-of-minimum-bayes-risk-decoding-in-neural-machine-translation"},{"title":"[PDF] Understanding the Properties of Minimum Bayes Risk Decoding in Neural Machine Translation | Semantic Scholar","url":"https://www.semanticscholar.org/paper/
…[truncated 1974 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_citation_audit_20260517T085237",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool call

_source line 131 · 2026-05-17T08:58:22.638858+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Fleiss Joseph \"Measuring nominal scale agreement among many raters\" Psychological Bulletin 1971"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_citation_audit_20260517T085237",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Fleiss Joseph \"Measuring nominal scale agreement among many raters\" Psychological Bulletin 1971"
  }
}
```

</details>

---

### Tool call

_source line 132 · 2026-05-17T08:58:22.638984+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Ratinov Lev Roth Dan \"Design Challenges Misconceptions Named Entity Recognition\" CoNLL 2009"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_citation_audit_20260517T085237",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Ratinov Lev Roth Dan \"Design Challenges Misconceptions Named Entity Recognition\" CoNLL 2009"
  }
}
```

</details>

---

### Tool call

_source line 133 · 2026-05-17T08:58:22.639142+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Mejer Avihai Crammer Koby \"Confidence Structured-Prediction Confidence-Weighted Models\" EMNLP 2010"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_citation_audit_20260517T085237",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Mejer Avihai Crammer Koby \"Confidence Structured-Prediction Confidence-Weighted Models\" EMNLP 2010"
  }
}
```

</details>

---

### Tool call

_source line 134 · 2026-05-17T08:58:22.639290+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Kuleshov Volodymyr Liang Percy \"Calibrated Structured Prediction\" NeurIPS 2015"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_citation_audit_20260517T085237",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Kuleshov Volodymyr Liang Percy \"Calibrated Structured Prediction\" NeurIPS 2015"
  }
}
```

</details>

---

### Tool call

_source line 135 · 2026-05-17T08:58:22.639412+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Sang \"Erik Tjong Kim\" Meulder \"Introduction CoNLL-2003 Shared Task Language-Independent Named Entity Recognition\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_citation_audit_20260517T085237",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Sang \"Erik Tjong Kim\" Meulder \"Introduction CoNLL-2003 Shared Task Language-Independent Named Entity Recognition\""
  }
}
```

</details>

---

### Tool result

_source line 136 · 2026-05-17T08:58:22.639553+00:00_

Web search results for query: "Fleiss Joseph "Measuring nominal scale agreement among many raters" Psychological Bulletin 1971"

Links: [{"title":"Measuring nominal scale agreement among many raters.","url":"https://psycnet.apa.org/record/1972-05083-001"},{"title":"Measuring nominal scale agreement among many raters","url":"https://www.proquest.com/docview/614289059"},{"title":"Measuring nominal scale agreement among many raters. | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Measuring-nominal-scale-agreement-among-many-Fleiss/cfb4592221080deb127de94e8063fb403b13a298"},{"title":"Fleiss, J.L. (1971) Measuring nominal scale agreement among many raters. Psychological Bulletin, 76, 378-382. doi10.1037/h0031619 - References - Scientific Research Publishing","url":"https://www.scirp.org/reference/referencespapers?referenceid=853322"},{"title":"Fleiss, J. L. (1971). Measuring Nominal Scale Agreement among Many Raters. Psychological Bulletin, 76, 378-382. - References - Scientific Research Publishing","url":"https://www.scirp.org/reference/referencespapers?referenceid=1733370"},{"title":"Measuring nominal scale agreement among many raters | BibSonomy","url":"https://www.bibsonomy.org/bibtex/2506a1115df044659165a488a75f9e449/folke"},{"title":"Measuring nominal scale agreement among many raters.","url":"https://europepmc.org/article/CTX/c6682"},{"title":"Measuring nominal scale agreement among many raters","url":"https://www.researchgate.net/publication/200086110_Measuring_nominal_scale_agreement_among_many_raters"},{"title":"Measuring nominal scale agreement among many raters - ProQuest","url":"https://www.proquest.com/openview/1b921ca73fe636a0b63739855763165d/1?pq-origsite=gscholar&cbl=60977"},{"title":"RIR002_Measuring nominal scale agreement among many raters","url":"https://www.scribd.com/document/801290776/RIR002-Measuring-nominal-scale-agreement-among-many-raters"}]

Based on the search results, I found the publication you're looking for:

Fleiss, J.L
…[truncated 722 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_citation_audit_20260517T085237",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 137 · 2026-05-17T08:58:22.639702+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Berg-Kirkpatrick Taylor Burkett Klein \"Empirical Investigation Statistical Significance NLP\" EMNLP 2012"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_citation_audit_20260517T085237",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Berg-Kirkpatrick Taylor Burkett Klein \"Empirical Investigation Statistical Significance NLP\" EMNLP 2012"
  }
}
```

</details>

---

### Tool result

_source line 138 · 2026-05-17T08:58:22.639858+00:00_

Web search results for query: "Ratinov Lev Roth Dan "Design Challenges Misconceptions Named Entity Recognition" CoNLL 2009"

Links: [{"title":"Design Challenges and Misconceptions in Named Entity Recognition - ACL Anthology","url":"https://aclanthology.org/W09-1119/"},{"title":"Design challenges and misconceptions in named entity recognition - Illinois Experts","url":"https://experts.illinois.edu/en/publications/design-challenges-and-misconceptions-in-named-entity-recognition/"},{"title":"Ratinov and Roth (2009) Design Challenges and Misconceptions in Named Entity Recognition | LingPipe Blog","url":"https://lingpipe-blog.com/2009/07/09/ratinov-and-roth-2009-design-challenges-and-misconceptions-in-named-entity-recognition/"},{"title":"[PDF] Design Challenges and Misconceptions in Named Entity Recognition | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Design-Challenges-and-Misconceptions-in-Named-Ratinov-Roth/aa9efc8b2737eac0675ba5abb5feab8305482c12"},{"title":"Design challenges and misconceptions in named entity recognition | BibSonomy","url":"https://www.bibsonomy.org/bibtex/2678a4431bc27f26d7bd8e3a1da9b2b95/jil"},{"title":"CoNLL ’09 Design Challenges and Misconceptions in Named Entity Recognition | Request PDF","url":"https://www.researchgate.net/publication/233530330_CoNLL_'09_Design_Challenges_and_Misconceptions_in_Named_Entity_Recognition"},{"title":"Google Scholar","url":"https://scholar.google.com/scholar?q=Ratinov%2C+L.%2C+Roth%2C+D.%3A+Design+challenges+and+misconceptions+in+named+entity+recognition.+In%3A+CoNLL%2C+pp.+147%E2%80%93155+%282009%29"},{"title":"CoNLL ’09 Design Challenges and Misconceptions in Named Entity Recognition∗† ‡","url":"https://cogcomp.seas.upenn.edu/papers/RatinovRo09.pdf"},{"title":"2009 DesignChallengesandMisconceptio - GM-RKB","url":"http://www.gabormelli.com/RKB/2009_DesignChallengesandMisconceptio"},{"title":"Table 6 from Design Challenges and Misconceptions in Named Entity Recognition | Semantic Scholar","url":
…[truncated 1144 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_citation_audit_20260517T085237",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 139 · 2026-05-17T08:58:22.640026+00:00_

Web search results for query: "Mejer Avihai Crammer Koby "Confidence Structured-Prediction Confidence-Weighted Models" EMNLP 2010"

Links: [{"title":"Confidence in Structured-Prediction Using Confidence-Weighted Models - ACL Anthology","url":"https://aclanthology.org/D10-1095/"},{"title":"Confidence in Structured-Prediction Using ...","url":"https://aclanthology.org/D10-1095.pdf"},{"title":"[1111.1386] Confidence Estimation in Structured Prediction","url":"https://arxiv.org/abs/1111.1386"},{"title":"dblp: Avihai Mejer","url":"https://dblp.org/pid/81/9012.html"},{"title":"Avihai Mejer - ACL Anthology","url":"https://www.aclweb.org/anthology/people/a/avihai-mejer/"},{"title":"Koby Crammer - ACL Anthology","url":"https://aclanthology.org/people/koby-crammer/"},{"title":"Are You Sure? Confidence in Prediction of Dependency Tree Edges - ACL Anthology","url":"https://aclanthology.org/N12-1068/"},{"title":"Multi-Class Conﬁdence Weighted Algorithms Koby Crammer∗ ∗Department of Computer","url":"https://www.alexkulesza.com/pubs/mccw_emnlp09.pdf"},{"title":"dblp: Koby Crammer","url":"https://dblp.org/pers/c/Crammer:Koby"},{"title":"(PDF) Are you sure?: confidence in prediction of dependency tree edges","url":"https://www.researchgate.net/publication/262289036_Are_you_sure_confidence_in_prediction_of_dependency_tree_edges"}]

I found the paper you were searching for! Here are the search results:

**"Confidence in Structured-Prediction Using Confidence-Weighted Models"** by Avihai Mejer and Koby Crammer, published in Proceedings of the 2010 Conference on Empirical Methods in Natural Language Processing, pages 971–981, Cambridge, MA.

The paper is available through the ACL Anthology at: https://aclanthology.org/D10-1095/

The paper extends Confidence-Weighted linear classifiers for sequence learning and shows that it achieves state-of-the-art performance on noun phrase chunking and named entity recognition tasks. The authors derive algorithmic approaches to estimate the predictio
…[truncated 156 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_citation_audit_20260517T085237",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 140 · 2026-05-17T08:58:22.640223+00:00_

Web search results for query: "Sang "Erik Tjong Kim" Meulder "Introduction CoNLL-2003 Shared Task Language-Independent Named Entity Recognition""

Links: [{"title":"[cs/0306050] Introduction to the CoNLL-2003 Shared Task: Language-Independent Named Entity Recognition","url":"https://arxiv.org/abs/cs/0306050"},{"title":"Introduction to the CoNLL-2003 Shared Task: Language-Independent Named Entity Recognition - ACL Anthology","url":"https://aclanthology.org/W03-0419/"},{"title":"Introduction to the CoNLL-2003 Shared Task: Language-Independent Named Entity Recognition - ADS","url":"https://ui.adsabs.harvard.edu/abs/2003cs........6050S/abstract"},{"title":"Introduction to the CoNLL-2003 Shared Task: Language-Independent Named Entity Recognition - Tilburg University Research Portal","url":"https://research.tilburguniversity.edu/en/publications/introduction-to-the-conll-2003-shared-task-language-independent-n/"},{"title":"2003 IntroductionToTheCoNLL2003SharedTask - GM-RKB","url":"https://www.gabormelli.com/RKB/2003_IntroductionToTheCoNLL2003SharedTask"},{"title":"[PDF] Introduction to the CoNLL-2003 Shared Task: Language-Independent Named Entity Recognition | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Introduction-to-the-CoNLL-2003-Shared-Task:-Named-Sang-Meulder/10f97f1fb4f5c2c8e6c44d4a33da46d331dd4aeb"},{"title":"dblp: Introduction to the CoNLL-2003 Shared Task: Language-Independent Named Entity Recognition","url":"https://dblp.org/rec/journals/corr/cs-CL-0306050.html"},{"title":"Introduction to the CoNLL-2003 Shared Task: Language-Independent Named Entity Recognition","url":"https://www.researchgate.net/publication/1956514_Introduction_to_the_CoNLL-2003_Shared_Task_Language-Independent_Named_Entity_Recognition"},{"title":"Introduction to the CoNLL-2003 Shared Task: Language-Independent Named Entity Recognition | BibSonomy","url":"https://www.bibsonomy.org/bibtex/2dd04b198987c07e41355e4a17fd1493d/hkorte"},{"title":"[cs/0306050v1] Introduction to the 
…[truncated 943 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_citation_audit_20260517T085237",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 141 · 2026-05-17T08:58:22.640407+00:00_

Web search results for query: "Kuleshov Volodymyr Liang Percy "Calibrated Structured Prediction" NeurIPS 2015"

Links: [{"title":"Calibrated Structured Prediction","url":"https://proceedings.neurips.cc/paper/2015/hash/52d2752b150f9c35ccb6869cbf074e48-Abstract.html"},{"title":"Calibrated structured prediction | Proceedings of the 29th International Conference on Neural Information Processing Systems - Volume 2","url":"https://dl.acm.org/citation.cfm?id=2969627"},{"title":"Calibrated Structured Prediction Volodymyr Kuleshov, Percy Liang","url":"https://ai.stanford.edu/~kuleshov/papers/nips2015-poster.pdf"},{"title":"Calibrated Structured Prediction Volodymyr Kuleshov","url":"https://cs.stanford.edu/~pliang/papers/calibration-nips2015.pdf"},{"title":"[PDF] Calibrated Structured Prediction | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Calibrated-Structured-Prediction-Kuleshov-Liang/a068b2dc837ed925a6f4724467572c05cbeb5f98"},{"title":"Volodymyr Kuleshov - Stanford AI Lab","url":"https://ai.stanford.edu/~kuleshov/"},{"title":"Volodymyr Kuleshov - Cornell: Computer Science","url":"https://www.cs.cornell.edu/~kuleshov/"},{"title":"NIPS 2015","url":"https://nips.cc/Conferences/2015/ScheduleMultitrack?event=5779"},{"title":"Volodymyr Kuleshov | Papers With Code","url":"https://paperswithcode.com/search?q=author:Volodymyr+Kuleshov&order=asc&order_by=stars"},{"title":"Calibrated Structured Prediction","url":"https://www.cs.cornell.edu/~kuleshov/papers/nips2015.pdf"}]

I found the paper you were looking for! Here are the key details:

**Paper:** "Calibrated Structured Prediction" by Volodymyr Kuleshov and Percy Liang

**Conference:** Published at NIPS'15 (the 29th International Conference on Neural Information Processing Systems)

**Main Focus:** In user-facing applications, displaying calibrated confidence measures—probabilities that correspond to true frequency—can be as important as obtaining high accuracy. The work addresses calibration for structured pred
…[truncated 779 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_citation_audit_20260517T085237",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 142 · 2026-05-17T08:58:22.640583+00:00_

Web search results for query: "Berg-Kirkpatrick Taylor Burkett Klein "Empirical Investigation Statistical Significance NLP" EMNLP 2012"

Links: [{"title":"An Empirical Investigation of Statistical Significance in NLP - ACL Anthology","url":"https://aclanthology.org/D12-1091/"},{"title":"An Empirical Investigation of Statistical Significance in NLP","url":"http://nlp.cs.berkeley.edu/pubs/BergKirkpatrick-Burkett-Klein_2012_Significance_paper.pdf"},{"title":"An empirical investigation of statistical significance in NLP | Proceedings of the 2012 Joint Conference on Empirical Methods in Natural Language Processing and Computational Natural Language Learning","url":"https://dl.acm.org/doi/10.5555/2390948.2391058"},{"title":"[PDF] An Empirical Investigation of Statistical Significance in NLP | Semantic Scholar","url":"https://www.semanticscholar.org/paper/An-Empirical-Investigation-of-Statistical-in-NLP-Berg-Kirkpatrick-Burkett/645c9d018d6379a4c2eed5ab2f62aeb5629544ce"},{"title":"Dblp","url":"https://dblp.org/rec/conf/emnlp/Berg-KirkpatrickBK12.rdf"},{"title":"Figure 4 from An Empirical Investigation of Statistical Significance in NLP | Semantic Scholar","url":"https://www.semanticscholar.org/paper/An-Empirical-Investigation-of-Statistical-in-NLP-Berg-Kirkpatrick-Burkett/645c9d018d6379a4c2eed5ab2f62aeb5629544ce/figure/4"},{"title":"An empirical investigation of statistical significance in NLP | Request PDF","url":"https://www.researchgate.net/publication/262168516_An_empirical_investigation_of_statistical_significance_in_NLP"},{"title":"MAWI Rec: Leveraging Severe Weather Data in Recommendation | Proceedings of the 18th ACM Conference on Recommender Systems","url":"https://dl.acm.org/doi/10.1145/3640457.3688157"},{"title":"Google Scholar","url":"https://scholar.google.com/scholar?q=Berg-Kirkpatrick,+T.,+Burkett,+D.,+Klein,+D.:+An+empirical+investigation+of+statistical+significance+in+NLP.+In:+Joint+Conference+on+Empirical+Methods+in+Natural+Language+Processing+and+Computat
…[truncated 1724 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_citation_audit_20260517T085237",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 143 · 2026-05-17T08:58:22.640803+00:00_

All 49 citations verified. Here's the audit report.

```
=== Citation Audit ===

Total citations: 49
Verified (correct): 44
Critical issues: 2
Minor metadata issues: 3
Not found / fabricated: 0
```

---

### CRITICAL ISSUES

**1. `xie2024selfevaluation` — WRONG AUTHORS + WRONG VENUE**

- **Bib authors**: Xie, Jie; Lu, Kai; Dong, Rui; Pan, Liangming; Han, Qi; Wang, Shasha; Huang, Deyu; Zhang, Junlan
- **Real authors**: Jie Ren, Yao Zhao, Tu Vu, Peter J. Liu, Balaji Lakshminarayanan
- **Bib venue**: NeurIPS 2024 (main conference)
- **Real venue**: NeurIPS 2023 Workshop ("I Can't Believe It's Not Better")
- The paper at arXiv:2312.09300 exists, title matches, but the author list is entirely fabricated. This is a hallucinated citation entry.

**2. `deguchi2024centroid` — WRONG VENUE + MISSING AUTHORS**

- **Bib venue**: "Proceedings of the 2024 Conference on Empirical Methods in Natural Language Processing (EMNLP)"
- **Real venue**: **Findings of ACL 2024** (Bangkok, pages 11009–11018)
- **Bib authors** (3): Deguchi, Kamigaito, Watanabe
- **Real authors** (6): Deguchi, Sakai, Kamigaito, Watanabe, Tanaka, Utiyama — missing 3 co-authors

---

### MINOR METADATA ISSUES

**3. `tian2023calibration`** — Title truncated (missing "Fine-Tuned with Human Feedback"), missing 3 co-authors (Allan Zhou, Archit Sharma, Rafael Rafailov). Core attribution correct.

**4. `oh2026latentsc`** — Listed as `@article` (arXiv preprint) but also published at **AAAI 2026**. Could update venue.

**5. `chen2024usc`** — Booktitle "arXiv preprint (ICML 2024 Workshop ICL)" is an unusual hybrid format.

---

### ALL OTHER 44 CITATIONS: VERIFIED

Every remaining entry was confirmed via WebSearch: paper exists, authors match, venue/year correct.

**Recommended fixes**: The two critical entries (`xie2024selfevaluation` and `deguchi2024centroid`) need immediate correction in the bib file. Want me to fix them?

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_research_citation_audit_20260517T085237"
}
```

</details>

---
