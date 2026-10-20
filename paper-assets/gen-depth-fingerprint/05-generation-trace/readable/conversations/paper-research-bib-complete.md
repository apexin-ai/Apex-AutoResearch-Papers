# paper research bib complete

**Depth Profiling: Classifying Recursive Generation Depth in Base-Model LLM Text** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 201
- **Recorded user turns:** 0
- **Tool calls:** 100
- **Original source:** `logs/chats/worker_paper_research_bib_complete_20260515T043737.jsonl`
- **Structured JSON:** [`a27ff5700332bb44919a.json`](../../sessions/a2/a27ff5700332bb44919a.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

201 recorded events

### Tool call

_source line 1 · 2026-05-15T04:42:11.254065+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/references.bib"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_research_bib_complete_20260515T043737",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/references.bib"
  }
}
```

</details>

---

### Tool result

_source line 2 · 2026-05-15T04:42:11.254624+00:00_

1	% ===== Detection =====
2	
3	@inproceedings{detectgpt,
4	  title = {{DetectGPT: Zero-Shot Machine-Generated Text Detection using Probability Curvature}},
5	  author = {Mitchell and others},
6	  booktitle = {Proceedings of the International Conference on Machine Learning},
7	  year = {2023},
8	}
9	
10	@inproceedings{gltr,
11	  title = {{GLTR: Statistical Detection and Visualization of Generated Text}},
12	  author = {Gehrmann and others},
13	  booktitle = {Proceedings of the Annual Meeting of the Association for Computational Linguistics},
14	  year = {2019},
15	}
16	
17	@inproceedings{dna_gpt,
18	  title = {{DNA-GPT: Divergent N-Gram Analysis for Training-Free Detection of GPT-Generated Text}},
19	  author = {Yang and others},
20	  booktitle = {Proceedings of the International Conference on Learning Representations},
21	  year = {2024},
22	}
23	
24	@inproceedings{binoculars,
25	  title = {{Spotting LLMs With Binoculars: Zero-Shot Detection of Machine-Generated Text}},
26	  author = {Hans and others},
27	  booktitle = {Proceedings of the International Conference on Machine Learning},
28	  year = {2024},
29	}
30	
31	@inproceedings{fast_detectgpt,
32	  title = {{Fast-DetectGPT: Efficient Zero-Shot Detection of Machine-Generated Text via Conditional Probability Curvature}},
33	  author = {Bao and others},
34	  booktitle = {Proceedings of the International Conference on Learning Representations},
35	  year = {2024},
36	}
37	
38	@article{ld_score,
39	  title = {{Beyond Perplexity: Character Distribution Signatures and the MDTA Benchmark for AI Text Detection}},
40	  author = {Narayanasamy and others},
41	  journal = {arXiv preprint arXiv:2605.01647},
42	  year = {2026},
43	}
44	
45	@inproceedings{intrinsic_dimension,
46	  title = {{Intrinsic Dimension Estimation for Robust Detection of AI-Generated Texts}},
47	  author = {Tulchinskii and others},
48	  booktitle = {Advances in Neural Information Processing Systems},
49	  year = {2023},
50	}
51	
52	@article{diveye,
53	  t
…[truncated 8471 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_research_bib_complete_20260515T043737",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-15T04:42:11.254992+00:00_

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
  "session": "worker_paper_research_bib_complete_20260515T043737",
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

_source line 4 · 2026-05-15T04:42:11.255190+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_research_bib_complete_20260515T043737",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-15T04:42:11.255454+00:00_

called Agent

<details open><summary>🔧 Tool call — Agent</summary>

```json
{
  "description": "Search authors group 1",
  "prompt": "Search for the complete author lists of these 6 academic papers using WebSearch. For each paper, search its title and find the full list of authors. Return the results in BibTeX format: {LastName, FirstName and LastName, FirstName and ...}\n\nPapers:\n1. \"DetectGPT: Zero-Shot Machine-Generated Text Detection using Probability Curvature\" (Mitchell and others, ICML 2023)\n2. \"GLTR: Statistical Detection and Visualization of Generated Text\" (Gehrmann and others, ACL 2019)\n3. \"DNA-GPT: Divergent N-Gram Analysis for Training-Free Detection of GPT-Generated Text\" (Yang and others, ICLR 2024)\n4. \"Spotting LLMs With Binoculars: Zero-Shot Detection of Machine-Generated Text\" (Hans and others, ICML 2024)\n5. \"Fast-DetectGPT: Efficient Zero-Shot Detection of Machine-Generated Text via Conditional Probability Curvature\" (Bao and others, ICLR 2024)\n6. \"Beyond Perplexity: Character Distribution Signatures and the MDTA Benchmark for AI Text Detection\" (Narayanasamy and others, arXiv 2605.01647, 2026)\n\nFor each paper, output ONLY the BibTeX key and the complete author field. Do NOT make up author names - if you can't find the full list, say so. Be precise with first/last names and spellings.",
  "subagent_type": "general-purpose"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_research_bib_complete_20260515T043737",
  "tool": "Agent",
  "tool_args": {
    "description": "Search authors group 1",
    "prompt": "Search for the complete author lists of these 6 academic papers using WebSearch. For each paper, search its title and find the full list of authors. Return the results in BibTeX format: {LastName, FirstName and LastName, FirstName and ...}\n\nPapers:\n1. \"DetectGPT: Zero-Shot Machine-Generated Text Detection using Probability Curvature\" (Mitchell and others, ICML 2023)\n2. \"GLTR: Statistical Detection and Visualization of Generated Text\" (Gehrmann and others, ACL 2019)\n3. \"DNA-GPT: Divergent N-Gram Analysis for Training-Free Detection of GPT-Generated Text\" (Yang and others, ICLR 2024)\n4. \"Spotting LLMs With Binoculars: Zero-Shot Detection of Machine-Generated Text\" (Hans and others, ICML 2024)\n5. \"Fast-DetectGPT: Efficient Zero-Shot Detection of Machine-Generated Text via Conditional Probability Curvature\" (Bao and others, ICLR 2024)\n6. \"Beyond Perplexity: Character Distribution Signatures and the MDTA Benchmark for AI Text Detection\" (Narayanasamy and others, arXiv 2605.01647, 2026)\n\nFor each paper, output ONLY the BibTeX key and the complete author field. Do NOT make up author names - if you can't find the full list, say so. Be precise with first/last names and spellings.",
    "subagent_type": "general-purpose"
  }
}
```

</details>

---

### Tool call

_source line 6 · 2026-05-15T04:42:11.255778+00:00_

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
  "session": "worker_paper_research_bib_complete_20260515T043737",
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

_source line 7 · 2026-05-15T04:42:11.255998+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_research_bib_complete_20260515T043737",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 8 · 2026-05-15T04:42:11.256207+00:00_

called Agent

<details open><summary>🔧 Tool call — Agent</summary>

```json
{
  "description": "Search authors group 2",
  "prompt": "Search for the complete author lists of these 6 academic papers using WebSearch. For each paper, search its title and find the full list of authors. Return the results in BibTeX format: {LastName, FirstName and LastName, FirstName and ...}\n\nPapers:\n1. \"Intrinsic Dimension Estimation for Robust Detection of AI-Generated Texts\" (Tulchinskii and others, NeurIPS 2023)\n2. \"Breaking the Generator Barrier: Disentangled Representation for Generalizable AI-Text Detection\" (Pu and others, arXiv 2604.13692, 2026)\n3. \"Feature-Augmented Transformers for Robust AI-Text Detection Across Domains and Generators\" (Mady and others, arXiv 2605.03969, 2026)\n4. \"Can AI-Generated Text be Reliably Detected?\" (Sadasivan and others, ICLR 2024)\n5. \"Paraphrasing Evades Detectors of AI-Generated Text, but Retrieval is an Effective Defense\" (Krishna and others, NeurIPS 2023)\n6. \"Position: On the Possibilities of AI-Generated Text Detection\" (Chakraborty and others, ICML 2024)\n\nFor each paper, output ONLY the BibTeX key and the complete author field. Do NOT make up author names - if you can't find the full list, say so. Be precise with first/last names and spellings.",
  "subagent_type": "general-purpose"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_research_bib_complete_20260515T043737",
  "tool": "Agent",
  "tool_args": {
    "description": "Search authors group 2",
    "prompt": "Search for the complete author lists of these 6 academic papers using WebSearch. For each paper, search its title and find the full list of authors. Return the results in BibTeX format: {LastName, FirstName and LastName, FirstName and ...}\n\nPapers:\n1. \"Intrinsic Dimension Estimation for Robust Detection of AI-Generated Texts\" (Tulchinskii and others, NeurIPS 2023)\n2. \"Breaking the Generator Barrier: Disentangled Representation for Generalizable AI-Text Detection\" (Pu and others, arXiv 2604.13692, 2026)\n3. \"Feature-Augmented Transformers for Robust AI-Text Detection Across Domains and Generators\" (Mady and others, arXiv 2605.03969, 2026)\n4. \"Can AI-Generated Text be Reliably Detected?\" (Sadasivan and others, ICLR 2024)\n5. \"Paraphrasing Evades Detectors of AI-Generated Text, but Retrieval is an Effective Defense\" (Krishna and others, NeurIPS 2023)\n6. \"Position: On the Possibilities of AI-Generated Text Detection\" (Chakraborty and others, ICML 2024)\n\nFor each paper, output ONLY the BibTeX key and the complete author field. Do NOT make up author names - if you can't find the full list, say so. Be precise with first/last names and spellings.",
    "subagent_type": "general-purpose"
  }
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-15T04:42:11.256531+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "DetectGPT Zero-Shot Machine-Generated Text Detection Probability Curvature ICML 2023 authors"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_research_bib_complete_20260515T043737",
  "tool": "WebSearch",
  "tool_args": {
    "query": "DetectGPT Zero-Shot Machine-Generated Text Detection Probability Curvature ICML 2023 authors"
  }
}
```

</details>

---

### Tool call

_source line 10 · 2026-05-15T04:42:11.256763+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "GLTR Statistical Detection and Visualization of Generated Text ACL 2019 authors"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_research_bib_complete_20260515T043737",
  "tool": "WebSearch",
  "tool_args": {
    "query": "GLTR Statistical Detection and Visualization of Generated Text ACL 2019 authors"
  }
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-15T04:42:11.256971+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "DNA-GPT Divergent N-Gram Analysis Training-Free Detection GPT-Generated Text ICLR 2024 authors"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_research_bib_complete_20260515T043737",
  "tool": "WebSearch",
  "tool_args": {
    "query": "DNA-GPT Divergent N-Gram Analysis Training-Free Detection GPT-Generated Text ICLR 2024 authors"
  }
}
```

</details>

---

### Tool call

_source line 12 · 2026-05-15T04:42:11.257166+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Spotting LLMs With Binoculars Zero-Shot Detection Machine-Generated Text ICML 2024 authors"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_research_bib_complete_20260515T043737",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Spotting LLMs With Binoculars Zero-Shot Detection Machine-Generated Text ICML 2024 authors"
  }
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-15T04:42:11.257522+00:00_

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
  "session": "worker_paper_research_bib_complete_20260515T043737",
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

_source line 14 · 2026-05-15T04:42:11.257749+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_research_bib_complete_20260515T043737",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-15T04:42:11.257967+00:00_

called Agent

<details open><summary>🔧 Tool call — Agent</summary>

```json
{
  "description": "Search authors group 3",
  "prompt": "Search for the complete author lists of these 6 academic papers using WebSearch. For each paper, search its title and find the full list of authors. Return the results in BibTeX format: {LastName, FirstName and LastName, FirstName and ...}\n\nPapers:\n1. \"Defending Against Neural Fake News\" (Zellers and others, NeurIPS 2019)\n2. \"Release Strategies and the Social Impacts of Language Models\" (Solaiman and others, arXiv 1908.09203, 2019)\n3. \"Self-Consuming Generative Models Go MAD\" (Alemohammad and others, arXiv 2307.01850, 2023)\n4. \"The Curse of Recursion: Training on Generated Data Makes Models Forget\" (Shumailov and others, Nature 2024)\n5. \"Strong Model Collapse\" (Dohmatob and others, ICLR 2024)\n6. \"Is Model Collapse Inevitable? Breaking the Curse of Recursion by Accumulating Real and Synthetic Data\" (Gerstgrasser and others, arXiv 2404.01413, 2024)\n\nFor each paper, output ONLY the BibTeX key and the complete author field. Do NOT make up author names - if you can't find the full list, say so. Be precise with first/last names and spellings.",
  "subagent_type": "general-purpose"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_research_bib_complete_20260515T043737",
  "tool": "Agent",
  "tool_args": {
    "description": "Search authors group 3",
    "prompt": "Search for the complete author lists of these 6 academic papers using WebSearch. For each paper, search its title and find the full list of authors. Return the results in BibTeX format: {LastName, FirstName and LastName, FirstName and ...}\n\nPapers:\n1. \"Defending Against Neural Fake News\" (Zellers and others, NeurIPS 2019)\n2. \"Release Strategies and the Social Impacts of Language Models\" (Solaiman and others, arXiv 1908.09203, 2019)\n3. \"Self-Consuming Generative Models Go MAD\" (Alemohammad and others, arXiv 2307.01850, 2023)\n4. \"The Curse of Recursion: Training on Generated Data Makes Models Forget\" (Shumailov and others, Nature 2024)\n5. \"Strong Model Collapse\" (Dohmatob and others, ICLR 2024)\n6. \"Is Model Collapse Inevitable? Breaking the Curse of Recursion by Accumulating Real and Synthetic Data\" (Gerstgrasser and others, arXiv 2404.01413, 2024)\n\nFor each paper, output ONLY the BibTeX key and the complete author field. Do NOT make up author names - if you can't find the full list, say so. Be precise with first/last names and spellings.",
    "subagent_type": "general-purpose"
  }
}
```

</details>

---

### Tool call

_source line 16 · 2026-05-15T04:42:11.258322+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Fast-DetectGPT Efficient Zero-Shot Detection Machine-Generated Text Conditional Probability Curvature ICLR 2024 authors"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_research_bib_complete_20260515T043737",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Fast-DetectGPT Efficient Zero-Shot Detection Machine-Generated Text Conditional Probability Curvature ICLR 2024 authors"
  }
}
```

</details>

---

### Tool result

_source line 17 · 2026-05-15T04:42:11.258544+00:00_

Web search results for query: "DetectGPT Zero-Shot Machine-Generated Text Detection Probability Curvature ICML 2023 authors"

Links: [{"title":"[2301.11305] DetectGPT: Zero-Shot Machine-Generated Text Detection using Probability Curvature","url":"https://arxiv.org/abs/2301.11305"},{"title":"GitHub - eric-mitchell/detect-gpt: DetectGPT: Zero-Shot Machine-Generated Text Detection using Probability Curvature · GitHub","url":"https://github.com/eric-mitchell/detect-gpt"},{"title":"DetectGPT: Zero-Shot Machine-Generated Text Detection ...","url":"https://openreview.net/pdf?id=UiAyIILXRd"},{"title":"[Paper Note] DetectGPT: Zero-Shot Machine-Generated Text Detection using Probability Curvature, Eric Mitchell+, ICML'23, 2023.01 · Issue #3698 · AkihikoWatanabe/paper_notes","url":"https://github.com/AkihikoWatanabe/paper_notes/issues/3698"},{"title":"dblp: DetectGPT: Zero-Shot Machine-Generated Text Detection using Probability Curvature.","url":"https://dblp.org/rec/conf/icml/Mitchell0KMF23.html"},{"title":"(PDF) DetectGPT: Zero-Shot Machine-Generated Text Detection using Probability Curvature","url":"https://www.researchgate.net/publication/367461943_DetectGPT_Zero-Shot_Machine-Generated_Text_Detection_using_Probability_Curvature"},{"title":"DetectGPT: zero-shot machine-generated text detection ...","url":"https://dl.acm.org/doi/10.5555/3618408.3619446"},{"title":"DetectGPT: Zero-Shot Machine-Generated Text Detection using Probability Curvature","url":"https://proceedings.mlr.press/v202/mitchell23a.html"},{"title":"Eric Mitchell, Yoonho Lee, Alexander Khazatsky, Christopher D. Manning, Chelsea Finn · DetectGPT: Zero-Shot Machine-Generated Text Detection using Probability Curvature","url":"https://slideslive.com/39004346/detectgpt-zeroshot-machinegenerated-text-detection-using-probability-curvature"},{"title":"Brief Review — DetectGPT: Zero-Shot Machine-Generated Text Detection using Probability Curvature | by Sik-Ho Tsang | Medium","url":"https://sh-tsang.medium.com/brief-re
…[truncated 927 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_research_bib_complete_20260515T043737",
  "tool": "WebSearch",
  "elapsed_ms": 2
}
```

</details>

---

### Tool call

_source line 18 · 2026-05-15T04:42:11.258834+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "arXiv 2605.01647 \"Beyond Perplexity\" Character Distribution Signatures MDTA Benchmark AI Text Detection authors"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_research_bib_complete_20260515T043737",
  "tool": "WebSearch",
  "tool_args": {
    "query": "arXiv 2605.01647 \"Beyond Perplexity\" Character Distribution Signatures MDTA Benchmark AI Text Detection authors"
  }
}
```

</details>

---

### Tool result

_source line 19 · 2026-05-15T04:42:11.259069+00:00_

Web search results for query: "Spotting LLMs With Binoculars Zero-Shot Detection Machine-Generated Text ICML 2024 authors"

Links: [{"title":"[2401.12070] Spotting LLMs With Binoculars: Zero-Shot Detection of Machine-Generated Text","url":"https://arxiv.org/abs/2401.12070"},{"title":"GitHub - ahans30/Binoculars: [ICML 2024] Binoculars: Zero-Shot Detection of LLM-Generated Text · GitHub","url":"https://github.com/ahans30/Binoculars"},{"title":"Spotting LLMs with binoculars: zero-shot detection of ...","url":"https://dl.acm.org/doi/10.5555/3692070.3692768"},{"title":"Spotting LLMs With Binoculars: Zero-Shot Detection of Machine-Generated Text | OpenReview","url":"https://openreview.net/forum?id=iARAKITHTH"},{"title":"[Quick Review] Spotting LLMs With Binoculars: Zero-Shot Detection of Machine-Generated Text","url":"https://liner.com/review/spotting-llms-with-binoculars-zeroshot-detection-machinegenerated-text"},{"title":"Under review as a conference paper at ICLR 2024 SPOTTING LLMS WITH BINOCULARS:","url":"https://openreview.net/pdf?id=iARAKITHTH"},{"title":"ICML Poster Spotting LLMs With Binoculars: Zero-Shot Detection of Machine-Generated Text","url":"https://icml.cc/virtual/2024/poster/33662"},{"title":"Binoculars/README.md at main · ahans30/Binoculars","url":"https://github.com/ahans30/Binoculars/blob/main/README.md"},{"title":"Spotting LLMs With Binoculars: Zero-Shot Detection of Machine-Generated Text","url":"https://arxiv.org/html/2401.12070v3"},{"title":"Spotting LLMs With Binoculars: Zero-Shot Detection of Machine-Generated Text - Zilliz Learn","url":"https://zilliz.com/learn/spotting-llms-with-binoculars-zero-shot-detection-of-machine-generated-text"}]

Based on the search results, here are the authors of the ICML 2024 paper "Spotting LLMs With Binoculars: Zero-Shot Detection of Machine-Generated Text":

The authors are: Abhimanyu Hans, Avi Schwarzschild, Valeriia Cherepanova, Hamid Kazemi, Aniruddha Saha, Micah Goldblum, Jonas Geiping, and Tom Goldstein.



…[truncated 100 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_research_bib_complete_20260515T043737",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool call

_source line 20 · 2026-05-15T04:42:11.259322+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Intrinsic Dimension Estimation for Robust Detection of AI-Generated Texts authors NeurIPS 2023 Tulchinskii"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_research_bib_complete_20260515T043737",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Intrinsic Dimension Estimation for Robust Detection of AI-Generated Texts authors NeurIPS 2023 Tulchinskii"
  }
}
```

</details>

---

### Tool call

_source line 21 · 2026-05-15T04:42:11.259545+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Breaking the Generator Barrier Disentangled Representation Generalizable AI-Text Detection arXiv 2604.13692 authors Pu"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_research_bib_complete_20260515T043737",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Breaking the Generator Barrier Disentangled Representation Generalizable AI-Text Detection arXiv 2604.13692 authors Pu"
  }
}
```

</details>

---

### Tool call

_source line 22 · 2026-05-15T04:42:11.259776+00:00_

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
  "session": "worker_paper_research_bib_complete_20260515T043737",
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

_source line 23 · 2026-05-15T04:42:11.259978+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_research_bib_complete_20260515T043737",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 24 · 2026-05-15T04:42:11.260186+00:00_

called Agent

<details open><summary>🔧 Tool call — Agent</summary>

```json
{
  "description": "Search authors group 4",
  "prompt": "Search for the complete author lists of these 6 academic papers using WebSearch. For each paper, search its title and find the full list of authors. Return the results in BibTeX format: {LastName, FirstName and LastName, FirstName and ...}\n\nPapers:\n1. \"Data Selection for Language Models via Importance Resampling\" (Xie and others, NeurIPS 2023)\n2. \"QuRating: Selecting High-Quality Data for Training Language Models\" (Wettig and others, ICML 2024)\n3. \"CCNet: Extracting High Quality Monolingual Datasets from Web Crawl Data\" (Wenzek and others, LREC 2020)\n4. \"A Watermark for Large Language Models\" (Kirchenbauer and others, ICML 2023)\n5. \"Scalable Watermarking for Identifying Large Language Model Outputs\" (Dathathri and others, Nature 2024)\n6. \"Chainwash: Multi-Step Rewriting Attacks on Diffusion Language Model Watermarks\" (Ameen and others, arXiv 2605.05503, 2026)\n\nFor each paper, output ONLY the BibTeX key and the complete author field. Do NOT make up author names - if you can't find the full list, say so. Be precise with first/last names and spellings.",
  "subagent_type": "general-purpose"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_research_bib_complete_20260515T043737",
  "tool": "Agent",
  "tool_args": {
    "description": "Search authors group 4",
    "prompt": "Search for the complete author lists of these 6 academic papers using WebSearch. For each paper, search its title and find the full list of authors. Return the results in BibTeX format: {LastName, FirstName and LastName, FirstName and ...}\n\nPapers:\n1. \"Data Selection for Language Models via Importance Resampling\" (Xie and others, NeurIPS 2023)\n2. \"QuRating: Selecting High-Quality Data for Training Language Models\" (Wettig and others, ICML 2024)\n3. \"CCNet: Extracting High Quality Monolingual Datasets from Web Crawl Data\" (Wenzek and others, LREC 2020)\n4. \"A Watermark for Large Language Models\" (Kirchenbauer and others, ICML 2023)\n5. \"Scalable Watermarking for Identifying Large Language Model Outputs\" (Dathathri and others, Nature 2024)\n6. \"Chainwash: Multi-Step Rewriting Attacks on Diffusion Language Model Watermarks\" (Ameen and others, arXiv 2605.05503, 2026)\n\nFor each paper, output ONLY the BibTeX key and the complete author field. Do NOT make up author names - if you can't find the full list, say so. Be precise with first/last names and spellings.",
    "subagent_type": "general-purpose"
  }
}
```

</details>

---

### Tool result

_source line 25 · 2026-05-15T04:42:11.260477+00:00_

Web search results for query: "Fast-DetectGPT Efficient Zero-Shot Detection Machine-Generated Text Conditional Probability Curvature ICLR 2024 authors"

Links: [{"title":"GitHub - baoguangsheng/fast-detect-gpt: Code base for ICLR 2024 \"Fast-DetectGPT: Efficient Zero-Shot Detection of Machine-Generated Text via Conditional Probability Curvature\". · GitHub","url":"https://github.com/baoguangsheng/fast-detect-gpt"},{"title":"ICLR Poster Fast-DetectGPT: Efficient Zero-Shot Detection of Machine-Generated Text via Conditional Probability Curvature","url":"https://iclr.cc/virtual/2024/poster/19201"},{"title":"Fast-DetectGPT: Efficient Zero-Shot Detection of Machine-Generated Text via Conditional Probability Curvature | OpenReview","url":"https://openreview.net/forum?id=Bpcgcr8E8Z"},{"title":"FAST-DETECTGPT: EFFICIENT ZERO-SHOT DETEC","url":"https://proceedings.iclr.cc/paper_files/paper/2024/file/6b8c6f846c3575e1d1ad496abea28826-Paper-Conference.pdf"},{"title":"[2310.05130] Fast-DetectGPT: Efficient Zero-Shot Detection of Machine-Generated Text via Conditional Probability Curvature","url":"https://arxiv.org/abs/2310.05130"},{"title":"Fast-DetectGPT: Efficient Zero-Shot Detection of Machine-Generated Text via Conditional Probability Curvature","url":"https://proceedings.iclr.cc/paper_files/paper/2024/hash/6b8c6f846c3575e1d1ad496abea28826-Abstract-Conference.html"},{"title":"(PDF) FAST-DETECTGPT: EFFICIENT ZERO-SHOT DETEC- TION OF MACHINE-GENERATED TEXT VIA CONDI- TIONAL PROBABILITY CURVATURE","url":"https://www.researchgate.net/publication/388188914_FAST-DETECTGPT_EFFICIENT_ZERO-SHOT_DETEC-_TION_OF_MACHINE-GENERATED_TEXT_VIA_CONDI-_TIONAL_PROBABILITY_CURVATURE"},{"title":"Fast-DetectGPT: Efficient Zero-Shot Detection of Machine-Generated Text via Conditional Probability Curvature","url":"https://arxiv.org/html/2310.05130v3"},{"title":"[2301.11305] DetectGPT: Zero-Shot Machine-Generated Text Detection using Probability Curvature","url":"https://arxiv.org/abs/2301.11305"},{"
…[truncated 733 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_research_bib_complete_20260515T043737",
  "tool": "WebSearch",
  "elapsed_ms": 2
}
```

