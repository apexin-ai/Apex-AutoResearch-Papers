# Research conversation: Search the web for negative result papers accepted at top NLP conferences (EMNLP, ACL, NAACL) in 2024-2026, especially m

**Exposure Bias Collapses Auxiliary Attention Losses in Multi-Turn Dialogue (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 63
- **Recorded user turns:** 1
- **Tool calls:** 26
- **Original source:** `logs/chats/exported-trajectories/account-1/agent-a2210751531ccd330.jsonl`
- **Structured JSON:** [`8457c8a130ff61592479.json`](../../sessions/84/8457c8a130ff61592479.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

63 recorded events

### User

_source line 1 · 2026-05-19T02:59:57.707Z_

Search the web for negative result papers accepted at top NLP conferences (EMNLP, ACL, NAACL) in 2024-2026, especially main track. I need to find:

1. Examples of accepted negative result papers at EMNLP 2024/2025, ACL 2024/2025, NAACL 2024/2025
2. Whether these venues have specific tracks or acceptance criteria for negative results
3. The contribution patterns of successful negative result papers (what makes them publishable?)
4. Any workshops specifically for negative results in NLP/ML (e.g., "Insights from Negative Results in NLP" workshop at EMNLP)

Use WebSearch with queries like:
- "negative result paper EMNLP 2024 2025 accepted"
- "EMNLP insights from negative results workshop"
- "ACL negative results accepted main track 2024"
- "negative result paper NLP conference contribution pattern"
- "when does negative result paper get accepted top venue"
- "EMNLP findings negative result"

Report: specific examples of accepted negative result papers (title, venue, what they showed), and the general acceptance criteria/patterns for such papers at these venues.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "d62aafe3-d75b-460d-a9bb-1b0f23cd5965",
  "agentId": "a2210751531ccd330",
  "type": "user",
  "uuid": "9c922907-ef9d-49aa-a4c7-6f27affd220a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/.claude/sessions/reviewer_e7517921",
  "sessionId": "5a74afe6-047b-48bc-9683-816dae74ac45",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "starry-mapping-hearth"
}
```

</details>

---

### Runtime record

_source line 2 · 2026-05-19T02:59:57.712Z_

```json
{
  "parentUuid": "9c922907-ef9d-49aa-a4c7-6f27affd220a",
  "isSidechain": true,
  "agentId": "a2210751531ccd330",
  "attachment": {
    "type": "deferred_tools_delta",
    "addedNames": [
      "CronCreate",
      "CronDelete",
      "CronList",
      "EnterWorktree",
      "ExitWorktree",
      "ListMcpResourcesTool",
      "Monitor",
      "NotebookEdit",
      "PushNotification",
      "ReadMcpResourceTool",
      "RemoteTrigger",
      "TaskStop",
      "TodoWrite",
      "WebFetch",
      "WebSearch",
      "mcp__agent-ml-research__cleanup_pdf_images",
      "mcp__agent-ml-research__compute_coverage_matrix",
      "mcp__agent-ml-research__fetch_wandb_metrics",
      "mcp__agent-ml-research__get_gpu_health",
      "mcp__agent-ml-research__get_project_resource_usage",
      "mcp__agent-ml-research__list_constraints",
      "mcp__agent-ml-research__pdf_to_images",
      "mcp__agent-ml-research__read_experiment_plan_with_status",
      "mcp__agent-ml-research__read_matrix",
      "mcp__agent-ml-research__read_project_file",
      "mcp__agent-ml-research__read_registry",
      "mcp__agent-ml-research__read_roadmap",
      "mcp__agent-ml-research__reviewer_post_to_director",
      "mcp__agent-ml-research__ssh_read_only",
      "mcp__agent-ml-research__tail_training_logs"
    ],
    "addedLines": [
      "CronCreate",
      "CronDelete",
      "CronList",
      "EnterWorktree",
      "ExitWorktree",
      "ListMcpResourcesTool",
      "Monitor",
      "NotebookEdit",
      "PushNotification",
      "ReadMcpResourceTool",
      "RemoteTrigger",
      "TaskStop",
      "TodoWrite",
      "WebFetch",
      "WebSearch",
      "mcp__agent-ml-research__cleanup_pdf_images",
      "mcp__agent-ml-research__compute_coverage_matrix",
      "mcp__agent-ml-research__fetch_wandb_metrics",
      "mcp__agent-ml-research__get_gpu_health",
      "mcp__agent-ml-research__get_project_resource_usage",
      "mcp__agent-ml-research__list_constraints",
      "mcp__agent-ml-research__pdf_to_images",
      "mcp__agent-ml-research__read_experiment_plan_with_status",
      "mcp__agent-ml-research__read_matrix",
      "mcp__agent-ml-research__read_project_file",
      "mcp__agent-ml-research__read_registry",
      "mcp__agent-ml-research__read_roadmap",
      "mcp__agent-ml-research__reviewer_post_to_director",
      "mcp__agent-ml-research__ssh_read_only",
      "mcp__agent-ml-research__tail_training_logs"
    ],
    "removedNames": []
  },
  "type": "attachment",
  "uuid": "a64501b5-f2a6-45a8-bd2a-8573d83eecc6",
  "timestamp": "2026-05-19T02:59:57.712Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/.claude/sessions/reviewer_e7517921",
  "sessionId": "5a74afe6-047b-48bc-9683-816dae74ac45",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "starry-mapping-hearth"
}
```

---

### Assistant

_source line 3 · 2026-05-19T03:00:00.114Z_



I'll search for negative result papers at top NLP venues systematically.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a64501b5-f2a6-45a8-bd2a-8573d83eecc6",
  "isSidechain": true,
  "agentId": "a2210751531ccd330",
  "requestId": "req_011CbBBQTq8HMSQqSrDYxzun",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "f0310d63-8cd6-4f54-9f08-0bd69c9b8c15",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/.claude/sessions/reviewer_e7517921",
  "sessionId": "5a74afe6-047b-48bc-9683-816dae74ac45",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "starry-mapping-hearth",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UNg8B1YfrueTkAEETujXPj",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 15865,
      "cache_read_input_tokens": 8262,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 15865,
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

_source line 4 · 2026-05-19T03:00:00.456Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_013PPuFJbKuptgAvJHZFSwQ6`</summary>

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
  "parentUuid": "f0310d63-8cd6-4f54-9f08-0bd69c9b8c15",
  "isSidechain": true,
  "agentId": "a2210751531ccd330",
  "requestId": "req_011CbBBQTq8HMSQqSrDYxzun",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "de8c2652-4b8a-4652-ada0-848347138d98",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/.claude/sessions/reviewer_e7517921",
  "sessionId": "5a74afe6-047b-48bc-9683-816dae74ac45",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "starry-mapping-hearth",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UNg8B1YfrueTkAEETujXPj",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 15865,
      "cache_read_input_tokens": 8262,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 15865,
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

### Tool result

_source line 5 · 2026-05-19T03:00:00.460Z_

<details><summary>↩ Tool result · `toolu_013PPuFJbKuptgAvJHZFSwQ6`</summary>

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
  "parentUuid": "de8c2652-4b8a-4652-ada0-848347138d98",
  "isSidechain": true,
  "promptId": "d62aafe3-d75b-460d-a9bb-1b0f23cd5965",
  "agentId": "a2210751531ccd330",
  "type": "user",
  "uuid": "15339a85-558b-4d02-a113-582bf8a2a3c1",
  "sourceToolAssistantUUID": "de8c2652-4b8a-4652-ada0-848347138d98",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/.claude/sessions/reviewer_e7517921",
  "sessionId": "5a74afe6-047b-48bc-9683-816dae74ac45",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "starry-mapping-hearth"
}
```

</details>

---

### Assistant

_source line 6 · 2026-05-19T03:00:03.352Z_



Running multiple searches in parallel to cover the key angles.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "15339a85-558b-4d02-a113-582bf8a2a3c1",
  "isSidechain": true,
  "agentId": "a2210751531ccd330",
  "requestId": "req_011CbBBQgGjgDccFiuGsNVZR",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "03601de6-cc5e-4e8b-a288-dd5a0d32eaff",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/.claude/sessions/reviewer_e7517921",
  "sessionId": "5a74afe6-047b-48bc-9683-816dae74ac45",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "starry-mapping-hearth",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FdmwC5JJD7oaDtpbrSr86T",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1456,
      "cache_read_input_tokens": 24127,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1456,
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

_source line 7 · 2026-05-19T03:00:03.365Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01RE8geNmdtxod64WBkQmo16`</summary>

```json
{
  "query": "negative result paper EMNLP 2024 2025 accepted main track"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "03601de6-cc5e-4e8b-a288-dd5a0d32eaff",
  "isSidechain": true,
  "agentId": "a2210751531ccd330",
  "requestId": "req_011CbBBQgGjgDccFiuGsNVZR",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "7d758c74-ac93-4ff8-b916-aeb4c569dc6a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/.claude/sessions/reviewer_e7517921",
  "sessionId": "5a74afe6-047b-48bc-9683-816dae74ac45",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "starry-mapping-hearth",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FdmwC5JJD7oaDtpbrSr86T",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1456,
      "cache_read_input_tokens": 24127,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1456,
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

_source line 8 · 2026-05-19T03:00:03.896Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_013vkGK88y3kf67BNheYRUZH`</summary>

```json
{
  "query": "EMNLP \"Insights from Negative Results\" workshop 2024 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7d758c74-ac93-4ff8-b916-aeb4c569dc6a",
  "isSidechain": true,
  "agentId": "a2210751531ccd330",
  "requestId": "req_011CbBBQgGjgDccFiuGsNVZR",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "76495545-d247-4daf-b481-49cac6ff7c23",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/.claude/sessions/reviewer_e7517921",
  "sessionId": "5a74afe6-047b-48bc-9683-816dae74ac45",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "starry-mapping-hearth",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FdmwC5JJD7oaDtpbrSr86T",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1456,
      "cache_read_input_tokens": 24127,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1456,
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

_source line 9 · 2026-05-19T03:00:04.355Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01UqFAWYyppKMiZYydXyTqvC`</summary>

```json
{
  "query": "ACL negative results accepted main track 2024 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "76495545-d247-4daf-b481-49cac6ff7c23",
  "isSidechain": true,
  "agentId": "a2210751531ccd330",
  "requestId": "req_011CbBBQgGjgDccFiuGsNVZR",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "11c0b238-ef09-4179-a123-f2d642e7b3b8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/.claude/sessions/reviewer_e7517921",
  "sessionId": "5a74afe6-047b-48bc-9683-816dae74ac45",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "starry-mapping-hearth",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FdmwC5JJD7oaDtpbrSr86T",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1456,
      "cache_read_input_tokens": 24127,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1456,
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

_source line 10 · 2026-05-19T03:00:04.621Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01MtGYzHUCbdGRHMs1zskEtT`</summary>

```json
{
  "query": "negative result paper NLP conference contribution pattern publishable criteria"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "11c0b238-ef09-4179-a123-f2d642e7b3b8",
  "isSidechain": true,
  "agentId": "a2210751531ccd330",
  "requestId": "req_011CbBBQgGjgDccFiuGsNVZR",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "c294c3ce-afd5-447b-a93d-91264fdd211a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/.claude/sessions/reviewer_e7517921",
  "sessionId": "5a74afe6-047b-48bc-9683-816dae74ac45",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "starry-mapping-hearth",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FdmwC5JJD7oaDtpbrSr86T",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1456,
      "cache_read_input_tokens": 24127,
      "output_tokens": 228,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1456
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 228,
          "cache_read_input_tokens": 24127,
          "cache_creation_input_tokens": 1456,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1456,
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

_source line 11 · 2026-05-19T03:00:10.596Z_

<details><summary>↩ Tool result · `toolu_013vkGK88y3kf67BNheYRUZH`</summary>

```text
Web search results for query: "EMNLP "Insights from Negative Results" workshop 2024 2025"

Links: [{"title":"Workshop on Insights from Negative Results in NLP | ACL Member Portal","url":"https://www.aclweb.org/portal/content/workshop-insights-negative-results-nlp-0"},{"title":"CFP | Insights 2024","url":"https://insights-workshop.github.io/2021/cfp/"},{"title":"Insights 2024 | Workshop on Insights from Negative Results in NLP","url":"https://insights-workshop.github.io/"},{"title":"Insights 2024 : Fifth Workshop on Insights from Negative Results in NLP","url":"http://wikicfp.com/cfp/servlet/event.showcfp?eventid=178569"},{"title":"Workshop on Insights from Negative Results in NLP | Insights 2024","url":"https://insights-workshop.github.io/index"},{"title":"INSIGHTS FROM NEGATIVE RESULTS IN NLP. WORKSHOP. 5TH 2025. (INSIGHTS 2025) - proceedings.com","url":"https://www.proceedings.com/80148.html"},{"title":"Insights 2023 : The Forth Workshop on Insights from Negative Results in NLP","url":"http://www.wikicfp.com/cfp/servlet/event.showcfp?eventid=171081&copyownerid=320"},{"title":"Workshop on Insights from Negative Results in NLP (2024) - ACL Anthology","url":"https://aclanthology.org/events/insights-2024/"},{"title":"Call For Papers: The Second Workshop on Insights from Negative Results (EMNLP 2021) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/call-papers-second-workshop-insights-negative-results-emnlp-2021-0"}]

Based on the search results, here's what I found about the EMNLP "Insights from Negative Results" workshop:

## Insights 2025

The workshop is being held with NAACL 2025 in Albuquerque, New Mexico, with a submission deadline of January 30, 2025. The contact email is insights-workshop-organizers@googlegroups.com and the workshop website is https://insights-workshop.github.io/.

## Insights 2024

The Fifth Workshop on Insights from Negative Results in NLP was held in 2024, which published 20 papers.

## General Information About the Workshop

Publication of negative results is difficult in most fields, but in NLP the problem is exacerbated by the near-universal focus on improvements in benchmarks. The workshop's goal is to provide both a publication venue and an opportunity to discuss the most urgent methodological issues, and to think about where the field is going.

## Upcoming Workshop

The next instance of the workshop will be in Budapest, Hungary, October 22-29, 2026 (co-located with EMNLP).


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "76495545-d247-4daf-b481-49cac6ff7c23",
  "isSidechain": true,
  "promptId": "d62aafe3-d75b-460d-a9bb-1b0f23cd5965",
  "agentId": "a2210751531ccd330",
  "type": "user",
  "uuid": "c3886d39-3659-481f-aa4b-002722344279",
  "sourceToolAssistantUUID": "76495545-d247-4daf-b481-49cac6ff7c23",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/.claude/sessions/reviewer_e7517921",
  "sessionId": "5a74afe6-047b-48bc-9683-816dae74ac45",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "starry-mapping-hearth"
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-19T03:00:10.668Z_

<details><summary>↩ Tool result · `toolu_01UqFAWYyppKMiZYydXyTqvC`</summary>

```text
Web search results for query: "ACL negative results accepted main track 2024 2025"

Links: [{"title":"Industry Track - ACL 2025","url":"https://2025.aclweb.org/calls/industry_track/"},{"title":"HalluCitation Matters: Revealing the Impact of Hallucinated References with 300 Hallucinated Papers in ACL Conferences","url":"https://arxiv.org/pdf/2601.18724"},{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"Has ACL Lost Its Crown? A Decade-Long Quantitative Analysis of Scale and Impact Across Leading AI Conferences","url":"https://arxiv.org/pdf/2512.04448"},{"title":"aclrollingreview/cfp.md at main · acl-org/aclrollingreview","url":"https://github.com/acl-org/aclrollingreview/blob/main/cfp.md"},{"title":"ACL 2024 Statistics - Paper Copilot","url":"https://papercopilot.com/statistics/acl-statistics/acl-2024-statistics/"}]

I performed a web search for "ACL negative results accepted main track 2024 2025" and found some relevant information, though the results don't directly address the specific query about negative results being accepted in the main track.

The search results provide some context about ACL conferences and papers, including:

- Information about ACL's growth, with the main conference growing from 692 long-paper submissions and 173 acceptances in 2015 to 4,407 submissions and 865 acceptances in 2024
- Analysis of papers published at ACL, NAACL, and EMNLP in 2024 and 2025, with nearly 300 papers containing hallucinated citations
- Details about ACL Rolling Review (ARR) policies and submission requirements

However, the search results don't contain specific information about whether negative results papers were officially accepted for the ACL main track in 2024 or 2025. To find more targeted information about this policy, you might want to check the official ACL 2025 call for papers or main conference submission guidelines directly.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "11c0b238-ef09-4179-a123-f2d642e7b3b8",
  "isSidechain": true,
  "promptId": "d62aafe3-d75b-460d-a9bb-1b0f23cd5965",
  "agentId": "a2210751531ccd330",
  "type": "user",
  "uuid": "87e75b20-b758-4d61-aa6b-856755c57c4c",
  "sourceToolAssistantUUID": "11c0b238-ef09-4179-a123-f2d642e7b3b8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/.claude/sessions/reviewer_e7517921",
  "sessionId": "5a74afe6-047b-48bc-9683-816dae74ac45",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "starry-mapping-hearth"
}
```

