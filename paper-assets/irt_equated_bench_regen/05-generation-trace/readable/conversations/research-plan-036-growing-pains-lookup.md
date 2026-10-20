# research plan 036 growing pains lookup

**Temporal Score Incomparability in LLM Benchmarks: A Large-Scale Psychometric Audit of 5,227 Models** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 33
- **Recorded user turns:** 0
- **Tool calls:** 16
- **Original source:** `logs/chats/worker_research_plan_036_growing_pains_lookup_20260521T160331.jsonl`
- **Structured JSON:** [`c7b20b9f63de10ff9775.json`](../../sessions/c7/c7b20b9f63de10ff9775.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

33 recorded events

### Tool call

_source line 1 · 2026-05-21T16:05:53.269234+00:00_

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
  "session": "worker_research_plan_036_growing_pains_lookup_20260521T160331",
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

_source line 2 · 2026-05-21T16:05:53.269850+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_plan_036_growing_pains_lookup_20260521T160331",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-21T16:05:53.270245+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Growing Pains LLM benchmark contamination paper"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_plan_036_growing_pains_lookup_20260521T160331",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Growing Pains LLM benchmark contamination paper"
  }
}
```

</details>

---

### Tool call

_source line 4 · 2026-05-21T16:05:53.270547+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"Growing Pains\" benchmark evaluation LLM 2024 2025 arXiv"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_plan_036_growing_pains_lookup_20260521T160331",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"Growing Pains\" benchmark evaluation LLM 2024 2025 arXiv"
  }
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-21T16:05:53.270860+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "FPC focal point contamination benchmark items LLM"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_plan_036_growing_pains_lookup_20260521T160331",
  "tool": "WebSearch",
  "tool_args": {
    "query": "FPC focal point contamination benchmark items LLM"
  }
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-21T16:05:53.271211+00:00_

Web search results for query: "FPC focal point contamination benchmark items LLM"

Links: [{"title":"Towards Contamination Resistant Benchmarks","url":"https://arxiv.org/pdf/2505.08389"},{"title":"Contamination Report for Multilingual Benchmarks","url":"https://arxiv.org/pdf/2410.16186"},{"title":"When Benchmarks Leak: Inference-Time Decontamination for LLMs","url":"https://arxiv.org/html/2601.19334v1"},{"title":"NLP Evaluation in trouble: On the Need to Measure LLM Data Contamination   for each Benchmark","url":"https://arxiv.org/pdf/2310.18018"},{"title":"Benchmark Data Contamination of Large Language Models: A Survey","url":"https://arxiv.org/pdf/2406.04244"},{"title":"Silicon Bureaucracy and AI Test-Oriented Education: Contamination Sensitivity and Score Confidence in LLM Benchmarks","url":"https://arxiv.org/pdf/2603.21636"},{"title":"LiveBench: A Challenging, Contamination-Limited LLM Benchmark","url":"https://arxiv.org/pdf/2406.19314"},{"title":"When Benchmarks Leak: Inference-Time Decontamination for LLMs","url":"https://arxiv.org/pdf/2601.19334"}]

Based on the search results, I found information about LLM benchmark contamination, though the specific term "FPC focal point contamination" doesn't appear in these results. Here's what the search revealed:

## LLM Benchmark Contamination Overview

Benchmark contamination refers to the presence of test datasets in Large Language Model pre-training or post-training data. Contamination can lead to inflated scores on benchmarks, compromising evaluation results and making it difficult to determine the capabilities of models.

## The Problem with Contaminated Benchmark Items

The benchmark problem is not only whether exact test items appeared in training, but also whether the model encountered generalized information sufficient to point toward the correct answer. Over 15 LLMs exhibit inflated benchmark performance on six popular benchmarks, where the estimated contamination rate ranges from 1% to 45%.

## Mitigation Ap
…[truncated 767 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_plan_036_growing_pains_lookup_20260521T160331",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 7 · 2026-05-21T16:05:53.271595+00:00_

Web search results for query: "Growing Pains LLM benchmark contamination paper"

Links: [{"title":"Growing Pains: Extensible and Efficient LLM Benchmarking Via Fixed Parameter Calibration","url":"https://arxiv.org/html/2604.12843"},{"title":"NLP Evaluation in trouble: On the Need to Measure LLM Data Contamination   for each Benchmark","url":"https://arxiv.org/pdf/2310.18018"},{"title":"Data Contamination Can Cross Language Barriers","url":"https://arxiv.org/pdf/2406.13236"},{"title":"Rethinking Benchmark and Contamination for Language Models with   Rephrased Samples","url":"https://arxiv.org/pdf/2311.04850"},{"title":"Contamination Report for Multilingual Benchmarks","url":"https://arxiv.org/pdf/2410.16186"},{"title":"Benchmark Data Contamination of Large Language Models: A Survey","url":"https://arxiv.org/html/2406.04244v1"}]

I found several papers related to LLM benchmark contamination, though the first result appears to be about an "Extensible and Efficient LLM Benchmarking" paper. The most directly relevant results are:

**Key Papers on LLM Benchmark Contamination:**

1. "NLP Evaluation in trouble: On the Need to Measure LLM Data Contamination for each Benchmark" - This position paper defines different levels of data contamination and argues for automatic and semi-automatic measures to detect benchmark contamination, as the consequences can cause wrong scientific conclusions to be published.

2. "Data Contamination Can Cross Language Barriers" - This paper presents a cross-lingual form of contamination that can inflate LLMs' performance while evading current detection methods, and proposes generalization-based approaches to unmask such contamination.

3. "Rethinking Benchmark and Contamination for Language Models with Rephrased Samples" - This work proposes a stronger LLM-based decontamination method and reveals significant previously unknown test overlap, finding that 8-18% of the HumanEval benchmark overlaps in pre-training sets like RedPajama-Data-1T and Sta
…[truncated 753 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_plan_036_growing_pains_lookup_20260521T160331",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-21T16:05:53.272009+00:00_

Web search results for query: ""Growing Pains" benchmark evaluation LLM 2024 2025 arXiv"

Links: [{"title":"[2604.12843] Growing Pains: Extensible and Efficient LLM Benchmarking Via Fixed Parameter Calibration","url":"https://arxiv.org/abs/2604.12843"},{"title":"Growing Pains: Extensible and Efficient LLM Benchmarking Via Fixed Parameter Calibration","url":"https://arxiv.org/html/2604.12843"},{"title":"[2601.20251] Efficient Evaluation of LLM Performance with Statistical Guarantees","url":"https://arxiv.org/abs/2601.20251"},{"title":"On Robustness and Reliability of Benchmark-Based Evaluation of LLMs","url":"https://arxiv.org/pdf/2509.04013"},{"title":"Examining the robustness of LLM evaluation to the distributional   assumptions of benchmarks","url":"https://arxiv.org/pdf/2404.16966"},{"title":"Benchmark Health Index: A Systematic Framework for Benchmarking the Benchmarks of LLMs","url":"https://arxiv.org/pdf/2602.11674"},{"title":"Benchmark^2: Systematic Evaluation of LLM Benchmarks","url":"https://arxiv.org/pdf/2601.03986"}]

Based on the search results, I found the paper you're looking for:

## Growing Pains: Extensible and Efficient LLM Benchmarking Via Fixed Parameter Calibration

The paper addresses the challenge that the rapid release of both language models and benchmarks makes it increasingly costly to evaluate every model on every dataset. In practice, models are often evaluated on different samples, making scores difficult to compare across studies.

**Main Approach:**
The authors propose a framework based on multidimensional Item Response Theory (IRT) that uses anchor items to calibrate new benchmarks to the evaluation suite while holding previously calibrated item parameters fixed. This approach supports a realistic evaluation setting in which datasets are introduced over time and models are evaluated only on the datasets available at the time of evaluation, while a fixed anchor set for each dataset is used so that results from different evaluation per
…[truncated 819 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_plan_036_growing_pains_lookup_20260521T160331",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-21T16:05:53.272436+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://arxiv.org/abs/2604.12843",
  "prompt": "Extract the following information: 1) Full paper title, 2) All authors, 3) Full abstract, 4) Venue/date, 5) Any links to code/data repositories (GitHub, HuggingFace, etc.), 6) What does FPC stand for in this paper? 7) Do they mention anchor items or item lists? 8) Do they release any item-level data or contamination flags?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_plan_036_growing_pains_lookup_20260521T160331",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://arxiv.org/abs/2604.12843",
    "prompt": "Extract the following information: 1) Full paper title, 2) All authors, 3) Full abstract, 4) Venue/date, 5) Any links to code/data repositories (GitHub, HuggingFace, etc.), 6) What does FPC stand for in this paper? 7) Do they mention anchor items or item lists? 8) Do they release any item-level data or contamination flags?"
  }
}
```