</details>

---

### Tool call

_source line 26 · 2026-05-15T04:42:11.260734+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Feature-Augmented Transformers Robust AI-Text Detection Across Domains Generators arXiv 2605.03969 authors Mady"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_research_bib_complete_20260515T043737",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Feature-Augmented Transformers Robust AI-Text Detection Across Domains Generators arXiv 2605.03969 authors Mady"
  }
}
```

</details>

---

### Tool result

_source line 27 · 2026-05-15T04:42:11.261040+00:00_

Web search results for query: "GLTR Statistical Detection and Visualization of Generated Text ACL 2019 authors"

Links: [{"title":"GLTR: Statistical Detection and Visualization of Generated Text - ACL Anthology","url":"https://aclanthology.org/P19-3019/"},{"title":"[1906.04043] GLTR: Statistical Detection and Visualization of Generated Text","url":"https://arxiv.org/abs/1906.04043"},{"title":"GLTR: Statistical detection and visualization of generated text for ACL 2019 - IBM Research","url":"https://research.ibm.com/publications/gltr-statistical-detection-and-visualization-of-generated-text"},{"title":"GLTR from MIT-IBM Watson AI Lab and HarvardNLP","url":"http://gltr.io/"},{"title":"[PDF] GLTR: Statistical Detection and Visualization of Generated Text | Semantic Scholar","url":"https://www.semanticscholar.org/paper/GLTR:-Statistical-Detection-and-Visualization-of-Gehrmann-Strobelt/867db5097ad6aaef098c60b0845785b440eca49a"},{"title":"GLTR: Statistical Detection and Visualization of Generated Text","url":"https://scholar.harvard.edu/files/gehrmann/files/acl_demo_2019_gltr_statistical_detection_of_fake_text_5.pdf"},{"title":"GLTR: Statistical Detection and Visualization of Generated Text | Sebastian Gehrmann","url":"https://scholar.harvard.edu/gehrmann/publications/gltr-statistical-detection-and-visualization-generated-text"},{"title":"GLTR: Statistical Detection and Visualization of Generated Text | Request PDF","url":"https://www.researchgate.net/publication/335781128_GLTR_Statistical_Detection_and_Visualization_of_Generated_Text"},{"title":"GLTR: Statistical Detection and Visualization of Generated ...","url":"https://par.nsf.gov/servlets/purl/10393945"},{"title":"[1906.04043v1] GLTR: Statistical Detection and Visualization of Generated Text","url":"https://arxiv.org/abs/1906.04043v1"}]

Based on the search results, the authors of "GLTR: Statistical Detection and Visualization of Generated Text" (ACL 2019) are Sebastian Gehrmann, Hendrik Strobelt, and Alexander Rush
…[truncated 104 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_research_bib_complete_20260515T043737",
  "tool": "WebSearch",
  "elapsed_ms": 4
}
```

</details>

---

### Tool result

_source line 28 · 2026-05-15T04:42:11.261299+00:00_

Web search results for query: "arXiv 2605.01647 "Beyond Perplexity" Character Distribution Signatures MDTA Benchmark AI Text Detection authors"

Links: [{"title":"[2605.01647] Beyond Perplexity: Character Distribution Signatures and the MDTA Benchmark for AI Text Detection","url":"https://arxiv.org/abs/2605.01647"},{"title":"[2605.01647v1] Beyond Perplexity: Character Distribution Signatures and the MDTA Benchmark for AI Text Detection","url":"https://arxiv.org/abs/2605.01647v1"},{"title":"Beyond Perplexity: Character Distribution Signatures and the MDTA Benchmark for AI Text Detection - ADS","url":"https://ui.adsabs.harvard.edu/abs/2026arXiv260501647N/abstract"},{"title":"Beyond Perplexity: Character Distribution Signatures and the MDTA Benchmark for AI Text Detection","url":"https://arxiv.org/html/2605.01647"},{"title":"Beyond Perplexity: A Geometric and Spectral Study of Low-Rank Pre-Training","url":"https://arxiv.org/html/2605.13652"},{"title":"[2605.13652] Beyond Perplexity: A Geometric and Spectral Study of Low-Rank Pre-Training","url":"https://arxiv.org/abs/2605.13652"},{"title":"Learning Perturbations to Extrapolate Your LLM","url":"https://arxiv.org/html/2605.13284"},{"title":"On the Hardness of Junking LLMs","url":"https://arxiv.org/html/2605.05116"},{"title":"Perplexity Cannot Always Tell Right from Wrong","url":"https://arxiv.org/html/2601.22950v1"},{"title":"Low-Perplexity LLM-Generated Sequences and Where To Find Them","url":"https://arxiv.org/html/2507.01844v1"}]

Perfect! I found the paper. Here are the key details:

## Paper Summary

**Title:** Beyond Perplexity: Character Distribution Signatures and the MDTA Benchmark for AI Text Detection

**Authors:** Priyadarshan Narayanasamy, Swastik Agrawal, Klint Faber, Fardina Fathmiul Alam

**Affiliation:** Department of Computer Science, University of Maryland, College Park

**Submission Date:** Submitted on 3 May 2026

## Key Contributions

The paper introduces an alternative detection signal based on cha
…[truncated 809 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_research_bib_complete_20260515T043737",
  "tool": "WebSearch",
  "elapsed_ms": 2
}
```

</details>

---

### Tool result

_source line 29 · 2026-05-15T04:42:11.261525+00:00_

Web search results for query: "DNA-GPT Divergent N-Gram Analysis Training-Free Detection GPT-Generated Text ICLR 2024 authors"

Links: [{"title":"[2305.17359] DNA-GPT: Divergent N-Gram Analysis for Training-Free Detection of GPT-Generated Text","url":"https://arxiv.org/abs/2305.17359"},{"title":"DNA-GPT: Divergent N-Gram Analysis for Training-Free Detection of GPT-Generated Text","url":"https://www.nec-labs.com/blog/dna-gpt-divergent-n-gram-analysis-for-training-free-detection-of-gpt-generated-text/"},{"title":"dblp: DNA-GPT: Divergent N-Gram Analysis for Training-Free Detection of GPT-Generated Text.","url":"https://dblp1.uni-trier.de/rec/conf/iclr/Yang0WPWC24.html"},{"title":"DNA-GPT: Divergent N-Gram Analysis for Training-Free ...","url":"https://arxiv.org/pdf/2305.17359"},{"title":"UC Santa Barbara UC Santa Barbara Electronic Theses and Dissertations Title","url":"https://escholarship.org/content/qt2g10w3nh/qt2g10w3nh.pdf"},{"title":"A Practical Examination of AI-Generated Text Detectors for ...","url":"https://aclanthology.org/2025.findings-naacl.271.pdf"},{"title":"[PDF] DNA-GPT: Divergent N-Gram Analysis for Training-Free Detection of GPT-Generated Text | Semantic Scholar","url":"https://www.semanticscholar.org/paper/DNA-GPT:-Divergent-N-Gram-Analysis-for-Detection-of-Yang-Cheng/08145978da4c8912f4a05444a6bbf048778dc4af"},{"title":"DNA-GPT: Divergent N-Gram Analysis for Training-Free Detection of GPT-Generated Text | OpenReview","url":"https://openreview.net/forum?id=Xlayxj2fWp"},{"title":"ICLR Poster DNA-GPT: Divergent N-Gram Analysis for Training-Free Detection of GPT-Generated Text","url":"https://iclr.cc/virtual/2024/poster/18444"},{"title":"(PDF) DNA-GPT: Divergent N-Gram Analysis for Training-Free Detection of GPT-Generated Text","url":"https://www.researchgate.net/publication/371136931_DNA-GPT_Divergent_N-Gram_Analysis_for_Training-Free_Detection_of_GPT-Generated_Text"}]

Based on the search results, here is the information about the DNA-GPT paper from 
…[truncated 937 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_research_bib_complete_20260515T043737",
  "tool": "WebSearch",
  "elapsed_ms": 4
}
```

</details>

---

### Tool call

_source line 30 · 2026-05-15T04:42:11.261772+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Can AI-Generated Text be Reliably Detected Sadasivan ICLR 2024 authors"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_research_bib_complete_20260515T043737",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Can AI-Generated Text be Reliably Detected Sadasivan ICLR 2024 authors"
  }
}
```

</details>

---

### Tool call

_source line 31 · 2026-05-15T04:42:11.261969+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Paraphrasing Evades Detectors AI-Generated Text Retrieval Effective Defense Krishna NeurIPS 2023 authors"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_research_bib_complete_20260515T043737",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Paraphrasing Evades Detectors AI-Generated Text Retrieval Effective Defense Krishna NeurIPS 2023 authors"
  }
}
```

</details>

---

### Tool call

_source line 32 · 2026-05-15T04:42:11.262158+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Position On the Possibilities of AI-Generated Text Detection Chakraborty ICML 2024 authors"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_research_bib_complete_20260515T043737",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Position On the Possibilities of AI-Generated Text Detection Chakraborty ICML 2024 authors"
  }
}
```

</details>

---

### Tool result

_source line 33 · 2026-05-15T04:42:11.262368+00:00_

Web search results for query: "Intrinsic Dimension Estimation for Robust Detection of AI-Generated Texts authors NeurIPS 2023 Tulchinskii"

Links: [{"title":"NeurIPS Poster Intrinsic Dimension Estimation for Robust Detection of AI-Generated Texts","url":"https://neurips.cc/virtual/2023/poster/72624"},{"title":"Intrinsic Dimension Estimation for Robust Detection of AI-Generated Texts","url":"https://proceedings.neurips.cc/paper_files/paper/2023/hash/7baa48bc166aa2013d78cbdc15010530-Abstract-Conference.html"},{"title":"[2306.04723] Intrinsic Dimension Estimation for Robust Detection of AI-Generated Texts","url":"https://arxiv.org/abs/2306.04723"},{"title":"Intrinsic Dimension Estimation for Robust Detection of AI-Generated Texts | OpenReview","url":"https://openreview.net/forum?id=8uOZ0kNji6"},{"title":"Intrinsic dimension estimation for robust detection of AI-generated texts | Proceedings of the 37th International Conference on Neural Information Processing Systems","url":"https://dl.acm.org/doi/10.5555/3666122.3667828"},{"title":"[PDF] Intrinsic Dimension Estimation for Robust Detection of AI-Generated Texts | Semantic Scholar","url":"https://www.semanticscholar.org/paper/a5fab19553e623e8787383cb3da76b8a3c42a8f4"},{"title":"Intrinsic Dimension Estimation for Robust Detection of AI-Generated Texts","url":"https://openreview.net/pdf?id=8uOZ0kNji6"},{"title":"Intrinsic Dimension Estimation for Robust Detection of AI- ...","url":"https://papers.neurips.cc/paper_files/paper/2023/file/7baa48bc166aa2013d78cbdc15010530-Paper-Conference.pdf"},{"title":"Intrinsic Dimension Estimation for Robust Detection of AI- ...","url":"https://arxiv.org/pdf/2306.04723"},{"title":"[Quick Review] Intrinsic Dimension Estimation for Robust Detection of AI-Generated Texts","url":"https://liner.com/review/intrinsic-dimension-estimation-for-robust-detection-of-aigenerated-texts"}]

I found the paper! Here are the search results for "Intrinsic Dimension Estimation for Robust Detection of AI-Gener
…[truncated 1281 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_research_bib_complete_20260515T043737",
  "tool": "WebSearch",
  "elapsed_ms": 3
}
```

</details>

---

### Tool call

_source line 34 · 2026-05-15T04:42:11.262631+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Defending Against Neural Fake News Zellers NeurIPS 2019 full author list"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_research_bib_complete_20260515T043737",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Defending Against Neural Fake News Zellers NeurIPS 2019 full author list"
  }
}
```

</details>

---

### Tool call

_source line 35 · 2026-05-15T04:42:11.262858+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Release Strategies and the Social Impacts of Language Models arXiv 1908.09203 authors"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_research_bib_complete_20260515T043737",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Release Strategies and the Social Impacts of Language Models arXiv 1908.09203 authors"
  }
}
```

</details>

---

### Tool call

_source line 36 · 2026-05-15T04:42:11.263054+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Self-Consuming Generative Models Go MAD arXiv 2307.01850 authors"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_research_bib_complete_20260515T043737",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Self-Consuming Generative Models Go MAD arXiv 2307.01850 authors"
  }
}
```

</details>

---

### Tool result

_source line 37 · 2026-05-15T04:42:11.263260+00:00_

Web search results for query: "Defending Against Neural Fake News Zellers NeurIPS 2019 full author list"

Links: [{"title":"Grover - Defending Against Neural Fake News","url":"https://rowanzellers.com/grover/"},{"title":"Defending against neural fake news | Proceedings of the 33rd International Conference on Neural Information Processing Systems","url":"https://dl.acm.org/doi/10.5555/3454287.3455099"},{"title":"[1905.12616] Defending Against Neural Fake News","url":"https://arxiv.org/abs/1905.12616"},{"title":"Defending Against Neural Fake News | NSF Public Access Repository","url":"https://par.nsf.gov/biblio/10107992-defending-against-neural-fake-news"},{"title":"[PDF] Defending Against Neural Fake News | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Defending-Against-Neural-Fake-News-Zellers-Holtzman/ad7129af0644dbcafa9aa2f111cb76526ea444a1"},{"title":"Defending Against Neural Fake News - researchr publication","url":"https://researchr.org/publication/ZellersHRBFRC19"},{"title":"Defending Against Neural Fake News","url":"https://papers.neurips.cc/paper_files/paper/2019/file/3e9f0fc9b2f89e043bc6233994dfcf76-Paper.pdf"},{"title":"dblp: Defending Against Neural Fake News.","url":"https://dblp.org/rec/conf/nips/ZellersHRBFRC19.html"},{"title":"Reviews: Defending Against Neural Fake News","url":"https://proceedings.neurips.cc/paper/2019/file/3e9f0fc9b2f89e043bc6233994dfcf76-Reviews.html"},{"title":"GitHub - rowanz/grover: Code for Defending Against Neural Fake News, https://rowanzellers.com/grover/ · GitHub","url":"https://github.com/rowanz/grover"}]

Based on the search results, the full author list for "Defending Against Neural Fake News" from NeurIPS 2019 is: Rowan Zellers, Ari Holtzman, Hannah Rashkin, Yonatan Bisk, Ali Farhadi, Franziska Roesner, and Yejin Choi.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_research_bib_complete_20260515T043737",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 38 · 2026-05-15T04:42:11.263470+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "The Curse of Recursion Training on Generated Data Makes Models Forget Shumailov Nature 2024 authors"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_research_bib_complete_20260515T043737",
  "tool": "WebSearch",
  "tool_args": {
    "query": "The Curse of Recursion Training on Generated Data Makes Models Forget Shumailov Nature 2024 authors"
  }
}
```

</details>

---

### Tool call

_source line 39 · 2026-05-15T04:42:11.263706+00:00_

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
  "session": "worker_paper_research_bib_complete_20260515T043737",
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

_source line 40 · 2026-05-15T04:42:11.263910+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_research_bib_complete_20260515T043737",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 41 · 2026-05-15T04:42:11.264103+00:00_

called Agent

<details open><summary>🔧 Tool call — Agent</summary>

```json
{
  "description": "Search authors group 5",
  "prompt": "Search for the complete author lists of these 6 academic papers using WebSearch. For each paper, search its title and find the full list of authors. Return the results in BibTeX format: {LastName, FirstName and LastName, FirstName and ...}\n\nPapers:\n1. \"The Curious Decline of Linguistic Diversity: Training Language Models on Synthetic Text\" (Guo and others, NAACL 2024)\n2. \"The Curious Case of Neural Text Degeneration\" (Holtzman and others, ICLR 2020)\n3. \"Mapping the Increasing Use of LLMs in Scientific Papers\" (Liang and others, arXiv 2404.01268, 2024)\n4. \"Monitoring AI-Modified Content at Scale: A Case Study on the Impact of ChatGPT on AI Conference Peer Reviews\" (Liang and others, ICML 2024)\n5. \"Computational Methods in Authorship Attribution\" (Koppel and others, JASIST 2009)\n6. \"Authorship Attribution for Neural Text Generation\" (Uchendu and others, EMNLP 2020)\n\nFor each paper, output ONLY the BibTeX key and the complete author field. Do NOT make up author names - if you can't find the full list, say so. Be precise with first/last names and spellings.",
  "subagent_type": "general-purpose"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_research_bib_complete_20260515T043737",
  "tool": "Agent",
  "tool_args": {
    "description": "Search authors group 5",
    "prompt": "Search for the complete author lists of these 6 academic papers using WebSearch. For each paper, search its title and find the full list of authors. Return the results in BibTeX format: {LastName, FirstName and LastName, FirstName and ...}\n\nPapers:\n1. \"The Curious Decline of Linguistic Diversity: Training Language Models on Synthetic Text\" (Guo and others, NAACL 2024)\n2. \"The Curious Case of Neural Text Degeneration\" (Holtzman and others, ICLR 2020)\n3. \"Mapping the Increasing Use of LLMs in Scientific Papers\" (Liang and others, arXiv 2404.01268, 2024)\n4. \"Monitoring AI-Modified Content at Scale: A Case Study on the Impact of ChatGPT on AI Conference Peer Reviews\" (Liang and others, ICML 2024)\n5. \"Computational Methods in Authorship Attribution\" (Koppel and others, JASIST 2009)\n6. \"Authorship Attribution for Neural Text Generation\" (Uchendu and others, EMNLP 2020)\n\nFor each paper, output ONLY the BibTeX key and the complete author field. Do NOT make up author names - if you can't find the full list, say so. Be precise with first/last names and spellings.",
    "subagent_type": "general-purpose"
  }
}
```

</details>

---

### Tool result

_source line 42 · 2026-05-15T04:42:11.264423+00:00_

Web search results for query: "Breaking the Generator Barrier Disentangled Representation Generalizable AI-Text Detection arXiv 2604.13692 authors Pu"

Links: [{"title":"Breaking the Generator Barrier: Disentangled Representation for Generalizable AI-Text Detection","url":"https://arxiv.org/html/2604.13692"},{"title":"[2604.13692v1] Breaking the Generator Barrier: Disentangled Representation for Generalizable AI-Text Detection","url":"https://arxiv.org/abs/2604.13692v1"},{"title":"[2604.13692] Breaking the Generator Barrier: Disentangled Representation for Generalizable AI-Text Detection","url":"https://arxiv.org/abs/2604.13692"},{"title":"DEER: Disentangled Mixture of Experts with Instance-Adaptive Routing for Generalizable Machine-Generated Text Detection","url":"https://arxiv.org/html/2511.01192"},{"title":"(PDF) Explainable Disentangled Representation Learning for Generalizable Authorship Attribution in the Era of Generative AI","url":"https://www.researchgate.net/publication/404144267_Explainable_Disentangled_Representation_Learning_for_Generalizable_Authorship_Attribution_in_the_Era_of_Generative_AI"},{"title":"Explainable Disentangled Representation Learning for Generalizable Authorship Attribution in the Era of Generative AI","url":"https://arxiv.org/html/2604.21300"},{"title":"[2604.21300] Explainable Disentangled Representation Learning for Generalizable Authorship Attribution in the Era of Generative AI","url":"https://arxiv.org/abs/2604.21300"},{"title":"Explainable Disentangled Representation Learning for Generalizable","url":"https://arxiv.org/pdf/2604.21300"},{"title":"Feature-Augmented Transformers for Robust AI-Text Detection Across Domains and Generators","url":"https://arxiv.org/html/2605.03969"},{"title":"AI-generated Text Detection: A Multifaceted Approach to Binary and Multiclass Classification","url":"https://arxiv.org/html/2505.11550"}]

I found the paper you're searching for. Here's what I found:

## "Breaking the Generator Barrier: Disentan
…[truncated 1275 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_research_bib_complete_20260515T043737",
  "tool": "WebSearch",
  "elapsed_ms": 4
}
```

</details>

---

### Tool result

_source line 43 · 2026-05-15T04:42:11.264718+00:00_

Web search results for query: "Can AI-Generated Text be Reliably Detected Sadasivan ICLR 2024 authors"

Links: [{"title":"Can AI-Generated Text be Reliably Detected? | OpenReview","url":"https://openreview.net/forum?id=NvSwR4IvLO"},{"title":"[2303.11156] Can AI-Generated Text be Reliably Detected?","url":"https://arxiv.org/abs/2303.11156"},{"title":"(PDF) Can AI-Generated Text be Reliably Detected?","url":"https://www.researchgate.net/publication/369380286_Can_AI-Generated_Text_be_Reliably_Detected"},{"title":"Can AI-Generated Text be Reliably Detected?","url":"https://arxiv.org/pdf/2303.11156"},{"title":"[PDF] Can AI-Generated Text be Reliably Detected? | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Can-AI-Generated-Text-be-Reliably-Detected-Sadasivan-Kumar/5ee8bb4fc80a291b2e416a2a879e7153a783d7e9"},{"title":"Can AI-Generated Text be Reliably Detected? - ADS","url":"https://ui.adsabs.harvard.edu/abs/2023arXiv230311156S/abstract"},{"title":"Can AI-Generated Text be Reliably Detected? Stress Testing AI Text Detectors Under Various Attacks | OpenReview","url":"https://openreview.net/forum?id=OOgsAZdFOt"},{"title":"Can AI-Generated Text be Reliably Detected?","url":"https://scispace.com/pdf/can-ai-generated-text-be-reliably-detected-1p8qe3ww.pdf"},{"title":"Can AI-Generated Text be Reliably Detected? | alphaXiv","url":"https://www.alphaxiv.org/overview/2303.11156v4"},{"title":"Can AI-Generated Text be Reliably Detected?","url":"https://bibbase.org/network/publication/sadasivan-kumar-balasubramanian-wang-feizi-canaigeneratedtextbereliablydetected-2023"}]

Based on the search results, I found information about the paper "Can AI-Generated Text be Reliably Detected?"

The paper is authored by Vinu Sankar Sadasivan and 3 other authors. More specifically, the authors are Vinu Sankar Sadasivan, Aounon Kumar, Sriram Balasubramanian, Wenxiao Wang, and Soheil Feizi.

The paper stress-tests the robustness of AI text detectors in the presence of an attacker, intr
…[truncated 647 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_research_bib_complete_20260515T043737",
  "tool": "WebSearch",
  "elapsed_ms": 2
}
```

</details>

---

### Tool result

_source line 44 · 2026-05-15T04:42:11.264989+00:00_

Web search results for query: "Feature-Augmented Transformers Robust AI-Text Detection Across Domains Generators arXiv 2605.03969 authors Mady"

Links: [{"title":"[2605.03969] Feature-Augmented Transformers for Robust AI-Text Detection Across Domains and Generators","url":"https://arxiv.org/abs/2605.03969"},{"title":"Feature-Augmented Transformers for Robust AI-Text Detection Across Domains and Generators","url":"https://arxiv.org/html/2605.03969"},{"title":"Adaptive Ensembles of Fine-Tuned Transformers for LLM-Generated Text Detection","url":"https://arxiv.org/html/2403.13335v1"},{"title":"[2509.20375] Assessing Classical Machine Learning and Transformer-based Approaches for Detecting AI-Generated Research Text","url":"https://arxiv.org/abs/2509.20375"},{"title":"Domain Gating Ensemble Networks for AI-Generated Text Detection","url":"https://arxiv.org/html/2505.13855v1"},{"title":"Modeling the Attack: Detecting AI-Generated Text by Quantifying Adversarial Perturbations","url":"https://arxiv.org/html/2510.02319v1"},{"title":"[2601.03812] AI Generated Text Detection","url":"https://arxiv.org/abs/2601.03812"},{"title":"[2605.13373] Exploiting Pre-trained Encoder-Decoder Transformers for Sequence-to-Sequence Constituent Parsing","url":"https://arxiv.org/abs/2605.13373"},{"title":"Diversity Boosts AI-Generated Text Detection","url":"https://arxiv.org/html/2509.18880v1"},{"title":"Efficient detection of AI-generated scientific abstracts with a lightweight transformer | Scientific Reports","url":"https://www.nature.com/articles/s41598-026-35203-3"}]

Based on the search results, I found the paper you're looking for. Here's the information about it:

## Paper Summary

The paper "Feature-Augmented Transformers for Robust AI-Text Detection Across Domains and Generators" (arXiv:2605.03969) was submitted on May 5, 2026, with authors Mohamed Mady, Johannes Reschke, and Björn Schuller.

## Research Focus

