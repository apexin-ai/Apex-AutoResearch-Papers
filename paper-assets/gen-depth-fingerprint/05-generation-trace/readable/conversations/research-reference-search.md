# research reference search

**Depth Profiling: Classifying Recursive Generation Depth in Base-Model LLM Text** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 19
- **Recorded user turns:** 0
- **Tool calls:** 9
- **Original source:** `logs/chats/worker_research_reference-search_20260517T170729.jsonl`
- **Structured JSON:** [`3af329c69391657f6a22.json`](../../sessions/3a/3af329c69391657f6a22.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

19 recorded events

### Tool call

_source line 1 · 2026-05-17T17:08:46.284466+00:00_

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
  "session": "worker_research_reference-search_20260517T170729",
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

_source line 2 · 2026-05-17T17:08:46.284771+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_reference-search_20260517T170729",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-17T17:08:46.284944+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Hammoudeh Lowd 2024 \"training data attribution\" machine learning survey"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_reference-search_20260517T170729",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Hammoudeh Lowd 2024 \"training data attribution\" machine learning survey"
  }
}
```

</details>

---

### Tool call

_source line 4 · 2026-05-17T17:08:46.285073+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Kumarage et al 2023 \"LLM-generated text detection\" stylometric"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_reference-search_20260517T170729",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Kumarage et al 2023 \"LLM-generated text detection\" stylometric"
  }
}
```

</details>

---

### Tool result

_source line 5 · 2026-05-17T17:08:46.285241+00:00_

Web search results for query: "Hammoudeh Lowd 2024 "training data attribution" machine learning survey"

Links: [{"title":"Training Data Influence Analysis & Estimation Resources","url":"https://github.com/ZaydH/influence_analysis_papers"},{"title":"[2212.04612] Training Data Influence Analysis and Estimation: A Survey","url":"https://arxiv.org/abs/2212.04612"},{"title":"Training Data Influence Analysis and Estimation: A Survey Zayd Hammoudeh∗1,2","url":"https://arxiv.org/pdf/2212.04612"},{"title":"[PDF] Training Data Influence Analysis and Estimation: A Survey | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Training-Data-Influence-Analysis-and-Estimation:-A-Hammoudeh-Lowd/c164ec3b73eb108f861fcd60df73b62d2482c3a6"},{"title":"(PDF) Training data influence analysis and estimation: a survey","url":"https://www.researchgate.net/publication/379410061_Training_data_influence_analysis_and_estimation_a_survey"},{"title":"Efficient Ensembles Improve Training Data Attribution","url":"https://arxiv.org/html/2405.17293v1"},{"title":"Training data influence analysis and estimation: a survey | Machine Language","url":"https://dl.acm.org/doi/abs/10.1007/s10994-023-06495-7"},{"title":"Stage 2026 - Data Science et Machine Learning/AI practitionner - Sujet : Data attribution (H/F/N) – Ekimetrics – Internship in Paris","url":"https://www.welcometothejungle.com/en/companies/ekimetrics/jobs/stage-2026-data-science-et-machine-learning-ai-practitionner-sujet-data-attribution-h-f-n_paris"},{"title":"How Data-Related AI Research can Support Technical ...","url":"https://openreview.net/pdf?id=MuFBL4Kogc"},{"title":"Zayd Hammoudeh's research works | University of Oregon and other places","url":"https://www.researchgate.net/scientific-contributions/Zayd-Hammoudeh-2171065948"}]

Based on the search results, I found the paper you're looking for:

Zayd Hammoudeh and Daniel Lowd published "Training Data Influence Analysis and Estimation: A Survey" in Machine Learning in 2024 (Volu
…[truncated 846 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_reference-search_20260517T170729",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-17T17:08:46.285430+00:00_

Web search results for query: "Kumarage et al 2023 "LLM-generated text detection" stylometric"

Links: [{"title":"Text Authorship Attribution: Stylometric Insights into Human and LLM-Generated Text | Proceedings of the 8th International Conference on Data Science and Management of Data (12th ACM IKDD CODS and 30th COMAD)","url":"https://dl.acm.org/doi/10.1145/3703323.3703712"},{"title":"On the Detectability of LLM-Generated Text: What Exactly Is LLM-Generated Text?","url":"https://arxiv.org/html/2510.20810v1"},{"title":"Stylometry recognizes human and LLM-generated texts in short samples - ScienceDirect","url":"https://www.sciencedirect.com/science/article/abs/pii/S0957417425026181"},{"title":"Stylometry recognizes human and LLM-generated texts in short samples","url":"https://arxiv.org/html/2507.00838v2"},{"title":"Stylometric Detection of AI-Generated Text in Twitter Timelines","url":"https://arxiv.org/pdf/2303.03697"},{"title":"Stylometry Recognizes Human and LLM-generated Texts in Short Samples | PDF | Artificial Intelligence | Intelligence (AI) & Semantics","url":"https://www.scribd.com/document/997061452/2507-00838v2"},{"title":"Benchmark of stylistic variation in LLM-generated texts","url":"https://arxiv.org/html/2509.10179v2"},{"title":"(PDF) Stylometry Recognizes Human and Llm-Generated Texts in Short Samples","url":"https://www.researchgate.net/publication/383897763_Stylometry_Recognizes_Human_and_Llm-Generated_Texts_in_Short_Samples"},{"title":"A Survey of AI-generated Text Forensic Systems: Detection, Attribution, and Characterization","url":"https://arxiv.org/html/2403.01152v1"},{"title":"Stylometry recognizes human and LLM-generated texts in short samples | Request PDF","url":"https://www.researchgate.net/publication/393713840_Stylometry_recognizes_human_and_LLM-generated_texts_in_short_samples"}]

I found relevant information about the Kumarage et al. 2023 work on LLM-generated text detection using stylometric analysis. Here's what I found:

## Key Fi
…[truncated 1203 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_reference-search_20260517T170729",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-17T17:08:46.285635+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Hammoudeh Lowd \"Training Data Influence Analysis and Estimation: A Survey\" Machine Learning journal 2024 DOI"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_reference-search_20260517T170729",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Hammoudeh Lowd \"Training Data Influence Analysis and Estimation: A Survey\" Machine Learning journal 2024 DOI"
  }
}
```

</details>

---

### Tool call

_source line 8 · 2026-05-17T17:08:46.285780+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Kumarage \"Stylometric Detection of AI-Generated Text in Twitter Timelines\" 2023 arXiv authors"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_reference-search_20260517T170729",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Kumarage \"Stylometric Detection of AI-Generated Text in Twitter Timelines\" 2023 arXiv authors"
  }
}
```

</details>

---

### Tool result

_source line 9 · 2026-05-17T17:08:46.285933+00:00_

Web search results for query: "Hammoudeh Lowd "Training Data Influence Analysis and Estimation: A Survey" Machine Learning journal 2024 DOI"

Links: [{"title":"[2212.04612] Training Data Influence Analysis and Estimation: A Survey","url":"https://arxiv.org/abs/2212.04612"},{"title":"[PDF] Training Data Influence Analysis and Estimation: A Survey | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Training-Data-Influence-Analysis-and-Estimation:-A-Hammoudeh-Lowd/c164ec3b73eb108f861fcd60df73b62d2482c3a6"},{"title":"Training Data Influence Analysis and Estimation: A Survey Zayd Hammoudeh∗1,2","url":"https://arxiv.org/pdf/2212.04612"},{"title":"Training Data Influence Analysis and Estimation: A Survey","url":"https://www.researchgate.net/publication/366190340_Training_Data_Influence_Analysis_and_Estimation_A_Survey/fulltext/63969d6d095a6a7774229577/Training-Data-Influence-Analysis-and-Estimation-A-Survey.pdf"},{"title":"Training data influence analysis and estimation: a survey | Machine Learning | Springer Nature Link","url":"https://link.springer.com/article/10.1007/s10994-023-06495-7"},{"title":"Training Data Influence Analysis & Estimation Resources","url":"https://github.com/ZaydH/influence_analysis_papers"},{"title":"(PDF) Training data influence analysis and estimation: a survey","url":"https://www.researchgate.net/publication/379410061_Training_data_influence_analysis_and_estimation_a_survey"},{"title":"Training data influence analysis and estimation: a survey | Machine Language","url":"https://dl.acm.org/doi/abs/10.1007/s10994-023-06495-7"},{"title":"Zayd Hammoudeh's research works | University of Oregon and other places","url":"https://www.researchgate.net/scientific-contributions/Zayd-Hammoudeh-2171065948"},{"title":"Journal of Machine Learning Research 24 (2023) 1-48","url":"https://arxiv.org/pdf/2205.00359"}]

Based on the search results, I found the paper you're looking for:

The paper "Training Data Influence Analysis and Estimation: A Survey"
…[truncated 1033 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_reference-search_20260517T170729",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-17T17:08:46.286107+00:00_

Web search results for query: "Kumarage "Stylometric Detection of AI-Generated Text in Twitter Timelines" 2023 arXiv authors"

Links: [{"title":"[2303.03697] Stylometric Detection of AI-Generated Text in Twitter Timelines","url":"https://arxiv.org/abs/2303.03697"},{"title":"Stylometric Detection of AI-Generated Text in Twitter Timelines","url":"https://arxiv.org/pdf/2303.03697"},{"title":"[PDF] Stylometric Detection of AI-Generated Text in Twitter Timelines | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Stylometric-Detection-of-AI-Generated-Text-in-Kumarage-Garland/18e0b11dd5b1b413d33308da0379836752aaaec1"},{"title":"Stylometric Detection of AI-Generated Text in Twitter Timelines - ADS","url":"https://ui.adsabs.harvard.edu/abs/2023arXiv230303697K/abstract"},{"title":"(PDF) Stylometric Detection of AI-Generated Text in Twitter Timelines","url":"https://www.researchgate.net/publication/373898266_Stylometric_Detection_of_AI-Generated_Text_in_Twitter_Timelines"},{"title":"Paper page - Stylometric Detection of AI-Generated Text in Twitter Timelines","url":"https://huggingface.co/papers/2303.03697"},{"title":"A Survey of AI-generated Text Forensic Systems: Detection, Attribution, and Characterization","url":"https://arxiv.org/html/2403.01152v1"},{"title":"Beyond Perplexity: Character Distribution Signatures and the MDTA Benchmark for AI Text Detection","url":"https://arxiv.org/html/2605.01647v1"},{"title":"AI-Writing Detection Using an Ensemble of Transformers and Stylometric Features","url":"https://ceur-ws.org/Vol-3496/autextification-paper9.pdf"},{"title":"Machine-Generated Text Detection using Deep Learning","url":"https://arxiv.org/html/2311.15425"}]

Based on the search results, I found the paper you're looking for. Here are the details:

**Paper Title:** Stylometric Detection of AI-Generated Text in Twitter Timelines

**Authors:** Tharindu Kumarage, Joshua Garland, Amrita Bhattacharjee, Kirill Trapeznikov, Scott Ruston, and Huan Liu

**Publication
…[truncated 491 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_reference-search_20260517T170729",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-17T17:08:46.286279+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "Hammoudeh|Kumarage",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper",
  "output_mode": "content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_reference-search_20260517T170729",
  "tool": "Grep",
  "tool_args": {
    "pattern": "Hammoudeh|Kumarage",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper",
    "output_mode": "content"
  }
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-17T17:08:46.286399+00:00_

No matches found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_reference-search_20260517T170729",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-17T17:08:46.286512+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls -la /home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/results/ 2>/dev/null || echo \"Directory does not exist\"",
  "description": "Check results directory existence"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_reference-search_20260517T170729",
  "tool": "Bash",
  "tool_args": {
    "command": "ls -la /home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/results/ 2>/dev/null || echo \"Directory does not exist\"",
    "description": "Check results directory existence"
  }
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-17T17:08:46.286646+00:00_

total 24
drwxr-xr-x 2 ubuntu ubuntu 4096 May 17 15:29 .
drwxr-xr-x 9 ubuntu ubuntu 4096 May 17 15:28 ..
-rw-r--r-- 1 ubuntu ubuntu 2042 May 17 15:29 cross_model_chains_per_class.json
-rw-r--r-- 1 ubuntu ubuntu 4701 May 17 15:29 distributional_tests.json
-rw-r--r-- 1 ubuntu ubuntu 1745 May 17 15:28 tost_multi_margin.json

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_reference-search_20260517T170729",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-17T17:08:46.286761+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "Hammoudeh|Kumarage",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper",
  "glob": "*.bib",
  "output_mode": "content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_reference-search_20260517T170729",
  "tool": "Grep",
  "tool_args": {
    "pattern": "Hammoudeh|Kumarage",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper",
    "glob": "*.bib",
    "output_mode": "content"
  }
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-17T17:08:46.286877+00:00_

No matches found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_reference-search_20260517T170729",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-17T17:08:46.287007+00:00_

called Write

<details open><summary>🔧 Tool call — Write</summary>

````json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/results/reference_verification.md",
  "content": "# Reference Verification Report\n\nDate: 2025-05-17\n\n## 1. Hammoudeh & Lowd 2024\n\n- **Status**: VERIFIED (real paper)\n- **Title**: Training Data Influence Analysis and Estimation: A Survey\n- **Authors**: Zayd Hammoudeh, Daniel Lowd\n- **Year**: 2024\n- **Venue**: Machine Learning (Springer), Volume 113, pp. 2351--2403\n- **arXiv**: 2212.04612\n- **DOI**: 10.1007/s10994-023-06495-7\n\n**Summary**: First comprehensive survey of training data influence analysis and estimation. Formalizes definitions of training data influence, organizes methods into a taxonomy (retraining-based vs. gradient-based), and compares assumptions, complexities, and trade-offs.\n\n**Relevance to depth fingerprinting**: Moderate. Training data attribution quantifies how individual training instances affect model behavior, which is conceptually related to identifying generative model fingerprints. However, this is a survey of influence estimation methods (influence functions, data Shapley, etc.), not directly about text generation detection. Appropriate as background reference if the paper discusses how training data shapes generator-specific artifacts, but not a core related work for stylometric detection.\n\n**Current citation status**: Not yet cited in the paper bib files.\n\n---\n\n## 2. Kumarage et al. 2023\n\n- **Status**: VERIFIED (real paper)\n- **Title**: Stylometric Detection of AI-Generated Text in Twitter Timelines\n- **Authors**: Tharindu Kumarage, Joshua Garland, Amrita Bhattacharjee, Kirill Trapeznikov, Scott Ruston, Huan Liu\n- **Year**: 2023\n- **arXiv**: 2303.03697\n- **Venue**: arXiv preprint (cited in multiple survey papers; no formal journal/conference publication identified)\n\n**Summary**: Proposes a stylometric approach to detect AI-generated tweets, using a fusion of fine-tuned RoBERTa with lexical, syntactic, and structural stylometric features (lexical richness, readability, punctuation counts). Addresses two tasks: discriminating human vs. AI tweets, and detecting the point in a timeline when AI generation begins.\n\n**Relevance to depth fingerprinting**: High. Directly relevant as related work on LLM-generated text detection using stylometric signals. The use of linguistic features to distinguish human from AI text is closely aligned with depth fingerprinting's goal of identifying generator-specific stylistic patterns. Good candidate for the Related Work section under \"detection methods\" or \"stylometric approaches.\"\n\n**Current citation status**: Not yet cited in the paper bib files.\n\n---\n\n## Suggested BibTeX Entries\n\n```bibtex\n@article{hammoudeh2024training,\n  title={Training Data Influence Analysis and Estimation: A Survey},\n  author={Hammoudeh, Zayd and Lowd, Daniel},\n  journal={Machine Learning},\n  volume={113},\n  pages={2351--2403},\n  year={2024},\n  publisher={Springer},\n  doi={10.1007/s10994-023-06495-7}\n}\n\n@article{kumarage2023stylometric,\n  title={Stylometric Detection of {AI}-Generated Text in Twitter Timelines},\n  author={Kumarage, Tharindu and Garland, Joshua and Bhattacharjee, Amrita and Trapeznikov, Kirill and Ruston, Scott and Liu, Huan},\n  journal={arXiv preprint arXiv:2303.03697},\n  year={2023}\n}\n```\n"
}
````

</details>

<details><summary>Recorded metadata</summary>

````json
{
  "recorded_role": "tool",
  "session": "worker_research_reference-search_20260517T170729",
  "tool": "Write",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/results/reference_verification.md",
    "content": "# Reference Verification Report\n\nDate: 2025-05-17\n\n## 1. Hammoudeh & Lowd 2024\n\n- **Status**: VERIFIED (real paper)\n- **Title**: Training Data Influence Analysis and Estimation: A Survey\n- **Authors**: Zayd Hammoudeh, Daniel Lowd\n- **Year**: 2024\n- **Venue**: Machine Learning (Springer), Volume 113, pp. 2351--2403\n- **arXiv**: 2212.04612\n- **DOI**: 10.1007/s10994-023-06495-7\n\n**Summary**: First comprehensive survey of training data influence analysis and estimation. Formalizes definitions of training data influence, organizes methods into a taxonomy (retraining-based vs. gradient-based), and compares assumptions, complexities, and trade-offs.\n\n**Relevance to depth fingerprinting**: Moderate. Training data attribution quantifies how individual training instances affect model behavior, which is conceptually related to identifying generative model fingerprints. However, this is a survey of influence estimation methods (influence functions, data Shapley, etc.), not directly about text generation detection. Appropriate as background reference if the paper discusses how training data shapes generator-specific artifacts, but not a core related work for stylometric detection.\n\n**Current citation status**: Not yet cited in the paper bib files.\n\n---\n\n## 2. Kumarage et al. 2023\n\n- **Status**: VERIFIED (real paper)\n- **Title**: Stylometric Detection of AI-Generated Text in Twitter Timelines\n- **Authors**: Tharindu Kumarage, Joshua Garland, Amrita Bhattacharjee, Kirill Trapeznikov, Scott Ruston, Huan Liu\n- **Year**: 2023\n- **arXiv**: 2303.03697\n- **Venue**: arXiv preprint (cited in multiple survey papers; no formal journal/conference publication identified)\n\n**Summary**: Proposes a stylometric approach to detect AI-generated tweets, using a fusion of fine-tuned RoBERTa with lexical, syntactic, and structural stylometric features (lexical richness, readability, punctuation counts). Addresses two tasks: discriminating human vs. AI tweets, and detecting the point in a timeline when AI generation begins.\n\n**Relevance to depth fingerprinting**: High. Directly relevant as related work on LLM-generated text detection using stylometric signals. The use of linguistic features to distinguish human from AI text is closely aligned with depth fingerprinting's goal of identifying generator-specific stylistic patterns. Good candidate for the Related Work section under \"detection methods\" or \"stylometric approaches.\"\n\n**Current citation status**: Not yet cited in the paper bib files.\n\n---\n\n## Suggested BibTeX Entries\n\n```bibtex\n@article{hammoudeh2024training,\n  title={Training Data Influence Analysis and Estimation: A Survey},\n  author={Hammoudeh, Zayd and Lowd, Daniel},\n  journal={Machine Learning},\n  volume={113},\n  pages={2351--2403},\n  year={2024},\n  publisher={Springer},\n  doi={10.1007/s10994-023-06495-7}\n}\n\n@article{kumarage2023stylometric,\n  title={Stylometric Detection of {AI}-Generated Text in Twitter Timelines},\n  author={Kumarage, Tharindu and Garland, Joshua and Bhattacharjee, Amrita and Trapeznikov, Kirill and Ruston, Scott and Liu, Huan},\n  journal={arXiv preprint arXiv:2303.03697},\n  year={2023}\n}\n```\n"
  }
}
````

</details>

---

### Tool result

_source line 18 · 2026-05-17T17:08:46.287149+00:00_

File created successfully at: /home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/results/reference_verification.md

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_reference-search_20260517T170729",
  "tool": "Write",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 19 · 2026-05-17T17:08:46.287320+00:00_

两篇论文均已验证为真实存在：

1. **Hammoudeh & Lowd 2024** — "Training Data Influence Analysis and Estimation: A Survey"，发表于 Machine Learning (Springer), Vol. 113, pp. 2351-2403, DOI: 10.1007/s10994-023-06495-7。与 depth fingerprinting 相关性中等（训练数据影响分析的综述，概念相关但非直接相关工作）。

2. **Kumarage et al. 2023** — "Stylometric Detection of AI-Generated Text in Twitter Timelines"，arXiv:2303.03697，作者6人（Kumarage, Garland, Bhattacharjee, Trapeznikov, Ruston, Liu）。与 depth fingerprinting 相关性高（直接使用 stylometric 特征检测 AI 生成文本）。

两篇论文目前均未在我们的 bib 文件中引用。验证报告和建议的 BibTeX 条目已写入 `artifacts/_project/results/reference_verification.md`。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_research_reference-search_20260517T170729"
}
```

</details>

---