</details>

---

### Tool call

_source line 10 · 2026-05-21T16:05:53.272768+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"Growing Pains\" \"Fixed Parameter Calibration\" LLM benchmark GitHub code data"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_plan_036_growing_pains_lookup_20260521T160331",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"Growing Pains\" \"Fixed Parameter Calibration\" LLM benchmark GitHub code data"
  }
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-21T16:05:53.273050+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "arXiv 2604.12843 \"Growing Pains\" code repository anchor items MMLU"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_plan_036_growing_pains_lookup_20260521T160331",
  "tool": "WebSearch",
  "tool_args": {
    "query": "arXiv 2604.12843 \"Growing Pains\" code repository anchor items MMLU"
  }
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-21T16:05:53.273364+00:00_

Web search results for query: "arXiv 2604.12843 "Growing Pains" code repository anchor items MMLU"

Links: [{"title":"[2604.12843] Growing Pains: Extensible and Efficient LLM Benchmarking Via Fixed Parameter Calibration","url":"https://arxiv.org/abs/2604.12843"},{"title":"Growing Pains: Extensible and Efficient LLM Benchmarking Via Fixed Parameter Calibration","url":"https://arxiv.org/html/2604.12843"},{"title":"Machine Learning Reveals Synovial Fibroblast Genes Associated with Pain Affect Sensory Nerve Growth in Rheumatoid Arthritis","url":"https://www.medrxiv.org/content/10.1101/2023.08.17.23294232.full.pdf"},{"title":"The LMSz method - an automatable scalable approach to constructing gene-specific growth charts in rare disorders","url":"https://www.medrxiv.org/content/10.1101/2024.08.19.24312213.full.pdf"},{"title":"Benchmarking Large Language Models for Bio-Image Analysis Code Generation","url":"https://www.biorxiv.org/content/10.1101/2024.04.19.590278.full.pdf"}]

