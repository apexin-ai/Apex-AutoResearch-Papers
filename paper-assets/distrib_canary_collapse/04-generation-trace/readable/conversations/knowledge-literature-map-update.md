# knowledge literature map update

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 9
- **Recorded user turns:** 0
- **Tool calls:** 4
- **Original source:** `logs/chats/worker_knowledge_literature-map-update_20260515T044254.jsonl`
- **Structured JSON:** [`651c92e72785d568f959.json`](../../sessions/65/651c92e72785d568f959.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

9 recorded events

### Tool call

_source line 1 · 2026-05-15T04:43:31.958192+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__save_project_file,WebSearch",
  "max_results": "3"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_knowledge_literature-map-update_20260515T044254",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__save_project_file,WebSearch",
    "max_results": "3"
  }
}
```

</details>

---

### Tool result

_source line 2 · 2026-05-15T04:43:31.958489+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_knowledge_literature-map-update_20260515T044254",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-15T04:43:31.958643+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "distrib_canary_collapse",
  "file": "literature_map.yaml",
  "max_chars": "0"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_knowledge_literature-map-update_20260515T044254",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "distrib_canary_collapse",
    "file": "literature_map.yaml",
    "max_chars": "0"
  }
}
```

</details>

---

### Tool result

_source line 4 · 2026-05-15T04:43:31.959093+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/literature_map.yaml\", \"content\": \"papers:\\n  # ============================================================\\n  # CORE MODEL COLLAPSE\\n  # ============================================================\\n  - id: \\\"shumailov2024curse\\\"\\n    title: \\\"The Curse of Recursion: Training on Generated Data Makes Models Forget\\\"\\n    authors: \\\"Ilia Shumailov, Zakhar Shumaylov, Yiren Zhao, Yarin Gal, Nicolas Papernot, Ross Anderson\\\"\\n    venue: \\\"Nature\\\"\\n    year: 2024\\n    url: \\\"https://arxiv.org/abs/2305.17493\\\"\\n    category: \\\"core-collapse\\\"\\n    role: \\\"foundation\\\"\\n    key_findings:\\n      - \\\"定义 model collapse 现象：迭代用合成数据替换真实数据训练会导致分布尾部消失\\\"\\n      - \\\"区分 early model collapse（尾部信息丢失）和 late model collapse（分布完全收敛）\\\"\\n      - \\\"三类误差来源：statistical approximation, functional expressivity, functional approximation，跨代复合\\\"\\n      - \\\"在 VAE、GMM、LLM 上均验证了 collapse 的普遍性\\\"\\n    relevance_to_us: \\\"奠基论文，定义了我们研究的核心现象。我们的 canary 指标旨在提前检测其描述的 early collapse 阶段\\\"\\n    metrics_studied: [\\\"perplexity\\\", \\\"distributional tail mass\\\"]\\n\\n  - id: \\\"alemohammad2024mad\\\"\\n    title: \\\"Self-Consuming Generative Models Go MAD\\\"\\n    authors: \\\"Sina Alemohammad, Josue Casco-Rodriguez, Lorenzo Luzi, Ahmed Imtiaz Humayun, Hossein Babaei, Daniel LeJeune, Ali Siahkoohi, Richard Baraniuk\\\"\\n    venue: \\\"ICLR 2024\\\"\\n    year: 2024\\n    url: \\\"https://arxiv.org/abs/2307.01850\\\"\\n    category: \\\"core-collapse\\\"\\n    role: \\\"foundation\\\"\\n    key_findings:\\n      - \\\"提出 Model Autophagy Disorder (MAD) 概念\\\"\\n      - \\\"autophagous loop 中没有足够新鲜真实数据时，质量或多样性必然渐进下降\\\"\\n      - \\\"在图像生成领域验证 self-consuming loop 的退化效应\\\"\\n    relevance_to_us: \\\"MAD 框架与我们的 iterative loop 设置直接对应；其 quality vs diversity tradeoff 可能反映在不同 canary 指标上\\\"\\n    metrics_studied:
…[truncated 25927 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_knowledge_literature-map-update_20260515T044254",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-15T04:43:31.959284+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Gambetta surplexity synthetic data model collapse perplexity"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_knowledge_literature-map-update_20260515T044254",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Gambetta surplexity synthetic data model collapse perplexity"
  }
}
```

</details>

---

### Tool call

_source line 6 · 2026-05-15T04:43:31.959424+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Schaeffer position paper model collapse definition framework 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_knowledge_literature-map-update_20260515T044254",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Schaeffer position paper model collapse definition framework 2025"
  }
}
```

</details>

---

### Tool result

_source line 7 · 2026-05-15T04:43:31.959586+00:00_

Web search results for query: "Gambetta surplexity synthetic data model collapse perplexity"