</details>

---

### Tool result

_source line 13 · 2026-05-19T03:00:13.194Z_

<details><summary>↩ Tool result · `toolu_01MtGYzHUCbdGRHMs1zskEtT`</summary>

```text
Web search results for query: "negative result paper NLP conference contribution pattern publishable criteria"

Links: [{"title":"Position: Embracing Negative Results in Machine Learning","url":"https://arxiv.org/html/2406.03980v1"},{"title":"The Third Workshop on Insights from Negative Results in NLP | ACL Member Portal","url":"https://aclweb.org/portal/content/third-workshop-insights-negative-results-nlp"},{"title":"Workshop on Insights from Negative Results in NLP | ACL Member Portal","url":"https://www.aclweb.org/portal/content/workshop-insights-negative-results-nlp"},{"title":"The Third Workshop on Insights from Negative Results in NLP | ACL Member Portal","url":"https://www.aclweb.org/portal/content/third-workshop-insights-negative-results-nlp-0"},{"title":"CFP | Insights 2024","url":"https://insights-workshop.github.io/2021/cfp/"},{"title":"CALL FOR PAPERS – ACL Rolling Review","url":"http://aclrollingreview.org/cfp"},{"title":"Workshop on Insights from Negative Results | ACL Member Portal","url":"https://www.aclweb.org/portal/content/workshop-insights-negative-results"}]

Based on the search results, here's what I found about negative result papers in NLP conferences and their publishable criteria:

## Key Publishable Criteria for Negative Results Papers

A successful negative results paper would contribute one of the following: experiments on stability issues due to hardware or random initializations; ablation studies showing components' contributions differ from reported; datasets or probing tasks showing previous approaches don't generalize; extensions of datasets revealing spurious statistical factors or annotation artifacts; the respective contributions of pre-training vs fine-tuning; cross-lingual studies showing techniques only work for certain languages; or broadly applicable recommendations for training/fine-tuning.

## Definition of Negative Results

A negative results paper might report on non-reproducibility or non-generalizability of previously published results, their misattribution, or present an idea that seemed well-justified but didn't work.

## Challenges in Publishing

Publishing negative results is not easy, partly because the author has the burden of proof that something truly does not work, rather than is caused by a bug.

## NLP Community Response

Publication of negative results is difficult in NLP due to focus on benchmark improvements, which discourages hypothesis-driven research and turns model development into art rather than science, while increasing time and carbon emissions as researchers cannot learn what has already been tried and failed.

The NLP research community has established dedicated workshops, such as "Insights from Negative Results in NLP," specifically to address the publication gap for this important type of research.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c294c3ce-afd5-447b-a93d-91264fdd211a",
  "isSidechain": true,
  "promptId": "d62aafe3-d75b-460d-a9bb-1b0f23cd5965",
  "agentId": "a2210751531ccd330",
  "type": "user",
  "uuid": "d62c1b98-1dab-4fc1-bbdb-c7e8d010f4f8",
  "sourceToolAssistantUUID": "c294c3ce-afd5-447b-a93d-91264fdd211a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/.claude/sessions/reviewer_e7517921",
  "sessionId": "5a74afe6-047b-48bc-9683-816dae74ac45",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "starry-mapping-hearth"
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-19T03:00:15.649Z_

<details><summary>↩ Tool result · `toolu_01RE8geNmdtxod64WBkQmo16`</summary>

```text
Web search results for query: "negative result paper EMNLP 2024 2025 accepted main track"

Links: [{"title":"Call for Main Conference Papers - EMNLP 2025","url":"https://2025.emnlp.org/calls/main_conference_papers/"},{"title":"HalluCitation Matters: Revealing the Impact of Hallucinated References with 300 Hallucinated Papers in ACL Conferences","url":"https://arxiv.org/pdf/2601.18724"},{"title":"EMNLP 2025 Decisions: Community Insights and the Controversial Desk Rejections | CSPaper Forum","url":"https://forum.cspaper.org/topic/131/emnlp-2025-decisions-community-insights-and-the-controversial-desk-rejections"},{"title":"Renewed call for action: Highlight negative results to improve science","url":"https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11261298/"},{"title":"EMNLP 2024 Statistics - Paper Copilot","url":"https://papercopilot.com/statistics/emnlp-statistics/emnlp-2024-statistics/"},{"title":"EMNLP 2024 Accepted Paper List - Paper Copilot","url":"https://papercopilot.com/paper-list/emnlp-paper-list/emnlp-2024-paper-list/"}]

Based on the search results, I found information about negative result papers at EMNLP:

EMNLP 2025 has a goal of curating a diverse technical program—in addition to traditional research results, papers may contribute negative findings, survey an area, announce the creation of a new resource, argue a position, report novel linguistic insights derived using existing computational techniques, and reproduce, or fail to reproduce, previous results.

This shows that EMNLP explicitly welcomes negative result papers as part of its main conference track. However, the search results did not return a specific list of negative result papers that were actually accepted to the EMNLP 2024 or 2025 main conference tracks. The results indicate that EMNLP 2025 had a Main acceptance rate of just over 22%, but they don't specify which individual papers with negative findings were accepted.

If you're looking for specific accepted negative result papers from these conferences, you may want to check the official EMNLP conference websites directly or search paper databases like Paper Copilot or OpenReview for papers tagged with negative findings or null results.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "7d758c74-ac93-4ff8-b916-aeb4c569dc6a",
  "isSidechain": true,
  "promptId": "d62aafe3-d75b-460d-a9bb-1b0f23cd5965",
  "agentId": "a2210751531ccd330",
  "type": "user",
  "uuid": "d109fc2f-fa18-49aa-90e0-2df4728f80b6",
  "sourceToolAssistantUUID": "7d758c74-ac93-4ff8-b916-aeb4c569dc6a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/.claude/sessions/reviewer_e7517921",
  "sessionId": "5a74afe6-047b-48bc-9683-816dae74ac45",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "starry-mapping-hearth"
}
```

</details>

---

### Assistant

_source line 15 · 2026-05-19T03:00:18.251Z_

Good initial results. Let me dig deeper into specific examples and the ICML position paper on negative results.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d109fc2f-fa18-49aa-90e0-2df4728f80b6",
  "isSidechain": true,
  "agentId": "a2210751531ccd330",
  "requestId": "req_011CbBBRnV4hHFNs67mnQhbk",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "f6d24c7f-4840-4389-8cee-47d95736d7d4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/.claude/sessions/reviewer_e7517921",
  "sessionId": "5a74afe6-047b-48bc-9683-816dae74ac45",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "starry-mapping-hearth",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DaFyWnhEwyfWg8TF7Jc6KJ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2039,
      "cache_creation_input_tokens": 885,
      "cache_read_input_tokens": 25583,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 885,
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

_source line 16 · 2026-05-19T03:00:18.733Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Bv4qvKqGgkKK2x7sddSUCJ`</summary>

```json
{
  "query": "arxiv \"Embracing Negative Results in Machine Learning\" ICML 2024 position paper criteria"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f6d24c7f-4840-4389-8cee-47d95736d7d4",
  "isSidechain": true,
  "agentId": "a2210751531ccd330",
  "requestId": "req_011CbBBRnV4hHFNs67mnQhbk",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "b292e93a-dff5-4585-814d-dcdefe59c588",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/.claude/sessions/reviewer_e7517921",
  "sessionId": "5a74afe6-047b-48bc-9683-816dae74ac45",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "starry-mapping-hearth",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DaFyWnhEwyfWg8TF7Jc6KJ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2039,
      "cache_creation_input_tokens": 885,
      "cache_read_input_tokens": 25583,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 885,
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

_source line 17 · 2026-05-19T03:00:19.666Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01FHfV3AUn7B1zHajLxjAG89`</summary>

```json
{
  "query": "EMNLP 2024 findings \"negative result\" \"does not\" \"fail to\" accepted paper examples"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b292e93a-dff5-4585-814d-dcdefe59c588",
  "isSidechain": true,
  "agentId": "a2210751531ccd330",
  "requestId": "req_011CbBBRnV4hHFNs67mnQhbk",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "c17436b0-a437-41a5-b80d-a65a56d0813f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/.claude/sessions/reviewer_e7517921",
  "sessionId": "5a74afe6-047b-48bc-9683-816dae74ac45",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "starry-mapping-hearth",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DaFyWnhEwyfWg8TF7Jc6KJ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2039,
      "cache_creation_input_tokens": 885,
      "cache_read_input_tokens": 25583,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 885,
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

_source line 18 · 2026-05-19T03:00:20.135Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_012X4VtJVSqHGWuQRJaUKi4J`</summary>

```json
{
  "query": "insights workshop negative results NLP 2024 accepted papers ACL Anthology"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c17436b0-a437-41a5-b80d-a65a56d0813f",
  "isSidechain": true,
  "agentId": "a2210751531ccd330",
  "requestId": "req_011CbBBRnV4hHFNs67mnQhbk",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "dc88a720-4398-49cd-8ca2-c03e0f7abfe0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/.claude/sessions/reviewer_e7517921",
  "sessionId": "5a74afe6-047b-48bc-9683-816dae74ac45",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "starry-mapping-hearth",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DaFyWnhEwyfWg8TF7Jc6KJ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2039,
      "cache_creation_input_tokens": 885,
      "cache_read_input_tokens": 25583,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 885,
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

_source line 19 · 2026-05-19T03:00:20.718Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01C7E5BpXZpX46rQxgVTYGqJ`</summary>

```json
{
  "query": "NAACL 2024 2025 negative result paper accepted reproducibility failure"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "dc88a720-4398-49cd-8ca2-c03e0f7abfe0",
  "isSidechain": true,
  "agentId": "a2210751531ccd330",
  "requestId": "req_011CbBBRnV4hHFNs67mnQhbk",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "b0805f02-7e2f-45a3-af6b-7897e86c8051",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/.claude/sessions/reviewer_e7517921",
  "sessionId": "5a74afe6-047b-48bc-9683-816dae74ac45",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "starry-mapping-hearth",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DaFyWnhEwyfWg8TF7Jc6KJ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2039,
      "cache_creation_input_tokens": 885,
      "cache_read_input_tokens": 25583,
      "output_tokens": 258,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 885
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2039,
          "output_tokens": 258,
          "cache_read_input_tokens": 25583,
          "cache_creation_input_tokens": 885,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 885,
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

_source line 20 · 2026-05-19T03:00:24.379Z_

<details><summary>↩ Tool result · `toolu_01Bv4qvKqGgkKK2x7sddSUCJ`</summary>

```text
Web search results for query: "arxiv "Embracing Negative Results in Machine Learning" ICML 2024 position paper criteria"

Links: [{"title":"[ICML 2024] Position: Embracing Negative Results in Machine Learning - YouTube","url":"https://www.youtube.com/watch?v=JDP6cXWmChI"},{"title":"Position: Embracing Negative Results in Machine Learning","url":"https://arxiv.org/pdf/2406.03980"},{"title":"[2406.03980] Position: Embracing Negative Results in Machine Learning","url":"https://arxiv.org/abs/2406.03980"},{"title":"ICML Poster Position: Embracing Negative Results in Machine Learning","url":"https://icml.cc/virtual/2024/poster/35063"},{"title":"Position: Embracing Negative Results in Machine Learning | AI Research Paper Details","url":"https://www.aimodels.fyi/papers/arxiv/position-embracing-negative-results-machine-learning"},{"title":"Position: Machine Learning Conferences Should Establish a “Refutations and Critiques” Track","url":"https://arxiv.org/html/2506.19882v3"},{"title":"ICML 2024 Call for Papers","url":"https://icml.cc/Conferences/2024/CallForPapers"},{"title":"Position: Machine Learning Conferences Should Establish a \"Refutations and Critiques\" Track","url":"https://arxiv.org/pdf/2506.19882"},{"title":"Machine Learning May 2024","url":"https://arxiv.org/list/cs.LG/2024-05?skip=300&show=100"}]

I found the paper! Based on the search results, here's what I can tell you about the ICML 2024 position paper:

**Paper Title:** "Position: Embracing Negative Results in Machine Learning"

**arXiv ID:** 2406.03980

**Main Argument:** The paper argues that predictive performance alone is not a good indicator for the worth of a publication. Using predictive performance as the sole metric fosters problems like inefficiencies in the machine learning research community and sets wrong incentives for researchers, and the authors put out a call for the publication of "negative" results.

**Key Contributions:** The paper presents the advantages of publishing negative results and provides concrete measures for the community to move towards a paradigm where their publication is normalized.

The paper was posted to arXiv on June 6, 2024, and presented as a position paper at ICML 2024. You can access the full PDF at https://arxiv.org/pdf/2406.03980.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "b292e93a-dff5-4585-814d-dcdefe59c588",
  "isSidechain": true,
  "promptId": "d62aafe3-d75b-460d-a9bb-1b0f23cd5965",
  "agentId": "a2210751531ccd330",
  "type": "user",
  "uuid": "7d0b84d4-5717-44c2-9090-c221fbf6f90e",
  "sourceToolAssistantUUID": "b292e93a-dff5-4585-814d-dcdefe59c588",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/.claude/sessions/reviewer_e7517921",
  "sessionId": "5a74afe6-047b-48bc-9683-816dae74ac45",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "starry-mapping-hearth"
}
```

</details>

---

### Tool result

_source line 21 · 2026-05-19T03:00:25.396Z_

<details><summary>↩ Tool result · `toolu_012X4VtJVSqHGWuQRJaUKi4J`</summary>

```text
Web search results for query: "insights workshop negative results NLP 2024 accepted papers ACL Anthology"

Links: [{"title":"Accepted papers | Insights 2024","url":"https://insights-workshop.github.io/2025/accepted/"},{"title":"Workshop on Insights from Negative Results in NLP (2024) - ACL Anthology","url":"https://aclanthology.org/events/insights-2024/"},{"title":"Other Workshops and Events - ACL Anthology","url":"https://aclanthology.org/venues/ws/"},{"title":"Workshop on Insights from Negative Results in NLP | ACL Member Portal","url":"https://www.aclweb.org/portal/content/workshop-insights-negative-results-nlp-0"},{"title":"Workshop on Insights from Negative Results in NLP - ACL Anthology","url":"https://aclanthology.org/venues/insights/"},{"title":"Workshop on Insights from Negative Results in NLP (2023) - ACL Anthology","url":"https://aclanthology.org/events/insights-2023/"},{"title":"Proceedings of the Fourth Workshop on Insights from Negative Results in NLP - ACL Anthology","url":"https://aclanthology.org/volumes/2023.insights-1/"}]

I found the information about the Workshop on Insights from Negative Results in NLP! Here are the key findings:

The Fifth Workshop on Insights from Negative Results in NLP had 20 accepted papers, and these papers are available on the ACL Anthology. 

The workshop is held in Albuquerque, New Mexico in May 2025, co-located with NAACL.

The search results also show information about the 2023 edition (Fourth Workshop), which had 15 papers. One notable accepted paper from that edition was on reproducibility issues in human evaluations in NLP.

For a complete list of all 20 accepted papers from the 2024 workshop, you can visit the ACL Anthology directly at the workshop's page: https://aclanthology.org/events/insights-2024/


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "dc88a720-4398-49cd-8ca2-c03e0f7abfe0",
  "isSidechain": true,
  "promptId": "d62aafe3-d75b-460d-a9bb-1b0f23cd5965",
  "agentId": "a2210751531ccd330",
  "type": "user",
  "uuid": "10d06ecb-0696-4a56-8007-7a6158480341",
  "sourceToolAssistantUUID": "dc88a720-4398-49cd-8ca2-c03e0f7abfe0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/.claude/sessions/reviewer_e7517921",
  "sessionId": "5a74afe6-047b-48bc-9683-816dae74ac45",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "starry-mapping-hearth"
}
```

</details>

---

### Tool result

_source line 22 · 2026-05-19T03:00:25.446Z_

<details><summary>↩ Tool result · `toolu_01C7E5BpXZpX46rQxgVTYGqJ`</summary>

```text
Web search results for query: "NAACL 2024 2025 negative result paper accepted reproducibility failure"

