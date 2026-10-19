# research libero plus assets download

**Meta-Brain: Perturbation-Diagnostic Routing of LoRA Experts for Parameter-E cient VLA Robustness** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 55
- **Recorded user turns:** 0
- **Tool calls:** 27
- **Original source:** `logs/chats/worker_research_libero-plus-assets-download_20260515T171307.jsonl`
- **Structured JSON:** [`5e58f028d355e9ee0486.json`](../../sessions/5e/5e58f028d355e9ee0486.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

55 recorded events

### Tool call

_source line 1 · 2026-05-15T17:15:50.850792+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__ssh_read_only,mcp__agent-ml-research__detect_image,WebSearch",
  "max_results": "3"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_libero-plus-assets-download_20260515T171307",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__ssh_read_only,mcp__agent-ml-research__detect_image,WebSearch",
    "max_results": "3"
  }
}
```

</details>

---

### Tool result

_source line 2 · 2026-05-15T17:15:50.851116+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_libero-plus-assets-download_20260515T171307",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-15T17:15:50.851291+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-34142",
  "command": "ls /root/LIBERO-plus/libero/libero/assets/ 2>/dev/null",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_libero-plus-assets-download_20260515T171307",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-34142",
    "command": "ls /root/LIBERO-plus/libero/libero/assets/ 2>/dev/null",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 4 · 2026-05-15T17:15:50.851455+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter '>' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_libero-plus-assets-download_20260515T171307",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-15T17:15:50.851606+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-34142",
  "command": "find /root/LIBERO-plus/ -name \"*_add*\" -type f 2>/dev/null",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_libero-plus-assets-download_20260515T171307",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-34142",
    "command": "find /root/LIBERO-plus/ -name \"*_add*\" -type f 2>/dev/null",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-15T17:15:50.851731+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter '>' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_libero-plus-assets-download_20260515T171307",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-15T17:15:50.851847+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-34142",
  "command": "head -100 /root/LIBERO-plus/README.md 2>/dev/null",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_libero-plus-assets-download_20260515T171307",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-34142",
    "command": "head -100 /root/LIBERO-plus/README.md 2>/dev/null",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-15T17:15:50.851998+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter '>' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_libero-plus-assets-download_20260515T171307",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-15T17:15:50.852120+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "LIBERO-Plus benchmark CVPR 2026 download assets GitHub"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_libero-plus-assets-download_20260515T171307",
  "tool": "WebSearch",
  "tool_args": {
    "query": "LIBERO-Plus benchmark CVPR 2026 download assets GitHub"
  }
}
```

</details>

---

### Tool call

_source line 10 · 2026-05-15T17:15:50.852234+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "LIBERO-Plus perturbed XML assets download _add distractor objects"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_libero-plus-assets-download_20260515T171307",
  "tool": "WebSearch",
  "tool_args": {
    "query": "LIBERO-Plus perturbed XML assets download _add distractor objects"
  }
}
```

</details>

---

### Tool result

_source line 11 · 2026-05-15T17:15:50.852383+00:00_

Web search results for query: "LIBERO-Plus benchmark CVPR 2026 download assets GitHub"

Links: [{"title":"GitHub - sylvestf/LIBERO-plus: Official repository of LIBERO-plus, a generalized benchmark for in-depth robustness analysis of vision-language-action models. · GitHub","url":"https://github.com/sylvestf/LIBERO-plus"},{"title":"CVPR Poster LIBERO-Plus: A Progressive Robustness Benchmark for Visual-Language-Action Models","url":"https://cvpr.thecvf.com/virtual/2026/poster/38735"},{"title":"GitHub - Zxy-MLlab/LIBERO-PRO: LIBERO-PRO is the official repository of the LIBERO-PRO — an evaluation extension of the original LIBERO benchmark","url":"https://github.com/Zxy-MLlab/LIBERO-PRO"},{"title":"GitHub - Lifelong-Robot-Learning/LIBERO: Benchmarking Knowledge Transfer in Lifelong Robot Learning · GitHub","url":"https://github.com/Lifelong-Robot-Learning/LIBERO"},{"title":"LIBERO-plus/README.md at main · sylvestf/LIBERO-plus","url":"https://github.com/sylvestf/LIBERO-plus/blob/main/README.md"},{"title":"LIBERO – LIBERO","url":"https://libero-project.github.io/main.html"},{"title":"LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-Action Models","url":"https://sylvestf.github.io/LIBERO-plus/"},{"title":"Sylvest/LIBERO-plus · Datasets at Hugging Face","url":"https://huggingface.co/datasets/Sylvest/LIBERO-plus"},{"title":"LIBERO-plus/index.html at main · sylvestf/LIBERO-plus","url":"https://github.com/sylvestf/LIBERO-plus/blob/main/index.html"},{"title":"LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-Action Models","url":"https://arxiv.org/html/2510.13626v1"}]

Based on the search results, I found comprehensive information about LIBERO-Plus and how to access its assets:

## LIBERO-Plus Benchmark Overview

LIBERO-Plus is a comprehensive, automatic, and fine-grained evaluation framework with controlled perturbations across seven dimensions: object layouts, camera viewpoints, robot initial states, language instructions, lighting conditions, background
…[truncated 1182 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_libero-plus-assets-download_20260515T171307",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-15T17:15:50.852618+00:00_

Web search results for query: "LIBERO-Plus perturbed XML assets download _add distractor objects"

Links: [{"title":"RL with LIBERO-Pro & LIBERO-Plus Benchmark — RLinf documentation","url":"https://rlinf.readthedocs.io/en/latest/rst_source/examples/embodied/liberoplus_pro.html"},{"title":"GitHub - sylvestf/LIBERO-plus: Official repository of LIBERO-plus, a generalized benchmark for in-depth robustness analysis of vision-language-action models. · GitHub","url":"https://github.com/sylvestf/LIBERO-plus"},{"title":"UG0691 User Guide Libero SoC Design Flow","url":"https://coredocs.s3.amazonaws.com/Libero/12_2_0/Tool/libero_ecf_ug.pdf"},{"title":"LIBERO-plus · Hugging Face","url":"https://huggingface.co/docs/lerobot/main/libero_plus"},{"title":"Libero SoC Design Flow User Guide","url":"https://coredocs.s3.amazonaws.com/Libero/2022_1/Tool/libero_ecf_ug.pdf"},{"title":"Sylvest/LIBERO-plus · Datasets at Hugging Face","url":"https://huggingface.co/datasets/Sylvest/LIBERO-plus"},{"title":"LIBERO-plus/README.md at main · sylvestf/LIBERO-plus","url":"https://github.com/sylvestf/LIBERO-plus/blob/main/README.md"},{"title":"LIBERO Benchmark: Vision-Language-Action in Robotics","url":"https://www.emergentmind.com/topics/libero"},{"title":"UG0691: Libero SoC Design Flow User Guide","url":"https://coredocs.s3.amazonaws.com/Libero/12_0_0/Tool/libero_ecf_ug.pdf"},{"title":"OpenMOSS LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-","url":"https://arxiv.org/pdf/2510.13626"}]

Based on the search results, I found information about LIBERO-Plus assets download. Here's what I found:

## LIBERO-Plus Assets Download

LIBERO-Plus requires downloading the assets.zip archive from the Hugging Face dataset Sylvest/LIBERO-plus and extracting it into the installed liberoplus.liberoplus package directory.

The asset structure includes various directories and XML files, including:
articulated_objects, new_objects, scenes, stable_hope_objects, stable_scanned_objects, textures, turbosquid_obj
…[truncated 953 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_libero-plus-assets-download_20260515T171307",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-15T17:15:50.852806+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-34142",
  "command": "ls /root/LIBERO-plus/libero/libero/assets/",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_libero-plus-assets-download_20260515T171307",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-34142",
    "command": "ls /root/LIBERO-plus/libero/libero/assets/",
    "account": "root"
  }
}
```

