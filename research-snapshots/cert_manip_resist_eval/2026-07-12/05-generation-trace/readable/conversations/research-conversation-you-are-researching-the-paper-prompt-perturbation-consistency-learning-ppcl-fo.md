# Research conversation: You are researching the paper "Prompt Perturbation Consistency Learning (PPCL) for Robust Language Models" by Qiang et a

**The Weakest Link Across Panel Sizes: Predictor Relevance Patterns in Multi-Judge LLM Evaluation under Adversarial Manipulation (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 43
- **Recorded user turns:** 2
- **Tool calls:** 16
- **Original source:** `logs/chats/exported-trajectories/account-3/agent-a905d999b9deee1fe.jsonl`
- **Structured JSON:** [`cdd2f28d5ee7e119986e.json`](../../sessions/cd/cdd2f28d5ee7e119986e.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

40 recorded events

### User

_source line 1 · 2026-05-29T05:30:48.187Z_

You are researching the paper "Prompt Perturbation Consistency Learning (PPCL) for Robust Language Models" by Qiang et al. (EACL 2024 Findings). URL: https://arxiv.org/abs/2402.15833

Tasks:
1. Use WebFetch to read the arxiv abstract page for this paper.
2. Use WebFetch to read the HTML version for method details (try https://arxiv.org/html/2402.15833).
3. Search for any reviews or discussion of this paper.

For each source, extract:
- The exact problem/gap they identified
- Their key insight: how consistency regularization works here
- Technical method: what loss function (KL/JS divergence), how perturbations are generated, how it's integrated into training
- Specific quantitative results (recovery percentages, comparison to pure augmentation)
- The claim about being 10x more data-efficient than augmentation

Return a detailed summary (under 1500 words) covering all the above points. Be specific about the mathematical formulation and technical details.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "76f1366f-40a2-4dae-a639-d8c8a80dcb55",
  "agentId": "a905d999b9deee1fe",
  "type": "user",
  "uuid": "e5bd71a8-8b8c-4a89-9194-9fdf88c737ba",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "5a7a1069-aaa7-4692-b429-b8501e411ab6",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 2 · 2026-05-29T05:30:48.191Z_

```json
{
  "parentUuid": "e5bd71a8-8b8c-4a89-9194-9fdf88c737ba",
  "isSidechain": true,
  "agentId": "a905d999b9deee1fe",
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
  "uuid": "9d2cee14-ae31-44b1-b7b2-826dc06e7f84",
  "timestamp": "2026-05-29T05:30:48.191Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "5a7a1069-aaa7-4692-b429-b8501e411ab6",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 3 · 2026-05-29T05:30:48.191Z_

```json
{
  "parentUuid": "9d2cee14-ae31-44b1-b7b2-826dc06e7f84",
  "isSidechain": true,
  "agentId": "a905d999b9deee1fe",
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "68cc0cae-cdc7-493c-816e-66d9b40573ec",
  "timestamp": "2026-05-29T05:30:48.191Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "5a7a1069-aaa7-4692-b429-b8501e411ab6",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Assistant

_source line 4 · 2026-05-29T05:30:54.765Z_



I'll fetch the paper details from multiple sources in parallel.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "68cc0cae-cdc7-493c-816e-66d9b40573ec",
  "isSidechain": true,
  "agentId": "a905d999b9deee1fe",
  "requestId": "req_011CbWJzmgWCa9GFGui22PZ4",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "b343cb80-4259-4c8c-9fc4-49742d8d5d39",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "5a7a1069-aaa7-4692-b429-b8501e411ab6",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KTLKnf9pcMPDQvtxxRWdRQ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1579,
      "cache_read_input_tokens": 7413,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1579,
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

_source line 5 · 2026-05-29T05:30:55.292Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_012Z7i8CMGn9nwRe4tsJ7doS`</summary>

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
  "parentUuid": "b343cb80-4259-4c8c-9fc4-49742d8d5d39",
  "isSidechain": true,
  "agentId": "a905d999b9deee1fe",
  "requestId": "req_011CbWJzmgWCa9GFGui22PZ4",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "69e16ab0-056d-4c93-8090-f2903d3722fc",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "5a7a1069-aaa7-4692-b429-b8501e411ab6",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KTLKnf9pcMPDQvtxxRWdRQ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1579,
      "cache_read_input_tokens": 7413,
      "output_tokens": 93,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1579
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 93,
          "cache_read_input_tokens": 7413,
          "cache_creation_input_tokens": 1579,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1579,
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

_source line 6 · 2026-05-29T05:30:55.297Z_

<details><summary>↩ Tool result · `toolu_012Z7i8CMGn9nwRe4tsJ7doS`</summary>

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
  "parentUuid": "69e16ab0-056d-4c93-8090-f2903d3722fc",
  "isSidechain": true,
  "promptId": "76f1366f-40a2-4dae-a639-d8c8a80dcb55",
  "agentId": "a905d999b9deee1fe",
  "type": "user",
  "uuid": "b25862a3-62c4-4274-bc4f-5d491c851bcd",
  "sourceToolAssistantUUID": "69e16ab0-056d-4c93-8090-f2903d3722fc",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "5a7a1069-aaa7-4692-b429-b8501e411ab6",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 7 · 2026-05-29T05:30:59.784Z_



Now let me fetch from all three sources in parallel.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b25862a3-62c4-4274-bc4f-5d491c851bcd",
  "isSidechain": true,
  "agentId": "a905d999b9deee1fe",
  "requestId": "req_011CbWK1JFXYPAs6Chtj48v8",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "d282b614-2914-4e57-b359-30ab2c48b712",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "5a7a1069-aaa7-4692-b429-b8501e411ab6",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011RV3uBrpCQTKtjzTaHtHTf",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1115,
      "cache_read_input_tokens": 8992,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1115,
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

_source line 8 · 2026-05-29T05:31:01.721Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01D4ZxQA9UXwiDchorEAPMWH`</summary>

```json
{
  "url": "https://arxiv.org/abs/2402.15833",
  "prompt": "Extract the full abstract, authors, title, venue, and any key claims made on this page about the paper. Include all details about their method, results, and contributions."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d282b614-2914-4e57-b359-30ab2c48b712",
  "isSidechain": true,
  "agentId": "a905d999b9deee1fe",
  "requestId": "req_011CbWK1JFXYPAs6Chtj48v8",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "650671af-c952-42c8-8382-e540c38b005c",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "5a7a1069-aaa7-4692-b429-b8501e411ab6",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011RV3uBrpCQTKtjzTaHtHTf",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1115,
      "cache_read_input_tokens": 8992,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1115,
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

_source line 9 · 2026-05-29T05:31:05.549Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01FkmzMECCfhUD1RetyGTaCS`</summary>

```json
{
  "url": "https://arxiv.org/html/2402.15833",
  "prompt": "Extract ALL technical details from this paper including: 1) The exact problem statement and motivation, 2) The mathematical formulation of the consistency regularization loss (KL divergence, JS divergence, or other), 3) How perturbations are generated (character-level, word-level, etc.), 4) The full training objective/loss function, 5) All quantitative results including recovery percentages and comparisons to baselines, 6) Any claims about data efficiency compared to augmentation, 7) The specific datasets and models used, 8) Key equations and their notation. Be as detailed as possible."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "650671af-c952-42c8-8382-e540c38b005c",
  "isSidechain": true,
  "agentId": "a905d999b9deee1fe",
  "requestId": "req_011CbWK1JFXYPAs6Chtj48v8",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "a2645144-75e7-412e-a471-6a1b26e989ee",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "5a7a1069-aaa7-4692-b429-b8501e411ab6",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011RV3uBrpCQTKtjzTaHtHTf",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1115,
      "cache_read_input_tokens": 8992,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1115,
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

_source line 10 · 2026-05-29T05:31:06.121Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01RYkd4miu6d4n6UdAizk875`</summary>

```json
{
  "query": "Prompt Perturbation Consistency Learning PPCL Qiang EACL 2024 review discussion"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a2645144-75e7-412e-a471-6a1b26e989ee",
  "isSidechain": true,
  "agentId": "a905d999b9deee1fe",
  "requestId": "req_011CbWK1JFXYPAs6Chtj48v8",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "365b1500-44ec-4e70-83e2-9e808e6b0867",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "5a7a1069-aaa7-4692-b429-b8501e411ab6",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011RV3uBrpCQTKtjzTaHtHTf",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1115,
      "cache_read_input_tokens": 8992,
      "output_tokens": 385,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1115
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 385,
          "cache_read_input_tokens": 8992,
          "cache_creation_input_tokens": 1115,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1115,
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

_source line 11 · 2026-05-29T05:31:07.111Z_

<details><summary>↩ Tool result · `toolu_01D4ZxQA9UXwiDchorEAPMWH`</summary>

```text
# Paper Summary: Prompt Perturbation Consistency Learning for Robust Language Models

**Title:** Prompt Perturbation Consistency Learning for Robust Language Models

**arXiv ID:** 2402.15833

**Submission Date:** February 24, 2024

**Authors:** Yao Qiang, Subhrangshu Nandi, Ninareh Mehrabi, Greg Ver Steeg, Anoop Kumar, Anna Rumshisky, Aram Galstyan

**Venue:** Computer Science > Computation and Language (cs.CL); Machine Learning (cs.LG)

## Abstract

The paper addresses robustness challenges in large language models for sequence labeling tasks. The researchers demonstrate that "fine-tuning sufficiently large LLMs can produce IC-SF performance comparable to discriminative models." They analyze performance degradation caused by three perturbation types: oronyms, synonyms, and paraphrasing.

## Key Contributions

1. **Performance Achievement:** Fine-tuned LLMs achieve parity with discriminative models on intent classification and slot filling tasks

2. **Robustness Analysis:** Systematic evaluation of how input perturbations affect model performance

3. **Proposed Method - PPCL:** A regularization approach that "works by regularizing the divergence between losses from clean and perturbed samples"

## Key Results

- PPCL recovers approximately 59% of performance loss for intent classification
- PPCL recovers approximately 69% of performance loss for slot filling
- PPCL demonstrates superior efficiency compared to data augmentation, "using ten times fewer augmented data samples"

**Subject Classification:** Computation and Language; Machine Learning
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "650671af-c952-42c8-8382-e540c38b005c",
  "isSidechain": true,
  "promptId": "76f1366f-40a2-4dae-a639-d8c8a80dcb55",
  "agentId": "a905d999b9deee1fe",
  "type": "user",
  "uuid": "aeeee182-ff75-466d-b77b-269cac1d5752",
  "sourceToolAssistantUUID": "650671af-c952-42c8-8382-e540c38b005c",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "5a7a1069-aaa7-4692-b429-b8501e411ab6",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-29T05:31:11.021Z_

<details><summary>↩ Tool result · `toolu_01FkmzMECCfhUD1RetyGTaCS`</summary>

```text
# Summary

The document provided is the **Responsible NLP Research Checklist** (arXiv:2402.15833v1), a structured ethical framework for NLP submissions. It does **not contain technical research content** about a specific NLP problem, mathematical formulations, loss functions, or experimental results.

## What This Document Actually Contains

This is an ethics and reproducibility checklist with five major sections:

1. **General Requirements** - Discussing limitations, risks, and claim clarity
2. **Scientific Artifacts** - Citation, licensing, intended use, anonymization, documentation, and statistics reporting
3. **Computational Experiments** - Parameters, budgets, hyperparameters, result statistics, and package reporting
4. **Human Annotation** - Instructions, payment, consent, ethics board approval, and demographics
5. **AI Assistant Use** - Transparency about generative tool usage

## Why No Technical Details Exist

The checklist itself contains no:
- Problem statements or mathematical formulations
- Loss functions (KL divergence, JS divergence, etc.)
- Perturbation generation methods
- Quantitative experimental results
- Dataset specifications or model architectures
- Technical equations or notation

**To extract technical details**, you would need to reference an actual NLP research paper that uses this checklist as a template, not the checklist itself.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a2645144-75e7-412e-a471-6a1b26e989ee",
  "isSidechain": true,
  "promptId": "76f1366f-40a2-4dae-a639-d8c8a80dcb55",
  "agentId": "a905d999b9deee1fe",
  "type": "user",
  "uuid": "207c7cf0-b001-459a-8dc4-49707672f1b1",
  "sourceToolAssistantUUID": "a2645144-75e7-412e-a471-6a1b26e989ee",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "5a7a1069-aaa7-4692-b429-b8501e411ab6",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 13 · 2026-05-29T05:31:16.391Z_

<details><summary>↩ Tool result · `toolu_01RYkd4miu6d4n6UdAizk875`</summary>

```text
Web search results for query: "Prompt Perturbation Consistency Learning PPCL Qiang EACL 2024 review discussion"

Links: [{"title":"Prompt Perturbation Consistency Learning for Robust Language Models - ACL Anthology","url":"https://aclanthology.org/2024.findings-eacl.91/"},{"title":"Prompt perturbation consistency learning for robust language models - Amazon Science","url":"https://www.amazon.science/publications/prompt-perturbation-consistency-learning-for-robust-language-models"},{"title":"Prompt Perturbation Experiments","url":"https://www.emergentmind.com/topics/prompt-perturbation-experiments"},{"title":"[2402.15833] Prompt Perturbation Consistency Learning for Robust Language Models","url":"https://arxiv.org/abs/2402.15833"},{"title":"Flip-Flop Consistency: Unsupervised Training for Robustness to Prompt Perturbations in LLMs","url":"https://arxiv.org/html/2510.14242v1"},{"title":"[Literature Review] Prompt Perturbation Consistency Learning for Robust Language Models","url":"https://www.themoonlight.io/en/review/prompt-perturbation-consistency-learning-for-robust-language-models"},{"title":"Prompt Perturbation Consistency Learning for Robust Language Models","url":"https://arxiv.org/pdf/2402.15833"},{"title":"Flip-Flop Consistency: Unsupervised Training for Robustness to Prompt Perturbations in LLMs","url":"https://arxiv.org/pdf/2510.14242"}]

Based on the search results, here's what I found about Prompt Perturbation Consistency Learning (PPCL) presented at EACL 2024:

## Paper Overview

The paper "Prompt Perturbation Consistency Learning for Robust Language Models" by Yao Qiang and colleagues was published in the Findings of the Association for Computational Linguistics: EACL 2024.

## Core Approach

PPCL is an efficient mitigation approach which works by regularizing the divergence between losses from clean and perturbed samples. The core idea is to encourage the LLM to produce consistent predictions when given an original utterance and a perturbed version of that utterance.

## Problem Focus

The research systematically analyzes the performance deterioration of fine-tuned models due to three distinct yet relevant types of input perturbations - oronyms, synonyms, and paraphrasing.

## Results

The experiments show that PPCL can recover on an average 59% and 69% of the performance drop for IC and SF tasks, respectively. Furthermore, PPCL beats data augmentation approach while using ten times fewer augmented data samples.

## Technical Details

The paper uses Jensen-Shannon (JS) divergence to quantify the difference between probability distributions.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "365b1500-44ec-4e70-83e2-9e808e6b0867",
  "isSidechain": true,
  "promptId": "76f1366f-40a2-4dae-a639-d8c8a80dcb55",
  "agentId": "a905d999b9deee1fe",
  "type": "user",
  "uuid": "cf0d111f-0164-4720-bb96-5ef3747210f5",
  "sourceToolAssistantUUID": "365b1500-44ec-4e70-83e2-9e808e6b0867",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "5a7a1069-aaa7-4692-b429-b8501e411ab6",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 14 · 2026-05-29T05:31:19.441Z_

The HTML version returned the checklist rather than the paper body. Let me fetch the PDF and additional sources for the technical details.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "cf0d111f-0164-4720-bb96-5ef3747210f5",
  "isSidechain": true,
  "agentId": "a905d999b9deee1fe",
  "requestId": "req_011CbWK2r8wywZoifGhFnBbX",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "1d3da86c-3e7b-443c-a67e-7816746e16af",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "5a7a1069-aaa7-4692-b429-b8501e411ab6",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0157ZdaQ4TLyAD92SDSQX58v",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1866,
      "cache_read_input_tokens": 10107,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1866,
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

_source line 15 · 2026-05-29T05:31:23.664Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01EFbcDmwYvCq3PSnsYjhGiC`</summary>

```json
{
  "url": "https://arxiv.org/pdf/2402.15833",
  "prompt": "Extract ALL technical details: 1) The exact loss function formula for PPCL (KL divergence, JS divergence, etc.), 2) The full training objective combining task loss and consistency loss, 3) How perturbations are generated (character-level oronyms, word-level synonyms, sentence-level paraphrasing), 4) All quantitative results tables - exact numbers for intent classification and slot filling recovery percentages, 5) Comparison with data augmentation baselines including the 10x data efficiency claim, 6) Which LLMs and datasets were used, 7) The hyperparameter lambda that balances losses, 8) Any equations with their exact mathematical notation. Be maximally detailed and include all numbers."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1d3da86c-3e7b-443c-a67e-7816746e16af",
  "isSidechain": true,
  "agentId": "a905d999b9deee1fe",
  "requestId": "req_011CbWK2r8wywZoifGhFnBbX",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "5353ec0d-bfb8-4d1a-bb2c-8e188837a2d7",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "5a7a1069-aaa7-4692-b429-b8501e411ab6",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0157ZdaQ4TLyAD92SDSQX58v",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1866,
      "cache_read_input_tokens": 10107,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1866,
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

_source line 16 · 2026-05-29T05:31:25.615Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_018jVVAE9RUWzrA7PmhMSt5M`</summary>

```json
{
  "url": "https://aclanthology.org/2024.findings-eacl.91/",
  "prompt": "Extract all information about this paper: abstract, key results, any supplementary details, citation information, and links to the PDF or other resources."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5353ec0d-bfb8-4d1a-bb2c-8e188837a2d7",
  "isSidechain": true,
  "agentId": "a905d999b9deee1fe",
  "requestId": "req_011CbWK2r8wywZoifGhFnBbX",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "dec2a596-c1cd-4b90-8050-83e841100b03",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "5a7a1069-aaa7-4692-b429-b8501e411ab6",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0157ZdaQ4TLyAD92SDSQX58v",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1866,
      "cache_read_input_tokens": 10107,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1866,
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

_source line 17 · 2026-05-29T05:31:26.492Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_0139PyjNXr9EsaajuvcieFPT`</summary>

```json
{
  "url": "https://www.themoonlight.io/en/review/prompt-perturbation-consistency-learning-for-robust-language-models",
  "prompt": "Extract the full review or discussion of this paper. Include any critique, strengths, weaknesses, and detailed analysis of the method and results."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "dec2a596-c1cd-4b90-8050-83e841100b03",
  "isSidechain": true,
  "agentId": "a905d999b9deee1fe",
  "requestId": "req_011CbWK2r8wywZoifGhFnBbX",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "38a4f4a9-0e76-4439-a551-f8612d218d24",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "5a7a1069-aaa7-4692-b429-b8501e411ab6",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0157ZdaQ4TLyAD92SDSQX58v",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1866,
      "cache_read_input_tokens": 10107,
      "output_tokens": 478,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1866
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 478,
          "cache_read_input_tokens": 10107,
          "cache_creation_input_tokens": 1866,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1866,
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

_source line 18 · 2026-05-29T05:31:29.926Z_

<details><summary>↩ Tool result · `toolu_01EFbcDmwYvCq3PSnsYjhGiC`</summary>

```text
I appreciate your detailed request, but I must inform you that the provided content appears to be a corrupted or improperly formatted PDF file containing compressed binary data rather than readable text.

The material shows PDF stream objects with FlateDecode compression and technical metadata (objects 210, 135, 224, 229, 232, 265, 292, 299, 310, 343, 345, 349, 357, 373, 382, 394, 403), but the actual document content cannot be extracted or analyzed from this compressed format.

**To assist you effectively, I would need:**

1. A properly decoded PDF or text version of the research paper
2. Direct access to the paper's HTML or plaintext content
3. The paper's title and authors (to potentially retrieve it from academic sources)

**Regarding your specific requests**, once readable content is available, I can extract:
- Mathematical formulas (loss functions, training objectives)
- Quantitative results (accuracy percentages, recovery metrics)
- Hyperparameter specifications (lambda values)
- Dataset and model identifiers
- Perturbation generation methodologies

Please provide the document in a readable format, and I'll deliver a comprehensive technical analysis within your 125-character quotation constraints.

[Binary content (application/pdf, 412.6KB) also saved to /home/ubuntu/.claude-account-3/projects/-home-ubuntu-idea-adversarial/5a7a1069-aaa7-4692-b429-b8501e411ab6/tool-results/webfetch-1780032683714-emq388.pdf]
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "5353ec0d-bfb8-4d1a-bb2c-8e188837a2d7",
  "isSidechain": true,
  "promptId": "76f1366f-40a2-4dae-a639-d8c8a80dcb55",
  "agentId": "a905d999b9deee1fe",
  "type": "user",
  "uuid": "1b262819-f866-4672-b862-e7c439f05376",
  "sourceToolAssistantUUID": "5353ec0d-bfb8-4d1a-bb2c-8e188837a2d7",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "5a7a1069-aaa7-4692-b429-b8501e411ab6",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 19 · 2026-05-29T05:31:30.255Z_

<details><summary>↩ Tool result · `toolu_018jVVAE9RUWzrA7PmhMSt5M`</summary>

```text
# Paper Summary: Prompt Perturbation Consistency Learning for Robust Language Models

## Citation Information
- **Authors:** Yao Qiang, Subhrangshu Nandi, Ninareh Mehrabi, Greg Ver Steeg, Anoop Kumar, Anna Rumshisky, Aram Galstyan
- **Venue:** Findings of the Association for Computational Linguistics: EACL 2024
- **Publication Date:** March 2024
- **Pages:** 1357–1370
- **DOI:** 10.18653/v1/2024.findings-eacl.91
- **Anthology ID:** 2024.findings-eacl.91

## Core Problem
The paper addresses a gap where large language models underperform on sequence labeling tasks like intent classification and slot filling compared to discriminative models. Additionally, there's limited research on LLM robustness against input prompt variations.

## Key Contributions
The authors demonstrate three main findings:
1. Fine-tuned LLMs can match discriminative model performance on intent classification and slot filling
2. Performance degrades significantly with three perturbation types: oronyms, synonyms, and paraphrasing
3. They propose "Prompt Perturbation Consistency Learning (PPCL)" as a mitigation strategy

## Results
PPCL recovered approximately 59% of performance loss for intent classification and 69% for slot filling tasks, while requiring ten times fewer augmented samples compared to standard data augmentation approaches.

## Resources
- **PDF:** https://aclanthology.org/2024.findings-eacl.91.pdf
- **Video:** https://aclanthology.org/2024.findings-eacl.91.mp4
- **Full URL:** https://aclanthology.org/2024.findings-eacl.91/
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "dec2a596-c1cd-4b90-8050-83e841100b03",
  "isSidechain": true,
  "promptId": "76f1366f-40a2-4dae-a639-d8c8a80dcb55",
  "agentId": "a905d999b9deee1fe",
  "type": "user",
  "uuid": "8dadeafc-efd0-4d8e-86bb-cbf7e9a1c3ed",
  "sourceToolAssistantUUID": "dec2a596-c1cd-4b90-8050-83e841100b03",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "5a7a1069-aaa7-4692-b429-b8501e411ab6",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-29T05:31:32.338Z_

<details><summary>↩ Tool result · `toolu_0139PyjNXr9EsaajuvcieFPT`</summary>

```text
# Analysis of "Prompt Perturbation Consistency Learning for Robust Language Models"

## Summary
The document presents a literature review summary rather than a full critical review. It outlines research addressing LLM robustness for Intent Classification and Slot Filling tasks through a novel training approach called PPCL.

## Strengths Highlighted

The paper demonstrates three notable contributions:

1. **Performance Parity**: "Fine-tuning sufficiently large LLMs can achieve IC-SF performance comparable to discriminative models" through prompt selection and supervised fine-tuning on moderate-sized datasets.

2. **Systematic Analysis**: The work systematically investigates how three perturbation types—oronyms, synonyms, and paraphrasing—degrade model performance.

3. **Efficient Solution**: PPCL reportedly "recover[s] a significant portion of the performance drop caused by perturbations" while using substantially fewer augmented samples than data augmentation alternatives.

## Methodological Strengths

- Uses Jensen-Shannon divergence for its symmetry properties, offering balanced similarity measurement
- Combines cross-entropy losses with consistency regularization through a unified objective function
- Generates perturbations through multiple mechanisms (token replacement, semantic-preserving paraphrasing)

## Limitations of Available Content

The provided summary lacks:
- Experimental result comparisons with competing methods
- Ablation study details
- Discussion of computational costs
- Analysis of failure cases or boundary conditions
- Independent peer review or critique

**Note**: This analysis reflects only the content available in the document provided, which functions as a promotional summary rather than a detailed academic critique.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "38a4f4a9-0e76-4439-a551-f8612d218d24",
  "isSidechain": true,
  "promptId": "76f1366f-40a2-4dae-a639-d8c8a80dcb55",
  "agentId": "a905d999b9deee1fe",
  "type": "user",
  "uuid": "99f5a216-b089-411f-bf7e-fb86ce8da3e4",
  "sourceToolAssistantUUID": "38a4f4a9-0e76-4439-a551-f8612d218d24",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "5a7a1069-aaa7-4692-b429-b8501e411ab6",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 21 · 2026-05-29T05:31:34.698Z_

Let me get the full paper content from the ACL Anthology PDF and also search for more technical details.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "99f5a216-b089-411f-bf7e-fb86ce8da3e4",
  "isSidechain": true,
  "agentId": "a905d999b9deee1fe",
  "requestId": "req_011CbWK42P8AotJfPtiQAFhV",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "1ef10c53-880c-4ce7-a8c5-20a15ceca309",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "5a7a1069-aaa7-4692-b429-b8501e411ab6",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AEtGXtVhpv4EeWuSgVwGai",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1716,
      "cache_read_input_tokens": 11973,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1716,
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

_source line 22 · 2026-05-29T05:31:37.094Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01LbsUXCbA93KuvJBF7TxbFL`</summary>

```json
{
  "url": "https://www.amazon.science/publications/prompt-perturbation-consistency-learning-for-robust-language-models",
  "prompt": "Extract ALL technical details about PPCL: the mathematical formulation, loss functions, equations, training procedure, perturbation types, datasets, models, and quantitative results. Be as detailed as possible about the method."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1ef10c53-880c-4ce7-a8c5-20a15ceca309",
  "isSidechain": true,
  "agentId": "a905d999b9deee1fe",
  "requestId": "req_011CbWK42P8AotJfPtiQAFhV",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "96995a26-eea5-44f7-a526-641c648705d0",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "5a7a1069-aaa7-4692-b429-b8501e411ab6",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AEtGXtVhpv4EeWuSgVwGai",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1716,
      "cache_read_input_tokens": 11973,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1716,
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

_source line 23 · 2026-05-29T05:31:38.586Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01HJZED7t6ApSiLPGJvYAHKM`</summary>

```json
{
  "url": "https://www.emergentmind.com/topics/prompt-perturbation-experiments",
  "prompt": "Find and extract any discussion or analysis of the paper 'Prompt Perturbation Consistency Learning for Robust Language Models' by Qiang et al. Include any technical details about the PPCL method, loss functions, results, and comparisons."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "96995a26-eea5-44f7-a526-641c648705d0",
  "isSidechain": true,
  "agentId": "a905d999b9deee1fe",
  "requestId": "req_011CbWK42P8AotJfPtiQAFhV",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "8540c7fb-5245-4cef-b4ae-052c4991c557",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "5a7a1069-aaa7-4692-b429-b8501e411ab6",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AEtGXtVhpv4EeWuSgVwGai",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1716,
      "cache_read_input_tokens": 11973,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1716,
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

_source line 24 · 2026-05-29T05:31:39.477Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_016zW3oyc59zRdpt6onmoHms`</summary>

```json
{
  "query": "\"Prompt Perturbation Consistency Learning\" PPCL Jensen-Shannon divergence loss function training objective lambda"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8540c7fb-5245-4cef-b4ae-052c4991c557",
  "isSidechain": true,
  "agentId": "a905d999b9deee1fe",
  "requestId": "req_011CbWK42P8AotJfPtiQAFhV",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "331696a9-e254-4495-bc1c-65bc1cf19c49",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "5a7a1069-aaa7-4692-b429-b8501e411ab6",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AEtGXtVhpv4EeWuSgVwGai",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1716,
      "cache_read_input_tokens": 11973,
      "output_tokens": 347,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1716
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 347,
          "cache_read_input_tokens": 11973,
          "cache_creation_input_tokens": 1716,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1716,
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

_source line 25 · 2026-05-29T05:31:43.012Z_

<details><summary>↩ Tool result · `toolu_01LbsUXCbA93KuvJBF7TxbFL`</summary>

```text
# PPCL Technical Details - Summary

Based on the provided content, the web page offers **limited technical specifics** about Prompt Perturbation Consistency Learning (PPCL). Here's what's available:

## Core Method
The approach "regularizes the divergence between losses from clean and perturbed samples," though the exact mathematical formulation isn't detailed in the excerpt.

## Perturbation Types
Three distinct perturbation categories are evaluated:
- **Oronyms** (words that sound alike)
- **Synonyms** (words with similar meaning)
- **Paraphrasing** (alternative phrasings)

## Tasks Addressed
- Intent Classification and Slot Filling (IC-SF)
- Sequence labeling tasks for personal assistant systems

## Performance Results
- Recovers approximately **59% of performance drop** for intent classification
- Recovers approximately **69% of performance drop** for slot filling
- Outperforms data augmentation using **10× fewer augmented samples**

## Model Architecture
Fine-tuned large language models (LLMs) achieving performance comparable to discriminative models on IC-SF tasks.

## Limitations
The webpage content lacks:
- Mathematical loss function equations
- Specific training hyperparameters
- Dataset details/names
- Model specifications or sizes
- Detailed algorithmic procedures

**Complete technical details would require accessing the full paper PDF** linked on the page.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "96995a26-eea5-44f7-a526-641c648705d0",
  "isSidechain": true,
  "promptId": "76f1366f-40a2-4dae-a639-d8c8a80dcb55",
  "agentId": "a905d999b9deee1fe",
  "type": "user",
  "uuid": "d0641b87-8549-4976-bda1-b9d9cbe92ad2",
  "sourceToolAssistantUUID": "96995a26-eea5-44f7-a526-641c648705d0",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "5a7a1069-aaa7-4692-b429-b8501e411ab6",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 26 · 2026-05-29T05:31:44.702Z_

<details><summary>↩ Tool result · `toolu_01HJZED7t6ApSiLPGJvYAHKM`</summary>

```text
# Analysis of PPCL by Qiang et al. (2024)

## Method Overview

The paper introduces **PPCL (Probabilistic Pairwise Contrastive Loss)**, a consistency learning approach that addresses prompt perturbation robustness. The technique regularizes the divergence between output distributions when comparing clean versus perturbed prompts.

## Technical Details

**Loss Function:**
The consistency regularization employs Jensen-Shannon divergence: "Lconsistency = 1L ∑j=1L JS(qc(j), qp(j))" where qc and qp represent output distributions for clean and perturbed prompts respectively.

## Experimental Results

According to the comparative outcomes table:
- **Intent Classification (IC):** Recovered 59% of performance loss
- **Slot Filling (SF):** Recovered 69% of performance loss  
- **Efficiency:** Required "10× fewer augmentations than DA" (domain alignment approaches)

## Key Theoretical Contribution

The research formalizes "Jensen–Shannon consistency as essential for alignment between clean and perturbed samples," demonstrating empirically that this regularization mechanism alone provides an additional 6–12 percentage point recovery in slot filling tasks.

## Positioning

PPCL represents a regularization-based defense strategy that achieves substantial robustness improvements with minimal computational overhead compared to traditional data augmentation methods.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "8540c7fb-5245-4cef-b4ae-052c4991c557",
  "isSidechain": true,
  "promptId": "76f1366f-40a2-4dae-a639-d8c8a80dcb55",
  "agentId": "a905d999b9deee1fe",
  "type": "user",
  "uuid": "1b4cf230-6a27-4cb9-92fc-16f4b4344d0d",
  "sourceToolAssistantUUID": "8540c7fb-5245-4cef-b4ae-052c4991c557",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "5a7a1069-aaa7-4692-b429-b8501e411ab6",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 27 · 2026-05-29T05:31:46.407Z_

<details><summary>↩ Tool result · `toolu_016zW3oyc59zRdpt6onmoHms`</summary>

```text
Web search results for query: ""Prompt Perturbation Consistency Learning" PPCL Jensen-Shannon divergence loss function training objective lambda"

Links: [{"title":"Prompt Perturbation Experiments","url":"https://www.emergentmind.com/topics/prompt-perturbation-experiments"},{"title":"[Literature Review] Prompt Perturbation Consistency Learning for Robust Language Models","url":"https://www.themoonlight.io/en/review/prompt-perturbation-consistency-learning-for-robust-language-models"},{"title":"Prompt Perturbation Consistency Learning for Robust Language Models","url":"https://arxiv.org/pdf/2402.15833"},{"title":"Prompt Perturbation Consistency Learning for Robust Language Models","url":"https://openreview.net/pdf/6531be6f8b4a39b29dc72a3ad3d4fd6eba931edb.pdf"},{"title":"Flip-Flop Consistency: Unsupervised Training for Robustness to Prompt Perturbations in LLMs","url":"https://arxiv.org/html/2510.14242v1"},{"title":"Prompt perturbation consistency learning for robust language models - Amazon Science","url":"https://www.amazon.science/publications/prompt-perturbation-consistency-learning-for-robust-language-models"},{"title":"[2402.15833] Prompt Perturbation Consistency Learning for Robust Language Models","url":"https://arxiv.org/abs/2402.15833"},{"title":"Prompt Perturbation Consistency Learning for Robust Language Models - ACL Anthology","url":"https://aclanthology.org/2024.findings-eacl.91/"}]

Based on the search results, I found comprehensive information about Prompt Perturbation Consistency Learning (PPCL):

## Overview
PPCL is an efficient mitigation approach that enhances the robustness of language models by adding a regularization term to the training objective that minimizes the divergence between the losses calculated from clean and perturbed samples.

## Training Objective and Loss Function
The training objective incorporates the Jensen-Shannon (JS) divergence of output probabilities between a clean utterance and its perturbed counterpart, integrated with the standard cross-entropy loss utilized in the auto-regression phase of the fine-tuning process.

## Technical Details
PPCL's core idea is to encourage the language model to produce consistent predictions when given an original utterance and a perturbed version of that utterance.

The mathematical implementation involves:
- JS divergence calculation: JS(ŷjc || ŷjp) = (1/2) * (KL(ŷjc || ŷjm) + KL(ŷjp || ŷjm)), where ŷjm = (1/2) * (ŷjc + ŷjp) is the average probability distribution.
- The average JS divergence across all output tokens is used as the perturbation consistency learning loss LJS: LJS = (1/L) * Σj=1L JS(ŷjc || ŷjp), where L is the length of the output sequence.

## Why Jensen-Shannon Divergence?
JS divergence is chosen due to its symmetry, which provides a more balanced measure of similarity compared to Kullback-Leibler (KL) divergence.

The search results don't contain specific details about the lambda hyperparameter value, but they confirm the core training objective structure combining cross-entropy loss with the JS divergence regularization term.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "331696a9-e254-4495-bc1c-65bc1cf19c49",
  "isSidechain": true,
  "promptId": "76f1366f-40a2-4dae-a639-d8c8a80dcb55",
  "agentId": "a905d999b9deee1fe",
  "type": "user",
  "uuid": "bad46dc2-ae90-4552-8d6b-89845d4f7f3c",
  "sourceToolAssistantUUID": "331696a9-e254-4495-bc1c-65bc1cf19c49",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "5a7a1069-aaa7-4692-b429-b8501e411ab6",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 28 · 2026-05-29T05:31:48.545Z_

Let me fetch the OpenReview version and the follow-up paper that cites PPCL for additional details.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "bad46dc2-ae90-4552-8d6b-89845d4f7f3c",
  "isSidechain": true,
  "agentId": "a905d999b9deee1fe",
  "requestId": "req_011CbWK54Vei2BEgwemNw6cV",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "1e2910fe-3b5a-4fb4-933c-f4658adf754d",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "5a7a1069-aaa7-4692-b429-b8501e411ab6",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01J6DRpAMJ59tffJhxN1EhQt",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1926,
      "cache_read_input_tokens": 13689,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1926,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 3,
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

_source line 29 · 2026-05-29T05:31:51.435Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01RCuts9h6ULukioi7dTGZMS`</summary>

```json
{
  "url": "https://arxiv.org/html/2510.14242v1",
  "prompt": "Find all references and discussion of PPCL (Prompt Perturbation Consistency Learning) by Qiang et al. Extract how this paper describes PPCL's method, loss function, limitations, and any comparison results. Also extract any details about the PPCL training objective formula, lambda parameter, and data efficiency claims."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1e2910fe-3b5a-4fb4-933c-f4658adf754d",
  "isSidechain": true,
  "agentId": "a905d999b9deee1fe",
  "requestId": "req_011CbWK54Vei2BEgwemNw6cV",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "de9d048d-04ce-4134-a133-87ca738770c1",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "5a7a1069-aaa7-4692-b429-b8501e411ab6",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01J6DRpAMJ59tffJhxN1EhQt",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1926,
      "cache_read_input_tokens": 13689,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1926,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 3,
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

_source line 30 · 2026-05-29T05:31:55.586Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01R6UCtGsM9N9BkyU4Uh1MrN`</summary>

```json
{
  "url": "https://openreview.net/pdf/6531be6f8b4a39b29dc72a3ad3d4fd6eba931edb.pdf",
  "prompt": "Extract ALL technical details from this paper: 1) The complete PPCL training objective formula L_total = L_CE + lambda * L_JS, 2) The exact JS divergence formula, 3) How perturbations are generated for oronyms, synonyms, paraphrasing, 4) All experimental results with exact numbers, 5) The lambda hyperparameter value, 6) Which LLMs were used (LLaMA sizes), 7) Which datasets (MASSIVE, SLURP, etc.), 8) The data augmentation comparison showing 10x efficiency, 9) Any ablation studies. Include all equations and numbers."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "de9d048d-04ce-4134-a133-87ca738770c1",
  "isSidechain": true,
  "agentId": "a905d999b9deee1fe",
  "requestId": "req_011CbWK54Vei2BEgwemNw6cV",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "b70ef08f-ec32-40d6-8d02-8ed6a98c57fc",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "5a7a1069-aaa7-4692-b429-b8501e411ab6",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01J6DRpAMJ59tffJhxN1EhQt",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1926,
      "cache_read_input_tokens": 13689,
      "output_tokens": 416,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1926
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 416,
          "cache_read_input_tokens": 13689,
          "cache_creation_input_tokens": 1926,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1926,
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

_source line 31 · 2026-05-29T05:31:57.210Z_

<details><summary>↩ Tool result · `toolu_01RCuts9h6ULukioi7dTGZMS`</summary>

```text
# PPCL (Prompt Perturbation Consistency Learning) Analysis

## Method Description
The paper describes PPCL as follows: During fine-tuning, researchers "feed both a clean utterance and its perturbed version (oronyms, synonyms, or paraphrases) and optimize the cross-entropy on each."

## Loss Function
PPCL employs a dual-component loss strategy. Beyond standard cross-entropy applied to both clean and perturbed inputs, the method incorporates "a Jensen-Shannon (JS) divergence term between their token-level output distributions," which the authors note "recovers much of the performance lost under prompt noise."

## Results and Performance
The paper indicates PPCL successfully mitigates performance degradation caused by prompt perturbations through its combined cross-entropy and divergence approach, though specific numerical improvements aren't detailed in the referenced section.

## Comparison Context
F2C differs fundamentally from PPCL in its approach: while PPCL requires gold labels during training (supervised), F2C operates entirely unsupervised using majority-vote pseudo-labels. Additionally, F2C's selective alignment toward confident variations contrasts with PPCL's uniform treatment of all perturbations.

## Key Reference
The paper cites: Qiang et al. (2024), "Prompt Perturbation Consistency Learning for Robust Language Models," in *Findings of EACL 2024*.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "de9d048d-04ce-4134-a133-87ca738770c1",
  "isSidechain": true,
  "promptId": "76f1366f-40a2-4dae-a639-d8c8a80dcb55",
  "agentId": "a905d999b9deee1fe",
  "type": "user",
  "uuid": "acb76045-273d-4d7b-886c-c564d727db5a",
  "sourceToolAssistantUUID": "de9d048d-04ce-4134-a133-87ca738770c1",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "5a7a1069-aaa7-4692-b429-b8501e411ab6",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 32 · 2026-05-29T05:32:01.549Z_

<details><summary>↩ Tool result · `toolu_01R6UCtGsM9N9BkyU4Uh1MrN`</summary>

```text
I appreciate your detailed request, but I must inform you that the provided content is a PDF file encoded in binary format (containing PDF stream objects, compression filters, and object references) rather than readable text content.

The material shows PDF structural elements like:
- Object streams (objects 402, 403)
- Compressed content streams with FlateDecode filters
- Font and graphics resource definitions
- Page structure metadata

**What I cannot do:**
Extract the technical details you've requested because the actual document text is not accessible in the provided format. The binary PDF encoding prevents me from reading the paper's content, equations, experimental results, hyperparameters, or dataset information.

**What you should do:**
1. Convert the PDF to text format using a PDF extraction tool
2. Provide the extracted text content directly
3. Re-submit your query with the readable text

Once you provide the actual document text, I can extract:
- Training objectives and loss formulas
- JS divergence equations
- Perturbation generation methods
- Experimental metrics with specific numbers
- Hyperparameter values (lambda, LLaMA sizes)
- Dataset names and configurations
- Ablation study results

I'm ready to help immediately upon receiving the readable content.

[Binary content (application/pdf, 346.8KB) also saved to /home/ubuntu/.claude-account-3/projects/-home-ubuntu-idea-adversarial/5a7a1069-aaa7-4692-b429-b8501e411ab6/tool-results/webfetch-1780032716143-vd2vfg.pdf]
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "b70ef08f-ec32-40d6-8d02-8ed6a98c57fc",
  "isSidechain": true,
  "promptId": "76f1366f-40a2-4dae-a639-d8c8a80dcb55",
  "agentId": "a905d999b9deee1fe",
  "type": "user",
  "uuid": "f9ca3574-298f-443e-b3f4-3e43d4d10b4f",
  "sourceToolAssistantUUID": "b70ef08f-ec32-40d6-8d02-8ed6a98c57fc",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "5a7a1069-aaa7-4692-b429-b8501e411ab6",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 33 · 2026-05-29T05:32:05.560Z_

Let me try to read the downloaded PDF and search for more specific technical details.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f9ca3574-298f-443e-b3f4-3e43d4d10b4f",
  "isSidechain": true,
  "agentId": "a905d999b9deee1fe",
  "requestId": "req_011CbWK6BJhfNQ6uU4sDED4M",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "96d474db-50b1-49ac-895b-51901e30fc5e",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "5a7a1069-aaa7-4692-b429-b8501e411ab6",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NfSgFv64Je4yEAjeojXqXH",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1160,
      "cache_read_input_tokens": 15615,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1160,
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

_source line 34 · 2026-05-29T05:32:06.502Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01SW3jdsHRtTqVQEe2pF5DA2`</summary>

```json
{
  "query": "PPCL \"Prompt Perturbation Consistency\" LLaMA MASSIVE SLURP dataset \"cross-entropy\" lambda oronym perturbation generation method"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "96d474db-50b1-49ac-895b-51901e30fc5e",
  "isSidechain": true,
  "agentId": "a905d999b9deee1fe",
  "requestId": "req_011CbWK6BJhfNQ6uU4sDED4M",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "00178d38-02d0-43fe-8413-4aebde374953",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "5a7a1069-aaa7-4692-b429-b8501e411ab6",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NfSgFv64Je4yEAjeojXqXH",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1160,
      "cache_read_input_tokens": 15615,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1160,
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

_source line 35 · 2026-05-29T05:32:07.527Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Kah7kWSdpf7c7VmzZvqx1L`</summary>

```json
{
  "query": "Qiang 2024 PPCL \"L_total\" OR \"total loss\" OR \"L_PPCL\" consistency regularization intent classification slot filling exact results"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "00178d38-02d0-43fe-8413-4aebde374953",
  "isSidechain": true,
  "agentId": "a905d999b9deee1fe",
  "requestId": "req_011CbWK6BJhfNQ6uU4sDED4M",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "9b6cdd86-0fde-4c33-9bd3-27961af07e16",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "5a7a1069-aaa7-4692-b429-b8501e411ab6",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NfSgFv64Je4yEAjeojXqXH",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1160,
      "cache_read_input_tokens": 15615,
      "output_tokens": 179,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1160
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 179,
          "cache_read_input_tokens": 15615,
          "cache_creation_input_tokens": 1160,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1160,
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

_source line 36 · 2026-05-29T05:32:13.400Z_

<details><summary>↩ Tool result · `toolu_01SW3jdsHRtTqVQEe2pF5DA2`</summary>

```text
Web search results for query: "PPCL "Prompt Perturbation Consistency" LLaMA MASSIVE SLURP dataset "cross-entropy" lambda oronym perturbation generation method"

Links: [{"title":"Prompt Perturbation Consistency Learning for Robust Language Models","url":"https://arxiv.org/pdf/2402.15833"},{"title":"Prompt Perturbation Experiments","url":"https://www.emergentmind.com/topics/prompt-perturbation-experiments"},{"title":"[Literature Review] Prompt Perturbation Consistency Learning for Robust Language Models","url":"https://www.themoonlight.io/en/review/prompt-perturbation-consistency-learning-for-robust-language-models"},{"title":"Prompt Perturbation Consistency Learning for Robust Language Models","url":"https://openreview.net/pdf/6531be6f8b4a39b29dc72a3ad3d4fd6eba931edb.pdf"},{"title":"Prompt perturbation consistency learning for robust language models - Amazon Science","url":"https://www.amazon.science/publications/prompt-perturbation-consistency-learning-for-robust-language-models"},{"title":"[2402.15833] Prompt Perturbation Consistency Learning for Robust Language Models","url":"https://arxiv.org/abs/2402.15833"},{"title":"Prompt Perturbation Consistency Learning for Robust Language Models - ACL Anthology","url":"https://aclanthology.org/2024.findings-eacl.91/"},{"title":"Flip-Flop Consistency: Unsupervised Training for Robustness to Prompt Perturbations in LLMs","url":"https://arxiv.org/pdf/2510.14242"},{"title":"Evaluating Robustness of Large Language Models in Enterprise Applications: Benchmarks for Perturbation Consistency Across Formats and Languages","url":"https://arxiv.org/html/2601.06341"}]

Based on the search results, I found information about PPCL and related research:

## PPCL (Prompt Perturbation Consistency Learning)

PPCL is an efficient mitigation approach that works by regularizing the divergence between losses from clean and perturbed samples. The paper addresses robustness of LLMs for intent classification and slot filling (IC-SF) tasks, and shows that fine-tuning sufficiently large LLMs can produce IC-SF performance comparable to discriminative models.

## Perturbation Types

The research systematically analyzes performance deterioration due to three distinct types of input perturbations - oronyms, synonyms, and paraphrasing.

## Datasets and Models

The paper evaluates results on the MASSIVE dataset, and uses LLaMA as the language model for experiments.

## Performance Results

PPCL recovers on average 59% and 69% of the performance drop for IC and SF tasks, respectively. PPCL beats the data augmentation approach while using ten times fewer augmented data samples.

The paper was published in the Findings of EACL 2024 and is available on arxiv as paper 2402.15833.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "00178d38-02d0-43fe-8413-4aebde374953",
  "isSidechain": true,
  "promptId": "76f1366f-40a2-4dae-a639-d8c8a80dcb55",
  "agentId": "a905d999b9deee1fe",
  "type": "user",
  "uuid": "1c7f32e4-aa36-4685-ad3e-c1febbaa1e20",
  "sourceToolAssistantUUID": "00178d38-02d0-43fe-8413-4aebde374953",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "5a7a1069-aaa7-4692-b429-b8501e411ab6",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 37 · 2026-05-29T05:32:13.660Z_

<details><summary>↩ Tool result · `toolu_01Kah7kWSdpf7c7VmzZvqx1L`</summary>

```text
Web search results for query: "Qiang 2024 PPCL "L_total" OR "total loss" OR "L_PPCL" consistency regularization intent classification slot filling exact results"

Links: [{"title":"Prompt Perturbation Consistency Learning for Robust Language Models - ACL Anthology","url":"https://aclanthology.org/2024.findings-eacl.91/"},{"title":"Prompt perturbation consistency learning for robust language models - Amazon Science","url":"https://www.amazon.science/publications/prompt-perturbation-consistency-learning-for-robust-language-models"},{"title":"Prompt Perturbation Consistency Learning for Robust Language Models","url":"https://arxiv.org/pdf/2402.15833"},{"title":"HIT-SCIR at MMNLU-22: Consistency Regularization for Multilingual Spoken   Language Understanding","url":"https://arxiv.org/pdf/2301.02010"},{"title":"[2301.02010] HIT-SCIR at MMNLU-22: Consistency Regularization for Multilingual Spoken Language Understanding","url":"https://arxiv.org/abs/2301.02010"},{"title":"Bi-directional Joint Neural Networks for Intent Classification and Slot   Filling","url":"https://arxiv.org/pdf/2202.13079"},{"title":"Joint Intent Detection And Slot Filling Based on Continual Learning   Model","url":"https://arxiv.org/pdf/2102.10905"},{"title":"An Explicit-Joint and Supervised-Contrastive Learning Framework for   Few-Shot Intent Classification and Slot Filling","url":"https://arxiv.org/pdf/2110.13691"}]

I found the research paper you're looking for. The paper is "Prompt Perturbation Consistency Learning for Robust Language Models" (PPCL), which works by regularizing the divergence between losses from clean and perturbed samples.

The experiments show that PPCL can recover on an average 59% and 69% of the performance drop for IC (intent classification) and SF (slot filling) tasks, respectively. Furthermore, PPCL beats data augmentation approach while using ten times fewer augmented data samples.

The paper was authored by Yao Qiang and colleagues and published in the Findings of the Association for Computational Linguistics: EACL 2024. The full paper is available on the ACL Anthology and ArXiv (arxiv.org/pdf/2402.15833).

Regarding the specific notation you mentioned ("L_total", "L_PPCL", etc.), I would need to access the full paper's mathematical formulations to provide exact details about these loss function definitions. The search results show the general approach but don't contain the specific loss function equations.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "9b6cdd86-0fde-4c33-9bd3-27961af07e16",
  "isSidechain": true,
  "promptId": "76f1366f-40a2-4dae-a639-d8c8a80dcb55",
  "agentId": "a905d999b9deee1fe",
  "type": "user",
  "uuid": "7a3ecdaf-4582-4712-a8e1-e3d1da12cd0e",
  "sourceToolAssistantUUID": "9b6cdd86-0fde-4c33-9bd3-27961af07e16",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "5a7a1069-aaa7-4692-b429-b8501e411ab6",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 38 · 2026-05-29T05:32:17.365Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01AzooVFPAwtQYr6iYFXaYPj`</summary>

```json
{
  "url": "https://www.emergentmind.com/papers/2402.15833",
  "prompt": "Extract ALL technical details about the PPCL paper: loss function formulas, training objective, perturbation generation methods, datasets, models, hyperparameters, and quantitative results. Include any equations, tables, or specific numbers mentioned."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7a3ecdaf-4582-4712-a8e1-e3d1da12cd0e",
  "isSidechain": true,
  "agentId": "a905d999b9deee1fe",
  "requestId": "req_011CbWK74yyZEHk7SaNqHsqU",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "454ea25e-2c54-462b-8c2d-5e847b4159c9",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "5a7a1069-aaa7-4692-b429-b8501e411ab6",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01ChoP5cQDz8M8rWnQBijgFg",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1681,
      "cache_read_input_tokens": 16775,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1681,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 37,
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

_source line 39 · 2026-05-29T05:32:21.001Z_

<details open><summary>🔧 Tool call — Read · `toolu_01CLjPRpHfUUWq81Fg6U1uj3`</summary>

```json
{
  "file_path": "/home/ubuntu/.claude-account-3/projects/-home-ubuntu-idea-adversarial/5a7a1069-aaa7-4692-b429-b8501e411ab6/tool-results/webfetch-1780032716143-vd2vfg.pdf",
  "pages": "1-10"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "454ea25e-2c54-462b-8c2d-5e847b4159c9",
  "isSidechain": true,
  "agentId": "a905d999b9deee1fe",
  "requestId": "req_011CbWK74yyZEHk7SaNqHsqU",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "47fde2e7-9596-485d-8f70-be4a0ce3b2d3",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "5a7a1069-aaa7-4692-b429-b8501e411ab6",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01ChoP5cQDz8M8rWnQBijgFg",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1681,
      "cache_read_input_tokens": 16775,
      "output_tokens": 260,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1681
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 260,
          "cache_read_input_tokens": 16775,
          "cache_creation_input_tokens": 1681,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1681,
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

_source line 40 · 2026-05-29T05:32:22.358Z_

<details><summary>↩ Tool result · `toolu_01CLjPRpHfUUWq81Fg6U1uj3`</summary>

```text
PDF pages extracted: 10 page(s) from /home/ubuntu/.claude-account-3/projects/-home-ubuntu-idea-adversarial/5a7a1069-aaa7-4692-b429-b8501e411ab6/tool-results/webfetch-1780032716143-vd2vfg.pdf (346.8KB)
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "47fde2e7-9596-485d-8f70-be4a0ce3b2d3",
  "isSidechain": true,
  "promptId": "76f1366f-40a2-4dae-a639-d8c8a80dcb55",
  "agentId": "a905d999b9deee1fe",
  "type": "user",
  "uuid": "59388a43-816a-4da8-93af-570962d4e980",
  "sourceToolAssistantUUID": "47fde2e7-9596-485d-8f70-be4a0ce3b2d3",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "5a7a1069-aaa7-4692-b429-b8501e411ab6",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

## Round 2

3 recorded events

### User

_source line 41 · 2026-05-29T05:32:22.353Z_

```json
{
  "type": "image",
  "source": {
    "type": "base64",
    "media_type": "image/jpeg",
    "data": "[ATTACHMENT_DATA_REDACTED]"
  }
}
```

```json
{
  "type": "image",
  "source": {
    "type": "base64",
    "media_type": "image/jpeg",
    "data": "[ATTACHMENT_DATA_REDACTED]"
  }
}
```

```json
{
  "type": "image",
  "source": {
    "type": "base64",
    "media_type": "image/jpeg",
    "data": "[ATTACHMENT_DATA_REDACTED]"
  }
}
```

```json
{
  "type": "image",
  "source": {
    "type": "base64",
    "media_type": "image/jpeg",
    "data": "[ATTACHMENT_DATA_REDACTED]"
  }
}
```

```json
{
  "type": "image",
  "source": {
    "type": "base64",
    "media_type": "image/jpeg",
    "data": "[ATTACHMENT_DATA_REDACTED]"
  }
}
```

```json
{
  "type": "image",
  "source": {
    "type": "base64",
    "media_type": "image/jpeg",
    "data": "[ATTACHMENT_DATA_REDACTED]"
  }
}
```

```json
{
  "type": "image",
  "source": {
    "type": "base64",
    "media_type": "image/jpeg",
    "data": "[ATTACHMENT_DATA_REDACTED]"
  }
}
```

```json
{
  "type": "image",
  "source": {
    "type": "base64",
    "media_type": "image/jpeg",
    "data": "[ATTACHMENT_DATA_REDACTED]"
  }
}
```

```json
{
  "type": "image",
  "source": {
    "type": "base64",
    "media_type": "image/jpeg",
    "data": "[ATTACHMENT_DATA_REDACTED]"
  }
}
```

```json
{
  "type": "image",
  "source": {
    "type": "base64",
    "media_type": "image/jpeg",
    "data": "[ATTACHMENT_DATA_REDACTED]"
  }
}
```

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "59388a43-816a-4da8-93af-570962d4e980",
  "isSidechain": true,
  "promptId": "76f1366f-40a2-4dae-a639-d8c8a80dcb55",
  "agentId": "a905d999b9deee1fe",
  "type": "user",
  "isMeta": true,
  "uuid": "d8f708d5-4af5-49f2-9bd3-6d2279af1914",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "5a7a1069-aaa7-4692-b429-b8501e411ab6",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 42 · 2026-05-29T05:32:23.162Z_

<details><summary>↩ Tool result · `toolu_01AzooVFPAwtQYr6iYFXaYPj`</summary>

```text
# Technical Details from PPCL Paper

Based on the provided webpage content, I can only extract limited technical information, as the page primarily displays metadata and navigation elements rather than the full paper content.

## Available Information:

**Core Contribution:**
The paper proposes "Prompt Perturbation Consistency Learning (PPCL)," which the authors describe as "regularizing the divergence between losses from clean and perturbed samples."

**Perturbation Types Studied:**
Three distinct input perturbation categories were analyzed:
- Oronyms
- Synonyms  
- Paraphrasing

**Performance Results:**
- PPCL recovered approximately 59% of performance drop for intent classification (IC) tasks
- PPCL recovered approximately 69% of performance drop for slot filling (SF) tasks
- The method outperformed data augmentation while using "ten times fewer augmented data samples"

**Task Focus:**
The research concentrated on sequence labeling tasks: intent classification and slot filling (IC-SF), which are "central component[s] in personal assistant systems."

## Limitation:

The webpage excerpt does not contain the actual mathematical formulas, detailed hyperparameters, specific dataset names, model architectures, or complete experimental tables. To access these technical specifics, consulting the full PDF or HTML version of arxiv paper 2402.15833 would be necessary.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "454ea25e-2c54-462b-8c2d-5e847b4159c9",
  "isSidechain": true,
  "promptId": "76f1366f-40a2-4dae-a639-d8c8a80dcb55",
  "agentId": "a905d999b9deee1fe",
  "type": "user",
  "uuid": "f492c46d-84b0-40dc-95e8-99594d8b1d38",
  "sourceToolAssistantUUID": "454ea25e-2c54-462b-8c2d-5e847b4159c9",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "5a7a1069-aaa7-4692-b429-b8501e411ab6",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 43 · 2026-05-29T05:33:16.583Z_

Now I have the full paper content from the PDF images. Let me compile the detailed summary.

---

## Prompt Perturbation Consistency Learning (PPCL) for Robust Language Models — Detailed Summary

**Paper:** Qiang et al., Findings of EACL 2024 (pp. 1357-1370). Authors: Yao Qiang, Subhrangshu Nandi, Ninareh Mehrabi, Greg Ver Steeg, Anoop Kumar, Anna Rumshisky, Aram Galstyan.

### Problem and Gap Identified

The paper addresses two intersecting gaps. First, LLMs underperform SOTA discriminative models (e.g., JointBERT, JointBERT+CRF) on structured prediction tasks — specifically intent classification (IC) and slot filling (SF), which are central to voice-based personal assistants. Second, there is a lack of substantive research on the robustness of LLMs to realistic input perturbations in these tasks. The authors quantify this vulnerability: on the MASSIVE dataset, LLaMA-7b+SFT suffers an average performance drop rate (PDR) of 16.67% on IC accuracy and 40.75% on SF F1-score for oronym perturbations, with comparable drops for synonyms and paraphrases. Across models, the average performance drop is 13.07% in IC accuracy and 22.20% in SF F1-score. These perturbations are realistic — they arise from ASR errors (oronyms), linguistic variation (synonyms), and natural rephrasing (paraphrases).

### Key Insight: Consistency Regularization

Standard data augmentation expands the training set with perturbed examples but treats each augmented sample independently, overlooking the semantic equivalence between original and perturbed inputs. PPCL's core insight is that augmented data should not just add volume — it should explicitly enforce that the model produces consistent output distributions for semantically equivalent inputs. By adding a regularization term that penalizes divergence between the output distributions on clean versus perturbed inputs, PPCL extracts far more signal from each perturbed example than naive augmentation does.

### Technical Method

**Perturbation Generation.** Three types are used: (1) **Oronyms** — phonetically similar word substitutions (e.g., "give me more light" becomes "give mi moore light"); (2) **Synonyms** — meaning-preserving word replacements (e.g., "decrease" becomes "minify"); (3) **Paraphrases** — sentence-level rephrasing preserving meaning. All generated perturbations are filtered using BERTScore with a threshold of 0.85 to ensure semantic equivalence.

**Loss Function — Jensen-Shannon Divergence.** During fine-tuning, both a clean utterance x_c and its perturbed counterpart x_p are fed simultaneously to the LLM. For the j-th output token, the model produces logits p_c^j and p_p^j over the vocabulary V (where p_c^j, p_p^j are in R^|V|). After applying softmax to obtain probability distributions y-hat_c^j = Softmax(p_c^j) and y-hat_p^j = Softmax(p_p^j), the JS divergence is computed:

**JS(P || Q) = (1/2)(KL(P || M) + KL(Q || M))**, where M = (1/2)(P + Q).

JS is chosen over KL for its symmetry, providing a more balanced similarity measure. The perturbation consistency loss averages JS divergence across all L output tokens:

**L_JS = (1/L) * sum_{j=1}^{L} JS(y-hat_c^j || y-hat_p^j)** (Eq. 2)

For paraphrasing perturbations, which may alter sequence length, the authors use averaged probability distributions instead of token-by-token alignment: **L_JS = JS(y-bar_c || y-bar_p)** (Eq. 3).

**Full Training Objective.** The total loss combines supervised cross-entropy on both clean and perturbed samples with the consistency term:

- L_C = CE(y-hat_c, y) — cross-entropy on clean input
- L_P = CE(y-hat_p, y) — cross-entropy on perturbed input
- **L = lambda_1 * L_C + lambda_2 * L_P + lambda_3 * L_JS** (Eq. 6)

where lambda_1, lambda_2, lambda_3 are weight coefficients.

### Experimental Setup

**Datasets:** ATIS, SNIPS, and MASSIVE (three NLU benchmarks). **Models:** GPT-2, LLaMA-7b, LLaMA-13b, LLaMA-30b, with instruction fine-tuning using sentinel-based structured prompt formats. **Baselines:** JointBERT, JointBERT+CRF, GPT-3.5 (zero-shot and few-shot). **Metric:** Performance Drop Rate (PDR) = 1 - (sum of metric on perturbed set / sum of metric on clean set).

### Quantitative Results (Table 4, MASSIVE dataset, LLaMA-7b)

**Oronym perturbation:** Baseline IC-PDR = 16.67%, SF-PDR = 40.75%. PPCL (L_C + L_P + L_JS with +3k augmentation) reduces to IC-PDR = 8.74 (47% recovery) and SF-PDR = 15.41 (62% recovery). Compare: pure augmentation with +50k samples achieves IC-PDR = 9.02 (45% recovery) and SF-PDR = 19.73 (51% recovery).

**Synonym perturbation:** Baseline IC-PDR = 13.94%, SF-PDR = 9.72%. PPCL (+5k) achieves IC-PDR = 3.74 (73% recovery) and SF-PDR = 1.44 (85% recovery). Pure augmentation at +50k achieves IC-PDR = 4.01 (71% recovery) and SF-PDR = 4.49 (53% recovery).

**Paraphrase perturbation:** Baseline IC-PDR = 8.62%, SF-PDR = 16.14%. PPCL (+6k) achieves IC-PDR = 3.69 (57% recovery) and SF-PDR = 6.36 (60% recovery). Pure augmentation at +50k achieves IC-PDR = 3.69 (57% recovery) and SF-PDR = 4.24 (74% recovery).

**Average across perturbation types:** PPCL recovers 59% of IC performance drop and 69% of SF performance drop. Multi-sample augmentation (+50k) recovers 58% IC and 59% SF — but uses roughly 10x more data.

### The 10x Data Efficiency Claim

This is the paper's most striking finding. PPCL with only 1 perturbed sample per clean example (+3k to +6k additional samples) outperforms or matches data augmentation using 5 perturbed samples per clean example (+50k samples) in 5 out of 6 task/perturbation combinations. The sole exception is SF under paraphrase perturbation, where multi-sample augmentation at +50k achieves 74% recovery vs. PPCL's 60%. The efficiency gain comes from the JS consistency term extracting alignment signal that raw augmentation misses.

### Ablation Study (Table 4)

Removing any of the three loss components degrades performance: using only L_C + L_JS (no perturbed cross-entropy) recovers less than the full objective; using only L_C + L_P (no JS term) is equivalent to standard augmentation and consistently underperforms the full PPCL objective. All three terms are necessary: L_C grounds the clean performance, L_P teaches the model from perturbed inputs, and L_JS enforces output distribution alignment.

### Limitations

The authors note PPCL was evaluated only on IC-SF tasks across small public datasets (MASSIVE, ATIS, SNIPS), and real-world datasets with different noise distributions might yield different results. They also note that paraphrase perturbation is the hardest case for PPCL due to length mismatches requiring averaged distributions rather than token-level alignment.

Sources:
- [ACL Anthology](https://aclanthology.org/2024.findings-eacl.91/)
- [arXiv Abstract](https://arxiv.org/abs/2402.15833)
- [Amazon Science](https://www.amazon.science/publications/prompt-perturbation-consistency-learning-for-robust-language-models)
- [Emergent Mind](https://www.emergentmind.com/topics/prompt-perturbation-experiments)
- [Moonlight Literature Review](https://www.themoonlight.io/en/review/prompt-perturbation-consistency-learning-for-robust-language-models)
- [Flip-Flop Consistency (citing PPCL)](https://arxiv.org/html/2510.14242v1)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f492c46d-84b0-40dc-95e8-99594d8b1d38",
  "isSidechain": true,
  "agentId": "a905d999b9deee1fe",
  "requestId": "req_011CbWK7moe9Qf9o3qXDwq1Q",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "3e1e83d3-c401-40d6-9c3b-01148dc252bd",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "5a7a1069-aaa7-4692-b429-b8501e411ab6",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KvnjTur6J5tQrATGqYCpXd",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 13346,
      "cache_read_input_tokens": 18456,
      "output_tokens": 2231,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 13346
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 2231,
          "cache_read_input_tokens": 18456,
          "cache_creation_input_tokens": 13346,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 13346,
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
