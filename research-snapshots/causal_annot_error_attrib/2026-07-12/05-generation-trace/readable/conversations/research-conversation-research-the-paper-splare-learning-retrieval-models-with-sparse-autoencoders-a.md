# Research conversation: Research the paper "SPLARE: Learning Retrieval Models with Sparse Autoencoders" (arXiv 2603.13277, 2026). 1. Use WebFetc

**Multi-Class Annotation Errors in Causal Inference: Topology-Dependent Bias, Sensitivity, and Correction (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 25
- **Recorded user turns:** 1
- **Tool calls:** 9
- **Original source:** `logs/chats/exported-trajectories/account-2/agent-afee5f8039c748a86.jsonl`
- **Structured JSON:** [`28f04ac6c35d10fb5f40.json`](../../sessions/28/28f04ac6c35d10fb5f40.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

25 recorded events

### User

_source line 1 · 2026-05-30T06:20:58.802Z_

Research the paper "SPLARE: Learning Retrieval Models with Sparse Autoencoders" (arXiv 2603.13277, 2026).

1. Use WebFetch to read the arxiv abstract page: https://arxiv.org/abs/2603.13277
2. Use WebFetch to read the HTML version for method details: https://arxiv.org/html/2603.13277
3. Search the web for any discussion or reviews of SPLARE sparse autoencoder retrieval.

Extract:
- The exact gap/problem they identified with SPLADE-style vocabulary-space projection
- Their key insight: using sparse autoencoders (SAEs) to decompose LLM representations into interpretable latent features
- Method details: how the sparse autoencoder is trained, how it replaces vocabulary projection, architecture
- Why this is more language-agnostic than SPLADE
- Results: SPLARE-7B performance on MMTEB multilingual and English retrieval benchmarks
- How this differs from traditional SPLADE approaches
- Any limitations or open questions

Be thorough with technical details about the SAE architecture and training procedure.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "0500c16e-7ea2-407e-bfcd-63f5d6e1769a",
  "agentId": "afee5f8039c748a86",
  "type": "user",
  "uuid": "60685317-a66d-47d4-8a2a-6e274dcefe80",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "71c77089-edc5-4f43-b783-1817930f1119",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 2 · 2026-05-30T06:20:58.806Z_

```json
{
  "parentUuid": "60685317-a66d-47d4-8a2a-6e274dcefe80",
  "isSidechain": true,
  "agentId": "afee5f8039c748a86",
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
  "uuid": "25119690-c763-46b1-9a19-06ae87926fe2",
  "timestamp": "2026-05-30T06:20:58.806Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "71c77089-edc5-4f43-b783-1817930f1119",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 3 · 2026-05-30T06:20:58.807Z_

```json
{
  "parentUuid": "25119690-c763-46b1-9a19-06ae87926fe2",
  "isSidechain": true,
  "agentId": "afee5f8039c748a86",
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "9c26bc52-fdd1-4ce6-ae56-963d83e74b1d",
  "timestamp": "2026-05-30T06:20:58.807Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "71c77089-edc5-4f43-b783-1817930f1119",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Assistant

_source line 4 · 2026-05-30T06:21:01.613Z_



I'll research this paper thoroughly. Let me start by fetching the tools and then the paper content.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9c26bc52-fdd1-4ce6-ae56-963d83e74b1d",
  "isSidechain": true,
  "agentId": "afee5f8039c748a86",
  "requestId": "req_011CbYGdcPbNwUPyoiJsMJSX",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "8f31aa2d-9cbc-4bf5-a9c0-42f891371de0",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "71c77089-edc5-4f43-b783-1817930f1119",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BEEqVKHCWvPZaMyXvotUpy",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1597,
      "cache_read_input_tokens": 7413,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1597,
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

_source line 5 · 2026-05-30T06:21:01.792Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01HxVdhLwrKjAcU8vYjoKyKP`</summary>

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
  "parentUuid": "8f31aa2d-9cbc-4bf5-a9c0-42f891371de0",
  "isSidechain": true,
  "agentId": "afee5f8039c748a86",
  "requestId": "req_011CbYGdcPbNwUPyoiJsMJSX",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "5c6c7dba-6553-46d1-aa3c-b3a030120e10",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "71c77089-edc5-4f43-b783-1817930f1119",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BEEqVKHCWvPZaMyXvotUpy",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1597,
      "cache_read_input_tokens": 7413,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1597,
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

### Tool result

_source line 6 · 2026-05-30T06:21:01.796Z_

<details><summary>↩ Tool result · `toolu_01HxVdhLwrKjAcU8vYjoKyKP`</summary>

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
  "parentUuid": "5c6c7dba-6553-46d1-aa3c-b3a030120e10",
  "isSidechain": true,
  "promptId": "0500c16e-7ea2-407e-bfcd-63f5d6e1769a",
  "agentId": "afee5f8039c748a86",
  "type": "user",
  "uuid": "73d8ebb8-2f25-4a42-a18e-88512302a7ba",
  "sourceToolAssistantUUID": "5c6c7dba-6553-46d1-aa3c-b3a030120e10",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "71c77089-edc5-4f43-b783-1817930f1119",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 7 · 2026-05-30T06:21:04.280Z_



Now let me fetch the paper from multiple sources in parallel.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "73d8ebb8-2f25-4a42-a18e-88512302a7ba",
  "isSidechain": true,
  "agentId": "afee5f8039c748a86",
  "requestId": "req_011CbYGdqPgtv69891kvrkLo",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "24906dcd-2db2-43b2-b3a4-55626dd06b43",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "71c77089-edc5-4f43-b783-1817930f1119",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WU8eQ5JHUrAXTqGqBaHMgL",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1124,
      "cache_read_input_tokens": 9010,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1124,
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

_source line 8 · 2026-05-30T06:21:06.387Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01GNCkCoEjRjPfDvPrEFEoyP`</summary>

```json
{
  "url": "https://arxiv.org/abs/2603.13277",
  "prompt": "Extract ALL information from this arxiv abstract page: the full title, all authors, the complete abstract text, submission date, and any other metadata. Be thorough and capture every detail."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "24906dcd-2db2-43b2-b3a4-55626dd06b43",
  "isSidechain": true,
  "agentId": "afee5f8039c748a86",
  "requestId": "req_011CbYGdqPgtv69891kvrkLo",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "f5ce8f8f-d64a-4948-9d50-917a541facbf",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "71c77089-edc5-4f43-b783-1817930f1119",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WU8eQ5JHUrAXTqGqBaHMgL",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1124,
      "cache_read_input_tokens": 9010,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1124,
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

### Tool result

_source line 9 · 2026-05-30T06:21:11.127Z_

<details><summary>↩ Tool result · `toolu_01GNCkCoEjRjPfDvPrEFEoyP`</summary>

```text
# arxiv Paper Information

**Full Title:** "Learning Retrieval Models with Sparse Autoencoders"

**Authors:**
- Thibault Formal
- Maxime Louis
- Hervé Dejean
- Stéphane Clinchant

**Submission Date:** February 27, 2026

**arXiv Identifier:** 2603.13277

**Subject Categories:** Machine Learning (cs.LG); Artificial Intelligence (cs.AI); Information Retrieval (cs.IR)

**Journal Reference:** ICLR 2026

**DOI:** https://doi.org/10.48550/arXiv.2603.13277

**License:** CC BY-NC-ND 4.0

---

## Abstract Summary

The paper proposes using sparse autoencoders (SAEs) as a foundation for learned sparse retrieval systems. Rather than projecting content into vocabulary space like existing methods, the researchers introduce SPLARE, which produces "more semantically structured, expressive, and language-agnostic features." Their SPLARE-7B model demonstrated superior performance in multilingual and cross-domain retrieval benchmarks on MMTEB, with a lighter 2B-parameter variant also developed.

**Key Innovation:** Leveraging SAE-based representations to decompose LLM outputs into interpretable latent features optimized for efficient information retrieval.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f5ce8f8f-d64a-4948-9d50-917a541facbf",
  "isSidechain": true,
  "promptId": "0500c16e-7ea2-407e-bfcd-63f5d6e1769a",
  "agentId": "afee5f8039c748a86",
  "type": "user",
  "uuid": "5f1f19db-db02-4bfb-8457-25baeb301a01",
  "sourceToolAssistantUUID": "f5ce8f8f-d64a-4948-9d50-917a541facbf",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "71c77089-edc5-4f43-b783-1817930f1119",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 10 · 2026-05-30T06:21:14.527Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_016YtQjFjCP67HugAHwrAbmH`</summary>

```json
{
  "url": "https://arxiv.org/html/2603.13277",
  "prompt": "Extract ALL technical details from this paper. I need:\n\n1. The exact problem/gap they identify with SPLADE-style vocabulary-space projection approaches\n2. Their key insight about using sparse autoencoders (SAEs) to decompose LLM representations\n3. Full method details: how the sparse autoencoder is trained, architecture details (encoder, decoder, activation functions, dimensions), how it replaces vocabulary projection, the full SPLARE pipeline\n4. Why this approach is more language-agnostic than SPLADE\n5. All experimental results: SPLARE-7B performance on MMTEB multilingual benchmarks, English retrieval benchmarks, any ablation studies\n6. How SPLARE differs from traditional SPLADE approaches\n7. Any limitations, open questions, or future work mentioned\n8. Training procedure details: loss functions, datasets used, hyperparameters\n9. Any figures or tables with key results\n10. The interpretability analysis of learned features\n\nBe extremely thorough and capture every technical detail, equation, and result number."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5f1f19db-db02-4bfb-8457-25baeb301a01",
  "isSidechain": true,
  "agentId": "afee5f8039c748a86",
  "requestId": "req_011CbYGdqPgtv69891kvrkLo",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "3d749b50-e166-4f3b-b1d9-b52f9ea6bb53",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "71c77089-edc5-4f43-b783-1817930f1119",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WU8eQ5JHUrAXTqGqBaHMgL",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1124,
      "cache_read_input_tokens": 9010,
      "output_tokens": 481,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1124
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 481,
          "cache_read_input_tokens": 9010,
          "cache_creation_input_tokens": 1124,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1124,
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

### Tool call

_source line 11 · 2026-05-30T06:21:15.000Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_011XikTrwFCXdwP1jbAaWGDR`</summary>

```json
{
  "query": "SPLARE sparse autoencoder retrieval arXiv 2603.13277 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3d749b50-e166-4f3b-b1d9-b52f9ea6bb53",
  "isSidechain": true,
  "agentId": "afee5f8039c748a86",
  "requestId": "req_011CbYGdqPgtv69891kvrkLo",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "5ec435a0-6a8a-455e-94b5-d03fd82191cf",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "71c77089-edc5-4f43-b783-1817930f1119",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WU8eQ5JHUrAXTqGqBaHMgL",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1124,
      "cache_read_input_tokens": 9010,
      "output_tokens": 481,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1124
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 481,
          "cache_read_input_tokens": 9010,
          "cache_creation_input_tokens": 1124,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1124,
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

_source line 12 · 2026-05-30T06:21:23.924Z_

<details><summary>↩ Tool result · `toolu_011XikTrwFCXdwP1jbAaWGDR`</summary>

```text
Web search results for query: "SPLARE sparse autoencoder retrieval arXiv 2603.13277 2026"

Links: [{"title":"[2603.13277] Learning Retrieval Models with Sparse Autoencoders","url":"https://arxiv.org/abs/2603.13277"},{"title":"Learning Retrieval Models with Sparse Autoencoders","url":"https://arxiv.org/html/2603.13277"},{"title":"Sparse Auto-Encoder Visual Word Scoring for Image ...","url":"https://arxiv.org/pdf/2603.05781"},{"title":"Learning Retrieval Models with Sparse Autoencoders | OpenReview","url":"https://openreview.net/forum?id=TuFjICawSc"},{"title":"Visual Words Meet BM25: Sparse Auto-Encoder Visual Word Scoring for Image Retrieval","url":"https://arxiv.org/html/2603.05781"},{"title":"Decoding Dense Embeddings: Sparse Autoencoders for Interpreting and Discretizing Dense Retrieval","url":"https://arxiv.org/pdf/2506.00041"},{"title":"Interpret and Control Dense Retrieval with Sparse Latent Features","url":"https://arxiv.org/pdf/2411.00786"}]

Based on the search results, here's what I found about SPLARE:

## Overview

SPLARE is a method to train SAE-based learned sparse retrieval (LSR) models. Sparse autoencoders (SAEs) decompose dense representations from Large Language Models into interpretable latent features and constitute a natural foundation for Learned Sparse Retrieval, whose objective is to encode queries and documents into high-dimensional sparse representations optimized for efficient retrieval.

## Key Advantages

SAE-based representations offer the potential to produce more semantically structured, expressive, and language-agnostic features compared to existing LSR approaches that project input sequences into the vocabulary space. The technique consistently outperforms vocabulary-based LSR in multilingual and out-of-domain settings.

## Model Architecture

A pre-trained SAE can be inserted at any layer of the LLM to get sparse latent representations of input tokens, which are then aggregated into a single sparse vector using a pooling mechanism analogous to SPLADE. During training, only the LLM parameters (via LoRA adapters) are fine-tuned while keeping the SAE frozen.

## Results

SPLARE-7B is a multilingual retrieval model capable of producing generalizable sparse latent embeddings for a wide range of languages and domains and achieves top results on MMTEB's multilingual and English retrieval tasks, with a 2B-parameter variant also developed.

The paper was posted on February 27, 2026.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "5ec435a0-6a8a-455e-94b5-d03fd82191cf",
  "isSidechain": true,
  "promptId": "0500c16e-7ea2-407e-bfcd-63f5d6e1769a",
  "agentId": "afee5f8039c748a86",
  "type": "user",
  "uuid": "4e08999f-afbb-4dc3-b233-3b0bf1c725e4",
  "sourceToolAssistantUUID": "5ec435a0-6a8a-455e-94b5-d03fd82191cf",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "71c77089-edc5-4f43-b783-1817930f1119",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 13 · 2026-05-30T06:21:52.081Z_

<details><summary>↩ Tool result · `toolu_016YtQjFjCP67HugAHwrAbmH`</summary>

````text
# Technical Details: Learning Retrieval Models with Sparse Autoencoders

## Problem/Gap Identified

Existing Learned Sparse Retrieval (LSR) methods like SPLADE project representations onto the vocabulary space, creating fundamental limitations:

- **Vocabulary Constraint**: Fixed vocabulary creates "tokenization redundancy" and poor performance on multilingual/cross-lingual retrieval
- **Language Specificity**: Vocabulary-based approaches struggle with languages outside their training distribution
- **Multilingual Generalization**: No sparse retrieval models ranked on MTEB (Multilingual, v2) leaderboard at paper submission

The authors note: "Unlike dense retrieval, which models relevance within a continuous embedding space, LSR methods are inherently constrained by the fixed vocabulary of their underlying backbone."

## Key Insight: SAE-Based Decomposition

Instead of vocabulary projection, use pre-trained Sparse Autoencoders to decompose dense LLM token representations into interpretable latent features. These features exhibit desirable properties:

- **Monosemanticity**: Most features correspond to single interpretable concepts
- **Language-Agnostic**: Largely invariant across languages
- **Multimodal**: Generalize across modalities in multimodal LLMs

## Full Method Details: SPLARE Architecture

### SAE Mathematical Foundation

Standard SAE equations:
```
z = f(W_enc * x + b_enc)
x̂ = W_dec * z + b_dec
```

Where:
- x ∈ ℝ^d: Activations from LLM layer
- z ∈ ℝ^|W|: Latent representation (width >> d)
- f: Activation function (ReLU, Top-K, or JumpReLU)
- Reconstruction loss: L = ||x̂ - x||²
- Sparsity induced via activation functions and ℓ₁ regularization

### SPLARE Pipeline

**Key Difference from SPLADE**: Replace LM head projection with SAE encoder:

1. **Layer Selection**: Apply SAE encoder at intermediate transformer layer (optimally ~2/3 model depth)
2. **Token-Level Features**: Extract sparse latent logits (w₁, w₂, ..., wₙ) from hidden states
3. **Sequence Aggregation**: Apply identical pooling to SPLADE—"SPLADE-pool":

```
u_j = max_{i=1...n} log(1 + ReLU(v_ij)), j ∈ W
```

Where W represents the latent feature space instead of vocabulary V.

4. **Relevance Scoring**: Sparse dot product: s(q,d) = &lt;u_q, u_d>

### Why Language-Agnostic

- SAEs trained on residual streams exhibit "language-agnostic" responses to conceptual content
- Features activate consistently across languages for same semantic content
- Not constrained by subword tokenization artifacts
- Latent vocabulary (131k features for Llama Scope) provides richer semantic grounding than fixed vocabulary

## Training Procedure

### Loss Function (Equation 3-4)

**Distillation-based approach** using cross-encoder teacher:

KL divergence between teacher and student relevance distributions:
```
L_KL = Σ_i p_i (log p_i - log p̂_i)

where:
p̂_i = e^s(q,d_i)/τ / Σ_j e^s(q,d_j)/τ  [student]
p_i = e^s_i / Σ_j e^s_j                  [teacher]
```

**Combined Loss**:
```
L = L_KL + λ_q * ℓ_FLOPS^q + λ_d * ℓ_FLOPS^d
```

Rationale: Distillation addresses false negatives in contrastive learning; aligns with SPLADE training practices.

### Sparsity Control

- **Training**: FLOPS loss with fixed λ values (λ_q = λ_d = 0.0001)
- **Inference**: Top-K pooling applied post-hoc
  - Default: k=40 (queries), k=400 (documents)
  - Allows single model to achieve various sparsity levels without retraining

### Architecture Modifications

- **LoRA Fine-tuning**: Freeze SAE parameters; fine-tune LLM backbone with LoRA rank=64
- **Bidirectional Attention**: Enable across all layers; crucial for position-wise pooling
- **Masked Language Modeling Pretraining**: 20% token masking on MS MARCO, 10k steps (~5 hours)

### Hyperparameters (Table 4)

| Parameter | Value |
|-----------|-------|
| Learning Rate | 5×10⁻⁵ |
| Batch Size | 128 |
| Temperature τ (Llama Scope) | 80 |
| Temperature τ (Gemma Scope) | 50 |
| Max Sequence Length (English) | 128 |
| Max Sequence Length (Multilingual) | 512 |
| Negatives per Query | 8 |
| Epochs | 1 |

Temperature critical and SAE-suite-dependent; grid search over {1, 10, 20, 40, 50, 80, 100}.

## Core Experimental Results

### SPLARE-7B Performance on Multilingual Tasks

**MMTEB (Multilingual, v2) Retrieval** (Table 3):
- **Average Score**: 62.3 nDCG@10
- **Ranking**: Top-10 models; top-1 LSR model
- **English Score**: 59.3 nDCG@10
- Comparison context: NV-Embed-v2 (56.7), gte-Qwen2-7B-instruct (60.1)

**MIRACL Dataset** (Table 11):
- **Average**: 71.7 nDCG@10
- SPLARE-7B outperforms M3-Embeddings (hybrid dense+sparse): +0.2 points
- State-of-the-art on 8 languages (English, Finnish, Hindi, Japanese, Russian, Swahili, German, Yoruba)
- Strong performance on "secret" languages (German, Yoruba) without training data

**XTREME-UP** (Low-Resource Languages, Table 12):
- **Score**: 58.6 MRR@10 vs. Gemini Embedding (64.3), SPLADE-Llama (56.2)
- Especially strong on low-resource Indic languages (+2.4 vs. SPLADE-Llama)

### English-Only Results (Table 1)

**MS MARCO Training Results**:
- SPLARE: 52.9 (tied with SPLADE-Llama baseline)
- Multilingual-trained SPLARE: 59.3 on English

**Out-of-Domain Multilingual**:
- Multilingual MTEB: +0.6 points vs. SPLADE-Llama (62.3 vs. 61.7)
- Multilingual-only datasets: +0.9 points (Table 8)

**Domain-Specific Performance** (Multilingual models):
- Medical: 67.7 (+0.1) — strong generalization
- Law: 60.8 (+0.1) — consistent
- Code: 63.0 (-1.3) — weakness identified
- Chemical: 78.1 (+0.7)

### Ablation Studies

#### Layer Depth Analysis (Figure 1 Left)

Optimal performance at intermediate layers:
- **Llama-3.1-8B** (32 layers): Peak at layer 20-22
- **Gemma-2-2B** (26 layers): Peak at layer 16-17
- Pattern: ~2/3 model depth provides best effectiveness-efficiency tradeoff
- SPLARE inference advantage: Only processes to intermediate layer vs. SPLADE (all layers)

#### SAE Width Scaling (Figure 1 Right)

**Log-linear relationship** between SAE width and retrieval effectiveness:
- Widths tested: 2¹⁴≈16k to 2²⁰≈1M on Gemma-2
- Consistent across layers 12 and 19
- Llama Scope (131k width) outperforms wider Gemma Scope variants

**Key Advantage**: Unlike SPLADE's fixed vocabulary, SAE width provides scaling mechanism for improved performance.

#### Robustness to Sparsification (Figure 2 Left)

**Top-K document pooling impact**:
- **SPLARE (Top-K=100)**: -2% performance drop
- **SPLADE (Top-K=100)**: -6% performance drop

**Feature Space Utilization** (Figure 2 Right):
- SPLARE activates nearly all 131k dimensions
- SPLADE activates <100k out of 128k vocabulary
- SPLARE exhibits balanced activation distribution; SPLADE concentrates on small feature subset

#### Lexical vs. Latent Features (Table 1)

English-only trained models on English MTEB:
- SPLARE: 52.9 = SPLADE-Llama: 52.9 (equivalent)
- Divergence on multilingual/out-of-domain tasks supports language-agnostic hypothesis

## Limitations Identified

### Domain-Specific Performance Gap

Code retrieval underperformance (-1.3 MTEB Code):
- Authors note: "Top activated features appear overly generic rather than specialized to code semantics"
- Solution suggested: "Dedicated SAEs trained on code-focused corpora may be more appropriate"

Example from Appendix G: SPLARE features on code tasks lack domain-specific semantic grounding.

### SAE Transfer Challenges

Acknowledged limitation: "SAEs can struggle to transfer effectively to certain downstream tasks" (citing recent negative results on downstream task performance).

## Interpretability Analysis

### Mechanistic Interpretation via Neuronpedia

Figure 3 (Tamil→English XTREME-UP example):
- SPLARE features: Coherent, language-agnostic concepts
  - Feature activations: "historical/cultural contexts" (10.5%), "India mentions" (8.7%), "casualties" (7.5%)
  - Document rank: 4
- SPLADE tokens: Redundant (separate "Indian" and "indian"), Latin-script dependent
  - Token activations: Scattered across language-specific variants
  - Document rank: 23

**Key Finding**: SPLARE provides higher-level semantic coherence; SPLADE defaults to surface-level token overlap.

Feature explanations sourced from Llama/Gemma Scope's publicly available Neuronpedia annotations.

## Training Data

### English Setting
- **Dataset**: MS MARCO
- **Hard Negatives**: Mined via SPLADE model
- **Distillation Targets**: DeBERTa-v3 reranker scores
- **Purpose**: Controlled SPLARE vs. SPLADE-Llama comparison

### Multilingual Setting
- **Dataset**: BGE multilingual training set (1.3M queries after filtering)
- **Sources**: 
  - English: MS MARCO, NQ, HotpotQA
  - Chinese: Large collection of Chinese retrieval datasets
  - Multilingual: MIRACL, Mr.TyDi
- **Teacher Scores**: BGE-reranker-v2-m3
- **Note**: Some tasks overlap MTEB benchmarks; acknowledged limitation on strict generalization evaluation

## Key Technical Innovations

1. **SAE Insertion at Intermediate Layers**: Reduces inference cost while maintaining/improving effectiveness
2. **Top-K Inference-Time Pooling**: Decouples sparsity control from training, enabling single model versatility
3. **Frozen SAE + LoRA Fine-tuning**: Preserves interpretability of latent feature space
4. **Distillation-based Training**: Addresses false negatives better than contrastive learning for sparse representations

## Efficiency Metrics

**MS MARCO Retrieval** (8.8M documents):
- Per-query latency: ~5ms (Top-K=(40,400)) without model inference
- Low-latency regime (<4ms): SPLARE outperforms SPLADE accuracy
- Measured with Seismic library using approximate query processing

## Future Work/Open Questions

1. Domain-specific SAEs for code/specialized domains
2. Scaling to larger SAE widths (up to 14M features noted as possible on large LLMs)
3. Multimodal extension of SPLARE
4. Integration with approximate sparse retrieval algorithms
5. Cross-modal sparse latent retrieval

## Models Released

- **SPLARE-7B**: 7B-parameter Llama-3.1-8B backbone, multilingual, 131k latent dimensions
- **SPLARE-2B**: 2B-parameter variant (Gemma-2-2B backbone, layer 6), lighter footprint, 65k latent dimensions
- Both available with frozen Llama/Gemma Scope SAEs from public sources
````

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "3d749b50-e166-4f3b-b1d9-b52f9ea6bb53",
  "isSidechain": true,
  "promptId": "0500c16e-7ea2-407e-bfcd-63f5d6e1769a",
  "agentId": "afee5f8039c748a86",
  "type": "user",
  "uuid": "0be370b4-9643-4fac-9343-a8ef0f0a58ff",
  "sourceToolAssistantUUID": "3d749b50-e166-4f3b-b1d9-b52f9ea6bb53",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "71c77089-edc5-4f43-b783-1817930f1119",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 14 · 2026-05-30T06:21:55.155Z_

Let me also fetch the OpenReview page for any reviews/discussion, and search for additional community discussion.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0be370b4-9643-4fac-9343-a8ef0f0a58ff",
  "isSidechain": true,
  "agentId": "afee5f8039c748a86",
  "requestId": "req_011CbYGhYGQp6xaaajcSsQnH",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "b52f2145-b2ce-4cdb-af42-7966ddd796f4",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "71c77089-edc5-4f43-b783-1817930f1119",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017ekwfvD4CnKrFdZp4FA8bk",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 698,
      "cache_creation_input_tokens": 4037,
      "cache_read_input_tokens": 10134,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4037,
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

_source line 15 · 2026-05-30T06:21:57.153Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01SoYRbEhHppM1Kev2d2HEP2`</summary>

```json
{
  "url": "https://openreview.net/forum?id=TuFjICawSc",
  "prompt": "Extract all reviews, reviewer comments, scores, criticisms, and discussion about this paper. Include reviewer ratings, strengths identified, weaknesses identified, questions raised, and any author responses. Be thorough."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b52f2145-b2ce-4cdb-af42-7966ddd796f4",
  "isSidechain": true,
  "agentId": "afee5f8039c748a86",
  "requestId": "req_011CbYGhYGQp6xaaajcSsQnH",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "d54497bd-6ef1-42ef-b7f2-e84058f848d0",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "71c77089-edc5-4f43-b783-1817930f1119",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017ekwfvD4CnKrFdZp4FA8bk",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 698,
      "cache_creation_input_tokens": 4037,
      "cache_read_input_tokens": 10134,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4037,
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

_source line 16 · 2026-05-30T06:21:57.615Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_019EM3K8ZvpEkRxytKGwww1S`</summary>

```json
{
  "query": "SPLARE \"sparse autoencoder\" retrieval SPLADE ICLR 2026 discussion review"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d54497bd-6ef1-42ef-b7f2-e84058f848d0",
  "isSidechain": true,
  "agentId": "afee5f8039c748a86",
  "requestId": "req_011CbYGhYGQp6xaaajcSsQnH",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "8b2978e5-f9af-4b3b-bcef-51a561cbf66e",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "71c77089-edc5-4f43-b783-1817930f1119",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017ekwfvD4CnKrFdZp4FA8bk",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 698,
      "cache_creation_input_tokens": 4037,
      "cache_read_input_tokens": 10134,
      "output_tokens": 210,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 4037
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 698,
          "output_tokens": 210,
          "cache_read_input_tokens": 10134,
          "cache_creation_input_tokens": 4037,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 4037,
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

_source line 17 · 2026-05-30T06:22:00.252Z_

<details><summary>↩ Tool result · `toolu_01SoYRbEhHppM1Kev2d2HEP2`</summary>

```text
# Review Analysis: "Learning Retrieval Models with Sparse Autoencoders"

Based on the provided webpage content, **no reviews, reviewer comments, scores, criticisms, or discussion are available**. 

The page displays only the paper's metadata and abstract, including:
- Publication date (26 Jan 2026)
- Author names
- Keywords and TL;DR
- Abstract describing the research

The webpage indicates that "Revisions" are available via a link, but the actual review content, peer feedback, ratings, strengths, weaknesses, or author responses are not included in the extracted text.

To access this information, you would need to:
1. Visit the full OpenReview page directly
2. Click the "Revisions" tab
3. Navigate to review sections (if visible on the page)
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d54497bd-6ef1-42ef-b7f2-e84058f848d0",
  "isSidechain": true,
  "promptId": "0500c16e-7ea2-407e-bfcd-63f5d6e1769a",
  "agentId": "afee5f8039c748a86",
  "type": "user",
  "uuid": "d5a549a6-95d4-4817-b387-5adcf2e0bd95",
  "sourceToolAssistantUUID": "d54497bd-6ef1-42ef-b7f2-e84058f848d0",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "71c77089-edc5-4f43-b783-1817930f1119",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-30T06:22:04.967Z_

<details><summary>↩ Tool result · `toolu_019EM3K8ZvpEkRxytKGwww1S`</summary>

```text
Web search results for query: "SPLARE "sparse autoencoder" retrieval SPLADE ICLR 2026 discussion review"

Links: [{"title":"Learning Retrieval Models with Sparse Autoencoders | OpenReview","url":"https://openreview.net/forum?id=TuFjICawSc"},{"title":"Naver Labs Europe @ WSDM CUP | Multilingual Retrieval","url":"https://arxiv.org/html/2602.20986"},{"title":"January, 2025 Naver Labs Europe @ WSDM CUP | Multilingual Retrieval","url":"https://arxiv.org/pdf/2602.20986"},{"title":"LEARNING RETRIEVAL MODELS WITH SPARSE ...","url":"https://openreview.net/pdf/d972ecd5f0e44502efe64ca31ab04d653121a803.pdf"},{"title":"[2603.13277] Learning Retrieval Models with Sparse Autoencoders","url":"https://arxiv.org/abs/2603.13277"},{"title":"Learning Retrieval Models with Sparse Autoencoders","url":"https://arxiv.org/html/2603.13277"},{"title":"SPLADE: Sparse Lexical and Expansion Model for First Stage Ranking | Proceedings of the 44th International ACM SIGIR Conference on Research and Development in Information Retrieval","url":"https://dl.acm.org/doi/10.1145/3404835.3463098"},{"title":"Decoding Dense Embeddings: Sparse Autoencoders for Interpreting and Discretizing Dense Retrieval","url":"https://arxiv.org/pdf/2506.00041"}]

Based on the search results, here's what I found about SPLARE and related research:

## SPLARE Overview

SPLARE is a 7B-parameter multilingual retrieval model capable of producing generalizable sparse latent embeddings for a wide range of languages and domains, achieving top results on MMTEB's multilingual and English retrieval tasks.

## Technical Approach

Sparse autoencoders (SAEs) provide a mechanism for decomposing dense representations from Large Language Models into interpretable latent features, and constitute a natural foundation for Learned Sparse Retrieval (LSR), which aims to encode queries and documents into high-dimensional sparse representations optimized for efficient retrieval.

In contrast to existing LSR approaches that project input sequences into the vocabulary space, SAE-based representations offer the potential to produce more semantically structured, expressive, and language-agnostic features.

## Comparison with SPLADE

Compared to equivalent SPLADE models operating over a fixed LLM vocabulary, SPLARE demonstrates consistently stronger performance, particularly on multilingual retrieval benchmarks such as MIRACL and cross-lingual tasks.

## Venue

The SPLARE paper appears on OpenReview with a submission date of October 8, 2025, suggesting it's being reviewed for a major venue, though the search results don't explicitly confirm ICLR 2026 as the submission venue.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "8b2978e5-f9af-4b3b-bcef-51a561cbf66e",
  "isSidechain": true,
  "promptId": "0500c16e-7ea2-407e-bfcd-63f5d6e1769a",
  "agentId": "afee5f8039c748a86",
  "type": "user",
  "uuid": "dc4c210c-a4e5-4760-99ca-64e5cccc344d",
  "sourceToolAssistantUUID": "8b2978e5-f9af-4b3b-bcef-51a561cbf66e",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "71c77089-edc5-4f43-b783-1817930f1119",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-30T06:22:08.163Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01VF2hatWE4XAsWQ7jTwY2Wc`</summary>

```json
{
  "query": "SPLARE-7B Thibault Formal Naver Labs sparse retrieval 2026 blog"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "dc4c210c-a4e5-4760-99ca-64e5cccc344d",
  "isSidechain": true,
  "agentId": "afee5f8039c748a86",
  "requestId": "req_011CbYGiVKLYXbRDG5AzAbBt",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "f88d2875-cd0f-405a-bcd8-2cc6f28c1d41",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "71c77089-edc5-4f43-b783-1817930f1119",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KAV8w2LuBBQBc7hbCoMVJS",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1892,
      "cache_read_input_tokens": 14171,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1892,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 39,
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

_source line 20 · 2026-05-30T06:22:08.537Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_019sucCCXc93jj4CMNy3wcp5`</summary>

```json
{
  "query": "\"sparse autoencoder\" \"learned sparse retrieval\" language-agnostic multilingual MMTEB 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f88d2875-cd0f-405a-bcd8-2cc6f28c1d41",
  "isSidechain": true,
  "agentId": "afee5f8039c748a86",
  "requestId": "req_011CbYGiVKLYXbRDG5AzAbBt",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "3f495bee-8156-4c49-8800-2e19936a623a",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "71c77089-edc5-4f43-b783-1817930f1119",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KAV8w2LuBBQBc7hbCoMVJS",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1892,
      "cache_read_input_tokens": 14171,
      "output_tokens": 135,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1892
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 135,
          "cache_read_input_tokens": 14171,
          "cache_creation_input_tokens": 1892,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1892,
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

_source line 21 · 2026-05-30T06:22:14.963Z_

<details><summary>↩ Tool result · `toolu_01VF2hatWE4XAsWQ7jTwY2Wc`</summary>

```text
Web search results for query: "SPLARE-7B Thibault Formal Naver Labs sparse retrieval 2026 blog"

Links: [{"title":"(PDF) Naver Labs Europe @ WSDM CUP | Multilingual Retrieval","url":"https://www.researchgate.net/publication/401178441_Naver_Labs_Europe_WSDM_CUP_Multilingual_Retrieval"},{"title":"[2602.20986] Naver Labs Europe @ WSDM CUP | Multilingual Retrieval","url":"https://arxiv.org/abs/2602.20986"},{"title":"January, 2025 Naver Labs Europe @ WSDM CUP | Multilingual Retrieval","url":"https://arxiv.org/pdf/2602.20986"},{"title":"[2603.13277] Learning Retrieval Models with Sparse Autoencoders","url":"https://arxiv.org/abs/2603.13277"},{"title":"Naver Labs Europe @ WSDM CUP | Multilingual Retrieval","url":"https://arxiv.org/html/2602.20986v1"},{"title":"GitHub - naver/splade: SPLADE: sparse neural search (SIGIR21, SIGIR22)","url":"https://github.com/naver/splade?tab=readme-ov-file"},{"title":"GitHub - naver/splade: SPLADE: sparse neural search (SIGIR21, SIGIR22) · GitHub","url":"https://github.com/naver/splade"}]

I found relevant results about SPLARE-7B and Thibault Formal's work with Naver Labs. Here's what I discovered:

Thibault Formal and colleagues from Naver Labs Europe participated in the WSDM Cup 2026 shared task on multilingual document retrieval from English queries. SPLARE is their recently proposed learned sparse retrieval model that produces generalizable sparse latent representations well-suited to multilingual retrieval, and they evaluated five progressively enhanced runs starting from a SPLARE-7B model with improvements including reranking with Qwen3-Reranker-4B and score fusion strategies.

SPLARE-7B is a multilingual retrieval model capable of producing generalizable sparse latent embeddings for a wide range of languages and domains, achieving top results on MMTEB's multilingual and English retrieval tasks. The experiments demonstrate that SPLARE achieves performance comparable to leading dense embedding models such as Qwen3-8B-Embed.

The search results include academic papers from arxiv.org (posted in February 2026) describing this work, rather than a traditional blog post. The papers are authored by Thibault Formal, Maxime Louis, Hervé Déjean, and Stéphane Clinchant from Naver Labs Europe.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f88d2875-cd0f-405a-bcd8-2cc6f28c1d41",
  "isSidechain": true,
  "promptId": "0500c16e-7ea2-407e-bfcd-63f5d6e1769a",
  "agentId": "afee5f8039c748a86",
  "type": "user",
  "uuid": "cc0f6219-389d-4d19-8a77-dbe09b2dd666",
  "sourceToolAssistantUUID": "f88d2875-cd0f-405a-bcd8-2cc6f28c1d41",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "71c77089-edc5-4f43-b783-1817930f1119",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 22 · 2026-05-30T06:22:16.061Z_

<details><summary>↩ Tool result · `toolu_019sucCCXc93jj4CMNy3wcp5`</summary>

```text
Web search results for query: ""sparse autoencoder" "learned sparse retrieval" language-agnostic multilingual MMTEB 2026"

Links: [{"title":"[2603.13277] Learning Retrieval Models with Sparse Autoencoders","url":"https://arxiv.org/abs/2603.13277"},{"title":"Learning Retrieval Models with Sparse Autoencoders | OpenReview","url":"https://openreview.net/forum?id=TuFjICawSc"},{"title":"Learning Retrieval Models with Sparse Autoencoders","url":"https://arxiv.org/html/2603.13277"},{"title":"Naver Labs Europe @ WSDM CUP | Multilingual Retrieval","url":"https://arxiv.org/html/2602.20986v1"},{"title":"LEARNING RETRIEVAL MODELS WITH SPARSE ...","url":"https://openreview.net/pdf/4dea76491cda15ab41c8e1ac4699debf57bf2458.pdf"},{"title":"Milco: Learned Sparse Retrieval Across Languages via a Multilingual Connector","url":"https://arxiv.org/html/2510.00671v2"},{"title":"Milco: Learned Sparse Retrieval Across Languages via a Multilingual Connector","url":"https://arxiv.org/pdf/2510.00671"}]

I found relevant research on this topic. Here are the key findings:

## Sparse Autoencoders and Learned Sparse Retrieval

Sparse autoencoders (SAEs) decompose dense representations from Large Language Models into interpretable latent features and constitute a natural foundation for Learned Sparse Retrieval (LSR), which encodes queries and documents into high-dimensional sparse representations optimized for efficient retrieval.

SAE-based representations offer the potential to produce more semantically structured, expressive, and language-agnostic features compared to existing LSR approaches that project input sequences into the vocabulary space.

## SPLARE Model and MMTEB Performance

SPLARE-7B, a multilingual retrieval model capable of producing generalizable sparse latent embeddings for a wide range of languages and domains, achieves top results on MMTEB's multilingual and English retrieval tasks. This SAE-based LSR technique consistently outperforms vocabulary-based LSR in multilingual and out-of-domain settings.

SPLARE is a 7B-parameter multilingual retrieval model with a more efficient 2B-parameter variant, both offering strong performance with varying computational footprints.

The research was published in early 2026, with the arxiv submission dated February 27, 2026.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "3f495bee-8156-4c49-8800-2e19936a623a",
  "isSidechain": true,
  "promptId": "0500c16e-7ea2-407e-bfcd-63f5d6e1769a",
  "agentId": "afee5f8039c748a86",
  "type": "user",
  "uuid": "eb78c968-5d95-4d15-9395-c563036daf77",
  "sourceToolAssistantUUID": "3f495bee-8156-4c49-8800-2e19936a623a",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "71c77089-edc5-4f43-b783-1817930f1119",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 23 · 2026-05-30T06:22:23.931Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01Teh95ZEwzzRHiTQp9RJevE`</summary>

```json
{
  "url": "https://arxiv.org/html/2602.20986v1",
  "prompt": "Extract all details about SPLARE-7B's use in the WSDM Cup competition. How did it perform? What improvements were made on top of it? What were the results? Include any comparison to other systems."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "eb78c968-5d95-4d15-9395-c563036daf77",
  "isSidechain": true,
  "agentId": "afee5f8039c748a86",
  "requestId": "req_011CbYGjJdvG1ySKkMEhBex8",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "092c2752-c4f3-4672-927b-80e94500517c",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "71c77089-edc5-4f43-b783-1817930f1119",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KhP4KxbCgEEkrpuiekno2H",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1545,
      "cache_read_input_tokens": 16063,
      "output_tokens": 130,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1545
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 130,
          "cache_read_input_tokens": 16063,
          "cache_creation_input_tokens": 1545,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1545,
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

_source line 24 · 2026-05-30T06:22:29.638Z_

<details><summary>↩ Tool result · `toolu_01Teh95ZEwzzRHiTQp9RJevE`</summary>

```text
# SPLARE-7B Performance in WSDM Cup 2026

## Baseline Performance

SPLARE-7B served as the foundation for Run 1, achieving an nDCG@20 score of 0.498 on the development set. This represented a substantial improvement, with the system demonstrating "+7.5 nDCG@20 over Qwen3-8B-Embed."

The researchers chose non-pooled representations over the pooled variant (Top-K=40,400), sacrificing efficiency for maximum effectiveness. The non-pooled version scored 0.498 versus 0.471 with pooling.

## Subsequent Enhancements

**Run 2 (Fusion):** SPLARE-7B was combined with SPLADE-8B using Reciprocal Rank Fusion, yielding 0.517 nDCG@20.

**Run 3 (Reranking):** Qwen3-Reranker-4B was applied to the top 100 candidates from Run 1, improving performance to 0.545.

**Run 4 & 5:** Additional fusion and reranking iterations progressively enhanced results, with the final configuration (Run 5) achieving 0.559 nDCG@20.

## Key Comparisons

SPLARE substantially outperformed competing baselines including MILCO (0.395) and PLAID-X (0.396), while surpassing the dense Qwen3-8B-Embed baseline (0.423).
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "092c2752-c4f3-4672-927b-80e94500517c",
  "isSidechain": true,
  "promptId": "0500c16e-7ea2-407e-bfcd-63f5d6e1769a",
  "agentId": "afee5f8039c748a86",
  "type": "user",
  "uuid": "838e6951-8888-4d59-bf8a-217834e595cf",
  "sourceToolAssistantUUID": "092c2752-c4f3-4672-927b-80e94500517c",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "71c77089-edc5-4f43-b783-1817930f1119",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 25 · 2026-05-30T06:24:01.942Z_

Now I have comprehensive information. Here is the full research synthesis:

---

## SPLARE: Learning Retrieval Models with Sparse Autoencoders (arXiv 2603.13277)

**Authors:** Thibault Formal, Maxime Louis, Herve Dejean, Stephane Clinchant (Naver Labs Europe)
**Venue:** ICLR 2026 | Submitted October 8, 2025; arXiv February 27, 2026

---

### 1. The Problem with SPLADE-Style Vocabulary-Space Projection

SPLADE and other Learned Sparse Retrieval (LSR) methods project LLM representations onto the **vocabulary space** -- essentially using the language model head to produce a sparse vector where each dimension corresponds to a token in the model's wordpiece vocabulary. The authors identify several fundamental limitations:

- **Fixed vocabulary constraint:** LSR methods are "inherently constrained by the fixed vocabulary of their underlying backbone." The vocabulary was designed for tokenization, not for representing semantic concepts.
- **Tokenization redundancy:** Multiple vocabulary tokens encode the same semantic concept (e.g., "Indian" and "indian" as separate dimensions), wasting representational capacity.
- **Language specificity:** Subword tokenizers are heavily biased toward the languages dominant in pretraining data. Low-resource languages get poor coverage, leading to fragmented and semantically incoherent sparse representations.
- **Multilingual failure:** At the time of submission, **no sparse retrieval model appeared on the MTEB Multilingual v2 leaderboard** -- a stark indicator that vocabulary-based LSR had fundamentally failed to generalize across languages.
- **Fixed dimensionality:** The vocabulary size is locked at whatever the backbone model uses (e.g., 128k for Llama-3.1), with no mechanism to scale representation capacity.

---

### 2. Key Insight: SAEs Decompose LLM Representations into Language-Agnostic Semantic Features

The central insight draws from the **mechanistic interpretability** literature. Sparse autoencoders (SAEs), when trained on LLM residual stream activations, decompose dense hidden states into interpretable latent features that exhibit several properties ideal for retrieval:

- **Monosemanticity:** Most SAE features correspond to a single, coherent concept (e.g., "casualties in conflict," "references to India"), unlike individual neurons which are polysemantic.
- **Language-agnosticism:** SAE features activate consistently for the same semantic content regardless of input language. A feature for "historical/cultural contexts" fires on Tamil, English, and German text alike.
- **Scalability:** SAE width (number of latent features) can be scaled independently of the LLM vocabulary -- from 16k to over 1M features -- providing a tunable knob for representational capacity.

The authors' key realization: if SAEs already produce sparse, interpretable, language-agnostic features from LLM hidden states, they are a **natural replacement** for vocabulary projection in sparse retrieval.

---

### 3. Method Details: The SPLARE Architecture

#### 3.1 SAE Mathematical Foundation

A standard sparse autoencoder maps an LLM hidden state **x** in R^d to a high-dimensional sparse latent **z** in R^|W| (where |W| >> d):

```
z = f(W_enc * x + b_enc)       [encoder]
x_hat = W_dec * z + b_dec       [decoder/reconstruction]
```

The SAE is trained to minimize reconstruction loss ||x_hat - x||^2 with sparsity induced through the activation function f (ReLU, Top-K, or JumpReLU) and L1 regularization. The authors use **pre-trained, publicly available SAEs** (Llama Scope for Llama-3.1-8B with 131k features; Gemma Scope for Gemma-2-2B with 65k features).

#### 3.2 SPLARE Pipeline (Replacing Vocabulary Projection)

The pipeline mirrors SPLADE but swaps out the LM head for an SAE encoder:

1. **Forward pass to intermediate layer:** Process input tokens through the LLM backbone, but only up to an intermediate layer (optimally ~2/3 depth -- layer 20-22 for Llama-3.1-8B's 32 layers, layer 16-17 for Gemma-2-2B's 26 layers). This is a computational advantage since SPLADE must run the full model.

2. **SAE encoding:** Apply the frozen SAE encoder to each token's hidden state, producing sparse latent logits (v_i1, v_i2, ..., v_i|W|) for each token i.

3. **SPLADE-style pooling ("SPLADE-pool"):** Aggregate token-level features into a single document/query vector using max-pooling with log-saturation:
   ```
   u_j = max_{i=1...n} log(1 + ReLU(v_ij)),  for j in W (latent feature space)
   ```
   This is identical to SPLADE's pooling, but over the SAE latent space W instead of vocabulary V.

4. **Scoring:** Standard sparse dot product: s(q, d) = &lt;u_q, u_d>

#### 3.3 Training Procedure

**What is trained vs. frozen:**
- **SAE:** Completely frozen (preserves interpretability and language-agnostic properties)
- **LLM backbone:** Fine-tuned with **LoRA** (rank=64) to adapt hidden states for retrieval
- **Bidirectional attention:** Enabled across all LLM layers (critical for position-wise pooling)

**Pre-training step:** Masked Language Modeling (20% token masking) on MS MARCO for 10k steps (~5 hours). This adapts the LLM to bidirectional attention before retrieval fine-tuning.

**Loss function -- distillation-based:**
```
L = L_KL + lambda_q * L_FLOPS^q + lambda_d * L_FLOPS^d
```

Where L_KL is the KL divergence between a cross-encoder teacher's relevance distribution and the student's:
```
p_hat_i = exp(s(q, d_i)/tau) / sum_j exp(s(q, d_j)/tau)   [student, temperature-scaled]
p_i = exp(s_i) / sum_j exp(s_j)                             [teacher]
```

The FLOPS regularizer controls sparsity (lambda_q = lambda_d = 0.0001). Distillation was chosen over contrastive learning because it better handles false negatives.

**Key hyperparameters:**
- Learning rate: 5e-5
- Batch size: 128
- Temperature tau: 80 (Llama Scope), 50 (Gemma Scope) -- selected via grid search over {1, 10, 20, 40, 50, 80, 100}; critically important and SAE-suite-dependent
- Negatives per query: 8
- Epochs: 1
- Max sequence length: 128 (English), 512 (multilingual)

**Inference-time sparsity control -- Top-K pooling:**
After training, a Top-K selection is applied: keep only the top k=40 features for queries and k=400 for documents. This decouples sparsity from training, allowing a single trained model to operate at multiple sparsity levels without retraining.

**Training data:**
- English setting: MS MARCO with DeBERTa-v3 reranker distillation targets
- Multilingual setting: BGE multilingual training set (1.3M queries from MS MARCO, NQ, HotpotQA, Chinese retrieval datasets, MIRACL, Mr.TyDi) with BGE-reranker-v2-m3 as teacher

---

### 4. Why SPLARE Is More Language-Agnostic Than SPLADE

Several reinforcing factors:

1. **SAE features transcend tokenization:** SPLADE's dimensions are vocabulary tokens -- inherently language-specific surface forms. SPLARE's dimensions are learned semantic concepts that activate identically across languages.

2. **Empirical evidence from interpretability research:** The authors cite work showing SAE features on residual streams are "largely invariant across languages" -- the same feature fires for "casualties" whether the input is in Tamil, English, or Yoruba.

3. **No tokenization artifacts:** SPLADE wastes capacity on redundant tokens ("Indian" vs. "indian") and fragments low-resource language words into meaningless subwords. SPLARE operates at the concept level.

4. **Concrete example (Figure 3):** On a Tamil-to-English retrieval task from XTREME-UP, SPLARE's top features are coherent concepts ("historical/cultural contexts," "India mentions," "casualties") that match across languages. SPLADE produces scattered Latin-script tokens that fail cross-lingually. SPLARE ranks the correct document 4th; SPLADE ranks it 23rd.

5. **Performance on unseen languages:** SPLARE achieves state-of-the-art on "secret" languages in MIRACL (German, Yoruba) that had zero training data, demonstrating genuine cross-lingual transfer rather than memorization.

---

### 5. Results

#### MMTEB Multilingual Retrieval (Table 3)
- **SPLARE-7B: 62.3 nDCG@10** -- top-10 overall on the leaderboard, and the **#1 learned sparse retrieval model**
- For context: NV-Embed-v2 scores 56.7, gte-Qwen2-7B-instruct scores 60.1
- English subset: 59.3 nDCG@10

#### MIRACL (18-language benchmark, Table 11)
- **SPLARE-7B: 71.7 nDCG@10 average**
- Outperforms M3-Embeddings (hybrid dense+sparse) by +0.2 points
- State-of-the-art on 8 individual languages: English, Finnish, Hindi, Japanese, Russian, Swahili, German, Yoruba
- Strong on "secret" (zero-shot) languages: German, Yoruba

#### XTREME-UP (Low-Resource Languages, Table 12)
- SPLARE-7B: 58.6 MRR@10 (vs. Gemini Embedding 64.3, SPLADE-Llama 56.2)
- Especially strong on low-resource Indic languages: +2.4 over SPLADE-Llama

#### English-Only (MS MARCO training, Table 1)
- SPLARE: 52.9 = SPLADE-Llama: 52.9 (identical on English when both trained on English data only)
- The divergence appears on multilingual/out-of-domain tasks, confirming the language-agnostic advantage

#### Domain-Specific (multilingual models)
- Medical: 67.7 (+0.1 vs SPLADE), Law: 60.8 (+0.1), Chemical: 78.1 (+0.7)
- Code: 63.0 (-1.3) -- a notable weakness

#### WSDM Cup 2026 Multilingual Retrieval
- SPLARE-7B (non-pooled) achieved 0.498 nDCG@20, which was **+7.5 nDCG@20 over Qwen3-8B-Embed** (0.423)
- With fusion and reranking enhancements, reached 0.559 nDCG@20
- Substantially outperformed MILCO (0.395) and PLAID-X (0.396)

---

### 6. How SPLARE Differs from Traditional SPLADE

| Aspect | SPLADE | SPLARE |
|--------|--------|--------|
| Projection space | Vocabulary (128k tokens) | SAE latent space (65k-131k+ features) |
| Dimension semantics | Subword tokens | Monosemantic concepts |
| Scalability | Fixed by vocabulary | SAE width scales independently (log-linear improvement) |
| Multilingual | Poor (tokenizer-dependent) | Strong (language-agnostic features) |
| Inference depth | Full model forward pass | Intermediate layer only (~2/3 depth) |
| Sparsity control | Trained into model | Post-hoc Top-K (single model, multiple sparsity levels) |
| Robustness to sparsification | -6% at Top-K=100 | -2% at Top-K=100 |
| Feature utilization | <100k of 128k vocab activated | Nearly all 131k features utilized |

---

### 7. Key Ablation Findings

- **Layer depth:** Optimal SAE insertion is at ~2/3 model depth. This also provides an inference speedup since later layers are never computed.
- **SAE width:** Log-linear relationship between width and retrieval effectiveness (tested 16k to 1M on Gemma-2). Wider SAEs consistently improve performance.
- **Robustness to sparsification:** SPLARE degrades only 2% when aggressively pruning to Top-K=100 document features, versus 6% for SPLADE. SPLARE's activation distribution is more balanced across features.
- **Feature utilization:** SPLARE activates nearly all 131k dimensions across the corpus; SPLADE concentrates activation on a small subset of the 128k vocabulary, wasting capacity.

---

### 8. Limitations and Open Questions

1. **Code retrieval underperformance (-1.3 vs SPLADE):** The authors find that top-activated features on code tasks "appear overly generic rather than specialized to code semantics." They suggest domain-specific SAEs trained on code-focused corpora may be needed.

2. **SAE transfer challenges:** The authors acknowledge recent work showing SAEs can struggle to transfer to certain downstream tasks. The frozen SAE may not always capture the right features for every domain.

3. **Training data overlap:** The multilingual training set (BGE) overlaps with some MTEB benchmark tasks, complicating strict generalization claims.

4. **Temperature sensitivity:** The distillation temperature tau is critically important and SAE-suite-dependent (80 for Llama Scope, 50 for Gemma Scope), requiring careful tuning.

5. **Future directions mentioned:** Domain-specific SAEs for specialized domains; scaling to very large SAE widths (up to 14M features on large LLMs); multimodal extension of SPLARE; cross-modal sparse latent retrieval; integration with approximate sparse retrieval algorithms.

---

### Sources

- [SPLARE Paper - arXiv Abstract](https://arxiv.org/abs/2603.13277)
- [SPLARE Paper - Full HTML](https://arxiv.org/html/2603.13277)
- [OpenReview Submission](https://openreview.net/forum?id=TuFjICawSc)
- [Naver Labs Europe @ WSDM Cup](https://arxiv.org/abs/2602.20986)
- [SPLADE GitHub (Naver)](https://github.com/naver/splade)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "838e6951-8888-4d59-bf8a-217834e595cf",
  "isSidechain": true,
  "agentId": "afee5f8039c748a86",
  "requestId": "req_011CbYGkJrqsDmfvPSouWTAP",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "c0de9194-c29f-4ab3-9571-0068b3fb87ab",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "71c77089-edc5-4f43-b783-1817930f1119",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VA2XADJN6oN2zBonJh7WcR",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 495,
      "cache_read_input_tokens": 17608,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 495,
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