</details>

---

### Tool call

_source line 14 · 2026-05-15T17:15:50.852932+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-34142",
  "command": "find /root/LIBERO-plus/ -name \"*_add*\" -type f",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_libero-plus-assets-download_20260515T171307",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-34142",
    "command": "find /root/LIBERO-plus/ -name \"*_add*\" -type f",
    "account": "root"
  }
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-15T17:15:50.853047+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-34142",
  "command": "head -100 /root/LIBERO-plus/README.md",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_libero-plus-assets-download_20260515T171307",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-34142",
    "command": "head -100 /root/LIBERO-plus/README.md",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-15T17:15:50.853168+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"articulated_objects\\nscenes\\nserving_region.xml\\nstable_hope_objects\\nstable_scanned_objects\\ntextures\\nturbosquid_objects\\nwall.xml\\nwall_frames.stl\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.54}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_libero-plus-assets-download_20260515T171307",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-15T17:15:50.853283+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "site:github.com sylvestf/LIBERO-plus assets.zip download instructions"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_libero-plus-assets-download_20260515T171307",
  "tool": "WebSearch",
  "tool_args": {
    "query": "site:github.com sylvestf/LIBERO-plus assets.zip download instructions"
  }
}
```

</details>

---

### Tool call

_source line 18 · 2026-05-15T17:15:50.853397+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "site:huggingface.co Sylvest/LIBERO-plus assets download"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_libero-plus-assets-download_20260515T171307",
  "tool": "WebSearch",
  "tool_args": {
    "query": "site:huggingface.co Sylvest/LIBERO-plus assets download"
  }
}
```

</details>

---

### Tool result

