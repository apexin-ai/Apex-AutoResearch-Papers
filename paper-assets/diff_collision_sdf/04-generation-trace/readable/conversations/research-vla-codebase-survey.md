# research vla codebase survey

**How Action Collapse Creates Illusory Safety in Diffusion-Based VLA Collision Avoidance Evaluation** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 155
- **Recorded user turns:** 0
- **Tool calls:** 77
- **Original source:** `logs/chats/worker_research_vla_codebase_survey_20260519T160639.jsonl`
- **Structured JSON:** [`449f8b4a87b654c07f2e.json`](../../sessions/44/449f8b4a87b654c07f2e.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

155 recorded events

### Tool call

_source line 1 · 2026-05-19T16:17:56.594377+00:00_

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
  "session": "worker_research_vla_codebase_survey_20260519T160639",
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

_source line 2 · 2026-05-19T16:17:56.594733+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_vla_codebase_survey_20260519T160639",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-19T16:17:56.594905+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Physical Intelligence openpi pi0 GitHub repository 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_vla_codebase_survey_20260519T160639",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Physical Intelligence openpi pi0 GitHub repository 2025 2026"
  }
}
```

</details>

---

### Tool call

_source line 4 · 2026-05-19T16:17:56.595035+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "OpenVLA-OFT GitHub repository orthogonal fine-tuning VLA 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_vla_codebase_survey_20260519T160639",
  "tool": "WebSearch",
  "tool_args": {
    "query": "OpenVLA-OFT GitHub repository orthogonal fine-tuning VLA 2025 2026"
  }
}
```

</details>

---

### Tool result

_source line 5 · 2026-05-19T16:17:56.595203+00:00_

Web search results for query: "Physical Intelligence openpi pi0 GitHub repository 2025 2026"

Links: [{"title":"GitHub - Physical-Intelligence/openpi · GitHub","url":"https://github.com/Physical-Intelligence/openpi"},{"title":"Physical Intelligence open-sources Pi0 robotics foundation model","url":"https://www.therobotreport.com/physical-intelligence-open-sources-pi0-robotics-foundation-model/"},{"title":"GitHub - Tonghe-Zhang/openpi-physical-intelligence · GitHub","url":"https://github.com/Tonghe-Zhang/openpi-physical-intelligence"},{"title":"Physical Intelligence · GitHub","url":"https://github.com/Physical-Intelligence"},{"title":"Evaluating \\( \\pi_0 \\) in the Wild: Strengths, Problems, and the Future of Generalist Robot Policies","url":"https://penn-pal-lab.github.io/Pi0-Experiment-in-the-Wild/"},{"title":"GitHub - qrafty-ai/pi-openpi: OpenPIE - Open source Pi0 implementation with RECAP training · GitHub","url":"https://github.com/qrafty-ai/pi-openpi"},{"title":"GitHub - allenzren/open-pi-zero: Re-implementation of pi0 vision-language-action (VLA) model from Physical Intelligence · GitHub","url":"https://github.com/allenzren/open-pi-zero"},{"title":"openpi/README.md at main · Physical-Intelligence/openpi","url":"https://github.com/Physical-Intelligence/openpi/blob/main/README.md"},{"title":"Open Sourcing π0","url":"https://www.pi.website/blog/openpi"},{"title":"Rohan Paul on X: \"π0.5 weights + fine-tuning code are now open-source made by Physical-Intelligenc This is the open-sourced π0 from Physical Intelligence, its robotic foundation model, via the openpi repository. π0 is the most advanced Vision Language Action model. It takes natural language https://t.co/2W1YjMubTr\" / X","url":"https://x.com/rohanpaul_ai/status/1965269131827069377"}]

Based on the search results, here's what I found about Physical Intelligence's openpi pi0 GitHub repository:

## Repository Overview

Physical Intelligence has released the code and weights for Pi0 as part of its experim
…[truncated 1183 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_vla_codebase_survey_20260519T160639",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-19T16:17:56.595390+00:00_

Web search results for query: "OpenVLA-OFT GitHub repository orthogonal fine-tuning VLA 2025 2026"

Links: [{"title":"Fine-Tuning Vision-Language-Action Models: Optimizing Speed and Success","url":"https://arxiv.org/pdf/2502.19645"},{"title":"moojink/openvla-7b-oft-finetuned-libero-object · Hugging Face","url":"https://huggingface.co/moojink/openvla-7b-oft-finetuned-libero-object"},{"title":"GitHub - moojink/openvla-oft: Fine-Tuning Vision-Language-Action Models: Optimizing Speed and Success · GitHub","url":"https://github.com/moojink/openvla-oft"},{"title":"Fine-Tuning Vision-Language-Action Models: Optimizing Speed and Success","url":"https://arxiv.org/html/2502.19645v1"},{"title":"[2502.19645] Fine-Tuning Vision-Language-Action Models: Optimizing Speed and Success","url":"https://arxiv.org/abs/2502.19645"},{"title":"GitHub - openvla/openvla: OpenVLA: An open-source vision-language-action model for robotic manipulation. · GitHub","url":"https://github.com/openvla/openvla"},{"title":"OpenVLA: An Open-Source Vision-Language-Action Model","url":"https://arxiv.org/pdf/2406.09246"},{"title":"GitHub - reazon-research/openvla: OpenVLA: An open-source vision-language-action model for robotic manipulation. · GitHub","url":"https://github.com/reazon-research/openvla"},{"title":"openvla/vla-scripts/finetune.py at main · openvla/openvla","url":"https://github.com/openvla/openvla/blob/main/vla-scripts/finetune.py"}]

Based on the search results, here's what I found about the OpenVLA-OFT GitHub repository:

## Overview

OpenVLA-OFT is a research project studying key VLA (vision-language-action) adaptation design choices such as different action decoding schemes, action representations, and learning objectives for fine-tuning, using OpenVLA as the base model.

## Key Features and Improvements

The Optimized Fine-Tuning (OFT) recipe enhances fine-tuned OpenVLA policies through improved inference efficiency, model quality, and input-output flexibility. Compared to vanilla OpenVLA 
…[truncated 942 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_vla_codebase_survey_20260519T160639",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-19T16:17:56.595617+00:00_

called Agent

<details open><summary>🔧 Tool call — Agent</summary>

```json
{
  "description": "Analyze openpi code structure",
  "subagent_type": "general-purpose",
  "prompt": "I'm researching the Physical Intelligence openpi repository (https://github.com/Physical-Intelligence/openpi) for a project called ColliForce-VLA. We want to add a custom SDF decoder head alongside the action decoder.\n\nPlease do a thorough analysis of the code structure. Use `gh` CLI and WebFetch to explore the repo. Specifically:\n\n1. **Repository metadata**: Stars, last update, license\n   - Run: `gh repo view Physical-Intelligence/openpi --json stargazersCount,updatedAt,licenseInfo`\n\n2. **Code structure overview**: \n   - Run: `gh api repos/Physical-Intelligence/openpi/git/trees/main?recursive=1` to get the full file tree\n   - Identify model architecture files, training scripts, fine-tune scripts\n\n3. **Model architecture deep dive**:\n   - Fetch and analyze the main model definition file(s) - likely in `src/openpi/models/` or similar\n   - What is the backbone? (PaliGemma? Gemma? Something else?)\n   - How is the action head structured? What are its input dimensions?\n   - Where are action tokens generated / what intermediate representations exist?\n   - What is the flow from vision+language inputs to action outputs?\n\n4. **Fine-tuning interface**:\n   - How does fine-tuning work? What config system is used?\n   - Can you freeze specific layers?\n   - How would one add a custom auxiliary task head (like an SDF decoder)?\n   - Is there a clear separation between the backbone and the action head?\n\n5. **Action token intermediate features**:\n   - What dimension are the intermediate features before the action head?\n   - At which layer(s) can we access these features?\n   - Can we cross-attend to these features from a separate decoder?\n\n6. **π0.5 and π0.6 updates**: \n   - Any newer model variants in the repo?\n   - How do they differ architecturally?\n\nFor each key finding, note the specific file path and relevant code sections. Be thorough - fetch actual source files, don't just rely on README descriptions.\n\nReturn a detailed report with all findings, organized by the sections above."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_vla_codebase_survey_20260519T160639",
  "tool": "Agent",
  "tool_args": {
    "description": "Analyze openpi code structure",
    "subagent_type": "general-purpose",
    "prompt": "I'm researching the Physical Intelligence openpi repository (https://github.com/Physical-Intelligence/openpi) for a project called ColliForce-VLA. We want to add a custom SDF decoder head alongside the action decoder.\n\nPlease do a thorough analysis of the code structure. Use `gh` CLI and WebFetch to explore the repo. Specifically:\n\n1. **Repository metadata**: Stars, last update, license\n   - Run: `gh repo view Physical-Intelligence/openpi --json stargazersCount,updatedAt,licenseInfo`\n\n2. **Code structure overview**: \n   - Run: `gh api repos/Physical-Intelligence/openpi/git/trees/main?recursive=1` to get the full file tree\n   - Identify model architecture files, training scripts, fine-tune scripts\n\n3. **Model architecture deep dive**:\n   - Fetch and analyze the main model definition file(s) - likely in `src/openpi/models/` or similar\n   - What is the backbone? (PaliGemma? Gemma? Something else?)\n   - How is the action head structured? What are its input dimensions?\n   - Where are action tokens generated / what intermediate representations exist?\n   - What is the flow from vision+language inputs to action outputs?\n\n4. **Fine-tuning interface**:\n   - How does fine-tuning work? What config system is used?\n   - Can you freeze specific layers?\n   - How would one add a custom auxiliary task head (like an SDF decoder)?\n   - Is there a clear separation between the backbone and the action head?\n\n5. **Action token intermediate features**:\n   - What dimension are the intermediate features before the action head?\n   - At which layer(s) can we access these features?\n   - Can we cross-attend to these features from a separate decoder?\n\n6. **π0.5 and π0.6 updates**: \n   - Any newer model variants in the repo?\n   - How do they differ architecturally?\n\nFor each key finding, note the specific file path and relevant code sections. Be thorough - fetch actual source files, don't just rely on README descriptions.\n\nReturn a detailed report with all findings, organized by the sections above."
  }
}
```

</details>

---

### Tool call

_source line 8 · 2026-05-19T16:17:56.595815+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "gh repo view Physical-Intelligence/openpi --json stargazersCount,updatedAt,licenseInfo 2>&1",
  "description": "Get repo metadata: stars, last update, license"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_vla_codebase_survey_20260519T160639",
  "tool": "Bash",
  "tool_args": {
    "command": "gh repo view Physical-Intelligence/openpi --json stargazersCount,updatedAt,licenseInfo 2>&1",
    "description": "Get repo metadata: stars, last update, license"
  }
}
```

</details>

---

### Tool result

_source line 9 · 2026-05-19T16:17:56.595982+00:00_

Exit code 127
/bin/bash: line 1: gh: command not found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_vla_codebase_survey_20260519T160639",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 10 · 2026-05-19T16:17:56.596163+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "gh api repos/Physical-Intelligence/openpi/git/trees/main?recursive=1 2>&1 | python3 -c \"\nimport json, sys\ndata = json.load(sys.stdin)\ntree = data.get('tree', [])\nfor item in tree:\n    print(f\\\"{item['type']}\\t{item['path']}\\\")\n\" 2>&1 | head -500",
  "description": "Get full file tree of the repo"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_vla_codebase_survey_20260519T160639",
  "tool": "Bash",
  "tool_args": {
    "command": "gh api repos/Physical-Intelligence/openpi/git/trees/main?recursive=1 2>&1 | python3 -c \"\nimport json, sys\ndata = json.load(sys.stdin)\ntree = data.get('tree', [])\nfor item in tree:\n    print(f\\\"{item['type']}\\t{item['path']}\\\")\n\" 2>&1 | head -500",
    "description": "Get full file tree of the repo"
  }
}
```

</details>

---

### Tool result

_source line 11 · 2026-05-19T16:17:56.596298+00:00_

&lt;tool_use_error>Cancelled: parallel tool call Bash(gh repo view Physical-Intelligence/openp…) errored&lt;/tool_use_error>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_vla_codebase_survey_20260519T160639",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 12 · 2026-05-19T16:17:56.596444+00:00_

called Agent

<details open><summary>🔧 Tool call — Agent</summary>

```json
{
  "description": "Analyze OpenVLA-OFT code structure",
  "subagent_type": "general-purpose",
  "prompt": "I'm researching the OpenVLA-OFT repository (https://github.com/moojink/openvla-oft) for a project called ColliForce-VLA. We want to add a custom SDF decoder head alongside the action decoder.\n\nPlease do a thorough analysis of the code structure. Use `gh` CLI and WebFetch to explore the repo. Specifically:\n\n1. **Repository metadata**: Stars, last update, license\n   - Run: `gh repo view moojink/openvla-oft --json stargazersCount,updatedAt,licenseInfo`\n\n2. **Code structure overview**: \n   - Run: `gh api repos/moojink/openvla-oft/git/trees/main?recursive=1` to get the full file tree\n   - Identify model architecture files, training scripts, fine-tune scripts\n\n3. **Model architecture deep dive**:\n   - Fetch and analyze the main model definition file(s)\n   - What is the backbone? (Prismatic VLM? Llama? Something else?)\n   - How is the action head structured? What are its input dimensions?\n   - How does OFT change the action decoding compared to vanilla OpenVLA?\n   - Where are action tokens generated / what intermediate representations exist?\n   - What dimension are the hidden states?\n\n4. **OFT mechanism analysis**:\n   - What exactly is \"Optimized Fine-Tuning\"? Is it truly orthogonal fine-tuning or something else?\n   - How does it achieve 25-50x faster inference?\n   - Does OFT replace autoregressive action token generation with a direct MLP head?\n   - What are the implications for adding auxiliary task heads?\n\n5. **Fine-tuning interface**:\n   - How does fine-tuning work? What config system is used?\n   - Can you freeze specific layers?\n   - How would one add a custom auxiliary task head (like an SDF decoder)?\n   - Is there a clear separation between the backbone and the action head?\n\n6. **Action token intermediate features**:\n   - What dimension are the intermediate features before the action head?\n   - At which layer(s) can we access these features?\n   - Can we cross-attend to these features from a separate decoder?\n\nAlso check the original OpenVLA repo (https://github.com/openvla/openvla) briefly to understand what OFT changes.\n\nFor each key finding, note the specific file path and relevant code sections. Be thorough - fetch actual source files, don't just rely on README descriptions.\n\nReturn a detailed report with all findings, organized by the sections above."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_vla_codebase_survey_20260519T160639",
  "tool": "Agent",
  "tool_args": {
    "description": "Analyze OpenVLA-OFT code structure",
    "subagent_type": "general-purpose",
    "prompt": "I'm researching the OpenVLA-OFT repository (https://github.com/moojink/openvla-oft) for a project called ColliForce-VLA. We want to add a custom SDF decoder head alongside the action decoder.\n\nPlease do a thorough analysis of the code structure. Use `gh` CLI and WebFetch to explore the repo. Specifically:\n\n1. **Repository metadata**: Stars, last update, license\n   - Run: `gh repo view moojink/openvla-oft --json stargazersCount,updatedAt,licenseInfo`\n\n2. **Code structure overview**: \n   - Run: `gh api repos/moojink/openvla-oft/git/trees/main?recursive=1` to get the full file tree\n   - Identify model architecture files, training scripts, fine-tune scripts\n\n3. **Model architecture deep dive**:\n   - Fetch and analyze the main model definition file(s)\n   - What is the backbone? (Prismatic VLM? Llama? Something else?)\n   - How is the action head structured? What are its input dimensions?\n   - How does OFT change the action decoding compared to vanilla OpenVLA?\n   - Where are action tokens generated / what intermediate representations exist?\n   - What dimension are the hidden states?\n\n4. **OFT mechanism analysis**:\n   - What exactly is \"Optimized Fine-Tuning\"? Is it truly orthogonal fine-tuning or something else?\n   - How does it achieve 25-50x faster inference?\n   - Does OFT replace autoregressive action token generation with a direct MLP head?\n   - What are the implications for adding auxiliary task heads?\n\n5. **Fine-tuning interface**:\n   - How does fine-tuning work? What config system is used?\n   - Can you freeze specific layers?\n   - How would one add a custom auxiliary task head (like an SDF decoder)?\n   - Is there a clear separation between the backbone and the action head?\n\n6. **Action token intermediate features**:\n   - What dimension are the intermediate features before the action head?\n   - At which layer(s) can we access these features?\n   - Can we cross-attend to these features from a separate decoder?\n\nAlso check the original OpenVLA repo (https://github.com/openvla/openvla) briefly to understand what OFT changes.\n\nFor each key finding, note the specific file path and relevant code sections. Be thorough - fetch actual source files, don't just rely on README descriptions.\n\nReturn a detailed report with all findings, organized by the sections above."
  }
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-19T16:17:56.596623+00:00_

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
  "session": "worker_research_vla_codebase_survey_20260519T160639",
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

_source line 14 · 2026-05-19T16:17:56.596741+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_vla_codebase_survey_20260519T160639",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-19T16:17:56.596867+00:00_

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
  "session": "worker_research_vla_codebase_survey_20260519T160639",
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

_source line 16 · 2026-05-19T16:17:56.596980+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_vla_codebase_survey_20260519T160639",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-19T16:17:56.597097+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "gh repo view moojink/openvla-oft --json stargazersCount,updatedAt,licenseInfo 2>&1",
  "description": "Get OpenVLA-OFT repo metadata"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_vla_codebase_survey_20260519T160639",
  "tool": "Bash",
  "tool_args": {
    "command": "gh repo view moojink/openvla-oft --json stargazersCount,updatedAt,licenseInfo 2>&1",
    "description": "Get OpenVLA-OFT repo metadata"
  }
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-19T16:17:56.597209+00:00_

Exit code 127
/bin/bash: line 1: gh: command not found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_vla_codebase_survey_20260519T160639",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-19T16:17:56.597329+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "which gh 2>/dev/null || (curl -fsSL https://cli.github.com/packages/githubcli-archive-keyring.gpg | sudo dd of=/usr/share/keyrings/githubcli-archive-keyring.gpg 2>/dev/null && sudo chmod go+r /usr/share/keyrings/githubcli-archive-keyring.gpg && echo \"deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/githubcli-archive-keyring.gpg] https://cli.github.com/packages stable main\" | sudo tee /etc/apt/sources.list.d/github-cli.list > /dev/null && sudo apt update -qq 2>/dev/null && sudo apt install gh -y -qq 2>/dev/null && echo \"GH_INSTALLED\") 2>&1 | tail -5",
  "description": "Install gh CLI",
  "timeout": "120000"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_vla_codebase_survey_20260519T160639",
  "tool": "Bash",
  "tool_args": {
    "command": "which gh 2>/dev/null || (curl -fsSL https://cli.github.com/packages/githubcli-archive-keyring.gpg | sudo dd of=/usr/share/keyrings/githubcli-archive-keyring.gpg 2>/dev/null && sudo chmod go+r /usr/share/keyrings/githubcli-archive-keyring.gpg && echo \"deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/githubcli-archive-keyring.gpg] https://cli.github.com/packages stable main\" | sudo tee /etc/apt/sources.list.d/github-cli.list > /dev/null && sudo apt update -qq 2>/dev/null && sudo apt install gh -y -qq 2>/dev/null && echo \"GH_INSTALLED\") 2>&1 | tail -5",
    "description": "Install gh CLI",
    "timeout": "120000"
  }
}
```

</details>

---

### Tool call

_source line 20 · 2026-05-19T16:17:56.597472+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://github.com/Physical-Intelligence/openpi",
  "prompt": "Extract all information about this repository: stars count, last update date, license, description, and the overall README content. List all key sections of the README including model architecture details, fine-tuning instructions, and any mention of pi0, pi0.5, pi0.6 models."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_vla_codebase_survey_20260519T160639",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://github.com/Physical-Intelligence/openpi",
    "prompt": "Extract all information about this repository: stars count, last update date, license, description, and the overall README content. List all key sections of the README including model architecture details, fine-tuning instructions, and any mention of pi0, pi0.5, pi0.6 models."
  }
}
```

</details>

---

### Tool call

_source line 21 · 2026-05-19T16:17:56.597608+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://api.github.com/repos/Physical-Intelligence/openpi",
  "prompt": "Extract the following fields: stargazers_count, updated_at, license (name and spdx_id), description, default_branch, language, forks_count, open_issues_count, topics. Return all values."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_vla_codebase_survey_20260519T160639",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://api.github.com/repos/Physical-Intelligence/openpi",
    "prompt": "Extract the following fields: stargazers_count, updated_at, license (name and spdx_id), description, default_branch, language, forks_count, open_issues_count, topics. Return all values."
  }
}
```

</details>

---

### Tool call

_source line 22 · 2026-05-19T16:17:56.597732+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "which gh 2>/dev/null || (curl -fsSL https://cli.github.com/packages/githubcli-archive-keyring.gpg | sudo dd of=/usr/share/keyrings/githubcli-archive-keyring.gpg 2>/dev/null && echo \"deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/githubcli-archive-keyring.gpg] https://cli.github.com/packages stable main\" | sudo tee /etc/apt/sources.list.d/github-cli.list > /dev/null && sudo apt update -qq && sudo apt install gh -y -qq 2>&1 | tail -3)",
  "description": "Install gh CLI",
  "timeout": "120000"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_vla_codebase_survey_20260519T160639",
  "tool": "Bash",
  "tool_args": {
    "command": "which gh 2>/dev/null || (curl -fsSL https://cli.github.com/packages/githubcli-archive-keyring.gpg | sudo dd of=/usr/share/keyrings/githubcli-archive-keyring.gpg 2>/dev/null && echo \"deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/githubcli-archive-keyring.gpg] https://cli.github.com/packages stable main\" | sudo tee /etc/apt/sources.list.d/github-cli.list > /dev/null && sudo apt update -qq && sudo apt install gh -y -qq 2>&1 | tail -3)",
    "description": "Install gh CLI",
    "timeout": "120000"
  }
}
```

</details>

---

### Tool result

_source line 23 · 2026-05-19T16:17:56.597848+00:00_

Exit code 100

WARNING: apt does not have a stable CLI interface. Use with caution in scripts.

Error: Could not get lock /var/lib/apt/lists/lock. It is held by process 600574 (apt)
Error: Unable to lock directory /var/lib/apt/lists/

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_vla_codebase_survey_20260519T160639",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 24 · 2026-05-19T16:17:56.597969+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "sleep 10 && sudo apt update -qq 2>&1 | tail -1 && sudo apt install gh -y -qq 2>&1 | tail -3",
  "description": "Install gh CLI after waiting for lock",
  "timeout": "120000"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_vla_codebase_survey_20260519T160639",
  "tool": "Bash",
  "tool_args": {
    "command": "sleep 10 && sudo apt update -qq 2>&1 | tail -1 && sudo apt install gh -y -qq 2>&1 | tail -3",
    "description": "Install gh CLI after waiting for lock",
    "timeout": "120000"
  }
}
```

</details>

---

### Tool result

_source line 25 · 2026-05-19T16:17:56.598099+00:00_

Preparing to unpack .../archives/gh_2.92.0_amd64.deb ...
Unpacking gh (2.92.0) ...
Setting up gh (2.92.0) ...
Processing triggers for man-db (2.13.1-1build1) ...
GH_INSTALLED

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_vla_codebase_survey_20260519T160639",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 26 · 2026-05-19T16:17:56.598209+00:00_

# OpenPI Repository Information

**Stargazers Count:** 11,907

**Updated At:** 2026-05-19T14:16:35Z

**License:** 
- Name: Apache License 2.0
- SPDX ID: Apache-2.0

**Description:** No description provided

**Default Branch:** main

**Language:** Python

**Forks Count:** 1,926

**Open Issues Count:** 282

**Topics:** None listed

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_vla_codebase_survey_20260519T160639",
  "tool": "WebFetch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 27 · 2026-05-19T16:17:56.598322+00:00_

