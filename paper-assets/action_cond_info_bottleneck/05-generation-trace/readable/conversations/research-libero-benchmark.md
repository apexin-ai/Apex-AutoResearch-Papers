# research libero benchmark

**action cond info bottleneck** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 159
- **Recorded user turns:** 0
- **Tool calls:** 79
- **Original source:** `logs/chats/worker_research_libero-benchmark_20260515T111137.jsonl`
- **Structured JSON:** [`aa20c734443dabe77914.json`](../../sessions/aa/aa20c734443dabe77914.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

159 recorded events

### Tool call

_source line 1 · 2026-05-15T11:18:42.222781+00:00_

called Agent

<details open><summary>🔧 Tool call — Agent</summary>

```json
{
  "description": "Research LIBERO Benchmark",
  "subagent_type": "general-purpose",
  "prompt": "Research the LIBERO Benchmark for robot manipulation. I need detailed information about:\n\n1. GitHub repo URL\n2. Installation method (pip or from source)\n3. The 5 task suites: LIBERO-Spatial, LIBERO-Object, LIBERO-Goal, LIBERO-Long, LIBERO-90 — what each contains\n4. Data download method and size for each suite\n5. Data format: observation space dimensions/meaning, action space dimensions/meaning\n6. Evaluation scripts: how to run evaluation, what metrics are output\n\nUse WebSearch to find the LIBERO benchmark paper and GitHub repo. Then use WebFetch to read the GitHub README, installation docs, and key source files to get specific details about data format, task suites, and evaluation.\n\nBe thorough — I need exact commands, file paths, and API details. Report everything you find in a structured format."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_libero-benchmark_20260515T111137",
  "tool": "Agent",
  "tool_args": {
    "description": "Research LIBERO Benchmark",
    "subagent_type": "general-purpose",
    "prompt": "Research the LIBERO Benchmark for robot manipulation. I need detailed information about:\n\n1. GitHub repo URL\n2. Installation method (pip or from source)\n3. The 5 task suites: LIBERO-Spatial, LIBERO-Object, LIBERO-Goal, LIBERO-Long, LIBERO-90 — what each contains\n4. Data download method and size for each suite\n5. Data format: observation space dimensions/meaning, action space dimensions/meaning\n6. Evaluation scripts: how to run evaluation, what metrics are output\n\nUse WebSearch to find the LIBERO benchmark paper and GitHub repo. Then use WebFetch to read the GitHub README, installation docs, and key source files to get specific details about data format, task suites, and evaluation.\n\nBe thorough — I need exact commands, file paths, and API details. Report everything you find in a structured format."
  }
}
```

</details>

---

### Tool call

_source line 2 · 2026-05-15T11:18:42.223170+00:00_

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
  "session": "worker_research_libero-benchmark_20260515T111137",
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

_source line 3 · 2026-05-15T11:18:42.223349+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_libero-benchmark_20260515T111137",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 4 · 2026-05-15T11:18:42.223508+00:00_

called Agent

<details open><summary>🔧 Tool call — Agent</summary>

```json
{
  "description": "Research LIBERO-Plus perturbation",
  "subagent_type": "general-purpose",
  "prompt": "Research LIBERO-Plus, which is a perturbation-based evaluation extension for the LIBERO benchmark in robot manipulation.\n\nI need to find:\n1. What LIBERO-Plus is — what it adds on top of LIBERO\n2. GitHub repo or paper source\n3. The 4 perturbation dimensions: camera perturbation, lighting change, texture swap, sensor noise — exact definitions\n4. Installation and running instructions\n5. How it integrates with standard LIBERO evaluation\n\nAlso research whether LIBERO's simulation environment has built-in randomization options (camera jitter, color/lighting changes, background texture randomization). If it does, how to configure them. If not, whether LIBERO-Plus perturbation implementations can be reused as training-time data augmentation.\n\nUse WebSearch to find papers and repos related to \"LIBERO-Plus\" or \"LIBERO perturbation evaluation\" or \"LIBERO robustness\". Then use WebFetch to read relevant GitHub repos and paper details.\n\nReport everything in structured format with exact commands and code paths where possible."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_libero-benchmark_20260515T111137",
  "tool": "Agent",
  "tool_args": {
    "description": "Research LIBERO-Plus perturbation",
    "subagent_type": "general-purpose",
    "prompt": "Research LIBERO-Plus, which is a perturbation-based evaluation extension for the LIBERO benchmark in robot manipulation.\n\nI need to find:\n1. What LIBERO-Plus is — what it adds on top of LIBERO\n2. GitHub repo or paper source\n3. The 4 perturbation dimensions: camera perturbation, lighting change, texture swap, sensor noise — exact definitions\n4. Installation and running instructions\n5. How it integrates with standard LIBERO evaluation\n\nAlso research whether LIBERO's simulation environment has built-in randomization options (camera jitter, color/lighting changes, background texture randomization). If it does, how to configure them. If not, whether LIBERO-Plus perturbation implementations can be reused as training-time data augmentation.\n\nUse WebSearch to find papers and repos related to \"LIBERO-Plus\" or \"LIBERO perturbation evaluation\" or \"LIBERO robustness\". Then use WebFetch to read relevant GitHub repos and paper details.\n\nReport everything in structured format with exact commands and code paths where possible."
  }
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-15T11:18:42.223748+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "LIBERO benchmark robot manipulation GitHub repo"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_libero-benchmark_20260515T111137",
  "tool": "WebSearch",
  "tool_args": {
    "query": "LIBERO benchmark robot manipulation GitHub repo"
  }
}
```

</details>

---

### Tool call

_source line 6 · 2026-05-15T11:18:42.223883+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "LIBERO benchmark paper Lifelong Learning robot manipulation task suites"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_libero-benchmark_20260515T111137",
  "tool": "WebSearch",
  "tool_args": {
    "query": "LIBERO benchmark paper Lifelong Learning robot manipulation task suites"
  }
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-15T11:18:42.224009+00:00_

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
  "session": "worker_research_libero-benchmark_20260515T111137",
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

_source line 8 · 2026-05-15T11:18:42.224131+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_libero-benchmark_20260515T111137",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-15T11:18:42.224254+00:00_

called Agent

<details open><summary>🔧 Tool call — Agent</summary>

```json
{
  "description": "Research LeRobot LIBERO integration",
  "subagent_type": "general-purpose",
  "prompt": "Research the integration between LeRobot (HuggingFace's robot learning framework) and the LIBERO benchmark.\n\nI need to find:\n1. Does LeRobot natively support LIBERO datasets?\n2. If yes, what are the dataset names on HuggingFace Hub?\n3. What is the data conversion pipeline from LIBERO's native HDF5 format to LeRobot format?\n4. Any conversion scripts or utilities available\n\nUse WebSearch to search for:\n- \"LeRobot LIBERO\" \n- \"lerobot libero dataset\"\n- HuggingFace Hub LIBERO datasets\n- \"lerobot convert libero\"\n\nThen use WebFetch to check:\n- The LeRobot GitHub repo for LIBERO-related code\n- HuggingFace Hub for LIBERO datasets in LeRobot format\n- Any conversion scripts or documentation\n\nReport everything in structured format with exact dataset names, commands, and code paths."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_libero-benchmark_20260515T111137",
  "tool": "Agent",
  "tool_args": {
    "description": "Research LeRobot LIBERO integration",
    "subagent_type": "general-purpose",
    "prompt": "Research the integration between LeRobot (HuggingFace's robot learning framework) and the LIBERO benchmark.\n\nI need to find:\n1. Does LeRobot natively support LIBERO datasets?\n2. If yes, what are the dataset names on HuggingFace Hub?\n3. What is the data conversion pipeline from LIBERO's native HDF5 format to LeRobot format?\n4. Any conversion scripts or utilities available\n\nUse WebSearch to search for:\n- \"LeRobot LIBERO\" \n- \"lerobot libero dataset\"\n- HuggingFace Hub LIBERO datasets\n- \"lerobot convert libero\"\n\nThen use WebFetch to check:\n- The LeRobot GitHub repo for LIBERO-related code\n- HuggingFace Hub for LIBERO datasets in LeRobot format\n- Any conversion scripts or documentation\n\nReport everything in structured format with exact dataset names, commands, and code paths."
  }
}
```

</details>

---

### Tool call

_source line 10 · 2026-05-15T11:18:42.224436+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "LIBERO-Plus perturbation evaluation robot manipulation benchmark"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_libero-benchmark_20260515T111137",
  "tool": "WebSearch",
  "tool_args": {
    "query": "LIBERO-Plus perturbation evaluation robot manipulation benchmark"
  }
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-15T11:18:42.224611+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "LIBERO-Plus GitHub repo robustness perturbation"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_libero-benchmark_20260515T111137",
  "tool": "WebSearch",
  "tool_args": {
    "query": "LIBERO-Plus GitHub repo robustness perturbation"
  }
}
```

</details>

---

### Tool call

_source line 12 · 2026-05-15T11:18:42.224746+00:00_

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
  "session": "worker_research_libero-benchmark_20260515T111137",
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

_source line 13 · 2026-05-15T11:18:42.224864+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_libero-benchmark_20260515T111137",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 14 · 2026-05-15T11:18:42.224991+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "LIBERO benchmark robustness evaluation camera lighting texture noise perturbation"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_libero-benchmark_20260515T111137",
  "tool": "WebSearch",
  "tool_args": {
    "query": "LIBERO benchmark robustness evaluation camera lighting texture noise perturbation"
  }
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-15T11:18:42.225120+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "LIBERO simulation environment randomization domain randomization options"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_libero-benchmark_20260515T111137",
  "tool": "WebSearch",
  "tool_args": {
    "query": "LIBERO simulation environment randomization domain randomization options"
  }
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-15T11:18:42.225274+00:00_

Web search results for query: "LIBERO benchmark robot manipulation GitHub repo"

Links: [{"title":"GitHub - Lifelong-Robot-Learning/LIBERO: Benchmarking Knowledge Transfer in Lifelong Robot Learning · GitHub","url":"https://github.com/Lifelong-Robot-Learning/LIBERO"},{"title":"LIBERO – LIBERO","url":"https://libero-project.github.io/main.html"},{"title":"GitHub - huggingface/lerobot-libero: A fork of the official LIBERO benchmark, extended for Hugging Face’s LeRobot integration and large-scale robotics experiments.","url":"https://github.com/huggingface/lerobot-libero"},{"title":"LIBERO: Benchmarking Knowledge Transfer for Lifelong Robot Learning – Sony AI","url":"https://ai.sony/publications/LIBERO-Benchmarking-Knowledge-Transfer-for-Lifelong-Robot-Learning/"},{"title":"Research – LIBERO","url":"https://libero-project.github.io/research"},{"title":"LIBERO Benchmark: Lifelong Robot Learning","url":"https://www.emergentmind.com/topics/libero-benchmark"},{"title":"Documentation for Libero, a lifelong robot learning benchmark — libero 0.1.0 documentation","url":"https://lifelong-robot-learning.github.io/LIBERO/html/index.html"},{"title":"openvla/experiments/robot/libero/regenerate_libero_dataset.py at main · openvla/openvla","url":"https://github.com/openvla/openvla/blob/main/experiments/robot/libero/regenerate_libero_dataset.py"},{"title":"LIBERO | Proceedings of the 37th International Conference on Neural Information Processing Systems","url":"https://dl.acm.org/doi/abs/10.5555/3666122.3668061"},{"title":"GitHub - Zxy-MLlab/LIBERO-PRO: LIBERO-PRO is the official repository of the LIBERO-PRO — an evaluation extension of the original LIBERO benchmark","url":"https://github.com/Zxy-MLlab/LIBERO-PRO"}]

Based on the search results, here's what I found about the LIBERO benchmark robot manipulation GitHub repository:

## Official LIBERO Repository

The main LIBERO GitHub repository is located at Lifelong-Robot-Learning/LIBERO, titled "Benchmarking Knowledge Transfer in Lif
…[truncated 1040 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_libero-benchmark_20260515T111137",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-15T11:18:42.225441+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "LeRobot LIBERO dataset integration HuggingFace"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_libero-benchmark_20260515T111137",
  "tool": "WebSearch",
  "tool_args": {
    "query": "LeRobot LIBERO dataset integration HuggingFace"
  }
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-15T11:18:42.225603+00:00_

Web search results for query: "LIBERO benchmark paper Lifelong Learning robot manipulation task suites"

Links: [{"title":"GitHub - Lifelong-Robot-Learning/LIBERO: Benchmarking Knowledge Transfer in Lifelong Robot Learning · GitHub","url":"https://github.com/Lifelong-Robot-Learning/LIBERO"},{"title":"LIBERO: Benchmarking Knowledge Transfer for Lifelong Robot Learning","url":"https://papers.neurips.cc/paper_files/paper/2023/file/8c3c666820ea055a77726d66fc7d447f-Paper-Datasets_and_Benchmarks.pdf"},{"title":"LIBERO: Benchmarking Knowledge Transfer for Lifelong Robot Learning | OpenReview","url":"https://openreview.net/forum?id=xzEtNSuDJk"},{"title":"[2306.03310] LIBERO: Benchmarking Knowledge Transfer for Lifelong Robot Learning","url":"https://arxiv.org/abs/2306.03310"},{"title":"LIBERO: simulation benchmark for the study of lifelong robot learning | by Deepthi Karkada | Medium","url":"https://medium.com/@deepkarkada/libero-simulation-benchmark-for-the-study-of-lifelong-robot-learning-583b786a96f6"},{"title":"LIBERO Benchmark: Lifelong Robot Learning","url":"https://www.emergentmind.com/topics/libero-benchmark"},{"title":"benchmarking knowledge transfer for lifelong robot learning","url":"https://dl.acm.org/doi/abs/10.5555/3666122.3668061"},{"title":"LIBERO · Hugging Face","url":"https://huggingface.co/docs/lerobot/libero"},{"title":"LIBERO: Benchmarking Knowledge Transfer for Lifelong Robot Learning – Sony AI","url":"https://ai.sony/publications/LIBERO-Benchmarking-Knowledge-Transfer-for-Lifelong-Robot-Learning/"},{"title":"LIBERO-Object: Lifelong Learning in Robotic Manipulation","url":"https://www.emergentmind.com/topics/libero-object"}]

Based on the search results, here's comprehensive information about the LIBERO benchmark paper and lifelong learning robot manipulation task suites:

## Overview

LIBERO is a novel benchmark of lifelong learning for robot manipulation. It is designed to study lifelong robot learning — the idea that robots need to keep learning and
…[truncated 1556 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_libero-benchmark_20260515T111137",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-15T11:18:42.225754+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "lerobot convert libero HDF5 dataset script"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_libero-benchmark_20260515T111137",
  "tool": "WebSearch",
  "tool_args": {
    "query": "lerobot convert libero HDF5 dataset script"
  }
}
```

</details>

---

### Tool call

_source line 20 · 2026-05-15T11:18:42.225881+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "huggingface hub lerobot libero dataset names"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_libero-benchmark_20260515T111137",
  "tool": "WebSearch",
  "tool_args": {
    "query": "huggingface hub lerobot libero dataset names"
  }
}
```

</details>

---

### Tool call

_source line 21 · 2026-05-15T11:18:42.226008+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "github huggingface lerobot libero conversion pipeline 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_libero-benchmark_20260515T111137",
  "tool": "WebSearch",
  "tool_args": {
    "query": "github huggingface lerobot libero conversion pipeline 2025 2026"
  }
}
```

</details>

---

### Tool result

_source line 22 · 2026-05-15T11:18:42.226144+00:00_

Web search results for query: "LIBERO-Plus perturbation evaluation robot manipulation benchmark"

Links: [{"title":"LIBERO Benchmark: Vision-Language-Action in Robotics","url":"https://www.emergentmind.com/topics/libero"},{"title":"GitHub - sylvestf/LIBERO-plus: Official repository of LIBERO-plus, a generalized benchmark for in-depth robustness analysis of vision-language-action models. · GitHub","url":"https://github.com/sylvestf/LIBERO-plus"},{"title":"LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-Action Models","url":"https://arxiv.org/html/2510.13626v1"},{"title":"LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-Action Models","url":"https://sylvestf.github.io/LIBERO-plus/"},{"title":"GitHub - Lifelong-Robot-Learning/LIBERO: Benchmarking Knowledge Transfer in Lifelong Robot Learning · GitHub","url":"https://github.com/Lifelong-Robot-Learning/LIBERO"},{"title":"[2510.13626] LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-Action Models","url":"https://arxiv.org/abs/2510.13626"},{"title":"OpenMOSS LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-","url":"https://arxiv.org/pdf/2510.13626"},{"title":"LIBERO-PRO: Towards Robust and Fair Evaluation of ...","url":"https://arxiv.org/pdf/2510.03827"},{"title":"Paper page - LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-Action Models","url":"https://huggingface.co/papers/2510.13626"},{"title":"[2510.13626v1] LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-Action Models","url":"https://arxiv.org/abs/2510.13626v1"}]

Based on the search results, here's comprehensive information about LIBERO-Plus:

## Overview

LIBERO-plus is a generalized benchmark for in-depth robustness analysis of vision-language-action models. LIBERO-Plus is an extensive benchmark with 10,030 tasks spanning seven perturbation dimensions, and includes a diverse training dataset with over 20,000 successful trajectories collected under systematically varied conditions.

## Key Pe
…[truncated 1458 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_libero-benchmark_20260515T111137",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 23 · 2026-05-15T11:18:42.226302+00:00_

Web search results for query: "LIBERO-Plus GitHub repo robustness perturbation"

Links: [{"title":"GitHub - sylvestf/LIBERO-plus: Official repository of LIBERO-plus, a generalized benchmark for in-depth robustness analysis of vision-language-action models. · GitHub","url":"https://github.com/sylvestf/LIBERO-plus"},{"title":"LIBERO-plus/README.md at main · sylvestf/LIBERO-plus","url":"https://github.com/sylvestf/LIBERO-plus/blob/main/README.md"},{"title":"LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-Action Models","url":"https://sylvestf.github.io/LIBERO-plus/"},{"title":"LIBERO-plus · Hugging Face","url":"https://huggingface.co/docs/lerobot/main/libero_plus"},{"title":"LIBERO-plus/index.html at main · sylvestf/LIBERO-plus","url":"https://github.com/sylvestf/LIBERO-plus/blob/main/index.html"},{"title":"Sylvest/LIBERO-plus · Datasets at Hugging Face","url":"https://huggingface.co/datasets/Sylvest/LIBERO-plus"},{"title":"GitHub - Zxy-MLlab/LIBERO-PRO: LIBERO-PRO is the official repository of the LIBERO-PRO — an evaluation extension of the original LIBERO benchmark","url":"https://github.com/Zxy-MLlab/LIBERO-PRO"},{"title":"LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-Action Models","url":"https://arxiv.org/html/2510.13626v1"},{"title":"Paper page - LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-Action Models","url":"https://huggingface.co/papers/2510.13626"},{"title":"[2510.13626] LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-Action Models","url":"https://arxiv.org/abs/2510.13626"}]

Based on the search results, here's information about the LIBERO-Plus GitHub repository and its robustness perturbation approach:

## Overview

LIBERO-Plus contains the official implementation and benchmark for a paper on "In-depth Robustness Analysis for Vision-Language-Action Models". LIBERO-Plus is a robustness benchmark for Vision-Language-Action (VLA) models built on top of LIBERO that systematically stress-tests policies by
…[truncated 1222 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_libero-benchmark_20260515T111137",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 24 · 2026-05-15T11:18:42.226462+00:00_

Web search results for query: "LIBERO benchmark robustness evaluation camera lighting texture noise perturbation"

Links: [{"title":"Paper page - LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-Action Models","url":"https://huggingface.co/papers/2510.13626"},{"title":"[2510.13626] LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-Action Models","url":"https://arxiv.org/abs/2510.13626"},{"title":"LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-Action Models","url":"https://arxiv.org/html/2510.13626v1"},{"title":"LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-Action Models","url":"https://sylvestf.github.io/LIBERO-plus/"},{"title":"LIBERO Benchmark: Vision-Language-Action in Robotics","url":"https://www.emergentmind.com/topics/libero"},{"title":"GitHub - sylvestf/LIBERO-plus: Official repository of LIBERO-plus, a generalized benchmark for in-depth robustness analysis of vision-language-action models. · GitHub","url":"https://github.com/sylvestf/LIBERO-plus"},{"title":"Efficient Spatial Adaptation in VLA Models","url":"https://www.emergentmind.com/papers/2512.02902"},{"title":"CVPR Poster LIBERO-Plus: A Progressive Robustness Benchmark for Visual-Language-Action Models","url":"https://cvpr.thecvf.com/virtual/2026/poster/38735"},{"title":"[2510.13626v1] LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-Action Models","url":"https://arxiv.org/abs/2510.13626v1"},{"title":"LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-Action Models | Takara TLDR","url":"https://tldr.takara.ai/p/2510.13626"}]

I found comprehensive information about the LIBERO benchmark and its robustness evaluation capabilities. Here's what the search revealed:

## LIBERO-Plus: Robustness Evaluation Framework

LIBERO-Plus is an in-depth robustness analysis framework for Visual-Language-Action (VLA) models that performs systematic vulnerability analysis by introducing controlled perturbations across seven dimensions: objects layout
…[truncated 1390 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_libero-benchmark_20260515T111137",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 25 · 2026-05-15T11:18:42.226698+00:00_

Web search results for query: "LIBERO simulation environment randomization domain randomization options"

Links: [{"title":"Domain Randomization for Sim2Real Transfer | Lil'Log","url":"https://lilianweng.github.io/posts/2019-05-05-domain-randomization/"},{"title":"Continual Domain Randomization","url":"https://arxiv.org/pdf/2403.12193"},{"title":"LIBERO-PRO: Towards Robust and Fair Evaluation of Vision-Language-Action Models Beyond Memorization","url":"https://arxiv.org/html/2510.03827v1"},{"title":"Flow-based Domain Randomization for Learning and Sequencing Robotic Skills","url":"https://arxiv.org/html/2502.01800v1"},{"title":"9.4. Domain Randomization for RL — Omniverse IsaacSim latest documentation","url":"https://docs.isaacsim.omniverse.nvidia.com/2023.1.1/isaac_gym_tutorials/tutorial_gym_domain_randomization.html"},{"title":"A Domain Data Pattern Randomization based Deep Reinforcement Learning method for Sim-to-Real transfer","url":"https://dl.acm.org/doi/fullHtml/10.1145/3461353.3461373"},{"title":"Cyclic policy distillation: Sample-efficient sim-to-real reinforcement learning with domain randomization - ScienceDirect","url":"https://www.sciencedirect.com/science/article/abs/pii/S0921889023000647"},{"title":"Flow-based Domain Randomization for Learning and Sequencing Robotic Skills | OpenReview","url":"https://openreview.net/forum?id=9JQXuyzdGL"},{"title":"2. Domain Randomization for RL — Omniverse IsaacSim latest documentation","url":"https://docs.omniverse.nvidia.com/app_isaacsim/app_isaacsim/tutorial_gym_domain_randomization.html"},{"title":"Domain Randomization","url":"https://stevengong.co/notes/Domain-Randomization"}]

Based on the search results, I found relevant information about LIBERO and domain randomization options. Here's what I discovered:

## LIBERO and Domain Randomization

LIBERO-PRO is a plug-and-play benchmark that incorporates carefully designed perturbations across four dimensions—manipulated objects, initial states, task instructions, and
…[truncated 1382 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_libero-benchmark_20260515T111137",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 26 · 2026-05-15T11:18:42.226877+00:00_

Web search results for query: "LeRobot LIBERO dataset integration HuggingFace"

Links: [{"title":"GitHub - huggingface/lerobot-libero: A fork of the official LIBERO benchmark, extended for Hugging Face’s LeRobot integration and large-scale robotics experiments.","url":"https://github.com/huggingface/lerobot-libero"},{"title":"GitHub - huggingface/lerobot: 🤗 LeRobot: Making AI for Robotics more accessible with end-to-end learning","url":"https://github.com/huggingface/lerobot"},{"title":"LIBERO","url":"https://huggingface.co/docs/lerobot/en/libero"},{"title":"lerobot/libero · Datasets at Hugging Face","url":"https://huggingface.co/datasets/lerobot/libero"},{"title":"lerobot/libero_object_image · Datasets at Hugging Face","url":"https://huggingface.co/datasets/lerobot/libero_object_image"},{"title":"lerobot/xvla-libero · Hugging Face","url":"https://huggingface.co/lerobot/xvla-libero"},{"title":"LeRobotDataset v3.0 · Hugging Face","url":"https://huggingface.co/docs/lerobot/en/lerobot-dataset-v3"},{"title":"HuggingFaceVLA/libero · Datasets at Hugging Face","url":"https://huggingface.co/datasets/HuggingFaceVLA/libero"},{"title":"LIBERO-plus · Hugging Face","url":"https://huggingface.co/docs/lerobot/main/libero_plus"},{"title":"LeRobot v0.4.0: Supercharging OSS Robot Learning","url":"https://huggingface.co/blog/lerobot-release-v040"}]

Based on the search results, here's what I found about LeRobot LIBERO dataset integration with HuggingFace:

## Overview

The LIBERO benchmark repository is now maintained by the Hugging Face team, with modifications for compatibility with LeRobot, simplified installation, and large-scale robotics experiments.

## Dataset Integration

LeRobot supports standard benchmarks like LIBERO and more, and LeRobot now officially supports LIBERO, one of the largest open benchmarks for Vision-Language-Action (VLA) policies, boasting over 130 tasks.

## Available Datasets

A preprocessed LIBERO dataset is provided that is fully compatible with the curr
…[truncated 608 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_libero-benchmark_20260515T111137",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool call

_source line 27 · 2026-05-15T11:18:42.227044+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://github.com/Lifelong-Robot-Learning/LIBERO",
  "prompt": "Extract ALL technical details from this README: 1) Installation instructions (exact commands), 2) Task suite descriptions (LIBERO-Spatial, LIBERO-Object, LIBERO-Goal, LIBERO-Long, LIBERO-90), 3) Data download commands and URLs, 4) Data format details (observation space, action space, dimensions), 5) Evaluation commands, 6) Any code structure information. Be extremely thorough - capture every command, URL, and technical detail."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_libero-benchmark_20260515T111137",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://github.com/Lifelong-Robot-Learning/LIBERO",
    "prompt": "Extract ALL technical details from this README: 1) Installation instructions (exact commands), 2) Task suite descriptions (LIBERO-Spatial, LIBERO-Object, LIBERO-Goal, LIBERO-Long, LIBERO-90), 3) Data download commands and URLs, 4) Data format details (observation space, action space, dimensions), 5) Evaluation commands, 6) Any code structure information. Be extremely thorough - capture every command, URL, and technical detail."
  }
}
```

</details>

---

### Tool result

_source line 28 · 2026-05-15T11:18:42.227228+00:00_

Web search results for query: "huggingface hub lerobot libero dataset names"

Links: [{"title":"GitHub - huggingface/lerobot: 🤗 LeRobot: Making AI for Robotics more accessible with end-to-end learning","url":"https://github.com/huggingface/lerobot"},{"title":"GitHub - huggingface/lerobot-libero: A fork of the official LIBERO benchmark, extended for Hugging Face’s LeRobot integration and large-scale robotics experiments.","url":"https://github.com/huggingface/lerobot-libero"},{"title":"LIBERO","url":"https://huggingface.co/docs/lerobot/en/libero"},{"title":"lerobot/libero · Datasets at Hugging Face","url":"https://huggingface.co/datasets/lerobot/libero"},{"title":"lerobot/libero_object_image · Datasets at Hugging Face","url":"https://huggingface.co/datasets/lerobot/libero_object_image"},{"title":"HuggingFaceVLA/libero · Datasets at Hugging Face","url":"https://huggingface.co/datasets/HuggingFaceVLA/libero"},{"title":"LeRobotDataset v3.0 · Hugging Face","url":"https://huggingface.co/docs/lerobot/en/lerobot-dataset-v3"},{"title":"https://raw.githubusercontent.com/Physical-Intelli...","url":"https://raw.githubusercontent.com/Physical-Intelligence/openpi/main/examples/libero/convert_libero_data_to_lerobot.py"},{"title":"lerobot/libero_10_image · Datasets at Hugging Face","url":"https://huggingface.co/datasets/lerobot/libero_10_image"},{"title":"lerobot/xvla-libero · Hugging Face","url":"https://huggingface.co/lerobot/xvla-libero"}]

Based on the web search results, here are the LIBERO dataset names available on the Hugging Face Hub for LeRobot:

## LIBERO Task Suites

LIBERO provides 130 tasks grouped into four task suites: LIBERO-Spatial, LIBERO-Object, LIBERO-Goal, and LIBERO-100.

## Raw Dataset Names

The raw dataset names include "libero_10_no_noops", "libero_goal_no_noops", "libero_object_no_noops", and "libero_spatial_no_noops".

## LeRobot Processed Datasets

Several preprocessed datasets are available on the Hugging Face Hub:

1. "HuggingFaceVLA/libero" - a prep
…[truncated 480 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_libero-benchmark_20260515T111137",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 29 · 2026-05-15T11:18:42.227401+00:00_

Web search results for query: "lerobot convert libero HDF5 dataset script"

Links: [{"title":"openpi/examples/libero/convert_libero_data_to_lerobot.py at main · Physical-Intelligence/openpi","url":"https://github.com/Physical-Intelligence/openpi/blob/main/examples/libero/convert_libero_data_to_lerobot.py"},{"title":"IPEC-COMMUNITY/libero_90_no_noops_lerobot · Dataset converted ideas","url":"https://huggingface.co/datasets/IPEC-COMMUNITY/libero_90_no_noops_lerobot/discussions/2"},{"title":"GitHub - anarnuri/hdf5_to_lerobot_converter · GitHub","url":"https://github.com/anarnuri/hdf5_to_lerobot_converter"},{"title":"GitHub - muhamuttaqien/ALOHADataConverter: This repository contains scripts for converting an ALOHA HDF5 dataset into the Lerobot, RMB and GR00T formats.","url":"https://github.com/muhamuttaqien/ALOHADataConverter"},{"title":"https://raw.githubusercontent.com/Physical-Intelli...","url":"https://raw.githubusercontent.com/Physical-Intelligence/openpi/main/examples/libero/convert_libero_data_to_lerobot.py"},{"title":"Policy Post-training — isaaclab_arena 0.2","url":"https://isaac-sim.github.io/IsaacLab-Arena/main/pages/example_workflows/static_manipulation/step_4_policy_training.html"},{"title":"Question: Is There an Official or Recommended Way to Convert Isaac Lab HDF5 Data to LeRobot Schema? · Issue #2739 · isaac-sim/IsaacLab","url":"https://github.com/isaac-sim/IsaacLab/issues/2739"},{"title":"How to convert my own dataset to LerobotDataset format? · Issue #846 · huggingface/lerobot","url":"https://github.com/huggingface/lerobot/issues/846"},{"title":"[Question] HDF5 to LeRobot convert pipeline in new release · Issue #2941 · isaac-sim/IsaacLab","url":"https://github.com/isaac-sim/IsaacLab/issues/2941"},{"title":"openvla/experiments/robot/libero/regenerate_libero_dataset.py at main · openvla/openvla","url":"https://github.com/openvla/openvla/blob/main/experiments/robot/libero/regenerate_libero_dataset.py"}]

Based on the search results, I found several relev
…[truncated 1160 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_libero-benchmark_20260515T111137",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool call

_source line 30 · 2026-05-15T11:18:42.227589+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://lifelong-robot-learning.github.io/LIBERO/html/index.html",
  "prompt": "Extract ALL technical documentation details: installation, API, data format, observation space, action space, evaluation methods, task suite descriptions, data download instructions, and any code examples. Be extremely thorough."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_libero-benchmark_20260515T111137",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://lifelong-robot-learning.github.io/LIBERO/html/index.html",
    "prompt": "Extract ALL technical documentation details: installation, API, data format, observation space, action space, evaluation methods, task suite descriptions, data download instructions, and any code examples. Be extremely thorough."
  }
}
```

</details>

---

### Tool call

_source line 31 · 2026-05-15T11:18:42.227734+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://github.com/sylvestf/LIBERO-plus/blob/main/README.md",
  "prompt": "Extract the full README content including: installation instructions, perturbation dimensions with exact definitions, how to run evaluation, project structure, configuration options, and any code examples. Include all technical details."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_libero-benchmark_20260515T111137",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://github.com/sylvestf/LIBERO-plus/blob/main/README.md",
    "prompt": "Extract the full README content including: installation instructions, perturbation dimensions with exact definitions, how to run evaluation, project structure, configuration options, and any code examples. Include all technical details."
  }
}
```

</details>

---

### Tool call

_source line 32 · 2026-05-15T11:18:42.227867+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://arxiv.org/abs/2306.03310",
  "prompt": "Extract details about: 1) The 5 task suites (LIBERO-Spatial, LIBERO-Object, LIBERO-Goal, LIBERO-Long, LIBERO-90), their exact contents, number of tasks, 2) Observation space dimensions and meaning, 3) Action space dimensions and meaning, 4) Data format and demonstration details, 5) Evaluation protocol and metrics. Be extremely detailed."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_libero-benchmark_20260515T111137",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://arxiv.org/abs/2306.03310",
    "prompt": "Extract details about: 1) The 5 task suites (LIBERO-Spatial, LIBERO-Object, LIBERO-Goal, LIBERO-Long, LIBERO-90), their exact contents, number of tasks, 2) Observation space dimensions and meaning, 3) Action space dimensions and meaning, 4) Data format and demonstration details, 5) Evaluation protocol and metrics. Be extremely detailed."
  }
}
```

</details>

---

### Tool result

_source line 33 · 2026-05-15T11:18:42.228006+00:00_

Web search results for query: "github huggingface lerobot libero conversion pipeline 2025 2026"

Links: [{"title":"GitHub - huggingface/lerobot-libero: A fork of the official LIBERO benchmark, extended for Hugging Face’s LeRobot integration and large-scale robotics experiments.","url":"https://github.com/huggingface/lerobot-libero"},{"title":"GitHub - huggingface/lerobot: 🤗 LeRobot: Making AI for Robotics more accessible with end-to-end learning","url":"https://github.com/huggingface/lerobot"},{"title":"LIBERO · Hugging Face","url":"https://huggingface.co/docs/lerobot/libero"},{"title":"GitHub - OpenDriveLab/AgiBot-World: [IROS 2025 Best Paper Award Finalist & IEEE TRO 2026] The Large-scale Manipulation Platform for Scalable and Intelligent Embodied Systems · GitHub","url":"https://github.com/OpenDriveLab/AgiBot-World"},{"title":"lerobot/xvla-libero · Hugging Face","url":"https://huggingface.co/lerobot/xvla-libero"},{"title":"Releases · huggingface/lerobot","url":"https://github.com/huggingface/lerobot/releases"},{"title":"GitHub - starVLA/starVLA: StarVLA: A Lego-like Codebase for Vision-Language-Action Model Developing · GitHub","url":"https://github.com/starVLA/starVLA"},{"title":"lerobot/docs/source/pi05.mdx at main · huggingface/lerobot","url":"https://github.com/huggingface/lerobot/blob/main/docs/source/pi05.mdx"},{"title":"LIBERO","url":"https://huggingface.co/docs/lerobot/main/en/libero"},{"title":"LeRobot · Hugging Face","url":"https://huggingface.co/docs/lerobot/index"}]

Based on the search results, here's what I found about the LeRobot LIBERO conversion pipeline:

## Overview

LIBERO provides a procedural generation pipeline that could in principle generate an infinite number of manipulation tasks, with 130 tasks grouped into four task suites: LIBERO-Spatial, LIBERO-Object, LIBERO-Goal, and LIBERO-100.

## LeRobot Integration

LeRobot ported LIBERO into its framework and used it mainly to evaluate SmolVLA, its lightweight Vision-Language-Action model. Le
…[truncated 893 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_libero-benchmark_20260515T111137",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 34 · 2026-05-15T11:18:42.228156+00:00_

# LIBERO Documentation Summary

Based on the provided webpage content, this is a **documentation index** rather than a technical reference page containing the requested details.

## Available Documentation Structure

The page outlines the following sections:

**Getting Started:**
- Installation procedures
- Code structure overview
- General orientation

**Technical Components:**
- Lifelong learning algorithms documentation
- Policy architecture specifications
- Dataset information

**Research Topics:**
- Knowledge transfer approaches (disentangled/entangled)
- Algorithmic design variations
- Architectural design options
- Task ordering strategies
- Pretraining methodology

**Generation Capabilities:**
- Scene creation procedures
- Task generation methods

**Practical Guides:**
- Experiment configuration instructions
- Custom algorithm/policy implementation
- Custom dataset creation

## Limitation

The extracted content provides **only navigation and section headings**, not the actual technical specifications. Details regarding API endpoints, observation/action spaces, evaluation metrics, task descriptions, download instructions, and code examples are referenced but not included in this excerpt.

To access the requested technical documentation (installation steps, API details, data formats, evaluation methods, and examples), you would need to navigate to the individual linked pages within the documentation.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_libero-benchmark_20260515T111137",
  "tool": "WebFetch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 35 · 2026-05-15T11:18:42.228303+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://arxiv.org/html/2510.13626v1",
  "prompt": "Extract detailed information about: 1) All 7 perturbation dimensions and their exact definitions/sub-dimensions, 2) How perturbations are implemented in the simulation (MuJoCo/robosuite), 3) Difficulty levels L1-L5, 4) Training data augmentation details, 5) Integration with LIBERO's simulation environment, 6) Any details about camera, lighting, texture, sensor noise implementations specifically. Include technical specifics like parameter ranges."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_libero-benchmark_20260515T111137",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://arxiv.org/html/2510.13626v1",
    "prompt": "Extract detailed information about: 1) All 7 perturbation dimensions and their exact definitions/sub-dimensions, 2) How perturbations are implemented in the simulation (MuJoCo/robosuite), 3) Difficulty levels L1-L5, 4) Training data augmentation details, 5) Integration with LIBERO's simulation environment, 6) Any details about camera, lighting, texture, sensor noise implementations specifically. Include technical specifics like parameter ranges."
  }
}
```

</details>

---

### Tool call

_source line 36 · 2026-05-15T11:18:42.228446+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://sylvestf.github.io/LIBERO-plus/",
  "prompt": "Extract all technical details about LIBERO-Plus: perturbation dimensions, implementation details, benchmark construction, evaluation protocol, and any information about how perturbations are applied in the simulation."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_libero-benchmark_20260515T111137",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://sylvestf.github.io/LIBERO-plus/",
    "prompt": "Extract all technical details about LIBERO-Plus: perturbation dimensions, implementation details, benchmark construction, evaluation protocol, and any information about how perturbations are applied in the simulation."
  }
}
```

