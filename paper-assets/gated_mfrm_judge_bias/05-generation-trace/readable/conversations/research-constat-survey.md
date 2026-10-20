# research constat survey

**Fair Scores via Joint Calibration: A Gated Many-Facet Rasch Model for Disentangling Judge Bias and Contamination in LLM Evaluation** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 27
- **Recorded user turns:** 0
- **Tool calls:** 13
- **Original source:** `logs/chats/worker_research_constat_survey_20260521T211244.jsonl`
- **Structured JSON:** [`1f5ab48f6776f7b49593.json`](../../sessions/1f/1f5ab48f6776f7b49593.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

27 recorded events

### Tool call

_source line 1 · 2026-05-21T21:14:41.831609+00:00_

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
  "session": "worker_research_constat_survey_20260521T211244",
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

_source line 2 · 2026-05-21T21:14:41.831919+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_constat_survey_20260521T211244",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-21T21:14:41.832086+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "ConStat statistical detection benchmark contamination github"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_constat_survey_20260521T211244",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ConStat statistical detection benchmark contamination github"
  }
}
```

</details>

---

### Tool call

_source line 4 · 2026-05-21T21:14:41.832255+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "ConStat NeurIPS 2024 code"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_constat_survey_20260521T211244",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ConStat NeurIPS 2024 code"
  }
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-21T21:14:41.832382+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"ConStat: Statistical Detection and Quantification of Benchmark Contamination\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_constat_survey_20260521T211244",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"ConStat: Statistical Detection and Quantification of Benchmark Contamination\""
  }
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-21T21:14:41.832574+00:00_

Web search results for query: "ConStat NeurIPS 2024 code"

Links: [{"title":"NeurIPS Poster ConStat: Performance-Based Contamination Detection in Large Language Models","url":"https://neurips.cc/virtual/2024/poster/96266"},{"title":"Formatting Instructions For NeurIPS 2024","url":"https://arxiv.org/html/2404.10198v3"},{"title":"NeurIPS 2024 Call for Papers","url":"https://neurips.cc/Conferences/2024/CallForPapers"},{"title":"NeurIPS 2024 - Overleaf, Online LaTeX Editor","url":"https://www.overleaf.com/latex/templates/neurips-2024/tpsbbrdqcmsh"},{"title":"NeurIPS 2024 Schedule","url":"https://neurips.cc/virtual/2024/calendar"},{"title":"2024 Dates and Deadlines","url":"https://nips.cc/Conferences/2024/Dates"}]

Based on the search results, I found information about ConStat at NeurIPS 2024. ConStat is a paper presented as a poster at NeurIPS 2024 by Jasper Dekoninck, Mark Müller, and Martin Vechev, with a Project Page, Paper, Slides, and Poster available.

The work proposes a novel definition of contamination as artificially inflated and non-generalizing benchmark performance instead of the inclusion of benchmark samples in the training data.

However, the search results don't provide a direct link to the code repository. To access the code, you would likely need to visit the project page mentioned in the NeurIPS poster listing or check the paper's supplementary materials. The paper appears to be available on OpenReview and other standard venues where NeurIPS papers are hosted.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_constat_survey_20260521T211244",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 7 · 2026-05-21T21:14:41.832763+00:00_

Web search results for query: "ConStat statistical detection benchmark contamination github"

Links: [{"title":"ConStat: Performance-Based Contamination Detection in Large Language Models","url":"https://arxiv.org/html/2405.16281v1"},{"title":"ConStat: Performance-Based Contamination Detection in Large Language Models","url":"https://constat.ai/"},{"title":"ConStat: Performance-Based Contamination Detection in Large Language   Models","url":"https://arxiv.org/pdf/2405.16281"},{"title":"[2405.16281] ConStat: Performance-Based Contamination Detection in Large Language Models","url":"https://arxiv.org/abs/2405.16281"},{"title":"GitHub - lyy1994/awesome-data-contamination: The Paper List on Data Contamination for Large Language Models Evaluation. · GitHub","url":"https://github.com/lyy1994/awesome-data-contamination"},{"title":"ConStat: Performance-Based Contamination Detection in Large Language Models","url":"https://files.sri.inf.ethz.ch/website/papers/dekoninck2024constat.pdf"},{"title":"GitHub - eth-sri/ConStat: A statistical test for contamination detection in language models. · GitHub","url":"https://github.com/eth-sri/ConStat"},{"title":"ConStat: Performance-Based Contamination Detection in Large Language Models","url":"https://www.researchgate.net/publication/397204928_ConStat_Performance-Based_Contamination_Detection_in_Large_Language_Models"}]

Based on the search results, here's what I found about ConStat:

## ConStat: Performance-Based Contamination Detection

ConStat is a statistical method that reliably detects and quantifies contamination by comparing performance between a primary and reference benchmark relative to a set of reference models.

The method defines contamination as artificially inflated, non-generalizing performance—specifically, a model is contaminated if its performance relative to other models is significantly higher on the original benchmark than on a similar reference benchmark.

### Key Features

ConStat can detect any model with infla
…[truncated 684 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_constat_survey_20260521T211244",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-21T21:14:41.833001+00:00_

Web search results for query: ""ConStat: Statistical Detection and Quantification of Benchmark Contamination""

Links: [{"title":"ConStat: Performance-Based Contamination Detection in Large Language Models | OpenReview","url":"https://openreview.net/forum?id=ALISPmDPCq"},{"title":"ConStat: Performance-Based Contamination Detection in Large Language   Models","url":"https://arxiv.org/pdf/2405.16281"},{"title":"[Quick Review] ConStat: Performance-Based Contamination Detection in Large Language Models","url":"https://liner.com/review/constat-performancebased-contamination-detection-in-large-language-models"},{"title":"ConStat: Performance-Based Contamination Detection in Large Language Models","url":"https://constat.ai/"},{"title":"NeurIPS Poster ConStat: Performance-Based Contamination Detection in Large Language Models","url":"https://neurips.cc/virtual/2024/poster/96266"},{"title":"ConStat: Performance-Based Contamination Detection in Large Language Models | SRI Lab","url":"https://www.sri.inf.ethz.ch/publications/dekoninck2024constat"},{"title":"[2405.16281] ConStat: Performance-Based Contamination Detection in Large Language Models","url":"https://arxiv.org/abs/2405.16281"},{"title":"[Literature Review] ConStat: Performance-Based Contamination Detection in Large Language Models","url":"https://www.themoonlight.io/en/review/constat-performance-based-contamination-detection-in-large-language-models"},{"title":"ConStat: Performance-Based Contamination Detection in Large Language Models","url":"https://proceedings.neurips.cc/paper_files/paper/2024/file/a7f89793b9e6f8c6568dbbb6ff727b9b-Paper-Conference.pdf"},{"title":"ConStat: Performance-Based Contamination Detection in Large Language Models","url":"https://arxiv.org/html/2405.16281v1"}]

I found detailed information about ConStat. Here's what the research shows:

## Overview

ConStat is a statistical method that reliably detects and quantifies contamination by comparing performance between a primary and reference ben
…[truncated 1445 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_constat_survey_20260521T211244",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-21T21:14:41.833189+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "site:github.com/eth-sri/ConStat README"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_constat_survey_20260521T211244",
  "tool": "WebSearch",
  "tool_args": {
    "query": "site:github.com/eth-sri/ConStat README"
  }
}
```

