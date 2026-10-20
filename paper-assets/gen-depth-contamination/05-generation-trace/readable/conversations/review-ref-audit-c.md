# review ref audit C

**Generational Depth Estimation of Recursive Synthetic Text: Measuring the Discrimination Boundary** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 115
- **Recorded user turns:** 0
- **Tool calls:** 57
- **Original source:** `logs/chats/worker_review_ref-audit-C_20260526T104716.jsonl`
- **Structured JSON:** [`9e2caaaf942692ebfa03.json`](../../sessions/9e/9e2caaaf942692ebfa03.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

115 recorded events

### Tool call

_source line 1 · 2026-05-26T10:55:30.809882+00:00_

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
  "session": "worker_review_ref-audit-C_20260526T104716",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/references.bib"
  }
}
```

</details>

---

### Tool result

_source line 2 · 2026-05-26T10:55:30.810296+00:00_

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
  "session": "worker_review_ref-audit-C_20260526T104716",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-26T10:55:30.810517+00:00_

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
  "session": "worker_review_ref-audit-C_20260526T104716",
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

_source line 4 · 2026-05-26T10:55:30.810664+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_review_ref-audit-C_20260526T104716",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-26T10:55:30.810849+00:00_

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
  "session": "worker_review_ref-audit-C_20260526T104716",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Kirchenbauer Geiping \"A Watermark for Large Language Models\" ICML 2023"
  }
}
```

</details>

---

### Tool call

_source line 6 · 2026-05-26T10:55:30.810997+00:00_

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
  "session": "worker_review_ref-audit-C_20260526T104716",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Drayson Yilmaz Lampos \"Machine-Generated Text Detection Prevents Language Model Collapse\" 2025"
  }
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-26T10:55:30.811118+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Schaeffer Kazdan \"Position: Model Collapse Does Not Mean What You Think\" 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_review_ref-audit-C_20260526T104716",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Schaeffer Kazdan \"Position: Model Collapse Does Not Mean What You Think\" 2025"
  }
}
```

</details>

---

### Tool call

_source line 8 · 2026-05-26T10:55:30.811235+00:00_

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
  "session": "worker_review_ref-audit-C_20260526T104716",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Kazdan Schaeffer \"Collapse or Thrive? Perils and Promises of Synthetic Data\" ICML 2025"
  }
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-26T10:55:30.811348+00:00_

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
  "session": "worker_review_ref-audit-C_20260526T104716",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Mitchell Lee Khazatsky \"DetectGPT Zero-Shot Machine-Generated Text Detection\" ICML 2023"
  }
}
```

</details>

---

### Tool call

_source line 10 · 2026-05-26T10:55:30.811469+00:00_

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
  "session": "worker_review_ref-audit-C_20260526T104716",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Basani Chen \"Diversity Boosts AI-Generated Text Detection\" DivEye TMLR 2026"
  }
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-26T10:55:30.811582+00:00_

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
  "session": "worker_review_ref-audit-C_20260526T104716",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Zawalski Boubdir \"Detecting Data Contamination in LLMs via In-Context Learning\" ICLR 2026"
  }
}
```

</details>

---

### Tool call

_source line 12 · 2026-05-26T10:55:30.811691+00:00_

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
  "session": "worker_review_ref-audit-C_20260526T104716",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Zhang Sun Yeats \"Min-K%++ Improved Baseline Detecting Pre-Training Data\" ICLR 2025"
  }
}
```

</details>

---

### Tool result

_source line 13 · 2026-05-26T10:55:30.811855+00:00_

Web search results for query: "Kirchenbauer Geiping "A Watermark for Large Language Models" ICML 2023"

Links: [{"title":"[2301.10226] A Watermark for Large Language Models","url":"https://arxiv.org/abs/2301.10226"},{"title":"A Watermark for Large Language Models","url":"https://proceedings.mlr.press/v202/kirchenbauer23a/kirchenbauer23a.pdf"},{"title":"[PDF] A Watermark for Large Language Models | Semantic Scholar","url":"https://www.semanticscholar.org/paper/A-Watermark-for-Large-Language-Models-Kirchenbauer-Geiping/cb5b71a622aff47014d4f28a958679629a8b6363"},{"title":"ICML Poster A Watermark for Large Language Models","url":"https://icml.cc/virtual/2023/poster/24544"},{"title":"dblp: A Watermark for Large Language Models.","url":"https://dblp.org/rec/conf/icml/KirchenbauerGWK23.html"},{"title":"GitHub - jwkirchenbauer/lm-watermarking · GitHub","url":"https://github.com/jwkirchenbauer/lm-watermarking"},{"title":"A Watermark for Large Language Models | NSF Public Access Repository","url":"https://par.nsf.gov/biblio/10522346-watermark-large-language-models"},{"title":"A Watermark for Large Language Models","url":"https://arxiv.org/pdf/2301.10226"},{"title":"A Watermark for Large Language Models | Request PDF","url":"https://www.researchgate.net/publication/367388838_A_Watermark_for_Large_Language_Models"},{"title":"[2301.10226v4] A Watermark for Large Language Models","url":"https://arxiv.org/abs/2301.10226v4"}]

I found the paper! Here's what I found about "A Watermark for Large Language Models" by Kirchenbauer and Geiping:

The paper "A Watermark for Large Language Models" by John Kirchenbauer, Jonas Geiping, Yuxin Wen, Jonathan Katz, Ian Miers, and Tom Goldstein was published at ICML 2023, pages 17061-17084.

**Overview:**
The paper proposes a watermarking framework for proprietary language models, aiming to mitigate potential harms by embedding signals into generated text that are invisible to humans but algorithmically detectable from a short span of tokens.

**K
…[truncated 949 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_review_ref-audit-C_20260526T104716",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-26T10:55:30.812042+00:00_

Web search results for query: "Drayson Yilmaz Lampos "Machine-Generated Text Detection Prevents Language Model Collapse" 2025"

Links: [{"title":"[2502.15654] Machine-generated text detection prevents language model collapse","url":"https://arxiv.org/abs/2502.15654"},{"title":"Machine-generated text detection prevents language ...","url":"https://omega.cs.ucl.ac.uk/assets/pdf/papers/drayson2025-model-collapse.pdf"},{"title":"(PDF) Machine-generated text detection prevents language model collapse","url":"https://www.researchgate.net/publication/397412242_Machine-generated_text_detection_prevents_language_model_collapse"},{"title":"Machine-generated text detection prevents language model collapse","url":"https://arxiv.org/html/2502.15654v1"},{"title":"Machine-generated text detection prevents language model collapse - UCL Discovery","url":"https://discovery.ucl.ac.uk/id/eprint/10217226/"},{"title":"Machine-generated text detection prevents language model ...","url":"https://discovery.ucl.ac.uk/id/eprint/10217226/1/2025.emnlp-main.1506.pdf"},{"title":"GitHub - GeorgeDrayson/model_collapse","url":"https://github.com/GeorgeDrayson/model_collapse"},{"title":"Learning by Surprise: Surplexity for Mitigating Model Collapse in Generative AI","url":"https://arxiv.org/html/2410.12341v3"},{"title":"Vasileios LAMPOS | Associate Professor | B.Sc., M.Sc., Ph.D. | University College London, London | UCL | Department of Computer Science | Research profile","url":"https://www.researchgate.net/profile/Vasileios-Lampos"}]

I found the paper you're looking for. Here are the search results:

"Machine-generated text detection prevents language model collapse" is a paper authored by George Drayson, Emine Yilmaz, and Vasileios Lampos from the Centre for Artificial Intelligence at the University College London. 

The paper was submitted on February 21, 2025, with the most recent version (v6) dated September 21, 2025. It was published in the Proceedings of the 2025 Conference on Empirical Meth
…[truncated 766 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_review_ref-audit-C_20260526T104716",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 15 · 2026-05-26T10:55:30.812214+00:00_

Web search results for query: "Schaeffer Kazdan "Position: Model Collapse Does Not Mean What You Think" 2025"

Links: [{"title":"[2503.03150] Position: Model Collapse Does Not Mean What You Think","url":"https://arxiv.org/abs/2503.03150"},{"title":"Position: Model Collapse Does Not Mean What You Think","url":"https://arxiv.org/pdf/2503.03150"},{"title":"[Literature Review] Position: Model Collapse Does Not Mean What You Think","url":"https://www.themoonlight.io/en/review/position-model-collapse-does-not-mean-what-you-think"},{"title":"Position: Model Collapse Does Not Mean What You Think Anonymous Author(s)","url":"https://openreview.net/pdf?id=ygfzWIGDN8"},{"title":"Position: Model Collapse Does Not Mean What You Think - ADS","url":"https://ui.adsabs.harvard.edu/abs/2025arXiv250303150S/abstract"},{"title":"Position: Model Collapse Does Not Mean What You Think | OpenReview","url":"https://openreview.net/forum?id=ygfzWIGDN8"},{"title":"Model collapse occurs under some definitions, but does not occur under... | Download Scientific Diagram","url":"https://www.researchgate.net/figure/Model-collapse-occurs-under-some-definitions-but-does-not-occur-under-others-for-the_tbl1_389617145"},{"title":"Escaping Collapse: The Strength of Weak Data for Large Language Model TrainingAuthors ordered alphabetically. Author contributions are listed at the end.","url":"https://arxiv.org/html/2502.08924v2"},{"title":"\"Arxiv Papers\" Position: Model Collapse Does Not Mean What You Think (Podcast Episode 2025) - IMDb","url":"https://www.imdb.com/title/tt39510662/"}]

I found the paper! Here's what the search revealed:

"Position: Model Collapse Does Not Mean What You Think" is authored by Rylan Schaeffer, Joshua Kazdan, Alvan Caleb Arulandu, and Sanmi Koyejo. The paper addresses concerns over model collapse, defined as a degradation in future generative models' performance when trained on synthetic data generated by earlier models.

**Key Argument:**
The authors contend that the widesprea
…[truncated 1031 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_review_ref-audit-C_20260526T104716",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-26T10:55:30.812385+00:00_

Web search results for query: "Mitchell Lee Khazatsky "DetectGPT Zero-Shot Machine-Generated Text Detection" ICML 2023"

Links: [{"title":"DetectGPT: Zero-Shot Machine-Generated Text Detection using Probability Curvature","url":"https://proceedings.mlr.press/v202/mitchell23a.html"},{"title":"[2301.11305] DetectGPT: Zero-Shot Machine-Generated Text Detection using Probability Curvature","url":"https://arxiv.org/abs/2301.11305"},{"title":"ICML Oral DetectGPT: Zero-Shot Machine-Generated Text Detection using Probability Curvature","url":"https://icml.cc/virtual/2023/oral/25525"},{"title":"dblp: DetectGPT: Zero-Shot Machine-Generated Text Detection using Probability Curvature.","url":"https://dblp.org/rec/conf/icml/Mitchell0KMF23.html"},{"title":"[Paper Note] DetectGPT: Zero-Shot Machine-Generated Text Detection using Probability Curvature, Eric Mitchell+, ICML'23, 2023.01 · Issue #3698 · AkihikoWatanabe/paper_notes","url":"https://github.com/AkihikoWatanabe/paper_notes/issues/3698"},{"title":"Eric Mitchell, Yoonho Lee, Alexander Khazatsky, Christopher D. Manning, Chelsea Finn · DetectGPT: Zero-Shot Machine-Generated Text Detection using Probability Curvature","url":"https://slideslive.com/39004346/detectgpt-zeroshot-machinegenerated-text-detection-using-probability-curvature"},{"title":"[PDF] DetectGPT: Zero-Shot Machine-Generated Text Detection using Probability Curvature | Semantic Scholar","url":"https://www.semanticscholar.org/paper/9a7ac45eafe11ca003db3a300505f3b5c3f9009a"},{"title":"ICML Poster DetectGPT: Zero-Shot Machine-Generated Text Detection using Probability Curvature","url":"https://icml.cc/virtual/2023/poster/24553"}]

I found the paper! Here's what I can tell you about it:

The paper "DetectGPT: Zero-Shot Machine-Generated Text Detection using Probability Curvature" was authored by Eric Mitchell, Yoonho Lee, Alexander Khazatsky, Christopher Manning, and Chelsea Finn and presented at ICML 2023.

**Key Findings:**

The paper demonstrates that text sampled
…[truncated 1044 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_review_ref-audit-C_20260526T104716",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 17 · 2026-05-26T10:55:30.812555+00:00_

Web search results for query: "Kazdan Schaeffer "Collapse or Thrive? Perils and Promises of Synthetic Data" ICML 2025"

Links: [{"title":"[2410.16713] Collapse or Thrive? Perils and Promises of Synthetic Data in a Self-Generating World","url":"https://arxiv.org/abs/2410.16713"},{"title":"Collapse or Thrive? Perils and Promises of Synthetic Data in a Self-Generating World | OpenReview","url":"https://openreview.net/forum?id=Xr5iINA3zU"},{"title":"1 Introduction","url":"https://arxiv.org/html/2410.16713"},{"title":"Collapse or Thrive? Perils and Promises of Synthetic Data in a Self-Generating World","url":"https://arxiv.org/html/2410.16713v1"},{"title":"[PDF] Collapse or Thrive? Perils and Promises of Synthetic Data in a Self-Generating World | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Collapse-or-Thrive-Perils-and-Promises-of-Synthetic-Kazdan-Schaeffer/4b510679ec7f6d138b04d5d0afff9ff316264974"},{"title":"Position: Machine Learning Conferences Should Establish ...","url":"https://openreview.net/pdf?id=DS1XSAPvKs"},{"title":"(PDF) Collapse or Thrive? Perils and Promises of Synthetic Data in a Self-Generating World","url":"https://www.researchgate.net/publication/385140496_Collapse_or_Thrive_Perils_and_Promises_of_Synthetic_Data_in_a_Self-Generating_World"},{"title":"GitHub - RylanSchaeffer/KoyejoLab-Collapse-or-Thrive: Code for Collapse or Thrive? Perils and Promises of Synthetic Data in a Self-Generating World","url":"https://github.com/RylanSchaeffer/KoyejoLab-Collapse-or-Thrive"},{"title":"A Closer Look at Model Collapse: From a Generalization-to-Memorization Perspective","url":"https://arxiv.org/html/2509.16499v1"}]

I found the paper! Here are the search results for the query "Kazdan Schaeffer 'Collapse or Thrive? Perils and Promises of Synthetic Data' ICML 2025":

## Paper Overview

The paper "Collapse or Thrive? Perils and Promises of Synthetic Data in a Self-Generating World" is authored by Joshua Kazdan, Rylan Schaeffer, Apratim Dey, Matth
…[truncated 1054 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_review_ref-audit-C_20260526T104716",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-26T10:55:30.812733+00:00_

Web search results for query: "Zhang Sun Yeats "Min-K%++ Improved Baseline Detecting Pre-Training Data" ICLR 2025"

Links: [{"title":"[2404.02936] Min-K%++: Improved Baseline for Detecting Pre-Training Data from Large Language Models","url":"https://arxiv.org/abs/2404.02936"},{"title":"MIN-K%++: IMPROVED BASELINE FOR DETECTING PRE ...","url":"https://proceedings.iclr.cc/paper_files/paper/2025/file/a2e3b4132ab2e0b7a21e6e75da7f91a9-Paper-Conference.pdf"},{"title":"Min-K%++: Improved Baseline for Detecting Pre-Training ...","url":"https://iclr.cc/media/iclr-2025/Slides/29228.pdf"},{"title":"Min-K%++: Improved Baseline for Pre-Training Data Detection from Large Language Models | OpenReview","url":"https://openreview.net/forum?id=ZGkfoufDaU"},{"title":"GitHub - zjysteven/mink-plus-plus: [ICLR'25 Spotlight] Min-K%++: Improved baseline for detecting pre-training data of LLMs · GitHub","url":"https://github.com/zjysteven/mink-plus-plus"},{"title":"ICLR Poster Min-K%++: Improved Baseline for Pre-Training Data Detection from Large Language Models","url":"https://iclr.cc/virtual/2025/poster/29228"},{"title":"min-k%++: improved baseline for detecting pre-training ...","url":"https://arxiv.org/pdf/2404.02936"},{"title":"Min-K%++: Improved Baseline for Detecting Pre-Training ...","url":"https://zjysteven.github.io/mink-plus-plus/"},{"title":"Min-K%++: Improved Baseline for Detecting Pre-Training Data from Large Language Models","url":"https://arxiv.org/html/2404.02936v1"},{"title":"Min-K%++: Improved Baseline for Detecting Pre-Training Data from Large Language Models | AI Research Paper Details","url":"https://www.aimodels.fyi/papers/arxiv/min-kpercent-improved-baseline-detecting-pre-training"}]

I found the paper you're looking for! Here are the key details:

**Paper Title:** Min-K%++: Improved Baseline for Pre-Training Data Detection from Large Language Models

**Authors:** Jingyang Zhang, Jingwei Sun, Eric Yeats, Yang Ouyang, Martin Kuo, Jianyi Zhang, Hao Frank Yang, and Hai L
…[truncated 760 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_review_ref-audit-C_20260526T104716",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 19 · 2026-05-26T10:55:30.812926+00:00_

Web search results for query: "Basani Chen "Diversity Boosts AI-Generated Text Detection" DivEye TMLR 2026"

Links: [{"title":"[2509.18880] Diversity Boosts AI-Generated Text Detection","url":"https://arxiv.org/abs/2509.18880"},{"title":"GitHub - IBM/diveye: [TMLR '26] Code for Diversity Boosts AI-generated Text Detection · GitHub","url":"https://github.com/IBM/diveye"},{"title":"[PDF] Diversity Boosts AI-Generated Text Detection | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Diversity-Boosts-AI-Generated-Text-Detection-Basani-Chen/77269d404ea3438f6d2ac327316f0b6ba116a48d"},{"title":"Diversity Boosts AI-Generated Text Detection","url":"https://arxiv.org/pdf/2509.18880"},{"title":"Diversity Boosts AI-Generated Text Detection Advik Raj Basani 1 Pin-Yu Chen 2","url":"https://openreview.net/pdf?id=QuDDXJ47nq"},{"title":"Diversity Boosts AI-Generated Text Detection | OpenReview","url":"https://openreview.net/forum?id=DNgsOhGZBI"},{"title":"DivEye","url":"https://diveye.vercel.app/"},{"title":"Under review as submission to TMLR Diversity Boosts AI-Generated Text Detection","url":"https://openreview.net/pdf?id=WscAU9It1l"},{"title":"[PDF] DivEye at PAN 2025: Diversity Boosts AI-Generated Text Detection | Semantic Scholar","url":"https://www.semanticscholar.org/paper/DivEye-at-PAN-2025:-Diversity-Boosts-AI-Generated-Basani-Chen/b18cdaf7ea2898664ed0850790059278ed50bb79"}]

Based on the search results, I found information about the paper "Diversity Boosts AI-Generated Text Detection" by Advik Raj Basani and Pin-Yu Chen.

The paper is authored by Advik Raj Basani and Pin-Yu Chen, and it was presented at "Data in Generative Models - The Bad, the Ugly, and the Greats" in 2025.

DivEye captures signals through interpretable statistical features, motivated by the observation that human-authored text exhibits richer variability in lexical and structural unpredictability than LLM outputs. The method outperforms existing zero-shot detectors by up to 33.2% and achiev
…[truncated 686 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_review_ref-audit-C_20260526T104716",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-26T10:55:30.813101+00:00_

Web search results for query: "Zawalski Boubdir "Detecting Data Contamination in LLMs via In-Context Learning" ICLR 2026"

Links: [{"title":"[2510.27055] Detecting Data Contamination in LLMs via In-Context Learning","url":"https://arxiv.org/abs/2510.27055"},{"title":"Detecting Data Contamination in LLMs via In-Context Learning","url":"https://arxiv.org/html/2510.27055v1"},{"title":"Detecting Data Contamination in LLMs via In-Context Learning | OpenReview","url":"https://openreview.net/forum?id=YlpaaYxx4t"},{"title":"Detecting Data Contamination in LLMs via In-Context Learning Michał Zawalski†","url":"https://openreview.net/pdf/753f569951799d9078f4db2d0e9debd74ad5b692.pdf"},{"title":"Time Travel in LLMs: Tracing Data Contamination in Large Language Models","url":"https://arxiv.org/pdf/2308.08493"},{"title":"Detecting Data Contamination in LLMs via In-Context Learning","url":"https://arxiv.org/pdf/2510.27055"},{"title":"A Comprehensive Survey of Contamination Detection Methods in Large Language Models","url":"https://arxiv.org/pdf/2404.00699"},{"title":"Towards Data Contamination Detection for Modern Large Language Models:   Limitations, Inconsistencies, and Oracle Challenges","url":"https://arxiv.org/pdf/2409.09927"}]

I found the paper! Here are the results:

The paper "Detecting Data Contamination in LLMs via In-Context Learning" is authored by Michał Zawalski and Meriem Boubdir along with Klaudia Bałazy, Besmira Nushi, and Pablo Ribalta.

The paper presents Contamination Detection via Context (CoDeC), a practical and accurate method to detect and quantify training data contamination in large language models. CoDeC distinguishes between data memorized during training and data outside the training distribution by measuring how in-context learning affects model performance.

The key finding is that in-context examples typically boost confidence for unseen datasets but may reduce it when the dataset was part of training, due to disrupted memorization patterns. The exp
…[truncated 437 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_review_ref-audit-C_20260526T104716",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool call

_source line 21 · 2026-05-26T10:55:30.813272+00:00_

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
  "session": "worker_review_ref-audit-C_20260526T104716",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Shumailov Shumaylov Zhao \"AI Models Collapse When Trained on Recursively Generated Data\" Nature 2024"
  }
}
```

</details>

---

### Tool call

_source line 22 · 2026-05-26T10:55:30.813395+00:00_

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
  "session": "worker_review_ref-audit-C_20260526T104716",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Alemohammad \"Self-Consuming Generative Models Go MAD\" ICLR 2024"
  }
}
```

</details>

---

### Tool call

_source line 23 · 2026-05-26T10:55:30.813510+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Dohmatob Feng Yang \"A Tale of Tails Model Collapse as a Change of Scaling Laws\" ICML 2024"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_review_ref-audit-C_20260526T104716",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Dohmatob Feng Yang \"A Tale of Tails Model Collapse as a Change of Scaling Laws\" ICML 2024"
  }
}
```

</details>

---

### Tool call

_source line 24 · 2026-05-26T10:55:30.813622+00:00_

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
  "session": "worker_review_ref-audit-C_20260526T104716",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Xie Santurkar Ma Liang \"Data Selection for Language Models via Importance Resampling\" NeurIPS 2023"
  }
}
```

</details>

---

### Tool call

_source line 25 · 2026-05-26T10:55:30.813752+00:00_

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
  "session": "worker_review_ref-audit-C_20260526T104716",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Tirumala Simig Aghajanyan Morcos \"D4 Improving LLM Pretraining Document De-Duplication Diversification\" NeurIPS 2023"
  }
}
```

</details>

---

### Tool call

_source line 26 · 2026-05-26T10:55:30.813888+00:00_

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
  "session": "worker_review_ref-audit-C_20260526T104716",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Xie Pham Dong \"DoReMi Optimizing Data Mixtures Speeds Up Language Model Pretraining\" NeurIPS 2023"
  }
}
```

</details>

---

### Tool call

_source line 27 · 2026-05-26T10:55:30.814000+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Hans Schwarzschild \"Spotting LLMs With Binoculars\" ICML 2024"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_review_ref-audit-C_20260526T104716",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Hans Schwarzschild \"Spotting LLMs With Binoculars\" ICML 2024"
  }
}
```

</details>

---

### Tool call

_source line 28 · 2026-05-26T10:55:30.814107+00:00_

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
  "session": "worker_review_ref-audit-C_20260526T104716",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Alain Bengio \"Understanding Intermediate Layers Using Linear Classifier Probes\" ICLR 2017"
  }
}
```

