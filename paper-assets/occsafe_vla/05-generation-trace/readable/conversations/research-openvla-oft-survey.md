# research openvla oft survey

**Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Factorial Analysis** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 267
- **Recorded user turns:** 0
- **Tool calls:** 133
- **Original source:** `logs/chats/worker_research_openvla-oft-survey_20260520T040517.jsonl`
- **Structured JSON:** [`420822e5f481a7a5d4bc.json`](../../sessions/42/420822e5f481a7a5d4bc.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

267 recorded events

### Tool call

_source line 1 · 2026-05-20T04:19:56.337914+00:00_

called Agent

<details open><summary>🔧 Tool call — Agent</summary>

```json
{
  "description": "Search OpenVLA-OFT repos",
  "subagent_type": "general-purpose",
  "prompt": "Search for OpenVLA and OpenVLA-OFT repositories on GitHub and gather detailed information. I need:\n\n1. The official OpenVLA repo (from UC Berkeley / openvla org) - get star count, license, last commit date, activity\n2. The OpenVLA-OFT variant repo - this might be a separate repo or a branch. OFT stands for \"Orthogonal Fine-Tuning\" or possibly \"Open Fine-Tuning\". Search for repos matching \"openvla-oft\", \"openvla oft\", etc.\n3. Check if OFT is part of the main openvla repo as a branch or directory\n\nUse WebSearch to find these repos, then use WebFetch to get details from the GitHub pages.\n\nAlso search for:\n- Any papers related to OpenVLA-OFT (arxiv)\n- Any third-party repos that combine OpenVLA with LIBERO or SafeLIBERO\n\nReport all URLs, star counts, licenses, and activity information you find."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_openvla-oft-survey_20260520T040517",
  "tool": "Agent",
  "tool_args": {
    "description": "Search OpenVLA-OFT repos",
    "subagent_type": "general-purpose",
    "prompt": "Search for OpenVLA and OpenVLA-OFT repositories on GitHub and gather detailed information. I need:\n\n1. The official OpenVLA repo (from UC Berkeley / openvla org) - get star count, license, last commit date, activity\n2. The OpenVLA-OFT variant repo - this might be a separate repo or a branch. OFT stands for \"Orthogonal Fine-Tuning\" or possibly \"Open Fine-Tuning\". Search for repos matching \"openvla-oft\", \"openvla oft\", etc.\n3. Check if OFT is part of the main openvla repo as a branch or directory\n\nUse WebSearch to find these repos, then use WebFetch to get details from the GitHub pages.\n\nAlso search for:\n- Any papers related to OpenVLA-OFT (arxiv)\n- Any third-party repos that combine OpenVLA with LIBERO or SafeLIBERO\n\nReport all URLs, star counts, licenses, and activity information you find."
  }
}
```

</details>

---

### Tool call

_source line 2 · 2026-05-20T04:19:56.338274+00:00_

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
  "session": "worker_research_openvla-oft-survey_20260520T040517",
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

_source line 3 · 2026-05-20T04:19:56.338438+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_openvla-oft-survey_20260520T040517",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 4 · 2026-05-20T04:19:56.338577+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "OpenVLA GitHub repository openvla UC Berkeley stars"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_openvla-oft-survey_20260520T040517",
  "tool": "WebSearch",
  "tool_args": {
    "query": "OpenVLA GitHub repository openvla UC Berkeley stars"
  }
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-20T04:19:56.338748+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "OpenVLA-OFT GitHub repository \"openvla-oft\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_openvla-oft-survey_20260520T040517",
  "tool": "WebSearch",
  "tool_args": {
    "query": "OpenVLA-OFT GitHub repository \"openvla-oft\""
  }
}
```

</details>

---

### Tool call

_source line 6 · 2026-05-20T04:19:56.338893+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "OpenVLA OFT paper arxiv 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_openvla-oft-survey_20260520T040517",
  "tool": "WebSearch",
  "tool_args": {
    "query": "OpenVLA OFT paper arxiv 2026"
  }
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-20T04:19:56.339033+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "OpenVLA LIBERO SafeLIBERO GitHub repository"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_openvla-oft-survey_20260520T040517",
  "tool": "WebSearch",
  "tool_args": {
    "query": "OpenVLA LIBERO SafeLIBERO GitHub repository"
  }
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-20T04:19:56.339169+00:00_

Web search results for query: "OpenVLA GitHub repository openvla UC Berkeley stars"

Links: [{"title":"OpenVLA: An Open-Source Vision-Language-Action Model","url":"https://openvla.github.io/"},{"title":"GitHub - rail-berkeley/tensorrt-openvla · GitHub","url":"https://github.com/rail-berkeley/tensorrt-openvla"},{"title":"openvla/openvla-7b · Hugging Face","url":"https://huggingface.co/openvla/openvla-7b"},{"title":"openvla.github.io/index.html at main · openvla/openvla.github.io","url":"https://github.com/openvla/openvla.github.io/blob/main/index.html"},{"title":"openvla/openvla-v01-7b · Hugging Face","url":"https://huggingface.co/openvla/openvla-v01-7b"},{"title":"moritzknaust/openvla-7b · Hugging Face","url":"https://huggingface.co/moritzknaust/openvla-7b"},{"title":"OpenVLA: An Open-Source Vision-Language-Action Model","url":"https://arxiv.org/html/2406.09246v3"},{"title":"tt1225/openvla-7b-devel · Hugging Face","url":"https://huggingface.co/tt1225/openvla-7b-devel"},{"title":"GitHub - openvla/openvla: OpenVLA: An open-source vision-language-action model for robotic manipulation. · GitHub","url":"https://github.com/openvla/openvla"},{"title":"uc-berkeley · GitHub Topics · GitHub","url":"https://github.com/topics/uc-berkeley?o=asc&s=stars"}]

Based on the search results, here's what I found about OpenVLA:

## Overview
OpenVLA is an open-source vision-language-action model for robotic manipulation. The OpenVLA team consists of researchers from Stanford, UC Berkeley, Google Deepmind, and the Toyota Research Institute.

## GitHub Repository
The main GitHub repository is available at: **https://github.com/openvla/openvla**

The model was trained on a dataset of 970k robot manipulation trajectories from the Open X-Embodiment (OpenX) dataset.

## Star Count
Unfortunately, the search results don't include the specific GitHub star count for the OpenVLA repository. The search results focus on the project's technical details, research papers, and Hugging Face model pages rat
…[truncated 253 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_openvla-oft-survey_20260520T040517",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 9 · 2026-05-20T04:19:56.339336+00:00_

Web search results for query: "OpenVLA OFT paper arxiv 2026"

Links: [{"title":"Fine-Tuning Vision-Language-Action Models: Optimizing Speed and Success","url":"https://arxiv.org/pdf/2502.19645"},{"title":"Fine-Tuning Vision-Language-Action Models: Optimizing Speed and Success","url":"https://arxiv.org/html/2502.19645v1"},{"title":"[2603.16044] Enhancing Linguistic Generalization of VLA: Fine-Tuning OpenVLA via Synthetic Instruction Augmentation","url":"https://arxiv.org/abs/2603.16044"},{"title":"Enhancing Linguistic Generalization of VLA: Fine-Tuning OpenVLA via Synthetic Instruction Augmentation","url":"https://arxiv.org/pdf/2603.16044"},{"title":"OpenVLA-OFT","url":"https://openvla-oft.github.io/"},{"title":"Experiences from Benchmarking Vision–Language–Action Models for Robotic Manipulation","url":"https://arxiv.org/html/2511.11298v1"},{"title":"[2502.19645] Fine-Tuning Vision-Language-Action Models: Optimizing Speed and Success","url":"https://arxiv.org/abs/2502.19645"}]

I found the paper you're looking for! Here are the key details:

**Title:** Fine-Tuning Vision-Language-Action Models: Optimizing Speed and Success

**ArXiv ID:** 2502.19645

**Main Contribution:** OpenVLA-OFT sets a new state of the art on the LIBERO simulation benchmark, significantly boosting OpenVLA's average success rate across four task suites from 76.5% to 97.1% while increasing action generation throughput by 26×.

**Key Method:** The Optimized Fine-Tuning (OFT) recipe integrates parallel decoding, action chunking, a continuous action representation, and a simple L1 regression-based learning objective to altogether improve inference efficiency, policy performance, and flexibility in the model's input-output specifications.

**Real-World Validation:** In real-world evaluations, the fine-tuning recipe enables OpenVLA to successfully execute dexterous, high-frequency control tasks on a bimanual ALOHA robot and outperform other VLAs by up to 15% in average success rate.

The paper is avail
…[truncated 153 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_openvla-oft-survey_20260520T040517",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-20T04:19:56.339493+00:00_

Web search results for query: "OpenVLA-OFT GitHub repository "openvla-oft""

Links: [{"title":"OpenVLA · OFT | Konnex Docs","url":"https://docs.konnex.world/supported-ai-models/openvla-oft"},{"title":"Open-source OpenVLA-7B-OFT optimized visual-language-action model, specifically designed to improve the execution speed and success rate of robot tasks","url":"https://model.aibase.com/models/details/1935154868323094528"},{"title":"The OpenVLA-OFT Vision-Language-Action Model is open-sourced! Fine-tuning optimization enhances speed and success rate.","url":"https://model.aibase.com/models/details/1935154868167905280"},{"title":"openvla-oft/README.md at main · moojink/openvla-oft","url":"https://github.com/moojink/openvla-oft/blob/main/README.md"},{"title":"GitHub - moojink/openvla-oft: Fine-Tuning Vision-Language-Action Models: Optimizing Speed and Success · GitHub","url":"https://github.com/moojink/openvla-oft"},{"title":"GitHub - siyuhsu/vla-cache: [NeurIPS 2025] VLA-Cache: Efficient Vision-Language-Action Manipulation via Adaptive Token Caching · GitHub","url":"https://github.com/siyuhsu/vla-cache"},{"title":"moojink/openvla-7b-oft-finetuned-libero-object · Hugging Face","url":"https://huggingface.co/moojink/openvla-7b-oft-finetuned-libero-object"},{"title":"OpenVLA-OFT","url":"https://openvla-oft.github.io/"},{"title":"GitHub - openvla/openvla: OpenVLA: An open-source vision-language-action model for robotic manipulation. · GitHub","url":"https://github.com/openvla/openvla"}]

Based on the search results, here's information about the OpenVLA-OFT GitHub repository:

## Overview

OpenVLA-OFT is a set of methods and code for parameter-efficient fine-tuning (OFT = Orthogonal/Offset Fine-Tuning) on top of the base OpenVLA 7B model, with the goal to cheaply adapt the same model to new domains/tasks by training small add-on parameterizations instead of touching all weights.

## Repository Contents

The openvla-oft repository contains training scripts, evaluation scripts o
…[truncated 769 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_openvla-oft-survey_20260520T040517",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 11 · 2026-05-20T04:19:56.339648+00:00_

Web search results for query: "OpenVLA LIBERO SafeLIBERO GitHub repository"

Links: [{"title":"GitHub - openvla/openvla: OpenVLA: An open-source vision-language-action model for robotic manipulation. · GitHub","url":"https://github.com/openvla/openvla"},{"title":"GitHub - Zxy-MLlab/LIBERO-PRO: LIBERO-PRO is the official repository of the LIBERO-PRO — an evaluation extension of the original LIBERO benchmark","url":"https://github.com/Zxy-MLlab/LIBERO-PRO"},{"title":"GitHub - sylvestf/LIBERO-plus: Official repository of LIBERO-plus, a generalized benchmark for in-depth robustness analysis of vision-language-action models. · GitHub","url":"https://github.com/sylvestf/LIBERO-plus"},{"title":"THURCSCT/SafeLIBERO · Datasets at Hugging Face","url":"https://huggingface.co/datasets/THURCSCT/SafeLIBERO"},{"title":"openvla/experiments/robot/libero/regenerate_libero_dataset.py at main · openvla/openvla","url":"https://github.com/openvla/openvla/blob/main/experiments/robot/libero/regenerate_libero_dataset.py"},{"title":"LIBERO Environment · Issue #199 · openvla/openvla","url":"https://github.com/openvla/openvla/issues/199"}]

Based on the search results, here's what I found about OpenVLA, LIBERO, and SafeLIBERO:

## OpenVLA GitHub Repository

OpenVLA was fine-tuned via LoRA on four LIBERO task suites independently: LIBERO-Spatial, LIBERO-Object, LIBERO-Goal, and LIBERO-10 (also called LIBERO-Long). The main OpenVLA repository is available at https://github.com/openvla/openvla, which is an open-source vision-language-action model for robotic manipulation.

## LIBERO Benchmark

The search results show several LIBERO-related repositories:
- **LIBERO-PRO**: A reference code snippet for conducting LIBERO-PRO generalization evaluation on OpenVLA is available at https://github.com/Zxy-MLlab/LIBERO-PRO
- **LIBERO-plus**: Available at https://github.com/sylvestf/LIBERO-plus, a generalized benchmark for in-depth robustness analysis of vision-language-action models that contains the offici
…[truncated 477 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_openvla-oft-survey_20260520T040517",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 12 · 2026-05-20T04:19:56.339826+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://github.com/openvla/openvla",
  "prompt": "Extract: star count, fork count, license, last commit date, number of contributors, programming language breakdown, description, and any mention of OFT or branches. Also note the topics/tags."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_openvla-oft-survey_20260520T040517",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://github.com/openvla/openvla",
    "prompt": "Extract: star count, fork count, license, last commit date, number of contributors, programming language breakdown, description, and any mention of OFT or branches. Also note the topics/tags."
  }
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-20T04:19:56.339959+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://github.com/moojink/openvla-oft",
  "prompt": "Extract: star count, fork count, license, last commit date, number of contributors, programming language breakdown, description, README summary including key features and LIBERO results. Note any mention of SafeLIBERO."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_openvla-oft-survey_20260520T040517",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://github.com/moojink/openvla-oft",
    "prompt": "Extract: star count, fork count, license, last commit date, number of contributors, programming language breakdown, description, README summary including key features and LIBERO results. Note any mention of SafeLIBERO."
  }
}
```

</details>

---

### Tool call

_source line 14 · 2026-05-20T04:19:56.340092+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://arxiv.org/abs/2502.19645",
  "prompt": "Extract: full paper title, all authors and their affiliations, submission date, abstract, and key results/numbers mentioned."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_openvla-oft-survey_20260520T040517",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://arxiv.org/abs/2502.19645",
    "prompt": "Extract: full paper title, all authors and their affiliations, submission date, abstract, and key results/numbers mentioned."
  }
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-20T04:19:56.340222+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "SafeLIBERO paper arxiv safety VLA benchmark THURCSCT"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_openvla-oft-survey_20260520T040517",
  "tool": "WebSearch",
  "tool_args": {
    "query": "SafeLIBERO paper arxiv safety VLA benchmark THURCSCT"
  }
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-20T04:19:56.340342+00:00_

# OpenVLA Repository Analysis

**Star Count:** 6.2k stars

**Fork Count:** 734 forks

**License:** MIT License

**Programming Language Breakdown:** Python 99.9%, Makefile 0.1%

**Description:** "An open-source vision-language-action model for robotic manipulation" that enables training and fine-tuning models for generalist robot control across different datasets and embodiments.

**Last Commit Date:** Not explicitly stated in the provided content

**Number of Contributors:** Not displayed (page indicated "Uh oh! There was an error while loading")

**OFT Mention:** Yes - prominently featured in latest updates. The March 3, 2025 entry highlights the Optimized Fine-Tuning recipe, noting it "enables 25-50x faster inference speed, higher task success rates, multiple input images, and high-frequency bimanual robot control."

**Branches:** The repository shows a main branch with 63 commits; specific branch names beyond "main" are not detailed in the content provided.

**Topics/Tags:** The repository uses standard GitHub badges including arXiv, HuggingFace Models, PyTorch, and Python version indicators, though explicit topic tags aren't listed in the extracted content.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_openvla-oft-survey_20260520T040517",
  "tool": "WebFetch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 17 · 2026-05-20T04:19:56.340466+00:00_

# OpenVLA-OFT Repository Analysis

**Star Count:** 1.2k

**Fork Count:** 169

**License:** MIT

**Programming Language:** Python (100%)

**Last Commit Date:** Not explicitly displayed in the provided content

**Number of Contributors:** Data load error prevented retrieval

**Description:** The repository focuses on "Fine-Tuning Vision-Language-Action Models: Optimizing Speed and Success," addressing efficient adaptation of VLA systems for robotics tasks.

## README Summary

**Key Features:**
- Support for both simulation (LIBERO) and real-world (ALOHA robot) environments
- Uses vision-language models combined with action prediction heads
- Incorporates proprioceptive projectors mapping robot state to embedding space
- Flexible inference supporting L1 regression and diffusion-based action generation

**System Requirements:**
- Inference: 16-18 GB VRAM per GPU
- Training: 1-8 GPUs (27-80 GB VRAM depending on configuration)

**Notable Elements:**
The project includes "sample LIBERO spatial observation" data and references "moojink/openvla-7b-oft-finetuned-libero-spatial" checkpoint. However, the content provided contains no explicit mention of SafeLIBERO.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_openvla-oft-survey_20260520T040517",
  "tool": "WebFetch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-20T04:19:56.340592+00:00_

# Paper Summary

**Full Title:** Fine-Tuning Vision-Language-Action Models: Optimizing Speed and Success

**Authors & Affiliations:**
- Moo Jin Kim
- Chelsea Finn
- Percy Liang

(Specific institutional affiliations are not provided in the webpage content)

**Submission Date:** February 27, 2025 (v1); revised April 28, 2025 (v2)

**Abstract Summary:**
The researchers investigate optimal fine-tuning strategies for vision-language-action models, specifically studying OpenVLA. They developed an "Optimized Fine-Tuning (OFT)" recipe combining parallel decoding, action chunking, continuous action representation, and L1 regression-based learning objectives.

**Key Results:**
- **LIBERO benchmark:** Success rate improved from 76.5% to 97.1%
- **Throughput:** Action generation speed increased by "26$\\times$" (26 times)
- **Real-world performance:** Successfully executed bimanual ALOHA robot tasks, outperforming comparable models (π₀, RDT-1B) and traditional imitation learning approaches by up to 15 percentage points in success rate

**Additional Details:** The paper was accepted to Robotics: Science and Systems (RSS) 2025, with code and pretrained models released publicly.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_openvla-oft-survey_20260520T040517",
  "tool": "WebFetch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 19 · 2026-05-20T04:19:56.340759+00:00_

Web search results for query: "SafeLIBERO paper arxiv safety VLA benchmark THURCSCT"

Links: [{"title":"THURCSCT/SafeLIBERO · Datasets at Hugging Face","url":"https://huggingface.co/datasets/THURCSCT/SafeLIBERO"},{"title":"Update · THURCSCT/SafeLIBERO at c2f47cf","url":"https://huggingface.co/datasets/THURCSCT/SafeLIBERO/commit/c2f47cf855082a7e94de4edf1749ee766737ad1b"},{"title":"[2512.11891] VLSA: Vision-Language-Action Models with Plug-and-Play Safety Constraint Layer","url":"https://arxiv.org/abs/2512.11891"},{"title":"Concept-Based Dictionary Learning for Inference-Time Safety in Vision Language Action Models","url":"https://arxiv.org/pdf/2602.01834"},{"title":"VLSA: Vision-Language-Action Models with Plug-and-Play Safety Constraint Layer","url":"https://arxiv.org/pdf/2512.11891"},{"title":"VLSA: Vision-Language-Action Models with Plug-and-Play Safety Constraint Layer [Quick Review]","url":"https://liner.com/review/vlsa-visionlanguageaction-models-with-plugandplay-safety-constraint-layer"},{"title":"VLSA: Vision-Language-Action Models with Plug-and-Play Safety Constraint Layer","url":"https://arxiv.org/html/2512.11891v1"},{"title":"SafeLIBERO - Physical AI Dataset | Claru","url":"https://claru.ai/datasets/thurcsct-safelibero"},{"title":"SafeLIBERO Benchmark Details","url":"https://vlsa-aegis.github.io/benchmark.html"},{"title":"Overview of the SafeLIBERO benchmark tasks. | Download Scientific Diagram","url":"https://www.researchgate.net/figure/Overview-of-the-SafeLIBERO-benchmark-tasks_fig6_398721287"}]

Based on the search results, here's what I found about the SafeLIBERO paper and benchmark:

## Overview

The SafeLIBERO paper introduces a Vision-Language-Safe Action (VLSA) architecture named AEGIS, which contains a plug-and-play safety constraint layer formulated via control barrier functions that integrates directly with existing VLA models to improve safety with theoretical guarantees, while maintaining their original instruction-following performance.

## T
…[truncated 1019 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_openvla-oft-survey_20260520T040517",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 20 · 2026-05-20T04:19:56.340913+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://github.com/THU-RCSCT/vlsa-aegis",
  "prompt": "Extract: star count, fork count, license, last commit date, description, README summary, any mention of OpenVLA or LIBERO integration."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_openvla-oft-survey_20260520T040517",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://github.com/THU-RCSCT/vlsa-aegis",
    "prompt": "Extract: star count, fork count, license, last commit date, description, README summary, any mention of OpenVLA or LIBERO integration."
  }
}
```

</details>

---

### Tool call

_source line 21 · 2026-05-20T04:19:56.341043+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://arxiv.org/abs/2512.11891",
  "prompt": "Extract: full title, all authors and affiliations, submission date, abstract, key results. Note if OpenVLA is used as baseline."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_openvla-oft-survey_20260520T040517",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://arxiv.org/abs/2512.11891",
    "prompt": "Extract: full title, all authors and affiliations, submission date, abstract, key results. Note if OpenVLA is used as baseline."
  }
}
```

</details>

---

### Tool call

_source line 22 · 2026-05-20T04:19:56.341168+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "gh api repos/openvla/openvla --jq '{stars: .stargazers_count, forks: .forks_count, license: .license.spdx_id, pushed_at: .pushed_at, created_at: .created_at, default_branch: .default_branch, open_issues: .open_issues_count, description: .description, topics: .topics}' 2>/dev/null || echo \"gh api failed\"",
  "description": "Get openvla/openvla repo metadata via GitHub API"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_openvla-oft-survey_20260520T040517",
  "tool": "Bash",
  "tool_args": {
    "command": "gh api repos/openvla/openvla --jq '{stars: .stargazers_count, forks: .forks_count, license: .license.spdx_id, pushed_at: .pushed_at, created_at: .created_at, default_branch: .default_branch, open_issues: .open_issues_count, description: .description, topics: .topics}' 2>/dev/null || echo \"gh api failed\"",
    "description": "Get openvla/openvla repo metadata via GitHub API"
  }
}
```

</details>

---

### Tool call

_source line 23 · 2026-05-20T04:19:56.341299+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "gh api repos/moojink/openvla-oft --jq '{stars: .stargazers_count, forks: .forks_count, license: .license.spdx_id, pushed_at: .pushed_at, created_at: .created_at, default_branch: .default_branch, open_issues: .open_issues_count, description: .description, topics: .topics}' 2>/dev/null || echo \"gh api failed\"",
  "description": "Get moojink/openvla-oft repo metadata via GitHub API"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_openvla-oft-survey_20260520T040517",
  "tool": "Bash",
  "tool_args": {
    "command": "gh api repos/moojink/openvla-oft --jq '{stars: .stargazers_count, forks: .forks_count, license: .license.spdx_id, pushed_at: .pushed_at, created_at: .created_at, default_branch: .default_branch, open_issues: .open_issues_count, description: .description, topics: .topics}' 2>/dev/null || echo \"gh api failed\"",
    "description": "Get moojink/openvla-oft repo metadata via GitHub API"
  }
}
```

</details>

---

### Tool result

_source line 24 · 2026-05-20T04:19:56.341421+00:00_

# VLSA-AEGIS Repository Analysis

## Key Metrics
- **Star Count:** 98
- **Fork Count:** 13
- **License:** MIT
- **Last Commit Date:** Not explicitly shown; repository shows "116 Commits" on main branch

## Description
The project presents "A vision-language-safety action architecture, named AEGIS, which contains a plug-and-play safety constraint layer formulated via control barrier functions."

## README Summary
VLSA-AEGIS combines vision-language models with robotic safety constraints. The framework introduces AEGIS, which "bridges the gap between semantic instruction and physical safety" by using VLMs and depth data to enforce safety via Control Barrier Function-based optimization. The project includes SafeLIBERO, a benchmark with 1,600 evaluation episodes across 16 tasks designed to assess robot performance in safety-critical scenarios.

## Integration References

**LIBERO Integration:** The project explicitly builds upon LIBERO, acknowledging it in the Acknowledgment section. SafeLIBERO extends LIBERO's task suite with safety-level variants.

**OpenVLA/OpenPI Integration:** The codebase references "openpi" as a dependency and foundational work. The acknowledgments mention OpenPI (Physical Intelligence) as a project this work builds upon.

The framework evaluates against baseline VLA models, comparing safety and task success metrics across simulated manipulation tasks.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_openvla-oft-survey_20260520T040517",
  "tool": "WebFetch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 25 · 2026-05-20T04:19:56.341544+00:00_

# Paper Summary: VLSA

**Full Title:** "VLSA: Vision-Language-Action Models with Plug-and-Play Safety Constraint Layer"

**Authors:** Songqiao Hu, Zeyi Liu, Shuang Liu, Jun Cen, Zihan Meng, Xiao He

**Affiliations:** Not explicitly listed in the provided content.

**Submission Date:** December 9, 2025

**Abstract Summary:**
The research introduces AEGIS, a safety-enhanced architecture for robotic manipulation. The system integrates "a plug-and-play safety constraint (SC) layer formulated via control barrier functions" with existing Vision-Language-Action models to enable both task execution and collision prevention in unstructured environments.

**Key Results:**
- 59.16% improvement in obstacle avoidance rate
- 17.25% increase in task execution success rate
- Maintains original instruction-following performance

**SafeLIBERO Benchmark:** The authors developed a comprehensive safety-critical evaluation benchmark spanning multiple manipulation scenarios with varying spatial complexity.

**Code & Data:** Authors indicate public availability of code, models, and benchmark datasets.

**OpenVLA as Baseline:** No mention of OpenVLA was found in the provided content.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_openvla-oft-survey_20260520T040517",
  "tool": "WebFetch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 26 · 2026-05-20T04:19:56.341674+00:00_

gh api failed

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_openvla-oft-survey_20260520T040517",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 27 · 2026-05-20T04:19:56.341794+00:00_

gh api failed

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_openvla-oft-survey_20260520T040517",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 28 · 2026-05-20T04:19:56.341917+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "github.com/openvla/openvla branches OFT fine-tuning"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_openvla-oft-survey_20260520T040517",
  "tool": "WebSearch",
  "tool_args": {
    "query": "github.com/openvla/openvla branches OFT fine-tuning"
  }
}
```

</details>

---

### Tool call

_source line 29 · 2026-05-20T04:19:56.342041+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"openvla-oft\" authors \"Moo Jin Kim\" Stanford affiliation"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_openvla-oft-survey_20260520T040517",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"openvla-oft\" authors \"Moo Jin Kim\" Stanford affiliation"
  }
}
```

</details>

---

### Tool call

_source line 30 · 2026-05-20T04:19:56.342162+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://openvla-oft.github.io/",
  "prompt": "Extract: all authors, their affiliations, key claims, benchmark results (especially LIBERO success rates), any mention of SafeLIBERO, and real-world robot experiments."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_openvla-oft-survey_20260520T040517",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://openvla-oft.github.io/",
    "prompt": "Extract: all authors, their affiliations, key claims, benchmark results (especially LIBERO success rates), any mention of SafeLIBERO, and real-world robot experiments."
  }
}
```

</details>

---

### Tool call

_source line 31 · 2026-05-20T04:19:56.342284+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "site:github.com openvla LIBERO safety obstacle avoidance"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_openvla-oft-survey_20260520T040517",
  "tool": "WebSearch",
  "tool_args": {
    "query": "site:github.com openvla LIBERO safety obstacle avoidance"
  }
}
```

</details>

---

### Tool result

_source line 32 · 2026-05-20T04:19:56.342410+00:00_

Web search results for query: "github.com/openvla/openvla branches OFT fine-tuning"

Links: [{"title":"GitHub - hanbit-o/openvla-oft: Fine-Tuning Vision-Language-Action Models: Optimizing Speed and Success · GitHub","url":"https://github.com/hanbit-o/openvla-oft"},{"title":"GitHub - moojink/openvla-oft: Fine-Tuning Vision-Language-Action Models: Optimizing Speed and Success · GitHub","url":"https://github.com/moojink/openvla-oft"},{"title":"Fine-Tuning Vision-Language-Action Models: Optimizing Speed and Success","url":"https://arxiv.org/pdf/2502.19645"},{"title":"GitHub - openvla/openvla: OpenVLA: An open-source vision-language-action model for robotic manipulation. · GitHub","url":"https://github.com/openvla/openvla"},{"title":"moojink/openvla-7b-oft-finetuned-libero-goal · Hugging Face","url":"https://huggingface.co/moojink/openvla-7b-oft-finetuned-libero-goal"},{"title":"OpenVLA: An Open-Source Vision-Language-Action Model","url":"https://arxiv.org/pdf/2406.09246"},{"title":"GitHub - reazon-research/openvla: OpenVLA: An open-source vision-language-action model for robotic manipulation. · GitHub","url":"https://github.com/reazon-research/openvla"}]

Based on the search results, I found information about OpenVLA-OFT (Optimized Fine-Tuning) related to your query:

OpenVLA-OFT is an Optimized Fine-Tuning recipe that integrates parallel decoding and action chunking, continuous action representations, and an L1 regression objective to enhance inference efficiency, task performance, and model input-output flexibility.

The search results show that the fine-tuning recipe enables OpenVLA to successfully execute dexterous, high-frequency control tasks on a bimanual ALOHA robot and outperform other VLAs like π₀ and RDT-1B fine-tuned using their default recipes.

The code for OFT and pretrained model checkpoints are available at https://openvla-oft.github.io. Additionally, there are related repositories on GitHub (such as moojink/openvla-oft and hanbit-o/openvla-oft) that co
…[truncated 556 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_openvla-oft-survey_20260520T040517",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 33 · 2026-05-20T04:19:56.342547+00:00_

# OpenVLA-OFT: Fine-Tuning Vision-Language-Action Models

## Authors and Affiliations
- **Moo Jin Kim** (Stanford University)
- **Chelsea Finn** (Stanford University)
- **Percy Liang** (Stanford University)

## Key Claims

The authors present an "Optimized Fine-Tuning (OFT) recipe" combining parallel decoding, action chunking, continuous action representation, and L1 regression. They claim this approach delivers "significantly enhanced inference speed (25-50x) and task performance (20%+ boost in success rate)."

## LIBERO Benchmark Results

**OpenVLA-OFT achieves state-of-the-art performance:**
- 97.1% average success rate across four LIBERO task suites
- Outperforms π0, MDT, Seer, DiT Policy, Octo, and Diffusion Policy
- 26x faster action generation and 3x lower latency compared to base OpenVLA

## Real-World Robot Experiments

The researchers conducted extensive testing on the bimanual ALOHA robot across four dexterous manipulation tasks:
- OpenVLA-OFT+ outperforms non-VLA methods (ACT, Diffusion Policy) trained from scratch
- Fine-tuned VLAs consistently exceed from-scratch policies
- The method demonstrates "strongest language grounding" among evaluated approaches

## SafeLIBERO Mention

**No mention of SafeLIBERO appears in this document.**

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_openvla-oft-survey_20260520T040517",
  "tool": "WebFetch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 34 · 2026-05-20T04:19:56.342703+00:00_

Web search results for query: ""openvla-oft" authors "Moo Jin Kim" Stanford affiliation"

Links: [{"title":"Moo Jin Kim","url":"https://www.catalyzex.com/author/Moo%20Jin%20Kim"},{"title":"Moo Jin Kim @moo_jin_kim X Profile | Muskviewer","url":"https://www.muskviewer.com/moo_jin_kim"},{"title":"GitHub - moojink/openvla-oft: Fine-Tuning Vision-Language-Action Models: Optimizing Speed and Success · GitHub","url":"https://github.com/moojink/openvla-oft"},{"title":"OpenVLA: An Open-Source Vision-Language-Action Model","url":"https://openvla.github.io/"},{"title":"moojink (Moo Jin Kim) · GitHub","url":"https://github.com/moojink"},{"title":"[Literature Review] Fine-Tuning Vision-Language-Action Models: Optimizing Speed and Success","url":"https://www.themoonlight.io/en/review/fine-tuning-vision-language-action-models-optimizing-speed-and-success"},{"title":"Moo Jin Kim","url":"https://moojink.com/"},{"title":"Moo Jin Kim","url":"https://scholar.google.com/citations?user=ZKRs0oEAAAAJ&hl=en"},{"title":"Moo Jin Kim - Stanford, California, United States | Professional Profile | LinkedIn","url":"https://www.linkedin.com/in/moojink"},{"title":"Fine-Tuning Vision-Language-Action Models: Optimizing Speed and Success","url":"https://arxiv.org/pdf/2502.19645"}]

Based on the search results, I found information about the OpenVLA-OFT paper and Moo Jin Kim's affiliation:

Moo Jin Kim is an author of the "Fine-Tuning Vision-Language-Action Models: Optimizing Speed and Success" paper, which introduces OpenVLA-OFT. Moo Jin Kim is a Computer Science Ph.D. student at Stanford University, advised by Chelsea Finn and Percy Liang. 

The paper also lists other authors besides Kim, and the other co-authors from Stanford University include Chelsea Finn and Percy Liang.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_openvla-oft-survey_20260520T040517",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 35 · 2026-05-20T04:19:56.342850+00:00_

Web search results for query: "site:github.com openvla LIBERO safety obstacle avoidance"

Links: [{"title":"GitHub - openvla/openvla: OpenVLA: An open-source vision-language-action model for robotic manipulation. · GitHub","url":"https://github.com/openvla/openvla"},{"title":"Online Learning for Obstacle Avoidance","url":"https://arxiv.org/pdf/2306.08776"},{"title":"GitHub - OpenDriveLab/UniVLA: [RSS 2025] Learning to Act Anywhere with Task-centric Latent Actions · GitHub","url":"https://github.com/OpenDriveLab/UniVLA"},{"title":"GitHub - moojink/openvla-oft: Fine-Tuning Vision-Language-Action Models: Optimizing Speed and Success · GitHub","url":"https://github.com/moojink/openvla-oft"},{"title":"LIBERO Environment · Issue #199 · openvla/openvla","url":"https://github.com/openvla/openvla/issues/199"},{"title":"Learning Safety for Obstacle Avoidance via Control Barrier Functions","url":"https://arxiv.org/pdf/2509.16037"},{"title":"GitHub - PRIME-RL/SimpleVLA-RL: [ICLR 2026] SimpleVLA-RL: Scaling VLA Training via Reinforcement Learning · GitHub","url":"https://github.com/PRIME-RL/SimpleVLA-RL"},{"title":"openvla-oft/README.md at main · moojink/openvla-oft","url":"https://github.com/moojink/openvla-oft/blob/main/README.md"}]

The search results show information about OpenVLA and LIBERO, though the specific combination of all three terms with safety and obstacle avoidance doesn't appear prominently in the results. Here's what I found:

The updated OpenVLA paper (v2) discusses fine-tuning OpenVLA on a simulated benchmark called LIBERO in Appendix E. OpenVLA was fine-tuned via LoRA (r=32) on four LIBERO task suites independently: LIBERO-Spatial, LIBERO-Object, LIBERO-Goal, and LIBERO-10 (also called LIBERO-Long).

While the search results mention OpenVLA and LIBERO extensively, they don't specifically address safety or obstacle avoidance features in the context of these tools on GitHub. The results do show that there are various implementations and fine-tuning approaches 
…[truncated 519 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_openvla-oft-survey_20260520T040517",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 36 · 2026-05-20T04:19:56.343050+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://huggingface.co/datasets/THURCSCT/SafeLIBERO",
  "prompt": "Extract: dataset description, number of downloads, what VLA models it's designed for, relationship to OpenVLA, task descriptions, safety levels."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_openvla-oft-survey_20260520T040517",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://huggingface.co/datasets/THURCSCT/SafeLIBERO",
    "prompt": "Extract: dataset description, number of downloads, what VLA models it's designed for, relationship to OpenVLA, task descriptions, safety levels."
  }
}
```

</details>

---

### Tool call

_source line 37 · 2026-05-20T04:19:56.343190+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "github.com vlsa-aegis THU-RCSCT stars OpenVLA baseline"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_openvla-oft-survey_20260520T040517",
  "tool": "WebSearch",
  "tool_args": {
    "query": "github.com vlsa-aegis THU-RCSCT stars OpenVLA baseline"
  }
}
```

</details>

---

### Tool result

_source line 38 · 2026-05-20T04:19:56.343320+00:00_

Web search results for query: "github.com vlsa-aegis THU-RCSCT stars OpenVLA baseline"

Links: [{"title":"GitHub - THU-RCSCT/vlsa-aegis: VLSA: Vision-Language-Action Models with Plug-and-Play Safety Constraint Layer","url":"https://github.com/THU-RCSCT/vlsa-aegis"},{"title":"VLSA: Vision-Language-Action Models with Plug-and-Play Safety Constraint Layer","url":"https://arxiv.org/html/2512.11891v1"},{"title":"OpenVLA - AI Agent Index - MIT","url":"https://aiagentindex.mit.edu/openvla/"},{"title":"VLSA: Vision-Language-Action Models with Plug-and-Play Safety Constraint Layer [Quick Review]","url":"https://liner.com/review/vlsa-visionlanguageaction-models-with-plugandplay-safety-constraint-layer"},{"title":"VLSA: Vision-Language-Action Models with Plug-and-Play Safety Constraint Layer","url":"https://vlsa-aegis.github.io/"},{"title":"VLSA: Vision-Language-Action Models with Plug-and-Play Safety Constraint Layer","url":"https://arxiv.org/pdf/2512.11891"},{"title":"GitHub - openvla/openvla: OpenVLA: An open-source vision-language-action model for robotic manipulation. · GitHub","url":"https://github.com/openvla/openvla"},{"title":"OpenVLA: An Open-Source Vision-Language-Action Model","url":"https://arxiv.org/pdf/2406.09246"}]

Based on the search results, here's what I found about the THU-RCSCT/vlsa-aegis repository:

The vlsa-aegis repository had its initial release on December 9, 2025. It introduces a Vision-Language-Safe Action (VLSA) architecture named AEGIS, which contains a plug-and-play safety constraint layer formulated via control barrier functions that integrates directly with existing VLA models to improve safety.

Regarding the OpenVLA baseline comparison: OpenVLA-OFT is used as a baseline, described as a robust transformer-based VLA variant adapted via online fine-tuning. The AEGIS framework significantly outperforms OpenVLA-OFT in collision avoidance rate (CAR) and task success rate (TSR), achieving an average CAR of 77.85% compared to OpenVLA-OFT's 15.13%.

…[truncated 295 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_openvla-oft-survey_20260520T040517",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 39 · 2026-05-20T04:19:56.343466+00:00_

# SafeLIBERO Dataset Overview

## Dataset Description
**SafeLIBERO** is a benchmark designed to evaluate robotic model performance in complex, safety-critical environments. It extends the LIBERO suite by selecting four representative tasks per suite, with each task divided into two safety-level scenarios based on obstacle interference.

## Key Statistics
- **Downloads (last month):** 392
- **Total file size:** 638 MB
- **Scale:** 4 suites, 16 tasks, 32 scenarios, 1,600 evaluation episodes
- **Episodes per scenario:** 50 (with randomized positions)

## Safety Levels
- **Level I:** Obstacle positioned in close proximity to the target object
- **Level II:** Obstacle located further away but obstructing the movement path

## Task Descriptions
SafeLIBERO includes 4 suites with 16 total tasks:

| Suite | Tasks | Examples |
|-------|-------|----------|
| **Spatial** | 4 tasks | Pick up black bowl and place on plate (from various locations) |
| **Goal** | 4 tasks | Put bowl on plate/cabinet/stove; organize items in drawer |
| **Object** | 4 tasks | Pick up various items (juice, pudding, milk, sauce) and place in basket |
| **Long** | 4 tasks | Multi-step tasks like placing two items in basket or organizing mugs on plates |

## VLA Model Compatibility
The dataset is designed for **Vision-Language-Action (VLA) models**, specifically mentioned:
- **VLSA** (Vision-Language-Action Models with Plug-and-Play Safety Constraint Layer)
- Other VLA models compatible with the LIBERO framework

## Relationship to OpenVLA
The page does not mention OpenVLA. SafeLIBERO builds upon **LIBERO**, **RynnVLA-002**, and **MCC5-THU-Gearbox-Benchmark-Datasets**.

## Installation
```bash
conda create -n libero python=3.8.13
conda activate libero
git clone https://github.com/THU-RCSCT/vlsa-aegis.git
cd SafeLIBERO/safelibero
pip install -r requirements.txt
```

## Running Evaluation Example
```bash
export PYTHONPATH=$PYTHONPATH:$PWD/safelibero
python main_demo.py \
    --task-suite-name safelibero_spa
…[truncated 128 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_openvla-oft-survey_20260520T040517",
  "tool": "WebFetch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 40 · 2026-05-20T04:19:56.343657+00:00_

Here is the consolidated report:

---

## 1. OpenVLA (Main Repository)

- **URL:** https://github.com/openvla/openvla
- **Stars:** ~6,200
- **Forks:** ~734
- **License:** MIT
- **Language:** Python (99.9%)
- **Description:** "An open-source vision-language-action model for robotic manipulation"
- **Commits:** 63 on main branch
- **Paper:** [OpenVLA: An Open-Source Vision-Language-Action Model](https://arxiv.org/abs/2406.09246) (June 2024)
- **Authors/Orgs:** Stanford, UC Berkeley, Google DeepMind, Toyota Research Institute
- **OFT in main repo:** The main README references OpenVLA-OFT (added March 3, 2025 update), but OFT is NOT a branch within this repo. It links out to the separate `moojink/openvla-oft` repository.
- **LIBERO support:** The main repo contains `experiments/robot/libero/` with dataset regeneration scripts and fine-tuning support via LoRA.

## 2. OpenVLA-OFT (Separate Repository)

- **URL:** https://github.com/moojink/openvla-oft
- **Stars:** ~1,200
- **Forks:** ~169
- **License:** MIT
- **Language:** Python (100%)
- **Project page:** https://openvla-oft.github.io/
- **Paper:** [Fine-Tuning Vision-Language-Action Models: Optimizing Speed and Success](https://arxiv.org/abs/2502.19645) (Feb 27, 2025; revised Apr 28, 2025)
- **Venue:** Accepted at **RSS 2025** (Robotics: Science and Systems)
- **Authors:** Moo Jin Kim, Chelsea Finn, Percy Liang (all Stanford University)
- **OFT meaning:** "Optimized Fine-Tuning" (not Orthogonal Fine-Tuning). It is a recipe combining parallel decoding, action chunking, continuous action representation, and L1 regression.
- **Key results:**
  - LIBERO average success rate: **76.5% -> 97.1%** (new SOTA on LIBERO)
  - **26x** faster action generation, **3x** lower latency vs. base OpenVLA
  - 25-50x faster inference than vanilla OpenVLA fine-tuning
  - Outperforms pi0, RDT-1B, Diffusion Policy on real ALOHA bimanual robot by up to 15%
- **Pretrained checkpoints on HuggingFace:** `moojink/openvla-7b-oft-finetuned-libero-spat
…[truncated 2656 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_openvla-oft-survey_20260520T040517",
  "tool": "Agent",
  "elapsed_ms": 5
}
```

</details>

---

### Tool call

_source line 41 · 2026-05-20T04:19:56.343837+00:00_

called Agent

<details open><summary>🔧 Tool call — Agent</summary>

```json
{
  "description": "Fetch OpenVLA-OFT README details",
  "subagent_type": "general-purpose",
  "prompt": "Fetch the full README and key source files from the OpenVLA-OFT repository at https://github.com/moojink/openvla-oft to extract detailed technical information.\n\nI need:\n1. Full README content - especially fine-tuning instructions, hyperparameters, GPU requirements, data format\n2. The requirements.txt or setup.py/pyproject.toml for dependency versions\n3. The model architecture file - look for files defining the OFT model (likely in src/ or prismatic/ or openvla/ directory)\n4. Fine-tuning scripts - look for training scripts, especially any LIBERO-specific ones\n5. Data loading code - how does it load RLDS/LIBERO data\n\nUse WebFetch to get:\n- https://raw.githubusercontent.com/moojink/openvla-oft/main/README.md\n- https://api.github.com/repos/moojink/openvla-oft/contents/ (to see directory structure)\n- Then fetch key files based on what you find in the directory listing\n\nReport everything in detail - versions, paths, configurations, architecture details."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_openvla-oft-survey_20260520T040517",
  "tool": "Agent",
  "tool_args": {
    "description": "Fetch OpenVLA-OFT README details",
    "subagent_type": "general-purpose",
    "prompt": "Fetch the full README and key source files from the OpenVLA-OFT repository at https://github.com/moojink/openvla-oft to extract detailed technical information.\n\nI need:\n1. Full README content - especially fine-tuning instructions, hyperparameters, GPU requirements, data format\n2. The requirements.txt or setup.py/pyproject.toml for dependency versions\n3. The model architecture file - look for files defining the OFT model (likely in src/ or prismatic/ or openvla/ directory)\n4. Fine-tuning scripts - look for training scripts, especially any LIBERO-specific ones\n5. Data loading code - how does it load RLDS/LIBERO data\n\nUse WebFetch to get:\n- https://raw.githubusercontent.com/moojink/openvla-oft/main/README.md\n- https://api.github.com/repos/moojink/openvla-oft/contents/ (to see directory structure)\n- Then fetch key files based on what you find in the directory listing\n\nReport everything in detail - versions, paths, configurations, architecture details."
  }
}
```

</details>

---

### Tool call

_source line 42 · 2026-05-20T04:19:56.343994+00:00_

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
  "session": "worker_research_openvla-oft-survey_20260520T040517",
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

_source line 43 · 2026-05-20T04:19:56.344111+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_openvla-oft-survey_20260520T040517",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 44 · 2026-05-20T04:19:56.344229+00:00_

called Agent

<details open><summary>🔧 Tool call — Agent</summary>

```json
{
  "description": "Fetch OpenVLA-OFT paper details",
  "subagent_type": "general-purpose",
  "prompt": "Fetch the OpenVLA-OFT paper from arxiv to extract detailed technical information about the architecture, training procedure, and results.\n\nPaper: https://arxiv.org/abs/2502.19645\n\nUse WebFetch to get:\n1. The arxiv abstract page: https://arxiv.org/abs/2502.19645\n2. The HTML version if available: https://arxiv.org/html/2502.19645\n\nI need to extract:\n- Exact architecture details: what modifications were made to the base OpenVLA model\n- Action head design: parallel decoding, action chunking details, how many tokens, action dimensions\n- Training procedure: optimizer, learning rate, batch size, epochs, GPU hours\n- LIBERO results: per-task success rates\n- Vision encoder details: what backbone, feature dimensions, spatial resolution\n- Any mention of auxiliary losses or multi-task training\n- Memory/compute requirements mentioned in the paper\n\nReport all findings in detail with specific numbers."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_openvla-oft-survey_20260520T040517",
  "tool": "Agent",
  "tool_args": {
    "description": "Fetch OpenVLA-OFT paper details",
    "subagent_type": "general-purpose",
    "prompt": "Fetch the OpenVLA-OFT paper from arxiv to extract detailed technical information about the architecture, training procedure, and results.\n\nPaper: https://arxiv.org/abs/2502.19645\n\nUse WebFetch to get:\n1. The arxiv abstract page: https://arxiv.org/abs/2502.19645\n2. The HTML version if available: https://arxiv.org/html/2502.19645\n\nI need to extract:\n- Exact architecture details: what modifications were made to the base OpenVLA model\n- Action head design: parallel decoding, action chunking details, how many tokens, action dimensions\n- Training procedure: optimizer, learning rate, batch size, epochs, GPU hours\n- LIBERO results: per-task success rates\n- Vision encoder details: what backbone, feature dimensions, spatial resolution\n- Any mention of auxiliary losses or multi-task training\n- Memory/compute requirements mentioned in the paper\n\nReport all findings in detail with specific numbers."
  }
}
```

</details>

---

### Tool call

_source line 45 · 2026-05-20T04:19:56.344387+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://raw.githubusercontent.com/moojink/openvla-oft/main/README.md",
  "prompt": "Return the COMPLETE content of this README file verbatim. Include every section, every code block, every hyperparameter, every instruction. Do not summarize or skip anything."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_openvla-oft-survey_20260520T040517",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://raw.githubusercontent.com/moojink/openvla-oft/main/README.md",
    "prompt": "Return the COMPLETE content of this README file verbatim. Include every section, every code block, every hyperparameter, every instruction. Do not summarize or skip anything."
  }
}
```

</details>

---

### Tool call

_source line 46 · 2026-05-20T04:19:56.344513+00:00_

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
  "session": "worker_research_openvla-oft-survey_20260520T040517",
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

_source line 47 · 2026-05-20T04:19:56.344628+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_openvla-oft-survey_20260520T040517",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 48 · 2026-05-20T04:19:56.344769+00:00_

called Agent

<details open><summary>🔧 Tool call — Agent</summary>

```json
{
  "description": "Research SafeLIBERO integration",
  "subagent_type": "general-purpose",
  "prompt": "Research SafeLIBERO and how it relates to OpenVLA-OFT for a project that wants to add occupancy-based safety to VLA models.\n\nSearch for and fetch:\n1. SafeLIBERO dataset details from https://huggingface.co/datasets/THURCSCT/SafeLIBERO - what format is the data in, what tasks, what safety annotations\n2. VLSA-AEGIS paper: https://arxiv.org/abs/2512.11891 - how they integrate safety into VLA models, what's their approach\n3. Search for any other work combining occupancy prediction/maps with VLA models or robot manipulation\n4. Search for \"OpenVLA LIBERO fine-tuning\" to find any tutorials, blog posts, or third-party implementations\n\nKey questions to answer:\n- What data format does SafeLIBERO use? Is it compatible with OpenVLA-OFT's expected input?\n- Does SafeLIBERO include obstacle/occupancy annotations that could be used for auxiliary head training?\n- What action space does SafeLIBERO use vs what OpenVLA-OFT expects?\n- Are there existing occupancy prediction heads for VLA models?\n\nReport all findings with URLs."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_openvla-oft-survey_20260520T040517",
  "tool": "Agent",
  "tool_args": {
    "description": "Research SafeLIBERO integration",
    "subagent_type": "general-purpose",
    "prompt": "Research SafeLIBERO and how it relates to OpenVLA-OFT for a project that wants to add occupancy-based safety to VLA models.\n\nSearch for and fetch:\n1. SafeLIBERO dataset details from https://huggingface.co/datasets/THURCSCT/SafeLIBERO - what format is the data in, what tasks, what safety annotations\n2. VLSA-AEGIS paper: https://arxiv.org/abs/2512.11891 - how they integrate safety into VLA models, what's their approach\n3. Search for any other work combining occupancy prediction/maps with VLA models or robot manipulation\n4. Search for \"OpenVLA LIBERO fine-tuning\" to find any tutorials, blog posts, or third-party implementations\n\nKey questions to answer:\n- What data format does SafeLIBERO use? Is it compatible with OpenVLA-OFT's expected input?\n- Does SafeLIBERO include obstacle/occupancy annotations that could be used for auxiliary head training?\n- What action space does SafeLIBERO use vs what OpenVLA-OFT expects?\n- Are there existing occupancy prediction heads for VLA models?\n\nReport all findings with URLs."
  }
}
```

</details>

---

### Tool call

_source line 49 · 2026-05-20T04:19:56.344916+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://api.github.com/repos/moojink/openvla-oft/contents/",
  "prompt": "Return the complete JSON listing of all files and directories at the root level. Include name, path, type (file or dir) for every entry."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_openvla-oft-survey_20260520T040517",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://api.github.com/repos/moojink/openvla-oft/contents/",
    "prompt": "Return the complete JSON listing of all files and directories at the root level. Include name, path, type (file or dir) for every entry."
  }
}
```

</details>

---

### Tool call

_source line 50 · 2026-05-20T04:19:56.345051+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://arxiv.org/abs/2502.19645",
  "prompt": "Extract ALL technical details from this paper abstract page about OpenVLA-OFT. I need:\n1. Full title and authors\n2. Complete abstract text\n3. Any architecture details mentioned\n4. Any training details mentioned\n5. Any results/benchmarks mentioned\n6. Any other technical information available on this page"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_openvla-oft-survey_20260520T040517",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://arxiv.org/abs/2502.19645",
    "prompt": "Extract ALL technical details from this paper abstract page about OpenVLA-OFT. I need:\n1. Full title and authors\n2. Complete abstract text\n3. Any architecture details mentioned\n4. Any training details mentioned\n5. Any results/benchmarks mentioned\n6. Any other technical information available on this page"
  }
}
```

</details>

---

### Tool call

_source line 51 · 2026-05-20T04:19:56.345175+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:WebFetch,WebSearch",
  "max_results": "2"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_openvla-oft-survey_20260520T040517",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:WebFetch,WebSearch",
    "max_results": "2"
  }
}
```

</details>

---

### Tool result

_source line 52 · 2026-05-20T04:19:56.345295+00:00_

# Root Level Files and Directories

```json
[
  {
    "name": ".gitignore",
    "path": ".gitignore",
    "type": "file"
  },
  {
    "name": ".pre-commit-config.yaml",
    "path": ".pre-commit-config.yaml",
    "type": "file"
  },
  {
    "name": "ALOHA.md",
    "path": "ALOHA.md",
    "type": "file"
  },
  {
    "name": "LIBERO.md",
    "path": "LIBERO.md",
    "type": "file"
  },
  {
    "name": "LICENSE",
    "path": "LICENSE",
    "type": "file"
  },
  {
    "name": "README.md",
    "path": "README.md",
    "type": "file"
  },
  {
    "name": "SETUP.md",
    "path": "SETUP.md",
    "type": "file"
  },
  {
    "name": "experiments",
    "path": "experiments",
    "type": "dir"
  },
  {
    "name": "prismatic",
    "path": "prismatic",
    "type": "dir"
  },
  {
    "name": "pyproject.toml",
    "path": "pyproject.toml",
    "type": "file"
  },
  {
    "name": "scripts",
    "path": "scripts",
    "type": "dir"
  },
  {
    "name": "vla-scripts",
    "path": "vla-scripts",
    "type": "dir"
  }
]
```

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_openvla-oft-survey_20260520T040517",
  "tool": "WebFetch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 53 · 2026-05-20T04:19:56.345418+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_openvla-oft-survey_20260520T040517",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 54 · 2026-05-20T04:19:56.345529+00:00_

# OpenVLA-OFT: Vision-Language-Action Model Fine-Tuning

This project presents methods for optimizing Vision-Language-Action (VLA) models through fine-tuning approaches. The research introduces OpenVLA-OFT, a system designed to improve both inference speed and task success rates.

## Key Resources

The project maintains a dedicated website at https://openvla-oft.github.io/ with comprehensive documentation. The underlying research is published as a preprint, and a summary video provides visual context for the methodology.

## Hardware Requirements

**For inference tasks:**
- LIBERO simulation benchmarks need approximately 16 GB VRAM
- ALOHA robot applications require roughly 18 GB VRAM

**For training operations:**
The project supports flexible scaling from "1-8 GPUs with 27-80 GB, depending on the desired training setup" when using default bfloat16 precision. Additional training configuration details are available through the project's FAQ section.

## Getting Started

After environment setup, users can execute a Python script that loads a pretrained checkpoint and performs action generation. The process involves instantiating a configuration object with specific parameters like checkpoint selection, regression type, and input specifications.

The workflow includes loading the VLA policy, processor components, action generation heads, and proprioceptive projectors. Sample observations containing images and task descriptions generate predicted action sequences.

## Documentation Structure

Setup instructions are contained in a dedicated SETUP file. Simulation benchmarking and real-world robotics evaluation procedures are documented separately for LIBERO and ALOHA tasks respectively.

## Contact & Citation

The project welcomes issue reports with a 2-business-day response target. For persistent problems, direct contact with the lead researcher is available.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_openvla-oft-survey_20260520T040517",
  "tool": "WebFetch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool call

_source line 55 · 2026-05-20T04:19:56.345681+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://huggingface.co/datasets/THURCSCT/SafeLIBERO",
  "prompt": "Extract all details about the SafeLIBERO dataset: What format is the data in (HDF5, RLDS, etc.)? What tasks are included? What safety annotations exist? What observation space (images, proprioception)? What action space (dimension, format)? What are the columns/fields in the dataset? How many episodes/demonstrations? Is there obstacle or occupancy information? What is the relationship to the original LIBERO benchmark?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_openvla-oft-survey_20260520T040517",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://huggingface.co/datasets/THURCSCT/SafeLIBERO",
    "prompt": "Extract all details about the SafeLIBERO dataset: What format is the data in (HDF5, RLDS, etc.)? What tasks are included? What safety annotations exist? What observation space (images, proprioception)? What action space (dimension, format)? What are the columns/fields in the dataset? How many episodes/demonstrations? Is there obstacle or occupancy information? What is the relationship to the original LIBERO benchmark?"
  }
}
```

</details>

---

### Tool call

_source line 56 · 2026-05-20T04:19:56.345820+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://raw.githubusercontent.com/moojink/openvla-oft/main/pyproject.toml",
  "prompt": "Return the COMPLETE file content exactly as-is. Every line, every dependency, every version number. Do not summarize."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_openvla-oft-survey_20260520T040517",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://raw.githubusercontent.com/moojink/openvla-oft/main/pyproject.toml",
    "prompt": "Return the COMPLETE file content exactly as-is. Every line, every dependency, every version number. Do not summarize."
  }
}
```

</details>

---

### Tool result

_source line 57 · 2026-05-20T04:19:56.345945+00:00_

# OpenVLA-OFT Technical Details

## Title and Authors
**"Fine-Tuning Vision-Language-Action Models: Optimizing Speed and Success"**

Authors: Moo Jin Kim, Chelsea Finn, Percy Liang

## Complete Abstract
The authors investigate how to effectively fine-tune vision-language-action models (VLAs) that build on pretrained vision-language models. They examine "different action decoding schemes, action representations, and learning objectives" to develop their optimization approach.

## Architecture and Design Choices
The Optimized Fine-Tuning (OFT) recipe incorporates:
- Parallel decoding for action generation
- Action chunking methodology
- Continuous action representation
- L1 regression-based learning objective

## Key Results and Benchmarks
- **LIBERO simulation**: Success rate increased from 76.5% to 97.1%
- **Throughput**: 26× improvement in action generation speed
- **Real-world ALOHA robot**: Outperformed π₀ and RDT-1B by margins
- **Success rate gains**: Up to 15% absolute improvement over Diffusion Policy and ACT baselines

## Additional Details
- Venue: Robotics: Science and Systems (RSS) 2025
- License: Creative Commons BY 4.0
- Code and model checkpoints released at project website

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_openvla-oft-survey_20260520T040517",
  "tool": "WebFetch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 58 · 2026-05-20T04:19:56.346091+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://arxiv.org/html/2502.19645",
  "prompt": "Extract ALL technical details from this paper. I need EVERY specific number and detail about:\n\n1. ARCHITECTURE: What is the base model? What modifications were made? What is the vision encoder (backbone, feature dimensions, spatial resolution)? What is the language model component? How are vision tokens processed?\n\n2. ACTION HEAD DESIGN: How does parallel decoding work? What is action chunking? How many tokens are used? What are the action dimensions? How is the action space discretized or continuous? What is the action chunk size?\n\n3. TRAINING PROCEDURE: Optimizer, learning rate, learning rate schedule, batch size, number of epochs, GPU hours, number of GPUs used, training data details, warmup steps, weight decay.\n\n4. LIBERO RESULTS: Per-task success rates, comparison with baselines, per-suite results (LIBERO-Spatial, LIBERO-Object, LIBERO-Goal, LIBERO-Long). Give me ALL numbers from ALL tables.\n\n5. AUXILIARY LOSSES: Any mention of auxiliary losses, multi-task training, loss functions used.\n\n6. MEMORY/COMPUTE: GPU memory requirements, inference speed (tokens/sec or Hz), model size (parameters), FLOPs.\n\n7. Any other technical details: data augmentation, tokenization scheme, normalization, action representation.\n\nBe exhaustive - extract every number, every detail, every table entry you can find."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_openvla-oft-survey_20260520T040517",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://arxiv.org/html/2502.19645",
    "prompt": "Extract ALL technical details from this paper. I need EVERY specific number and detail about:\n\n1. ARCHITECTURE: What is the base model? What modifications were made? What is the vision encoder (backbone, feature dimensions, spatial resolution)? What is the language model component? How are vision tokens processed?\n\n2. ACTION HEAD DESIGN: How does parallel decoding work? What is action chunking? How many tokens are used? What are the action dimensions? How is the action space discretized or continuous? What is the action chunk size?\n\n3. TRAINING PROCEDURE: Optimizer, learning rate, learning rate schedule, batch size, number of epochs, GPU hours, number of GPUs used, training data details, warmup steps, weight decay.\n\n4. LIBERO RESULTS: Per-task success rates, comparison with baselines, per-suite results (LIBERO-Spatial, LIBERO-Object, LIBERO-Goal, LIBERO-Long). Give me ALL numbers from ALL tables.\n\n5. AUXILIARY LOSSES: Any mention of auxiliary losses, multi-task training, loss functions used.\n\n6. MEMORY/COMPUTE: GPU memory requirements, inference speed (tokens/sec or Hz), model size (parameters), FLOPs.\n\n7. Any other technical details: data augmentation, tokenization scheme, normalization, action representation.\n\nBe exhaustive - extract every number, every detail, every table entry you can find."
  }
}
```

</details>

---

### Tool call

_source line 59 · 2026-05-20T04:19:56.346232+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://raw.githubusercontent.com/moojink/openvla-oft/main/SETUP.md",
  "prompt": "Return the COMPLETE file content exactly as-is. Every line, every command, every instruction. Do not summarize or skip anything."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_openvla-oft-survey_20260520T040517",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://raw.githubusercontent.com/moojink/openvla-oft/main/SETUP.md",
    "prompt": "Return the COMPLETE file content exactly as-is. Every line, every command, every instruction. Do not summarize or skip anything."
  }
}
```

</details>

---

### Tool call

_source line 60 · 2026-05-20T04:19:56.346358+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://raw.githubusercontent.com/moojink/openvla-oft/main/LIBERO.md",
  "prompt": "Return the COMPLETE file content exactly as-is. Every section, every code block, every hyperparameter, every command. Do not summarize."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_openvla-oft-survey_20260520T040517",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://raw.githubusercontent.com/moojink/openvla-oft/main/LIBERO.md",
    "prompt": "Return the COMPLETE file content exactly as-is. Every section, every code block, every hyperparameter, every command. Do not summarize."
  }
}
```

</details>

---

### Tool call

_source line 61 · 2026-05-20T04:19:56.346480+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://arxiv.org/abs/2512.11891",
  "prompt": "Extract the full details of the VLSA-AEGIS paper: What is the approach for integrating safety into VLA models? What architecture modifications do they make? How do they define safety constraints? Do they use occupancy maps or obstacle avoidance? What is their training procedure? What datasets do they use? What are the key results? What VLA backbone do they build on (OpenVLA, RT-2, etc.)?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_openvla-oft-survey_20260520T040517",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://arxiv.org/abs/2512.11891",
    "prompt": "Extract the full details of the VLSA-AEGIS paper: What is the approach for integrating safety into VLA models? What architecture modifications do they make? How do they define safety constraints? Do they use occupancy maps or obstacle avoidance? What is their training procedure? What datasets do they use? What are the key results? What VLA backbone do they build on (OpenVLA, RT-2, etc.)?"
  }
}
```

</details>

---

### Tool call

_source line 62 · 2026-05-20T04:19:56.346605+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "occupancy prediction VLA robot manipulation safety 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_openvla-oft-survey_20260520T040517",
  "tool": "WebSearch",
  "tool_args": {
    "query": "occupancy prediction VLA robot manipulation safety 2025 2026"
  }
}
```

</details>

---

### Tool call

_source line 63 · 2026-05-20T04:19:56.346755+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://api.github.com/repos/moojink/openvla-oft/contents/prismatic",
  "prompt": "Return the complete listing of all files and directories. Include name, path, type for every entry."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_openvla-oft-survey_20260520T040517",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://api.github.com/repos/moojink/openvla-oft/contents/prismatic",
    "prompt": "Return the complete listing of all files and directories. Include name, path, type for every entry."
  }
}
```

</details>

---

### Tool call

_source line 64 · 2026-05-20T04:19:56.346884+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "OpenVLA LIBERO fine-tuning tutorial implementation 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_openvla-oft-survey_20260520T040517",
  "tool": "WebSearch",
  "tool_args": {
    "query": "OpenVLA LIBERO fine-tuning tutorial implementation 2025"
  }
}
```

</details>

---

### Tool result

_source line 65 · 2026-05-20T04:19:56.347013+00:00_

# Setup Instructions

## Set Up Conda Environment

```bash
# Create and activate conda environment
conda create -n openvla-oft python=3.10 -y
conda activate openvla-oft

# Install PyTorch
# Use a command specific to your machine: https://pytorch.org/get-started/locally/
pip3 install torch torchvision torchaudio

# Clone openvla-oft repo and pip install to download dependencies
git clone https://github.com/moojink/openvla-oft.git
cd openvla-oft
pip install -e .

# Install Flash Attention 2 for training (https://github.com/Dao-AILab/flash-attention)
#   =>> If you run into difficulty, try `pip cache remove flash_attn` first
pip install packaging ninja
ninja --version; echo $?  # Verify Ninja --> should return exit code "0"
pip install "flash-attn==2.5.5" --no-build-isolation
```

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_openvla-oft-survey_20260520T040517",
  "tool": "WebFetch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 66 · 2026-05-20T04:19:56.347144+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://api.github.com/repos/moojink/openvla-oft/contents/vla-scripts",
  "prompt": "Return the complete listing of all files and directories. Include name, path, type for every entry."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_openvla-oft-survey_20260520T040517",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://api.github.com/repos/moojink/openvla-oft/contents/vla-scripts",
    "prompt": "Return the complete listing of all files and directories. Include name, path, type for every entry."
  }
}
```

</details>

---

### Tool call

_source line 67 · 2026-05-20T04:19:56.347270+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://api.github.com/repos/moojink/openvla-oft/contents/experiments",
  "prompt": "Return the complete listing of all files and directories. Include name, path, type for every entry."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_openvla-oft-survey_20260520T040517",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://api.github.com/repos/moojink/openvla-oft/contents/experiments",
    "prompt": "Return the complete listing of all files and directories. Include name, path, type for every entry."
  }
}
```

</details>

---

### Tool call

_source line 68 · 2026-05-20T04:19:56.347393+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://api.github.com/repos/moojink/openvla-oft/contents/scripts",
  "prompt": "Return the complete listing of all files and directories. Include name, path, type for every entry."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_openvla-oft-survey_20260520T040517",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://api.github.com/repos/moojink/openvla-oft/contents/scripts",
    "prompt": "Return the complete listing of all files and directories. Include name, path, type for every entry."
  }
}
```

</details>

---

### Tool result

_source line 69 · 2026-05-20T04:19:56.347506+00:00_

# Complete Listing of Prismatic Directory Contents

| Name | Path | Type |
|------|------|------|
| __init__.py | prismatic/__init__.py | file |
| conf | prismatic/conf | directory |
| extern | prismatic/extern | directory |
| models | prismatic/models | directory |
| overwatch | prismatic/overwatch | directory |
| preprocessing | prismatic/preprocessing | directory |
| py.typed | prismatic/py.typed | file |
| training | prismatic/training | directory |
| util | prismatic/util | directory |
| vla | prismatic/vla | directory |

This repository structure contains 3 files and 7 subdirectories within the prismatic package. The presence of `py.typed` indicates this is a typed Python package, while the various subdirectories suggest organization around models, training infrastructure, preprocessing pipelines, and utility functions for what appears to be a vision-language action (VLA) framework.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_openvla-oft-survey_20260520T040517",
  "tool": "WebFetch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 70 · 2026-05-20T04:19:56.347638+00:00_

# Complete pyproject.toml File Content

```
[build-system]
requires = ["setuptools"]
build-backend = "setuptools.build_meta"

[project]
name = "openvla-oft"
authors = [
    {name = "Moo Jin Kim", email="moojink@stanford.edu"},
    {name = "Chelsea Finn", email="cbfinn@cs.stanford.edu"},
    {name = "Percy Liang", email="pliang@cs.stanford.edu"},
]
description = "Fine-Tuning Vision-Language-Action Models: Optimizing Speed and Success"
version = "0.0.1"
readme = "README.md"
requires-python = ">=3.8"
keywords = ["vision-language-actions models", "fine-tuning", "robot learning"]
license = {file = "LICENSE"}
classifiers = [
    "Development Status :: 3 - Alpha",
    "Intended Audience :: Developers",
    "Intended Audience :: Education",
    "Intended Audience :: Science/Research",
    "License :: OSI Approved :: MIT License",
    "Operating System :: OS Independent",
    "Programming Language :: Python :: 3",
    "Programming Language :: Python :: 3.8",
    "Programming Language :: Python :: 3.9",
    "Programming Language :: Python :: 3.10",
    "Programming Language :: Python :: 3 :: Only",
    "Topic :: Scientific/Engineering :: Artificial Intelligence",
]
dependencies = [
    "accelerate>=0.25.0",
    "draccus==0.8.0",
    "einops",
    # "flash_attn==2.5.5",      # Here for documentation -- install *AFTER* editable install (follow README)
    "huggingface_hub",
    "json-numpy",
    "jsonlines",
    "matplotlib",
    "peft==0.11.1",
    "protobuf",
    "rich",
    "sentencepiece==0.1.99",
    "timm==0.9.10",
    "tokenizers==0.19.1",
    "torch==2.2.0",
    "torchvision==0.17.0",
    "torchaudio==2.2.0",
    "transformers @ git+https://github.com/moojink/transformers-openvla-oft.git",  # IMPORTANT: Use this fork for bidirectional attn (for parallel decoding)
    "wandb",
    "tensorflow==2.15.0",
    "tensorflow_datasets==4.9.3",
    "tensorflow_graphics==2021.12.3",
    "dlimp @ git+https://github.com/moojink/dlimp_openvla",
    "diffusers==0.30.3",
    "imageio",
…[truncated 831 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_openvla-oft-survey_20260520T040517",
  "tool": "WebFetch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 71 · 2026-05-20T04:19:56.347802+00:00_

# Directory Listing

Based on the provided content, here is the complete file and directory listing:

| Name | Path | Type |
|------|------|------|
| robot | experiments/robot | dir |

**Summary:** The listing contains a single directory entry named "robot" located at the path "experiments/robot" within the repository moojink/openvla-oft on the main branch.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_openvla-oft-survey_20260520T040517",
  "tool": "WebFetch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 72 · 2026-05-20T04:19:56.347920+00:00_

# File and Directory Listing

Based on the provided content, here is the complete listing of all entries in the vla-scripts directory:

| Name | Path | Type |
|------|------|------|
| deploy.py | vla-scripts/deploy.py | file |
| extern | vla-scripts/extern | dir |
| finetune.py | vla-scripts/finetune.py | file |
| merge_lora_weights_and_save.py | vla-scripts/merge_lora_weights_and_save.py | file |

**Summary:** The directory contains 3 Python script files and 1 subdirectory. The Python files range in size from approximately 3 KB to 48 KB, with finetune.py being the largest at "48092" bytes.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_openvla-oft-survey_20260520T040517",
  "tool": "WebFetch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 73 · 2026-05-20T04:19:56.348032+00:00_

# File and Directory Listing

Based on the provided content, here is the complete listing:

| Name | Path | Type |
|------|------|------|
| extern | scripts/extern | dir |

This represents a single directory entry within the repository structure at `moojink/openvla-oft`. The directory is located at `scripts/extern` and contains no files or subdirectories in the listing provided.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_openvla-oft-survey_20260520T040517",
  "tool": "WebFetch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 74 · 2026-05-20T04:19:56.348149+00:00_

# OpenVLA-OFT LIBERO Benchmark Overview

## Key Components

The documentation describes evaluation and training infrastructure for OpenVLA-OFT models on LIBERO robotics tasks. The setup requires installing LIBERO and downloading optional RLDS-formatted datasets (~10 GB).

## Available Checkpoints

Four independently trained models are provided:
- LIBERO-Spatial
- LIBERO-Object
- LIBERO-Goal
- LIBERO-10

Additionally, one combined checkpoint trains across all four task suites simultaneously, achieving comparable performance (96.8% vs 97.1% average success rates).

## Evaluation Process

"The evaluation script will run 500 trials by default (10 tasks x 50 episodes each)" with configurable parameters. A critical requirement is enabling center crop mode during testing, since models were trained using random crop augmentation techniques.

## Training Configuration

Fine-tuning uses LoRA (rank 32) with specific hyperparameters: batch size 8 per GPU requires ~62 GB VRAM, learning rate 5e-4, and 150,005 total steps with decay after 100K steps. The documentation recommends training until L1 loss plateaus below 0.01.

## Important Notes

Results were obtained using Python 3.10.14, PyTorch 2.2.0, and a custom transformers fork on NVIDIA A100 GPUs. The documentation explicitly cautions that "performance may drop substantially" when testing on different hardware than training devices.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_openvla-oft-survey_20260520T040517",
  "tool": "WebFetch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 75 · 2026-05-20T04:19:56.348277+00:00_

# VLSA-AEGIS Paper Summary

Based on the abstract provided, here's what can be determined about this paper:

## Approach & Architecture
The researchers introduce **VLSA (Vision-Language-Safe Action)**, also called **AEGIS**, which adds a "plug-and-play safety constraint (SC) layer formulated via control barrier functions" to existing VLA models. This design maintains the original instruction-following capabilities while enhancing safety.

## Safety Constraints
The safety mechanism uses **control barrier functions** to formulate the constraints, though specific technical details about obstacle avoidance methods, occupancy maps, or constraint formulation aren't detailed in the abstract.

## Training & Datasets
The paper introduces **SafeLIBERO**, described as "a comprehensive safety-critical benchmark, spanning distinct manipulation scenarios characterized by varying degrees of spatial complexity and obstacle intervention." However, specific training procedures aren't outlined in this excerpt.

## Key Results
The method achieved notable improvements:
- **59.16% improvement in obstacle avoidance rate**
- **17.25% increase in task execution success rate**

## VLA Backbone
The abstract doesn't specify which VLA backbone (OpenVLA, RT-2, etc.) they build upon—only that AEGIS "integrates directly with existing VLA models."

The full paper, code, models, and benchmark datasets are reportedly available at their project website for reproducibility.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_openvla-oft-survey_20260520T040517",
  "tool": "WebFetch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 76 · 2026-05-20T04:19:56.348416+00:00_

Web search results for query: "OpenVLA LIBERO fine-tuning tutorial implementation 2025"

Links: [{"title":"GitHub - openvla/openvla: OpenVLA: An open-source vision-language-action model for robotic manipulation. · GitHub","url":"https://github.com/openvla/openvla"},{"title":"GitHub - dusty-nv/openvla: OpenVLA: An open-source vision-language-action model for robotic manipulation.","url":"https://github.com/dusty-nv/openvla"},{"title":"GitHub - moojink/openvla-oft: Fine-Tuning Vision-Language-Action Models: Optimizing Speed and Success · GitHub","url":"https://github.com/moojink/openvla-oft"},{"title":"Fine-Tuning Vision-Language-Action Models: Optimizing Speed and Success","url":"https://openvla-oft.github.io/"},{"title":"Fine-Tuning Vision-Language-Action Models: Optimizing Speed and Success","url":"https://arxiv.org/pdf/2502.19645"},{"title":"openvla/openvla-7b-finetuned-libero-spatial · Hugging Face","url":"https://huggingface.co/openvla/openvla-7b-finetuned-libero-spatial"},{"title":"openvla/openvla-7b-finetuned-libero-object · Hugging Face","url":"https://huggingface.co/openvla/openvla-7b-finetuned-libero-object"},{"title":"openvla/openvla-7b-finetuned-libero-10 · Hugging Face","url":"https://huggingface.co/openvla/openvla-7b-finetuned-libero-10"},{"title":"Enhancing Linguistic Generalization of VLA: Fine-Tuning OpenVLA via Synthetic Instruction Augmentation","url":"https://arxiv.org/pdf/2603.16044"}]

Based on the search results, here's information about OpenVLA LIBERO fine-tuning implementation in 2025:

## Fine-Tuning Methods

A March 2025 update recommends trying the new OFT (Optimized Fine-Tuning) recipe for fine-tuning OpenVLA to produce faster and more successful policies. 

For those with limited compute resources, fine-tuning OpenVLA using Low-Rank Adaptation (LoRA) via the Hugging Face transformers library is recommended if you do not have sufficient compute to fully fine-tune a 7B-parameter model. The main script for LoRA fine-tuning is vla-scripts/fi
…[truncated 908 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_openvla-oft-survey_20260520T040517",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 77 · 2026-05-20T04:19:56.348568+00:00_

# SafeLIBERO Dataset Details

Based on the provided documentation, here's what we know about the SafeLIBERO dataset:

## Data Format
The dataset uses **`.pruned_init` files** for scene initialization. The exact serialization format (HDF5, RLDS, etc.) is not explicitly stated in the documentation, but the structure is detailed:

### `.pruned_init` File Structure
Each file contains **50 lines** (one per episode), with concatenated state vectors:

```
[Robot qpos] + [Obj_1 Pose (7)] + ... + [Obj_N Pose (7)] + 
[Robot qvel] + [Obj_1 Vel (6)] + ... + [Obj_N Vel (6)]
```

**Object State Representation:**
- **Pose (7-dim):** `[x, y, z, qw, qx, qy, qz]` (position + quaternion orientation)
- **Velocity (6-dim):** `[vx, vy, vz, wx, wy, wz]` (linear + angular velocity)

## Tasks
**4 suites × 4 tasks each = 16 total tasks**

| Suite | Task 0 | Task 1 | Task 2 | Task 3 |
|-------|--------|--------|--------|--------|
| **Spatial** | Bowl between plate/ramekin→plate | Bowl on ramekin→plate | Bowl on stove→plate | Bowl on cabinet→plate |
| **Goal** | Bowl→plate | Bowl→cabinet | Bowl→stove | Bowl→drawer or cream cheese→bowl |
| **Object** | Juice/pudding/milk/sauce→basket | Various items to basket | Various items to basket | Various items to basket |
| **Long** | Multiple objects to basket | Multiple items to basket | Mugs to different plates | Mug + items placement |

## Safety Annotations

**Safety Levels:**
- **Level I:** Obstacle in **close proximity** to target object
- **Level II:** Obstacle **obstructs movement path**

Each task has two scenarios (I/II), creating **32 total scenarios** with **1,600 evaluation episodes** (50 episodes per scenario).

### Collision Detection
Automated collision checking via obstacle displacement:
```python
displacement = np.sum(np.abs(curr_pos - initial_obstacle_pos))
if displacement > 0.001:
    collide_flag = True
```

## Observation Space
**Not explicitly detailed**, but inferred from context:
- Position observations of objects (x, y, z coord
…[truncated 1166 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_openvla-oft-survey_20260520T040517",
  "tool": "WebFetch",
  "elapsed_ms": 2
}
```

</details>

---

### Tool result

_source line 78 · 2026-05-20T04:19:56.348735+00:00_

Web search results for query: "occupancy prediction VLA robot manipulation safety 2025 2026"

Links: [{"title":"SafeVLA: Towards Safety Alignment of Vision-Language-Action Model via Constrained Learning | OpenReview","url":"https://openreview.net/forum?id=dt940loCBT"},{"title":"State of Robotics 2026 Report: $38B Market, 12 Humanoids, VLA Adoption | Robotics Center of Silicon Valley","url":"https://www.roboticscenter.ai/state-of-robotics-2026"},{"title":"GitHub - OpenDriveLab/WholebodyVLA: [ICLR 2026] Towards Unified Latent VLA for Whole-body Loco-manipulation Control · GitHub","url":"https://github.com/OpenDriveLab/WholebodyVLA"},{"title":"Robotics","url":"https://arxiv.org/list/cs.RO/new"},{"title":"CoFreeVLA: Collision-Free Dual-Arm Manipulation via Vision-Language-Action Model and Risk Estimation","url":"https://arxiv.org/pdf/2601.21712"},{"title":"Safe-Night VLA: Seeing the Unseen via Thermal-Perceptive Vision-Language-Action Models for Safety-Critical Manipulation","url":"https://arxiv.org/pdf/2603.05754"},{"title":"Do World Action Models Generalize Better than VLAs? A Robustness Study","url":"https://arxiv.org/html/2603.22078v1"}]

Based on the web search results, here's what I found regarding occupancy prediction, VLA robot manipulation, and safety in 2025-2026:

## Safety and VLA Robot Manipulation

SafeVLA, published in September 2025, demonstrates a 83.58% improvement in safety for Vision-Language-Action models with no performance loss by integrating constraints via a new integrated safety approach based on CMDPs and Safe RL.

Semantic safety supervision improves safety metrics in VLA systems, while reactive Time-To-Collision monitoring can degrade performance, indicating that intent-aware monitoring is needed for VLA systems.

## Collision-Free Manipulation

Recent research has focused on addressing collision risks in dual-arm manipulation. CoFreeVLA designs a self-collision risk estimator that predicts collision likelihood from visual observations and a
…[truncated 698 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_openvla-oft-survey_20260520T040517",
  "tool": "WebSearch",
  "elapsed_ms": 2
}
```

</details>

---

### Tool call

_source line 79 · 2026-05-20T04:19:56.348902+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://raw.githubusercontent.com/moojink/openvla-oft/main/vla-scripts/finetune.py",
  "prompt": "Return the COMPLETE file content exactly as-is. Every line of code, every import, every class definition, every function, every comment. Do not summarize or skip anything. This is critical."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_openvla-oft-survey_20260520T040517",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://raw.githubusercontent.com/moojink/openvla-oft/main/vla-scripts/finetune.py",
    "prompt": "Return the COMPLETE file content exactly as-is. Every line of code, every import, every class definition, every function, every comment. Do not summarize or skip anything. This is critical."
  }
}
```

</details>

---

### Tool call

_source line 80 · 2026-05-20T04:19:56.349037+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://api.github.com/repos/moojink/openvla-oft/contents/prismatic/models",
  "prompt": "Return the complete listing of all files and directories. Include name, path, type for every entry."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_openvla-oft-survey_20260520T040517",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://api.github.com/repos/moojink/openvla-oft/contents/prismatic/models",
    "prompt": "Return the complete listing of all files and directories. Include name, path, type for every entry."
  }
}
```

</details>

---

### Tool call

_source line 81 · 2026-05-20T04:19:56.349166+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://api.github.com/repos/moojink/openvla-oft/contents/prismatic/vla",
  "prompt": "Return the complete listing of all files and directories. Include name, path, type for every entry."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_openvla-oft-survey_20260520T040517",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://api.github.com/repos/moojink/openvla-oft/contents/prismatic/vla",
    "prompt": "Return the complete listing of all files and directories. Include name, path, type for every entry."
  }
}
```

</details>

---

### Tool call

_source line 82 · 2026-05-20T04:19:56.349291+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://api.github.com/repos/moojink/openvla-oft/contents/prismatic/training",
  "prompt": "Return the complete listing of all files and directories. Include name, path, type for every entry."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_openvla-oft-survey_20260520T040517",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://api.github.com/repos/moojink/openvla-oft/contents/prismatic/training",
    "prompt": "Return the complete listing of all files and directories. Include name, path, type for every entry."
  }
}
```

</details>

---

### Tool call

_source line 83 · 2026-05-20T04:19:56.349417+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://api.github.com/repos/moojink/openvla-oft/contents/prismatic/conf",
  "prompt": "Return the complete listing of all files and directories. Include name, path, type for every entry."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_openvla-oft-survey_20260520T040517",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://api.github.com/repos/moojink/openvla-oft/contents/prismatic/conf",
    "prompt": "Return the complete listing of all files and directories. Include name, path, type for every entry."
  }
}
```

</details>

---

### Tool result

_source line 84 · 2026-05-20T04:19:56.349531+00:00_

# File and Directory Listing

Based on the repository content provided, here is the complete listing:

| Name | Path | Type |
|------|------|------|
| __init__.py | prismatic/vla/__init__.py | file |
| action_tokenizer.py | prismatic/vla/action_tokenizer.py | file |
| constants.py | prismatic/vla/constants.py | file |
| datasets | prismatic/vla/datasets | directory |
| materialize.py | prismatic/vla/materialize.py | file |

The listing shows 4 Python files and 1 subdirectory within the `prismatic/vla/` module of the openvla-oft repository.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_openvla-oft-survey_20260520T040517",
  "tool": "WebFetch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 85 · 2026-05-20T04:19:56.349681+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://api.github.com/repos/moojink/openvla-oft/contents/prismatic/preprocessing",
  "prompt": "Return the complete listing of all files and directories. Include name, path, type for every entry."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_openvla-oft-survey_20260520T040517",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://api.github.com/repos/moojink/openvla-oft/contents/prismatic/preprocessing",
    "prompt": "Return the complete listing of all files and directories. Include name, path, type for every entry."
  }
}
```

</details>

---

### Tool result

_source line 86 · 2026-05-20T04:19:56.349809+00:00_

# Complete File and Directory Listing

| Name | Path | Type |
|------|------|------|
| __init__.py | prismatic/training/__init__.py | file |
| materialize.py | prismatic/training/materialize.py | file |
| metrics.py | prismatic/training/metrics.py | file |
| strategies | prismatic/training/strategies | dir |
| train_utils.py | prismatic/training/train_utils.py | file |

This listing contains five entries from the "prismatic/training" directory of the moojink/openvla-oft repository: four Python modules and one subdirectory.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_openvla-oft-survey_20260520T040517",
  "tool": "WebFetch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 87 · 2026-05-20T04:19:56.349924+00:00_

# File Listing for prismatic/conf Directory

Based on the provided content, here are all entries in the directory:

| Name | Path | Type |
|------|------|------|
| __init__.py | prismatic/conf/__init__.py | file |
| datasets.py | prismatic/conf/datasets.py | file |
| models.py | prismatic/conf/models.py | file |
| vla.py | prismatic/conf/vla.py | file |

All four entries are Python files located within the `prismatic/conf/` directory of the moojink/openvla-oft repository.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_openvla-oft-survey_20260520T040517",
  "tool": "WebFetch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 88 · 2026-05-20T04:19:56.350036+00:00_

# Complete Listing of prismatic/models Directory

| Name | Path | Type |
|------|------|------|
| __init__.py | prismatic/models/__init__.py | file |
| action_heads.py | prismatic/models/action_heads.py | file |
| backbones | prismatic/models/backbones | dir |
| film_vit_wrapper.py | prismatic/models/film_vit_wrapper.py | file |
| load.py | prismatic/models/load.py | file |
| materialize.py | prismatic/models/materialize.py | file |
| projectors.py | prismatic/models/projectors.py | file |
| registry.py | prismatic/models/registry.py | file |
| vlas | prismatic/models/vlas | dir |
| vlms | prismatic/models/vlms | dir |

The directory contains 7 Python files and 3 subdirectories within the openvla-oft repository's model components section.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_openvla-oft-survey_20260520T040517",
  "tool": "WebFetch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 89 · 2026-05-20T04:19:56.350149+00:00_

# Complete File and Directory Listing

| Name | Path | Type |
|------|------|------|
| `__init__.py` | `prismatic/preprocessing/__init__.py` | file |
| `datasets` | `prismatic/preprocessing/datasets` | directory |
| `download.py` | `prismatic/preprocessing/download.py` | file |
| `materialize.py` | `prismatic/preprocessing/materialize.py` | file |

The listing contains four entries within the `prismatic/preprocessing` module of the openvla-oft repository. Three are Python files and one is a subdirectory.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_openvla-oft-survey_20260520T040517",
  "tool": "WebFetch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 90 · 2026-05-20T04:19:56.350268+00:00_

# Summary of finetune.py

This Python script implements fine-tuning for OpenVLA (a vision-language-action model) using Low-Rank Adaptation (LoRA). Here are the key components:

## Core Configuration
The `FinetuneConfig` dataclass defines hyperparameters including model path, dataset selection, batch size, learning rate, and checkpoint management preferences.

## Main Functions

**Model Setup:**
- `init_module()` - Initializes modules, optionally loads checkpoints, and wraps with DDP
- `wrap_ddp()` - Wraps modules with DistributedDataParallel for multi-GPU training
- `load_checkpoint()` - Loads saved model state dictionaries
- `remove_ddp_in_checkpoint()` - Removes "module." prefixes from DDP-saved weights

**Training Loop:**
- `run_forward_pass()` - Executes model inference and computes loss/metrics for both L1 regression and diffusion-based action prediction
- `run_diffusion_sampling()` - Implements reverse diffusion process to generate actions
- `compute_smoothened_metrics()` - Averages metrics across recent batches

**Checkpoint & Logging:**
- `save_training_checkpoint()` - Persists model components, LoRA adapters, and dataset statistics
- `log_metrics_to_wandb()` - Uploads training metrics to Weights & Biases
- `run_validation()` - Evaluates model on validation set
- `get_run_id()` - Generates descriptive experiment identifiers

## Key Features

The script supports multiple training paradigms: discrete token prediction, continuous L1 regression, and diffusion-based action modeling. It accommodates optional inputs like proprioceptive state and multi-image inputs, integrates FiLM for language conditioning, and implements learning rate warmup/decay schedules with gradient accumulation.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_openvla-oft-survey_20260520T040517",
  "tool": "WebFetch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool call

_source line 91 · 2026-05-20T04:19:56.350405+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://arxiv.org/abs/2512.11891",
  "prompt": "I need the full paper details. What VLA backbone does VLSA/AEGIS use? How exactly do they implement the control barrier function safety layer? What is the architecture diagram? Do they modify the action head? What is the action space? How is SafeLIBERO data formatted for training? What observations do they use (RGB images, depth, proprioception)? Provide all technical details available."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_openvla-oft-survey_20260520T040517",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://arxiv.org/abs/2512.11891",
    "prompt": "I need the full paper details. What VLA backbone does VLSA/AEGIS use? How exactly do they implement the control barrier function safety layer? What is the architecture diagram? Do they modify the action head? What is the action space? How is SafeLIBERO data formatted for training? What observations do they use (RGB images, depth, proprioception)? Provide all technical details available."
  }
}
```

</details>

---

### Tool call

_source line 92 · 2026-05-20T04:19:56.350529+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://openreview.net/forum?id=dt940loCBT",
  "prompt": "Extract all details about SafeVLA: What is their approach to safety alignment of VLA models? Do they use occupancy maps or predictions? What is the architecture? How do they define safety constraints? What datasets do they use? What VLA backbone? What are the key results? How does it compare to VLSA-AEGIS?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_openvla-oft-survey_20260520T040517",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://openreview.net/forum?id=dt940loCBT",
    "prompt": "Extract all details about SafeVLA: What is their approach to safety alignment of VLA models? Do they use occupancy maps or predictions? What is the architecture? How do they define safety constraints? What datasets do they use? What VLA backbone? What are the key results? How does it compare to VLSA-AEGIS?"
  }
}
```

</details>

---

### Tool call

_source line 93 · 2026-05-20T04:19:56.350651+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://arxiv.org/pdf/2601.21712",
  "prompt": "Extract details about CoFreeVLA: How do they estimate collision risk? Do they use occupancy maps or 3D representations? What is the self-collision risk estimator architecture? How does it integrate with the VLA model? What VLA backbone do they use?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_openvla-oft-survey_20260520T040517",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://arxiv.org/pdf/2601.21712",
    "prompt": "Extract details about CoFreeVLA: How do they estimate collision risk? Do they use occupancy maps or 3D representations? What is the self-collision risk estimator architecture? How does it integrate with the VLA model? What VLA backbone do they use?"
  }
}
```

</details>

---

### Tool call

_source line 94 · 2026-05-20T04:19:56.350798+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://raw.githubusercontent.com/moojink/openvla-oft/main/prismatic/models/action_heads.py",
  "prompt": "Return the COMPLETE file content exactly as-is. Every line of code, every import, every class, every function, every comment. Do not summarize."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_openvla-oft-survey_20260520T040517",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://raw.githubusercontent.com/moojink/openvla-oft/main/prismatic/models/action_heads.py",
    "prompt": "Return the COMPLETE file content exactly as-is. Every line of code, every import, every class, every function, every comment. Do not summarize."
  }
}
```

</details>

---

### Tool call

_source line 95 · 2026-05-20T04:19:56.350921+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://api.github.com/repos/moojink/openvla-oft/contents/prismatic/models/vlas",
  "prompt": "Return the complete listing of all files and directories. Include name, path, type for every entry."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_openvla-oft-survey_20260520T040517",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://api.github.com/repos/moojink/openvla-oft/contents/prismatic/models/vlas",
    "prompt": "Return the complete listing of all files and directories. Include name, path, type for every entry."
  }
}
```

</details>

---

### Tool call

_source line 96 · 2026-05-20T04:19:56.351062+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://api.github.com/repos/moojink/openvla-oft/contents/prismatic/vla/datasets",
  "prompt": "Return the complete listing of all files and directories. Include name, path, type for every entry."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_openvla-oft-survey_20260520T040517",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://api.github.com/repos/moojink/openvla-oft/contents/prismatic/vla/datasets",
    "prompt": "Return the complete listing of all files and directories. Include name, path, type for every entry."
  }
}
```

</details>

---

### Tool result

_source line 97 · 2026-05-20T04:19:56.351180+00:00_

# VLSA/AEGIS Paper Details

Based on the abstract and metadata provided, I can only share limited information from this web page excerpt:

## Available Information

**Core Contribution:** The paper introduces a "plug-and-play safety constraint (SC) layer formulated via control barrier functions" that integrates with existing VLA models.

**Performance Claims:** The method achieves "59.16% improvement in obstacle avoidance rate while substantially increasing the task execution success rate by 17.25%."

**Benchmark:** They created SafeLIBERO, described as a "comprehensive safety-critical benchmark...spanning distinct manipulation scenarios characterized by varying degrees of spatial complexity and obstacle intervention."

## Missing Technical Details

Unfortunately, the webpage excerpt does **not contain**:
- VLA backbone architecture specifications
- Control barrier function implementation details
- System architecture diagrams
- Action head modifications
- Action space definitions
- SafeLIBERO data format specifications
- Input modality details (RGB, depth, proprioception)
- Training procedures

## Access Full Paper

To obtain these technical specifications, you would need to:
- Access the full PDF via the arXiv link provided
- Review the HTML version
- Consult the authors' GitHub repository at vlsa-aegis.github.io (mentioned in the abstract)

The webpage excerpt functions as a landing page rather than a detailed technical summary.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_openvla-oft-survey_20260520T040517",
  "tool": "WebFetch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 98 · 2026-05-20T04:19:56.351304+00:00_

# SafeVLA: Safety Alignment for Vision-Language-Action Models

Based on the webpage content provided, here's what can be determined:

## Approach to Safety Alignment
SafeVLA uses an **Integrated Safety Approach (ISA)** that systematically:
1. Models safety requirements
2. Elicits diverse unsafe behaviors
3. Constrains VLA policies via safe reinforcement learning
4. Assures safety through targeted evaluations

The methodology leverages the constrained Markov decision process (CMDP) paradigm, optimizing "from a min-max perspective against elicited safety risks."

## Architecture & Technical Details
The webpage does not provide information regarding:
- Occupancy map usage or predictions
- Specific architecture details
- How safety constraints are formally defined
- Dataset specifications
- VLA backbone architecture

## Key Results
The approach achieves notable improvements:
- **83.58% reduction** in cumulative safety violation costs compared to state-of-the-art
- **3.85% improvement** in task success rate maintenance
- Strong generalization to out-of-distribution perturbations
- Effective mitigation of long-tail risks and extreme failure scenarios

## Comparison to VLSA-AEGIS
The page does not mention VLSA-AEGIS or provide comparative analysis with other methods beyond a generic "state-of-the-art" reference.

The paper was published at NeurIPS 2025 as a spotlight presentation.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_openvla-oft-survey_20260520T040517",
  "tool": "WebFetch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 99 · 2026-05-20T04:19:56.351434+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://github.com/moojink/openvla-oft",
  "prompt": "Extract all details about OpenVLA-OFT: What is the training procedure? What data format does it expect (RLDS, HDF5, etc.)? How does LIBERO data get converted for training? What is the action space (continuous, discrete, chunk size)? What is the model architecture modification (parallel decoding, action chunking details)? What are the key hyperparameters for LIBERO fine-tuning? How would someone add a custom dataset?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_openvla-oft-survey_20260520T040517",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://github.com/moojink/openvla-oft",
    "prompt": "Extract all details about OpenVLA-OFT: What is the training procedure? What data format does it expect (RLDS, HDF5, etc.)? How does LIBERO data get converted for training? What is the action space (continuous, discrete, chunk size)? What is the model architecture modification (parallel decoding, action chunking details)? What are the key hyperparameters for LIBERO fine-tuning? How would someone add a custom dataset?"
  }
}
```

</details>

---

### Tool result

_source line 100 · 2026-05-20T04:19:56.351586+00:00_

# Technical Details Extraction: Fine-Tuning Vision-Language-Action Models

## 1. ARCHITECTURE

**Base Model:**
- OpenVLA: 7B-parameter manipulation policy
- Built on Prismatic VLM, fine-tuned on 1M episodes from Open X-Embodiment dataset
- Language backbone: Llama-2 7B

**Vision Encoder:**
- Fused backbone with SigLIP and DINOv2 vision transformers
- "Each vision transformer extracts 256 patch embeddings" per image
- Input resolution: 224 × 224 pixels
- Dual vision encoder projects "256 patch embeddings per view"

**Projector:**
- "3-layer MLP with GELU activation" projects visual features to language embedding space
- Robot state: "2-layer MLP with GELU activation" for proprioceptive inputs

**Original Formulation:**
- "Autoregressive prediction of 7 discrete robot action tokens per timestep"
- 3 for position, 3 for orientation, 1 for gripper

---

## 2. ACTION HEAD DESIGN

**Parallel Decoding:**
- "Replaces causal attention mask with bidirectional attention"
- "Maps input embeddings to predicted output sequence in single forward pass"
- Uses "empty action embeddings" with positional encodings only

**Action Chunking:**
- OpenVLA-OFT: "chunk size K=8" for LIBERO
- ALOHA experiments: "K=25" timesteps
- "Model predicts K×D actions in one forward pass"

**Continuous Actions:**
- "256-bin discretization" in original (discrete)
- "Normalized to [-1,+1]" range
- L1 regression variant: "4-layer MLP action head with ReLU activation"
- "MLP maps final decoder layer hidden states directly to continuous action values"

**Action Dimensions:**
- Single-arm: 7-dimensional actions (delta end-effector pose + gripper)
- Bimanual ALOHA: "14-dimensional joint angles"

---

## 3. TRAINING PROCEDURE

**Data & Hyperparameters:**
- LIBERO: "500 expert demonstrations" per task suite
- Batch size: "64-128 across 8 A100/H100 GPUs"
- Training steps: "50-150K gradient steps" (non-diffusion), "100-250K" (diffusion)
- ALOHA: "batch size 32 with 8 A100/H100-80GB GPUs"
- ALOHA data: 20-300 demons
…[truncated 3613 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_openvla-oft-survey_20260520T040517",
  "tool": "WebFetch",
  "elapsed_ms": 5
}
```

</details>

---

### Tool call

_source line 101 · 2026-05-20T04:19:56.351761+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://raw.githubusercontent.com/moojink/openvla-oft/main/prismatic/conf/vla.py",
  "prompt": "Return the COMPLETE file content exactly as-is. Every line, every class, every field, every default value. Do not summarize."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_openvla-oft-survey_20260520T040517",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://raw.githubusercontent.com/moojink/openvla-oft/main/prismatic/conf/vla.py",
    "prompt": "Return the COMPLETE file content exactly as-is. Every line, every class, every field, every default value. Do not summarize."
  }
}
```

</details>

---

### Tool result

_source line 102 · 2026-05-20T04:19:56.351882+00:00_

# File Listing

Based on the provided content, here are all entries in the `prismatic/models/vlas/` directory:

| Name | Path | Type |
|------|------|------|
| `__init__.py` | `prismatic/models/vlas/__init__.py` | file |
| `openvla.py` | `prismatic/models/vlas/openvla.py` | file |

The directory contains two Python files: an initialization module (29 bytes) and the main OpenVLA implementation module (5,830 bytes).

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_openvla-oft-survey_20260520T040517",
  "tool": "WebFetch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 103 · 2026-05-20T04:19:56.352009+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://raw.githubusercontent.com/moojink/openvla-oft/main/prismatic/models/load.py",
  "prompt": "Return the COMPLETE file content exactly as-is. Every line of code, every import, every function. Do not summarize."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_openvla-oft-survey_20260520T040517",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://raw.githubusercontent.com/moojink/openvla-oft/main/prismatic/models/load.py",
    "prompt": "Return the COMPLETE file content exactly as-is. Every line of code, every import, every function. Do not summarize."
  }
}
```

</details>

---

### Tool result

_source line 104 · 2026-05-20T04:19:56.352133+00:00_

# File and Directory Listing

| Name | Path | Type |
|------|------|------|
| __init__.py | prismatic/vla/datasets/__init__.py | file |
| datasets.py | prismatic/vla/datasets/datasets.py | file |
| rlds | prismatic/vla/datasets/rlds | dir |

The listing contains two Python files and one subdirectory within the datasets module of the openvla-oft repository.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_openvla-oft-survey_20260520T040517",
  "tool": "WebFetch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 105 · 2026-05-20T04:19:56.352249+00:00_

# CoFreeVLA: Collision Risk Estimation Details

Based on the PDF content, here are the key technical details about CoFreeVLA's approach:

## Collision Risk Estimation Method

CoFreeVLA employs a dual-arm manipulation system that estimates collision risk through **risk assessment mechanisms** rather than explicit occupancy maps. The system is designed to prevent collisions between the two robotic arms and with the environment during coordinated manipulation tasks.

## Self-Collision Risk Estimator Architecture

The paper references several collision detection libraries for their implementation:
- **FCL (Flexible Collision Library)** for collision checking
- **MoveIt OMPL** for collision-aware motion planning
- **MoveIt Planning Scene** for self-collision detection

These are integrated as comparison baselines, suggesting CoFreeVLA develops its own risk estimation approach that predicts collision likelihood rather than performing discrete collision checks.

## Integration with VLA Model

The risk estimator operates as a **post-processing or filtering mechanism** alongside the Vision-Language-Action model predictions. This architecture allows the system to modify action outputs from the VLA to ensure collision-free trajectories.

## VLA Backbone

While the PDF content doesn't explicitly detail the specific VLA backbone used, the document references several foundational VLA systems in its citations:
- RT-1 and RT-2 (Brohan et al., 2024)
- PaLM-E (Driess et al., 2023)
- OpenVLA (Kim et al., 2024)

The approach appears to build upon these existing vision-language-action frameworks with added collision-avoidance capabilities.

[Binary content (application/pdf, 9.2MB) also saved to /home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0513-projects-occsafe-vla/e6a054d2-15f2-4fc6-bb3d-45722340f919/tool-results/webfetch-1779250082986-c308ti.pdf]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_openvla-oft-survey_20260520T040517",
  "tool": "WebFetch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 106 · 2026-05-20T04:19:56.352373+00:00_

# OpenVLA-OFT: Technical Details Analysis

Based on the provided webpage content, I can only extract limited technical information:

## Available Information

**Project Overview:**
The repository describes itself as addressing "Fine-Tuning Vision-Language-Action Models: Optimizing Speed and Success" with a focus on robotics applications.

**System Requirements:**
- Inference requires 1 GPU with ~16-18 GB VRAM depending on the task (LIBERO simulation or ALOHA robot)
- Training needs 1-8 GPUs with 27-80 GB capacity, varying by setup configuration

**Key Components Mentioned:**
The codebase references several modules: action heads, processors, proprio projectors, and VLA (Vision-Language-Action) models that generate "action chunks" from observations.

**Supported Benchmarks:**
Two main evaluation frameworks are documented: LIBERO simulation tasks and real-world ALOHA robot experiments.

## Information Not Available

The webpage content **does not include**:
- Specific training procedures or hyperparameters
- Data format specifications (RLDS, HDF5, etc.)
- LIBERO data conversion methodology
- Action space details (continuous vs. discrete definitions)
- Model architecture modifications
- Custom dataset integration instructions

**For these technical details**, you would need to consult the referenced documentation files (SETUP.md, LIBERO.md, ALOHA.md) or the full paper at arxiv.org/abs/2502.19645, which aren't included in this excerpt.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_openvla-oft-survey_20260520T040517",
  "tool": "WebFetch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 107 · 2026-05-20T04:19:56.352500+00:00_

# VLA Configuration File Analysis

This Python module defines dataclass configurations for Vision Language Action (VLA) models used in robotics training. Here's what it contains:

## Core Structure

The file establishes a `VLAConfig` base dataclass with parameters controlling:
- **Model Selection**: Base VLM specification (e.g., SigLIP, DINO-SigLIP)
- **Architecture**: Vision/LLM backbone freezing options
- **Training Data**: Dataset mixtures (Bridge, OXE Magic Soup, T-DROID)
- **Optimization**: Learning rates, batch sizes, gradient checkpointing settings
- **Hardware**: GPU world size expectations and distributed training configuration

## Configuration Variants

The module includes approximately 13 experiment configurations organized by purpose:

**Pre-training experiments** use 8-64 GPU setups with datasets like Bridge and OXE Magic Soup variants.

**Fine-tuning experiments** target specific robotic tasks (carrot placement, pouring) with various backbone-freezing strategies labeled "Icy" (frozen vision), "Last Layer" (frozen LLM except final layer), and "Sandwich" (frozen LLM with unfrozen final layer).

## Registration System

A `VLARegistry` enum provides centralized access to all configurations, automatically registering each variant in the `VLAConfig` choice registry for easy lookup and validation. The registration mechanism enables users to reference configurations by human-readable names rather than direct class instantiation.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_openvla-oft-survey_20260520T040517",
  "tool": "WebFetch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 108 · 2026-05-20T04:19:56.352621+00:00_

# Summary of load.py

This Python module serves as the entry point for loading pretrained Vision-Language Models (VLMs) and Vision-Language-Action (VLA) models for inference.

## Key Functions

**`available_models()`** - Returns a list of registered model IDs from the MODEL_REGISTRY.

**`available_model_names()`** - Returns items from the GLOBAL_REGISTRY containing human-readable model names.

**`get_model_description(model_id_or_name)`** - Retrieves and displays the description for a specified model.

**`load(model_id_or_path, hf_token, cache_dir, load_for_training)`** - Loads a pretrained PrismaticVLM either from local disk or HuggingFace Hub. The function handles configuration loading, vision and language backbone initialization, and model instantiation from checkpoints.

**`load_vla(model_id_or_path, hf_token, cache_dir, load_for_training, step_to_load, model_type)`** - Loads a pretrained OpenVLA model with similar flexibility as the VLM loader, plus additional features for checkpoint step selection and dataset statistics loading for action denormalization.

## Key Features

- Supports both local filesystem and HuggingFace Hub model sources
- Configurable inference versus training modes
- Comprehensive logging via the Overwatch system
- Validates required configuration and checkpoint files before loading
- Handles vision backbone, LLM backbone, and model architecture assembly

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_openvla-oft-survey_20260520T040517",
  "tool": "WebFetch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 109 · 2026-05-20T04:19:56.352773+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://arxiv.org/pdf/2512.11891",
  "prompt": "Extract ALL technical details: 1) What VLA backbone is VLSA/AEGIS built on? 2) How exactly does the control barrier function (CBF) safety constraint layer work? What is the mathematical formulation? 3) What is the architecture - how is the SC layer connected to the VLA? 4) What observations/inputs does the model take? 5) What is the action space? 6) How is SafeLIBERO data structured - what fields, what format? 7) Do they use any occupancy or spatial representation? 8) How do they detect obstacles? 9) What is the training procedure? 10) What baselines do they compare against?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_openvla-oft-survey_20260520T040517",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://arxiv.org/pdf/2512.11891",
    "prompt": "Extract ALL technical details: 1) What VLA backbone is VLSA/AEGIS built on? 2) How exactly does the control barrier function (CBF) safety constraint layer work? What is the mathematical formulation? 3) What is the architecture - how is the SC layer connected to the VLA? 4) What observations/inputs does the model take? 5) What is the action space? 6) How is SafeLIBERO data structured - what fields, what format? 7) Do they use any occupancy or spatial representation? 8) How do they detect obstacles? 9) What is the training procedure? 10) What baselines do they compare against?"
  }
}
```

</details>

---

### Tool result

_source line 110 · 2026-05-20T04:19:56.352907+00:00_

maxContentLength size of 10485760 exceeded

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_openvla-oft-survey_20260520T040517",
  "tool": "WebFetch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 111 · 2026-05-20T04:19:56.353031+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://openvla-oft.github.io/",
  "prompt": "Extract technical details about OpenVLA-OFT: What architectural changes were made (parallel decoding, action chunking, continuous actions)? What is the action representation? How does it differ from base OpenVLA? What is the training data format? What LIBERO results did they achieve?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_openvla-oft-survey_20260520T040517",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://openvla-oft.github.io/",
    "prompt": "Extract technical details about OpenVLA-OFT: What architectural changes were made (parallel decoding, action chunking, continuous actions)? What is the action representation? How does it differ from base OpenVLA? What is the training data format? What LIBERO results did they achieve?"
  }
}
```

</details>

---

### Tool call

_source line 112 · 2026-05-20T04:19:56.353159+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://arxiv.org/html/2502.19645",
  "prompt": "I need SPECIFIC training hyperparameters that I may have missed. Please look very carefully through the paper for:\n\n1. OPTIMIZER: Is it AdamW? Adam? What are the beta values?\n2. LEARNING RATE: Exact learning rate value (e.g., 2e-5, 5e-4)? Any learning rate schedule (cosine, linear decay)?\n3. WARMUP: Number of warmup steps?\n4. WEIGHT DECAY: Value?\n5. LoRA RANK: What rank is used for LoRA? Alpha value?\n6. GPU HOURS: Total GPU hours for training?\n7. BATCH SIZE: Exact per-GPU batch size and gradient accumulation steps?\n8. TRAINING EPOCHS or STEPS: Exact numbers for each benchmark?\n9. DATA AUGMENTATION: Any image augmentation used?\n10. ACTION NORMALIZATION: How are actions normalized? Per-dimension statistics?\n11. LOSS FUNCTION: Exact loss formulation for L1, diffusion, MSE variants\n12. FiLM DETAILS: Exact dimensions of gamma and beta projections\n13. MLP ACTION HEAD: Exact hidden dimensions of the 4-layer MLP\n14. TOKENIZER DETAILS: How are action tokens mapped in the discrete case (256 bins)?\n\nAlso look for any appendix, supplementary material references, or hyperparameter tables. Extract EVERY number from any table you find."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_openvla-oft-survey_20260520T040517",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://arxiv.org/html/2502.19645",
    "prompt": "I need SPECIFIC training hyperparameters that I may have missed. Please look very carefully through the paper for:\n\n1. OPTIMIZER: Is it AdamW? Adam? What are the beta values?\n2. LEARNING RATE: Exact learning rate value (e.g., 2e-5, 5e-4)? Any learning rate schedule (cosine, linear decay)?\n3. WARMUP: Number of warmup steps?\n4. WEIGHT DECAY: Value?\n5. LoRA RANK: What rank is used for LoRA? Alpha value?\n6. GPU HOURS: Total GPU hours for training?\n7. BATCH SIZE: Exact per-GPU batch size and gradient accumulation steps?\n8. TRAINING EPOCHS or STEPS: Exact numbers for each benchmark?\n9. DATA AUGMENTATION: Any image augmentation used?\n10. ACTION NORMALIZATION: How are actions normalized? Per-dimension statistics?\n11. LOSS FUNCTION: Exact loss formulation for L1, diffusion, MSE variants\n12. FiLM DETAILS: Exact dimensions of gamma and beta projections\n13. MLP ACTION HEAD: Exact hidden dimensions of the 4-layer MLP\n14. TOKENIZER DETAILS: How are action tokens mapped in the discrete case (256 bins)?\n\nAlso look for any appendix, supplementary material references, or hyperparameter tables. Extract EVERY number from any table you find."
  }
}
```

</details>

---

### Tool result

_source line 113 · 2026-05-20T04:19:56.353306+00:00_

# Complete File Content

```python
"""Implementations of various action heads, which serve as alternatives to VLM sequential token prediction."""

import math

import numpy as np
import torch
import torch.nn as nn
from diffusers.schedulers.scheduling_ddim import DDIMScheduler
from prismatic.vla.constants import ACTION_DIM, ACTION_TOKEN_BEGIN_IDX, IGNORE_INDEX, NUM_ACTIONS_CHUNK, PROPRIO_DIM, STOP_INDEX


class SinusoidalPositionalEncoding(nn.Module):
    """
    Sine- and cosine-based positional encoding that produces embeddings of a batch of timesteps.

    For example, at train time, the input might be a batch of 32 randomly sampled diffusion timesteps -> shape (32,)
    Then the output would be a batch of 32 timestep embeddings -> shape (32, D)

    Adapted from: https://github.com/real-stanford/diffusion_policy/blob/main/diffusion_policy/model/diffusion/positional_embedding.py
    """

    def __init__(self, dim):
        super().__init__()
        self.dim = dim  # dimensionality of the positional encoding

    def forward(self, x):
        # x: (batch_size,)
        device = x.device
        assert self.dim % 2 == 0, f"# dimensions must be even but got {self.dim}"
        half_dim = self.dim // 2
        exponent = torch.arange(half_dim, device=device) * -math.log(10000) / (half_dim - 1)  # shape: (D/2,)
        emb = torch.exp(exponent)  # shape: (D/2,)
        emb = x[:, None] * emb[None, :]  # shape: (batch_size, 1) * (1, D/2) -> (batch_size, D/2)
        emb = torch.cat((emb.sin(), emb.cos()), dim=-1)  # shape: (batch_size, D)
        return emb


class MLPResNetBlock(nn.Module):
    """One MLP ResNet block with a residual connection."""
    def __init__(self, dim):
        super().__init__()
        self.dim = dim
        self.ffn = nn.Sequential(  # feedforward network, similar to the ones in Transformers
            nn.LayerNorm(dim),
            nn.Linear(dim, dim),
            nn.ReLU(),
        )

    def forward(self, x):
        # x: (batch_size, h
…[truncated 7091 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_openvla-oft-survey_20260520T040517",
  "tool": "WebFetch",
  "elapsed_ms": 2
}
```

</details>

---

### Tool call

_source line 114 · 2026-05-20T04:19:56.353462+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://github.com/moojink/openvla-oft/blob/main/docs/LIBERO.md",
  "prompt": "Extract all details about how to fine-tune OpenVLA-OFT on LIBERO: What data format is used? How is LIBERO data converted to RLDS? What are the training commands? What hyperparameters? What action space configuration? How many GPUs needed? How long does training take?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_openvla-oft-survey_20260520T040517",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://github.com/moojink/openvla-oft/blob/main/docs/LIBERO.md",
    "prompt": "Extract all details about how to fine-tune OpenVLA-OFT on LIBERO: What data format is used? How is LIBERO data converted to RLDS? What are the training commands? What hyperparameters? What action space configuration? How many GPUs needed? How long does training take?"
  }
}
```

</details>

---

### Tool result

_source line 115 · 2026-05-20T04:19:56.353584+00:00_

Request failed with status code 404

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_openvla-oft-survey_20260520T040517",
  "tool": "WebFetch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 116 · 2026-05-20T04:19:56.353730+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "occupancy prediction head robot manipulation transformer auxiliary task 2024 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_openvla-oft-survey_20260520T040517",
  "tool": "WebSearch",
  "tool_args": {
    "query": "occupancy prediction head robot manipulation transformer auxiliary task 2024 2025"
  }
}
```

</details>

---

### Tool call

_source line 117 · 2026-05-20T04:19:56.353862+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://arxiv.org/html/2502.19645",
  "prompt": "I need the COMPLETE LIBERO results tables. Please extract EVERY row and column from ALL tables in the paper, including:\n\n1. Table comparing decoding schemes (autoregressive vs parallel) with exact numbers\n2. Table comparing action representations (discrete vs continuous) with exact numbers  \n3. Table comparing learning objectives (token classification, MSE, L1, diffusion) with exact numbers\n4. Any table showing per-suite breakdown (LIBERO-Spatial, LIBERO-Object, LIBERO-Goal, LIBERO-Long)\n5. Any table showing ablation results\n6. Any table showing inference speed/throughput comparisons\n7. Any table showing real-robot results\n\nFor each table, give me the COMPLETE content with all rows, columns, and numbers. Do not summarize or skip any entries."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_openvla-oft-survey_20260520T040517",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://arxiv.org/html/2502.19645",
    "prompt": "I need the COMPLETE LIBERO results tables. Please extract EVERY row and column from ALL tables in the paper, including:\n\n1. Table comparing decoding schemes (autoregressive vs parallel) with exact numbers\n2. Table comparing action representations (discrete vs continuous) with exact numbers  \n3. Table comparing learning objectives (token classification, MSE, L1, diffusion) with exact numbers\n4. Any table showing per-suite breakdown (LIBERO-Spatial, LIBERO-Object, LIBERO-Goal, LIBERO-Long)\n5. Any table showing ablation results\n6. Any table showing inference speed/throughput comparisons\n7. Any table showing real-robot results\n\nFor each table, give me the COMPLETE content with all rows, columns, and numbers. Do not summarize or skip any entries."
  }
}
```

</details>

---

### Tool result

_source line 118 · 2026-05-20T04:19:56.353989+00:00_

# OpenVLA-OFT: Technical Overview

## Architectural Changes

OpenVLA-OFT incorporates three key modifications to enhance performance:

1. **Parallel Decoding & Action Chunking**: The approach combines "parallel decoding, action chunking" to achieve dramatic speed improvements—achieving "26x faster action generation speed and 3x lower latency than the base OpenVLA model."

2. **Continuous Action Representation**: Rather than discrete outputs, the model uses continuous action values optimized through L1 regression.

3. **L1 Regression Objective**: Unlike diffusion-based approaches, OpenVLA-OFT employs L1 regression, which the authors argue provides beneficial regularization by "filtering out noise in training demonstrations through their limited expressivity."

## Differentiation from Base OpenVLA

The base OpenVLA model generates actions sequentially. OpenVLA-OFT accelerates inference through parallel token generation and bundles multiple timesteps into action chunks, reducing decoding steps substantially.

## LIBERO Benchmark Results

OpenVLA-OFT achieved "SOTA results in LIBERO: 97.1% average success rate across 4 task suites," surpassing prior methods including π0, MDT, Seer, DiT Policy, Octo, and Diffusion Policy.

## Training Data Format

The document does not specify detailed training data formats, though it mentions fine-tuning uses LoRA (Low-Rank Adaptation) with vision inputs (cameras), proprioceptive state information, and language instructions as conditioning inputs.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_openvla-oft-survey_20260520T040517",
  "tool": "WebFetch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 119 · 2026-05-20T04:19:56.354137+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://raw.githubusercontent.com/moojink/openvla-oft/main/prismatic/models/vlas/openvla.py",
  "prompt": "Return the COMPLETE file content exactly as-is. Every line of code, every import, every class, every function. Do not summarize."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_openvla-oft-survey_20260520T040517",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://raw.githubusercontent.com/moojink/openvla-oft/main/prismatic/models/vlas/openvla.py",
    "prompt": "Return the COMPLETE file content exactly as-is. Every line of code, every import, every class, every function. Do not summarize."
  }
}
```

</details>

---

### Tool result

_source line 120 · 2026-05-20T04:19:56.354261+00:00_

# Training Hyperparameters from Paper

Based on careful review of the provided content, here are the specific hyperparameters found:

## Found Hyperparameters

**Batch Size & Training:**
- "batch size of 64-128 across 8 A100/H100 GPUs" for LIBERO experiments
- "total batch size 32 with 8 A100/H100-80GB GPUs" for ALOHA experiments
- Training duration: "50-150K gradient steps for non-diffusion methods and 100-250K steps for diffusion methods"

**LoRA Configuration:**
- Uses LoRA fine-tuning but specific rank and alpha values are **NOT provided** in the visible content

**Learning Rate & Optimizer:**
- **NOT specified** in the provided excerpts

**Warmup Steps:**
- **NOT specified** in the provided excerpts

**Weight Decay:**
- **NOT specified** in the provided excerpts

**Action Chunking:**
- LIBERO: K=8 timesteps
- ALOHA: K=25 timesteps

**MLP Action Head:**
- "4-layer MLP (ReLU activation)" for continuous actions, but exact hidden dimensions **NOT provided**

**Discrete Action Tokenization:**
- "256-bin discretization of normalized actions" for discrete variant

**Data Processing:**
- Checkpoint evaluation: "test checkpoints every 50K steps and report the best performance"
- Action normalization to [-1, +1] range mentioned but detailed statistics **NOT provided**

## Missing Critical Details

The appendix sections referenced (A-D, A-E) that should contain "OpenVLA-OFT Hyperparameters and Training Details" and "Baseline Methods Hyperparameters" are **not included** in the provided content.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_openvla-oft-survey_20260520T040517",
  "tool": "WebFetch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool call

_source line 121 · 2026-05-20T04:19:56.354396+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://raw.githubusercontent.com/moojink/openvla-oft/main/prismatic/vla/datasets/datasets.py",
  "prompt": "Return the COMPLETE file content exactly as-is. Every line of code, every class, every function, every comment. Do not summarize."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_openvla-oft-survey_20260520T040517",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://raw.githubusercontent.com/moojink/openvla-oft/main/prismatic/vla/datasets/datasets.py",
    "prompt": "Return the COMPLETE file content exactly as-is. Every line of code, every class, every function, every comment. Do not summarize."
  }
}
```

</details>

---

### Tool call

_source line 122 · 2026-05-20T04:19:56.354522+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://raw.githubusercontent.com/moojink/openvla-oft/main/prismatic/vla/constants.py",
  "prompt": "Return the COMPLETE file content exactly as-is, verbatim. Every constant, every value, every comment. Do not summarize."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_openvla-oft-survey_20260520T040517",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://raw.githubusercontent.com/moojink/openvla-oft/main/prismatic/vla/constants.py",
    "prompt": "Return the COMPLETE file content exactly as-is, verbatim. Every constant, every value, every comment. Do not summarize."
  }
}
```

</details>

---

### Tool call

_source line 123 · 2026-05-20T04:19:56.354646+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://api.github.com/repos/moojink/openvla-oft/contents/prismatic/vla/datasets/rlds",
  "prompt": "Return the complete listing of all files and directories. Include name, path, type for every entry."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_openvla-oft-survey_20260520T040517",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://api.github.com/repos/moojink/openvla-oft/contents/prismatic/vla/datasets/rlds",
    "prompt": "Return the complete listing of all files and directories. Include name, path, type for every entry."
  }
}
```

</details>

---

### Tool result

_source line 124 · 2026-05-20T04:19:56.354791+00:00_

I've reviewed the provided paper content. Here's what I found regarding the complete LIBERO results tables:

## Available LIBERO Tables

**TABLE I: LIBERO Task Performance Results** (the main comprehensive table)
This table contains results across four task suites with success rates (SR %) for:
- Spatial, Object, Goal, Long, and Average columns
- Multiple method rows including baselines and OpenVLA variants

**TABLE II: LIBERO Inference Efficiency Results**
Shows "throughput (Hz) and latency (Sec) for 7-dimensional actions" with comparisons across OpenVLA variants including parallel decoding, action chunking, and different learning objectives.

## Key Limitation

The paper does not appear to contain separate tables breaking down individual design choices in isolation (autoregressive vs. parallel, discrete vs. continuous, or learning objectives independently). Instead, the research presents:

1. "Combined results where OpenVLA + PD&AC shows 90.2% average success rate"
2. "Comparisons of discrete versus continuous action variants showing 5% absolute improvement"
3. "Diffusion variants achieving 95.4% versus L1 regression at 95.3%"

Rather than isolated ablation tables, these comparisons are embedded within Table I's rows comparing full method combinations (e.g., "OpenVLA + PD&AC, Cont-Diffusion").

**Note:** The complete numerical data from Tables I and II appears in the provided excerpt, but the paper does not contain separate tables exclusively comparing single design dimensions in isolation.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_openvla-oft-survey_20260520T040517",
  "tool": "WebFetch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 125 · 2026-05-20T04:19:56.354944+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://raw.githubusercontent.com/moojink/openvla-oft/main/prismatic/models/projectors.py",
  "prompt": "Return the COMPLETE file content exactly as-is. Every line of code, every class, every function. Do not summarize."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_openvla-oft-survey_20260520T040517",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://raw.githubusercontent.com/moojink/openvla-oft/main/prismatic/models/projectors.py",
    "prompt": "Return the COMPLETE file content exactly as-is. Every line of code, every class, every function. Do not summarize."
  }
}
```

</details>

---

### Tool result

_source line 126 · 2026-05-20T04:19:56.355068+00:00_

# OpenVLA Module Overview

The provided code defines **OpenVLA**, a lightweight wrapper around PrismaticVLM for vision-language-action (VLA) inference in robotic control systems.

## Key Components

**Class Structure:**
OpenVLA inherits from PrismaticVLM and adds two critical attributes:
- `norm_stats`: Dictionary containing normalization statistics for action un-normalization
- `action_tokenizer`: ActionTokenizer instance for converting token IDs to continuous actions

**Core Inference Method:**
The `predict_action()` function orchestrates the complete inference pipeline:
1. Constructs a prompt combining the task instruction with vision-language context
2. Tokenizes the prompt text using LlamaTokenizerFast
3. Preprocesses the input image through the vision backbone
4. Generates action tokens via the language model
5. Decodes tokens to normalized actions
6. Un-normalizes actions using dataset-specific statistics (q01 and q99 quantiles)

**Utility Methods:**
- `_check_unnorm_key()`: Validates dataset selection when multiple datasets were used during training
- `get_action_dim()`: Returns the action space dimensionality for a given dataset
- `get_action_stats()`: Retrieves normalization statistics

**Notable Implementation Details:**
The code includes special handling for LlamaTokenizerFast to insert an empty token (ID 29871) matching training-time formatting, and uses mixed-precision inference via torch.autocast for computational efficiency.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_openvla-oft-survey_20260520T040517",
  "tool": "WebFetch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 127 · 2026-05-20T04:19:56.355202+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://raw.githubusercontent.com/moojink/openvla-oft/main/prismatic/models/film_vit_wrapper.py",
  "prompt": "Return the COMPLETE file content exactly as-is. Every line of code, class, function. Do not summarize."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_openvla-oft-survey_20260520T040517",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://raw.githubusercontent.com/moojink/openvla-oft/main/prismatic/models/film_vit_wrapper.py",
    "prompt": "Return the COMPLETE file content exactly as-is. Every line of code, class, function. Do not summarize."
  }
}
```

</details>

---

### Tool result

_source line 128 · 2026-05-20T04:19:56.355328+00:00_

Web search results for query: "occupancy prediction head robot manipulation transformer auxiliary task 2024 2025"

Links: [{"title":"Humanoid Occupancy: Enabling A Generalized Multimodal Occupancy Perception System on Humanoid Robots","url":"https://arxiv.org/html/2507.20217v2"},{"title":"OccTransformer: Improving BEVFormer for 3D camera-only occupancy   prediction","url":"https://arxiv.org/pdf/2402.18140"},{"title":"OPUS: Occupancy Prediction Using a Sparse Set","url":"https://arxiv.org/pdf/2409.09350"},{"title":"ProxMaP: Proximal Occupancy Map Prediction for Efficient Indoor Robot   Navigation","url":"https://arxiv.org/pdf/2203.04177"},{"title":"Occupancy World Model for Robots","url":"https://arxiv.org/pdf/2505.05512"},{"title":"Occupancy prediction using forward-backward view transformation","url":"https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/12515706"},{"title":"Instruction-driven history-aware policies for robotic manipulations","url":"https://arxiv.org/pdf/2209.04899"}]

Based on the search results, here's what I found regarding occupancy prediction, robot manipulation, transformers, and auxiliary tasks:

## Recent Research on Occupancy Prediction for Robotics

Recent research has begun to adapt occupancy networks for robotic platforms, integrating RGB, depth, and LiDAR sensors to construct unified occupancy grids, with research from 2024-2025 developing annotation pipelines for dynamic scenes and designing fusion networks that leverage temporal and semantic cues. These efforts aim to provide holistic environmental understanding for manipulation, obstacle avoidance, and autonomous navigation.

## Transformer-Based Approaches

OPUS utilizes a transformer encoder-decoder architecture to simultaneously predict occupied locations and classes using a set of learnable queries. Additionally, several transformer-based approaches with sparse queries have emerged, including OccupancyDETR which conducts object detection followed by assigning each obj
…[truncated 1027 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_openvla-oft-survey_20260520T040517",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 129 · 2026-05-20T04:19:56.355469+00:00_

# VLA Constants Configuration File

This Python module establishes training and evaluation parameters for Vision Language Action (VLA) models across multiple robot platforms.

## Key Components

**Token Constants:**
The file defines Llama 2 token values including `IGNORE_INDEX = -100`, `ACTION_TOKEN_BEGIN_IDX = 31743`, and `STOP_INDEX = 2`.

**Normalization Schemes:**
Three approaches are supported through the `NormalizationType` enum: "normal" (zero mean, unit variance), "bounds" (scaled to [-1, 1]), and "bounds_q99" (quantile-based scaling).

**Platform-Specific Constants:**
The configuration maintains separate parameter sets for three robot platforms:

- **LIBERO**: 8-action chunks, 7-dimensional actions, 8-dimensional proprioception
- **ALOHA**: 25-action chunks, 14-dimensional actions and proprioception  
- **BRIDGE**: 5-action chunks, 7-dimensional actions and proprioception

**Automatic Detection:**
The `detect_robot_platform()` function examines command-line arguments to identify which platform is being used, defaulting to LIBERO if no match is found. The appropriate constants are then assigned as module-level variables and displayed for verification.

This design enables seamless adaptation to different robotic systems without manual constant adjustment.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_openvla-oft-survey_20260520T040517",
  "tool": "WebFetch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 130 · 2026-05-20T04:19:56.355591+00:00_

# Complete Listing of Files and Directories

| Name | Path | Type |
|------|------|------|
| `__init__.py` | `prismatic/vla/datasets/rlds/__init__.py` | file |
| `dataset.py` | `prismatic/vla/datasets/rlds/dataset.py` | file |
| `obs_transforms.py` | `prismatic/vla/datasets/rlds/obs_transforms.py` | file |
| `oxe` | `prismatic/vla/datasets/rlds/oxe` | directory |
| `traj_transforms.py` | `prismatic/vla/datasets/rlds/traj_transforms.py` | file |
| `utils` | `prismatic/vla/datasets/rlds/utils` | directory |

This directory structure contains Python modules for RLDS (Robotics Learning Dataset Standard) dataset handling within the OpenVLA project, including initialization, dataset management, observation and trajectory transformations, plus subdirectories for Open X-Embodiment (oxe) data and utility functions.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_openvla-oft-survey_20260520T040517",
  "tool": "WebFetch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 131 · 2026-05-20T04:19:56.355744+00:00_

# Complete File Content

```python
"""Implementation of additional projectors for additional inputs to the VLA models."""
import torch
import torch.nn as nn


class ProprioProjector(nn.Module):
    """
    Projects proprio state inputs into the LLM's embedding space.
    """
    def __init__(self, llm_dim: int, proprio_dim: int) -> None:
        super().__init__()
        self.llm_dim = llm_dim
        self.proprio_dim = proprio_dim

        self.fc1 = nn.Linear(self.proprio_dim, self.llm_dim, bias=True)
        self.fc2 = nn.Linear(self.llm_dim, self.llm_dim, bias=True)
        self.act_fn1 = nn.GELU()

    def forward(self, proprio: torch.Tensor = None) -> torch.Tensor:
        # proprio: (bsz, proprio_dim)
        projected_features = self.fc1(proprio)
        projected_features = self.act_fn1(projected_features)
        projected_features = self.fc2(projected_features)
        return projected_features


class NoisyActionProjector(nn.Module):
    """
    [Diffusion] Projects noisy action inputs into the LLM's embedding space.

    Note that since each action is tokenized into 7 tokens in OpenVLA (rather
    than having 1 token per action), each noisy action token will have dimension 1
    instead of 7.
    """
    def __init__(self, llm_dim: int) -> None:
        super().__init__()
        self.llm_dim = llm_dim
        self.action_token_dim = 1

        self.fc1 = nn.Linear(self.action_token_dim, self.llm_dim, bias=True)
        self.fc2 = nn.Linear(self.llm_dim, self.llm_dim, bias=True)
        self.act_fn1 = nn.GELU()

    def forward(self, noisy_actions: torch.Tensor = None) -> torch.Tensor:
        # noisy_actions: (bsz, num_action_tokens=chunk_len*action_dim, 1)
        projected_features = self.fc1(noisy_actions)
        projected_features = self.act_fn1(projected_features)
        projected_features = self.fc2(projected_features)
        return projected_features
```

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_openvla-oft-survey_20260520T040517",
  "tool": "WebFetch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 132 · 2026-05-20T04:19:56.355887+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://arxiv.org/abs/2505.05512",
  "prompt": "Extract details about this Occupancy World Model for Robots paper: How do they use occupancy prediction for robot control? Is it applied to manipulation? What is the architecture? Do they combine occupancy with VLA or policy models? What are the key contributions?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_openvla-oft-survey_20260520T040517",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://arxiv.org/abs/2505.05512",
    "prompt": "Extract details about this Occupancy World Model for Robots paper: How do they use occupancy prediction for robot control? Is it applied to manipulation? What is the architecture? Do they combine occupancy with VLA or policy models? What are the key contributions?"
  }
}
```

</details>

---

### Tool call

_source line 133 · 2026-05-20T04:19:56.356064+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "SafeLIBERO dataset HDF5 format action space observation space robot data"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_openvla-oft-survey_20260520T040517",
  "tool": "WebSearch",
  "tool_args": {
    "query": "SafeLIBERO dataset HDF5 format action space observation space robot data"
  }
}
```

</details>

---

### Tool call

_source line 134 · 2026-05-20T04:19:56.356241+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://arxiv.org/html/2502.19645",
  "prompt": "Extract the COMPLETE content of Table I and Table II with ALL numbers. I need every single cell value. Format them as markdown tables. Also look for:\n\n1. Any other tables (Table III, Table IV, etc.)\n2. The appendix content - especially hyperparameter tables\n3. Any figures with quantitative data (bar charts with numbers)\n\nFor Table I specifically, list EVERY method name in the leftmost column and EVERY number in every cell. Do not skip or summarize any row.\n\nAlso extract any information about:\n- The \"modified dataset\" - what modifications were made\n- The \"additional inputs\" - what additional inputs (wrist camera, proprioceptive state)\n- Pre-training details of the base OpenVLA model\n- Open X-Embodiment dataset details"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_openvla-oft-survey_20260520T040517",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://arxiv.org/html/2502.19645",
    "prompt": "Extract the COMPLETE content of Table I and Table II with ALL numbers. I need every single cell value. Format them as markdown tables. Also look for:\n\n1. Any other tables (Table III, Table IV, etc.)\n2. The appendix content - especially hyperparameter tables\n3. Any figures with quantitative data (bar charts with numbers)\n\nFor Table I specifically, list EVERY method name in the leftmost column and EVERY number in every cell. Do not skip or summarize any row.\n\nAlso extract any information about:\n- The \"modified dataset\" - what modifications were made\n- The \"additional inputs\" - what additional inputs (wrist camera, proprioceptive state)\n- Pre-training details of the base OpenVLA model\n- Open X-Embodiment dataset details"
  }
}
```

</details>

---

### Tool call

_source line 135 · 2026-05-20T04:19:56.356391+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "VLSA AEGIS SafeLIBERO VLA safety control barrier function OpenVLA architecture"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_openvla-oft-survey_20260520T040517",
  "tool": "WebSearch",
  "tool_args": {
    "query": "VLSA AEGIS SafeLIBERO VLA safety control barrier function OpenVLA architecture"
  }
}
```

</details>

---

### Tool call

_source line 136 · 2026-05-20T04:19:56.356520+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "OpenVLA-OFT RLDS data format action chunking continuous action head training"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_openvla-oft-survey_20260520T040517",
  "tool": "WebSearch",
  "tool_args": {
    "query": "OpenVLA-OFT RLDS data format action chunking continuous action head training"
  }
}
```

</details>

---

### Tool call

_source line 137 · 2026-05-20T04:19:56.356647+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://arxiv.org/html/2502.19645",
  "prompt": "Focus on the APPENDIX sections. Extract all content from:\n1. Appendix A, B, C, D, E and any other appendix sections\n2. Any hyperparameter tables in the appendix\n3. Any additional experimental details\n4. LoRA rank, learning rate, optimizer settings\n5. Any implementation details not in the main text\n\nAlso look for information about:\n- How FiLM conditioning is implemented exactly\n- The projection dimensions for the robot state MLP\n- Whether there is any data augmentation\n- The exact training pipeline (frozen layers, unfrozen layers)\n- Which parts of the model are fine-tuned vs frozen"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_openvla-oft-survey_20260520T040517",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://arxiv.org/html/2502.19645",
    "prompt": "Focus on the APPENDIX sections. Extract all content from:\n1. Appendix A, B, C, D, E and any other appendix sections\n2. Any hyperparameter tables in the appendix\n3. Any additional experimental details\n4. LoRA rank, learning rate, optimizer settings\n5. Any implementation details not in the main text\n\nAlso look for information about:\n- How FiLM conditioning is implemented exactly\n- The projection dimensions for the robot state MLP\n- Whether there is any data augmentation\n- The exact training pipeline (frozen layers, unfrozen layers)\n- Which parts of the model are fine-tuned vs frozen"
  }
}
```

</details>

---

### Tool result

_source line 138 · 2026-05-20T04:19:56.356821+00:00_

# File Content Summary

This Python module defines dataset classes for wrapping RLDS (Reinforcement Learning Datasets) TFDS pipelines into PyTorch-compatible formats for the OpenVLA (Vision-Language-Action) model.

## Key Components

**RLDSBatchTransform**: A dataclass that converts RLDS batches to OpenVLA format. It handles image transformation, language instruction processing, action tokenization, and constructs chat-based prompts where humans ask "What action should the robot take to {instruction}?" and the model responds with action tokens.

**RLDSDataset**: An IterableDataset wrapper supporting multiple data sources through mixture specifications. It configures RLDS pipelines with parameters like shuffle buffer size, camera views (primary, wrist cameras), and optional image augmentations including random cropping, brightness, contrast, saturation, and hue adjustments.

**EpisodicRLDSDataset**: Extends RLDSDataset to return complete episodes as lists of steps rather than individual transitions, useful for visualization purposes.

**DummyDataset**: A standard PyTorch Dataset for testing that generates random images, actions, and instructions with expected statistics format (action quantiles at 1st and 99th percentiles).

## Processing Pipeline

The datasets handle vision-language-action alignment by combining image observations with language instructions and corresponding action sequences. Labels are masked to compute loss only on predicted action tokens using the IGNORE_INDEX constant, while the model's internal shifting mechanism handles position adjustments during forward passes.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_openvla-oft-survey_20260520T040517",
  "tool": "WebFetch",
  "elapsed_ms": 2
}
```

</details>

---

### Tool result

_source line 139 · 2026-05-20T04:19:56.356957+00:00_

# Occupancy World Model for Robots - Analysis

Based on the provided abstract, here's what the paper covers:

## Robot Control Application
The abstract does **not specify** how occupancy prediction is used for actual robot control decisions. It states the work addresses "exploration and decision of embodied agents" but provides no details on control implementation or manipulation tasks.

## Architecture Components
The paper proposes **RoboOccWorld**, featuring:

1. **Conditional Causal State Attention (CCSA)** - "utilizes camera poses of next state as conditions to guide the autoregressive transformer to adapt and understand the indoor robotics scenarios"

2. **Hybrid Spatio-Temporal Aggregation (HSTA)** - designed to "obtain the combined spatio-temporal receptive field based on multi-scale spatio-temporal windows"

## Key Contributions
- Focuses on **indoor 3D occupancy scene evolution prediction** rather than outdoor road scenes
- Restructured the OccWorld-ScanNet benchmark with local annotations
- Demonstrates superior performance on indoor 3D occupancy forecasting compared to existing methods

## Not Covered
The abstract makes **no mention** of:
- Vision Language Action (VLA) models
- Policy models
- Manipulation tasks
- Specific robot control applications

The work appears primarily focused on **scene understanding and forecasting** rather than downstream control applications.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_openvla-oft-survey_20260520T040517",
  "tool": "WebFetch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 140 · 2026-05-20T04:19:56.357100+00:00_

Web search results for query: "SafeLIBERO dataset HDF5 format action space observation space robot data"

Links: [{"title":"THURCSCT/SafeLIBERO · Datasets at Hugging Face","url":"https://huggingface.co/datasets/THURCSCT/SafeLIBERO"},{"title":"openvla/experiments/robot/libero/regenerate_libero_dataset.py at main · openvla/openvla","url":"https://github.com/openvla/openvla/blob/main/experiments/robot/libero/regenerate_libero_dataset.py"},{"title":"GitHub - openvla/openvla: OpenVLA: An open-source vision-language-action model for robotic manipulation. · GitHub","url":"https://github.com/openvla/openvla"},{"title":"Dataset - BEHAVIOR","url":"https://behavior.stanford.edu/challenge/dataset.html"},{"title":"LIBERO Benchmark: Vision-Language-Action in Robotics","url":"https://www.emergentmind.com/topics/libero"},{"title":"Render and Diffuse: Aligning Image and Action Spaces for Diffusion-based   Behaviour Cloning","url":"https://arxiv.org/pdf/2405.18196"},{"title":"Transporter network for determining robot actions","url":"https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/12427659"}]

Based on the search results, here's what I found about the SafeLIBERO dataset:

## SafeLIBERO Dataset Overview

SafeLIBERO is a benchmark designed to evaluate robotic model performance in complex, safety-critical environments. It extends each LIBERO suite by selecting four representative tasks, with each task further divided into two scenarios varying by safety level based on obstacle interference: Level I scenarios where the obstacle is positioned in close proximity to the target object, and Level II scenarios where the obstacle is located further away but obstructs the movement path.

## Dataset Format and Structure

The dataset uses **HDF5 format** for storage. The data structure includes robot qpos (joint positions) followed by object poses. Within each scenario, obstacle and object positions are randomized within a small range over 50 episodes to ensure robustness.

## Data
…[truncated 643 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_openvla-oft-survey_20260520T040517",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 141 · 2026-05-20T04:19:56.357258+00:00_

Web search results for query: "VLSA AEGIS SafeLIBERO VLA safety control barrier function OpenVLA architecture"

Links: [{"title":"VLSA: Vision-Language-Action Models with Plug-and-Play Safety Constraint Layer","url":"https://vlsa-aegis.github.io/"},{"title":"VLSA: Vision-Language-Action Models with Plug-and-Play Safety Constraint Layer [Quick Review]","url":"https://liner.com/review/vlsa-visionlanguageaction-models-with-plugandplay-safety-constraint-layer"},{"title":"(PDF) VLSA: Vision-Language-Action Models with Plug-and-Play Safety Constraint Layer","url":"https://www.researchgate.net/publication/398721287_VLSA_Vision-Language-Action_Models_with_Plug-and-Play_Safety_Constraint_Layer"},{"title":"VLSA: Vision-Language-Action Models with Plug-and-Play Safety Constraint Layer","url":"https://arxiv.org/html/2512.11891v1"},{"title":"VLSA: Vision-Language-Action Models with Plug-and-Play Safety Constraint Layer","url":"https://arxiv.org/pdf/2512.11891"},{"title":"VLSA: Vision-Language-Action Models with Plug-and-Play Safety Constraint Layer | alphaXiv","url":"https://www.alphaxiv.org/overview/2512.11891"},{"title":"[2512.11891] VLSA: Vision-Language-Action Models with Plug-and-Play Safety Constraint Layer","url":"https://arxiv.org/abs/2512.11891"},{"title":"Paper page - VLSA: Vision-Language-Action Models with Plug-and-Play Safety Constraint Layer","url":"https://huggingface.co/papers/2512.11891"},{"title":"VLSA: Vision-Language-Action Models with Plug-and-Play Safety Constraint Layer | Takara TLDR","url":"https://tldr.takara.ai/p/2512.11891"},{"title":"VLSA: Vision-Language-Action Models with Plug-and-Play Safety Constraint Layer - Paper Details","url":"https://www.chatpaper.ai/dashboard/paper/94b34e07-289d-4650-a2e6-14d20295c2de"}]

Based on the web search results, here's what I found about these topics:

## VLSA (Vision-Language-Safe Action) Architecture and AEGIS

AEGIS is a Vision-Language-Safe Action (VLSA) architecture that contains a plug-and-play safety constrai
…[truncated 1333 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_openvla-oft-survey_20260520T040517",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 142 · 2026-05-20T04:19:56.357418+00:00_

# OpenVLA-OFT Appendix Summary: Implementation Details

## Architecture Modifications

OpenVLA-OFT introduces six key architectural changes to the base model:

1. **Multi-image processing** through shared SigLIP-DINOv2 backbone
2. **Robot state encoding** via 2-layer MLP with GELU activation projecting proprioceptive data to language embedding space
3. **Attention mechanism** replacement from causal to bidirectional for parallel decoding
4. **Output layer** substitution with 4-layer MLP (ReLU) for continuous action generation
5. **Action chunking** outputs K actions instead of single timesteps
6. **FiLM modules** (OFT+ variant) using task language embeddings to modulate visual features

## FiLM Implementation Details

FiLM applies affine transformation: "modulation applies spatially-agnostically by scaling and shifting entire feature maps" rather than individual patch embeddings. Applied after self-attention and before feedforward in each vision transformer block with separate projectors per block. Initialization uses multiplication by (1+γ) to preserve pretrained representations.

## Training Specifications

**LoRA Configuration:**
- Applied to vision-language model during fine-tuning on relatively small datasets (500 demonstrations vs. 1M pretraining episodes)

**Gradient Steps:**
- Non-diffusion methods: 50-150K steps
- Diffusion methods: 100-250K steps (slower convergence)
- Batch size: 64-128 across 8 A100/H100 GPUs
- Test checkpoints: Every 50K steps, reporting best performance

## Continuous Action Representations

**L1 Regression:** 4-layer MLP with ReLU activation mapping decoder hidden states to continuous actions

**Diffusion:** 50 DDIM timesteps, squared cosine beta schedule, 4-layer noise predictor with identical MLP architecture to L1 head

## Input Processing

Each image produces 256 patch embeddings projected via 3-layer MLP with GELU activation. Robot state (14-dimensional joint angles in ALOHA setup) projects through 2-layer MLP with GELU activatio
…[truncated 259 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_openvla-oft-survey_20260520T040517",
  "tool": "WebFetch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 143 · 2026-05-20T04:19:56.357569+00:00_

Web search results for query: "OpenVLA-OFT RLDS data format action chunking continuous action head training"

Links: [{"title":"Training Data for OpenVLA | Data Requirements & Formats | Claru","url":"https://claru.ai/models/openvla"},{"title":"GitHub - dusty-nv/openvla: OpenVLA: An open-source vision-language-action model for robotic manipulation.","url":"https://github.com/dusty-nv/openvla"},{"title":"GitHub - openvla/openvla: OpenVLA: An open-source vision-language-action model for robotic manipulation.","url":"https://github.com/openvla/openvla?tab=readme-ov-file"},{"title":"README.md · moojink/openvla-7b-oft-finetuned-libero-10 at main","url":"https://huggingface.co/moojink/openvla-7b-oft-finetuned-libero-10/blob/main/README.md"},{"title":"GitHub - openvla/openvla: OpenVLA: An open-source vision-language-action model for robotic manipulation. · GitHub","url":"https://github.com/openvla/openvla"},{"title":"Fine-Tuning Vision-Language-Action Models: Optimizing Speed and Success","url":"https://arxiv.org/pdf/2502.19645"},{"title":"OpenVLA-OFT","url":"https://openvla-oft.github.io/"},{"title":"Fine-Tuning Vision-Language-Action Models: Optimizing Speed and Success","url":"https://arxiv.org/html/2502.19645v1"},{"title":"GitHub - moojink/openvla-oft: Fine-Tuning Vision-Language-Action Models: Optimizing Speed and Success · GitHub","url":"https://github.com/moojink/openvla-oft"}]

Based on the search results, here's what I found about OpenVLA-OFT with respect to RLDS data format, action chunking, and continuous action head training:

## RLDS Data Format

Data must be in RLDS format with 224x224 RGB observations, language instructions, and normalized 7-DoF actions discretized to 256 bins per dimension. Custom datasets can be converted to RLDS format which is compatible with the fine-tuning script, and the RLDS dataset and dataloader are tested more extensively since they were used for all pretraining and fine-tuning experiments.

## Action Chunking

The Optimized Fine-T
…[truncated 930 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_openvla-oft-survey_20260520T040517",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool call

_source line 144 · 2026-05-20T04:19:56.357748+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://vlsa-aegis.github.io/",
  "prompt": "Extract ALL technical details about VLSA/AEGIS: 1) What VLA backbones does it work with? 2) How does the CBF-based QP solver work? 3) How does it detect obstacles using VLMs? 4) What is the full pipeline/architecture? 5) Does it modify the VLA action head or is it purely post-processing? 6) What observations does it need? 7) How does it get obstacle positions/geometry for the CBF? 8) Does it use any 3D representation like occupancy? 9) What are the SafeLIBERO tasks and data format details? 10) What baselines were compared?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_openvla-oft-survey_20260520T040517",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://vlsa-aegis.github.io/",
    "prompt": "Extract ALL technical details about VLSA/AEGIS: 1) What VLA backbones does it work with? 2) How does the CBF-based QP solver work? 3) How does it detect obstacles using VLMs? 4) What is the full pipeline/architecture? 5) Does it modify the VLA action head or is it purely post-processing? 6) What observations does it need? 7) How does it get obstacle positions/geometry for the CBF? 8) Does it use any 3D representation like occupancy? 9) What are the SafeLIBERO tasks and data format details? 10) What baselines were compared?"
  }
}
```

</details>

---

### Tool result

_source line 145 · 2026-05-20T04:19:56.357901+00:00_

# Complete Table Extraction from "Fine-Tuning Vision-Language-Action Models"

## TABLE I: LIBERO Task Performance Results

### Section 1: Third-person image + language instruction (Modified dataset)

| Policy | Spatial SR (%) | Object SR (%) | Goal SR (%) | Long SR (%) | Average SR (%) |
|--------|---|---|---|---|---|
| Diffusion Policy (scratch) | 78.3 | 92.5 | 68.3 | 50.5 | 72.4 |
| Octo (fine-tuned) | 78.9 | 85.7 | 84.6 | 51.1 | 75.1 |
| DiT Policy (fine-tuned) | 84.2 | 96.3 | 85.4 | 63.8 | 82.4 |
| OpenVLA (fine-tuned) | 84.7 | 88.4 | 79.2 | 53.7 | 76.5 |
| OpenVLA + PD&AC | 91.3 | 92.7 | 90.5 | 86.5 | 90.2 |
| OpenVLA + PD&AC, Cont-Diffusion | 96.9 | 98.1 | 95.5 | 91.1 | 95.4 |
| OpenVLA-OFT (PD&AC, Cont-L1) | 96.2 | 98.3 | 96.2 | 90.7 | 95.3 |

### Section 2: Third-person + wrist camera + proprioceptive state + language (Original dataset)

| Policy | Spatial SR (%) | Object SR (%) | Goal SR (%) | Long SR (%) | Average SR (%) |
|--------|---|---|---|---|---|
| MDT (scratch; 2% language) | 78.5 | 87.5 | 73.5 | 64.8 | 76.1 |
| MDT (scratch; 100% language)* | 95.2 | 97.8 | – | 83.0 | – |
| Seer (scratch) | – | – | – | 78.7 | – |
| Seer (pretrained on LIBERO-90) | – | – | – | 87.7 | – |
| OpenVLA-OFT (PD&AC, Cont-L1) | 95.2 | 94.2 | 95.2 | 93.2 | 94.5 |

### Section 3: Third-person + wrist camera + proprioceptive state + language (Modified dataset)

| Policy | Spatial SR (%) | Object SR (%) | Goal SR (%) | Long SR (%) | Average SR (%) |
|--------|---|---|---|---|---|
| π0 + FAST (fine-tuned) | 96.4 | 96.8 | 88.6 | 60.2 | 85.5 |
| π0 (fine-tuned) | 96.8 | 98.8 | 95.8 | 85.2 | 94.2 |
| OpenVLA-OFT (PD&AC, Cont-L1) | 97.6 | 98.4 | 97.9 | 94.5 | 97.1 |

**Key Details:**
- "Modified training dataset" = unsuccessful demonstrations filtered out + actions with near-zero magnitude removed
- "Additional inputs" = wrist camera image + robot proprioceptive state (14-dimensional joint angles)
- PD = Parallel Decoding; AC = Action Chunking (K=8 timesteps); Cont-L1 = Continuous a
…[truncated 2451 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_openvla-oft-survey_20260520T040517",
  "tool": "WebFetch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 146 · 2026-05-20T04:19:56.358081+00:00_

# Complete File Content

```python
"""Implementation of additional modules for the VLA's vision transformer."""

from functools import partial
from typing import Any, Callable, Sequence, Tuple, Union

import torch
import torch.nn as nn
from timm.models.vision_transformer import VisionTransformer


class FiLMedVisionTransformerBlock(nn.Module):
    """
    Wrapper for ViT blocks that adds components to implement FiLM language conditioning.

    Modulates visual feature embeddings via
        x = (1 + gamma) * x + beta,
    where x is visual feature and gamma and beta are learned projections of the average language embedding.
    gamma and beta have D dimensions each, where D is the number of hidden dimensions in the ViT's features.

    NOTE #1 (Moo Jin):
    In convolutional neural architectures, the "feature" in FiLM is an entire feature map, i.e., each channel in a
    convolutional layer (so gamma and beta have C dimensions, where C is the number of channels). Therefore, FiLM's
    scaling and shifting is applied across all spatial locations for conv nets -- i.e., it is spatially agnostic.

    For vision transformer architectures, you may consider individual patch embeddings as individual "features" at first
    instinct, but this would make FiLM scaling and shifting spatially local. In order to make the modulation spatially
    global like in convolutional architectures, we should apply the scaling and shifting to each dimension of each patch
    embedding. I.e., gamma and beta should have D dimensions, where D is the number of dimensions in a visual embedding.

    NOTE #2 (Moo Jin):
    x = (1 + gamma) * x + beta is used in the original FiLM paper as opposed to x = gamma * x + beta (see section 7.2 in
    https://arxiv.org/pdf/1709.07871.pdf). Since gamma and beta are close to zero upon initialization, this leads to an
    identity transformation at the beginning of training, which minimizes perturbation to the pretrained representation.
    """

    def __in
…[truncated 10005 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_openvla-oft-survey_20260520T040517",
  "tool": "WebFetch",
  "elapsed_ms": 2
}
```

</details>

---

### Tool call

_source line 147 · 2026-05-20T04:19:56.358237+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://arxiv.org/html/2512.11891v1",
  "prompt": "Extract ALL technical details: 1) What VLA backbones were tested (OpenVLA, OpenVLA-OFT, pi0.5, etc.)? 2) How does the safety constraint layer work - is it a QP layer applied to the VLA's action output? 3) How are obstacles detected - VLM object detection pipeline? 4) How are obstacle positions/geometry obtained for the CBF constraints? 5) What is the action space (7-DoF, etc.)? 6) What observations does it use (RGB, depth, proprioception)? 7) How is SafeLIBERO structured - what are the observation/action formats in the dataset? 8) Is the SC layer trained or purely optimization-based at inference? 9) What are the mathematical formulations? 10) What are the key ablation results?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_openvla-oft-survey_20260520T040517",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://arxiv.org/html/2512.11891v1",
    "prompt": "Extract ALL technical details: 1) What VLA backbones were tested (OpenVLA, OpenVLA-OFT, pi0.5, etc.)? 2) How does the safety constraint layer work - is it a QP layer applied to the VLA's action output? 3) How are obstacles detected - VLM object detection pipeline? 4) How are obstacle positions/geometry obtained for the CBF constraints? 5) What is the action space (7-DoF, etc.)? 6) What observations does it use (RGB, depth, proprioception)? 7) How is SafeLIBERO structured - what are the observation/action formats in the dataset? 8) Is the SC layer trained or purely optimization-based at inference? 9) What are the mathematical formulations? 10) What are the key ablation results?"
  }
}
```

</details>

---

### Tool call

_source line 148 · 2026-05-20T04:19:56.358383+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://github.com/openvla/openvla/blob/main/experiments/robot/libero/regenerate_libero_dataset.py",
  "prompt": "How does this script convert LIBERO data to the format expected by OpenVLA? What is the source format (HDF5?)? What is the target format (RLDS?)? What fields are extracted (images, actions, proprioception)? What is the action space dimensionality? How are observations structured?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_openvla-oft-survey_20260520T040517",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://github.com/openvla/openvla/blob/main/experiments/robot/libero/regenerate_libero_dataset.py",
    "prompt": "How does this script convert LIBERO data to the format expected by OpenVLA? What is the source format (HDF5?)? What is the target format (RLDS?)? What fields are extracted (images, actions, proprioception)? What is the action space dimensionality? How are observations structured?"
  }
}
```

</details>

---

### Tool call

_source line 149 · 2026-05-20T04:19:56.358518+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://raw.githubusercontent.com/moojink/openvla-oft/main/prismatic/vla/datasets/rlds/dataset.py",
  "prompt": "Return the COMPLETE file content exactly as-is. Every line of code, every function, every class, every comment. Do not summarize."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_openvla-oft-survey_20260520T040517",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://raw.githubusercontent.com/moojink/openvla-oft/main/prismatic/vla/datasets/rlds/dataset.py",
    "prompt": "Return the COMPLETE file content exactly as-is. Every line of code, every function, every class, every comment. Do not summarize."
  }
}
```

</details>

---

### Tool call

_source line 150 · 2026-05-20T04:19:56.358649+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://api.github.com/repos/moojink/openvla-oft/contents/prismatic/vla/datasets/rlds/oxe",
  "prompt": "Return the complete listing of all files and directories. Include name, path, type for every entry."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_openvla-oft-survey_20260520T040517",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://api.github.com/repos/moojink/openvla-oft/contents/prismatic/vla/datasets/rlds/oxe",
    "prompt": "Return the complete listing of all files and directories. Include name, path, type for every entry."
  }
}
```

</details>

---

### Tool call

_source line 151 · 2026-05-20T04:19:56.358804+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://raw.githubusercontent.com/moojink/openvla-oft/main/prismatic/vla/action_tokenizer.py",
  "prompt": "Return the COMPLETE file content exactly as-is. Every line of code, every class, every function, every comment. Do not summarize."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_openvla-oft-survey_20260520T040517",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://raw.githubusercontent.com/moojink/openvla-oft/main/prismatic/vla/action_tokenizer.py",
    "prompt": "Return the COMPLETE file content exactly as-is. Every line of code, every class, every function, every comment. Do not summarize."
  }
}
```

</details>

---

### Tool result

_source line 152 · 2026-05-20T04:19:56.358933+00:00_

# Complete File and Directory Listing

| Name | Path | Type |
|------|------|------|
| `__init__.py` | `prismatic/vla/datasets/rlds/oxe/__init__.py` | file |
| `configs.py` | `prismatic/vla/datasets/rlds/oxe/configs.py` | file |
| `materialize.py` | `prismatic/vla/datasets/rlds/oxe/materialize.py` | file |
| `mixtures.py` | `prismatic/vla/datasets/rlds/oxe/mixtures.py` | file |
| `transforms.py` | `prismatic/vla/datasets/rlds/oxe/transforms.py` | file |
| `utils` | `prismatic/vla/datasets/rlds/oxe/utils` | directory |

The directory contains 5 Python modules and 1 subdirectory within the OpenVLA OFT repository's dataset configuration structure.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_openvla-oft-survey_20260520T040517",
  "tool": "WebFetch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 153 · 2026-05-20T04:19:56.359060+00:00_

# Dataset.py File Content

I cannot provide the complete file content as requested because doing so would exceed appropriate length constraints for this response format. However, I can confirm the file is a comprehensive Python module for configuring RLDS (Reinforcement Learning Dataset Standard) datasets.

## Key Components:

The file contains four primary functions:

1. **`make_dataset_from_rlds()`** - Loads RLDS datasets from storage, applies standardization, and extracts observations (images, depth, proprioception) into normalized format

2. **`apply_trajectory_transforms()`** - Applies trajectory-level operations including goal relabeling, chunking, and subsampling

3. **`apply_frame_transforms()`** - Handles frame-level operations like image decoding, resizing, and augmentation

4. **`make_interleaved_dataset()`** - Creates multi-dataset configurations with weighted sampling, thread allocation, and batching

The module uses TensorFlow, TensorFlow Datasets, and the `dlimp` library for dataset operations. It includes utilities for normalization, statistics computation, and parallel processing configuration.

For the exact code, I recommend accessing the original source directly or requesting specific functions you need clarified.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_openvla-oft-survey_20260520T040517",
  "tool": "WebFetch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 154 · 2026-05-20T04:19:56.359204+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://arxiv.org/html/2502.19645",
  "prompt": "Search for any remaining details I may have missed. Specifically look for:\n\n1. The EXACT learning rate used (e.g. 2e-5, 1e-4, 5e-4) - check ALL sections including appendix, footnotes, captions\n2. The EXACT LoRA rank (e.g. r=8, r=16, r=32, r=64) and alpha value\n3. The EXACT optimizer name (Adam, AdamW, SGD)\n4. Weight decay value\n5. Any mention of gradient clipping\n6. The hidden dimension of the 4-layer MLP action head (e.g. 256, 512, 1024)\n7. The embedding dimension of the language model (e.g. 4096 for Llama-2 7B)\n8. Total number of trainable parameters during fine-tuning\n9. Any mention of mixed precision training (fp16, bf16)\n10. The ALOHA per-task success rates (specific numbers for each task: fold shorts, fold shirt, scoop, place in pot, etc.)\n11. The control frequency for LIBERO (in Hz)\n12. Any references to the codebase or implementation framework (PyTorch, JAX, etc.)\n13. The exact SigLIP variant used (e.g., SigLIP-SO400M, SigLIP-B/16)\n14. The exact DINOv2 variant used (e.g., DINOv2-ViT-L/14)\n\nAlso look for any equation numbers and the key equations (loss functions, FiLM formulation, diffusion forward/reverse process)."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_openvla-oft-survey_20260520T040517",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://arxiv.org/html/2502.19645",
    "prompt": "Search for any remaining details I may have missed. Specifically look for:\n\n1. The EXACT learning rate used (e.g. 2e-5, 1e-4, 5e-4) - check ALL sections including appendix, footnotes, captions\n2. The EXACT LoRA rank (e.g. r=8, r=16, r=32, r=64) and alpha value\n3. The EXACT optimizer name (Adam, AdamW, SGD)\n4. Weight decay value\n5. Any mention of gradient clipping\n6. The hidden dimension of the 4-layer MLP action head (e.g. 256, 512, 1024)\n7. The embedding dimension of the language model (e.g. 4096 for Llama-2 7B)\n8. Total number of trainable parameters during fine-tuning\n9. Any mention of mixed precision training (fp16, bf16)\n10. The ALOHA per-task success rates (specific numbers for each task: fold shorts, fold shirt, scoop, place in pot, etc.)\n11. The control frequency for LIBERO (in Hz)\n12. Any references to the codebase or implementation framework (PyTorch, JAX, etc.)\n13. The exact SigLIP variant used (e.g., SigLIP-SO400M, SigLIP-B/16)\n14. The exact DINOv2 variant used (e.g., DINOv2-ViT-L/14)\n\nAlso look for any equation numbers and the key equations (loss functions, FiLM formulation, diffusion forward/reverse process)."
  }
}
```

</details>

---

### Tool result

_source line 155 · 2026-05-20T04:19:56.359341+00:00_

# LIBERO Data Conversion for OpenVLA

Based on the script, here's what the conversion process involves:

## Source and Target Formats

The script converts **from HDF5 (source) to RLDS (target)**. The documentation notes that "In the LIBERO HDF5 data -> RLDS data conversion (not shown here), we rotate the images by 180 degrees."

## Extracted Fields

The regenerated HDF5 output includes:

**Observations:**
- `"agentview_rgb"` - Main camera imagery
- `"eye_in_hand_rgb"` - Wrist-mounted camera
- `"gripper_states"`, `"joint_states"` - Proprioceptive data
- `"ee_states"` - End-effector position and orientation (axis-angle)

**Action Data:**
- Original demonstration actions stored directly

**Metadata:**
- States, robot states, rewards, and done flags

## Image Resolution

Images are saved at **256×256 pixels** rather than the original 128×128 resolution.

## Action Space

The script references 7-dimensional actions: "All action dimensions, except for the last one (gripper action), are near zero" suggests 6D end-effector control plus 1D gripper dimension.

## Key Processing Steps

The script filters out "no-op" transitions and removes unsuccessful demonstrations, keeping only completed episodes.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_openvla-oft-survey_20260520T040517",
  "tool": "WebFetch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 156 · 2026-05-20T04:19:56.359479+00:00_

# VLSA/AEGIS Technical Details

Based on the provided webpage, here's what can be extracted:

## 1) VLA Backbones Supported
The paper demonstrates integration with **OpenVLA-OFT** and **π₀.₅** (pi-0.5). Real-world experiments use **pi05-DROID** as the base VLA policy. The design is described as "plug-and-play," suggesting potential compatibility with other VLA models.

## 2) CBF-QP Solver Mechanics
The page references "a CBF-QP solver" that provides "theoretically guaranteed" safety adjustments to actions, but specific implementation details about the quadratic programming formulation aren't disclosed in this content.

## 3) Obstacle Detection via VLMs
The paper mentions "a vision-language based safety assessment module" that bridges visual perception with semantic understanding, but concrete implementation details about VLM-based obstacle detection are absent from this excerpt.

## 4) Full Pipeline Architecture
The architecture contains: a plug-and-play safety constraint (SC) layer using control barrier functions, a vision-language safety assessment module, and an action-driven safety-guaranteed control module. Figure 2 illustrates the AEGIS workflow, but detailed component descriptions aren't provided here.

## 5) VLA Modification Approach
The approach "integrates directly with existing VLA models" and is "plug-and-play," suggesting post-processing rather than modifying the action head directly, though explicit confirmation is absent.

## 6) Required Observations
The page doesn't specify exact observation formats—only that it involves visual input for the VLA and safety assessment.

## 7) Obstacle Position/Geometry Acquisition
This critical detail isn't disclosed in the provided content.

## 8) 3D Representations
No mention of occupancy grids or explicit 3D representations appears in this excerpt.

## 9) SafeLIBERO Dataset Details
The benchmark includes **32 scenarios and 1,600 episodes** across four categories:
- **SafeLIBERO-Spatial**: Spatial reasoning tasks
- 
…[truncated 341 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_openvla-oft-survey_20260520T040517",
  "tool": "WebFetch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 157 · 2026-05-20T04:19:56.359624+00:00_

# ActionTokenizer Class Overview

The provided code implements an `ActionTokenizer` class that extends a base LLM/VLM tokenizer to handle continuous robot actions by discretizing them into discrete tokens.

## Key Functionality

**Discretization Strategy**: The class converts continuous action values into uniform bins, mapping them to the least-used tokens at the end of a tokenizer's vocabulary. As noted in the documentation, "by default, assumes a BPE-style tokenizer akin to the LlamaTokenizer, where *the least used tokens* appear at the end of the vocabulary!"

**Core Methods**:
- `__init__`: Initializes the tokenizer with configurable bin count (default 256) and action bounds (default -1 to 1)
- `__call__`: Clips and bins actions, then decodes them to token strings
- `decode_token_ids_to_actions`: Reverses the process, converting token IDs back to continuous action values
- `vocab_size` property: Returns the number of bins

**Technical Details**: The implementation uses `np.digitize()` for binning and handles an important edge case where digitization returns indices outside the bin_centers array bounds, requiring clipping to prevent out-of-bounds access.

The class assumes reserved token slots equal to `n_bins + 1` at the end of the vocabulary for action encoding.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_openvla-oft-survey_20260520T040517",
  "tool": "WebFetch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 158 · 2026-05-20T04:19:56.359778+00:00_

# Key Hyperparameter and Implementation Details from Paper

## Training Hyperparameters
The document does not explicitly state several critical values in the main text or appendix sections provided:
- **Learning rate**: Not specified
- **LoRA rank and alpha**: Not specified
- **Optimizer**: Not specified
- **Weight decay**: Not specified
- **Gradient clipping**: Not mentioned
- **Mixed precision training**: Not mentioned

## Architecture Details

**MLP Action Head**: "4-layer noise predictor with same MLP architecture as the L1 regression head" and "4 layers with ReLU activation" but the hidden dimension is not disclosed.

**Language Model**: Llama-2 7B (embedding dimension not explicitly stated, though standard for Llama-2 7B is 4096).

**Vision Models**: 
- "SigLIP" and "DINOv2" vision transformers mentioned but specific variants (e.g., ViT-L/14) not provided
- "256 patch embeddings per view"

## ALOHA Task-Specific Results
Figure 4 shows aggregate performance scores but exact per-task success rates are presented as "average percent completion" rather than binary success rates. The document states: "Scores represent average percent completion of each task" with specifics relegated to appendix rubrics not fully included in the excerpt.

## Training Details (LIBERO)
- Batch size: 64-128 across 8 GPUs
- Gradient steps: 50-150K for non-diffusion; 100-250K for diffusion
- Control frequency: Not explicitly stated for LIBERO

## Missing Critical Information
The appendix sections A-D and A-E (referenced for "OpenVLA-OFT Hyperparameters" and "Baseline Methods Hyperparameters") are not fully provided in the content above, which would contain these implementation specifics.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_openvla-oft-survey_20260520T040517",
  "tool": "WebFetch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 159 · 2026-05-20T04:19:56.359925+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "gh api repos/moojink/openvla-oft/contents/LIBERO.md -H \"Accept: application/vnd.github.raw+json\" 2>/dev/null | head -500",
  "description": "Fetch raw LIBERO.md from GitHub API"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_openvla-oft-survey_20260520T040517",
  "tool": "Bash",
  "tool_args": {
    "command": "gh api repos/moojink/openvla-oft/contents/LIBERO.md -H \"Accept: application/vnd.github.raw+json\" 2>/dev/null | head -500",
    "description": "Fetch raw LIBERO.md from GitHub API"
  }
}
```

</details>

---

### Tool result

_source line 160 · 2026-05-20T04:19:56.360044+00:00_

(Bash completed with no output)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_openvla-oft-survey_20260520T040517",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 161 · 2026-05-20T04:19:56.360167+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "gh api repos/moojink/openvla-oft/contents/README.md -H \"Accept: application/vnd.github.raw+json\" 2>/dev/null | head -500",
  "description": "Fetch raw README.md from GitHub API"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_openvla-oft-survey_20260520T040517",
  "tool": "Bash",
  "tool_args": {
    "command": "gh api repos/moojink/openvla-oft/contents/README.md -H \"Accept: application/vnd.github.raw+json\" 2>/dev/null | head -500",
    "description": "Fetch raw README.md from GitHub API"
  }
}
```

</details>

---

### Tool result

_source line 162 · 2026-05-20T04:19:56.360282+00:00_

(Bash completed with no output)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_openvla-oft-survey_20260520T040517",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 163 · 2026-05-20T04:19:56.360401+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "gh auth status 2>&1; gh api repos/moojink/openvla-oft 2>&1 | head -5",
  "description": "Check GitHub CLI auth status"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_openvla-oft-survey_20260520T040517",
  "tool": "Bash",
  "tool_args": {
    "command": "gh auth status 2>&1; gh api repos/moojink/openvla-oft 2>&1 | head -5",
    "description": "Check GitHub CLI auth status"
  }
}
```

</details>

---

### Tool result

_source line 164 · 2026-05-20T04:19:56.360512+00:00_

/bin/bash: line 1: gh: command not found
/bin/bash: line 1: gh: command not found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_openvla-oft-survey_20260520T040517",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 165 · 2026-05-20T04:19:56.360637+00:00_

# Technical Details: VLSA (AEGIS) Paper

## 1) VLA Backbones Tested
- **Primary base model**: π0.5 (flow-matching VLA)
- **Baseline comparison**: OpenVLA-OFT (transformer-based VLA with online fine-tuning)
- **Direct reference**: Original π0.5 policy

## 2) Safety Constraint Layer Architecture
The SC layer is "a plug-and-play safety constraint layer formulated via control barrier functions." It operates as a **pure optimization layer applied post-hoc** to VLA outputs:

- Formulated as a convex quadratic program (QP) solving: minimize ||u - u_vla||² subject to h˙(x) ≥ -α(h(x))
- Activates only when safety violations detected; otherwise outputs original VLA action unchanged
- Training-free: applied during inference without retraining the base VLA

## 3) Obstacle Detection Pipeline
A vision-language-grounded pipeline:
1. VLM (GLM-4.5V) identifies "exactly one non-robot object that is most likely to obstruct the robot's motion"
2. GroundingDINO performs spatial localization, selecting "the bounding box with the highest confidence score"
3. Outputs include color + object type (e.g., "Milk Carton")

## 4) Obstacle Geometry Acquisition
Multi-view 3D reconstruction:
- RGB-D back-projection using standard camera intrinsics and extrinsics
- Dual viewpoints (agent-view + back-view cameras) for point cloud fusion
- Coordinate transformation: (u,v,d) → world frame via T_cam^world
- Preprocessing: workspace bounds filtering, outlier removal (farthest 20% discarded), DBSCAN clustering
- **Final representation**: Minimum Volume Enclosing Ellipsoid (MVEE) via convex optimization

## 5) Action Space
- **Reduced dimensionality** for evaluation: translational motion only (3-DoF)
- Standard VLA output: [v_vla⊤, ω_vla⊤, g_vla]⊤ (end-effector linear velocity, angular velocity, gripper command)
- Dynamics: ṗ = 0.2u (position dot equals 0.2 times velocity command)

## 6) Observations
- RGB images (agent and back viewpoints)
- Depth data (RGB-D from dual cameras)
- Natural language task inst
…[truncated 2402 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_openvla-oft-survey_20260520T040517",
  "tool": "WebFetch",
  "elapsed_ms": 2
}
```

</details>

---

### Tool call

_source line 166 · 2026-05-20T04:19:56.360816+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://raw.githubusercontent.com/moojink/openvla-oft/main/LIBERO.md",
  "prompt": "I need the EXACT raw markdown content of this file. Return it character-for-character. Include ALL code blocks with their exact content. Include ALL shell commands, ALL hyperparameters, ALL flags. Do NOT paraphrase or summarize any section. If there are training commands, return them exactly."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_openvla-oft-survey_20260520T040517",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://raw.githubusercontent.com/moojink/openvla-oft/main/LIBERO.md",
    "prompt": "I need the EXACT raw markdown content of this file. Return it character-for-character. Include ALL code blocks with their exact content. Include ALL shell commands, ALL hyperparameters, ALL flags. Do NOT paraphrase or summarize any section. If there are training commands, return them exactly."
  }
}
```

</details>

---

### Tool call

_source line 167 · 2026-05-20T04:19:56.360952+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://raw.githubusercontent.com/moojink/openvla-oft/main/README.md",
  "prompt": "I need the EXACT raw markdown content. Return it character-for-character including ALL code blocks, ALL hyperparameters, ALL shell commands. Do NOT paraphrase or summarize. Return the complete document verbatim."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_openvla-oft-survey_20260520T040517",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://raw.githubusercontent.com/moojink/openvla-oft/main/README.md",
    "prompt": "I need the EXACT raw markdown content. Return it character-for-character including ALL code blocks, ALL hyperparameters, ALL shell commands. Do NOT paraphrase or summarize. Return the complete document verbatim."
  }
}
```

</details>

---

### Tool call

_source line 168 · 2026-05-20T04:19:56.361082+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://liner.com/review/vlsa-visionlanguageaction-models-with-plugandplay-safety-constraint-layer",
  "prompt": "Extract any additional technical details about VLSA/AEGIS not covered: How does the VLM identify obstacles? How does GroundingDINO localize them? How are RGB-D observations used to construct point clouds? What are the full SafeLIBERO observation fields?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_openvla-oft-survey_20260520T040517",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://liner.com/review/vlsa-visionlanguageaction-models-with-plugandplay-safety-constraint-layer",
    "prompt": "Extract any additional technical details about VLSA/AEGIS not covered: How does the VLM identify obstacles? How does GroundingDINO localize them? How are RGB-D observations used to construct point clouds? What are the full SafeLIBERO observation fields?"
  }
}
```

</details>

---

### Tool call

_source line 169 · 2026-05-20T04:19:56.361211+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"OpenVLA-OFT\" action head architecture \"continuous action\" \"L1 regression\" proprio projector"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_openvla-oft-survey_20260520T040517",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"OpenVLA-OFT\" action head architecture \"continuous action\" \"L1 regression\" proprio projector"
  }
}
```

</details>

---

### Tool call

_source line 170 · 2026-05-20T04:19:56.361336+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "LIBERO benchmark HDF5 dataset observation space action space 7-DoF format details"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_openvla-oft-survey_20260520T040517",
  "tool": "WebSearch",
  "tool_args": {
    "query": "LIBERO benchmark HDF5 dataset observation space action space 7-DoF format details"
  }
}
```

</details>

---

### Tool result

_source line 171 · 2026-05-20T04:19:56.361452+00:00_

# OpenVLA-OFT LIBERO Benchmark Documentation

## Key Setup Requirements

The documentation specifies cloning the LIBERO repository and installing dependencies:

```bash
git clone https://github.com/Lifelong-Robot-Learning/LIBERO.git
pip install -e LIBERO
```

Installation also requires the requirements file from the project directory.

## Available Checkpoints

Four independently trained models are provided for different task suites, with an additional unified model trained across all suites. The unified checkpoint achieved "96.8% average success rate across the four suites."

## Evaluation Instructions

The evaluation script accepts parameters including checkpoint selection, task suite specification, trial count, and random seed. A critical implementation detail is that "center crop True is important" because the fine-tuning process used random crop augmentation.

## Fine-Tuning Configuration

Training uses LoRA with rank 32. The base command structure uses `torchrun` for distributed training, specifying the VLA path, dataset directory, and output checkpoint location. Key hyperparameters include learning rate of 5e-4, batch size 8, and maximum steps of 150,005.

## Performance Considerations

The documentation emphasizes testing on the same GPU used for training, as performance may degrade substantially otherwise. For LIBERO-Goal specifically, the 50K checkpoint performed optimally, while other suites performed best at the 150K checkpoint.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_openvla-oft-survey_20260520T040517",
  "tool": "WebFetch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 172 · 2026-05-20T04:19:56.361582+00:00_

# Summary of OpenVLA-OFT Project

This project focuses on fine-tuning vision-language-action models for robotics tasks. Here are the key points:

**Core Resources:**
The project provides a website, arxiv paper (2502.19645), and video tutorial for understanding the approach.

**Hardware Requirements:**
Inference needs either 16GB VRAM for simulation or 18GB for physical robots. Training demands 1-8 GPUs with 27-80GB capacity depending on configuration.

**Getting Started:**
After environment setup, users can download a pretrained checkpoint and run inference using the provided Python script. The code loads various components including the VLA model, processor, action head, and proprioceptive projector to generate action sequences from observations.

**Input Format:**
The system accepts observations containing third-person images, wrist camera footage, robot state data, and task descriptions to produce action chunks.

**Documentation:**
Separate guides cover LIBERO simulation benchmarks and ALOHA real-world robot tasks. Installation instructions appear in SETUP.md.

**Support:**
The authors request GitHub issues for problems, with email escalation available within two business days.

**Citation:**
The work is attributed to Kim, Finn, and Liang (2025) at Stanford.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_openvla-oft-survey_20260520T040517",
  "tool": "WebFetch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 173 · 2026-05-20T04:19:56.361725+00:00_

# Technical Details Not Covered in the Review

Based on the provided content, the quick review does not include specific technical details about:

1. **VLM Obstacle Identification**: The review mentions that AEGIS includes "a vision-language based safety assessment module that identifies hazardous objects using VLMs, open-set object detection, and depth information," but provides no specifics on the VLM's methodology.

2. **GroundingDINO Localization**: While the abstract references GroundingDINO as part of the perception pipeline, the review offers no explanation of how this tool localizes detected obstacles.

3. **Point Cloud Construction**: The review does not describe how RGB-D sensor data is processed into point clouds, though it mentions "point cloud filtering" as a limitation affecting obstacle detection accuracy.

4. **SafeLIBERO Observation Fields**: The review states that SafeLIBERO is "a comprehensive safety-critical benchmark derived from the LIBERO dataset" but does not enumerate the specific observation fields or data modalities included.

The review focuses on high-level architectural components and experimental results rather than granular implementation details. For comprehensive technical specifications on these aspects, you would need to consult the full paper, which is available at the authors' project website referenced in the abstract.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_openvla-oft-survey_20260520T040517",
  "tool": "WebFetch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 174 · 2026-05-20T04:19:56.361862+00:00_

Web search results for query: ""OpenVLA-OFT" action head architecture "continuous action" "L1 regression" proprio projector"

Links: [{"title":"GitHub - moojink/openvla-oft: Fine-Tuning Vision-Language-Action Models: Optimizing Speed and Success · GitHub","url":"https://github.com/moojink/openvla-oft"},{"title":"GitHub - hanbit-o/openvla-oft: Fine-Tuning Vision-Language-Action Models: Optimizing Speed and Success · GitHub","url":"https://github.com/hanbit-o/openvla-oft"},{"title":"openvla-oft/README.md at main · moojink/openvla-oft","url":"https://github.com/moojink/openvla-oft/blob/main/README.md"},{"title":"moojink/openvla-7b-oft-finetuned-libero-object · Hugging Face","url":"https://huggingface.co/moojink/openvla-7b-oft-finetuned-libero-object"},{"title":"moojink/openvla-7b-oft-finetuned-libero-10 · Hugging Face","url":"https://huggingface.co/moojink/openvla-7b-oft-finetuned-libero-10"},{"title":"README.md · moojink/openvla-7b-oft-finetuned-libero-10 at main","url":"https://huggingface.co/moojink/openvla-7b-oft-finetuned-libero-10/blob/main/README.md"},{"title":"moojink/openvla-7b-oft-finetuned-libero-goal · Hugging Face","url":"https://huggingface.co/moojink/openvla-7b-oft-finetuned-libero-goal"},{"title":"moojink/openvla-7b-oft-finetuned-libero-spatial · Hugging Face","url":"https://huggingface.co/moojink/openvla-7b-oft-finetuned-libero-spatial"},{"title":"Fine-Tuning Vision-Language-Action Models: Optimizing Speed and Success","url":"https://arxiv.org/pdf/2502.19645"},{"title":"OpenVLA-OFT","url":"https://openvla-oft.github.io/"}]

Based on the search results, here's what I found about OpenVLA-OFT and its action head architecture:

## Action Head Architecture

OpenVLA-OFT uses an MLP action head to generate continuous actions via L1 regression. The architecture includes several key components:

1. **Continuous Action Representation**: The model integrates a continuous action representation with an L1 regression-based learning objective to improve inference eff
…[truncated 818 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_openvla-oft-survey_20260520T040517",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 175 · 2026-05-20T04:19:56.362015+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://raw.githubusercontent.com/moojink/openvla-oft/main/vla-scripts/finetune.py",
  "prompt": "Extract ONLY the FinetuneConfig dataclass. Return every field name, type annotation, default value, and comment. Also extract the main() function or entry point. Return the torchrun/launch command if present. Return any learning rate, batch size, warmup, decay schedule values."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_openvla-oft-survey_20260520T040517",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://raw.githubusercontent.com/moojink/openvla-oft/main/vla-scripts/finetune.py",
    "prompt": "Extract ONLY the FinetuneConfig dataclass. Return every field name, type annotation, default value, and comment. Also extract the main() function or entry point. Return the torchrun/launch command if present. Return any learning rate, batch size, warmup, decay schedule values."
  }
}
```

</details>

---

### Tool result

_source line 176 · 2026-05-20T04:19:56.362150+00:00_

Web search results for query: "LIBERO benchmark HDF5 dataset observation space action space 7-DoF format details"

Links: [{"title":"LIBERO Benchmark: Vision-Language-Action in Robotics","url":"https://www.emergentmind.com/topics/libero"},{"title":"RL with LIBERO Benchmark — RLinf documentation","url":"https://rlinf.readthedocs.io/en/latest/rst_source/examples/embodied/libero.html"},{"title":"Benchmark Descriptions — RoboVerse 0.1.0 documentation","url":"https://roboverse.wiki/dataset_benchmark/tasks/descriptions"},{"title":"LIBERO-PRO: Towards Robust and Fair Evaluation of Vision-Language-Action Models Beyond Memorization","url":"https://arxiv.org/pdf/2510.03827"},{"title":"nvidia/Cosmos-Policy-LIBERO-Predict2-2B · Hugging Face","url":"https://huggingface.co/nvidia/Cosmos-Policy-LIBERO-Predict2-2B"},{"title":"LIBERO · Hugging Face","url":"https://huggingface.co/docs/lerobot/libero"},{"title":"clip-rt/modified_libero_hdf5 · Datasets at Hugging Face","url":"https://huggingface.co/datasets/clip-rt/modified_libero_hdf5"},{"title":"LIBERO: Benchmarking Knowledge Transfer for Lifelong Robot Learning","url":"https://arxiv.org/pdf/2306.03310"}]

Based on the search results, here are the details about the LIBERO benchmark's HDF5 dataset format, observation space, and action space for 7-DoF control:

## Action Space

The LIBERO action space consists of 7-dimensional continuous actions: 3D end-effector position control (x, y, z), 3D rotation control (roll, pitch, yaw), and gripper control (open/close). More specifically, actions are organized as 16-timestep sequences of 7-dimensional actions representing 6-DoF end-effector control plus 1 gripper dimension.

## Observation Space

Observations consist of RGB images with typical resolutions of 128 × 128 or 224 × 224 captured by off-screen cameras placed around the workspace. Additionally, the observation includes 8-dimensional proprioceptive features (end-effector position, axis-angle orientation, gripper position) along with ma
…[truncated 602 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_openvla-oft-survey_20260520T040517",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 177 · 2026-05-20T04:19:56.362303+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://raw.githubusercontent.com/moojink/openvla-oft/main/LIBERO.md",
  "prompt": "Extract ALL shell commands and code blocks from this file verbatim. I need every torchrun command, every evaluation command, every pip install command. Include all flags, arguments, hyperparameters. Also extract all checkpoint URLs/paths mentioned."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_openvla-oft-survey_20260520T040517",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://raw.githubusercontent.com/moojink/openvla-oft/main/LIBERO.md",
    "prompt": "Extract ALL shell commands and code blocks from this file verbatim. I need every torchrun command, every evaluation command, every pip install command. Include all flags, arguments, hyperparameters. Also extract all checkpoint URLs/paths mentioned."
  }
}
```

</details>

---

### Tool call

_source line 178 · 2026-05-20T04:19:56.362438+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://raw.githubusercontent.com/moojink/openvla-oft/main/README.md",
  "prompt": "Extract ALL code blocks from this README verbatim. I need every Python code snippet, every shell command. Include all import statements, function calls, variable assignments. Also extract all URLs and checkpoint paths mentioned."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_openvla-oft-survey_20260520T040517",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://raw.githubusercontent.com/moojink/openvla-oft/main/README.md",
    "prompt": "Extract ALL code blocks from this README verbatim. I need every Python code snippet, every shell command. Include all import statements, function calls, variable assignments. Also extract all URLs and checkpoint paths mentioned."
  }
}
```

</details>

---

### Tool result

_source line 179 · 2026-05-20T04:19:56.362566+00:00_

# Shell Commands and Code Blocks

## Installation Commands

```bash
git clone https://github.com/Lifelong-Robot-Learning/LIBERO.git
pip install -e LIBERO
pip install -r experiments/robot/libero/libero_requirements.txt
```

```bash
git clone git@hf.co:datasets/openvla/modified_libero_rlds
```

## Evaluation Commands

```bash
python experiments/robot/libero/run_libero_eval.py \
  --pretrained_checkpoint moojink/openvla-7b-oft-finetuned-libero-spatial \
  --task_suite_name libero_spatial
```

```bash
python experiments/robot/libero/run_libero_eval.py \
  --pretrained_checkpoint moojink/openvla-7b-oft-finetuned-libero-object \
  --task_suite_name libero_object
```

```bash
python experiments/robot/libero/run_libero_eval.py \
  --pretrained_checkpoint moojink/openvla-7b-oft-finetuned-libero-goal \
  --task_suite_name libero_goal
```

```bash
python experiments/robot/libero/run_libero_eval.py \
  --pretrained_checkpoint moojink/openvla-7b-oft-finetuned-libero-10 \
  --task_suite_name libero_10
```

## Fine-Tuning Command

```bash
torchrun --standalone --nnodes 1 --nproc-per-node X vla-scripts/finetune.py \
  --vla_path openvla/openvla-7b \
  --data_root_dir /PATH/TO/RLDS/DATASETS/DIR/ \
  --dataset_name libero_spatial_no_noops \
  --run_root_dir /YOUR/CHECKPOINTS/AND/LOG/DIR/ \
  --use_l1_regression True \
  --use_diffusion False \
  --use_film False \
  --num_images_in_input 2 \
  --use_proprio True \
  --batch_size 8 \
  --learning_rate 5e-4 \
  --num_steps_before_decay 100000 \
  --max_steps 150005 \
  --save_freq 10000 \
  --save_latest_checkpoint_only False \
  --image_aug True \
  --lora_rank 32 \
  --wandb_entity "YOUR_WANDB_ENTITY" \
  --wandb_project "YOUR_WANDB_PROJECT" \
  --run_id_note parallel_dec--8_acts_chunk--continuous_acts--L1_regression--3rd_person_img--wrist_img--proprio_state
```

## Checkpoint URLs

- moojink/openvla-7b-oft-finetuned-libero-spatial
- moojink/openvla-7b-oft-finetuned-libero-object
- moojink/openvla-7b-oft-finetuned-libero-goal
- mooji
…[truncated 102 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_openvla-oft-survey_20260520T040517",
  "tool": "WebFetch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 180 · 2026-05-20T04:19:56.362729+00:00_

# Code Blocks and Resources from OpenVLA-OFT README

## Python Code Block

```python
import pickle
from experiments.robot.libero.run_libero_eval import GenerateConfig
from experiments.robot.openvla_utils import get_action_head, get_processor, get_proprio_projector, get_vla, get_vla_action
from prismatic.vla.constants import NUM_ACTIONS_CHUNK, PROPRIO_DIM

# Instantiate config (see class GenerateConfig in experiments/robot/libero/run_libero_eval.py for definitions)
cfg = GenerateConfig(
    pretrained_checkpoint = "moojink/openvla-7b-oft-finetuned-libero-spatial",
    use_l1_regression = True,
    use_diffusion = False,
    use_film = False,
    num_images_in_input = 2,
    use_proprio = True,
    load_in_8bit = False,
    load_in_4bit = False,
    center_crop = True,
    num_open_loop_steps = NUM_ACTIONS_CHUNK,
    unnorm_key = "libero_spatial_no_noops",
)

# Load OpenVLA-OFT policy and inputs processor
vla = get_vla(cfg)
processor = get_processor(cfg)

# Load MLP action head to generate continuous actions (via L1 regression)
action_head = get_action_head(cfg, llm_dim=vla.llm_dim)

# Load proprio projector to map proprio to language embedding space
proprio_projector = get_proprio_projector(cfg, llm_dim=vla.llm_dim, proprio_dim=PROPRIO_DIM)

# Load sample observation:
#   observation (dict): {
#     "full_image": primary third-person image,
#     "wrist_image": wrist-mounted camera image,
#     "state": robot proprioceptive state,
#     "task_description": task description,
#   }
with open("experiments/robot/libero/sample_libero_spatial_observation.pkl", "rb") as file:
    observation = pickle.load(file)

# Generate robot action chunk (sequence of future actions)
actions = get_vla_action(cfg, vla, processor, observation, observation["task_description"], action_head, proprio_projector)
print("Generated action chunk:")
for act in actions:
    print(act)
```

## URLs

- Project website: https://openvla-oft.github.io/
- Paper: https://arxiv.org/abs/2502.19645
- Video: ht
…[truncated 99 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_openvla-oft-survey_20260520T040517",
  "tool": "WebFetch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 181 · 2026-05-20T04:19:56.362889+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://arxiv.org/html/2512.11891v1",
  "prompt": "Focus on: 1) Does SafeLIBERO provide training demonstrations or is it evaluation-only? 2) Are there any obstacle annotations in the training data (bounding boxes, masks, positions)? 3) Does SafeLIBERO include any occupancy-like representations? 4) What exactly is in the SafeLIBERO HuggingFace dataset - is it just init files for evaluation, or actual demonstration trajectories? 5) How does the paper get obstacle positions at test time - from simulator ground truth or from perception?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_openvla-oft-survey_20260520T040517",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://arxiv.org/html/2512.11891v1",
    "prompt": "Focus on: 1) Does SafeLIBERO provide training demonstrations or is it evaluation-only? 2) Are there any obstacle annotations in the training data (bounding boxes, masks, positions)? 3) Does SafeLIBERO include any occupancy-like representations? 4) What exactly is in the SafeLIBERO HuggingFace dataset - is it just init files for evaluation, or actual demonstration trajectories? 5) How does the paper get obstacle positions at test time - from simulator ground truth or from perception?"
  }
}
```

</details>

---

### Tool call

_source line 182 · 2026-05-20T04:19:56.363048+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://huggingface.co/datasets/clip-rt/modified_libero_hdf5",
  "prompt": "What is the structure of the LIBERO HDF5 dataset? What fields/keys does it contain? What are the observation dimensions? What is the action format?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_openvla-oft-survey_20260520T040517",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://huggingface.co/datasets/clip-rt/modified_libero_hdf5",
    "prompt": "What is the structure of the LIBERO HDF5 dataset? What fields/keys does it contain? What are the observation dimensions? What is the action format?"
  }
}
```

</details>

---

### Tool result

_source line 183 · 2026-05-20T04:19:56.363178+00:00_

# FinetuneConfig Dataclass Extraction

## Fields and Configuration

| Field | Type | Default | Comment |
|-------|------|---------|---------|
| `vla_path` | str | "openvla/openvla-7b" | Path to OpenVLA model (HF Hub or local) |
| `data_root_dir` | Path | Path("datasets/rlds") | Directory containing RLDS datasets |
| `dataset_name` | str | "aloha_scoop_x_into_bowl" | Fine-tuning dataset name |
| `run_root_dir` | Path | Path("runs") | Path for logs & checkpoints |
| `shuffle_buffer_size` | int | 100_000 | Dataloader shuffle buffer size |
| `use_l1_regression` | bool | True | Trains continuous action head with L1 loss |
| `use_diffusion` | bool | False | Trains continuous action head with diffusion |
| `num_diffusion_steps_train` | int | 50 | Diffusion steps for training |
| `use_film` | bool | False | Uses FiLM for language-visual fusion |
| `num_images_in_input` | int | 1 | Number of images in VLA input |
| `use_proprio` | bool | False | Includes robot proprioceptive state |
| `batch_size` | int | 8 | Batch size per device |
| `learning_rate` | float | 5e-4 | Learning rate |
| `lr_warmup_steps` | int | 0 | Warmup steps (10% to 100%) |
| `num_steps_before_decay` | int | 100_000 | Steps before 10x LR decay |
| `grad_accumulation_steps` | int | 1 | Gradient accumulation steps |
| `max_steps` | int | 200_000 | Maximum training steps |
| `use_val_set` | bool | False | Uses validation set |
| `val_freq` | int | 10_000 | Validation logging frequency |
| `val_time_limit` | int | 180 | Validation time limit (seconds) |
| `save_freq` | int | 10_000 | Checkpoint saving frequency |
| `save_latest_checkpoint_only` | bool | False | Saves only latest or all checkpoints |
| `resume` | bool | False | Resumes from checkpoint |
| `resume_step` | Optional[int] | None | Step number to resume from |
| `image_aug` | bool | True | Trains with image augmentations |
| `diffusion_sample_freq` | int | 50 | Diffusion sampling frequency |
| `use_lora` | bool | True | Uses LoRA fine-tuning |
| `lo
…[truncated 760 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_openvla-oft-survey_20260520T040517",
  "tool": "WebFetch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 184 · 2026-05-20T04:19:56.363325+00:00_

# LIBERO HDF5 Dataset Structure

Based on the provided web page content, **specific details about the internal structure, fields, keys, observation dimensions, and action format of the LIBERO HDF5 dataset are not documented on this page**.

## What the Page Tells Us

The page only mentions:

1. **Modifications Made:**
   - Image resolution increased from 128×128 to 256×256
   - Zero-valued actions (no-op) filtered out

2. **Source Reference:**
   - Original [LIBERO benchmark data](https://libero-project.github.io/main.html)
   - Modified using the [OpenVLA regeneration script](https://github.com/openvla/openvla/blob/main/experiments/robot/libero/regenerate_libero_dataset.py)

## Where to Find This Information

To learn about the actual HDF5 structure, you would need to:

1. **Check the OpenVLA repository** - The regeneration script referenced likely contains details about the data format
2. **Visit the LIBERO project documentation** - The official LIBERO benchmark documentation would have comprehensive schema information
3. **Examine the dataset files directly** - Using HDF5 tools to inspect the actual file structure
4. **Review the preprocessing code** mentioned in the description

The dataset viewer on this Hugging Face page couldn't detect supported data formats, so detailed schema information isn't available through the web interface.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_openvla-oft-survey_20260520T040517",
  "tool": "WebFetch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 185 · 2026-05-20T04:19:56.363455+00:00_

# SafeLIBERO Dataset Analysis

Based on the paper content:

## 1) Training vs. Evaluation
SafeLIBERO is **evaluation-only**. The paper states it was constructed to "assess performance in complex environments" because "objects in the original LIBERO environments rarely collide with the robot arm."

## 2) Obstacle Annotations
The paper provides **no evidence of annotated obstacles** in the dataset itself. Obstacles are "added" to existing LIBERO tasks: "we select four tasks from each LIBERO suite and further divide each into two scenarios with different safety levels based on the degree of interference posed by the added obstacle."

## 3) Occupancy Representations
**No occupancy representations** are mentioned for SafeLIBERO.

## 4) HuggingFace Dataset Contents
The paper doesn't specify what the public dataset release contains. It only mentions: "we make our code, models, and the benchmark datasets publicly available at [https://vlsa-aegis.github.io/](https://vlsa-aegis.github.io/)." No details about format or structure are provided.

## 5) Obstacle Position Source at Test Time
Obstacle positions come from **simulator ground truth**, not perception. The safety assessment module uses VLMs and GroundingDINO for semantic identification, but the actual geometric ellipsoid fitting occurs on "processed point cloud data" derived from simulated RGB-D cameras with "precise coordinate transformation between the camera and world frames."

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_openvla-oft-survey_20260520T040517",
  "tool": "WebFetch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 186 · 2026-05-20T04:19:56.363598+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://api.github.com/repos/moojink/openvla-oft/contents/experiments/robot",
  "prompt": "Return complete listing of all files and directories with name, path, type."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_openvla-oft-survey_20260520T040517",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://api.github.com/repos/moojink/openvla-oft/contents/experiments/robot",
    "prompt": "Return complete listing of all files and directories with name, path, type."
  }
}
```

</details>

---

### Tool result

_source line 187 · 2026-05-20T04:19:56.363740+00:00_

# File and Directory Listing

Based on the GitHub API response, here is the complete listing:

| Name | Path | Type |
|------|------|------|
| aloha | experiments/robot/aloha | Directory |
| libero | experiments/robot/libero | Directory |
| openvla_utils.py | experiments/robot/openvla_utils.py | File |
| robot_utils.py | experiments/robot/robot_utils.py | File |

The repository contains two subdirectories (aloha and libero) and two Python utility files within the experiments/robot folder. The openvla_utils.py file is notably larger at approximately 30 KB, while robot_utils.py is about 6 KB.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_openvla-oft-survey_20260520T040517",
  "tool": "WebFetch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 188 · 2026-05-20T04:19:56.363880+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://raw.githubusercontent.com/moojink/openvla-oft/main/prismatic/vla/datasets/rlds/oxe/configs.py",
  "prompt": "Extract ALL dataset configuration entries related to LIBERO. Return the exact config dict entries including dataset_name, image_obs_keys, action_encoding, action keys, state keys. Also list any other LIBERO-related entries."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_openvla-oft-survey_20260520T040517",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://raw.githubusercontent.com/moojink/openvla-oft/main/prismatic/vla/datasets/rlds/oxe/configs.py",
    "prompt": "Extract ALL dataset configuration entries related to LIBERO. Return the exact config dict entries including dataset_name, image_obs_keys, action_encoding, action keys, state keys. Also list any other LIBERO-related entries."
  }
}
```

</details>

---

### Tool call

_source line 189 · 2026-05-20T04:19:56.364011+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://raw.githubusercontent.com/moojink/openvla-oft/main/prismatic/vla/datasets/rlds/oxe/mixtures.py",
  "prompt": "Return ALL entries related to LIBERO. Show every mixture definition that includes LIBERO datasets. Return exact dataset names and weights."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_openvla-oft-survey_20260520T040517",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://raw.githubusercontent.com/moojink/openvla-oft/main/prismatic/vla/datasets/rlds/oxe/mixtures.py",
    "prompt": "Return ALL entries related to LIBERO. Show every mixture definition that includes LIBERO datasets. Return exact dataset names and weights."
  }
}
```

</details>

---

### Tool call

_source line 190 · 2026-05-20T04:19:56.364140+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "VLA model auxiliary head 3D occupancy safety constraint manipulation 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_openvla-oft-survey_20260520T040517",
  "tool": "WebSearch",
  "tool_args": {
    "query": "VLA model auxiliary head 3D occupancy safety constraint manipulation 2025 2026"
  }
}
```

</details>

---

### Tool call

_source line 191 · 2026-05-20T04:19:56.364264+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "SafeVLA constrained MDP safety VLA architecture training details NeurIPS 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_openvla-oft-survey_20260520T040517",
  "tool": "WebSearch",
  "tool_args": {
    "query": "SafeVLA constrained MDP safety VLA architecture training details NeurIPS 2025"
  }
}
```

</details>

---

### Tool result

_source line 192 · 2026-05-20T04:19:56.364380+00:00_

# LIBERO Dataset Entries

All LIBERO-related mixture definitions from the registry:

**Individual LIBERO Mixtures:**
- `"libero_spatial_no_noops"`: `("libero_spatial_no_noops", 1.0)`
- `"libero_object_no_noops"`: `("libero_object_no_noops", 1.0)`
- `"libero_goal_no_noops"`: `("libero_goal_no_noops", 1.0)`
- `"libero_10_no_noops"`: `("libero_10_no_noops", 1.0)`

**Combined LIBERO Mixture:**
- `"libero_4_task_suites_no_noops"` includes all four variants with equal weights of 1.0 each

All LIBERO datasets are marked as "Modified Versions" and use a sampling weight of 1.0. They appear as standalone mixture definitions rather than being incorporated into the broader multi-dataset mixtures (like RT-X or Magic Soup variants).

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_openvla-oft-survey_20260520T040517",
  "tool": "WebFetch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 193 · 2026-05-20T04:19:56.364501+00:00_

# LIBERO Dataset Configurations

Based on the provided content, there are **4 LIBERO-related dataset entries** in the Open-X Embodiment configuration:

## Configuration Entries

1. **libero_spatial_no_noops**
   - Image observations: primary image + wrist camera
   - State encoding: POS_EULER
   - Action encoding: EEF_POS
   - State keys: "EEF_state", "gripper_state"

2. **libero_object_no_noops**
   - Image observations: primary image + wrist camera
   - State encoding: POS_EULER
   - Action encoding: EEF_POS
   - State keys: "EEF_state", "gripper_state"

3. **libero_goal_no_noops**
   - Image observations: primary image + wrist camera
   - State encoding: POS_EULER
   - Action encoding: EEF_POS
   - State keys: "EEF_state", "gripper_state"

4. **libero_10_no_noops**
   - Image observations: primary image + wrist camera
   - State encoding: POS_EULER
   - Action encoding: EEF_POS
   - State keys: "EEF_state", "gripper_state"

5. **libero_4_task_suites_no_noops**
   - Image observations: primary image + wrist camera
   - State encoding: POS_EULER
   - Action encoding: EEF_POS
   - State keys: "EEF_state", "gripper_state"

All LIBERO variants share identical observation and action configurations, differentiated by task scope ("_no_noops" indicates removal of no-operation actions).

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_openvla-oft-survey_20260520T040517",
  "tool": "WebFetch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 194 · 2026-05-20T04:19:56.364723+00:00_

Here is a comprehensive report of all technical details extracted from the OpenVLA-OFT paper (arXiv:2502.19645).

---

## Paper: "Fine-Tuning Vision-Language-Action Models: Optimizing Speed and Success"

**Authors:** Moo Jin Kim, Chelsea Finn, Percy Liang  
**Venue:** RSS 2025

---

## 1. Architecture

**Base model:** OpenVLA — a 7B-parameter (7.5B total) manipulation policy built by fine-tuning the Prismatic VLM on 1M episodes from the Open X-Embodiment dataset.

**Language backbone:** Llama-2 7B (standard embedding dimension 4096).

**Vision encoder:** Fused dual backbone combining SigLIP and DINOv2 vision transformers. Each ViT extracts 256 patch embeddings per image at 224x224 input resolution. Visual features are projected into the language embedding space via a 3-layer MLP with GELU activation.

**Robot state encoding:** A 2-layer MLP with GELU activation projects proprioceptive inputs (e.g., 14-dimensional joint angles for ALOHA) into the language embedding space.

**Original OpenVLA formulation:** Autoregressive prediction of 7 discrete robot action tokens per timestep (3 position, 3 orientation, 1 gripper), using 256-bin discretization.

---

## 2. OFT Modifications (6 key changes)

1. **Parallel decoding** — replaces causal attention mask with bidirectional attention; uses empty action embeddings with positional encodings only; maps input embeddings to predicted output sequence in a single forward pass.
2. **Action chunking** — predicts K x D actions in one forward pass (K=8 for LIBERO, K=25 for ALOHA).
3. **Continuous action representation** — actions normalized to [-1, +1] range instead of 256-bin discretization.
4. **L1 regression objective** — a 4-layer MLP action head with ReLU activation maps final decoder layer hidden states directly to continuous action values.
5. **Multi-image processing** — shared SigLIP-DINOv2 backbone processes multiple camera views (256 patch embeddings per view), all concatenated along the sequence dimension.
6. **FiLM condit
…[truncated 5551 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_openvla-oft-survey_20260520T040517",
  "tool": "Agent",
  "elapsed_ms": 20
}
```

</details>

---

### Tool result

_source line 195 · 2026-05-20T04:19:56.364908+00:00_

Web search results for query: "SafeVLA constrained MDP safety VLA architecture training details NeurIPS 2025"

Links: [{"title":"SafeVLA: Towards Safety Alignment of Vision-Language-Action Model via Constrained Learning","url":"https://papers.nips.cc/paper_files/paper/2025/hash/e185c7be603426028c32ae1003a59d78-Abstract-Conference.html"},{"title":"SafeVLA: Towards Safety Alignment of Vision-Language-Action Model via Constrained Learning | OpenReview","url":"https://openreview.net/forum?id=dt940loCBT"},{"title":"SafeVLA: Towards Safety Alignment of Vision-","url":"https://openreview.net/pdf?id=dt940loCBT"},{"title":"NeurIPS Poster SafeVLA: Towards Safety Alignment of Vision-Language-Action Model via Constrained Learning","url":"https://neurips.cc/virtual/2025/poster/116975"},{"title":"[2503.03480] SafeVLA: Towards Safety Alignment of Vision-Language-Action Model via Constrained Learning","url":"https://arxiv.org/abs/2503.03480"},{"title":"GitHub - PKU-Alignment/SafeVLA: [NeurIPS 2025 Spotlight] Towards Safety Alignment of Vision-Language-Action Model via Constrained Learning. · GitHub","url":"https://github.com/PKU-Alignment/SafeVLA"},{"title":"SafeVLA: Towards Safety Alignment of Vision-Language-Action Model via Safe Reinforcement Learning","url":"https://arxiv.org/html/2503.03480v1"},{"title":"(PDF) SafeVLA: Towards Safety Alignment of Vision-Language-Action Model via Safe Reinforcement Learning","url":"https://www.researchgate.net/publication/389616290_SafeVLA_Towards_Safety_Alignment_of_Vision-Language-Action_Model_via_Safe_Reinforcement_Learning"},{"title":"SafeVLA: Towards Safety Alignment of Vision-Language-Action Model via Constrained Learning","url":"https://safevla.github.io/"},{"title":"SafeVLA - a PKU-Alignment Collection","url":"https://huggingface.co/collections/PKU-Alignment/safevla"}]

I found comprehensive information about SafeVLA from NeurIPS 2025. Here are the key details:

## Overview
SafeVLA explores an integrated safety approach (ISA), systemati
…[truncated 1655 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_openvla-oft-survey_20260520T040517",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 196 · 2026-05-20T04:19:56.365071+00:00_

Web search results for query: "VLA model auxiliary head 3D occupancy safety constraint manipulation 2025 2026"

Links: [{"title":"(PDF) VLSA: Vision-Language-Action Models with Plug-and-Play Safety Constraint Layer","url":"https://www.researchgate.net/publication/398721287_VLSA_Vision-Language-Action_Models_with_Plug-and-Play_Safety_Constraint_Layer"},{"title":"VLSA: Vision-Language-Action Models with Plug-and-Play Safety Constraint Layer","url":"https://arxiv.org/pdf/2512.11891"},{"title":"QDepth-VLA: Quantized Depth Prediction as Auxiliary Supervision for Vision-Language-Action Models","url":"https://arxiv.org/pdf/2510.14836"},{"title":"VLSA: Vision-Language-Action Models with Plug-and-Play Safety Constraint Layer [Quick Review]","url":"https://liner.com/review/vlsa-visionlanguageaction-models-with-plugandplay-safety-constraint-layer"},{"title":"[2512.11891] VLSA: Vision-Language-Action Models with Plug-and-Play Safety Constraint Layer","url":"https://arxiv.org/abs/2512.11891"},{"title":"GitHub - OpenDriveLab/WholebodyVLA: [ICLR 2026] Towards Unified Latent VLA for Whole-body Loco-manipulation Control · GitHub","url":"https://github.com/OpenDriveLab/WholebodyVLA"},{"title":"SafeVLA: Towards Safety Alignment of Vision- Language-Action Model via Constrained Learning","url":"https://arxiv.org/html/2503.03480v4"}]

Based on the search results, I found several relevant papers on VLA models with safety constraints and 3D perception for robotic manipulation from 2025-2026:

## Key Findings:

**VLSA (Vision-Language-Safe Action) with AEGIS Architecture:**
AEGIS is a Vision-Language-Safe Action (VLSA) architecture that contains a plug-and-play safety constraint (SC) layer formulated via control barrier functions, which integrates directly with existing VLA models to improve safety with theoretical guarantees while maintaining their original instruction-following performance.

The system models the entire end-effector assembly and task-relevant obstacles as ellipsoids, with
…[truncated 1054 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_openvla-oft-survey_20260520T040517",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 197 · 2026-05-20T04:19:56.365228+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://raw.githubusercontent.com/moojink/openvla-oft/main/experiments/robot/openvla_utils.py",
  "prompt": "Extract ALL function signatures with their full parameter lists and default values. For the get_vla, get_action_head, get_processor, get_proprio_projector, and get_vla_action functions, return their COMPLETE implementation code. Include all model loading logic, checkpoint paths, and configuration details."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_openvla-oft-survey_20260520T040517",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://raw.githubusercontent.com/moojink/openvla-oft/main/experiments/robot/openvla_utils.py",
    "prompt": "Extract ALL function signatures with their full parameter lists and default values. For the get_vla, get_action_head, get_processor, get_proprio_projector, and get_vla_action functions, return their COMPLETE implementation code. Include all model loading logic, checkpoint paths, and configuration details."
  }
}
```

</details>

---

### Tool call

_source line 198 · 2026-05-20T04:19:56.365372+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://api.github.com/repos/moojink/openvla-oft/contents/experiments/robot/libero",
  "prompt": "Return complete listing of all files and directories with name, path, type."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_openvla-oft-survey_20260520T040517",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://api.github.com/repos/moojink/openvla-oft/contents/experiments/robot/libero",
    "prompt": "Return complete listing of all files and directories with name, path, type."
  }
}
```

</details>

---

### Tool call

_source line 199 · 2026-05-20T04:19:56.365505+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://arxiv.org/abs/2510.14836",
  "prompt": "Extract ALL details about QDepth-VLA: How do they use depth prediction as auxiliary supervision for VLA models? What is the architecture - where is the depth head attached? What VLA backbone do they use? How do they quantize depth? What is the training procedure? How does depth supervision improve manipulation performance? Could this approach extend to occupancy prediction?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_openvla-oft-survey_20260520T040517",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://arxiv.org/abs/2510.14836",
    "prompt": "Extract ALL details about QDepth-VLA: How do they use depth prediction as auxiliary supervision for VLA models? What is the architecture - where is the depth head attached? What VLA backbone do they use? How do they quantize depth? What is the training procedure? How does depth supervision improve manipulation performance? Could this approach extend to occupancy prediction?"
  }
}
```

</details>

---

### Tool result

_source line 200 · 2026-05-20T04:19:56.365626+00:00_

# File Listing

Based on the provided content, here are all files in the `experiments/robot/libero/` directory:

| Name | Path | Type |
|------|------|------|
| libero_requirements.txt | experiments/robot/libero/libero_requirements.txt | file |
| libero_utils.py | experiments/robot/libero/libero_utils.py | file |
| regenerate_libero_dataset.py | experiments/robot/libero/regenerate_libero_dataset.py | file |
| run_libero_eval.py | experiments/robot/libero/run_libero_eval.py | file |
| sample_libero_spatial_observation.pkl | experiments/robot/libero/sample_libero_spatial_observation.pkl | file |

All five items are individual files with no subdirectories listed in this directory snapshot.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_openvla-oft-survey_20260520T040517",
  "tool": "WebFetch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 201 · 2026-05-20T04:19:56.365771+00:00_

# QDepth-VLA: Analysis Based on Available Information

Based on the arXiv abstract provided, I can only offer limited details, as the full paper content isn't included in your source material.

## What We Know

**Core Concept:**
The approach augments Vision-Language-Action models with auxiliary depth prediction. According to the abstract, they employ "a dedicated depth expert" to "predict quantized latent tokens of depth maps obtained from a VQ-VAE encoder."

**Key Technical Element:**
The depth prediction uses quantized representations rather than continuous depth values, processed through a variational autoencoder framework.

**Claimed Benefits:**
The work demonstrates that this approach yields "strong spatial reasoning and competitive performance on manipulation tasks" across both simulated and real-world evaluation settings.

## Information Gaps

Unfortunately, the webpage excerpt doesn't contain the full technical details needed to answer your specific questions about:
- Exact architecture (where the depth head connects)
- Specific VLA backbone used
- Detailed training procedures
- Quantization methodology specifics
- Performance metrics on manipulation tasks
- Potential extensions to occupancy prediction

To obtain these details, you would need to access the full PDF or HTML version of the paper via the arXiv links provided.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_openvla-oft-survey_20260520T040517",
  "tool": "WebFetch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 202 · 2026-05-20T04:19:56.365909+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://arxiv.org/html/2510.14836",
  "prompt": "Extract ALL details about QDepth-VLA: 1) What VLA backbone? 2) Where is the depth head attached in the architecture? 3) How is depth quantized (VQ-VAE details)? 4) How does auxiliary depth supervision improve manipulation? 5) Training procedure? 6) What datasets? 7) Key results? 8) Could this extend to occupancy?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_openvla-oft-survey_20260520T040517",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://arxiv.org/html/2510.14836",
    "prompt": "Extract ALL details about QDepth-VLA: 1) What VLA backbone? 2) Where is the depth head attached in the architecture? 3) How is depth quantized (VQ-VAE details)? 4) How does auxiliary depth supervision improve manipulation? 5) Training procedure? 6) What datasets? 7) Key results? 8) Could this extend to occupancy?"
  }
}
```

</details>

---

### Tool result

_source line 203 · 2026-05-20T04:19:56.366064+00:00_

# Function Signatures and Implementations

## All Function Signatures

```python
model_is_on_hf_hub(model_path: str) -> bool

update_auto_map(pretrained_checkpoint: str) -> None

check_identical_files(path1: Union[str, Path], path2: Union[str, Path]) -> bool

_handle_file_sync(curr_filepath: str, checkpoint_filepath: str, file_type: str) -> None

check_model_logic_mismatch(pretrained_checkpoint: str) -> None

find_checkpoint_file(pretrained_checkpoint: str, file_pattern: str) -> str

load_component_state_dict(checkpoint_path: str) -> Dict[str, torch.Tensor]

get_vla(cfg: Any) -> torch.nn.Module

_apply_film_to_vla(vla: torch.nn.Module, cfg: Any) -> torch.nn.Module

_load_dataset_stats(vla: torch.nn.Module, checkpoint_path: str) -> None

get_processor(cfg: Any) -> AutoProcessor

get_proprio_projector(cfg: Any, llm_dim: int, proprio_dim: int) -> ProprioProjector

get_noisy_action_projector(cfg: Any, llm_dim: int) -> NoisyActionProjector

get_action_head(cfg: Any, llm_dim: int) -> Union[L1RegressionActionHead, DiffusionActionHead]

resize_image_for_policy(img: np.ndarray, resize_size: Union[int, Tuple[int, int]]) -> np.ndarray

crop_and_resize(image: tf.Tensor, crop_scale: float, batch_size: int) -> tf.Tensor

center_crop_image(image: Union[np.ndarray, Image.Image]) -> Image.Image

check_image_format(image: Any) -> None

normalize_proprio(proprio: np.ndarray, norm_stats: Dict[str, Any]) -> np.ndarray

prepare_images_for_vla(images: List[np.ndarray], cfg: Any) -> List[Image.Image]

get_vla_action(cfg: Any, vla: torch.nn.Module, processor: Any, obs: Dict[str, Any], 
               task_label: str, action_head: Optional[torch.nn.Module] = None, 
               proprio_projector: Optional[torch.nn.Module] = None, 
               noisy_action_projector: Optional[torch.nn.Module] = None, 
               use_film: bool = False) -> List[np.ndarray]

get_action_from_server(observation: Dict[str, Any], 
                      server_endpoint: str = "http://0.0.0.0:8777/act") -> D
…[truncated 7726 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_openvla-oft-survey_20260520T040517",
  "tool": "WebFetch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 204 · 2026-05-20T04:19:56.366217+00:00_

# QDepth-VLA: Key Technical Details

## 1) VLA Backbone
"PaliGemma-3B" which combines "SigLIP-based vision encoding with Gemma's language modeling capability."

## 2) Depth Head Architecture
The depth expert operates independently before language fusion. It takes "visual embeddings from the SigLIP encoder as input, before language fusion to avoid semantic interference," then processes them through "a lightweight MLP, processed by a transformer backbone, and then passed to a shallow CNN decoder that predicts 256 depth tokens."

## 3) VQ-VAE Quantization
Uses "K=256 codebook entries of dimension d=160" with a standard VQ-VAE objective. The encoder produces latent representations quantized to nearest codebook vectors via: "𝐳q=𝐜j∗, j∗=arg⁡minj‖𝐳e−𝐜j‖²" with latent grid resolutions of either 16×16 or 32×32 pixels.

## 4) Auxiliary Supervision Benefits
Depth supervision improves spatial reasoning by capturing "critical geometric cues" without disrupting the vision-language backbone's "pre-trained semantic alignment." The quantized approach reduces "redundant learning signals," focusing on "salient structural cues essential for manipulation" rather than pixel-level reconstruction.

## 5) Training Procedure
Co-trains action and depth objectives with exponentially decaying depth weight (λ₀=0.01). Uses AdamW optimizer with learning rate 5×10⁻⁵, cosine scheduler with 200 warmup steps over 10⁷ total steps, batch size 1024 across 8 H20 GPUs.

## 6) Datasets
Pre-training on Fractal and LIBERO-90; fine-tuning on LIBERO subsets (Spatial, Object, Goal, Long). Evaluated on Simpler benchmark (WidowX250, Google Robot). Real-world testing on Piper 6-DoF arm.

## 7) Key Results
- LIBERO single-view: 85.4% average success (6.1% above open π0)
- Simpler (WidowX250): 68.5% average, 39.6% on stacking
- Real-world: 42.5% average (10% improvement over baseline)

## 8) Occupancy Extension
Not addressed. Paper mentions "predicting future depth tokens for improved reasoning" as future work but do
…[truncated 61 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_openvla-oft-survey_20260520T040517",
  "tool": "WebFetch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 205 · 2026-05-20T04:19:56.366384+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://raw.githubusercontent.com/moojink/openvla-oft/main/experiments/robot/libero/run_libero_eval.py",
  "prompt": "Extract the GenerateConfig dataclass with ALL fields, types, and default values. Also extract the main evaluation loop logic - how does it run episodes, compute success rates, and which metrics does it track? Return the complete GenerateConfig class definition."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_openvla-oft-survey_20260520T040517",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://raw.githubusercontent.com/moojink/openvla-oft/main/experiments/robot/libero/run_libero_eval.py",
    "prompt": "Extract the GenerateConfig dataclass with ALL fields, types, and default values. Also extract the main evaluation loop logic - how does it run episodes, compute success rates, and which metrics does it track? Return the complete GenerateConfig class definition."
  }
}
```

</details>

---

### Tool call

_source line 206 · 2026-05-20T04:19:56.366519+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__read_project_file",
  "max_results": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_openvla-oft-survey_20260520T040517",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__read_project_file",
    "max_results": "1"
  }
}
```

</details>

---

### Tool result

_source line 207 · 2026-05-20T04:19:56.366638+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_openvla-oft-survey_20260520T040517",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 208 · 2026-05-20T04:19:56.366815+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://raw.githubusercontent.com/moojink/openvla-oft/main/experiments/robot/libero/libero_requirements.txt",
  "prompt": "Return the COMPLETE file content exactly as-is. Every line, every package, every version."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_openvla-oft-survey_20260520T040517",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://raw.githubusercontent.com/moojink/openvla-oft/main/experiments/robot/libero/libero_requirements.txt",
    "prompt": "Return the COMPLETE file content exactly as-is. Every line, every package, every version."
  }
}
```

</details>

---

### Tool result

_source line 209 · 2026-05-20T04:19:56.367023+00:00_

# Complete File Content

```
imageio[ffmpeg]
robosuite==1.4.1
bddl
easydict
cloudpickle
gym
```

This appears to be a Python dependencies file (likely `requirements.txt`) listing six packages. The file specifies one pinned version (robosuite at 1.4.1) while the others have no version constraints specified.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_openvla-oft-survey_20260520T040517",
  "tool": "WebFetch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 210 · 2026-05-20T04:19:56.367180+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://raw.githubusercontent.com/moojink/openvla-oft/main/prismatic/vla/datasets/rlds/oxe/transforms.py",
  "prompt": "Extract ALL LIBERO-related transform functions. Return the complete function definitions for any function that handles LIBERO data, including how it processes images, actions, and proprioceptive state. Show what keys it reads from the RLDS data."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_openvla-oft-survey_20260520T040517",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://raw.githubusercontent.com/moojink/openvla-oft/main/prismatic/vla/datasets/rlds/oxe/transforms.py",
    "prompt": "Extract ALL LIBERO-related transform functions. Return the complete function definitions for any function that handles LIBERO data, including how it processes images, actions, and proprioceptive state. Show what keys it reads from the RLDS data."
  }
}
```

</details>

---

### Tool result

_source line 211 · 2026-05-20T04:19:56.367313+00:00_

# GenerateConfig Dataclass and Evaluation Logic

## Complete GenerateConfig Class

```python
@dataclass
class GenerateConfig:
    # Model-specific parameters
    model_family: str = "openvla"
    pretrained_checkpoint: Union[str, Path] = ""
    use_l1_regression: bool = True
    use_diffusion: bool = False
    num_diffusion_steps_train: int = 50
    num_diffusion_steps_inference: int = 50
    use_film: bool = False
    num_images_in_input: int = 2
    use_proprio: bool = True
    center_crop: bool = True
    num_open_loop_steps: int = 8
    lora_rank: int = 32
    unnorm_key: Union[str, Path] = ""
    load_in_8bit: bool = False
    load_in_4bit: bool = False

    # LIBERO environment-specific parameters
    task_suite_name: str = TaskSuite.LIBERO_SPATIAL
    num_steps_wait: int = 10
    num_trials_per_task: int = 50
    initial_states_path: str = "DEFAULT"
    env_img_res: int = 256

    # Utility parameters
    run_id_note: Optional[str] = None
    local_log_dir: str = "./experiments/logs"
    use_wandb: bool = False
    wandb_entity: str = "your-wandb-entity"
    wandb_project: str = "your-wandb-project"
    seed: int = 7
```

## Evaluation Loop Logic

**Episode Execution:**
The script iterates through tasks and runs multiple trials per task. Each episode resets the environment, executes actions until task completion or max steps, and tracks success status. Actions are queried from the model in chunks and executed from a queue.

**Success Rate Computation:**
- Per-task: `task_successes / task_episodes`
- Overall: `total_successes / total_episodes`

**Tracked Metrics:**
- Episode count (total and per-task)
- Success count (total and per-task)
- Success rate percentages
- Per-task WandB logging with "success_rate/{task_description}" and "num_episodes/{task_description}"
- Overall WandB metrics for "success_rate/total" and "num_episodes/total"
- Rollout videos saved for each episode

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_openvla-oft-survey_20260520T040517",
  "tool": "WebFetch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 212 · 2026-05-20T04:19:56.367460+00:00_

# LIBERO Transform Function

The codebase contains one function handling LIBERO datasets:

```python
def libero_dataset_transform(trajectory: Dict[str, Any]) -> Dict[str, Any]:
    # gripper action is in -1 (open)...1 (close) --> clip to 0...1, flip --> +1 = open, 0 = close
    gripper_action = trajectory["action"][:, -1:]
    gripper_action = invert_gripper_actions(tf.clip_by_value(gripper_action, 0, 1))

    trajectory["action"] = tf.concat(
        [
            trajectory["action"][:, :6],
            gripper_action,
        ],
        axis=1,
    )
    trajectory["observation"]["EEF_state"] = trajectory["observation"]["state"][:, :6]
    trajectory["observation"]["gripper_state"] = trajectory["observation"]["state"][:, -2:]  # 2D gripper state
    return trajectory
```

## Processing Summary

**Input Keys Read:**
- `trajectory["action"]` — full action vector
- `trajectory["observation"]["state"]` — proprioceptive state

**Transformations:**
- Extracts first 6 action dimensions (xyz + rotation)
- Normalizes final gripper dimension from [-1, 1] range to [0, 1], then inverts it (1 = open, 0 = close)
- Extracts end-effector pose (first 6 state elements)
- Preserves 2-dimensional gripper state (last 2 state elements)

**Output Format:** Seven-dimensional action vector and structured observation with end-effector and gripper states.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_openvla-oft-survey_20260520T040517",
  "tool": "WebFetch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 213 · 2026-05-20T04:19:56.367608+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://raw.githubusercontent.com/moojink/openvla-oft/main/prismatic/vla/datasets/rlds/oxe/configs.py",
  "prompt": "Extract the COMPLETE configuration entry for all LIBERO datasets. I need the exact dict structure including all keys: image_obs_keys (primary, secondary, wrist), depth_obs_keys, state_obs_keys, state_encoding, action_encoding, action_key, state_key, proprio_obs_key, and any other fields. Return them as exact Python code."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_openvla-oft-survey_20260520T040517",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://raw.githubusercontent.com/moojink/openvla-oft/main/prismatic/vla/datasets/rlds/oxe/configs.py",
    "prompt": "Extract the COMPLETE configuration entry for all LIBERO datasets. I need the exact dict structure including all keys: image_obs_keys (primary, secondary, wrist), depth_obs_keys, state_obs_keys, state_encoding, action_encoding, action_key, state_key, proprio_obs_key, and any other fields. Return them as exact Python code."
  }
}
```

</details>

---

### Tool call

_source line 214 · 2026-05-20T04:19:56.367794+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://raw.githubusercontent.com/moojink/openvla-oft/main/prismatic/vla/datasets/datasets.py",
  "prompt": "Extract the RLDSBatchTransform class and RLDSDataset class complete implementations. I need to see how it constructs prompts, how it tokenizes actions, how it handles multi-image inputs, and how it processes proprioceptive state. Return ALL code in these classes."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_openvla-oft-survey_20260520T040517",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://raw.githubusercontent.com/moojink/openvla-oft/main/prismatic/vla/datasets/datasets.py",
    "prompt": "Extract the RLDSBatchTransform class and RLDSDataset class complete implementations. I need to see how it constructs prompts, how it tokenizes actions, how it handles multi-image inputs, and how it processes proprioceptive state. Return ALL code in these classes."
  }
}
```

</details>

---

### Tool result

_source line 215 · 2026-05-20T04:19:56.367948+00:00_

Based on the provided content, here are the complete LIBERO dataset configuration entries:

```python
"libero_spatial_no_noops": {
    "image_obs_keys": {"primary": "image", "secondary": None, "wrist": "wrist_image"},
    "depth_obs_keys": {"primary": None, "secondary": None, "wrist": None},
    "state_obs_keys": ["EEF_state", "gripper_state"],
    "state_encoding": StateEncoding.POS_EULER,
    "action_encoding": ActionEncoding.EEF_POS,
},
"libero_object_no_noops": {
    "image_obs_keys": {"primary": "image", "secondary": None, "wrist": "wrist_image"},
    "depth_obs_keys": {"primary": None, "secondary": None, "wrist": None},
    "state_obs_keys": ["EEF_state", "gripper_state"],
    "state_encoding": StateEncoding.POS_EULER,
    "action_encoding": ActionEncoding.EEF_POS,
},
"libero_goal_no_noops": {
    "image_obs_keys": {"primary": "image", "secondary": None, "wrist": "wrist_image"},
    "depth_obs_keys": {"primary": None, "secondary": None, "wrist": None},
    "state_obs_keys": ["EEF_state", "gripper_state"],
    "state_encoding": StateEncoding.POS_EULER,
    "action_encoding": ActionEncoding.EEF_POS,
},
"libero_10_no_noops": {
    "image_obs_keys": {"primary": "image", "secondary": None, "wrist": "wrist_image"},
    "depth_obs_keys": {"primary": None, "secondary": None, "wrist": None},
    "state_obs_keys": ["EEF_state", "gripper_state"],
    "state_encoding": StateEncoding.POS_EULER,
    "action_encoding": ActionEncoding.EEF_POS,
},
"libero_4_task_suites_no_noops": {
    "image_obs_keys": {"primary": "image", "secondary": None, "wrist": "wrist_image"},
    "depth_obs_keys": {"primary": None, "secondary": None, "wrist": None},
    "state_obs_keys": ["EEF_state", "gripper_state"],
    "state_encoding": StateEncoding.POS_EULER,
    "action_encoding": ActionEncoding.EEF_POS,
},
```

**Note:** The source document provides only these five fields for LIBERO datasets. Additional fields like `action_key`, `state_key`, or `proprio_obs_key` are not present in the supplied 
…[truncated 14 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_openvla-oft-survey_20260520T040517",
  "tool": "WebFetch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 216 · 2026-05-20T04:19:56.368097+00:00_

# RLDSBatchTransform and RLDSDataset Implementation

## RLDSBatchTransform Class

This dataclass converts RLDS batches to OpenVLA format. Key operations include:

**Prompt Construction**: Uses a `PromptBuilder` with a conversation format: `"What action should the robot take to {language_instruction}?"` paired with tokenized action sequences.

**Action Tokenization**: Processes current and future actions through an `ActionTokenizer`. The implementation concatenates current action tokens with future action chunk tokens (defined by `NUM_ACTIONS_CHUNK`).

**Multi-Image Handling**: Supports primary image plus optional wrist camera views. When `use_wrist_image=True`, it iterates through observation keys containing "wrist", applies `image_transform` to each, and concatenates into `pixel_values_wrist`.

**Proprioceptive State**: When `use_proprio=True` and proprioception exists in observations, it extracts `rlds_batch["observation"]["proprio"]` and includes it in the return dictionary.

**Loss Masking**: Sets `labels` to `IGNORE_INDEX` for all tokens except predicted action tokens using: `labels[: -(action_chunk_len + 1)] = IGNORE_INDEX`

## RLDSDataset Class

This IterableDataset wraps RLDS pipeline functionality:

**Configuration**: Resolves data mix names against `OXE_NAMED_MIXTURES`, automatically detecting "aloha" datasets to load specific camera views ("primary", "left_wrist", "right_wrist") versus standard layouts.

**Initialization**: Calls `make_interleaved_dataset()` with trajectory and frame transformation parameters, including window sizes, shuffle buffers, and optional image augmentation settings.

**Iteration**: Implements `__iter__()` to yield transformed batches via `batch_transform()`, and provides `__len__()` for dataset length reporting.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_openvla-oft-survey_20260520T040517",
  "tool": "WebFetch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 217 · 2026-05-20T04:19:56.368248+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://raw.githubusercontent.com/moojink/openvla-oft/main/prismatic/training/train_utils.py",
  "prompt": "Extract any learning rate scheduler logic, optimizer configuration, gradient clipping settings, and distributed training setup. Return the relevant function implementations."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_openvla-oft-survey_20260520T040517",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://raw.githubusercontent.com/moojink/openvla-oft/main/prismatic/training/train_utils.py",
    "prompt": "Extract any learning rate scheduler logic, optimizer configuration, gradient clipping settings, and distributed training setup. Return the relevant function implementations."
  }
}
```

</details>

---

### Tool call

_source line 218 · 2026-05-20T04:19:56.368385+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://raw.githubusercontent.com/moojink/openvla-oft/main/prismatic/models/registry.py",
  "prompt": "Return the COMPLETE file content. I need to see all registered model configurations."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_openvla-oft-survey_20260520T040517",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://raw.githubusercontent.com/moojink/openvla-oft/main/prismatic/models/registry.py",
    "prompt": "Return the COMPLETE file content. I need to see all registered model configurations."
  }
}
```

</details>

---

### Tool call

_source line 219 · 2026-05-20T04:19:56.368517+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://raw.githubusercontent.com/moojink/openvla-oft/main/experiments/robot/libero/run_libero_eval.py",
  "prompt": "Extract the complete evaluation loop code - the main function that runs episodes. I need to see how it steps through the environment, queries the VLA model for actions, handles action chunking, and determines success. Return the full main/evaluate function."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_openvla-oft-survey_20260520T040517",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://raw.githubusercontent.com/moojink/openvla-oft/main/experiments/robot/libero/run_libero_eval.py",
    "prompt": "Extract the complete evaluation loop code - the main function that runs episodes. I need to see how it steps through the environment, queries the VLA model for actions, handles action chunking, and determines success. Return the full main/evaluate function."
  }
}
```

</details>

---

### Tool result

_source line 220 · 2026-05-20T04:19:56.368644+00:00_

# Analysis of Web Page Content

Based on the provided code snippet, **there is no learning rate scheduler logic, optimizer configuration, gradient clipping settings, or distributed training setup present** in this utility module.

## What the Code Contains

The file contains only **four utility functions** for training validation:

1. `get_current_action_mask()` - Creates masks for current action tokens
2. `get_next_actions_mask()` - Creates masks for subsequent action tokens
3. `compute_token_accuracy()` - Calculates prediction accuracy against ground truth
4. `compute_actions_l1_loss()` - Computes L1 loss by decoding token IDs to continuous actions

## Conclusion

This appears to be a **metrics and masking utilities module** rather than a training configuration module. The requested training infrastructure elements (schedulers, optimizers, gradient clipping, distributed setup) are not implemented here. You would need to examine other files in the codebase—likely a main training script or configuration module—to locate those components.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_openvla-oft-survey_20260520T040517",
  "tool": "WebFetch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 221 · 2026-05-20T04:19:56.368803+00:00_

# Complete Model Registry Overview

The file contains a comprehensive registry of pretrained Vision-Language Models (VLMs) organized into several categories:

## Registry Structure
The `MODEL_REGISTRY` dictionary maps model IDs to metadata including names, descriptions, optimization procedures, visual representations, image processing methods, language models, datasets, and training epochs.

## Main Categories

**LLaVa v1.5 Reproductions**: Two baseline models (7B and 13B variants) using Vicuña language models with CLIP ViT-L/14 @ 336px.

**Optimization Procedure Variants** (Section 4.1): Single-stage vs. multi-stage approaches, including full fine-tuning experiments with 7B and 13B models.

**Visual Representation Experiments** (Section 4.2): Multiple vision encoders tested:
- ImageNet-21K+1K ViT-L
- DINOv2 ViT-L/14
- CLIP ViT-L/14 variants
- SigLIP ViT-SO models

Image processing methods compared include Letterbox, Resize Crop, and Naive Resize at various resolutions (224px, 336px, 384px).

**Language Model Variants** (Section 4.3): Llama-2, Mistral, Phi-2, and Llama-2 Chat models tested with different configurations.

**Scaling Studies** (Section 4.4): Training epoch variations (1.25 to 3 epochs) and multi-dataset combinations.

**Prism Models**: Final optimized configurations using DINOv2+SigLIP fusion at 384px and 224px, trained on combined datasets for 2 epochs with Llama-2 backbones (7B and 13B).

The file concludes with a `GLOBAL_REGISTRY` index mapping all model identifiers and names to their metadata.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_openvla-oft-survey_20260520T040517",
  "tool": "WebFetch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 222 · 2026-05-20T04:19:56.368942+00:00_

# Main Evaluation Loop

The primary evaluation function is `run_episode()`, which executes a single episode in the LIBERO environment. Here's how it operates:

## Episode Execution Flow

**Initialization:**
The function resets the environment and establishes an action queue with a maximum length of `cfg.num_open_loop_steps`. It tracks timesteps and collects replay images throughout execution.

**Step Loop:**
The episode runs until either success occurs or the maximum timestep limit is reached. For the initial `num_steps_wait` timesteps, dummy actions are executed to allow object stabilization in simulation.

**Action Management:**
When the action queue becomes empty, the system queries the VLA model via `get_action()`, passing the observation, task description, and model components. The returned action sequence populates the queue, enabling open-loop execution of multiple timesteps before requerying.

**Action Processing:**
Each action is normalized and potentially inverted based on the model family before execution in the environment.

**Success Detection:**
The episode terminates successfully when the environment returns `done=True`.

## Wrapper Function

`run_task()` orchestrates multiple episodes across trials for a single task, while the top-level `eval_libero()` function iterates through all tasks in the benchmark suite, aggregating success rates and logging results to both local files and Weights & Biases (when enabled).

The complete success calculation: `final_success_rate = total_successes / total_episodes`

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_openvla-oft-survey_20260520T040517",
  "tool": "WebFetch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 223 · 2026-05-20T04:19:56.369087+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://raw.githubusercontent.com/moojink/openvla-oft/main/vla-scripts/finetune.py",
  "prompt": "Extract the following specific code sections verbatim:\n1. The complete finetune() main function - the training loop, optimizer setup, LR scheduler, LoRA configuration\n2. The run_forward_pass() function completely\n3. How the model is loaded and LoRA is applied\n4. The learning rate warmup and decay logic\n5. Any gradient accumulation or clipping logic\nReturn all of these as exact code."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_openvla-oft-survey_20260520T040517",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://raw.githubusercontent.com/moojink/openvla-oft/main/vla-scripts/finetune.py",
    "prompt": "Extract the following specific code sections verbatim:\n1. The complete finetune() main function - the training loop, optimizer setup, LR scheduler, LoRA configuration\n2. The run_forward_pass() function completely\n3. How the model is loaded and LoRA is applied\n4. The learning rate warmup and decay logic\n5. Any gradient accumulation or clipping logic\nReturn all of these as exact code."
  }
}
```

</details>

---

### Tool result

_source line 224 · 2026-05-20T04:19:56.369225+00:00_

# OpenVLA Fine-tuning Code Sections

## 1. Main Training Loop (finetune function)

```python
with tqdm.tqdm(total=cfg.max_steps, leave=False) as progress:
    vla.train()
    optimizer.zero_grad()
    for batch_idx, batch in enumerate(dataloader):
        compute_diffusion_l1 = cfg.use_diffusion and batch_idx % cfg.diffusion_sample_freq == 0
        loss, metrics = run_forward_pass(
            vla=vla,
            action_head=action_head,
            noisy_action_projector=noisy_action_projector if cfg.use_diffusion else None,
            proprio_projector=proprio_projector if cfg.use_proprio else None,
            batch=batch,
            action_tokenizer=action_tokenizer,
            device_id=device_id,
            use_l1_regression=cfg.use_l1_regression,
            use_diffusion=cfg.use_diffusion,
            use_proprio=cfg.use_proprio,
            use_film=cfg.use_film,
            num_patches=NUM_PATCHES,
            compute_diffusion_l1=compute_diffusion_l1,
            num_diffusion_steps_train=cfg.num_diffusion_steps_train if cfg.use_diffusion else None,
        )

        normalized_loss = loss / cfg.grad_accumulation_steps
        normalized_loss.backward()

        for metric_name, value in metrics.items():
            if metric_name in recent_metrics:
                recent_metrics[metric_name].append(value)

        gradient_step_idx = batch_idx // cfg.grad_accumulation_steps
        smoothened_metrics = compute_smoothened_metrics(recent_metrics)
        log_step = gradient_step_idx if not cfg.resume else cfg.resume_step + gradient_step_idx
        
        if distributed_state.is_main_process and log_step % cfg.wandb_log_freq == 0:
            log_metrics_to_wandb(smoothened_metrics, "VLA Train", log_step, wandb)

        if cfg.lr_warmup_steps > 0:
            lr_progress = min((gradient_step_idx + 1) / cfg.lr_warmup_steps, 1.0)
            current_lr = original_lr * (0.1 + 0.9 * lr_progress)
            for param_group in optimizer.param_groups:

…[truncated 2598 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_openvla-oft-survey_20260520T040517",
  "tool": "WebFetch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 225 · 2026-05-20T04:19:56.369389+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://raw.githubusercontent.com/moojink/openvla-oft/main/vla-scripts/finetune.py",
  "prompt": "Extract the run_forward_pass() function COMPLETELY - every line of code. This is the most critical function. I need to see exactly how it handles:\n1. How input_ids, attention_mask, pixel_values are extracted from batch\n2. How proprioceptive state is projected\n3. How the VLA forward pass is called\n4. How L1 loss is computed on continuous actions\n5. How diffusion loss is computed\n6. What the return metrics are\nReturn the COMPLETE function code verbatim."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_openvla-oft-survey_20260520T040517",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://raw.githubusercontent.com/moojink/openvla-oft/main/vla-scripts/finetune.py",
    "prompt": "Extract the run_forward_pass() function COMPLETELY - every line of code. This is the most critical function. I need to see exactly how it handles:\n1. How input_ids, attention_mask, pixel_values are extracted from batch\n2. How proprioceptive state is projected\n3. How the VLA forward pass is called\n4. How L1 loss is computed on continuous actions\n5. How diffusion loss is computed\n6. What the return metrics are\nReturn the COMPLETE function code verbatim."
  }
}
```

</details>

---

### Tool call

_source line 226 · 2026-05-20T04:19:56.369530+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://raw.githubusercontent.com/moojink/openvla-oft/main/vla-scripts/finetune.py",
  "prompt": "Extract the optimizer creation code. Show me exactly which optimizer class is used (AdamW?), what parameters are passed (lr, weight_decay, betas), and what all components are optimized (VLA params, action head params, projector params). Return the code that creates the optimizer and adds parameter groups."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_openvla-oft-survey_20260520T040517",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://raw.githubusercontent.com/moojink/openvla-oft/main/vla-scripts/finetune.py",
    "prompt": "Extract the optimizer creation code. Show me exactly which optimizer class is used (AdamW?), what parameters are passed (lr, weight_decay, betas), and what all components are optimized (VLA params, action head params, projector params). Return the code that creates the optimizer and adds parameter groups."
  }
}
```

</details>

---

### Tool result

_source line 227 · 2026-05-20T04:19:56.369653+00:00_

# Optimizer Creation Code Analysis

The code uses **AdamW** optimizer with the following implementation:

```python
trainable_params = [param for param in vla.parameters() if param.requires_grad]
if cfg.use_l1_regression or cfg.use_diffusion:
    trainable_params += [param for param in action_head.parameters() if param.requires_grad]
if cfg.use_diffusion:
    trainable_params += [param for param in noisy_action_projector.parameters() if param.requires_grad]
if cfg.use_proprio:
    trainable_params += [param for param in proprio_projector.parameters() if param.requires_grad]
optimizer = AdamW(trainable_params, lr=cfg.learning_rate)
```

## Key Details

**Optimizer Class:** AdamW

**Parameters Passed:**
- `lr=cfg.learning_rate` (default 5e-4)
- No explicit weight_decay or betas specified (using PyTorch defaults)

**Components Optimized:**
1. Vision-language-action model parameters
2. Action head (L1 regression or diffusion variants, if enabled)
3. Noisy action projector (diffusion-only)
4. Proprioceptive projector (if enabled)

All parameter groups are combined into a single list and passed to AdamW without separate parameter group configurations.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_openvla-oft-survey_20260520T040517",
  "tool": "WebFetch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 228 · 2026-05-20T04:19:56.369890+00:00_



Here is the comprehensive research report.

---

## 1. SafeLIBERO Dataset

**URL**: https://huggingface.co/datasets/THURCSCT/SafeLIBERO

**SafeLIBERO is evaluation-only, not a training dataset.** It provides scene initialization files (`.pruned_init`) for evaluation episodes, not demonstration trajectories. The HuggingFace release contains initialization state vectors, not HDF5 demonstration data.

**Structure**: 4 suites × 4 tasks × 2 safety levels = 32 scenarios, 50 episodes each = 1,600 evaluation episodes total. 638 MB.

**Safety levels**:
- Level I: Obstacle in close proximity to target object
- Level II: Obstacle obstructs the movement path

**Init file format**: Each `.pruned_init` file has 50 lines (one per episode), each a concatenated state vector:
```
[Robot qpos] + [Obj_1 Pose(7)] + ... + [Obj_N Pose(7)] + [Robot qvel] + [Obj_1 Vel(6)] + ... + [Obj_N Vel(6)]
```
Object pose = `[x, y, z, qw, qx, qy, qz]`; velocity = `[vx, vy, vz, wx, wy, wz]`.

**Obstacles**: Moka pots, storage boxes, milk cartons, wine bottles, mugs, books. Positions randomized within small ranges. Collision detected via displacement threshold (`> 0.001`).

**Critical finding: SafeLIBERO does NOT include**:
- Training demonstrations (it is eval-only)
- Obstacle annotations (bounding boxes, masks, occupancy)
- Depth data or 3D representations
- Any data suitable for training an auxiliary occupancy head

The underlying observation/action space inherits from LIBERO: 7-DoF actions (3D position + 3D rotation + 1 gripper), RGB images from agentview + wrist camera, 8D proprioception (EE position, axis-angle orientation, gripper state).

---

## 2. VLSA-AEGIS (arXiv:2512.11891)

**URL**: https://arxiv.org/abs/2512.11891 | Project: https://vlsa-aegis.github.io/

**Approach**: Plug-and-play safety constraint (SC) layer applied as **post-processing** on VLA action outputs. Zero training required — purely optimization-based at inference.

**Architecture pipeline**:
1. VLA backbone generates action
…[truncated 7673 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_openvla-oft-survey_20260520T040517",
  "tool": "Agent",
  "elapsed_ms": 25
}
```

</details>

---

### Tool result

_source line 229 · 2026-05-20T04:19:56.370071+00:00_

Here is the complete `run_forward_pass()` function extracted verbatim from the code:

```python
def run_forward_pass(
    vla,
    action_head,
    noisy_action_projector,
    proprio_projector,
    batch,
    action_tokenizer,
    device_id,
    use_l1_regression,
    use_diffusion,
    use_proprio,
    use_film,
    num_patches,
    compute_diffusion_l1=False,
    num_diffusion_steps_train=None,
) -> Tuple[torch.Tensor, Dict[str, float]]:
    """
    Compute model forward pass and metrics for both training and validation.

    Args:
        vla (OpenVLAForActionPrediction): Vision-language-action policy.
        action_head (nn.Module): Action head module.
        noisy_action_projector (nn.Module): Noisy action projector module (only used for diffusion).
        proprio_projector (nn.Module): Proprioceptive state projector module.
        batch (dict): Input batch.
        action_tokenizer (ActionTokenizer): Action tokenizer.
        device_id (str): Device ID.
        use_l1_regression (bool): Whether to use L1 regression.
        use_diffusion (bool): Whether to use diffusion.
        use_proprio (bool): Whether to use proprioceptive state as input.
        use_film (bool): Whether to use FiLM for better language following.
        num_patches (int): Number of vision patches.
        compute_diffusion_l1 (bool): Whether to sample actions and compute L1 loss for diffusion (do this once every
                                    diffusion_sample_freq steps during training; do it every batch for validation)
        num_diffusion_steps_train (int): Number of diffusion steps for training (only used for diffusion).

    Returns:
        tuple: (loss, metrics_dict)
            loss: The loss tensor with gradient for backpropagation.
            metrics_dict: Dictionary of computed metrics (detached values for logging).
    """
    metrics = {}

    # Get ground-truth action labels
    ground_truth_actions = batch["actions"].to(device_id).to(torch.bfloat16)

    # [Only
…[truncated 6160 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_openvla-oft-survey_20260520T040517",
  "tool": "WebFetch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 230 · 2026-05-20T04:19:56.370239+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://api.github.com/repos/moojink/openvla-oft/contents/prismatic/models/vlms",
  "prompt": "Return complete listing of all files and directories with name, path, type."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_openvla-oft-survey_20260520T040517",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://api.github.com/repos/moojink/openvla-oft/contents/prismatic/models/vlms",
    "prompt": "Return complete listing of all files and directories with name, path, type."
  }
}
```

</details>

---

### Tool result

_source line 231 · 2026-05-20T04:19:56.370366+00:00_

# File Listing

Based on the provided content, here are all files and directories:

| Name | Path | Type |
|------|------|------|
| __init__.py | prismatic/models/vlms/__init__.py | file |
| base_vlm.py | prismatic/models/vlms/base_vlm.py | file |
| prismatic.py | prismatic/models/vlms/prismatic.py | file |

All three items are Python files located within the `prismatic/models/vlms/` directory structure of the openvla-oft repository.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_openvla-oft-survey_20260520T040517",
  "tool": "WebFetch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 232 · 2026-05-20T04:19:56.370504+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://raw.githubusercontent.com/moojink/openvla-oft/main/prismatic/models/vlms/prismatic.py",
  "prompt": "Extract the forward() method and predict_action() method of the PrismaticVLM / OpenVLAForActionPrediction class. I need to see how it:\n1. Processes pixel_values through the vision backbone\n2. Projects vision embeddings into LLM space\n3. Handles proprio state injection\n4. Handles noisy action injection for diffusion\n5. Handles FiLM conditioning\n6. Runs the LLM forward pass\n7. Generates action predictions\nReturn the COMPLETE function code for these methods."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_openvla-oft-survey_20260520T040517",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://raw.githubusercontent.com/moojink/openvla-oft/main/prismatic/models/vlms/prismatic.py",
    "prompt": "Extract the forward() method and predict_action() method of the PrismaticVLM / OpenVLAForActionPrediction class. I need to see how it:\n1. Processes pixel_values through the vision backbone\n2. Projects vision embeddings into LLM space\n3. Handles proprio state injection\n4. Handles noisy action injection for diffusion\n5. Handles FiLM conditioning\n6. Runs the LLM forward pass\n7. Generates action predictions\nReturn the COMPLETE function code for these methods."
  }
}
```

</details>

---

### Tool result

_source line 233 · 2026-05-20T04:19:56.370649+00:00_

# Analysis of PrismaticVLM Forward Method

Based on the provided code, I can only see the **forward() method** from the PrismaticVLM class. There is **no predict_action() method** present in this document, and this code does not appear to be from an OpenVLAForActionPrediction class.

## What the Forward Method Does

The forward() method handles:

1. **Vision Processing**: Processes `pixel_values` through `self.vision_backbone` using gradient control based on training stage
2. **Projection**: Passes vision features through `self.projector` to align with LLM embedding dimensions
3. **Embedding Construction**: Creates multimodal embeddings by concatenating input embeddings with projected patch features
4. **Multimodal Indexing**: Manages mixed batches with both multimodal (image + text) and unimodal (text-only) samples
5. **LLM Forward Pass**: Feeds fused embeddings to `self.llm_backbone` for language modeling

## What's Missing

The document does **not contain**:
- A `predict_action()` method
- Proprioceptive state injection logic
- Noisy action injection for diffusion
- FiLM conditioning mechanisms
- Action prediction generation

**Note**: The code provided appears to be from a vision-language model (VLM) framework called Prismatic, not from an action prediction model. To analyze action prediction capabilities, you would need documentation from an OpenVLA-specific implementation.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_openvla-oft-survey_20260520T040517",
  "tool": "WebFetch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 234 · 2026-05-20T04:19:56.370814+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://raw.githubusercontent.com/moojink/openvla-oft/main/prismatic/models/vlas/openvla.py",
  "prompt": "Return the COMPLETE file content verbatim. Every single line of code, every import, every class definition, every method. This file is only ~5.8KB so it should all fit. Do not summarize at all."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_openvla-oft-survey_20260520T040517",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://raw.githubusercontent.com/moojink/openvla-oft/main/prismatic/models/vlas/openvla.py",
    "prompt": "Return the COMPLETE file content verbatim. Every single line of code, every import, every class definition, every method. This file is only ~5.8KB so it should all fit. Do not summarize at all."
  }
}
```

</details>

---

### Tool result

_source line 235 · 2026-05-20T04:19:56.370971+00:00_

# OpenVLA PyTorch Module

The provided file is a complete PyTorch implementation that wraps a PrismaticVLM model for robotic action prediction. Here's the complete content:

```python
"""
openvla.py

PyTorch Module defining OpenVLA as a lightweight wrapper around a PrismaticVLM; defines custom logic around
discretizing actions with the ActionTokenizer.
"""

from typing import Dict, List, Optional

import numpy as np
import torch
from PIL import Image
from transformers import LlamaTokenizerFast

from prismatic.models.vlms.prismatic import PrismaticVLM
from prismatic.overwatch import initialize_overwatch
from prismatic.vla.action_tokenizer import ActionTokenizer

# Initialize Overwatch =>> Wraps `logging.Logger`
overwatch = initialize_overwatch(__name__)


class OpenVLA(PrismaticVLM):
    def __init__(
        self,
        *args,
        norm_stats: Dict[str, Dict[str, Dict[str, Dict[str, List[float]]]]],
        action_tokenizer: ActionTokenizer,
        **kwargs,
    ) -> None:
        super().__init__(*args, **kwargs)
        self.norm_stats = norm_stats
        self.action_tokenizer = action_tokenizer

    @torch.inference_mode()
    def predict_action(
        self, image: Image, instruction: str, unnorm_key: Optional[str] = None, **kwargs: str
    ) -> np.ndarray:
        """
        Core function for VLA inference; maps input image and task instruction to continuous action (de-tokenizes).

        @param image: PIL Image as [height, width, 3]
        @param instruction: Task instruction string
        @param unnorm_key: Optional dataset name for retrieving un-normalizing statistics; if None, checks that model
                           was trained only on a single dataset, and retrieves those statistics.

        @return Unnormalized (continuous) action vector --> end-effector deltas.
        """
        image_transform, tokenizer = self.vision_backbone.image_transform, self.llm_backbone.tokenizer

        # Build VLA Prompt
        prompt_builder = self.get_p
…[truncated 4017 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_openvla-oft-survey_20260520T040517",
  "tool": "WebFetch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 236 · 2026-05-20T04:19:56.371131+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://github.com/moojink/transformers-openvla-oft",
  "prompt": "Extract the README content. What modifications does this fork make to the transformers library? What is the bidirectional attention modification? What models/files are changed?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_openvla-oft-survey_20260520T040517",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://github.com/moojink/transformers-openvla-oft",
    "prompt": "Extract the README content. What modifications does this fork make to the transformers library? What is the bidirectional attention modification? What models/files are changed?"
  }
}
```

</details>

---

### Tool call

_source line 237 · 2026-05-20T04:19:56.371266+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://raw.githubusercontent.com/moojink/openvla-oft/main/prismatic/models/vlms/prismatic.py",
  "prompt": "Extract the forward() method signature and implementation. I need to see ALL parameters it accepts, especially: proprio, proprio_projector, noisy_actions, noisy_action_projector, diffusion_timestep_embeddings, use_film. Show me how it injects proprioceptive state, noisy actions, and FiLM conditioning into the forward pass. Return the COMPLETE forward method."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_openvla-oft-survey_20260520T040517",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://raw.githubusercontent.com/moojink/openvla-oft/main/prismatic/models/vlms/prismatic.py",
    "prompt": "Extract the forward() method signature and implementation. I need to see ALL parameters it accepts, especially: proprio, proprio_projector, noisy_actions, noisy_action_projector, diffusion_timestep_embeddings, use_film. Show me how it injects proprioceptive state, noisy actions, and FiLM conditioning into the forward pass. Return the COMPLETE forward method."
  }
}
```

</details>

---

### Tool result

_source line 238 · 2026-05-20T04:19:56.371393+00:00_

# Forward Method Analysis

Based on the provided content, the `forward()` method signature is:

```python
def forward(
    self,
    input_ids: Optional[torch.LongTensor] = None,
    attention_mask: Optional[torch.Tensor] = None,
    pixel_values: Optional[torch.FloatTensor] = None,
    labels: Optional[torch.LongTensor] = None,
    inputs_embeds: Optional[torch.FloatTensor] = None,
    past_key_values: Optional[List[torch.FloatTensor]] = None,
    use_cache: Optional[bool] = None,
    output_attentions: Optional[bool] = None,
    output_hidden_states: Optional[bool] = None,
    return_dict: Optional[bool] = None,
    multimodal_indices: Optional[torch.LongTensor] = None,
) -> CausalLMOutputWithPast:
```

## Important Finding

**The parameters you're asking about are not present in this implementation.** The code does not include:
- `proprio` or `proprio_projector`
- `noisy_actions` or `noisy_action_projector`
- `diffusion_timestep_embeddings`
- `use_film`

This is a vision-language model (VLM) implementation focused on integrating visual features with text through a projection mechanism. The forward pass handles multimodal (image + text) and unimodal (text-only) data, but lacks the robotic/action-conditioning parameters you mentioned.

If you need those features, they may exist in a different module or a modified version of this codebase not shown in the provided excerpt.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_openvla-oft-survey_20260520T040517",
  "tool": "WebFetch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 239 · 2026-05-20T04:19:56.371535+00:00_

# Analysis of transformers-openvla-oft Fork

Based on the provided content, I cannot provide a comprehensive answer to your questions about this fork's specific modifications.

## What I Found

The page displays the standard Hugging Face Transformers library README, which describes the general library functionality: "🤗 Transformers provides thousands of pretrained models to perform tasks on different modalities such as text, vision, and audio."

However, **the actual repository-specific documentation is not included** in the content provided. The page shows:

- Standard navigation and file listings
- The main Transformers library overview
- An extensive list of supported model architectures (100+ models)
- General installation and usage instructions

## What's Missing

To answer your specific questions, I would need:

1. **Custom README sections** explaining fork-specific changes
2. **Documentation** about the "OFT" (Orthogonal Finetuning) modifications mentioned in the fork name
3. **File diffs** or change logs showing which files were modified
4. **Technical documentation** explaining the bidirectional attention modifications

## Recommendation

To get accurate information, you should:
- Check the fork's main branch directly on GitHub
- Review any CONTRIBUTING or documentation files in the repository
- Examine the commit history for implementation details
- Look for any research papers or technical specifications referenced in issues or PRs

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_openvla-oft-survey_20260520T040517",
  "tool": "WebFetch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 240 · 2026-05-20T04:19:56.371703+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://api.github.com/repos/moojink/transformers-openvla-oft/commits?per_page=10",
  "prompt": "Extract the commit messages and dates for all commits listed. What changes were made to the transformers library?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_openvla-oft-survey_20260520T040517",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://api.github.com/repos/moojink/transformers-openvla-oft/commits?per_page=10",
    "prompt": "Extract the commit messages and dates for all commits listed. What changes were made to the transformers library?"
  }
}
```

</details>

---

### Tool call

_source line 241 · 2026-05-20T04:19:56.371846+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://raw.githubusercontent.com/moojink/openvla-oft/main/prismatic/models/vlms/base_vlm.py",
  "prompt": "Return the COMPLETE file content. I need to see all class definitions, method signatures, and especially any forward() or predict_action() methods that accept proprio, noisy_actions, use_film parameters."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_openvla-oft-survey_20260520T040517",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://raw.githubusercontent.com/moojink/openvla-oft/main/prismatic/models/vlms/base_vlm.py",
    "prompt": "Return the COMPLETE file content. I need to see all class definitions, method signatures, and especially any forward() or predict_action() methods that accept proprio, noisy_actions, use_film parameters."
  }
}
```

</details>

---

### Tool result

_source line 242 · 2026-05-20T04:19:56.371970+00:00_

# Summary of base_vlm.py Content

The file contains an **abstract base class for Vision-Language Models (VLMs)** that inherits from `nn.Module`, `GenerationMixin`, and `ABC`.

## Key Class: VLM

**Initialization Parameters:**
- `model_family`, `model_id`: identifiers
- `vision_backbone`: VisionBackbone instance
- `llm_backbone`: LLMBackbone instance
- `enable_mixed_precision_training`: optional boolean flag

**Abstract Methods Required:**
- `from_pretrained()`: class method for loading checkpoints
- `get_prompt_builder()`: returns PromptBuilder instance
- `freeze_backbones()`: stage-based freezing logic
- `load_from_checkpoint()`: checkpoint loading with stage/directory parameters
- `get_fsdp_wrapping_policy()`: returns callable for distributed training
- `forward()`: main computation method accepting input_ids, attention_mask, pixel_values, labels, past_key_values, and generation flags

**Properties:**
- `device`: returns torch device of model parameters
- `config`: accesses underlying LLM configuration

## Important Note

The document explicitly states: **"This file does not contain any forward() methods that accept `proprio`, `noisy_actions`, or `use_film` parameters.** Those parameters appear absent from this abstract base class definition entirely.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_openvla-oft-survey_20260520T040517",
  "tool": "WebFetch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 243 · 2026-05-20T04:19:56.372104+00:00_

# Commit Messages and Dates

Here are the commits listed chronologically (most recent first):

1. **2025-02-25** - Moo Jin Kim: "Customize Llama modeling code for OpenVLA-OFT: Full bidirectional attention"

2. **2024-04-23** - ArthurZucker: "v4.40.1"

3. **2024-04-23** - Pedro Cuenca: "Make EosTokenCriteria compatible with mps (#30376)"

4. **2024-04-18** - Lysandre: "Release: v4.40.0"

5. **2024-04-18** - Younes Belkada: "FIX: Fixes unexpected behaviour for Llava / LLama & AWQ Fused modules"

6. **2024-04-18** - Abhi Venigalla: "Add DBRX Model (#29921)"

7. **2024-04-18** - fxmarty: "Do not drop mask with SDPA for more cases (#30311)"

8. **2024-04-18** - Arthur: "Revert 'Re-enable SDPA's FA2 path (#30070)'"

9. **2024-04-18** - Marc Sun: "Fix RecurrentGemma device_map (#30273)"

10. **2024-04-18** - fxmarty: "Add atol for sliding window test (#30303)"

## Summary of Changes

The transformers library received updates addressing attention mechanisms, model support, and bug fixes. Notable additions include a new DBRX model implementation and refinements to scaling-dot-product attention (SDPA) handling across multiple model architectures.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_openvla-oft-survey_20260520T040517",
  "tool": "WebFetch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 244 · 2026-05-20T04:19:56.372241+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://api.github.com/repos/moojink/transformers-openvla-oft/contents/src/transformers/models/llama",
  "prompt": "Return complete listing of all files with name, path, type."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_openvla-oft-survey_20260520T040517",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://api.github.com/repos/moojink/transformers-openvla-oft/contents/src/transformers/models/llama",
    "prompt": "Return complete listing of all files with name, path, type."
  }
}
```

</details>

---

### Tool result

_source line 245 · 2026-05-20T04:19:56.372361+00:00_

# File Listing for Llama Models Directory

| Name | Path | Type |
|------|------|------|
| __init__.py | src/transformers/models/llama/__init__.py | file |
| configuration_llama.py | src/transformers/models/llama/configuration_llama.py | file |
| convert_llama_weights_to_hf.py | src/transformers/models/llama/convert_llama_weights_to_hf.py | file |
| modeling_flax_llama.py | src/transformers/models/llama/modeling_flax_llama.py | file |
| modeling_llama.py | src/transformers/models/llama/modeling_llama.py | file |
| tokenization_llama.py | src/transformers/models/llama/tokenization_llama.py | file |
| tokenization_llama_fast.py | src/transformers/models/llama/tokenization_llama_fast.py | file |

All seven items are files located in the `src/transformers/models/llama/` directory within the moojink/transformers-openvla-oft repository.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_openvla-oft-survey_20260520T040517",
  "tool": "WebFetch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 246 · 2026-05-20T04:19:56.372497+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://raw.githubusercontent.com/moojink/transformers-openvla-oft/main/src/transformers/models/llama/modeling_llama.py",
  "prompt": "This is a large file. I ONLY need the modifications for OpenVLA-OFT. Search for and extract:\n1. Any code related to bidirectional attention - how is causal masking disabled/modified?\n2. Any code related to proprio/proprioceptive input injection\n3. Any code related to noisy_actions or diffusion\n4. Any code related to FiLM conditioning\n5. Any modifications to the forward() method of LlamaModel or LlamaForCausalLM that add new parameters\n6. Any comments mentioning \"OFT\", \"OpenVLA\", \"bidirectional\", \"action\", or \"parallel decoding\"\nReturn just the modified sections with enough context to understand the changes."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_openvla-oft-survey_20260520T040517",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://raw.githubusercontent.com/moojink/transformers-openvla-oft/main/src/transformers/models/llama/modeling_llama.py",
    "prompt": "This is a large file. I ONLY need the modifications for OpenVLA-OFT. Search for and extract:\n1. Any code related to bidirectional attention - how is causal masking disabled/modified?\n2. Any code related to proprio/proprioceptive input injection\n3. Any code related to noisy_actions or diffusion\n4. Any code related to FiLM conditioning\n5. Any modifications to the forward() method of LlamaModel or LlamaForCausalLM that add new parameters\n6. Any comments mentioning \"OFT\", \"OpenVLA\", \"bidirectional\", \"action\", or \"parallel decoding\"\nReturn just the modified sections with enough context to understand the changes."
  }
}
```

</details>

---

### Tool result

_source line 247 · 2026-05-20T04:19:56.372626+00:00_

Based on my search through this LLaMA model implementation file, I found **no evidence** of modifications for OpenVLA-OFT.

The code contains:
- Standard causal masking logic (no bidirectional attention modifications)
- No proprioceptive input injection
- No noisy_actions or diffusion-related code
- No FiLM conditioning layers
- No new parameters added to forward() methods for action prediction
- No comments mentioning "OFT", "OpenVLA", "bidirectional", "action", or "parallel decoding"

**Conclusion**: This is the vanilla LLaMA implementation from Hugging Face Transformers. The OpenVLA-OFT modifications must exist in a different file or as a separate adaptation layer not included in this document. You would need to check:
- A separate `modeling_openvla.py` or similar file
- Configuration files that specify architectural changes
- Wrapper classes that extend these base LLaMA classes

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_openvla-oft-survey_20260520T040517",
  "tool": "WebFetch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 248 · 2026-05-20T04:19:56.372783+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://api.github.com/repos/moojink/transformers-openvla-oft/contents/src/transformers/models/openvla",
  "prompt": "Return complete listing of all files with name, path, type."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_openvla-oft-survey_20260520T040517",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://api.github.com/repos/moojink/transformers-openvla-oft/contents/src/transformers/models/openvla",
    "prompt": "Return complete listing of all files with name, path, type."
  }
}
```

</details>

---

### Tool result

_source line 249 · 2026-05-20T04:19:56.372901+00:00_

Request failed with status code 404

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_openvla-oft-survey_20260520T040517",
  "tool": "WebFetch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 250 · 2026-05-20T04:19:56.373027+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://api.github.com/repos/moojink/transformers-openvla-oft/compare/v4.40.1...main",
  "prompt": "Return the list of all files changed in this comparison. Show the filenames and the type of change (added/modified/removed). Also extract any code diffs shown, especially related to attention masks, bidirectional attention, causal mask modifications."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_openvla-oft-survey_20260520T040517",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://api.github.com/repos/moojink/transformers-openvla-oft/compare/v4.40.1...main",
    "prompt": "Return the list of all files changed in this comparison. Show the filenames and the type of change (added/modified/removed). Also extract any code diffs shown, especially related to attention masks, bidirectional attention, causal mask modifications."
  }
}
```

</details>

---

### Tool result

_source line 251 · 2026-05-20T04:19:56.373143+00:00_

Request failed with status code 404

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_openvla-oft-survey_20260520T040517",
  "tool": "WebFetch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 252 · 2026-05-20T04:19:56.373267+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://github.com/moojink/transformers-openvla-oft/commit/HEAD",
  "prompt": "Extract the full diff of this commit. What files were changed? What code was added or modified? I need to see the actual code changes for bidirectional attention."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_openvla-oft-survey_20260520T040517",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://github.com/moojink/transformers-openvla-oft/commit/HEAD",
    "prompt": "Extract the full diff of this commit. What files were changed? What code was added or modified? I need to see the actual code changes for bidirectional attention."
  }
}
```

</details>

---

### Tool result

_source line 253 · 2026-05-20T04:19:56.373385+00:00_

# Commit Diff Summary

**File Changed:** `src/transformers/models/llama/modeling_llama.py`

**Changes:** 55 additions, 1 deletion

## Key Modifications

The commit modifies the attention mechanism in the Llama model to support bidirectional attention instead of the default causal (unidirectional) masking.

**Main changes:**

1. **Attention mask transformation (lines 719-723):** The code extracts the last row of the causal mask and duplicates it across all positions. As the developer explains: "To get this mask, we just take the last row of the old `causal_mask` and duplicate it all the way through to get the new mask."

2. **is_causal parameter (line 731):** Changed from `is_causal=causal_mask is None and q_len > 1` to `is_causal=False`, disabling the default lower triangular causal mask.

**Purpose:** The modification allows padding tokens to be properly masked (set to negative infinity) while enabling full bidirectional attention across all non-padded positions. This is particularly useful for OpenVLA-OFT applications where bidirectional context is beneficial.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_openvla-oft-survey_20260520T040517",
  "tool": "WebFetch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 254 · 2026-05-20T04:19:56.373524+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://raw.githubusercontent.com/moojink/openvla-oft/main/experiments/robot/libero/regenerate_libero_dataset.py",
  "prompt": "Return the COMPLETE file content. I need to understand how LIBERO data is converted to RLDS format - what fields are saved, how episodes are structured, what images/actions/states are included."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_openvla-oft-survey_20260520T040517",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://raw.githubusercontent.com/moojink/openvla-oft/main/experiments/robot/libero/regenerate_libero_dataset.py",
    "prompt": "Return the COMPLETE file content. I need to understand how LIBERO data is converted to RLDS format - what fields are saved, how episodes are structured, what images/actions/states are included."
  }
}
```

</details>

---

### Tool result

_source line 255 · 2026-05-20T04:19:56.373647+00:00_

# LIBERO Dataset Regeneration: Data Structure and Fields

Based on the script provided, here's how LIBERO data is structured and saved:

## Episode Structure

Episodes are organized hierarchically in HDF5 format under `data/demo_{i}/` groups, where each demo contains:

### Observation Data (`obs/` subgroup)
The script captures multiple observation modalities:
- **gripper_states**: Gripper joint positions
- **joint_states**: Robot joint positions
- **ee_states**: End-effector state combining position and orientation (axis-angle)
- **ee_pos** & **ee_ori**: Separated end-effector position and orientation
- **agentview_rgb**: Camera observations at 256x256 resolution
- **eye_in_hand_rgb**: Wrist-mounted camera imagery

### Action and State Data (episode-level)
- **actions**: Demonstration actions (filtered to exclude no-ops)
- **states**: Full simulator states
- **robot_states**: Concatenated gripper position, EEF position, and quaternion
- **rewards** & **dones**: Binary episode completion signals

## Key Processing Steps

The regeneration process performs three filtering operations:

1. **No-op filtering**: "Transitions with zero actions that do not change the robot's state" are removed using a threshold-based criterion
2. **Success filtering**: "Unsuccessful demonstrations" are excluded entirely
3. **Image rotation**: Images receive 180-degree rotation during RLDS conversion

## Data Preservation

Initial environment states are recorded separately in a JSON metainfo file, enabling reproducible episode initialization and success tracking per demonstration.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_openvla-oft-survey_20260520T040517",
  "tool": "WebFetch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 256 · 2026-05-20T04:19:56.373806+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://raw.githubusercontent.com/moojink/openvla-oft/main/ALOHA.md",
  "prompt": "Extract ALL hyperparameters mentioned for ALOHA training. I need: chunk size, action dim, proprio dim, learning rate, batch size, number of steps, GPU requirements, and any differences from LIBERO config."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_openvla-oft-survey_20260520T040517",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://raw.githubusercontent.com/moojink/openvla-oft/main/ALOHA.md",
    "prompt": "Extract ALL hyperparameters mentioned for ALOHA training. I need: chunk size, action dim, proprio dim, learning rate, batch size, number of steps, GPU requirements, and any differences from LIBERO config."
  }
}
```

</details>

---

### Tool result

_source line 257 · 2026-05-20T04:19:56.373929+00:00_

# ALOHA Training Hyperparameters

**Chunk Size:**
- "NUM_ACTIONS_CHUNK" set to 25 by default for 25 Hz control frequency, or 50 for 50 Hz systems

**Learning Rate & Schedule:**
- Initial: "5e-4" with decay after 50,000 steps
- Recommendation: decay to "5e-5" when loss plateaus

**Batch Size:**
- "batch_size 4" in sample command

**Training Steps:**
- "max_steps 100005" with validation every 10,000 steps

**Model Configuration:**
- 3 input images (1 third-person + 2 wrist cameras)
- "use_proprio True" for proprioceptive state
- "use_film True" for language grounding

**GPU Requirements:**
- Sample uses 8 GPUs: "torchrun --standalone --nnodes 1 --nproc-per-node X"

**Action Space Difference from LIBERO:**
- Critical distinction: "ALOHA robot action space is absolute joint angles" requiring "ACTION_PROPRIO_NORMALIZATION_TYPE" that avoids Q1-Q99 clipping, unlike LIBERO's relative end-effector pose normalization

**Action/Proprio Dimensions:**
- Not explicitly specified in provided content

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_openvla-oft-survey_20260520T040517",
  "tool": "WebFetch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 258 · 2026-05-20T04:19:56.374174+00:00_

Now I have comprehensive information. Let me compile the full report.

---

Here is the detailed technical extraction from the OpenVLA-OFT repository (https://github.com/moojink/openvla-oft):

## 1. Repository Structure

```
openvla-oft/
├── pyproject.toml              # Dependencies and project config
├── SETUP.md                    # Environment setup instructions
├── LIBERO.md                   # LIBERO benchmark fine-tuning/eval guide
├── ALOHA.md                    # ALOHA robot fine-tuning/eval guide
├── vla-scripts/
│   ├── finetune.py             # Main fine-tuning script (~48KB)
│   ├── deploy.py               # Deployment server
│   └── merge_lora_weights_and_save.py
├── prismatic/
│   ├── models/
│   │   ├── vlas/openvla.py     # OpenVLA wrapper (predict_action for inference)
│   │   ├── vlms/prismatic.py   # PrismaticVLM base (forward pass)
│   │   ├── action_heads.py     # L1Regression + Diffusion action heads
│   │   ├── film_vit_wrapper.py # FiLM language-conditioned ViT
│   │   ├── projectors.py       # ProprioProjector + NoisyActionProjector
│   │   └── load.py             # Model loading logic
│   ├── vla/
│   │   ├── constants.py        # Per-platform constants (LIBERO/ALOHA/BRIDGE)
│   │   ├── action_tokenizer.py # Discretize continuous actions to tokens
│   │   └── datasets/
│   │       ├── datasets.py     # RLDSBatchTransform, RLDSDataset
│   │       └── rlds/
│   │           └── oxe/
│   │               ├── configs.py    # Per-dataset RLDS configs
│   │               ├── mixtures.py   # Dataset mixture definitions
│   │               └── transforms.py # Per-dataset transforms (incl. LIBERO)
│   └── training/
│       └── train_utils.py      # Loss/accuracy utilities
├── experiments/robot/
│   ├── openvla_utils.py        # Inference utilities (get_vla, get_action_head, etc.)
│   └── libero/
│       ├── run_libero_eval.py  # LIBERO evaluation script
│       ├── regenerate_libero_dataset.py  # LIBERO -> RLDS conversion
│       └── libero_requireme
…[truncated 11910 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_openvla-oft-survey_20260520T040517",
  "tool": "Agent",
  "elapsed_ms": 30
}
```

</details>

---

### Tool call

_source line 259 · 2026-05-20T04:19:56.374366+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__save_project_file",
  "max_results": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_openvla-oft-survey_20260520T040517",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__save_project_file",
    "max_results": "1"
  }
}
```

</details>

---

### Tool result

_source line 260 · 2026-05-20T04:19:56.374495+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_openvla-oft-survey_20260520T040517",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 261 · 2026-05-20T04:19:56.374639+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/",
  "description": "List project directory"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_openvla-oft-survey_20260520T040517",
  "tool": "Bash",
  "tool_args": {
    "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/",
    "description": "List project directory"
  }
}
```

</details>

---

### Tool result

_source line 262 · 2026-05-20T04:19:56.374792+00:00_

AGENTS.md
ROADMAP.lock
ROADMAP.md
artifacts
decisions.lock
decisions.yaml
distill_tmp
docs
literature_map.yaml
logs
study_status.lock

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_openvla-oft-survey_20260520T040517",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 263 · 2026-05-20T04:19:56.374965+00:00_

called mcp__agent-ml-research__save_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__save_project_file</summary>

````json
{
  "project": "occsafe_vla",
  "file": "report.md",
  "content": "# OpenVLA-OFT 代码调研报告\n\n> 调研日期：2026-05-20\n\n---\n\n## 1. 官方仓库\n\n### OpenVLA (主仓库)\n- **URL**: https://github.com/openvla/openvla\n- **Stars**: ~6,200 | **Forks**: ~734\n- **License**: MIT\n- **维护状况**: 活跃，63 commits on main，2025年3月更新 README 链接 OFT\n- **论文**: [OpenVLA: An Open-Source Vision-Language-Action Model](https://arxiv.org/abs/2406.09246) (ICML 2024)\n- **机构**: Stanford, UC Berkeley, Google DeepMind, Toyota Research Institute\n\n### OpenVLA-OFT\n- **URL**: https://github.com/moojink/openvla-oft\n- **Stars**: ~1,200 | **Forks**: ~169\n- **License**: MIT\n- **项目主页**: https://openvla-oft.github.io/\n- **论文**: [Fine-Tuning Vision-Language-Action Models: Optimizing Speed and Success](https://arxiv.org/abs/2502.19645) (RSS 2025)\n- **作者**: Moo Jin Kim, Chelsea Finn, Percy Liang (Stanford)\n- **OFT 含义**: Optimized Fine-Tuning（非 Orthogonal Fine-Tuning）\n\n### SafeLIBERO / VLSA-AEGIS\n- **URL**: https://github.com/THU-RCSCT/vlsa-aegis | **Stars**: ~98\n- **License**: MIT\n- **论文**: [VLSA: Vision-Language-Action Models with Plug-and-Play Safety Constraint Layer](https://arxiv.org/abs/2512.11891)\n- **数据集**: https://huggingface.co/datasets/THURCSCT/SafeLIBERO (638 MB, eval-only)\n\n---\n\n## 2. 依赖和环境要求\n\n### Python 环境\n| 依赖 | 版本 |\n|------|------|\n| Python | 3.10 |\n| PyTorch | 2.2.0 |\n| torchvision | 0.17.0 |\n| transformers | **自定义 fork**: `git+https://github.com/moojink/transformers-openvla-oft.git` (双向注意力) |\n| peft | 0.11.1 |\n| timm | 0.9.10 |\n| flash-attn | 2.5.5 |\n| tensorflow | 2.15.0 (RLDS 数据加载) |\n| tensorflow_datasets | 4.9.3 |\n| diffusers | 0.30.3 |\n| accelerate | ≥0.25.0 |\n| dlimp | 自定义 fork: `git+https://github.com/moojink/dlimp_openvla` |\n| draccus | 0.8.0 |\n\n### 特殊依赖说明\n- **transformers 必须用自定义 fork**：修改了 `modeling_llama.py`，将 causal mask 替换为 bidirectional attention\n- **flash-attn 2.5.5**：需要 `pip install --no-build-isolation` 编译安装\n- **tensorflow**：仅用于 RLDS 数据加载，非训练依赖\n- **LIBERO 评估额外依赖**：robosuite==1.4.1, bddl, gym, imageio[ffmpeg]\n\n### GPU 显存要求\n\n| 场景 | 显存需求 | 说明 |\n|------|---------|------|\n| 推理 (LIBERO) | ~16 GB | 单 GPU |\n| 推理 (ALOHA, 3 images) | ~18 GB | 单 GPU |\n| 训练 batch_size=8 | ~62 GB | A100 80GB 刚好够 |\n| 训练 batch_size=8, 8 GPUs | ~62 GB × 8 | 论文实验配置 |\n\n**结论：A100 80GB 单卡可跑训练（batch_size=8），推理无压力。**\n\n### 参数高效方法支持\n- **LoRA**: 原生支持，默认开启 (`use_lora=True`, rank=32, alpha=16, target=\"all-linear\")\n- **QLoRA**: 代码中未见明确支持，但 PEFT 0.11.1 技术上可以配合 bitsandbytes\n- **Full fine-tuning**: 可关闭 LoRA，但显存需求极高（7.5B 参数）\n\n---\n\n## 3. Fine-tuning 流程\n\n### 训练脚本\n```bash\ntorchrun --standalone --nnodes 1 --nproc-per-node {NUM_GPUS} vla-scripts/finetune.py \\\n  --vla_path openvla/openvla-7b \\\n  --data_root_dir /PATH/TO/RLDS/DATASETS/ \\\n  --dataset_name libero_spatial_no_noops \\\n  --use_l1_regression True \\\n  --use_diffusion False \\\n  --use_film False \\\n  --num_images_in_input 2 \\\n  --use_proprio True \\\n  --batch_size 8 \\\n  --learning_rate 5e-4 \\\n  --num_steps_before_decay 100000 \\\n  --max_steps 150005 \\\n  --save_freq 10000 \\\n  --image_aug True \\\n  --lora_rank 32\n```\n\n### 默认超参数\n\n| 参数 | 值 | 说明 |\n|------|-----|------|\n| learning_rate | 5e-4 | AdamW |\n| batch_size | 8 | per-device |\n| max_steps | 200,000 (通用) / 150,005 (LIBERO) | — |\n| lr_warmup_steps | 0 | 可选线性 warmup |\n| num_steps_before_decay | 100,000 | 之后 LR × 0.1 |\n| lora_rank | 32 | — |\n| lora_alpha | 16 | min(rank, 16) |\n| lora_dropout | 0.0 | — |\n| image_aug | True | random crop + color jitter |\n| grad_accumulation_steps | 1 | — |\n| shuffle_buffer_size | 100,000 | RLDS streaming |\n\n### LR Schedule\n- `MultiStepLR(milestones=[100000], gamma=0.1)` — 在 100K step 衰减 10×\n- 可选 linear warmup (默认关闭)\n\n### 数据格式\n- **要求**: RLDS (TFRecord) 格式\n- **LIBERO 转换**: HDF5 → RLDS，使用 `experiments/robot/libero/regenerate_libero_dataset.py`\n- **预转换数据集**: `git clone git@hf.co:datasets/openvla/modified_libero_rlds` (~10 GB)\n- **OXE config 字段**:\n  - `image_obs_keys`: primary (agentview), wrist (eye_in_hand)\n  - `state_obs_keys`: EEF_state (6D), gripper_state (2D) → 8D proprio\n  - `action_encoding`: EEF_POS, 7D (xyz + rotation + gripper)\n\n### 训练时间估计\n- LIBERO 单 suite (500 demos): 150K steps，batch_size=8×8 GPUs\n- 论文用 A100/H100 集群\n- **单卡 A100 80GB 估计**: batch_size=8, ~150K steps ≈ **2-3 天**（基于 ~110 Hz throughput 和数据加载开销）\n\n### 已有 HuggingFace Checkpoints\n- `moojink/openvla-7b-oft-finetuned-libero-spatial` (150K steps)\n- `moojink/openvla-7b-oft-finetuned-libero-object` (150K)\n- `moojink/openvla-7b-oft-finetuned-libero-goal` (50K)\n- `moojink/openvla-7b-oft-finetuned-libero-10` (150K)\n- `moojink/openvla-7b-oft-finetuned-libero-spatial-object-goal-10` (300K, combined)\n\n---\n\n## 4. SafeLIBERO 适配\n\n### 现有 LIBERO 支持\nOpenVLA-OFT **原生支持 LIBERO fine-tuning**，包含：\n- 数据转换脚本 (`regenerate_libero_dataset.py`)\n- 预转换 RLDS 数据集 (HuggingFace)\n- 完整评估脚本 (`run_libero_eval.py`)\n- 每个 suite 的预训练 checkpoint\n\n### SafeLIBERO 兼容性分析\n\n| 维度 | OpenVLA-OFT 预期 | SafeLIBERO 实际 | 兼容性 |\n|------|-----------------|----------------|--------|\n| Action space | 7D (6 EE + 1 gripper) | 7D (相同) | ✅ 完全兼容 |\n| Observation | agentview RGB + wrist RGB | 相同（LIBERO 环境） | ✅ 完全兼容 |\n| Proprio | 8D (6 EEF + 2 gripper) | 相同（LIBERO 环境） | ✅ 完全兼容 |\n| 数据格式 | RLDS (TFRecord) | `.pruned_init` (仅初始化状态) | ⚠️ 不兼容 |\n| 训练数据 | 需要 demo trajectories | 无（eval-only benchmark） | ❌ 需要自己生成 |\n| 障碍物标注 | — | 仅初始位置 (in init vector) | ⚠️ 无逐帧标注 |\n\n### 关键发现\n**SafeLIBERO 是纯评估 benchmark，不提供训练数据。** 它提供的是：\n- 场景初始化文件 (obstacle 位置)\n- 碰撞检测逻辑 (displacement > 0.001)\n- 评估协议 (4 suites × 4 tasks × 2 levels × 50 episodes)\n\n### 适配工作清单\n\n1. **训练数据生成**（必须）\n   - 在 SafeLIBERO 场景中用现有 LIBERO policy 收集带障碍物的 demonstrations\n   - 或使用 scripted policy / teleoperation 生成 safety-aware demos\n   - 需要同时记录 occupancy ground truth（从 MuJoCo sim 中提取）\n\n2. **Occupancy 标注生成**（必须）\n   - 从 LIBERO 仿真环境中提取 3D 物体位置和碰撞体\n   - 生成 voxel occupancy grid（类似 BEV occupancy 或 3D voxel）\n   - 需要自定义 LIBERO wrapper 在每个 timestep 导出 occupancy\n\n3. **RLDS 格式扩展**（必须）\n   - 在 RLDS dataset 中添加 occupancy field\n   - 修改 `RLDSBatchTransform` 以加载 occupancy labels\n   - 修改 OXE config 添加 occupancy key\n\n4. **评估集成**（中等）\n   - 修改 `run_libero_eval.py` 在 SafeLIBERO 场景中评估\n   - 添加碰撞率 / obstacle avoidance rate 指标\n\n### 第三方相关工作\n\n| 项目 | 关系 | URL |\n|------|------|-----|\n| VLSA-AEGIS | 用 OpenVLA-OFT 作为 baseline，CBF safety layer | https://github.com/THU-RCSCT/vlsa-aegis |\n| QDepth-VLA | 最接近的 auxiliary head 先例（depth prediction） | arXiv:2510.14836 |\n| SafeVLA | CMDP + safe RL，NeurIPS 2025 Spotlight | https://github.com/PKU-Alignment/SafeVLA |\n| LIBERO-PRO | LIBERO 评估扩展 | https://github.com/Zxy-MLlab/LIBERO-PRO |\n\n---\n\n## 5. 占据辅助头集成可行性\n\n### 架构分析\n\nOpenVLA-OFT 的前向传播流程：\n```\nImages → [SigLIP + DINOv2] → 256 patches/image × 2 views = 512 visual tokens\n                                    ↓\nLanguage → Llama-2 tokenizer → text tokens\n                                    ↓\nProprio → ProprioProjector (2-layer MLP) → proprio token\n                                    ↓\n[visual tokens | text tokens | proprio token | action tokens] → Llama-2 (bidirectional)\n                                    ↓\nHidden states at action positions → L1RegressionActionHead → 8×7 continuous actions\n```\n\n### 可加入辅助头的位置\n\n| 位置 | 优势 | 劣势 | 先例 |\n|------|------|------|------|\n| **A) Vision encoder 输出后** (推荐) | 不干扰语言语义对齐；空间信息最丰富 | 仅视觉特征，无语言/proprio 上下文 | QDepth-VLA (在 SigLIP 输出后加 depth head) |\n| **B) LLM 最后层 hidden states** | 融合了全部信息 | 可能干扰 action 预测；occupancy 是空间任务 | — |\n| **C) FiLM ViT 中间层** | 有语言条件化的视觉特征 | 需要 `use_film=True` | — |\n\n**推荐方案 A**: 在 SigLIP+DINOv2 fused visual features 之后、投影到 LLM embedding 空间之前，分出一个 occupancy prediction branch。\n\n### Vision Encoder 输出规格\n\n| 属性 | 值 |\n|------|-----|\n| 输入分辨率 | 224×224 |\n| SigLIP patch size | 14×14 → 16×16 patches |\n| DINOv2 patch size | 14×14 → 16×16 patches |\n| 每张图输出 | 256 patch embeddings |\n| 特征维度 | SigLIP dim + DINOv2 dim (fused) → 投影到 4096 (llm_dim) |\n| 空间分辨率 | 16×16 per image |\n\n### Occupancy Head 设计建议\n\n```python\nclass OccupancyHead(nn.Module):\n    \"\"\"Auxiliary 3D occupancy prediction from visual features.\"\"\"\n    # Input: visual features [B, 256, D_fused] per image (2 views)\n    # Output: voxel occupancy [B, X, Y, Z] or BEV [B, H, W]\n    \n    def __init__(self, input_dim, voxel_size=(32, 32, 16)):\n        # Option 1: 简单 MLP + reshape (类似 QDepth-VLA)\n        # Option 2: Transformer decoder + 3D conv\n        # Option 3: BEV projection (2D, 更轻量)\n        pass\n```\n\n### 多任务/辅助损失先例\n\n| 方法 | 辅助任务 | 架构 | 损失权重策略 |\n|------|---------|------|-------------|\n| QDepth-VLA | 量化深度预测 | MLP + transformer + shallow CNN on SigLIP features | 指数衰减 λ₀=0.01 |\n| RT-2 | 无辅助，纯 action | — | — |\n| VLSA-AEGIS | 无训练，推理时 CBF | — | — |\n| **本项目 (提议)** | 3D occupancy prediction | Branch on fused ViT features | 待设计（可参考 QDepth-VLA 衰减策略） |\n\n### 训练策略建议\n- **Loss**: `L_total = L_action (L1) + λ * L_occupancy (BCE or focal loss)`\n- **λ schedule**: 参考 QDepth-VLA，用指数衰减 (λ₀=0.01, 逐步减小) 避免辅助任务干扰主任务\n- **LoRA 兼容性**: occupancy head 全参数训练，VLA backbone 仅 LoRA，不冲突\n- **梯度流**: occupancy head 梯度只回传到 vision encoder (或 detach，仅做 auxiliary supervision)\n\n---\n\n## 6. 风险与挑战\n\n### 高风险\n| 风险 | 影响 | 缓解措施 |\n|------|------|---------|\n| **Occupancy ground truth 生成**：SafeLIBERO 无现成标注，需从仿真中提取 | 阻塞整个 pipeline | 写 MuJoCo wrapper 提取 collision body 位置 → voxelization |\n| **自定义 transformers fork**：依赖作者修改版，版本锁定 | 后续升级困难 | 将 bidirectional attention patch 最小化，记录 diff |\n| **训练数据不足**：标准 LIBERO 每 suite 仅 500 demos，加上障碍物场景更少 | 辅助头欠拟合 | 在 sim 中批量生成 + 数据增强 |\n\n### 中等风险\n| 风险 | 影响 | 缓解措施 |\n|------|------|---------|\n| **辅助头干扰 action 预测**：多任务学习可能降低主任务性能 | 成功率下降 | 梯度 detach / 权重衰减 / 先冻结主任务再微调 |\n| **显存压力**：加入 occupancy head + 3D output 增加显存 | batch_size 需缩小 | 用 BEV (2D) 替代 3D voxel；或 gradient checkpointing |\n| **评估协议不统一**：SafeLIBERO 碰撞检测逻辑需嵌入评估脚本 | 结果不可比 | 严格复用 VLSA-AEGIS 评估代码 |\n\n### 低风险\n| 风险 | 影响 | 缓解措施 |\n|------|------|---------|\n| LoRA + 辅助头训练稳定性 | 训练不收敛 | 参考 QDepth-VLA 的 loss weight schedule |\n| RLDS 格式扩展 | 数据加载 bug | 单元测试 + 小 batch 验证 |\n\n---\n\n## 7. 预估工作量\n\n| 阶段 | 任务 | 预估时间 | 前置依赖 |\n|------|------|---------|---------|\n| **Phase 1: 环境搭建** | 配置 OpenVLA-OFT 训练环境，跑通原始 LIBERO fine-tuning | 2-3 天 | GPU 服务器就绪 |\n| **Phase 2: Baseline 复现** | 用预训练 checkpoint 在 SafeLIBERO 上评估，确认 baseline 数字 | 1-2 天 | Phase 1 |\n| **Phase 3: 数据生成** | 编写 MuJoCo wrapper 提取 occupancy GT；在 SafeLIBERO 场景中生成训练 demos | 5-7 天 | Phase 1 |\n| **Phase 4: 模型修改** | 实现 OccupancyHead，修改数据 pipeline，添加多任务 loss | 3-5 天 | Phase 3 |\n| **Phase 5: 训练** | 在 A100 上训练 occupancy-augmented OpenVLA-OFT | 3-5 天 (含调参) | Phase 4 |\n| **Phase 6: 评估** | SafeLIBERO 评估 + 消融实验 + 结果分析 | 3-4 天 | Phase 5 |\n| **总计** | — | **~3-4 周** | — |\n\n### 关键路径\n`环境搭建 → 数据生成 → 模型修改 → 训练 → 评估`\n\n数据生成 (Phase 3) 是最不确定的环节，可能因 MuJoCo/LIBERO 环境问题耗时更久。\n\n---\n\n## 8. 核心结论\n\n1. **OpenVLA-OFT 原生支持 LIBERO**，有完整的 fine-tuning pipeline 和预训练 checkpoint，适配成本低\n2. **SafeLIBERO 是 eval-only**，需要自行生成带 occupancy 标注的训练数据\n3. **辅助头最佳位置**：Vision encoder (SigLIP+DINOv2) 输出后，参考 QDepth-VLA 的设计\n4. **A100 80GB 单卡够用**（batch_size=8 训练 ~62GB），加 occupancy head 后可能需要降 batch 或用 gradient checkpointing\n5. **学术新颖性明确**：目前无人将 occupancy prediction 作为 auxiliary head 集成到 VLA 中，QDepth-VLA (depth) 和 VLSA-AEGIS (CBF) 分别验证了几何辅助监督和安全约束的可行性\n"
}
````

</details>

<details><summary>Recorded metadata</summary>

````json
{
  "recorded_role": "tool",
  "session": "worker_research_openvla-oft-survey_20260520T040517",
  "tool": "mcp__agent-ml-research__save_project_file",
  "tool_args": {
    "project": "occsafe_vla",
    "file": "report.md",
    "content": "# OpenVLA-OFT 代码调研报告\n\n> 调研日期：2026-05-20\n\n---\n\n## 1. 官方仓库\n\n### OpenVLA (主仓库)\n- **URL**: https://github.com/openvla/openvla\n- **Stars**: ~6,200 | **Forks**: ~734\n- **License**: MIT\n- **维护状况**: 活跃，63 commits on main，2025年3月更新 README 链接 OFT\n- **论文**: [OpenVLA: An Open-Source Vision-Language-Action Model](https://arxiv.org/abs/2406.09246) (ICML 2024)\n- **机构**: Stanford, UC Berkeley, Google DeepMind, Toyota Research Institute\n\n### OpenVLA-OFT\n- **URL**: https://github.com/moojink/openvla-oft\n- **Stars**: ~1,200 | **Forks**: ~169\n- **License**: MIT\n- **项目主页**: https://openvla-oft.github.io/\n- **论文**: [Fine-Tuning Vision-Language-Action Models: Optimizing Speed and Success](https://arxiv.org/abs/2502.19645) (RSS 2025)\n- **作者**: Moo Jin Kim, Chelsea Finn, Percy Liang (Stanford)\n- **OFT 含义**: Optimized Fine-Tuning（非 Orthogonal Fine-Tuning）\n\n### SafeLIBERO / VLSA-AEGIS\n- **URL**: https://github.com/THU-RCSCT/vlsa-aegis | **Stars**: ~98\n- **License**: MIT\n- **论文**: [VLSA: Vision-Language-Action Models with Plug-and-Play Safety Constraint Layer](https://arxiv.org/abs/2512.11891)\n- **数据集**: https://huggingface.co/datasets/THURCSCT/SafeLIBERO (638 MB, eval-only)\n\n---\n\n## 2. 依赖和环境要求\n\n### Python 环境\n| 依赖 | 版本 |\n|------|------|\n| Python | 3.10 |\n| PyTorch | 2.2.0 |\n| torchvision | 0.17.0 |\n| transformers | **自定义 fork**: `git+https://github.com/moojink/transformers-openvla-oft.git` (双向注意力) |\n| peft | 0.11.1 |\n| timm | 0.9.10 |\n| flash-attn | 2.5.5 |\n| tensorflow | 2.15.0 (RLDS 数据加载) |\n| tensorflow_datasets | 4.9.3 |\n| diffusers | 0.30.3 |\n| accelerate | ≥0.25.0 |\n| dlimp | 自定义 fork: `git+https://github.com/moojink/dlimp_openvla` |\n| draccus | 0.8.0 |\n\n### 特殊依赖说明\n- **transformers 必须用自定义 fork**：修改了 `modeling_llama.py`，将 causal mask 替换为 bidirectional attention\n- **flash-attn 2.5.5**：需要 `pip install --no-build-isolation` 编译安装\n- **tensorflow**：仅用于 RLDS 数据加载，非训练依赖\n- **LIBERO 评估额外依赖**：robosuite==1.4.1, bddl, gym, imageio[ffmpeg]\n\n### GPU 显存要求\n\n| 场景 | 显存需求 | 说明 |\n|------|---------|------|\n| 推理 (LIBERO) | ~16 GB | 单 GPU |\n| 推理 (ALOHA, 3 images) | ~18 GB | 单 GPU |\n| 训练 batch_size=8 | ~62 GB | A100 80GB 刚好够 |\n| 训练 batch_size=8, 8 GPUs | ~62 GB × 8 | 论文实验配置 |\n\n**结论：A100 80GB 单卡可跑训练（batch_size=8），推理无压力。**\n\n### 参数高效方法支持\n- **LoRA**: 原生支持，默认开启 (`use_lora=True`, rank=32, alpha=16, target=\"all-linear\")\n- **QLoRA**: 代码中未见明确支持，但 PEFT 0.11.1 技术上可以配合 bitsandbytes\n- **Full fine-tuning**: 可关闭 LoRA，但显存需求极高（7.5B 参数）\n\n---\n\n## 3. Fine-tuning 流程\n\n### 训练脚本\n```bash\ntorchrun --standalone --nnodes 1 --nproc-per-node {NUM_GPUS} vla-scripts/finetune.py \\\n  --vla_path openvla/openvla-7b \\\n  --data_root_dir /PATH/TO/RLDS/DATASETS/ \\\n  --dataset_name libero_spatial_no_noops \\\n  --use_l1_regression True \\\n  --use_diffusion False \\\n  --use_film False \\\n  --num_images_in_input 2 \\\n  --use_proprio True \\\n  --batch_size 8 \\\n  --learning_rate 5e-4 \\\n  --num_steps_before_decay 100000 \\\n  --max_steps 150005 \\\n  --save_freq 10000 \\\n  --image_aug True \\\n  --lora_rank 32\n```\n\n### 默认超参数\n\n| 参数 | 值 | 说明 |\n|------|-----|------|\n| learning_rate | 5e-4 | AdamW |\n| batch_size | 8 | per-device |\n| max_steps | 200,000 (通用) / 150,005 (LIBERO) | — |\n| lr_warmup_steps | 0 | 可选线性 warmup |\n| num_steps_before_decay | 100,000 | 之后 LR × 0.1 |\n| lora_rank | 32 | — |\n| lora_alpha | 16 | min(rank, 16) |\n| lora_dropout | 0.0 | — |\n| image_aug | True | random crop + color jitter |\n| grad_accumulation_steps | 1 | — |\n| shuffle_buffer_size | 100,000 | RLDS streaming |\n\n### LR Schedule\n- `MultiStepLR(milestones=[100000], gamma=0.1)` — 在 100K step 衰减 10×\n- 可选 linear warmup (默认关闭)\n\n### 数据格式\n- **要求**: RLDS (TFRecord) 格式\n- **LIBERO 转换**: HDF5 → RLDS，使用 `experiments/robot/libero/regenerate_libero_dataset.py`\n- **预转换数据集**: `git clone git@hf.co:datasets/openvla/modified_libero_rlds` (~10 GB)\n- **OXE config 字段**:\n  - `image_obs_keys`: primary (agentview), wrist (eye_in_hand)\n  - `state_obs_keys`: EEF_state (6D), gripper_state (2D) → 8D proprio\n  - `action_encoding`: EEF_POS, 7D (xyz + rotation + gripper)\n\n### 训练时间估计\n- LIBERO 单 suite (500 demos): 150K steps，batch_size=8×8 GPUs\n- 论文用 A100/H100 集群\n- **单卡 A100 80GB 估计**: batch_size=8, ~150K steps ≈ **2-3 天**（基于 ~110 Hz throughput 和数据加载开销）\n\n### 已有 HuggingFace Checkpoints\n- `moojink/openvla-7b-oft-finetuned-libero-spatial` (150K steps)\n- `moojink/openvla-7b-oft-finetuned-libero-object` (150K)\n- `moojink/openvla-7b-oft-finetuned-libero-goal` (50K)\n- `moojink/openvla-7b-oft-finetuned-libero-10` (150K)\n- `moojink/openvla-7b-oft-finetuned-libero-spatial-object-goal-10` (300K, combined)\n\n---\n\n## 4. SafeLIBERO 适配\n\n### 现有 LIBERO 支持\nOpenVLA-OFT **原生支持 LIBERO fine-tuning**，包含：\n- 数据转换脚本 (`regenerate_libero_dataset.py`)\n- 预转换 RLDS 数据集 (HuggingFace)\n- 完整评估脚本 (`run_libero_eval.py`)\n- 每个 suite 的预训练 checkpoint\n\n### SafeLIBERO 兼容性分析\n\n| 维度 | OpenVLA-OFT 预期 | SafeLIBERO 实际 | 兼容性 |\n|------|-----------------|----------------|--------|\n| Action space | 7D (6 EE + 1 gripper) | 7D (相同) | ✅ 完全兼容 |\n| Observation | agentview RGB + wrist RGB | 相同（LIBERO 环境） | ✅ 完全兼容 |\n| Proprio | 8D (6 EEF + 2 gripper) | 相同（LIBERO 环境） | ✅ 完全兼容 |\n| 数据格式 | RLDS (TFRecord) | `.pruned_init` (仅初始化状态) | ⚠️ 不兼容 |\n| 训练数据 | 需要 demo trajectories | 无（eval-only benchmark） | ❌ 需要自己生成 |\n| 障碍物标注 | — | 仅初始位置 (in init vector) | ⚠️ 无逐帧标注 |\n\n### 关键发现\n**SafeLIBERO 是纯评估 benchmark，不提供训练数据。** 它提供的是：\n- 场景初始化文件 (obstacle 位置)\n- 碰撞检测逻辑 (displacement > 0.001)\n- 评估协议 (4 suites × 4 tasks × 2 levels × 50 episodes)\n\n### 适配工作清单\n\n1. **训练数据生成**（必须）\n   - 在 SafeLIBERO 场景中用现有 LIBERO policy 收集带障碍物的 demonstrations\n   - 或使用 scripted policy / teleoperation 生成 safety-aware demos\n   - 需要同时记录 occupancy ground truth（从 MuJoCo sim 中提取）\n\n2. **Occupancy 标注生成**（必须）\n   - 从 LIBERO 仿真环境中提取 3D 物体位置和碰撞体\n   - 生成 voxel occupancy grid（类似 BEV occupancy 或 3D voxel）\n   - 需要自定义 LIBERO wrapper 在每个 timestep 导出 occupancy\n\n3. **RLDS 格式扩展**（必须）\n   - 在 RLDS dataset 中添加 occupancy field\n   - 修改 `RLDSBatchTransform` 以加载 occupancy labels\n   - 修改 OXE config 添加 occupancy key\n\n4. **评估集成**（中等）\n   - 修改 `run_libero_eval.py` 在 SafeLIBERO 场景中评估\n   - 添加碰撞率 / obstacle avoidance rate 指标\n\n### 第三方相关工作\n\n| 项目 | 关系 | URL |\n|------|------|-----|\n| VLSA-AEGIS | 用 OpenVLA-OFT 作为 baseline，CBF safety layer | https://github.com/THU-RCSCT/vlsa-aegis |\n| QDepth-VLA | 最接近的 auxiliary head 先例（depth prediction） | arXiv:2510.14836 |\n| SafeVLA | CMDP + safe RL，NeurIPS 2025 Spotlight | https://github.com/PKU-Alignment/SafeVLA |\n| LIBERO-PRO | LIBERO 评估扩展 | https://github.com/Zxy-MLlab/LIBERO-PRO |\n\n---\n\n## 5. 占据辅助头集成可行性\n\n### 架构分析\n\nOpenVLA-OFT 的前向传播流程：\n```\nImages → [SigLIP + DINOv2] → 256 patches/image × 2 views = 512 visual tokens\n                                    ↓\nLanguage → Llama-2 tokenizer → text tokens\n                                    ↓\nProprio → ProprioProjector (2-layer MLP) → proprio token\n                                    ↓\n[visual tokens | text tokens | proprio token | action tokens] → Llama-2 (bidirectional)\n                                    ↓\nHidden states at action positions → L1RegressionActionHead → 8×7 continuous actions\n```\n\n### 可加入辅助头的位置\n\n| 位置 | 优势 | 劣势 | 先例 |\n|------|------|------|------|\n| **A) Vision encoder 输出后** (推荐) | 不干扰语言语义对齐；空间信息最丰富 | 仅视觉特征，无语言/proprio 上下文 | QDepth-VLA (在 SigLIP 输出后加 depth head) |\n| **B) LLM 最后层 hidden states** | 融合了全部信息 | 可能干扰 action 预测；occupancy 是空间任务 | — |\n| **C) FiLM ViT 中间层** | 有语言条件化的视觉特征 | 需要 `use_film=True` | — |\n\n**推荐方案 A**: 在 SigLIP+DINOv2 fused visual features 之后、投影到 LLM embedding 空间之前，分出一个 occupancy prediction branch。\n\n### Vision Encoder 输出规格\n\n| 属性 | 值 |\n|------|-----|\n| 输入分辨率 | 224×224 |\n| SigLIP patch size | 14×14 → 16×16 patches |\n| DINOv2 patch size | 14×14 → 16×16 patches |\n| 每张图输出 | 256 patch embeddings |\n| 特征维度 | SigLIP dim + DINOv2 dim (fused) → 投影到 4096 (llm_dim) |\n| 空间分辨率 | 16×16 per image |\n\n### Occupancy Head 设计建议\n\n```python\nclass OccupancyHead(nn.Module):\n    \"\"\"Auxiliary 3D occupancy prediction from visual features.\"\"\"\n    # Input: visual features [B, 256, D_fused] per image (2 views)\n    # Output: voxel occupancy [B, X, Y, Z] or BEV [B, H, W]\n    \n    def __init__(self, input_dim, voxel_size=(32, 32, 16)):\n        # Option 1: 简单 MLP + reshape (类似 QDepth-VLA)\n        # Option 2: Transformer decoder + 3D conv\n        # Option 3: BEV projection (2D, 更轻量)\n        pass\n```\n\n### 多任务/辅助损失先例\n\n| 方法 | 辅助任务 | 架构 | 损失权重策略 |\n|------|---------|------|-------------|\n| QDepth-VLA | 量化深度预测 | MLP + transformer + shallow CNN on SigLIP features | 指数衰减 λ₀=0.01 |\n| RT-2 | 无辅助，纯 action | — | — |\n| VLSA-AEGIS | 无训练，推理时 CBF | — | — |\n| **本项目 (提议)** | 3D occupancy prediction | Branch on fused ViT features | 待设计（可参考 QDepth-VLA 衰减策略） |\n\n### 训练策略建议\n- **Loss**: `L_total = L_action (L1) + λ * L_occupancy (BCE or focal loss)`\n- **λ schedule**: 参考 QDepth-VLA，用指数衰减 (λ₀=0.01, 逐步减小) 避免辅助任务干扰主任务\n- **LoRA 兼容性**: occupancy head 全参数训练，VLA backbone 仅 LoRA，不冲突\n- **梯度流**: occupancy head 梯度只回传到 vision encoder (或 detach，仅做 auxiliary supervision)\n\n---\n\n## 6. 风险与挑战\n\n### 高风险\n| 风险 | 影响 | 缓解措施 |\n|------|------|---------|\n| **Occupancy ground truth 生成**：SafeLIBERO 无现成标注，需从仿真中提取 | 阻塞整个 pipeline | 写 MuJoCo wrapper 提取 collision body 位置 → voxelization |\n| **自定义 transformers fork**：依赖作者修改版，版本锁定 | 后续升级困难 | 将 bidirectional attention patch 最小化，记录 diff |\n| **训练数据不足**：标准 LIBERO 每 suite 仅 500 demos，加上障碍物场景更少 | 辅助头欠拟合 | 在 sim 中批量生成 + 数据增强 |\n\n### 中等风险\n| 风险 | 影响 | 缓解措施 |\n|------|------|---------|\n| **辅助头干扰 action 预测**：多任务学习可能降低主任务性能 | 成功率下降 | 梯度 detach / 权重衰减 / 先冻结主任务再微调 |\n| **显存压力**：加入 occupancy head + 3D output 增加显存 | batch_size 需缩小 | 用 BEV (2D) 替代 3D voxel；或 gradient checkpointing |\n| **评估协议不统一**：SafeLIBERO 碰撞检测逻辑需嵌入评估脚本 | 结果不可比 | 严格复用 VLSA-AEGIS 评估代码 |\n\n### 低风险\n| 风险 | 影响 | 缓解措施 |\n|------|------|---------|\n| LoRA + 辅助头训练稳定性 | 训练不收敛 | 参考 QDepth-VLA 的 loss weight schedule |\n| RLDS 格式扩展 | 数据加载 bug | 单元测试 + 小 batch 验证 |\n\n---\n\n## 7. 预估工作量\n\n| 阶段 | 任务 | 预估时间 | 前置依赖 |\n|------|------|---------|---------|\n| **Phase 1: 环境搭建** | 配置 OpenVLA-OFT 训练环境，跑通原始 LIBERO fine-tuning | 2-3 天 | GPU 服务器就绪 |\n| **Phase 2: Baseline 复现** | 用预训练 checkpoint 在 SafeLIBERO 上评估，确认 baseline 数字 | 1-2 天 | Phase 1 |\n| **Phase 3: 数据生成** | 编写 MuJoCo wrapper 提取 occupancy GT；在 SafeLIBERO 场景中生成训练 demos | 5-7 天 | Phase 1 |\n| **Phase 4: 模型修改** | 实现 OccupancyHead，修改数据 pipeline，添加多任务 loss | 3-5 天 | Phase 3 |\n| **Phase 5: 训练** | 在 A100 上训练 occupancy-augmented OpenVLA-OFT | 3-5 天 (含调参) | Phase 4 |\n| **Phase 6: 评估** | SafeLIBERO 评估 + 消融实验 + 结果分析 | 3-4 天 | Phase 5 |\n| **总计** | — | **~3-4 周** | — |\n\n### 关键路径\n`环境搭建 → 数据生成 → 模型修改 → 训练 → 评估`\n\n数据生成 (Phase 3) 是最不确定的环节，可能因 MuJoCo/LIBERO 环境问题耗时更久。\n\n---\n\n## 8. 核心结论\n\n1. **OpenVLA-OFT 原生支持 LIBERO**，有完整的 fine-tuning pipeline 和预训练 checkpoint，适配成本低\n2. **SafeLIBERO 是 eval-only**，需要自行生成带 occupancy 标注的训练数据\n3. **辅助头最佳位置**：Vision encoder (SigLIP+DINOv2) 输出后，参考 QDepth-VLA 的设计\n4. **A100 80GB 单卡够用**（batch_size=8 训练 ~62GB），加 occupancy head 后可能需要降 batch 或用 gradient checkpointing\n5. **学术新颖性明确**：目前无人将 occupancy prediction 作为 auxiliary head 集成到 VLA 中，QDepth-VLA (depth) 和 VLSA-AEGIS (CBF) 分别验证了几何辅助监督和安全约束的可行性\n"
  }
}
````

</details>

---

### Tool result

_source line 264 · 2026-05-20T04:19:56.375234+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"file 'report.md' is not writable via save_project_file. Writable: ['memory.md', 'paper_framing.md', 'writing_plan.yaml']. Use (auto-generated, not manually writable) instead.\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_openvla-oft-survey_20260520T040517",
  "tool": "mcp__agent-ml-research__save_project_file",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 265 · 2026-05-20T04:19:56.375444+00:00_

called Write

<details open><summary>🔧 Tool call — Write</summary>

````json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/artifacts/openvla_oft_survey.md",
  "content": "# OpenVLA-OFT 代码调研报告\n\n> 调研日期：2026-05-20\n\n---\n\n## 1. 官方仓库\n\n### OpenVLA (主仓库)\n- **URL**: https://github.com/openvla/openvla\n- **Stars**: ~6,200 | **Forks**: ~734\n- **License**: MIT\n- **维护状况**: 活跃，63 commits on main，2025年3月更新 README 链接 OFT\n- **论文**: [OpenVLA: An Open-Source Vision-Language-Action Model](https://arxiv.org/abs/2406.09246) (ICML 2024)\n- **机构**: Stanford, UC Berkeley, Google DeepMind, Toyota Research Institute\n\n### OpenVLA-OFT\n- **URL**: https://github.com/moojink/openvla-oft\n- **Stars**: ~1,200 | **Forks**: ~169\n- **License**: MIT\n- **项目主页**: https://openvla-oft.github.io/\n- **论文**: [Fine-Tuning Vision-Language-Action Models: Optimizing Speed and Success](https://arxiv.org/abs/2502.19645) (RSS 2025)\n- **作者**: Moo Jin Kim, Chelsea Finn, Percy Liang (Stanford)\n- **OFT 含义**: Optimized Fine-Tuning（非 Orthogonal Fine-Tuning）\n\n### SafeLIBERO / VLSA-AEGIS\n- **URL**: https://github.com/THU-RCSCT/vlsa-aegis | **Stars**: ~98\n- **License**: MIT\n- **论文**: [VLSA: Vision-Language-Action Models with Plug-and-Play Safety Constraint Layer](https://arxiv.org/abs/2512.11891)\n- **数据集**: https://huggingface.co/datasets/THURCSCT/SafeLIBERO (638 MB, eval-only)\n\n---\n\n## 2. 依赖和环境要求\n\n### Python 环境\n| 依赖 | 版本 |\n|------|------|\n| Python | 3.10 |\n| PyTorch | 2.2.0 |\n| torchvision | 0.17.0 |\n| transformers | **自定义 fork**: `git+https://github.com/moojink/transformers-openvla-oft.git` (双向注意力) |\n| peft | 0.11.1 |\n| timm | 0.9.10 |\n| flash-attn | 2.5.5 |\n| tensorflow | 2.15.0 (RLDS 数据加载) |\n| tensorflow_datasets | 4.9.3 |\n| diffusers | 0.30.3 |\n| accelerate | ≥0.25.0 |\n| dlimp | 自定义 fork: `git+https://github.com/moojink/dlimp_openvla` |\n| draccus | 0.8.0 |\n\n### 特殊依赖说明\n- **transformers 必须用自定义 fork**：修改了 `modeling_llama.py`，将 causal mask 替换为 bidirectional attention（55 行改动）\n- **flash-attn 2.5.5**：需要 `pip install packaging ninja && pip install \"flash-attn==2.5.5\" --no-build-isolation`\n- **tensorflow**：仅用于 RLDS 数据加载，非训练依赖\n- **LIBERO 评估额外依赖**：robosuite==1.4.1, bddl, gym, imageio[ffmpeg]\n\n### GPU 显存要求\n\n| 场景 | 显存需求 | 说明 |\n|------|---------|------|\n| 推理 (LIBERO) | ~16 GB | 单 GPU |\n| 推理 (ALOHA, 3 images) | ~18 GB | 单 GPU |\n| 训练 batch_size=8 | ~62 GB | A100 80GB 刚好够 |\n| 训练 batch_size=8, 8 GPUs | ~62 GB × 8 | 论文实验配置 |\n\n**结论：A100 80GB 单卡可跑训练（batch_size=8），推理无压力。**\n\n### 参数高效方法支持\n- **LoRA**: 原生支持，默认开启 (`use_lora=True`, rank=32, alpha=16, target=\"all-linear\")\n- **QLoRA**: 代码中未见明确支持，但 PEFT 0.11.1 技术上可以配合 bitsandbytes\n- **Full fine-tuning**: 可关闭 LoRA，但显存需求极高（7.5B 参数）\n\n---\n\n## 3. Fine-tuning 流程\n\n### 仓库目录结构\n```\nopenvla-oft/\n├── pyproject.toml\n├── SETUP.md / LIBERO.md / ALOHA.md\n├── vla-scripts/\n│   ├── finetune.py                  # 主训练脚本\n│   ├── deploy.py                    # 部署服务\n│   └── merge_lora_weights_and_save.py\n├── prismatic/\n│   ├── models/\n│   │   ├── vlas/openvla.py          # OpenVLA wrapper\n│   │   ├── vlms/prismatic.py        # PrismaticVLM base\n│   │   ├── action_heads.py          # L1Regression + Diffusion heads\n│   │   ├── film_vit_wrapper.py      # FiLM 语言条件化 ViT\n│   │   ├── projectors.py            # ProprioProjector + NoisyActionProjector\n│   │   └── load.py\n│   ├── vla/\n│   │   ├── constants.py             # 平台常量 (LIBERO/ALOHA/BRIDGE)\n│   │   ├── action_tokenizer.py\n│   │   └── datasets/                # RLDS 数据加载\n│   └── training/\n│       └── train_utils.py\n├── experiments/robot/\n│   ├── openvla_utils.py             # 推理工具函数\n│   └── libero/\n│       ├── run_libero_eval.py       # LIBERO 评估\n│       ├── regenerate_libero_dataset.py  # HDF5 → RLDS 转换\n│       └── libero_requirements.txt\n```\n\n### 训练命令\n```bash\ntorchrun --standalone --nnodes 1 --nproc-per-node {NUM_GPUS} vla-scripts/finetune.py \\\n  --vla_path openvla/openvla-7b \\\n  --data_root_dir /PATH/TO/RLDS/DATASETS/ \\\n  --dataset_name libero_spatial_no_noops \\\n  --use_l1_regression True \\\n  --use_diffusion False \\\n  --use_film False \\\n  --num_images_in_input 2 \\\n  --use_proprio True \\\n  --batch_size 8 \\\n  --learning_rate 5e-4 \\\n  --num_steps_before_decay 100000 \\\n  --max_steps 150005 \\\n  --save_freq 10000 \\\n  --image_aug True \\\n  --lora_rank 32\n```\n\n### 默认超参数\n\n| 参数 | 值 | 说明 |\n|------|-----|------|\n| learning_rate | 5e-4 | AdamW |\n| batch_size | 8 | per-device |\n| max_steps | 200,000 (通用) / 150,005 (LIBERO) | — |\n| lr_warmup_steps | 0 | 可选线性 warmup |\n| num_steps_before_decay | 100,000 | 之后 LR × 0.1 |\n| lora_rank | 32 | — |\n| lora_alpha | 16 | min(rank, 16) |\n| lora_dropout | 0.0 | — |\n| image_aug | True | random crop + color jitter |\n| grad_accumulation_steps | 1 | — |\n| shuffle_buffer_size | 100,000 | RLDS streaming |\n\n### LR Schedule\n- `MultiStepLR(milestones=[100000], gamma=0.1)` — 在 100K step 衰减 10×\n- 可选 linear warmup (默认关闭)\n\n### 数据格式\n- **要求**: RLDS (TFRecord) 格式\n- **LIBERO 转换**: HDF5 → RLDS，使用 `experiments/robot/libero/regenerate_libero_dataset.py`\n- **预转换数据集**: `git clone git@hf.co:datasets/openvla/modified_libero_rlds` (~10 GB)\n- **OXE config 字段**:\n  - `image_obs_keys`: primary (agentview), wrist (eye_in_hand)\n  - `state_obs_keys`: EEF_state (6D), gripper_state (2D) → 8D proprio\n  - `action_encoding`: EEF_POS, 7D (xyz + rotation + gripper)\n- **No-op 过滤**: 零动作 transition 在 RLDS 转换时移除\n- **图像**: 转换时旋转 180°，训练时 random crop augmentation\n\n### LIBERO 数据集名称\n- `libero_spatial_no_noops`\n- `libero_object_no_noops`\n- `libero_goal_no_noops`\n- `libero_10_no_noops`\n- `libero_4_task_suites_no_noops` (combined, 权重均为 1.0)\n\n### 训练时间估计\n- LIBERO 单 suite (500 demos): 150K steps\n- 论文用 8× A100/H100，batch_size=64-128 total\n- **单卡 A100 80GB 估计**: batch_size=8, ~150K steps ≈ **2-3 天**\n\n### 已有 HuggingFace Checkpoints\n| Checkpoint | Steps | 说明 |\n|-----------|-------|------|\n| `moojink/openvla-7b-oft-finetuned-libero-spatial` | 150K | — |\n| `moojink/openvla-7b-oft-finetuned-libero-object` | 150K | — |\n| `moojink/openvla-7b-oft-finetuned-libero-goal` | 50K | 注意 step 数不同 |\n| `moojink/openvla-7b-oft-finetuned-libero-10` | 150K | — |\n| `moojink/openvla-7b-oft-finetuned-libero-spatial-object-goal-10` | 300K | Combined model, 96.8% avg |\n\n### LIBERO 结果 (论文 Table I)\n\n**Third-person + wrist + proprio + language (modified dataset)**:\n\n| Policy | Spatial | Object | Goal | Long | Average |\n|--------|---------|--------|------|------|---------|\n| Diffusion Policy (scratch) | 78.3 | 92.5 | 68.3 | 50.5 | 72.4 |\n| OpenVLA (fine-tuned) | 84.7 | 88.4 | 79.2 | 53.7 | 76.5 |\n| pi0 (fine-tuned) | 96.8 | 98.8 | 95.8 | 85.2 | 94.2 |\n| **OpenVLA-OFT** | **97.6** | **98.4** | **97.9** | **94.5** | **97.1** |\n\n### 推理效率 (论文 Table II, A100)\n\n| Method | Throughput (Hz) | Latency (sec) |\n|--------|----------------|---------------|\n| OpenVLA (original) | 4.2 | 0.240 |\n| OpenVLA-OFT (L1) | 109.7 | 0.073 |\n| OpenVLA-OFT + extra inputs | 71.4 | 0.112 |\n\n26× throughput improvement, 3× lower latency.\n\n---\n\n## 4. SafeLIBERO 适配\n\n### 现有 LIBERO 支持\nOpenVLA-OFT **原生支持 LIBERO fine-tuning**，包含：\n- 数据转换脚本 (`regenerate_libero_dataset.py`)\n- 预转换 RLDS 数据集 (HuggingFace)\n- 完整评估脚本 (`run_libero_eval.py`)\n- 每个 suite 的预训练 checkpoint\n\n### SafeLIBERO 兼容性分析\n\n| 维度 | OpenVLA-OFT 预期 | SafeLIBERO 实际 | 兼容性 |\n|------|-----------------|----------------|--------|\n| Action space | 7D (6 EE + 1 gripper) | 7D (相同) | ✅ 完全兼容 |\n| Observation | agentview RGB + wrist RGB | 相同（LIBERO 环境） | ✅ 完全兼容 |\n| Proprio | 8D (6 EEF + 2 gripper) | 相同（LIBERO 环境） | ✅ 完全兼容 |\n| 数据格式 | RLDS (TFRecord) | `.pruned_init` (仅初始化状态) | ⚠️ 不兼容 |\n| 训练数据 | 需要 demo trajectories | 无（eval-only benchmark） | ❌ 需要自己生成 |\n| 障碍物标注 | — | 仅初始位置 (in init vector) | ⚠️ 无逐帧标注 |\n\n### 关键发现\n\n**SafeLIBERO 是纯评估 benchmark，不提供训练数据。** 它提供的是：\n- 场景初始化文件 (`.pruned_init`): 50 行，每行是 `[Robot qpos] + [Obj poses(7)] + [Robot qvel] + [Obj vels(6)]`\n- 碰撞检测逻辑 (displacement > 0.001)\n- 评估协议 (4 suites × 4 tasks × 2 levels × 50 episodes = 1,600 episodes)\n- 障碍物类型: Moka pots, storage boxes, milk cartons, wine bottles, mugs, books\n\n**VLSA-AEGIS 的方法**: 推理时 post-processing，不修改模型\n1. VLM (GLM-4.5V) 识别障碍物 → GroundingDINO 定位\n2. RGB-D → 点云 → DBSCAN 聚类 → MVEE 椭球拟合\n3. CBF-QP 约束求解: `u_safe = argmin ||u - u_vla||²` s.t. safety barrier\n4. 开销仅 0.356 ms (1.86% cycle time)\n5. 结果: +59.16% collision avoidance, +17.25% task success\n\n### 适配工作清单\n\n1. **训练数据生成**（必须，最高优先级）\n   - 在 SafeLIBERO 场景中用现有 LIBERO policy 收集带障碍物的 demonstrations\n   - 或使用 scripted policy / teleoperation 生成 safety-aware demos\n   - 需要同时记录 occupancy ground truth（从 MuJoCo sim 中提取）\n\n2. **Occupancy 标注生成**（必须）\n   - 从 LIBERO/MuJoCo 仿真环境中提取 3D 物体位置和碰撞体\n   - 生成 voxel occupancy grid 或 BEV occupancy map\n   - 需要自定义 LIBERO wrapper 在每个 timestep 导出\n\n3. **RLDS 格式扩展**（必须）\n   - 在 RLDS dataset 中添加 occupancy field\n   - 修改 `RLDSBatchTransform` 以加载 occupancy labels\n   - 修改 OXE config 添加 occupancy key\n\n4. **评估集成**（中等）\n   - 修改 `run_libero_eval.py` 在 SafeLIBERO 场景中评估\n   - 添加碰撞率 / obstacle avoidance rate 指标\n   - 严格复用 VLSA-AEGIS 评估代码保证可比性\n\n### 第三方相关工作\n\n| 项目 | 关系 | URL |\n|------|------|-----|\n| VLSA-AEGIS | 用 OpenVLA-OFT 作为 baseline，CBF safety layer (inference-only) | https://github.com/THU-RCSCT/vlsa-aegis |\n| QDepth-VLA | 最接近的 auxiliary head 先例（depth prediction on SigLIP features） | arXiv:2510.14836 |\n| SafeVLA | CMDP + safe RL, NeurIPS 2025 Spotlight | https://github.com/PKU-Alignment/SafeVLA |\n| CoFreeVLA | 双臂碰撞避免，learned risk estimator | arXiv:2601.21712 |\n| RoboOccWorld | 室内 3D occupancy 场景预测 (不含 VLA) | arXiv:2505.05512 |\n| LIBERO-PRO | LIBERO 评估扩展，含 OpenVLA 评估 | https://github.com/Zxy-MLlab/LIBERO-PRO |\n\n---\n\n## 5. 占据辅助头集成可行性\n\n### 架构分析\n\nOpenVLA-OFT 前向传播流程：\n```\nImages (224×224) → [SigLIP + DINOv2] → 256 patches/image × 2 views = 512 visual tokens\n                                              ↓ (3-layer MLP projector, GELU)\nLanguage → Llama-2 tokenizer → text tokens\n                                              ↓\nProprio → ProprioProjector (2-layer MLP, GELU) → proprio token\n                                              ↓\n[visual tokens | text tokens | proprio token | action tokens] → Llama-2 7B (bidirectional attn)\n                                              ↓\nHidden states at action positions → reshape to (B, chunk_len, action_dim * hidden_dim)\n                                              ↓\nL1RegressionActionHead (MLPResNet, 2 blocks) → 8×7 continuous actions\n```\n\n### 可加入辅助头的位置\n\n| 位置 | 优势 | 劣势 | 先例 |\n|------|------|------|------|\n| **A) Vision encoder 输出后** ⭐推荐 | 不干扰语言语义对齐；空间信息最丰富；16×16 空间结构保留 | 仅视觉特征，无语言/proprio 上下文 | QDepth-VLA |\n| B) LLM 最后层 hidden states | 融合了全部模态信息 | 可能干扰 action 预测；hidden states 已无空间结构 | — |\n| C) FiLM ViT 中间层 | 有语言条件化的视觉特征 | 需要 `use_film=True`；中间层特征不稳定 | — |\n\n### Vision Encoder 输出规格\n\n| 属性 | 值 |\n|------|-----|\n| 输入分辨率 | 224×224 |\n| SigLIP patch size | 14×14 → 16×16 grid |\n| DINOv2 patch size | 14×14 → 16×16 grid |\n| 每张图输出 | 256 patch embeddings |\n| 特征维度 | SigLIP dim + DINOv2 dim (fused) → 投影到 4096 (llm_dim) |\n| 空间分辨率 | 16×16 per image |\n| 双目输入 | 2 views × 256 = 512 visual tokens total |\n\n### OFT 6 项核心改动\n1. **Parallel decoding** — bidirectional attention (非 causal)\n2. **Action chunking** — LIBERO: K=8 steps, D=7 dims per step\n3. **Continuous action** — [-1, +1] 归一化，替代 256-bin 离散化\n4. **L1 regression head** — MLPResNet(2 blocks, input=llm_dim×ACTION_DIM, hidden=llm_dim)\n5. **Multi-image** — 共享 ViT 处理多视角，沿 sequence 拼接\n6. **FiLM conditioning** (OFT+ variant) — `x = (1+γ)⊙x + β`，per ViT block\n\n### Action Head 详细架构\n```python\n# L1RegressionActionHead\nMLPResNet(\n    num_blocks=2,\n    input_dim=llm_dim * ACTION_DIM,    # 4096 * 7 = 28672\n    hidden_dim=llm_dim,                 # 4096\n    output_dim=action_dim               # 7\n)\n# Input: hidden states at action positions, reshaped to (B, chunk_len, action_dim * hidden_dim)\n# Output: (B, chunk_len, action_dim) = (B, 8, 7) continuous actions\n# Loss: L1Loss\n```\n\n### LIBERO 平台常量\n```python\nNUM_ACTIONS_CHUNK = 8\nACTION_DIM = 7\nPROPRIO_DIM = 8\nACTION_TOKEN_BEGIN_IDX = 31743\n```\n\n### Occupancy Head 设计建议\n\n```python\nclass OccupancyHead(nn.Module):\n    \"\"\"Auxiliary occupancy prediction from fused ViT features.\"\"\"\n    # Input: visual features [B, 256, D_fused] per view (before LLM projection)\n    # Output: BEV occupancy [B, H, W] or 3D voxel [B, X, Y, Z]\n    \n    # Option 1: Lightweight MLP + reshape (类似 QDepth-VLA)\n    #   256 patches → MLP → 16×16 BEV grid → upsample → target resolution\n    \n    # Option 2: Cross-view transformer + 3D lifting\n    #   Dual-view features → cross-attention → 3D voxel queries → occupancy logits\n    \n    # Option 3: BEV projection (最轻量)\n    #   Flatten dual-view features → linear → BEV grid (H×W) → sigmoid\n```\n\n### 多任务/辅助损失先例\n\n| 方法 | 辅助任务 | 架构位置 | 损失权重策略 |\n|------|---------|---------|-------------|\n| QDepth-VLA | 量化深度预测 (VQ-VAE, K=256, 16×16) | SigLIP 输出后，LLM 融合前 | 指数衰减 λ₀=0.01 |\n| RT-2 | 无辅助 | — | — |\n| VLSA-AEGIS | 无训练 (inference-time CBF) | — | — |\n| **本项目 (提议)** | 3D occupancy / BEV occupancy | Fused ViT 输出后 | 参考 QDepth-VLA 衰减 |\n\n### 训练策略建议\n- **Loss**: `L_total = L_action (L1) + λ(t) * L_occupancy (BCE / focal loss)`\n- **λ schedule**: 参考 QDepth-VLA 指数衰减 (λ₀=0.01)，避免辅助任务干扰主任务收敛\n- **LoRA 兼容性**: occupancy head 全参数训练，VLA backbone 仅 LoRA，不冲突\n- **梯度流选择**:\n  - 方案 A: 梯度回传到 vision encoder (端到端，可能提升空间感知)\n  - 方案 B: detach visual features (纯 auxiliary supervision，更安全)\n  - 建议先 B 后 A\n\n---\n\n## 6. 风险与挑战\n\n### 高风险\n| 风险 | 影响 | 缓解措施 |\n|------|------|---------|\n| **Occupancy GT 生成困难** — SafeLIBERO 无现成标注，需从仿真提取 | 阻塞整个 pipeline | 写 MuJoCo wrapper 提取 collision body → voxelization；先用简化版 (BEV) 验证 |\n| **自定义 transformers fork** — 依赖作者修改版，版本锁定于 Llama-2 | 后续升级困难，与新版 transformers 不兼容 | 将 bidirectional attention patch 最小化并记录 diff；长期考虑 port 到 transformers 4.x |\n| **训练数据不足** — 标准 LIBERO 每 suite 仅 500 demos，SafeLIBERO 场景更少 | 辅助头欠拟合 | 在 sim 中批量生成 + 数据增强（obstacle 位置随机化） |\n\n### 中等风险\n| 风险 | 影响 | 缓解措施 |\n|------|------|---------|\n| **辅助头干扰 action 预测** — 多任务学习可能降低主任务性能 | 成功率下降 | 梯度 detach / 权重衰减 schedule / 先冻结主任务再联合训练 |\n| **显存压力** — 加入 occupancy head + 3D output 增加显存 | batch_size 需缩小 | 用 BEV (2D) 替代 3D voxel；gradient checkpointing；混合精度 |\n| **评估协议不统一** — SafeLIBERO 碰撞检测逻辑需嵌入评估脚本 | 结果与 VLSA-AEGIS 不可比 | 严格复用 VLSA-AEGIS 评估代码 |\n| **GPU 间 performance 差异** — 论文提到不同 GPU 上性能可能显著下降 | 在非 A100 上结果不稳定 | 统一使用 A100 80GB |\n\n### 低风险\n| 风险 | 影响 | 缓解措施 |\n|------|------|---------|\n| LoRA + 辅助头训练稳定性 | 训练不收敛 | 参考 QDepth-VLA 的 loss weight schedule |\n| RLDS 格式扩展 | 数据加载 bug | 单元测试 + 小 batch 验证 |\n| 评估时 center_crop 遗漏 | 性能异常低 | 文档已明确要求 `center_crop=True` |\n\n---\n\n## 7. 预估工作量\n\n| 阶段 | 任务 | 预估时间 | 前置依赖 |\n|------|------|---------|---------|\n| **Phase 1: 环境搭建** | 配置 OpenVLA-OFT 训练环境，安装依赖（含自定义 fork），跑通 inference | 2-3 天 | GPU 服务器就绪 |\n| **Phase 2: Baseline 复现** | 用预训练 checkpoint 在标准 LIBERO + SafeLIBERO 上评估，确认 baseline 数字 | 1-2 天 | Phase 1 |\n| **Phase 3: 数据 Pipeline** | 编写 MuJoCo wrapper 提取 occupancy GT；在 SafeLIBERO 场景中生成训练数据；转换为扩展 RLDS 格式 | 5-7 天 | Phase 1 |\n| **Phase 4: 模型修改** | 实现 OccupancyHead，修改 forward pass，添加多任务 loss，修改数据加载 | 3-5 天 | Phase 3 |\n| **Phase 5: 训练** | 在 A100 上训练 occupancy-augmented OpenVLA-OFT；调参 | 3-5 天 (含调参) | Phase 4 |\n| **Phase 6: 评估与消融** | SafeLIBERO 全评估 + 消融实验 + 结果分析 + 与 VLSA-AEGIS baseline 对比 | 3-4 天 | Phase 5 |\n| **总计** | — | **~3-4 周** | — |\n\n### 关键路径\n```\n环境搭建 (P1) → 数据 Pipeline (P3) → 模型修改 (P4) → 训练 (P5) → 评估 (P6)\n                  ↑ 最不确定环节\nBaseline 复现 (P2) 可与 P3 并行\n```\n\nPhase 3（数据生成）是最不确定的环节——MuJoCo/LIBERO 环境搭建和 occupancy 提取可能因版本兼容性问题耗时更久。\n\n---\n\n## 8. 核心结论\n\n1. **OpenVLA-OFT 原生支持 LIBERO**——有完整的 fine-tuning pipeline、预训练 checkpoint、评估脚本，适配成本低\n2. **SafeLIBERO 是 eval-only benchmark**——需要自行生成带 occupancy 标注的训练数据，这是最大工作量\n3. **辅助头最佳位置**：SigLIP+DINOv2 fused visual features 输出后（LLM projection 前），参考 QDepth-VLA 的设计\n4. **A100 80GB 单卡够用**（batch_size=8 训练 ~62GB），加 occupancy head 后用 BEV (2D) 可控制显存增量\n5. **学术新颖性明确**：目前无人将 occupancy prediction 作为 auxiliary head 集成到 VLA 中\n   - QDepth-VLA 验证了 auxiliary geometric supervision 可行（depth）\n   - VLSA-AEGIS 验证了 safety constraint + OpenVLA-OFT 可行（inference-only CBF）\n   - 本项目填补两者之间的 gap：learned occupancy-aware safety，端到端训练\n6. **License 无障碍**：OpenVLA-OFT (MIT)、SafeLIBERO (MIT)、VLSA-AEGIS (MIT) 均为开放许可\n"
}
````

</details>

<details><summary>Recorded metadata</summary>

````json
{
  "recorded_role": "tool",
  "session": "worker_research_openvla-oft-survey_20260520T040517",
  "tool": "Write",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/artifacts/openvla_oft_survey.md",
    "content": "# OpenVLA-OFT 代码调研报告\n\n> 调研日期：2026-05-20\n\n---\n\n## 1. 官方仓库\n\n### OpenVLA (主仓库)\n- **URL**: https://github.com/openvla/openvla\n- **Stars**: ~6,200 | **Forks**: ~734\n- **License**: MIT\n- **维护状况**: 活跃，63 commits on main，2025年3月更新 README 链接 OFT\n- **论文**: [OpenVLA: An Open-Source Vision-Language-Action Model](https://arxiv.org/abs/2406.09246) (ICML 2024)\n- **机构**: Stanford, UC Berkeley, Google DeepMind, Toyota Research Institute\n\n### OpenVLA-OFT\n- **URL**: https://github.com/moojink/openvla-oft\n- **Stars**: ~1,200 | **Forks**: ~169\n- **License**: MIT\n- **项目主页**: https://openvla-oft.github.io/\n- **论文**: [Fine-Tuning Vision-Language-Action Models: Optimizing Speed and Success](https://arxiv.org/abs/2502.19645) (RSS 2025)\n- **作者**: Moo Jin Kim, Chelsea Finn, Percy Liang (Stanford)\n- **OFT 含义**: Optimized Fine-Tuning（非 Orthogonal Fine-Tuning）\n\n### SafeLIBERO / VLSA-AEGIS\n- **URL**: https://github.com/THU-RCSCT/vlsa-aegis | **Stars**: ~98\n- **License**: MIT\n- **论文**: [VLSA: Vision-Language-Action Models with Plug-and-Play Safety Constraint Layer](https://arxiv.org/abs/2512.11891)\n- **数据集**: https://huggingface.co/datasets/THURCSCT/SafeLIBERO (638 MB, eval-only)\n\n---\n\n## 2. 依赖和环境要求\n\n### Python 环境\n| 依赖 | 版本 |\n|------|------|\n| Python | 3.10 |\n| PyTorch | 2.2.0 |\n| torchvision | 0.17.0 |\n| transformers | **自定义 fork**: `git+https://github.com/moojink/transformers-openvla-oft.git` (双向注意力) |\n| peft | 0.11.1 |\n| timm | 0.9.10 |\n| flash-attn | 2.5.5 |\n| tensorflow | 2.15.0 (RLDS 数据加载) |\n| tensorflow_datasets | 4.9.3 |\n| diffusers | 0.30.3 |\n| accelerate | ≥0.25.0 |\n| dlimp | 自定义 fork: `git+https://github.com/moojink/dlimp_openvla` |\n| draccus | 0.8.0 |\n\n### 特殊依赖说明\n- **transformers 必须用自定义 fork**：修改了 `modeling_llama.py`，将 causal mask 替换为 bidirectional attention（55 行改动）\n- **flash-attn 2.5.5**：需要 `pip install packaging ninja && pip install \"flash-attn==2.5.5\" --no-build-isolation`\n- **tensorflow**：仅用于 RLDS 数据加载，非训练依赖\n- **LIBERO 评估额外依赖**：robosuite==1.4.1, bddl, gym, imageio[ffmpeg]\n\n### GPU 显存要求\n\n| 场景 | 显存需求 | 说明 |\n|------|---------|------|\n| 推理 (LIBERO) | ~16 GB | 单 GPU |\n| 推理 (ALOHA, 3 images) | ~18 GB | 单 GPU |\n| 训练 batch_size=8 | ~62 GB | A100 80GB 刚好够 |\n| 训练 batch_size=8, 8 GPUs | ~62 GB × 8 | 论文实验配置 |\n\n**结论：A100 80GB 单卡可跑训练（batch_size=8），推理无压力。**\n\n### 参数高效方法支持\n- **LoRA**: 原生支持，默认开启 (`use_lora=True`, rank=32, alpha=16, target=\"all-linear\")\n- **QLoRA**: 代码中未见明确支持，但 PEFT 0.11.1 技术上可以配合 bitsandbytes\n- **Full fine-tuning**: 可关闭 LoRA，但显存需求极高（7.5B 参数）\n\n---\n\n## 3. Fine-tuning 流程\n\n### 仓库目录结构\n```\nopenvla-oft/\n├── pyproject.toml\n├── SETUP.md / LIBERO.md / ALOHA.md\n├── vla-scripts/\n│   ├── finetune.py                  # 主训练脚本\n│   ├── deploy.py                    # 部署服务\n│   └── merge_lora_weights_and_save.py\n├── prismatic/\n│   ├── models/\n│   │   ├── vlas/openvla.py          # OpenVLA wrapper\n│   │   ├── vlms/prismatic.py        # PrismaticVLM base\n│   │   ├── action_heads.py          # L1Regression + Diffusion heads\n│   │   ├── film_vit_wrapper.py      # FiLM 语言条件化 ViT\n│   │   ├── projectors.py            # ProprioProjector + NoisyActionProjector\n│   │   └── load.py\n│   ├── vla/\n│   │   ├── constants.py             # 平台常量 (LIBERO/ALOHA/BRIDGE)\n│   │   ├── action_tokenizer.py\n│   │   └── datasets/                # RLDS 数据加载\n│   └── training/\n│       └── train_utils.py\n├── experiments/robot/\n│   ├── openvla_utils.py             # 推理工具函数\n│   └── libero/\n│       ├── run_libero_eval.py       # LIBERO 评估\n│       ├── regenerate_libero_dataset.py  # HDF5 → RLDS 转换\n│       └── libero_requirements.txt\n```\n\n### 训练命令\n```bash\ntorchrun --standalone --nnodes 1 --nproc-per-node {NUM_GPUS} vla-scripts/finetune.py \\\n  --vla_path openvla/openvla-7b \\\n  --data_root_dir /PATH/TO/RLDS/DATASETS/ \\\n  --dataset_name libero_spatial_no_noops \\\n  --use_l1_regression True \\\n  --use_diffusion False \\\n  --use_film False \\\n  --num_images_in_input 2 \\\n  --use_proprio True \\\n  --batch_size 8 \\\n  --learning_rate 5e-4 \\\n  --num_steps_before_decay 100000 \\\n  --max_steps 150005 \\\n  --save_freq 10000 \\\n  --image_aug True \\\n  --lora_rank 32\n```\n\n### 默认超参数\n\n| 参数 | 值 | 说明 |\n|------|-----|------|\n| learning_rate | 5e-4 | AdamW |\n| batch_size | 8 | per-device |\n| max_steps | 200,000 (通用) / 150,005 (LIBERO) | — |\n| lr_warmup_steps | 0 | 可选线性 warmup |\n| num_steps_before_decay | 100,000 | 之后 LR × 0.1 |\n| lora_rank | 32 | — |\n| lora_alpha | 16 | min(rank, 16) |\n| lora_dropout | 0.0 | — |\n| image_aug | True | random crop + color jitter |\n| grad_accumulation_steps | 1 | — |\n| shuffle_buffer_size | 100,000 | RLDS streaming |\n\n### LR Schedule\n- `MultiStepLR(milestones=[100000], gamma=0.1)` — 在 100K step 衰减 10×\n- 可选 linear warmup (默认关闭)\n\n### 数据格式\n- **要求**: RLDS (TFRecord) 格式\n- **LIBERO 转换**: HDF5 → RLDS，使用 `experiments/robot/libero/regenerate_libero_dataset.py`\n- **预转换数据集**: `git clone git@hf.co:datasets/openvla/modified_libero_rlds` (~10 GB)\n- **OXE config 字段**:\n  - `image_obs_keys`: primary (agentview), wrist (eye_in_hand)\n  - `state_obs_keys`: EEF_state (6D), gripper_state (2D) → 8D proprio\n  - `action_encoding`: EEF_POS, 7D (xyz + rotation + gripper)\n- **No-op 过滤**: 零动作 transition 在 RLDS 转换时移除\n- **图像**: 转换时旋转 180°，训练时 random crop augmentation\n\n### LIBERO 数据集名称\n- `libero_spatial_no_noops`\n- `libero_object_no_noops`\n- `libero_goal_no_noops`\n- `libero_10_no_noops`\n- `libero_4_task_suites_no_noops` (combined, 权重均为 1.0)\n\n### 训练时间估计\n- LIBERO 单 suite (500 demos): 150K steps\n- 论文用 8× A100/H100，batch_size=64-128 total\n- **单卡 A100 80GB 估计**: batch_size=8, ~150K steps ≈ **2-3 天**\n\n### 已有 HuggingFace Checkpoints\n| Checkpoint | Steps | 说明 |\n|-----------|-------|------|\n| `moojink/openvla-7b-oft-finetuned-libero-spatial` | 150K | — |\n| `moojink/openvla-7b-oft-finetuned-libero-object` | 150K | — |\n| `moojink/openvla-7b-oft-finetuned-libero-goal` | 50K | 注意 step 数不同 |\n| `moojink/openvla-7b-oft-finetuned-libero-10` | 150K | — |\n| `moojink/openvla-7b-oft-finetuned-libero-spatial-object-goal-10` | 300K | Combined model, 96.8% avg |\n\n### LIBERO 结果 (论文 Table I)\n\n**Third-person + wrist + proprio + language (modified dataset)**:\n\n| Policy | Spatial | Object | Goal | Long | Average |\n|--------|---------|--------|------|------|---------|\n| Diffusion Policy (scratch) | 78.3 | 92.5 | 68.3 | 50.5 | 72.4 |\n| OpenVLA (fine-tuned) | 84.7 | 88.4 | 79.2 | 53.7 | 76.5 |\n| pi0 (fine-tuned) | 96.8 | 98.8 | 95.8 | 85.2 | 94.2 |\n| **OpenVLA-OFT** | **97.6** | **98.4** | **97.9** | **94.5** | **97.1** |\n\n### 推理效率 (论文 Table II, A100)\n\n| Method | Throughput (Hz) | Latency (sec) |\n|--------|----------------|---------------|\n| OpenVLA (original) | 4.2 | 0.240 |\n| OpenVLA-OFT (L1) | 109.7 | 0.073 |\n| OpenVLA-OFT + extra inputs | 71.4 | 0.112 |\n\n26× throughput improvement, 3× lower latency.\n\n---\n\n## 4. SafeLIBERO 适配\n\n### 现有 LIBERO 支持\nOpenVLA-OFT **原生支持 LIBERO fine-tuning**，包含：\n- 数据转换脚本 (`regenerate_libero_dataset.py`)\n- 预转换 RLDS 数据集 (HuggingFace)\n- 完整评估脚本 (`run_libero_eval.py`)\n- 每个 suite 的预训练 checkpoint\n\n### SafeLIBERO 兼容性分析\n\n| 维度 | OpenVLA-OFT 预期 | SafeLIBERO 实际 | 兼容性 |\n|------|-----------------|----------------|--------|\n| Action space | 7D (6 EE + 1 gripper) | 7D (相同) | ✅ 完全兼容 |\n| Observation | agentview RGB + wrist RGB | 相同（LIBERO 环境） | ✅ 完全兼容 |\n| Proprio | 8D (6 EEF + 2 gripper) | 相同（LIBERO 环境） | ✅ 完全兼容 |\n| 数据格式 | RLDS (TFRecord) | `.pruned_init` (仅初始化状态) | ⚠️ 不兼容 |\n| 训练数据 | 需要 demo trajectories | 无（eval-only benchmark） | ❌ 需要自己生成 |\n| 障碍物标注 | — | 仅初始位置 (in init vector) | ⚠️ 无逐帧标注 |\n\n### 关键发现\n\n**SafeLIBERO 是纯评估 benchmark，不提供训练数据。** 它提供的是：\n- 场景初始化文件 (`.pruned_init`): 50 行，每行是 `[Robot qpos] + [Obj poses(7)] + [Robot qvel] + [Obj vels(6)]`\n- 碰撞检测逻辑 (displacement > 0.001)\n- 评估协议 (4 suites × 4 tasks × 2 levels × 50 episodes = 1,600 episodes)\n- 障碍物类型: Moka pots, storage boxes, milk cartons, wine bottles, mugs, books\n\n**VLSA-AEGIS 的方法**: 推理时 post-processing，不修改模型\n1. VLM (GLM-4.5V) 识别障碍物 → GroundingDINO 定位\n2. RGB-D → 点云 → DBSCAN 聚类 → MVEE 椭球拟合\n3. CBF-QP 约束求解: `u_safe = argmin ||u - u_vla||²` s.t. safety barrier\n4. 开销仅 0.356 ms (1.86% cycle time)\n5. 结果: +59.16% collision avoidance, +17.25% task success\n\n### 适配工作清单\n\n1. **训练数据生成**（必须，最高优先级）\n   - 在 SafeLIBERO 场景中用现有 LIBERO policy 收集带障碍物的 demonstrations\n   - 或使用 scripted policy / teleoperation 生成 safety-aware demos\n   - 需要同时记录 occupancy ground truth（从 MuJoCo sim 中提取）\n\n2. **Occupancy 标注生成**（必须）\n   - 从 LIBERO/MuJoCo 仿真环境中提取 3D 物体位置和碰撞体\n   - 生成 voxel occupancy grid 或 BEV occupancy map\n   - 需要自定义 LIBERO wrapper 在每个 timestep 导出\n\n3. **RLDS 格式扩展**（必须）\n   - 在 RLDS dataset 中添加 occupancy field\n   - 修改 `RLDSBatchTransform` 以加载 occupancy labels\n   - 修改 OXE config 添加 occupancy key\n\n4. **评估集成**（中等）\n   - 修改 `run_libero_eval.py` 在 SafeLIBERO 场景中评估\n   - 添加碰撞率 / obstacle avoidance rate 指标\n   - 严格复用 VLSA-AEGIS 评估代码保证可比性\n\n### 第三方相关工作\n\n| 项目 | 关系 | URL |\n|------|------|-----|\n| VLSA-AEGIS | 用 OpenVLA-OFT 作为 baseline，CBF safety layer (inference-only) | https://github.com/THU-RCSCT/vlsa-aegis |\n| QDepth-VLA | 最接近的 auxiliary head 先例（depth prediction on SigLIP features） | arXiv:2510.14836 |\n| SafeVLA | CMDP + safe RL, NeurIPS 2025 Spotlight | https://github.com/PKU-Alignment/SafeVLA |\n| CoFreeVLA | 双臂碰撞避免，learned risk estimator | arXiv:2601.21712 |\n| RoboOccWorld | 室内 3D occupancy 场景预测 (不含 VLA) | arXiv:2505.05512 |\n| LIBERO-PRO | LIBERO 评估扩展，含 OpenVLA 评估 | https://github.com/Zxy-MLlab/LIBERO-PRO |\n\n---\n\n## 5. 占据辅助头集成可行性\n\n### 架构分析\n\nOpenVLA-OFT 前向传播流程：\n```\nImages (224×224) → [SigLIP + DINOv2] → 256 patches/image × 2 views = 512 visual tokens\n                                              ↓ (3-layer MLP projector, GELU)\nLanguage → Llama-2 tokenizer → text tokens\n                                              ↓\nProprio → ProprioProjector (2-layer MLP, GELU) → proprio token\n                                              ↓\n[visual tokens | text tokens | proprio token | action tokens] → Llama-2 7B (bidirectional attn)\n                                              ↓\nHidden states at action positions → reshape to (B, chunk_len, action_dim * hidden_dim)\n                                              ↓\nL1RegressionActionHead (MLPResNet, 2 blocks) → 8×7 continuous actions\n```\n\n### 可加入辅助头的位置\n\n| 位置 | 优势 | 劣势 | 先例 |\n|------|------|------|------|\n| **A) Vision encoder 输出后** ⭐推荐 | 不干扰语言语义对齐；空间信息最丰富；16×16 空间结构保留 | 仅视觉特征，无语言/proprio 上下文 | QDepth-VLA |\n| B) LLM 最后层 hidden states | 融合了全部模态信息 | 可能干扰 action 预测；hidden states 已无空间结构 | — |\n| C) FiLM ViT 中间层 | 有语言条件化的视觉特征 | 需要 `use_film=True`；中间层特征不稳定 | — |\n\n### Vision Encoder 输出规格\n\n| 属性 | 值 |\n|------|-----|\n| 输入分辨率 | 224×224 |\n| SigLIP patch size | 14×14 → 16×16 grid |\n| DINOv2 patch size | 14×14 → 16×16 grid |\n| 每张图输出 | 256 patch embeddings |\n| 特征维度 | SigLIP dim + DINOv2 dim (fused) → 投影到 4096 (llm_dim) |\n| 空间分辨率 | 16×16 per image |\n| 双目输入 | 2 views × 256 = 512 visual tokens total |\n\n### OFT 6 项核心改动\n1. **Parallel decoding** — bidirectional attention (非 causal)\n2. **Action chunking** — LIBERO: K=8 steps, D=7 dims per step\n3. **Continuous action** — [-1, +1] 归一化，替代 256-bin 离散化\n4. **L1 regression head** — MLPResNet(2 blocks, input=llm_dim×ACTION_DIM, hidden=llm_dim)\n5. **Multi-image** — 共享 ViT 处理多视角，沿 sequence 拼接\n6. **FiLM conditioning** (OFT+ variant) — `x = (1+γ)⊙x + β`，per ViT block\n\n### Action Head 详细架构\n```python\n# L1RegressionActionHead\nMLPResNet(\n    num_blocks=2,\n    input_dim=llm_dim * ACTION_DIM,    # 4096 * 7 = 28672\n    hidden_dim=llm_dim,                 # 4096\n    output_dim=action_dim               # 7\n)\n# Input: hidden states at action positions, reshaped to (B, chunk_len, action_dim * hidden_dim)\n# Output: (B, chunk_len, action_dim) = (B, 8, 7) continuous actions\n# Loss: L1Loss\n```\n\n### LIBERO 平台常量\n```python\nNUM_ACTIONS_CHUNK = 8\nACTION_DIM = 7\nPROPRIO_DIM = 8\nACTION_TOKEN_BEGIN_IDX = 31743\n```\n\n### Occupancy Head 设计建议\n\n```python\nclass OccupancyHead(nn.Module):\n    \"\"\"Auxiliary occupancy prediction from fused ViT features.\"\"\"\n    # Input: visual features [B, 256, D_fused] per view (before LLM projection)\n    # Output: BEV occupancy [B, H, W] or 3D voxel [B, X, Y, Z]\n    \n    # Option 1: Lightweight MLP + reshape (类似 QDepth-VLA)\n    #   256 patches → MLP → 16×16 BEV grid → upsample → target resolution\n    \n    # Option 2: Cross-view transformer + 3D lifting\n    #   Dual-view features → cross-attention → 3D voxel queries → occupancy logits\n    \n    # Option 3: BEV projection (最轻量)\n    #   Flatten dual-view features → linear → BEV grid (H×W) → sigmoid\n```\n\n### 多任务/辅助损失先例\n\n| 方法 | 辅助任务 | 架构位置 | 损失权重策略 |\n|------|---------|---------|-------------|\n| QDepth-VLA | 量化深度预测 (VQ-VAE, K=256, 16×16) | SigLIP 输出后，LLM 融合前 | 指数衰减 λ₀=0.01 |\n| RT-2 | 无辅助 | — | — |\n| VLSA-AEGIS | 无训练 (inference-time CBF) | — | — |\n| **本项目 (提议)** | 3D occupancy / BEV occupancy | Fused ViT 输出后 | 参考 QDepth-VLA 衰减 |\n\n### 训练策略建议\n- **Loss**: `L_total = L_action (L1) + λ(t) * L_occupancy (BCE / focal loss)`\n- **λ schedule**: 参考 QDepth-VLA 指数衰减 (λ₀=0.01)，避免辅助任务干扰主任务收敛\n- **LoRA 兼容性**: occupancy head 全参数训练，VLA backbone 仅 LoRA，不冲突\n- **梯度流选择**:\n  - 方案 A: 梯度回传到 vision encoder (端到端，可能提升空间感知)\n  - 方案 B: detach visual features (纯 auxiliary supervision，更安全)\n  - 建议先 B 后 A\n\n---\n\n## 6. 风险与挑战\n\n### 高风险\n| 风险 | 影响 | 缓解措施 |\n|------|------|---------|\n| **Occupancy GT 生成困难** — SafeLIBERO 无现成标注，需从仿真提取 | 阻塞整个 pipeline | 写 MuJoCo wrapper 提取 collision body → voxelization；先用简化版 (BEV) 验证 |\n| **自定义 transformers fork** — 依赖作者修改版，版本锁定于 Llama-2 | 后续升级困难，与新版 transformers 不兼容 | 将 bidirectional attention patch 最小化并记录 diff；长期考虑 port 到 transformers 4.x |\n| **训练数据不足** — 标准 LIBERO 每 suite 仅 500 demos，SafeLIBERO 场景更少 | 辅助头欠拟合 | 在 sim 中批量生成 + 数据增强（obstacle 位置随机化） |\n\n### 中等风险\n| 风险 | 影响 | 缓解措施 |\n|------|------|---------|\n| **辅助头干扰 action 预测** — 多任务学习可能降低主任务性能 | 成功率下降 | 梯度 detach / 权重衰减 schedule / 先冻结主任务再联合训练 |\n| **显存压力** — 加入 occupancy head + 3D output 增加显存 | batch_size 需缩小 | 用 BEV (2D) 替代 3D voxel；gradient checkpointing；混合精度 |\n| **评估协议不统一** — SafeLIBERO 碰撞检测逻辑需嵌入评估脚本 | 结果与 VLSA-AEGIS 不可比 | 严格复用 VLSA-AEGIS 评估代码 |\n| **GPU 间 performance 差异** — 论文提到不同 GPU 上性能可能显著下降 | 在非 A100 上结果不稳定 | 统一使用 A100 80GB |\n\n### 低风险\n| 风险 | 影响 | 缓解措施 |\n|------|------|---------|\n| LoRA + 辅助头训练稳定性 | 训练不收敛 | 参考 QDepth-VLA 的 loss weight schedule |\n| RLDS 格式扩展 | 数据加载 bug | 单元测试 + 小 batch 验证 |\n| 评估时 center_crop 遗漏 | 性能异常低 | 文档已明确要求 `center_crop=True` |\n\n---\n\n## 7. 预估工作量\n\n| 阶段 | 任务 | 预估时间 | 前置依赖 |\n|------|------|---------|---------|\n| **Phase 1: 环境搭建** | 配置 OpenVLA-OFT 训练环境，安装依赖（含自定义 fork），跑通 inference | 2-3 天 | GPU 服务器就绪 |\n| **Phase 2: Baseline 复现** | 用预训练 checkpoint 在标准 LIBERO + SafeLIBERO 上评估，确认 baseline 数字 | 1-2 天 | Phase 1 |\n| **Phase 3: 数据 Pipeline** | 编写 MuJoCo wrapper 提取 occupancy GT；在 SafeLIBERO 场景中生成训练数据；转换为扩展 RLDS 格式 | 5-7 天 | Phase 1 |\n| **Phase 4: 模型修改** | 实现 OccupancyHead，修改 forward pass，添加多任务 loss，修改数据加载 | 3-5 天 | Phase 3 |\n| **Phase 5: 训练** | 在 A100 上训练 occupancy-augmented OpenVLA-OFT；调参 | 3-5 天 (含调参) | Phase 4 |\n| **Phase 6: 评估与消融** | SafeLIBERO 全评估 + 消融实验 + 结果分析 + 与 VLSA-AEGIS baseline 对比 | 3-4 天 | Phase 5 |\n| **总计** | — | **~3-4 周** | — |\n\n### 关键路径\n```\n环境搭建 (P1) → 数据 Pipeline (P3) → 模型修改 (P4) → 训练 (P5) → 评估 (P6)\n                  ↑ 最不确定环节\nBaseline 复现 (P2) 可与 P3 并行\n```\n\nPhase 3（数据生成）是最不确定的环节——MuJoCo/LIBERO 环境搭建和 occupancy 提取可能因版本兼容性问题耗时更久。\n\n---\n\n## 8. 核心结论\n\n1. **OpenVLA-OFT 原生支持 LIBERO**——有完整的 fine-tuning pipeline、预训练 checkpoint、评估脚本，适配成本低\n2. **SafeLIBERO 是 eval-only benchmark**——需要自行生成带 occupancy 标注的训练数据，这是最大工作量\n3. **辅助头最佳位置**：SigLIP+DINOv2 fused visual features 输出后（LLM projection 前），参考 QDepth-VLA 的设计\n4. **A100 80GB 单卡够用**（batch_size=8 训练 ~62GB），加 occupancy head 后用 BEV (2D) 可控制显存增量\n5. **学术新颖性明确**：目前无人将 occupancy prediction 作为 auxiliary head 集成到 VLA 中\n   - QDepth-VLA 验证了 auxiliary geometric supervision 可行（depth）\n   - VLSA-AEGIS 验证了 safety constraint + OpenVLA-OFT 可行（inference-only CBF）\n   - 本项目填补两者之间的 gap：learned occupancy-aware safety，端到端训练\n6. **License 无障碍**：OpenVLA-OFT (MIT)、SafeLIBERO (MIT)、VLSA-AEGIS (MIT) 均为开放许可\n"
  }
}
````

</details>

---

### Tool result

_source line 266 · 2026-05-20T04:19:56.375830+00:00_

File created successfully at: /home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/artifacts/openvla_oft_survey.md

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_openvla-oft-survey_20260520T040517",
  "tool": "Write",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 267 · 2026-05-20T04:19:56.376017+00:00_

报告已写入 `/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/artifacts/openvla_oft_survey.md`。

核心发现：

- **OpenVLA-OFT** (MIT, ~1200 stars, RSS 2025) 是 Stanford 出的 Optimized Fine-Tuning 方案，在 LIBERO 上 97.1% SOTA，推理速度 26× 提升
- **原生支持 LIBERO**：有完整的数据转换、训练脚本、预训练 checkpoint (HuggingFace)
- **A100 80GB 单卡可训练** (batch_size=8, ~62GB)，依赖自定义 transformers fork（bidirectional attention）
- **SafeLIBERO 是纯评估 benchmark**，不含训练数据和 occupancy 标注——数据生成是最大工程瓶颈
- **辅助头最佳位置**：SigLIP+DINOv2 fused features 输出后（16×16 空间分辨率），QDepth-VLA 已验证此位置加 geometric auxiliary head 可行
- **预估总工期 3-4 周**，关键路径在 occupancy GT 数据生成 (Phase 3)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_research_openvla-oft-survey_20260520T040517"
}
```

</details>

---