</details>

---

### Tool call

_source line 10 · 2026-05-21T21:14:41.833316+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "constat.ai contamination detection API usage reference benchmark"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_constat_survey_20260521T211244",
  "tool": "WebSearch",
  "tool_args": {
    "query": "constat.ai contamination detection API usage reference benchmark"
  }
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-21T21:14:41.833521+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "LogProber benchmark contamination detection LLM alternative"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_constat_survey_20260521T211244",
  "tool": "WebSearch",
  "tool_args": {
    "query": "LogProber benchmark contamination detection LLM alternative"
  }
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-21T21:14:41.833715+00:00_

Web search results for query: "site:github.com/eth-sri/ConStat README"

Links: [{"title":"GitHub - eth-sri/ConStat: A statistical test for contamination detection in language models. · GitHub","url":"https://github.com/eth-sri/ConStat"},{"title":"ConStat/src/constat/base.py at main · eth-sri/ConStat","url":"https://github.com/eth-sri/ConStat/blob/main/src/constat/base.py"},{"title":"ConStat/src/constat/detection.py at main · eth-sri/ConStat","url":"https://github.com/eth-sri/ConStat/blob/main/src/constat/detection.py"},{"title":"ConStat/src/constat/spline_fit.py at main · eth-sri/ConStat","url":"https://github.com/eth-sri/ConStat/blob/main/src/constat/spline_fit.py"},{"title":"ethereum · GitHub","url":"https://github.com/ethereum"},{"title":"SRI Lab, ETH Zurich · GitHub","url":"https://github.com/eth-sri"},{"title":"eth-sri repositories · GitHub","url":"https://github.com/orgs/eth-sri/repositories"},{"title":"GitHub - eth-sri/eran: ETH Robustness Analyzer for Deep Neural Networks · GitHub","url":"https://github.com/eth-sri/eran"},{"title":"GitHub - eth-sri/eth-sri.github.io: SRI Group Website · GitHub","url":"https://github.com/eth-sri/eth-sri.github.io"},{"title":"GitHub - eth-sri/learch · GitHub","url":"https://github.com/eth-sri/learch"}]