Based on the search results, I found the arXiv paper 2604.12843. Here's what the search revealed:

The paper "Growing Pains: Extensible and Efficient LLM Benchmarking Via Fixed Parameter Calibration" proposes a framework that uses anchor items to calibrate benchmarks, and in large-scale experiments on more than 400 models, it predicts full-evaluation performance within 2-3 percentage points using only 100 anchor questions per dataset.

The paper specifically addresses the use of anchor items in the context of an Item Response Theory (IRT) framework. However, the search results don't contain detailed information about a code repository or specific details about how these anchor items relate to MMLU in particular. To get more specific information about the code repository and the detailed implementation regarding anchor items and MMLU, you may want to check the paper's GitHub repository directly, which is typically linked from the arXiv abstract page.


REMINDER: You MUST include the sources above in yo
…[truncated 50 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_plan_036_growing_pains_lookup_20260521T160331",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 13 · 2026-05-21T16:05:53.273729+00:00_

# Paper Information Extraction

**1) Full Paper Title:**
"Growing Pains: Extensible and Efficient LLM Benchmarking Via Fixed Parameter Calibration"

**2) All Authors:**
Eliya Habba, Itay Itzhak, Asaf Yehudai, Yotam Perlitz, Elron Bandel, Michal Shmueli-Scheuer, Leshem Choshen, Gabriel Stanovsky

**3) Full Abstract:**
The authors propose "a framework based on multidimensional Item Response Theory (IRT) that uses anchor items to calibrate new benchmarks to the evaluation suite while holding previously calibrated item parameters fixed." The approach enables extending benchmark suites over time while preserving score comparability, predicting full-evaluation performance within 2-3 percentage points using only 100 anchor questions per dataset, achieving Spearman ρ ≥ 0.9 for ranking preservation.

**4) Venue/Date:**
arXiv:2604.12843 [cs.CL], submitted April 14, 2026 (v1); revised April 15, 2026 (v2)

**5) Code/Data Repository Links:**
"Code available at [this https URL](https://github.com/eliyahabba/growing-pains)"

**6) What FPC Stands For:**
The acronym "FPC" is not defined in the provided content.

**7) Anchor Items/Item Lists:**
Yes, the paper explicitly mentions using "anchor items" and "anchor questions" (100 per dataset) for calibration purposes.

**8) Item-Level Data or Contamination Flags:**
The document does not mention releasing item-level data or contamination flags.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_plan_036_growing_pains_lookup_20260521T160331",
  "tool": "WebFetch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-21T16:05:53.274109+00:00_

Web search results for query: ""Growing Pains" "Fixed Parameter Calibration" LLM benchmark GitHub code data"

Links: [{"title":"Growing Pains: Extensible and Efficient LLM Benchmarking Via Fixed Parameter Calibration","url":"https://arxiv.org/html/2604.12843"},{"title":"[2604.12843] Growing Pains: Extensible and Efficient LLM Benchmarking Via Fixed Parameter Calibration","url":"https://arxiv.org/abs/2604.12843"},{"title":"Calibrating Behavioral Parameters with Large Language Models","url":"https://arxiv.org/pdf/2602.01022"},{"title":"GitHub - NIKHIL0VERMA/LLM-Confidence-Calibration-Benchmark: To analyze whether modern open-source LLMs are well-calibrated, and how calibration varies across different task types such as reasoning, common sense, binary decision making, and factual truthfulness. · GitHub","url":"https://github.com/NIKHIL0VERMA/LLM-Confidence-Calibration-Benchmark"},{"title":"llm-benchmarking · GitHub Topics · GitHub","url":"https://github.com/topics/llm-benchmarking"},{"title":"Calibrating LLM Confidence by Probing Perturbed Representation Stability","url":"https://arxiv.org/pdf/2505.21772"}]

