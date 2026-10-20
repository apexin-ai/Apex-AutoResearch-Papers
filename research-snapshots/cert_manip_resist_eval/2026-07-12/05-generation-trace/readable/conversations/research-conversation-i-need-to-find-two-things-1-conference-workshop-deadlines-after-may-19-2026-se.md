# Research conversation: I need to find two things: ## 1. Conference/Workshop Deadlines After May 19, 2026 Search for submission deadlines for th

**The Weakest Link Across Panel Sizes: Predictor Relevance Patterns in Multi-Judge LLM Evaluation under Adversarial Manipulation (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 87
- **Recorded user turns:** 1
- **Tool calls:** 39
- **Original source:** `logs/chats/exported-trajectories/account-2/agent-ac3625b267e3eea76.jsonl`
- **Structured JSON:** [`2034b3690c693f8096a0.json`](../../sessions/20/2034b3690c693f8096a0.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

87 recorded events

### User

_source line 1 · 2026-05-19T19:09:15.874Z_

I need to find two things:

## 1. Conference/Workshop Deadlines After May 19, 2026

Search for submission deadlines for these NLP/ML venues that are AFTER May 19, 2026:

- EMNLP 2026 deadline
- ACL 2026 deadline (main conference and ARR)
- NAACL 2026 deadline
- COLING 2026 deadline
- NeurIPS 2026 deadline
- ICML 2026 deadline
- ICLR 2027 deadline
- EACL 2027 deadline
- AfricaNLP 2027 workshop deadline
- LREC-COLING 2026 deadline
- WMT 2026 deadline
- Any relevant multilingual NLP workshops in 2026-2027

For each, search "[venue name] 2026 submission deadline" or "[venue name] 2027 call for papers". Report the exact deadline dates. Only include venues whose deadline is AFTER 2026-05-19.

## 2. Existing Implementations

Search GitHub for:
- "token tax multilingual" implementation
- "causal mediation analysis NLP" code
- "tokenization fertility" measurement code
- "AfriMMLU" evaluation code
- "regression discontinuity tokenization" code
- "selective translation multilingual" code

Report what implementations exist that could be reused.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "504e2971-a17d-4553-9508-335bf1f3968f",
  "agentId": "ac3625b267e3eea76",
  "type": "user",
  "uuid": "6fc9ec71-c891-4181-8a24-4e395ae8fd82",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "072a3a1a-465c-4992-a530-3e78def2ac5a",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 2 · 2026-05-19T19:09:15.877Z_

```json
{
  "parentUuid": "6fc9ec71-c891-4181-8a24-4e395ae8fd82",
  "isSidechain": true,
  "agentId": "ac3625b267e3eea76",
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
  "uuid": "4b785c07-6411-4db7-92f7-53d3031ba948",
  "timestamp": "2026-05-19T19:09:15.877Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "072a3a1a-465c-4992-a530-3e78def2ac5a",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 3 · 2026-05-19T19:09:15.877Z_

```json
{
  "parentUuid": "4b785c07-6411-4db7-92f7-53d3031ba948",
  "isSidechain": true,
  "agentId": "ac3625b267e3eea76",
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "e5b62576-1967-424b-b2e1-c9cb5b6c64a0",
  "timestamp": "2026-05-19T19:09:15.877Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "072a3a1a-465c-4992-a530-3e78def2ac5a",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Assistant

_source line 4 · 2026-05-19T19:09:18.858Z_



I'll search for both conference deadlines and existing implementations. Let me start by fetching the WebSearch tool schema, then run all searches in parallel.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e5b62576-1967-424b-b2e1-c9cb5b6c64a0",
  "isSidechain": true,
  "agentId": "ac3625b267e3eea76",
  "requestId": "req_011CbCTKZA5jHTA6oJvSz3VU",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "6d22e602-4185-4713-a02f-811fba11136f",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "072a3a1a-465c-4992-a530-3e78def2ac5a",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01R2cuPiuQvc8aYSRtVEjQgf",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1676,
      "cache_read_input_tokens": 7773,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1676,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 6,
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

_source line 5 · 2026-05-19T19:09:19.389Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_017fbMzPaVprTnbQFuHCAe5E`</summary>

```json
{
  "query": "select:WebSearch",
  "max_results": 1
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6d22e602-4185-4713-a02f-811fba11136f",
  "isSidechain": true,
  "agentId": "ac3625b267e3eea76",
  "requestId": "req_011CbCTKZA5jHTA6oJvSz3VU",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "4d04457a-2f31-49d4-addc-d61645d3e2b0",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "072a3a1a-465c-4992-a530-3e78def2ac5a",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01R2cuPiuQvc8aYSRtVEjQgf",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1676,
      "cache_read_input_tokens": 7773,
      "output_tokens": 108,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1676
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 108,
          "cache_read_input_tokens": 7773,
          "cache_creation_input_tokens": 1676,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1676,
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

_source line 6 · 2026-05-19T19:09:19.392Z_

<details><summary>↩ Tool result · `toolu_017fbMzPaVprTnbQFuHCAe5E`</summary>

````text
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
  "parentUuid": "4d04457a-2f31-49d4-addc-d61645d3e2b0",
  "isSidechain": true,
  "promptId": "504e2971-a17d-4553-9508-335bf1f3968f",
  "agentId": "ac3625b267e3eea76",
  "type": "user",
  "uuid": "49ddc0da-8379-4c30-b011-8ab571bb7aa5",
  "sourceToolAssistantUUID": "4d04457a-2f31-49d4-addc-d61645d3e2b0",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "072a3a1a-465c-4992-a530-3e78def2ac5a",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 7 · 2026-05-19T19:09:21.892Z_



Now let me run all the searches in parallel - both conference deadlines and GitHub implementations.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "49ddc0da-8379-4c30-b011-8ab571bb7aa5",
  "isSidechain": true,
  "agentId": "ac3625b267e3eea76",
  "requestId": "req_011CbCTKpAiur3LNd8bAsuGk",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "bae59a92-fcf8-4174-8911-e3b95d44b9b3",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "072a3a1a-465c-4992-a530-3e78def2ac5a",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013JsML3W9nx3HR8QbaqRGVP",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 638,
      "cache_read_input_tokens": 9449,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 638,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 2,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": {
      "cache_miss_reason": {
        "type": "unavailable"
      }
    }
  }
}
```

</details>

---

### Tool call

_source line 8 · 2026-05-19T19:09:22.238Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_017YVRbueT8euzux9DQ1RFpX`</summary>

```json
{
  "query": "EMNLP 2026 submission deadline call for papers"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "bae59a92-fcf8-4174-8911-e3b95d44b9b3",
  "isSidechain": true,
  "agentId": "ac3625b267e3eea76",
  "requestId": "req_011CbCTKpAiur3LNd8bAsuGk",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "c35c0f26-474c-4596-859c-29fcc6f97e65",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "072a3a1a-465c-4992-a530-3e78def2ac5a",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013JsML3W9nx3HR8QbaqRGVP",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 638,
      "cache_read_input_tokens": 9449,
      "output_tokens": 85,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 638
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 85,
          "cache_read_input_tokens": 9449,
          "cache_creation_input_tokens": 638,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 638,
            "ephemeral_1h_input_tokens": 0
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": {
      "cache_miss_reason": {
        "type": "unavailable"
      }
    }
  }
}
```

</details>

---

### Tool result

_source line 9 · 2026-05-19T19:09:29.882Z_

<details><summary>↩ Tool result · `toolu_017YVRbueT8euzux9DQ1RFpX`</summary>

```text
Web search results for query: "EMNLP 2026 submission deadline call for papers"

Links: [{"title":"Call for Main Conference Papers - EMNLP 2026","url":"https://2026.emnlp.org/calls/main_conference_papers/"},{"title":"EMNLP 2026 Call for Papers — Official Deadlines & Important Dates | PaperPilot","url":"https://www.getpaperpilot.com/deadlines/emnlp-2026.html"},{"title":"EMNLP 2026 on X: \"📢 The First Call for Papers for EMNLP 2026 is officially out! 📝 We welcome long &amp; short papers featuring original research on empirical methods for NLP. 🗓️ ARR Submission Deadline: May 25, 2026 🔗 Read the full CFP here: https://t.co/GU2kaISjUG #EMNLP2026\" / X","url":"https://x.com/emnlpmeeting/status/2029508292637061462"},{"title":"emnlp 2026 - AI Conference Deadlines","url":"https://mlciv.com/ai-deadlines/conference/?id=emnlp26"},{"title":"EMNLP 2026 : The 2026 Conference on Empirical Methods in N","url":"https://callforpaper.org/call-for-papers-emnlp-2026"},{"title":"EMNLP 2026 on X: \"📢 Please note a critical update to the original #EMNLP2026 Call for Papers: since EMNLP and AACL share the ARR May cycle, authors will need to explicitly select a target conference at submission time. This choice will be binding! For more details see: https://t.co/0u1wbX9fT6\" / X","url":"https://x.com/emnlpmeeting/status/2047754845919031450"},{"title":"Call for workshops: EMNLP & AACL","url":"https://groups.google.com/g/ml-news/c/W-fucfhVto4"},{"title":"EMNLP 2026 Conference | OpenReview","url":"https://openreview.net/group?id=EMNLP%2F2026%2FConference"},{"title":"Update EMNLP 2026 conference dates and deadlines · huggingface/ai-deadlines at 2754f67","url":"https://huggingface.co/spaces/huggingface/ai-deadlines/commit/2754f67c0550847973789522a0a082dd5443b5c0"},{"title":"2026 *ACL Conference Dates | Computational Linguistics","url":"https://submissions.cljournal.org/index.php/cljournal/announcement/view/14"}]

Based on the search results, here's the information about EMNLP 2026 submission deadline and call for papers:

## Key Submission Details

The EMNLP 2026 submission deadline is May 25, 2026, with all deadlines at 11:59PM UTC-12:00 ("anywhere on Earth").

## Important Dates

Key dates include the ARR submission deadline for long & short papers on May 25, 2026, and the reviewer registration deadline for all authors on May 27, 2026. Additional milestones include author response and author-reviewer discussion from July 7-13, 2026, and meta review release on July 30, 2026.

## Conference Details

EMNLP 2026 will be held in Budapest, Hungary from October 24-29, 2026.

## Paper Submission Guidelines

EMNLP 2026 invites the submission of long and short papers featuring substantial, original, and unpublished research on empirical methods for Natural Language Processing. The conference welcomes papers contributing negative findings, surveys, new resources, positions, novel linguistic insights, and reproductions (or failures to reproduce) of previous results.

## Important Policy Note

Authors submitting to the ARR 2026 May cycle that is aligned with both EMNLP and AACL must explicitly declare their target conference at submission time, and this choice will be binding for EMNLP 2026.

For the full call for papers, you can visit https://2026.emnlp.org/.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c35c0f26-474c-4596-859c-29fcc6f97e65",
  "isSidechain": true,
  "promptId": "504e2971-a17d-4553-9508-335bf1f3968f",
  "agentId": "ac3625b267e3eea76",
  "type": "user",
  "uuid": "83056e5a-b6f2-40cb-b3be-70cbee3f9624",
  "sourceToolAssistantUUID": "c35c0f26-474c-4596-859c-29fcc6f97e65",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "072a3a1a-465c-4992-a530-3e78def2ac5a",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 10 · 2026-05-19T19:09:32.941Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01YBpYd7sVjsRnCidBK6bjSg`</summary>

```json
{
  "query": "ACL 2026 submission deadline ARR call for papers"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "83056e5a-b6f2-40cb-b3be-70cbee3f9624",
  "isSidechain": true,
  "agentId": "ac3625b267e3eea76",
  "requestId": "req_011CbCTLb1EgsXwSYdQ558wU",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "66c4c6e1-807c-4a92-b436-8d2504519ad6",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "072a3a1a-465c-4992-a530-3e78def2ac5a",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0145QjQ96v2B8YcgHwHmsCQK",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1823,
      "cache_read_input_tokens": 9449,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1823,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 64,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": {
      "cache_miss_reason": {
        "type": "previous_message_not_found"
      }
    }
  }
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-19T19:09:33.044Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_0158PVWf3E2grb8Vy9MyX2K3`</summary>

```json
{
  "query": "NAACL 2026 submission deadline call for papers"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "66c4c6e1-807c-4a92-b436-8d2504519ad6",
  "isSidechain": true,
  "agentId": "ac3625b267e3eea76",
  "requestId": "req_011CbCTLb1EgsXwSYdQ558wU",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "06a52cee-0058-427f-a650-b91bd79dc870",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "072a3a1a-465c-4992-a530-3e78def2ac5a",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0145QjQ96v2B8YcgHwHmsCQK",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1823,
      "cache_read_input_tokens": 9449,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1823,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 64,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": {
      "cache_miss_reason": {
        "type": "previous_message_not_found"
      }
    }
  }
}
```

</details>

---

### Tool call

_source line 12 · 2026-05-19T19:09:33.338Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_012btvz9FL51HAPhX23GD8cM`</summary>

```json
{
  "query": "COLING 2026 submission deadline call for papers"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "06a52cee-0058-427f-a650-b91bd79dc870",
  "isSidechain": true,
  "agentId": "ac3625b267e3eea76",
  "requestId": "req_011CbCTLb1EgsXwSYdQ558wU",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "68dd15bb-1043-4b39-acb0-832292f08b9f",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "072a3a1a-465c-4992-a530-3e78def2ac5a",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0145QjQ96v2B8YcgHwHmsCQK",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1823,
      "cache_read_input_tokens": 9449,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1823,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 64,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": {
      "cache_miss_reason": {
        "type": "previous_message_not_found"
      }
    }
  }
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-19T19:09:33.815Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01ALdMB9bLWBL4XR4TdNV25S`</summary>

```json
{
  "query": "NeurIPS 2026 submission deadline call for papers"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "68dd15bb-1043-4b39-acb0-832292f08b9f",
  "isSidechain": true,
  "agentId": "ac3625b267e3eea76",
  "requestId": "req_011CbCTLb1EgsXwSYdQ558wU",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "82dc3f6e-cc5d-4228-aca3-b07cd12a00ce",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "072a3a1a-465c-4992-a530-3e78def2ac5a",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0145QjQ96v2B8YcgHwHmsCQK",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1823,
      "cache_read_input_tokens": 9449,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1823,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 64,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": {
      "cache_miss_reason": {
        "type": "previous_message_not_found"
      }
    }
  }
}
```

</details>

---

### Tool call

_source line 14 · 2026-05-19T19:09:33.846Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01GRjbkiWCwkTDf1dK2igTMM`</summary>

```json
{
  "query": "ICML 2026 submission deadline call for papers"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "82dc3f6e-cc5d-4228-aca3-b07cd12a00ce",
  "isSidechain": true,
  "agentId": "ac3625b267e3eea76",
  "requestId": "req_011CbCTLb1EgsXwSYdQ558wU",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "fdb12882-e11a-46da-aaec-2e5250d14e61",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "072a3a1a-465c-4992-a530-3e78def2ac5a",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0145QjQ96v2B8YcgHwHmsCQK",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1823,
      "cache_read_input_tokens": 9449,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1823,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 64,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": {
      "cache_miss_reason": {
        "type": "previous_message_not_found"
      }
    }
  }
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-19T19:09:34.344Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01PZAnjSMC2MHyArd5kF2Z1Y`</summary>

```json
{
  "query": "ICLR 2027 submission deadline call for papers"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "fdb12882-e11a-46da-aaec-2e5250d14e61",
  "isSidechain": true,
  "agentId": "ac3625b267e3eea76",
  "requestId": "req_011CbCTLb1EgsXwSYdQ558wU",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "527fb5c2-1ed0-420a-828d-ce7df0cd5758",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "072a3a1a-465c-4992-a530-3e78def2ac5a",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0145QjQ96v2B8YcgHwHmsCQK",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1823,
      "cache_read_input_tokens": 9449,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1823,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 64,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": {
      "cache_miss_reason": {
        "type": "previous_message_not_found"
      }
    }
  }
}
```

</details>

---

### Tool call

_source line 16 · 2026-05-19T19:09:34.757Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01TFc6NQKAPPnVrjc3S6Y4v1`</summary>

```json
{
  "query": "EACL 2027 submission deadline call for papers"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "527fb5c2-1ed0-420a-828d-ce7df0cd5758",
  "isSidechain": true,
  "agentId": "ac3625b267e3eea76",
  "requestId": "req_011CbCTLb1EgsXwSYdQ558wU",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "310d4ae3-4a0e-45f4-b03e-5d569f17d139",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "072a3a1a-465c-4992-a530-3e78def2ac5a",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0145QjQ96v2B8YcgHwHmsCQK",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1823,
      "cache_read_input_tokens": 9449,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1823,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 64,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": {
      "cache_miss_reason": {
        "type": "previous_message_not_found"
      }
    }
  }
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-19T19:09:35.252Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_0113WMWkbX15Ms3WLvwGb9nC`</summary>

```json
{
  "query": "AfricaNLP 2027 workshop submission deadline"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "310d4ae3-4a0e-45f4-b03e-5d569f17d139",
  "isSidechain": true,
  "agentId": "ac3625b267e3eea76",
  "requestId": "req_011CbCTLb1EgsXwSYdQ558wU",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "8a5c6cd4-6489-4aa6-ae75-6975c2262ec8",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "072a3a1a-465c-4992-a530-3e78def2ac5a",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0145QjQ96v2B8YcgHwHmsCQK",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1823,
      "cache_read_input_tokens": 9449,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1823,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 64,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": {
      "cache_miss_reason": {
        "type": "previous_message_not_found"
      }
    }
  }
}
```

</details>

---

### Tool call

_source line 18 · 2026-05-19T19:09:36.265Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01ScEaof4niAk4ytARkUCJXG`</summary>

```json
{
  "query": "LREC-COLING 2026 submission deadline call for papers"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8a5c6cd4-6489-4aa6-ae75-6975c2262ec8",
  "isSidechain": true,
  "agentId": "ac3625b267e3eea76",
  "requestId": "req_011CbCTLb1EgsXwSYdQ558wU",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "9ee570cb-520a-4837-8083-dedd11429ec8",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "072a3a1a-465c-4992-a530-3e78def2ac5a",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0145QjQ96v2B8YcgHwHmsCQK",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1823,
      "cache_read_input_tokens": 9449,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1823,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 64,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": {
      "cache_miss_reason": {
        "type": "previous_message_not_found"
      }
    }
  }
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-19T19:09:37.146Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01MdqhZrNMWFwaEoFnaQHRJb`</summary>

```json
{
  "query": "WMT 2026 shared task submission deadline"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9ee570cb-520a-4837-8083-dedd11429ec8",
  "isSidechain": true,
  "agentId": "ac3625b267e3eea76",
  "requestId": "req_011CbCTLb1EgsXwSYdQ558wU",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "d3c0fc8a-476c-4020-af68-898f1ca0f22d",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "072a3a1a-465c-4992-a530-3e78def2ac5a",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0145QjQ96v2B8YcgHwHmsCQK",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1823,
      "cache_read_input_tokens": 9449,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1823,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 64,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": {
      "cache_miss_reason": {
        "type": "previous_message_not_found"
      }
    }
  }
}
```

</details>

---

### Tool call

_source line 20 · 2026-05-19T19:09:37.383Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01T1zUz4LHzwyhBbMbPWMEyu`</summary>

```json
{
  "query": "multilingual NLP workshop 2026 2027 submission deadline call for papers"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d3c0fc8a-476c-4020-af68-898f1ca0f22d",
  "isSidechain": true,
  "agentId": "ac3625b267e3eea76",
  "requestId": "req_011CbCTLb1EgsXwSYdQ558wU",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "8862a274-19e8-4883-a3c4-eb58604fa5e3",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "072a3a1a-465c-4992-a530-3e78def2ac5a",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0145QjQ96v2B8YcgHwHmsCQK",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1823,
      "cache_read_input_tokens": 9449,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1823,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 64,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": {
      "cache_miss_reason": {
        "type": "previous_message_not_found"
      }
    }
  }
}
```

</details>

---

### Tool result

_source line 21 · 2026-05-19T19:09:38.181Z_

<details><summary>↩ Tool result · `toolu_01PZAnjSMC2MHyArd5kF2Z1Y`</summary>

```text
Web search results for query: "ICLR 2027 submission deadline call for papers"