The paper addresses the challenge that AI-generated text is nowadays produ
…[truncated 1024 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_research_bib_complete_20260515T043737",
  "tool": "WebSearch",
  "elapsed_ms": 4
}
```

</details>

---

### Tool result

_source line 45 · 2026-05-15T04:42:11.265263+00:00_

Web search results for query: "Paraphrasing Evades Detectors AI-Generated Text Retrieval Effective Defense Krishna NeurIPS 2023 authors"

Links: [{"title":"GitHub - martiansideofthemoon/ai-detection-paraphrases: Official repository for our NeurIPS 2023 paper \"Paraphrasing evades detectors of AI-generated text, but retrieval is an effective defense\" (https://arxiv.org/abs/2303.13408). · GitHub","url":"https://github.com/martiansideofthemoon/ai-detection-paraphrases"},{"title":"Paraphrasing evades detectors of AI-generated text, but retrieval is an effective defense","url":"https://proceedings.neurips.cc/paper_files/paper/2023/hash/575c450013d0e99e4b0ecf82bd1afaa4-Abstract-Conference.html"},{"title":"[2303.13408] Paraphrasing evades detectors of AI-generated text, but retrieval is an effective defense","url":"https://arxiv.org/abs/2303.13408"},{"title":"NeurIPS Poster Paraphrasing evades detectors of AI-generated text, but retrieval is an effective defense","url":"https://neurips.cc/virtual/2023/poster/71402"},{"title":"[PDF] Paraphrasing evades detectors of AI-generated text, but retrieval is an effective defense | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Paraphrasing-evades-detectors-of-AI-generated-text,-Krishna-Song/1c13af186d1e177b85ef1ec3fc7b8d33ec314cfd"},{"title":"Paraphrasing evades detectors of AI-generated text, but retrieval is an effective defense | OpenReview","url":"https://openreview.net/forum?id=WbFhFvjjKj"},{"title":"Paraphrasing evades detectors of AI-generated text, but retrieval is an effective defense | Request PDF","url":"https://www.researchgate.net/publication/369477232_Paraphrasing_evades_detectors_of_AI-generated_text_but_retrieval_is_an_effective_defense"},{"title":"Paraphrasing evades detectors of AI-generated text, but ...","url":"https://arxiv.org/pdf/2303.13408"},{"title":"Paraphrasing evades detectors of AI-generated text, but retrieval is an effective defense - ADS","url":"https://ui.adsabs.harvard.edu/abs/2023
…[truncated 1682 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_research_bib_complete_20260515T043737",
  "tool": "WebSearch",
  "elapsed_ms": 3
}
```

</details>

---

### Tool call

_source line 46 · 2026-05-15T04:42:11.265504+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Strong Model Collapse Dohmatob ICLR 2024 authors"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_research_bib_complete_20260515T043737",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Strong Model Collapse Dohmatob ICLR 2024 authors"
  }
}
```

</details>

---

### Tool call

_source line 47 · 2026-05-15T04:42:11.265768+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Is Model Collapse Inevitable Breaking the Curse of Recursion Accumulating Real Synthetic Data arXiv 2404.01413 authors"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_research_bib_complete_20260515T043737",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Is Model Collapse Inevitable Breaking the Curse of Recursion Accumulating Real Synthetic Data arXiv 2404.01413 authors"
  }
}
```

</details>

---

### Tool result

_source line 48 · 2026-05-15T04:42:11.265985+00:00_

Web search results for query: "Self-Consuming Generative Models Go MAD arXiv 2307.01850 authors"

Links: [{"title":"[2307.01850] Self-Consuming Generative Models Go MAD","url":"https://arxiv.org/abs/2307.01850"},{"title":"[PDF] Self-Consuming Generative Models Go MAD | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Self-Consuming-Generative-Models-Go-MAD-Alemohammad-Casco-Rodriguez/ad022cd5da75637ac3e0a8f8cc4f0d394ba5ff7a"},{"title":"(PDF) Self-Consuming Generative Models Go MAD","url":"https://www.researchgate.net/publication/372136378_Self-Consuming_Generative_Models_Go_MAD"},{"title":"Self-Consuming Generative Models Go MAD | BibSonomy","url":"https://www.bibsonomy.org/bibtex/2b7d3868c3b55dac04a64f9b2231237a6/andolab"},{"title":"Self-Consuming Generative Models Go MAD","url":"https://richb.rice.edu/2023/07/12/self-consuming-generative-models-go-mad/"},{"title":"Self-Consuming Generative Models Go MAD | Cool Papers - Immersive Paper Discovery","url":"https://papers.cool/arxiv/2307.01850"},{"title":"Self-Consuming Generative Models Go MAD","url":"https://dsp.rice.edu/2023/07/06/self-consuming-generative-models-go-mad/"},{"title":"SELF-CONSUMING GENERATIVE MODELS GO MAD","url":"https://openreview.net/pdf?id=ShjMHfmPs0"},{"title":"Paper page - Self-Consuming Generative Models Go MAD","url":"https://huggingface.co/papers/2307.01850"},{"title":"Self-Consuming Generative Models Go MAD - ADS","url":"https://ui.adsabs.harvard.edu/abs/2023arXiv230701850A/abstract"}]

Based on the search results, the authors of arXiv:2307.01850 "Self-Consuming Generative Models Go MAD" are Sina Alemohammad, Josue Casco-Rodriguez, Lorenzo Luzi, Ahmed Imtiaz Humayun, Hossein Babaei, Daniel LeJeune, Ali Siahkoohi, and Richard G. Baraniuk. The paper was to appear at ICLR 2024.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_research_bib_complete_20260515T043737",
  "tool": "WebSearch",
  "elapsed_ms": 2
}
```

</details>

---

### Tool call

_source line 49 · 2026-05-15T04:42:11.266258+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Data Selection for Language Models via Importance Resampling Xie NeurIPS 2023 authors"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_research_bib_complete_20260515T043737",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Data Selection for Language Models via Importance Resampling Xie NeurIPS 2023 authors"
  }
}
```

</details>

---

### Tool call

_source line 50 · 2026-05-15T04:42:11.266454+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "QuRating Selecting High-Quality Data for Training Language Models Wettig ICML 2024 authors"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_research_bib_complete_20260515T043737",
  "tool": "WebSearch",
  "tool_args": {
    "query": "QuRating Selecting High-Quality Data for Training Language Models Wettig ICML 2024 authors"
  }
}
```

</details>

---

### Tool call

_source line 51 · 2026-05-15T04:42:11.266719+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "CCNet Extracting High Quality Monolingual Datasets from Web Crawl Data Wenzek LREC 2020 authors"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_research_bib_complete_20260515T043737",
  "tool": "WebSearch",
  "tool_args": {
    "query": "CCNet Extracting High Quality Monolingual Datasets from Web Crawl Data Wenzek LREC 2020 authors"
  }
}
```

</details>

---

### Tool call

_source line 52 · 2026-05-15T04:42:11.266926+00:00_

called Agent

<details open><summary>🔧 Tool call — Agent</summary>

```json
{
  "description": "Search authors group 6",
  "prompt": "Search for the complete author lists of these 4 academic papers using WebSearch. For each paper, search its title and find the full list of authors. Return the results in BibTeX format: {LastName, FirstName and LastName, FirstName and ...}\n\nPapers:\n1. \"LLM as a Broken Telephone: Iterative Generation Distorts Information\" (Mohamed and others, ACL 2025)\n2. \"Markovian Generation Chains in Large Language Models\" (Geng and others, arXiv 2603.11228, 2026)\n3. \"Detecting Pretraining Data from Large Language Models\" (Shi and others, ICLR 2024)\n4. \"Automatic Detection of Machine Generated Text: A Critical Survey\" (Jawahar and others, COLING 2020)\n\nFor each paper, output ONLY the BibTeX key and the complete author field. Do NOT make up author names - if you can't find the full list, say so. Be precise with first/last names and spellings.",
  "subagent_type": "general-purpose"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_research_bib_complete_20260515T043737",
  "tool": "Agent",
  "tool_args": {
    "description": "Search authors group 6",
    "prompt": "Search for the complete author lists of these 4 academic papers using WebSearch. For each paper, search its title and find the full list of authors. Return the results in BibTeX format: {LastName, FirstName and LastName, FirstName and ...}\n\nPapers:\n1. \"LLM as a Broken Telephone: Iterative Generation Distorts Information\" (Mohamed and others, ACL 2025)\n2. \"Markovian Generation Chains in Large Language Models\" (Geng and others, arXiv 2603.11228, 2026)\n3. \"Detecting Pretraining Data from Large Language Models\" (Shi and others, ICLR 2024)\n4. \"Automatic Detection of Machine Generated Text: A Critical Survey\" (Jawahar and others, COLING 2020)\n\nFor each paper, output ONLY the BibTeX key and the complete author field. Do NOT make up author names - if you can't find the full list, say so. Be precise with first/last names and spellings.",
    "subagent_type": "general-purpose"
  }
}
```

</details>

---

### Tool result

_source line 53 · 2026-05-15T04:42:11.267197+00:00_

Web search results for query: "Release Strategies and the Social Impacts of Language Models arXiv 1908.09203 authors"

Links: [{"title":"[1908.09203] Release Strategies and the Social Impacts of Language Models","url":"https://arxiv.org/abs/1908.09203"},{"title":"[1908.09203v1] Release Strategies and the Social Impacts of Language Models","url":"https://arxiv.org/abs/1908.09203v1"},{"title":"[1908.09203v2] Release Strategies and the Social Impacts of Language Models","url":"https://arxiv.org/abs/1908.09203v2"},{"title":"Release Strategies and the Social Impacts of Language Models | Request PDF","url":"https://www.researchgate.net/publication/335419868_Release_Strategies_and_the_Social_Impacts_of_Language_Models"},{"title":"[PDF] Release Strategies and the Social Impacts of Language Models | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Release-Strategies-and-the-Social-Impacts-of-Models-Solaiman-Brundage/c7462e0ee928f095a7fc40b91f1e7557d283ae8e"},{"title":"Google Scholar","url":"https://scholar.google.com/scholar?q=I.+Solaiman+%2C+%E2%80%98Release+Strategies+and+the+Social+Impacts+of+Language+Models%E2%80%99.+arXiv%2C+Nov.+12%2C+2019.+Accessed%3A+Feb.+21%2C+2023.+%5BOnline%5D.+Available%3A+http%3A%2F%2Farxiv.org%2Fabs%2F1908.09203"},{"title":"Release Strategies and the Social Impacts of Language ...","url":"https://arxiv.org/pdf/1908.09203"},{"title":"Paper page - Release Strategies and the Social Impacts of Language Models","url":"https://huggingface.co/papers/1908.09203"},{"title":"Release Strategies and the Social Impacts of Language Models","url":"https://www.catalyzex.com/paper/arxiv:1908.09203"},{"title":"Ethical Bias Mitigation in Large Language Models: A Comparative Evaluation of Fairness-Aware Fine-Tuning Strategies | Journal of Neonatal Surgery","url":"https://www.jneonatalsurg.com/index.php/jns/article/view/4410"}]

Based on the search results, the authors of the arXiv paper 1908.09203 "Release Strategies and the Social Impacts of Languag
…[truncated 650 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_research_bib_complete_20260515T043737",
  "tool": "WebSearch",
  "elapsed_ms": 4
}
```

</details>

---

### Tool result

_source line 54 · 2026-05-15T04:42:11.267463+00:00_

Web search results for query: "Position On the Possibilities of AI-Generated Text Detection Chakraborty ICML 2024 authors"

Links: [{"title":"Position: On the Possibilities of AI-Generated Text Detection","url":"https://proceedings.mlr.press/v235/chakraborty24a.html"},{"title":"[2304.04736] On the Possibilities of AI-Generated Text Detection","url":"https://arxiv.org/abs/2304.04736"},{"title":"Position: On the Possibilities of AI-Generated Text Detection","url":"https://raw.githubusercontent.com/mlresearch/v235/main/assets/chakraborty24a/chakraborty24a.pdf"},{"title":"Position: On the Possibilities of AI-Generated Text Detection | OpenReview","url":"https://openreview.net/forum?id=CJbhtpcyGL"},{"title":"On the Possibilities of AI-Generated Text Detection: A Sample Complexity Analysis | OpenReview","url":"https://openreview.net/forum?id=oxEER3kZ9M"},{"title":"Position: On the possibilities of AI-generated text detection","url":"https://dl.acm.org/doi/10.5555/3692070.3692305"},{"title":"A Survey on the Possibilities & Impossibilities of AI-generated Text Detection | Semantic Scholar","url":"https://www.semanticscholar.org/paper/f582daa2f2822c0aa1291fe3925f69c25280e37e"},{"title":"ICML Poster Position: On the Possibilities of AI-Generated Text Detection","url":"https://icml.cc/virtual/2024/poster/34689"},{"title":"On the Possibilities of AI-Generated Text Detection","url":"https://arxiv.org/pdf/2304.04736"},{"title":"[PDF] On the Possibilities of AI-Generated Text Detection | Semantic Scholar","url":"https://www.semanticscholar.org/paper/On-the-Possibilities-of-AI-Generated-Text-Detection-Chakraborty-Bedi/1c9693a721271e3f915f0f0b8159578495d5c815"}]

Based on the search results, here's the information about the paper "Position: On the Possibilities of AI-Generated Text Detection" from ICML 2024:

## Authors

The authors are: Souradip Chakraborty, Amrit Singh Bedi, Sicheng Zhu, Bang An, Dinesh Manocha, and Furong Huang.

## Paper Overview

The study addresses the challen
…[truncated 901 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_research_bib_complete_20260515T043737",
  "tool": "WebSearch",
  "elapsed_ms": 5
}
```

</details>

---

### Tool call

_source line 55 · 2026-05-15T04:42:11.267724+00:00_

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
  "session": "worker_paper_research_bib_complete_20260515T043737",
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

_source line 56 · 2026-05-15T04:42:11.267902+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_research_bib_complete_20260515T043737",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 57 · 2026-05-15T04:42:11.268101+00:00_

Web search results for query: "Data Selection for Language Models via Importance Resampling Xie NeurIPS 2023 authors"

Links: [{"title":"NeurIPS Poster Data Selection for Language Models via Importance Resampling","url":"https://neurips.cc/virtual/2023/poster/70154"},{"title":"[2302.03169] Data Selection for Language Models via Importance Resampling","url":"https://arxiv.org/abs/2302.03169"},{"title":"Data Selection for Language Models via Importance Resampling","url":"https://proceedings.neurips.cc//paper_files/paper/2023/hash/6b9aa8f418bde2840d5f4ab7a02f663b-Abstract-Conference.html"},{"title":"Data Selection for Language Models via Importance Resampling | OpenReview","url":"https://openreview.net/forum?id=uPSQv0leAu&noteId=3EMr1ZhaRY"},{"title":"Data Selection for Language Models via Importance Resampling","url":"https://openreview.net/pdf?id=uPSQv0leAu"},{"title":"GitHub - p-lambda/dsir: DSIR large-scale data selection framework for language model training · GitHub","url":"https://github.com/p-lambda/dsir"},{"title":"Data Selection for Language Models via Importance Resampling - ADS","url":"https://ui.adsabs.harvard.edu/abs/2023arXiv230203169X/abstract"},{"title":"Data Selection for Language Models via Importance Resampling","url":"https://www.researchgate.net/publication/368333487_Data_Selection_for_Language_Models_via_Importance_Resampling"},{"title":"[Quick Review] Data Selection for Language Models via Importance Resampling","url":"https://liner.com/review/data-selection-for-language-models-via-importance-resampling"},{"title":"Data selection for language models via importance resampling | Proceedings of the 37th International Conference on Neural Information Processing Systems","url":"https://dl.acm.org/doi/10.5555/3666122.3667604"}]

Based on the search results, I found the authors of the NeurIPS 2023 paper "Data Selection for Language Models via Importance Resampling":

The authors are Sang Michael Xie, Shibani Santurkar, Tengyu Ma, and Percy Liang.


REM
…[truncated 97 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_research_bib_complete_20260515T043737",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool call

_source line 58 · 2026-05-15T04:42:11.268322+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "A Watermark for Large Language Models Kirchenbauer ICML 2023 authors"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_research_bib_complete_20260515T043737",
  "tool": "WebSearch",
  "tool_args": {
    "query": "A Watermark for Large Language Models Kirchenbauer ICML 2023 authors"
  }
}
```

</details>

---

### Tool result

_source line 59 · 2026-05-15T04:42:11.268535+00:00_

Web search results for query: "Strong Model Collapse Dohmatob ICLR 2024 authors"

Links: [{"title":"Published as a conference paper at ICLR 2025 STRONG MODEL COLLAPSE","url":"https://proceedings.iclr.cc/paper_files/paper/2025/file/284afdc2309f9667d2d4fb9290235b0c-Paper-Conference.pdf"},{"title":"[2410.04840] Strong Model Collapse","url":"https://arxiv.org/abs/2410.04840"},{"title":"Strong Model Collapse | OpenReview","url":"https://openreview.net/forum?id=et5l9qPUhm"},{"title":"Strong Model Collapse Elvis Dohmatob1 e.dohmatob@meta.com Yunzhen Feng1,2,∗","url":"https://arxiv.org/pdf/2410.04840"},{"title":"Overcoming the AI Data Crisis: A New Solution to Model Collapse | by NYU Center for Data Science | Medium","url":"https://nyudatascience.medium.com/overcoming-the-ai-data-crisis-a-new-solution-to-model-collapse-ddc5b382e182"},{"title":"Escaping Model Collapse via Synthetic Data Verification: Near-term Improvements and Long-term ConvergenceThis project is supported by the AI2050 program at Schmidt Sciences (Grant G-24-66104) and Army Research Office Award W911NF-23-1-0030. We also thank Cong Ma from UChicago, Hongning Wang and Bo Li from Tsinghua, Pinyan Lu and Gavin Tang from Shanghai University of Finance and Economics for helpful discussions and suggestions.","url":"https://arxiv.org/html/2510.16657v1"},{"title":"ICLR A Tale of Tails: Model Collapse as a Change of Scaling Laws","url":"https://iclr.cc/virtual/2024/22420"},{"title":"Strong Model Collapse - ADS","url":"https://ui.adsabs.harvard.edu/abs/2024arXiv241004840D/abstract"},{"title":"ICLR Poster Strong Model Collapse","url":"https://iclr.cc/virtual/2025/poster/32070"},{"title":"Position: Model Collapse Does Not Mean What You Think Anonymous Author(s)","url":"https://openreview.net/pdf?id=ygfzWIGDN8"}]

Based on the search results, the authors of "Strong Model Collapse" are Elvis Dohmatob, Yunzhen Feng, Arjun Subramonian, and Julia Kempe. 

Note: The paper was published at ICLR 2025, not ICLR 2024. The paper 
…[truncated 170 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_research_bib_complete_20260515T043737",
  "tool": "WebSearch",
  "elapsed_ms": 3
}
```

</details>

---

### Tool result

_source line 60 · 2026-05-15T04:42:11.268774+00:00_

Web search results for query: "The Curse of Recursion Training on Generated Data Makes Models Forget Shumailov Nature 2024 authors"

Links: [{"title":"[2305.17493] The Curse of Recursion: Training on Generated Data Makes Models Forget","url":"https://arxiv.org/abs/2305.17493"},{"title":"[PDF] The Curse of Recursion: Training on Generated Data Makes Models Forget | Semantic Scholar","url":"https://www.semanticscholar.org/paper/The-Curse-of-Recursion:-Training-on-Generated-Data-Shumailov-Shumaylov/155aec5cff650263a4c71136f97570611d1bba7a"},{"title":"The Curse of Recursion: Training on Generated Data Makes Models Forget","url":"https://arxiv.org/html/2305.17493v3"},{"title":"The Curse of Recursion: Training on Generated Data Makes Models Forget | AI Research Paper Details","url":"https://www.aimodels.fyi/papers/arxiv/curse-recursion-training-generated-data-makes-models"},{"title":"THE CURSE OF RECURSION: TRAINING ON GENERATED DATA MAKES MODELS FORGET","url":"https://www.cl.cam.ac.uk/~is410/Papers/dementia_arxiv.pdf"},{"title":"The Curse of Recursion: Training on Generated Data Makes Models Forget | alphaXiv","url":"https://www.alphaxiv.org/overview/2305.17493v3"},{"title":"The Curse of Recursion: Training on Generated Data Makes Models Forget (2023) | Ilia Shumailov | 153 Citations","url":"https://scispace.com/papers/the-curse-of-recursion-training-on-generated-data-makes-34zgysyl"},{"title":"Is Model Collapse Inevitable? Breaking the Curse of Recursion by Accumulating Real and Synthetic Data","url":"https://arxiv.org/html/2404.01413v2"},{"title":"Is Model Collapse Inevitable? Breaking the Curse of Recursion by Accumulating Real and Synthetic Data | OpenReview","url":"https://openreview.net/forum?id=5B2K4LRgmz"},{"title":"Recursive Pollution and Model Collapse Are Not the Same | BIML","url":"https://berryvilleiml.com/2026/01/10/recursive-pollution-and-model-collapse-are-not-the-same/"}]

Based on the search results, I found information about the paper "The Curse of Rec
…[truncated 898 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_research_bib_complete_20260515T043737",
  "tool": "WebSearch",
  "elapsed_ms": 5
}
```

</details>

---

### Tool call

_source line 61 · 2026-05-15T04:42:11.269020+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Scalable Watermarking for Identifying Large Language Model Outputs Dathathri Nature 2024 authors"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_research_bib_complete_20260515T043737",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Scalable Watermarking for Identifying Large Language Model Outputs Dathathri Nature 2024 authors"
  }
}
```

</details>

---

### Tool call

_source line 62 · 2026-05-15T04:42:11.269241+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "arxiv 2305.17359 DNA-GPT Xianjun Yang Wei Cheng Yue Wu Linda Petzold William Wang Haifeng Chen full author list"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_research_bib_complete_20260515T043737",
  "tool": "WebSearch",
  "tool_args": {
    "query": "arxiv 2305.17359 DNA-GPT Xianjun Yang Wei Cheng Yue Wu Linda Petzold William Wang Haifeng Chen full author list"
  }
}
```

</details>

---

### Tool call

_source line 63 · 2026-05-15T04:42:11.269424+00:00_

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
  "session": "worker_paper_research_bib_complete_20260515T043737",
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

_source line 64 · 2026-05-15T04:42:11.269610+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_research_bib_complete_20260515T043737",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 65 · 2026-05-15T04:42:11.269793+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "arxiv 2401.12070 Binoculars Abhimanyu Hans Avi Schwarzschild full author list"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_research_bib_complete_20260515T043737",
  "tool": "WebSearch",
  "tool_args": {
    "query": "arxiv 2401.12070 Binoculars Abhimanyu Hans Avi Schwarzschild full author list"
  }
}
```

</details>

---

### Tool call

_source line 66 · 2026-05-15T04:42:11.269971+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Chainwash Multi-Step Rewriting Attacks Diffusion Language Model Watermarks Ameen arXiv 2605.05503 2026 authors"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_research_bib_complete_20260515T043737",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Chainwash Multi-Step Rewriting Attacks Diffusion Language Model Watermarks Ameen arXiv 2605.05503 2026 authors"
  }
}
```

</details>

---

### Tool result

_source line 67 · 2026-05-15T04:42:11.270154+00:00_

Web search results for query: "Is Model Collapse Inevitable Breaking the Curse of Recursion Accumulating Real Synthetic Data arXiv 2404.01413 authors"

Links: [{"title":"[2404.01413] Is Model Collapse Inevitable? Breaking the Curse of Recursion by Accumulating Real and Synthetic Data","url":"https://arxiv.org/abs/2404.01413"},{"title":"Is Model Collapse Inevitable? Breaking the Curse of Recursion by Accumulating Real and Synthetic Data","url":"https://arxiv.org/html/2404.01413v2"},{"title":"Is Model Collapse Inevitable? Breaking the Curse of","url":"https://arxiv.org/pdf/2404.01413"},{"title":"Is Model Collapse Inevitable? Breaking the Curse of Recursion by Accumulating Real and Synthetic Data | Rylan Schaeffer","url":"https://rylanschaeffer.github.io/content/research/2024_arxiv_is_model_collapse_inevitable/main.html"},{"title":"Is Model Collapse Inevitable? Breaking the Curse of Recursion by Accumulating Real and Synthetic Data | OpenReview","url":"https://openreview.net/forum?id=5B2K4LRgmz"},{"title":"[2404.01413v1] Is Model Collapse Inevitable? Breaking the Curse of Recursion by Accumulating Real and Synthetic Data","url":"https://arxiv.org/abs/2404.01413v1"},{"title":"Is Model Collapse Inevitable? Breaking the Curse of Recursion by Accumulating Real and Synthetic Data - ADS","url":"https://ui.adsabs.harvard.edu/abs/2024arXiv240401413G/abstract"},{"title":"[PDF] Is Model Collapse Inevitable? Breaking the Curse of Recursion by Accumulating Real and Synthetic Data | Semantic Scholar","url":"https://www.semanticscholar.org/paper/e8815da26d4e6cac8b23b7e6aa75cec028cb66d2"},{"title":"Accumulating Data Prevents Model Collapse","url":"https://www.emergentmind.com/papers/2404.01413"},{"title":"Google Scholar","url":"https://scholar.google.com/scholar?q=Is+Model+Collapse+Inevitable?+Breaking+the+Curse+of+Recursion+by+Accumulating+Real+and+Synthetic+Data."}]

Based on the search results, here is the information about the paper arXiv 2404.01413:

## Paper Information

**Titl
…[truncated 942 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_research_bib_complete_20260515T043737",
  "tool": "WebSearch",
  "elapsed_ms": 4
}
```

</details>

---

### Tool call