</details>

---

### Tool call

_source line 37 · 2026-05-15T11:18:42.228599+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://huggingface.co/docs/lerobot/en/libero",
  "prompt": "Extract ALL information about LIBERO integration: dataset names, conversion commands, training commands, evaluation commands, task suite names, dataset structure, any code examples. Be exhaustive."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_libero-benchmark_20260515T111137",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://huggingface.co/docs/lerobot/en/libero",
    "prompt": "Extract ALL information about LIBERO integration: dataset names, conversion commands, training commands, evaluation commands, task suite names, dataset structure, any code examples. Be exhaustive."
  }
}
```

</details>

---

### Tool result

_source line 38 · 2026-05-15T11:18:42.228723+00:00_

# LIBERO Benchmark Details - Limited Information Available

Based on the provided arXiv page content, I can only extract minimal technical specifications:

## Available Information

**Task Suites:** The abstract mentions "four task suites (130 tasks in total)" but does not enumerate the specific suite names or their individual task counts. The suite names you listed (LIBERO-Spatial, LIBERO-Object, etc.) do not appear in this page content.

**Demonstration Data:** The paper notes it provides "high-quality human-teleoperated demonstration data for all tasks" to support sample-efficient learning, but specific formatting details are absent.

**Key Findings:** The research reveals that "sequential finetuning outperforms existing lifelong learning methods in forward transfer" and that "no single visual encoder architecture excels at all types of knowledge transfer."

## Missing Technical Details

The arXiv abstract page does not contain:
- Observation space dimensionality or specifications
- Action space dimensionality or specifications  
- Data format specifications
- Evaluation metrics and protocols
- Individual task suite compositions

## Recommendation

To obtain the detailed technical specifications you're seeking, you would need to access the full PDF paper (available via the provided link) or visit the project website referenced as "this https URL" in the abstract.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_libero-benchmark_20260515T111137",
  "tool": "WebFetch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 39 · 2026-05-15T11:18:42.228870+00:00_

# LIBERO Technical Details Extraction

## Installation Instructions

The exact commands provided are:

```bash
conda create -n libero python=3.8.13
conda activate libero
git clone https://github.com/Lifelong-Robot-Learning/LIBERO.git
cd LIBERO
pip install -r requirements.txt
pip install torch==1.11.0+cu113 torchvision==0.12.0+cu113 torchaudio==0.11.0 --extra-index-url https://download.pytorch.org/whl/cu113
pip install -e .
```

## Task Suite Descriptions

The README identifies four task suites with specific characteristics:

- **LIBERO-Spatial**: Requires transfer of spatial relationship knowledge with controlled distribution shifts
- **LIBERO-Object**: Focuses on object knowledge transfer with controlled shifts
- **LIBERO-Goal**: Goal-oriented knowledge transfer with controlled shifts
- **LIBERO-100**: Contains "100 manipulation tasks requiring entangled knowledge transfer"
- **LIBERO-90/LIBERO-10**: The 100-task suite split—first portion for pretraining, latter for downstream testing

## Data Download Commands and URLs

Standard download:
```bash
python benchmark_scripts/download_libero_datasets.py
```

Specific dataset selection:
```bash
python benchmark_scripts/download_libero_datasets.py --datasets DATASET
```
where DATASET ∈ `[libero_spatial, libero_object, libero_100, libero_goal]`

HuggingFace alternative:
```bash
python benchmark_scripts/download_libero_datasets.py --use-huggingface
```

**Data URL**: https://huggingface.co/datasets/yifengzhu-hf/LIBERO-datasets

**Default storage location**: LIBERO folder (root directory)

## Data Format Details

The README does not explicitly specify observation space dimensions, action space details, or data format structures. However, it references:

- "camera_heights": 128
- "camera_widths": 128
- Action format: "dummy_action = [0.] * 7" (suggesting 7-dimensional action space)
- Reward function: Sparse ("+1 when task finished")

## Training/Evaluation Commands

Training command structure:
```bash
export CUDA_VISIBLE_DEV
…[truncated 835 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_libero-benchmark_20260515T111137",
  "tool": "WebFetch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 40 · 2026-05-15T11:18:42.229030+00:00_

# LIBERO

LIBERO is a benchmark designed to study **lifelong robot learning** — the idea that robots need to keep learning and adapting with their users over time, not just be pretrained once. It provides a set of standardized manipulation tasks that focus on **knowledge transfer**: how well a robot can apply what it has already learned to new situations. By evaluating on LIBERO, different algorithms can be compared fairly and researchers can build on each other's work.

- Paper: [Benchmarking Knowledge Transfer for Lifelong Robot Learning](https://arxiv.org/abs/2306.03310)
- GitHub: [Lifelong-Robot-Learning/LIBERO](https://github.com/Lifelong-Robot-Learning/LIBERO)
- Project website: [libero-project.github.io](https://libero-project.github.io)

![An overview of the LIBERO benchmark](https://libero-project.github.io/assets/img/libero/fig1.png)

## Available tasks

LIBERO includes **five task suites** covering **130 tasks**, ranging from simple object manipulations to complex multi-step scenarios:

| Suite          | CLI name         | Tasks | Description                                        |
| -------------- | ---------------- | ----- | -------------------------------------------------- |
| LIBERO-Spatial | `libero_spatial` | 10    | Tasks requiring reasoning about spatial relations  |
| LIBERO-Object  | `libero_object`  | 10    | Tasks centered on manipulating different objects   |
| LIBERO-Goal    | `libero_goal`    | 10    | Goal-conditioned tasks with changing targets       |
| LIBERO-90      | `libero_90`      | 90    | Short-horizon tasks from the LIBERO-100 collection |
| LIBERO-Long    | `libero_10`      | 10    | Long-horizon tasks from the LIBERO-100 collection  |

## Installation

After following the LeRobot installation instructions:

```bash
pip install -e ".[libero]"
```

LIBERO requires Linux (`sys_platform == 'linux'`). LeRobot uses MuJoCo for simulation — set the rendering backend before training or evaluation:

```bash
export MUJOCO_GL=egl  # fo
…[truncated 4883 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_libero-benchmark_20260515T111137",
  "tool": "WebFetch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 41 · 2026-05-15T11:18:42.229184+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://huggingface.co/datasets/lerobot/libero",
  "prompt": "Extract the full dataset card: dataset name, size, number of episodes, number of tasks, data format, column names, how to load it, any usage examples. Include all metadata."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_libero-benchmark_20260515T111137",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://huggingface.co/datasets/lerobot/libero",
    "prompt": "Extract the full dataset card: dataset name, size, number of episodes, number of tasks, data format, column names, how to load it, any usage examples. Include all metadata."
  }
}
```

</details>

---

### Tool result

_source line 42 · 2026-05-15T11:18:42.229322+00:00_

# LIBERO-Plus: Robustness Analysis Framework

## Overview

LIBERO-Plus is a comprehensive benchmark evaluating vision-language-action (VLA) models across multiple perturbation dimensions. The project functions as a drop-in replacement for the original LIBERO package, maintaining backward compatibility while adding extensive robustness testing capabilities.

## Installation

The setup process mirrors the original LIBERO system. Users should:

1. Clone the repository and navigate to the directory
2. Uninstall any existing LIBERO installation
3. Verify configuration paths at `/root/.libero/config.yaml`
4. Install via `pip install -e .`
5. Add system dependencies (libexpat1, libfontconfig1-dev, libmagickwand-dev)
6. Install additional Python packages from extra_requirements.txt

Assets must be downloaded from Hugging Face and extracted to `LIBERO-plus/libero/libero/assets/`, creating subdirectories for articulated objects, new objects, scenes, textures, and supporting files.

## Seven Perturbation Dimensions

The benchmark evaluates resilience across:

1. **Objects Layout** – "Confounding objects and target object displacement"
2. **Camera Viewpoints** – Position, orientation, and field-of-view modifications
3. **Robot Initial States** – Manipulator pose variations
4. **Language Instructions** – LLM-based instruction rewrites
5. **Light Conditions** – Intensity, direction, color, and shadow changes
6. **Background Textures** – Scene and surface appearance modifications
7. **Sensor Noise** – "Photometric distortions and image degradation"

## Evaluation Protocol

The evaluation methodology closely follows original LIBERO standards with one critical adjustment: modify `num_trials_per_task` from 50 to 1 in configuration files. Task classification mappings between IDs, perturbation categories, and difficulty levels are located in `.libero/libero/benchmark/task_classification.json`.

## Project Structure

The extracted asset directory should contain:
- articulated_objects/
-
…[truncated 707 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_libero-benchmark_20260515T111137",
  "tool": "WebFetch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool call

_source line 43 · 2026-05-15T11:18:42.229475+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://github.com/Physical-Intelligence/openpi/blob/main/examples/libero/convert_libero_data_to_lerobot.py",
  "prompt": "Extract the FULL conversion script code. Show all imports, functions, the main conversion logic, command-line arguments, and how it maps LIBERO HDF5 fields to LeRobot format. Include every detail of the data mapping."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_libero-benchmark_20260515T111137",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://github.com/Physical-Intelligence/openpi/blob/main/examples/libero/convert_libero_data_to_lerobot.py",
    "prompt": "Extract the FULL conversion script code. Show all imports, functions, the main conversion logic, command-line arguments, and how it maps LIBERO HDF5 fields to LeRobot format. Include every detail of the data mapping."
  }
}
```

</details>

---

### Tool call

_source line 44 · 2026-05-15T11:18:42.229641+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://github.com/huggingface/lerobot-libero",
  "prompt": "Extract all information about this repository: what it does, how it integrates with LeRobot, installation instructions, usage, any conversion scripts or utilities. Include all README content."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_libero-benchmark_20260515T111137",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://github.com/huggingface/lerobot-libero",
    "prompt": "Extract all information about this repository: what it does, how it integrates with LeRobot, installation instructions, usage, any conversion scripts or utilities. Include all README content."
  }
}
```

</details>

---

### Tool result

_source line 45 · 2026-05-15T11:18:42.229773+00:00_

# LIBERO-Plus Technical Details

## Seven Perturbation Dimensions

The study introduces controlled perturbations across: "(i) objects layout, (ii) camera viewpoints, (iii) robot initial states, (iv) language instructions, (v) light conditions, (vi) background textures and (vii) sensor noise."

## Benchmark Construction

The researchers employed a "systematic two-stage process": first, they expanded the original LIBERO benchmark through seven distinct perturbation factors, then filtered tasks and balanced categories based on empirical findings. Subsequently, they evaluated results using four representative models and stratified tasks into five difficulty levels (Level-1 to Level-5) according to accuracy distributions.

## Key Implementation Findings

**Language Perturbations:**
- Blank instruction tests removed valid language input entirely
- Goal replacement tests substituted target objects with alternatives
- Results showed models degrade into vision-action patterns, largely disregarding language signals

**Visual Perturbations:**
- Camera changes (position, orientation, field-of-view) caused dramatic performance drops
- Robot initial pose variations significantly impacted success rates
- Background and lighting changes showed surprising resilience, attributed to wrist camera stability

**Compositional Testing:**
The study measured interaction effects using: "Δij = P(Di=1, Dj=1 | Y=1) - P(Di=1 | Y=1) · P(Dj=1 | Y=1)" where negative values indicate negative interactions between perturbation pairs.

## Benchmark Scale

LIBERO-Plus comprises "10,030 tasks spanning seven perturbation dimensions" with over 20,000 successful trajectories collected under systematically varied conditions.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_libero-benchmark_20260515T111137",
  "tool": "WebFetch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool call

_source line 46 · 2026-05-15T11:18:42.229920+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://lifelong-robot-learning.github.io/LIBERO/html/algo_data/datasets.html",
  "prompt": "Extract ALL details about datasets: observation space, action space, dimensions, data format, HDF5 structure, image sizes, proprioceptive state dimensions, and any other technical details about the data."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_libero-benchmark_20260515T111137",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://lifelong-robot-learning.github.io/LIBERO/html/algo_data/datasets.html",
    "prompt": "Extract ALL details about datasets: observation space, action space, dimensions, data format, HDF5 structure, image sizes, proprioceptive state dimensions, and any other technical details about the data."
  }
}
```

</details>

---

### Tool call

_source line 47 · 2026-05-15T11:18:42.230057+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://lifelong-robot-learning.github.io/LIBERO/html/getting_started/installation.html",
  "prompt": "Extract complete installation instructions, all commands, dependencies, and requirements."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_libero-benchmark_20260515T111137",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://lifelong-robot-learning.github.io/LIBERO/html/getting_started/installation.html",
    "prompt": "Extract complete installation instructions, all commands, dependencies, and requirements."
  }
}
```

</details>

---

### Tool call

_source line 48 · 2026-05-15T11:18:42.230187+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://huggingface.co/datasets/yifengzhu-hf/LIBERO-datasets",
  "prompt": "Extract ALL details: dataset sizes for each suite, file names, download instructions, data format description, observation and action space details, number of demonstrations per task, and any other technical specifications."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_libero-benchmark_20260515T111137",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://huggingface.co/datasets/yifengzhu-hf/LIBERO-datasets",
    "prompt": "Extract ALL details: dataset sizes for each suite, file names, download instructions, data format description, observation and action space details, number of demonstrations per task, and any other technical specifications."
  }
}
```

</details>

---

### Tool result

_source line 49 · 2026-05-15T11:18:42.230312+00:00_

# LIBERO Installation Instructions

## Prerequisites
The project requires **Python 3.8.13** and uses miniconda for environment management.

## Step-by-Step Installation

**1. Create Conda Environment**
```
conda create -n libero python=3.8.13
```

**2. Install Python Dependencies**
```
pip install -r requirements.txt
```

**3. Install PyTorch and Related Libraries**
```
pip install torch==1.11.0+cu113 torchvision==0.12.0+cu113 torchaudio==0.11.0 --extra-index-url https://download.pytorch.org/whl/cu113
```

**4. Install Robosuite**
The documentation notes that "robosuite" serves as the underlying simulation environment.
```
pip install robosuite
```

**5. Clone and Install LIBERO Package**
```
git clone git@github.com:Lifelong-Robot-Learning/LIBERO.git
pip install -e .
```

## Key Dependencies
- **Python**: 3.8.13
- **PyTorch**: 1.11.0 (with CUDA 11.3 support)
- **Robosuite**: Required simulation framework
- **Requirements.txt**: Contains additional package specifications (file contents not detailed in documentation)

The installation guide indicates the setup enables lifelong learning research upon completion.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_libero-benchmark_20260515T111137",
  "tool": "WebFetch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 50 · 2026-05-15T11:18:42.230455+00:00_

# LeRobot LIBERO Dataset Card

## Dataset Overview
**Name:** `lerobot/libero`  
**Task:** Robotics  
**License:** Apache 2.0  
**Created by:** LeRobot

## Dataset Statistics
- **Total Episodes:** 1,693
- **Total Frames:** 273,465
- **Total Tasks:** 40
- **Rows:** 273,465 (273K)
- **Total Size:** 1.94 GB
- **Video Files Size:** ~500 MB
- **Data Files Size:** ~100 MB
- **FPS:** 10.0

## Data Format & Structure
- **Format:** Parquet (auto-converted)
- **Robot Type:** Panda
- **Chunks Size:** 1,000
- **Split:** Train (0:1693)

## Column Names & Features

### Observation Features
- `observation.images.image` - Video (256×256×3 RGB, AV1 codec, yuv420p)
- `observation.images.image2` - Video (256×256×3 RGB, AV1 codec, yuv420p)
- `observation.state` - Float32, shape [8] (robot state vector)

### Action & Metadata
- `action` - Float32, shape [7] (action vector)
- `timestamp` - Float32
- `frame_index` - Int64
- `episode_index` - Int64
- `task_index` - Int64 (0-39)
- `index` - Int64 (row index)

## How to Load

### Using Hugging Face Datasets Library
```python
from datasets import load_dataset

# Load the dataset
dataset = load_dataset("lerobot/libero")

# Access training split
train_split = dataset["train"]