Based on the search results, I found the paper you're looking for:

**"Growing Pains: Extensible and Efficient LLM Benchmarking Via Fixed Parameter Calibration"** - Code is available at https://github.com/eliyahabba/growing-pains/

The paper proposes a framework based on multidimensional Item Response Theory (IRT) that uses anchor items to calibrate new benchmarks to the evaluation suite while holding previously calibrated item parameters fixed. The approach supports a realistic evaluation setting in which datasets are introduced over time and models are evaluated only on the datasets available at the time of evaluation, while a fixed anchor set for each dataset is used so that results from different evaluation periods can be compared directly.

In large-scale experiments on more than 400 models, the framework predicts full-evaluation performance within 2-3 percent
…[truncated 204 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_plan_036_growing_pains_lookup_20260521T160331",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-21T16:05:53.274506+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://github.com/eliyahabba/growing-pains",
  "prompt": "List all files and directories in this repository. Look specifically for: 1) Any data files (CSV, JSON, TSV, etc.), 2) Anchor item lists or item IDs, 3) MMLU-related data, 4) Contamination flags or labels, 5) README content describing what data is available, 6) Any mention of DIF or differential item functioning"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_plan_036_growing_pains_lookup_20260521T160331",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://github.com/eliyahabba/growing-pains",
    "prompt": "List all files and directories in this repository. Look specifically for: 1) Any data files (CSV, JSON, TSV, etc.), 2) Anchor item lists or item IDs, 3) MMLU-related data, 4) Contamination flags or labels, 5) README content describing what data is available, 6) Any mention of DIF or differential item functioning"
  }
}
```

</details>

---

### Tool call

_source line 16 · 2026-05-21T16:05:53.274825+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://arxiv.org/html/2604.12843",
  "prompt": "Extract from this paper: 1) How are anchor items selected? What criteria? 2) Is there any mention of contamination detection, DIF (differential item functioning), or item flagging? 3) What specific datasets/benchmarks do they use (especially MMLU)? 4) Do they release anchor item lists publicly? 5) Is there any mention of item-level contamination or data leakage? 6) What is the exact definition of FPC in this paper? 7) Any mention of focal point contamination?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_plan_036_growing_pains_lookup_20260521T160331",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://arxiv.org/html/2604.12843",
    "prompt": "Extract from this paper: 1) How are anchor items selected? What criteria? 2) Is there any mention of contamination detection, DIF (differential item functioning), or item flagging? 3) What specific datasets/benchmarks do they use (especially MMLU)? 4) Do they release anchor item lists publicly? 5) Is there any mention of item-level contamination or data leakage? 6) What is the exact definition of FPC in this paper? 7) Any mention of focal point contamination?"
  }
}
```

</details>

---

### Tool result

_source line 17 · 2026-05-21T16:05:53.275145+00:00_

# Repository Contents Analysis

Based on the GitHub page content provided, here's what's documented about data and files:

## Data Files Mentioned

The repository contains benchmark response files in `data/input/`:
- `lb.pickle` (Leaderboard benchmark)
- `mmlu_fields.pickle` (MMLU benchmark)

According to the README: "The item-level response data is from Polo et al. (2024b), 'tinyBenchmarks: evaluating LLMs with fewer examples' (ICML 2024)."

## Directory Structure