Links: [{"title":"[2410.12341] Learning by Surprise: Surplexity for Mitigating Model Collapse in Generative AI","url":"https://arxiv.org/abs/2410.12341"},{"title":"Learning by Surprise: Surplexity for Mitigating Model Collapse in Generative AI","url":"https://arxiv.org/html/2410.12341"},{"title":"Learning by Surprise: Surplexity for Mitigating Model Collapse in Generative AI","url":"https://www.arxiv.org/pdf/2410.12341v3"},{"title":"Unveiling the Flaws: Exploring Imperfections in Synthetic Data and Mitigation Strategies for Large Language Models","url":"https://arxiv.org/html/2406.12397v1"},{"title":"Perplexity - Evaluation of LLMs Part 1","url":"https://www.linkedin.com/pulse/perplexity-evaluation-llms-part-1-akash-gautam-jnkpc"},{"title":"Beyond Model Collapse: Scaling Up with Synthesized Data Requires Reinforcement","url":"https://arxiv.org/html/2406.07515v1"},{"title":"Models - Perplexity","url":"https://docs.perplexity.ai/docs/sonar/models"},{"title":"Strong Model Collapse","url":"https://arxiv.org/html/2410.04840v1"},{"title":"Multimodal Synthetic Data Finetuning and Model Collapse: Insights from VLMs and Diffusion Models | Proceedings of the 27th International Conference on Multimodal Interaction","url":"https://dl.acm.org/doi/full/10.1145/3716553.3750806"},{"title":"Characterizing Model Collapse in Large Language Models Using Semantic Networks and Next-Token Probability","url":"https://arxiv.org/html/2410.12341v2"}]

Based on the search results, here's what I found about Gambetta, surplexity, synthetic data, model collapse, and perplexity:

## Overview

Daniele Gambetta and colleagues published a paper titled "Learning by Surprise: Surplexity for Mitigating Model Collapse in Generative AI", which addresses a critical challenge in AI model training.

## Model Collapse Problem

As synthetic content increasingly infiltrates the web, generative AI models may be retraine
…[truncated 1304 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_knowledge_literature-map-update_20260515T044254",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-15T04:43:31.959749+00:00_

Web search results for query: "Schaeffer position paper model collapse definition framework 2025"

Links: [{"title":"Position: Model Collapse Does Not Mean What You Think","url":"https://arxiv.org/pdf/2503.03150"},{"title":"[2503.03150] Position: Model Collapse Does Not Mean What You Think","url":"https://arxiv.org/abs/2503.03150"},{"title":"A Closer Look at Model Collapse: From a Generalization-to-Memorization Perspective","url":"https://arxiv.org/html/2509.16499v1"},{"title":"Position: Model Collapse Does Not Mean What You Think Anonymous Author(s)","url":"https://openreview.net/pdf?id=ygfzWIGDN8"},{"title":"Escaping Model Collapse via Synthetic Data Verification: Near-term Improvements and Long-term ConvergenceThis project is supported by the AI2050 program at Schmidt Sciences (Grant G-24-66104) and Army Research Office Award W911NF-23-1-0030. We also thank Cong Ma from UChicago, Hongning Wang and Bo Li from Tsinghua, Pinyan Lu and Gavin Tang from Shanghai University of Finance and Economics for helpful discussions and suggestions.","url":"https://arxiv.org/html/2510.16657v1"},{"title":"Published as a conference paper at ICLR 2025 STRONG MODEL COLLAPSE","url":"https://proceedings.iclr.cc/paper_files/paper/2025/file/284afdc2309f9667d2d4fb9290235b0c-Paper-Conference.pdf"},{"title":"Strong Model Collapse | OpenReview","url":"https://openreview.net/forum?id=et5l9qPUhm"},{"title":"[Literature Review] Position: Model Collapse Does Not Mean What You Think","url":"https://www.themoonlight.io/en/review/position-model-collapse-does-not-mean-what-you-think"},{"title":"1 Introduction","url":"https://arxiv.org/html/2503.03150"},{"title":"[2404.01413] Is Model Collapse Inevitable? Breaking the Curse of Recursion by Accumulating Real and Synthetic Data","url":"https://arxiv.org/abs/2404.01413"}]

Based on my search results, I found information about Rylan Schaeffer's position paper on model collapse.

## Schaeffer's Position Paper on Model Collapse (2025)

Model collapse refers
…[truncated 1807 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_knowledge_literature-map-update_20260515T044254",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 9 · 2026-05-15T04:43:31.959935+00:00_

两篇论文都已经存在于 `literature_map.yaml` 中：

1. **gambetta2024surplexity** — 在 `canary-metrics` 分类下，role 为 `direct-competitor`，包含 surplexity 定义、semantic network 方法、过滤策略等 key findings。
2. **schaeffer2025position** — 在 `core-collapse` 分类下（POSITION / SURVEY / EPISTEMICS 区段），role 为 `background`，包含 8 种 collapse 定义、假设与现实不符等 key findings。

无需重复添加。如果需要更新现有条目的内容（比如修改 role、补充 relevance_to_us 中关于伪回归的论点），请告知。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_knowledge_literature-map-update_20260515T044254"
}
```

</details>

---