_source line 68 · 2026-05-15T04:42:11.270399+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "arxiv 2310.05130 Fast-DetectGPT Guangsheng Bao Yanbin Zhao full author list"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_research_bib_complete_20260515T043737",
  "tool": "WebSearch",
  "tool_args": {
    "query": "arxiv 2310.05130 Fast-DetectGPT Guangsheng Bao Yanbin Zhao full author list"
  }
}
```

</details>

---

### Tool result

_source line 69 · 2026-05-15T04:42:11.270605+00:00_

Web search results for query: "QuRating Selecting High-Quality Data for Training Language Models Wettig ICML 2024 authors"

Links: [{"title":"GitHub - princeton-nlp/QuRating: [ICML 2024] Selecting High-Quality Data for Training Language Models","url":"https://github.com/princeton-nlp/QuRating"},{"title":"[2402.09739] QuRating: Selecting High-Quality Data for Training Language Models","url":"https://arxiv.org/abs/2402.09739"},{"title":"ICLR QuRating: Selecting High-Quality Data for Training Language Models","url":"https://iclr.cc/virtual/2024/21159"},{"title":"QuRating: selecting high-quality data for training language ...","url":"https://dl.acm.org/doi/10.5555/3692070.3694241"},{"title":"QuRating: Selecting High-Quality Data for Training Language Models","url":"https://proceedings.mlr.press/v235/wettig24a.html"},{"title":"ICLR QuRating: Selecting High-Quality Data for Training Lanugage Models","url":"https://iclr.cc/virtual/2024/22410"},{"title":"QuRating: Selecting High-Quality Data for Training Language Models - ADS","url":"https://ui.adsabs.harvard.edu/abs/2024arXiv240209739W/abstract"},{"title":"[2402.09739v3] QuRating: Selecting High-Quality Data for Training Language Models","url":"https://arxiv.org/abs/2402.09739v3"},{"title":"QuRating: Selecting High-Quality Data for Training Language Models | OpenReview","url":"https://openreview.net/forum?id=GLGYYqPwjy"},{"title":"[PDF] QuRating: Selecting High-Quality Data for Training Language Models | Semantic Scholar","url":"https://www.semanticscholar.org/paper/QuRating:-Selecting-High-Quality-Data-for-Training-Wettig-Gupta/34efdeaf0a78d6906b4da7335afc7182df11f639"}]

Based on the search results, here is the information about the QuRating paper:

## Paper Details

The paper is titled "QuRating: Selecting High-Quality Data for Training Language Models" and was published at ICML 2024 by authors Alexander Wettig, Aatmik Gupta, Saumya Malik, and Danqi Chen.

## Overview

QuRating is a method for selecting pre-training dat
…[truncated 907 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_research_bib_complete_20260515T043737",
  "tool": "WebSearch",
  "elapsed_ms": 4
}
```

</details>

---

### Tool result

_source line 70 · 2026-05-15T04:42:11.270847+00:00_

Web search results for query: "A Watermark for Large Language Models Kirchenbauer ICML 2023 authors"

Links: [{"title":"[2301.10226] A Watermark for Large Language Models","url":"https://arxiv.org/abs/2301.10226"},{"title":"[PDF] A Watermark for Large Language Models | Semantic Scholar","url":"https://www.semanticscholar.org/paper/A-Watermark-for-Large-Language-Models-Kirchenbauer-Geiping/cb5b71a622aff47014d4f28a958679629a8b6363"},{"title":"A Watermark for Large Language Models","url":"https://proceedings.mlr.press/v202/kirchenbauer23a.html"},{"title":"ICML Poster A Watermark for Large Language Models","url":"https://icml.cc/virtual/2023/poster/24544"},{"title":"GitHub - jwkirchenbauer/lm-watermarking · GitHub","url":"https://github.com/jwkirchenbauer/lm-watermarking"},{"title":"A Watermark for Large Language Models | NSF Public Access Repository","url":"https://par.nsf.gov/biblio/10522346-watermark-large-language-models"},{"title":"A Watermark for Large Language Models","url":"https://arxiv.org/pdf/2301.10226"},{"title":"dblp: A Watermark for Large Language Models.","url":"https://dblp.org/rec/conf/icml/KirchenbauerGWK23.html"},{"title":"A Watermark for Large Language Models | Request PDF","url":"https://www.researchgate.net/publication/367388838_A_Watermark_for_Large_Language_Models"},{"title":"[2306.04634] On the Reliability of Watermarks for Large Language Models","url":"https://arxiv.org/abs/2306.04634"}]

Based on the search results, the authors of "A Watermark for Large Language Models" published at ICML 2023 are: John Kirchenbauer, Jonas Geiping, Yuxin Wen, Jonathan Katz, Ian Miers, and Tom Goldstein.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_research_bib_complete_20260515T043737",
  "tool": "WebSearch",
  "elapsed_ms": 2
}
```

</details>

---

### Tool call

_source line 71 · 2026-05-15T04:42:11.271097+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "arxiv 2604.13692 \"Xiao Pu\" \"Zepeng Cheng\" \"Lin Yuan\" full author list"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_research_bib_complete_20260515T043737",
  "tool": "WebSearch",
  "tool_args": {
    "query": "arxiv 2604.13692 \"Xiao Pu\" \"Zepeng Cheng\" \"Lin Yuan\" full author list"
  }
}
```

</details>

---

### Tool call

_source line 72 · 2026-05-15T04:42:11.271323+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "arxiv 2605.03969 \"Mohamed Mady\" \"Johannes Reschke\" \"Björn Schuller\" full author list"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_research_bib_complete_20260515T043737",
  "tool": "WebSearch",
  "tool_args": {
    "query": "arxiv 2605.03969 \"Mohamed Mady\" \"Johannes Reschke\" \"Björn Schuller\" full author list"
  }
}
```

</details>

---

### Tool result

_source line 73 · 2026-05-15T04:42:11.271524+00:00_

Web search results for query: "arxiv 2305.17359 DNA-GPT Xianjun Yang Wei Cheng Yue Wu Linda Petzold William Wang Haifeng Chen full author list"

Links: [{"title":"[2305.17359] DNA-GPT: Divergent N-Gram Analysis for Training-Free Detection of GPT-Generated Text","url":"https://arxiv.org/abs/2305.17359"},{"title":"DNA-GPT: Divergent N-Gram Analysis for Training-Free ...","url":"https://arxiv.org/pdf/2305.17359"},{"title":"dblp: DNA-GPT: Divergent N-Gram Analysis for Training-Free Detection of GPT-Generated Text.","url":"https://dblp.org/rec/journals/corr/abs-2305-17359.html"},{"title":"GP-GPT: Large Language Model for Gene-Phenotype Mapping","url":"https://arxiv.org/html/2409.09825v1"},{"title":"ChatGPT for digital pathology research - PMC","url":"https://pmc.ncbi.nlm.nih.gov/articles/PMC11299190/"},{"title":"Biology Instructions: A Dataset and Benchmark for Multi-Omics Sequence Understanding Capability of Large Language Models","url":"https://arxiv.org/html/2412.19191v1"},{"title":"Biomolecules authors/titles recent submissions","url":"https://arxiv.org/list/q-bio.BM/pastweek?show=8"},{"title":"Genomic Language Models: Opportunities and Challenges","url":"https://arxiv.org/html/2407.11435v1"},{"title":"Computational Geometry authors/titles May 2011","url":"https://arxiv.org/list/cs.CG/1105"},{"title":"Computer Science authors/titles Jan 2016","url":"https://arxiv.org/list/cs/1601"}]

Based on the search results, I found the full author list for the arXiv paper 2305.17359 "DNA-GPT: Divergent N-Gram Analysis for Training-Free Detection of GPT-Generated Text."

The authors are: Xianjun Yang, Wei Cheng, Yue Wu, Linda Petzold, William Yang Wang, and Haifeng Chen.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_research_bib_complete_20260515T043737",
  "tool": "WebSearch",
  "elapsed_ms": 2
}
```

</details>

---

### Tool call

_source line 74 · 2026-05-15T04:42:11.271776+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "LLM as a Broken Telephone Iterative Generation Distorts Information ACL 2025 authors"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_research_bib_complete_20260515T043737",
  "tool": "WebSearch",
  "tool_args": {
    "query": "LLM as a Broken Telephone Iterative Generation Distorts Information ACL 2025 authors"
  }
}
```

</details>

---

### Tool result

_source line 75 · 2026-05-15T04:42:11.271993+00:00_

Web search results for query: "arxiv 2401.12070 Binoculars Abhimanyu Hans Avi Schwarzschild full author list"

Links: [{"title":"[2401.12070] Spotting LLMs With Binoculars: Zero-Shot Detection of Machine-Generated Text","url":"https://arxiv.org/abs/2401.12070"},{"title":"[2401.12070v1] Spotting LLMs With Binoculars: Zero-Shot Detection of Machine-Generated Text","url":"https://arxiv.org/abs/2401.12070v1"},{"title":"[2401.12070v2] Spotting LLMs With Binoculars: Zero-Shot Detection of Machine-Generated Text","url":"https://arxiv.org/abs/2401.12070v2"},{"title":"[PDF] Spotting LLMs With Binoculars: Zero-Shot Detection of Machine-Generated Text | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Spotting-LLMs-With-Binoculars:-Zero-Shot-Detection-Hans-Schwarzschild/8dafb105a0cec1956443003eeea9fcf13c0ffa99"},{"title":"Spotting LLMs With Binoculars: Zero-Shot Detection of Machine-Generated Text - ADS","url":"https://ui.adsabs.harvard.edu/abs/2024arXiv240112070H/abstract"},{"title":"Google Académico","url":"https://scholar.google.com/scholar?q=Abhimanyu+Hans%2C+Avi+Schwarzschild%2C+Valeriia+Cherepanova%2C+Hamid+Kazemi%2C+Aniruddha+Saha%2C+Micah+Goldblum%2C+Jonas+Geiping%2C+and+Tom+Goldstein.+2024.+Spotting+llms+with+binoculars%3A+Zero-shot+detection+of+machine-generated+text.+arXiv+preprint+arXiv%3A2401.12070%282024%29."},{"title":"GitHub - ahans30/Binoculars: [ICML 2024] Binoculars: Zero-Shot Detection of LLM-Generated Text · GitHub","url":"https://github.com/ahans30/Binoculars"},{"title":"Spotting LLMs With Binoculars: Zero-Shot Detection of Machine-Generated Text","url":"https://arxiv.org/html/2401.12070"},{"title":"Spotting LLMs With Binoculars: Zero-Shot...","url":"https://axi.lims.ac.uk/paper/2401.12070"},{"title":"Spotting LLMs With Binoculars: Zero-Shot Detection of ...","url":"https://arxiv.org/pdf/2401.12070"}]

Based on the search results, the full author list for arXiv paper 2401.12070 "Spotting LLMs With Binoculars: Zero-Shot Detection of Machine-G
…[truncated 258 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_research_bib_complete_20260515T043737",
  "tool": "WebSearch",
  "elapsed_ms": 2
}
```

</details>

---

### Tool call

_source line 76 · 2026-05-15T04:42:11.272253+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "arxiv 1908.09203 Solaiman Brundage Clark Askell complete author list all authors"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_research_bib_complete_20260515T043737",
  "tool": "WebSearch",
  "tool_args": {
    "query": "arxiv 1908.09203 Solaiman Brundage Clark Askell complete author list all authors"
  }
}
```

</details>

---

### Tool call

_source line 77 · 2026-05-15T04:42:11.272478+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Markovian Generation Chains in Large Language Models arXiv 2603.11228 authors"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_research_bib_complete_20260515T043737",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Markovian Generation Chains in Large Language Models arXiv 2603.11228 authors"
  }
}
```

</details>

---

### Tool call

_source line 78 · 2026-05-15T04:42:11.272705+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "arxiv 2410.04840 \"Strong Model Collapse\" Dohmatob Feng complete authors"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_research_bib_complete_20260515T043737",
  "tool": "WebSearch",
  "tool_args": {
    "query": "arxiv 2410.04840 \"Strong Model Collapse\" Dohmatob Feng complete authors"
  }
}
```

</details>

---

### Tool result

_source line 79 · 2026-05-15T04:42:11.272937+00:00_

Web search results for query: "CCNet Extracting High Quality Monolingual Datasets from Web Crawl Data Wenzek LREC 2020 authors"

Links: [{"title":"CCNet: Extracting High Quality Monolingual Datasets from Web Crawl Data - ACL Anthology","url":"https://aclanthology.org/2020.lrec-1.494/"},{"title":"[1911.00359] CCNet: Extracting High Quality Monolingual Datasets from Web Crawl Data","url":"https://arxiv.org/abs/1911.00359"},{"title":"CCNet: Extracting High Quality Monolingual Datasets from ...","url":"https://aclanthology.org/2020.lrec-1.494.pdf"},{"title":"GitHub - facebookresearch/cc_net: Tools to download and cleanup Common Crawl data","url":"https://github.com/facebookresearch/cc_net"},{"title":"CCNet: Extracting High Quality Monolingual Datasets from ...","url":"http://www.lrec-conf.org/proceedings/lrec2020/pdf/2020.lrec-1.494.pdf"},{"title":"CCNet: Extracting High Quality Monolingual Datasets from Web Crawl Data - ACL Anthology","url":"https://arne.chark.eu/anthology/2020.lrec-1.494/"},{"title":"[1911.00359v2] CCNet: Extracting High Quality Monolingual Datasets from Web Crawl Data","url":"https://arxiv.org/abs/1911.00359v2"},{"title":"CCNet: Extracting High Quality Monolingual Datasets from Web Crawl Data. | BibSonomy","url":"https://www.bibsonomy.org/bibtex/245540f9667239913db153792be9fff73/dblp"},{"title":"[PDF] CCNet: Extracting High Quality Monolingual Datasets from Web Crawl Data | Semantic Scholar","url":"https://www.semanticscholar.org/paper/CCNet:-Extracting-High-Quality-Monolingual-Datasets-Wenzek-Lachaux/c20c68c45127439139a08adb0b1f2b8354a94d6c"},{"title":"SEACrowd/cc100 · Datasets at Hugging Face","url":"https://huggingface.co/datasets/SEACrowd/cc100"}]

Based on the search results, here is the information about the CCNet paper:

## Paper Details

The paper "CCNet: Extracting High Quality Monolingual Datasets from Web Crawl Data" was published by Wenzek et al. at LREC 2020.

## Authors

The seven authors are: Guillaume Wenzek, Marie-Anne Lachaux, Alexi
…[truncated 757 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_research_bib_complete_20260515T043737",
  "tool": "WebSearch",
  "elapsed_ms": 6
}
```

</details>

---

### Tool result

_source line 80 · 2026-05-15T04:42:11.273172+00:00_

Web search results for query: "Scalable Watermarking for Identifying Large Language Model Outputs Dathathri Nature 2024 authors"

Links: [{"title":"Scalable watermarking for identifying large language model outputs | Nature","url":"https://www.nature.com/articles/s41586-024-08025-4"},{"title":"Scalable watermarking for identifying large language model outputs | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Scalable-watermarking-for-identifying-large-model-Dathathri-See/89bd8efe0b9c0427cb7814d7b8c2b0190d2ffa9e"},{"title":"Scalable watermarking for identifying large language model outputs - PMC","url":"https://pmc.ncbi.nlm.nih.gov/articles/PMC11499265/"},{"title":"Scalable watermarking for identifying large language model outputs – ScienceOpen","url":"https://www.scienceopen.com/document?vid=e36b034b-6be1-439b-bccb-f413efc57773"},{"title":"GitHub - google-deepmind/synthid-text · GitHub","url":"https://github.com/google-deepmind/synthid-text"},{"title":"(PDF) Scalable watermarking for identifying large language model outputs","url":"https://www.researchgate.net/publication/385176946_Scalable_watermarking_for_identifying_large_language_model_outputs"},{"title":"Scalable watermarking for identifying large language ...","url":"https://pubmed.ncbi.nlm.nih.gov/39443777/"},{"title":"Scalable watermarking for identifying large language model outputs","url":"https://ideas.repec.org/a/nat/nature/v634y2024i8035d10.1038_s41586-024-08025-4.html"},{"title":"Scalable watermarking for identifying large language model outputs - ADS","url":"https://ui.adsabs.harvard.edu/abs/2024Natur.634..818D/abstract"},{"title":"Scalable watermarking for identifying large language ...","url":"https://europepmc.org/article/med/39443777"}]

Based on the search results, I found the information about the paper "Scalable Watermarking for Identifying Large Language Model Outputs" published in Nature in 2024.

The authors of this paper are Sumanth Dathathri, Abigail See, Sumedh Ghaisas, Po-
…[truncated 582 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_research_bib_complete_20260515T043737",
  "tool": "WebSearch",
  "elapsed_ms": 4
}
```

</details>

---

### Tool call

_source line 81 · 2026-05-15T04:42:11.273419+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "The Curious Decline of Linguistic Diversity Training Language Models on Synthetic Text authors NAACL 2024"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_research_bib_complete_20260515T043737",
  "tool": "WebSearch",
  "tool_args": {
    "query": "The Curious Decline of Linguistic Diversity Training Language Models on Synthetic Text authors NAACL 2024"
  }
}
```

</details>

---

### Tool call

_source line 82 · 2026-05-15T04:42:11.273612+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Detecting Pretraining Data from Large Language Models ICLR 2024 Shi authors full list"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_research_bib_complete_20260515T043737",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Detecting Pretraining Data from Large Language Models ICLR 2024 Shi authors full list"
  }
}
```

</details>

---

### Tool call

_source line 83 · 2026-05-15T04:42:11.273814+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "The Curious Case of Neural Text Degeneration authors Holtzman ICLR 2020"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_research_bib_complete_20260515T043737",
  "tool": "WebSearch",
  "tool_args": {
    "query": "The Curious Case of Neural Text Degeneration authors Holtzman ICLR 2020"
  }
}
```

</details>

---

### Tool call

_source line 84 · 2026-05-15T04:42:11.274031+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Mapping the Increasing Use of LLMs in Scientific Papers arXiv 2404.01268 authors"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_research_bib_complete_20260515T043737",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Mapping the Increasing Use of LLMs in Scientific Papers arXiv 2404.01268 authors"
  }
}
```

</details>

---

### Tool call

_source line 85 · 2026-05-15T04:42:11.274223+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Monitoring AI-Modified Content at Scale Case Study Impact ChatGPT AI Conference Peer Reviews authors ICML 2024 Liang"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_research_bib_complete_20260515T043737",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Monitoring AI-Modified Content at Scale Case Study Impact ChatGPT AI Conference Peer Reviews authors ICML 2024 Liang"
  }
}
```

</details>

---

### Tool call

_source line 86 · 2026-05-15T04:42:11.274430+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Computational Methods in Authorship Attribution Koppel JASIST 2009 authors"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_research_bib_complete_20260515T043737",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Computational Methods in Authorship Attribution Koppel JASIST 2009 authors"
  }
}
```

</details>

---

### Tool call

_source line 87 · 2026-05-15T04:42:11.274647+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Authorship Attribution for Neural Text Generation Uchendu EMNLP 2020 authors"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_research_bib_complete_20260515T043737",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Authorship Attribution for Neural Text Generation Uchendu EMNLP 2020 authors"
  }
}
```

</details>

---

### Tool call

_source line 88 · 2026-05-15T04:42:11.274881+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Automatic Detection of Machine Generated Text Critical Survey COLING 2020 Jawahar authors"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_research_bib_complete_20260515T043737",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Automatic Detection of Machine Generated Text Critical Survey COLING 2020 Jawahar authors"
  }
}
```

</details>

---

### Tool result

_source line 89 · 2026-05-15T04:42:11.275100+00:00_

Web search results for query: "arxiv 2310.05130 Fast-DetectGPT Guangsheng Bao Yanbin Zhao full author list"

Links: [{"title":"[2310.05130] Fast-DetectGPT: Efficient Zero-Shot Detection of Machine-Generated Text via Conditional Probability Curvature","url":"https://arxiv.org/abs/2310.05130"},{"title":"fast-detectgpt: efficient zero-shot detec","url":"https://arxiv.org/pdf/2310.05130"},{"title":"[2310.05130v2] Fast-DetectGPT: Efficient Zero-Shot Detection of Machine-Generated Text via Conditional Probability Curvature","url":"https://arxiv.org/abs/2310.05130v2"},{"title":"Fast-DetectGPT: Efficient Zero-Shot Detection of Machine-Generated Text via Conditional Probability Curvature","url":"https://arxiv.org/html/2310.05130v3"},{"title":"GitHub - baoguangsheng/fast-detect-gpt: Code base for ICLR 2024 \"Fast-DetectGPT: Efficient Zero-Shot Detection of Machine-Generated Text via Conditional Probability Curvature\". · GitHub","url":"https://github.com/baoguangsheng/fast-detect-gpt"},{"title":"Paper page - Fast-DetectGPT: Efficient Zero-Shot Detection of Machine-Generated Text via Conditional Probability Curvature","url":"https://huggingface.co/papers/2310.05130"},{"title":"Google Scholar","url":"https://scholar.google.com/scholar?q=Guangsheng+Bao,+Yanbin+Zhao,+Zhiyang+Teng,+Linyi+Yang,+and+Yue+Zhang.+2024.+Fast-DetectGPT:+Efficient+Zero-Shot+Detection+of+Machine-Generated+Text+via+Conditional+Probability+Curvature.+In+The+Twelfth+International+Conference+on+Learning+Representations.+https://openreview.net/forum?id%3DBpcgcr8E8Z"},{"title":"[PDF] Fast-DetectGPT: Efficient Zero-Shot Detection of Machine-Generated Text via Conditional Probability Curvature | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Fast-DetectGPT:-Efficient-Zero-Shot-Detection-of-Bao-Zhao/85664bb73d09a20f4d3f7aae81143c0f25060fbb"},{"title":"Fast, Interpretable AI-Generated Text Detection Using Style Embeddings","url":"https://web.stanford.edu/class/archive/cs/cs224n/cs224n.1244/final-proj
…[truncated 652 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_research_bib_complete_20260515T043737",
  "tool": "WebSearch",
  "elapsed_ms": 4
}
```

</details>

---

### Tool result

_source line 90 · 2026-05-15T04:42:11.275339+00:00_

Web search results for query: "arxiv 1908.09203 Solaiman Brundage Clark Askell complete author list all authors"

Links: [{"title":"[1908.09203] Release Strategies and the Social Impacts of Language Models","url":"https://arxiv.org/abs/1908.09203"},{"title":"Google Scholar","url":"https://scholar.google.com/scholar?q=Irene+Solaiman%2C+Miles+Brundage%2C+Jack+Clark%2C+Amanda+Askell%2C+Ariel+Herbert-Voss%2C+Jeff+Wu%2C+Alec+Radford%2C+Gretchen+Krueger%2C+Jong+Wook+Kim%2C+Sarah+Kreps%2C+et+al.%2C+2019.+Release+strategies+and+the+social+impacts+of+language+models.+arXiv+preprint+arXiv%3A1908.09203%282019%29."},{"title":"[1908.09203v2] Release Strategies and the Social Impacts of Language Models","url":"https://arxiv.org/abs/1908.09203v2"},{"title":"[1908.09203v1] Release Strategies and the Social Impacts of Language Models","url":"https://arxiv.org/abs/1908.09203v1"},{"title":"[PDF] Release Strategies and the Social Impacts of Language Models | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Release-Strategies-and-the-Social-Impacts-of-Models-Solaiman-Brundage/c7462e0ee928f095a7fc40b91f1e7557d283ae8e"},{"title":"Release Strategies and the Social Impacts of Language ...","url":"https://arxiv.org/pdf/1908.09203"},{"title":"Real-World Gaps in AI Governance Research | SuperIntelligence - Robotics - Safety & Alignment","url":"https://s-rsa.com/index.php/agi/article/view/15163"},{"title":"Amanda Askell email: amanda@askell.io Employment and Professional Roles","url":"https://askell.io/files/Askell-CV.pdf"},{"title":"Release Strategies and the Social Impacts of Language Models | Request PDF","url":"https://www.researchgate.net/publication/335419868_Release_Strategies_and_the_Social_Impacts_of_Language_Models"},{"title":"https://arxiv.org/search/cs?searchtype=author&quer...","url":"https://arxiv.org/search/cs?searchtype=author&query=Solaiman,+I"}]

Based on the search results, the complete author list for arxiv paper 1908.09203 "Release Strategies and the Social Im
…[truncated 358 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_research_bib_complete_20260515T043737",
  "tool": "WebSearch",
  "elapsed_ms": 3
}
```

</details>

---

### Tool result

_source line 91 · 2026-05-15T04:42:11.275583+00:00_

Web search results for query: "Markovian Generation Chains in Large Language Models arXiv 2603.11228 authors"

Links: [{"title":"[2603.11228] Markovian Generation Chains in Large Language Models","url":"https://arxiv.org/abs/2603.11228"},{"title":"Markovian Generation Chains in Large Language Models","url":"https://arxiv.org/html/2603.11228"},{"title":"Large Language Models as Markov Chains","url":"https://arxiv.org/html/2410.02724v1"},{"title":"[2410.02724] Large Language Models as Markov Chains","url":"https://arxiv.org/abs/2410.02724"},{"title":"Markovian Generation Chains in Large Language Models | OpenReview","url":"https://openreview.net/forum?id=nTDn4OMiym"},{"title":"1 Introduction","url":"https://arxiv.org/html/2410.02724v2"},{"title":"[2410.02724v1] Large Language Models as Markov Chains","url":"https://arxiv.org/abs/2410.02724v1"},{"title":"Large Language Models as Markov Chains | OpenReview","url":"https://openreview.net/forum?id=RDFkGZ9Dkh"},{"title":"Additive Multi-Step Markov Chains and the Curse of Dimensionality in Large Language Models","url":"https://arxiv.org/html/2603.04412"},{"title":"[2603.04412] Additive Multi-Step Markov Chains and the Curse of Dimensionality in Large Language Models","url":"https://arxiv.org/abs/2603.04412"}]

Based on the search results, the authors of the arXiv paper 2603.11228 "Markovian Generation Chains in Large Language Models" are Mingmeng Geng, Amr Mohamed, Guokan Shang, Michalis Vazirgiannis, and Thierry Poibeau. The paper was submitted on March 11, 2026.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_research_bib_complete_20260515T043737",
  "tool": "WebSearch",
  "elapsed_ms": 3
}
```

</details>

---

### Tool result

_source line 92 · 2026-05-15T04:42:11.275819+00:00_

Web search results for query: "arxiv 2410.04840 "Strong Model Collapse" Dohmatob Feng complete authors"