</details>

---

### Tool result

_source line 29 · 2026-05-26T10:55:30.814243+00:00_

Web search results for query: "Alemohammad "Self-Consuming Generative Models Go MAD" ICLR 2024"

Links: [{"title":"SELF-CONSUMING GENERATIVE MODELS GO MAD","url":"https://proceedings.iclr.cc/paper_files/paper/2024/file/ebc042e767de551803ccfcc45e2454f5-Paper-Conference.pdf"},{"title":"Self-Consuming Generative Models Go MAD | OpenReview","url":"https://openreview.net/forum?id=ShjMHfmPs0"},{"title":"SELF-CONSUMING GENERATIVE MODELS GO MAD - Houston Methodist Scholars","url":"https://scholars.houstonmethodist.org/en/publications/self-consuming-generative-models-go-mad/"},{"title":"[PDF] Self-Consuming Generative Models Go MAD | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Self-Consuming-Generative-Models-Go-MAD-Alemohammad-Casco-Rodriguez/ad022cd5da75637ac3e0a8f8cc4f0d394ba5ff7a"},{"title":"Self-Consuming Generative Models Go MAD | NSF Public Access Repository","url":"https://par.nsf.gov/biblio/10570494"},{"title":"ICLR Poster Self-Consuming Generative Models Go MAD","url":"https://iclr.cc/virtual/2024/poster/18592"},{"title":"Self-Consuming AI Resources","url":"https://dsp.rice.edu/ai-loops/"},{"title":"[2307.01850] Self-Consuming Generative Models Go MAD","url":"https://arxiv.org/abs/2307.01850"},{"title":"Self-Consuming Generative Models Go MAD | Montreal AI Ethics Institute","url":"https://montrealethics.ai/self-consuming-generative-models-go-mad/"}]

I found the paper! Here's a summary of the search results for "Self-Consuming Generative Models Go MAD" by Alemohammad and colleagues from ICLR 2024:

## Paper Overview

The paper addresses how advances in generative AI have led to the temptation to use synthetic data to train next-generation models. Repeating this process creates an autophagous (self-consuming) loop whose properties are poorly understood.

## Key Findings

The primary conclusion is that without enough fresh real data in each generation of an autophagous loop, future generative models are doomed to have their quality (precision) or d
…[truncated 1031 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_review_ref-audit-C_20260526T104716",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 30 · 2026-05-26T10:55:30.814402+00:00_

Web search results for query: "Dohmatob Feng Yang "A Tale of Tails Model Collapse as a Change of Scaling Laws" ICML 2024"

Links: [{"title":"A Tale of Tails: Model Collapse as a Change of Scaling Laws","url":"https://proceedings.mlr.press/v235/dohmatob24b.html"},{"title":"[2402.07043] A Tale of Tails: Model Collapse as a Change of Scaling Laws","url":"https://arxiv.org/abs/2402.07043"},{"title":"Overcoming the AI Data Crisis: A New Solution to Model Collapse | by NYU Center for Data Science | Medium","url":"https://nyudatascience.medium.com/overcoming-the-ai-data-crisis-a-new-solution-to-model-collapse-ddc5b382e182"},{"title":"ICML Poster A Tale of Tails: Model Collapse as a Change of Scaling Laws","url":"https://icml.cc/virtual/2024/poster/34339"},{"title":"[Quick Review] A Tale of Tails: Model Collapse as a Change of Scaling Laws","url":"https://liner.com/review/tale-tails-model-collapse-as-change-scaling-laws"},{"title":"A Tale of Tails: Model Collapse as a Change of Scaling Laws - NYU Scholars","url":"https://nyuscholars.nyu.edu/en/publications/a-tale-of-tails-model-collapse-as-a-change-of-scaling-laws"},{"title":"A Tale of Tails: Model Collapse as a Change of Scaling Laws | NSF Public Access Repository","url":"https://par.nsf.gov/biblio/10535859"},{"title":"A Tale of Tails: Model Collapse as a Change of Scaling Laws | AI Research Paper Details","url":"https://www.aimodels.fyi/papers/arxiv/tale-tails-model-collapse-as-change-scaling"},{"title":"A Tale of Tails: Model Collapse as a Change of Scaling Laws","url":"https://arxiv.org/html/2402.07043v2"}]

I found the paper you're looking for! Here are the key details:

## Paper Information

The paper "A Tale of Tails: Model Collapse as a Change of Scaling Laws" was authored by Elvis Dohmatob, Yunzhen Feng, Pu Yang, Francois Charton, and Julia Kempe, and appeared in the Proceedings of the 41st International Conference on Machine Learning (ICML 2024), pages 11165-11197.

## Paper Content

The paper develops a theoretic
…[truncated 873 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_review_ref-audit-C_20260526T104716",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 31 · 2026-05-26T10:55:30.814573+00:00_

Web search results for query: "Xie Santurkar Ma Liang "Data Selection for Language Models via Importance Resampling" NeurIPS 2023"

Links: [{"title":"NeurIPS Poster Data Selection for Language Models via Importance Resampling","url":"https://neurips.cc/virtual/2023/poster/70154"},{"title":"Data Selection for Language Models via Importance Resampling","url":"https://proceedings.neurips.cc//paper_files/paper/2023/hash/6b9aa8f418bde2840d5f4ab7a02f663b-Abstract-Conference.html"},{"title":"[2302.03169] Data Selection for Language Models via Importance Resampling","url":"https://arxiv.org/abs/2302.03169"},{"title":"[PDF] Data Selection for Language Models via Importance Resampling | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Data-Selection-for-Language-Models-via-Importance-Xie-Santurkar/74013b7cfa0fc524803350fca51341004565eb22"},{"title":"Sang Michael Xie, Shibani Santurkar, Tengyu Ma, Percy Liang · Data Selection for Language Models via Importance Resampling","url":"https://slideslive.com/39009489/data-selection-for-language-models-via-importance-resampling"},{"title":"Data Selection for Language Models via Importance Resampling - ADS","url":"https://ui.adsabs.harvard.edu/abs/2023arXiv230203169X/abstract"},{"title":"[2302.03169v3] Data Selection for Language Models via Importance Resampling","url":"http://arxiv.org/abs/2302.03169v3"},{"title":"Data Selection for Language Models via Importance Resampling","url":"https://www.researchgate.net/publication/368333487_Data_Selection_for_Language_Models_via_Importance_Resampling"},{"title":"Data Selection for Language Models via Importance Resampling","url":"https://arxiv.org/pdf/2302.03169"}]

I found the research paper you were searching for. Here are the key details:

**Paper Title:** Data Selection for Language Models via Importance Resampling

**Authors:** Sang Michael Xie, Shibani Santurkar, Tengyu Ma, and Percy Liang

**Conference:** Advances in Neural Information Processing Systems 36 (NeurIPS 2023) 
…[truncated 736 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_review_ref-audit-C_20260526T104716",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 32 · 2026-05-26T10:55:30.814744+00:00_

Web search results for query: "Tirumala Simig Aghajanyan Morcos "D4 Improving LLM Pretraining Document De-Duplication Diversification" NeurIPS 2023"

Links: [{"title":"D4: Improving LLM Pretraining via Document De-Duplication and Diversification","url":"https://proceedings.neurips.cc/paper_files/paper/2023/hash/a8f8cbd7f7a5fb2c837e578c75e5b615-Abstract-Datasets_and_Benchmarks.html"},{"title":"NeurIPS Poster D4: Improving LLM Pretraining via Document De-Duplication and Diversification","url":"https://neurips.cc/virtual/2023/poster/73662"},{"title":"[2308.12284] D4: Improving LLM Pretraining via Document De-Duplication and Diversification","url":"https://arxiv.org/abs/2308.12284"},{"title":"D4: Improving LLM Pretraining via Document De-Duplication and Diversification","url":"https://papers.nips.cc/paper_files/paper/2023/hash/a8f8cbd7f7a5fb2c837e578c75e5b615-Abstract-Datasets_and_Benchmarks.html"},{"title":"[PDF] D4: Improving LLM Pretraining via Document De-Duplication and Diversification | Semantic Scholar","url":"https://www.semanticscholar.org/paper/D4:-Improving-LLM-Pretraining-via-Document-and-Tirumala-Simig/11cf88dce827bd67cbfa60400306318022e736d5"},{"title":"D4: Improving LLM Pretraining via Document De-Duplication and Diversiﬁcation","url":"https://proceedings.neurips.cc/paper_files/paper/2023/file/a8f8cbd7f7a5fb2c837e578c75e5b615-Paper-Datasets_and_Benchmarks.pdf"},{"title":"D4: Improving LLM Pretraining via Document De-Duplication and Diversification","url":"https://arxiv.org/pdf/2308.12284"},{"title":"Kushal Tirumala, Daniel Simig, Armen Aghajanyan, Ari S. Morcos · D4: Improving LLM Pretraining via Document De-Duplication and Diversification","url":"https://slideslive.com/39010897/d4-improving-llm-pretraining-via-document-deduplication-and-diversification"},{"title":"Paper page - D4: Improving LLM Pretraining via Document De-Duplication and Diversification","url":"https://paperswithcode.com/paper/d4-improving-llm-pretraining-via-document-de"}]

Great! I fou
…[truncated 1168 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_review_ref-audit-C_20260526T104716",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 33 · 2026-05-26T10:55:30.814943+00:00_

Web search results for query: "Shumailov Shumaylov Zhao "AI Models Collapse When Trained on Recursively Generated Data" Nature 2024"

Links: [{"title":"A Note on Shumailov et al. (2024): ‘AI Models Collapse When Trained on Recursively Generated Data’","url":"https://arxiv.org/html/2410.12954v2"},{"title":"AI models collapse when trained on recursively generated data | Nature","url":"https://www.nature.com/articles/s41586-024-07566-y"},{"title":"AI models collapse when trained on recursively generated data - PubMed","url":"https://pubmed.ncbi.nlm.nih.gov/39048682/"},{"title":"A Note on Shumailov et al. (2024): 'AI Models Collapse ...","url":"https://arxiv.org/pdf/2410.12954"},{"title":"A note on “AI models collapse when trained on recursively generated data” | by Ali Borji | Medium","url":"https://medium.com/@aliborji/a-note-on-ai-models-collapse-when-trained-on-recursively-generated-data-5bee1de1ab87"},{"title":"AI models collapse when trained on recursively generated data","url":"https://www.pure.ed.ac.uk/ws/portalfiles/portal/460496122/ShumailovEtalNature2024AIModelsCollapseWhen.pdf"},{"title":"[PDF] AI models collapse when trained on recursively generated data | Semantic Scholar","url":"https://www.semanticscholar.org/paper/AI-models-collapse-when-trained-on-recursively-data-Shumailov-Shumaylov/603d3f90fc40f79ff51258f0295de3ec5107f73e"},{"title":"[2410.12954] A Note on Shumailov et al. (2024): `AI Models Collapse When Trained on Recursively Generated Data'","url":"https://arxiv.org/abs/2410.12954"},{"title":"Author Correction: AI models collapse when trained on recursively generated data | Nature","url":"https://www.nature.com/articles/s41586-025-08905-3"},{"title":"AI models collapse when trained on recursively generated data","url":"https://bibbase.org/network/publication/shumailov-shumaylov-zhao-papernot-anderson-gal-aimodelscollapsewhentrainedonrecursivelygenerateddata-2024"}]

I found the paper you're looking for. Here are the key details:

**Publication Inf
…[truncated 1181 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_review_ref-audit-C_20260526T104716",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 34 · 2026-05-26T10:55:30.815122+00:00_

Web search results for query: "Hans Schwarzschild "Spotting LLMs With Binoculars" ICML 2024"

Links: [{"title":"GitHub - ahans30/Binoculars: [ICML 2024] Binoculars: Zero-Shot Detection of LLM-Generated Text · GitHub","url":"https://github.com/ahans30/Binoculars"},{"title":"[2401.12070] Spotting LLMs With Binoculars: Zero-Shot Detection of Machine-Generated Text","url":"https://arxiv.org/abs/2401.12070"},{"title":"Spotting LLMs With Binoculars: Zero-Shot Detection of Machine-Generated Text | MPI-IS","url":"https://is.mpg.de/en/publications/hans_spotting_2024"},{"title":"Spotting LLMs with binoculars | Proceedings of the 41st International Conference on Machine Learning","url":"https://dl.acm.org/doi/10.5555/3692070.3692768"},{"title":"[Quick Review] Spotting LLMs With Binoculars: Zero-Shot Detection of Machine-Generated Text","url":"https://liner.com/review/spotting-llms-with-binoculars-zeroshot-detection-machinegenerated-text"},{"title":"Spotting LLMs With Binoculars: Zero-Shot Detection of Machine-Generated Text","url":"https://proceedings.mlr.press/v235/hans24a.html"},{"title":"Spotting LLMs With Binoculars: Zero-Shot Detection of Machine-Generated Text | Safety- and Efficiency- aligned Learning – MPI-IS","url":"https://is.mpg.de/seal/publications/hans_spotting_2024"},{"title":"Binoculars/README.md at main · ahans30/Binoculars","url":"https://github.com/ahans30/Binoculars/blob/main/README.md"},{"title":"[PDF] Spotting LLMs With Binoculars: Zero-Shot Detection of Machine-Generated Text | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Spotting-LLMs-With-Binoculars:-Zero-Shot-Detection-Hans-Schwarzschild/8dafb105a0cec1956443003eeea9fcf13c0ffa99"},{"title":"[2401.12070v2] Spotting LLMs With Binoculars: Zero-Shot Detection of Machine-Generated Text","url":"https://arxiv.org/abs/2401.12070v2"}]

I found the paper! Here's what I found about "Spotting LLMs With Binoculars":

The paper is authored by Abhimanyu Hans, Avi Schwarzschild, Valeriia Cherepanova, 
…[truncated 1138 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_review_ref-audit-C_20260526T104716",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 35 · 2026-05-26T10:55:30.815289+00:00_

Web search results for query: "Alain Bengio "Understanding Intermediate Layers Using Linear Classifier Probes" ICLR 2017"

Links: [{"title":"Workshop track - ICLR 2017 UNDERSTANDING INTERMEDIATE LAYERS","url":"https://openreview.net/pdf?id=HJ4-rAVtl"},{"title":"[1610.01644] Understanding intermediate layers using linear classifier probes","url":"https://arxiv.org/abs/1610.01644"},{"title":"[PDF] Understanding intermediate layers using linear classifier probes | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Understanding-intermediate-layers-using-linear-Alain-Bengio/5e23a28063b395bdaf784dc548a046885cb90cf2"},{"title":"(PDF) Understanding intermediate layers using linear classifier probes","url":"https://www.researchgate.net/publication/308913017_Understanding_intermediate_layers_using_linear_classifier_probes"},{"title":"Understanding intermediate layers using linear classifier probes","url":"http://index.cslt.org/mediawiki/images/f/f6/Understanding_intermediate_layers_using_linear_classifier_probes.pdf"},{"title":"Understanding intermediate layers using linear classiﬁer probes Guillaume Alain","url":"https://arxiv.org/pdf/1610.01644"},{"title":"[1610.01644v3] Understanding intermediate layers using linear classifier probes","url":"https://arxiv.org/abs/1610.01644v3"},{"title":"[1610.01644v1] Understanding intermediate layers using linear classifier probes","url":"https://www.arxiv.org/abs/1610.01644v1"}]

Based on the search results, I found information about this paper. Note that the author's name is **Guillaume Alain** (not Alain Bengio), co-authored with Yoshua Bengio.

The paper "Understanding Intermediate Layers Using Linear Classifier Probes" was authored by Guillaume Alain and Yoshua Bengio and published in the Workshop track at ICLR 2017.

The method uses linear classifiers referred to as "probes" that can only use hidden units from intermediate layers as features, and these probes cannot affect the training phase of a model—they are general
…[truncated 461 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_review_ref-audit-C_20260526T104716",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 36 · 2026-05-26T10:55:30.815465+00:00_

Web search results for query: "Xie Pham Dong "DoReMi Optimizing Data Mixtures Speeds Up Language Model Pretraining" NeurIPS 2023"

Links: [{"title":"DoReMi: Optimizing Data Mixtures Speeds Up Language Model Pretraining | OpenReview","url":"https://openreview.net/forum?id=lXuByUeHhd"},{"title":"NeurIPS Poster DoReMi: Optimizing Data Mixtures Speeds Up Language Model Pretraining","url":"https://neurips.cc/virtual/2023/poster/70588"},{"title":"DoReMi: Optimizing Data Mixtures Speeds Up Language Model Pretraining","url":"https://proceedings.neurips.cc/paper_files/paper/2023/file/dcba6be91359358c2355cd920da3fcbd-Paper-Conference.pdf"},{"title":"[2305.10429] DoReMi: Optimizing Data Mixtures Speeds Up Language Model Pretraining","url":"https://arxiv.org/abs/2305.10429"},{"title":"[PDF] DoReMi: Optimizing Data Mixtures Speeds Up Language Model Pretraining | Semantic Scholar","url":"https://www.semanticscholar.org/paper/DoReMi:-Optimizing-Data-Mixtures-Speeds-Up-Language-Xie-Pham/9b4f7c97c0b83a80c32bc0b93595cbcfb4ecb16d"},{"title":"Papers with Code - DoReMi: Optimizing Data Mixtures Speeds Up Language Model Pretraining","url":"https://paperswithcode.com/paper/doremi-optimizing-data-mixtures-speeds-up-1"},{"title":"DoReMi: Optimizing Data Mixtures for LM Pretraining","url":"https://hunterheidenreich.com/notes/natural-language-processing/language-models/doremi-data-mixture-optimization/"},{"title":"DoReMi: Optimizing Data Mixtures Speeds Up Language Model Pretraining - ADS","url":"https://ui.adsabs.harvard.edu/abs/2023arXiv230510429X/abstract"},{"title":"[Quick Review] DoReMi: Optimizing Data Mixtures Speeds Up Language Model Pretraining","url":"https://liner.com/review/doremi-optimizing-data-mixtures-speeds-up-language-model-pretraining"},{"title":"GitHub - sangmichaelxie/doremi: Pytorch implementation of DoReMi, a method for optimizing the data mixture weights in language modeling datasets · GitHub","url":"https://github.com/sangmichaelxie/doremi"}]

I found comprehensive in
…[truncated 1423 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_review_ref-audit-C_20260526T104716",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool call

_source line 37 · 2026-05-26T10:55:30.815637+00:00_

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
  "session": "worker_review_ref-audit-C_20260526T104716",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Belinkov \"Probing Classifiers: Promises, Shortcomings, and Advances\" Computational Linguistics 2022"
  }
}
```

</details>

---

### Tool call

_source line 38 · 2026-05-26T10:55:30.815762+00:00_

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
  "session": "worker_review_ref-audit-C_20260526T104716",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Bao Zhao Teng \"Fast-DetectGPT Efficient Zero-Shot Detection Machine-Generated Text\" ICLR 2024"
  }
}
```

</details>

---

### Tool call

_source line 39 · 2026-05-26T10:55:30.815901+00:00_

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
  "session": "worker_review_ref-audit-C_20260526T104716",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Frank Hall \"A Simple Approach to Ordinal Classification\" ECML 2001"
  }
}
```

</details>

---

### Tool call

_source line 40 · 2026-05-26T10:55:30.816017+00:00_

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
  "session": "worker_review_ref-audit-C_20260526T104716",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Cheng Zhou Jiang \"Beyond Binary Towards Fine-Grained LLM-Generated Text Detection Role Recognition\" WWW 2025"
  }
}
```

</details>

---

### Tool call

_source line 41 · 2026-05-26T10:55:30.816135+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Mehta \"Beyond Surface-Level Similarity Hierarchical Contamination Detection Synthetic Training Data\" arXiv 2511.17602"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_review_ref-audit-C_20260526T104716",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Mehta \"Beyond Surface-Level Similarity Hierarchical Contamination Detection Synthetic Training Data\" arXiv 2511.17602"
  }
}
```

</details>

---

### Tool call

_source line 42 · 2026-05-26T10:55:30.816249+00:00_

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
  "session": "worker_review_ref-audit-C_20260526T104716",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Sun Zhang Shen \"Are We in the AI-Generated Text World Already Quantifying Monitoring AIGT Social Media\" ACL 2025"
  }
}
```

</details>

---

### Tool call

_source line 43 · 2026-05-26T10:55:30.816359+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Spennemann \"Delving into Quantification AI-Generated Content Internet Synthetic Data\" arXiv 2504.08755"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_review_ref-audit-C_20260526T104716",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Spennemann \"Delving into Quantification AI-Generated Content Internet Synthetic Data\" arXiv 2504.08755"
  }
}
```

</details>

---

### Tool call

_source line 44 · 2026-05-26T10:55:30.816467+00:00_

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
  "session": "worker_review_ref-audit-C_20260526T104716",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Dohmatob Feng Subramonian Kempe \"Strong Model Collapse\" ICLR 2025"
  }
}
```