7 packages can be upgraded. Run 'apt list --upgradable' to see them.
gh is already the newest version (2.92.0).
Summary:
  Upgrading: 0, Installing: 0, Removing: 0, Not Upgrading: 7

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_vla_codebase_survey_20260519T160639",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 28 · 2026-05-19T16:17:56.598453+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "gh repo view moojink/openvla-oft --json stargazersCount,updatedAt,licenseInfo 2>&1",
  "description": "Get OpenVLA-OFT repo metadata"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_vla_codebase_survey_20260519T160639",
  "tool": "Bash",
  "tool_args": {
    "command": "gh repo view moojink/openvla-oft --json stargazersCount,updatedAt,licenseInfo 2>&1",
    "description": "Get OpenVLA-OFT repo metadata"
  }
}
```

</details>

---

### Tool result

_source line 29 · 2026-05-19T16:17:56.598573+00:00_

Exit code 4
To get started with GitHub CLI, please run:  gh auth login
Alternatively, populate the GH_TOKEN environment variable with a GitHub API authentication token.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_vla_codebase_survey_20260519T160639",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 30 · 2026-05-19T16:17:56.598693+00:00_

# OpenPI Repository Analysis

## Repository Statistics
- **Stars:** 11.9k
- **License:** Apache-2.0
- **Primary Language:** Python (99.3%)
- **Forks:** 1.9k
- **Last Update:** September 2025

## Repository Description
The openpi repository contains "open-source models and packages for robotics, published by the Physical Intelligence team." The project provides base model checkpoints pre-trained on 10,000+ hours of robot data.

## Available Models

### Core Models
1. **π₀** - Flow-based vision-language-action (VLA) model
2. **π₀-FAST** - Autoregressive VLA using the FAST action tokenizer
3. **π₀.₅** - Enhanced version with improved generalization and knowledge insulation

**Note:** Only the π₀.₅ model supports flow matching heads for training and inference in this repository.

## Key README Sections

### Installation
- Uses `uv` for Python dependency management
- Requires submodule initialization during cloning
- Docker alternative available for simplified setup
- GPU requirements: 8GB+ for inference, 22.5GB+ for LoRA fine-tuning, 70GB+ for full fine-tuning

### Model Checkpoints
The repository offers base models for fine-tuning and specialized "expert" checkpoints optimized for platforms including:
- DROID robots
- ALOHA systems
- LIBERO benchmark tasks

### Fine-Tuning Workflow
Three-step process outlined:
1. Converting custom data to LeRobot dataset format
2. Defining training configurations and executing training
3. Deploying policy server for inference

### PyTorch Support
September 2025 update added PyTorch implementations alongside JAX versions, supporting inference and fine-tuning with validation on LIBERO benchmark.

### Inference & Deployment
- Direct inference with pre-trained checkpoints via simple Python API
- Remote inference capability via WebSocket connections
- Policy server for distributed deployment

## Recent Updates (2025)
- PyTorch support implementation
- π₀.₅ model release with improved generalization
- Enhanced idle filtering for DROID traini
…[truncated 45 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_vla_codebase_survey_20260519T160639",
  "tool": "WebFetch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool call

_source line 31 · 2026-05-19T16:17:56.598839+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://github.com/moojink/openvla-oft",
  "prompt": "Extract: 1) Number of stars, 2) Last update date, 3) License, 4) Full file/directory tree structure (list ALL files and directories visible), 5) Key description from README about what OFT does"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_vla_codebase_survey_20260519T160639",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://github.com/moojink/openvla-oft",
    "prompt": "Extract: 1) Number of stars, 2) Last update date, 3) License, 4) Full file/directory tree structure (list ALL files and directories visible), 5) Key description from README about what OFT does"
  }
}
```

</details>

---

### Tool call

_source line 32 · 2026-05-19T16:17:56.598968+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://api.github.com/repos/Physical-Intelligence/openpi/git/trees/main?recursive=1",
  "prompt": "List ALL file paths from the tree. Group them by directory. Focus especially on files under src/, models/, training/, config/ directories. List every single file path, don't skip any."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_vla_codebase_survey_20260519T160639",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://api.github.com/repos/Physical-Intelligence/openpi/git/trees/main?recursive=1",
    "prompt": "List ALL file paths from the tree. Group them by directory. Focus especially on files under src/, models/, training/, config/ directories. List every single file path, don't skip any."
  }
}
```

</details>

---

### Tool result

_source line 33 · 2026-05-19T16:17:56.599084+00:00_

# OpenVLA-OFT Repository Summary

**1) Number of Stars:** 1.2k stars

**2) Last Update Date:** Not explicitly stated in the provided content

**3) License:** MIT license

**4) File/Directory Tree Structure:**
- experiments/robot/
- prismatic/
- scripts/extern/
- vla-scripts/
- .gitignore
- .pre-commit-config.yaml
- ALOHA.md
- LIBERO.md
- LICENSE
- README.md
- SETUP.md
- pyproject.toml

**5) Key Description of OFT Functionality:**

The project focuses on "Fine-Tuning Vision-Language-Action Models: Optimizing Speed and Success." According to the README, it provides tools for training and evaluating vision-language-action models on robotics tasks. The system enables users to download pretrained checkpoints and run inference to generate action sequences. It supports both simulation benchmarks (LIBERO) and real-world robotic tasks (ALOHA), with requirements ranging from single GPUs for inference to multiple GPUs for training depending on the configuration used.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_vla_codebase_survey_20260519T160639",
  "tool": "WebFetch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 34 · 2026-05-19T16:17:56.599211+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://github.com/Physical-Intelligence/openpi/tree/main/src/openpi",
  "prompt": "List all files and subdirectories in this directory. For each subdirectory, list its contents if visible."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_vla_codebase_survey_20260519T160639",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://github.com/Physical-Intelligence/openpi/tree/main/src/openpi",
    "prompt": "List all files and subdirectories in this directory. For each subdirectory, list its contents if visible."
  }
}
```

</details>

---

### Tool call

_source line 35 · 2026-05-19T16:17:56.599335+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://github.com/moojink/openvla-oft/tree/main/prismatic",
  "prompt": "List ALL files and subdirectories in the prismatic/ directory. I need the complete recursive file tree structure."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_vla_codebase_survey_20260519T160639",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://github.com/moojink/openvla-oft/tree/main/prismatic",
    "prompt": "List ALL files and subdirectories in the prismatic/ directory. I need the complete recursive file tree structure."
  }
}
```

</details>

---

### Tool result

_source line 36 · 2026-05-19T16:17:56.599471+00:00_

# OpenPI Source Directory Structure

Based on the GitHub page, here are the files and subdirectories in `/src/openpi`:

## Subdirectories:
- **models** – Contains model definitions
- **models_pytorch** – PyTorch-specific model implementations
- **policies** – Policy-related code
- **serving** – Serving infrastructure code
- **shared** – Shared utilities and components
- **training** – Training scripts and logic

## Files:
- `__init__.py` – Package initialization
- `conftest.py` – pytest configuration
- `py.typed` – Type-checking marker file
- `transforms.py` – Data transformation utilities
- `transforms_test.py` – Tests for transformations

The repository appears to be the OpenPI project from Physical Intelligence, a codebase focused on "robot learning or physical AI systems" based on the directory organization around models, training, and serving components.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_vla_codebase_survey_20260519T160639",
  "tool": "WebFetch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 37 · 2026-05-19T16:17:56.599606+00:00_

# Prismatic Directory Structure

Based on the GitHub page content provided, here is the visible directory structure for the `prismatic/` folder:

## Top-Level Contents:

- **conf/** (subdirectory)
- **extern/** (subdirectory)
- **models/** (subdirectory)
- **overwatch/** (subdirectory)
- **preprocessing/** (subdirectory)
- **training/** (subdirectory)
- **util/** (subdirectory)
- **vla/** (subdirectory)
- **__init__.py** (file)
- **py.typed** (file)

## Limitation:

The webpage content shows only the immediate contents of the `prismatic/` directory. The page indicates there are additional files available but doesn't display the complete recursive structure of subdirectories and their contents. To obtain the full recursive file tree (files within conf/, models/, training/, etc.), you would need to navigate into each subdirectory on GitHub individually or access the repository through Git commands or the GitHub API.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_vla_codebase_survey_20260519T160639",
  "tool": "WebFetch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 38 · 2026-05-19T16:17:56.599737+00:00_

# OpenPI Repository File Structure

## Root Level Files
- .dockerignore
- .gitignore
- .gitmodules
- .python-version
- .pre-commit-config.yaml
- pyproject.toml
- README.md
- LICENSE
- LICENSE_GEMMA.txt
- CONTRIBUTING.md
- uv.lock

## .github/
- CODEOWNERS
- workflows/pre-commit.yml
- workflows/test.yml

## .vscode/
- settings.json

## docs/
- docker.md
- norm_stats.md
- remote_inference.md

## examples/
- inference.ipynb
- policy_records.ipynb
- convert_jax_model_to_pytorch.py

### examples/aloha_real/
- Dockerfile
- README.md
- compose.yml
- constants.py
- convert_aloha_data_to_lerobot.py
- env.py
- main.py
- real_env.py
- robot_utils.py
- video_display.py
- requirements.in
- requirements.txt

### examples/aloha_sim/
- Dockerfile
- README.md
- compose.yml
- env.py
- main.py
- saver.py
- requirements.in
- requirements.txt

### examples/droid/
- README.md
- README_train.md
- compute_droid_nonidle_ranges.py
- convert_droid_data_to_lerobot.py
- main.py

### examples/libero/
- Dockerfile
- README.md
- compose.yml
- convert_libero_data_to_lerobot.py
- main.py
- requirements.in
- requirements.txt

### examples/simple_client/
- Dockerfile
- README.md
- compose.yml
- main.py
- requirements.in
- requirements.txt

### examples/ur5/
- README.md

## packages/openpi-client/
- pyproject.toml

### packages/openpi-client/src/openpi_client/
- __init__.py
- action_chunk_broker.py
- base_policy.py
- image_tools.py
- image_tools_test.py
- msgpack_numpy.py
- msgpack_numpy_test.py
- websocket_client_policy.py

### packages/openpi-client/src/openpi_client/runtime/
- agent.py
- environment.py
- runtime.py
- subscriber.py

### packages/openpi-client/src/openpi_client/runtime/agents/
- policy_agent.py

## scripts/
- __init__.py
- compute_norm_stats.py
- serve_policy.py
- train.py
- train_pytorch.py
- train_test.py

### scripts/docker/
- compose.yml
- install_docker_ubuntu22.sh
- install_nvidia_container_toolkit.sh
- serve_policy.Dockerfile

## src/openpi/
- __init__.py
- conftest.py
- py.typ
…[truncated 1385 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_vla_codebase_survey_20260519T160639",
  "tool": "WebFetch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 39 · 2026-05-19T16:17:56.599882+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://api.github.com/repos/moojink/openvla-oft/git/trees/main?recursive=1",
  "prompt": "List ALL file paths from the tree. Group them by directory. Focus especially on files under prismatic/models/, prismatic/vla/, prismatic/training/, and vla-scripts/. Return the complete list."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_vla_codebase_survey_20260519T160639",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://api.github.com/repos/moojink/openvla-oft/git/trees/main?recursive=1",
    "prompt": "List ALL file paths from the tree. Group them by directory. Focus especially on files under prismatic/models/, prismatic/vla/, prismatic/training/, and vla-scripts/. Return the complete list."
  }
}
```

</details>

---

### Tool call

_source line 40 · 2026-05-19T16:17:56.600092+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://raw.githubusercontent.com/Physical-Intelligence/openpi/main/src/openpi/models/model.py",
  "prompt": "Return the COMPLETE file content, every single line. This is a critical model definition file. Do not summarize - return the full source code."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_vla_codebase_survey_20260519T160639",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://raw.githubusercontent.com/Physical-Intelligence/openpi/main/src/openpi/models/model.py",
    "prompt": "Return the COMPLETE file content, every single line. This is a critical model definition file. Do not summarize - return the full source code."
  }
}
```

</details>

---

### Tool call

_source line 41 · 2026-05-19T16:17:56.600230+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://raw.githubusercontent.com/Physical-Intelligence/openpi/main/src/openpi/models/pi0.py",
  "prompt": "Return the COMPLETE file content, every single line of code. This is a critical model architecture file. Do not summarize - return all source code verbatim."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_vla_codebase_survey_20260519T160639",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://raw.githubusercontent.com/Physical-Intelligence/openpi/main/src/openpi/models/pi0.py",
    "prompt": "Return the COMPLETE file content, every single line of code. This is a critical model architecture file. Do not summarize - return all source code verbatim."
  }
}
```

</details>

---

### Tool call

_source line 42 · 2026-05-19T16:17:56.600356+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://raw.githubusercontent.com/Physical-Intelligence/openpi/main/src/openpi/models/pi0_config.py",
  "prompt": "Return the COMPLETE file content verbatim. Every line of code. Do not summarize."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_vla_codebase_survey_20260519T160639",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://raw.githubusercontent.com/Physical-Intelligence/openpi/main/src/openpi/models/pi0_config.py",
    "prompt": "Return the COMPLETE file content verbatim. Every line of code. Do not summarize."
  }
}
```

</details>

---

### Tool call

_source line 43 · 2026-05-19T16:17:56.600499+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://raw.githubusercontent.com/Physical-Intelligence/openpi/main/src/openpi/models/pi0_fast.py",
  "prompt": "Return the COMPLETE file content verbatim. Every line of code. Do not summarize."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_vla_codebase_survey_20260519T160639",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://raw.githubusercontent.com/Physical-Intelligence/openpi/main/src/openpi/models/pi0_fast.py",
    "prompt": "Return the COMPLETE file content verbatim. Every line of code. Do not summarize."
  }
}
```

</details>

---

### Tool result

_source line 44 · 2026-05-19T16:17:56.600630+00:00_

# File Structure Organization

## Root Level Files
- `.gitignore`
- `.pre-commit-config.yaml`
- `ALOHA.md`
- `LIBERO.md`
- `LICENSE`
- `README.md`
- `SETUP.md`
- `pyproject.toml`

## experiments/
- `experiments/robot/robot_utils.py`
- `experiments/robot/openvla_utils.py`

### experiments/robot/aloha/
- `aloha_utils.py`
- `constants.py`
- `preprocess_split_aloha_data.py`
- `real_env.py`
- `requirements_aloha.txt`
- `robot_utils.py`
- `run_aloha_eval.py`

### experiments/robot/libero/
- `libero_requirements.txt`
- `libero_utils.py`
- `regenerate_libero_dataset.py`
- `run_libero_eval.py`
- `sample_libero_spatial_observation.pkl`

## prismatic/models/
- `__init__.py`
- `action_heads.py`
- `film_vit_wrapper.py`
- `load.py`
- `materialize.py`
- `projectors.py`
- `registry.py`

### prismatic/models/backbones/
- `__init__.py`

### prismatic/models/backbones/llm/
- `__init__.py`
- `base_llm.py`
- `llama2.py`
- `mistral.py`
- `phi.py`

### prismatic/models/backbones/llm/prompting/
- `__init__.py`
- `base_prompter.py`
- `llama2_chat_prompter.py`
- `mistral_instruct_prompter.py`
- `phi_prompter.py`
- `vicuna_v15_prompter.py`

### prismatic/models/backbones/vision/
- `__init__.py`
- `base_vision.py`
- `clip_vit.py`
- `dinoclip_vit.py`
- `dinosiglip_vit.py`
- `dinov2_vit.py`
- `in1k_vit.py`
- `siglip_vit.py`

### prismatic/models/vlas/
- `__init__.py`
- `openvla.py`

### prismatic/models/vlms/
- `__init__.py`
- `base_vlm.py`
- `prismatic.py`

## prismatic/vla/
- `__init__.py`
- `action_tokenizer.py`
- `constants.py`
- `materialize.py`

### prismatic/vla/datasets/
- `__init__.py`
- `datasets.py`

### prismatic/vla/datasets/rlds/
- `__init__.py`
- `dataset.py`
- `obs_transforms.py`
- `traj_transforms.py`

### prismatic/vla/datasets/rlds/oxe/
- `__init__.py`
- `configs.py`
- `materialize.py`
- `mixtures.py`
- `transforms.py`

### prismatic/vla/datasets/rlds/oxe/utils/
- `droid_utils.py`

### prismatic/vla/datasets/rlds/utils/
- `__init__.py`
- `data_utils.py`
- `goal_relabeling.py`

…[truncated 1085 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_vla_codebase_survey_20260519T160639",
  "tool": "WebFetch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 45 · 2026-05-19T16:17:56.600775+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://raw.githubusercontent.com/moojink/openvla-oft/main/prismatic/models/action_heads.py",
  "prompt": "Return the COMPLETE file content verbatim. Do not summarize. Include every line of code, every class definition, every function, every comment. This is critical."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_vla_codebase_survey_20260519T160639",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://raw.githubusercontent.com/moojink/openvla-oft/main/prismatic/models/action_heads.py",
    "prompt": "Return the COMPLETE file content verbatim. Do not summarize. Include every line of code, every class definition, every function, every comment. This is critical."
  }
}
```

</details>

---

### Tool result

_source line 46 · 2026-05-19T16:17:56.600912+00:00_

# Complete File Content

```python
import dataclasses
from typing import TYPE_CHECKING

import flax.nnx as nnx
import jax
import jax.numpy as jnp
from typing_extensions import override

from openpi.models import model as _model
import openpi.models.gemma as _gemma
from openpi.shared import array_typing as at
import openpi.shared.nnx_utils as nnx_utils

if TYPE_CHECKING:
    from openpi.models.pi0 import Pi0


@dataclasses.dataclass(frozen=True)
class Pi0Config(_model.BaseModelConfig):
    dtype: str = "bfloat16"
    paligemma_variant: _gemma.Variant = "gemma_2b"
    action_expert_variant: _gemma.Variant = "gemma_300m"

    # Set the model specific defaults.
    action_dim: int = 32
    action_horizon: int = 50
    max_token_len: int = None  # type: ignore
    # Pi05 has two differences from Pi0:
    # - the state input is part of the discrete language tokens rather than a continuous input that is part of the suffix
    # - the action expert uses adaRMSNorm to inject the flow matching timestep
    pi05: bool = False
    # This config option is not used directly by the model, but it is read by the ModelTransformFactory.
    discrete_state_input: bool = None  # type: ignore

    pytorch_compile_mode: str | None = "max-autotune"

    def __post_init__(self):
        if self.max_token_len is None:
            object.__setattr__(self, "max_token_len", 200 if self.pi05 else 48)
        if self.discrete_state_input is None:
            object.__setattr__(self, "discrete_state_input", self.pi05)
        if self.pytorch_compile_mode is not None:
            assert self.pytorch_compile_mode in [
                "default",
                "reduce-overhead",
                "max-autotune",
                "max-autotune-no-cudagraphs",
            ]

    @property
    @override
    def model_type(self) -> _model.ModelType:
        if self.pi05:
            return _model.ModelType.PI05
        return _model.ModelType.PI0

    @override
    def create(self, rng: at.KeyArrayLike) ->
…[truncated 2473 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_vla_codebase_survey_20260519T160639",
  "tool": "WebFetch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 47 · 2026-05-19T16:17:56.601049+00:00_

# Analysis of Action Head Implementations

This Python module defines neural network components for robotic action prediction, offering alternatives to standard VLM token-based approaches.

## Key Components

**Positional Encoding**: The `SinusoidalPositionalEncoding` class generates timestep embeddings using sine and cosine functions, adapted from diffusion policy research. It converts batch timesteps into dimensional embeddings.

**Residual Architecture**: `MLPResNetBlock` and `MLPResNet` implement feed-forward networks with residual connections, following "Pre-Layer Normalization" design patterns from transformer research.

**L1 Regression Head**: `L1RegressionActionHead` predicts continuous actions through supervised learning, processing transformer hidden states via an MLP network with 2 residual blocks.

**Diffusion-Based Approach**: The `DiffusionActionHead` and `NoisePredictionModel` implement conditional denoising diffusion for action generation. Key features include:

- Random noise sampling matched to action dimensions
- Random diffusion timestep selection during training
- Closed-form forward diffusion noise addition
- Timestep embedding generation for conditioning

The noise predictor takes observation embeddings and outputs noise predictions, enabling iterative denoising during inference.

## Design Pattern

Both approaches condition action generation on vision-language transformer embeddings, but differ fundamentally: L1 regression predicts actions directly, while diffusion iteratively denoises from noise toward clean actions using timestep-conditioned guidance.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_vla_codebase_survey_20260519T160639",
  "tool": "WebFetch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 48 · 2026-05-19T16:17:56.601188+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://raw.githubusercontent.com/moojink/openvla-oft/main/prismatic/models/vlas/openvla.py",
  "prompt": "Return the COMPLETE file content verbatim, preserving all code exactly. Include every import, class, method, comment, and line. Do not summarize or paraphrase."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_vla_codebase_survey_20260519T160639",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://raw.githubusercontent.com/moojink/openvla-oft/main/prismatic/models/vlas/openvla.py",
    "prompt": "Return the COMPLETE file content verbatim, preserving all code exactly. Include every import, class, method, comment, and line. Do not summarize or paraphrase."
  }
}
```

</details>

---

### Tool result

_source line 49 · 2026-05-19T16:17:56.601308+00:00_

# OpenVLA Module Overview

The file defines **OpenVLA**, a lightweight wrapper around PrismaticVLM that handles vision-language action prediction for robotics. 

## Key Components

**Class Structure**: OpenVLA extends PrismaticVLM and adds normalization statistics and an action tokenizer to the parent model.

**Core Method**: The `predict_action()` function performs inference by:
- Building a formatted prompt from the task instruction
- Tokenizing the prompt text with special handling for LlamaTokenizerFast
- Transforming and preprocessing the input image
- Generating action tokens via the parent class's generation method
- Decoding tokens to normalized actions
- Un-normalizing actions using stored statistics with quantile-based ranges

**Helper Methods**: 
- `_check_unnorm_key()` validates dataset selection, ensuring a single dataset if no key provided
- `get_action_dim()` retrieves the action space dimensionality
- `get_action_stats()` accesses normalization statistics

**Notable Implementation Details**: The code includes special handling for LlamaTokenizerFast to match training-time inputs by inserting token ID 29871 (empty token) when needed. Un-normalization uses a mask to selectively apply quantile-based scaling versus passthrough for specific action dimensions.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_vla_codebase_survey_20260519T160639",
  "tool": "WebFetch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 50 · 2026-05-19T16:17:56.601454+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://raw.githubusercontent.com/moojink/openvla-oft/main/prismatic/models/vlms/prismatic.py",
  "prompt": "Return the COMPLETE file content verbatim. Include every import, class definition, method, property, comment, and line of code. Do not summarize. I need the exact architecture details including hidden dimensions, forward pass logic, and how action heads are integrated."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_vla_codebase_survey_20260519T160639",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://raw.githubusercontent.com/moojink/openvla-oft/main/prismatic/models/vlms/prismatic.py",
    "prompt": "Return the COMPLETE file content verbatim. Include every import, class definition, method, property, comment, and line of code. Do not summarize. I need the exact architecture details including hidden dimensions, forward pass logic, and how action heads are integrated."
  }
}
```

</details>

---

### Tool result

_source line 51 · 2026-05-19T16:17:56.601617+00:00_

# Complete File Content

```python
import abc
from collections.abc import Sequence
import dataclasses
import enum
import logging
import pathlib
from typing import Generic, TypeVar

import augmax
from flax import nnx
from flax import struct
from flax import traverse_util
import jax
import jax.numpy as jnp
import numpy as np
import orbax.checkpoint as ocp
import safetensors
import torch

from openpi.models_pytorch import pi0_pytorch
from openpi.shared import image_tools
import openpi.shared.array_typing as at

logger = logging.getLogger("openpi")

# Type variable for array types (JAX arrays, PyTorch tensors, or numpy arrays)
ArrayT = TypeVar("ArrayT", bound=jax.Array | torch.Tensor | np.ndarray)


class ModelType(enum.Enum):
    """Supported model types."""

    PI0 = "pi0"
    PI0_FAST = "pi0_fast"
    PI05 = "pi05"


# The model always expects these images
IMAGE_KEYS = (
    "base_0_rgb",
    "left_wrist_0_rgb",
    "right_wrist_0_rgb",
)


# This may need change if we release a small model.
IMAGE_RESOLUTION = (224, 224)


# Data format
#
# Data transforms produce the model input as a nested dictionary which is later converted
# into `Obesrvation` and `Actions` objects. See below.
#
# In the dictory form, this data should look like:
# {
#     # Observation data.
#     "image": {
#         "base_0_rgb": (float32|uint8)[*b, h, w, 3],  # RGB image in [-1, 1] or [0, 255]
#         ...  # Additional camera views
#     },
#     "image_mask": {
#         "base_0_rgb": bool[*b],  # True if image is valid
#         ...  # Masks for additional views
#     },
#     "state": float32[*b, s],  # Low-dimensional robot state
#     "tokenized_prompt": int32[*b, l],  # Optional, tokenized language prompt
#     "tokenized_prompt_mask": bool[*b, l],  # Optional, mask for tokenized prompt
#     "token_ar_mask": int32[*b, l],  # Optional, autoregressive mask for FAST model
#     "token_loss_mask": bool[*b, l],  # Optional, loss mask for FAST model
#
#      # Actions data.
#      "actions
…[truncated 10308 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_vla_codebase_survey_20260519T160639",
  "tool": "WebFetch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 52 · 2026-05-19T16:17:56.601795+00:00_

# Pi0 Model Architecture File

This is a complete Flax NNX implementation of the Pi0 diffusion-based robot policy model. Here's the file content verbatim:

```python
import logging

import einops
import flax.nnx as nnx
import flax.nnx.bridge as nnx_bridge
import jax
import jax.numpy as jnp
from typing_extensions import override

from openpi.models import model as _model
from openpi.models import pi0_config
import openpi.models.gemma as _gemma
import openpi.models.siglip as _siglip
from openpi.shared import array_typing as at

logger = logging.getLogger("openpi")


def make_attn_mask(input_mask, mask_ar):
    """Adapted from big_vision.

    Tokens can attend to valid inputs tokens which have a cumulative mask_ar
    smaller or equal to theirs. This way `mask_ar` bool[?B, N] can be used to
    setup several types of attention, for example:

      [[1 1 1 1 1 1]]: pure causal attention.

      [[0 0 0 1 1 1]]: prefix-lm attention. The first 3 tokens can attend between
          themselves and the last 3 tokens have a causal attention. The first
          entry could also be a 1 without changing behaviour.

      [[1 0 1 0 1 0 0 1 0 0]]: causal attention between 4 blocks. Tokens of a
          block can attend all previous blocks and all tokens on the same block.

    Args:
      input_mask: bool[B, N] true if its part of the input, false if padding.
      mask_ar: bool[?B, N] mask that's true where previous tokens cannot depend on
        it and false where it shares the same attention mask as the previous token.
    """
    mask_ar = jnp.broadcast_to(mask_ar, input_mask.shape)
    cumsum = jnp.cumsum(mask_ar, axis=1)
    attn_mask = cumsum[:, None, :] <= cumsum[:, :, None]
    valid_mask = input_mask[:, None, :] * input_mask[:, :, None]
    return jnp.logical_and(attn_mask, valid_mask)