Links: [{"title":"2026 Dates and Deadlines","url":"https://iclr.cc/Conferences/2026/Dates"},{"title":"International Conference on Learning Representations ICLR in August 2027 in Sydney","url":"https://waset.org/learning-representations-conference-in-august-2027-in-sydney"},{"title":"Key deadlines in AI and ML conferences | Yutori","url":"https://scouts.yutori.com/inbox/53e01f0f-2f7a-4f63-9b38-22358e5386ac"},{"title":"AI Conference Deadlines","url":"https://mlciv.com/ai-deadlines/"},{"title":"Year-Round Deadlines - Imranur Rahman","url":"https://imranur-rahman.github.io/deadlines/"},{"title":"AI & ML Conference Deadlines 2026–2027","url":"https://trybibby.com/conference-deadlines"},{"title":"ICLR 2026 Call for Papers","url":"https://iclr.cc/Conferences/2026/CallForPapers"},{"title":"ICLR 2026","url":"https://iclr.cc/"},{"title":"ICLR | OpenReview","url":"https://openreview.net/group?id=ICLR.cc"}]

Based on the search results, I found information about ICLR 2026, but the specific details for ICLR 2027 submission deadlines are not yet available. ICLR 2027 is predicted to occur April 24-28, 2027, with dates predicted based on the previous year schedule, and you should verify on the official conference website.

The search results show that some 2026/2027 CFPs are not yet posted, meaning the official call for papers and submission deadlines for ICLR 2027 have not been announced yet.

For the most current and official information about ICLR 2027 submission deadlines, I recommend:
- Visiting the official ICLR website at https://iclr.cc/
- Checking OpenReview.net for ICLR announcements
- Monitoring conference deadline tracking websites like the ones found in the search results


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "527fb5c2-1ed0-420a-828d-ce7df0cd5758",
  "isSidechain": true,
  "promptId": "504e2971-a17d-4553-9508-335bf1f3968f",
  "agentId": "ac3625b267e3eea76",
  "type": "user",
  "uuid": "fdc52547-7a1f-4234-9d29-6c5faf68eb97",
  "sourceToolAssistantUUID": "527fb5c2-1ed0-420a-828d-ce7df0cd5758",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "072a3a1a-465c-4992-a530-3e78def2ac5a",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 22 · 2026-05-19T19:09:38.253Z_

<details><summary>↩ Tool result · `toolu_0158PVWf3E2grb8Vy9MyX2K3`</summary>

```text
Web search results for query: "NAACL 2026 submission deadline call for papers"

Links: [{"title":"Dates and Venues – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/dates"},{"title":"NAACL: Nations of the Americas Chapter of the ACL (Association for Computational Linguistics)","url":"https://naacl.org/"},{"title":"Announcements | Computational Linguistics","url":"https://submissions.cljournal.org/index.php/cljournal/announcement"},{"title":"Year-Round Deadlines - Imranur Rahman","url":"https://imranur-rahman.github.io/deadlines/"},{"title":"Second Call for Main Conference Papers - NAACL-HLT 2025","url":"https://2025.naacl.org/calls/papers/"},{"title":"NAACL 2026 - Annual Conference of the Nations of the Americas Chapter of the Association for Computational Linguistics Deadline | ConferenceDeadlines.com","url":"https://www.conferencedeadlines.com/venue/naacl"},{"title":"The 64th Annual Meeting of the Association for Computational Linguistics - ACL 2026","url":"https://2026.aclweb.org/"},{"title":"Upcoming ACL-Sponsored Events | ACL Member Portal","url":"https://www.aclweb.org/portal/acl_sponsored_events?order=field_event_country&sort=desc"},{"title":"Links - Human Language Intelligence Lab","url":"https://hli.skku.edu/links"},{"title":"NAACL: North American Chapter of the Association for Computational Linguistics 2027 2026 2025 ...","url":"http://www.wikicfp.com/cfp/program?id=2170"}]

Based on the search results, here's what I found about NAACL 2026:

Starting from 2024, all main *ACL conferences use ACL Rolling Review (ARR) exclusively, with NAACL 2025 and other conferences included. However, the search results show information primarily about NAACL 2025 rather than NAACL 2026 specifically.

Key findings:

1. **Submission System**: NAACL 2025 uses ACL Rolling Review (ARR) as a reviewing system, with final decisions made by the conference. It's likely that NAACL 2026 will follow a similar process.

2. **Conference Location**: NAACL 2026 will be held in Albuquerque, USA.

3. **General Submission Timeline**: For NAACL, the paper submission deadline is usually in December, and the conference is usually held in June.

Unfortunately, the official NAACL 2026 call for papers with specific submission deadlines is not yet prominently featured in the search results. For the most current and detailed information about NAACL 2026 submission deadlines, I recommend visiting the official NAACL website or the ACL Rolling Review platform at aclrollingreview.org, as these details are typically announced a few months before submissions open.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "06a52cee-0058-427f-a650-b91bd79dc870",
  "isSidechain": true,
  "promptId": "504e2971-a17d-4553-9508-335bf1f3968f",
  "agentId": "ac3625b267e3eea76",
  "type": "user",
  "uuid": "146afcc5-3002-4d81-9340-9a0bc27921e9",
  "sourceToolAssistantUUID": "06a52cee-0058-427f-a650-b91bd79dc870",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "072a3a1a-465c-4992-a530-3e78def2ac5a",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 23 · 2026-05-19T19:09:38.743Z_

<details><summary>↩ Tool result · `toolu_01YBpYd7sVjsRnCidBK6bjSg`</summary>

```text
Web search results for query: "ACL 2026 submission deadline ARR call for papers"

