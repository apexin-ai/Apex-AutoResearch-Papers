# Research conversation: You are a senior ML researcher. Research the paper "Steering Knowledge Selection Behaviours in LLMs via SAE-Based Repres

**Reproducibility Budgets for Open-Weight LLM Evaluation: A Generalizability Theory Study of 7–9B Instruction-Tuned Models (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 74
- **Recorded user turns:** 1
- **Tool calls:** 30
- **Original source:** `logs/chats/exported-trajectories/account-2/agent-ad05b8d9866c10448.jsonl`
- **Structured JSON:** [`4aefade144c226ee3a8e.json`](../../sessions/4a/4aefade144c226ee3a8e.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

74 recorded events

### User

_source line 1 · 2026-05-30T06:19:30.966Z_

You are a senior ML researcher. Research the paper "Steering Knowledge Selection Behaviours in LLMs via SAE-Based Representation Engineering (SpARE)" by Yu Zhao et al., NAACL 2025 Oral, arxiv 2410.15999.

Use WebSearch and WebFetch to:
1. Read the arxiv abstract and paper details
2. Search for OpenReview or ACL Anthology reviews for this paper
3. Find additional details about their SAE-based steering method

For each search/fetch, extract:
- The exact problem gap they identified and HOW they identified it
- The key insight that others missed
- How they formulated the problem differently from prior work
- What existing techniques they adapted/combined (SAEs, representation engineering, contrastive methods)
- Reviewer praise and criticisms (if found)
- Technical method details: how do they identify functional features? How do they use SAEs? What is the steering mechanism? How do they achieve +10% EM?
- Limitations and open questions
- Building blocks (reusable methods/tools/datasets)

Report all findings in detail. Be thorough but focus on HOW they innovate, not just WHAT they did.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "eee12e6f-4b22-4cb0-adff-def0ae050a12",
  "agentId": "ad05b8d9866c10448",
  "type": "user",
  "uuid": "ff32f8f7-0cba-4ddb-8254-a52b826ba231",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "94d88260-dbbe-43d4-abc2-f8f5a7fda9d7",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 2 · 2026-05-30T06:19:30.969Z_

```json
{
  "parentUuid": "ff32f8f7-0cba-4ddb-8254-a52b826ba231",
  "isSidechain": true,
  "agentId": "ad05b8d9866c10448",
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
  "uuid": "e20b943f-56e3-40c6-be64-7959032358a9",
  "timestamp": "2026-05-30T06:19:30.969Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "94d88260-dbbe-43d4-abc2-f8f5a7fda9d7",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 3 · 2026-05-30T06:19:30.970Z_

```json
{
  "parentUuid": "e20b943f-56e3-40c6-be64-7959032358a9",
  "isSidechain": true,
  "agentId": "ad05b8d9866c10448",
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "1cf95bd9-dcc1-4730-8b23-09076ddc181d",
  "timestamp": "2026-05-30T06:19:30.970Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "94d88260-dbbe-43d4-abc2-f8f5a7fda9d7",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Assistant

_source line 4 · 2026-05-30T06:19:33.311Z_



I'll conduct a thorough research investigation of this paper. Let me start by fetching the paper details and searching for reviews simultaneously.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1cf95bd9-dcc1-4730-8b23-09076ddc181d",
  "isSidechain": true,
  "agentId": "ad05b8d9866c10448",
  "requestId": "req_011CbYGX8sDTcHcJXp3togWo",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "729bc511-ce7f-4832-b353-664d1d820694",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "94d88260-dbbe-43d4-abc2-f8f5a7fda9d7",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Na31KKnDoKzA4RNCzhRXTi",
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

_source line 5 · 2026-05-30T06:19:33.834Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_018ZTVJocxu3sojTHvFTBs5d`</summary>

```json
{
  "query": "select:WebSearch,WebFetch",
  "max_results": 2
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "729bc511-ce7f-4832-b353-664d1d820694",
  "isSidechain": true,
  "agentId": "ad05b8d9866c10448",
  "requestId": "req_011CbYGX8sDTcHcJXp3togWo",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "99f44df6-a5cd-45be-8119-d52ff5f97ea8",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "94d88260-dbbe-43d4-abc2-f8f5a7fda9d7",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Na31KKnDoKzA4RNCzhRXTi",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1616,
      "cache_read_input_tokens": 7413,
      "output_tokens": 108,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1616
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 108,
          "cache_read_input_tokens": 7413,
          "cache_creation_input_tokens": 1616,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1616,
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

_source line 6 · 2026-05-30T06:19:33.859Z_

<details><summary>↩ Tool result · `toolu_018ZTVJocxu3sojTHvFTBs5d`</summary>

````text
```json
{
  "type": "tool_reference",
  "tool_name": "WebSearch"
}
```

```json
{
  "type": "tool_reference",
  "tool_name": "WebFetch"
}
```
````

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "99f44df6-a5cd-45be-8119-d52ff5f97ea8",
  "isSidechain": true,
  "promptId": "eee12e6f-4b22-4cb0-adff-def0ae050a12",
  "agentId": "ad05b8d9866c10448",
  "type": "user",
  "uuid": "2a7e440a-5b98-4aff-9dce-1725b411f304",
  "sourceToolAssistantUUID": "99f44df6-a5cd-45be-8119-d52ff5f97ea8",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "94d88260-dbbe-43d4-abc2-f8f5a7fda9d7",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 7 · 2026-05-30T06:19:39.064Z_



Now let me launch multiple searches and fetches in parallel to gather comprehensive information.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2a7e440a-5b98-4aff-9dce-1725b411f304",
  "isSidechain": true,
  "agentId": "ad05b8d9866c10448",
  "requestId": "req_011CbYGXXcCFiGkWu5HQySGa",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "0f3f2afd-2460-47c1-a414-293228a65276",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "94d88260-dbbe-43d4-abc2-f8f5a7fda9d7",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Y2Bg4sTEXAyJHLWP9cLLoc",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1130,
      "cache_read_input_tokens": 9029,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1130,
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

_source line 8 · 2026-05-30T06:19:40.930Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01Aw84fZmL8EbNrVqFnto6dx`</summary>

```json
{
  "url": "https://arxiv.org/abs/2410.15999",
  "prompt": "Extract ALL details from this paper page: title, authors, abstract, submission dates, categories, comments (conference acceptance info). Provide the complete abstract verbatim."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0f3f2afd-2460-47c1-a414-293228a65276",
  "isSidechain": true,
  "agentId": "ad05b8d9866c10448",
  "requestId": "req_011CbYGXXcCFiGkWu5HQySGa",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "14115798-344b-455c-a4cd-1251ba06e635",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "94d88260-dbbe-43d4-abc2-f8f5a7fda9d7",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Y2Bg4sTEXAyJHLWP9cLLoc",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1130,
      "cache_read_input_tokens": 9029,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1130,
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

_source line 9 · 2026-05-30T06:19:42.410Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_012JRNRVBAaNRmeE1VxQkWPy`</summary>

```json
{
  "query": "SpARE SAE-Based Representation Engineering steering knowledge selection LLMs Yu Zhao NAACL 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "14115798-344b-455c-a4cd-1251ba06e635",
  "isSidechain": true,
  "agentId": "ad05b8d9866c10448",
  "requestId": "req_011CbYGXXcCFiGkWu5HQySGa",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "07bb69a8-15e3-4520-acf1-69f29d845d58",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "94d88260-dbbe-43d4-abc2-f8f5a7fda9d7",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Y2Bg4sTEXAyJHLWP9cLLoc",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1130,
      "cache_read_input_tokens": 9029,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1130,
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

_source line 10 · 2026-05-30T06:19:42.853Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_013kyRNpBL1nxAmhMpu7u92K`</summary>

```json
{
  "query": "arxiv 2410.15999 SpARE openreview reviews NAACL 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "07bb69a8-15e3-4520-acf1-69f29d845d58",
  "isSidechain": true,
  "agentId": "ad05b8d9866c10448",
  "requestId": "req_011CbYGXXcCFiGkWu5HQySGa",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "f5659ac5-21d8-4e52-aaa6-b4d8f0834dc6",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "94d88260-dbbe-43d4-abc2-f8f5a7fda9d7",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Y2Bg4sTEXAyJHLWP9cLLoc",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1130,
      "cache_read_input_tokens": 9029,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1130,
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

_source line 11 · 2026-05-30T06:19:45.617Z_

<details><summary>↩ Tool result · `toolu_01Aw84fZmL8EbNrVqFnto6dx`</summary>

```text
# Paper Details

**Title:** Steering Knowledge Selection Behaviours in LLMs via SAE-Based Representation Engineering

**Authors:** Yu Zhao, Alessio Devoto, Giwon Hong, Xiaotang Du, Aryo Pradipta Gema, Hongru Wang, Xuanli He, Kam-Fai Wong, Pasquale Minervini

**Category:** Computer Science > Computation and Language (cs.CL)

**Submission Dates:**
- v1: October 21, 2024
- v2: October 25, 2024
- v3: February 9, 2025

**Comments:** Accepted at NAACL 2025

**Abstract:** The research addresses how LLMs handle conflicting information between stored parametric knowledge and context-provided details. The team discovered that models internally register conflict signals at intermediate layers. They developed SpARE, a training-free method utilizing pre-trained sparse autoencoders to modify knowledge selection behaviors during inference. The approach identifies functional features controlling knowledge selection and edits internal activations accordingly. Results demonstrate the method surpasses existing representation engineering by "+10%" and contrastive decoding methods by "+15%" in open-domain question-answering tasks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "14115798-344b-455c-a4cd-1251ba06e635",
  "isSidechain": true,
  "promptId": "eee12e6f-4b22-4cb0-adff-def0ae050a12",
  "agentId": "ad05b8d9866c10448",
  "type": "user",
  "uuid": "c81a8e6d-d807-40a2-b7a9-2f29da9cbeb6",
  "sourceToolAssistantUUID": "14115798-344b-455c-a4cd-1251ba06e635",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "94d88260-dbbe-43d4-abc2-f8f5a7fda9d7",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-30T06:19:48.287Z_

<details><summary>↩ Tool result · `toolu_012JRNRVBAaNRmeE1VxQkWPy`</summary>

```text
Web search results for query: "SpARE SAE-Based Representation Engineering steering knowledge selection LLMs Yu Zhao NAACL 2025"

Links: [{"title":"[Quick Review] Steering Knowledge Selection Behaviours in LLMs via SAE-Based Representation Engineering","url":"https://liner.com/review/steering-knowledge-selection-behaviours-in-llms-via-saebased-representation-engineering"},{"title":"Steering Knowledge Selection Behaviours in LLMs via SAE-Based Representation Engineering - ACL Anthology","url":"https://aclanthology.org/2025.naacl-long.264/"},{"title":"Paper page - Steering Knowledge Selection Behaviours in LLMs via SAE-Based Representation Engineering","url":"https://huggingface.co/papers/2410.15999"},{"title":"Steering Knowledge Selection Behaviours in LLMs via SAE-Based Representation Engineering","url":"https://arxiv.org/html/2410.15999v1"},{"title":"[PDF] Steering Knowledge Selection Behaviours in LLMs via SAE-Based Representation Engineering | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Steering-Knowledge-Selection-Behaviours-in-LLMs-via-Zhao-Devoto/d2c1b1a8ac40fbd45e8a91504b1a131f99bad02f"},{"title":"Steering Knowledge Selection Behaviours in LLMs via SAE-Based Representation Engineering","url":"https://www.rohan-paul.com/p/steering-knowledge-selection-behaviours"},{"title":"[Literature Review] Steering Knowledge Selection Behaviours in LLMs via SAE-Based Representation Engineering","url":"https://www.themoonlight.io/en/review/steering-knowledge-selection-behaviours-in-llms-via-sae-based-representation-engineering"},{"title":"[2410.15999] Steering Knowledge Selection Behaviours in LLMs via SAE-Based Representation Engineering","url":"https://arxiv.org/abs/2410.15999"}]

Based on the search results, I found comprehensive information about SpARE:

## SpARE: SAE-Based Representation Engineering

SpARE is a training-free representation engineering method that uses pre-trained sparse auto-encoders (SAEs) to control the knowledge selection behaviour of LLMs.

### How It Works

SpARE identifies the functional features that control the knowledge selection behaviours and applies them to edit the internal activations of LLMs at inference time. Unlike existing representation engineering methods that directly modify polysemantic dense vectors, SpARE uses SAEs to decompose them into monosemantic features for more precise editing.

### Performance

SpARE can effectively control the usage of either knowledge source to resolve knowledge conflict in open-domain question-answering tasks, surpassing existing representation engineering methods (+10%) as well as contrastive decoding methods (+15%).

### Purpose

The method addresses knowledge conflicts—when parametric knowledge may conflict with the information provided in the context, a phenomenon known as context-memory knowledge conflicts, which can lead to undesirable model behaviour, such as reliance on outdated or incorrect information.

The paper was published at **NAACL 2025** and is authored by researchers including Yu Zhao, as indicated in the search results.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "07bb69a8-15e3-4520-acf1-69f29d845d58",
  "isSidechain": true,
  "promptId": "eee12e6f-4b22-4cb0-adff-def0ae050a12",
  "agentId": "ad05b8d9866c10448",
  "type": "user",
  "uuid": "3baacf50-2c76-4cde-a8f2-3f1ba15cb823",
  "sourceToolAssistantUUID": "07bb69a8-15e3-4520-acf1-69f29d845d58",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "94d88260-dbbe-43d4-abc2-f8f5a7fda9d7",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 13 · 2026-05-30T06:19:50.008Z_

<details><summary>↩ Tool result · `toolu_013kyRNpBL1nxAmhMpu7u92K`</summary>

```text
Web search results for query: "arxiv 2410.15999 SpARE openreview reviews NAACL 2025"

Links: [{"title":"NAACL 2025 | OpenReview","url":"https://openreview.net/group?id=aclweb.org%2FNAACL%2F2025"},{"title":"[2410.15999] Steering Knowledge Selection Behaviours in LLMs via SAE-Based Representation Engineering","url":"https://arxiv.org/abs/2410.15999"},{"title":"Large Language Models for Supporting Clear Writing and Detecting Spin in Randomized Controlled Trials in Oncology: Comparative Analysis of GPT Models and Prompts","url":"https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12823016/"},{"title":"Computer Science Oct 2024","url":"https://arxiv.org/list/cs/2024-10?skip=8000&show=500"},{"title":"arXiv:2410.15999v3 [cs.CL] 9 Feb 2025","url":"https://arxiv.org/pdf/2410.15999"},{"title":"Performance of reasoning large language models on nephrology multiple-choice questions","url":"https://www.medrxiv.org/content/10.64898/2025.12.03.25341427.full.pdf"},{"title":"OpenReviewer: A Specialized Large Language Model for Generating Critical Scientific Paper Reviews","url":"https://arxiv.org/html/2412.11948v3"},{"title":"Physician- and Large Language Model-Generated Hospital Discharge Summaries: A Blinded, Comparative Quality and Safety Study","url":"https://www.medrxiv.org/content/10.1101/2024.09.29.24314562.full.pdf"}]

Based on the search results, I found information about the paper arxiv 2410.15999:

The paper "Steering Knowledge Selection Behaviours in LLMs via SAE-Based Representation Engineering" by Yu Zhao, Alessio Devoto, Giwon Hong, Xiaotang Du, Aryo Pradipta Gema, Hongru Wang, Xuanli He, Kam-Fai Wong, and Pasquale Minervini has been accepted at NAACL 2025.

The paper proposes SpARE, a training-free representation engineering method that uses pre-trained sparse auto-encoders (SAEs) to control the knowledge selection behaviour of LLMs by identifying functional features that control the knowledge selection behaviours and applying them to edit the internal activations of LLMs at inference time.

The experimental results show that SpARE can effectively control the usage of either knowledge source to resolve knowledge conflict in open-domain question-answering tasks, surpassing existing representation engineering methods.

However, the search results do not contain the specific OpenReview reviews for this paper. To access the detailed reviews, you would need to visit the NAACL 2025 OpenReview page directly at https://openreview.net/group?id=aclweb.org%2FNAACL%2F2025.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f5659ac5-21d8-4e52-aaa6-b4d8f0834dc6",
  "isSidechain": true,
  "promptId": "eee12e6f-4b22-4cb0-adff-def0ae050a12",
  "agentId": "ad05b8d9866c10448",
  "type": "user",
  "uuid": "051d0d46-d15a-473b-b879-40e7beecd1c2",
  "sourceToolAssistantUUID": "f5659ac5-21d8-4e52-aaa6-b4d8f0834dc6",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "94d88260-dbbe-43d4-abc2-f8f5a7fda9d7",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 14 · 2026-05-30T06:19:59.560Z_

Good, I have the basic overview. Now let me fetch the full paper HTML, the ACL Anthology page, and search for reviews.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "051d0d46-d15a-473b-b879-40e7beecd1c2",
  "isSidechain": true,
  "agentId": "ad05b8d9866c10448",
  "requestId": "req_011CbYGYYV4PZrCP8KmWzBo4",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "cf09f99f-d62a-464f-8869-d5b60c75ab00",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "94d88260-dbbe-43d4-abc2-f8f5a7fda9d7",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RWfnve5DAb3DnziJUGCfwc",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2187,
      "cache_read_input_tokens": 10159,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2187,
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

_source line 15 · 2026-05-30T06:20:05.050Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01GyGnhxn96b2NknZA99JvsP`</summary>

```json
{
  "url": "https://arxiv.org/html/2410.15999v3",
  "prompt": "Extract ALL technical details from this paper. I need:\n1. The EXACT problem formulation - how do they define knowledge conflicts? What datasets?\n2. The preliminary analysis / discovery phase - how did they discover conflict signals in intermediate layers? What probing experiments did they do?\n3. The FULL SpARE method: how do they use SAEs to decompose activations? How do they identify functional features? What is the contrastive method for finding steering features? What is the exact steering/editing mechanism (equations)?\n4. Baselines compared against\n5. Main results with exact numbers\n6. Ablation studies and analysis\n7. Limitations section\n8. Key related work they build on\nProvide as much detail as possible including equations, layer numbers, feature selection criteria."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "cf09f99f-d62a-464f-8869-d5b60c75ab00",
  "isSidechain": true,
  "agentId": "ad05b8d9866c10448",
  "requestId": "req_011CbYGYYV4PZrCP8KmWzBo4",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "9702a5fc-fad4-4887-8ac1-dd040201fcfa",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "94d88260-dbbe-43d4-abc2-f8f5a7fda9d7",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RWfnve5DAb3DnziJUGCfwc",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2187,
      "cache_read_input_tokens": 10159,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2187,
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

_source line 16 · 2026-05-30T06:20:07.398Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01AwVKBLZNKA8yJp8zQzc4rv`</summary>

```json
{
  "url": "https://aclanthology.org/2025.naacl-long.264/",
  "prompt": "Extract all information from this ACL Anthology page: authors, venue, DOI, abstract, PDF link, any supplementary materials, citation info, and any links to reviews or discussion."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9702a5fc-fad4-4887-8ac1-dd040201fcfa",
  "isSidechain": true,
  "agentId": "ad05b8d9866c10448",
  "requestId": "req_011CbYGYYV4PZrCP8KmWzBo4",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "35a5b2ab-6807-4f3f-a6a4-d61f7fb0be90",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "94d88260-dbbe-43d4-abc2-f8f5a7fda9d7",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RWfnve5DAb3DnziJUGCfwc",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2187,
      "cache_read_input_tokens": 10159,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2187,
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

_source line 17 · 2026-05-30T06:20:07.770Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_011J9e98QGPUHnTxsmHpPHrX`</summary>

```json
{
  "query": "\"Steering Knowledge Selection\" \"SpARE\" openreview.net NAACL 2025 review"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "35a5b2ab-6807-4f3f-a6a4-d61f7fb0be90",
  "isSidechain": true,
  "agentId": "ad05b8d9866c10448",
  "requestId": "req_011CbYGYYV4PZrCP8KmWzBo4",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "fa59ef8c-9afa-4972-8e05-28d071e4e51e",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "94d88260-dbbe-43d4-abc2-f8f5a7fda9d7",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RWfnve5DAb3DnziJUGCfwc",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2187,
      "cache_read_input_tokens": 10159,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2187,
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

_source line 18 · 2026-05-30T06:20:08.775Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01KYVn5ShhkWTxXCqBZUtPPg`</summary>

```json
{
  "query": "SpARE sparse autoencoder representation engineering knowledge conflict steering method details technical"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "fa59ef8c-9afa-4972-8e05-28d071e4e51e",
  "isSidechain": true,
  "agentId": "ad05b8d9866c10448",
  "requestId": "req_011CbYGYYV4PZrCP8KmWzBo4",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "8ddbaa1d-f894-4d14-b0d6-6fe0e7e9ed85",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "94d88260-dbbe-43d4-abc2-f8f5a7fda9d7",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RWfnve5DAb3DnziJUGCfwc",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2187,
      "cache_read_input_tokens": 10159,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2187,
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

_source line 19 · 2026-05-30T06:20:12.543Z_

<details><summary>↩ Tool result · `toolu_01AwVKBLZNKA8yJp8zQzc4rv`</summary>

```text
# Paper Information: SpARE - SAE-Based Representation Engineering for LLMs

## Authors
Yu Zhao, Alessio Devoto, Giwon Hong, Xiaotang Du, Aryo Pradipta Gema, Hongru Wang, Xuanli He, Kam-Fai Wong, Pasquale Minervini

## Venue & Publication Details
- **Conference:** NAACL 2025 (Nations of the Americas Chapter of the Association for Computational Linguistics)
- **Location:** Albuquerque, New Mexico
- **Month/Year:** April 2025
- **Pages:** 5117–5136
- **Volume:** Proceedings of the 2025 Conference (Volume 1: Long Papers)

## Identifiers
- **DOI:** 10.18653/v1/2025.naacl-long.264
- **Anthology ID:** 2025.naacl-long.264
- **BibTeX Key:** zhao-etal-2025-steering

## Abstract
The paper addresses "context-memory knowledge conflicts" where LLM parametric knowledge contradicts contextual information. The authors propose SpARE, a "training-free representation engineering method" utilizing sparse auto-encoders to control knowledge selection during inference. Results reportedly exceed existing methods by 10% and contrastive decoding by 15% on open-domain question-answering tasks.

## Links
- **PDF:** https://aclanthology.org/2025.naacl-long.264.pdf
- **Full Citation Page:** https://aclanthology.org/2025.naacl-long.264/

## Additional Resources
The page provides multiple citation formats (BibTeX, MODS XML, Endnote, Markdown) but lists no supplementary materials, reviews, or discussion links.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "35a5b2ab-6807-4f3f-a6a4-d61f7fb0be90",
  "isSidechain": true,
  "promptId": "eee12e6f-4b22-4cb0-adff-def0ae050a12",
  "agentId": "ad05b8d9866c10448",
  "type": "user",
  "uuid": "1bb039fa-fcac-4783-aff1-b90c644cb694",
  "sourceToolAssistantUUID": "35a5b2ab-6807-4f3f-a6a4-d61f7fb0be90",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "94d88260-dbbe-43d4-abc2-f8f5a7fda9d7",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-30T06:20:13.287Z_

<details><summary>↩ Tool result · `toolu_011J9e98QGPUHnTxsmHpPHrX`</summary>

```text
Web search results for query: ""Steering Knowledge Selection" "SpARE" openreview.net NAACL 2025 review"

Links: [{"title":"[Quick Review] Steering Knowledge Selection Behaviours in LLMs via SAE-Based Representation Engineering","url":"https://liner.com/review/steering-knowledge-selection-behaviours-in-llms-via-saebased-representation-engineering"},{"title":"Steering Knowledge Selection Behaviours in LLMs via SAE-Based Representation Engineering - ACL Anthology","url":"https://aclanthology.org/2025.naacl-long.264/"},{"title":"Steering Knowledge Selection Behaviours in LLMs","url":"https://arxiv.org/pdf/2410.15999"},{"title":"NAACL 2025 Workshop | OpenReview","url":"https://openreview.net/group?id=aclweb.org%2FNAACL%2F2025%2FWorkshop"},{"title":"NAACL 2025 | OpenReview","url":"https://openreview.net/group?id=aclweb.org%2FNAACL%2F2025"},{"title":"Second Call for Main Conference Papers - NAACL-HLT 2025","url":"https://2025.naacl.org/calls/papers/"},{"title":"SteerConf: Steering LLMs for Confidence Elicitation | OpenReview","url":"https://openreview.net/forum?id=5sgK63Zshg"}]

Based on the search results, I found information about the paper you're looking for:

SpARE is a training-free representation engineering method that uses pre-trained sparse auto-encoders (SAEs) to control the knowledge selection behaviour of LLMs. The paper "Steering Knowledge Selection Behaviours in LLMs via SAE-Based Representation Engineering" was published in Proceedings of the 2025 Conference of the Nations of the Americas Chapter of the Association for Computational Linguistics: Human Language Technologies in Albuquerque, New Mexico.

SpARE identifies the functional features that control the knowledge selection behaviours and applies them to edit the internal activations of LLMs at inference time. The paper is authored by Zhao et al. and appears in the NAACL 2025 long papers track.

The paper appears to be published in the ACL Anthology, though I also found references to it on arXiv and other review platforms. If you're specifically looking for OpenReview.net links or peer review information, those details weren't available in these particular search results.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "fa59ef8c-9afa-4972-8e05-28d071e4e51e",
  "isSidechain": true,
  "promptId": "eee12e6f-4b22-4cb0-adff-def0ae050a12",
  "agentId": "ad05b8d9866c10448",
  "type": "user",
  "uuid": "614410db-5609-4b6e-a432-ae305d76faa3",
  "sourceToolAssistantUUID": "fa59ef8c-9afa-4972-8e05-28d071e4e51e",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "94d88260-dbbe-43d4-abc2-f8f5a7fda9d7",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 21 · 2026-05-30T06:20:16.436Z_

<details><summary>↩ Tool result · `toolu_01KYVn5ShhkWTxXCqBZUtPPg`</summary>

```text
Web search results for query: "SpARE sparse autoencoder representation engineering knowledge conflict steering method details technical"

Links: [{"title":"Steering Knowledge Selection Behaviours in LLMs via SAE-Based   Representation Engineering","url":"https://arxiv.org/pdf/2410.15999"},{"title":"Paper page - Steering Knowledge Selection Behaviours in LLMs via SAE-Based Representation Engineering","url":"https://huggingface.co/papers/2410.15999"},{"title":"Interpretable LLM Guardrails via Sparse Representation Steering","url":"https://arxiv.org/html/2503.16851"},{"title":"Sparse Autoencoder Features for Classifications and Transferability","url":"https://arxiv.org/html/2502.11367v1"},{"title":"Steering Knowledge Selection Behaviours in LLMs via SAE-Based Representation Engineering | AI Research Paper Details","url":"https://www.aimodels.fyi/papers/arxiv/steering-knowledge-selection-behaviours-llms-via-sae"},{"title":"Interpretable LLM Guardrails via Sparse Representation Steering","url":"https://arxiv.org/pdf/2503.16851"},{"title":"Steering Language Model Refusal with Sparse Autoencoders","url":"https://arxiv.org/html/2411.11296v1"}]

Based on the search results, here are the technical details about SpARE (Sparse Auto-Encoder-based Representation Engineering):

## Overview

SpARE is a training-free representation engineering method that uses pre-trained sparse auto-encoders (SAEs) to control the knowledge selection behaviour of LLMs.

## The Problem It Addresses

LLMs' parametric knowledge may conflict with the information provided in the context -- this phenomenon, known as context-memory knowledge conflicts, can lead to undesirable model behaviour, such as reliance on outdated or incorrect information.

## Technical Mechanism

LLMs can internally register signals of knowledge conflict at mid-layers, and such signals allow detection of whether a knowledge conflict occurs and use inference-time intervention strategies to resolve it.

SpARE identifies the functional features that control the knowledge selection behaviours and applies them to edit the internal activations of LLMs at inference time.

## Key Technical Steps

SpARE first identifies the SAE activations that are related to specific knowledge selection behaviours; then, it extracts functional features that control the usage of contextual and parametric knowledge, and finally applies them to steer the behaviour of the model.

## Performance Results

SpARE can effectively control the usage of either knowledge source to resolve knowledge conflict in open-domain question-answering tasks, surpassing existing representation engineering methods (+10%) as well as contrastive decoding methods (+15%).


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "8ddbaa1d-f894-4d14-b0d6-6fe0e7e9ed85",
  "isSidechain": true,
  "promptId": "eee12e6f-4b22-4cb0-adff-def0ae050a12",
  "agentId": "ad05b8d9866c10448",
  "type": "user",
  "uuid": "24d53e3b-b334-447e-a66a-50ddddb6ea09",
  "sourceToolAssistantUUID": "8ddbaa1d-f894-4d14-b0d6-6fe0e7e9ed85",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "94d88260-dbbe-43d4-abc2-f8f5a7fda9d7",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 22 · 2026-05-30T06:20:29.978Z_

<details><summary>↩ Tool result · `toolu_01GyGnhxn96b2NknZA99JvsP`</summary>

```text
# Technical Details Extraction: SpARE Paper

## 1. Problem Formulation

**Knowledge Conflict Definition:**
Context-memory knowledge conflicts occur when "contextual knowledge may sometimes conflict with the parametric knowledge of the model." The paper focuses on scenarios where "the knowledge stored in their parameters (parametric knowledge) can be inaccurate or outdated" while external retrieval systems provide conflicting information.

**Problem Setup:**
Following prior work, they use open-domain QA with knowledge conflicts formulated as (Q, E_M, M, E_C, C) where:
- Q: question
- E_M: evidence supporting memorized knowledge (answer M)
- E_C: conflicting evidence (answer C)
- M, C: corresponding answers

**Datasets:**
- NQSwap (Longpre et al., 2021)
- Macnoise (Hong et al., 2024)

---

## 2. Preliminary Discovery Phase

**Conflict Detection via Linear Probing:**

They trained logistic regression models to classify whether activations come from datasets with conflict (D_EC) or without (D_EM). Key findings:

- "Probing accuracy increases from the first layer to the middle layers, and this trend is the same across different types of activations"
- Mid-layer residual streams show highest AUROC for distinguishing conflicted vs. non-conflicted inputs
- Later layers show declining probing accuracy, suggesting "MLP and Self-Attention modules do not further add the signal of conflicting knowledge"

**Tested Activation Types:**
Hidden states, MLP activations, Self-Attention activations across all layers.

---

## 3. Full SpARE Method

### 3.1 SAE Background

SAEs encode activation h ∈ ℝ^d into sparse vector z ∈ ℝ^n:

**Encoding:** f_θ(h) = σ(W_θ(h - b) + b_θ) = z

**Decoding:** g_φ(z) = W_φ·z = Σ(z_i · f_i) + b = ĥ

Where:
- σ is ReLU (non-negative output)
- f_i are learned monosemantic feature vectors
- z_i are activation values

### 3.2 Step 1: Collecting Activations with Different Behaviors

From conflicted instances D_EC, separate based on model predictions:
- D_C: instances where model generates contextual answer C
- D_M: instances where model relies on parametric knowledge M

For N samples, collect hidden states at last input position:
- {h^j_C}^N_{j=1} from D_C
- {h^j_M}^N_{j=1} from D_M

Convert to SAE activations: z^j_C = f_θ(h^j_C), z^j_M = f_θ(h^j_M)

Compute mean vectors: z̄_C = mean({z^j_C}), z̄_M = mean({z^j_M})

### 3.3 Step 2: Identifying Functional SAE Activations

**Mutual Information Selection:**

Calculate mutual information I(Z_i; Y) between each SAE activation Z_i and behavior Y ∈ {C, M}. Select top-k activations with highest mutual information, denoted as Z.

**Behavior Correlation:**

For each Z_i ∈ Z, determine correlation:
- If E_C[Z_i] - E_M[Z_i] > 0: positively correlated with contextual knowledge
- If E_C[Z_i] - E_M[Z_i] < 0: positively correlated with parametric knowledge

**Construct Functional Activations:**

z_Ci = {z̄_Ci if E_C[Z_i] - E_M[Z_i] > 0; 0 otherwise}

z_Mi = {z̄_Mi if E_C[Z_i] - E_M[Z_i] < 0; 0 otherwise}

Result: z_C and z_M ∈ ℝ^n that separately encode contextual and parametric steering directions.

### 3.4 Step 3: Editing Activations (Inference-Time Steering)

To steer toward parametric knowledge (removing contextual bias):

**Remove undesired features (Eq. 2):**
z_i^- = min{z_i, z_Ci}

Constraint: "subtract at most z_i when z_i < z_Ci" to maintain non-negativity.

**Add desired features (Eq. 3):**
z_i^+ = max{z_Mi - z_i, 0}

Constraint: "no excess value is added once the activation reaches z_Mi"

**Edit hidden state (Eq. 4):**
h' = h + α(-g_φ(z^-) + g_φ(z^+))

Where α ∈ ℝ^+ controls editing strength.

**Key Design Choice:** They edit hidden states directly rather than SAE activations because: (1) "direct SAE editing results in unexpected information loss due to reconstruction loss," and (2) "the SAE activation requires non-negative values, which prevents flexible control via α."

**Hyperparameters:**
- Llama2-7B: layers 12-15
- Llama3-8B: layers 13-16
- Gemma2-9B: layers 23-25 and 29-31

---

## 4. Baselines

**Representation Engineering Methods:**
- TaskVec (Hendel et al., 2023)
- ActAdd (Turner et al., 2023a)
- SEA with linear and non-linear (SqExp) variants (Qiu et al., 2024)

**Contrastive Decoding Methods:**
- DoLa (Chuang et al., 2024)
- CAD (Shi et al., 2024)

**In-Context Learning:**
- ICL with demonstrations using E_C + C for contextual steering; E_C + M for parametric steering

---

## 5. Main Results (Table 1)

**Steering to Parametric Knowledge (EM_M):**

| Model | Without | SpARE |
|-------|---------|-------|
| Llama3-8B | 26.63% | **47.51%** |
| Llama2-7B | 22.23% | **43.76%** |
| Gemma2-9B | 26.32% | **44.11%** |

**Steering to Contextual Knowledge (EM_C):**

| Model | Without | SpARE |
|-------|---------|-------|
| Llama3-8B | 42.69% | **77.69%** |
| Llama2-7B | 41.67% | **69.32%** |
| Gemma2-9B | 45.96% | **73.78%** |

**Comparative Improvements:**
- "+10%" over representation engineering baselines
- "+15%" over contrastive decoding
- "+7%" over in-context learning

---

## 6. Ablation Studies

**Three Variants (Figure 4c):**

1. **Input-Independent:** Uses z_C and z_M directly without computing z^- and z^+ from input—"fails to steer the usage of knowledge"

2. **Remove Only:** Edits by only removing contextual features—"results in zero accuracy on both EM_M and EM_C"

3. **Add Only:** Edits by only adding parametric features—"leads to worse performance than without controlling"

**Conclusion:** All components (removal + addition + input-dependent constraints) are necessary.

---

## 7. Analysis & Key Findings

**Layer Analysis (Figure 5):**
"SpARE can control the behaviour of LLMs most effectively at mid-layers" for both models tested, aligning with where conflict signals are strongest.

**Residual Stream Analysis (Section 6.2):**
- When steering toward parametric knowledge: "probing performance decreases immediately," indicating conflict signal fades
- When steering toward contextual knowledge: "probing performance increases"
- Skewness (kurtosis) of residual stream shows distinct patterns: contextual selection produces "significantly more skewed" representations than parametric selection

---

## 8. Limitations

The paper acknowledges:
- Method relies on availability of pre-trained SAEs
- Evaluation limited to ODQA tasks
- Computational cost of SAE training (though inference-time cost is minimal)
- Generalization to other knowledge conflict types unexplored

---

## 9. Key Related Work Foundation

**SAE Foundation (Bricken et al., 2023; Huben et al., 2024):** Established that SAEs decompose polysemantic activations into monosemantic features.

**Representation Engineering (Turner et al., 2023a; Zou et al., 2023a):** Showed activations can be edited to steer behavior, but struggled with polysemy.

**Knowledge Conflicts (Longpre et al., 2021; Hong et al., 2024):** Established datasets and problem formulation; prior work showed LLMs preferentially use context over parametric knowledge.

**Task Vectors (Hendel et al., 2023):** Inspired hypothesis that combinations of SAE features encode functional behaviors.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "9702a5fc-fad4-4887-8ac1-dd040201fcfa",
  "isSidechain": true,
  "promptId": "eee12e6f-4b22-4cb0-adff-def0ae050a12",
  "agentId": "ad05b8d9866c10448",
  "type": "user",
  "uuid": "47ab4fcc-698d-4df1-a6cf-c6db502d809f",
  "sourceToolAssistantUUID": "9702a5fc-fad4-4887-8ac1-dd040201fcfa",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "94d88260-dbbe-43d4-abc2-f8f5a7fda9d7",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 23 · 2026-05-30T06:20:32.716Z_

Excellent. I now have strong technical details. Let me search for reviews and additional analysis, including the OpenReview forum and blog posts with commentary.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "47ab4fcc-698d-4df1-a6cf-c6db502d809f",
  "isSidechain": true,
  "agentId": "ad05b8d9866c10448",
  "requestId": "req_011CbYGbV8ESb7YWtxzCLDnT",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "494e2e50-010c-4764-9d2f-13aba8955f04",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "94d88260-dbbe-43d4-abc2-f8f5a7fda9d7",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017uWnPLkK2QYmFRUk6dqn7L",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1791,
      "cache_creation_input_tokens": 2910,
      "cache_read_input_tokens": 12346,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2910,
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

_source line 24 · 2026-05-30T06:20:33.216Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_0183oFjbTXcuuJo2Yuziza7C`</summary>

```json
{
  "query": "openreview.net \"Steering Knowledge Selection Behaviours\" forum NAACL"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "494e2e50-010c-4764-9d2f-13aba8955f04",
  "isSidechain": true,
  "agentId": "ad05b8d9866c10448",
  "requestId": "req_011CbYGbV8ESb7YWtxzCLDnT",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "7c1da496-9f26-4686-a2f8-c14e02419195",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "94d88260-dbbe-43d4-abc2-f8f5a7fda9d7",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017uWnPLkK2QYmFRUk6dqn7L",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1791,
      "cache_creation_input_tokens": 2910,
      "cache_read_input_tokens": 12346,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2910,
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

_source line 25 · 2026-05-30T06:20:35.122Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01Vm1hUdfNE31XTpRqREBw3R`</summary>

```json
{
  "url": "https://liner.com/review/steering-knowledge-selection-behaviours-in-llms-via-saebased-representation-engineering",
  "prompt": "Extract ALL review details: strengths, weaknesses, questions, reviewer comments, scores, criticisms, praise. Provide the full text of all review content available."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7c1da496-9f26-4686-a2f8-c14e02419195",
  "isSidechain": true,
  "agentId": "ad05b8d9866c10448",
  "requestId": "req_011CbYGbV8ESb7YWtxzCLDnT",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "364af677-bdcb-43f0-8e41-78376b61e444",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "94d88260-dbbe-43d4-abc2-f8f5a7fda9d7",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017uWnPLkK2QYmFRUk6dqn7L",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1791,
      "cache_creation_input_tokens": 2910,
      "cache_read_input_tokens": 12346,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2910,
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

_source line 26 · 2026-05-30T06:20:36.469Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_014TM8Ga7wmGWtEpyBawBT72`</summary>

```json
{
  "url": "https://huggingface.co/papers/2410.15999",
  "prompt": "Extract all information: upvotes, comments, discussion, community feedback, any linked models or datasets, and any community analysis of this paper."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "364af677-bdcb-43f0-8e41-78376b61e444",
  "isSidechain": true,
  "agentId": "ad05b8d9866c10448",
  "requestId": "req_011CbYGbV8ESb7YWtxzCLDnT",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "3ecb1bf3-2e1c-44a1-9711-92f2982d3480",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "94d88260-dbbe-43d4-abc2-f8f5a7fda9d7",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017uWnPLkK2QYmFRUk6dqn7L",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1791,
      "cache_creation_input_tokens": 2910,
      "cache_read_input_tokens": 12346,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2910,
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

### Tool result

_source line 27 · 2026-05-30T06:20:37.046Z_

<details><summary>↩ Tool result · `toolu_014TM8Ga7wmGWtEpyBawBT72`</summary>

```text
&lt;persisted-output>
Output too large (80.4KB). Full output saved to: /home/ubuntu/.claude-account-2/projects/-home-ubuntu-idea-adversarial/94d88260-dbbe-43d4-abc2-f8f5a7fda9d7/tool-results/toolu_014TM8Ga7wmGWtEpyBawBT72.txt

Preview (first 2KB):
Title: Steering Knowledge Selection Behaviours in LLMs via SAE-Based Representation Engineering

URL Source: https://arxiv.org/html/2410.15999

Published Time: Tue, 11 Feb 2025 02:00:40 GMT

Markdown Content:
 Abstract
1Introduction
2Background
3Detection of Knowledge Conflicts
4Resolving Knowledge Conflicts by Representation Engineering
5Experimental Results
6Analysis and Discussion
7Related Works
8Conclusions
 References
Steering Knowledge Selection Behaviours in LLMs via SAE-Based Representation Engineering
Yu Zhao1 Alessio Devoto3 Giwon Hong1 Xiaotang Du1 Aryo Pradipta Gema1
Hongru Wang2 Xuanli He4 Kam-Fai Wong2 Pasquale Minervini1,5
1University of Edinburgh  2The Chinese University of Hong Kong
3Sapienza University of Rome  4University College London  5Miniml.AI
{yu.zhao, p.minervini}@ed.ac.uk
\faGithub  https://github.com/yuzhaouoe/SAE-based-representation-engineering
Abstract

Large language models (LLMs) can store a significant amount of factual knowledge in their parameters. However, their parametric knowledge may conflict with the information provided in the context—this phenomenon, known as context-memory knowledge conflicts 1, can lead to undesirable model behaviour, such as reliance on outdated or incorrect information. Analysing the internal activations of LLMs, we find that they can internally register the signals of knowledge conflict at mid-layers. Such signals allow us to detect whether a knowledge conflict occurs and use inference-time intervention strategies to resolve it. In this work, we propose SpARE, a training-free representation engineering method that uses pre-trained sparse auto-encoders (SAEs) to control the knowledge selection behaviour of LLMs. SpARE identifies the functional features that control the knowledge selection behaviours and applies them to edit the internal activations of LLMs at inference time. Our experimental results show that SpARE can effectively control the usage of either knowledge source to resolve knowledge conflic
...
&lt;/persisted-output>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "3ecb1bf3-2e1c-44a1-9711-92f2982d3480",
  "isSidechain": true,
  "promptId": "eee12e6f-4b22-4cb0-adff-def0ae050a12",
  "agentId": "ad05b8d9866c10448",
  "type": "user",
  "uuid": "3e94bea9-2649-4e50-9379-89bc570a52c2",
  "sourceToolAssistantUUID": "3ecb1bf3-2e1c-44a1-9711-92f2982d3480",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "94d88260-dbbe-43d4-abc2-f8f5a7fda9d7",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 28 · 2026-05-30T06:20:37.442Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_015SYmuvfWKEEJ8fVr94F3AW`</summary>

```json
{
  "url": "https://www.aimodels.fyi/papers/arxiv/steering-knowledge-selection-behaviours-llms-via-sae",
  "prompt": "Extract all technical analysis, review commentary, key insights, methodology details, and any critical assessment of the SpARE paper."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3e94bea9-2649-4e50-9379-89bc570a52c2",
  "isSidechain": true,
  "agentId": "ad05b8d9866c10448",
  "requestId": "req_011CbYGbV8ESb7YWtxzCLDnT",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "593beeb6-4538-4e51-8f7d-18420f75c149",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "94d88260-dbbe-43d4-abc2-f8f5a7fda9d7",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017uWnPLkK2QYmFRUk6dqn7L",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1791,
      "cache_creation_input_tokens": 2910,
      "cache_read_input_tokens": 12346,
      "output_tokens": 419,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2910
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1791,
          "output_tokens": 419,
          "cache_read_input_tokens": 12346,
          "cache_creation_input_tokens": 2910,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2910,
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

_source line 29 · 2026-05-30T06:20:37.661Z_

<details><summary>↩ Tool result · `toolu_015SYmuvfWKEEJ8fVr94F3AW`</summary>

```text
The server returned HTTP 403 Forbidden.

The response body was not retrieved. If this URL requires authentication, use an authenticated tool (e.g. `gh` for GitHub, or an MCP-provided fetch tool) instead of WebFetch.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "593beeb6-4538-4e51-8f7d-18420f75c149",
  "isSidechain": true,
  "promptId": "eee12e6f-4b22-4cb0-adff-def0ae050a12",
  "agentId": "ad05b8d9866c10448",
  "type": "user",
  "uuid": "4d4d5493-260c-4c87-88a9-a7ebf10c159b",
  "sourceToolAssistantUUID": "593beeb6-4538-4e51-8f7d-18420f75c149",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "94d88260-dbbe-43d4-abc2-f8f5a7fda9d7",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 30 · 2026-05-30T06:20:38.631Z_

<details><summary>↩ Tool result · `toolu_0183oFjbTXcuuJo2Yuziza7C`</summary>

```text
Web search results for query: "openreview.net "Steering Knowledge Selection Behaviours" forum NAACL"

Links: [{"title":"[Quick Review] Steering Knowledge Selection Behaviours in LLMs via SAE-Based Representation Engineering","url":"https://liner.com/review/steering-knowledge-selection-behaviours-in-llms-via-saebased-representation-engineering"},{"title":"Steering Knowledge Selection Behaviours in LLMs via SAE-Based Representation Engineering","url":"https://arxiv.org/html/2410.15999v1"},{"title":"Steering Knowledge Selection Behaviours in LLMs via SAE-Based Representation Engineering - ACL Anthology","url":"https://aclanthology.org/2025.naacl-long.264/"},{"title":"Steering Knowledge Selection Behaviours in LLMs via SAE-Based Representation Engineering | AI Research Paper Details","url":"https://www.aimodels.fyi/papers/arxiv/steering-knowledge-selection-behaviours-llms-via-sae"},{"title":"[Literature Review] Steering Knowledge Selection Behaviours in LLMs via SAE-Based Representation Engineering","url":"https://www.themoonlight.io/en/review/steering-knowledge-selection-behaviours-in-llms-via-sae-based-representation-engineering"},{"title":"[2410.15999] Steering Knowledge Selection Behaviours in LLMs via SAE-Based Representation Engineering","url":"https://arxiv.org/abs/2410.15999"},{"title":"Steering Knowledge Selection Behaviours in LLMs via ...","url":"https://aclanthology.org/2025.naacl-long.264.pdf"},{"title":"Paper page - Steering Knowledge Selection Behaviours in LLMs via SAE-Based Representation Engineering","url":"https://huggingface.co/papers/2410.15999"}]

Based on the search results, I found information about the paper "Steering Knowledge Selection Behaviours in LLMs via SAE-Based Representation Engineering":

The paper proposes SpARE, a training-free representation engineering method that uses pre-trained sparse auto-encoders (SAEs) to control the knowledge selection behaviour of LLMs. SpARE identifies the functional features that control the knowledge selection behaviours and applies them to edit the internal activations of LLMs at inference time, effectively controlling the usage of either knowledge source to resolve knowledge conflict in open-domain question-answering tasks, surpassing existing representation engineering methods (+10%) as well as contrastive decoding methods (+15%).

The paper investigates how large language models (LLMs) can control the selection between parametric knowledge (knowledge stored within the model) and contextual knowledge (knowledge provided in real-time prompts), with the authors introducing SPARE to resolve knowledge conflicts that arise when the model's inherent knowledge contradicts the context provided.

The paper was published at NAACL 2025 and is authored by Yu Zhao and colleagues. The work addresses the problem of knowledge conflicts in large language models and proposes a practical solution using sparse auto-encoders for steering LLM behavior during inference.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "7c1da496-9f26-4686-a2f8-c14e02419195",
  "isSidechain": true,
  "promptId": "eee12e6f-4b22-4cb0-adff-def0ae050a12",
  "agentId": "ad05b8d9866c10448",
  "type": "user",
  "uuid": "362da14e-175e-453d-8ca1-526078bc6620",
  "sourceToolAssistantUUID": "7c1da496-9f26-4686-a2f8-c14e02419195",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "94d88260-dbbe-43d4-abc2-f8f5a7fda9d7",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 31 · 2026-05-30T06:20:40.357Z_

<details><summary>↩ Tool result · `toolu_01Vm1hUdfNE31XTpRqREBw3R`</summary>

```text
# Review Analysis: SPARE - SAE-Based Representation Engineering

Based on the available content, this page is a **Quick Review summary** rather than a traditional peer review with explicit strengths/weaknesses sections. Here's what was extracted:

## Available Content Structure

The review covers:
- **Motivation & Objective**
- **Proposed Method**
- **Experimental Results** (with 7 research questions)
- **Related Papers/Citation Network**

## Key Findings Presented

**Performance Highlights:**
The paper demonstrates that SPARE "achieves up to a 10% higher EM score compared to these methods" (TaskVec, ActAdd, SEA) and shows "up to a 15% improvement in EM scores" versus contrastive decoding approaches.

**Method Strengths Implied:**
- Training-free approach using pre-trained SAEs
- Outperforms multiple baseline categories (representation engineering, contrastive decoding, in-context learning)
- Effective at mid-layer intervention
- All components deemed critical through ablation studies

## Limitations of Available Content

**No explicit review sections found for:**
- Formal strengths/weaknesses assessments
- Reviewer criticisms or concerns
- Numerical quality scores
- Direct reviewer commentary
- Identified limitations or future work

This appears to be an **automated summary** rather than a detailed human peer review, as noted: *"This review was created with AI, and reviewed by a human editor."*
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "364af677-bdcb-43f0-8e41-78376b61e444",
  "isSidechain": true,
  "promptId": "eee12e6f-4b22-4cb0-adff-def0ae050a12",
  "agentId": "ad05b8d9866c10448",
  "type": "user",
  "uuid": "8020fffb-3041-468f-8af9-9b123cc65322",
  "sourceToolAssistantUUID": "364af677-bdcb-43f0-8e41-78376b61e444",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "94d88260-dbbe-43d4-abc2-f8f5a7fda9d7",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 32 · 2026-05-30T06:20:42.840Z_

Let me get the full paper content that was saved, search for the OpenReview forum directly, and look for the blog review with more details.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8020fffb-3041-468f-8af9-9b123cc65322",
  "isSidechain": true,
  "agentId": "ad05b8d9866c10448",
  "requestId": "req_011CbYGcFbR5ow22Kc2e7oH3",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "8807d064-dd7f-4e3e-9ea9-a398b6836195",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "94d88260-dbbe-43d4-abc2-f8f5a7fda9d7",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XUsFstXKY5XepmmHjuV8JY",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 730,
      "cache_creation_input_tokens": 3339,
      "cache_read_input_tokens": 15256,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3339,
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

_source line 33 · 2026-05-30T06:20:43.842Z_

<details open><summary>🔧 Tool call — Read · `toolu_019QBKjexpxasUwYpQuxK58o`</summary>

```json
{
  "file_path": "/home/ubuntu/.claude-account-2/projects/-home-ubuntu-idea-adversarial/94d88260-dbbe-43d4-abc2-f8f5a7fda9d7/tool-results/toolu_014TM8Ga7wmGWtEpyBawBT72.txt",
  "limit": 300
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8807d064-dd7f-4e3e-9ea9-a398b6836195",
  "isSidechain": true,
  "agentId": "ad05b8d9866c10448",
  "requestId": "req_011CbYGcFbR5ow22Kc2e7oH3",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "18552580-ce97-40d7-8a8d-ec909441aa06",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "94d88260-dbbe-43d4-abc2-f8f5a7fda9d7",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XUsFstXKY5XepmmHjuV8JY",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 730,
      "cache_creation_input_tokens": 3339,
      "cache_read_input_tokens": 15256,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3339,
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

_source line 34 · 2026-05-30T06:20:43.882Z_

<details><summary>↩ Tool result · `toolu_019QBKjexpxasUwYpQuxK58o`</summary>

```text
1	Title: Steering Knowledge Selection Behaviours in LLMs via SAE-Based Representation Engineering
2	
3	URL Source: https://arxiv.org/html/2410.15999
4	
5	Published Time: Tue, 11 Feb 2025 02:00:40 GMT
6	
7	Markdown Content:
8	 Abstract
9	1Introduction
10	2Background
11	3Detection of Knowledge Conflicts
12	4Resolving Knowledge Conflicts by Representation Engineering
13	5Experimental Results
14	6Analysis and Discussion
15	7Related Works
16	8Conclusions
17	 References
18	Steering Knowledge Selection Behaviours in LLMs via SAE-Based Representation Engineering
19	Yu Zhao1 Alessio Devoto3 Giwon Hong1 Xiaotang Du1 Aryo Pradipta Gema1
20	Hongru Wang2 Xuanli He4 Kam-Fai Wong2 Pasquale Minervini1,5
21	1University of Edinburgh  2The Chinese University of Hong Kong
22	3Sapienza University of Rome  4University College London  5Miniml.AI
23	{yu.zhao, p.minervini}@ed.ac.uk
24	\faGithub  https://github.com/yuzhaouoe/SAE-based-representation-engineering
25	Abstract
26	
27	Large language models (LLMs) can store a significant amount of factual knowledge in their parameters. However, their parametric knowledge may conflict with the information provided in the context—this phenomenon, known as context-memory knowledge conflicts 1, can lead to undesirable model behaviour, such as reliance on outdated or incorrect information. Analysing the internal activations of LLMs, we find that they can internally register the signals of knowledge conflict at mid-layers. Such signals allow us to detect whether a knowledge conflict occurs and use inference-time intervention strategies to resolve it. In this work, we propose SpARE, a training-free representation engineering method that uses pre-trained sparse auto-encoders (SAEs) to control the knowledge selection behaviour of LLMs. SpARE identifies the functional features that control the knowledge selection behaviours and applies them to edit the internal activations of LLMs at inference time. Our experimental results show that SpARE can effectively control the usage of either knowledge source to resolve knowledge conflict in open-domain question-answering tasks, surpassing existing representation engineering methods (
28	+
29	10
30	%
31	) as well as contrastive decoding methods (
32	+
33	15
34	%
35	).
36	
37	Steering Knowledge Selection Behaviours in LLMs
38	via SAE-Based Representation Engineering
39	
40	
41	
42	
43	Yu Zhao1 Alessio Devoto3 Giwon Hong1 Xiaotang Du1 Aryo Pradipta Gema1
44	Hongru Wang2 Xuanli He4 Kam-Fai Wong2 Pasquale Minervini1,5
45	1University of Edinburgh  2The Chinese University of Hong Kong
46	3Sapienza University of Rome  4University College London  5Miniml.AI
47	{yu.zhao, p.minervini}@ed.ac.uk
48	\faGithub  https://github.com/yuzhaouoe/SAE-based-representation-engineering
49	
50	
51	
52	1Introduction
53	Figure 1: In the event of a knowledge conflict, the model can rely on the context or on the parametric knowledge. The figure presents the predictions of Llama2-7B steered by SpARE.
54	
55	Large language models (LLMs) have shown remarkable capability to memorise factual knowledge and solve knowledge-intensive tasks (Petroni et al., 2019; Brown, 2020; Touvron et al., 2023; Jiang et al., 2023; Anil et al., 2023). Nevertheless, the knowledge stored in their parameters (parametric knowledge) can be inaccurate or outdated (Xu et al., 2024). To alleviate this issue, retrieval and tool-augmented approaches have been widely adopted to provide LLMs with external knowledge (contextual knowledge) (Karpukhin et al., 2020; Lewis et al., 2020; Wu et al., 2022; Schick et al., 2024). However, contextual knowledge may sometimes conflict with the parametric knowledge of the model, leading to what we refer to as knowledge conflicts. Such conflicts can cause undesired behaviour, where the model may rely on inaccurate information sources, resulting in incorrect outputs (Mallen et al., 2023; Xie et al., 2024a; Su et al., 2024; Wang et al., 2023; Zhao et al., 2024a).
56	
57	Prior research found that LLMs tend to prefer contextual knowledge (e.g., retrieved passages) over their parametric knowledge when conflicts occur (Su et al., 2024; Xie et al., 2024a; Hong et al., 2024). For instance, Su et al. (2024) show that most LLMs choose parametric knowledge in less than 
58	10
59	%
60	 examples. However, in more general applications, LLMs should retain the ability to use their parametric knowledge when presented with misinformation (Chen and Shu, 2023b, a; Zou et al., 2024; Mallen et al., 2023; Zhong et al., 2023). Existing works investigate fine-tuning and prompting-based strategies to detect and resolve knowledge conflicts (Wang et al., 2023); however, they need additional interactions with the model, e.g., by asking the LLMs to examine the conflicts sentence by sentence, resulting in high latency times and preventing practical applications.
61	
62	In this work, we investigate representation engineering methods to efficiently steer the usage of parametric and contextual knowledge of LLMs at inference time. Although representation engineering has provided an efficient and transparent framework for controlling the behaviour of LLMs, we find that existing methods fail to effectively steer knowledge usage. This may be because these methods directly modify the internal activations of LLMs, such as hidden states (Turner et al., 2023a; Zou et al., 2023a) or MLP activations (Qiu et al., 2024; Meng et al., 2022). These activations are polysemantic dense vectors that overlap with many independent semantic features (Olah, 2023). Thus, minor edits in one dimension can influence multiple semantic features, making it difficult to adjust activations accurately without affecting other features in practice.
63	
64	Recently, sparse auto-encoders (SAEs) have been proposed to address the difficulty of interpreting polysemantic activations by decomposing them into a large-scale monosemantic feature dictionary (Huben et al., 2024; Gao et al., 2024; Templeton et al., 2024a). Therefore, we introduce SAEs as a tool for precise activation editing to guide the knowledge selection of LLMs. Specifically, we propose SpARE, a Sparse Auto-Encoder-based Representation Engineering method to steer the knowledge selection behavior of LLMs. SpARE first identifies the SAE activations that are related to specific knowledge selection behaviours (Section 4.2); then, it extracts functional features that control the usage of contextual and parametric knowledge, and finally applies them to steer the behaviour of the model (Section 4.3).
65	
66	Our experimental results on open-domain question-answering tasks show that SpARE effectively controls the knowledge selection behaviours by utilising a small set of SAE features, e.g., less than 
67	0.05
68	%
69	 SAE activations for Gemma2-9B in the 
70	6
71	 layers2. SpARE yields more accurate results than state-of-the-art representation engineering methods (
72	+
73	10
74	%
75	), contrastive decoding (
76	+
77	15
78	%
79	), and in-context learning (
80	+
81	7
82	%
83	), achieving the best performance on steering knowledge selection behaviours of LLMs under knowledge conflicts.
84	
85	2Background
86	Problem Setup
87	
88	Following Longpre et al. (2021); Hong et al. (2024); Xie et al. (2024a), we use open-domain question-answering (ODQA) tasks to investigate the behaviour of LLMs when there is a conflict between the parametric knowledge of the model and contextual knowledge. In ODQA datasets with knowledge conflicts, each instance is presented as 
89	(
90	𝑄
91	,
92	𝐸
93	𝑀
94	,
95	𝑀
96	,
97	𝐸
98	𝐶
99	,
100	𝐶
101	)
102	, where 
103	𝑄
104	 is the question, 
105	𝐸
106	𝑀
107	 is the evidence that supports the memorised knowledge stored in the model parameters, 
108	𝐸
109	𝐶
110	 is the evidence that conflicts with the language model’s memorised knowledge, 
111	𝑀
112	 is the answer based on the 
113	𝐸
114	𝑀
115	, and 
116	𝐶
117	 is the answer based on the 
118	𝐸
119	𝐶
120	.
121	
122	Sparse Auto-Encoders
123	
124	Recent works have proposed using sparse auto-encoders (SAEs) to interpret the complex representations of LLMs by decomposing them into a large set of monosemantic features Huben et al. (2024); Gao et al. (2024); Templeton et al. (2024a). Given an activation 
125	𝐡
126	∈
127	ℝ
128	𝑑
129	 from the residual stream of LLMs, a SAE with 
130	𝑛
131	 latent dimensions encodes it into a sparse vector 
132	𝐳
133	∈
134	ℝ
135	𝑛
136	 and decodes it to recover 
137	𝐡
138	:
139	
140			
141	𝑓
142	𝜃
143	⁢
144	(
145	𝐡
146	)
147	=
148	𝜎
149	⁢
150	(
151	𝐖
152	𝜃
153	⁢
154	(
155	𝐡
156	−
157	𝐛
158	)
159	+
160	𝐛
161	𝜃
162	)
163	=
164	𝐳
165	,
166			
167	(1)
168	
169			
170	𝑔
171	𝜙
172	⁢
173	(
174	𝐳
175	)
176	=
177	𝐖
178	𝜙
179	⁢
180	𝐳
181	=
182	∑
183	𝑖
184	=
185	1
186	𝑛
187	𝑧
188	𝑖
189	⁢
190	𝐟
191	𝑖
192	+
193	𝐛
194	=
195	𝐡
196	^
197		
198	
199	where 
200	𝜎
201	 is an activation function that outputs a non-negative value such as ReLU, 
202	𝐖
203	𝜃
204	∈
205	ℝ
206	𝑛
207	×
208	𝑑
209	, 
210	𝐛
211	∈
212	ℝ
213	𝑑
214	, 
215	𝐛
216	𝜃
217	∈
218	ℝ
219	𝑛
220	, 
221	𝐖
222	𝜙
223	∈
224	ℝ
225	𝑑
226	×
227	𝑛
228	, 
229	𝑧
230	𝑖
231	 is the 
232	𝑖
233	-th element of the SAE activation 
234	𝐳
235	, and 
236	𝐟
237	𝑖
238	∈
239	ℝ
240	𝑑
241	 is the 
242	𝑖
243	-th column of 
244	𝐖
245	𝜙
246	. The 
247	{
248	𝐟
249	𝑖
250	}
251	𝑖
252	=
253	1
254	𝑛
255	 learned through the SAE are considered highly monosemantic, and the SAE activation 
256	𝐳
257	 indicates the activated values of 
258	{
259	𝐟
260	𝑖
261	}
262	𝑖
263	=
264	1
265	𝑛
266	.
267	
268	3Detection of Knowledge Conflicts
269	
270	In this section, we investigate whether we can detect the occurrence of conflicts during the generation process, since identifying such conflicts is a prerequisite for exploring inference-time strategies to control the LLM.
271	
272	We focus on the residual stream (Elhage et al., 2021) of the model and look for a signal of knowledge conflict. To this end, we create two groups of input instances, 
273	𝒟
274	𝐸
275	𝑀
276	 
277	=
278	{
279	(
280	𝑄
281	,
282	𝐸
283	𝑀
284	)
285	}
286	 and 
287	𝒟
288	𝐸
289	𝐶
290	 
291	=
292	{
293	(
294	𝑄
295	,
296	𝐸
297	𝐶
298	)
299	}
300	. In 
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "18552580-ce97-40d7-8a8d-ec909441aa06",
  "isSidechain": true,
  "promptId": "eee12e6f-4b22-4cb0-adff-def0ae050a12",
  "agentId": "ad05b8d9866c10448",
  "type": "user",
  "uuid": "8dc909d8-900c-419d-858d-5d17b68bf6dd",
  "sourceToolAssistantUUID": "18552580-ce97-40d7-8a8d-ec909441aa06",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "94d88260-dbbe-43d4-abc2-f8f5a7fda9d7",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 35 · 2026-05-30T06:20:46.248Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_015tThhLGF4qQ7veei6ZqTgo`</summary>

```json
{
  "url": "https://www.themoonlight.io/en/review/steering-knowledge-selection-behaviours-in-llms-via-sae-based-representation-engineering",
  "prompt": "Extract ALL review content: strengths, weaknesses, criticisms, praise, scores, questions from reviewers, detailed assessment. Provide full text of all review sections."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8dc909d8-900c-419d-858d-5d17b68bf6dd",
  "isSidechain": true,
  "agentId": "ad05b8d9866c10448",
  "requestId": "req_011CbYGcFbR5ow22Kc2e7oH3",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "dc2a2e9e-7d18-46f0-b80d-829bf2649fa1",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "94d88260-dbbe-43d4-abc2-f8f5a7fda9d7",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XUsFstXKY5XepmmHjuV8JY",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 730,
      "cache_creation_input_tokens": 3339,
      "cache_read_input_tokens": 15256,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3339,
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

_source line 36 · 2026-05-30T06:20:46.711Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01SZe5kFCEVjiyowSVR32tfY`</summary>

```json
{
  "query": "site:openreview.net \"Steering Knowledge Selection\" OR \"SpARE\" OR \"SAE-Based Representation\" Yu Zhao"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "dc2a2e9e-7d18-46f0-b80d-829bf2649fa1",
  "isSidechain": true,
  "agentId": "ad05b8d9866c10448",
  "requestId": "req_011CbYGcFbR5ow22Kc2e7oH3",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "f325cf69-ed83-4fd8-9c7a-586bf7b6134f",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "94d88260-dbbe-43d4-abc2-f8f5a7fda9d7",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XUsFstXKY5XepmmHjuV8JY",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 730,
      "cache_creation_input_tokens": 3339,
      "cache_read_input_tokens": 15256,
      "output_tokens": 366,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 3339
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 730,
          "output_tokens": 366,
          "cache_read_input_tokens": 15256,
          "cache_creation_input_tokens": 3339,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 3339,
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

_source line 37 · 2026-05-30T06:20:50.359Z_

<details><summary>↩ Tool result · `toolu_015tThhLGF4qQ7veei6ZqTgo`</summary>

```text
# Response

Based on my review of the provided content, **no peer review sections were found**. The webpage is a summary/overview of the paper "Steering Knowledge Selection Behaviours in LLMs via SAE-Based Representation Engineering" created by Moonlight (an AI research tool), not a peer-reviewed publication or review document.

The page contains:
- A literature review summary of the paper's methodology
- Overview of key concepts
- Core methodology breakdown
- Experimental results summary
- Conclusions and limitations sections

**These are descriptive summaries, not critical peer reviews.** There are no reviewer comments, scores, criticisms, praise, or detailed assessments from academic reviewers present in this content.

To access actual peer review content, you would need to consult the original publication venue (conference proceedings, journal, or preprint server) where this paper was submitted for formal peer review.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "dc2a2e9e-7d18-46f0-b80d-829bf2649fa1",
  "isSidechain": true,
  "promptId": "eee12e6f-4b22-4cb0-adff-def0ae050a12",
  "agentId": "ad05b8d9866c10448",
  "type": "user",
  "uuid": "5647a40e-7a42-439a-a6cd-0792e4afbc9b",
  "sourceToolAssistantUUID": "dc2a2e9e-7d18-46f0-b80d-829bf2649fa1",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "94d88260-dbbe-43d4-abc2-f8f5a7fda9d7",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 38 · 2026-05-30T06:20:55.104Z_

<details><summary>↩ Tool result · `toolu_01SZe5kFCEVjiyowSVR32tfY`</summary>

```text
Web search results for query: "site:openreview.net "Steering Knowledge Selection" OR "SpARE" OR "SAE-Based Representation" Yu Zhao"

Links: [{"title":"Steering Large Language Model Activations in Sparse ...","url":"https://openreview.net/pdf/70f3af98996906bfa9bd84ba645f0cf45176844a.pdf"},{"title":"Steering Knowledge Selection Behaviours in LLMs via SAE-Based   Representation Engineering","url":"https://arxiv.org/pdf/2410.15999"},{"title":"000 001 002 003 004 005 006 007 008 009 010 011 012 013 014 015 016 017 018 019","url":"https://openreview.net/pdf/8fe1619ca5452f80fddd11dec1d1665ab3d5a717.pdf"},{"title":"Beyond Prompt Engineering: Robust Behavior Control in LLMs via Steering Target Atoms","url":"https://arxiv.org/pdf/2505.20322"},{"title":"SAE-SSV: Supervised Steering in Sparse Representation Spaces for Reliable Control of Language Models","url":"https://arxiv.org/pdf/2505.16188"}]

The search found relevant results about the paper on OpenReview. Here's what I found:

The paper "Steering Knowledge Selection Behaviours in LLMs via SAE-Based Representation Engineering" is authored by Yu Zhao and colleagues from institutions including the University of Edinburgh, The Chinese University of Hong Kong, Sapienza University of Rome, University College London, and Miniml.AI.

The paper proposes SPARE, a training-free representation engineering method that uses pre-trained sparse auto-encoders (SAEs) to control the knowledge selection behavior of LLMs by identifying functional features that control knowledge selection behaviors and applying them to edit the internal activations of LLMs at inference time.

The work addresses context-memory knowledge conflicts where LLMs' parametric knowledge may conflict with context information, and uses inference-time intervention strategies to resolve these conflicts.

The paper is available on both OpenReview and arXiv, with the GitHub repository linked at the project page.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f325cf69-ed83-4fd8-9c7a-586bf7b6134f",
  "isSidechain": true,
  "promptId": "eee12e6f-4b22-4cb0-adff-def0ae050a12",
  "agentId": "ad05b8d9866c10448",
  "type": "user",
  "uuid": "2d58b541-cd4f-46f8-ae07-66ea32b1c7ba",
  "sourceToolAssistantUUID": "f325cf69-ed83-4fd8-9c7a-586bf7b6134f",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "94d88260-dbbe-43d4-abc2-f8f5a7fda9d7",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 39 · 2026-05-30T06:20:57.146Z_

Let me continue reading the paper and try to access the OpenReview forum for actual reviews.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2d58b541-cd4f-46f8-ae07-66ea32b1c7ba",
  "isSidechain": true,
  "agentId": "ad05b8d9866c10448",
  "requestId": "req_011CbYGdLeoLtJ5rV5nEvhAZ",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "9a1d6efc-5de4-4c87-b910-5d7893882c2e",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "94d88260-dbbe-43d4-abc2-f8f5a7fda9d7",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BUedv4qj3VTd5EcJQTG4cG",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5484,
      "cache_read_input_tokens": 18595,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 5484,
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

_source line 40 · 2026-05-30T06:21:01.907Z_

<details open><summary>🔧 Tool call — Read · `toolu_01DGSJifMwrz2UetPWZAZJwX`</summary>

```json
{
  "file_path": "/home/ubuntu/.claude-account-2/projects/-home-ubuntu-idea-adversarial/94d88260-dbbe-43d4-abc2-f8f5a7fda9d7/tool-results/toolu_014TM8Ga7wmGWtEpyBawBT72.txt",
  "offset": 300,
  "limit": 400
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9a1d6efc-5de4-4c87-b910-5d7893882c2e",
  "isSidechain": true,
  "agentId": "ad05b8d9866c10448",
  "requestId": "req_011CbYGdLeoLtJ5rV5nEvhAZ",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "a55262d9-337d-4240-bc81-f3b1061cce53",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "94d88260-dbbe-43d4-abc2-f8f5a7fda9d7",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BUedv4qj3VTd5EcJQTG4cG",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5484,
      "cache_read_input_tokens": 18595,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 5484,
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

### Tool result

_source line 41 · 2026-05-30T06:21:01.934Z_

<details><summary>↩ Tool result · `toolu_01DGSJifMwrz2UetPWZAZJwX`</summary>

```text
300	. In 
301	𝒟
302	𝐸
303	𝑀
304	, the model is provided with a context that is coherent with the model internal memorized knowledge, whereas in 
305	𝒟
306	𝐸
307	𝐶
308	 the model is provided with a context that does not agree with model parametric knowledge, thus causing a knowledge conflict. To determine whether a signal of conflict arises in the residual stream, we focus on the last position of the sequence during generation, which is supposed to encode the information to predict the first token of the answer.
309	
310	We apply a linear probing method (Conneau et al., 2018; Zhu and Li, 2023; Allen-Zhu and Li, 2023) to investigate whether the residual stream contains a signal of knowledge conflict. Specifically, we train logistic regression models to classify whether a given activation (the hidden state, MLP or Self-Attention activations) is from the 
311	𝒟
312	𝐸
313	𝐶
314	 or 
315	𝒟
316	𝐸
317	𝑀
318	, i.e. whether it contains a knowledge conflict or not. We use activations from each layer as input and formulate this as a binary classification task. The evaluation is conducted on a held-out test set. We present probing results on Llama2-7B (Touvron et al., 2023) and Gemma2-9B (Rivière et al., 2024) using AUROC as metric in Fig. 2. We observe that the probing accuracy increases from the first layer to the middle layers, and this trend is the same across different types of activations. This indicates that we can detect the signal of knowledge conflict in the residual stream of the mid-layers. The probing accuracy decreases in the later layers, especially for MLP and Self-Attention activations, which indicates that MLP and Self-Attention modules do not further add the signal of conflicting knowledge to the residual stream. We provide more details and analysis about knowledge conflict detection in Appendix A and Zhao et al. (2024b).
319	
320	The above analysis shows that knowledge conflicts can be identified in the internal states of LLMs. Moreover, it provides insight into which layers can be more influential in the knowledge selection (Section 6.1).
321	
322	(a)Llama2-7B
323	(b)Gemma2-9B
324	Figure 2:The knowledge conflict probing results of Llama2-7B and Gemma2-9B on NQSwap (Longpre et al., 2021). The probing results on hidden states, MLP and Self-Attention activations are coloured differently.
325	4Resolving Knowledge Conflicts by Representation Engineering
326	
327	In this section, we introduce SpARE, our SAE-based representation engineering method, to steer the usage of parametric and contextual knowledge to generate the answers. SpARE consists of the three following steps: 1) collecting activations that lead to different knowledge selection behaviours (Section 4.1); 2) identifying SAE activations that are related to each knowledge selection behaviour (Section 4.2); 3) steering the usage of either knowledge source by editing the hidden states of LLMs at inference time (Section 4.3).
328	
329	4.1Collecting Activations with Different Knowledge Selection Behaviours
330	
331	We showed in Section 3 that we can detect the knowledge conflict by probing the residual stream. We now want to characterise the activations that lead to different knowledge selection behaviours. To this end, given a set of instances 
332	𝒟
333	𝐸
334	𝐶
335	 that cause a knowledge conflict, we separate it into two groups based on the model’s predictions: 
336	𝒟
337	𝐶
338	, where the model generates an answer that aligns with the context, and 
339	𝒟
340	𝑀
341	, where the model ignores the context and generates an answer relying on the parametric knowledge. These two subsets characterise two knowledge selection behaviours of the model. In the following, we omit the notation to specify the layer of 
342	𝐡
343	 and 
344	𝐳
345	 for simplicity, as the method can be applied to arbitrary layers. We collect the hidden state at the last position of the input that is used to generate the first token of the answer.
346	
347	We collect the hidden states from 
348	𝒟
349	𝐶
350	 and 
351	𝒟
352	𝑀
353	 for 
354	𝑁
355	 samples, denoting them as 
356	{
357	𝐡
358	𝐶
359	𝑗
360	}
361	𝑗
362	=
363	1
364	𝑁
365	 and 
366	{
367	𝐡
368	𝑀
369	𝑗
370	}
371	𝑗
372	=
373	1
374	𝑁
375	, respectively. We then obtain the SAE activation for each sample by 
376	𝐳
377	𝐶
378	𝑗
379	=
380	𝑓
381	𝜃
382	⁢
383	(
384	𝐡
385	𝐶
386	𝑗
387	)
388	 and 
389	𝐳
390	𝑀
391	𝑗
392	=
393	𝑓
394	𝜃
395	⁢
396	(
397	𝐡
398	𝑀
399	𝑗
400	)
401	. Finally, we compute the average of the sets 
402	{
403	𝐳
404	𝐶
405	𝑗
406	}
407	𝑗
408	=
409	1
410	𝑁
411	 and 
412	{
413	𝐳
414	𝑀
415	𝑗
416	}
417	𝑗
418	=
419	1
420	𝑁
421	 to obtain the mean vectors 
422	𝐳
423	𝐶
424	¯
425	 and 
426	𝐳
427	𝑀
428	¯
429	, respectively. More details are presented in Section C.1 and Section C.3.
430	
431	At this stage, 
432	𝐳
433	𝐶
434	¯
435	 and 
436	𝐳
437	𝑀
438	¯
439	 contain the information to steer the generation towards 
440	𝐶
441	 or 
442	𝑀
443	. However, there might still be instance-specific activations with non-zero values that are not responsible for the knowledge selection behaviour. In the next section, we identify functional activations related to knowledge selection behaviours and then construct two orthogonal SAE activations, 
444	𝐳
445	𝐶
446	 and 
447	𝐳
448	𝑀
449	 for steering the knowledge selection behaviours.
450	
451	Figure 3: The workflow of SpARE steers the knowledge selection behaviour. The figure presents an example of steering the model to use parametric knowledge. First, the SAE encoder 
452	𝑓
453	𝜃
454	 encodes hidden state 
455	𝐡
456	 into the SAE activation 
457	𝐳
458	. Then, it determines the values of SAE activations 
459	𝐳
460	−
461	 and 
462	𝐳
463	+
464	 for editing (Eq. 2 and Eq. 3). Finally, we edit the hidden state using the features extracted from the SAE decoder 
465	𝑔
466	𝜙
467	 (Eq. 4).
468	4.2Identifying Functional SAE Activations
469	
470	As shown by previous works (Gao et al., 2024; Templeton et al., 2024a), a single SAE activation can capture one monosemantic feature. In this work, we hypothesise a combination of a small set of SAE activations can be responsible for a functional feature, such as knowledge selection in case of conflict. Our hypothesis is motivated by Task Vector (Hendel et al., 2023; Todd et al., 2024), which shows that hidden states contain the functional information that drives a task.
471	
472	We now show how we find the SAE activations that are responsible for driving the knowledge selection. First, we calculate mutual information between each SAE activation and the knowledge selection behaviours, which measures to which extent the behaviour depends on each activation. Let the random variable 
473	𝑍
474	𝑖
475	 be the 
476	𝑖
477	th activation of SAE, and 
478	𝑌
479	=
480	{
481	𝐶
482	,
483	𝑀
484	}
485	 be the generated answers; we calculate the mutual information 
486	𝐼
487	⁢
488	(
489	𝑍
490	𝑖
491	;
492	𝑌
493	)
494	 between them. A higher 
495	𝐼
496	⁢
497	(
498	𝑍
499	𝑖
500	;
501	𝑌
502	)
503	 indicates a higher dependency between 
504	𝑍
505	𝑖
506	 and the knowledge selection behaviour. We then select the top-
507	𝑘
508	 activations with the highest 
509	𝐼
510	⁢
511	(
512	𝑍
513	𝑖
514	;
515	𝑌
516	)
517	, denoted as 
518	𝒵
519	. More details are available in Section C.2
520	
521	In the following, we determine which knowledge selection behaviour each 
522	𝑍
523	𝑖
524	∈
525	𝒵
526	 positively correlates with. Given the sets of activations 
527	{
528	𝐳
529	𝐶
530	𝑗
531	}
532	𝑗
533	=
534	1
535	𝑁
536	 and 
537	{
538	𝐳
539	𝑀
540	𝑗
541	}
542	𝑗
543	=
544	1
545	𝑁
546	, we estimate the expected value of each activation feature 
547	𝑍
548	𝑖
549	∈
550	𝒵
551	 in both sets, denoted as 
552	𝔼
553	𝐶
554	⁢
555	[
556	𝑍
557	𝑖
558	]
559	 and 
560	𝔼
561	𝑀
562	⁢
563	[
564	𝑍
565	𝑖
566	]
567	. We then have that 
568	𝑍
569	𝑖
570	 is positively correlated with the behaviour of selecting contextual knowledge if 
571	𝔼
572	𝐶
573	⁢
574	[
575	𝑍
576	𝑖
577	]
578	−
579	𝔼
580	𝑀
581	⁢
582	[
583	𝑍
584	𝑖
585	]
586	>
587	0
588	. Conversely, if this condition is not met, 
589	𝑍
590	𝑖
591	 is positively correlated with the behaviour of selecting parametric knowledge. Finally, we construct two functional SAE activations 
592	𝐳
593	𝐶
594	 and 
595	𝐳
596	𝑀
597	∈
598	ℝ
599	𝑛
600	, that steer the usage of contextual and parametric knowledge, respectively. For each element, 
601	𝑧
602	𝐶
603	⁢
604	𝑖
605	 and 
606	𝑧
607	𝑀
608	⁢
609	𝑖
610	 are set to 
611	0
612	 if 
613	𝑍
614	𝑖
615	∉
616	𝒵
617	, and the remaining values are taken from 
618	𝐳
619	𝐶
620	¯
621	 and 
622	𝐳
623	𝑀
624	¯
625	 based on their expectations:
626	
627		
628	𝑧
629	𝐶
630	⁢
631	𝑖
632	=
633		
634	{
635	𝑧
636	𝐶
637	¯
638	𝑖
639	,
640		
641	 if 
642	⁢
643	𝔼
644	𝐶
645	⁢
646	[
647	𝑍
648	𝑖
649	]
650	−
651	𝔼
652	𝑀
653	⁢
654	[
655	𝑍
656	𝑖
657	]
658	>
659	0
660	
661	
662	0
663	,
664		
665	otherwise
666		
667		
668	𝑧
669	𝑀
670	⁢
671	𝑖
672	=
673		
674	{
675	𝑧
676	𝑀
677	¯
678	𝑖
679	,
680		
681	 if 
682	⁢
683	𝔼
684	𝐶
685	⁢
686	[
687	𝑍
688	𝑖
689	]
690	−
691	𝔼
692	𝑀
693	⁢
694	[
695	𝑍
696	𝑖
697	]
698	<
699	0
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a55262d9-337d-4240-bc81-f3b1061cce53",
  "isSidechain": true,
  "promptId": "eee12e6f-4b22-4cb0-adff-def0ae050a12",
  "agentId": "ad05b8d9866c10448",
  "type": "user",
  "uuid": "b5fb3698-bfb7-4068-9597-172ebfe459ec",
  "sourceToolAssistantUUID": "a55262d9-337d-4240-bc81-f3b1061cce53",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "94d88260-dbbe-43d4-abc2-f8f5a7fda9d7",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 42 · 2026-05-30T06:21:03.321Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01WrQptaEP4Y4zCRqknCzw7K`</summary>

```json
{
  "url": "https://openreview.net/pdf/70f3af98996906bfa9bd84ba645f0cf45176844a.pdf",
  "prompt": "Extract all content from this PDF. Is this the SpARE paper by Yu Zhao? What are the key details?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b5fb3698-bfb7-4068-9597-172ebfe459ec",
  "isSidechain": true,
  "agentId": "ad05b8d9866c10448",
  "requestId": "req_011CbYGdLeoLtJ5rV5nEvhAZ",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "bcd5052c-fbb0-4ac7-9fa7-a5b76f735d08",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "94d88260-dbbe-43d4-abc2-f8f5a7fda9d7",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BUedv4qj3VTd5EcJQTG4cG",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5484,
      "cache_read_input_tokens": 18595,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 5484,
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

_source line 43 · 2026-05-30T06:21:06.279Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Kw2imv44skTHVJaqJjgTLK`</summary>

```json
{
  "query": "openreview.net forum \"Steering Knowledge Selection Behaviours in LLMs\" reviews ratings"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "bcd5052c-fbb0-4ac7-9fa7-a5b76f735d08",
  "isSidechain": true,
  "agentId": "ad05b8d9866c10448",
  "requestId": "req_011CbYGdLeoLtJ5rV5nEvhAZ",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "1eed82f1-0fe4-4bb0-91db-14d55bf61f8b",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "94d88260-dbbe-43d4-abc2-f8f5a7fda9d7",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BUedv4qj3VTd5EcJQTG4cG",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5484,
      "cache_read_input_tokens": 18595,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 5484,
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

### Tool result

_source line 44 · 2026-05-30T06:21:10.827Z_

<details><summary>↩ Tool result · `toolu_01Kw2imv44skTHVJaqJjgTLK`</summary>

```text
Web search results for query: "openreview.net forum "Steering Knowledge Selection Behaviours in LLMs" reviews ratings"

Links: [{"title":"[Quick Review] Steering Knowledge Selection Behaviours in LLMs via SAE-Based Representation Engineering","url":"https://liner.com/review/steering-knowledge-selection-behaviours-in-llms-via-saebased-representation-engineering"},{"title":"Steering Knowledge Selection Behaviours in LLMs","url":"https://arxiv.org/pdf/2410.15999"},{"title":"Steering Knowledge Selection Behaviours in LLMs via SAE-Based Representation Engineering","url":"https://arxiv.org/html/2410.15999v1"},{"title":"[Literature Review] Steering Knowledge Selection Behaviours in LLMs via SAE-Based Representation Engineering","url":"https://www.themoonlight.io/en/review/steering-knowledge-selection-behaviours-in-llms-via-sae-based-representation-engineering"},{"title":"[2410.15999] Steering Knowledge Selection Behaviours in LLMs via SAE-Based Representation Engineering","url":"https://arxiv.org/abs/2410.15999"},{"title":"Steering Knowledge Selection Behaviours in LLMs via SAE-Based Representation Engineering","url":"https://www.rohan-paul.com/p/steering-knowledge-selection-behaviours"},{"title":"Steering Knowledge Selection Behaviours in LLMs via SAE-Based Representation Engineering - ACL Anthology","url":"https://aclanthology.org/2025.naacl-long.264/"}]

Based on the search results, I found information about the paper "Steering Knowledge Selection Behaviours in LLMs via SAE-Based Representation Engineering," but the results do not contain specific information about OpenReview.net forum reviews and ratings for this paper.

The search results show that this paper has been published and is available through multiple sources, including arXiv and the ACL Anthology. The paper was published in 2025 as part of the Conference of the Nations of the Americas Chapter of the Association for Computational Linguistics.

However, the search results do not include the actual OpenReview.net forum page with reviewer comments and ratings. To access the specific reviews and ratings you're looking for, you would need to visit the OpenReview.net website directly and search for the paper there, as that information is not captured in the available search results.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "1eed82f1-0fe4-4bb0-91db-14d55bf61f8b",
  "isSidechain": true,
  "promptId": "eee12e6f-4b22-4cb0-adff-def0ae050a12",
  "agentId": "ad05b8d9866c10448",
  "type": "user",
  "uuid": "751eb479-6c4f-4b99-9cba-a47efe0885aa",
  "sourceToolAssistantUUID": "1eed82f1-0fe4-4bb0-91db-14d55bf61f8b",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "94d88260-dbbe-43d4-abc2-f8f5a7fda9d7",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 45 · 2026-05-30T06:21:11.405Z_

<details><summary>↩ Tool result · `toolu_01WrQptaEP4Y4zCRqknCzw7K`</summary>

```text
I cannot extract meaningful content from this PDF document. The file appears to be a linearized PDF with compressed stream objects that require proper PDF parsing to decode.

Based on the technical structure visible (PDF version 1.5, stream objects with FlateDecode compression), this is a valid PDF file, but I cannot reliably determine:

1. **Whether this is the SpARE paper by Yu Zhao** - The document's readable metadata and content are not accessible to me in this raw format
2. **Key details** - The actual text content is encoded in compressed streams that I cannot properly decompress and render

To properly analyze this document, you would need to:
- Open it with a standard PDF reader (Adobe Reader, browser PDF viewer, etc.)
- Use PDF extraction tools
- Or provide the document in an alternative format (text, HTML, etc.)

If you can access the PDF directly, please check the title page and abstract to confirm authorship and topic. If you'd like me to analyze the SpARE paper, consider providing it in a more accessible format.

[Binary content (application/pdf, 3.9MB) also saved to /home/ubuntu/.claude-account-2/projects/-home-ubuntu-idea-adversarial/94d88260-dbbe-43d4-abc2-f8f5a7fda9d7/tool-results/webfetch-1780122064483-ahm7xc.pdf]
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "bcd5052c-fbb0-4ac7-9fa7-a5b76f735d08",
  "isSidechain": true,
  "promptId": "eee12e6f-4b22-4cb0-adff-def0ae050a12",
  "agentId": "ad05b8d9866c10448",
  "type": "user",
  "uuid": "986f73ee-a4d7-455b-bbcc-601c54ccba03",
  "sourceToolAssistantUUID": "bcd5052c-fbb0-4ac7-9fa7-a5b76f735d08",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "94d88260-dbbe-43d4-abc2-f8f5a7fda9d7",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 46 · 2026-05-30T06:21:13.895Z_

Let me continue reading the paper and try to find the OpenReview forum and the blog post with detailed analysis.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "986f73ee-a4d7-455b-bbcc-601c54ccba03",
  "isSidechain": true,
  "agentId": "ad05b8d9866c10448",
  "requestId": "req_011CbYGeYGaLtXyxMCNbp4s8",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "5ad56fd6-6836-40d5-bbfb-0422ab6fdc64",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "94d88260-dbbe-43d4-abc2-f8f5a7fda9d7",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018AnjP3ay9pjyr4Db2zEAZL",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 617,
      "cache_creation_input_tokens": 4512,
      "cache_read_input_tokens": 24079,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4512,
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

_source line 47 · 2026-05-30T06:21:16.309Z_

<details open><summary>🔧 Tool call — Read · `toolu_01XkTKMpBDVLVXmPwxRa8PK4`</summary>

```json
{
  "file_path": "/home/ubuntu/.claude-account-2/projects/-home-ubuntu-idea-adversarial/94d88260-dbbe-43d4-abc2-f8f5a7fda9d7/tool-results/toolu_014TM8Ga7wmGWtEpyBawBT72.txt",
  "offset": 700,
  "limit": 500
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5ad56fd6-6836-40d5-bbfb-0422ab6fdc64",
  "isSidechain": true,
  "agentId": "ad05b8d9866c10448",
  "requestId": "req_011CbYGeYGaLtXyxMCNbp4s8",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "0723daf2-0c02-4eb7-aa95-d7aedac921ef",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "94d88260-dbbe-43d4-abc2-f8f5a7fda9d7",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018AnjP3ay9pjyr4Db2zEAZL",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 617,
      "cache_creation_input_tokens": 4512,
      "cache_read_input_tokens": 24079,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4512,
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

_source line 48 · 2026-05-30T06:21:16.319Z_

<details><summary>↩ Tool result · `toolu_01XkTKMpBDVLVXmPwxRa8PK4`</summary>

```text
700	
701	
702	0
703	,
704		
705	otherwise
706		
707	4.3Editing Activations to Steer Behaviours
708	
709	In the following, we introduce how we utilise the functional activation 
710	𝐳
711	𝐶
712	 and 
713	𝐳
714	𝑀
715	 to control the usage of knowledge sources at inference time. Suppose we want to control the LLM to use its parametric knowledge and ignore the conflict contextual knowledge that might be misinformation. In this case, we aim to remove the features that steer the contextual knowledge usage and add the features that steer the parametric knowledge usage. To avoid removing or adding unnecessary features, we restrict the values to edit by the following two constraints. Let an activation be 
716	𝐡
717	 and corresponding SAE activations be 
718	𝐳
719	=
720	𝑓
721	𝜃
722	⁢
723	(
724	𝐡
725	)
726	. First, in Eq. 2, we determine the value we need to remove from 
727	𝑧
728	𝑖
729	 to avoid the undesired behaviour, i.e., generating contextual knowledge in this case. At this step, we ensure that the resulting activation remains non-negative after the removal, i.e., subtract at most 
730	𝑧
731	𝑖
732	 when 
733	𝑧
734	𝑖
735	<
736	𝑧
737	𝐶
738	⁢
739	𝑖
740	:
741	
742		
743	𝑧
744	𝑖
745	−
746	=
747	min
748	⁡
749	{
750	𝑧
751	𝑖
752	,
753	𝑧
754	𝐶
755	⁢
756	𝑖
757	}
758	.
759			
760	(2)
761	
762	Then, in Eq. 3, we determine the value we need to add to 
763	𝑧
764	𝑖
765	 to encourage the desired behaviour, i.e., generating parametric knowledge in this case. Here, we ensure that no excess value is added once the activation reaches 
766	𝑧
767	𝑀
768	⁢
769	𝑖
770	:
771	
772		
773	𝑧
774	𝑖
775	+
776	=
777	max
778	⁡
779	{
780	𝑧
781	𝑀
782	⁢
783	𝑖
784	−
785	𝑧
786	𝑖
787	,
788	0
789	}
790	.
791			
792	(3)
793	
794	Finally, we obtain the edited hidden states 
795	𝐡
796	′
797	 by:
798	
799		
800	𝐡
801	′
802	=
803	𝐡
804	+
805	𝛼
806	⁢
807	(
808	−
809	𝑔
810	𝜙
811	⁢
812	(
813	𝐳
814	−
815	)
816	+
817	𝑔
818	𝜙
819	⁢
820	(
821	𝐳
822	+
823	)
824	)
825	,
826			
827	(4)
828	
829	where 
830	𝛼
831	∈
832	ℝ
833	+
834	 is a user-defined hyperparameter that controls the degree of editing. Note that we do not directly edit the activation 
835	𝐳
836	 of hidden state 
837	𝐡
838	 to obtain the modified hidden states by 
839	𝐡
840	′
841	=
842	𝑔
843	𝜙
844	⁢
845	(
846	𝐳
847	′
848	)
849	 with 
850	𝐳
851	′
852	=
853	𝐳
854	−
855	𝐳
856	−
857	+
858	𝐳
859	+
860	 for two reasons: 1) it can result in unexpected information loss of original 
861	𝐡
862	 due to the reconstruction loss of the SAE, leading to a nearly zero accuracy in our experiments; 2) the definition of the SAE activation shown in Eq. 1 requires each element of 
863	𝐳
864	 be a non-negative value, which prevents us from using 
865	𝛼
866	 to flexibly control the strengthen of editing like Eq. 4.
867	
868	Similarly, if we want to control the model to be faithful to the context in the case of the contextual knowledge is more likely correct, we can swap 
869	𝑧
870	𝐶
871	⁢
872	𝑖
873	 and 
874	𝑧
875	𝑀
876	⁢
877	𝑖
878	 in Eq. 2 and Eq. 3. In this work, we only edit hidden states at the last position of the input for ODQA tasks.
879	
880	5Experimental Results
881	5.1Settings
882	Datasets
883	
884	We use two widely adopted open-domain question-answering datasets with knowledge conflicts NQSwap (Longpre et al., 2021) and Macnoise (Hong et al., 2024) to investigate the controlling capability of several methods.
885	
886	Models
887	
888	We evaluate our method using Llama3-8B (Dubey et al., 2024) and Gemma2-9B (Rivière et al., 2024), which have corresponding public pre-trained SAEs. Moreover, we also evaluate our method using Llama2-7B (Touvron et al., 2023) with our pre-trained SAEs to examine the feasibility of adopting SpARE to an LLM without public SAEs. More details are presented in Appendix B.
889	
890	Evaluation
891	
892	We use the greedy decoding method to evaluate the LLMs in an open-ended generation setting. We use 
893	3
894	 in-context demonstrations to align the answer format. The demonstrations use non-conflict evidence 
895	𝐸
896	𝑀
897	 and memorised answer 
898	𝑀
899	, so they do not point out which knowledge source to select. More details are presented in Section C.4. The test examples use 
900	𝐸
901	𝐶
902	, leading to a knowledge conflict for LLMs, and a behaviour-controlling method needs to steer the usage of either parametric or contextual knowledge to generate the answer. We compare the evaluation results under control with the results without any control to show each method’s controlling capability.
903	
904	Metric	Method	NQSwap (Longpre et al., 2021)	Macnoise (Hong et al., 2024)
905	Llama3-8B	Llama2-7B	Gemma-2-9B	Llama3-8B	Llama2-7B	Gemma-2-9B
906	Steer to Use Parametric Knowledge						
907	
908	EM
909	𝑀
910		Without Controlling	
911	26.63
912	±
913	6.02
914		
915	22.23
916	±
917	4.75
918		
919	26.32
920	±
921	1.80
922		
923	18.96
924	±
925	2.65
926		
927	22.37
928	±
929	1.89
930		
931	17.06
932	±
933	3.79
934	
935	TaskVec (Hendel et al., 2023) 	
936	24.16
937	±
938	6.58
939		
940	24.88
941	±
942	0.85
943		
944	29.85
945	±
946	0.83
947		
948	21.23
949	±
950	1.89
951		
952	22.93
953	±
954	2.31
955		
956	28.92
957	±
958	1.19
959	
960	ActAdd (Turner et al., 2023a) 	
961	37.87
962	±
963	8.96
964		
965	31.43
966	±
967	3.68
968		
969	27.67
970	±
971	0.82
972		
973	26.17
974	±
975	0.22
976		
977	27.52
978	±
979	3.07
980		
981	29.75
982	±
983	1.68
984	
985	SEA
986	linear
987	 (Qiu et al., 2024) 	
988	21.03
989	±
990	1.83
991		
992	23.73
993	±
994	0.86
995		
996	24.43
997	±
998	0.91
999		
1000	12.84
1001	±
1002	0.18
1003		
1004	15.64
1005	±
1006	0.24
1007		
1008	28.10
1009	±
1010	2.78
1011	
1012	SEA
1013	SqExp
1014	 (Qiu et al., 2024) 	
1015	13.64
1016	±
1017	1.62
1018		
1019	16.66
1020	±
1021	0.55
1022		
1023	23.79
1024	±
1025	1.38
1026		
1027	14.24
1028	±
1029	1.45
1030		
1031	16.24
1032	±
1033	1.06
1034		
1035	28.07
1036	±
1037	1.30
1038	
1039	DoLa (Chuang et al., 2024) 	
1040	25.53
1041	±
1042	5.19
1043		
1044	16.50
1045	±
1046	3.91
1047		
1048	20.58
1049	±
1050	1.06
1051		
1052	16.52
1053	±
1054	2.65
1055		
1056	15.66
1057	±
1058	0.88
1059		
1060	19.81
1061	±
1062	2.58
1063	
1064	♭CAD (Shi et al., 2024) 	
1065	33.72
1066	±
1067	0.84
1068		
1069	31.23
1070	±
1071	1.45
1072		
1073	41.17
1074	±
1075	0.59
1076		
1077	28.58
1078	±
1079	0.75
1080		
1081	30.81
1082	±
1083	0.94
1084		
1085	33.15
1086	¯
1087	±
1088	2.87
1089	
1090	♯ICL (Brown, 2020) 	
1091	43.73
1092	¯
1093	±
1094	1.55
1095		
1096	31.67
1097	¯
1098	±
1099	5.49
1100		
1101	43.10
1102	¯
1103	±
1104	3.63
1105		
1106	29.54
1107	¯
1108	±
1109	4.16
1110		
1111	31.23
1112	¯
1113	±
1114	0.94
1115		
1116	21.91
1117	±
1118	2.35
1119	
1120	SpARE (Ours)	
1121	47.51
1122	±
1123	1.30
1124		
1125	43.76
1126	±
1127	3.14
1128		
1129	44.11
1130	±
1131	1.30
1132		
1133	30.72
1134	±
1135	1.42
1136		
1137	35.43
1138	±
1139	1.10
1140		
1141	35.53
1142	±
1143	2.07
1144	
1145	Steer to Use Contextual Knowledge						
1146	
1147	EM
1148	𝐶
1149		Without Controlling	
1150	42.69
1151	±
1152	8.40
1153		
1154	41.67
1155	±
1156	4.66
1157		
1158	45.96
1159	±
1160	2.48
1161		
1162	69.36
1163	±
1164	3.57
1165		
1166	62.38
1167	±
1168	3.05
1169		
1170	59.25
1171	±
1172	2.82
1173	
1174	TaskVec (Hendel et al., 2023) 	
1175	41.88
1176	±
1177	9.45
1178		
1179	38.25
1180	±
1181	1.23
1182		
1183	45.52
1184	±
1185	1.06
1186		
1187	88.47
1188	¯
1189	±
1190	1.93
1191		
1192	86.91
1193	¯
1194	±
1195	0.44
1196		
1197	59.25
1198	±
1199	1.49
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "0723daf2-0c02-4eb7-aa95-d7aedac921ef",
  "isSidechain": true,
  "promptId": "eee12e6f-4b22-4cb0-adff-def0ae050a12",
  "agentId": "ad05b8d9866c10448",
  "type": "user",
  "uuid": "50259e9a-2f8b-48b5-909f-2e72e69f266a",
  "sourceToolAssistantUUID": "0723daf2-0c02-4eb7-aa95-d7aedac921ef",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "94d88260-dbbe-43d4-abc2-f8f5a7fda9d7",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 49 · 2026-05-30T06:21:18.209Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01DQXcHDHar5JC2SSctgd6W8`</summary>

```json
{
  "url": "https://www.rohan-paul.com/p/steering-knowledge-selection-behaviours",
  "prompt": "Extract ALL content from this blog post about SpARE. I need: technical analysis, key insights, critical commentary, strengths, weaknesses, method details, and any opinions about the paper's contributions. Provide full text."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "50259e9a-2f8b-48b5-909f-2e72e69f266a",
  "isSidechain": true,
  "agentId": "ad05b8d9866c10448",
  "requestId": "req_011CbYGeYGaLtXyxMCNbp4s8",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "a31f0b08-8a5a-4707-8252-7b9232929534",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "94d88260-dbbe-43d4-abc2-f8f5a7fda9d7",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018AnjP3ay9pjyr4Db2zEAZL",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 617,
      "cache_creation_input_tokens": 4512,
      "cache_read_input_tokens": 24079,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4512,
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

_source line 50 · 2026-05-30T06:21:19.130Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01EySdQXWzRpg9yhGpyz2NLp`</summary>

```json
{
  "query": "NAACL 2025 oral presentation \"knowledge conflict\" SAE sparse autoencoder steering review criticism"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a31f0b08-8a5a-4707-8252-7b9232929534",
  "isSidechain": true,
  "agentId": "ad05b8d9866c10448",
  "requestId": "req_011CbYGeYGaLtXyxMCNbp4s8",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "65d9fe18-66ac-48ca-801c-de2cb1776abc",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "94d88260-dbbe-43d4-abc2-f8f5a7fda9d7",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018AnjP3ay9pjyr4Db2zEAZL",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 617,
      "cache_creation_input_tokens": 4512,
      "cache_read_input_tokens": 24079,
      "output_tokens": 363,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 4512
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 617,
          "output_tokens": 363,
          "cache_read_input_tokens": 24079,
          "cache_creation_input_tokens": 4512,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 4512,
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

_source line 51 · 2026-05-30T06:21:24.848Z_

<details><summary>↩ Tool result · `toolu_01DQXcHDHar5JC2SSctgd6W8`</summary>

```text
# SpARE: SAE-Based Representation Engineering for LLM Knowledge Control

## Technical Overview

SpARE addresses a fundamental challenge in large language models: conflicts between knowledge stored in model parameters and knowledge provided through context. The method employs sparse autoencoders (SAEs) to identify and manipulate internal neural representations without requiring model retraining.

## Core Methodology

The approach operates through several interconnected steps:

1. **Conflict Detection**: "Knowledge conflicts are detectable in mid-layer residual streams" by probing internal activations during inference.

2. **Feature Decomposition**: Rather than directly editing dense vectors, SpARE leverages SAEs to break down complex representations into "monosemantic features"—individual interpretable components that encode specific behaviors.

3. **Targeted Intervention**: The system identifies features controlling knowledge selection and applies surgical edits at inference time, manipulating "less than 0.05% SAE activations for steering."

4. **Input-Dependent Editing**: The method adapts interventions based on specific inputs rather than applying static modifications.

## Key Strengths

- **Training-Free Design**: Operates without retraining, reducing computational overhead
- **Interpretability**: SAEs provide transparency into which features control knowledge behavior
- **Efficiency**: Minimal feature manipulation achieves substantial effects
- **Performance Gains**: "Outperforms existing representation engineering methods by 10%" and surpasses contrastive decoding approaches

## Limitations & Gaps

The post provides limited information regarding:

- Failure cases or edge conditions
- Computational costs of SAE inference
- Generalization across different model architectures
- Potential safety implications of precise knowledge steering

## Distinctive Contribution

SpARE differentiates itself by combining SAE-based decomposition with mid-layer targeting, contrasting sharply with methods requiring additional model interactions or input modifications.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a31f0b08-8a5a-4707-8252-7b9232929534",
  "isSidechain": true,
  "promptId": "eee12e6f-4b22-4cb0-adff-def0ae050a12",
  "agentId": "ad05b8d9866c10448",
  "type": "user",
  "uuid": "d497bfb5-ce55-446f-aa58-b8e497d1385b",
  "sourceToolAssistantUUID": "a31f0b08-8a5a-4707-8252-7b9232929534",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "94d88260-dbbe-43d4-abc2-f8f5a7fda9d7",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 52 · 2026-05-30T06:21:26.618Z_

<details><summary>↩ Tool result · `toolu_01EySdQXWzRpg9yhGpyz2NLp`</summary>

```text
Web search results for query: "NAACL 2025 oral presentation "knowledge conflict" SAE sparse autoencoder steering review criticism"

Links: [{"title":"CorrSteer: Generation-Time LLM Steering via Correlated Sparse Autoencoder Features","url":"https://arxiv.org/html/2508.12535v2"},{"title":"SAEs Are Good for Steering – If You Select the Right Features","url":"https://arxiv.org/html/2505.20063v1"},{"title":"Steering Knowledge Selection Behaviours in LLMs via SAE-Based   Representation Engineering","url":"https://arxiv.org/pdf/2410.15999"},{"title":"Does higher interpretability imply better utility? A Pairwise Analysis on Sparse Autoencoders","url":"https://arxiv.org/pdf/2510.03659"},{"title":"Findings of the Association for Computational Linguistics:","url":"https://aclanthology.org/2025.findings-naacl.423.pdf"},{"title":"Use Sparse Autoencoders to Discover Unknown Concepts, Not to Act on Known Concepts","url":"https://arxiv.org/html/2506.23845v1"},{"title":"Denoising Concept Vectors with Sparse Autoencoders for Improved Language Model Steering","url":"https://arxiv.org/pdf/2505.15038"},{"title":"Improving Steering Vectors by Targeting Sparse Autoencoder Features","url":"https://arxiv.org/pdf/2411.02193"}]

Based on the search results, I found relevant information about SAE-based steering and knowledge conflict research at NAACL 2025:

A NAACL 2025 paper by Yu Zhao, Alessio Devoto, Giwon Hong, and colleagues titled "Steering knowledge selection behaviours in LLMs via SAE-based representation engineering" was published in the Proceedings of the 2025 Conference of the North American Chapter of the Association for Computational Linguistics in April 2025.

The paper proposes SPARE, a Sparse Auto-Encoder-based Representation Engineering method to steer the knowledge selection behavior of LLMs, which identifies SAE activations related to specific knowledge selection behaviors and extracts functional features that control the usage of contextual and parametric knowledge. The research evaluates their approach on ODQA datasets with knowledge conflicts, where instances are presented with evidence supporting memorized knowledge versus evidence that conflicts with the language model's memorized knowledge.

Notably, the search results also reveal broader criticism of SAE-based steering approaches. A 2025 evaluation by Wu et al. compared SAE steering against many methods and found that even simple baselines outperform SAEs. However, subsequent work shows that most of the gap can be closed via more careful choice of SAE features.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "65d9fe18-66ac-48ca-801c-de2cb1776abc",
  "isSidechain": true,
  "promptId": "eee12e6f-4b22-4cb0-adff-def0ae050a12",
  "agentId": "ad05b8d9866c10448",
  "type": "user",
  "uuid": "c02c3d1a-4a1d-457b-ae6d-250798acea21",
  "sourceToolAssistantUUID": "65d9fe18-66ac-48ca-801c-de2cb1776abc",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "94d88260-dbbe-43d4-abc2-f8f5a7fda9d7",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 53 · 2026-05-30T06:21:29.508Z_

Let me continue reading the rest of the paper for analysis/discussion and limitations, and fetch the related critique papers.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c02c3d1a-4a1d-457b-ae6d-250798acea21",
  "isSidechain": true,
  "agentId": "ad05b8d9866c10448",
  "requestId": "req_011CbYGffJmWtCrA1Gm3Dcy6",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "ff9cd252-ab84-45bd-82f9-41371eac57dc",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "94d88260-dbbe-43d4-abc2-f8f5a7fda9d7",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EtcZDokGJhRJCkcXaA4gYF",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5790,
      "cache_read_input_tokens": 28591,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 5790,
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

_source line 54 · 2026-05-30T06:21:33.809Z_

<details open><summary>🔧 Tool call — Read · `toolu_01TraBwZ6qvaX2hcopn1t7SA`</summary>

```json
{
  "file_path": "/home/ubuntu/.claude-account-2/projects/-home-ubuntu-idea-adversarial/94d88260-dbbe-43d4-abc2-f8f5a7fda9d7/tool-results/toolu_014TM8Ga7wmGWtEpyBawBT72.txt",
  "offset": 1200,
  "limit": 500
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ff9cd252-ab84-45bd-82f9-41371eac57dc",
  "isSidechain": true,
  "agentId": "ad05b8d9866c10448",
  "requestId": "req_011CbYGffJmWtCrA1Gm3Dcy6",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "aac42429-05ed-462a-a126-6bf0f1f67400",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "94d88260-dbbe-43d4-abc2-f8f5a7fda9d7",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EtcZDokGJhRJCkcXaA4gYF",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5790,
      "cache_read_input_tokens": 28591,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 5790,
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

### Tool result

_source line 55 · 2026-05-30T06:21:34.138Z_

<details><summary>↩ Tool result · `toolu_01TraBwZ6qvaX2hcopn1t7SA`</summary>

```text
1200	
1201	ActAdd (Turner et al., 2023a) 	
1202	51.91
1203	±
1204	8.03
1205		
1206	47.48
1207	±
1208	3.93
1209		
1210	46.90
1211	±
1212	1.89
1213		
1214	73.01
1215	±
1216	1.58
1217		
1218	69.64
1219	±
1220	0.20
1221		
1222	59.66
1223	±
1224	2.89
1225	
1226	SEA
1227	linear
1228	 (Qiu et al., 2024) 	
1229	43.61
1230	±
1231	10.3
1232		
1233	47.73
1234	±
1235	0.43
1236		
1237	52.95
1238	±
1239	1.90
1240		
1241	69.78
1242	±
1243	0.97
1244		
1245	67.32
1246	±
1247	0.28
1248		
1249	60.31
1250	±
1251	2.25
1252	
1253	SEA
1254	SqExp
1255	 (Qiu et al., 2024) 	
1256	57.08
1257	±
1258	2.92
1259		
1260	48.04
1261	±
1262	0.45
1263		
1264	61.45
1265	±
1266	0.54
1267		
1268	72.04
1269	±
1270	1.60
1271		
1272	68.20
1273	±
1274	1.10
1275		
1276	61.45
1277	±
1278	0.30
1279	
1280	DoLa (Chuang et al., 2024) 	
1281	44.29
1282	±
1283	8.46
1284		
1285	33.54
1286	±
1287	3.38
1288		
1289	15.90
1290	±
1291	10.1
1292		
1293	68.45
1294	±
1295	3.83
1296		
1297	50.95
1298	±
1299	5.15
1300		
1301	23.34
1302	±
1303	10.5
1304	
1305	♭CAD (Shi et al., 2024) 	
1306	65.65
1307	±
1308	5.50
1309		
1310	54.69
1311	±
1312	3.25
1313		
1314	63.10
1315	±
1316	2.32
1317		
1318	78.69
1319	±
1320	3.85
1321		
1322	70.07
1323	±
1324	3.77
1325		
1326	64.12
1327	¯
1328	±
1329	4.44
1330	
1331	♯ICL (Brown, 2020) 	
1332	73.35
1333	¯
1334	±
1335	3.82
1336		
1337	63.33
1338	¯
1339	±
1340	3.50
1341		
1342	70.19
1343	¯
1344	±
1345	2.51
1346		
1347	51.75
1348	±
1349	5.60
1350		
1351	47.51
1352	±
1353	1.86
1354		
1355	47.24
1356	±
1357	3.81
1358	
1359	SpARE (Ours)	
1360	77.69
1361	±
1362	1.24
1363		
1364	69.32
1365	±
1366	1.26
1367		
1368	73.78
1369	±
1370	0.74
1371		
1372	92.24
1373	±
1374	0.49
1375		
1376	87.30
1377	±
1378	1.96
1379		
1380	87.96
1381	±
1382	1.85
1383	Table 1: Overall performance of steering the utilisation of parametric and contextual knowledge, measured by 
1384	EM
1385	𝑀
1386	 and 
1387	EM
1388	𝐶
1389	. "Without Controlling" indicates the baseline that we do not use any controlling methods to steer the generation. ♯ICL is not an inference-time controlling strategy, which controls the behaviours by changing demonstrations. ♭CAD needs additional forwarding for contrastive decoding.
1390	Baselines
1391	
1392	We compare SpARE against the following inference-time representation engineering methods: 1) TaskVec (Hendel et al., 2023); 2) ActAdd (Turner et al., 2023a); 3) SEA (Qiu et al., 2024) with linear and non-linear versions, noted by subscript "linear" and "SqExp". We compare with the following contrastive decoding methods: 1) DoLa (Chuang et al., 2024); 2) CAD (Shi et al., 2024). Moreover, we also compare using in-context learning (ICL) (Brown, 2020) to steer the knowledge selection. We use 
1393	𝐸
1394	𝐶
1395	 and 
1396	𝐶
1397	 in the demonstrations to guide the model to ignore its parametric knowledge and use the contextual knowledge, and use 
1398	𝐸
1399	𝐶
1400	 and 
1401	𝑀
1402	 to guide the model to ignore the contextual knowledge and use its parametric knowledge. ICL is not an inference-time strategy because it requires changing the original input of the model to achieve a desired behaviour. More details of baseline implementation and hyperparameters searching are presented in Section C.5 and  Section C.6.
1403	
1404	Hyperparameters
1405	
1406	We select the proper hyperparameters for SpARE in the developments set that is also used to select the hyperparameters of baselines, and the details are presented in Section C.6. In the following, we apply SpARE from the 12th to the 15th and 13th to the 16th layer for Llama2-7B and Llama3-8B and from the 23rd to 25th and the 29th to 31st layers for Gemma2-9B; we analyse the performance of editing individual layers in Section 6.1.
1407	
1408	5.2Overall Performance Comparison
1409	Metrics
1410	
1411	We use Exact Match (EM) to evaluate the performance. Specifically, we evaluate the control capability of generating contextual or parametric answers using the following metrics:
1412	
1413	EM
1414	𝐶
1415	
1416	accuracy of steering the usage of contextual knowledge to generate answers 
1417	𝐶
1418	.
1419	
1420	EM
1421	𝑀
1422	
1423	accuracy of steering the usage of parametric knowledge to generate answer 
1424	𝑀
1425	.
1426	
1427	Experimental Results
1428	
1429	We present the main results in Table 1. First, we find SpARE outperforms existing representation engineering methods TaskVec, ActAdd and SEA on steering the usage of both contextual and parametric knowledge. This indicates that SpARE can more accurately extract features related to knowledge selection behaviours through the SAE and use them to steer the generation more effectively.
1430	
1431	Second, we find SpARE outperforms contrastive decoding methods DoLa and CAD, especially in steering the usage of parametric knowledge. Though contrastive decoding strategies can effectively improve the use of contextual knowledge, they struggle to steer the use of parametric knowledge. In contrast, SpARE can more effectively steer the usage of both knowledge by adding and removing the desired and undesired functional features, which we will further analyse in the later ablation study.
1432	
1433	Moreover, SpARE surpasses the non-inference-time controlling method ICL. It suggests the SpARE can both effectively and efficiently control the knowledge selection behaviours of LLMs. It also suggests a promising capability of representation engineering to control the behaviours of LLMs at inference time in practical applications.
1434	
1435	(a)Capability of changing behaviours.
1436	(b)Impact of intervention.
1437	(c)Ablation studies.
1438	Figure 4: Detailed evaluation results of controlling capability on NQSwap. We use different colours for different methods and use different shapes for different models. The upper-right area indicates a high performance for all figures. (a) presents the capability of changing the behaviour of LLMs, where 
1439	𝑥
1440	-axis and 
1441	𝑦
1442	-axis are 
1443	EM
1444	𝐶
1445	→
1446	𝑀
1447	 and 
1448	EM
1449	𝑀
1450	→
1451	𝐶
1452	, measuring the capability of changing the answer from 
1453	𝐶
1454	 to 
1455	𝑀
1456	 and from 
1457	𝑀
1458	 to 
1459	𝐶
1460	, respectively; (b) presents the capability of maintaining the behaviour when steering to the same behaviour as the original behaviour, where 
1461	𝑥
1462	-axis and 
1463	𝑦
1464	-axis are 
1465	EM
1466	𝑀
1467	→
1468	𝑀
1469	 and 
1470	EM
1471	𝐶
1472	→
1473	𝐶
1474	, measuring the maintaining capability of generating 
1475	𝑀
1476	 and 
1477	𝐶
1478	, respectively; (c) present the ablation analysis of SpARE, 
1479	𝑥
1480	-axis and 
1481	𝑦
1482	-axis are 
1483	EM
1484	𝑀
1485	 and 
1486	EM
1487	𝐶
1488	.
1489	5.3Multi-Perspective Controlling Analysis
1490	
1491	In the following, we analyse the controlling capability of SpARE from different perspectives: 1) the capability of changing the behaviour (Fig. 4(a)), 2) the potential negative impact of intervention (Fig. 4(b)), and 3) the ablation study (Fig. 4(c)).
1492	
1493	Capability of Changing the Behaviours
1494	
1495	Unlike merely comparing overall performance across the entire dataset, we further examine their capability of changing the original knowledge selection behaviour of LLMs by the following two metrics:
1496	
1497	EM
1498	𝐶
1499	→
1500	𝑀
1501	
1502	accuracy of changing the behaviour from generating contextual answers 
1503	𝐶
1504	 to parametric answers 
1505	𝑀
1506	 in the subset of instances where the model generates 
1507	𝐶
1508	 without controlling.
1509	
1510	EM
1511	𝑀
1512	→
1513	𝐶
1514	
1515	accuracy of changing the behaviour from generating parametric answers 
1516	𝑀
1517	 to contextual answers 
1518	𝐶
1519	 in the subset of instances where the model generates 
1520	𝑀
1521	 without controlling.
1522	
1523	As shown in Fig. 4(a), SpARE outperforms contrastive decoding methods and is located in the upper-right area of the figure. SpARE also outperforms representation engineering methods. It suggests that the SAE enables accurately extracting features related to knowledge behaviour and thus more effectively changes both the original behaviours of using contextual and parametric knowledge. We also observe that all methods are less effective in steering toward the use of parametric knowledge than contextual knowledge. This finding matches the previous works (Su et al., 2024; Xie et al., 2024a; Ortu et al., 2024), which shows LLMs prefer contextual knowledge, and thus more difficult to steer the behaviour of using parametric knowledge.
1524	
1525	Impacts of Intervention
1526	
1527	A sufficient but unnecessary intervention can change the behaviour of LLMs, but it also can introduce noise and decrease accuracy. Here, we investigate the potential negative impact of methods by steering LLMs using the same knowledge they will use without control. We expect LLMs to maintain their original behaviours, measured by the following two metrics:
1528	
1529	EM
1530	𝑀
1531	→
1532	𝑀
1533	
1534	accuracy of maintaining the behaviour of generating 
1535	𝑀
1536	 when steering the use of parametric knowledge in the subset of instances where the model generates 
1537	𝑀
1538	 without controlling.
1539	
1540	EM
1541	𝐶
1542	→
1543	𝐶
1544	
1545	accuracy of maintaining the behaviour of generating 
1546	𝐶
1547	 when steering the use contextual knowledge in the subset of instances where the model generates 
1548	𝐶
1549	 without controlling.
1550	
1551	As shown in Fig. 4(b), as it minimally alters the original behaviour when guiding the model to produce similar outcomes. SpARE has a close performance to ICL, indicating it can steer the behaviour effectively while introducing a little unnecessary editing. Though CAD maintains the most accuracy in contextual knowledge, its performance decreases substantially in maintaining the behaviour of generating parametric knowledge. Finally, while other representation engineering methods may alter the entire model behaviour due to editing of polysemantic features, SpARE provides a more precise approach to editing through the SAE activations and thus delivers better performance in maintaining the model behaviours.
1552	
1553	Ablation Study
1554	
1555	We present the ablation study in the following settings: 1) SpARE input-independent: it uses 
1556	𝐳
1557	𝐶
1558	 and 
1559	𝐳
1560	𝑀
1561	 to steer the generation without calculating 
1562	𝐳
1563	−
1564	 and 
1565	𝐳
1566	+
1567	 based on the input activation; 2) SpARE remove only: it edits the hidden states by only removing the functional features of the undesired behaviour; 3) SpARE add only: it edits the hidden states by only adding the functional features of the desired behaviour.
1568	
1569	As shown in Fig. 4(c), we can see that every ablation results in a significant controlling capability decrease. The input-independent editing strategy that omits the calculations of Eq. 2 and Eq. 3 fails to steer the usage of knowledge and obtain results that are close to the ones we obtain without controlling. The results of SpARE "remove only" obtain a zero accuracy on both 
1570	EM
1571	𝑀
1572	 and 
1573	EM
1574	𝐶
1575	, indicating that the model cannot keep the original behaviour and also cannot generate answers toward another behaviour. This suggests that SpARE can effectively remove the functional features of the original behaviour. Moreover, SpARE "add only" leads to worse performance than without controlling, suggesting the importance of removing the features of undesired knowledge selection behaviour.
1576	
1577	6Analysis and Discussion
1578	6.1Analysing the Layer Choice
1579	
1580	We present the results of editing multiple layers in Table 1; here, we analyse the effectiveness of SpARE by editing each layer individually. As shown in Fig. 6, we find SpARE can control the behaviour of LLMs most effectively at mid-layers for both Llama3-8B and Gemma2-9B. These layers are also where we can detect knowledge conflict most accurately, as shown in Fig. 2 and Appendix A. This supports the practical application of inference-time intervention to control knowledge selection behaviour, where SpARE can effectively steer the generation once we detect the conflict.
1581	
1582	The effectiveness of steering the behaviours in middle layers also matches previous findings (Hendel et al., 2023; Pan et al., 2023a; Todd et al., 2024), that suggest that the middle layers of LLMs contain the functional feature that drives a task. To the best of our knowledge, we are the first to accurately extract this functional feature using pre-trained SAEs.
1583	
1584	(a)Llama3-8B
1585	(b)Gemma2-9B
1586	Figure 5:Effectiveness of SpARE on editing different layers individually.
1587	(c)Probing results
1588	(d)Skewness pattern
1589	Figure 6:The residual stream changes after applying SpARE to Llama3-8B at the 15th layer.
1590	6.2Analysing the Residual Stream
1591	
1592	We analyse how the residual stream changes after applying SpARE. Here, we edit the hidden states from 
1593	𝒟
1594	𝐸
1595	𝐶
1596	 
1597	=
1598	{
1599	(
1600	𝑄
1601	,
1602	𝐸
1603	𝐶
1604	)
1605	}
1606	 at the 15th layer to steer the contextual and parametric knowledge usage.
1607	
1608	In Fig. 5(c), we present the probing results on the residual stream using the same probing model described in Section 3. We observe that when we steer towards the usage of parametric knowledge, the probing performance decreases immediately (green line), indicating that the signal of knowledge conflict fades quickly, and the representations of activations become closer to 
1609	𝒟
1610	𝐸
1611	𝑀
1612	, thus making it more difficult for the probing model to distinguish whether a given activation is from 
1613	𝒟
1614	𝐸
1615	𝐶
1616	 or 
1617	𝒟
1618	𝐸
1619	𝑀
1620	. In contrast, when we steer towards using contextual knowledge, the probing performance increases (blue line), indicating the signal of the conflict increases, and the representations of activations become more different from 
1621	𝒟
1622	𝐸
1623	𝑀
1624	, making it easier for the probing model to distinguish whether a given activations is from 
1625	𝒟
1626	𝐸
1627	𝐶
1628	 or 
1629	𝒟
1630	𝐸
1631	𝑀
1632	.
1633	
1634	(a)Llama3-8B
1635	(b)Llama2-7B
1636	Figure 7:The skewness patterns of the residual steam when LLMs select different sources of knowledge to generate the answer without controlling in NQSwap.
1637	
1638	In Fig. 5(d), we find the skewness of the representation from the residual stream – measured by Kurtosis – shows distinct patterns after applying SpARE. We observe that when we apply SpARE to steer the usage of contextual knowledge at the 15th layer, the residual stream becomes significantly more skewed starting from later layers—the 19th layer (blue line); in contrast, when we use parametric knowledge, the residual stream becomes less skewed (green line). Moreover, in Fig. 7, we analyse the skewness pattern when LLMs freely select knowledge to generate answers without controlling. We find the residual stream of 
1639	𝒟
1640	𝐶
1641	, where the model uses contextual knowledge to generate answers, is significantly more skewed than 
1642	𝒟
1643	𝑀
1644	 from the 19th layer. Thus, the skewness pattern changes shown in Fig. 5(d) can indicate that SpARE steers the knowledge selection behaviours.
1645	
1646	We provide more analysis of the representation patterns in Appendix F and Zhao et al. (2024b). In this work, we only provide our empirical observation on the representation pattern and leave investigating the reasons in future works.
1647	
1648	7Related Works
1649	Representation Engineering
1650	
1651	Many studies focus on mechanistic interpretability to understand the LLMs by analysing the activities and connections of individual network components, such as circuits (Elhage et al., 2021; Olsson et al., 2022) and neurons (Geva et al., 2021; Meng et al., 2022) However, though mechanistic interpretability can successfully explain simple mechanisms, it often struggles with more complex phenomena  (Zou et al., 2023a). Differently, representation engineering Turner et al. (2023a); Qiu et al. (2024); Zou et al. (2023a) offers a complementary approach. It focuses on the characteristics of representations rather than lower-level mechanisms, providing a framework for understanding complex systems at a higher level of abstraction. It has shown more promise in interpreting higher-level behaviours of LLMs at scale. Some works modify model activations to change behaviours (Ravfogel et al., 2020; Iskander et al., 2023; Liu et al., 2024; Zou et al., 2023b; Li et al., 2023), and some works extract latent vectors and leveraging these vectors to regulate the model’s inference (Turner et al., 2023b; Subramani et al., 2022; Rimsky et al., 2023).
1652	
1653	Knowledge Conflicts
1654	
1655	Knowledge conflicts refer to discrepancies among contextual and parametric knowledge (Chen et al., 2022; Xie et al., 2024b). Xu et al. (2024) identify three types of knowledge conflicts: inter-context (Zhang and Choi, 2021; Du et al., 2022; Pan et al., 2023b; Zhao et al., 2024c), context-memory (Longpre et al., 2021; Xie et al., 2024b; Minder et al., 2024), and intra-memory conflicts (Huang et al., 2023). In this work, we focus on context-memory knowledge conflict, which refers to conflicts between the contextual knowledge and the parametric knowledge encoded in the model parameters. Ortu et al. (2024) and Jin et al. (2024) investigate the mechanisms of attention heads and feed-forward networks of LLMs when context-memory knowledge conflict occurs.
1656	
1657	Sparse Auto-Encoder
1658	
1659	Sparse Auto-Encoders (SAEs) have been introduced as a post-hoc analysis tool to identify disentangled features within uncompressed representations of an LLM (Yun et al., 2021; Bricken et al., 2023; Huben et al., 2024). SAEs are trained with sparsity regularisation to learn a sparse, overcomplete basis that characterises the activation space of an LLM (Bereska and Gavves, 2024). Marks et al. (2024) showed that the features learned by SAEs can identify sparse circuits in LLMs. Templeton et al. (2024b) showed the possibility of searching for monosemantic features and steering LLMs’ generation. Chalnev et al. (2024) improves steering vectors using SAEs. Gur-Arieh et al. (2025) generates description for representations learned through SEAs. (Lan et al., 2024) finds universal representation across different language models.
1660	
1661	8Conclusions
1662	
1663	We investigated the context-memory knowledge conflicts in LLMs. We identify that knowledge conflicts can be detected by probing the residual stream of the model (Section 3) and propose SpARE (Section 4), a training-free representation engineering method that leverages pre-trained SAEs to effectively and efficiently control the knowledge selection behaviour of LLMs at inference time. Our experimental results on ODQA tasks show that SpARE produces more accurate results than existing representation engineering and contrastive decoding methods (Section 5). By providing a mechanism to steer knowledge selection behaviours at inference time, SpARE offers a promising approach to managing knowledge conflicts in LLMs without significant computational overhead. Additionally, we investigate the residual stream of LLMs under knowledge conflicts (Section 6). We find that 1) the knowledge selection behaviour is more steerable at the middle layers of LLMs; 2) the residual stream shows a significantly more skewed representation when models using contextual knowledge compared to using parametric knowledge.
1664	
1665	Limitations
1666	
1667	While our proposed method, SpARE, demonstrates effective control over knowledge selection behaviours in LLMs, there are several limitations to consider. First, the approach relies on pre-trained SAEs to identify and manipulate functional features within the internal activations of the model, so it may not directly apply to models where pre-trained SAEs are unavailable or cannot be efficiently trained. Second, our experiments are conducted on specific ODQA tasks involving context-memory knowledge conflicts. While the results are promising in this setting, it is unclear how well the method generalises to other types of tasks or conflicts, such as those involving complex reasoning, multi-hop questions, or long-form generation. Finally, the control over knowledge selection behaviours is evaluated primarily in terms of steering the model towards either contextual or parametric knowledge. In practice, the decision about which knowledge source to trust may not be binary or require a more elaborate approach, such as using another model as a critic (Hong et al., 2024).
1668	
1669	Acknowledgments
1670	
1671	Yu Zhao and Xiaotang Du were partly supported by the UKRI Centre for Doctoral Training in Natural Language Processing, funded by UK Research and Innovation (grant EP/S022481/1) and the University of Edinburgh, School of Informatics. Alessio Devoto was supported by Sapienza Grant RM1221816BD028D6 (DeSMOS). Giwon Hong was supported by the ILCC PhD program (School of Informatics Funding Package) at the University of Edinburgh, School of Informatics. Aryo Pradipta Gema was supported by the United Kingdom Research and Innovation (grant EP/S02431X/1), UKRI Centre for Doctoral Training in Biomedical AI at the University of Edinburgh, School of Informatics. Xuanli He was funded by an industry grant from Cisco. Pasquale Minervini was partially funded by ELIAI (The Edinburgh Laboratory for Integrated Artificial Intelligence), EPSRC (grant no. EP/W002876/1), an industry grant from Cisco, and a donation from Accenture LLP. This work was supported by the Edinburgh International Data Facility (EIDF) and the Data-Driven Innovation Programme at the University of Edinburgh.
1672	
1673	References
1674	Allen-Zhu and Li (2023)	Zeyuan Allen-Zhu and Yuanzhi Li. 2023.Physics of language models: Part 1, context-free grammar.arXiv preprint arXiv:2305.13673.
1675	Anil et al. (2023)	Rohan Anil, Sebastian Borgeaud, Yonghui Wu, Jean-Baptiste Alayrac, Jiahui Yu, Radu Soricut, Johan Schalkwyk, Andrew M Dai, Anja Hauth, et al. 2023.Gemini: a family of highly capable multimodal models.arXiv preprint arXiv:2312.11805.
1676	Bereska and Gavves (2024)	Leonard Bereska and Efstratios Gavves. 2024.Mechanistic interpretability for AI safety - A review.CoRR, abs/2404.14082.
1677	Bricken et al. (2023)	Trenton Bricken, Adly Templeton, Joshua Batson, Brian Chen, Adam Jermyn, Tom Conerly, Nicholas L. Turner, Cem Anil, Carson Denison, Amanda Askell, Robert Lasenby, Yifan Wu, Shauna Kravec, Nicholas Schiefer, Tim Maxwell, Nicholas Joseph, Alex Tamkin, Karina Nguyen, Brayden McLean, Josiah E. Burke, Tristan Hume, Shan Carter, Tom Henighan, and Chris Olah. 2023.Towards monosemanticity: Decomposing language models with dictionary learning.Transformer Circuits Thread.
1678	Brown (2020)	Tom B Brown. 2020.Language models are few-shot learners.arXiv preprint arXiv:2005.14165.
1679	Chalnev et al. (2024)	Sviatoslav Chalnev, Matthew Siu, and Arthur Conmy. 2024.Improving steering vectors by targeting sparse autoencoder features.ArXiv, abs/2411.02193.
1680	Chen and Shu (2023a)	Canyu Chen and Kai Shu. 2023a.Can llm-generated misinformation be detected?arXiv preprint arXiv:2309.13788.
1681	Chen and Shu (2023b)	Canyu Chen and Kai Shu. 2023b.Combating misinformation in the age of llms: Opportunities and challenges.AI Magazine.
1682	Chen et al. (2022)	Hung-Ting Chen, Michael J. Q. Zhang, and Eunsol Choi. 2022.Rich knowledge sources bring complex knowledge conflicts: Recalibrating models to reflect conflicting evidence.In EMNLP, pages 2292–2307. Association for Computational Linguistics.
1683	Chuang et al. (2024)	Yung-Sung Chuang, Yujia Xie, Hongyin Luo, Yoon Kim, James R. Glass, and Pengcheng He. 2024.Dola: Decoding by contrasting layers improves factuality in large language models.In The Twelfth International Conference on Learning Representations, ICLR 2024, Vienna, Austria, May 7-11, 2024. OpenReview.net.
1684	Conneau et al. (2018)	Alexis Conneau, German Kruszewski, Guillaume Lample, Loïc Barrault, and Marco Baroni. 2018.What you can cram into a single vector: Probing sentence embeddings for linguistic properties.arXiv preprint arXiv:1805.01070.
1685	Devoto et al. (2024)	Alessio Devoto, Yu Zhao, Simone Scardapane, and Pasquale Minervini. 2024.A simple and effective l
1686	2
1687	 norm-based strategy for KV cache compression.CoRR, abs/2406.11430.
1688	Du et al. (2022)	Yibing Du, Antoine Bosselut, and Christopher D. Manning. 2022.Synthetic disinformation attacks on automated fact verification systems.In AAAI, pages 10581–10589. AAAI Press.
1689	Dubey et al. (2024)	Abhimanyu Dubey, Abhinav Jauhri, Abhinav Pandey, Abhishek Kadian, Ahmad Al-Dahle, Aiesha Letman, Akhil Mathur, Alan Schelten, Amy Yang, Angela Fan, et al. 2024.The llama 3 herd of models.arXiv preprint arXiv:2407.21783.
1690	Elhage et al. (2021)	Nelson Elhage, Neel Nanda, Catherine Olsson, Tom Henighan, Nicholas Joseph, Ben Mann, Amanda Askell, Yuntao Bai, Anna Chen, Tom Conerly, et al. 2021.A mathematical framework for transformer circuits.Transformer Circuits Thread, 1(1):12.
1691	Gao et al. (2024)	Leo Gao, Tom Dupré la Tour, Henk Tillman, Gabriel Goh, Rajan Troll, Alec Radford, Ilya Sutskever, Jan Leike, and Jeffrey Wu. 2024.Scaling and evaluating sparse autoencoders.CoRR, abs/2406.04093.
1692	Geva et al. (2021)	Mor Geva, Roei Schuster, Jonathan Berant, and Omer Levy. 2021.Transformer feed-forward layers are key-value memories.In Proceedings of the 2021 Conference on Empirical Methods in Natural Language Processing, pages 5484–5495.
1693	Gur-Arieh et al. (2025)	Yoav Gur-Arieh, Roy Mayan, Chen Agassy, Atticus Geiger, and Mor Geva. 2025.Enhancing automated interpretability with output-centric feature descriptions.arXiv preprint arXiv:2501.08319.
1694	Hendel et al. (2023)	Roee Hendel, Mor Geva, and Amir Globerson. 2023.In-context learning creates task vectors.In Findings of the Association for Computational Linguistics: EMNLP 2023, Singapore, December 6-10, 2023, pages 9318–9333. Association for Computational Linguistics.
1695	Hong et al. (2024)	Giwon Hong, Jeonghwan Kim, Junmo Kang, Sung-Hyon Myaeng, and Joyce Jiyoung Whang. 2024.Why so gullible? enhancing the robustness of retrieval-augmented models against counterfactual noise.In Findings of the Association for Computational Linguistics: NAACL 2024, Mexico City, Mexico, June 16-21, 2024, pages 2474–2495. Association for Computational Linguistics.
1696	Huang et al. (2023)	Lei Huang, Weijiang Yu, Weitao Ma, Weihong Zhong, Zhangyin Feng, Haotian Wang, Qianglong Chen, Weihua Peng, Xiaocheng Feng, Bing Qin, and Ting Liu. 2023.A survey on hallucination in large language models: Principles, taxonomy, challenges, and open questions.CoRR, abs/2311.05232.
1697	Huben et al. (2024)	Robert Huben, Hoagy Cunningham, Logan Riggs, Aidan Ewart, and Lee Sharkey. 2024.Sparse autoencoders find highly interpretable features in language models.In ICLR. OpenReview.net.
1698	Iskander et al. (2023)	Shadi Iskander, Kira Radinsky, and Yonatan Belinkov. 2023.Shielded representations: Protecting sensitive attributes through iterative gradient-based projection.In ACL (Findings), pages 5961–5977. Association for Computational Linguistics.
1699	Jiang et al. (2023)	Albert Q Jiang, Alexandre Sablayrolles, Arthur Mensch, Chris Bamford, Devendra Singh Chaplot, Diego de las Casas, Florian Bressand, Gianna Lengyel, Guillaume Lample, Lucile Saulnier, et al. 2023.Mistral 7b.arXiv preprint arXiv:2310.06825.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "aac42429-05ed-462a-a126-6bf0f1f67400",
  "isSidechain": true,
  "promptId": "eee12e6f-4b22-4cb0-adff-def0ae050a12",
  "agentId": "ad05b8d9866c10448",
  "type": "user",
  "uuid": "99cfd411-78ff-4434-a42d-656c86b29720",
  "sourceToolAssistantUUID": "aac42429-05ed-462a-a126-6bf0f1f67400",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "94d88260-dbbe-43d4-abc2-f8f5a7fda9d7",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 56 · 2026-05-30T06:21:36.218Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01HXNZSraDP6ovfQCMp2MfJt`</summary>

```json
{
  "url": "https://arxiv.org/html/2505.20063v1",
  "prompt": "Extract any discussion of the SpARE paper (Zhao et al. 2024/2025, arxiv 2410.15999) in this paper about SAE feature selection for steering. What do they say about SpARE's approach? Any criticisms or comparisons?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "99cfd411-78ff-4434-a42d-656c86b29720",
  "isSidechain": true,
  "agentId": "ad05b8d9866c10448",
  "requestId": "req_011CbYGffJmWtCrA1Gm3Dcy6",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "37857e8e-21e6-467d-bc76-ca42d37eb4fa",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "94d88260-dbbe-43d4-abc2-f8f5a7fda9d7",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EtcZDokGJhRJCkcXaA4gYF",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5790,
      "cache_read_input_tokens": 28591,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 5790,
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

_source line 57 · 2026-05-30T06:21:36.963Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_011BS9E3pBtiMf6c9XXSVacP`</summary>

```json
{
  "query": "\"yu zhao\" \"SAE-based representation engineering\" SpARE github code dataset NQSwap implementation"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "37857e8e-21e6-467d-bc76-ca42d37eb4fa",
  "isSidechain": true,
  "agentId": "ad05b8d9866c10448",
  "requestId": "req_011CbYGffJmWtCrA1Gm3Dcy6",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "2d5e7230-0530-421b-9bdc-3a6302575fac",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "94d88260-dbbe-43d4-abc2-f8f5a7fda9d7",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EtcZDokGJhRJCkcXaA4gYF",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5790,
      "cache_read_input_tokens": 28591,
      "output_tokens": 373,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 5790
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 373,
          "cache_read_input_tokens": 28591,
          "cache_creation_input_tokens": 5790,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 5790,
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

_source line 58 · 2026-05-30T06:21:39.466Z_

<details><summary>↩ Tool result · `toolu_01HXNZSraDP6ovfQCMp2MfJt`</summary>

```text
I've carefully reviewed the entire document provided, including all sections, appendices, and references. 

**There is no discussion of the SpARE paper (Zhao et al. 2024/2025, arxiv 2410.15999) in this document.**

The paper does not cite or mention SpARE anywhere in its main text, related work sections, or reference list. While this paper discusses SAE feature selection for steering and proposes input/output scores as selection criteria, it does not engage with or compare against the SpARE approach.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "37857e8e-21e6-467d-bc76-ca42d37eb4fa",
  "isSidechain": true,
  "promptId": "eee12e6f-4b22-4cb0-adff-def0ae050a12",
  "agentId": "ad05b8d9866c10448",
  "type": "user",
  "uuid": "f77bbdcf-ef1a-4e39-b3d2-e09a7b902a84",
  "sourceToolAssistantUUID": "37857e8e-21e6-467d-bc76-ca42d37eb4fa",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "94d88260-dbbe-43d4-abc2-f8f5a7fda9d7",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 59 · 2026-05-30T06:21:44.155Z_

<details><summary>↩ Tool result · `toolu_011BS9E3pBtiMf6c9XXSVacP`</summary>

```text
Web search results for query: ""yu zhao" "SAE-based representation engineering" SpARE github code dataset NQSwap implementation"

Links: [{"title":"GitHub - yuzhaouoe/SAE-based-representation-engineering: [NAACL'25 Oral] Steering Knowledge Selection Behaviours in LLMs via SAE-Based Representation Engineering","url":"https://github.com/yuzhaouoe/SAE-based-representation-engineering"},{"title":"GitHub - chrisliu298/awesome-representation-engineering: A resource repository for representation engineering in large language models · GitHub","url":"https://github.com/chrisliu298/awesome-representation-engineering"},{"title":"yuzhaouoe (Yu Zhao) · GitHub","url":"https://github.com/yuzhaouoe"},{"title":"SAE-Based Representation Engineering - a yuzhaouoe Collection","url":"https://huggingface.co/collections/yuzhaouoe/sae-based-representation-engineering"},{"title":"https://github.com/chrisliu298/awesome-representation-engineering | Ecosyste.ms: Awesome","url":"https://awesome.ecosyste.ms/projects/github.com/chrisliu298/awesome-representation-engineering"},{"title":"Yu Zhao","url":"https://yuzhaouoe.github.io/"},{"title":"Probing the Representational Power of Sparse Autoencoders in Vision Models","url":"https://arxiv.org/pdf/2508.11277"},{"title":"Group-SAE: Efficient Training of Sparse Autoencoders for Large Language Models via Layer Groups","url":"https://arxiv.org/pdf/2410.21508"}]

I found the relevant information! Here are the search results:

The paper "Steering Knowledge Selection Behaviours in LLMs via SAE-Based Representation Engineering" is authored by Yu Zhao, Alessio Devoto, Giwon Hong, Xiaotang Du, Aryo Pradipta Gema, Hongru Wang, Xuanli He, Kam-Fai Wong, and Pasquale Minervini (2024), and it was published at NAACL 2025.

The GitHub repository is located at https://github.com/yuzhaouoe/SAE-based-representation-engineering and includes implementation of the SpARE (Sparse Auto-encoder based Representation Engineering) method, with support for the NQSwap dataset. The repository includes a script (`run_spare.py`) that demonstrates usage with the Llama-2-7b model and the nqswap dataset.

The sparse auto-encoder implementation is adapted from EleutherAI/sae and jbloomAus/SAELens.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "2d5e7230-0530-421b-9bdc-3a6302575fac",
  "isSidechain": true,
  "promptId": "eee12e6f-4b22-4cb0-adff-def0ae050a12",
  "agentId": "ad05b8d9866c10448",
  "type": "user",
  "uuid": "f8675c6f-571f-4531-9222-bfd7fe0e8efa",
  "sourceToolAssistantUUID": "2d5e7230-0530-421b-9bdc-3a6302575fac",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "94d88260-dbbe-43d4-abc2-f8f5a7fda9d7",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 60 · 2026-05-30T06:21:46.859Z_

Now let me fetch the GitHub repo for implementation details and look for any OpenReview forum page for this specific paper.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f8675c6f-571f-4531-9222-bfd7fe0e8efa",
  "isSidechain": true,
  "agentId": "ad05b8d9866c10448",
  "requestId": "req_011CbYGgxFXSZeQQJg2r1fn6",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "cbccdefc-e897-41c4-8fe9-786b9b3930ea",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "94d88260-dbbe-43d4-abc2-f8f5a7fda9d7",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019wng7fGfRgHE6qL2qZGxse",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 10317,
      "cache_read_input_tokens": 34381,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 10317,
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

_source line 61 · 2026-05-30T06:21:48.735Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_0113vByTyeq12rumLPJBqw2U`</summary>

```json
{
  "url": "https://github.com/yuzhaouoe/SAE-based-representation-engineering",
  "prompt": "Extract ALL information: README content, repository structure, code details, dependencies, how to run, what SAE implementations they use, what datasets, what models, any configuration details, number of stars/forks."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "cbccdefc-e897-41c4-8fe9-786b9b3930ea",
  "isSidechain": true,
  "agentId": "ad05b8d9866c10448",
  "requestId": "req_011CbYGgxFXSZeQQJg2r1fn6",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "7cb5e404-9e3a-49cd-8744-6b79f307a195",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "94d88260-dbbe-43d4-abc2-f8f5a7fda9d7",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019wng7fGfRgHE6qL2qZGxse",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 10317,
      "cache_read_input_tokens": 34381,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 10317,
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

_source line 62 · 2026-05-30T06:21:49.716Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01CaJ7ZKXbaTBpKDze2Gru8m`</summary>

```json
{
  "query": "openreview.net/forum NAACL 2025 \"knowledge selection\" \"sparse auto\" zhao devoto hong"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7cb5e404-9e3a-49cd-8744-6b79f307a195",
  "isSidechain": true,
  "agentId": "ad05b8d9866c10448",
  "requestId": "req_011CbYGgxFXSZeQQJg2r1fn6",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "505eabcb-5a21-450d-bb95-de03a7a79bb7",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "94d88260-dbbe-43d4-abc2-f8f5a7fda9d7",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019wng7fGfRgHE6qL2qZGxse",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 10317,
      "cache_read_input_tokens": 34381,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 10317,
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

_source line 63 · 2026-05-30T06:21:50.736Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_015NSEGT1yXSwAZKNW7SfXVo`</summary>

```json
{
  "url": "https://huggingface.co/collections/yuzhaouoe/sae-based-representation-engineering",
  "prompt": "List all models/datasets in this collection. What SAE models are shared? Which layers do they cover? What are the model details?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "505eabcb-5a21-450d-bb95-de03a7a79bb7",
  "isSidechain": true,
  "agentId": "ad05b8d9866c10448",
  "requestId": "req_011CbYGgxFXSZeQQJg2r1fn6",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "3b1d7979-3ded-418f-bcc3-905b89edaec1",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "94d88260-dbbe-43d4-abc2-f8f5a7fda9d7",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019wng7fGfRgHE6qL2qZGxse",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 10317,
      "cache_read_input_tokens": 34381,
      "output_tokens": 320,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 10317
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 320,
          "cache_read_input_tokens": 34381,
          "cache_creation_input_tokens": 10317,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 10317,
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

_source line 64 · 2026-05-30T06:21:55.191Z_

<details><summary>↩ Tool result · `toolu_015NSEGT1yXSwAZKNW7SfXVo`</summary>

```text
# SAE-Based Representation Engineering Collection

## Models/Datasets in Collection

Based on the content, here are the items in this collection:

### SAE Models

1. **yuzhaouoe/Llama2-7b-SAE**
   - Updated: Mar 7, 2025
   - Model: Llama 2 7B
   - Layer coverage: Not specified in the content

2. **google/gemma-scope-9b-pt-res**
   - Updated: Dec 24, 2024
   - Model: Gemma Scope 9B (pre-trained residual stream)
   - Layer coverage: Not specified in the content

3. **EleutherAI/sae-llama-3-8b-32x**
   - Updated: Jul 9, 2024
   - Model: Llama 3 8B
   - Layer coverage: 32x expansion factor
   - Note: Most popular (44 references)

### Papers

4. **Steering Knowledge Selection Behaviours in LLMs via SAE-Based Representation Engineering** (2410.15999) - Oct 21, 2024

5. **Analysing the Residual Stream of Language Models Under Knowledge Conflicts** (2410.16090) - Oct 21, 2024

## Key Details

- **Collection Focus**: SAE-Based Representation Engineering (accepted at NAACL'25)
- **Primary Reference**: [GitHub repo](https://github.com/yuzhaouoe/SAE-based-representation-engineering)
- **Curator**: yuzhaouoe

The content provided doesn't include detailed layer-by-layer specifications. For more technical details about layer coverage and model architecture, you would need to access the individual model cards or the GitHub repository.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "3b1d7979-3ded-418f-bcc3-905b89edaec1",
  "isSidechain": true,
  "promptId": "eee12e6f-4b22-4cb0-adff-def0ae050a12",
  "agentId": "ad05b8d9866c10448",
  "type": "user",
  "uuid": "82c84105-ef77-49de-90f2-21efc11472e2",
  "sourceToolAssistantUUID": "3b1d7979-3ded-418f-bcc3-905b89edaec1",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "94d88260-dbbe-43d4-abc2-f8f5a7fda9d7",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 65 · 2026-05-30T06:21:55.673Z_

<details><summary>↩ Tool result · `toolu_01CaJ7ZKXbaTBpKDze2Gru8m`</summary>

```text
Web search results for query: "openreview.net/forum NAACL 2025 "knowledge selection" "sparse auto" zhao devoto hong"

Links: [{"title":"Accepted Papers - NAACL-HLT 2025","url":"https://2025.naacl.org/program/accepted_papers/"},{"title":"[2410.15999] Steering Knowledge Selection Behaviours in LLMs via SAE-Based Representation Engineering","url":"https://arxiv.org/abs/2410.15999"},{"title":"Steering Knowledge Selection Behaviours in LLMs via SAE-Based   Representation Engineering","url":"https://arxiv.org/pdf/2410.15999"},{"title":"Diversity-driven Data Selection for Language Model Tuning through Sparse   Autoencoder","url":"https://arxiv.org/pdf/2502.14050"},{"title":"Multi-Sentence Knowledge Selection in Open-Domain Dialogue","url":"https://arxiv.org/pdf/2203.00763"}]

Based on the search results, I found the paper you're looking for:

**"Steering Knowledge Selection Behaviours in LLMs via SAE-Based Representation Engineering"** by Yu Zhao, Alessio Devoto, Giwon Hong, Xiaotang Du, Aryo Pradipta Gema, Hongru Wang, Xuanli He, Kam-Fai Wong, and Pasquale Minervini

This paper is accepted to NAACL-HLT 2025.

The paper proposes SpARE, a training-free representation engineering method that uses pre-trained sparse auto-encoders (SAEs) to control the knowledge selection behaviour of LLMs. The work addresses context-memory knowledge conflicts where parametric knowledge may conflict with information in context, analyzing internal activations of LLMs to detect and resolve these conflicts through inference-time intervention strategies.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "505eabcb-5a21-450d-bb95-de03a7a79bb7",
  "isSidechain": true,
  "promptId": "eee12e6f-4b22-4cb0-adff-def0ae050a12",
  "agentId": "ad05b8d9866c10448",
  "type": "user",
  "uuid": "fb7b3e29-a260-45a6-82d3-2a339ff6fca8",
  "sourceToolAssistantUUID": "505eabcb-5a21-450d-bb95-de03a7a79bb7",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "94d88260-dbbe-43d4-abc2-f8f5a7fda9d7",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 66 · 2026-05-30T06:21:57.237Z_

<details><summary>↩ Tool result · `toolu_0113vByTyeq12rumLPJBqw2U`</summary>

````text
# SAE-Based Representation Engineering Repository Summary

## Project Overview
This repository implements **SpARE** (Sparse Auto-Encoder Representation Engineering), a technique for steering knowledge selection behaviors in large language models. The work has been accepted as a NAACL'25 oral presentation.

## Repository Statistics
- **Stars**: 81
- **Forks**: 9
- **Languages**: Python (99%), Shell (1%)
- **Total Commits**: 7

## Repository Structure
```
cache_data/          # Intermediate computation results
scripts/             # Execution and experiment scripts
spare/               # Core implementation
.gitignore
LICENSE (MIT)
README.md
demo.py
setup.py
```

## Setup & Installation
The project requires Python 3.9 and can be initialized via:
```bash
conda create -n spare python=3.9 -y
conda activate spare
bash ./scripts/install.sh
```

## Key Features & Execution

**Quick Demo**: Run `python ./demo.py` (currently supports short-form ODQA tasks)

**Step-by-Step Workflow**:
1. Group prompts by knowledge selection patterns
2. Save activations from grouped prompts
3. Compute mutual information and expectations
4. Apply SpARE edits with configurable parameters

**Main Experiment Command**:
```bash
python ./scripts/run_spare.py --model_path="meta-llama/Llama-2-7b-hf" \
  --data_name="nqswap" --layer_ids 12 13 14 15 --edit_degree=2.0
```

## SAE Implementation & Dependencies
- Adapted from **EleutherAI/sae** and **jbloomAus/SAELens** repositories
- Uses sparse auto-encoders to identify and manipulate knowledge-related activations

## Models & Datasets
- **Model**: Llama-2-7b (referenced in examples)
- **Dataset**: NQswap (knowledge conflict benchmark for ODQA evaluation)

## Key Configuration Parameters
- `layer_ids`: Target transformer layers (12-15 mentioned)
- `edit_degree`: Intervention magnitude (2.0 default)
- `select_topk_proportion`: SAE activation selection ratio (0.07)
- `seed`: Reproducibility control (42)

## Citation
The authors provide BibTeX entries for both the main paper and preliminary study on residual stream analysis under knowledge conflicts.
````

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "7cb5e404-9e3a-49cd-8744-6b79f307a195",
  "isSidechain": true,
  "promptId": "eee12e6f-4b22-4cb0-adff-def0ae050a12",
  "agentId": "ad05b8d9866c10448",
  "type": "user",
  "uuid": "2560195f-e541-4232-ad87-aded5ba79836",
  "sourceToolAssistantUUID": "7cb5e404-9e3a-49cd-8744-6b79f307a195",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "94d88260-dbbe-43d4-abc2-f8f5a7fda9d7",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 67 · 2026-05-30T06:22:00.262Z_

Now let me search for the related companion paper on residual stream analysis and try one more time to find any peer reviews.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2560195f-e541-4232-ad87-aded5ba79836",
  "isSidechain": true,
  "agentId": "ad05b8d9866c10448",
  "requestId": "req_011CbYGhvDmCEdTP9mjAxcnK",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "ad075bb5-80e2-446c-aa1f-585bf5e082d3",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "94d88260-dbbe-43d4-abc2-f8f5a7fda9d7",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UWXdtCqVxs2Rkxm28FPivZ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 931,
      "cache_creation_input_tokens": 1023,
      "cache_read_input_tokens": 44698,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1023,
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

_source line 68 · 2026-05-30T06:22:01.747Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_011rtK6Mp1QoGQQFtticS4e9`</summary>

```json
{
  "url": "https://arxiv.org/abs/2410.16090",
  "prompt": "Extract the abstract and key findings of this companion paper about residual stream analysis under knowledge conflicts. How does it relate to the SpARE paper?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ad075bb5-80e2-446c-aa1f-585bf5e082d3",
  "isSidechain": true,
  "agentId": "ad05b8d9866c10448",
  "requestId": "req_011CbYGhvDmCEdTP9mjAxcnK",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "145848f3-03a0-4d85-8055-c8157fe518b1",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "94d88260-dbbe-43d4-abc2-f8f5a7fda9d7",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UWXdtCqVxs2Rkxm28FPivZ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 931,
      "cache_creation_input_tokens": 1023,
      "cache_read_input_tokens": 44698,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1023,
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

_source line 69 · 2026-05-30T06:22:02.686Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01RxaSV6pdpF6BKaRG4cLWpu`</summary>

```json
{
  "query": "NAACL 2025 accepted papers list oral presentations SpARE knowledge conflict SAE reviews feedback"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "145848f3-03a0-4d85-8055-c8157fe518b1",
  "isSidechain": true,
  "agentId": "ad05b8d9866c10448",
  "requestId": "req_011CbYGhvDmCEdTP9mjAxcnK",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "af9d8a85-b099-429f-8c33-e39e62c19202",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "94d88260-dbbe-43d4-abc2-f8f5a7fda9d7",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UWXdtCqVxs2Rkxm28FPivZ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 931,
      "cache_creation_input_tokens": 1023,
      "cache_read_input_tokens": 44698,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1023,
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

_source line 70 · 2026-05-30T06:22:03.364Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01JfAyQ74RUUJd1RVvJc6JCq`</summary>

```json
{
  "query": "\"Steering Knowledge Selection\" SpARE criticism limitation polysemantic dense vector SAE monosemantic advantage"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "af9d8a85-b099-429f-8c33-e39e62c19202",
  "isSidechain": true,
  "agentId": "ad05b8d9866c10448",
  "requestId": "req_011CbYGhvDmCEdTP9mjAxcnK",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "dd5ac00b-4e7e-49c8-a9d2-034e9d127b65",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "94d88260-dbbe-43d4-abc2-f8f5a7fda9d7",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UWXdtCqVxs2Rkxm28FPivZ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 931,
      "cache_creation_input_tokens": 1023,
      "cache_read_input_tokens": 44698,
      "output_tokens": 252,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1023
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 931,
          "output_tokens": 252,
          "cache_read_input_tokens": 44698,
          "cache_creation_input_tokens": 1023,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1023,
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

_source line 71 · 2026-05-30T06:22:08.544Z_

<details><summary>↩ Tool result · `toolu_011rtK6Mp1QoGQQFtticS4e9`</summary>

```text
# Analysis of Residual Stream Paper (arXiv:2410.16090)

## Abstract Summary

This paper investigates how language models internally handle conflicts between parametric knowledge (stored in parameters) and contextual knowledge (from input). The researchers analyze the residual stream—the vector flowing through the model's layers—to detect when conflicts occur.

## Key Findings

The study demonstrates three main discoveries:

1. **Conflict Detection**: Models register knowledge conflict signals in their residual stream that can be detected through probing intermediate activations, "without modifying the input or model parameters."

2. **Predictable Patterns**: Different activation patterns emerge depending on whether the model relies on contextual versus parametric knowledge, enabling prediction of model behavior before answer generation.

3. **Practical Application**: These insights provide "a foundation for developing methods to control the knowledge selection processes."

## Relation to SpARE

Without access to the SpARE paper's content in your message, I cannot establish the specific connection. However, both papers likely share focus on:
- Understanding internal model mechanisms during knowledge conflicts
- Analyzing activation patterns to predict and potentially control model behavior
- Developing interpretability techniques for LLMs

If you provide SpARE's details, I can clarify their relationship more precisely.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "145848f3-03a0-4d85-8055-c8157fe518b1",
  "isSidechain": true,
  "promptId": "eee12e6f-4b22-4cb0-adff-def0ae050a12",
  "agentId": "ad05b8d9866c10448",
  "type": "user",
  "uuid": "1389c7bd-84c4-43d7-8749-05ec84f43d88",
  "sourceToolAssistantUUID": "145848f3-03a0-4d85-8055-c8157fe518b1",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "94d88260-dbbe-43d4-abc2-f8f5a7fda9d7",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 72 · 2026-05-30T06:22:09.783Z_

<details><summary>↩ Tool result · `toolu_01RxaSV6pdpF6BKaRG4cLWpu`</summary>

```text
Web search results for query: "NAACL 2025 accepted papers list oral presentations SpARE knowledge conflict SAE reviews feedback"

Links: [{"title":"Accepted Papers - NAACL-HLT 2025","url":"https://2025.naacl.org/program/accepted_papers/"},{"title":"[NAACL 2025] Second Call for Main Conference Papers | ACL Member Portal","url":"https://www.aclweb.org/portal/content/naacl-2025-second-call-main-conference-papers"},{"title":"NAACL 2025 Annual Conference of the Nations of the Americas Chapter of","url":"https://aclanthology.org/2025.naacl-short.0.pdf"},{"title":"NAACL 2025 – CL deadlines for Qualifying Papers | Computational Linguistics","url":"https://submissions.cljournal.org/index.php/cljournal/announcement/view/4"},{"title":"Second Call for Main Conference Papers - NAACL-HLT 2025","url":"https://2025.naacl.org/calls/papers/"},{"title":"Call for Industry Track Papers - NAACL-HLT 2025","url":"https://2025.naacl.org/calls/industry/"},{"title":"First Call for Papers: NAACL 2025 Main Conference | ACL Member Portal","url":"https://www.aclweb.org/portal/content/naacl-first-call-main-conference-papers"}]

Based on the search results, I found relevant information about NAACL 2025:

## NAACL 2025 Accepted Papers and Oral Presentations

Out of the 1,647 papers committed to NAACL with ARR reviews, 719 were accepted to the main conference, and 477 were accepted to Findings.

### Oral Presentations

246 of the papers accepted to the main conference were selected as oral presentations, with the rest assigned as posters. Oral presentations were assigned a 15-minute slot, with 12 minutes for presentation and 3 minutes for questions.

246 papers are to be presented as oral presentations (also including papers from TACL, CL, and the industry track), 594 papers are scheduled as in-person posters, and 256 virtual posters.

### Selection Criteria

For choosing papers as oral presentations, papers were split according to track, sorted according to overall score (considering review, metareview, SAC recommendation), and authors' considerations were taken into account.

You can access the full list of accepted papers at the official NAACL 2025 website: https://2025.naacl.org/program/accepted_papers/

However, the search results don't contain specific information about papers on "SpARE" or "knowledge conflict" topics, or details about SAE reviews and feedback mechanisms that you mentioned in your query.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "af9d8a85-b099-429f-8c33-e39e62c19202",
  "isSidechain": true,
  "promptId": "eee12e6f-4b22-4cb0-adff-def0ae050a12",
  "agentId": "ad05b8d9866c10448",
  "type": "user",
  "uuid": "59f72e69-bfe2-4ee0-ba8c-8c2b3fd0c63e",
  "sourceToolAssistantUUID": "af9d8a85-b099-429f-8c33-e39e62c19202",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "94d88260-dbbe-43d4-abc2-f8f5a7fda9d7",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 73 · 2026-05-30T06:22:10.607Z_

<details><summary>↩ Tool result · `toolu_01JfAyQ74RUUJd1RVvJc6JCq`</summary>

```text
Web search results for query: ""Steering Knowledge Selection" SpARE criticism limitation polysemantic dense vector SAE monosemantic advantage"

Links: [{"title":"Steering Knowledge Selection Behaviours in LLMs via SAE-Based Representation Engineering","url":"https://arxiv.org/html/2410.15999v1"},{"title":"Steering Knowledge Selection Behaviours in LLMs via SAE-Based Representation Engineering","url":"https://www.rohan-paul.com/p/steering-knowledge-selection-behaviours"},{"title":"Steering Knowledge Selection Behaviours in LLMs","url":"https://arxiv.org/pdf/2410.15999"},{"title":"[Quick Review] Steering Knowledge Selection Behaviours in LLMs via SAE-Based Representation Engineering","url":"https://liner.com/review/steering-knowledge-selection-behaviours-in-llms-via-saebased-representation-engineering"},{"title":"[Literature Review] Steering Knowledge Selection Behaviours in LLMs via SAE-Based Representation Engineering","url":"https://www.themoonlight.io/en/review/steering-knowledge-selection-behaviours-in-llms-via-sae-based-representation-engineering"},{"title":"Steering Knowledge Selection Behaviours in LLMs via ...","url":"https://aclanthology.org/anthology-files/anthology-files/pdf/naacl/2025.naacl-long.264.pdf"},{"title":"[2410.15999] Steering Knowledge Selection Behaviours in LLMs via SAE-Based Representation Engineering","url":"https://arxiv.org/abs/2410.15999"},{"title":"Steering Knowledge Selection Behaviours in LLMs via SAE-Based Representation Engineering - ACL Anthology","url":"https://aclanthology.org/2025.naacl-long.264/"}]

I found relevant results about "Steering Knowledge Selection Behaviours in LLMs via SAE-Based Representation Engineering." Here's what the search revealed:

## Overview

SpARE is a Sparse Auto-Encoder-based Representation Engineering method to steer the knowledge selection behavior of LLMs. SpARE is a training-free representation engineering method that uses pre-trained sparse auto-encoders (SAEs) to control the knowledge selection behaviour of LLMs.

## Key Advantage Over Dense Vector Approaches

The research addresses a critical limitation of existing methods. Existing representation engineering methods inadequately steer knowledge usage because they modify polysemantic dense vectors, making precise adjustments difficult. More specifically, these activations are polysemantic dense vectors that overlap with many independent semantic features, and minor edits in one dimension can influence multiple semantic features, making it difficult to adjust activations accurately without affecting other features in practice.

## SpARE's Solution Using SAEs

Unlike existing representation engineering methods that directly modify polysemantic dense vectors, SpARE uses SAEs to decompose them into monosemantic features for more precise editing. Sparse auto-encoders (SAEs) have been proposed to address the difficulty of interpreting polysemantic activations by decomposing them into a large-scale monosemantic feature dictionary.

## Performance Results

SpARE can effectively control the usage of either knowledge source to resolve knowledge conflict in open-domain question-answering tasks, surpassing existing representation engineering methods (+10%) as well as contrastive decoding methods (+15%).


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "dd5ac00b-4e7e-49c8-a9d2-034e9d127b65",
  "isSidechain": true,
  "promptId": "eee12e6f-4b22-4cb0-adff-def0ae050a12",
  "agentId": "ad05b8d9866c10448",
  "type": "user",
  "uuid": "b4122b26-cdde-4a49-81c5-0d1ca51389a5",
  "sourceToolAssistantUUID": "dd5ac00b-4e7e-49c8-a9d2-034e9d127b65",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "94d88260-dbbe-43d4-abc2-f8f5a7fda9d7",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 74 · 2026-05-30T06:23:58.873Z_

I now have comprehensive information. Let me compile the thorough research report.

---

## Thorough Research Report: SpARE (Zhao et al., NAACL 2025 Oral)

**"Steering Knowledge Selection Behaviours in LLMs via SAE-Based Representation Engineering"**
Authors: Yu Zhao, Alessio Devoto, Giwon Hong, Xiaotang Du, Aryo Pradipta Gema, Hongru Wang, Xuanli He, Kam-Fai Wong, Pasquale Minervini
Institutions: University of Edinburgh, CUHK, Sapienza Rome, UCL, Miniml.AI
Published: NAACL 2025 Long Papers (Oral), pages 5117-5136. [ACL Anthology](https://aclanthology.org/2025.naacl-long.264/)

---

### 1. THE EXACT PROBLEM GAP AND HOW THEY IDENTIFIED IT

**The gap:** Existing representation engineering methods (ActAdd, TaskVec, SEA) *fail* to effectively steer knowledge selection in LLMs when context-memory knowledge conflicts occur. The authors diagnosed WHY: these methods directly edit polysemantic dense vectors (hidden states, MLP activations), where "minor edits in one dimension can influence multiple semantic features, making it difficult to adjust activations accurately without affecting other features." This is the polysemanticity problem applied specifically to the knowledge conflict steering task.

**How they identified it:** They performed a systematic two-phase investigation:

**Phase 1 -- Conflict Detection via Linear Probing (Section 3):** They created two data groups: D_EM (question + concordant evidence, no conflict) and D_EC (question + conflicting evidence, conflict present). They trained logistic regression probes on activations at every layer across hidden states, MLP outputs, and self-attention outputs. Key finding: **conflict signals peak at mid-layers** (AUROC increases from layer 1 to mid-layers, then decreases). MLP and self-attention modules stop adding conflict signal in later layers. This probing was done on Llama2-7B and Gemma2-9B using NQSwap data.

**Phase 2 -- Failure analysis of baselines:** They empirically showed existing representation engineering baselines (ActAdd, TaskVec, SEA) produce poor results because they operate on entangled dense vectors. This motivated the SAE decomposition.

---

### 2. THE KEY INSIGHT OTHERS MISSED

The central insight has two parts:

1. **Behavioral decomposition via SAEs:** A *small* set of monosemantic SAE features (less than 0.05% of all SAE activations for Gemma2-9B across 6 layers) controls the entire knowledge selection behavior. Prior work treated steering as operating on full activation vectors; this paper shows the relevant signal is extremely sparse in the SAE feature space.

2. **Input-dependent, constrained editing:** Rather than applying a static steering vector (as ActAdd/TaskVec do), SpARE computes input-specific edit magnitudes with explicit non-negativity and ceiling constraints. The ablation study proved this is critical -- input-independent editing "fails to steer the usage of knowledge," and remove-only editing produces zero accuracy on both metrics. Every component is necessary.

3. **Edit in residual stream space, not SAE space:** They crucially avoid reconstructing h' = g_phi(z') because (a) SAE reconstruction loss destroys information, yielding "nearly zero accuracy," and (b) SAE activations must be non-negative, preventing flexible alpha scaling. Instead, they use the SAE decoder columns as feature directions and add/subtract them from the original hidden state h.

---

### 3. HOW THEY FORMULATED THE PROBLEM DIFFERENTLY

Prior work on knowledge conflicts used:
- **Fine-tuning/prompting** (Wang et al. 2023): requires additional model interactions, high latency
- **Contrastive decoding** (DoLa, CAD): operates at the output/logit level, needs extra forward passes
- **Standard representation engineering** (ActAdd, SEA): treats activations as monolithic vectors

SpARE reformulates the problem as: **identifying a sparse functional feature mask in the SAE activation space that separates contextual-knowledge-favoring features from parametric-knowledge-favoring features, then performing targeted additive/subtractive editing in the residual stream using those feature directions.**

The formal problem setup uses the tuple (Q, E_M, M, E_C, C) where Q is the question, E_M is concordant evidence, E_C is conflicting evidence, M is the parametric answer, and C is the contextual answer. They steer the model to produce either M or C on demand.

---

### 4. EXISTING TECHNIQUES ADAPTED/COMBINED

SpARE is a synthesis of four building blocks:

1. **Sparse Autoencoders** (Bricken et al. 2023, Huben et al. 2024, Gao et al. 2024): Used off-the-shelf pre-trained SAEs (EleutherAI/sae for Llama3-8B, Google gemma-scope for Gemma2-9B) plus their own trained SAE for Llama2-7B. The SAE provides the monosemantic decomposition: f_theta(h) = sigma(W_theta(h-b) + b_theta) = z, and g_phi(z) = W_phi * z + b.

2. **Representation Engineering** (Turner et al. 2023, Zou et al. 2023): The general framework of editing activations at inference time. SpARE inherits this paradigm but improves the precision of editing via SAE features.

3. **Contrastive/Task Vector methods** (Hendel et al. 2023, Todd et al. 2024): The idea that behavioral differences can be captured by contrasting activations from different behavioral conditions. SpARE extends this by doing the contrast in SAE space rather than dense space.

4. **Mutual Information-based feature selection:** They use I(Z_i; Y) to select the top-k SAE activations most dependent on the knowledge selection outcome Y in {C, M}. This is a well-known statistical feature selection technique applied in a novel context.

---

### 5. TECHNICAL METHOD IN FULL DETAIL

**Step 1 -- Collect behavioral activations:** From conflicting instances D_EC, partition by model predictions into D_C (model chose context) and D_M (model chose parametric). Collect N hidden states at the last input position from each group. Encode through SAE to get z_C^j and z_M^j. Compute means z_bar_C and z_bar_M.

**Step 2 -- Identify functional features via mutual information:** For each SAE dimension i, compute I(Z_i; Y) where Y in {C, M}. Select top-k by MI. For each selected feature, determine correlation direction: if E_C[Z_i] - E_M[Z_i] > 0, feature is contextual; else parametric. Construct orthogonal functional vectors z_C (contextual features only, values from z_bar_C, rest zeroed) and z_M (parametric features only, values from z_bar_M, rest zeroed).

**Step 3 -- Constrained input-dependent editing:** For a given input h with SAE activation z = f_theta(h):
- **Remove undesired features (Eq. 2):** z_i^- = min{z_i, z_Ci} (removes at most z_i to keep non-negative)
- **Add desired features (Eq. 3):** z_i^+ = max{z_Mi - z_i, 0} (adds up to z_Mi, no excess)
- **Edit hidden state (Eq. 4):** h' = h + alpha * (-g_phi(z^-) + g_phi(z^+))

Alpha is a scalar controlling edit strength. The edits are applied through the SAE decoder columns (feature directions) but added to the original h, avoiding reconstruction loss.

**Hyperparameters:**
- Layers: 12-15 (Llama2-7B), 13-16 (Llama3-8B), 23-25 + 29-31 (Gemma2-9B)
- select_topk_proportion: 0.07 (top 7% of SAE features by MI)
- edit_degree (alpha): 2.0 default
- Editing applied at last token position only

---

### 6. MAIN RESULTS (EXACT NUMBERS)

**NQSwap dataset -- Steering to Parametric Knowledge (EM_M):**
| Method | Llama3-8B | Llama2-7B | Gemma2-9B |
|--------|-----------|-----------|-----------|
| No control | 26.63 | 22.23 | 26.32 |
| ActAdd | 37.87 | 31.43 | 27.67 |
| CAD | 33.72 | 31.23 | 41.17 |
| ICL | 43.73 | 31.67 | 43.10 |
| **SpARE** | **47.51** | **43.76** | **44.11** |

**NQSwap dataset -- Steering to Contextual Knowledge (EM_C):**
| Method | Llama3-8B | Llama2-7B | Gemma2-9B |
|--------|-----------|-----------|-----------|
| No control | 42.69 | 41.67 | 45.96 |
| SEA_SqExp | 57.08 | 48.04 | 61.45 |
| CAD | 65.65 | 54.69 | 63.10 |
| ICL | 73.35 | 63.33 | 70.19 |
| **SpARE** | **77.69** | **69.32** | **73.78** |

SpARE beats all baselines on both directions across all models and both datasets. The advantage is most pronounced for parametric steering, where contrastive decoding methods particularly struggle.

---

### 7. ABLATION FINDINGS

Three ablation variants, all critically degraded:
1. **Input-independent:** Using z_C and z_M directly without computing input-specific z^- and z^+ -- "fails to steer," performance near uncontrolled baseline. This proves the min/max constraints in Eq. 2-3 are essential.
2. **Remove only:** Only subtracts contextual features -- produces **zero accuracy** on both EM_M and EM_C. The model cannot generate coherent answers.
3. **Add only:** Only adds parametric features -- **worse than no control**. Shows both addition and removal are required for effective steering.

---

### 8. KEY ANALYSIS FINDINGS

**Layer analysis:** Steering is most effective at mid-layers, precisely where conflict probing AUROC is highest. This validates the detect-then-intervene paradigm.

**Residual stream analysis after steering:** When steering toward parametric knowledge, the conflict probe AUROC drops immediately (conflict signal fades). When steering toward contextual knowledge, probe AUROC increases. This confirms SpARE is genuinely reshaping internal representations.

**Skewness/Kurtosis pattern:** Contextual knowledge selection produces significantly more skewed residual stream representations than parametric selection, starting from layer 19 (in Llama3-8B). SpARE's steering reproduces these natural patterns -- an indirect validation that the method operates through the same mechanisms the model naturally uses.

---

### 9. LIMITATIONS AND OPEN QUESTIONS

The authors acknowledge:
1. **SAE dependency:** Requires pre-trained SAEs, which may not be available for all models. (They trained their own for Llama2-7B to partially address this.)
2. **Task scope:** Only evaluated on ODQA (NQSwap, Macnoise). Unclear generalization to complex reasoning, multi-hop QA, or long-form generation.
3. **Binary knowledge selection:** Real-world knowledge integration is rarely binary (context vs. parametric). More nuanced approaches may be needed, "such as using another model as a critic."
4. **No safety evaluation:** The ability to steer away from context could be misused (e.g., ignoring safety-relevant context).
5. **Unexplained representation patterns:** They observe the skewness phenomenon but leave causal explanation to future work.

**Additional open questions I identify:**
- Scalability to larger models (only tested on 7B-9B)
- Whether the MI-based feature selection transfers across domains/datasets
- How robust the method is to SAE quality (reconstruction loss, feature completeness)
- Whether this generalizes to non-factual behaviors (e.g., style, reasoning strategies)

---

### 10. REVIEWER FEEDBACK

**NAACL 2025 reviews were not publicly accessible** on OpenReview at the time of search. NAACL 2025 used ARR (ACL Rolling Review), and the OpenReview forums for individual papers are typically not publicly visible. However:

- The paper was selected as an **oral presentation** (246 out of 719 accepted papers), indicating it received strong reviewer scores. Oral selection was based on "overall score (considering review, metareview, SAC recommendation)."
- The paper appears on the NAACL 2025 accepted papers list at `2025.naacl.org/program/accepted_papers/`.
- Community reception: 81 GitHub stars, 9 forks. HuggingFace paper page exists. Multiple third-party review summaries (Liner, Moonlight, Rohan Paul blog) characterize the work positively.

**Likely reviewer praise** (inferred from oral status and method quality):
- Clean, well-motivated three-step pipeline
- Strong empirical results across 3 models, 2 datasets
- Thorough ablation proving all components necessary
- Novel combination of SAEs with representation engineering
- Training-free (no fine-tuning required)

**Likely reviewer concerns** (inferred from limitations and standard ML reviewing):
- Narrow evaluation scope (ODQA only)
- Dependence on pre-trained SAE availability
- The 7% top-k proportion and alpha=2.0 are tuned per setting; how sensitive is performance?
- No evaluation on larger models (70B+)

---

### 11. BUILDING BLOCKS (REUSABLE METHODS/TOOLS/DATASETS)

**Reusable components from this work:**

1. **MI-based SAE feature selection pipeline:** The mutual information approach to identify which SAE features drive a specific behavior is generalizable to any behavioral steering task.

2. **Constrained input-dependent SAE editing (Eq. 2-4):** The min/max clipping + residual-stream-space editing pattern can be applied to other SAE-based steering problems (safety, style, etc.).

3. **Conflict detection probing methodology:** Linear probing across layers/activation types to find where behavioral signals peak -- reusable for any mechanistic investigation.

4. **Datasets:** NQSwap (Longpre et al., 2021) and Macnoise (Hong et al., 2024) for knowledge conflict evaluation.

5. **Pre-trained SAEs shared on HuggingFace:**
   - `yuzhaouoe/Llama2-7b-SAE` (their own trained SAE)
   - `EleutherAI/sae-llama-3-8b-32x`
   - `google/gemma-scope-9b-pt-res`

6. **Open-source code:** `github.com/yuzhaouoe/SAE-based-representation-engineering` (MIT license, Python, adapted from EleutherAI/sae and SAELens).

7. **Companion paper:** "Analysing the Residual Stream of Language Models Under Knowledge Conflicts" (arXiv 2410.16090) provides deeper analysis of the residual stream patterns (skewness, probing) that underpin SpARE.

---

### 12. HOW THEY INNOVATE (SYNTHESIS)

The core innovation of SpARE is **not** inventing SAEs, representation engineering, or mutual information -- it is the **precise combination and adaptation** of these tools to solve a specific failure mode. The innovation chain is:

1. **Diagnosis:** Identify that polysemanticity is why existing RepEng fails at knowledge steering (not just that it fails, but *why*).
2. **Bridge:** Recognize SAEs solve exactly this polysemanticity problem by providing monosemantic decomposition.
3. **Selection:** Use MI to find the needle-in-a-haystack (0.05% of features) rather than using all SAE features.
4. **Constrained editing:** Design input-dependent, bounded edits that respect SAE activation properties (non-negativity) while operating in the more forgiving residual stream space.
5. **Validation:** Show the method works through the model's own natural mechanisms (skewness patterns match, probing confirms representation changes).

This is a clean example of "problem-driven method design" where every technical choice is motivated by a specific observed failure or constraint.

Sources:
- [arXiv paper](https://arxiv.org/abs/2410.15999)
- [ACL Anthology page](https://aclanthology.org/2025.naacl-long.264/)
- [Full HTML paper](https://arxiv.org/html/2410.15999v3)
- [GitHub repository](https://github.com/yuzhaouoe/SAE-based-representation-engineering)
- [HuggingFace paper page](https://huggingface.co/papers/2410.15999)
- [HuggingFace model collection](https://huggingface.co/collections/yuzhaouoe/sae-based-representation-engineering)
- [Rohan Paul blog analysis](https://www.rohan-paul.com/p/steering-knowledge-selection-behaviours)
- [Companion paper on residual streams](https://arxiv.org/abs/2410.16090)
- [NAACL 2025 accepted papers](https://2025.naacl.org/program/accepted_papers/)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b4122b26-cdde-4a49-81c5-0d1ca51389a5",
  "isSidechain": true,
  "agentId": "ad05b8d9866c10448",
  "requestId": "req_011CbYGiuPBc3rj3WDkoH8u4",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "f39eb415-f38a-4f55-82fd-14bf8d5bf5f8",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "94d88260-dbbe-43d4-abc2-f8f5a7fda9d7",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Wb3zo19UCDgWF9YKHcJy2L",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3046,
      "cache_read_input_tokens": 45721,
      "output_tokens": 4381,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 3046
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 4381,
          "cache_read_input_tokens": 45721,
          "cache_creation_input_tokens": 3046,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 3046,
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