# View sample
print(train_split[0])
```

### Using Polars/Dask
The dataset is compatible with Polars and Dask libraries for distributed processing.

## Data Studio Access
- **Viewer:** Available at [Data Studio](/datasets/lerobot/libero/viewer/)
- **Interactive exploration** of all 273K rows

## Modalities
- **Tabular** (state vectors, actions, metadata)
- **Time-series** (sequential frame data)
- **Video** (RGB camera streams)

## Usage Notes
- Data is organized in parquet chunks for efficient loading
- Videos stored separately from structured data
- Each row represents a single timestep with corresponding observations and actions
- Suitable for training imitation learning and robotic control models

## Related Models
11+ models trained on this dataset, including:
- `lero
…[truncated 75 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_libero-benchmark_20260515T111137",
  "tool": "WebFetch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 51 · 2026-05-15T11:18:42.230625+00:00_

# LIBERO to LeRobot Conversion Script

## Overview
The script converts LIBERO dataset (stored in RLDS format via TensorFlow Datasets) to LeRobot format for robotics training.

## Full Code Structure

**Imports:**
```python
import shutil
from lerobot.common.datasets.lerobot_dataset import HF_LEROBOT_HOME
from lerobot.common.datasets.lerobot_dataset import LeRobotDataset
import tensorflow_datasets as tfds
import tyro
```

**Configuration:**
- `REPO_NAME`: "your_hf_username/libero" (output dataset identifier)
- `RAW_DATASET_NAMES`: Four LIBERO variants ("libero_10_no_noops", "libero_goal_no_noops", "libero_object_no_noops", "libero_spatial_no_noops")

## Data Mapping Details

The script maps LIBERO fields to LeRobot features as follows:

| LIBERO Field | LeRobot Feature | Type | Shape | Purpose |
|---|---|---|---|---|
| observation["image"] | image | image | (256, 256, 3) | Primary camera view |
| observation["wrist_image"] | wrist_image | image | (256, 256, 3) | Wrist camera view |
| observation["state"] | state | float32 | (8,) | Proprioceptive data |
| action | actions | float32 | (7,) | Robot joint commands |
| language_instruction | task | string | N/A | Task description |

## Main Conversion Logic

1. Cleans existing output directory
2. Creates LeRobot dataset with specified features and metadata (robot_type="panda", fps=10)
3. Iterates through four raw LIBERO datasets
4. For each episode and step, extracts observation and action data
5. Calls `dataset.add_frame()` with mapped fields
6. Saves completed episodes with `dataset.save_episode()`
7. Optionally pushes to Hugging Face Hub with tags and metadata

## Command-Line Interface

Uses `tyro.cli(main)` with arguments:
- `data_dir`: Path to LIBERO dataset directory (required)
- `push_to_hub`: Boolean flag for Hugging Face Hub upload (optional)

**Note:** Requires TensorFlow and tensorflow_datasets installation; processing takes ~30 minutes.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_libero-benchmark_20260515T111137",
  "tool": "WebFetch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 52 · 2026-05-15T11:18:42.230769+00:00_

# LIBERO Datasets - Extracted Details

## Dataset Structure

The LIBERO datasets are organized into **5 suites**:
- `libero_object/`
- `libero_spatial/`
- `libero_goal/`
- `libero_90/`
- `libero_10/`

## Key Specifications

| Metric | Value |
|--------|-------|
| **Total Size** | 100 GB |
| **Monthly Downloads** | 24,823 |
| **License** | Apache 2.0 |
| **Data Format** | HDF5 files |

## Data Format

- Demonstrations are stored in **HDF5 file format**
- Each task contains multiple demonstrations stored within HDF5 containers

## Download Instructions

For detailed download and configuration instructions, refer to the **official download script**:
```
https://github.com/Lifelong-Robot-Learning/LIBERO/blob/master/benchmark_scripts/download_libero_datasets.py
```

## Limitations of This Dataset Card

⚠️ **Note:** The dataset viewer is unavailable as the repository does not have auto-detected supported data files configured. Manual data file configuration may be required.

## Related Work

- **Models trained on this dataset:**
  - tanshh97/RIPT_VLA (May 29, 2025)
  - Youyi-Kou/rynnvla-002 (Jan 3)

- **Space using dataset:**
  - jacob314159/robot-episode-curator

---

**Missing Details:** The page content does not include observation/action space specifications, individual suite sizes, or per-task demonstration counts. Consult the [official LIBERO GitHub repository](https://github.com/Lifelong-Robot-Learning/LIBERO) for comprehensive technical documentation.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_libero-benchmark_20260515T111137",
  "tool": "WebFetch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 53 · 2026-05-15T11:18:42.230909+00:00_

# LIBERO-LeRobot Repository Summary

## Overview
This is Hugging Face's fork of the official LIBERO benchmark, designed for studying knowledge transfer in multitask and lifelong robot learning. The repository extends the original LIBERO framework with "modifications for compatibility with LeRobot, simplified installation, and large-scale robotics experiments."

## Core Purpose
LIBERO provides a benchmarking framework that includes:
- A procedural generation pipeline for manipulation tasks
- 130 tasks organized into four suites: LIBERO-Spatial, LIBERO-Object, LIBERO-Goal, and LIBERO-100
- Five research topics and three visuomotor policy architectures
- Three lifelong learning algorithms with baseline implementations

## Installation
The setup requires:
1. Creating a conda environment with Python 3.8.13
2. Cloning the repository
3. Installing dependencies via `pip install -r requirements.txt`
4. Installing PyTorch with CUDA 11.3 support
5. Installing the package in editable mode: `pip install -e .`

## Dataset Acquisition
Datasets can be downloaded via:
- `python benchmark_scripts/download_libero_datasets.py` (default storage)
- Alternative: `python benchmark_scripts/download_libero_datasets.py --use-huggingface` (from Hugging Face hub)
- Specific dataset selection available through the `--datasets` flag

## Usage Workflow

**Task Retrieval:** Users import from `libero.libero` to access benchmark dictionaries and instantiate task suites, then retrieve specific tasks with associated BDDL files and language descriptions.

**Training:** Lifelong learning experiments require selecting a benchmark, policy type (bc_rnn_policy, bc_transformer_policy, bc_vilt_policy), and algorithm (base, er, ewc, packnet, multitask), then executing the training script with specified parameters.

**Evaluation:** Separate evaluation script available for resource-constrained scenarios, accepting benchmark name, task ID, algorithm, policy type, seed, epoch, and CUDA device specifications.

## Ke
…[truncated 501 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_libero-benchmark_20260515T111137",
  "tool": "WebFetch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 54 · 2026-05-15T11:18:42.231067+00:00_

# Dataset Details from LIBERO Documentation

Based on the provided webpage content, the available information about datasets is limited:

## Available Datasets

The documentation mentions four datasets for lifelong learning research:
- `libero_spatial` (10 tasks)
- `libero_object` (10 tasks)
- `libero_goal` (10 tasks)
- `libero_100` (100 tasks)

## Download Instructions

Datasets can be downloaded via Python scripts to a `./datasets` directory, with options to retrieve all datasets or specific ones individually.

## Technical Specifications

**Unfortunately, the provided webpage content does not include technical details** about:
- Observation space dimensions
- Action space specifications
- Data format or encoding
- HDF5 file structures
- Image resolutions
- Proprioceptive state dimensions
- Any other structural data specifications

The current page serves as a navigation hub rather than a comprehensive technical reference. To access detailed specifications about data format, dimensions, and structure, you would need to consult additional documentation pages, the actual dataset files, or the project's GitHub repository.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_libero-benchmark_20260515T111137",
  "tool": "WebFetch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 55 · 2026-05-15T11:18:42.231299+00:00_

# LIBERO-Plus: Perturbation Framework Technical Details

## 1. Seven Perturbation Dimensions

**Objects Layout (O1-O2):**
- O1 adds "n additional unseen objects into the task scene" from a set of 416 distractor objects via BDDL modifications
- O2 applies "random perturbations to the target object's initial position (x,y,z) and orientation" while preserving semantic relationships

**Background Textures (B1-B2):**
- B1 changes "scene texture of the environment" using 950 curated textures via XML scene definition files
- B2 randomly alters "texture of the working surface (e.g., tabletop or floor)"

**Light Conditions (L1-L4):**
- L1: Diffuse color adjustment via RGB channels
- L2: Parallel light source direction changes
- L3: Specular highlight intensity (affecting reflective surfaces)
- L4: Boolean shadow casting control

**Camera Viewpoints (C1-C3):**
- C1: Distance scaling from 1.01× to 2.00× original value along optical axis
- C2: Spherical position changes with azimuth (Δθ) and elevation (Δφ) within 15°–75° cones
- C3: Camera orientation perturbation (yaw, pitch, roll) within 2°–10°

**Robot Initial States:**
- "Random perturbations are applied to the robot arm's initial joint positions" with magnitudes 0.1–0.5 via Problem class interface modifications

**Language Instructions (R1-R3):**
- R1: Distraction rewrites adding task-irrelevant contextual information
- R2: Commonsense-based object description replacements
- R3: Reasoning complexity alterations for multi-step tasks

**Sensor Noise (N1-N5):**
- Motion Blur: kernel radius (r=5 to 35), Gaussian σ (2 to 20), angle θ ∈ U(-45°, 45°)
- Gaussian Blur: σ from 1 to 10
- Zoom Blur: scaling factors [s_min, s_max, step] from [1, 1.11, 0.01] to [1, 1.56, 0.03]
- Fog: density α (0.5–5.0), decay rate β (1.3–3.0)
- Glass Blur: σ (0.5–2.5), pixel displacement δ (1–5), iterations (1–3)

## 2. Simulation Implementation

**Environment Framework:** LIBERO benchmark built on MuJoCo physics engine via robosuite

**Implementation 
…[truncated 3105 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_libero-benchmark_20260515T111137",
  "tool": "WebFetch",
  "elapsed_ms": 2
}
```

</details>

---

### Tool call

_source line 56 · 2026-05-15T11:18:42.231478+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://raw.githubusercontent.com/Lifelong-Robot-Learning/LIBERO/master/libero/libero/envs/env_wrapper.py",
  "prompt": "Extract ALL details about observation space and action space: dimensions, meanings of each dimension, image sizes, proprioceptive state components, action components (position, rotation, gripper), and any other relevant specifications."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_libero-benchmark_20260515T111137",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://raw.githubusercontent.com/Lifelong-Robot-Learning/LIBERO/master/libero/libero/envs/env_wrapper.py",
    "prompt": "Extract ALL details about observation space and action space: dimensions, meanings of each dimension, image sizes, proprioceptive state components, action components (position, rotation, gripper), and any other relevant specifications."
  }
}
```

</details>

---

### Tool call

_source line 57 · 2026-05-15T11:18:42.231685+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://huggingface.co/datasets/HuggingFaceVLA/libero",
  "prompt": "Extract the full dataset card: exact dataset name, size, number of episodes, task suites included, how to load, data format, any instructions on usage with LeRobot. Include all metadata and statistics."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_libero-benchmark_20260515T111137",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://huggingface.co/datasets/HuggingFaceVLA/libero",
    "prompt": "Extract the full dataset card: exact dataset name, size, number of episodes, task suites included, how to load, data format, any instructions on usage with LeRobot. Include all metadata and statistics."
  }
}
```

</details>

---

### Tool call

_source line 58 · 2026-05-15T11:18:42.231829+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://raw.githubusercontent.com/Lifelong-Robot-Learning/LIBERO/master/benchmark_scripts/download_libero_datasets.py",
  "prompt": "Extract the complete download script: URLs for each dataset, download methods, file sizes, dataset names, and any configuration options."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_libero-benchmark_20260515T111137",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://raw.githubusercontent.com/Lifelong-Robot-Learning/LIBERO/master/benchmark_scripts/download_libero_datasets.py",
    "prompt": "Extract the complete download script: URLs for each dataset, download methods, file sizes, dataset names, and any configuration options."
  }
}
```

</details>

---

### Tool call

_source line 59 · 2026-05-15T11:18:42.231964+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://huggingface.co/docs/lerobot/main/libero_plus",
  "prompt": "Extract ALL information about LIBERO-plus: what it is, how it differs from standard LIBERO, any new datasets, new tasks, commands, etc."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_libero-benchmark_20260515T111137",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://huggingface.co/docs/lerobot/main/libero_plus",
    "prompt": "Extract ALL information about LIBERO-plus: what it is, how it differs from standard LIBERO, any new datasets, new tasks, commands, etc."
  }
}
```

</details>

---

### Tool result

_source line 60 · 2026-05-15T11:18:42.232114+00:00_

# LIBERO-plus

LIBERO-plus is a **robustness benchmark** for Vision-Language-Action (VLA) models built on top of [LIBERO](./libero). It systematically stress-tests policies by applying **seven independent perturbation dimensions** to the original LIBERO task set, exposing failure modes that standard benchmarks miss.

- Paper: [In-depth Robustness Analysis of Vision-Language-Action Models](https://arxiv.org/abs/2510.13626)
- GitHub: [sylvestf/LIBERO-plus](https://github.com/sylvestf/LIBERO-plus)
- Dataset: [lerobot/libero_plus](https://huggingface.co/datasets/lerobot/libero_plus)

![An overview of the LIBERO-plus benchmark perturbation dimensions](https://github.com/sylvestf/LIBERO-plus/raw/main/static/images/libero-plus.jpg)

## Perturbation dimensions

LIBERO-plus creates ~10 000 task variants by perturbing each original LIBERO task along these axes:

| Dimension             | What changes                                          |
| --------------------- | ----------------------------------------------------- |
| Objects layout        | Target position, presence of confounding objects      |
| Camera viewpoints     | Camera position, orientation, field-of-view           |
| Robot initial states  | Manipulator start pose                                |
| Language instructions | LLM-rewritten task description (paraphrase / synonym) |
| Light conditions      | Intensity, direction, color, shadow                   |
| Background textures   | Scene surface and object appearance                   |
| Sensor noise          | Photometric distortions and image degradation         |

## Available task suites

LIBERO-plus covers the same five suites as LIBERO:

| Suite          | CLI name         | Tasks | Max steps | Description                                        |
| -------------- | ---------------- | ----- | --------- | -------------------------------------------------- |
| LIBERO-Spatial | `libero_spatial` | 10    | 280       | Tasks requiring reasoning about spatia
…[truncated 5193 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_libero-benchmark_20260515T111137",
  "tool": "WebFetch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 61 · 2026-05-15T11:18:42.232279+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "huggingface datasets \"lerobot/libero_spatial\" OR \"lerobot/libero_object\" OR \"lerobot/libero_goal\" OR \"lerobot/libero_90\" site:huggingface.co"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_libero-benchmark_20260515T111137",
  "tool": "WebSearch",
  "tool_args": {
    "query": "huggingface datasets \"lerobot/libero_spatial\" OR \"lerobot/libero_object\" OR \"lerobot/libero_goal\" OR \"lerobot/libero_90\" site:huggingface.co"
  }
}
```

</details>

---

### Tool call

_source line 62 · 2026-05-15T11:18:42.232415+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://raw.githubusercontent.com/Lifelong-Robot-Learning/LIBERO/master/libero/lifelong/evaluate.py",
  "prompt": "Extract ALL details about evaluation: what metrics are computed, how success rate is calculated, how many episodes are run, evaluation protocol, output format, and command-line arguments."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_libero-benchmark_20260515T111137",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://raw.githubusercontent.com/Lifelong-Robot-Learning/LIBERO/master/libero/lifelong/evaluate.py",
    "prompt": "Extract ALL details about evaluation: what metrics are computed, how success rate is calculated, how many episodes are run, evaluation protocol, output format, and command-line arguments."
  }
}
```

</details>

---

### Tool call

_source line 63 · 2026-05-15T11:18:42.232568+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://github.com/sylvestf/LIBERO-plus",
  "prompt": "Extract the full repository structure, installation commands, configuration details, how to run evaluation, and any code examples. Include exact pip install commands, asset download links, and configuration file paths."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_libero-benchmark_20260515T111137",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://github.com/sylvestf/LIBERO-plus",
    "prompt": "Extract the full repository structure, installation commands, configuration details, how to run evaluation, and any code examples. Include exact pip install commands, asset download links, and configuration file paths."
  }
}
```

</details>

---

### Tool call

_source line 64 · 2026-05-15T11:18:42.232700+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "LIBERO robosuite MuJoCo built-in camera randomization lighting randomization domain randomization config"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_libero-benchmark_20260515T111137",
  "tool": "WebSearch",
  "tool_args": {
    "query": "LIBERO robosuite MuJoCo built-in camera randomization lighting randomization domain randomization config"
  }
}
```

</details>

---

### Tool call

_source line 65 · 2026-05-15T11:18:42.232827+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "site:github.com Lifelong-Robot-Learning LIBERO domain randomization camera jitter"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_libero-benchmark_20260515T111137",
  "tool": "WebSearch",
  "tool_args": {
    "query": "site:github.com Lifelong-Robot-Learning LIBERO domain randomization camera jitter"
  }
}
```

</details>

---

### Tool result

_source line 66 · 2026-05-15T11:18:42.232950+00:00_

# Observation and Action Space Analysis

Based on the provided code, here's what can be determined about the spaces:

## Observation Space

The code doesn't explicitly define observation dimensions. However, several clues exist:

- **Camera observations**: The environment supports multiple cameras with configurable parameters:
  - Default cameras: `"agentview"` and `"robot0_eye_in_hand"`
  - Resolution: 128×128 pixels (customizable via `camera_heights` and `camera_widths`)
  - Optional depth channels: `camera_depths=False` by default
  - Optional segmentation masks: `camera_segmentations=None` by default

- **Proprioceptive state**: Generated through `"_get_observations()"` and `"_update_observables(force=False)"`, but specific components aren't detailed in this excerpt.

## Action Space

No explicit action space definition appears in the provided code. However, the controller configuration suggests:

- Controller type: `"OSC_POSE"` (default) - indicates operational space control
- Likely includes: position commands, rotation/orientation, and gripper state
- The `"step(action)"` method accepts actions but doesn't specify their structure or dimensionality

## Key Limitation

The actual observation and action space specifications reside in the underlying `robosuite` library and task-specific implementations referenced via `"TASK_MAPPING[self.problem_name]"`, which aren't included in this excerpt.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_libero-benchmark_20260515T111137",
  "tool": "WebFetch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 67 · 2026-05-15T11:18:42.233091+00:00_

# LIBERO Dataset Download Script Analysis

## Script Overview
This Python script manages downloads for LIBERO robotic manipulation datasets. However, **the actual download URLs, file sizes, and implementation details are not contained in this code snippet**.

## Available Configuration Options

**Download Directory:**
- Default: `get_libero_path("datasets")`
- Customizable via `--download-dir` argument

**Dataset Choices:**
The script supports four dataset options via `--datasets`:
- "all" (default)
- "libero_goal"
- "libero_spatial"
- "libero_object"
- "libero_100"

**Download Source:**
- `--use-huggingface` flag toggles between two sources
- Default: Original download links with expiration warning
- Alternative: Hugging Face hosting

## Implementation Details

The script delegates actual downloading to `download_utils.libero_dataset_download()`, which is imported but not shown. Key functions referenced:
- `libero_dataset_download()` – performs the actual transfers
- `check_libero_dataset()` – verifies downloaded files

The script includes user prompts warning that "original links may lead to failures" and suggests switching to Hugging Face if users decline.

## Missing Information
**URLs, file sizes, and detailed download methods are located in the `download_utils` module**, which is not provided in this excerpt.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_libero-benchmark_20260515T111137",
  "tool": "WebFetch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 68 · 2026-05-15T11:18:42.233227+00:00_

Web search results for query: "huggingface datasets "lerobot/libero_spatial" OR "lerobot/libero_object" OR "lerobot/libero_goal" OR "lerobot/libero_90" site:huggingface.co"

Links: [{"title":"IPEC-COMMUNITY/libero_90_no_noops_lerobot · Dataset converted ideas","url":"https://huggingface.co/datasets/IPEC-COMMUNITY/libero_90_no_noops_lerobot/discussions/2"},{"title":"lerobot/libero_object_image · Datasets at Hugging Face","url":"https://huggingface.co/datasets/lerobot/libero_object_image"},{"title":"lerobot/libero_spatial_image · Datasets at Hugging Face","url":"https://huggingface.co/datasets/lerobot/libero_spatial_image"},{"title":"Commits · lerobot/libero_goal_image","url":"https://huggingface.co/datasets/lerobot/libero_goal_image/commits/main"}]

Based on the web search results, I found references to LeRobot LIBERO datasets on Hugging Face. The search revealed:

1. lerobot/libero_object_image dataset was created using LeRobot

2. lerobot/libero_spatial_image dataset was created using LeRobot

3. lerobot/libero_goal_image is available on Hugging Face

These datasets appear to be part of the LeRobot framework's LIBERO dataset collection on Hugging Face. The search results also mention discussions about converting LIBERO datasets and comparisons between different LIBERO variants (spatial, goal, object, and the 90-task version). The results indicate that LIBERO has different variants including LIBERO 10, spatial, goal and object datasets.

If you need more specific information about any of these datasets, their documentation, or how to access them, I can search for additional details.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_libero-benchmark_20260515T111137",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 69 · 2026-05-15T11:18:42.233360+00:00_

# Evaluation Details Extraction

## Metrics Computed
Two primary metrics are calculated:
1. **Loss**: Test dataset loss (initialized as 0.0, not actively computed in shown code)
2. **Success Rate**: Proportion of successful task completions across parallel environments

## Success Rate Calculation
The implementation runs "20 parallel environments" simultaneously. A task succeeds when the environment signals completion via the `done` flag. The success rate is calculated as: `num_success / env_num` (successful environments divided by total environments).

## Episodes and Evaluation Protocol
- **Parallel rollouts**: "env_num = 20" concurrent environments
- **Maximum steps per evaluation**: "cfg.eval.max_steps" (value not specified in code)
- **Physics simulation**: "5" initial steps with zero actions before policy control begins
- **Termination conditions**: Rollout ends when all environments signal completion or max steps reached

## Output Format
Results are saved as a PyTorch tensor dictionary containing:
```
{"loss": test_loss, "success_rate": success_rate}
```
Saved to: `{save_dir}/{benchmark}_{algo}_{policy}_{seed}_[ep/load]_{task_id}.stats`

## Command-Line Arguments
- `--benchmark`: Task suite selection (required)
- `--task_id`: Target task number (required)
- `--algo`: Learning algorithm (required)
- `--policy`: Policy architecture (required)
- `--seed`: Random seed (required)
- `--ep`: Episode for multitask checkpoints
- `--load_task`: Task checkpoint to load
- `--device_id`: GPU device selection
- `--save-videos`: Optional video recording flag

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_libero-benchmark_20260515T111137",
  "tool": "WebFetch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 70 · 2026-05-15T11:18:42.233523+00:00_

Web search results for query: "site:github.com Lifelong-Robot-Learning LIBERO domain randomization camera jitter"

Links: [{"title":"GitHub - Lifelong-Robot-Learning/LIBERO: Benchmarking Knowledge Transfer in Lifelong Robot Learning · GitHub","url":"https://github.com/Lifelong-Robot-Learning/LIBERO"},{"title":"Issues · Lifelong-Robot-Learning/LIBERO","url":"https://github.com/Lifelong-Robot-Learning/LIBERO/issues"},{"title":"Lifelong Robot Learning · GitHub","url":"https://github.com/Lifelong-Robot-Learning"},{"title":"Technical details Regarding LIBERO Dataset · Issue #95 · Lifelong-Robot-Learning/LIBERO","url":"https://github.com/Lifelong-Robot-Learning/LIBERO/issues/95"},{"title":"Issues with Playback · Issue #16 · Lifelong-Robot-Learning/LIBERO","url":"https://github.com/Lifelong-Robot-Learning/LIBERO/issues/16"},{"title":"GitHub - Zxy-MLlab/LIBERO-PRO: LIBERO-PRO is the official repository of the LIBERO-PRO — an evaluation extension of the original LIBERO benchmark","url":"https://github.com/Zxy-MLlab/LIBERO-PRO"},{"title":"LIBERO-Object image rendering issue: darker floors · Issue #88 · Lifelong-Robot-Learning/LIBERO","url":"https://github.com/Lifelong-Robot-Learning/LIBERO/issues/88"},{"title":"LIBERO/README.md at master · Lifelong-Robot-Learning/LIBERO","url":"https://github.com/Lifelong-Robot-Learning/LIBERO/blob/master/README.md"},{"title":"Activity · Lifelong-Robot-Learning/LIBERO","url":"https://github.com/Lifelong-Robot-Learning/LIBERO/activity"},{"title":"collect_demonstrations.py · Issue #48 · Lifelong-Robot-Learning/LIBERO","url":"https://github.com/Lifelong-Robot-Learning/LIBERO/issues/48"}]

The search returned results from the LIBERO GitHub repository and related pages. LIBERO is designed for studying knowledge transfer in multitask and lifelong robot learning problems. It provides a procedural generation pipeline that could generate an infinite number of manipulation tasks, with 130 tasks grouped into four task suites: LIBERO-Spatial, LIBERO-Obje
…[truncated 832 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_libero-benchmark_20260515T111137",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 71 · 2026-05-15T11:18:42.233679+00:00_

# LIBERO-Plus Repository Summary

## Overview
LIBERO-Plus is "a generalized benchmark for in-depth robustness analysis of vision-language-action models" offering comprehensive evaluation across 7 perturbation dimensions with 10,030 tasks.

## Installation Commands

```bash
# Clone repository
git clone https://github.com/sylvestf/LIBERO-plus.git
cd LIBERO-plus

# Uninstall existing LIBERO if present

# Install package
pip install -e .

# Install system dependencies
apt install libexpat1
apt install libfontconfig1-dev
apt install libpython3-stdlib
apt-get install libmagickwand-dev

# Install additional Python requirements
pip install -r extra_requirements.txt
```

## Asset Download & Configuration

**Assets Location:** Download from [Hugging Face LIBERO-plus dataset](https://huggingface.co/datasets/Sylvest/LIBERO-plus/tree/main)

**Installation Path:** Extract `assets.zip` to `LIBERO-plus/libero/libero/`

**Configuration File:** `/root/.libero/config.yaml` (verify repo path in `libero/__init__.py`)

**Required Asset Structure:**
```
libero/libero/assets/
├── articulated_objects/
├── new_objects/
├── scenes/
├── stable_hope_objects/
├── stable_scanned_objects/
├── textures/
├── turbosquid_objects/
└── supporting XML/STL files
```

## Evaluation Setup

Modify configuration to set `num_trials_per_task: 1` (adjusted from original 50). Task mappings between IDs, perturbation categories, and difficulty levels are provided in `.libero/libero/benchmark/task_classification.json`.

## Additional Resources

- **RLDS Training Dataset:** Available on Hugging Face
- **Fine-tuned Model:** OpenVLA-OFT weights after mix-SFT provided
- **LeRobot Dataset:** Alternative training dataset available

## Key Performance Metrics

Top-performing model (OpenVLA-OFT+) achieves 79.6% average across perturbation categories, with particularly strong results in camera robustness (92.8%) and light conditions (94.9%).

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_libero-benchmark_20260515T111137",
  "tool": "WebFetch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 72 · 2026-05-15T11:18:42.233833+00:00_

Web search results for query: "LIBERO robosuite MuJoCo built-in camera randomization lighting randomization domain randomization config"

Links: [{"title":"Demo Showcases — robosuite 1.5 documentation","url":"https://robosuite.ai/docs/demos.html"},{"title":"robosuite/robosuite/utils/mjmod.py at master · ARISE-Initiative/robosuite","url":"https://github.com/ARISE-Initiative/robosuite/blob/master/robosuite/utils/mjmod.py"},{"title":"Environments — robosuite 1.5 documentation","url":"https://robosuite.ai/docs/modules/environments.html"},{"title":"Sim-to-Real Transfer — robosuite 1.5 documentation","url":"https://robosuite.ai/docs/algorithms/sim2real.html"},{"title":"Changelog — robosuite 1.5 documentation","url":"https://robosuite.ai/docs/changelog.html"},{"title":"robosuite.utils package — robosuite 1.5 documentation","url":"https://robosuite.ai/docs/source/robosuite.utils.html"},{"title":"robosuite | robosuite: A Modular Simulation Framework and Benchmark for Robot Learning","url":"https://robosuite.ai/"},{"title":"GitHub - ARISE-Initiative/robosuite: robosuite: A Modular Simulation Framework and Benchmark for Robot Learning · GitHub","url":"https://github.com/ARISE-Initiative/robosuite"},{"title":"robosuite · PyPI","url":"https://pypi.org/project/robosuite/"},{"title":"GitHub - Robot-Learning-Library/robolite: This is a fork of Surreal Robotics Suite that enables support to domain randomization and inverse kinematics (IK).","url":"https://github.com/Robot-Learning-Library/robolite"}]

Based on the search results, here's what I found about LIBERO, robosuite, MuJoCo, and domain randomization features:

## Domain Randomization in Robosuite

Domain randomization can be easily enabled by wrapping an environment with the DomainRandomizationWrapper, with randomization functionality focusing on visual variations, including colors, textures, and camera viewpoints.

## Randomization Modders

Robosuite provides three main Modders: CameraModder for controlling camera parameters
…[truncated 1087 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_libero-benchmark_20260515T111137",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool call

_source line 73 · 2026-05-15T11:18:42.233992+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://raw.githubusercontent.com/Lifelong-Robot-Learning/LIBERO/master/libero/libero/benchmark/libero_suite.py",
  "prompt": "Extract ALL details about the benchmark suites: LIBERO-Spatial, LIBERO-Object, LIBERO-Goal, LIBERO-Long, LIBERO-90, LIBERO-10. How many tasks in each? What are the task descriptions? How are they defined?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_libero-benchmark_20260515T111137",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://raw.githubusercontent.com/Lifelong-Robot-Learning/LIBERO/master/libero/libero/benchmark/libero_suite.py",
    "prompt": "Extract ALL details about the benchmark suites: LIBERO-Spatial, LIBERO-Object, LIBERO-Goal, LIBERO-Long, LIBERO-90, LIBERO-10. How many tasks in each? What are the task descriptions? How are they defined?"
  }
}
```

</details>

---

### Tool result

_source line 74 · 2026-05-15T11:18:42.234117+00:00_

Request failed with status code 404

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_libero-benchmark_20260515T111137",
  "tool": "WebFetch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 75 · 2026-05-15T11:18:42.234248+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://raw.githubusercontent.com/Lifelong-Robot-Learning/LIBERO/master/libero/libero/benchmark/__init__.py",
  "prompt": "Extract all benchmark suite names, class definitions, task counts, and how benchmarks are registered or accessed."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_libero-benchmark_20260515T111137",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://raw.githubusercontent.com/Lifelong-Robot-Learning/LIBERO/master/libero/libero/benchmark/__init__.py",
    "prompt": "Extract all benchmark suite names, class definitions, task counts, and how benchmarks are registered or accessed."
  }
}
```

</details>

---

### Tool call

_source line 76 · 2026-05-15T11:18:42.234380+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://raw.githubusercontent.com/Lifelong-Robot-Learning/LIBERO/master/libero/lifelong/datasets.py",
  "prompt": "Extract ALL details about the dataset class: HDF5 data structure, observation keys, action dimensions, image dimensions, proprioceptive state components, how data is loaded and processed. Be extremely thorough."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_libero-benchmark_20260515T111137",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://raw.githubusercontent.com/Lifelong-Robot-Learning/LIBERO/master/libero/lifelong/datasets.py",
    "prompt": "Extract ALL details about the dataset class: HDF5 data structure, observation keys, action dimensions, image dimensions, proprioceptive state components, how data is loaded and processed. Be extremely thorough."
  }
}
```

</details>

---

### Tool call

_source line 77 · 2026-05-15T11:18:42.234528+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://robosuite.ai/docs/algorithms/sim2real.html",
  "prompt": "Extract all details about domain randomization in robosuite: CameraModder, TextureModder, LightingModder parameters, DomainRandomizationWrapper usage, configuration options, parameter ranges, and code examples. Include exact API details."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_libero-benchmark_20260515T111137",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://robosuite.ai/docs/algorithms/sim2real.html",
    "prompt": "Extract all details about domain randomization in robosuite: CameraModder, TextureModder, LightingModder parameters, DomainRandomizationWrapper usage, configuration options, parameter ranges, and code examples. Include exact API details."
  }
}
```

</details>

---

### Tool result

_source line 78 · 2026-05-15T11:18:42.234656+00:00_

# LIBERO Benchmark Suite Overview

## Benchmark Suite Names
The codebase defines five core suites: `libero_spatial`, `libero_object`, `libero_goal`, `libero_90`, and `libero_10`.

## Class Definitions
Six benchmark classes are registered via the `@register_benchmark` decorator:

- **LIBERO_SPATIAL**: Handles spatial reasoning tasks
- **LIBERO_OBJECT**: Focuses on object-centric tasks
- **LIBERO_GOAL**: Addresses goal-oriented tasks
- **LIBERO_90**: Contains 90 combined tasks (uses all available tasks)
- **LIBERO_10**: Manages 10-task suites with predefined orderings
- **LIBERO_100**: Includes 100 total tasks

