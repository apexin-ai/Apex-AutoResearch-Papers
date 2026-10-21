# research nora bib entry

**Instruction Routing in Fine-Tuned Vision-Language-Action Models: A Cross-Architecture Analysis** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 13
- **Recorded user turns:** 0
- **Tool calls:** 6
- **Original source:** `logs/chats/worker_research_nora_bib_entry_20260522T061000.jsonl`
- **Structured JSON:** [`6893f8e493106b9adfab.json`](../../sessions/68/6893f8e493106b9adfab.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

13 recorded events

### Tool call

_source line 1 · 2026-05-22T06:10:47.454291+00:00_

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
  "session": "worker_research_nora_bib_entry_20260522T061000",
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

_source line 2 · 2026-05-22T06:10:47.454627+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_nora_bib_entry_20260522T061000",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-22T06:10:47.454795+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "NORA VLA Qwen2.5-VL robot action model paper"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_nora_bib_entry_20260522T061000",
  "tool": "WebSearch",
  "tool_args": {
    "query": "NORA VLA Qwen2.5-VL robot action model paper"
  }
}
```

</details>

---

### Tool call

_source line 4 · 2026-05-22T06:10:47.454951+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "NoRA vision language action model robotic manipulation arXiv"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_nora_bib_entry_20260522T061000",
  "tool": "WebSearch",
  "tool_args": {
    "query": "NoRA vision language action model robotic manipulation arXiv"
  }
}
```

</details>

---

### Tool result

_source line 5 · 2026-05-22T06:10:47.455165+00:00_

Web search results for query: "NORA VLA Qwen2.5-VL robot action model paper"

Links: [{"title":"[Literature Review] NORA: A Small Open-Sourced Generalist Vision Language Action Model for Embodied Tasks","url":"https://www.themoonlight.io/en/review/nora-a-small-open-sourced-generalist-vision-language-action-model-for-embodied-tasks"},{"title":"Paper page - NORA: A Small Open-Sourced Generalist Vision Language Action Model for Embodied Tasks","url":"https://huggingface.co/papers/2504.19854"},{"title":"NORA: A Small Open-Sourced Generalist Vision Language Action Model for Embodied Tasks","url":"https://arxiv.org/html/2504.19854v1"},{"title":"NORA: A Small Open-Sourced Generalist Vision Language Action Model for Embodied Tasks - Paper Details","url":"https://www.chatpaper.ai/dashboard/paper/3970d274-9357-4a8c-96d4-0c0734d618f8"},{"title":"NORA: A Small Open-Sourced Generalist Vision Language Action Model for   Embodied Tasks","url":"https://arxiv.org/pdf/2504.19854"},{"title":"NORA-1.5: A Vision-Language-Action Model Trained using World Model- and Action-based Preference Rewards","url":"https://arxiv.org/html/2511.14659v1"},{"title":"[2504.19854] NORA: A Small Open-Sourced Generalist Vision Language Action Model for Embodied Tasks","url":"https://arxiv.org/abs/2504.19854"},{"title":"NORA: A Small Open-Sourced Generalist Vision Language Action Model for Embodied Tasks","url":"https://declare-lab.github.io/nora"},{"title":"GitHub - ehaller00/NORA-VLA: NORA: A Small Open-Sourced Generalist Vision Language Action Model for Embodied Tasks · GitHub","url":"https://github.com/ehaller00/NORA-VLA"},{"title":"declare-lab/nora · Hugging Face","url":"https://huggingface.co/declare-lab/nora"}]

Based on the search results, here's information about the NORA VLA Qwen2.5-VL robot action model paper:

## Overview

NORA is a 3B-parameter Visual-Language-Action (VLA) model designed for embodied tasks, aiming to reduce computational overhead while maintaining strong task performance.

