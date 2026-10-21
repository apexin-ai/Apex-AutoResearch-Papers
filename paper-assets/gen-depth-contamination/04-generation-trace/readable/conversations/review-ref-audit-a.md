# review ref audit A

**Generational Depth Estimation of Recursive Synthetic Text: Measuring the Discrimination Boundary** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 111
- **Recorded user turns:** 0
- **Tool calls:** 55
- **Original source:** `logs/chats/worker_review_ref-audit-A_20260526T104656.jsonl`
- **Structured JSON:** [`a34541c27380d866f0aa.json`](../../sessions/a3/a34541c27380d866f0aa.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

111 recorded events

### Tool call

_source line 1 · 2026-05-26T10:54:43.598273+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/references.bib"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_review_ref-audit-A_20260526T104656",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/references.bib"
  }
}
```

</details>

---

### Tool result

_source line 2 · 2026-05-26T10:54:43.598680+00:00_

1	% === References ===
2	
3	% === Must-Cite ===
4	
5	@inproceedings{kirchenbauer2023watermark,
6	  title     = {A Watermark for Large Language Models},
7	  author    = {John Kirchenbauer and Jonas Geiping and Yuxin Wen and Jonathan Katz and Ian Miers and Tom Goldstein},
8	  booktitle = {Proceedings of the 40th International Conference on Machine Learning},
9	  year      = {2023},
10	  pages     = {17061--17084},
11	  publisher = {PMLR},
12	}
13	
14	@inproceedings{drayson2025,
15	  title={Machine-Generated Text Detection Prevents Language Model Collapse},
16	  author={Drayson, George and Yilmaz, Emine and Lampos, Vasileios},
17	  booktitle={Proceedings of EMNLP},
18	  year={2025},
19	  url={https://arxiv.org/abs/2502.15654}
20	}
21	
22	@article{schaeffer2025position,
23	  title={Position: Model Collapse Does Not Mean What You Think},
24	  author={Schaeffer, Rylan and Kazdan, Joshua and Arulandu, Alvan Caleb and Koyejo, Sanmi},
25	  journal={arXiv preprint arXiv:2503.03150},
26	  year={2025},
27	  url={https://arxiv.org/abs/2503.03150}
28	}
29	
30	@inproceedings{kazdan2025collapse,
31	  title={Collapse or Thrive? Perils and Promises of Synthetic Data in a Self-Generating World},
32	  author={Kazdan, Joshua and Schaeffer, Rylan and Dey, Apratim and Gerstgrasser, Matthias and Rafailov, Rafael and Donoho, David and Koyejo, Sanmi},
33	  booktitle={Proceedings of ICML},
34	  year={2025},
35	  url={https://arxiv.org/abs/2410.16713}
36	}
37	
38	@inproceedings{mitchell2023detectgpt,
39	  title={{DetectGPT}: Zero-Shot Machine-Generated Text Detection using Probability Curvature},
40	  author={Mitchell, Eric and Lee, Yoonho and Khazatsky, Alexander and Manning, Christopher D. and Finn, Chelsea},
41	  booktitle={Proceedings of ICML},
42	  year={2023},
43	  url={https://arxiv.org/abs/2301.11305}
44	}
45	
46	% === Should-Cite ===
47	
48	@article{basani2026diveye,
49	  title={Diversity Boosts {AI}-Generated Text Detection},
50	  author={Basani, Advik Raj and Chen, Pin-Yu},
51	  jou
…[truncated 12186 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_review_ref-audit-A_20260526T104656",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-26T10:54:43.598942+00:00_

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
  "session": "worker_review_ref-audit-A_20260526T104656",
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

_source line 4 · 2026-05-26T10:54:43.599092+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_review_ref-audit-A_20260526T104656",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-26T10:54:43.599242+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Kirchenbauer \"A Watermark for Large Language Models\" ICML 2023"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_review_ref-audit-A_20260526T104656",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Kirchenbauer \"A Watermark for Large Language Models\" ICML 2023"
  }
}
```

</details>

---

### Tool call

_source line 6 · 2026-05-26T10:54:43.599368+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Drayson \"Machine-Generated Text Detection Prevents Language Model Collapse\" EMNLP 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_review_ref-audit-A_20260526T104656",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Drayson \"Machine-Generated Text Detection Prevents Language Model Collapse\" EMNLP 2025"
  }
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-26T10:54:43.599488+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Schaeffer \"Position: Model Collapse Does Not Mean What You Think\" arXiv 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_review_ref-audit-A_20260526T104656",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Schaeffer \"Position: Model Collapse Does Not Mean What You Think\" arXiv 2025"
  }
}
```

</details>

---

### Tool call

_source line 8 · 2026-05-26T10:54:43.599607+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Kazdan \"Collapse or Thrive? Perils and Promises of Synthetic Data\" ICML 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_review_ref-audit-A_20260526T104656",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Kazdan \"Collapse or Thrive? Perils and Promises of Synthetic Data\" ICML 2025"
  }
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-26T10:54:43.599723+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Mitchell \"DetectGPT Zero-Shot Machine-Generated Text Detection\" ICML 2023"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_review_ref-audit-A_20260526T104656",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Mitchell \"DetectGPT Zero-Shot Machine-Generated Text Detection\" ICML 2023"
  }
}
```

</details>

---

### Tool call

_source line 10 · 2026-05-26T10:54:43.599886+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Basani \"Diversity Boosts AI-Generated Text Detection\" TMLR 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_review_ref-audit-A_20260526T104656",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Basani \"Diversity Boosts AI-Generated Text Detection\" TMLR 2026"
  }
}
```

</details>

---

### Tool result

_source line 11 · 2026-05-26T10:54:43.600051+00:00_

Web search results for query: "Drayson "Machine-Generated Text Detection Prevents Language Model Collapse" EMNLP 2025"

Links: [{"title":"[2502.15654] Machine-generated text detection prevents language model collapse","url":"https://arxiv.org/abs/2502.15654"},{"title":"(PDF) Machine-generated text detection prevents language model collapse","url":"https://www.researchgate.net/publication/397412242_Machine-generated_text_detection_prevents_language_model_collapse"},{"title":"Machine-generated text detection prevents language model collapse","url":"https://arxiv.org/html/2502.15654"},{"title":"Machine-generated text detection prevents language model ...","url":"https://discovery.ucl.ac.uk/id/eprint/10217226/1/2025.emnlp-main.1506.pdf"},{"title":"Machine-generated text detection prevents language ...","url":"https://omega.cs.ucl.ac.uk/assets/pdf/papers/drayson2025-model-collapse.pdf"},{"title":"Machine-generated text detection prevents language model collapse - UCL Discovery","url":"https://discovery.ucl.ac.uk/id/eprint/10217226/"},{"title":"GitHub - GeorgeDrayson/model_collapse","url":"https://github.com/GeorgeDrayson/model_collapse"},{"title":"Computation and Language Feb 2025","url":"https://www.arxiv.org/list/cs.CL/2025-02?skip=1325&show=250"},{"title":"Learning by Surprise: Surplexity for Mitigating Model Collapse in Generative AI","url":"https://arxiv.org/html/2410.12341v3"}]

I found the paper you were searching for. Here's what I found:

The paper "Machine-generated text detection prevents language model collapse" by George Drayson, Emine Yilmaz, and Vasileios Lampos was accepted to and presented at the 2025 Conference on Empirical Methods in Natural Language Processing (EMNLP 2025) in Suzhou, China.

The paper addresses the problem that as LLMs become more prevalent, their generated outputs proliferate across the web, risking dilution of human-authored text. Since online data is the primary resource for LLM pre-training, subsequent models could be trained on s
…[truncated 637 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_review_ref-audit-A_20260526T104656",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-26T10:54:43.600235+00:00_

Web search results for query: "Schaeffer "Position: Model Collapse Does Not Mean What You Think" arXiv 2025"

Links: [{"title":"[2503.03150] Position: Model Collapse Does Not Mean What You Think","url":"https://arxiv.org/abs/2503.03150"},{"title":"Position: Model Collapse Does Not Mean What You Think","url":"https://arxiv.org/pdf/2503.03150"},{"title":"1 Introduction","url":"https://arxiv.org/html/2503.03150v2"},{"title":"A Closer Look at Model Collapse: From a Generalization-to-Memorization Perspective","url":"https://arxiv.org/html/2509.16499v1"},{"title":"LLM Web Dynamics: Tracing Model Collapse in a Network of LLMs","url":"https://arxiv.org/html/2506.15690v1"},{"title":"Position: Model Collapse Does Not Mean What You Think - ADS","url":"https://ui.adsabs.harvard.edu/abs/2025arXiv250303150S/abstract"},{"title":"Escaping Collapse: The Strength of Weak Data for Large Language Model TrainingAuthors ordered alphabetically. Author contributions are listed at the end.","url":"https://arxiv.org/html/2502.08924v2"},{"title":"Computers and Society Mar 2025","url":"https://arxiv.org/list/cs.CY/2025-03?skip=300&show=25"},{"title":"Escaping Model Collapse via Synthetic Data Verification: Near-term Improvements and Long-term ConvergenceThis project is supported by the AI2050 program at Schmidt Sciences (Grant G-24-66104) and Army Research Office Award W911NF-23-1-0030. We also thank Cong Ma from UChicago, Hongning Wang and Bo Li from Tsinghua, Pinyan Lu and Gavin Tang from Shanghai University of Finance and Economics for helpful discussions and suggestions.","url":"https://arxiv.org/html/2510.16657v1"},{"title":"When Models Don’t Collapse: On the Consistency of Iterative MLE","url":"https://arxiv.org/html/2505.19046v1"}]

I found the paper you're looking for. Here are the key details:

**Title:** Position: Model Collapse Does Not Mean What You Think

**Authors:** Rylan Schaeffer, Joshua Kazdan, Alvan Caleb Arulandu, and Sanmi Koyejo

**arXiv ID:** arXiv:2503.03150

**Publicat
…[truncated 813 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_review_ref-audit-A_20260526T104656",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 13 · 2026-05-26T10:54:43.600414+00:00_

Web search results for query: "Kirchenbauer "A Watermark for Large Language Models" ICML 2023"

Links: [{"title":"ICML Poster A Watermark for Large Language Models","url":"https://icml.cc/virtual/2023/poster/24544"},{"title":"dblp: A Watermark for Large Language Models.","url":"https://dblp.org/rec/conf/icml/KirchenbauerGWK23.html"},{"title":"A Watermark for Large Language Models","url":"https://proceedings.mlr.press/v202/kirchenbauer23a.html"},{"title":"[2301.10226] A Watermark for Large Language Models","url":"https://arxiv.org/abs/2301.10226"},{"title":"A Watermark for Large Language Models - TL;DR With Paper Author","url":"https://arize.com/blog/a-watermark-for-large-language-models/"},{"title":"A Resilient and Accessible Distribution-Preserving Watermark for Large   Language Models","url":"https://arxiv.org/pdf/2310.07710"},{"title":"A Watermark for Large Language Models | Request PDF","url":"https://www.researchgate.net/publication/367388838_A_Watermark_for_Large_Language_Models"},{"title":"Necessary and Sufficient Watermark for Large Language Models","url":"https://arxiv.org/pdf/2310.00833"}]

Based on the search results, here's information about the paper:

## "A Watermark for Large Language Models" by Kirchenbauer et al., ICML 2023

The paper addresses watermarking model output by embedding signals into generated text that are invisible to humans but algorithmically detectable from a short span of tokens.

**Key Contributions:**
- The authors propose a watermarking framework for proprietary language models that can be embedded with negligible impact on text quality and detected using an efficient open-source algorithm without access to the language model API or parameters.

**Technical Approach:**
The watermark works by selecting a randomized set of "green" tokens before a word is generated, and then softly promoting use of green tokens during sampling.

**Analysis and Testing:**
The authors propose a statistical test for detecting the watermark with interp
…[truncated 631 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_review_ref-audit-A_20260526T104656",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-26T10:54:43.600590+00:00_

Web search results for query: "Basani "Diversity Boosts AI-Generated Text Detection" TMLR 2026"

Links: [{"title":"GitHub - IBM/diveye: [TMLR '26] Code for Diversity Boosts AI-generated Text Detection · GitHub","url":"https://github.com/IBM/diveye"},{"title":"Diversity Boosts AI-Generated Text Detection","url":"https://arxiv.org/html/2509.18880v1"},{"title":"Pin-Yu Chen on X: \"Happy to see this work published at @TmlrOrg We show that diversity-driven features (computed by a very small LM, such as GPT-2) are powerful for detecting AI-written content. Try out our online detector at https://t.co/7sLfMdcmDG Kudos to Advik for leading this work.\" / X","url":"https://x.com/pinyuchenTW/status/2031014939846995984"},{"title":"[2509.18880] Diversity Boosts AI-Generated Text Detection","url":"https://arxiv.org/abs/2509.18880"},{"title":"Diversity Boosts AI-Generated Text Detection Advik Raj Basani 1 Pin-Yu Chen 2","url":"https://openreview.net/pdf?id=QuDDXJ47nq"},{"title":"Diversity Boosts AI-Generated Text Detection","url":"https://www.arxiv.org/pdf/2509.18880v1"},{"title":"Diversity Boosts AI-Generated Text Detection","url":"https://arxiv.org/pdf/2509.18880"},{"title":"Diversity Boosts AI-Generated Text Detection | OpenReview","url":"https://openreview.net/forum?id=DNgsOhGZBI"},{"title":"[PDF] Diversity Boosts AI-Generated Text Detection | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Diversity-Boosts-AI-Generated-Text-Detection-Basani-Chen/77269d404ea3438f6d2ac327316f0b6ba116a48d"},{"title":"[PDF] DivEye at PAN 2025: Diversity Boosts AI-Generated Text Detection | Semantic Scholar","url":"https://www.semanticscholar.org/paper/DivEye-at-PAN-2025:-Diversity-Boosts-AI-Generated-Basani-Chen/b18cdaf7ea2898664ed0850790059278ed50bb79"}]

Based on the search results, I found information about this paper. Here are the key details:

**Paper Title:** Diversity Boosts AI-Generated Text Detection

**Authors:** Advik Raj Basani and Pin-Yu Chen

**Publication Status:** A
…[truncated 875 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_review_ref-audit-A_20260526T104656",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 15 · 2026-05-26T10:54:43.600763+00:00_

Web search results for query: "Kazdan "Collapse or Thrive? Perils and Promises of Synthetic Data" ICML 2025"

Links: [{"title":"[2410.16713] Collapse or Thrive? Perils and Promises of Synthetic Data in a Self-Generating World","url":"https://arxiv.org/abs/2410.16713"},{"title":"Collapse or Thrive? Perils and Promises of Synthetic Data in a Self-Generating World","url":"https://arxiv.org/html/2410.16713v2"},{"title":"Collapse or Thrive? Perils and Promises of Synthetic Data in a Self-Generating World | OpenReview","url":"https://openreview.net/forum?id=Xr5iINA3zU"},{"title":"1 Introduction","url":"https://arxiv.org/html/2410.16713"},{"title":"[PDF] Collapse or Thrive? Perils and Promises of Synthetic Data in a Self-Generating World | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Collapse-or-Thrive-Perils-and-Promises-of-Synthetic-Kazdan-Schaeffer/4b510679ec7f6d138b04d5d0afff9ff316264974"},{"title":"(PDF) Collapse or Thrive? Perils and Promises of Synthetic Data in a Self-Generating World","url":"https://www.researchgate.net/publication/385140496_Collapse_or_Thrive_Perils_and_Promises_of_Synthetic_Data_in_a_Self-Generating_World"},{"title":"GitHub - RylanSchaeffer/KoyejoLab-Collapse-or-Thrive: Code for Collapse or Thrive? Perils and Promises of Synthetic Data in a Self-Generating World","url":"https://github.com/RylanSchaeffer/KoyejoLab-Collapse-or-Thrive"},{"title":"Position: Model Collapse Does Not Mean What You Think","url":"https://arxiv.org/pdf/2503.03150"},{"title":"Strong Model Collapse","url":"https://arxiv.org/pdf/2410.04840"}]

Based on the search results, I found the paper you're looking for:

"Collapse or Thrive? Perils and Promises of Synthetic Data in a Self-Generating World" is by Joshua Kazdan and 6 other authors. The full author list is Joshua Kazdan, Rylan Schaeffer, Apratim Dey, Matthias Gerstgrasser, Rafael Rafailov, David Donoho, and Sanmi Koyejo from Stanford Statistics and Stanford Computer Science.

The paper addresses what hap
…[truncated 932 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_review_ref-audit-A_20260526T104656",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-26T10:54:43.600961+00:00_

Web search results for query: "Mitchell "DetectGPT Zero-Shot Machine-Generated Text Detection" ICML 2023"

Links: [{"title":"ICML Oral DetectGPT: Zero-Shot Machine-Generated Text Detection using Probability Curvature","url":"https://icml.cc/virtual/2023/oral/25525"},{"title":"Eric Mitchell, Yoonho Lee, Alexander Khazatsky, Christopher D. Manning, Chelsea Finn · DetectGPT: Zero-Shot Machine-Generated Text Detection using Probability Curvature","url":"https://slideslive.com/39004346/detectgpt-zeroshot-machinegenerated-text-detection-using-probability-curvature"},{"title":"dblp: DetectGPT: Zero-Shot Machine-Generated Text Detection using Probability Curvature.","url":"https://dblp.org/rec/conf/icml/Mitchell0KMF23.html"},{"title":"DetectGPT: Zero-Shot Machine-Generated Text Detection using Probability   Curvature","url":"https://arxiv.org/pdf/2301.11305"},{"title":"[2301.11305] DetectGPT: Zero-Shot Machine-Generated Text Detection using Probability Curvature","url":"https://arxiv.org/abs/2301.11305"},{"title":"[Paper Note] DetectGPT: Zero-Shot Machine-Generated Text Detection using Probability Curvature, Eric Mitchell+, ICML'23, 2023.01 · Issue #3698 · AkihikoWatanabe/paper_notes","url":"https://github.com/AkihikoWatanabe/paper_notes/issues/3698"},{"title":"DetectGPT: Zero-Shot Machine-Generated Text Detection using Probability Curvature [Quick Review]","url":"https://liner.com/review/detectgpt-zeroshot-machinegenerated-text-detection-using-probability-curvature"},{"title":"DetectGPT: Zero-Shot Machine-Generated Text Detection using Probability Curvature","url":"https://proceedings.mlr.press/v202/mitchell23a.html"},{"title":"DetectGPT: zero-shot machine-generated text detection ...","url":"https://dl.acm.org/doi/10.5555/3618408.3619446"}]

Based on the search results, here's what I found about the paper:

**Title and Authors:** DetectGPT: Zero-Shot Machine-Generated Text Detection using Probability Curvature was authored by Eric Mitchell, Yoonho Lee, Alexander Khazatsky
…[truncated 1061 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_review_ref-audit-A_20260526T104656",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-26T10:54:43.601140+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Zawalski \"Detecting Data Contamination in LLMs via In-Context Learning\" ICLR 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_review_ref-audit-A_20260526T104656",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Zawalski \"Detecting Data Contamination in LLMs via In-Context Learning\" ICLR 2026"
  }
}
```

