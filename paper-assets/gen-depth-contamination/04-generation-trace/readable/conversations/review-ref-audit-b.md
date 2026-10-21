# review ref audit B

**Generational Depth Estimation of Recursive Synthetic Text: Measuring the Discrimination Boundary** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 109
- **Recorded user turns:** 0
- **Tool calls:** 54
- **Original source:** `logs/chats/worker_review_ref-audit-B_20260526T104706.jsonl`
- **Structured JSON:** [`195601ba9f20a52b8a94.json`](../../sessions/19/195601ba9f20a52b8a94.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

109 recorded events

### Tool call

_source line 1 · 2026-05-26T10:53:59.334902+00:00_

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
  "session": "worker_review_ref-audit-B_20260526T104706",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/references.bib"
  }
}
```

</details>

---

### Tool result

_source line 2 · 2026-05-26T10:53:59.335320+00:00_

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
  "session": "worker_review_ref-audit-B_20260526T104706",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-26T10:53:59.335550+00:00_

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
  "session": "worker_review_ref-audit-B_20260526T104706",
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

_source line 4 · 2026-05-26T10:53:59.335695+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_review_ref-audit-B_20260526T104706",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-26T10:53:59.335870+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Kirchenbauer Geiping \"A Watermark for Large Language Models\" ICML 2023"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_review_ref-audit-B_20260526T104706",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Kirchenbauer Geiping \"A Watermark for Large Language Models\" ICML 2023"
  }
}
```

</details>

---

### Tool call

_source line 6 · 2026-05-26T10:53:59.336002+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Drayson Yilmaz Lampos \"Machine-Generated Text Detection Prevents Language Model Collapse\" 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_review_ref-audit-B_20260526T104706",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Drayson Yilmaz Lampos \"Machine-Generated Text Detection Prevents Language Model Collapse\" 2025"
  }
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-26T10:53:59.336122+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Schaeffer Kazdan \"Position: Model Collapse Does Not Mean What You Think\" 2025 arXiv"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_review_ref-audit-B_20260526T104706",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Schaeffer Kazdan \"Position: Model Collapse Does Not Mean What You Think\" 2025 arXiv"
  }
}
```

</details>

---

### Tool call

_source line 8 · 2026-05-26T10:53:59.336239+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Kazdan Schaeffer \"Collapse or Thrive? Perils and Promises of Synthetic Data\" ICML 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_review_ref-audit-B_20260526T104706",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Kazdan Schaeffer \"Collapse or Thrive? Perils and Promises of Synthetic Data\" ICML 2025"
  }
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-26T10:53:59.336364+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Mitchell Lee Khazatsky \"DetectGPT Zero-Shot Machine-Generated Text Detection\" ICML 2023"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_review_ref-audit-B_20260526T104706",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Mitchell Lee Khazatsky \"DetectGPT Zero-Shot Machine-Generated Text Detection\" ICML 2023"
  }
}
```

</details>

---

### Tool call

_source line 10 · 2026-05-26T10:53:59.336481+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Basani Chen \"Diversity Boosts AI-Generated Text Detection\" DivEye TMLR 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_review_ref-audit-B_20260526T104706",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Basani Chen \"Diversity Boosts AI-Generated Text Detection\" DivEye TMLR 2026"
  }
}
```

</details>

---

### Tool result

_source line 11 · 2026-05-26T10:53:59.336636+00:00_

Web search results for query: "Drayson Yilmaz Lampos "Machine-Generated Text Detection Prevents Language Model Collapse" 2025"

Links: [{"title":"[2502.15654] Machine-generated text detection prevents language model collapse","url":"https://arxiv.org/abs/2502.15654"},{"title":"Machine-generated text detection prevents language ...","url":"https://omega.cs.ucl.ac.uk/assets/pdf/papers/drayson2025-model-collapse.pdf"},{"title":"(PDF) Machine-generated text detection prevents language model collapse","url":"https://www.researchgate.net/publication/397412242_Machine-generated_text_detection_prevents_language_model_collapse"},{"title":"Machine-generated text detection prevents language model collapse","url":"https://arxiv.org/html/2502.15654v1"},{"title":"Machine-generated text detection prevents language model collapse - UCL Discovery","url":"https://discovery.ucl.ac.uk/id/eprint/10217226/"},{"title":"Machine-generated text detection prevents language model ...","url":"https://discovery.ucl.ac.uk/id/eprint/10217226/1/2025.emnlp-main.1506.pdf"},{"title":"GitHub - GeorgeDrayson/model_collapse","url":"https://github.com/GeorgeDrayson/model_collapse"},{"title":"Learning by Surprise: Surplexity for Mitigating Model Collapse in Generative AI","url":"https://arxiv.org/html/2410.12341v3"},{"title":"Vasileios LAMPOS | Associate Professor | B.Sc., M.Sc., Ph.D. | University College London, London | UCL | Department of Computer Science | Research profile","url":"https://www.researchgate.net/profile/Vasileios-Lampos"}]

I've found the paper! Here are the search results:

"Machine-generated text detection prevents language model collapse" is a paper by George Drayson, Emine Yilmaz, and Vasileios Lampos, submitted on February 21, 2025.

**Key Information:**
- The paper addresses how as LLMs become more prevalent, their generated outputs are proliferating across the web, risking dilution of human-authored text
- Since online data is the primary resource for LLM pre-training, subsequent 
…[truncated 847 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_review_ref-audit-B_20260526T104706",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-26T10:53:59.336829+00:00_

Web search results for query: "Kirchenbauer Geiping "A Watermark for Large Language Models" ICML 2023"

Links: [{"title":"[2301.10226] A Watermark for Large Language Models","url":"https://arxiv.org/abs/2301.10226"},{"title":"A Watermark for Large Language Models","url":"https://proceedings.mlr.press/v202/kirchenbauer23a/kirchenbauer23a.pdf"},{"title":"[PDF] A Watermark for Large Language Models | Semantic Scholar","url":"https://www.semanticscholar.org/paper/A-Watermark-for-Large-Language-Models-Kirchenbauer-Geiping/cb5b71a622aff47014d4f28a958679629a8b6363"},{"title":"ICML Poster A Watermark for Large Language Models","url":"https://icml.cc/virtual/2023/poster/24544"},{"title":"dblp: A Watermark for Large Language Models.","url":"https://dblp.org/rec/conf/icml/KirchenbauerGWK23.html"},{"title":"GitHub - jwkirchenbauer/lm-watermarking · GitHub","url":"https://github.com/jwkirchenbauer/lm-watermarking"},{"title":"A Watermark for Large Language Models | NSF Public Access Repository","url":"https://par.nsf.gov/biblio/10522346-watermark-large-language-models"},{"title":"[2306.04634] On the Reliability of Watermarks for Large Language Models","url":"https://arxiv.org/abs/2306.04634"},{"title":"A Watermark for Large Language Models","url":"https://arxiv.org/pdf/2301.10226"},{"title":"A Watermark for Large Language Models | Request PDF","url":"https://www.researchgate.net/publication/367388838_A_Watermark_for_Large_Language_Models"}]

I found the paper you're looking for. Here's what I found:

"A Watermark for Large Language Models" is by John Kirchenbauer, Jonas Geiping, Yuxin Wen, Jonathan Katz, Ian Miers, and Tom Goldstein, and it was published at ICML 2023.

The paper proposes a watermarking framework for proprietary language models that embeds signals into generated text that are invisible to humans but algorithmically detectable from a short span of tokens. The watermark can be embedded with negligible impact on text quality, and can be detected using an efficient op
…[truncated 560 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_review_ref-audit-B_20260526T104706",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 13 · 2026-05-26T10:53:59.337013+00:00_

Web search results for query: "Schaeffer Kazdan "Position: Model Collapse Does Not Mean What You Think" 2025 arXiv"

Links: [{"title":"[2503.03150] Position: Model Collapse Does Not Mean What You Think","url":"https://arxiv.org/abs/2503.03150"},{"title":"Position: Model Collapse Does Not Mean What You Think","url":"https://arxiv.org/pdf/2503.03150"},{"title":"Escaping Collapse: The Strength of Weak Data for Large Language Model TrainingAuthors ordered alphabetically. Author contributions are listed at the end.","url":"https://arxiv.org/html/2502.08924v2"},{"title":"Position: Model Collapse Does Not Mean What You Think - ADS","url":"https://ui.adsabs.harvard.edu/abs/2025arXiv250303150S/abstract"},{"title":"LLM Web Dynamics: Tracing Model Collapse in a Network of LLMs","url":"https://arxiv.org/html/2506.15690v1"},{"title":"Escaping Model Collapse via Synthetic Data Verification: Near-term Improvements and Long-term ConvergenceThis project is supported by the AI2050 program at Schmidt Sciences (Grant G-24-66104) and Army Research Office Award W911NF-23-1-0030. We also thank Cong Ma from UChicago, Hongning Wang and Bo Li from Tsinghua, Pinyan Lu and Gavin Tang from Shanghai University of Finance and Economics for helpful discussions and suggestions.","url":"https://arxiv.org/html/2510.16657v1"},{"title":"Computers and Society Mar 2025","url":"https://arxiv.org/list/cs.CY/2025-03?skip=300&show=25"},{"title":"Recursive Training Loops in LLMs: How training data properties modulate distribution shift in generated data?","url":"https://arxiv.org/html/2504.03814v4"},{"title":"Position: Model Collapse Does Not Mean What You Think | OpenReview","url":"https://openreview.net/forum?id=ygfzWIGDN8"}]

I found the paper you're looking for. Here's what I found:

"Position: Model Collapse Does Not Mean What You Think" is an arXiv paper by Rylan Schaeffer, Joshua Kazdan, Alvan Caleb Arulandu, and Sanmi Koyejo, submitted on March 5, 2025.

The paper addresses concerns over model collaps
…[truncated 695 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_review_ref-audit-B_20260526T104706",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-26T10:53:59.337187+00:00_

Web search results for query: "Mitchell Lee Khazatsky "DetectGPT Zero-Shot Machine-Generated Text Detection" ICML 2023"

Links: [{"title":"DetectGPT: Zero-Shot Machine-Generated Text Detection using Probability Curvature","url":"https://proceedings.mlr.press/v202/mitchell23a.html"},{"title":"[2301.11305] DetectGPT: Zero-Shot Machine-Generated Text Detection using Probability Curvature","url":"https://arxiv.org/abs/2301.11305"},{"title":"ICML Oral DetectGPT: Zero-Shot Machine-Generated Text Detection using Probability Curvature","url":"https://icml.cc/virtual/2023/oral/25525"},{"title":"dblp: DetectGPT: Zero-Shot Machine-Generated Text Detection using Probability Curvature.","url":"https://dblp.org/rec/conf/icml/Mitchell0KMF23.html"},{"title":"[Paper Note] DetectGPT: Zero-Shot Machine-Generated Text Detection using Probability Curvature, Eric Mitchell+, ICML'23, 2023.01 · Issue #3698 · AkihikoWatanabe/paper_notes","url":"https://github.com/AkihikoWatanabe/paper_notes/issues/3698"},{"title":"Eric Mitchell, Yoonho Lee, Alexander Khazatsky, Christopher D. Manning, Chelsea Finn · DetectGPT: Zero-Shot Machine-Generated Text Detection using Probability Curvature","url":"https://slideslive.com/39004346/detectgpt-zeroshot-machinegenerated-text-detection-using-probability-curvature"},{"title":"[PDF] DetectGPT: Zero-Shot Machine-Generated Text Detection using Probability Curvature | Semantic Scholar","url":"https://www.semanticscholar.org/paper/9a7ac45eafe11ca003db3a300505f3b5c3f9009a"},{"title":"ICML Poster DetectGPT: Zero-Shot Machine-Generated Text Detection using Probability Curvature","url":"https://icml.cc/virtual/2023/poster/24553"}]

I found the paper you're looking for. DetectGPT: Zero-Shot Machine-Generated Text Detection using Probability Curvature is authored by Eric Mitchell, Yoonho Lee, Alexander Khazatsky, Christopher D. Manning, and Chelsea Finn, and it was published in the Proceedings of the 40th International Conference on Machine Learning in 2023.

The paper
…[truncated 567 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_review_ref-audit-B_20260526T104706",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 15 · 2026-05-26T10:53:59.337390+00:00_

Web search results for query: "Kazdan Schaeffer "Collapse or Thrive? Perils and Promises of Synthetic Data" ICML 2025"

Links: [{"title":"Collapse or Thrive? Perils and Promises of Synthetic Data in a Self-Generating World","url":"https://arxiv.org/html/2410.16713v1"},{"title":"[2410.16713] Collapse or Thrive? Perils and Promises of Synthetic Data in a Self-Generating World","url":"https://arxiv.org/abs/2410.16713"},{"title":"A Closer Look at Model Collapse: From a Generalization-to-Memorization Perspective","url":"https://arxiv.org/html/2509.16499v1"},{"title":"1 Introduction","url":"https://arxiv.org/html/2410.16713"},{"title":"Position: Machine Learning Conferences Should Establish ...","url":"https://openreview.net/pdf?id=DS1XSAPvKs"},{"title":"[PDF] Collapse or Thrive? Perils and Promises of Synthetic Data in a Self-Generating World | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Collapse-or-Thrive-Perils-and-Promises-of-Synthetic-Kazdan-Schaeffer/4b510679ec7f6d138b04d5d0afff9ff316264974"},{"title":"Collapse or Thrive? Perils and Promises of Synthetic Data in a Self-Generating World | OpenReview","url":"https://openreview.net/forum?id=Xr5iINA3zU"},{"title":"GitHub - RylanSchaeffer/KoyejoLab-Collapse-or-Thrive: Code for Collapse or Thrive? Perils and Promises of Synthetic Data in a Self-Generating World","url":"https://github.com/RylanSchaeffer/KoyejoLab-Collapse-or-Thrive"},{"title":"(PDF) Collapse or Thrive? Perils and Promises of Synthetic Data in a Self-Generating World","url":"https://www.researchgate.net/publication/385140496_Collapse_or_Thrive_Perils_and_Promises_of_Synthetic_Data_in_a_Self-Generating_World"}]

Based on the search results, I found information about this paper:

"Collapse or Thrive? Perils and Promises of Synthetic Data in a Self-Generating World" is authored by Joshua Kazdan, Rylan Schaeffer, Apratim Dey, Matthias Gerstgrasser, Rafael Rafailov, David Donoho, and Sanmi Koyejo from Stanford University and Harvard SEAS.

The
…[truncated 1175 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_review_ref-audit-B_20260526T104706",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-26T10:53:59.337573+00:00_

Web search results for query: "Basani Chen "Diversity Boosts AI-Generated Text Detection" DivEye TMLR 2026"

Links: [{"title":"[2509.18880] Diversity Boosts AI-Generated Text Detection","url":"https://arxiv.org/abs/2509.18880"},{"title":"GitHub - IBM/diveye: [TMLR '26] Code for Diversity Boosts AI-generated Text Detection · GitHub","url":"https://github.com/IBM/diveye"},{"title":"[PDF] Diversity Boosts AI-Generated Text Detection | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Diversity-Boosts-AI-Generated-Text-Detection-Basani-Chen/77269d404ea3438f6d2ac327316f0b6ba116a48d"},{"title":"Diversity Boosts AI-Generated Text Detection","url":"https://arxiv.org/pdf/2509.18880"},{"title":"Diversity Boosts AI-Generated Text Detection Advik Raj Basani 1 Pin-Yu Chen 2","url":"https://openreview.net/pdf?id=QuDDXJ47nq"},{"title":"Diversity Boosts AI-Generated Text Detection | OpenReview","url":"https://openreview.net/forum?id=DNgsOhGZBI"},{"title":"DivEye","url":"https://diveye.vercel.app/"},{"title":"Under review as submission to TMLR Diversity Boosts AI-Generated Text Detection","url":"https://openreview.net/pdf?id=WscAU9It1l"},{"title":"[PDF] DivEye at PAN 2025: Diversity Boosts AI-Generated Text Detection | Semantic Scholar","url":"https://www.semanticscholar.org/paper/DivEye-at-PAN-2025:-Diversity-Boosts-AI-Generated-Basani-Chen/b18cdaf7ea2898664ed0850790059278ed50bb79"}]

I found the paper you're looking for! Here's what the search revealed:

The paper "Diversity Boosts AI-Generated Text Detection" is authored by Advik Raj Basani and Pin-Yu Chen, published at the "Data in Generative Models - The Bad, the Ugly, and the Greats" workshop in 2025, though your search noted TMLR 2026. Note that the author you mentioned is "Pin-Yu Chen," not "Basani Chen" – Basani is the first author's name.

The work introduces DivEye, which captures the signal that human-authored text exhibits richer variability in lexical and structural unpredictability than LLM outputs throug
…[truncated 627 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_review_ref-audit-B_20260526T104706",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-26T10:53:59.337765+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Zawalski Boubdir \"Detecting Data Contamination in LLMs via In-Context Learning\" ICLR 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_review_ref-audit-B_20260526T104706",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Zawalski Boubdir \"Detecting Data Contamination in LLMs via In-Context Learning\" ICLR 2026"
  }
}
```

</details>

---

### Tool call

