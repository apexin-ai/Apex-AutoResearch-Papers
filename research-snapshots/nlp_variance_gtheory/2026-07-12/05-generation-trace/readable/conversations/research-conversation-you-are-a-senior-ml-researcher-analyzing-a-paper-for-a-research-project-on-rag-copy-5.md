# Research conversation: You are a senior ML researcher analyzing a paper for a research project on RAG circuit tracing in LLMs. Paper: "How Tran

**Reproducibility Budgets for Open-Weight LLM Evaluation: A Generalizability Theory Study of 7–9B Instruction-Tuned Models (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 31
- **Recorded user turns:** 1
- **Tool calls:** 11
- **Original source:** `logs/chats/exported-trajectories/account-2/agent-a2899b2126e594028.jsonl`
- **Structured JSON:** [`539a7a56f6306a6b0772.json`](../../sessions/53/539a7a56f6306a6b0772.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

31 recorded events

### User

_source line 1 · 2026-05-30T06:19:45.858Z_

You are a senior ML researcher analyzing a paper for a research project on RAG circuit tracing in LLMs.

Paper: "How Transformers Reject Wrong Answers: Rotational Dynamics of Factual Constraint Processing" by Javier Marín. arXiv 2026. URL: https://arxiv.org/abs/2603.13259

Tasks:
1. Use WebFetch to read the arxiv abstract page for this paper.
2. Use WebFetch to read the full PDF at https://arxiv.org/pdf/2603.13259
3. This is an arXiv preprint so no formal reviews, but search for any discussion or citations (search "rotational dynamics factual constraint processing transformers 2026").

For each fetch, extract:
- Abstract and introduction: What gap did they identify? How?
- Method section: What is the technical approach? What existing techniques did they adapt/combine?
- Key insight that others missed
- How they formulated the problem differently

Report all findings in detail. I need specifics about:
- The rotational dynamics framework — what does "rotation not rescaling" mean concretely?
- The approximate hypersphere finding
- Active suppression of correct answers — how is this measured/demonstrated?
- The 1.6B parameter emergence threshold
- Connection to the "flip phenomenon" where correct answers appear mid-layers then get suppressed
- Any geometric/mathematical formalism they use

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "355ad2bb-a24a-42aa-9911-1293fa95f808",
  "agentId": "a2899b2126e594028",
  "type": "user",
  "uuid": "be5da377-afa8-41af-9a38-dea7b5454733",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "867e4b99-e4d4-402e-8b5a-1d69a93e0fb6",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 2 · 2026-05-30T06:19:45.861Z_

```json
{
  "parentUuid": "be5da377-afa8-41af-9a38-dea7b5454733",
  "isSidechain": true,
  "agentId": "a2899b2126e594028",
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
      "TaskCreate",
      "TaskGet",
      "TaskList",
      "TaskStop",
      "TaskUpdate",
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
      "TaskCreate",
      "TaskGet",
      "TaskList",
      "TaskStop",
      "TaskUpdate",
      "WebFetch",
      "WebSearch"
    ],
    "removedNames": [],
    "readdedNames": []
  },
  "type": "attachment",
  "uuid": "f2f8d131-9c7f-432d-a2c9-f5d2860319f7",
  "timestamp": "2026-05-30T06:19:45.861Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "867e4b99-e4d4-402e-8b5a-1d69a93e0fb6",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 3 · 2026-05-30T06:19:45.861Z_

```json
{
  "parentUuid": "f2f8d131-9c7f-432d-a2c9-f5d2860319f7",
  "isSidechain": true,
  "agentId": "a2899b2126e594028",
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "7798404d-cff7-4ebf-a59d-0d1a518bd1e7",
  "timestamp": "2026-05-30T06:19:45.861Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "867e4b99-e4d4-402e-8b5a-1d69a93e0fb6",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Assistant

_source line 4 · 2026-05-30T06:19:48.849Z_



I'll fetch the arxiv abstract page, the full PDF, and search for discussions about this paper in parallel.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7798404d-cff7-4ebf-a59d-0d1a518bd1e7",
  "isSidechain": true,
  "agentId": "a2899b2126e594028",
  "requestId": "req_011CbYGYEX4e5ptkzaBNc5zy",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "286cd41e-2eb6-4c7f-af51-9bf4457a275d",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "867e4b99-e4d4-402e-8b5a-1d69a93e0fb6",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PuSGWTTZrZfiK7BLz3xwqo",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1668,
      "cache_read_input_tokens": 7413,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1668,
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

_source line 5 · 2026-05-30T06:19:49.063Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_013tWc7en95qWvdu2YMiCbKm`</summary>

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
  "parentUuid": "286cd41e-2eb6-4c7f-af51-9bf4457a275d",
  "isSidechain": true,
  "agentId": "a2899b2126e594028",
  "requestId": "req_011CbYGYEX4e5ptkzaBNc5zy",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "cfa97233-5266-441c-b8e7-c210d1e913d1",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "867e4b99-e4d4-402e-8b5a-1d69a93e0fb6",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PuSGWTTZrZfiK7BLz3xwqo",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1668,
      "cache_read_input_tokens": 7413,
      "output_tokens": 104,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1668
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 104,
          "cache_read_input_tokens": 7413,
          "cache_creation_input_tokens": 1668,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1668,
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

_source line 6 · 2026-05-30T06:19:49.069Z_

<details><summary>↩ Tool result · `toolu_013tWc7en95qWvdu2YMiCbKm`</summary>

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
  "parentUuid": "cfa97233-5266-441c-b8e7-c210d1e913d1",
  "isSidechain": true,
  "promptId": "355ad2bb-a24a-42aa-9911-1293fa95f808",
  "agentId": "a2899b2126e594028",
  "type": "user",
  "uuid": "43ed49e4-4b94-410c-b9fe-186f3d3c2242",
  "sourceToolAssistantUUID": "cfa97233-5266-441c-b8e7-c210d1e913d1",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "867e4b99-e4d4-402e-8b5a-1d69a93e0fb6",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 7 · 2026-05-30T06:19:51.529Z_



Now I'll fetch the abstract page, the full PDF, and search for discussions in parallel.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "43ed49e4-4b94-410c-b9fe-186f3d3c2242",
  "isSidechain": true,
  "agentId": "a2899b2126e594028",
  "requestId": "req_011CbYGYUXBdRX6BwLwmWTrY",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "db80c60b-a082-4420-8f96-a90f846e31cb",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "867e4b99-e4d4-402e-8b5a-1d69a93e0fb6",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019VppcXj2GhwJN2szVyThTz",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1126,
      "cache_read_input_tokens": 9081,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1126,
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

_source line 8 · 2026-05-30T06:19:53.416Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01978yjUfd4PoTv467ie8tCH`</summary>

```json
{
  "url": "https://arxiv.org/abs/2603.13259",
  "prompt": "Extract the full abstract, authors, title, submission date, and any other metadata available on this arxiv page. Also extract any subject categories and comments listed."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "db80c60b-a082-4420-8f96-a90f846e31cb",
  "isSidechain": true,
  "agentId": "a2899b2126e594028",
  "requestId": "req_011CbYGYUXBdRX6BwLwmWTrY",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "5e3a2612-5593-4707-bdc0-dcb3665fa51f",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "867e4b99-e4d4-402e-8b5a-1d69a93e0fb6",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019VppcXj2GhwJN2szVyThTz",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1126,
      "cache_read_input_tokens": 9081,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1126,
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

_source line 9 · 2026-05-30T06:19:57.774Z_

<details><summary>↩ Tool result · `toolu_01978yjUfd4PoTv467ie8tCH`</summary>

```text
# Paper Metadata Extraction

**Title:** How Transformers Reject Wrong Answers: Rotational Dynamics of Factual Constraint Processing

**Author:** Javier Marín

**Submission Date:** February 25, 2026

**arXiv Identifier:** 2603.13259

**Subject Categories:** 
- Computation and Language (cs.CL)
- Artificial Intelligence (cs.AI)

**Abstract Summary:**
The research investigates internal network behavior when language models encounter incorrect answers. Using "forced-completion probing," the authors tracked geometric measurements across decoder-only models (1.5B-13B parameters). Key findings indicate that correct and incorrect processing paths diverge through rotational displacement rather than magnitude changes. The models actively suppress correct answers rather than passively failing. Additionally, these phenomena emerge only above a 1.6B parameter threshold, suggesting a phase transition in factual processing capabilities.

**License:** Creative Commons Attribution-ShareAlike 4.0

**DOI:** https://doi.org/10.48550/arXiv.2603.13259

**Access Formats:** PDF, HTML (experimental), and TeX source available
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "5e3a2612-5593-4707-bdc0-dcb3665fa51f",
  "isSidechain": true,
  "promptId": "355ad2bb-a24a-42aa-9911-1293fa95f808",
  "agentId": "a2899b2126e594028",
  "type": "user",
  "uuid": "4c2fba05-8bb6-4aa9-bdc6-dab0326cf671",
  "sourceToolAssistantUUID": "5e3a2612-5593-4707-bdc0-dcb3665fa51f",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "867e4b99-e4d4-402e-8b5a-1d69a93e0fb6",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 10 · 2026-05-30T06:20:00.172Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01KXq93qj8GL1dibgQTyiCcV`</summary>

```json
{
  "url": "https://arxiv.org/pdf/2603.13259",
  "prompt": "Extract the FULL content of this paper in as much detail as possible. I need:\n\n1. ABSTRACT - complete text\n2. INTRODUCTION - complete text, especially what gap they identify and how they frame the problem\n3. METHOD/APPROACH - complete technical details of their approach, including:\n   - The rotational dynamics framework\n   - What \"rotation not rescaling\" means\n   - The approximate hypersphere finding\n   - How they measure active suppression of correct answers\n   - Mathematical formalism and equations\n   - The geometric framework\n4. RESULTS - key findings including:\n   - The 1.6B parameter emergence threshold\n   - The \"flip phenomenon\" where correct answers appear mid-layers then get suppressed\n   - Any quantitative results\n5. DISCUSSION/CONCLUSION - implications and connections to other work\n6. REFERENCES - list key references they cite\n\nPlease be as detailed and complete as possible, preserving mathematical notation where feasible."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4c2fba05-8bb6-4aa9-bdc6-dab0326cf671",
  "isSidechain": true,
  "agentId": "a2899b2126e594028",
  "requestId": "req_011CbYGYUXBdRX6BwLwmWTrY",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "5bdb24b2-deca-4f7e-bc1e-3f289d0fff26",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "867e4b99-e4d4-402e-8b5a-1d69a93e0fb6",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019VppcXj2GhwJN2szVyThTz",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1126,
      "cache_read_input_tokens": 9081,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1126,
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

_source line 11 · 2026-05-30T06:20:01.090Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01UCvzRxRWkssRtRDiEV4g47`</summary>

```json
{
  "query": "rotational dynamics factual constraint processing transformers 2026 Javier Marín"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5bdb24b2-deca-4f7e-bc1e-3f289d0fff26",
  "isSidechain": true,
  "agentId": "a2899b2126e594028",
  "requestId": "req_011CbYGYUXBdRX6BwLwmWTrY",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "24d47ca5-adb6-42fa-b5a5-01d42bd16d9a",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "867e4b99-e4d4-402e-8b5a-1d69a93e0fb6",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019VppcXj2GhwJN2szVyThTz",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1126,
      "cache_read_input_tokens": 9081,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1126,
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

_source line 12 · 2026-05-30T06:20:07.802Z_

<details><summary>↩ Tool result · `toolu_01UCvzRxRWkssRtRDiEV4g47`</summary>

```text
Web search results for query: "rotational dynamics factual constraint processing transformers 2026 Javier Marín"

Links: [{"title":"[2603.13259] How Transformers Reject Wrong Answers: Rotational Dynamics of Factual Constraint Processing","url":"https://arxiv.org/abs/2603.13259"},{"title":"How Transformers Reject Wrong Answers: Rotational Dynamics of Factual Constraint Processing","url":"https://arxiv.org/pdf/2603.13259"},{"title":"Five-shot performance on Massive Multitask Language Understanding (MMLU). | Download Scientific Diagram","url":"https://www.researchgate.net/figure/Five-shot-performance-on-Massive-Multitask-Language-Understanding-MMLU_tbl1_372961198"},{"title":"How Transformers Reject Wrong Answers: Rotational Dynamics of Factual Constraint Processing","url":"https://arxiv.org/html/2603.13259"},{"title":"Rule guided transformers for dynamic knowledge adaptation in rotating machinery fault diagnosis - ScienceDirect","url":"https://www.sciencedirect.com/science/article/pii/S1474034626001369"},{"title":"Rotational Dynamics – Angular Momentum | Crack JEE 2026 ...","url":"https://www.facebook.com/Cengagelearningindia/videos/rotational-dynamics-angular-momentum-crack-jee-2026-physicsstrengthen-your-under/1525539342218746/"},{"title":"[2511.10654] Empirical Characterization of Temporal Constraint Processing in LLMs","url":"https://arxiv.org/abs/2511.10654"}]

Based on the search results, I found the paper you're looking for:

"How Transformers Reject Wrong Answers: Rotational Dynamics of Factual Constraint Processing" is a paper by Javier Marín from February 2026.

The key findings of the paper are:

1. Correct and incorrect paths diverge through rotation, not rescaling: displacement vectors maintain near-identical magnitudes while their angular separation increases, meaning factual selection is encoded in direction on an approximate hypersphere.

2. The model does not passively fail on incorrect input—it actively suppresses the correct answer, driving internal probability away from the right token.

3. Both phenomena are entirely absent below a parameter threshold and emerge at 1.6B, suggesting a phase transition in factual processing capability.

The research uses a method called forced-completion probing, which presents identical queries with known correct and incorrect single-token continuations and tracks five geometric measurements across every layer of four decoder-only models (1.5B–13B parameters).


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "24d47ca5-adb6-42fa-b5a5-01d42bd16d9a",
  "isSidechain": true,
  "promptId": "355ad2bb-a24a-42aa-9911-1293fa95f808",
  "agentId": "a2899b2126e594028",
  "type": "user",
  "uuid": "eba88d63-7e70-42c5-897e-6e4fc088b032",
  "sourceToolAssistantUUID": "24d47ca5-adb6-42fa-b5a5-01d42bd16d9a",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "867e4b99-e4d4-402e-8b5a-1d69a93e0fb6",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 13 · 2026-05-30T06:20:15.112Z_

<details><summary>↩ Tool result · `toolu_01KXq93qj8GL1dibgQTyiCcV`</summary>

```text
# Paper Extract: "How Transformers Reject Wrong Answers: Rotational Dynamics of Factual Constraint Processing"

**Author:** Javier Marín
**ArXiv ID:** 2603.13259v1
**License:** CC-BY-SA 4.0

## 1. ABSTRACT

The paper investigates how transformer models actively suppress incorrect answers during factual reasoning tasks. The authors discover that this rejection mechanism involves **rotational dynamics in representation space** rather than simple rescaling of logits. They identify an emergence threshold around 1.6B parameters where this sophisticated suppression behavior first appears.

## 2. INTRODUCTION

**The Problem Framing:**
The authors identify a gap between how transformers process factual information internally versus what gets output. While prior work (Burns et al. 2023, Azaria et al. 2023) examined where knowledge is stored, this work asks: *how do models actively prevent wrong answers from being selected?*

Key motivating observations:
- Transformers don't simply boost correct answer logits
- The mechanism involves suppression of competing incorrect options
- This behavior exhibits interesting scaling properties and emergent characteristics

## 3. METHODOLOGY

### 3.1 Rotational Dynamics Framework

The core insight: **"Rotation not rescaling"** - the transformation isn't merely amplifying logits but involves geometric rotation in embedding space.

**Mathematical Formalism:**

The authors model the answer rejection mechanism through:
- Hidden states at layer ℓ: h^(ℓ) ∈ ℝ^d
- Projection to approximate hypersphere followed by rotation
- The key equation involves rotating representations while maintaining approximate unit norm

**Approximate Hypersphere Finding:**
1. Identify a lower-dimensional hypersphere in the full d-dimensional space
2. Project representations onto this manifold
3. Measure rotation angles on this constrained surface
4. This provides geometric interpretation of how answers are "rejected"

### 3.2 Active Suppression Measurement

The authors quantify suppression through:
- **Geometric metrics:** angles between correct and incorrect answer embeddings
- **Layer-by-layer analysis:** tracking how separation evolves
- **The "flip phenomenon":** correct answers appear with high logits at intermediate layers but get actively suppressed in later layers

### 3.3 The Flip Phenomenon

Critical finding: In factual reasoning, correct answers often appear mid-layers with substantial probability, then are *actively suppressed* in subsequent layers. This contrasts with simple knowledge retrieval where answers monotonically improve.

## 4. RESULTS

### 4.1 Emergence Threshold: 1.6B Parameters

Models below ~1.6B parameters show:
- Simple monotonic improvement in answer logits
- Lack of active suppression behavior
- Cannot simultaneously boost correct while suppressing incorrect

Models at 1.6B+ show:
- Sophisticated rotation-based suppression
- Active rejection of wrong answers mid-computation
- Non-monotonic behavior (correct answers appear then get suppressed)

### 4.2 Key Quantitative Findings

**The Flip Pattern:**
- Correct answer logits increase in early-to-mid layers
- Intermediate layers: both correct and incorrect answers have elevated logits
- Final layers: correct answer boosted, incorrect answers rotated away
- Maximum entropy/uncertainty at the "flip point" where suppression begins

**Geometric Signatures:**
- Angular separation between correct/incorrect embeddings changes dramatically
- Rotation angles follow consistent patterns across different factual domains
- Hypersphere radius constraints predict when suppression occurs

### 4.3 Tested Models

Analysis includes:
- LLaMA models (various sizes)
- Mistral
- Qwen2
- Demonstrates consistency across architectures

## 5. DISCUSSION & IMPLICATIONS

**Theoretical Significance:**
The finding that factual reasoning involves *active suppression via rotation* rather than simple knowledge amplification suggests transformers implement constraint satisfaction mechanisms analogous to:
- Negation handling in logic systems
- Conflict resolution in attention patterns
- Multi-objective optimization

**Connections to Prior Work:**
- Extends Burns et al. (2023) on factual localization
- Complements Azaria et al. (2023) on internal knowledge representation
- Aligns with Marks et al. (2023) geometric perspectives on transformers
- Relates to Geva et al. (2023) on intermediate computations

**Practical Implications:**
- Understanding suppression helps explain why models sometimes output wrong answers despite "knowing" correct ones
- The 1.6B threshold suggests when models gain reasoning capability
- Provides framework for studying hallucinations and factual errors

## 6. KEY REFERENCES CITED

- Burns et al. (2023): "Discovering Latent Knowledge in Language Models"
- Azaria et al. (2023): "Internal Knowledge and Inference"
- Marks et al. (2023): "Geometry of Factual Knowledge"
- Geva et al. (2023): "Transformer Information Flow"
- Meng et al. (2022): "Locating Factual Knowledge"
- Li et al. (2023): "Inference Time"
- Belrose et al. (2023): "Eliciting Latent Knowledge"
- Nostalgebraist (2020): "Logit Lens" (foundational methodology)

---

**Note:** The paper represents a significant contribution to mechanistic interpretability, providing concrete evidence that transformer reasoning involves geometric transformation mechanisms beyond simple statistical associations.

[Binary content (application/pdf, 695.2KB) also saved to /home/ubuntu/.claude-account-2/projects/-home-ubuntu-idea-adversarial/867e4b99-e4d4-402e-8b5a-1d69a93e0fb6/tool-results/webfetch-1780122000186-sa34qc.pdf]
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "5bdb24b2-deca-4f7e-bc1e-3f289d0fff26",
  "isSidechain": true,
  "promptId": "355ad2bb-a24a-42aa-9911-1293fa95f808",
  "agentId": "a2899b2126e594028",
  "type": "user",
  "uuid": "2106b2ef-d895-4b11-bcaf-f606f0a1c495",
  "sourceToolAssistantUUID": "5bdb24b2-deca-4f7e-bc1e-3f289d0fff26",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "867e4b99-e4d4-402e-8b5a-1d69a93e0fb6",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 14 · 2026-05-30T06:20:18.602Z_

Good, I have the abstract page and a summary of the PDF. Let me now fetch the HTML version for more detailed content, and do additional searches for any community discussion or citations.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2106b2ef-d895-4b11-bcaf-f606f0a1c495",
  "isSidechain": true,
  "agentId": "a2899b2126e594028",
  "requestId": "req_011CbYGaPYM9sqqfo2fuH6yy",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "6d84f6d4-b59a-408c-8721-065de70c07f6",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "867e4b99-e4d4-402e-8b5a-1d69a93e0fb6",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PavESBuHnrrkLJsUfXUPJY",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 693,
      "cache_creation_input_tokens": 2146,
      "cache_read_input_tokens": 10207,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2146,
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

_source line 15 · 2026-05-30T06:20:25.182Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01RVTo2g5dxHN61hZhDpFPBL`</summary>

```json
{
  "url": "https://arxiv.org/html/2603.13259",
  "prompt": "Extract ALL content from this paper in maximum detail. I need every section, every equation, every figure description, every table. Specifically:\n\n1. The FULL introduction with all citations and problem framing\n2. ALL mathematical equations and formalism - especially:\n   - How they define the rotational dynamics\n   - The hypersphere projection\n   - Angular displacement metrics\n   - Any cosine similarity or angular separation formulas\n   - The five geometric measurements they track\n3. The forced-completion probing methodology in full detail\n4. ALL results including:\n   - Exact numbers for the flip phenomenon\n   - Layer-by-layer analysis details\n   - The 1.6B threshold evidence\n   - Which models were tested and exact results\n5. ALL figures and their descriptions\n6. The full discussion section\n7. Complete reference list\n\nBe as exhaustive as possible. Do not summarize - extract verbatim where possible."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6d84f6d4-b59a-408c-8721-065de70c07f6",
  "isSidechain": true,
  "agentId": "a2899b2126e594028",
  "requestId": "req_011CbYGaPYM9sqqfo2fuH6yy",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "145b59db-471f-4b55-b3b9-ebb1bed6deb7",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "867e4b99-e4d4-402e-8b5a-1d69a93e0fb6",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PavESBuHnrrkLJsUfXUPJY",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 693,
      "cache_creation_input_tokens": 2146,
      "cache_read_input_tokens": 10207,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2146,
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

_source line 16 · 2026-05-30T06:20:26.185Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_018P311GyxXK9XZxREgZ5dgj`</summary>

```json
{
  "query": "\"How Transformers Reject Wrong Answers\" \"rotational dynamics\" arxiv 2603.13259"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "145b59db-471f-4b55-b3b9-ebb1bed6deb7",
  "isSidechain": true,
  "agentId": "a2899b2126e594028",
  "requestId": "req_011CbYGaPYM9sqqfo2fuH6yy",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "5f72b013-e87e-4aba-87d8-95ccaebb7a3a",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "867e4b99-e4d4-402e-8b5a-1d69a93e0fb6",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PavESBuHnrrkLJsUfXUPJY",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 693,
      "cache_creation_input_tokens": 2146,
      "cache_read_input_tokens": 10207,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2146,
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

_source line 17 · 2026-05-30T06:20:26.577Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01FFSAJyW2omQdwHdfMNWqXc`</summary>

```json
{
  "query": "arxiv 2603.13259 citation discussion blog review \"flip phenomenon\" factual suppression"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5f72b013-e87e-4aba-87d8-95ccaebb7a3a",
  "isSidechain": true,
  "agentId": "a2899b2126e594028",
  "requestId": "req_011CbYGaPYM9sqqfo2fuH6yy",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "d32f3ac7-b26f-41eb-8da7-f0251a58b2ac",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "867e4b99-e4d4-402e-8b5a-1d69a93e0fb6",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PavESBuHnrrkLJsUfXUPJY",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 693,
      "cache_creation_input_tokens": 2146,
      "cache_read_input_tokens": 10207,
      "output_tokens": 433,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2146
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 693,
          "output_tokens": 433,
          "cache_read_input_tokens": 10207,
          "cache_creation_input_tokens": 2146,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2146,
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

_source line 18 · 2026-05-30T06:20:30.444Z_

<details><summary>↩ Tool result · `toolu_01FFSAJyW2omQdwHdfMNWqXc`</summary>

```text
Web search results for query: "arxiv 2603.13259 citation discussion blog review "flip phenomenon" factual suppression"

Links: [{"title":"[2603.13259] How Transformers Reject Wrong Answers: Rotational Dynamics of Factual Constraint Processing","url":"https://arxiv.org/abs/2603.13259"},{"title":"Exposing Attention Glitches with Flip-Flop Language Modeling","url":"https://arxiv.org/pdf/2306.00946"},{"title":"What the flip? What the P-N flip can tell us about proactive suppression","url":"https://www.biorxiv.org/content/10.1101/2022.03.04.483004.full.pdf"},{"title":"[2306.00946] Exposing Attention Glitches with Flip-Flop Language Modeling","url":"https://arxiv.org/abs/2306.00946"},{"title":"DSCC-HS: A Dynamic Self-Reinforcing Framework for Hallucination Suppression in Large Language Models","url":"https://arxiv.org/pdf/2509.13702"}]

I found the arXiv paper 2603.13259. The paper describes how correct and incorrect paths diverge through rotation, and finds that the model actively suppresses the correct answer when fed incorrect input, driving internal probability away from the right token.

However, the search results don't show blog reviews or discussions about this paper's "flip phenomenon." Would you like me to search more specifically for blog posts, citations, or discussions that reference this paper?


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d32f3ac7-b26f-41eb-8da7-f0251a58b2ac",
  "isSidechain": true,
  "promptId": "355ad2bb-a24a-42aa-9911-1293fa95f808",
  "agentId": "a2899b2126e594028",
  "type": "user",
  "uuid": "00bc8bff-d974-444f-96e3-8071f6204f65",
  "sourceToolAssistantUUID": "d32f3ac7-b26f-41eb-8da7-f0251a58b2ac",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "867e4b99-e4d4-402e-8b5a-1d69a93e0fb6",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 19 · 2026-05-30T06:20:33.245Z_

<details><summary>↩ Tool result · `toolu_018P311GyxXK9XZxREgZ5dgj`</summary>

```text
Web search results for query: ""How Transformers Reject Wrong Answers" "rotational dynamics" arxiv 2603.13259"

Links: [{"title":"[2603.13259] How Transformers Reject Wrong Answers: Rotational Dynamics of Factual Constraint Processing","url":"https://arxiv.org/abs/2603.13259"},{"title":"How Transformers Reject Wrong Answers: Rotational Dynamics of Factual Constraint Processing","url":"https://arxiv.org/html/2603.13259"},{"title":"How Transformers Reject Wrong Answers: Rotational Dynamics of Factual Constraint Processing","url":"https://arxiv.org/pdf/2603.13259"},{"title":"Symmetry Breaking in Transformers for Efficient and Interpretable Training","url":"https://arxiv.org/pdf/2601.22257"},{"title":"The Kinetics of Reasoning: How Chain-of-Thought Shapes Learning in Transformers?","url":"https://arxiv.org/pdf/2510.25791"},{"title":"Shattered Compositionality: Counterintuitive Learning Dynamics of Transformers for Arithmetic","url":"https://arxiv.org/pdf/2601.22510"}]

I found the paper! Here's what I retrieved:

The paper "How Transformers Reject Wrong Answers: Rotational Dynamics of Factual Constraint Processing" by Javier Marín investigates what happens inside a language model's network when it is fed a wrong answer.

The researchers introduced forced-completion probing, a method that presents identical queries with known correct and incorrect single-token continuations and tracks five geometric measurements across every layer of four decoder-only models (1.5B–13B parameters).

The paper reports three main findings:

1. Correct and incorrect paths diverge through rotation, not rescaling: displacement vectors maintain near-identical magnitudes while their angular separation increases, meaning factual selection is encoded in direction on an approximate hypersphere.

2. The model does not passively fail on incorrect input—it actively suppresses the correct answer, driving internal probability away from the right token.

3. Both phenomena are entirely absent below a parameter threshold and emerge at 1.6B, suggesting a phase transition in factual processing capability.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "5f72b013-e87e-4aba-87d8-95ccaebb7a3a",
  "isSidechain": true,
  "promptId": "355ad2bb-a24a-42aa-9911-1293fa95f808",
  "agentId": "a2899b2126e594028",
  "type": "user",
  "uuid": "2464c2b9-38f0-445d-8be7-830196cd4171",
  "sourceToolAssistantUUID": "5f72b013-e87e-4aba-87d8-95ccaebb7a3a",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "867e4b99-e4d4-402e-8b5a-1d69a93e0fb6",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-30T06:20:55.659Z_

<details><summary>↩ Tool result · `toolu_01RVTo2g5dxHN61hZhDpFPBL`</summary>

````text
# Comprehensive Paper Extraction: "How Transformers Reject Wrong Answers"

## 1. INTRODUCTION

The paper investigates how transformer language models process factual correctness internally. The authors note that existing work treats truthfulness as "a static property of individual-layer representations" but lacks understanding of "how internal representations diverge across the full depth of the network when the model processes correct versus incorrect continuations."

**Core Method:** "Forced-completion probing, a method that presents identical queries with known correct and incorrect single-token continuations and tracks five geometric measurements across every layer."

**Three Primary Findings:**

1. "Correct and incorrect paths diverge through rotation, not rescaling: displacement vectors maintain near-identical magnitudes while their angular separation increases"

2. "The model does not passively fail on incorrect input—it actively suppresses the correct answer, driving internal probability away from the right token"

3. "Both phenomena are entirely absent below a parameter threshold and emerge at 1.6B, suggesting a phase transition in factual processing capability"

---

## 2. MATHEMATICAL FORMALISM & FIVE MEASUREMENTS

### Definition 1: Displacement Field
```
d_ℓ^± = h_ℓ^± - h_ℓ^q ∈ ℝ^d
```
Captures how appending an answer token shifts the representation from the query-only state.

### Definition 2: Rotational Divergence
```
ρ(ℓ) = 1 - ⟨d_ℓ^+, d_ℓ^-⟩ / (‖d_ℓ^+‖ · ‖d_ℓ^-‖)
η(ℓ) = ‖d_ℓ^+‖ / ‖d_ℓ^-‖
```

"Together, ρ and η decompose the divergence between answer paths into angular and radial components."

### Definition 3: Commitment Ratio
```
κ(ℓ) = exp(φ(h_ℓ)[t^+]) / (exp(φ(h_ℓ)[t^+]) + exp(φ(h_ℓ)[t^-]))
```

### Definition 4: Active Suppression
"A model shows active suppression at layer ℓ if...κ(ℓ) < 0.5 - ε for significance threshold ε > 0."

The "suppression depth σ = 0.5 - κ_min quantifies the strength of this effect."

### Definition 5: Attention Allocation Ratio
```
α(ℓ) = Σ_(t∈T_d) a_ℓ(t) / (Σ_(t∈T_d) a_ℓ(t) + Σ_(t∈T_s) a_ℓ(t))
```

### Measurement M1: Trajectory Similarity
"The cosine similarity τ(ℓ) = cos(h_ℓ^+, h_ℓ^-) measures how similar the hidden states for correct and incorrect answers are at layer ℓ."

---

## 3. FORCED-COMPLETION PROBING METHODOLOGY

**Dataset Construction (300 total queries):**

- **Deep Constraint (DC, n=182):** "The correct answer requires integrating a domain-specific factual rule with the query context"
  
- **Control (CTRL, n=66):** "The query has a single correct answer, but arriving at it requires less domain-specific reasoning"

- **Neutral (NEU, n=52):** "The distinction between correct and incorrect tokens does not depend on factual knowledge"

**Domains:** Transport regulation, medical protocols, financial compliance (n=100 each)

**Annotations:** "Manually annotated deep keywords (tokens encoding the factual constraint...e.g., 'US', 'warfarin') and surface keywords (tokens providing context without factual specificity, e.g., 'ambulance', 'medication')"

---

## 4. MODELS EVALUATED

| Model | Parameters | Layers | Hidden Dim |
|-------|-----------|--------|-----------|
| LLaMA-2 13B | 13B | 40 | 5120 |
| Mistral 7B v0.3 | 7B | 32 | 4096 |
| StableLM-2 1.6B | 1.6B | 24 | 2048 |
| Qwen2 1.5B | 1.5B | 28 | 1536 |

"We use eager attention computation (attn_implementation='eager') rather than Flash Attention to obtain explicit per-head attention weight matrices."

---

## 5. RESULTS

### 5.1 Rotational Divergence

**Table 2: Displacement Geometry at Selected Depths**

At ℓ/L = 0.50:
- LLaMA-2: cos(d^+, d^-) = 0.69, η = 0.99
- Mistral: cos = 0.65, η = 1.00  
- StableLM-2: cos = 0.77, η = 1.00

"Across all models and layer depth, the norm ratio η(ℓ) stays within 3% of unity (range: 0.97–1.02)."

**Figure 1 Description:** Trajectory similarity drops from 0.99 at embedding to minimum values (LLaMA-2: τ_min = 0.49 at ℓ/L ≈ 0.35; Mistral: τ_min = 0.51 at ℓ/L ≈ 0.31; StableLM-2: τ_min = 0.79).

"Deep constraint and control categories show nearly identical profiles (τ_min = 0.49 vs. 0.47...not significantly different, p_FDR = 0.17)"

### 5.2 Active Suppression

**Table 3: Commitment Dynamics**

| Model | κ_final^+ | κ_min^- | ℓ*/L | σ | t-statistic | p-value |
|-------|-----------|---------|------|---|-------------|---------|
| LLaMA-2 13B | 0.77 | 0.08 | 0.85 | 0.42 | -36.5 | <10^-100 |
| Mistral 7B | 0.76 | 0.08 | 0.91 | 0.42 | -39.1 | <10^-100 |
| StableLM-2 | 0.72 | 0.32 | 0.88 | 0.18 | -7.9 | <10^-13 |
| Qwen2 1.5B | 0.50 | 0.50 | — | 0.00 | -0.01 | 0.99 |

"For incorrect answers, the logit lens commitment ratio does not only stagnate—it collapses to κ_min = 0.08 in the two larger models (p < 10^-100)"

**Figure 2 Description:** For incorrect answers (dashed gray line), κ collapses dramatically in larger models, reaching 0.08 in LLaMA-2 at ℓ/L ≈ 0.85 and Mistral at ℓ/L ≈ 0.91. StableLM-2 shows κ_min = 0.32. Qwen2 remains at 0.50 throughout.

### 5.3 Attention Reallocation

**Table 4: Attention Allocation**

| Model | ᾱ^+ (correct) | ᾱ^- (incorrect) | Sig. Layers | Max r | Best p_FDR |
|-------|---------------|-----------------|-------------|-------|-----------|
| LLaMA-2 13B | 0.62 | 0.46 | 39/41 | 0.35 | <10^-5 |
| Mistral 7B | 0.60 | 0.42 | 31/33 | 0.35 | <10^-5 |
| StableLM-2 | 0.61 | 0.42 | 18/25 | 0.40 | <10^-6 |
| Qwen2 1.5B | 0.48 | 0.34 | 0/29 | 0.07 | 0.20 |

"Correct answers consistently allocate more attention to deep-constraint tokens than incorrect answers."

### 5.4 Scale Threshold and Linear Probing

**Figure 3 (Left): Probe Accuracy Across Depth**

- LLaMA-2: 0.85 ± 0.08 peak at ℓ/L = 0.35; final: 0.76
- Mistral: 0.82 ± 0.09 peak at ℓ/L = 0.47; final: 0.75
- StableLM-2: 0.79 ± 0.05 peak at ℓ/L = 0.21; final: 0.72
- Qwen2: 0.50 throughout

"The dissociation between peak probe accuracy and final-layer accuracy is consistent across models (Δ = 0.07–0.09)"

**Figure 3 (Right): Cross-Domain Transfer AUROC**

- LLaMA-2 within-domain: 1.00; cross-domain mean: 0.87
- Mistral within-domain: 1.00; cross-domain mean: 0.84
- StableLM-2 within-domain: 1.00; cross-domain mean: 0.80

---

## 6. DISCUSSION

### 6.1 Geometry of Factual Processing

"Methods that detect hallucinations by comparing embedding magnitudes or norms will miss the signal. The discriminative information lives entirely in angular position."

Correlation between probe accuracy and commitment gap: "positive and significant in LLaMA-2 (r = 0.64, p < 10^-5, Pearson) but absent in StableLM-2 (r = -0.01, p = 0.97)."

### 6.2 Active Suppression as Computational Strategy

"A model could process an incorrect answer while remaining agnostic about correctness (maintaining κ ≈ 0.5), as Qwen2 does. Instead, the larger models actively shift their internal representations to favor the token they are currently processing—even when that token is factually wrong."

The "suppression depth σ scaling with model size (0.00 → 0.18 → 0.42 → 0.42) suggests that larger models develop stronger internal consistency mechanisms."

### 6.3 Hallucination Detection Implications

"However, our experimental design uses forced answers with known correct/incorrect tokens, which does not directly apply to open-ended generation where the set of possible answers is wider."

---

## 7. LIMITATIONS

1. **Dataset scale:** "300 queries across three domains is sufficient for the large effect sizes...but limits...domain-specific structure"

2. **Forced vs. autoregressive:** "Our method appends a single token...In natural generation, the model autoregressively selects tokens, and the dynamics of this selection process may differ"

3. **Architecture scope:** "All four models are decoder-only transformers"

4. **Probe significance:** "The peak-to-final accuracy gap...reaches only p ≈ 0.10–0.12...likely underpowered"

5. **Qwen2 architecture:** "Could reflect architectural differences rather than scale alone"

---

## 8. CONCLUSIONS

The paper establishes that "transformers characterize correct and incorrect answers through rotation in representation space, not through scaling." The "suppression depth scales with model size" and phenomena "emerge at 1.6B parameters."

"Two limitations bound these conclusions. First, forced-completion probing controls for confounds by constraining the experimental setup to single-token continuations...Whether the rotational geometry persists in free-form autoregressive generation...remains untested. Second, four models cannot characterize a phase transition."
````

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "145b59db-471f-4b55-b3b9-ebb1bed6deb7",
  "isSidechain": true,
  "promptId": "355ad2bb-a24a-42aa-9911-1293fa95f808",
  "agentId": "a2899b2126e594028",
  "type": "user",
  "uuid": "71db8e48-9936-459c-905f-0fe445cd93df",
  "sourceToolAssistantUUID": "145b59db-471f-4b55-b3b9-ebb1bed6deb7",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "867e4b99-e4d4-402e-8b5a-1d69a93e0fb6",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 21 · 2026-05-30T06:20:59.411Z_

Let me do a couple more targeted searches to find any community discussion, blog posts, or citing papers, and also try to get more detail from the paper on the specific geometric formalism.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "71db8e48-9936-459c-905f-0fe445cd93df",
  "isSidechain": true,
  "agentId": "a2899b2126e594028",
  "requestId": "req_011CbYGdP2BLE9F2fh152U86",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "2e5b5323-5d8c-4d0a-b37e-7fe9d88fd56c",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "867e4b99-e4d4-402e-8b5a-1d69a93e0fb6",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01W8eUDXsVusnYFchhDmuU7V",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 994,
      "cache_creation_input_tokens": 4269,
      "cache_read_input_tokens": 12353,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4269,
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

_source line 22 · 2026-05-30T06:20:59.946Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_0179HmUnwGUwnYLhSsDT5m9G`</summary>

```json
{
  "query": "Javier Marín \"forced-completion probing\" transformer factual constraint rotation hypersphere"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2e5b5323-5d8c-4d0a-b37e-7fe9d88fd56c",
  "isSidechain": true,
  "agentId": "a2899b2126e594028",
  "requestId": "req_011CbYGdP2BLE9F2fh152U86",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "517c8831-a27d-4c9b-803f-7119f07095f3",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "867e4b99-e4d4-402e-8b5a-1d69a93e0fb6",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01W8eUDXsVusnYFchhDmuU7V",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 994,
      "cache_creation_input_tokens": 4269,
      "cache_read_input_tokens": 12353,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4269,
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

_source line 23 · 2026-05-30T06:21:00.504Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01MfjSDgXtYReBLSFajhbUTN`</summary>

```json
{
  "query": "\"active suppression\" \"correct answer\" transformer mechanistic interpretability rotation embedding 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "517c8831-a27d-4c9b-803f-7119f07095f3",
  "isSidechain": true,
  "agentId": "a2899b2126e594028",
  "requestId": "req_011CbYGdP2BLE9F2fh152U86",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "5d0741af-3205-41fc-9b6a-52f99684bf6d",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "867e4b99-e4d4-402e-8b5a-1d69a93e0fb6",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01W8eUDXsVusnYFchhDmuU7V",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 994,
      "cache_creation_input_tokens": 4269,
      "cache_read_input_tokens": 12353,
      "output_tokens": 164,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 4269
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 994,
          "output_tokens": 164,
          "cache_read_input_tokens": 12353,
          "cache_creation_input_tokens": 4269,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 4269,
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

_source line 24 · 2026-05-30T06:21:07.284Z_

<details><summary>↩ Tool result · `toolu_0179HmUnwGUwnYLhSsDT5m9G`</summary>

```text
Web search results for query: "Javier Marín "forced-completion probing" transformer factual constraint rotation hypersphere"

Links: [{"title":"[2603.13259] How Transformers Reject Wrong Answers: Rotational Dynamics of Factual Constraint Processing","url":"https://arxiv.org/abs/2603.13259"},{"title":"How Transformers Reject Wrong Answers: Rotational Dynamics of Factual Constraint Processing","url":"https://arxiv.org/html/2603.13259"},{"title":"How Transformers Reject Wrong Answers: Rotational Dynamics of Factual Constraint Processing","url":"https://arxiv.org/pdf/2603.13259"},{"title":"Attention Satisfies: A Constraint-Satisfaction Lens on Factual...","url":"https://arxiv.org/abs/2309.15098"},{"title":"Attention Satisfies: A Constraint-Satisfaction Lens on Factual Errors of Language Models","url":"https://arxiv.org/html/2309.15098v2"},{"title":"MODIFYING MEMORIES IN TRANSFORMER MODELS","url":"https://openreview.net/pdf?id=KubHAaKdSr7"}]

I found the paper you're looking for! Here are the search results:

The paper is titled "How Transformers Reject Wrong Answers: Rotational Dynamics of Factual Constraint Processing" by Javier Marín.

Key findings from the research:

The paper introduces forced-completion probing, a method that presents identical queries with known correct and incorrect single-token continuations and tracks five geometric measurements across every layer of four decoder-only models (1.5B-13B parameters).

The first main finding is that correct and incorrect paths diverge through rotation, not rescaling: displacement vectors maintain near-identical magnitudes while their angular separation increases, meaning factual selection is encoded in direction on an approximate hypersphere.

Second, the model does not passively fail on incorrect input—it actively suppresses the correct answer, driving internal probability away from the right token.

Third, both phenomena are entirely absent below a parameter threshold and emerge at 1.6B, suggesting a phase transition in factual processing capability.

The paper was published in February 2026 and is available on arXiv (paper ID: 2603.13259).


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "517c8831-a27d-4c9b-803f-7119f07095f3",
  "isSidechain": true,
  "promptId": "355ad2bb-a24a-42aa-9911-1293fa95f808",
  "agentId": "a2899b2126e594028",
  "type": "user",
  "uuid": "76e9faa2-8ed2-4219-b385-835d64f435fd",
  "sourceToolAssistantUUID": "517c8831-a27d-4c9b-803f-7119f07095f3",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "867e4b99-e4d4-402e-8b5a-1d69a93e0fb6",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 25 · 2026-05-30T06:21:08.186Z_

<details><summary>↩ Tool result · `toolu_01MfjSDgXtYReBLSFajhbUTN`</summary>

```text
Web search results for query: ""active suppression" "correct answer" transformer mechanistic interpretability rotation embedding 2026"

Links: [{"title":"How Transformers Reject Wrong Answers: Rotational Dynamics of Factual Constraint Processing","url":"https://arxiv.org/html/2603.13259"},{"title":"How Transformers Reject Wrong Answers: Rotational Dynamics of Factual Constraint Processing","url":"https://arxiv.org/pdf/2603.13259"},{"title":"[2605.24577] Polymorphism Is Rotation: Operational Mechanistic Interpretability from a Two-Layer Transformer to Pythia-70m","url":"https://arxiv.org/abs/2605.24577"},{"title":"Symmetry Breaking in Transformers for Efficient and Interpretable Training","url":"https://arxiv.org/pdf/2601.22257"},{"title":"Mechanistic Interpretability for Transformer-Based Time Series Classification | Springer Nature Link","url":"https://link.springer.com/chapter/10.1007/978-3-032-15638-9_15"},{"title":"Directional Routing in Transformers","url":"https://arxiv.org/html/2603.14923"},{"title":"[2511.21514] Mechanistic Interpretability for Transformer-based Time Series Classification","url":"https://arxiv.org/abs/2511.21514"},{"title":"Interpreting Transformers Through Attention Head Intervention","url":"https://arxiv.org/pdf/2601.04398"},{"title":"Mechanistic Interpretability for Transformer-based Time Series Classification","url":"https://arxiv.org/html/2511.21514v1"}]

Based on the search results, I found a highly relevant paper on this topic. The most closely matching work is:

**"How Transformers Reject Wrong Answers: Rotational Dynamics of Factual Constraint Processing"** (February 2026)

This paper directly addresses your search terms. Key findings include:

1. **Active Suppression**: The model does not passively fail on incorrect input—it actively suppresses the correct answer, driving internal probability away from the right token.

2. **Rotational Embedding Dynamics**: Correct and incorrect paths diverge through rotation, not rescaling: displacement vectors maintain near-identical magnitudes while their angular separation increases, meaning factual selection is encoded in direction on an approximate hypersphere.

3. **Mechanistic Methodology**: The paper introduces forced-completion probing, a method that presents identical queries with known correct and incorrect single-token continuations and tracks five geometric measurements across every layer of four decoder-only models (1.5B–13B parameters).

4. **Scale-Dependent Behavior**: Both phenomena are entirely absent below a parameter threshold and emerge at 1.6B, suggesting a phase transition in factual processing capability.

The paper demonstrates that factual constraint processing has a specific geometric character—rotational, not scalar; active, not passive—that is invisible to methods based on single-layer probes or magnitude comparisons.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "5d0741af-3205-41fc-9b6a-52f99684bf6d",
  "isSidechain": true,
  "promptId": "355ad2bb-a24a-42aa-9911-1293fa95f808",
  "agentId": "a2899b2126e594028",
  "type": "user",
  "uuid": "05562ccb-0752-485e-a889-8b6ff143adc9",
  "sourceToolAssistantUUID": "5d0741af-3205-41fc-9b6a-52f99684bf6d",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "867e4b99-e4d4-402e-8b5a-1d69a93e0fb6",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 26 · 2026-05-30T06:21:13.035Z_

I also noticed a potentially related paper in those results. Let me check it and do one final search for any Twitter/blog discussion.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "05562ccb-0752-485e-a889-8b6ff143adc9",
  "isSidechain": true,
  "agentId": "a2899b2126e594028",
  "requestId": "req_011CbYGeJW6hEBm2wVJ7HN9j",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "306eea58-a7df-4011-bfc0-1735bb858da6",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "867e4b99-e4d4-402e-8b5a-1d69a93e0fb6",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01A3RuYc6NhCt8D7yAuxXChC",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2515,
      "cache_read_input_tokens": 16622,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2515,
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

_source line 27 · 2026-05-30T06:21:13.575Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_015DRx2wBPha3TSJUE7B3231`</summary>

```json
{
  "query": "\"Polymorphism Is Rotation\" arxiv 2605.24577 mechanistic interpretability"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "306eea58-a7df-4011-bfc0-1735bb858da6",
  "isSidechain": true,
  "agentId": "a2899b2126e594028",
  "requestId": "req_011CbYGeJW6hEBm2wVJ7HN9j",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "c651877b-f8a2-4b45-b4b1-649fade2a0f8",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "867e4b99-e4d4-402e-8b5a-1d69a93e0fb6",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01A3RuYc6NhCt8D7yAuxXChC",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2515,
      "cache_read_input_tokens": 16622,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2515,
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

_source line 28 · 2026-05-30T06:21:14.188Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01HYbBBLjTL4YoC7bzJhBanc`</summary>

```json
{
  "query": "site:twitter.com OR site:x.com \"rotational dynamics\" \"factual constraint\" OR \"2603.13259\" transformer"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c651877b-f8a2-4b45-b4b1-649fade2a0f8",
  "isSidechain": true,
  "agentId": "a2899b2126e594028",
  "requestId": "req_011CbYGeJW6hEBm2wVJ7HN9j",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "63e62e30-a2b6-49b0-bdb4-ae99363f1cec",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "867e4b99-e4d4-402e-8b5a-1d69a93e0fb6",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01A3RuYc6NhCt8D7yAuxXChC",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2515,
      "cache_read_input_tokens": 16622,
      "output_tokens": 165,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2515
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 165,
          "cache_read_input_tokens": 16622,
          "cache_creation_input_tokens": 2515,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2515,
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

_source line 29 · 2026-05-30T06:21:20.178Z_

<details><summary>↩ Tool result · `toolu_015DRx2wBPha3TSJUE7B3231`</summary>

```text
Web search results for query: ""Polymorphism Is Rotation" arxiv 2605.24577 mechanistic interpretability"

Links: [{"title":"[2605.24577] Polymorphism Is Rotation: Operational Mechanistic Interpretability from a Two-Layer Transformer to Pythia-70m","url":"https://arxiv.org/abs/2605.24577"},{"title":"Polymorphism Is Rotation: Operational Mechanistic Interpretability from a Two-Layer Transformer to Pythia-70m","url":"https://arxiv.org/html/2605.24577"},{"title":"[2605.09881] Dissecting Jet-Tagger Through Mechanistic Interpretability","url":"https://arxiv.org/abs/2605.09881"},{"title":"Validating Mechanistic Interpretations: An Axiomatic Approach","url":"https://arxiv.org/pdf/2407.13594"},{"title":"Mechanistic Interpretability for Large Language Model Alignment: Progress, Challenges, and Future Directions","url":"https://arxiv.org/pdf/2602.11180"},{"title":"Contents","url":"https://arxiv.org/html/2605.09881"}]

Based on the search results, here's what I found about this paper:

## "Polymorphism Is Rotation: Operational Mechanistic Interpretability from a Two-Layer Transformer to Pythia-70m"

The paper, authored by Jordan F. McCann and submitted on May 23, 2026, discovers that independently trained transformers compute the same function in residual-stream bases that differ by a uniform random rotation on SO(d_model).

**Key findings:**

- The phenomenon is called polymorphism: same function, mutually unintelligible interior coordinates.

- One matrix multiplication per model pair removes it: an orthogonal Procrustes fit on a single batch of activations transfers sparse-autoencoder feature dictionaries and steering vectors between independently trained models, with no retraining.

- The phenomenon is invisible to the standard SAE universality metric, despite decoder-column cosine similarity matching across seeds at 98%.

The paper addresses an important issue in mechanistic interpretability—that seemingly universal properties of neural networks can mask fundamental differences in how different models represent and compute the same functions internally.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c651877b-f8a2-4b45-b4b1-649fade2a0f8",
  "isSidechain": true,
  "promptId": "355ad2bb-a24a-42aa-9911-1293fa95f808",
  "agentId": "a2899b2126e594028",
  "type": "user",
  "uuid": "71a0281f-94ec-4d46-a4f1-b16106798f2e",
  "sourceToolAssistantUUID": "c651877b-f8a2-4b45-b4b1-649fade2a0f8",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "867e4b99-e4d4-402e-8b5a-1d69a93e0fb6",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 30 · 2026-05-30T06:21:21.379Z_

<details><summary>↩ Tool result · `toolu_01HYbBBLjTL4YoC7bzJhBanc`</summary>

```text
Web search results for query: "site:twitter.com OR site:x.com "rotational dynamics" "factual constraint" OR "2603.13259" transformer"

Links: [{"title":"How Transformers Reject Wrong Answers: Rotational Dynamics of Factual Constraint Processing","url":"https://arxiv.org/pdf/2603.13259"},{"title":"How Transformers Reject Wrong Answers: Rotational Dynamics of Factual Constraint Processing","url":"https://arxiv.org/html/2603.13259"},{"title":"[2603.13259] How Transformers Reject Wrong Answers: Rotational Dynamics of Factual Constraint Processing","url":"https://arxiv.org/abs/2603.13259"},{"title":"Rule guided transformers for dynamic knowledge adaptation in rotating machinery fault diagnosis - ScienceDirect","url":"https://www.sciencedirect.com/science/article/pii/S1474034626001369"},{"title":"Improving Computational Efficiency for Powered Descent Guidance via Transformer-based Tight Constraint Prediction","url":"https://arxiv.org/html/2311.05135v2"}]

The search results show that the academic paper you're looking for is "How Transformers Reject Wrong Answers: Rotational Dynamics of Factual Constraint Processing" by Javier Marín, published in February 2026. 

The research introduces forced-completion probing, a method that tracks five geometric measurements across every layer of four decoder-only models (1.5B–13B parameters). The key finding is that correct and incorrect paths diverge through rotation, not rescaling: displacement vectors maintain near-identical magnitudes while their angular separation increases, meaning factual selection is encoded in direction on an approximate hypersphere.

The paper is available on arXiv as document 2603.13259 and can be accessed in multiple formats (PDF, HTML, and abstract pages). However, I should note that this search did not return results specifically from Twitter/X, likely because such academic papers are not typically shared on those platforms or are not indexed in standard search results in that way.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "63e62e30-a2b6-49b0-bdb4-ae99363f1cec",
  "isSidechain": true,
  "promptId": "355ad2bb-a24a-42aa-9911-1293fa95f808",
  "agentId": "a2899b2126e594028",
  "type": "user",
  "uuid": "242993c5-fc93-4fdc-8df5-796154a4f019",
  "sourceToolAssistantUUID": "63e62e30-a2b6-49b0-bdb4-ae99363f1cec",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "867e4b99-e4d4-402e-8b5a-1d69a93e0fb6",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 31 · 2026-05-30T06:22:51.692Z_

Now I have comprehensive information. Here is the detailed analysis.

---

## Detailed Analysis: "How Transformers Reject Wrong Answers: Rotational Dynamics of Factual Constraint Processing"

**Author:** Javier Marin | **arXiv:** [2603.13259](https://arxiv.org/abs/2603.13259) | **Submitted:** February 25, 2026 | **Categories:** cs.CL, cs.AI

---

### 1. THE GAP THEY IDENTIFIED

The paper identifies that prior work on factual knowledge in LLMs (Burns et al. 2023, Azaria et al. 2023, Meng et al. 2022) treats truthfulness as **a static property of individual-layer representations**. These works ask *where* knowledge is stored but never address **how internal representations diverge across the full depth of the network when the model processes correct versus incorrect continuations**. The existing paradigm uses single-layer probes or logit-based evaluations that provide snapshots but miss the dynamic, layer-by-layer evolution of factual processing.

The reformulation: instead of asking "does the model know X?" they ask "what geometric transformation does the model perform on its representations when it encounters a wrong answer versus a right one, and how does this transformation evolve across layers?"

---

### 2. TECHNICAL METHOD: FORCED-COMPLETION PROBING

The method presents identical queries paired with known correct (+) and incorrect (-) single-token continuations, then tracks **five geometric measurements** at every layer. This is not autoregressive generation -- they force-feed the answer token and observe what happens inside.

**Dataset:** 300 queries across three domains (transport regulation, medical protocols, financial compliance), split into:
- **Deep Constraint (DC, n=182):** Requires integrating a domain-specific factual rule with context
- **Control (CTRL, n=66):** Single correct answer but less domain reasoning needed
- **Neutral (NEU, n=52):** Distinction doesn't depend on factual knowledge

Queries are manually annotated with "deep keywords" (tokens encoding the factual constraint, e.g., "US", "warfarin") and "surface keywords" (context tokens without factual specificity, e.g., "ambulance", "medication").

**Models tested:**
| Model | Params | Layers | Hidden Dim |
|-------|--------|--------|-----------|
| LLaMA-2 | 13B | 40 | 5120 |
| Mistral 7B v0.3 | 7B | 32 | 4096 |
| StableLM-2 | 1.6B | 24 | 2048 |
| Qwen2 | 1.5B | 28 | 1536 |

They use eager attention (not Flash Attention) to obtain explicit per-head attention weight matrices.

---

### 3. THE FIVE GEOMETRIC MEASUREMENTS AND MATHEMATICAL FORMALISM

**Definition 1 -- Displacement Field:**
```
d_l^± = h_l^± - h_l^q ∈ R^d
```
This captures how appending a correct (+) or incorrect (-) answer token shifts the representation away from the query-only state.

**Definition 2 -- Rotational Divergence (the core contribution):**
```
rho(l) = 1 - &lt;d_l^+, d_l^-> / (||d_l^+|| * ||d_l^-||)
eta(l) = ||d_l^+|| / ||d_l^-||
```
rho is the angular component (rotation), eta is the radial component (scaling). Together they decompose the divergence between correct and incorrect answer paths into angular versus radial components.

**Definition 3 -- Commitment Ratio (logit lens application):**
```
kappa(l) = exp(phi(h_l)[t^+]) / (exp(phi(h_l)[t^+]) + exp(phi(h_l)[t^-]))
```
This measures, at each layer, how much the model's internal state "commits" to the correct answer token versus the incorrect one, using the unembedding matrix (logit lens).

**Definition 4 -- Active Suppression:**
A model shows active suppression at layer l if kappa(l) < 0.5 - epsilon for a significance threshold epsilon > 0. The **suppression depth** sigma = 0.5 - kappa_min quantifies the strength of this effect.

**Definition 5 -- Attention Allocation Ratio:**
```
alpha(l) = Sum_{t in T_d} a_l(t) / (Sum_{t in T_d} a_l(t) + Sum_{t in T_s} a_l(t))
```
This measures how much attention goes to deep-constraint tokens versus surface tokens.

**Measurement M1 -- Trajectory Similarity:**
```
tau(l) = cos(h_l^+, h_l^-)
```
Cosine similarity between the hidden states for correct and incorrect answers at each layer.

---

### 4. "ROTATION NOT RESCALING" -- WHAT IT MEANS CONCRETELY

This is the paper's headline finding. Across all models and all layers, the norm ratio eta(l) stays **within 3% of unity** (range: 0.97-1.02). This means the displacement vectors for correct and incorrect answers have essentially the same magnitude. The model is NOT distinguishing correct from incorrect by making one representation "bigger" or "smaller."

Instead, the divergence lives entirely in the **angular separation** (rho). The cosine similarity between displacement vectors drops substantially (e.g., from ~1.0 at embedding to 0.69 at midpoint for LLaMA-2), while norms remain matched.

Concretely: if you imagine the representation space, the correct-answer displacement and incorrect-answer displacement are vectors of the same length pointing in increasingly different directions. They trace paths on an **approximate hypersphere** (same radius, different angular positions). The factual discrimination signal is entirely directional.

The practical implication, stated directly in the paper: **"Methods that detect hallucinations by comparing embedding magnitudes or norms will miss the signal. The discriminative information lives entirely in angular position."**

---

### 5. THE APPROXIMATE HYPERSPHERE

The "approximate hypersphere" finding follows from the norm ratio staying near unity. Since ||d_l^+|| / ||d_l^-|| is approximately 1.0 at every layer, both displacement vectors have essentially the same norm, meaning they lie on a hypersphere of approximately constant radius in the d-dimensional representation space. The factual processing happens as rotation on this surface, not as movement toward or away from the origin.

This is not a claimed exact geometric constraint -- the "approximate" qualifier is important -- but the consistency (within 3% across all models, layers, and query types) makes it a robust empirical regularity.

---

### 6. ACTIVE SUPPRESSION OF CORRECT ANSWERS

This is the most striking finding. When the model is force-fed an **incorrect** answer, it does not simply remain agnostic (kappa approximately 0.5). Instead, larger models **actively drive kappa below 0.5**, meaning they internally boost the probability of the wrong token they were given and suppress the correct token.

**Quantitative results (Table 3):**

| Model | kappa_final (correct) | kappa_min (incorrect) | Suppression depth sigma | p-value |
|-------|----------------------|----------------------|------------------------|---------|
| LLaMA-2 13B | 0.77 | 0.08 | 0.42 | <10^-100 |
| Mistral 7B | 0.76 | 0.08 | 0.42 | <10^-100 |
| StableLM-2 1.6B | 0.72 | 0.32 | 0.18 | <10^-13 |
| Qwen2 1.5B | 0.50 | 0.50 | 0.00 | 0.99 |

For LLaMA-2 and Mistral, when fed the wrong answer, the commitment ratio for the correct token collapses to **0.08** -- the model is actively representing the wrong answer as the "right" one internally, with t-statistics exceeding -36.

The paper frames this as a "computational strategy": the model could remain neutral (as Qwen2 does at 0.50), but larger models choose to actively reinforce whatever answer they're processing, even when it's wrong. The suppression depth scales with model size: 0.00 -> 0.18 -> 0.42 -> 0.42.

---

### 7. THE FLIP PHENOMENON

The paper documents this through the linear probing analysis (Figure 3). Probe accuracy (ability to discriminate correct from incorrect from hidden states alone) peaks at **intermediate layers** and then **decreases** toward the final layer:

- LLaMA-2: peak 0.85 at l/L = 0.35, final 0.76 (drop of 0.09)
- Mistral: peak 0.82 at l/L = 0.47, final 0.75 (drop of 0.07)
- StableLM-2: peak 0.79 at l/L = 0.21, final 0.72 (drop of 0.07)
- Qwen2: 0.50 throughout (no discrimination at any layer)

This means the model internally "knows" the answer is wrong most clearly at mid-depth, but by the final layers, some of this discriminative information has been lost -- consistent with the active suppression mechanism overwriting the factual signal. The dissociation between peak probe accuracy and final-layer accuracy (Delta = 0.07-0.09) is consistent across the three models above threshold.

The paper notes this peak-then-decline pattern is **not** what you'd expect from simple knowledge retrieval, where accuracy should monotonically increase. Instead, it suggests the model first identifies correctness/incorrectness, then actively adjusts its representations -- and in the case of wrong answers, this adjustment partially obscures the very correctness signal.

---

### 8. THE 1.6B PARAMETER EMERGENCE THRESHOLD

Qwen2 (1.5B parameters) shows **none** of the phenomena:
- No rotational divergence (trajectory similarity stays high)
- No active suppression (kappa = 0.50 throughout, sigma = 0.00, p = 0.99)
- No differential attention allocation (0 out of 29 layers significant, max r = 0.07)
- No probe discrimination (0.50 = chance throughout)

StableLM-2 (1.6B) shows **all** phenomena, though at reduced magnitude compared to the 7B and 13B models. The paper interprets this as a **phase transition in factual processing capability** at approximately 1.6B parameters.

However, the paper is appropriately cautious: "four models cannot characterize a phase transition." The Qwen2 null result could reflect architectural differences rather than scale alone (Qwen2 has 28 layers with 1536 hidden dim vs. StableLM-2's 24 layers with 2048 hidden dim).

---

### 9. ATTENTION REALLOCATION

Correct answers consistently allocate more attention to deep-constraint tokens:

| Model | alpha (correct) | alpha (incorrect) | Significant Layers |
|-------|----------------|-------------------|-------------------|
| LLaMA-2 | 0.62 | 0.46 | 39/41 |
| Mistral | 0.60 | 0.42 | 31/33 |
| StableLM-2 | 0.61 | 0.42 | 18/25 |
| Qwen2 | 0.48 | 0.34 | 0/29 |

Cross-domain transfer AUROC shows the mechanism generalizes: LLaMA-2 achieves 0.87 cross-domain mean, Mistral 0.84, StableLM-2 0.80.

---

### 10. CONNECTIONS TO PRIOR WORK AND RAG RELEVANCE

The paper builds on and extends:
- **Nostalgebraist (2020) logit lens** -- used for the commitment ratio kappa
- **Burns et al. (2023) "Discovering Latent Knowledge"** -- but moves from static probing to dynamic layer-by-layer analysis
- **Meng et al. (2022) "Locating Factual Knowledge"** -- but studies the rejection mechanism rather than storage
- **Marks et al. (2023) geometric perspectives** -- the paper's closest methodological kin
- **Geva et al. (2023)** on intermediate computations

A related recent paper found in searches: **"Polymorphism Is Rotation"** ([arxiv 2605.24577](https://arxiv.org/abs/2605.24577), McCann, May 2026) independently finds that transformers compute the same function in residual-stream bases differing by uniform random rotation on SO(d_model), with orthogonal Procrustes alignment transferring SAE dictionaries between models. This resonates strongly with the rotational dynamics finding -- both suggest rotation is a fundamental computational primitive in transformer representation spaces.

---

### 11. LIMITATIONS AND OPEN QUESTIONS

1. **Forced vs. autoregressive:** The method appends a single token; natural generation dynamics may differ.
2. **Dataset scale:** 300 queries, three domains -- sufficient for large effect sizes but limited for domain structure.
3. **Architecture scope:** Only decoder-only transformers tested.
4. **Probe significance:** The peak-to-final accuracy gap reaches only p approximately 0.10-0.12, likely underpowered.
5. **Qwen2 confound:** Architecture vs. scale cannot be disentangled with four models.

---

### 12. EXTERNAL DISCUSSION AND CITATIONS

No blog posts, Twitter threads, or third-party reviews were found in searches. The paper appears to have limited community uptake so far (submitted February 2026). No formal citations were found. The only related concurrent work is the "Polymorphism Is Rotation" paper, which does not cite this work but arrives at complementary rotation-centric findings from a different angle.

---

### KEY TAKEAWAY FOR RAG CIRCUIT TRACING

This paper is directly relevant to RAG circuit tracing because it provides a geometric framework for understanding how models process (and reject) factual information at the representation level. For RAG specifically:

- The finding that factual discrimination is **rotational/angular, not magnitude-based** means that any RAG circuit tracing method that relies on activation magnitudes or norms will miss the signal.
- The **active suppression** mechanism suggests that when a RAG system retrieves wrong context, the model may not just fail to use it -- it may actively suppress the correct answer it already "knows," making retrieval errors potentially worse than no retrieval.
- The **flip phenomenon** (correct answer peaking at mid-layers then declining) has direct implications for where to probe or intervene in RAG-augmented models.
- The **1.6B threshold** suggests that smaller models used in RAG pipelines may lack the factual constraint processing machinery entirely, processing retrieved context in a qualitatively different way.

Sources:
- [arXiv Abstract Page](https://arxiv.org/abs/2603.13259)
- [Full Paper (HTML)](https://arxiv.org/html/2603.13259)
- [Full Paper (PDF)](https://arxiv.org/pdf/2603.13259)
- [Polymorphism Is Rotation (related work)](https://arxiv.org/abs/2605.24577)
- [Attention Satisfies: Constraint-Satisfaction Lens (related prior work)](https://arxiv.org/abs/2309.15098)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "242993c5-fc93-4fdc-8df5-796154a4f019",
  "isSidechain": true,
  "agentId": "a2899b2126e594028",
  "requestId": "req_011CbYGfGusvNfwtbDZKjscE",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "565b9af6-a3d4-4b51-b692-e0d1b57331f8",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "867e4b99-e4d4-402e-8b5a-1d69a93e0fb6",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JSG8N6THoMLYyUHTFVokEU",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1292,
      "cache_read_input_tokens": 19137,
      "output_tokens": 3790,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1292
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 3790,
          "cache_read_input_tokens": 19137,
          "cache_creation_input_tokens": 1292,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1292,
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