</details>

---

### Tool call

_source line 18 · 2026-05-26T10:54:43.601271+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Zhang \"Min-K%++ Improved Baseline Detecting Pre-Training Data\" ICLR 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_review_ref-audit-A_20260526T104656",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Zhang \"Min-K%++ Improved Baseline Detecting Pre-Training Data\" ICLR 2025"
  }
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-26T10:54:43.601392+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Shumailov \"AI Models Collapse When Trained on Recursively Generated Data\" Nature 2024"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_review_ref-audit-A_20260526T104656",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Shumailov \"AI Models Collapse When Trained on Recursively Generated Data\" Nature 2024"
  }
}
```

</details>

---

### Tool call

_source line 20 · 2026-05-26T10:54:43.601509+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Alemohammad \"Self-Consuming Generative Models Go MAD\" ICLR 2024"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_review_ref-audit-A_20260526T104656",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Alemohammad \"Self-Consuming Generative Models Go MAD\" ICLR 2024"
  }
}
```

</details>

---

### Tool call

_source line 21 · 2026-05-26T10:54:43.601624+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Dohmatob \"A Tale of Tails: Model Collapse as a Change of Scaling Laws\" ICML 2024"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_review_ref-audit-A_20260526T104656",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Dohmatob \"A Tale of Tails: Model Collapse as a Change of Scaling Laws\" ICML 2024"
  }
}
```

</details>

---

### Tool call

_source line 22 · 2026-05-26T10:54:43.601768+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Xie \"Data Selection for Language Models via Importance Resampling\" NeurIPS 2023"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_review_ref-audit-A_20260526T104656",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Xie \"Data Selection for Language Models via Importance Resampling\" NeurIPS 2023"
  }
}
```

</details>

---

### Tool result

_source line 23 · 2026-05-26T10:54:43.601948+00:00_

Web search results for query: "Zawalski "Detecting Data Contamination in LLMs via In-Context Learning" ICLR 2026"

Links: [{"title":"[2510.27055] Detecting Data Contamination in LLMs via In-Context Learning","url":"https://arxiv.org/abs/2510.27055"},{"title":"Detecting Data Contamination in LLMs via In-Context Learning","url":"https://arxiv.org/html/2510.27055v1"},{"title":"Detecting Data Contamination in LLMs via In-Context Learning Michał Zawalski†","url":"https://openreview.net/pdf/753f569951799d9078f4db2d0e9debd74ad5b692.pdf"},{"title":"Detecting Data Contamination in LLMs via In-Context ...","url":"https://openreview.net/pdf?id=YlpaaYxx4t"},{"title":"Detecting Data Contamination in LLMs via In-Context Learning | OpenReview","url":"https://openreview.net/forum?id=YlpaaYxx4t"},{"title":"Published as a conference paper at ICLR 2026","url":"https://openreview.net/pdf?id=W8VCH9x1HZ"},{"title":"ICLR 2026: Detecting Data Contamination in LLMs via In- ...","url":"https://www.linkedin.com/posts/besmira-nushi-43969712_our-work-on-data-contamination-analysis-was-activity-7422343437376561152-O2kU"},{"title":"Detecting Data Contamination in LLMs via In-Context ...","url":"https://www.researchgate.net/publication/397188985_Detecting_Data_Contamination_in_LLMs_via_In-Context_Learning"},{"title":"[2510.09259] Detecting Data Contamination from Reinforcement Learning Post-training for Large Language Models","url":"https://arxiv.org/abs/2510.09259"}]

I found the paper you're looking for! Here are the key details:

The paper "Detecting Data Contamination in LLMs via In-Context Learning" by Zawalski and colleagues was published as a conference paper at ICLR 2026.

**Key Information:**

The authors are Michał Zawalski, Meriem Boubdir, Klaudia Bałazy, Besmira Nushi, and Pablo Ribalta from NVIDIA.

**What the Paper Presents:**