_source line 18 · 2026-05-26T10:53:59.337918+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Zhang Sun Yeats \"Min-K%++ Improved Baseline Detecting Pre-Training Data\" ICLR 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_review_ref-audit-B_20260526T104706",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Zhang Sun Yeats \"Min-K%++ Improved Baseline Detecting Pre-Training Data\" ICLR 2025"
  }
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-26T10:53:59.338042+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Shumailov Shumaylov Zhao \"AI Models Collapse When Trained on Recursively Generated Data\" Nature 2024"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_review_ref-audit-B_20260526T104706",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Shumailov Shumaylov Zhao \"AI Models Collapse When Trained on Recursively Generated Data\" Nature 2024"
  }
}
```

</details>

---

### Tool call

_source line 20 · 2026-05-26T10:53:59.338160+00:00_

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
  "session": "worker_review_ref-audit-B_20260526T104706",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Alemohammad \"Self-Consuming Generative Models Go MAD\" ICLR 2024"
  }
}
```

</details>

---

### Tool call

_source line 21 · 2026-05-26T10:53:59.338276+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Dohmatob Feng Yang \"A Tale of Tails Model Collapse Change of Scaling Laws\" ICML 2024"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_review_ref-audit-B_20260526T104706",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Dohmatob Feng Yang \"A Tale of Tails Model Collapse Change of Scaling Laws\" ICML 2024"
  }
}
```

</details>

---

### Tool call

_source line 22 · 2026-05-26T10:53:59.338390+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Xie Santurkar Ma Liang \"Data Selection for Language Models via Importance Resampling\" NeurIPS 2023"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_review_ref-audit-B_20260526T104706",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Xie Santurkar Ma Liang \"Data Selection for Language Models via Importance Resampling\" NeurIPS 2023"
  }
}
```

</details>

---

### Tool result

_source line 23 · 2026-05-26T10:53:59.338539+00:00_

Web search results for query: "Zawalski Boubdir "Detecting Data Contamination in LLMs via In-Context Learning" ICLR 2026"

Links: [{"title":"Detecting Data Contamination in LLMs via In-Context ...","url":"https://openreview.net/pdf?id=YlpaaYxx4t"},{"title":"[2510.27055] Detecting Data Contamination in LLMs via In-Context Learning","url":"https://arxiv.org/abs/2510.27055"},{"title":"Detecting Data Contamination in LLMs via In-Context Learning","url":"https://arxiv.org/html/2510.27055v1"},{"title":"Detecting Data Contamination in LLMs via In-Context Learning | OpenReview","url":"https://openreview.net/forum?id=YlpaaYxx4t"},{"title":"DETECTING BENCHMARK CONTAMINATION THROUGH ...","url":"https://openreview.net/pdf?id=WFGxFzFDmQ"},{"title":"Detecting Data Contamination in LLMs via In-Context Learning Michał Zawalski†","url":"https://openreview.net/pdf/753f569951799d9078f4db2d0e9debd74ad5b692.pdf"},{"title":"Published as a conference paper at ICLR 2026 CONTAMINATION DETECTION","url":"https://openreview.net/pdf?id=gk6OC3XIZW"},{"title":"OBSCURING DATA CONTAMINATION ...","url":"https://openreview.net/pdf/2e5c661a0aff3003ce18874dc593210c26709c3e.pdf"},{"title":"ICLR 2026: Detecting Data Contamination in LLMs via In- ...","url":"https://www.linkedin.com/posts/besmira-nushi-43969712_our-work-on-data-contamination-analysis-was-activity-7422343437376561152-O2kU"},{"title":"OBSCURING DATA CONTAMINATION THROUGH TRANSLATION","url":"https://openreview.net/pdf?id=omg9K6lI93"}]

I found the paper! Here's what I found:

The paper "Detecting Data Contamination in LLMs via In-Context Learning" is authored by Michał Zawalski and Meriem Boubdir from NVIDIA, along with co-authors Klaudia Bałazy and Besmira Nushi from NVIDIA, and Pablo Ribalta from NVIDIA.

The paper presents Contamination Detection via Context (CoDeC), a practical and accurate method to detect and quantify training data contamination in large language models. 

CoDeC distinguishes between data memorized during training and 
…[truncated 680 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_review_ref-audit-B_20260526T104706",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 24 · 2026-05-26T10:53:59.338721+00:00_

Web search results for query: "Shumailov Shumaylov Zhao "AI Models Collapse When Trained on Recursively Generated Data" Nature 2024"

Links: [{"title":"A Note on Shumailov et al. (2024): 'AI Models Collapse ...","url":"https://arxiv.org/html/2410.12954v2"},{"title":"AI models collapse when trained on recursively generated data | Nature","url":"https://www.nature.com/articles/s41586-024-07566-y"},{"title":"AI models collapse when trained on recursively generated data - PubMed","url":"https://pubmed.ncbi.nlm.nih.gov/39048682/"},{"title":"A note on “AI models collapse when trained on recursively generated data” | by Ali Borji | Medium","url":"https://medium.com/@aliborji/a-note-on-ai-models-collapse-when-trained-on-recursively-generated-data-5bee1de1ab87"},{"title":"[PDF] AI models collapse when trained on recursively generated data | Semantic Scholar","url":"https://www.semanticscholar.org/paper/AI-models-collapse-when-trained-on-recursively-data-Shumailov-Shumaylov/603d3f90fc40f79ff51258f0295de3ec5107f73e"},{"title":"AI models collapse when trained on recursively generated data","url":"https://www.pure.ed.ac.uk/ws/portalfiles/portal/460496122/ShumailovEtalNature2024AIModelsCollapseWhen.pdf"},{"title":"AI models collapse when trained on recursively generated data","url":"https://bibbase.org/network/publication/shumailov-shumaylov-zhao-papernot-anderson-gal-aimodelscollapsewhentrainedonrecursivelygenerateddata-2024"},{"title":"AI models collapse when trained on recursively generated data - University of Edinburgh Research Explorer","url":"https://www.research.ed.ac.uk/en/publications/ai-models-collapse-when-trained-on-recursively-generated-data/"},{"title":"dblp: AI models collapse when trained on recursively generated data.","url":"https://dblp.uni-trier.de/rec/journals/nature/ShumailovSZPAG24.html"},{"title":"Author Correction: AI models collapse when trained on recursively generated data | Nature","url":"https://www.nature.com/articles/s41586-025-08905-3"}]

I found
…[truncated 1233 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_review_ref-audit-B_20260526T104706",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 25 · 2026-05-26T10:53:59.338927+00:00_

Web search results for query: "Alemohammad "Self-Consuming Generative Models Go MAD" ICLR 2024"

Links: [{"title":"SELF-CONSUMING GENERATIVE MODELS GO MAD","url":"https://proceedings.iclr.cc/paper_files/paper/2024/file/ebc042e767de551803ccfcc45e2454f5-Paper-Conference.pdf"},{"title":"Self-Consuming Generative Models Go MAD | OpenReview","url":"https://openreview.net/forum?id=ShjMHfmPs0"},{"title":"SELF-CONSUMING GENERATIVE MODELS GO MAD - Houston Methodist Scholars","url":"https://scholars.houstonmethodist.org/en/publications/self-consuming-generative-models-go-mad/"},{"title":"[PDF] Self-Consuming Generative Models Go MAD | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Self-Consuming-Generative-Models-Go-MAD-Alemohammad-Casco-Rodriguez/ad022cd5da75637ac3e0a8f8cc4f0d394ba5ff7a"},{"title":"Self-Consuming Generative Models Go MAD | NSF Public Access Repository","url":"https://par.nsf.gov/biblio/10570494"},{"title":"ICLR Poster Self-Consuming Generative Models Go MAD","url":"https://iclr.cc/virtual/2024/poster/18592"},{"title":"Self-Consuming AI Resources","url":"https://dsp.rice.edu/ai-loops/"},{"title":"[2307.01850] Self-Consuming Generative Models Go MAD","url":"https://arxiv.org/abs/2307.01850"},{"title":"Self-Consuming Generative Models Go MAD | Montreal AI Ethics Institute","url":"https://montrealethics.ai/self-consuming-generative-models-go-mad/"}]

I found the paper! Here are the search results for the query:

## "Self-Consuming Generative Models Go MAD" - ICLR 2024

This paper addresses the problem of using AI-synthesized data to train next-generation generative models, where repeating this process creates an autophagous ("self-consuming") loop whose properties are poorly understood.

**Key Finding:**
Without enough fresh real data in each generation of an autophagous loop, generative models are doomed to have their quality (precision) or diversity (recall) progressively decrease—a condition termed Model Autophagy Disorder (MAD), by analogy to
…[truncated 841 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_review_ref-audit-B_20260526T104706",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 26 · 2026-05-26T10:53:59.339104+00:00_

Web search results for query: "Dohmatob Feng Yang "A Tale of Tails Model Collapse Change of Scaling Laws" ICML 2024"

Links: [{"title":"[2402.07043] A Tale of Tails: Model Collapse as a Change of Scaling Laws","url":"https://arxiv.org/abs/2402.07043"},{"title":"[Quick Review] A Tale of Tails: Model Collapse as a Change of Scaling Laws","url":"https://liner.com/review/tale-tails-model-collapse-as-change-scaling-laws"},{"title":"Overcoming the AI Data Crisis: A New Solution to Model Collapse | by NYU Center for Data Science | Medium","url":"https://nyudatascience.medium.com/overcoming-the-ai-data-crisis-a-new-solution-to-model-collapse-ddc5b382e182"},{"title":"ICML Poster A Tale of Tails: Model Collapse as a Change of Scaling Laws","url":"https://icml.cc/virtual/2024/poster/34339"},{"title":"A Tale of Tails: Model Collapse as a Change of Scaling Laws","url":"https://proceedings.mlr.press/v235/dohmatob24b.html"},{"title":"A Tale of Tails: Model Collapse as a Change of Scaling Laws - NYU Scholars","url":"https://nyuscholars.nyu.edu/en/publications/a-tale-of-tails-model-collapse-as-a-change-of-scaling-laws"},{"title":"A Tale of Tails: Model Collapse as a Change of Scaling Laws | NSF Public Access Repository","url":"https://par.nsf.gov/biblio/10534888-tale-tails-model-collapse-change-scaling-laws"},{"title":"A Tale of Tails: Model Collapse as a Change of Scaling Laws | AI Research Paper Details","url":"https://www.aimodels.fyi/papers/arxiv/tale-tails-model-collapse-as-change-scaling"},{"title":"A Tale of Tails: Model Collapse as a Change of Scaling Laws","url":"https://openreview.net/pdf/c028ead5595978096e7ba1f2c41cc3bb709058f9.pdf"}]

I found the paper! Here's what I found about it:

"A Tale of Tails: Model Collapse as a Change of Scaling Laws" by Dohmatob, Feng, Yang, Charton, and Kempe was published in the Proceedings of the 41st International Conference on Machine Learning in 2024.

**Overview:**
The paper addresses how neural scaling laws will change as synthetic dat
…[truncated 940 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_review_ref-audit-B_20260526T104706",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 27 · 2026-05-26T10:53:59.339287+00:00_

Web search results for query: "Xie Santurkar Ma Liang "Data Selection for Language Models via Importance Resampling" NeurIPS 2023"

Links: [{"title":"NeurIPS Poster Data Selection for Language Models via Importance Resampling","url":"https://neurips.cc/virtual/2023/poster/70154"},{"title":"[2302.03169] Data Selection for Language Models via Importance Resampling","url":"https://arxiv.org/abs/2302.03169"},{"title":"Data Selection for Language Models via Importance Resampling","url":"https://proceedings.neurips.cc//paper_files/paper/2023/hash/6b9aa8f418bde2840d5f4ab7a02f663b-Abstract-Conference.html"},{"title":"[PDF] Data Selection for Language Models via Importance Resampling | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Data-Selection-for-Language-Models-via-Importance-Xie-Santurkar/74013b7cfa0fc524803350fca51341004565eb22"},{"title":"Data Selection for Language Models via Importance Resampling | OpenReview","url":"https://openreview.net/forum?id=uPSQv0leAu"},{"title":"Sang Michael Xie, Shibani Santurkar, Tengyu Ma, Percy Liang · Data Selection for Language Models via Importance Resampling","url":"https://slideslive.com/39009489/data-selection-for-language-models-via-importance-resampling"},{"title":"[Quick Review] Data Selection for Language Models via Importance Resampling","url":"https://liner.com/review/data-selection-for-language-models-via-importance-resampling"},{"title":"Data Selection for Language Models via Importance Resampling - ADS","url":"https://ui.adsabs.harvard.edu/abs/2023arXiv230203169X/abstract"},{"title":"Paper page - Data Selection for Language Models via Importance Resampling","url":"https://huggingface.co/papers/2302.03169"},{"title":"Data Selection for Language Models via Importance Resampling","url":"https://arxiv.org/pdf/2302.03169"}]

I found comprehensive information about this paper. Here are the search results:

## Paper Overview

The paper "Data Selection for Language Models via Importance Resampling" was published 
…[truncated 1368 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_review_ref-audit-B_20260526T104706",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 28 · 2026-05-26T10:53:59.339465+00:00_

Web search results for query: "Zhang Sun Yeats "Min-K%++ Improved Baseline Detecting Pre-Training Data" ICLR 2025"

Links: [{"title":"MIN-K%++: IMPROVED BASELINE FOR DETECTING PRE ...","url":"https://proceedings.iclr.cc/paper_files/paper/2025/file/a2e3b4132ab2e0b7a21e6e75da7f91a9-Paper-Conference.pdf"},{"title":"[2404.02936] Min-K%++: Improved Baseline for Detecting Pre-Training Data from Large Language Models","url":"https://arxiv.org/abs/2404.02936"},{"title":"Min-K%++: Improved Baseline for Detecting Pre-Training ...","url":"https://iclr.cc/media/iclr-2025/Slides/29228.pdf"},{"title":"min-k%++: improved baseline for detecting pre-training ...","url":"https://arxiv.org/pdf/2404.02936"},{"title":"Min-K%++: Improved Baseline for Pre-Training Data Detection from Large Language Models | OpenReview","url":"https://openreview.net/forum?id=ZGkfoufDaU"},{"title":"GitHub - zjysteven/mink-plus-plus: [ICLR'25 Spotlight] Min-K%++: Improved baseline for detecting pre-training data of LLMs · GitHub","url":"https://github.com/zjysteven/mink-plus-plus"},{"title":"Min-K%++: Improved Baseline for Detecting Pre-Training ...","url":"https://zjysteven.github.io/mink-plus-plus/"},{"title":"Min-K%++: Improved Baseline for Detecting Pre-Training Data from Large Language Models | AI Research Paper Details","url":"https://www.aimodels.fyi/papers/arxiv/min-kpercent-improved-baseline-detecting-pre-training"},{"title":"(PDF) Min-K%++: Improved Baseline for Detecting Pre-Training Data from Large Language Models","url":"https://www.researchgate.net/publication/379541659_Min-K_Improved_Baseline_for_Detecting_Pre-Training_Data_from_Large_Language_Models"}]

I found relevant information about the paper! Here are the search results:

The paper "Min-K%++: Improved Baseline for Detecting Pre-Training Data" was published as a conference paper at ICLR 2025.

The authors are Jingyang Zhang, Jingwei Sun, Eric Yeats, Yang Ouyang, Martin Kuo, Jianyi Zhang, Hao Frank Yang, and Hai Li.

The paper addresses t
…[truncated 950 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_review_ref-audit-B_20260526T104706",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool call

_source line 29 · 2026-05-26T10:53:59.339647+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Tirumala Simig Aghajanyan Morcos \"D4 Improving LLM Pretraining Document De-Duplication Diversification\" NeurIPS 2023"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_review_ref-audit-B_20260526T104706",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Tirumala Simig Aghajanyan Morcos \"D4 Improving LLM Pretraining Document De-Duplication Diversification\" NeurIPS 2023"
  }
}
```

</details>

---

### Tool call

_source line 30 · 2026-05-26T10:53:59.339792+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Xie Pham Dong \"DoReMi Optimizing Data Mixtures Speeds Up Language Model Pretraining\" NeurIPS 2023"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_review_ref-audit-B_20260526T104706",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Xie Pham Dong \"DoReMi Optimizing Data Mixtures Speeds Up Language Model Pretraining\" NeurIPS 2023"
  }
}
```

</details>

---

### Tool call

_source line 31 · 2026-05-26T10:53:59.339922+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Hans Schwarzschild Cherepanova \"Spotting LLMs With Binoculars\" ICML 2024"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_review_ref-audit-B_20260526T104706",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Hans Schwarzschild Cherepanova \"Spotting LLMs With Binoculars\" ICML 2024"
  }
}
```

</details>

---

### Tool call

_source line 32 · 2026-05-26T10:53:59.340041+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Alain Bengio \"Understanding Intermediate Layers Using Linear Classifier Probes\" 2017 ICLR workshop"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_review_ref-audit-B_20260526T104706",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Alain Bengio \"Understanding Intermediate Layers Using Linear Classifier Probes\" 2017 ICLR workshop"
  }
}
```

</details>

---

### Tool call

_source line 33 · 2026-05-26T10:53:59.340158+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Belinkov \"Probing Classifiers Promises Shortcomings Advances\" Computational Linguistics 2022"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_review_ref-audit-B_20260526T104706",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Belinkov \"Probing Classifiers Promises Shortcomings Advances\" Computational Linguistics 2022"
  }
}
```

</details>

---

### Tool call

_source line 34 · 2026-05-26T10:53:59.340272+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Bao Zhao Teng \"Fast-DetectGPT Efficient Zero-Shot Detection Machine-Generated Text\" ICLR 2024"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_review_ref-audit-B_20260526T104706",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Bao Zhao Teng \"Fast-DetectGPT Efficient Zero-Shot Detection Machine-Generated Text\" ICLR 2024"
  }
}
```