Links: [{"title":"[2410.04840] Strong Model Collapse","url":"https://arxiv.org/abs/2410.04840"},{"title":"Strong Model Collapse Elvis Dohmatob1 e.dohmatob@meta.com Yunzhen Feng1,2,∗","url":"https://arxiv.org/pdf/2410.04840"},{"title":"Strong Model Collapse","url":"https://arxiv.org/html/2410.04840.pdf"},{"title":"Strong Model Collapse - ADS","url":"https://ui.adsabs.harvard.edu/abs/2024arXiv241004840D/abstract"},{"title":"Strong Model Collapse | Request PDF","url":"https://www.researchgate.net/publication/384700001_Strong_Model_Collapse"},{"title":"Position: the Stochastic Parrot in the Coal Mine Model Collapse is a Threat to Low-Resource Communities","url":"https://arxiv.org/html/2605.04127"},{"title":"Position: Model Collapse Does Not Mean What You Think","url":"https://arxiv.org/pdf/2503.03150"},{"title":"Elvis Dohmatob on X: \"1/n Introducing our new preprint: Strong Model Collapse https://t.co/spdA6sGtDT, wherein we show that within the \"scaling laws\" paradigm, even 1% bad / synthetic data in the training corpus might lead to model collapse, an eventual critical flattening or even degradation of model https://t.co/ydRtUVe0BT\" / X","url":"https://x.com/dohmatobelvis/status/1844300320811241477"},{"title":"A Closer Look at Model Collapse: From a Generalization-to-Memorization Perspective","url":"https://arxiv.org/html/2509.16499v2"},{"title":"Is Model Collapse Inevitable? Breaking the Curse of","url":"https://arxiv.org/pdf/2404.01413"}]

Based on the search results, the authors of the paper "Strong Model Collapse" (arxiv 2410.04840) are Elvis Dohmatob, Yunzhen Feng, Arjun Subramonian, and Julia Kempe.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_research_bib_complete_20260515T043737",
  "tool": "WebSearch",
  "elapsed_ms": 3
}
```

</details>

---

### Tool result

_source line 93 · 2026-05-15T04:42:11.276061+00:00_

Web search results for query: "LLM as a Broken Telephone Iterative Generation Distorts Information ACL 2025 authors"

Links: [{"title":"LLM as a Broken Telephone: Iterative Generation Distorts Information - ACL Anthology","url":"https://aclanthology.org/2025.acl-long.371/"},{"title":"GitHub - amr-mohamedd/LLM-as-a-Broken-Telephone: [ACL 2025] Code implementation for the \"LLM as a Broken Telephone: Iterative Generation Distorts Information\" paper.","url":"https://github.com/amr-mohamedd/LLM-as-a-Broken-Telephone"},{"title":"[2502.20258] LLM as a Broken Telephone: Iterative Generation Distorts Information","url":"https://arxiv.org/abs/2502.20258"},{"title":"LLM as a Broken Telephone: Iterative Generation Distorts ...","url":"https://aclanthology.org/2025.acl-long.371.pdf"},{"title":"LLM as a Broken Telephone: Iterative Generation Distorts Information","url":"https://arxiv.org/html/2502.20258v1"},{"title":"[Quick Review] LLM as a Broken Telephone: Iterative Generation Distorts Information","url":"https://liner.com/review/llm-as-broken-telephone-iterative-generation-distorts-information"},{"title":"LLM as a Broken Telephone: Iterative Generation Distorts Information | Request PDF","url":"https://www.researchgate.net/publication/394300051_LLM_as_a_Broken_Telephone_Iterative_Generation_Distorts_Information"},{"title":"Accepted Main Conference Papers - ACL 2025","url":"https://2025.aclweb.org/program/main_papers/"},{"title":"Paper page - LLM as a Broken Telephone: Iterative Generation Distorts Information","url":"https://huggingface.co/papers/2502.20258"},{"title":"The Telephone Game for Local LLMs: Quantifying Semantic Drift Across 17 Open-Weight Models in 30-Iteration Paraphrase Chains | Joshua8.AI","url":"https://joshua8.ai/llm-telephone-game-semantic-drift/"}]

Based on the search results, I found the paper you're looking for:

The authors of "LLM as a Broken Telephone: Iterative Generation Distorts Information" are Amr Mohamed, Mingmeng Geng, Michalis Vazirgiannis, 
…[truncated 588 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_research_bib_complete_20260515T043737",
  "tool": "WebSearch",
  "elapsed_ms": 4
}
```

</details>

---

### Tool result

_source line 94 · 2026-05-15T04:42:11.276296+00:00_

Web search results for query: "arxiv 2604.13692 "Xiao Pu" "Zepeng Cheng" "Lin Yuan" full author list"

Links: [{"title":"[2604.13692] Breaking the Generator Barrier: Disentangled Representation for Generalizable AI-Text Detection","url":"https://arxiv.org/abs/2604.13692"},{"title":"[2604.13692v1] Breaking the Generator Barrier: Disentangled Representation for Generalizable AI-Text Detection","url":"https://arxiv.org/abs/2604.13692v1"},{"title":"Computer Science","url":"https://arxiv.org/list/cs/recent?skip=1568&show=1000"},{"title":"Computer Vision and Pattern Recognition May 2025","url":"https://arxiv.org/list/cs.CV/2025-05?skip=2125&show=1000"},{"title":"[2604.04503v1] Memory Intelligence Agent","url":"https://arxiv.org/abs/2604.04503v1"},{"title":"[2604.06566] AI-Driven Research for Databases","url":"https://arxiv.org/abs/2604.06566"},{"title":"Computer Vision and Pattern Recognition Jun 2025","url":"https://arxiv.org/list/cs.CV/2025-06?skip=900&show=2000"},{"title":"[2604.04503v2] Memory Intelligence Agent","url":"https://arxiv.org/abs/2604.04503v2"},{"title":"Computation and Language May 2025","url":"https://www.arxiv.org/list/cs.CL/2025-05?skip=1575&show=1000"},{"title":"Computation and Language Aug 2024","url":"https://www.arxiv.org/list/cs.CL/2024-08?skip=25&show=2000"}]

Based on the search results, the full author list for arxiv paper 2604.13692 is: Xiao Pu, Zepeng Cheng, Lin Yuan, Yu Wu, and Xiuli Bi. The paper is titled "Breaking the Generator Barrier: Disentangled Representation for Generalizable AI-Text Detection" and was submitted on April 15, 2026.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_research_bib_complete_20260515T043737",
  "tool": "WebSearch",
  "elapsed_ms": 5
}
```

</details>

---

### Tool result

_source line 95 · 2026-05-15T04:42:11.276537+00:00_

Web search results for query: "Computational Methods in Authorship Attribution Koppel JASIST 2009 authors"

Links: [{"title":"Computational methods in authorship attribution","url":"https://ideas.repec.org/a/bla/jamist/v60y2009i1p9-26.html"},{"title":"(PDF) Computational Methods in Authorship Attribution","url":"https://www.researchgate.net/publication/220433607_Computational_Methods_in_Authorship_Attribution"},{"title":"Computational methods in authorship attribution - Koppel - 2009 - Journal of the American Society for Information Science and Technology - Wiley Online Library","url":"https://onlinelibrary.wiley.com/doi/abs/10.1002/asi.20961"},{"title":"Computational methods in authorship attribution - Semantic Scholar","url":"https://www.semanticscholar.org/paper/Computational-methods-in-authorship-attribution-Koppel-Schler/c4550ee1f3a1a08c9d2f89e13a7dec7c220c1704"},{"title":"1 Computational Methods in Authorship Attribution","url":"https://u.cs.biu.ac.il/~koppel/papers/authorship-JASIST-final.pdf"},{"title":"Survey of Methods in Computational Literary Studies - 5 What is Authorship Attribution?","url":"https://methods.clsinfra.io/what-author.html"},{"title":"Publications (Chronological) - Prof. Moshe Koppel","url":"https://u.cs.biu.ac.il/~koppel/Publications.html"},{"title":"\"Computational Methods in Authorship Attribution\" by Moshe Koppel, Jonathan Schler et al.","url":"https://touroscholar.touro.edu/president_pubs/275/"},{"title":"(PDF) Computational methods in authorship attribution","url":"https://www.academia.edu/15373725/Computational_methods_in_authorship_attribution"},{"title":"A Comparison of Authorship Attribution Approaches ...","url":"https://annals-csis.org/Volume_11/drp/110.html"}]

Based on the search results, I found the information about the paper "Computational Methods in Authorship Attribution" published in JASIST in 2009.

The authors of "Computational Methods in Authorship Attribution" published in the Journal of the American Society for In
…[truncated 198 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_research_bib_complete_20260515T043737",
  "tool": "WebSearch",
  "elapsed_ms": 2
}
```

</details>

---

### Tool result

_source line 96 · 2026-05-15T04:42:11.276776+00:00_

Web search results for query: "Authorship Attribution for Neural Text Generation Uchendu EMNLP 2020 authors"

Links: [{"title":"Authorship Attribution for Neural Text Generation - ACL Anthology","url":"https://aclanthology.org/2020.emnlp-main.673/"},{"title":"Authorship Attribution for Neural Text Generation (Conference Paper) | NSF PAGES","url":"https://par.nsf.gov/biblio/10212709-authorship-attribution-neural-text-generation"},{"title":"GitHub - AdaUchendu/Authorship-Attribution-for-Neural-Text-Generation · GitHub","url":"https://github.com/AdaUchendu/Authorship-Attribution-for-Neural-Text-Generation"},{"title":"Authorship Attribution for Neural Text Generation | Request PDF","url":"https://www.researchgate.net/publication/347235360_Authorship_Attribution_for_Neural_Text_Generation"},{"title":"Authorship attribution for neural text generation - Penn State","url":"https://pure.psu.edu/en/publications/authorship-attribution-for-neural-text-generation"},{"title":"Authorship Attribution for Neural Text Generation.","url":"https://dblp.org/rec/conf/emnlp/UchenduLSL20.xml"},{"title":"EMNLP2020: Authorship Attribution for Neural Text Generation","url":"https://virtual.2020.emnlp.org/paper_main.125.html"},{"title":"Attribution and Obfuscation of Neural Text Authorship: A Data Mining Perspective | ACM SIGKDD Explorations Newsletter","url":"https://dl.acm.org/doi/10.1145/3606274.3606276"},{"title":"Authorship Attribution for Neural Text Generation Adaku Uchendu Thai Le","url":"https://www.cs.emory.edu/~kshu5/files/emnlp20.pdf"},{"title":"[PDF] Authorship Attribution for Neural Text Generation | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Authorship-Attribution-for-Neural-Text-Generation-Uchendu-Le/9da9cab545bd1534a8c953bb66e611243dcee24d"}]

Based on the web search results, I found the information about the paper "Authorship Attribution for Neural Text Generation" from EMNLP 2020:

The authors of this paper are Adaku Uchendu, Thai Le, Kai Shu, and Dongwon
…[truncated 252 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_research_bib_complete_20260515T043737",
  "tool": "WebSearch",
  "elapsed_ms": 2
}
```

</details>

---

### Tool result

_source line 97 · 2026-05-15T04:42:11.276967+00:00_

Web search results for query: "Mapping the Increasing Use of LLMs in Scientific Papers arXiv 2404.01268 authors"

Links: [{"title":"[2404.01268] Mapping the Increasing Use of LLMs in Scientific Papers","url":"https://arxiv.org/abs/2404.01268"},{"title":"Mapping the Increasing Use of LLMs in Scientific Papers","url":"https://arxiv.org/html/2404.01268v1"},{"title":"Preprint Mapping the Increasing Use of LLMs in Scientific Papers","url":"https://arxiv.org/pdf/2404.01268"},{"title":"Mapping the Increasing Use of LLMs in Scientific Papers | BibSonomy","url":"https://www.bibsonomy.org/bibtex/28f3ef49cf074d7caa6cdd244449c11cf/diekhans"},{"title":"Mapping the Increasing Use of LLMs in Scientific Papers | alphaXiv","url":"https://www.alphaxiv.org/abs/2404.01268"},{"title":"Mapping the Increasing Use of LLMs in Scientific Papers","url":"https://www.emergentmind.com/papers/2404.01268"},{"title":"GitHub - Weixin-Liang/Mapping-the-Increasing-Use-of-LLMs-in-Scientific-Papers · GitHub","url":"https://github.com/Weixin-Liang/Mapping-the-Increasing-Use-of-LLMs-in-Scientific-Papers"},{"title":"ArxivBench: Can LLMs Assist Researchers in Conducting Research?","url":"https://arxiv.org/html/2504.10496v1"},{"title":"How much are LLMs changing the language of academic papers after ChatGPT? A multi-database and full text analysis | Scientometrics | Springer Nature Link","url":"https://link.springer.com/article/10.1007/s11192-026-05601-5"},{"title":"Mapping the Increasing Use of LLMs in Scientific Papers | OpenReview","url":"https://openreview.net/forum?id=YX7QnhxESU"}]

I've found the paper and its authors. Here are the results:

## Paper Details

**Title:** Mapping the Increasing Use of LLMs in Scientific Papers

**arXiv ID:** 2404.01268

**Submission Date:** April 1, 2024

## Authors

The paper has 14 authors: Weixin Liang, Yaohui Zhang, Zhengxuan Wu, Haley Lepp, Wenlong Ji, Xuandong Zhao, Hancheng Cao, Sheng Liu, Siyu He, Zhi Huang, Diyi Yang, Christopher Potts, Christopher D Manning, an
…[truncated 456 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_research_bib_complete_20260515T043737",
  "tool": "WebSearch",
  "elapsed_ms": 2
}
```

</details>

---

### Tool call

_source line 98 · 2026-05-15T04:42:11.277196+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "arxiv 2605.01647 Narayanasamy Agrawal Faber Alam \"Beyond Perplexity\" 2026 author names"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_research_bib_complete_20260515T043737",
  "tool": "WebSearch",
  "tool_args": {
    "query": "arxiv 2605.01647 Narayanasamy Agrawal Faber Alam \"Beyond Perplexity\" 2026 author names"
  }
}
```

</details>

---

### Tool result

_source line 99 · 2026-05-15T04:42:11.277413+00:00_

Web search results for query: "Monitoring AI-Modified Content at Scale Case Study Impact ChatGPT AI Conference Peer Reviews authors ICML 2024 Liang"

Links: [{"title":"[2403.07183] Monitoring AI-Modified Content at Scale: A Case Study on the Impact of ChatGPT on AI Conference Peer Reviews","url":"https://arxiv.org/abs/2403.07183"},{"title":"Monitoring AI-Modified Content at Scale: A Case Study on the Impact of ChatGPT on AI Conference Peer Reviews","url":"https://proceedings.mlr.press/v235/liang24b.html"},{"title":"Monitoring AI-modified content at scale | Proceedings of the 41st International Conference on Machine Learning","url":"https://dl.acm.org/doi/10.5555/3692070.3693262"},{"title":"[PDF] Monitoring AI-Modified Content at Scale: A Case Study on the Impact of ChatGPT on AI Conference Peer Reviews | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Monitoring-AI-Modified-Content-at-Scale:-A-Case-on-Liang-Izzo/023e113b11ff7bac182713a069fedcbcccad9562"},{"title":"Monitoring AI-Modified Content at Scale: A Case Study on the Impact of ChatGPT on AI Conference Peer Reviews","url":"https://arxiv.org/html/2403.07183v2"},{"title":"Monitoring AI-Modified Content at Scale: A Case Study on the ...","url":"http://lingjiaochen.com/papers/2024_MonitoringAIContent_ICML.pdf"},{"title":"Monitoring AI-Modified Content at Scale: A Case Study on ...","url":"https://arxiv.org/pdf/2403.07183"},{"title":"Monitoring AI-Modified Content at Scale: A Case Study on the Impact of ChatGPT on AI Conference Peer Reviews | alphaXiv","url":"https://www.alphaxiv.org/resources/2403.07183v2"},{"title":"ICML 2024 Monitoring AI-Modified Content at Scale: A Case Study on the Impact of ChatGPT on AI Conference Peer Reviews Oral","url":"https://icml.cc/virtual/2024/oral/35507"},{"title":"[2403.07183v2] Monitoring AI-Modified Content at Scale: A Case Study on the Impact of ChatGPT on AI Conference Peer Reviews","url":"https://arxiv.org/abs/2403.07183v2"}]

I found the paper you're looking f
…[truncated 1583 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_research_bib_complete_20260515T043737",
  "tool": "WebSearch",
  "elapsed_ms": 3
}
```

</details>

---

### Tool result

_source line 100 · 2026-05-15T04:42:11.277693+00:00_

Web search results for query: "Automatic Detection of Machine Generated Text Critical Survey COLING 2020 Jawahar authors"

Links: [{"title":"Automatic Detection of Machine Generated Text: A Critical Survey - ACL Anthology","url":"https://aclanthology.org/2020.coling-main.208/"},{"title":"GitHub - UBC-NLP/coling2020_machine_generated_text: Automatic Detection of Machine Generated Text: A Critical Survey","url":"https://github.com/UBC-NLP/coling2020_machine_generated_text"},{"title":"Automatic Detection of Machine Generated Text: A Critical Survey | Request PDF","url":"https://www.researchgate.net/publication/348344789_Automatic_Detection_of_Machine_Generated_Text_A_Critical_Survey"},{"title":"Automatic Detection of Machine Generated Text: A Critical ...","url":"https://aclanthology.org/2020.coling-main.208.pdf"},{"title":"[PDF] Automatic Detection of Machine Generated Text: A Critical Survey | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Automatic-Detection-of-Machine-Generated-Text:-A-Jawahar-Abdul-Mageed/9438bc5626b2d9a771cecc7a41ecabf6639db53c"},{"title":"Table 2 from Automatic Detection of Machine Generated Text: A Critical Survey | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Automatic-Detection-of-Machine-Generated-Text:-A-Jawahar-Abdul-Mageed/9438bc5626b2d9a771cecc7a41ecabf6639db53c/figure/2"},{"title":"Table 1 from Automatic Detection of Machine Generated Text: A Critical Survey | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Automatic-Detection-of-Machine-Generated-Text:-A-Jawahar-Abdul-Mageed/9438bc5626b2d9a771cecc7a41ecabf6639db53c/figure/0"},{"title":"Figure 1 from Automatic Detection of Machine Generated Text: A Critical Survey | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Automatic-Detection-of-Machine-Generated-Text:-A-Jawahar-Abdul-Mageed/9438bc5626b2d9a771cecc7a41ecabf6639db53c/figure/1"},{"title":"[2011.01314] Automatic Detection of Machine Generated Text: A Critical Survey","ur
…[truncated 1344 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_research_bib_complete_20260515T043737",
  "tool": "WebSearch",
  "elapsed_ms": 2
}
```

</details>

---

### Tool result

_source line 101 · 2026-05-15T04:42:11.277953+00:00_

Web search results for query: "The Curious Decline of Linguistic Diversity Training Language Models on Synthetic Text authors NAACL 2024"

Links: [{"title":"The Curious Decline of Linguistic Diversity: Training Language Models on Synthetic Text - ACL Anthology","url":"https://aclanthology.org/2024.findings-naacl.228/"},{"title":"The Curious Decline of Linguistic Diversity: Training Language Models on Synthetic Text - Archive ouverte HAL","url":"https://hal.science/hal-04593399v1"},{"title":"(PDF) The Curious Decline of Linguistic Diversity: Training Language Models on Synthetic Text","url":"https://www.researchgate.net/publication/382631840_The_Curious_Decline_of_Linguistic_Diversity_Training_Language_Models_on_Synthetic_Text"},{"title":"The Curious Decline of Linguistic Diversity: Training Language Models on Synthetic Text - ADS","url":"https://ui.adsabs.harvard.edu/abs/2023arXiv231109807G/abstract"},{"title":"[2311.09807] The Curious Decline of Linguistic Diversity: Training Language Models on Synthetic Text","url":"https://arxiv.org/abs/2311.09807"},{"title":"The Curious Decline of Linguistic Diversity: Training Language Models on Synthetic Text","url":"https://arxiv.org/html/2311.09807v2"},{"title":"[PDF] The Curious Decline of Linguistic Diversity: Training Language Models on Synthetic Text | Semantic Scholar","url":"https://www.semanticscholar.org/paper/The-Curious-Decline-of-Linguistic-Diversity:-Models-Guo-Shang/7d5ea474aa1cf732bb1d00faa07a5bb2c9119cfd"},{"title":"The Curious Decline of Linguistic Diversity: Training Language Models on Synthetic Text - Laboratoire d'informatique de l'X (LIX)","url":"https://dumas.ccsd.cnrs.fr/X-LIX/hal-04593399v1"},{"title":"Google Scholar","url":"https://scholar.google.com/scholar?q=The+Curious+Decline+of+Linguistic+Diversity:+Training+Language+Models+on+Synthetic+Text."},{"title":"The Curious Decline of Linguistic Diversity:","url":"https://arxiv.org/pdf/2311.09807"}]

I found the paper you're looking for. Here's the infor
…[truncated 1225 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_research_bib_complete_20260515T043737",
  "tool": "WebSearch",
  "elapsed_ms": 4
}
```

</details>

---

### Tool result

_source line 102 · 2026-05-15T04:42:11.278210+00:00_

Web search results for query: "Detecting Pretraining Data from Large Language Models ICLR 2024 Shi authors full list"

Links: [{"title":"[2310.16789] Detecting Pretraining Data from Large Language Models","url":"https://arxiv.org/abs/2310.16789"},{"title":"Detecting Pretraining Data from Large Language Models | OpenReview","url":"https://openreview.net/forum?id=zWqr3MQuNs"},{"title":"DETECTING PRETRAINING DATA FROM LARGE LANGUAGE MODELS - Princeton University","url":"https://collaborate.princeton.edu/en/publications/detecting-pretraining-data-from-large-language-models/"},{"title":"Detecting Pretraining Data from Large Language Models","url":"https://swj0419.github.io/detect-pretrain.github.io/"},{"title":"Detecting Pretraining Data from Large Language Models","url":"https://arxiv.org/html/2310.16789v3"},{"title":"DETECTING PRETRAINING DATA FROM LARGE LAN","url":"https://openreview.net/pdf?id=zWqr3MQuNs"},{"title":"Pretraining Data Detection for Large Language Models","url":"https://aclanthology.org/2024.emnlp-main.300.pdf"},{"title":"[2404.02936] Min-K%++: Improved Baseline for Detecting Pre-Training Data from Large Language Models","url":"https://arxiv.org/abs/2404.02936"},{"title":"Min-K%++: Improved Baseline for Detecting Pre-Training Data from Large Language Models","url":"https://arxiv.org/html/2404.02936v1"},{"title":"GitHub - swj0419/detect-pretrain-code: This repository provides an original implementation of Detecting Pretraining Data from Large Language Models by *Weijia Shi, *Anirudh Ajith, Mengzhou Xia, Yangsibo Huang, Daogao Liu , Terra Blevins , Danqi Chen , Luke Zettlemoyer. · GitHub","url":"https://github.com/swj0419/detect-pretrain-code"}]

Based on the search results, I found the paper "Detecting Pretraining Data from Large Language Models" presented at ICLR 2024. Here is the full list of authors:

Weijia Shi, Anirudh Ajith, Mengzhou Xia, Yangsibo Huang, Daogao Liu, Terra Blevins, Danqi Chen, and Luke Zettlemoyer

The authors are from University of
…[truncated 201 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_research_bib_complete_20260515T043737",
  "tool": "WebSearch",
  "elapsed_ms": 4
}
```

</details>

---

### Tool result

_source line 103 · 2026-05-15T04:42:11.278474+00:00_

Web search results for query: "Chainwash Multi-Step Rewriting Attacks Diffusion Language Model Watermarks Ameen arXiv 2605.05503 2026 authors"

Links: [{"title":"[2605.05503] Chainwash: Multi-Step Rewriting Attacks on Diffusion Language Model Watermarks","url":"https://arxiv.org/abs/2605.05503"},{"title":"Chainwash: Multi-Step Rewriting Attacks on Diffusion Language Model Watermarks","url":"https://arxiv.org/html/2605.05503"},{"title":"Computation and Language","url":"https://arxiv.org/list/cs.CL/new"},{"title":"Watermarking Diffusion Language Models","url":"https://arxiv.org/pdf/2509.24368"},{"title":"Watermarking Language Models through Language Models","url":"https://arxiv.org/html/2411.05091v2"},{"title":"Watermark Smoothing Attacks against Language Models","url":"https://aclanthology.org/2025.findings-emnlp.264.pdf"},{"title":"Unified attacks to large language model watermarks: spoofing and scrubbing in unauthorized knowledge distillation","url":"https://arxiv.org/html/2504.17480"},{"title":"Unified attacks to large language model watermarks: Spoofing and scrubbing in unauthorized knowledge distillation - ScienceDirect","url":"https://www.sciencedirect.com/science/article/abs/pii/S095070512501336X"},{"title":"Breaking Semantic-Aware Watermarks via LLM-Guided Coherence-Preserving Semantic Injection","url":"https://arxiv.org/html/2602.21593"},{"title":"Publicly-Detectable Watermarking for Language Models","url":"https://eprint.iacr.org/2023/1661.pdf"}]

Based on the search results, I found the paper you're looking for. Here's the information about it:

## Chainwash: Multi-Step Rewriting Attacks on Diffusion Language Model Watermarks

The paper is by Mohd Ruhul Ameen and 3 other authors. The complete author list includes Mohd Ruhul Ameen, Akif Islam, Nadim Mahmud, and Md. Ekramul Hamid.

**arXiv ID:** 2605.05503

**Key Findings:**

The paper addresses watermarking in diffusion language models, which generate text by denoising tokens in arbitrary order, making exis
…[truncated 877 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_research_bib_complete_20260515T043737",
  "tool": "WebSearch",
  "elapsed_ms": 8
}
```

</details>

---

### Tool result

_source line 104 · 2026-05-15T04:42:11.278738+00:00_

Web search results for query: "arxiv 2605.03969 "Mohamed Mady" "Johannes Reschke" "Björn Schuller" full author list"

Links: [{"title":"[2605.03969] Feature-Augmented Transformers for Robust AI-Text Detection Across Domains and Generators","url":"https://arxiv.org/abs/2605.03969"},{"title":"Feature-Augmented Transformers for Robust AI-Text Detection Across Domains and Generators","url":"https://arxiv.org/html/2605.03969"},{"title":"[2605.10602] Inherent Altermagnetism on regular hyperbolic lattices","url":"https://arxiv.org/abs/2605.10602"},{"title":"[2601.12591] SmoothCLAP: Soft-Target Enhanced Contrastive Language\\--Audio Pretraining for Affective Computing","url":"https://arxiv.org/abs/2601.12591"},{"title":"[1307.6170] 6th International Symposium on Attention in Cognitive Systems 2013","url":"https://arxiv.org/abs/1307.6170"},{"title":"[2605.01162] Propagation Mechanism-Aware Near-Field Spatially Non-Stationary Channel Estimation and Environment Mapping","url":"https://arxiv.org/abs/2605.01162"},{"title":"[2102.09150] An Enhanced Adversarial Network with Combined Latent Features for Spatio-Temporal Facial Affect Estimation in the Wild","url":"https://arxiv.org/abs/2102.09150"},{"title":"[2605.09013] Semantic Communication for Multi-Satellite Massive MIMO Transmission: A Mixture of Cooperative Modes Framework","url":"https://arxiv.org/abs/2605.09013"},{"title":"[2109.08049v1] A Machine Learning Framework for Automatic Prediction of Human Semen Motility","url":"https://arxiv.org/abs/2109.08049v1"},{"title":"[2603.27377] Non-Unitary Quantum Machine Learning: Fisher Efficiency Transitions from Distributed Quantum Expressivity","url":"https://arxiv.org/abs/2603.27377"}]

Based on the search results, the paper arXiv:2605.03969 titled "Feature-Augmented Transformers for Robust AI-Text Detection Across Domains and Generators" has authors Mohamed Mady, Johannes Reschke, and Björn Schuller. The search results indicate these are the three authors of the paper, with the ab
…[truncated 160 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_research_bib_complete_20260515T043737",
  "tool": "WebSearch",
  "elapsed_ms": 7
}
```

</details>

---

### Tool result

_source line 105 · 2026-05-15T04:42:11.279024+00:00_

Web search results for query: "The Curious Case of Neural Text Degeneration authors Holtzman ICLR 2020"

Links: [{"title":"[1904.09751] The Curious Case of Neural Text Degeneration","url":"https://arxiv.org/abs/1904.09751"},{"title":"ICLR: The Curious Case of Neural Text Degeneration","url":"https://iclr.cc/virtual_2020/poster_rygGQyrFvH.html"},{"title":"THE CURIOUS CASE OF NEURAL TEXT DeGENERATION","url":"https://openreview.net/pdf?id=rygGQyrFvH"},{"title":"The Curious Case of Neural Text Degeneration","url":"https://www.researchgate.net/publication/332590110_The_Curious_Case_of_Neural_Text_Degeneration"},{"title":"dblp: The Curious Case of Neural Text Degeneration.","url":"https://dblp.org/rec/conf/iclr/HoltzmanBDFC20.html"},{"title":"[Paper Note] The Curious Case of Neural Text Degeneration, Ari Holtzman+, ICLR'20 · Issue #1889 · AkihikoWatanabe/paper_notes","url":"https://github.com/AkihikoWatanabe/paper_notes/issues/1889"},{"title":"[1904.09751] The Curious Case of Neural Text Degeneration","url":"https://ar5iv.labs.arxiv.org/html/1904.09751"},{"title":"The Curious Case of Neural Text Degeneration - UCT Computer Science Research Document Archive","url":"https://pubs.cs.uct.ac.za/id/eprint/1407/"},{"title":"CLOSING THE CURIOUS CASE OF NEURAL TEXT DEGENERATION Matthew Finlayson∗","url":"https://proceedings.iclr.cc/paper_files/paper/2024/file/34899013589ef41aea4d7b2f0ef310c1-Paper-Conference.pdf"},{"title":"The Curious Case of Neural Text Degeneration | OpenReview","url":"https://openreview.net/forum?id=rygGQyrFvH"}]

Based on the search results, here's the information about "The Curious Case of Neural Text Degeneration":

## Authors

The paper was authored by Ari Holtzman, Jan Buys, Li Du, Maxwell Forbes, and Yejin Choi, with affiliations at the Paul G. Allen School of Computer Science & Engineering at the University of Washington, the Allen Institute for Artificial Intelligence, and the Department of Computer Science at the University of Cape Town.

## Publicati
…[truncated 962 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_research_bib_complete_20260515T043737",
  "tool": "WebSearch",
  "elapsed_ms": 5
}
```

</details>

---

### Tool call

_source line 106 · 2026-05-15T04:42:11.279286+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "arxiv 2502.20258 \"LLM as a Broken Telephone\" full author list"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_research_bib_complete_20260515T043737",
  "tool": "WebSearch",
  "tool_args": {
    "query": "arxiv 2502.20258 \"LLM as a Broken Telephone\" full author list"
  }
}
```

</details>

---

### Tool result

_source line 107 · 2026-05-15T04:42:11.279521+00:00_

Web search results for query: "arxiv 2605.01647 Narayanasamy Agrawal Faber Alam "Beyond Perplexity" 2026 author names"

Links: [{"title":"[2605.01647] Beyond Perplexity: Character Distribution Signatures and the MDTA Benchmark for AI Text Detection","url":"https://arxiv.org/abs/2605.01647"},{"title":"[2605.01647v1] Beyond Perplexity: Character Distribution Signatures and the MDTA Benchmark for AI Text Detection","url":"https://arxiv.org/abs/2605.01647v1"},{"title":"Beyond Perplexity: Character Distribution Signatures and the MDTA Benchmark for AI Text Detection - ADS","url":"https://ui.adsabs.harvard.edu/abs/2026arXiv260501647N/abstract"},{"title":"[2605.13652] Beyond Perplexity: A Geometric and Spectral Study of Low-Rank Pre-Training","url":"https://arxiv.org/abs/2605.13652"},{"title":"Beyond Perplexity: Character Distribution Signatures and the MDTA Benchmark for AI Text Detection","url":"https://arxiv.org/html/2605.01647"},{"title":"Beyond Perplexity: A Geometric and Spectral Study of Low-Rank Pre-Training","url":"https://arxiv.org/html/2605.13652"},{"title":"(PDF) Beyond Perplexity: A Lightweight Benchmark for Knowledge Retention in Supervised Fine-Tuning","url":"https://www.researchgate.net/publication/399559297_Beyond_Perplexity_A_Lightweight_Benchmark_for_Knowledge_Retention_in_Supervised_Fine-Tuning"},{"title":"[2601.03505] Beyond Perplexity: A Lightweight Benchmark for Knowledge Retention in Supervised Fine-Tuning","url":"https://arxiv.org/abs/2601.03505"},{"title":"Beyond Perplexity: A Lightweight Benchmark for Knowledge Retention in Supervised Fine-Tuning","url":"https://arxiv.org/html/2601.03505"},{"title":"From Entropy to Epiplexity: Rethinking Information for Computationally Bounded Intelligence","url":"https://arxiv.org/html/2601.03220v1"}]

Based on the search results, the authors of arxiv 2605.01647 "Beyond Perplexity: Character Distribution Signatures and the MDTA Benchmark for AI Text Detection" are Priyadarshan Narayanasamy, Swastik Agrawal, Klin
…[truncated 284 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_research_bib_complete_20260515T043737",
  "tool": "WebSearch",
  "elapsed_ms": 2
}
```

</details>

---

### Tool call

_source line 108 · 2026-05-15T04:42:11.279802+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "arxiv 2402.09739 QuRating authors full list"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_research_bib_complete_20260515T043737",
  "tool": "WebSearch",
  "tool_args": {
    "query": "arxiv 2402.09739 QuRating authors full list"
  }
}
```

</details>

---

### Tool call

_source line 109 · 2026-05-15T04:42:11.280029+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "arxiv 2605.05503 Chainwash authors full list"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_research_bib_complete_20260515T043737",
  "tool": "WebSearch",
  "tool_args": {
    "query": "arxiv 2605.05503 Chainwash authors full list"
  }
}
```

