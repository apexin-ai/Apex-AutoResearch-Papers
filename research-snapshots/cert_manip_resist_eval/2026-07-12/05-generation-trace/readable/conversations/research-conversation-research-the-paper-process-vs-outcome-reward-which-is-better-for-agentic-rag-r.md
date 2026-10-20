# Research conversation: Research the paper "Process vs. Outcome Reward: Which is Better for Agentic RAG Reinforcement Learning" (ReasonRAG / RAG

**The Weakest Link Across Panel Sizes: Predictor Relevance Patterns in Multi-Judge LLM Evaluation under Adversarial Manipulation (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 47
- **Recorded user turns:** 1
- **Tool calls:** 18
- **Original source:** `logs/chats/exported-trajectories/account-2/agent-aa34d3135a3369818.jsonl`
- **Structured JSON:** [`bbdd9ead2b7800f2fa4d.json`](../../sessions/bb/bbdd9ead2b7800f2fa4d.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

47 recorded events

### User

_source line 1 · 2026-05-30T06:28:12.213Z_

Research the paper "Process vs. Outcome Reward: Which is Better for Agentic RAG Reinforcement Learning" (ReasonRAG / RAG-ProGuide) by Wenlin Zhang et al. (arXiv 2025), arxiv URL: https://arxiv.org/abs/2505.14069

Steps:
1. Use WebFetch to read the arxiv abstract page
2. Use WebFetch to read the full paper PDF (https://arxiv.org/pdf/2505.14069)
3. Search for any reviews or discussion about this paper

For each, extract:
- What gap did they identify and HOW? (process vs outcome rewards for RAG)
- What was the key insight others missed?
- How did they formulate the problem differently?
- What existing technique did they adapt/combine/simplify?
- Technical method details (RAG-ProGuide, the process-level rewards for query generation, evidence extraction, answer generation)
- Key quantitative results (18× data efficiency claim)
- Limitations
- Whether this trains the retriever or the LLM (critical distinction for our research)

Be thorough and specific. Return all findings in a structured format.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "bbbe4bf2-b0a9-43d5-8f54-a157f509f7eb",
  "agentId": "aa34d3135a3369818",
  "type": "user",
  "uuid": "61ef2033-24ff-4531-96cb-1b78b837a7de",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "27d805b7-0ea1-4632-9635-35f016c03b5a",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 2 · 2026-05-30T06:28:12.216Z_

```json
{
  "parentUuid": "61ef2033-24ff-4531-96cb-1b78b837a7de",
  "isSidechain": true,
  "agentId": "aa34d3135a3369818",
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
  "uuid": "d8906665-62b5-45a2-b854-4488bebfa6ad",
  "timestamp": "2026-05-30T06:28:12.216Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "27d805b7-0ea1-4632-9635-35f016c03b5a",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 3 · 2026-05-30T06:28:12.219Z_

```json
{
  "parentUuid": "d8906665-62b5-45a2-b854-4488bebfa6ad",
  "isSidechain": true,
  "agentId": "aa34d3135a3369818",
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "31d109d2-5503-4feb-a530-060f40c6159b",
  "timestamp": "2026-05-30T06:28:12.219Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "27d805b7-0ea1-4632-9635-35f016c03b5a",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Assistant

_source line 4 · 2026-05-30T06:28:26.507Z_



I'll research this paper thoroughly. Let me start by fetching the tools I need and then gathering information from multiple sources.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "31d109d2-5503-4feb-a530-060f40c6159b",
  "isSidechain": true,
  "agentId": "aa34d3135a3369818",
  "requestId": "req_011CbYHBZgmPbgqNh2tuQEMs",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "8322d574-9b03-4939-9279-8b81803e04d3",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "27d805b7-0ea1-4632-9635-35f016c03b5a",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PRmPHAu5zFYZaQTVrUMZj4",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1616,
      "cache_read_input_tokens": 7413,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1616,
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

_source line 5 · 2026-05-30T06:28:27.127Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01CjsbncuiYhCxdBXWFYMCU9`</summary>

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
  "parentUuid": "8322d574-9b03-4939-9279-8b81803e04d3",
  "isSidechain": true,
  "agentId": "aa34d3135a3369818",
  "requestId": "req_011CbYHBZgmPbgqNh2tuQEMs",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "98bfbfa2-6fab-4100-92cd-4a633db4ec3a",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "27d805b7-0ea1-4632-9635-35f016c03b5a",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PRmPHAu5zFYZaQTVrUMZj4",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1616,
      "cache_read_input_tokens": 7413,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1616,
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

_source line 6 · 2026-05-30T06:28:27.133Z_

<details><summary>↩ Tool result · `toolu_01CjsbncuiYhCxdBXWFYMCU9`</summary>

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
  "parentUuid": "98bfbfa2-6fab-4100-92cd-4a633db4ec3a",
  "isSidechain": true,
  "promptId": "bbbe4bf2-b0a9-43d5-8f54-a157f509f7eb",
  "agentId": "aa34d3135a3369818",
  "type": "user",
  "uuid": "d1326db8-dcff-4fac-ab68-99095f9f4171",
  "sourceToolAssistantUUID": "98bfbfa2-6fab-4100-92cd-4a633db4ec3a",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "27d805b7-0ea1-4632-9635-35f016c03b5a",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 7 · 2026-05-30T06:28:29.586Z_



Now let me fetch the paper from multiple sources in parallel.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d1326db8-dcff-4fac-ab68-99095f9f4171",
  "isSidechain": true,
  "agentId": "aa34d3135a3369818",
  "requestId": "req_011CbYHCgiiWn5fVgsCmezgA",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "c2efc941-122a-4049-a304-4696d7f9c17f",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "27d805b7-0ea1-4632-9635-35f016c03b5a",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QuuWMSpREvRxWq84qKoBqT",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1128,
      "cache_read_input_tokens": 9029,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1128,
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

_source line 8 · 2026-05-30T06:28:31.474Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01JSFdiczFiPe7m5F9K2bjwP`</summary>

```json
{
  "url": "https://arxiv.org/abs/2505.14069",
  "prompt": "Extract ALL information from this arxiv abstract page: title, authors, full abstract text, submission date, categories, and any other metadata. Be comprehensive and return everything verbatim."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c2efc941-122a-4049-a304-4696d7f9c17f",
  "isSidechain": true,
  "agentId": "aa34d3135a3369818",
  "requestId": "req_011CbYHCgiiWn5fVgsCmezgA",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "5f6c1e7d-6816-4579-8b9a-be96a1b12c03",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "27d805b7-0ea1-4632-9635-35f016c03b5a",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QuuWMSpREvRxWq84qKoBqT",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1128,
      "cache_read_input_tokens": 9029,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1128,
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

_source line 9 · 2026-05-30T06:28:37.130Z_

<details><summary>↩ Tool result · `toolu_01JSFdiczFiPe7m5F9K2bjwP`</summary>

```text
# ArXiv Paper Extraction: 2505.14069

**Title:** "Process vs. Outcome Reward: Which is Better for Agentic RAG Reinforcement Learning"

**Authors:** Wenlin Zhang, Xiangyang Li, Kuicai Dong, Yichao Wang, Pengyue Jia, Xiaopeng Li, Yingyi Zhang, Derong Xu, Zhaocheng Du, Huifeng Guo, Ruiming Tang, Xiangyu Zhao

**Category:** Computer Science - Information Retrieval (cs.IR)

**ArXiv Identifier:** 2505.14069

**Submission Timeline:**
- v1: May 20, 2025
- v2: May 22, 2025
- v3: December 8, 2025

**DOI:** https://doi.org/10.48550/arXiv.2505.14069

**Abstract Summary:**
The authors address limitations in traditional retrieval-augmented generation systems by proposing ReasonRAG, which employs process-level rewards rather than outcome-based signals. Their method constructs RAG-ProGuide, a dataset supporting fine-grained feedback for query generation, evidence extraction, and answer synthesis. The framework achieves competitive results on five benchmarks using merely "5k training instances, significantly fewer than the 90k training instances required by Search-R1," demonstrating improved efficiency and training stability.

**Available Formats:** PDF, HTML (experimental), TeX source, Audio summary
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "5f6c1e7d-6816-4579-8b9a-be96a1b12c03",
  "isSidechain": true,
  "promptId": "bbbe4bf2-b0a9-43d5-8f54-a157f509f7eb",
  "agentId": "aa34d3135a3369818",
  "type": "user",
  "uuid": "a5720d6c-0ad6-423f-b175-793ece1db7e9",
  "sourceToolAssistantUUID": "5f6c1e7d-6816-4579-8b9a-be96a1b12c03",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "27d805b7-0ea1-4632-9635-35f016c03b5a",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 10 · 2026-05-30T06:28:37.348Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_018PvvrUHQA7jhb33hEEW9AL`</summary>

```json
{
  "url": "https://arxiv.org/pdf/2505.14069",
  "prompt": "Extract the COMPLETE content of this research paper. I need:\n1. Full abstract\n2. Introduction - what gap did they identify, motivation\n3. Related work section - what prior work existed\n4. Method section - complete details of RAG-ProGuide, how process rewards work for query generation, evidence extraction, answer generation. All formulas and algorithmic details.\n5. Experimental setup - datasets, baselines, models used\n6. Results - ALL quantitative results, tables, key numbers including the 18x data efficiency claim\n7. Analysis and ablation studies\n8. Limitations section\n9. Whether this trains the retriever or the LLM\n10. Any discussion of process vs outcome rewards\nReturn EVERYTHING in detail. Do not summarize or skip sections."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a5720d6c-0ad6-423f-b175-793ece1db7e9",
  "isSidechain": true,
  "agentId": "aa34d3135a3369818",
  "requestId": "req_011CbYHCgiiWn5fVgsCmezgA",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "98297dda-9879-4cce-b9b8-dd65d3fa7c79",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "27d805b7-0ea1-4632-9635-35f016c03b5a",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QuuWMSpREvRxWq84qKoBqT",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1128,
      "cache_read_input_tokens": 9029,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1128,
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

_source line 11 · 2026-05-30T06:28:38.304Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_012nVh7wEQ8Zqv5nb1JBNSmA`</summary>

```json
{
  "query": "RAG-ProGuide \"Process vs Outcome Reward\" agentic RAG reinforcement learning Wenlin Zhang 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "98297dda-9879-4cce-b9b8-dd65d3fa7c79",
  "isSidechain": true,
  "agentId": "aa34d3135a3369818",
  "requestId": "req_011CbYHCgiiWn5fVgsCmezgA",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "a8efe38b-0dc5-46c1-b91f-9e408676d92e",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "27d805b7-0ea1-4632-9635-35f016c03b5a",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QuuWMSpREvRxWq84qKoBqT",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1128,
      "cache_read_input_tokens": 9029,
      "output_tokens": 427,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1128
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 427,
          "cache_read_input_tokens": 9029,
          "cache_creation_input_tokens": 1128,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1128,
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

_source line 12 · 2026-05-30T06:28:45.312Z_

<details><summary>↩ Tool result · `toolu_012nVh7wEQ8Zqv5nb1JBNSmA`</summary>

```text
Web search results for query: "RAG-ProGuide "Process vs Outcome Reward" agentic RAG reinforcement learning Wenlin Zhang 2025"

Links: [{"title":"[2505.14069] Process vs. Outcome Reward: Which is Better for Agentic RAG Reinforcement Learning","url":"https://arxiv.org/abs/2505.14069"},{"title":"(PDF) Process vs. Outcome Reward: Which is Better for Agentic RAG Reinforcement Learning","url":"https://www.researchgate.net/publication/391910704_Process_vs_Outcome_Reward_Which_is_Better_for_Agentic_RAG_Reinforcement_Learning"},{"title":"Process vs. Outcome Reward: Which is Better for Agentic RAG Reinforcement Learning | alphaXiv","url":"https://www.alphaxiv.org/overview/2505.14069v2"},{"title":"Process vs. Outcome Reward: Which is Better for Agentic RAG Reinforcement Learning","url":"https://arxiv.org/pdf/2505.14069"},{"title":"arXiv:2505.14069v2 [cs.IR] 22 May 2025","url":"https://arxiv.org/pdf/2505.14069v2"},{"title":"Process vs. Outcome Reward: Which is Better for Agentic RAG","url":"https://neurips.cc/media/neurips-2025/Slides/116682.pdf"},{"title":"Process vs. Outcome Reward: Which is Better for","url":"https://openreview.net/pdf?id=h3LlJ6Bh4S"},{"title":"Process vs. Outcome Reward: Which is Better for Agentic RAG Reinforcement Learning | OpenReview","url":"https://openreview.net/forum?id=h3LlJ6Bh4S"},{"title":"NeurIPS Poster Process vs. Outcome Reward: Which is Better for Agentic RAG Reinforcement Learning","url":"https://neurips.cc/virtual/2025/loc/san-diego/poster/116682"}]

I found relevant research on your query. Here are the key findings:

## Paper Overview

The paper "Process vs. Outcome Reward: Which is Better for Agentic RAG Reinforcement Learning" is authored by Wenlin Zhang and 11 other authors. The authors are affiliated with City University of Hong Kong and Noah's Ark Lab, Huawei.

## Main Contributions

The researchers propose ReasonRAG, an automatic framework for agentic RAG process-level reward annotations. They introduce a novel method that automatically constructs RAG-ProGuide, a high-quality dataset providing process-level rewards for query generation, evidence extraction, and answer generation.

## Key Problem Addressed

Recent advances like Search-R1 demonstrated gains using outcome-based reinforcement learning, but such outcome-supervised agentic RAG methods face challenges including low exploration efficiency, gradient conflict, and sparse reward signals.

## Main Finding

ReasonRAG demonstrates that process-supervised reinforcement learning, guided by fine-grained intermediate rewards, significantly enhances the training efficiency and performance of agentic RAG systems, outperforming outcome-supervised approaches by achieving higher accuracy with substantially less training data.

The RAG-ProGUIDE dataset provides fine-grained, process-level rewards for query generation, evidence extraction, and answer generation.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a8efe38b-0dc5-46c1-b91f-9e408676d92e",
  "isSidechain": true,
  "promptId": "bbbe4bf2-b0a9-43d5-8f54-a157f509f7eb",
  "agentId": "aa34d3135a3369818",
  "type": "user",
  "uuid": "ba71e05b-1e54-432b-8be3-d21a0358e5f0",
  "sourceToolAssistantUUID": "a8efe38b-0dc5-46c1-b91f-9e408676d92e",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "27d805b7-0ea1-4632-9635-35f016c03b5a",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 13 · 2026-05-30T06:28:46.301Z_

<details><summary>↩ Tool result · `toolu_018PvvrUHQA7jhb33hEEW9AL`</summary>

```text
I appreciate your detailed request, but I need to clarify what I'm working with. The content you provided is a PDF file structure (object references, metadata, and encoded streams) rather than readable text. The actual paper content is compressed/encoded in the stream objects, which I cannot directly decompress and read.

However, based on the metadata visible in the PDF header, I can confirm this is:

**"Process vs. Outcome Reward: Which is Better for Agentic RAG Reinforcement Learning"**
- Authors: Wenlin Zhang, Xiangyang Li, Kuicai Dong, and others
- arXiv ID: 2505.14069v3
- Published: December 9, 2025

To properly extract and summarize this research paper as you've requested, I would need:

1. **The actual readable text content** of the paper (PDF text layer or plain text version)
2. Or access to the paper directly from arXiv or the authors' repository

**What I cannot do:**
- Decompress the binary stream objects in this PDF structure
- Extract meaningful content from encoded PDF data without rendering tools

**What I recommend:**
- Visit: https://arxiv.org/abs/2505.14069v3
- Download the PDF directly and share it in a text-readable format, or
- Share the abstract and sections as plain text

Once you provide readable content, I'll gladly deliver the comprehensive analysis you requested, covering all sections from abstract through limitations, while respecting the 125-character quote limit and proper attribution.

[Binary content (application/pdf, 1.2MB) also saved to /home/ubuntu/.claude-account-2/projects/-home-ubuntu-idea-adversarial/27d805b7-0ea1-4632-9635-35f016c03b5a/tool-results/webfetch-1780122517388-wy0ec5.pdf]
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "98297dda-9879-4cce-b9b8-dd65d3fa7c79",
  "isSidechain": true,
  "promptId": "bbbe4bf2-b0a9-43d5-8f54-a157f509f7eb",
  "agentId": "aa34d3135a3369818",
  "type": "user",
  "uuid": "b8bca47e-a180-4c3e-8bbf-9488ce930327",
  "sourceToolAssistantUUID": "98297dda-9879-4cce-b9b8-dd65d3fa7c79",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "27d805b7-0ea1-4632-9635-35f016c03b5a",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 14 · 2026-05-30T06:28:49.361Z_

Good, I have the abstract and some overview. The PDF didn't parse well, so let me try the HTML version and also fetch the OpenReview page for reviews, plus the NeurIPS page.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b8bca47e-a180-4c3e-8bbf-9488ce930327",
  "isSidechain": true,
  "agentId": "aa34d3135a3369818",
  "requestId": "req_011CbYHE58NtaEahXmcxJSmf",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "5f9ddc5b-a24a-4fdb-b009-b00ce2b56b19",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "27d805b7-0ea1-4632-9635-35f016c03b5a",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01ErX7bRLBAnMH1me4oN1nfX",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 859,
      "cache_creation_input_tokens": 1268,
      "cache_read_input_tokens": 10157,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1268,
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

_source line 15 · 2026-05-30T06:28:54.660Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_014hsC8ekN2CGDCdBDumABX3`</summary>

```json
{
  "url": "https://arxiv.org/html/2505.14069",
  "prompt": "Extract the COMPLETE content of this research paper in full detail. I need EVERYTHING:\n1. Full abstract verbatim\n2. Introduction - what gap, motivation, key claims\n3. Related work\n4. Method section - COMPLETE details of ReasonRAG/RAG-ProGuide: how process rewards are constructed for (a) query generation, (b) evidence extraction, (c) answer generation. All formulas, reward functions, training procedures.\n5. Experimental setup - datasets, baselines, models, hyperparameters\n6. ALL quantitative results from tables - exact numbers\n7. Analysis, ablation studies\n8. Limitations\n9. Whether this trains the retriever or the LLM\nDo NOT skip or summarize any section. Return everything."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5f9ddc5b-a24a-4fdb-b009-b00ce2b56b19",
  "isSidechain": true,
  "agentId": "aa34d3135a3369818",
  "requestId": "req_011CbYHE58NtaEahXmcxJSmf",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "d72023f9-cc67-4240-9c98-812744194953",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "27d805b7-0ea1-4632-9635-35f016c03b5a",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01ErX7bRLBAnMH1me4oN1nfX",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 859,
      "cache_creation_input_tokens": 1268,
      "cache_read_input_tokens": 10157,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1268,
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

_source line 16 · 2026-05-30T06:28:56.457Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01HyQ2eerWCmyVDqzF2ZZ1QY`</summary>

```json
{
  "url": "https://openreview.net/forum?id=h3LlJ6Bh4S",
  "prompt": "Extract ALL reviews and discussion about this paper. Include reviewer scores, detailed comments, strengths, weaknesses, questions, and any author responses. Return everything comprehensively."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d72023f9-cc67-4240-9c98-812744194953",
  "isSidechain": true,
  "agentId": "aa34d3135a3369818",
  "requestId": "req_011CbYHE58NtaEahXmcxJSmf",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "40e77867-67c2-4c56-a001-97f5c1e3adcf",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "27d805b7-0ea1-4632-9635-35f016c03b5a",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01ErX7bRLBAnMH1me4oN1nfX",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 859,
      "cache_creation_input_tokens": 1268,
      "cache_read_input_tokens": 10157,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1268,
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

_source line 17 · 2026-05-30T06:28:57.311Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01452kgcHbmFezohUA5C7bgJ`</summary>

```json
{
  "url": "https://www.alphaxiv.org/overview/2505.14069v2",
  "prompt": "Extract all discussion, comments, and analysis about this paper. Include any community feedback, questions, or critiques."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "40e77867-67c2-4c56-a001-97f5c1e3adcf",
  "isSidechain": true,
  "agentId": "aa34d3135a3369818",
  "requestId": "req_011CbYHE58NtaEahXmcxJSmf",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "58d6ef42-0d0f-4e7c-86d8-f78b1e51a98f",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "27d805b7-0ea1-4632-9635-35f016c03b5a",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01ErX7bRLBAnMH1me4oN1nfX",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 859,
      "cache_creation_input_tokens": 1268,
      "cache_read_input_tokens": 10157,
      "output_tokens": 494,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1268
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 859,
          "output_tokens": 494,
          "cache_read_input_tokens": 10157,
          "cache_creation_input_tokens": 1268,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1268,
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

_source line 18 · 2026-05-30T06:28:57.565Z_

<details><summary>↩ Tool result · `toolu_01452kgcHbmFezohUA5C7bgJ`</summary>

```text
The server returned HTTP 403 Forbidden.

The response body was not retrieved. If this URL requires authentication, use an authenticated tool (e.g. `gh` for GitHub, or an MCP-provided fetch tool) instead of WebFetch.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "58d6ef42-0d0f-4e7c-86d8-f78b1e51a98f",
  "isSidechain": true,
  "promptId": "bbbe4bf2-b0a9-43d5-8f54-a157f509f7eb",
  "agentId": "aa34d3135a3369818",
  "type": "user",
  "uuid": "bcc2bf3d-9022-4c4f-9069-6c06715e38b5",
  "sourceToolAssistantUUID": "58d6ef42-0d0f-4e7c-86d8-f78b1e51a98f",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "27d805b7-0ea1-4632-9635-35f016c03b5a",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 19 · 2026-05-30T06:28:59.760Z_

<details><summary>↩ Tool result · `toolu_01HyQ2eerWCmyVDqzF2ZZ1QY`</summary>

```text
# Reviews and Discussion for ReasonRAG Paper

Based on the provided web page content, I cannot extract any reviews or discussion comments about this paper.

**Why:** The page content shows only the paper's title, abstract, author list, and metadata from OpenReview.net. It does not include:

- Reviewer scores or ratings
- Detailed reviewer comments
- Strengths and weaknesses assessments
- Reviewer questions
- Author responses or rebuttals
- Any discussion thread content

**What is visible:**
The abstract mentions the paper addresses "process vs. outcome reward" in agentic RAG systems, presenting ReasonRAG with the RAG-ProGUIDE dataset. However, the actual peer review section—which would contain the comprehensive feedback you're requesting—is not included in the provided content.

To access reviews and discussions, you would need to visit the full OpenReview page directly and scroll to the "Reviews" and "Discussion" sections.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "40e77867-67c2-4c56-a001-97f5c1e3adcf",
  "isSidechain": true,
  "promptId": "bbbe4bf2-b0a9-43d5-8f54-a157f509f7eb",
  "agentId": "aa34d3135a3369818",
  "type": "user",
  "uuid": "771beea5-dde8-4cec-a5bc-b4091b3dcda3",
  "sourceToolAssistantUUID": "40e77867-67c2-4c56-a001-97f5c1e3adcf",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "27d805b7-0ea1-4632-9635-35f016c03b5a",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-30T06:29:54.392Z_

<details><summary>↩ Tool result · `toolu_014hsC8ekN2CGDCdBDumABX3`</summary>

````text
# Complete Research Paper Extraction: ReasonRAG

## 1. ABSTRACT (Verbatim)

"Retrieval-augmented generation (RAG) enhances the text generation capabilities of large language models (LLMs) by integrating external knowledge and up-to-date information. However, traditional RAG systems are limited by static workflows and lack the adaptability required for multistep reasoning and complex task management. To address these limitations, agentic RAG systems (e.g., DeepResearch) have been proposed, enabling dynamic retrieval strategies, iterative context refinement, and adaptive workflows for handling complex search queries beyond the capabilities of conventional RAG. Recent advances, such as Search-R1, have demonstrated promising gains using outcome-based reinforcement learning, where the correctness of the final answer serves as the reward signal. Nevertheless, such outcome-supervised agentic RAG methods face challenges including low exploration efficiency, gradient conflict, and sparse reward signals. To overcome these challenges, we propose to utilize fine-grained, process-level rewards to improve training stability, reduce computational costs, and enhance efficiency. Specifically, we introduce a novel method ReasonRAG that automatically constructs RAG-ProGuide, a high-quality dataset providing process-level rewards for (i) query generation, (ii) evidence extraction, and (iii) answer generation, thereby enhancing model inherent capabilities via process-supervised reinforcement learning. With the process-level policy optimization, the proposed framework empowers LLMs to autonomously invoke search, generate queries, extract relevant evidence, and produce final answers. Compared to existing approaches such as Search-R1 and traditional RAG systems, ReasonRAG, leveraging RAG-ProGuide, achieves superior performance on five benchmark datasets using only 5k training instances, significantly fewer than the 90k training instances required by Search-R1."

## 2. INTRODUCTION

**Gap & Motivation:**
The document identifies three core limitations of outcome-supervised RL for agentic RAG:
- "Low exploration efficiency occurs since the model must generate a complete reasoning chain before receiving any reward"
- "Gradient conflict arises when mistakes occur late in the reasoning process; the entire sequence (including correct early steps) is penalized"
- "Rewards are sparse, as outcome-supervised RL only provides feedback upon producing the final answer"

**Key Claims:**
Process-supervised RL addresses these issues by "providing fine-grained, stepwise rewards throughout the reasoning process, enabling more efficient exploration, reducing gradient conflict, and accelerating model learning through denser feedback."

**Central Challenge:**
Two obstacles exist: (1) Process Reward Design requiring "effective process rewards are essential for guiding the model toward the shortest and most efficient correct reasoning path"; (2) Exploration Efficiency where "While human annotators...can create high-quality process-level annotations...this approach is prohibitively expensive"

## 3. RELATED WORK

**Prompt-Based Agentic RAG:**
Early approaches leverage "manually designed workflows to elicit the inherent capabilities of LLMs for interacting with external information." The field lacks explicit mechanisms for autonomous search invocation and struggles with manual design requirements for new domains.

**RL-Based Agentic RAG:**
"Reinforcement Learning (RL) has consistently delivered significant performance gains across sequential decision-making tasks." Recent work extended "outcome-supervised reinforcement learning to RAG, empowering LLMs to autonomously utilize search engines." The document notes that "outcome-supervised RL faces challenges such as reward sparsity, training instability, and substantial computational cost," while "process-supervised RL has recently been applied to enhance reasoning abilities, outperforming outcome-supervised approaches by providing fine-grained rewards" but "process-supervised RL for RAG remains unexplored."

## 4. METHOD SECTION: REASONRAG COMPLETE DETAILS

### 4.1 Framework Overview

ReasonRAG consists of three phases:
1. Process-supervised data generation (SPRE + MCTS)
2. Process-supervised preference optimization (DPO)
3. Agentic RAG inference

### 4.2 Shortest Path Reward Estimation (SPRE)

**Core Formula (Equation 1):**
```
Q_t = MonteCarlo(x, y_{1:t}) = (1/k) * Σ_{i=1}^k v(rollout_i) * α^{step(rollout_i)}
```

**Components:**
- `rollout_i`: i-th simulated completion of partial sequence y_{1:t}
- `v(rollout_i) ∈ [0,1]`: Correctness score (F1 match to ground truth)
- `step(rollout_i)`: Total number of reasoning steps in trajectory
- `α ∈ (0,1]`: Decay factor penalizing long reasoning paths

**Purpose:** "This reward encourages the model to favor trajectories that achieve correct answers with fewer steps, thus balancing accuracy and efficiency in agentic RAG reasoning."

### 4.3 Monte Carlo Tree Search (MCTS) for Process-level Exploration

**State Definition:**
s = (x, y_{&lt;i}, stage), where:
- x: original question
- y_{&lt;i}: sequence of prior reasoning outputs
- stage ∈ {Reasoning, Grounding, Terminal}

**Actions by Stage:**
- **Reasoning stage:** Choose between generating new query for retrieval OR producing final answer
- **Grounding stage:** Extract evidence spans from retrieved documents
- **Terminal stage:** End exploration

**Policy (Equation 2):**
```
π(a|s) = LLM(a|s) = {
  π_θ(·|x, y_{&lt;i}, p_stage), if stage is Reasoning
  π_θ(·|x, y_{&lt;i}, docs, p_stage), otherwise
}
```

**State Transitions:**
s_{t+1} = concatenate(s_t, a_t)

**MCTS Operations:**

1. **Selection (UCB-based, Equation 5):**
```
s_i* = argmax_{s_i ∈ children(s)} [Q(s_i) + c_uct * √(Σ_i N(s_i))/(1+N(s_i))]
```
where c_uct controls exploration-exploitation tradeoff

2. **Expansion:**
- Generate next action via Equation 4
- Initialize new child node with generated response
- Evaluate correctness via LLM judgment (Equation 6):
```
v(s) = π_θ(·|x, y_{1:t}, answer, p_eval)
```
This avoids time-consuming full simulations

3. **Backpropagation:**
- Update Q(s_t) using Equation 1
- Increment visit counts: N(s) ← N(s) + 1 for all traversed nodes

### 4.4 RAG-ProGuide Dataset Construction

**Sampling Strategy:**
- 3,000 questions each from PopQA, HotpotQA, 2WikiMultiHopQA
- Total: 4,603 questions after processing

**Reward Computation:**
- Compute F1 score between predicted and ground truth answers
- Use correctness signal to estimate intermediate node rewards via SPRE
- Propagate rewards through MCTS tree for preference pair selection

**Post-Processing Filtering:**
- Remove preference pairs with identical response sequences
- Discard pairs with reward difference < 0.01

**Final Dataset Statistics (Table 1):**
- 4,603 questions
- 13,289 distinct preference pairs
- Action distribution:
  - Query Generation: 3,295 (24.8%)
  - Evidence Extraction: 4,305 (32.4%)
  - Answer Generation: 5,689 (42.8%)
- Iteration range: min/med/max 1/3/5 (avg 2.7)
- Token length: min/med/max 9/60/625 (avg 65.5)

**Dataset Characteristics (Figure 3):**
- Pair types show diverse comparative scenarios (diverse action type combinations)
- Iteration counts range reflecting multi-hop complexity
- Token length distribution confirms various response complexities
- Reward gap distribution spans wide range, ensuring rich preference learning signal

### 4.5 Process-Supervised Preference Optimization

**Training Objective (Equation 3):**
```
L(θ) = -E_{(x, y_{&lt;t}, y_t^w, y_t^l)~D} [log σ(β log p_θ(y_t^w|x,y_{&lt;t}) / p_θ(y_t^l|x,y_{&lt;t}))]
```

**Variables:**
- x: original question
- y_{&lt;t}: responses from previous reasoning steps
- y_t^w: preferred response in subsequent step
- y_t^l: dispreferred response in subsequent step
- β: hyperparameter controlling KL constraint

**Method:** Direct Preference Optimization (DPO)

### 4.6 Agentic RAG Inference (Algorithm 1)

**Workflow:**
1. Initialize: reasoning count i ← 0, stage ← Reasoning
2. Loop until terminal (max N rounds):
   - In Reasoning stage: y_i ~ π_θ(·|x, y_{&lt;i}, p_stage)
   - In other stages: y_i ~ π_θ(·|x, y_{&lt;i}, docs, p_stage)
   - Append y_i to response
   - If "&lt;query>" detected: stage ← Grounding, retrieve docs
   - If "&lt;answer>" detected: stage ← Terminal, return answer
   - If "&lt;evidence>" detected: stage ← Reasoning
3. Return final response

**Key Features:**
- Three recursive decision states (Reasoning, Grounding, Terminal)
- Explicit placeholder use (&lt;query>, &lt;/query>, &lt;answer>, &lt;/answer>, &lt;evidence>, &lt;/evidence>) for interpretability
- Structured decision control enabling programmatic deployment

## 5. EXPERIMENTAL SETUP

### 5.1 Datasets & Metrics

**Evaluation Datasets:**
- **Single-hop:** PopQA
- **Multi-hop:** HotpotQA, 2WikiMultiHopQA, Bamboogle, MuSiQue
- **Training set:** 4,603 questions from PopQA (704), HotpotQA (2,843), 2WikiMultiHopQA (1,056)
- **Test set sizes (Table 4):**
  - PopQA: 11,267
  - HotpotQA: 7,405
  - 2WikiMultiHopQA: 12,576
  - Bamboogle: 125
  - MuSiQue: 2,417

**Metrics:**
- Exact Match (EM): Percentage of predictions exactly matching reference answers
- F1 Score: Token-level overlap between predicted and ground-truth answers

### 5.2 Baselines (12 total, 6 categories)

**Zero-shot:**
- Naïve Generation
- Standard RAG

**Active:**
- FLARE
- Self-RAG (146k)

**Adaptive:**
- AdaptiveRAG (3k)

**RAG-CoT:**
- Iter-Retgen
- IRCoT

**Summary:**
- RECOMP
- LongLLMLingua
- Selective-Context

**Reasoning:**
- Search-o1
- AutoRAG (10k)
- Search-R1 (90k)

### 5.3 Model Configuration

**Backbone:** Qwen2.5-7B-Instruct (same across all methods for fair comparison)
**Retriever:** BGE (BAAI/bge-base-en-v1.5)
**Knowledge Source:** Wikidump 2018 augmented with dataset-specific content
**Retrieval Setting:** Top-3 documents per query (unless tested otherwise)

### 5.4 Training Details

**ReasonRAG-specific:**
- Process-level policy optimization via DPO
- Dataset: RAG-ProGuide (5k queries, 13k preference pairs)
- No explicit hyperparameter specification for β in paper

**Baseline implementations** detailed in Appendix E.2, utilizing FlashRAG toolkit

## 6. QUANTITATIVE RESULTS

### 6.1 Main Results (Table 2: Complete Numbers)

| Method | PopQA EM | PopQA F1 | HotpotQA EM | HotpotQA F1 | 2Wiki EM | 2Wiki F1 | Bamboogle EM | Bamboogle F1 | MuSiQue EM | MuSiQue F1 | Avg EM | Avg F1 |
|--------|----------|----------|-------------|-------------|----------|----------|--------------|--------------|-----------|-----------|--------|--------|
| Naïve Generation | 12.7 | 16.5 | 15.7 | 24.8 | 20.2 | 28.0 | 6.4 | 17.4 | 2.7 | 10.2 | 11.5 | 19.4 |
| Standard RAG | 38.4 | 44.7 | 29.3 | 39.9 | 29.4 | 36.3 | 17.6 | 24.1 | 6.7 | 15.1 | 24.3 | 32.0 |
| FLARE | 14.3 | 17.6 | 18.1 | 25.7 | 27.9 | 32.8 | 12.0 | 20.8 | 4.3 | 12.6 | 15.3 | 21.9 |
| Self-RAG | 22.7 | 33.9 | 21.0 | 29.7 | 12.0 | 25.2 | 1.6 | 10.9 | 4.6 | 13.3 | 12.4 | 22.6 |
| AdaptiveRAG | 36.6 | 41.5 | 29.1 | 40.7 | 24.2 | 33.4 | 18.4 | 26.1 | 6.9 | 14.3 | 23.0 | 31.2 |
| Iter-Retgen | 38.7 | 44.9 | 30.3 | 42.1 | 31.2 | 38.7 | 19.2 | 26.4 | 7.7 | 14.2 | 25.4 | 33.3 |
| IRCoT | 36.2 | 43.6 | 27.7 | 41.5 | 23.5 | 32.5 | 17.2 | 22.5 | 8.6 | 13.2 | 22.6 | 30.7 |
| RECOMP | 40.5 | 45.8 | 29.7 | 41.2 | 33.2 | 39.4 | 21.7 | 28.6 | 9.2 | 15.8 | 26.9 | 34.2 |
| LongLLMLingua | 39.2 | 45.1 | 31.4 | 43.2 | 34.5 | 40.2 | 20.3 | 27.4 | 8.7 | 14.9 | 26.8 | 34.2 |
| Selective-Context | 34.9 | 41.5 | 19.3 | 27.3 | 20.3 | 29.7 | 15.3 | 22.6 | 6.1 | 13.7 | 19.2 | 27.0 |
| Search-o1 | 33.2 | 40.3 | 24.8 | 38.1 | 16.4 | 27.1 | 30.4 | 40.6 | 6.3 | 13.7 | 22.2 | 31.96 |
| AutoRAG | 38.6 | 44.1 | 33.3 | 43.7 | 39.5 | 46.1 | 24.8 | 32.2 | 11.3 | 18.3 | 29.5 | 36.9 |
| Search-R1 | 39.7 | 44.8 | 37.0 | 47.0 | 41.4 | 48.0 | 32.0 | 43.8 | 14.6 | 19.9 | 32.8 | 40.7 |
| **ReasonRAG** | **41.5*** | **46.2*** | **38.4*** | **48.9*** | **43.6*** | **50.4*** | **36.0*** | **45.5*** | 12.8 | **20.6*** | **34.4*** | **42.3*** |

*\*indicates statistical significance (two-sided t-test, p<0.05)*

**Key Findings:**
- ReasonRAG trained on 5k queries outperforms Search-R1 (90k queries)
- Average EM improvement: 34.4% vs 32.8% (1.6 percentage point gain)
- Average F1 improvement: 42.3% vs 40.7% (1.6 percentage point gain)
- Strong multi-hop performance: HotpotQA F1 48.9% vs AutoRAG 43.7%, Search-R1 47.0%
- Robust out-of-domain generalization on Bamboogle, MuSiQue

### 6.2 Training Efficiency (Figure 5)

**Comparison:** ReasonRAG vs Search-R1 convergence speed measured in GPU hours

**Findings:**
- "ReasonRAG has higher training efficiency compared to Search-R1. ReasonRAG achieves superior EM scores with fewer GPU hours"
- Single-hop (PopQA): "performance gains for both models are comparably rapid"
- Multi-hop (2WikiMultiHopQA, HotpotQA): "ReasonRAG consistently demonstrates significant improvements with increased GPU hours"

### 6.3 Optimization Strategy Ablation (Table 3)

| Method | PopQA EM | PopQA F1 | HotpotQA EM | HotpotQA F1 | 2Wiki EM | 2Wiki F1 | Bamboogle EM | Bamboogle F1 | MuSiQue EM | MuSiQue F1 | Avg EM | Avg F1 |
|--------|----------|----------|-------------|-------------|----------|----------|--------------|--------------|-----------|-----------|--------|--------|
| Base | 35.6 | 42.7 | 23.7 | 38.2 | 15.2 | 28.9 | 28.0 | 38.7 | 7.7 | 15.4 | 22.0 | 32.8 |
| SFT | 31.6 | 37.4 | 26.8 | 38.7 | 35.1 | 40.9 | 17.6 | 27.3 | 8.6 | 15.5 | 23.9 | 32.0 |
| RL-ORL (5k) | 23.0 | 30.9 | 28.1 | 32.6 | 32.0 | 43.8 | 17.5 | 24.1 | 5.9 | 13.1 | 21.3 | 28.9 |
| RL-ORL (10k) | 39.5 | 45.7 | 36.7 | 46.7 | 40.5 | 47.2 | 30.7 | 40.6 | 12.6 | 19.5 | 32.0 | 39.9 |
| **RL-PRL** | **41.5** | **46.2** | **38.4** | **48.9** | **43.6** | **50.4** | **36.0** | **45.5** | **12.8** | **20.6** | **34.5** | **42.3** |

**Findings:**
- "ReasonRAG (PRL) consistently outperforms all other variants across all datasets, both in-domain and out-of-domain"
- "ReasonRAG (ORL) achieves the second-best results, but requires substantially more training data to match comparable performance of PRL"
- "SFT leads to overfitting on multi-hop reasoning paths, resulting in reduced performance on single-hop tasks"

### 6.4 Impact of Retrieval Iterations (Figure 6)

**Performance vs. Retrieval Steps:**
- PopQA: Converges at 2-3 steps
- 2WikiMultiHopQA: Requires 3-5 steps
- HotpotQA: Requires 3-5 steps
- Base model (without optimization) "struggles to handle multi-hop settings"

### 6.5 Impact of Retrieved Document Count (Figure 7)

**Top-k Retrieved Documents:**
- k=1: Limited context restricts reasoning
- k=3: Significant improvements across all datasets
- k=5: No further improvement on PopQA/HotpotQA; 2WikiMultiHopQA continues benefiting

## 7. ANALYSIS

### 7.1 Data Efficiency Claims

"ReasonRAG, despite being trained on only 5k queries, outperforms the search-R1 baseline trained with 90k queries."

### 7.2 Multi-hop Reasoning Strength

"ReasonRAG shows substantial performance gains on multi-hop reasoning tasks. On the HotpotQA dataset, it achieves an F1 score of 48.9%, outperforming models like AutoRAG (43.7% F1) and search-R1 (47.0% F1)"

### 7.3 Out-of-domain Generalization

"ReasonRAG demonstrates strong generalization to out-of-domain data. On challenging benchmarks such as Bamboogle and MuSiQue, it consistently achieves higher F1 scores"

### 7.4 Process vs. Outcome Supervision

The ablation clearly demonstrates process-supervised RL superiority. "Reward sparsity relies on more training data and steps to converge" for outcome-supervised approaches, whereas process-supervision provides "denser feedback."

## 8. LIMITATIONS

**Appendix H states:**
"We employ process-supervised RL to optimize the model policy...acquiring sufficient data for process-level annotation incurs a higher time cost compared to outcome supervision during data rollout. Nevertheless, as the training efficiency verifies, our data exhibits superior quality, enabling models to achieve greater performance gains with fewer data samples."

**Additional limitations mentioned:**
- Process-level exploration requires more iterations than outcome-level
- Higher annotation effort per sample despite lower sample count overall

## 9. WHAT IS BEING TRAINED: LLM vs. RETRIEVER

**Critical Finding:** The paper trains **ONLY THE LANGUAGE MODEL (LLM)**, NOT the retriever.

**Evidence:**
1. Section 4.5 explicitly uses "Direct Preference Optimization (DPO)" to tune "the policy model" - defined as π_θ, an LLM
2. Appendix E.1: "We employ BGE as our retriever" - static/fixed component
3. Algorithm 1 shows inference uses fixed retriever ℛ: "docs ← ℛ(q)"
4. All experiments use identical BGE retriever across all methods
5. Training objective (Equation 3) optimizes p_θ(...) - the LLM's conditional probability distribution

**Retriever Role:** Static information retrieval component providing top-3 passages; no gradient flow or parameter updates applied.

---

## SUMMARY OF KEY TECHNICAL INNOVATIONS

1. **SPRE Algorithm:** Monte Carlo-based reward estimation with step-based decay encouraging shortest valid paths
2. **MCTS Integration:** Efficient exploration of RAG decision space using UCB-based node selection
3. **RAG-ProGuide Dataset:** 4.6k questions × 13k preference pairs with process-level supervision across query generation, evidence extraction, answer generation
4. **Process-supervised DPO:** Preference optimization at intermediate reasoning steps rather than final outcomes
5. **Three-stage workflow:** Reasoning → Grounding → Terminal state machine for structured agentic interaction
````

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d72023f9-cc67-4240-9c98-812744194953",
  "isSidechain": true,
  "promptId": "bbbe4bf2-b0a9-43d5-8f54-a157f509f7eb",
  "agentId": "aa34d3135a3369818",
  "type": "user",
  "uuid": "6f171aa7-c1cf-4b70-a9bb-1a1d1548d578",
  "sourceToolAssistantUUID": "d72023f9-cc67-4240-9c98-812744194953",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "27d805b7-0ea1-4632-9635-35f016c03b5a",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 21 · 2026-05-30T06:29:57.560Z_

Excellent, the HTML version gave me comprehensive content. Let me now try to get the OpenReview reviews and search for additional discussion/commentary.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6f171aa7-c1cf-4b70-a9bb-1a1d1548d578",
  "isSidechain": true,
  "agentId": "aa34d3135a3369818",
  "requestId": "req_011CbYHK6EFLU4VfRseJHxct",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "03c7257e-6943-46a9-b868-d0f1bc7a80c0",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "27d805b7-0ea1-4632-9635-35f016c03b5a",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FhafSdwRLKbFQaofddXUXp",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 316,
      "cache_creation_input_tokens": 7517,
      "cache_read_input_tokens": 11425,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 7517,
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

_source line 22 · 2026-05-30T06:29:58.038Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_017u8sZ7WWuazsjSvyRo9h7p`</summary>

```json
{
  "query": "ReasonRAG RAG-ProGuide NeurIPS 2025 review discussion process reward agentic RAG"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "03c7257e-6943-46a9-b868-d0f1bc7a80c0",
  "isSidechain": true,
  "agentId": "aa34d3135a3369818",
  "requestId": "req_011CbYHK6EFLU4VfRseJHxct",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "9ac23f1f-bd27-4da4-b111-7959dc8e2e9e",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "27d805b7-0ea1-4632-9635-35f016c03b5a",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FhafSdwRLKbFQaofddXUXp",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 316,
      "cache_creation_input_tokens": 7517,
      "cache_read_input_tokens": 11425,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 7517,
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

_source line 23 · 2026-05-30T06:30:00.453Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01HnPYBFMMAMN3StwRW3ydTa`</summary>

```json
{
  "url": "https://openreview.net/forum?id=h3LlJ6Bh4S",
  "prompt": "Extract all reviewer comments, scores, ratings, strengths, weaknesses, questions, and author responses. Look for any review sections, decision sections, or discussion threads. Return everything available."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9ac23f1f-bd27-4da4-b111-7959dc8e2e9e",
  "isSidechain": true,
  "agentId": "aa34d3135a3369818",
  "requestId": "req_011CbYHK6EFLU4VfRseJHxct",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "f87a3e5c-158e-4a7c-b3b5-56e48f5daefd",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "27d805b7-0ea1-4632-9635-35f016c03b5a",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FhafSdwRLKbFQaofddXUXp",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 316,
      "cache_creation_input_tokens": 7517,
      "cache_read_input_tokens": 11425,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 7517,
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

_source line 24 · 2026-05-30T06:30:00.719Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_016ahVbq9TkHAVTQkfPP3WRq`</summary>

```json
{
  "query": "site:openreview.net \"Process vs. Outcome Reward\" \"agentic RAG\" reviews scores"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f87a3e5c-158e-4a7c-b3b5-56e48f5daefd",
  "isSidechain": true,
  "agentId": "aa34d3135a3369818",
  "requestId": "req_011CbYHK6EFLU4VfRseJHxct",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "e30322d3-a3c6-48f5-8236-027423130fbf",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "27d805b7-0ea1-4632-9635-35f016c03b5a",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FhafSdwRLKbFQaofddXUXp",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 316,
      "cache_creation_input_tokens": 7517,
      "cache_read_input_tokens": 11425,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 7517,
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

_source line 25 · 2026-05-30T06:30:03.292Z_

<details><summary>↩ Tool result · `toolu_01HnPYBFMMAMN3StwRW3ydTa`</summary>

```text
# Review Information

Based on the provided web page content, **no reviewer comments, scores, ratings, strengths, weaknesses, questions, or author responses are available**.

The page displays only the paper's title, abstract, author list, and metadata for a NeurIPS 2025 submission titled "Process vs. Outcome Reward: Which is Better for Agentic RAG Reinforcement Learning."

The abstract describes a method called ReasonRAG that uses "process-supervised reinforcement learning" to improve agentic RAG systems, utilizing a dataset with "fine-grained, process-level rewards" and achieving results with fewer training instances than comparable approaches.

To access review information, one would need to navigate to additional sections of the OpenReview page not included in this excerpt, such as dedicated review or discussion tabs.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f87a3e5c-158e-4a7c-b3b5-56e48f5daefd",
  "isSidechain": true,
  "promptId": "bbbe4bf2-b0a9-43d5-8f54-a157f509f7eb",
  "agentId": "aa34d3135a3369818",
  "type": "user",
  "uuid": "3bee0869-93ba-41cf-8990-da846a9ae19b",
  "sourceToolAssistantUUID": "f87a3e5c-158e-4a7c-b3b5-56e48f5daefd",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "27d805b7-0ea1-4632-9635-35f016c03b5a",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 26 · 2026-05-30T06:30:07.156Z_

<details><summary>↩ Tool result · `toolu_016ahVbq9TkHAVTQkfPP3WRq`</summary>

```text
Web search results for query: "site:openreview.net "Process vs. Outcome Reward" "agentic RAG" reviews scores"

Links: [{"title":"Process vs. Outcome Reward: Which is Better for Agentic RAG Reinforcement Learning | OpenReview","url":"https://openreview.net/forum?id=h3LlJ6Bh4S"},{"title":"Process vs. Outcome Reward: Which is Better for Agentic RAG Reinforcement Learning","url":"https://arxiv.org/pdf/2505.14069"},{"title":"Process vs. Outcome Reward: Which is Better for","url":"https://openreview.net/pdf?id=h3LlJ6Bh4S"},{"title":"HiPRAG: Hierarchical Process Rewards for Efficient Agentic Retrieval Augmented Generation","url":"https://arxiv.org/pdf/2510.07794"},{"title":"Search-P1: Path-Centric Reward Shaping for Stable and Efficient Agentic RAG Training","url":"https://arxiv.org/pdf/2602.22576"}]

I found the paper on OpenReview! Here are the results:

**Paper Title:** "Process vs. Outcome Reward: Which is Better for Agentic RAG Reinforcement Learning"

**Key Details:**
- **Source:** https://openreview.net/forum?id=h3LlJ6Bh4S
- **Posted:** October 29, 2025

**Summary:**
The paper addresses how retrieval-augmented generation (RAG) systems struggle with static workflows and limited adaptability, while agentic RAG systems like DeepResearch enable dynamic retrieval and adaptive workflows. The authors argue that outcome-based reinforcement learning methods face challenges like low exploration efficiency and sparse rewards, and propose ReasonRAG, which uses process-level rewards for query generation, evidence extraction, and answer generation to enhance LLMs' autonomous capabilities.

The paper appears to be a recent research contribution comparing process-based versus outcome-based reward signals for training agentic RAG systems. However, the search results don't include the specific review scores from the OpenReview submission. To view the detailed review scores and comments, you would need to visit the OpenReview page directly at the link above.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "e30322d3-a3c6-48f5-8236-027423130fbf",
  "isSidechain": true,
  "promptId": "bbbe4bf2-b0a9-43d5-8f54-a157f509f7eb",
  "agentId": "aa34d3135a3369818",
  "type": "user",
  "uuid": "e546df49-2ea0-48d0-bd06-7f5d09dc39ae",
  "sourceToolAssistantUUID": "e30322d3-a3c6-48f5-8236-027423130fbf",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "27d805b7-0ea1-4632-9635-35f016c03b5a",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 27 · 2026-05-30T06:30:07.644Z_

<details><summary>↩ Tool result · `toolu_017u8sZ7WWuazsjSvyRo9h7p`</summary>

```text
Web search results for query: "ReasonRAG RAG-ProGuide NeurIPS 2025 review discussion process reward agentic RAG"

Links: [{"title":"NeurIPS Poster Process vs. Outcome Reward: Which is Better for Agentic RAG Reinforcement Learning","url":"https://neurips.cc/virtual/2025/poster/116682"},{"title":"Process vs. Outcome Reward: Which is Better for Agentic RAG Reinforcement Learning","url":"https://arxiv.org/html/2505.14069v1"},{"title":"Which is Better for Agentic RAG Reinforcement Learning","url":"https://openreview.net/pdf?id=h3LlJ6Bh4S"},{"title":"Process vs. Outcome Reward: Which is Better for Agentic RAG Reinforcement Learning","url":"https://arxiv.org/pdf/2505.14069"},{"title":"Process vs. Outcome Reward: Which is Better for Agentic RAG Reinforcement Learning | OpenReview","url":"https://openreview.net/forum?id=h3LlJ6Bh4S"},{"title":"(PDF) Process vs. Outcome Reward: Which is Better for Agentic RAG Reinforcement Learning","url":"https://www.researchgate.net/publication/391910704_Process_vs_Outcome_Reward_Which_is_Better_for_Agentic_RAG_Reinforcement_Learning"},{"title":"Process vs. Outcome Reward: Which is Better for Agentic RAG","url":"https://neurips.cc/media/neurips-2025/Slides/116682.pdf"},{"title":"[2505.14069] Process vs. Outcome Reward: Which is Better for Agentic RAG Reinforcement Learning","url":"https://arxiv.org/abs/2505.14069"},{"title":"GitHub - Applied-Machine-Learning-Lab/ReasonRAG: Code implementation of NeurIPS'25 paper \"Process vs. Outcome Reward: Which is Better for Agentic RAG Reinforcement Learning\" · GitHub","url":"https://github.com/Applied-Machine-Learning-Lab/ReasonRAG"},{"title":"HiPRAG: Hierarchical Process Rewards for Efficient Agentic Retrieval Augmented Generation","url":"https://arxiv.org/pdf/2510.07794"}]

Based on the search results, here's what I found about ReasonRAG, RAG-ProGuide, and the NeurIPS 2025 review discussion:

## Overview

ReasonRAG is a novel method that leverages RAG-ProGUIDE—a high-quality dataset providing fine-grained, process-level rewards for query generation, evidence extraction, and answer generation. This work was presented as a NeurIPS 2025 poster.

## Problem and Solution

Agentic RAG systems like DeepResearch address dynamic retrieval and adaptive workflows, but recent methods like Search-R1, which rely on outcome-based reinforcement learning, face challenges such as low exploration efficiency, gradient conflict, and sparse reward signals.

By employing process-supervised reinforcement learning, ReasonRAG enhances LLMs' autonomous capabilities in search, query generation, evidence extraction, and answer synthesis.

## Key Dataset and Methodology

The framework employs Monte Carlo Tree Search (MCTS) algorithm to explore the decision space in agentic RAG and collect informative intermediate steps, with the resulting process-supervised dataset, RAG-ProGuide, then used to optimize ReasonRAG via policy preference optimization.

RAG-ProGuide comprises 5k queries with 13,000 high-quality process-level preference pairs.

## Performance Results

ReasonRAG, utilizing RAG-ProGUIDE, outperforms existing approaches like Search-R1 and traditional RAG systems, achieving superior performance on five benchmark datasets with only 5k training instances—significantly fewer than the 90k required by Search-R1.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "9ac23f1f-bd27-4da4-b111-7959dc8e2e9e",
  "isSidechain": true,
  "promptId": "bbbe4bf2-b0a9-43d5-8f54-a157f509f7eb",
  "agentId": "aa34d3135a3369818",
  "type": "user",
  "uuid": "d5743516-0c59-474c-a670-537fc66cf09a",
  "sourceToolAssistantUUID": "9ac23f1f-bd27-4da4-b111-7959dc8e2e9e",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "27d805b7-0ea1-4632-9635-35f016c03b5a",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 28 · 2026-05-30T06:30:10.195Z_

Let me try to get the GitHub repo for additional insights and the follow-up HiPRAG paper that cites this work.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d5743516-0c59-474c-a670-537fc66cf09a",
  "isSidechain": true,
  "agentId": "aa34d3135a3369818",
  "requestId": "req_011CbYHL4wsy4iubkvgBZAaF",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "5686e9e7-723e-40bc-a0b0-54f211a56ea6",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "27d805b7-0ea1-4632-9635-35f016c03b5a",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AAa8Bsszb74tH14JjHrYJk",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 792,
      "cache_creation_input_tokens": 1585,
      "cache_read_input_tokens": 18942,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1585,
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

_source line 29 · 2026-05-30T06:30:11.609Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01NT2BdCFi6jNHF3sFg3vh2E`</summary>

```json
{
  "url": "https://github.com/Applied-Machine-Learning-Lab/ReasonRAG",
  "prompt": "Extract all information from this GitHub repository: README content, code structure, any additional details about the method, dataset availability, usage instructions, and any issues or discussions."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5686e9e7-723e-40bc-a0b0-54f211a56ea6",
  "isSidechain": true,
  "agentId": "aa34d3135a3369818",
  "requestId": "req_011CbYHL4wsy4iubkvgBZAaF",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "c13b49bc-b88c-4c72-b241-0c07eaef7645",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "27d805b7-0ea1-4632-9635-35f016c03b5a",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AAa8Bsszb74tH14JjHrYJk",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 792,
      "cache_creation_input_tokens": 1585,
      "cache_read_input_tokens": 18942,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1585,
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

_source line 30 · 2026-05-30T06:30:13.493Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01C1jV1offeg6vHZaBjMVYpt`</summary>

```json
{
  "url": "https://neurips.cc/virtual/2025/poster/116682",
  "prompt": "Extract all information about this NeurIPS 2025 poster: presentation details, any reviewer scores or acceptance information, session details, and any available discussion or comments."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c13b49bc-b88c-4c72-b241-0c07eaef7645",
  "isSidechain": true,
  "agentId": "aa34d3135a3369818",
  "requestId": "req_011CbYHL4wsy4iubkvgBZAaF",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "fcd44991-a020-4f51-ae37-dfbf8d8c77e3",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "27d805b7-0ea1-4632-9635-35f016c03b5a",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AAa8Bsszb74tH14JjHrYJk",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 792,
      "cache_creation_input_tokens": 1585,
      "cache_read_input_tokens": 18942,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1585,
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

_source line 31 · 2026-05-30T06:30:13.830Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01UCzuCDt3oVV7iqQtmUaA7d`</summary>

```json
{
  "query": "\"ReasonRAG\" OR \"RAG-ProGuide\" criticism limitations analysis blog 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "fcd44991-a020-4f51-ae37-dfbf8d8c77e3",
  "isSidechain": true,
  "agentId": "aa34d3135a3369818",
  "requestId": "req_011CbYHL4wsy4iubkvgBZAaF",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "084c954c-5b88-479d-9bf3-3ddc59a19bf4",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "27d805b7-0ea1-4632-9635-35f016c03b5a",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AAa8Bsszb74tH14JjHrYJk",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 792,
      "cache_creation_input_tokens": 1585,
      "cache_read_input_tokens": 18942,
      "output_tokens": 307,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1585
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 792,
          "output_tokens": 307,
          "cache_read_input_tokens": 18942,
          "cache_creation_input_tokens": 1585,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1585,
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

_source line 32 · 2026-05-30T06:30:17.994Z_

<details><summary>↩ Tool result · `toolu_01NT2BdCFi6jNHF3sFg3vh2E`</summary>

```text
# ReasonRAG Repository Summary

## Overview
ReasonRAG is a GitHub project implementing a NeurIPS'25 paper on agentic RAG systems. The repository demonstrates "Process vs. Outcome Reward: Which is Better for Agentic RAG Reinforcement Learning."

## Core Methodology
The project uses three main components:

1. **Monte Carlo Tree Search (MCTS)** generates process-supervised rollouts capturing strategic preferences at a granular level
2. **Direct Preference Optimization (DPO)** refines these preferences within the RAG framework
3. **Agentic RAG Pipeline** enables autonomous query generation, evidence extraction, and answer formulation

## Key Assets
- **Dataset**: RAG_ProGuide available on Hugging Face, generated from PopQA, HotpotQA, and 2WikimultihopQA
- **Trained Models**: Qwen2.5-7B-Instruct-ReasonRAG and corresponding LoRA variants
- **Performance**: Achieves superior results using only 5,000 training instances compared to 90,000 required by competing approaches

## Technical Setup
- Built on FlashRAG framework
- Requires Python 3.10.16, vLLM (≥0.4.1), and DeepSpeed
- Training utilizes LLaMA Factory with DPO configuration
- Uses BGE embeddings for retrieval indexing

## Code Structure
- `data_generation.py` – Creates policy preference data
- `preference_data_generation.py` – Generates optimization data
- `inference.py` – Runs evaluations on benchmark datasets
- `training_config/` – Contains configuration files for model training

## Repository Statistics
- 36 commits, 14 stars, 1 fork
- 3 open issues, 0 pull requests
- 100% Python codebase under MIT license
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c13b49bc-b88c-4c72-b241-0c07eaef7645",
  "isSidechain": true,
  "promptId": "bbbe4bf2-b0a9-43d5-8f54-a157f509f7eb",
  "agentId": "aa34d3135a3369818",
  "type": "user",
  "uuid": "7ea0745e-dfde-4210-a270-d8ed7f42bbb3",
  "sourceToolAssistantUUID": "c13b49bc-b88c-4c72-b241-0c07eaef7645",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "27d805b7-0ea1-4632-9635-35f016c03b5a",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 33 · 2026-05-30T06:30:18.420Z_

<details><summary>↩ Tool result · `toolu_01C1jV1offeg6vHZaBjMVYpt`</summary>

```text
# NeurIPS 2025 Poster: Process vs. Outcome Reward for Agentic RAG

## Presentation Details
**Title:** "Process vs. Outcome Reward: Which is Better for Agentic RAG Reinforcement Learning"

**Schedule:** Thursday, December 4, 2025 • 11:00 AM – 2:00 PM PST

**Location:** San Diego

**Poster ID:** 119662

## Authors
Wenlin Zhang, Xiangyang Li, Kuicai Dong, Yichao Wang, Pengyue Jia, Xiaopeng Li, Yingyi Zhang, Derong Xu, Zhaocheng Du, Huifeng Guo, Ruiming Tang, and Xiangyu Zhao

## Research Overview
The paper introduces ReasonRAG, addressing limitations in agentic retrieval-augmented generation systems. The researchers contend that "process-supervised reinforcement learning" outperforms outcome-based approaches, requiring only 5,000 training instances versus 90,000 for competing methods.

## Available Resources
- Project repository with implementation code
- PDF slides and poster graphics
- OpenReview forum for discussion
- Evaluation across five benchmark datasets

## Key Finding
ReasonRAG leverages "fine-grained, process-level rewards for query generation, evidence extraction, and answer generation," demonstrating superior performance compared to traditional RAG and Search-R1 systems.

**Note:** No reviewer scores or acceptance comments were included in the provided content.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "fcd44991-a020-4f51-ae37-dfbf8d8c77e3",
  "isSidechain": true,
  "promptId": "bbbe4bf2-b0a9-43d5-8f54-a157f509f7eb",
  "agentId": "aa34d3135a3369818",
  "type": "user",
  "uuid": "bdc91168-029e-4870-87de-561605c2f21e",
  "sourceToolAssistantUUID": "fcd44991-a020-4f51-ae37-dfbf8d8c77e3",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "27d805b7-0ea1-4632-9635-35f016c03b5a",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 34 · 2026-05-30T06:30:21.703Z_

<details><summary>↩ Tool result · `toolu_01UCzuCDt3oVV7iqQtmUaA7d`</summary>

```text
Web search results for query: ""ReasonRAG" OR "RAG-ProGuide" criticism limitations analysis blog 2025 2026"

Links: [{"title":"RAG Limitations: 7 Critical Challenges You Need to Know in 2026","url":"https://www.stackai.com/blog/rag-limitations"},{"title":"Retrieval is Not Enough: Enhancing RAG Reasoning through Test-Time Critique and Optimization","url":"https://arxiv.org/pdf/2504.14858"},{"title":"Eliciting Critical Reasoning in Retrieval-Augmented Language Models via Contrastive Explanations","url":"https://arxiv.org/pdf/2410.22874"},{"title":"RAG Evaluation Metrics 2026 - KOIRO Dev Blog","url":"https://blog.koiro.me/en/2026/04/30/rag-evaluation-metrics-2026/"},{"title":"EmoRAG: Evaluating RAG Robustness to Symbolic Perturbations","url":"https://arxiv.org/pdf/2512.01335"},{"title":"How Much Can RAG Help the Reasoning of LLM?","url":"https://arxiv.org/pdf/2410.02338"},{"title":"Synergizing RAG and Reasoning: A Systematic Review","url":"https://arxiv.org/pdf/2504.15909"},{"title":"The State of RAG 2026: From \"Vibe Checking\" to Reasoning | AIGuys","url":"https://medium.com/aiguys/the-state-of-rag-2026-from-vibe-checking-to-reasoning-cee536ae3f02"},{"title":"GitHub - DavidZWZ/Awesome-RAG-Reasoning: [EMNLP 2025] Awesome RAG Reasoning Resources · GitHub","url":"https://github.com/DavidZWZ/Awesome-RAG-Reasoning"}]

I found several relevant results related to RAG criticism, limitations, and analysis from 2025-2026, though the search didn't turn up specific results for "ReasonRAG" or "RAG-ProGuide" by those exact names. Here's what I found:

## RAG Limitations and Criticism (2025-2026)

**Key Limitations Identified:**

Contemporary studies have identified limitations emerging from noisy retrieval, where irrelevant or contradictory passages can introduce biases, stemming from RAG's inability to systematically and critically assess retrieved passages.

RAG systems can remain "pragmatically misleading" even when citing accurate sources without hallucination—by decontextualizing facts, omitting critical sources, or reinforcing patient misunderstandings.

Current RAG systems have a critical robustness vulnerability where adversaries could manipulate them, and standard defenses have been found insufficient.

**Reasoning and RAG Synergy:**

The impact of RAG on enhancing reasoning capacity has yet to be thoroughly investigated, though recent work identifies "Reasoning Misalignment"—the divergence between an LLM's internal reasoning trajectory and the evidential constraints provided by retrieval.

Current limitations in RAG assessment include the absence of intermediate supervision for multi-step reasoning and practical challenges related to cost-risk trade-offs.

The search results don't contain specific critiques of products named "ReasonRAG" or "RAG-ProGuide," but they do document substantial ongoing debate about RAG system limitations in 2025-2026.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "084c954c-5b88-479d-9bf3-3ddc59a19bf4",
  "isSidechain": true,
  "promptId": "bbbe4bf2-b0a9-43d5-8f54-a157f509f7eb",
  "agentId": "aa34d3135a3369818",
  "type": "user",
  "uuid": "9623d152-81ae-4c2b-ba17-2a0c8a62e1ce",
  "sourceToolAssistantUUID": "084c954c-5b88-479d-9bf3-3ddc59a19bf4",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "27d805b7-0ea1-4632-9635-35f016c03b5a",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 35 · 2026-05-30T06:30:28.450Z_

Let me also look at the follow-up papers that reference this work and search for the NeurIPS slides.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9623d152-81ae-4c2b-ba17-2a0c8a62e1ce",
  "isSidechain": true,
  "agentId": "aa34d3135a3369818",
  "requestId": "req_011CbYHM76Pak4XTDitQEVUr",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "9ddaea48-0288-42ee-a30c-3ad48fe69f33",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "27d805b7-0ea1-4632-9635-35f016c03b5a",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011orBLosoCGmRwYtJ7wos8f",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2803,
      "cache_read_input_tokens": 20527,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2803,
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

_source line 36 · 2026-05-30T06:30:30.298Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01HwM8qnDMH9ASDK3h1uoRYS`</summary>

```json
{
  "url": "https://arxiv.org/abs/2510.07794",
  "prompt": "Extract the full abstract and key details of HiPRAG - how does it relate to and build upon ReasonRAG? What criticisms or improvements does it propose over ReasonRAG?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9ddaea48-0288-42ee-a30c-3ad48fe69f33",
  "isSidechain": true,
  "agentId": "aa34d3135a3369818",
  "requestId": "req_011CbYHM76Pak4XTDitQEVUr",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "6b886eee-0cc2-4515-a384-e5f54477ac08",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "27d805b7-0ea1-4632-9635-35f016c03b5a",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011orBLosoCGmRwYtJ7wos8f",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2803,
      "cache_read_input_tokens": 20527,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2803,
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

_source line 37 · 2026-05-30T06:30:31.659Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01WVoruUHtLCwGFAfyPUXYrP`</summary>

```json
{
  "url": "https://arxiv.org/abs/2602.22576",
  "prompt": "Extract the full abstract and key details of Search-P1. How does it relate to ReasonRAG? What criticisms or improvements over ReasonRAG does it propose? Extract all relevant comparisons."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6b886eee-0cc2-4515-a384-e5f54477ac08",
  "isSidechain": true,
  "agentId": "aa34d3135a3369818",
  "requestId": "req_011CbYHM76Pak4XTDitQEVUr",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "aaec0c71-2d53-4582-97ef-bf8c1a6e7150",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "27d805b7-0ea1-4632-9635-35f016c03b5a",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011orBLosoCGmRwYtJ7wos8f",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2803,
      "cache_read_input_tokens": 20527,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2803,
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

_source line 38 · 2026-05-30T06:30:32.145Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Xsss5iTzzde9HFxVUySiyn`</summary>

```json
{
  "query": "Search-R1 vs ReasonRAG process reward outcome reward RAG comparison critique 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "aaec0c71-2d53-4582-97ef-bf8c1a6e7150",
  "isSidechain": true,
  "agentId": "aa34d3135a3369818",
  "requestId": "req_011CbYHM76Pak4XTDitQEVUr",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "dde1b509-cbf4-4519-a81a-19deaf0149a0",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "27d805b7-0ea1-4632-9635-35f016c03b5a",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011orBLosoCGmRwYtJ7wos8f",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2803,
      "cache_read_input_tokens": 20527,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2803,
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

_source line 39 · 2026-05-30T06:30:35.908Z_

<details><summary>↩ Tool result · `toolu_01HwM8qnDMH9ASDK3h1uoRYS`</summary>

```text
# HiPRAG: Summary and Key Details

## Full Abstract

The paper introduces HiPRAG, a training methodology addressing inefficiencies in agentic RAG systems. The core issue involves problematic search behaviors—specifically over-searching (retrieving already-known information) and under-searching (failing to search when needed). Rather than relying solely on outcome-based rewards, HiPRAG implements "a fine-grained, knowledge-grounded process reward into the RL training" by decomposing reasoning trajectories into discrete steps and applying hierarchical reward functions.

Results demonstrate strong performance: "average accuracies of 65.4% (3B) and 67.2% (7B)" while substantially reducing over-search rates to 2.3% and concurrently lowering under-search rates.

## Regarding ReasonRAG

**The provided content does not mention ReasonRAG.** The abstract and arXiv page excerpt provided contain no references to, comparisons with, or discussions of ReasonRAG, making it impossible to determine how HiPRAG relates to or builds upon that work based on this source material alone.

To answer your question about the relationship between these methods and specific criticisms HiPRAG proposes, you would need access to the full paper text or a source that explicitly discusses both systems.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "6b886eee-0cc2-4515-a384-e5f54477ac08",
  "isSidechain": true,
  "promptId": "bbbe4bf2-b0a9-43d5-8f54-a157f509f7eb",
  "agentId": "aa34d3135a3369818",
  "type": "user",
  "uuid": "3fe7200e-bdd3-4638-8092-8ddb73c19b40",
  "sourceToolAssistantUUID": "6b886eee-0cc2-4515-a384-e5f54477ac08",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "27d805b7-0ea1-4632-9635-35f016c03b5a",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 40 · 2026-05-30T06:30:37.389Z_

<details><summary>↩ Tool result · `toolu_01WVoruUHtLCwGFAfyPUXYrP`</summary>

```text
# Search-P1: Abstract and Key Details

## Full Abstract

"Retrieval-Augmented Generation (RAG) enhances large language models (LLMs) by incorporating external knowledge, yet traditional single-round retrieval struggles with complex multi-step reasoning. Agentic RAG addresses this by enabling LLMs to dynamically decide when and what to retrieve, but current RL-based training methods suffer from sparse outcome rewards that discard intermediate signals and low sample efficiency where failed samples contribute nothing. We propose Search-P1, a framework that introduces path-centric reward shaping for agentic RAG training, comprising two key components: (1) Path-Centric Reward, which evaluates the structural quality of reasoning trajectories through order-agnostic step coverage and soft scoring that extracts learning signals even from failed samples, and (2) Dual-Track Path Scoring with offline-generated reference planners that assesses paths from both self-consistency and reference-alignment perspectives."

## Key Results

The paper reports "an average accuracy gain of 7.7 points" when compared to existing baselines.

## ReasonRAG Comparison

**Note:** The provided webpage content does not mention "ReasonRAG" or contain any direct comparisons to that specific approach. The paper references "Search-R1" as a baseline for comparison but provides no detailed discussion of ReasonRAG relationships or criticisms in the abstract or accessible content shown.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "aaec0c71-2d53-4582-97ef-bf8c1a6e7150",
  "isSidechain": true,
  "promptId": "bbbe4bf2-b0a9-43d5-8f54-a157f509f7eb",
  "agentId": "aa34d3135a3369818",
  "type": "user",
  "uuid": "8a46d664-a47c-42ef-a7b6-a247e8a1375e",
  "sourceToolAssistantUUID": "aaec0c71-2d53-4582-97ef-bf8c1a6e7150",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "27d805b7-0ea1-4632-9635-35f016c03b5a",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 41 · 2026-05-30T06:30:38.990Z_

<details><summary>↩ Tool result · `toolu_01Xsss5iTzzde9HFxVUySiyn`</summary>

```text
Web search results for query: "Search-R1 vs ReasonRAG process reward outcome reward RAG comparison critique 2025"

Links: [{"title":"Process vs. Outcome Reward: Which is Better for Agentic RAG Reinforcement Learning | alphaXiv","url":"https://www.alphaxiv.org/overview/2505.14069v2"},{"title":"[2505.14069] Process vs. Outcome Reward: Which is Better for Agentic RAG Reinforcement Learning","url":"https://arxiv.org/abs/2505.14069"},{"title":"arXiv:2505.14069v2 [cs.IR] 22 May 2025","url":"https://arxiv.org/pdf/2505.14069v2"},{"title":"Process vs. Outcome Reward: Which is Better for Agentic RAG Reinforcement Learning","url":"https://arxiv.org/html/2505.14069"},{"title":"Process vs. Outcome Reward: Which is Better for Agentic RAG Reinforcement Learning | OpenReview","url":"https://openreview.net/forum?id=h3LlJ6Bh4S"},{"title":"[Literature Review] Process vs. Outcome Reward: Which is Better for Agentic RAG Reinforcement Learning","url":"https://www.themoonlight.io/en/review/process-vs-outcome-reward-which-is-better-for-agentic-rag-reinforcement-learning"},{"title":"Process vs. Outcome Reward: Which is Better for Agentic RAG","url":"https://neurips.cc/media/neurips-2025/Slides/116682.pdf"},{"title":"Process vs. Outcome Reward: Which is Better for","url":"https://openreview.net/pdf?id=h3LlJ6Bh4S"},{"title":"Process vs. Outcome Reward: Which is Better for Agentic RAG Reinforcement Learning","url":"https://arxiv.org/pdf/2505.14069"},{"title":"NeurIPS Poster Process vs. Outcome Reward: Which is Better for Agentic RAG Reinforcement Learning","url":"https://neurips.cc/virtual/2025/poster/116682"}]

Based on the search results, here's a comprehensive overview of the Search-R1 vs ReasonRAG comparison:

## Key Approaches

Search-R1 uses outcome-based reinforcement learning, where the correctness of the final answer serves as the reward signal. In contrast, ReasonRAG introduces a method that automatically constructs RAG-ProGuide, a high-quality dataset providing process-level rewards for (i) query generation, (ii) evidence extraction, and (iii) answer generation, thereby enhancing model inherent capabilities via process-supervised reinforcement learning.

## Critical Limitations of Outcome-Supervised RL

Outcome-supervised agentic RAG methods face challenges including low exploration efficiency, gradient conflict, and sparse reward signals.

## Performance Comparison

The experimental results show significant efficiency gains for ReasonRAG:

- ReasonRAG (trained on 5k queries) outperforms Search-R1 (trained on 90k queries) in average EM (34.4% vs 32.8%) and F1 (42.3% vs 40.7%) scores.

- On the HotpotQA dataset, ReasonRAG achieves an F1 score of 48.9%, outperforming Search-R1 (47.0% F1), both of which are trained on larger datasets.

- Extensive experiments on five benchmark RAG datasets show ReasonRAG (trained with only 13k process-level steps) outperforms Search-R1 (trained on 90k queries with approximately 270k intermediate steps), suggesting the superiority of process-supervised RL over outcome-supervised RL.

## Training Efficiency

ReasonRAG converges faster and achieves higher performance with fewer GPU hours compared to Search-R1, particularly on complex multi-hop tasks.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "dde1b509-cbf4-4519-a81a-19deaf0149a0",
  "isSidechain": true,
  "promptId": "bbbe4bf2-b0a9-43d5-8f54-a157f509f7eb",
  "agentId": "aa34d3135a3369818",
  "type": "user",
  "uuid": "7a5edda9-66da-43f3-a6ec-d53f4e2ebe8e",
  "sourceToolAssistantUUID": "dde1b509-cbf4-4519-a81a-19deaf0149a0",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "27d805b7-0ea1-4632-9635-35f016c03b5a",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 42 · 2026-05-30T06:30:41.377Z_

Let me get the Moonlight review and the NeurIPS slides for additional analysis.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7a5edda9-66da-43f3-a6ec-d53f4e2ebe8e",
  "isSidechain": true,
  "agentId": "aa34d3135a3369818",
  "requestId": "req_011CbYHNNvRRQXB4HZsCQ78M",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "58c8fcb2-78cd-4831-b066-c32694f9b362",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "27d805b7-0ea1-4632-9635-35f016c03b5a",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EbunWT5HebvHCLGqvGQ9Qw",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2068,
      "cache_read_input_tokens": 23330,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2068,
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

_source line 43 · 2026-05-30T06:30:43.265Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_011oYRSZW1z9huwmaG7BivEa`</summary>

```json
{
  "url": "https://www.themoonlight.io/en/review/process-vs-outcome-reward-which-is-better-for-agentic-rag-reinforcement-learning",
  "prompt": "Extract the COMPLETE literature review and analysis of this paper. Include all critiques, strengths, weaknesses, and any detailed technical analysis. Return everything available."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "58c8fcb2-78cd-4831-b066-c32694f9b362",
  "isSidechain": true,
  "agentId": "aa34d3135a3369818",
  "requestId": "req_011CbYHNNvRRQXB4HZsCQ78M",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "79ef9c8a-dd44-4db3-b8f2-a60d1eb648a6",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "27d805b7-0ea1-4632-9635-35f016c03b5a",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EbunWT5HebvHCLGqvGQ9Qw",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2068,
      "cache_read_input_tokens": 23330,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2068,
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

_source line 44 · 2026-05-30T06:30:44.427Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01XeBt4LPeavDgc9K22hUjvb`</summary>

```json
{
  "url": "https://neurips.cc/media/neurips-2025/Slides/116682.pdf",
  "prompt": "Extract all content from these NeurIPS presentation slides. Include all key points, figures described, claims made, and any additional details not in the paper."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "79ef9c8a-dd44-4db3-b8f2-a60d1eb648a6",
  "isSidechain": true,
  "agentId": "aa34d3135a3369818",
  "requestId": "req_011CbYHNNvRRQXB4HZsCQ78M",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "eaf6f7c8-8693-4d66-8824-200e8bf3175f",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "27d805b7-0ea1-4632-9635-35f016c03b5a",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EbunWT5HebvHCLGqvGQ9Qw",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2068,
      "cache_read_input_tokens": 23330,
      "output_tokens": 265,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2068
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 265,
          "cache_read_input_tokens": 23330,
          "cache_creation_input_tokens": 2068,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2068,
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

_source line 45 · 2026-05-30T06:30:48.619Z_

<details><summary>↩ Tool result · `toolu_011oYRSZW1z9huwmaG7BivEa`</summary>

```text
# Literature Review: Process vs. Outcome Reward in Agentic RAG Reinforcement Learning

## Paper Overview
This work introduces ReasonRAG, contrasting process-supervised RL with outcome-supervised approaches for retrieval-augmented generation systems.

## Key Strengths

**Data Efficiency**: The framework achieves superior results with significantly less training data. ReasonRAG trained on 5k queries "outperforms Search-R1 (trained on 90k queries)" with better EM and F1 scores, demonstrating marked efficiency gains.

**Technical Innovation**: The dual-component methodology combining Shortest Path Reward Estimation and Monte Carlo Tree Search provides "fine-grained, process-level rewards during the RAG reasoning process," enabling more nuanced supervision than outcome-only approaches.

**Comprehensive Evaluation**: Testing across five benchmark datasets (PopQA, HotpotQA, 2WikiMultihopQA, Bamboogle, MuSiQue) with generalization analysis strengthens claims about robustness and real-world applicability.

**Training Efficiency**: Convergence analysis shows ReasonRAG "converges faster and achieves higher performance with fewer GPU hours compared to Search-R1," particularly benefiting complex multi-hop tasks.

## Identified Weaknesses

**Computational Cost**: The framework requires "higher time cost for process-level data rollout compared to outcome supervision," though authors argue quality offsets this burden—a trade-off requiring careful consideration.

**Limited Scale**: Testing uses Qwen2.5-7B-Instruct; scalability to larger models remains undemonstrated.

**Safety Concerns**: Documented "potential risks of generating harmful content if external knowledge sources are not curated," highlighting deployment challenges.

## Technical Analysis

The SPRE algorithm employs Monte Carlo estimation with length penalties, while MCTS efficiently explores decision spaces through structured state representation incorporating reasoning stage information.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "79ef9c8a-dd44-4db3-b8f2-a60d1eb648a6",
  "isSidechain": true,
  "promptId": "bbbe4bf2-b0a9-43d5-8f54-a157f509f7eb",
  "agentId": "aa34d3135a3369818",
  "type": "user",
  "uuid": "9809edc5-ac9d-4c3c-869c-3b2d2b677ce7",
  "sourceToolAssistantUUID": "79ef9c8a-dd44-4db3-b8f2-a60d1eb648a6",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "27d805b7-0ea1-4632-9635-35f016c03b5a",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 46 · 2026-05-30T06:30:53.216Z_

<details><summary>↩ Tool result · `toolu_01XeBt4LPeavDgc9K22hUjvb`</summary>

```text
I appreciate you sharing this content, but I need to let you know that what you've provided appears to be a PDF file encoded in binary format (the raw PDF stream data), not readable presentation slides or text content.

The file structure shows this is a PDF document with:
- Language setting: Chinese (zh)
- Multiple embedded images and fonts
- Compressed content streams that require PDF rendering to display

**I cannot extract meaningful content from this raw binary PDF data** because:

1. The actual slide text and images are compressed and encoded within the PDF structure
2. Without rendering the PDF properly, I can only see technical metadata, not the presentation content itself

**To help you extract content from these NeurIPS slides, I'd recommend:**

- Converting the PDF to readable text format using a PDF-to-text tool (like pdftotext)
- Providing screenshots or exported images from the slides
- Sharing the original PowerPoint/Keynote file if available
- Uploading the PDF to a document processing service that can extract text

If you can provide the slide content in a text-readable format, I'd be happy to summarize the key points, figures, and claims while following the content guidelines you've outlined.

[Binary content (application/pdf, 1.1MB) also saved to /home/ubuntu/.claude-account-2/projects/-home-ubuntu-idea-adversarial/27d805b7-0ea1-4632-9635-35f016c03b5a/tool-results/webfetch-1780122645678-1g9ays.pdf]
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "eaf6f7c8-8693-4d66-8824-200e8bf3175f",
  "isSidechain": true,
  "promptId": "bbbe4bf2-b0a9-43d5-8f54-a157f509f7eb",
  "agentId": "aa34d3135a3369818",
  "type": "user",
  "uuid": "f16dd2ee-a7b4-49e1-b5c0-00feeabe389c",
  "sourceToolAssistantUUID": "eaf6f7c8-8693-4d66-8824-200e8bf3175f",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "27d805b7-0ea1-4632-9635-35f016c03b5a",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 47 · 2026-05-30T06:32:31.726Z_

Now I have comprehensive information. Let me compile the complete structured research summary.

---

# Research Deep-Dive: "Process vs. Outcome Reward: Which is Better for Agentic RAG Reinforcement Learning"

**Paper:** ReasonRAG / RAG-ProGuide
**Authors:** Wenlin Zhang, Xiangyang Li, Kuicai Dong, Yichao Wang, Pengyue Jia, Xiaopeng Li, Yingyi Zhang, Derong Xu, Zhaocheng Du, Huifeng Guo, Ruiming Tang, Xiangyu Zhao
**Affiliations:** City University of Hong Kong, Noah's Ark Lab (Huawei)
**Venue:** NeurIPS 2025 (Poster), presented December 4, 2025, San Diego
**arXiv:** 2505.14069 (v1: May 20, 2025; v3: December 8, 2025)
**Code:** https://github.com/Applied-Machine-Learning-Lab/ReasonRAG (MIT license)
**Dataset:** RAG-ProGuide on HuggingFace

---

## 1. Gap Identified and HOW They Identified It

**The gap:** Prior agentic RAG systems (notably Search-R1) used **outcome-supervised RL** where only the final answer correctness provides the reward signal. Nobody had systematically applied **process-supervised RL** to agentic RAG.

**How they identified it:** They analyzed three specific failure modes of outcome-supervised RL in the RAG setting:

1. **Low exploration efficiency** -- the model must generate an entire reasoning chain (query, retrieve, extract, answer -- potentially multi-hop) before receiving ANY reward signal. This makes the search space enormous and learning slow.
2. **Gradient conflict** -- when a mistake occurs late in the reasoning chain, the entire sequence (including correct early steps like good query formulation) gets penalized equally. Correct intermediate actions are punished alongside incorrect ones.
3. **Sparse rewards** -- outcome supervision only provides feedback at the terminal state (final answer), creating a credit assignment problem across the multi-step RAG pipeline.

They positioned this against the broader RL literature where process reward models (PRMs) had shown success in math reasoning (e.g., in the PRM800K / Let's Verify Step by Step line of work) but had NOT been applied to the retrieval-augmented generation setting.

---

## 2. Key Insight Others Missed

The central insight: **the RAG pipeline has natural decomposition points where process-level rewards can be meaningfully defined** -- specifically at three stages: (i) query generation quality, (ii) evidence extraction quality, and (iii) answer generation quality. Unlike math reasoning where step verification is more ambiguous, RAG has observable intermediate artifacts (the query sent to the retriever, the evidence spans selected from documents, the final answer) that can each be evaluated.

The second insight: **you can use MCTS + a Shortest Path Reward Estimation (SPRE) to automatically construct process-level preference data** without expensive human annotation. The SPRE formulation specifically encourages the shortest correct path via an exponential decay factor alpha^{steps}, encoding the bias that fewer retrieval rounds are preferable when they lead to correct answers. This is domain-specific to RAG and wouldn't apply straightforwardly to other reasoning tasks.

---

## 3. Problem Formulation -- How It Differs

They formulate agentic RAG as a **three-stage state machine** with explicit states:
- **Reasoning stage:** The model decides whether to generate a search query or produce a final answer
- **Grounding stage:** Given retrieved documents, the model extracts evidence spans
- **Terminal stage:** The model has produced an answer; episode ends

This is formalized as a state `s = (x, y_{&lt;i}, stage)` where stage in {Reasoning, Grounding, Terminal}. The policy is:

```
pi(a|s) = LLM(a|x, y_{&lt;i}, p_stage)  [Reasoning]
pi(a|s) = LLM(a|x, y_{&lt;i}, docs, p_stage)  [Grounding]
```

This differs from Search-R1 which treats the entire generation as a single monolithic RL problem with a binary reward at the end. ReasonRAG's formulation enables reward assignment at each state transition.

---

## 4. Existing Techniques Adapted/Combined/Simplified

ReasonRAG combines several existing techniques in a novel way:

1. **Monte Carlo Tree Search (MCTS)** -- adapted from AlphaGo/AlphaZero and recent LLM reasoning work. Used here specifically to explore the RAG decision space (query vs. answer, which evidence to extract) rather than math/code reasoning.

2. **Shortest Path Reward Estimation (SPRE)** -- a novel reward formulation:
   ```
   Q_t = (1/k) * sum_{i=1}^{k} v(rollout_i) * alpha^{step(rollout_i)}
   ```
   This adapts Monte Carlo value estimation with a **step-decay penalty** (alpha in (0,1]) that specifically rewards shorter correct trajectories. This is their novel contribution -- encoding the RAG-specific prior that fewer retrieval iterations are better.

3. **Direct Preference Optimization (DPO)** -- used instead of PPO/GRPO for the actual policy optimization. The preference pairs come from the MCTS exploration, comparing high-reward vs. low-reward actions at each intermediate step:
   ```
   L(theta) = -E[log sigma(beta * log(p_theta(y_w|x,y_{&lt;t}) / p_theta(y_l|x,y_{&lt;t})))]
   ```

4. **UCB-based tree exploration** -- standard UCB formula for node selection in MCTS:
   ```
   s* = argmax [Q(s_i) + c_uct * sqrt(sum N(s_i)) / (1+N(s_i))]
   ```

The combination is: MCTS explores the RAG decision tree -> SPRE evaluates nodes with shortest-path bias -> preference pairs are extracted -> DPO trains the LLM. This is a pipeline combination rather than a single algorithmic innovation.

---

## 5. Technical Method Details

### RAG-ProGuide Dataset Construction

- **Source questions:** 3,000 each from PopQA, HotpotQA, 2WikiMultiHopQA
- **After processing:** 4,603 questions total
- **MCTS exploration:** For each question, MCTS explores multiple trajectories through the RAG state machine
- **Reward computation:** F1 score between predicted and ground-truth answers, propagated through tree via SPRE
- **Preference pair extraction:** At each tree node, children with higher SPRE scores become "preferred" and lower become "dispreferred"
- **Filtering:** Pairs with identical responses or reward difference < 0.01 are removed

**Final dataset statistics:**
- 4,603 questions
- 13,289 preference pairs total
- Action type distribution: Query Generation 24.8%, Evidence Extraction 32.4%, Answer Generation 42.8%
- Retrieval iterations: 1-5 (median 3, avg 2.7)
- Token length per action: 9-625 (median 60, avg 65.5)

### Training

- **Base model:** Qwen2.5-7B-Instruct
- **Method:** DPO using LLaMA Factory
- **Retriever:** BGE (bge-base-en-v1.5) -- STATIC, not trained
- **Knowledge source:** Wikidump 2018 + dataset-specific corpora
- **Retrieval:** Top-3 documents per query

### Inference (Algorithm 1)

Structured loop with explicit tags: `&lt;query>`, `&lt;evidence>`, `&lt;answer>` control state transitions. The model autonomously decides when to search vs. when to answer, what query to formulate, which evidence to extract, all via the trained policy.

---

## 6. Key Quantitative Results

### Main results (5 benchmarks, Avg EM / Avg F1):

| Method | Training Data | Avg EM | Avg F1 |
|--------|--------------|--------|--------|
| Naive Generation | 0 | 11.5 | 19.4 |
| Standard RAG | 0 | 24.3 | 32.0 |
| Search-R1 | 90k | 32.8 | 40.7 |
| AutoRAG | 10k | 29.5 | 36.9 |
| **ReasonRAG** | **5k** | **34.4** | **42.3** |

### Data efficiency claim (the "18x" number):

ReasonRAG uses 5k training instances vs. Search-R1's 90k = **18x fewer training instances** while achieving **+1.6 points higher Avg EM** and **+1.6 points higher Avg F1**.

More precisely: ReasonRAG has 13k process-level preference pairs from 5k questions. Search-R1 has ~270k intermediate steps from 90k questions. So in terms of step-level data, ReasonRAG uses ~20x less.

### Per-dataset highlights:
- **PopQA** (single-hop): 41.5 EM / 46.2 F1 vs. Search-R1's 39.7/44.8
- **HotpotQA** (multi-hop): 38.4 EM / 48.9 F1 vs. Search-R1's 37.0/47.0
- **2WikiMultiHopQA** (multi-hop): 43.6 EM / 50.4 F1 vs. Search-R1's 41.4/48.0
- **Bamboogle** (out-of-domain): 36.0 EM / 45.5 F1 vs. Search-R1's 32.0/43.8
- **MuSiQue** (out-of-domain): 12.8 EM / 20.6 F1 vs. Search-R1's 14.6/19.9

Note: ReasonRAG loses to Search-R1 on MuSiQue EM (12.8 vs 14.6) but wins on F1 (20.6 vs 19.9).

### Ablation (optimization strategy, Table 3):
- Base model: 22.0 Avg EM / 32.8 Avg F1
- SFT on process data: 23.9 / 32.0 (overfits on multi-hop, hurts single-hop)
- RL-ORL with 5k data (outcome reward): 21.3 / 28.9 (WORSE than base -- outcome reward with small data fails)
- RL-ORL with 10k data: 32.0 / 39.9 (competitive but still below)
- **RL-PRL (ReasonRAG):** 34.5 / 42.3

This ablation is the strongest evidence: with the SAME 5k data, outcome RL completely fails (21.3 EM) while process RL succeeds (34.5 EM). Outcome RL needs 10k+ data to even approach process RL's results.

### Training efficiency:
ReasonRAG converges faster in GPU hours than Search-R1, especially on multi-hop tasks.

---

## 7. Limitations

**Explicitly stated by the authors (Appendix H):**
1. **Higher per-sample annotation cost:** Process-level data rollout via MCTS is more time-consuming per sample than outcome-level data collection (though fewer samples are needed overall).
2. **Safety concerns:** Potential risk of generating harmful content if external knowledge sources are not properly curated.

**Implicit/unstated limitations I identify:**
3. **Only tested at 7B scale** -- scalability to larger models (70B+) is undemonstrated.
4. **Static retriever** -- the retriever (BGE) is never trained. The system only improves the LLM's ability to USE retrieval, not the retrieval quality itself.
5. **Wikipedia-only knowledge base** -- Wikidump 2018 is the knowledge source; performance on domain-specific or more current corpora is unknown.
6. **Closed-book QA benchmarks only** -- all five benchmarks are factoid QA. No evaluation on long-form generation, summarization, or open-ended tasks.
7. **DPO rather than online RL** -- they use offline preference optimization (DPO) rather than online RL (PPO/GRPO). This means the policy cannot improve beyond the quality of the MCTS-generated preference data.
8. **MCTS requires a capable base model** -- the MCTS exploration uses the base Qwen2.5-7B model to generate rollouts. If the base model is weak, the exploration quality will be poor, creating a bootstrapping problem.
9. **The "18x" claim is about instance count, not compute** -- MCTS data generation is expensive. The total compute (data generation + training) comparison is not clearly presented.
10. **MuSiQue underperformance** -- ReasonRAG loses to Search-R1 on MuSiQue EM, suggesting the process reward may not generalize equally well to all multi-hop reasoning patterns.

---

## 8. CRITICAL DISTINCTION: What Gets Trained?

**ReasonRAG trains ONLY the LLM (Qwen2.5-7B-Instruct). The retriever is NOT trained.**

Evidence:
- The retriever is BGE (bge-base-en-v1.5), used as a static component across ALL methods
- The DPO objective (Equation 3) optimizes p_theta -- the LLM's parameters
- Algorithm 1 shows the retriever R is called as a black-box: `docs <- R(q)`
- No gradient flows through the retriever at any point
- The LLM is trained to: (a) decide WHEN to retrieve, (b) formulate WHAT query to send, (c) extract WHICH evidence from retrieved docs, and (d) generate the final answer

**This is a critical distinction for your research:** The retriever remains frozen. All improvements come from teaching the LLM to be a better "user" of the retriever -- better query formulation, better evidence selection, better answer synthesis. The retrieval quality itself is unchanged.

---

## 9. Related/Follow-up Work

Two notable follow-ups that address similar themes:

- **HiPRAG** (arXiv 2510.07794): Also uses process rewards for agentic RAG but with a "hierarchical" reward structure. Focuses on over-search and under-search behaviors. Reports 65.4% (3B) and 67.2% (7B) average accuracy.

- **Search-P1** (arXiv 2602.22576): Introduces "path-centric reward shaping" -- evaluates structural quality of reasoning trajectories via order-agnostic step coverage and dual-track scoring. Claims +7.7 average accuracy gain. Takes a different approach to intermediate rewards than ReasonRAG.

---

## 10. Assessment for Your Research

**Strengths relevant to your work:**
- Clean demonstration that process rewards >> outcome rewards for RAG (the 5k vs. 90k comparison is compelling)
- The three-stage decomposition (query/evidence/answer) is a natural and reusable framework
- MCTS for automatic preference data construction avoids human annotation costs
- The SPRE shortest-path bias is a simple but effective inductive bias for RAG

**Weaknesses to be aware of:**
- The absolute performance improvements over Search-R1 are modest (+1.6 EM/F1 on average)
- The "18x data efficiency" headline obscures that MCTS data generation is computationally expensive
- DPO is a one-shot offline method -- no iterative online improvement
- Retriever is frozen -- a joint LLM+retriever training approach could potentially do better
- Only factoid QA benchmarks; unclear how this transfers to more complex RAG tasks

Sources:
- [arXiv Paper](https://arxiv.org/abs/2505.14069)
- [OpenReview](https://openreview.net/forum?id=h3LlJ6Bh4S)
- [NeurIPS 2025 Poster](https://neurips.cc/virtual/2025/poster/116682)
- [GitHub Repository](https://github.com/Applied-Machine-Learning-Lab/ReasonRAG)
- [Moonlight Literature Review](https://www.themoonlight.io/en/review/process-vs-outcome-reward-which-is-better-for-agentic-rag-reinforcement-learning)
- [HiPRAG (follow-up)](https://arxiv.org/abs/2510.07794)
- [Search-P1 (follow-up)](https://arxiv.org/abs/2602.22576)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f16dd2ee-a7b4-49e1-b5c0-00feeabe389c",
  "isSidechain": true,
  "agentId": "aa34d3135a3369818",
  "requestId": "req_011CbYHPRnbKLnzQJfthBfns",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "ced3c47c-86a4-47a9-b664-646fdf7a246e",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "27d805b7-0ea1-4632-9635-35f016c03b5a",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CcHGK1VawTu9SrqWkKoDEa",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1101,
      "cache_read_input_tokens": 25398,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1101,
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