## Task Counts
The `libero_spatial`, `libero_object`, and `libero_goal` suites each contain 10 tasks. The `libero_90` contains 90 tasks, while `libero_100` contains 100 tasks. Task counts are dynamically determined through `get_num_tasks()`.

## Registration & Access
The registration system uses a case-insensitive mapping: "benchmark names are registered automatically via the decorator and accessed through `get_benchmark()`" which queries `BENCHMARK_MAPPING`. The `get_benchmark_dict()` function provides the complete registry with optional help display.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_libero-benchmark_20260515T111137",
  "tool": "WebFetch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 79 · 2026-05-15T11:18:42.234803+00:00_

# LIBERO Dataset Card

## Dataset Overview

**Dataset Name:** `HuggingFaceVLA/libero`

**Source:** Hugging Face Datasets

**Task Category:** Robotics

**Modalities:** Image, Time-series

**Format:** Parquet

**License:** Apache 2.0

---

## Dataset Statistics

| Metric | Value |
|--------|-------|
| **Total Rows** | 273,000 |
| **Size Category** | 100K - 1M |
| **Splits** | 1 (train) |
| **Episodes** | 148 |
| **Tasks** | 10 |
| **Subset** | default |

---

## Data Structure

### Observation Fields
- **observation.images.image** - Primary camera image (256×256 pixels)
- **observation.images.image2** - Secondary camera image (256×256 pixels)
- **observation.state** - Robot state vector (8 floating-point values)

### Action Fields
- **action** - Action vector (7 elements representing robot control commands)

### Metadata Fields
- **timestamp** - float32 (0-45.4 range)
- **frame_index** - int64 (frame within episode)
- **episode_index** - int64 (0-147, 148 total episodes)
- **task_index** - int64 (0-9, 10 tasks)
- **index** - int64 (global row index)

---

## Sample Data Examples

From the viewer, sample observations show:
- Robot arm in tabletop manipulation scenario
- Dual RGB camera views of workspace
- Continuous 7-DOF joint commands
- State includes position, orientation, and gripper status

**Example action structure:** `[0.016, 0, 0, 0, 0, 0, -1]` (normalized joint velocities + gripper)

---

## How to Load the Dataset

### Using Hugging Face Datasets Library

```python
from datasets import load_dataset

# Load the full dataset
dataset = load_dataset("HuggingFaceVLA/libero")

# Access train split
train_data = dataset['train']

# Inspect a sample
sample = train_data[0]
print(sample.keys())
# Output: dict_keys(['observation.images.image', 'observation.images.image2', 
#                     'observation.state', 'action', 'timestamp', 'frame_index', 
#                     'episode_index', 'task_index', 'index'])
```

### Using LeRobot Integration

```python
from ler
…[truncated 2530 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_libero-benchmark_20260515T111137",
  "tool": "WebFetch",
  "elapsed_ms": 3
}
```

</details>

---

### Tool call

_source line 80 · 2026-05-15T11:18:42.234961+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://github.com/ARISE-Initiative/robosuite/blob/master/robosuite/utils/mjmod.py",
  "prompt": "Extract the CameraModder, TextureModder, and LightingModder class definitions. Include all parameters they can modify, default values, and method signatures. Focus on what visual properties can be randomized."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_libero-benchmark_20260515T111137",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://github.com/ARISE-Initiative/robosuite/blob/master/robosuite/utils/mjmod.py",
    "prompt": "Extract the CameraModder, TextureModder, and LightingModder class definitions. Include all parameters they can modify, default values, and method signatures. Focus on what visual properties can be randomized."
  }
}
```

</details>

---

### Tool call

_source line 81 · 2026-05-15T11:18:42.235119+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://huggingface.co/datasets/Sylvest/LIBERO-plus",
  "prompt": "Extract all details about the LIBERO-plus dataset: file structure, download instructions, dataset contents, how the training data is organized, and any usage instructions."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_libero-benchmark_20260515T111137",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://huggingface.co/datasets/Sylvest/LIBERO-plus",
    "prompt": "Extract all details about the LIBERO-plus dataset: file structure, download instructions, dataset contents, how the training data is organized, and any usage instructions."
  }
}
```

</details>

---

### Tool result

_source line 82 · 2026-05-15T11:18:42.235272+00:00_

# Dataset Class Details Analysis

## Data Loading Architecture

The code provides a wrapper around robomimic's `SequenceDataset` class. The primary function `get_dataset()` loads HDF5 demonstration files and initializes observation utilities.

## HDF5 Structure

The HDF5 file organization relies on:
- **Observation keys**: Dynamically extracted from `obs_modality` dictionary (which groups observations by modality type)
- **Action data**: Loaded as a standard dataset key labeled `"actions"`
- **Shape metadata**: Extracted via `FileUtils.get_shape_metadata_from_dataset()`, retrieving dimensions for all observation keys

The code explicitly notes: *"robomimic's SequenceDataset has two properties: seq_len and frame_stack, we should in principle use seq_len, but the paddings of the two are different"*, indicating the internal complexity of sequence handling.

## Data Processing Parameters

Configuration options include:
- **Sequence length** and **frame stacking**: Handled separately with independent padding strategies
- **Caching mode** (`hdf5_cache_mode="low_dim"`): Controls in-memory dataset caching to minimize file I/O
- **Padding**: Both sequence length and frame stack use padding; no pad masks are generated

## Observation Modality

The function accepts `obs_modality` as a nested dictionary where modality names map to lists of observation keys. Specific dimensions (image sizes, proprioceptive state components) are extracted from shape metadata but aren't hardcoded in this file.

## Dataset Wrapper Classes

Three wrapper implementations manage multi-task and truncated scenarios while preserving the underlying sequence structure and adding task embeddings or buffer constraints.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_libero-benchmark_20260515T111137",
  "tool": "WebFetch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 83 · 2026-05-15T11:18:42.235420+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "site:huggingface.co/datasets/lerobot libero"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_libero-benchmark_20260515T111137",
  "tool": "WebSearch",
  "tool_args": {
    "query": "site:huggingface.co/datasets/lerobot libero"
  }
}
```

</details>

---

### Tool call

_source line 84 · 2026-05-15T11:18:42.235572+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "site:huggingface.co/datasets/physical-intelligence/libero lerobot"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_libero-benchmark_20260515T111137",
  "tool": "WebSearch",
  "tool_args": {
    "query": "site:huggingface.co/datasets/physical-intelligence/libero lerobot"
  }
}
```

</details>

---

### Tool result

_source line 85 · 2026-05-15T11:18:42.235697+00:00_

# Domain Randomization in robosuite

Based on the documentation, robosuite provides three primary `Modder` classes for visual domain randomization:

## Visual Modders

**CameraModder**: Handles camera parameters including field of view and positioning adjustments.

**TextureModder**: Controls the appearance of simulation objects through texture and material property modifications.

**LightingModder**: Manages lighting environment by adjusting light source characteristics and their spatial placement.

The documentation notes that these tools enable users to either "directly override default simulation settings, or to randomize their respective properties mid-sim."

## Dynamics Randomization

The `DynamicsModder` class addresses physics parameter variation across four categories:

**Global Parameters** (Opt): density and viscosity of the medium

**Body Parameters**: position, quaternion orientation, inertia components, and mass

**Geom Parameters**: friction coefficients (sliding, torsional, rolling), contact solver values (solref), and impedance settings (solimp)

**Joint Parameters**: stiffness, friction loss, damping, and armature values

## API Usage Pattern

The basic workflow involves creating the modder instance, calling `.mod()` to adjust parameters, then invoking `.update()` to propagate changes into the simulation. The documentation includes a code example demonstrating modification of cube mass and friction values, followed by restoration of defaults.

The system includes "sanity checks to prevent presumably undesired / non-sensical behavior" such as preventing damping additions to free joints.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_libero-benchmark_20260515T111137",
  "tool": "WebFetch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool call

_source line 86 · 2026-05-15T11:18:42.235837+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://huggingface.co/datasets/lerobot/libero_10_image",
  "prompt": "Extract dataset card info: name, size, episodes, tasks, features, format. Include all metadata."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_libero-benchmark_20260515T111137",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://huggingface.co/datasets/lerobot/libero_10_image",
    "prompt": "Extract dataset card info: name, size, episodes, tasks, features, format. Include all metadata."
  }
}
```

</details>

---

### Tool result

_source line 87 · 2026-05-15T11:18:42.235959+00:00_

# Visual Property Randomization in Robosuite

## LightingModder

The LightingModder class enables domain randomization for light sources. Key parameters include:

**Modifiable Properties:**
- Position (with `position_perturbation_size=0.1`)
- Direction (with `direction_perturbation_size=0.35`)
- Specular attribute (with `specular_perturbation_size=0.1`)
- Ambient attribute (with `ambient_perturbation_size=0.1`)
- Diffuse attribute (with `diffuse_perturbation_size=0.1`)
- Active status (on/off)

**Key Methods:** `randomize()`, `save_defaults()`, `restore_defaults()`, and individual getters/setters for each property.

## CameraModder

This modder adjusts camera viewing parameters during simulation. Configurable aspects are:

**Modifiable Properties:**
- Position (with `position_perturbation_size=0.01`)
- Rotation/orientation via quaternions (with `rotation_perturbation_size=0.087`)
- Field of view (fovy) in degrees (with `fovy_perturbation_size=5.0`)

**Key Methods:** `randomize()`, `_randomize_position()`, `_randomize_rotation()`, `_randomize_fovy()`, plus accessor methods for position, quaternion orientation, and fovy values.

## TextureModder

This comprehensive modder handles surface appearance changes. As noted, "in order for the textures to take full effect, you'll need to set the rgba values for all materials to [1, 1, 1, 1]."

**Modifiable Properties:**
- RGB colors (with `local_rgb_interpolation=0.1`)
- Texture patterns: RGB, checker, noise, gradient
- Material properties: reflectance, shininess, specular (with `local_material_interpolation=0.2`)
- Skybox textures (when `randomize_skybox=True`)

**Key Methods:** `randomize()`, `rand_rgb()`, `rand_checker()`, `rand_gradient()`, `rand_noise()`, plus material and texture management functions.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_libero-benchmark_20260515T111137",
  "tool": "WebFetch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 88 · 2026-05-15T11:18:42.236096+00:00_

Web search results for query: "site:huggingface.co/datasets/physical-intelligence/libero lerobot"

Links: [{"title":"physical-intelligence/libero · Datasets at Hugging Face","url":"https://huggingface.co/datasets/physical-intelligence/libero"},{"title":"README.md · physical-intelligence/libero at main","url":"https://huggingface.co/datasets/physical-intelligence/libero/blob/main/README.md"},{"title":"physical-intelligence/libero at main","url":"https://huggingface.co/datasets/physical-intelligence/libero/tree/main"},{"title":"physical-intelligence/libero · Description of the dataset features","url":"https://huggingface.co/datasets/physical-intelligence/libero/discussions/1"}]

I found results for the physical-intelligence/libero dataset on Hugging Face. Here's what the search revealed:

The libero dataset was created using LeRobot and combines four individual Libero datasets: Libero-Spatial, Libero-Object, Libero-Goal and Libero-10, all converted into LeRobot format. The dataset is available at https://huggingface.co/datasets/physical-intelligence/libero and has a size of approximately 34.9 GB.

The dataset is licensed under CC-BY-4.0 and is categorized as a robotics dataset with tags for LeRobot, libero, panda, and rlds. The data is stored in Parquet format.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_libero-benchmark_20260515T111137",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 89 · 2026-05-15T11:18:42.236234+00:00_

Web search results for query: "site:huggingface.co/datasets/lerobot libero"

Links: [{"title":"lerobot/libero · Datasets at Hugging Face","url":"https://huggingface.co/datasets/lerobot/libero"},{"title":"lerobot/libero_object_image · Datasets at Hugging Face","url":"https://huggingface.co/datasets/lerobot/libero_object_image"},{"title":"lerobot/libero_10_image · Datasets at Hugging Face","url":"https://huggingface.co/datasets/lerobot/libero_10_image"},{"title":"lerobot/libero_spatial_image · Datasets at Hugging Face","url":"https://huggingface.co/datasets/lerobot/libero_spatial_image"},{"title":"Commits · lerobot/libero_goal_image","url":"https://huggingface.co/datasets/lerobot/libero_goal_image/commits/main"},{"title":"lerobot/xarm_lift_medium at main","url":"https://huggingface.co/datasets/lerobot/xarm_lift_medium/tree/main"},{"title":"lerobot/config_examples · add_configs","url":"https://huggingface.co/datasets/lerobot/config_examples/discussions/1/files"},{"title":"lerobot/droid_1.0.1 at main","url":"https://huggingface.co/datasets/lerobot/droid_1.0.1/tree/main"},{"title":"lerobot/example_hil_serl_dataset · Datasets at Hugging Face","url":"https://huggingface.co/datasets/lerobot/example_hil_serl_dataset"},{"title":"lerobot/austin_sirius_dataset · Datasets at Hugging Face","url":"https://huggingface.co/datasets/lerobot/austin_sirius_dataset"}]

The search results show that there are several LIBERO-related datasets available on Hugging Face under the LeRobot organization. The search found:

1. **lerobot/libero** - The main LIBERO dataset
2. **lerobot/libero_object_image** - An image variant of the LIBERO dataset
3. **lerobot/libero_10_image** - Another image-based variant (last updated August 3, 2025)
4. **lerobot/libero_spatial_image** - A spatial image variant (last updated August 21, 2025)
5. **lerobot/libero_goal_image** - A goal-based image variant (last updated February 27, 2025)

All of these datasets are hosted on the Hugging Face platform as part of the L
…[truncated 250 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_libero-benchmark_20260515T111137",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 90 · 2026-05-15T11:18:42.236391+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://raw.githubusercontent.com/Lifelong-Robot-Learning/LIBERO/master/libero/lifelong/main.py",
  "prompt": "Extract ALL details: default configuration values for observation space (image size, obs keys like agentview_image, robot0_eye_in_hand_image, robot0_joint_pos, robot0_gripper_qpos, etc.), action dimensions, training parameters, evaluation settings (number of eval episodes, max steps), and any other technical specifications."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_libero-benchmark_20260515T111137",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://raw.githubusercontent.com/Lifelong-Robot-Learning/LIBERO/master/libero/lifelong/main.py",
    "prompt": "Extract ALL details: default configuration values for observation space (image size, obs keys like agentview_image, robot0_eye_in_hand_image, robot0_joint_pos, robot0_gripper_qpos, etc.), action dimensions, training parameters, evaluation settings (number of eval episodes, max steps), and any other technical specifications."
  }
}
```

</details>

---

### Tool call

_source line 91 · 2026-05-15T11:18:42.236549+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://raw.githubusercontent.com/Lifelong-Robot-Learning/LIBERO/master/libero/lifelong/algos/base.py",
  "prompt": "Extract details about: observation processing (what obs keys are used, dimensions), action space dimensions, policy output format, evaluation rollout procedure, success rate computation, and any other technical details about how the agent interacts with the environment."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_libero-benchmark_20260515T111137",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://raw.githubusercontent.com/Lifelong-Robot-Learning/LIBERO/master/libero/lifelong/algos/base.py",
    "prompt": "Extract details about: observation processing (what obs keys are used, dimensions), action space dimensions, policy output format, evaluation rollout procedure, success rate computation, and any other technical details about how the agent interacts with the environment."
  }
}
```

</details>

---

### Tool call

_source line 92 · 2026-05-15T11:18:42.236685+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "LIBERO benchmark observation space action space 7-dimensional joint position gripper robosuite hdf5 format"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_libero-benchmark_20260515T111137",
  "tool": "WebSearch",
  "tool_args": {
    "query": "LIBERO benchmark observation space action space 7-dimensional joint position gripper robosuite hdf5 format"
  }
}
```

</details>

---

### Tool result

_source line 93 · 2026-05-15T11:18:42.236825+00:00_

# LIBERO-plus Dataset Details

## Overview
LIBERO-plus is a comprehensive robustness benchmark for Vision-Language-Action (VLA) models containing **10,030 tasks** across 7 perturbation dimensions. It extends the original LIBERO benchmark with systematic robustness evaluation.

## File Structure

After extraction, the directory structure should be:

```
LIBERO-plus/
└── libero/
    └── libero/
        └── assets/
            ├── articulated_objects/
            ├── new_objects/
            ├── scenes/
            ├── stable_hope_objects/
            ├── stable_scanned_objects/
            ├── textures/
            ├── turbosquid_objects/
            ├── serving_region.xml
            ├── wall_frames.stl
            └── wall.xml
```

## Installation Instructions

```bash
# Clone the repository
git clone https://github.com/sylvestf/LIBERO-plus.git
cd LIBERO-plus

# Install system dependencies
apt install libexpat1
apt install libfontconfig1-dev
apt install libpython3-stdlib
apt-get install libmagickwand-dev

# Install Python package
pip install -e .
pip install -r extra_requirements.txt
```

**Note:** If you have the original LIBERO installed, uninstall it first. Update the config path at `/root/.libero/config.yaml`.

## Dataset Contents

### 7 Perturbation Dimensions

1. **Objects Layout** - Confounding objects and target object displacement
2. **Camera Viewpoints** - Position, orientation, and field-of-view changes
3. **Robot Initial States** - Manipulator initial pose variations
4. **Language Instructions** - LLM-based instruction rewriting
5. **Light Conditions** - Intensity, direction, color, and shadow variations
6. **Background Textures** - Scene and surface appearance changes
7. **Sensor Noise** - Photometric distortions and image degradation

### Total Size
**6.4 GB** with 1,591 downloads

## Training Data

**Location:** [LIBERO-plus RLDS Dataset](https://huggingface.co/datasets/Sylvest/libero_plus_rlds/tree/main)

**Pre-trained Model:** [OpenVLA-7B-OFT Fine-t
…[truncated 1458 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_libero-benchmark_20260515T111137",
  "tool": "WebFetch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 94 · 2026-05-15T11:18:42.236974+00:00_

# Configuration Details Analysis

Based on the provided code, I cannot extract the specific default values you requested because **this script does not contain them**. Here's what I found:

## What the Code Does
This is a lifelong learning training orchestrator that loads configuration from external sources via Hydra: `"@hydra.main(config_path="../configs", config_name="config", version_base=None)"`

## Configuration Sources (Not Shown)
The actual defaults are defined in:
- YAML configuration files in the `../configs` directory
- The benchmark definitions loaded via `get_benchmark()`
- Dataset specifications from `get_dataset()`

## Parameters Referenced But Not Defined Here
The script *references* these config values without defining them:
- `cfg.data.obs.modality` (observation modality)
- `cfg.data.seq_len` (sequence length)
- `cfg.data.task_group_size` (grouping parameter)
- `cfg.train.n_epochs` (training epochs)
- `cfg.eval.n_eval` (evaluation episodes)
- `cfg.eval.eval_every` (evaluation frequency)
- `cfg.seed` (random seed)

## To Find Actual Specifications
You would need to examine:
1. The YAML configuration files in the `configs/` directory
2. The benchmark class implementation
3. The dataset loading module (`libero/lifelong/datasets`)

The code shows this is part of the LIBERO (Long-horizon Lifelong Robotic Learning) framework, but the technical specifications are stored elsewhere in the project structure.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_libero-benchmark_20260515T111137",
  "tool": "WebFetch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 95 · 2026-05-15T11:18:42.237110+00:00_

# LeRobot LIBERO-10 Dataset Card

## Basic Information
- **Name**: lerobot/libero_10_image
- **Organization**: LeRobot
- **License**: Apache 2.0
- **Repository**: Hugging Face Datasets

## Dataset Size & Structure
- **Total Rows**: 101,000 (101k rows)
- **Size Category**: 100K - 1M
- **Format**: Parquet (auto-converted)
- **Split**: Single training split

## Metadata

### Tasks
- **Primary Task**: Robotics
- **Task Count**: 10 tasks (indices 0-9)
- **Episodes**: 148 episodes (episode_index range: 0-147)

### Modalities
- Image (observation cameras)
- Time-series (state and action sequences)

### Features

#### Observations
- **observation.images.image**: 256×256 pixel RGB images (main camera)
- **observation.images.wrist_image**: 256×256 pixel RGB images (wrist camera)
- **observation.state**: List of 8 float values (robot state/joint positions)

#### Actions
- **action**: List of 7 float values (robot control commands)
  - Typically includes 6 continuous values + 1 discrete gripper value (-1, 0, 1)

#### Metadata
- **timestamp**: Float32 (0-45.4 range, in seconds)
- **frame_index**: Int64 (frame number within episode, 0-454)
- **episode_index**: Int64 (which episode, 0-147)
- **task_index**: Int64 (which task, 0-9)
- **index**: Int64 (global row index, 0-40.3k)

## Data Characteristics

### Sample Data Structure
```
Frame 0:
  - Timestamp: 0.0
  - State: [-0.053, 0.007, 0.678, 3.141, 0.002, -0.090, 0.039, -0.039]
  - Action: [0.016, 0, 0, 0, 0, 0, -1]
  - Episode: 0, Task: 0
```

### Action Space Pattern
- First 6 values: continuous control (typically normalized)
- Last value: discrete gripper control (-1 = open, 0 = maintain, 1 = close)

## Libraries & Tools
- **Datasets**: Hugging Face Datasets library
- **Dask**: Distributed computing support
- **Polars**: DataFrames support

## Availability
- **Viewer**: Interactive Data Studio available
- **Community**: 4 discussions/comments
- **Download**: Available via Hugging Face Hub (xet protocol supported)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_libero-benchmark_20260515T111137",
  "tool": "WebFetch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool call

_source line 96 · 2026-05-15T11:18:42.237262+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "robosuite DomainRandomizationWrapper example code camera_names randomize_color randomize_camera"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_libero-benchmark_20260515T111137",
  "tool": "WebSearch",
  "tool_args": {
    "query": "robosuite DomainRandomizationWrapper example code camera_names randomize_color randomize_camera"
  }
}
```

</details>

---

### Tool call

_source line 97 · 2026-05-15T11:18:42.237393+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "LIBERO-Plus training augmentation reuse perturbation training time data augmentation robustness"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_libero-benchmark_20260515T111137",
  "tool": "WebSearch",
  "tool_args": {
    "query": "LIBERO-Plus training augmentation reuse perturbation training time data augmentation robustness"
  }
}
```

</details>

---

### Tool call

_source line 98 · 2026-05-15T11:18:42.237538+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "github huggingface lerobot \"convert_libero\" OR \"libero\" path:lerobot/common/datasets"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_libero-benchmark_20260515T111137",
  "tool": "WebSearch",
  "tool_args": {
    "query": "github huggingface lerobot \"convert_libero\" OR \"libero\" path:lerobot/common/datasets"
  }
}
```

</details>

---

### Tool result

_source line 99 · 2026-05-15T11:18:42.237666+00:00_

# Technical Details from Code Analysis

## Observable Processing
The code does not explicitly detail observation key specifications or dimensions. It references `cfg.shape_meta` passed to the policy class, suggesting metadata defines observation structure, but specifics are abstracted away.

## Action Space
No direct action space dimensionality is specified in this file. The policy class implementation (via `get_policy_class()`) would contain this information.

## Policy Output Format
The code emphasizes loss computation: `"loss = self.policy.compute_loss(data)"`. The policy produces loss values during training but doesn't explicitly detail action output formatting.

## Evaluation Rollout Procedure
The framework uses `"evaluate_one_task_success()"` to assess performance. Key parameters include task specification, task embeddings, and task IDs. The evaluation occurs at intervals defined by `"cfg.eval.eval_every"`.

## Success Rate Computation
Success rates are computed via the evaluation function and tracked across epochs. The framework calculates confidence intervals using `"confidence_interval(success_rate, self.cfg.eval.n_eval)"`, where n_eval specifies evaluation trials.

## Learning Dynamics
The algorithm employs an "Area under Curve" metric: `"cumulated_counter"` accumulates across evaluations, with success values frozen at peak performance to compute learning efficiency.

## Additional Details
- Model checkpoints save when success improves
- Learning continues until peak performance; no explicit early stopping beyond this heuristic
- The base `Sequential` class serves as a template for lifelong learning variants via metaclass registration

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_libero-benchmark_20260515T111137",
  "tool": "WebFetch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 100 · 2026-05-15T11:18:42.237805+00:00_

Web search results for query: "LIBERO benchmark observation space action space 7-dimensional joint position gripper robosuite hdf5 format"

Links: [{"title":"LIBERO Benchmark: Vision-Language-Action in Robotics","url":"https://www.emergentmind.com/topics/libero"},{"title":"Benchmark Descriptions — RoboVerse 0.1.0 documentation","url":"https://roboverse.wiki/dataset_benchmark/tasks/descriptions"},{"title":"LIBERO Tasks: Lifelong Robotic Learning","url":"https://www.emergentmind.com/topics/libero-tasks"},{"title":"Real-World Data for LIBERO Lifelong Robot Learning | Claru","url":"https://claru.ai/benchmarks/libero"},{"title":"Robosuite Dataset: Robotic Manipulation Benchmarks","url":"https://www.emergentmind.com/topics/robosuite-dataset"},{"title":"RL with LIBERO Benchmark — RLinf documentation","url":"https://rlinf.readthedocs.io/en/latest/rst_source/examples/embodied/libero.html"},{"title":"LIBERO: Benchmarking Knowledge Transfer for Lifelong Robot Learning | OpenReview","url":"https://openreview.net/forum?id=xzEtNSuDJk"},{"title":"LIBERO: simulation benchmark for the study of lifelong robot learning | by Deepthi Karkada | Medium","url":"https://medium.com/@deepkarkada/libero-simulation-benchmark-for-the-study-of-lifelong-robot-learning-583b786a96f6"},{"title":"LIBERO · Hugging Face","url":"https://huggingface.co/docs/lerobot/libero"},{"title":"LIBERO – LIBERO","url":"https://libero-project.github.io/main.html"}]

Based on the search results, here's what I found about the LIBERO benchmark's observation space, action space, and data format:

## Action Space

LIBERO uses 7-DOF end-effector pose deltas (3D position delta, 3D orientation delta, gripper open/close) at 20 Hz control frequency on a simulated Franka Panda arm via robosuite's OSC controller.

## Data Format

Demonstrations are collected using a SpaceMouse teleoperator at 20 Hz with automatic filtering and validation pipelines, and are available as HDF5 for reproducibility. Additionally, LIBERO manages data l
…[truncated 695 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_libero-benchmark_20260515T111137",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool call

_source line 101 · 2026-05-15T11:18:42.237962+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://huggingface.co/datasets/physical-intelligence/libero",
  "prompt": "Extract the full dataset card: how this dataset was created, what raw datasets it combines, size, format, features, conversion process details. Include everything about how it maps to LeRobot format."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_libero-benchmark_20260515T111137",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://huggingface.co/datasets/physical-intelligence/libero",
    "prompt": "Extract the full dataset card: how this dataset was created, what raw datasets it combines, size, format, features, conversion process details. Include everything about how it maps to LeRobot format."
  }
}
```

</details>

---

### Tool call

_source line 102 · 2026-05-15T11:18:42.238096+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://rlinf.readthedocs.io/en/latest/rst_source/examples/embodied/libero.html",
  "prompt": "Extract ALL technical details about LIBERO: observation space dimensions and keys (agentview_image, eye_in_hand_image, joint_pos, gripper_qpos, ee_pos, ee_quat), action space dimensions and meaning, HDF5 data structure, evaluation protocol, and any other specifications."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_libero-benchmark_20260515T111137",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://rlinf.readthedocs.io/en/latest/rst_source/examples/embodied/libero.html",
    "prompt": "Extract ALL technical details about LIBERO: observation space dimensions and keys (agentview_image, eye_in_hand_image, joint_pos, gripper_qpos, ee_pos, ee_quat), action space dimensions and meaning, HDF5 data structure, evaluation protocol, and any other specifications."
  }
}
```

</details>

---

### Tool result

_source line 103 · 2026-05-15T11:18:42.238232+00:00_

Web search results for query: "robosuite DomainRandomizationWrapper example code camera_names randomize_color randomize_camera"

Links: [{"title":"Demo Showcases — robosuite 1.5 documentation","url":"https://robosuite.ai/docs/demos.html"},{"title":"robosuite/robosuite/utils/camera_utils.py at master · ARISE-Initiative/robosuite","url":"https://github.com/ARISE-Initiative/robosuite/blob/master/robosuite/utils/camera_utils.py"},{"title":"Sim-to-Real Transfer — robosuite 1.5 documentation","url":"https://robosuite.ai/docs/algorithms/sim2real.html"},{"title":"robosuite/robosuite/demos/demo_segmentation.py at master · ARISE-Initiative/robosuite","url":"https://github.com/ARISE-Initiative/robosuite/blob/master/robosuite/demos/demo_segmentation.py"},{"title":"GitHub - quantumiracle/robolite: This is a fork of Surreal Robotics Suite that enables support to domain randomization and inverse kinematics (IK). · GitHub","url":"https://github.com/quantumiracle/robolite"},{"title":"robosuite | robosuite: A Modular Simulation Framework and Benchmark for Robot Learning","url":"https://robosuite.ai/"},{"title":"robosuite/robosuite/environments/manipulation/stack.py at master · ARISE-Initiative/robosuite","url":"https://github.com/ARISE-Initiative/robosuite/blob/master/robosuite/environments/manipulation/stack.py"},{"title":"robosuite.environments.manipulation package — robosuite 1.5 documentation","url":"https://robosuite.ai/docs/source/robosuite.environments.manipulation.html"},{"title":"robosuite.utils package — robosuite 1.5 documentation","url":"https://robosuite.ai/docs/source/robosuite.utils.html"},{"title":"Environments — robosuite 1.5 documentation","url":"https://robosuite.ai/docs/modules/environments.html"}]

Based on the search results, here's what I found about the DomainRandomizationWrapper in robosuite:

## DomainRandomizationWrapper Overview

The randomization functionality focuses on visual variations, including colors, textures, and camera viewpoints.

## Example Cod
…[truncated 1470 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_libero-benchmark_20260515T111137",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 104 · 2026-05-15T11:18:42.238386+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://medium.com/@deepkarkada/libero-simulation-benchmark-for-the-study-of-lifelong-robot-learning-583b786a96f6",
  "prompt": "Extract ALL technical details about LIBERO: task suite descriptions (Spatial, Object, Goal, Long, 90), observation space, action space, data format, number of demonstrations, evaluation metrics, and any other specifications."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_libero-benchmark_20260515T111137",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://medium.com/@deepkarkada/libero-simulation-benchmark-for-the-study-of-lifelong-robot-learning-583b786a96f6",
    "prompt": "Extract ALL technical details about LIBERO: task suite descriptions (Spatial, Object, Goal, Long, 90), observation space, action space, data format, number of demonstrations, evaluation metrics, and any other specifications."
  }
}
```