## T
…[truncated 936 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_nora_bib_entry_20260522T061000",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-22T06:10:47.455344+00:00_

Web search results for query: "NoRA vision language action model robotic manipulation arXiv"

Links: [{"title":"NORA: A Small Open-Sourced Generalist Vision Language Action Model for Embodied Tasks","url":"https://arxiv.org/html/2504.19854v1"},{"title":"[2507.10672] Vision Language Action Models in Robotic Manipulation: A Systematic Review","url":"https://arxiv.org/abs/2507.10672"},{"title":"Vision Language Action Models in Robotic Manipulation: A Systematic Review","url":"https://arxiv.org/html/2507.10672v1"},{"title":"Language-Grounded Decoupled Action Representation for Robotic Manipulation","url":"https://arxiv.org/pdf/2603.12967"},{"title":"Global Prior Meets Local Consistency: Dual-Memory Augmented Vision-Language-Action Model for Efficient Robotic Manipulation","url":"https://arxiv.org/pdf/2602.20200"},{"title":"CogACT: A Foundational Vision-Language-Action Model for Synergizing   Cognition and Action in Robotic Manipulation","url":"https://arxiv.org/pdf/2411.19650"},{"title":"LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-Action Models","url":"https://arxiv.org/html/2510.13626v3"}]

Based on the search results, I found information about NoRA (NORA):

NORA is a 3B-parameter Visual-Language-Action (VLA) model designed to optimize robotic task execution by reducing computational overhead and improving efficiency. NORA is trained on the Open X-Embodiment dataset, which incorporates diverse robotic embodiments and tasks.

NORA demonstrates significant superiority in policy generation over baseline models across three types of tasks: out-of-domain object grasping, tasks requiring spatial reasoning, and multi-object grasping. Specifically, NORA achieves impressive success rates in OOD/zero-shot object grasping tasks, such as "put the carrot in pot" and "put banana in pot" with a success rate of up to 90%.

The paper appears to have been published on arXiv on April 28, 2025 (arXiv:2504.19854), and it presents NORA as a small, open-sourced generalist vi
…[truncated 157 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_nora_bib_entry_20260522T061000",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-22T06:10:47.455506+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "arxiv 2504.19854 NORA authors list"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_nora_bib_entry_20260522T061000",
  "tool": "WebSearch",
  "tool_args": {
    "query": "arxiv 2504.19854 NORA authors list"
  }
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-22T06:10:47.455686+00:00_

Web search results for query: "arxiv 2504.19854 NORA authors list"

Links: [{"title":"[2504.19854] NORA: A Small Open-Sourced Generalist Vision Language Action Model for Embodied Tasks","url":"https://arxiv.org/abs/2504.19854"},{"title":"NORA: A Small Open-Sourced Generalist Vision Language Action Model for Embodied Tasks","url":"https://arxiv.org/html/2504.19854"},{"title":"Performance of o1 pro and GPT-4 in self-assessment questions for nephrology board renewal","url":"https://www.medrxiv.org/content/10.1101/2025.01.14.25320525.full.pdf"},{"title":"DNN-Aided Block Sparse Bayesian Learning for User Activity Detection and   Channel Estimation in Grant-Free Non-Orthogonal Random Access","url":"https://arxiv.org/pdf/1910.02953"},{"title":"Correction: Testing the ELSA Birth App During Pregnancy and Labor for Primiparous Women: Randomized Controlled Trial","url":"https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12551930/"},{"title":"Correction to: Risk conditions in children hospitalized with influenza in Norway, 2017–2019","url":"https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7898737/"},{"title":"No difference in risk of hospitalisation between reported cases of the SARS-CoV-2 Delta variant and Alpha variant in Norway","url":"https://www.medrxiv.org/content/10.1101/2021.09.02.21263014.full.pdf"}]

Based on the search results, the authors of arXiv paper 2504.19854 (NORA: A Small Open-Sourced Generalist Vision Language Action Model for Embodied Tasks) are: Chia-Yu Hung, Qi Sun, Pengfei Hong, Amir Zadeh, Chuan Li, U-Xuan Tan, Navonil Majumder, and Soujanya Poria.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_nora_bib_entry_20260522T061000",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-22T06:10:47.455835+00:00_

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
  "session": "worker_research_nora_bib_entry_20260522T061000",
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

_source line 10 · 2026-05-22T06:10:47.456002+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_nora_bib_entry_20260522T061000",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-22T06:10:47.456153+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://arxiv.org/abs/2504.19854",
  "prompt": "Extract the exact full list of authors and the exact paper title. Also confirm the arXiv ID and submission date/year."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_nora_bib_entry_20260522T061000",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://arxiv.org/abs/2504.19854",
    "prompt": "Extract the exact full list of authors and the exact paper title. Also confirm the arXiv ID and submission date/year."
  }
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-22T06:10:47.456292+00:00_

# Paper Details

**Title:** "NORA: A Small Open-Sourced Generalist Vision Language Action Model for Embodied Tasks"

**Authors:**
1. Chia-Yu Hung
2. Qi Sun
3. Pengfei Hong
4. Amir Zadeh
5. Chuan Li
6. U-Xuan Tan
7. Navonil Majumder
8. Soujanya Poria

**arXiv ID:** 2504.19854

**Submission Date:** April 28, 2025

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_nora_bib_entry_20260522T061000",
  "tool": "WebFetch",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 13 · 2026-05-22T06:10:47.456454+00:00_

```bibtex
@article{hung2025nora,
  title={{NORA}: A Small Open-Sourced Generalist Vision Language Action Model for Embodied Tasks},
  author={Hung, Chia-Yu and Sun, Qi and Hong, Pengfei and Zadeh, Amir and Li, Chuan and Tan, U-Xuan and Majumder, Navonil and Poria, Soujanya},
  journal={arXiv preprint arXiv:2504.19854},
  year={2025}
}
```

arXiv ID: 2504.19854，2025年4月发表，来自 DeCLaRe Lab (Soujanya Poria 组)。基于 Qwen2.5-VL-3B，3B 参数，用 FAST+ tokenizer 在 970k 真实机器人示范上训练。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_research_nora_bib_entry_20260522T061000"
}
```

</details>

---