</details>

---

### Tool result

_source line 35 · 2026-05-26T10:53:59.340420+00:00_

Web search results for query: "Tirumala Simig Aghajanyan Morcos "D4 Improving LLM Pretraining Document De-Duplication Diversification" NeurIPS 2023"

Links: [{"title":"D4: Improving LLM Pretraining via Document De-Duplication and Diversification","url":"https://proceedings.neurips.cc/paper_files/paper/2023/hash/a8f8cbd7f7a5fb2c837e578c75e5b615-Abstract-Datasets_and_Benchmarks.html"},{"title":"NeurIPS Poster D4: Improving LLM Pretraining via Document De-Duplication and Diversification","url":"https://neurips.cc/virtual/2023/poster/73662"},{"title":"[2308.12284] D4: Improving LLM Pretraining via Document De-Duplication and Diversification","url":"https://arxiv.org/abs/2308.12284"},{"title":"D4: Improving LLM Pretraining via Document De-Duplication and Diversification","url":"https://papers.nips.cc/paper_files/paper/2023/hash/a8f8cbd7f7a5fb2c837e578c75e5b615-Abstract-Datasets_and_Benchmarks.html"},{"title":"[PDF] D4: Improving LLM Pretraining via Document De-Duplication and Diversification | Semantic Scholar","url":"https://www.semanticscholar.org/paper/D4:-Improving-LLM-Pretraining-via-Document-and-Tirumala-Simig/11cf88dce827bd67cbfa60400306318022e736d5"},{"title":"D4: Improving LLM Pretraining via Document De-Duplication and Diversiﬁcation","url":"https://proceedings.neurips.cc/paper_files/paper/2023/file/a8f8cbd7f7a5fb2c837e578c75e5b615-Paper-Datasets_and_Benchmarks.pdf"},{"title":"D4: Improving LLM Pretraining via Document De-Duplication and Diversification","url":"https://arxiv.org/pdf/2308.12284"},{"title":"Kushal Tirumala, Daniel Simig, Armen Aghajanyan, Ari S. Morcos · D4: Improving LLM Pretraining via Document De-Duplication and Diversification","url":"https://slideslive.com/39010897/d4-improving-llm-pretraining-via-document-deduplication-and-diversification"},{"title":"Paper page - D4: Improving LLM Pretraining via Document De-Duplication and Diversification","url":"https://paperswithcode.com/paper/d4-improving-llm-pretraining-via-document-de"}]