The repo includes:
- **config/** - Constants, sweep grids, dataset lists, and anchor methods
- **data/input/** - Benchmark response files
- **data/output/** - Experiment results directory
- **src/calibration.py** - Handles "anchor selection" and "fixed-anchor calibration"

## Key Focus Areas

The project implements "Fixed Parameter Calibration" using anchor items. The README notes: "uses anchor items to calibrate new benchmarks to the evaluation suite while holding previously calibrated item parameters fixed."

## Notable Gaps

The provided content **does not explicitly mention**:
- Specific anchor item lists or IDs
- CSV/JSON/TSV formatted data files
- Contamination flags or labels
- DIF (Differential Item Functioning) discussions
- Detailed MMLU-specific data structure

The repository appears designed for reproducible benchmark calibration, with actual benchmark response files stored in pickle format rather than human-readable data formats.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_plan_036_growing_pains_lookup_20260521T160331",
  "tool": "WebFetch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-21T16:05:53.275460+00:00_

# Analysis of "Growing Pains" Paper

## 1) Anchor Item Selection Criteria

The paper uses **clustering-based selection**. They "select the most representative item from each cluster" after clustering IRT item representations. Importantly, they demonstrate that selecting high-discrimination items alone is insufficient—"clustering distributes anchors across the full difficulty and discrimination space" while naive top-K selection performs poorly.

## 2) Contamination Detection & DIF

**No mention** of contamination detection, differential item functioning (DIF), or item flagging procedures. This is a notable gap acknowledged in limitations: "anchors may become contaminated or saturated over time, requiring recalibration."

## 3) Specific Datasets Used

- **Open LLM Leaderboard**: ARC Challenge, GSM8K, HellaSwag, MMLU, TruthfulQA, Winogrande
- **MMLU**: All 57 subject subdomains treated as distinct datasets (from ~100-1,534 items per subject)
- **Total scope**: 395-428 models evaluated

## 4) Public Anchor Release

**Code availability stated**: "Code available at [https://github.com/eliyahabba/growing-pains/](https://github.com/eliyahabba/growing-pains/)" but the text does not explicitly confirm anchor item lists are published separately.

## 5) Item-Level Contamination/Data Leakage

**Not addressed**. The methodology assumes "anchor questions maintain stable statistical properties" but provides no contamination detection mechanisms.

## 6) Fixed Parameter Calibration Definition

FPC "holds anchor item parameters fixed and estimates only the parameters of newly introduced items," enabling "model abilities to retain consistent meaning across calibration steps."

## 7) Focal Point Contamination

**No mention** of this concept anywhere in the paper.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_plan_036_growing_pains_lookup_20260521T160331",
  "tool": "WebFetch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-21T16:05:53.275832+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://github.com/eliyahabba/growing-pains/tree/main/src",
  "prompt": "List all Python files in the src directory and any subdirectories. Look for files related to anchor selection, calibration, or MMLU data processing."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_plan_036_growing_pains_lookup_20260521T160331",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://github.com/eliyahabba/growing-pains/tree/main/src",
    "prompt": "List all Python files in the src directory and any subdirectories. Look for files related to anchor selection, calibration, or MMLU data processing."
  }
}
```

</details>

---

### Tool call

_source line 20 · 2026-05-21T16:05:53.276071+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://github.com/eliyahabba/growing-pains/tree/main/config",
  "prompt": "List all files in the config directory. Look for any configuration that specifies anchor items, item IDs, or MMLU subject lists."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_plan_036_growing_pains_lookup_20260521T160331",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://github.com/eliyahabba/growing-pains/tree/main/config",
    "prompt": "List all files in the config directory. Look for any configuration that specifies anchor items, item IDs, or MMLU subject lists."
  }
}
```

</details>

---

### Tool call

_source line 21 · 2026-05-21T16:05:53.276269+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://github.com/eliyahabba/growing-pains/tree/main/data",
  "prompt": "List all files in the data directory and any subdirectories. Look for any data files that contain item IDs, anchor item lists, or MMLU data."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_plan_036_growing_pains_lookup_20260521T160331",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://github.com/eliyahabba/growing-pains/tree/main/data",
    "prompt": "List all files in the data directory and any subdirectories. Look for any data files that contain item IDs, anchor item lists, or MMLU data."
  }
}
```

</details>

---

### Tool result

_source line 22 · 2026-05-21T16:05:53.276452+00:00_

# Python Files in growing-pains/src Directory

Based on the GitHub page content, the following Python files are visible in the src directory:

**Root level files:**
- `__init__.py`
- `calibration.py`
- `chain_experiment.py`
- `cleanup.py`
- `data_loading.py`
- `evaluation.py`
- `io.py`

**Subdirectory:**
- `irt/` (folder containing additional modules)

**Files relevant to your search:**

The `calibration.py` file appears directly related to calibration tasks. The `data_loading.py` module likely handles dataset ingestion, which could include MMLU data processing. The page indicates "View all files" is available, suggesting additional files exist that aren't fully enumerated in this view.

The `irt/` subdirectory may contain Item Response Theory implementations, potentially including anchor selection mechanisms, though specific file names within that folder aren't displayed in the provided content.

To see the complete file listing and examine specific implementations, you would need to navigate the full repository structure on GitHub.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_plan_036_growing_pains_lookup_20260521T160331",
  "tool": "WebFetch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 23 · 2026-05-21T16:05:53.276637+00:00_

# Files in the Config Directory

Based on the GitHub page content provided, the config directory contains the following files:

1. `__init__.py`
2. `constants.py`
3. `data_source_config.json`
4. `data_sources.py`
5. `experiment_presets.yaml`

However, **the actual content of these files is not visible** in the web page excerpt provided. The page only displays the file directory listing without showing the internal configuration details.

To find specifications regarding anchor items, item IDs, or MMLU subject lists, you would need to:
- Open each configuration file individually
- Review `data_source_config.json` (likely contains data source specifications)
- Check `experiment_presets.yaml` (possibly contains experiment-related settings)
- Examine `constants.py` (may define configuration constants)

The current view shows only the file structure, not the configuration contents themselves.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_plan_036_growing_pains_lookup_20260521T160331",
  "tool": "WebFetch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 24 · 2026-05-21T16:05:53.276842+00:00_

# Data Directory Contents

Based on the GitHub page for the "growing-pains" repository, the `/data` directory contains two subdirectories:

1. **input** - Location for source/input data files
2. **output** - Location for processed/output data files

However, the page does not display the specific files within these subdirectories. To see the actual data files (such as item IDs, anchor item lists, or MMLU data), you would need to navigate into each subdirectory or view the repository's file tree in more detail.

The page shown is a directory listing view that only reveals the folder structure, not the individual file contents or names within those folders.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_plan_036_growing_pains_lookup_20260521T160331",
  "tool": "WebFetch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 25 · 2026-05-21T16:05:53.277045+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://github.com/eliyahabba/growing-pains/blob/main/src/calibration.py",
  "prompt": "Read the full code. Focus on: 1) How are anchor items selected? Is there a fixed list or are they computed dynamically? 2) Are anchor item indices/IDs saved to a file? 3) What format are items identified by (index, ID, name)? 4) Is there any function that outputs or saves anchor items?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_plan_036_growing_pains_lookup_20260521T160331",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://github.com/eliyahabba/growing-pains/blob/main/src/calibration.py",
    "prompt": "Read the full code. Focus on: 1) How are anchor items selected? Is there a fixed list or are they computed dynamically? 2) Are anchor item indices/IDs saved to a file? 3) What format are items identified by (index, ID, name)? 4) Is there any function that outputs or saves anchor items?"
  }
}
```

</details>

---

### Tool call

_source line 26 · 2026-05-21T16:05:53.277215+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://github.com/eliyahabba/growing-pains/tree/main/data/input",
  "prompt": "List all files in the data/input directory. Are there pickle files, CSVs, or other data files? What are their names?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_plan_036_growing_pains_lookup_20260521T160331",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://github.com/eliyahabba/growing-pains/tree/main/data/input",
    "prompt": "List all files in the data/input directory. Are there pickle files, CSVs, or other data files? What are their names?"
  }
}
```

</details>

---

### Tool result

_source line 27 · 2026-05-21T16:05:53.277383+00:00_

# Files in data/input Directory

Based on the GitHub repository page, the data/input directory contains:

1. **README.md** - Documentation file
2. **lb.pickle** - Open LLM Leaderboard data (395 models, 6 datasets)
3. **mmlu_fields.pickle** - MMLU subjects data (428 models, 57 subjects)

The directory contains pickle files rather than CSVs or other formats. According to the documentation, "The item-level response data is from Polo et al. (2024b), 'tinyBenchmarks: evaluating LLMs with fewer examples' (ICML 2024)."

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_plan_036_growing_pains_lookup_20260521T160331",
  "tool": "WebFetch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 28 · 2026-05-21T16:05:53.277556+00:00_

# Anchor Item Selection Analysis

## 1. Selection Method
Anchor items are **computed dynamically**, not from a fixed list. The code offers multiple selection strategies:

- **Top-k discrimination**: Uses `find_anchor_items_top_k_discrimination()` to select items with highest discrimination values
- **IRT clustering**: Employs `find_anchor_items_clustering()` for clustering-based selection, optionally using correctness matrices from training data

Selection occurs per-dataset, with a configurable number of anchors (`n_anchors_per_dataset`).

## 2. File Persistence
There is **no explicit function that saves anchor item selections** to disk. The code caches IRT parameters (in `item_params.parquet`), but anchor IDs themselves are returned as in-memory lists without dedicated persistence.

## 3. Item Identification Format
Items are identified by **string IDs** (`item_id`). The code references "question_id" throughout, treating them as string-based identifiers that map to index positions when needed.

## 4. Output Functions
The `build_anchor_items_for_fixed_calibration()` function constructs anchor dictionaries containing:
- Item ID and difficulty/discrimination parameters
- Support for multi-dimensional IRT (vectors) via `discrimination_vector` and `difficulty_vector`

However, this returns a list without automatic file serialization. Callers must handle saving if needed.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_plan_036_growing_pains_lookup_20260521T160331",
  "tool": "WebFetch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 29 · 2026-05-21T16:05:53.277804+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "mkdir -p /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_036_growing_pains",
  "description": "Create output directory for plan_036"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_plan_036_growing_pains_lookup_20260521T160331",
  "tool": "Bash",
  "tool_args": {
    "command": "mkdir -p /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_036_growing_pains",
    "description": "Create output directory for plan_036"
  }
}
```

</details>

---

### Tool result

_source line 30 · 2026-05-21T16:05:53.277995+00:00_

(Bash completed with no output)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_plan_036_growing_pains_lookup_20260521T160331",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 31 · 2026-05-21T16:05:53.278191+00:00_

called Write

<details open><summary>🔧 Tool call — Write</summary>

````json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_036_growing_pains/plan_036_report.md",
  "content": "# Plan 036: Growing Pains LLM Benchmark — FPC Anchor Item Overlap Analysis\n\n**Date**: 2026-05-21\n**Status**: Data not available for overlap analysis\n\n---\n\n## Paper Information\n\n| Field | Value |\n|-------|-------|\n| **Title** | Growing Pains: Extensible and Efficient LLM Benchmarking Via Fixed Parameter Calibration |\n| **Authors** | Eliya Habba, Itay Itzhak, Asaf Yehudai, Yotam Perlitz, Elron Bandel, Michal Shmueli-Scheuer, Leshem Choshen, Gabriel Stanovsky |\n| **Venue** | arXiv preprint (April 2026) |\n| **arXiv** | [2604.12843](https://arxiv.org/abs/2604.12843) |\n| **Code** | [github.com/eliyahabba/growing-pains](https://github.com/eliyahabba/growing-pains) |\n\n## Key Clarification: FPC ≠ Focal Point Contamination\n\n**FPC in this paper stands for \"Fixed Parameter Calibration\"**, not \"Focal Point Contamination.\" The paper does not perform contamination detection, DIF analysis, or item flagging. The term \"Focal Point Contamination\" does not appear in the paper or in related LLM benchmark literature found during search.\n\n## What the Paper Actually Does\n\nThe paper proposes an IRT-based framework for efficient LLM benchmarking:\n\n1. **Anchor items** are selected per dataset (100 per dataset) via clustering-based methods on IRT item parameters (difficulty + discrimination).\n2. New models only need to be evaluated on anchor items; full-benchmark scores are inferred via calibrated IRT parameters.\n3. New datasets are calibrated into an existing evaluation suite using Fixed Parameter Calibration (holding prior item parameters fixed).\n4. Evaluated on Open LLM Leaderboard (6 datasets, 395 models) and MMLU (57 subjects, 428 models).\n5. Achieves predictions within 2–3 pp of full evaluation, Spearman ρ ≥ 0.9.\n\n## Data Availability Assessment\n\n| Component | Status |\n|-----------|--------|\n| Code repository | Public (GitHub) |\n| Item response data | Public (pickle files from tinyBenchmarks, Polo et al. 2024) |\n| Anchor item IDs | **Not public** — computed dynamically at runtime, not persisted as a fixed list |\n| Contamination flags | **Does not exist** — paper does not detect contamination |\n| DIF / item flagging | **Does not exist** — not part of the methodology |\n\n## Why Overlap Analysis Cannot Be Performed\n\nThe specified Jaccard / enrichment / Fisher exact test analysis requires a set of items flagged as contaminated by an external method. This paper provides neither:\n\n- **No contamination detection**: FPC anchors are selected for statistical stability (high discrimination, representative of difficulty space), not for contamination status.\n- **No fixed anchor list**: Anchors are computed dynamically based on clustering — different random seeds or configurations yield different anchor sets.\n- **Conceptual mismatch**: FPC anchors are items chosen to be *stable calibration references*. If anything, they should be *anti-correlated* with contaminated items (the paper notes \"anchors may become contaminated or saturated over time, requiring recalibration\" as a limitation).\n\n## Relevance to Our Work\n\nDespite the mismatch, the paper is relevant to cite in our work for two reasons:\n\n1. **Shared IRT foundation**: Both our method and theirs use IRT on LLM benchmark data. Their work validates that IRT-based item analysis is viable at scale (400+ models, 57 MMLU subjects).\n2. **Contamination as acknowledged threat**: The paper explicitly acknowledges (in Limitations) that anchor items may become contaminated over time — this supports our argument that item-level contamination analysis (via DIF) is a necessary complement to IRT-based benchmarking.\n\n## Suggested Citation\n\n```bibtex\n@article{habba2026growing,\n  title={Growing Pains: Extensible and Efficient {LLM} Benchmarking Via Fixed Parameter Calibration},\n  author={Habba, Eliya and Itzhak, Itay and Yehudai, Asaf and Perlitz, Yotam and Bandel, Elron and Shmueli-Scheuer, Michal and Choshen, Leshem and Stanovsky, Gabriel},\n  journal={arXiv preprint arXiv:2604.12843},\n  year={2026}\n}\n```\n"
}
````

</details>

<details><summary>Recorded metadata</summary>

````json
{
  "recorded_role": "tool",
  "session": "worker_research_plan_036_growing_pains_lookup_20260521T160331",
  "tool": "Write",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_036_growing_pains/plan_036_report.md",
    "content": "# Plan 036: Growing Pains LLM Benchmark — FPC Anchor Item Overlap Analysis\n\n**Date**: 2026-05-21\n**Status**: Data not available for overlap analysis\n\n---\n\n## Paper Information\n\n| Field | Value |\n|-------|-------|\n| **Title** | Growing Pains: Extensible and Efficient LLM Benchmarking Via Fixed Parameter Calibration |\n| **Authors** | Eliya Habba, Itay Itzhak, Asaf Yehudai, Yotam Perlitz, Elron Bandel, Michal Shmueli-Scheuer, Leshem Choshen, Gabriel Stanovsky |\n| **Venue** | arXiv preprint (April 2026) |\n| **arXiv** | [2604.12843](https://arxiv.org/abs/2604.12843) |\n| **Code** | [github.com/eliyahabba/growing-pains](https://github.com/eliyahabba/growing-pains) |\n\n## Key Clarification: FPC ≠ Focal Point Contamination\n\n**FPC in this paper stands for \"Fixed Parameter Calibration\"**, not \"Focal Point Contamination.\" The paper does not perform contamination detection, DIF analysis, or item flagging. The term \"Focal Point Contamination\" does not appear in the paper or in related LLM benchmark literature found during search.\n\n## What the Paper Actually Does\n\nThe paper proposes an IRT-based framework for efficient LLM benchmarking:\n\n1. **Anchor items** are selected per dataset (100 per dataset) via clustering-based methods on IRT item parameters (difficulty + discrimination).\n2. New models only need to be evaluated on anchor items; full-benchmark scores are inferred via calibrated IRT parameters.\n3. New datasets are calibrated into an existing evaluation suite using Fixed Parameter Calibration (holding prior item parameters fixed).\n4. Evaluated on Open LLM Leaderboard (6 datasets, 395 models) and MMLU (57 subjects, 428 models).\n5. Achieves predictions within 2–3 pp of full evaluation, Spearman ρ ≥ 0.9.\n\n## Data Availability Assessment\n\n| Component | Status |\n|-----------|--------|\n| Code repository | Public (GitHub) |\n| Item response data | Public (pickle files from tinyBenchmarks, Polo et al. 2024) |\n| Anchor item IDs | **Not public** — computed dynamically at runtime, not persisted as a fixed list |\n| Contamination flags | **Does not exist** — paper does not detect contamination |\n| DIF / item flagging | **Does not exist** — not part of the methodology |\n\n## Why Overlap Analysis Cannot Be Performed\n\nThe specified Jaccard / enrichment / Fisher exact test analysis requires a set of items flagged as contaminated by an external method. This paper provides neither:\n\n- **No contamination detection**: FPC anchors are selected for statistical stability (high discrimination, representative of difficulty space), not for contamination status.\n- **No fixed anchor list**: Anchors are computed dynamically based on clustering — different random seeds or configurations yield different anchor sets.\n- **Conceptual mismatch**: FPC anchors are items chosen to be *stable calibration references*. If anything, they should be *anti-correlated* with contaminated items (the paper notes \"anchors may become contaminated or saturated over time, requiring recalibration\" as a limitation).\n\n## Relevance to Our Work\n\nDespite the mismatch, the paper is relevant to cite in our work for two reasons:\n\n1. **Shared IRT foundation**: Both our method and theirs use IRT on LLM benchmark data. Their work validates that IRT-based item analysis is viable at scale (400+ models, 57 MMLU subjects).\n2. **Contamination as acknowledged threat**: The paper explicitly acknowledges (in Limitations) that anchor items may become contaminated over time — this supports our argument that item-level contamination analysis (via DIF) is a necessary complement to IRT-based benchmarking.\n\n## Suggested Citation\n\n```bibtex\n@article{habba2026growing,\n  title={Growing Pains: Extensible and Efficient {LLM} Benchmarking Via Fixed Parameter Calibration},\n  author={Habba, Eliya and Itzhak, Itay and Yehudai, Asaf and Perlitz, Yotam and Bandel, Elron and Shmueli-Scheuer, Michal and Choshen, Leshem and Stanovsky, Gabriel},\n  journal={arXiv preprint arXiv:2604.12843},\n  year={2026}\n}\n```\n"
  }
}
````

</details>

---

### Tool result

_source line 32 · 2026-05-21T16:05:53.278438+00:00_

File created successfully at: /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_036_growing_pains/plan_036_report.md

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_plan_036_growing_pains_lookup_20260521T160331",
  "tool": "Write",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 33 · 2026-05-21T16:05:53.278778+00:00_

报告已写入 `artifacts/plan_036_growing_pains/plan_036_report.md`。

## 结论

**"Growing Pains"** 论文（Habba et al., arXiv 2604.12843, 2026.04）的 FPC 是 **Fixed Parameter Calibration**，不是 Focal Point Contamination。论文用 IRT anchor items 做高效 benchmark 校准，**不涉及污染检测**，也没有公开的 contamination flag list。因此无法执行 Jaccard overlap 分析。

与我们工作的关联：
- 共享 IRT 基础，验证了 IRT 在 400+ 模型、57 个 MMLU subjects 上的可行性
- 论文在 Limitations 中承认 anchor items 可能随时间被污染——直接支持我们 DIF-based contamination detection 的必要性论点
- 适合在 Related Work 中引用

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_research_plan_036_growing_pains_lookup_20260521T160331"
}
```

</details>

---