Links: [{"title":"Second Call for Main Conference Papers - NAACL-HLT 2025","url":"https://2025.naacl.org/calls/papers/"},{"title":"Second Call for Main Conference Papers - NAACL-HLT 2024","url":"https://2024.naacl.org/calls/papers/"},{"title":"[NAACL 2025] Second Call for Main Conference Papers | ACL Member Portal","url":"https://www.aclweb.org/portal/content/naacl-2025-second-call-main-conference-papers"},{"title":"First Call for Papers: NAACL 2025 Main Conference | ACL Member Portal","url":"https://www.aclweb.org/portal/content/naacl-first-call-main-conference-papers"},{"title":"Accepted Industry Track Paper - NAACL-HLT 2024","url":"https://2024.naacl.org/program/accepted_papers_industry/"},{"title":"Accepted Papers - NAACL-HLT 2024","url":"https://2024.naacl.org/program/accepted_papers/"},{"title":"HalluCitation Matters: Revealing the Impact of Hallucinated References with 300 Hallucinated Papers in ACL Conferences","url":"https://arxiv.org/pdf/2601.18724"},{"title":"NAACL 2024 Accepted Paper List - Paper Copilot","url":"https://papercopilot.com/paper-list/naacl-paper-list/naacl-2024-paper-list/"},{"title":"CALL FOR PAPERS – ACL Rolling Review","url":"http://aclrollingreview.org/cfp"}]

Based on the search results, I found information about how NAACL accepts papers on these topics:

NAACL 2024 and 2025 have goals of diverse technical programs where papers may contribute negative findings and reproduce, or fail to reproduce, previous results. This indicates that both NAACL 2024 and NAACL 2025 officially accept papers reporting negative results and reproducibility failures as valid contributions to the conference.

However, the search results don't contain specific information about particular papers accepted at NAACL 2024 or 2025 that reported negative results or reproducibility failures. The results show general conference policies and accepted paper listings, but not details about individual papers focused on reproducibility issues or failed replications.

If you're looking for specific papers on these topics accepted at NAACL 2024 or 2025, you might want to search the conference proceedings directly or look for papers with keywords like "reproducibility," "negative results," or "failure to replicate."


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "b0805f02-7e2f-45a3-af6b-7897e86c8051",
  "isSidechain": true,
  "promptId": "d62aafe3-d75b-460d-a9bb-1b0f23cd5965",
  "agentId": "a2210751531ccd330",
  "type": "user",
  "uuid": "eef0c291-9485-43cb-a156-6e77ac1daa38",
  "sourceToolAssistantUUID": "b0805f02-7e2f-45a3-af6b-7897e86c8051",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/.claude/sessions/reviewer_e7517921",
  "sessionId": "5a74afe6-047b-48bc-9683-816dae74ac45",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "starry-mapping-hearth"
}
```

</details>

---

### Tool result

_source line 23 · 2026-05-19T03:00:33.997Z_

<details><summary>↩ Tool result · `toolu_01FHfV3AUn7B1zHajLxjAG89`</summary>

```text
Web search results for query: "EMNLP 2024 findings "negative result" "does not" "fail to" accepted paper examples"

Links: [{"title":"Insights 2024 | Workshop on Insights from Negative Results in NLP","url":"https://insights-workshop.github.io/"},{"title":"Findings - EMNLP 2024","url":"https://2024.emnlp.org/program/accepted_findings/"},{"title":"CFP | Insights 2024","url":"https://insights-workshop.github.io/2021/cfp/"},{"title":"EMNLP 2024 Statistics - Paper Copilot","url":"https://papercopilot.com/statistics/emnlp-statistics/emnlp-2024-statistics/"},{"title":"EMNLP 2024 Accepted Paper List - Paper Copilot","url":"https://papercopilot.com/paper-list/emnlp-paper-list/emnlp-2024-paper-list/"},{"title":"HalluCitation Matters: Revealing the Impact of Hallucinated References with 300 Hallucinated Papers in ACL Conferences","url":"https://arxiv.org/pdf/2601.18724"}]

Let me search more specifically for EMNLP 2024 findings papers that focus on negative results:

Links: [{"title":"EMNLP.2024 - Findings | Cool Papers - Immersive Paper Discovery","url":"https://papers.cool/venue/EMNLP.2024?group=Findings"},{"title":"EMNLP 2024 The 2024 Conference on Empirical Methods in Natural","url":"https://aclanthology.org/2024.findings-emnlp.0.pdf"},{"title":"Findings - EMNLP 2024","url":"https://2024.emnlp.org/program/accepted_findings/"},{"title":"EMNLP (Findings) 2024: Miami, FL, USA","url":"https://dblp.org/db/conf/emnlp/emnlp2024f.html"},{"title":"Findings of the Association for Computational Linguistics: EMNLP 2024 - ACL Anthology","url":"https://aclanthology.org/volumes/2024.findings-emnlp/"},{"title":"LLMs Have Made Failure Worth Publishing","url":"https://arxiv.org/pdf/2604.06236"}]

Based on the web search results, I found some examples of EMNLP 2024 Findings papers that present negative or disappointing results:

## Examples of EMNLP 2024 Findings Papers with Negative Results

1. **"Are LLMs Good Annotators for Discourse-level Event Relation Extraction?"** by Kangda Wei, Aayush Gautam, and Ruihong Huang
   - The study reveals a notable underperformance of LLMs compared to the baseline established through supervised learning. Additionally, LLMs have several weaknesses when applied for extracting event relations, including a tendency to fabricate event mentions, and failures to capture transitivity rules among relations, detect long distance relations, or comprehend contexts with dense event mentions.

2. **"SEAVER: Attention Reallocation for Mitigating Distractions in Language Models for Conditional Semantic Textual Similarity"** by Baixuan Li, Yunlong Fan, and Zhiqiang Gao
   - Language models employing cross-encoding demonstrate satisfactory performance in STS, yet their effectiveness significantly diminishes in C-STS.

3. **"Insights into LLM Long-Context Failures: When Transformers Know but Don't Tell"** by Muhan Gao and others
   - This paper directly examines failure modes in LLMs with long contexts, as evidenced by the paper title itself.

In total, 1271 papers were accepted to the Main Conference and 1029 papers accepted to Findings, with the acceptance rate for Findings papers being 16.9%. These negative result papers demonstrate that EMNLP accepts papers highlighting limitations and failures of existing approaches.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c17436b0-a437-41a5-b80d-a65a56d0813f",
  "isSidechain": true,
  "promptId": "d62aafe3-d75b-460d-a9bb-1b0f23cd5965",
  "agentId": "a2210751531ccd330",
  "type": "user",
  "uuid": "1f33a052-3699-4c08-8f1e-0f700dcdfd0f",
  "sourceToolAssistantUUID": "c17436b0-a437-41a5-b80d-a65a56d0813f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/.claude/sessions/reviewer_e7517921",
  "sessionId": "5a74afe6-047b-48bc-9683-816dae74ac45",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "starry-mapping-hearth"
}
```

</details>

---

### Assistant

_source line 24 · 2026-05-19T03:00:37.011Z_

Let me now get more specific examples and dig into the ACL Anthology for the Insights workshop papers, plus the ICML position paper details.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1f33a052-3699-4c08-8f1e-0f700dcdfd0f",
  "isSidechain": true,
  "agentId": "a2210751531ccd330",
  "requestId": "req_011CbBBT8z8mxNbLFJ8tqRTE",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "d8836e15-4f90-4010-a005-d4ff31687d4d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/.claude/sessions/reviewer_e7517921",
  "sessionId": "5a74afe6-047b-48bc-9683-816dae74ac45",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "starry-mapping-hearth",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AdLJiLDAtnY17urLJSamr2",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1254,
      "cache_creation_input_tokens": 4115,
      "cache_read_input_tokens": 26468,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4115,
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

_source line 25 · 2026-05-19T03:00:37.496Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_015sQ5EsPGTBidWJrdUirkZD`</summary>

```json
{
  "query": "site:aclanthology.org insights-2024 negative results workshop papers list"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d8836e15-4f90-4010-a005-d4ff31687d4d",
  "isSidechain": true,
  "agentId": "a2210751531ccd330",
  "requestId": "req_011CbBBT8z8mxNbLFJ8tqRTE",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "d98d5839-6b8e-4c9c-bb9b-bbe681c3f241",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/.claude/sessions/reviewer_e7517921",
  "sessionId": "5a74afe6-047b-48bc-9683-816dae74ac45",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "starry-mapping-hearth",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AdLJiLDAtnY17urLJSamr2",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1254,
      "cache_creation_input_tokens": 4115,
      "cache_read_input_tokens": 26468,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4115,
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

_source line 26 · 2026-05-19T03:00:38.438Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01CsheruyMiv2CCFgD5kxvg5`</summary>

```json
{
  "query": "\"LLMs Have Made Failure Worth Publishing\" arxiv 2024 negative results NLP"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d98d5839-6b8e-4c9c-bb9b-bbe681c3f241",
  "isSidechain": true,
  "agentId": "a2210751531ccd330",
  "requestId": "req_011CbBBT8z8mxNbLFJ8tqRTE",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "0ef89e08-e72b-461b-87d5-1193a8fc1050",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/.claude/sessions/reviewer_e7517921",
  "sessionId": "5a74afe6-047b-48bc-9683-816dae74ac45",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "starry-mapping-hearth",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AdLJiLDAtnY17urLJSamr2",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1254,
      "cache_creation_input_tokens": 4115,
      "cache_read_input_tokens": 26468,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4115,
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

_source line 27 · 2026-05-19T03:00:39.460Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01DJXCB9R4nmq3tweFjwsuwD`</summary>

```json
{
  "query": "ACL Rolling Review call for papers \"negative findings\" \"reproduce or fail to reproduce\" contribution types"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0ef89e08-e72b-461b-87d5-1193a8fc1050",
  "isSidechain": true,
  "agentId": "a2210751531ccd330",
  "requestId": "req_011CbBBT8z8mxNbLFJ8tqRTE",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "0bb5c1ec-84d7-4b9a-aa1b-7f4ac46554a1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/.claude/sessions/reviewer_e7517921",
  "sessionId": "5a74afe6-047b-48bc-9683-816dae74ac45",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "starry-mapping-hearth",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AdLJiLDAtnY17urLJSamr2",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1254,
      "cache_creation_input_tokens": 4115,
      "cache_read_input_tokens": 26468,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4115,
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

_source line 28 · 2026-05-19T03:00:39.835Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01MiYsLLCLWZTk97vmZYMWdZ`</summary>

```json
{
  "query": "EMNLP 2024 main conference \"negative\" \"does not improve\" \"surprising\" accepted paper title"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0bb5c1ec-84d7-4b9a-aa1b-7f4ac46554a1",
  "isSidechain": true,
  "agentId": "a2210751531ccd330",
  "requestId": "req_011CbBBT8z8mxNbLFJ8tqRTE",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "58ffad99-2ab5-4759-9e80-45a741e34d38",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/.claude/sessions/reviewer_e7517921",
  "sessionId": "5a74afe6-047b-48bc-9683-816dae74ac45",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "starry-mapping-hearth",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AdLJiLDAtnY17urLJSamr2",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1254,
      "cache_creation_input_tokens": 4115,
      "cache_read_input_tokens": 26468,
      "output_tokens": 269,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 4115
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1254,
          "output_tokens": 269,
          "cache_read_input_tokens": 26468,
          "cache_creation_input_tokens": 4115,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 4115,
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

_source line 29 · 2026-05-19T03:00:43.229Z_

<details><summary>↩ Tool result · `toolu_015sQ5EsPGTBidWJrdUirkZD`</summary>

```text
Web search results for query: "site:aclanthology.org insights-2024 negative results workshop papers list"

Links: [{"title":"Insights 2024 The 5th Workshop on Insights from Negative Results in NLP","url":"https://aclanthology.org/2024.insights-1.0.pdf"},{"title":"Workshop on Insights from Negative Results in NLP (2024) - ACL Anthology","url":"https://aclanthology.org/events/insights-2024/"},{"title":"Other Workshops and Events (2024) - ACL Anthology","url":"https://aclanthology.org/events/ws-2024/"},{"title":"Aclanthology","url":"https://aclanthology.org/2024.insights-1.16.pdf"},{"title":"Other Workshops and Events - ACL Anthology","url":"https://aclanthology.org/venues/ws/"},{"title":"2024 Annual Conference of the North American Chapter of the Association for Computational Linguistics - ACL Anthology","url":"https://aclanthology.org/events/naacl-2024/"},{"title":"Workshop on Insights from Negative Results in NLP (2023) - ACL Anthology","url":"https://aclanthology.org/events/insights-2023/"}]

Based on my search results, I found information about the Insights 2024 workshop. The Fifth Workshop on Insights from Negative Results in NLP included 20 papers, and 19 short papers were accepted at a 57.5% acceptance rate.

The workshop proceedings are available on the ACL Anthology at https://aclanthology.org/events/insights-2024/. This page contains the complete list of papers presented at the workshop, including titles, authors, and abstracts for all 20 papers. You can access the full proceedings and individual paper PDFs directly from that URL.

Some example papers from the workshop include:
- "MoSECroT: Model Stitching with Static Word Embeddings for Crosslingual Zero-shot Transfer" by Haotian Ye et al.
- "The Paradox of Preference: A Study on LLM Alignment Algorithms" 
- "What explains the success of cross-modal fine-tuning with ORCA?"

To view the complete annotated list of all papers with abstracts, you can visit the workshop's event page directly on the ACL Anthology website.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d98d5839-6b8e-4c9c-bb9b-bbe681c3f241",
  "isSidechain": true,
  "promptId": "d62aafe3-d75b-460d-a9bb-1b0f23cd5965",
  "agentId": "a2210751531ccd330",
  "type": "user",
  "uuid": "bd713254-c331-4906-8e65-acb5613f0145",
  "sourceToolAssistantUUID": "d98d5839-6b8e-4c9c-bb9b-bbe681c3f241",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/.claude/sessions/reviewer_e7517921",
  "sessionId": "5a74afe6-047b-48bc-9683-816dae74ac45",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "starry-mapping-hearth"
}
```

</details>

---

### Tool result

_source line 30 · 2026-05-19T03:00:46.180Z_

<details><summary>↩ Tool result · `toolu_01CsheruyMiv2CCFgD5kxvg5`</summary>

```text
Web search results for query: ""LLMs Have Made Failure Worth Publishing" arxiv 2024 negative results NLP"

Links: [{"title":"LLMs Have Made Failure Worth Publishing","url":"https://arxiv.org/pdf/2604.06236"},{"title":"LLMs Have Made Failure Worth Publishing","url":"https://arxiv.org/html/2604.06236v1"},{"title":"Large Language Models for Supporting Clear Writing and Detecting Spin in Randomized Controlled Trials in Oncology: Comparative Analysis of GPT Models and Prompts","url":"https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12823016/"},{"title":"Why Does the LLM Stop Computing: An Empirical Study of User-Reported Failures in Open-Source LLMs","url":"https://arxiv.org/html/2601.13655v1"},{"title":"How much do LLMs learn from negative examples?","url":"https://arxiv.org/pdf/2503.14391"}]

Based on the search results, I found the paper you're looking for. Here's what I found:

**"LLMs Have Made Failure Worth Publishing"** is a preprint by Sungmin Lee from April 9, 2026.

The paper's central argument is that the systematic filtering out of negative results in scientific publishing has become an urgent problem in the era of large language models, which inherit the positive bias of the literature they are trained on, face an impending shortage of high-quality training data, and are increasingly deployed as both research tools and peer reviewers.

Key findings include:

1. **The extent of positive bias**: Fanelli analyzed over 4,600 papers published between 1990 and 2007 and found that the proportion reporting positive results exceeded 80% after 1999, peaking at 88.6% in 2005.

2. **Impact on LLM training**: An LLM trained predominantly on positive-result literature inherits a distorted model of science in which most experiments succeed, and this positive skew may systematically miscalibrate the model's judgment about which research directions are viable.

3. **The paper's scope**: The authors analyze three ways in which LLMs have changed the value of failure data and show that the systematic absence of such data degrades their utility as research tools, training data consumers, and peer reviewers alike.

The full paper is available on arXiv at https://arxiv.org/pdf/2604.06236


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "0ef89e08-e72b-461b-87d5-1193a8fc1050",
  "isSidechain": true,
  "promptId": "d62aafe3-d75b-460d-a9bb-1b0f23cd5965",
  "agentId": "a2210751531ccd330",
  "type": "user",
  "uuid": "2c52a124-5465-4290-a72e-3a666f47289f",
  "sourceToolAssistantUUID": "0ef89e08-e72b-461b-87d5-1193a8fc1050",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/.claude/sessions/reviewer_e7517921",
  "sessionId": "5a74afe6-047b-48bc-9683-816dae74ac45",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "starry-mapping-hearth"
}
```

</details>

---

### Tool result

_source line 31 · 2026-05-19T03:00:49.586Z_

<details><summary>↩ Tool result · `toolu_01DJXCB9R4nmq3tweFjwsuwD`</summary>

```text
Web search results for query: "ACL Rolling Review call for papers "negative findings" "reproduce or fail to reproduce" contribution types"