I found the 
…[truncated 1193 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_review_ref-audit-B_20260526T104706",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 36 · 2026-05-26T10:53:59.340600+00:00_

Web search results for query: "Hans Schwarzschild Cherepanova "Spotting LLMs With Binoculars" ICML 2024"

Links: [{"title":"GitHub - ahans30/Binoculars: [ICML 2024] Binoculars: Zero-Shot Detection of LLM-Generated Text · GitHub","url":"https://github.com/ahans30/Binoculars"},{"title":"Spotting LLMs with binoculars | Proceedings of the 41st International Conference on Machine Learning","url":"https://dl.acm.org/doi/10.5555/3692070.3692768"},{"title":"[2401.12070] Spotting LLMs With Binoculars: Zero-Shot Detection of Machine-Generated Text","url":"https://arxiv.org/abs/2401.12070"},{"title":"Spotting LLMs With Binoculars: Zero-Shot Detection of Machine-Generated Text | MPI-IS","url":"https://is.mpg.de/en/publications/hans_spotting_2024"},{"title":"Spotting LLMs With Binoculars: Zero-Shot Detection of Machine-Generated Text","url":"https://proceedings.mlr.press/v235/hans24a.html"},{"title":"Spotting LLMs With Binoculars: Zero-Shot Detection of Machine-Generated Text | Safety- and Efficiency- aligned Learning – MPI-IS","url":"https://is.mpg.de/seal/publications/hans_spotting_2024"},{"title":"[PDF] Spotting LLMs With Binoculars: Zero-Shot Detection of Machine-Generated Text | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Spotting-LLMs-With-Binoculars:-Zero-Shot-Detection-Hans-Schwarzschild/8dafb105a0cec1956443003eeea9fcf13c0ffa99"},{"title":"Binoculars/README.md at main · ahans30/Binoculars","url":"https://github.com/ahans30/Binoculars/blob/main/README.md"},{"title":"[2401.12070v2] Spotting LLMs With Binoculars: Zero-Shot Detection of Machine-Generated Text","url":"https://arxiv.org/abs/2401.12070v2"},{"title":"[2401.12070v1] Spotting LLMs With Binoculars: Zero-Shot Detection of Machine-Generated Text","url":"https://arxiv.org/abs/2401.12070v1"}]

I found the paper! Here are the search results for "Spotting LLMs With Binoculars" ICML 2024:

## Overview

The paper "Spotting LLMs With Binoculars: Zero-Shot Detection of Machine-Generated Text" was published
…[truncated 1135 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_review_ref-audit-B_20260526T104706",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 37 · 2026-05-26T10:53:59.340789+00:00_

Web search results for query: "Xie Pham Dong "DoReMi Optimizing Data Mixtures Speeds Up Language Model Pretraining" NeurIPS 2023"

Links: [{"title":"NeurIPS Poster DoReMi: Optimizing Data Mixtures Speeds Up Language Model Pretraining","url":"https://neurips.cc/virtual/2023/poster/70588"},{"title":"DoReMi: Optimizing Data Mixtures Speeds Up Language Model Pretraining","url":"https://arxiv.org/pdf/2305.10429"},{"title":"[2305.10429] DoReMi: Optimizing Data Mixtures Speeds Up Language Model Pretraining","url":"https://arxiv.org/abs/2305.10429"},{"title":"[Quick Review] DoReMi: Optimizing Data Mixtures Speeds Up Language Model Pretraining","url":"https://liner.com/review/doremi-optimizing-data-mixtures-speeds-up-language-model-pretraining"},{"title":"GitHub - sangmichaelxie/doremi: Pytorch implementation of DoReMi, a method for optimizing the data mixture weights in language modeling datasets · GitHub","url":"https://github.com/sangmichaelxie/doremi"},{"title":"DoReMi: Optimizing Data Mixtures Speeds Up Language Model Pretraining - ADS","url":"https://ui.adsabs.harvard.edu/abs/2023arXiv230510429X/abstract"},{"title":"DoReMi: Optimizing Data Mixtures Speeds Up Language Model Pretraining","url":"https://proceedings.neurips.cc/paper_files/paper/2023/file/dcba6be91359358c2355cd920da3fcbd-Paper-Conference.pdf"},{"title":"[PDF] DoReMi: Optimizing Data Mixtures Speeds Up Language Model Pretraining | Semantic Scholar","url":"https://www.semanticscholar.org/paper/DoReMi:-Optimizing-Data-Mixtures-Speeds-Up-Language-Xie-Pham/9b4f7c97c0b83a80c32bc0b93595cbcfb4ecb16d"},{"title":"DoReMi: Optimizing Data Mixtures Speeds Up Language Model Pretraining | Request PDF","url":"https://www.researchgate.net/publication/401463528_DoReMi_Optimizing_Data_Mixtures_Speeds_Up_Language_Model_Pretraining"}]

I found comprehensive information about the DoReMi paper from NeurIPS 2023. Here are the key details:

**Paper Overview:**
The paper is authored by Sang Michael Xie, Hieu Pham, Xuanyi Dong, Nan D
…[truncated 1183 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_review_ref-audit-B_20260526T104706",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 38 · 2026-05-26T10:53:59.340978+00:00_

Web search results for query: "Bao Zhao Teng "Fast-DetectGPT Efficient Zero-Shot Detection Machine-Generated Text" ICLR 2024"

Links: [{"title":"GitHub - baoguangsheng/fast-detect-gpt: Code base for ICLR 2024 \"Fast-DetectGPT: Efficient Zero-Shot Detection of Machine-Generated Text via Conditional Probability Curvature\". · GitHub","url":"https://github.com/baoguangsheng/fast-detect-gpt"},{"title":"Published as a conference paper at ICLR 2024","url":"https://arxiv.org/pdf/2310.05130"},{"title":"ICLR Poster Fast-DetectGPT: Efficient Zero-Shot Detection of Machine-Generated Text via Conditional Probability Curvature","url":"https://iclr.cc/virtual/2024/poster/19201"},{"title":"Fast-DetectGPT: Efficient Zero-Shot Detection of Machine-Generated Text via Conditional Probability Curvature | OpenReview","url":"https://openreview.net/forum?id=Bpcgcr8E8Z"},{"title":"[2310.05130] Fast-DetectGPT: Efficient Zero-Shot Detection of Machine-Generated Text via Conditional Probability Curvature","url":"https://arxiv.org/abs/2310.05130"},{"title":"Fast-DetectGPT: Efficient Zero-Shot Detection of Machine-Generated Text via Conditional Probability Curvature","url":"https://proceedings.iclr.cc/paper_files/paper/2024/hash/6b8c6f846c3575e1d1ad496abea28826-Abstract-Conference.html"},{"title":"Google Scholar","url":"https://scholar.google.com/scholar?q=Guangsheng+Bao,+Yanbin+Zhao,+Zhiyang+Teng,+Linyi+Yang,+and+Yue+Zhang.+2024.+Fast-DetectGPT:+Efficient+Zero-Shot+Detection+of+Machine-Generated+Text+via+Conditional+Probability+Curvature.+In+The+Twelfth+International+Conference+on+Learning+Representations.+https://openreview.net/forum?id%3DBpcgcr8E8Z"},{"title":"ICLR 2024 | Fast-DetectGPT: Efficient Zero-Shot Detection of Machine-Generated Text - YouTube","url":"https://www.youtube.com/watch?v=Nk7LpsrIUDE"},{"title":"(PDF) FAST-DETECTGPT: EFFICIENT ZERO-SHOT DETEC- TION OF MACHINE-GENERATED TEXT VIA CONDI- TIONAL PROBABILITY CURVATURE","url":"https://www.researchgate.net/publication/388188914_
…[truncated 1333 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_review_ref-audit-B_20260526T104706",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 39 · 2026-05-26T10:53:59.341151+00:00_

Web search results for query: "Alain Bengio "Understanding Intermediate Layers Using Linear Classifier Probes" 2017 ICLR workshop"

Links: [{"title":"Workshop track - ICLR 2017 UNDERSTANDING INTERMEDIATE LAYERS","url":"https://openreview.net/pdf?id=HJ4-rAVtl"},{"title":"[1610.01644] Understanding intermediate layers using linear classifier probes","url":"https://arxiv.org/abs/1610.01644"},{"title":"[PDF] Understanding intermediate layers using linear classifier probes | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Understanding-intermediate-layers-using-linear-Alain-Bengio/5e23a28063b395bdaf784dc548a046885cb90cf2"},{"title":"(PDF) Understanding intermediate layers using linear classifier probes","url":"https://www.researchgate.net/publication/308913017_Understanding_intermediate_layers_using_linear_classifier_probes"},{"title":"Understanding intermediate layers using linear classiﬁer probes Guillaume Alain","url":"https://arxiv.org/pdf/1610.01644"},{"title":"Understanding intermediate layers using linear classifier probes","url":"http://index.cslt.org/mediawiki/images/f/f6/Understanding_intermediate_layers_using_linear_classifier_probes.pdf"},{"title":"[1610.01644v3] Understanding intermediate layers using linear classifier probes","url":"https://arxiv.org/abs/1610.01644v3"},{"title":"[1610.01644v1] Understanding intermediate layers using linear classifier probes","url":"https://www.arxiv.org/abs/1610.01644v1"}]

I found the paper! The paper "Understanding Intermediate Layers Using Linear Classifier Probes" was authored by Guillaume Alain & Yoshua Bengio and presented at the ICLR 2017 workshop track.

The method uses linear classifiers, referred to as "probes", where a probe can only use the hidden units of a given intermediate layer as discriminating features. These probes cannot affect the training phase of a model, and they are generally added after training.

The paper proposes a new method to better understand the roles and dynamics of the int
…[truncated 367 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_review_ref-audit-B_20260526T104706",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 40 · 2026-05-26T10:53:59.341330+00:00_

Web search results for query: "Belinkov "Probing Classifiers Promises Shortcomings Advances" Computational Linguistics 2022"

Links: [{"title":"Probing Classifiers: Promises, Shortcomings, and Advances - ACL Anthology","url":"https://aclanthology.org/2022.cl-1.7/"},{"title":"[2102.12452] Probing Classifiers: Promises, Shortcomings, and Advances","url":"https://arxiv.org/abs/2102.12452"},{"title":"Probing Classifiers: Promises, Shortcomings, and Advances | Computational Linguistics | MIT Press","url":"https://direct.mit.edu/coli/article/48/1/207/107571/Probing-Classifiers-Promises-Shortcomings-and"},{"title":"Yonatan Belinkov | publications","url":"https://belinkov.com/publications/publicationstype/"},{"title":"Probing Classifiers: Promises, Shortcomings, and Advances - Technion - Israel Institute of Technology","url":"https://cris.technion.ac.il/en/publications/probing-classifiers-promises-shortcomings-and-advances/"},{"title":"(PDF) Probing Classifiers: Promises, Shortcomings, and Advances","url":"https://www.researchgate.net/publication/355072709_Probing_Classifiers_Promises_Shortcomings_and_Advances"},{"title":"Probing Classifiers: Promises, Shortcomings, and Advances - Israeli Research Community Portal","url":"https://cris.iucc.ac.il/en/publications/probing-classifiers-promises-shortcomings-and-advances/"},{"title":"@article{belinkov-2022-probing,","url":"https://aclanthology.org/2022.cl-1.7.bib"},{"title":"Probing Classifiers: Promises, Shortcomings, and Advances","url":"https://aclanthology.org/2022.cl-1.7.pdf"}]

I found the paper! Here are the search results for the article:

**"Probing Classifiers: Promises, Shortcomings, and Advances"** by Yonatan Belinkov

**Publication Details:**
- Author: Yonatan Belinkov; Published: 2022; Journal: Computational Linguistics, Volume 48, Issue 1, Pages 207–219

**Summary:**
Probing classifiers have emerged as one of the prominent methodologies for interpreting and analyzing deep neural network models of natural language p
…[truncated 749 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_review_ref-audit-B_20260526T104706",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool call

_source line 41 · 2026-05-26T10:53:59.341505+00:00_

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
  "session": "worker_review_ref-audit-B_20260526T104706",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Frank Hall \"A Simple Approach to Ordinal Classification\" ECML 2001"
  }
}
```

</details>

---

### Tool call

_source line 42 · 2026-05-26T10:53:59.341632+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Cheng Zhou Jiang \"Beyond Binary Towards Fine-Grained LLM-Generated Text Detection Role Recognition\" WWW 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_review_ref-audit-B_20260526T104706",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Cheng Zhou Jiang \"Beyond Binary Towards Fine-Grained LLM-Generated Text Detection Role Recognition\" WWW 2025"
  }
}
```

</details>

---

### Tool call

_source line 43 · 2026-05-26T10:53:59.341768+00:00_

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
  "session": "worker_review_ref-audit-B_20260526T104706",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Mehta \"Beyond Surface-Level Similarity Hierarchical Contamination Detection\" arXiv 2511.17602"
  }
}
```

</details>

---

### Tool call

_source line 44 · 2026-05-26T10:53:59.341909+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Sun Zhang Shen \"Are We in the AI-Generated Text World Already Quantifying Monitoring AIGT Social Media\" ACL 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_review_ref-audit-B_20260526T104706",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Sun Zhang Shen \"Are We in the AI-Generated Text World Already Quantifying Monitoring AIGT Social Media\" ACL 2025"
  }
}
```

</details>

---

### Tool call

_source line 45 · 2026-05-26T10:53:59.342027+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Spennemann \"Delving into Quantification of AI-Generated Content on the Internet\" arXiv 2504.08755"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_review_ref-audit-B_20260526T104706",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Spennemann \"Delving into Quantification of AI-Generated Content on the Internet\" arXiv 2504.08755"
  }
}
```

</details>

---

### Tool call

_source line 46 · 2026-05-26T10:53:59.342143+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Dohmatob Feng Subramonian Kempe \"Strong Model Collapse\" ICLR 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_review_ref-audit-B_20260526T104706",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Dohmatob Feng Subramonian Kempe \"Strong Model Collapse\" ICLR 2025"
  }
}
```

</details>

---

### Tool result

_source line 47 · 2026-05-26T10:53:59.342290+00:00_

Web search results for query: "Cheng Zhou Jiang "Beyond Binary Towards Fine-Grained LLM-Generated Text Detection Role Recognition" WWW 2025"

Links: [{"title":"[2410.14259] Beyond Binary: Towards Fine-Grained LLM-Generated Text Detection via Role Recognition and Involvement Measurement","url":"https://arxiv.org/abs/2410.14259"},{"title":"[2410.14259v1] Beyond Binary: Towards Fine-Grained LLM-Generated Text Detection via Role Recognition and Involvement Measurement","url":"https://arxiv.org/abs/2410.14259v1"},{"title":"Beyond Binary: Towards Fine-Grained LLM-Generated Text Detection via Role Recognition and Involvement Measurement – Own Your AI","url":"https://ownyourai.com/beyond-binary-towards-fine-grained-llm-generated-text-detection-via-role-recognition-and-involvement-measurement/"},{"title":"Beyond Binary: Towards Fine-Grained LLM-Generated Text Detection via Role Recognition and Involvement Measurement | Proceedings of the ACM on Web Conference 2025","url":"https://dl.acm.org/doi/10.1145/3696410.3714770"},{"title":"Beyond Binary: Towards Fine-Grained LLM-Generated Text Detection via Role Recognition and Involvement Measurement","url":"https://arxiv.org/html/2410.14259v2"},{"title":"Papers with Code - Beyond Binary: Towards Fine-Grained LLM-Generated Text Detection via Role Recognition and Involvement Measurement","url":"https://paperswithcode.com/paper/beyond-binary-towards-fine-grained-llm"},{"title":"On the Detectability of LLM-Generated Text: What Exactly Is LLM-Generated Text?","url":"https://arxiv.org/html/2510.20810v1"}]

I found the paper you're looking for. Here are the key details:

**Paper Title:** "Beyond Binary: Towards Fine-Grained LLM-Generated Text Detection via Role Recognition and Involvement Measurement"

**Authors:** Zihao Cheng, Li Zhou, Feng Jiang, Benyou Wang, and Haizhou Li

**Conference:** Published in Proceedings of the ACM on Web Conference 2025, pages 2677–2688

**Key Contribution:** The paper proposes a new paradigm for detecting LL
…[truncated 569 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_review_ref-audit-B_20260526T104706",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 48 · 2026-05-26T10:53:59.342458+00:00_

Web search results for query: "Frank Hall "A Simple Approach to Ordinal Classification" ECML 2001"

Links: [{"title":"A Simple Approach to Ordinal Classification | Springer Nature Link","url":"https://link.springer.com/chapter/10.1007/3-540-44795-4_13"},{"title":"[PDF] A Simple Approach to Ordinal Classification | Semantic Scholar","url":"https://www.semanticscholar.org/paper/A-Simple-Approach-to-Ordinal-Classification-Frank-Hall/76fc26939d73c565431e1f38107a4245e739284e"},{"title":"A simple approach to ordinal classification.","url":"https://researchcommons.waikato.ac.nz/items/ce0009f5-92fa-4113-b8b2-7ac929cfd32c"},{"title":"(PDF) A Simple Approach to Ordinal Classification (2001) | Eibe Frank | 655 Citations","url":"https://scispace.com/papers/a-simple-approach-to-ordinal-classification-2mjbzk39ox"},{"title":"(PDF) A Simple Approach to Ordinal Classification","url":"https://www.researchgate.net/publication/226877154_A_Simple_Approach_to_Ordinal_Classification"},{"title":"A simple approach to ordinal classification | Proceedings of the 12th European Conference on Machine Learning","url":"https://dl.acm.org/doi/10.1007/3-540-44795-4_13"},{"title":"An Improved Approach to Ordinal Classification | Springer Nature Link","url":"https://link.springer.com/chapter/10.1007/978-3-662-45652-1_4"},{"title":"A Simple Approach to Ordinal Classification - Eibe Frank, Mark Andrew Hall - Google Books","url":"https://books.google.com/books/about/A_Simple_Approach_to_Ordinal_Classificat.html?id=SI2oMQAACAAJ"},{"title":"Classification of Ordinal Data Using Neural Networks | Springer Nature Link","url":"https://link.springer.com/chapter/10.1007/11564096_70"},{"title":"GitHub - liorsidi/ordinal-classifier: python implemantation for Ordinal classifier by Frank, Eibe, and Mark Hall. \"A simple approach to ordinal classification.\" European Conference on Machine Learning. Springer Berlin Heidelberg, 2001.","url":"https://github.com/liorsidi/ordinal-classifier"}]

I found the paper you were 
…[truncated 829 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_review_ref-audit-B_20260526T104706",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 49 · 2026-05-26T10:53:59.342630+00:00_

Web search results for query: "Mehta "Beyond Surface-Level Similarity Hierarchical Contamination Detection" arXiv 2511.17602"

Links: [{"title":"[2511.17602] Beyond Surface-Level Similarity: Hierarchical Contamination Detection for Synthetic Training Data in Foundation Models","url":"https://arxiv.org/abs/2511.17602"},{"title":"Beyond Surface-Level Similarity: Hierarchical Contamination Detection for Synthetic Training Data in Foundation Models","url":"https://arxiv.org/html/2511.17602v1"},{"title":"Beyond Surface-Level Similarity: Hierarchical Contamination Detection","url":"https://www.arxiv.org/pdf/2511.17602"},{"title":"(PDF) Beyond Surface-Level Similarity: Hierarchical Contamination Detection for Synthetic Training Data in Foundation Models","url":"https://www.researchgate.net/publication/397933312_Beyond_Surface-Level_Similarity_Hierarchical_Contamination_Detection_for_Synthetic_Training_Data_in_Foundation_Models"},{"title":"Beyond Surface-Level Similarity: Hierarchical Contamination Detection for Synthetic Training Data in Foundation Models | Article Information | J-GLOBAL","url":"https://jglobal.jst.go.jp/en/detail?JGLOBAL_ID=202502216067314793"},{"title":"Machine Learning Feb 2025","url":"https://arxiv.org/list/cs.LG/2025-02?skip=3050&show=2000"},{"title":"Computer Science","url":"https://arxiv.org/list/cs/pastweek?skip=235&show=1000"},{"title":"Machine Learning Oct 2024","url":"https://arxiv.org/list/cs.LG/2024-10?skip=1475&show=2000"},{"title":"Machine Learning Jun 2024","url":"https://web3.arxiv.org/list/cs.LG/2024-06?skip=1900&show=2000"},{"title":"Machine Learning Jan 2024","url":"https://arxiv.org/list/cs.LG/2024-01?skip=325&show=2000"}]

I found the paper you're looking for! Here's the information about it:

**Title:** Beyond Surface-Level Similarity: Hierarchical Contamination Detection for Synthetic Training Data in Foundation Models

**Author:** Sushant Mehta

**ArXiv ID:** 2511.17602

**Publication Date:** November 18, 2025

**Summary:**

Synthe
…[truncated 878 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_review_ref-audit-B_20260526T104706",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 50 · 2026-05-26T10:53:59.342817+00:00_

Web search results for query: "Spennemann "Delving into Quantification of AI-Generated Content on the Internet" arXiv 2504.08755"

Links: [{"title":"[2504.08755] Delving into: the quantification of Ai-generated content on the internet (synthetic data)","url":"https://arxiv.org/abs/2504.08755"},{"title":"(PDF) Delving into: the quantification of Ai-generated content on the internet (synthetic data)","url":"https://www.researchgate.net/publication/390772908_Delving_into_the_quantification_of_Ai-generated_content_on_the_internet_synthetic_data"},{"title":"25-12 Delving into Ai generated content on the internet","url":"https://arxiv.org/pdf/2504.08755"},{"title":"Delving into: the quantification of Ai-generated content on ...","url":"https://www.semanticscholar.org/paper/Delving-into:-the-quantification-of-Ai-generated-on-Spennemann/f7740011daee667f954a69b73458686c173e2ea1"},{"title":"\"Delving into\" the quantification of Ai-generated content on the ...","url":"https://researchoutput.csu.edu.au/en/publications/delving-into-the-quantification-of-ai-generated-content-on-the-in/fingerprints/"},{"title":"[2511.05535] Future of AI Models: A Computational perspective on Model collapse","url":"https://arxiv.org/abs/2511.05535"},{"title":"Dirk SPENNEMANN | Professor (Level D) | Doctor of Philosophy | Charles Sturt University, Bathurst | SAEVS | Research profile","url":"https://www.researchgate.net/profile/Dirk-Spennemann"},{"title":"A Practical Synthesis of Detecting AI-Generated Textual, ...","url":"https://arxiv.org/pdf/2504.02898"},{"title":"[2504.02898] A Practical Synthesis of Detecting AI-Generated Textual, Visual, and Audio Content","url":"https://arxiv.org/abs/2504.02898"}]

I found the paper! Here's what I found about "Delving into Quantification of AI-Generated Content on the Internet" (arXiv 2504.08755):

**Author:** Dirk HR Spennemann

**Main Findings:** The findings suggest that at least 30% of text on active web pages originates from AI-generated sources, with th
…[truncated 943 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_review_ref-audit-B_20260526T104706",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 51 · 2026-05-26T10:53:59.342997+00:00_

Web search results for query: "Sun Zhang Shen "Are We in the AI-Generated Text World Already Quantifying Monitoring AIGT Social Media" ACL 2025"

Links: [{"title":"Are We in the AI-Generated Text World Already? Quantifying and Monitoring AIGT on Social Media - ACL Anthology","url":"https://aclanthology.org/2025.acl-long.1120/"},{"title":"Are We in the AI-Generated Text World Already? Quantifying and Monitoring AIGT on Social Media | Request PDF","url":"https://www.researchgate.net/publication/394299909_Are_We_in_the_AI-Generated_Text_World_Already_Quantifying_and_Monitoring_AIGT_on_Social_Media"},{"title":"[2412.18148] Are We in the AI-Generated Text World Already? Quantifying and Monitoring AIGT on Social Media","url":"https://arxiv.org/abs/2412.18148"},{"title":"arXiv:2412.18148v3 [cs.AI] 1 Jun 2025","url":"https://arxiv.org/pdf/2412.18148"},{"title":"Zhen Sun - Homepage","url":"https://zhensun.cn/"},{"title":"Are We in the AI-Generated Text World Already? Quantifying and Monitoring AIGT on Social Media","url":"https://arxiv.org/html/2412.18148v2"},{"title":"Xinyue Shen Email: xinyue.shen@cispa.de Site: https://xinyueshen.me","url":"https://xinyueshen.me/pdf/CV_of_Xinyue_Shen.pdf"}]

I found the paper you're looking for! Here are the details:

"Are We in the AI-Generated Text World Already? Quantifying and Monitoring AIGT on Social Media" was published at ACL 2025 by Zhen Sun, Zongmin Zhang, Xinyue Shen, Ziyi Zhang, Yule Liu, Michael Backes, Yang Zhang, and Xinlei He.

The paper appears in the Proceedings of the 63rd Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers), pages 22975–23005, in Vienna, Austria.

The research collects a dataset (SM-D) with around 2.4M posts from 3 major social media platforms: Medium, Quora, and Reddit, and constructs a diverse dataset (AIGTBench) to train and evaluate AIGT detectors. The paper addresses the growing presence of AI-Generated Texts (AIGTs) on social media platforms, which could have pr
…[truncated 350 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_review_ref-audit-B_20260526T104706",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 52 · 2026-05-26T10:53:59.343189+00:00_

Web search results for query: "Dohmatob Feng Subramonian Kempe "Strong Model Collapse" ICLR 2025"

Links: [{"title":"Published as a conference paper at ICLR 2025 STRONG MODEL COLLAPSE","url":"https://proceedings.iclr.cc/paper_files/paper/2025/file/284afdc2309f9667d2d4fb9290235b0c-Paper-Conference.pdf"},{"title":"Strong Model Collapse | OpenReview","url":"https://openreview.net/forum?id=et5l9qPUhm"},{"title":"[2410.04840] Strong Model Collapse","url":"https://arxiv.org/abs/2410.04840"},{"title":"ICLR Poster Strong Model Collapse","url":"https://iclr.cc/virtual/2025/poster/32070"},{"title":"Strong Model Collapse - ADS","url":"https://ui.adsabs.harvard.edu/abs/2024arXiv241004840D/abstract"},{"title":"Published as a conference paper at ICLR 2025","url":"https://openreview.net/pdf?id=MQXrTMonT1"},{"title":"Published as a conference paper at ICLR 2025","url":"https://proceedings.iclr.cc/paper_files/paper/2025/file/7416573f05b50beac6d0aef3abc805c0-Paper-Conference.pdf"},{"title":"A Closer Look at Model Collapse: From a Generalization-to-Memorization Perspective | Request PDF","url":"https://www.researchgate.net/publication/395724450_A_Closer_Look_at_Model_Collapse_From_a_Generalization-to-Memorization_Perspective"},{"title":"dblp: Elvis Dohmatob","url":"https://dblp.org/pid/134/9794.html"},{"title":"Elvis Dohmatob - Concordia University","url":"https://www.concordia.ca/faculty/elvis-dohmatob.html"}]

I found the paper! Here are the key details about the search results:

## Paper Summary

The paper is authored by Elvis Dohmatob, Yunzhen Feng, Arjun Subramonian, and Julia Kempe, with affiliations at Meta FAIR, Concordia University, Mila, NYU, and UCLA.

The paper was published as an ICLR 2025 Spotlight presentation.

## Main Findings

The paper establishes a strong form of the model collapse phenomenon—a critical performance degradation due to synthetic data in the training corpus—within the scaling laws paradigm that underpins the training of large neural networks like Chat
…[truncated 640 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_review_ref-audit-B_20260526T104706",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool call

_source line 53 · 2026-05-26T10:53:59.343369+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Wang Mansurov Ivanov \"SemEval-2024 Task 8 Multidomain Multimodel Multilingual Machine-Generated Text Detection\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_review_ref-audit-B_20260526T104706",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Wang Mansurov Ivanov \"SemEval-2024 Task 8 Multidomain Multimodel Multilingual Machine-Generated Text Detection\""
  }
}
```

</details>

---

### Tool call

_source line 54 · 2026-05-26T10:53:59.343498+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Gerstgrasser Schaeffer Dey \"Is Model Collapse Inevitable Breaking Curse Recursion Accumulating\" 2024"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_review_ref-audit-B_20260526T104706",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Gerstgrasser Schaeffer Dey \"Is Model Collapse Inevitable Breaking Curse Recursion Accumulating\" 2024"
  }
}
```

</details>

---

### Tool call

_source line 55 · 2026-05-26T10:53:59.343619+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Guo Shang Vazirgiannis \"Curious Decline of Linguistic Diversity Training Language Models Synthetic Text\" NAACL 2024"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_review_ref-audit-B_20260526T104706",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Guo Shang Vazirgiannis \"Curious Decline of Linguistic Diversity Training Language Models Synthetic Text\" NAACL 2024"
  }
}
```

</details>

---

### Tool call

_source line 56 · 2026-05-26T10:53:59.343744+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Briesch Sobania Rothlauf \"Large Language Models Suffer From Their Own Output Self-Consuming Training Loop\" arXiv 2311.16822"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_review_ref-audit-B_20260526T104706",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Briesch Sobania Rothlauf \"Large Language Models Suffer From Their Own Output Self-Consuming Training Loop\" arXiv 2311.16822"
  }
}
```

</details>

---

### Tool call

_source line 57 · 2026-05-26T10:53:59.343887+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Padmakumar He \"Does Writing with Language Models Reduce Content Diversity\" ICLR 2024"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_review_ref-audit-B_20260526T104706",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Padmakumar He \"Does Writing with Language Models Reduce Content Diversity\" ICLR 2024"
  }
}
```

</details>

---

### Tool call

_source line 58 · 2026-05-26T10:53:59.344005+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Krishna Song Karpinska \"Paraphrasing Evades Detectors AI-Generated Text Retrieval Effective Defense\" NeurIPS 2023"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_review_ref-audit-B_20260526T104706",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Krishna Song Karpinska \"Paraphrasing Evades Detectors AI-Generated Text Retrieval Effective Defense\" NeurIPS 2023"
  }
}
```

</details>

---

### Tool result

_source line 59 · 2026-05-26T10:53:59.344155+00:00_

Web search results for query: "Wang Mansurov Ivanov "SemEval-2024 Task 8 Multidomain Multimodel Multilingual Machine-Generated Text Detection""

Links: [{"title":"SemEval-2024 Task 8: Multidomain, Multimodel and Multilingual Machine-Generated Text Detection - ACL Anthology","url":"https://aclanthology.org/2024.semeval-1.279/"},{"title":"[2404.14183] SemEval-2024 Task 8: Multidomain, Multimodel and Multilingual Machine-Generated Text Detection","url":"https://arxiv.org/abs/2404.14183"},{"title":"SemEval-2024 Task 8: Multidomain, Multimodel and Multilingual Machine-Generated Text Detection","url":"https://arxiv.org/html/2404.14183v1"},{"title":"SemEval-2024 Task 8: Multidomain, Multimodel and Multilingual Machine-Generated Text Detection - NYU Scholars","url":"https://nyuscholars.nyu.edu/en/publications/semeval-2024-task-8-multidomain-multimodel-and-multilingual-machi"},{"title":"[PDF] SemEval-2024 Task 8: Multidomain, Multimodel and Multilingual Machine-Generated Text Detection | Semantic Scholar","url":"https://www.semanticscholar.org/paper/SemEval-2024-Task-8:-Multidomain,-Multimodel-and-Wang-Mansurov/c56eab12bd00e2fe28868af21d518044d66df00d"},{"title":"SemEval-2024 Task 8: Multidomain, Multimodel and Multilingual Machine-Generated Text Detection. | BibSonomy","url":"https://www.bibsonomy.org/bibtex/bfca76cf8884cdacbcb4db85e0b442bc"},{"title":"SemEval-2024 Tasks | SemEval-2024","url":"https://semeval.github.io/SemEval2024/tasks.html"},{"title":"Semeval-2024 task 8: Multigenerator, multidomain, and multilingual black-box machine-generated text detection","url":"https://airi.net/articles/semeval-2024-task-8-multigenerator-multidomain-and-multilingual-black-box-machine-generated-text-det/"}]

I found the paper you're looking for! Here are the search results:

The paper "SemEval-2024 Task 8: Multidomain, Multimodel and Multilingual Machine-Generated Text Detection" was authored by Yuxia Wang, Jonibek Mansurov, Petar Ivanov, Jinyan Su, Artem Shelmanov, Akim Tsvigun, Osa
…[truncated 1077 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_review_ref-audit-B_20260526T104706",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 60 · 2026-05-26T10:53:59.344334+00:00_

Web search results for query: "Gerstgrasser Schaeffer Dey "Is Model Collapse Inevitable Breaking Curse Recursion Accumulating" 2024"

Links: [{"title":"[2404.01413] Is Model Collapse Inevitable? Breaking the Curse of Recursion by Accumulating Real and Synthetic Data","url":"https://arxiv.org/abs/2404.01413"},{"title":"Is Model Collapse Inevitable? Breaking the Curse of Recursion by Accumulating Real and Synthetic Data | Rylan Schaeffer","url":"https://rylanschaeffer.github.io/content/research/2024_arxiv_is_model_collapse_inevitable/main.html"},{"title":"Is Model Collapse Inevitable? Breaking the Curse of Recursion by Accumulating Real and Synthetic Data | OpenReview","url":"https://openreview.net/forum?id=5B2K4LRgmz"},{"title":"Is Model Collapse Inevitable? Breaking the Curse of Recursion by Accumulating Real and Synthetic Data | Stanford SALT Lab","url":"https://saltlab.stanford.edu/papers/gerstgrasser-is-model-collapse-2024/"},{"title":"Is Model Collapse Inevitable? Breaking the Curse of Recursion by Accumulating Real and Synthetic Data","url":"https://arxiv.org/html/2404.01413v2"},{"title":"[PDF] Is Model Collapse Inevitable? Breaking the Curse of Recursion by Accumulating Real and Synthetic Data | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Is-Model-Collapse-Inevitable-Breaking-the-Curse-of-Gerstgrasser-Schaeffer/e8815da26d4e6cac8b23b7e6aa75cec028cb66d2"},{"title":"Is Model Collapse Inevitable? Breaking the Curse of Recursion by Accumulating Real and Synthetic Data | AI Research Paper Details","url":"https://www.aimodels.fyi/papers/arxiv/is-model-collapse-inevitable-breaking-curse-recursion"},{"title":"[2404.01413v1] Is Model Collapse Inevitable? Breaking the Curse of Recursion by Accumulating Real and Synthetic Data","url":"https://arxiv.org/abs/2404.01413v1"},{"title":"Is Model Collapse Inevitable? Breaking the Curse of Recursion by Accumulating Real and Synthetic Data - ADS","url":"https://ui.adsabs.harvard.edu/abs/2024arXiv240401413G/abstr
…[truncated 1615 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_review_ref-audit-B_20260526T104706",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 61 · 2026-05-26T10:53:59.344512+00:00_

Web search results for query: "Padmakumar He "Does Writing with Language Models Reduce Content Diversity" ICLR 2024"

Links: [{"title":"[2309.05196] Does Writing with Language Models Reduce Content Diversity?","url":"https://arxiv.org/abs/2309.05196"},{"title":"DOES WRITING WITH LANGUAGE MODELS REDUCE CONTENT DIVERSITY? - NYU Scholars","url":"https://nyuscholars.nyu.edu/en/publications/does-writing-with-language-models-reduce-content-diversity"},{"title":"Does Writing with Language Models Reduce Content Diversity? | AI Research Paper Details","url":"https://www.aimodels.fyi/papers/arxiv/does-writing-language-models-reduce-content-diversity"},{"title":"[PDF] Does Writing with Language Models Reduce Content Diversity? | Semantic Scholar","url":"https://www.semanticscholar.org/paper/f95fb254da1f7b74a14ac8feb3f834d64e67e4cd"},{"title":"Does Writing with Language Models Reduce Content Diversity? | NSF Public Access Repository","url":"https://par.nsf.gov/biblio/10534705-does-writing-language-models-reduce-content-diversity"},{"title":"Does Writing with Language Models Reduce Content Diversity? | Request PDF","url":"https://www.researchgate.net/publication/373837896_Does_Writing_with_Language_Models_Reduce_Content_Diversity"},{"title":"Published as a conference paper at ICLR 2025","url":"https://proceedings.iclr.cc/paper_files/paper/2025/file/ea94957d81b1c1caf87ef5319fa6b467-Paper-Conference.pdf"},{"title":"Does Writing with Language Models Reduce Content Diversity?","url":"https://arxiv.org/html/2309.05196v3"}]

I found the paper you're looking for. Here are the key details:

**Paper Title:** Does Writing with Language Models Reduce Content Diversity?

**Authors:** Vishakh Padmakumar and He He from New York University

**Conference:** 12th International Conference on Learning Representations, ICLR 2024, held in Vienna, Austria

**Summary:**
The paper examines the impact of collaborative writing with language models, noting that as different users incorporate suggestions f
…[truncated 793 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_review_ref-audit-B_20260526T104706",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 62 · 2026-05-26T10:53:59.344679+00:00_

Web search results for query: "Briesch Sobania Rothlauf "Large Language Models Suffer From Their Own Output Self-Consuming Training Loop" arXiv 2311.16822"

Links: [{"title":"[2311.16822] Large Language Models Suffer From Their Own Output: An Analysis of the Self-Consuming Training Loop","url":"https://arxiv.org/abs/2311.16822"},{"title":"Large Language Models Suffer From Their Own Output: An Analysis of the Self-Consuming Training Loop","url":"https://arxiv.org/html/2311.16822v2"},{"title":"[2311.16822v2] Large Language Models Suffer From Their Own Output: An Analysis of the Self-Consuming Training Loop","url":"https://arxiv.org/abs/2311.16822v2"},{"title":"[2311.16822] Large Language Models Suffer From Their Own Output: An Analysis of the Self-Consuming Training Loop","url":"https://ar5iv.labs.arxiv.org/html/2311.16822"},{"title":"[PDF] Large Language Models Suffer From Their Own Output: An Analysis of the Self-Consuming Training Loop | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Large-Language-Models-Suffer-From-Their-Own-Output:-Briesch-Sobania/c24ed03689adc2a075004c6619f43f7f6230fe4b"},{"title":"arXiv:2311.16822v2 [cs.LG] 17 Jun 2024","url":"https://arxiv.org/pdf/2311.16822"},{"title":"Large Language Models Suffer From Their Own Output: An Analysis of the Self-Consuming Training Loop | AI Research Paper Details","url":"https://www.aimodels.fyi/papers/arxiv/large-language-models-suffer-from-their-own"}]

I found the paper! Here's a summary of the search results:

The paper "Large Language Models Suffer From Their Own Output: An Analysis of the Self-Consuming Training Loop" by Martin Briesch, Dominik Sobania, and Franz Rothlauf investigates how self-consuming training loops produce correct outputs, but the output declines in diversity depending on the proportion of generated data used.

The research addresses the problem that LLM-generated content cannot be safely distinguished from human-produced content and is used to train the next generatio
…[truncated 584 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_review_ref-audit-B_20260526T104706",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 63 · 2026-05-26T10:53:59.344881+00:00_

Web search results for query: "Krishna Song Karpinska "Paraphrasing Evades Detectors AI-Generated Text Retrieval Effective Defense" NeurIPS 2023"

Links: [{"title":"[PDF] Paraphrasing evades detectors of AI-generated text, but retrieval is an effective defense | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Paraphrasing-evades-detectors-of-AI-generated-text,-Krishna-Song/1c13af186d1e177b85ef1ec3fc7b8d33ec314cfd"},{"title":"[2303.13408] Paraphrasing evades detectors of AI-generated text, but retrieval is an effective defense","url":"https://arxiv.org/abs/2303.13408"},{"title":"NeurIPS Poster Paraphrasing evades detectors of AI-generated text, but retrieval is an effective defense","url":"https://neurips.cc/virtual/2023/poster/71402"},{"title":"GitHub - martiansideofthemoon/ai-detection-paraphrases: Official repository for our NeurIPS 2023 paper \"Paraphrasing evades detectors of AI-generated text, but retrieval is an effective defense\" (https://arxiv.org/abs/2303.13408). · GitHub","url":"https://github.com/martiansideofthemoon/ai-detection-paraphrases"},{"title":"Paraphrasing evades detectors of AI-generated text, but ...","url":"https://openreview.net/pdf?id=WbFhFvjjKj"},{"title":"Adversarial Paraphrasing: A Universal Attack for Humanizing AI-Generated Text","url":"https://arxiv.org/pdf/2506.07001"},{"title":"Paraphrasing evades detectors of AI-generated text, but retrieval is an effective defense | Request PDF","url":"https://www.researchgate.net/publication/369477232_Paraphrasing_evades_detectors_of_AI-generated_text_but_retrieval_is_an_effective_defense"},{"title":"Paper page - Paraphrasing evades detectors of AI-generated text, but retrieval is an effective defense","url":"https://huggingface.co/papers/2303.13408"},{"title":"Paraphrasing evades detectors of AI-generated text, but retrieval is an effective defense","url":"https://papers.nips.cc/paper_files/paper/2023/hash/575c450013d0e99e4b0ecf82bd1afaa4-Abstract-Conference.html"}]

I found the 
…[truncated 1460 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_review_ref-audit-B_20260526T104706",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 64 · 2026-05-26T10:53:59.345074+00:00_

Web search results for query: "Guo Shang Vazirgiannis "Curious Decline of Linguistic Diversity Training Language Models Synthetic Text" NAACL 2024"

Links: [{"title":"The Curious Decline of Linguistic Diversity: Training Language Models on Synthetic Text - ACL Anthology","url":"https://aclanthology.org/2024.findings-naacl.228/"},{"title":"(PDF) The Curious Decline of Linguistic Diversity: Training Language Models on Synthetic Text","url":"https://www.researchgate.net/publication/382631840_The_Curious_Decline_of_Linguistic_Diversity_Training_Language_Models_on_Synthetic_Text"},{"title":"[2311.09807] The Curious Decline of Linguistic Diversity: Training Language Models on Synthetic Text","url":"https://arxiv.org/abs/2311.09807"},{"title":"The Curious Decline of Linguistic Diversity: Training Language Models on Synthetic Text - Archive ouverte HAL","url":"https://hal.science/hal-04593399"},{"title":"The Curious Decline of Linguistic Diversity: Training Language Models on Synthetic Text - Laboratoire d'informatique de l'X (LIX)","url":"https://hal.inrae.fr/X-LIX/hal-04593399v1"},{"title":"[PDF] The Curious Decline of Linguistic Diversity: Training Language Models on Synthetic Text | Semantic Scholar","url":"https://www.semanticscholar.org/paper/The-Curious-Decline-of-Linguistic-Diversity:-Models-Guo-Shang/7d5ea474aa1cf732bb1d00faa07a5bb2c9119cfd"},{"title":"@inproceedings{guo-etal-2024-curious,","url":"https://aclanthology.org/2024.findings-naacl.228.bib"},{"title":"The Curious Decline of Linguistic Diversity: Training Language Models on Synthetic Text | AI Research Paper Details","url":"https://www.aimodels.fyi/papers/arxiv/curious-decline-linguistic-diversity-training-language-models"},{"title":"The Curious Decline of Linguistic Diversity: Training Language Models on Synthetic Text","url":"https://arxiv.org/html/2311.09807v2"}]

I found the paper you're looking for. Here's the information:

**"The Curious Decline of Linguistic Diversity: Training Language Models on Sy
…[truncated 1269 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_review_ref-audit-B_20260526T104706",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool call

_source line 65 · 2026-05-26T10:53:59.345252+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Sadasivan Kumar Balasubramanian \"Can AI-Generated Text be Reliably Detected\" arXiv 2303.11156 published venue"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_review_ref-audit-B_20260526T104706",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Sadasivan Kumar Balasubramanian \"Can AI-Generated Text be Reliably Detected\" arXiv 2303.11156 published venue"
  }
}
```

</details>

---

### Tool call

_source line 66 · 2026-05-26T10:53:59.345380+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Hao Li Zhao Yang Mao \"Learning to Rewrite Generalized LLM-Generated Text Detection\" ACL 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_review_ref-audit-B_20260526T104706",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Hao Li Zhao Yang Mao \"Learning to Rewrite Generalized LLM-Generated Text Detection\" ACL 2025"
  }
}
```

</details>

---

### Tool call

_source line 67 · 2026-05-26T10:53:59.345503+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Wang Li Yan Cheng Zhang \"Unveiling Attractor Cycles Large Language Models Dynamical Systems Successive Paraphrasing\" ACL 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_review_ref-audit-B_20260526T104706",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Wang Li Yan Cheng Zhang \"Unveiling Attractor Cycles Large Language Models Dynamical Systems Successive Paraphrasing\" ACL 2025"
  }
}
```

</details>

---

### Tool call

_source line 68 · 2026-05-26T10:53:59.345622+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Fu Wang Chen Tian Tao \"Theoretical Perspective How to Prevent Model Collapse Self-consuming Training Loops\" ICLR 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_review_ref-audit-B_20260526T104706",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Fu Wang Chen Tian Tao \"Theoretical Perspective How to Prevent Model Collapse Self-consuming Training Loops\" ICLR 2025"
  }
}
```

</details>

---

### Tool call

_source line 69 · 2026-05-26T10:53:59.345824+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Verma Fleisig Tomlin Klein \"Ghostbuster Detecting Text Ghostwritten Large Language Models\" NAACL 2024"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_review_ref-audit-B_20260526T104706",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Verma Fleisig Tomlin Klein \"Ghostbuster Detecting Text Ghostwritten Large Language Models\" NAACL 2024"
  }
}
```

</details>

---

### Tool call

_source line 70 · 2026-05-26T10:53:59.345954+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Dugan Hwang Trhlik \"RAID Shared Benchmark Robust Evaluation Machine-Generated Text Detectors\" ACL 2024"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_review_ref-audit-B_20260526T104706",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Dugan Hwang Trhlik \"RAID Shared Benchmark Robust Evaluation Machine-Generated Text Detectors\" ACL 2024"
  }
}
```

</details>

---

### Tool result

_source line 71 · 2026-05-26T10:53:59.346093+00:00_

Web search results for query: "Sadasivan Kumar Balasubramanian "Can AI-Generated Text be Reliably Detected" arXiv 2303.11156 published venue"

Links: [{"title":"[2303.11156] Can AI-Generated Text be Reliably Detected?","url":"https://arxiv.org/abs/2303.11156"},{"title":"(PDF) Can AI-Generated Text be Reliably Detected?","url":"https://www.researchgate.net/publication/369380286_Can_AI-Generated_Text_be_Reliably_Detected"},{"title":"[PDF] Can AI-Generated Text be Reliably Detected? | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Can-AI-Generated-Text-be-Reliably-Detected-Sadasivan-Kumar/5ee8bb4fc80a291b2e416a2a879e7153a783d7e9"},{"title":"[2303.11156] Can AI-Generated Text be Reliably Detected?","url":"https://ar5iv.labs.arxiv.org/html/2303.11156"},{"title":"Paper page - Can AI-Generated Text be Reliably Detected?","url":"https://huggingface.co/papers/2303.11156"},{"title":"Can AI-Generated Text be Reliably Detected?","url":"https://bibbase.org/network/publication/sadasivan-kumar-balasubramanian-wang-feizi-canaigeneratedtextbereliablydetected-2023"},{"title":"[2303.11156v3] Can AI-Generated Text be Reliably Detected?","url":"https://arxiv.org/abs/2303.11156v3"}]

Based on the search results, the paper "Can AI-Generated Text be Reliably Detected?" was published on arXiv with identifier 2303.11156, authored by Vinu Sankar Sadasivan, Aounon Kumar, Sriram Balasubramanian, Wenxiao Wang, and Soheil Feizi.

The published venue is arXiv, published on March 17, 2023. This is a preprint paper that remains on arXiv as its primary venue of publication.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_review_ref-audit-B_20260526T104706",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 72 · 2026-05-26T10:53:59.346261+00:00_

Web search results for query: "Hao Li Zhao Yang Mao "Learning to Rewrite Generalized LLM-Generated Text Detection" ACL 2025"

Links: [{"title":"Learning to Rewrite: Generalized LLM-Generated Text Detection - ACL Anthology","url":"https://aclanthology.org/2025.acl-long.322/"},{"title":"Learning to Rewrite: Generalized LLM-Generated Text ...","url":"https://www.cs.columbia.edu/~junfeng/papers/learn2rewrite-acl25.pdf"},{"title":"[2408.04237] Learning to Rewrite: Generalized LLM-Generated Text Detection","url":"https://arxiv.org/abs/2408.04237"},{"title":"Accepted Main Conference Papers - ACL 2025","url":"https://2025.aclweb.org/program/main_papers/"},{"title":"Learning to Rewrite: Generalized LLM-Generated Text Detection - ADS","url":"https://ui.adsabs.harvard.edu/abs/2024arXiv240804237L/abstract"},{"title":"Evaluating Fine-Tuned LLMs for AI Text Detection | Springer Nature Link","url":"https://link.springer.com/chapter/10.1007/978-3-032-00642-4_17"},{"title":"Paper page - Learning to Rewrite: Generalized LLM-Generated Text Detection","url":"https://huggingface.co/papers/2408.04237"},{"title":"Publications - WEI HAO","url":"https://weihao97.github.io/publications/"},{"title":"(PDF) Learning to Rewrite: Generalized LLM-Generated Text Detection","url":"https://www.researchgate.net/publication/382971537_Learning_to_Rewrite_Generalized_LLM-Generated_Text_Detection"}]

I found the paper you're looking for! Here are the key details:

"Learning to Rewrite: Generalized LLM-Generated Text Detection" is by Wei Hao, Ran Li, Weiliang Zhao, Junfeng Yang, and Chengzhi Mao, published at ACL 2025.

The paper was presented at the 63rd Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers), pages 6421–6434, Vienna, Austria.

**About the Paper:**

The paper introduces Learning2Rewrite, a novel framework for detecting AI-generated text with exceptional generalization to unseen domains. The method leverages the insight that LLMs inherently modify AI-generat
…[truncated 551 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_review_ref-audit-B_20260526T104706",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 73 · 2026-05-26T10:53:59.346433+00:00_

Web search results for query: "Wang Li Yan Cheng Zhang "Unveiling Attractor Cycles Large Language Models Dynamical Systems Successive Paraphrasing" ACL 2025"

Links: [{"title":"Unveiling Attractor Cycles in Large Language Models: A Dynamical Systems View of Successive Paraphrasing - ACL Anthology","url":"https://aclanthology.org/2025.acl-long.624/"},{"title":"[2502.15208] Unveiling Attractor Cycles in Large Language Models: A Dynamical Systems View of Successive Paraphrasing","url":"https://arxiv.org/abs/2502.15208"},{"title":"Unveiling Attractor Cycles in Large Language Models: A Dynamical Systems View of Successive Paraphrasing [Quick Review]","url":"https://liner.com/review/unveiling-attractor-cycles-in-large-language-models-dynamical-systems-view"},{"title":"[2502.15208v1] Unveiling Attractor Cycles in Large Language Models: A Dynamical Systems View of Successive Paraphrasing","url":"https://arxiv.org/abs/2502.15208v1"},{"title":"Unveiling Attractor Cycles in Large Language Models: A Dynamical Systems View of Successive Paraphrasing","url":"https://arxiv.org/html/2502.15208v1"},{"title":"Unveiling Attractor Cycles in Large Language Models: A Dynamical Systems View of Successive Paraphrasing | Request PDF","url":"https://www.researchgate.net/publication/394299645_Unveiling_Attractor_Cycles_in_Large_Language_Models_A_Dynamical_Systems_View_of_Successive_Paraphrasing"},{"title":"Unveiling Attractor Cycles in Large Language Models: A Dynamical Systems View of Successive Paraphrasing | AI Research Paper Details","url":"https://www.aimodels.fyi/papers/arxiv/unveiling-attractor-cycles-large-language-models-dynamical"},{"title":"Unveiling Attractor Cycles in Large Language Models: A Dynamical","url":"https://arxiv.org/pdf/2502.15208"}]

I found the paper! Here are the search results for the paper you requested:

## Paper Information

**Unveiling Attractor Cycles in Large Language Models: A Dynamical Systems View of Successive Paraphrasing** was published at ACL 2025 by 
…[truncated 1052 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_review_ref-audit-B_20260526T104706",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 74 · 2026-05-26T10:53:59.346612+00:00_

Web search results for query: "Verma Fleisig Tomlin Klein "Ghostbuster Detecting Text Ghostwritten Large Language Models" NAACL 2024"

Links: [{"title":"Ghostbuster: Detecting Text Ghostwritten by Large Language Models - ACL Anthology","url":"https://aclanthology.org/2024.naacl-long.95/"},{"title":"Detecting Text Ghostwritten by Large Language Models","url":"https://aclanthology.org/2024.naacl-long.95.pdf"},{"title":"[2305.15047] Ghostbuster: Detecting Text Ghostwritten by Large Language Models","url":"https://arxiv.org/abs/2305.15047"},{"title":"Ghostbuster: Detecting Text Ghostwritten by Large Language Models Vivek Verma","url":"https://nlp.cs.berkeley.edu/pubs/Verma-Fleisig-Tomlin-Klein_2024_Ghostbuster_paper.pdf"},{"title":"Ghostbuster: Detecting Text Ghostwritten by Large Language Models","url":"https://arxiv.org/html/2305.15047v3"},{"title":"[PDF] Ghostbuster: Detecting Text Ghostwritten by Large Language Models | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Ghostbuster:-Detecting-Text-Ghostwritten-by-Large-Verma-Fleisig/fb467f368b9e196b32c90e3da7ae0986d59cd66f"},{"title":"Ghostbuster: Detecting Text Ghostwritten by Large Language Models | Request PDF","url":"https://www.researchgate.net/publication/382631441_Ghostbuster_Detecting_Text_Ghostwritten_by_Large_Language_Models"},{"title":"[2305.15047v1] Ghostbuster: Detecting Text Ghostwritten by Large Language Models","url":"https://arxiv.org/abs/2305.15047v1"},{"title":"Ghostbuster: Detecting Text Ghostwritten by Large Language Models | AI Research Paper Details","url":"https://www.aimodels.fyi/papers/arxiv/ghostbuster-detecting-text-ghostwritten-by-large-language"},{"title":"Ghostbuster: Detecting Text Ghostwritten by Large Language Models - ADS","url":"https://ui.adsabs.harvard.edu/abs/2023arXiv230515047V/abstract"}]

I found the paper! Here are the results:

**Paper Information:**

The paper is "Ghostbuster: Detecting Text Ghostwritten by Large Language Models" by Vivek Verma, Eve Fleisig, N
…[truncated 1297 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_review_ref-audit-B_20260526T104706",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 75 · 2026-05-26T10:53:59.346799+00:00_

Web search results for query: "Fu Wang Chen Tian Tao "Theoretical Perspective How to Prevent Model Collapse Self-consuming Training Loops" ICLR 2025"

Links: [{"title":"A Theoretical Perspective: How to Prevent Model Collapse in Self-consuming Training Loops | OpenReview","url":"https://openreview.net/forum?id=WttfQGwpES"},{"title":"[2502.18865] A Theoretical Perspective: How to Prevent Model Collapse in Self-consuming Training Loops","url":"https://arxiv.org/abs/2502.18865"},{"title":"A Theoretical Perspective: How to Prevent Model Collapse in Self-consuming Training Loops","url":"https://arxiv.org/html/2502.18865"},{"title":"Self-Consuming AI Resources","url":"https://dsp.rice.edu/ai-loops/"},{"title":"dblp: Xinmei Tian 0001","url":"https://dblp.org/pid/03/5204-1.html"},{"title":"HOW TO PREVENT MODEL COLLAPSE IN SELF- ...","url":"https://openreview.net/pdf?id=WttfQGwpES"},{"title":"Towards Theoretical Understandings of Self-Consuming Generative Models","url":"https://arxiv.org/html/2402.11778v2"},{"title":"International Conference on Learning Representations 2025","url":"https://proceedings.iclr.cc/paper_files/paper/2025"}]

I found the paper! Here are the search results for your query:

The paper "A Theoretical Perspective: How to Prevent Model Collapse in Self-consuming Training Loops" is by Shi Fu, Yingjie Wang, Yuzhu Chen, Xinmei Tian, and Dacheng Tao, and it has been accepted to ICLR 2025.

The paper addresses Self-consuming Training Loops (STLs), where models increasingly generate their own data for further training, and introduces the concept of recursive stability with the first theoretical generalization analysis, revealing how both model architecture and the proportion between real and synthetic data influence the success of STLs.

The analysis extends to transformers in in-context learning, showing that even a constant-sized proportion of real data ensures convergence, while also providing insights into optimal synthetic data sizing.

The paper is avail
…[truncated 186 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_review_ref-audit-B_20260526T104706",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 76 · 2026-05-26T10:53:59.346985+00:00_

Web search results for query: "Dugan Hwang Trhlik "RAID Shared Benchmark Robust Evaluation Machine-Generated Text Detectors" ACL 2024"

Links: [{"title":"RAID: A Shared Benchmark for Robust Evaluation of Machine-Generated Text Detectors - ACL Anthology","url":"https://aclanthology.org/2024.acl-long.674/"},{"title":"[2405.07940] RAID: A Shared Benchmark for Robust Evaluation of Machine-Generated Text Detectors","url":"https://arxiv.org/abs/2405.07940"},{"title":"RAID: A Shared Benchmark for Robust Evaluation of Machine-Generated Text Detectors | Request PDF","url":"https://www.researchgate.net/publication/384214327_RAID_A_Shared_Benchmark_for_Robust_Evaluation_of_Machine-Generated_Text_Detectors"},{"title":"GitHub - liamdugan/raid: RAID is the largest and most challenging benchmark for AI-generated text detection. (ACL 2024) · GitHub","url":"https://github.com/liamdugan/raid"},{"title":"RAID: A Shared Benchmark for Robust Evaluation of Machine-Generated Text Detectors","url":"https://arxiv.org/html/2405.07940v1"},{"title":"RAID: A Shared Benchmark for Robust Evaluation of Machine-Generated Text Detectors (Conference Paper) | NSF PAGES","url":"https://par.nsf.gov/biblio/10563509-raid-shared-benchmark-robust-evaluation-machine-generated-text-detectors"},{"title":"[PDF] RAID: A Shared Benchmark for Robust Evaluation of Machine-Generated Text Detectors | Semantic Scholar","url":"https://www.semanticscholar.org/paper/RAID:-A-Shared-Benchmark-for-Robust-Evaluation-of-Dugan-Hwang/a28474db72957c239127374cfee3c8ed8190defc"}]

I found the paper! Here's what the search revealed:

RAID: A Shared Benchmark for Robust Evaluation of Machine-Generated Text Detectors is authored by Liam Dugan, Alyssa Hwang, Filip Trhlík, Andrew Zhu, Josh Magnus Ludan, Hainiu Xu, Daphne Ippolito, and Chris Callison-Burch, and was published at ACL 2024.

RAID is the largest and most challenging benchmark dataset for machine-generated text detection, including over 6 million generations spanning 11 mode
…[truncated 774 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_review_ref-audit-B_20260526T104706",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool call

_source line 77 · 2026-05-26T10:53:59.347167+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Liang Yuksekgonul Mao Wu Zou \"GPT detectors are biased against non-native English writers\" Patterns 2023"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_review_ref-audit-B_20260526T104706",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Liang Yuksekgonul Mao Wu Zou \"GPT detectors are biased against non-native English writers\" Patterns 2023"
  }
}
```

</details>

---

### Tool call

_source line 78 · 2026-05-26T10:53:59.347299+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Gerstgrasser \"Is Model Collapse Inevitable\" COLM 2024 conference venue"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_review_ref-audit-B_20260526T104706",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Gerstgrasser \"Is Model Collapse Inevitable\" COLM 2024 conference venue"
  }
}
```

</details>

---

### Tool call

_source line 79 · 2026-05-26T10:53:59.347422+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Kazdan Schaeffer \"Collapse or Thrive\" ICML 2025 accepted conference paper"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_review_ref-audit-B_20260526T104706",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Kazdan Schaeffer \"Collapse or Thrive\" ICML 2025 accepted conference paper"
  }
}
```

</details>

---

### Tool call

_source line 80 · 2026-05-26T10:53:59.347541+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Schaeffer Kazdan \"Position Model Collapse Does Not Mean What You Think\" ICML 2025 accepted"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_review_ref-audit-B_20260526T104706",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Schaeffer Kazdan \"Position Model Collapse Does Not Mean What You Think\" ICML 2025 accepted"
  }
}
```

</details>

---

### Tool call

_source line 81 · 2026-05-26T10:53:59.347662+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Guo Shang Vazirgiannis Clavel \"Curious Decline Linguistic Diversity\" author Chloé Chloe"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_review_ref-audit-B_20260526T104706",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Guo Shang Vazirgiannis Clavel \"Curious Decline Linguistic Diversity\" author Chloé Chloe"
  }
}
```

</details>

---

### Tool result

_source line 82 · 2026-05-26T10:53:59.347823+00:00_

Web search results for query: "Liang Yuksekgonul Mao Wu Zou "GPT detectors are biased against non-native English writers" Patterns 2023"

Links: [{"title":"[2304.02819] GPT detectors are biased against non-native English writers","url":"https://arxiv.org/abs/2304.02819"},{"title":"GPT detectors are biased against non-native English writers: Patterns","url":"https://www.cell.com/patterns/fulltext/S2666-3899(23)00130-7"},{"title":"GPT detectors can be biased against non-native English writers | ScienceDaily","url":"https://www.sciencedaily.com/releases/2023/07/230710113921.htm"},{"title":"GPT detectors are biased against non-native English writers","url":"https://arxiv.org/pdf/2304.02819"},{"title":"Liang, W. X. et al. (2023). GPT Detectors Are Biased against Non-Native English Writers. Patterns, 4, Article ID 100779. - References - Scientific Research Publishing","url":"https://www.scirp.org/reference/referencespapers?referenceid=3900453"},{"title":"(PDF) GPT detectors are biased against non-native English writers","url":"https://www.researchgate.net/publication/372269006_GPT_detectors_are_biased_against_non-native_English_writers"},{"title":"GPT DETECTORS ARE BIASED AGAINST NON-NATIVE ...","url":"https://openreview.net/pdf?id=SPuX8tKKIQ"},{"title":"[2304.02819v2] GPT detectors are biased against non-native English writers","url":"https://arxiv.org/abs/2304.02819v2"},{"title":"GPT detectors are biased against non-native English writers","url":"https://km4s.ca/wp-content/uploads/GPT-detectors-are-biased-against-non-native-English-writers-2023.pdf"}]

I found the research paper you were looking for! Here are the key details:

**Paper Title:** "GPT detectors are biased against non-native English writers"

**Authors:** Weixin Liang, Mert Yuksekgonul, Yining Mao, Eric Wu, and James Zou

**Publication:** Published in Patterns, 2023, with DOI: 10.1016/j.patter.2023.100779

**Key Findings:** 
- The detectors consistently misclassify non-native English writing samples as AI-g
…[truncated 697 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_review_ref-audit-B_20260526T104706",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 83 · 2026-05-26T10:53:59.348006+00:00_

Web search results for query: "Kazdan Schaeffer "Collapse or Thrive" ICML 2025 accepted conference paper"

Links: [{"title":"ICML Poster Collapse or Thrive: Perils and Promises of Synthetic Data in a Self-Generating World","url":"https://icml.cc/virtual/2025/poster/44713"},{"title":"[2410.16713] Collapse or Thrive? Perils and Promises of Synthetic Data in a Self-Generating World","url":"https://arxiv.org/abs/2410.16713"},{"title":"Collapse or Thrive: Perils and Promises of Synthetic Data in a Self-Generating World","url":"https://proceedings.mlr.press/v267/kazdan25a.html"},{"title":"1 Introduction","url":"https://arxiv.org/html/2410.16713"},{"title":"Position: Machine Learning Conferences Should Establish ...","url":"https://openreview.net/pdf?id=DS1XSAPvKs"},{"title":"Collapse or Thrive?Perils and Promises of Synthetic Data ...","url":"https://arxiv.org/pdf/2410.16713"},{"title":"Collapse or Thrive: Perils and Promises of Synthetic Data in a Self-Generating World | OpenReview","url":"https://openreview.net/forum?id=buwLCdOHxO&noteId=536VRf5UKe"},{"title":"[PDF] The Curse of Recursion: Training on Generated Data Makes Models Forget | Semantic Scholar","url":"https://www.semanticscholar.org/paper/The-Curse-of-Recursion:-Training-on-Generated-Data-Shumailov-Shumaylov/155aec5cff650263a4c71136f97570611d1bba7a"},{"title":"Escaping Model Collapse via Synthetic Data Verification: Near-term Improvements and Long-term ConvergenceThis project is supported by the AI2050 program at Schmidt Sciences (Grant G-24-66104) and Army Research Office Award W911NF-23-1-0030. We also thank Cong Ma from UChicago, Hongning Wang and Bo Li from Tsinghua, Pinyan Lu and Gavin Tang from Shanghai University of Finance and Economics for helpful discussions and suggestions.","url":"https://arxiv.org/html/2510.16657v1"},{"title":"(PDF) Collapse or Thrive? Perils and Promises of Synthetic Data in a Self-Generating World","url":"https://www.researchgate.net/publication/385140496_Collapse_or_Thrive_Per
…[truncated 1104 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_review_ref-audit-B_20260526T104706",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 84 · 2026-05-26T10:53:59.348186+00:00_

Web search results for query: "Guo Shang Vazirgiannis Clavel "Curious Decline Linguistic Diversity" author Chloé Chloe"

Links: [{"title":"The Curious Decline of Linguistic Diversity: Training Language Models on Synthetic Text - ACL Anthology","url":"https://aclanthology.org/2024.findings-naacl.228/"},{"title":"[PDF] The Curious Decline of Linguistic Diversity: Training Language Models on Synthetic Text | Semantic Scholar","url":"https://www.semanticscholar.org/paper/The-Curious-Decline-of-Linguistic-Diversity:-Models-Guo-Shang/7d5ea474aa1cf732bb1d00faa07a5bb2c9119cfd"},{"title":"[2311.09807] The Curious Decline of Linguistic Diversity: Training Language Models on Synthetic Text","url":"https://arxiv.org/abs/2311.09807"},{"title":"The Curious Decline of Linguistic Diversity: Training Language Models on Synthetic Text - Archive ouverte HAL","url":"https://hal.science/hal-04593399"},{"title":"The Curious Decline of Linguistic Diversity: Training Language Models on Synthetic Text","url":"https://arxiv.org/html/2311.09807v2"},{"title":"The Curious Decline of Linguistic Diversity: Training Language Models on Synthetic Text - ADS","url":"https://ui.adsabs.harvard.edu/abs/2023arXiv231109807G/abstract"},{"title":"The Curious Decline of Linguistic Diversity: Training Language Models on Synthetic Text - Laboratoire d'informatique de l'X (LIX)","url":"https://hal.inrae.fr/X-LIX/hal-04593399v1"},{"title":"The Curious Decline of Linguistic Diversity: Training Language Models on Synthetic Text | AI Research Paper Details","url":"https://www.aimodels.fyi/papers/arxiv/curious-decline-linguistic-diversity-training-language-models"},{"title":"The Curious Decline of Linguistic Diversity: Training Language Models on Synthetic Text","url":"https://www.catalyzex.com/paper/the-curious-decline-of-linguistic-diversity"},{"title":"(PDF) The Curious Decline of Linguistic Diversity: Training Language Models on Synthetic Text","url":"https://www.researchgate.net/publication/382631840_The_Curiou
…[truncated 1079 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_review_ref-audit-B_20260526T104706",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 85 · 2026-05-26T10:53:59.348370+00:00_

Web search results for query: "Gerstgrasser "Is Model Collapse Inevitable" COLM 2024 conference venue"

Links: [{"title":"Is Model Collapse Inevitable? Breaking the Curse of Recursion by Accumulating Real and Synthetic Data | Rylan Schaeffer","url":"https://rylanschaeffer.github.io/content/research/2024_arxiv_is_model_collapse_inevitable/main.html"},{"title":"[2404.01413] Is Model Collapse Inevitable? Breaking the Curse of Recursion by Accumulating Real and Synthetic Data","url":"https://arxiv.org/abs/2404.01413"},{"title":"[PDF] Is Model Collapse Inevitable? Breaking the Curse of Recursion by Accumulating Real and Synthetic Data | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Is-Model-Collapse-Inevitable-Breaking-the-Curse-of-Gerstgrasser-Schaeffer/e8815da26d4e6cac8b23b7e6aa75cec028cb66d2"},{"title":"Is Model Collapse Inevitable? Breaking the Curse of Recursion by Accumulating Real and Synthetic Data | OpenReview","url":"https://openreview.net/forum?id=5B2K4LRgmz"},{"title":"[2404.01413v1] Is Model Collapse Inevitable? Breaking the Curse of Recursion by Accumulating Real and Synthetic Data","url":"https://arxiv.org/abs/2404.01413v1"},{"title":"Is Model Collapse Inevitable? Breaking the Curse of Recursion by Accumulating Real and Synthetic Data | Stanford SALT Lab","url":"https://saltlab.stanford.edu/papers/gerstgrasser-is-model-collapse-2024/"},{"title":"Addressing Concerns of Model Collapse from Synthetic Data in AI","url":"https://www.gretel.ai/blog/addressing-concerns-of-model-collapse-from-synthetic-data-in-ai"},{"title":"Position: Model Collapse Does Not Mean What You Think Anonymous Author(s)","url":"https://openreview.net/pdf?id=ygfzWIGDN8"}]

Based on the search results, I found information about the Gerstgrasser paper "Is Model Collapse Inevitable," but the results indicate the venue listed is Arxiv 2024, not specifically a COLM 2024 conference venue. However, the paper does appear on OpenReview with a reference to the COLM Code of Ethics 
…[truncated 1987 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_review_ref-audit-B_20260526T104706",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 86 · 2026-05-26T10:53:59.348553+00:00_

Web search results for query: "Schaeffer Kazdan "Position Model Collapse Does Not Mean What You Think" ICML 2025 accepted"

Links: [{"title":"[2503.03150] Position: Model Collapse Does Not Mean What You Think","url":"https://arxiv.org/abs/2503.03150"},{"title":"Position: Model Collapse Does Not Mean What You Think","url":"https://arxiv.org/pdf/2503.03150"},{"title":"Position: Model Collapse Does Not Mean What You Think - ADS","url":"https://ui.adsabs.harvard.edu/abs/2025arXiv250303150S/abstract"},{"title":"Position: Model Collapse Does Not Mean What You Think Anonymous Author(s)","url":"https://openreview.net/pdf?id=ygfzWIGDN8"},{"title":"[Literature Review] Position: Model Collapse Does Not Mean What You Think","url":"https://www.themoonlight.io/en/review/position-model-collapse-does-not-mean-what-you-think"},{"title":"Position: Model Collapse Does Not Mean What You Think | OpenReview","url":"https://openreview.net/forum?id=ygfzWIGDN8"},{"title":"Escaping Collapse: The Strength of Weak Data for Large Language Model TrainingAuthors ordered alphabetically. Author contributions are listed at the end.","url":"https://arxiv.org/html/2502.08924v2"},{"title":"Model collapse occurs under some definitions, but does not occur under... | Download Scientific Diagram","url":"https://www.researchgate.net/figure/Model-collapse-occurs-under-some-definitions-but-does-not-occur-under-others-for-the_tbl1_389617145"},{"title":"LLM Web Dynamics: Tracing Model Collapse in a Network of LLMs","url":"https://arxiv.org/html/2506.15690v1"}]

Based on the search results, I found information about this paper. However, I should note that the paper appears to be submitted to NeurIPS 2025, not ICML 2025.

The paper "Position: Model Collapse Does Not Mean What You Think" was submitted on March 5, 2025 (with a revised version on March 18, 2025) by authors Rylan Schaeffer, Joshua Kazdan, Alvan Caleb Arulandu, and Sanmi Koyejo. 

The paper was submitted to NeurIPS 2025 as a Position Paper Track submi
…[truncated 753 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_review_ref-audit-B_20260526T104706",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool call

_source line 87 · 2026-05-26T10:53:59.348735+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "site:openreview.net \"Is Model Collapse Inevitable\" Gerstgrasser COLM 2024 accepted"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_review_ref-audit-B_20260526T104706",
  "tool": "WebSearch",
  "tool_args": {
    "query": "site:openreview.net \"Is Model Collapse Inevitable\" Gerstgrasser COLM 2024 accepted"
  }
}
```

</details>

---

### Tool call

_source line 88 · 2026-05-26T10:53:59.348888+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"Collapse or Thrive\" Kazdan title ICML 2025 \"Perils and Promises\" exact title question mark"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_review_ref-audit-B_20260526T104706",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"Collapse or Thrive\" Kazdan title ICML 2025 \"Perils and Promises\" exact title question mark"
  }
}
```

</details>

---

### Tool result

_source line 89 · 2026-05-26T10:53:59.349038+00:00_

Web search results for query: ""Collapse or Thrive" Kazdan title ICML 2025 "Perils and Promises" exact title question mark"

Links: [{"title":"ICML Poster Collapse or Thrive: Perils and Promises of Synthetic Data in a Self-Generating World","url":"https://icml.cc/virtual/2025/poster/44713"},{"title":"[2410.16713] Collapse or Thrive? Perils and Promises of Synthetic Data in a Self-Generating World","url":"https://arxiv.org/abs/2410.16713"},{"title":"1 Introduction","url":"https://arxiv.org/html/2410.16713"},{"title":"Collapse or Thrive?Perils and Promises of Synthetic Data ...","url":"https://arxiv.org/pdf/2410.16713"},{"title":"COLLAPSE OR THRIVE? PERILS AND PROMISES OF ...","url":"https://openreview.net/pdf/4315166693bd1ac3b3fe3a8307a83520a31c5441.pdf"},{"title":"Collapse or Thrive? Perils and Promises of Synthetic Data in a Self-Generating World | OpenReview","url":"https://openreview.net/forum?id=Xr5iINA3zU"},{"title":"Collapse or Thrive? Perils and Promises of Synthetic Data in a Self-Generating World","url":"https://arxiv.org/html/2410.16713v2"},{"title":"(PDF) Collapse or Thrive? Perils and Promises of Synthetic Data in a Self-Generating World","url":"https://www.researchgate.net/publication/385140496_Collapse_or_Thrive_Perils_and_Promises_of_Synthetic_Data_in_a_Self-Generating_World"},{"title":"Downloads 2025","url":"https://icml.cc/Downloads/2025"},{"title":"Humanity in the Age of AI: Reassessing 2025's Existential-Risk Narratives","url":"https://arxiv.org/pdf/2512.04119"}]

I found the paper you're looking for! 

The paper is titled "Collapse or Thrive? Perils and Promises of Synthetic Data in a Self-Generating World" by Joshua Kazdan and co-authors, and was presented at ICML 2025. 

The paper addresses the question: "What happens when generative machine learning models are pretrained on web-scale datasets containing data generated by earlier models?" The authors report experiments on three ways of using data across three generative model task-settings (mul
…[truncated 249 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_review_ref-audit-B_20260526T104706",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 90 · 2026-05-26T10:53:59.349205+00:00_

Web search results for query: "site:openreview.net "Is Model Collapse Inevitable" Gerstgrasser COLM 2024 accepted"

Links: [{"title":"Is Model Collapse Inevitable? Breaking the Curse of Recursion by Accumulating Real and Synthetic Data | OpenReview","url":"https://openreview.net/forum?id=5B2K4LRgmz"},{"title":"Is Model Collapse Inevitable? Breaking the Curse of Recursion by","url":"https://openreview.net/pdf/264715d321dd6b63cbc356483cbb650791eb374b.pdf"},{"title":"Position: Model Collapse Does Not Mean What You Think Anonymous Author(s)","url":"https://openreview.net/pdf?id=ygfzWIGDN8"},{"title":"HOW TO PREVENT MODEL COLLAPSE IN SELF- ...","url":"https://openreview.net/pdf?id=WttfQGwpES"},{"title":"[2404.01413] Is Model Collapse Inevitable? Breaking the Curse of Recursion by Accumulating Real and Synthetic Data","url":"https://arxiv.org/abs/2404.01413"},{"title":"Is Model Collapse Inevitable? Breaking the Curse of Recursion ...","url":"https://openreview.net/pdf/c24f30d84a2a8e887926826f0051dc4b6c0e3760.pdf"},{"title":"A Closer Look at Model Collapse: From a Generalization-to ...","url":"https://openreview.net/pdf?id=vvwpY99gXj"},{"title":"COLM 2024: Accepted Papers","url":"http://2024.colmweb.org/AcceptedPapers.html"}]

I found the paper you're looking for! "Is Model Collapse Inevitable? Breaking the Curse of Recursion by Accumulating Real and Synthetic Data" by Matthias Gerstgrasser and colleagues is listed among the accepted papers for COLM 2024.

The paper is available on OpenReview at: https://openreview.net/forum?id=5B2K4LRgmz

The paper investigates what effect accumulating data has on model collapse, and demonstrates that accumulating synthetic data with real data avoids model collapse.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_review_ref-audit-B_20260526T104706",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 91 · 2026-05-26T10:53:59.349396+00:00_

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
  "session": "worker_review_ref-audit-B_20260526T104706",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/introduction.tex"
  }
}
```