</details>

---

### Tool call

_source line 110 · 2026-05-15T04:42:11.280252+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "arxiv 2603.11228 \"Markovian Generation Chains\" Geng Mohamed Shang Vazirgiannis Poibeau authors"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_research_bib_complete_20260515T043737",
  "tool": "WebSearch",
  "tool_args": {
    "query": "arxiv 2603.11228 \"Markovian Generation Chains\" Geng Mohamed Shang Vazirgiannis Poibeau authors"
  }
}
```

</details>

---

### Tool result

_source line 111 · 2026-05-15T04:42:11.280454+00:00_

Web search results for query: "arxiv 2502.20258 "LLM as a Broken Telephone" full author list"

Links: [{"title":"[2502.20258] LLM as a Broken Telephone: Iterative Generation Distorts Information","url":"https://arxiv.org/abs/2502.20258"},{"title":"LLM as a Broken Telephone: Iterative Generation Distorts Information","url":"https://arxiv.org/html/2502.20258"},{"title":"Paper page - LLM as a Broken Telephone: Iterative Generation Distorts Information","url":"https://huggingface.co/papers/2502.20258"},{"title":"LLM as a Broken Telephone: Iterative Generation Distorts Information | alphaXiv","url":"https://www.alphaxiv.org/overview/2502.20258v1"},{"title":"dblp: LLM as a Broken Telephone: Iterative Generation Distorts Information.","url":"https://dblp.org/rec/journals/corr/abs-2502-20258.html"},{"title":"GitHub - amr-mohamedd/LLM-as-a-Broken-Telephone: [ACL 2025] Code implementation for the \"LLM as a Broken Telephone: Iterative Generation Distorts Information\" paper.","url":"https://github.com/amr-mohamedd/LLM-as-a-Broken-Telephone"},{"title":"Computer Science Feb 2025","url":"https://arxiv.org/list/cs/2025-02?skip=10175&show=2000"},{"title":"Computation and Language Feb 2025","url":"https://www.arxiv.org/list/cs.CL/2025-02?skip=1700&show=50"},{"title":"LLM as a Broken Telephone: Iterative Generation Distorts Information - ACL Anthology","url":"https://aclanthology.org/2025.acl-long.371/"},{"title":"LLM as a Broken Telephone: Iterative Generation Distorts Information | Request PDF","url":"https://www.researchgate.net/publication/394300051_LLM_as_a_Broken_Telephone_Iterative_Generation_Distorts_Information"}]

Based on the search results, the full author list for the paper "LLM as a Broken Telephone: Iterative Generation Distorts Information" (arxiv 2502.20258) is: Amr Mohamed, Mingmeng Geng, Michalis Vazirgiannis, and Guokan Shang.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_research_bib_complete_20260515T043737",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool call

_source line 112 · 2026-05-15T04:42:11.280706+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "arxiv 2404.01268 Weixin Liang Yaohui Zhang full author list bibtex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_research_bib_complete_20260515T043737",
  "tool": "WebSearch",
  "tool_args": {
    "query": "arxiv 2404.01268 Weixin Liang Yaohui Zhang full author list bibtex"
  }
}
```

</details>

---

### Tool result

_source line 113 · 2026-05-15T04:42:11.280926+00:00_

Web search results for query: "arxiv 2402.09739 QuRating authors full list"

Links: [{"title":"[2402.09739] QuRating: Selecting High-Quality Data for Training Language Models","url":"https://arxiv.org/abs/2402.09739"},{"title":"[2402.09739] QuRating: Selecting High-Quality Data for Training Language Models","url":"https://ar5iv.labs.arxiv.org/html/2402.09739"},{"title":"QuRating: Selecting High-Quality Data for Training Language Models","url":"https://arxiv.org/pdf/2402.09739"},{"title":"[2402.09739v3] QuRating: Selecting High-Quality Data for Training Language Models","url":"https://arxiv.org/abs/2402.09739v3"},{"title":"QuRating: Selecting High-Quality Data for Training Language Models - ADS","url":"https://ui.adsabs.harvard.edu/abs/2024arXiv240209739W/abstract"},{"title":"princeton-nlp/QuRating-GPT3.5-Judgments-Test · Datasets at Hugging Face","url":"https://huggingface.co/datasets/princeton-nlp/QuRating-GPT3.5-Judgments-Test"},{"title":"Paper page - QuRating: Selecting High-Quality Data for Training Language Models","url":"https://huggingface.co/papers/2402.09739"},{"title":"princeton-nlp/QuRater-1.3B · Hugging Face","url":"https://huggingface.co/princeton-nlp/QuRater-1.3B"},{"title":"Bohrium | AI for Science with Global Scientists","url":"https://www.bohrium.com/paper/arxiv/2402.09739"},{"title":"GitHub - princeton-nlp/QuRating: [ICML 2024] Selecting High-Quality Data for Training Language Models","url":"https://github.com/princeton-nlp/qurating"}]

Based on the search results, the authors of the QuRating paper (arXiv:2402.09739) are Alexander Wettig, Aatmik Gupta, Saumya Malik, and Danqi Chen.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_research_bib_complete_20260515T043737",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool call

_source line 114 · 2026-05-15T04:42:11.281166+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "site:proceedings.mlr.press \"Monitoring AI-Modified Content at Scale\" Liang Izzo bibtex author list"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_research_bib_complete_20260515T043737",
  "tool": "WebSearch",
  "tool_args": {
    "query": "site:proceedings.mlr.press \"Monitoring AI-Modified Content at Scale\" Liang Izzo bibtex author list"
  }
}
```

</details>

---

### Tool call

_source line 115 · 2026-05-15T04:42:11.281387+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "site:neurips.cc \"Intrinsic Dimension Estimation\" Tulchinskii Kuznetsov Kushnareva Cherniavskii full author list 2023"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_research_bib_complete_20260515T043737",
  "tool": "WebSearch",
  "tool_args": {
    "query": "site:neurips.cc \"Intrinsic Dimension Estimation\" Tulchinskii Kuznetsov Kushnareva Cherniavskii full author list 2023"
  }
}
```

</details>

---

### Tool result

_source line 116 · 2026-05-15T04:42:11.281630+00:00_

Web search results for query: "arxiv 2605.05503 Chainwash authors full list"

Links: [{"title":"[2605.05503] Chainwash: Multi-Step Rewriting Attacks on Diffusion Language Model Watermarks","url":"https://arxiv.org/abs/2605.05503"},{"title":"Chainwash: Multi-Step Rewriting Attacks on Diffusion Language Model Watermarks","url":"https://arxiv.org/html/2605.05503"},{"title":"Computation and Language","url":"https://arxiv.org/list/cs.CL/new"},{"title":"Combining pre-trained models via localized model averagingThe authors are listed in alphabetical order and recognized as co-first authors.","url":"https://arxiv.org/html/2605.13421"},{"title":"Arxiv","url":"https://arxiv.org/pdf/2310.05503"},{"title":"An improved double-exponential lower bound for 𝑟₄⁢(5,𝑛)After submitting the manuscript to arXiv.org, the first and third authors learned that the second and fourth authors, as well as Longma Du, Xinyu Hu, Ruilong Liu, and Guanghui Wang, had independently obtained the same result. Following discussions, the authors decided to write a joint paper. The current manuscript is mainly based on the original version by the first and third authors.","url":"https://arxiv.org/html/2605.04105"},{"title":"Computer Science","url":"https://arxiv.org/list/cs/recent?skip=1408&show=2000"},{"title":"[2106.05503] Panel Data with Unknown Clusters","url":"https://arxiv.org/abs/2106.05503"},{"title":"[2602.05503] Repairing Property Graphs under PG-Constraints","url":"https://arxiv.org/abs/2602.05503"},{"title":"arXiv.org e-Print archive","url":"https://arxiv.org/"}]

Based on the search results, the full list of authors for arxiv paper 2605.05503 "Chainwash: Multi-Step Rewriting Attacks on Diffusion Language Model Watermarks" is:

1. Mohd Ruhul Ameen (College of Engineering and Computer Science, Marshall University, Huntington, WV, USA)
2. Akif Islam (Department of Computer Science and Engineering, University of Rajshahi, Rajshahi, Bangladesh)
3. Nadim Mahmud (Miami University, Oxford, OH)
4. Md. Ek
…[truncated 209 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_research_bib_complete_20260515T043737",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 117 · 2026-05-15T04:42:11.281892+00:00_

Web search results for query: "arxiv 2603.11228 "Markovian Generation Chains" Geng Mohamed Shang Vazirgiannis Poibeau authors"

Links: [{"title":"[2603.11228] Markovian Generation Chains in Large Language Models","url":"https://arxiv.org/abs/2603.11228"},{"title":"Markovian Generation Chains in Large Language Models","url":"https://arxiv.org/html/2603.11228"},{"title":"Markovian Generation Chains in Large Language Models | OpenReview","url":"https://openreview.net/forum?id=nTDn4OMiym"},{"title":"Dressed-state master equation for two strongly coupled two-level atoms with long-lived entanglement","url":"https://arxiv.org/html/2603.22238"},{"title":"[2001.02183] Markov chains revisited","url":"https://arxiv.org/abs/2001.02183"},{"title":"1 Introduction","url":"https://arxiv.org/html/2410.02724v2"},{"title":"(PDF) GSNs : Generative Stochastic Networks","url":"https://www.researchgate.net/publication/273788029_GSNs_Generative_Stochastic_Networks"},{"title":"Large Language Models as Markov Chains","url":"https://arxiv.org/html/2410.02724v1"},{"title":"Markov chain - Wikipedia","url":"https://en.wikipedia.org/wiki/Markov_chain"},{"title":"arXiv:2012.07152v1 [cs.PF] 13 Dec 2020 On Non-Markovian Performance Models","url":"https://arxiv.org/pdf/2012.07152"}]

Based on the search results, I found the paper you're looking for. Here are the key details:

**Paper Title:** Markovian Generation Chains in Large Language Models

**arXiv ID:** 2603.11228

**Authors:** Mingmeng Geng, Amr Mohamed, Guokan Shang, Michalis Vazirgiannis, and Thierry Poibeau

**Publication Date:** March 11, 2026

**Key Concept:** The paper defines an iterative inference process as Markovian generation chains, where each step takes a specific prompt template and the previous output as input, without including any prior memory.

**Main Findings:** In iterative rephrasing and round-trip translation experiments, the output either converges to a small recurrent set or continues to produce novel sentences over a f
…[truncated 515 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_research_bib_complete_20260515T043737",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 118 · 2026-05-15T04:42:11.282187+00:00_

Here are the complete author lists in BibTeX format:

**1. Defending Against Neural Fake News (NeurIPS 2019)**
```
author = {Zellers, Rowan and Holtzman, Ari and Rashkin, Hannah and Bisk, Yonatan and Farhadi, Ali and Roesner, Franziska and Choi, Yejin}
```

**2. Release Strategies and the Social Impacts of Language Models (arXiv 1908.09203, 2019)**
```
author = {Solaiman, Irene and Brundage, Miles and Clark, Jack and Askell, Amanda and Herbert-Voss, Ariel and Wu, Jeff and Radford, Alec and Krueger, Gretchen and Kim, Jong Wook and Kreps, Sarah and McCain, Miles and Newhouse, Alex and Blazakis, Jason and McGuffie, Kris and Wang, Jasmine}
```

**3. Self-Consuming Generative Models Go MAD (arXiv 2307.01850, 2023)**
```
author = {Alemohammad, Sina and Casco-Rodriguez, Josue and Luzi, Lorenzo and Humayun, Ahmed Imtiaz and Babaei, Hossein and LeJeune, Daniel and Siahkoohi, Ali and Baraniuk, Richard G.}
```

**4. The Curse of Recursion: Training on Generated Data Makes Models Forget (Nature 2024)**
```
author = {Shumailov, Ilia and Shumaylov, Zakhar and Zhao, Yiren and Gal, Yarin and Papernot, Nicolas and Anderson, Ross}
```

**5. Strong Model Collapse (ICLR 2025, not 2024 as stated)**
```
author = {Dohmatob, Elvis and Feng, Yunzhen and Subramonian, Arjun and Kempe, Julia}
```

**6. Is Model Collapse Inevitable? Breaking the Curse of Recursion by Accumulating Real and Synthetic Data (arXiv 2404.01413, 2024)**
```
author = {Gerstgrasser, Matthias and Schaeffer, Rylan and Dey, Apratim and Rafailov, Rafael and Sleight, Henry and Hughes, John and Korbak, Tomasz and Agrawal, Rajashree and Pai, Dhruv and Gromov, Andrey and Roberts, Daniel A. and Yang, Diyi and Donoho, David L. and Koyejo, Sanmi}
```

Note on paper 5: "Strong Model Collapse" was published at ICLR 2025, not ICLR 2024.

Sources:
- [Defending Against Neural Fake News - arXiv](https://arxiv.org/abs/1905.12616)
- [Release Strategies and the Social Impacts of Language Models - arXiv](https://arxiv.org/abs/1908.09203)
- 
…[truncated 460 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_research_bib_complete_20260515T043737",
  "tool": "Agent",
  "elapsed_ms": 24
}
```

</details>

---

### Tool call

_source line 119 · 2026-05-15T04:42:11.282458+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "site:nature.com \"Scalable watermarking for identifying large language model outputs\" complete author list Dathathri"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_research_bib_complete_20260515T043737",
  "tool": "WebSearch",
  "tool_args": {
    "query": "site:nature.com \"Scalable watermarking for identifying large language model outputs\" complete author list Dathathri"
  }
}
```

</details>

---

### Tool result

_source line 120 · 2026-05-15T04:42:11.282708+00:00_

Web search results for query: "site:proceedings.mlr.press "Monitoring AI-Modified Content at Scale" Liang Izzo bibtex author list"

Links: [{"title":"[2403.07183] Monitoring AI-Modified Content at Scale: A Case Study on the Impact of ChatGPT on AI Conference Peer Reviews","url":"https://arxiv.org/abs/2403.07183"},{"title":"Monitoring AI-modified content at scale | Proceedings of the 41st International Conference on Machine Learning","url":"https://dl.acm.org/doi/10.5555/3692070.3693262"},{"title":"[PDF] Monitoring AI-Modified Content at Scale: A Case Study on the Impact of ChatGPT on AI Conference Peer Reviews | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Monitoring-AI-Modified-Content-at-Scale:-A-Case-on-Liang-Izzo/023e113b11ff7bac182713a069fedcbcccad9562"},{"title":"Monitoring AI-Modified Content at Scale: A Case Study on the Impact of ChatGPT on AI Conference Peer Reviews","url":"https://proceedings.mlr.press/v235/liang24b.html"},{"title":"Monitoring AI-Modified Content at Scale: A Case Study on the Impact of ChatGPT on AI Conference Peer Reviews","url":"https://arxiv.org/html/2403.07183v1"},{"title":"Monitoring AI-Modified Content at Scale: A Case Study on ...","url":"https://arxiv.org/pdf/2403.07183"},{"title":"[2403.07183v2] Monitoring AI-Modified Content at Scale: A Case Study on the Impact of ChatGPT on AI Conference Peer Reviews","url":"https://arxiv.org/abs/2403.07183v2"},{"title":"Monitoring AI-Modified Content at Scale: A Case Study on the Impact of ChatGPT on AI Conference Peer Reviews | alphaXiv","url":"https://www.alphaxiv.org/resources/2403.07183v2"},{"title":"Monitoring AI-Modified Content at Scale: A Case Study on the Impact of ChatGPT on AI Conference Peer Reviews. | NSF Public Access Repository","url":"https://par.nsf.gov/biblio/10617068-monitoring-ai-modified-content-scale-case-study-impact-chatgpt-ai-conference-peer-reviews"},{"title":"Monitoring AI-Modified Content at Scale: A Case Study on the Impact of ChatGPT on AI Confer
…[truncated 818 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_research_bib_complete_20260515T043737",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 121 · 2026-05-15T04:42:11.282964+00:00_

Web search results for query: "arxiv 2404.01268 Weixin Liang Yaohui Zhang full author list bibtex"

Links: [{"title":"[2404.01268] Mapping the Increasing Use of LLMs in Scientific Papers","url":"https://arxiv.org/abs/2404.01268"},{"title":"arXiv:2404.01268v1 [cs.CL] 1 Apr 2024","url":"https://arxiv.org/pdf/2404.01268"},{"title":"Mapping the Increasing Use of LLMs in Scientific Papers","url":"https://arxiv.org/html/2404.01268"},{"title":"Weixin Liang","url":"https://arxiv.org/search/?searchtype=author&query=Weixin+Liang"},{"title":"dblp: Weixin Liang","url":"https://dblp.org/pid/231/1803.html"},{"title":"Zhengxuan Wu Phone: 216-551-7046 wuzhengx@cs.stanford.edu","url":"https://zen-wu.social/pdf/cv.pdf"},{"title":"[2403.07183] Monitoring AI-Modified Content at Scale: A Case Study on the Impact of ChatGPT on AI Conference Peer Reviews","url":"https://arxiv.org/abs/2403.07183"},{"title":"BibTex file for LLMs · GitHub","url":"https://gist.github.com/ryokamoi/59dc522fbd00b432c5de1f5692fdfb3a"},{"title":"[2506.17467] Computational Approaches to Understanding Large Language Model Impact on Writing and Information Ecosystems","url":"https://arxiv.org/abs/2506.17467"},{"title":"Computer Vision and Pattern Recognition","url":"https://web3.arxiv.org/list/cs.CV/recent?skip=145&show=500"}]

Based on the search results, here is the information for arxiv paper 2404.01268:

## Full Author List

The authors are: Weixin Liang, Yaohui Zhang, Zhengxuan Wu, Haley Lepp, Wenlong Ji, Xuandong Zhao, Hancheng Cao, Sheng Liu, Siyu He, Zhi Huang, Diyi Yang, Christopher Potts, Christopher D Manning, and James Y. Zou.

## BibTeX Citation

Based on the information from the search results, here is the BibTeX entry:

```bibtex
@article{Liang2024Mapping,
  title={Mapping the Increasing Use of LLMs in Scientific Papers},
  author={Liang, Weixin and Zhang, Yaohui and Wu, Zhengxuan and Lepp, Haley and Ji, Wenlong and Zhao, Xuandong and Cao, Hancheng and Liu, Sheng and He, Siyu and Huang, Zhi and Yang, D
…[truncated 376 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_research_bib_complete_20260515T043737",
  "tool": "WebSearch",
  "elapsed_ms": 2
}
```

</details>

---

### Tool result

_source line 122 · 2026-05-15T04:42:11.283192+00:00_

Web search results for query: "site:neurips.cc "Intrinsic Dimension Estimation" Tulchinskii Kuznetsov Kushnareva Cherniavskii full author list 2023"

Links: [{"title":"Intrinsic Dimension Estimation for Robust Detection of AI-Generated Texts","url":"https://proceedings.neurips.cc/paper_files/paper/2023/hash/7baa48bc166aa2013d78cbdc15010530-Abstract-Conference.html"},{"title":"NeurIPS Poster Intrinsic Dimension Estimation for Robust Detection of AI-Generated Texts","url":"https://neurips.cc/virtual/2023/poster/72624"},{"title":"Intrinsic dimension estimation for robust detection of AI-generated texts | Proceedings of the 37th International Conference on Neural Information Processing Systems","url":"https://dl.acm.org/doi/10.5555/3666122.3667828"},{"title":"Intrinsic Dimension Estimation for Robust Detection of AI-Generated Texts","url":"https://papers.nips.cc/paper_files/paper/2023/file/7baa48bc166aa2013d78cbdc15010530-Paper-Conference.pdf"},{"title":"[PDF] Intrinsic Dimension Estimation for Robust Detection of AI-Generated Texts | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Intrinsic-Dimension-Estimation-for-Robust-Detection-Tulchinskii-Kuznetsov/a5fab19553e623e8787383cb3da76b8a3c42a8f4"},{"title":"Neurips","url":"https://neurips.cc/media/neurips-2024/Slides/93678_85QV4kz.pdf"},{"title":"[2306.04723] Intrinsic Dimension Estimation for Robust Detection of AI-Generated Texts","url":"https://arxiv.org/abs/2306.04723"},{"title":"NeurIPS Poster A Geometric View of Data Complexity: Efficient Local Intrinsic Dimension Estimation with Diffusion Models","url":"https://neurips.cc/virtual/2024/poster/93678"},{"title":"Intrinsic Dimension Estimation for Robust Detection of AI-Generated Texts | OpenReview","url":"https://openreview.net/forum?id=8uOZ0kNji6"},{"title":"NeurIPS Poster Intrinsic Dimension Estimation for Robust Detection of AI-Generated Texts","url":"https://nips.cc/virtual/2023/poster/72624"}]

I found the paper! Here's the complete author list fo
…[truncated 484 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_research_bib_complete_20260515T043737",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool call

_source line 123 · 2026-05-15T04:42:11.283423+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Daniel McFarland Stanford professor full name \"Daniel A. McFarland\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_research_bib_complete_20260515T043737",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Daniel McFarland Stanford professor full name \"Daniel A. McFarland\""
  }
}
```

</details>

---

### Tool result

_source line 124 · 2026-05-15T04:42:11.283687+00:00_

Here are the complete author lists in BibTeX format:

**1. DetectGPT (ICML 2023)**
```
author = {Mitchell, Eric and Lee, Yoonho and Khazatsky, Alexander and Manning, Christopher D. and Finn, Chelsea}
```

**2. GLTR (ACL 2019)**
```
author = {Gehrmann, Sebastian and Strobelt, Hendrik and Rush, Alexander}
```

**3. DNA-GPT (ICLR 2024)**
```
author = {Yang, Xianjun and Cheng, Wei and Wu, Yue and Petzold, Linda and Wang, William Yang and Chen, Haifeng}
```

**4. Binoculars (ICML 2024)**
```
author = {Hans, Abhimanyu and Schwarzschild, Avi and Cherepanova, Valeriia and Kazemi, Hamid and Saha, Aniruddha and Goldblum, Micah and Geiping, Jonas and Goldstein, Tom}
```

**5. Fast-DetectGPT (ICLR 2024)**
```
author = {Bao, Guangsheng and Zhao, Yanbin and Teng, Zhiyang and Yang, Linyi and Zhang, Yue}
```

**6. Beyond Perplexity (arXiv 2605.01647, 2026)**
```
author = {Narayanasamy, Priyadarshan and Agrawal, Swastik and Faber, Klint and Alam, Fardina Fathmiul}
```

Note on paper 2: Alexander Rush's full name in some publications appears as "Alexander M. Rush"; the DBLP entry for GLTR lists him as "Alexander M. Rush". If you want maximum precision for that entry, use `Rush, Alexander M.` instead.

Sources:
- [DetectGPT on arXiv](https://arxiv.org/abs/2301.11305)
- [DetectGPT at ICML proceedings](https://proceedings.mlr.press/v202/mitchell23a.html)
- [GLTR on ACL Anthology](https://aclanthology.org/P19-3019/)
- [DNA-GPT on arXiv](https://arxiv.org/abs/2305.17359)
- [DNA-GPT on DBLP](https://dblp1.uni-trier.de/rec/conf/iclr/Yang0WPWC24.html)
- [Binoculars on arXiv](https://arxiv.org/abs/2401.12070)
- [Fast-DetectGPT on arXiv](https://arxiv.org/abs/2310.05130)
- [Beyond Perplexity on arXiv](https://arxiv.org/abs/2605.01647)
agentId: a439e7e10988ccd9d (use SendMessage with to: 'a439e7e10988ccd9d' to continue this agent)
&lt;usage>total_tokens: 25590
tool_uses: 11
duration_ms: 58642&lt;/usage>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_research_bib_complete_20260515T043737",
  "tool": "Agent",
  "elapsed_ms": 28
}
```

</details>

---

### Tool result

_source line 125 · 2026-05-15T04:42:11.283952+00:00_

Here are the complete author lists in BibTeX format:

**Paper 1: "LLM as a Broken Telephone: Iterative Generation Distorts Information"**
```
author = {Mohamed, Amr and Geng, Mingmeng and Vazirgiannis, Michalis and Shang, Guokan}
```

**Paper 2: "Markovian Generation Chains in Large Language Models"**
```
author = {Geng, Mingmeng and Mohamed, Amr and Shang, Guokan and Vazirgiannis, Michalis and Poibeau, Thierry}
```

**Paper 3: "Detecting Pretraining Data from Large Language Models"**
```
author = {Shi, Weijia and Ajith, Anirudh and Xia, Mengzhou and Huang, Yangsibo and Liu, Daogao and Blevins, Terra and Chen, Danqi and Zettlemoyer, Luke}
```

**Paper 4: "Automatic Detection of Machine Generated Text: A Critical Survey"**
```
author = {Jawahar, Ganesh and Abdul-Mageed, Muhammad and Lakshmanan, Laks V.S.}
```

Sources:
- [ACL Anthology - LLM as a Broken Telephone](https://aclanthology.org/2025.acl-long.371/)
- [arXiv 2603.11228 - Markovian Generation Chains](https://arxiv.org/abs/2603.11228)
- [arXiv 2310.16789 - Detecting Pretraining Data](https://arxiv.org/abs/2310.16789)
- [ACL Anthology - Automatic Detection of Machine Generated Text](https://aclanthology.org/2020.coling-main.208/)
- [GitHub - detect-pretrain-code (confirms full author list)](https://github.com/swj0419/detect-pretrain-code)
agentId: aeaaf762bd1e2d765 (use SendMessage with to: 'aeaaf762bd1e2d765' to continue this agent)
&lt;usage>total_tokens: 21123
tool_uses: 7
duration_ms: 35473&lt;/usage>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_research_bib_complete_20260515T043737",
  "tool": "Agent",
  "elapsed_ms": 17
}
```

</details>

---

### Tool result

_source line 126 · 2026-05-15T04:42:11.284164+00:00_

Web search results for query: "Daniel McFarland Stanford professor full name "Daniel A. McFarland""

Links: [{"title":"Daniel McFarland's Profile | Stanford Profiles","url":"https://profiles.stanford.edu/daniel-mcfarland"},{"title":"Daniel A. McFarland | Stanford Graduate School of Education","url":"https://ed.stanford.edu/faculty/mcfarland"},{"title":"Daniel A. McFarland | Stanford Graduate School of Business","url":"https://www.gsb.stanford.edu/faculty-research/faculty/daniel-mcfarland"},{"title":"Daniel McFarland","url":"https://scholar.google.com/citations?user=nx8clgcAAAAJ&hl=en"},{"title":"Daniel McFarland","url":"https://cap.stanford.edu/profiles/frdActionServlet?choiceId=printerprofile&profileversion=full&profileId=10400"},{"title":"Daniel A. McFarland, Instructor | Coursera","url":"https://www.coursera.org/instructor/~1139667"},{"title":"Daniel McFarland | Department of Sociology","url":"https://sociology.stanford.edu/people/daniel-mcfarland"},{"title":"Daniel McFarland - Stanford, California, United States | Professional Profile | LinkedIn","url":"https://www.linkedin.com/in/daniel-mcfarland-0a9a92/"},{"title":"Daniel McFarland","url":"https://openreview.net/profile?id=~Daniel_McFarland1"},{"title":"Daniel McFarland - Stanford University - Academia.edu","url":"https://stanford.academia.edu/DMcFarland"}]

Based on the search results, I can confirm information about Daniel A. McFarland at Stanford:

Daniel A. McFarland is a Professor of Education, Sociology, and Organizational Behavior at Stanford University. He is the director of Stanford's certificate program in Computational Social Science.

He studies the intellectual, social and institutional dynamics of educational systems like schools, classrooms, universities and disciplines. He holds a PhD from the University of Chicago in Sociology.

The search results confirm that "Daniel A. McFarland" is indeed his full name, as shown across multiple Stanford institutional profiles and academic databases.


REMIN
…[truncated 95 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_research_bib_complete_20260515T043737",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 127 · 2026-05-15T04:42:11.284385+00:00_

Web search results for query: "site:nature.com "Scalable watermarking for identifying large language model outputs" complete author list Dathathri"

Links: [{"title":"Scalable watermarking for identifying large language model outputs | Nature","url":"https://www.nature.com/articles/s41586-024-08025-4"},{"title":"Scalable watermarking for identifying large language model outputs - PMC","url":"https://pmc.ncbi.nlm.nih.gov/articles/PMC11499265/"},{"title":"Scalable watermarking for identifying large language model outputs | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Scalable-watermarking-for-identifying-large-model-Dathathri-See/89bd8efe0b9c0427cb7814d7b8c2b0190d2ffa9e"},{"title":"(PDF) Scalable watermarking for identifying large language model outputs","url":"https://www.researchgate.net/publication/385176946_Scalable_watermarking_for_identifying_large_language_model_outputs"},{"title":"Scalable watermarking for identifying large language model outputs – ScienceOpen","url":"https://www.scienceopen.com/document?vid=e36b034b-6be1-439b-bccb-f413efc57773"},{"title":"Scalable watermarking for identifying large language ...","url":"https://pubmed.ncbi.nlm.nih.gov/39443777/"},{"title":"GitHub - google-deepmind/synthid-text · GitHub","url":"https://github.com/google-deepmind/synthid-text"},{"title":"AI watermarking must be watertight to be effective","url":"https://www.nature.com/articles/d41586-024-03418-x"},{"title":"Scalable watermarking for identifying large language model outputs - ADS","url":"https://ui.adsabs.harvard.edu/abs/2024Natur.634..818D/abstract"},{"title":"Scalable watermarking for identifying large language model outputs","url":"https://www.openread.academy/paper/reading?corpusId=511427010"}]

Based on my search results, here is the complete author list for the Nature paper "Scalable watermarking for identifying large language model outputs":

Dathathri, Sumanth; See, Abigail; Ghaisas, Sumedh; Huang, Po-Sen; McAdam, Rob; Welbl, Johannes; B
…[truncated 467 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_research_bib_complete_20260515T043737",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 128 · 2026-05-15T04:42:11.284743+00:00_

Here are the complete author lists in BibTeX format for all six papers:

**1. Intrinsic Dimension Estimation for Robust Detection of AI-Generated Texts (NeurIPS 2023)**
```
author = {Tulchinskii, Eduard and Kuznetsov, Kristian and Kushnareva, Laida and Cherniavskii, Daniil and Nikolenko, Sergey and Burnaev, Evgeny and Barannikov, Serguei and Piontkovskaya, Irina}
```

**2. Breaking the Generator Barrier: Disentangled Representation for Generalizable AI-Text Detection (arXiv 2604.13692, 2026)**
```
author = {Pu, Xiao and Cheng, Zepeng and Yuan, Lin and Wu, Yu and Bi, Xiuli}
```

**3. Feature-Augmented Transformers for Robust AI-Text Detection Across Domains and Generators (arXiv 2605.03969, 2026)**
```
author = {Mady, Mohamed and Reschke, Johannes and Schuller, Bj{\"o}rn}
```

**4. Can AI-Generated Text be Reliably Detected? (ICLR 2024)**
```
author = {Sadasivan, Vinu Sankar and Kumar, Aounon and Balasubramanian, Sriram and Wang, Wenxiao and Feizi, Soheil}
```

**5. Paraphrasing Evades Detectors of AI-Generated Text, but Retrieval is an Effective Defense (NeurIPS 2023)**
```
author = {Krishna, Kalpesh and Song, Yixiao and Karpinska, Marzena and Wieting, John and Iyyer, Mohit}
```

**6. Position: On the Possibilities of AI-Generated Text Detection (ICML 2024)**
```
author = {Chakraborty, Souradip and Bedi, Amrit Singh and Zhu, Sicheng and An, Bang and Manocha, Dinesh and Huang, Furong}
```

Sources:
- [NeurIPS 2023 - Tulchinskii et al.](https://proceedings.neurips.cc/paper_files/paper/2023/hash/7baa48bc166aa2013d78cbdc15010530-Abstract-Conference.html)
- [arXiv 2604.13692 - Pu et al.](https://arxiv.org/abs/2604.13692)
- [arXiv 2605.03969 - Mady et al.](https://arxiv.org/abs/2605.03969)
- [arXiv 2303.11156 - Sadasivan et al.](https://arxiv.org/abs/2303.11156)
- [NeurIPS 2023 - Krishna et al.](https://proceedings.neurips.cc/paper_files/paper/2023/hash/575c450013d0e99e4b0ecf82bd1afaa4-Abstract-Conference.html)
- [ICML 2024 - Chakraborty et al.](https://proceedings.mlr.pr
…[truncated 194 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_research_bib_complete_20260515T043737",
  "tool": "Agent",
  "elapsed_ms": 28
}
```

</details>

---

### Tool result

_source line 129 · 2026-05-15T04:42:11.285069+00:00_

Here are the complete author lists for all 6 papers in BibTeX format:

---

**1. "The Curious Decline of Linguistic Diversity: Training Language Models on Synthetic Text" (NAACL 2024)**

```
author = {Guo, Yanzhu and Shang, Guokan and Vazirgiannis, Michalis and Clavel, Chlo\'{e}}
```

**2. "The Curious Case of Neural Text Degeneration" (ICLR 2020)**

```
author = {Holtzman, Ari and Buys, Jan and Du, Li and Forbes, Maxwell and Choi, Yejin}
```

**3. "Mapping the Increasing Use of LLMs in Scientific Papers" (arXiv 2404.01268, 2024)**

```
author = {Liang, Weixin and Zhang, Yaohui and Wu, Zhengxuan and Lepp, Haley and Ji, Wenlong and Zhao, Xuandong and Cao, Hancheng and Liu, Sheng and He, Siyu and Huang, Zhi and Yang, Diyi and Potts, Christopher and Manning, Christopher D. and Zou, James Y.}
```

**4. "Monitoring AI-Modified Content at Scale: A Case Study on the Impact of ChatGPT on AI Conference Peer Reviews" (ICML 2024)**

```
author = {Liang, Weixin and Izzo, Zachary and Zhang, Yaohui and Lepp, Haley and Cao, Hancheng and Zhao, Xuandong and Chen, Lingjiao and Ye, Haotian and Liu, Sheng and Huang, Zhi and McFarland, Daniel A. and Zou, James Y.}
```

**5. "Computational Methods in Authorship Attribution" (JASIST 2009)**

```
author = {Koppel, Moshe and Schler, Jonathan and Argamon, Shlomo}
```

**6. "Authorship Attribution for Neural Text Generation" (EMNLP 2020)**

```
author = {Uchendu, Adaku and Le, Thai and Shu, Kai and Lee, Dongwon}
```

---

Sources:
- [ACL Anthology - Guo et al. NAACL 2024](https://aclanthology.org/2024.findings-naacl.228/)
- [DBLP - Holtzman et al. ICLR 2020](https://dblp.org/rec/conf/iclr/HoltzmanBDFC20.html)
- [arXiv - Liang et al. 2404.01268](https://arxiv.org/abs/2404.01268)
- [PMLR - Liang et al. ICML 2024](https://proceedings.mlr.press/v235/liang24b.html)
- [Wiley - Koppel et al. JASIST 2009](https://onlinelibrary.wiley.com/doi/abs/10.1002/asi.20961)
- [ACL Anthology - Uchendu et al. EMNLP 2020](https://aclanthology.org/2020.emnlp-main.6
…[truncated 251 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_research_bib_complete_20260515T043737",
  "tool": "Agent",
  "elapsed_ms": 20
}
```

</details>

---

### Tool result

_source line 130 · 2026-05-15T04:42:11.285370+00:00_

Here are the complete author lists in BibTeX format:

**1. Data Selection for Language Models via Importance Resampling (NeurIPS 2023)**
```
author = {Xie, Sang Michael and Santurkar, Shibani and Ma, Tengyu and Liang, Percy}
```

**2. QuRating: Selecting High-Quality Data for Training Language Models (ICML 2024)**
```
author = {Wettig, Alexander and Gupta, Aatmik and Malik, Saumya and Chen, Danqi}
```

**3. CCNet: Extracting High Quality Monolingual Datasets from Web Crawl Data (LREC 2020)**
```
author = {Wenzek, Guillaume and Lachaux, Marie-Anne and Conneau, Alexis and Chaudhary, Vishrav and Guzm{\'a}n, Francisco and Joulin, Armand and Grave, Edouard}
```

**4. A Watermark for Large Language Models (ICML 2023)**
```
author = {Kirchenbauer, John and Geiping, Jonas and Wen, Yuxin and Katz, Jonathan and Miers, Ian and Goldstein, Tom}
```

**5. Scalable Watermarking for Identifying Large Language Model Outputs (Nature 2024)**
```
author = {Dathathri, Sumanth and See, Abigail and Ghaisas, Sumedh and Huang, Po-Sen and McAdam, Rob and Welbl, Johannes and Bachani, Vandana and Kaskasoli, Alex and Stanforth, Robert and Matejovicova, Tatiana and Hayes, Jamie and Vyas, Nidhi and Al Merey, Majd and Brown-Cohen, Jonah and Bunel, Rudy and Balle, Borja and Cemgil, Taylan and Ahmed, Zahra and Stacpoole, Kitty and Shumailov, Ilia and Baetu, Ciprian and Gowal, Sven and Hassabis, Demis and Kohli, Pushmeet}
```

**6. Chainwash: Multi-Step Rewriting Attacks on Diffusion Language Model Watermarks (arXiv 2605.05503, 2026)**
```
author = {Ameen, Mohd Ruhul and Islam, Akif and Mahmud, Nadim and Hamid, Md. Ekramul}
```

Sources:
- [NeurIPS 2023 - DSIR](https://neurips.cc/virtual/2023/poster/70154)
- [arXiv 2302.03169 - DSIR](https://arxiv.org/abs/2302.03169)
- [ICML 2024 - QuRating](https://proceedings.mlr.press/v235/wettig24a.html)
- [arXiv 2402.09739 - QuRating](https://arxiv.org/abs/2402.09739)
- [ACL Anthology - CCNet](https://aclanthology.org/2020.lrec-1.494/)
- [arXiv 2301.10226 - Wate
…[truncated 451 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_research_bib_complete_20260515T043737",
  "tool": "Agent",
  "elapsed_ms": 25
}
```

</details>

---

### Tool call

_source line 131 · 2026-05-15T04:42:11.285682+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/references.bib",
  "old_string": "  author = {Mitchell and others},",
  "new_string": "  author = {Mitchell, Eric and Lee, Yoonho and Khazatsky, Alexander and Manning, Christopher D. and Finn, Chelsea},"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_research_bib_complete_20260515T043737",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/references.bib",
    "old_string": "  author = {Mitchell and others},",
    "new_string": "  author = {Mitchell, Eric and Lee, Yoonho and Khazatsky, Alexander and Manning, Christopher D. and Finn, Chelsea},"
  }
}
```

</details>

---

### Tool result

_source line 132 · 2026-05-15T04:42:11.285899+00:00_

The file /home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/references.bib has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_research_bib_complete_20260515T043737",
  "tool": "Edit",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 133 · 2026-05-15T04:42:11.286105+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/references.bib",
  "old_string": "  author = {Gehrmann and others},",
  "new_string": "  author = {Gehrmann, Sebastian and Strobelt, Hendrik and Rush, Alexander M.},"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_research_bib_complete_20260515T043737",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/references.bib",
    "old_string": "  author = {Gehrmann and others},",
    "new_string": "  author = {Gehrmann, Sebastian and Strobelt, Hendrik and Rush, Alexander M.},"
  }
}
```

</details>

---

### Tool result

_source line 134 · 2026-05-15T04:42:11.286381+00:00_

The file /home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/references.bib has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_research_bib_complete_20260515T043737",
  "tool": "Edit",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 135 · 2026-05-15T04:42:11.286624+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/references.bib",
  "old_string": "  author = {Yang and others},",
  "new_string": "  author = {Yang, Xianjun and Cheng, Wei and Wu, Yue and Petzold, Linda and Wang, William Yang and Chen, Haifeng},"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_research_bib_complete_20260515T043737",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/references.bib",
    "old_string": "  author = {Yang and others},",
    "new_string": "  author = {Yang, Xianjun and Cheng, Wei and Wu, Yue and Petzold, Linda and Wang, William Yang and Chen, Haifeng},"
  }
}
```

</details>

---

### Tool result

_source line 136 · 2026-05-15T04:42:11.286907+00:00_

The file /home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/references.bib has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_research_bib_complete_20260515T043737",
  "tool": "Edit",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 137 · 2026-05-15T04:42:11.287114+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/references.bib",
  "old_string": "  author = {Hans and others},",
  "new_string": "  author = {Hans, Abhimanyu and Schwarzschild, Avi and Cherepanova, Valeriia and Kazemi, Hamid and Saha, Aniruddha and Goldblum, Micah and Geiping, Jonas and Goldstein, Tom},"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_research_bib_complete_20260515T043737",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/references.bib",
    "old_string": "  author = {Hans and others},",
    "new_string": "  author = {Hans, Abhimanyu and Schwarzschild, Avi and Cherepanova, Valeriia and Kazemi, Hamid and Saha, Aniruddha and Goldblum, Micah and Geiping, Jonas and Goldstein, Tom},"
  }
}
```

</details>

---

### Tool result

_source line 138 · 2026-05-15T04:42:11.287386+00:00_

The file /home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/references.bib has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_research_bib_complete_20260515T043737",
  "tool": "Edit",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 139 · 2026-05-15T04:42:11.287631+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/references.bib",
  "old_string": "  author = {Bao and others},",
  "new_string": "  author = {Bao, Guangsheng and Zhao, Yanbin and Teng, Zhiyang and Yang, Linyi and Zhang, Yue},"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_research_bib_complete_20260515T043737",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/references.bib",
    "old_string": "  author = {Bao and others},",
    "new_string": "  author = {Bao, Guangsheng and Zhao, Yanbin and Teng, Zhiyang and Yang, Linyi and Zhang, Yue},"
  }
}
```

</details>

---

### Tool result

_source line 140 · 2026-05-15T04:42:11.287907+00:00_

The file /home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/references.bib has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_research_bib_complete_20260515T043737",
  "tool": "Edit",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 141 · 2026-05-15T04:42:11.288111+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/references.bib",
  "old_string": "  author = {Narayanasamy and others},",
  "new_string": "  author = {Narayanasamy, Priyadarshan and Agrawal, Swastik and Faber, Klint and Alam, Fardina Fathmiul},"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_research_bib_complete_20260515T043737",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/references.bib",
    "old_string": "  author = {Narayanasamy and others},",
    "new_string": "  author = {Narayanasamy, Priyadarshan and Agrawal, Swastik and Faber, Klint and Alam, Fardina Fathmiul},"
  }
}
```

</details>

---

### Tool result

_source line 142 · 2026-05-15T04:42:11.288354+00:00_

The file /home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/references.bib has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_research_bib_complete_20260515T043737",
  "tool": "Edit",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 143 · 2026-05-15T04:42:11.288545+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/references.bib",
  "old_string": "  author = {Tulchinskii and others},",
  "new_string": "  author = {Tulchinskii, Eduard and Kuznetsov, Kristian and Kushnareva, Laida and Cherniavskii, Daniil and Nikolenko, Sergey and Burnaev, Evgeny and Barannikov, Serguei and Piontkovskaya, Irina},"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_research_bib_complete_20260515T043737",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/references.bib",
    "old_string": "  author = {Tulchinskii and others},",
    "new_string": "  author = {Tulchinskii, Eduard and Kuznetsov, Kristian and Kushnareva, Laida and Cherniavskii, Daniil and Nikolenko, Sergey and Burnaev, Evgeny and Barannikov, Serguei and Piontkovskaya, Irina},"
  }
}
```

</details>

---

### Tool result

_source line 144 · 2026-05-15T04:42:11.288782+00:00_

The file /home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/references.bib has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_research_bib_complete_20260515T043737",
  "tool": "Edit",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 145 · 2026-05-15T04:42:11.288955+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/references.bib",
  "old_string": "  author = {Pu and others},",
  "new_string": "  author = {Pu, Xiao and Cheng, Zepeng and Yuan, Lin and Wu, Yu and Bi, Xiuli},"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_research_bib_complete_20260515T043737",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/references.bib",
    "old_string": "  author = {Pu and others},",
    "new_string": "  author = {Pu, Xiao and Cheng, Zepeng and Yuan, Lin and Wu, Yu and Bi, Xiuli},"
  }
}
```

</details>

---

### Tool result

_source line 146 · 2026-05-15T04:42:11.289175+00:00_

The file /home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/references.bib has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_research_bib_complete_20260515T043737",
  "tool": "Edit",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 147 · 2026-05-15T04:42:11.289349+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/references.bib",
  "old_string": "  author = {Mady and others},",
  "new_string": "  author = {Mady, Mohamed and Reschke, Johannes and Schuller, Bj{\\\"o}rn},"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_research_bib_complete_20260515T043737",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/references.bib",
    "old_string": "  author = {Mady and others},",
    "new_string": "  author = {Mady, Mohamed and Reschke, Johannes and Schuller, Bj{\\\"o}rn},"
  }
}
```

</details>

---

### Tool result

_source line 148 · 2026-05-15T04:42:11.289604+00:00_

The file /home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/references.bib has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_research_bib_complete_20260515T043737",
  "tool": "Edit",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 149 · 2026-05-15T04:42:11.289834+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/references.bib",
  "old_string": "  author = {Sadasivan and others},",
  "new_string": "  author = {Sadasivan, Vinu Sankar and Kumar, Aounon and Balasubramanian, Sriram and Wang, Wenxiao and Feizi, Soheil},"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_research_bib_complete_20260515T043737",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/references.bib",
    "old_string": "  author = {Sadasivan and others},",
    "new_string": "  author = {Sadasivan, Vinu Sankar and Kumar, Aounon and Balasubramanian, Sriram and Wang, Wenxiao and Feizi, Soheil},"
  }
}
```

</details>

---

### Tool result

_source line 150 · 2026-05-15T04:42:11.290107+00:00_

The file /home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/references.bib has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_research_bib_complete_20260515T043737",
  "tool": "Edit",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 151 · 2026-05-15T04:42:11.290326+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/references.bib",
  "old_string": "  author = {Krishna and others},",
  "new_string": "  author = {Krishna, Kalpesh and Song, Yixiao and Karpinska, Marzena and Wieting, John and Iyyer, Mohit},"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_research_bib_complete_20260515T043737",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/references.bib",
    "old_string": "  author = {Krishna and others},",
    "new_string": "  author = {Krishna, Kalpesh and Song, Yixiao and Karpinska, Marzena and Wieting, John and Iyyer, Mohit},"
  }
}
```

</details>

---

### Tool result

_source line 152 · 2026-05-15T04:42:11.290586+00:00_

The file /home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/references.bib has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_research_bib_complete_20260515T043737",
  "tool": "Edit",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 153 · 2026-05-15T04:42:11.290825+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/references.bib",
  "old_string": "  author = {Chakraborty and others},",
  "new_string": "  author = {Chakraborty, Souradip and Bedi, Amrit Singh and Zhu, Sicheng and An, Bang and Manocha, Dinesh and Huang, Furong},"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_research_bib_complete_20260515T043737",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/references.bib",
    "old_string": "  author = {Chakraborty and others},",
    "new_string": "  author = {Chakraborty, Souradip and Bedi, Amrit Singh and Zhu, Sicheng and An, Bang and Manocha, Dinesh and Huang, Furong},"
  }
}
```

</details>

---

### Tool result

_source line 154 · 2026-05-15T04:42:11.291084+00:00_

The file /home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/references.bib has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_research_bib_complete_20260515T043737",
  "tool": "Edit",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 155 · 2026-05-15T04:42:11.291291+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/references.bib",
  "old_string": "  author = {Zellers and others},",
  "new_string": "  author = {Zellers, Rowan and Holtzman, Ari and Rashkin, Hannah and Bisk, Yonatan and Farhadi, Ali and Roesner, Franziska and Choi, Yejin},"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_research_bib_complete_20260515T043737",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/references.bib",
    "old_string": "  author = {Zellers and others},",
    "new_string": "  author = {Zellers, Rowan and Holtzman, Ari and Rashkin, Hannah and Bisk, Yonatan and Farhadi, Ali and Roesner, Franziska and Choi, Yejin},"
  }
}
```

</details>

---

### Tool result

_source line 156 · 2026-05-15T04:42:11.291562+00:00_

The file /home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/references.bib has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_research_bib_complete_20260515T043737",
  "tool": "Edit",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 157 · 2026-05-15T04:42:11.291797+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/references.bib",
  "old_string": "  author = {Solaiman and others},",
  "new_string": "  author = {Solaiman, Irene and Brundage, Miles and Clark, Jack and Askell, Amanda and Herbert-Voss, Ariel and Wu, Jeff and Radford, Alec and Krueger, Gretchen and Kim, Jong Wook and Kreps, Sarah and McCain, Miles and Newhouse, Alex and Blazakis, Jason and McGuffie, Kris and Wang, Jasmine},"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_research_bib_complete_20260515T043737",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/references.bib",
    "old_string": "  author = {Solaiman and others},",
    "new_string": "  author = {Solaiman, Irene and Brundage, Miles and Clark, Jack and Askell, Amanda and Herbert-Voss, Ariel and Wu, Jeff and Radford, Alec and Krueger, Gretchen and Kim, Jong Wook and Kreps, Sarah and McCain, Miles and Newhouse, Alex and Blazakis, Jason and McGuffie, Kris and Wang, Jasmine},"
  }
}
```

</details>

---

### Tool result

_source line 158 · 2026-05-15T04:42:11.292072+00:00_

The file /home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/references.bib has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_research_bib_complete_20260515T043737",
  "tool": "Edit",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 159 · 2026-05-15T04:42:11.292272+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/references.bib",
  "old_string": "  author = {Alemohammad and others},",
  "new_string": "  author = {Alemohammad, Sina and Casco-Rodriguez, Josue and Luzi, Lorenzo and Humayun, Ahmed Imtiaz and Babaei, Hossein and LeJeune, Daniel and Siahkoohi, Ali and Baraniuk, Richard G.},"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_research_bib_complete_20260515T043737",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/references.bib",
    "old_string": "  author = {Alemohammad and others},",
    "new_string": "  author = {Alemohammad, Sina and Casco-Rodriguez, Josue and Luzi, Lorenzo and Humayun, Ahmed Imtiaz and Babaei, Hossein and LeJeune, Daniel and Siahkoohi, Ali and Baraniuk, Richard G.},"
  }
}
```

</details>

---

### Tool result

_source line 160 · 2026-05-15T04:42:11.292533+00:00_

The file /home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/references.bib has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_research_bib_complete_20260515T043737",
  "tool": "Edit",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 161 · 2026-05-15T04:42:11.292753+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/references.bib",
  "old_string": "  author = {Shumailov and others},",
  "new_string": "  author = {Shumailov, Ilia and Shumaylov, Zakhar and Zhao, Yiren and Gal, Yarin and Papernot, Nicolas and Anderson, Ross},"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_research_bib_complete_20260515T043737",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/references.bib",
    "old_string": "  author = {Shumailov and others},",
    "new_string": "  author = {Shumailov, Ilia and Shumaylov, Zakhar and Zhao, Yiren and Gal, Yarin and Papernot, Nicolas and Anderson, Ross},"
  }
}
```

</details>

---

### Tool result

_source line 162 · 2026-05-15T04:42:11.293009+00:00_

The file /home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/references.bib has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_research_bib_complete_20260515T043737",
  "tool": "Edit",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 163 · 2026-05-15T04:42:11.293220+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/references.bib",
  "old_string": "  author = {Dohmatob and others},",
  "new_string": "  author = {Dohmatob, Elvis and Feng, Yunzhen and Subramonian, Arjun and Kempe, Julia},"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_research_bib_complete_20260515T043737",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/references.bib",
    "old_string": "  author = {Dohmatob and others},",
    "new_string": "  author = {Dohmatob, Elvis and Feng, Yunzhen and Subramonian, Arjun and Kempe, Julia},"
  }
}
```

</details>

---

### Tool result

_source line 164 · 2026-05-15T04:42:11.293483+00:00_

The file /home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/references.bib has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_research_bib_complete_20260515T043737",
  "tool": "Edit",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 165 · 2026-05-15T04:42:11.293701+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/references.bib",
  "old_string": "  author = {Gerstgrasser and others},",
  "new_string": "  author = {Gerstgrasser, Matthias and Schaeffer, Rylan and Dey, Apratim and Rafailov, Rafael and Sleight, Henry and Hughes, John and Korbak, Tomasz and Agrawal, Rajashree and Pai, Dhruv and Gromov, Andrey and Roberts, Daniel A. and Yang, Diyi and Donoho, David L. and Koyejo, Sanmi},"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_research_bib_complete_20260515T043737",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/references.bib",
    "old_string": "  author = {Gerstgrasser and others},",
    "new_string": "  author = {Gerstgrasser, Matthias and Schaeffer, Rylan and Dey, Apratim and Rafailov, Rafael and Sleight, Henry and Hughes, John and Korbak, Tomasz and Agrawal, Rajashree and Pai, Dhruv and Gromov, Andrey and Roberts, Daniel A. and Yang, Diyi and Donoho, David L. and Koyejo, Sanmi},"
  }
}
```

</details>

---

### Tool result

_source line 166 · 2026-05-15T04:42:11.293964+00:00_

The file /home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/references.bib has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_research_bib_complete_20260515T043737",
  "tool": "Edit",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 167 · 2026-05-15T04:42:11.294158+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/references.bib",
  "old_string": "  author = {Xie and others},",
  "new_string": "  author = {Xie, Sang Michael and Santurkar, Shibani and Ma, Tengyu and Liang, Percy},"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_research_bib_complete_20260515T043737",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/references.bib",
    "old_string": "  author = {Xie and others},",
    "new_string": "  author = {Xie, Sang Michael and Santurkar, Shibani and Ma, Tengyu and Liang, Percy},"
  }
}
```

</details>

---

### Tool result

_source line 168 · 2026-05-15T04:42:11.294423+00:00_

The file /home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/references.bib has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_research_bib_complete_20260515T043737",
  "tool": "Edit",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 169 · 2026-05-15T04:42:11.294614+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/references.bib",
  "old_string": "  author = {Wettig and others},",
  "new_string": "  author = {Wettig, Alexander and Gupta, Aatmik and Malik, Saumya and Chen, Danqi},"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_research_bib_complete_20260515T043737",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/references.bib",
    "old_string": "  author = {Wettig and others},",
    "new_string": "  author = {Wettig, Alexander and Gupta, Aatmik and Malik, Saumya and Chen, Danqi},"
  }
}
```