</details>

---

### Tool result

_source line 105 · 2026-05-15T11:18:42.238545+00:00_

Web search results for query: "github huggingface lerobot "convert_libero" OR "libero" path:lerobot/common/datasets"

Links: [{"title":"GitHub - huggingface/lerobot-libero: A fork of the official LIBERO benchmark, extended for Hugging Face’s LeRobot integration and large-scale robotics experiments.","url":"https://github.com/huggingface/lerobot-libero"},{"title":"GitHub - huggingface/lerobot: 🤗 LeRobot: Making AI for Robotics more accessible with end-to-end learning","url":"https://github.com/huggingface/lerobot"},{"title":"openpi/examples/libero/convert_libero_data_to_lerobot.py at main · Physical-Intelligence/openpi","url":"https://github.com/Physical-Intelligence/openpi/blob/main/examples/libero/convert_libero_data_to_lerobot.py"},{"title":"https://raw.githubusercontent.com/Physical-Intelli...","url":"https://raw.githubusercontent.com/Physical-Intelligence/openpi/main/examples/libero/convert_libero_data_to_lerobot.py"},{"title":"LIBERO · Hugging Face","url":"https://huggingface.co/docs/lerobot/libero"},{"title":"lerobot/xvla-libero · Hugging Face","url":"https://huggingface.co/lerobot/xvla-libero"},{"title":"lerobot/libero_object_image · Datasets at Hugging Face","url":"https://huggingface.co/datasets/lerobot/libero_object_image"},{"title":"HuggingFaceVLA/libero · Datasets at Hugging Face","url":"https://huggingface.co/datasets/HuggingFaceVLA/libero"},{"title":"lerobot/libero · Datasets at Hugging Face","url":"https://huggingface.co/datasets/lerobot/libero/viewer/default/train"},{"title":"README.md · physical-intelligence/libero at main","url":"https://huggingface.co/datasets/physical-intelligence/libero/blob/main/README.md"}]

Based on the web search results, I found relevant information about LIBERO dataset conversion and LeRobot integration:

## Key Findings

LeRobot supports standard benchmarks like LIBERO, which is a benchmark for studying robot learning.

### LIBERO Dataset Resources

The dataset combines four individual Libero datasets: Libero-Spatial, Lib
…[truncated 918 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_libero-benchmark_20260515T111137",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool call

_source line 106 · 2026-05-15T11:18:42.238712+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://raw.githubusercontent.com/Lifelong-Robot-Learning/LIBERO/master/libero/lifelong/configs/config.yaml",
  "prompt": "Extract ALL configuration values: observation keys, image dimensions, action dimensions, evaluation settings (n_eval, max_steps), training parameters, and any other specifications."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_libero-benchmark_20260515T111137",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://raw.githubusercontent.com/Lifelong-Robot-Learning/LIBERO/master/libero/lifelong/configs/config.yaml",
    "prompt": "Extract ALL configuration values: observation keys, image dimensions, action dimensions, evaluation settings (n_eval, max_steps), training parameters, and any other specifications."
  }
}
```

</details>

---

### Tool result

_source line 107 · 2026-05-15T11:18:42.238866+00:00_

Web search results for query: "LIBERO-Plus training augmentation reuse perturbation training time data augmentation robustness"

Links: [{"title":"LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-Action Models","url":"https://sylvestf.github.io/LIBERO-plus/"},{"title":"LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-Action Models","url":"https://arxiv.org/html/2510.13626v1"},{"title":"LIBERO-X: Robustness Litmus for Vision-Language-Action Models","url":"https://arxiv.org/html/2602.06556v1"},{"title":"Paper page - LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-Action Models","url":"https://huggingface.co/papers/2510.13626"},{"title":"GitHub - sylvestf/LIBERO-plus: Official repository of LIBERO-plus, a generalized benchmark for in-depth robustness analysis of vision-language-action models. · GitHub","url":"https://github.com/sylvestf/LIBERO-plus"},{"title":"OpenMOSS LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-","url":"https://arxiv.org/pdf/2510.13626"},{"title":"LIBERO-plus · Hugging Face","url":"https://huggingface.co/docs/lerobot/main/libero_plus"},{"title":"[2510.13626] LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-Action Models","url":"https://arxiv.org/abs/2510.13626"},{"title":"RL with LIBERO-Pro & LIBERO-Plus Benchmark — RLinf documentation","url":"https://rlinf.readthedocs.io/en/latest/rst_source/examples/embodied/liberoplus_pro.html"},{"title":"LIBERO Benchmark: Vision-Language-Action in Robotics","url":"https://www.emergentmind.com/topics/libero"}]

I've found comprehensive information about LIBERO-Plus and related research. Here's what the search reveals:

## LIBERO-Plus Overview

LIBERO-Plus is an extensive benchmark with 10,030 tasks spanning seven perturbation dimensions, with a diverse training dataset containing over 20,000 successful trajectories collected under systematically varied conditions.

## Training Data Augmentation and Diversity

Training strategies that emphasize divers
…[truncated 1603 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_libero-benchmark_20260515T111137",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 108 · 2026-05-15T11:18:42.239005+00:00_

Request failed with status code 404

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_libero-benchmark_20260515T111137",
  "tool": "WebFetch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 109 · 2026-05-15T11:18:42.239146+00:00_

# LIBERO Technical Specifications from Documentation

Based on the provided documentation, here are the available technical details:

## Observation Space
The documentation specifies that observations consist of **"RGB images (typical resolutions 128 × 128 or 224 × 224) captured by off-screen cameras placed around the workspace."** The data structure indicates **"Images: RGB tensors `[batch_size, 224, 224, 3]`"**

However, the specific observation keys mentioned in your query (agentview_image, eye_in_hand_image, joint_pos, gripper_qpos, ee_pos, ee_quat) are **not detailed in this document**.

## Action Space
The documentation clearly defines the action output as **"7-dimensional continuous actions"** consisting of:
- 3D end-effector position control (x, y, z)
- 3D rotation control (roll, pitch, yaw)  
- Gripper control (open/close)

Actions are described as **"Normalized continuous values converted to discrete tokens."**

## Task Format & Rewards
Task descriptions follow this structure: **"In: What action should the robot take to [task_description]? Out:"**

The reward mechanism involves **"Step-level rewards based on task completion"** with sparse rewards in practice—**"0 for all intermediate steps and 1 only at successful termination."**

## HDF5 Data Structure & Evaluation Protocol
The documentation does **not provide HDF5 structure details or comprehensive evaluation protocols** beyond noting that evaluation occurs across 500-6,500 environment instances depending on the LIBERO suite.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_libero-benchmark_20260515T111137",
  "tool": "WebFetch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool call

_source line 110 · 2026-05-15T11:18:42.239297+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://robosuite.ai/docs/demos.html",
  "prompt": "Extract the full domain randomization demo details: DomainRandomizationWrapper parameters, how to use it, what it randomizes (camera, texture, lighting, dynamics), code examples, and all configurable parameters with their defaults."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_libero-benchmark_20260515T111137",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://robosuite.ai/docs/demos.html",
    "prompt": "Extract the full domain randomization demo details: DomainRandomizationWrapper parameters, how to use it, what it randomizes (camera, texture, lighting, dynamics), code examples, and all configurable parameters with their defaults."
  }
}
```

</details>

---

### Tool result

_source line 111 · 2026-05-15T11:18:42.239425+00:00_

# LIBERO Technical Specifications

## Task Suite Descriptions

LIBERO contains **130 language-conditioned manipulation tasks** organized into four groups:

- **LIBERO-OBJECT**: "Tasks with distribution shifts in object types"
- **LIBERO-SPATIAL**: "Tasks with distribution shifts in the spatial arrangement of objects"
- **LIBERO-GOAL**: "Tasks with distribution shifts in the task goals"
- **LIBERO-100**: "Tasks with a combination of the above three"

## Task Generation

Tasks are procedurally generated using:
- **Templated actions**: "pick, place, put on, take off etc"
- **Behavioral templates**: Extracted from the Ego4D human activity dataset, including "open, put, turn on"
- **PDDL configuration files** specifying: (1) objects and layouts, (2) initial object configurations, (3) goal states

## Observation & Action Space

The document does **not specify** observation or action space dimensions.

## Demonstrations

- **50 episodes** of high-quality human demonstrations per task used for behavior cloning training

## Evaluation Metrics

Three primary metrics are employed:

1. **FWT (Forward Transfer)**: Success rate improvement on new tasks after sequential training
2. **NBT (Negative Backward Transfer)**: Performance drop on earlier tasks after learning new ones (catastrophic forgetting measure)
3. **AUC**: Overall performance integrating both FWT and NBT

## Simulation Environment

- **MuJoCo-based** simulation framework
- Expandable benchmark supporting custom procedural generation pipelines

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_libero-benchmark_20260515T111137",
  "tool": "WebFetch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool call

_source line 112 · 2026-05-15T11:18:42.239587+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://huggingface.co/docs/lerobot/main/libero_plus",
  "prompt": "Extract all details about LIBERO-plus integration with LeRobot: setup instructions, how to use the dataset, training commands, and any code examples for using LIBERO-plus perturbations during training."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_libero-benchmark_20260515T111137",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://huggingface.co/docs/lerobot/main/libero_plus",
    "prompt": "Extract all details about LIBERO-plus integration with LeRobot: setup instructions, how to use the dataset, training commands, and any code examples for using LIBERO-plus perturbations during training."
  }
}
```

</details>

---

### Tool result

_source line 113 · 2026-05-15T11:18:42.239736+00:00_

# LIBERO-plus

LIBERO-plus is a **robustness benchmark** for Vision-Language-Action (VLA) models built on top of [LIBERO](./libero). It systematically stress-tests policies by applying **seven independent perturbation dimensions** to the original LIBERO task set, exposing failure modes that standard benchmarks miss.

- Paper: [In-depth Robustness Analysis of Vision-Language-Action Models](https://arxiv.org/abs/2510.13626)
- GitHub: [sylvestf/LIBERO-plus](https://github.com/sylvestf/LIBERO-plus)
- Dataset: [lerobot/libero_plus](https://huggingface.co/datasets/lerobot/libero_plus)

![An overview of the LIBERO-plus benchmark perturbation dimensions](https://github.com/sylvestf/LIBERO-plus/raw/main/static/images/libero-plus.jpg)

## Perturbation dimensions

LIBERO-plus creates ~10 000 task variants by perturbing each original LIBERO task along these axes:

| Dimension             | What changes                                          |
| --------------------- | ----------------------------------------------------- |
| Objects layout        | Target position, presence of confounding objects      |
| Camera viewpoints     | Camera position, orientation, field-of-view           |
| Robot initial states  | Manipulator start pose                                |
| Language instructions | LLM-rewritten task description (paraphrase / synonym) |
| Light conditions      | Intensity, direction, color, shadow                   |
| Background textures   | Scene surface and object appearance                   |
| Sensor noise          | Photometric distortions and image degradation         |

## Available task suites

LIBERO-plus covers the same five suites as LIBERO:

| Suite          | CLI name         | Tasks | Max steps | Description                                        |
| -------------- | ---------------- | ----- | --------- | -------------------------------------------------- |
| LIBERO-Spatial | `libero_spatial` | 10    | 280       | Tasks requiring reasoning about spatia
…[truncated 5193 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_libero-benchmark_20260515T111137",
  "tool": "WebFetch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 114 · 2026-05-15T11:18:42.239894+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://raw.githubusercontent.com/Lifelong-Robot-Learning/LIBERO/master/libero/configs/config.yaml",
  "prompt": "Extract ALL configuration values: observation keys, image dimensions, action dimensions, evaluation settings, training parameters."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_libero-benchmark_20260515T111137",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://raw.githubusercontent.com/Lifelong-Robot-Learning/LIBERO/master/libero/configs/config.yaml",
    "prompt": "Extract ALL configuration values: observation keys, image dimensions, action dimensions, evaluation settings, training parameters."
  }
}
```

</details>

---

### Tool call

_source line 115 · 2026-05-15T11:18:42.240031+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://raw.githubusercontent.com/Lifelong-Robot-Learning/LIBERO/master/libero/lifelong/utils.py",
  "prompt": "Extract details about observation space processing, action space, evaluation rollout (evaluate_one_task_success function), success rate computation, number of evaluation episodes, max steps, and any other technical details."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_libero-benchmark_20260515T111137",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://raw.githubusercontent.com/Lifelong-Robot-Learning/LIBERO/master/libero/lifelong/utils.py",
    "prompt": "Extract details about observation space processing, action space, evaluation rollout (evaluate_one_task_success function), success rate computation, number of evaluation episodes, max steps, and any other technical details."
  }
}
```

</details>

---

### Tool result

_source line 116 · 2026-05-15T11:18:42.240170+00:00_

# LIBERO Dataset Card

## Overview
The LIBERO dataset is a robotic manipulation dataset published by Physical Intelligence and hosted on Hugging Face. It contains demonstration data for learning robot control policies.

## Dataset Statistics
- **Size**: 273,000 rows
- **Format**: Parquet (auto-converted from original format)
- **Task Categories**: Robotics
- **Modalities**: Image, Time-series
- **License**: CC-BY-4.0
- **ArXiv Reference**: 2306.03310

## Data Structure

### Raw Format
The dataset is organized hierarchically:
- **Subsets**: 1 (default)
- **Splits**: 1 (train)
- **Episodes**: 147 episodes
- **Total Frames**: ~273k frames

### Features

The dataset contains the following fields per frame:

| Field | Type | Description |
|-------|------|-------------|
| `image` | Image (256×256px) | RGB observation from main camera |
| `wrist_image` | Image (256×256px) | RGB observation from wrist-mounted camera |
| `state` | List (8 floats) | Robot joint positions/states |
| `actions` | List (7 floats) | Robot action command (likely 6-DOF + gripper) |
| `timestamp` | float32 | Frame timestamp |
| `frame_index` | int64 | Frame number within episode (0-454) |
| `episode_index` | int64 | Episode identifier (0-146) |
| `index` | int64 | Global row index (0-40.1k) |
| `task_index` | int64 | Task identifier (0-9, suggesting 10 tasks) |

### Data Example

```python
# Frame sample structure
{
  "image": <256×256 RGB image>,
  "wrist_image": <256×256 RGB wrist view>,
  "state": [-0.0534, 0.0070, 0.6783, 3.1408, 0.0018, -0.0899, 0.0388, -0.0388],
  "actions": [0.0161, 0, 0, 0, 0, 0, -1],
  "timestamp": 45.4,
  "frame_index": 0,
  "episode_index": 0,
  "task_index": 0
}
```

## Robot Hardware
- **Robot**: Franka Panda (indicated by "panda" tag)
- **State Dimension**: 8 (7 joint angles + gripper state)
- **Action Dimension**: 7 (6-DOF end-effector control + gripper command)

## LeRobot Integration

### Format Compatibility
The dataset includes tags for **LeRobot** integration:
- S
…[truncated 2034 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_libero-benchmark_20260515T111137",
  "tool": "WebFetch",
  "elapsed_ms": 2
}
```

</details>

---

### Tool result

_source line 117 · 2026-05-15T11:18:42.240316+00:00_

# Domain Randomization Demo Details

Based on the provided documentation, the information available about the Domain Randomization demo is limited:

## What the Documentation States

The `demo_domain_randomization.py` script is described as showcasing "domain randomization functionality." According to the content, this feature "can be easily enabled by wrapping an environment with the DomainRandomizationWrapper."

The documentation specifies that **"the randomization functionality focuses on visual variations, including colors, textures, and camera viewpoints."**

## Limitations of Available Information

Unfortunately, the provided webpage content does not include:
- Specific parameters for the DomainRandomizationWrapper
- Code examples showing implementation
- Default values for any configurable settings
- Details on dynamics randomization (though it mentions visual variations only)
- Detailed usage instructions beyond wrapping an environment

## Recommendation

To obtain comprehensive details about DomainRandomizationWrapper parameters, code examples, and all configurable options, you would need to:
1. Consult the full robosuite source code repository
2. Review the `robosuite.wrappers` module documentation
3. Examine the actual `demo_domain_randomization.py` script in the [robosuite GitHub repository](https://github.com/ARISE-Initiative/robosuite)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_libero-benchmark_20260515T111137",
  "tool": "WebFetch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool call

_source line 118 · 2026-05-15T11:18:42.240457+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "LIBERO robot benchmark \"agentview\" \"eye_in_hand\" observation keys joint_pos action 7 dimensions hdf5 demo structure"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_libero-benchmark_20260515T111137",
  "tool": "WebSearch",
  "tool_args": {
    "query": "LIBERO robot benchmark \"agentview\" \"eye_in_hand\" observation keys joint_pos action 7 dimensions hdf5 demo structure"
  }
}
```

</details>

---

### Tool result

_source line 119 · 2026-05-15T11:18:42.240608+00:00_

# Configuration Extraction

Based on the provided YAML configuration file, here are the extracted values:

## Core Settings
- **Seed**: 10000
- **Device**: "cuda"
- **Benchmark**: "LIBERO_SPATIAL"
- **Task Embedding Format**: "bert"
- **Task Embedding Offset**: 1

## Flags & Paths
- **Weights & Biases Logging**: Disabled (use_wandb: false)
- **Pretraining**: Disabled (pretrain: false)
- **Load Previous Model**: false
- **Data Folder**: Uses default path (folder: null)
- **BDDL Folder**: Uses default path (bddl_folder: null)
- **Initial States Folder**: Uses default path (init_states_folder: null)

## Configuration References
The file references external configuration modules through defaults:
- Data configuration (data: default)
- Policy: BC Transformer
- Training configuration (train: default)
- Evaluation configuration (eval: default)
- Lifelong learning: base variant
- Test configuration: null (not specified)

## Notable Gaps
The provided excerpt does not contain **observation keys, image dimensions, or action dimensions**—these are likely defined in the referenced configuration modules (data/default, policy/bc_transformer_policy, train/default, eval/default).

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_libero-benchmark_20260515T111137",
  "tool": "WebFetch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 120 · 2026-05-15T11:18:42.240748+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__append_idea",
  "max_results": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_libero-benchmark_20260515T111137",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__append_idea",
    "max_results": "1"
  }
}
```

</details>

---

### Tool result

_source line 121 · 2026-05-15T11:18:42.240865+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_libero-benchmark_20260515T111137",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 122 · 2026-05-15T11:18:42.240988+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://github.com/ARISE-Initiative/robosuite/blob/master/robosuite/wrappers/domain_randomization_wrapper.py",
  "prompt": "Extract the complete DomainRandomizationWrapper class definition including all constructor parameters, their defaults, and descriptions. Include the full docstring and all randomization-related parameters."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_libero-benchmark_20260515T111137",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://github.com/ARISE-Initiative/robosuite/blob/master/robosuite/wrappers/domain_randomization_wrapper.py",
    "prompt": "Extract the complete DomainRandomizationWrapper class definition including all constructor parameters, their defaults, and descriptions. Include the full docstring and all randomization-related parameters."
  }
}
```

</details>

---

### Tool result

_source line 123 · 2026-05-15T11:18:42.241117+00:00_

# Technical Details Extraction

Based on the provided code, here are the key technical details:

## Observation & Action Space
No explicit observation or action space definitions are present in this code snippet. The code focuses on utility functions rather than environment specifications.

## Evaluation Details
The code does not contain an `evaluate_one_task_success` function. There are no parameters for:
- Success rate computation methods
- Number of evaluation episodes
- Maximum evaluation steps

## Available Functions

**Data Loading**: The `get_train_test_loader` function splits datasets using a "train_ratio parameter, creating separate DataLoaders for training and testing phases with configurable batch sizes.

**Model Checkpointing**: The `torch_save_model` function preserves "state_dict, cfg, and previous_masks" in a checkpoint file, while `torch_load_model` retrieves these components.

**Computational Analysis**: A `compute_flops` function calculates model efficiency by measuring "macs, params" using the THOP profiler library.

**Task Embedding**: The `get_task_embs` function generates task representations from text descriptions using multiple transformer architectures (BERT, GPT-2, CLIP, RoBERTa).

## Missing Information
This utility module lacks evaluation-specific implementations. Additional files would be needed to identify rollout procedures, success metrics, and episode configurations.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_libero-benchmark_20260515T111137",
  "tool": "WebFetch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 124 · 2026-05-15T11:18:42.241256+00:00_

Web search results for query: "LIBERO robot benchmark "agentview" "eye_in_hand" observation keys joint_pos action 7 dimensions hdf5 demo structure"

Links: [{"title":"LIBERO · Hugging Face","url":"https://huggingface.co/docs/lerobot/libero"},{"title":"Libero - LeRobot","url":"https://www.mintlify.com/huggingface/lerobot/simulation/libero"},{"title":"openvla/experiments/robot/libero/regenerate_libero_dataset.py at main · openvla/openvla","url":"https://github.com/openvla/openvla/blob/main/experiments/robot/libero/regenerate_libero_dataset.py"},{"title":"LIBERO Benchmark: Vision-Language-Action in Robotics","url":"https://www.emergentmind.com/topics/libero"},{"title":"libero-mem/LIBERO-Mem · Datasets at Hugging Face","url":"https://huggingface.co/datasets/libero-mem/LIBERO-Mem"},{"title":"robosuite Datasets — robomimic 0.5 documentation","url":"https://robomimic.github.io/docs/datasets/robosuite.html"},{"title":"nvidia/LIBERO-Cosmos-Policy · Datasets at Hugging Face","url":"https://huggingface.co/datasets/nvidia/LIBERO-Cosmos-Policy"},{"title":"Real-World Data for LIBERO Lifelong Robot Learning | Claru","url":"https://claru.ai/benchmarks/libero"},{"title":"Dataset Contents and Visualization — robomimic 0.5 documentation","url":"https://robomimic.github.io/docs/tutorials/dataset_contents.html"},{"title":"Robot LIBERO 数据集 | LIAO JIAYI Blog","url":"https://www.liaojiayi.com/blog/robot-libero"}]

I found relevant information about the LIBERO robot benchmark with details about the HDF5 data structure and observation keys.

## LIBERO Benchmark Data Structure

Based on the search results, here's what I found about the LIBERO benchmark:

### HDF5 Demo Structure

LIBERO HDF5 files contain data organized as: actions (T, 7), dones (T,), and obs/ containing agentview_rgb, agentview_depth, agentview_seg, eye_in_hand_rgb, eye_in_hand_depth, eye_in_hand_seg, gripper_states, and joint_states.

### Camera Observations

The benchmark supports agentview_image and robot0_eye_in_hand_imag
…[truncated 680 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_libero-benchmark_20260515T111137",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 125 · 2026-05-15T11:18:42.241400+00:00_

# DomainRandomizationWrapper Class Definition

## Class Overview
The `DomainRandomizationWrapper` is designed to "allow for domain randomization mid-simulation" in robosuite environments.

## Constructor Parameters

**Core Parameters:**
- `env` (MujocoEnv): The environment being wrapped
- `seed` (int, optional): Used to create isolated `np.random.RandomState` instance

**Randomization Toggles:**
- `randomize_color` (bool, default=True): Controls geom and texture color randomization
- `randomize_camera` (bool, default=True): Controls camera location and parameter changes
- `randomize_lighting` (bool, default=True): Controls light location and property modifications
- `randomize_dynamics` (bool, default=True): Controls physics parameter randomization

**Configuration Dictionaries:**
- `color_randomization_args`: Includes geom names, local color sampling, material properties, texture variations, and skybox settings
- `camera_randomization_args`: Includes camera names, position/rotation/fovy randomization with perturbation sizes
- `lighting_randomization_args`: Includes light names and randomization flags for position, direction, specular, ambient, and diffuse properties
- `dynamics_randomization_args`: Includes body, geom, and joint parameters with density, viscosity, friction, and inertia controls

**Execution Parameters:**
- `randomize_on_reset` (bool, default=True): Applies randomization at episode reset
- `randomize_every_n_steps` (int, default=1): Sets randomization frequency during steps

## Key Methods
- `reset()`: Restores defaults, resets environment, saves parameters, applies randomization if enabled
- `step()`: Calls step randomization before delegating to superclass
- `randomize_domain()`: Executes randomization across all active modders
- `save_default_domain()`: Preserves current simulation parameters
- `restore_default_domain()`: Reverts to saved parameters

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_libero-benchmark_20260515T111137",
  "tool": "WebFetch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 126 · 2026-05-15T11:18:42.241561+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://huggingface.co/docs/lerobot/libero",
  "prompt": "Extract ALL technical details about LIBERO: task suites (Spatial, Object, Goal, Long, 90), observation keys and dimensions, action dimensions, HDF5 structure, data download, evaluation protocol, number of demos per task, and any exact specifications."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_libero-benchmark_20260515T111137",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://huggingface.co/docs/lerobot/libero",
    "prompt": "Extract ALL technical details about LIBERO: task suites (Spatial, Object, Goal, Long, 90), observation keys and dimensions, action dimensions, HDF5 structure, data download, evaluation protocol, number of demos per task, and any exact specifications."
  }
}
```

</details>

---

### Tool result

_source line 127 · 2026-05-15T11:18:42.241708+00:00_

# LIBERO

LIBERO is a benchmark designed to study **lifelong robot learning** — the idea that robots need to keep learning and adapting with their users over time, not just be pretrained once. It provides a set of standardized manipulation tasks that focus on **knowledge transfer**: how well a robot can apply what it has already learned to new situations. By evaluating on LIBERO, different algorithms can be compared fairly and researchers can build on each other's work.