</details>

---

### Tool result

_source line 92 · 2026-05-26T10:53:59.349552+00:00_

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
  "session": "worker_review_ref-audit-B_20260526T104706",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 93 · 2026-05-26T10:53:59.349715+00:00_

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
  "session": "worker_review_ref-audit-B_20260526T104706",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/related_work.tex"
  }
}
```

</details>

---

### Tool result

_source line 94 · 2026-05-26T10:53:59.349884+00:00_

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
  "session": "worker_review_ref-audit-B_20260526T104706",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 95 · 2026-05-26T10:53:59.350041+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/experiments_c1.tex",
  "offset": "185",
  "limit": "5"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_review_ref-audit-B_20260526T104706",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/experiments_c1.tex",
    "offset": "185",
    "limit": "5"
  }
}
```

</details>

---

### Tool result

_source line 96 · 2026-05-26T10:53:59.350169+00:00_

185	\label{sec:binary_confidence}
186	
187	Binary detectors (DivEye~\cite{basani2026diveye}, Binoculars~\cite{hans2024binoculars}) provide no depth signal beyond the human-vs.-machine boundary: $\Kempirical^{\text{binary}} \leq 1$, with moderate rank correlations ($|\rho| = 0.06$--$0.46$) driven entirely by the 0v1 gap (Table~\ref{tab:s9_binary_spearman}).
188	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_review_ref-audit-B_20260526T104706",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 97 · 2026-05-26T10:53:59.350294+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/experiments_c3.tex",
  "offset": "1",
  "limit": "10"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_review_ref-audit-B_20260526T104706",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/experiments_c3.tex",
    "offset": "1",
    "limit": "10"
  }
}
```

</details>

---

### Tool result

_source line 98 · 2026-05-26T10:53:59.350425+00:00_

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

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_review_ref-audit-B_20260526T104706",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 99 · 2026-05-26T10:53:59.350551+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/discussion.tex",
  "offset": "10",
  "limit": "6"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_review_ref-audit-B_20260526T104706",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/discussion.tex",
    "offset": "10",
    "limit": "6"
  }
}
```