Links: [{"title":"ACL 2025 Call for Papers","url":"https://groups.google.com/g/ml-news/c/9pXrq63VQ6c"},{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"Main Conference - ACL 2026","url":"https://2026.aclweb.org/calls/main_conference_papers/"},{"title":"Second Call for Main Conference Papers - NAACL-HLT 2025","url":"https://2025.naacl.org/calls/papers/"},{"title":"ARR Reviewer Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewerguidelines"},{"title":"Review Form – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewform"},{"title":"ACL Rolling Review | ACL Member Portal","url":"https://www.aclweb.org/portal/content/acl-rolling-review"},{"title":"First Call for Papers: NAACL 2025 Main Conference | ACL Member Portal","url":"https://www.aclweb.org/portal/content/naacl-first-call-main-conference-papers"},{"title":"Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authors"}]

Based on the search results, here's information about ACL Rolling Review's call for papers regarding the contribution types you asked about:

## Contribution Types Including Negative Findings and Reproduction Papers

ACL 2025 has a goal of a diverse technical program—in addition to traditional research results, papers may contribute negative findings, survey an area, announce the creation of a new resource, argue a position, report novel linguistic insights derived using existing computational techniques, and reproduce, or fail to reproduce, previous results.

## Specific Details on Short Paper Types

Some common kinds of short papers are (non-)reproduction reports, negative results, opinion pieces, interesting application nuggets (but all these types of contributions could also be presented in long papers, given sufficient substance).

## What Constitutes a Negative Results Paper

A negative results paper might report on non-reproducibility or non-generalizability of previously published results, their misattribution ('right for the wrong reasons'), or present an idea that seemed great (for well-justified reasons), but didn't work.

These guidelines reflect ACL's commitment to publishing diverse types of research contributions beyond traditional positive results, explicitly welcoming reproduction studies, replication failures, and negative findings as valuable contributions to the field.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "0bb5c1ec-84d7-4b9a-aa1b-7f4ac46554a1",
  "isSidechain": true,
  "promptId": "d62aafe3-d75b-460d-a9bb-1b0f23cd5965",
  "agentId": "a2210751531ccd330",
  "type": "user",
  "uuid": "132207db-a3db-4227-b5ea-9589d9e7cbb5",
  "sourceToolAssistantUUID": "0bb5c1ec-84d7-4b9a-aa1b-7f4ac46554a1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/.claude/sessions/reviewer_e7517921",
  "sessionId": "5a74afe6-047b-48bc-9683-816dae74ac45",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "starry-mapping-hearth"
}
```

</details>

---

### Tool result

_source line 32 · 2026-05-19T03:00:56.753Z_

<details><summary>↩ Tool result · `toolu_01MiYsLLCLWZTk97vmZYMWdZ`</summary>

```text
Web search results for query: "EMNLP 2024 main conference "negative" "does not improve" "surprising" accepted paper title"

Links: [{"title":"EMNLP 2024: Call for Papers | ACL Member Portal","url":"https://www.aclweb.org/portal/content/emnlp-2024-call-papers"},{"title":"Conference Overview - EMNLP 2024","url":"https://2024.emnlp.org/program/"},{"title":"15 Papers Accepted to EMNLP 2024 | Department of Computer Science, Columbia University","url":"https://www.cs.columbia.edu/2024/15-papers-accepted-to-emnlp-2024/"},{"title":"Customizable NLP @ EMNLP 2024 | Accepted Papers","url":"https://customnlp4u-24.github.io/accepted/"},{"title":"A quick guide to Amazon’s 50-plus papers at EMNLP 2024 - Amazon Science","url":"https://www.amazon.science/blog/a-quick-guide-to-amazons-50-plus-papers-at-emnlp-2024"},{"title":"EMNLP 2024_Main Conference","url":"https://emnlp2024-main-conference.paperform.co/"}]

Let me search more specifically for the paper title you're looking for:

Links: [{"title":"CFP | Insights 2024","url":"https://insights-workshop.github.io/2021/cfp/"},{"title":"EMNLP (Findings) 2024: Miami, FL, USA","url":"https://dblp.org/db/conf/emnlp/emnlp2024f.html"},{"title":"Alignment with Human Negative Samples via Distributional ...","url":"https://aclanthology.org/2024.findings-emnlp.56.pdf"},{"title":"Enhancing AI Assisted Writing with One-Shot Implicit Negative Feedback - ACL Anthology","url":"https://aclanthology.org/2024.emnlp-main.705/"},{"title":"Reassessing EMNLP 2024’s Best Paper: Does Divergence-Based Calibration for Membership Inference Attacks Hold Up? | Anshuman Suri","url":"https://www.anshumansuri.com/blog/2024/calibrated-mia/"},{"title":"Findings - EMNLP 2024","url":"https://2024.emnlp.org/program/accepted_findings/"},{"title":"dblp: EMNLP 2024 - Industry Track","url":"https://dblp.org/db/conf/emnlp/emnlp2024i.html"},{"title":"Proceedings of the 2024 Conference on Empirical Methods in Natural Language Processing - ACL Anthology","url":"https://aclanthology.org/volumes/2024.emnlp-main/"}]

Let me try a more targeted search for papers with those specific phrases in their titles:

Links: [{"title":"Conference Overview - EMNLP 2024","url":"https://2024.emnlp.org/program/"},{"title":"EMNLP 2024 The 2024 Conference on Empirical Methods in Natural","url":"https://aclanthology.org/2024.findings-emnlp.0.pdf"},{"title":"15 Papers Accepted to EMNLP 2024 | Department of Computer Science, Columbia University","url":"https://www.cs.columbia.edu/2024/15-papers-accepted-to-emnlp-2024/"},{"title":"EMNLP 2024: Call for Papers | ACL Member Portal","url":"https://www.aclweb.org/portal/content/emnlp-2024-call-papers"},{"title":"Customizable NLP @ EMNLP 2024 | Accepted Papers","url":"https://customnlp4u-24.github.io/accepted/"},{"title":"Paper Digest: EMNLP 2024 Papers & Highlights – Resources | Paper Digest","url":"https://resources.paperdigest.org/2024/11/emnlp-2024-papers-highlights/"},{"title":"A quick guide to Amazon’s 50-plus papers at EMNLP 2024 - Amazon Science","url":"https://www.amazon.science/blog/a-quick-guide-to-amazons-50-plus-papers-at-emnlp-2024"},{"title":"EMNLP 2024 Accepted Paper List - Paper Copilot","url":"https://papercopilot.com/paper-list/emnlp-paper-list/emnlp-2024-paper-list/"}]

Let me search more specifically for papers with those exact phrases in the title:

Links: [{"title":"Reassessing EMNLP 2024’s Best Paper: Does Divergence-Based Calibration for Membership Inference Attacks Hold Up? | Anshuman Suri","url":"https://www.anshumansuri.com/blog/2024/calibrated-mia/"},{"title":"Findings - EMNLP 2024","url":"https://2024.emnlp.org/program/accepted_findings/"},{"title":"15 Papers Accepted to EMNLP 2024 | Department of Computer Science, Columbia University","url":"https://www.cs.columbia.edu/2024/15-papers-accepted-to-emnlp-2024/"},{"title":"EMNLP 2024: Call for Papers | ACL Member Portal","url":"https://www.aclweb.org/portal/content/emnlp-2024-call-papers"},{"title":"Paper Digest: EMNLP 2024 Papers & Highlights – Resources | Paper Digest","url":"https://resources.paperdigest.org/2024/11/emnlp-2024-papers-highlights/"},{"title":"HalluCitation Matters: Revealing the Impact of Hallucinated References with 300 Hallucinated Papers in ACL Conferences","url":"https://arxiv.org/pdf/2601.18724"},{"title":"Min-p, Max Exaggeration: A Critical Analysis of Min-p Sampling in Language Models","url":"https://arxiv.org/pdf/2506.13681"},{"title":"Most Influential EMNLP Papers (2024-09 Version) – Resources | Paper Digest","url":"https://resources.paperdigest.org/2024/09/most-influential-emnlp-papers-2024-09/"},{"title":"EMNLP 2024 Accepted Paper List - Paper Copilot","url":"https://papercopilot.com/paper-list/emnlp-paper-list/emnlp-2024-paper-list/"},{"title":"Paper Digest: EMNLP 2025 Papers & Highlights – Paper Digest","url":"https://www.paperdigest.org/2025/11/emnlp-2025-papers-highlights/"}]

Let me try one more search with different keywords:

Links: [{"title":"Our EMNLP 2025 Papers – Center for Research in Computer Vision","url":"https://www.crcv.ucf.edu/2025/09/04/our-emnlp-2025-papers/"},{"title":"HalluCitation Matters: Revealing the Impact of Hallucinated References with 300 Hallucinated Papers in ACL Conferences","url":"https://arxiv.org/pdf/2601.18724"},{"title":"Proceedings of the 2025 Conference on Empirical Methods in Natural Language Processing - ACL Anthology","url":"https://aclanthology.org/volumes/2025.emnlp-main/"},{"title":"The 2025 Conference on Empirical Methods in Natural Language Processing - ACL Anthology","url":"https://aclanthology.org/events/emnlp-2025/"},{"title":"Proceedings of the 2024 Conference on Empirical Methods in Natural Language Processing - ACL Anthology","url":"https://aclanthology.org/volumes/2024.emnlp-main/"},{"title":"The 2024 Conference on Empirical Methods in Natural Language Processing - ACL Anthology","url":"https://aclanthology.org/events/emnlp-2024/"}]

Based on my web searches, I was unable to find a specific EMNLP 2024 main conference paper with the exact combination of keywords you mentioned in the title ("negative," "does not improve," and "surprising"). 

While my searches revealed that 1,271 papers were accepted to the EMNLP 2024 Main Conference, and EMNLP 2024 welcomed papers that may contribute negative findings, I could not locate a specific accepted paper title containing all three of those particular phrases.

Could you provide any additional details about the paper, such as:
- The approximate topic area (NLP domain, methodology type, etc.)
- Author names if you know them
- Whether it was a long or short paper
- Any other distinguishing details

This would help me locate the specific paper you're looking for.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "58ffad99-2ab5-4759-9e80-45a741e34d38",
  "isSidechain": true,
  "promptId": "d62aafe3-d75b-460d-a9bb-1b0f23cd5965",
  "agentId": "a2210751531ccd330",
  "type": "user",
  "uuid": "2285cfb3-ac1f-4ed7-8f28-23b1a3248d87",
  "sourceToolAssistantUUID": "58ffad99-2ab5-4759-9e80-45a741e34d38",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/.claude/sessions/reviewer_e7517921",
  "sessionId": "5a74afe6-047b-48bc-9683-816dae74ac45",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "starry-mapping-hearth"
}
```

</details>

---

### Assistant

_source line 33 · 2026-05-19T03:00:59.693Z_

Let me get the specific paper lists from the Insights workshop and search for more concrete examples.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2285cfb3-ac1f-4ed7-8f28-23b1a3248d87",
  "isSidechain": true,
  "agentId": "a2210751531ccd330",
  "requestId": "req_011CbBBUpLmo6kR4F3MeUDfA",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "c18c268a-18c6-4a25-95dc-8f6b008216b6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/.claude/sessions/reviewer_e7517921",
  "sessionId": "5a74afe6-047b-48bc-9683-816dae74ac45",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "starry-mapping-hearth",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FxFwG2QdWEu9ReRiBbGTmo",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5765,
      "cache_read_input_tokens": 30583,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 5765,
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

_source line 34 · 2026-05-19T03:01:00.649Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_012XN89HK1czgseAJFyRoupZ`</summary>

```json
{
  "query": "aclanthology.org/2024.insights-1 papers titles list workshop negative results"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c18c268a-18c6-4a25-95dc-8f6b008216b6",
  "isSidechain": true,
  "agentId": "a2210751531ccd330",
  "requestId": "req_011CbBBUpLmo6kR4F3MeUDfA",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "dce4f0f5-a179-4fbe-be84-254cb5d5c530",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/.claude/sessions/reviewer_e7517921",
  "sessionId": "5a74afe6-047b-48bc-9683-816dae74ac45",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "starry-mapping-hearth",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FxFwG2QdWEu9ReRiBbGTmo",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5765,
      "cache_read_input_tokens": 30583,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 5765,
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

_source line 35 · 2026-05-19T03:01:01.581Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_018rgmcndGn59a7WRdsyxjfz`</summary>

```json
{
  "query": "\"Position: Embracing Negative Results\" ICML 2024 taxonomy categories negative results criteria publishable"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "dce4f0f5-a179-4fbe-be84-254cb5d5c530",
  "isSidechain": true,
  "agentId": "a2210751531ccd330",
  "requestId": "req_011CbBBUpLmo6kR4F3MeUDfA",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "f9d5492d-0f81-43f3-9553-d3cb8ff04e4c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/.claude/sessions/reviewer_e7517921",
  "sessionId": "5a74afe6-047b-48bc-9683-816dae74ac45",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "starry-mapping-hearth",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FxFwG2QdWEu9ReRiBbGTmo",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5765,
      "cache_read_input_tokens": 30583,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 5765,
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

_source line 36 · 2026-05-19T03:01:02.553Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01MY1ZLtBGdidCePvwL7cpWs`</summary>

```json
{
  "query": "EMNLP ACL 2024 2025 \"revisiting\" \"rethinking\" \"do we really need\" \"critical analysis\" accepted paper"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f9d5492d-0f81-43f3-9553-d3cb8ff04e4c",
  "isSidechain": true,
  "agentId": "a2210751531ccd330",
  "requestId": "req_011CbBBUpLmo6kR4F3MeUDfA",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "0f4d02c3-3f63-4c06-8727-7b506ae3404f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/.claude/sessions/reviewer_e7517921",
  "sessionId": "5a74afe6-047b-48bc-9683-816dae74ac45",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "starry-mapping-hearth",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FxFwG2QdWEu9ReRiBbGTmo",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5765,
      "cache_read_input_tokens": 30583,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 5765,
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

_source line 37 · 2026-05-19T03:01:03.050Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01WYbYfSaGe7RrBvuMJtP4nx`</summary>

```json
{
  "query": "Insights 2025 NAACL workshop accepted papers negative results NLP"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0f4d02c3-3f63-4c06-8727-7b506ae3404f",
  "isSidechain": true,
  "agentId": "a2210751531ccd330",
  "requestId": "req_011CbBBUpLmo6kR4F3MeUDfA",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "5c800ea0-e4d7-421b-b742-c9eaac986ad1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/.claude/sessions/reviewer_e7517921",
  "sessionId": "5a74afe6-047b-48bc-9683-816dae74ac45",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "starry-mapping-hearth",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FxFwG2QdWEu9ReRiBbGTmo",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5765,
      "cache_read_input_tokens": 30583,
      "output_tokens": 269,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 5765
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 269,
          "cache_read_input_tokens": 30583,
          "cache_creation_input_tokens": 5765,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 5765,
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

_source line 38 · 2026-05-19T03:01:04.901Z_

<details><summary>↩ Tool result · `toolu_012XN89HK1czgseAJFyRoupZ`</summary>

```text
Web search results for query: "aclanthology.org/2024.insights-1 papers titles list workshop negative results"

Links: [{"title":"Other Workshops and Events (2024) - ACL Anthology","url":"https://aclanthology.org/events/ws-2024/"},{"title":"Insights 2024 The 5th Workshop on Insights from Negative Results in NLP","url":"https://aclanthology.org/2024.insights-1.0.pdf"},{"title":"Workshop on Insights from Negative Results in NLP (2023) - ACL Anthology","url":"https://aclanthology.org/events/insights-2023/"},{"title":"Aclanthology","url":"https://aclanthology.org/2024.insights-1.15.pdf"},{"title":"Workshop on Insights from Negative Results in NLP (2025) - ACL Anthology","url":"https://aclanthology.org/events/insights-2025/"},{"title":"Workshop on Insights from Negative Results in NLP - ACL Anthology","url":"https://aclanthology.org/venues/insights/"},{"title":"Proceedings of the Fourth Workshop on Insights from Negative Results in NLP - ACL Anthology","url":"https://aclanthology.org/volumes/2023.insights-1/"},{"title":"NAACL 2025 The 5th Workshop on Insights from Negative Results in NLP","url":"https://aclanthology.org/2025.insights-1.0.pdf"}]