Links: [{"title":"EACL 2026: First Call for Papers | ACL Member Portal","url":"https://www.aclweb.org/portal/content/eacl-2026-first-call-papers"},{"title":"Main Conference - ACL 2026","url":"https://2026.aclweb.org/calls/main_conference_papers/"},{"title":"Call for Student Research Workshop Papers -","url":"https://2026.eacl.org/calls/srw/"},{"title":"Call for Main Conference Papers -","url":"https://2026.eacl.org/calls/papers/"},{"title":"Final call for EACL and ACL 2026 workshops","url":"https://groups.google.com/g/ML-news/c/3rH5gRoL_8k"},{"title":"*SEM 2026: Commitment Link for ARR-Reviewed Papers (Deadline: 10 April 2026) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/sem-2026-commitment-link-arr-reviewed-papers-deadline-10-april-2026"},{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"}]

Based on the search results, here's what I found regarding ACL 2026 and ARR submission deadlines:

## ACL 2026 Main Conference

Papers may be submitted to the ARR 2025 October cycle and ARR 2026 January cycle. At the time of submission to ARR, authors will be asked to select a preferred venue (e.g., ACL 2026), and authors submit articles to ARR, where submissions receive reviews and meta-reviews from ARR reviewers and area chairs, then commit their reviewed articles to a publication venue.

## EACL 2026

For EACL 2026 (which coordinates with ACL 2026), the ARR submission deadline is October 6, 2025, and the EACL commitment deadline is December 14, 2025.

All deadlines are at 11:59PM UTC-12:00 ("anywhere on Earth").

The search results show that both ACL 2026 and EACL 2026 use the ACL Rolling Review (ARR) system for submissions, with a coordinated submission and commitment process to allow flexibility for authors across the *CL 2026 conferences.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "66c4c6e1-807c-4a92-b436-8d2504519ad6",
  "isSidechain": true,
  "promptId": "504e2971-a17d-4553-9508-335bf1f3968f",
  "agentId": "ac3625b267e3eea76",
  "type": "user",
  "uuid": "09f74cc9-c90a-4d86-91d8-64cd658de57d",
  "sourceToolAssistantUUID": "66c4c6e1-807c-4a92-b436-8d2504519ad6",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "072a3a1a-465c-4992-a530-3e78def2ac5a",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 24 · 2026-05-19T19:09:39.299Z_

<details><summary>↩ Tool result · `toolu_01ALdMB9bLWBL4XR4TdNV25S`</summary>

```text
Web search results for query: "NeurIPS 2026 submission deadline call for papers"

Links: [{"title":"Call for Papers 2026","url":"https://neurips.cc/Conferences/2026/CallForPapers"},{"title":"2026 Dates and Deadlines","url":"https://neurips.cc/Conferences/2026/Dates"},{"title":"Call For Evaluations & Datasets 2026","url":"https://neurips.cc/Conferences/2026/CallForEvaluationsDatasets"},{"title":"2026 Conference – NeurIPS Blog","url":"https://blog.neurips.cc/category/2026-conference/"},{"title":"NeurIPS 2026 Call For Competitions","url":"https://neurips.cc/Conferences/2026/CallForCompetitions"},{"title":"NeurIPS 2026","url":"https://neurips.cc/"},{"title":"NeurIPS 2026 Call for Papers — Official Deadlines & Important Dates | PaperPilot","url":"https://www.getpaperpilot.com/deadlines/neurips-2026.html"},{"title":"NeurIPS 2026 Call for Workshops","url":"https://neurips.cc/Conferences/2026/CallForWorkshops"},{"title":"NeurIPS Newsletter – April 2026 – NeurIPS Blog","url":"https://blog.neurips.cc/2026/04/22/neurips-newsletter-april-2026/"},{"title":"NeurIPS/ICLR/ICML Journal-to-Conference Track","url":"https://neurips.cc/public/JournalToConference"}]

Based on the search results, here's the information about NeurIPS 2026 submission deadlines and call for papers:

## Main Track

NeurIPS 2026 is accepting submissions as of April 15, 2026, with abstracts due by May 4th, 2026, and full papers due on May 6th, 2026, Anywhere On Earth (AOE). All authors must have an OpenReview profile when submitting.

## Multiple Submission Tracks

The different tracks (main, evaluations and datasets, position papers) have different calls for papers, different submission portals, and possibly different timelines.

### Evaluations & Datasets Track
The full paper submission deadline (including all supplementary materials) is May 6, 2026 (AoE), and the submission portal opens on April 15, 2026.

### Position Paper Track
The deadlines are the same as for the main track, with abstracts due by May 4th, 2026 (AOE), and full papers due on May 6th, 2026 (AOE).

## Conference Details

The Fortieth annual conference is held Sun. Dec 6th through Sat the 12th, 2026 at the International Convention Centre.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "82dc3f6e-cc5d-4228-aca3-b07cd12a00ce",
  "isSidechain": true,
  "promptId": "504e2971-a17d-4553-9508-335bf1f3968f",
  "agentId": "ac3625b267e3eea76",
  "type": "user",
  "uuid": "a576fae3-954b-467b-a5f8-25601d7cd797",
  "sourceToolAssistantUUID": "82dc3f6e-cc5d-4228-aca3-b07cd12a00ce",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "072a3a1a-465c-4992-a530-3e78def2ac5a",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 25 · 2026-05-19T19:09:39.649Z_

<details><summary>↩ Tool result · `toolu_01TFc6NQKAPPnVrjc3S6Y4v1`</summary>

```text
Web search results for query: "EACL 2027 submission deadline call for papers"

Links: [{"title":"EACL 2027 Call for Main Conference Papers","url":"https://2027.eacl.org/calls/papers/"},{"title":"Dates and Venues – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/dates"},{"title":"The 20th Conference of the European Chapter of the Association for Computational LinguisticsAthens, GreeceMarch 9-14, 2027 -","url":"https://2027.eacl.org/"},{"title":"CALL FOR BIDS TO HOST EACL 2027 | ACL Member Portal","url":"https://www.aclweb.org/portal/content/call-bids-host-eacl-2027"},{"title":"EACL","url":"https://eacl.org/"},{"title":"EACL: Conference of the European Chapter of the Association for Computational Linguistics 2027 2026 2025 ...","url":"http://www.wikicfp.com/cfp/program?id=785"},{"title":"AI Conference Deadlines","url":"https://hlr.github.io/deadlines/"},{"title":"AI Conference Deadlines","url":"https://mlciv.com/ai-deadlines/"},{"title":"CALL FOR PAPERS – ACL Rolling Review","url":"http://aclrollingreview.org/cfp"},{"title":"Association for Computational Linguistics","url":"https://eacl.org/conferences/"}]

Based on the search results, here's the information about EACL 2027 submission deadline:

The ARR (ACL Rolling Review) submission deadline for long and short papers is August 3, 2026 (AoE - Anywhere on Earth).

All deadlines are 11:59PM UTC-12:00 ("anywhere on Earth").

The official EACL 2027 Call for Papers page indicates that more complete details will be provided soon, as the page notes "Please check back soon for the complete Call for Papers."


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "310d4ae3-4a0e-45f4-b03e-5d569f17d139",
  "isSidechain": true,
  "promptId": "504e2971-a17d-4553-9508-335bf1f3968f",
  "agentId": "ac3625b267e3eea76",
  "type": "user",
  "uuid": "2a26b68d-ef57-4c05-a8d7-6273c441f74e",
  "sourceToolAssistantUUID": "310d4ae3-4a0e-45f4-b03e-5d569f17d139",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "072a3a1a-465c-4992-a530-3e78def2ac5a",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 26 · 2026-05-19T19:09:40.072Z_

<details><summary>↩ Tool result · `toolu_0113WMWkbX15Ms3WLvwGb9nC`</summary>

```text
Web search results for query: "AfricaNLP 2027 workshop submission deadline"

Links: [{"title":"First Call for Participation for the 6th AfricaNLP WorkshopCall For Papers | ACL Member Portal","url":"https://www.aclweb.org/portal/content/first-call-participation-6th-africanlp-workshopcall-papers"},{"title":"About the workshop | AfricaNLP Workshop","url":"https://africanlp.masakhane.io/calls/"},{"title":"AfricaNLP Workshop","url":"https://africanlp.masakhane.io/"},{"title":"AI/ML/DS Conference Deadlines 4 Africans","url":"https://mldsafrica.co.za/"},{"title":"AfricaNLP 2025","url":"https://sites.google.com/view/africanlp2025/home"},{"title":"AfricaNLP 2024","url":"https://sites.google.com/view/africanlp2024/home"},{"title":"Program | AfricaNLP Workshop","url":"https://africanlp-workshop.github.io/program.html"},{"title":"AfricaNLP Workshop collocated with ICLR 2023 - Corpora - ELRA lists","url":"https://list.elra.info/mailman3/hyperkitty/list/corpora@list.elra.info/thread/DZNTDN2C472CLX3P2PLJKHUWX6ZHPDB6/"},{"title":"David Ifeoluwa Adelani - X","url":"https://x.com/davlanade/status/1893879817134620873"},{"title":"Important Dates | AfricaNLP Workshop - GitHub Pages","url":"https://africanlp-workshop.github.io/dates.html"}]

Based on the search results, I found information about the AfricaNLP workshop, but the results primarily cover past and current editions (2020-2025). The search results do not contain specific information about an AfricaNLP 2027 workshop submission deadline.

The most recent information available is for AfricaNLP 2025, which has a submission deadline of March 7, 2025 (AoE). The 2025 workshop will be hybrid and co-located with ACL 2025.

Since 2027 is in the future and announcement details may not yet be available, I recommend:
1. Checking the official AfricaNLP workshop website or social media for announcements
2. Contacting the workshop organizers directly at africanlp-acl2025 [at] googlegroups.com for information about future editions


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "8a5c6cd4-6489-4aa6-ae75-6975c2262ec8",
  "isSidechain": true,
  "promptId": "504e2971-a17d-4553-9508-335bf1f3968f",
  "agentId": "ac3625b267e3eea76",
  "type": "user",
  "uuid": "eba8c027-213e-42a5-a94e-a76eb34486d7",
  "sourceToolAssistantUUID": "8a5c6cd4-6489-4aa6-ae75-6975c2262ec8",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "072a3a1a-465c-4992-a530-3e78def2ac5a",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 27 · 2026-05-19T19:09:40.839Z_

<details><summary>↩ Tool result · `toolu_01GRjbkiWCwkTDf1dK2igTMM`</summary>

```text
Web search results for query: "ICML 2026 submission deadline call for papers"

Links: [{"title":"ICML 2026 Call for Papers","url":"https://icml.cc/Conferences/2026/CallForPapers"},{"title":"2026 Dates and Deadlines","url":"https://icml.cc/Conferences/2026/Dates"},{"title":"ICML 2026 Author Instructions","url":"https://icml.cc/Conferences/2026/AuthorInstructions"},{"title":"ICML 2026 Call For Position Papers","url":"https://icml.cc/Conferences/2026/CallForPositionPapers"},{"title":"ICML 2026: Strictest New Rules Ever - LLMs Banned as Authors, Papers with AI Abuse Rejected","url":"https://eu.36kr.com/en/p/3540848514510723"},{"title":"ICML 2026 Call for Post-Conference Workshops","url":"https://icml.cc/Conferences/2026/CallForWorkshops"},{"title":"ICLR 2026 Call for Papers","url":"https://iclr.cc/Conferences/2026/CallForPapers"},{"title":"IEEE ICMLCN 2026 | IEEE International Conference on Machine Learning for Communication and Networking 2026 | IEEE ICMLCN 2026","url":"https://icmlcn2026.ieee-icmlcn.org/"},{"title":"ICML 2026 Peer Review FAQ","url":"https://icml.cc/Conferences/2026/PeerReviewFAQ"},{"title":"ICML 2026","url":"https://conferences-basecamp.informatik.uni-hamburg.de/conference/?id=icml26"}]

Based on the search results, here's the information about ICML 2026 submission deadlines and call for papers:

## Key Submission Deadlines

The submission site opens on January 8, 2026, and the abstract submission deadline is January 24, 2026 (12 Noon UTC-0), while the full paper submission deadline is January 29, 2026 (12 Noon UTC-0).

## Paper Submission Requirements

Papers must be prepared and submitted as a single file: 8 pages for the main paper, with unlimited pages for references, the impact statement, and appendices. There will be no separate deadline for the submission of supplementary material.

## Reviewer Requirements

Qualified authors are required to review for ICML, with two requirements: per-submission requirement and per-author requirement. All submissions must have at least one author who agrees to serve as a reviewer for ICML.

## Conference Details

The Forty-Third annual conference is held from Monday, July 6th through Saturday the 11th, 2026 at the Coex Convention & Exhibition Center.

## Position Papers Track

There is also a separate call for position papers with the same submission deadlines. Position papers make an argument for a viewpoint or perspective about what should be done, in contrast to main track papers, which report on advances that have already been accomplished. Position papers also generally adopt a meta-level perspective on the field of machine learning, with wider scope than any individual area.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "fdb12882-e11a-46da-aaec-2e5250d14e61",
  "isSidechain": true,
  "promptId": "504e2971-a17d-4553-9508-335bf1f3968f",
  "agentId": "ac3625b267e3eea76",
  "type": "user",
  "uuid": "6d1db9bb-8cd4-4c88-a20e-91de226e6dd9",
  "sourceToolAssistantUUID": "fdb12882-e11a-46da-aaec-2e5250d14e61",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "072a3a1a-465c-4992-a530-3e78def2ac5a",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 28 · 2026-05-19T19:09:41.381Z_

<details><summary>↩ Tool result · `toolu_012btvz9FL51HAPhX23GD8cM`</summary>

```text
Web search results for query: "COLING 2026 submission deadline call for papers"

Links: [{"title":"COLING: International Conference on Computational Linguistics 2027 2026 2025 ...","url":"http://www.wikicfp.com/cfp/program?id=533"},{"title":"COLING 2026 - International Conference on Computational Linguistics Deadline | ConferenceDeadlines.com","url":"https://www.conferencedeadlines.com/venue/coling"},{"title":"Call for Main Conference Papers - COLING 2025","url":"https://coling2025.org/calls/main_conference_papers/"},{"title":"Call for papers for computational linguistics conference in ...","url":"https://www.facebook.com/groups/CorpusLinguistics/posts/10162428528018002/"},{"title":"AbjadNLP 2026 – The 2nd Workshop on NLP for Languages Using Arabic Script","url":"https://wp.lancs.ac.uk/abjad/"},{"title":"Computer Science conferences timeline","url":"https://lucjaulmes.github.io/cfp-timeline/"},{"title":"Call for Main Conference Papers -","url":"https://2026.eacl.org/calls/papers/"},{"title":"CoNLL 2026: 3rd and Final Call for Papers - Corpora - ELRA lists","url":"https://list.elra.info/mailman3/hyperkitty/list/corpora@list.elra.info/thread/BDW4FPXENUKPTACOYMT5PXZSDZHJ5LB4/"},{"title":"CoNLL 2026 | CoNLL","url":"https://conll.org/"},{"title":"AI Deadlines – AI Conference Call For Paper Deadlines","url":"http://aideadlines.org/"}]

Based on the search results, I found information about COLING conferences, though the results primarily show information for COLING 2025 rather than a detailed call for COLING 2026. Here's what I found:

## COLING 2026 Overview

COLING 2026 will be held in Abu Dhabi, UAE, continuing the tradition of the International Conference on Computational Linguistics.

## COLING 2025 (for reference)

Since specific COLING 2026 call details weren't fully available in the search results, here's information about the most recent completed call for COLING 2025:

The 31st International Conference on Computational Linguistics (COLING 2025) took place in Abu Dhabi, UAE, January 19-24 2025. COLING 2025 invited the submission of long papers of up to eight pages and short papers of up to four pages.

For the most current and detailed information about COLING 2026 submission deadlines and the official call for papers, I recommend:
- Visiting the official COLING 2026 website directly
- Checking the WikiCFP database for the most up-to-date deadlines
- Looking at ConferenceDeadlines.com for COLING 2026 specifics

The search results indicate that COLING 2026 submission details should be posted on the official conference website, but the exact deadlines weren't captured in these results.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "68dd15bb-1043-4b39-acb0-832292f08b9f",
  "isSidechain": true,
  "promptId": "504e2971-a17d-4553-9508-335bf1f3968f",
  "agentId": "ac3625b267e3eea76",
  "type": "user",
  "uuid": "b4dfc0c9-e977-48dc-bdc1-60c26aa75da3",
  "sourceToolAssistantUUID": "68dd15bb-1043-4b39-acb0-832292f08b9f",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "072a3a1a-465c-4992-a530-3e78def2ac5a",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 29 · 2026-05-19T19:09:41.516Z_

<details><summary>↩ Tool result · `toolu_01ScEaof4niAk4ytARkUCJXG`</summary>

```text
Web search results for query: "LREC-COLING 2026 submission deadline call for papers"

Links: [{"title":"LREC 2026: Deadline Extended to October 24, 2025 - Main conference papers, Workshop & Tutorial Proposals - Corpora - ELRA lists","url":"https://list.elra.info/mailman3/hyperkitty/list/corpora@list.elra.info/thread/2TFINXQSH2WTSARQITYUNC4JEIGRSQFL/"},{"title":"LREC 2026 - First Call for Workshops - Corpora - ELRA lists","url":"https://list.elra.info/mailman3/hyperkitty/list/corpora@list.elra.info/thread/OVBL6KCW5Q4IIYDZRJNEVL4SKO3TFMOZ/"},{"title":"Second Call for Papers - LREC 2026","url":"https://lrec2026.info/calls/second-call-for-papers/"},{"title":"Calls - LREC 2026","url":"https://lrec2026.info/calls/"},{"title":"Third Call for Papers - LREC 2026","url":"https://lrec2026.info/third-call-for-papers/"},{"title":"Language Resources and Evaluation Conference - LREC 2026","url":"https://lrec2026.info/"},{"title":"15th LREC 2026 Conference - call for papers | CLARIN-EL","url":"https://www.clarin.gr/en/content/15th-lrec-2026-conference-call-papers"},{"title":"LINGUIST List 36.2162 Confs: 15th Language Resources and Evaluation Conference - Call for Tutorial Proposals (Spain)","url":"https://linguistlist.org/issues/36/2162/"}]

Based on the search results, here's the information about LREC 2026 submissions and deadlines:

## Main Conference Paper Submission

The submission deadline for oral and poster papers is October 24, 2025. Submissions should be 4 to 8 pages in length (excluding references and potential Ethics Statements), and papers must be anonymized to support double-blind reviewing.

## Other Important Dates

Notification of acceptance is February 13, 2026, with a camera-ready deadline of March 15, 2026.

## Conference Details

The Fifteenth biennial Language Resources and Evaluation Conference (LREC) will be held at the Palau de Congressos de Palma in Palma, Mallorca, Spain, on 11-16 May 2026.

## Workshop and Tutorial Proposals

For those interested in organizing workshops or tutorials: the workshop proposal submission deadline is October 17, 2025, with notification of acceptance on November 17, 2025. Similar deadlines apply for tutorial proposals.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "9ee570cb-520a-4837-8083-dedd11429ec8",
  "isSidechain": true,
  "promptId": "504e2971-a17d-4553-9508-335bf1f3968f",
  "agentId": "ac3625b267e3eea76",
  "type": "user",
  "uuid": "ce31da34-74b4-481e-a6b2-7c5036802c40",
  "sourceToolAssistantUUID": "9ee570cb-520a-4837-8083-dedd11429ec8",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "072a3a1a-465c-4992-a530-3e78def2ac5a",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 30 · 2026-05-19T19:09:42.091Z_

<details><summary>↩ Tool result · `toolu_01MdqhZrNMWFwaEoFnaQHRJb`</summary>

```text
Web search results for query: "WMT 2026 shared task submission deadline"

Links: [{"title":"WMT 2026","url":"https://www2.statmt.org/wmt26/index.html"},{"title":"WMT 2026 Shared Task on Automated Translation Quality Evaluation Systems | ACL Member Portal","url":"https://www.aclweb.org/portal/content/wmt-2026-shared-task-automated-translation-quality-evaluation-systems"},{"title":"Model Compression Shared Task @ WMT 2026 | ACL Member Portal","url":"https://www.aclweb.org/portal/content/model-compression-shared-task-wmt-2026"},{"title":"WMT 2026 Shared Task on Automated Translation Quality Evaluation Systems: Preliminary Announcement and Call for Participation","url":"https://groups.google.com/g/wmt-tasks/c/u0YeZeBnNpU"},{"title":"WMT: Workshop on Machine Translation - Google Groups","url":"https://groups.google.com/g/wmt-tasks"},{"title":"WMT 2025","url":"https://www2.statmt.org/wmt25/"},{"title":"WMT26 | Machine Translate","url":"https://machinetranslate.org/wmt26"},{"title":"Shared Task: General Machine Translation","url":"https://www2.statmt.org/wmt26/translation-task.html"},{"title":"Ninth Conference on Machine Translation (WMT24)","url":"https://www2.statmt.org/wmt24/"},{"title":"Model Compression Shared Task @ WMT 2025 | ACL Member Portal","url":"https://www.aclweb.org/portal/content/model-compression-shared-task-wmt-2025"}]

Based on the search results, here's what I found about WMT 2026 shared task submission deadlines:

## WMT 2026 Shared Task Submission Deadlines

The submission deadlines vary by task:

**Model Compression Shared Task:**
Test data released: June 18, 2026; Model Submission deadline: July 2, 2026

**Automated Translation Quality Evaluation Systems (Quality Evaluation Task):**
Challenge set submission deadline: 16 July 2026; Tasks 1, 2, and 3 test data release: 23 July 2026

**General Notes:**
All deadlines are in AoE (Anywhere on Earth) time.

For more specific deadlines related to other shared tasks or detailed timeline information, you may want to visit the official WMT 2026 website at www2.statmt.org/wmt26 or check the task-specific pages linked in the search results.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d3c0fc8a-476c-4020-af68-898f1ca0f22d",
  "isSidechain": true,
  "promptId": "504e2971-a17d-4553-9508-335bf1f3968f",
  "agentId": "ac3625b267e3eea76",
  "type": "user",
  "uuid": "7758ad36-5a71-4972-aeb1-c6daf7190b74",
  "sourceToolAssistantUUID": "d3c0fc8a-476c-4020-af68-898f1ca0f22d",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "072a3a1a-465c-4992-a530-3e78def2ac5a",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 31 · 2026-05-19T19:09:44.360Z_

<details><summary>↩ Tool result · `toolu_01T1zUz4LHzwyhBbMbPWMEyu`</summary>

```text
Web search results for query: "multilingual NLP workshop 2026 2027 submission deadline call for papers"

Links: [{"title":"Call for workshops: EMNLP & AACL","url":"https://groups.google.com/g/ml-news/c/W-fucfhVto4"},{"title":"Call for Papers: the 6th workshop of Natural Language Meets Logic and Machine Learning (NALOMA) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/call-papers-6th-workshop-natural-language-meets-logic-and-machine-learning-naloma"},{"title":"Call for Main Conference Papers - EMNLP 2026","url":"https://2026.emnlp.org/calls/main_conference_papers/"},{"title":"21st Workshop on Innovative Use of NLP for Building Educational Applications - SIGEDU","url":"https://sig-edu.org/bea/2026"},{"title":"BabyLM Turns 4 and Goes Multilingual: Call for Papers for the 2026 BabyLM Workshop","url":"https://arxiv.org/pdf/2602.20092"},{"title":"TrustNLP","url":"https://trustnlpworkshop.github.io/"}]

Based on the search results, I found several relevant workshops and conferences with calls for papers for 2026-2027:

## BabyLM Workshop 2026 (Multilingual Track)

The BabyLM Workshop 2026 includes a new MULTILINGUAL track, focusing on English, Dutch, and Chinese. The workshop calls for papers related to training efficiency, small-scale training datasets, cognitive modeling, model evaluation, and architecture innovation.

## Other NLP Workshops with 2026 Deadlines

1. **TrustNLP Workshop** - March 5, 2026 is the Workshop Paper Due Date for Direct Submission, with an April 10, 2026 deadline for Fast-Track submissions.

2. **BEA 2026** (Building Educational Applications) - The submission platform is https://softconf.com/acl2026/bea2026/ with all deadlines at 11:59pm UTC-12 (anywhere on earth).

3. **NALOMA Workshop** (Natural Language Meets Logic and Machine Learning) - The deadline for papers and extended abstracts is April 30, 2026.

For more specific details about submission deadlines and requirements for the multilingual NLP workshop that interests you, I recommend checking the official workshop websites directly through the links provided in the search results.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "8862a274-19e8-4883-a3c4-eb58604fa5e3",
  "isSidechain": true,
  "promptId": "504e2971-a17d-4553-9508-335bf1f3968f",
  "agentId": "ac3625b267e3eea76",
  "type": "user",
  "uuid": "a671b49e-2a69-4815-9fc5-7dc87cb1aff0",
  "sourceToolAssistantUUID": "8862a274-19e8-4883-a3c4-eb58604fa5e3",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "072a3a1a-465c-4992-a530-3e78def2ac5a",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 32 · 2026-05-19T19:09:47.253Z_

Now let me search for more specific deadline details and the GitHub implementations.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a671b49e-2a69-4815-9fc5-7dc87cb1aff0",
  "isSidechain": true,
  "agentId": "ac3625b267e3eea76",
  "requestId": "req_011CbCTMeiWDQjcqEftiPDSk",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "0669245e-47ad-4c33-a537-608f3f7227b6",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "072a3a1a-465c-4992-a530-3e78def2ac5a",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UEhjMsz9yzsmXWmBPhSh5j",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 11850,
      "cache_read_input_tokens": 7773,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 11850,
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

_source line 33 · 2026-05-19T19:09:47.777Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01DWpTtZohJSbKosWGDiBAQN`</summary>

```json
{
  "query": "ACL 2026 commitment deadline dates important"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0669245e-47ad-4c33-a537-608f3f7227b6",
  "isSidechain": true,
  "agentId": "ac3625b267e3eea76",
  "requestId": "req_011CbCTMeiWDQjcqEftiPDSk",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "8e86cdd0-004b-4cd2-be0b-b81aec80b297",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "072a3a1a-465c-4992-a530-3e78def2ac5a",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UEhjMsz9yzsmXWmBPhSh5j",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 11850,
      "cache_read_input_tokens": 7773,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 11850,
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

_source line 34 · 2026-05-19T19:09:48.268Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01M1bBNrmkJayszZ8FpMj1CK`</summary>

```json
{
  "query": "NAACL 2026 ARR commitment deadline dates"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8e86cdd0-004b-4cd2-be0b-b81aec80b297",
  "isSidechain": true,
  "agentId": "ac3625b267e3eea76",
  "requestId": "req_011CbCTMeiWDQjcqEftiPDSk",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "9ce75a99-c7e3-4c4a-8668-57bce89035d6",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "072a3a1a-465c-4992-a530-3e78def2ac5a",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UEhjMsz9yzsmXWmBPhSh5j",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 11850,
      "cache_read_input_tokens": 7773,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 11850,
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

_source line 35 · 2026-05-19T19:09:48.722Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01R8wQKD945gNL3vsW4m14Xd`</summary>

```json
{
  "query": "ICLR 2027 deadline dates predicted"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9ce75a99-c7e3-4c4a-8668-57bce89035d6",
  "isSidechain": true,
  "agentId": "ac3625b267e3eea76",
  "requestId": "req_011CbCTMeiWDQjcqEftiPDSk",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "e11d9e83-4c5d-4a1a-b528-df6962663540",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "072a3a1a-465c-4992-a530-3e78def2ac5a",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UEhjMsz9yzsmXWmBPhSh5j",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 11850,
      "cache_read_input_tokens": 7773,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 11850,
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

_source line 36 · 2026-05-19T19:09:49.191Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Nmfd2SdeYC5RpggBMfLEog`</summary>

```json
{
  "query": "AfricaNLP 2026 workshop deadline submission"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e11d9e83-4c5d-4a1a-b528-df6962663540",
  "isSidechain": true,
  "agentId": "ac3625b267e3eea76",
  "requestId": "req_011CbCTMeiWDQjcqEftiPDSk",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "c9a44b0f-c59d-48d9-8626-554e1b1e92b9",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "072a3a1a-465c-4992-a530-3e78def2ac5a",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UEhjMsz9yzsmXWmBPhSh5j",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 11850,
      "cache_read_input_tokens": 7773,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 11850,
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

_source line 37 · 2026-05-19T19:09:49.721Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01LZJEUBDHLSLzmHKceqPM4a`</summary>

```json
{
  "query": "WMT 2026 research paper submission deadline EMNLP"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c9a44b0f-c59d-48d9-8626-554e1b1e92b9",
  "isSidechain": true,
  "agentId": "ac3625b267e3eea76",
  "requestId": "req_011CbCTMeiWDQjcqEftiPDSk",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "a26eb90d-65dc-4853-98ee-3cd12ed75253",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "072a3a1a-465c-4992-a530-3e78def2ac5a",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UEhjMsz9yzsmXWmBPhSh5j",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 11850,
      "cache_read_input_tokens": 7773,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 11850,
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

_source line 38 · 2026-05-19T19:09:50.192Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01N49BHFDAnRKbz4RBbLQL8p`</summary>

```json
{
  "query": "site:github.com \"token tax\" multilingual tokenization"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a26eb90d-65dc-4853-98ee-3cd12ed75253",
  "isSidechain": true,
  "agentId": "ac3625b267e3eea76",
  "requestId": "req_011CbCTMeiWDQjcqEftiPDSk",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "536a644d-d6a7-44d2-94f4-53430f96b19f",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "072a3a1a-465c-4992-a530-3e78def2ac5a",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UEhjMsz9yzsmXWmBPhSh5j",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 11850,
      "cache_read_input_tokens": 7773,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 11850,
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

_source line 39 · 2026-05-19T19:09:51.110Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01VpDws678rbHGuYC3qULopW`</summary>

```json
{
  "query": "site:github.com \"causal mediation analysis\" NLP transformer"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "536a644d-d6a7-44d2-94f4-53430f96b19f",
  "isSidechain": true,
  "agentId": "ac3625b267e3eea76",
  "requestId": "req_011CbCTMeiWDQjcqEftiPDSk",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "98c56618-6908-44b1-8499-021be21a1339",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "072a3a1a-465c-4992-a530-3e78def2ac5a",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UEhjMsz9yzsmXWmBPhSh5j",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 11850,
      "cache_read_input_tokens": 7773,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 11850,
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

_source line 40 · 2026-05-19T19:09:51.603Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01JgZiMA8npddkMYAyHHoNAZ`</summary>

```json
{
  "query": "site:github.com \"tokenization fertility\" multilingual measurement"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "98c56618-6908-44b1-8499-021be21a1339",
  "isSidechain": true,
  "agentId": "ac3625b267e3eea76",
  "requestId": "req_011CbCTMeiWDQjcqEftiPDSk",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "36b7126e-786d-46a5-ab4d-dcca69f31987",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "072a3a1a-465c-4992-a530-3e78def2ac5a",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UEhjMsz9yzsmXWmBPhSh5j",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 11850,
      "cache_read_input_tokens": 7773,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 11850,
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

_source line 41 · 2026-05-19T19:09:52.077Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01RovW7PcwhSTMmSm9Mpuon6`</summary>

```json
{
  "query": "site:github.com AfriMMLU evaluation benchmark African languages"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "36b7126e-786d-46a5-ab4d-dcca69f31987",
  "isSidechain": true,
  "agentId": "ac3625b267e3eea76",
  "requestId": "req_011CbCTMeiWDQjcqEftiPDSk",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "b50a8b39-080b-4eba-9a71-bb29295fb2e3",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "072a3a1a-465c-4992-a530-3e78def2ac5a",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UEhjMsz9yzsmXWmBPhSh5j",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 11850,
      "cache_read_input_tokens": 7773,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 11850,
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

_source line 42 · 2026-05-19T19:09:52.297Z_

<details><summary>↩ Tool result · `toolu_01DWpTtZohJSbKosWGDiBAQN`</summary>

```text
Web search results for query: "ACL 2026 commitment deadline dates important"

Links: [{"title":"The 64th Annual Meeting of the Association for Computational Linguistics - ACL 2026","url":"https://2026.aclweb.org/"},{"title":"Dates and Venues – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/dates"},{"title":"Update ACL 2025 and 2026 conference deadlines · huggingface/ai-deadlines at 9dc485d","url":"https://huggingface.co/spaces/huggingface/ai-deadlines/commit/9dc485d7522c481c65e1e366500d2ab6398449d9"},{"title":"Update acl conference deadlines · huggingface/ai-deadlines at 70e03c7","url":"https://huggingface.co/spaces/huggingface/ai-deadlines/commit/70e03c703becac091e137e762eceafad105bd1c0"},{"title":"ACL 2026 in California: Dates, Deadline, Fees & Registration Steps - Conference Inc.","url":"https://conferenceinc.net/post/acl/"},{"title":"AI Conference Deadlines","url":"https://mlciv.com/ai-deadlines/"},{"title":"Incentives 2026 – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/incentives2026"},{"title":"ACL 2026","url":"http://aideadlines.org/conference/?id=acl26"},{"title":"LINGUIST List 37.181 Confs: 64th Annual Meeting of the Association for Computational Linguistics: Industry Track (USA)","url":"https://linguistlist.org/issues/37/181/"},{"title":"The 19th Conference of the European Chapter of the Association for Computational LinguisticsRabat, MoroccoMarch 24-29, 2026 -","url":"https://2026.eacl.org/"}]

Based on the search results, here are the important commitment deadline dates for ACL 2026:

## Key ACL 2026 Commitment Deadlines

The 64th Annual Meeting of the Association for Computational Linguistics (ACL 2026) will take place in San Diego, California, from July 2 - 7, 2026. All deadlines are 11:59 pm UTC -12h (anywhere on earth).

**Main Conference Track:**
- ARR reviews available: March 9, 2026. Commitment deadline: March 14, 2026. Notification: April 4, 2026. Camera-ready: April 19, 2026.

**Industry Track:**
- Paper submission deadline: February 14, 2026. Author response deadline: March 29, 2026. Notification of acceptance: April 12, 2026. Camera-ready deadline: April 19, 2026.

Note that starting from 2024, all main *ACL conferences used ARR exclusively, including ACL 2026, though the ACL 2026 Industry Track does not use ARR.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "8e86cdd0-004b-4cd2-be0b-b81aec80b297",
  "isSidechain": true,
  "promptId": "504e2971-a17d-4553-9508-335bf1f3968f",
  "agentId": "ac3625b267e3eea76",
  "type": "user",
  "uuid": "2f2bad35-b2db-4ac7-9b2f-46c5ffdc9761",
  "sourceToolAssistantUUID": "8e86cdd0-004b-4cd2-be0b-b81aec80b297",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "072a3a1a-465c-4992-a530-3e78def2ac5a",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 43 · 2026-05-19T19:09:52.545Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_019Uao18P8zU8N2HxH2y7Ped`</summary>

```json
{
  "query": "site:github.com \"regression discontinuity\" tokenization NLP"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2f2bad35-b2db-4ac7-9b2f-46c5ffdc9761",
  "isSidechain": true,
  "agentId": "ac3625b267e3eea76",
  "requestId": "req_011CbCTMeiWDQjcqEftiPDSk",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "f2df057f-797f-4950-ad05-85f4ff8068c0",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "072a3a1a-465c-4992-a530-3e78def2ac5a",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UEhjMsz9yzsmXWmBPhSh5j",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 11850,
      "cache_read_input_tokens": 7773,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 11850,
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

_source line 44 · 2026-05-19T19:09:53.020Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01D1u5qu4XR96tMkNLKRyC7v`</summary>

```json
{
  "query": "site:github.com \"selective translation\" multilingual NLP code"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f2df057f-797f-4950-ad05-85f4ff8068c0",
  "isSidechain": true,
  "agentId": "ac3625b267e3eea76",
  "requestId": "req_011CbCTMeiWDQjcqEftiPDSk",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "fa3c43cf-61d0-44de-8b88-7a6eda95f929",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "072a3a1a-465c-4992-a530-3e78def2ac5a",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UEhjMsz9yzsmXWmBPhSh5j",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 11850,
      "cache_read_input_tokens": 7773,
      "output_tokens": 551,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 11850
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 551,
          "cache_read_input_tokens": 7773,
          "cache_creation_input_tokens": 11850,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 11850,
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

_source line 45 · 2026-05-19T19:09:53.226Z_

<details><summary>↩ Tool result · `toolu_01R8wQKD945gNL3vsW4m14Xd`</summary>

```text
Web search results for query: "ICLR 2027 deadline dates predicted"

Links: [{"title":"2026 Dates and Deadlines","url":"https://iclr.cc/Conferences/2026/Dates"},{"title":"AI Conference Deadlines","url":"https://mlciv.com/ai-deadlines/"},{"title":"International Conference on Learning Representations ICLR in August 2027 in Sydney","url":"https://waset.org/learning-representations-conference-in-august-2027-in-sydney"},{"title":"Year-Round Deadlines - Imranur Rahman","url":"https://imranur-rahman.github.io/deadlines/"},{"title":"Key deadlines in AI and ML conferences | Yutori","url":"https://scouts.yutori.com/inbox/53e01f0f-2f7a-4f63-9b38-22358e5386ac"},{"title":"AI & ML Conference Deadlines 2026–2027","url":"https://trybibby.com/conference-deadlines"},{"title":"Personal Conference Deadlines","url":"https://zhaohsu.top/conference-deadlines/"},{"title":"International Conference on Learning and Reinforcement ICLR in August 2027 in Barcelona","url":"https://waset.org/learning-and-reinforcement-conference-in-august-2027-in-barcelona"},{"title":"AI Conference Deadlines","url":"https://nunoduarte.github.io/deadlines/"},{"title":"International Conference on Learning Robots ICLR in May 2027 in Crete","url":"https://waset.org/learning-robots-conference-in-may-2027-in-crete"}]

Based on the search results, here are the predicted deadline dates for ICLR 2027:

The main conference is predicted to be held April 24-28, 2027, with the dates predicted based on previous year schedule. However, you should verify on the official conference website, as these are predictions rather than confirmed dates.

The search results indicate that specific submission deadline dates for ICLR 2027 have not yet been officially announced. The prediction is based on the pattern of conference dates from previous years (ICLR 2025 was April 24-28, 2026 was also April 24-28, so 2027 follows the same pattern). Typically, ICLR has a mandatory abstract deadline followed by a full paper deadline several days later, but exact dates for 2027 are not yet available in these sources.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "e11d9e83-4c5d-4a1a-b528-df6962663540",
  "isSidechain": true,
  "promptId": "504e2971-a17d-4553-9508-335bf1f3968f",
  "agentId": "ac3625b267e3eea76",
  "type": "user",
  "uuid": "158fcce3-ac38-4f07-be88-339cc90db053",
  "sourceToolAssistantUUID": "e11d9e83-4c5d-4a1a-b528-df6962663540",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "072a3a1a-465c-4992-a530-3e78def2ac5a",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 46 · 2026-05-19T19:09:53.398Z_

<details><summary>↩ Tool result · `toolu_01M1bBNrmkJayszZ8FpMj1CK`</summary>

```text
Web search results for query: "NAACL 2026 ARR commitment deadline dates"

Links: [{"title":"Dates and Venues","url":"http://aclrollingreview.org/dates"},{"title":"Second Call for Main Conference Papers - NAACL-HLT 2025","url":"https://2025.naacl.org/calls/papers/"},{"title":"AI Conference Deadlines","url":"https://mlciv.com/ai-deadlines/"},{"title":"*SEM 2026: Commitment Link for ARR-Reviewed Papers (Deadline: 10 April 2026) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/sem-2026-commitment-link-arr-reviewed-papers-deadline-10-april-2026"},{"title":"Community announcement: Submission dates and process for EACL, NAACL and ACL","url":"https://www.aclweb.org/portal/sites/default/files/Submission%20Dates%20and%20Process%20for%20EACL_NAACL%20and%20ACL%202024-2.pdf"},{"title":"NAACL: Nations of the Americas Chapter of the ACL (Association for Computational Linguistics)","url":"https://naacl.org/"},{"title":"NAACL: North American Chapter of the Association for Computational Linguistics 2027 2026 2025 ...","url":"http://www.wikicfp.com/cfp/program?id=2170"},{"title":"Incentives 2026","url":"http://aclrollingreview.org/incentives2026"},{"title":"AI Conference Deadlines","url":"https://hlr.github.io/deadlines/"}]

Based on the search results, here are the key ARR commitment deadline dates for NAACL 2026:

ARR reviews will be available on March 9, 2026, with a commitment deadline of March 14, 2026. Following the commitment deadline, notification will be issued on April 4, 2026, and the camera-ready deadline is April 19, 2026.

These dates reflect the timeline for authors who have already received reviews from ARR and wish to commit their papers to NAACL 2026 for final publication consideration.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "9ce75a99-c7e3-4c4a-8668-57bce89035d6",
  "isSidechain": true,
  "promptId": "504e2971-a17d-4553-9508-335bf1f3968f",
  "agentId": "ac3625b267e3eea76",
  "type": "user",
  "uuid": "7f54969d-d9a1-478f-9f9d-106f268a0adc",
  "sourceToolAssistantUUID": "9ce75a99-c7e3-4c4a-8668-57bce89035d6",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "072a3a1a-465c-4992-a530-3e78def2ac5a",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 47 · 2026-05-19T19:09:54.021Z_

<details><summary>↩ Tool result · `toolu_01Nmfd2SdeYC5RpggBMfLEog`</summary>

```text
Web search results for query: "AfricaNLP 2026 workshop deadline submission"

Links: [{"title":"[Corpora-List] Deadline extended: AfricaNLP @ EACL 2026","url":"http://www.mail-archive.com/corpora@list.elra.info/msg05265.html"},{"title":"AfricaNLP 2026 - Sign in","url":"https://sites.google.com/view/africanlp2026/home"},{"title":"AfricaNLP 2026","url":"https://sites.google.com/view/africanlp2026"},{"title":"AfricaNLP 2026 7th Workshop on African Natural Language Processing","url":"https://aclanthology.org/2026.africanlp-main.pdf"},{"title":"The 7th AfricaNLP Workshop @ EACL 2026 (Rabat, Morocco)","url":"https://groups.google.com/g/ml-news/c/WGxap-KXkXQ"},{"title":"AfricaNLP Workshop","url":"https://africanlp.masakhane.io/"},{"title":"AfricaNLP 2025","url":"https://sites.google.com/view/africanlp2025/home"},{"title":"eLearning Africa's Post","url":"https://www.linkedin.com/posts/elearning-africa_elearningafrica-callforproposals-digitallearning-activity-7396852284510515200-iOoN"},{"title":"First Call for Participation for the 6th AfricaNLP WorkshopCall For Papers | ACL Member Portal","url":"https://www.aclweb.org/portal/content/first-call-participation-6th-africanlp-workshopcall-papers"},{"title":"AI/ML/DS Conference Deadlines 4 Africans","url":"https://mldsafrica.co.za/"}]

Based on the search results, here's the information about the AfricaNLP 2026 workshop submission deadlines:

## AfricaNLP 2026 Submission Deadlines

The direct submission deadline is December 22nd, 2025 (extended), and the ARR submission deadline is January 9th, 2026, with acceptance notification on January 23, 2026. The workshop itself will be a day-long event during EACL 2026 (March 24-29, 2026).

## Workshop Details

The 7th AfricaNLP Workshop is co-located with EACL 2026 in Rabat, Morocco, with the theme "Multilingual Multimodal LLMs". The submission URL is https://openreview.net/group?id=eacl.org/EACL/2026/Workshop/AfricaNLP.

For additional support, you are invited to join the Masakhane community Slack (channel #africanlp-acl2026-support), where organizers will be available to answer questions regarding submissions, format, topics, etc.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c9a44b0f-c59d-48d9-8626-554e1b1e92b9",
  "isSidechain": true,
  "promptId": "504e2971-a17d-4553-9508-335bf1f3968f",
  "agentId": "ac3625b267e3eea76",
  "type": "user",
  "uuid": "d6d4463b-4622-468f-865e-b36093412c03",
  "sourceToolAssistantUUID": "c9a44b0f-c59d-48d9-8626-554e1b1e92b9",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "072a3a1a-465c-4992-a530-3e78def2ac5a",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 48 · 2026-05-19T19:09:54.336Z_

<details><summary>↩ Tool result · `toolu_01LZJEUBDHLSLzmHKceqPM4a`</summary>

```text
Web search results for query: "WMT 2026 research paper submission deadline EMNLP"

Links: [{"title":"WMT 2026","url":"https://www2.statmt.org/wmt26/index.html"},{"title":"EMNLP 2026 Conference Deadline | Live Countdown Tracker","url":"https://www.getpaperpilot.com/deadlines/emnlp-2026.html"},{"title":"WMT 2025","url":"https://www2.statmt.org/wmt25/"},{"title":"EMNLP 2026 on X: \"📢 The First Call for Papers for EMNLP 2026 is officially out! 📝 We welcome long &amp; short papers featuring original research on empirical methods for NLP. 🗓️ ARR Submission Deadline: May 25, 2026 🔗 Read the full CFP here: https://t.co/GU2kaISjUG #EMNLP2026\" / X","url":"https://x.com/emnlpmeeting/status/2029508292637061462"},{"title":"LINGUIST List 37.972 Confs: 2026 Conference on Empirical Methods in Natural Language Processing (Hungary)","url":"https://linguistlist.org/issues/37/972/"},{"title":"Call for Main Conference Papers - EMNLP 2026","url":"https://2026.emnlp.org/calls/main_conference_papers/"},{"title":"Ninth Conference on Machine Translation (WMT24)","url":"https://www2.statmt.org/wmt24/"}]

Based on the search results, here's what I found about WMT 2026 research paper submission:

WMT accepts both research and system papers submitted electronically via SoftConf with the same deadlines, and papers should follow EMNLP formatting guidelines.

However, the search results don't show a specific deadline date listed on the WMT 2026 page itself. However, since WMT will participate in the ACL Rolling Review, and any ARR-reviewed paper that received all of its reviews and meta-reviews available by the ARR commitment deadline will be considered for publication at the conference, the relevant deadline would be the ARR Submission Deadline of May 25, 2026.

For more specific details about WMT 2026's own submission deadlines and requirements, you may want to check the official WMT 2026 website directly at https://www2.statmt.org/wmt26/index.html.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a26eb90d-65dc-4853-98ee-3cd12ed75253",
  "isSidechain": true,
  "promptId": "504e2971-a17d-4553-9508-335bf1f3968f",
  "agentId": "ac3625b267e3eea76",
  "type": "user",
  "uuid": "78657e86-1e92-4559-b15a-cc48e0acab1b",
  "sourceToolAssistantUUID": "a26eb90d-65dc-4853-98ee-3cd12ed75253",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "072a3a1a-465c-4992-a530-3e78def2ac5a",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 49 · 2026-05-19T19:09:56.705Z_

<details><summary>↩ Tool result · `toolu_01N49BHFDAnRKbz4RBbLQL8p`</summary>

```text
Web search results for query: "site:github.com "token tax" multilingual tokenization"

Links: [{"title":"GitHub - keon/awesome-nlp: :book: A curated list of resources dedicated to Natural Language Processing (NLP) · GitHub","url":"https://github.com/keon/awesome-nlp"},{"title":"GitHub - remeinium/WWHO: Seperate before you Compress: The WWHO Tokenization Architecture. See the Tokenization Flow using following url. · GitHub","url":"https://github.com/remeinium/WWHO"},{"title":"TokenTaxonomyFramework/token-taxonomy.md at main · InterWorkAlliance/TokenTaxonomyFramework","url":"https://github.com/InterWorkAlliance/TokenTaxonomyFramework/blob/main/token-taxonomy.md"},{"title":"GitHub - Consensys/UniversalToken: Implementation of Universal Token for Assets and Payments · GitHub","url":"https://github.com/Consensys/UniversalToken"}]

Based on the search results, I found relevant information about "token tax" and multilingual tokenization on GitHub:

## Key Findings

The Token Tax is a research paper from 2025 that quantifies how tokenization fertility predicts model accuracy across languages, exposing structural cost penalties for morphologically complex and low-resource languages.

Additionally, there's a related project called WWHO (Where-What-How Often) that addresses this issue. Byte-Pair Encoding and its descendants routinely shatter complex conjuncts—atomic multi-codepoint grapheme clusters that constitute the fundamental phonetic units of Indic and Southeast Asian writing systems—into meaningless sub-character fragments, resulting in degraded reasoning, inflated inference costs, and a systemic "Token Tax" that disproportionately burdens more than one billion speakers. WWHO radically compresses the context window for Abugida text, effectively ending the Token Tax without penalizing existing state-of-the-art programming and reasoning capabilities.

The search results show that this research and these projects are actively addressing the challenges of how different languages are tokenized in language models, particularly focusing on non-Latin writing systems and low-resource languages.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "536a644d-d6a7-44d2-94f4-53430f96b19f",
  "isSidechain": true,
  "promptId": "504e2971-a17d-4553-9508-335bf1f3968f",
  "agentId": "ac3625b267e3eea76",
  "type": "user",
  "uuid": "3daeffec-25bb-4039-a310-45848642392f",
  "sourceToolAssistantUUID": "536a644d-d6a7-44d2-94f4-53430f96b19f",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "072a3a1a-465c-4992-a530-3e78def2ac5a",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 50 · 2026-05-19T19:09:57.781Z_

<details><summary>↩ Tool result · `toolu_01VpDws678rbHGuYC3qULopW`</summary>

```text
Web search results for query: "site:github.com "causal mediation analysis" NLP transformer"

Links: [{"title":"GitHub - zhijing-jin/CausalNLP_Papers: A reading list for papers on causality for natural language processing (NLP) · GitHub","url":"https://github.com/zhijing-jin/CausalNLP_Papers"},{"title":"Causal Mediation Analysis for Interpreting Neural NLP: The Case of   Gender Bias","url":"https://arxiv.org/pdf/2004.12265"},{"title":"[2004.12265] Causal Mediation Analysis for Interpreting Neural NLP: The Case of Gender Bias","url":"https://arxiv.org/abs/2004.12265"},{"title":"GitHub - sebastianGehrmann/CausalMediationAnalysis: Code for the paper \"Causal Mediation Analysis for Interpreting Neural NLP: The Case of Gender Bias\"","url":"https://github.com/sebastianGehrmann/CausalMediationAnalysis"},{"title":"causal-models · GitHub Topics · GitHub","url":"https://github.com/topics/causal-models?l=python"},{"title":"Estimating the Causal Effects of Natural Logic Features in   Transformer-Based NLI Models","url":"https://arxiv.org/pdf/2404.02622"},{"title":"GitHub - causaltext/causal-text-papers: Curated research at the intersection of causal inference and natural language processing.","url":"https://github.com/causaltext/causal-text-papers"},{"title":"Transformer-Specific Interpretability","url":"https://explanation-llm.github.io/slides/section_4_slides.pdf"}]

I found relevant GitHub repositories and resources for causal mediation analysis in NLP with transformers:

## Key GitHub Repositories:

1. **CausalMediationAnalysis** - This repository contains the code to replicate the experiments for the paper "Causal Mediation Analysis for Interpreting Neural NLP: The Case of Gender Bias". The repository is located at: https://github.com/sebastianGehrmann/CausalMediationAnalysis

2. **CausalNLP_Papers** - A reading list for papers on causality for NLP available at: https://github.com/zhijing-jin/CausalNLP_Papers. "Causal Mediation Analysis for Interpreting Neural NLP: The Case of Gender Bias" by Jesse Vig, Sebastian Gehrmann, Yonatan Belinkov, Sharon Qian, Daniel Nevo, Simas Sakenis, Jason Huang, Yaron Singer, Stuart Shieber is featured in this collection.

3. **Causal-Text-Papers** - https://github.com/causaltext/causal-text-papers contains curated research at the intersection of causal inference and NLP.

## Key Research:

The methodology uses causal mediation analysis for interpreting which parts of a model are causally implicated in its behavior, enabling analysis of mechanisms by which information flows from input to output through various model components, and applies this to analyze gender bias in pre-trained Transformer language models by studying the role of individual neurons and attention heads.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "98c56618-6908-44b1-8499-021be21a1339",
  "isSidechain": true,
  "promptId": "504e2971-a17d-4553-9508-335bf1f3968f",
  "agentId": "ac3625b267e3eea76",
  "type": "user",
  "uuid": "1782135d-c7f6-449b-8cb9-2b63e30314f2",
  "sourceToolAssistantUUID": "98c56618-6908-44b1-8499-021be21a1339",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "072a3a1a-465c-4992-a530-3e78def2ac5a",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 51 · 2026-05-19T19:09:58.161Z_

<details><summary>↩ Tool result · `toolu_019Uao18P8zU8N2HxH2y7Ped`</summary>

```text
Web search results for query: "site:github.com "regression discontinuity" tokenization NLP"

Links: [{"title":"Causal Estimation of Tokenisation Bias","url":"https://arxiv.org/pdf/2506.03149"},{"title":"How Much is Enough? The Diminishing Returns of Tokenization Training Data","url":"https://arxiv.org/pdf/2502.20273"},{"title":"Regression Discontinuity for Causal Effect Estimation in Epidemiology","url":"https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4978750/"},{"title":"Noise-Induced Randomization in Regression Discontinuity Designs","url":"https://arxiv.org/pdf/2004.09458"},{"title":"Tokenization Consistency Matters for Generative Models on Extractive NLP   Tasks","url":"https://arxiv.org/pdf/2212.09912"},{"title":"GitHub - nxarteagag/rddsw: Regression discontinuity","url":"https://github.com/nxarteagag/rddsw"},{"title":"GitHub - NataliArteaga/rddsw: regression discontinuity","url":"https://github.com/NataliArteaga/rddsw/"}]

I found some relevant results for your search query. The most notable finding is a research paper that directly combines regression discontinuity design with NLP tokenization:

A paper titled "Causal Estimation of Tokenisation Bias" frames tokenisation bias as a causal effect and estimates it using the regression discontinuity design. The approach exploits the fact that tokenisation algorithms rank subwords and add the first K to a tokeniser's vocabulary at an arbitrary cutoff point, allowing researchers to estimate a causal effect by comparing similar subwords around this cutoff. The research finds that tokenisation consistently affects models' outputs across scales, vocabularies, and tokenisers.

I also found other tokenization-related NLP papers and some GitHub repositories related to regression discontinuity methods, though the latter don't appear to specifically combine both concepts.

The arxiv paper (index 1-1 to 1-11) appears to be the most directly relevant result to your specific query combining regression discontinuity, tokenization, and NLP.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f2df057f-797f-4950-ad05-85f4ff8068c0",
  "isSidechain": true,
  "promptId": "504e2971-a17d-4553-9508-335bf1f3968f",
  "agentId": "ac3625b267e3eea76",
  "type": "user",
  "uuid": "5dadf03f-164e-4831-899e-72314fee084a",
  "sourceToolAssistantUUID": "f2df057f-797f-4950-ad05-85f4ff8068c0",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "072a3a1a-465c-4992-a530-3e78def2ac5a",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 52 · 2026-05-19T19:09:59.277Z_

<details><summary>↩ Tool result · `toolu_01D1u5qu4XR96tMkNLKRyC7v`</summary>

```text
Web search results for query: "site:github.com "selective translation" multilingual NLP code"

Links: [{"title":"GitHub - atharva-naik/MultiLingProject: Multilingual NLP term project. Unified translation of multilingual code and natural languages. · GitHub","url":"https://github.com/atharva-naik/MultiLingProject"},{"title":"multilingual-translation · GitHub Topics · GitHub","url":"https://github.com/topics/multilingual-translation"},{"title":"multilingual-translations · GitHub Topics · GitHub","url":"https://github.com/topics/multilingual-translations"},{"title":"GitHub - DevSinghSachan/multilingual_nmt: Experiments on Multilingual NMT","url":"https://github.com/DevSinghSachan/multilingual_nmt"},{"title":"multilingual-nlp · GitHub Topics · GitHub","url":"https://github.com/topics/multilingual-nlp"},{"title":"GitHub - aboSamoor/polyglot: Multilingual text (NLP) processing toolkit · GitHub","url":"https://github.com/aboSamoor/polyglot"},{"title":"GitHub - multilingual-dh/nlp-resources: Natural language processing resources for multiple languages, with an eye towards use for digital humanities.","url":"https://github.com/multilingual-dh/nlp-resources"}]

I've performed the web search for "site:github.com 'selective translation' multilingual NLP code". Here are the results:

The search returned several GitHub repositories related to multilingual NLP and translation:

1. **MultiLingProject** (atharva-naik/MultiLingProject): A multilingual NLP term project focused on unified translation of multilingual code and natural languages.

2. **multilingual_nmt** (DevSinghSachan/multilingual_nmt): A codebase used for multilingual translation experiments for the paper "Parameter Sharing Methods for Multilingual Self-Attentional Translation Models, WMT-EMNLP 2018". The multilingual model is based on the Transformer model.

3. **Polyglot** (aboSamoor/polyglot): A natural language pipeline that supports massive multilingual applications.

4. **NLP Resources** (multilingual-dh/nlp-resources): A repository containing natural language processing resources for multiple languages with a focus on digital humanities applications.

The search also returned GitHub topic pages for "multilingual-translation" and "multilingual-nlp" with references to various projects and tools in this space.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "fa3c43cf-61d0-44de-8b88-7a6eda95f929",
  "isSidechain": true,
  "promptId": "504e2971-a17d-4553-9508-335bf1f3968f",
  "agentId": "ac3625b267e3eea76",
  "type": "user",
  "uuid": "23892e60-b7c5-4387-be67-bcd67ce2997b",
  "sourceToolAssistantUUID": "fa3c43cf-61d0-44de-8b88-7a6eda95f929",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "072a3a1a-465c-4992-a530-3e78def2ac5a",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 53 · 2026-05-19T19:09:59.375Z_

<details><summary>↩ Tool result · `toolu_01JgZiMA8npddkMYAyHHoNAZ`</summary>

```text
Web search results for query: "site:github.com "tokenization fertility" multilingual measurement"

Links: [{"title":"Beyond Fertility: Analyzing STRR as a Metric for Multilingual Tokenization Evaluation","url":"https://arxiv.org/pdf/2510.09947"},{"title":"The Script Tax: Measuring Tokenization-Driven Efficiency and Latency Disparities in Multilingual Language Models","url":"https://arxiv.org/pdf/2602.11174"},{"title":"The Token Tax: Systematic Bias in Multilingual Tokenization","url":"https://arxiv.org/pdf/2509.05486"},{"title":"MUTANT: A Recipe for Multilingual Tokenizer Design","url":"https://arxiv.org/pdf/2511.03237"},{"title":"GitHub - keon/awesome-nlp: :book: A curated list of resources dedicated to Natural Language Processing (NLP) · GitHub","url":"https://github.com/keon/awesome-nlp"},{"title":"Qtok: A Comprehensive Framework for Evaluating Multilingual Tokenizer   Quality in Large Language Models","url":"https://arxiv.org/pdf/2410.12989"}]

Based on the search results, I found several relevant research papers and resources related to tokenization fertility and multilingual measurement:

**Key Papers:**

1. **"Beyond Fertility: Analyzing STRR as a Metric for Multilingual Tokenization Evaluation"** - This paper notes that fertility (the average number of tokens per word) captures compression efficiency but obscures how vocabularies are allocated across languages and domains. The authors propose the Single Token Retention Rate (STRR) as an alternative metric that measures the proportion of words preserved as single tokens, revealing systematic prioritization of English, strong support for Chinese, and fragmentation in Hindi.

2. **"The Script Tax: Measuring Tokenization-Driven Efficiency and Latency Disparities in Multilingual Language Models"** - This study found that across mBERT and XLM-R, the higher-fragmentation orthography shows approximately a 3.4× increase in fertility (6.73–6.85 vs. 2.10-2.35 tokens/word), leading to a 16.5× inference slowdown.

3. **"The Token Tax: Systematic Bias in Multilingual Tokenization"** - This research evaluated 10 large language models and showed that fertility (tokens/word) reliably predicts accuracy, with higher fertility consistently predicting lower accuracy across all models and subjects.

4. **"MUTANT: A Recipe for Multilingual Tokenizer Design"** - This paper discusses how tokenization remains an understudied topic in multilingual settings, where skewed fertility scores across languages often lead to concerns around fairness, high inference latency, cost and context size.

5. **Qtok Framework** - A comprehensive framework available at https://github.com/nup-csai/Qtok/ for evaluating multilingual tokenizer quality in large language models.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "36b7126e-786d-46a5-ab4d-dcca69f31987",
  "isSidechain": true,
  "promptId": "504e2971-a17d-4553-9508-335bf1f3968f",
  "agentId": "ac3625b267e3eea76",
  "type": "user",
  "uuid": "a4557c0c-a762-436e-9846-8b14e80a5221",
  "sourceToolAssistantUUID": "36b7126e-786d-46a5-ab4d-dcca69f31987",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "072a3a1a-465c-4992-a530-3e78def2ac5a",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 54 · 2026-05-19T19:10:01.641Z_

<details><summary>↩ Tool result · `toolu_01RovW7PcwhSTMmSm9Mpuon6`</summary>

```text
Web search results for query: "site:github.com AfriMMLU evaluation benchmark African languages"

Links: [{"title":"GitHub - The-African-Research-Collective/afrobench-eval-suite: LLM Eval leaderboard for African Languages","url":"https://github.com/The-African-Research-Collective/afrobench-eval-suite"},{"title":"IrokoBench: A New Benchmark for African Languages in the Age of Large   Language Models","url":"https://arxiv.org/pdf/2406.03368"},{"title":"[EVAL]: Add more African Benchmarks · Issue #373 · huggingface/lighteval","url":"https://github.com/huggingface/lighteval/issues/373"},{"title":"GitHub - McGill-NLP/AfroBench: Large Scale Benchmark of Large Language Models on African Languages","url":"https://github.com/McGill-NLP/AfroBench"},{"title":"Irokobench: Benchmark Dataset for African languages by JessicaOjo · Pull Request #2042 · EleutherAI/lm-evaluation-harness","url":"https://github.com/EleutherAI/lm-evaluation-harness/pull/2042"},{"title":"Afri-MCQA: Multimodal Cultural Question Answering for African Languages","url":"https://arxiv.org/pdf/2601.05699"},{"title":"GitHub - masakhane-io/masakhane-nlu: Lacuna funded project to create benchmark dataset for AfricaNLI, AfricaMGSM, AfricaMMLU, and cultural relevant intent classificationand slot filling detection datasets","url":"https://github.com/masakhane-io/masakhane-nlu"},{"title":"Lugha-Llama: Adapting Large Language Models for African Languages","url":"https://arxiv.org/pdf/2504.06536"}]

Based on the search results, here's what I found about AfriMMLU and related evaluation benchmarks for African languages:

## AfriMMLU Overview

AfriMMLU is a multilingual multi-choice language understanding benchmark in 16 languages of focus across a variety of topics. The task is to predict the correct answer to a multiple-choice question given a context and a list of possible answers.

## Related Benchmarks

AfriMMLU is part of IrokoBench—a human-translated benchmark dataset for 17 typologically-diverse low-resource African languages covering three tasks: natural language inference (AfriXNLI), mathematical reasoning (AfriMGSM), and multi-choice knowledge-based question answering (AfriMMLU).

Additionally, AfroBench is an open, multilingual benchmark designed to evaluate Large Language Models (LLMs) across 64 African languages, 15 NLP tasks, and 22 datasets — covering classification, QA, reasoning, generation, and more.

## Key Findings

Evaluation reveals a significant performance gap between high-resource languages (such as English and French) and low-resource African languages.

The search results reference several GitHub repositories hosting these evaluation suites, including the African Research Collective's afrobench-eval-suite, McGill-NLP's AfroBench, and integration with major evaluation frameworks like the EleutherAI's lm-evaluation-harness.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "b50a8b39-080b-4eba-9a71-bb29295fb2e3",
  "isSidechain": true,
  "promptId": "504e2971-a17d-4553-9508-335bf1f3968f",
  "agentId": "ac3625b267e3eea76",
  "type": "user",
  "uuid": "6a7ce21e-e480-4862-b16a-b4d48657265e",
  "sourceToolAssistantUUID": "b50a8b39-080b-4eba-9a71-bb29295fb2e3",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "072a3a1a-465c-4992-a530-3e78def2ac5a",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 55 · 2026-05-19T19:10:04.794Z_

Now let me get a few more specific details.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6a7ce21e-e480-4862-b16a-b4d48657265e",
  "isSidechain": true,
  "agentId": "ac3625b267e3eea76",
  "requestId": "req_011CbCTNvcWEJmMFS9mBe9kC",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "5a9841bf-4729-4497-a6b1-abce73e317ee",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "072a3a1a-465c-4992-a530-3e78def2ac5a",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01X4ckrcCSmUHGiR7NDMQ9bY",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1220,
      "cache_creation_input_tokens": 7032,
      "cache_read_input_tokens": 19623,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 7032,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 1,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": {
      "cache_miss_reason": {
        "type": "unavailable"
      }
    }
  }
}
```

</details>

---

### Tool call

_source line 56 · 2026-05-19T19:10:05.435Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Jkx83bL4dwBAhWpNiLYaS6`</summary>

```json
{
  "query": "github.com sebastianGehrmann CausalMediationAnalysis code implementation"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5a9841bf-4729-4497-a6b1-abce73e317ee",
  "isSidechain": true,
  "agentId": "ac3625b267e3eea76",
  "requestId": "req_011CbCTNvcWEJmMFS9mBe9kC",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "c887f66d-a1b5-4b6f-a8cd-4dd11400c57d",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "072a3a1a-465c-4992-a530-3e78def2ac5a",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01X4ckrcCSmUHGiR7NDMQ9bY",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1220,
      "cache_creation_input_tokens": 7032,
      "cache_read_input_tokens": 19623,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 7032,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 1,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": {
      "cache_miss_reason": {
        "type": "unavailable"
      }
    }
  }
}
```

</details>

---

### Tool call

_source line 57 · 2026-05-19T19:10:06.206Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01HsV3GQPgq9qcXagbcJkqkJ`</summary>

```json
{
  "query": "github.com masakhane-io masakhane-nlu AfriMMLU code evaluation"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c887f66d-a1b5-4b6f-a8cd-4dd11400c57d",
  "isSidechain": true,
  "agentId": "ac3625b267e3eea76",
  "requestId": "req_011CbCTNvcWEJmMFS9mBe9kC",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "e5d386bb-f568-4d35-b95a-aa993901e0bd",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "072a3a1a-465c-4992-a530-3e78def2ac5a",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01X4ckrcCSmUHGiR7NDMQ9bY",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1220,
      "cache_creation_input_tokens": 7032,
      "cache_read_input_tokens": 19623,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 7032,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 1,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": {
      "cache_miss_reason": {
        "type": "unavailable"
      }
    }
  }
}
```

</details>

---

### Tool call

_source line 58 · 2026-05-19T19:10:06.677Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01DHqJwjNLr24sQSpmpRAn5w`</summary>

```json
{
  "query": "\"causal estimation tokenisation bias\" regression discontinuity github code"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e5d386bb-f568-4d35-b95a-aa993901e0bd",
  "isSidechain": true,
  "agentId": "ac3625b267e3eea76",
  "requestId": "req_011CbCTNvcWEJmMFS9mBe9kC",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "0fab6b2d-f995-4b61-bded-497a5c3873ac",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "072a3a1a-465c-4992-a530-3e78def2ac5a",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01X4ckrcCSmUHGiR7NDMQ9bY",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1220,
      "cache_creation_input_tokens": 7032,
      "cache_read_input_tokens": 19623,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 7032,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 1,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": {
      "cache_miss_reason": {
        "type": "unavailable"
      }
    }
  }
}
```

</details>

---

### Tool call

_source line 59 · 2026-05-19T19:10:07.617Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Gzi4jYKr9Z1k5g4nnKtxgh`</summary>

```json
{
  "query": "github.com nup-csai Qtok tokenization fertility multilingual evaluation code"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0fab6b2d-f995-4b61-bded-497a5c3873ac",
  "isSidechain": true,
  "agentId": "ac3625b267e3eea76",
  "requestId": "req_011CbCTNvcWEJmMFS9mBe9kC",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "33c79c70-66fb-4ca0-849d-17fc7abb7074",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "072a3a1a-465c-4992-a530-3e78def2ac5a",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01X4ckrcCSmUHGiR7NDMQ9bY",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1220,
      "cache_creation_input_tokens": 7032,
      "cache_read_input_tokens": 19623,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 7032,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 1,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": {
      "cache_miss_reason": {
        "type": "unavailable"
      }
    }
  }
}
```

</details>

---

### Tool call

_source line 60 · 2026-05-19T19:10:08.149Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_019y1xbh1dXMN5P3L7TovjPr`</summary>

```json
{
  "query": "COLING 2026 deadline date Abu Dhabi submission"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "33c79c70-66fb-4ca0-849d-17fc7abb7074",
  "isSidechain": true,
  "agentId": "ac3625b267e3eea76",
  "requestId": "req_011CbCTNvcWEJmMFS9mBe9kC",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "bd351f67-b680-4b69-9109-2313435e5fbb",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "072a3a1a-465c-4992-a530-3e78def2ac5a",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01X4ckrcCSmUHGiR7NDMQ9bY",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1220,
      "cache_creation_input_tokens": 7032,
      "cache_read_input_tokens": 19623,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 7032,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 1,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": {
      "cache_miss_reason": {
        "type": "unavailable"
      }
    }
  }
}
```

</details>

---

### Tool result

_source line 61 · 2026-05-19T19:10:12.629Z_

<details><summary>↩ Tool result · `toolu_01Jkx83bL4dwBAhWpNiLYaS6`</summary>

```text
Web search results for query: "github.com sebastianGehrmann CausalMediationAnalysis code implementation"

Links: [{"title":"GitHub - sebastianGehrmann/CausalMediationAnalysis: Code for the paper \"Causal Mediation Analysis for Interpreting Neural NLP: The Case of Gender Bias\"","url":"https://github.com/sebastianGehrmann/CausalMediationAnalysis"},{"title":"CausalMediationAnalysis/winobias.py at master · sebastianGehrmann/CausalMediationAnalysis","url":"https://github.com/sebastianGehrmann/CausalMediationAnalysis/blob/master/winobias.py"},{"title":"CausalMediationAnalysis/attention_intervention_winobias.py at master · sebastianGehrmann/CausalMediationAnalysis","url":"https://github.com/sebastianGehrmann/CausalMediationAnalysis/blob/master/attention_intervention_winobias.py"},{"title":"CausalMediationAnalysis/attention_intervention_winobias.sh at master · sebastianGehrmann/CausalMediationAnalysis","url":"https://github.com/sebastianGehrmann/CausalMediationAnalysis/blob/master/attention_intervention_winobias.sh"},{"title":"sebastianGehrmann (Sebastian Gehrmann) · GitHub","url":"https://github.com/sebastianGehrmann"},{"title":"[2004.12265] Causal Mediation Analysis for Interpreting Neural NLP: The Case of Gender Bias","url":"https://ar5iv.labs.arxiv.org/html/2004.12265"},{"title":"Investigating Gender Bias in Language Models Using Causal Mediation Analysis","url":"https://proceedings.neurips.cc/paper/2020/file/92650b2e92217715fe312e6fa7b90d82-Paper.pdf"},{"title":"MEDIATION ANALYSIS FOR INTERPRETING NLP: GENDER BIAS","url":"https://arxiv.org/pdf/2004.12265"},{"title":"causal-mediation-analysis · GitHub Topics","url":"https://github.com/topics/causal-mediation-analysis"},{"title":"Sebastian Gehrmann","url":"https://sebastiangehrmann.github.io/"}]

I found the repository you're looking for! The CausalMediationAnalysis repository contains code for the paper "Causal Mediation Analysis for Interpreting Neural NLP: The Case of Gender Bias".

Here are the key details about the code implementation:

**Location:** https://github.com/sebastianGehrmann/CausalMediationAnalysis

**Main Components:**
- You can run attention intervention experiments using either the attention_intervention_winobias.py or attention_intervention_winogender.py scripts
- The arguments are specified in the respective script in the intervene_attention method, with all possible configurations documented in attention_intervention_winobias.sh or attention_intervention_winogender.sh

**Data:**
- Analysis JSON files for Winogender and Winobias are already available in the winogender_data and winobias_data directories
- The raw Winogender and Winobias datasets were obtained from https://github.com/rudinger/winogender-schemas and from https://github.com/uclanlp/corefBias/tree/master/WinoBias/wino/data respectively

The repository uses Python and implements causal mediation analysis techniques to interpret gender bias in neural NLP models.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c887f66d-a1b5-4b6f-a8cd-4dd11400c57d",
  "isSidechain": true,
  "promptId": "504e2971-a17d-4553-9508-335bf1f3968f",
  "agentId": "ac3625b267e3eea76",
  "type": "user",
  "uuid": "8ec379c4-3824-41a9-807a-ab648d54e793",
  "sourceToolAssistantUUID": "c887f66d-a1b5-4b6f-a8cd-4dd11400c57d",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "072a3a1a-465c-4992-a530-3e78def2ac5a",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 62 · 2026-05-19T19:10:12.524Z_

<details><summary>↩ Tool result · `toolu_01HsV3GQPgq9qcXagbcJkqkJ`</summary>

```text
Web search results for query: "github.com masakhane-io masakhane-nlu AfriMMLU code evaluation"

Links: [{"title":"GitHub - masakhane-io/masakhane-nlu: Lacuna funded project to create benchmark dataset for AfricaNLI, AfricaMGSM, AfricaMMLU, and cultural relevant intent classificationand slot filling detection datasets","url":"https://github.com/masakhane-io/masakhane-nlu"},{"title":"masakhane/afrimmlu · Datasets at Hugging Face","url":"https://huggingface.co/datasets/masakhane/afrimmlu"},{"title":"Masakhane · GitHub","url":"https://github.com/masakhane-io"},{"title":"GitHub - masakhane-io/masakhane-mt: Machine Translation for Africa · GitHub","url":"https://github.com/masakhane-io/masakhane-mt"},{"title":"GitHub - masakhane-io/masakhane-community: All our community docs! Start here! Lets put Africa on the NLP Map · GitHub","url":"https://github.com/masakhane-io/masakhane-community"},{"title":"GitHub - masakhane-io/masakhane-ner · GitHub","url":"https://github.com/masakhane-io/masakhane-ner"},{"title":"masakhane-nlu/InjongoIntent at main · masakhane-io/masakhane-nlu","url":"https://github.com/masakhane-io/masakhane-nlu/tree/main/InjongoIntent"},{"title":"GitHub - masakhane-io/masakhane-news: MasakhaNEWS: News Topic Classification for African Languages","url":"https://github.com/masakhane-io/masakhane-news"}]

Based on the search results, here's what I found about the masakhane-io masakhane-nlu AfriMMLU project:

The masakhane-nlu repository is a Lacuna funded project to create benchmark datasets for AfricaNLI, AfricaMGSM, AfricaMMLU, and cultural relevant intent classification and slot filling detection datasets. It includes IrokoBench, a human-translated benchmark dataset for 16 typologically-diverse low-resource African languages covering three tasks: natural language inference (AfriXNLI), mathematical reasoning (AfriMGSM), and multi-choice knowledge-based QA (AfriMMLU).

AfriMMLU is an evaluation dataset comprising translations of a subset of the MMLU dataset into 15 African languages, with test sets across all 17 languages, maintaining English and French subsets from the original MMLU dataset.

The datasets are also available on HuggingFace. You can access the repository at https://github.com/masakhane-io/masakhane-nlu and the dataset at https://huggingface.co/datasets/masakhane/afrimmlu.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "e5d386bb-f568-4d35-b95a-aa993901e0bd",
  "isSidechain": true,
  "promptId": "504e2971-a17d-4553-9508-335bf1f3968f",
  "agentId": "ac3625b267e3eea76",
  "type": "user",
  "uuid": "6d8d6499-ef20-4227-8af8-e8a4f84d42f9",
  "sourceToolAssistantUUID": "e5d386bb-f568-4d35-b95a-aa993901e0bd",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "072a3a1a-465c-4992-a530-3e78def2ac5a",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 63 · 2026-05-19T19:10:14.772Z_

<details><summary>↩ Tool result · `toolu_01DHqJwjNLr24sQSpmpRAn5w`</summary>

```text
Web search results for query: ""causal estimation tokenisation bias" regression discontinuity github code"

Links: [{"title":"Causal Estimation of Tokenisation Bias - ACL Anthology","url":"https://aclanthology.org/2025.acl-long.1374/"},{"title":"Causal Estimation of Tokenisation Bias","url":"https://arxiv.org/html/2506.03149v1"},{"title":"[2506.03149] Causal Estimation of Tokenisation Bias","url":"https://arxiv.org/abs/2506.03149"},{"title":"GitHub - pietrolesci/tokenisation-bias","url":"https://github.com/pietrolesci/tokenisation-bias"},{"title":"Causal Estimation of Tokenisation Bias","url":"https://arxiv.org/pdf/2506.03149"},{"title":"Causal Estimation of Tokenisation Bias","url":"https://aclanthology.org/2025.acl-long.1374.pdf"},{"title":"GitHub - roccojhu/neural_regression_discontinuity: In this repository, I modify a quasi-experimental statistical procedure for time-series inference using convolutional long short-term memory networks.","url":"https://github.com/roccojhu/neural_regression_discontinuity"},{"title":"Regression Discontinuity for Causal Effect Estimation in Epidemiology","url":"https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4978750/"}]

Based on the search results, here's what I found about causal estimation of tokenisation bias using regression discontinuity:

## Research Paper

The choice of tokeniser, which maps character-strings to subwords, can affect the probability assigned to the underlying character-string; this mismatch is defined as tokenisation bias.

The research addresses this by framing tokenisation bias as a causal effect and estimating it using the regression discontinuity design. Tokenisation algorithms rank subwords and add the first K to a tokeniser's vocabulary at an arbitrary cutoff point; a causal effect can be estimated by comparing similar subwords around this cutoff.

## Key Findings

The bias in BPE was estimated at 2.88 nats, meaning a character-string can be assigned roughly 17 times less probability due solely to tokenisation. Tokenisation consistently affects models' outputs across scales, vocabularies, and tokenisers.

## GitHub Repository

The code implementing this approach is available at https://github.com/pietrolesci/tokenisation-bias, which contains the implementation of the regression discontinuity design for estimating tokenisation bias.

The paper was recently published in ACL 2025 and is also available on arXiv (2506.03149).


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "0fab6b2d-f995-4b61-bded-497a5c3873ac",
  "isSidechain": true,
  "promptId": "504e2971-a17d-4553-9508-335bf1f3968f",
  "agentId": "ac3625b267e3eea76",
  "type": "user",
  "uuid": "9a3245d5-eb3b-481e-9449-da0fdf8d4005",
  "sourceToolAssistantUUID": "0fab6b2d-f995-4b61-bded-497a5c3873ac",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "072a3a1a-465c-4992-a530-3e78def2ac5a",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 64 · 2026-05-19T19:10:15.487Z_

<details><summary>↩ Tool result · `toolu_01Gzi4jYKr9Z1k5g4nnKtxgh`</summary>

```text
Web search results for query: "github.com nup-csai Qtok tokenization fertility multilingual evaluation code"

Links: [{"title":"Qtok: A Comprehensive Framework for Evaluating Multilingual Tokenizer Quality in Large Language Models","url":"https://arxiv.org/html/2410.12989v1"},{"title":"qtok:acomprehensive framework for evaluating multilingual ...","url":"https://arxiv.org/pdf/2410.12989"},{"title":"Multilingual Tokenizer Advances","url":"https://www.emergentmind.com/topics/multilingual-tokenizer"},{"title":"[2410.12989] Qtok: A Comprehensive Framework for Evaluating Multilingual Tokenizer Quality in Large Language Models","url":"https://arxiv.org/abs/2410.12989"},{"title":"Multilingual Tokenizers","url":"https://www.emergentmind.com/topics/multilingual-tokenizers"},{"title":"GitHub - nup-csai/Qtok","url":"https://github.com/nup-csai/Qtok/"},{"title":"Beyond Fertility: Analyzing STRR as a Metric for Multilingual Tokenization Evaluation","url":"https://arxiv.org/pdf/2510.09947"},{"title":"[2510.09947] Beyond Fertility: Analyzing STRR as a Metric for Multilingual Tokenization Evaluation","url":"https://arxiv.org/abs/2510.09947"}]

Based on the search results, I found comprehensive information about the Qtok project:

## Qtok - Multilingual Tokenizer Evaluation Framework

Qtok is a tool designed to evaluate tokenizer quality, with a focus on multilingual performance. It is a Python-based tool designed for quality control and analysis of tokenizers used in natural language processing (NLP) tasks.

**Repository:** The code is available at https://github.com/nup-csai/Qtok/

**Key Features:**

Qtok offers metrics that assess tokenizers both at the system level and for individual tokens, examining factors like token completeness, accuracy, and distribution across different languages.

The research proposes a set of metrics for evaluating tokenizer quality, including measures of language coverage, token completeness, and distribution across languages and linguistic categories.

**Evaluation Scope:**

Qtok performed an in-depth evaluation of popular tokenizers from the Chatbot Arena dataset, identifying 13 distinct tokenizers across 58 models.

**Key Contribution:**

One of the key contributions of this work is the introduction of the concept of core tokens—tokens that consistently appear across different tokenizers, grouped by the vocabulary size, regardless of the specific model or dataset from which they are derived.

The framework addresses the important role of tokenization in multilingual LLM development and provides systematic evaluation metrics including measures related to fertility (a metric measuring the average number of tokens per word).


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "33c79c70-66fb-4ca0-849d-17fc7abb7074",
  "isSidechain": true,
  "promptId": "504e2971-a17d-4553-9508-335bf1f3968f",
  "agentId": "ac3625b267e3eea76",
  "type": "user",
  "uuid": "33c5d594-fbac-4abe-a8e0-45ecd859c165",
  "sourceToolAssistantUUID": "33c79c70-66fb-4ca0-849d-17fc7abb7074",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "072a3a1a-465c-4992-a530-3e78def2ac5a",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 65 · 2026-05-19T19:10:12.920Z_

<details><summary>↩ Tool result · `toolu_019y1xbh1dXMN5P3L7TovjPr`</summary>

```text
Web search results for query: "COLING 2026 deadline date Abu Dhabi submission"

Links: [{"title":"COLING 2026 - International Conference on Computational Linguistics Deadline | ConferenceDeadlines.com","url":"https://www.conferencedeadlines.com/venue/coling"},{"title":"https://ivader.unist.ac.kr/importantDates","url":"https://ivader.unist.ac.kr/importantDates"},{"title":"COLING: International Conference on Computational Linguistics 2027 2026 2025 ...","url":"http://www.wikicfp.com/cfp/program?id=533"},{"title":"COLING 2025 : [CFT] International Conference on Computational Linguistics - Tutorials","url":"http://www.wikicfp.com/cfp/servlet/event.showcfp?copyownerid=90704&eventid=180677"},{"title":"AbjadNLP 2026 – The 2nd Workshop on NLP for Languages Using Arabic Script","url":"https://wp.lancs.ac.uk/abjad/"},{"title":"The 31st International Conference on Computational Linguistics - COLING 2025","url":"https://coling2025.org/"},{"title":"COLING 2025 : [CFW] International Conference on Computational Linguistics - Call for Workshops (Deadline is Extended)","url":"http://www.wikicfp.com/cfp/servlet/event.showcfp?eventid=180669"},{"title":"International Conference on Computational Linguistics | ADNEC Centre Abu Dhabi","url":"https://www.adnec.ae/en/eventlisting/international-conference-on-computational-linguistics-coling"},{"title":"Conference Deadlines - Ziping Zhao","url":"https://www.ncvxopt.com/conf/"},{"title":"Volunteering deadline for COLING 2025 extension | ACL Member Portal","url":"https://www.aclweb.org/portal/content/deadline-coling-2025-volunteering-call-has-been-extended"}]

Based on my search results, I found that COLING 2025 will take place in Abu Dhabi, UAE from January 19th to 24th, 2025. However, the search results don't contain specific submission deadline information for COLING 2026 in Abu Dhabi.

The search results primarily return information about COLING 2025 (which is already happening this January) rather than COLING 2026. To get accurate submission deadlines for COLING 2026, I'd recommend checking:

1. The official COLING 2026 conference website (once it's announced)
2. The ACL web portal at aclweb.org
3. The WikiCFP database (wikicfp.com) which tracks call for papers

If you have a link to the COLING 2026 conference page or need help finding it, please let me know!


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "bd351f67-b680-4b69-9109-2313435e5fbb",
  "isSidechain": true,
  "promptId": "504e2971-a17d-4553-9508-335bf1f3968f",
  "agentId": "ac3625b267e3eea76",
  "type": "user",
  "uuid": "adcc440d-05c4-4fc4-b406-755fbe8fdf4a",
  "sourceToolAssistantUUID": "bd351f67-b680-4b69-9109-2313435e5fbb",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "072a3a1a-465c-4992-a530-3e78def2ac5a",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 66 · 2026-05-19T19:10:16.032Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01B8SkNuoazuB3p24WhNzMxP`</summary>

```json
{
  "query": "NAACL 2026 Albuquerque dates ARR cycle deadline"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "adcc440d-05c4-4fc4-b406-755fbe8fdf4a",
  "isSidechain": true,
  "agentId": "ac3625b267e3eea76",
  "requestId": "req_011CbCTNvcWEJmMFS9mBe9kC",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "e25f115a-6e78-4fe8-88ba-7c3edc1ba0a0",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "072a3a1a-465c-4992-a530-3e78def2ac5a",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01X4ckrcCSmUHGiR7NDMQ9bY",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1220,
      "cache_creation_input_tokens": 7032,
      "cache_read_input_tokens": 19623,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 7032,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 1,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": {
      "cache_miss_reason": {
        "type": "unavailable"
      }
    }
  }
}
```

</details>

---

### Tool result

_source line 67 · 2026-05-19T19:10:20.158Z_

<details><summary>↩ Tool result · `toolu_01B8SkNuoazuB3p24WhNzMxP`</summary>

```text
Web search results for query: "NAACL 2026 Albuquerque dates ARR cycle deadline"

Links: [{"title":"Dates and Venues","url":"http://aclrollingreview.org/dates"},{"title":"AI Conference Deadlines","url":"https://mlciv.com/ai-deadlines/"},{"title":"NAACL 2026 - Annual Conference of the Nations of the Americas Chapter of the Association for Computational Linguistics Deadline | ConferenceDeadlines.com","url":"https://www.conferencedeadlines.com/venue/naacl"},{"title":"NAACL: Nations of the Americas Chapter of the ACL (Association for Computational Linguistics)","url":"https://naacl.org/"},{"title":"NAACL: North American Chapter of the Association for Computational Linguistics 2027 2026 2025 ...","url":"http://www.wikicfp.com/cfp/program?id=2170"},{"title":"2025 Annual Conference of the Nations of the Americas Chapter of the Association for Computational Linguistics - NAACL-HLT 2025","url":"https://2025.naacl.org/"},{"title":"ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/"},{"title":"Community announcement: Submission dates and process for EACL, NAACL and ACL","url":"https://www.aclweb.org/portal/sites/default/files/Submission%20Dates%20and%20Process%20for%20EACL_NAACL%20and%20ACL%202024-2.pdf"},{"title":"Year-Round Deadlines - Imranur Rahman","url":"https://imranur-rahman.github.io/deadlines/"},{"title":"Announcements | Computational Linguistics","url":"https://submissions.cljournal.org/index.php/cljournal/announcement"}]

Based on the search results, here's what I found about NAACL 2026:

NAACL 2026 will be held in Albuquerque, USA. However, the search results don't contain specific conference dates for NAACL 2026 in Albuquerque. 

Regarding the ARR cycle deadlines for NAACL 2026, ARR switched from 8-week cycles to 10-week cycles, with the new schedule in action starting in May 2025. However, the search results don't include the specific ARR submission deadlines relevant to NAACL 2026.

To get the exact conference dates for NAACL 2026 in Albuquerque and the relevant ARR cycle deadlines, you may want to check the official NAACL 2026 conference website directly, as this detailed information doesn't appear in the current search results.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "e25f115a-6e78-4fe8-88ba-7c3edc1ba0a0",
  "isSidechain": true,
  "promptId": "504e2971-a17d-4553-9508-335bf1f3968f",
  "agentId": "ac3625b267e3eea76",
  "type": "user",
  "uuid": "2a9e0415-8e22-4868-b0cf-8fdc0e7f9074",
  "sourceToolAssistantUUID": "e25f115a-6e78-4fe8-88ba-7c3edc1ba0a0",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "072a3a1a-465c-4992-a530-3e78def2ac5a",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 68 · 2026-05-19T19:10:22.673Z_

Let me get a few final pieces of information.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2a9e0415-8e22-4868-b0cf-8fdc0e7f9074",
  "isSidechain": true,
  "agentId": "ac3625b267e3eea76",
  "requestId": "req_011CbCTQHsxRgmxTiRUkJaHs",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "fcf28614-ff90-4351-b3ef-39706f26ff8d",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "072a3a1a-465c-4992-a530-3e78def2ac5a",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RmJpYoo2ic42Zt7mmQqL37",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 24960,
      "cache_read_input_tokens": 7773,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 24960,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 1,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": {
      "cache_miss_reason": {
        "type": "previous_message_not_found"
      }
    }
  }
}
```

</details>

---

### Tool call

_source line 69 · 2026-05-19T19:10:23.701Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01TabD1kBaoZiSN5nZwBcMgS`</summary>

```json
{
  "query": "ACL rolling review dates venues 2026 2027 ARR submission cycles"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "fcf28614-ff90-4351-b3ef-39706f26ff8d",
  "isSidechain": true,
  "agentId": "ac3625b267e3eea76",
  "requestId": "req_011CbCTQHsxRgmxTiRUkJaHs",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "eff9a638-c7a9-42ad-ac47-30ca1ccfe635",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "072a3a1a-465c-4992-a530-3e78def2ac5a",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RmJpYoo2ic42Zt7mmQqL37",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 24960,
      "cache_read_input_tokens": 7773,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 24960,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 1,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": {
      "cache_miss_reason": {
        "type": "previous_message_not_found"
      }
    }
  }
}
```

</details>

---

### Tool call

_source line 70 · 2026-05-19T19:10:24.173Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_016tKm6S6bZnv3VustwGxsEx`</summary>

```json
{
  "query": "EACL 2027 ARR submission deadline August 2026 commitment deadline"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "eff9a638-c7a9-42ad-ac47-30ca1ccfe635",
  "isSidechain": true,
  "agentId": "ac3625b267e3eea76",
  "requestId": "req_011CbCTQHsxRgmxTiRUkJaHs",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "237cea12-70db-4f3c-ab4c-c34aebf39946",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "072a3a1a-465c-4992-a530-3e78def2ac5a",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RmJpYoo2ic42Zt7mmQqL37",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 24960,
      "cache_read_input_tokens": 7773,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 24960,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 1,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": {
      "cache_miss_reason": {
        "type": "previous_message_not_found"
      }
    }
  }
}
```

</details>

---

### Tool call

_source line 71 · 2026-05-19T19:10:25.172Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Wkb7st9e32rfANBBRbc1HW`</summary>