</details>

---

### Tool result

_source line 100 · 2026-05-26T10:53:59.350675+00:00_

10	\paragraph{One-wash laundering (web text).}
11	For general web text, $\Kempirical{=}2$ reflects concentrated information loss: 0v1 is near-trivially separable ($\auc \geq 0.92$), 1v2 drops by ${\sim}$30\,pp, and 2v3 falls below $\theta$.
12	OBD achieves 94\% depth-0 recall but only 15--23\% for depths $\geq$2; frontier LLMs show 8--38\% ($p > 0.05$ vs.\ OBD; Table~\ref{tab:s3_llm_zeroshot}; per-depth breakdown in Table~\ref{tab:s3c_perdepth}), which supports a data-intrinsic interpretation.
13	Unlike model collapse~\cite{shumailov2024collapse}, one-wash laundering describes erasure of statistical fingerprints; quality may degrade further after features become indistinguishable.
14	
15	\begin{figure}[t]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_review_ref-audit-B_20260526T104706",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 101 · 2026-05-26T10:53:59.350818+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/appendix_extended.tex",
  "offset": "1",
  "limit": "10"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_review_ref-audit-B_20260526T104706",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/appendix_extended.tex",
    "offset": "1",
    "limit": "10"
  }
}
```

</details>

---

### Tool result

_source line 102 · 2026-05-26T10:53:59.350949+00:00_

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

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_review_ref-audit-B_20260526T104706",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 103 · 2026-05-26T10:53:59.351087+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/appendix_extended.tex",
  "offset": "60",
  "limit": "10"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_review_ref-audit-B_20260526T104706",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/appendix_extended.tex",
    "offset": "60",
    "limit": "10"
  }
}
```

