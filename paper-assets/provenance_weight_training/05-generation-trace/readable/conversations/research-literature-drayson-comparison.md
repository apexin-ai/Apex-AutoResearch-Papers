# research literature drayson comparison

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 37
- **Recorded user turns:** 0
- **Tool calls:** 18
- **Original source:** `logs/chats/worker_research_literature-drayson-comparison_20260514T233124.jsonl`
- **Structured JSON:** [`36bd7cc232cc4fbc4661.json`](../../sessions/36/36bd7cc232cc4fbc4661.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

37 recorded events

### Tool call

_source line 1 · 2026-05-14T23:34:16.213629+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:WebSearch,WebFetch",
  "max_results": "2"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_literature-drayson-comparison_20260514T233124",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:WebSearch,WebFetch",
    "max_results": "2"
  }
}
```

</details>

---

### Tool result

_source line 2 · 2026-05-14T23:34:16.214051+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_literature-drayson-comparison_20260514T233124",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-14T23:34:16.214269+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Drayson detect reweight synthetic data EMNLP 2025 model collapse"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_literature-drayson-comparison_20260514T233124",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Drayson detect reweight synthetic data EMNLP 2025 model collapse"
  }
}
```

</details>

---

### Tool call

_source line 4 · 2026-05-14T23:34:16.214404+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Golden Ratio Weighting arXiv 2502.18049 synthetic data 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_literature-drayson-comparison_20260514T233124",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Golden Ratio Weighting arXiv 2502.18049 synthetic data 2025"
  }
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-14T23:34:16.214527+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"Strong Model Collapse\" ICLR 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_literature-drayson-comparison_20260514T233124",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"Strong Model Collapse\" ICLR 2025"
  }
}
```

</details>

---

### Tool call

_source line 6 · 2026-05-14T23:34:16.214647+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"Dynamic Loss-Based Sample Reweighting\" ICLR 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_literature-drayson-comparison_20260514T233124",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"Dynamic Loss-Based Sample Reweighting\" ICLR 2025"
  }
}
```

</details>

---

### Tool result

_source line 7 · 2026-05-14T23:34:16.214815+00:00_

Web search results for query: "Drayson detect reweight synthetic data EMNLP 2025 model collapse"