```json
{
  "query": "ICLR 2027 predicted submission deadline October 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "237cea12-70db-4f3c-ab4c-c34aebf39946",
  "isSidechain": true,
  "agentId": "ac3625b267e3eea76",
  "requestId": "req_011CbCTQHsxRgmxTiRUkJaHs",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "3d89b21c-d4d3-4550-865f-9fa0bf5b9877",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "072a3a1a-465c-4992-a530-3e78def2ac5a",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RmJpYoo2ic42Zt7mmQqL37",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 24960,
      "cache_read_input_tokens": 7773,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 24960,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 1,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": {
      "cache_miss_reason": {
        "type": "previous_message_not_found"
      }
    }
  }
}
```

</details>

---

### Tool call

_source line 72 · 2026-05-19T19:10:25.413Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01AqmpeGSxgkwdUYUK2tTbBs`</summary>

```json
{
  "query": "github \"token tax\" tokenization bias multilingual code implementation paper"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3d89b21c-d4d3-4550-865f-9fa0bf5b9877",
  "isSidechain": true,
  "agentId": "ac3625b267e3eea76",
  "requestId": "req_011CbCTQHsxRgmxTiRUkJaHs",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "2d1cae09-3427-4c9b-a6ca-ece1c3e26b53",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "072a3a1a-465c-4992-a530-3e78def2ac5a",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RmJpYoo2ic42Zt7mmQqL37",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 24960,
      "cache_read_input_tokens": 7773,
      "output_tokens": 228,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 24960
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 228,
          "cache_read_input_tokens": 7773,
          "cache_creation_input_tokens": 24960,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 24960,
            "ephemeral_1h_input_tokens": 0
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": {
      "cache_miss_reason": {
        "type": "previous_message_not_found"
      }
    }
  }
}
```

</details>

---

### Tool result

_source line 73 · 2026-05-19T19:10:28.782Z_

<details><summary>↩ Tool result · `toolu_016tKm6S6bZnv3VustwGxsEx`</summary>

```text
Web search results for query: "EACL 2027 ARR submission deadline August 2026 commitment deadline"