- Paper: [Benchmarking Knowledge Transfer for Lifelong Robot Learning](https://arxiv.org/abs/2306.03310)
- GitHub: [Lifelong-Robot-Learning/LIBERO](https://github.com/Lifelong-Robot-Learning/LIBERO)
- Project website: [libero-project.github.io](https://libero-project.github.io)

![An overview of the LIBERO benchmark](https://libero-project.github.io/assets/img/libero/fig1.png)

## Available tasks

LIBERO includes **five task suites** covering **130 tasks**, ranging from simple object manipulations to complex multi-step scenarios:

| Suite          | CLI name         | Tasks | Description                                        |
| -------------- | ---------------- | ----- | -------------------------------------------------- |
| LIBERO-Spatial | `libero_spatial` | 10    | Tasks requiring reasoning about spatial relations  |
| LIBERO-Object  | `libero_object`  | 10    | Tasks centered on manipulating different objects   |
| LIBERO-Goal    | `libero_goal`    | 10    | Goal-conditioned tasks with changing targets       |
| LIBERO-90      | `libero_90`      | 90    | Short-horizon tasks from the LIBERO-100 collection |
| LIBERO-Long    | `libero_10`      | 10    | Long-horizon tasks from the LIBERO-100 collection  |

## Installation

After following the LeRobot installation instructions:

```bash
pip install -e ".[libero]"
```

LIBERO requires Linux (`sys_platform == 'linux'`). LeRobot uses MuJoCo for simulation — set the rendering backend before training or evaluation:

```bash
export MUJOCO_GL=egl  # fo
…[truncated 4883 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_libero-benchmark_20260515T111137",
  "tool": "WebFetch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 128 · 2026-05-15T11:18:42.241865+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://github.com/openvla/openvla/blob/main/experiments/robot/libero/regenerate_libero_dataset.py",
  "prompt": "Extract ALL details about LIBERO data format: observation keys (agentview_image, eye_in_hand_image, robot0_joint_pos, robot0_gripper_qpos, ee_pos, ee_quat), action dimensions, HDF5 structure, image dimensions, and how data is loaded from LIBERO demos."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_libero-benchmark_20260515T111137",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://github.com/openvla/openvla/blob/main/experiments/robot/libero/regenerate_libero_dataset.py",
    "prompt": "Extract ALL details about LIBERO data format: observation keys (agentview_image, eye_in_hand_image, robot0_joint_pos, robot0_gripper_qpos, ee_pos, ee_quat), action dimensions, HDF5 structure, image dimensions, and how data is loaded from LIBERO demos."
  }
}
```

</details>

---

### Tool call

_source line 129 · 2026-05-15T11:18:42.241997+00:00_

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
  "session": "worker_research_libero-benchmark_20260515T111137",
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

_source line 130 · 2026-05-15T11:18:42.242113+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_libero-benchmark_20260515T111137",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 131 · 2026-05-15T11:18:42.242237+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://robomimic.github.io/docs/tutorials/dataset_contents.html",
  "prompt": "Extract ALL details about robosuite/robomimic HDF5 dataset format: obs keys, action dimensions, data structure, demonstration format. Focus on information relevant to LIBERO which uses this format."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_libero-benchmark_20260515T111137",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://robomimic.github.io/docs/tutorials/dataset_contents.html",
    "prompt": "Extract ALL details about robosuite/robomimic HDF5 dataset format: obs keys, action dimensions, data structure, demonstration format. Focus on information relevant to LIBERO which uses this format."
  }
}
```

</details>

---

### Tool result

_source line 132 · 2026-05-15T11:18:42.242365+00:00_

# LIBERO Data Format Details

## Observation Keys
The script records multiple observation modalities from the environment:
- **Image observations**: `agentview_rgb` and `eye_in_hand_rgb` (both at 256x256 resolution)
- **Gripper state**: `gripper_states` from `robot0_gripper_qpos`
- **Joint configuration**: `joint_states` from `robot0_joint_pos`
- **End-effector pose**: `ee_states` combining position and axis-angle orientation, stored separately as `ee_pos` (3D) and `ee_ori` (3D axis-angle)
- **Robot state**: Full concatenation of gripper position, end-effector position, and quaternion

## Action Dimensions
Actions are 7-dimensional vectors where the final dimension represents gripper control. The script filters "no-op actions" when all movement dimensions are near zero (threshold <1e-4) and gripper action matches the previous timestep's gripper command.

## HDF5 Structure
Data is organized hierarchically:
```
data/
  demo_0/
    obs/
      gripper_states, joint_states, ee_states, ee_pos, ee_ori
      agentview_rgb, eye_in_hand_rgb
    actions, states, robot_states, rewards, dones
```

Each episode stores timestep sequences where "dones" and "rewards" are one-hot vectors marking successful task completion at the final transition.

## Data Loading Process
The script replays original demonstrations by: setting initial environment state from stored states, executing recorded actions sequentially, and capturing observations at each step—filtering unsuccessful episodes and no-op transitions in the process.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_libero-benchmark_20260515T111137",
  "tool": "WebFetch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 133 · 2026-05-15T11:18:42.242527+00:00_

# robomimic HDF5 Dataset Format Overview

Based on the documentation provided, here's what's available about the robomimic HDF5 dataset structure:

## Key References

The page indicates that **"HDF5 Dataset Structure"** details are documented elsewhere in their [dataset overview section](../datasets/overview.html#dataset-structure), which would contain the authoritative specification.

## Available Information

The documentation mentions several components stored in datasets:

1. **Trajectory Statistics**: The `get_dataset_info.py` utility reveals "statistics about the trajectories (number, average length, etc.)"

2. **Metadata Elements**:
   - Filter keys (for data organization)
   - "Environment metadata in the dataset, which is used to construct the same simulator environment that the data was collected on"

3. **Data Types**: The tutorial demonstrates handling:
   - Image observations (agentview, robot0_eye_in_hand cameras)
   - Depth observations
   - Action recordings
   - Demonstration frames

## Practical Access

For detailed specifications on observation keys, action dimensions, and complete data structure, the documentation directs users to:
- The `get_dataset_info.py` script for structure inspection
- A Jupyter notebook at `examples/notebooks/datasets.ipynb` containing "useful python code snippets for working with robomimic hdf5 datasets"

**Note**: This webpage excerpt doesn't contain the actual field names or dimensional specifications—those appear to be documented in linked sections not included here.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_libero-benchmark_20260515T111137",
  "tool": "WebFetch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 134 · 2026-05-15T11:18:42.242682+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://raw.githubusercontent.com/Lifelong-Robot-Learning/LIBERO/master/libero/configs/data/default.yaml",
  "prompt": "Extract ALL observation configuration: obs keys, image sizes, modalities, action dimensions, sequence length, and any other data specifications."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_libero-benchmark_20260515T111137",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://raw.githubusercontent.com/Lifelong-Robot-Learning/LIBERO/master/libero/configs/data/default.yaml",
    "prompt": "Extract ALL observation configuration: obs keys, image sizes, modalities, action dimensions, sequence length, and any other data specifications."
  }
}
```

</details>

---

### Tool call

_source line 135 · 2026-05-15T11:18:42.242815+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://raw.githubusercontent.com/Lifelong-Robot-Learning/LIBERO/master/libero/configs/eval/default.yaml",
  "prompt": "Extract ALL evaluation configuration: number of evaluation episodes, max steps, success metrics, and any other evaluation parameters."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_libero-benchmark_20260515T111137",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://raw.githubusercontent.com/Lifelong-Robot-Learning/LIBERO/master/libero/configs/eval/default.yaml",
    "prompt": "Extract ALL evaluation configuration: number of evaluation episodes, max steps, success metrics, and any other evaluation parameters."
  }
}
```

</details>

---

### Tool call

_source line 136 · 2026-05-15T11:18:42.242945+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "LIBERO benchmark dataset size GB each suite libero_spatial libero_object libero_goal libero_90 libero_long download"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_libero-benchmark_20260515T111137",
  "tool": "WebSearch",
  "tool_args": {
    "query": "LIBERO benchmark dataset size GB each suite libero_spatial libero_object libero_goal libero_90 libero_long download"
  }
}
```

</details>

---

### Tool result

_source line 137 · 2026-05-15T11:18:42.243066+00:00_

# Observation Configuration Extraction

**Observation Keys:**
- RGB images: "agentview_rgb", "eye_in_hand_rgb"
- Low-dimensional: "gripper_states", "joint_states"

**Image Specifications:**
- Resolution: 128×128 pixels
- Frame stacking: 1
- Number of keypoints: 64

**Data Modalities:**
The configuration includes "image" and "proprio" (proprioceptive) data types, with eye-in-hand and gripper observations enabled.

**Sequence & Temporal:**
- Sequence length: 10 steps
- Maximum word length: 25 characters

**Action Configuration:**
- Affine translation dimension: 4
- Action scale: 1.0
- Training/dataset split: 80% train ratio

**Additional Specifications:**
- Single task group (no multitasking)
- Task shuffling disabled
- Joint states and end-effector gripper information included
- State dimension: not predefined (null)

**Environment Mapping:**
Observations map to robosuite-compatible keys: agentview_image, robot0_eye_in_hand_image, robot0_gripper_qpos, and robot0_joint_pos.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_libero-benchmark_20260515T111137",
  "tool": "WebFetch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 138 · 2026-05-15T11:18:42.243263+00:00_

# Evaluation Configuration Extracted

Based on the provided configuration file, here are the evaluation parameters:

**Evaluation Episodes & Frequency:**
- `"n_eval: 20"` — number of evaluation episodes per evaluation cycle
- `"eval_every: 5"` — evaluation conducted at 5-step intervals

**Maximum Steps:**
- `"max_steps: 600"` — training terminates at 600 steps total

**Processing Parameters:**
- `"batch_size: 64"` — samples processed per batch during evaluation
- `"num_workers: 4"` — parallel workers for data loading
- `"use_mp: true"` with `"num_procs: 20"` — multiprocessing enabled across 20 processes

**Additional Settings:**
- `"eval: true"` — evaluation mode activated
- `"save_sim_states: false"` — simulation states not preserved

**Note:** No explicit success metrics are defined in this configuration snippet. The document contains infrastructure and scheduling parameters but lacks threshold-based performance criteria.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_libero-benchmark_20260515T111137",
  "tool": "WebFetch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 139 · 2026-05-15T11:18:42.243434+00:00_

Web search results for query: "LIBERO benchmark dataset size GB each suite libero_spatial libero_object libero_goal libero_90 libero_long download"

Links: [{"title":"LIBERO · Hugging Face","url":"https://huggingface.co/docs/lerobot/libero"},{"title":"GitHub - Lifelong-Robot-Learning/LIBERO: Benchmarking Knowledge Transfer in Lifelong Robot Learning · GitHub","url":"https://github.com/Lifelong-Robot-Learning/LIBERO"},{"title":"Libero-Object Benchmark","url":"https://www.emergentmind.com/topics/libero-object-benchmark"},{"title":"LIBERO: Benchmarking Knowledge Transfer for Lifelong Robot Learning","url":"https://papers.neurips.cc/paper_files/paper/2023/file/8c3c666820ea055a77726d66fc7d447f-Paper-Datasets_and_Benchmarks.pdf"},{"title":"Libero - LeRobot","url":"https://www.mintlify.com/huggingface/lerobot/simulation/libero"},{"title":"LIBERO Benchmark: Vision-Language-Action in Robotics","url":"https://www.emergentmind.com/topics/libero"},{"title":"LIBERO: simulation benchmark for the study of lifelong robot learning | by Deepthi Karkada | Medium","url":"https://medium.com/@deepkarkada/libero-simulation-benchmark-for-the-study-of-lifelong-robot-learning-583b786a96f6"},{"title":"LIBERO Datasets – LIBERO","url":"https://libero-project.github.io/datasets"},{"title":"LIBERO-PRO: Towards Robust and Fair Evaluation of Vision-Language-Action Models Beyond Memorization","url":"https://arxiv.org/html/2510.03827v1"},{"title":"LIBERO Tasks: Lifelong Robotic Learning","url":"https://www.emergentmind.com/topics/libero-tasks"}]

Let me search more specifically for dataset size information in GB.

Links: [{"title":"HuggingFaceVLA/libero · Datasets at Hugging Face","url":"https://huggingface.co/datasets/HuggingFaceVLA/libero"},{"title":"yifengzhu-hf/LIBERO-datasets · Datasets at Hugging Face","url":"https://huggingface.co/datasets/yifengzhu-hf/LIBERO-datasets"},{"title":"lerobot/libero · Datasets at Hugging Face","url":"https://huggingface.co/datasets/lerobot/libero"},{"title":"physic
…[truncated 6186 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_libero-benchmark_20260515T111137",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 140 · 2026-05-15T11:18:42.243611+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://libero-project.github.io/datasets",
  "prompt": "Extract ALL dataset details: size of each suite, number of demonstrations per task, total data sizes, download instructions, and any other specifications."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_libero-benchmark_20260515T111137",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://libero-project.github.io/datasets",
    "prompt": "Extract ALL dataset details: size of each suite, number of demonstrations per task, total data sizes, download instructions, and any other specifications."
  }
}
```

</details>

---

### Tool call

_source line 141 · 2026-05-15T11:18:42.243754+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://huggingface.co/datasets/physical-intelligence/libero",
  "prompt": "Extract dataset size information: total size, individual suite sizes (libero_spatial, libero_object, libero_goal, libero_10/libero_long, libero_90), number of episodes per suite, file counts, and any other size/format details."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_libero-benchmark_20260515T111137",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://huggingface.co/datasets/physical-intelligence/libero",
    "prompt": "Extract dataset size information: total size, individual suite sizes (libero_spatial, libero_object, libero_goal, libero_10/libero_long, libero_90), number of episodes per suite, file counts, and any other size/format details."
  }
}
```

</details>

---

### Tool call

_source line 142 · 2026-05-15T11:18:42.243889+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://raw.githubusercontent.com/Lifelong-Robot-Learning/LIBERO/master/libero/configs/policy/bc_transformer_policy.yaml",
  "prompt": "Extract ALL policy configuration: observation dimensions, action dimensions, network architecture, and any other relevant specs."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_libero-benchmark_20260515T111137",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://raw.githubusercontent.com/Lifelong-Robot-Learning/LIBERO/master/libero/configs/policy/bc_transformer_policy.yaml",
    "prompt": "Extract ALL policy configuration: observation dimensions, action dimensions, network architecture, and any other relevant specs."
  }
}
```

</details>

---

### Tool result

_source line 143 · 2026-05-15T11:18:42.244094+00:00_



Here is the structured research report.

---

## 1. Does LeRobot Natively Support LIBERO?

**Yes.** LIBERO is a first-class benchmark in LeRobot. It is installed via:

```bash
pip install -e ".[libero]"
```

LeRobot provides native environment wrappers (`--env.type=libero`), official documentation at [huggingface.co/docs/lerobot/en/libero](https://huggingface.co/docs/lerobot/en/libero), and a dedicated fork of the LIBERO codebase at [github.com/huggingface/lerobot-libero](https://github.com/huggingface/lerobot-libero).

LIBERO covers **130 tasks** across **5 task suites**:

| Suite | CLI name | Tasks | Description |
|-------|----------|-------|-------------|
| LIBERO-Spatial | `libero_spatial` | 10 | Spatial relation reasoning |
| LIBERO-Object | `libero_object` | 10 | Object manipulation |
| LIBERO-Goal | `libero_goal` | 10 | Goal-conditioned tasks |
| LIBERO-90 | `libero_90` | 90 | Short-horizon tasks |
| LIBERO-Long | `libero_10` | 10 | Long-horizon tasks |

There is also **LIBERO-plus** (`--env.type=libero_plus`), a robustness extension with ~10,000 perturbed task variants across 7 dimensions (camera, lighting, layout, language, etc.).

---

## 2. Dataset Names on HuggingFace Hub

### Primary datasets (recommended for training)

| Dataset ID | Episodes | Tasks | Size | Notes |
|------------|----------|-------|------|-------|
| `HuggingFaceVLA/libero` | 148 | 10 | ~1.9 GB | Official preprocessed dataset, recommended by LeRobot docs |
| `lerobot/libero` | 1,693 | 40 | ~1.94 GB | All 4 standard suites combined (video format, AV1 codec) |
| `physical-intelligence/libero` | 147 | 10 | ~34.9 GB | PI's conversion, RLDS-origin, CC-BY-4.0 |
| `lerobot/libero_plus` | — | — | — | LIBERO-plus training data |

### Per-suite image datasets

| Dataset ID | Tasks | Episodes |
|------------|-------|----------|
| `lerobot/libero_10_image` | 10 | 148 |
| `lerobot/libero_object_image` | 10 | 454 |
| `lerobot/libero_spatial_image` | 10 | — |
| `lerobot/libero_goal_image` | 10 | — 
…[truncated 5326 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_libero-benchmark_20260515T111137",
  "tool": "Agent",
  "elapsed_ms": 19
}
```

</details>

---

### Tool result

_source line 144 · 2026-05-15T11:18:42.244255+00:00_

# LIBERO Datasets Summary

Based on the webpage content provided, here's what can be extracted about the datasets:

## Available Suites

The page lists four dataset suites:
- **LIBERO-Spatial**: "10 tasks from LIBERO-Spatial suite"
- **LIBERO-Object**: "10 tasks from LIBERO-Object suite"
- **LIBERO-Goal**: "10 tasks from LIBERO-Goal suite"
- **LIBERO-100**: "100 tasks from LIBERO-100 suite" with data organized under LIBERO-90 and LIBERO-10 folders

## Data Included

Each dataset contains:
- "RGB images from workspace and wrist cameras"
- Proprioceptive sensor readings
- Language-based task descriptions
- PDDL scene representations

## Access Methods

The page provides direct download links for each suite via University of Texas Box storage, plus "a script for programmatic downloading the datasets" through their documentation portal.

## Limitations

The webpage does not specify demonstration counts per task, total storage sizes, or other granular specifications—only directing users to the full LIBERO documentation for comprehensive details.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_libero-benchmark_20260515T111137",
  "tool": "WebFetch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 145 · 2026-05-15T11:18:42.244467+00:00_

# Policy Configuration Extraction

## Policy Type & Architecture
- **Policy Type**: BCTransformerPolicy
- **Extra Network Layers**: 0
- **Extra Hidden Size**: 128
- **Embedding Size**: 64

## Transformer Specifications
- **Number of Layers**: 4
- **Attention Heads**: 6
- **Head Output Size**: 64 per head
- **MLP Hidden Size**: 256
- **Dropout Rate**: 0.1
- **Maximum Sequence Length**: 10
- **Input Size**: Not specified (null)

## Default Component Configuration
The policy uses several standard modules:
- **Image Encoding**: ResNet-based encoder
- **Language Encoding**: MLP encoder
- **Temporal Positioning**: Sinusoidal position encoding
- **Policy Head**: Gaussian Mixture Model head
- **Data Augmentation**: Includes color jittering and translation augmentation

## Notable Gaps
The configuration does not explicitly specify observation or action dimensions—these are likely defined in referenced encoder and head configuration files (e.g., `resnet_encoder.yaml`, `gmm_head.yaml`).

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_libero-benchmark_20260515T111137",
  "tool": "WebFetch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 146 · 2026-05-15T11:18:42.244692+00:00_

# LIBERO Dataset Size Information

Based on the webpage content, here's the dataset size information:

## Overall Dataset Statistics

- **Total Rows**: 273,000 frames
- **Total Episodes**: 147 episodes
- **Dataset Size Category**: 100K - 1M (parquet format)
- **Task Categories**: 10 distinct tasks
- **Data Format**: Parquet (auto-converted from original format)

## Dataset Structure

### Subsets
- **Default subset**: 273k rows

### Splits
- **Train split**: 273k rows (only split available)

## Data Modalities

The dataset includes:
- **Image data**: 256x256 pixel resolution
  - `image`: Main camera view
  - `wrist_image`: Wrist-mounted camera view
- **Time-series data**:
  - `state`: Robot state vector (8 dimensions)
  - `actions`: Action vectors (7 dimensions)
  - `timestamp`: Float32 values

## Frame-level Metadata

Each frame includes:
- `frame_index`: 0-454 (frames per episode)
- `episode_index`: 0-146 (episode identifier)
- `task_index`: 0-9 (10 tasks)
- `index`: 0-40.1k (global frame identifier)

## Related Information

- **Libraries**: Datasets, Dask, Croissant
- **License**: CC-BY-4.0
- **Organization**: Physical Intelligence
- **Related Tags**: LeRobot, libero, panda, rlds
- **Citation**: arXiv:2306.03310

The dataset appears to be a large-scale robotics manipulation dataset with multiple camera views and synchronized state-action pairs suitable for imitation learning and robot learning research.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_libero-benchmark_20260515T111137",
  "tool": "WebFetch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 147 · 2026-05-15T11:18:42.244850+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://raw.githubusercontent.com/Lifelong-Robot-Learning/LIBERO/master/libero/libero/benchmark/libero_suite_task_map.py",
  "prompt": "Extract the complete task list for each suite: LIBERO-Spatial (all 10 task descriptions), LIBERO-Object (all 10 task descriptions), LIBERO-Goal (all 10 task descriptions). Show the exact task names/descriptions."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_libero-benchmark_20260515T111137",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://raw.githubusercontent.com/Lifelong-Robot-Learning/LIBERO/master/libero/libero/benchmark/libero_suite_task_map.py",
    "prompt": "Extract the complete task list for each suite: LIBERO-Spatial (all 10 task descriptions), LIBERO-Object (all 10 task descriptions), LIBERO-Goal (all 10 task descriptions). Show the exact task names/descriptions."
  }
}
```

</details>

---

### Tool call

_source line 148 · 2026-05-15T11:18:42.244986+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://pypi.org/project/libero/",
  "prompt": "Extract installation instructions, version info, dependencies, and any other details about the LIBERO pip package."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_libero-benchmark_20260515T111137",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://pypi.org/project/libero/",
    "prompt": "Extract installation instructions, version info, dependencies, and any other details about the LIBERO pip package."
  }
}
```

</details>

---

### Tool result

_source line 149 · 2026-05-15T11:18:42.245119+00:00_

# LIBERO Task Suites

## LIBERO-Spatial (10 tasks)
1. "pick_up_the_black_bowl_between_the_plate_and_the_ramekin_and_place_it_on_the_plate"
2. "pick_up_the_black_bowl_next_to_the_ramekin_and_place_it_on_the_plate"
3. "pick_up_the_black_bowl_from_table_center_and_place_it_on_the_plate"
4. "pick_up_the_black_bowl_on_the_cookie_box_and_place_it_on_the_plate"
5. "pick_up_the_black_bowl_in_the_top_drawer_of_the_wooden_cabinet_and_place_it_on_the_plate"
6. "pick_up_the_black_bowl_on_the_ramekin_and_place_it_on_the_plate"
7. "pick_up_the_black_bowl_next_to_the_cookie_box_and_place_it_on_the_plate"
8. "pick_up_the_black_bowl_on_the_stove_and_place_it_on_the_plate"
9. "pick_up_the_black_bowl_next_to_the_plate_and_place_it_on_the_plate"
10. "pick_up_the_black_bowl_on_the_wooden_cabinet_and_place_it_on_the_plate"

## LIBERO-Object (10 tasks)
1. "pick_up_the_alphabet_soup_and_place_it_in_the_basket"
2. "pick_up_the_cream_cheese_and_place_it_in_the_basket"
3. "pick_up_the_salad_dressing_and_place_it_in_the_basket"
4. "pick_up_the_bbq_sauce_and_place_it_in_the_basket"
5. "pick_up_the_ketchup_and_place_it_in_the_basket"
6. "pick_up_the_tomato_sauce_and_place_it_in_the_basket"
7. "pick_up_the_butter_and_place_it_in_the_basket"
8. "pick_up_the_milk_and_place_it_in_the_basket"
9. "pick_up_the_chocolate_pudding_and_place_it_in_the_basket"
10. "pick_up_the_orange_juice_and_place_it_in_the_basket"

## LIBERO-Goal (10 tasks)
1. "open_the_middle_drawer_of_the_cabinet"
2. "put_the_bowl_on_the_stove"
3. "put_the_wine_bottle_on_top_of_the_cabinet"
4. "open_the_top_drawer_and_put_the_bowl_inside"
5. "put_the_bowl_on_top_of_the_cabinet"
6. "push_the_plate_to_the_front_of_the_stove"
7. "put_the_cream_cheese_in_the_bowl"
8. "turn_on_the_stove"
9. "put_the_bowl_on_the_plate"
10. "put_the_wine_bottle_on_the_rack"

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_libero-benchmark_20260515T111137",
  "tool": "WebFetch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 150 · 2026-05-15T11:18:42.245252+00:00_

# LIBERO Package Information

## Version & Release
- **Current Version:** 0.1.1
- **Release Date:** November 3, 2025
- **Python Requirement:** Python >=3

## Installation

The package supports two installation methods:

**Standard Installation:**
```bash
conda create -n libero python=3.8.13
conda activate libero
git clone https://github.com/Lifelong-Robot-Learning/LIBERO.git
cd LIBERO
pip install -r requirements.txt
pip install torch==1.11.0+cu113 torchvision==0.12.0+cu113 torchaudio==0.11.0 --extra-index-url https://download.pytorch.org/whl/cu113
pip install -e .
```

**PyPI Installation:**
```bash
pip install libero
```

## Project Overview

"LIBERO is designed for studying knowledge transfer in multitask and lifelong robot learning problems." The benchmark provides 130 tasks organized into four suites: LIBERO-Spatial, LIBERO-Object, LIBERO-Goal, and LIBERO-100.

## Key Features

- Procedural generation pipeline for manipulation tasks
- Four task suites with controlled distribution shifts
- Three policy architectures: bc_rnn_policy, bc_transformer_policy, bc_vilt_policy
- Multiple lifelong learning algorithms

## Maintainers
- imstevenpmwork
- jadechoghari (Jade Choghari, HuggingFace)

## Licensing

| Component | License |
|-----------|---------|
| Codebase | MIT |
| Datasets | CC BY 4.0 |

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_libero-benchmark_20260515T111137",
  "tool": "WebFetch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 151 · 2026-05-15T11:18:42.245505+00:00_



Here is the structured research report.

---

## 1. What LIBERO-Plus Is

LIBERO-Plus is a robustness evaluation benchmark that extends the original LIBERO robot manipulation benchmark. It was published as "LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-Action Models" (arXiv:2510.13626, accepted at CVPR 2026).

**What it adds on top of LIBERO:**
- **10,030 task variants** generated by applying systematic perturbations to original LIBERO tasks
- **7 perturbation dimensions** with **21 sub-dimensions**
- **5 difficulty levels** (L1-L5) stratified by multi-model consensus (how many of 4 reference models solve the task)
- **20,000+ training trajectories** collected under varied conditions (stored in RLDS format)
- Drop-in replacement for vanilla LIBERO — same Python interface, same camera names, same observation/action format

## 2. Source

