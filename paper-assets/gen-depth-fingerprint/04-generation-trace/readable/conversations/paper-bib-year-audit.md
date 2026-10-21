# paper bib year audit

**Depth Profiling: Classifying Recursive Generation Depth in Base-Model LLM Text** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 99
- **Recorded user turns:** 0
- **Tool calls:** 49
- **Original source:** `logs/chats/worker_paper_bib-year-audit_20260515T174748.jsonl`
- **Structured JSON:** [`f9b555dd48356e307826.json`](../../sessions/f9/f9b555dd48356e307826.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

99 recorded events

### Tool call

_source line 1 · 2026-05-15T17:54:07.226737+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/references.bib"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_bib-year-audit_20260515T174748",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/references.bib"
  }
}
```

</details>

---

### Tool result

_source line 2 · 2026-05-15T17:54:07.227101+00:00_

1	% ===== Detection =====
2	
3	@inproceedings{detectgpt,
4	  title = {{DetectGPT: Zero-Shot Machine-Generated Text Detection using Probability Curvature}},
5	  author = {Mitchell, Eric and Lee, Yoonho and Khazatsky, Alexander and Manning, Christopher D. and Finn, Chelsea},
6	  booktitle = {Proceedings of the International Conference on Machine Learning},
7	  year = {2023},
8	}
9	
10	@inproceedings{gltr,
11	  title = {{GLTR: Statistical Detection and Visualization of Generated Text}},
12	  author = {Gehrmann, Sebastian and Strobelt, Hendrik and Rush, Alexander M.},
13	  booktitle = {Proceedings of the Annual Meeting of the Association for Computational Linguistics},
14	  year = {2019},
15	}
16	
17	@inproceedings{dna_gpt,
18	  title = {{DNA-GPT: Divergent N-Gram Analysis for Training-Free Detection of GPT-Generated Text}},
19	  author = {Yang, Xianjun and Cheng, Wei and Wu, Yue and Petzold, Linda and Wang, William Yang and Chen, Haifeng},
20	  booktitle = {Proceedings of the International Conference on Learning Representations},
21	  year = {2024},
22	}
23	
24	@inproceedings{binoculars,
25	  title = {{Spotting LLMs With Binoculars: Zero-Shot Detection of Machine-Generated Text}},
26	  author = {Hans, Abhimanyu and Schwarzschild, Avi and Cherepanova, Valeriia and Kazemi, Hamid and Saha, Aniruddha and Goldblum, Micah and Geiping, Jonas and Goldstein, Tom},
27	  booktitle = {Proceedings of the International Conference on Machine Learning},
28	  year = {2024},
29	}
30	
31	@inproceedings{fast_detectgpt,
32	  title = {{Fast-DetectGPT: Efficient Zero-Shot Detection of Machine-Generated Text via Conditional Probability Curvature}},
33	  author = {Bao, Guangsheng and Zhao, Yanbin and Teng, Zhiyang and Yang, Linyi and Zhang, Yue},
34	  booktitle = {Proceedings of the International Conference on Learning Representations},
35	  year = {2024},
36	}
37	
38	@article{ld_score,
39	  title = {{Beyond Perplexity: Character Distribution Signatures and the MDTA Benchmark for AI Text Detec
…[truncated 16718 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_bib-year-audit_20260515T174748",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-15T17:54:07.227276+00:00_

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
  "session": "worker_paper_bib-year-audit_20260515T174748",
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

_source line 4 · 2026-05-15T17:54:07.227407+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_bib-year-audit_20260515T174748",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-15T17:54:07.227603+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "DNA-GPT Divergent N-Gram Analysis Training-Free Detection ICLR 2024"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_bib-year-audit_20260515T174748",
  "tool": "WebSearch",
  "tool_args": {
    "query": "DNA-GPT Divergent N-Gram Analysis Training-Free Detection ICLR 2024"
  }
}
```

</details>

---

### Tool call

_source line 6 · 2026-05-15T17:54:07.227759+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Binoculars Zero-Shot Detection Machine-Generated Text Hans ICML 2024"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_bib-year-audit_20260515T174748",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Binoculars Zero-Shot Detection Machine-Generated Text Hans ICML 2024"
  }
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-15T17:54:07.227876+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Fast-DetectGPT Efficient Zero-Shot Detection Bao ICLR 2024"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_bib-year-audit_20260515T174748",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Fast-DetectGPT Efficient Zero-Shot Detection Bao ICLR 2024"
  }
}
```

</details>

---

### Tool call

_source line 8 · 2026-05-15T17:54:07.227987+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Self-Consuming Generative Models Go MAD Alemohammad conference publication year"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_bib-year-audit_20260515T174748",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Self-Consuming Generative Models Go MAD Alemohammad conference publication year"
  }
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-15T17:54:07.228096+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Curse of Recursion Training Generated Data Models Forget Shumailov Nature publication year"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_bib-year-audit_20260515T174748",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Curse of Recursion Training Generated Data Models Forget Shumailov Nature publication year"
  }
}
```

</details>

---

### Tool call

_source line 10 · 2026-05-15T17:54:07.228209+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"Is Model Collapse Inevitable\" Gerstgrasser publication venue year"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_bib-year-audit_20260515T174748",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"Is Model Collapse Inevitable\" Gerstgrasser publication venue year"
  }
}
```

</details>

---

### Tool result

_source line 11 · 2026-05-15T17:54:07.228338+00:00_

Web search results for query: "Self-Consuming Generative Models Go MAD Alemohammad conference publication year"

Links: [{"title":"[2307.01850] Self-Consuming Generative Models Go MAD","url":"https://arxiv.org/abs/2307.01850"},{"title":"(PDF) Self-Consuming Generative Models Go MAD","url":"https://www.researchgate.net/publication/372136378_Self-Consuming_Generative_Models_Go_MAD"},{"title":"SELF-CONSUMING GENERATIVE MODELS GO MAD - Houston Methodist Scholars","url":"https://scholars.houstonmethodist.org/en/publications/self-consuming-generative-models-go-mad/"},{"title":"[PDF] Self-Consuming Generative Models Go MAD | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Self-Consuming-Generative-Models-Go-MAD-Alemohammad-Casco-Rodriguez/ad022cd5da75637ac3e0a8f8cc4f0d394ba5ff7a"},{"title":"Self-Consuming Generative Models Go MAD | Montreal AI Ethics Institute","url":"https://montrealethics.ai/self-consuming-generative-models-go-mad/"},{"title":"SELF-CONSUMING GENERATIVE MODELS GO MAD","url":"https://proceedings.iclr.cc/paper_files/paper/2024/file/ebc042e767de551803ccfcc45e2454f5-Paper-Conference.pdf"},{"title":"Self-Consuming AI Resources","url":"https://dsp.rice.edu/ai-loops/"},{"title":"Self-Consuming Generative Models Go MAD | OpenReview","url":"https://openreview.net/forum?id=ShjMHfmPs0"},{"title":"Self-Consuming Generative Models Go MAD - ADS","url":"https://ui.adsabs.harvard.edu/abs/2023arXiv230701850A/abstract"},{"title":"Self-Consuming Generative Models Go MAD | NSF Public Access Repository","url":"https://par.nsf.gov/biblio/10570494"}]

Based on the search results, "Self-Consuming Generative Models Go MAD" was presented at the 12th International Conference on Learning Representations (ICLR 2024), which took place in Vienna, Austria. The publication year was 2024.

However, it's worth noting that the paper was authored by Sina Alemohammad and colleagues, and was first available on arXiv on July 4, 2023, before being formally published at the ICLR 20
…[truncated 117 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_bib-year-audit_20260515T174748",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-15T17:54:07.228491+00:00_

Web search results for query: "DNA-GPT Divergent N-Gram Analysis Training-Free Detection ICLR 2024"

Links: [{"title":"DNA-GPT: Divergent N-Gram Analysis for Training-Free Detection of GPT-Generated Text | OpenReview","url":"https://openreview.net/forum?id=Xlayxj2fWp"},{"title":"[2305.17359] DNA-GPT: Divergent N-Gram Analysis for Training-Free Detection of GPT-Generated Text","url":"https://arxiv.org/abs/2305.17359"},{"title":"ICLR Poster DNA-GPT: Divergent N-Gram Analysis for Training-Free Detection of GPT-Generated Text","url":"https://iclr.cc/virtual/2024/poster/18444"},{"title":"dblp: DNA-GPT: Divergent N-Gram Analysis for Training-Free Detection of GPT-Generated Text.","url":"https://dblp1.uni-trier.de/rec/conf/iclr/Yang0WPWC24.html"},{"title":"DNA-GPT: Divergent N-Gram Analysis for Training-Free Detection of GPT-Generated Text","url":"https://www.nec-labs.com/blog/dna-gpt-divergent-n-gram-analysis-for-training-free-detection-of-gpt-generated-text/"},{"title":"(PDF) DNA-GPT: Divergent N-Gram Analysis for Training-Free Detection of GPT-Generated Text","url":"https://www.researchgate.net/publication/371136931_DNA-GPT_Divergent_N-Gram_Analysis_for_Training-Free_Detection_of_GPT-Generated_Text"},{"title":"[2303.02909] DNA-GPT: Divergent N-Gram Analysis for Training-Free Detection of GPT-Generated Text","url":"https://ar5iv.labs.arxiv.org/html/2303.02909"},{"title":"DNA-GPT: Divergent N-Gram Analysis for Training-Free ...","url":"https://arxiv.org/pdf/2305.17359"},{"title":"DNA-GPT: DIVERGENT N-GRAM ANALYSIS FOR ...","url":"https://openreview.net/pdf?id=Xlayxj2fWp"},{"title":"DNA-GPT: Divergent N-Gram Analysis for Training-Free Detection of GPT-Generated Text","url":"https://paperreading.club/page?id=167623"}]

Based on the search results, here's what I found about DNA-GPT:

## Overview

DNA-GPT (Divergent N-Gram Analysis) is a novel training-free detection strategy for identifying GPT-generated text. The research was conducted by Xianjun Yang, Wei Cheng, Yue Wu, Li
…[truncated 1165 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_bib-year-audit_20260515T174748",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 13 · 2026-05-15T17:54:07.228696+00:00_

Web search results for query: "Binoculars Zero-Shot Detection Machine-Generated Text Hans ICML 2024"

Links: [{"title":"GitHub - ahans30/Binoculars: [ICML 2024] Binoculars: Zero-Shot Detection of LLM-Generated Text · GitHub","url":"https://github.com/ahans30/Binoculars"},{"title":"[2401.12070] Spotting LLMs With Binoculars: Zero-Shot Detection of Machine-Generated Text","url":"https://arxiv.org/abs/2401.12070"},{"title":"[Quick Review] Spotting LLMs With Binoculars: Zero-Shot Detection of Machine-Generated Text","url":"https://liner.com/review/spotting-llms-with-binoculars-zeroshot-detection-machinegenerated-text"},{"title":"Spotting LLMs With Binoculars: Zero-Shot Detection of Machine-Generated Text | OpenReview","url":"https://openreview.net/forum?id=iARAKITHTH"},{"title":"Spotting LLMs With Binoculars: Zero-Shot Detection of Machine-Generated Text | MPI-IS","url":"https://is.mpg.de/en/publications/hans_spotting_2024"},{"title":"Spotting LLMs With Binoculars: Zero-Shot Detection of Machine-Generated Text","url":"https://proceedings.mlr.press/v235/hans24a.html"},{"title":"Spotting LLMs with binoculars: zero-shot detection of ...","url":"https://dl.acm.org/doi/10.5555/3692070.3692768"},{"title":"ICML Poster Spotting LLMs With Binoculars: Zero-Shot Detection of Machine-Generated Text","url":"https://icml.cc/virtual/2024/poster/33662"},{"title":"Spotting LLMs With Binoculars: Zero-Shot Detection of Machine-Generated Text | Safety- and Efficiency- aligned Learning – MPI-IS","url":"https://is.mpg.de/seal/publications/hans_spotting_2024"},{"title":"Spotting LLMs With Binoculars: Zero-Shot Detection of Machine-Generated Text","url":"https://deepnlp.org/content/articles/spotting-llms-with-binoculars:-zero-shot-detection-of-machine-generated-text"}]

## Search Results

I found detailed information about the research paper on Binoculars. Here's a summary:

**Paper Overview:**
Binoculars is a zero-shot LLM detection method using contrasting language models for machine-generat
…[truncated 1239 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_bib-year-audit_20260515T174748",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-15T17:54:07.228874+00:00_

Web search results for query: "Fast-DetectGPT Efficient Zero-Shot Detection Bao ICLR 2024"

Links: [{"title":"GitHub - baoguangsheng/fast-detect-gpt: Code base for ICLR 2024 \"Fast-DetectGPT: Efficient Zero-Shot Detection of Machine-Generated Text via Conditional Probability Curvature\". · GitHub","url":"https://github.com/baoguangsheng/fast-detect-gpt"},{"title":"FAST-DETECTGPT: EFFICIENT ZERO-SHOT DETEC","url":"https://proceedings.iclr.cc/paper_files/paper/2024/file/6b8c6f846c3575e1d1ad496abea28826-Paper-Conference.pdf"},{"title":"Fast-DetectGPT: Efficient Zero-Shot Detection of Machine-Generated Text via Conditional Probability Curvature | OpenReview","url":"https://openreview.net/forum?id=Bpcgcr8E8Z"},{"title":"ICLR Poster Fast-DetectGPT: Efficient Zero-Shot Detection of Machine-Generated Text via Conditional Probability Curvature","url":"https://iclr.cc/virtual/2024/poster/19201"},{"title":"(PDF) FAST-DETECTGPT: EFFICIENT ZERO-SHOT DETEC- TION OF MACHINE-GENERATED TEXT VIA CONDI- TIONAL PROBABILITY CURVATURE","url":"https://www.researchgate.net/publication/388188914_FAST-DETECTGPT_EFFICIENT_ZERO-SHOT_DETEC-_TION_OF_MACHINE-GENERATED_TEXT_VIA_CONDI-_TIONAL_PROBABILITY_CURVATURE"},{"title":"Fast-DetectGPT: Efficient Zero-Shot Detection of Machine-Generated Text via Conditional Probability Curvature","url":"https://proceedings.iclr.cc/paper_files/paper/2024/hash/6b8c6f846c3575e1d1ad496abea28826-Abstract-Conference.html"},{"title":"[2310.05130] Fast-DetectGPT: Efficient Zero-Shot Detection of Machine-Generated Text via Conditional Probability Curvature","url":"https://arxiv.org/abs/2310.05130"},{"title":"ICLR 2024 | Fast-DetectGPT: Efficient Zero-Shot Detection of Machine-Generated Text - YouTube","url":"https://www.youtube.com/watch?v=Nk7LpsrIUDE"},{"title":"Releases · baoguangsheng/fast-detect-gpt","url":"https://github.com/baoguangsheng/fast-detect-gpt/releases"},{"title":"fast-detect-gpt/scripts/fast_detect_gpt.py at main · baoguangsheng/fast-detect-gpt","url":
…[truncated 1459 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_bib-year-audit_20260515T174748",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 15 · 2026-05-15T17:54:07.229043+00:00_

Web search results for query: ""Is Model Collapse Inevitable" Gerstgrasser publication venue year"

Links: [{"title":"[2404.01413] Is Model Collapse Inevitable? Breaking the Curse of Recursion by Accumulating Real and Synthetic Data","url":"https://arxiv.org/abs/2404.01413"},{"title":"Is Model Collapse Inevitable? Breaking the Curse of Recursion by Accumulating Real and Synthetic Data | Stanford SALT Lab","url":"https://saltlab.stanford.edu/papers/gerstgrasser-is-model-collapse-2024/"},{"title":"Experts divided over training AI with more data from AI • The Register","url":"https://www.theregister.com/2024/05/09/ai_model_collapse/"},{"title":"[2404.01413v1] Is Model Collapse Inevitable? Breaking the Curse of Recursion by Accumulating Real and Synthetic Data","url":"https://arxiv.org/abs/2404.01413v1"},{"title":"Is Model Collapse Inevitable? Breaking the Curse of Recursion by Accumulating Real and Synthetic Data | Rylan Schaeffer","url":"https://rylanschaeffer.github.io/content/research/2024_arxiv_is_model_collapse_inevitable/main.html"},{"title":"Addressing Concerns of Model Collapse from Synthetic Data in AI","url":"https://www.gretel.ai/blog/addressing-concerns-of-model-collapse-from-synthetic-data-in-ai"},{"title":"Is Model Collapse Inevitable? Breaking the Curse of Recursion by Accumulating Real and Synthetic Data","url":"https://arxiv.org/html/2404.01413v2"},{"title":"Is Model Collapse Inevitable? Breaking the Curse of Recursion by","url":"https://openreview.net/pdf/264715d321dd6b63cbc356483cbb650791eb374b.pdf"},{"title":"[PDF] Is Model Collapse Inevitable? Breaking the Curse of Recursion by Accumulating Real and Synthetic Data | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Is-Model-Collapse-Inevitable-Breaking-the-Curse-of-Gerstgrasser-Schaeffer/e8815da26d4e6cac8b23b7e6aa75cec028cb66d2"},{"title":"Is Model Collapse Inevitable? Breaking the Curse of Recursion by Accumulating Real and Synthetic Data | AI Research Paper Details","url":"https://ww
…[truncated 661 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_bib-year-audit_20260515T174748",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-15T17:54:07.229203+00:00_

Web search results for query: "Curse of Recursion Training Generated Data Models Forget Shumailov Nature publication year"

Links: [{"title":"[2305.17493] The Curse of Recursion: Training on Generated Data Makes Models Forget","url":"https://arxiv.org/abs/2305.17493"},{"title":"[PDF] The Curse of Recursion: Training on Generated Data Makes Models Forget | Semantic Scholar","url":"https://www.semanticscholar.org/paper/The-Curse-of-Recursion:-Training-on-Generated-Data-Shumailov-Shumaylov/155aec5cff650263a4c71136f97570611d1bba7a"},{"title":"The Curse of Recursion: Training on Generated Data Makes Models Forget","url":"https://arxiv.org/html/2305.17493v3"},{"title":"The Curse of Recursion: Training on Generated Data Makes Models Forget | AI Research Paper Details","url":"https://www.aimodels.fyi/papers/arxiv/curse-recursion-training-generated-data-makes-models"},{"title":"The Curse of Recursion: Training on Generated Data Makes Models Forget | alphaXiv","url":"https://www.alphaxiv.org/overview/2305.17493v3"},{"title":"THE CURSE OF RECURSION: TRAINING ON GENERATED DATA MAKES MODELS FORGET","url":"https://www.cl.cam.ac.uk/~is410/Papers/dementia_arxiv.pdf"},{"title":"The Curse of Recursion: Training on Generated Data Makes Models Forget (2023) | Ilia Shumailov | 153 Citations","url":"https://scispace.com/papers/the-curse-of-recursion-training-on-generated-data-makes-34zgysyl"},{"title":"[2305.17493v3] The Curse of Recursion: Training on Generated Data Makes Models Forget","url":"https://arxiv.org/abs/2305.17493v3"},{"title":"Is Model Collapse Inevitable? Breaking the Curse of Recursion by Accumulating Real and Synthetic Data","url":"https://arxiv.org/html/2404.01413v2"},{"title":"Recursive Pollution and Model Collapse Are Not the Same | BIML","url":"https://berryvilleiml.com/2026/01/10/recursive-pollution-and-model-collapse-are-not-the-same/"}]

Based on the search results, I found important information about "The Curse of Recursion: Training on Generated Data Makes Model
…[truncated 921 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_bib-year-audit_20260515T174748",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-15T17:54:07.229381+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"Intrinsic Dimension Estimation for Robust Detection of AI-Generated Texts\" Tulchinskii NeurIPS 2023"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_bib-year-audit_20260515T174748",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"Intrinsic Dimension Estimation for Robust Detection of AI-Generated Texts\" Tulchinskii NeurIPS 2023"
  }
}
```