</details>

---

### Tool result

_source line 45 · 2026-05-26T10:55:30.816610+00:00_

Web search results for query: "Belinkov "Probing Classifiers: Promises, Shortcomings, and Advances" Computational Linguistics 2022"

Links: [{"title":"Probing Classifiers: Promises, Shortcomings, and Advances - ACL Anthology","url":"https://aclanthology.org/2022.cl-1.7/"},{"title":"[2102.12452] Probing Classifiers: Promises, Shortcomings, and Advances","url":"https://arxiv.org/abs/2102.12452"},{"title":"Probing Classifiers: Promises, Shortcomings, and Advances | Computational Linguistics | MIT Press","url":"https://direct.mit.edu/coli/article/48/1/207/107571/Probing-Classifiers-Promises-Shortcomings-and"},{"title":"Yonatan Belinkov | publications","url":"https://belinkov.com/publications/publicationstype/"},{"title":"(PDF) Probing Classifiers: Promises, Shortcomings, and Advances","url":"https://www.researchgate.net/publication/355072709_Probing_Classifiers_Promises_Shortcomings_and_Advances"},{"title":"Probing Classifiers: Promises, Shortcomings, and Advances - Technion - Israel Institute of Technology","url":"https://cris.technion.ac.il/en/publications/probing-classifiers-promises-shortcomings-and-advances/"},{"title":"Probing Classifiers: Promises, Shortcomings, and Advances - Israeli Research Community Portal","url":"https://cris.iucc.ac.il/en/publications/probing-classifiers-promises-shortcomings-and-advances/"},{"title":"Probing Classifiers: Promises, Shortcomings, and Advances","url":"https://aclanthology.org/2022.cl-1.7.pdf"},{"title":"@article{belinkov-2022-probing,","url":"https://aclanthology.org/2022.cl-1.7.bib"},{"title":"Probing Classifiers: Promises, Shortcomings, and Advances","url":"https://scite.ai/reports/probing-classifiers-promises-shortcomings-and-kepAxaJ3"}]

I found the paper you're looking for! Here are the key details:

**Publication Information:**
Yonatan Belinkov. 2022. Probing Classifiers: Promises, Shortcomings, and Advances. Computational Linguistics, 48(1):207–219.