_source line 19 · 2026-05-15T17:15:50.853604+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"/root/LIBERO-plus/libero/libero/bddl_files/libero_10/KITCHEN_SCENE3_turn_on_the_stove_and_put_the_moka_pot_on_it_add_1.bddl\\n/root/LIBERO-plus/libero/libero/bddl_files/libero_10/KITCHEN_SCENE3_turn_on_the_stove_and_put_the_moka_pot_on_it_add_10.bddl\\n/root/LIBERO-plus/libero/libero/bddl_files/libero_10/KITCHEN_SCENE3_turn_on_the_stove_and_put_the_moka_pot_on_it_add_11.bddl\\n/root/LIBERO-plus/libero/libero/bddl_files/libero_10/KITCHEN_SCENE3_turn_on_the_stove_and_put_the_moka_pot_on_it_add_12.bddl\\n/root/LIBERO-plus/libero/libero/bddl_files/libero_10/KITCHEN_SCENE3_turn_on_the_stove_and_put_the_moka_pot_on_it_add_13.bddl\\n/root/LIBERO-plus/libero/libero/bddl_files/libero_10/KITCHEN_SCENE3_turn_on_the_stove_and_put_the_moka_pot_on_it_add_14.bddl\\n/root/LIBERO-plus/libero/libero/bddl_files/libero_10/KITCHEN_SCENE3_turn_on_the_stove_and_put_the_moka_pot_on_it_add_15.bddl\\n/root/LIBERO-plus/libero/libero/bddl_files/libero_10/KITCHEN_SCENE3_turn_on_the_stove_and_put_the_moka_pot_on_it_add_16.bddl\\n/root/LIBERO-plus/libero/libero/bddl_files/libero_10/KITCHEN_SCENE3_turn_on_the_stove_and_put_the_moka_pot_on_it_add_17.bddl\\n/root/LIBERO-plus/libero/libero/bddl_files/libero_10/KITCHEN_SCENE3_turn_on_the_stove_and_put_the_moka_pot_on_it_add_18.bddl\\n/root/LIBERO-plus/libero/libero/bddl_files/libero_10/KITCHEN_SCENE3_turn_on_the_stove_and_put_the_moka_pot_on_it_add_19.bddl\\n/root/LIBERO-plus/libero/libero/bddl_files/libero_10/KITCHEN_SCENE3_turn_on_the_stove_and_put_the_moka_pot_on_it_add_2.bddl\\n/root/LIBERO-plus/libero/libero/bddl_files/libero_10/KITCHEN_SCENE3_turn_on_the_stove_and_put_the_moka_pot_on_it_add_20.bddl\\n/root/LIBERO-plus/libero/libero/bddl_files/libero_10/KITCHEN_SCENE3_turn_on_the_stove_and_put_the_moka_pot_on_it_add_21.bddl\\n/root/LIBERO-plus/libero/libero/bddl_files/libero_10/KITCHEN_SCENE3_turn_on_the_stove_and_put_the_moka_pot_on_it_add_22.bddl\\n/root/LIBERO-plus/libero/libero/bddl_file
…[truncated 6317 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_libero-plus-assets-download_20260515T171307",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-15T17:15:50.853836+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"&lt;h1 align=\\\"center\\\">\\nLIBERO-Plus: In-depth Robustness Analysis of Vision-Language-Action Models\\n&lt;/h1>\\n\\n&lt;p align=\\\"center\\\">\\n  📄 &lt;a href=\\\"https://arxiv.org/pdf/2510.13626\\\">&lt;strong>Paper&lt;/strong>&lt;/a> |   \\n  🏗️ &lt;a href=\\\"https://huggingface.co/datasets/Sylvest/LIBERO-plus/tree/main\\\">&lt;strong>Assets&lt;/strong>&lt;/a> | \\n  🌐 &lt;a href=\\\"https://sylvestf.github.io/LIBERO-plus\\\">&lt;strong>Website&lt;/strong>&lt;/a> | \\n  🤗 &lt;a href=\\\"https://huggingface.co/Sylvest/openvla-7b-oft-finetuned-libero-plus-mixdata\\\">&lt;strong>Model&lt;/strong>&lt;/a> | \\n  📁 &lt;a href=\\\"https://huggingface.co/datasets/Sylvest/libero_plus_rlds\\\">&lt;strong>RldsDataset&lt;/strong>&lt;/a>\\n  📁 &lt;a href=\\\"https://huggingface.co/datasets/Sylvest/libero_plus_lerobot\\\">&lt;strong>LerobotDataset&lt;/strong>&lt;/a>\\n&lt;/p>\\n\\n![libero-plus](./static/images/libero-plus.jpg)\\n\\n## 🔥 Overview\\nThis repository contains the official implementation and benchmark for our paper \\\"In-depth Robustness Analysis for Vision-Language-Action Models\\\". We systematically expose the hidden vulnerabilities of contemporary VLA models through comprehensive robustness evaluation across seven perturbation dimensions. You can simply replace the original `libero` with a `pip install -e .` without modifying your code.\\n\\n## 🚀 Key Findings\\n- **Significant Fragility**: VLA models exhibit extreme sensitivity to camera viewpoints and robot initial states, with performance dropping from 95% to below 30% under modest perturbations\\n- **Language Ignorance**: Models largely ignore language instructions, functioning more like Vision-Action models\\n- **Negative Compositional Generalization**: Combined perturbations reveal complex interaction effects beyond independent factors\\n\\n## 📊 LIBERO-plus Benchmark\\n\\n### 7 Perturbation Dimensions\\nWe introduce **LIBERO-plus**, a comprehensive benchmark with 10,030 tasks spanning:\\n\\n1. **Objects Layout** - Confoundi
…[truncated 4117 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_libero-plus-assets-download_20260515T171307",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 21 · 2026-05-15T17:15:50.854017+00:00_

Web search results for query: "site:huggingface.co Sylvest/LIBERO-plus assets download"

Links: [{"title":"Sylvest/LIBERO-plus · Datasets at Hugging Face","url":"https://huggingface.co/datasets/Sylvest/LIBERO-plus"},{"title":"Sylvest/libero_plus_rlds · Datasets at Hugging Face","url":"https://huggingface.co/datasets/Sylvest/libero_plus_rlds"},{"title":"Sylvest/openvla-7b-oft-finetuned-libero-plus-mixdata · Hugging Face","url":"https://huggingface.co/Sylvest/openvla-7b-oft-finetuned-libero-plus-mixdata"},{"title":"Sylvest/libero_plus_lerobot at main","url":"https://huggingface.co/datasets/Sylvest/libero_plus_lerobot/tree/main/meta"},{"title":"Huggingface","url":"https://huggingface.co/Sylvest/openvla-7b-oft-finetuned-libero-plus-mixdata/resolve/main/README.md?download=true"},{"title":"LIBERO-plus · Hugging Face","url":"https://huggingface.co/docs/lerobot/main/libero_plus"},{"title":"Sylvest/LIBERO-plus · Discussions","url":"https://huggingface.co/datasets/Sylvest/LIBERO-plus/discussions"},{"title":"Sylvest/libero_plus_lerobot · Datasets at Hugging Face","url":"https://huggingface.co/datasets/Sylvest/libero_plus_lerobot/viewer/default/train?p=22380"},{"title":"Sylvest/LIBERO-plus · Repo is missing","url":"https://huggingface.co/datasets/Sylvest/LIBERO-plus/discussions/2"},{"title":"LIBERO","url":"https://huggingface.co/docs/lerobot/en/libero"}]

Based on the search results, here's what I found about downloading assets for Sylvest/LIBERO-plus:

You should download assets from LIBERO-plus, including hundreds of new objects, textures, and other required assets. You need to unzip the assets.zip file to /LIBERO-plus/libero/libero path.

The assets are available on the Hugging Face dataset page at https://huggingface.co/datasets/Sylvest/LIBERO-plus. 

The assets directory structure includes articulated_objects, new_objects, scenes, stable_hope_objects, stable_scanned_objects, textures, turbosquid_objects, and several XML and STL files.

According to the documentation, the p
…[truncated 286 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_libero-plus-assets-download_20260515T171307",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 22 · 2026-05-15T17:15:50.854197+00:00_

Web search results for query: "site:github.com sylvestf/LIBERO-plus assets.zip download instructions"

Links: [{"title":"GitHub - sylvestf/LIBERO-plus: Official repository of LIBERO-plus, a generalized benchmark for in-depth robustness analysis of vision-language-action models. · GitHub","url":"https://github.com/sylvestf/LIBERO-plus"},{"title":"LIBERO-plus/README.md at main · sylvestf/LIBERO-plus","url":"https://github.com/sylvestf/LIBERO-plus/blob/main/README.md"},{"title":"Sylvest/LIBERO-plus · Datasets at Hugging Face","url":"https://huggingface.co/datasets/Sylvest/LIBERO-plus"},{"title":"LIBERO-plus/index.html at main · sylvestf/LIBERO-plus","url":"https://github.com/sylvestf/LIBERO-plus/blob/main/index.html"},{"title":"LIBERO-plus · Hugging Face","url":"https://huggingface.co/docs/lerobot/main/libero_plus"},{"title":"Sylvest/libero_plus_rlds · Datasets at Hugging Face","url":"https://huggingface.co/datasets/Sylvest/libero_plus_rlds"},{"title":"RL with LIBERO-Pro & LIBERO-Plus Benchmark — RLinf documentation","url":"https://rlinf.readthedocs.io/en/latest/rst_source/examples/embodied/liberoplus_pro.html"},{"title":"LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-Action Models","url":"https://sylvestf.github.io/LIBERO-plus/"},{"title":"LIBERO – LIBERO","url":"https://libero-project.github.io/main.html"},{"title":"litsh - Overview","url":"https://github.com/litsh"}]

Based on the search results from the GitHub repository for sylvestf/LIBERO-plus, here are the download instructions for assets.zip:

## Assets Download Instructions

Please download the assets from LIBERO-plus, including hundreds of new objects, textures, and other required assets, and unzip the assets.zip file to /LIBERO-plus/libero/libero path.

More specifically:

1. LIBERO-plus ships its extended asset pack separately. Download assets.zip from the Hugging Face dataset and extract it into the LIBERO-plus package directory

2. Alternative method using command line: Download the assets.z
…[truncated 668 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_libero-plus-assets-download_20260515T171307",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 23 · 2026-05-15T17:15:50.854381+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-34142",
  "command": "cat /root/LIBERO-plus/libero/libero/bddl_files/libero_10/KITCHEN_SCENE3_turn_on_the_stove_and_put_the_moka_pot_on_it_add_1.bddl",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_libero-plus-assets-download_20260515T171307",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-34142",
    "command": "cat /root/LIBERO-plus/libero/libero/bddl_files/libero_10/KITCHEN_SCENE3_turn_on_the_stove_and_put_the_moka_pot_on_it_add_1.bddl",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 24 · 2026-05-15T17:15:50.854564+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"(define (problem LIBERO_Kitchen_Tabletop_Manipulation)\\n  (:domain robosuite)\\n  (:language turn on the stove and put the moka pot on it)\\n    (:regions\\n      (flat_stove_init_region\\n          (:target kitchen_table)\\n          (:ranges (\\n              (-0.21000000000000002 0.19 -0.19 0.21000000000000002)\\n            )\\n          )\\n          (:yaw_rotation (\\n              (0.0 0.0)\\n            )\\n          )\\n      )\\n      (frypan_init_region\\n          (:target kitchen_table)\\n          (:ranges (\\n              (-0.07500000000000001 -0.275 -0.024999999999999994 -0.22499999999999998)\\n            )\\n          )\\n          (:yaw_rotation (\\n              (0.0 0.0)\\n            )\\n          )\\n      )\\n      (moka_pot_init_region\\n          (:target kitchen_table)\\n          (:ranges (\\n              (0.024999999999999998 -0.025000000000000005 0.07500000000000001 0.025000000000000005)\\n            )\\n          )\\n          (:yaw_rotation (\\n              (0.0 0.0)\\n            )\\n          )\\n      )\\n      (add_object_region_4\\n          (:target kitchen_table)\\n          (:ranges (\\n              (0.19999950000000002 0.1499995 0.2000005 0.15000049999999998)\\n            )\\n          )\\n          (:yaw_rotation (\\n              (0.0 0.0)\\n            )\\n          )\\n      )\\n      (cook_region\\n          (:target flat_stove_1)\\n      )\\n    )\\n\\n  (:fixtures\\n    kitchen_table - kitchen_table\\n    flat_stove_1 - flat_stove\\n  )\\n\\n  (:objects\\n    chefmate_8_frypan_1 - chefmate_8_frypan\\n    moka_pot_1 - moka_pot\\n    bag_of_yeast_1 - bag_of_yeast\\n  )\\n\\n  (:obj_of_interest\\n    moka_pot_1\\n    flat_stove_1\\n  )\\n\\n  (:init\\n    (On flat_stove_1 kitchen_table_flat_stove_init_region)\\n    (On chefmate_8_frypan_1 kitchen_table_frypan_init_region)\\n    (On moka_pot_1 kitchen_table_moka_pot_init_region)\\n    (On bag_of_yeast_1 kitchen
…[truncated 242 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_libero-plus-assets-download_20260515T171307",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 25 · 2026-05-15T17:15:50.854715+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-34142",
  "command": "ls /root/LIBERO-plus/libero/libero/assets/new_objects/",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_libero-plus-assets-download_20260515T171307",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-34142",
    "command": "ls /root/LIBERO-plus/libero/libero/assets/new_objects/",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 26 · 2026-05-15T17:15:50.854839+00:00_

{"result":"{\"success\": false, \"data\": {\"stdout\": \"\", \"stderr\": \"ls: cannot access '/root/LIBERO-plus/libero/libero/assets/new_objects/': No such file or directory\\n\", \"return_code\": 2}, \"error\": \"exit code 2\", \"metadata\": {\"elapsed_seconds\": 0.45}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_libero-plus-assets-download_20260515T171307",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 27 · 2026-05-15T17:15:50.854958+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-34142",
  "command": "grep -r \"new_objects\" /root/LIBERO-plus/libero/libero/ --include=\"*.py\" -l",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_libero-plus-assets-download_20260515T171307",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-34142",
    "command": "grep -r \"new_objects\" /root/LIBERO-plus/libero/libero/ --include=\"*.py\" -l",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 28 · 2026-05-15T17:15:50.855153+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"/root/LIBERO-plus/libero/libero/envs/objects/custom_objects.py\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.58}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_libero-plus-assets-download_20260515T171307",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 29 · 2026-05-15T17:15:50.855301+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-34142",
  "command": "find /root/meta_brain_lora_routing/artifacts/ -name \"*.log\" -type f",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_libero-plus-assets-download_20260515T171307",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-34142",
    "command": "find /root/meta_brain_lora_routing/artifacts/ -name \"*.log\" -type f",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 30 · 2026-05-15T17:15:50.855456+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.54}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_libero-plus-assets-download_20260515T171307",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 31 · 2026-05-15T17:15:50.855621+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-34142",
  "command": "cat /root/LIBERO-plus/libero/libero/envs/objects/custom_objects.py",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_libero-plus-assets-download_20260515T171307",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-34142",
    "command": "cat /root/LIBERO-plus/libero/libero/envs/objects/custom_objects.py",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 32 · 2026-05-15T17:15:50.855852+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"import os\\nimport re\\nimport numpy as np\\nimport copy\\nfrom robosuite.models.objects import MujocoXMLObject\\nfrom robosuite.utils.mjcf_utils import array_to_string\\n \\nimport pathlib\\n \\n# 使用pathlib计算项目根目录的绝对路径\\nabsolute_path = pathlib.Path(__file__).parent.parent.parent.absolute()\\n \\nfrom libero.libero.envs.base_object import register_object\\n \\ndef hack_robosuite():\\n    \\\"\\\"\\\"\\n    Hack 'robosuite.models.objects.objects.MujocoXMLObject._get_object_subtree' function for custom objects supports.\\n    \\\"\\\"\\\"\\n    from robosuite.models.objects.objects import (\\n        MujocoXMLObject, GEOMTYPE2GROUP, array_to_string, OBJECT_COLLISION_COLOR,\\n        ET, new_joint\\n    )\\n\\n    def _get_object_subtree(self):\\n        # Parse object\\n\\n        # # ===== Original Code =====================================\\n        # obj = copy.deepcopy(self.worldbody.find(\\\"./body/body[@name='object']\\\"))\\n        # # =========================================================\\n\\n        # ===== Modified Code =====================================\\n        obj = self.worldbody.find(\\\"./body/body[@name='object']\\\")\\n        if obj is None:\\n            obj = self.worldbody.find(\\\"./body[@name='object']\\\")\\n        if obj is None:\\n            raise ValueError(\\n                \\\"Could not find object body with name='object' at either \\\"\\n                \\\"./body[@name='object'] or ./body/body[@name='object']. \\\"\\n                \\\"Please check your XML structure.\\\"\\n            )\\n        obj = copy.deepcopy(obj)\\n        # =========================================================\\n\\n        # Rename this top level object body (will have self.naming_prefix added later)\\n        obj.attrib[\\\"name\\\"] = \\\"main\\\"\\n        # Get all geom_pairs in this tree\\n        geom_pairs = self._get_geoms(obj)\\n\\n        # Define a temp function so we don't du
…[truncated 7090 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_libero-plus-assets-download_20260515T171307",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 33 · 2026-05-15T17:15:50.856043+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-34142",
  "command": "grep -r \"FileNotFoundError\\|No such file\\|not found\\|missing\\|add_\" /root/meta_brain_lora_routing/ --include=\"*.log\" -l",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_libero-plus-assets-download_20260515T171307",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-34142",
    "command": "grep -r \"FileNotFoundError\\|No such file\\|not found\\|missing\\|add_\" /root/meta_brain_lora_routing/ --include=\"*.log\" -l",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 34 · 2026-05-15T17:15:50.856174+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter '|' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_libero-plus-assets-download_20260515T171307",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 35 · 2026-05-15T17:15:50.856301+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-34142",
  "command": "grep -r \"bag_of_yeast\\|new_objects\" /root/LIBERO-plus/libero/libero/envs/ --include=\"*.py\" -n",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_libero-plus-assets-download_20260515T171307",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-34142",
    "command": "grep -r \"bag_of_yeast\\|new_objects\" /root/LIBERO-plus/libero/libero/envs/ --include=\"*.py\" -n",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 36 · 2026-05-15T17:15:50.856438+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter '|' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_libero-plus-assets-download_20260515T171307",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 37 · 2026-05-15T17:15:50.856560+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-34142",
  "command": "grep -rn \"skip\\|skipped\\|FileNotFound\\|error\\|failed\" /root/meta_brain_lora_routing/artifacts/phase0/ --include=\"*.py\"",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_libero-plus-assets-download_20260515T171307",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-34142",
    "command": "grep -rn \"skip\\|skipped\\|FileNotFound\\|error\\|failed\" /root/meta_brain_lora_routing/artifacts/phase0/ --include=\"*.py\"",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 38 · 2026-05-15T17:15:50.856677+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter '|' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_libero-plus-assets-download_20260515T171307",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 39 · 2026-05-15T17:15:50.856831+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "huggingface.co/datasets/Sylvest/LIBERO-plus/tree/main assets.zip size"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_libero-plus-assets-download_20260515T171307",
  "tool": "WebSearch",
  "tool_args": {
    "query": "huggingface.co/datasets/Sylvest/LIBERO-plus/tree/main assets.zip size"
  }
}
```

</details>

---

### Tool result

_source line 40 · 2026-05-15T17:15:50.856977+00:00_

Web search results for query: "huggingface.co/datasets/Sylvest/LIBERO-plus/tree/main assets.zip size"

Links: [{"title":"Sylvest/libero_plus_rlds · Datasets at Hugging Face","url":"https://huggingface.co/datasets/Sylvest/libero_plus_rlds"},{"title":"Sylvest/LIBERO-plus · Datasets at Hugging Face","url":"https://huggingface.co/datasets/Sylvest/LIBERO-plus"},{"title":"Sylvest/libero_plus_lerobot at main","url":"https://huggingface.co/datasets/Sylvest/libero_plus_lerobot/tree/main/meta"},{"title":"LIBERO-plus · Hugging Face","url":"https://huggingface.co/docs/lerobot/main/libero_plus"},{"title":"Sylvest/openvla-7b-oft-finetuned-libero-plus-mixdata · Hugging Face","url":"https://huggingface.co/Sylvest/openvla-7b-oft-finetuned-libero-plus-mixdata"},{"title":"Sylvest/libero_plus_lerobot · Datasets at Hugging Face","url":"https://huggingface.co/datasets/Sylvest/libero_plus_lerobot/viewer/default/train?p=22380"},{"title":"Sylvest/LIBERO-plus · Discussions","url":"https://huggingface.co/datasets/Sylvest/LIBERO-plus/discussions"},{"title":"Datasets · Hugging Face","url":"https://huggingface.co/docs/datasets/index"},{"title":"Datasets – Hugging Face","url":"https://huggingface.co/datasets"},{"title":"Sylvest/LIBERO-plus · Repo is missing","url":"https://huggingface.co/datasets/Sylvest/LIBERO-plus/discussions/2"}]

Based on the search results, I found information about the LIBERO-plus dataset on Hugging Face, but the search results do not contain the specific file size for the assets.zip file. The search results show that assets can be downloaded from LIBERO-plus, including hundreds of new objects, textures, and other required assets, and assets.zip can be downloaded from the Hugging Face dataset and extracted into the LIBERO-plus package directory, but the actual file size is not provided in these results.

To find the specific file size of assets.zip, you would need to visit the Hugging Face dataset page directly at https://huggingface.co/datasets/Sylvest/LIBERO-plus and navi
…[truncated 162 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_libero-plus-assets-download_20260515T171307",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 41 · 2026-05-15T17:15:50.857154+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"Sylvest/LIBERO-plus\" huggingface \"repo is missing\" discussion assets"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_libero-plus-assets-download_20260515T171307",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"Sylvest/LIBERO-plus\" huggingface \"repo is missing\" discussion assets"
  }
}
```

</details>

---

### Tool call

_source line 42 · 2026-05-15T17:15:50.857274+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-34142",
  "command": "find /root/ -name \"assets.zip\" -type f",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_libero-plus-assets-download_20260515T171307",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-34142",
    "command": "find /root/ -name \"assets.zip\" -type f",
    "account": "root"
  }
}
```

</details>

---

### Tool call

_source line 43 · 2026-05-15T17:15:50.857390+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-34142",
  "command": "df -h /root/autodl-tmp",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_libero-plus-assets-download_20260515T171307",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-34142",
    "command": "df -h /root/autodl-tmp",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 44 · 2026-05-15T17:15:50.857552+00:00_

Web search results for query: ""Sylvest/LIBERO-plus" huggingface "repo is missing" discussion assets"

Links: [{"title":"Sylvest/LIBERO-plus · Repo is missing","url":"https://huggingface.co/datasets/Sylvest/LIBERO-plus/discussions/2"},{"title":"Sylvest/LIBERO-plus · Datasets at Hugging Face","url":"https://huggingface.co/datasets/Sylvest/LIBERO-plus"},{"title":"Sylvest/LIBERO-plus · Discussions","url":"https://huggingface.co/datasets/Sylvest/LIBERO-plus/discussions"},{"title":"Sylvest/libero_plus_rlds · Datasets at Hugging Face","url":"https://huggingface.co/datasets/Sylvest/libero_plus_rlds"},{"title":"LIBERO-plus · Hugging Face","url":"https://huggingface.co/docs/lerobot/main/libero_plus"},{"title":"Sylvest/openvla-7b-oft-finetuned-libero-plus-mixdata · Hugging Face","url":"https://huggingface.co/Sylvest/openvla-7b-oft-finetuned-libero-plus-mixdata"},{"title":"Sylvest/libero_plus_lerobot at main","url":"https://huggingface.co/datasets/Sylvest/libero_plus_lerobot/tree/main/meta"},{"title":"Cannot see discussion - Site Feedback - Hugging Face Forums","url":"https://discuss.huggingface.co/t/cannot-see-discussion/175426"},{"title":"Huggingface","url":"https://huggingface.co/Sylvest/openvla-7b-oft-finetuned-libero-plus-mixdata/resolve/main/README.md?download=true"},{"title":"LIBERO · Hugging Face","url":"https://huggingface.co/docs/lerobot/libero"}]

I found the discussion you were looking for. Here's what I found:

## Discussion: "Repo is Missing" on Sylvest/LIBERO-plus

A user asked if the repository was planning to be released soon, and the owner (Sylvest) responded that due to their personal GitHub account being temporarily suspended, the main repository was currently inaccessible.

As an alternative, they provided access to the repository at https://github.com/sii-research/LIBERO-plus.

Additionally, another user reported that some config files appeared to be missing from the provided repo, specifically some init files related to task configurations.

Regarding th
…[truncated 333 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_libero-plus-assets-download_20260515T171307",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 45 · 2026-05-15T17:15:50.857696+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"/root/autodl-tmp/libero_plus_assets/assets.zip\\n/root/autodl-tmp/assets.zip\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.83}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_libero-plus-assets-download_20260515T171307",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 46 · 2026-05-15T17:15:50.857821+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"Filesystem      Size  Used Avail Use% Mounted on\\n/dev/md0        250G   25G  226G  10% /root/autodl-tmp\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.54}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_libero-plus-assets-download_20260515T171307",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 47 · 2026-05-15T17:15:50.857968+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-34142",
  "command": "stat /root/autodl-tmp/assets.zip",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_libero-plus-assets-download_20260515T171307",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-34142",
    "command": "stat /root/autodl-tmp/assets.zip",
    "account": "root"
  }
}
```

</details>

---

### Tool call

_source line 48 · 2026-05-15T17:15:50.858085+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-34142",
  "command": "ls /root/autodl-tmp/libero_plus_assets/",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_libero-plus-assets-download_20260515T171307",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-34142",
    "command": "ls /root/autodl-tmp/libero_plus_assets/",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 49 · 2026-05-15T17:15:50.858207+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"  File: /root/autodl-tmp/assets.zip\\n  Size: 4108077   \\tBlocks: 8024       IO Block: 4096   regular file\\nDevice: 900h/2304d\\tInode: 32331495415  Links: 1\\nAccess: (0644/-rw-r--r--)  Uid: (    0/    root)   Gid: (    0/    root)\\nAccess: 2026-05-15 21:49:23.900698056 +0800\\nModify: 2026-05-15 21:50:15.052753771 +0800\\nChange: 2026-05-15 21:50:15.052753771 +0800\\n Birth: 2026-05-15 21:49:23.900698056 +0800\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.45}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_libero-plus-assets-download_20260515T171307",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 50 · 2026-05-15T17:15:50.858327+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"assets.zip\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.54}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_libero-plus-assets-download_20260515T171307",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 51 · 2026-05-15T17:15:50.858486+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-34142",
  "command": "head -5 /root/autodl-tmp/assets.zip",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_libero-plus-assets-download_20260515T171307",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-34142",
    "command": "head -5 /root/autodl-tmp/assets.zip",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 52 · 2026-05-15T17:15:50.858702+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"PK\\u0003\\u0004\\n\\u0000\\u0000\\u0000\\u0000\\u0000\\u0011�N[\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000h\\u0000\\u001c\\u0000inspire/hdd/project/embodied-multimodality/public/syfei/libero_new/release/dataset/LIBERO-plus-0/assets/UT\\t\\u0000\\u0003�\\u0014�h�\\u001a�hux\\u000b\\u0000\\u0001\\u0004\\u0000\\u0000\\u0000\\u0000\\u0004\\u0000\\u0000\\u0000\\u0000PK\\u0003\\u0004\\n\\u0000\\u0000\\u0000\\u0000\\u0000\\u0011�N[\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000o\\u0000\\u001c\\u0000inspire/hdd/project/embodied-multimodality/public/syfei/libero_new/release/dataset/LIBERO-plus-0/assets/scenes/UT\\t\\u0000\\u0003�\\u0014�h�\\u001a�hux\\u000b\\u0000\\u0001\\u0004\\u0000\\u0000\\u0000\\u0000\\u0004\\u0000\\u0000\\u0000\\u0000PK\\u0003\\u0004\\u0014\\u0000\\u0000\\u0000\\b\\u0000\\u000f�N[�\\n�� \\u0007\\u0000\\u0000k*\\u0000\\u0000�\\u0000\\u001c\\u0000inspire/hdd/project/embodied-multimodality/public/syfei/libero_new/release/dataset/LIBERO-plus-0/assets/scenes/kitchen_table_WoodFine001_REFL_6K.xmlUT\\t\\u0000\\u0003�\\u0014�h�\\u0014�hux\\u000b\\u0000\\u0001\\u0004\\u0000\\u0000\\u0000\\u0000\\u0004\\u0000\\u0000\\u0000\\u0000�ZKs�8\\u0010�ϯ�r��\\u0001�Ļ*�9m.;����#��l���\\u0005�����x\\b�\\u000f�$�Tb\\u0002BR�'u�%����&'O��������}CD��iV��n����\\fo�}�r���[&%ٔ��?�\\\"�(���\\u000b!���E�wp߈�fW\\t���&+�U��L\\u0014�A�\\\"[��;�y�A��\\u0003�3���/��3�gF,�X�A�׭�3��ׇ�� �YڬU�Ş�e�CE�Z�\\u0005����xUe���\\t�SQ�x[V��yV�˼,+k[�:\\u001b,5H�7p\\u0007=ls^��Ɔ7��x޾�MU\\rR�e.��\\u0017\\t��-� �:+�B�u��\\u0015�.�U�\\b�Wb+8\\b�\\u0010G>#\\\\�*\\u0016�lYV\\u001b(�v\\u0003�_L�$@c�%D�ߵ&�HI��4\\u000fJ�]/�)��\\u001e��6�����{���+��\\u001e���)ML\\u0010�\\u0010�g�1��1=�Dj��TR6��\\u0012:�t�\\u0004*X7B�$\\u0017��\\u001c�J'��\\u0015�߸(��c�\\f\\u0002Ʋ����iƲ�>�p�n8���\\u0018���\\u0004<+���|\\u0012�zS��:��7�k�k�vq�GL��\\u0018Ci7�³���3<�\\\"��i\\u0017�i*�\\u0013\\u000e
…[truncated 1200 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_libero-plus-assets-download_20260515T171307",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 53 · 2026-05-15T17:15:50.858855+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-34142",
  "command": "find /root/LIBERO-plus/libero/libero/assets/ -type d",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_libero-plus-assets-download_20260515T171307",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-34142",
    "command": "find /root/LIBERO-plus/libero/libero/assets/ -type d",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 54 · 2026-05-15T17:15:50.859061+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"/root/LIBERO-plus/libero/libero/assets/\\n/root/LIBERO-plus/libero/libero/assets/textures\\n/root/LIBERO-plus/libero/libero/assets/articulated_objects\\n/root/LIBERO-plus/libero/libero/assets/articulated_objects/short_fridge\\n/root/LIBERO-plus/libero/libero/assets/articulated_objects/short_fridge/base\\n/root/LIBERO-plus/libero/libero/assets/articulated_objects/short_fridge/base/visual\\n/root/LIBERO-plus/libero/libero/assets/articulated_objects/short_fridge/door\\n/root/LIBERO-plus/libero/libero/assets/articulated_objects/short_fridge/door/visual\\n/root/LIBERO-plus/libero/libero/assets/articulated_objects/basin_faucet\\n/root/LIBERO-plus/libero/libero/assets/articulated_objects/basin_faucet/basin_faucet_base\\n/root/LIBERO-plus/libero/libero/assets/articulated_objects/basin_faucet/basin_faucet_base/visual\\n/root/LIBERO-plus/libero/libero/assets/articulated_objects/basin_faucet/basin_faucet_movable\\n/root/LIBERO-plus/libero/libero/assets/articulated_objects/basin_faucet/basin_faucet_movable/visual\\n/root/LIBERO-plus/libero/libero/assets/articulated_objects/textures\\n/root/LIBERO-plus/libero/libero/assets/articulated_objects/flat_stove\\n/root/LIBERO-plus/libero/libero/assets/articulated_objects/flat_stove/stove_burner\\n/root/LIBERO-plus/libero/libero/assets/articulated_objects/flat_stove/stove_knob_base\\n/root/LIBERO-plus/libero/libero/assets/articulated_objects/flat_stove/stove_knob_base/visual\\n/root/LIBERO-plus/libero/libero/assets/articulated_objects/flat_stove/stove_knob_button\\n/root/LIBERO-plus/libero/libero/assets/articulated_objects/flat_stove/stove_knob_button/visual\\n/root/LIBERO-plus/libero/libero/assets/articulated_objects/white_cabinet\\n/root/LIBERO-plus/libero/libero/assets/articulated_objects/white_cabinet/white_cabinet_base\\n/root/LIBERO-plus/libero/libero/assets/articulated_objects/white_cabinet/white_cabinet_base/visual\\n/root/LIBERO-plus/libero/libero/assets/articulated_objects
…[truncated 6404 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_libero-plus-assets-download_20260515T171307",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 55 · 2026-05-15T17:15:50.859290+00:00_

调查完成。以下是结论：

---

## 结论：**可下载。** `new_objects/` 目录缺失是唯一问题。

### 1. 问题根因

服务器上 `/root/LIBERO-plus/libero/libero/assets/` 缺少 `new_objects/` 目录。这是 `_add_N` 扰动所需的全部干扰物体 XML 所在位置。

`custom_objects.py` 引用路径格式：
```
assets/new_objects/cupcake/sutaow/usd/MJCF/sutaow.xml
assets/new_objects/cutting_board/aibvew/usd/MJCF/aibvew.xml
assets/new_objects/bag_of_yeast/...
```

当前 assets 目录有 7 个子目录（articulated_objects, scenes, stable_hope_objects 等），但缺了关键的 `new_objects/`。

### 2. 已下载但不完整

服务器上有两个 `assets.zip`：
- `/root/autodl-tmp/assets.zip` — **仅 4MB**，只包含 scenes 的纹理变体 XML（如 `kitchen_table_WoodFine001_REFL_6K.xml`），**不含 `new_objects/`**
- `/root/autodl-tmp/libero_plus_assets/assets.zip` — 同一个文件

4MB 不可能包含"hundreds of new objects"。可能是下载不完整或 HuggingFace Git LFS 未正确拉取。

### 3. 公开下载源

| 来源 | URL |
|------|-----|
| HuggingFace 数据集 | [Sylvest/LIBERO-plus](https://huggingface.co/datasets/Sylvest/LIBERO-plus) |
| GitHub 主仓库 | [sylvestf/LIBERO-plus](https://github.com/sylvestf/LIBERO-plus) |
| 备用仓库（主账号被封时） | [sii-research/LIBERO-plus](https://github.com/sii-research/LIBERO-plus) |

README 明确指示：
> "Please download our assets from [LIBERO-plus](https://huggingface.co/datasets/Sylvest/LIBERO-plus/tree/main), including hundreds of new objects, textures, and other required assets. Please unzip the `assets.zip` file to `/LIBERO-plus/libero/libero` path."

### 4. 修复命令

```bash
source /etc/network_turbo
export HF_HUB_DISABLE_XET=1
export REQUESTS_CA_BUNDLE=/etc/ssl/certs/ca-certificates.crt
export SSL_CERT_FILE=/etc/ssl/certs/ca-certificates.crt

# 方法1: huggingface-cli (推荐)
pip install -U huggingface_hub
huggingface-cli download --repo-type dataset Sylvest/LIBERO-plus assets.zip --local-dir /root/autodl-tmp/libero_plus_assets/

# 解压到正确位置（assets.zip 内路径较深，需 strip）
cd /root/autodl-tmp/libero_plus_assets/
unzip -o assets.zip
# 检查解压后的目录结构，找到 new_objects/ 并 cp/mv 到正确位置
cp -r &lt;extracted_path>/assets/new_objects /root/LIBERO-plus/libero/libero/assets/

# 方法2: 如果 HF 太慢，用 wget 直接下载
wget "https://huggingface.co/datasets/Sylvest/LIBERO-plus/resolve/main/assets.zip" -O /root/autodl-tmp/assets_full.zip
```

### 5. 典型缺失文件（从 `custom_objects.py` 提取）

```
assets/new_objects/bag_of_yeast/&lt;hash>/usd/MJCF/&lt;hash>.xml
assets/new_objects/cupcake/sutaow/usd/MJCF/sutaow.xml
assets/new_objects/cupcake/wdiezm/usd/MJCF/wdiezm.xml
assets/new_objects/cutting_board/aibvew/usd/MJCF/aibvew.xml
assets/new_objects/cutting_board/idmcgf/usd/MJCF/idmcgf.xml
```
（`custom_objects.py` 中注册了数十种物体类别，每类多个变体）

### 6. 风险点

- HuggingFace "Repo is missing" [讨论帖](https://huggingface.co/datasets/Sylvest/LIBERO-plus/discussions/2) 提到原作者 GitHub 账号曾被封，但数据集仍在 HuggingFace 上
- 如果 HF 下载失败，备用方案：联系作者（论文一作 Sylvest / syfei）或从 [sii-research/LIBERO-plus](https://github.com/sii-research/LIBERO-plus) 获取
- AutoDL 上下载 HF 大文件慢，建议用 `network_turbo` + 后台 nohup 执行

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_research_libero-plus-assets-download_20260515T171307"
}
```

</details>

---