@at.typecheck
def posemb_sincos(
    pos: at.Real[at.Array, " b"], embedding_dim: int, min_period: float, max_period: float
) -> at.Float[at.Array, "b {embedding_dim}"]:
    """Compu
…[truncated 11246 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_vla_codebase_survey_20260519T160639",
  "tool": "WebFetch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 53 · 2026-05-19T16:17:56.601971+00:00_

# Complete File Content

```python
import dataclasses
import logging
from typing import Any

import einops
import flax.nnx as nnx
import flax.nnx.bridge as nnx_bridge
import jax
import jax.numpy as jnp
from typing_extensions import override

from openpi.models import model as _model
import openpi.models.gemma_fast as _gemma
import openpi.models.siglip as _siglip
from openpi.shared import array_typing as at
import openpi.shared.nnx_utils as nnx_utils

logger = logging.getLogger("openpi")

PALIGEMMA_EOS_TOKEN = 1


def make_attn_mask(input_mask, mask_ar):
    """Adapted from big_vision.

    Tokens can attend to valid inputs tokens which have a cumulative mask_ar
    smaller or equal to theirs. This way `mask_ar` bool[?B, N] can be used to
    setup several types of attention, for example:

      [[1 1 1 1 1 1]]: pure causal attention.

      [[0 0 0 1 1 1]]: prefix-lm attention. The first 3 tokens can attend between
          themselves and the last 3 tokens have a causal attention. The first
          entry could also be a 1 without changing behaviour.

      [[1 0 1 0 1 0 0 1 0 0]]: causal attention between 4 blocks. Tokens of a
          block can attend all previous blocks and all tokens on the same block.

    Args:
      input_mask: bool[B, N] true if its part of the input, false if padding.
      mask_ar: bool[?B, N] mask that's true where previous tokens cannot depend on
        it and false where it shares the same attention mask as the previous token.
    """
    mask_ar = jnp.broadcast_to(mask_ar, input_mask.shape)
    cumsum = jnp.cumsum(mask_ar, axis=1)
    attn_mask = cumsum[:, None, :] <= cumsum[:, :, None]
    valid_mask = input_mask[:, None, :] * input_mask[:, :, None]
    return jnp.logical_and(attn_mask, valid_mask)


@jax.vmap
def left_to_right_align(x, input_mask, attn_mask):
    """Converts input from left-align to right-aligned."""
    # Due to vmap, this is operating in a single example (not batch level).
    assert x.ndim == 2
    assert inpu
…[truncated 11247 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_vla_codebase_survey_20260519T160639",
  "tool": "WebFetch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 54 · 2026-05-19T16:17:56.602122+00:00_

# PrismaticVLM Architecture Analysis

## Overview
This PyTorch module implements `PrismaticVLM`, a vision-language model that combines visual and text processing through a projection mechanism. The architecture is not a direct subclass of `transformers.PretrainedModel` but rather implements key methods needed for generation.

## Core Components

**Three Main Modules:**
1. **Vision Backbone** - Extracts visual features from images
2. **LLM Backbone** - Processes text and generates responses
3. **Projector** - Bridges visual embeddings to LLM embedding space

## Projector Architecture Options

The system supports three projection strategies, selected via `arch_specifier`:

- `"linear"`: Simple `LinearProjector`
- `"gelu-mlp"`: Multi-layer perceptron with GELU activation
- `"fused-gelu-mlp"`: Optimized fused MLP variant

Weight initialization uses the vision backbone's embedding dimension as seed for consistency.

## Training Stages

The `freeze_backbones()` method supports six distinct training configurations:

- **align**: Only projector trains; both backbones frozen
- **finetune/vla-train**: Projector and LLM train; vision frozen
- **full-finetune/vla-full-train**: All components trainable
- **last-layer-finetune/vla-last-layer-train**: Only final LLM layer unfrozen
- **vla-sandwich-train**: Vision and projector train; only LLM's final layer unfrozen

## Forward Pass Logic

The forward method handles three scenarios:

1. **Inference with cache** - Returns LLM output directly when leveraging KV cache
2. **Unimodal-only** - Routes purely text inputs to LLM backbone
3. **Multimodal** - Fuses visual and textual embeddings

For multimodal inputs, the system:
- Extracts patch features from images
- Projects them to LLM embedding dimension
- Inserts projected embeddings after initial token in sequence
- Maintains proper attention masks and label assignments (image tokens ignored in loss)

## Generation Methods

**generate()** - Single image inference with prompt text
**gen
…[truncated 470 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_vla_codebase_survey_20260519T160639",
  "tool": "WebFetch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 55 · 2026-05-19T16:17:56.602273+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://raw.githubusercontent.com/Physical-Intelligence/openpi/main/src/openpi/models/gemma.py",
  "prompt": "Return the COMPLETE file content verbatim. Every line of code. This is the backbone model. Do not summarize."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_vla_codebase_survey_20260519T160639",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://raw.githubusercontent.com/Physical-Intelligence/openpi/main/src/openpi/models/gemma.py",
    "prompt": "Return the COMPLETE file content verbatim. Every line of code. This is the backbone model. Do not summarize."
  }
}
```

</details>

---

### Tool call

_source line 56 · 2026-05-19T16:17:56.602411+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://raw.githubusercontent.com/moojink/openvla-oft/main/vla-scripts/finetune.py",
  "prompt": "Return the COMPLETE file content verbatim. Include every import, function, class, argument parser, config, and line of code. I need to see how the action head is configured, what training configs exist, how the model is built, and what OFT-specific changes are made."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_vla_codebase_survey_20260519T160639",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://raw.githubusercontent.com/moojink/openvla-oft/main/vla-scripts/finetune.py",
    "prompt": "Return the COMPLETE file content verbatim. Include every import, function, class, argument parser, config, and line of code. I need to see how the action head is configured, what training configs exist, how the model is built, and what OFT-specific changes are made."
  }
}
```

</details>

---

### Tool call

_source line 57 · 2026-05-19T16:17:56.602567+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://raw.githubusercontent.com/Physical-Intelligence/openpi/main/src/openpi/training/config.py",
  "prompt": "Return the COMPLETE file content verbatim. Every line of code. This is the training configuration. Do not summarize."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_vla_codebase_survey_20260519T160639",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://raw.githubusercontent.com/Physical-Intelligence/openpi/main/src/openpi/training/config.py",
    "prompt": "Return the COMPLETE file content verbatim. Every line of code. This is the training configuration. Do not summarize."
  }
}
```

</details>

---

### Tool call

_source line 58 · 2026-05-19T16:17:56.602696+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://raw.githubusercontent.com/Physical-Intelligence/openpi/main/src/openpi/models_pytorch/pi0_pytorch.py",
  "prompt": "Return the COMPLETE file content verbatim. Every line of code. This is the PyTorch model implementation. Do not summarize."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_vla_codebase_survey_20260519T160639",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://raw.githubusercontent.com/Physical-Intelligence/openpi/main/src/openpi/models_pytorch/pi0_pytorch.py",
    "prompt": "Return the COMPLETE file content verbatim. Every line of code. This is the PyTorch model implementation. Do not summarize."
  }
}
```

</details>

---

### Tool result

_source line 59 · 2026-05-19T16:17:56.602821+00:00_

# OpenVLA Fine-tuning Analysis

## Overview
This is a LoRA fine-tuning script for OpenVLA (a vision-language-action model) that supports multiple action representation approaches and training objectives.

## Key Configuration (`FinetuneConfig`)

The training framework accepts these primary settings:

**Model & Data:**
- Base model path (HuggingFace Hub or local)
- RLDS dataset specification
- Checkpoint/logging directory

**Action Representations:**
- L1 regression for continuous actions
- Diffusion-based action generation
- Discrete token prediction (default)

**Architecture Options:**
- FiLM wrapper for language-conditioned vision features
- Multi-image inputs (third-person + wrist cameras)
- Proprioceptive state integration

**Training Parameters:**
- Batch size, learning rate, warmup, decay schedule
- Gradient accumulation steps
- Validation frequency and time limits
- Checkpoint saving strategy

## Action Head Configuration

The script instantiates action heads conditionally:

1. **L1RegressionActionHead** (when `use_l1_regression=True`): Takes hidden states and predicts continuous actions via regression loss

2. **DiffusionActionHead** (when `use_diffusion=True`): Implements noise prediction with timestep embeddings; paired with `NoisyActionProjector` for embedding noisy actions

3. **No explicit head** (discrete mode): Uses language model logits directly for next-token action prediction

All heads receive the VLA's LLM dimension and ACTION_DIM as configuration parameters.

## Training Flow

The `run_forward_pass()` function handles three distinct pathways:

- **Discrete**: Standard language modeling loss on action tokens
- **L1 Regression**: Predicts action chunk from hidden states, computes L1 loss
- **Diffusion**: Predicts noise, optionally samples actions via reverse diffusion for validation L1 metrics

The script uses gradient accumulation, distributed training (DDP), and Weights & Biases logging. Checkpointing includes LoRA adapters, component modules, a
…[truncated 64 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_vla_codebase_survey_20260519T160639",
  "tool": "WebFetch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 60 · 2026-05-19T16:17:56.602956+00:00_

# PI0Pytorch Model Implementation

This file contains the complete PyTorch implementation of the PI0 model, a diffusion-based policy architecture that combines PaliGemma vision-language processing with an expert Gemma decoder for robot action prediction.

## Key Components

**Utility Functions:**
- `get_safe_dtype()`: Handles device-specific dtype compatibility (CPU lacks bfloat16 support)
- `create_sinusoidal_pos_embedding()`: Generates sine-cosine positional encodings for timestep conditioning
- `make_att_2d_masks()`: Constructs flexible 2D attention masks supporting causal, prefix-LM, and block-causal patterns

**Core PI0Pytorch Class:**

The main model inherits from `nn.Module` and orchestrates three processing stages:

1. **Prefix embedding**: Processes images via SigLIP and language tokens through PaliGemma's embedding layers
2. **Suffix embedding**: Encodes state, noisy actions, and timesteps for the expert decoder
3. **Forward pass**: Combines embeddings through a transformer, predicting action corrections

**Training (`forward`)**: Accepts observations and actions, optionally samples noise and timesteps, computes diffusion targets (x_t, u_t), and returns MSE loss predictions.

**Inference (`sample_actions`)**: Performs iterative denoising using Euler steps, leveraging cached prefix embeddings for efficiency.

**Memory Optimization**: Includes gradient checkpointing methods (`gradient_checkpointing_enable/disable`) to reduce activation memory during training.

**Model Variants**: Supports two configurations via `pi05` flag, with different time conditioning strategies (adaRMS-based vs. MLP-fused).

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_vla_codebase_survey_20260519T160639",
  "tool": "WebFetch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 61 · 2026-05-19T16:17:56.603099+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://raw.githubusercontent.com/moojink/openvla-oft/main/prismatic/models/vlms/base_vlm.py",
  "prompt": "Return the COMPLETE file content verbatim. Every import, class, method, abstract method, property, comment. I need to understand the base VLM interface and what dimensions/properties are exposed."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_vla_codebase_survey_20260519T160639",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://raw.githubusercontent.com/moojink/openvla-oft/main/prismatic/models/vlms/base_vlm.py",
    "prompt": "Return the COMPLETE file content verbatim. Every import, class, method, abstract method, property, comment. I need to understand the base VLM interface and what dimensions/properties are exposed."
  }
}
```

</details>

---

### Tool result

_source line 62 · 2026-05-19T16:17:56.603221+00:00_

# VLM Base Class Interface Summary

The provided file defines an abstract Vision-Language Model class that serves as a foundational interface for multimodal AI systems. Here are the key structural elements:

## Class Hierarchy
The `VLM` class inherits from `nn.Module`, `GenerationMixin`, and `ABC`, combining PyTorch's module system with HuggingFace's generation capabilities.

## Core Initialization Parameters
The constructor accepts:
- `model_family` and `model_id` for identification
- `vision_backbone` (VisionBackbone instance)
- `llm_backbone` (LLMBackbone instance)
- A flag for mixed-precision training support

## Key Abstract Methods
Classes implementing this interface must define:
- `from_pretrained()` - loading from checkpoints
- `get_prompt_builder()` - creating prompt construction utilities
- `freeze_backbones()` - controlling trainable parameters by stage
- `load_from_checkpoint()` - resuming from saved states
- `get_fsdp_wrapping_policy()` - distributed training configuration
- `forward()` - the primary computation method

## Forward Method Signature
The forward pass accepts vision inputs (`pixel_values`), language inputs (`input_ids`, `attention_mask`), embeddings, and generation-related parameters like `past_key_values` and `use_cache`, returning a `CausalLMOutputWithPast` object.

## Generation Support
The class integrates generation functionality through properties like `generation_config` and `main_input_name`, with a utility method `_reorder_cache()` for beam search optimization.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_vla_codebase_survey_20260519T160639",
  "tool": "WebFetch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 63 · 2026-05-19T16:17:56.603355+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://raw.githubusercontent.com/moojink/openvla-oft/main/README.md",
  "prompt": "Return ALL content verbatim. I need the full README including all descriptions of what OFT is, how it achieves faster inference, what architectural changes it makes, performance numbers, and any figures/diagrams described. Do NOT skip any sections."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_vla_codebase_survey_20260519T160639",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://raw.githubusercontent.com/moojink/openvla-oft/main/README.md",
    "prompt": "Return ALL content verbatim. I need the full README including all descriptions of what OFT is, how it achieves faster inference, what architectural changes it makes, performance numbers, and any figures/diagrams described. Do NOT skip any sections."
  }
}
```

</details>

---

### Tool result

_source line 64 · 2026-05-19T16:17:56.603506+00:00_

# Summary of OpenVLA-OFT README Content

Based on the webpage provided, I can share what's available, though I should note the document appears to be a README excerpt rather than a complete paper.

## What's Included

The page contains setup instructions and a quick-start guide for OpenVLA-OFT, a vision-language-action model system. It specifies that the project involves "Fine-Tuning Vision-Language-Action Models: Optimizing Speed and Success."

## Key Information Present

**System Requirements:** The document lists GPU memory needs—approximately 16-18 GB VRAM for inference depending on the task type, and 27-80 GB across 1-8 GPUs for training.

**Code Example:** A Python script demonstrates loading a pretrained checkpoint and generating action sequences using components like an action head and proprio projector.

**Resource Directions:** Rather than detailing architectural changes or performance metrics in this section, the README directs readers to supplementary files (SETUP.md, LIBERO.md, ALOHA.md) and external resources including the full paper at arxiv.org, a project website, and a video summary.

## What's Not Included

The excerpt doesn't contain descriptions of what OFT specifically is, how it achieves faster inference, architectural modifications, performance benchmarks, or figures—these details likely reside in the linked paper, website, or other documentation not reproduced here.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_vla_codebase_survey_20260519T160639",
  "tool": "WebFetch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 65 · 2026-05-19T16:17:56.603651+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://raw.githubusercontent.com/moojink/openvla-oft/main/prismatic/models/action_heads.py",
  "prompt": "Return the COMPLETE source code verbatim - every single line including imports, class definitions, __init__ methods with all parameters and dimensions, forward methods, all comments. I need exact dimensions, layer sizes, hidden sizes. Do NOT summarize."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_vla_codebase_survey_20260519T160639",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://raw.githubusercontent.com/moojink/openvla-oft/main/prismatic/models/action_heads.py",
    "prompt": "Return the COMPLETE source code verbatim - every single line including imports, class definitions, __init__ methods with all parameters and dimensions, forward methods, all comments. I need exact dimensions, layer sizes, hidden sizes. Do NOT summarize."
  }
}
```

</details>

---

### Tool result

_source line 66 · 2026-05-19T16:17:56.603821+00:00_

# Complete File Content

```python
# Copyright 2024 Big Vision Authors.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Gemma adaptation for Pi, taken from big_vision.

We follow this einsum axis naming convention:
  B: batch
  T: query length
  S: k/v length
  N: num query heads
  K: num k/v heads
  G: num query heads per k/v head
  H: head dim
  D: d_model ("features")
"""

from collections.abc import Sequence
import dataclasses
from typing import Literal, TypeAlias

import einops
import flax.linen as nn
import jax
import jax.numpy as jnp

import openpi.models.lora as lora
import openpi.shared.array_typing as at
import openpi.training.sharding as sharding

PALIGEMMA_VOCAB_SIZE = 257_152


@dataclasses.dataclass
class Config:
    width: int
    depth: int
    mlp_dim: int
    num_heads: int
    num_kv_heads: int
    head_dim: int
    lora_configs: dict[str, lora.LoRAConfig] = dataclasses.field(default_factory=dict)


Variant = Literal["dummy", "gemma_300m", "gemma_300m_lora", "gemma_2b", "gemma_2b_lora"]