Based on the search results, I found information about the 2024 "Insights from Negative Results in NLP" workshop. The Fifth Workshop on Insights from Negative Results in NLP had 20 papers.

However, the search results don't provide a complete list of all paper titles from the 2024.insights-1 workshop. The PDF files referenced appear to contain the proceedings, but the full title list is not displayed in the search results. 

To access the complete list of paper titles for the 2024.insights-1 workshop, you would need to visit the ACL Anthology page directly at aclanthology.org/volumes/2024.insights-1/ or download the proceedings PDF, which should contain the full table of contents with all paper titles.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "dce4f0f5-a179-4fbe-be84-254cb5d5c530",
  "isSidechain": true,
  "promptId": "d62aafe3-d75b-460d-a9bb-1b0f23cd5965",
  "agentId": "a2210751531ccd330",
  "type": "user",
  "uuid": "87e43d61-acaf-4a56-91c5-5d68c7ac8c40",
  "sourceToolAssistantUUID": "dce4f0f5-a179-4fbe-be84-254cb5d5c530",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/.claude/sessions/reviewer_e7517921",
  "sessionId": "5a74afe6-047b-48bc-9683-816dae74ac45",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "starry-mapping-hearth"
}
```

</details>

---

### Tool result

_source line 39 · 2026-05-19T03:01:07.786Z_

<details><summary>↩ Tool result · `toolu_01MY1ZLtBGdidCePvwL7cpWs`</summary>

```text
Web search results for query: "EMNLP ACL 2024 2025 "revisiting" "rethinking" "do we really need" "critical analysis" accepted paper"

Links: [{"title":"HalluCitation Matters: Revealing the Impact of Hallucinated References with 300 Hallucinated Papers in ACL Conferences","url":"https://arxiv.org/pdf/2601.18724"},{"title":"[EMNLP 2025] First Call for Papers | ACL Member Portal","url":"https://www.aclweb.org/portal/content/emnlp-2025-first-call-papers"},{"title":"The 2024 Conference on Empirical Methods in Natural Language Processing - ACL Anthology","url":"https://aclanthology.org/events/emnlp-2024/"},{"title":"EMNLP 2024 Accepted Paper List - Paper Copilot","url":"https://papercopilot.com/paper-list/emnlp-paper-list/emnlp-2024-paper-list/"},{"title":"Call for Main Conference Papers - EMNLP 2025","url":"https://2025.emnlp.org/calls/main_conference_papers/"},{"title":"Paper Digest: EMNLP 2025 Papers & Highlights – Paper Digest","url":"https://www.paperdigest.org/2025/11/emnlp-2025-papers-highlights/"},{"title":"dblp: EMNLP","url":"https://dblp.org/db/conf/emnlp/index.html"},{"title":"The 2025 Conference on Empirical Methods in Natural Language Processing - ACL Anthology","url":"https://aclanthology.org/events/emnlp-2025/"}]

I've performed the web search for papers from EMNLP and ACL 2024/2025 with those specific phrases. The search results show general information about EMNLP 2024 and 2025 conferences and their accepted papers, including 1406 papers accepted in the Findings of the Association for Computational Linguistics: EMNLP 2025. However, the search results don't specifically highlight papers with those exact phrases in their titles ("revisiting," "rethinking," "do we really need," or "critical analysis").

To find specific papers containing those phrases, you might want to:

1. Browse the ACL Anthology directly at aclanthology.org and search for papers from EMNLP 2024, EMNLP 2025, and ACL 2024/2025 with those keywords
2. Search arXiv.org with those specific phrases combined with conference names
3. Use the Paper Copilot tool or similar services that index conference papers and allow title/keyword searches

Would you like me to perform additional targeted searches to find specific papers with those phrases?


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "0f4d02c3-3f63-4c06-8727-7b506ae3404f",
  "isSidechain": true,
  "promptId": "d62aafe3-d75b-460d-a9bb-1b0f23cd5965",
  "agentId": "a2210751531ccd330",
  "type": "user",
  "uuid": "d7ede7f1-20f2-45f0-b7b1-ae2756ea5e72",
  "sourceToolAssistantUUID": "0f4d02c3-3f63-4c06-8727-7b506ae3404f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/.claude/sessions/reviewer_e7517921",
  "sessionId": "5a74afe6-047b-48bc-9683-816dae74ac45",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "starry-mapping-hearth"
}
```

</details>

---

### Tool result

_source line 40 · 2026-05-19T03:01:08.590Z_

<details><summary>↩ Tool result · `toolu_01WYbYfSaGe7RrBvuMJtP4nx`</summary>

```text
Web search results for query: "Insights 2025 NAACL workshop accepted papers negative results NLP"

Links: [{"title":"NAACL 2025 The 5th Workshop on Insights from Negative Results in NLP","url":"https://aclanthology.org/2025.insights-1.0.pdf"},{"title":"CFP | Insights 2024","url":"https://insights-workshop.github.io/2025/cfp/"},{"title":"Workshop on Insights from Negative Results in NLP | ACL Member Portal","url":"https://www.aclweb.org/portal/content/workshop-insights-negative-results-nlp-0"},{"title":"Accepted papers | Insights 2024","url":"https://insights-workshop.github.io/2025/accepted/"},{"title":"Workshop on Insights from Negative Results in NLP | Insights 2024","url":"https://insights-workshop.github.io/index"},{"title":"INSIGHTS FROM NEGATIVE RESULTS IN NLP. WORKSHOP. 5TH 2025. (INSIGHTS 2025) - proceedings.com","url":"https://www.proceedings.com/80148.html"},{"title":"Second Call for Main Conference Papers - NAACL-HLT 2025","url":"https://2025.naacl.org/calls/papers/"},{"title":"Call for Industry Track Papers - NAACL-HLT 2025","url":"https://2025.naacl.org/calls/industry/"},{"title":"Insights 2024 | Workshop on Insights from Negative Results in NLP","url":"https://insights-workshop.github.io/"},{"title":"The Sixth Workshop on Insights from Negative Results in NLP - ACL Anthology","url":"https://aclanthology.org/volumes/2025.insights-1/"}]

Based on the search results, here's what I found about the Insights 2025 NAACL workshop:

## Key Statistics

The fifth iteration of the Workshop on Insights from Negative Results attracted 23 submissions and accepted 16 papers, resulting in a 64% acceptance rate.

## Workshop Details

The Workshop on Insights from Negative Results in NLP took place in Albuquerque, New Mexico in May 2025 (co-located with NAACL). It was hybrid, allowing for both in-person and virtual presentations.

## Workshop Purpose

The workshop continues to contribute to reality-check discussions on progress in NLP. Publication of negative results is difficult in most fields, but in NLP the problem is exacerbated by the near-universal focus on improvements in benchmarks.

The search results also point to an ACL Anthology page with the accepted papers, though the specific paper titles and authors are not fully displayed in the search results. You can access the full list of accepted papers at the ACL Anthology or through the workshop's official website.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "5c800ea0-e4d7-421b-b742-c9eaac986ad1",
  "isSidechain": true,
  "promptId": "d62aafe3-d75b-460d-a9bb-1b0f23cd5965",
  "agentId": "a2210751531ccd330",
  "type": "user",
  "uuid": "804e7db1-4ed8-417b-8980-634d71cee343",
  "sourceToolAssistantUUID": "5c800ea0-e4d7-421b-b742-c9eaac986ad1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/.claude/sessions/reviewer_e7517921",
  "sessionId": "5a74afe6-047b-48bc-9683-816dae74ac45",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "starry-mapping-hearth"
}
```

</details>

---

### Tool result

_source line 41 · 2026-05-19T03:01:23.921Z_

<details><summary>↩ Tool result · `toolu_018rgmcndGn59a7WRdsyxjfz`</summary>

```text
Web search results for query: ""Position: Embracing Negative Results" ICML 2024 taxonomy categories negative results criteria publishable"

Links: [{"title":"[ICML 2024] Position: Embracing Negative Results in Machine Learning - YouTube","url":"https://www.youtube.com/watch?v=JDP6cXWmChI"},{"title":"Position: Embracing Negative Results in Machine Learning | OpenReview","url":"https://openreview.net/forum?id=3RXAiU7sss"},{"title":"ICML Poster Position: Embracing Negative Results in Machine Learning","url":"https://icml.cc/virtual/2024/poster/35063"},{"title":"ICML 2024 Schedule","url":"https://icml.cc/virtual/2024/calendar"},{"title":"ICML 2024 Orals","url":"https://icml.cc/virtual/2024/events/oral"},{"title":"[2406.03980] Position: Embracing Negative Results in Machine Learning","url":"https://arxiv.org/abs/2406.03980"},{"title":"Position: Embracing Negative Results in Machine Learning","url":"https://proceedings.mlr.press/v235/karl24a.html"},{"title":"Position: Embracing Negative Results in Machine Learning","url":"https://arxiv.org/pdf/2406.03980"}]

I found the paper! Now let me search for more specific information about the taxonomy categories, criteria for publishable negative results, and any categorization system mentioned in the paper.

Links: [{"title":"Position: Embracing Negative Results in Machine Learning","url":"https://proceedings.mlr.press/v235/karl24a.html"},{"title":"Position: Embracing Negative Results in Machine Learning","url":"https://arxiv.org/html/2406.03980v1"},{"title":"[2406.03980] Position: Embracing Negative Results in Machine Learning","url":"https://arxiv.org/abs/2406.03980"},{"title":"Position: Embracing Negative Results in Machine Learning","url":"https://arxiv.org/pdf/2406.03980"},{"title":"ICML Poster Position: Embracing Negative Results in Machine Learning","url":"https://icml.cc/virtual/2024/poster/35063"},{"title":"(PDF) Position: Embracing Negative Results in Machine Learning","url":"https://www.researchgate.net/publication/381226301_Position_Embracing_Negative_Results_in_Machine_Learning"}]

Let me search more specifically for the taxonomy and types of negative results mentioned in the paper.

Links: [{"title":"Position: Embracing Negative Results in Machine Learning","url":"https://arxiv.org/html/2406.03980v1"},{"title":"(PDF) Position: Embracing Negative Results in Machine Learning","url":"https://www.researchgate.net/publication/381226301_Position_Embracing_Negative_Results_in_Machine_Learning"},{"title":"Position: Embracing Negative Results in Machine Learning","url":"https://arxiv.org/pdf/2406.03980"},{"title":"[2406.03980] Position: Embracing Negative Results in Machine Learning","url":"https://arxiv.org/abs/2406.03980"},{"title":"Negative results: negative perceptions limit their potential for increasing reproducibility","url":"https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4494691/"}]

Great! I found the taxonomy. Now let me search for more details about the specific criteria for publishability.

Links: [{"title":"Position: Embracing Negative Results in Machine Learning","url":"https://arxiv.org/html/2406.03980v1"},{"title":"Position: Embracing Negative Results in Machine Learning","url":"https://proceedings.mlr.press/v235/karl24a.html"},{"title":"Position: Embracing Negative Results in Machine Learning","url":"https://arxiv.org/pdf/2406.03980"},{"title":"Position: Embracing Negative Results in Machine Learning | AI Research Paper Details","url":"https://www.aimodels.fyi/papers/arxiv/position-embracing-negative-results-machine-learning"},{"title":"(PDF) Position: Embracing Negative Results in Machine Learning","url":"https://www.researchgate.net/publication/381226301_Position_Embracing_Negative_Results_in_Machine_Learning"},{"title":"[2406.03980] Position: Embracing Negative Results in Machine Learning","url":"https://arxiv.org/abs/2406.03980"}]

Perfect! I now have enough information to provide a comprehensive answer. Let me compile the findings.

## Summary of "Position: Embracing Negative Results" (ICML 2024)

This position paper argues that publications proposing novel machine learning methods are often primarily rated by exhibited predictive performance on selected problems, but predictive performance alone is not a good indicator for the worth of a publication and can foster inefficiencies in the machine learning research community and wrong incentives for researchers.

### Taxonomy of Negative Results

The paper distinguishes between two important subtypes of negative results: Novel method negative results (NMNR), which refer to submissions proposing a novel method that does not beat existing state-of-the-art methods, and existing method negative results (EMNR), which occur when existing state-of-the-art methods are demonstrated to have inferior performance as expected. EMNR can be a replication study or a publication shining a light on specific failure modes of existing methods.

### Criteria for Publishable Negative Results

The paper specifies several criteria for publishing negative results:

1. **Experimental Design and Setup**: Proper and meticulous experimentation is an important foundation for all conclusions drawn in empirical machine learning papers, and this criterion should be equally important for all positive and negative results.

2. **Surprise Factor**: While a surprising result is generally regarded as positive, this is not a crucial factor for many papers with positive results; however, if a negative result is very predictable and obvious, there really is not much sense in publishing it.

3. **Depth of Analysis**: For NMNR-publications it can be especially important to foster an understanding of the observed results, and ideally authors would provide an in-depth analysis as to why the negative results were observed.

### Review Process Recommendations

The paper suggests that results should be included in the final version, which is then re-examined for soundness, quality and other applicable criteria by reviewers, deliberately eliminating bias from experimental results in the first decision round while re-emphasizing other virtues, with this idea specifically targeting NMNR-publications.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f9d5492d-0f81-43f3-9553-d3cb8ff04e4c",
  "isSidechain": true,
  "promptId": "d62aafe3-d75b-460d-a9bb-1b0f23cd5965",
  "agentId": "a2210751531ccd330",
  "type": "user",
  "uuid": "f220c534-2804-4f0e-9c52-878f50595aa8",
  "sourceToolAssistantUUID": "f9d5492d-0f81-43f3-9553-d3cb8ff04e4c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/.claude/sessions/reviewer_e7517921",
  "sessionId": "5a74afe6-047b-48bc-9683-816dae74ac45",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "starry-mapping-hearth"
}
```

</details>

---

### Assistant

_source line 42 · 2026-05-19T03:01:27.771Z_

Let me fetch the actual paper lists from the workshops and find specific main-track examples.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f220c534-2804-4f0e-9c52-878f50595aa8",
  "isSidechain": true,
  "agentId": "a2210751531ccd330",
  "requestId": "req_011CbBBWpRJ1BbGQbphahvvE",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "4dbb7af2-0bec-4a60-8b3f-a157040b4dc9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/.claude/sessions/reviewer_e7517921",
  "sessionId": "5a74afe6-047b-48bc-9683-816dae74ac45",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "starry-mapping-hearth",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019tmTwRMHhdJVqEAcJ1xQeL",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1455,
      "cache_creation_input_tokens": 2572,
      "cache_read_input_tokens": 36348,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2572,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 5,
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

_source line 43 · 2026-05-19T03:01:28.676Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_011wJZdxYV1SxmSooTA7tNHD`</summary>

```json
{
  "query": "site:aclanthology.org/2025.insights-1 paper titles"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4dbb7af2-0bec-4a60-8b3f-a157040b4dc9",
  "isSidechain": true,
  "agentId": "a2210751531ccd330",
  "requestId": "req_011CbBBWpRJ1BbGQbphahvvE",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "8a12664f-aa1d-485c-b43b-34cd01e4e9d1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/.claude/sessions/reviewer_e7517921",
  "sessionId": "5a74afe6-047b-48bc-9683-816dae74ac45",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "starry-mapping-hearth",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019tmTwRMHhdJVqEAcJ1xQeL",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1455,
      "cache_creation_input_tokens": 2572,
      "cache_read_input_tokens": 36348,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2572,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 5,
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

_source line 44 · 2026-05-19T03:01:29.385Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_011N4WehS6iheKuL1JRgV5EG`</summary>

```json
{
  "query": "EMNLP 2024 \"Insights into LLM Long-Context Failures\" Transformers Know but Don't Tell"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8a12664f-aa1d-485c-b43b-34cd01e4e9d1",
  "isSidechain": true,
  "agentId": "a2210751531ccd330",
  "requestId": "req_011CbBBWpRJ1BbGQbphahvvE",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "7f7b2c91-f2f9-44dc-b0f0-afe387387cb0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/.claude/sessions/reviewer_e7517921",
  "sessionId": "5a74afe6-047b-48bc-9683-816dae74ac45",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "starry-mapping-hearth",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019tmTwRMHhdJVqEAcJ1xQeL",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1455,
      "cache_creation_input_tokens": 2572,
      "cache_read_input_tokens": 36348,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2572,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 5,
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

_source line 45 · 2026-05-19T03:01:30.504Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01M4CW3fbj8jzF8mssdnKfHE`</summary>