Links: [{"title":"Dates and Venues","url":"http://aclrollingreview.org/dates"},{"title":"The 20th Conference of the European Chapter of the Association for Computational LinguisticsAthens, GreeceMarch 9-14, 2027 -","url":"https://2027.eacl.org/"},{"title":"Call for Main Conference Papers -","url":"https://2026.eacl.org/calls/papers/"},{"title":"EACL 2027 Call for Main Conference Papers","url":"https://2027.eacl.org/calls/papers/"},{"title":"aclrollingreview/dates.md at main · acl-org/aclrollingreview","url":"https://github.com/acl-org/aclrollingreview/blob/main/dates.md"},{"title":"AI Conference Deadlines","url":"https://mlciv.com/ai-deadlines/"},{"title":"eaclmeeting on X: \"📢⚠️ IMPORTANT DATE CORRECTION: the ARR deadline for EACL 2027 is Aug 3, 2026 (not Aug 6 as previously announced). EACL is earlier than usual in '27, so this is the only viable ARR cycle! 📚 All areas of CL/NLP + related fields welcome. Full CfP coming soon. #NLProc #EACL2027\" / X","url":"https://x.com/eaclmeeting/status/2051971432171688436"},{"title":"Call for Student Research Workshop Papers -","url":"https://2026.eacl.org/calls/srw/"},{"title":"AI & ML Conference Deadlines 2026–2027","url":"https://trybibby.com/conference-deadlines"},{"title":"The 19th Conference of the European Chapter of the Association for Computational LinguisticsRabat, MoroccoMarch 24-29, 2026 -","url":"https://2026.eacl.org/"}]