**Paper Overview:**
Probing classifiers have emerged as one of the pr
…[truncated 857 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_review_ref-audit-C_20260526T104716",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 46 · 2026-05-26T10:55:30.816796+00:00_

Web search results for query: "Bao Zhao Teng "Fast-DetectGPT Efficient Zero-Shot Detection Machine-Generated Text" ICLR 2024"

Links: [{"title":"GitHub - baoguangsheng/fast-detect-gpt: Code base for ICLR 2024 \"Fast-DetectGPT: Efficient Zero-Shot Detection of Machine-Generated Text via Conditional Probability Curvature\". · GitHub","url":"https://github.com/baoguangsheng/fast-detect-gpt"},{"title":"ICLR Poster Fast-DetectGPT: Efficient Zero-Shot Detection of Machine-Generated Text via Conditional Probability Curvature","url":"https://iclr.cc/virtual/2024/poster/19201"},{"title":"[2310.05130] Fast-DetectGPT: Efficient Zero-Shot Detection of Machine-Generated Text via Conditional Probability Curvature","url":"https://arxiv.org/abs/2310.05130"},{"title":"Fast-DetectGPT: Efficient Zero-Shot Detection of Machine-Generated Text via Conditional Probability Curvature","url":"https://proceedings.iclr.cc/paper_files/paper/2024/hash/6b8c6f846c3575e1d1ad496abea28826-Abstract-Conference.html"},{"title":"(PDF) FAST-DETECTGPT: EFFICIENT ZERO-SHOT DETEC- TION OF MACHINE-GENERATED TEXT VIA CONDI- TIONAL PROBABILITY CURVATURE","url":"https://www.researchgate.net/publication/388188914_FAST-DETECTGPT_EFFICIENT_ZERO-SHOT_DETEC-_TION_OF_MACHINE-GENERATED_TEXT_VIA_CONDI-_TIONAL_PROBABILITY_CURVATURE"},{"title":"Fast-DetectGPT: Efficient Zero-Shot Detection of Machine-Generated Text via Conditional Probability Curvature | OpenReview","url":"https://openreview.net/forum?id=Bpcgcr8E8Z"},{"title":"Fast-DetectGPT: Efficient Zero-Shot Detection of Machine-Generated Text via Conditional Probability Curvature","url":"https://arxiv.org/html/2310.05130v3"},{"title":"ICLR 2024 | Fast-DetectGPT: Efficient Zero-Shot Detection of Machine-Generated Text - YouTube","url":"https://www.youtube.com/watch?v=Nk7LpsrIUDE"},{"title":"[2310.05130v3] Fast-DetectGPT: Efficient Zero-Shot Detection of Machine-Generated Text via Conditional Probability Curvature","url":"https://arxiv.org/abs/2310.05130v3"}]

I found 
…[truncated 1124 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_review_ref-audit-C_20260526T104716",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 47 · 2026-05-26T10:55:30.816977+00:00_

Web search results for query: "Cheng Zhou Jiang "Beyond Binary Towards Fine-Grained LLM-Generated Text Detection Role Recognition" WWW 2025"

Links: [{"title":"[2410.14259] Beyond Binary: Towards Fine-Grained LLM-Generated Text Detection via Role Recognition and Involvement Measurement","url":"https://arxiv.org/abs/2410.14259"},{"title":"[2410.14259v1] Beyond Binary: Towards Fine-Grained LLM-Generated Text Detection via Role Recognition and Involvement Measurement","url":"https://arxiv.org/abs/2410.14259v1"},{"title":"Beyond Binary: Towards Fine-Grained LLM-Generated Text","url":"https://arxiv.org/pdf/2410.14259"},{"title":"Beyond Binary: Towards Fine-Grained LLM-Generated Text Detection via Role Recognition and Involvement Measurement – Own Your AI","url":"https://ownyourai.com/beyond-binary-towards-fine-grained-llm-generated-text-detection-via-role-recognition-and-involvement-measurement/"},{"title":"Beyond Binary: Towards Fine-Grained LLM-Generated Text Detection via Role Recognition and Involvement Measurement | Proceedings of the ACM on Web Conference 2025","url":"https://dl.acm.org/doi/10.1145/3696410.3714770"},{"title":"Beyond Binary: Towards Fine-Grained LLM-Generated Text Detection via Role Recognition and Involvement Measurement","url":"https://arxiv.org/html/2410.14259v2"},{"title":"Papers with Code - Beyond Binary: Towards Fine-Grained LLM-Generated Text Detection via Role Recognition and Involvement Measurement","url":"https://paperswithcode.com/paper/beyond-binary-towards-fine-grained-llm"},{"title":"About me - Feng Jiang / Personal Homepage","url":"https://fjiangai.github.io/"}]

I found the paper! Here are the search results:

The paper "Beyond Binary: Towards Fine-Grained LLM-Generated Text Detection via Role Recognition and Involvement Measurement" is authored by Zihao Cheng, Li Zhou, Feng Jiang, Benyou Wang, and Haizhou Li.

The paper was published in the Proceedings of the ACM Web Conference 2025 (WWW '25), held April 28-May 2, 2025, in Sydney, N
…[truncated 717 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_review_ref-audit-C_20260526T104716",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 48 · 2026-05-26T10:55:30.817154+00:00_

Web search results for query: "Frank Hall "A Simple Approach to Ordinal Classification" ECML 2001"

Links: [{"title":"A Simple Approach to Ordinal Classification | Springer Nature Link","url":"https://link.springer.com/chapter/10.1007/3-540-44795-4_13"},{"title":"[PDF] A Simple Approach to Ordinal Classification | Semantic Scholar","url":"https://www.semanticscholar.org/paper/A-Simple-Approach-to-Ordinal-Classification-Frank-Hall/76fc26939d73c565431e1f38107a4245e739284e"},{"title":"A simple approach to ordinal classification.","url":"https://researchcommons.waikato.ac.nz/items/ce0009f5-92fa-4113-b8b2-7ac929cfd32c"},{"title":"(PDF) A Simple Approach to Ordinal Classification (2001) | Eibe Frank | 655 Citations","url":"https://scispace.com/papers/a-simple-approach-to-ordinal-classification-2mjbzk39ox"},{"title":"(PDF) A Simple Approach to Ordinal Classification","url":"https://www.researchgate.net/publication/226877154_A_Simple_Approach_to_Ordinal_Classification"},{"title":"A simple approach to ordinal classification | Proceedings of the 12th European Conference on Machine Learning","url":"https://dl.acm.org/doi/10.1007/3-540-44795-4_13"},{"title":"An Improved Approach to Ordinal Classification | Springer Nature Link","url":"https://link.springer.com/chapter/10.1007/978-3-662-45652-1_4"},{"title":"A Simple Approach to Ordinal Classification - Eibe Frank, Mark Andrew Hall - Google Books","url":"https://books.google.com/books/about/A_Simple_Approach_to_Ordinal_Classificat.html?id=SI2oMQAACAAJ"},{"title":"Classification of Ordinal Data Using Neural Networks | Springer Nature Link","url":"https://link.springer.com/chapter/10.1007/11564096_70"},{"title":"GitHub - liorsidi/ordinal-classifier: python implemantation for Ordinal classifier by Frank, Eibe, and Mark Hall. \"A simple approach to ordinal classification.\" European Conference on Machine Learning. Springer Berlin Heidelberg, 2001.","url":"https://github.com/liorsidi/ordinal-classifier"}]

I found the paper! Here are
…[truncated 1509 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_review_ref-audit-C_20260526T104716",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 49 · 2026-05-26T10:55:30.817332+00:00_

Web search results for query: "Sun Zhang Shen "Are We in the AI-Generated Text World Already Quantifying Monitoring AIGT Social Media" ACL 2025"

Links: [{"title":"Are We in the AI-Generated Text World Already? Quantifying and Monitoring AIGT on Social Media - ACL Anthology","url":"https://aclanthology.org/2025.acl-long.1120/"},{"title":"GitHub - TrustAIRLab/AIGT_on_Social_Media: [ACL2025] Official repository for \"Are We in the AI-Generated Text World Already? Quantifying and Monitoring AIGT on Social Media\"","url":"https://github.com/TrustAIRLab/AIGT_on_Social_Media"},{"title":"Are We in the AI-Generated Text World Already? Quantifying and Monitoring AIGT on Social Media | Request PDF","url":"https://www.researchgate.net/publication/394299909_Are_We_in_the_AI-Generated_Text_World_Already_Quantifying_and_Monitoring_AIGT_on_Social_Media"},{"title":"[2412.18148] Are We in the AI-Generated Text World Already? Quantifying and Monitoring AIGT on Social Media","url":"https://arxiv.org/abs/2412.18148"},{"title":"Google Scholar","url":"https://scholar.google.com/scholar?q=Zhen+Sun%2C+Zongmin+Zhang%2C+Xinyue+Shen%2C+Ziyi+Zhang%2C+Yule+Liu%2C+Michael+Backes%2C+Yang+Zhang%2C+and+Xinlei+He.+2024.+Are+We+in+the+AI-Generated+Text+World+Already%3F+Quantifying+and+Monitoring+AIGT+on+Social+Media.+arXiv+preprint+arXiv%3A2412.18148%282024%29."},{"title":"tarryzhang/OSM-Det · Hugging Face","url":"https://huggingface.co/tarryzhang/OSM-Det"},{"title":"Are We in the AI-Generated Text World Already? Quantifying and Monitoring AIGT on Social Media","url":"https://arxiv.org/html/2412.18148v2"},{"title":"(PDF) Are We in the AI-Generated Text World Already? Quantifying and Monitoring AIGT on Social Media","url":"https://www.researchgate.net/publication/387382689_Are_We_in_the_AI-Generated_Text_World_Already_Quantifying_and_Monitoring_AIGT_on_Social_Media"}]

I found the paper! Here's what the search results show:

The paper "Are We in the AI-Generated Text World Already? Quantifying and Mon
…[truncated 1149 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_review_ref-audit-C_20260526T104716",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 50 · 2026-05-26T10:55:30.817502+00:00_

Web search results for query: "Mehta "Beyond Surface-Level Similarity Hierarchical Contamination Detection Synthetic Training Data" arXiv 2511.17602"

Links: [{"title":"[2511.17602] Beyond Surface-Level Similarity: Hierarchical Contamination Detection for Synthetic Training Data in Foundation Models","url":"https://arxiv.org/abs/2511.17602"},{"title":"Beyond Surface-Level Similarity: Hierarchical Contamination Detection for Synthetic Training Data in Foundation Models","url":"https://arxiv.org/html/2511.17602v1"},{"title":"Beyond Surface-Level Similarity: Hierarchical Contamination Detection","url":"https://www.arxiv.org/pdf/2511.17602"},{"title":"(PDF) Beyond Surface-Level Similarity: Hierarchical Contamination Detection for Synthetic Training Data in Foundation Models","url":"https://www.researchgate.net/publication/397933312_Beyond_Surface-Level_Similarity_Hierarchical_Contamination_Detection_for_Synthetic_Training_Data_in_Foundation_Models"},{"title":"Beyond Surface-Level Similarity: Hierarchical Contamination Detection for Synthetic Training Data in Foundation Models | Article Information | J-GLOBAL","url":"https://jglobal.jst.go.jp/en/detail?JGLOBAL_ID=202502216067314793"},{"title":"Machine Learning Oct 2024","url":"https://arxiv.org/list/cs.LG/2024-10?skip=1475&show=2000"},{"title":"Machine Learning Jan 2024","url":"https://arxiv.org/list/cs.LG/2024-01?skip=325&show=2000"},{"title":"Machine Learning Feb 2025","url":"https://arxiv.org/list/cs.LG/2025-02?skip=2425&show=2000"},{"title":"Catchup results for stat from Wed, 13 Dec 2023","url":"https://arxiv.org/catchup?smonth=12&sday=13&group=grp_&archive=stat&num=2000&order=reverse&method=without&syear=2023"}]

I found the paper! Here are the search results for the arXiv preprint 2511.17602:

**Title:** Beyond Surface-Level Similarity: Hierarchical Contamination Detection for Synthetic Training Data in Foundation Models

**Author:** Sushant Mehta

**Publication Date:** November 18, 2025

**Summary:** Synthetic dat
…[truncated 885 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_review_ref-audit-C_20260526T104716",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 51 · 2026-05-26T10:55:30.817666+00:00_

Web search results for query: "Dohmatob Feng Subramonian Kempe "Strong Model Collapse" ICLR 2025"

Links: [{"title":"Published as a conference paper at ICLR 2025 STRONG MODEL COLLAPSE","url":"https://proceedings.iclr.cc/paper_files/paper/2025/file/284afdc2309f9667d2d4fb9290235b0c-Paper-Conference.pdf"},{"title":"Strong Model Collapse | OpenReview","url":"https://openreview.net/forum?id=et5l9qPUhm"},{"title":"[2410.04840] Strong Model Collapse","url":"https://arxiv.org/abs/2410.04840"},{"title":"ICLR Poster Strong Model Collapse","url":"https://iclr.cc/virtual/2025/poster/32070"},{"title":"Strong Model Collapse - ADS","url":"https://ui.adsabs.harvard.edu/abs/2024arXiv241004840D/abstract"},{"title":"Published as a conference paper at ICLR 2025","url":"https://openreview.net/pdf?id=MQXrTMonT1"},{"title":"Published as a conference paper at ICLR 2025","url":"https://proceedings.iclr.cc/paper_files/paper/2025/file/7416573f05b50beac6d0aef3abc805c0-Paper-Conference.pdf"},{"title":"A Closer Look at Model Collapse: From a Generalization-to-Memorization Perspective | Request PDF","url":"https://www.researchgate.net/publication/395724450_A_Closer_Look_at_Model_Collapse_From_a_Generalization-to-Memorization_Perspective"},{"title":"dblp: Elvis Dohmatob","url":"https://dblp.org/pid/134/9794.html"},{"title":"Elvis Dohmatob - Concordia University","url":"https://www.concordia.ca/faculty/elvis-dohmatob.html"}]

I found the paper! Here are the search results for "Strong Model Collapse" by Dohmatob, Feng, Subramonian, and Kempe at ICLR 2025:

## Overview

The paper establishes a strong form of the model collapse phenomenon within the scaling laws paradigm, which underpins the training of large neural networks like ChatGPT and Llama, considering a supervised regression setting where model collapse is a critical performance degradation due to synthetic data in the training corpus.

## Key Findings

The results show that even the smallest fraction of synthetic data (e.g., as little as 1 p
…[truncated 746 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_review_ref-audit-C_20260526T104716",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 52 · 2026-05-26T10:55:30.817879+00:00_

Web search results for query: "Spennemann "Delving into Quantification AI-Generated Content Internet Synthetic Data" arXiv 2504.08755"

Links: [{"title":"[2504.08755] Delving into: the quantification of Ai-generated content on the internet (synthetic data)","url":"https://arxiv.org/abs/2504.08755"},{"title":"25-12 Delving into Ai generated content on the internet","url":"https://arxiv.org/pdf/2504.08755"},{"title":"(PDF) Delving into: the quantification of Ai-generated content on the internet (synthetic data)","url":"https://www.researchgate.net/publication/390772908_Delving_into_the_quantification_of_Ai-generated_content_on_the_internet_synthetic_data"},{"title":"Delving into: the quantification of Ai-generated content on ...","url":"https://www.semanticscholar.org/paper/Delving-into:-the-quantification-of-Ai-generated-on-Spennemann/f7740011daee667f954a69b73458686c173e2ea1"},{"title":"We Need Improved Data Curation and Attribution in AI for Scientific Discovery","url":"https://arxiv.org/html/2504.02486v1"},{"title":"[2504.02898] A Practical Synthesis of Detecting AI-Generated Textual, Visual, and Audio Content","url":"https://arxiv.org/abs/2504.02898"},{"title":"Machine Learning Apr 2025","url":"https://arxiv.org/list/cs.LG/2025-04?show=500&skip=2500"}]

I found the paper! Here's information about the research:

**Paper Details:**
The paper is titled "Delving into: the quantification of Ai-generated content on the internet (synthetic data)" by Dirk HR Spennemann, with arXiv identifier 2504.08755.

**Methodology:**
The paper demonstrates that linguistic markers—specifically, keywords commonly used by ChatGPT—can effectively be used to estimate the presence of generative AI content online. The research derived monthly frequencies of webpages containing specific phrases through Google searches for terms like 'delve into' and 'explore', with data collected for the period January 2020 to March 2025.

**Key Findings:**
The findings suggest that at least 30% of text on ac
…[truncated 370 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_review_ref-audit-C_20260526T104716",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool call

_source line 53 · 2026-05-26T10:55:30.818056+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Wang Mansurov \"SemEval-2024 Task 8 Multidomain Multimodel Multilingual Machine-Generated Text Detection\" 2024"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_review_ref-audit-C_20260526T104716",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Wang Mansurov \"SemEval-2024 Task 8 Multidomain Multimodel Multilingual Machine-Generated Text Detection\" 2024"
  }
}
```

</details>

---

### Tool call

_source line 54 · 2026-05-26T10:55:30.818180+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Gerstgrasser Schaeffer \"Is Model Collapse Inevitable Breaking Curse Recursion\" COLM 2024"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_review_ref-audit-C_20260526T104716",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Gerstgrasser Schaeffer \"Is Model Collapse Inevitable Breaking Curse Recursion\" COLM 2024"
  }
}
```

</details>

---

### Tool call

_source line 55 · 2026-05-26T10:55:30.818296+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Guo Shang \"The Curious Decline of Linguistic Diversity Training Language Models Synthetic Text\" NAACL 2024"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_review_ref-audit-C_20260526T104716",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Guo Shang \"The Curious Decline of Linguistic Diversity Training Language Models Synthetic Text\" NAACL 2024"
  }
}
```

</details>

---

### Tool call

_source line 56 · 2026-05-26T10:55:30.818413+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Briesch Sobania Rothlauf \"Large Language Models Suffer From Their Own Output Self-Consuming Training Loop\" 2023"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_review_ref-audit-C_20260526T104716",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Briesch Sobania Rothlauf \"Large Language Models Suffer From Their Own Output Self-Consuming Training Loop\" 2023"
  }
}
```

</details>

---

### Tool call

_source line 57 · 2026-05-26T10:55:30.818525+00:00_

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
  "session": "worker_review_ref-audit-C_20260526T104716",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Padmakumar He \"Does Writing with Language Models Reduce Content Diversity\" ICLR 2024"
  }
}
```

</details>

---

### Tool call

_source line 58 · 2026-05-26T10:55:30.818634+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Krishna Song Karpinska \"Paraphrasing Evades Detectors AI-Generated Text Retrieval Defense\" NeurIPS 2023"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_review_ref-audit-C_20260526T104716",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Krishna Song Karpinska \"Paraphrasing Evades Detectors AI-Generated Text Retrieval Defense\" NeurIPS 2023"
  }
}
```

</details>

---

### Tool call

_source line 59 · 2026-05-26T10:55:30.818742+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Sadasivan Kumar Balasubramanian \"Can AI-Generated Text be Reliably Detected\" 2023 venue published"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_review_ref-audit-C_20260526T104716",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Sadasivan Kumar Balasubramanian \"Can AI-Generated Text be Reliably Detected\" 2023 venue published"
  }
}
```

</details>

---

### Tool result

_source line 60 · 2026-05-26T10:55:30.818933+00:00_

Web search results for query: "Guo Shang "The Curious Decline of Linguistic Diversity Training Language Models Synthetic Text" NAACL 2024"

Links: [{"title":"The Curious Decline of Linguistic Diversity: Training Language Models on Synthetic Text - ACL Anthology","url":"https://aclanthology.org/2024.findings-naacl.228/"},{"title":"[PDF] The Curious Decline of Linguistic Diversity: Training Language Models on Synthetic Text | Semantic Scholar","url":"https://www.semanticscholar.org/paper/The-Curious-Decline-of-Linguistic-Diversity:-Models-Guo-Shang/7d5ea474aa1cf732bb1d00faa07a5bb2c9119cfd"},{"title":"(PDF) The Curious Decline of Linguistic Diversity: Training Language Models on Synthetic Text","url":"https://www.researchgate.net/publication/382631840_The_Curious_Decline_of_Linguistic_Diversity_Training_Language_Models_on_Synthetic_Text"},{"title":"The Curious Decline of Linguistic Diversity: Training Language Models on Synthetic Text - Laboratoire d'informatique de l'X (LIX)","url":"https://hal.inrae.fr/X-LIX/hal-04593399v1"},{"title":"The Curious Decline of Linguistic Diversity: Training Language Models on Synthetic Text - Archive ouverte HAL","url":"https://hal.science/hal-04593399"},{"title":"@inproceedings{guo-etal-2024-curious,","url":"https://aclanthology.org/2024.findings-naacl.228.bib"},{"title":"The Curious Decline of Linguistic Diversity: Training Language Models on Synthetic Text | AI Research Paper Details","url":"https://www.aimodels.fyi/papers/arxiv/curious-decline-linguistic-diversity-training-language-models"},{"title":"[2311.09807] The Curious Decline of Linguistic Diversity: Training Language Models on Synthetic Text","url":"https://arxiv.org/abs/2311.09807"}]

I found the paper you're looking for! Here are the details:

The paper is titled "The Curious Decline of Linguistic Diversity: Training Language Models on Synthetic Text" by Yanzhu Guo, Guokan Shang, Michalis Vazirgiannis, and Chloé Clavel, and it was published in the Findings of the Associati
…[truncated 1082 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_review_ref-audit-C_20260526T104716",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 61 · 2026-05-26T10:55:30.819105+00:00_

Web search results for query: "Padmakumar He "Does Writing with Language Models Reduce Content Diversity" ICLR 2024"

Links: [{"title":"[2309.05196] Does Writing with Language Models Reduce Content Diversity?","url":"https://arxiv.org/abs/2309.05196"},{"title":"DOES WRITING WITH LANGUAGE MODELS REDUCE CONTENT DIVERSITY? - NYU Scholars","url":"https://nyuscholars.nyu.edu/en/publications/does-writing-with-language-models-reduce-content-diversity"},{"title":"Does Writing with Language Models Reduce Content Diversity? | AI Research Paper Details","url":"https://www.aimodels.fyi/papers/arxiv/does-writing-language-models-reduce-content-diversity"},{"title":"[PDF] Does Writing with Language Models Reduce Content Diversity? | Semantic Scholar","url":"https://www.semanticscholar.org/paper/f95fb254da1f7b74a14ac8feb3f834d64e67e4cd"},{"title":"Does Writing with Language Models Reduce Content Diversity? | NSF Public Access Repository","url":"https://par.nsf.gov/biblio/10534705-does-writing-language-models-reduce-content-diversity"},{"title":"Does Writing with Language Models Reduce Content Diversity? | Request PDF","url":"https://www.researchgate.net/publication/373837896_Does_Writing_with_Language_Models_Reduce_Content_Diversity"},{"title":"Published as a conference paper at ICLR 2025","url":"https://proceedings.iclr.cc/paper_files/paper/2025/file/ea94957d81b1c1caf87ef5319fa6b467-Paper-Conference.pdf"},{"title":"Does Writing with Language Models Reduce Content Diversity?","url":"https://arxiv.org/html/2309.05196v3"}]

I found the paper you're looking for! Here's information about it:

"Does Writing with Language Models Reduce Content Diversity?" is a paper by Padmakumar and He presented at ICLR 2024.

**Key Findings:**

The research was conducted by Vishakh Padmakumar and He He from New York University, measuring the impact of co-writing on diversity through a controlled experiment where users wrote argumentative essays in three setups—using a base LLM (GPT3), a feedback-tuned 
…[truncated 677 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_review_ref-audit-C_20260526T104716",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 62 · 2026-05-26T10:55:30.819252+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Hao Li Zhao \"Learning to Rewrite Generalized LLM-Generated Text Detection\" ACL 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_review_ref-audit-C_20260526T104716",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Hao Li Zhao \"Learning to Rewrite Generalized LLM-Generated Text Detection\" ACL 2025"
  }
}
```

</details>

---

### Tool result

_source line 63 · 2026-05-26T10:55:30.819397+00:00_

Web search results for query: "Briesch Sobania Rothlauf "Large Language Models Suffer From Their Own Output Self-Consuming Training Loop" 2023"

Links: [{"title":"[2311.16822] Large Language Models Suffer From Their Own Output: An Analysis of the Self-Consuming Training Loop","url":"https://arxiv.org/abs/2311.16822"},{"title":"[PDF] Large Language Models Suffer From Their Own Output: An Analysis of the Self-Consuming Training Loop | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Large-Language-Models-Suffer-From-Their-Own-Output:-Briesch-Sobania/c24ed03689adc2a075004c6619f43f7f6230fe4b"},{"title":"Large Language Models Suffer From Their Own Output: An Analysis of the Self-Consuming Training Loop","url":"https://arxiv.org/html/2311.16822v2"},{"title":"[2311.16822v2] Large Language Models Suffer From Their Own Output: An Analysis of the Self-Consuming Training Loop","url":"https://arxiv.org/abs/2311.16822v2"},{"title":"Google Scholar","url":"https://scholar.google.com/scholar_lookup?title=Large+language+models+suffer+from+their+own+output:+An+analysis+of+the+self-consuming+training+loop&amp=&author=Martin+Briesch&amp=&author=Dominik+Sobania&amp=&author=Franz+Rothlauf&amp=&publication_year=2023"},{"title":"Large Language Models Suffer From Their Own Output: An Analysis of the Self-Consuming Training Loop - ADS","url":"https://ui.adsabs.harvard.edu/abs/arXiv:2311.16822"},{"title":"[2311.16822] Large Language Models Suffer From Their Own Output: An Analysis of the Self-Consuming Training Loop","url":"https://ar5iv.labs.arxiv.org/html/2311.16822"},{"title":"Large Language Models Suffer From Their Own Output: An Analysis of the Self-Consuming Training Loop | AI Research Paper Details","url":"https://www.aimodels.fyi/papers/arxiv/large-language-models-suffer-from-their-own"},{"title":"Collapse or Thrive? Perils and Promises of Synthetic Data in a Self-Generating World","url":"https://arxiv.org/html/2410.16713v2"},{"title":"An Analysis of the Self-Consuming T
…[truncated 1342 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_review_ref-audit-C_20260526T104716",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 64 · 2026-05-26T10:55:30.819570+00:00_

Web search results for query: "Wang Mansurov "SemEval-2024 Task 8 Multidomain Multimodel Multilingual Machine-Generated Text Detection" 2024"

Links: [{"title":"[2404.14183] SemEval-2024 Task 8: Multidomain, Multimodel and Multilingual Machine-Generated Text Detection","url":"https://arxiv.org/abs/2404.14183"},{"title":"SemEval-2024 Task 8: Multidomain, Multimodel and Multilingual Machine-Generated Text Detection - ACL Anthology","url":"https://aclanthology.org/2024.semeval-1.279/"},{"title":"SemEval-2024 Task 8: Multidomain, Multimodel and Multilingual Machine-Generated Text Detection","url":"https://arxiv.org/html/2404.14183v1"},{"title":"SemEval-2024 Task 8: Multidomain, Multimodel and Multilingual Machine-Generated Text Detection - NYU Scholars","url":"https://nyuscholars.nyu.edu/en/publications/semeval-2024-task-8-multidomain-multimodel-and-multilingual-machi"},{"title":"[PDF] SemEval-2024 Task 8: Multidomain, Multimodel and Multilingual Machine-Generated Text Detection | Semantic Scholar","url":"https://www.semanticscholar.org/paper/SemEval-2024-Task-8:-Multidomain,-Multimodel-and-Wang-Mansurov/c56eab12bd00e2fe28868af21d518044d66df00d"},{"title":"SemEval-2024 Tasks | SemEval-2024","url":"https://semeval.github.io/SemEval2024/tasks.html"},{"title":"SemEval-2024 Task 8: Multidomain, Multimodel and Multilingual Machine-Generated Text Detection. | BibSonomy","url":"https://www.bibsonomy.org/bibtex/bfca76cf8884cdacbcb4db85e0b442bc"}]

Based on the search results, I found comprehensive information about the SemEval-2024 Task 8 paper. Here are the key findings:

## Paper Overview

The paper is authored by Yuxia Wang, Jonibek Mansurov, Petar Ivanov, Jinyan Su, Artem Shelmanov, Akim Tsvigun, Osama Mohammed Afzal, Tarek Mahmoud, Giovanni Puccetti, Thomas Arnold, and others.

## Task Structure

The paper presents the results and main findings of SemEval-2024 Task 8: Multigenerator, Multidomain, and Multilingual Machine-Generated Text Detection, which featured three subta
…[truncated 867 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_review_ref-audit-C_20260526T104716",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 65 · 2026-05-26T10:55:30.819733+00:00_

Web search results for query: "Gerstgrasser Schaeffer "Is Model Collapse Inevitable Breaking Curse Recursion" COLM 2024"

Links: [{"title":"[2404.01413] Is Model Collapse Inevitable? Breaking the Curse of Recursion by Accumulating Real and Synthetic Data","url":"https://arxiv.org/abs/2404.01413"},{"title":"Is Model Collapse Inevitable? Breaking the Curse of Recursion by Accumulating Real and Synthetic Data | Rylan Schaeffer","url":"https://rylanschaeffer.github.io/content/research/2024_arxiv_is_model_collapse_inevitable/main.html"},{"title":"Is Model Collapse Inevitable? Breaking the Curse of Recursion by Accumulating Real and Synthetic Data | Stanford SALT Lab","url":"https://saltlab.stanford.edu/papers/gerstgrasser-is-model-collapse-2024/"},{"title":"Is Model Collapse Inevitable? Breaking the Curse of Recursion by Accumulating Real and Synthetic Data | AI Research Paper Details","url":"https://www.aimodels.fyi/papers/arxiv/is-model-collapse-inevitable-breaking-curse-recursion"},{"title":"[PDF] Is Model Collapse Inevitable? Breaking the Curse of Recursion by Accumulating Real and Synthetic Data | Semantic Scholar","url":"https://www.semanticscholar.org/paper/e8815da26d4e6cac8b23b7e6aa75cec028cb66d2"},{"title":"Is Model Collapse Inevitable? Breaking the Curse of Recursion by Accumulating Real and Synthetic Data - ADS","url":"https://ui.adsabs.harvard.edu/abs/2024arXiv240401413G/abstract"},{"title":"[2404.01413v1] Is Model Collapse Inevitable? Breaking the Curse of Recursion by Accumulating Real and Synthetic Data","url":"https://arxiv.org/abs/2404.01413v1"},{"title":"Is Model Collapse Inevitable? Breaking the Curse of Recursion by Accumulating Real and Synthetic Data","url":"https://arxiv.org/html/2404.01413v2"}]

I found the paper you're looking for! Here are the details:

**Paper Title:** "Is Model Collapse Inevitable? Breaking the Curse of Recursion by Accumulating Real and Synthetic Data"

**Authors:** Matthias Gerstgrasser, Rylan Schaeffer, Apratim Dey, Rafael 
…[truncated 851 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_review_ref-audit-C_20260526T104716",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 66 · 2026-05-26T10:55:30.819929+00:00_

Web search results for query: "Sadasivan Kumar Balasubramanian "Can AI-Generated Text be Reliably Detected" 2023 venue published"

Links: [{"title":"[2303.11156] Can AI-Generated Text be Reliably Detected?","url":"https://arxiv.org/abs/2303.11156"},{"title":"Can AI-Generated Text be Reliably Detected?","url":"https://bibbase.org/network/publication/sadasivan-kumar-balasubramanian-wang-feizi-canaigeneratedtextbereliablydetected-2023"},{"title":"Can AI-Generated Text be Reliably Detected? - ADS","url":"https://ui.adsabs.harvard.edu/abs/2023arXiv230311156S/abstract"},{"title":"(PDF) Can AI-Generated Text be Reliably Detected?","url":"https://www.researchgate.net/publication/369380286_Can_AI-Generated_Text_be_Reliably_Detected"},{"title":"Can AI-Generated Text be Reliably Detected? (2023) | Vinu Sankar Sadasivan | 186 Citations","url":"https://scispace.com/papers/can-ai-generated-text-be-reliably-detected-1n2s6nbj"},{"title":"[PDF] Can AI-Generated Text be Reliably Detected? | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Can-AI-Generated-Text-be-Reliably-Detected-Sadasivan-Kumar/5ee8bb4fc80a291b2e416a2a879e7153a783d7e9"},{"title":"Can AI-Generated Text be Reliably Detected?","url":"https://www.catalyzex.com/paper/can-ai-generated-text-be-reliably-detected"},{"title":"No reliable way to detect AI-generated text, boffins say • The Register","url":"https://www.theregister.com/2023/03/21/detecting_ai_generated_text/"},{"title":"[2303.11156v4] Can AI-Generated Text be Reliably Detected?","url":"https://arxiv.org/abs/2303.11156v4"}]

Based on the search results, here's the information about the paper:

**Paper Title:** "Can AI-Generated Text be Reliably Detected?"

**Authors:** Vinu Sankar Sadasivan, Aounon Kumar, Sriram Balasubramanian, Wenxiao Wang, Soheil Feizi

**Publication Venue:** arXiv:2303.11156 (preprint server)

**Year Published:** June 2023

**Submission Date:** Submitted on 17 Mar 2023 (v1)

The paper was initially submitted to arXiv in March 20
…[truncated 202 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_review_ref-audit-C_20260526T104716",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 67 · 2026-05-26T10:55:30.820103+00:00_

Web search results for query: "Hao Li Zhao "Learning to Rewrite Generalized LLM-Generated Text Detection" ACL 2025"

Links: [{"title":"Learning to Rewrite: Generalized LLM-Generated Text Detection - ACL Anthology","url":"https://aclanthology.org/2025.acl-long.322/"},{"title":"[2408.04237] Learning to Rewrite: Generalized LLM-Generated Text Detection","url":"https://arxiv.org/abs/2408.04237"},{"title":"Learning to Rewrite: Generalized LLM-Generated Text ...","url":"https://www.cs.columbia.edu/~junfeng/papers/learn2rewrite-acl25.pdf"},{"title":"Learning to Rewrite: Generalized LLM-Generated Text Detection - ADS","url":"https://ui.adsabs.harvard.edu/abs/2024arXiv240804237L/abstract"},{"title":"Accepted Main Conference Papers - ACL 2025","url":"https://2025.aclweb.org/program/main_papers/"},{"title":"Learning to Rewrite: Generalized Detection of LLM-Generated Text | OpenReview","url":"https://openreview.net/forum?id=wojnTvBXqt"},{"title":"Paper page - Learning to Rewrite: Generalized LLM-Generated Text Detection","url":"https://huggingface.co/papers/2408.04237"},{"title":"Distance Learning for Detecting LLM-Generated Text","url":"https://arxiv.org/pdf/2601.21895"},{"title":"Learning to Rewrite: Generalized LLM-Generated Text Detection","url":"https://arxiv.org/html/2408.04237v2"},{"title":"Evaluating Fine-Tuned LLMs for AI Text Detection | Springer Nature Link","url":"https://link.springer.com/chapter/10.1007/978-3-032-00642-4_17"}]

I found the paper you're looking for! Here are the key details:

"Learning to Rewrite: Generalized LLM-Generated Text Detection" is a paper by Wei Hao, Ran Li, Weiliang Zhao, Junfeng Yang, and Chengzhi Mao, published at ACL 2025. It appears in the Proceedings of the 63rd Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers), pages 6421–6434, Vienna, Austria.

**Overview of the work:**

The paper introduces Learning2Rewrite, a novel framework for detecting AI-generated text with exceptional generalization to
…[truncated 686 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_review_ref-audit-C_20260526T104716",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 68 · 2026-05-26T10:55:30.820282+00:00_

Web search results for query: "Krishna Song Karpinska "Paraphrasing Evades Detectors AI-Generated Text Retrieval Defense" NeurIPS 2023"

Links: [{"title":"GitHub - martiansideofthemoon/ai-detection-paraphrases: Official repository for our NeurIPS 2023 paper \"Paraphrasing evades detectors of AI-generated text, but retrieval is an effective defense\" (https://arxiv.org/abs/2303.13408). · GitHub","url":"https://github.com/martiansideofthemoon/ai-detection-paraphrases"},{"title":"[PDF] Paraphrasing evades detectors of AI-generated text, but retrieval is an effective defense | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Paraphrasing-evades-detectors-of-AI-generated-text,-Krishna-Song/1c13af186d1e177b85ef1ec3fc7b8d33ec314cfd"},{"title":"Paraphrasing evades detectors of AI-generated text, but retrieval is an effective defense | OpenReview","url":"https://openreview.net/forum?id=WbFhFvjjKj"},{"title":"Paraphrasing evades detectors of AI-generated text, but retrieval is an effective defense","url":"https://proceedings.neurips.cc/paper_files/paper/2023/hash/575c450013d0e99e4b0ecf82bd1afaa4-Abstract-Conference.html"},{"title":"[2303.13408] Paraphrasing evades detectors of AI-generated text, but retrieval is an effective defense","url":"https://arxiv.org/abs/2303.13408"},{"title":"Paper page - Paraphrasing evades detectors of AI-generated text, but retrieval is an effective defense","url":"https://huggingface.co/papers/2303.13408"},{"title":"Paraphrasing evades detectors of AI-generated text, but ...","url":"https://openreview.net/pdf?id=WbFhFvjjKj"},{"title":"Adversarial Paraphrasing: A Universal Attack for Humanizing AI-Generated Text","url":"https://arxiv.org/pdf/2506.07001"},{"title":"Paraphrasing evades detectors of AI-generated text, but retrieval is an effective defense | Request PDF","url":"https://www.researchgate.net/publication/369477232_Paraphrasing_evades_detectors_of_AI-generated_text_but_retrieval_is_an_effective_defense"},{"title":"NeurIPS Po
…[truncated 1697 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_review_ref-audit-C_20260526T104716",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool call

_source line 69 · 2026-05-26T10:55:30.820457+00:00_

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
  "session": "worker_review_ref-audit-C_20260526T104716",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Wang Li Yan Cheng Zhang \"Unveiling Attractor Cycles Large Language Models Dynamical Systems Successive Paraphrasing\" ACL 2025"
  }
}
```

</details>

---

### Tool call

_source line 70 · 2026-05-26T10:55:30.820582+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Fu Wang Chen Tian Tao \"Theoretical Perspective How to Prevent Model Collapse Self-consuming Training\" ICLR 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_review_ref-audit-C_20260526T104716",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Fu Wang Chen Tian Tao \"Theoretical Perspective How to Prevent Model Collapse Self-consuming Training\" ICLR 2025"
  }
}
```

</details>

---

### Tool call

_source line 71 · 2026-05-26T10:55:30.820699+00:00_

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
  "session": "worker_review_ref-audit-C_20260526T104716",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Verma Fleisig Tomlin Klein \"Ghostbuster Detecting Text Ghostwritten Large Language Models\" NAACL 2024"
  }
}
```

</details>

---

### Tool call

_source line 72 · 2026-05-26T10:55:30.820838+00:00_

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
  "session": "worker_review_ref-audit-C_20260526T104716",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Dugan Hwang Trhlik \"RAID Shared Benchmark Robust Evaluation Machine-Generated Text Detectors\" ACL 2024"
  }
}
```

</details>

---

### Tool call

_source line 73 · 2026-05-26T10:55:30.820957+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Liang Yuksekgonul Mao \"GPT detectors are biased against non-native English writers\" Patterns 2023"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_review_ref-audit-C_20260526T104716",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Liang Yuksekgonul Mao \"GPT detectors are biased against non-native English writers\" Patterns 2023"
  }
}
```

</details>

---

### Tool call

_source line 74 · 2026-05-26T10:55:30.821068+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Gerstgrasser \"Is Model Collapse Inevitable\" COLM 2024 conference publication"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_review_ref-audit-C_20260526T104716",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Gerstgrasser \"Is Model Collapse Inevitable\" COLM 2024 conference publication"
  }
}
```

</details>

---

### Tool call

_source line 75 · 2026-05-26T10:55:30.821177+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Padmakumar He \"Does Writing with Language Models Reduce Content Diversity\" ICLR 2024 OR 2025 proceedings"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_review_ref-audit-C_20260526T104716",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Padmakumar He \"Does Writing with Language Models Reduce Content Diversity\" ICLR 2024 OR 2025 proceedings"
  }
}
```

</details>

---

### Tool call

_source line 76 · 2026-05-26T10:55:30.821284+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Schaeffer Kazdan \"Position Model Collapse Does Not Mean\" ICML 2025 accepted conference"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_review_ref-audit-C_20260526T104716",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Schaeffer Kazdan \"Position Model Collapse Does Not Mean\" ICML 2025 accepted conference"
  }
}
```

</details>

---

### Tool result

_source line 77 · 2026-05-26T10:55:30.821431+00:00_

Web search results for query: "Wang Li Yan Cheng Zhang "Unveiling Attractor Cycles Large Language Models Dynamical Systems Successive Paraphrasing" ACL 2025"

Links: [{"title":"Unveiling Attractor Cycles in Large Language Models: A Dynamical Systems View of Successive Paraphrasing - ACL Anthology","url":"https://aclanthology.org/2025.acl-long.624/"},{"title":"Unveiling Attractor Cycles in Large Language Models: A Dynamical Systems View of Successive Paraphrasing [Quick Review]","url":"https://liner.com/review/unveiling-attractor-cycles-in-large-language-models-dynamical-systems-view"},{"title":"[2502.15208] Unveiling Attractor Cycles in Large Language Models: A Dynamical Systems View of Successive Paraphrasing","url":"https://arxiv.org/abs/2502.15208"},{"title":"A Dynamical Systems View of Successive Paraphrasing","url":"https://aclanthology.org/2025.acl-long.624.pdf"},{"title":"Unveiling Attractor Cycles in Large Language Models: A Dynamical Systems View of Successive Paraphrasing","url":"https://arxiv.org/html/2502.15208v1"},{"title":"Google Scholar","url":"https://scholar.google.com/scholar?q=Unveiling+Attractor+Cycles+in+Large+Language+Models:+A+Dynamical+Systems+View+of+Successive+Paraphrasing."},{"title":"Unveiling Attractor Cycles in Large Language Models: A Dynamical Systems View of Successive Paraphrasing | AI Research Paper Details","url":"https://www.aimodels.fyi/papers/arxiv/unveiling-attractor-cycles-large-language-models-dynamical"},{"title":"Unveiling Attractor Cycles in Large Language Models: A Dynamical","url":"https://arxiv.org/pdf/2502.15208"},{"title":"[2502.15208v1] Unveiling Attractor Cycles in Large Language Models: A Dynamical Systems View of Successive Paraphrasing","url":"https://arxiv.org/abs/2502.15208v1"}]

I found the paper! Here's the information about the research:

The paper is titled "Unveiling Attractor Cycles in Large Language Models: A Dynamical Systems View of Successive Paraphrasing" by Zhilin Wang, Yafu Li, Jianhao Yan, Yu Che
…[truncated 1158 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_review_ref-audit-C_20260526T104716",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 78 · 2026-05-26T10:55:30.821604+00:00_

Web search results for query: "Verma Fleisig Tomlin Klein "Ghostbuster Detecting Text Ghostwritten Large Language Models" NAACL 2024"

Links: [{"title":"Ghostbuster: Detecting Text Ghostwritten by Large Language Models - ACL Anthology","url":"https://aclanthology.org/2024.naacl-long.95/"},{"title":"Detecting Text Ghostwritten by Large Language Models","url":"https://aclanthology.org/2024.naacl-long.95.pdf"},{"title":"[2305.15047] Ghostbuster: Detecting Text Ghostwritten by Large Language Models","url":"https://arxiv.org/abs/2305.15047"},{"title":"Ghostbuster: Detecting Text Ghostwritten by Large Language Models Vivek Verma","url":"https://nlp.cs.berkeley.edu/pubs/Verma-Fleisig-Tomlin-Klein_2024_Ghostbuster_paper.pdf"},{"title":"Ghostbuster: Detecting Text Ghostwritten by Large Language Models","url":"https://arxiv.org/html/2305.15047v3"},{"title":"[PDF] Ghostbuster: Detecting Text Ghostwritten by Large Language Models | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Ghostbuster:-Detecting-Text-Ghostwritten-by-Large-Verma-Fleisig/fb467f368b9e196b32c90e3da7ae0986d59cd66f"},{"title":"Ghostbuster: Detecting Text Ghostwritten by Large Language Models | Request PDF","url":"https://www.researchgate.net/publication/382631441_Ghostbuster_Detecting_Text_Ghostwritten_by_Large_Language_Models"},{"title":"[2305.15047v1] Ghostbuster: Detecting Text Ghostwritten by Large Language Models","url":"https://arxiv.org/abs/2305.15047v1"},{"title":"Ghostbuster: Detecting Text Ghostwritten by Large Language Models | AI Research Paper Details","url":"https://www.aimodels.fyi/papers/arxiv/ghostbuster-detecting-text-ghostwritten-by-large-language"},{"title":"Ghostbuster: Detecting Text Ghostwritten by Large Language Models - ADS","url":"https://ui.adsabs.harvard.edu/abs/2023arXiv230515047V/abstract"}]

Perfect! I found the paper you're looking for. Here are the search results:

**"Ghostbuster: Detecting Text Ghostwritten by Large Language Models"** by Vivek Verma, Eve Fleisig,
…[truncated 1297 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_review_ref-audit-C_20260526T104716",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 79 · 2026-05-26T10:55:30.821793+00:00_

Web search results for query: "Fu Wang Chen Tian Tao "Theoretical Perspective How to Prevent Model Collapse Self-consuming Training" ICLR 2025"

Links: [{"title":"A Theoretical Perspective: How to Prevent Model Collapse in Self-consuming Training Loops | OpenReview","url":"https://openreview.net/forum?id=WttfQGwpES"},{"title":"Published as a conference paper at ICLR 2025","url":"https://openreview.net/pdf?id=WttfQGwpES"},{"title":"dblp: Xinmei Tian 0001","url":"https://dblp.org/pid/03/5204-1.html"},{"title":"Published as a conference paper at ICLR 2025","url":"https://arxiv.org/pdf/2403.18699"},{"title":"Publications – Furong Huang","url":"https://furong-huang.com/publications/"}]

Based on the web search results, I found the paper you're looking for:

"A Theoretical Perspective: How to Prevent Model Collapse in Self-consuming Training Loops" by Shi Fu, Yingjie Wang, Yuzhu Chen, Xinmei Tian, and Dacheng Tao, published at ICLR 2025.

The paper introduces the notion of "recursive stability" and presents the first theoretical generalization analysis, revealing how both model architecture and the proportion between real and synthetic data influence the success of self-consuming training loops. The analysis extends to transformers in in-context learning, showing that even a constant-sized proportion of real data ensures convergence, while also providing insights into optimal synthetic data sizing.

The paper is available on OpenReview at: https://openreview.net/forum?id=WttfQGwpES


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_review_ref-audit-C_20260526T104716",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 80 · 2026-05-26T10:55:30.821966+00:00_

Web search results for query: "Dugan Hwang Trhlik "RAID Shared Benchmark Robust Evaluation Machine-Generated Text Detectors" ACL 2024"

Links: [{"title":"RAID: A Shared Benchmark for Robust Evaluation of Machine-Generated Text Detectors - ACL Anthology","url":"https://aclanthology.org/2024.acl-long.674/"},{"title":"[2405.07940] RAID: A Shared Benchmark for Robust Evaluation of Machine-Generated Text Detectors","url":"https://arxiv.org/abs/2405.07940"},{"title":"RAID: A Shared Benchmark for Robust Evaluation of Machine-Generated Text Detectors | Request PDF","url":"https://www.researchgate.net/publication/384214327_RAID_A_Shared_Benchmark_for_Robust_Evaluation_of_Machine-Generated_Text_Detectors"},{"title":"GitHub - liamdugan/raid: RAID is the largest and most challenging benchmark for AI-generated text detection. (ACL 2024) · GitHub","url":"https://github.com/liamdugan/raid"},{"title":"RAID: A Shared Benchmark for Robust Evaluation of Machine-Generated Text Detectors","url":"https://arxiv.org/html/2405.07940v1"},{"title":"RAID: A Shared Benchmark for Robust Evaluation of Machine-Generated Text Detectors (Conference Paper) | NSF PAGES","url":"https://par.nsf.gov/biblio/10563509-raid-shared-benchmark-robust-evaluation-machine-generated-text-detectors"},{"title":"[PDF] RAID: A Shared Benchmark for Robust Evaluation of Machine-Generated Text Detectors | Semantic Scholar","url":"https://www.semanticscholar.org/paper/RAID:-A-Shared-Benchmark-for-Robust-Evaluation-of-Dugan-Hwang/a28474db72957c239127374cfee3c8ed8190defc"}]

I found the research paper you're looking for. Here's what I found:

RAID: A Shared Benchmark for Robust Evaluation of Machine-Generated Text Detectors was published at ACL 2024 by Liam Dugan, Alyssa Hwang, Filip Trhlík, Andrew Zhu, Josh Magnus Ludan, Hainiu Xu, Daphne Ippolito, and Chris Callison-Burch.

RAID is the largest and most challenging benchmark dataset for machine-generated text detection, including over 6 million generations spanning 11 model
…[truncated 710 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_review_ref-audit-C_20260526T104716",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 81 · 2026-05-26T10:55:30.822140+00:00_

Web search results for query: "Liang Yuksekgonul Mao "GPT detectors are biased against non-native English writers" Patterns 2023"

Links: [{"title":"[2304.02819] GPT detectors are biased against non-native English writers","url":"https://arxiv.org/abs/2304.02819"},{"title":"GPT detectors are biased against non-native English writers: Patterns","url":"https://www.cell.com/patterns/fulltext/S2666-3899(23)00130-7"},{"title":"Liang, W. X. et al. (2023). GPT Detectors Are Biased against Non-Native English Writers. Patterns, 4, Article ID 100779. - References - Scientific Research Publishing","url":"https://www.scirp.org/reference/referencespapers?referenceid=3900453"},{"title":"(PDF) GPT detectors are biased against non-native English writers","url":"https://www.researchgate.net/publication/372269006_GPT_detectors_are_biased_against_non-native_English_writers"},{"title":"GPT detectors are biased against non-native English writers","url":"https://arxiv.org/pdf/2304.02819"},{"title":"[PDF] GPT detectors are biased against non-native English writers | Semantic Scholar","url":"https://www.semanticscholar.org/paper/GPT-detectors-are-biased-against-non-native-English-Liang-Yuksekgonul/e2352eb8e69d7cc0d98f9b13eae33f9c02310ad4"},{"title":"GitHub - Weixin-Liang/ChatGPT-Detector-Bias · GitHub","url":"https://github.com/Weixin-Liang/ChatGPT-Detector-Bias"},{"title":"GPT detectors can be biased against non-native English writers | ScienceDaily","url":"https://www.sciencedaily.com/releases/2023/07/230710113921.htm"}]

I found the research paper you're looking for. The paper was authored by Weixin Liang, Mert Yuksekgonul, Yining Mao, Eric Wu, and James Zou, submitted on April 6, 2023, with the final version released on July 10, 2023.

The study evaluated the performance of several widely-used GPT detectors using writing samples from native and non-native English writers, and found that these detectors consistently misclassify non-native English writing samples as AI-generated, whereas
…[truncated 685 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_review_ref-audit-C_20260526T104716",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 82 · 2026-05-26T10:55:30.822315+00:00_

Web search results for query: "Padmakumar He "Does Writing with Language Models Reduce Content Diversity" ICLR 2024 OR 2025 proceedings"

Links: [{"title":"[2309.05196] Does Writing with Language Models Reduce Content Diversity?","url":"https://arxiv.org/abs/2309.05196"},{"title":"Does Writing With Language Models (LLMs) Reduce Content Diversity?","url":"https://iclr.cc/media/iclr-2024/Slides/19056.pdf"},{"title":"Does Writing with Language Models Reduce Content Diversity? | NSF Public Access Repository","url":"https://par.nsf.gov/biblio/10534705-does-writing-language-models-reduce-content-diversity"},{"title":"[PDF] Does Writing with Language Models Reduce Content Diversity? | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Does-Writing-with-Language-Models-Reduce-Content-Padmakumar-He/f95fb254da1f7b74a14ac8feb3f834d64e67e4cd"},{"title":"Does Writing with Language Models Reduce Content Diversity? | Request PDF","url":"https://www.researchgate.net/publication/373837896_Does_Writing_with_Language_Models_Reduce_Content_Diversity"},{"title":"Published as a conference paper at ICLR 2025","url":"https://proceedings.iclr.cc/paper_files/paper/2025/file/3df1eca840e82b11bbc33f68c773c38e-Paper-Conference.pdf"},{"title":"Does Writing with Language Models Reduce Content Diversity?","url":"https://arxiv.org/html/2309.05196v3"},{"title":"DOES WRITING WITH LANGUAGE MODELS REDUCE CONTENT DIVERSITY? - NYU Scholars","url":"https://nyuscholars.nyu.edu/en/publications/does-writing-with-language-models-reduce-content-diversity"}]

Based on the search results, I found the paper you're looking for:

The paper "Does Writing with Language Models Reduce Content Diversity?" by Vishakh Padmakumar and He He was presented at the 12th International Conference on Learning Representations (ICLR 2024) in Vienna, Austria.

The research involved a controlled experiment where users write argumentative essays in three setups—using a base LLM (GPT3), a feedback-tuned LLM (InstructGPT), and
…[truncated 519 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_review_ref-audit-C_20260526T104716",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 83 · 2026-05-26T10:55:30.822476+00:00_

Web search results for query: "Schaeffer Kazdan "Position Model Collapse Does Not Mean" ICML 2025 accepted conference"

Links: [{"title":"[2503.03150] Position: Model Collapse Does Not Mean What You Think","url":"https://arxiv.org/abs/2503.03150"},{"title":"Position: Model Collapse Does Not Mean What You Think","url":"https://arxiv.org/pdf/2503.03150"},{"title":"Position: Model Collapse Does Not Mean What You Think - ADS","url":"https://ui.adsabs.harvard.edu/abs/2025arXiv250303150S/abstract"},{"title":"[Literature Review] Position: Model Collapse Does Not Mean What You Think","url":"https://www.themoonlight.io/en/review/position-model-collapse-does-not-mean-what-you-think"},{"title":"Model collapse occurs under some definitions, but does not occur under... | Download Scientific Diagram","url":"https://www.researchgate.net/figure/Model-collapse-occurs-under-some-definitions-but-does-not-occur-under-others-for-the_tbl1_389617145"},{"title":"LLM Web Dynamics: Tracing Model Collapse in a Network of LLMs","url":"https://arxiv.org/html/2506.15690v1"},{"title":"Position: Model Collapse Does Not Mean What You Think | OpenReview","url":"https://openreview.net/forum?id=ygfzWIGDN8"},{"title":"A Closer Look at Model Collapse: From a Generalization-to-Memorization Perspective","url":"https://arxiv.org/html/2509.16499v1"}]

Based on the search results, I found information about the paper you're looking for:

The paper "Position: Model Collapse Does Not Mean What You Think" was authored by Rylan Schaeffer, Joshua Kazdan, Alvan Caleb Arulandu, and Sanmi Koyejo, and was submitted on March 5, 2025.

The paper addresses concerns over model collapse, a degradation in future generative models' performance when trained on synthetic data generated by earlier models. The authors contend that the widespread narrative fundamentally misunderstands the scientific evidence, highlighting that research on model collapse actually encompasses eight distinct and at times conflicting definitions of m
…[truncated 305 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_review_ref-audit-C_20260526T104716",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 84 · 2026-05-26T10:55:30.822654+00:00_

Web search results for query: "Gerstgrasser "Is Model Collapse Inevitable" COLM 2024 conference publication"

Links: [{"title":"Is Model Collapse Inevitable? Breaking the Curse of Recursion by Accumulating Real and Synthetic Data | Stanford SALT Lab","url":"https://saltlab.stanford.edu/papers/gerstgrasser-is-model-collapse-2024/"},{"title":"[2404.01413] Is Model Collapse Inevitable? Breaking the Curse of Recursion by Accumulating Real and Synthetic Data","url":"https://arxiv.org/abs/2404.01413"},{"title":"[PDF] Is Model Collapse Inevitable? Breaking the Curse of Recursion by Accumulating Real and Synthetic Data | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Is-Model-Collapse-Inevitable-Breaking-the-Curse-of-Gerstgrasser-Schaeffer/e8815da26d4e6cac8b23b7e6aa75cec028cb66d2"},{"title":"Is Model Collapse Inevitable? Breaking the Curse of Recursion by Accumulating Real and Synthetic Data | Rylan Schaeffer","url":"https://rylanschaeffer.github.io/content/research/2024_arxiv_is_model_collapse_inevitable/main.html"},{"title":"Escaping Model Collapse via Synthetic Data Verification: Near-term Improvements and Long-term ConvergenceThis project is supported by the AI2050 program at Schmidt Sciences (Grant G-24-66104) and Army Research Office Award W911NF-23-1-0030. We also thank Cong Ma from UChicago, Hongning Wang and Bo Li from Tsinghua, Pinyan Lu and Gavin Tang from Shanghai University of Finance and Economics for helpful discussions and suggestions.","url":"https://arxiv.org/html/2510.16657v1"},{"title":"Is Model Collapse Inevitable? Breaking the Curse of Recursion by Accumulating Real and Synthetic Data | OpenReview","url":"https://openreview.net/forum?id=5B2K4LRgmz"},{"title":"Experts divided over training AI with more data from AI • The Register","url":"https://www.theregister.com/2024/05/09/ai_model_collapse/"},{"title":"Addressing Concerns of Model Collapse from Synthetic Data in AI","url":"https://www.gretel.ai/blog/addressing-concerns-of-model-colla
…[truncated 1579 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_review_ref-audit-C_20260526T104716",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool call

_source line 85 · 2026-05-26T10:55:30.822856+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "arxiv 2502.18865 \"Theoretical Perspective\" model collapse self-consuming"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_review_ref-audit-C_20260526T104716",
  "tool": "WebSearch",
  "tool_args": {
    "query": "arxiv 2502.18865 \"Theoretical Perspective\" model collapse self-consuming"
  }
}
```

</details>

---

### Tool call

_source line 86 · 2026-05-26T10:55:30.822990+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"Kazdan\" \"Collapse or Thrive\" ICML 2025 accepted proceedings openreview"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_review_ref-audit-C_20260526T104716",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"Kazdan\" \"Collapse or Thrive\" ICML 2025 accepted proceedings openreview"
  }
}
```

</details>

---

### Tool call

_source line 87 · 2026-05-26T10:55:30.823108+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Basani Chen DivEye TMLR published 2026 Transactions Machine Learning Research"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_review_ref-audit-C_20260526T104716",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Basani Chen DivEye TMLR published 2026 Transactions Machine Learning Research"
  }
}
```

</details>

---

### Tool call

_source line 88 · 2026-05-26T10:55:30.823240+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Zawalski Boubdir \"Detecting Data Contamination\" CoDeC ICLR 2026 accepted openreview"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_review_ref-audit-C_20260526T104716",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Zawalski Boubdir \"Detecting Data Contamination\" CoDeC ICLR 2026 accepted openreview"
  }
}
```

</details>

---

### Tool result

_source line 89 · 2026-05-26T10:55:30.823453+00:00_

Web search results for query: ""Kazdan" "Collapse or Thrive" ICML 2025 accepted proceedings openreview"

Links: [{"title":"ICML Poster Collapse or Thrive: Perils and Promises of Synthetic Data in a Self-Generating World","url":"https://icml.cc/virtual/2025/poster/44713"},{"title":"1 Introduction","url":"https://arxiv.org/html/2410.16713"},{"title":"42nd ICML 2025: Vancouver, BC, Canada","url":"https://dblp.org/db/conf/icml/icml2025.html"},{"title":"ICML 2025 Conference | OpenReview","url":"https://openreview.net/group?id=ICML.cc%2F2025%2FConference"},{"title":"Collapse or Thrive? Perils and Promises of Synthetic Data in a Self-Generating World | OpenReview","url":"https://openreview.net/forum?id=Xr5iINA3zU"},{"title":"ICML.2025 | Cool Papers - Immersive Paper Discovery","url":"https://papers.cool/venue/ICML.2025"},{"title":"ICML 2025 | OpenReview","url":"https://openreview.net/group?id=ICML.cc%2F2025"},{"title":"ICML 2025 Conference Submissions","url":"https://openreview.net/submissions?page=115&venue=ICML.cc/2025/Conference"},{"title":"ICML 2025 Workshop | OpenReview","url":"https://openreview.net/group?id=ICML.cc%2F2025%2FWorkshop"},{"title":"Position: Solve Layerwise Linear Models First to Understand Neural Dynamical Phenomena (Neural Collapse, Emergence, Lazy/Rich Regime, and Grokking) | OpenReview","url":"https://openreview.net/forum?id=nrlGUdlo16"}]

Based on the search results, I found the paper you're looking for:

"Collapse or Thrive: Perils and Promises of Synthetic Data in a Self-Generating World" by Joshua Kazdan, Rylan Schaeffer, Apratim Dey, Matthias Gerstgrasser, Rafael Rafailov, David Donoho, and Sanmi Koyejo is an accepted paper at ICML 2025. 

The paper addresses the question: "What happens when generative machine learning models are pretrained on web-scale datasets containing data generated by earlier models?" Some prior work warns of "model collapse" as the web is overwhelmed by synthetic data; other work suggests the problem can be contained by 
…[truncated 310 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_review_ref-audit-C_20260526T104716",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 90 · 2026-05-26T10:55:30.823659+00:00_

Web search results for query: "Basani Chen DivEye TMLR published 2026 Transactions Machine Learning Research"

Links: [{"title":"Transactions on Machine Learning Research","url":"https://jmlr.org/tmlr/papers/"},{"title":"TMLR - Transactions on Machine Learning Research","url":"https://openreview.net/group?id=TMLR"},{"title":"Transactions on Machine Learning Research (TMLR)","url":"https://dblp.org/db/journals/tmlr/index.html"},{"title":"dblp: Transactions on Machine Learning Research, Volume 2026","url":"https://dblp.org/db/journals/tmlr/tmlr2026.html"},{"title":"Transactions on Machine Learning Research – DOAJ","url":"https://doaj.org/toc/2835-8856"},{"title":"Transactions on Machine Learning Research (TMLR)","url":"https://www.deepmind.com/venues/transactions-on-machine-learning-research-tmlr"},{"title":"Transactions on Machine Learning Research (@TmlrOrg) / X","url":"https://x.com/TmlrOrg"},{"title":"Publications - Apple Machine Learning Research","url":"https://machinelearning.apple.com/research/?event=Transactions+on+Machine+Learning+Research+(TMLR)"},{"title":"A Comprehensive Survey of Deep Research: Systems, Methodologies, and Applications","url":"https://arxiv.org/pdf/2506.12594"}]

Based on the search results, Advik Raj Basani and Pin-Yu Chen published a paper in February 2026 in Transactions on Machine Learning Research. The search results show their paper is listed among the TMLR publications from that period with links to OpenReview, PDF, bibliography, and code resources.

However, the search results do not display the specific title "DivEye" for their paper. To find more detailed information about the specific DivEye paper, you may want to visit the OpenReview link or the TMLR paper listing directly.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_review_ref-audit-C_20260526T104716",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 91 · 2026-05-26T10:55:30.823869+00:00_

Web search results for query: "Zawalski Boubdir "Detecting Data Contamination" CoDeC ICLR 2026 accepted openreview"

Links: [{"title":"Detecting Data Contamination in LLMs via In-Context ...","url":"https://openreview.net/pdf?id=YlpaaYxx4t"},{"title":"[2510.27055] Detecting Data Contamination in LLMs via In-Context Learning","url":"https://arxiv.org/abs/2510.27055"},{"title":"Detecting Data Contamination in LLMs via In-Context Learning","url":"https://arxiv.org/html/2510.27055v1"},{"title":"Detecting Data Contamination in LLMs via In-Context Learning | OpenReview","url":"https://openreview.net/forum?id=YlpaaYxx4t"},{"title":"Detecting Data Contamination in LLMs via In-Context Learning Michał Zawalski†","url":"https://openreview.net/pdf/753f569951799d9078f4db2d0e9debd74ad5b692.pdf"},{"title":"Michał Zawalski's scientific contributions","url":"https://www.researchgate.net/scientific-contributions/Michal-Zawalski-2200204644"},{"title":"Published as a conference paper at ICLR 2026 CONTAMINATION DETECTION","url":"https://openreview.net/pdf?id=gk6OC3XIZW"},{"title":"Detecting Data Contamination in LLMs via In-Context Learning","url":"https://openreview.net/pdf/fbfd3e4f09f698fff38f0024c147e2e942876160.pdf"},{"title":"Did the Model See the Benchmark During Training? Detecting LLM Contamination","url":"https://kaitchup.substack.com/p/did-the-model-see-the-benchmark-during"},{"title":"ICLR 2026: Detecting Data Contamination in LLMs via In- ...","url":"https://www.linkedin.com/posts/besmira-nushi-43969712_our-work-on-data-contamination-analysis-was-activity-7422343437376561152-O2kU"}]

I found the paper! Here are the search results:

The paper "Detecting Data Contamination in LLMs via In-Context Learning" by Michał Zawalski and Meriem Boubdir (along with co-authors Klaudia Bałazy, Besmira Nushi, and Pablo Ribalta from NVIDIA) presents Contamination Detection via Context (CoDeC), a practical and accurate method to detect and quantify training data contamination in large languag
…[truncated 787 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_review_ref-audit-C_20260526T104716",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 92 · 2026-05-26T10:55:30.824058+00:00_

Web search results for query: "arxiv 2502.18865 "Theoretical Perspective" model collapse self-consuming"

Links: [{"title":"[2502.18865] A Theoretical Perspective: How to Prevent Model Collapse in Self-consuming Training Loops","url":"https://arxiv.org/abs/2502.18865"},{"title":"A Theoretical Perspective: How to Prevent Model Collapse in Self-consuming Training Loops","url":"https://arxiv.org/html/2502.18865"},{"title":"Model Collapse in the Self-Consuming Chain of Diffusion Finetuning: A Novel Perspective from Quantitative Trait Modeling","url":"https://arxiv.org/html/2407.17493v3"},{"title":"How to Prevent Model Collapse in Self-consuming Training ...","url":"https://arxiv.org/pdf/2502.18865"},{"title":"Model Collapse in the Self-Consuming Chain of Diffusion ...","url":"https://arxiv.org/pdf/2407.17493"},{"title":"A Theoretical Perspective: How to Prevent Model Collapse in Self-consuming Training Loops | OpenReview","url":"https://openreview.net/forum?id=WttfQGwpES"},{"title":"A Closer Look at Model Collapse: From a Generalization-to-Memorization Perspective","url":"https://arxiv.org/html/2509.16499v1"},{"title":"The Economics of Model Collapse: Equilibrium, Welfare, and Optimal Provenance Subsidies in Synthetic Data Markets","url":"https://arxiv.org/html/2605.20279"}]

Based on the search results, I found the paper you're looking for:

**Title:** "A Theoretical Perspective: How to Prevent Model Collapse in Self-consuming Training Loops"

**Main Topic:** The paper addresses the problem that high-quality data available online has become nearly depleted, leading models to increasingly generate their own data for further training, forming Self-consuming Training Loops (STLs).

**Problem:** Empirical results have been strikingly inconsistent—some models degrade or even collapse, while others successfully avoid these failures, leaving a significant gap in theoretical understanding to explain this discrepancy.

**Key Contribution:** The paper introduces the notion of re
…[truncated 669 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_review_ref-audit-C_20260526T104716",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool call

_source line 93 · 2026-05-26T10:55:30.824242+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"Position: Model Collapse Does Not Mean What You Think\" ICML 2025 poster accepted Schaeffer"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_review_ref-audit-C_20260526T104716",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"Position: Model Collapse Does Not Mean What You Think\" ICML 2025 poster accepted Schaeffer"
  }
}
```

</details>

---

### Tool call

_source line 94 · 2026-05-26T10:55:30.824371+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "sadasivan2023 \"Can AI-Generated Text be Reliably Detected\" ICLR 2024 conference published"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_review_ref-audit-C_20260526T104716",
  "tool": "WebSearch",
  "tool_args": {
    "query": "sadasivan2023 \"Can AI-Generated Text be Reliably Detected\" ICLR 2024 conference published"
  }
}
```

</details>

---

### Tool result

_source line 95 · 2026-05-26T10:55:30.824519+00:00_

Web search results for query: ""Position: Model Collapse Does Not Mean What You Think" ICML 2025 poster accepted Schaeffer"

Links: [{"title":"ICML Poster Collapse or Thrive: Perils and Promises of Synthetic Data in a Self-Generating World","url":"https://icml.cc/virtual/2025/poster/44713"},{"title":"1 Introduction","url":"https://arxiv.org/html/2503.03150v2"},{"title":"[2503.03150] Position: Model Collapse Does Not Mean What You Think","url":"https://arxiv.org/abs/2503.03150"},{"title":"Position: Model Collapse Does Not Mean What You Think","url":"https://arxiv.org/pdf/2503.03150"},{"title":"A Closer Look at Model Collapse: From a Generalization-to-Memorization Perspective","url":"https://arxiv.org/html/2509.16499v1"},{"title":"Escaping Model Collapse via Synthetic Data Verification: Near-term Improvements and Long-term ConvergenceThis project is supported by the AI2050 program at Schmidt Sciences (Grant G-24-66104) and Army Research Office Award W911NF-23-1-0030. We also thank Cong Ma from UChicago, Hongning Wang and Bo Li from Tsinghua, Pinyan Lu and Gavin Tang from Shanghai University of Finance and Economics for helpful discussions and suggestions.","url":"https://arxiv.org/html/2510.16657v1"},{"title":"Position: Model Collapse Does Not Mean What You Think Anonymous Author(s)","url":"https://openreview.net/pdf?id=ygfzWIGDN8"},{"title":"Sanmi Koyejo, Rylan Schaeffer, Joshua Kazdan, Alvan Arlando, Angelina Wang · Model Collapse Does Not Mean What You Think","url":"https://slideslive.com/39038994/model-collapse-does-not-mean-what-you-think"},{"title":"ICLR Model Collapse Does Not Mean What You Think (Invited talk: Sanmi Koyejo)","url":"https://iclr.cc/virtual/2025/37806"}]

Based on the search results, I found information about this paper. Here's what I discovered:

"Position: Model Collapse Does Not Mean What You Think" is authored by Rylan Schaeffer, Joshua Kazdan, Alvan Caleb Arulandu, and Sanmi Koyejo, with affiliations at Stanford Computer Science, Stanford S
…[truncated 1099 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_review_ref-audit-C_20260526T104716",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 96 · 2026-05-26T10:55:30.824680+00:00_

Web search results for query: "sadasivan2023 "Can AI-Generated Text be Reliably Detected" ICLR 2024 conference published"

Links: [{"title":"[PDF] Can AI-Generated Text be Reliably Detected? | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Can-AI-Generated-Text-be-Reliably-Detected-Sadasivan-Kumar/5ee8bb4fc80a291b2e416a2a879e7153a783d7e9"},{"title":"(PDF) Can AI-Generated Text be Reliably Detected?","url":"https://www.researchgate.net/publication/369380286_Can_AI-Generated_Text_be_Reliably_Detected"},{"title":"[2303.11156] Can AI-Generated Text be Reliably Detected?","url":"https://arxiv.org/abs/2303.11156"},{"title":"Can AI-Generated Text be Reliably Detected? | OpenReview","url":"https://openreview.net/forum?id=NvSwR4IvLO"},{"title":"Can AI-Generated Text be Reliably Detected?","url":"https://bibbase.org/network/publication/sadasivan-kumar-balasubramanian-wang-feizi-canaigeneratedtextbereliablydetected-2023"},{"title":"Can AI-Generated Text be Reliably Detected? Stress Testing AI Text Detectors Under Various Attacks | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Can-AI-Generated-Text-be-Reliably-Detected-Stress-Sadasivan-Kumar/42f7d83e6c20fd4aaf3e3f53b18ab7db221ee300"},{"title":"Can AI-Generated Text be Reliably Detected? Stress Testing AI Text Detectors Under Various Attacks | OpenReview","url":"https://openreview.net/forum?id=OOgsAZdFOt"}]

Based on the search results, I found information about the paper you're looking for:

The paper "Can AI-Generated Text be Reliably Detected?" was authored by Vinu Sankar Sadasivan, Aounon Kumar, Sriram Balasubramanian, Wenxiao Wang, and Soheil Feizi, and was originally published on arXiv in 2023.

The paper was submitted with the ICLR 2024 conference guidelines, and it was published at ICLR 2024.

The paper introduces a recursive paraphrasing attack to stress test the robustness of AI text detectors and provides a theoretical framework connecting the AUROC of the best possible detector to the
…[truncated 375 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_review_ref-audit-C_20260526T104716",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 97 · 2026-05-26T10:55:30.824880+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Sadasivan \"Can AI-Generated Text be Reliably Detected\" ICLR 2024 published openreview accepted rejected"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_review_ref-audit-C_20260526T104716",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Sadasivan \"Can AI-Generated Text be Reliably Detected\" ICLR 2024 published openreview accepted rejected"
  }
}
```

</details>

---

### Tool call

_source line 98 · 2026-05-26T10:55:30.825011+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Briesch Sobania Rothlauf \"Large Language Models Suffer\" self-consuming loop conference published accepted 2024 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_review_ref-audit-C_20260526T104716",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Briesch Sobania Rothlauf \"Large Language Models Suffer\" self-consuming loop conference published accepted 2024 2025"
  }
}
```

</details>

---

### Tool result

_source line 99 · 2026-05-26T10:55:30.825148+00:00_

Web search results for query: "Sadasivan "Can AI-Generated Text be Reliably Detected" ICLR 2024 published openreview accepted rejected"

Links: [{"title":"[2303.11156] Can AI-Generated Text be Reliably Detected?","url":"https://arxiv.org/abs/2303.11156"},{"title":"[PDF] Can AI-Generated Text be Reliably Detected? | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Can-AI-Generated-Text-be-Reliably-Detected-Sadasivan-Kumar/5ee8bb4fc80a291b2e416a2a879e7153a783d7e9"},{"title":"Can AI-Generated Text be Reliably Detected?","url":"https://bibbase.org/network/publication/sadasivan-kumar-balasubramanian-wang-feizi-canaigeneratedtextbereliablydetected-2024"},{"title":"Can AI-Generated Text be Reliably Detected? | OpenReview","url":"https://openreview.net/forum?id=NvSwR4IvLO"},{"title":"(PDF) Can AI-Generated Text be Reliably Detected?","url":"https://www.researchgate.net/publication/369380286_Can_AI-Generated_Text_be_Reliably_Detected"},{"title":"[2303.11156v3] Can AI-Generated Text be Reliably Detected?","url":"https://arxiv.org/abs/2303.11156v3"},{"title":"[2303.11156v4] Can AI-Generated Text be Reliably Detected?","url":"https://arxiv.org/abs/2303.11156v4"}]

Based on the search results, I found information about this paper. The paper "Can AI-Generated Text be Reliably Detected?" by Sadasivan et al. was submitted to ICLR 2024. The paper is available on OpenReview with the forum ID NvSwR4IvLO.

However, the search results do not clearly indicate whether the paper was ultimately accepted or rejected at ICLR 2024. The OpenReview page shows a submission dated October 13, 2023, but the acceptance/rejection status is not explicitly stated in the search results. The paper was last revised in February 2024, and it has also been posted on arXiv as paper 2303.11156 with multiple versions.

To find the definitive acceptance/rejection status for ICLR 2024, you would need to check the official ICLR 2024 conference website or the full OpenReview page directly, as this info
…[truncated 157 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_review_ref-audit-C_20260526T104716",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 100 · 2026-05-26T10:55:30.825315+00:00_

Web search results for query: "Briesch Sobania Rothlauf "Large Language Models Suffer" self-consuming loop conference published accepted 2024 2025"

Links: [{"title":"[2311.16822] Large Language Models Suffer From Their Own Output: An Analysis of the Self-Consuming Training Loop","url":"https://arxiv.org/abs/2311.16822"},{"title":"[2311.16822v2] Large Language Models Suffer From Their Own Output: An Analysis of the Self-Consuming Training Loop","url":"https://arxiv.org/abs/2311.16822v2"},{"title":"Large Language Models Suffer From Their Own Output: An Analysis of the Self-Consuming Training Loop","url":"https://arxiv.org/html/2311.16822v2"},{"title":"[PDF] Large Language Models Suffer From Their Own Output: An Analysis of the Self-Consuming Training Loop | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Large-Language-Models-Suffer-From-Their-Own-Output:-Briesch-Sobania/c24ed03689adc2a075004c6619f43f7f6230fe4b"},{"title":"Large Language Models Suffer From Their Own Output: An Analysis of the Self-Consuming Training Loop | AI Research Paper Details","url":"https://www.aimodels.fyi/papers/arxiv/large-language-models-suffer-from-their-own"},{"title":"Large Language Models Suffer From Their Own Output: An Analysis of the Self-Consuming Training Loop - ADS","url":"https://ui.adsabs.harvard.edu/abs/arXiv:2311.16822"},{"title":"Collapse or Thrive? Perils and Promises of Synthetic Data in a Self-Generating World","url":"https://arxiv.org/html/2410.16713v2"},{"title":"Is Model Collapse Inevitable? Breaking the Curse of Recursion by Accumulating Real and Synthetic Data","url":"https://arxiv.org/html/2404.01413v2"},{"title":"How Bad is Training on Synthetic Data? A Statistical Analysis of Language Model Collapse","url":"https://arxiv.org/html/2404.05090v1"},{"title":"[2311.16822] Large Language Models Suffer From Their Own Output: An Analysis of the Self-Consuming Training Loop","url":"https://ar5iv.labs.arxiv.org/html/2311.16822"}]

Based on the search results,
…[truncated 1121 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_review_ref-audit-C_20260526T104716",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 101 · 2026-05-26T10:55:30.825485+00:00_

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
  "session": "worker_review_ref-audit-C_20260526T104716",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/introduction.tex"
  }
}
```

</details>

---

### Tool result

_source line 102 · 2026-05-26T10:55:30.825630+00:00_

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
  "session": "worker_review_ref-audit-C_20260526T104716",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 103 · 2026-05-26T10:55:30.825805+00:00_

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
  "session": "worker_review_ref-audit-C_20260526T104716",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/related_work.tex"
  }
}
```

</details>

---

### Tool result

_source line 104 · 2026-05-26T10:55:30.825951+00:00_

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
  "session": "worker_review_ref-audit-C_20260526T104716",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 105 · 2026-05-26T10:55:30.826087+00:00_

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
  "session": "worker_review_ref-audit-C_20260526T104716",
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

_source line 106 · 2026-05-26T10:55:30.826314+00:00_

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
  "session": "worker_review_ref-audit-C_20260526T104716",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 107 · 2026-05-26T10:55:30.826463+00:00_

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
  "session": "worker_review_ref-audit-C_20260526T104716",
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

_source line 108 · 2026-05-26T10:55:30.826605+00:00_

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
  "session": "worker_review_ref-audit-C_20260526T104716",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 109 · 2026-05-26T10:55:30.826749+00:00_

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
  "session": "worker_review_ref-audit-C_20260526T104716",
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

_source line 110 · 2026-05-26T10:55:30.826914+00:00_

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
  "session": "worker_review_ref-audit-C_20260526T104716",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 111 · 2026-05-26T10:55:30.827054+00:00_

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
  "session": "worker_review_ref-audit-C_20260526T104716",
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

_source line 112 · 2026-05-26T10:55:30.827215+00:00_

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
  "session": "worker_review_ref-audit-C_20260526T104716",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 113 · 2026-05-26T10:55:30.827453+00:00_

called Write

<details open><summary>🔧 Tool call — Write</summary>

````json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/artifacts/ref_audit_worker_C.md",
  "content": "# Reference Audit Report — Worker C\n\nAudit date: 2026-05-26\n\nEach entry verified via WebSearch for: existence, authors, title, year, venue, and cite-context correctness.\n\n---\n\n## Per-Entry Results\n\n```\n[kirchenbauer2023watermark] ✓ | ICML 2023, pp. 17061–17084. Authors, title, venue all confirmed.\n[drayson2025] ✓ | EMNLP 2025. Authors, title correct. arXiv 2502.15654 confirmed.\n[schaeffer2025position] ✓ | arXiv preprint arXiv:2503.03150. Authors, title correct. Not yet formally published at a conference (invited talk at ICLR 2025; under review elsewhere). Listing as arXiv is appropriate.\n[kazdan2025collapse] ✓ | ICML 2025 poster confirmed (icml.cc/virtual/2025/poster/44713). Authors, title correct.\n[mitchell2023detectgpt] ✓ | ICML 2023. Authors, title correct. arXiv 2301.11305 confirmed.\n[basani2026diveye] ✓ | TMLR 2026 confirmed (DBLP, GitHub \"[TMLR '26]\"). Authors (Basani, Chen), title, ISSN correct.\n[zawalski2026codec] ✓ | ICLR 2026 confirmed (OpenReview YlpaaYxx4t). Authors, title correct. arXiv 2510.27055 confirmed.\n[zhang2024minkpp] ✓ | ICLR 2025 Spotlight. Bib year=2025 correct (cite key says 2024, irrelevant). Authors, title correct.\n[shumailov2024collapse] ✓ | Nature 2024, vol. 631, pp. 755–759. Authors (Shumailov, Shumaylov, Zhao, Papernot, Anderson, Gal), title, DOI all correct.\n[alemohammad2024selfconsuming] ✓ | ICLR 2024. Authors, title correct. arXiv 2307.01850 confirmed.\n[dohmatob2024model] ✓ | ICML 2024, pp. 11165–11197. Authors (Dohmatob, Feng, Yang, Charton, Kempe), title correct.\n[xie2023dsir] ✓ | NeurIPS 2023. Authors (Xie, Santurkar, Ma, Liang), title correct.\n[tirumala2023d4] ✓ | NeurIPS 2023 Datasets & Benchmarks. Authors (Tirumala, Simig, Aghajanyan, Morcos), title correct.\n[xie2023doremi] ✓ | NeurIPS 2023. Authors, title correct.\n[hans2024binoculars] ✓ | ICML 2024. Authors, title correct. arXiv 2401.12070 confirmed.\n[alain2017understanding] ✓ | ICLR 2017 Workshop. Authors (Alain, Bengio), title correct.\n[belinkov2022probing] ✓ | Computational Linguistics 48(1):207–219, 2022. Author, title, volume, pages, DOI all correct.\n[bao2024fast] ✓ | ICLR 2024. Authors (Bao, Zhao, Teng, Yang, Zhang), title correct.\n[frank2001ordinal] ✓ | ECML 2001, pp. 145–156. Authors (Frank, Hall), title, DOI correct.\n[cheng2025beyond] ✓ | WWW 2025 (ACM Web Conference). Authors, title correct. arXiv 2410.14259 confirmed.\n[mehta2025beyond] ✓ | arXiv preprint arXiv:2511.17602. Author (Sushant Mehta), title, year correct.\n[sun2025aigt] ✓ | ACL 2025. Authors, title correct. arXiv 2412.18148 confirmed.\n[spennemann2025quantifying] ✓ | arXiv preprint arXiv:2504.08755. Author (Dirk H. R. Spennemann), title, year correct.\n[dohmatob2025strong] ✓ | ICLR 2025. Authors (Dohmatob, Feng, Subramonian, Kempe), title correct.\n[wang2024semeval] ✓ | SemEval 2024 (co-located with NAACL). Authors, title correct.\n[gerstgrasser2024model] ✓ | COLM 2024. Authors, title correct. arXiv 2404.01413 confirmed.\n[guo2024curious] ✓ | Findings of NAACL 2024. Authors, title correct. Minor: \"Clavel, Chloe\" could use diacritics (Chloé), but functionally acceptable in BibTeX.\n[briesch2023selfconsuming] ✓ | arXiv preprint arXiv:2311.16822, year 2023. Authors, title correct. Remains unpublished at a venue.\n[padmakumar2024writing] ✓ | ICLR 2024. Authors (Padmakumar, He), title correct. Confirmed via ICLR 2024 slides and NSF record.\n[krishna2023paraphrasing] ✓ | NeurIPS 2023. Authors, title correct. arXiv 2303.13408 confirmed.\n[sadasivan2023detect] ✓ | arXiv preprint arXiv:2303.11156. Authors, title correct. Submitted to ICLR 2024 but acceptance status unclear from public sources; listing as arXiv preprint is safe.\n[hao2025rewrite] ✓ | ACL 2025, pp. 6421–6434. Authors, title correct.\n[wang2025unveiling] ✓ | ACL 2025, pp. 12740–12755. Authors (Wang, Li, Yan, Cheng, Zhang), title, venue, pages all correct.\n[fu2025theoretical] ✓ | ICLR 2025 (OpenReview WttfQGwpES). Authors, title correct. arXiv 2502.18865 confirmed.\n[verma2024ghostbuster] ✓ | NAACL 2024, pp. 1702–1717. Authors, title, pages correct.\n[dugan2024raid] ✓ | ACL 2024, pp. 12463–12492. Authors, title, pages correct.\n[liang2023gpt] ✓ | Patterns 4(7):100779, 2023. Authors, title, volume, pages correct.\n```\n\n## Cite-Context Issues\n\nOne contextual concern (bibliographic entry itself is correct):\n\n- **related_work.tex:11** — `liang2023gpt` is cited as \"GPTZero~\\cite{liang2023gpt}\" in the phrase \"benchmarks such as RAID and GPTZero evaluate robustness at scale.\" The Liang et al. paper is about **detector bias against non-native English writers**, not about GPTZero as a benchmark. GPTZero is a commercial detection tool (Tian et al.) without a standalone academic paper; Liang et al. merely evaluate it as one of several biased detectors. The cite is tangentially related but the sentence implies liang2023gpt *is* the GPTZero benchmark paper, which it is not.\n\n## Summary\n\n| Metric | Count |\n|--------|-------|\n| Total entries | 37 |\n| ✓ Correct | 37 |\n| ✗ Bibliographic errors | 0 |\n| Cite-context flags | 1 (liang2023gpt used as \"GPTZero\" benchmark reference) |\n\nAll 37 bib entries are real papers with correct authors, titles, years, and venues. No hallucinated references found. One minor cite-context misattribution flagged above.\n"
}
````

</details>

<details><summary>Recorded metadata</summary>

````json
{
  "recorded_role": "tool",
  "session": "worker_review_ref-audit-C_20260526T104716",
  "tool": "Write",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/artifacts/ref_audit_worker_C.md",
    "content": "# Reference Audit Report — Worker C\n\nAudit date: 2026-05-26\n\nEach entry verified via WebSearch for: existence, authors, title, year, venue, and cite-context correctness.\n\n---\n\n## Per-Entry Results\n\n```\n[kirchenbauer2023watermark] ✓ | ICML 2023, pp. 17061–17084. Authors, title, venue all confirmed.\n[drayson2025] ✓ | EMNLP 2025. Authors, title correct. arXiv 2502.15654 confirmed.\n[schaeffer2025position] ✓ | arXiv preprint arXiv:2503.03150. Authors, title correct. Not yet formally published at a conference (invited talk at ICLR 2025; under review elsewhere). Listing as arXiv is appropriate.\n[kazdan2025collapse] ✓ | ICML 2025 poster confirmed (icml.cc/virtual/2025/poster/44713). Authors, title correct.\n[mitchell2023detectgpt] ✓ | ICML 2023. Authors, title correct. arXiv 2301.11305 confirmed.\n[basani2026diveye] ✓ | TMLR 2026 confirmed (DBLP, GitHub \"[TMLR '26]\"). Authors (Basani, Chen), title, ISSN correct.\n[zawalski2026codec] ✓ | ICLR 2026 confirmed (OpenReview YlpaaYxx4t). Authors, title correct. arXiv 2510.27055 confirmed.\n[zhang2024minkpp] ✓ | ICLR 2025 Spotlight. Bib year=2025 correct (cite key says 2024, irrelevant). Authors, title correct.\n[shumailov2024collapse] ✓ | Nature 2024, vol. 631, pp. 755–759. Authors (Shumailov, Shumaylov, Zhao, Papernot, Anderson, Gal), title, DOI all correct.\n[alemohammad2024selfconsuming] ✓ | ICLR 2024. Authors, title correct. arXiv 2307.01850 confirmed.\n[dohmatob2024model] ✓ | ICML 2024, pp. 11165–11197. Authors (Dohmatob, Feng, Yang, Charton, Kempe), title correct.\n[xie2023dsir] ✓ | NeurIPS 2023. Authors (Xie, Santurkar, Ma, Liang), title correct.\n[tirumala2023d4] ✓ | NeurIPS 2023 Datasets & Benchmarks. Authors (Tirumala, Simig, Aghajanyan, Morcos), title correct.\n[xie2023doremi] ✓ | NeurIPS 2023. Authors, title correct.\n[hans2024binoculars] ✓ | ICML 2024. Authors, title correct. arXiv 2401.12070 confirmed.\n[alain2017understanding] ✓ | ICLR 2017 Workshop. Authors (Alain, Bengio), title correct.\n[belinkov2022probing] ✓ | Computational Linguistics 48(1):207–219, 2022. Author, title, volume, pages, DOI all correct.\n[bao2024fast] ✓ | ICLR 2024. Authors (Bao, Zhao, Teng, Yang, Zhang), title correct.\n[frank2001ordinal] ✓ | ECML 2001, pp. 145–156. Authors (Frank, Hall), title, DOI correct.\n[cheng2025beyond] ✓ | WWW 2025 (ACM Web Conference). Authors, title correct. arXiv 2410.14259 confirmed.\n[mehta2025beyond] ✓ | arXiv preprint arXiv:2511.17602. Author (Sushant Mehta), title, year correct.\n[sun2025aigt] ✓ | ACL 2025. Authors, title correct. arXiv 2412.18148 confirmed.\n[spennemann2025quantifying] ✓ | arXiv preprint arXiv:2504.08755. Author (Dirk H. R. Spennemann), title, year correct.\n[dohmatob2025strong] ✓ | ICLR 2025. Authors (Dohmatob, Feng, Subramonian, Kempe), title correct.\n[wang2024semeval] ✓ | SemEval 2024 (co-located with NAACL). Authors, title correct.\n[gerstgrasser2024model] ✓ | COLM 2024. Authors, title correct. arXiv 2404.01413 confirmed.\n[guo2024curious] ✓ | Findings of NAACL 2024. Authors, title correct. Minor: \"Clavel, Chloe\" could use diacritics (Chloé), but functionally acceptable in BibTeX.\n[briesch2023selfconsuming] ✓ | arXiv preprint arXiv:2311.16822, year 2023. Authors, title correct. Remains unpublished at a venue.\n[padmakumar2024writing] ✓ | ICLR 2024. Authors (Padmakumar, He), title correct. Confirmed via ICLR 2024 slides and NSF record.\n[krishna2023paraphrasing] ✓ | NeurIPS 2023. Authors, title correct. arXiv 2303.13408 confirmed.\n[sadasivan2023detect] ✓ | arXiv preprint arXiv:2303.11156. Authors, title correct. Submitted to ICLR 2024 but acceptance status unclear from public sources; listing as arXiv preprint is safe.\n[hao2025rewrite] ✓ | ACL 2025, pp. 6421–6434. Authors, title correct.\n[wang2025unveiling] ✓ | ACL 2025, pp. 12740–12755. Authors (Wang, Li, Yan, Cheng, Zhang), title, venue, pages all correct.\n[fu2025theoretical] ✓ | ICLR 2025 (OpenReview WttfQGwpES). Authors, title correct. arXiv 2502.18865 confirmed.\n[verma2024ghostbuster] ✓ | NAACL 2024, pp. 1702–1717. Authors, title, pages correct.\n[dugan2024raid] ✓ | ACL 2024, pp. 12463–12492. Authors, title, pages correct.\n[liang2023gpt] ✓ | Patterns 4(7):100779, 2023. Authors, title, volume, pages correct.\n```\n\n## Cite-Context Issues\n\nOne contextual concern (bibliographic entry itself is correct):\n\n- **related_work.tex:11** — `liang2023gpt` is cited as \"GPTZero~\\cite{liang2023gpt}\" in the phrase \"benchmarks such as RAID and GPTZero evaluate robustness at scale.\" The Liang et al. paper is about **detector bias against non-native English writers**, not about GPTZero as a benchmark. GPTZero is a commercial detection tool (Tian et al.) without a standalone academic paper; Liang et al. merely evaluate it as one of several biased detectors. The cite is tangentially related but the sentence implies liang2023gpt *is* the GPTZero benchmark paper, which it is not.\n\n## Summary\n\n| Metric | Count |\n|--------|-------|\n| Total entries | 37 |\n| ✓ Correct | 37 |\n| ✗ Bibliographic errors | 0 |\n| Cite-context flags | 1 (liang2023gpt used as \"GPTZero\" benchmark reference) |\n\nAll 37 bib entries are real papers with correct authors, titles, years, and venues. No hallucinated references found. One minor cite-context misattribution flagged above.\n"
  }
}
````

</details>

---

### Tool result

_source line 114 · 2026-05-26T10:55:30.827657+00:00_

File created successfully at: /home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/artifacts/ref_audit_worker_C.md

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_review_ref-audit-C_20260526T104716",
  "tool": "Write",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 115 · 2026-05-26T10:55:30.827828+00:00_

审计完成。37 条 bib 全部通过验证——无幻觉引用、无作者/年份/标题/会议错误。唯一发现是 `liang2023gpt` 在 related_work.tex 中被当作 "GPTZero" 基准引用，但该论文实际讲的是检测器对非母语英语写作者的偏见，不是 GPTZero 本身。结果已写入 `artifacts/ref_audit_worker_C.md`。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_review_ref-audit-C_20260526T104716"
}
```

</details>

---