- **Paper:** [arXiv:2510.13626](https://arxiv.org/abs/2510.13626)
- **GitHub:** [github.com/sylvestf/LIBERO-plus](https://github.com/sylvestf/LIBERO-plus)
- **Project page:** [sylvestf.github.io/LIBERO-plus](https://sylvestf.github.io/LIBERO-plus/)
- **Assets (HuggingFace):** [Sylvest/LIBERO-plus](https://huggingface.co/datasets/Sylvest/LIBERO-plus)
- **Training dataset (RLDS):** [Sylvest/libero_plus_rlds](https://huggingface.co/datasets/Sylvest/libero_plus_rlds)
- **LeRobot-format dataset:** [lerobot/libero_plus](https://huggingface.co/datasets/lerobot/libero_plus)

## 3. The 7 Perturbation Dimensions (Exact Definitions)

Note: The user asked about 4 dimensions. LIBERO-Plus actually defines **7**, not 4.

### 3.1 Objects Layout (O1, O2)
- **O1 — Confounding objects:** Adds n additional unseen distractor objects into the scene from a pool of 416 objects, implemented by modifying BDDL task description files.
- **O2 — Target displacement:** Applies random perturbations to the target object's initial position (x, y, z) and orientation while preserving semantic relationships.

### 3.2 Camera Viewpoints (C1, C2, C3)
- **C1 
…[truncated 10149 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_libero-benchmark_20260515T111137",
  "tool": "Agent",
  "elapsed_ms": 21
}
```

</details>

---

### Tool result

_source line 152 · 2026-05-15T11:18:42.245793+00:00_

Now I have comprehensive information. Let me compile the final report.

---

## LIBERO Benchmark: Comprehensive Technical Reference

### 1. GitHub Repo URL

**Official:** https://github.com/Lifelong-Robot-Learning/LIBERO

**Paper:** [arXiv:2306.03310](https://arxiv.org/abs/2306.03310) (NeurIPS 2023 Datasets & Benchmarks)

**Project website:** https://libero-project.github.io

**HuggingFace fork (LeRobot integration):** https://github.com/huggingface/lerobot-libero

---

### 2. Installation

**Method A: pip (simplest)**
```bash
pip install libero
```
Current version: 0.1.1. Requires Python >= 3.

**Method B: From source (recommended for development)**
```bash
conda create -n libero python=3.8.13
conda activate libero
git clone https://github.com/Lifelong-Robot-Learning/LIBERO.git
cd LIBERO
pip install -r requirements.txt
pip install torch==1.11.0+cu113 torchvision==0.12.0+cu113 torchaudio==0.11.0 --extra-index-url https://download.pytorch.org/whl/cu113
pip install -e .
```

**Method C: Via LeRobot**
```bash
pip install -e ".[libero]"
```

Underlying simulator: **robosuite** (MuJoCo-based). For headless rendering: `export MUJOCO_GL=egl`.

Licenses: MIT (code), CC BY 4.0 (datasets).

---

### 3. The 5 Task Suites

All tasks are language-conditioned manipulation with a Franka Panda arm.

| Suite | CLI name | Tasks | Description |
|-------|----------|-------|-------------|
| **LIBERO-Spatial** | `libero_spatial` | 10 | Same goal (pick black bowl, place on plate) but bowl is in different spatial locations. Tests transfer of **spatial relationship knowledge**. |
| **LIBERO-Object** | `libero_object` | 10 | Same goal structure (pick X, place in basket) but with different objects (soup, cream cheese, ketchup, etc.). Tests transfer of **object knowledge**. |
| **LIBERO-Goal** | `libero_goal` | 10 | Same scene but different goals (open drawer, put bowl on stove, turn on stove, etc.). Tests transfer of **goal/procedural knowledge**. |
| **LIBERO-90** | `libero_90` | 90 | Short-
…[truncated 8140 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_libero-benchmark_20260515T111137",
  "tool": "Agent",
  "elapsed_ms": 23
}
```

</details>

---

### Tool call

_source line 153 · 2026-05-15T11:18:42.245997+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls /home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/action_cond_info_bottleneck/artifacts/",
  "description": "Check artifacts directory exists"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_libero-benchmark_20260515T111137",
  "tool": "Bash",
  "tool_args": {
    "command": "ls /home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/action_cond_info_bottleneck/artifacts/",
    "description": "Check artifacts directory exists"
  }
}
```

</details>

---

### Tool result

_source line 154 · 2026-05-15T11:18:42.246130+00:00_

Exit code 2
ls: cannot access '/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/action_cond_info_bottleneck/artifacts/': No such file or directory

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_libero-benchmark_20260515T111137",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 155 · 2026-05-15T11:18:42.246251+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "mkdir -p /home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/action_cond_info_bottleneck/artifacts",
  "description": "Create artifacts directory"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_libero-benchmark_20260515T111137",
  "tool": "Bash",
  "tool_args": {
    "command": "mkdir -p /home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/action_cond_info_bottleneck/artifacts",
    "description": "Create artifacts directory"
  }
}
```

</details>

---

### Tool result

_source line 156 · 2026-05-15T11:18:42.246370+00:00_

(Bash completed with no output)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_libero-benchmark_20260515T111137",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 157 · 2026-05-15T11:18:42.246559+00:00_

called Write

<details open><summary>🔧 Tool call — Write</summary>

````json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/action_cond_info_bottleneck/artifacts/research_libero_benchmark.md",
  "content": "# LIBERO Benchmark + LIBERO-Plus 调研报告\n\n调研日期：2026-05-15\n\n---\n\n## 1. LIBERO Benchmark\n\n### 1.1 基本信息\n\n| 项目 | 内容 |\n|------|------|\n| 论文 | [LIBERO: Benchmarking Knowledge Transfer for Lifelong Robot Learning](https://arxiv.org/abs/2306.03310) (NeurIPS 2023 D&B) |\n| GitHub | https://github.com/Lifelong-Robot-Learning/LIBERO |\n| 项目主页 | https://libero-project.github.io |\n| License | MIT (代码), CC BY 4.0 (数据集) |\n| 模拟器 | robosuite (MuJoCo) |\n| 机器人 | Franka Panda 7-DOF |\n\n### 1.2 安装\n\n**方式 A：pip**\n```bash\npip install libero\n```\n\n**方式 B：from source（推荐）**\n```bash\nconda create -n libero python=3.8.13\nconda activate libero\ngit clone https://github.com/Lifelong-Robot-Learning/LIBERO.git\ncd LIBERO\npip install -r requirements.txt\npip install torch==1.11.0+cu113 torchvision==0.12.0+cu113 torchaudio==0.11.0 --extra-index-url https://download.pytorch.org/whl/cu113\npip install -e .\n```\n\n**方式 C：通过 LeRobot**\n```bash\npip install -e \".[libero]\"\n```\n\n无头渲染需设置：`export MUJOCO_GL=egl`\n\n### 1.3 五个 Task Suite\n\n所有任务都是 language-conditioned manipulation，使用 Franka Panda 机械臂。\n\n| Suite | CLI 名称 | 任务数 | 描述 |\n|-------|----------|--------|------|\n| **LIBERO-Spatial** | `libero_spatial` | 10 | 同一目标（拿黑碗放盘子），碗在不同空间位置。测试 **空间关系知识** 迁移 |\n| **LIBERO-Object** | `libero_object` | 10 | 同一目标结构（拿 X 放篮子），不同物体。测试 **物体知识** 迁移 |\n| **LIBERO-Goal** | `libero_goal` | 10 | 同一场景，不同目标（开抽屉、放碗到炉子上等）。测试 **目标/程序知识** 迁移 |\n| **LIBERO-90** | `libero_90` | 90 | LIBERO-100 中的短期任务，跨 spatial/object/goal 的混合分布偏移。用于 **预训练** |\n| **LIBERO-Long** | `libero_10` | 10 | LIBERO-100 中的长期多步骤任务。用于预训练后的 **下游评测** |\n\n**LIBERO-Spatial 示例任务（全部 10 个）：**\n1. pick_up_the_black_bowl_between_the_plate_and_the_ramekin_and_place_it_on_the_plate\n2. pick_up_the_black_bowl_next_to_the_ramekin_and_place_it_on_the_plate\n3. pick_up_the_black_bowl_from_table_center_and_place_it_on_the_plate\n4. pick_up_the_black_bowl_on_the_cookie_box_and_place_it_on_the_plate\n5. pick_up_the_black_bowl_in_the_top_drawer_of_the_wooden_cabinet_and_place_it_on_the_plate\n6. pick_up_the_black_bowl_on_the_ramekin_and_place_it_on_the_plate\n7. pick_up_the_black_bowl_next_to_the_cookie_box_and_place_it_on_the_plate\n8. pick_up_the_black_bowl_on_the_stove_and_place_it_on_the_plate\n9. pick_up_the_black_bowl_next_to_the_plate_and_place_it_on_the_plate\n10. pick_up_the_black_bowl_on_the_wooden_cabinet_and_place_it_on_the_plate\n\n**LIBERO-Object 示例任务：** pick_up_the_{alphabet_soup, cream_cheese, salad_dressing, bbq_sauce, ketchup, tomato_sauce, butter, milk, chocolate_pudding, orange_juice}_and_place_it_in_the_basket\n\n**LIBERO-Goal 示例任务：** open_the_middle_drawer_of_the_cabinet, put_the_bowl_on_the_stove, put_the_wine_bottle_on_top_of_the_cabinet, open_the_top_drawer_and_put_the_bowl_inside, put_the_bowl_on_top_of_the_cabinet, push_the_plate_to_the_front_of_the_stove, put_the_cream_cheese_in_the_bowl, turn_on_the_stove, put_the_bowl_on_the_plate, put_the_wine_bottle_on_the_rack\n\n### 1.4 数据下载\n\n每个任务有 **50 条人类遥操作演示**，通过 SpaceMouse 以 20 Hz 采集。\n\n**方式 A：官方脚本**\n```bash\n# 全部下载\npython benchmark_scripts/download_libero_datasets.py\n\n# 下载特定 suite\npython benchmark_scripts/download_libero_datasets.py --datasets libero_spatial\npython benchmark_scripts/download_libero_datasets.py --datasets libero_object\npython benchmark_scripts/download_libero_datasets.py --datasets libero_goal\npython benchmark_scripts/download_libero_datasets.py --datasets libero_100  # 含 libero_90 + libero_10\n\n# 通过 HuggingFace 下载（推荐，原始链接可能过期）\npython benchmark_scripts/download_libero_datasets.py --use-huggingface\n```\n\n默认下载位置：LIBERO 根目录下的 `./datasets/`\n\n**方式 B：HuggingFace 直接下载**\n\n| 数据集 | 格式 | 大小 |\n|--------|------|------|\n| `yifengzhu-hf/LIBERO-datasets` | 原始 HDF5 | ~100 GB 总计 |\n| `physical-intelligence/libero` | LeRobot (Parquet) | ~34.9 GB |\n| `HuggingFaceVLA/libero` | LeRobot | ~1.9 GB |\n| `lerobot/libero` | LeRobot (视频 AV1) | ~1.94 GB |\n\n**各 suite 近似大小（原始 HDF5 格式）：**\n\n| Suite | 大小 |\n|-------|------|\n| libero_spatial | ~6.6 GB |\n| libero_object | ~9.3 GB |\n| libero_goal | ~6-9 GB |\n| libero_10 (Long) | ~12.8 GB |\n| libero_90 | ~60-70 GB |\n| **总计** | **~100 GB** |\n\n### 1.5 数据格式\n\n**文件格式：** HDF5（每个任务一个 `.hdf5` 文件）\n\n**HDF5 结构：**\n```\ndata/\n  demo_0/\n    obs/\n      agentview_rgb          # (T, 128, 128, 3) uint8 — 第三人称相机\n      eye_in_hand_rgb        # (T, 128, 128, 3) uint8 — 腕部相机\n      gripper_states         # (T, 1) — 夹爪开合度\n      joint_states           # (T, 7) — 7 个关节角度\n      ee_states              # (T, 6) — 末端执行器位置 + 轴角朝向\n      ee_pos                 # (T, 3) — 末端执行器 xyz 位置\n      ee_ori                 # (T, 3) — 末端执行器轴角朝向\n    actions                  # (T, 7) — 7-DOF 动作\n    states                   # (T, D) — 完整模拟器状态\n    robot_states             # (T, D) — gripper_pos + ee_pos + ee_quat 拼接\n    rewards                  # (T,) — 稀疏: 全 0，最后成功步为 1\n    dones                    # (T,) — episode 结束时为 1\n  demo_1/ ...\n  demo_49/ ...\n```\n\n**观测空间：**\n\n| 键 | 维度 | 含义 |\n|----|------|------|\n| `agentview_rgb` (→ `agentview_image`) | (128, 128, 3) | 工作区 RGB 图像 |\n| `eye_in_hand_rgb` (→ `robot0_eye_in_hand_image`) | (128, 128, 3) | 腕部 RGB 图像 |\n| `gripper_states` (→ `robot0_gripper_qpos`) | (1,) 或 (2,) | 夹爪指位置 |\n| `joint_states` (→ `robot0_joint_pos`) | (7,) | Franka Panda 7 关节角 |\n| `ee_pos` | (3,) | 末端执行器 xyz 位置 |\n| `ee_ori` | (3,) | 末端执行器轴角朝向 |\n\n**LeRobot 格式中** proprioceptive state 为 8 维：`observation.state` = [ee_pos (3) + ee_axis_angle (3) + gripper_qpos (2)]\n\n**动作空间：**\n\n| 维度 | 含义 |\n|------|------|\n| 0-2 | 末端执行器位置增量 (dx, dy, dz) |\n| 3-5 | 末端执行器朝向增量 (轴角 / 欧拉角) |\n| 6 | 夹爪命令 (1=闭合, -1=打开) |\n\n- 总计 **7 维连续动作**，Box(-1, 1, shape=(7,))\n- 控制模式：**OSC_POSE**（操作空间控制）\n- 频率：**20 Hz**（原始），LeRobot 格式 **10 Hz**\n- 支持 `relative`（增量，默认）和 `absolute` 两种控制模式\n- 奖励：稀疏 — 中间步全 0，任务完成时 +1\n\n### 1.6 评测\n\n**原生 LIBERO 评测：**\n\n```bash\npython libero/lifelong/evaluate.py \\\n  --benchmark LIBERO_SPATIAL \\\n  --task_id 0 \\\n  --algo base \\\n  --policy bc_transformer_policy \\\n  --seed 10000 \\\n  --ep 50 \\\n  --load_task 0 \\\n  --device_id 0\n```\n\n参数说明：\n- `--benchmark`: `LIBERO_SPATIAL` / `LIBERO_OBJECT` / `LIBERO_GOAL` / `LIBERO_90` / `LIBERO_10`\n- `--task_id`: suite 内的任务索引\n- `--algo`: 终身学习算法 (`base`, `er`, `ewc`, `packnet`, `multitask`)\n- `--policy`: 策略架构 (`bc_rnn_policy`, `bc_transformer_policy`, `bc_vilt_policy`)\n- `--save-videos`: 可选，录制评测视频\n\n**评测协议：**\n- 20 个并行环境同时运行 (`n_eval: 20`, `num_procs: 20`)\n- 每个 episode 最多 600 步 (`max_steps: 600`)\n- 开头 5 步零动作用于物理稳定\n- episode 在 `done=True` 或达到最大步数时终止\n\n**输出指标：**\n- **Success rate** = num_success / num_envs（每个任务）\n- **Loss** = 测试集损失\n- 结果保存路径：`{save_dir}/{benchmark}_{algo}_{policy}_{seed}_[ep|load]_{task_id}.stats`\n\n**终身学习指标（跨任务序列）：**\n- **FWT (Forward Transfer)**: 序列训练后在新任务上的成功率\n- **NBT (Negative Backward Transfer)**: 早期任务性能退化（灾难性遗忘）\n- **AUC (Area Under Curve)**: 综合 FWT 和 NBT 的累积成功率\n\n**原生训练命令：**\n```bash\nexport CUDA_VISIBLE_DEVICES=0 && \\\nexport MUJOCO_EGL_DEVICE_ID=0 && \\\npython libero/lifelong/main.py seed=10000 \\\n  benchmark_name=LIBERO_SPATIAL \\\n  policy=bc_transformer_policy \\\n  lifelong=base\n```\n\n**LeRobot 评测：**\n```bash\nlerobot-eval \\\n  --policy.path=\"your-policy-id\" \\\n  --env.type=libero \\\n  --env.task=libero_spatial,libero_object,libero_goal,libero_10 \\\n  --eval.batch_size=1 \\\n  --eval.n_episodes=10 \\\n  --env.max_parallel_tasks=1\n```\n标准协议：每个任务 10 个 episode，4 个标准 suite = 400 个 episode。\n\n---\n\n## 2. LIBERO-Plus 扰动评测\n\n### 2.1 基本信息\n\n| 项目 | 内容 |\n|------|------|\n| 论文 | [LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-Action Models](https://arxiv.org/abs/2510.13626) (CVPR 2026) |\n| GitHub | https://github.com/sylvestf/LIBERO-plus |\n| 项目主页 | https://sylvestf.github.io/LIBERO-plus/ |\n| HF 资产 | https://huggingface.co/datasets/Sylvest/LIBERO-plus |\n| 训练数据 (RLDS) | https://huggingface.co/datasets/Sylvest/libero_plus_rlds |\n| LeRobot 格式 | https://huggingface.co/datasets/lerobot/libero_plus |\n\n### 2.2 LIBERO-Plus 是什么\n\n在原始 LIBERO 基础上增加了：\n- **10,030 个任务变体**，通过系统化扰动生成\n- **7 个扰动维度**，**21 个子维度**\n- **5 个难度级别** (L1-L5)，按多模型共识分层（4 个参考模型中几个能解决该任务）\n- **20,000+ 训练轨迹**（RLDS 格式）\n- 与 vanilla LIBERO 完全兼容的 drop-in replacement\n\n### 2.3 七个扰动维度（精确定义）\n\n#### 2.3.1 物体布局 (Objects Layout)\n- **O1 — 干扰物体 (Confounding objects):** 从 416 个物体池中随机添加 n 个未见过的干扰物体，通过修改 BDDL 任务描述文件实现\n- **O2 — 目标位移 (Target displacement):** 对目标物体初始位置 (x, y, z) 和朝向施加随机扰动，保持语义关系\n\n#### 2.3.2 相机视角 (Camera Viewpoints)\n- **C1 — 距离缩放 (Distance scaling):** 沿光轴将相机距离缩放 1.01x-2.00x\n- **C2 — 球坐标位置 (Spherical position):** 改变方位角 (delta-theta) 和仰角 (delta-phi)，范围 15-75 度\n- **C3 — 朝向扰动 (Orientation perturbation):** 扰动 yaw/pitch/roll，范围 2-10 度\n\n实现：修改 `Problem` 类接口；主要针对第三人称相机（非腕部相机）\n\n#### 2.3.3 机器人初始状态 (Robot Initial States)\n- 对机械臂初始关节位置施加随机扰动，幅度 0.1-0.5\n- 实现：修改 `Problem` 类接口\n\n#### 2.3.4 语言指令 (Language Instructions)\n- **R1 — 干扰改写 (Distraction rewrites):** 添加与任务无关的上下文信息\n- **R2 — 常识替换 (Commonsense substitution):** 用常识性替代描述替换物体名称\n- **R3 — 推理复杂度 (Reasoning complexity):** 改变多步骤任务的推理复杂度\n- 实现：基于 LLM 的指令改写\n\n#### 2.3.5 光照条件 (Light Conditions)\n- **L1 — 漫射颜色 (Diffuse color):** RGB 通道漫射光照调整\n- **L2 — 方向 (Direction):** 平行光源方向变化\n- **L3 — 镜面强度 (Specular intensity):** 镜面高光强度（反射表面）\n- **L4 — 阴影 (Shadow casting):** 阴影开关控制\n- 实现：修改 MuJoCo 场景 XML 定义文件，注册新场景类\n\n#### 2.3.6 背景纹理 (Background Textures)\n- **B1 — 场景纹理 (Scene texture):** 使用 950 张精选纹理通过 XML 场景文件替换环境纹理\n- **B2 — 表面纹理 (Surface texture):** 随机改变工作表面纹理（桌面、地板）\n- 实现：修改 XML 场景定义文件，添加新纹理资产\n\n#### 2.3.7 传感器噪声 (Sensor Noise)\n图像空间后处理（非物理层级）：\n- **N1 — 运动模糊 (Motion blur):** kernel 半径 r=5-35，高斯 sigma=2-20，角度 U(-45, 45)度\n- **N2 — 高斯模糊 (Gaussian blur):** sigma 1-10\n- **N3 — 缩放模糊 (Zoom blur):** 缩放因子 [s_min, s_max, step] 从 [1, 1.11, 0.01] 到 [1, 1.56, 0.03]\n- **N4 — 雾 (Fog):** 密度 alpha=0.5-5.0，衰减率 beta=1.3-3.0\n- **N5 — 毛玻璃模糊 (Glass blur):** sigma=0.5-2.5，像素位移 delta=1-5，迭代 1-3 次\n\n### 2.4 难度级别 (L1-L5)\n\n按 4 个参考模型（OpenVLA-OFT, pi0, pi0-fast, UniVLA）能否解决分层：\n- L1: 4 个都能解决\n- L2: 3 个能解决\n- L3: 2 个能解决\n- L4: 1 个能解决\n- L5: 无一能解决\n\n### 2.5 安装和运行\n\n**安装：**\n```bash\n# 系统依赖\nsudo apt install libexpat1 libfontconfig1-dev libmagickwand-dev\n\n# 克隆安装\ngit clone https://github.com/sylvestf/LIBERO-plus.git\ncd LIBERO-plus\npip install -e .\npip install -r extra_requirements.txt\n\n# 如果已装 vanilla LIBERO，需先卸载\npip uninstall -y hf-libero\n\nexport MUJOCO_GL=egl\n```\n\n**下载资产：**\n\n从 [HuggingFace](https://huggingface.co/datasets/Sylvest/LIBERO-plus/tree/main) 下载 `assets.zip`，解压到 `LIBERO-plus/libero/libero/assets/`。\n\n期望结构：\n```\nlibero/libero/assets/\n├── articulated_objects/\n├── new_objects/\n├── scenes/\n├── stable_hope_objects/\n├── stable_scanned_objects/\n├── textures/\n├── turbosquid_objects/\n├── serving_region.xml\n├── wall_frames.stl\n└── wall.xml\n```\n\n**配置：** 检查 `/root/.libero/config.yaml`。评测时设 `num_trials_per_task: 1`。\n\n任务到扰动类别映射：`.libero/libero/benchmark/task_classification.json`\n\n**LeRobot 评测：**\n```bash\nlerobot-eval \\\n  --policy.path=\"your-policy-id\" \\\n  --env.type=libero_plus \\\n  --env.task=libero_spatial,libero_object,libero_goal,libero_10 \\\n  --eval.batch_size=1 \\\n  --eval.n_episodes=10 \\\n  --env.max_parallel_tasks=1\n```\n\n### 2.6 与标准 LIBERO 的关系\n\nLIBERO-Plus 是 vanilla LIBERO 的 **drop-in replacement**：\n- 安装在同一个 `libero` Python 包名下（替换原版）\n- 相同的 `LiberoEnv` gym 接口\n- 相同的相机名称 (`agentview_image`, `robot0_eye_in_hand_image`)\n- 相同的观测/动作格式\n- 相同的 task suite 名称\n- **不能同时安装 vanilla LIBERO 和 LIBERO-Plus**，切换需要先卸载再安装\n\n---\n\n## 3. 数据增强相关\n\n### 3.1 robosuite 内置随机化\n\nLIBERO 基于 robosuite (MuJoCo)，robosuite 提供了 `DomainRandomizationWrapper` 和三个 Modder 类，可用于任何 robosuite 环境包括 LIBERO。\n\n**DomainRandomizationWrapper：**\n```python\nfrom robosuite.wrappers import DomainRandomizationWrapper\n\nenv = DomainRandomizationWrapper(\n    env=base_env,\n    seed=42,\n    randomize_color=True,        # 几何体/纹理颜色随机化\n    randomize_camera=True,       # 相机位置/朝向/FOV\n    randomize_lighting=True,     # 光源位置/方向/颜色\n    randomize_dynamics=True,     # 物理参数\n    randomize_on_reset=True,     # episode 重置时随机化\n    randomize_every_n_steps=1,   # rollout 中的频率\n)\n```\n\n**CameraModder（内置）：**\n- 位置扰动：默认 size 0.01\n- 旋转扰动（四元数）：默认 size 0.087 (~5 度)\n- FOV 扰动：默认 size 5.0 度\n\n**LightingModder（内置）：**\n- 位置扰动：默认 size 0.1\n- 方向扰动：默认 size 0.35\n- 镜面/环境光/漫射扰动：默认 size 0.1\n- 开关控制：on/off\n\n**TextureModder（内置）：**\n- RGB 颜色随机化 (local interpolation 0.1)\n- 纹理模式：RGB, checker, noise, gradient\n- 材质属性：反射率、光泽度、镜面反射 (local interpolation 0.2)\n- 天空盒随机化（可选）\n\nDemo 脚本：`robosuite/demos/demo_domain_randomization.py`\n\n### 3.2 LIBERO-Plus 扰动可否复用为训练时数据增强\n\n**可以，且论文已经这样做了。** LIBERO-Plus 同时提供评测任务和训练数据集：\n\n**已提供的训练数据：**\n- **22,400 条训练轨迹**（过滤后 20,000+），在各种扰动条件下生成\n- 分布：2,400 物体布局变体 + 各 4,000 光照/相机/背景/语言/噪声维度\n- RLDS 格式存储，LeRobot 格式见 `lerobot/libero_plus`\n- 论文证明混合 SFT (mix-SFT) 训练显著提升鲁棒性：OpenVLA-OFT+ 平均 79.6%\n\n**三条数据增强路径：**\n\n**路径 A — 直接使用 LIBERO-Plus 训练数据：**\n```bash\nlerobot-train \\\n    --policy.type=smolvla \\\n    --dataset.repo_id=lerobot/libero_plus \\\n    --env.type=libero_plus \\\n    ...\n```\n\n**路径 B — 使用 robosuite 内置 DomainRandomizationWrapper 在线增强：**\n```python\nfrom robosuite.wrappers import DomainRandomizationWrapper\nenv = DomainRandomizationWrapper(\n    env=libero_env,\n    randomize_camera=True,\n    randomize_lighting=True,\n    randomize_color=True\n)\n```\n在线随机化，每 N 步应用随机扰动。适合训练时增强但可控性较低。\n\n**路径 C — 复用 LIBERO-Plus 扰动代码做自定义增强：**\n- 光照/纹理扰动：修改场景 XML + 注册新场景\n- 相机扰动：修改 `Problem` 类接口\n- 传感器噪声 (N1-N5)：纯图像空间后处理，可直接作为标准数据增强应用于任何存储轨迹，无需重新渲染\n\n**关键区别：**\n- robosuite 内置随机化（路径 B）是 **在线** 的，可控性低\n- LIBERO-Plus 扰动（路径 C）是 **结构化** 的，有明确参数范围和难度分层，更适合系统性鲁棒性训练\n- 传感器噪声 (N1-N5) 是纯图像后处理，可以零成本复用为数据增强\n\n---\n\n## 4. 与 LeRobot 的集成\n\n### 4.1 原生支持\n\nLeRobot **原生支持** LIBERO，是一级基准测试环境。\n\n安装：`pip install -e \".[libero]\"`\n\n文档：https://huggingface.co/docs/lerobot/en/libero\n\nHuggingFace 维护了 LIBERO fork：https://github.com/huggingface/lerobot-libero\n\n### 4.2 HuggingFace Hub 数据集\n\n**主要数据集（推荐用于训练）：**\n\n| 数据集 ID | Episodes | 任务数 | 大小 | 说明 |\n|-----------|----------|--------|------|------|\n| `HuggingFaceVLA/libero` | 148 | 10 | ~1.9 GB | 官方预处理数据集，LeRobot 文档推荐 |\n| `lerobot/libero` | 1,693 | 40 | ~1.94 GB | 4 个标准 suite 合并（视频格式, AV1 编码） |\n| `physical-intelligence/libero` | 147 | 10 | ~34.9 GB | PI 的转换版本, RLDS 来源, CC-BY-4.0 |\n| `lerobot/libero_plus` | — | — | — | LIBERO-Plus 训练数据 |\n\n**每个 suite 的图像数据集：**\n\n| 数据集 ID | 任务数 |\n|-----------|--------|\n| `lerobot/libero_10_image` | 10 |\n| `lerobot/libero_object_image` | 10 |\n| `lerobot/libero_spatial_image` | 10 |\n| `lerobot/libero_goal_image` | 10 |\n\n**社区数据集：**\n- `IPEC-COMMUNITY/libero_90_no_noops_lerobot` — LIBERO-90 去除 no-op 版本\n\n### 4.3 数据格式映射\n\n| LIBERO 字段 | LeRobot 特征 | 类型 | 形状 |\n|-------------|-------------|------|------|\n| `agentview_image` | `observation.images.image` | Video/Image | (256, 256, 3) |\n| `robot0_eye_in_hand_image` | `observation.images.image2` | Video/Image | (256, 256, 3) |\n| `observation[\"state\"]` | `observation.state` | float32 | (8,) |\n| `action` | `action` | float32 | (7,) |\n| `language_instruction` | `task` (task_index) | string/int | — |\n\nLeRobot 元数据：robot_type=`panda`，fps=`10`，视频编码=AV1 yuv420p，表格数据用 Parquet 存储\n\n### 4.4 转换脚本\n\n**方式 A：Physical Intelligence 的 OpenPI 转换脚本（主要）**\n\n脚本路径：[`Physical-Intelligence/openpi/examples/libero/convert_libero_data_to_lerobot.py`](https://github.com/Physical-Intelligence/openpi/blob/main/examples/libero/convert_libero_data_to_lerobot.py)\n\n```bash\n# 前置依赖\nuv pip install tensorflow tensorflow_datasets\n\n# 原始数据来源\n# https://huggingface.co/datasets/openvla/modified_libero_rlds\n\n# 执行转换\nuv run examples/libero/convert_libero_data_to_lerobot.py \\\n  --data_dir /path/to/your/data \\\n  --push_to_hub\n```\n\n处理流程：\n1. 读取 4 个 RLDS 数据集：`libero_10_no_noops`, `libero_goal_no_noops`, `libero_object_no_noops`, `libero_spatial_no_noops`\n2. 创建 `LeRobotDataset`，robot_type=panda, fps=10\n3. 逐 episode 迭代，每步调用 `dataset.add_frame()`\n4. 每个 episode 调用 `dataset.save_episode()`\n5. 可选推送到 HuggingFace Hub\n\n处理时间：约 30 分钟\n\n**方式 B：通用 HDF5 → LeRobot 转换器**\n\n仓库：https://github.com/anarnuri/hdf5_to_lerobot_converter\n\n支持 LIBERO 原生 HDF5 格式。\n\n**方式 C：直接使用预转换数据集（无需转换）**\n\n```python\nfrom lerobot.common.datasets.lerobot_dataset import LeRobotDataset\n\ndataset = LeRobotDataset(\"HuggingFaceVLA/libero\")\n# 或\ndataset = LeRobotDataset(\"lerobot/libero\")\n```\n\n### 4.5 端到端训练和评测示例\n\n**训练：**\n```bash\nlerobot-train \\\n  --policy.type=smolvla \\\n  --policy.repo_id=${HF_USER}/libero-test \\\n  --policy.load_vlm_weights=true \\\n  --dataset.repo_id=HuggingFaceVLA/libero \\\n  --env.type=libero \\\n  --env.task=libero_10 \\\n  --output_dir=./outputs/ \\\n  --steps=100000 \\\n  --batch_size=4 \\\n  --eval.batch_size=1 \\\n  --eval.n_episodes=1 \\\n  --eval_freq=1000\n```\n\n**评测：**\n```bash\nlerobot-eval \\\n  --policy.path=\"your-policy-id\" \\\n  --env.type=libero \\\n  --env.task=libero_spatial,libero_object,libero_goal,libero_10 \\\n  --eval.batch_size=1 \\\n  --eval.n_episodes=10 \\\n  --env.max_parallel_tasks=1\n```\n\n---\n\n## 5. 关键注意事项\n\n1. **LIBERO-90 数据** 不在标准预转换数据集中。需要用 OpenPI 转换脚本或社区数据集 `IPEC-COMMUNITY/libero_90_no_noops_lerobot`\n2. **控制模式** (`relative` vs `absolute`) 必须与策略的动作参数化匹配\n3. **vanilla LIBERO 和 LIBERO-Plus 不能同时安装**，两者共用同一 Python 包名\n4. LeRobot 中 LIBERO 仅支持 Linux（MuJoCo 渲染需 EGL）\n5. LeRobot 格式的图像分辨率为 256x256，而原始 LIBERO 为 128x128 [UNVERIFIED — 需确认是否做了上采样或 LeRobot 环境重新渲染]\n6. 原始 LIBERO 采集频率 20Hz，LeRobot 格式为 10Hz（可能做了下采样）[UNVERIFIED — 需确认具体降频策略]\n"
}
````

</details>

<details><summary>Recorded metadata</summary>

````json
{
  "recorded_role": "tool",
  "session": "worker_research_libero-benchmark_20260515T111137",
  "tool": "Write",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/action_cond_info_bottleneck/artifacts/research_libero_benchmark.md",
    "content": "# LIBERO Benchmark + LIBERO-Plus 调研报告\n\n调研日期：2026-05-15\n\n---\n\n## 1. LIBERO Benchmark\n\n### 1.1 基本信息\n\n| 项目 | 内容 |\n|------|------|\n| 论文 | [LIBERO: Benchmarking Knowledge Transfer for Lifelong Robot Learning](https://arxiv.org/abs/2306.03310) (NeurIPS 2023 D&B) |\n| GitHub | https://github.com/Lifelong-Robot-Learning/LIBERO |\n| 项目主页 | https://libero-project.github.io |\n| License | MIT (代码), CC BY 4.0 (数据集) |\n| 模拟器 | robosuite (MuJoCo) |\n| 机器人 | Franka Panda 7-DOF |\n\n### 1.2 安装\n\n**方式 A：pip**\n```bash\npip install libero\n```\n\n**方式 B：from source（推荐）**\n```bash\nconda create -n libero python=3.8.13\nconda activate libero\ngit clone https://github.com/Lifelong-Robot-Learning/LIBERO.git\ncd LIBERO\npip install -r requirements.txt\npip install torch==1.11.0+cu113 torchvision==0.12.0+cu113 torchaudio==0.11.0 --extra-index-url https://download.pytorch.org/whl/cu113\npip install -e .\n```\n\n**方式 C：通过 LeRobot**\n```bash\npip install -e \".[libero]\"\n```\n\n无头渲染需设置：`export MUJOCO_GL=egl`\n\n### 1.3 五个 Task Suite\n\n所有任务都是 language-conditioned manipulation，使用 Franka Panda 机械臂。\n\n| Suite | CLI 名称 | 任务数 | 描述 |\n|-------|----------|--------|------|\n| **LIBERO-Spatial** | `libero_spatial` | 10 | 同一目标（拿黑碗放盘子），碗在不同空间位置。测试 **空间关系知识** 迁移 |\n| **LIBERO-Object** | `libero_object` | 10 | 同一目标结构（拿 X 放篮子），不同物体。测试 **物体知识** 迁移 |\n| **LIBERO-Goal** | `libero_goal` | 10 | 同一场景，不同目标（开抽屉、放碗到炉子上等）。测试 **目标/程序知识** 迁移 |\n| **LIBERO-90** | `libero_90` | 90 | LIBERO-100 中的短期任务，跨 spatial/object/goal 的混合分布偏移。用于 **预训练** |\n| **LIBERO-Long** | `libero_10` | 10 | LIBERO-100 中的长期多步骤任务。用于预训练后的 **下游评测** |\n\n**LIBERO-Spatial 示例任务（全部 10 个）：**\n1. pick_up_the_black_bowl_between_the_plate_and_the_ramekin_and_place_it_on_the_plate\n2. pick_up_the_black_bowl_next_to_the_ramekin_and_place_it_on_the_plate\n3. pick_up_the_black_bowl_from_table_center_and_place_it_on_the_plate\n4. pick_up_the_black_bowl_on_the_cookie_box_and_place_it_on_the_plate\n5. pick_up_the_black_bowl_in_the_top_drawer_of_the_wooden_cabinet_and_place_it_on_the_plate\n6. pick_up_the_black_bowl_on_the_ramekin_and_place_it_on_the_plate\n7. pick_up_the_black_bowl_next_to_the_cookie_box_and_place_it_on_the_plate\n8. pick_up_the_black_bowl_on_the_stove_and_place_it_on_the_plate\n9. pick_up_the_black_bowl_next_to_the_plate_and_place_it_on_the_plate\n10. pick_up_the_black_bowl_on_the_wooden_cabinet_and_place_it_on_the_plate\n\n**LIBERO-Object 示例任务：** pick_up_the_{alphabet_soup, cream_cheese, salad_dressing, bbq_sauce, ketchup, tomato_sauce, butter, milk, chocolate_pudding, orange_juice}_and_place_it_in_the_basket\n\n**LIBERO-Goal 示例任务：** open_the_middle_drawer_of_the_cabinet, put_the_bowl_on_the_stove, put_the_wine_bottle_on_top_of_the_cabinet, open_the_top_drawer_and_put_the_bowl_inside, put_the_bowl_on_top_of_the_cabinet, push_the_plate_to_the_front_of_the_stove, put_the_cream_cheese_in_the_bowl, turn_on_the_stove, put_the_bowl_on_the_plate, put_the_wine_bottle_on_the_rack\n\n### 1.4 数据下载\n\n每个任务有 **50 条人类遥操作演示**，通过 SpaceMouse 以 20 Hz 采集。\n\n**方式 A：官方脚本**\n```bash\n# 全部下载\npython benchmark_scripts/download_libero_datasets.py\n\n# 下载特定 suite\npython benchmark_scripts/download_libero_datasets.py --datasets libero_spatial\npython benchmark_scripts/download_libero_datasets.py --datasets libero_object\npython benchmark_scripts/download_libero_datasets.py --datasets libero_goal\npython benchmark_scripts/download_libero_datasets.py --datasets libero_100  # 含 libero_90 + libero_10\n\n# 通过 HuggingFace 下载（推荐，原始链接可能过期）\npython benchmark_scripts/download_libero_datasets.py --use-huggingface\n```\n\n默认下载位置：LIBERO 根目录下的 `./datasets/`\n\n**方式 B：HuggingFace 直接下载**\n\n| 数据集 | 格式 | 大小 |\n|--------|------|------|\n| `yifengzhu-hf/LIBERO-datasets` | 原始 HDF5 | ~100 GB 总计 |\n| `physical-intelligence/libero` | LeRobot (Parquet) | ~34.9 GB |\n| `HuggingFaceVLA/libero` | LeRobot | ~1.9 GB |\n| `lerobot/libero` | LeRobot (视频 AV1) | ~1.94 GB |\n\n**各 suite 近似大小（原始 HDF5 格式）：**\n\n| Suite | 大小 |\n|-------|------|\n| libero_spatial | ~6.6 GB |\n| libero_object | ~9.3 GB |\n| libero_goal | ~6-9 GB |\n| libero_10 (Long) | ~12.8 GB |\n| libero_90 | ~60-70 GB |\n| **总计** | **~100 GB** |\n\n### 1.5 数据格式\n\n**文件格式：** HDF5（每个任务一个 `.hdf5` 文件）\n\n**HDF5 结构：**\n```\ndata/\n  demo_0/\n    obs/\n      agentview_rgb          # (T, 128, 128, 3) uint8 — 第三人称相机\n      eye_in_hand_rgb        # (T, 128, 128, 3) uint8 — 腕部相机\n      gripper_states         # (T, 1) — 夹爪开合度\n      joint_states           # (T, 7) — 7 个关节角度\n      ee_states              # (T, 6) — 末端执行器位置 + 轴角朝向\n      ee_pos                 # (T, 3) — 末端执行器 xyz 位置\n      ee_ori                 # (T, 3) — 末端执行器轴角朝向\n    actions                  # (T, 7) — 7-DOF 动作\n    states                   # (T, D) — 完整模拟器状态\n    robot_states             # (T, D) — gripper_pos + ee_pos + ee_quat 拼接\n    rewards                  # (T,) — 稀疏: 全 0，最后成功步为 1\n    dones                    # (T,) — episode 结束时为 1\n  demo_1/ ...\n  demo_49/ ...\n```\n\n**观测空间：**\n\n| 键 | 维度 | 含义 |\n|----|------|------|\n| `agentview_rgb` (→ `agentview_image`) | (128, 128, 3) | 工作区 RGB 图像 |\n| `eye_in_hand_rgb` (→ `robot0_eye_in_hand_image`) | (128, 128, 3) | 腕部 RGB 图像 |\n| `gripper_states` (→ `robot0_gripper_qpos`) | (1,) 或 (2,) | 夹爪指位置 |\n| `joint_states` (→ `robot0_joint_pos`) | (7,) | Franka Panda 7 关节角 |\n| `ee_pos` | (3,) | 末端执行器 xyz 位置 |\n| `ee_ori` | (3,) | 末端执行器轴角朝向 |\n\n**LeRobot 格式中** proprioceptive state 为 8 维：`observation.state` = [ee_pos (3) + ee_axis_angle (3) + gripper_qpos (2)]\n\n**动作空间：**\n\n| 维度 | 含义 |\n|------|------|\n| 0-2 | 末端执行器位置增量 (dx, dy, dz) |\n| 3-5 | 末端执行器朝向增量 (轴角 / 欧拉角) |\n| 6 | 夹爪命令 (1=闭合, -1=打开) |\n\n- 总计 **7 维连续动作**，Box(-1, 1, shape=(7,))\n- 控制模式：**OSC_POSE**（操作空间控制）\n- 频率：**20 Hz**（原始），LeRobot 格式 **10 Hz**\n- 支持 `relative`（增量，默认）和 `absolute` 两种控制模式\n- 奖励：稀疏 — 中间步全 0，任务完成时 +1\n\n### 1.6 评测\n\n**原生 LIBERO 评测：**\n\n```bash\npython libero/lifelong/evaluate.py \\\n  --benchmark LIBERO_SPATIAL \\\n  --task_id 0 \\\n  --algo base \\\n  --policy bc_transformer_policy \\\n  --seed 10000 \\\n  --ep 50 \\\n  --load_task 0 \\\n  --device_id 0\n```\n\n参数说明：\n- `--benchmark`: `LIBERO_SPATIAL` / `LIBERO_OBJECT` / `LIBERO_GOAL` / `LIBERO_90` / `LIBERO_10`\n- `--task_id`: suite 内的任务索引\n- `--algo`: 终身学习算法 (`base`, `er`, `ewc`, `packnet`, `multitask`)\n- `--policy`: 策略架构 (`bc_rnn_policy`, `bc_transformer_policy`, `bc_vilt_policy`)\n- `--save-videos`: 可选，录制评测视频\n\n**评测协议：**\n- 20 个并行环境同时运行 (`n_eval: 20`, `num_procs: 20`)\n- 每个 episode 最多 600 步 (`max_steps: 600`)\n- 开头 5 步零动作用于物理稳定\n- episode 在 `done=True` 或达到最大步数时终止\n\n**输出指标：**\n- **Success rate** = num_success / num_envs（每个任务）\n- **Loss** = 测试集损失\n- 结果保存路径：`{save_dir}/{benchmark}_{algo}_{policy}_{seed}_[ep|load]_{task_id}.stats`\n\n**终身学习指标（跨任务序列）：**\n- **FWT (Forward Transfer)**: 序列训练后在新任务上的成功率\n- **NBT (Negative Backward Transfer)**: 早期任务性能退化（灾难性遗忘）\n- **AUC (Area Under Curve)**: 综合 FWT 和 NBT 的累积成功率\n\n**原生训练命令：**\n```bash\nexport CUDA_VISIBLE_DEVICES=0 && \\\nexport MUJOCO_EGL_DEVICE_ID=0 && \\\npython libero/lifelong/main.py seed=10000 \\\n  benchmark_name=LIBERO_SPATIAL \\\n  policy=bc_transformer_policy \\\n  lifelong=base\n```\n\n**LeRobot 评测：**\n```bash\nlerobot-eval \\\n  --policy.path=\"your-policy-id\" \\\n  --env.type=libero \\\n  --env.task=libero_spatial,libero_object,libero_goal,libero_10 \\\n  --eval.batch_size=1 \\\n  --eval.n_episodes=10 \\\n  --env.max_parallel_tasks=1\n```\n标准协议：每个任务 10 个 episode，4 个标准 suite = 400 个 episode。\n\n---\n\n## 2. LIBERO-Plus 扰动评测\n\n### 2.1 基本信息\n\n| 项目 | 内容 |\n|------|------|\n| 论文 | [LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-Action Models](https://arxiv.org/abs/2510.13626) (CVPR 2026) |\n| GitHub | https://github.com/sylvestf/LIBERO-plus |\n| 项目主页 | https://sylvestf.github.io/LIBERO-plus/ |\n| HF 资产 | https://huggingface.co/datasets/Sylvest/LIBERO-plus |\n| 训练数据 (RLDS) | https://huggingface.co/datasets/Sylvest/libero_plus_rlds |\n| LeRobot 格式 | https://huggingface.co/datasets/lerobot/libero_plus |\n\n### 2.2 LIBERO-Plus 是什么\n\n在原始 LIBERO 基础上增加了：\n- **10,030 个任务变体**，通过系统化扰动生成\n- **7 个扰动维度**，**21 个子维度**\n- **5 个难度级别** (L1-L5)，按多模型共识分层（4 个参考模型中几个能解决该任务）\n- **20,000+ 训练轨迹**（RLDS 格式）\n- 与 vanilla LIBERO 完全兼容的 drop-in replacement\n\n### 2.3 七个扰动维度（精确定义）\n\n#### 2.3.1 物体布局 (Objects Layout)\n- **O1 — 干扰物体 (Confounding objects):** 从 416 个物体池中随机添加 n 个未见过的干扰物体，通过修改 BDDL 任务描述文件实现\n- **O2 — 目标位移 (Target displacement):** 对目标物体初始位置 (x, y, z) 和朝向施加随机扰动，保持语义关系\n\n#### 2.3.2 相机视角 (Camera Viewpoints)\n- **C1 — 距离缩放 (Distance scaling):** 沿光轴将相机距离缩放 1.01x-2.00x\n- **C2 — 球坐标位置 (Spherical position):** 改变方位角 (delta-theta) 和仰角 (delta-phi)，范围 15-75 度\n- **C3 — 朝向扰动 (Orientation perturbation):** 扰动 yaw/pitch/roll，范围 2-10 度\n\n实现：修改 `Problem` 类接口；主要针对第三人称相机（非腕部相机）\n\n#### 2.3.3 机器人初始状态 (Robot Initial States)\n- 对机械臂初始关节位置施加随机扰动，幅度 0.1-0.5\n- 实现：修改 `Problem` 类接口\n\n#### 2.3.4 语言指令 (Language Instructions)\n- **R1 — 干扰改写 (Distraction rewrites):** 添加与任务无关的上下文信息\n- **R2 — 常识替换 (Commonsense substitution):** 用常识性替代描述替换物体名称\n- **R3 — 推理复杂度 (Reasoning complexity):** 改变多步骤任务的推理复杂度\n- 实现：基于 LLM 的指令改写\n\n#### 2.3.5 光照条件 (Light Conditions)\n- **L1 — 漫射颜色 (Diffuse color):** RGB 通道漫射光照调整\n- **L2 — 方向 (Direction):** 平行光源方向变化\n- **L3 — 镜面强度 (Specular intensity):** 镜面高光强度（反射表面）\n- **L4 — 阴影 (Shadow casting):** 阴影开关控制\n- 实现：修改 MuJoCo 场景 XML 定义文件，注册新场景类\n\n#### 2.3.6 背景纹理 (Background Textures)\n- **B1 — 场景纹理 (Scene texture):** 使用 950 张精选纹理通过 XML 场景文件替换环境纹理\n- **B2 — 表面纹理 (Surface texture):** 随机改变工作表面纹理（桌面、地板）\n- 实现：修改 XML 场景定义文件，添加新纹理资产\n\n#### 2.3.7 传感器噪声 (Sensor Noise)\n图像空间后处理（非物理层级）：\n- **N1 — 运动模糊 (Motion blur):** kernel 半径 r=5-35，高斯 sigma=2-20，角度 U(-45, 45)度\n- **N2 — 高斯模糊 (Gaussian blur):** sigma 1-10\n- **N3 — 缩放模糊 (Zoom blur):** 缩放因子 [s_min, s_max, step] 从 [1, 1.11, 0.01] 到 [1, 1.56, 0.03]\n- **N4 — 雾 (Fog):** 密度 alpha=0.5-5.0，衰减率 beta=1.3-3.0\n- **N5 — 毛玻璃模糊 (Glass blur):** sigma=0.5-2.5，像素位移 delta=1-5，迭代 1-3 次\n\n### 2.4 难度级别 (L1-L5)\n\n按 4 个参考模型（OpenVLA-OFT, pi0, pi0-fast, UniVLA）能否解决分层：\n- L1: 4 个都能解决\n- L2: 3 个能解决\n- L3: 2 个能解决\n- L4: 1 个能解决\n- L5: 无一能解决\n\n### 2.5 安装和运行\n\n**安装：**\n```bash\n# 系统依赖\nsudo apt install libexpat1 libfontconfig1-dev libmagickwand-dev\n\n# 克隆安装\ngit clone https://github.com/sylvestf/LIBERO-plus.git\ncd LIBERO-plus\npip install -e .\npip install -r extra_requirements.txt\n\n# 如果已装 vanilla LIBERO，需先卸载\npip uninstall -y hf-libero\n\nexport MUJOCO_GL=egl\n```\n\n**下载资产：**\n\n从 [HuggingFace](https://huggingface.co/datasets/Sylvest/LIBERO-plus/tree/main) 下载 `assets.zip`，解压到 `LIBERO-plus/libero/libero/assets/`。\n\n期望结构：\n```\nlibero/libero/assets/\n├── articulated_objects/\n├── new_objects/\n├── scenes/\n├── stable_hope_objects/\n├── stable_scanned_objects/\n├── textures/\n├── turbosquid_objects/\n├── serving_region.xml\n├── wall_frames.stl\n└── wall.xml\n```\n\n**配置：** 检查 `/root/.libero/config.yaml`。评测时设 `num_trials_per_task: 1`。\n\n任务到扰动类别映射：`.libero/libero/benchmark/task_classification.json`\n\n**LeRobot 评测：**\n```bash\nlerobot-eval \\\n  --policy.path=\"your-policy-id\" \\\n  --env.type=libero_plus \\\n  --env.task=libero_spatial,libero_object,libero_goal,libero_10 \\\n  --eval.batch_size=1 \\\n  --eval.n_episodes=10 \\\n  --env.max_parallel_tasks=1\n```\n\n### 2.6 与标准 LIBERO 的关系\n\nLIBERO-Plus 是 vanilla LIBERO 的 **drop-in replacement**：\n- 安装在同一个 `libero` Python 包名下（替换原版）\n- 相同的 `LiberoEnv` gym 接口\n- 相同的相机名称 (`agentview_image`, `robot0_eye_in_hand_image`)\n- 相同的观测/动作格式\n- 相同的 task suite 名称\n- **不能同时安装 vanilla LIBERO 和 LIBERO-Plus**，切换需要先卸载再安装\n\n---\n\n## 3. 数据增强相关\n\n### 3.1 robosuite 内置随机化\n\nLIBERO 基于 robosuite (MuJoCo)，robosuite 提供了 `DomainRandomizationWrapper` 和三个 Modder 类，可用于任何 robosuite 环境包括 LIBERO。\n\n**DomainRandomizationWrapper：**\n```python\nfrom robosuite.wrappers import DomainRandomizationWrapper\n\nenv = DomainRandomizationWrapper(\n    env=base_env,\n    seed=42,\n    randomize_color=True,        # 几何体/纹理颜色随机化\n    randomize_camera=True,       # 相机位置/朝向/FOV\n    randomize_lighting=True,     # 光源位置/方向/颜色\n    randomize_dynamics=True,     # 物理参数\n    randomize_on_reset=True,     # episode 重置时随机化\n    randomize_every_n_steps=1,   # rollout 中的频率\n)\n```\n\n**CameraModder（内置）：**\n- 位置扰动：默认 size 0.01\n- 旋转扰动（四元数）：默认 size 0.087 (~5 度)\n- FOV 扰动：默认 size 5.0 度\n\n**LightingModder（内置）：**\n- 位置扰动：默认 size 0.1\n- 方向扰动：默认 size 0.35\n- 镜面/环境光/漫射扰动：默认 size 0.1\n- 开关控制：on/off\n\n**TextureModder（内置）：**\n- RGB 颜色随机化 (local interpolation 0.1)\n- 纹理模式：RGB, checker, noise, gradient\n- 材质属性：反射率、光泽度、镜面反射 (local interpolation 0.2)\n- 天空盒随机化（可选）\n\nDemo 脚本：`robosuite/demos/demo_domain_randomization.py`\n\n### 3.2 LIBERO-Plus 扰动可否复用为训练时数据增强\n\n**可以，且论文已经这样做了。** LIBERO-Plus 同时提供评测任务和训练数据集：\n\n**已提供的训练数据：**\n- **22,400 条训练轨迹**（过滤后 20,000+），在各种扰动条件下生成\n- 分布：2,400 物体布局变体 + 各 4,000 光照/相机/背景/语言/噪声维度\n- RLDS 格式存储，LeRobot 格式见 `lerobot/libero_plus`\n- 论文证明混合 SFT (mix-SFT) 训练显著提升鲁棒性：OpenVLA-OFT+ 平均 79.6%\n\n**三条数据增强路径：**\n\n**路径 A — 直接使用 LIBERO-Plus 训练数据：**\n```bash\nlerobot-train \\\n    --policy.type=smolvla \\\n    --dataset.repo_id=lerobot/libero_plus \\\n    --env.type=libero_plus \\\n    ...\n```\n\n**路径 B — 使用 robosuite 内置 DomainRandomizationWrapper 在线增强：**\n```python\nfrom robosuite.wrappers import DomainRandomizationWrapper\nenv = DomainRandomizationWrapper(\n    env=libero_env,\n    randomize_camera=True,\n    randomize_lighting=True,\n    randomize_color=True\n)\n```\n在线随机化，每 N 步应用随机扰动。适合训练时增强但可控性较低。\n\n**路径 C — 复用 LIBERO-Plus 扰动代码做自定义增强：**\n- 光照/纹理扰动：修改场景 XML + 注册新场景\n- 相机扰动：修改 `Problem` 类接口\n- 传感器噪声 (N1-N5)：纯图像空间后处理，可直接作为标准数据增强应用于任何存储轨迹，无需重新渲染\n\n**关键区别：**\n- robosuite 内置随机化（路径 B）是 **在线** 的，可控性低\n- LIBERO-Plus 扰动（路径 C）是 **结构化** 的，有明确参数范围和难度分层，更适合系统性鲁棒性训练\n- 传感器噪声 (N1-N5) 是纯图像后处理，可以零成本复用为数据增强\n\n---\n\n## 4. 与 LeRobot 的集成\n\n### 4.1 原生支持\n\nLeRobot **原生支持** LIBERO，是一级基准测试环境。\n\n安装：`pip install -e \".[libero]\"`\n\n文档：https://huggingface.co/docs/lerobot/en/libero\n\nHuggingFace 维护了 LIBERO fork：https://github.com/huggingface/lerobot-libero\n\n### 4.2 HuggingFace Hub 数据集\n\n**主要数据集（推荐用于训练）：**\n\n| 数据集 ID | Episodes | 任务数 | 大小 | 说明 |\n|-----------|----------|--------|------|------|\n| `HuggingFaceVLA/libero` | 148 | 10 | ~1.9 GB | 官方预处理数据集，LeRobot 文档推荐 |\n| `lerobot/libero` | 1,693 | 40 | ~1.94 GB | 4 个标准 suite 合并（视频格式, AV1 编码） |\n| `physical-intelligence/libero` | 147 | 10 | ~34.9 GB | PI 的转换版本, RLDS 来源, CC-BY-4.0 |\n| `lerobot/libero_plus` | — | — | — | LIBERO-Plus 训练数据 |\n\n**每个 suite 的图像数据集：**\n\n| 数据集 ID | 任务数 |\n|-----------|--------|\n| `lerobot/libero_10_image` | 10 |\n| `lerobot/libero_object_image` | 10 |\n| `lerobot/libero_spatial_image` | 10 |\n| `lerobot/libero_goal_image` | 10 |\n\n**社区数据集：**\n- `IPEC-COMMUNITY/libero_90_no_noops_lerobot` — LIBERO-90 去除 no-op 版本\n\n### 4.3 数据格式映射\n\n| LIBERO 字段 | LeRobot 特征 | 类型 | 形状 |\n|-------------|-------------|------|------|\n| `agentview_image` | `observation.images.image` | Video/Image | (256, 256, 3) |\n| `robot0_eye_in_hand_image` | `observation.images.image2` | Video/Image | (256, 256, 3) |\n| `observation[\"state\"]` | `observation.state` | float32 | (8,) |\n| `action` | `action` | float32 | (7,) |\n| `language_instruction` | `task` (task_index) | string/int | — |\n\nLeRobot 元数据：robot_type=`panda`，fps=`10`，视频编码=AV1 yuv420p，表格数据用 Parquet 存储\n\n### 4.4 转换脚本\n\n**方式 A：Physical Intelligence 的 OpenPI 转换脚本（主要）**\n\n脚本路径：[`Physical-Intelligence/openpi/examples/libero/convert_libero_data_to_lerobot.py`](https://github.com/Physical-Intelligence/openpi/blob/main/examples/libero/convert_libero_data_to_lerobot.py)\n\n```bash\n# 前置依赖\nuv pip install tensorflow tensorflow_datasets\n\n# 原始数据来源\n# https://huggingface.co/datasets/openvla/modified_libero_rlds\n\n# 执行转换\nuv run examples/libero/convert_libero_data_to_lerobot.py \\\n  --data_dir /path/to/your/data \\\n  --push_to_hub\n```\n\n处理流程：\n1. 读取 4 个 RLDS 数据集：`libero_10_no_noops`, `libero_goal_no_noops`, `libero_object_no_noops`, `libero_spatial_no_noops`\n2. 创建 `LeRobotDataset`，robot_type=panda, fps=10\n3. 逐 episode 迭代，每步调用 `dataset.add_frame()`\n4. 每个 episode 调用 `dataset.save_episode()`\n5. 可选推送到 HuggingFace Hub\n\n处理时间：约 30 分钟\n\n**方式 B：通用 HDF5 → LeRobot 转换器**\n\n仓库：https://github.com/anarnuri/hdf5_to_lerobot_converter\n\n支持 LIBERO 原生 HDF5 格式。\n\n**方式 C：直接使用预转换数据集（无需转换）**\n\n```python\nfrom lerobot.common.datasets.lerobot_dataset import LeRobotDataset\n\ndataset = LeRobotDataset(\"HuggingFaceVLA/libero\")\n# 或\ndataset = LeRobotDataset(\"lerobot/libero\")\n```\n\n### 4.5 端到端训练和评测示例\n\n**训练：**\n```bash\nlerobot-train \\\n  --policy.type=smolvla \\\n  --policy.repo_id=${HF_USER}/libero-test \\\n  --policy.load_vlm_weights=true \\\n  --dataset.repo_id=HuggingFaceVLA/libero \\\n  --env.type=libero \\\n  --env.task=libero_10 \\\n  --output_dir=./outputs/ \\\n  --steps=100000 \\\n  --batch_size=4 \\\n  --eval.batch_size=1 \\\n  --eval.n_episodes=1 \\\n  --eval_freq=1000\n```\n\n**评测：**\n```bash\nlerobot-eval \\\n  --policy.path=\"your-policy-id\" \\\n  --env.type=libero \\\n  --env.task=libero_spatial,libero_object,libero_goal,libero_10 \\\n  --eval.batch_size=1 \\\n  --eval.n_episodes=10 \\\n  --env.max_parallel_tasks=1\n```\n\n---\n\n## 5. 关键注意事项\n\n1. **LIBERO-90 数据** 不在标准预转换数据集中。需要用 OpenPI 转换脚本或社区数据集 `IPEC-COMMUNITY/libero_90_no_noops_lerobot`\n2. **控制模式** (`relative` vs `absolute`) 必须与策略的动作参数化匹配\n3. **vanilla LIBERO 和 LIBERO-Plus 不能同时安装**，两者共用同一 Python 包名\n4. LeRobot 中 LIBERO 仅支持 Linux（MuJoCo 渲染需 EGL）\n5. LeRobot 格式的图像分辨率为 256x256，而原始 LIBERO 为 128x128 [UNVERIFIED — 需确认是否做了上采样或 LeRobot 环境重新渲染]\n6. 原始 LIBERO 采集频率 20Hz，LeRobot 格式为 10Hz（可能做了下采样）[UNVERIFIED — 需确认具体降频策略]\n"
  }
}
````

</details>

---

### Tool result

_source line 158 · 2026-05-15T11:18:42.246946+00:00_

File created successfully at: /home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/action_cond_info_bottleneck/artifacts/research_libero_benchmark.md

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_libero-benchmark_20260515T111137",
  "tool": "Write",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 159 · 2026-05-15T11:18:42.247155+00:00_

报告已写入 `artifacts/research_libero_benchmark.md`。

覆盖的内容：
- **LIBERO Benchmark**：GitHub/安装/5 个 task suite 详情/HDF5 数据格式（观测 128x128 双相机 + 7D 关节 + 6D EE，动作 7D OSC_POSE）/评测脚本命令和指标（success rate, FWT, NBT, AUC）
- **LIBERO-Plus**：实际是 7 个扰动维度 21 个子维度（不只是 4 个），含物体布局/相机/机器人初态/语言指令/光照/背景纹理/传感器噪声，CVPR 2026 论文，drop-in replacement 架构
- **数据增强**：robosuite 内置 DomainRandomizationWrapper + 三个 Modder 可直接用；LIBERO-Plus 同时提供 22,400 条增强训练轨迹；传感器噪声为纯图像后处理可零成本复用
- **LeRobot 集成**：原生支持，HuggingFace 上有 `lerobot/libero`、`HuggingFaceVLA/libero` 等预转换数据集，附 OpenPI 转换脚本路径

两处标注了 `[UNVERIFIED]`：LeRobot 格式图像分辨率（256 vs 128）和采样率降频策略。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_research_libero-benchmark_20260515T111137"
}
```

</details>

---
