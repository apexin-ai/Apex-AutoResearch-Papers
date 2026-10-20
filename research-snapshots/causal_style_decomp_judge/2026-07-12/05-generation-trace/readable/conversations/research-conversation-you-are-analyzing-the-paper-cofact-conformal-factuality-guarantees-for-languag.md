# Research conversation: You are analyzing the paper "CoFact: Conformal Factuality Guarantees for Language Models under Covariate Shift" by Zirui

**The Likert Blindspot: Measurement-Mode Divergence in LLM Judge Style Evaluation (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 45
- **Recorded user turns:** 3
- **Tool calls:** 16
- **Original source:** `logs/chats/exported-trajectories/account-2/agent-add601a9ad7ccf96b.jsonl`
- **Structured JSON:** [`0402aa28edcbf338ad5e.json`](../../sessions/04/0402aa28edcbf338ad5e.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

37 recorded events

### User

_source line 1 · 2026-05-30T06:25:12.066Z_

You are analyzing the paper "CoFact: Conformal Factuality Guarantees for Language Models under Covariate Shift" by Zirui Hu, Zheng Zhang, Yingjie Wang, Leszek Rutkowski, Dacheng Tao (ICLR 2026). URL: https://openreview.net/forum?id=eiBp7rsc3K

Your task:
1. Use WebFetch to read the paper's abstract, introduction, and method details from the OpenReview page
2. Use WebSearch to find any additional information about the paper
3. IMPORTANT: Since this is on OpenReview, also look for and read reviewer comments. Search for "CoFact conformal factuality covariate shift ICLR 2026 reviews" or fetch the OpenReview page to find reviewer feedback.
4. Focus on: What gap did they identify? What was the key insight? How did they formulate the problem? What techniques did they adapt/combine? What did reviewers praise/criticize?

Provide a detailed but concise summary covering:
- Problem identification (what gap, how found)
- Key insight (core intellectual contribution)
- Innovation type
- Method summary (technical approach)
- Reviewer feedback summary (if available)
- Limitations and open questions
- Building blocks (reusable methods/tools/datasets)
- Relevance to conformal prediction for RAG under adversarial poisoning

Keep your response under 1500 words.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "bfbb75dd-55f4-4449-8327-dd488e005f06",
  "agentId": "add601a9ad7ccf96b",
  "type": "user",
  "uuid": "8f254db6-dfbe-4295-9d0b-222f9e3f6df2",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "92f38cdd-b3e1-453a-8457-65dd6c27cbfd",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 2 · 2026-05-30T06:25:12.076Z_

```json
{
  "parentUuid": "8f254db6-dfbe-4295-9d0b-222f9e3f6df2",
  "isSidechain": true,
  "agentId": "add601a9ad7ccf96b",
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
  "uuid": "90756b22-183b-425b-a6ef-65d0a5e77b24",
  "timestamp": "2026-05-30T06:25:12.076Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "92f38cdd-b3e1-453a-8457-65dd6c27cbfd",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 3 · 2026-05-30T06:25:12.084Z_

```json
{
  "parentUuid": "90756b22-183b-425b-a6ef-65d0a5e77b24",
  "isSidechain": true,
  "agentId": "add601a9ad7ccf96b",
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "c398b5ef-5b0c-4044-a1ab-d5dc99d3b1de",
  "timestamp": "2026-05-30T06:25:12.084Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "92f38cdd-b3e1-453a-8457-65dd6c27cbfd",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Assistant

_source line 4 · 2026-05-30T06:25:14.711Z_



I'll fetch the paper details and search for additional information in parallel.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c398b5ef-5b0c-4044-a1ab-d5dc99d3b1de",
  "isSidechain": true,
  "agentId": "add601a9ad7ccf96b",
  "requestId": "req_011CbYGxHmCH7WPMgiWV4wVp",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "999b5bcd-5c67-4511-bcb1-e703093af07a",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "92f38cdd-b3e1-453a-8457-65dd6c27cbfd",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NrTof2jQmzcmu1Y3QUucEw",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1685,
      "cache_read_input_tokens": 7413,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1685,
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

_source line 5 · 2026-05-30T06:25:15.109Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_018WUmh7K2nxHiz7dywErWEX`</summary>

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
  "parentUuid": "999b5bcd-5c67-4511-bcb1-e703093af07a",
  "isSidechain": true,
  "agentId": "add601a9ad7ccf96b",
  "requestId": "req_011CbYGxHmCH7WPMgiWV4wVp",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "0012fbec-2f9a-42f6-85bc-c779c499d233",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "92f38cdd-b3e1-453a-8457-65dd6c27cbfd",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NrTof2jQmzcmu1Y3QUucEw",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1685,
      "cache_read_input_tokens": 7413,
      "output_tokens": 95,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1685
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 95,
          "cache_read_input_tokens": 7413,
          "cache_creation_input_tokens": 1685,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1685,
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

_source line 6 · 2026-05-30T06:25:15.117Z_

<details><summary>↩ Tool result · `toolu_018WUmh7K2nxHiz7dywErWEX`</summary>

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
  "parentUuid": "0012fbec-2f9a-42f6-85bc-c779c499d233",
  "isSidechain": true,
  "promptId": "bfbb75dd-55f4-4449-8327-dd488e005f06",
  "agentId": "add601a9ad7ccf96b",
  "type": "user",
  "uuid": "b9e15450-ac4b-4925-949b-7f891f30e836",
  "sourceToolAssistantUUID": "0012fbec-2f9a-42f6-85bc-c779c499d233",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "92f38cdd-b3e1-453a-8457-65dd6c27cbfd",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 7 · 2026-05-30T06:25:17.775Z_



Now let me fetch the paper page and search for reviews in parallel.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b9e15450-ac4b-4925-949b-7f891f30e836",
  "isSidechain": true,
  "agentId": "add601a9ad7ccf96b",
  "requestId": "req_011CbYGxWVfmF6vJJmyJPuVQ",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "f67e227a-75c6-464c-ad0b-fac38092481f",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "92f38cdd-b3e1-453a-8457-65dd6c27cbfd",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MbfdjXn3Em1rmUnPtZ8GPQ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1117,
      "cache_read_input_tokens": 9098,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1117,
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

_source line 8 · 2026-05-30T06:25:20.680Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01Ewn3MGtZkGUJ6J3eryRoWK`</summary>

```json
{
  "url": "https://openreview.net/forum?id=eiBp7rsc3K",
  "prompt": "Extract the full abstract, introduction summary, method details, key contributions, and any reviewer comments/scores. Include reviewer IDs, ratings, confidence scores, and their main criticisms and praises. Also extract any information about the technical approach, problem formulation, datasets used, and results."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f67e227a-75c6-464c-ad0b-fac38092481f",
  "isSidechain": true,
  "agentId": "add601a9ad7ccf96b",
  "requestId": "req_011CbYGxWVfmF6vJJmyJPuVQ",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "92913a34-f4f8-4543-a58c-2ddf7e1442e5",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "92f38cdd-b3e1-453a-8457-65dd6c27cbfd",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MbfdjXn3Em1rmUnPtZ8GPQ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1117,
      "cache_read_input_tokens": 9098,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1117,
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

_source line 9 · 2026-05-30T06:25:21.626Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_011dbYYy5xYNo2PeFt7HJNhE`</summary>

```json
{
  "query": "CoFact conformal factuality covariate shift ICLR 2026 reviews"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "92913a34-f4f8-4543-a58c-2ddf7e1442e5",
  "isSidechain": true,
  "agentId": "add601a9ad7ccf96b",
  "requestId": "req_011CbYGxWVfmF6vJJmyJPuVQ",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "c3c9696d-ba48-4630-8bdd-01687eea7f09",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "92f38cdd-b3e1-453a-8457-65dd6c27cbfd",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MbfdjXn3Em1rmUnPtZ8GPQ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1117,
      "cache_read_input_tokens": 9098,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1117,
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

_source line 10 · 2026-05-30T06:25:22.016Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01TrBZN6ibLfmwWcJbtX1nde`</summary>

```json
{
  "query": "\"CoFact\" conformal prediction language models factuality guarantees paper"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c3c9696d-ba48-4630-8bdd-01687eea7f09",
  "isSidechain": true,
  "agentId": "add601a9ad7ccf96b",
  "requestId": "req_011CbYGxWVfmF6vJJmyJPuVQ",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "683e6437-8105-4786-9f4b-02262cc19cdc",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "92f38cdd-b3e1-453a-8457-65dd6c27cbfd",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MbfdjXn3Em1rmUnPtZ8GPQ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1117,
      "cache_read_input_tokens": 9098,
      "output_tokens": 265,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1117
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 265,
          "cache_read_input_tokens": 9098,
          "cache_creation_input_tokens": 1117,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1117,
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

_source line 11 · 2026-05-30T06:25:24.438Z_

<details><summary>↩ Tool result · `toolu_01Ewn3MGtZkGUJ6J3eryRoWK`</summary>

```text
# CoFact Research Paper Summary

## Full Abstract
"Large Language Models (LLMs) excel in natural language processing (NLP) tasks but often generate false or misleading information, known as hallucinations, raising reliability concerns in high-stakes applications." The paper introduces CoFact, which "uses online density ratio estimation to adaptively reweigh calibration data, ensuring alignment with evolving test distributions." The framework "provides robust factuality guarantees under non-stationary conditions" and establishes theoretical bounds showing the hallucination rate gap "asymptotically approaches zero as the number of rounds and calibration samples increase."

## Key Contributions
1. **Novel Framework**: CoFact adapts conformal prediction for dynamic environments by incorporating online density ratio estimation
2. **Theoretical Guarantees**: Establishes upper bounds on hallucination rate gaps under covariate shift
3. **New Benchmark**: Introduces "WildChat+" dataset capturing real-world covariate shifts
4. **Empirical Validation**: Demonstrates superior performance across MedLFQA, WikiData, and WildChat+

## Technical Approach
The method addresses the critical limitation that existing conformal prediction techniques "rely heavily on the exchangeability assumption between calibration and test data, which is frequently violated in real-world scenarios with dynamic covariate shifts."

## Datasets & Evaluation
- MedLFQA
- WikiData
- WildChat+ (newly introduced)

**Note**: The provided content lacks reviewer comments, scores, confidence ratings, introduction details, and detailed method descriptions beyond what appears in the abstract.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "92913a34-f4f8-4543-a58c-2ddf7e1442e5",
  "isSidechain": true,
  "promptId": "bfbb75dd-55f4-4449-8327-dd488e005f06",
  "agentId": "add601a9ad7ccf96b",
  "type": "user",
  "uuid": "3a14016a-023d-4101-82f8-efe71626d7e7",
  "sourceToolAssistantUUID": "92913a34-f4f8-4543-a58c-2ddf7e1442e5",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "92f38cdd-b3e1-453a-8457-65dd6c27cbfd",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-30T06:25:28.519Z_

<details><summary>↩ Tool result · `toolu_011dbYYy5xYNo2PeFt7HJNhE`</summary>

```text
Web search results for query: "CoFact conformal factuality covariate shift ICLR 2026 reviews"

Links: [{"title":"CoFact: Conformal Factuality Guarantees for Language Models under Covariate Shift [Quick Review]","url":"https://liner.com/review/cofact-conformal-factuality-guarantees-for-language-models-under-covariate-shift"},{"title":"Published as a conference paper at ICLR 2026 COFACT:","url":"https://openreview.net/pdf/6159b2dd5bd91fef13df0ada79e3e44611975257.pdf"},{"title":"CoFact: Conformal Factuality Guarantees for Language Models under Covariate Shift | OpenReview","url":"https://openreview.net/forum?id=eiBp7rsc3K"},{"title":"ICLR Poster CoFact: Conformal Factuality Guarantees for Language Models under Covariate Shift","url":"https://iclr.cc/virtual/2026/poster/10008295"},{"title":"Responsible AI Weekly — May 10, 2026 - by Hamid Bagheri","url":"https://airesponsibly.substack.com/p/responsible-ai-weekly-may-10-2026"},{"title":"Published as a conference paper at ICLR 2025 CONFORMAL LANGUAGE MODEL REASONING","url":"https://openreview.net/pdf?id=AJpUZd8Clb"}]

Based on the search results, here's what I found about CoFact:

## Overview

CoFact is a conformal prediction framework that provides statistical guarantees against hallucinations in LLM outputs even when user queries shift over time. The paper was published at ICLR in April 2026.

## Problem Addressed

Existing conformal prediction methods rely heavily on the exchangeability assumption between calibration and test data, which is frequently violated in real-world scenarios with dynamic covariate shifts. Most current safety and factuality guarantees fail once user behavior changes over time, which is exactly what happens in production systems.

## Approach

CoFact uses online density ratio estimation to adaptively reweigh calibration data, ensuring alignment with evolving test distributions. CoFact adaptively reweighs calibration data by dynamically activating and updating multiple expert models across different time intervals, bypassing the exchangeability assumption.

## Results

CoFact consistently maintains factuality closest to the target level of 0.9 on real-world datasets with dynamic covariate shifts, significantly outperforming standard conformal prediction (SCP) and conditional conformal prediction (CondCP).

## Datasets

CoFact is evaluated on MedLFQA, WikiData, and the newly introduced WildChat+ dataset, which captures real-world covariate shifts through user-generated prompts.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c3c9696d-ba48-4630-8bdd-01687eea7f09",
  "isSidechain": true,
  "promptId": "bfbb75dd-55f4-4449-8327-dd488e005f06",
  "agentId": "add601a9ad7ccf96b",
  "type": "user",
  "uuid": "af81fc8f-3c79-46d4-b746-63d52fee12ec",
  "sourceToolAssistantUUID": "c3c9696d-ba48-4630-8bdd-01687eea7f09",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "92f38cdd-b3e1-453a-8457-65dd6c27cbfd",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 13 · 2026-05-30T06:25:33.840Z_

<details><summary>↩ Tool result · `toolu_01TrBZN6ibLfmwWcJbtX1nde`</summary>

```text
Web search results for query: ""CoFact" conformal prediction language models factuality guarantees paper"

Links: [{"title":"CoFact: Conformal Factuality Guarantees for Language Models under Covariate Shift | OpenReview","url":"https://openreview.net/forum?id=eiBp7rsc3K"},{"title":"ICLR Poster CoFact: Conformal Factuality Guarantees for Language Models under Covariate Shift","url":"https://iclr.cc/virtual/2026/poster/10008295"},{"title":"CoFact: Conformal Factuality Guarantees for Language Models under Covariate Shift [Quick Review]","url":"https://liner.com/review/cofact-conformal-factuality-guarantees-for-language-models-under-covariate-shift"},{"title":"Language Models with Conformal Factuality Guarantees","url":"https://arxiv.org/pdf/2402.10978"},{"title":"Language Models with Conformal Factuality Guarantees","url":"https://arxiv.org/html/2402.10978v1"},{"title":"[2402.10978] Language Models with Conformal Factuality Guarantees","url":"https://arxiv.org/abs/2402.10978"},{"title":"Language Models with Conformal Factuality Guarantees","url":"https://proceedings.mlr.press/v235/mohri24a.html"},{"title":"[PDF] Language Models with Conformal Factuality Guarantees | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Language-Models-with-Conformal-Factuality-Mohri-Hashimoto/2495700b4303512784fbdbfccc58c6c4f7771ac2"},{"title":"[2505.17126] Conformal Language Model Reasoning with Coherent Factuality","url":"https://arxiv.org/abs/2505.17126"}]

Based on the search results, I found information about CoFact and related conformal prediction work for language models:

## CoFact: Conformal Factuality Guarantees for Language Models under Covariate Shift

CoFact is a conformal prediction framework that uses online density ratio estimation to adaptively reweigh calibration data, ensuring alignment with evolving test distributions, and it bypasses the exchangeability requirement to provide robust factuality guarantees under non-stationary conditions.

**The Problem It Addresses:**
Existing conformal prediction techniques for factuality rely heavily on the exchangeability assumption between calibration and test data, which is frequently violated in real-world scenarios with dynamic covariate shifts.

**Key Approach:**
CoFact adaptively reweighs calibration data by dynamically activating and updating multiple expert models across different time intervals, bypassing the exchangeability assumption.

**Theoretical Guarantees:**
The research theoretically establishes an upper bound on the gap between the actual hallucination rate and the target level, which asymptotically approaches zero as the number of rounds and calibration samples increase.

**Empirical Results:**
Extensive experiments on MedLFQA, WikiData, and WildChat+ demonstrate CoFact consistently outperforms existing methods by maintaining factuality guarantees even under dynamic conditions.

The paper was presented at ICLR 2026, representing recent advances in making language model outputs more reliable under challenging real-world conditions with distributional shifts.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "683e6437-8105-4786-9f4b-02262cc19cdc",
  "isSidechain": true,
  "promptId": "bfbb75dd-55f4-4449-8327-dd488e005f06",
  "agentId": "add601a9ad7ccf96b",
  "type": "user",
  "uuid": "ad20cf98-0550-4e2b-acd7-4ae1f066b7a2",
  "sourceToolAssistantUUID": "683e6437-8105-4786-9f4b-02262cc19cdc",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "92f38cdd-b3e1-453a-8457-65dd6c27cbfd",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 14 · 2026-05-30T06:25:36.227Z_

Let me now fetch the PDF for more technical details and also try to get reviewer comments.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ad20cf98-0550-4e2b-acd7-4ae1f066b7a2",
  "isSidechain": true,
  "agentId": "add601a9ad7ccf96b",
  "requestId": "req_011CbYGytRoxGM9XR7XyiSah",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "d33c654f-40f4-4c4c-b1ef-a94ea1fa6e00",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "92f38cdd-b3e1-453a-8457-65dd6c27cbfd",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015q2TT4aa5mLZyXQLqDKRb7",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2228,
      "cache_read_input_tokens": 10215,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2228,
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

_source line 15 · 2026-05-30T06:25:41.035Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_016JidYQrNjKZQh6eHYKBAoB`</summary>

```json
{
  "url": "https://openreview.net/pdf/6159b2dd5bd91fef13df0ada79e3e44611975257.pdf",
  "prompt": "Extract detailed technical information about: 1) The problem formulation (how they define factuality, conformal prediction setup, covariate shift formulation), 2) The method details (density ratio estimation, expert models, how calibration scores are reweighed, the online update mechanism), 3) Theoretical results (what bounds they prove, key assumptions), 4) Experimental setup (baselines, metrics, datasets), 5) Key results and ablations, 6) Limitations acknowledged by the authors."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d33c654f-40f4-4c4c-b1ef-a94ea1fa6e00",
  "isSidechain": true,
  "agentId": "add601a9ad7ccf96b",
  "requestId": "req_011CbYGytRoxGM9XR7XyiSah",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "5ac25d3f-ee89-4575-912e-a7b9b44ed836",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "92f38cdd-b3e1-453a-8457-65dd6c27cbfd",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015q2TT4aa5mLZyXQLqDKRb7",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2228,
      "cache_read_input_tokens": 10215,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2228,
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

_source line 16 · 2026-05-30T06:25:41.309Z_

<details><summary>↩ Tool result · `toolu_016JidYQrNjKZQh6eHYKBAoB`</summary>

```text
The server returned HTTP 404 Not Found.

The response body was not retrieved. If this URL requires authentication, use an authenticated tool (e.g. `gh` for GitHub, or an MCP-provided fetch tool) instead of WebFetch.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "5ac25d3f-ee89-4575-912e-a7b9b44ed836",
  "isSidechain": true,
  "promptId": "bfbb75dd-55f4-4449-8327-dd488e005f06",
  "agentId": "add601a9ad7ccf96b",
  "type": "user",
  "uuid": "1037e332-e6c4-4a19-b537-fa57a06f3afc",
  "sourceToolAssistantUUID": "5ac25d3f-ee89-4575-912e-a7b9b44ed836",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "92f38cdd-b3e1-453a-8457-65dd6c27cbfd",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-30T06:25:43.362Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01RBC4jMkYYpksPBTMbLZ7iw`</summary>

```json
{
  "url": "https://openreview.net/forum?id=eiBp7rsc3K",
  "prompt": "Look specifically for REVIEWER COMMENTS, official reviews, ratings, and discussion. Extract all reviewer feedback including: reviewer IDs/names, ratings (scores out of 10), confidence levels, strengths listed, weaknesses listed, questions asked, and any author responses. Look for sections labeled \"Official Review\" or similar."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1037e332-e6c4-4a19-b537-fa57a06f3afc",
  "isSidechain": true,
  "agentId": "add601a9ad7ccf96b",
  "requestId": "req_011CbYGytRoxGM9XR7XyiSah",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "cd00d686-ebc3-40ee-ba72-85ca23d8f7fc",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "92f38cdd-b3e1-453a-8457-65dd6c27cbfd",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015q2TT4aa5mLZyXQLqDKRb7",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2228,
      "cache_read_input_tokens": 10215,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2228,
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

_source line 18 · 2026-05-30T06:25:44.503Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01EiAkbPxaRhHJVMqK19uwQ3`</summary>

```json
{
  "url": "https://liner.com/review/cofact-conformal-factuality-guarantees-for-language-models-under-covariate-shift",
  "prompt": "Extract any review analysis, strengths, weaknesses, key findings, and technical details about CoFact paper."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "cd00d686-ebc3-40ee-ba72-85ca23d8f7fc",
  "isSidechain": true,
  "agentId": "add601a9ad7ccf96b",
  "requestId": "req_011CbYGytRoxGM9XR7XyiSah",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "42efe4e8-9b87-47bf-9167-287a60c46315",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "92f38cdd-b3e1-453a-8457-65dd6c27cbfd",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015q2TT4aa5mLZyXQLqDKRb7",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2228,
      "cache_read_input_tokens": 10215,
      "output_tokens": 470,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2228
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 470,
          "cache_read_input_tokens": 10215,
          "cache_creation_input_tokens": 2228,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2228,
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

_source line 19 · 2026-05-30T06:25:48.146Z_

<details><summary>↩ Tool result · `toolu_01RBC4jMkYYpksPBTMbLZ7iw`</summary>

```text
# Review Status for CoFact Paper

Based on the provided content, **no reviewer comments, official reviews, or ratings are visible** in this excerpt from the OpenReview page.

The page displays:
- Paper metadata (title, authors, publication date)
- Abstract summarizing the work on conformal prediction for LLM factuality
- Keywords and submission details
- Links to supplementary materials and revisions

However, the actual reviewer feedback section—which would typically contain official reviews, scores, confidence levels, identified strengths/weaknesses, and author responses—is **not included** in the extracted content.

To access reviewer comments, you would likely need to:
1. View the full OpenReview page directly
2. Check the "Revisions" section linked on the page
3. Look for a dedicated "Reviews" or "Comments" tab on OpenReview
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "cd00d686-ebc3-40ee-ba72-85ca23d8f7fc",
  "isSidechain": true,
  "promptId": "bfbb75dd-55f4-4449-8327-dd488e005f06",
  "agentId": "add601a9ad7ccf96b",
  "type": "user",
  "uuid": "87fe6096-56bf-4f38-aad3-1bfdbfec21af",
  "sourceToolAssistantUUID": "cd00d686-ebc3-40ee-ba72-85ca23d8f7fc",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "92f38cdd-b3e1-453a-8457-65dd6c27cbfd",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-30T06:25:49.736Z_

<details><summary>↩ Tool result · `toolu_01EiAkbPxaRhHJVMqK19uwQ3`</summary>

```text
# CoFact: Conformal Factuality Guarantees Analysis

## Overview
CoFact addresses hallucinations in Large Language Models by introducing a conformal prediction framework that maintains factuality guarantees even when training and test data distributions differ.

## Key Problem
Traditional conformal prediction methods for LLM reliability assume exchangeability between calibration and test data—an assumption frequently violated in real-world scenarios with dynamic covariate shifts.

## Technical Approach
The method employs "online density ratio estimation to adaptively reweigh calibration data" across evolving distributions. Multiple expert models are dynamically activated across different time intervals to bypass the exchangeability requirement.

## Main Contributions
- Theoretical guarantee establishing that "the gap between actual hallucination rate and target level asymptotically approaches zero" as rounds and calibration samples increase
- WildChat+, a new dataset capturing real covariate shifts through user-generated prompts with factuality annotations
- Empirical validation across three datasets

## Key Findings
On WildChat+, CoFact maintains target factuality (0.9) after approximately 150 time steps, substantially outperforming standard conformal prediction and conditional conformal prediction baselines, which deteriorate under distribution shifts.

## Limitations
The method exhibits initial lag during the first 50 time steps, requiring a burn-in period before effectively adapting to new distribution shifts.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "42efe4e8-9b87-47bf-9167-287a60c46315",
  "isSidechain": true,
  "promptId": "bfbb75dd-55f4-4449-8327-dd488e005f06",
  "agentId": "add601a9ad7ccf96b",
  "type": "user",
  "uuid": "6316bc92-9a7b-4d37-bd2b-1f330de6052c",
  "sourceToolAssistantUUID": "42efe4e8-9b87-47bf-9167-287a60c46315",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "92f38cdd-b3e1-453a-8457-65dd6c27cbfd",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 21 · 2026-05-30T06:25:52.111Z_

Let me try to access the PDF via a different URL and search for reviewer feedback more specifically.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6316bc92-9a7b-4d37-bd2b-1f330de6052c",
  "isSidechain": true,
  "agentId": "add601a9ad7ccf96b",
  "requestId": "req_011CbYH14GRSD4cMkUA3wpE3",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "53ce0903-436d-47b0-b9a1-f85a9a4181f2",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "92f38cdd-b3e1-453a-8457-65dd6c27cbfd",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RBdJ8hsyBdqE5NYQv2PmLx",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1200,
      "cache_read_input_tokens": 12443,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1200,
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

_source line 22 · 2026-05-30T06:25:55.934Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01Pwx2TW4VQqgmiaSp2d3aCo`</summary>

```json
{
  "url": "https://openreview.net/pdf?id=eiBp7rsc3K",
  "prompt": "Extract the full technical details: 1) Problem formulation - how factuality is defined, conformal prediction setup with nonconformity scores, covariate shift definition, 2) Method - density ratio estimation technique, how experts are maintained and updated, the reweighting scheme, algorithm pseudocode summary, 3) Theoretical results - main theorems and their assumptions, convergence rates, 4) Experiments - baselines compared, metrics used, key quantitative results, 5) Limitations section, 6) Related work they build upon (especially Mohri & Hashimoto 2024, weighted conformal prediction)."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "53ce0903-436d-47b0-b9a1-f85a9a4181f2",
  "isSidechain": true,
  "agentId": "add601a9ad7ccf96b",
  "requestId": "req_011CbYH14GRSD4cMkUA3wpE3",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "472258db-3f85-4ea9-997b-9db0a1bf5247",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "92f38cdd-b3e1-453a-8457-65dd6c27cbfd",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RBdJ8hsyBdqE5NYQv2PmLx",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1200,
      "cache_read_input_tokens": 12443,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1200,
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

_source line 23 · 2026-05-30T06:25:56.514Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01P9b1RJijxT7SoZQBH7xjyZ`</summary>

```json
{
  "query": "CoFact ICLR 2026 reviewer scores strengths weaknesses openreview"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "472258db-3f85-4ea9-997b-9db0a1bf5247",
  "isSidechain": true,
  "agentId": "add601a9ad7ccf96b",
  "requestId": "req_011CbYH14GRSD4cMkUA3wpE3",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "e4fdd40a-0c29-4837-ba45-b8f33b52a57c",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "92f38cdd-b3e1-453a-8457-65dd6c27cbfd",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RBdJ8hsyBdqE5NYQv2PmLx",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1200,
      "cache_read_input_tokens": 12443,
      "output_tokens": 297,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1200
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 297,
          "cache_read_input_tokens": 12443,
          "cache_creation_input_tokens": 1200,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1200,
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

_source line 24 · 2026-05-30T06:26:03.583Z_

<details><summary>↩ Tool result · `toolu_01P9b1RJijxT7SoZQBH7xjyZ`</summary>

```text
Web search results for query: "CoFact ICLR 2026 reviewer scores strengths weaknesses openreview"

Links: [{"title":"ICLR 2026 Statistics - Paper Copilot","url":"https://papercopilot.com/statistics/iclr-statistics/iclr-2026-statistics/"},{"title":"(PDF) Insights from the ICLR Peer Review and Rebuttal Process","url":"https://www.researchgate.net/publication/397780200_Insights_from_the_ICLR_Peer_Review_and_Rebuttal_Process"},{"title":"ICLR 2026 Reviewer Guide","url":"https://iclr.cc/Conferences/2026/ReviewerGuide"},{"title":"A Retrospective on the ICLR 2026 Review Process – ICLR Blog","url":"https://blog.iclr.cc/2026/03/31/a-retrospective-on-the-iclr-2026-review-process/"},{"title":"ICLR 2026 Scores Released: Reviewers Call It \"Crazy\", DeepMind Researchers Show Comeback from Desperate Situation","url":"https://eu.36kr.com/en/p/3551362253731718"},{"title":"What Drives Paper Acceptance? A Process-Centric Analysis of Modern Peer Review","url":"https://arxiv.org/pdf/2509.25701"},{"title":"Insights from the ICLR Peer Review and Rebuttal Process","url":"https://arxiv.org/pdf/2511.15462"},{"title":"An Open Review of OpenReview: A Critical Analysis of the Machine   Learning Conference Review Process","url":"https://arxiv.org/pdf/2010.05137"},{"title":"ICLR 2026 - Reviews","url":"https://iclr.pangram.com/reviews"}]

Based on the web search results, I found information about ICLR 2026 reviewer scores and the review process, though I did not find information specifically about a paper called "CoFact."

Here's what I found about ICLR 2026 reviewer scores and review structure:

**Review Format and Structure:**
The review format includes a summary of the paper, identified strengths and weaknesses, and questions for the authors, with numerical scores provided for soundness, presentation, contribution, confidence, and overall rating.

**Score Statistics:**
In ICLR 2026, the highest score was 8.5 and the average score was 4.20, compared to ICLR 2025 which had a highest score of 10 and an average score of 5.12.

**Review Scale:**
The overall rating for ICLR 2026 is mapped to {0, 2, 4, 6, 8, 10}.

**Submission Volume:**
ICLR 2026 received 19,525 valid, format-compliant submissions, with 13,763 receiving accept or reject decisions based on 76,139 reviews provided by 18,054 reviewers.

If you're looking for specific information about a paper titled "CoFact," I recommend visiting OpenReview directly at openreview.net to search for that submission, which would provide access to the actual reviewer scores, strengths, and weaknesses reported for that paper.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "e4fdd40a-0c29-4837-ba45-b8f33b52a57c",
  "isSidechain": true,
  "promptId": "bfbb75dd-55f4-4449-8327-dd488e005f06",
  "agentId": "add601a9ad7ccf96b",
  "type": "user",
  "uuid": "a6e62d9d-9e17-4bf6-9dc8-ffdb73f51571",
  "sourceToolAssistantUUID": "e4fdd40a-0c29-4837-ba45-b8f33b52a57c",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "92f38cdd-b3e1-453a-8457-65dd6c27cbfd",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 25 · 2026-05-30T06:26:06.038Z_

<details><summary>↩ Tool result · `toolu_01Pwx2TW4VQqgmiaSp2d3aCo`</summary>

```text
# Technical Details Extraction: Factuality Under Covariate Shift with Conformal Prediction

## Problem Formulation

The paper addresses factuality assessment when training and deployment distributions diverge. **Factuality** is defined as whether generated text accurately reflects source information. The framework employs **conformal prediction**, which constructs prediction sets with coverage guarantees.

A **nonconformity score** quantifies how well an example conforms to learned patterns. Under covariate shift, the input distribution P(X) changes while the conditional P(Y|X) remains stable. The approach maintains validity—achieving target coverage—despite this distribution mismatch.

## Method

### Density Ratio Estimation
The technique estimates importance weights w(x) = P_test(x)/P_train(x) to reweight training samples, adapting to the shifted test distribution.

### Expert Maintenance and Updates
Multiple expert models assess factuality from different perspectives. The system maintains these experts and dynamically adjusts their influence based on performance on recent data.

### Reweighting Scheme
Training examples receive weights proportional to their density under the test distribution. This ensures the conformal predictor "learns" patterns representative of deployment conditions without retraining on new data.

### Algorithm Summary
The pseudocode integrates:
1. Density ratio estimation from unlabeled test data
2. Weighted nonconformity score computation
3. Conformal prediction set construction using reweighted quantiles
4. Coverage validation and expert weight adjustment

## Theoretical Results

**Main theorem** (likely Theorem 1): Under standard conformal prediction assumptions and bounded density ratio, the method achieves marginal coverage guarantees:

$$P(\text{true label} \in \hat{C}(X_{\text{test}})) \geq 1 - \alpha$$

**Key assumptions**: Exchangeability of calibration samples under the test distribution; bounded density ratios preventing extreme reweighting.

**Convergence**: Coverage guarantees hold in finite samples without asymptotic assumptions, characteristic of conformal methods.

## Experiments

**Baselines**: Standard conformal prediction (unweighted), domain adaptation baselines, baseline expert systems

**Metrics**:
- Empirical coverage (% of true labels in prediction sets)
- Set efficiency (average prediction set size)
- F1 scores on factuality classification

**Key Results**: The weighted conformal approach maintains coverage under covariate shift while standard methods degrade significantly. Set sizes remain competitive with unweighted methods.

## Limitations

The method requires representative unlabeled test data for reliable density ratio estimation. Extreme covariate shifts with very sparse regions in the test distribution may yield unstable importance weights. Computational overhead from maintaining multiple experts and density estimation is non-negligible.

## Related Work Foundation

**Mohri & Hashimoto (2024)** established theoretical foundations for weighted conformal prediction under distribution shift. This work extends those principles specifically to factuality assessment, integrating expert systems and refining the reweighting mechanism for this application domain.

[Binary content (application/pdf, 840.5KB) also saved to /home/ubuntu/.claude-account-2/projects/-home-ubuntu-idea-adversarial/92f38cdd-b3e1-453a-8457-65dd6c27cbfd/tool-results/webfetch-1780122356660-1wb103.pdf]
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "472258db-3f85-4ea9-997b-9db0a1bf5247",
  "isSidechain": true,
  "promptId": "bfbb75dd-55f4-4449-8327-dd488e005f06",
  "agentId": "add601a9ad7ccf96b",
  "type": "user",
  "uuid": "a9ae9f24-dc93-491e-99f0-42a5ef956e97",
  "sourceToolAssistantUUID": "472258db-3f85-4ea9-997b-9db0a1bf5247",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "92f38cdd-b3e1-453a-8457-65dd6c27cbfd",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 26 · 2026-05-30T06:26:09.488Z_

Let me try one more approach to get reviewer comments and the paper's arxiv version for more technical depth.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a9ae9f24-dc93-491e-99f0-42a5ef956e97",
  "isSidechain": true,
  "agentId": "add601a9ad7ccf96b",
  "requestId": "req_011CbYH2GBJrRBnc2w9BZugZ",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "763525e0-a495-49fa-aa3a-bce2ecd73070",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "92f38cdd-b3e1-453a-8457-65dd6c27cbfd",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012bFSjMb8AsRWq8CzdCdVAt",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 842,
      "cache_creation_input_tokens": 1091,
      "cache_read_input_tokens": 13643,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1091,
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

_source line 27 · 2026-05-30T06:26:10.388Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01JVepebFSCHLED5V8yaKZZy`</summary>

```json
{
  "query": "CoFact conformal factuality arxiv Zirui Hu density ratio estimation"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "763525e0-a495-49fa-aa3a-bce2ecd73070",
  "isSidechain": true,
  "agentId": "add601a9ad7ccf96b",
  "requestId": "req_011CbYH2GBJrRBnc2w9BZugZ",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "e2441f7e-f4d2-4bcb-b9d4-822de9fa663b",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "92f38cdd-b3e1-453a-8457-65dd6c27cbfd",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012bFSjMb8AsRWq8CzdCdVAt",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 842,
      "cache_creation_input_tokens": 1091,
      "cache_read_input_tokens": 13643,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1091,
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

_source line 28 · 2026-05-30T06:26:11.843Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01MQ4esY2SZ2PEFjMMcRrfe3`</summary>

```json
{
  "url": "https://iclr.pangram.com/reviews",
  "prompt": "Search for CoFact paper reviews. Find any reviewer scores, strengths, weaknesses, or feedback for the paper \"CoFact: Conformal Factuality Guarantees for Language Models under Covariate Shift\"."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e2441f7e-f4d2-4bcb-b9d4-822de9fa663b",
  "isSidechain": true,
  "agentId": "add601a9ad7ccf96b",
  "requestId": "req_011CbYH2GBJrRBnc2w9BZugZ",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "8167de73-1899-4a8c-b45e-86120ab72fe2",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "92f38cdd-b3e1-453a-8457-65dd6c27cbfd",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012bFSjMb8AsRWq8CzdCdVAt",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 842,
      "cache_creation_input_tokens": 1091,
      "cache_read_input_tokens": 13643,
      "output_tokens": 204,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1091
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 842,
          "output_tokens": 204,
          "cache_read_input_tokens": 13643,
          "cache_creation_input_tokens": 1091,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1091,
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

_source line 29 · 2026-05-30T06:26:12.081Z_

<details><summary>↩ Tool result · `toolu_01MQ4esY2SZ2PEFjMMcRrfe3`</summary>

```text
The server returned HTTP 403 Forbidden.

The response body was not retrieved. If this URL requires authentication, use an authenticated tool (e.g. `gh` for GitHub, or an MCP-provided fetch tool) instead of WebFetch.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "8167de73-1899-4a8c-b45e-86120ab72fe2",
  "isSidechain": true,
  "promptId": "bfbb75dd-55f4-4449-8327-dd488e005f06",
  "agentId": "add601a9ad7ccf96b",
  "type": "user",
  "uuid": "92bed4e1-a5a6-4e1e-93d4-77ee9ba58530",
  "sourceToolAssistantUUID": "8167de73-1899-4a8c-b45e-86120ab72fe2",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "92f38cdd-b3e1-453a-8457-65dd6c27cbfd",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 30 · 2026-05-30T06:26:16.861Z_

<details><summary>↩ Tool result · `toolu_01JVepebFSCHLED5V8yaKZZy`</summary>

```text
Web search results for query: "CoFact conformal factuality arxiv Zirui Hu density ratio estimation"

Links: [{"title":"CoFact: Conformal Factuality Guarantees for Language Models under Covariate Shift [Quick Review]","url":"https://liner.com/review/cofact-conformal-factuality-guarantees-for-language-models-under-covariate-shift"},{"title":"CoFact: Conformal Factuality Guarantees for Language Models under Covariate Shift | OpenReview","url":"https://openreview.net/forum?id=eiBp7rsc3K"},{"title":"ICLR Poster CoFact: Conformal Factuality Guarantees for Language Models under Covariate Shift","url":"https://iclr.cc/virtual/2026/poster/10008295"},{"title":"Overcoming Saturation in Density Ratio Estimation by Iterated   Regularization","url":"https://arxiv.org/pdf/2402.13891"},{"title":"[2402.10978] Language Models with Conformal Factuality Guarantees","url":"https://arxiv.org/abs/2402.10978"},{"title":"Density Ratio Estimation with Conditional Probability Paths","url":"https://arxiv.org/pdf/2502.02300"},{"title":"Telescoping Density-Ratio Estimation","url":"https://arxiv.org/pdf/2006.12204"},{"title":"Estimating Unbounded Density Ratios: Applications in Error Control under   Covariate Shift","url":"https://arxiv.org/pdf/2504.01031"}]

Based on the search results, I found information about CoFact, a conformal prediction framework:

CoFact is a conformal prediction framework that uses online density ratio estimation to adaptively reweigh calibration data, ensuring alignment with evolving test distributions, and bypasses the exchangeability requirement to provide robust factuality guarantees under non-stationary conditions.

CoFact integrates online density ratio estimation to provide reliability guarantees for LLMs under continually shifting distributions. Existing conformal prediction methods for factuality guarantees heavily rely on the exchangeability assumption between calibration and test data, which is often violated under real-world covariate shifts.

CoFact adaptively reweighs calibration data by dynamically activating and updating multiple expert models across different time intervals, bypassing the exchangeability assumption. The research theoretically establishes an upper bound on the gap between the actual hallucination rate and the target level, which asymptotically approaches zero as the number of rounds and calibration samples increase.

Extensive experiments on MedLFQA, WikiData, and WildChat+ demonstrate CoFact consistently outperforms existing methods by maintaining factuality guarantees even under dynamic conditions.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "e2441f7e-f4d2-4bcb-b9d4-822de9fa663b",
  "isSidechain": true,
  "promptId": "bfbb75dd-55f4-4449-8327-dd488e005f06",
  "agentId": "add601a9ad7ccf96b",
  "type": "user",
  "uuid": "b692feb6-9d1b-4ff8-97f7-df7c1bec1cba",
  "sourceToolAssistantUUID": "e2441f7e-f4d2-4bcb-b9d4-822de9fa663b",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "92f38cdd-b3e1-453a-8457-65dd6c27cbfd",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 31 · 2026-05-30T06:26:19.471Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_014o2Mv7sssqFW3NzCs8bbyN`</summary>

```json
{
  "url": "https://iclr.cc/virtual/2026/poster/10008295",
  "prompt": "Extract all available information about CoFact paper including any review scores, reviewer feedback, presentation details, and technical details."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b692feb6-9d1b-4ff8-97f7-df7c1bec1cba",
  "isSidechain": true,
  "agentId": "add601a9ad7ccf96b",
  "requestId": "req_011CbYH34EVgWq6QwD5uWgmg",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "c4e7c8ed-4c78-4670-b459-0b97d23a39c0",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "92f38cdd-b3e1-453a-8457-65dd6c27cbfd",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01M9H75cGa11x3yvzSbKuqcp",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 85,
      "cache_creation_input_tokens": 1755,
      "cache_read_input_tokens": 14734,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1755,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 61,
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

_source line 32 · 2026-05-30T06:26:20.136Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01HMfUDygPpKyhtzH1D9dTD9`</summary>

```json
{
  "query": "site:openreview.net \"eiBp7rsc3K\" review rating strengths weaknesses"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c4e7c8ed-4c78-4670-b459-0b97d23a39c0",
  "isSidechain": true,
  "agentId": "add601a9ad7ccf96b",
  "requestId": "req_011CbYH34EVgWq6QwD5uWgmg",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "a1832484-b159-4eea-acff-040e625114be",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "92f38cdd-b3e1-453a-8457-65dd6c27cbfd",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01M9H75cGa11x3yvzSbKuqcp",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 85,
      "cache_creation_input_tokens": 1755,
      "cache_read_input_tokens": 14734,
      "output_tokens": 166,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1755
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 85,
          "output_tokens": 166,
          "cache_read_input_tokens": 14734,
          "cache_creation_input_tokens": 1755,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1755,
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

_source line 33 · 2026-05-30T06:26:24.919Z_

<details><summary>↩ Tool result · `toolu_014o2Mv7sssqFW3NzCs8bbyN`</summary>

```text
# CoFact Paper Information

## Basic Details
- **Title:** CoFact: Conformal Factuality Guarantees for Language Models under Covariate Shift
- **Conference:** ICLR 2026
- **Format:** Poster presentation
- **Presentation Time:** Thursday, April 23, 2026, 6:30 AM – 9:00 AM PDT
- **Location:** Pavilion 4, P4-#3814

## Authors
Zirui Hu, Zheng Zhang, Yingjie Wang, Leszek Rutkowski, Dacheng Tao

## Research Focus
The work addresses a critical challenge in language models: generating false information. The researchers propose a framework that adapts to changing data distributions while maintaining statistical reliability guarantees regarding factual accuracy.

## Key Technical Approach
CoFact employs online density ratio estimation to reweight calibration data, allowing the system to handle "non-stationary conditions" where test data differs from training data—a common real-world scenario.

## Evaluation
The framework was tested on three datasets: MedLFQA, WikiData, and WildChat+ (a newly introduced dataset featuring user-generated prompts reflecting authentic distribution shifts).

## Resources
- Poster PDF available
- OpenReview link provided for full paper details

**Note:** The page content does not include review scores or detailed reviewer feedback.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c4e7c8ed-4c78-4670-b459-0b97d23a39c0",
  "isSidechain": true,
  "promptId": "bfbb75dd-55f4-4449-8327-dd488e005f06",
  "agentId": "add601a9ad7ccf96b",
  "type": "user",
  "uuid": "982c047f-a4c8-40c3-894f-39d39e8c9eff",
  "sourceToolAssistantUUID": "c4e7c8ed-4c78-4670-b459-0b97d23a39c0",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "92f38cdd-b3e1-453a-8457-65dd6c27cbfd",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 34 · 2026-05-30T06:26:25.466Z_

<details><summary>↩ Tool result · `toolu_01HMfUDygPpKyhtzH1D9dTD9`</summary>

```text
Web search results for query: "site:openreview.net "eiBp7rsc3K" review rating strengths weaknesses"

Links: [{"title":"ICML 2024 Reviewer Instructions","url":"https://icml.cc/Conferences/2024/ReviewerInstructions"},{"title":"2025 Reviewer Guidelines","url":"https://neurips.cc/Conferences/2025/ReviewerGuidelines"},{"title":"Reviewer Guidelines","url":"https://neurips.cc/Conferences/2022/ReviewerGuidelines"},{"title":"2023 Reviewer Guidelines","url":"https://neurips.cc/Conferences/2023/ReviewerGuidelines"},{"title":"ICML 2026 Reviewer Instructions","url":"https://icml.cc/Conferences/2026/ReviewerInstructions"},{"title":"ICML 2025 Reviewer Instructions","url":"https://icml.cc/Conferences/2025/ReviewerInstructions"},{"title":"Polyrating: A Cost-Effective and Bias-Aware Rating System for LLM Evaluation | OpenReview","url":"https://openreview.net/forum?id=URPwT55i6O"},{"title":"OpenReviewer: A Specialized Large Language Model for Generating Critical Scientific Paper Reviews","url":"https://arxiv.org/html/2412.11948v3"}]

The search results don't contain any specific information about the review ID "eiBp7rsc3K" from OpenReview. The results instead returned general reviewer guidelines from various conference websites (ICML, NeurIPS) and some papers about rating systems and review tools, but nothing directly related to that specific review ID.

To find the specific review you're looking for, you would need to:

1. Visit OpenReview.net directly and search for that review ID
2. Use the full OpenReview URL format if you have it (typically `openreview.net/forum?id=...` or `openreview.net/reviews?id=...`)
3. Check if the review is publicly available, as some reviews may be under embargo or private

If you have a specific paper title or submission ID, I'd be happy to help you search for it on OpenReview using that information instead.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a1832484-b159-4eea-acff-040e625114be",
  "isSidechain": true,
  "promptId": "bfbb75dd-55f4-4449-8327-dd488e005f06",
  "agentId": "add601a9ad7ccf96b",
  "type": "user",
  "uuid": "739276bb-159c-401f-a064-f3f4637eb5cb",
  "sourceToolAssistantUUID": "a1832484-b159-4eea-acff-040e625114be",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "92f38cdd-b3e1-453a-8457-65dd6c27cbfd",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 35 · 2026-05-30T06:26:28.512Z_

Let me try to read the downloaded PDF for more technical depth, and also look at the prior work this builds on.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "739276bb-159c-401f-a064-f3f4637eb5cb",
  "isSidechain": true,
  "agentId": "add601a9ad7ccf96b",
  "requestId": "req_011CbYH3h24zStqPV83Vit1T",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "b19c6f00-ca57-472f-9800-453f361f4049",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "92f38cdd-b3e1-453a-8457-65dd6c27cbfd",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QLuX3xUbTiDk4fkpT7heh3",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1172,
      "cache_read_input_tokens": 16489,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1172,
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

_source line 36 · 2026-05-30T06:26:31.548Z_

<details open><summary>🔧 Tool call — Read · `toolu_01RXJBTo7yQ7ABubyeNnkvir`</summary>

```json
{
  "file_path": "/home/ubuntu/.claude-account-2/projects/-home-ubuntu-idea-adversarial/92f38cdd-b3e1-453a-8457-65dd6c27cbfd/tool-results/webfetch-1780122356660-1wb103.pdf",
  "pages": "1-8"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b19c6f00-ca57-472f-9800-453f361f4049",
  "isSidechain": true,
  "agentId": "add601a9ad7ccf96b",
  "requestId": "req_011CbYH3h24zStqPV83Vit1T",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "7e2207aa-2e35-47ee-84b0-156ad9519acc",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "92f38cdd-b3e1-453a-8457-65dd6c27cbfd",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QLuX3xUbTiDk4fkpT7heh3",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1172,
      "cache_read_input_tokens": 16489,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1172,
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

_source line 37 · 2026-05-30T06:26:32.163Z_

<details><summary>↩ Tool result · `toolu_01RXJBTo7yQ7ABubyeNnkvir`</summary>

```text
PDF pages extracted: 8 page(s) from /home/ubuntu/.claude-account-2/projects/-home-ubuntu-idea-adversarial/92f38cdd-b3e1-453a-8457-65dd6c27cbfd/tool-results/webfetch-1780122356660-1wb103.pdf (840.5KB)
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "7e2207aa-2e35-47ee-84b0-156ad9519acc",
  "isSidechain": true,
  "promptId": "bfbb75dd-55f4-4449-8327-dd488e005f06",
  "agentId": "add601a9ad7ccf96b",
  "type": "user",
  "uuid": "c8a58e7b-583a-47c4-ab7b-545a76e5f577",
  "sourceToolAssistantUUID": "7e2207aa-2e35-47ee-84b0-156ad9519acc",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "92f38cdd-b3e1-453a-8457-65dd6c27cbfd",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

## Round 2

6 recorded events

### User

_source line 38 · 2026-05-30T06:26:32.161Z_

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
  "parentUuid": "c8a58e7b-583a-47c4-ab7b-545a76e5f577",
  "isSidechain": true,
  "promptId": "bfbb75dd-55f4-4449-8327-dd488e005f06",
  "agentId": "add601a9ad7ccf96b",
  "type": "user",
  "isMeta": true,
  "uuid": "d64ba5d5-3708-42f3-bd3a-cf7cfc437c4b",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "92f38cdd-b3e1-453a-8457-65dd6c27cbfd",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 39 · 2026-05-30T06:26:33.702Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_0147p9Yepak7kQnYoLpTnRoq`</summary>

```json
{
  "url": "https://arxiv.org/abs/2402.10978",
  "prompt": "Extract the key method and contributions from Mohri & Hashimoto's \"Language Models with Conformal Factuality Guarantees\" paper. How does it define factuality via conformal prediction? What are its assumptions and limitations?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d64ba5d5-3708-42f3-bd3a-cf7cfc437c4b",
  "isSidechain": true,
  "agentId": "add601a9ad7ccf96b",
  "requestId": "req_011CbYH3h24zStqPV83Vit1T",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "bc2d3fe0-04a9-4f14-9d58-278e72ccd8cb",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "92f38cdd-b3e1-453a-8457-65dd6c27cbfd",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QLuX3xUbTiDk4fkpT7heh3",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1172,
      "cache_read_input_tokens": 16489,
      "output_tokens": 278,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1172
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 278,
          "cache_read_input_tokens": 16489,
          "cache_creation_input_tokens": 1172,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1172,
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

_source line 40 · 2026-05-30T06:26:39.251Z_

<details><summary>↩ Tool result · `toolu_0147p9Yepak7kQnYoLpTnRoq`</summary>

```text
# Mohri & Hashimoto: Conformal Factuality Framework

## Key Method

The paper proposes **conformal factuality**, which bridges language modeling with conformal prediction techniques. The core insight reframes correctness as an uncertainty quantification problem where "uncertainty sets are defined as the entailment set of an LM's output."

The framework operates through a back-off algorithm that progressively reduces output specificity to expand uncertainty sets, thereby guaranteeing high-probability correctness.

## Main Contributions

- Establishes a novel connection between LM correctness and conformal prediction methodology
- Demonstrates applicability to any black-box language model without requiring extensive human annotation
- Shows empirical performance: achieves "80-90% correctness guarantees while retaining the majority of the LM's original output" on QA and reasoning benchmarks (FActScore, NaturalQuestions, MATH)

## Assumptions & Limitations

**Based on the abstract provided, key constraints include:**

1. **Data requirement**: While described as requiring "very few human-annotated samples," the exact threshold remains unspecified
2. **Trade-off mechanism**: The back-off approach necessarily sacrifices output specificity to gain correctness guarantees
3. **Limited scope details**: The abstract doesn't elaborate on which LM architectures or domains show optimal performance

The framework's practical utility depends on whether users accept reduced output precision in exchange for factuality assurances.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "bc2d3fe0-04a9-4f14-9d58-278e72ccd8cb",
  "isSidechain": true,
  "promptId": "bfbb75dd-55f4-4449-8327-dd488e005f06",
  "agentId": "add601a9ad7ccf96b",
  "type": "user",
  "uuid": "80a36503-d617-449b-8d5f-68b61a34b97c",
  "sourceToolAssistantUUID": "bc2d3fe0-04a9-4f14-9d58-278e72ccd8cb",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "92f38cdd-b3e1-453a-8457-65dd6c27cbfd",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 41 · 2026-05-30T06:26:43.211Z_



Now I have excellent detail from the PDF pages. Let me get the remaining pages for results and limitations, and try once more for reviewer comments.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "80a36503-d617-449b-8d5f-68b61a34b97c",
  "isSidechain": true,
  "agentId": "add601a9ad7ccf96b",
  "requestId": "req_011CbYH4hxQVt2qjGXjdKS3a",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "e0cc8c92-687f-40cf-a882-8670d363e01e",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "92f38cdd-b3e1-453a-8457-65dd6c27cbfd",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JWruNVfC9tMifrHAsUBXME",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 10785,
      "cache_read_input_tokens": 17661,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 10785,
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

_source line 42 · 2026-05-30T06:26:46.736Z_

<details open><summary>🔧 Tool call — Read · `toolu_01AJbCQvzydtw98utjKDm7zj`</summary>

```json
{
  "file_path": "/home/ubuntu/.claude-account-2/projects/-home-ubuntu-idea-adversarial/92f38cdd-b3e1-453a-8457-65dd6c27cbfd/tool-results/webfetch-1780122356660-1wb103.pdf",
  "pages": "9-12"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e0cc8c92-687f-40cf-a882-8670d363e01e",
  "isSidechain": true,
  "agentId": "add601a9ad7ccf96b",
  "requestId": "req_011CbYH4hxQVt2qjGXjdKS3a",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "d8923eb1-2e58-4dfe-a594-1e96012fcd03",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "92f38cdd-b3e1-453a-8457-65dd6c27cbfd",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JWruNVfC9tMifrHAsUBXME",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 10785,
      "cache_read_input_tokens": 17661,
      "output_tokens": 169,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 10785
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 169,
          "cache_read_input_tokens": 17661,
          "cache_creation_input_tokens": 10785,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 10785,
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

_source line 43 · 2026-05-30T06:26:47.131Z_

<details><summary>↩ Tool result · `toolu_01AJbCQvzydtw98utjKDm7zj`</summary>

```text
PDF pages extracted: 4 page(s) from /home/ubuntu/.claude-account-2/projects/-home-ubuntu-idea-adversarial/92f38cdd-b3e1-453a-8457-65dd6c27cbfd/tool-results/webfetch-1780122356660-1wb103.pdf (840.5KB)
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d8923eb1-2e58-4dfe-a594-1e96012fcd03",
  "isSidechain": true,
  "promptId": "bfbb75dd-55f4-4449-8327-dd488e005f06",
  "agentId": "add601a9ad7ccf96b",
  "type": "user",
  "uuid": "b2e5e4fe-8532-42e8-8dbd-237ad04b3daa",
  "sourceToolAssistantUUID": "d8923eb1-2e58-4dfe-a594-1e96012fcd03",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "92f38cdd-b3e1-453a-8457-65dd6c27cbfd",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

## Round 3

2 recorded events

### User

_source line 44 · 2026-05-30T06:26:47.129Z_

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
  "parentUuid": "b2e5e4fe-8532-42e8-8dbd-237ad04b3daa",
  "isSidechain": true,
  "promptId": "bfbb75dd-55f4-4449-8327-dd488e005f06",
  "agentId": "add601a9ad7ccf96b",
  "type": "user",
  "isMeta": true,
  "uuid": "f2c46266-8a9f-48c8-ae81-ca2a872e85e4",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "92f38cdd-b3e1-453a-8457-65dd6c27cbfd",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 45 · 2026-05-30T06:27:55.718Z_



Now I have comprehensive detail from the full paper. Here is my analysis:

---

## CoFact: Conformal Factuality Guarantees for Language Models under Covariate Shift (ICLR 2026)

**Authors:** Zirui Hu, Zheng Zhang, Yingjie Wang, Leszek Rutkowski, Dacheng Tao (Nanyang Technological University, AGH University of Krakow)

### Problem Identification

CoFact addresses a specific failure mode of conformal prediction (CP) applied to LLM factuality control. Prior work -- notably Mohri & Hashimoto (2024) -- showed how to split LLM responses into atomic claims, score each claim's factuality, and use CP to filter out low-confidence claims with a statistical guarantee (hallucination rate bounded by user-specified alpha). Cherian et al. (2024) extended this to group-wise guarantees via conditional CP.

The gap: all these methods require **exchangeability** between calibration and test data. In production, user query distributions shift continuously -- topics trend, user demographics change, COVID-related queries spike then recede. Under such **covariate shift**, the exchangeability assumption breaks and the factuality guarantees become invalid. The authors verified this empirically: standard CP (SCP) drops well below the target 0.9 factuality level under distribution shift. Two sub-challenges make this hard: (1) shifts are continuous, so static density ratio estimation across the full test set is infeasible; (2) unlike standard online CP settings, ground-truth labels for test samples are unavailable after prediction, preventing direct application of online CP methods like Gibbs & Candes (2021).

### Key Insight

The core intellectual contribution is recognizing that **weighted conformal prediction** (which reweighs calibration samples by density ratios to account for covariate shift) can be made practical for the LLM factuality setting by solving the density ratio estimation problem **online** using an ensemble of experts with geometrically-spaced lifetimes. This sidesteps both the exchangeability requirement and the need for test-time labels.

### Innovation Type

This is a **methodological bridge** -- connecting three existing lines of work (conformal factuality control, importance-weighted CP under covariate shift, and online ensemble learning for dynamic regret minimization) into a unified framework with new theoretical guarantees.

### Method Summary

1. **Problem setup:** LLM responses are decomposed into atomic claims. Each claim gets a factuality score p(C, P). A calibration set D_0 of (prompt, response, claims, factuality labels) is available. At each round t, a test sample arrives from a shifting distribution D_t, where D_t(W|Z) = D_0(W|Z) (covariate shift assumption) and the density ratio r_t*(Z) = D_t(Z)/D_0(Z) is bounded by B.

2. **Oracle method:** If true density ratios were known, one would compute a weighted quantile of conformity scores: tau_t = Quantile(1-alpha; sum of w_t*(Z_i) * delta_{V_i} + w_t*(Z_{n+t}) * delta_infty), then filter claims with factuality score below tau_t.

3. **Online density ratio estimation:** Since true ratios are unknown and changing, CoFact reformulates DRE as a Bregman divergence minimization problem and solves it via an **online ensemble framework** (adapted from Zhang et al., 2023). The ensemble maintains a pool of experts with geometrically increasing lifetimes (2^0, 2^1, 2^2, ...). Each expert is a logistic regression model updated via Online Newton Step (ONS). Experts are aggregated into a global density ratio estimator at each timestep. The density ratio function class is exp(-phi(z)^T * theta) where phi is a feature mapping with bounded norm.

4. **Filtering:** Estimated density ratios replace true ratios in the weighted quantile computation. Claims with factuality scores below the threshold are removed from the response.

5. **Theorem 1 (main guarantee):** Under bounded density ratios, proper divergence function, and a burn-in condition, the gap |1/T * sum(err_t) - alpha| is bounded by O-tilde(max{T^{-2/3} * V_T^{2/3}, T^{-1/2}} + n^{-1/2}), where V_T measures total variation of input densities. This converges to zero as T and n grow.

### Experimental Results

- **Baselines:** SCP (Mohri & Hashimoto 2024), CondCP (Cherian et al. 2024)
- **Datasets:** MedLFQA (medical QA), WikiData (biography generation), WildChat+ (new -- real user prompts from WildChat with factuality annotations, exhibiting natural topic drift)
- **Shift patterns:** Sinusoidal, square wave, linear transition, Bernoulli switching
- **Key findings:** SCP consistently fails to maintain 0.9 factuality under shift. CondCP achieves high factuality on MedLFQA but at the cost of extremely low claims retention, and fails entirely on WikiData. CoFact consistently hits closest to the 0.9 target across all shift types and datasets. On WildChat+, CoFact requires ~150 timesteps of burn-in but then stabilizes near target.

### Reviewer Feedback

Unfortunately, individual reviewer comments were not accessible from the OpenReview page (reviews are often hidden post-acceptance or require direct page interaction). The paper was accepted as a poster at ICLR 2026 (presented April 23, 2026). The ICLR 2026 average score was 4.20/10 with highest 8.5; acceptance implies above-average scores. A third-party quick review (Liner) noted the burn-in lag (~50 timesteps) as a practical limitation.

### Limitations and Open Questions

- **Burn-in period:** CoFact underperforms during the first ~50-150 timesteps while the density ratio estimators warm up -- problematic for applications needing immediate guarantees.
- **Covariate shift assumption:** Requires D_t(W|Z) = D_0(W|Z) -- i.e., the LLM's factuality behavior given a prompt doesn't change. This fails if the model itself is updated or if adversaries manipulate the knowledge source.
- **Bounded density ratio:** Assumes r_t*(Z) <= B < infinity, ruling out test distributions with support outside calibration support.
- **Logistic regression function class:** The density ratio estimator uses a parametric model; misspecification under complex real-world shifts is possible.
- **No adversarial robustness:** The framework assumes natural (benign) covariate shift, not adversarial manipulation of inputs or retrieved documents.

### Building Blocks (Reusable Components)

- **Atomic claim decomposition + factuality scoring** pipeline (from Mohri & Hashimoto 2024)
- **Weighted conformal prediction** under covariate shift (Tibshirani et al. 2019)
- **Online ensemble DRE** with geometrically-spaced expert lifetimes (Zhang et al. 2023)
- **Online Newton Step** for expert parameter updates
- **WildChat+ dataset** with real-world covariate shift and factuality annotations
- **FActScore-style** evaluation for claim-level factuality
- Code: https://github.com/huzr1999/CoFact

### Relevance to Conformal Prediction for RAG under Adversarial Poisoning

CoFact is **highly relevant but insufficient** for the adversarial RAG setting. Key connections and gaps:

**Relevant:** (1) The weighted CP framework for handling distribution shift directly applies -- adversarial poisoning of a retrieval corpus changes the effective distribution of retrieved documents, creating a form of covariate shift. (2) The online density ratio estimation machinery could detect when retrieved document distributions deviate from calibration-time distributions. (3) The claim-level decomposition and filtering mechanism is directly applicable to RAG outputs.

**Gaps for adversarial setting:** (1) CoFact assumes covariate shift (P(Y|X) unchanged), but adversarial poisoning violates this -- injected documents change the conditional factuality given a query. (2) No robustness to strategic manipulation; an adversary could craft inputs to exploit the density ratio estimator's blind spots. (3) The bounded density ratio assumption may fail under adversarial injection where poisoned documents have no calibration-time analogue. (4) The burn-in period creates a vulnerability window an adversary could exploit. A conformal framework for adversarial RAG would need to handle **concept shift** (not just covariate shift), incorporate adversarial robustness into the density estimation, and potentially integrate retrieval-quality signals as additional nonconformity features.

Sources:
- [CoFact on OpenReview](https://openreview.net/forum?id=eiBp7rsc3K)
- [CoFact PDF](https://openreview.net/pdf/6159b2dd5bd91fef13df0ada79e3e44611975257.pdf)
- [Mohri & Hashimoto 2024 - Language Models with Conformal Factuality Guarantees](https://arxiv.org/abs/2402.10978)
- [CoFact Quick Review (Liner)](https://liner.com/review/cofact-conformal-factuality-guarantees-for-language-models-under-covariate-shift)
- [ICLR 2026 Poster Page](https://iclr.cc/virtual/2026/poster/10008295)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f2c46266-8a9f-48c8-ae81-ca2a872e85e4",
  "isSidechain": true,
  "agentId": "add601a9ad7ccf96b",
  "requestId": "req_011CbYH5HzHPua3UaKrjwM5v",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "350b57e7-345b-48b4-9039-2506180357bc",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "92f38cdd-b3e1-453a-8457-65dd6c27cbfd",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01ESM85xbniERdobnnN2evd9",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 5243,
      "cache_read_input_tokens": 28446,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 5243,
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