```json
{
  "query": "ACL 2024 2025 main track accepted \"rethinking\" OR \"revisiting\" OR \"failure\" OR \"do not\" negative finding paper"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7f7b2c91-f2f9-44dc-b0f0-afe387387cb0",
  "isSidechain": true,
  "agentId": "a2210751531ccd330",
  "requestId": "req_011CbBBWpRJ1BbGQbphahvvE",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "bfb84b51-3ccf-4c27-9217-15fc205bf5c6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/.claude/sessions/reviewer_e7517921",
  "sessionId": "5a74afe6-047b-48bc-9683-816dae74ac45",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "starry-mapping-hearth",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019tmTwRMHhdJVqEAcJ1xQeL",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1455,
      "cache_creation_input_tokens": 2572,
      "cache_read_input_tokens": 36348,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2572,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 5,
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

_source line 46 · 2026-05-19T03:01:32.166Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01KBRfLhe55s4J3TXUTpUfsL`</summary>

```json
{
  "query": "\"Machine Learning Conferences Should Establish\" \"Refutations and Critiques\" track arxiv 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "bfb84b51-3ccf-4c27-9217-15fc205bf5c6",
  "isSidechain": true,
  "agentId": "a2210751531ccd330",
  "requestId": "req_011CbBBWpRJ1BbGQbphahvvE",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "c22dda26-9e6a-43a8-a608-b029429dcfde",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/.claude/sessions/reviewer_e7517921",
  "sessionId": "5a74afe6-047b-48bc-9683-816dae74ac45",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "starry-mapping-hearth",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019tmTwRMHhdJVqEAcJ1xQeL",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1455,
      "cache_creation_input_tokens": 2572,
      "cache_read_input_tokens": 36348,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2572,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 5,
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

_source line 47 · 2026-05-19T03:01:33.731Z_

<details><summary>↩ Tool result · `toolu_011wJZdxYV1SxmSooTA7tNHD`</summary>

```text
Web search results for query: "site:aclanthology.org/2025.insights-1 paper titles"

Links: [{"title":"Exploring Limitations of LLM Capabilities with Multi-Problem Evaluation - ACL Anthology","url":"https://aclanthology.org/2025.insights-1.12/"},{"title":"Study to Evaluate the Safety, Tolerability, Pharmacokinetics, and Efficacy of AMG 562 in Subjects With r/r Diffuse Large B-cell Lymphoma, Mantle Cell Lymphoma, or Follicular Lymphoma","url":"https://cdn.clinicaltrials.gov/large-docs/28/NCT03571828/Prot_000.pdf"},{"title":"Collaborative Large Language Models for Automated Data Extraction in Living Systematic Reviews","url":"https://www.medrxiv.org/content/10.1101/2024.09.20.24314108.full.pdf"},{"title":"Findings of the Association for Computational Linguistics: ACL 2025 - ACL Anthology","url":"https://aclanthology.org/volumes/2025.findings-acl/"},{"title":"Generalizable Clinical Note Section Identification with Large Language Models","url":"https://www.medrxiv.org/content/10.1101/2024.02.18.24303014.full.pdf"},{"title":"Evaluating large language models for natural-language-to-code generation on aggregate Czech public health data analysis","url":"https://www.medrxiv.org/content/10.64898/2025.12.05.25341697.full.pdf"},{"title":"ExDoRA: enhancing the transferability of large language models for depression detection using free-text explanations","url":"https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12133835/"},{"title":"Reasoning Models for Text Mining in Oncology – a Comparison Between o1 Preview and GPT-4o","url":"https://www.medrxiv.org/content/10.1101/2024.12.06.24318592.full.pdf"},{"title":"Open Label Trial to Explore Safety of Combining Afatinib (BIBW 2992) and Radiotherapy With or Without Temozolomide in Newly Diagnosed Glioblastoma Multiform","url":"https://cdn.clinicaltrials.gov/large-docs/31/NCT00977431/Prot_000.pdf"}]

The search returned limited results for the specific venue. From the results, I found one paper from the 2025 Insights workshop (which appears to be "The Sixth Workshop on Insights from Negative Results in NLP"):

**Exploring Limitations of LLM Capabilities with Multi-Problem Evaluation** by Wang et al.

To get a more complete list of all paper titles from the 2025.insights-1 venue, you may want to visit the ACL Anthology directly at the volume page, as the search with special operators returned limited results. The venue appears to be for the Sixth Workshop on Insights from Negative Results in NLP held in Albuquerque, New Mexico in 2025.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "8a12664f-aa1d-485c-b43b-34cd01e4e9d1",
  "isSidechain": true,
  "promptId": "d62aafe3-d75b-460d-a9bb-1b0f23cd5965",
  "agentId": "a2210751531ccd330",
  "type": "user",
  "uuid": "947f044a-d41d-480e-9295-f69052b96fd2",
  "sourceToolAssistantUUID": "8a12664f-aa1d-485c-b43b-34cd01e4e9d1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/.claude/sessions/reviewer_e7517921",
  "sessionId": "5a74afe6-047b-48bc-9683-816dae74ac45",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "starry-mapping-hearth"
}
```

</details>

---

### Tool result

_source line 48 · 2026-05-19T03:01:35.426Z_

<details><summary>↩ Tool result · `toolu_011N4WehS6iheKuL1JRgV5EG`</summary>

```text
Web search results for query: "EMNLP 2024 "Insights into LLM Long-Context Failures" Transformers Know but Don't Tell"

Links: [{"title":"Insights into LLM Long-Context Failures: When Transformers Know but Don’t Tell - ACL Anthology","url":"https://aclanthology.org/2024.findings-emnlp.447/"},{"title":"Insights into LLM Long-Context Failures: When Transformers Know but Don't Tell [Quick Review]","url":"https://liner.com/review/insights-into-llm-longcontext-failures-when-transformers-know-but-dont"},{"title":"[2406.14673] Insights into LLM Long-Context Failures: When Transformers Know but Don't Tell","url":"https://arxiv.org/abs/2406.14673"},{"title":"Findings - EMNLP 2024","url":"https://2024.emnlp.org/program/accepted_findings/"},{"title":"EMNLP-Findings’24 Insights into LLM Long-Context Failures: When Transformers Know but Don’t Tell","url":"https://arxiv.org/html/2406.14673v2"},{"title":"Insights into LLM Long-Context Failures: When Transformers Know but Don't Tell - ADS","url":"https://ui.adsabs.harvard.edu/abs/2024arXiv240614673L/abstract"},{"title":"EMNLP-Findings’24 Insights into LLM Long-Context Failures:","url":"https://arxiv.org/pdf/2406.14673"},{"title":"Insights into LLM Long-Context Failures","url":"https://aclanthology.org/2024.findings-emnlp.447.pdf"}]

I found the research paper! Here's what I can tell you about it:

"Insights into LLM Long-Context Failures: When Transformers Know but Don't Tell" was published in Findings of the Association for Computational Linguistics: EMNLP 2024, authored by Muhan Gao, TaiMing Lu, Kuai Yu, Adam Byerly, and Daniel Khashabi.

The key finding of the paper is that while LLMs encode the position of target information, they often fail to leverage this in generating accurate responses, revealing a disconnect between information retrieval and utilization, a "know but don't tell" phenomenon.

The research explores how Large Language Models exhibit positional bias, struggling to utilize information from the middle or end of long contexts, by probing their hidden representations.

The paper is available through the ACL Anthology (https://aclanthology.org/2024.findings-emnlp.447/) and also on arXiv (https://arxiv.org/abs/2406.14673).


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "7f7b2c91-f2f9-44dc-b0f0-afe387387cb0",
  "isSidechain": true,
  "promptId": "d62aafe3-d75b-460d-a9bb-1b0f23cd5965",
  "agentId": "a2210751531ccd330",
  "type": "user",
  "uuid": "45d9bc42-9f8c-43eb-bbe4-750a764b1372",
  "sourceToolAssistantUUID": "7f7b2c91-f2f9-44dc-b0f0-afe387387cb0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/.claude/sessions/reviewer_e7517921",
  "sessionId": "5a74afe6-047b-48bc-9683-816dae74ac45",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "starry-mapping-hearth"
}
```

</details>

---

### Tool result

_source line 49 · 2026-05-19T03:01:41.343Z_

<details><summary>↩ Tool result · `toolu_01M4CW3fbj8jzF8mssdnKfHE`</summary>

```text
Web search results for query: "ACL 2024 2025 main track accepted "rethinking" OR "revisiting" OR "failure" OR "do not" negative finding paper"

Links: [{"title":"Main Conference - ACL 2025","url":"https://2025.aclweb.org/calls/main_conference_papers/"},{"title":"HalluCitation Matters: Revealing the Impact of Hallucinated References with 300 Hallucinated Papers in ACL Conferences","url":"https://arxiv.org/pdf/2601.18724"},{"title":"acl 2024 Accepted Paper List - Paper Copilot","url":"https://papercopilot.com/paper-list/acl-paper-list/acl-2024-paper-list/"},{"title":"LLMs Have Made Failure Worth Publishing","url":"https://arxiv.org/pdf/2604.06236"},{"title":"ACL 2025 Industry Track | ACL Member Portal","url":"https://www.aclweb.org/portal/content/acl-2025-industry-track"},{"title":"ACL.2025 - Short Papers | Cool Papers - Immersive Paper Discovery","url":"https://papers.cool/venue/ACL.2025?group=Short+Papers"},{"title":"Paper Digest: ACL 2025 Papers & Highlights – Paper Digest","url":"https://www.paperdigest.org/2025/07/acl-2025-papers-highlights/"}]

I found some results, but I need to search more specifically for ACL 2024 and 2025 main track papers with those keywords. Let me refine the search:

Links: [{"title":"Accepted Main Conference Papers - ACL 2024","url":"https://2024.aclweb.org/program/main_conference_papers/"},{"title":"ACL 2024: Bangkok, Thailand","url":"https://dblp.org/db/conf/acl/acl2024-1.html"},{"title":"A quick guide to Amazon’s papers at ACL 2024 - Amazon Science","url":"https://www.amazon.science/blog/a-quick-guide-to-amazons-papers-at-acl-2024"},{"title":"ACL 2024 - Amazon Science","url":"https://www.amazon.science/conferences-and-events/acl-2024"},{"title":"Best Papers - ACL 2023","url":"https://2023.aclweb.org/program/best_papers/"},{"title":"Findings Accepted Papers -","url":"https://2026.eacl.org/program/findings-accepted/"},{"title":"Proceedings of the 62nd Annual Meeting of the Association for Computational Linguistics (Volume 2: Short Papers) - ACL Anthology","url":"https://aclanthology.org/volumes/2024.acl-short/"},{"title":"ACL 2025 — My First Dive into the NLP Universe | by Nikhil Verma | Medium","url":"https://lih-verma.medium.com/acl-2025-my-first-dive-into-the-nlp-universe-c9fc0ae809b1"}]

Links: [{"title":"Main Conference - ACL 2025","url":"https://2025.aclweb.org/calls/main_conference_papers/"},{"title":"ACL 2025 Call for Papers","url":"https://groups.google.com/g/ml-news/c/9pXrq63VQ6c"},{"title":"[NAACL 2025] Second Call for Main Conference Papers | ACL Member Portal","url":"https://www.aclweb.org/portal/content/naacl-2025-second-call-main-conference-papers"},{"title":"Second Call for Main Conference Papers - NAACL-HLT 2025","url":"https://2025.naacl.org/calls/papers/"},{"title":"HalluCitation Matters: Revealing the Impact of Hallucinated References with 300 Hallucinated Papers in ACL Conferences","url":"https://arxiv.org/pdf/2601.18724"},{"title":"Paper Digest: ACL 2025 Papers & Highlights – Paper Digest","url":"https://www.paperdigest.org/2025/07/acl-2025-papers-highlights/"}]

Based on my web search results, I found relevant information about papers with those keywords at ACL 2024 and 2025:

## ACL 2024 Main Track Papers

ACL 2024 included papers such as "Rethinking Task-Oriented Dialogue Systems: From Complex Modularity to Zero-Shot Autonomous Agent" by Heng-Da Xu et al. and "How Johnny Can Persuade LLMs to Jailbreak Them: Rethinking Persuasion to Challenge AI Safety by Humanizing LLMs" by Yi Zeng et al. Additionally, "ConSiDERS-The-Human Evaluation Framework: Rethinking Human Evaluation for Generative Large Language Models" was accepted to ACL 2024 by Aparna Elangovan et al.

In ACL 2024 short papers, there was "Revisiting Code Similarity Evaluation with Abstract Syntax Tree Edit Distance" by Yewei Song et al., which revisits recent code similarity evaluation metrics, particularly focusing on the application of Abstract Syntax Tree (AST) editing distance in diverse programming languages.

## ACL 2025 Main Conference

Notably, ACL 2025 has a goal of a diverse technical program—in addition to traditional research results, papers may contribute negative findings, survey an area, announce the creation of a new resource, argue a position, report novel linguistic insights derived using existing computational techniques, and reproduce, or fail to reproduce, previous results.

The search results indicate ACL conferences explicitly encourage submissions with negative findings and papers that fail to reproduce previous results as part of their diverse technical programs.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "bfb84b51-3ccf-4c27-9217-15fc205bf5c6",
  "isSidechain": true,
  "promptId": "d62aafe3-d75b-460d-a9bb-1b0f23cd5965",
  "agentId": "a2210751531ccd330",
  "type": "user",
  "uuid": "07748ddd-0749-4a8d-8f0f-e806c66b4396",
  "sourceToolAssistantUUID": "bfb84b51-3ccf-4c27-9217-15fc205bf5c6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/.claude/sessions/reviewer_e7517921",
  "sessionId": "5a74afe6-047b-48bc-9683-816dae74ac45",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "starry-mapping-hearth"
}
```

</details>

---

### Tool result

_source line 50 · 2026-05-19T03:01:41.582Z_

<details><summary>↩ Tool result · `toolu_01KBRfLhe55s4J3TXUTpUfsL`</summary>

```text
Web search results for query: ""Machine Learning Conferences Should Establish" "Refutations and Critiques" track arxiv 2025"

Links: [{"title":"[2506.19882] Position: Machine Learning Conferences Should Establish a \"Refutations and Critiques\" Track","url":"https://arxiv.org/abs/2506.19882"},{"title":"Position: Machine Learning Conferences Should Establish a \"Refutations and Critiques\" Track","url":"https://arxiv.org/pdf/2506.19882"},{"title":"Machine Learning Jun 2025","url":"https://www.arxiv.org/list/cs.LG/2025-06?skip=2050&show=250"},{"title":"Position: Machine Learning Conferences Should Establish a “Refutations and Critiques” Track","url":"https://arxiv.org/html/2506.19882v3"},{"title":"(PDF) Position: Machine Learning Conferences Should Establish a \"Refutations and Critiques\" Track","url":"https://www.researchgate.net/publication/393022185_Position_Machine_Learning_Conferences_Should_Establish_a_Refutations_and_Critiques_Track"},{"title":"A Case for a “Refutations and Critiques” Track in Statistics Journals","url":"https://arxiv.org/html/2509.03702v2"},{"title":"Position on LLM-Assisted Peer Review: Addressing Reviewer Gap through Mentoring and Feedback","url":"https://arxiv.org/html/2601.09182v1"},{"title":"Computers and Society Jun 2025","url":"https://arxiv.org/list/cs.CY/2025-06?skip=350&show=50"},{"title":"Computers and Society Jun 2025","url":"https://www.arxiv.org/list/cs.CY/2025-06?skip=325&show=100"}]

I found the paper you're looking for! Here are the search results:

"Position: Machine Learning Conferences Should Establish a 'Refutations and Critiques' Track" is a position paper that champions the creation of a "Refutations and Critiques" (R&C) Track within ML conferences to provide an official mechanism for the field to self-correct.

**Paper Details:**
- **ArXiv ID:** 2506.19882
- **Authors:** Rylan Schaeffer, Joshua Kazdan, Yegor Denisov-Blanch, Brando Miranda, Matthias Gerstgrasser, Susan Zhang, Andreas Haupt, Isha Gupta, Elyas Obbad, Jesse Dodge, Jessica Zosa Forde, Francesco Orabona, Sanmi Koyejo, and David Donoho
- **Posted:** June 24, 2025 (with updates through July 7, 2025)

**Key Proposal:**
The objective is to provide the community with a high-profile, reputable platform dedicated to the critical re-examination of prior research published in ML conferences, with researchers encouraged to submit responses and criticisms of others' research as well as of their own research.

**Paper Contents:**
The paper discusses key considerations including track design, review principles, potential pitfalls, and provides an illustrative example submission concerning a recent ICLR 2025 Oral.