The paper presents Contamination Detection via Context (CoDeC), a practical and accurate method to detect and quantify training data contamination in large la
…[truncated 750 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_review_ref-audit-A_20260526T104656",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 24 · 2026-05-26T10:54:43.602131+00:00_

Web search results for query: "Zhang "Min-K%++ Improved Baseline Detecting Pre-Training Data" ICLR 2025"

Links: [{"title":"GitHub - zjysteven/mink-plus-plus: [ICLR'25 Spotlight] Min-K%++: Improved baseline for detecting pre-training data of LLMs · GitHub","url":"https://github.com/zjysteven/mink-plus-plus"},{"title":"MIN-K%++: IMPROVED BASELINE FOR DETECTING PRE ...","url":"https://proceedings.iclr.cc/paper_files/paper/2025/file/a2e3b4132ab2e0b7a21e6e75da7f91a9-Paper-Conference.pdf"},{"title":"[2404.02936] Min-K%++: Improved Baseline for Detecting Pre-Training Data from Large Language Models","url":"https://arxiv.org/abs/2404.02936"},{"title":"MIN-K%++: IMPROVED BASELINE FOR DETECTING PRE ...","url":"https://openreview.net/pdf?id=ZGkfoufDaU"},{"title":"min-k%++: improved baseline for detecting pre-training ...","url":"https://arxiv.org/pdf/2404.02936"},{"title":"ICLR Poster Min-K%++: Improved Baseline for Pre-Training Data Detection from Large Language Models","url":"https://iclr.cc/virtual/2025/poster/29228"},{"title":"Min-K%++: Improved Baseline for Pre-Training Data Detection from Large Language Models | OpenReview","url":"https://openreview.net/forum?id=ZGkfoufDaU"},{"title":"Min-K%++: Improved Baseline for Detecting Pre-Training Data from Large Language Models","url":"https://arxiv.org/html/2404.02936v1"},{"title":"Min-K%++: Improved Baseline for Detecting Pre-Training ...","url":"https://zjysteven.github.io/mink-plus-plus/"}]

I found the paper! Here are the details about the research:

Min-K%++ is a new Membership Inference Attack method for detecting pre-training data of LLMs, which achieves state-of-the-art results among reference-free methods.

**Paper Information:**
- Published at The Thirteenth International Conference on Learning Representations (ICLR 2025)
- Accepted as an ICLR 2025 Spotlight paper
- Authors: Jingyang Zhang, Jingwei Sun, Eric Yeats, Yang Ouyang, Martin Kuo, Jianyi Zhang, Hao Yang, and Hai Li from Duke University and Johns Hopkins Univ
…[truncated 864 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_review_ref-audit-A_20260526T104656",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 25 · 2026-05-26T10:54:43.602312+00:00_

Web search results for query: "Shumailov "AI Models Collapse When Trained on Recursively Generated Data" Nature 2024"

Links: [{"title":"AI models collapse when trained on recursively generated data | Nature","url":"https://www.nature.com/articles/s41586-024-07566-y"},{"title":"A Note on Shumailov et al. (2024): ‘AI Models Collapse When Trained on Recursively Generated Data’","url":"https://arxiv.org/html/2410.12954v2"},{"title":"AI models collapse when trained on recursively generated data - PubMed","url":"https://pubmed.ncbi.nlm.nih.gov/39048682/"},{"title":"[PDF] AI models collapse when trained on recursively generated data | Semantic Scholar","url":"https://www.semanticscholar.org/paper/AI-models-collapse-when-trained-on-recursively-data-Shumailov-Shumaylov/603d3f90fc40f79ff51258f0295de3ec5107f73e"},{"title":"A note on “AI models collapse when trained on recursively generated data” | by Ali Borji | Medium","url":"https://medium.com/@aliborji/a-note-on-ai-models-collapse-when-trained-on-recursively-generated-data-5bee1de1ab87"},{"title":"AI models collapse when trained on recursively generated data","url":"https://www.pure.ed.ac.uk/ws/portalfiles/portal/460496122/ShumailovEtalNature2024AIModelsCollapseWhen.pdf"},{"title":"A Note on Shumailov et al. (2024): 'AI Models Collapse ...","url":"https://arxiv.org/pdf/2410.12954"},{"title":"[2410.12954] A Note on Shumailov et al. (2024): `AI Models Collapse When Trained on Recursively Generated Data'","url":"https://arxiv.org/abs/2410.12954"},{"title":"Author Correction: AI models collapse when trained on recursively generated data | Nature","url":"https://www.nature.com/articles/s41586-025-08905-3"},{"title":"dblp: AI models collapse when trained on recursively generated data.","url":"https://dblp.org/rec/journals/nature/ShumailovSZPAG24.html"}]

I found the research paper you're looking for. Here's what I discovered:

## Paper Details

The paper "AI models collapse when trained on recursively generated data" was publish
…[truncated 1128 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_review_ref-audit-A_20260526T104656",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 26 · 2026-05-26T10:54:43.602491+00:00_

Web search results for query: "Dohmatob "A Tale of Tails: Model Collapse as a Change of Scaling Laws" ICML 2024"

Links: [{"title":"[2402.07043] A Tale of Tails: Model Collapse as a Change of Scaling Laws","url":"https://arxiv.org/abs/2402.07043"},{"title":"ICML Poster A Tale of Tails: Model Collapse as a Change of Scaling Laws","url":"https://icml.cc/virtual/2024/poster/34339"},{"title":"[Quick Review] A Tale of Tails: Model Collapse as a Change of Scaling Laws","url":"https://liner.com/review/tale-tails-model-collapse-as-change-scaling-laws"},{"title":"A Tale of Tails: Model Collapse as a Change of Scaling Laws","url":"https://proceedings.mlr.press/v235/dohmatob24b.html"},{"title":"Overcoming the AI Data Crisis: A New Solution to Model Collapse | by NYU Center for Data Science | Medium","url":"https://nyudatascience.medium.com/overcoming-the-ai-data-crisis-a-new-solution-to-model-collapse-ddc5b382e182"},{"title":"A Tale of Tails: Model Collapse as a Change of Scaling Laws - NYU Scholars","url":"https://nyuscholars.nyu.edu/en/publications/a-tale-of-tails-model-collapse-as-a-change-of-scaling-laws"},{"title":"A Tale of Tails: Model Collapse as a Change of Scaling Laws | OpenReview","url":"https://openreview.net/forum?id=KVvku47shW"},{"title":"A tale of tails: model collapse as a change of scaling laws","url":"https://dl.acm.org/doi/10.5555/3692070.3692515"},{"title":"A Tale of Tails: Model Collapse as a Change of Scaling Laws | NSF Public Access Repository","url":"https://par.nsf.gov/biblio/10535859"},{"title":"A Tale of Tails: Model Collapse as a Change of Scaling Laws | AI Research Paper Details","url":"https://www.aimodels.fyi/papers/arxiv/tale-tails-model-collapse-as-change-scaling"}]

I found the paper! Here's what I discovered:

"A Tale of Tails: Model Collapse as a Change of Scaling Laws" by Dohmatob, Elvis; Feng, Yunzhen; Yang, Pu; Charton, Francois; and Kempe, Julia was published in the Proceedings of the 41st International Conference on Machine Learning (I
…[truncated 934 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_review_ref-audit-A_20260526T104656",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 27 · 2026-05-26T10:54:43.602668+00:00_

Web search results for query: "Alemohammad "Self-Consuming Generative Models Go MAD" ICLR 2024"

Links: [{"title":"SELF-CONSUMING GENERATIVE MODELS GO MAD","url":"https://proceedings.iclr.cc/paper_files/paper/2024/file/ebc042e767de551803ccfcc45e2454f5-Paper-Conference.pdf"},{"title":"Self-Consuming Generative Models Go MAD | OpenReview","url":"https://openreview.net/forum?id=ShjMHfmPs0"},{"title":"SELF-CONSUMING GENERATIVE MODELS GO MAD - Houston Methodist Scholars","url":"https://scholars.houstonmethodist.org/en/publications/self-consuming-generative-models-go-mad/"},{"title":"[PDF] Self-Consuming Generative Models Go MAD | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Self-Consuming-Generative-Models-Go-MAD-Alemohammad-Casco-Rodriguez/ad022cd5da75637ac3e0a8f8cc4f0d394ba5ff7a"},{"title":"Self-Consuming Generative Models Go MAD | NSF Public Access Repository","url":"https://par.nsf.gov/biblio/10570494"},{"title":"ICLR Poster Self-Consuming Generative Models Go MAD","url":"https://iclr.cc/virtual/2024/poster/18592"},{"title":"Self-Consuming AI Resources","url":"https://dsp.rice.edu/ai-loops/"},{"title":"[2307.01850] Self-Consuming Generative Models Go MAD","url":"https://arxiv.org/abs/2307.01850"},{"title":"Self-Consuming Generative Models Go MAD | Montreal AI Ethics Institute","url":"https://montrealethics.ai/self-consuming-generative-models-go-mad/"}]

I found the paper! Here's a summary of the research:

## "Self-Consuming Generative Models Go MAD"

The paper by Alemohammad, Casco-Rodriguez, Luzi, and colleagues was presented at the 12th International Conference on Learning Representations (ICLR 2024) in Vienna, Austria.

**Main Findings:**

The paper addresses the temptation to use AI-synthesized data to train next-generation models, and examines the properties of autophagous ("self-consuming") loops created by repeating this process.

The key conclusion is that without enough fresh real data in each generation of an autophagous loop, future gene
…[truncated 734 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_review_ref-audit-A_20260526T104656",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 28 · 2026-05-26T10:54:43.602862+00:00_

Web search results for query: "Xie "Data Selection for Language Models via Importance Resampling" NeurIPS 2023"

Links: [{"title":"NeurIPS Poster Data Selection for Language Models via Importance Resampling","url":"https://neurips.cc/virtual/2023/poster/70154"},{"title":"Data Selection for Language Models via Importance Resampling","url":"https://proceedings.neurips.cc//paper_files/paper/2023/hash/6b9aa8f418bde2840d5f4ab7a02f663b-Abstract-Conference.html"},{"title":"[2302.03169] Data Selection for Language Models via Importance Resampling","url":"https://arxiv.org/abs/2302.03169"},{"title":"Data Selection for Language Models via Importance Resampling","url":"https://openreview.net/pdf?id=uPSQv0leAu"},{"title":"Data Selection for Language Models via Importance Resampling | OpenReview","url":"https://openreview.net/forum?id=uPSQv0leAu"},{"title":"Data Selection for Language Models via Importance Resampling","url":"https://www.researchgate.net/publication/368333487_Data_Selection_for_Language_Models_via_Importance_Resampling"},{"title":"[PDF] Data Selection for Language Models via Importance Resampling | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Data-Selection-for-Language-Models-via-Importance-Xie-Santurkar/74013b7cfa0fc524803350fca51341004565eb22"},{"title":"[2302.03169v3] Data Selection for Language Models via Importance Resampling","url":"http://arxiv.org/abs/2302.03169v3"},{"title":"Data Selection for Language Models via Importance Resampling - ADS","url":"https://ui.adsabs.harvard.edu/abs/2023arXiv230203169X/abstract"},{"title":"GitHub - p-lambda/dsir: DSIR large-scale data selection framework for language model training · GitHub","url":"https://github.com/p-lambda/dsir"}]

I found the paper! Here's what the search reveals:

"Data Selection for Language Models via Importance Resampling" is by Sang Michael Xie, Shibani Santurkar, Tengyu Ma, and Percy Liang, published at NeurIPS 2023.

The paper proposes Data Selection with Importance Resamplin
…[truncated 1042 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_review_ref-audit-A_20260526T104656",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool call

_source line 29 · 2026-05-26T10:54:43.603046+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Tirumala \"D4 Improving LLM Pretraining via Document De-Duplication and Diversification\" NeurIPS 2023"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_review_ref-audit-A_20260526T104656",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Tirumala \"D4 Improving LLM Pretraining via Document De-Duplication and Diversification\" NeurIPS 2023"
  }
}
```

</details>

---

### Tool call

_source line 30 · 2026-05-26T10:54:43.603176+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Xie \"DoReMi Optimizing Data Mixtures Speeds Up Language Model Pretraining\" NeurIPS 2023"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_review_ref-audit-A_20260526T104656",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Xie \"DoReMi Optimizing Data Mixtures Speeds Up Language Model Pretraining\" NeurIPS 2023"
  }
}
```

</details>

---

### Tool call

_source line 31 · 2026-05-26T10:54:43.603296+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Hans \"Spotting LLMs With Binoculars\" ICML 2024"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_review_ref-audit-A_20260526T104656",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Hans \"Spotting LLMs With Binoculars\" ICML 2024"
  }
}
```

</details>

---

### Tool call

_source line 32 · 2026-05-26T10:54:43.603412+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Alain Bengio \"Understanding Intermediate Layers Using Linear Classifier Probes\" ICLR 2017"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_review_ref-audit-A_20260526T104656",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Alain Bengio \"Understanding Intermediate Layers Using Linear Classifier Probes\" ICLR 2017"
  }
}
```

</details>

---

### Tool call

_source line 33 · 2026-05-26T10:54:43.603526+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Belinkov \"Probing Classifiers: Promises, Shortcomings, and Advances\" Computational Linguistics 2022"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_review_ref-audit-A_20260526T104656",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Belinkov \"Probing Classifiers: Promises, Shortcomings, and Advances\" Computational Linguistics 2022"
  }
}
```

</details>

---

### Tool call

_source line 34 · 2026-05-26T10:54:43.603638+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Bao \"Fast-DetectGPT Efficient Zero-Shot Detection Machine-Generated Text\" ICLR 2024"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_review_ref-audit-A_20260526T104656",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Bao \"Fast-DetectGPT Efficient Zero-Shot Detection Machine-Generated Text\" ICLR 2024"
  }
}
```

</details>

---

### Tool result

_source line 35 · 2026-05-26T10:54:43.603804+00:00_

Web search results for query: "Tirumala "D4 Improving LLM Pretraining via Document De-Duplication and Diversification" NeurIPS 2023"

Links: [{"title":"D4: Improving LLM Pretraining via Document De-Duplication and Diversification","url":"https://proceedings.neurips.cc/paper_files/paper/2023/hash/a8f8cbd7f7a5fb2c837e578c75e5b615-Abstract-Datasets_and_Benchmarks.html"},{"title":"D4: Improving LLM Pretraining via Document De-Duplication and Diversiﬁcation","url":"https://proceedings.neurips.cc/paper_files/paper/2023/file/a8f8cbd7f7a5fb2c837e578c75e5b615-Paper-Datasets_and_Benchmarks.pdf"},{"title":"NeurIPS Poster D4: Improving LLM Pretraining via Document De-Duplication and Diversification","url":"https://neurips.cc/virtual/2023/poster/73662"},{"title":"[2308.12284] D4: Improving LLM Pretraining via Document De-Duplication and Diversification","url":"https://arxiv.org/abs/2308.12284"},{"title":"D4: Improving LLM Pretraining via Document De-Duplication and Diversification","url":"https://papers.nips.cc/paper_files/paper/2023/hash/a8f8cbd7f7a5fb2c837e578c75e5b615-Abstract-Datasets_and_Benchmarks.html"},{"title":"[PDF] D4: Improving LLM Pretraining via Document De-Duplication and Diversification | Semantic Scholar","url":"https://www.semanticscholar.org/paper/D4:-Improving-LLM-Pretraining-via-Document-and-Tirumala-Simig/11cf88dce827bd67cbfa60400306318022e736d5"},{"title":"D4: Improving LLM Pretraining via Document De-Duplication and Diversification | OpenReview","url":"https://openreview.net/forum?id=CG0L2PFrb1&noteId=CG0L2PFrb1"},{"title":"Kushal Tirumala, Daniel Simig, Armen Aghajanyan, Ari S. Morcos · D4: Improving LLM Pretraining via Document De-Duplication and Diversification","url":"https://slideslive.com/39010897/d4-improving-llm-pretraining-via-document-deduplication-and-diversification"},{"title":"Paper page - D4: Improving LLM Pretraining via Document De-Duplication and Diversification","url":"https://paperswithcode.com/paper/d4-improving-llm-pretraining-via-doc
…[truncated 1519 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_review_ref-audit-A_20260526T104656",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 36 · 2026-05-26T10:54:43.603996+00:00_

Web search results for query: "Alain Bengio "Understanding Intermediate Layers Using Linear Classifier Probes" ICLR 2017"

Links: [{"title":"[1610.01644] Understanding intermediate layers using linear classifier probes","url":"https://arxiv.org/abs/1610.01644"},{"title":"[PDF] Understanding intermediate layers using linear classifier probes | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Understanding-intermediate-layers-using-linear-Alain-Bengio/5e23a28063b395bdaf784dc548a046885cb90cf2"},{"title":"(PDF) Understanding intermediate layers using linear classifier probes","url":"https://www.researchgate.net/publication/308913017_Understanding_intermediate_layers_using_linear_classifier_probes"},{"title":"Understanding intermediate layers using linear classifier probes | Request PDF","url":"https://www.researchgate.net/publication/319770004_Understanding_intermediate_layers_using_linear_classifier_probes"},{"title":"iclr-2017-paper-collection/Understanding intermediate layers using linear classifier probes.pdf at master · zjmwqx/iclr-2017-paper-collection","url":"https://github.com/zjmwqx/iclr-2017-paper-collection/blob/master/Understanding%20intermediate%20layers%20using%20linear%20classifier%20probes.pdf"},{"title":"Understanding intermediate layers using linear classifier probes","url":"http://index.cslt.org/mediawiki/images/f/f6/Understanding_intermediate_layers_using_linear_classifier_probes.pdf"},{"title":"[1610.01644v3] Understanding intermediate layers using linear classifier probes","url":"https://arxiv.org/abs/1610.01644v3"},{"title":"[1610.01644v1] Understanding intermediate layers using linear classifier probes","url":"https://www.arxiv.org/abs/1610.01644v1"},{"title":"[1610.01644v4] Understanding intermediate layers using linear classifier probes","url":"https://arxiv.org/abs/1610.01644v4"}]

Based on the search results, I found information about this paper:

The paper "Understanding intermediate layers using linear classifier probes" is au
…[truncated 915 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_review_ref-audit-A_20260526T104656",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 37 · 2026-05-26T10:54:43.604171+00:00_

Web search results for query: "Hans "Spotting LLMs With Binoculars" ICML 2024"

Links: [{"title":"GitHub - ahans30/Binoculars: [ICML 2024] Binoculars: Zero-Shot Detection of LLM-Generated Text · GitHub","url":"https://github.com/ahans30/Binoculars"},{"title":"[2401.12070] Spotting LLMs With Binoculars: Zero-Shot Detection of Machine-Generated Text","url":"https://arxiv.org/abs/2401.12070"},{"title":"Spotting LLMs With Binoculars: Zero-Shot Detection of Machine-Generated Text","url":"https://proceedings.mlr.press/v235/hans24a.html"},{"title":"Spotting LLMs With Binoculars: Zero-Shot Detection of Machine-Generated Text | Safety- and Efficiency- aligned Learning – MPI-IS","url":"https://is.mpg.de/seal/publications/hans_spotting_2024"},{"title":"Spotting LLMs With Binoculars: Zero-Shot Detection of Machine-Generated Text | MPI-IS","url":"https://is.mpg.de/en/publications/hans_spotting_2024"},{"title":"[Quick Review] Spotting LLMs With Binoculars: Zero-Shot Detection of Machine-Generated Text","url":"https://liner.com/review/spotting-llms-with-binoculars-zeroshot-detection-machinegenerated-text"},{"title":"ICML Poster Spotting LLMs With Binoculars: Zero-Shot Detection of Machine-Generated Text","url":"https://icml.cc/virtual/2024/poster/33662"},{"title":"Spotting LLMs With Binoculars: Zero-Shot Detection of Machine-Generated Text | OpenReview","url":"https://openreview.net/forum?id=iARAKITHTH"},{"title":"Under review as a conference paper at ICLR 2024 SPOTTING LLMS WITH BINOCULARS:","url":"https://openreview.net/pdf?id=iARAKITHTH"}]

Based on the search results, I found the paper you're looking for:

"Spotting LLMs With Binoculars: Zero-Shot Detection of Machine-Generated Text" is a paper presented at ICML 2024 by Abhimanyu Hans, Avi Schwarzschild, Valeriia Cherepanova, Hamid Kazemi, Aniruddha Saha, Micah Goldblum, Jonas Geiping, and Tom Goldstein.

The paper introduces Binoculars, a method for detecting AI-generated text, and it is a zero-shot and domain-agnostic method
…[truncated 603 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_review_ref-audit-A_20260526T104656",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 38 · 2026-05-26T10:54:43.604353+00:00_

Web search results for query: "Belinkov "Probing Classifiers: Promises, Shortcomings, and Advances" Computational Linguistics 2022"

Links: [{"title":"Probing Classifiers: Promises, Shortcomings, and Advances - ACL Anthology","url":"https://aclanthology.org/2022.cl-1.7/"},{"title":"[2102.12452] Probing Classifiers: Promises, Shortcomings, and Advances","url":"https://arxiv.org/abs/2102.12452"},{"title":"Probing Classifiers: Promises, Shortcomings, and Advances | Computational Linguistics | MIT Press","url":"https://direct.mit.edu/coli/article/48/1/207/107571/Probing-Classifiers-Promises-Shortcomings-and"},{"title":"Yonatan Belinkov | publications","url":"https://belinkov.com/publications/publicationstype/"},{"title":"(PDF) Probing Classifiers: Promises, Shortcomings, and Advances","url":"https://www.researchgate.net/publication/355072709_Probing_Classifiers_Promises_Shortcomings_and_Advances"},{"title":"Probing Classifiers: Promises, Shortcomings, and Advances - Technion - Israel Institute of Technology","url":"https://cris.technion.ac.il/en/publications/probing-classifiers-promises-shortcomings-and-advances/"},{"title":"Probing Classifiers: Promises, Shortcomings, and Advances - Israeli Research Community Portal","url":"https://cris.iucc.ac.il/en/publications/probing-classifiers-promises-shortcomings-and-advances/"},{"title":"Probing Classifiers: Promises, Shortcomings, and Advances","url":"https://aclanthology.org/2022.cl-1.7.pdf"},{"title":"@article{belinkov-2022-probing,","url":"https://aclanthology.org/2022.cl-1.7.bib"},{"title":"Probing Classifiers: Promises, Shortcomings, and Advances","url":"https://scite.ai/reports/probing-classifiers-promises-shortcomings-and-kepAxaJ3"}]

I found the paper you're looking for! Here are the details:

**Title:** Probing Classifiers: Promises, Shortcomings, and Advances
**Author:** Yonatan Belinkov
**Journal:** Computational Linguistics
**Year:** 2022
**Volume/Issue:** 48(1)
**Pages:** 207–219

The paper addresses how probing 
…[truncated 794 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_review_ref-audit-A_20260526T104656",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 39 · 2026-05-26T10:54:43.604533+00:00_

Web search results for query: "Xie "DoReMi Optimizing Data Mixtures Speeds Up Language Model Pretraining" NeurIPS 2023"

Links: [{"title":"DoReMi: Optimizing Data Mixtures Speeds Up Language Model Pretraining","url":"https://proceedings.neurips.cc/paper_files/paper/2023/file/dcba6be91359358c2355cd920da3fcbd-Paper-Conference.pdf"},{"title":"[2305.10429] DoReMi: Optimizing Data Mixtures Speeds Up Language Model Pretraining","url":"https://arxiv.org/abs/2305.10429"},{"title":"DoReMi: Optimizing Data Mixtures Speeds Up Language Model Pretraining | OpenReview","url":"https://openreview.net/forum?id=lXuByUeHhd"},{"title":"NeurIPS Poster DoReMi: Optimizing Data Mixtures Speeds Up Language Model Pretraining","url":"https://neurips.cc/virtual/2023/poster/70588"},{"title":"DoReMi: Optimizing Data Mixtures Speeds Up Language Model Pretraining | Request PDF","url":"https://www.researchgate.net/publication/401463528_DoReMi_Optimizing_Data_Mixtures_Speeds_Up_Language_Model_Pretraining"},{"title":"DoReMi: Optimizing Data Mixtures Speeds Up Language Model Pretraining - ADS","url":"https://ui.adsabs.harvard.edu/abs/2023arXiv230510429X/abstract"},{"title":"[PDF] DoReMi: Optimizing Data Mixtures Speeds Up Language Model Pretraining | Semantic Scholar","url":"https://www.semanticscholar.org/paper/DoReMi:-Optimizing-Data-Mixtures-Speeds-Up-Language-Xie-Pham/9b4f7c97c0b83a80c32bc0b93595cbcfb4ecb16d"},{"title":"GitHub - sangmichaelxie/doremi: Pytorch implementation of DoReMi, a method for optimizing the data mixture weights in language modeling datasets · GitHub","url":"https://github.com/sangmichaelxie/doremi"},{"title":"[Quick Review] DoReMi: Optimizing Data Mixtures Speeds Up Language Model Pretraining","url":"https://liner.com/review/doremi-optimizing-data-mixtures-speeds-up-language-model-pretraining"},{"title":"DoReMi: optimizing data mixtures speeds up language ...","url":"https://dl.acm.org/doi/10.5555/3666122.3669181"}]

I found comprehensive information about this paper. Here's 
…[truncated 1440 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_review_ref-audit-A_20260526T104656",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 40 · 2026-05-26T10:54:43.604716+00:00_

Web search results for query: "Bao "Fast-DetectGPT Efficient Zero-Shot Detection Machine-Generated Text" ICLR 2024"

Links: [{"title":"GitHub - baoguangsheng/fast-detect-gpt: Code base for ICLR 2024 \"Fast-DetectGPT: Efficient Zero-Shot Detection of Machine-Generated Text via Conditional Probability Curvature\". · GitHub","url":"https://github.com/baoguangsheng/fast-detect-gpt"},{"title":"ICLR Poster Fast-DetectGPT: Efficient Zero-Shot Detection of Machine-Generated Text via Conditional Probability Curvature","url":"https://iclr.cc/virtual/2024/poster/19201"},{"title":"FAST-DETECTGPT: EFFICIENT ZERO-SHOT DETEC","url":"https://openreview.net/pdf?id=Bpcgcr8E8Z"},{"title":"(PDF) FAST-DETECTGPT: EFFICIENT ZERO-SHOT DETEC- TION OF MACHINE-GENERATED TEXT VIA CONDI- TIONAL PROBABILITY CURVATURE","url":"https://www.researchgate.net/publication/388188914_FAST-DETECTGPT_EFFICIENT_ZERO-SHOT_DETEC-_TION_OF_MACHINE-GENERATED_TEXT_VIA_CONDI-_TIONAL_PROBABILITY_CURVATURE"},{"title":"Fast-DetectGPT: Efficient Zero-Shot Detection of Machine-Generated Text via Conditional Probability Curvature | OpenReview","url":"https://openreview.net/forum?id=Bpcgcr8E8Z"},{"title":"[2310.05130] Fast-DetectGPT: Efficient Zero-Shot Detection of Machine-Generated Text via Conditional Probability Curvature","url":"https://arxiv.org/abs/2310.05130"},{"title":"Fast-DetectGPT: Efficient Zero-Shot Detection of Machine-Generated Text via Conditional Probability Curvature","url":"https://proceedings.iclr.cc/paper_files/paper/2024/hash/6b8c6f846c3575e1d1ad496abea28826-Abstract-Conference.html"},{"title":"Fast-DetectGPT: Efficient Zero-Shot Detection of Machine-Generated Text - IEEE Computational Intelligence Society (CIS) Shenzhen Chapter","url":"https://r10.ieee.org/shenzhen-cis/blog/2024/04/25/fast-detectgpt-efficient-zero-shot-detection-of-machine-generated-text/"},{"title":"Releases · baoguangsheng/fast-detect-gpt","url":"https://github.com/baoguangsheng/fast-detect-gpt/releases"}]

I found the paper you
…[truncated 1081 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_review_ref-audit-A_20260526T104656",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool call

_source line 41 · 2026-05-26T10:54:43.604915+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Frank Hall \"A Simple Approach to Ordinal Classification\" ECML 2001"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_review_ref-audit-A_20260526T104656",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Frank Hall \"A Simple Approach to Ordinal Classification\" ECML 2001"
  }
}
```

</details>

---

### Tool call

_source line 42 · 2026-05-26T10:54:43.605049+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Cheng \"Beyond Binary: Towards Fine-Grained LLM-Generated Text Detection via Role Recognition\" WWW 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_review_ref-audit-A_20260526T104656",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Cheng \"Beyond Binary: Towards Fine-Grained LLM-Generated Text Detection via Role Recognition\" WWW 2025"
  }
}
```

</details>

---

### Tool call

_source line 43 · 2026-05-26T10:54:43.605171+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Mehta \"Beyond Surface-Level Similarity Hierarchical Contamination Detection\" arXiv 2511.17602"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_review_ref-audit-A_20260526T104656",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Mehta \"Beyond Surface-Level Similarity Hierarchical Contamination Detection\" arXiv 2511.17602"
  }
}
```

</details>

---

### Tool call

_source line 44 · 2026-05-26T10:54:43.605288+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Sun \"Are We in the AI-Generated Text World Already Quantifying AIGT Social Media\" ACL 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_review_ref-audit-A_20260526T104656",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Sun \"Are We in the AI-Generated Text World Already Quantifying AIGT Social Media\" ACL 2025"
  }
}
```

</details>

---

### Tool call

_source line 45 · 2026-05-26T10:54:43.605403+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Spennemann \"Quantification of AI-Generated Content on the Internet\" arXiv 2504.08755"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_review_ref-audit-A_20260526T104656",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Spennemann \"Quantification of AI-Generated Content on the Internet\" arXiv 2504.08755"
  }
}
```

</details>

---

### Tool call

_source line 46 · 2026-05-26T10:54:43.605516+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Dohmatob \"Strong Model Collapse\" ICLR 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_review_ref-audit-A_20260526T104656",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Dohmatob \"Strong Model Collapse\" ICLR 2025"
  }
}
```

</details>

---

### Tool result

_source line 47 · 2026-05-26T10:54:43.605654+00:00_

Web search results for query: "Frank Hall "A Simple Approach to Ordinal Classification" ECML 2001"

Links: [{"title":"A Simple Approach to Ordinal Classification | Springer Nature Link","url":"https://link.springer.com/chapter/10.1007/3-540-44795-4_13"},{"title":"[PDF] A Simple Approach to Ordinal Classification | Semantic Scholar","url":"https://www.semanticscholar.org/paper/A-Simple-Approach-to-Ordinal-Classification-Frank-Hall/76fc26939d73c565431e1f38107a4245e739284e"},{"title":"A simple approach to ordinal classification.","url":"https://researchcommons.waikato.ac.nz/items/ce0009f5-92fa-4113-b8b2-7ac929cfd32c"},{"title":"(PDF) A Simple Approach to Ordinal Classification (2001) | Eibe Frank | 655 Citations","url":"https://scispace.com/papers/a-simple-approach-to-ordinal-classification-2mjbzk39ox"},{"title":"(PDF) A Simple Approach to Ordinal Classification","url":"https://www.researchgate.net/publication/226877154_A_Simple_Approach_to_Ordinal_Classification"},{"title":"A simple approach to ordinal classification | Proceedings of the 12th European Conference on Machine Learning","url":"https://dl.acm.org/doi/10.1007/3-540-44795-4_13"},{"title":"An Improved Approach to Ordinal Classification | Springer Nature Link","url":"https://link.springer.com/chapter/10.1007/978-3-662-45652-1_4"},{"title":"A Simple Approach to Ordinal Classification - Eibe Frank, Mark Andrew Hall - Google Books","url":"https://books.google.com/books/about/A_Simple_Approach_to_Ordinal_Classificat.html?id=SI2oMQAACAAJ"},{"title":"Classification of Ordinal Data Using Neural Networks | Springer Nature Link","url":"https://link.springer.com/chapter/10.1007/11564096_70"},{"title":"GitHub - liorsidi/ordinal-classifier: python implemantation for Ordinal classifier by Frank, Eibe, and Mark Hall. \"A simple approach to ordinal classification.\" European Conference on Machine Learning. Springer Berlin Heidelberg, 2001.","url":"https://github.com/liorsidi/ordinal-classifier"}]

The search results show inf
…[truncated 838 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_review_ref-audit-A_20260526T104656",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 48 · 2026-05-26T10:54:43.605856+00:00_

Web search results for query: "Cheng "Beyond Binary: Towards Fine-Grained LLM-Generated Text Detection via Role Recognition" WWW 2025"

Links: [{"title":"[2410.14259] Beyond Binary: Towards Fine-Grained LLM-Generated Text Detection via Role Recognition and Involvement Measurement","url":"https://arxiv.org/abs/2410.14259"},{"title":"[2410.14259v1] Beyond Binary: Towards Fine-Grained LLM-Generated Text Detection via Role Recognition and Involvement Measurement","url":"https://arxiv.org/abs/2410.14259v1"},{"title":"Beyond Binary: Towards Fine-Grained LLM-Generated Text Detection via Role Recognition and Involvement Measurement – Own Your AI","url":"https://ownyourai.com/beyond-binary-towards-fine-grained-llm-generated-text-detection-via-role-recognition-and-involvement-measurement/"},{"title":"Beyond Binary: Towards Fine-Grained LLM-Generated Text Detection via Role Recognition and Involvement Measurement | Proceedings of the ACM on Web Conference 2025","url":"https://dl.acm.org/doi/10.1145/3696410.3714770"},{"title":"Beyond Binary: Towards Fine-Grained LLM-Generated Text","url":"https://arxiv.org/pdf/2410.14259"},{"title":"Beyond Binary: Towards Fine-Grained LLM-Generated Text Detection via Role Recognition and Involvement Measurement","url":"https://arxiv.org/html/2410.14259v2"},{"title":"FAID: Fine-Grained AI-Generated Text Detection Using Multi-Task Auxiliary and Multi-Level Contrastive Learning","url":"https://arxiv.org/html/2505.14271"},{"title":"[Quick Review] Robust and Fine-Grained Detection of AI Generated Texts","url":"https://liner.com/review/robust-and-finegrained-detection-ai-generated-texts"}]

Based on the search results, I found the paper you're looking for:

The paper is titled "Beyond Binary: Towards Fine-Grained LLM-Generated Text Detection via Role Recognition and Involvement Measurement" and was authored by Zihao Cheng, Li Zhou, Feng Jiang, Benyou Wang, and Haizhou Li.

The paper was published in the Proceedings of the ACM Web Conference 2025 (WWW
…[truncated 672 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_review_ref-audit-A_20260526T104656",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 49 · 2026-05-26T10:54:43.606035+00:00_

Web search results for query: "Mehta "Beyond Surface-Level Similarity Hierarchical Contamination Detection" arXiv 2511.17602"

Links: [{"title":"[2511.17602] Beyond Surface-Level Similarity: Hierarchical Contamination Detection for Synthetic Training Data in Foundation Models","url":"https://arxiv.org/abs/2511.17602"},{"title":"Beyond Surface-Level Similarity: Hierarchical Contamination Detection for Synthetic Training Data in Foundation Models","url":"https://arxiv.org/html/2511.17602v1"},{"title":"Beyond Surface-Level Similarity: Hierarchical Contamination Detection","url":"https://www.arxiv.org/pdf/2511.17602"},{"title":"(PDF) Beyond Surface-Level Similarity: Hierarchical Contamination Detection for Synthetic Training Data in Foundation Models","url":"https://www.researchgate.net/publication/397933312_Beyond_Surface-Level_Similarity_Hierarchical_Contamination_Detection_for_Synthetic_Training_Data_in_Foundation_Models"},{"title":"Beyond Surface-Level Similarity: Hierarchical Contamination Detection for Synthetic Training Data in Foundation Models | Article Information | J-GLOBAL","url":"https://jglobal.jst.go.jp/en/detail?JGLOBAL_ID=202502216067314793"},{"title":"Machine Learning Oct 2024","url":"https://arxiv.org/list/cs.LG/2024-10?skip=1475&show=2000"},{"title":"Machine Learning Feb 2025","url":"https://arxiv.org/list/cs.LG/2025-02?skip=3050&show=2000"},{"title":"Machine Learning Jan 2024","url":"https://arxiv.org/list/cs.LG/2024-01?skip=325&show=2000"},{"title":"Computer Science","url":"https://arxiv.org/list/cs/pastweek?skip=235&show=1000"},{"title":"Catchup results for stat from Wed, 13 Dec 2023","url":"https://arxiv.org/catchup?smonth=12&sday=13&group=grp_&archive=stat&num=2000&order=reverse&method=without&syear=2023"}]

I found the paper you're looking for! Here are the results:

**Paper Title:** Beyond Surface-Level Similarity: Hierarchical Contamination Detection for Synthetic Training Data in Foundation Models

**Author:** Sushant Mehta

**arXiv ID:** 25
…[truncated 871 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_review_ref-audit-A_20260526T104656",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 50 · 2026-05-26T10:54:43.606207+00:00_

Web search results for query: "Sun "Are We in the AI-Generated Text World Already Quantifying AIGT Social Media" ACL 2025"

Links: [{"title":"Are We in the AI-Generated Text World Already? Quantifying and Monitoring AIGT on Social Media - ACL Anthology","url":"https://aclanthology.org/2025.acl-long.1120/"},{"title":"GitHub - TrustAIRLab/AIGT_on_Social_Media: [ACL2025] Official repository for \"Are We in the AI-Generated Text World Already? Quantifying and Monitoring AIGT on Social Media\"","url":"https://github.com/TrustAIRLab/AIGT_on_Social_Media"},{"title":"[2412.18148] Are We in the AI-Generated Text World Already? Quantifying and Monitoring AIGT on Social Media","url":"https://arxiv.org/abs/2412.18148"},{"title":"Are We in the AI-Generated Text World Already? Quantifying and Monitoring AIGT on Social Media | Request PDF","url":"https://www.researchgate.net/publication/394299909_Are_We_in_the_AI-Generated_Text_World_Already_Quantifying_and_Monitoring_AIGT_on_Social_Media"},{"title":"Are We in the AI-Generated Text World Already? Quantifying and Monitoring AIGT on Social Media","url":"https://arxiv.org/html/2412.18148v1"},{"title":"[Literature Review] Are We in the AI-Generated Text World Already? Quantifying and Monitoring AIGT on Social Media","url":"https://www.themoonlight.io/en/review/are-we-in-the-ai-generated-text-world-already-quantifying-and-monitoring-aigt-on-social-media"},{"title":"Zhen Sun - Homepage","url":"https://zhensun.cn/"}]

I found the research paper you're looking for! Here's the information about it:

## Paper Details

"Are We in the AI-Generated Text World Already? Quantifying and Monitoring AIGT on Social Media" is authored by Zhen Sun, Zongmin Zhang, Xinyue Shen, Ziyi Zhang, Yule Liu, Michael Backes, Yang Zhang, and Xinlei He, and was published in Proceedings of the 63rd Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers) in Vienna, Austria.

## Research Overview

The paper addresses the growing presenc
…[truncated 641 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_review_ref-audit-A_20260526T104656",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 51 · 2026-05-26T10:54:43.606374+00:00_

Web search results for query: "Dohmatob "Strong Model Collapse" ICLR 2025"

Links: [{"title":"Published as a conference paper at ICLR 2025 STRONG MODEL COLLAPSE","url":"https://proceedings.iclr.cc/paper_files/paper/2025/file/284afdc2309f9667d2d4fb9290235b0c-Paper-Conference.pdf"},{"title":"Published as a conference paper at ICLR 2025 STRONG MODEL COLLAPSE","url":"https://par.nsf.gov/servlets/purl/10649434"},{"title":"[2410.04840] Strong Model Collapse","url":"https://arxiv.org/abs/2410.04840"},{"title":"ICLR Poster Strong Model Collapse","url":"https://iclr.cc/virtual/2025/poster/32070"},{"title":"Published as a conference paper at ICLR 2025","url":"https://openreview.net/pdf?id=MQXrTMonT1"},{"title":"Published as a conference paper at ICLR 2025","url":"https://proceedings.iclr.cc/paper_files/paper/2025/file/7416573f05b50beac6d0aef3abc805c0-Paper-Conference.pdf"},{"title":"Escaping Model Collapse via Synthetic Data Verification: Near-term Improvements and Long-term ConvergenceThis project is supported by the AI2050 program at Schmidt Sciences (Grant G-24-66104) and Army Research Office Award W911NF-23-1-0030. We also thank Cong Ma from UChicago, Hongning Wang and Bo Li from Tsinghua, Pinyan Lu and Gavin Tang from Shanghai University of Finance and Economics for helpful discussions and suggestions.","url":"https://arxiv.org/html/2510.16657v1"},{"title":"[Quick Review] Strong Model Collapse","url":"https://liner.com/review/strong-model-collapse"}]

I found the paper! Here are the key details about the research:

## "Strong Model Collapse" by Dohmatob et al. at ICLR 2025

The paper, authored by Elvis Dohmatob, Yunzhen Feng, Arjun Subramonian, and Julia Kempe, establishes a strong form of the model collapse phenomenon, a critical performance degradation due to synthetic data in the training corpus within the scaling laws paradigm that underpins large neural networks like ChatGPT and Llama.

**Key Findings:**

The results show that even the smallest fraction of synthetic
…[truncated 804 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_review_ref-audit-A_20260526T104656",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 52 · 2026-05-26T10:54:43.606540+00:00_

Web search results for query: "Spennemann "Quantification of AI-Generated Content on the Internet" arXiv 2504.08755"

Links: [{"title":"[2504.08755] Delving into: the quantification of Ai-generated content on the internet (synthetic data)","url":"https://arxiv.org/abs/2504.08755"},{"title":"25-12 Delving into Ai generated content on the internet","url":"https://arxiv.org/pdf/2504.08755"},{"title":"(PDF) Delving into: the quantification of Ai-generated content on the internet (synthetic data)","url":"https://www.researchgate.net/publication/390772908_Delving_into_the_quantification_of_Ai-generated_content_on_the_internet_synthetic_data"},{"title":"Delving into: the quantification of Ai-generated content on ...","url":"https://www.semanticscholar.org/paper/Delving-into:-the-quantification-of-Ai-generated-on-Spennemann/f7740011daee667f954a69b73458686c173e2ea1"},{"title":"[2604.16407] How unique are hallucinated citations offered by generative Artificial Intelligence models?","url":"https://arxiv.org/abs/2604.16407"},{"title":"[2504.02898] A Practical Synthesis of Detecting AI-Generated Textual, Visual, and Audio Content","url":"https://arxiv.org/abs/2504.02898"},{"title":"Is Sam Altman a victim of the dead internet - or the person who killed it?","url":"https://www.machine.news/is-openai-boss-sam-altman-a-victim-of-the-dead-internet-or-the-person-who-killed-it/"}]

I found the paper you're looking for! Here's what I discovered:

The paper is titled "Delving into: the quantification of Ai-generated content on the internet (synthetic data)" by Dirk HR Spennemann and was submitted on March 29, 2025.

**Key Findings:**

The paper demonstrates that linguistic markers commonly used by ChatGPT can effectively be used to estimate the presence of generative AI content online. 

The findings suggest that at least 30% of text on active web pages originates from AI-generated sources, with the actual proportion likely approaching 40%.

**Methodology:**

Monthly frequencies of webpa
…[truncated 436 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_review_ref-audit-A_20260526T104656",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool call

_source line 53 · 2026-05-26T10:54:43.606711+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Wang \"SemEval-2024 Task 8 Multidomain Multimodel Multilingual Machine-Generated Text Detection\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_review_ref-audit-A_20260526T104656",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Wang \"SemEval-2024 Task 8 Multidomain Multimodel Multilingual Machine-Generated Text Detection\""
  }
}
```

</details>

---

### Tool call

_source line 54 · 2026-05-26T10:54:43.606859+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Gerstgrasser \"Is Model Collapse Inevitable? Breaking the Curse of Recursion\" COLM 2024"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_review_ref-audit-A_20260526T104656",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Gerstgrasser \"Is Model Collapse Inevitable? Breaking the Curse of Recursion\" COLM 2024"
  }
}
```

</details>

---

### Tool call

_source line 55 · 2026-05-26T10:54:43.606981+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Guo \"The Curious Decline of Linguistic Diversity Training Language Models Synthetic Text\" NAACL 2024"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_review_ref-audit-A_20260526T104656",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Guo \"The Curious Decline of Linguistic Diversity Training Language Models Synthetic Text\" NAACL 2024"
  }
}
```

</details>

---

### Tool call

_source line 56 · 2026-05-26T10:54:43.607098+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Briesch \"Large Language Models Suffer From Their Own Output Self-Consuming Training Loop\" arXiv 2311.16822"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_review_ref-audit-A_20260526T104656",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Briesch \"Large Language Models Suffer From Their Own Output Self-Consuming Training Loop\" arXiv 2311.16822"
  }
}
```

</details>

---

### Tool call

_source line 57 · 2026-05-26T10:54:43.607219+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Padmakumar \"Does Writing with Language Models Reduce Content Diversity\" ICLR 2024"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_review_ref-audit-A_20260526T104656",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Padmakumar \"Does Writing with Language Models Reduce Content Diversity\" ICLR 2024"
  }
}
```

</details>

---

### Tool call

_source line 58 · 2026-05-26T10:54:43.607334+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Krishna \"Paraphrasing Evades Detectors AI-Generated Text Retrieval Effective Defense\" NeurIPS 2023"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_review_ref-audit-A_20260526T104656",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Krishna \"Paraphrasing Evades Detectors AI-Generated Text Retrieval Effective Defense\" NeurIPS 2023"
  }
}
```

</details>

---

### Tool result

_source line 59 · 2026-05-26T10:54:43.607472+00:00_

Web search results for query: "Gerstgrasser "Is Model Collapse Inevitable? Breaking the Curse of Recursion" COLM 2024"

Links: [{"title":"[2404.01413] Is Model Collapse Inevitable? Breaking the Curse of Recursion by Accumulating Real and Synthetic Data","url":"https://arxiv.org/abs/2404.01413"},{"title":"Is Model Collapse Inevitable? Breaking the Curse of Recursion by Accumulating Real and Synthetic Data | Rylan Schaeffer","url":"https://rylanschaeffer.github.io/content/research/2024_arxiv_is_model_collapse_inevitable/main.html"},{"title":"Is Model Collapse Inevitable? Breaking the Curse of Recursion by Accumulating Real and Synthetic Data | Stanford SALT Lab","url":"https://saltlab.stanford.edu/papers/gerstgrasser-is-model-collapse-2024/"},{"title":"Is Model Collapse Inevitable? Breaking the Curse of Recursion by Accumulating Real and Synthetic Data | OpenReview","url":"https://openreview.net/forum?id=5B2K4LRgmz"},{"title":"Is Model Collapse Inevitable? Breaking the Curse of Recursion by Accumulating Real and Synthetic Data | AI Research Paper Details","url":"https://www.aimodels.fyi/papers/arxiv/is-model-collapse-inevitable-breaking-curse-recursion"},{"title":"[PDF] Is Model Collapse Inevitable? Breaking the Curse of Recursion by Accumulating Real and Synthetic Data | Semantic Scholar","url":"https://www.semanticscholar.org/paper/e8815da26d4e6cac8b23b7e6aa75cec028cb66d2"},{"title":"[2404.01413v1] Is Model Collapse Inevitable? Breaking the Curse of Recursion by Accumulating Real and Synthetic Data","url":"https://arxiv.org/abs/2404.01413v1"},{"title":"Is Model Collapse Inevitable? Breaking the Curse of Recursion by Accumulating Real and Synthetic Data","url":"https://arxiv.org/html/2404.01413v2"}]

I found the research paper you're looking for. Here's what the search returned:

The paper "Is Model Collapse Inevitable? Breaking the Curse of Recursion by Accumulating Real and Synthetic Data" was authored by Matthias Gerstgrasser, Rylan Schaeffer, Apratim Dey, Rafael 
…[truncated 1008 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_review_ref-audit-A_20260526T104656",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 60 · 2026-05-26T10:54:43.607646+00:00_

Web search results for query: "Guo "The Curious Decline of Linguistic Diversity Training Language Models Synthetic Text" NAACL 2024"

Links: [{"title":"The Curious Decline of Linguistic Diversity: Training Language Models on Synthetic Text - ACL Anthology","url":"https://aclanthology.org/2024.findings-naacl.228/"},{"title":"(PDF) The Curious Decline of Linguistic Diversity: Training Language Models on Synthetic Text","url":"https://www.researchgate.net/publication/382631840_The_Curious_Decline_of_Linguistic_Diversity_Training_Language_Models_on_Synthetic_Text"},{"title":"[2311.09807] The Curious Decline of Linguistic Diversity: Training Language Models on Synthetic Text","url":"https://arxiv.org/abs/2311.09807"},{"title":"[PDF] The Curious Decline of Linguistic Diversity: Training Language Models on Synthetic Text | Semantic Scholar","url":"https://www.semanticscholar.org/paper/The-Curious-Decline-of-Linguistic-Diversity:-Models-Guo-Shang/7d5ea474aa1cf732bb1d00faa07a5bb2c9119cfd"},{"title":"The Curious Decline of Linguistic Diversity: Training Language Models on Synthetic Text - Archive ouverte HAL","url":"https://hal.science/hal-04593399"},{"title":"The Curious Decline of Linguistic Diversity: Training Language Models on Synthetic Text - ADS","url":"https://ui.adsabs.harvard.edu/abs/2023arXiv231109807G/abstract"},{"title":"The Curious Decline of Linguistic Diversity: Training Language Models on Synthetic Text - Laboratoire d'informatique de l'X (LIX)","url":"https://dumas.ccsd.cnrs.fr/X-LIX/hal-04593399v1"},{"title":"@inproceedings{guo-etal-2024-curious,","url":"https://aclanthology.org/2024.findings-naacl.228.bib"},{"title":"The Curious Decline of Linguistic Diversity: Training Language Models on Synthetic Text | AI Research Paper Details","url":"https://www.aimodels.fyi/papers/arxiv/curious-decline-linguistic-diversity-training-language-models"}]

I've found the paper you're looking for. Here's what I found:

"The Curious Decline of Linguistic Diversity: Training
…[truncated 1288 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_review_ref-audit-A_20260526T104656",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 61 · 2026-05-26T10:54:43.607845+00:00_

Web search results for query: "Briesch "Large Language Models Suffer From Their Own Output Self-Consuming Training Loop" arXiv 2311.16822"

Links: [{"title":"[2311.16822] Large Language Models Suffer From Their Own Output: An Analysis of the Self-Consuming Training Loop","url":"https://arxiv.org/abs/2311.16822"},{"title":"Large Language Models Suffer From Their Own Output: An Analysis of the Self-Consuming Training Loop","url":"https://arxiv.org/html/2311.16822v2"},{"title":"[2311.16822v2] Large Language Models Suffer From Their Own Output: An Analysis of the Self-Consuming Training Loop","url":"https://arxiv.org/abs/2311.16822v2"},{"title":"[2311.16822] Large Language Models Suffer From Their Own Output: An Analysis of the Self-Consuming Training Loop","url":"https://ar5iv.labs.arxiv.org/html/2311.16822"},{"title":"Large Language Models Suffer From Their Own Output: An Analysis of the Self-Consuming Training Loop | AI Research Paper Details","url":"https://www.aimodels.fyi/papers/arxiv/large-language-models-suffer-from-their-own"},{"title":"arXiv:2311.16822v2 [cs.LG] 17 Jun 2024","url":"https://arxiv.org/pdf/2311.16822"},{"title":"Large Language Models Suffer From Their Own Output: An Analysis of the Self-Consuming Training Loop - ADS","url":"https://ui.adsabs.harvard.edu/abs/arXiv:2311.16822"},{"title":"[PDF] Large Language Models Suffer From Their Own Output: An Analysis of the Self-Consuming Training Loop | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Large-Language-Models-Suffer-From-Their-Own-Output:-Briesch-Sobania/c24ed03689adc2a075004c6619f43f7f6230fe4b"},{"title":"Large Language Models Suffer From Their Own Output:","url":"https://arxiv.org/pdf/2311.16822v1"},{"title":"Why Does ChatGPT “Delve” So Much? Exploring the Sources of Lexical Overrepresentation in Large Language Models","url":"https://arxiv.org/html/2412.11385v1"}]

I've found the paper you're looking for. Here's what I found:

**Paper Details:**
- **Title:** "Large Language Mode
…[truncated 1088 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_review_ref-audit-A_20260526T104656",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 62 · 2026-05-26T10:54:43.608024+00:00_

Web search results for query: "Padmakumar "Does Writing with Language Models Reduce Content Diversity" ICLR 2024"

Links: [{"title":"[2309.05196] Does Writing with Language Models Reduce Content Diversity?","url":"https://arxiv.org/abs/2309.05196"},{"title":"DOES WRITING WITH LANGUAGE MODELS REDUCE CONTENT DIVERSITY? - NYU Scholars","url":"https://nyuscholars.nyu.edu/en/publications/does-writing-with-language-models-reduce-content-diversity"},{"title":"Does Writing with Language Models Reduce Content Diversity? | Request PDF","url":"https://www.researchgate.net/publication/373837896_Does_Writing_with_Language_Models_Reduce_Content_Diversity"},{"title":"Does Writing with Language Models Reduce Content Diversity? | AI Research Paper Details","url":"https://www.aimodels.fyi/papers/arxiv/does-writing-language-models-reduce-content-diversity"},{"title":"[PDF] Does Writing with Language Models Reduce Content Diversity? | Semantic Scholar","url":"https://www.semanticscholar.org/paper/f95fb254da1f7b74a14ac8feb3f834d64e67e4cd"},{"title":"Does Writing with Language Models Reduce Content Diversity? | OpenReview","url":"https://openreview.net/forum?id=Feiz5HtCD0"},{"title":"Does Writing with Language Models Reduce Content Diversity? | NSF Public Access Repository","url":"https://par.nsf.gov/biblio/10534705-does-writing-language-models-reduce-content-diversity"},{"title":"Does Writing with Language Models Reduce Content Diversity?","url":"https://arxiv.org/html/2309.05196v3"},{"title":"International Conference on Learning Representations 2024","url":"https://proceedings.iclr.cc/paper_files/paper/2024"}]

I found the research paper you're looking for! The paper "Does Writing with Language Models Reduce Content Diversity?" was written by Padmakumar and He and presented at the 12th International Conference on Learning Representations (ICLR 2024) in Vienna, Austria.

Here's a summary of the paper's key findings:

The study measured the impact of co-writing on diversity through a con
…[truncated 736 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_review_ref-audit-A_20260526T104656",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 63 · 2026-05-26T10:54:43.608206+00:00_

Web search results for query: "Wang "SemEval-2024 Task 8 Multidomain Multimodel Multilingual Machine-Generated Text Detection""

Links: [{"title":"[2404.14183] SemEval-2024 Task 8: Multidomain, Multimodel and Multilingual Machine-Generated Text Detection","url":"https://arxiv.org/abs/2404.14183"},{"title":"SemEval-2024 Task 8: Multidomain, Multimodel and Multilingual Machine-Generated Text Detection - ACL Anthology","url":"https://aclanthology.org/2024.semeval-1.279/"},{"title":"SemEval-2024 Task 8: Multidomain, Multimodel and Multilingual Machine-Generated Text Detection","url":"https://arxiv.org/html/2404.14183v1"},{"title":"SemEval-2024 Task 8: Multidomain, Multimodel and Multilingual Machine-Generated Text Detection - NYU Scholars","url":"https://nyuscholars.nyu.edu/en/publications/semeval-2024-task-8-multidomain-multimodel-and-multilingual-machi"},{"title":"[PDF] SemEval-2024 Task 8: Multidomain, Multimodel and Multilingual Machine-Generated Text Detection | Semantic Scholar","url":"https://www.semanticscholar.org/paper/SemEval-2024-Task-8:-Multidomain,-Multimodel-and-Wang-Mansurov/c56eab12bd00e2fe28868af21d518044d66df00d"}]

The search has returned relevant results about the SemEval-2024 Task 8 paper. Here's what I found:

The paper "SemEval-2024 Task 8: Multidomain, Multimodel and Multilingual Machine-Generated Text Detection" was authored by Yuxia Wang, Jonibek Mansurov, Petar Ivanov, Jinyan Su, Artem Shelmanov, Akim Tsvigun, Osama Mohammed Afzal, Tarek Mahmoud, Giovanni Puccetti, and Thomas Arnold.

The paper was published in the Proceedings of the 18th International Workshop on Semantic Evaluation (SemEval-2024), pages 2057–2079, in Mexico City, Mexico, in 2024.

The task consisted of three subtasks: Subtask A, a binary classification task determining whether a text is written by a human or generated by a machine; Subtask B, to detect the exact source of a text; and Subtask C, which aims to identify the changing point within a text at which authorship tran
…[truncated 383 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_review_ref-audit-A_20260526T104656",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 64 · 2026-05-26T10:54:43.608448+00:00_

Web search results for query: "Krishna "Paraphrasing Evades Detectors AI-Generated Text Retrieval Effective Defense" NeurIPS 2023"

Links: [{"title":"GitHub - martiansideofthemoon/ai-detection-paraphrases: Official repository for our NeurIPS 2023 paper \"Paraphrasing evades detectors of AI-generated text, but retrieval is an effective defense\" (https://arxiv.org/abs/2303.13408). · GitHub","url":"https://github.com/martiansideofthemoon/ai-detection-paraphrases"},{"title":"NeurIPS Poster Paraphrasing evades detectors of AI-generated text, but retrieval is an effective defense","url":"https://neurips.cc/virtual/2023/poster/71402"},{"title":"[PDF] Paraphrasing evades detectors of AI-generated text, but retrieval is an effective defense | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Paraphrasing-evades-detectors-of-AI-generated-text,-Krishna-Song/1c13af186d1e177b85ef1ec3fc7b8d33ec314cfd"},{"title":"Paraphrasing evades detectors of AI-generated text, but ...","url":"https://openreview.net/pdf?id=WbFhFvjjKj"},{"title":"[2303.13408] Paraphrasing evades detectors of AI-generated text, but retrieval is an effective defense","url":"https://arxiv.org/abs/2303.13408"},{"title":"Paraphrasing evades detectors of AI-generated text, but retrieval is an effective defense","url":"https://papers.nips.cc/paper_files/paper/2023/hash/575c450013d0e99e4b0ecf82bd1afaa4-Abstract-Conference.html"},{"title":"Paraphrasing evades detectors of AI-generated text, but retrieval is an effective defense | Request PDF","url":"https://www.researchgate.net/publication/369477232_Paraphrasing_evades_detectors_of_AI-generated_text_but_retrieval_is_an_effective_defense"},{"title":"Paraphrasing evades detectors of AI-generated text, but retrieval is an effective defense - NLP with Friends","url":"https://nlpwithfriends.com/speakers/kalpesh-krishna"}]

Based on the search results, I found comprehensive information about this NeurIPS 2023 paper:

## Paper Overview

The paper is titled "Paraph
…[truncated 1480 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_review_ref-audit-A_20260526T104656",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool call

_source line 65 · 2026-05-26T10:54:43.608640+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Sadasivan \"Can AI-Generated Text be Reliably Detected\" arXiv 2303.11156"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_review_ref-audit-A_20260526T104656",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Sadasivan \"Can AI-Generated Text be Reliably Detected\" arXiv 2303.11156"
  }
}
```

</details>

---

### Tool call

_source line 66 · 2026-05-26T10:54:43.608789+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Hao \"Learning to Rewrite Generalized LLM-Generated Text Detection\" ACL 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_review_ref-audit-A_20260526T104656",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Hao \"Learning to Rewrite Generalized LLM-Generated Text Detection\" ACL 2025"
  }
}
```

</details>

---

### Tool call

_source line 67 · 2026-05-26T10:54:43.608935+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Wang \"Unveiling Attractor Cycles Large Language Models Dynamical Systems Successive Paraphrasing\" ACL 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_review_ref-audit-A_20260526T104656",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Wang \"Unveiling Attractor Cycles Large Language Models Dynamical Systems Successive Paraphrasing\" ACL 2025"
  }
}
```

</details>

---

### Tool call

_source line 68 · 2026-05-26T10:54:43.609057+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Fu \"A Theoretical Perspective How to Prevent Model Collapse Self-consuming Training Loops\" ICLR 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_review_ref-audit-A_20260526T104656",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Fu \"A Theoretical Perspective How to Prevent Model Collapse Self-consuming Training Loops\" ICLR 2025"
  }
}
```

</details>

---

### Tool call

_source line 69 · 2026-05-26T10:54:43.609173+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Verma \"Ghostbuster Detecting Text Ghostwritten by Large Language Models\" NAACL 2024"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_review_ref-audit-A_20260526T104656",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Verma \"Ghostbuster Detecting Text Ghostwritten by Large Language Models\" NAACL 2024"
  }
}
```

</details>

---

### Tool call

_source line 70 · 2026-05-26T10:54:43.609288+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Dugan \"RAID Shared Benchmark Robust Evaluation Machine-Generated Text Detectors\" ACL 2024"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_review_ref-audit-A_20260526T104656",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Dugan \"RAID Shared Benchmark Robust Evaluation Machine-Generated Text Detectors\" ACL 2024"
  }
}
```

</details>

---

### Tool result

_source line 71 · 2026-05-26T10:54:43.609423+00:00_

Web search results for query: "Sadasivan "Can AI-Generated Text be Reliably Detected" arXiv 2303.11156"

Links: [{"title":"[2303.11156] Can AI-Generated Text be Reliably Detected?","url":"https://arxiv.org/abs/2303.11156"},{"title":"[PDF] Can AI-Generated Text be Reliably Detected? | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Can-AI-Generated-Text-be-Reliably-Detected-Sadasivan-Kumar/5ee8bb4fc80a291b2e416a2a879e7153a783d7e9"},{"title":"[2303.11156] Can AI-Generated Text be Reliably Detected?","url":"https://ar5iv.labs.arxiv.org/html/2303.11156"},{"title":"Can AI-Generated Text be Reliably Detected?","url":"https://bibbase.org/network/publication/sadasivan-kumar-balasubramanian-wang-feizi-canaigeneratedtextbereliablydetected-2023"},{"title":"(PDF) Can AI-Generated Text be Reliably Detected?","url":"https://www.researchgate.net/publication/369380286_Can_AI-Generated_Text_be_Reliably_Detected"},{"title":"[2303.11156v3] Can AI-Generated Text be Reliably Detected?","url":"https://arxiv.org/abs/2303.11156v3"},{"title":"[2303.11156v4] Can AI-Generated Text be Reliably Detected?","url":"https://arxiv.org/abs/2303.11156v4"},{"title":"Paper page - Can AI-Generated Text be Reliably Detected?","url":"https://huggingface.co/papers/2303.11156"}]

I found the paper you're looking for. Here are the key details:

**Paper Title:** "Can AI-Generated Text be Reliably Detected?" by Vinu Sankar Sadasivan and 3 other authors

**arXiv ID:** 2303.11156

**Authors:** Vinu Sankar Sadasivan, Aounon Kumar, Sriram Balasubramanian, Wenxiao Wang, and Soheil Feizi

**Main Contribution:** The paper introduces recursive paraphrasing attack to stress test the robustness of AI text detectors in the presence of an attacker, and provides a theoretical framework connecting the AUROC of the best possible detector to the Total Variation distance between human and AI text distributions.

**Key Finding:** Both empirically and theoretically, the paper shows that these detectors are not reli
…[truncated 477 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_review_ref-audit-A_20260526T104656",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 72 · 2026-05-26T10:54:43.609601+00:00_

Web search results for query: "Hao "Learning to Rewrite Generalized LLM-Generated Text Detection" ACL 2025"

Links: [{"title":"Learning to Rewrite: Generalized LLM-Generated Text Detection - ACL Anthology","url":"https://aclanthology.org/2025.acl-long.322/"},{"title":"Learning to Rewrite: Generalized LLM-Generated Text ...","url":"https://www.cs.columbia.edu/~junfeng/papers/learn2rewrite-acl25.pdf"},{"title":"[2408.04237] Learning to Rewrite: Generalized LLM-Generated Text Detection","url":"https://arxiv.org/abs/2408.04237"},{"title":"Accepted Main Conference Papers - ACL 2025","url":"https://2025.aclweb.org/program/main_papers/"},{"title":"Distance Learning for Detecting LLM-Generated Text","url":"https://arxiv.org/pdf/2601.21895"},{"title":"Learn-to-Distance: Distance Learning for Detecting LLM-Generated Text","url":"https://arxiv.org/html/2601.21895"},{"title":"(PDF) Learning to Rewrite: Generalized LLM-Generated Text Detection","url":"https://www.researchgate.net/publication/382971537_Learning_to_Rewrite_Generalized_LLM-Generated_Text_Detection"}]

Based on the search results, I found the paper you're looking for:

## Paper Summary

"Learning to Rewrite: Generalized LLM-Generated Text Detection" by Wei Hao, Ran Li, Weiliang Zhao, Junfeng Yang, and Chengzhi Mao was published in 2025 in the Proceedings of the 63rd Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers), pages 6421–6434, Vienna, Austria.

## Key Contribution

The paper introduces Learning2Rewrite, a novel framework to detect LLM-generated text with exceptional generalization to unseen domains. The method leverages the insight that LLMs inherently modify AI-generated content less than human-written text when tasked with rewriting. By training LLMs to minimize alterations on AI-generated inputs, the framework amplifies this disparity, yielding a more distinguishable and generalizable edit distance across diverse text distributions.

## Results

Extensive experiments on
…[truncated 489 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_review_ref-audit-A_20260526T104656",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 73 · 2026-05-26T10:54:43.609830+00:00_

Web search results for query: "Wang "Unveiling Attractor Cycles Large Language Models Dynamical Systems Successive Paraphrasing" ACL 2025"

Links: [{"title":"Unveiling Attractor Cycles in Large Language Models: A Dynamical Systems View of Successive Paraphrasing - ACL Anthology","url":"https://aclanthology.org/2025.acl-long.624/"},{"title":"[2502.15208] Unveiling Attractor Cycles in Large Language Models: A Dynamical Systems View of Successive Paraphrasing","url":"https://arxiv.org/abs/2502.15208"},{"title":"Unveiling Attractor Cycles in Large Language Models: A Dynamical Systems View of Successive Paraphrasing","url":"https://arxiv.org/html/2502.15208v1"},{"title":"[2502.15208v1] Unveiling Attractor Cycles in Large Language Models: A Dynamical Systems View of Successive Paraphrasing","url":"https://arxiv.org/abs/2502.15208v1"},{"title":"A Dynamical Systems View of Successive Paraphrasing","url":"https://aclanthology.org/2025.acl-long.624.pdf"},{"title":"Unveiling Attractor Cycles in Large Language Models: A Dynamical Systems View of Successive Paraphrasing | Request PDF","url":"https://www.researchgate.net/publication/394299645_Unveiling_Attractor_Cycles_in_Large_Language_Models_A_Dynamical_Systems_View_of_Successive_Paraphrasing"},{"title":"Unveiling Attractor Cycles in Large Language Models: A Dynamical Systems View of Successive Paraphrasing [Quick Review]","url":"https://liner.com/review/unveiling-attractor-cycles-in-large-language-models-dynamical-systems-view"},{"title":"[Literature Review] Unveiling Attractor Cycles in Large Language Models: A Dynamical Systems View of Successive Paraphrasing","url":"https://www.themoonlight.io/en/review/unveiling-attractor-cycles-in-large-language-models-a-dynamical-systems-view-of-successive-paraphrasing"},{"title":"dblp: Unveiling Attractor Cycles in Large Language Models: A Dynamical Systems View of Successive Paraphrasing.","url":"https://dblp.org/rec/journals/corr/abs-2502-15208.html"}]

I found the paper you're lookin
…[truncated 902 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_review_ref-audit-A_20260526T104656",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 74 · 2026-05-26T10:54:43.610011+00:00_

Web search results for query: "Fu "A Theoretical Perspective How to Prevent Model Collapse Self-consuming Training Loops" ICLR 2025"

Links: [{"title":"[2502.18865] A Theoretical Perspective: How to Prevent Model Collapse in Self-consuming Training Loops","url":"https://arxiv.org/abs/2502.18865"},{"title":"A Theoretical Perspective: How to Prevent Model Collapse in Self-consuming Training Loops | OpenReview","url":"https://openreview.net/forum?id=WttfQGwpES"},{"title":"Computer Science Feb 2025","url":"https://arxiv.org/list/cs/2025-02?skip=9525&show=25"},{"title":"Escaping Model Collapse via Synthetic Data Verification: Near-term Improvements and Long-term ConvergenceThis project is supported by the AI2050 program at Schmidt Sciences (Grant G-24-66104) and Army Research Office Award W911NF-23-1-0030. We also thank Cong Ma from UChicago, Hongning Wang and Bo Li from Tsinghua, Pinyan Lu and Gavin Tang from Shanghai University of Finance and Economics for helpful discussions and suggestions.","url":"https://arxiv.org/html/2510.16657v1"},{"title":"A Theoretical Perspective: How to Prevent Model Collapse in Self-consuming Training Loops","url":"https://arxiv.org/html/2502.18865"},{"title":"HOW TO PREVENT MODEL COLLAPSE IN SELF- ...","url":"https://openreview.net/pdf?id=WttfQGwpES"},{"title":"A Closer Look at Model Collapse: From a Generalization-to-Memorization Perspective | Request PDF","url":"https://www.researchgate.net/publication/395724450_A_Closer_Look_at_Model_Collapse_From_a_Generalization-to-Memorization_Perspective"},{"title":"A Closer Look at Model Collapse: From a Generalization-to-Memorization Perspective","url":"https://arxiv.org/html/2509.16499v1"}]

I found the paper you were searching for! Here are the results:

"A Theoretical Perspective: How to Prevent Model Collapse in Self-consuming Training Loops" by Shi Fu, Yingjie Wang, Yuzhu Chen, Xinmei Tian, and Dacheng Tao has been accepted at ICLR 2025.

**Key Details:**

- **arXiv:** The paper is available 
…[truncated 795 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_review_ref-audit-A_20260526T104656",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 75 · 2026-05-26T10:54:43.610194+00:00_

Web search results for query: "Verma "Ghostbuster Detecting Text Ghostwritten by Large Language Models" NAACL 2024"

Links: [{"title":"Ghostbuster: Detecting Text Ghostwritten by Large Language Models - ACL Anthology","url":"https://aclanthology.org/2024.naacl-long.95/"},{"title":"[2305.15047] Ghostbuster: Detecting Text Ghostwritten by Large Language Models","url":"https://arxiv.org/abs/2305.15047"},{"title":"GitHub - vivek3141/ghostbuster: Ghostbuster: Detecting Text Ghostwritten by Large Language Models (NAACL 2024) · GitHub","url":"https://github.com/vivek3141/ghostbuster"},{"title":"Detecting Text Ghostwritten by Large Language Models","url":"https://aclanthology.org/2024.naacl-long.95.pdf"},{"title":"Ghostbuster: Detecting Text Ghostwritten by Large Language Models","url":"https://arxiv.org/html/2305.15047v3"},{"title":"Ghostbuster: Detecting Text Ghostwritten by Large Language Models Vivek Verma","url":"https://nlp.cs.berkeley.edu/pubs/Verma-Fleisig-Tomlin-Klein_2024_Ghostbuster_paper.pdf"},{"title":"Ghostbuster: Detecting Text Ghostwritten by Large Language Models | Request PDF","url":"https://www.researchgate.net/publication/382631441_Ghostbuster_Detecting_Text_Ghostwritten_by_Large_Language_Models"},{"title":"Ghostbuster: Detecting Text Ghostwritten by Large Language Models | AI Research Paper Details","url":"https://www.aimodels.fyi/papers/arxiv/ghostbuster-detecting-text-ghostwritten-by-large-language"},{"title":"[2305.15047v1] Ghostbuster: Detecting Text Ghostwritten by Large Language Models","url":"https://arxiv.org/abs/2305.15047v1"},{"title":"Accepted Papers - NAACL-HLT 2024","url":"https://2024.naacl.org/program/accepted_papers/"}]

I found the paper you're looking for! Here's what I found:

"Ghostbuster: Detecting Text Ghostwritten by Large Language Models" by Verma et al. was published in the Proceedings of the 2024 Conference of the North American Chapter of the Association for Computational Linguistics (NAACL 2024), which took place in Mexico Ci
…[truncated 982 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_review_ref-audit-A_20260526T104656",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 76 · 2026-05-26T10:54:43.610377+00:00_

Web search results for query: "Dugan "RAID Shared Benchmark Robust Evaluation Machine-Generated Text Detectors" ACL 2024"

Links: [{"title":"RAID: A Shared Benchmark for Robust Evaluation of Machine-Generated Text Detectors - Liam Dugan","url":"https://liamdugan.com/talks/2024-08-10-raid-benchmark"},{"title":"RAID: A Shared Benchmark for Robust Evaluation of Machine-Generated Text Detectors - ACL Anthology","url":"https://aclanthology.org/2024.acl-long.674/"},{"title":"[Quick Review] RAID: A Shared Benchmark for Robust Evaluation of Machine-Generated Text Detectors","url":"https://liner.com/review/raid-shared-benchmark-for-robust-evaluation-machinegenerated-text-detectors"},{"title":"Paper page - RAID: A Shared Benchmark for Robust Evaluation of Machine-Generated Text Detectors","url":"https://huggingface.co/papers/2405.07940"},{"title":"RAID: A Shared Benchmark for Robust Evaluation of Machine-Generated Text Detectors","url":"https://arxiv.org/html/2405.07940v1"},{"title":"[2405.07940] RAID: A Shared Benchmark for Robust Evaluation of Machine-Generated Text Detectors","url":"https://arxiv.org/abs/2405.07940"},{"title":"RAID: A Shared Benchmark for Robust Evaluation of Machine-Generated Text Detectors (Conference Paper) | NSF PAGES","url":"https://par.nsf.gov/biblio/10563509-raid-shared-benchmark-robust-evaluation-machine-generated-text-detectors"},{"title":"RAID: A Shared Benchmark for Robust Evaluation of Machine-Generated Text Detectors | Request PDF","url":"https://www.researchgate.net/publication/384214327_RAID_A_Shared_Benchmark_for_Robust_Evaluation_of_Machine-Generated_Text_Detectors"},{"title":"[PDF] RAID: A Shared Benchmark for Robust Evaluation of Machine-Generated Text Detectors | Semantic Scholar","url":"https://www.semanticscholar.org/paper/RAID:-A-Shared-Benchmark-for-Robust-Evaluation-of-Dugan-Hwang/a28474db72957c239127374cfee3c8ed8190defc"}]

Based on the search results, here's what I found about the paper:

The paper "RAID: A Shared Benchmark for R
…[truncated 1419 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_review_ref-audit-A_20260526T104656",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool call

_source line 77 · 2026-05-26T10:54:43.610557+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Liang \"GPT detectors are biased against non-native English writers\" Patterns 2023"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_review_ref-audit-A_20260526T104656",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Liang \"GPT detectors are biased against non-native English writers\" Patterns 2023"
  }
}
```

</details>

---

### Tool call

_source line 78 · 2026-05-26T10:54:43.610685+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Kazdan \"Collapse or Thrive\" accepted ICML 2025 conference paper OpenReview"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_review_ref-audit-A_20260526T104656",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Kazdan \"Collapse or Thrive\" accepted ICML 2025 conference paper OpenReview"
  }
}
```

</details>

---

### Tool call

_source line 79 · 2026-05-26T10:54:43.610822+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Gerstgrasser \"Is Model Collapse Inevitable\" accepted COLM 2024 conference paper"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_review_ref-audit-A_20260526T104656",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Gerstgrasser \"Is Model Collapse Inevitable\" accepted COLM 2024 conference paper"
  }
}
```

</details>

---

### Tool call

_source line 80 · 2026-05-26T10:54:43.610944+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Schaeffer \"Position Model Collapse Does Not Mean\" accepted ICML 2025 conference"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_review_ref-audit-A_20260526T104656",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Schaeffer \"Position Model Collapse Does Not Mean\" accepted ICML 2025 conference"
  }
}
```

</details>

---

### Tool result

_source line 81 · 2026-05-26T10:54:43.611095+00:00_

Web search results for query: "Gerstgrasser "Is Model Collapse Inevitable" accepted COLM 2024 conference paper"

Links: [{"title":"Is Model Collapse Inevitable? Breaking the Curse of Recursion by Accumulating Real and Synthetic Data | Stanford SALT Lab","url":"https://saltlab.stanford.edu/papers/gerstgrasser-is-model-collapse-2024/"},{"title":"[2404.01413] Is Model Collapse Inevitable? Breaking the Curse of Recursion by Accumulating Real and Synthetic Data","url":"https://arxiv.org/abs/2404.01413"},{"title":"[PDF] Is Model Collapse Inevitable? Breaking the Curse of Recursion by Accumulating Real and Synthetic Data | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Is-Model-Collapse-Inevitable-Breaking-the-Curse-of-Gerstgrasser-Schaeffer/e8815da26d4e6cac8b23b7e6aa75cec028cb66d2"},{"title":"Is Model Collapse Inevitable? Breaking the Curse of Recursion by Accumulating Real and Synthetic Data | Rylan Schaeffer","url":"https://rylanschaeffer.github.io/content/research/2024_arxiv_is_model_collapse_inevitable/main.html"},{"title":"Escaping Model Collapse via Synthetic Data Verification: Near-term Improvements and Long-term ConvergenceThis project is supported by the AI2050 program at Schmidt Sciences (Grant G-24-66104) and Army Research Office Award W911NF-23-1-0030. We also thank Cong Ma from UChicago, Hongning Wang and Bo Li from Tsinghua, Pinyan Lu and Gavin Tang from Shanghai University of Finance and Economics for helpful discussions and suggestions.","url":"https://arxiv.org/html/2510.16657v1"},{"title":"Is Model Collapse Inevitable? Breaking the Curse of Recursion by Accumulating Real and Synthetic Data | OpenReview","url":"https://openreview.net/forum?id=5B2K4LRgmz"},{"title":"Experts divided over training AI with more data from AI • The Register","url":"https://www.theregister.com/2024/05/09/ai_model_collapse/"},{"title":"Addressing Concerns of Model Collapse from Synthetic Data in AI","url":"https://www.gretel.ai/blog/addressing-concerns-of-model-co
…[truncated 966 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_review_ref-audit-A_20260526T104656",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 82 · 2026-05-26T10:54:43.611263+00:00_

Web search results for query: "Kazdan "Collapse or Thrive" accepted ICML 2025 conference paper OpenReview"

Links: [{"title":"ICML Poster Collapse or Thrive: Perils and Promises of Synthetic Data in a Self-Generating World","url":"https://icml.cc/virtual/2025/poster/44713"},{"title":"1 Introduction","url":"https://arxiv.org/html/2410.16713"},{"title":"Collapse or Thrive? Perils and Promises of Synthetic Data in a Self-Generating World | OpenReview","url":"https://openreview.net/forum?id=Xr5iINA3zU"},{"title":"A Probabilistic Perspective on Model Collapse","url":"https://arxiv.org/pdf/2505.13947"},{"title":"Context Collapse: In-Context Learning and Model Collapse","url":"https://arxiv.org/pdf/2601.00923"},{"title":"When Models Don't Collapse: On the Consistency of Iterative MLE","url":"https://arxiv.org/pdf/2505.19046"},{"title":"Universality of the $\\pi^2/6$ Pathway in Avoiding Model Collapse","url":"https://arxiv.org/pdf/2410.22812"}]

Based on the search results, I found information about this paper:

The paper "Collapse or Thrive: Perils and Promises of Synthetic Data in a Self-Generating World" by Joshua Kazdan, Rylan Schaeffer, Apratim Dey, Matthias Gerstgrasser, Rafael Rafailov, David Donoho, and Sanmi Koyejo was accepted to ICML 2025 and presented as a poster.

The paper addresses the question of what happens when generative machine learning models are pretrained on web-scale datasets containing data generated by earlier models. Some prior work warns of "model collapse" as the web is overwhelmed by synthetic data; other work suggests the problem can be contained (i.e. collapse can be avoided) by managing how available data are used in pretraining.

The paper is available on OpenReview and ICML's virtual conference website, with links to both the poster presentation and the OpenReview forum discussion.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_review_ref-audit-A_20260526T104656",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 83 · 2026-05-26T10:54:43.611433+00:00_

Web search results for query: "Liang "GPT detectors are biased against non-native English writers" Patterns 2023"

Links: [{"title":"[2304.02819] GPT detectors are biased against non-native English writers","url":"https://arxiv.org/abs/2304.02819"},{"title":"Liang, W. X. et al. (2023). GPT Detectors Are Biased against Non-Native English Writers. Patterns, 4, Article ID 100779. - References - Scientific Research Publishing","url":"https://www.scirp.org/reference/referencespapers?referenceid=3900453"},{"title":"GPT detectors are biased against non-native English writers","url":"https://arxiv.org/pdf/2304.02819"},{"title":"(PDF) GPT detectors are biased against non-native English writers","url":"https://www.researchgate.net/publication/372269006_GPT_detectors_are_biased_against_non-native_English_writers"},{"title":"GPT detectors can be biased against non-native English writers | ScienceDaily","url":"https://www.sciencedaily.com/releases/2023/07/230710113921.htm"},{"title":"GPT detectors are biased against non-native English writers - ScienceDirect","url":"https://www.sciencedirect.com/science/article/pii/S2666389923001307"},{"title":"GitHub - Weixin-Liang/ChatGPT-Detector-Bias · GitHub","url":"https://github.com/Weixin-Liang/ChatGPT-Detector-Bias"},{"title":"GPT detectors are biased against non-native English writers: Patterns","url":"https://www.cell.com/patterns/fulltext/S2666-3899(23)00130-7"},{"title":"GPT DETECTORS ARE BIASED AGAINST NON-NATIVE ...","url":"https://openreview.net/pdf?id=SPuX8tKKIQ"}]

I found the research you're looking for. Here's what the web search reveals:

The paper "GPT Detectors Are Biased against Non-Native English Writers" was authored by Liang et al. and published in Patterns in 2023, Volume 4, Article ID 100779.

The key findings of the research include:

More than half of the non-native-authored TOEFL (Test of English as a Foreign Language) essays are incorrectly classified as "AI-generated," while detectors exhibit near-perfect accura
…[truncated 832 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_review_ref-audit-A_20260526T104656",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 84 · 2026-05-26T10:54:43.611604+00:00_

Web search results for query: "Schaeffer "Position Model Collapse Does Not Mean" accepted ICML 2025 conference"

Links: [{"title":"1 Introduction","url":"https://arxiv.org/html/2503.03150v2"},{"title":"[2503.03150] Position: Model Collapse Does Not Mean What You Think","url":"https://arxiv.org/abs/2503.03150"},{"title":"Position: Model Collapse Does Not Mean What You Think","url":"https://arxiv.org/pdf/2503.03150"},{"title":"ICML Poster Collapse or Thrive: Perils and Promises of Synthetic Data in a Self-Generating World","url":"https://icml.cc/virtual/2025/poster/44713"},{"title":"42nd ICML 2025: Vancouver, BC, Canada","url":"https://dblp.org/db/conf/icml/icml2025.html"},{"title":"Position: Model Collapse Does Not Mean What You Think - ADS","url":"https://ui.adsabs.harvard.edu/abs/2025arXiv250303150S/abstract"},{"title":"ICML.2025 | Cool Papers - Immersive Paper Discovery","url":"https://papers.cool/venue/ICML.2025"},{"title":"Stanford AI Lab Papers and Talks at ICML 2025 | SAIL Blog","url":"http://ai.stanford.edu/blog/icml-2025/"}]

Based on the search results, I found information about the paper you're asking about:

The paper "Position: Model Collapse Does Not Mean What You Think" was authored by Rylan Schaeffer, Joshua Kazdan, Alvan Caleb Arulandu, and Sanmi Koyejo from Stanford Computer Science, Stanford Statistics, and Harvard University.

In this position piece, the authors contend that the widespread narrative about model collapse fundamentally misunderstands the scientific evidence. They highlight that research on model collapse actually encompasses eight distinct and at times conflicting definitions of model collapse, and argue that inconsistent terminology within and between papers has hindered building a comprehensive understanding of model collapse.

The paper was posted on arXiv in March 2025. While I found evidence that Rylan Schaeffer is presenting work at ICML 2025, I could not find explicit confirmation in these search results that this specific "P
…[truncated 209 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_review_ref-audit-A_20260526T104656",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 85 · 2026-05-26T10:54:43.611802+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Schaeffer \"Position: Model Collapse Does Not Mean What You Think\" ICML 2025 poster proceedings"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_review_ref-audit-A_20260526T104656",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Schaeffer \"Position: Model Collapse Does Not Mean What You Think\" ICML 2025 poster proceedings"
  }
}
```

</details>

---

### Tool call

_source line 86 · 2026-05-26T10:54:43.611938+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Sadasivan \"Can AI-Generated Text be Reliably Detected\" published conference venue 2024 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_review_ref-audit-A_20260526T104656",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Sadasivan \"Can AI-Generated Text be Reliably Detected\" published conference venue 2024 2025"
  }
}
```

</details>

---

### Tool call

_source line 87 · 2026-05-26T10:54:43.612059+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Briesch \"Large Language Models Suffer From Their Own Output\" published conference 2024"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_review_ref-audit-A_20260526T104656",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Briesch \"Large Language Models Suffer From Their Own Output\" published conference 2024"
  }
}
```

</details>

---

### Tool call

_source line 88 · 2026-05-26T10:54:43.612175+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Spennemann \"Delving into the quantification of AI-generated content\" exact title arxiv 2504.08755"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_review_ref-audit-A_20260526T104656",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Spennemann \"Delving into the quantification of AI-generated content\" exact title arxiv 2504.08755"
  }
}
```

</details>

---

### Tool result

_source line 89 · 2026-05-26T10:54:43.612313+00:00_

Web search results for query: "Sadasivan "Can AI-Generated Text be Reliably Detected" published conference venue 2024 2025"

Links: [{"title":"[2303.11156] Can AI-Generated Text be Reliably Detected?","url":"https://arxiv.org/abs/2303.11156"},{"title":"Can AI-Generated Text be Reliably Detected?","url":"https://bibbase.org/network/publication/sadasivan-kumar-balasubramanian-wang-feizi-canaigeneratedtextbereliablydetected-2024"},{"title":"Can AI-Generated Text be Reliably Detected? | OpenReview","url":"https://openreview.net/forum?id=NvSwR4IvLO"},{"title":"(PDF) Can AI-Generated Text be Reliably Detected?","url":"https://www.researchgate.net/publication/369380286_Can_AI-Generated_Text_be_Reliably_Detected"},{"title":"[PDF] Can AI-Generated Text be Reliably Detected? | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Can-AI-Generated-Text-be-Reliably-Detected-Sadasivan-Kumar/5ee8bb4fc80a291b2e416a2a879e7153a783d7e9"},{"title":"[2303.11156v3] Can AI-Generated Text be Reliably Detected?","url":"https://arxiv.org/abs/2303.11156v3"},{"title":"[2303.11156v1] Can AI-Generated Text be Reliably Detected?","url":"https://arxiv.org/abs/2303.11156v1"},{"title":"Can AI-Generated Text be Reliably Detected? Stress Testing AI Text Detectors Under Various Attacks | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Can-AI-Generated-Text-be-Reliably-Detected-Stress-Sadasivan-Kumar/42f7d83e6c20fd4aaf3e3f53b18ab7db221ee300"}]

Based on the web search results, here's what I found about this paper:

The paper "Can AI-Generated Text be Reliably Detected?" by Vinu Sankar Sadasivan, Aounon Kumar, Sriram Balasubramanian, Wenxiao Wang, and Soheil Feizi was originally submitted on March 17, 2023, with revisions through February 2024.

Regarding the published conference venue, the paper appears to have been submitted to ICLR 2024 (International Conference on Learning Representations 2024) based on references in the OpenReview submission guidelines.

Additionally, the pa
…[truncated 463 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_review_ref-audit-A_20260526T104656",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 90 · 2026-05-26T10:54:43.612490+00:00_

Web search results for query: "Schaeffer "Position: Model Collapse Does Not Mean What You Think" ICML 2025 poster proceedings"

Links: [{"title":"1 Introduction","url":"https://arxiv.org/html/2503.03150v2"},{"title":"[2503.03150] Position: Model Collapse Does Not Mean What You Think","url":"https://arxiv.org/abs/2503.03150"},{"title":"Position: Model Collapse Does Not Mean What You Think","url":"https://arxiv.org/pdf/2503.03150"},{"title":"ICML Poster Collapse or Thrive: Perils and Promises of Synthetic Data in a Self-Generating World","url":"https://icml.cc/virtual/2025/poster/44713"},{"title":"Position: Model Collapse Does Not Mean What You Think - ADS","url":"https://ui.adsabs.harvard.edu/abs/2025arXiv250303150S/abstract"},{"title":"Position: the Stochastic Parrot in the Coal Mine Model Collapse is a Threat to Low-Resource Communities","url":"https://arxiv.org/html/2605.04127"},{"title":"Position: Model Collapse Does Not Mean What You Think | OpenReview","url":"https://openreview.net/forum?id=ygfzWIGDN8"},{"title":"42nd ICML 2025: Vancouver, BC, Canada","url":"https://dblp.org/db/conf/icml/icml2025.html"}]

I found the paper! Here's what I found about this work:

"Position: Model Collapse Does Not Mean What You Think" is authored by Rylan Schaeffer, Joshua Kazdan, Alvan Caleb Arulandu, and Sanmi Koyejo from Stanford Computer Science, Stanford Statistics, and Harvard University.

The paper addresses concerns about model collapse—a degradation in generative models' performance when trained on synthetic data from earlier models—and contends that the widespread narrative fundamentally misunderstands the scientific evidence. It highlights that research on model collapse encompasses eight distinct and sometimes conflicting definitions, and argues that inconsistent terminology has hindered understanding of the phenomenon.

Through hand-annotating 28 prior research publications, the authors identify 8 definitions of model collapse that can be grouped into three families:
…[truncated 434 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_review_ref-audit-A_20260526T104656",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 91 · 2026-05-26T10:54:43.612665+00:00_

Web search results for query: "Briesch "Large Language Models Suffer From Their Own Output" published conference 2024"

Links: [{"title":"[2311.16822] Large Language Models Suffer From Their Own Output: An Analysis of the Self-Consuming Training Loop","url":"https://arxiv.org/abs/2311.16822"},{"title":"[PDF] Large Language Models Suffer From Their Own Output: An Analysis of the Self-Consuming Training Loop | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Large-Language-Models-Suffer-From-Their-Own-Output:-Briesch-Sobania/c24ed03689adc2a075004c6619f43f7f6230fe4b"},{"title":"Large Language Models Suffer From Their Own Output: An Analysis of the Self-Consuming Training Loop","url":"https://arxiv.org/html/2311.16822v2"},{"title":"Large Language Models Suffer From Their Own Output: An Analysis of the Self-Consuming Training Loop | AI Research Paper Details","url":"https://www.aimodels.fyi/papers/arxiv/large-language-models-suffer-from-their-own"},{"title":"[2311.16822v2] Large Language Models Suffer From Their Own Output: An Analysis of the Self-Consuming Training Loop","url":"https://arxiv.org/abs/2311.16822v2"},{"title":"Theoretical Proof that Auto-regressive Language Models ...","url":"https://arxiv.org/pdf/2412.14872"},{"title":"[2311.16822] Large Language Models Suffer From Their Own Output: An Analysis of the Self-Consuming Training Loop","url":"https://ar5iv.labs.arxiv.org/html/2311.16822"},{"title":"Large Language Models Suffer From Their Own Output: An Analysis of the Self-Consuming Training Loop | OpenReview","url":"https://openreview.net/forum?id=SaOxhcDCM3"},{"title":"[Submitted on 28 Nov 2023 (v1), last revised 17 Jun 2024 (this version, v2)]","url":"https://arxiv.org/pdf/2311.16822"}]

Based on the search results, I found the paper you're looking for:

**Title:** "Large Language Models Suffer From Their Own Output: An Analysis of the Self-Consuming Training Loop" by Martin Briesch and 2 other authors

**Authors:** Martin Briesch, Dominik Sob
…[truncated 703 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_review_ref-audit-A_20260526T104656",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 92 · 2026-05-26T10:54:43.612849+00:00_

Web search results for query: "Spennemann "Delving into the quantification of AI-generated content" exact title arxiv 2504.08755"

Links: [{"title":"[2504.08755] Delving into: the quantification of Ai-generated content on the internet (synthetic data)","url":"https://arxiv.org/abs/2504.08755"},{"title":"25-12 Delving into Ai generated content on the internet","url":"https://arxiv.org/pdf/2504.08755"},{"title":"(PDF) Delving into: the quantification of Ai-generated content on the internet (synthetic data)","url":"https://www.researchgate.net/publication/390772908_Delving_into_the_quantification_of_Ai-generated_content_on_the_internet_synthetic_data"},{"title":"Delving into: the quantification of Ai-generated content on ...","url":"https://www.semanticscholar.org/paper/Delving-into:-the-quantification-of-Ai-generated-on-Spennemann/f7740011daee667f954a69b73458686c173e2ea1"},{"title":"\"Delving into\" the quantification of Ai-generated content on the ...","url":"https://researchoutput.csu.edu.au/en/publications/delving-into-the-quantification-of-ai-generated-content-on-the-in/fingerprints/"},{"title":"[2511.05535] Future of AI Models: A Computational perspective on Model collapse","url":"https://arxiv.org/abs/2511.05535"},{"title":"[2604.16407] How unique are hallucinated citations offered by generative Artificial Intelligence models?","url":"https://arxiv.org/abs/2604.16407"},{"title":"1 Quantitative Analysis of AI-Generated Texts in Academic Research: A Study","url":"https://arxiv.org/pdf/2403.13812"},{"title":"[2504.02898] A Practical Synthesis of Detecting AI-Generated Textual, Visual, and Audio Content","url":"https://arxiv.org/abs/2504.02898"}]

I found the paper you're looking for! Here are the key details:

**Paper Title:** Delving into: the quantification of Ai-generated content on the internet (synthetic data)

**Author:** Dirk HR Spennemann

**ArXiv ID:** 2504.08755

**Main Findings:** By analyzing the frequency of specific keywords commonly used by ChatGPT, 
…[truncated 720 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_review_ref-audit-A_20260526T104656",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 93 · 2026-05-26T10:54:43.613066+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_review_ref-audit-A_20260526T104656",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/introduction.tex"
  }
}
```

</details>

---

### Tool result

_source line 94 · 2026-05-26T10:54:43.613227+00:00_

1	\section{Introduction}
2	\label{sec:introduction}
3	
4	Web-scale text corpora are increasingly contaminated by synthetic content that has itself been generated from earlier synthetic content.
5	Estimates suggest that a substantial fraction of online text is machine-generated~\cite{sun2025aigt, spennemann2025quantifying}, and this share continues to rise.
6	When models train on the outputs of earlier models, the resulting multi-generational synthetic text degrades with each iteration: tail modes vanish, lexical diversity contracts, and surprisal distributions flatten~\cite{shumailov2024collapse, dohmatob2024model}.
7	This degradation arises in both \emph{retrain-chains} (iteratively training on model outputs) and \emph{prompt-chains} (recursively generating from previous outputs without retraining); we study the latter, which isolates generation-level information loss from training dynamics (Appendix~\ref{sec:extended_limitations}).
8	Yet the dominant paradigm treats all machine-generated text identically, discarding the generational depth dimension.
9	
10	This gap cuts across four lines of work: binary detectors~\cite{basani2026diveye, zhang2024minkpp} produce no depth estimate (Section~\ref{sec:binary_confidence}); membership inference~\cite{zawalski2026codec} addresses a different question; the model collapse literature~\cite{shumailov2024collapse, alemohammad2024selfconsuming, schaeffer2025position} provides no per-text tool; and data selection methods~\cite{xie2023dsir, tirumala2023d4, drayson2025} ignore recursive depth.
11	No existing method estimates how many rounds of recursive generation a text has undergone.
12	
13	The Data Processing Inequality (DPI) guarantees that information degrades monotonically across generations, motivating a finite discrimination boundary $\Kstar$.
14	We empirically measure a lower bound $\Kempirical$ on the discrimination boundary (the maximum depth at which a classifier reliably distinguishes adjacent generations) using 15 sta
…[truncated 1665 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_review_ref-audit-A_20260526T104656",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 95 · 2026-05-26T10:54:43.613374+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_review_ref-audit-A_20260526T104656",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/related_work.tex"
  }
}
```

</details>

---

### Tool result

_source line 96 · 2026-05-26T10:54:43.613562+00:00_

1	\section{Related Work}
2	\label{sec:related_work}
3	
4	\paragraph{Model collapse and recursive degradation.}
5	Iterative training on model outputs causes tail-distribution degradation~\cite{shumailov2024collapse, alemohammad2024selfconsuming, dohmatob2024model, dohmatob2025strong}, diversity contraction~\cite{guo2024curious, padmakumar2024writing, briesch2023selfconsuming}, and predictable convergence dynamics~\cite{schaeffer2025position, kazdan2025collapse, gerstgrasser2024model, wang2025unveiling}.
6	Fu et al.~\cite{fu2025theoretical} formalize the convergence via Markov chain theory, complementing the DPI's mutual information monotonicity.
7	Our prompt-chain operates in the replace regime~\cite{kazdan2025collapse}, making $\Kempirical = 2$ a conservative lower bound; empirically, detection accuracy erodes with each generation~\cite{hao2025rewrite}, consistent with our measured discrimination boundary.
8	This literature characterizes macro dynamics but provides no per-text depth estimation, the gap we address.
9	
10	\paragraph{Machine-generated text detection.}
11	Statistical detectors~\cite{mitchell2023detectgpt, bao2024fast} and model-based classifiers~\cite{hans2024binoculars, basani2026diveye, zhang2024minkpp, verma2024ghostbuster} achieve strong human-vs.-machine separation; benchmarks such as RAID~\cite{dugan2024raid} and GPTZero~\cite{liang2023gpt} evaluate robustness at scale.
12	Recent extensions move beyond binary labels: Cheng et al.~\cite{cheng2025beyond} estimate human-AI collaboration degree, Mehta et al.~\cite{mehta2025beyond} propose contamination hierarchies, and Wang et al.~\cite{wang2024semeval} construct multigenerator benchmarks.
13	Robustness concerns arise under paraphrasing~\cite{sadasivan2023detect, krishna2023paraphrasing} and cross-mode transfer~\cite{hao2025rewrite}; CoDeC~\cite{zawalski2026codec} addresses contamination via membership inference.
14	None of these methods estimates recursive generation depth.
15	
16	\paragraph{Data cur
…[truncated 781 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_review_ref-audit-A_20260526T104656",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 97 · 2026-05-26T10:54:43.613762+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/experiments_c1.tex",
  "limit": "200"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_review_ref-audit-A_20260526T104656",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/experiments_c1.tex",
    "limit": "200"
  }
}
```

</details>

---

### Tool result

_source line 98 · 2026-05-26T10:54:43.614068+00:00_

1	\section{Experiments}
2	\label{sec:experiments}
3	
4	We evaluate on ten configurations spanning six families: Pythia-1.4B/6.9B, OLMo-1B, Qwen2.5-1.5B-Instruct (rewrite/continuation), Qwen2.5-1.5B (base), Qwen2.5-7B, LLaMA-3.1-8B, Mistral-7B, and Gemma-2-2B.
5	Unless noted, all experiments use the OBD-LightGBM classifier with 15 features (Section~\ref{sec:method}), 5{,}000 C4 texts per depth level (depths 0--5).
6	
7	%% ====================================================================
8	\subsection{The Discrimination Boundary}
9	\label{sec:kstar_boundary}
10	
11	\begin{figure}[t]
12	\centering
13	\includegraphics[width=\columnwidth]{figures/fig2_auc_decay.pdf}
14	\caption{Pairwise $\auc$ decay across adjacent depth pairs (0v1, 1v2, \ldots, 4v5) for model-mode configurations (solid) and decoding strategies (dashed); shaded bands show bootstrap 95\% CIs. Horizontal dashed line: $\theta = 0.60$.}
15	\label{fig:auc_decay}
16	\end{figure}
17	
18	\begin{table*}[t]
19	\centering
20	\small
21	\caption{Pairwise $\auc$ for adjacent depth pairs with bootstrap 95\% CIs and permutation $p$-values for boundary rows.
22	$\Kempirical = 2$ requires 1v2 $\auc > \theta{=}0.60$ and 2v3 $\auc < \theta$; CIs quantify boundary uncertainty.
23	Extended results (all models) in Table~\ref{tab:kstar_ci_extended}.}
24	\label{tab:kstar_ci}
25	\resizebox{\textwidth}{!}{%
26	\begin{tabular}{lcccccccccc}
27	\toprule
28	 & \multicolumn{2}{c}{Qwen-rw} & \multicolumn{2}{c}{Pythia} & \multicolumn{2}{c}{OLMo} & \multicolumn{2}{c}{Qwen-cont} & \multicolumn{2}{c}{Qwen-7B\rlap{$^\ddagger$}} \\
29	\cmidrule(lr){2-3}\cmidrule(lr){4-5}\cmidrule(lr){6-7}\cmidrule(lr){8-9}\cmidrule(lr){10-11}
30	 & $\auc$ & 95\% CI & $\auc$ & 95\% CI & $\auc$ & 95\% CI & $\auc$ & 95\% CI & $\auc$ & 95\% CI \\
31	\midrule
32	0v1 & .9956 & & .9722 & & .9861 & & .9971 & & .9644 & [.961,\,.967] \\
33	1v2 & .6955 & [.686,\,.704]\rlap{$^*$} & .6074 & [.598,\,.617]\rlap{$^*$} & .5001 & [.496,\,.519] & .6112 & [.602,\,.621]\rlap{$
…[truncated 15516 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_review_ref-audit-A_20260526T104656",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 99 · 2026-05-26T10:54:43.614238+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/experiments_c3.tex",
  "limit": "20"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_review_ref-audit-A_20260526T104656",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/experiments_c3.tex",
    "limit": "20"
  }
}
```

</details>

---

### Tool result

_source line 100 · 2026-05-26T10:54:43.614390+00:00_

1	\section{Consistency Check: $\Kstar$-Guided Filtering}
2	\label{sec:filtering}
3	
4	$\Kempirical = 2$ predicts that binary curation should suffice; we validate this under extreme contamination (${\sim}$83\% synthetic), not as an independent contribution (at realistic rates $\leq$50\%, differences $<$0.3\,pp; Appendix~\ref{sec:dose_response}).
5	We compare six strategies on 30{,}000 documents (depths 0--5): (i)~\textbf{no-filter}, (ii)~\textbf{binary-ours} (15D LightGBM), (iii)~\textbf{binary-Drayson}~\citep{drayson2025}, (iv)~\textbf{graduated} ($w = \exp(-\alpha \hat{d})$, $\alpha \in \{0.1,\ldots,0.9\}$), (v)~\textbf{surprisal}, and (vi)~\textbf{DSIR}~\citep{xie2023dsir}, fine-tuning Qwen2.5-1.5B-Instruct via LoRA (rank~8) for 3 epochs across 5 seeds~\cite{shumailov2024collapse, dohmatob2024model}.
6	
7	\begin{table}[t]
8	\centering
9	\small
10	\caption{Downstream task performance (MMLU, HellaSwag) under six data-filtering strategies. Binary-ours uses the 15D LightGBM depth classifier; Graduated applies exponentially decaying weights $w = \exp(-\alpha \hat{d})$. Mean $\pm$ std over 5 seeds. Full $\alpha$ sweep in Figure~\ref{fig:filtering_strategies}.}
11	\label{tab:tab_filtering_main}
12	\resizebox{\columnwidth}{!}{\input{tables/tab_filtering_main}}
13	\end{table}
14	
15	Binary-ours reduces the MMLU gap from $-$1.53\,pp (no-filter) to $-$0.77\,pp (${\sim}$50\% reduction; $p_{\text{corr}} < 0.05$ vs.\ all alternatives; Table~\ref{tab:tab_filtering_main}, \ref{tab:pairwise_significance}).
16	The ordering is interpretable through $\Kempirical$: binary filtering exploits the strongest boundary (0v1), while graduated strategies assign weights based on near-random classifier outputs for depths $\geq 2$, injecting noise rather than useful signal.
17	Graduated filtering converges toward binary: at $\alpha{=}0.9$, it matches binary-ours on HellaSwag ($p_{\text{corr}} = 1.00$) but remains worse on MMLU ($p_{\text{corr}} = 0.011$); DSIR is indistinguishable from no-filter
…[truncated 290 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_review_ref-audit-A_20260526T104656",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 101 · 2026-05-26T10:54:43.614536+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/discussion.tex",
  "limit": "30"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_review_ref-audit-A_20260526T104656",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/discussion.tex",
    "limit": "30"
  }
}
```

</details>

---

### Tool result

_source line 102 · 2026-05-26T10:54:43.614682+00:00_

1	\section{Discussion}
2	\label{sec:discussion}
3	\label{sec:why_kstar}
4	\label{sec:one_wash}
5	\label{sec:negative_graduated}
6	\label{sec:repr_dependence}
7	\label{sec:boundary_cases}
8	\label{sec:length_confound}
9	
10	\paragraph{One-wash laundering (web text).}
11	For general web text, $\Kempirical{=}2$ reflects concentrated information loss: 0v1 is near-trivially separable ($\auc \geq 0.92$), 1v2 drops by ${\sim}$30\,pp, and 2v3 falls below $\theta$.
12	OBD achieves 94\% depth-0 recall but only 15--23\% for depths $\geq$2; frontier LLMs show 8--38\% ($p > 0.05$ vs.\ OBD; Table~\ref{tab:s3_llm_zeroshot}; per-depth breakdown in Table~\ref{tab:s3c_perdepth}), which supports a data-intrinsic interpretation.
13	Unlike model collapse~\cite{shumailov2024collapse}, one-wash laundering describes erasure of statistical fingerprints; quality may degrade further after features become indistinguishable.
14	
15	\begin{figure}[t]
16	\centering
17	\includegraphics[width=\columnwidth]{figures/fig_filtering_strategies.pdf}
18	\caption{MMLU accuracy under six filtering strategies (5 seeds, $\pm$1 std). Binary $\Kstar$ filtering (red) minimizes degradation; graduated weighting converges toward binary as $\alpha$ increases. Dashed line: no-filter baseline.}
19	\label{fig:filtering_strategies}
20	\end{figure}
21	
22	\paragraph{Boundary cases and representation dependence.}
23	Under Bonferroni correction (Table~\ref{tab:bonferroni_ci}), three of six $\Kempirical{=}2$ cases become marginal (CI lower 0.593--0.599), though $\Kempirical \leq 2$ holds across $\theta \in [0.59, 0.61]$ (Figure~\ref{fig:kstar_theta}).
24	$\Kempirical$ is representation-dependent: neural probes yield $\Kempirical^{\text{neural}} \in \{1,2,3\}$ (Table~\ref{tab:neural_probe_crossmodel}); a DeBERTa probe extends to $\Kempirical{=}4$ on arXiv (Table~\ref{tab:deberta_vs_obd}).
25	
26	\paragraph{Domain dependence and scope.}
27	arXiv yields $\Kempirical{=}3$ across four families (Figure~\ref{fig:jsd_decay}), drive
…[truncated 268 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_review_ref-audit-A_20260526T104656",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 103 · 2026-05-26T10:54:43.614849+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/appendix_extended.tex",
  "limit": "80"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_review_ref-audit-A_20260526T104656",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/appendix_extended.tex",
    "limit": "80"
  }
}
```

</details>

---

### Tool result

_source line 104 · 2026-05-26T10:54:43.615029+00:00_

1	\section{Extended Discussion}
2	\label{sec:extended_discussion}
3	
4	\subsection{Theoretical Implications of $\Kempirical = 2$}
5	
6	The DPI guarantees a finite $\Ktheory$; for general web text, $\Kempirical \leq 2$ across all 10 configurations (1B--8B, 6 families), while structured domains (arXiv) yield $\Kempirical{=}3$, aligning with model collapse convergence~\cite{shumailov2024collapse, dohmatob2024model, alemohammad2024selfconsuming}.
7	Decoding strategy modestly affects signal strength (1v2 $\auc \in [0.6862, 0.7037]$) but does not shift the boundary.
8	
9	\subsection{Cross-Model Transfer Implications}
10	
11	Cross-model classification retains 80--92\% accuracy with scorer-invariant feature rankings ($\rho > 0.90$), which enables single-classifier deployment across generators.
12	Absolute discriminability at the $\Kempirical$ boundary is scorer-sensitive: alternative scorers reduce Qwen-continuation $\Kempirical$ from 2 to 1, while rewrite-mode $\Kempirical = 2$ is preserved.
13	Model family similarity modulates transfer (Pythia$\leftrightarrow$OLMo: 89--92\% vs.\ Qwen-cont$\leftrightarrow$OLMo: 80--85\%).
14	
15	\begin{table}[h]
16	\centering
17	\caption{Cross-scorer validation. Alternative scorers (Pythia-1.4B, OLMo-1B) preserve feature ranking ($\rho > 0.90$) and rewrite-mode $\Kempirical = 2$, but reduce continuation-mode $\Kempirical$ from 2 to 1. OLMo arXiv cross-scorer confirms $\Kempirical{=}1$ ($p{=}0.510$, n.s.).}
18	\label{tab:crossscorer}
19	\resizebox{\columnwidth}{!}{\input{tables/tab_crossscorer}}
20	\end{table}
21	
22	\begin{table}[h]
23	\centering
24	\small
25	\caption{Three-way ANOVA (Generator $\times$ Scorer $\times$ Depth-Pair) on per-fold pairwise $\auc$ values. DV = per-fold AUC; $N{=}300$ (12 cells $\times$ 5 folds $\times$ 5 depth-pairs). Scorer is statistically significant but explains modest variance ($\eta^2_p{=}.192$) relative to Depth-Pair ($\eta^2_p{=}.998$), which supports near-scorer-independence of depth discrimination.}
26
…[truncated 4560 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_review_ref-audit-A_20260526T104656",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 105 · 2026-05-26T10:54:43.615263+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "site:openreview.net \"Position: Model Collapse Does Not Mean What You Think\" ICML 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_review_ref-audit-A_20260526T104656",
  "tool": "WebSearch",
  "tool_args": {
    "query": "site:openreview.net \"Position: Model Collapse Does Not Mean What You Think\" ICML 2025"
  }
}
```

</details>

---

### Tool call

_source line 106 · 2026-05-26T10:54:43.615401+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Sadasivan \"Can AI-Generated Text be Reliably Detected\" TMLR published 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_review_ref-audit-A_20260526T104656",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Sadasivan \"Can AI-Generated Text be Reliably Detected\" TMLR published 2025"
  }
}
```

</details>

---

### Tool result

_source line 107 · 2026-05-26T10:54:43.615544+00:00_

Web search results for query: "Sadasivan "Can AI-Generated Text be Reliably Detected" TMLR published 2025"

Links: [{"title":"[2303.11156] Can AI-Generated Text be Reliably Detected?","url":"https://arxiv.org/abs/2303.11156"},{"title":"Can AI-Generated Text be Reliably Detected? Stress Testing AI Text Detectors Under Various Attacks | OpenReview","url":"https://openreview.net/forum?id=OOgsAZdFOt"},{"title":"(PDF) Can AI-Generated Text be Reliably Detected?","url":"https://www.researchgate.net/publication/369380286_Can_AI-Generated_Text_be_Reliably_Detected"},{"title":"[PDF] Can AI-Generated Text be Reliably Detected? | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Can-AI-Generated-Text-be-Reliably-Detected-Sadasivan-Kumar/5ee8bb4fc80a291b2e416a2a879e7153a783d7e9"},{"title":"Can AI-Generated Text be Reliably Detected? | OpenReview","url":"https://openreview.net/forum?id=NvSwR4IvLO"},{"title":"Accepted papers at TMLR on X: \"Can AI-Generated Text be Reliably Detected? Stress Testing AI Text Detectors Under Various Attacks Vinu Sankar Sadasivan, Aounon Kumar, Sriram Balasubramanian, Wenxiao Wang, Soheil Feizi. Action editor: Kamalika Chaudhuri. https://t.co/6h6ByH1n0v #watermark\" / X","url":"https://x.com/TmlrPub/status/1900336120296034775"},{"title":"[2303.11156v4] Can AI-Generated Text be Reliably Detected?","url":"https://arxiv.org/abs/2303.11156v4"}]

Based on the search results, I found the paper you're looking for:

"Can AI-Generated Text be Reliably Detected? Stress Testing AI Text Detectors Under Various Attacks" by Vinu Sankar Sadasivan, Aounon Kumar, Sriram Balasubramanian, Wenxiao Wang, and Soheil Feizi, with action editor Kamalika Chaudhuri, was accepted to TMLR in March 2025.

The paper introduces a recursive paraphrasing attack to stress test the robustness of AI text detectors in the presence of an attacker, and provides a theoretical framework connecting the AUROC of the best possible detector to the Total Variation distance between hu
…[truncated 215 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_review_ref-audit-A_20260526T104656",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 108 · 2026-05-26T10:54:43.615704+00:00_

Web search results for query: "site:openreview.net "Position: Model Collapse Does Not Mean What You Think" ICML 2025"

Links: [{"title":"Position: Model Collapse Does Not Mean What You Think Anonymous Author(s)","url":"https://openreview.net/pdf?id=ygfzWIGDN8"},{"title":"Position: Model Collapse Does Not Mean What You Think | OpenReview","url":"https://openreview.net/forum?id=ygfzWIGDN8"},{"title":"Surplexity for Mitigating Model Collapse in Generative AI","url":"https://openreview.net/pdf?id=zzk6DUQggQ"},{"title":"Position: Model Collapse Does Not Mean What You Think","url":"https://arxiv.org/pdf/2503.03150"},{"title":"When Models Don't Collapse: On the Consistency of Iterative MLE","url":"https://arxiv.org/pdf/2505.19046"}]

I found the paper! Based on the search results, here's what I found:

The paper "Position: Model Collapse Does Not Mean What You Think" addresses concerns over model collapse, a degradation in future generative models' performance when trained on synthetic data generated by earlier models.

The research highlights that model collapse encompasses eight distinct and at times conflicting definitions, and argues that inconsistent terminology within and between papers has hindered building a comprehensive understanding of model collapse.

The paper specifically identifies eight distinct and at times conflicting definitions of model collapse. These 8 definitions can be loosely grouped into three families: (1) the behavior of the test loss on real data over model-fitting iterations, (2) the deformation of the real data distribution over model-fitting iterations, and (3) the scaling behavior of the test loss with respect to typical scaling quantities.

However, I should note that the search results show this paper was submitted to **NeurIPS 2025**, not ICML 2025 as mentioned in your query. The paper can be found at https://openreview.net/forum?id=ygfzWIGDN8.


REMINDER: You MUST include the sources above in your response to the user using markdown hyp
…[truncated 8 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_review_ref-audit-A_20260526T104656",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 109 · 2026-05-26T10:54:43.615939+00:00_

called Write

<details open><summary>🔧 Tool call — Write</summary>

````json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/artifacts/ref_audit_worker_A.md",
  "content": "# Reference Audit Report — Worker A\n\nAudited: 2026-05-26\nFile: `docs/paper/references.bib` (37 entries)\n\n---\n\n## Per-Entry Verification\n\n```\n[kirchenbauer2023watermark] ✓\n[drayson2025]               ✓\n[schaeffer2025position]     ✓ (arXiv preprint; under review at NeurIPS 2025 per OpenReview, not yet accepted — listing as arXiv is currently correct)\n[kazdan2025collapse]        ✓ (ICML 2025 poster confirmed)\n[mitchell2023detectgpt]     ✓\n[basani2026diveye]          ✓ (TMLR 2026 confirmed)\n[zawalski2026codec]         ✓ (ICLR 2026 confirmed)\n[zhang2024minkpp]           ✓ (ICLR 2025 Spotlight; year=2025 in bib is correct)\n[shumailov2024collapse]     ✓ (Nature 631, pp. 755–759, 2024)\n[alemohammad2024selfconsuming] ✓ (ICLR 2024)\n[dohmatob2024model]         ✓ (ICML 2024)\n[xie2023dsir]               ✓ (NeurIPS 2023)\n[tirumala2023d4]            ✓ (NeurIPS 2023)\n[xie2023doremi]             ✓ (NeurIPS 2023)\n[hans2024binoculars]        ✗ | Title truncated: missing subtitle\n[alain2017understanding]    ✓ (ICLR 2017 Workshop)\n[belinkov2022probing]       ✓ (Computational Linguistics 48(1), 207–219, 2022)\n[bao2024fast]               ✓ (ICLR 2024)\n[frank2001ordinal]          ✓ (ECML 2001, pp. 145–156)\n[cheng2025beyond]           ✓ (WWW 2025)\n[mehta2025beyond]           ✓ (arXiv 2511.17602)\n[sun2025aigt]               ✓ (ACL 2025)\n[spennemann2025quantifying] ✓ (arXiv 2504.08755)\n[dohmatob2025strong]        ✓ (ICLR 2025)\n[wang2024semeval]           ✓ (SemEval 2024)\n[gerstgrasser2024model]     ✓ (COLM 2024)\n[guo2024curious]            ✓ (Findings of NAACL 2024)\n[briesch2023selfconsuming]  ✓ (arXiv preprint)\n[padmakumar2024writing]     ✓ (ICLR 2024)\n[krishna2023paraphrasing]   ✓ (NeurIPS 2023)\n[sadasivan2023detect]       ✗ | Venue outdated: published in TMLR (March 2025), bib still lists as arXiv preprint 2023\n[hao2025rewrite]            ✓ (ACL 2025)\n[wang2025unveiling]         ✓ (ACL 2025, pp. 12740–12755)\n[fu2025theoretical]         ✓ (ICLR 2025)\n[verma2024ghostbuster]      ✓ (NAACL 2024, pp. 1702–1717)\n[dugan2024raid]             ✓ (ACL 2024, pp. 12463–12492)\n[liang2023gpt]              ✗ | Citation context error (see below)\n```\n\n---\n\n## Error Details\n\n### 1. [hans2024binoculars] ✗ — Title truncated\n\n**What's wrong:** Bib title is `Spotting {LLMs} With Binoculars`. The official PMLR proceedings title is **\"Spotting LLMs With Binoculars: Zero-Shot Detection of Machine-Generated Text\"**.\n\n**Fix:**\n```bibtex\ntitle={Spotting {LLMs} With Binoculars: Zero-Shot Detection of Machine-Generated Text},\n```\n\n### 2. [sadasivan2023detect] ✗ — Venue outdated\n\n**What's wrong:** Bib lists as `@article` / `journal={arXiv preprint arXiv:2303.11156}` / `year={2023}`. The paper was accepted at **TMLR** (Transactions on Machine Learning Research) in **March 2025** (confirmed via @TmlrPub announcement, OpenReview forum id OOgsAZdFOt). The published version has a slightly extended title.\n\n**Fix:**\n```bibtex\n@article{sadasivan2023detect,\n  title={Can {AI}-Generated Text be Reliably Detected?},\n  author={Sadasivan, Vinu Sankar and Kumar, Aounon and Balasubramanian, Sriram and Wang, Wenxiao and Feizi, Soheil},\n  journal={Transactions on Machine Learning Research},\n  year={2025},\n  url={https://openreview.net/forum?id=OOgsAZdFOt}\n}\n```\n\n### 3. [liang2023gpt] ✗ — Citation context error (wrong cite)\n\n**What's wrong:** In `related_work.tex:11`:\n```latex\nbenchmarks such as RAID~\\cite{dugan2024raid} and GPTZero~\\cite{liang2023gpt} evaluate robustness at scale.\n```\n`liang2023gpt` is **\"GPT detectors are biased against non-native English writers\"** (Liang et al., Patterns 2023) — a study about bias in GPT detectors. It is **not** the GPTZero tool/benchmark. GPTZero is a commercial product by Edward Tian. The sentence implies `liang2023gpt` IS the GPTZero reference, which is a misattribution.\n\n**Fix options:**\n- (a) Remove the GPTZero mention or cite it properly (GPTZero has no peer-reviewed reference paper).\n- (b) Rephrase to correctly use liang2023gpt: e.g., \"...and bias analyses~\\cite{liang2023gpt} probe detector fairness.\"\n\n---\n\n## Minor Issues (not counted as errors)\n\n- **[guo2024curious]** Author `Chloe` missing accent → should be `Chlo{\\'e}` (Chloé Clavel)\n- **[dohmatob2024model]** Author `Francois` missing cedilla → should be `Fran\\c{c}ois` (François Charton)\n\n---\n\n## Summary\n\n| Metric | Count |\n|--------|-------|\n| Total entries | 37 |\n| ✓ Correct | 34 |\n| ✗ Errors | 3 |\n\n**Errors:** `hans2024binoculars` (truncated title), `sadasivan2023detect` (venue outdated: arXiv → TMLR 2025), `liang2023gpt` (citation context: misattributed as GPTZero)\n"
}
````

</details>

<details><summary>Recorded metadata</summary>

````json
{
  "recorded_role": "tool",
  "session": "worker_review_ref-audit-A_20260526T104656",
  "tool": "Write",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/artifacts/ref_audit_worker_A.md",
    "content": "# Reference Audit Report — Worker A\n\nAudited: 2026-05-26\nFile: `docs/paper/references.bib` (37 entries)\n\n---\n\n## Per-Entry Verification\n\n```\n[kirchenbauer2023watermark] ✓\n[drayson2025]               ✓\n[schaeffer2025position]     ✓ (arXiv preprint; under review at NeurIPS 2025 per OpenReview, not yet accepted — listing as arXiv is currently correct)\n[kazdan2025collapse]        ✓ (ICML 2025 poster confirmed)\n[mitchell2023detectgpt]     ✓\n[basani2026diveye]          ✓ (TMLR 2026 confirmed)\n[zawalski2026codec]         ✓ (ICLR 2026 confirmed)\n[zhang2024minkpp]           ✓ (ICLR 2025 Spotlight; year=2025 in bib is correct)\n[shumailov2024collapse]     ✓ (Nature 631, pp. 755–759, 2024)\n[alemohammad2024selfconsuming] ✓ (ICLR 2024)\n[dohmatob2024model]         ✓ (ICML 2024)\n[xie2023dsir]               ✓ (NeurIPS 2023)\n[tirumala2023d4]            ✓ (NeurIPS 2023)\n[xie2023doremi]             ✓ (NeurIPS 2023)\n[hans2024binoculars]        ✗ | Title truncated: missing subtitle\n[alain2017understanding]    ✓ (ICLR 2017 Workshop)\n[belinkov2022probing]       ✓ (Computational Linguistics 48(1), 207–219, 2022)\n[bao2024fast]               ✓ (ICLR 2024)\n[frank2001ordinal]          ✓ (ECML 2001, pp. 145–156)\n[cheng2025beyond]           ✓ (WWW 2025)\n[mehta2025beyond]           ✓ (arXiv 2511.17602)\n[sun2025aigt]               ✓ (ACL 2025)\n[spennemann2025quantifying] ✓ (arXiv 2504.08755)\n[dohmatob2025strong]        ✓ (ICLR 2025)\n[wang2024semeval]           ✓ (SemEval 2024)\n[gerstgrasser2024model]     ✓ (COLM 2024)\n[guo2024curious]            ✓ (Findings of NAACL 2024)\n[briesch2023selfconsuming]  ✓ (arXiv preprint)\n[padmakumar2024writing]     ✓ (ICLR 2024)\n[krishna2023paraphrasing]   ✓ (NeurIPS 2023)\n[sadasivan2023detect]       ✗ | Venue outdated: published in TMLR (March 2025), bib still lists as arXiv preprint 2023\n[hao2025rewrite]            ✓ (ACL 2025)\n[wang2025unveiling]         ✓ (ACL 2025, pp. 12740–12755)\n[fu2025theoretical]         ✓ (ICLR 2025)\n[verma2024ghostbuster]      ✓ (NAACL 2024, pp. 1702–1717)\n[dugan2024raid]             ✓ (ACL 2024, pp. 12463–12492)\n[liang2023gpt]              ✗ | Citation context error (see below)\n```\n\n---\n\n## Error Details\n\n### 1. [hans2024binoculars] ✗ — Title truncated\n\n**What's wrong:** Bib title is `Spotting {LLMs} With Binoculars`. The official PMLR proceedings title is **\"Spotting LLMs With Binoculars: Zero-Shot Detection of Machine-Generated Text\"**.\n\n**Fix:**\n```bibtex\ntitle={Spotting {LLMs} With Binoculars: Zero-Shot Detection of Machine-Generated Text},\n```\n\n### 2. [sadasivan2023detect] ✗ — Venue outdated\n\n**What's wrong:** Bib lists as `@article` / `journal={arXiv preprint arXiv:2303.11156}` / `year={2023}`. The paper was accepted at **TMLR** (Transactions on Machine Learning Research) in **March 2025** (confirmed via @TmlrPub announcement, OpenReview forum id OOgsAZdFOt). The published version has a slightly extended title.\n\n**Fix:**\n```bibtex\n@article{sadasivan2023detect,\n  title={Can {AI}-Generated Text be Reliably Detected?},\n  author={Sadasivan, Vinu Sankar and Kumar, Aounon and Balasubramanian, Sriram and Wang, Wenxiao and Feizi, Soheil},\n  journal={Transactions on Machine Learning Research},\n  year={2025},\n  url={https://openreview.net/forum?id=OOgsAZdFOt}\n}\n```\n\n### 3. [liang2023gpt] ✗ — Citation context error (wrong cite)\n\n**What's wrong:** In `related_work.tex:11`:\n```latex\nbenchmarks such as RAID~\\cite{dugan2024raid} and GPTZero~\\cite{liang2023gpt} evaluate robustness at scale.\n```\n`liang2023gpt` is **\"GPT detectors are biased against non-native English writers\"** (Liang et al., Patterns 2023) — a study about bias in GPT detectors. It is **not** the GPTZero tool/benchmark. GPTZero is a commercial product by Edward Tian. The sentence implies `liang2023gpt` IS the GPTZero reference, which is a misattribution.\n\n**Fix options:**\n- (a) Remove the GPTZero mention or cite it properly (GPTZero has no peer-reviewed reference paper).\n- (b) Rephrase to correctly use liang2023gpt: e.g., \"...and bias analyses~\\cite{liang2023gpt} probe detector fairness.\"\n\n---\n\n## Minor Issues (not counted as errors)\n\n- **[guo2024curious]** Author `Chloe` missing accent → should be `Chlo{\\'e}` (Chloé Clavel)\n- **[dohmatob2024model]** Author `Francois` missing cedilla → should be `Fran\\c{c}ois` (François Charton)\n\n---\n\n## Summary\n\n| Metric | Count |\n|--------|-------|\n| Total entries | 37 |\n| ✓ Correct | 34 |\n| ✗ Errors | 3 |\n\n**Errors:** `hans2024binoculars` (truncated title), `sadasivan2023detect` (venue outdated: arXiv → TMLR 2025), `liang2023gpt` (citation context: misattributed as GPTZero)\n"
  }
}
````

</details>

---

### Tool result

_source line 110 · 2026-05-26T10:54:43.616142+00:00_

File created successfully at: /home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/artifacts/ref_audit_worker_A.md

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_review_ref-audit-A_20260526T104656",
  "tool": "Write",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 111 · 2026-05-26T10:54:43.616309+00:00_

37 条引用逐条核查完成，结果写入 `artifacts/ref_audit_worker_A.md`。

**3 条有问题：**
- `hans2024binoculars` — 标题截断，缺副标题 ": Zero-Shot Detection of Machine-Generated Text"
- `sadasivan2023detect` — 已发表在 TMLR 2025，bib 仍标为 arXiv preprint 2023
- `liang2023gpt` — `related_work.tex:11` 将其作为 GPTZero 引用，但该论文是关于 GPT 检测器对非母语写作者偏见的研究，不是 GPTZero

其余 34 条均验证通过。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_review_ref-audit-A_20260526T104656"
}
```

</details>

---