</details>

---

### Tool result

_source line 104 · 2026-05-26T10:53:59.351215+00:00_

60	Per-depth recall confirms convergent failure at depths $\geq 2$ (Section~\ref{sec:why_kstar}).
61	The LLM baseline evaluates depths 0--4 (5-class; Table~\ref{tab:s3_llm_zeroshot}). When probabilities are marginalized to 4 classes ($P(d{\geq}3)$), accuracy rises to 44.4\% but concentrates in the merged class while depths 2--3 collapse to 2--8\%.
62	
63	\subsection{Practical Considerations}
64	
65	All filtering strategies degrade general capabilities (MMLU: 0.6018 $\to$ 0.5865--0.5941; HellaSwag: 0.6821 $\to$ 0.6631--0.6701); our depth-chain setting (${\sim}$83\% synthetic) is an upper bound; in mixed corpora, degradation scales with contamination fraction~\cite{shumailov2024collapse, dohmatob2024model}.
66	$\Kstar$-aware binary filtering reduces MMLU degradation by ${\sim}$50\% ($-$1.53\,pp $\to$ $-$0.77\,pp), requires no per-model calibration, and is combinable with distribution-matching methods (DSIR, DoReMi).
67	
68	\subsection{Additional Scope Analysis}
69	\label{sec:extended_limitations}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_review_ref-audit-B_20260526T104706",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 105 · 2026-05-26T10:53:59.351424+00:00_

called Write

<details open><summary>🔧 Tool call — Write</summary>