The paper is available on arXiv at: https://arxiv.org/abs/2506.19882


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c22dda26-9e6a-43a8-a608-b029429dcfde",
  "isSidechain": true,
  "promptId": "d62aafe3-d75b-460d-a9bb-1b0f23cd5965",
  "agentId": "a2210751531ccd330",
  "type": "user",
  "uuid": "fa6478d0-cd3d-4fd4-86f1-eccc22d2774d",
  "sourceToolAssistantUUID": "c22dda26-9e6a-43a8-a608-b029429dcfde",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/.claude/sessions/reviewer_e7517921",
  "sessionId": "5a74afe6-047b-48bc-9683-816dae74ac45",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "starry-mapping-hearth"
}
```

</details>

---

### Assistant

_source line 51 · 2026-05-19T03:01:44.339Z_

Let me do one more round to get specific paper examples from the workshops and main tracks.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "fa6478d0-cd3d-4fd4-86f1-eccc22d2774d",
  "isSidechain": true,
  "agentId": "a2210751531ccd330",
  "requestId": "req_011CbBBY7vXZqE4kLGewgu2t",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "6f952704-7ecf-40ed-8384-3831a41e27d1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/.claude/sessions/reviewer_e7517921",
  "sessionId": "5a74afe6-047b-48bc-9683-816dae74ac45",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "starry-mapping-hearth",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BVxkw9zwpUtS1Ztc3cvfXS",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5577,
      "cache_read_input_tokens": 38920,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 5577,
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

_source line 52 · 2026-05-19T03:01:45.420Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_0157noo2nAeL7GDCD8mekM5Z`</summary>

```json
{
  "query": "insights-workshop.github.io 2025 accepted papers list titles"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6f952704-7ecf-40ed-8384-3831a41e27d1",
  "isSidechain": true,
  "agentId": "a2210751531ccd330",
  "requestId": "req_011CbBBY7vXZqE4kLGewgu2t",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "6527a47b-9f49-4c91-bb38-4a88c29057eb",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/.claude/sessions/reviewer_e7517921",
  "sessionId": "5a74afe6-047b-48bc-9683-816dae74ac45",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "starry-mapping-hearth",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BVxkw9zwpUtS1Ztc3cvfXS",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5577,
      "cache_read_input_tokens": 38920,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 5577,
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

_source line 53 · 2026-05-19T03:01:46.945Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01FyfoKWmK4qSGa7hu6nhQHT`</summary>

```json
{
  "query": "EMNLP 2024 main conference \"Are LLMs\" limitations failure analysis accepted paper"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6527a47b-9f49-4c91-bb38-4a88c29057eb",
  "isSidechain": true,
  "agentId": "a2210751531ccd330",
  "requestId": "req_011CbBBY7vXZqE4kLGewgu2t",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "0ec0246c-446a-41f0-96ea-002d2fd4d41e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/.claude/sessions/reviewer_e7517921",
  "sessionId": "5a74afe6-047b-48bc-9683-816dae74ac45",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "starry-mapping-hearth",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BVxkw9zwpUtS1Ztc3cvfXS",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5577,
      "cache_read_input_tokens": 38920,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 5577,
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

_source line 54 · 2026-05-19T03:01:47.364Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_014sCHSSBtTgUc8iHkgNnjyo`</summary>

```json
{
  "query": "negative results NLP \"what makes\" publishable \"burden of proof\" \"thorough analysis\" community value"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0ec0246c-446a-41f0-96ea-002d2fd4d41e",
  "isSidechain": true,
  "agentId": "a2210751531ccd330",
  "requestId": "req_011CbBBY7vXZqE4kLGewgu2t",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "09c1210d-04b3-481a-bc13-83298df47acf",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/.claude/sessions/reviewer_e7517921",
  "sessionId": "5a74afe6-047b-48bc-9683-816dae74ac45",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "starry-mapping-hearth",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BVxkw9zwpUtS1Ztc3cvfXS",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5577,
      "cache_read_input_tokens": 38920,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 5577,
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

_source line 55 · 2026-05-19T03:01:49.888Z_

<details><summary>↩ Tool result · `toolu_0157noo2nAeL7GDCD8mekM5Z`</summary>

```text
Web search results for query: "insights-workshop.github.io 2025 accepted papers list titles"

Links: [{"title":"Accepted papers | Insights 2024","url":"https://insights-workshop.github.io/2025/accepted/"},{"title":"General Information | Workshop on Actionable Interpretability@ICML 2025","url":"https://actionable-interpretability.github.io/"},{"title":"SCOPE Workshop @ ICLR 2025","url":"https://scope-workshop.github.io/accepted_paper.html"},{"title":"Thank you to our 2025 reviewers","url":"https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12921489/"},{"title":"CFP | Insights 2024","url":"https://insights-workshop.github.io/2025/cfp/"},{"title":"Insights 2024 | Workshop on Insights from Negative Results in NLP","url":"https://insights-workshop.github.io/"},{"title":"Workshop on Insights from Negative Results in NLP | Insights 2024","url":"https://insights-workshop.github.io/index"},{"title":"Program | Insights 2024","url":"https://insights-workshop.github.io/2025/program/"}]

Based on the search results, I found information about the Insights 2025 workshop accepted papers. The Workshop on Insights from Negative Results in NLP is being held in Albuquerque, New Mexico, May 2025 (co-located with NAACL).

The search results show some of the accepted paper titles from the program, including:

- "Reassessing Graph Linearization for Sequence-to-sequence AMR Parsing: On the Advantages and Limitations of Triple-Based" by Jeongwoo Kang, Maximin Coavoux, Didier Schwab and Cédric Lopez
- "Do Prevalent Bias Metrics Capture Allocational Harms from LLMs?" by Hannah Cyberey, Yangfeng Ji and David Evans
- "Language-Specific Neurons Do Not Facilitate Cross-Lingual Transfer" by Soumen Kumar Mondal, Sayambhu Sen, Abhishek Singhania and Preethi Jyothi
- "Monte Carlo Sampling for Analyzing In-Context Examples" by Stephanie Schoch and Yangfeng Ji
- "Bridging the Faithfulness Gap in Prototypical Models" by Andrew Koulogeorge, Sean Xie, Saeed Hassanpour and Soroush Vosoughi
- "Exploring Limitations of LLM Capabilities with Multi-Problem Evaluation" by Zhengxiang Wang, Jordan Kodner and Owen Rambow

For the complete list of all accepted papers, you can visit the official accepted papers page at https://insights-workshop.github.io/2025/accepted/


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "6527a47b-9f49-4c91-bb38-4a88c29057eb",
  "isSidechain": true,
  "promptId": "d62aafe3-d75b-460d-a9bb-1b0f23cd5965",
  "agentId": "a2210751531ccd330",
  "type": "user",
  "uuid": "13917d31-767e-476d-86d1-bdffdce90f78",
  "sourceToolAssistantUUID": "6527a47b-9f49-4c91-bb38-4a88c29057eb",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/.claude/sessions/reviewer_e7517921",
  "sessionId": "5a74afe6-047b-48bc-9683-816dae74ac45",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "starry-mapping-hearth"
}
```

</details>

---

### Tool result

_source line 56 · 2026-05-19T03:01:52.984Z_

<details><summary>↩ Tool result · `toolu_01FyfoKWmK4qSGa7hu6nhQHT`</summary>

```text
Web search results for query: "EMNLP 2024 main conference "Are LLMs" limitations failure analysis accepted paper"

Links: [{"title":"The 2024 Conference on Empirical Methods in Natural Language Processing","url":"https://www.kitware.com/the-2024-conference-on-empirical-methods-in-natural-language-processing/"},{"title":"Knowledge Conflicts for LLMs: A Survey - ACL Anthology","url":"https://aclanthology.org/2024.emnlp-main.486/"},{"title":"Main Conference - EMNLP 2024","url":"https://2024.emnlp.org/program/accepted_main_conference/"},{"title":"Understanding LLM Failures: A Multi-Tape Turing Machine Analysis of Systematic Errors in Language Model Reasoning","url":"https://arxiv.org/pdf/2602.15868"},{"title":"Efficient Solutions For An Intriguing Failure of LLMs: Long Context   Window Does Not Mean LLMs Can Analyze Long Sequences Flawlessly","url":"https://arxiv.org/pdf/2408.01866"},{"title":"The 2024 Conference on Empirical Methods in Natural Language Processing - ACL Anthology","url":"https://aclanthology.org/events/emnlp-2024/"},{"title":"Stalled, Biased, and Confused: Uncovering Reasoning Failures in LLMs for Cloud-Based Root Cause Analysis","url":"https://arxiv.org/pdf/2601.22208"}]

Based on the search results, I found information about EMNLP 2024 papers related to LLM limitations and failure analysis. However, I did not find a specific paper with the exact title starting with "Are LLMs" in the main conference proceedings.

The search results show several related EMNLP 2024 main conference papers that examine LLM limitations and failures:

1. A survey on "Knowledge Conflicts for LLMs" which provides an in-depth analysis of knowledge conflicts large language models encounter when blending contextual and parametric knowledge.

2. A paper on "Defending Against Social Engineering Attacks in the Age of LLMs" which explores challenges posed by LLMs in detecting and preventing digital deception, finding that while LLMs can generate convincing content, their ability to detect such threats is limited.

The general EMNLP 2024 main conference program listing also appears to include other papers examining LLM capabilities and limitations, though the specific paper with the "Are LLMs" title you mentioned was not found in these results. If you have more specific details about the paper (such as authors or a more precise title), I could search for more targeted results.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "0ec0246c-446a-41f0-96ea-002d2fd4d41e",
  "isSidechain": true,
  "promptId": "d62aafe3-d75b-460d-a9bb-1b0f23cd5965",
  "agentId": "a2210751531ccd330",
  "type": "user",
  "uuid": "1b2ece1c-3596-481a-9694-c6cc59aab484",
  "sourceToolAssistantUUID": "0ec0246c-446a-41f0-96ea-002d2fd4d41e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/.claude/sessions/reviewer_e7517921",
  "sessionId": "5a74afe6-047b-48bc-9683-816dae74ac45",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "starry-mapping-hearth"
}
```

</details>

---

### Tool result

_source line 57 · 2026-05-19T03:01:53.909Z_

<details><summary>↩ Tool result · `toolu_014sCHSSBtTgUc8iHkgNnjyo`</summary>

```text
Web search results for query: "negative results NLP "what makes" publishable "burden of proof" "thorough analysis" community value"

Links: [{"title":"[CFP] The Third Workshop on Insights from Negative Results in NLP (ACL 2022)","url":"https://groups.google.com/g/ml-news/c/c47GCEdW1L0"},{"title":"The Third Workshop on Insights from Negative Results in NLP | ACL Member Portal","url":"https://www.aclweb.org/portal/content/third-workshop-insights-negative-results-nlp-0"},{"title":"Workshop on Insights from Negative Results in NLP | ACL Member Portal","url":"https://www.aclweb.org/portal/content/workshop-insights-negative-results-nlp"},{"title":"Workshop on Insights from Negative Results | ACL Member Portal","url":"https://www.aclweb.org/portal/content/workshop-insights-negative-results"},{"title":"CFP | Insights 2024","url":"https://insights-workshop.github.io/2021/cfp/"},{"title":"Call For Papers: The Second Workshop on Insights from Negative Results (EMNLP 2021) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/call-papers-second-workshop-insights-negative-results-emnlp-2021-0"},{"title":"Publishing Negative Results in Machine Learning is like Proving Dragons don’t Exist","url":"https://luckytoilet.wordpress.com/2018/03/07/publishing-negative-results-in-machine-learning-is-like-proving-dragons-dont-exist/"},{"title":"Proceedings of the Third Workshop on Insights from Negative Results in NLP - ACL Anthology","url":"https://aclanthology.org/volumes/2022.insights-1/"},{"title":"Guest Post: Reproducibility at EMNLP 2020","url":"https://2020.emnlp.org/blog/2020-05-20-reproducibility/"}]

Based on the web search results, I found relevant information about what makes negative results publishable in NLP research:

Publishing negative results is not easy, partly because the author has the burden of proof that something truly does not work, rather than is caused by a bug.

To overcome this challenge, a successful negative results paper would contribute experiments on stability of previously published results, ablation studies of model components, datasets or probing tasks showing that previous approaches do not generalize to other domains, extensions or annotations of existing datasets which show that prior successes are due to spurious statistical factors or annotation artifacts, among other contributions.

The broader context shows that publication of negative results is difficult in NLP due to the near-universal focus on improvements in benchmarks, which implicitly discourages hypothesis-driven research and increases time and carbon emissions spent on model development since researchers have no opportunity to learn what has already been tried and failed.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "09c1210d-04b3-481a-bc13-83298df47acf",
  "isSidechain": true,
  "promptId": "d62aafe3-d75b-460d-a9bb-1b0f23cd5965",
  "agentId": "a2210751531ccd330",
  "type": "user",
  "uuid": "1deff30d-1945-4350-9d81-20e8f3a66bd8",
  "sourceToolAssistantUUID": "09c1210d-04b3-481a-bc13-83298df47acf",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/.claude/sessions/reviewer_e7517921",
  "sessionId": "5a74afe6-047b-48bc-9683-816dae74ac45",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "starry-mapping-hearth"
}
```

</details>

---

### Assistant

_source line 58 · 2026-05-19T03:01:57.033Z_

Now let me fetch the actual workshop page to get the complete Insights 2025 paper list.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1deff30d-1945-4350-9d81-20e8f3a66bd8",
  "isSidechain": true,
  "agentId": "a2210751531ccd330",
  "requestId": "req_011CbBBZ2dKF2xfLQB5Magmu",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "6d59b00c-18d8-41b0-8a9a-43e67ac51c51",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/.claude/sessions/reviewer_e7517921",
  "sessionId": "5a74afe6-047b-48bc-9683-816dae74ac45",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "starry-mapping-hearth",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EWzyshfAiphiKz3vQqzz6o",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2354,
      "cache_read_input_tokens": 44497,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2354,
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

_source line 59 · 2026-05-19T03:01:57.592Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Pwy7X9JSbKWn4RHSf2TiWA`</summary>

```json
{
  "query": "site:aclanthology.org \"2025.insights-1\" proceedings papers"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6d59b00c-18d8-41b0-8a9a-43e67ac51c51",
  "isSidechain": true,
  "agentId": "a2210751531ccd330",
  "requestId": "req_011CbBBZ2dKF2xfLQB5Magmu",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "2b8a33e1-7fcc-4fbf-a7a7-76845bf08cbd",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/.claude/sessions/reviewer_e7517921",
  "sessionId": "5a74afe6-047b-48bc-9683-816dae74ac45",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "starry-mapping-hearth",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EWzyshfAiphiKz3vQqzz6o",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2354,
      "cache_read_input_tokens": 44497,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2354,
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

_source line 60 · 2026-05-19T03:01:58.663Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01WyzWvUBpTsgybY9hkbnR9k`</summary>

```json
{
  "query": "EMNLP 2025 main accepted paper \"does not\" OR \"fail\" OR \"limitation\" OR \"negative\" OR \"rethinking\" title list"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2b8a33e1-7fcc-4fbf-a7a7-76845bf08cbd",
  "isSidechain": true,
  "agentId": "a2210751531ccd330",
  "requestId": "req_011CbBBZ2dKF2xfLQB5Magmu",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "2e7c8e7c-1c06-4b7e-8c3d-85f75100abbc",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/.claude/sessions/reviewer_e7517921",
  "sessionId": "5a74afe6-047b-48bc-9683-816dae74ac45",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "starry-mapping-hearth",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EWzyshfAiphiKz3vQqzz6o",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2354,
      "cache_read_input_tokens": 44497,
      "output_tokens": 161,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2354
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 161,
          "cache_read_input_tokens": 44497,
          "cache_creation_input_tokens": 2354,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2354,
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

_source line 61 · 2026-05-19T03:02:02.826Z_

<details><summary>↩ Tool result · `toolu_01Pwy7X9JSbKWn4RHSf2TiWA`</summary>

```text
Web search results for query: "site:aclanthology.org "2025.insights-1" proceedings papers"

Links: [{"title":"Proceedings of the 2025 Conference of the Nations of the Americas Chapter of the Association for Computational Linguistics: Human Language Technologies (Volume 1: Long Papers) - ACL Anthology","url":"https://aclanthology.org/volumes/2025.naacl-long/"},{"title":"The 2025 Conference on Empirical Methods in Natural Language Processing - ACL Anthology","url":"https://aclanthology.org/events/emnlp-2025/"},{"title":"Inferring Functionality of Attention Heads from their Parameters - ACL Anthology","url":"https://aclanthology.org/2025.acl-long.866/"},{"title":"MT-RAIG: Novel Benchmark and Evaluation Framework for Retrieval-Augmented Insight Generation over Multiple Tables - ACL Anthology","url":"https://aclanthology.org/2025.acl-long.1128/"},{"title":"Proceedings of the 19th International Workshop on Semantic Evaluation (SemEval-2025) - ACL Anthology","url":"https://aclanthology.org/volumes/2025.semeval-1/"}]