Based on the search results, here are the key deadlines for EACL 2027:

**ARR submission deadline (long & short papers): August 3, 2026 (AoE)**

**Commitment Date: October 11, 2026**

These are the two important dates you were asking about. All deadlines are 11:59PM UTC-12:00 ("anywhere on Earth").


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "237cea12-70db-4f3c-ab4c-c34aebf39946",
  "isSidechain": true,
  "promptId": "504e2971-a17d-4553-9508-335bf1f3968f",
  "agentId": "ac3625b267e3eea76",
  "type": "user",
  "uuid": "1f026f3d-7086-4a7d-9bef-621c477cc337",
  "sourceToolAssistantUUID": "237cea12-70db-4f3c-ab4c-c34aebf39946",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "072a3a1a-465c-4992-a530-3e78def2ac5a",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 74 · 2026-05-19T19:10:29.613Z_

<details><summary>↩ Tool result · `toolu_01Wkb7st9e32rfANBBRbc1HW`</summary>

```text
Web search results for query: "ICLR 2027 predicted submission deadline October 2026"

Links: [{"title":"2026 Dates and Deadlines","url":"https://iclr.cc/Conferences/2026/Dates"},{"title":"Key deadlines in AI and ML conferences | Yutori","url":"https://scouts.yutori.com/inbox/53e01f0f-2f7a-4f63-9b38-22358e5386ac"},{"title":"Year-Round Deadlines - Imranur Rahman","url":"https://imranur-rahman.github.io/deadlines/"},{"title":"AI & ML Conference Deadlines 2026–2027","url":"https://trybibby.com/conference-deadlines"},{"title":"International Conference on Learning Representations ICLR in August 2027 in Sydney","url":"https://waset.org/learning-representations-conference-in-august-2027-in-sydney"},{"title":"ICLR 2026","url":"https://iclr.cc/"},{"title":"AI Conference Deadlines","url":"https://mlciv.com/ai-deadlines/"},{"title":"When is ICLR 2026? Dates, Deadline & Location | ConferenceDeadlines.com","url":"https://www.conferencedeadlines.com/conference/iclr"},{"title":"ICLR 2026 Call for Papers","url":"https://iclr.cc/Conferences/2026/CallForPapers"},{"title":"AI Deadlines – AI Conference Call For Paper Deadlines","url":"http://aideadlines.org/"}]

Based on the search results, I was unable to find specific information about ICLR 2027's predicted submission deadline for October 2026. 

The search results show information about ICLR 2026 (which is currently happening) and some general deadline tracking websites, but they don't contain details about when ICLR 2027 submissions are expected to open or close.

One source notes that predictions for future conference deadlines are "based on previous year schedule," which suggests that ICLR 2027 deadlines would likely follow a similar timeline to previous years, but the exact dates for ICLR 2027 don't appear to have been officially announced or widely published yet.

To find the most accurate information about ICLR 2027 deadlines, I recommend:
1. Visiting the official ICLR website (iclr.cc) when the Call for Papers is announced
2. Checking conference deadline tracking sites like aideadlines.org or mlciv.com as they update with official information


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "3d89b21c-d4d3-4550-865f-9fa0bf5b9877",
  "isSidechain": true,
  "promptId": "504e2971-a17d-4553-9508-335bf1f3968f",
  "agentId": "ac3625b267e3eea76",
  "type": "user",
  "uuid": "2a919e88-767b-4ff6-adc3-17731b4e52db",
  "sourceToolAssistantUUID": "3d89b21c-d4d3-4550-865f-9fa0bf5b9877",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "072a3a1a-465c-4992-a530-3e78def2ac5a",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 75 · 2026-05-19T19:10:29.686Z_

<details><summary>↩ Tool result · `toolu_01TabD1kBaoZiSN5nZwBcMgS`</summary>

```text
Web search results for query: "ACL rolling review dates venues 2026 2027 ARR submission cycles"