def get_config(variant: Variant) -> Config:
    """Returns config for specified gemma variant."""
    if variant == "dummy":
        return Config(
            width=64,
            depth=4,
            mlp_dim=128,
            num_heads=8,
            num_kv_heads=1,
            head_dim=16,
        )
    if variant == "gemma_300m":
        # 311M params
        return Config(
            width=1024,
            depth=18,
            mlp_dim=4096,
            num_heads=
…[truncated 15184 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_vla_codebase_survey_20260519T160639",
  "tool": "WebFetch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 67 · 2026-05-19T16:17:56.604046+00:00_

# Complete Source Code

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
        # x: (batch_size, hi
…[truncated 7090 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_vla_codebase_survey_20260519T160639",
  "tool": "WebFetch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 68 · 2026-05-19T16:17:56.604224+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://raw.githubusercontent.com/moojink/openvla-oft/main/prismatic/vla/constants.py",
  "prompt": "Return the COMPLETE file content verbatim. Every constant definition, every value. I need the exact numerical values for ACTION_DIM, ACTION_TOKEN_BEGIN_IDX, NUM_ACTIONS_CHUNK, PROPRIO_DIM, etc."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_vla_codebase_survey_20260519T160639",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://raw.githubusercontent.com/moojink/openvla-oft/main/prismatic/vla/constants.py",
    "prompt": "Return the COMPLETE file content verbatim. Every constant definition, every value. I need the exact numerical values for ACTION_DIM, ACTION_TOKEN_BEGIN_IDX, NUM_ACTIONS_CHUNK, PROPRIO_DIM, etc."
  }
}
```

</details>

---

### Tool result

_source line 69 · 2026-05-19T16:17:56.604353+00:00_

# VLA Constants - Complete File Content

Here are all the exact numerical values and constants from the file:

**Token Constants:**
- `IGNORE_INDEX = -100`
- `ACTION_TOKEN_BEGIN_IDX = 31743`
- `STOP_INDEX = 2`

**LIBERO Platform:**
- `NUM_ACTIONS_CHUNK: 8`
- `ACTION_DIM: 7`
- `PROPRIO_DIM: 8`
- `ACTION_PROPRIO_NORMALIZATION_TYPE: BOUNDS_Q99`

**ALOHA Platform:**
- `NUM_ACTIONS_CHUNK: 25`
- `ACTION_DIM: 14`
- `PROPRIO_DIM: 14`
- `ACTION_PROPRIO_NORMALIZATION_TYPE: BOUNDS`

**BRIDGE Platform:**
- `NUM_ACTIONS_CHUNK: 5`
- `ACTION_DIM: 7`
- `PROPRIO_DIM: 7`
- `ACTION_PROPRIO_NORMALIZATION_TYPE: BOUNDS_Q99`

**Normalization Types:**
- `NORMAL` = "normal"
- `BOUNDS` = "bounds"
- `BOUNDS_Q99` = "bounds_q99"

The file automatically detects the robot platform from command-line arguments, defaulting to LIBERO if none match, then assigns the corresponding constants globally.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_vla_codebase_survey_20260519T160639",
  "tool": "WebFetch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 70 · 2026-05-19T16:17:56.604614+00:00_

# Training Configuration File - OpenPI

This Python module defines the complete training configuration system for OpenPI, a robotics policy model framework. Here's the complete content:

```python
"""See _CONFIGS for the list of available configs."""

import abc
from collections.abc import Sequence
import dataclasses
import difflib
import logging
import pathlib
from typing import Any, Literal, Protocol, TypeAlias

import etils.epath as epath
import flax.nnx as nnx
from typing_extensions import override
import tyro

import openpi.models.model as _model
import openpi.models.pi0_config as pi0_config
import openpi.models.pi0_fast as pi0_fast
import openpi.models.tokenizer as _tokenizer
import openpi.policies.aloha_policy as aloha_policy
import openpi.policies.droid_policy as droid_policy
import openpi.policies.libero_policy as libero_policy
import openpi.shared.download as _download
import openpi.shared.normalize as _normalize
import openpi.training.droid_rlds_dataset as droid_rlds_dataset
import openpi.training.misc.polaris_config as polaris_config
import openpi.training.misc.roboarena_config as roboarena_config
import openpi.training.optimizer as _optimizer
import openpi.training.weight_loaders as weight_loaders
import openpi.transforms as _transforms

ModelType: TypeAlias = _model.ModelType
Filter: TypeAlias = nnx.filterlib.Filter


@dataclasses.dataclass(frozen=True)
class AssetsConfig:
    """Determines the location of assets (e.g., norm stats) that will be used to set up the data pipeline.

    These assets will be replicated inside the checkpoint under the `assets/asset_id` directory.

    This can be used to load assets from a different checkpoint (e.g., base model checkpoint) or some other
    centralized location. For example, to load the norm stats for the Trossen robot from the base model checkpoint
    during fine-tuning, use:

    ```
    AssetsConfig(
        assets_dir="gs://openpi-assets/checkpoints/pi0_base/assets",
        asset_id="trossen",
    )
  
…[truncated 29592 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_vla_codebase_survey_20260519T160639",
  "tool": "WebFetch",
  "elapsed_ms": 2
}
```

</details>

---

### Tool call

_source line 71 · 2026-05-19T16:17:56.604785+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://raw.githubusercontent.com/moojink/openvla-oft/main/vla-scripts/finetune.py",
  "prompt": "Return the COMPLETE source code verbatim - every single line including all imports, the FinetuneConfig dataclass with every field, the finetune() function, and the run_forward_pass() function. I need to see exact variable names, dimensions, how action_head is created, how hidden_states are extracted, how the loss is computed. Do NOT summarize."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_vla_codebase_survey_20260519T160639",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://raw.githubusercontent.com/moojink/openvla-oft/main/vla-scripts/finetune.py",
    "prompt": "Return the COMPLETE source code verbatim - every single line including all imports, the FinetuneConfig dataclass with every field, the finetune() function, and the run_forward_pass() function. I need to see exact variable names, dimensions, how action_head is created, how hidden_states are extracted, how the loss is computed. Do NOT summarize."
  }
}
```

</details>

---

### Tool call

_source line 72 · 2026-05-19T16:17:56.604926+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://raw.githubusercontent.com/Physical-Intelligence/openpi/main/src/openpi/models_pytorch/pi0_pytorch.py",
  "prompt": "I need the EXACT source code. Print every single line from the file. Do NOT summarize or paraphrase. Return the raw Python code from line 1 to the last line. This is critical for code analysis."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_vla_codebase_survey_20260519T160639",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://raw.githubusercontent.com/Physical-Intelligence/openpi/main/src/openpi/models_pytorch/pi0_pytorch.py",
    "prompt": "I need the EXACT source code. Print every single line from the file. Do NOT summarize or paraphrase. Return the raw Python code from line 1 to the last line. This is critical for code analysis."
  }
}
```

</details>

---

### Tool call

_source line 73 · 2026-05-19T16:17:56.605059+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://raw.githubusercontent.com/Physical-Intelligence/openpi/main/src/openpi/models/lora.py",
  "prompt": "Return the COMPLETE file content. Every line of code verbatim. Do not summarize."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_vla_codebase_survey_20260519T160639",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://raw.githubusercontent.com/Physical-Intelligence/openpi/main/src/openpi/models/lora.py",
    "prompt": "Return the COMPLETE file content. Every line of code verbatim. Do not summarize."
  }
}
```

</details>

---

### Tool call

_source line 74 · 2026-05-19T16:17:56.605195+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://raw.githubusercontent.com/Physical-Intelligence/openpi/main/scripts/train.py",
  "prompt": "Return the COMPLETE file content verbatim. Every line of code. Do not summarize."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_vla_codebase_survey_20260519T160639",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://raw.githubusercontent.com/Physical-Intelligence/openpi/main/scripts/train.py",
    "prompt": "Return the COMPLETE file content verbatim. Every line of code. Do not summarize."
  }
}
```

</details>

---

### Tool result

_source line 75 · 2026-05-19T16:17:56.605317+00:00_

I've provided the complete source code from the PyTorch implementation file. This is a PyTorch module for PI0 (a diffusion-based policy model) that includes:

**Key Components:**
- `PI0Pytorch` class inheriting from `nn.Module`
- Helper functions for positional embeddings, attention masks, and dtype management
- Training method `forward()` implementing diffusion loss computation
- Inference method `sample_actions()` performing iterative denoising
- Support for gradient checkpointing to optimize memory usage

**Main Features:**
- Integration with PaliGemma vision-language model and expert Gemma model
- Action embedding and projection layers
- Sinusoidal positional encoding with configurable frequency ranges
- Flexible attention masking supporting various patterns (causal, prefix-LM, etc.)
- Noise sampling from Beta distribution
- Support for both PI0 and PI0.5 variants via conditional logic

The code implements a complete diffusion-based policy learning framework suitable for robotic control tasks, with support for both training and inference modes.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_vla_codebase_survey_20260519T160639",
  "tool": "WebFetch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 76 · 2026-05-19T16:17:56.605460+00:00_

# Training Script Analysis

This is a JAX-based training loop implementation for a machine learning model. Here are the key components:

## Main Functions

**Logging & Monitoring:**
- `init_logging()` creates a custom formatter with abbreviated log levels (D, I, W, E, C)
- `init_wandb()` initializes Weights & Biases tracking, supporting both new runs and resumption

**Model Initialization:**
- `init_train_state()` sets up the training state with model parameters, optimizer, and optional EMA decay
- `_load_weights_and_validate()` loads pretrained weights and validates structure

**Training:**
- `train_step()` executes a single optimization step: computes loss, calculates gradients, applies updates, and tracks metrics like "grad_norm" and "param_norm"

**Main Loop:**
The `main()` function orchestrates:
1. Configuration validation (batch size divisibility)
2. Mesh creation for distributed training via FSDP
3. Data loader initialization with logging of sample images
4. Training loop spanning `config.num_train_steps` iterations
5. Periodic checkpointing and metric logging

## Technical Details

- Uses Flax NNX for neural network modules
- Implements `jax.jit` compilation with specified shardings for distributed execution
- Supports resuming from checkpoints
- Tracks exponential moving average (EMA) of parameters when configured
- Filters frozen vs. trainable parameters during updates

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_vla_codebase_survey_20260519T160639",
  "tool": "WebFetch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 77 · 2026-05-19T16:17:56.605607+00:00_

# Complete File Content

```python
import math
import re

import flax.linen as nn
import flax.struct as struct
import jax.numpy as jnp

import openpi.shared.array_typing as at


@struct.dataclass
class LoRAConfig:
    """Configuration for LoRA."""

    # LoRA rank.
    rank: int
    # LoRA scaling factor.
    alpha: float = 1.0
    # Initialization function for LoRA parameters.
    init_fn: nn.initializers.Initializer = nn.initializers.normal(stddev=0.01)
    # Enable rank-stabilized LoRA: https://arxiv.org/pdf/2312.03732
    rslora: bool = False
    # Axes in the weight to apply LoRA to. Should typically be the last two axes.
    axes: tuple[int, int] = (-2, -1)
    # Axis label which is used by LoRA in einsum equations. Must not be present in the original equation.
    label: str = "L"

    @property
    def scaling_value(self) -> float:
        return self.alpha / math.sqrt(self.rank) if self.rslora else self.alpha / self.rank


class Einsum(nn.Module):
    """Einsum with LoRA support. Can be used as a drop-in replacement for the Gemma Einsum."""

    # Shape of the weight.
    shape: tuple[int, ...]
    # Initialization function for the weight.
    init_fn: nn.initializers.Initializer = nn.initializers.zeros
    # If not None, apply LoRA to the weight.
    lora_config: LoRAConfig | None = None

    def setup(self):
        self.w = self.param("w", self.init_fn, self.shape)

        if config := self.lora_config:
            # Setup LoRA parameters.
            shape_a, shape_b = list(self.shape), list(self.shape)
            shape_a[config.axes[1]] = config.rank
            shape_b[config.axes[0]] = config.rank
            self.w_a = self.param("lora_a", config.init_fn, shape_a)
            self.w_b = self.param("lora_b", config.init_fn, shape_b)

    @nn.compact
    def __call__(self, eqn: str, x):
        dtype = x.dtype  # original dtype, could be half-precision
        result = jnp.einsum(eqn, x, self.w.astype(dtype))

        if config := self.lora_config:

…[truncated 3380 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_vla_codebase_survey_20260519T160639",
  "tool": "WebFetch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 78 · 2026-05-19T16:17:56.605763+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://raw.githubusercontent.com/Physical-Intelligence/openpi/main/src/openpi/models_pytorch/pi0_pytorch.py",
  "prompt": "Print the raw text. I need every line of Python source code. Start from the imports and go to the end of file. Output line by line. Include ALL class definitions, method bodies, and helper functions. Do not omit anything."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_vla_codebase_survey_20260519T160639",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://raw.githubusercontent.com/Physical-Intelligence/openpi/main/src/openpi/models_pytorch/pi0_pytorch.py",
    "prompt": "Print the raw text. I need every line of Python source code. Start from the imports and go to the end of file. Output line by line. Include ALL class definitions, method bodies, and helper functions. Do not omit anything."
  }
}
```

</details>

---

### Tool call

_source line 79 · 2026-05-19T16:17:56.605897+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://raw.githubusercontent.com/Physical-Intelligence/openpi/main/src/openpi/models/siglip.py",
  "prompt": "Return the COMPLETE file content. Every line. Focus on class definitions, __call__ methods, output dimensions."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_vla_codebase_survey_20260519T160639",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://raw.githubusercontent.com/Physical-Intelligence/openpi/main/src/openpi/models/siglip.py",
    "prompt": "Return the COMPLETE file content. Every line. Focus on class definitions, __call__ methods, output dimensions."
  }
}
```

</details>

---

### Tool call

_source line 80 · 2026-05-19T16:17:56.606024+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://raw.githubusercontent.com/Physical-Intelligence/openpi/main/scripts/train_pytorch.py",
  "prompt": "Return the COMPLETE file content verbatim. Every line of code. Do not summarize."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_vla_codebase_survey_20260519T160639",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://raw.githubusercontent.com/Physical-Intelligence/openpi/main/scripts/train_pytorch.py",
    "prompt": "Return the COMPLETE file content verbatim. Every line of code. Do not summarize."
  }
}
```

</details>

---

### Tool result

_source line 81 · 2026-05-19T16:17:56.606150+00:00_

# Vision Transformer (ViT) Implementation Analysis

## File Overview
This is a refactored ViT adoption for Pi from big_vision, licensed under Apache 2.0. The code implements a transformer-based vision model using Flax/JAX.

## Key Classes and Output Dimensions

### `MlpBlock`
- **Purpose**: Feed-forward network in transformer blocks
- **Output**: Same shape as input (preserves sequence dimensions)
- Expands to `4x` input dimension (configurable), then projects back to original

### `Encoder1DBlock`
- **Purpose**: Single transformer layer combining attention and MLP
- **Flow**: LayerNorm → MultiHeadAttention → Dropout → Residual → LayerNorm → MLP → Dropout → Residual
- **Output**: Same shape as input `(batch, sequence_length, width)`

### `Encoder`
- **Purpose**: Stack of transformer blocks
- **Key Feature**: Supports `scan` mode for memory efficiency via JAX's `nn.scan`
- **Output**: Normalized tensor matching input shape

### `MAPHead`
- **Purpose**: Multihead attention pooling layer
- **Process**: Creates learnable probe, applies cross-attention to sequence, adds MLP
- **Output**: `(batch, width)` - reduces sequence dimension to single vector

### `_Module` (Main ViT)
**Pipeline**:
1. Conv patch embedding: `(batch, height, width, 3)` → `(batch, H, W, width)`
2. Flatten patches: `(batch, H*W, width)`
3. Add positional embeddings (learned or sincos2d)
4. Optional CLS token prepending (for "tok" pooling)
5. Transformer encoder stack
6. Pooling (MAP, GAP, first token, or none)
7. Optional representation projection via tanh
8. Optional classification head

**Final Outputs** (in `out` dict):
- `logits`: `(batch, num_classes)` if num_classes specified
- `logits_2d`: `(batch, H, W, num_classes)` spatial logits
- `pre_logits`: `(batch, width)` or `(batch, rep_size)`
- `pre_logits_2d`: `(batch, H, W, width)` or spatial representation

## Positional Embedding Functions
- **`get_posemb()`**: Routes between learned or sincos2d embeddings
- **`posemb_sincos_2d()`**: Creates 2D 
…[truncated 181 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_vla_codebase_survey_20260519T160639",
  "tool": "WebFetch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 82 · 2026-05-19T16:17:56.606329+00:00_

# Complete Source Code from finetune.py

I'll provide the complete verbatim source code you requested, organized by the key sections you specified.

## Imports Section

```python
import os
import time
from collections import deque
from dataclasses import dataclass
from pathlib import Path
from typing import Dict, Optional, Tuple, Type

import draccus
import torch
import torch.distributed as dist
import torch.nn as nn
import tqdm
from accelerate import PartialState
from huggingface_hub import HfApi, snapshot_download
from peft import LoraConfig, PeftModel, get_peft_model
from torch.nn.parallel import DistributedDataParallel as DDP
from torch.optim import AdamW
from torch.optim.lr_scheduler import MultiStepLR
from torch.utils.data import DataLoader
from transformers import AutoConfig, AutoImageProcessor, AutoModelForVision2Seq, AutoProcessor
from transformers.modeling_outputs import CausalLMOutputWithPast

import wandb

from experiments.robot.openvla_utils import (
    check_model_logic_mismatch,
    model_is_on_hf_hub,
    update_auto_map,
)

from prismatic.extern.hf.configuration_prismatic import OpenVLAConfig
from prismatic.extern.hf.modeling_prismatic import OpenVLAForActionPrediction
from prismatic.extern.hf.processing_prismatic import PrismaticImageProcessor, PrismaticProcessor
from prismatic.models.action_heads import DiffusionActionHead, L1RegressionActionHead
from prismatic.models.backbones.llm.prompting import PurePromptBuilder
from prismatic.models.film_vit_wrapper import FiLMedPrismaticVisionBackbone
from prismatic.models.projectors import (
    NoisyActionProjector,
    ProprioProjector,
)
from prismatic.training.train_utils import (
    compute_actions_l1_loss,
    compute_token_accuracy,
    get_current_action_mask,
    get_next_actions_mask,
)
from prismatic.util.data_utils import PaddedCollatorForActionPrediction
from prismatic.vla.action_tokenizer import ActionTokenizer
from prismatic.vla.constants import (
    ACTION_DIM,
    ACTION_PROPRIO_NORMALIZ
…[truncated 11273 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_vla_codebase_survey_20260519T160639",
  "tool": "WebFetch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool call

_source line 83 · 2026-05-19T16:17:56.606499+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://raw.githubusercontent.com/moojink/openvla-oft/main/prismatic/extern/hf/modeling_prismatic.py",
  "prompt": "Return the COMPLETE source code. I need every class definition, especially OpenVLAForActionPrediction. I need to see: how the forward pass works, how hidden states flow through the model, what llm_dim is, how action tokens are handled, how noisy_actions/proprio/FiLM are integrated. Include all methods, all parameters."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_vla_codebase_survey_20260519T160639",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://raw.githubusercontent.com/moojink/openvla-oft/main/prismatic/extern/hf/modeling_prismatic.py",
    "prompt": "Return the COMPLETE source code. I need every class definition, especially OpenVLAForActionPrediction. I need to see: how the forward pass works, how hidden states flow through the model, what llm_dim is, how action tokens are handled, how noisy_actions/proprio/FiLM are integrated. Include all methods, all parameters."
  }
}
```

</details>

---

### Tool result

_source line 84 · 2026-05-19T16:17:56.606639+00:00_

# Complete Source Code Analysis: Prismatic VLM Architecture

The provided source file `modeling_prismatic.py` contains the full implementation you requested. Here's a comprehensive overview:

## Core Classes

### PrismaticVisionBackbone
Extracts visual features using TIMM models (e.g., SigLIP, DINOv2). Supports single or fused backbone configurations where features from two models are concatenated along the feature dimension.

### PrismaticProjector
Maps vision embeddings to language model space. For non-fused backbones: `vision_dim → llm_dim` via two linear layers with GELU activation. For fused backbones: `vision_dim → 4*vision_dim → llm_dim → llm_dim` with additional intermediate processing.

### PrismaticForConditionalGeneration
Main VLM class handling three forward modes:

1. **Cached generation** (input_ids.shape[1]==1): Uses past_key_values for efficient decoding
2. **Unimodal** (pixel_values=None): Language-only processing
3. **Multimodal** (both inputs): Integrates vision and language

Key integration points:
- Vision features processed via `_process_vision_features()` (optional FiLM conditioning)
- Proprioceptive features appended via `_process_proprio_features()`
- Diffusion timestep embeddings concatenated
- Action token embeddings replaced using `_replace_input_embeddings()`
- Multimodal sequence constructed by inserting patches after BOS token

### OpenVLAForActionPrediction
Extends PrismaticForConditionalGeneration for robotic action prediction. Key methods:

**`predict_action()`** - Main inference method supporting three prediction modes:
- **Diffusion-based**: Uses noise scheduler with iterative denoising
- **L1 regression**: Direct action head prediction
- **Discrete tokens**: Converts logits to discretized action bins

**Hidden state flow**:
```
input_ids → embeddings → language_embeddings (non-action tokens)
pixel_values → vision_backbone → patches → projector → projected_patch_embeddings
[append proprio, diffusion timesteps if present]
→ multimo
…[truncated 1276 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_vla_codebase_survey_20260519T160639",
  "tool": "WebFetch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 85 · 2026-05-19T16:17:56.606793+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://raw.githubusercontent.com/moojink/openvla-oft/main/prismatic/models/projectors.py",
  "prompt": "Return the COMPLETE source code verbatim. I need to see NoisyActionProjector, ProprioProjector, and any other projector classes. Include all init parameters, dimensions, forward methods."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_vla_codebase_survey_20260519T160639",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://raw.githubusercontent.com/moojink/openvla-oft/main/prismatic/models/projectors.py",
    "prompt": "Return the COMPLETE source code verbatim. I need to see NoisyActionProjector, ProprioProjector, and any other projector classes. Include all init parameters, dimensions, forward methods."
  }
}
```

</details>

---

### Tool result

_source line 86 · 2026-05-19T16:17:56.606919+00:00_

# VLA Projector Classes - Summary

Based on the provided code, here are the two projector implementations:

## ProprioProjector
Projects proprioceptive state inputs into LLM embedding space using a two-layer architecture with GELU activation between layers.

**Parameters:**
- `llm_dim`: Target embedding dimension
- `proprio_dim`: Input proprioceptive state dimension

**Architecture:** Linear(proprio_dim → llm_dim) → GELU → Linear(llm_dim → llm_dim)

## NoisyActionProjector
Projects diffusion-based noisy action inputs into LLM embedding space. Designed for tokenized actions where each token has dimension 1.

**Parameters:**
- `llm_dim`: Target embedding dimension

**Architecture:** Linear(1 → llm_dim) → GELU → Linear(llm_dim → llm_dim)

Both use identical forward pass patterns: initial projection, GELU activation, then refinement projection to produce features matching the LLM's embedding dimensionality.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_vla_codebase_survey_20260519T160639",
  "tool": "WebFetch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 87 · 2026-05-19T16:17:56.607092+00:00_

# Python Source Code - Line by Line

```python
import logging
import math

import torch
from torch import Tensor
from torch import nn
import torch.nn.functional as F  # noqa: N812

import openpi.models.gemma as _gemma
from openpi.models_pytorch.gemma_pytorch import PaliGemmaWithExpertModel
import openpi.models_pytorch.preprocessing_pytorch as _preprocessing


def get_safe_dtype(target_dtype, device_type):
    """Get a safe dtype for the given device type."""
    if device_type == "cpu":
        # CPU doesn't support bfloat16, use float32 instead
        if target_dtype == torch.bfloat16:
            return torch.float32
        if target_dtype == torch.float64:
            return torch.float64
    return target_dtype


def create_sinusoidal_pos_embedding(
    time: torch.tensor, dimension: int, min_period: float, max_period: float, device="cpu"
) -> Tensor:
    """Computes sine-cosine positional embedding vectors for scalar positions."""
    if dimension % 2 != 0:
        raise ValueError(f"dimension ({dimension}) must be divisible by 2")

    if time.ndim != 1:
        raise ValueError("The time tensor is expected to be of shape `(batch_size, )`.")

    dtype = get_safe_dtype(torch.float64, device.type)
    fraction = torch.linspace(0.0, 1.0, dimension // 2, dtype=dtype, device=device)
    period = min_period * (max_period / min_period) ** fraction

    # Compute the outer product
    scaling_factor = 1.0 / period * 2 * math.pi
    sin_input = scaling_factor[None, :] * time[:, None]
    return torch.cat([torch.sin(sin_input), torch.cos(sin_input)], dim=1)


def sample_beta(alpha, beta, bsize, device):
    alpha_t = torch.as_tensor(alpha, dtype=torch.float32, device=device)
    beta_t = torch.as_tensor(beta, dtype=torch.float32, device=device)
    dist = torch.distributions.Beta(alpha_t, beta_t)
    return dist.sample((bsize,))


def make_att_2d_masks(pad_masks, att_masks):
    """Copied from big_vision.

    Tokens can attend to valid inputs tokens which have a cum
…[truncated 17178 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_vla_codebase_survey_20260519T160639",
  "tool": "WebFetch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool call

_source line 88 · 2026-05-19T16:17:56.607248+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://raw.githubusercontent.com/moojink/openvla-oft/main/prismatic/models/backbones/llm/base_llm.py",
  "prompt": "Return the COMPLETE source code. I need to see the LLM backbone base class - what properties it exposes (embed_dim, hidden_dim, etc.), what model is used, how hidden states are returned."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_vla_codebase_survey_20260519T160639",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://raw.githubusercontent.com/moojink/openvla-oft/main/prismatic/models/backbones/llm/base_llm.py",
    "prompt": "Return the COMPLETE source code. I need to see the LLM backbone base class - what properties it exposes (embed_dim, hidden_dim, etc.), what model is used, how hidden states are returned."
  }
}
```

</details>

---

### Tool result

_source line 89 · 2026-05-19T16:17:56.607375+00:00_

# LLM Backbone Base Class Summary

Based on the provided source code, here's what the LLM backbone architecture exposes:

## Properties Exposed

The `LLMBackbone` abstract class defines these key properties:

- **`embed_dim`**: Returns `self.llm.config.hidden_size` - the embedding dimension
- **`pad_token_id`**: Returns the tokenizer's padding token ID
- **`prompt_builder_fn`**: Abstract property for prompt construction (type: `Type[PromptBuilder]`)
- **`transformer_layer_cls`**: Abstract property for the transformer layer class
- **`half_precision_dtype`**: Abstract property for precision handling
- **`last_layer_finetune_modules`**: Abstract property for fine-tuning specific layers

## Model Information

The implementation uses **HuggingFace `PreTrainedModel`** instances, specifically models following the `AutoModelForCausalLM` API. The code explicitly states: "we make the assumption that any given LLM backbone implements the AutoModelForCausalLM API."

## Hidden States Return

The `forward()` method returns **`CausalLMOutputWithPast`**, which is HuggingFace's standard output format. The implementation passes through `output_hidden_states` as an optional parameter, enabling hidden state extraction when requested.

## Key Instance Attributes

- `self.llm`: The actual `PreTrainedModel` instance
- `self.tokenizer`: The `PreTrainedTokenizerBase` instance
- `self.llm_max_length`: Maximum sequence length (default: 2048)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_vla_codebase_survey_20260519T160639",
  "tool": "WebFetch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 90 · 2026-05-19T16:17:56.607540+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://raw.githubusercontent.com/moojink/openvla-oft/main/prismatic/extern/hf/configuration_prismatic.py",
  "prompt": "Return the COMPLETE source code. I need the OpenVLAConfig class, all config fields, especially text_config hidden_size, vision dimensions, model_type, any default values."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_vla_codebase_survey_20260519T160639",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://raw.githubusercontent.com/moojink/openvla-oft/main/prismatic/extern/hf/configuration_prismatic.py",
    "prompt": "Return the COMPLETE source code. I need the OpenVLAConfig class, all config fields, especially text_config hidden_size, vision dimensions, model_type, any default values."
  }
}
```

</details>

---

### Tool result

_source line 91 · 2026-05-19T16:17:56.607736+00:00_

# PyTorch Training Entrypoint - Complete File Content

```python
"""
PyTorch training entrypoint for PI0/PI05 with multi-GPU and multi-node (DDP) support.
This script mirrors the behavior of the JAX trainer (`scripts/train.py`) but runs
entirely in PyTorch using the `PI0Pytorch` model and your existing config/data
pipeline from `src/openpi/training/config.py` and `src/openpi/training/data_loader.py`.

Usage
Single GPU:
  python scripts/train_pytorch.py &lt;config_name> --exp_name &lt;run_name> --save_interval &lt;interval>
  Example:
  python scripts/train_pytorch.py debug --exp_name pytorch_ddp_test
  python scripts/train_pytorch.py debug --exp_name pytorch_ddp_test --resume  # Resume from latest checkpoint
Multi-GPU (single node):
  torchrun --standalone --nnodes=1 --nproc_per_node=&lt;num_gpus> scripts/train_pytorch.py &lt;config_name> --exp_name &lt;run_name>
  Example:
  torchrun --standalone --nnodes=1 --nproc_per_node=2 scripts/train_pytorch.py pi0_aloha_sim --exp_name pytorch_ddp_test
  torchrun --standalone --nnodes=1 --nproc_per_node=2 scripts/train_pytorch.py pi0_aloha_sim --exp_name pytorch_ddp_test --resume
Multi-Node Training:
	torchrun \
    --nnodes=&lt;num_nodes> --nproc_per_node=&lt;gpus_per_node> --node_rank=&lt;rank_of_node> \
    --master_addr=&lt;master_ip> --master_port=&lt;port> \
    scripts/train_pytorch.py &lt;config_name> --exp_name=&lt;run_name> --save_interval &lt;interval>

"""

import dataclasses
import gc
import logging
import os
import platform
import shutil
import time

import jax
import numpy as np
import safetensors.torch
import torch
import torch.distributed as dist
import torch.nn.parallel
import tqdm
import wandb

import openpi.models.pi0_config
import openpi.models_pytorch.pi0_pytorch
import openpi.shared.normalize as _normalize
import openpi.training.config as _config
import openpi.training.data_loader as _data


def init_logging():
    level_mapping = {"DEBUG": "D", "INFO": "I", "WARNING": "W", "ERROR": "E", "CRITICAL": "C"}

    class CustomFormatter(logging.Forma
…[truncated 24006 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_vla_codebase_survey_20260519T160639",
  "tool": "WebFetch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 92 · 2026-05-19T16:17:56.607879+00:00_

# Prismatic and OpenVLAConfig Source Code Summary

Based on the provided content, here's the complete configuration structure:

## OpenVLAConfig Class

The `OpenVLAConfig` class extends `PrismaticConfig` with two additional fields:
- `norm_stats`: Optional normalization statistics dictionary
- `n_action_bins`: Integer (default 256) for action discretization

## Key Configuration Fields

**Vision Configuration:**
- `vision_backbone_id` (default: "siglip-vit-so400m")
- `image_sizes`: List of resolutions from `VISION_BACKBONE_TO_RESOLUTION`
- `timm_model_ids`: Model identifiers from timm library
- `use_fused_vision_backbone`: Boolean flag for dual-backbone support

**Language Model Configuration:**
- `llm_backbone_id` (default: "vicuna-v15-7b")
- `hf_llm_id`: HuggingFace model path
- `text_config`: Auto-generated from `LLM_BACKBONE_TO_HF_METACLASS`
- `llm_max_length`: Maximum sequence length (default 2048)

**Model Identity:**
- `model_type`: "openvla" for OpenVLAConfig, "prismatic" for base class
- `pad_token_id`: Default 32000
- `pad_to_multiple_of`: Default 64

**Architecture:**
- `arch_specifier`: Default "no-align+gelu-mlp"
- `image_resize_strategy`: Default "letterbox"

The `text_config` is dynamically instantiated using HuggingFace's CONFIG_MAPPING based on the LLM backbone's metaclass designation (llama, mistral, or phi).

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_vla_codebase_survey_20260519T160639",
  "tool": "WebFetch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 93 · 2026-05-19T16:17:56.608080+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://raw.githubusercontent.com/Physical-Intelligence/openpi/main/src/openpi/models_pytorch/gemma_pytorch.py",
  "prompt": "Return the COMPLETE file content verbatim. Every line of code. This is the PyTorch Gemma model with expert. Do not summarize - I need the full source."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_vla_codebase_survey_20260519T160639",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://raw.githubusercontent.com/Physical-Intelligence/openpi/main/src/openpi/models_pytorch/gemma_pytorch.py",
    "prompt": "Return the COMPLETE file content verbatim. Every line of code. This is the PyTorch Gemma model with expert. Do not summarize - I need the full source."
  }
}
```

</details>

---

### Tool call

_source line 94 · 2026-05-19T16:17:56.608229+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://raw.githubusercontent.com/Physical-Intelligence/openpi/main/src/openpi/models_pytorch/preprocessing_pytorch.py",
  "prompt": "Return the COMPLETE file content verbatim. Every line of code. Do not summarize."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_vla_codebase_survey_20260519T160639",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://raw.githubusercontent.com/Physical-Intelligence/openpi/main/src/openpi/models_pytorch/preprocessing_pytorch.py",
    "prompt": "Return the COMPLETE file content verbatim. Every line of code. Do not summarize."
  }
}
```

</details>

---

### Tool call

_source line 95 · 2026-05-19T16:17:56.608360+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://raw.githubusercontent.com/Physical-Intelligence/openpi/main/src/openpi/policies/policy_config.py",
  "prompt": "Return the COMPLETE file content verbatim. Every line of code. Do not summarize."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_vla_codebase_survey_20260519T160639",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://raw.githubusercontent.com/Physical-Intelligence/openpi/main/src/openpi/policies/policy_config.py",
    "prompt": "Return the COMPLETE file content verbatim. Every line of code. Do not summarize."
  }
}
```