Based on the search results, I found information about the ConStat repository. Here's what the README reveals:

## ConStat Overview

This repository contains the code necessary to reproduce the results from the paper ConStat: Performance-Based Contamination Detection in Large Language Models and use ConStat for your projects.

ConStat is a tool designed for detecting performance-based contamination in large language models. This project aims to provide an efficient and effective method for identifying and measuring contamination in language models by analyzing performance metrics.

## Key Features

The document provides instructions for installation, usage, and reproducing results, along with details on the custom forks and mod
…[truncated 645 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_constat_survey_20260521T211244",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 13 · 2026-05-21T21:14:41.833894+00:00_

Web search results for query: "constat.ai contamination detection API usage reference benchmark"

Links: [{"title":"GitHub - eth-sri/ConStat: A statistical test for contamination detection in language models. · GitHub","url":"https://github.com/eth-sri/ConStat"},{"title":"ConStat: Performance-Based Contamination Detection in Large Language Models","url":"https://constat.ai/"},{"title":"ConStat/src/constat/detection.py at main · eth-sri/ConStat","url":"https://github.com/eth-sri/ConStat/blob/main/src/constat/detection.py"},{"title":"ConStat: Performance-Based Contamination Detection in Large Language Models","url":"https://arxiv.org/html/2405.16281v1"},{"title":"[2405.16281] ConStat: Performance-Based Contamination Detection in Large Language Models","url":"https://arxiv.org/abs/2405.16281"},{"title":"ConStat: Performance-Based Contamination Detection in Large Language Models","url":"https://proceedings.neurips.cc/paper_files/paper/2024/file/a7f89793b9e6f8c6568dbbb6ff727b9b-Paper-Conference.pdf"},{"title":"[Quick Review] ConStat: Performance-Based Contamination Detection in Large Language Models","url":"https://liner.com/review/constat-performancebased-contamination-detection-in-large-language-models"},{"title":"[Literature Review] ConStat: Performance-Based Contamination Detection in Large Language Models","url":"https://www.themoonlight.io/en/review/constat-performance-based-contamination-detection-in-large-language-models"},{"title":"ConStat: Performance-Based Contamination Detection in Large Language Models","url":"https://www.researchgate.net/publication/397204928_ConStat_Performance-Based_Contamination_Detection_in_Large_Language_Models"},{"title":"NeurIPS Poster ConStat: Performance-Based Contamination Detection in Large Language Models","url":"https://neurips.cc/virtual/2024/poster/96266"}]

Based on the search results, I found information about ConStat, a contamination detection method for large language models. However, the results show that ConStat is **no
…[truncated 1433 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_constat_survey_20260521T211244",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-21T21:14:41.834060+00:00_

Web search results for query: "LogProber benchmark contamination detection LLM alternative"

Links: [{"title":"LogProber: Disentangling confidence from contamination in LLM responses","url":"https://arxiv.org/pdf/2408.14352"},{"title":"Assessing Contamination in Large Language Models: Introducing the LogProber method","url":"https://arxiv.org/html/2408.14352v1"},{"title":"[2408.14352] LogProber: Disentangling confidence from contamination in LLM responses","url":"https://arxiv.org/abs/2408.14352"},{"title":"LogProber: Disentangling confidence from contamination in LLM responses","url":"https://arxiv.org/html/2408.14352v3"},{"title":"[2408.14352v3] LogProber: Disentangling confidence from contamination in LLM responses","url":"https://arxiv.org/abs/2408.14352v3"},{"title":"PaCoST: Paired Confidence Significance Testing for Benchmark   Contamination Detection in Large Language Models","url":"https://arxiv.org/pdf/2406.18326"}]

Based on the search results, here's information about LogProber and benchmark contamination detection for LLMs:

## LogProber Overview

LogProber is a novel, efficient algorithm designed to detect contamination in a black box setting by focusing on the familiarity with the question rather than the answer. The algorithm allows for disentangling contamination from confidence in a way that is computationally cheap and adapted to the short question/answer format commonly used in machine learning benchmarks and cognitive tests.

## The Contamination Problem

In machine learning, contamination refers to situations where testing data leak into the training set, which is particularly relevant for evaluating Large Language Models that are trained on massive, opaque corpora of text scraped from the web. When contamination occurs, benchmark results are not valid, as a model's performance may not reflect its true capabilities in a given domain, but rather its ability to merely retrieve training data.

## Alternative Detection Methods

The search results in
…[truncated 478 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_constat_survey_20260521T211244",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-21T21:14:41.834237+00:00_

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
  "session": "worker_research_constat_survey_20260521T211244",
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

_source line 16 · 2026-05-21T21:14:41.834361+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_constat_survey_20260521T211244",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-21T21:14:41.834522+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://github.com/eth-sri/ConStat",
  "prompt": "Extract the full README content. I need: 1) Installation instructions, 2) Usage API/interface (what classes/functions, what inputs, what outputs), 3) Required data format, 4) Dependencies, 5) License, 6) Last update info, 7) Stars count if visible. Be very detailed about the Python API - what arguments does the main ConStat class/function take, and what does it return."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_constat_survey_20260521T211244",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://github.com/eth-sri/ConStat",
    "prompt": "Extract the full README content. I need: 1) Installation instructions, 2) Usage API/interface (what classes/functions, what inputs, what outputs), 3) Required data format, 4) Dependencies, 5) License, 6) Last update info, 7) Stars count if visible. Be very detailed about the Python API - what arguments does the main ConStat class/function take, and what does it return."
  }
}
```

</details>

---

### Tool call

_source line 18 · 2026-05-21T21:14:41.834656+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://github.com/eth-sri/ConStat/blob/main/src/constat/detection.py",
  "prompt": "Extract the full source code of detection.py. I need to understand: 1) The ConStat class constructor parameters, 2) The main detection method signature and return values, 3) What data format it expects (numpy arrays? lists? dataframes?), 4) The key algorithms used (bootstrapping, spline fitting, etc). Show all class methods and their signatures."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_constat_survey_20260521T211244",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://github.com/eth-sri/ConStat/blob/main/src/constat/detection.py",
    "prompt": "Extract the full source code of detection.py. I need to understand: 1) The ConStat class constructor parameters, 2) The main detection method signature and return values, 3) What data format it expects (numpy arrays? lists? dataframes?), 4) The key algorithms used (bootstrapping, spline fitting, etc). Show all class methods and their signatures."
  }
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-21T21:14:41.834784+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://github.com/eth-sri/ConStat/blob/main/src/constat/base.py",
  "prompt": "Extract the full source code of base.py. I need to understand: 1) The base class/data structures used, 2) What Benchmark and Model classes look like, 3) Input data format requirements. Show all class definitions and method signatures."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_constat_survey_20260521T211244",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://github.com/eth-sri/ConStat/blob/main/src/constat/base.py",
    "prompt": "Extract the full source code of base.py. I need to understand: 1) The base class/data structures used, 2) What Benchmark and Model classes look like, 3) Input data format requirements. Show all class definitions and method signatures."
  }
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-21T21:14:41.834914+00:00_

# BaseClass Analysis from ConStat

Based on the GitHub page content provided, here's what I can extract:

## Base Class Structure

The `BaseClass` serves as a serialization/deserialization framework. Key characteristics:

**Core Methods:**
- `__init__(**kwargs)` - Stores keyword arguments
- `generate_settings()` - Returns a dictionary with class name and serialized attributes
- `save(path)` - Writes settings to JSON file
- `load(path, **kwargs)` - Reads and instantiates from JSON

**Data Transformation Methods:**
- `generate_list_settings(list_)` - Converts lists recursively, handling nested BaseClass instances
- `generate_kwarg_setting(kwargs)` - Recursively normalizes dictionaries

**Deserialization Methods:**
- `load_from_settings(settings)` - Factory method that reconstructs objects from saved state
- `load_from_dict(dict_)` and `load_from_list_settings(list_)` - Handle nested structures

## Limitations of Available Information

The provided content shows **only the base.py file**. The document does not include:
- Benchmark class definition
- Model class definition
- Input data format specifications

To understand these components, you would need to examine other files in the `/src/constat/` directory, such as dedicated modules for benchmarks and models.

**Recommendation:** Access the full repository to review additional source files for complete architectural understanding.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_constat_survey_20260521T211244",
  "tool": "WebFetch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 21 · 2026-05-21T21:14:41.835060+00:00_

# ConStat Detection Module Analysis

## ConStat Class Constructor Parameters

```python
def __init__(self, n_bootstrap=1000, bootstrap_models=True, 
             add_extended_models=True, random_performance=(0,0), 
             p_value_delta=0, sort=True)
```

**Parameters:**
- `n_bootstrap` (int): Bootstrap iteration count (default: 1000)
- `bootstrap_models` (bool): Whether to resample model selection (default: True)
- `add_extended_models` (bool): Whether to include random baseline (default: True)
- `random_performance` (tuple): Range for random model performance (default: (0,0))
- `p_value_delta` (int): Delta threshold for p-value computation (default: 0)
- `sort` (bool): Whether to sort performance values (default: True)

## Main Detection Methods

**Primary method:**
```python
def test(self, scores_model, scores_model_ref_data, 
         scores_ref_models, scores_ref_models_ref_data)
```

**Extended method (returns fitted functions):**
```python
def return_functions_test(self, scores_model, scores_model_ref_data, 
                         scores_ref_models, scores_ref_models_ref_data)
```

## Data Format Expectations

All inputs are NumPy arrays with shapes:
- `scores_model`: (n_samples,)
- `scores_model_ref_data`: (n_samples_ref,)
- `scores_ref_models`: (n_ref_models, n_samples)
- `scores_ref_models_ref_data`: (n_ref_models, n_samples_ref)

## Return Values Dictionary

The test methods return a dictionary containing:
- `p_value`: Statistical significance measure
- `estimated_contamination`: Contamination level estimate
- `estimated_contamination_std`: Standard deviation
- `min_delta_095`: 95% confidence lower bound
- `delta`: Mean difference between actual and estimated scores
- `delta_std`: Difference standard deviation
- `estimated_contamination_025/975`: Confidence interval bounds (extended method only)
- `functions`: Fitted spline functions (extended method only)

## Key Algorithms

**Bootstrap resampling** (via `bootstrap()` function):
- Performs samplin
…[truncated 1042 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_constat_survey_20260521T211244",
  "tool": "WebFetch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 22 · 2026-05-21T21:14:41.835222+00:00_

# ConStat Repository Summary

## 1. Installation Instructions

The setup process involves creating a Conda environment and installing dependencies:

```bash
conda create -n constat python=3.10
conda activate constat
python -m pip install -e .
python -m pip install -r requirements.txt
cd lm-evaluation-harness
python -m pip install -e .
cd ..
```

Additional requirements are needed only for reproducing results beyond basic usage.

## 2. Usage API/Interface

**Main Class: ConStat**

Constructor parameters:
- `n_bootstrap` (int): Number of bootstrap iterations (high values recommended)
- `p_value_delta` (float): Delta value for p-value reporting
- `random_performance` (tuple): Range for random model performance (e.g., `(0,0)` for deterministic, `(0.25,0.25)` for multiple-choice)

**Primary Method: `test()`**

Input parameters:
- `accuracies_model`: Array of model accuracies on benchmark samples
- `accuracies_model_reference`: Model accuracies on reference benchmark
- `accuracies`: Reference model accuracies on benchmark (2D array)
- `accuracies_reference`: Reference model accuracies on reference benchmark (2D array)

Output dictionary contains:
- `p_value`: Statistical significance result
- `estimated_contamination`: Predicted uncontaminated performance
- `estimated_contamination_025` / `_975`: Confidence interval bounds
- `estimated_contamination_std`: Standard deviation estimate
- `delta`: Estimated contamination effect size
- `delta_std`: Effect size standard deviation
- `min_delta_095`: 95th percentile lower bound

**Utility Function: `perform_test()`**

Evaluates contamination across benchmarks with parameters for model names, benchmark variants, reference models, and output paths.

## 3. Required Data Format

- Benchmark scores as NumPy arrays (1D for single model, 2D for multiple models)
- CSV-based benchmark storage (via custom `csv_loader.py`)
- LM Evaluation Harness output with sample-level logs (requires `--log-samples` parameter)
- Directory structure: `[BAS
…[truncated 717 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_constat_survey_20260521T211244",
  "tool": "WebFetch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 23 · 2026-05-21T21:14:41.835379+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "LogProber github code \"disentangling confidence from contamination\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_constat_survey_20260521T211244",
  "tool": "WebSearch",
  "tool_args": {
    "query": "LogProber github code \"disentangling confidence from contamination\""
  }
}
```

</details>

---

### Tool call

_source line 24 · 2026-05-21T21:14:41.835526+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://github.com/eth-sri/ConStat/blob/main/src/constat/spline_fit.py",
  "prompt": "Extract the spline fitting code. What does make_smoothing_spline do? What are its inputs/outputs? How does it map reference benchmark performance to primary benchmark performance?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_constat_survey_20260521T211244",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://github.com/eth-sri/ConStat/blob/main/src/constat/spline_fit.py",
    "prompt": "Extract the spline fitting code. What does make_smoothing_spline do? What are its inputs/outputs? How does it map reference benchmark performance to primary benchmark performance?"
  }
}
```

</details>

---

### Tool result

_source line 25 · 2026-05-21T21:14:41.835661+00:00_

# Spline Fitting Code Analysis

## Function Purpose

`make_smoothing_spline` computes coefficients for a smoothing cubic spline function that balances smoothness with proximity to data points.

## Inputs

- **x**: Array of abscissas (independent variable values), must be ascending with length ≥ 5
- **y**: Array of ordinates (dependent variable values), same length as x
- **w** (optional): Weight vector; defaults to all ones if not provided
- **lam** (optional): Regularization parameter controlling smoothness; automatically determined via GCV criteria if None

## Outputs

The function returns a tuple containing:
1. **BSpline object**: A callable spline function in B-spline basis form
2. **lam**: The regularization parameter value actually used in the fit

## Functional Approach

The algorithm solves a regularized weighted regression problem: "sum of weighted squared residuals plus lambda times the integral of squared second derivatives."

**Note on benchmark mapping**: The provided code does not contain any reference to benchmark performance mapping. The document focuses exclusively on mathematical spline fitting methodology and does not address performance benchmarking or secondary-to-primary performance translation.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_constat_survey_20260521T211244",
  "tool": "WebFetch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 26 · 2026-05-21T21:14:41.835814+00:00_

Web search results for query: "LogProber github code "disentangling confidence from contamination""

Links: [{"title":"[2408.14352] LogProber: Disentangling confidence from contamination in LLM responses","url":"https://arxiv.org/abs/2408.14352"},{"title":"[2408.14352v3] LogProber: Disentangling confidence from contamination in LLM responses","url":"https://arxiv.org/abs/2408.14352v3"},{"title":"LogProber: Disentangling confidence from contamination in LLM responses","url":"https://arxiv.org/html/2408.14352v2"},{"title":"LogProber: Disentangling confidence from contamination in LLM responses","url":"https://arxiv.org/pdf/2408.14352"},{"title":"Assessing Contamination in Large Language Models: Introducing the LogProber method","url":"https://arxiv.org/html/2408.14352v1"}]

Based on the search results, I found information about LogProber and the research paper on "Disentangling confidence from contamination in LLM responses." Here's what I found:

LogProber is a novel, efficient algorithm designed to detect contamination in a black box setting that focuses on the familiarity with the question rather than the answer. It is capable of detecting common forms of contamination in LLMs while disentangling confidence from contamination.

LogProber is inexpensive, deterministic, fully automated, well-suited to the short question/answer format commonly found in benchmark tasks, and capable of disentangling contamination from confidence.

The research paper by Nicolas Yax, Pierre-Yves Oudeyer, and Stefano Palminteri appears to be published on arXiv. The search results show the academic paper discussing the algorithm and its applications, but I did not find a direct GitHub repository link in these results. You may want to check the arXiv page or the authors' institutional websites for links to the code repository.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_constat_survey_20260521T211244",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 27 · 2026-05-21T21:14:41.836004+00:00_

信息已收集完整。注意论文实际标题是 "ConStat: **Performance-Based** Contamination Detection in Large Language Models"，而非 "Statistical Detection and Quantification"——后者可能是项目 ROADMAP 中的简称。

### ConStat

- **官方 Repo**: [github.com/eth-sri/ConStat](https://github.com/eth-sri/ConStat) — Apache-2.0, 6 stars, 低活跃度 (4 commits)，ETH Zurich SRI Lab 出品
- **论文**: [NeurIPS 2024 Poster](https://neurips.cc/virtual/2024/poster/96266)，作者 Jasper Dekoninck, Mark Müller, Martin Vechev
- **核心定义**: Contamination = 不泛化的虚高性能（而非训练集包含 benchmark 样本）

**接口设计**:
```python
from constat.detection import ConStat

cs = ConStat(
    n_bootstrap=1000,          # bootstrap 迭代次数
    random_performance=(0.25, 0.25),  # 随机猜测的正确率（如4选1=0.25）
    p_value_delta=0,           # p-value 阈值偏移
)

result = cs.test(
    scores_model,              # shape (n_samples,) — 待测模型在原始 benchmark 上的 per-item 0/1 得分
    scores_model_ref_data,     # shape (n_ref_samples,) — 待测模型在 reference benchmark 上的 per-item 得分
    scores_ref_models,         # shape (n_ref_models, n_samples) — 参考模型群在原始 benchmark 上的得分
    scores_ref_models_ref_data # shape (n_ref_models, n_ref_samples) — 参考模型群在 reference benchmark 上的得分
)
```

**输出 dict**:
| 字段 | 含义 |
|------|------|
| `p_value` | 污染的统计显著性 |
| `estimated_contamination` | 预测的无污染性能 |
| `delta` | 实际 vs 预测性能差（= 污染影响量） |
| `min_delta_095` | delta 的 95% 置信下界 |
| `estimated_contamination_025/975` | 置信区间 |

**数据需求**:
1. **Reference benchmark** — 与原始 benchmark 同分布但未被泄露的变体（重述/合成/同任务不同 benchmark），**这是最大依赖**
2. **Reference models** — 一组已知未污染（或代表"正常"性能曲线）的模型在两个 benchmark 上的 per-item 得分
3. 所有数据均为 numpy array，per-item binary scores

**适配难度**: **中等**
- ConStat 核心统计测试本身是轻量 Python 包，`pip install -e .` 即可
- **主要工作量在准备数据**：需要 (a) 构造 reference benchmark、(b) 收集一批 reference models 的 per-item evaluation 结果
- 它自带 lm-evaluation-harness fork 用于跑评测，但我们可以用自己的评测 pipeline，只要最终喂入 numpy 格式的 per-item scores 即可
- 不需要访问模型权重/logprobs——纯粹基于 accuracy，**黑盒方法**

**关键限制**:
- 需要 reference benchmark（构造成本高，且质量直接影响检测力）
- 需要多个 reference models 的评测结果（论文用了 ~20 个模型）
- 检测粒度是 per-model（判断整个模型是否污染），**不直接输出 per-item exposure level e_i**
- `delta` 是全局污染影响量，不是逐 item 的

**⚠️ 对 G-MFRM 的关键 gap**: G-MFRM 需要 **per-item e_i**（每道题的曝光程度），但 ConStat 输出的是 per-model 的全局污染检测。要获得 per-item 粒度，需要额外工程：
- 可利用 `return_functions_test()` 返回的 spline 拟合函数，对每个 item 计算其 observed vs expected 性能偏差作为 proxy e_i
- 或者对 item 子集做 leave-one-out 式的 ConStat 测试（计算量大）

**替代方案**:

| 方法 | 特点 | 可行性 |
|------|------|--------|
| **LogProber** | 基于 logprobs 的黑盒方法，检测对 question 的 familiarity，计算便宜，per-item 粒度天然支持 | 需要 logprob API 访问；无官方 GitHub repo 找到 |
| **Min-K% Prob** | 基于 token logprobs 分布尾部，per-item 检测 | 需要模型 logprobs |
| **CDD / PaCoST** | 配对置信度测试 | 类似 ConStat 思路，需要 reference data |
| **直接用 performance gap** | 原始 vs rephrased benchmark 的 per-item accuracy 差作为 e_i 的 proxy | 最简单，不依赖统计框架 |

**建议**: ConStat 的核心统计思想可用，但 per-item e_i 需要我们自己从 spline 拟合中推导。最简方案是直接用 item-level performance gap（original vs reference）作为 e_i proxy，ConStat 的 spline hardness correction 可作为更精确的校正层。

Sources:
- [ConStat GitHub](https://github.com/eth-sri/ConStat)
- [ConStat Paper (arXiv)](https://arxiv.org/abs/2405.16281)
- [ConStat Project Page](https://constat.ai/)
- [NeurIPS 2024 Poster](https://neurips.cc/virtual/2024/poster/96266)
- [LogProber Paper](https://arxiv.org/abs/2408.14352)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_research_constat_survey_20260521T211244"
}
```

</details>

---
