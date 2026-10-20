# Research conversation: I found a potentially important paper during my search: Zhang et al. "Reinforcement Learning Fine-Tuning Enhances Activa

**Multi-Class Annotation Errors in Causal Inference: Topology-Dependent Bias, Sensitivity, and Correction (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 22
- **Recorded user turns:** 1
- **Tool calls:** 7
- **Original source:** `logs/chats/exported-trajectories/account-2/agent-af9d4c86b4e361086.jsonl`
- **Structured JSON:** [`0a6455d2900029fda73f.json`](../../sessions/0a/0a6455d2900029fda73f.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

22 recorded events

### User

_source line 1 · 2026-05-19T23:42:42.133Z_

I found a potentially important paper during my search: Zhang et al. "Reinforcement Learning Fine-Tuning Enhances Activation Intensity and Diversity in the Internal Circuitry of LLMs" (arXiv 2509.21044). The concurrent work search flagged this as using EAP (edge attribution patching) to compare internal circuitry before and after RL fine-tuning.

I need to:
1. Verify this paper exists at arXiv 2509.21044
2. Understand what it actually studies - does it look at calibration specifically, or general circuit changes?
3. Does it compare across multiple training stages (Base, SFT, DPO, RL)?
4. Does it use OLMo models?
5. How does it relate to/threaten the novelty of a proposal about "factorial mechanistic dissection of calibration circuits across post-training pathways"?

Also search for: "CORAL Miao Ungar ICML 2026 arXiv 2602.06022" to verify this paper exists and understand how it relates.

And search for: "Confidence Regulation Neurons language models arXiv 2406.16254" to verify this paper.

Report findings for all three papers.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "eec20fb0-9336-4e73-a283-089bd6e9bec5",
  "agentId": "af9d4c86b4e361086",
  "type": "user",
  "uuid": "0836b50b-9d95-4e2a-a373-cb6d3f709cd7",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "b89f7886-bb1e-46f5-8067-f36e58028d73",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 2 · 2026-05-19T23:42:42.135Z_

```json
{
  "parentUuid": "0836b50b-9d95-4e2a-a373-cb6d3f709cd7",
  "isSidechain": true,
  "agentId": "af9d4c86b4e361086",
  "attachment": {
    "type": "deferred_tools_delta",
    "addedNames": [
      "CronCreate",
      "CronDelete",
      "CronList",
      "EnterWorktree",
      "ExitWorktree",
      "Monitor",
      "NotebookEdit",
      "PushNotification",
      "RemoteTrigger",
      "TaskStop",
      "WebFetch",
      "WebSearch"
    ],
    "addedLines": [
      "CronCreate",
      "CronDelete",
      "CronList",
      "EnterWorktree",
      "ExitWorktree",
      "Monitor",
      "NotebookEdit",
      "PushNotification",
      "RemoteTrigger",
      "TaskStop",
      "WebFetch",
      "WebSearch"
    ],
    "removedNames": [],
    "readdedNames": []
  },
  "type": "attachment",
  "uuid": "40e69482-8c26-4ed6-a582-85e9c540200b",
  "timestamp": "2026-05-19T23:42:42.135Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "b89f7886-bb1e-46f5-8067-f36e58028d73",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 3 · 2026-05-19T23:42:42.136Z_

```json
{
  "parentUuid": "40e69482-8c26-4ed6-a582-85e9c540200b",
  "isSidechain": true,
  "agentId": "af9d4c86b4e361086",
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "01ae22c4-1a60-4109-8e30-5f0118bfcedf",
  "timestamp": "2026-05-19T23:42:42.136Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "b89f7886-bb1e-46f5-8067-f36e58028d73",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Assistant

_source line 4 · 2026-05-19T23:42:44.710Z_



I'll search for all three papers simultaneously to verify their existence and understand their content.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "01ae22c4-1a60-4109-8e30-5f0118bfcedf",
  "isSidechain": true,
  "agentId": "af9d4c86b4e361086",
  "requestId": "req_011CbCpAvmnURW8X6CtSs286",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "2ba5f2fd-6ca5-440c-bd8b-cf4819357a75",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "b89f7886-bb1e-46f5-8067-f36e58028d73",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015e1CGoknfbg8ipnExwPa8w",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1621,
      "cache_read_input_tokens": 7773,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1621,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 2,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-19T23:42:45.470Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_017jVPdXcsmVZFWxxcES2iJD`</summary>

```json
{
  "query": "select:WebFetch,WebSearch",
  "max_results": 2
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2ba5f2fd-6ca5-440c-bd8b-cf4819357a75",
  "isSidechain": true,
  "agentId": "af9d4c86b4e361086",
  "requestId": "req_011CbCpAvmnURW8X6CtSs286",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "72cf5309-41f1-4bf4-be19-9d5b5456e109",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "b89f7886-bb1e-46f5-8067-f36e58028d73",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015e1CGoknfbg8ipnExwPa8w",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1621,
      "cache_read_input_tokens": 7773,
      "output_tokens": 98,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1621
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 98,
          "cache_read_input_tokens": 7773,
          "cache_creation_input_tokens": 1621,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1621,
            "ephemeral_1h_input_tokens": 0
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-19T23:42:45.474Z_

<details><summary>↩ Tool result · `toolu_017jVPdXcsmVZFWxxcES2iJD`</summary>

````text
```json
{
  "type": "tool_reference",
  "tool_name": "WebFetch"
}
```

```json
{
  "type": "tool_reference",
  "tool_name": "WebSearch"
}
```
````

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "72cf5309-41f1-4bf4-be19-9d5b5456e109",
  "isSidechain": true,
  "promptId": "eec20fb0-9336-4e73-a283-089bd6e9bec5",
  "agentId": "af9d4c86b4e361086",
  "type": "user",
  "uuid": "7ece12dd-9204-41cc-aff9-ceabdb6e6049",
  "sourceToolAssistantUUID": "72cf5309-41f1-4bf4-be19-9d5b5456e109",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "b89f7886-bb1e-46f5-8067-f36e58028d73",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 7 · 2026-05-19T23:42:47.957Z_



Now let me search for all three papers simultaneously.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7ece12dd-9204-41cc-aff9-ceabdb6e6049",
  "isSidechain": true,
  "agentId": "af9d4c86b4e361086",
  "requestId": "req_011CbCpBBGv4M8Q2whK9MX1r",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "010609dc-51ca-44c8-8969-91d2380649fc",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "b89f7886-bb1e-46f5-8067-f36e58028d73",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016tag3TCxmZwA6sWLbjsJLX",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1120,
      "cache_read_input_tokens": 9394,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1120,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 2,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool call

_source line 8 · 2026-05-19T23:42:49.856Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_018dVhr1Dm5FUbdtjyUgGYGg`</summary>

```json
{
  "url": "https://arxiv.org/abs/2509.21044",
  "prompt": "Extract the full title, authors, abstract, and key details of this paper. What models does it study? Does it use OLMo? Does it compare Base, SFT, DPO, RL training stages? Does it study calibration specifically? What methods does it use (e.g., edge attribution patching / EAP)? What are its main findings?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "010609dc-51ca-44c8-8969-91d2380649fc",
  "isSidechain": true,
  "agentId": "af9d4c86b4e361086",
  "requestId": "req_011CbCpBBGv4M8Q2whK9MX1r",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "12bacba9-2373-46b5-a689-9f4cde1e4027",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "b89f7886-bb1e-46f5-8067-f36e58028d73",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016tag3TCxmZwA6sWLbjsJLX",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1120,
      "cache_read_input_tokens": 9394,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1120,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 2,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-19T23:42:51.410Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01GfoELRPS1DGLSamufx6SRV`</summary>

```json
{
  "url": "https://arxiv.org/abs/2602.06022",
  "prompt": "Extract the full title, authors, abstract, and key details of this paper. Is this the CORAL paper by Miao and Ungar? Is it accepted at ICML 2026? What does it study? How does it relate to calibration of language models?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "12bacba9-2373-46b5-a689-9f4cde1e4027",
  "isSidechain": true,
  "agentId": "af9d4c86b4e361086",
  "requestId": "req_011CbCpBBGv4M8Q2whK9MX1r",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "2441d244-7c97-4467-8b37-d314ee1084f2",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "b89f7886-bb1e-46f5-8067-f36e58028d73",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016tag3TCxmZwA6sWLbjsJLX",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1120,
      "cache_read_input_tokens": 9394,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1120,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 2,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool call

_source line 10 · 2026-05-19T23:42:52.365Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01KCn5uiMqkUf31WuuuvTuac`</summary>

```json
{
  "url": "https://arxiv.org/abs/2406.16254",
  "prompt": "Extract the full title, authors, abstract, and key details of this paper. Does it study \"confidence regulation neurons\" in language models? What are its main findings about how LLMs regulate confidence internally?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2441d244-7c97-4467-8b37-d314ee1084f2",
  "isSidechain": true,
  "agentId": "af9d4c86b4e361086",
  "requestId": "req_011CbCpBBGv4M8Q2whK9MX1r",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "d9c6fff5-f585-4c02-a12f-78bdb7298e42",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "b89f7886-bb1e-46f5-8067-f36e58028d73",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016tag3TCxmZwA6sWLbjsJLX",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1120,
      "cache_read_input_tokens": 9394,
      "output_tokens": 405,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1120
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 405,
          "cache_read_input_tokens": 9394,
          "cache_creation_input_tokens": 1120,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1120,
            "ephemeral_1h_input_tokens": 0
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool result

_source line 11 · 2026-05-19T23:42:55.843Z_

<details><summary>↩ Tool result · `toolu_018dVhr1Dm5FUbdtjyUgGYGg`</summary>

```text
# Paper Summary

**Title:** "Reinforcement Learning Fine-Tuning Enhances Activation Intensity and Diversity in the Internal Circuitry of LLMs"

**Authors:** Honglin Zhang, Qianyue Hao, Fengli Xu, Yong Li

## Key Details

**Models Studied:** The research examines "multiple model families and mathematical datasets" but doesn't specify OLMo or other particular model names in the provided abstract.

**Training Stages:** The paper compares supervised fine-tuning (SFT) and reinforcement learning (RL) approaches. It specifically analyzes PPO, GRPO, and Direct Preference Optimization (DPO) methods, examining how they differ in their effects on internal model structure.

**Methodology:** The study uses edge attribution patching (EAP) to investigate internal differences before and after RL fine-tuning.

**Main Findings:**

1. RL post-training produces an overall increase in average activation intensity, meaning "more internal pathways are engaged and their signals become stronger"

2. Greater diversity emerges in activation patterns through higher entropy and less concentrated distributions

3. These changes suggest "RL reshapes information flow to be both more redundant and more flexible," potentially explaining advantages in mathematical reasoning

4. DPO exhibits substantially different behavior compared to online RL methods, showing weaker or inconsistent internal changes

**Note:** The paper does not specifically study calibration based on the abstract provided.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "12bacba9-2373-46b5-a689-9f4cde1e4027",
  "isSidechain": true,
  "promptId": "eec20fb0-9336-4e73-a283-089bd6e9bec5",
  "agentId": "af9d4c86b4e361086",
  "type": "user",
  "uuid": "f1c6e499-1d88-4899-9c05-20b5621d0676",
  "sourceToolAssistantUUID": "12bacba9-2373-46b5-a689-9f4cde1e4027",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "b89f7886-bb1e-46f5-8067-f36e58028d73",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-19T23:42:56.376Z_

<details><summary>↩ Tool result · `toolu_01GfoELRPS1DGLSamufx6SRV`</summary>

```text
# CORAL Paper Summary

**Full Title:** "Correctness-Optimized Residual Activation Lens (CORAL): Transferrable and Calibration-Aware Inference-Time Steering"

**Authors:** Miranda Muqing Miao, Young-Min Cho, Lyle Ungar

**Submission Date:** February 5, 2026

## Is this the CORAL paper by Miao and Ungar?
Yes, this matches the authorship you referenced.

## Acceptance Status
The document does not indicate acceptance at ICML 2026. It shows only an arXiv submission with no journal reference listed.

## Research Focus
The paper addresses miscalibration in large language models. The authors note that "LLMs exhibit persistent miscalibration, especially after instruction tuning and preference alignment." Rather than expensive retraining, they propose CORAL as an inference-time solution.

## Key Innovation
CORAL uses "weight-decay MLP probes" to extract correctness signals from internal model activations. The method operates on 7B-parameter models without requiring model retraining.

## Calibration Connection
The work directly targets calibration improvement, reporting "expected calibration error (ECE) by 50% on average" alongside accuracy gains. The approach demonstrates that "distributed information in model internals can be extracted using regularized probes" to enhance both correctness and calibration for multiple-choice question-answering tasks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "2441d244-7c97-4467-8b37-d314ee1084f2",
  "isSidechain": true,
  "promptId": "eec20fb0-9336-4e73-a283-089bd6e9bec5",
  "agentId": "af9d4c86b4e361086",
  "type": "user",
  "uuid": "f0bcf624-f51b-40c9-931e-1f2a949d6ac9",
  "sourceToolAssistantUUID": "2441d244-7c97-4467-8b37-d314ee1084f2",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "b89f7886-bb1e-46f5-8067-f36e58028d73",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 13 · 2026-05-19T23:42:57.563Z_

<details><summary>↩ Tool result · `toolu_01KCn5uiMqkUf31WuuuvTuac`</summary>

```text
# Paper Summary: Confidence Regulation Neurons in Language Models

**Full Title:** Confidence Regulation Neurons in Language Models

**Authors:** Alessandro Stolfo, Ben Wu, Wes Gurnee, Yonatan Belinkov, Xingyi Song, Mrinmaya Sachan, Neel Nanda

**ArXiv ID:** 2406.16254 | **Venue:** NeurIPS 2024

---

## Does it Study Confidence Regulation Neurons?

Yes, directly. The paper investigates "two critical components believed to influence" uncertainty in language models' next-token predictions.

---

## Main Findings

**Entropy Neurons:**
The researchers identify neurons characterized by "unusually high weight norm" that "influence the final layer normalization scale to effectively scale down the logits." These neurons operate through a novel mechanism—writing to an "unembedding null space" to impact residual stream norms with minimal direct logit effects. They appear consistently across models up to 7 billion parameters.

**Token Frequency Neurons:**
The team describes newly discovered neurons that "boost or suppress each token's logit proportionally to its log frequency," shifting output distributions toward or away from unigram distributions.

**Practical Application:**
A detailed case study demonstrates how entropy neurons actively manage confidence when "detecting and continuing repeated subsequences" (induction tasks).

These findings reveal distinct internal mechanisms through which language models calibrate and regulate their certainty levels during prediction.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d9c6fff5-f585-4c02-a12f-78bdb7298e42",
  "isSidechain": true,
  "promptId": "eec20fb0-9336-4e73-a283-089bd6e9bec5",
  "agentId": "af9d4c86b4e361086",
  "type": "user",
  "uuid": "0526e5f0-c457-4a48-869a-ae7d1b21db2f",
  "sourceToolAssistantUUID": "d9c6fff5-f585-4c02-a12f-78bdb7298e42",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "b89f7886-bb1e-46f5-8067-f36e58028d73",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 14 · 2026-05-19T23:43:00.463Z_

Now let me get more details on the Zhang et al. paper to answer the specific questions about models used and training stages more precisely.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0526e5f0-c457-4a48-869a-ae7d1b21db2f",
  "isSidechain": true,
  "agentId": "af9d4c86b4e361086",
  "requestId": "req_011CbCpC4hJvNQmKPeze4kpW",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "5f3d430f-a978-4d39-a8de-a3a2fbe65c4a",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "b89f7886-bb1e-46f5-8067-f36e58028d73",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019GBncSMDmCe6viDqNB6wEL",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1477,
      "cache_read_input_tokens": 10514,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1477,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 4,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-19T23:43:03.273Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_011VKcj7nwyWhToirmi7fMKe`</summary>

```json
{
  "url": "https://arxiv.org/abs/2509.21044",
  "prompt": "Read the full abstract very carefully. List ALL specific model names/families mentioned (e.g., Qwen, LLaMA, OLMo, DeepSeek, etc.). List ALL training stages compared (e.g., Base, SFT, DPO, GRPO, PPO). Does the paper compare a base (pretrained-only) model against post-trained variants? How many training stages total does it analyze? Does it mention OLMo at all?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5f3d430f-a978-4d39-a8de-a3a2fbe65c4a",
  "isSidechain": true,
  "agentId": "af9d4c86b4e361086",
  "requestId": "req_011CbCpC4hJvNQmKPeze4kpW",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "cc2d0569-e7f8-4c7b-b97f-08cab542a802",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "b89f7886-bb1e-46f5-8067-f36e58028d73",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019GBncSMDmCe6viDqNB6wEL",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1477,
      "cache_read_input_tokens": 10514,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1477,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 4,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool call

_source line 16 · 2026-05-19T23:43:03.646Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01RPzrUqBNMDSV4EXGSSgMau`</summary>

```json
{
  "query": "Zhang \"Reinforcement Learning Fine-Tuning Enhances Activation Intensity\" arXiv 2509.21044 models OLMo Qwen"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "cc2d0569-e7f8-4c7b-b97f-08cab542a802",
  "isSidechain": true,
  "agentId": "af9d4c86b4e361086",
  "requestId": "req_011CbCpC4hJvNQmKPeze4kpW",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "f03c3d8a-0581-4ac0-901c-47f01ae358be",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "b89f7886-bb1e-46f5-8067-f36e58028d73",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019GBncSMDmCe6viDqNB6wEL",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1477,
      "cache_read_input_tokens": 10514,
      "output_tokens": 287,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1477
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 287,
          "cache_read_input_tokens": 10514,
          "cache_creation_input_tokens": 1477,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1477,
            "ephemeral_1h_input_tokens": 0
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool result

_source line 17 · 2026-05-19T23:43:06.620Z_

<details><summary>↩ Tool result · `toolu_011VKcj7nwyWhToirmi7fMKe`</summary>

```text
# Analysis of Paper arXiv:2509.21044

## Specific Model Names/Families Mentioned
The abstract does **not explicitly name** any specific model families (e.g., Qwen, LLaMA, OLMo, DeepSeek). It only refers generically to "multiple model families."

## Training Stages Compared
The paper compares the following training stages:
1. **Base/Pretrained models** (implied as starting point)
2. **SFT** (Supervised Fine-Tuning)
3. **PPO-based training**
4. **GRPO-based training**
5. **DPO** (Direct Preference Optimization)

**Total: 5 stages analyzed** (including the base model as the reference point)

## Base vs. Post-trained Comparison
Yes, the paper explicitly compares base models against post-trained variants. The abstract states that "RL fine-tuning improves the capability of LLMs beyond what SFT alone achieves" and investigates "internal differences of LLMs before and after RL fine-tuning."

## OLMo Mention
**No, OLMo is not mentioned** in the provided abstract or page content.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "cc2d0569-e7f8-4c7b-b97f-08cab542a802",
  "isSidechain": true,
  "promptId": "eec20fb0-9336-4e73-a283-089bd6e9bec5",
  "agentId": "af9d4c86b4e361086",
  "type": "user",
  "uuid": "5c434a0e-fb15-419e-a315-8600754b972c",
  "sourceToolAssistantUUID": "cc2d0569-e7f8-4c7b-b97f-08cab542a802",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "b89f7886-bb1e-46f5-8067-f36e58028d73",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-19T23:43:10.489Z_

<details><summary>↩ Tool result · `toolu_01RPzrUqBNMDSV4EXGSSgMau`</summary>

```text
Web search results for query: "Zhang "Reinforcement Learning Fine-Tuning Enhances Activation Intensity" arXiv 2509.21044 models OLMo Qwen"

Links: [{"title":"[2509.21044] Reinforcement Learning Fine-Tuning Enhances Activation Intensity and Diversity in the Internal Circuitry of LLMs","url":"https://arxiv.org/abs/2509.21044"},{"title":"Reinforcement Learning Fine-Tuning Enhances Activation Intensity and Diversity in the Internal Circuitry of LLMs","url":"https://arxiv.org/html/2509.21044"},{"title":"Reinforcement Learning Fine-Tuning Enhances Activation Intensity and Diversity in the Internal Circuitry of LLMs","url":"https://arxiv.org/pdf/2509.21044"},{"title":"Reinforcement Learning for Intensity Control: An Application to Choice-Based Network Revenue Management","url":"https://arxiv.org/pdf/2406.05358"},{"title":"Balancing Expressivity and Robustness: Constrained Rational Activations for Reinforcement Learning","url":"https://arxiv.org/pdf/2507.14736"}]

I found the paper you're looking for! Here are the key details:

**Paper Title:** "Reinforcement Learning Fine-Tuning Enhances Activation Intensity and Diversity in the Internal Circuitry of LLMs"

**Authors:** Honglin Zhang, Qianyue Hao, Fengli Xu, and Yong Li from Tsinghua University

**arXiv ID:** 2509.21044

**Key Findings:**

The analysis across multiple model families shows two robust effects of online RL post-training: (i) an overall increase in activation intensity, indicating that more internal pathways are engaged and their signals become stronger, and (ii) greater diversity in activation patterns, reflected by higher entropy and less concentrated edge distributions.

These changes suggest that RL reshapes information flow to be both more redundant and more flexible, which may explain its advantage in generalization. Notably, models fine-tuned with Direct Preference Optimization (DPO) deviate from these trends, exhibiting substantially weaker or inconsistent internal changes compared to PPO- and GRPO-based training.

The paper includes analysis on multiple LLM models, including Qwen2.5 variants as you mentioned, and the research was last updated on January 27, 2026.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f03c3d8a-0581-4ac0-901c-47f01ae358be",
  "isSidechain": true,
  "promptId": "eec20fb0-9336-4e73-a283-089bd6e9bec5",
  "agentId": "af9d4c86b4e361086",
  "type": "user",
  "uuid": "dfa156e5-ca89-4c75-98ff-3c8fb339c556",
  "sourceToolAssistantUUID": "f03c3d8a-0581-4ac0-901c-47f01ae358be",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "b89f7886-bb1e-46f5-8067-f36e58028d73",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 19 · 2026-05-19T23:43:13.218Z_

Let me get the HTML version of the Zhang et al. paper for more details on the specific models used.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "dfa156e5-ca89-4c75-98ff-3c8fb339c556",
  "isSidechain": true,
  "agentId": "af9d4c86b4e361086",
  "requestId": "req_011CbCpD1xdtELEg3zHDgkZB",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "33e75e61-c1d5-4a70-b16b-62079cfc063a",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "b89f7886-bb1e-46f5-8067-f36e58028d73",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RwkGocAKy8ckRHCgM9Xzej",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1232,
      "cache_read_input_tokens": 11991,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1232,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 1,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool call

_source line 20 · 2026-05-19T23:43:15.934Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01BwNA23HEuhiV5xkAHbyREP`</summary>

```json
{
  "url": "https://arxiv.org/html/2509.21044",
  "prompt": "I need to know: 1) What SPECIFIC model families/names are used in experiments (e.g., Qwen2.5, LLaMA, DeepSeek, OLMo)? 2) Does the paper study calibration (ECE, reliability diagrams, confidence calibration) at all, or only activation intensity/diversity? 3) What tasks/benchmarks are used? 4) Does the paper do a factorial comparison across training methods, or does it mostly compare Base vs RL? 5) What specific model sizes are used?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "33e75e61-c1d5-4a70-b16b-62079cfc063a",
  "isSidechain": true,
  "agentId": "af9d4c86b4e361086",
  "requestId": "req_011CbCpD1xdtELEg3zHDgkZB",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "72e8c3fd-0afd-437a-bd44-4b3a4585243e",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "b89f7886-bb1e-46f5-8067-f36e58028d73",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RwkGocAKy8ckRHCgM9Xzej",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1232,
      "cache_read_input_tokens": 11991,
      "output_tokens": 228,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1232
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 228,
          "cache_read_input_tokens": 11991,
          "cache_creation_input_tokens": 1232,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1232,
            "ephemeral_1h_input_tokens": 0
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool result

_source line 21 · 2026-05-19T23:43:22.135Z_

<details><summary>↩ Tool result · `toolu_01BwNA23HEuhiV5xkAHbyREP`</summary>

```text
# Research Paper Analysis: RL Fine-Tuning and LLM Internal Circuitry

## 1. **Model Families Used in Experiments**

The paper examines four model pairs (~7B parameters each):

- **DeepSeek-Math**: deepseek-math-7b-instruct vs. deepseek-math-7b-rl (LLaMA-based)
- **Mistral**: mistral-7b-sft vs. math-shepherd-mistral-7b-rl
- **Distilled-Qwen**: DeepSeek-R1-Distill-Qwen-7B vs. AceReason-Nemotron-7B
- **Qwen2.5**: Qwen2.5-7B-SFT vs. Qwen2.5-7B-DPO

All models use "Transformer architecture" with "distinctive structural and functional characteristics."

## 2. **Calibration Analysis**

**No calibration research is conducted.** The paper focuses exclusively on internal circuit metrics: "Activation Intensity," "Information Complexity" (entropy-based), and "Distribution Kurtosis." No ECE, reliability diagrams, or confidence calibration studies appear.

## 3. **Tasks and Benchmarks**

Mathematical reasoning datasets only:
- GSM8K
- MATH
- College Math

The authors acknowledge this limitation: "empirical validation is currently confined to mathematical reasoning tasks."

## 4. **Comparison Design**

The study employs a **paired before/after approach** rather than factorial design. It compares base SFT models against their RL-trained counterparts, analyzing three training paradigms (PPO, GRPO, DPO) but not systematically crossing factors.

## 5. **Model Sizes**

All primary experiments use **7B parameters**. One intervention study uses Qwen2.5-**3B**-Instruct. The authors note: "memory overhead...prevented us from extending our experiments to models larger than 7B parameters."
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "72e8c3fd-0afd-437a-bd44-4b3a4585243e",
  "isSidechain": true,
  "promptId": "eec20fb0-9336-4e73-a283-089bd6e9bec5",
  "agentId": "af9d4c86b4e361086",
  "type": "user",
  "uuid": "cba4d6a5-d195-4b24-b647-3b470c19d8f8",
  "sourceToolAssistantUUID": "72e8c3fd-0afd-437a-bd44-4b3a4585243e",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "b89f7886-bb1e-46f5-8067-f36e58028d73",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 22 · 2026-05-19T23:43:59.363Z_

Excellent. Now I have comprehensive information on all three papers. Here is my consolidated report.

---

## Paper 1: Zhang et al. "Reinforcement Learning Fine-Tuning Enhances Activation Intensity and Diversity in the Internal Circuitry of LLMs" (arXiv 2509.21044)

**Verified:** Yes, this paper exists at [arxiv.org/abs/2509.21044](https://arxiv.org/abs/2509.21044).

**Authors:** Honglin Zhang, Qianyue Hao, Fengli Xu, Yong Li (Tsinghua University). Last updated January 27, 2026.

**What it actually studies:** It uses Edge Attribution Patching (EAP) to compare internal circuit-level activation patterns before and after RL fine-tuning, focusing exclusively on **mathematical reasoning** tasks (GSM8K, MATH, College Math). It does **NOT** study calibration at all -- no ECE, no reliability diagrams, no confidence calibration analysis. Its metrics are activation intensity, information complexity (entropy), and distribution kurtosis.

**Training stages compared:** It uses a **paired before/after design** (SFT vs. RL-tuned variant), not a true factorial comparison. The four model pairs are:
- DeepSeek-Math-7B (SFT vs. RL)
- Mistral-7B (SFT vs. RL via Math-Shepherd)
- Distilled-Qwen-7B (DeepSeek-R1-Distill vs. AceReason-Nemotron)
- Qwen2.5-7B (SFT vs. DPO)

It compares PPO, GRPO, and DPO training paradigms but does **not** do a systematic factorial crossing of Base -> SFT -> DPO -> RL stages on the same model lineage.

**Does it use OLMo?** No. It uses DeepSeek-Math, Mistral, and Qwen2.5 families, all at ~7B scale.

**Main findings:** Online RL (PPO/GRPO) increases activation intensity (more pathways engaged, stronger signals) and diversity (higher entropy, less concentrated distributions). DPO deviates from these trends, showing weaker/inconsistent internal changes.

**Novelty threat assessment for "factorial mechanistic dissection of calibration circuits across post-training pathways":**

This paper is related but **does not threaten the core novelty** of a calibration-focused proposal for the following reasons:
1. **No calibration focus** -- Zhang et al. study activation intensity/diversity, not calibration (ECE, confidence, reliability).
2. **No factorial design** -- They do paired SFT-vs-RL comparisons, not a systematic Base -> SFT -> DPO -> RL progression on the same model.
3. **No OLMo** -- They use different model families.
4. **Different research question** -- They ask "how does RL reshape circuits for math reasoning?" not "how do different post-training stages create or destroy calibration circuits?"

However, it **must be cited as concurrent/related work** because it shares the methodology (EAP for comparing circuits across training methods) and the broad theme (mechanistic changes from post-training). The key differentiation would be: (a) calibration as the target phenomenon, (b) factorial design across all training stages, and (c) using a single model family (OLMo) to isolate the effect of each stage.

---

## Paper 2: CORAL by Miao, Cho, and Ungar (arXiv 2602.06022)

**Verified:** Yes, this paper exists at [arxiv.org/abs/2602.06022](https://arxiv.org/abs/2602.06022).

**Full title:** "Correctness-Optimized Residual Activation Lens (CORAL): Transferrable and Calibration-Aware Inference-Time Steering"

**Authors:** Miranda Muqing Miao, Young-Min Cho, Lyle Ungar. Submitted February 5, 2026.

**ICML 2026 status:** The arXiv page does **not** indicate ICML 2026 acceptance. It may still be under review or accepted without the arXiv listing being updated.

**What it studies:** It addresses LLM miscalibration, particularly after instruction tuning and preference alignment. Rather than retraining, CORAL uses weight-decay MLP probes to extract correctness signals from internal model activations for inference-time steering on 7B models.

**Key results:** Reduces expected calibration error (ECE) by ~50% on average while also improving accuracy, demonstrating that distributed information in model internals can be extracted via regularized probes for multiple-choice QA tasks.

**Relevance:** Directly relevant to calibration research. It is a probe-based inference-time intervention approach, not a mechanistic interpretability study of how calibration circuits form/change across training stages. A factorial mechanistic dissection proposal would be complementary -- CORAL shows calibration information exists in activations; a mechanistic study would explain *how* and *where* that information is structured and how post-training reshapes it.

---

## Paper 3: "Confidence Regulation Neurons in Language Models" (arXiv 2406.16254)

**Verified:** Yes, this paper exists at [arxiv.org/abs/2406.16254](https://arxiv.org/abs/2406.16254).

**Authors:** Alessandro Stolfo, Ben Wu, Wes Gurnee, Yonatan Belinkov, Xingyi Song, Mrinmaya Sachan, Neel Nanda.

**Venue:** NeurIPS 2024.

**What it studies:** It identifies two types of neurons that regulate confidence/uncertainty in LLM next-token predictions:
1. **Entropy neurons** -- neurons with unusually high weight norms that influence final layer normalization to effectively scale down logits. They operate by writing to an "unembedding null space" to impact residual stream norms.
2. **Token frequency neurons** -- newly discovered neurons that boost or suppress each token's logit proportionally to its log frequency, shifting output distributions toward/away from unigram distributions.

A case study demonstrates how entropy neurons actively manage confidence during induction (repeated subsequence) tasks. Results are consistent across models up to 7B parameters.

**Relevance:** This is a foundational reference for any work on calibration circuits. It identifies the neuron-level mechanisms for confidence regulation but does not study how these mechanisms change across post-training stages (Base -> SFT -> DPO -> RL). A factorial mechanistic dissection proposal would build directly on this work by asking: do entropy neurons and token frequency neurons change their behavior or connectivity across training stages, and does this explain calibration differences?

---

## Summary of the Three-Paper Landscape

| Aspect | Zhang et al. (2509.21044) | CORAL (2602.06022) | Stolfo et al. (2406.16254) |
|---|---|---|---|
| Studies calibration? | No | Yes (ECE reduction) | Yes (confidence mechanisms) |
| Mechanistic interpretability? | Yes (EAP circuits) | No (probe-based) | Yes (neuron-level) |
| Compares training stages? | Partially (SFT vs RL) | Notes post-training degrades calibration | No |
| Factorial design? | No | No | No |
| Uses OLMo? | No | No | No |

The key novelty gap that remains open: **no existing work performs a systematic factorial mechanistic dissection (Base -> SFT -> DPO -> RL) of calibration-specific circuits using a single model family**. Zhang et al. is the closest methodologically (EAP across training stages) but targets a different phenomenon (math reasoning activation patterns, not calibration). Stolfo et al. identifies the relevant neurons but doesn't track them across training. CORAL demonstrates calibration information exists in activations but doesn't do mechanistic analysis of circuit structure.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "cba4d6a5-d195-4b24-b647-3b470c19d8f8",
  "isSidechain": true,
  "agentId": "af9d4c86b4e361086",
  "requestId": "req_011CbCpDsnY9qh65RFMBPm9J",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "cdbc3e7f-b043-47c2-a661-8c574ee1d6a4",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "b89f7886-bb1e-46f5-8067-f36e58028d73",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LXd6G65WZdWdZ4pAFzkLbA",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 710,
      "cache_read_input_tokens": 13223,
      "output_tokens": 1908,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 710
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1908,
          "cache_read_input_tokens": 13223,
          "cache_creation_input_tokens": 710,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 710,
            "ephemeral_1h_input_tokens": 0
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---