The search results don't show a specific "2025.insights-1" proceedings. The results returned are for other 2025 ACL events like NAACL, EMNLP, SemEval, and the main ACL conference, but not for a proceedings identifier matching "2025.insights-1."

It's possible that:
1. The "Insights" workshop or conference hasn't been indexed yet at aclanthology.org
2. The proceedings identifier might be slightly different
3. The event might not have published proceedings on the ACL Anthology yet

If you're looking for a specific workshop or conference called "Insights," could you provide more details about it so I can search more effectively?


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "2b8a33e1-7fcc-4fbf-a7a7-76845bf08cbd",
  "isSidechain": true,
  "promptId": "d62aafe3-d75b-460d-a9bb-1b0f23cd5965",
  "agentId": "a2210751531ccd330",
  "type": "user",
  "uuid": "c59253c2-7c4b-4c4f-a871-ae8ed28dbdac",
  "sourceToolAssistantUUID": "2b8a33e1-7fcc-4fbf-a7a7-76845bf08cbd",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/.claude/sessions/reviewer_e7517921",
  "sessionId": "5a74afe6-047b-48bc-9683-816dae74ac45",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "starry-mapping-hearth"
}
```

</details>

---

### Tool result

_source line 62 · 2026-05-19T03:02:18.149Z_

<details><summary>↩ Tool result · `toolu_01WyzWvUBpTsgybY9hkbnR9k`</summary>

```text
Web search results for query: "EMNLP 2025 main accepted paper "does not" OR "fail" OR "limitation" OR "negative" OR "rethinking" title list"

Links: [{"title":"Accepted Main Conference Papers - EMNLP 2025","url":"https://2025.emnlp.org/program/main_papers/"},{"title":"6 papers were accepted at EMNLP 2025 | Center for Advanced Intelligence Project","url":"https://aip.riken.jp/news/emnlp2025/"},{"title":"Paper Digest: EMNLP 2025 Papers & Highlights – Paper Digest","url":"https://www.paperdigest.org/2025/11/emnlp-2025-papers-highlights/"},{"title":"Our EMNLP 2025 Papers – Center for Research in Computer Vision","url":"https://www.crcv.ucf.edu/2025/09/04/our-emnlp-2025-papers/"},{"title":"Paper Digest: EMNLP 2025 Papers & Highlights – Resources | Paper Digest","url":"https://resources.paperdigest.org/2025/11/emnlp-2025-papers-highlights/"},{"title":"EMNLP 2025 Highlights. I just got back from EMNLP 2025 in… | by Itay Nakash | Medium","url":"https://medium.com/@itaynakash/emnlp-2025-highlights-1d2bca37cc7a"},{"title":"Three papers accepted to EMNLP 2025: similarity, change ...","url":"https://www.linkedin.com/posts/danushka-bollegala-6a636516_emnlp2025-activity-7365688277468618752-pl54"},{"title":"EMNLP.2025 | Cool Papers - Immersive Paper Discovery","url":"https://papers.cool/venue/EMNLP.2025"}]

I found the official EMNLP 2025 accepted main papers page. Let me search more specifically for papers with the keywords you mentioned in their titles.

Links: [{"title":"HalluCitation Matters: Revealing the Impact of Hallucinated References with 300 Hallucinated Papers in ACL Conferences","url":"https://arxiv.org/pdf/2601.18724"},{"title":"Natural language processing for humanitarian action: Opportunities, challenges, and the path toward humanitarian NLP","url":"https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10080095/"},{"title":"Thank you to our 2025 reviewers","url":"https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12921489/"},{"title":"Evaluation of Finetuned LLMs in AMR Parsing","url":"https://arxiv.org/pdf/2508.05028"},{"title":"Enhancing Entity Aware Machine Translation with Multi-task Learning","url":"https://arxiv.org/pdf/2506.18318"}]

Links: [{"title":"Accepted Main Conference Papers - EMNLP 2025","url":"https://2025.emnlp.org/program/main_papers/"},{"title":"Accepted Findings Papers - EMNLP 2025","url":"https://2025.emnlp.org/program/find_papers/"},{"title":"MCML - MCML at EMNLP 2025","url":"https://mcml.ai/news/2025-11-03-papers-emnlp2025/"},{"title":"Carnegie Mellon University at EMNLP 2025 – Machine Learning Blog | ML@CMU | Carnegie Mellon University","url":"https://blog.ml.cmu.edu/2025/11/08/carnegie-mellon-university-at-emnlp-2025/"},{"title":"Main Conference - EMNLP 2023","url":"https://2023.emnlp.org/program/accepted_main_conference/"},{"title":"HalluCitation Matters: Revealing the Impact of Hallucinated References with 300 Hallucinated Papers in ACL Conferences","url":"https://arxiv.org/pdf/2601.18724"}]

Links: [{"title":"Our EMNLP 2025 Papers – Center for Research in Computer Vision","url":"https://www.crcv.ucf.edu/2025/09/04/our-emnlp-2025-papers/"},{"title":"Call for Main Conference Papers - EMNLP 2025","url":"https://2025.emnlp.org/calls/main_conference_papers/"},{"title":"[EMNLP 2025] Call for Main Conference Papers","url":"https://groups.google.com/g/ml-news/c/HKZ_H_iiM_A"},{"title":"[EMNLP 2025] First Call for Papers | ACL Member Portal","url":"https://www.aclweb.org/portal/content/emnlp-2025-first-call-papers"},{"title":"Our EMNLP 2025 Papers - Institute of Artificial Intelligence","url":"https://ai.ucf.edu/our-emnlp-2025-papers/"},{"title":"EMNLP.2025 | Cool Papers - Immersive Paper Discovery","url":"https://papers.cool/venue/EMNLP.2025"},{"title":"Findings of the Association for Computational Linguistics: EMNLP 2025 - ACL Anthology","url":"https://aclanthology.org/volumes/2025.findings-emnlp/"}]

Based on my web search results, I found several EMNLP 2025 main conference papers with titles containing the keywords you specified:

**Papers with "Rethinking" in title:**

- "Rethinking Cross-Subject Data Splitting for Brain-to-Text Decoding" by Congchi Yin, Qian Yu, Zhiwei Fang, Changping Peng, Piji Li
- "Humanizing Machines: Rethinking LLM Anthropomorphism Through a Multi-Level Framework of Design" by Yunze Xiao, Lynnette Hui Xian Ng, Jiarui Liu, Mona T. Diab

- "LegalSearchLM: Rethinking Legal Case Retrieval as Legal Elements Generation" by Chaeeun Kim, Jinu Lee, Wonseok Hwang

- "ReEvalMed: Rethinking Medical Report Evaluation by Aligning Metrics with Real-World Clinical Judgment" by R. Li, J. Jian, K. Yuan, Y. Zhu

**Papers with "Generative Models" and "Underconfident":**

- "Are Generative Models Underconfident?" by Tu Anh Dinh, Jan Niehues

**Papers with question phrases similar to your search terms:**

- "Why Do Some Inputs Break Low-Bit LLM Quantization?" by Ting-Yun Chang, Muru Zhang, Jesse Thomason, Robin Jia

The official EMNLP 2025 main papers page at 2025.emnlp.org/program/main_papers/ contains the complete list of all accepted papers. While I found papers with "rethinking" in their titles, a comprehensive search for all papers matching your specific keyword combination ("does not" OR "fail" OR "limitation" OR "negative" OR "rethinking") would require direct access to the full paper listing with title search functionality on the official conference website.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "2e7c8e7c-1c06-4b7e-8c3d-85f75100abbc",
  "isSidechain": true,
  "promptId": "d62aafe3-d75b-460d-a9bb-1b0f23cd5965",
  "agentId": "a2210751531ccd330",
  "type": "user",
  "uuid": "16b0ae1e-e970-49c7-8503-69bb5de1130a",
  "sourceToolAssistantUUID": "2e7c8e7c-1c06-4b7e-8c3d-85f75100abbc",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/.claude/sessions/reviewer_e7517921",
  "sessionId": "5a74afe6-047b-48bc-9683-816dae74ac45",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "starry-mapping-hearth"
}
```

</details>

---

### Assistant

_source line 63 · 2026-05-19T03:03:21.890Z_

I now have sufficient information to compile a comprehensive report. Here is the synthesis:

---

## 报告：NLP 顶会负面结果论文的接收情况与模式

### 一、各会议对负面结果的官方态度

**ACL/EMNLP/NAACL 统一通过 ACL Rolling Review (ARR) 投稿，CFP 原文明确列出负面结果为合法贡献类型：**

> "Papers may contribute negative findings, survey an area, announce the creation of a new resource, argue a position, report novel linguistic insights derived using existing computational techniques, and reproduce, or fail to reproduce, previous results."

ARR 进一步说明负面结果论文的定义：
> "A negative results paper might report on non-reproducibility or non-generalizability of previously published results, their misattribution ('right for the wrong reasons'), or present an idea that seemed great (for well-justified reasons), but didn't work."

ARR 还将负面结果论文明确列为 short paper 的常见类型之一，但也说明 long paper 同样可以。

**结论：ACL/EMNLP/NAACL 主会和 Findings 均接收负面结果论文，这不是例外而是 CFP 明文鼓励的贡献类型。**

---

### 二、专门的负面结果 Workshop

**"Insights from Negative Results in NLP" (Insights Workshop)** 是 ACL 社区的旗舰负面结果工作坊，已连续举办六届：

| 届次 | 年份 | 依附会议 | 论文数 | 接收率 |
|------|------|----------|--------|--------|
| 5th | 2024 | EACL 2024 (Malta) | 20篇 | 57.5% (19 short papers) |
| 6th | 2025 | NAACL 2025 (Albuquerque) | 16篇 | 64% (23 submissions) |
| 7th | 2026 | EMNLP 2026 (Budapest, 10月) | 待定 | — |

**Insights 2025 接收论文具体例子（NAACL 2025 workshop）：**
- "Language-Specific Neurons Do Not Facilitate Cross-Lingual Transfer" — Soumen Kumar Mondal et al. 证明语言特定神经元并不促进跨语言迁移
- "Do Prevalent Bias Metrics Capture Allocational Harms from LLMs?" — Hannah Cyberey et al. 质疑流行偏见指标能否捕捉 LLM 的分配性损害
- "Exploring Limitations of LLM Capabilities with Multi-Problem Evaluation" — Zhengxiang Wang et al. 探索 LLM 能力限制
- "Bridging the Faithfulness Gap in Prototypical Models" — Andrew Koulogeorge et al.
- "Monte Carlo Sampling for Analyzing In-Context Examples" — Stephanie Schoch, Yangfeng Ji

---

### 三、主会/Findings 接收的负面结果论文实例

**EMNLP 2024 Findings:**
- **"Insights into LLM Long-Context Failures: When Transformers Know but Don't Tell"** (Muhan Gao et al.) — 发现 LLM 虽然在隐藏表示中编码了目标信息位置，但在生成回答时经常无法利用这些信息，揭示了 "知道但不说" 现象。ACL Anthology: `2024.findings-emnlp.447`

**EMNLP 2025 Main Conference (含质疑/重新审视类论文):**
- "Are Generative Models Underconfident?" — Tu Anh Dinh, Jan Niehues
- "Why Do Some Inputs Break Low-Bit LLM Quantization?" — Ting-Yun Chang et al.
- 多篇 "Rethinking..." 类论文（如 "Rethinking Cross-Subject Data Splitting for Brain-to-Text Decoding"）

---

### 四、成功负面结果论文的贡献模式

综合 Insights Workshop CFP、ICML 2024 Position Paper (Karl et al., "Position: Embracing Negative Results in Machine Learning")、以及 ARR 指南，可发表的负面结果论文通常符合以下模式之一：

**A. 七类公认贡献（Insights Workshop CFP 原文）：**
1. **稳定性实验** — 硬件差异或随机初始化导致的结果不稳定
2. **消融研究** — 证明组件贡献与原论文声称不同
3. **泛化性失败** — 新数据集或 probing task 证明已有方法不泛化
4. **虚假统计因素** — 数据集扩展/标注揭示先前成功源于统计伪相关或标注artifact
5. **预训练 vs 微调贡献分离** — 区分预训练和微调各自的真实贡献
6. **跨语言研究** — 技术只在某些语言有效
7. **广泛适用的训练/微调建议** — 基于负面结果提炼出实操指南

**B. ICML 2024 Position Paper 提出的三个可发表性标准：**
1. **实验设计严谨性 (Experimental rigor)** — 与正面结果论文要求完全相同，控制变量、多 seed、公平 baseline
2. **惊奇度 (Surprise factor)** — 如果结果非常可预见则发表价值低；违反直觉的失败更有价值
3. **分析深度 (Depth of analysis)** — 仅报告"不work"远远不够，**必须深入分析为什么不 work**，这是关键区分点

**C. 核心难点（社区共识）：**
> "Publishing negative results is not easy, partly because the author has the burden of proof that something truly does not work, rather than is caused by a bug."

即：负面结果论文的举证责任比正面结果论文更重。审稿人会质疑：是方法真的不行，还是你实现有 bug？因此需要更充分的消融、多配置验证、代码细节。

---

### 五、相关立场论文与社区讨论

1. **"Position: Embracing Negative Results in Machine Learning"** (Karl et al., ICML 2024 Poster) — 系统论证为什么只用预测性能评价论文价值是有害的，提出负面结果分类法(NMNR: Novel Method Negative Results; EMNR: Existing Method Negative Results)和评审流程改革建议。 `arxiv:2406.03980`

2. **"LLMs Have Made Failure Worth Publishing"** (Sungmin Lee, arXiv 2026.04) — 论证在 LLM 时代负面结果数据更加重要：(a) LLM 训练数据中正面结果偏见导致模型对科学判断的系统性偏差；(b) 高质量训练数据短缺加剧；(c) LLM 作为审稿工具时继承了正面偏见。 `arxiv:2604.06236`

3. **"Position: Machine Learning Conferences Should Establish a 'Refutations and Critiques' Track"** (Schaeffer, Donoho et al., arXiv 2025.06) — 提议 ML 会议设立 R&C track 作为正式的自我纠错机制。 `arxiv:2506.19882`

---

### 六、对本项目的启示

如果 turn_residual_gating 实验产生了负面结果（gating 机制未带来预期提升），以下是可发表性的关键要素：

1. **不能只说"不 work"** — 必须有深入的 why-not 分析（哪些条件下失败、failure mode 是什么）
2. **消融要充分** — 多配置、多 seed、公平 baseline，排除实现 bug 的可能
3. **惊奇度** — 如果社区普遍认为 residual gating 应该 work（有理论或先验预期），那失败本身就有 surprise value
4. **可操作的 insight** — 提炼出"什么时候不该用 gating"的指导性结论
5. **投稿路径** — 主会 Findings 可接收；Insights Workshop (EMNLP 2026, Budapest) 是专门渠道且接收率 ~60%

Sources:
- [ACL Rolling Review CFP](http://aclrollingreview.org/cfp)
- [EMNLP 2025 Call for Papers](https://2025.emnlp.org/calls/main_conference_papers/)
- [NAACL 2025 Call for Papers](https://2025.naacl.org/calls/papers/)
- [Insights 2025 Workshop (NAACL)](https://insights-workshop.github.io/2025/accepted/)
- [Insights 2024 Workshop - ACL Anthology](https://aclanthology.org/events/insights-2024/)
- [Insights 2025 Proceedings - ACL Anthology](https://aclanthology.org/volumes/2025.insights-1/)
- [Position: Embracing Negative Results in ML (ICML 2024)](https://arxiv.org/abs/2406.03980)
- [LLMs Have Made Failure Worth Publishing](https://arxiv.org/html/2604.06236v1)
- [Position: ML Conferences Should Establish R&C Track](https://arxiv.org/abs/2506.19882)
- [Insights into LLM Long-Context Failures (EMNLP 2024 Findings)](https://aclanthology.org/2024.findings-emnlp.447/)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "16b0ae1e-e970-49c7-8503-69bb5de1130a",
  "isSidechain": true,
  "agentId": "a2210751531ccd330",
  "requestId": "req_011CbBBapNgES8sKY8UiESHy",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "54301f08-6ab5-469b-be96-50759eeaadbd",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/.claude/sessions/reviewer_e7517921",
  "sessionId": "5a74afe6-047b-48bc-9683-816dae74ac45",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "starry-mapping-hearth",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Pp3WAjy1njfLAvxRFwrnU5",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2679,
      "cache_read_input_tokens": 46851,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2679,
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