Links: [{"title":"Dates and Venues – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/dates"},{"title":"aclrollingreview/dates.md at main · acl-org/aclrollingreview","url":"https://github.com/acl-org/aclrollingreview/blob/main/dates.md"},{"title":"ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/"},{"title":"AI Conference Deadlines","url":"https://mlciv.com/ai-deadlines/"},{"title":"Main Conference - ACL 2026","url":"https://2026.aclweb.org/calls/main_conference_papers/"},{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"Call for Main Conference Papers -","url":"https://2026.eacl.org/calls/papers/"},{"title":"ACL ARR | OpenReview","url":"https://openreview.net/group?id=aclweb.org%2FACL%2FARR"},{"title":"ACL ARR 2026 March | OpenReview","url":"https://openreview.net/group?id=aclweb.org%2FACL%2FARR%2F2026%2FMarch"},{"title":"How ARR works – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewing"}]

Based on the search results, here's what I found about ACL Rolling Review (ARR) dates, venues, and submission cycles for 2026-2027:

## ARR Review Schedule Changes

ARR switched from 8-week review cycles to 10-week cycles starting in May 2025. This means instead of 6 cycles a year there will generally be 5 cycles.

## Key Conference Commitment Deadlines for 2026-2027

For EMNLP 2026, the final ARR submission date is May 25, 2026 with a commitment date of August 2, 2026.

For AACL 2026, the final ARR submission date is May 25, 2026 with a commitment date of August 26, 2026.

For EACL 2027, the final ARR submission date is August 3, 2026 with a commitment date of October 11, 2026.

## Submission Options for ACL 2026

Papers may be submitted to the ARR 2025 October cycle and ARR 2026 January cycle for ACL 2026.

## Venues in 2026

ACL 2026 will take place July 2-7, 2026 in San Diego, CA, USA.

The official ARR website at aclrollingreview.org/dates contains the most comprehensive and up-to-date information on all submission cycles and venue commitment deadlines.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "eff9a638-c7a9-42ad-ac47-30ca1ccfe635",
  "isSidechain": true,
  "promptId": "504e2971-a17d-4553-9508-335bf1f3968f",
  "agentId": "ac3625b267e3eea76",
  "type": "user",
  "uuid": "7253a060-df04-4408-859d-f45603c699a3",
  "sourceToolAssistantUUID": "eff9a638-c7a9-42ad-ac47-30ca1ccfe635",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "072a3a1a-465c-4992-a530-3e78def2ac5a",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 76 · 2026-05-19T19:10:30.804Z_

<details><summary>↩ Tool result · `toolu_01AqmpeGSxgkwdUYUK2tTbBs`</summary>

```text
Web search results for query: "github "token tax" tokenization bias multilingual code implementation paper"

Links: [{"title":"(PDF) The Token Tax: Systematic Bias in Multilingual Tokenization","url":"https://www.researchgate.net/publication/395355055_The_Token_Tax_Systematic_Bias_in_Multilingual_Tokenization"},{"title":"Natural Language Processing Papers on X: \"The Token Tax: Systematic Bias in Multilingual Tokenization. https://t.co/XXFdvS3k4T\" / X","url":"https://x.com/HEI/status/1965438941974106394"},{"title":"The Token Tax: Systematic Bias in Multilingual Tokenization - ACL Anthology","url":"https://aclanthology.org/2026.africanlp-main.10/"},{"title":"[2509.05486] The Token Tax: Systematic Bias in Multilingual Tokenization","url":"https://arxiv.org/abs/2509.05486"},{"title":"The Token Tax: Systematic Bias in Multilingual Tokenization | AI Research Paper Details","url":"https://www.aimodels.fyi/papers/arxiv/token-tax-systematic-bias-multilingual-tokenization"},{"title":"The Token Tax: Systematic Bias in Multilingual Tokenization","url":"https://arxiv.org/html/2509.05486v1"},{"title":"Papers by Ada Zhang","url":"https://www.aimodels.fyi/author-profile/ada-zhang-05c78027-ae9f-4318-8d0a-f5a9d648e740"},{"title":"The Token Tax: Systematic Bias in Multilingual Tokenization","url":"https://chatpaper.com/ja/chatpaper/paper/186756"}]

I found search results for "The Token Tax: Systematic Bias in Multilingual Tokenization" paper. Here's what the research covers:

## Overview

The paper shows that tokenization inefficiency imposes structural disadvantages on morphologically complex, low-resource languages, inflating compute resources and depressing accuracy.

## Key Findings

The researchers evaluated 10 large language models (LLMs) on AfriMMLU (9,000 MCQA items; 5 subjects; 16 African languages) and found that fertility (tokens/word) reliably predicts accuracy, with higher fertility consistently predicting lower accuracy across all models and subjects.

Reasoning models (DeepSeek, o1) consistently outperform non-reasoning peers across high and low resource languages in the AfriMMLU dataset, narrowing accuracy gaps observed in prior generations.

## Economic Impact

A doubling in tokens results in quadrupled training cost and time, underscoring the token tax faced by many languages.

## Recommendations

The results motivate morphologically aware tokenization, fair pricing, and multilingual benchmarks for equitable natural language processing (NLP).

The paper was published in the Proceedings of the 7th Workshop on African Natural Language Processing (AfricaNLP 2026) and is available on arXiv (paper 2509.05486).


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "2d1cae09-3427-4c9b-a6ca-ece1c3e26b53",
  "isSidechain": true,
  "promptId": "504e2971-a17d-4553-9508-335bf1f3968f",
  "agentId": "ac3625b267e3eea76",
  "type": "user",
  "uuid": "417d99bc-6918-429d-b116-ad929def11a7",
  "sourceToolAssistantUUID": "2d1cae09-3427-4c9b-a6ca-ece1c3e26b53",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "072a3a1a-465c-4992-a530-3e78def2ac5a",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 77 · 2026-05-19T19:10:33.977Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01JL7P8PTLAqh4kESpqD88rF`</summary>

```json
{
  "query": "\"token tax\" tokenization github.com code repository arxiv 2509.05486"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "417d99bc-6918-429d-b116-ad929def11a7",
  "isSidechain": true,
  "agentId": "ac3625b267e3eea76",
  "requestId": "req_011CbCTR5LvDDXYwDgvZsWWh",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "0b8178a1-bfa9-4a2b-873f-745b80f960b9",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "072a3a1a-465c-4992-a530-3e78def2ac5a",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Q5JSNeb6bF5ohG5EXKvp4M",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3259,
      "cache_read_input_tokens": 32733,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3259,
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

_source line 78 · 2026-05-19T19:10:34.423Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01FwwpZU2yLniN6RdNeFqJz4`</summary>

```json
{
  "query": "NeurIPS 2026 workshop deadline submission dates"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0b8178a1-bfa9-4a2b-873f-745b80f960b9",
  "isSidechain": true,
  "agentId": "ac3625b267e3eea76",
  "requestId": "req_011CbCTR5LvDDXYwDgvZsWWh",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "ec1b6aa9-c05f-460a-a758-eac5e3d597ed",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "072a3a1a-465c-4992-a530-3e78def2ac5a",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Q5JSNeb6bF5ohG5EXKvp4M",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3259,
      "cache_read_input_tokens": 32733,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3259,
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

_source line 79 · 2026-05-19T19:10:35.012Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01UHpYMK4oLzJnXmjD8Amnaq`</summary>

```json
{
  "query": "multilingual NLP workshop EMNLP 2026 call for papers submission"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ec1b6aa9-c05f-460a-a758-eac5e3d597ed",
  "isSidechain": true,
  "agentId": "ac3625b267e3eea76",
  "requestId": "req_011CbCTR5LvDDXYwDgvZsWWh",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "a57f9d81-edd7-42e2-ab6a-7e826e737750",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "072a3a1a-465c-4992-a530-3e78def2ac5a",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Q5JSNeb6bF5ohG5EXKvp4M",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3259,
      "cache_read_input_tokens": 32733,
      "output_tokens": 168,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 3259
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 168,
          "cache_read_input_tokens": 32733,
          "cache_creation_input_tokens": 3259,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 3259,
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

_source line 80 · 2026-05-19T19:10:39.841Z_

<details><summary>↩ Tool result · `toolu_01FwwpZU2yLniN6RdNeFqJz4`</summary>

```text
Web search results for query: "NeurIPS 2026 workshop deadline submission dates"

Links: [{"title":"2026 Dates and Deadlines","url":"https://neurips.cc/Conferences/2026/Dates"},{"title":"NeurIPS 2026 Call for Workshops","url":"https://neurips.cc/Conferences/2026/CallForWorkshops"},{"title":"NeurIPS 2026","url":"https://neurips.cc/"},{"title":"Call for Papers 2026","url":"https://neurips.cc/Conferences/2026/CallForPapers"},{"title":"NeurIPS Conference on X: \"The NeurIPS 2026 submission site opening has been moved to April 15th. Note that all tracks (Main Submission, Evaluations &amp; Datasets, and Position Papers) share the same dates. The final submission deadlines remain unchanged: • Paper Abstracts: May 4th (AOE) • Full Papers:\" / X","url":"https://x.com/NeurIPSConf/status/2041303457554940336"},{"title":"Guidance for NeurIPS Workshop Proposals 2026","url":"https://neurips.cc/Conferences/2026/WorkshopsGuidance"},{"title":"NeurIPS 2026 Call For Competitions","url":"https://neurips.cc/Conferences/2026/CallForCompetitions"},{"title":"2026 Conference – NeurIPS Blog","url":"https://blog.neurips.cc/category/2026-conference/"},{"title":"Update NeurIPS 2025 and 2026 conference data · huggingface/ai-deadlines at 99f16a7","url":"https://huggingface.co/spaces/huggingface/ai-deadlines/commit/99f16a754ac0ed468034709b8cd393e594791a01"},{"title":"NeurIPS 2026 Call for Papers — Official Deadlines & Important Dates | PaperPilot","url":"https://www.getpaperpilot.com/deadlines/neurips-2026.html"}]

Here are the key submission dates for NeurIPS 2026 workshops:

**Workshop Application Open:** April 21, 2026, AoE (Anywhere on Earth)

**Workshop Application Deadline:** June 06, 2026, AoE

**Workshop Acceptance Notification:** July 11, 2026, AoE

**Suggested Submission Date for Workshop Contributions:** August 29, 2026, AoE

**Mandatory Accept/Reject Notification Date:** September 29, 2026, AoE

These dates are important for workshop organizers who want to propose and organize workshops at the conference. The Fortieth annual conference is held from December 6th through December 12th, 2026 at the International Convention Centre in Sydney, Australia.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ec1b6aa9-c05f-460a-a758-eac5e3d597ed",
  "isSidechain": true,
  "promptId": "504e2971-a17d-4553-9508-335bf1f3968f",
  "agentId": "ac3625b267e3eea76",
  "type": "user",
  "uuid": "dadcb67d-c0a7-46cc-afca-d9c9af7b7d88",
  "sourceToolAssistantUUID": "ec1b6aa9-c05f-460a-a758-eac5e3d597ed",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "072a3a1a-465c-4992-a530-3e78def2ac5a",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 81 · 2026-05-19T19:10:42.516Z_

<details><summary>↩ Tool result · `toolu_01JL7P8PTLAqh4kESpqD88rF`</summary>

```text
Web search results for query: ""token tax" tokenization github.com code repository arxiv 2509.05486"

Links: [{"title":"[2509.05486] The Token Tax: Systematic Bias in Multilingual Tokenization","url":"https://arxiv.org/abs/2509.05486"},{"title":"The Token Tax: Systematic Bias in Multilingual Tokenization | AI Research Paper Details","url":"https://www.aimodels.fyi/papers/arxiv/token-tax-systematic-bias-multilingual-tokenization"},{"title":"(PDF) The Token Tax: Systematic Bias in Multilingual Tokenization","url":"https://www.researchgate.net/publication/395355055_The_Token_Tax_Systematic_Bias_in_Multilingual_Tokenization"},{"title":"The Token Tax: Systematic Bias in Multilingual Tokenization Jessica M. Lundin","url":"https://arxiv.org/pdf/2509.05486"},{"title":"The Token Tax: Systematic Bias in Multilingual Tokenization","url":"https://arxiv.org/html/2509.05486"},{"title":"The Token Tax: Systematic Bias in Multilingual Tokenization - ACL Anthology","url":"https://aclanthology.org/2026.africanlp-main.10/"},{"title":"Tokenization Multiplicity Leads to Arbitrary Price Variation in LLM-as-a-service","url":"https://arxiv.org/pdf/2506.06446"},{"title":"Is Your LLM Overcharging You? Tokenization, Transparency, and Incentives","url":"https://arxiv.org/pdf/2505.21627"}]

Based on the search results, here's what I found about the "Token Tax" paper (arxiv 2509.05486):

## The Token Tax: Systematic Bias in Multilingual Tokenization

Tokenization inefficiency imposes structural disadvantages on morphologically complex, low-resource languages, inflating compute resources and depressing accuracy.

**Research Overview:**
The researchers evaluated 10 large language models (LLMs) on AfriMMLU (9,000 MCQA items; 5 subjects; 16 African languages) and showed that fertility (tokens/word) reliably predicts accuracy, with higher fertility consistently predicting lower accuracy across all models and subjects.

**Key Finding:**
A doubling in tokens results in quadrupled training cost and time, underscoring the token tax faced by many languages.

**Authors and Publication:**
The paper was authored by Jessica M. Lundin, Ada Zhang, Nihal Karim, Hamza Louzan, Guohao Wei, David Ifeoluwa Adelani, and Cody Carroll, and appears in the Proceedings of the 7th Workshop on African Natural Language Processing (AfricaNLP 2026).

**Recommendations:**
The results motivate morphologically aware tokenization, fair pricing, and multilingual benchmarks for equitable natural language processing.

The search results show the paper is available on arXiv and was submitted on September 5, 2025. However, I didn't find specific GitHub repository information in these results for the code repository you mentioned.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "0b8178a1-bfa9-4a2b-873f-745b80f960b9",
  "isSidechain": true,
  "promptId": "504e2971-a17d-4553-9508-335bf1f3968f",
  "agentId": "ac3625b267e3eea76",
  "type": "user",
  "uuid": "5e9d16fe-cb80-4c53-97fb-35b2caada0cf",
  "sourceToolAssistantUUID": "0b8178a1-bfa9-4a2b-873f-745b80f960b9",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "072a3a1a-465c-4992-a530-3e78def2ac5a",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 82 · 2026-05-19T19:10:43.234Z_

<details><summary>↩ Tool result · `toolu_01UHpYMK4oLzJnXmjD8Amnaq`</summary>

```text
Web search results for query: "multilingual NLP workshop EMNLP 2026 call for papers submission"

Links: [{"title":"Call for workshops: EMNLP & AACL","url":"https://groups.google.com/g/ml-news/c/W-fucfhVto4"},{"title":"Joint Call for Tutorial Proposals (EMNLP/AACL-IJCNLP 2026) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/joint-call-tutorial-proposals-emnlpaacl-ijcnlp-2026"},{"title":"LINGUIST List 37.972 Confs: 2026 Conference on Empirical Methods in Natural Language Processing (Hungary)","url":"https://linguistlist.org/issues/37/972/"},{"title":"EACL/ACL 2026 Joint Call for Workshops | ACL Member Portal","url":"https://www.aclweb.org/portal/content/eaclacl-2026-joint-call-workshops"},{"title":"Call for Main Conference Papers - EMNLP 2026","url":"https://2026.emnlp.org/calls/main_conference_papers/"},{"title":"BabyLM Turns 4 and Goes Multilingual: Call for Papers for the 2026 BabyLM Workshop","url":"https://arxiv.org/pdf/2602.20092"}]