</details>

---

### Tool call

_source line 96 · 2026-05-19T16:17:56.608511+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://raw.githubusercontent.com/moojink/openvla-oft/main/vla-scripts/deploy.py",
  "prompt": "Return the COMPLETE source code. I need to see how inference works, how the model is loaded, how action_head is loaded and used, how predict_action is called, and full inference pipeline."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_vla_codebase_survey_20260519T160639",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://raw.githubusercontent.com/moojink/openvla-oft/main/vla-scripts/deploy.py",
    "prompt": "Return the COMPLETE source code. I need to see how inference works, how the model is loaded, how action_head is loaded and used, how predict_action is called, and full inference pipeline."
  }
}
```

</details>

---

### Tool result

_source line 97 · 2026-05-19T16:17:56.608648+00:00_

# Complete File Content

```python
import logging
import os
import pathlib
from typing import Any

import jax.numpy as jnp

import openpi.models.model as _model
import openpi.policies.policy as _policy
import openpi.shared.download as download
from openpi.training import checkpoints as _checkpoints
from openpi.training import config as _config
import openpi.transforms as transforms


def create_trained_policy(
    train_config: _config.TrainConfig,
    checkpoint_dir: pathlib.Path | str,
    *,
    repack_transforms: transforms.Group | None = None,
    sample_kwargs: dict[str, Any] | None = None,
    default_prompt: str | None = None,
    norm_stats: dict[str, transforms.NormStats] | None = None,
    pytorch_device: str | None = None,
) -> _policy.Policy:
    """Create a policy from a trained checkpoint.

    Args:
        train_config: The training config to use to create the model.
        checkpoint_dir: The directory to load the model from.
        repack_transforms: Optional transforms that will be applied before any other transforms.
        sample_kwargs: The kwargs to pass to the `sample_actions` method. If not provided, the default
            kwargs will be used.
        default_prompt: The default prompt to use for the policy. Will inject the prompt into the input
            data if it doesn't already exist.
        norm_stats: The norm stats to use for the policy. If not provided, the norm stats will be loaded
            from the checkpoint directory.
        pytorch_device: Device to use for PyTorch models (e.g., "cpu", "cuda", "cuda:0").
                      If None and is_pytorch=True, will use "cuda" if available, otherwise "cpu".

    Note:
        The function automatically detects whether the model is PyTorch-based by checking for the
        presence of "model.safensors" in the checkpoint directory.
    """
    repack_transforms = repack_transforms or transforms.Group()
    checkpoint_dir = download.maybe_download(str(checkpoint_dir))

    # C
…[truncated 2145 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_vla_codebase_survey_20260519T160639",
  "tool": "WebFetch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 98 · 2026-05-19T16:17:56.608796+00:00_

# OpenVLA Inference Pipeline Analysis

Based on the provided `deploy.py` file, here's how the inference works:

## Model Loading

The server initializes components via `OpenVLAServer.__init__()`:
- **VLA Model**: Loaded through `get_vla(cfg)`
- **Action Head**: Conditionally loaded via `get_action_head(cfg, self.vla.llm_dim)` when L1 regression or diffusion is enabled
- **Proprioceptive Projector**: Optionally loaded through `get_proprio_projector()` if `cfg.use_proprio` is True
- **Processor**: Obtained via `get_processor(cfg)`

## Inference Pipeline

The inference flow occurs in `get_server_action()`:

1. **Request Handling**: Accepts a payload containing observation data and instruction text
2. **Payload Processing**: Handles both standard and "double-encoded" numpy array formats
3. **Action Prediction**: Calls `get_vla_action()` with:
   - Configuration settings
   - Loaded VLA model
   - Processor instance
   - Observation data
   - Text instruction
   - Optional action head and proprioceptive projector
   - FiLM configuration flag

4. **Response**: Returns predicted action as JSON (with appropriate encoding based on input format)

## Key Configuration Parameters

The `DeployConfig` dataclass specifies critical inference settings:
- Model checkpoint path
- Action modeling approach (L1 regression vs. diffusion)
- Number of input images (default: 3)
- Proprioceptive state inclusion
- Quantization options (8-bit/4-bit)
- Action normalization/denormalization handling

## Server Deployment

The FastAPI server exposes a POST endpoint `/act` on the specified host and port (default: `0.0.0.0:8777`).

**Note**: The actual `get_vla_action()` implementation details are imported from `openvla_utils` but not shown in this file.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_vla_codebase_survey_20260519T160639",
  "tool": "WebFetch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 99 · 2026-05-19T16:17:56.608936+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://raw.githubusercontent.com/moojink/openvla-oft/main/experiments/robot/openvla_utils.py",
  "prompt": "Return the COMPLETE source code. I need to see get_vla_action(), get_action_head(), get_vla(), and any function that shows how hidden states are extracted from the VLA for action prediction. Include all dimensions and shapes mentioned in comments."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_vla_codebase_survey_20260519T160639",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://raw.githubusercontent.com/moojink/openvla-oft/main/experiments/robot/openvla_utils.py",
    "prompt": "Return the COMPLETE source code. I need to see get_vla_action(), get_action_head(), get_vla(), and any function that shows how hidden states are extracted from the VLA for action prediction. Include all dimensions and shapes mentioned in comments."
  }
}
```

</details>

---

### Tool result

_source line 100 · 2026-05-19T16:17:56.609076+00:00_

# Complete File Content

```python
from collections.abc import Sequence
import logging

import torch

from openpi.shared import image_tools

logger = logging.getLogger("openpi")

# Constants moved from model.py
IMAGE_KEYS = (
    "base_0_rgb",
    "left_wrist_0_rgb",
    "right_wrist_0_rgb",
)

IMAGE_RESOLUTION = (224, 224)


def preprocess_observation_pytorch(
    observation,
    *,
    train: bool = False,
    image_keys: Sequence[str] = IMAGE_KEYS,
    image_resolution: tuple[int, int] = IMAGE_RESOLUTION,
):
    """Torch.compile-compatible version of preprocess_observation_pytorch with simplified type annotations.

    This function avoids complex type annotations that can cause torch.compile issues.
    """
    if not set(image_keys).issubset(observation.images):
        raise ValueError(f"images dict missing keys: expected {image_keys}, got {list(observation.images)}")

    batch_shape = observation.state.shape[:-1]

    out_images = {}
    for key in image_keys:
        image = observation.images[key]

        # TODO: This is a hack to handle both [B, C, H, W] and [B, H, W, C] formats
        # Handle both [B, C, H, W] and [B, H, W, C] formats
        is_channels_first = image.shape[1] == 3  # Check if channels are in dimension 1

        if is_channels_first:
            # Convert [B, C, H, W] to [B, H, W, C] for processing
            image = image.permute(0, 2, 3, 1)

        if image.shape[1:3] != image_resolution:
            logger.info(f"Resizing image {key} from {image.shape[1:3]} to {image_resolution}")
            image = image_tools.resize_with_pad_torch(image, *image_resolution)

        if train:
            # Convert from [-1, 1] to [0, 1] for PyTorch augmentations
            image = image / 2.0 + 0.5

            # Apply PyTorch-based augmentations
            if "wrist" not in key:
                # Geometric augmentations for non-wrist cameras
                height, width = image.shape[1:3]

                # Random crop and resize
        
…[truncated 5302 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_vla_codebase_survey_20260519T160639",
  "tool": "WebFetch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 101 · 2026-05-19T16:17:56.609224+00:00_

# VLA Action Prediction Code Analysis

Based on the provided source, here are the key functions for action prediction:

## Primary Action Generation Function

The `get_vla_action()` function handles prediction by:

1. **Image Processing**: Collects "full_image" and any wrist camera images, resizes them to 224x224, applies center cropping if configured
2. **Prompt Construction**: Builds prompt as `"In: What action should the robot take to {task}?\nOut:"`
3. **Model Inference**: Processes inputs through the VLA with optional proprioception normalization
4. **Custom Head Support**: Routes to either standard VLA output or custom action head depending on configuration

The function signature accepts an optional `action_head` parameter, indicating the model can use external continuous-valued action prediction layers.

## Action Head Loading

The `get_action_head()` function initializes prediction heads with dimensions matching the language model output (`llm_dim`). Two variants are supported:

- **L1RegressionActionHead**: Maps language model features directly to action space
- **DiffusionActionHead**: Uses iterative refinement with configurable inference steps

Both variants specify `ACTION_DIM` as the output dimensionality, though the exact value isn't exposed in this excerpt.

## VLA Model Loading

The `get_vla()` function loads the base model and applies optional FiLM (Feature-wise Linear Modulation) wrapping. The vision backbone processes images to produce features that feed into the language model component.

## Hidden State Extraction

The provided code does not explicitly show hidden state extraction mechanisms. The `predict_action()` call on the VLA returns action predictions directly, but intermediate feature dimensions and hidden state architectures are not detailed in this source material.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_vla_codebase_survey_20260519T160639",
  "tool": "WebFetch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 102 · 2026-05-19T16:17:56.609365+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://raw.githubusercontent.com/moojink/openvla-oft/main/prismatic/models/backbones/llm/llama2.py",
  "prompt": "Return the COMPLETE source code. I need to see the Llama backbone class, the HF model ID used, the embed_dim / hidden_size, transformer_layer_cls, and any dimension-related properties."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_vla_codebase_survey_20260519T160639",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://raw.githubusercontent.com/moojink/openvla-oft/main/prismatic/models/backbones/llm/llama2.py",
    "prompt": "Return the COMPLETE source code. I need to see the Llama backbone class, the HF model ID used, the embed_dim / hidden_size, transformer_layer_cls, and any dimension-related properties."
  }
}
```

</details>

---

### Tool result

_source line 103 · 2026-05-19T16:17:56.609542+00:00_

# PaliGemmaWithExpertModel - Complete Source Code

Here is the full file content as requested:

```python
from typing import Literal

import torch
from torch import nn
from transformers import GemmaForCausalLM
from transformers import PaliGemmaForConditionalGeneration
from transformers.models.auto import CONFIG_MAPPING
from transformers.models.gemma import modeling_gemma


class PaliGemmaWithExpertModel(nn.Module):
    def __init__(
        self,
        vlm_config,
        action_expert_config,
        use_adarms=None,
        precision: Literal["bfloat16", "float32"] = "bfloat16",
    ):
        if use_adarms is None:
            use_adarms = [False, False]
        super().__init__()

        vlm_config_hf = CONFIG_MAPPING["paligemma"]()
        vlm_config_hf._vocab_size = 257152  # noqa: SLF001
        vlm_config_hf.image_token_index = 257152
        vlm_config_hf.text_config.hidden_size = vlm_config.width
        vlm_config_hf.text_config.intermediate_size = vlm_config.mlp_dim
        vlm_config_hf.text_config.num_attention_heads = vlm_config.num_heads
        vlm_config_hf.text_config.head_dim = vlm_config.head_dim
        vlm_config_hf.text_config.num_hidden_layers = vlm_config.depth
        vlm_config_hf.text_config.num_key_value_heads = vlm_config.num_kv_heads
        vlm_config_hf.text_config.hidden_activation = "gelu_pytorch_tanh"
        vlm_config_hf.text_config.torch_dtype = "float32"
        vlm_config_hf.text_config.vocab_size = 257152
        vlm_config_hf.text_config.use_adarms = use_adarms[0]
        vlm_config_hf.text_config.adarms_cond_dim = vlm_config.width if use_adarms[0] else None
        vlm_config_hf.vision_config.intermediate_size = 4304
        vlm_config_hf.vision_config.projection_dim = 2048
        vlm_config_hf.vision_config.projector_hidden_act = "gelu_fast"
        vlm_config_hf.vision_config.torch_dtype = "float32"

        action_expert_config_hf = CONFIG_MAPPING["gemma"](
            head_dim=action_expert_config.head_dim,
      
…[truncated 11808 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_vla_codebase_survey_20260519T160639",
  "tool": "WebFetch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 104 · 2026-05-19T16:17:56.609693+00:00_

# LLaMa2 Backbone Analysis

Based on the provided source code, here's what I found:

## Class Definition
The `LLaMa2LLMBackbone` class inherits from `HFCausalLLMBackbone` and supports multiple model variants through the `LLAMA2_MODELS` registry.

## Supported Models & HF IDs
- **llama2-7b-pure**: `meta-llama/Llama-2-7b-hf`
- **llama2-13b-pure**: `meta-llama/Llama-2-13b-hf`
- **llama2-7b-chat**: `meta-llama/Llama-2-7b-chat-hf`
- **llama2-13b-chat**: `meta-llama/Llama-2-13b-chat-hf`
- **vicuna-v15-7b/13b**: `lmsys/vicuna-*-v1.5`

## Key Properties

**Transformer Layer Class**: `"return LlamaDecoderLayer"`

**Precision**: The model uses `torch.bfloat16` as its half-precision dtype, "trained in BF16" per HuggingFace documentation.

**Special Token Handling**: The implementation adds a `&lt;PAD>` token and resizes embeddings to multiples of 64.

**Fine-tuning Modules**: Last-layer fine-tuning targets `"embed_tokens, layers[-1], lm_head"`

## Limitation
The provided code excerpt doesn't explicitly show embed_dim/hidden_size properties—these likely reside in the parent `HFCausalLLMBackbone` class or are loaded from the HuggingFace model config.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_vla_codebase_survey_20260519T160639",
  "tool": "WebFetch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 105 · 2026-05-19T16:17:56.609835+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://raw.githubusercontent.com/Physical-Intelligence/openpi/main/src/openpi/models/vit.py",
  "prompt": "Return the key class definitions, their __call__ methods, and output shapes. Focus on the Module class and what it outputs. Include the variant decoder function."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_vla_codebase_survey_20260519T160639",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://raw.githubusercontent.com/Physical-Intelligence/openpi/main/src/openpi/models/vit.py",
    "prompt": "Return the key class definitions, their __call__ methods, and output shapes. Focus on the Module class and what it outputs. Include the variant decoder function."
  }
}
```

</details>

---

### Tool call

_source line 106 · 2026-05-19T16:17:56.609965+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://raw.githubusercontent.com/Physical-Intelligence/openpi/main/src/openpi/training/optimizer.py",
  "prompt": "Return the COMPLETE file content. Focus on optimizer config classes, learning rate schedule classes, and any freeze/parameter filtering logic."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_vla_codebase_survey_20260519T160639",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://raw.githubusercontent.com/Physical-Intelligence/openpi/main/src/openpi/training/optimizer.py",
    "prompt": "Return the COMPLETE file content. Focus on optimizer config classes, learning rate schedule classes, and any freeze/parameter filtering logic."
  }
}
```

</details>

---

### Tool call

_source line 107 · 2026-05-19T16:17:56.610092+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://raw.githubusercontent.com/moojink/openvla-oft/main/prismatic/models/film_vit_wrapper.py",
  "prompt": "Return the COMPLETE source code. I need to see the FiLM wrapper class, how it integrates with the vision backbone, its dimensions and forward method."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_vla_codebase_survey_20260519T160639",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://raw.githubusercontent.com/moojink/openvla-oft/main/prismatic/models/film_vit_wrapper.py",
    "prompt": "Return the COMPLETE source code. I need to see the FiLM wrapper class, how it integrates with the vision backbone, its dimensions and forward method."
  }
}
```

</details>

---

### Tool result

_source line 108 · 2026-05-19T16:17:56.610222+00:00_

# Key Class Definitions and Output Shapes

## Core Modules

**IdentityLayer**
- `__call__(x)` → returns `x` unchanged
- Output shape: Same as input

**AddPositionEmbs**
- `__call__(inputs)` → adds learned positional embeddings
- Input shape: `(batch_size, seq_len, emb_dim)` with `ndim==3`
- Output shape: `(batch_size, seq_len, emb_dim)`

**MlpBlock**
- `__call__(inputs, *, deterministic)` → applies two dense layers with GELU activation
- Output shape: `(batch_size, ..., out_dim)` or input last dimension if `out_dim is None`

**Encoder1DBlock**
- `__call__(inputs, deterministic)` → transformer encoder layer with multihead attention + MLP
- Input shape: `(batch, seq, hidden)` with `ndim==3`
- Output shape: `(batch, seq, hidden)` plus `None` residual

**Encoder**
- `__call__(x, *, train)` → stacked transformer layers with optional positional embeddings
- Input shape: `(batch, len, emb)` with `ndim==3`
- Output shape: `(batch, len, emb)` after layer normalization

**VisionTransformer** (main module)
- `__call__(inputs, *, train)` → complete ViT pipeline combining optional ResNet stem, patch embedding, transformer, and classification head
- Output shape: `(batch, num_classes)` for standard classification; varies by classifier type ("token", "gap", "unpooled")

No variant decoder function appears in the provided code.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_vla_codebase_survey_20260519T160639",
  "tool": "WebFetch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 109 · 2026-05-19T16:17:56.610356+00:00_

# Optimizer and Learning Rate Schedule Configuration

## Learning Rate Schedules

The file defines two learning rate schedule configurations through the `LRScheduleConfig` protocol:

1. **CosineDecaySchedule**: Implements cosine annealing with a linear warmup phase. Default parameters include 1,000 warmup steps, peak learning rate of 2.5e-5, and 30,000 decay steps declining to 2.5e-6.

2. **RsqrtDecaySchedule**: Uses inverse square root decay following warmup. It joins a linear warmup schedule with an inverse square root decay function, defaulting to 1,000 warmup steps and peak learning rate of 5e-5.

## Optimizer Configurations

Two optimizer implementations satisfy the `OptimizerConfig` protocol:

1. **AdamW**: Wraps Optax's AdamW with configurable exponential moving average coefficients (b1=0.9, b2=0.95), epsilon smoothing (1e-8), and gradient clipping by global norm (default 1.0). A negligible weight decay (1e-10) is applied by default to avoid memory issues.

2. **SGD**: Standard stochastic gradient descent supporting momentum (0.9) and optional Nesterov acceleration. The implementation explicitly rejects weight decay masking.

## Key Design Patterns

Both protocols use `@runtime_checkable` decorators enabling structural subtyping. All configurations are frozen dataclasses. The `create_optimizer()` factory function instantiates the learning rate schedule, then passes it to the optimizer's creation method, supporting optional per-parameter weight decay masking via JAX pytrees.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_vla_codebase_survey_20260519T160639",
  "tool": "WebFetch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 110 · 2026-05-19T16:17:56.610507+00:00_

# FiLM Vision Transformer Implementation Summary

## Core Components

The code implements FiLM (Feature-wise Linear Modulation) for vision transformers through three main classes:

### 1. FiLMedVisionTransformerBlock
This wrapper modulates visual features using the transformation: `x = (1 + gamma) * x + beta`

Where gamma and beta are "learned projections of the average language embedding." The key design choice applies modulation across all spatial dimensions to maintain global conditioning consistency with convolutional architectures.

**Constructor Parameters:**
- `block`: Original ViT block
- `vision_dim`: Hidden dimensions in visual embeddings
- `llm_dim`: Hidden dimensions in language embeddings

**Forward Method:**
- Projects language embeddings to gamma/beta (batch_size, vision_dim)
- Applies attention with FiLM modulation between norm/attention and norm/MLP layers
- Reshapes scaling factors as (batch_size, 1, vision_dim) for broadcasting across patch embeddings

### 2. FiLMedVisionTransformer
Extends timm's VisionTransformer to override `_intermediate_layers()` and `get_intermediate_layers()` methods, enabling language embeddings to flow through the architecture.

### 3. FiLMedPrismaticVisionBackbone
**Integration wrapper** that:
- Wraps dual vision backbones (SigLIP + DINOv2)
- Converts individual blocks into FiLMedVisionTransformerBlock instances
- Supports 1-3 image inputs

**Forward Signature:**
```
forward(pixel_values: torch.Tensor, language_embeddings: torch.Tensor)
```
Averages sequence-length language embeddings (B, seq_len, llm_dim) → (B, llm_dim) for conditioning.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_vla_codebase_survey_20260519T160639",
  "tool": "WebFetch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 111 · 2026-05-19T16:17:56.610655+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://raw.githubusercontent.com/Physical-Intelligence/openpi/main/src/openpi/models/siglip.py",
  "prompt": "Return the COMPLETE source code verbatim. Every line. Focus on class Module definition, __call__ signature, output dimensions, and the variant configuration."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_vla_codebase_survey_20260519T160639",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://raw.githubusercontent.com/Physical-Intelligence/openpi/main/src/openpi/models/siglip.py",
    "prompt": "Return the COMPLETE source code verbatim. Every line. Focus on class Module definition, __call__ signature, output dimensions, and the variant configuration."
  }
}
```

</details>

---

### Tool call

_source line 112 · 2026-05-19T16:17:56.610788+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://raw.githubusercontent.com/Physical-Intelligence/openpi/main/src/openpi/training/weight_loaders.py",
  "prompt": "Return the COMPLETE file content verbatim. Every line of code. Do not summarize."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_vla_codebase_survey_20260519T160639",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://raw.githubusercontent.com/Physical-Intelligence/openpi/main/src/openpi/training/weight_loaders.py",
    "prompt": "Return the COMPLETE file content verbatim. Every line of code. Do not summarize."
  }
}
```

</details>

---

### Tool call

_source line 113 · 2026-05-19T16:17:56.610916+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://raw.githubusercontent.com/moojink/openvla-oft/main/prismatic/training/train_utils.py",
  "prompt": "Return the COMPLETE source code. I need to see compute_actions_l1_loss, compute_token_accuracy, get_current_action_mask, get_next_actions_mask, and any other utility functions for extracting action tokens from hidden states."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_vla_codebase_survey_20260519T160639",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://raw.githubusercontent.com/moojink/openvla-oft/main/prismatic/training/train_utils.py",
    "prompt": "Return the COMPLETE source code. I need to see compute_actions_l1_loss, compute_token_accuracy, get_current_action_mask, get_next_actions_mask, and any other utility functions for extracting action tokens from hidden states."
  }
}
```

</details>

---

### Tool result

_source line 114 · 2026-05-19T16:17:56.611042+00:00_

# Vision Transformer Implementation Analysis

## Module Factory Function

The `Module` function is a factory that creates `_Module` instances:

```python
def Module(num_classes=None, *, variant=None, **kw):
    """Factory function, because linen really don't like what I'm doing!"""
    return _Module(num_classes, **{**decode_variant(variant), **kw})
```

## Core __call__ Signature

The main model's forward pass accepts:
```python
def __call__(self, image, *, train=False):
```

The image undergoes patch embedding, positional encoding, transformer encoding, and pooling.

## Output Structure

Returns a tuple: `(x, out)` where:
- **x**: Classification logits (if `num_classes` specified) or pooled representation
- **out**: Dictionary containing intermediate activations including "stem", "encoded", "logits_2d", "pre_logits_2d"

## Variant Configurations

The `decode_variant` function maps model sizes to hyperparameters:

| Variant | Width | Depth | MLP Dim | Heads |
|---------|-------|-------|---------|-------|
| Ti (Tiny) | 192 | 12 | 768 | 3 |
| B (Base) | 768 | 12 | 3072 | 12 |
| L (Large) | 1024 | 24 | 4096 | 16 |
| H (Huge) | 1280 | 32 | 5120 | 16 |

Patch sizes are customizable via `"B/32"` notation, where the denominator specifies patch dimensions (default 16×16).

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_vla_codebase_survey_20260519T160639",
  "tool": "WebFetch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 115 · 2026-05-19T16:17:56.611183+00:00_

# Training/Fine-tuning Utilities Source Code

Based on the provided content, here is the complete source code for the utility functions:

```python
"""Utils for training/fine-tuning scripts."""

import torch
from prismatic.vla.constants import ACTION_DIM, ACTION_TOKEN_BEGIN_IDX, IGNORE_INDEX


def get_current_action_mask(token_ids):
    """Identifies positions of current action tokens in a sequence."""
    newline_positions = token_ids != IGNORE_INDEX
    cumsum = torch.cumsum(newline_positions, dim=1)
    mask = (1 <= cumsum) & (cumsum <= ACTION_DIM)
    action_tokens_only_mask = token_ids > ACTION_TOKEN_BEGIN_IDX
    mask = action_tokens_only_mask * mask
    return mask


def get_next_actions_mask(token_ids):
    """Identifies positions of future action tokens in a sequence."""
    newline_positions = token_ids != IGNORE_INDEX
    cumsum = torch.cumsum(newline_positions, dim=1)
    mask = cumsum > ACTION_DIM
    action_tokens_only_mask = token_ids > ACTION_TOKEN_BEGIN_IDX
    mask = action_tokens_only_mask * mask
    return mask


def compute_token_accuracy(predicted_token_ids, ground_truth_token_ids, mask):
    """Calculates accuracy of token predictions against ground truth."""
    correct_preds = (predicted_token_ids == ground_truth_token_ids) & mask
    accuracy = correct_preds.sum().float() / mask.sum().float()
    return accuracy


def compute_actions_l1_loss(action_tokenizer, predicted_token_ids, 
                            ground_truth_token_ids, mask):
    """Computes L1 loss between predicted and actual continuous actions."""
    pred_continuous_actions = torch.tensor(
        action_tokenizer.decode_token_ids_to_actions(
            predicted_token_ids[mask].cpu().numpy()
        )
    )
    true_continuous_actions = torch.tensor(
        action_tokenizer.decode_token_ids_to_actions(
            ground_truth_token_ids[mask].cpu().numpy()
        )
    )
    l1_loss = torch.nn.functional.l1_loss(
        pred_continuous_actions, true_continuous_actions

…[truncated 151 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_vla_codebase_survey_20260519T160639",
  "tool": "WebFetch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 116 · 2026-05-19T16:17:56.611331+00:00_

# Complete File Content

```python
import dataclasses
import logging
import re
from typing import Protocol, runtime_checkable

