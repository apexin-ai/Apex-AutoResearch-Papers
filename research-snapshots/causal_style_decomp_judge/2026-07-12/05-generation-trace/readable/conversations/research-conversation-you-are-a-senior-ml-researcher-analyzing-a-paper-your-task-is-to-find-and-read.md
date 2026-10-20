# Research conversation: You are a senior ML researcher analyzing a paper. Your task is to find and read the paper "A Theoretical Analysis of Com

**The Likert Blindspot: Measurement-Mode Divergence in LLM Judge Style Evaluation (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 34
- **Recorded user turns:** 1
- **Tool calls:** 13
- **Original source:** `logs/chats/exported-trajectories/account-3/agent-ac264cfb0150d4e15.jsonl`
- **Structured JSON:** [`90e0b1c119400aacaad7.json`](../../sessions/90/90e0b1c119400aacaad7.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

34 recorded events

### User

_source line 1 · 2026-05-29T05:31:46.558Z_

You are a senior ML researcher analyzing a paper. Your task is to find and read the paper "A Theoretical Analysis of Compositional Generalization in Neural Networks: A Necessary and Sufficient Condition" by Li, arXiv 2025, available at https://arxiv.org/abs/2505.02627.

Steps:
1. Use WebFetch to read the arxiv abstract page.
2. Use WebFetch to read the HTML version at https://arxiv.org/html/2505.02627 to get method details.
3. Search for any reviews or discussions of this paper.

Then provide a detailed analysis covering:
- What gap did they identify and HOW?
- What was the key insight others missed?
- How did they formulate the problem differently?
- What existing technique did they adapt/combine/simplify?
- The formal necessary and sufficient condition they derive
- How computational graph alignment relates to compositional structure
- What "minimal sufficient information" means in their framework
- Implications for skill-graph-guided training data synthesis

Be thorough and precise. Report all findings in detail.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "d4a73727-8220-46d8-98b1-d049e20c8ef5",
  "agentId": "ac264cfb0150d4e15",
  "type": "user",
  "uuid": "3542d1ba-e960-4380-844d-f6e250c86a62",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "bd21c8ef-b139-4bde-afcd-7b4dbdab2a90",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 2 · 2026-05-29T05:31:46.564Z_

```json
{
  "parentUuid": "3542d1ba-e960-4380-844d-f6e250c86a62",
  "isSidechain": true,
  "agentId": "ac264cfb0150d4e15",
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
  "uuid": "727a115b-9dc4-4895-b57a-17f0d345f9a0",
  "timestamp": "2026-05-29T05:31:46.564Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "bd21c8ef-b139-4bde-afcd-7b4dbdab2a90",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 3 · 2026-05-29T05:31:46.565Z_

```json
{
  "parentUuid": "727a115b-9dc4-4895-b57a-17f0d345f9a0",
  "isSidechain": true,
  "agentId": "ac264cfb0150d4e15",
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "86320f88-a4e2-4c97-9645-26d11b85a2cd",
  "timestamp": "2026-05-29T05:31:46.565Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "bd21c8ef-b139-4bde-afcd-7b4dbdab2a90",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Assistant

_source line 4 · 2026-05-29T05:31:48.772Z_



I'll start by fetching the tool schemas and then retrieving the paper information.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "86320f88-a4e2-4c97-9645-26d11b85a2cd",
  "isSidechain": true,
  "agentId": "ac264cfb0150d4e15",
  "requestId": "req_011CbWK55BphbYfBEjGYVSds",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "5fe179af-51fb-4466-9e7b-2aa23be2a5a0",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "bd21c8ef-b139-4bde-afcd-7b4dbdab2a90",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017w5wSNq1BnFm9gxBYxBd3n",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1577,
      "cache_read_input_tokens": 7413,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1577,
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

_source line 5 · 2026-05-29T05:31:49.337Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01ULNP29k9HUqFo1v72ywbHH`</summary>

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
  "parentUuid": "5fe179af-51fb-4466-9e7b-2aa23be2a5a0",
  "isSidechain": true,
  "agentId": "ac264cfb0150d4e15",
  "requestId": "req_011CbWK55BphbYfBEjGYVSds",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "d59e1b27-8894-44fb-b798-2b3cf9d4d5d9",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "bd21c8ef-b139-4bde-afcd-7b4dbdab2a90",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017w5wSNq1BnFm9gxBYxBd3n",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1577,
      "cache_read_input_tokens": 7413,
      "output_tokens": 98,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1577
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 98,
          "cache_read_input_tokens": 7413,
          "cache_creation_input_tokens": 1577,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1577,
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

_source line 6 · 2026-05-29T05:31:49.346Z_

<details><summary>↩ Tool result · `toolu_01ULNP29k9HUqFo1v72ywbHH`</summary>

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
  "parentUuid": "d59e1b27-8894-44fb-b798-2b3cf9d4d5d9",
  "isSidechain": true,
  "promptId": "d4a73727-8220-46d8-98b1-d049e20c8ef5",
  "agentId": "ac264cfb0150d4e15",
  "type": "user",
  "uuid": "b5ccba2a-6689-416d-9682-a88e8412370e",
  "sourceToolAssistantUUID": "d59e1b27-8894-44fb-b798-2b3cf9d4d5d9",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "bd21c8ef-b139-4bde-afcd-7b4dbdab2a90",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 7 · 2026-05-29T05:31:51.761Z_



Now let me fetch the paper information from multiple sources in parallel.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b5ccba2a-6689-416d-9682-a88e8412370e",
  "isSidechain": true,
  "agentId": "ac264cfb0150d4e15",
  "requestId": "req_011CbWK5HdBhGbHtjf4rWTvq",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "5c56d52d-93b0-45d2-85cf-1e7b88e969a7",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "bd21c8ef-b139-4bde-afcd-7b4dbdab2a90",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EaPbthghSTMjk9XtEZ5gPh",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1120,
      "cache_read_input_tokens": 8990,
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

_source line 8 · 2026-05-29T05:31:53.145Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01GZqc5XUH9wJmFTvvH27Ruk`</summary>

```json
{
  "url": "https://arxiv.org/abs/2505.02627",
  "prompt": "Extract the full abstract, title, authors, and all metadata from this arxiv paper page. Include every detail available."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5c56d52d-93b0-45d2-85cf-1e7b88e969a7",
  "isSidechain": true,
  "agentId": "ac264cfb0150d4e15",
  "requestId": "req_011CbWK5HdBhGbHtjf4rWTvq",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "ea96889a-d440-481f-b421-a7a065f2902a",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "bd21c8ef-b139-4bde-afcd-7b4dbdab2a90",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EaPbthghSTMjk9XtEZ5gPh",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1120,
      "cache_read_input_tokens": 8990,
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

_source line 9 · 2026-05-29T05:31:57.022Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01RwHQGZZwVs5QEnQYQGYtuq`</summary>

```json
{
  "url": "https://arxiv.org/html/2505.02627",
  "prompt": "Extract the FULL content of this paper in as much detail as possible. Include: all section headings, the complete introduction, all definitions, theorems, lemmas, proofs, the problem formulation, the methodology, the formal conditions they derive, how they define compositional generalization, computational graph alignment, minimal sufficient information, all experimental details, and the conclusion. Be as thorough and detailed as possible - capture every key equation, definition, and result."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ea96889a-d440-481f-b421-a7a065f2902a",
  "isSidechain": true,
  "agentId": "ac264cfb0150d4e15",
  "requestId": "req_011CbWK5HdBhGbHtjf4rWTvq",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "59fc37f7-b6c2-44b2-9f2c-cfcb4023aa55",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "bd21c8ef-b139-4bde-afcd-7b4dbdab2a90",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EaPbthghSTMjk9XtEZ5gPh",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1120,
      "cache_read_input_tokens": 8990,
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

_source line 10 · 2026-05-29T05:31:57.604Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01NFrQW77c5kZGaqe3mToFrJ`</summary>

```json
{
  "query": "\"A Theoretical Analysis of Compositional Generalization in Neural Networks\" Li 2025 arXiv 2505.02627 review discussion"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "59fc37f7-b6c2-44b2-9f2c-cfcb4023aa55",
  "isSidechain": true,
  "agentId": "ac264cfb0150d4e15",
  "requestId": "req_011CbWK5HdBhGbHtjf4rWTvq",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "a4bebdc5-0eb0-42c8-b143-ada816de2e79",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "bd21c8ef-b139-4bde-afcd-7b4dbdab2a90",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EaPbthghSTMjk9XtEZ5gPh",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1120,
      "cache_read_input_tokens": 8990,
      "output_tokens": 346,
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
          "output_tokens": 346,
          "cache_read_input_tokens": 8990,
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

_source line 11 · 2026-05-29T05:31:57.965Z_

<details><summary>↩ Tool result · `toolu_01GZqc5XUH9wJmFTvvH27Ruk`</summary>

```text
# ArXiv Paper Metadata Extraction

**Title:** "A Theoretical Analysis of Compositional Generalization in Neural Networks: A Necessary and Sufficient Condition"

**Author:** Yuanpeng Li

**ArXiv Identifier:** 2505.02627

**Submission Date:** May 5, 2025

**Category:** Computer Science > Machine Learning (cs.LG); Artificial Intelligence (cs.AI)

**DOI:** https://doi.org/10.48550/arXiv.2505.02627

**License:** Creative Commons Attribution 4.0 (CC BY 4.0)

## Abstract

The paper examines compositional generalization—a key capability enabling AI systems to manage novel combinations of familiar components. While most deep learning models struggle with this, some succeed in specific contexts, suggesting underlying principles exist. The research establishes mathematical conditions that are both necessary and sufficient for this property.

The core requirement has two parts: "(i) the computational graph matches the true compositional structure, and (ii) components encode just enough information in training." The authors provide formal proofs alongside a minimal worked example for intuitive understanding. The framework integrates architectural design, regularization techniques, and training data characteristics. The study also explores assessing this capability before model training.

**Access:** PDF and HTML versions available; TeX source included
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ea96889a-d440-481f-b421-a7a065f2902a",
  "isSidechain": true,
  "promptId": "d4a73727-8220-46d8-98b1-d049e20c8ef5",
  "agentId": "ac264cfb0150d4e15",
  "type": "user",
  "uuid": "c1f33527-3635-4598-a9aa-c26a46fd2e4e",
  "sourceToolAssistantUUID": "ea96889a-d440-481f-b421-a7a065f2902a",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "bd21c8ef-b139-4bde-afcd-7b4dbdab2a90",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-29T05:32:04.714Z_

<details><summary>↩ Tool result · `toolu_01NFrQW77c5kZGaqe3mToFrJ`</summary>

```text
Web search results for query: ""A Theoretical Analysis of Compositional Generalization in Neural Networks" Li 2025 arXiv 2505.02627 review discussion"

Links: [{"title":"[2505.02627] A Theoretical Analysis of Compositional Generalization in Neural Networks: A Necessary and Sufficient Condition","url":"https://arxiv.org/abs/2505.02627"},{"title":"A Theoretical Analysis of Compositional Generalization in Neural Networks: A Necessary and Sufficient Condition","url":"https://arxiv.org/html/2505.02627v1"},{"title":"arXiv:2505.02627v1 [cs.LG] 5 May 2025","url":"https://arxiv.org/pdf/2505.02627"},{"title":"A General Theory for Compositional Generalization","url":"https://arxiv.org/pdf/2405.11743"},{"title":"Swing-by Dynamics in Concept Learning and Compositional Generalization","url":"https://arxiv.org/pdf/2410.08309"},{"title":"Compositional Generalization for Primitive Substitutions","url":"https://arxiv.org/pdf/1910.02612"}]

Based on the search results, I found information about the paper you're inquiring about:

## Overview

The paper derives a necessary and sufficient condition for compositional generalization in neural networks. Conceptually, it requires that (i) the computational graph matches the true compositional structure, and (ii) components encode just enough information in training.

## Context and Motivation

Compositional generalization is a crucial property in artificial intelligence, enabling models to handle novel combinations of known components. While most deep learning models lack this capability, certain models succeed in specific tasks, suggesting the existence of governing conditions.

## Related Work

The paper situates itself within recent theoretical research on this topic. Jarvis et al. (2023) demonstrated that modular architectures alone cannot guarantee compositional generalization without aligned dataset structures, emphasizing the critical role of training dynamics and low-rank substructures in compositional learning. Additionally, Lippl and Stachenfeld (2025) proposed a kernel theory revealing fundamental limitations of compositional models, showing they are constrained to "conjunction-wise additive" computations that prevent transitive generalization.

## Key Contributions

The condition is supported by mathematical proofs. This criterion combines aspects of architecture design, regularization, and training data properties. The authors also discuss the potential of the condition for assessing compositional generalization before training.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a4bebdc5-0eb0-42c8-b143-ada816de2e79",
  "isSidechain": true,
  "promptId": "d4a73727-8220-46d8-98b1-d049e20c8ef5",
  "agentId": "ac264cfb0150d4e15",
  "type": "user",
  "uuid": "0152f1eb-1605-4205-824d-8fdcc62f8a9c",
  "sourceToolAssistantUUID": "a4bebdc5-0eb0-42c8-b143-ada816de2e79",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "bd21c8ef-b139-4bde-afcd-7b4dbdab2a90",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 13 · 2026-05-29T05:32:13.928Z_

<details><summary>↩ Tool result · `toolu_01RwHQGZZwVs5QEnQYQGYtuq`</summary>

```text
# Comprehensive Summary: Compositional Generalization in Neural Networks

## Core Contribution

This paper establishes a necessary and sufficient condition for compositional generalization in neural networks: "A model enables compositional generalization if and only if it has structural alignment, unambiguous representation, and minimized representation."

## Key Definitions

**Compositional Generalization (Definition 5):** If a model correctly predicts all training samples, it must also predict all test samples accurately, enabling models to handle novel combinations of known components.

**Structural Alignment (Definition 6):** The hypothesis graph set's structure matches an existing reference graph set—the computational architecture mirrors the true compositional hierarchy.

**Unambiguous Representation (Definition 7):** For training data, if two samples share identical hypothesis values at a node, they must have identical reference values there, ensuring well-defined mappings.

**Minimized Representation (Definition 8):** Each component produces the minimal number of distinct training outputs, preventing redundant information encoding while avoiding excessive compression.

## Computational Graph Framework

**Component (Definition 1):** A deterministic function mapping input node sequences to single output nodes. Neural network modules without parameter sharing qualify as components.

**Computational Graph (Definition 2):** A directed acyclic graph connecting components, transforming sample inputs into outputs. Graphs are not provided directly in data.

**Reference Graph Set (Definition 4):** A graph set where all predictions are correct and all test component inputs appear in training data. This ensures test samples can compositionally combine seen elements.

## Mathematical Foundations

**Lemma 1 (Mappings on Nodes):** A well-defined onto mapping between finite sets becomes bijective if and only if the domain contains no redundant elements—connecting minimized representation to one-to-one mappings.

**Lemma 2 (Induction Step):** Structural alignment plus one-to-one mappings on training data enable correct predictions for test samples when test component inputs have been observed during training.

**Proposition 1 (Necessity):** Compositional generalization requires all three conditions. Under Assumption 1 (test component inputs are seen in training), these conditions become necessary.

**Proposition 2 (Sufficiency):** All three conditions together enable compositional generalization through mathematical induction over graph structure.

## Necessity Assumption

"A model enables compositional generalization only if test component inputs are seen in training." This reflects how gradient-based optimization compresses representations at early layers, making unseen component inputs unavailable for later compositional processing.

## Minimal Example

The paper illustrates these abstract concepts through a concrete XOR-based task:
- **Function:** y = (x₁ ⊕ x₂) ⊕ x₃
- **Training data:** Six samples covering all necessary component input combinations
- **Test data:** Two novel input combinations requiring compositional generalization

A carefully designed model with modular structure, regularization, and appropriate training data achieves perfect test accuracy, while standard fully-connected networks fail completely. Ablation studies confirm each condition is essential.

## Practical Implementation

**Regularization (Section 5.2):** Apply Gaussian noise plus power constraints to hidden layers, reducing distinct component outputs:
- h' = h + 𝒩(0,α)
- ℒ' = ℒ + β||h||²

**Structural Alignment:** Architectural design encoding known compositional hierarchies through modular networks.

**Unambiguous Representation:** Data validation ensuring no training ambiguities exist before training begins.

## Alternative Formulation

The authors provide Theorem 2, an alternative formulation incorporating the necessity assumption into the definition itself, making the condition sufficient without requiring Assumption 1 as external justification.

## Discussion Topics

- **Attention Mechanisms:** Effectively equal representations under permutation satisfy the conditions
- **Representation Compression:** Neural networks naturally compress intermediate representations during training
- **Assessability Before Training:** Conditions guide architecture and data design decisions pre-training
- **One-to-One Mapping:** Equivalent to combining unambiguous and minimized representation conditions

## Related Work Context

The paper positions itself among recent theoretical work investigating compositional generalization through kernel theory, identifiable representations, and neuro-symbolic formalisms, while addressing limitations identified in prior work on modular architectures and distributed representations.

## Significance

This establishes compositional generalization as requiring interacting constraints across architecture, regularization, and data properties—no single factor suffices independently. The mathematical framework provides theoretical grounding for why most deep learning models fail at compositional tasks while certain carefully designed systems succeed.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "59fc37f7-b6c2-44b2-9f2c-cfcb4023aa55",
  "isSidechain": true,
  "promptId": "d4a73727-8220-46d8-98b1-d049e20c8ef5",
  "agentId": "ac264cfb0150d4e15",
  "type": "user",
  "uuid": "f223c9b6-5656-4834-adec-9379877be98d",
  "sourceToolAssistantUUID": "59fc37f7-b6c2-44b2-9f2c-cfcb4023aa55",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "bd21c8ef-b139-4bde-afcd-7b4dbdab2a90",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 14 · 2026-05-29T05:32:17.080Z_

Let me search for more discussions and reviews of this paper, and also try to get more detailed content from the HTML version.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f223c9b6-5656-4834-adec-9379877be98d",
  "isSidechain": true,
  "agentId": "ac264cfb0150d4e15",
  "requestId": "req_011CbWK76CenFaTtZtjmNr1N",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "b7b08fb1-f0c8-4211-a095-ec59c8f0e3fd",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "bd21c8ef-b139-4bde-afcd-7b4dbdab2a90",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AJRMrtGSu3PwPabUEXEvaW",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 632,
      "cache_creation_input_tokens": 1738,
      "cache_read_input_tokens": 10110,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1738,
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

_source line 15 · 2026-05-29T05:32:17.677Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01KCRvAwQSFwbLEsmr913XLZ`</summary>

```json
{
  "query": "Yuanpeng Li compositional generalization necessary sufficient condition neural networks 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b7b08fb1-f0c8-4211-a095-ec59c8f0e3fd",
  "isSidechain": true,
  "agentId": "ac264cfb0150d4e15",
  "requestId": "req_011CbWK76CenFaTtZtjmNr1N",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "7dd0dc0c-3efd-4ed3-9c0e-51bcaa084542",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "bd21c8ef-b139-4bde-afcd-7b4dbdab2a90",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AJRMrtGSu3PwPabUEXEvaW",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 632,
      "cache_creation_input_tokens": 1738,
      "cache_read_input_tokens": 10110,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1738,
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

_source line 16 · 2026-05-29T05:32:18.146Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01VkaARYuTc5PjKBtcEAMx1i`</summary>

```json
{
  "query": "compositional generalization computational graph alignment minimal sufficient information theory 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7dd0dc0c-3efd-4ed3-9c0e-51bcaa084542",
  "isSidechain": true,
  "agentId": "ac264cfb0150d4e15",
  "requestId": "req_011CbWK76CenFaTtZtjmNr1N",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "fcb88ff9-a7f8-458e-9efe-bb26ecfb2ebb",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "bd21c8ef-b139-4bde-afcd-7b4dbdab2a90",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AJRMrtGSu3PwPabUEXEvaW",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 632,
      "cache_creation_input_tokens": 1738,
      "cache_read_input_tokens": 10110,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1738,
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

### Tool result

_source line 17 · 2026-05-29T05:32:23.442Z_

<details><summary>↩ Tool result · `toolu_01KCRvAwQSFwbLEsmr913XLZ`</summary>

```text
Web search results for query: "Yuanpeng Li compositional generalization necessary sufficient condition neural networks 2025"

Links: [{"title":"[2505.02627] A Theoretical Analysis of Compositional Generalization in Neural Networks: A Necessary and Sufficient Condition","url":"https://arxiv.org/abs/2505.02627"},{"title":"Artificial Intelligence May 2025","url":"https://arxiv.org/list/cs.AI/2025-05?skip=1175&show=50"},{"title":"arXiv:2505.02627v1 [cs.LG] 5 May 2025","url":"https://arxiv.org/pdf/2505.02627"},{"title":"A Theoretical Analysis of Compositional Generalization in Neural Networks: A Necessary and Sufficient Condition","url":"https://arxiv.org/html/2505.02627"},{"title":"Compositional Generalization for Primitive Substitutions - ACL Anthology","url":"https://aclanthology.org/D19-1438/"},{"title":"Published as a conference paper at ICLR 2025","url":"https://arxiv.org/pdf/2405.16391"},{"title":"Compositional Generalization for Primitive Substitutions","url":"https://arxiv.org/pdf/1910.02612"},{"title":"arXiv:2405.02350v1 [cs.LG] 2 May 2024 What makes Models Compositional?","url":"https://arxiv.org/pdf/2405.02350"}]

Based on the search results, I found the relevant paper you're looking for:

Yuanpeng Li's paper derives a necessary and sufficient condition for compositional generalization in neural networks, which conceptually requires that (i) the computational graph matches the true compositional structure, and (ii) components encode just enough information in training.

Compositional generalization is a crucial property in artificial intelligence, enabling models to handle novel combinations of known components. While most deep learning models lack this capability, certain models succeed in specific tasks, suggesting the existence of governing conditions.

The condition combines aspects of architecture design, regularization, and training data properties. The paper also includes mathematical proofs supporting the condition.

The paper was published on arXiv on May 5, 2025 (arXiv:2505.02627) with the title "A Theoretical Analysis of Compositional Generalization in Neural Networks: A Necessary and Sufficient Condition."


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "7dd0dc0c-3efd-4ed3-9c0e-51bcaa084542",
  "isSidechain": true,
  "promptId": "d4a73727-8220-46d8-98b1-d049e20c8ef5",
  "agentId": "ac264cfb0150d4e15",
  "type": "user",
  "uuid": "ba4cd549-4cdf-4d54-ae8b-dea127de17aa",
  "sourceToolAssistantUUID": "7dd0dc0c-3efd-4ed3-9c0e-51bcaa084542",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "bd21c8ef-b139-4bde-afcd-7b4dbdab2a90",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 18 · 2026-05-29T05:32:23.691Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01KjLPeJhx1mrnmNQDzgkVTL`</summary>

```json
{
  "url": "https://arxiv.org/html/2505.02627v1",
  "prompt": "Extract the FULL details of: (1) Section on related work - what prior approaches existed and what gaps they left. (2) The complete problem formulation including all definitions of component, computational graph, reference graph set. (3) The full statement of Theorem 1 and Theorem 2 with all conditions. (4) The proof sketch or key proof ideas. (5) The discussion on how to assess compositional generalization BEFORE training. (6) The discussion on attention mechanisms and how they relate to the framework. (7) What \"minimal sufficient information\" means - all details about minimized representation. (8) The connection between computational graph alignment and compositional structure. (9) Any discussion of training data synthesis or data requirements. (10) The ablation study details and what happens when each condition is removed. Be maximally thorough."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ba4cd549-4cdf-4d54-ae8b-dea127de17aa",
  "isSidechain": true,
  "agentId": "ac264cfb0150d4e15",
  "requestId": "req_011CbWK76CenFaTtZtjmNr1N",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "8cf93385-5c31-48af-8c28-0e947986c890",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "bd21c8ef-b139-4bde-afcd-7b4dbdab2a90",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AJRMrtGSu3PwPabUEXEvaW",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 632,
      "cache_creation_input_tokens": 1738,
      "cache_read_input_tokens": 10110,
      "output_tokens": 389,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1738
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 632,
          "output_tokens": 389,
          "cache_read_input_tokens": 10110,
          "cache_creation_input_tokens": 1738,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1738,
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

_source line 19 · 2026-05-29T05:32:25.009Z_

<details><summary>↩ Tool result · `toolu_01VkaARYuTc5PjKBtcEAMx1i`</summary>

```text
Web search results for query: "compositional generalization computational graph alignment minimal sufficient information theory 2025"

Links: [{"title":"A Theoretical Analysis of Compositional Generalization in Neural Networks: A Necessary and Sufficient Condition","url":"https://arxiv.org/html/2505.02627"},{"title":"[2505.02627] A Theoretical Analysis of Compositional Generalization in Neural Networks: A Necessary and Sufficient Condition","url":"https://arxiv.org/abs/2505.02627"},{"title":"arXiv:2505.02627v1 [cs.LG] 5 May 2025","url":"https://arxiv.org/pdf/2505.02627"},{"title":"Statistical-computational gap in multiple Gaussian graph alignment","url":"https://arxiv.org/pdf/2512.00610"},{"title":"The Mystery of Compositional Generalization in Graph- ...","url":"https://aclanthology.org/2024.findings-emnlp.492.pdf"},{"title":"Scalable Evaluation and Neural Models for Compositional Generalization for NeurIPS 2025 - IBM Research","url":"https://research.ibm.com/publications/scalable-evaluation-and-neural-models-for-compositional-generalization"}]

Based on the search results, I found highly relevant research on compositional generalization that directly addresses your query:

The most directly relevant work is a paper that derives a necessary and sufficient condition for compositional generalization in neural networks, requiring that the computational graph matches the true compositional structure and components encode just enough information in training. 

This condition includes structural alignment, where the computational graph structure matches the true compositional hierarchy, and minimized and unambiguous representations in training, where components encode just enough information with no redundancies and no ambiguities.

Key aspects of this theoretical framework include:

- The condition is both necessary and sufficient, meaning that meeting this condition is not only required but also enough for a model to achieve compositional generalization
- The condition is supported by rigorous mathematical proofs, ensuring the reliability and universality of the findings
- This condition combines aspects of architecture design, regularization, and training data properties

This research (arxiv 2505.02627) was published in May 2025 and appears to be the primary work matching your specific search terms about compositional generalization, computational graph alignment, and minimal sufficient information principles.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "fcb88ff9-a7f8-458e-9efe-bb26ecfb2ebb",
  "isSidechain": true,
  "promptId": "d4a73727-8220-46d8-98b1-d049e20c8ef5",
  "agentId": "ac264cfb0150d4e15",
  "type": "user",
  "uuid": "971e472d-0581-41d2-a406-3fc72bcff08d",
  "sourceToolAssistantUUID": "fcb88ff9-a7f8-458e-9efe-bb26ecfb2ebb",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "bd21c8ef-b139-4bde-afcd-7b4dbdab2a90",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-29T05:33:08.657Z_

<details><summary>↩ Tool result · `toolu_01KjLPeJhx1mrnmNQDzgkVTL`</summary>

````text
# Comprehensive Analysis of Compositional Generalization Framework

## 1. Related Work and Research Gaps

**Prior Approaches:**
The paper identifies three main research directions:

- **Disentangled representation learning**: Methods like β-VAE learn statistical independence, with later work introducing symmetry-based approaches. However, these remain largely unsupervised.

- **Architecture design**: Modular networks and attention mechanisms (including Transformers) are explored. Recent work shows "modular architectures alone cannot guarantee compositional generalization without aligned dataset structures" (Jarvis et al. 2023).

- **Meta-learning**: Enables task adaptation but requires carefully designed meta-training sequences.

**Identified Gaps:**
Recent theoretical work (Lippl & Stachenfeld 2025) reveals fundamental limitations, showing models constrained to "conjunction-wise additive" computations preventing transitive generalization. Wiedemer et al. (2023) established that "generalization requires sufficient latent support and compositional function structure." The paper fills this gap by deriving both necessary *and* sufficient conditions.

---

## 2. Complete Problem Formulation

### Core Definitions

**Definition 1 (Component):** "A component is a deterministic function that maps a sequence of input nodes to a single output node." Neural network modules without parameter sharing qualify as components.

**Definition 2 (Computational Graph):** "A directed acyclic graph that maps sample input to output by combining components." The graph input is X; output Ŷ has the same node count as Y. Components can be reused across positions (e.g., convolutional kernels).

**Definition 3 (Graph Set):** Collection of graphs, one per dataset sample. Hypothesis graph set ℋ contains graphs produced by the model; reference graph set 𝒵 represents the true compositional structure.

**Definition 4 (Reference Graph Set):** A graph set 𝒵 with two properties:
1. All graphs have correct predictions: ∀A ∈ 𝒟: Ŷᴬ = Yᴬ
2. "All test component inputs are seen in training"—every test component input (represented as zᴮ ∈ Zᴮ) has a corresponding training instance with identical input.

This definition ensures test graphs represent novel *combinations* of seen components, not entirely novel components.

---

## 3. Complete Theorem Statements

**Theorem 1 (Necessary and Sufficient Condition):**

A model enables compositional generalization if and only if it has:

1. **Structural Alignment (Definition 6):** "The hypothesis graph set ℋ has structural alignment property if it has structural alignment with a reference graph set." Formally: ∃𝒵 ∈ ℤ: ℋ ≅ 𝒵. This means computational graph structure *matches* the true compositional hierarchy.

2. **Unambiguous Representation (Definition 7):** "Given structural alignment, all component output nodes have well-defined mappings for training data." If two training samples have identical hypothesis values at a node, they must have identical reference values: hᴬ = hᶜ ⟹ zᴬ = zᶜ.

3. **Minimized Representation (Definition 8):** "The number of distinct training outputs is minimized for each component." This prevents redundant or spurious information encoding.

**Theorem 2 (Alternative Necessary and Sufficient Condition):**

When compositional generalization is alternatively defined to include the requirement that "all test component inputs must have been observed during training" as part of the definition itself (Definition 11), the same three conditions remain necessary and sufficient, eliminating dependence on Assumption 1.

---

## 4. Proof Architecture and Key Ideas

### Necessity (Proposition 1)

The proof treats the trained hypothesis graph set ℋ as itself a reference graph set when:
- All training samples are correctly predicted
- All test component inputs were seen in training (Assumption 1)

Since ℋ satisfies reference properties, the three conditions follow:
- Structural alignment is trivial (ℋ ≅ ℋ)
- Unambiguous representation: nodes map to themselves (bijections)
- Minimized representation: By **Lemma 1**, a well-defined onto mapping becomes bijective *if and only if* the domain size is minimized. Since bijections exist, representations are minimal.

### Sufficiency (Proposition 2)

Uses **bottom-up mathematical induction** over graph structure:

**Lemma 2 (Induction Step)** proves: Given structural alignment and one-to-one mappings in training, if every test node's input neighbors have corresponding training instances with identical reference inputs and hypothesis values, then the node itself has a training instance matching its reference output and hypothesis value.

**Proof sketch (Figure 3):**
- For test node B with reference value zᴮ and input nodes {z₁ᴮ, ..., zₙᴮ}
- By structural alignment and reference graph properties (Definition 4), ∃A ∈ 𝒟ₜᵣₐᵢₙ with 𝐳ᴬ = 𝐳ᴮ
- By induction, each input neighbor zᵢᴮ has a training counterpart Cᵢ with hᶜⁱ = hᵢᴮ
- One-to-one mapping (from unambiguous + minimized representation by Lemma 1): zᶜⁱ = zᵢᴮ ⟹ hᶜⁱ = hᵢᴮ
- Determinism of components (Definition 1): identical inputs ⟹ identical outputs
- Therefore: zᴬ = zᴮ (by determinism) and hᴬ = hᴮ (by induction)
- Base case: input nodes directly from training data satisfy properties

This inductive reasoning extends from leaf nodes to output nodes, ensuring test predictions match reference outputs.

---

## 5. Assessing Compositional Generalization Before Training

Section 5.7 outlines operationalizing the conditions as *inductive biases*:

**Minimized Representation:** Enable via regularization (Section 5.2)
- Add Gaussian noise: h' = h + 𝒩(0, α)
- Enforce power constraint: ℒ' = ℒ + β‖h‖²
- These reduce redundant information, automatically merging similar representations

**Structural Alignment:** Achieved through architectural design
- Leverage prior knowledge of compositional structure
- Use modular networks explicitly mirroring input hierarchies
- Example: In the minimal XOR example, design fₕ to process (x₁, x₂) before combining with x₃

**Unambiguous Representation:** Require pre-training data analysis
- Identify potential ambiguous pairs where "the same hypothesis node value maps to different reference values"
- Verify training data contains no such pairs
- Analyze model architecture to ensure it cannot create such ambiguities given data structure
- The paper notes: "currently requiring case-by-case analysis"

The conditions thus become **design objectives** rather than post-hoc verification criteria.

---

## 6. Attention Mechanisms and the Framework

**Definition 9 (Effectively Equal Representations):**

Two input representations 𝐳ᴬ, 𝐳ᴮ are "effectively equal" if the component performs a commutative operation and representations match under permutation.

**Application to Attention:**

The standard attention computation: Attention(U,V) = VU = Σᵢ₌₁ᵏ uᵢvᵢ

Because summation is commutative, "different permutations of the weighted values do not change the output result." This allows attention mechanisms to handle variable-order inputs while maintaining component determinism (Definition 1).

**Implications:**
- Attention can effectively implement structural alignment by dynamically determining component input ordering
- The framework extends naturally to attention-based architectures
- Effectively equal representations preserve the bijective mapping property required for minimized representation

---

## 7. Minimized Representation: Complete Details

**Definition 8 (Minimized Representation):** "The number of distinct training outputs is minimized for each component."

**Why minimize?**
- Excessive information encoding creates spurious correlations unreliable under distribution shift
- Excessive compression loses information needed for composition

**Achieving Minimization:**

The regularization approach (Section 5.2) applies information-theoretic principles:

**Definition 10 (Gaussian Channel with Power Constraint):**
Channel equation: Y = X + Z where Z ~ 𝒩(0, N)
Power constraint: (1/n)Σᵢ₌₁ⁿ xᵢ² ≤ P

This formalizes information bottleneck: constrained capacity forces selective information retention.

**Implementation:**
```
h' = h + 𝒩(0, α)        [noise injection]
ℒ' = ℒ + β‖h‖²          [activity regularization]
```

- Noise adds stochastic compression; tight distributions become indistinguishable
- L2 regularization penalizes large activations, reducing effective information
- Hyperparameters α (noise scale) and β (regularization weight) control compression strength

**Result:** Components with redundant outputs converge to identical representations; distinct outputs only arise when necessary for correct training predictions.

**Connection to Section 5.3 (Representation Compression in Training):**

The paper argues implicit compression occurs naturally: "neural network components tend to reduce the number of distinct training inputs" because networks with fewer input patterns converge faster. This suggests regularization weakly occurs without explicit design, aligning training dynamics with the minimized representation requirement.

---

## 8. Computational Graph Alignment and Compositional Structure

**Core Insight:**

Compositional structure is defined by the *reference graph set* 𝒵, which the model cannot directly observe. Structural alignment requires the hypothesis graph ℋ to *match* this hidden structure.

**How Alignment Works:**

1. **Graph Isomorphism:** ℋ ≅ 𝒵 means there exists a bijection between node sets preserving edge relationships
   - If hypothesis node h connects to inputs {h₁, h₂}, then corresponding reference node z connects to {z₁, z₂}
   - This mirrors the true compositional hierarchy

2. **Without Alignment:** 
   - Example: If the true function is y = (x₁ ⊕ x₂) ⊕ x₃ (hierarchical)
   - But model assumes y = f(x₁, x₂, x₃) (flat)
   - Even with perfect component learning, the structure is wrong
   - Test samples with unseen feature combinations will fail

3. **With Alignment:**
   - Model structure mirrors true composition
   - Test samples, though combining known components differently, follow the correct computational pathway
   - Example: the minimal XOR model processes x₁, x₂ through component fₕ before combining output h with x₃

**Practical Implication:**

Structural alignment cannot be learned from data alone—it requires inductive bias. The paper states: "compositional generalization fundamentally requires prior knowledge of the target compositional hierarchy."

---

## 9. Training Data Synthesis and Requirements

**Definition 4 Requirements:**

The reference graph set mandates:
1. Correct predictions on all data
2. All test component inputs must appear in training

**What "component inputs" means:**

Not the raw features, but the *processed inputs to each component*. For y = (x₁ ⊕ x₂) ⊕ x₃:
- First component receives (x₁, x₂); test samples have all combinations seen in training
- Second component receives (z, x₃) where z = x₁ ⊕ x₂; all (z, x₃) pairs in test are seen in training

**Minimal Training Dataset:**

The minimal example (Section 4, Table 1) includes 6 training samples: a, b, c, d, e, f
- Must cover all input combinations to the first component: (0,0), (0,1), (1,0), (1,1)
- Must cover all input combinations to the second component for each possible z value
- Test samples {(1,0,0), (1,1,0)} are unseen *full combinations* but use seen component inputs

**Data Synthesis Guidance:**

Before training, one must:
1. Decompose target function into compositional hierarchy
2. For each component, enumerate all input combinations that appear in test
3. Ensure training data covers these combinations
4. Verify no training sample ambiguities (Definition 7)

The paper explicitly states this requires understanding "the true compositional structure," which human designers or inductive biases must provide.

---

## 10. Ablation Study: Impact of Removing Each Condition

**Table 2 Results Summary:**

| Configuration | Accuracy |
|---------------|----------|
| Full model (all conditions) | 1.0 ± 0.0 |
| Baseline (flat fully-connected) | 0.0 ± 0.0 |
| **No Regularization** | 0.0 ± 0.0 |
| **No Structure** | 0.0 ± 0.0 |
| **Modified Training Data** | 0.0 ± 0.0 |

### Detailed Failure Modes:

**1. Removing Regularization (Minimized Representation):**

The model retains structural alignment and correct training data but removes noise injection and L2 penalties.

*Result:* 0% test accuracy

*Reason:* Without minimization pressure, components encode spurious information. For the hidden node h, multiple training samples with identical hypothesis values hᴬ = hᶜ can have different reference values zᴬ ≠ zᶜ. This breaks well-defined mappings (Definition 7). When test samples appear, the ambiguous h cannot reliably predict z, causing cascading errors.

**2. Removing Structural Alignment (Structure):**

Uses baseline fully-connected architecture instead of the designed modular structure.

*Result:* 0% test accuracy

*Reason:* The baseline processes all inputs (x₁, x₂, x₃) simultaneously in a flat network. This cannot mirror the true hierarchical composition of y = (x₁ ⊕ x₂) ⊕ x₃. Even if the network somehow learns the function on training data, test samples following a different feature combination pattern encounter regions of weight space not constrained by training.

**3. Removing Training Data Completeness:**

Removes the last two training samples (e and f) from Table 1.

*Result:* 0% test accuracy

*Reason:* This creates an ambiguity counterexample. With samples {a, b, c, d} only, the second component's inputs (z, x₃) are:
- Sample a: (0, 0)
- Sample b: (1, 0)
- Sample c: (1, 1)
- Sample d: (0, 1)

This appears complete, but removing samples e and f breaks unambiguous representation on the hidden node h. Specifically, if h = x₂ for the remaining samples, then:
- Sample a: h = 0, but should reference z = 0
- Sample c: h = 0, but should reference z = 1 ✗ *Ambiguity*

The mapping from h to z is not well-defined. During test, when h = 0 appears, the model cannot determine which z value to use.

---

## Summary Integration

The framework unifies architecture (structural alignment), regularization (minimized representation), and data requirements (unambiguous representation) into a coherent necessary and sufficient condition. Each component is independently essential; removing any causes complete failure on compositional generalization tasks. The mathematical framework explains *why* modern approaches work (when they do) and provides guidance for designing systems that provably achieve compositional generalization.
````

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "8cf93385-5c31-48af-8c28-0e947986c890",
  "isSidechain": true,
  "promptId": "d4a73727-8220-46d8-98b1-d049e20c8ef5",
  "agentId": "ac264cfb0150d4e15",
  "type": "user",
  "uuid": "790c57ff-72fc-420e-ad64-6dbeb72aaf09",
  "sourceToolAssistantUUID": "8cf93385-5c31-48af-8c28-0e947986c890",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "bd21c8ef-b139-4bde-afcd-7b4dbdab2a90",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 21 · 2026-05-29T05:33:11.791Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01GaDwLYaaJKfcspHT642U7M`</summary>

```json
{
  "query": "Yuanpeng Li compositional generalization paper review OpenReview NeurIPS ICML 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "790c57ff-72fc-420e-ad64-6dbeb72aaf09",
  "isSidechain": true,
  "agentId": "ac264cfb0150d4e15",
  "requestId": "req_011CbWKB86rmD25n1GH4mzUu",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "67177f07-2907-4627-bc76-cd9780ca088d",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "bd21c8ef-b139-4bde-afcd-7b4dbdab2a90",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UZ4u2mkHsbZLfVbqSjkzwh",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6131,
      "cache_read_input_tokens": 11848,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 6131,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 35,
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

_source line 22 · 2026-05-29T05:33:12.334Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01NUxUroaDCxdMUsJNHqahrm`</summary>

```json
{
  "query": "compositional generalization skill graph training data synthesis neural network theory 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "67177f07-2907-4627-bc76-cd9780ca088d",
  "isSidechain": true,
  "agentId": "ac264cfb0150d4e15",
  "requestId": "req_011CbWKB86rmD25n1GH4mzUu",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "337c56f9-e31c-496c-a285-f39bf863df4e",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "bd21c8ef-b139-4bde-afcd-7b4dbdab2a90",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UZ4u2mkHsbZLfVbqSjkzwh",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6131,
      "cache_read_input_tokens": 11848,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 6131,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 35,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool result

_source line 23 · 2026-05-29T05:33:17.476Z_

<details><summary>↩ Tool result · `toolu_01GaDwLYaaJKfcspHT642U7M`</summary>

```text
Web search results for query: "Yuanpeng Li compositional generalization paper review OpenReview NeurIPS ICML 2025 2026"

Links: [{"title":"[2505.02627] A Theoretical Analysis of Compositional Generalization in Neural Networks: A Necessary and Sufficient Condition","url":"https://arxiv.org/abs/2505.02627"},{"title":"Understanding Compositional Generalization via Hierarchical Concept Models | OpenReview","url":"https://openreview.net/forum?id=DeD9rkzQfP"},{"title":"Yuanpeng Li | OpenReview","url":"https://openreview.net/profile?id=~Yuanpeng_Li2"},{"title":"Transferability of Compositionality | OpenReview","url":"https://openreview.net/forum?id=GHCu1utcBvX"},{"title":"Compositional Generalization from First Principles | OpenReview","url":"https://openreview.net/forum?id=LqOQ1uJmSx"},{"title":"Measuring Compositional Generalization: A Comprehensive Method on Realistic Data | OpenReview","url":"https://openreview.net/forum?id=SygcCnNKwr"},{"title":"Grounded Compositional Generalization with Environment Interactions | OpenReview","url":"https://openreview.net/forum?id=b6BdrqTnFs7"},{"title":"Towards Understanding the Relationship between In-context Learning and   Compositional Generalization","url":"https://arxiv.org/pdf/2403.11834"},{"title":"Automatically Composing Representation Transformations as a Means for   Generalization","url":"https://arxiv.org/pdf/1807.04640"}]

Based on the search results, I found relevant information about Yuanpeng Li's work on compositional generalization:

## Key Finding

Yuanpeng Li has authored a paper that derives a necessary and sufficient condition for compositional generalization in neural networks. Conceptually, it requires that (i) the computational graph matches the true compositional structure, and (ii) components encode just enough information in training.

## Paper Details

The paper is titled "A Theoretical Analysis of Compositional Generalization in Neural Networks: A Necessary and Sufficient Condition" (arXiv 2505.02627). The paper was published on May 5, 2025.

## Profile Information

Yuanpeng Li has a profile on OpenReview with multiple submissions to ICLR, including work last modified on January 14, 2026.

The search results show this is a recent theoretical contribution to understanding the conditions under which neural networks can achieve compositional generalization—the ability to handle novel combinations of known components.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "67177f07-2907-4627-bc76-cd9780ca088d",
  "isSidechain": true,
  "promptId": "d4a73727-8220-46d8-98b1-d049e20c8ef5",
  "agentId": "ac264cfb0150d4e15",
  "type": "user",
  "uuid": "3fd5e4a3-47a0-4848-84be-695d25d0aa25",
  "sourceToolAssistantUUID": "67177f07-2907-4627-bc76-cd9780ca088d",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "bd21c8ef-b139-4bde-afcd-7b4dbdab2a90",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 24 · 2026-05-29T05:33:19.223Z_

<details><summary>↩ Tool result · `toolu_01NUxUroaDCxdMUsJNHqahrm`</summary>

```text
Web search results for query: "compositional generalization skill graph training data synthesis neural network theory 2025 2026"

Links: [{"title":"Towards Compositional Generalization of LLMs via Skill Taxonomy Guided Data Synthesis","url":"https://arxiv.org/pdf/2601.03676"},{"title":"Towards Compositional Generalization of LLMs via Skill Taxonomy Guided Data Synthesis","url":"https://arxiv.org/html/2601.03676"},{"title":"A Theoretical Analysis of Compositional Generalization in Neural   Networks: A Necessary and Sufficient Condition","url":"https://arxiv.org/pdf/2505.02627"},{"title":"A Theoretical Analysis of Compositional Generalization in Neural Networks: A Necessary and Sufficient Condition","url":"https://arxiv.org/html/2505.02627v1"},{"title":"Compositional Generalization and Decomposition in Neural Program   Synthesis","url":"https://arxiv.org/pdf/2204.03758"},{"title":"[2505.02627] A Theoretical Analysis of Compositional Generalization in Neural Networks: A Necessary and Sufficient Condition","url":"https://arxiv.org/abs/2505.02627"},{"title":"[2601.03676] Towards Compositional Generalization of LLMs via Skill Taxonomy Guided Data Synthesis","url":"https://arxiv.org/abs/2601.03676"}]

Based on the search results, I found highly relevant recent research on compositional generalization, skill graphs, and training data synthesis:

## Key Recent Research (2025-2026)

**STEPS Framework (January 2026):**
STEPS is a Skill Taxonomy–guided Entropy-based Post-training data Synthesis framework that targets compositional generalization by uncovering latent relationships among skills and organizing them into a hierarchical skill taxonomy using structural information theory. The framework formulates data synthesis as a constrained information maximization problem, selecting skill combinations that maximize marginal structural information within the hierarchy while preserving semantic coherence.

**Problem Context:**
Large Language Models and agent-based systems often struggle with compositional generalization due to a data bottleneck in which complex skill combinations follow a long-tailed, power-law distribution. Existing data-centric strategies primarily operate at the level of individual skills and do not fundamentally address the scarcity of compositionally challenging examples, though some efforts synthesize data through skill mixing but typically ignore underlying structural and hierarchical relationships among skills.

**Neural Network Theory (May 2025):**
Recent theoretical work derives a necessary and sufficient condition for compositional generalization in neural networks, requiring that the computational graph matches the true compositional structure and components encode just enough information in training.

These represent the cutting-edge research in compositional generalization for neural networks in 2025-2026.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "337c56f9-e31c-496c-a285-f39bf863df4e",
  "isSidechain": true,
  "promptId": "d4a73727-8220-46d8-98b1-d049e20c8ef5",
  "agentId": "ac264cfb0150d4e15",
  "type": "user",
  "uuid": "436a9858-8944-4408-b0c0-9cc8dd330cae",
  "sourceToolAssistantUUID": "337c56f9-e31c-496c-a285-f39bf863df4e",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "bd21c8ef-b139-4bde-afcd-7b4dbdab2a90",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 25 · 2026-05-29T05:33:21.803Z_

Let me get more details on the STEPS paper which connects to the skill-graph-guided training data synthesis angle.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "436a9858-8944-4408-b0c0-9cc8dd330cae",
  "isSidechain": true,
  "agentId": "ac264cfb0150d4e15",
  "requestId": "req_011CbWKBuKwTXhVYzysqr7b8",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "28628e26-0008-46cd-9582-65b087ea7b01",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "bd21c8ef-b139-4bde-afcd-7b4dbdab2a90",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018EVmxFmQYKmSf15W88bNHj",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1544,
      "cache_read_input_tokens": 17979,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1544,
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

_source line 26 · 2026-05-29T05:33:24.169Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_016dTpPGmVNdHyzmbgGogisi`</summary>

```json
{
  "url": "https://arxiv.org/abs/2601.03676",
  "prompt": "Extract the full abstract, title, authors, and key details of this paper on skill taxonomy guided data synthesis for compositional generalization. How does it relate to the theoretical framework of Li (2505.02627)? What is the STEPS framework and how does it use skill graphs?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "28628e26-0008-46cd-9582-65b087ea7b01",
  "isSidechain": true,
  "agentId": "ac264cfb0150d4e15",
  "requestId": "req_011CbWKBuKwTXhVYzysqr7b8",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "c4893a72-9b19-48d7-a8c2-bc9c4e06c62e",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "bd21c8ef-b139-4bde-afcd-7b4dbdab2a90",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018EVmxFmQYKmSf15W88bNHj",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1544,
      "cache_read_input_tokens": 17979,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1544,
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

_source line 27 · 2026-05-29T05:33:25.247Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01LAqFYbpjpWJZXpLedwFaLh`</summary>

```json
{
  "url": "https://openreview.net/profile?id=~Yuanpeng_Li2",
  "prompt": "Extract all information about Yuanpeng Li's submissions, reviews, and any discussion or feedback on the compositional generalization paper."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c4893a72-9b19-48d7-a8c2-bc9c4e06c62e",
  "isSidechain": true,
  "agentId": "ac264cfb0150d4e15",
  "requestId": "req_011CbWKBuKwTXhVYzysqr7b8",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "15e18162-b584-4515-8e13-d499a981c95e",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "bd21c8ef-b139-4bde-afcd-7b4dbdab2a90",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018EVmxFmQYKmSf15W88bNHj",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1544,
      "cache_read_input_tokens": 17979,
      "output_tokens": 265,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1544
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 265,
          "cache_read_input_tokens": 17979,
          "cache_creation_input_tokens": 1544,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1544,
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

_source line 28 · 2026-05-29T05:33:29.921Z_

<details><summary>↩ Tool result · `toolu_01LAqFYbpjpWJZXpLedwFaLh`</summary>

```text
# Yuanpeng Li's OpenReview Profile Summary

## Profile Information
Yuanpeng Li joined OpenReview in September 2019 and studied at Shanghai Jiao Tong University and Tsinghua University (2004–2008). No specific expertise areas or advisor relations are listed on the profile.

## Publications Overview
Li has submitted nine papers to OpenReview, primarily focusing on compositional generalization, causal representations, and deep learning:

**Recent Work:**
- "On the Relation between Gradient Directions and Systematic Generalization" (ICLR 2024, withdrawn submission)
- "Efficiently Disentangle Causal Representations" (CPAL 2024, oral presentation)
- "On a Built-in Conflict between Deep Learning and Systematic Generalization" (submitted to ICLR 2023)

**Earlier Submissions (ICLR 2021):**
- Papers titled "Gradient Descent Resists Compositionality," "Transferability of Compositionality," and "Necessary and Sufficient Conditions for Compositional Representations"

## Collaborators
Li frequently collaborates with Joel Hestness, Kenneth Church, Liang Zhao, Mohamed Elhoseiny, and Ka Yee Lun across multiple submissions.

**Note:** The provided content contains no discussion feedback, reviewer comments, or detailed reviews of these papers.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "15e18162-b584-4515-8e13-d499a981c95e",
  "isSidechain": true,
  "promptId": "d4a73727-8220-46d8-98b1-d049e20c8ef5",
  "agentId": "ac264cfb0150d4e15",
  "type": "user",
  "uuid": "8396d95e-c77e-4b1c-a8ea-040ea993a839",
  "sourceToolAssistantUUID": "15e18162-b584-4515-8e13-d499a981c95e",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "bd21c8ef-b139-4bde-afcd-7b4dbdab2a90",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 29 · 2026-05-29T05:33:30.316Z_

<details><summary>↩ Tool result · `toolu_016dTpPGmVNdHyzmbgGogisi`</summary>

```text
# Paper Summary: Compositional Generalization via Skill Taxonomy

## Full Details

**Title:** "Towards Compositional Generalization of LLMs via Skill Taxonomy Guided Data Synthesis"

**Authors:** Yifan Wei, Li Du, Xiaoyan Yu, Yang Feng, Angsheng Li

**Submission Date:** January 7, 2026 (arXiv:2601.03676)

## Abstract Overview

The paper addresses a critical limitation in large language models: difficulty with compositional generalization due to "a data bottleneck in which complex skill combinations follow a long-tailed, power-law distribution." This constraint impacts both instruction-following performance and agent-based task generalization.

## The STEPS Framework

STEPS (Skill Taxonomy guided Entropy-based Post-training data Synthesis) tackles this challenge through:

1. **Skill Taxonomy Development:** Organizing skills into "an interpretable, hierarchical skill taxonomy using structural information theory"

2. **Data Synthesis Approach:** Formulating synthesis as a constrained optimization problem that "selecting skill combinations that maximize marginal structural information within the hierarchy"

## Regarding Li (2505.02627)

The provided content contains no reference to Li (2505.02627), so I cannot establish any connection to that theoretical framework based on the available information.

## Key Resources

Code and experimental data are available on GitHub at the repository referenced in the paper's comments section.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c4893a72-9b19-48d7-a8c2-bc9c4e06c62e",
  "isSidechain": true,
  "promptId": "d4a73727-8220-46d8-98b1-d049e20c8ef5",
  "agentId": "ac264cfb0150d4e15",
  "type": "user",
  "uuid": "f4c8f5df-f42d-4ec4-b014-d00470ed2db9",
  "sourceToolAssistantUUID": "c4893a72-9b19-48d7-a8c2-bc9c4e06c62e",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "bd21c8ef-b139-4bde-afcd-7b4dbdab2a90",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 30 · 2026-05-29T05:33:35.236Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01XvuTXMdotNtpncatiQNpXH`</summary>

```json
{
  "query": "\"Compositional Generalization from First Principles\" OpenReview LqOQ1uJmSx"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f4c8f5df-f42d-4ec4-b014-d00470ed2db9",
  "isSidechain": true,
  "agentId": "ac264cfb0150d4e15",
  "requestId": "req_011CbWKCioD3j9H2AVqURXNc",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "8b1be9c3-2566-4142-ac72-433b760ce24e",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "bd21c8ef-b139-4bde-afcd-7b4dbdab2a90",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013xZG8iZoEor3gVsNpGEZ2L",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 350,
      "cache_creation_input_tokens": 620,
      "cache_read_input_tokens": 19523,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 620,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 42,
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

_source line 31 · 2026-05-29T05:33:36.042Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01VhycYWTrnQYupUjf224qEe`</summary>

```json
{
  "url": "https://openreview.net/forum?id=LqOQ1uJmSx",
  "prompt": "Extract all reviews, discussions, and feedback about this paper on compositional generalization. What are reviewers saying about the approach, strengths, weaknesses?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8b1be9c3-2566-4142-ac72-433b760ce24e",
  "isSidechain": true,
  "agentId": "ac264cfb0150d4e15",
  "requestId": "req_011CbWKCioD3j9H2AVqURXNc",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "9a285416-6bed-4617-89a5-e5242555da34",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "bd21c8ef-b139-4bde-afcd-7b4dbdab2a90",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013xZG8iZoEor3gVsNpGEZ2L",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 350,
      "cache_creation_input_tokens": 620,
      "cache_read_input_tokens": 19523,
      "output_tokens": 181,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 620
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 350,
          "output_tokens": 181,
          "cache_read_input_tokens": 19523,
          "cache_creation_input_tokens": 620,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 620,
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

_source line 32 · 2026-05-29T05:33:40.713Z_

<details><summary>↩ Tool result · `toolu_01XvuTXMdotNtpncatiQNpXH`</summary>

```text
Web search results for query: ""Compositional Generalization from First Principles" OpenReview LqOQ1uJmSx"

Links: [{"title":"Compositional Generalization from First Principles | OpenReview","url":"https://openreview.net/forum?id=LqOQ1uJmSx"},{"title":"Compositional Generalization from First Principles","url":"https://arxiv.org/pdf/2307.05596"},{"title":"Compositional Generalization from First Principles Thaddäus Wiedemer1,2,3∗","url":"https://proceedings.neurips.cc/paper_files/paper/2023/file/15f6a10899f557ce53fe39939af6f930-Paper-Conference.pdf"},{"title":"Compositional Generalization from First Principles","url":"https://arxiv.org/html/2307.05596"},{"title":"[2307.05596] Compositional Generalization from First Principles","url":"https://arxiv.org/abs/2307.05596"},{"title":"[PDF] Compositional Generalization from First Principles | Semantic Scholar","url":"https://www.semanticscholar.org/paper/8cb0b1047de0bfd50f52bfb6a9f8daca4f243ec7"},{"title":"Compositional generalization from first principles | Proceedings of the 37th International Conference on Neural Information Processing Systems","url":"https://dl.acm.org/doi/10.5555/3666122.3666426"},{"title":"Compositional Generalization from First Principles","url":"https://proceedings.neurips.cc//paper_files/paper/2023/hash/15f6a10899f557ce53fe39939af6f930-Abstract-Conference.html"}]

I found the paper you're looking for! Here are the key details:

## Compositional Generalization from First Principles

**Paper Information:**
- Authors: Thaddäus Wiedemer, Prasanna Mayilvahanan, Matthias Bethge, and Wieland Brendel from the University of Tübingen, Tübingen AI Center, and Max-Planck-Institute for Intelligent Systems
- Published on OpenReview (November 2, 2023) and appeared at NeurIPS 2023
- OpenReview ID: LqOQ1uJmSx

**Main Contribution:**
The paper investigates compositionality as a property of the data-generating process rather than the data itself, inspired by identifiable representation learning. This reformulation enables the authors to derive mild conditions on only the support of the training distribution and the model architecture, which are sufficient for compositional generalization.

**Key Finding:**
The work derives sufficient conditions on the data generating process and model architecture under which compositional generalization provably occurs.

The paper is available on both OpenReview and arXiv (2307.05596) and demonstrates how their theoretical framework applies to real-world scenarios with empirical validation.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "8b1be9c3-2566-4142-ac72-433b760ce24e",
  "isSidechain": true,
  "promptId": "d4a73727-8220-46d8-98b1-d049e20c8ef5",
  "agentId": "ac264cfb0150d4e15",
  "type": "user",
  "uuid": "60276a2d-7822-4fd9-8fc8-06e64c7a04a0",
  "sourceToolAssistantUUID": "8b1be9c3-2566-4142-ac72-433b760ce24e",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "bd21c8ef-b139-4bde-afcd-7b4dbdab2a90",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 33 · 2026-05-29T05:33:41.233Z_

<details><summary>↩ Tool result · `toolu_01VhycYWTrnQYupUjf224qEe`</summary>

```text
# Review Information Unavailable

Based on the webpage content provided, I cannot extract reviews, discussions, or feedback about this paper. The page displays only the **paper metadata and abstract**, including:

- Title and authors
- Publication date (September 21, 2023)
- Keywords and TL;DR summary
- Basic abstract content describing the theoretical framework

The actual peer reviews, reviewer comments, discussion threads, and community feedback that would typically appear on OpenReview are **not included** in the content you provided. To access this information, you would need to visit the full OpenReview page at the paper's URL and navigate to sections like "Reviews" or "Comments."
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "9a285416-6bed-4617-89a5-e5242555da34",
  "isSidechain": true,
  "promptId": "d4a73727-8220-46d8-98b1-d049e20c8ef5",
  "agentId": "ac264cfb0150d4e15",
  "type": "user",
  "uuid": "8e532726-585d-4bdd-9b9e-a32723f7f94d",
  "sourceToolAssistantUUID": "9a285416-6bed-4617-89a5-e5242555da34",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "bd21c8ef-b139-4bde-afcd-7b4dbdab2a90",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 34 · 2026-05-29T05:35:25.724Z_

Now I have gathered comprehensive information. Let me compile the detailed analysis.

---

## Detailed Analysis: "A Theoretical Analysis of Compositional Generalization in Neural Networks: A Necessary and Sufficient Condition" (Li, arXiv:2505.02627, May 2025)

---

### 1. What Gap Did They Identify, and How?

Li identified that the existing literature on compositional generalization suffered from a fundamental asymmetry: prior theoretical work could establish **sufficient** conditions for compositional generalization, or could demonstrate **necessary** conditions, but no work had unified both into a single **necessary AND sufficient** characterization.

Specifically, the paper surveys three prior directions and their limitations:

- **Disentangled representation learning** (e.g., beta-VAE and symmetry-based approaches): These remained largely unsupervised and offered no formal guarantees about compositional generalization.
- **Architectural approaches** (modular networks, Transformers): Jarvis et al. (2023) showed that modular architectures **alone** cannot guarantee compositional generalization without aligned dataset structures, revealing the insufficiency of architecture-only solutions.
- **Kernel-theoretic analyses**: Lippl and Stachenfeld (2025) revealed fundamental limitations showing that compositional models are constrained to "conjunction-wise additive" computations that prevent transitive generalization.

The closest prior work was Wiedemer et al. (NeurIPS 2023, "Compositional Generalization from First Principles"), which derived **sufficient** conditions based on identifiable representation learning, requiring sufficient latent support and compositional function structure. However, their conditions were only sufficient, not necessary -- they could tell you when compositional generalization would happen, but not characterize all the ways it could fail.

Li identified this gap by observing that the field needed a complete characterization -- a condition that is both necessary (without it, compositional generalization is impossible) and sufficient (with it, compositional generalization is guaranteed). This would provide both a diagnostic tool and a design principle.

---

### 2. What Was the Key Insight Others Missed?

The key insight is that compositional generalization is not a property of any single factor (architecture, data, or training procedure) in isolation, but rather an **emergent property of the interaction among three simultaneous constraints**:

1. **Structural alignment** -- the model's computational graph must mirror the true compositional hierarchy
2. **Unambiguous representation** -- component mappings must be well-defined on training data
3. **Minimized representation** -- components must encode the minimal number of distinct values

Previous work tended to focus on one axis at a time. Architecture-focused work (modular networks) addressed structural alignment but ignored data requirements. Data-focused work addressed coverage but ignored how the model's internal representations must behave. Regularization-focused work addressed representation compression but didn't connect it to graph structure.

Li's insight was that these three conditions are not independent desiderata but form an **indivisible triple**: removing any one of them causes complete failure (0% test accuracy in the ablation study). The mathematical framework shows why: the sufficiency proof uses **bottom-up induction** over the computational graph, and each condition plays a distinct, irreplaceable role in the inductive step.

---

### 3. How Did They Formulate the Problem Differently?

Li introduced a **computational graph formalism** that is distinct from prior approaches in several ways:

**Component (Definition 1):** A deterministic function mapping a sequence of input nodes to a single output node. Neural network modules without parameter sharing qualify as components.

**Computational Graph (Definition 2):** A directed acyclic graph (DAG) that connects components to transform sample inputs into outputs. Crucially, these graphs are **not provided in the data** -- they are latent structural properties.

**Graph Set (Definition 3):** A collection of computational graphs, one per dataset sample. The paper distinguishes between:
- The **hypothesis graph set** (H) -- produced by the model
- The **reference graph set** (Z) -- representing the true compositional structure

**Reference Graph Set (Definition 4):** A graph set satisfying two properties: (a) all predictions are correct, and (b) all test component inputs appear in training data. This second property is the critical formalization of what it means for test samples to be "novel combinations of familiar components."

This formulation is different from prior work because it casts compositional generalization as a **graph alignment problem** between the model's internal computational structure and the ground-truth compositional hierarchy. Rather than reasoning about latent variables, disentanglement, or kernel properties, the framework operates on the structural level of how computation is organized.

---

### 4. What Existing Technique Did They Adapt/Combine/Simplify?

Li adapted and combined several existing ideas:

**From information theory:** The concept of a Gaussian channel with power constraint (Definition 10) is used to formalize minimized representation. The regularization scheme -- adding Gaussian noise h' = h + N(0, alpha) and imposing L2 penalties L' = L + beta||h||^2 -- is an adaptation of the **information bottleneck principle** to the compositional setting. This is not new as a regularization technique, but its theoretical role as a *necessary* condition for compositional generalization is novel.

**From graph theory:** The structural alignment condition draws on **graph isomorphism** concepts, requiring a bijection between the hypothesis and reference graph node sets that preserves edge structure.

**From mathematical induction:** The sufficiency proof uses a classical **bottom-up structural induction** over the DAG, which is a standard technique in computer science but had not been applied to prove compositional generalization results. The induction starts at leaf nodes (raw inputs) and propagates correctness guarantees upward through the graph.

**From the bijection lemma (Lemma 1):** The paper proves that a well-defined onto mapping between finite sets becomes bijective if and only if the domain contains no redundant elements. This connects minimized representation to one-to-one mappings, which is the algebraic core enabling the inductive step.

The simplification achieved is notable: rather than reasoning about complex optimization landscapes, kernel properties, or representation geometry, the framework reduces compositional generalization to a combinatorial/algebraic condition on graph structure and mapping cardinalities.

---

### 5. The Formal Necessary and Sufficient Condition

**Theorem 1:** A model enables compositional generalization if and only if it satisfies all three conditions simultaneously:

**(i) Structural Alignment (Definition 6):** There exists a reference graph set Z such that the hypothesis graph set H is structurally isomorphic to Z. Formally: there exists Z in the set of all valid reference graph sets such that H is isomorphic to Z. This means the model's computational DAG mirrors the true compositional hierarchy.

**(ii) Unambiguous Representation (Definition 7):** For all training data, if two samples A and C have identical hypothesis values at a node (h^A = h^C), they must have identical reference values at the corresponding node (z^A = z^C). This ensures mappings from hypothesis space to reference space are well-defined.

**(iii) Minimized Representation (Definition 8):** Each component produces the minimal number of distinct training outputs. No component encodes more information than is necessary to maintain correct training predictions.

**Theorem 2 (Alternative formulation):** When the definition of compositional generalization is augmented to include the requirement that all test component inputs must have been observed during training (rolling Assumption 1 into the definition itself), the same three conditions remain necessary and sufficient without needing the external assumption.

The necessity is proven via **Proposition 1**: Under Assumption 1 (test component inputs seen in training), the trained hypothesis graph set itself serves as a reference graph set when all training samples are correctly predicted. The three conditions then follow from the properties of bijective mappings (Lemma 1).

The sufficiency is proven via **Proposition 2**: Using bottom-up induction over the graph (Lemma 2 as the inductive step), structural alignment + one-to-one mappings (which follow from unambiguous + minimized representation by Lemma 1) guarantee that correct predictions propagate from training to test samples.

---

### 6. How Computational Graph Alignment Relates to Compositional Structure

Compositional structure is defined by the reference graph set Z, which represents how the true target function decomposes into sub-functions organized in a DAG. The model cannot directly observe this structure -- it is a latent property of the task.

**Structural alignment** requires the model's hypothesis graph H to be isomorphic to Z: there must be a bijection between node sets that preserves all edge (dependency) relationships. This means:
- If the true function is y = (x1 XOR x2) XOR x3, the reference graph has a hierarchical structure: first compute z = x1 XOR x2, then compute y = z XOR x3
- A structurally aligned model must have a corresponding two-stage architecture: component f_h processing (x1, x2) to produce h, then component f_y processing (h, x3) to produce y-hat
- A flat fully-connected network processing all three inputs simultaneously **violates** structural alignment

The paper demonstrates through the ablation study that without structural alignment, even with perfect data and regularization, test accuracy drops to 0%. The reason is fundamental: a flat model sees test samples as entirely novel input combinations in its weight space, while a hierarchically structured model decomposes them into familiar sub-computations.

The critical practical implication stated in the paper: "compositional generalization fundamentally requires prior knowledge of the target compositional hierarchy." Structural alignment cannot be learned purely from data -- it must be injected as an inductive bias through architecture design.

For attention mechanisms (Definition 9), the paper shows they can satisfy structural alignment because attention's commutative summation operation (Attention(U,V) = sum_i u_i * v_i) makes representations "effectively equal" under permutation, allowing dynamic input ordering while preserving component determinism.

---

### 7. What "Minimal Sufficient Information" Means in Their Framework

"Minimized representation" (Definition 8) is the paper's formalization of what we might call "minimal sufficient information." It requires that each component produces the **minimum number of distinct training outputs** -- no more information than is strictly necessary to maintain correct training predictions.

**Why minimization matters -- the Goldilocks principle:**
- **Too much information** (no minimization): Components encode spurious correlations and incidental features that happen to vary across training samples. These are unreliable under distribution shift -- novel test combinations may have different spurious patterns, causing failures.
- **Too little information** (over-compression): Components lose information needed for downstream composition, making correct predictions impossible.
- **Just right** (minimized): Components encode exactly the information needed to distinguish inputs that must be distinguished, and nothing more.

**Formal mechanism:** By Lemma 1, a well-defined onto mapping between finite sets is bijective if and only if the domain has minimal cardinality (no redundant elements). Minimized representation ensures the domain (set of distinct hypothesis values) has no redundant elements, which combined with unambiguous representation (well-definedness) yields a **bijection** between hypothesis and reference values. This bijection is what makes the inductive step in the sufficiency proof work.

**Implementation via information bottleneck:** The paper formalizes this through a Gaussian channel with power constraint (Definition 10):
- Channel equation: Y = X + Z, where Z ~ N(0, N)
- Power constraint: (1/n) sum(x_i^2) <= P
- Implementation: h' = h + N(0, alpha) [noise injection] and L' = L + beta||h||^2 [L2 activity regularization]

The noise forces representations that are close together to merge (they become indistinguishable through the noise), while the power constraint limits the dynamic range. Together, they push the number of distinct outputs toward the minimum. Hyperparameters alpha and beta control the compression strength.

**Natural tendency toward minimization:** The paper also observes (Section 5.3) that neural network training **implicitly** tends toward minimized representations because networks with fewer distinct input patterns at intermediate layers converge faster during gradient descent. This provides a partial explanation for why some standard networks occasionally succeed at compositional tasks even without explicit regularization.

---

### 8. Implications for Skill-Graph-Guided Training Data Synthesis

The paper's framework has direct and significant implications for training data synthesis, particularly in the context of skill-graph-guided approaches like the STEPS framework (Wei et al., arXiv:2601.03676, January 2026).

**From Definition 4 (Reference Graph Set):** The requirement that "all test component inputs are seen in training" provides a precise **data coverage criterion**. For each component in the skill graph, all input combinations that will appear at test time must appear at least once during training. This is not about covering all raw input combinations (which is exponential), but about covering all **component-level** input combinations (which can be much smaller due to the hierarchical decomposition).

**Concrete example from the paper:** For y = (x1 XOR x2) XOR x3:
- A naive approach would require covering all 2^3 = 8 input combinations
- The compositional approach requires: (a) all 4 combinations of (x1, x2) for the first component, and (b) all 4 combinations of (z, x3) for the second component, where z is in {0,1}
- The paper shows that 6 training samples suffice (not all 8), because the coverage requirement is at the component level

**Implications for skill taxonomy approaches:**

1. **The skill graph IS the reference graph:** If we interpret "skills" as components and the skill taxonomy/hierarchy as the reference graph, then Li's theorem directly prescribes what training data must cover. Each skill (component) must see all its input combinations that will appear during evaluation.

2. **Coverage at the right granularity:** The paper's framework explains why approaches like STEPS, which organize skills into hierarchical taxonomies and maximize information-theoretic diversity within the hierarchy, are on the right track. The key is ensuring component-level coverage, not raw input coverage.

3. **Unambiguous representation as a data quality criterion:** Training data must not contain ambiguous samples -- cases where the same intermediate skill representation could correspond to different ground-truth skill states. This provides a formal criterion for data quality beyond mere coverage.

4. **The minimization principle guides data efficiency:** Because the goal is minimal representation, training data should encourage components to encode only essential distinctions. This aligns with the STEPS paper's use of structural information theory to select skill combinations that maximize *marginal structural information* -- essentially maximizing the information that matters while keeping representations compact.

5. **Architecture must align with skill graph:** No amount of data synthesis can compensate for a mismatch between model architecture and skill hierarchy. This is a strong constraint: the model's computational structure must be designed to mirror the skill graph before data synthesis can be effective.

---

### Summary of the Paper's Core Contribution

Li (2505.02627) provides the first **complete characterization** (both necessary and sufficient) of when neural networks can achieve compositional generalization. The three-part condition -- structural alignment, unambiguous representation, and minimized representation -- unifies architecture design, data requirements, and regularization into a single coherent framework. The ablation study on a minimal XOR task demonstrates that each condition is independently essential: removing any one causes complete failure. The framework provides both theoretical foundations and practical design principles: use modular architectures matching the compositional hierarchy, ensure training data covers all component-level input combinations without ambiguity, and apply information-bottleneck-style regularization to minimize component representations.

The paper's intellectual lineage traces through Wiedemer et al. (NeurIPS 2023), who provided sufficient-only conditions, and Jarvis et al. (2023) and Lippl & Stachenfeld (2025), who identified limitations of existing approaches. Li's contribution closes the loop by showing exactly what is needed -- no more, no less -- for compositional generalization to occur.

---

Sources:
- [Li (2505.02627) - Abstract page](https://arxiv.org/abs/2505.02627)
- [Li (2505.02627) - Full HTML](https://arxiv.org/html/2505.02627v1)
- [Wiedemer et al. - Compositional Generalization from First Principles (NeurIPS 2023)](https://openreview.net/forum?id=LqOQ1uJmSx)
- [Wei et al. - STEPS: Skill Taxonomy Guided Data Synthesis (2601.03676)](https://arxiv.org/abs/2601.03676)
- [Yuanpeng Li - OpenReview Profile](https://openreview.net/profile?id=~Yuanpeng_Li2)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8e532726-585d-4bdd-9b9e-a32723f7f94d",
  "isSidechain": true,
  "agentId": "ac264cfb0150d4e15",
  "requestId": "req_011CbWKDXRs8p2ekfU4oQULQ",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "f7e8fad8-ac8f-4b86-aafe-92be3b772ffc",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "bd21c8ef-b139-4bde-afcd-7b4dbdab2a90",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01A2NHtE7WgUCZjxhLbT2NZS",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1463,
      "cache_read_input_tokens": 20143,
      "output_tokens": 3913,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1463
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 3913,
          "cache_read_input_tokens": 20143,
          "cache_creation_input_tokens": 1463,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1463,
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