</details>

---

### Tool call

_source line 18 · 2026-05-15T17:54:07.229505+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"Can AI-Generated Text be Reliably Detected\" Sadasivan ICLR publication year"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_bib-year-audit_20260515T174748",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"Can AI-Generated Text be Reliably Detected\" Sadasivan ICLR publication year"
  }
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-15T17:54:07.229640+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"Paraphrasing Evades Detectors of AI-Generated Text\" Krishna NeurIPS 2023"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_bib-year-audit_20260515T174748",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"Paraphrasing Evades Detectors of AI-Generated Text\" Krishna NeurIPS 2023"
  }
}
```

</details>

---

### Tool call

_source line 20 · 2026-05-15T17:54:07.229755+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"Beyond Binary Towards Fine-Grained LLM-Generated Text Detection\" Cheng ACM Web Conference 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_bib-year-audit_20260515T174748",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"Beyond Binary Towards Fine-Grained LLM-Generated Text Detection\" Cheng ACM Web Conference 2025"
  }
}
```

</details>

---

### Tool call

_source line 21 · 2026-05-15T17:54:07.229864+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"The Curious Decline of Linguistic Diversity\" Guo NAACL 2024 Findings"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_bib-year-audit_20260515T174748",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"The Curious Decline of Linguistic Diversity\" Guo NAACL 2024 Findings"
  }
}
```

</details>

---

### Tool call

_source line 22 · 2026-05-15T17:54:07.229970+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"Does Writing with Language Models Reduce Content Diversity\" Padmakumar ICLR 2024"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_bib-year-audit_20260515T174748",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"Does Writing with Language Models Reduce Content Diversity\" Padmakumar ICLR 2024"
  }
}
```

</details>

---

### Tool result

_source line 23 · 2026-05-15T17:54:07.230098+00:00_

Web search results for query: ""Can AI-Generated Text be Reliably Detected" Sadasivan ICLR publication year"

Links: [{"title":"Can AI-Generated Text be Reliably Detected?","url":"https://arxiv.org/pdf/2303.11156"},{"title":"[2303.11156] Can AI-Generated Text be Reliably Detected?","url":"https://arxiv.org/abs/2303.11156"},{"title":"(PDF) Can AI-Generated Text be Reliably Detected?","url":"https://www.researchgate.net/publication/369380286_Can_AI-Generated_Text_be_Reliably_Detected"},{"title":"[PDF] Can AI-Generated Text be Reliably Detected? | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Can-AI-Generated-Text-be-Reliably-Detected-Sadasivan-Kumar/5ee8bb4fc80a291b2e416a2a879e7153a783d7e9"},{"title":"Can AI-Generated Text be Reliably Detected? | OpenReview","url":"https://openreview.net/forum?id=NvSwR4IvLO"},{"title":"Can AI-Generated Text be Reliably Detected? - ADS","url":"https://ui.adsabs.harvard.edu/abs/2023arXiv230311156S/abstract"},{"title":"The Problems with AI Detectors: False Positives and False Negatives - Generative AI Detection Tools - Guides at University of San Diego Legal Research Center","url":"https://lawlibguides.sandiego.edu/c.php?g=1443311&p=10721367"},{"title":"Can AI-Generated Text be Reliably Detected?","url":"https://bibbase.org/network/publication/sadasivan-kumar-balasubramanian-wang-feizi-canaigeneratedtextbereliablydetected-2023"},{"title":"Can AI-Generated Text be Reliably Detected? Stress Testing AI Text Detectors Under Various Attacks | OpenReview","url":"https://openreview.net/forum?id=OOgsAZdFOt"},{"title":"Can AI-Generated Text be Reliably Detected? Stress Testing AI Text Detectors Under Various Attacks | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Can-AI-Generated-Text-be-Reliably-Detected-Stress-Sadasivan-Kumar/42f7d83e6c20fd4aaf3e3f53b18ab7db221ee300"}]

Based on the search results, I found information about the Sadasivan paper on AI-generated text detection:

The paper "Can AI-Generated Text be
…[truncated 723 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_bib-year-audit_20260515T174748",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 24 · 2026-05-15T17:54:07.230257+00:00_

Web search results for query: ""Intrinsic Dimension Estimation for Robust Detection of AI-Generated Texts" Tulchinskii NeurIPS 2023"

Links: [{"title":"NeurIPS Poster Intrinsic Dimension Estimation for Robust Detection of AI-Generated Texts","url":"https://neurips.cc/virtual/2023/poster/72624"},{"title":"Intrinsic Dimension Estimation for Robust Detection of AI-Generated Texts","url":"https://proceedings.neurips.cc/paper_files/paper/2023/hash/7baa48bc166aa2013d78cbdc15010530-Abstract-Conference.html"},{"title":"[2306.04723] Intrinsic Dimension Estimation for Robust Detection of AI-Generated Texts","url":"https://arxiv.org/abs/2306.04723"},{"title":"Intrinsic Dimension Estimation for Robust Detection of AI-Generated Texts | OpenReview","url":"https://openreview.net/forum?id=8uOZ0kNji6"},{"title":"Intrinsic Dimension Estimation for Robust Detection of AI-Generated Texts","url":"https://arxiv.org/pdf/2306.04723"},{"title":"Intrinsic Dimension Estimation for Robust Detection of AI- ...","url":"https://papers.neurips.cc/paper_files/paper/2023/file/7baa48bc166aa2013d78cbdc15010530-Paper-Conference.pdf"},{"title":"[PDF] Intrinsic Dimension Estimation for Robust Detection of AI-Generated Texts | Semantic Scholar","url":"https://www.semanticscholar.org/paper/a5fab19553e623e8787383cb3da76b8a3c42a8f4"},{"title":"[Quick Review] Intrinsic Dimension Estimation for Robust Detection of AI-Generated Texts","url":"https://liner.com/review/intrinsic-dimension-estimation-for-robust-detection-of-aigenerated-texts"},{"title":"Intrinsic dimension estimation for robust detection of AI-generated texts | Proceedings of the 37th International Conference on Neural Information Processing Systems","url":"https://dl.acm.org/doi/10.5555/3666122.3667828"},{"title":"Are AI Detectors Good Enough? A Survey on Quality of Datasets with","url":"https://openreview.net/pdf?id=WDhwO4Hhq2"}]

I found the paper! Here are the key details about "Intrinsic Dimension Estimation for Robust Detection of AI-Generate
…[truncated 1529 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_bib-year-audit_20260515T174748",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 25 · 2026-05-15T17:54:07.230491+00:00_

Web search results for query: ""The Curious Decline of Linguistic Diversity" Guo NAACL 2024 Findings"

Links: [{"title":"The Curious Decline of Linguistic Diversity: Training Language Models on Synthetic Text - ACL Anthology","url":"https://aclanthology.org/2024.findings-naacl.228/"},{"title":"(PDF) The Curious Decline of Linguistic Diversity: Training Language Models on Synthetic Text","url":"https://www.researchgate.net/publication/382631840_The_Curious_Decline_of_Linguistic_Diversity_Training_Language_Models_on_Synthetic_Text"},{"title":"@inproceedings{guo-etal-2024-curious,","url":"https://aclanthology.org/2024.findings-naacl.228.bib"},{"title":"The Curious Decline of Linguistic Diversity: Training Language Models on Synthetic Text - Laboratoire d'informatique de l'X (LIX)","url":"https://hal.inrae.fr/X-LIX/hal-04593399v1"},{"title":"[2311.09807] The Curious Decline of Linguistic Diversity: Training Language Models on Synthetic Text","url":"https://arxiv.org/abs/2311.09807"},{"title":"The Curious Decline of Linguistic Diversity: Training Language Models on Synthetic Text - ADS","url":"https://ui.adsabs.harvard.edu/abs/2023arXiv231109807G/abstract"},{"title":"The Curious Decline of Linguistic Diversity: Training Language Models on Synthetic Text - Archive ouverte HAL","url":"https://hal.science/hal-04593399"},{"title":"[PDF] The Curious Decline of Linguistic Diversity: Training Language Models on Synthetic Text | Semantic Scholar","url":"https://www.semanticscholar.org/paper/The-Curious-Decline-of-Linguistic-Diversity:-Models-Guo-Shang/7d5ea474aa1cf732bb1d00faa07a5bb2c9119cfd"},{"title":"GitHub - YanzhuGuo/linguistic-diversity","url":"https://github.com/YanzhuGuo/linguistic-diversity"},{"title":"The Curious Decline of Linguistic Diversity: Training Language Models on Synthetic Text | AI Research Paper Details","url":"https://www.aimodels.fyi/papers/arxiv/curious-decline-linguistic-diversity-training-language-models"}]

Here are the search results for "The Curious
…[truncated 1402 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_bib-year-audit_20260515T174748",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 26 · 2026-05-15T17:54:07.230719+00:00_

Web search results for query: ""Paraphrasing Evades Detectors of AI-Generated Text" Krishna NeurIPS 2023"

Links: [{"title":"GitHub - martiansideofthemoon/ai-detection-paraphrases: Official repository for our NeurIPS 2023 paper \"Paraphrasing evades detectors of AI-generated text, but retrieval is an effective defense\" (https://arxiv.org/abs/2303.13408). · GitHub","url":"https://github.com/martiansideofthemoon/ai-detection-paraphrases"},{"title":"Paraphrasing evades detectors of AI-generated text, but retrieval is an effective defense","url":"https://proceedings.neurips.cc/paper_files/paper/2023/hash/575c450013d0e99e4b0ecf82bd1afaa4-Abstract-Conference.html"},{"title":"NeurIPS Poster Paraphrasing evades detectors of AI-generated text, but retrieval is an effective defense","url":"https://neurips.cc/virtual/2023/poster/71402"},{"title":"[2303.13408] Paraphrasing evades detectors of AI-generated text, but retrieval is an effective defense","url":"https://arxiv.org/abs/2303.13408"},{"title":"Paraphrasing evades detectors of AI-generated text, but ...","url":"https://openreview.net/pdf?id=WbFhFvjjKj"},{"title":"[PDF] Paraphrasing evades detectors of AI-generated text, but retrieval is an effective defense | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Paraphrasing-evades-detectors-of-AI-generated-text,-Krishna-Song/1c13af186d1e177b85ef1ec3fc7b8d33ec314cfd"},{"title":"Paraphrasing evades detectors of AI-generated text, but retrieval is an effective defense | Request PDF","url":"https://www.researchgate.net/publication/369477232_Paraphrasing_evades_detectors_of_AI-generated_text_but_retrieval_is_an_effective_defense"},{"title":"Paraphrasing evades detectors of AI-generated text, but retrieval is an effective defense - ADS","url":"https://ui.adsabs.harvard.edu/abs/2023arXiv230313408K/abstract"},{"title":"Paraphrasing evades detectors of AI-generated text, but retrieval is an effective defense","url":"https://papers.nips.cc/paper_files/paper/2023/hash/575
…[truncated 2150 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_bib-year-audit_20260515T174748",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 27 · 2026-05-15T17:54:07.230896+00:00_

Web search results for query: ""Does Writing with Language Models Reduce Content Diversity" Padmakumar ICLR 2024"

Links: [{"title":"[2309.05196] Does Writing with Language Models Reduce Content Diversity?","url":"https://arxiv.org/abs/2309.05196"},{"title":"Does Writing with Language Models Reduce Content Diversity? | OpenReview","url":"https://openreview.net/forum?id=Feiz5HtCD0"},{"title":"DOES WRITING WITH LANGUAGE MODELS REDUCE ...","url":"https://openreview.net/pdf?id=Feiz5HtCD0"},{"title":"Does Writing With Language Models (LLMs) Reduce Content Diversity?","url":"https://iclr.cc/media/iclr-2024/Slides/19056.pdf"},{"title":"Does Writing with Language Models Reduce Content Diversity? | AI Research Paper Details","url":"https://www.aimodels.fyi/papers/arxiv/does-writing-language-models-reduce-content-diversity"},{"title":"Does Writing with Language Models Reduce Content Diversity? | Request PDF","url":"https://www.researchgate.net/publication/373837896_Does_Writing_with_Language_Models_Reduce_Content_Diversity"},{"title":"DOES WRITING WITH LANGUAGE MODELS REDUCE CONTENT DIVERSITY? - NYU Scholars","url":"https://nyuscholars.nyu.edu/en/publications/does-writing-with-language-models-reduce-content-diversity"},{"title":"Does Writing with Language Models Reduce Content Diversity? | NSF Public Access Repository","url":"https://par.nsf.gov/biblio/10534705-does-writing-language-models-reduce-content-diversity"},{"title":"[PDF] Does Writing with Language Models Reduce Content Diversity? | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Does-Writing-with-Language-Models-Reduce-Content-Padmakumar-He/f95fb254da1f7b74a14ac8feb3f834d64e67e4cd"},{"title":"DOES WRITING WITH LANGUAGE MODELS REDUCE ...","url":"https://proceedings.iclr.cc/paper_files/paper/2024/file/02dec8877fb7c6aa9a79f81661baca7c-Paper-Conference.pdf"}]

Based on the search results, I found the paper you're looking for. Here's what the research shows:

## Paper Overview

"Does Writing with Language
…[truncated 1162 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_bib-year-audit_20260515T174748",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 28 · 2026-05-15T17:54:07.231065+00:00_

Web search results for query: ""Beyond Binary Towards Fine-Grained LLM-Generated Text Detection" Cheng ACM Web Conference 2025"

Links: [{"title":"Beyond Binary: Towards Fine-Grained LLM-Generated Text Detection via Role Recognition and Involvement Measurement | Proceedings of the ACM on Web Conference 2025","url":"https://dl.acm.org/doi/10.1145/3696410.3714770"},{"title":"Beyond Binary: Towards Fine-Grained LLM-Generated Text","url":"https://arxiv.org/pdf/2410.14259"},{"title":"Beyond Binary: Towards Fine-Grained LLM-Generated Text Detection via Role Recognition and Involvement Measurement","url":"https://arxiv.org/html/2410.14259v2"},{"title":"[2410.14259] Beyond Binary: Towards Fine-Grained LLM-Generated Text Detection via Role Recognition and Involvement Measurement","url":"https://arxiv.org/abs/2410.14259"},{"title":"[2410.14259v1] Beyond Binary: Towards Fine-Grained LLM-Generated Text Detection via Role Recognition and Involvement Measurement","url":"https://arxiv.org/abs/2410.14259v1"},{"title":"On the Detectability of LLM-Generated Text: What Exactly Is LLM-Generated Text?","url":"https://arxiv.org/html/2510.20810v1"},{"title":"Beyond Binary: Towards Fine-Grained LLM-Generated Text Detection via Role Recognition and Involvement Measurement – Own Your AI","url":"https://ownyourai.com/beyond-binary-towards-fine-grained-llm-generated-text-detection-via-role-recognition-and-involvement-measurement/"},{"title":"Toward Reliable Detection of LLM-Generated Texts: A Comprehensive Evaluation Framework with CUDRT | ACM Transactions on Intelligent Systems and Technology","url":"https://dl.acm.org/doi/10.1145/3779427"},{"title":"Bilingual generated text detection through semantic and statistical analysis - Chenxi Min, Ru Zhang, Jianyi Liu, 2025","url":"https://journals.sagepub.com/doi/abs/10.1177/1088467X241307192"},{"title":"Beyond the Final Actor: Modeling the Dual Roles of Creator and Editor for Fine-Grained LLM-Generated Text Detection","url":"https://arxiv.org/html/
…[truncated 1292 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_bib-year-audit_20260515T174748",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool call

_source line 29 · 2026-05-15T17:54:07.231246+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"Can AI-Generated Text be Reliably Detected\" Sadasivan ICLR 2024 accepted conference"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_bib-year-audit_20260515T174748",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"Can AI-Generated Text be Reliably Detected\" Sadasivan ICLR 2024 accepted conference"
  }
}
```

</details>

---

### Tool call

_source line 30 · 2026-05-15T17:54:07.231368+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"Mapping the Increasing Use of LLMs in Scientific Papers\" Liang publication venue year"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_bib-year-audit_20260515T174748",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"Mapping the Increasing Use of LLMs in Scientific Papers\" Liang publication venue year"
  }
}
```

</details>

---

### Tool call

_source line 31 · 2026-05-15T17:54:07.231481+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"Monitoring AI-Modified Content at Scale\" Liang ICML 2024"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_bib-year-audit_20260515T174748",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"Monitoring AI-Modified Content at Scale\" Liang ICML 2024"
  }
}
```

</details>

---

### Tool call

_source line 32 · 2026-05-15T17:54:07.231607+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"Through the Looking Glass Learning to Attribute Synthetic Text\" Munir EACL 2021"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_bib-year-audit_20260515T174748",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"Through the Looking Glass Learning to Attribute Synthetic Text\" Munir EACL 2021"
  }
}
```

</details>

---

### Tool call

_source line 33 · 2026-05-15T17:54:07.231722+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"Authorship Attribution for Neural Text Generation\" Uchendu EMNLP 2020"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_bib-year-audit_20260515T174748",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"Authorship Attribution for Neural Text Generation\" Uchendu EMNLP 2020"
  }
}
```

</details>

---

### Tool call

_source line 34 · 2026-05-15T17:54:07.231828+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"LLM as a Broken Telephone Iterative Generation\" Mohamed ACL 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_bib-year-audit_20260515T174748",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"LLM as a Broken Telephone Iterative Generation\" Mohamed ACL 2025"
  }
}
```

</details>

---

### Tool result

_source line 35 · 2026-05-15T17:54:07.231960+00:00_

Web search results for query: ""Mapping the Increasing Use of LLMs in Scientific Papers" Liang publication venue year"

Links: [{"title":"Mapping the Increasing Use of LLMs in Scientific Papers","url":"https://arxiv.org/html/2404.01268v1"},{"title":"GitHub - Weixin-Liang/Mapping-the-Increasing-Use-of-LLMs-in-Scientific-Papers · GitHub","url":"https://github.com/Weixin-Liang/Mapping-the-Increasing-Use-of-LLMs-in-Scientific-Papers"},{"title":"[2404.01268] Mapping the Increasing Use of LLMs in Scientific Papers","url":"https://arxiv.org/abs/2404.01268"},{"title":"Mapping the Increasing Use of LLMs in Scientific Papers | BibSonomy","url":"https://www.bibsonomy.org/bibtex/28f3ef49cf074d7caa6cdd244449c11cf/diekhans"},{"title":"Mapping the Increasing Use of LLMs in Scientific Papers | OpenReview","url":"https://openreview.net/forum?id=YX7QnhxESU"},{"title":"Mapping the Increasing Use of LLMs in Scientific Papers","url":"https://www.semanticscholar.org/paper/882f3d1b718e833156ccd6f5bda3190cd06791ea"},{"title":"Mapping the Increasing Use of LLMs in Scientific Papers","url":"https://openreview.net/pdf/eff0ea8ed41a89a9e267752af56df912888fee65.pdf"},{"title":"Large Language Models and Scientific Writing (Part 1)","url":"https://nilsreiter.de/blog/2025/llms-and-science-part-1"},{"title":"Quantifying large language model usage in scientific papers - PubMed","url":"https://pubmed.ncbi.nlm.nih.gov/40760036/"},{"title":"Preprint Mapping the Increasing Use of LLMs in Scientific Papers","url":"https://arxiv.org/pdf/2404.01268"}]

Based on the search results, here is the information about the publication "Mapping the Increasing Use of LLMs in Scientific Papers" by Liang:

**Publication Details:**
- Title: "Mapping the Increasing Use of LLMs in Scientific Papers" by Weixin Liang and 13 other authors
- Year: 2024
- Publication Venue: First Conference on Language Modeling (COLM)

**Key Information:**
The paper conducts a systematic, large-scale analysis across 950,965 papers published bet
…[truncated 296 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_bib-year-audit_20260515T174748",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 36 · 2026-05-15T17:54:07.232117+00:00_

Web search results for query: ""Can AI-Generated Text be Reliably Detected" Sadasivan ICLR 2024 accepted conference"

Links: [{"title":"Can AI-Generated Text be Reliably Detected?","url":"https://arxiv.org/pdf/2303.11156"},{"title":"[2303.11156] Can AI-Generated Text be Reliably Detected?","url":"https://arxiv.org/abs/2303.11156"},{"title":"Can AI-Generated Text be Reliably Detected? | OpenReview","url":"https://openreview.net/forum?id=NvSwR4IvLO"},{"title":"[PDF] Can AI-Generated Text be Reliably Detected? | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Can-AI-Generated-Text-be-Reliably-Detected-Sadasivan-Kumar/5ee8bb4fc80a291b2e416a2a879e7153a783d7e9"},{"title":"(PDF) Can AI-Generated Text be Reliably Detected?","url":"https://www.researchgate.net/publication/369380286_Can_AI-Generated_Text_be_Reliably_Detected"},{"title":"Can AI-Generated Text be Reliably Detected? - ADS","url":"https://ui.adsabs.harvard.edu/abs/2023arXiv230311156S/abstract"},{"title":"Can AI-Generated Text be Reliably Detected?","url":"https://bibbase.org/network/publication/sadasivan-kumar-balasubramanian-wang-feizi-canaigeneratedtextbereliablydetected-2024"},{"title":"Can AI-Generated Text be Reliably Detected? Stress Testing AI Text Detectors Under Various Attacks | OpenReview","url":"https://openreview.net/forum?id=OOgsAZdFOt"},{"title":"Can AI-Generated Text be Reliably Detected?","url":"https://scispace.com/pdf/can-ai-generated-text-be-reliably-detected-1p8qe3ww.pdf"},{"title":"Can AI-Generated Text be Reliably Detected? | alphaXiv","url":"https://www.alphaxiv.org/overview/2303.11156v4"}]

Based on my web search results, I found information about this paper:

The paper "Can AI-Generated Text be Reliably Detected?" is authored by Vinu Sankar Sadasivan and 3 other authors (Aounon Kumar, Sriram Balasubramanian, and Wenxiao Wang, along with Soheil Feizi).

The paper shows that AI text detectors are not reliable in practical scenarios, and develops a recursive paraphrasing atta
…[truncated 805 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_bib-year-audit_20260515T174748",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 37 · 2026-05-15T17:54:07.232279+00:00_

Web search results for query: ""Through the Looking Glass Learning to Attribute Synthetic Text" Munir EACL 2021"

Links: [{"title":"Through the Looking Glass: Learning to Attribute Synthetic Text Generated by Language Models - ACL Anthology","url":"https://aclanthology.org/2021.eacl-main.155/"},{"title":"EACL2021: Through the Looking Glass: Learning to Attribute Synthetic Text Generated by Language Models","url":"https://www.virtual2021.eacl.org/paper_main.753.html"},{"title":"[PDF] Through the Looking Glass: Learning to Attribute Synthetic Text Generated by Language Models | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Through-the-Looking-Glass:-Learning-to-Attribute-by-Munir-Batool/03e6b951e3665d28a7beeef87fcb1c9baecfd396"},{"title":"Through the Looking Glass: Learning to Attribute Synthetic Text Generated by Language Models - researchr publication","url":"https://researchr.org/publication/MunirBSSZ21"},{"title":"Through the Looking Glass: Learning to Attribute Synthetic Text Generated by Language Models | Request PDF","url":"https://www.researchgate.net/publication/355428226_Through_the_Looking_Glass_Learning_to_Attribute_Synthetic_Text_Generated_by_Language_Models"},{"title":"Through the looking glass: Learning to attribute synthetic text generated by language models","url":"https://papertalk.org/papertalks/28247"},{"title":"Through the Looking Glass: Learning to Attribute Synthetic Text Generated by Language Models - About Me","url":"http://shaoormunir.com/publications/1-through-the-looking-glass/"},{"title":"Learning to Attribute Synthetic Text Generated by ...","url":"https://web.cs.ucdavis.edu/~zubair/files/lm-eacl2021.pdf"},{"title":"(PDF) Through the Looking Glass: Learning to Attribute Synthetic Text Generated by Language Models","url":"https://www.academia.edu/67763523/Through_the_Looking_Glass_Learning_to_Attribute_Synthetic_Text_Generated_by_Language_Models"},{"title":"Main Conference Accepted Papers - EACL 2021","url":"https://2021.e
…[truncated 1228 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_bib-year-audit_20260515T174748",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 38 · 2026-05-15T17:54:07.232438+00:00_

Web search results for query: ""Monitoring AI-Modified Content at Scale" Liang ICML 2024"

Links: [{"title":"Monitoring AI-Modified Content at Scale: A Case Study on the Impact of ChatGPT on AI Conference Peer Reviews","url":"https://proceedings.mlr.press/v235/liang24b.html"},{"title":"[2403.07183] Monitoring AI-Modified Content at Scale: A Case Study on the Impact of ChatGPT on AI Conference Peer Reviews","url":"https://arxiv.org/abs/2403.07183"},{"title":"Monitoring AI-Modified Content at Scale: A Case Study on the ...","url":"http://lingjiaochen.com/papers/2024_MonitoringAIContent_ICML.pdf"},{"title":"Monitoring AI-modified content at scale | Proceedings of the 41st International Conference on Machine Learning","url":"https://dl.acm.org/doi/10.5555/3692070.3693262"},{"title":"ICML 2024 Monitoring AI-Modified Content at Scale: A Case Study on the Impact of ChatGPT on AI Conference Peer Reviews Oral","url":"https://icml.cc/virtual/2024/oral/35507"},{"title":"[PDF] Monitoring AI-Modified Content at Scale: A Case Study on the Impact of ChatGPT on AI Conference Peer Reviews | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Monitoring-AI-Modified-Content-at-Scale:-A-Case-on-Liang-Izzo/023e113b11ff7bac182713a069fedcbcccad9562"},{"title":"Monitoring AI-Modified Content at Scale: A Case Study on the Impact of ChatGPT on AI Conference Peer Reviews | alphaXiv","url":"https://www.alphaxiv.org/resources/2403.07183v2"},{"title":"Monitoring AI-Modified Content at Scale: A Case Study on the Impact of ChatGPT on AI Conference Peer Reviews","url":"https://arxiv.org/html/2403.07183v2"},{"title":"Monitoring AI-Modified Content at Scale: A Case Study on ...","url":"https://arxiv.org/pdf/2403.07183"},{"title":"dblp: ICML 2024","url":"https://dblp.org/db/conf/icml/icml2024.html"}]

I found the paper you're looking for! Here are the key details about "Monitoring AI-Modified Content at Scale: A Case Study on the Impact of ChatGPT on AI Conference Peer Reviews":

## Overvie
…[truncated 1238 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_bib-year-audit_20260515T174748",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 39 · 2026-05-15T17:54:07.232618+00:00_

Web search results for query: ""Authorship Attribution for Neural Text Generation" Uchendu EMNLP 2020"

Links: [{"title":"Authorship Attribution for Neural Text Generation - ACL Anthology","url":"https://aclanthology.org/2020.emnlp-main.673/"},{"title":"Authorship Attribution for Neural Text Generation | Request PDF","url":"https://www.researchgate.net/publication/347235360_Authorship_Attribution_for_Neural_Text_Generation"},{"title":"GitHub - AdaUchendu/Authorship-Attribution-for-Neural-Text-Generation · GitHub","url":"https://github.com/AdaUchendu/Authorship-Attribution-for-Neural-Text-Generation"},{"title":"Authorship attribution for neural text generation - Penn State","url":"https://pure.psu.edu/en/publications/authorship-attribution-for-neural-text-generation"},{"title":"[PDF] Authorship Attribution for Neural Text Generation | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Authorship-Attribution-for-Neural-Text-Generation-Uchendu-Le/9da9cab545bd1534a8c953bb66e611243dcee24d"},{"title":"Authorship Attribution for Neural Text Generation.","url":"https://dblp.org/rec/conf/emnlp/UchenduLSL20.xml"},{"title":"EMNLP2020: Authorship Attribution for Neural Text Generation","url":"https://virtual.2020.emnlp.org/paper_main.125.html"},{"title":"Authorship Attribution for Neural Text Generation - researchr publication","url":"https://researchr.org/publication/UchenduLSL20"},{"title":"Authorship Attribution for Neural Text Generation","url":"https://pike.psu.edu/publications/emnlp20.pdf"},{"title":"Authorship Attribution for Neural Text Generation (Conference Paper) | NSF PAGES","url":"https://par.nsf.gov/biblio/10212709"}]

I found the paper you're looking for! Here are the search results:

## Paper Details

**Authorship Attribution for Neural Text Generation** by Adaku Uchendu, Thai Le, Kai Shu, and Dongwon Lee was published in Proceedings of the 2020 Conference on Empirical Methods in Natural Language Processing (EMNLP), pages 8384–8395, Online.

## Overv
…[truncated 1010 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_bib-year-audit_20260515T174748",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 40 · 2026-05-15T17:54:07.232799+00:00_

Web search results for query: ""LLM as a Broken Telephone Iterative Generation" Mohamed ACL 2025"

Links: [{"title":"LLM as a Broken Telephone: Iterative Generation Distorts Information - ACL Anthology","url":"https://aclanthology.org/2025.acl-long.371/"},{"title":"GitHub - amr-mohamedd/LLM-as-a-Broken-Telephone: [ACL 2025] Code implementation for the \"LLM as a Broken Telephone: Iterative Generation Distorts Information\" paper.","url":"https://github.com/amr-mohamedd/LLM-as-a-Broken-Telephone"},{"title":"[2502.20258] LLM as a Broken Telephone: Iterative Generation Distorts Information","url":"https://arxiv.org/abs/2502.20258"},{"title":"[Quick Review] LLM as a Broken Telephone: Iterative Generation Distorts Information","url":"https://liner.com/review/llm-as-broken-telephone-iterative-generation-distorts-information"},{"title":"LLM as a Broken Telephone: Iterative Generation Distorts ...","url":"https://aclanthology.org/2025.acl-long.371.pdf"},{"title":"Accepted Main Conference Papers - ACL 2025","url":"https://2025.aclweb.org/program/main_papers/"},{"title":"LLM as a Broken Telephone: Iterative Generation Distorts Information | Request PDF","url":"https://www.researchgate.net/publication/394300051_LLM_as_a_Broken_Telephone_Iterative_Generation_Distorts_Information"},{"title":"dblp: LLM as a Broken Telephone: Iterative Generation Distorts Information.","url":"https://dblp.org/rec/journals/corr/abs-2502-20258.html"},{"title":"Paper page - LLM as a Broken Telephone: Iterative Generation Distorts Information","url":"https://huggingface.co/papers/2502.20258"},{"title":"Google Scholar","url":"https://scholar.google.com/scholar?q=LLM+as+a+Broken+Telephone:+Iterative+Generation+Distorts+Information."}]

I found the paper! Here's information about "LLM as a Broken Telephone: Iterative Generation Distorts Information" by Mohamed et al., ACL 2025:

## Overview

This study investigates whether LLMs similarly distort information through iterative generation, inspired by the "
…[truncated 1596 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_bib-year-audit_20260515T174748",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 41 · 2026-05-15T17:54:07.232983+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Sadasivan \"Can AI-Generated Text be Reliably Detected\" ICLR 2024 proceedings accepted rejected"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_bib-year-audit_20260515T174748",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Sadasivan \"Can AI-Generated Text be Reliably Detected\" ICLR 2024 proceedings accepted rejected"
  }
}
```

</details>

---

### Tool call

_source line 42 · 2026-05-15T17:54:07.233108+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"Through the Looking Glass\" Munir Siddiqui Dengel Ahmed synthetic text attribution venue year"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_bib-year-audit_20260515T174748",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"Through the Looking Glass\" Munir Siddiqui Dengel Ahmed synthetic text attribution venue year"
  }
}
```

</details>

---

### Tool call

_source line 43 · 2026-05-15T17:54:07.233222+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"A Survey on LLM-Generated Text Detection\" Wu \"Computational Linguistics\" MIT Press 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_bib-year-audit_20260515T174748",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"A Survey on LLM-Generated Text Detection\" Wu \"Computational Linguistics\" MIT Press 2025"
  }
}
```

</details>

---

### Tool call

_source line 44 · 2026-05-15T17:54:07.233330+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"Automatic Detection of Machine Generated Text Critical Survey\" Jawahar COLING 2020"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_bib-year-audit_20260515T174748",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"Automatic Detection of Machine Generated Text Critical Survey\" Jawahar COLING 2020"
  }
}
```

</details>

---

### Tool call

_source line 45 · 2026-05-15T17:54:07.233435+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"OLMo Accelerating the Science of Language Models\" Groeneveld ACL 2024"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_bib-year-audit_20260515T174748",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"OLMo Accelerating the Science of Language Models\" Groeneveld ACL 2024"
  }
}
```

</details>

---

### Tool call

_source line 46 · 2026-05-15T17:54:07.233539+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"Position On the Possibilities of AI-Generated Text Detection\" Chakraborty ICML 2024"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_bib-year-audit_20260515T174748",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"Position On the Possibilities of AI-Generated Text Detection\" Chakraborty ICML 2024"
  }
}
```

</details>

---

### Tool result

_source line 47 · 2026-05-15T17:54:07.233685+00:00_

Web search results for query: "Sadasivan "Can AI-Generated Text be Reliably Detected" ICLR 2024 proceedings accepted rejected"

Links: [{"title":"[2303.11156] Can AI-Generated Text be Reliably Detected?","url":"https://arxiv.org/abs/2303.11156"},{"title":"Can AI-Generated Text be Reliably Detected?","url":"https://arxiv.org/pdf/2303.11156"},{"title":"[PDF] Can AI-Generated Text be Reliably Detected? | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Can-AI-Generated-Text-be-Reliably-Detected-Sadasivan-Kumar/5ee8bb4fc80a291b2e416a2a879e7153a783d7e9"},{"title":"Can AI-Generated Text be Reliably Detected? | OpenReview","url":"https://openreview.net/forum?id=NvSwR4IvLO"},{"title":"Can AI-Generated Text be Reliably Detected?","url":"https://bibbase.org/network/publication/sadasivan-kumar-balasubramanian-wang-feizi-canaigeneratedtextbereliablydetected-2024"},{"title":"Can AI-Generated Text be Reliably Detected? - ADS","url":"https://ui.adsabs.harvard.edu/abs/2023arXiv230311156S/abstract"},{"title":"(PDF) Can AI-Generated Text be Reliably Detected?","url":"https://www.researchgate.net/publication/369380286_Can_AI-Generated_Text_be_Reliably_Detected"},{"title":"[2303.11156v3] Can AI-Generated Text be Reliably Detected?","url":"https://arxiv.org/abs/2303.11156v3"},{"title":"Can AI-Generated Text be Reliably Detected?","url":"https://scispace.com/pdf/can-ai-generated-text-be-reliably-detected-1p8qe3ww.pdf"},{"title":"[2303.11156v4] Can AI-Generated Text be Reliably Detected?","url":"https://arxiv.org/abs/2303.11156v4"}]

Based on the search results, I found information about the paper "Can AI-Generated Text be Reliably Detected?" by Sadasivan and colleagues. The paper has a submission to ICLR 2024 as indicated by certification of compliance with submission instructions on https://iclr.cc/Conferences/2024/AuthorGuide.

However, the search results I found do not contain specific information about whether the paper was accepted or rejected by ICLR 2024. The paper a
…[truncated 487 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_bib-year-audit_20260515T174748",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 48 · 2026-05-15T17:54:07.233834+00:00_

Web search results for query: ""Through the Looking Glass" Munir Siddiqui Dengel Ahmed synthetic text attribution venue year"

Links: [{"title":"Through the Looking Glass: Learning to Attribute Synthetic Text Generated by Language Models - ACL Anthology","url":"https://aclanthology.org/2021.eacl-main.155/"},{"title":"[PDF] Through the Looking Glass: Learning to Attribute Synthetic Text Generated by Language Models | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Through-the-Looking-Glass:-Learning-to-Attribute-by-Munir-Batool/03e6b951e3665d28a7beeef87fcb1c9baecfd396"},{"title":"EACL2021: Through the Looking Glass: Learning to Attribute Synthetic Text Generated by Language Models","url":"https://www.virtual2021.eacl.org/paper_main.753.html"},{"title":"Through the Looking Glass: Learning to Attribute Synthetic Text Generated by Language Models | Request PDF","url":"https://www.researchgate.net/publication/355428226_Through_the_Looking_Glass_Learning_to_Attribute_Synthetic_Text_Generated_by_Language_Models"},{"title":"(PDF) Through the Looking Glass: Learning to Attribute Synthetic Text Generated by Language Models","url":"https://www.academia.edu/67763523/Through_the_Looking_Glass_Learning_to_Attribute_Synthetic_Text_Generated_by_Language_Models"},{"title":"Through the Looking Glass: Learning to Attribute Synthetic Text Generated by Language Models - researchr publication","url":"https://researchr.org/publication/MunirBSSZ21"},{"title":"Through the Looking Glass:","url":"https://web.cs.ucdavis.edu/~zubair/files/lm-eacl2021.pdf"},{"title":"(PDF) Through the looking glass","url":"https://www.academia.edu/57037772/Through_the_looking_glass"},{"title":"Through the Looking Glass | Columbia University Press","url":"https://cup.columbia.edu/book/through-the-looking-glass/9788323342908/"},{"title":"Through the Looking Glass - Madlik Disruptive Torah","url":"https://madlik.substack.com/p/through-the-looking-glass"}]

Based on the search results, I found informa
…[truncated 960 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_bib-year-audit_20260515T174748",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 49 · 2026-05-15T17:54:07.234003+00:00_

Web search results for query: ""A Survey on LLM-Generated Text Detection" Wu "Computational Linguistics" MIT Press 2025"

Links: [{"title":"A Survey on LLM-Generated Text Detection: Necessity, Methods, and Future Directions | Computational Linguistics | MIT Press","url":"https://direct.mit.edu/coli/article/51/1/275/127462/A-Survey-on-LLM-Generated-Text-Detection-Necessity"},{"title":"A Survey on LLM-Generated Text Detection: Necessity, Methods, and Future Directions - ACL Anthology","url":"https://aclanthology.org/2025.cl-1.8/"},{"title":"[2310.14724] A Survey on LLM-Generated Text Detection: Necessity, Methods, and Future Directions","url":"https://arxiv.org/abs/2310.14724"},{"title":"A Survey on LLM-Generated Text Detection: Necessity, Methods, and Future Directions | Computational Linguistics","url":"https://submissions.cljournal.org/index.php/cljournal/article/view/2687"},{"title":"[PDF] A Survey on LLM-generated Text Detection: Necessity, Methods, and Future Directions | Semantic Scholar","url":"https://www.semanticscholar.org/paper/A-Survey-on-LLM-generated-Text-Detection:-Methods,-Wu-Yang/a09d3686285f609b60b18b5935da64b29a5cce0f"},{"title":"RepreGuard: Detecting LLM-Generated Text by Revealing Hidden Representation Patterns | Transactions of the Association for Computational Linguistics | MIT Press","url":"https://direct.mit.edu/tacl/article/doi/10.1162/TACL.a.61/134537/RepreGuard-Detecting-LLM-Generated-Text-by"},{"title":"GitHub - NLP2CT/LLM-generated-Text-Detection: A survey and reflection on the latest research breakthroughs in LLM-generated Text detection, including data, detectors, metrics, current issues and future directions. · GitHub","url":"https://github.com/NLP2CT/LLM-generated-Text-Detection"},{"title":"A Survey on LLM-Generated Text Detection:","url":"https://fah.um.edu.mo/wp-content/uploads/2025/10/coli_a_00549.pdf"},{"title":"On the Detectability of LLM-Generated Text: What Exactly Is LLM-Generated Text?","url":"https://arxiv.org/html/2510.208
…[truncated 1125 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_bib-year-audit_20260515T174748",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 50 · 2026-05-15T17:54:07.234165+00:00_

Web search results for query: ""Automatic Detection of Machine Generated Text Critical Survey" Jawahar COLING 2020"

Links: [{"title":"Automatic Detection of Machine Generated Text: A Critical Survey - ACL Anthology","url":"https://aclanthology.org/2020.coling-main.208/"},{"title":"GitHub - UBC-NLP/coling2020_machine_generated_text: Automatic Detection of Machine Generated Text: A Critical Survey","url":"https://github.com/UBC-NLP/coling2020_machine_generated_text"},{"title":"Automatic Detection of Machine Generated Text: A Critical Survey | Request PDF","url":"https://www.researchgate.net/publication/348344789_Automatic_Detection_of_Machine_Generated_Text_A_Critical_Survey"},{"title":"Automatic Detection of Machine Generated Text: A Critical ...","url":"https://aclanthology.org/2020.coling-main.208.pdf"},{"title":"[PDF] Automatic Detection of Machine Generated Text: A Critical Survey | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Automatic-Detection-of-Machine-Generated-Text:-A-Jawahar-Abdul-Mageed/9438bc5626b2d9a771cecc7a41ecabf6639db53c"},{"title":"(PDF) Automatic Detection of Machine Generated Text: A Critical Survey","url":"https://www.researchgate.net/publication/345261249_Automatic_Detection_of_Machine_Generated_Text_A_Critical_Survey"},{"title":"Papers with Code - Automatic Detection of Machine Generated Text: A Critical Survey","url":"https://paperswithcode.com/paper/automatic-detection-of-machine-generated-text"},{"title":"Table 1 from Automatic Detection of Machine Generated Text: A Critical Survey | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Automatic-Detection-of-Machine-Generated-Text:-A-Jawahar-Abdul-Mageed/9438bc5626b2d9a771cecc7a41ecabf6639db53c/figure/0"},{"title":"Table 2 from Automatic Detection of Machine Generated Text: A Critical Survey | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Automatic-Detection-of-Machine-Generated-Text:-A-Jawahar-Abdul-Mageed/9438bc5626b2d9a771cecc7a41ecabf6639db
…[truncated 1813 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_bib-year-audit_20260515T174748",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 51 · 2026-05-15T17:54:07.234319+00:00_

Web search results for query: ""Position On the Possibilities of AI-Generated Text Detection" Chakraborty ICML 2024"

Links: [{"title":"Position: On the Possibilities of AI-Generated Text Detection","url":"https://proceedings.mlr.press/v235/chakraborty24a.html"},{"title":"Position: On the Possibilities of AI-Generated Text Detection | OpenReview","url":"https://openreview.net/forum?id=CJbhtpcyGL"},{"title":"Position: On the Possibilities of AI-Generated Text Detection","url":"https://raw.githubusercontent.com/mlresearch/v235/main/assets/chakraborty24a/chakraborty24a.pdf"},{"title":"Position: On the possibilities of AI-generated text detection","url":"https://dl.acm.org/doi/10.5555/3692070.3692305"},{"title":"[2304.04736] On the Possibilities of AI-Generated Text Detection","url":"https://arxiv.org/abs/2304.04736"},{"title":"ICML Poster Position: On the Possibilities of AI-Generated Text Detection","url":"https://icml.cc/virtual/2024/poster/34689"},{"title":"On the Possibilities of AI-Generated Text Detection: A Sample Complexity Analysis | OpenReview","url":"https://openreview.net/forum?id=oxEER3kZ9M"},{"title":"A Survey on the Possibilities & Impossibilities of AI-generated Text Detection | Semantic Scholar","url":"https://www.semanticscholar.org/paper/f582daa2f2822c0aa1291fe3925f69c25280e37e"},{"title":"[PDF] On the Possibilities of AI-Generated Text Detection | Semantic Scholar","url":"https://www.semanticscholar.org/paper/On-the-Possibilities-of-AI-Generated-Text-Detection-Chakraborty-Bedi/1c9693a721271e3f915f0f0b8159578495d5c815"},{"title":"On the Possibilities of AI-Generated Text Detection","url":"https://arxiv.org/pdf/2304.04736"}]

I found the paper you're looking for! Here's what I found:

**Paper Title:** Position: On the Possibilities of AI-Generated Text Detection

**Authors:** Souradip Chakraborty, Amrit Bedi, Sicheng Zhu, Bang An, Dinesh Manocha (and Furong Huang)

**Publication:** Proceedings of the 41st International Conference on Machine Learning, 
…[truncated 928 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_bib-year-audit_20260515T174748",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 52 · 2026-05-15T17:54:07.234487+00:00_

Web search results for query: ""OLMo Accelerating the Science of Language Models" Groeneveld ACL 2024"

Links: [{"title":"OLMo: Accelerating the Science of Language Models - ACL Anthology","url":"https://aclanthology.org/2024.acl-long.841/"},{"title":"[2402.00838] OLMo: Accelerating the Science of Language Models","url":"https://arxiv.org/abs/2402.00838"},{"title":"OLMo: Accelerating the Science of Language Models | Request PDF","url":"https://www.researchgate.net/publication/384217754_OLMo_Accelerating_the_Science_of_Language_Models"},{"title":"OLMo : Accelerating the Science of Language Models","url":"https://aclanthology.org/2024.acl-long.841.pdf"},{"title":"[PDF] OLMo: Accelerating the Science of Language Models | Semantic Scholar","url":"https://www.semanticscholar.org/paper/OLMo:-Accelerating-the-Science-of-Language-Models-Groeneveld-Beltagy/ac45bbf9940512d9d686cf8cd3a95969bc313570"},{"title":"OLMo: Accelerating the Science of Language Models Dirk Groeneveld>a> Iz Beltagy>a> - Bar-Ilan University","url":"https://cris.biu.ac.il/en/publications/olmo-accelerating-the-science-of-language-models-dirk-groenevelds"},{"title":"OLMo : Accelerating the Science of Language Models Dirk Groeneveldα Iz Beltagyα","url":"https://arxiv.org/pdf/2402.00838"},{"title":"Allen School News » A way with words and trillions of tokens: Allen School researchers recognized at ACL 2024 for expanding the capabilities of language models","url":"https://news.cs.washington.edu/2024/10/08/a-way-with-words-and-trillions-of-tokens-allen-school-researchers-recognized-at-acl-2024-for-expanding-the-capabilities-of-language-models/"},{"title":"OLMo: Accelerating the Science of Language Models","url":"https://www.researchhub.com/paper/6025716/olmo-accelerating-the-science-of-language-models"},{"title":"OLMo : Accelerating the Science of Language Models","url":"https://arxiv.org/html/2402.00838v1"}]

I found the paper you're looking for! Here are the key details:

## Publication Information

The paper
…[truncated 1547 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_bib-year-audit_20260515T174748",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool call

_source line 53 · 2026-05-15T17:54:07.234673+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "site:proceedings.iclr.cc \"Can AI-Generated Text be Reliably Detected\" 2024"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_bib-year-audit_20260515T174748",
  "tool": "WebSearch",
  "tool_args": {
    "query": "site:proceedings.iclr.cc \"Can AI-Generated Text be Reliably Detected\" 2024"
  }
}
```

</details>

---

### Tool call

_source line 54 · 2026-05-15T17:54:07.234808+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"Muhammad Adnan Munir\" \"Through the Looking Glass\" synthetic text DFKI"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_bib-year-audit_20260515T174748",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"Muhammad Adnan Munir\" \"Through the Looking Glass\" synthetic text DFKI"
  }
}
```

</details>

---

### Tool call

_source line 55 · 2026-05-15T17:54:07.234921+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"A Survey on LLM-Generated Text Detection\" Wu Zhu Li Decheng authors Computational Linguistics"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_bib-year-audit_20260515T174748",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"A Survey on LLM-Generated Text Detection\" Wu Zhu Li Decheng authors Computational Linguistics"
  }
}
```

</details>

---

### Tool call

_source line 56 · 2026-05-15T17:54:07.235032+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"SemEval-2024 Task 8\" Wang Mansurov publication venue year"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_bib-year-audit_20260515T174748",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"SemEval-2024 Task 8\" Wang Mansurov publication venue year"
  }
}
```

</details>

---

### Tool call

_source line 57 · 2026-05-15T17:54:07.235144+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"Data Selection for Language Models via Importance Resampling\" Xie DSIR NeurIPS 2023"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_bib-year-audit_20260515T174748",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"Data Selection for Language Models via Importance Resampling\" Xie DSIR NeurIPS 2023"
  }
}
```

</details>

---

### Tool call

_source line 58 · 2026-05-15T17:54:07.235253+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"QuRating Selecting High-Quality Data\" Wettig ICML 2024"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_bib-year-audit_20260515T174748",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"QuRating Selecting High-Quality Data\" Wettig ICML 2024"
  }
}
```

</details>

---

### Tool result

_source line 59 · 2026-05-15T17:54:07.235367+00:00_

Web search results for query: "site:proceedings.iclr.cc "Can AI-Generated Text be Reliably Detected" 2024"

Links: [{"title":"Published as a conference paper at ICLR 2024","url":"https://proceedings.iclr.cc/paper_files/paper/2024/file/6b8c6f846c3575e1d1ad496abea28826-Paper-Conference.pdf"},{"title":"can watermarked llms be identified by users","url":"https://proceedings.iclr.cc/paper_files/paper/2025/file/596b9662ebbc92686901e8a9665c92ed-Paper-Conference.pdf"}]

The search found a relevant paper published at ICLR 2024. The first result appears to be a conference paper discussing AI-generated text detection methods. Based on the content snippets, the paper focuses on zero-shot detection of machine-generated text as a binary classification problem, aiming to determine whether a passage is human-authored or produced by a source model.

The paper explores both white-box settings where the source model is accessible to aid in classification, and black-box settings where surrogate models are used instead. The research compares Fast-DetectGPT with DetectGPT and other baseline methods like NPR and DNA-GPT.

The PDF is available at: https://proceedings.iclr.cc/paper_files/paper/2024/file/6b8c6f846c3575e1d1ad496abea28826-Paper-Conference.pdf


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_bib-year-audit_20260515T174748",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 60 · 2026-05-15T17:54:07.235504+00:00_

Web search results for query: ""Muhammad Adnan Munir" "Through the Looking Glass" synthetic text DFKI"

Links: [{"title":"Through the Looking Glass: Learning to Attribute Synthetic Text Generated by Language Models - ACL Anthology","url":"https://aclanthology.org/2021.eacl-main.155/"},{"title":"[PDF] Through the Looking Glass: Learning to Attribute Synthetic Text Generated by Language Models | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Through-the-Looking-Glass:-Learning-to-Attribute-by-Munir-Batool/03e6b951e3665d28a7beeef87fcb1c9baecfd396"},{"title":"Through the Looking Glass: Learning to Attribute Synthetic Text Generated by Language Models | Request PDF","url":"https://www.researchgate.net/publication/355428226_Through_the_Looking_Glass_Learning_to_Attribute_Synthetic_Text_Generated_by_Language_Models"},{"title":"EACL2021: Through the Looking Glass: Learning to Attribute Synthetic Text Generated by Language Models","url":"https://www.virtual2021.eacl.org/paper_main.753.html"},{"title":"(PDF) Through the Looking Glass: Learning to Attribute Synthetic Text Generated by Language Models","url":"https://www.academia.edu/67763523/Through_the_Looking_Glass_Learning_to_Attribute_Synthetic_Text_Generated_by_Language_Models"},{"title":"Through the looking glass: Learning to attribute synthetic text generated by language models","url":"https://papertalk.org/papertalks/28247"},{"title":"Through the Looking Glass: Learning to Attribute Synthetic ...","url":"https://www.connectedpapers.com/main/03e6b951e3665d28a7beeef87fcb1c9baecfd396/Through-the-Looking-Glass:-Learning-to-Attribute-Synthetic-Text-Generated-by-Language-Models/graph"}]

Based on the search results, I found relevant information about the paper "Through the Looking Glass: Learning to Attribute Synthetic Text Generated by Language Models."

However, I notice that the search results show the authors as Shaoor Munir, Brishna Batool, Zubair Shafiq, Padmini Srinivasan, and Fareed Zaffar, not "Muham
…[truncated 883 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_bib-year-audit_20260515T174748",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 61 · 2026-05-15T17:54:07.235713+00:00_

Web search results for query: ""A Survey on LLM-Generated Text Detection" Wu Zhu Li Decheng authors Computational Linguistics"

Links: [{"title":"A Survey on LLM-Generated Text Detection: Necessity, Methods, and Future Directions - ACL Anthology","url":"https://aclanthology.org/2025.cl-1.8/"},{"title":"A Survey on LLM-Generated Text Detection: Necessity, Methods, and Future Directions | Computational Linguistics | MIT Press","url":"https://direct.mit.edu/coli/article/51/1/275/127462/A-Survey-on-LLM-Generated-Text-Detection-Necessity"},{"title":"[2310.14724] A Survey on LLM-Generated Text Detection: Necessity, Methods, and Future Directions","url":"https://arxiv.org/abs/2310.14724"},{"title":"A Survey on LLM-Generated Text Detection: Necessity, Methods, and Future Directions | Computational Linguistics","url":"https://submissions.cljournal.org/index.php/cljournal/article/view/2687"},{"title":"On the Detectability of LLM-Generated Text: What Exactly Is LLM-Generated Text?","url":"https://arxiv.org/html/2510.20810v1"},{"title":"A Survey on LLM-Generated Text Detection: Necessity, Methods, and Future Directions","url":"https://arxiv.org/html/2310.14724v3"},{"title":"A Survey on LLM-Generated Text Detection:","url":"https://arxiv.org/pdf/2310.14724"},{"title":"[PDF] A Survey on LLM-generated Text Detection: Necessity, Methods, and Future Directions | Semantic Scholar","url":"https://www.semanticscholar.org/paper/A-Survey-on-LLM-generated-Text-Detection:-Methods,-Wu-Yang/a09d3686285f609b60b18b5935da64b29a5cce0f"},{"title":"GitHub - NLP2CT/LLM-generated-Text-Detection: A survey and reflection on the latest research breakthroughs in LLM-generated Text detection, including data, detectors, metrics, current issues and future directions. · GitHub","url":"https://github.com/NLP2CT/LLM-generated-Text-Detection"},{"title":"GitHub - junchaoIU/LLM-generated-Text-Detection: A survey and reflection on the latest research breakthroughs in LLM-generated Text detection, including data, 
…[truncated 974 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_bib-year-audit_20260515T174748",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 62 · 2026-05-15T17:54:07.235892+00:00_

Web search results for query: ""SemEval-2024 Task 8" Wang Mansurov publication venue year"

Links: [{"title":"SemEval-2024 Task 8: Multidomain, Multimodel and Multilingual Machine-Generated Text Detection - ACL Anthology","url":"https://aclanthology.org/2024.semeval-1.279/"},{"title":"SemEval-2024 Task 8: Multigenerator, Multidomain, and ...","url":"https://github.com/mbzuai-nlp/SemEval2024-task8"},{"title":"[2404.14183] SemEval-2024 Task 8: Multidomain, Multimodel and Multilingual Machine-Generated Text Detection","url":"https://arxiv.org/abs/2404.14183"},{"title":"[PDF] SemEval-2024 Task 8: Multidomain, Multimodel and Multilingual Machine-Generated Text Detection | Semantic Scholar","url":"https://www.semanticscholar.org/paper/SemEval-2024-Task-8:-Multidomain,-Multimodel-and-Wang-Mansurov/c56eab12bd00e2fe28868af21d518044d66df00d"},{"title":"SemEval-2024 Tasks | SemEval-2024","url":"https://semeval.github.io/SemEval2024/tasks.html"},{"title":"SemEval-2024 Task 8: Multidomain, Multimodel and Multilingual Machine-Generated Text Detection","url":"https://arxiv.org/html/2404.14183v1"},{"title":"SemEval-2024 Task 8: Multidomain, Multimodel and Multilingual Machine-Generated Text Detection - NYU Scholars","url":"https://nyuscholars.nyu.edu/en/publications/semeval-2024-task-8-multidomain-multimodel-and-multilingual-machi"},{"title":"SemEval-2024 Task 8","url":"https://iris.cnr.it/bitstream/20.500.14243/532501/1/2024.semeval-1.279.pdf"},{"title":"TueCICL at SemEval-2024 Task 8: Resource-efficient approaches for machine-generated text detection","url":"https://www.researchgate.net/publication/382632408_TueCICL_at_SemEval-2024_Task_8_Resource-efficient_approaches_for_machine-generated_text_detection"},{"title":"NewbieML at SemEval-2024 Task 8: Ensemble Approach for Multidomain Machine-Generated Text Detection | Request PDF","url":"https://www.researchgate.net/publication/382633120_NewbieML_at_SemEval-2024_Task_8_Ensemble_Approach_for_Multidomain_Machine-Generated_Text_Detect
…[truncated 601 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_bib-year-audit_20260515T174748",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 63 · 2026-05-15T17:54:07.236066+00:00_

Web search results for query: ""Data Selection for Language Models via Importance Resampling" Xie DSIR NeurIPS 2023"

Links: [{"title":"NeurIPS Poster Data Selection for Language Models via Importance Resampling","url":"https://neurips.cc/virtual/2023/poster/70154"},{"title":"[2302.03169] Data Selection for Language Models via Importance Resampling","url":"https://arxiv.org/abs/2302.03169"},{"title":"Data Selection for Language Models via Importance Resampling","url":"https://proceedings.neurips.cc//paper_files/paper/2023/hash/6b9aa8f418bde2840d5f4ab7a02f663b-Abstract-Conference.html"},{"title":"Data Selection for Language Models via Importance Resampling","url":"https://openreview.net/pdf?id=uPSQv0leAu"},{"title":"Data Selection for Language Models via Importance Resampling - ADS","url":"https://ui.adsabs.harvard.edu/abs/2023arXiv230203169X/abstract"},{"title":"[Quick Review] Data Selection for Language Models via Importance Resampling","url":"https://liner.com/review/data-selection-for-language-models-via-importance-resampling"},{"title":"GitHub - p-lambda/dsir: DSIR large-scale data selection framework for language model training · GitHub","url":"https://github.com/p-lambda/dsir"},{"title":"Data Selection for Language Models via Importance Resampling","url":"https://www.researchgate.net/publication/368333487_Data_Selection_for_Language_Models_via_Importance_Resampling"},{"title":"Data Selection for Language Models via Importance Resampling | OpenReview","url":"https://openreview.net/forum?id=uPSQv0leAu"},{"title":"Data selection for language models via importance resampling | Proceedings of the 37th International Conference on Neural Information Processing Systems","url":"https://dl.acm.org/doi/10.5555/3666122.3667604"}]

Based on the search results, here's information about the paper "Data Selection for Language Models via Importance Resampling":

## Overview

Data Selection with Importance Resampling (DSIR) is an efficient and scalable framework that estimates 
…[truncated 1573 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_bib-year-audit_20260515T174748",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 64 · 2026-05-15T17:54:07.236234+00:00_

Web search results for query: ""QuRating Selecting High-Quality Data" Wettig ICML 2024"

Links: [{"title":"GitHub - princeton-nlp/QuRating: [ICML 2024] Selecting High-Quality Data for Training Language Models","url":"https://github.com/princeton-nlp/QuRating"},{"title":"[2402.09739] QuRating: Selecting High-Quality Data for Training Language Models","url":"https://arxiv.org/abs/2402.09739"},{"title":"ICLR QuRating: Selecting High-Quality Data for Training Language Models","url":"https://iclr.cc/virtual/2024/21159"},{"title":"QuRating: selecting high-quality data for training language ...","url":"https://dl.acm.org/doi/10.5555/3692070.3694241"},{"title":"QuRating: Selecting High-Quality Data for Training Language Models","url":"https://proceedings.mlr.press/v235/wettig24a.html"},{"title":"ICLR QuRating: Selecting High-Quality Data for Training Lanugage Models","url":"https://iclr.cc/virtual/2024/22410"},{"title":"[PDF] QuRating: Selecting High-Quality Data for Training Language Models | Semantic Scholar","url":"https://www.semanticscholar.org/paper/QuRating:-Selecting-High-Quality-Data-for-Training-Wettig-Gupta/34efdeaf0a78d6906b4da7335afc7182df11f639"},{"title":"[2402.09739v3] QuRating: Selecting High-Quality Data for Training Language Models","url":"https://arxiv.org/abs/2402.09739v3"},{"title":"QuRating: Selecting High-Quality Data for Training Language Models - ADS","url":"https://ui.adsabs.harvard.edu/abs/2024arXiv240209739W/abstract"},{"title":"QuRating: Selecting High-Quality Data for Training Language Models | OpenReview","url":"https://openreview.net/forum?id=GLGYYqPwjy"}]

Based on the search results, here's what I found about the QuRating paper:

## Overview

QuRating is a method for selecting pre-training data that can capture human intuitions about data quality. The paper was authored by Alexander Wettig, Aatmik Gupta, Saumya Malik, and Danqi Chen, and was presented at the International Conference on Machine Learning (ICML) in 2024.

## Key Contributions
…[truncated 1040 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_bib-year-audit_20260515T174748",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 65 · 2026-05-15T17:54:07.236409+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Sadasivan Kumar \"Can AI-Generated Text be Reliably Detected\" ICLR 2024 accepted proceedings.iclr"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_bib-year-audit_20260515T174748",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Sadasivan Kumar \"Can AI-Generated Text be Reliably Detected\" ICLR 2024 accepted proceedings.iclr"
  }
}
```

</details>

---

### Tool call

_source line 66 · 2026-05-15T17:54:07.236532+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"Scalable Watermarking for Identifying Large Language Model Outputs\" SynthID Nature 2024"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_bib-year-audit_20260515T174748",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"Scalable Watermarking for Identifying Large Language Model Outputs\" SynthID Nature 2024"
  }
}
```

</details>

---

### Tool call

_source line 67 · 2026-05-15T17:54:07.236667+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"CCNet Extracting High Quality Monolingual Datasets\" Wenzek LREC 2020"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_bib-year-audit_20260515T174748",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"CCNet Extracting High Quality Monolingual Datasets\" Wenzek LREC 2020"
  }
}
```

</details>

---

### Tool call

_source line 68 · 2026-05-15T17:54:07.236778+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"Rank Consistent Ordinal Regression\" Cao Raschka \"Pattern Recognition Letters\" year"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_bib-year-audit_20260515T174748",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"Rank Consistent Ordinal Regression\" Cao Raschka \"Pattern Recognition Letters\" year"
  }
}
```

</details>

---

### Tool call

_source line 69 · 2026-05-15T17:54:07.236886+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"Curse of Recursion\" Shumailov Nature volume year published 2024"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_bib-year-audit_20260515T174748",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"Curse of Recursion\" Shumailov Nature volume year published 2024"
  }
}
```

</details>

---

### Tool call

_source line 70 · 2026-05-15T17:54:07.236991+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"Mapping the Increasing Use of LLMs in Scientific Papers\" Liang COLM 2024 conference"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_bib-year-audit_20260515T174748",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"Mapping the Increasing Use of LLMs in Scientific Papers\" Liang COLM 2024 conference"
  }
}
```

</details>

---

### Tool result

_source line 71 · 2026-05-15T17:54:07.237121+00:00_

Web search results for query: ""Rank Consistent Ordinal Regression" Cao Raschka "Pattern Recognition Letters" year"

Links: [{"title":"[1901.07884] Rank consistent ordinal regression for neural networks with application to age estimation","url":"https://arxiv.org/abs/1901.07884"},{"title":"(PDF) Rank consistent ordinal regression for neural networks with application to age estimation","url":"https://www.researchgate.net/publication/347503290_Rank_consistent_ordinal_regression_for_neural_networks_with_application_to_age_estimation"},{"title":"Rank consistent ordinal regression for neural networks with ...","url":"https://sebastianraschka.com/pdf/papers/2020-coral.pdf"},{"title":"Rank consistent ordinal regression for neural networks with application to age estimation - ScienceDirect","url":"https://www.sciencedirect.com/science/article/pii/S016786552030413X"},{"title":"GitHub - Raschka-research-group/coral-cnn: Rank Consistent Ordinal Regression for Neural Networks with Application to Age Estimation · GitHub","url":"https://github.com/Raschka-research-group/coral-cnn"},{"title":"Deep Neural Networks for Rank-Consistent Ordinal ...","url":"https://arxiv.org/pdf/2111.08851"},{"title":"1 Rank-consistent ordinal regression for neural networks","url":"https://sebastianraschka.com/pdf/papers/2020-coral2-2020-july.pdf"},{"title":"[2111.08851] Deep Neural Networks for Rank-Consistent Ordinal Regression Based On Conditional Probabilities","url":"https://arxiv.org/abs/2111.08851"},{"title":"GitHub - Raschka-research-group/coral-pytorch: CORAL and CORN implementations for ordinal regression with deep neural networks. · GitHub","url":"https://github.com/Raschka-research-group/coral-pytorch"},{"title":"Deep neural networks for rank-consistent ordinal regression based on conditional probabilities | Pattern Analysis and Applications | Springer Nature Link","url":"https://link.springer.com/article/10.1007/s10044-023-01181-9"}]

Based on the search results, I found the information yo
…[truncated 347 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_bib-year-audit_20260515T174748",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 72 · 2026-05-15T17:54:07.237276+00:00_

Web search results for query: "Sadasivan Kumar "Can AI-Generated Text be Reliably Detected" ICLR 2024 accepted proceedings.iclr"

Links: [{"title":"Can AI-Generated Text be Reliably Detected?","url":"https://arxiv.org/pdf/2303.11156"},{"title":"[PDF] Can AI-Generated Text be Reliably Detected? | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Can-AI-Generated-Text-be-Reliably-Detected-Sadasivan-Kumar/5ee8bb4fc80a291b2e416a2a879e7153a783d7e9"},{"title":"Can AI-Generated Text be Reliably Detected?","url":"https://bibbase.org/network/publication/sadasivan-kumar-balasubramanian-wang-feizi-canaigeneratedtextbereliablydetected-2024"},{"title":"Can AI-Generated Text be Reliably Detected? - ADS","url":"https://ui.adsabs.harvard.edu/abs/2023arXiv230311156S/abstract"},{"title":"(PDF) Can AI-Generated Text be Reliably Detected?","url":"https://www.researchgate.net/publication/369380286_Can_AI-Generated_Text_be_Reliably_Detected"},{"title":"[2303.11156] Can AI-Generated Text be Reliably Detected?","url":"https://arxiv.org/abs/2303.11156"},{"title":"Can AI-Generated Text be Reliably Detected? | OpenReview","url":"https://openreview.net/forum?id=NvSwR4IvLO"},{"title":"Can AI-Generated Text be Reliably Detected? Stress Testing AI Text Detectors Under Various Attacks | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Can-AI-Generated-Text-be-Reliably-Detected-Stress-Sadasivan-Kumar/42f7d83e6c20fd4aaf3e3f53b18ab7db221ee300"},{"title":"[2303.11156v3] Can AI-Generated Text be Reliably Detected?","url":"https://arxiv.org/abs/2303.11156v3"},{"title":"Can AI-Generated Text be Reliably Detected?","url":"https://scispace.com/pdf/can-ai-generated-text-be-reliably-detected-1p8qe3ww.pdf"}]

Based on the search results, I found information about the paper "Can AI-Generated Text be Reliably Detected?" by Sadasivan, Kumar, and colleagues. 

The paper was submitted to ICLR 2024 according to the OpenReview submission guidelines. The paper was published in February 2024
…[truncated 844 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_bib-year-audit_20260515T174748",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 73 · 2026-05-15T17:54:07.237437+00:00_

Web search results for query: ""CCNet Extracting High Quality Monolingual Datasets" Wenzek LREC 2020"

Links: [{"title":"CCNet: Extracting High Quality Monolingual Datasets from Web Crawl Data - ACL Anthology","url":"https://aclanthology.org/2020.lrec-1.494/"},{"title":"CCNet: Extracting High Quality Monolingual Datasets from ...","url":"https://aclanthology.org/2020.lrec-1.494.pdf"},{"title":"CCNet: Extracting High Quality Monolingual Datasets from ...","url":"http://www.lrec-conf.org/proceedings/lrec2020/pdf/2020.lrec-1.494.pdf"},{"title":"CCNet: Extracting High Quality Monolingual Datasets from Web Crawl Data - ACL Anthology","url":"https://arne.chark.eu/anthology/2020.lrec-1.494/"},{"title":"[1911.00359] CCNet: Extracting High Quality Monolingual Datasets from Web Crawl Data","url":"https://arxiv.org/abs/1911.00359"},{"title":"Papers with Code - CCNet: Extracting High Quality Monolingual Datasets from Web Crawl Data","url":"https://paperswithcode.com/paper/ccnet-extracting-high-quality-monolingual"},{"title":"CCNet: Extracting High Quality Monolingual Datasets from Web Crawl Data. | BibSonomy","url":"https://www.bibsonomy.org/bibtex/245540f9667239913db153792be9fff73/dblp"},{"title":"@inproceedings{wenzek-etal-2020-ccnet,","url":"https://aclanthology.org/2020.lrec-1.494.bib"},{"title":"[PDF] CCNet: Extracting High Quality Monolingual Datasets from Web Crawl Data | Semantic Scholar","url":"https://www.semanticscholar.org/paper/CCNet:-Extracting-High-Quality-Monolingual-Datasets-Wenzek-Lachaux/c20c68c45127439139a08adb0b1f2b8354a94d6c"},{"title":"GitHub - facebookresearch/cc_net: Tools to download and cleanup Common Crawl data","url":"https://github.com/facebookresearch/cc_net"}]

I found the paper you're looking for. Here are the key details:

**Paper Title:** CCNet: Extracting High Quality Monolingual Datasets from Web Crawl Data (Wenzek et al., LREC 2020)

**Authors:** Guillaume Wenzek, Marie-Anne Lachaux, Alexis Conneau, Vishrav Chaudhary, Francisco Guzmán, Arma
…[truncated 757 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_bib-year-audit_20260515T174748",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 74 · 2026-05-15T17:54:07.237621+00:00_

Web search results for query: ""Scalable Watermarking for Identifying Large Language Model Outputs" SynthID Nature 2024"

Links: [{"title":"Scalable watermarking for identifying large language model outputs | Nature","url":"https://www.nature.com/articles/s41586-024-08025-4"},{"title":"GitHub - google-deepmind/synthid-text · GitHub","url":"https://github.com/google-deepmind/synthid-text"},{"title":"Scalable watermarking for identifying large language ...","url":"https://pubmed.ncbi.nlm.nih.gov/39443777/"},{"title":"Scalable watermarking for identifying large language model outputs - ADS","url":"https://ui.adsabs.harvard.edu/abs/2024Natur.634..818D/abstract"},{"title":"Scalable watermarking for identifying large language model outputs - PMC","url":"https://pmc.ncbi.nlm.nih.gov/articles/PMC11499265/"},{"title":"Scalable watermarking for identifying large language model outputs | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Scalable-watermarking-for-identifying-large-model-Dathathri-See/89bd8efe0b9c0427cb7814d7b8c2b0190d2ffa9e"},{"title":"Scalable watermarking for identifying large language model outputs – ScienceOpen","url":"https://www.scienceopen.com/document?vid=e36b034b-6be1-439b-bccb-f413efc57773"},{"title":"Scalable Watermarking for LLM Outputs | PDF | Information Science | Computing","url":"https://es.scribd.com/document/974409962/s41586-024-08025-4-1-1-5"},{"title":"Scalable watermarking for identifying large language model outputs","url":"https://ideas.repec.org/a/nat/nature/v634y2024i8035d10.1038_s41586-024-08025-4.html"},{"title":"LLM Watermark Series — SynthID: Scalable watermarking for identifying LLM outputs | by Kiel Dang | Medium","url":"https://medium.com/@kirudang/llm-watermark-series-synthid-scalable-watermarking-for-identifying-llm-outputs-ad49a0c55a4c"}]

I found comprehensive information about the paper. Here's a summary of the search results:

## Overview

"SynthID-Text is a production-ready text watermarking scheme that preser
…[truncated 1341 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_bib-year-audit_20260515T174748",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 75 · 2026-05-15T17:54:07.237786+00:00_

Web search results for query: ""Curse of Recursion" Shumailov Nature volume year published 2024"

Links: [{"title":"[2305.17493] The Curse of Recursion: Training on Generated Data Makes Models Forget","url":"https://arxiv.org/abs/2305.17493"},{"title":"[PDF] The Curse of Recursion: Training on Generated Data Makes Models Forget | Semantic Scholar","url":"https://www.semanticscholar.org/paper/The-Curse-of-Recursion:-Training-on-Generated-Data-Shumailov-Shumaylov/155aec5cff650263a4c71136f97570611d1bba7a"},{"title":"The Curse of Recursion: Training on Generated Data Makes Models Forget | AI Research Paper Details","url":"https://www.aimodels.fyi/papers/arxiv/curse-recursion-training-generated-data-makes-models"},{"title":"The Curse of Recursion: Training on Generated Data Makes Models Forget (2023) | Ilia Shumailov | 153 Citations","url":"https://scispace.com/papers/the-curse-of-recursion-training-on-generated-data-makes-34zgysyl"},{"title":"Recursive Pollution and Model Collapse Are Not the Same | BIML","url":"https://berryvilleiml.com/2026/01/10/recursive-pollution-and-model-collapse-are-not-the-same/"},{"title":"Published as a conference paper at ICLR 2025 STRONG MODEL COLLAPSE","url":"https://proceedings.iclr.cc/paper_files/paper/2025/file/284afdc2309f9667d2d4fb9290235b0c-Paper-Conference.pdf"},{"title":"What Is Model Collapse? | IBM","url":"https://www.ibm.com/think/topics/model-collapse"},{"title":"Is Model Collapse Inevitable? Breaking the Curse of Recursion by Accumulating Real and Synthetic Data","url":"https://arxiv.org/html/2404.01413v2"},{"title":"Addressing Concerns of Model Collapse from Synthetic Data in AI","url":"https://www.gretel.ai/blog/addressing-concerns-of-model-collapse-from-synthetic-data-in-ai"},{"title":"The Curse of Recursion: Training on Generated Data Makes Models Forget","url":"https://arxiv.org/html/2305.17493v3"}]

Based on the search results, I can provide you with information about "The Curse of Recursion" paper by Shumailov and colle
…[truncated 691 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_bib-year-audit_20260515T174748",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 76 · 2026-05-15T17:54:07.237953+00:00_

Web search results for query: ""Mapping the Increasing Use of LLMs in Scientific Papers" Liang COLM 2024 conference"

Links: [{"title":"Mapping the Increasing Use of LLMs in Scientific Papers | OpenReview","url":"https://openreview.net/forum?id=YX7QnhxESU"},{"title":"[2404.01268] Mapping the Increasing Use of LLMs in Scientific Papers","url":"https://arxiv.org/abs/2404.01268"},{"title":"Mapping the Increasing Use of LLMs in Scientific Papers","url":"https://openreview.net/pdf/eff0ea8ed41a89a9e267752af56df912888fee65.pdf"},{"title":"GitHub - Weixin-Liang/Mapping-the-Increasing-Use-of-LLMs-in-Scientific-Papers · GitHub","url":"https://github.com/Weixin-Liang/Mapping-the-Increasing-Use-of-LLMs-in-Scientific-Papers"},{"title":"Mapping the Increasing Use of LLMs in Scientific Papers","url":"https://arxiv.org/html/2404.01268v1"},{"title":"Mapping the Increasing Use of LLMs in Scientific Papers | BibSonomy","url":"https://www.bibsonomy.org/bibtex/28f3ef49cf074d7caa6cdd244449c11cf/diekhans"},{"title":"Quantifying large language model usage in scientific papers | Nature Human Behaviour","url":"https://www.nature.com/articles/s41562-025-02273-8"},{"title":"Liang 2024 Preprint Mapping Increasing Use LLMs in Scientific Papers | PDF | Bootstrapping (Statistics) | Statistics","url":"https://www.scribd.com/document/819741512/Liang-2024-Preprint-Mapping-Increasing-Use-LLMs-in-Scientific-Papers"},{"title":"Mapping the Increasing Use of LLMs in Scientific Papers","url":"https://www.semanticscholar.org/paper/Mapping-the-Increasing-Use-of-LLMs-in-Scientific-Liang-Zhang/882f3d1b718e833156ccd6f5bda3190cd06791ea"},{"title":"[Literature Review] Mapping the Increasing Use of LLMs in Scientific Papers","url":"https://www.themoonlight.io/en/review/mapping-the-increasing-use-of-llms-in-scientific-papers"}]

I found the paper you're looking for! Here's information about it:

## Paper Overview

"Mapping the Increasing Use of LLMs in Scientific Papers" was published as a conference paper at COLM 
…[truncated 1299 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_bib-year-audit_20260515T174748",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 77 · 2026-05-15T17:54:07.238128+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "openreview.net NvSwR4IvLO \"Can AI-Generated Text\" decision accepted rejected ICLR"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_bib-year-audit_20260515T174748",
  "tool": "WebSearch",
  "tool_args": {
    "query": "openreview.net NvSwR4IvLO \"Can AI-Generated Text\" decision accepted rejected ICLR"
  }
}
```

</details>

---

### Tool call

_source line 78 · 2026-05-15T17:54:07.238250+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"Qwen3 Technical Report\" arXiv 2025 2505.09388"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_bib-year-audit_20260515T174748",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"Qwen3 Technical Report\" arXiv 2025 2505.09388"
  }
}
```

</details>

---

### Tool call

_source line 79 · 2026-05-15T17:54:07.238363+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"Markovian Generation Chains in Large Language Models\" Geng arXiv 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_bib-year-audit_20260515T174748",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"Markovian Generation Chains in Large Language Models\" Geng arXiv 2026"
  }
}
```

</details>

---

### Tool call

_source line 80 · 2026-05-15T17:54:07.238473+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"Diversity Boosts AI-Generated Text Detection\" Basani Chen TMLR 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_bib-year-audit_20260515T174748",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"Diversity Boosts AI-Generated Text Detection\" Basani Chen TMLR 2026"
  }
}
```

</details>

---

### Tool result

_source line 81 · 2026-05-15T17:54:07.238603+00:00_

Web search results for query: "openreview.net NvSwR4IvLO "Can AI-Generated Text" decision accepted rejected ICLR"

Links: [{"title":"Can AI-Generated Text be Reliably Detected? | OpenReview","url":"https://openreview.net/forum?id=NvSwR4IvLO"}]

Based on the search results, I found the paper on OpenReview with ID NvSwR4IvLO. The paper empirically shows that AI-text detectors are not reliable in practical scenarios along with theoretical evidence. 

The authors develop a recursive paraphrasing attack to apply on AI text, which can break a whole range of detectors, including ones using watermarking schemes as well as neural network-based detectors, zero-shot classifiers, and retrieval-based detectors.

However, the search results provided do not include specific information about the final decision status (accepted or rejected) for this submission at ICLR. The page content shown is from the initial submission, dated October 13, 2023, but does not display the review decisions or final acceptance/rejection status.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_bib-year-audit_20260515T174748",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 82 · 2026-05-15T17:54:07.238759+00:00_

Web search results for query: ""Qwen3 Technical Report" arXiv 2025 2505.09388"

Links: [{"title":"[2505.09388] Qwen3 Technical Report","url":"https://arxiv.org/abs/2505.09388"},{"title":"Paper page - Qwen3 Technical Report","url":"https://huggingface.co/papers/2505.09388"},{"title":"2025-05-15 Qwen3 Technical Report Qwen Team https://huggingface.co/Qwen","url":"https://arxiv.org/pdf/2505.09388"},{"title":"[2505.09388] Qwen3 Technical Report - ar5iv - arXiv","url":"https://ar5iv.labs.arxiv.org/html/2505.09388"},{"title":"Qwen3 Technical Report | Request PDF","url":"https://www.researchgate.net/publication/391741196_Qwen3_Technical_Report"},{"title":"Qwen3 Technical Report | Cool Papers - Immersive Paper Discovery","url":"https://papers.cool/arxiv/2505.09388"},{"title":"[2505.09388v1] Qwen3 Technical Report","url":"https://arxiv.org/abs/2505.09388v1"},{"title":"GitHub - bytegoose/arxiv.2505.09388: Qwen3 MoE Model Simplified Implementation following the technical report","url":"https://github.com/bytegoose/arxiv.2505.09388"},{"title":"Qwen3 Technical Report","url":"https://summarizepaper.com/en/arxiv-id/2505.09388v1/"},{"title":"Qwen3 Technical Report","url":"https://arxiv.org/html/2505.09388.pdf"}]

I found the Qwen3 Technical Report on arXiv (paper 2505.09388). Here's an overview of the paper:

## Overview

Qwen3 is the latest version of the Qwen model family, comprising a series of large language models (LLMs) designed to advance performance, efficiency, and multilingual capabilities.

## Key Features

**Model Architecture:** The Qwen3 series includes models of both dense and Mixture-of-Expert (MoE) architectures, with parameter scales ranging from 0.6 to 235 billion. The flagship model, Qwen3-235B-A22B, is an MoE model with a total of 235 billion parameters and 22 billion activated ones per token.

**Unified Thinking Framework:** A key innovation in Qwen3 is the integration of thinking mode (for complex, multi-step reasoning) and non-thinking mode (for rapid, conte
…[truncated 1091 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_bib-year-audit_20260515T174748",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 83 · 2026-05-15T17:54:07.238927+00:00_

Web search results for query: ""Diversity Boosts AI-Generated Text Detection" Basani Chen TMLR 2026"

Links: [{"title":"[2509.18880] Diversity Boosts AI-Generated Text Detection","url":"https://arxiv.org/abs/2509.18880"},{"title":"Diversity Boosts AI-Generated Text Detection","url":"https://arxiv.org/html/2509.18880v1"},{"title":"GitHub - IBM/diveye: [TMLR '26] Code for Diversity Boosts AI-generated Text Detection · GitHub","url":"https://github.com/IBM/diveye"},{"title":"[PDF] Diversity Boosts AI-Generated Text Detection | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Diversity-Boosts-AI-Generated-Text-Detection-Basani-Chen/77269d404ea3438f6d2ac327316f0b6ba116a48d"},{"title":"Diversity Boosts AI-Generated Text Detection | OpenReview","url":"https://openreview.net/forum?id=DNgsOhGZBI"},{"title":"Diversity Boosts AI-Generated Text Detection Advik Raj Basani 1 Pin-Yu Chen 2","url":"https://openreview.net/pdf?id=QuDDXJ47nq"},{"title":"ICML Diversity Boosts AI-Generated Text Detection","url":"https://icml.cc/virtual/2025/51028"},{"title":"[PDF] DivEye at PAN 2025: Diversity Boosts AI-Generated Text Detection | Semantic Scholar","url":"https://www.semanticscholar.org/paper/DivEye-at-PAN-2025:-Diversity-Boosts-AI-Generated-Basani-Chen/b18cdaf7ea2898664ed0850790059278ed50bb79"},{"title":"Under review as submission to TMLR Diversity Boosts AI-Generated Text Detection","url":"https://openreview.net/pdf?id=WscAU9It1l"},{"title":"Diversity Boosts AI-Generated Text Detection","url":"https://www.arxiv.org/pdf/2509.18880v1"}]

I found the paper "Diversity Boosts AI-Generated Text Detection" by Advik Raj Basani and Pin-Yu Chen. Here's what I found:

## Paper Overview

This paper was accepted at TMLR '26 and also appeared at ICML's Data in Generative Models (DIG-BUG) '25 workshop.

## Key Contribution

The paper proposes DivEye, a novel detection framework motivated by the observation that human-authored text exhibits richer variability in lexical and structural un
…[truncated 1019 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_bib-year-audit_20260515T174748",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 84 · 2026-05-15T17:54:07.239083+00:00_

Web search results for query: ""Markovian Generation Chains in Large Language Models" Geng arXiv 2026"

Links: [{"title":"[2603.11228] Markovian Generation Chains in Large Language Models","url":"https://arxiv.org/abs/2603.11228"},{"title":"Markovian Generation Chains in Large Language Models","url":"https://arxiv.org/html/2603.11228"},{"title":"Large Language Models as Markov Chains","url":"https://arxiv.org/html/2410.02724v1"},{"title":"[2410.02724] Large Language Models as Markov Chains","url":"https://arxiv.org/abs/2410.02724"},{"title":"1 Introduction","url":"https://arxiv.org/html/2410.02724v2"},{"title":"Large Language Models as Markov Chains Oussama Zekri * 1 Ambroise Odonnat * 2 3","url":"https://arxiv.org/pdf/2410.02724"},{"title":"Markovian Generation Chains in Large Language Models | OpenReview","url":"https://openreview.net/forum?id=nTDn4OMiym"},{"title":"[2410.02724v1] Large Language Models as Markov Chains","url":"https://arxiv.org/abs/2410.02724v1"},{"title":"Additive Multi-Step Markov Chains and the Curse of Dimensionality in Large Language Models","url":"https://arxiv.org/html/2603.04412"},{"title":"Large Language Models as Markov Chains | AI Research Paper Details","url":"https://www.aimodels.fyi/papers/arxiv/large-language-models-as-markov-chains"}]

I found the paper you were looking for! Here are the details about "Markovian Generation Chains in Large Language Models":

## Paper Overview

The paper is authored by Mingmeng Geng and 4 other authors and was submitted to arXiv on March 11, 2026.

## Main Contribution

The paper addresses the question: "How do texts evolve when they are repeatedly processed by LLMs?" The authors define this iterative inference process as Markovian generation chains, where each step takes a specific prompt template and the previous output as input, without including any prior memory.

## Key Findings

In iterative rephrasing and round-trip translation experiments, the output either converges to a small recurrent set 
…[truncated 497 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_bib-year-audit_20260515T174748",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 85 · 2026-05-15T17:54:07.239254+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"Can AI-Generated Text be Reliably Detected\" Sadasivan proceedings.iclr.cc paper_files 2024"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_bib-year-audit_20260515T174748",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"Can AI-Generated Text be Reliably Detected\" Sadasivan proceedings.iclr.cc paper_files 2024"
  }
}
```

</details>

---

### Tool call

_source line 86 · 2026-05-15T17:54:07.239373+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"Release Strategies and the Social Impacts of Language Models\" Solaiman arXiv 2019"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_bib-year-audit_20260515T174748",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"Release Strategies and the Social Impacts of Language Models\" Solaiman arXiv 2019"
  }
}
```

</details>

---

### Tool result

_source line 87 · 2026-05-15T17:54:07.239507+00:00_

Web search results for query: ""Can AI-Generated Text be Reliably Detected" Sadasivan proceedings.iclr.cc paper_files 2024"

Links: [{"title":"Can AI-Generated Text be Reliably Detected?","url":"https://arxiv.org/pdf/2303.11156"},{"title":"[2303.11156] Can AI-Generated Text be Reliably Detected?","url":"https://arxiv.org/abs/2303.11156"},{"title":"Can AI-Generated Text be Reliably Detected? | OpenReview","url":"https://openreview.net/forum?id=NvSwR4IvLO"},{"title":"[PDF] Can AI-Generated Text be Reliably Detected? | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Can-AI-Generated-Text-be-Reliably-Detected-Sadasivan-Kumar/5ee8bb4fc80a291b2e416a2a879e7153a783d7e9"},{"title":"(PDF) Can AI-Generated Text be Reliably Detected?","url":"https://www.researchgate.net/publication/369380286_Can_AI-Generated_Text_be_Reliably_Detected"},{"title":"Can AI-Generated Text be Reliably Detected? - ADS","url":"https://ui.adsabs.harvard.edu/abs/2023arXiv230311156S/abstract"},{"title":"Can AI-Generated Text be Reliably Detected?","url":"https://bibbase.org/network/publication/sadasivan-kumar-balasubramanian-wang-feizi-canaigeneratedtextbereliablydetected-2024"},{"title":"Can AI-Generated Text be Reliably Detected? Stress Testing AI Text Detectors Under Various Attacks | OpenReview","url":"https://openreview.net/forum?id=OOgsAZdFOt"},{"title":"Can AI-Generated Text be Reliably Detected?","url":"https://scispace.com/pdf/can-ai-generated-text-be-reliably-detected-1p8qe3ww.pdf"},{"title":"Can AI-Generated Text be Reliably Detected? | alphaXiv","url":"https://www.alphaxiv.org/overview/2303.11156v4"}]

I found the paper you're looking for. The paper "Can AI-Generated Text be Reliably Detected?" is authored by Vinu Sankar Sadasivan and 3 other authors.

The paper shows that AI text detectors are not reliable in practical scenarios, and develops a recursive paraphrasing attack that can break detectors including watermarking schemes, neural network-based detectors, zero-shot classi
…[truncated 612 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_bib-year-audit_20260515T174748",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 88 · 2026-05-15T17:54:07.239699+00:00_

Web search results for query: ""Release Strategies and the Social Impacts of Language Models" Solaiman arXiv 2019"

Links: [{"title":"[1908.09203] Release Strategies and the Social Impacts of Language Models","url":"https://arxiv.org/abs/1908.09203"},{"title":"[PDF] Release Strategies and the Social Impacts of Language Models | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Release-Strategies-and-the-Social-Impacts-of-Models-Solaiman-Brundage/c7462e0ee928f095a7fc40b91f1e7557d283ae8e"},{"title":"[1908.09203v2] Release Strategies and the Social Impacts of Language Models","url":"https://arxiv.org/abs/1908.09203v2"},{"title":"[1908.09203v1] Release Strategies and the Social Impacts of Language Models","url":"https://arxiv.org/abs/1908.09203v1"},{"title":"(Open Access) Release Strategies and the Social Impacts of Language Models. (2019) | Irene Solaiman | 502 Citations","url":"https://scispace.com/papers/release-strategies-and-the-social-impacts-of-language-models-1l0q23081e"},{"title":"Release Strategies and the Social Impacts of Language Models | Request PDF","url":"https://www.researchgate.net/publication/335419868_Release_Strategies_and_the_Social_Impacts_of_Language_Models"},{"title":"Google Scholar","url":"https://scholar.google.com/scholar?q=I.+Solaiman+%2C+%E2%80%98Release+Strategies+and+the+Social+Impacts+of+Language+Models%E2%80%99.+arXiv%2C+Nov.+12%2C+2019.+Accessed%3A+Feb.+21%2C+2023.+%5BOnline%5D.+Available%3A+http%3A%2F%2Farxiv.org%2Fabs%2F1908.09203"},{"title":"Paper page - Release Strategies and the Social Impacts of Language Models","url":"https://huggingface.co/papers/1908.09203"},{"title":"Release Strategies and the Social Impacts of Language Models - Paper Detail","url":"https://deeplearn.org/arxiv/90005/release-strategies-and-the-social-impacts-of-language-models"},{"title":"Human Variability vs. Machine Consistency: A Linguistic Analysis of Texts Generated by Humans and Large Language Models","url":"https://arxiv.org/html/2412.03025
…[truncated 1189 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_bib-year-audit_20260515T174748",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 89 · 2026-05-15T17:54:07.239894+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "iclr.cc virtual 2024 poster \"Can AI-Generated Text be Reliably Detected\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_bib-year-audit_20260515T174748",
  "tool": "WebSearch",
  "tool_args": {
    "query": "iclr.cc virtual 2024 poster \"Can AI-Generated Text be Reliably Detected\""
  }
}
```

</details>

---

### Tool result

_source line 90 · 2026-05-15T17:54:07.240027+00:00_

Web search results for query: "iclr.cc virtual 2024 poster "Can AI-Generated Text be Reliably Detected""

Links: [{"title":"Can AI-Generated Text be Reliably Detected? | OpenReview","url":"https://openreview.net/forum?id=NvSwR4IvLO"},{"title":"Can AI-Generated Text Be Reliably Detected? | Hacker News","url":"https://news.ycombinator.com/item?id=35253088"},{"title":"[2303.11156] Can AI-Generated Text be Reliably Detected?","url":"https://arxiv.org/abs/2303.11156"}]

I found search results for the paper "Can AI-Generated Text be Reliably Detected?" The results show that the unregulated use of Large Language Models can potentially lead to malicious consequences such as plagiarism, generating fake news, and spamming, making reliable detection of AI-generated text critical.

The paper demonstrates that existing detectors are not reliable in practical scenarios and develops a recursive paraphrasing attack that can break a range of detectors, including those using watermarking schemes, neural network-based detectors, zero-shot classifiers, and retrieval-based detectors.

The paper appears on OpenReview (a platform used for ICLR submissions) and is also available on arXiv. However, the search results don't specifically confirm whether this was presented as a virtual poster at ICLR 2024. The OpenReview submission reference indicates it was submitted for ICLR 2024.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_bib-year-audit_20260515T174748",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 91 · 2026-05-15T17:54:07.240175+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "openreview \"Can AI-Generated Text be Reliably Detected\" NvSwR4IvLO reject decision"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_bib-year-audit_20260515T174748",
  "tool": "WebSearch",
  "tool_args": {
    "query": "openreview \"Can AI-Generated Text be Reliably Detected\" NvSwR4IvLO reject decision"
  }
}
```

</details>

---

### Tool result

_source line 92 · 2026-05-15T17:54:07.240312+00:00_

Web search results for query: "openreview "Can AI-Generated Text be Reliably Detected" NvSwR4IvLO reject decision"

Links: [{"title":"Can AI-Generated Text be Reliably Detected? | OpenReview","url":"https://openreview.net/forum?id=NvSwR4IvLO"},{"title":"Can AI-Generated Text be Reliably Detected? Stress Testing AI Text Detectors Under Various Attacks | OpenReview","url":"https://openreview.net/forum?id=OOgsAZdFOt"},{"title":"Can AI-Generated Text be Reliably Detected? Stress ...","url":"https://openreview.net/pdf/a06fe5303ab3d0c635e565d4eae91e5ab7ac8175.pdf"},{"title":"CAN AI-GENERATED TEXT BE RELIABLY DETECTED?","url":"https://openreview.net/pdf/1f0e01f7e566b02cf3078fd6e307d6b9421d47fc.pdf"},{"title":"[2303.11156] Can AI-Generated Text be Reliably Detected?","url":"https://arxiv.org/abs/2303.11156"},{"title":"Can AI-Generated Text be Reliably Detected? | alphaXiv","url":"https://www.alphaxiv.org/overview/2303.11156v4"},{"title":"Can AI-Generated Text be Reliably Detected? - ADS","url":"https://ui.adsabs.harvard.edu/abs/2023arXiv230311156S/abstract"},{"title":"Can AI-Generated Text be Reliably Detected?","url":"https://arxiv.org/pdf/2303.11156"},{"title":"[PDF] Can AI-Generated Text be Reliably Detected? | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Can-AI-Generated-Text-be-Reliably-Detected-Sadasivan-Kumar/5ee8bb4fc80a291b2e416a2a879e7153a783d7e9"},{"title":"The Problems with AI Detectors: False Positives and False Negatives - Generative AI Detection Tools - Guides at University of San Diego Legal Research Center","url":"https://lawlibguides.sandiego.edu/c.php?g=1443311&p=10721367"}]

Based on the search results, I found information about the paper "Can AI-Generated Text be Reliably Detected?" with the ID NvSwR4IvLO on OpenReview.

The paper shows that AI text detectors are not reliable in practical scenarios, developing a recursive paraphrasing attack that can break a wide range of detectors, including those using watermarking schemes as well as
…[truncated 1056 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_bib-year-audit_20260515T174748",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 93 · 2026-05-15T17:54:07.240493+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/references.bib",
  "old_string": "@article{self_consuming_mad,\n  title = {{Self-Consuming Generative Models Go MAD}},\n  author = {Alemohammad, Sina and Casco-Rodriguez, Josue and Luzi, Lorenzo and Humayun, Ahmed Imtiaz and Babaei, Hossein and LeJeune, Daniel and Siahkoohi, Ali and Baraniuk, Richard G.},\n  journal = {arXiv preprint arXiv:2307.01850},\n  year = {2023},\n}",
  "new_string": "@inproceedings{self_consuming_mad,\n  title = {{Self-Consuming Generative Models Go MAD}},\n  author = {Alemohammad, Sina and Casco-Rodriguez, Josue and Luzi, Lorenzo and Humayun, Ahmed Imtiaz and Babaei, Hossein and LeJeune, Daniel and Siahkoohi, Ali and Baraniuk, Richard G.},\n  booktitle = {Proceedings of the International Conference on Learning Representations},\n  year = {2024},\n}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_bib-year-audit_20260515T174748",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/references.bib",
    "old_string": "@article{self_consuming_mad,\n  title = {{Self-Consuming Generative Models Go MAD}},\n  author = {Alemohammad, Sina and Casco-Rodriguez, Josue and Luzi, Lorenzo and Humayun, Ahmed Imtiaz and Babaei, Hossein and LeJeune, Daniel and Siahkoohi, Ali and Baraniuk, Richard G.},\n  journal = {arXiv preprint arXiv:2307.01850},\n  year = {2023},\n}",
    "new_string": "@inproceedings{self_consuming_mad,\n  title = {{Self-Consuming Generative Models Go MAD}},\n  author = {Alemohammad, Sina and Casco-Rodriguez, Josue and Luzi, Lorenzo and Humayun, Ahmed Imtiaz and Babaei, Hossein and LeJeune, Daniel and Siahkoohi, Ali and Baraniuk, Richard G.},\n  booktitle = {Proceedings of the International Conference on Learning Representations},\n  year = {2024},\n}"
  }
}
```

</details>

---

### Tool result

_source line 94 · 2026-05-15T17:54:07.240681+00:00_

The file /home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/references.bib has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_bib-year-audit_20260515T174748",
  "tool": "Edit",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 95 · 2026-05-15T17:54:07.240824+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/references.bib",
  "limit": "10",
  "offset": "122"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_bib-year-audit_20260515T174748",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/references.bib",
    "limit": "10",
    "offset": "122"
  }
}
```

</details>

---

### Tool result

_source line 96 · 2026-05-15T17:54:07.240947+00:00_

122	% ===== Model Collapse =====
123	
124	@article{self_consuming_mad,
125	  title = {{Self-Consuming Generative Models Go MAD}},
126	  author = {Alemohammad, Sina and Casco-Rodriguez, Josue and Luzi, Lorenzo and Humayun, Ahmed Imtiaz and Babaei, Hossein and LeJeune, Daniel and Siahkoohi, Ali and Baraniuk, Richard G.},
127	  journal = {arXiv preprint arXiv:2307.01850},
128	  year = {2023},
129	}
130	
131	@article{curse_of_recursion,

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_bib-year-audit_20260515T174748",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 97 · 2026-05-15T17:54:07.241066+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/references.bib",
  "old_string": "@article{self_consuming_mad,\n  title = {{Self-Consuming Generative Models Go MAD}},\n  author = {Alemohammad, Sina and Casco-Rodriguez, Josue and Luzi, Lorenzo and Humayun, Ahmed Imtiaz and Babaei, Hossein and LeJeune, Daniel and Siahkoohi, Ali and Baraniuk, Richard G.},\n  journal = {arXiv preprint arXiv:2307.01850},\n  year = {2023},\n}",
  "new_string": "@inproceedings{self_consuming_mad,\n  title = {{Self-Consuming Generative Models Go MAD}},\n  author = {Alemohammad, Sina and Casco-Rodriguez, Josue and Luzi, Lorenzo and Humayun, Ahmed Imtiaz and Babaei, Hossein and LeJeune, Daniel and Siahkoohi, Ali and Baraniuk, Richard G.},\n  booktitle = {Proceedings of the International Conference on Learning Representations},\n  year = {2024},\n}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_bib-year-audit_20260515T174748",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/references.bib",
    "old_string": "@article{self_consuming_mad,\n  title = {{Self-Consuming Generative Models Go MAD}},\n  author = {Alemohammad, Sina and Casco-Rodriguez, Josue and Luzi, Lorenzo and Humayun, Ahmed Imtiaz and Babaei, Hossein and LeJeune, Daniel and Siahkoohi, Ali and Baraniuk, Richard G.},\n  journal = {arXiv preprint arXiv:2307.01850},\n  year = {2023},\n}",
    "new_string": "@inproceedings{self_consuming_mad,\n  title = {{Self-Consuming Generative Models Go MAD}},\n  author = {Alemohammad, Sina and Casco-Rodriguez, Josue and Luzi, Lorenzo and Humayun, Ahmed Imtiaz and Babaei, Hossein and LeJeune, Daniel and Siahkoohi, Ali and Baraniuk, Richard G.},\n  booktitle = {Proceedings of the International Conference on Learning Representations},\n  year = {2024},\n}"
  }
}
```

</details>

---

### Tool result

_source line 98 · 2026-05-15T17:54:07.241225+00:00_

The file /home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/references.bib has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_bib-year-audit_20260515T174748",
  "tool": "Edit",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 99 · 2026-05-15T17:54:07.241371+00:00_

已修复并同步。

**修复：**
- `self_consuming_mad`: 2023 → 2024，`@article` → `@inproceedings`，venue 改为 ICLR（两个 bib 文件均已更新）

**可疑：**
- `reliable_detection`: bib 标为 ICLR 2024，但无法在 ICLR 2024 proceedings 中确认收录。扩展版 "Stress Testing" 发表于 TMLR 2025。原文可能仅为 arXiv preprint（首发 2023）。建议手动确认后决定是否改为 arXiv preprint 2023 或 TMLR 2025。

**其他非年份问题（供参考）：**
- `munir_looking_glass`: 作者名与 EACL 2021 论文实际作者不匹配
- `wu_survey_2025`: 除第一作者外，后续作者列表与 CL 2025 实际作者不匹配
- `mapping_llm_science`: 已正式发表于 COLM 2024，可考虑更新 venue

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_paper_bib-year-audit_20260515T174748"
}
```

</details>

---