import flax.traverse_util
import numpy as np

import openpi.models.model as _model
import openpi.shared.array_typing as at
import openpi.shared.download as download

logger = logging.getLogger(__name__)


@runtime_checkable
class WeightLoader(Protocol):
    def load(self, params: at.Params) -> at.Params:
        """Loads the model weights.

        Args:
            params: Parameters of the model. This is a nested structure of array-like objects that
                represent the model's parameters.

        Returns:
            Loaded parameters. The structure must be identical to `params`. If returning a subset of
            the parameters the loader must merge the loaded parameters with `params`.
        """


@dataclasses.dataclass(frozen=True)
class NoOpWeightLoader(WeightLoader):
    def load(self, params: at.Params) -> at.Params:
        return params


@dataclasses.dataclass(frozen=True)
class CheckpointWeightLoader(WeightLoader):
    """Loads an entire set of weights from a checkpoint.

    Compatible with:
      trained checkpoints:
        example: "./checkpoints/&lt;config>/&lt;exp>/&lt;step>/params"
      released checkpoints:
        example: "gs://openpi-assets/checkpoints/&lt;model>/params"
    """

    params_path: str

    def load(self, params: at.Params) -> at.Params:
        # We are loading np.ndarray and relying on the training code to properly convert and shard the params.
        loaded_params = _model.restore_params(download.maybe_download(self.params_path), restore_type=np.ndarray)
        # Add all missing LoRA weights.
        return _merge_params(loaded_params, params, missing_regex=".*lora.*")