</details>

---

### Tool result

_source line 170 · 2026-05-15T04:42:11.294860+00:00_

The file /home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/references.bib has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_research_bib_complete_20260515T043737",
  "tool": "Edit",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 171 · 2026-05-15T04:42:11.295041+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/references.bib",
  "old_string": "  author = {Wenzek and others},",
  "new_string": "  author = {Wenzek, Guillaume and Lachaux, Marie-Anne and Conneau, Alexis and Chaudhary, Vishrav and Guzm{\\'a}n, Francisco and Joulin, Armand and Grave, Edouard},"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_research_bib_complete_20260515T043737",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/references.bib",
    "old_string": "  author = {Wenzek and others},",
    "new_string": "  author = {Wenzek, Guillaume and Lachaux, Marie-Anne and Conneau, Alexis and Chaudhary, Vishrav and Guzm{\\'a}n, Francisco and Joulin, Armand and Grave, Edouard},"
  }
}
```

</details>

---

### Tool result

_source line 172 · 2026-05-15T04:42:11.295300+00:00_

The file /home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/references.bib has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_research_bib_complete_20260515T043737",
  "tool": "Edit",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 173 · 2026-05-15T04:42:11.295514+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/references.bib",
  "old_string": "  author = {Kirchenbauer and others},",
  "new_string": "  author = {Kirchenbauer, John and Geiping, Jonas and Wen, Yuxin and Katz, Jonathan and Miers, Ian and Goldstein, Tom},"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_research_bib_complete_20260515T043737",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/references.bib",
    "old_string": "  author = {Kirchenbauer and others},",
    "new_string": "  author = {Kirchenbauer, John and Geiping, Jonas and Wen, Yuxin and Katz, Jonathan and Miers, Ian and Goldstein, Tom},"
  }
}
```

</details>

---

### Tool result

_source line 174 · 2026-05-15T04:42:11.295784+00:00_

The file /home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/references.bib has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_research_bib_complete_20260515T043737",
  "tool": "Edit",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 175 · 2026-05-15T04:42:11.296012+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/references.bib",
  "old_string": "  author = {Dathathri and others},",
  "new_string": "  author = {Dathathri, Sumanth and See, Abigail and Ghaisas, Sumedh and Huang, Po-Sen and McAdam, Rob and Welbl, Johannes and Bachani, Vandana and Kaskasoli, Alex and Stanforth, Robert and Matejovicova, Tatiana and Hayes, Jamie and Vyas, Nidhi and Al-Merey, Majd and Brown-Cohen, Jonah and Bunel, Rudy and Balle, Borja and Cemgil, Taylan and Ahmed, Zahra and Stacpoole, Kitty and Shumailov, Ilia and Baetu, Ciprian and Gowal, Sven and Hassabis, Demis and Kohli, Pushmeet},"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_research_bib_complete_20260515T043737",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/references.bib",
    "old_string": "  author = {Dathathri and others},",
    "new_string": "  author = {Dathathri, Sumanth and See, Abigail and Ghaisas, Sumedh and Huang, Po-Sen and McAdam, Rob and Welbl, Johannes and Bachani, Vandana and Kaskasoli, Alex and Stanforth, Robert and Matejovicova, Tatiana and Hayes, Jamie and Vyas, Nidhi and Al-Merey, Majd and Brown-Cohen, Jonah and Bunel, Rudy and Balle, Borja and Cemgil, Taylan and Ahmed, Zahra and Stacpoole, Kitty and Shumailov, Ilia and Baetu, Ciprian and Gowal, Sven and Hassabis, Demis and Kohli, Pushmeet},"
  }
}
```

</details>

---

### Tool result

_source line 176 · 2026-05-15T04:42:11.296267+00:00_

The file /home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/references.bib has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_research_bib_complete_20260515T043737",
  "tool": "Edit",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 177 · 2026-05-15T04:42:11.296469+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/references.bib",
  "old_string": "  author = {Ameen and others},",
  "new_string": "  author = {Ameen, Mohd Ruhul and Islam, Akif and Mahmud, Nadim and Hamid, Md. Ekramul},"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_research_bib_complete_20260515T043737",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/references.bib",
    "old_string": "  author = {Ameen and others},",
    "new_string": "  author = {Ameen, Mohd Ruhul and Islam, Akif and Mahmud, Nadim and Hamid, Md. Ekramul},"
  }
}
```

</details>

---

### Tool result

_source line 178 · 2026-05-15T04:42:11.296758+00:00_

The file /home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/references.bib has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_research_bib_complete_20260515T043737",
  "tool": "Edit",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 179 · 2026-05-15T04:42:11.296973+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/references.bib",
  "old_string": "  author = {Guo and others},",
  "new_string": "  author = {Guo, Yanzhu and Shang, Guokan and Vazirgiannis, Michalis and Clavel, Chlo\\'{e}},"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_research_bib_complete_20260515T043737",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/references.bib",
    "old_string": "  author = {Guo and others},",
    "new_string": "  author = {Guo, Yanzhu and Shang, Guokan and Vazirgiannis, Michalis and Clavel, Chlo\\'{e}},"
  }
}
```

</details>

---

### Tool result

_source line 180 · 2026-05-15T04:42:11.297234+00:00_

The file /home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/references.bib has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_research_bib_complete_20260515T043737",
  "tool": "Edit",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 181 · 2026-05-15T04:42:11.297425+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/references.bib",
  "old_string": "  author = {Holtzman and others},",
  "new_string": "  author = {Holtzman, Ari and Buys, Jan and Du, Li and Forbes, Maxwell and Choi, Yejin},"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_research_bib_complete_20260515T043737",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/references.bib",
    "old_string": "  author = {Holtzman and others},",
    "new_string": "  author = {Holtzman, Ari and Buys, Jan and Du, Li and Forbes, Maxwell and Choi, Yejin},"
  }
}
```

</details>

---

### Tool result

_source line 182 · 2026-05-15T04:42:11.297786+00:00_

The file /home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/references.bib has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_research_bib_complete_20260515T043737",
  "tool": "Edit",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 183 · 2026-05-15T04:42:11.298062+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/references.bib",
  "old_string": "  author = {Koppel and others},",
  "new_string": "  author = {Koppel, Moshe and Schler, Jonathan and Argamon, Shlomo},"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_research_bib_complete_20260515T043737",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/references.bib",
    "old_string": "  author = {Koppel and others},",
    "new_string": "  author = {Koppel, Moshe and Schler, Jonathan and Argamon, Shlomo},"
  }
}
```

</details>

---

### Tool result

_source line 184 · 2026-05-15T04:42:11.298335+00:00_

The file /home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/references.bib has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_research_bib_complete_20260515T043737",
  "tool": "Edit",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 185 · 2026-05-15T04:42:11.298544+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/references.bib",
  "old_string": "  author = {Uchendu and others},",
  "new_string": "  author = {Uchendu, Adaku and Le, Thai and Shu, Kai and Lee, Dongwon},"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_research_bib_complete_20260515T043737",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/references.bib",
    "old_string": "  author = {Uchendu and others},",
    "new_string": "  author = {Uchendu, Adaku and Le, Thai and Shu, Kai and Lee, Dongwon},"
  }
}
```

</details>

---

### Tool result

_source line 186 · 2026-05-15T04:42:11.298845+00:00_

The file /home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/references.bib has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_research_bib_complete_20260515T043737",
  "tool": "Edit",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 187 · 2026-05-15T04:42:11.299057+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/references.bib",
  "old_string": "  author = {Mohamed and others},",
  "new_string": "  author = {Mohamed, Amr and Geng, Mingmeng and Vazirgiannis, Michalis and Shang, Guokan},"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_research_bib_complete_20260515T043737",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/references.bib",
    "old_string": "  author = {Mohamed and others},",
    "new_string": "  author = {Mohamed, Amr and Geng, Mingmeng and Vazirgiannis, Michalis and Shang, Guokan},"
  }
}
```

</details>

---

### Tool result

_source line 188 · 2026-05-15T04:42:11.299324+00:00_

The file /home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/references.bib has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_research_bib_complete_20260515T043737",
  "tool": "Edit",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 189 · 2026-05-15T04:42:11.299544+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/references.bib",
  "old_string": "  author = {Geng and others},",
  "new_string": "  author = {Geng, Mingmeng and Mohamed, Amr and Shang, Guokan and Vazirgiannis, Michalis and Poibeau, Thierry},"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_research_bib_complete_20260515T043737",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/references.bib",
    "old_string": "  author = {Geng and others},",
    "new_string": "  author = {Geng, Mingmeng and Mohamed, Amr and Shang, Guokan and Vazirgiannis, Michalis and Poibeau, Thierry},"
  }
}
```

</details>

---

### Tool result

_source line 190 · 2026-05-15T04:42:11.299835+00:00_

The file /home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/references.bib has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_research_bib_complete_20260515T043737",
  "tool": "Edit",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 191 · 2026-05-15T04:42:11.300064+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/references.bib",
  "old_string": "  author = {Shi and others},",
  "new_string": "  author = {Shi, Weijia and Ajith, Anirudh and Xia, Mengzhou and Huang, Yangsibo and Liu, Daogao and Blevins, Terra and Chen, Danqi and Zettlemoyer, Luke},"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_research_bib_complete_20260515T043737",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/references.bib",
    "old_string": "  author = {Shi and others},",
    "new_string": "  author = {Shi, Weijia and Ajith, Anirudh and Xia, Mengzhou and Huang, Yangsibo and Liu, Daogao and Blevins, Terra and Chen, Danqi and Zettlemoyer, Luke},"
  }
}
```

</details>

---

### Tool result

_source line 192 · 2026-05-15T04:42:11.300310+00:00_

The file /home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/references.bib has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_research_bib_complete_20260515T043737",
  "tool": "Edit",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 193 · 2026-05-15T04:42:11.300529+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/references.bib",
  "old_string": "  author = {Jawahar and others},",
  "new_string": "  author = {Jawahar, Ganesh and Abdul-Mageed, Muhammad and Lakshmanan, Laks V.S.},"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_research_bib_complete_20260515T043737",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/references.bib",
    "old_string": "  author = {Jawahar and others},",
    "new_string": "  author = {Jawahar, Ganesh and Abdul-Mageed, Muhammad and Lakshmanan, Laks V.S.},"
  }
}
```

</details>

---

### Tool result

_source line 194 · 2026-05-15T04:42:11.300900+00:00_

The file /home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/references.bib has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_research_bib_complete_20260515T043737",
  "tool": "Edit",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 195 · 2026-05-15T04:42:11.301241+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/references.bib",
  "old_string": "  title = {{Mapping the Increasing Use of LLMs in Scientific Papers}},\n  author = {Liang and others},",
  "new_string": "  title = {{Mapping the Increasing Use of LLMs in Scientific Papers}},\n  author = {Liang, Weixin and Zhang, Yaohui and Wu, Zhengxuan and Lepp, Haley and Ji, Wenlong and Zhao, Xuandong and Cao, Hancheng and Liu, Sheng and He, Siyu and Huang, Zhi and Yang, Diyi and Potts, Christopher and Manning, Christopher D. and Zou, James Y.},"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_research_bib_complete_20260515T043737",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/references.bib",
    "old_string": "  title = {{Mapping the Increasing Use of LLMs in Scientific Papers}},\n  author = {Liang and others},",
    "new_string": "  title = {{Mapping the Increasing Use of LLMs in Scientific Papers}},\n  author = {Liang, Weixin and Zhang, Yaohui and Wu, Zhengxuan and Lepp, Haley and Ji, Wenlong and Zhao, Xuandong and Cao, Hancheng and Liu, Sheng and He, Siyu and Huang, Zhi and Yang, Diyi and Potts, Christopher and Manning, Christopher D. and Zou, James Y.},"
  }
}
```

</details>

---

### Tool result

_source line 196 · 2026-05-15T04:42:11.301521+00:00_

The file /home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/references.bib has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_research_bib_complete_20260515T043737",
  "tool": "Edit",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 197 · 2026-05-15T04:42:11.301763+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/references.bib",
  "old_string": "  title = {{Monitoring AI-Modified Content at Scale: A Case Study on the Impact of ChatGPT on AI Conference Peer Reviews}},\n  author = {Liang and others},",
  "new_string": "  title = {{Monitoring AI-Modified Content at Scale: A Case Study on the Impact of ChatGPT on AI Conference Peer Reviews}},\n  author = {Liang, Weixin and Izzo, Zachary and Zhang, Yaohui and Lepp, Haley and Cao, Hancheng and Zhao, Xuandong and Chen, Lingjiao and Ye, Haotian and Liu, Sheng and Huang, Zhi and McFarland, Daniel A. and Zou, James Y.},"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_research_bib_complete_20260515T043737",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/references.bib",
    "old_string": "  title = {{Monitoring AI-Modified Content at Scale: A Case Study on the Impact of ChatGPT on AI Conference Peer Reviews}},\n  author = {Liang and others},",
    "new_string": "  title = {{Monitoring AI-Modified Content at Scale: A Case Study on the Impact of ChatGPT on AI Conference Peer Reviews}},\n  author = {Liang, Weixin and Izzo, Zachary and Zhang, Yaohui and Lepp, Haley and Cao, Hancheng and Zhao, Xuandong and Chen, Lingjiao and Ye, Haotian and Liu, Sheng and Huang, Zhi and McFarland, Daniel A. and Zou, James Y.},"
  }
}
```

</details>

---

### Tool result

_source line 198 · 2026-05-15T04:42:11.302027+00:00_

The file /home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/references.bib has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_research_bib_complete_20260515T043737",
  "tool": "Edit",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 199 · 2026-05-15T04:42:11.302236+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "and others",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/references.bib",
  "output_mode": "content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_research_bib_complete_20260515T043737",
  "tool": "Grep",
  "tool_args": {
    "pattern": "and others",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/references.bib",
    "output_mode": "content"
  }
}
```

</details>

---

### Tool result

_source line 200 · 2026-05-15T04:42:11.302438+00:00_

No matches found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_research_bib_complete_20260515T043737",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 201 · 2026-05-15T04:42:11.302707+00:00_

34 条 "and others" 全部替换为完整作者列表，无残留。所有作者信息均通过 WebSearch 从 arXiv/ACL Anthology/NeurIPS Proceedings/Nature 等权威来源验证，未编造任何名字。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_paper_research_bib_complete_20260515T043737"
}
```

</details>

---