Links: [{"title":"Machine-generated text detection prevents language ...","url":"https://omega.cs.ucl.ac.uk/assets/pdf/papers/drayson2025-model-collapse.pdf"},{"title":"GitHub - pengr/LLM-Synthetic-Data: A live reading list for LLM data synthesis (Updated to July, 2025). · GitHub","url":"https://github.com/pengr/LLM-Synthetic-Data"},{"title":"Demystifying Synthetic Data in LLM Pre-training","url":"https://aclanthology.org/2025.emnlp-main.544.pdf"},{"title":"Demystifying Synthetic Data in LLM Pre-training: A Systematic Study of Scaling Laws, Benefits, and Pitfalls - ACL Anthology","url":"https://aclanthology.org/2025.emnlp-main.544/"},{"title":"AI model collapse: The synthetic data trap and how to avoid it","url":"https://insights.manageengine.com/artificial-intelligence/ai-model-collapse-synthetic-data-trap/"},{"title":"Strong Model Collapse | OpenReview","url":"https://openreview.net/forum?id=et5l9qPUhm"},{"title":"Escaping Model Collapse via Synthetic Data Verification: Near-term Improvements and Long-term ConvergenceThis project is supported by the AI2050 program at Schmidt Sciences (Grant G-24-66104) and Army Research Office Award W911NF-23-1-0030. We also thank Cong Ma from UChicago, Hongning Wang and Bo Li from Tsinghua, Pinyan Lu and Gavin Tang from Shanghai University of Finance and Economics for helpful discussions and suggestions.","url":"https://arxiv.org/html/2510.16657v1"},{"title":"NeurIPS Poster A Closer Look at Model Collapse: From a Generalization-to-Memorization Perspective","url":"https://neurips.cc/virtual/2025/poster/119754"},{"title":"Published as a conference paper at ICLR 2025 STRONG MODEL COLLAPSE","url":"https://proceedings.iclr.cc/paper_files/paper/2025/file/284afdc2309f9667d2d4fb9290235b0c-Paper-Conference.pdf"},{"title":"Curated Synthetic Data Doesn’t Have to Collapse: A Theoretical Study of Generative Retraining with Pluralistic Preferences
…[truncated 1272 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_literature-drayson-comparison_20260514T233124",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-14T23:34:16.215034+00:00_

Web search results for query: "Golden Ratio Weighting arXiv 2502.18049 synthetic data 2025"

Links: [{"title":"[2502.18049] Golden Ratio Weighting Prevents Model Collapse","url":"https://arxiv.org/abs/2502.18049"},{"title":"Golden Ratio Weighting Prevents Model Collapse Hengzhi He† Shirong Xu†∗","url":"https://arxiv.org/pdf/2502.18049"},{"title":"Golden Ratio Weighting Prevents Model Collapse","url":"https://arxiv.org/html/2502.18049"},{"title":"Escaping Model Collapse via Synthetic Data Verification: Near-term Improvements and Long-term ConvergenceThis project is supported by the AI2050 program at Schmidt Sciences (Grant G-24-66104) and Army Research Office Award W911NF-23-1-0030. We also thank Cong Ma from UChicago, Hongning Wang and Bo Li from Tsinghua, Pinyan Lu and Gavin Tang from Shanghai University of Finance and Economics for helpful discussions and suggestions.","url":"https://arxiv.org/html/2510.16657v1"},{"title":"LLM Web Dynamics: Tracing Model Collapse in a Network of LLMs Tianyu Wang†","url":"https://arxiv.org/pdf/2506.15690"},{"title":"LLM Web Dynamics: Tracing Model Collapse in a Network of LLMs","url":"https://arxiv.org/html/2506.15690v2"},{"title":"Preventing Model Collapse Under Overparametrization: Optimal Mixing Ratios for Interpolation Learning and Ridge Regression","url":"https://arxiv.org/html/2509.22341v1"},{"title":"Machine Learning Feb 2025","url":"https://arxiv.org/list/stat.ML/2025-02?skip=25&show=250"},{"title":"Statistics Feb 2025","url":"https://www.arxiv.org/list/stat/2025-02?skip=525&show=250"},{"title":"Machine Learning Feb 2025 - stat.ML","url":"https://arxiv.org/list/stat.ML/2025-02?skip=200&show=1000"}]

Based on the search results, here's what I found about the paper "Golden Ratio Weighting Prevents Model Collapse" (arXiv 2502.18049):

## Overview

The paper investigates model collapse—a phenomenon where models trained on data generated by previous models exhibit severe performance degradation—by studying how generative models 
…[truncated 1259 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_literature-drayson-comparison_20260514T233124",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 9 · 2026-05-14T23:34:16.215234+00:00_

Web search results for query: ""Strong Model Collapse" ICLR 2025"

Links: [{"title":"Strong Model Collapse | OpenReview","url":"https://openreview.net/forum?id=et5l9qPUhm"},{"title":"Published as a conference paper at ICLR 2025 STRONG MODEL COLLAPSE","url":"https://proceedings.iclr.cc/paper_files/paper/2025/file/284afdc2309f9667d2d4fb9290235b0c-Paper-Conference.pdf"},{"title":"ICLR Poster Strong Model Collapse","url":"https://iclr.cc/virtual/2025/poster/32070"},{"title":"[2410.04840] Strong Model Collapse","url":"https://arxiv.org/abs/2410.04840"},{"title":"[Quick Review] Strong Model Collapse","url":"https://liner.com/review/strong-model-collapse"},{"title":"GitHub - pengr/LLM-Synthetic-Data: A live reading list for LLM data synthesis (Updated to July, 2025). · GitHub","url":"https://github.com/pengr/LLM-Synthetic-Data"},{"title":"A Closer Look at Model Collapse: From a Generalization-to-Memorization Perspective | Request PDF","url":"https://www.researchgate.net/publication/395724450_A_Closer_Look_at_Model_Collapse_From_a_Generalization-to-Memorization_Perspective"},{"title":"NeurIPS Poster A Closer Look at Model Collapse: From a Generalization-to-Memorization Perspective","url":"https://neurips.cc/virtual/2025/poster/119754"},{"title":"Elvis DOHMATOB's Post","url":"https://www.linkedin.com/posts/elvis-dohmatob-53bba979_papers-accepted-at-iclr-2025-an-effective-activity-7307242348252442624-vT2L"},{"title":"Collapse or Thrive? Perils and Promises of Synthetic Data in a Self-Generating World | OpenReview","url":"https://openreview.net/forum?id=Xr5iINA3zU"}]

## Search Results for "Strong Model Collapse" ICLR 2025

I found detailed information about the paper "Strong Model Collapse" presented at ICLR 2025. Here's what the research reveals:

### Overview

"Strong Model Collapse" examines model collapse within the scaling laws paradigm, establishing a strong form of the model collapse phenomenon—a critical performance degradation due to synthetic data in the training co
…[truncated 1161 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_literature-drayson-comparison_20260514T233124",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-14T23:34:16.215424+00:00_

Web search results for query: ""Dynamic Loss-Based Sample Reweighting" ICLR 2025"

Links: [{"title":"Dynamic Loss-Based Sample Reweighting for Improved Large Language Model Pretraining | OpenReview","url":"https://openreview.net/forum?id=gU4ZgQNsOC"},{"title":"GitHub - sowmaster/Sample-Level-Loss-Reweighting-ICLR-2025","url":"https://github.com/sowmaster/Sample-Level-Loss-Reweighting-ICLR-2025"},{"title":"Dynamic Loss-Based Sample Reweighting for Improved Large Language Model Pretraining for ICLR 2025 - IBM Research","url":"https://research.ibm.com/publications/dynamic-loss-based-sample-reweighting-for-improved-large-language-model-pretraining"},{"title":"[2502.06733] Dynamic Loss-Based Sample Reweighting for Improved Large Language Model Pretraining","url":"https://arxiv.org/abs/2502.06733"},{"title":"Dynamic Loss-Based Sample Reweighting for Improved Large Language Model Pretraining","url":"https://arxiv.org/html/2502.06733v1"},{"title":"GitHub - F-JISOO/ICLR-2025-Submitted · GitHub","url":"https://github.com/F-JISOO/ICLR-2025-Submitted"},{"title":"ICLR Poster Dynamic Loss-Based Sample Reweighting for Improved Large Language Model Pretraining","url":"https://iclr.cc/virtual/2025/poster/28818"},{"title":"DYNAMIC LOSS-BASED SAMPLE REWEIGHTING FOR ...","url":"https://shiqiang.wang/papers/DS_ICLR2025.pdf"},{"title":"[Quick Review] Dynamic Loss-Based Sample Reweighting for Improved Large Language Model Pretraining","url":"https://liner.com/review/dynamic-lossbased-sample-reweighting-for-improved-large-language-model-pretraining"},{"title":"DYNAMIC LOSS-BASED SAMPLE REWEIGHTING FOR ...","url":"https://openreview.net/notes/edits/attachment?id=apDGBqycrP&name=pdf"}]

## Search Results for "Dynamic Loss-Based Sample Reweighting" ICLR 2025

I found comprehensive information about this ICLR 2025 paper. Here's what I discovered:

### Paper Overview

This is an ICLR 2025 paper on Dynamic Loss-Based Sample Reweighting for Improved Large Language Model Pretraining.

### Main Con
…[truncated 1573 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_literature-drayson-comparison_20260514T233124",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-14T23:34:16.215596+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://omega.cs.ucl.ac.uk/assets/pdf/papers/drayson2025-model-collapse.pdf",
  "prompt": "Extract the following details from this paper:\n1. The exact formula for reweighting (w = (1-q)^b or similar)\n2. How they select b (grid search? validation set? what values?)\n3. What models they use (GPT-2, SmolLM sizes?)\n4. What detectors they use and their AUC/accuracy\n5. What contamination ratios they test\n6. Whether training is iterative/recursive or single-pass\n7. Key perplexity improvement results\n8. Whether there is any adaptive or per-batch mechanism for b\n9. The dataset used\n10. Any theoretical justification for the formula"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_literature-drayson-comparison_20260514T233124",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://omega.cs.ucl.ac.uk/assets/pdf/papers/drayson2025-model-collapse.pdf",
    "prompt": "Extract the following details from this paper:\n1. The exact formula for reweighting (w = (1-q)^b or similar)\n2. How they select b (grid search? validation set? what values?)\n3. What models they use (GPT-2, SmolLM sizes?)\n4. What detectors they use and their AUC/accuracy\n5. What contamination ratios they test\n6. Whether training is iterative/recursive or single-pass\n7. Key perplexity improvement results\n8. Whether there is any adaptive or per-batch mechanism for b\n9. The dataset used\n10. Any theoretical justification for the formula"
  }
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-14T23:34:16.215727+00:00_

unable to verify the first certificate

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_literature-drayson-comparison_20260514T233124",
  "tool": "WebFetch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-14T23:34:16.215871+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://arxiv.org/html/2502.18049",
  "prompt": "Extract: 1. The exact formula for optimal weighting (w* = 1/phi claim). 2. What scenarios they study. 3. Key assumptions. 4. Whether it applies to LLM training or only theoretical distributions. 5. How they handle detection/contamination. 6. Main theoretical result in one paragraph."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_literature-drayson-comparison_20260514T233124",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://arxiv.org/html/2502.18049",
    "prompt": "Extract: 1. The exact formula for optimal weighting (w* = 1/phi claim). 2. What scenarios they study. 3. Key assumptions. 4. Whether it applies to LLM training or only theoretical distributions. 5. How they handle detection/contamination. 6. Main theoretical result in one paragraph."
  }
}
```

</details>

---

### Tool call

_source line 14 · 2026-05-14T23:34:16.216013+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://arxiv.org/abs/2502.06733",
  "prompt": "Extract: 1. The reweighting formula/strategy (LinUpper, Quadratic, Extremes). 2. Whether it uses detection scores or just loss values. 3. Model sizes tested. 4. Key results. 5. Whether it's online/dynamic per-batch."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_literature-drayson-comparison_20260514T233124",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://arxiv.org/abs/2502.06733",
    "prompt": "Extract: 1. The reweighting formula/strategy (LinUpper, Quadratic, Extremes). 2. Whether it uses detection scores or just loss values. 3. Model sizes tested. 4. Key results. 5. Whether it's online/dynamic per-batch."
  }
}
```

</details>

---

### Tool result

_source line 15 · 2026-05-14T23:34:16.216151+00:00_

# Dynamic Loss-Based Sample Reweighting for LLM Pretraining

Based on the arXiv abstract provided, here's what can be extracted:

**Reweighting Strategy:**
The paper introduces "novel algorithms for dynamic, instance-level data reweighting" that "adjust the weight of each training sample based on its loss value in an online fashion." Specific formula names (LinUpper, Quadratic, Extremes) are mentioned in your query but not detailed in this abstract.

**Detection Approach:**
The method uses loss values rather than separate detection scores. The abstract emphasizes "loss-based reweighting" that focuses on "deprioritizing redundant or uninformative data."

**Model Sizes Tested:**
Testing included "7B and 1.4B parameter LLMs to smaller-scale language models and linear regression problems."

**Key Results:**
The approach demonstrates "faster convergence and significantly improved performance" across evaluated tasks.

**Online/Dynamic Nature:**
Yes—described as "dynamic, instance-level data reweighting" operating "in an online fashion," allowing the model to "dynamically focus on more informative or important samples at the current training stage."

**Note:** The abstract doesn't explicitly detail the specific reweighting formulas. For complete technical details, you'd need to consult the full paper (available via PDF link on the arXiv page).

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_literature-drayson-comparison_20260514T233124",
  "tool": "WebFetch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-14T23:34:16.216299+00:00_

# Analysis of "Golden Ratio Weighting Prevents Model Collapse"

## 1. Optimal Weighting Formula

The exact optimal weight for real data is: **w* = (√(k² + 4k) - k)/2**, where k = n/m (ratio of real to synthetic samples).

When k=1 (equal amounts), this simplifies to **(√5 - 1)/2 ≈ 0.618**, the reciprocal of the golden ratio (φ).

## 2. Scenarios Studied

The paper investigates three main settings:

- **Multivariate Gaussian estimation** (warm-up case with closed-form solutions)
- **Generalized Linear Models** (GLMs encompassing linear/logistic/Poisson regression)
- **Nonparametric distribution estimation** (discrete distributions via empirical CDFs)

## 3. Key Assumptions

For GLMs, they require:
- Sub-Gaussian covariates (Assumption 1)
- Standard regularity conditions on the log-partition function: continuity, bounded moments, identifiability, smoothness (Assumption 2)

These are described as "relatively weak" and satisfied by standard models.

## 4. Application Scope

**Theoretical only.** The framework analyzes parametric/nonparametric statistical models, not LLM training directly. The authors note: "despite its importance, the practice of training a model on a combination of newly collected real data and synthetic data...remains theoretically underexplored."

LLMs are mentioned motivationally but not experimentally validated.

## 5. Contamination Handling

The paper **does not address detection or contamination.** It assumes synthetic data derives from previous model iterations in a "fresh data augmentation" setting where new real data arrives at each step—a stylized scenario unlike actual LLM retraining where old real data may be unavailable.

## 6. Main Theoretical Result (One Paragraph)

Under recursive training with newly collected real and synthetic data mixed at each step, weighted training schemes outperform naive mixing. The limiting estimation error follows a unified expression C(w,k)·[problem-dependent constant]/n across Gaussian, GLM, and nonparametri
…[truncated 349 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_literature-drayson-comparison_20260514T233124",
  "tool": "WebFetch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-14T23:34:16.216473+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Drayson \"Machine-generated text detection prevents language model collapse\" EMNLP 2025 reweighting formula"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_literature-drayson-comparison_20260514T233124",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Drayson \"Machine-generated text detection prevents language model collapse\" EMNLP 2025 reweighting formula"
  }
}
```

</details>

---

### Tool call

_source line 18 · 2026-05-14T23:34:16.216597+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Drayson 2025 model collapse \"(1-q)^b\" reweighting synthetic detection"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_literature-drayson-comparison_20260514T233124",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Drayson 2025 model collapse \"(1-q)^b\" reweighting synthetic detection"
  }
}
```

</details>

---

### Tool result

_source line 19 · 2026-05-14T23:34:16.216753+00:00_

Web search results for query: "Drayson 2025 model collapse "(1-q)^b" reweighting synthetic detection"

Links: [{"title":"Machine-generated text detection prevents language ...","url":"https://omega.cs.ucl.ac.uk/assets/pdf/papers/drayson2025-model-collapse.pdf"},{"title":"[2502.15654] Machine-generated text detection prevents language model collapse","url":"https://arxiv.org/abs/2502.15654"},{"title":"Machine-generated text detection prevents language model collapse - UCL Discovery","url":"https://discovery.ucl.ac.uk/id/eprint/10217226/"},{"title":"GitHub - GeorgeDrayson/model_collapse","url":"https://github.com/GeorgeDrayson/model_collapse"},{"title":"Escaping Model Collapse via Synthetic Data Verification: Near-term Improvements and Long-term ConvergenceThis project is supported by the AI2050 program at Schmidt Sciences (Grant G-24-66104) and Army Research Office Award W911NF-23-1-0030. We also thank Cong Ma from UChicago, Hongning Wang and Bo Li from Tsinghua, Pinyan Lu and Gavin Tang from Shanghai University of Finance and Economics for helpful discussions and suggestions.","url":"https://arxiv.org/html/2510.16657v1"},{"title":"Strong Model Collapse | OpenReview","url":"https://openreview.net/forum?id=et5l9qPUhm"},{"title":"The AI Model Collapse Risk is Not Solved in 2025","url":"https://www.winssolutions.org/ai-model-collapse-2025-recursive-training/"},{"title":"AI model collapse: The synthetic data trap and how to avoid it","url":"https://insights.manageengine.com/artificial-intelligence/ai-model-collapse-synthetic-data-trap/"},{"title":"Published as a conference paper at ICLR 2025 STRONG MODEL COLLAPSE","url":"https://proceedings.iclr.cc/paper_files/paper/2025/file/284afdc2309f9667d2d4fb9290235b0c-Paper-Conference.pdf"},{"title":"Curated Synthetic Data Doesn’t Have to Collapse: A Theoretical Study of Generative Retraining with Pluralistic Preferences","url":"https://arxiv.org/html/2605.07724"}]

Based on the search results, I found relevant information about t
…[truncated 1815 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_literature-drayson-comparison_20260514T233124",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-14T23:34:16.216940+00:00_

Web search results for query: "Drayson "Machine-generated text detection prevents language model collapse" EMNLP 2025 reweighting formula"

Links: [{"title":"[2502.15654] Machine-generated text detection prevents language model collapse","url":"https://arxiv.org/abs/2502.15654"},{"title":"Machine-generated text detection prevents language model collapse","url":"https://arxiv.org/html/2502.15654"},{"title":"(PDF) Machine-generated text detection prevents language model collapse","url":"https://www.researchgate.net/publication/397412242_Machine-generated_text_detection_prevents_language_model_collapse"},{"title":"Machine-generated text detection prevents language model ...","url":"https://discovery.ucl.ac.uk/id/eprint/10217226/1/2025.emnlp-main.1506.pdf"},{"title":"Machine-generated text detection prevents language ...","url":"https://omega.cs.ucl.ac.uk/assets/pdf/papers/drayson2025-model-collapse.pdf"},{"title":"GitHub - GeorgeDrayson/model_collapse","url":"https://github.com/GeorgeDrayson/model_collapse"},{"title":"Machine-generated text detection prevents language model collapse - UCL Discovery","url":"https://discovery.ucl.ac.uk/id/eprint/10217226/"},{"title":"Computation and Language Feb 2025","url":"https://www.arxiv.org/list/cs.CL/2025-02?skip=1325&show=250"},{"title":"Learning by Surprise: Surplexity for Mitigating Model Collapse in Generative AI","url":"https://arxiv.org/html/2410.12341v3"},{"title":"Machine-generated text detection prevents language model collapse","url":"https://openreview.net/pdf/22a5ff4d5a06122ee42c12ae85435b110781d685.pdf"}]

I found the paper! The paper was accepted by EMNLP 2025 (main), and it's authored by George Drayson, Emine Yilmaz, and Vasileios Lampos in the Proceedings of the 2025 Conference on Empirical Methods in Natural Language Processing.

The search results show the paper is available on arXiv (2502.15654) and through UCL Discovery. However, the search results don't contain the specific reweighting formula you're asking ab
…[truncated 898 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_literature-drayson-comparison_20260514T233124",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 21 · 2026-05-14T23:34:16.217201+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://arxiv.org/html/2502.15654",
  "prompt": "Extract ALL of the following details from this paper:\n1. The exact mathematical formula for reweighting/importance sampling (look for w = (1-q)^b or similar power-law weighting)\n2. How they select the exponent b - is it grid search on a validation set? What specific values of b do they test?\n3. What models are used (GPT-2 sizes, SmolLM sizes - exact parameter counts)\n4. What detector they use (name, architecture) and its detection accuracy/AUC\n5. What contamination ratios (percentage of synthetic data) they test\n6. Is the training iterative/recursive (multiple generations) or single-pass?\n7. Key perplexity (PPL) improvement numbers - before vs after reweighting\n8. Is there ANY adaptive or per-batch mechanism? Or is b fixed throughout training?\n9. What dataset is used for training?\n10. Any theoretical justification for choosing the specific formula form\n11. The importance sampling formula - what is q exactly? Detection probability?\n12. How many generations of recursive training do they run?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_literature-drayson-comparison_20260514T233124",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://arxiv.org/html/2502.15654",
    "prompt": "Extract ALL of the following details from this paper:\n1. The exact mathematical formula for reweighting/importance sampling (look for w = (1-q)^b or similar power-law weighting)\n2. How they select the exponent b - is it grid search on a validation set? What specific values of b do they test?\n3. What models are used (GPT-2 sizes, SmolLM sizes - exact parameter counts)\n4. What detector they use (name, architecture) and its detection accuracy/AUC\n5. What contamination ratios (percentage of synthetic data) they test\n6. Is the training iterative/recursive (multiple generations) or single-pass?\n7. Key perplexity (PPL) improvement numbers - before vs after reweighting\n8. Is there ANY adaptive or per-batch mechanism? Or is b fixed throughout training?\n9. What dataset is used for training?\n10. Any theoretical justification for choosing the specific formula form\n11. The importance sampling formula - what is q exactly? Detection probability?\n12. How many generations of recursive training do they run?"
  }
}
```

</details>

---

### Tool call

_source line 22 · 2026-05-14T23:34:16.217390+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://github.com/GeorgeDrayson/model_collapse",
  "prompt": "Extract: 1. The implementation details of the reweighting formula. 2. How b is selected. 3. What values of b are used. 4. The detector used. 5. Any code showing the weight calculation formula."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_literature-drayson-comparison_20260514T233124",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://github.com/GeorgeDrayson/model_collapse",
    "prompt": "Extract: 1. The implementation details of the reweighting formula. 2. How b is selected. 3. What values of b are used. 4. The detector used. 5. Any code showing the weight calculation formula."
  }
}
```

</details>

---

### Tool result

_source line 23 · 2026-05-14T23:34:16.217529+00:00_

# Extraction Results

Based on the GitHub page content provided, I cannot find the specific information you requested:

1. **Reweighting formula implementation details** - Not present in the README
2. **How b is selected** - Not documented in the page
3. **Values of b used** - Not specified
4. **Detector used** - The page mentions "a fine-tuned version of ModernBERT-base trained on the MAGE dataset" but no specific detector implementation details
5. **Weight calculation code** - Not included in the repository documentation shown

## What is documented:

The page indicates this is code for a paper titled "Machine-generated text detection prevents language model collapse" accepted at EMNLP 2025. The repository structure shows source files exist (`src/train.py`, `src/generate.py`), but their contents aren't visible in this GitHub page excerpt.

**Recommendation:** To access the specific technical details you're seeking, you would need to:
- Review the actual source code files in the `src/` directory
- Consult the full paper at the ACL Anthology link provided
- Check the actual Python implementation files not shown in this page overview

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_literature-drayson-comparison_20260514T233124",
  "tool": "WebFetch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 24 · 2026-05-14T23:34:16.217696+00:00_

# Extraction of Key Details from Model Collapse Paper

## 1. Reweighting Formula
The exact importance sampling weighting formula is:
```
w_j = (1-q(x_j))^b / Σ(1-q(x_l))^b
```
where w_j ∈ [0,1] denotes the weight for sample x_j.

## 2. Exponent b Selection
The exponent is "selected by evaluating each model on the Wikitext-2 validation set after 1 generation of recursive training." Optimal values vary by model: GPT-2 uses b=10, SmolLM 135M uses b=10, SmolLM 360M uses b=10, and SmolLM 1.7B uses b=1 (Table S1).

## 3. Models Tested
- **GPT-2**: 124M parameters
- **SmolLM2**: 135M, 360M, and 1.7B parameter variants

## 4. Detector Details
Three detector models are evaluated: RoBERTa (125M), DeBERTav3 (86M backbone + 98M embedding), and ModernBERT (150M). ModernBERT achieved the best in-distribution AUC of ".986" and out-of-distribution AUC of ".943".

## 5. Contamination Ratios
Three mixing scenarios are tested with coefficients (α, β, γ): (0.5, 1, 0), (0.5, 0.5, 0.5), and (1, 1, 0), where α represents human data proportion and β represents synthetic data proportion.

## 6. Training Methodology
The approach is fully iterative/recursive. "Successive rounds of recursive training are carried out. In each generation i, the original language model is fine-tuned using the synthetic dataset 𝒟^i." They conduct "10 iterations of recursive training."

## 7. Perplexity Improvements
For GPT-2 with top-k decoding at (0.5, 1, 0): -7.28% perplexity reduction. For SmolLM2 360M with top-k at (1, 1, 0): -3.05% reduction. SmolLM2 135M shows -4.19% improvement.

## 8. Adaptive Mechanism
The bias term b is **fixed throughout training** after hyperparameter selection. There is no per-batch adaptation mechanism described.

## 9. Training Dataset
"WikiText-2 dataset" with 36,718 documents in the training set and 4,358 in the test set. "Wikipedia articles are segmented into non-overlapping chunks of 512 tokens."

## 10. Theoretical Justification
Limited justification is provided. The method is 
…[truncated 482 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_literature-drayson-comparison_20260514T233124",
  "tool": "WebFetch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 25 · 2026-05-14T23:34:16.217902+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://arxiv.org/html/2502.06733v1",
  "prompt": "Extract: 1. The specific reweighting formulas (LinUpper, Quadratic, Extremes - what are the exact weight functions?). 2. Are weights based on per-sample loss only, or do they use external signals like detection scores? 3. Is there theoretical convergence analysis? 4. Model sizes and datasets used. 5. Key improvement numbers. 6. Authors."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_literature-drayson-comparison_20260514T233124",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://arxiv.org/html/2502.06733v1",
    "prompt": "Extract: 1. The specific reweighting formulas (LinUpper, Quadratic, Extremes - what are the exact weight functions?). 2. Are weights based on per-sample loss only, or do they use external signals like detection scores? 3. Is there theoretical convergence analysis? 4. Model sizes and datasets used. 5. Key improvement numbers. 6. Authors."
  }
}
```

</details>

---

### Tool call

_source line 26 · 2026-05-14T23:34:16.218038+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Drayson 2025 arXiv 2502.15654 SmolLM detector MAGE dataset importance resampling b=10"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_literature-drayson-comparison_20260514T233124",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Drayson 2025 arXiv 2502.15654 SmolLM detector MAGE dataset importance resampling b=10"
  }
}
```

</details>

---

### Tool result

_source line 27 · 2026-05-14T23:34:16.218181+00:00_

Web search results for query: "Drayson 2025 arXiv 2502.15654 SmolLM detector MAGE dataset importance resampling b=10"

Links: [{"title":"Machine-generated text detection prevents language model collapse","url":"https://arxiv.org/html/2502.15654"},{"title":"[2502.15654] Machine-generated text detection prevents language model collapse","url":"https://arxiv.org/abs/2502.15654"},{"title":"Integration Concept of the CBM Micro Vertex Detector","url":"https://arxiv.org/html/2502.04858"},{"title":"[2605.06322] SMolLM: Small Language Models Learn Small Molecular Grammar","url":"https://arxiv.org/abs/2605.06322"},{"title":"[2310.15654] A Survey on Detection of LLMs-Generated Content","url":"https://arxiv.org/abs/2310.15654"},{"title":"MSAD: A Deep Dive into Model Selection for Time series Anomaly Detection","url":"https://arxiv.org/html/2510.26643v1"},{"title":"Physics Jun 2024","url":"https://arxiv.org/list/physics/2024-06?skip=600&show=2000"},{"title":"Tiny Model, Big Logic: Diversity-Driven Optimization Elicits Large-Model","url":"https://arxiv.org/pdf/2511.06221"},{"title":"Deep Generative Models for Detector Signature Simulation","url":"https://arxiv.org/pdf/2312.09597"},{"title":"Comprehensive Review of Deep Unfolding Techniques for Next-Generation Wireless Communication Systems","url":"https://arxiv.org/html/2502.05952v1"}]

I found the paper! Here's what I discovered about this arXiv paper (2502.15654):

## Paper Overview

The paper is titled "Machine-generated text detection prevents language model collapse" by authors George Drayson, Emine Yilmaz, and Vasileios Lampos from University College London. It was accepted by EMNLP 2025 (main).

## Main Contributions

The authors train a machine-generated text detector and propose an importance resampling approach to prevent model collapse by up-sampling likely human content in the training data.

## Methodology

For the machine-generated text detector, they trained and evaluated three pretrained models (RoBERTa, DeBERTav3
…[truncated 658 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_literature-drayson-comparison_20260514T233124",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 28 · 2026-05-14T23:34:16.218350+00:00_

# Dynamic Loss-Based Sample Reweighting for LLM Pretraining: Key Findings

## 1. Reweighting Formulas

The paper proposes three strategies applied to normalized losses in range [-α, α]:

- **LinUpper**: "s_i := min{h_i + α, α}" - weights proportional to loss but capped at α
- **Quadratic**: "s_i := α(1 - h_i²/α²)" - emphasizes moderate losses, deprioritizes extremes
- **Extremes**: "s_i := |h_i|" - prioritizes both highest and lowest loss samples

Final weights use softmax: "w_i = e^(s_i/r) / Σ_j e^(s_j/r)" with temperature parameter r annealed during training.

## 2. Weight Basis

Weights depend **solely on per-sample loss values** computed during forward passes. No external signals, auxiliary models, or validation sets required—enabling fully online, single-pass reweighting suitable for large-scale pretraining where samples appear only once.

## 3. Theoretical Analysis

Yes, comprehensive convergence bounds provided:

- **Theorem 1** analyzes full gradient descent with convex losses, showing down-weighting low-loss samples improves convergence bounds
- **Theorem 2** extends analysis to minibatch SGD with momentum
- **Proposition 1** proves LinUpper achieves optimal KL-regularized loss-gap minimization

Key constraint: maximum weight limited to 2/M to prevent outlier overfitting.

## 4. Experimental Setup

**Models**: GPT2-mini (120M), GPT2-small (210M), GPT2-medium (300M), plus Llama 1.4B and 7B parameters

**Datasets**: SlimPajama (7 domains) and FineWeb 15T (100B-175B tokens sampled)

**Evaluation**: Per-domain perplexity and 5-shot reasoning benchmarks (LogiQA, SciQ, PiQA)

## 5. Key Improvements

- **GPT2-medium**: LinUpper achieves lower perplexity on 5/7 domains; 40.9% average accuracy vs. 39.4% uniform baseline on reasoning tasks
- **1.4B model**: 0.66% LUR improvement, 1.72% QA improvement; wins on 11/19 tasks
- **7B model**: 1.44% LUR improvement, 1.16% QA improvement; wins on 14/19 tasks
- Synergistic gains when combined with domain-level methods (DoGE, 
…[truncated 214 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_literature-drayson-comparison_20260514T233124",
  "tool": "WebFetch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 29 · 2026-05-14T23:34:16.218530+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/ 2>/dev/null && echo \"EXISTS\" || echo \"NOT_EXISTS\"",
  "description": "Check artifacts directory exists"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_literature-drayson-comparison_20260514T233124",
  "tool": "Bash",
  "tool_args": {
    "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/ 2>/dev/null && echo \"EXISTS\" || echo \"NOT_EXISTS\"",
    "description": "Check artifacts directory exists"
  }
}
```

</details>

---

### Tool result

_source line 30 · 2026-05-14T23:34:16.218660+00:00_

_project
data_generation
detector
evaluation
experiment_setup_draft.md
grid_b5_0_seed123
interim_mvp_analysis.md
literature_diff_drayson.md
literature_notes.md
manifest.yaml
method_section_draft.md
mvp_analysis_summary.md
related_work_notes.md
run_mvp.sh
seed42_diagnostic.md
training
training_progress_check.md
weighting
worker_output.md
EXISTS

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_literature-drayson-comparison_20260514T233124",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 31 · 2026-05-14T23:34:16.218776+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"Strong Model Collapse\" arXiv 2410.04840 authors Dohmatob ICLR 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_literature-drayson-comparison_20260514T233124",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"Strong Model Collapse\" arXiv 2410.04840 authors Dohmatob ICLR 2025"
  }
}
```

</details>

---

### Tool result

_source line 32 · 2026-05-14T23:34:16.218951+00:00_

Web search results for query: ""Strong Model Collapse" arXiv 2410.04840 authors Dohmatob ICLR 2025"

Links: [{"title":"[2410.04840] Strong Model Collapse","url":"https://arxiv.org/abs/2410.04840"},{"title":"Published as a conference paper at ICLR 2025 STRONG MODEL COLLAPSE","url":"https://proceedings.iclr.cc/paper_files/paper/2025/file/284afdc2309f9667d2d4fb9290235b0c-Paper-Conference.pdf"},{"title":"Strong Model Collapse Elvis Dohmatob1 e.dohmatob@meta.com Yunzhen Feng1,2,∗","url":"https://arxiv.org/pdf/2410.04840"},{"title":"Strong Model Collapse | OpenReview","url":"https://openreview.net/forum?id=et5l9qPUhm"},{"title":"Strong Model Collapse","url":"https://arxiv.org/html/2410.04840.pdf"},{"title":"A Closer Look at Model Collapse: From a Generalization-to-Memorization Perspective","url":"https://arxiv.org/html/2509.16499v1"},{"title":"Strong Model Collapse - ADS","url":"https://ui.adsabs.harvard.edu/abs/2024arXiv241004840D/abstract"},{"title":"ICLR Poster Strong Model Collapse","url":"https://iclr.cc/virtual/2025/poster/32070"},{"title":"Position: Model Collapse Does Not Mean What You Think","url":"https://arxiv.org/pdf/2503.03150"},{"title":"A Closer Look at Model Collapse: From a Generalization-to-Memorization Perspective | Request PDF","url":"https://www.researchgate.net/publication/395724450_A_Closer_Look_at_Model_Collapse_From_a_Generalization-to-Memorization_Perspective"}]

Based on the search results, here's information about "Strong Model Collapse":

## Paper Overview

The paper "Strong Model Collapse" by Elvis Dohmatob and 3 other authors establishes a strong form of the model collapse phenomenon within the scaling laws paradigm, demonstrating critical performance degradation due to synthetic data in training corpora.

## Key Findings

The results show that even the smallest fraction of synthetic data (e.g., as little as 1 per 1000) can still lead to model collapse, where larger and larger training sets do not enhance performance.

In a simplified regime
…[truncated 797 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_literature-drayson-comparison_20260514T233124",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 33 · 2026-05-14T23:34:16.219127+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/literature_diff_drayson.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_literature-drayson-comparison_20260514T233124",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/literature_diff_drayson.md"
  }
}
```

</details>

---

### Tool result

_source line 34 · 2026-05-14T23:34:16.219308+00:00_

1	# Drayson et al. (EMNLP 2025) 新颖性差异化调研报告
2	
3	> 调研日期: 2026-05-14
4	> 关联决策: D013
5	
6	---
7	
8	## 1. Drayson et al. 摘要
9	
10	### 论文信息
11	- **全名**: Machine-generated text detection prevents language model collapse
12	- **作者**: George Drayson, Emine Yilmaz, Vasileios Lampos
13	- **单位**: University College London (UCL)
14	- **Venue**: EMNLP 2025 Main Conference (arXiv: 2502.15654)
15	- **代码**: https://github.com/GeorgeDrayson/model_collapse
16	
17	### 方法
18	- **公式**: wⱼ = (1−q(xⱼ))^b / Σₗ(1−q(xₗ))^b
19	  - q(x): ModernBERT 检测器输出的 machine-generated 概率（AUC=0.986 in-domain, 0.943 OOD）
20	  - b ≥ 1: bias term，控制权重分布倾斜程度
21	- **采样策略**: Sampling Importance Resampling (SIR)——按权重有放回采样 n×k 个样本（k=1.5），加 rmax 上限防止单样本过度重复
22	- **检测器**: ModernBERT fine-tuned on MAGE dataset，label smoothing α=0.1，temperature scaling 校准
23	
24	### b 的选择方式
25	- **验证集选取，非 grid search，也非 adaptive**
26	- 具体做法："We select values for rmax and b by evaluating each model on the Wikitext-2 validation set after 1 generation of recursive training"
27	- 实际使用的值：
28	  - GPT-2 (124M): b=10
29	  - SmolLM 135M: b=10
30	  - SmolLM 360M: b=10
31	  - SmolLM 1.7B: b=1
32	- **无系统性的 b 敏感度分析或 ablation**
33	
34	### 实验设置
35	- **数据**: WikiText-2 (36,718 training documents)
36	- **模型**: GPT-2 124M, SmolLM2 135M/360M/1.7B (2 model families, 4 models)
37	- **递归训练**: 10 generations of recursive fine-tuning
38	- **解码策略**: 6 种 (greedy, beam search, pure sampling, temperature, top-k, nucleus)
39	- **污染场景**: 3 种 mixing configurations (α,β,γ)，从 equal splits 到 cross-generational accumulation
40	- **评估指标**: Perplexity, diversity (distinct-n), MAUVE (semantic similarity)
41	
42	### 主要 Claims
43	1. 模型坍塌受解码策略选择显著影响
44	2. 训练一个提供校准置信度估计的 MGT 检测器
45	3. 使用检测器输出通过引导数据重采样防止坍塌
46	4. 跨 4 个 LLM、2 个模型家族、6 种解码策略验证
47	5. 某些设置下甚至超越 "Oracle"（完美检测器）
48	
49	### 结果
50	- Perplexity 改善: −0.85% to −25.65%
51	- Diversity 增益: +3.44% to +14.62%
52	- MAUVE 提升: +8.46% to +20.92%
53	
54	---
55	
56	## 2. 与我们方法的关键差异点
57	
58	| 维度 | Drayson et al. (EMNLP 2025) | 我们 (pro
…[truncated 6628 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_literature-drayson-comparison_20260514T233124",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 35 · 2026-05-14T23:34:16.219501+00:00_

called Write

<details open><summary>🔧 Tool call — Write</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/drayson_comparison.md",
  "content": "# Drayson et al. (EMNLP 2025) 深度对比分析\n\n> 日期: 2026-05-14 | 关联: D013 新颖性风险\n\n---\n\n## 1. Drayson 方法总结（200 字）\n\nDrayson et al. 提出 **detect-and-reweight** 防止语言模型在递归训练中坍塌。核心公式：**wⱼ = (1−q(xⱼ))^b / Σₗ(1−q(xₗ))^b**，其中 q(x) 为 ModernBERT 检测器输出的 machine-generated 概率。通过 Sampling Importance Resampling (SIR) 按权重重采样训练数据，上采样可能为人类撰写的内容。检测器在 MAGE 数据集上 fine-tune，in-domain AUC=0.986，OOD AUC=0.943。b 值通过在 WikiText-2 验证集上 1 代递归训练后评估选取（GPT-2/SmolLM 135M/360M 用 b=10，SmolLM 1.7B 用 b=1）。实验在 4 个模型（GPT-2 124M, SmolLM 135M/360M/1.7B）上进行 10 代递归训练，覆盖 6 种解码策略。结果：PPL 降低 0.85%–25.65%，diversity 提升 3.44%–14.62%。**b 在整个训练过程中固定，无自适应机制。**\n\n---\n\n## 2. 我们 vs Drayson 对比表\n\n| 维度 | Drayson et al. (EMNLP 2025) | 我们 (Adaptive b*) |\n|------|---------------------------|-------------------|\n| **b 选择方法** | 验证集 empirical 选取，per-model 固定 | α_eff(b) + ESS 约束自适应推导，per-batch 动态调整 |\n| **检测器** | ModernBERT 150M (AUC=0.986) | TF-IDF + LR (AUC=0.939)，证明轻量检测器即可 |\n| **污染设置** | 已知比例（实验控制 α,β,γ） | 未知比例（从 batch 统计量在线估计） |\n| **理论基础** | 无（SIR 启发式，无 b 选取理论） | 收敛理论 motivated α_eff(b) 推导 + 连续谱统一框架 |\n| **计算开销** | 需 per-model validation run（等价于 grid search） | 零额外 validation cost，从 batch 统计量直接计算 |\n| **训练场景** | 递归训练 model collapse prevention | Web corpus 一次性预训练中的未知污染 |\n| **数据规模** | WikiText-2 (36K docs, ~2M tokens) | FineWeb subset (132M+ tokens) |\n| **生成器** | 单一生成器 per experiment | 多生成器 cross-contamination |\n| **动态性** | b 固定（训练全程不变） | b* per-batch 自适应 |\n| **框架贡献** | 提出 detect-and-reweight 方法 | 统一 soft-to-hard 连续谱 (b=0 uniform → b→∞ hard filter) |\n\n---\n\n## 3. 三个关键差异化论点（Related Work 可用）\n\n### 论点 1: From Heuristic to Principled（最直接）\n\n> Drayson et al. (2025) demonstrate that detect-and-reweight with w=(1−q)^b effectively prevents model collapse, but their bias term b is selected empirically per model via validation-set evaluation after one generation of recursive training. This requires a labeled validation set and separate tuning runs for each model architecture. We derive a principled, batch-adaptive b* from convergence-theory-inspired α_eff(b) with ESS constraints, eliminating validation-based tuning while matching or exceeding their best heuristic choices.\n\n### 论点 2: Unknown Contamination Proportion（差异化最强）\n\n> Prior detect-and-reweight approaches (Drayson et al., 2025) operate under controlled recursive training where contamination fractions are known by experimental design. In contrast, we address the realistic web-corpus scenario where neither the contamination proportion nor a clean validation set is available. Our adaptive b* is derived solely from batch-level detector statistics, making it applicable to large-scale pretraining where contamination is organic and unquantified.\n\n### 论点 3: Lightweight Detector Sufficiency（实用性角度）\n\n> Drayson et al. rely on ModernBERT (150M parameters, AUC=0.986), a state-of-the-art neural detector requiring GPU inference over the entire training corpus. We demonstrate that a simple TF-IDF + logistic regression detector (AUC=0.939) suffices when paired with our adaptive b*, reducing detector compute by orders of magnitude. This suggests the reweighting mechanism's effectiveness depends more on principled exponent selection than on detector precision.\n\n---\n\n## 4. Golden Ratio Weighting 总结（100 字）\n\nHe & Xu (arXiv 2502.18049, 2025) 理论证明在递归训练中混合真实与合成数据时，最优权重 **w\\* = (√(k²+4k)−k)/2**（k=真实/合成样本比）。当 k=1 时 w\\*=1/φ≈0.618（黄金比例倒数）。在高斯分布估计、GLM、非参数估计三种设置下验证。**局限**：纯理论工作，假设已知污染比例，未涉及检测器或 LLM 实验，不处理 unknown/online 设置。\n\n---\n\n## 5. 其他相关论文一句话总结\n\n| 论文 | Venue | 一句话 |\n|------|-------|--------|\n| **Strong Model Collapse** (Dohmatob & Feng et al.) | ICLR 2025 (Spotlight), arXiv:2410.04840 | 理论证明即使 0.1% 合成数据污染也会导致 scaling law 失效，更大模型反而放大坍塌 |\n| **Dynamic Loss-Based Sample Reweighting** (Sow et al., IBM/OSU/TUM) | ICLR 2025, arXiv:2502.06733 | 基于 per-sample loss 的在线重加权（LinUpper/Quadratic/Extremes + softmax temperature），不使用检测器，纯 loss signal 驱动，7B 模型验证有效 |\n| **DoReMi** (Xie et al.) | NeurIPS 2023 | 域级别权重优化（Group DRO + 小模型代理），不处理 instance-level 污染 |\n| **DSIR** (Xie et al.) | NeurIPS 2023 | N-gram 特征重要性采样选择数据子集匹配目标分布 |\n| **Escaping Model Collapse via Synthetic Data Verification** | arXiv:2510.16657 | 提出验证机制筛选合成数据质量，与我们的 detection-based 方法互补 |\n\n---\n\n## 6. 搜索来源\n\n- Drayson et al.: [arXiv:2502.15654](https://arxiv.org/abs/2502.15654) | [HTML](https://arxiv.org/html/2502.15654) | [GitHub](https://github.com/GeorgeDrayson/model_collapse)\n- Golden Ratio Weighting: [arXiv:2502.18049](https://arxiv.org/abs/2502.18049)\n- Strong Model Collapse: [arXiv:2410.04840](https://arxiv.org/abs/2410.04840) | [ICLR 2025](https://openreview.net/forum?id=et5l9qPUhm)\n- Dynamic Loss-Based Reweighting: [arXiv:2502.06733](https://arxiv.org/abs/2502.06733) | [GitHub](https://github.com/sowmaster/Sample-Level-Loss-Reweighting-ICLR-2025)\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_literature-drayson-comparison_20260514T233124",
  "tool": "Write",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/drayson_comparison.md",
    "content": "# Drayson et al. (EMNLP 2025) 深度对比分析\n\n> 日期: 2026-05-14 | 关联: D013 新颖性风险\n\n---\n\n## 1. Drayson 方法总结（200 字）\n\nDrayson et al. 提出 **detect-and-reweight** 防止语言模型在递归训练中坍塌。核心公式：**wⱼ = (1−q(xⱼ))^b / Σₗ(1−q(xₗ))^b**，其中 q(x) 为 ModernBERT 检测器输出的 machine-generated 概率。通过 Sampling Importance Resampling (SIR) 按权重重采样训练数据，上采样可能为人类撰写的内容。检测器在 MAGE 数据集上 fine-tune，in-domain AUC=0.986，OOD AUC=0.943。b 值通过在 WikiText-2 验证集上 1 代递归训练后评估选取（GPT-2/SmolLM 135M/360M 用 b=10，SmolLM 1.7B 用 b=1）。实验在 4 个模型（GPT-2 124M, SmolLM 135M/360M/1.7B）上进行 10 代递归训练，覆盖 6 种解码策略。结果：PPL 降低 0.85%–25.65%，diversity 提升 3.44%–14.62%。**b 在整个训练过程中固定，无自适应机制。**\n\n---\n\n## 2. 我们 vs Drayson 对比表\n\n| 维度 | Drayson et al. (EMNLP 2025) | 我们 (Adaptive b*) |\n|------|---------------------------|-------------------|\n| **b 选择方法** | 验证集 empirical 选取，per-model 固定 | α_eff(b) + ESS 约束自适应推导，per-batch 动态调整 |\n| **检测器** | ModernBERT 150M (AUC=0.986) | TF-IDF + LR (AUC=0.939)，证明轻量检测器即可 |\n| **污染设置** | 已知比例（实验控制 α,β,γ） | 未知比例（从 batch 统计量在线估计） |\n| **理论基础** | 无（SIR 启发式，无 b 选取理论） | 收敛理论 motivated α_eff(b) 推导 + 连续谱统一框架 |\n| **计算开销** | 需 per-model validation run（等价于 grid search） | 零额外 validation cost，从 batch 统计量直接计算 |\n| **训练场景** | 递归训练 model collapse prevention | Web corpus 一次性预训练中的未知污染 |\n| **数据规模** | WikiText-2 (36K docs, ~2M tokens) | FineWeb subset (132M+ tokens) |\n| **生成器** | 单一生成器 per experiment | 多生成器 cross-contamination |\n| **动态性** | b 固定（训练全程不变） | b* per-batch 自适应 |\n| **框架贡献** | 提出 detect-and-reweight 方法 | 统一 soft-to-hard 连续谱 (b=0 uniform → b→∞ hard filter) |\n\n---\n\n## 3. 三个关键差异化论点（Related Work 可用）\n\n### 论点 1: From Heuristic to Principled（最直接）\n\n> Drayson et al. (2025) demonstrate that detect-and-reweight with w=(1−q)^b effectively prevents model collapse, but their bias term b is selected empirically per model via validation-set evaluation after one generation of recursive training. This requires a labeled validation set and separate tuning runs for each model architecture. We derive a principled, batch-adaptive b* from convergence-theory-inspired α_eff(b) with ESS constraints, eliminating validation-based tuning while matching or exceeding their best heuristic choices.\n\n### 论点 2: Unknown Contamination Proportion（差异化最强）\n\n> Prior detect-and-reweight approaches (Drayson et al., 2025) operate under controlled recursive training where contamination fractions are known by experimental design. In contrast, we address the realistic web-corpus scenario where neither the contamination proportion nor a clean validation set is available. Our adaptive b* is derived solely from batch-level detector statistics, making it applicable to large-scale pretraining where contamination is organic and unquantified.\n\n### 论点 3: Lightweight Detector Sufficiency（实用性角度）\n\n> Drayson et al. rely on ModernBERT (150M parameters, AUC=0.986), a state-of-the-art neural detector requiring GPU inference over the entire training corpus. We demonstrate that a simple TF-IDF + logistic regression detector (AUC=0.939) suffices when paired with our adaptive b*, reducing detector compute by orders of magnitude. This suggests the reweighting mechanism's effectiveness depends more on principled exponent selection than on detector precision.\n\n---\n\n## 4. Golden Ratio Weighting 总结（100 字）\n\nHe & Xu (arXiv 2502.18049, 2025) 理论证明在递归训练中混合真实与合成数据时，最优权重 **w\\* = (√(k²+4k)−k)/2**（k=真实/合成样本比）。当 k=1 时 w\\*=1/φ≈0.618（黄金比例倒数）。在高斯分布估计、GLM、非参数估计三种设置下验证。**局限**：纯理论工作，假设已知污染比例，未涉及检测器或 LLM 实验，不处理 unknown/online 设置。\n\n---\n\n## 5. 其他相关论文一句话总结\n\n| 论文 | Venue | 一句话 |\n|------|-------|--------|\n| **Strong Model Collapse** (Dohmatob & Feng et al.) | ICLR 2025 (Spotlight), arXiv:2410.04840 | 理论证明即使 0.1% 合成数据污染也会导致 scaling law 失效，更大模型反而放大坍塌 |\n| **Dynamic Loss-Based Sample Reweighting** (Sow et al., IBM/OSU/TUM) | ICLR 2025, arXiv:2502.06733 | 基于 per-sample loss 的在线重加权（LinUpper/Quadratic/Extremes + softmax temperature），不使用检测器，纯 loss signal 驱动，7B 模型验证有效 |\n| **DoReMi** (Xie et al.) | NeurIPS 2023 | 域级别权重优化（Group DRO + 小模型代理），不处理 instance-level 污染 |\n| **DSIR** (Xie et al.) | NeurIPS 2023 | N-gram 特征重要性采样选择数据子集匹配目标分布 |\n| **Escaping Model Collapse via Synthetic Data Verification** | arXiv:2510.16657 | 提出验证机制筛选合成数据质量，与我们的 detection-based 方法互补 |\n\n---\n\n## 6. 搜索来源\n\n- Drayson et al.: [arXiv:2502.15654](https://arxiv.org/abs/2502.15654) | [HTML](https://arxiv.org/html/2502.15654) | [GitHub](https://github.com/GeorgeDrayson/model_collapse)\n- Golden Ratio Weighting: [arXiv:2502.18049](https://arxiv.org/abs/2502.18049)\n- Strong Model Collapse: [arXiv:2410.04840](https://arxiv.org/abs/2410.04840) | [ICLR 2025](https://openreview.net/forum?id=et5l9qPUhm)\n- Dynamic Loss-Based Reweighting: [arXiv:2502.06733](https://arxiv.org/abs/2502.06733) | [GitHub](https://github.com/sowmaster/Sample-Level-Loss-Reweighting-ICLR-2025)\n"
  }
}
```

</details>

---

### Tool result

_source line 36 · 2026-05-14T23:34:16.219699+00:00_

File created successfully at: /home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/drayson_comparison.md

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_literature-drayson-comparison_20260514T233124",
  "tool": "Write",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 37 · 2026-05-14T23:34:16.219874+00:00_

文件已写入 `artifacts/drayson_comparison.md`。

关键发现：
- **Drayson 的 b 是验证集 empirical 选取，训练中固定**（GPT-2/SmolLM 135M/360M 用 b=10，1.7B 用 b=1），无任何 adaptive 机制
- **你们的 adaptive b\* 在文献中无先例**——没有找到任何工作对 detection-score 权重指数做自适应推导
- 已有 `literature_diff_drayson.md` 包含更详细的策略建议（Angle A+B+C），新文件以更紧凑的格式呈现可直接用于论文的对比表和差异化论点

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_research_literature-drayson-comparison_20260514T233124"
}
```

</details>

---