````json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/artifacts/ref_audit_worker_B.md",
  "content": "# Reference Audit — Worker B\n\nAudited: `references.bib` (37 entries)\nDate: 2026-05-26\n\n## Per-Entry Verification\n\n```\n[kirchenbauer2023watermark] ✓ | Real paper. ICML 2023, PMLR, pages 17061–17084. Authors, title, venue all correct.\n\n[drayson2025] ✓ | Real paper. EMNLP 2025. Title, authors (Drayson, Yilmaz, Lampos) correct. arXiv:2502.15654 confirmed.\n\n[schaeffer2025position] ✓ | Real paper. arXiv preprint 2503.03150, March 2025. Authors (Schaeffer, Kazdan, Arulandu, Koyejo) correct. Currently under review (NeurIPS 2025 OpenReview); bib correctly lists as @article/arXiv.\n\n[kazdan2025collapse] ✓ | Real paper. Confirmed ICML 2025 (PMLR proceedings + ICML poster page). Authors correct. Note: ICML proceedings title drops \"?\" → \"Collapse or Thrive: Perils and Promises…\" (colon, not question mark), but arXiv original has \"?\". Cosmetic, not an error.\n\n[mitchell2023detectgpt] ✓ | Real paper. ICML 2023. Authors (Mitchell, Lee, Khazatsky, Manning, Finn) correct.\n\n[basani2026diveye] ✓ | Real paper. TMLR 2026 confirmed (GitHub: [TMLR '26], OpenReview). Authors (Basani, Chen) correct. ISSN 2835-8856 correct.\n\n[zawalski2026codec] ✓ | Real paper. ICLR 2026 confirmed (OpenReview, LinkedIn announcement). Authors (Zawalski, Boubdir, Bałazy, Nushi, Ribalta) correct.\n\n[zhang2024minkpp] ✓ | Real paper. ICLR 2025 Spotlight. Year field = 2025, correct. (Cite key says \"2024\" — cosmetic, no effect on output.) Authors correct.\n\n[shumailov2024collapse] ✓ | Real paper. Nature 2024, vol 631, pages 755–759. Authors correct (Nature itself lists \"Ross Anderson\" without middle initial, matching bib). Title, DOI correct.\n\n[alemohammad2024selfconsuming] ✓ | Real paper. ICLR 2024. Authors (Alemohammad, Casco-Rodriguez, Luzi, Humayun, Babaei, LeJeune, Siahkoohi, Baraniuk) correct.\n\n[dohmatob2024model] ✓ | Real paper. ICML 2024 (PMLR v235). Authors (Dohmatob, Feng, Yang, Charton, Kempe) correct.\n\n[xie2023dsir] ✓ | Real paper. NeurIPS 2023. Authors (Xie, Santurkar, Ma, Liang) correct.\n\n[tirumala2023d4] ✓ | Real paper. NeurIPS 2023 (Datasets & Benchmarks track). Authors (Tirumala, Simig, Aghajanyan, Morcos) correct.\n\n[xie2023doremi] ✓ | Real paper. NeurIPS 2023. Authors (Xie, Pham, Dong, Du, Liu, Lu, Liang, Le, Ma, Yu) correct.\n\n[hans2024binoculars] ✓ | Real paper. ICML 2024 (PMLR v235). Authors (Hans, Schwarzschild, Cherepanova, Kazemi, Saha, Goldblum, Geiping, Goldstein) correct.\n\n[alain2017understanding] ✓ | Real paper. ICLR 2017 Workshop track. Authors (Alain, Bengio) correct.\n\n[belinkov2022probing] ✓ | Real paper. Computational Linguistics, vol 48, no 1, pages 207–219, 2022. All metadata correct.\n\n[bao2024fast] ✓ | Real paper. ICLR 2024. Authors (Bao, Zhao, Teng, Yang, Zhang) correct.\n\n[frank2001ordinal] ✓ | Real paper. ECML 2001 (LNCS 2167), pages 145–156. Authors (Frank, Hall) correct. DOI 10.1007/3-540-44795-4_13 correct.\n\n[cheng2025beyond] ✓ | Real paper. WWW 2025 (ACM Web Conference). Authors (Cheng, Zhou, Jiang, Wang, Li) correct.\n\n[mehta2025beyond] ✓ | Real paper. arXiv 2511.17602, November 2025. Author (Mehta) correct. Bib correctly lists as @article/arXiv.\n\n[sun2025aigt] ✓ | Real paper. ACL 2025 (ACL Anthology 2025.acl-long.1120). Authors (Sun, Zhang, Shen, Zhang, Liu, Backes, Zhang, He) correct.\n\n[spennemann2025quantifying] ✓ | Real paper. arXiv 2504.08755, April 2025. Author (Spennemann) correct. Note: original arXiv title uses odd \"Ai\" capitalization; bib normalizes to {AI} which is correct.\n\n[dohmatob2025strong] ✓ | Real paper. ICLR 2025 Spotlight. Authors (Dohmatob, Feng, Subramonian, Kempe) correct.\n\n[wang2024semeval] ✓ | Real paper. SemEval-2024 (co-located with NAACL 2024). Authors correct (large author list verified against ACL Anthology).\n\n[gerstgrasser2024model] ✓ | Real paper. COLM 2024 confirmed (OpenReview, COLM accepted papers list). Authors correct.\n\n[guo2024curious] ✗ | Author name spelling: bib has \"Clavel, Chloe\" but correct name is \"Chloé Clavel\" (accent é). Should be \"Clavel, Chlo\\'{e}\". Everything else (title, Findings of NAACL 2024, other authors) correct.\n\n[briesch2023selfconsuming] ✓ | Real paper. arXiv 2311.16822, November 2023 (v2 June 2024). Still preprint; bib correctly lists as @article/arXiv. Authors (Briesch, Sobania, Rothlauf) correct.\n\n[padmakumar2024writing] ✓ | Real paper. ICLR 2024. Authors (Padmakumar, He) correct.\n\n[krishna2023paraphrasing] ✓ | Real paper. NeurIPS 2023. Authors (Krishna, Song, Karpinska, Wieting, Iyyer) correct.\n\n[sadasivan2023detect] ✓ | Real paper. arXiv 2303.11156, March 2023. Still preprint; bib correctly lists as @article/arXiv. Authors correct.\n\n[hao2025rewrite] ✓ | Real paper. ACL 2025 (ACL Anthology 2025.acl-long.322). Authors (Hao, Li, Zhao, Yang, Mao) correct.\n\n[wang2025unveiling] ✓ | Real paper. ACL 2025 (ACL Anthology 2025.acl-long.624), pages 12740–12755. Authors (Wang, Li, Yan, Cheng, Zhang) correct.\n\n[fu2025theoretical] ✓ | Real paper. ICLR 2025 (OpenReview). Authors (Fu, Wang, Chen, Tian, Tao) correct.\n\n[verma2024ghostbuster] ✓ | Real paper. NAACL 2024, pages 1702–1717. Authors (Verma, Fleisig, Tomlin, Klein) correct.\n\n[dugan2024raid] ✓ | Real paper. ACL 2024, pages 12463–12492. Authors (Dugan, Hwang, Trhlík, Zhu, Ludan, Xu, Ippolito, Callison-Burch) correct.\n\n[liang2023gpt] ✓ | Real paper. Patterns, vol 4, no 7, pages 100779, 2023. Authors (Liang, Yuksekgonul, Mao, Wu, Zou) correct. All metadata correct.\n```\n\n## Cite-Context Cross-Check\n\nAll cite-context pairings verified against the tex files. One note:\n\n- **related_work.tex:11** — `GPTZero~\\cite{liang2023gpt}` groups this paper alongside RAID as a \"benchmark\" that \"evaluates robustness at scale.\" Liang et al. 2023 is actually a study showing GPT detectors are biased against non-native writers — it evaluates detectors (including GPTZero) but is not itself a benchmark. The citation is not wrong (the paper does evaluate robustness), but framing it as a benchmark parallel to RAID is slightly misleading. Consider rewording to clarify it evaluates robustness concerns rather than providing a benchmark.\n\nAll other cite-context pairings are accurate — no misattributions found.\n\n## Summary\n\n| Metric | Count |\n|--------|-------|\n| Total entries | 37 |\n| ✓ Correct | 36 |\n| ✗ Error | 1 |\n\n### Errors to fix\n\n1. **[guo2024curious]** — Author name: `Clavel, Chloe` → `Clavel, Chlo\\'{e}` (missing accent on Chloé)\n\n### Advisory (not errors)\n\n1. **[liang2023gpt]** cite context in related_work.tex:11 — framed as a \"benchmark\" alongside RAID; actually a robustness/bias study. Consider rewording the sentence.\n"
}
````

</details>

<details><summary>Recorded metadata</summary>

````json
{
  "recorded_role": "tool",
  "session": "worker_review_ref-audit-B_20260526T104706",
  "tool": "Write",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/artifacts/ref_audit_worker_B.md",
    "content": "# Reference Audit — Worker B\n\nAudited: `references.bib` (37 entries)\nDate: 2026-05-26\n\n## Per-Entry Verification\n\n```\n[kirchenbauer2023watermark] ✓ | Real paper. ICML 2023, PMLR, pages 17061–17084. Authors, title, venue all correct.\n\n[drayson2025] ✓ | Real paper. EMNLP 2025. Title, authors (Drayson, Yilmaz, Lampos) correct. arXiv:2502.15654 confirmed.\n\n[schaeffer2025position] ✓ | Real paper. arXiv preprint 2503.03150, March 2025. Authors (Schaeffer, Kazdan, Arulandu, Koyejo) correct. Currently under review (NeurIPS 2025 OpenReview); bib correctly lists as @article/arXiv.\n\n[kazdan2025collapse] ✓ | Real paper. Confirmed ICML 2025 (PMLR proceedings + ICML poster page). Authors correct. Note: ICML proceedings title drops \"?\" → \"Collapse or Thrive: Perils and Promises…\" (colon, not question mark), but arXiv original has \"?\". Cosmetic, not an error.\n\n[mitchell2023detectgpt] ✓ | Real paper. ICML 2023. Authors (Mitchell, Lee, Khazatsky, Manning, Finn) correct.\n\n[basani2026diveye] ✓ | Real paper. TMLR 2026 confirmed (GitHub: [TMLR '26], OpenReview). Authors (Basani, Chen) correct. ISSN 2835-8856 correct.\n\n[zawalski2026codec] ✓ | Real paper. ICLR 2026 confirmed (OpenReview, LinkedIn announcement). Authors (Zawalski, Boubdir, Bałazy, Nushi, Ribalta) correct.\n\n[zhang2024minkpp] ✓ | Real paper. ICLR 2025 Spotlight. Year field = 2025, correct. (Cite key says \"2024\" — cosmetic, no effect on output.) Authors correct.\n\n[shumailov2024collapse] ✓ | Real paper. Nature 2024, vol 631, pages 755–759. Authors correct (Nature itself lists \"Ross Anderson\" without middle initial, matching bib). Title, DOI correct.\n\n[alemohammad2024selfconsuming] ✓ | Real paper. ICLR 2024. Authors (Alemohammad, Casco-Rodriguez, Luzi, Humayun, Babaei, LeJeune, Siahkoohi, Baraniuk) correct.\n\n[dohmatob2024model] ✓ | Real paper. ICML 2024 (PMLR v235). Authors (Dohmatob, Feng, Yang, Charton, Kempe) correct.\n\n[xie2023dsir] ✓ | Real paper. NeurIPS 2023. Authors (Xie, Santurkar, Ma, Liang) correct.\n\n[tirumala2023d4] ✓ | Real paper. NeurIPS 2023 (Datasets & Benchmarks track). Authors (Tirumala, Simig, Aghajanyan, Morcos) correct.\n\n[xie2023doremi] ✓ | Real paper. NeurIPS 2023. Authors (Xie, Pham, Dong, Du, Liu, Lu, Liang, Le, Ma, Yu) correct.\n\n[hans2024binoculars] ✓ | Real paper. ICML 2024 (PMLR v235). Authors (Hans, Schwarzschild, Cherepanova, Kazemi, Saha, Goldblum, Geiping, Goldstein) correct.\n\n[alain2017understanding] ✓ | Real paper. ICLR 2017 Workshop track. Authors (Alain, Bengio) correct.\n\n[belinkov2022probing] ✓ | Real paper. Computational Linguistics, vol 48, no 1, pages 207–219, 2022. All metadata correct.\n\n[bao2024fast] ✓ | Real paper. ICLR 2024. Authors (Bao, Zhao, Teng, Yang, Zhang) correct.\n\n[frank2001ordinal] ✓ | Real paper. ECML 2001 (LNCS 2167), pages 145–156. Authors (Frank, Hall) correct. DOI 10.1007/3-540-44795-4_13 correct.\n\n[cheng2025beyond] ✓ | Real paper. WWW 2025 (ACM Web Conference). Authors (Cheng, Zhou, Jiang, Wang, Li) correct.\n\n[mehta2025beyond] ✓ | Real paper. arXiv 2511.17602, November 2025. Author (Mehta) correct. Bib correctly lists as @article/arXiv.\n\n[sun2025aigt] ✓ | Real paper. ACL 2025 (ACL Anthology 2025.acl-long.1120). Authors (Sun, Zhang, Shen, Zhang, Liu, Backes, Zhang, He) correct.\n\n[spennemann2025quantifying] ✓ | Real paper. arXiv 2504.08755, April 2025. Author (Spennemann) correct. Note: original arXiv title uses odd \"Ai\" capitalization; bib normalizes to {AI} which is correct.\n\n[dohmatob2025strong] ✓ | Real paper. ICLR 2025 Spotlight. Authors (Dohmatob, Feng, Subramonian, Kempe) correct.\n\n[wang2024semeval] ✓ | Real paper. SemEval-2024 (co-located with NAACL 2024). Authors correct (large author list verified against ACL Anthology).\n\n[gerstgrasser2024model] ✓ | Real paper. COLM 2024 confirmed (OpenReview, COLM accepted papers list). Authors correct.\n\n[guo2024curious] ✗ | Author name spelling: bib has \"Clavel, Chloe\" but correct name is \"Chloé Clavel\" (accent é). Should be \"Clavel, Chlo\\'{e}\". Everything else (title, Findings of NAACL 2024, other authors) correct.\n\n[briesch2023selfconsuming] ✓ | Real paper. arXiv 2311.16822, November 2023 (v2 June 2024). Still preprint; bib correctly lists as @article/arXiv. Authors (Briesch, Sobania, Rothlauf) correct.\n\n[padmakumar2024writing] ✓ | Real paper. ICLR 2024. Authors (Padmakumar, He) correct.\n\n[krishna2023paraphrasing] ✓ | Real paper. NeurIPS 2023. Authors (Krishna, Song, Karpinska, Wieting, Iyyer) correct.\n\n[sadasivan2023detect] ✓ | Real paper. arXiv 2303.11156, March 2023. Still preprint; bib correctly lists as @article/arXiv. Authors correct.\n\n[hao2025rewrite] ✓ | Real paper. ACL 2025 (ACL Anthology 2025.acl-long.322). Authors (Hao, Li, Zhao, Yang, Mao) correct.\n\n[wang2025unveiling] ✓ | Real paper. ACL 2025 (ACL Anthology 2025.acl-long.624), pages 12740–12755. Authors (Wang, Li, Yan, Cheng, Zhang) correct.\n\n[fu2025theoretical] ✓ | Real paper. ICLR 2025 (OpenReview). Authors (Fu, Wang, Chen, Tian, Tao) correct.\n\n[verma2024ghostbuster] ✓ | Real paper. NAACL 2024, pages 1702–1717. Authors (Verma, Fleisig, Tomlin, Klein) correct.\n\n[dugan2024raid] ✓ | Real paper. ACL 2024, pages 12463–12492. Authors (Dugan, Hwang, Trhlík, Zhu, Ludan, Xu, Ippolito, Callison-Burch) correct.\n\n[liang2023gpt] ✓ | Real paper. Patterns, vol 4, no 7, pages 100779, 2023. Authors (Liang, Yuksekgonul, Mao, Wu, Zou) correct. All metadata correct.\n```\n\n## Cite-Context Cross-Check\n\nAll cite-context pairings verified against the tex files. One note:\n\n- **related_work.tex:11** — `GPTZero~\\cite{liang2023gpt}` groups this paper alongside RAID as a \"benchmark\" that \"evaluates robustness at scale.\" Liang et al. 2023 is actually a study showing GPT detectors are biased against non-native writers — it evaluates detectors (including GPTZero) but is not itself a benchmark. The citation is not wrong (the paper does evaluate robustness), but framing it as a benchmark parallel to RAID is slightly misleading. Consider rewording to clarify it evaluates robustness concerns rather than providing a benchmark.\n\nAll other cite-context pairings are accurate — no misattributions found.\n\n## Summary\n\n| Metric | Count |\n|--------|-------|\n| Total entries | 37 |\n| ✓ Correct | 36 |\n| ✗ Error | 1 |\n\n### Errors to fix\n\n1. **[guo2024curious]** — Author name: `Clavel, Chloe` → `Clavel, Chlo\\'{e}` (missing accent on Chloé)\n\n### Advisory (not errors)\n\n1. **[liang2023gpt]** cite context in related_work.tex:11 — framed as a \"benchmark\" alongside RAID; actually a robustness/bias study. Consider rewording the sentence.\n"
  }
}
````

</details>

---

### Tool result

_source line 106 · 2026-05-26T10:53:59.351645+00:00_

File created successfully at: /home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/artifacts/ref_audit_worker_B.md

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_review_ref-audit-B_20260526T104706",
  "tool": "Write",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 107 · 2026-05-26T10:53:59.351792+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:register_artifact",
  "max_results": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_review_ref-audit-B_20260526T104706",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:register_artifact",
    "max_results": "1"
  }
}
```

</details>

---

### Tool result

_source line 108 · 2026-05-26T10:53:59.351922+00:00_

No matching deferred tools found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_review_ref-audit-B_20260526T104706",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 109 · 2026-05-26T10:53:59.352078+00:00_

审计完成。结果写入 `artifacts/ref_audit_worker_B.md`。

**37 条 entry 全部为真实论文，无 AI 幻觉。**

- **36 ✓**，**1 ✗**
- 唯一错误：`[guo2024curious]` 作者 `Clavel, Chloe` 缺少重音符号，应为 `Clavel, Chlo\'{e}`
- 建议关注：`[liang2023gpt]` 在 related_work.tex 中被当作 "benchmark" 引用，但该论文实际是关于检测器对非母语者偏见的研究，非基准测试本身

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_review_ref-audit-B_20260526T104706"
}
```

</details>

---