Based on the search results, here's what I found regarding multilingual NLP workshops and EMNLP 2026:

## General Workshop Call for EMNLP 2026

The Association for Computational Linguistics invites proposals for workshops to be held in conjunction with AACL 2026 or EMNLP 2026, with electronic submission at https://softconf.com/p/acl-workshops2026/

The proposals should describe the ways your workshop will support diversity in NLP. This includes use of multilingual data and indications of how the described methods scale up to various languages.

## Specific Multilingual NLP Workshop: BabyLM 2026

One notable multilingual NLP workshop is the BabyLM workshop for 2026. The workshop features a new multilingual track focusing on English, Dutch, and Chinese, and calls for papers related to training efficiency, small-scale training datasets, cognitive modeling, model evaluation, and architecture innovation. The workshop encourages submissions on topics related to multilingual language acquisition and typological diversity.

If you're looking for a specific multilingual NLP workshop's call for papers, you may want to check the ACL workshops submission portal or contact the workshop organizers directly for detailed submission deadlines and requirements.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a57f9d81-edd7-42e2-ab6a-7e826e737750",
  "isSidechain": true,
  "promptId": "504e2971-a17d-4553-9508-335bf1f3968f",
  "agentId": "ac3625b267e3eea76",
  "type": "user",
  "uuid": "b4e11e0f-dcaa-4625-8907-0d0a8c4eb130",
  "sourceToolAssistantUUID": "a57f9d81-edd7-42e2-ab6a-7e826e737750",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "072a3a1a-465c-4992-a530-3e78def2ac5a",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 83 · 2026-05-19T19:10:45.953Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01XdADz45dsbh1QcyfzE99s1`</summary>

```json
{
  "query": "WMT 2026 paper submission deadline date research papers"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b4e11e0f-dcaa-4625-8907-0d0a8c4eb130",
  "isSidechain": true,
  "agentId": "ac3625b267e3eea76",
  "requestId": "req_011CbCTRzT23F6sNdwhxhWoX",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "f7cfbf49-7867-43d1-9a48-1cb0f0b87933",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "072a3a1a-465c-4992-a530-3e78def2ac5a",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017Zfv16gm1mzb969BeLgWhw",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2386,
      "cache_read_input_tokens": 35992,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2386,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 48,
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

_source line 84 · 2026-05-19T19:10:46.137Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Y9vqj8CXQ18UbJT3s9FVc1`</summary>

```json
{
  "query": "ICLR 2026 submission deadline date abstract full paper"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f7cfbf49-7867-43d1-9a48-1cb0f0b87933",
  "isSidechain": true,
  "agentId": "ac3625b267e3eea76",
  "requestId": "req_011CbCTRzT23F6sNdwhxhWoX",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "e7af932d-8d3c-4ec5-b3d3-0db43c07948e",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "072a3a1a-465c-4992-a530-3e78def2ac5a",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017Zfv16gm1mzb969BeLgWhw",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2386,
      "cache_read_input_tokens": 35992,
      "output_tokens": 112,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2386
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 112,
          "cache_read_input_tokens": 35992,
          "cache_creation_input_tokens": 2386,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2386,
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

_source line 85 · 2026-05-19T19:10:50.998Z_

<details><summary>↩ Tool result · `toolu_01Y9vqj8CXQ18UbJT3s9FVc1`</summary>

```text
Web search results for query: "ICLR 2026 submission deadline date abstract full paper"

Links: [{"title":"2026 Dates and Deadlines","url":"https://iclr.cc/Conferences/2026/Dates"},{"title":"ICLR 2026 Call for Papers","url":"https://iclr.cc/Conferences/2026/CallForPapers"},{"title":"ICLR 2026 Author Guide","url":"https://iclr.cc/Conferences/2026/AuthorGuide"},{"title":"ICLR 2026 in Brazil– Deadlines, Venue, Dates, and Call for Papers","url":"https://conferenceinc.net/post/iclr-2026-conference/"},{"title":"ICLR 2026 Conference | OpenReview","url":"https://openreview.net/group?id=ICLR.cc%2F2026%2FConference"},{"title":"When is ICLR 2026? Dates, Deadline & Location | ConferenceDeadlines.com","url":"https://www.conferencedeadlines.com/conference/iclr"},{"title":"ICML 2026 Peer Review FAQ","url":"https://icml.cc/Conferences/2026/PeerReviewFAQ"},{"title":"2025 Dates and Deadlines","url":"https://iclr.cc/Conferences/2025/Dates"},{"title":"ICML 2026 Call for Papers","url":"https://icml.cc/Conferences/2026/CallForPapers"},{"title":"about | ICLR Blogposts 2026","url":"https://iclr-blogposts.github.io/2026/about/"}]

Based on the search results, I found information about ICLR 2026 submission deadlines:

Abstract submission is mandatory, and without an abstract, you cannot submit a full paper. In OpenReview, only the "Abstract" section is mandatory, and you can upload the full paper in the "PDF" section anytime before the deadline.

However, the specific deadline dates are not clearly displayed in the search results I retrieved. The blogposts track mentions December 7th, 2025 as the abstract and submission deadline, but this appears to be for the ICLR 2026 blogposts track specifically, not the main conference.

For the exact ICLR 2026 main conference submission deadlines for abstracts and full papers, I recommend checking the official ICLR 2026 Call for Papers page at iclr.cc/Conferences/2026/CallForPapers or the ICLR 2026 Dates and Deadlines page directly, as they should contain the precise deadline information.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "e7af932d-8d3c-4ec5-b3d3-0db43c07948e",
  "isSidechain": true,
  "promptId": "504e2971-a17d-4553-9508-335bf1f3968f",
  "agentId": "ac3625b267e3eea76",
  "type": "user",
  "uuid": "48695bcd-8e64-4e08-82e9-b9a639236906",
  "sourceToolAssistantUUID": "e7af932d-8d3c-4ec5-b3d3-0db43c07948e",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "072a3a1a-465c-4992-a530-3e78def2ac5a",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 86 · 2026-05-19T19:10:51.407Z_

<details><summary>↩ Tool result · `toolu_01XdADz45dsbh1QcyfzE99s1`</summary>

```text
Web search results for query: "WMT 2026 paper submission deadline date research papers"

Links: [{"title":"WMT 2026","url":"https://www2.statmt.org/wmt26/index.html"},{"title":"WMT 2026 Shared Task on Automated Translation Quality Evaluation Systems | ACL Member Portal","url":"https://www.aclweb.org/portal/content/wmt-2026-shared-task-automated-translation-quality-evaluation-systems"},{"title":"Model Compression Shared Task @ WMT 2026 - First Call for Participation - Corpora - ELRA lists","url":"https://list.elra.info/mailman3/hyperkitty/list/corpora@list.elra.info/thread/QFBE3PYYAXYI2R5FBJZQOKXWC7CCJ6GD/"},{"title":"WMT 2025","url":"https://www2.statmt.org/wmt25/"},{"title":"WMT: Workshop on Machine Translation - Google Groups","url":"https://groups.google.com/g/wmt-tasks"},{"title":"WMT26 | Machine Translate","url":"https://machinetranslate.org/wmt26"},{"title":"Dates and Venues","url":"http://aclrollingreview.org/dates"},{"title":"Model Compression Shared Task @ WMT 2026 | ACL Member Portal","url":"https://www.aclweb.org/portal/content/model-compression-shared-task-wmt-2026"},{"title":"WMS 2026 abstract submission deadline","url":"https://www.instagram.com/p/DW0_gbjAeM8/"},{"title":"2026 Abstract submission guidelines - WMS 2026","url":"https://www.wms2026.com/page/2026-abstract-submission-guidelines"}]

Based on the search results, I found information about WMT 2026 research paper submission details. However, the specific paper submission deadline date is not explicitly listed on the main WMT 2026 page. 

According to the search results, the WMT paper submission deadline is "TBA (follows EMNLP)". This means the exact deadline has not yet been announced and will follow the timeline of EMNLP 2026 (the parent conference being held in Budapest, Hungary in November 2026).

Research papers are submitted electronically via SoftConf and should follow EMNLP formatting guidelines. Additionally, WMT participates in the ACL Rolling Review, which is an alternative submission pathway for research papers.

For the most current and specific paper submission deadline, you would need to check the official WMT 2026 website directly at https://www2.statmt.org/wmt26/ as the deadline information will be finalized and announced closer to the submission period.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f7cfbf49-7867-43d1-9a48-1cb0f0b87933",
  "isSidechain": true,
  "promptId": "504e2971-a17d-4553-9508-335bf1f3968f",
  "agentId": "ac3625b267e3eea76",
  "type": "user",
  "uuid": "1aa16c70-b923-44d0-87fb-96468ea10913",
  "sourceToolAssistantUUID": "f7cfbf49-7867-43d1-9a48-1cb0f0b87933",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "072a3a1a-465c-4992-a530-3e78def2ac5a",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 87 · 2026-05-19T19:11:48.564Z_

Now I have all the information needed to compile a comprehensive report. Here is my findings:

---

## 1. Conference/Workshop Deadlines AFTER May 19, 2026

### Confirmed Deadlines After May 19, 2026

**EMNLP 2026** (Budapest, Hungary, Oct 24-29, 2026)
- ARR Submission Deadline: **May 25, 2026**
- Commitment Deadline: **August 2, 2026**
- Source: [EMNLP 2026 CFP](https://2026.emnlp.org/calls/main_conference_papers/)

**EACL 2027** (Athens, Greece, Mar 9-14, 2027)
- ARR Submission Deadline: **August 3, 2026**
- Commitment Deadline: **October 11, 2026**
- Source: [EACL 2027 CFP](https://2027.eacl.org/calls/papers/), [ARR Dates](http://aclrollingreview.org/dates)

**WMT 2026** (co-located with EMNLP 2026)
- Research paper submission: **TBA (follows EMNLP timeline)** -- likely aligns with the EMNLP ARR May 25 cycle or later
- Shared task deadlines: Model Compression submission **July 2, 2026**; Quality Evaluation challenge set **July 16, 2026**; Test data release **July 23, 2026**
- Source: [WMT 2026](https://www2.statmt.org/wmt26/index.html)

**NeurIPS 2026 Workshops** (Sydney, Australia, Dec 6-12, 2026)
- Workshop application deadline: **June 6, 2026**
- Suggested workshop paper submission date: **August 29, 2026**
- Mandatory accept/reject notification: **September 29, 2026**
- Source: [NeurIPS 2026 Dates](https://neurips.cc/Conferences/2026/Dates)

**ICLR 2027** (predicted ~Apr 2027)
- Not yet announced. Based on ICLR 2026 patterns (abstract ~Oct 1, full paper ~Oct 8), the ICLR 2027 deadline would likely be around **October 2026** -- but this is an estimate only, no official dates exist yet.
- Source: [ICLR Conferences](https://iclr.cc/)

**AACL 2026**
- Final ARR submission: **May 25, 2026** (same cycle as EMNLP)
- Commitment deadline: **August 26, 2026**
- Source: [ARR Dates](http://aclrollingreview.org/dates)

### Deadlines ALREADY PASSED (Before May 19, 2026)

**ACL 2026** (San Diego, CA, Jul 2-7, 2026)
- ARR cycles: Oct 2025 and Jan 2026 (both passed)
- Commitment deadline: **March 14, 2026** (PASSED)
- Industry Track: **February 14, 2026** (PASSED)
- Source: [ACL 2026](https://2026.aclweb.org/)

**NeurIPS 2026 Main Track** (Sydney, Dec 6-12, 2026)
- Abstract deadline: **May 4, 2026** (PASSED)
- Full paper deadline: **May 6, 2026** (PASSED)
- Source: [NeurIPS 2026 CFP](https://neurips.cc/Conferences/2026/CallForPapers)

**ICML 2026** (Seoul, Jul 6-11, 2026)
- Abstract: **Jan 24, 2026** (PASSED)
- Full paper: **Jan 29, 2026** (PASSED)
- Source: [ICML 2026 CFP](https://icml.cc/Conferences/2026/CallForPapers)

**EACL 2026** (Rabat, Morocco, Mar 24-29, 2026)
- ARR submission: **Oct 6, 2025** (PASSED)
- Commitment: **Dec 14, 2025** (PASSED)
- Source: [EACL 2026](https://2026.eacl.org/calls/papers/)

**LREC 2026** (Palma, Spain, May 11-16, 2026)
- Submission: **Oct 24, 2025** (PASSED)
- Source: [LREC 2026](https://lrec2026.info/calls/)

**NAACL 2026** (Albuquerque, USA)
- Commitment deadline: **March 14, 2026** (PASSED, same as ACL 2026)
- Source: [ARR Dates](http://aclrollingreview.org/dates)

**AfricaNLP 2026** (co-located with EACL 2026)
- Direct submission: **Dec 22, 2025** (PASSED)
- Source: [AfricaNLP 2026](https://sites.google.com/view/africanlp2026)

**COLING 2026 / AfricaNLP 2027**: No confirmed dates found. COLING runs biennially (2025 was the last), so COLING 2027 may be next. AfricaNLP 2027 has not been announced.

### Relevant Multilingual NLP Workshops (2026-2027)

- **BabyLM 2026 Workshop** -- new multilingual track (English, Dutch, Chinese). Deadline details not fully confirmed but expected to be co-located with a major 2026 conference.
- **AbjadNLP 2026** -- Workshop on NLP for Languages Using Arabic Script. Source: [AbjadNLP 2026](https://wp.lancs.ac.uk/abjad/)
- NeurIPS 2026 workshops (multilingual/fairness-focused) -- workshop proposals due **June 6, 2026**; individual paper submissions likely ~**August 29, 2026**.

---

## 2. Existing Implementations on GitHub

### "Token Tax Multilingual" Implementation
- **Paper**: "The Token Tax: Systematic Bias in Multilingual Tokenization" (Lundin, Zhang, Karim, Louzan, Wei, Adelani, Carroll). Published at AfricaNLP 2026. arXiv: [2509.05486](https://arxiv.org/abs/2509.05486)
- **No public GitHub repo found** for this specific paper's code. The paper evaluated 10 LLMs on AfriMMLU but no linked code repository was discovered.
- **Related**: [remeinium/WWHO](https://github.com/remeinium/WWHO) -- a tokenization architecture addressing the "Token Tax" for Indic/SE Asian scripts.

### "Causal Mediation Analysis NLP" Code
- **Repository**: [sebastianGehrmann/CausalMediationAnalysis](https://github.com/sebastianGehrmann/CausalMediationAnalysis)
- Implements causal mediation analysis for interpreting neural NLP models, specifically studying gender bias in Transformers. Includes attention intervention experiments on Winobias and Winogender datasets. This is directly reusable for adapting causal mediation analysis to tokenization/multilingual settings.

### "Tokenization Fertility" Measurement Code
- **Qtok Framework**: [nup-csai/Qtok](https://github.com/nup-csai/Qtok/) -- comprehensive framework for evaluating multilingual tokenizer quality in LLMs. Includes fertility metrics, language coverage, token completeness, and distribution analysis across languages. Directly applicable for measuring tokenization fertility.
- **Related papers**: "Beyond Fertility: Analyzing STRR" proposes Single Token Retention Rate as an alternative/complement to fertility. "The Script Tax" (arXiv: 2602.11174) measures tokenization-driven efficiency disparities.

### "AfriMMLU" Evaluation Code
- **Repository**: [masakhane-io/masakhane-nlu](https://github.com/masakhane-io/masakhane-nlu) -- contains AfriMMLU as part of IrokoBench (benchmark for 16 African languages covering AfriXNLI, AfriMGSM, and AfriMMLU).
- **Dataset**: [masakhane/afrimmlu on HuggingFace](https://huggingface.co/datasets/masakhane/afrimmlu)
- **Related**: [The-African-Research-Collective/afrobench-eval-suite](https://github.com/The-African-Research-Collective/afrobench-eval-suite) -- LLM eval leaderboard for African languages. [McGill-NLP/AfroBench](https://github.com/McGill-NLP/AfroBench) -- evaluates LLMs across 64 African languages, 15 tasks, 22 datasets.
- Integration with [EleutherAI/lm-evaluation-harness](https://github.com/EleutherAI/lm-evaluation-harness/pull/2042) (IrokoBench PR).

### "Regression Discontinuity Tokenization" Code
- **Repository**: [pietrolesci/tokenisation-bias](https://github.com/pietrolesci/tokenisation-bias) -- implements regression discontinuity design for estimating causal tokenisation bias. Published at ACL 2025 ("Causal Estimation of Tokenisation Bias"). Exploits BPE vocabulary cutoff as a natural experiment. Found BPE bias of ~2.88 nats (~17x probability difference). Directly relevant and reusable.

### "Selective Translation Multilingual" Code
- **No directly matching repository found.** General multilingual translation repos exist:
  - [DevSinghSachan/multilingual_nmt](https://github.com/DevSinghSachan/multilingual_nmt) -- Transformer-based multilingual NMT
  - [aboSamoor/polyglot](https://github.com/aboSamoor/polyglot) -- multilingual NLP toolkit
  - But none specifically implement "selective translation" as a technique.

---

## Summary of Actionable Deadlines (After May 19, 2026)

| Venue | Deadline | Date |
|-------|----------|------|
| EMNLP 2026 | ARR Submission | May 25, 2026 |
| EMNLP 2026 | Commitment | Aug 2, 2026 |
| AACL 2026 | Commitment | Aug 26, 2026 |
| EACL 2027 | ARR Submission | Aug 3, 2026 |
| EACL 2027 | Commitment | Oct 11, 2026 |
| WMT 2026 | Shared task submissions | Jul 2-23, 2026 |
| WMT 2026 | Research papers | TBA (follows EMNLP) |
| NeurIPS 2026 | Workshop proposals | Jun 6, 2026 |
| NeurIPS 2026 | Workshop papers | ~Aug 29, 2026 |
| ICLR 2027 | Estimated submission | ~Oct 2026 (unannounced) |

The most immediate deadline is **EMNLP 2026 ARR on May 25, 2026** (6 days from now).

Sources:
- [EMNLP 2026 Call for Papers](https://2026.emnlp.org/calls/main_conference_papers/)
- [ACL Rolling Review Dates & Venues](http://aclrollingreview.org/dates)
- [EACL 2027](https://2027.eacl.org/)
- [NeurIPS 2026 Dates](https://neurips.cc/Conferences/2026/Dates)
- [WMT 2026](https://www2.statmt.org/wmt26/index.html)
- [ACL 2026](https://2026.aclweb.org/)
- [ICML 2026](https://icml.cc/Conferences/2026/CallForPapers)
- [LREC 2026](https://lrec2026.info/calls/)
- [ICLR Conferences](https://iclr.cc/)
- [AfricaNLP 2026](https://sites.google.com/view/africanlp2026)
- [sebastianGehrmann/CausalMediationAnalysis](https://github.com/sebastianGehrmann/CausalMediationAnalysis)
- [nup-csai/Qtok](https://github.com/nup-csai/Qtok/)
- [masakhane-io/masakhane-nlu](https://github.com/masakhane-io/masakhane-nlu)
- [pietrolesci/tokenisation-bias](https://github.com/pietrolesci/tokenisation-bias)
- [The-African-Research-Collective/afrobench-eval-suite](https://github.com/The-African-Research-Collective/afrobench-eval-suite)
- [The Token Tax paper (arXiv 2509.05486)](https://arxiv.org/abs/2509.05486)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1aa16c70-b923-44d0-87fb-96468ea10913",
  "isSidechain": true,
  "agentId": "ac3625b267e3eea76",
  "requestId": "req_011CbCTSbVRB8rvJnAKarAjx",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "2a8e9aa9-92a6-42fa-b665-fea54a96ed38",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "072a3a1a-465c-4992-a530-3e78def2ac5a",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Hsc74a1JgRkCNgD2muo6k5",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 704,
      "cache_creation_input_tokens": 846,
      "cache_read_input_tokens": 38378,
      "output_tokens": 3332,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 846
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 704,
          "output_tokens": 3332,
          "cache_read_input_tokens": 38378,
          "cache_creation_input_tokens": 846,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 846,
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