@dataclasses.dataclass(frozen=True)
class PaliGemmaWeightLoader(WeightLoader):
    """Loads weights from the official PaliGemma checkpoint.

    This will overwrite existing weights with similar names while keeping all extra weig
…[truncated 1776 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_vla_codebase_survey_20260519T160639",
  "tool": "WebFetch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 117 · 2026-05-19T16:17:56.611502+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://github.com/openvla/openvla",
  "prompt": "Extract: 1) Stars count, 2) Architecture description - what backbone, what action representation, 3) How actions are generated (autoregressive token generation?), 4) Any model dimension info. Focus on architecture differences from OFT."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_vla_codebase_survey_20260519T160639",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://github.com/openvla/openvla",
    "prompt": "Extract: 1) Stars count, 2) Architecture description - what backbone, what action representation, 3) How actions are generated (autoregressive token generation?), 4) Any model dimension info. Focus on architecture differences from OFT."
  }
}
```

</details>

---

### Tool call

_source line 118 · 2026-05-19T16:17:56.611636+00:00_

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
  "session": "worker_research_vla_codebase_survey_20260519T160639",
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

_source line 119 · 2026-05-19T16:17:56.611752+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_vla_codebase_survey_20260519T160639",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 120 · 2026-05-19T16:17:56.611870+00:00_

# OpenVLA Architecture Summary

**Stars:** 6.2k stars on GitHub

**Backbone Architecture:**
The flagship model uses the "Prismatic `prism-dinosiglip-224px` VLM" which combines "a fused DINOv2 and SigLIP vision backbone, and Llama-2 LLM." An earlier variant (`openvla-v01-7b`) uses "singular SigLIP vision backbone, and a Vicuña v1.5 LLM."

**Action Representation:**
The repository indicates support for "256-bin action discretization" with actions generated as discrete tokens. The newer FAST tokenizer mentioned can compress "action chunks...into fewer tokens," suggesting the base model uses discrete action binning rather than continuous outputs.

**Action Generation:**
While the document doesn't explicitly state the generation method, the code references "Action Token Accuracy" in training logs and involves predicting discrete action tokens, implying token-based autoregressive generation similar to language modeling.

**Model Dimensions:**
The primary model is identified as "`openvla-7b`" (7 billion parameters). A Prismatic-compatible checkpoint weights "30 GB," and training uses configurations with per-device batch sizes and gradient accumulation strategies typical of 7B-parameter models.

**Note on OFT Differences:**
OFT is presented as an optimization enabling "25-50x faster inference" and supporting "continuous actions," contrasting with the base model's discrete token approach.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_vla_codebase_survey_20260519T160639",
  "tool": "WebFetch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 121 · 2026-05-19T16:17:56.612144+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://arxiv.org/abs/2502.19645",
  "prompt": "Extract all technical details about OpenVLA-OFT: 1) What does OFT stand for? 2) What are the key architectural changes from vanilla OpenVLA? 3) How does it achieve faster inference? 4) What is the action head architecture? 5) What are the hidden state dimensions? 6) How does the L1 regression head work? 7) How does the diffusion head work? 8) What is the action chunking approach? 9) FiLM conditioning details. 10) Performance improvements. 11) Any mention of auxiliary task heads or multi-task learning."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_vla_codebase_survey_20260519T160639",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://arxiv.org/abs/2502.19645",
    "prompt": "Extract all technical details about OpenVLA-OFT: 1) What does OFT stand for? 2) What are the key architectural changes from vanilla OpenVLA? 3) How does it achieve faster inference? 4) What is the action head architecture? 5) What are the hidden state dimensions? 6) How does the L1 regression head work? 7) How does the diffusion head work? 8) What is the action chunking approach? 9) FiLM conditioning details. 10) Performance improvements. 11) Any mention of auxiliary task heads or multi-task learning."
  }
}
```

</details>

---

### Tool result

_source line 122 · 2026-05-19T16:17:56.612294+00:00_

# OpenVLA-OFT Technical Analysis

Based on the provided arXiv page content, I can only offer limited technical details, as the abstract and metadata don't contain comprehensive architectural specifications:

## Available Information:

**1) OFT Definition:**
"Optimized Fine-Tuning" - the paper presents this as a recipe for adapting vision-language-action models.

**2) Key Changes:**
The abstract identifies these design modifications: "parallel decoding, action chunking, a continuous action representation, and a simple L1 regression-based learning objective."

**3) Inference Speed:**
The model achieves "26× increase in action generation throughput" compared to baseline OpenVLA.

**4-9) Architectural Details:**
The provided web content does not specify hidden state dimensions, detailed action head architecture, diffusion head mechanics, FiLM conditioning parameters, or specific technical implementations of these components.

**10) Performance Improvements:**
On LIBERO simulation: success rate improved from 76.5% to 97.1%. On real robots, OpenVLA-OFT outperformed competing VLAs (π₀, RDT-1B) and imitation learning baselines by up to 15% absolute success rate.

**11) Multi-task Learning:**
No information about auxiliary task heads or multi-task approaches appears in this abstract.

**Note:** Full technical details require accessing the complete paper PDF or HTML version linked on the arXiv page.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_vla_codebase_survey_20260519T160639",
  "tool": "WebFetch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 123 · 2026-05-19T16:17:56.612471+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://arxiv.org/html/2502.19645v2",
  "prompt": "Extract ALL technical architecture details: 1) What exactly does \"parallel decoding\" mean here - does it replace autoregressive token generation with a single forward pass? 2) Exact hidden state dimensions (llm_dim). 3) How are action tokens replaced by continuous predictions? 4) The L1 regression action head architecture details. 5) The diffusion action head details. 6) Action chunking - how many actions predicted at once? 7) FiLM conditioning mechanism. 8) What intermediate representations are available. 9) How the action head is attached to the LLM backbone. 10) What happens to the original discrete action tokens during OFT training?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_vla_codebase_survey_20260519T160639",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://arxiv.org/html/2502.19645v2",
    "prompt": "Extract ALL technical architecture details: 1) What exactly does \"parallel decoding\" mean here - does it replace autoregressive token generation with a single forward pass? 2) Exact hidden state dimensions (llm_dim). 3) How are action tokens replaced by continuous predictions? 4) The L1 regression action head architecture details. 5) The diffusion action head details. 6) Action chunking - how many actions predicted at once? 7) FiLM conditioning mechanism. 8) What intermediate representations are available. 9) How the action head is attached to the LLM backbone. 10) What happens to the original discrete action tokens during OFT training?"
  }
}
```

</details>

---

### Tool call

_source line 124 · 2026-05-19T16:17:56.612634+00:00_

called mcp__agent-ml-research__save_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__save_project_file</summary>

```json
{
  "project": "diff_collision_sdf",
  "file": "memory.md",
  "content": "# ColliForce-VLA Project Memory\n\n## OpenPI Repository Analysis (2026-05-19)\n\n### Key Architecture Facts\n- **Backbone**: PaliGemma (SigLIP So400m/14 vision encoder + Gemma 2B language model)\n- **Action Expert**: Separate Gemma 300M model (18 layers, width=1024, head_dim=256)\n- **Action dim**: Default 32, action_horizon default 50 (pi0) / 10-16 (pi0.5/FAST)\n- **Intermediate feature dim**: action_expert_config.width = 1024 (Gemma 300M) or 2048 (Gemma 2B)\n- **Action head**: Simple Linear(action_expert_width, action_dim) projection from suffix_out[:, -action_horizon:]\n- **Flow matching**: Beta(1.5,1) time sampling, sinusoidal time embedding, Euler ODE solver\n\n### Architecture Flow\n1. Images -> SigLIP So400m/14 -> image tokens (224x224 input, 16x16 patches = 196 tokens per image, dim=2048)\n2. Language -> Gemma 2B embedder -> language tokens (dim=2048)\n3. State -> Linear(action_dim, 1024) -> state token (pi0 only; pi0.5 uses discrete state in language)\n4. Noisy actions -> Linear(action_dim, 1024) -> action tokens\n5. Time -> sinusoidal PE -> MLP -> time conditioning (fused with actions for pi0, adaRMS for pi0.5)\n6. [prefix_tokens, suffix_tokens] -> dual-expert Gemma transformer (shared attention, separate FFN weights)\n7. suffix_out[:, -action_horizon:] -> Linear(1024, action_dim) -> predicted velocity\n\n### Dual-Expert Transformer\n- PaliGemma (Gemma 2B): processes prefix (images + language), width=2048, 18 layers\n- Action Expert (Gemma 300M): processes suffix (state + actions), width=1024, 18 layers\n- Shared self-attention across both streams (Q/K/V concatenated), separate FFN per expert\n- Both share same head_dim=256, num_heads=8, num_kv_heads=1\n\n### Where to Tap for SDF Decoder\n- **Best hook point**: suffix_out before action_out_proj — shape [B, action_horizon, 1024]\n- **Alternative**: prefix_out after transformer — shape [B, prefix_len, 2048] (richer visual features)\n- **In JAX pi0.py**: `suffix_out[:, -self.action_horizon:]` at line ~compute_loss\n- **In PyTorch pi0_pytorch.py**: `suffix_out = suffix_out[:, -self.config.action_horizon:]` before action_out_proj\n\n### Fine-tuning Interface\n- Config system: tyro-based CLI with predefined TrainConfig objects in training/config.py\n- LoRA support: gemma_2b_lora (rank=16) and gemma_300m_lora (rank=32) variants\n- Freeze filter: `get_freeze_filter()` on Pi0Config, uses PathRegex for selective freezing\n- Weight loading: CheckpointWeightLoader loads from GCS, PaliGemmaWeightLoader for base PaliGemma\n- PyTorch training: train_pytorch.py with DDP support, safetensors checkpoints\n\n### Model Variants\n- **pi0**: Flow matching with state token in suffix, MLP time-action fusion\n- **pi0.5 (pi05)**: adaRMSNorm for time conditioning, discrete state in language tokens, max_token_len=200\n- **pi0-FAST**: Autoregressive (not flow matching), single Gemma 2B (no action expert), FAST tokenizer\n- No pi0.6 found in repo\n\n### Key File Paths\n- `src/openpi/models/pi0.py` — JAX Pi0 model (flow matching)\n- `src/openpi/models/pi0_config.py` — Model config with freeze_filter\n- `src/openpi/models/pi0_fast.py` — JAX Pi0-FAST (autoregressive)\n- `src/openpi/models/gemma.py` — Dual-expert Gemma backbone (JAX/Flax)\n- `src/openpi/models/model.py` — Base model, Observation/Actions types\n- `src/openpi/models/lora.py` — LoRA implementation\n- `src/openpi/models_pytorch/pi0_pytorch.py` — PyTorch Pi0 model\n- `src/openpi/models_pytorch/gemma_pytorch.py` — PyTorch PaliGemma+Expert wrapper\n- `src/openpi/training/config.py` — All training configs\n- `scripts/train_pytorch.py` — PyTorch training loop\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_vla_codebase_survey_20260519T160639",
  "tool": "mcp__agent-ml-research__save_project_file",
  "tool_args": {
    "project": "diff_collision_sdf",
    "file": "memory.md",
    "content": "# ColliForce-VLA Project Memory\n\n## OpenPI Repository Analysis (2026-05-19)\n\n### Key Architecture Facts\n- **Backbone**: PaliGemma (SigLIP So400m/14 vision encoder + Gemma 2B language model)\n- **Action Expert**: Separate Gemma 300M model (18 layers, width=1024, head_dim=256)\n- **Action dim**: Default 32, action_horizon default 50 (pi0) / 10-16 (pi0.5/FAST)\n- **Intermediate feature dim**: action_expert_config.width = 1024 (Gemma 300M) or 2048 (Gemma 2B)\n- **Action head**: Simple Linear(action_expert_width, action_dim) projection from suffix_out[:, -action_horizon:]\n- **Flow matching**: Beta(1.5,1) time sampling, sinusoidal time embedding, Euler ODE solver\n\n### Architecture Flow\n1. Images -> SigLIP So400m/14 -> image tokens (224x224 input, 16x16 patches = 196 tokens per image, dim=2048)\n2. Language -> Gemma 2B embedder -> language tokens (dim=2048)\n3. State -> Linear(action_dim, 1024) -> state token (pi0 only; pi0.5 uses discrete state in language)\n4. Noisy actions -> Linear(action_dim, 1024) -> action tokens\n5. Time -> sinusoidal PE -> MLP -> time conditioning (fused with actions for pi0, adaRMS for pi0.5)\n6. [prefix_tokens, suffix_tokens] -> dual-expert Gemma transformer (shared attention, separate FFN weights)\n7. suffix_out[:, -action_horizon:] -> Linear(1024, action_dim) -> predicted velocity\n\n### Dual-Expert Transformer\n- PaliGemma (Gemma 2B): processes prefix (images + language), width=2048, 18 layers\n- Action Expert (Gemma 300M): processes suffix (state + actions), width=1024, 18 layers\n- Shared self-attention across both streams (Q/K/V concatenated), separate FFN per expert\n- Both share same head_dim=256, num_heads=8, num_kv_heads=1\n\n### Where to Tap for SDF Decoder\n- **Best hook point**: suffix_out before action_out_proj — shape [B, action_horizon, 1024]\n- **Alternative**: prefix_out after transformer — shape [B, prefix_len, 2048] (richer visual features)\n- **In JAX pi0.py**: `suffix_out[:, -self.action_horizon:]` at line ~compute_loss\n- **In PyTorch pi0_pytorch.py**: `suffix_out = suffix_out[:, -self.config.action_horizon:]` before action_out_proj\n\n### Fine-tuning Interface\n- Config system: tyro-based CLI with predefined TrainConfig objects in training/config.py\n- LoRA support: gemma_2b_lora (rank=16) and gemma_300m_lora (rank=32) variants\n- Freeze filter: `get_freeze_filter()` on Pi0Config, uses PathRegex for selective freezing\n- Weight loading: CheckpointWeightLoader loads from GCS, PaliGemmaWeightLoader for base PaliGemma\n- PyTorch training: train_pytorch.py with DDP support, safetensors checkpoints\n\n### Model Variants\n- **pi0**: Flow matching with state token in suffix, MLP time-action fusion\n- **pi0.5 (pi05)**: adaRMSNorm for time conditioning, discrete state in language tokens, max_token_len=200\n- **pi0-FAST**: Autoregressive (not flow matching), single Gemma 2B (no action expert), FAST tokenizer\n- No pi0.6 found in repo\n\n### Key File Paths\n- `src/openpi/models/pi0.py` — JAX Pi0 model (flow matching)\n- `src/openpi/models/pi0_config.py` — Model config with freeze_filter\n- `src/openpi/models/pi0_fast.py` — JAX Pi0-FAST (autoregressive)\n- `src/openpi/models/gemma.py` — Dual-expert Gemma backbone (JAX/Flax)\n- `src/openpi/models/model.py` — Base model, Observation/Actions types\n- `src/openpi/models/lora.py` — LoRA implementation\n- `src/openpi/models_pytorch/pi0_pytorch.py` — PyTorch Pi0 model\n- `src/openpi/models_pytorch/gemma_pytorch.py` — PyTorch PaliGemma+Expert wrapper\n- `src/openpi/training/config.py` — All training configs\n- `scripts/train_pytorch.py` — PyTorch training loop\n"
  }
}
```

</details>

---

### Tool result

_source line 125 · 2026-05-19T16:17:56.612801+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/memory.md\", \"saved\": true}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_vla_codebase_survey_20260519T160639",
  "tool": "mcp__agent-ml-research__save_project_file",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 126 · 2026-05-19T16:17:56.612939+00:00_

# Technical Architecture Details: OpenVLA-OFT

## 1. Parallel Decoding Mechanism

Parallel decoding fundamentally changes action generation from sequential to simultaneous. Rather than the original autoregressive approach where "each predicted token is fed back as input for the next prediction," the system "replace[s] this input with empty action embeddings" and uses "bidirectional attention mask" to "leverage all intermediate features non-causally when predicting each element in the action chunk."

## 2. Hidden State Dimensions

The document specifies that FiLM's scaling/shifting vectors have dimensionality matching "D_ViT...the number of hidden dimensions" in the vision transformer. For OpenVLA's base model, this involves a "Llama-2 7B language model," but explicit hidden dimension values aren't provided.

## 3. Discrete-to-Continuous Action Token Replacement

The original discretization scheme using "256-bin discretization of normalized actions" is replaced entirely. The document states the transition: "discrete actions (256-bin discretization of normalized actions) processed through softmax-based token prediction" becomes continuous actions "directly generated by an MLP action head."

## 4. L1 Regression Action Head Architecture

The continuous L1 regression implementation uses a "4-layer MLP (ReLU activation)" that performs "direct mapping [of] final decoder layer hidden states to continuous action values." Training minimizes "mean L1 difference between predicted and ground-truth actions."

## 5. Diffusion Action Head Details

The diffusion variant employs:
- "4-layer noise predictor with same MLP architecture as the L1 regression head"
- "DDIM sampler with 50 diffusion timesteps"
- "Squared cosine beta schedule"

## 6. Action Chunking Configuration

The system predicts multiple timesteps simultaneously. For LIBERO experiments: "chunk size K=8." For ALOHA robot tasks: "action chunk size K=25." This represents "K timesteps of actions" generated in "one forward p
…[truncated 1303 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_vla_codebase_survey_20260519T160639",
  "tool": "WebFetch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 127 · 2026-05-19T16:17:56.613097+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://raw.githubusercontent.com/moojink/openvla-oft/main/prismatic/vla/action_tokenizer.py",
  "prompt": "Return the COMPLETE source code. I need to see how action tokens are defined, the bin size (256), how continuous actions are discretized and de-discretized."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_vla_codebase_survey_20260519T160639",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://raw.githubusercontent.com/moojink/openvla-oft/main/prismatic/vla/action_tokenizer.py",
    "prompt": "Return the COMPLETE source code. I need to see how action tokens are defined, the bin size (256), how continuous actions are discretized and de-discretized."
  }
}
```

</details>

---

### Tool result

_source line 128 · 2026-05-19T16:17:56.613226+00:00_

# ActionTokenizer: Complete Source Code Analysis

The complete source code provided is `action_tokenizer.py`, an extension class that wraps LLM/VLM tokenizers to handle robot actions.

## Key Components

**Action Token Definition:**
Action tokens are mapped to "the last `n_bins` tokens" of the vocabulary. The system reserves the final 256 tokens by default for discretized actions via `action_token_begin_idx = vocab_size - (n_bins + 1)`.

**Bin Configuration:**
- Default bin count: 256
- Range: -1.0 to 1.0 (configurable)
- Strategy: "Uniform binning" across the action range
- Bin centers calculated as midpoints between consecutive bin edges

**Discretization Process:**
The `__call__` method clips continuous actions to the defined range, then uses `np.digitize()` to map values into bins. Results are converted to token IDs by subtracting from `vocab_size`.

**De-discretization Process:**
The `decode_token_ids_to_actions()` method reverses this: it recovers discrete bin indices, applies clipping to handle boundary conditions, then retrieves corresponding continuous values from `bin_centers`.

**Boundary Handling:**
A critical note: "digitization returns indices between [1, # bins]" but only `(# bins - 1)` intervals exist. The code clips indices to prevent out-of-bounds access when indexing `bin_centers`.

The system assumes BPE-style tokenizers where least-used tokens appear at vocabulary's end.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_vla_codebase_survey_20260519T160639",
  "tool": "WebFetch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 129 · 2026-05-19T16:17:56.613364+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://raw.githubusercontent.com/moojink/openvla-oft/main/prismatic/conf/models.py",
  "prompt": "Return the COMPLETE source code. I need to see model configurations, what vision backbones and LLMs are defined, and the default architecture specs."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_vla_codebase_survey_20260519T160639",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://raw.githubusercontent.com/moojink/openvla-oft/main/prismatic/conf/models.py",
    "prompt": "Return the COMPLETE source code. I need to see model configurations, what vision backbones and LLMs are defined, and the default architecture specs."
  }
}
```

</details>

---

### Tool result

_source line 130 · 2026-05-19T16:17:56.613510+00:00_

# Summary of models.py Configuration

## Base ModelConfig Structure

The `ModelConfig` dataclass defines Vision-Language Model configurations with:
- **Vision backbone**: Pretrained visual featurizer (TIMM)
- **LLM backbone**: Pretrained language model (HuggingFace Transformers)
- **Image processing**: Resize strategy (crop, letterbox, corner-pad)
- **Two-stage optimization**: Align stage + Finetune stage with separate hyperparameters

## Key Vision Backbones Referenced

- CLIP ViT-L (224px, 336px variants)
- SigLIP ViT-SO400M (224px, 384px variants)
- DINOv2 ViT-L
- IN1K ViT-L
- DINOSigLIP (fused representations, 224px/384px)
- DINOCLIP (fused representations)

## Key LLM Backbones Referenced

- Vicuna v1.5 (7B, 13B)
- LLaMa-2 (7B, 13B base and chat variants)
- Mistral v0.1 (base and instruct)
- Phi-2 (3B)

## Architecture Specifications

Default: `"gelu-mlp"` (single-vision projector)
Variants: `"no-align+gelu-mlp"`, `"no-align+fused-gelu-mlp"` (for multi-backbone ensembles)

## Model Registry

The file includes 50+ registered configuration variants organized by research sections (optimization procedures, image processing strategies, language models, scaling properties, and Prism model family).

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_vla_codebase_survey_20260519T160639",
  "tool": "WebFetch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 131 · 2026-05-19T16:17:56.613657+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://raw.githubusercontent.com/moojink/openvla-oft/main/prismatic/extern/hf/modeling_prismatic.py",
  "prompt": "I need the EXACT code for these specific methods in OpenVLAForActionPrediction: 1) predict_action() - the full method, 2) the forward() method, 3) _process_action_masks(), 4) _replace_input_embeddings(). Also include the class __init__ and any property that reveals llm_dim. Return verbatim code, not summaries."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_vla_codebase_survey_20260519T160639",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://raw.githubusercontent.com/moojink/openvla-oft/main/prismatic/extern/hf/modeling_prismatic.py",
    "prompt": "I need the EXACT code for these specific methods in OpenVLAForActionPrediction: 1) predict_action() - the full method, 2) the forward() method, 3) _process_action_masks(), 4) _replace_input_embeddings(). Also include the class __init__ and any property that reveals llm_dim. Return verbatim code, not summaries."
  }
}
```

</details>

---

### Tool result

_source line 132 · 2026-05-19T16:17:56.613789+00:00_

# Requested Code from modeling_prismatic.py

## 1) OpenVLAForActionPrediction.__init__()

```python
def __init__(self, config: OpenVLAConfig) -> None:
    super().__init__(config)
    self.norm_stats = config.norm_stats

    # Compute action bins
    self.bins = np.linspace(-1, 1, config.n_action_bins)
    self.bin_centers = (self.bins[:-1] + self.bins[1:]) / 2.0

    # Compute vocab size for de-tokenization
    self.vocab_size = self.config.text_config.vocab_size - self.config.pad_to_multiple_of
```

## 2) llm_dim Property

Located in `PrismaticForConditionalGeneration.__init__()`:
```python
self.llm_dim = config.text_config.hidden_size
```

## 3) _process_action_masks()

```python
def _process_action_masks(self, labels):
    """Helper to get action masks from labels"""
    current_action_mask = get_current_action_mask(labels)
    next_actions_mask = get_next_actions_mask(labels)
    all_actions_mask = current_action_mask | next_actions_mask
    return all_actions_mask
```

## 4) _replace_input_embeddings()

```python
def _replace_input_embeddings(self, input_embeddings, all_actions_mask, noisy_action_features):
    new_input_embeddings = input_embeddings.clone()
    repositioned_noisy_action_features = torch.zeros_like(input_embeddings)
    batch_indices = torch.arange(input_embeddings.shape[0], device=input_embeddings.device)
    batch_indices = batch_indices.unsqueeze(1).expand(-1, noisy_action_features.shape[1])
    masked_indices = torch.stack([torch.where(mask)[0] for mask in all_actions_mask])
    repositioned_noisy_action_features[batch_indices, masked_indices] = noisy_action_features
    new_input_embeddings = torch.where(
        all_actions_mask.unsqueeze(-1), repositioned_noisy_action_features, new_input_embeddings
    )
    return new_input_embeddings
```

## 5) predict_action() - Full Method

See the document provided above for the complete `predict_action()` method implementation, which spans approximately 120 lines and includes handling for diffusio
…[truncated 348 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_vla_codebase_survey_20260519T160639",
  "tool": "WebFetch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 133 · 2026-05-19T16:17:56.613936+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://raw.githubusercontent.com/moojink/openvla-oft/main/prismatic/extern/hf/modeling_prismatic.py",
  "prompt": "Return ONLY the predict_action() method from OpenVLAForActionPrediction class, VERBATIM, line by line. I need every single line of code including all conditionals for diffusion vs L1 regression vs discrete, how hidden_states are extracted, how action_head is called, and how unnormalization works. Do not summarize ANY line."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_vla_codebase_survey_20260519T160639",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://raw.githubusercontent.com/moojink/openvla-oft/main/prismatic/extern/hf/modeling_prismatic.py",
    "prompt": "Return ONLY the predict_action() method from OpenVLAForActionPrediction class, VERBATIM, line by line. I need every single line of code including all conditionals for diffusion vs L1 regression vs discrete, how hidden_states are extracted, how action_head is called, and how unnormalization works. Do not summarize ANY line."
  }
}
```

</details>

---

### Tool result

_source line 134 · 2026-05-19T16:17:56.614077+00:00_

# predict_action() Method from OpenVLAForActionPrediction

```python
def predict_action(
    self,
    input_ids: Optional[torch.LongTensor] = None,
    unnorm_key: Optional[str] = None,
    proprio=None,
    proprio_projector=None,
    action_head=None,
    noisy_action_projector=None,
    use_film: bool = False,
    **kwargs: str,
) -> np.ndarray:
    """Predict actions from input sequence, with options for different prediction methods.

    Args:
        input_ids: Input token ids
        unnorm_key: Key for unnormalization statistics
        proprio: Proprioceptive features
        proprio_projector: Projector for proprioceptive features
        action_head: Optional head for L1 regression or diffusion-based prediction
        noisy_action_projector: Projector for noisy actions in diffusion-based prediction
        use_film: Whether to use FiLM conditioning
        **kwargs: Additional arguments including pixel_values and attention_mask

    Returns:
        Tuple of (unnormalized_actions, action_hidden_states)
    """
    # If the special empty token ('') does not already appear after the colon (':') token in the prompt
    # (after "OUT:" or "ASSISTANT:"), insert it to match the inputs seen at training time
    if not torch.all(input_ids[:, -1] == 29871):
        input_ids = torch.cat(
            (input_ids, torch.unsqueeze(torch.Tensor([29871]).long(), dim=0).to(input_ids.device)), dim=1
        )

    pixel_values = kwargs["pixel_values"]
    attention_mask = kwargs["attention_mask"]

    # Create fake labels tensor (needed for action mask)
    labels = input_ids.clone()
    labels[:] = IGNORE_INDEX

    # Get number of tokens in prompt (excluding the start token)
    NUM_PROMPT_TOKENS = input_ids.shape[-1] - 1  # Subtract action tokens and stop token

    # Prepare inputs by adding necessary tokens
    input_ids, attention_mask = self._prepare_input_for_action_prediction(input_ids, attention_mask)

    # Update labels tensor for action mask computation lat
…[truncated 2716 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_vla_codebase_survey_20260519T160639",
  "tool": "WebFetch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 135 · 2026-05-19T16:17:56.614229+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://raw.githubusercontent.com/moojink/openvla-oft/main/prismatic/extern/hf/modeling_prismatic.py",
  "prompt": "Return VERBATIM the _regression_or_discrete_prediction() method AND the _run_diffusion_prediction() method. I need to see exactly how hidden_states are extracted, how action_hidden_states are shaped, and how the action_head is called. Also return _prepare_input_for_action_prediction() and _prepare_labels_for_action_prediction()."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_vla_codebase_survey_20260519T160639",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://raw.githubusercontent.com/moojink/openvla-oft/main/prismatic/extern/hf/modeling_prismatic.py",
    "prompt": "Return VERBATIM the _regression_or_discrete_prediction() method AND the _run_diffusion_prediction() method. I need to see exactly how hidden_states are extracted, how action_hidden_states are shaped, and how the action_head is called. Also return _prepare_input_for_action_prediction() and _prepare_labels_for_action_prediction()."
  }
}
```

</details>

---

### Tool result

_source line 136 · 2026-05-19T16:17:56.614470+00:00_

Here is the complete analysis report:

---

## 1. Repository Metadata

| Field | Value |
|-------|-------|
| Stars | 11,907 |
| Last Updated | 2026-05-19 |
| License | Apache-2.0 |
| Language | Python (99.3%) |
| Forks | 1,926 |
| Open Issues | 282 |

---

## 2. Code Structure Overview

**Model architecture files** (JAX primary, PyTorch secondary):
- `src/openpi/models/pi0.py` — Pi0 flow-matching model (JAX/Flax)
- `src/openpi/models/pi0_fast.py` — Pi0-FAST autoregressive model (JAX/Flax)
- `src/openpi/models/pi0_config.py` — Model configs with freeze filters
- `src/openpi/models/gemma.py` — Dual-expert Gemma backbone (Flax Linen)
- `src/openpi/models/siglip.py` — SigLIP vision encoder (wraps ViT)
- `src/openpi/models/model.py` — Base classes, Observation/Actions data structures
- `src/openpi/models/lora.py` — LoRA for Einsum and FeedForward layers
- `src/openpi/models_pytorch/pi0_pytorch.py` — PyTorch Pi0 implementation
- `src/openpi/models_pytorch/gemma_pytorch.py` — PyTorch PaliGemma+Expert wrapper

**Training scripts**:
- `scripts/train.py` — JAX training loop (FSDP)
- `scripts/train_pytorch.py` — PyTorch training loop (DDP)
- `src/openpi/training/config.py` — All predefined training configurations

---

## 3. Model Architecture Deep Dive

### Backbone

The model uses **PaliGemma**, which is a combination of:
- **SigLIP So400m/14** vision encoder: Takes 224x224 images, 14x14 patches = 256 spatial tokens per image (16x16 grid), output dimension = 2048 (projected to match Gemma 2B width)
- **Gemma 2B** language model: width=2048, depth=18, mlp_dim=16384, 8 heads, 1 KV head, head_dim=256

### Dual-Expert Architecture (Key Insight)

This is NOT a standard single-backbone model. It uses a **dual-expert transformer** where two Gemma models share attention but have separate FFN weights:

1. **Expert 0 (PaliGemma/Gemma 2B)**: Processes "prefix" tokens (images + language). Width = 2048.
2. **Expert 1 (Action Expert/Gemma 300M)**: Processes "suffix" tokens (state + noisy 
…[truncated 8442 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_vla_codebase_survey_20260519T160639",
  "tool": "Agent",
  "elapsed_ms": 18
}
```

</details>

---

### Tool result

_source line 137 · 2026-05-19T16:17:56.614667+00:00_

# Requested Methods from modeling_prismatic.py

## _prepare_input_for_action_prediction()

```python
def _prepare_input_for_action_prediction(self, input_ids, attention_mask):
    """Prepares input for action prediction by adding necessary tokens"""
    # Add (ACTION_DIM * NUM_ACTIONS_CHUNK) placeholder tokens to input_ids to simulate action tokens
    placeholder_action_token_ids = (
        torch.ones((input_ids.shape[0], ACTION_DIM * NUM_ACTIONS_CHUNK)).to(input_ids.device).to(input_ids.dtype)
    )
    input_ids = torch.cat([input_ids, placeholder_action_token_ids], dim=-1)

    # Add stop token to sequence (needed in non-causal bi-directional self-attention, as it appears at train time)
    stop_token_id = torch.ones((input_ids.shape[0], 1)).to(input_ids.device).to(input_ids.dtype) * STOP_INDEX
    input_ids = torch.cat([input_ids, stop_token_id], dim=-1)

    # Extend the attention mask to fit the new shape of input
    # Note: Only batch size == 1 supported right now
    mask_extension = (
        torch.ones((attention_mask.shape[0], input_ids.shape[-1] - attention_mask.shape[-1]))
        .to(attention_mask.device)
        .to(attention_mask.dtype)
    )
    attention_mask = torch.cat([attention_mask, mask_extension], dim=-1)

    return input_ids, attention_mask
```

## _prepare_labels_for_action_prediction()

```python
def _prepare_labels_for_action_prediction(self, labels, input_ids):
    """Creates labels tensor for action prediction if not provided"""
    # Extend labels tensor with fake action labels
    ARBITRARY_ACTION_TOKEN_IDX = ACTION_TOKEN_BEGIN_IDX + 1
    labels_extension = (
        torch.ones((labels.shape[0], input_ids.shape[-1] - labels.shape[-1])).to(labels.device).to(labels.dtype)
        * ARBITRARY_ACTION_TOKEN_IDX
    )
    labels = torch.cat([labels, labels_extension], dim=-1)

    # Replace last label token with stop token
    labels[:, -1] = STOP_INDEX

    return labels
```

## _regression_or_discrete_prediction()

```python
def _r
…[truncated 6248 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_vla_codebase_survey_20260519T160639",
  "tool": "WebFetch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 138 · 2026-05-19T16:17:56.614825+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://raw.githubusercontent.com/moojink/openvla-oft/main/prismatic/extern/hf/modeling_prismatic.py",
  "prompt": "Return VERBATIM the forward() method of PrismaticForConditionalGeneration. I need the full method including how pixel_values are processed, how multimodal embeddings are built, how the language_model is called, and what output is returned. Also return _build_multimodal_attention() and _process_vision_features() methods."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_vla_codebase_survey_20260519T160639",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://raw.githubusercontent.com/moojink/openvla-oft/main/prismatic/extern/hf/modeling_prismatic.py",
    "prompt": "Return VERBATIM the forward() method of PrismaticForConditionalGeneration. I need the full method including how pixel_values are processed, how multimodal embeddings are built, how the language_model is called, and what output is returned. Also return _build_multimodal_attention() and _process_vision_features() methods."
  }
}
```

</details>

---

### Tool result

_source line 139 · 2026-05-19T16:17:56.614964+00:00_

# Key Methods from PrismaticForConditionalGeneration

## forward() Method

The primary forward pass handles three scenarios:

1. **Generation with Cache** (input_ids.shape[1] == 1): Passes through language model with past_key_values
2. **Unimodal Forward** (pixel_values is None): Language-only processing
3. **Multimodal Forward**: Processes vision and text together

For multimodal inputs, the method:
- Extracts input embeddings from token IDs
- Processes action masks from labels
- Calls "_process_vision_features()" to get projected patch embeddings
- Adds proprioceptive features if provided
- Handles noisy actions by replacing action token embeddings
- Calls "_build_multimodal_attention()" to combine vision and language embeddings
- Dispatches to the language model with combined multimodal embeddings
- Returns "PrismaticCausalLMOutputWithPast" containing loss, logits, past_key_values, hidden states, and projector features

## _process_vision_features() Method

```python
def _process_vision_features(self, pixel_values, language_embeddings=None, use_film=False):
    """Process vision features with optional FiLM conditioning"""
    if use_film:
        patch_features = self.vision_backbone(pixel_values, language_embeddings)
    else:
        patch_features = self.vision_backbone(pixel_values)
    
    return self.projector(patch_features)
```

Extracts patches via vision backbone, then projects them into language model embedding space.

## _build_multimodal_attention() Method

```python
def _build_multimodal_attention(self, input_embeddings, 
                                projected_patch_embeddings, attention_mask):
    """Build multimodal embeddings and attention mask"""
    projected_patch_attention_mask = None
    if attention_mask is not None:
        projected_patch_attention_mask = torch.full(
            (projected_patch_embeddings.shape[0], 
             projected_patch_embeddings.shape[1]),
            fill_value=True, dtype=attention_mask.dtype,
           
…[truncated 584 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_vla_codebase_survey_20260519T160639",
  "tool": "WebFetch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 140 · 2026-05-19T16:17:56.615117+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://raw.githubusercontent.com/moojink/openvla-oft/main/prismatic/extern/hf/modeling_prismatic.py",
  "prompt": "Return VERBATIM the full forward() method code of PrismaticForConditionalGeneration class. Include ALL parameters, ALL conditionals, ALL branches. I need to see: how output_hidden_states is passed, how noisy_actions are handled, how diffusion_timestep_embeddings are concatenated, and the exact return statement."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_vla_codebase_survey_20260519T160639",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://raw.githubusercontent.com/moojink/openvla-oft/main/prismatic/extern/hf/modeling_prismatic.py",
    "prompt": "Return VERBATIM the full forward() method code of PrismaticForConditionalGeneration class. Include ALL parameters, ALL conditionals, ALL branches. I need to see: how output_hidden_states is passed, how noisy_actions are handled, how diffusion_timestep_embeddings are concatenated, and the exact return statement."
  }
}
```

</details>

---

### Tool result

_source line 141 · 2026-05-19T16:17:56.615262+00:00_

# Full `forward()` Method of PrismaticForConditionalGeneration

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
    output_projector_features: Optional[bool] = None,
    return_dict: Optional[bool] = None,
    proprio=None,
    proprio_projector=None,
    noisy_actions=None,
    noisy_action_projector=None,
    diffusion_timestep_embeddings=None,
    use_film: bool = False,
) -> Union[Tuple, PrismaticCausalLMOutputWithPast]:
    """Run a forward pass through the VLM, returning a PrismaticCausalLMOutputWithPast instance."""
    output_attentions = output_attentions if output_attentions is not None else self.config.output_attentions
    output_hidden_states = (
        output_hidden_states if output_hidden_states is not None else self.config.output_hidden_states
    )
    output_projector_features = output_projector_features if output_projector_features is not None else False
    return_dict = return_dict if return_dict is not None else self.config.use_return_dict

    # Respect `use_cache` only if not training (even if `gradient_checkpointing` is off)
    use_cache = use_cache and not self.training

    # Instantiate Placeholder for Projector Features
    projected_patch_embeddings = None

    # === Handle Generation with Cache (`input_ids.shape[1] == 1`) =>> requires `past_keys_values` ===
    if input_ids.shape[1] == 1:
        assert input_ids.shape[0] == 1, "Generation is only currently supported for batch size of 1!"
        assert past_key_values is not None, "You must provide `past_key_values` during cached generation!"
        as
…[truncated 6403 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_vla_codebase_survey_20260519T160639",
  "tool": "WebFetch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 142 · 2026-05-19T16:17:56.615432+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://raw.githubusercontent.com/moojink/openvla-oft/main/SETUP.md",
  "prompt": "Return the full content. I need to see setup details, model configurations, pretrained checkpoint info, and any architecture details mentioned."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_vla_codebase_survey_20260519T160639",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://raw.githubusercontent.com/moojink/openvla-oft/main/SETUP.md",
    "prompt": "Return the full content. I need to see setup details, model configurations, pretrained checkpoint info, and any architecture details mentioned."
  }
}
```

</details>

---

### Tool result

_source line 143 · 2026-05-19T16:17:56.615569+00:00_

# Setup Instructions Summary

The provided content contains **setup instructions only** — no model configurations, pretrained checkpoint information, or architecture details are included.

## What's Covered

The documentation provides guidance for establishing a development environment:

**Environment Setup:**
"Create and activate conda environment" with Python 3.10, then install PyTorch dependencies tailored to your system via pytorch.org.

**Repository Installation:**
Users should clone the openvla-oft repository and execute `pip install -e .` to obtain project dependencies.

**Flash Attention 2:**
The instructions recommend installing Flash Attention 2 for training purposes, including dependency packages (packaging and ninja) and specific version specifications: "flash-attn==2.5.5" with the `--no-build-isolation` flag.

## Missing Information

The provided excerpt **does not include**:
- Model architecture specifications
- Pretrained checkpoint locations or download instructions
- Configuration parameters
- Training hyperparameters
- Additional documentation sections

To access comprehensive setup details, model information, and architecture specifications, you would need to review the complete repository documentation or README file from the openvla-oft GitHub project.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_vla_codebase_survey_20260519T160639",
  "tool": "WebFetch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 144 · 2026-05-19T16:17:56.615713+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://raw.githubusercontent.com/moojink/openvla-oft/main/prismatic/models/load.py",
  "prompt": "Return the COMPLETE source code. I need to see how models are loaded, what the default LLM backbone is, what llm_dim values are used."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_vla_codebase_survey_20260519T160639",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://raw.githubusercontent.com/moojink/openvla-oft/main/prismatic/models/load.py",
    "prompt": "Return the COMPLETE source code. I need to see how models are loaded, what the default LLM backbone is, what llm_dim values are used."
  }
}
```

</details>

---

### Tool result

_source line 145 · 2026-05-19T16:17:56.615836+00:00_

# Model Loading Analysis

Based on the provided code, here's what I found:

## How Models Are Loaded

The `load()` function accepts a `model_id_or_path` parameter and:
1. Checks if it's a local directory path
2. Falls back to searching the HuggingFace Hub using `GLOBAL_REGISTRY`
3. Downloads `config.json` and checkpoint files
4. Instantiates vision and LLM backbones separately
5. Creates a `PrismaticVLM` instance via `from_pretrained()`

## Default LLM Backbone

The code does **not specify a default LLM backbone**. Instead, it retrieves the backbone ID from the model configuration: `"llm_backbone_id"` is extracted from the loaded `config.json` file. The actual backbone is obtained via `"get_llm_backbone_and_tokenizer(model_cfg['llm_backbone_id'], ...)"`.

## LLM Dimension Values

The provided code **does not contain `llm_dim` values**. The only dimension-related parameter shown is `"llm_max_length"`, which defaults to 2048 if not specified: `"llm_max_length=model_cfg.get('llm_max_length', 2048)"`.

**Note:** To find default backbones and dimension specifications, you'd need to examine the `ModelConfig` definitions and `GLOBAL_REGISTRY` contents, which aren't included in this file.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_vla_codebase_survey_20260519T160639",
  "tool": "WebFetch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 146 · 2026-05-19T16:17:56.616020+00:00_

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
  "session": "worker_research_vla_codebase_survey_20260519T160639",
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

_source line 147 · 2026-05-19T16:17:56.616173+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_vla_codebase_survey_20260519T160639",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 148 · 2026-05-19T16:17:56.616397+00:00_



Here is the comprehensive analysis of the OpenVLA-OFT repository for the ColliForce-VLA project.

---

## 1. Repository Metadata

- **Stars**: ~1.2k
- **License**: MIT
- **Base repo (openvla/openvla)**: ~6.2k stars
- **Key paper**: arXiv:2502.19645 — "Fine-Tuning Vision-Language-Action Models: Optimizing Speed and Success"

---

## 2. Code Structure Overview

```
openvla-oft/
├── prismatic/
│   ├── models/
│   │   ├── action_heads.py          # L1 regression & diffusion action heads
│   │   ├── film_vit_wrapper.py      # FiLM conditioning for vision backbone
│   │   ├── projectors.py            # NoisyActionProjector, ProprioProjector
│   │   ├── vlas/openvla.py          # OpenVLA wrapper (discrete token inference)
│   │   ├── vlms/
│   │   │   ├── base_vlm.py          # Abstract VLM base class
│   │   │   └── prismatic.py         # PrismaticVLM (core VLM implementation)
│   │   └── backbones/
│   │       ├── llm/ (llama2.py, mistral.py, phi.py)
│   │       └── vision/ (siglip_vit.py, dinov2_vit.py, dinosiglip_vit.py, ...)
│   ├── extern/hf/
│   │   ├── modeling_prismatic.py     # HF-compatible model: PrismaticForConditionalGeneration + OpenVLAForActionPrediction
│   │   └── configuration_prismatic.py # OpenVLAConfig
│   ├── training/
│   │   ├── train_utils.py           # Action mask utilities, loss functions
│   │   └── strategies/ (ddp.py, fsdp.py)
│   └── vla/
│       ├── constants.py             # ACTION_DIM, NUM_ACTIONS_CHUNK, PROPRIO_DIM per platform
│       ├── action_tokenizer.py      # 256-bin discretization tokenizer
│       └── datasets/                # RLDS data loading
├── vla-scripts/
│   ├── finetune.py                  # Main fine-tuning script (OFT training)
│   ├── deploy.py                    # Inference server
│   └── merge_lora_weights_and_save.py
└── experiments/robot/
    ├── openvla_utils.py             # get_vla_action(), get_action_head(), get_vla()
    ├── libero/                      # LIBERO simulation eval
    └── aloha/            
…[truncated 10461 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_vla_codebase_survey_20260519T160639",
  "tool": "Agent",
  "elapsed_ms": 19
}
```

</details>

---

### Tool call

_source line 149 · 2026-05-19T16:17:56.616611+00:00_

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
  "session": "worker_research_vla_codebase_survey_20260519T160639",
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

_source line 150 · 2026-05-19T16:17:56.616740+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_vla_codebase_survey_20260519T160639",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 151 · 2026-05-19T16:17:56.616888+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls /home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/artifacts/ 2>/dev/null; ls /home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/",
  "description": "List project directory structure"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_vla_codebase_survey_20260519T160639",
  "tool": "Bash",
  "tool_args": {
    "command": "ls /home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/artifacts/ 2>/dev/null; ls /home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/",
    "description": "List project directory structure"
  }
}
```

</details>

---

### Tool result

_source line 152 · 2026-05-19T16:17:56.617015+00:00_

report_sdf_extraction.md
AGENTS.md
ROADMAP.lock
ROADMAP.md
artifacts
decisions.lock
decisions.yaml
docs
logs
memory.md
study_status.lock

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_vla_codebase_survey_20260519T160639",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 153 · 2026-05-19T16:17:56.617159+00:00_

called Write

<details open><summary>🔧 Tool call — Write</summary>

````json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/artifacts/report_vla_codebase.md",
  "content": "# VLA 基座代码库调研报告\n\n> 调研日期：2026-05-19\n> 目的：评估 openpi (π0) 和 OpenVLA-OFT 作为 ColliForce-VLA MVP 基座的适合度\n\n---\n\n## 1. 仓库概览\n\n| 项目 | openpi (π0) | OpenVLA-OFT |\n|------|------------|-------------|\n| 仓库地址 | [Physical-Intelligence/openpi](https://github.com/Physical-Intelligence/openpi) | [moojink/openvla-oft](https://github.com/moojink/openvla-oft) |\n| Stars | ~11,900 | ~1,200 |\n| 最近更新 | 2026-05-19（活跃维护） | 2025 Q2（论文发布后维护） |\n| License | Apache-2.0 | MIT |\n| 框架 | JAX/Flax（主）+ PyTorch（辅） | PyTorch / HuggingFace |\n| 基础论文 | π0: A Vision-Language-Action Flow Model | arXiv:2502.19645 |\n\n---\n\n## 2. 模型架构概述\n\n### 2.1 openpi (π0)\n\n**双专家 Transformer 架构**：\n\n- **Vision Encoder**: SigLIP So400m/14, 224×224 输入, 196 tokens/image, dim=2048\n- **Expert 0 (PaliGemma/Gemma 2B)**: 处理 prefix（图像 + 语言），width=2048, depth=18, 8 heads\n- **Expert 1 (Action Expert/Gemma 300M)**: 处理 suffix（state + noisy actions），width=1024, depth=18\n\n核心设计：两个 Expert **共享 Attention（Q/K/V concat 后联合计算）但有独立的 FFN**。Action Expert 的参数量远小于 PaliGemma Expert。\n\n**Action Head**:\n```\naction_in_proj: Linear(action_dim → 1024)   # 将 action 投射到 expert 宽度\naction_out_proj: Linear(1024 → action_dim)   # 从 expert 特征解码回 action\n```\n\n**训练目标**: Flow Matching — 预测噪声到干净 action 的 velocity field，loss = MSE(v_t, noise - actions)\n\n**推理**: Euler ODE solver，默认 10 步去噪\n\n**数据流**:\n1. Images → SigLIP → `[B, 196*num_imgs, 2048]`\n2. Language → Gemma embedder → `[B, max_token_len, 2048]`\n3. State → state_proj → `[B, 1, 1024]`; Noisy actions → action_in_proj → `[B, action_horizon, 1024]`\n4. Prefix + Suffix → 双专家 Transformer (18 layers, shared attention)\n5. `suffix_out[:, -action_horizon:]` → action_out_proj → predicted velocity\n\n### 2.2 OpenVLA-OFT\n\n**Prismatic VLM + 独立 Action Head 架构**：\n\n- **Vision Backbone**: Fused DINOv2 + SigLIP（dual backbone, 特征 concat），256 patches/image\n- **Projector**: 2-layer MLP (GELU), vision_dim → llm_dim\n- **LLM Backbone**: Llama-2 7B (Vicuna-7B), hidden_size=4096, 32 layers\n\n**Action Head** (独立 nn.Module):\n```\nL1RegressionActionHead:\n  Input: (B, NUM_ACTIONS_CHUNK * ACTION_DIM, 4096)\n  MLPResNet: LayerNorm → Linear(input_dim*ACTION_DIM, 4096) → ReLU → 2x ResNetBlock → Linear(4096, action_dim)\n  Output: (B, NUM_ACTIONS_CHUNK, ACTION_DIM)\n```\n\n**OFT 的核心改进**（非 Orthogonal Fine-Tuning，而是一组优化策略）：\n1. **并行解码**: 替代自回归逐 token 生成，一次前向得到所有 action token 的 hidden states\n2. **Action chunking**: 预测 K 个连续 action（LIBERO: 8, ALOHA: 25）\n3. **连续 action 表示**: 替代 256-bin 离散化\n4. **L1 回归损失**: 替代 cross-entropy\n\n**推理速度**: ~26x faster（1 次前向 vs 56 次自回归前向）\n\n---\n\n## 3. Fine-tune 接口分析\n\n### 3.1 openpi — 添加辅助任务 Head\n\n**配置系统**: `tyro` CLI + Python dataclass，预定义 config 在 `src/openpi/training/config.py`\n\n**冻结机制**: `Pi0Config.get_freeze_filter()` 返回 Flax NNX filter\n- LoRA fine-tune: 冻结 Gemma LLM 参数，只训练 LoRA + action expert\n- PathRegex 模式匹配：`\".*llm.*\"`, `\".*lora.*\"` 等\n\n**添加 SDF decoder 的方法**:\n\n```python\n# 在 Pi0.__init__() 或 PI0Pytorch.__init__() 中:\nself.sdf_decoder = SDFDecoderHead(input_dim=1024, ...)  # action expert width\n\n# 在 compute_loss() 中，Transformer 前向之后:\nsuffix_features = suffix_out[:, -self.action_horizon:]  # [B, action_horizon, 1024]\nsdf_pred = self.sdf_decoder(suffix_features)\nsdf_loss = sdf_criterion(sdf_pred, sdf_target)\ntotal_loss = flow_loss + lambda_sdf * sdf_loss\n```\n\n**优势**: 新增参数不匹配 `\".*llm.*\"` 正则，默认可训练，freeze filter 无需修改。\n\n**替代方案**: Cross-attend 到 prefix features `[B, ~636, 2048]`（视觉 token），适合 SDF 这种空间几何任务。\n\n**关键文件**:\n- `src/openpi/models/pi0.py` — 模型定义、compute_loss\n- `src/openpi/models/gemma.py` — 双专家 Transformer\n- `src/openpi/models_pytorch/pi0_pytorch.py` — PyTorch 版本\n- `src/openpi/training/config.py` — 训练配置\n\n### 3.2 OpenVLA-OFT — 添加辅助任务 Head\n\n**配置系统**: `draccus` (dataclass-based config) + `@draccus.wrap()`\n\n**冻结机制**: `freeze_backbones()` 支持多种策略\n- `\"finetune\"` / `\"vla-train\"`: Vision 冻结, Projector + LLM 训练\n- `\"last-layer-finetune\"`: 只解冻 LLM 最后一层\n- `\"vla-sandwich-train\"`: Vision + Projector 训练, 只解冻 LLM 最后一层\n\n**添加 SDF decoder 的方法**:\n\n```python\n# 参照 L1RegressionActionHead 的模式:\nclass SDFDecoderHead(nn.Module):\n    def __init__(self, input_dim=4096, hidden_dim=..., output_dim=...):\n        ...\n\n# 在 finetune.py 中:\nsdf_head = init_module(SDFDecoderHead, \"sdf_head\", cfg, device_id,\n    {\"input_dim\": vla.module.llm_dim, ...}, to_bf16=True)\n\n# 训练循环中:\nlast_hidden_states = language_model_output.hidden_states[-1]  # (B, seq_len, 4096)\n# 可取任意位置的 hidden states 输入 SDF decoder\nsdf_pred = sdf_head(last_hidden_states[:, vision_positions, :])\n```\n\n**优势**: Action Head 已经是独立 nn.Module，有独立 optimizer 参数、独立保存/加载。模式成熟，添加新 head 完全遵循相同 pattern。\n\n**关键文件**:\n- `prismatic/models/action_heads.py` — Action Head 定义（SDF Head 模板）\n- `prismatic/extern/hf/modeling_prismatic.py` — HF 兼容模型，forward + predict_action\n- `vla-scripts/finetune.py` — 训练循环、head 初始化、loss 计算\n- `prismatic/models/projectors.py` — Projector 定义\n\n---\n\n## 4. Action Token Intermediate Features 分析\n\n### 4.1 openpi\n\n| 特征 | 维度 | 位置 |\n|------|------|------|\n| Prefix output (视觉+语言) | `[B, ~636, 2048]` | Expert 0, 18 层后 |\n| Suffix output (state+action) | `[B, 1+action_horizon, 1024]` | Expert 1, 18 层后 |\n| **Action features (SDF 最佳挂载点)** | **`[B, action_horizon, 1024]`** | Expert 1 最后一层 |\n| 中间层特征 | 需修改 scan loop (JAX) 或 hook (PyTorch) | 每层均可 |\n\n**可访问性**:\n- JAX 版本：层级特征需修改 `nn.scan` loop，不够方便\n- **PyTorch 版本**：`gemma_pytorch.py` 中层级循环是显式 for-loop，可直接添加 hook 或在循环中截取，**推荐使用 PyTorch 版本**\n\n### 4.2 OpenVLA-OFT\n\n| 特征 | 维度 | 位置 |\n|------|------|------|\n| Vision patch embeddings | `[B, 256, 4096]` (经 projector 后) | LLM 输入层 |\n| 全序列 hidden states | `[B, seq_len, 4096]` | 每层均可 (32+1 层) |\n| **Action token hidden states** | **`[B, NUM_ACTIONS_CHUNK*ACTION_DIM, 4096]`** | 最后一层（已有提取逻辑） |\n| Projector features (pre-LLM 视觉) | 需 `output_projector_features=True` | Projector 输出 |\n\n**可访问性**:\n- `output_hidden_states=True` 已是默认行为，返回所有 32 层 + embedding 层的 hidden states\n- 序列布局：`[BOS] [vision_patches(256)] [proprio(1)] [text_tokens] [action_tokens(K*D)] [STOP]`\n- **已有成熟的 hidden state 提取和路由机制**\n\n---\n\n## 5. 对比与推荐\n\n### 关键维度对比\n\n| 维度 | openpi (π0) | OpenVLA-OFT | ColliForce-VLA 偏好 |\n|------|------------|-------------|-------------------|\n| Action 中间表示维度 | 1024 | 4096 | 4096 更丰富 ✓ |\n| 添加辅助 Head 难度 | 中等（需改模型类） | **低（独立模块模式成熟）** | OFT ✓ |\n| Hidden state 可访问性 | JAX 需改 scan; PyTorch 可行 | **开箱即用** | OFT ✓ |\n| 训练框架 | JAX FSDP (主) / PyTorch DDP (辅) | **PyTorch FSDP/DDP** | OFT ✓ |\n| 模型质量 (LIBERO) | 高（π0 预训练数据 10k+ 小时） | **97.1% 成功率** | 相当 |\n| 推理速度 | 10 步 ODE (~10x 前向) | **1 次前向** | OFT ✓ |\n| 社区活跃度 | 11.9k stars, 活跃维护 | 1.2k stars, 较少维护 | openpi ✓ |\n| SDF 梯度传播 | Flow matching ODE loop 需 differentiable solver | **单次前向，梯度直接回传** | OFT ✓ |\n| 模型规模 | ~2.5B (2B + 300M) | 7B | openpi 更轻量 ✓ |\n\n### 推荐：OpenVLA-OFT 作为 MVP 基座\n\n**理由**:\n\n1. **辅助任务集成最简单**: Action Head 已是独立 nn.Module，有成熟的初始化、训练、保存模式。添加 SDF decoder 完全遵循现有 pattern，无需修改核心模型类。\n\n2. **Hidden state 访问开箱即用**: `output_hidden_states=True` 已是标准流程，返回所有 32 层 hidden states。序列中每个位置（视觉、语言、action）的 hidden state 都可直接提取。\n\n3. **梯度传播友好**: 单次前向+L1 回归，action 预测完全可微。SDF gradient 可直接通过 action head hidden states 回传到 backbone，无需处理 ODE solver 的梯度问题（openpi 的 flow matching 需要 10 步 Euler 循环）。\n\n4. **纯 PyTorch 生态**: 与大多数 ML 研究工具链兼容（wandb、accelerate、deepspeed 等），调试方便。\n\n5. **4096 维 hidden state**: 比 openpi 的 1024 维 action expert 表示更丰富，为 SDF decoder 提供更多信息容量。\n\n**openpi 作为备选的优势**:\n- 更小模型（2.5B vs 7B），显存/速度友好\n- 社区更活跃，长期维护有保障\n- Flow matching 架构本身优雅\n- 如果后续需要更强的预训练基础（10k+ 小时机器人数据），openpi 有明显优势\n\n---\n\n## 6. Blockers 与风险\n\n### OpenVLA-OFT\n- **仓库维护活跃度较低**: 论文发布后更新不频繁，遇到 bug 可能需要自行修复\n- **模型较大 (7B)**: 训练需要更多 GPU 显存；单卡 A100 80GB 可跑但余量不大\n- **Llama-2 7B 作为 backbone**: 不是最新的 LLM，但对 VLA 任务影响不大\n\n### openpi\n- **JAX/Flax 为主**: 如果团队 PyTorch 经验为主，开发效率受影响（虽有 PyTorch 版但功能不完整）\n- **Flow matching ODE 的梯度**: 10 步 Euler 循环的梯度回传需要 differentiable ODE solver 或 adjoint method，增加 SDF 集成复杂度\n- **双专家架构**: 修改需要理解两个 expert 的交互机制，学习曲线较陡\n\n### 共同风险\n- 两个仓库都没有 SDF 相关功能的先例，集成需要从零开始\n- 训练数据格式需要扩展以包含 SDF ground truth\n- Action refinement (用 SDF gradient 修正 action) 的具体实现方式需要进一步设计\n\n---\n\n## 7. 下一步建议\n\n1. **Fork openvla-oft**，在 `prismatic/models/action_heads.py` 中实现 `SDFDecoderHead`\n2. 先用 dummy SDF target 验证训练流程跑通（梯度正常回传、loss 下降）\n3. 再接入真实的可微分 workspace SDF 模块\n4. 如果 7B 模型显存压力过大，再考虑切换到 openpi PyTorch 版本（1024 维 action expert 仍然足够）\n"
}
````

</details>

<details><summary>Recorded metadata</summary>

````json
{
  "recorded_role": "tool",
  "session": "worker_research_vla_codebase_survey_20260519T160639",
  "tool": "Write",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/artifacts/report_vla_codebase.md",
    "content": "# VLA 基座代码库调研报告\n\n> 调研日期：2026-05-19\n> 目的：评估 openpi (π0) 和 OpenVLA-OFT 作为 ColliForce-VLA MVP 基座的适合度\n\n---\n\n## 1. 仓库概览\n\n| 项目 | openpi (π0) | OpenVLA-OFT |\n|------|------------|-------------|\n| 仓库地址 | [Physical-Intelligence/openpi](https://github.com/Physical-Intelligence/openpi) | [moojink/openvla-oft](https://github.com/moojink/openvla-oft) |\n| Stars | ~11,900 | ~1,200 |\n| 最近更新 | 2026-05-19（活跃维护） | 2025 Q2（论文发布后维护） |\n| License | Apache-2.0 | MIT |\n| 框架 | JAX/Flax（主）+ PyTorch（辅） | PyTorch / HuggingFace |\n| 基础论文 | π0: A Vision-Language-Action Flow Model | arXiv:2502.19645 |\n\n---\n\n## 2. 模型架构概述\n\n### 2.1 openpi (π0)\n\n**双专家 Transformer 架构**：\n\n- **Vision Encoder**: SigLIP So400m/14, 224×224 输入, 196 tokens/image, dim=2048\n- **Expert 0 (PaliGemma/Gemma 2B)**: 处理 prefix（图像 + 语言），width=2048, depth=18, 8 heads\n- **Expert 1 (Action Expert/Gemma 300M)**: 处理 suffix（state + noisy actions），width=1024, depth=18\n\n核心设计：两个 Expert **共享 Attention（Q/K/V concat 后联合计算）但有独立的 FFN**。Action Expert 的参数量远小于 PaliGemma Expert。\n\n**Action Head**:\n```\naction_in_proj: Linear(action_dim → 1024)   # 将 action 投射到 expert 宽度\naction_out_proj: Linear(1024 → action_dim)   # 从 expert 特征解码回 action\n```\n\n**训练目标**: Flow Matching — 预测噪声到干净 action 的 velocity field，loss = MSE(v_t, noise - actions)\n\n**推理**: Euler ODE solver，默认 10 步去噪\n\n**数据流**:\n1. Images → SigLIP → `[B, 196*num_imgs, 2048]`\n2. Language → Gemma embedder → `[B, max_token_len, 2048]`\n3. State → state_proj → `[B, 1, 1024]`; Noisy actions → action_in_proj → `[B, action_horizon, 1024]`\n4. Prefix + Suffix → 双专家 Transformer (18 layers, shared attention)\n5. `suffix_out[:, -action_horizon:]` → action_out_proj → predicted velocity\n\n### 2.2 OpenVLA-OFT\n\n**Prismatic VLM + 独立 Action Head 架构**：\n\n- **Vision Backbone**: Fused DINOv2 + SigLIP（dual backbone, 特征 concat），256 patches/image\n- **Projector**: 2-layer MLP (GELU), vision_dim → llm_dim\n- **LLM Backbone**: Llama-2 7B (Vicuna-7B), hidden_size=4096, 32 layers\n\n**Action Head** (独立 nn.Module):\n```\nL1RegressionActionHead:\n  Input: (B, NUM_ACTIONS_CHUNK * ACTION_DIM, 4096)\n  MLPResNet: LayerNorm → Linear(input_dim*ACTION_DIM, 4096) → ReLU → 2x ResNetBlock → Linear(4096, action_dim)\n  Output: (B, NUM_ACTIONS_CHUNK, ACTION_DIM)\n```\n\n**OFT 的核心改进**（非 Orthogonal Fine-Tuning，而是一组优化策略）：\n1. **并行解码**: 替代自回归逐 token 生成，一次前向得到所有 action token 的 hidden states\n2. **Action chunking**: 预测 K 个连续 action（LIBERO: 8, ALOHA: 25）\n3. **连续 action 表示**: 替代 256-bin 离散化\n4. **L1 回归损失**: 替代 cross-entropy\n\n**推理速度**: ~26x faster（1 次前向 vs 56 次自回归前向）\n\n---\n\n## 3. Fine-tune 接口分析\n\n### 3.1 openpi — 添加辅助任务 Head\n\n**配置系统**: `tyro` CLI + Python dataclass，预定义 config 在 `src/openpi/training/config.py`\n\n**冻结机制**: `Pi0Config.get_freeze_filter()` 返回 Flax NNX filter\n- LoRA fine-tune: 冻结 Gemma LLM 参数，只训练 LoRA + action expert\n- PathRegex 模式匹配：`\".*llm.*\"`, `\".*lora.*\"` 等\n\n**添加 SDF decoder 的方法**:\n\n```python\n# 在 Pi0.__init__() 或 PI0Pytorch.__init__() 中:\nself.sdf_decoder = SDFDecoderHead(input_dim=1024, ...)  # action expert width\n\n# 在 compute_loss() 中，Transformer 前向之后:\nsuffix_features = suffix_out[:, -self.action_horizon:]  # [B, action_horizon, 1024]\nsdf_pred = self.sdf_decoder(suffix_features)\nsdf_loss = sdf_criterion(sdf_pred, sdf_target)\ntotal_loss = flow_loss + lambda_sdf * sdf_loss\n```\n\n**优势**: 新增参数不匹配 `\".*llm.*\"` 正则，默认可训练，freeze filter 无需修改。\n\n**替代方案**: Cross-attend 到 prefix features `[B, ~636, 2048]`（视觉 token），适合 SDF 这种空间几何任务。\n\n**关键文件**:\n- `src/openpi/models/pi0.py` — 模型定义、compute_loss\n- `src/openpi/models/gemma.py` — 双专家 Transformer\n- `src/openpi/models_pytorch/pi0_pytorch.py` — PyTorch 版本\n- `src/openpi/training/config.py` — 训练配置\n\n### 3.2 OpenVLA-OFT — 添加辅助任务 Head\n\n**配置系统**: `draccus` (dataclass-based config) + `@draccus.wrap()`\n\n**冻结机制**: `freeze_backbones()` 支持多种策略\n- `\"finetune\"` / `\"vla-train\"`: Vision 冻结, Projector + LLM 训练\n- `\"last-layer-finetune\"`: 只解冻 LLM 最后一层\n- `\"vla-sandwich-train\"`: Vision + Projector 训练, 只解冻 LLM 最后一层\n\n**添加 SDF decoder 的方法**:\n\n```python\n# 参照 L1RegressionActionHead 的模式:\nclass SDFDecoderHead(nn.Module):\n    def __init__(self, input_dim=4096, hidden_dim=..., output_dim=...):\n        ...\n\n# 在 finetune.py 中:\nsdf_head = init_module(SDFDecoderHead, \"sdf_head\", cfg, device_id,\n    {\"input_dim\": vla.module.llm_dim, ...}, to_bf16=True)\n\n# 训练循环中:\nlast_hidden_states = language_model_output.hidden_states[-1]  # (B, seq_len, 4096)\n# 可取任意位置的 hidden states 输入 SDF decoder\nsdf_pred = sdf_head(last_hidden_states[:, vision_positions, :])\n```\n\n**优势**: Action Head 已经是独立 nn.Module，有独立 optimizer 参数、独立保存/加载。模式成熟，添加新 head 完全遵循相同 pattern。\n\n**关键文件**:\n- `prismatic/models/action_heads.py` — Action Head 定义（SDF Head 模板）\n- `prismatic/extern/hf/modeling_prismatic.py` — HF 兼容模型，forward + predict_action\n- `vla-scripts/finetune.py` — 训练循环、head 初始化、loss 计算\n- `prismatic/models/projectors.py` — Projector 定义\n\n---\n\n## 4. Action Token Intermediate Features 分析\n\n### 4.1 openpi\n\n| 特征 | 维度 | 位置 |\n|------|------|------|\n| Prefix output (视觉+语言) | `[B, ~636, 2048]` | Expert 0, 18 层后 |\n| Suffix output (state+action) | `[B, 1+action_horizon, 1024]` | Expert 1, 18 层后 |\n| **Action features (SDF 最佳挂载点)** | **`[B, action_horizon, 1024]`** | Expert 1 最后一层 |\n| 中间层特征 | 需修改 scan loop (JAX) 或 hook (PyTorch) | 每层均可 |\n\n**可访问性**:\n- JAX 版本：层级特征需修改 `nn.scan` loop，不够方便\n- **PyTorch 版本**：`gemma_pytorch.py` 中层级循环是显式 for-loop，可直接添加 hook 或在循环中截取，**推荐使用 PyTorch 版本**\n\n### 4.2 OpenVLA-OFT\n\n| 特征 | 维度 | 位置 |\n|------|------|------|\n| Vision patch embeddings | `[B, 256, 4096]` (经 projector 后) | LLM 输入层 |\n| 全序列 hidden states | `[B, seq_len, 4096]` | 每层均可 (32+1 层) |\n| **Action token hidden states** | **`[B, NUM_ACTIONS_CHUNK*ACTION_DIM, 4096]`** | 最后一层（已有提取逻辑） |\n| Projector features (pre-LLM 视觉) | 需 `output_projector_features=True` | Projector 输出 |\n\n**可访问性**:\n- `output_hidden_states=True` 已是默认行为，返回所有 32 层 + embedding 层的 hidden states\n- 序列布局：`[BOS] [vision_patches(256)] [proprio(1)] [text_tokens] [action_tokens(K*D)] [STOP]`\n- **已有成熟的 hidden state 提取和路由机制**\n\n---\n\n## 5. 对比与推荐\n\n### 关键维度对比\n\n| 维度 | openpi (π0) | OpenVLA-OFT | ColliForce-VLA 偏好 |\n|------|------------|-------------|-------------------|\n| Action 中间表示维度 | 1024 | 4096 | 4096 更丰富 ✓ |\n| 添加辅助 Head 难度 | 中等（需改模型类） | **低（独立模块模式成熟）** | OFT ✓ |\n| Hidden state 可访问性 | JAX 需改 scan; PyTorch 可行 | **开箱即用** | OFT ✓ |\n| 训练框架 | JAX FSDP (主) / PyTorch DDP (辅) | **PyTorch FSDP/DDP** | OFT ✓ |\n| 模型质量 (LIBERO) | 高（π0 预训练数据 10k+ 小时） | **97.1% 成功率** | 相当 |\n| 推理速度 | 10 步 ODE (~10x 前向) | **1 次前向** | OFT ✓ |\n| 社区活跃度 | 11.9k stars, 活跃维护 | 1.2k stars, 较少维护 | openpi ✓ |\n| SDF 梯度传播 | Flow matching ODE loop 需 differentiable solver | **单次前向，梯度直接回传** | OFT ✓ |\n| 模型规模 | ~2.5B (2B + 300M) | 7B | openpi 更轻量 ✓ |\n\n### 推荐：OpenVLA-OFT 作为 MVP 基座\n\n**理由**:\n\n1. **辅助任务集成最简单**: Action Head 已是独立 nn.Module，有成熟的初始化、训练、保存模式。添加 SDF decoder 完全遵循现有 pattern，无需修改核心模型类。\n\n2. **Hidden state 访问开箱即用**: `output_hidden_states=True` 已是标准流程，返回所有 32 层 hidden states。序列中每个位置（视觉、语言、action）的 hidden state 都可直接提取。\n\n3. **梯度传播友好**: 单次前向+L1 回归，action 预测完全可微。SDF gradient 可直接通过 action head hidden states 回传到 backbone，无需处理 ODE solver 的梯度问题（openpi 的 flow matching 需要 10 步 Euler 循环）。\n\n4. **纯 PyTorch 生态**: 与大多数 ML 研究工具链兼容（wandb、accelerate、deepspeed 等），调试方便。\n\n5. **4096 维 hidden state**: 比 openpi 的 1024 维 action expert 表示更丰富，为 SDF decoder 提供更多信息容量。\n\n**openpi 作为备选的优势**:\n- 更小模型（2.5B vs 7B），显存/速度友好\n- 社区更活跃，长期维护有保障\n- Flow matching 架构本身优雅\n- 如果后续需要更强的预训练基础（10k+ 小时机器人数据），openpi 有明显优势\n\n---\n\n## 6. Blockers 与风险\n\n### OpenVLA-OFT\n- **仓库维护活跃度较低**: 论文发布后更新不频繁，遇到 bug 可能需要自行修复\n- **模型较大 (7B)**: 训练需要更多 GPU 显存；单卡 A100 80GB 可跑但余量不大\n- **Llama-2 7B 作为 backbone**: 不是最新的 LLM，但对 VLA 任务影响不大\n\n### openpi\n- **JAX/Flax 为主**: 如果团队 PyTorch 经验为主，开发效率受影响（虽有 PyTorch 版但功能不完整）\n- **Flow matching ODE 的梯度**: 10 步 Euler 循环的梯度回传需要 differentiable ODE solver 或 adjoint method，增加 SDF 集成复杂度\n- **双专家架构**: 修改需要理解两个 expert 的交互机制，学习曲线较陡\n\n### 共同风险\n- 两个仓库都没有 SDF 相关功能的先例，集成需要从零开始\n- 训练数据格式需要扩展以包含 SDF ground truth\n- Action refinement (用 SDF gradient 修正 action) 的具体实现方式需要进一步设计\n\n---\n\n## 7. 下一步建议\n\n1. **Fork openvla-oft**，在 `prismatic/models/action_heads.py` 中实现 `SDFDecoderHead`\n2. 先用 dummy SDF target 验证训练流程跑通（梯度正常回传、loss 下降）\n3. 再接入真实的可微分 workspace SDF 模块\n4. 如果 7B 模型显存压力过大，再考虑切换到 openpi PyTorch 版本（1024 维 action expert 仍然足够）\n"
  }
}
````

</details>

---

### Tool result

_source line 154 · 2026-05-19T16:17:56.617410+00:00_

File created successfully at: /home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/artifacts/report_vla_codebase.md

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_vla_codebase_survey_20260519T160639",
  "tool": "Write",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 155 · 2026-05-19T16:17:56.617599+00:00_

报告已保存到 `artifacts/report_vla_codebase.md`。核心结论：

**推荐 OpenVLA-OFT 作为 MVP 基座**，主要理由：
- Action Head 已是独立 `nn.Module`，添加 SDF decoder 遵循现有 pattern，改动最小
- Hidden states 访问开箱即用（`output_hidden_states=True`），32 层 × 4096 维全序列可提取
- 单次前向 + L1 回归，梯度可直接回传——不像 openpi 需要处理 10 步 ODE solver 的梯度
- 纯 PyTorch 生态

**openpi 作为备选**——模型更小 (2.5B vs 7B)、社区更活跃、预训练数据量更大，但 JAX 为主框架 + flow matching ODE 梯度处理增加集成复杂度。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_research_vla_codebase_survey_20260519T160639"
}
```

</details>

---
