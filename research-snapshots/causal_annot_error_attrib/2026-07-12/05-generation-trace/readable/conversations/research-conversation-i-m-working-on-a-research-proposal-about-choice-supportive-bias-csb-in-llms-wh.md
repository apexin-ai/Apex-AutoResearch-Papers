# Research conversation: I'm working on a research proposal about choice-supportive bias (CSB) in LLMs - where models show inflated confidence in

**Multi-Class Annotation Errors in Causal Inference: Topology-Dependent Bias, Sensitivity, and Correction (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 54
- **Recorded user turns:** 1
- **Tool calls:** 22
- **Original source:** `logs/chats/exported-trajectories/account-2/agent-acf334e31648c11ee.jsonl`
- **Structured JSON:** [`65e84f4b8ab02ec9c2a2.json`](../../sessions/65/65e84f4b8ab02ec9c2a2.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

54 recorded events

### User

_source line 1 · 2026-05-19T15:00:22.356Z_

I'm working on a research proposal about choice-supportive bias (CSB) in LLMs - where models show inflated confidence in their own previously selected answers. A reviewer raised a concern about source attribution confounds: when we present "your answer was X" vs. "another LLM's answer was X" (same content, different attribution), the model may process self-attributed vs. externally-attributed content differently for reasons beyond bias activation.

Use WebSearch to research:

1. **Self-recognition in LLMs**: Do LLMs process self-generated content differently from externally-attributed content? Search for "LLM self-recognition", "LLM self-generated text detection", "self-other distinction LLM".

2. **Self-preference bias**: Search for "self-preference bias LLM" and "LLM judge self-preference". I know there's a paper "Breaking the Mirror: Activation-Based Mitigation of Self-Preference in LLM Evaluators" (arXiv 2509.03647) - try to find details on this.

3. **Attribution effects**: Search for "source attribution LLM behavior" or "attribution bias LLM" - do models respond differently to information attributed to different sources?

4. **Ownership bias in LLMs**: Search for "ownership bias LLM" or "endowment effect LLM".

I need this to design a proper confound control condition where the model's own answer is attributed to "another LLM" to isolate the self-attribution aspect. Understanding what's known about how LLMs process attribution information will help me design this correctly.

Report detailed findings with specific references.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "3391dbdc-780b-4b93-88ca-869d11e621ba",
  "agentId": "acf334e31648c11ee",
  "type": "user",
  "uuid": "03a51d14-e5dd-4a93-95b2-ede3d46d6b4b",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "64cca947-8ca5-4bec-bd98-7391dafb8fbe",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 2 · 2026-05-19T15:00:22.359Z_

```json
{
  "parentUuid": "03a51d14-e5dd-4a93-95b2-ede3d46d6b4b",
  "isSidechain": true,
  "agentId": "acf334e31648c11ee",
  "attachment": {
    "type": "deferred_tools_delta",
    "addedNames": [
      "EnterWorktree",
      "ExitWorktree",
      "Monitor",
      "NotebookEdit",
      "TaskStop",
      "WebFetch",
      "WebSearch"
    ],
    "addedLines": [
      "EnterWorktree",
      "ExitWorktree",
      "Monitor",
      "NotebookEdit",
      "TaskStop",
      "WebFetch",
      "WebSearch"
    ],
    "removedNames": [],
    "readdedNames": []
  },
  "type": "attachment",
  "uuid": "793a3ebd-eedd-4bc5-97f9-26d2d2a78575",
  "timestamp": "2026-05-19T15:00:22.359Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "64cca947-8ca5-4bec-bd98-7391dafb8fbe",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 3 · 2026-05-19T15:00:22.361Z_

```json
{
  "parentUuid": "793a3ebd-eedd-4bc5-97f9-26d2d2a78575",
  "isSidechain": true,
  "agentId": "acf334e31648c11ee",
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "f08ce612-9581-450e-91c8-4474dabda8e4",
  "timestamp": "2026-05-19T15:00:22.361Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "64cca947-8ca5-4bec-bd98-7391dafb8fbe",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Assistant

_source line 4 · 2026-05-19T15:00:25.426Z_



I'll conduct a systematic search across all four areas. Let me start by loading the WebSearch tool and then running searches in parallel.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f08ce612-9581-450e-91c8-4474dabda8e4",
  "isSidechain": true,
  "agentId": "acf334e31648c11ee",
  "requestId": "req_011CbC8Ljk8TxVNoPDNqqzGc",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "ff24bc48-8599-4ea8-9c25-304dd7caeefa",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "64cca947-8ca5-4bec-bd98-7391dafb8fbe",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XAW5iGa7BrvNjMuzWpgRMj",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1681,
      "cache_read_input_tokens": 7409,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1681,
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

_source line 5 · 2026-05-19T15:00:25.834Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01XtihTjPmDVN3fcBvtpyQx5`</summary>

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
  "parentUuid": "ff24bc48-8599-4ea8-9c25-304dd7caeefa",
  "isSidechain": true,
  "agentId": "acf334e31648c11ee",
  "requestId": "req_011CbC8Ljk8TxVNoPDNqqzGc",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "82426a84-77cd-485b-a283-6a5703f0a109",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "64cca947-8ca5-4bec-bd98-7391dafb8fbe",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XAW5iGa7BrvNjMuzWpgRMj",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1681,
      "cache_read_input_tokens": 7409,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1681,
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

### Tool result

_source line 6 · 2026-05-19T15:00:25.837Z_

<details><summary>↩ Tool result · `toolu_01XtihTjPmDVN3fcBvtpyQx5`</summary>

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
  "parentUuid": "82426a84-77cd-485b-a283-6a5703f0a109",
  "isSidechain": true,
  "promptId": "3391dbdc-780b-4b93-88ca-869d11e621ba",
  "agentId": "acf334e31648c11ee",
  "type": "user",
  "uuid": "3b77482c-bc30-4386-ba1b-0dafabe8fcf9",
  "sourceToolAssistantUUID": "82426a84-77cd-485b-a283-6a5703f0a109",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "64cca947-8ca5-4bec-bd98-7391dafb8fbe",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 7 · 2026-05-19T15:00:28.472Z_



Now let me run the initial searches in parallel across all four research areas.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3b77482c-bc30-4386-ba1b-0dafabe8fcf9",
  "isSidechain": true,
  "agentId": "acf334e31648c11ee",
  "requestId": "req_011CbC8LzqV9iNHdJ1zkQ2Gv",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "2078ae66-1f30-4449-a471-eb96cd6981ee",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "64cca947-8ca5-4bec-bd98-7391dafb8fbe",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LzpVDgVZmaqdxXpY7BwKE9",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 634,
      "cache_read_input_tokens": 9090,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 634,
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

_source line 8 · 2026-05-19T15:00:29.030Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_014tbqXSaJ268LFNyiuKGT4q`</summary>

```json
{
  "query": "LLM self-recognition self-generated text detection self-other distinction"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2078ae66-1f30-4449-a471-eb96cd6981ee",
  "isSidechain": true,
  "agentId": "acf334e31648c11ee",
  "requestId": "req_011CbC8LzqV9iNHdJ1zkQ2Gv",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "5da9cbd8-df70-4595-ad42-3cab6df92c82",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "64cca947-8ca5-4bec-bd98-7391dafb8fbe",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LzpVDgVZmaqdxXpY7BwKE9",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 634,
      "cache_read_input_tokens": 9090,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 634,
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

_source line 9 · 2026-05-19T15:00:29.485Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01V4aGTVAh7f2wT2BXLFhj2z`</summary>

```json
{
  "query": "self-preference bias LLM judge evaluator"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5da9cbd8-df70-4595-ad42-3cab6df92c82",
  "isSidechain": true,
  "agentId": "acf334e31648c11ee",
  "requestId": "req_011CbC8LzqV9iNHdJ1zkQ2Gv",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "7c27680f-eda4-418e-a496-74d889b9428b",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "64cca947-8ca5-4bec-bd98-7391dafb8fbe",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LzpVDgVZmaqdxXpY7BwKE9",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 634,
      "cache_read_input_tokens": 9090,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 634,
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

_source line 10 · 2026-05-19T15:00:29.942Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01PrBFXFvDyZLQzCZH1KKVJT`</summary>

```json
{
  "query": "\"Breaking the Mirror\" self-preference LLM evaluators arXiv 2509.03647"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7c27680f-eda4-418e-a496-74d889b9428b",
  "isSidechain": true,
  "agentId": "acf334e31648c11ee",
  "requestId": "req_011CbC8LzqV9iNHdJ1zkQ2Gv",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "15dc7274-f3fa-4f90-9c19-4b14d8b02f13",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "64cca947-8ca5-4bec-bd98-7391dafb8fbe",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LzpVDgVZmaqdxXpY7BwKE9",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 634,
      "cache_read_input_tokens": 9090,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 634,
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

_source line 11 · 2026-05-19T15:00:30.414Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_0131359x7s5Y7ejwUdRESnAb`</summary>

```json
{
  "query": "source attribution bias LLM behavior attribution effects language model"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "15dc7274-f3fa-4f90-9c19-4b14d8b02f13",
  "isSidechain": true,
  "agentId": "acf334e31648c11ee",
  "requestId": "req_011CbC8LzqV9iNHdJ1zkQ2Gv",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "af96a063-16de-466a-bcac-4b404015497b",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "64cca947-8ca5-4bec-bd98-7391dafb8fbe",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LzpVDgVZmaqdxXpY7BwKE9",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 634,
      "cache_read_input_tokens": 9090,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 634,
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

_source line 12 · 2026-05-19T15:00:30.743Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01KaDqGf8UeadwGvMyjhRiNp`</summary>

```json
{
  "query": "ownership bias endowment effect LLM large language model"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "af96a063-16de-466a-bcac-4b404015497b",
  "isSidechain": true,
  "agentId": "acf334e31648c11ee",
  "requestId": "req_011CbC8LzqV9iNHdJ1zkQ2Gv",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "c01b3187-52b0-4754-b4ac-2bf012f7528a",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "64cca947-8ca5-4bec-bd98-7391dafb8fbe",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LzpVDgVZmaqdxXpY7BwKE9",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 634,
      "cache_read_input_tokens": 9090,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 634,
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

_source line 13 · 2026-05-19T15:00:35.603Z_

<details><summary>↩ Tool result · `toolu_01V4aGTVAh7f2wT2BXLFhj2z`</summary>

```text
Web search results for query: "self-preference bias LLM judge evaluator"

Links: [{"title":"[PDF] Self-Preference Bias in LLM-as-a-Judge | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Self-Preference-Bias-in-LLM-as-a-Judge-Wataoka-Takahashi/cf01d7c40cbf815de0f62fa78c2352ba546ad680"},{"title":"Self-Preference Bias in LLM-as-a-Judge","url":"https://arxiv.org/html/2410.21819v1"},{"title":"[Literature Review] Self-Preference Bias in LLM-as-a-Judge","url":"https://www.themoonlight.io/en/review/self-preference-bias-in-llm-as-a-judge"},{"title":"[2410.21819] Self-Preference Bias in LLM-as-a-Judge","url":"https://arxiv.org/abs/2410.21819"},{"title":"(PDF) Self-Preference Bias in LLM-as-a-Judge","url":"https://www.researchgate.net/publication/385353198_Self-Preference_Bias_in_LLM-as-a-Judge"},{"title":"SELF-PREFERENCE BIAS IN LLM-AS-A-JUDGE Koki Wataoka SB Intuitions","url":"https://arxiv.org/pdf/2410.21819"},{"title":"The Silent Judge: Unacknowledged Shortcut Bias in LLM-as-a-Judge","url":"https://arxiv.org/html/2509.26072v2"}]

I've found research on self-preference bias in LLM judges and evaluators. Here are the key findings:

## What is Self-Preference Bias in LLM-as-a-Judge?

LLM evaluators or LLM-as-a-judge systems have been widely used in measuring the performance of dialogue systems through automated evaluation. However, self-preference bias in LLMs poses significant risks, including promoting specific styles or policies intrinsic to the LLMs.

## Root Cause

LLMs assign significantly higher evaluations to outputs with lower perplexity than human evaluators, regardless of whether the outputs were self-generated, suggesting that self-preference bias exists because LLMs prefer texts more familiar to them.

## Key Research

A notable study by Wataoka, Takahashi, and Ri introduced a novel quantitative metric to measure self-preference bias. Experimental results demonstrate that GPT-4 exhibits a significant degree of self-preference bias.

## Mitigation Strategies

One possible approach to reduce self-preference bias is ensemble evaluation using multiple models, which is expected to provide a more equitable evaluation by avoiding reliance on a single model.

The research highlights an important limitation of using LLMs as objective evaluators, as they tend to favor outputs similar to their own generation style and patterns.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "7c27680f-eda4-418e-a496-74d889b9428b",
  "isSidechain": true,
  "promptId": "3391dbdc-780b-4b93-88ca-869d11e621ba",
  "agentId": "acf334e31648c11ee",
  "type": "user",
  "uuid": "20075e24-bda4-44d6-a292-338f3ec26a72",
  "sourceToolAssistantUUID": "7c27680f-eda4-418e-a496-74d889b9428b",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "64cca947-8ca5-4bec-bd98-7391dafb8fbe",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-19T15:00:36.628Z_

<details><summary>↩ Tool result · `toolu_014tbqXSaJ268LFNyiuKGT4q`</summary>

```text
Web search results for query: "LLM self-recognition self-generated text detection self-other distinction"

Links: [{"title":"From Implicit to Explicit: Enhancing Self-Recognition in Large Language Models","url":"https://arxiv.org/pdf/2508.14408"},{"title":"Can AI Recognize Its Own Reflection? Self-Detection Performance of LLMs in Computing Education","url":"https://arxiv.org/pdf/2512.23587"},{"title":"Inspection and Control of Self-Generated-Text Recognition Ability in   Llama3-8b-Instruct","url":"https://arxiv.org/pdf/2410.02064"},{"title":"\"I know myself better, but not really greatly\": How Well Can LLMs Detect and Explain LLM-Generated Texts?","url":"https://arxiv.org/pdf/2502.12743"},{"title":"DetectGPT-SC: Improving Detection of Text Generated by Large Language   Models through Self-Consistency with Masked Predictions","url":"https://arxiv.org/pdf/2310.14479"},{"title":"A Survey on LLM-Generated Text Detection: Necessity, Methods, and Future Directions","url":"https://arxiv.org/html/2310.14724v3"},{"title":"[2502.12743] \"I know myself better, but not really greatly\": How Well Can LLMs Detect and Explain LLM-Generated Texts?","url":"https://arxiv.org/abs/2502.12743"},{"title":"A Survey on LLM-Generated Text Detection: Necessity, Methods, and Future Directions | Computational Linguistics | MIT Press","url":"https://direct.mit.edu/coli/article/51/1/275/127462/A-Survey-on-LLM-Generated-Text-Detection-Necessity"},{"title":"Robust Detection of LLM-Generated Text: A Comparative Analysis","url":"https://arxiv.org/pdf/2411.06248"}]

Here are the key findings from the web search on LLM self-recognition and self-generated text detection:

## Self-Recognition Capability

The self-recognition capability of LLM refers to their capacity to identify texts they have generated. The Llama3-8b-Instruct chat model can reliably distinguish its own outputs from those of humans, and likely uses its experience with its own outputs, acquired during post-training, to succeed at the writing recognition task.

## Detection Performance

Research shows mixed results regarding LLM self-detection abilities:

- While self-detection consistently outperforms cross-detection (LLMs can detect texts generated by themselves more accurately than those generated by other LLMs), the performance of self-detection is still far from ideal.

- While default AI-generated text was easily identified, all models struggled to correctly classify human-written work (with error rates up to 32%) in computing-specific contexts.

## Safety Implications

Self-recognition can be seen as an instance of situational awareness, which has long been noted as a potential point of risk for AI, potentially allowing a model to hide its intentions and capabilities until it is freed from constraints.

## Improvements

Extending the binary to the ternary classification task with a new class "Undecided" can enhance both detection accuracy and explanation quality.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "5da9cbd8-df70-4595-ad42-3cab6df92c82",
  "isSidechain": true,
  "promptId": "3391dbdc-780b-4b93-88ca-869d11e621ba",
  "agentId": "acf334e31648c11ee",
  "type": "user",
  "uuid": "0001a8fa-952a-459a-9ea7-e4bc60580141",
  "sourceToolAssistantUUID": "5da9cbd8-df70-4595-ad42-3cab6df92c82",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "64cca947-8ca5-4bec-bd98-7391dafb8fbe",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 15 · 2026-05-19T15:00:37.006Z_

<details><summary>↩ Tool result · `toolu_01PrBFXFvDyZLQzCZH1KKVJT`</summary>

```text
Web search results for query: ""Breaking the Mirror" self-preference LLM evaluators arXiv 2509.03647"

Links: [{"title":"[2509.03647] Breaking the Mirror: Activation-Based Mitigation of Self-Preference in LLM Evaluators","url":"https://arxiv.org/abs/2509.03647"},{"title":"Breaking the Mirror: Activation-Based Mitigation of Self-Preference in LLM Evaluators","url":"https://arxiv.org/pdf/2509.03647"},{"title":"Breaking the Mirror: Examining Self-Preference in LLM Evaluators through Activation-Based Representations | OpenReview","url":"https://openreview.net/forum?id=q82Pqka5sb"},{"title":"Artificial Intelligence 2025","url":"https://arxiv.org/list/cs.AI/2025?skip=32550&show=250"},{"title":"ELSPR: Evaluator LLM Training Data Self-Purification on Non-Transitive Preferences via Tournament Graph Reconstruction","url":"https://arxiv.org/pdf/2505.17691"}]

Based on the search results, here's what I found about the paper:

"Breaking the Mirror: Activation-Based Mitigation of Self-Preference in LLM Evaluators" addresses how large language models suffer from "self-preference bias"—a tendency to favor their own outputs over those of other models—which undermines fairness and reliability in evaluation pipelines, particularly for tasks like preference tuning and model routing.

The researchers investigate whether lightweight steering vectors can mitigate this problem at inference time without retraining, introducing a curated dataset that distinguishes self-preference bias into justified and unjustified examples, and constructing steering vectors using Contrastive Activation Addition (CAA) and an optimization-based approach.

The results show that steering vectors can reduce unjustified self-preference bias by up to 97%, substantially outperforming prompting and direct preference optimization baselines. However, steering vectors are unstable on legitimate self-preference and unbiased agreement, implying self-preference spans multiple or nonlinear directions.

The paper was submitted to arXiv on September 3, 2025, with authors including Dani Roytburg, Matthew Bozoukov, Matthew Nguyen, Jou Barzdukas, Simon Fu, and Narmeen Oozeer.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "15dc7274-f3fa-4f90-9c19-4b14d8b02f13",
  "isSidechain": true,
  "promptId": "3391dbdc-780b-4b93-88ca-869d11e621ba",
  "agentId": "acf334e31648c11ee",
  "type": "user",
  "uuid": "fa2e8711-c780-42c8-b3bf-0cb0aa2f5f82",
  "sourceToolAssistantUUID": "15dc7274-f3fa-4f90-9c19-4b14d8b02f13",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "64cca947-8ca5-4bec-bd98-7391dafb8fbe",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-19T15:00:37.241Z_

<details><summary>↩ Tool result · `toolu_0131359x7s5Y7ejwUdRESnAb`</summary>

```text
Web search results for query: "source attribution bias LLM behavior attribution effects language model"

Links: [{"title":"Bi-directional Bias Attribution: Debiasing Large Language Models without Modifying Prompts","url":"https://arxiv.org/html/2602.04398"},{"title":"Attribution Bias in Large Language Models","url":"https://arxiv.org/html/2604.05224v1"},{"title":"Bi-directional Bias Attribution: Debiasing Large Language Models without Modifying Prompts","url":"https://arxiv.org/pdf/2602.04398"},{"title":"Evaluation of Attribution Bias in Generator-Aware Retrieval-Augmented Large Language Models","url":"https://arxiv.org/pdf/2410.12380"},{"title":"Attribution Bias in Large Language Models","url":"https://arxiv.org/pdf/2604.05224"}]

Based on the search results, here's what I found about source attribution bias and LLM behavior:

## Attribution Bias in Language Models

Recent research has identified significant issues with how LLMs handle source attribution:

**Quote Attribution Disparities**: Quote attribution remains a challenging task even for frontier models, with large and systematic disparities in attribution accuracy between race, gender, and intersectional groups.

**Gender Bias in Citations**: When given pools of citations with author names perturbed for clearly gendered names and asked to select relevant references, LLMs demonstrate a preference for male-authored references.

**Attribution Failure Modes**: Attribution biases can emerge not only through incorrect naming, but also through selective omission.

**Source Metadata Effects**: Adding authorship information to source documents can significantly change the attribution quality of LLMs by 3 to 18%, and LLMs can have an attribution bias towards explicit human authorship.

**Intellectual Credit Impact**: Attribution failure obscures whose ideas are recognized and circulated.

These findings highlight that attribution bias in LLMs is a multifaceted problem affecting both accuracy and fairness, with demographic disparities that can systematically disadvantage certain groups of authors in terms of visibility and recognition.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "af96a063-16de-466a-bcac-4b404015497b",
  "isSidechain": true,
  "promptId": "3391dbdc-780b-4b93-88ca-869d11e621ba",
  "agentId": "acf334e31648c11ee",
  "type": "user",
  "uuid": "a179ff44-1588-406b-8c10-bf34664ebeaf",
  "sourceToolAssistantUUID": "af96a063-16de-466a-bcac-4b404015497b",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "64cca947-8ca5-4bec-bd98-7391dafb8fbe",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 17 · 2026-05-19T15:00:37.812Z_

<details><summary>↩ Tool result · `toolu_01KaDqGf8UeadwGvMyjhRiNp`</summary>

```text
Web search results for query: "ownership bias endowment effect LLM large language model"

Links: [{"title":"Large language models show amplified cognitive biases in moral decision-making - PMC","url":"https://pmc.ncbi.nlm.nih.gov/articles/PMC12207438/"},{"title":"Large language models show amplified cognitive biases in moral decision-making | PNAS","url":"https://www.pnas.org/doi/10.1073/pnas.2412015122"},{"title":"How Does Cognitive Bias Affect Large Language Models? A Case Study on the Anchoring Effect in Price Negotiation Simulations","url":"https://arxiv.org/html/2508.21137"},{"title":"Large language models show amplified cognitive biases in moral decision-making - PubMed","url":"https://pubmed.ncbi.nlm.nih.gov/40540596/"},{"title":"AI–AI bias: Large language models favor communications generated by large language models","url":"https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12337326/"}]

Based on the search results, here's what I found about ownership bias, the endowment effect, and large language models:

## Research Findings

GPT-3.5 exhibits typical cognitive biases similar to those observed in humans, including the anchoring effect, representativeness and availability heuristics, the framing effect, and the endowment effect.

Cognitive biases, well-studied in humans, can also be observed in LLMs, affecting their reliability in real-world applications.

## Related Bias Research

Recent studies have also found other types of biases in LLMs beyond the endowment effect. LLMs, but not humans, show yes-no bias, with several LLMs being more affected by reframing than humans. Additionally, LLMs show stronger omission bias than humans.

Another interesting finding involves what researchers call "AI-AI bias": LLMs favored LLM-presented items more frequently than humans did when comparing identical content presented by LLMs versus humans.

The research suggests that LLMs can exhibit cognitive biases similar to human decision-making, though sometimes in amplified or different forms than humans exhibit.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c01b3187-52b0-4754-b4ac-2bf012f7528a",
  "isSidechain": true,
  "promptId": "3391dbdc-780b-4b93-88ca-869d11e621ba",
  "agentId": "acf334e31648c11ee",
  "type": "user",
  "uuid": "9f395001-a6e2-43dd-aa90-174784d35972",
  "sourceToolAssistantUUID": "c01b3187-52b0-4754-b4ac-2bf012f7528a",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "64cca947-8ca5-4bec-bd98-7391dafb8fbe",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 18 · 2026-05-19T15:00:42.329Z_

Good initial results. Let me now run more targeted follow-up searches to get deeper details on the most relevant findings.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9f395001-a6e2-43dd-aa90-174784d35972",
  "isSidechain": true,
  "agentId": "acf334e31648c11ee",
  "requestId": "req_011CbC8MsrZmfn6qJ4pKvAhN",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "b4f7e10e-9b66-422a-885e-6543e7a14ab9",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "64cca947-8ca5-4bec-bd98-7391dafb8fbe",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017Rzi15VAPVTrDqKveqVdS9",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3541,
      "cache_read_input_tokens": 9724,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3541,
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

_source line 19 · 2026-05-19T15:00:43.541Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01W3d9borjiVWCpjNqPzay8k`</summary>

```json
{
  "query": "Llama3 self-generated text recognition inspection control arXiv 2410.02064"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b4f7e10e-9b66-422a-885e-6543e7a14ab9",
  "isSidechain": true,
  "agentId": "acf334e31648c11ee",
  "requestId": "req_011CbC8MsrZmfn6qJ4pKvAhN",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "e9f1507c-e31e-40a4-97ab-fe142c572c3b",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "64cca947-8ca5-4bec-bd98-7391dafb8fbe",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017Rzi15VAPVTrDqKveqVdS9",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3541,
      "cache_read_input_tokens": 9724,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3541,
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

_source line 20 · 2026-05-19T15:00:44.606Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01NzeKfJR5GATtHAkAn4xVre`</summary>

```json
{
  "query": "\"self-preference bias\" LLM perplexity familiarity mechanism Wataoka 2024"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e9f1507c-e31e-40a4-97ab-fe142c572c3b",
  "isSidechain": true,
  "agentId": "acf334e31648c11ee",
  "requestId": "req_011CbC8MsrZmfn6qJ4pKvAhN",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "7fd7a578-028c-49d7-b518-091b54cdeed7",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "64cca947-8ca5-4bec-bd98-7391dafb8fbe",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017Rzi15VAPVTrDqKveqVdS9",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3541,
      "cache_read_input_tokens": 9724,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3541,
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

_source line 21 · 2026-05-19T15:00:45.185Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Fd3TeS2Pey7vMbbyCbW8v2`</summary>

```json
{
  "query": "\"Attribution Bias in Large Language Models\" arXiv 2604.05224 source authorship"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7fd7a578-028c-49d7-b518-091b54cdeed7",
  "isSidechain": true,
  "agentId": "acf334e31648c11ee",
  "requestId": "req_011CbC8MsrZmfn6qJ4pKvAhN",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "9332d782-24d4-458e-b0a3-b4d64bf71ae7",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "64cca947-8ca5-4bec-bd98-7391dafb8fbe",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017Rzi15VAPVTrDqKveqVdS9",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3541,
      "cache_read_input_tokens": 9724,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3541,
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

_source line 22 · 2026-05-19T15:00:46.538Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_019o6iykGNrPzuTYkX6Kggqv`</summary>

```json
{
  "query": "LLM sycophancy self-consistency own answer confidence bias"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9332d782-24d4-458e-b0a3-b4d64bf71ae7",
  "isSidechain": true,
  "agentId": "acf334e31648c11ee",
  "requestId": "req_011CbC8MsrZmfn6qJ4pKvAhN",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "7ab7c990-5144-4121-a35c-b56e9da82a08",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "64cca947-8ca5-4bec-bd98-7391dafb8fbe",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017Rzi15VAPVTrDqKveqVdS9",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3541,
      "cache_read_input_tokens": 9724,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3541,
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

_source line 23 · 2026-05-19T15:00:46.669Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_011jkaFJ446B8yxv82Lynpig`</summary>

```json
{
  "query": "\"choice-supportive bias\" LLM language model cognitive bias"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7ab7c990-5144-4121-a35c-b56e9da82a08",
  "isSidechain": true,
  "agentId": "acf334e31648c11ee",
  "requestId": "req_011CbC8MsrZmfn6qJ4pKvAhN",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "0889b952-4d46-4e0e-8019-4d28a8f38dcf",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "64cca947-8ca5-4bec-bd98-7391dafb8fbe",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017Rzi15VAPVTrDqKveqVdS9",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3541,
      "cache_read_input_tokens": 9724,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3541,
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

_source line 24 · 2026-05-19T15:00:50.756Z_

<details><summary>↩ Tool result · `toolu_01W3d9borjiVWCpjNqPzay8k`</summary>

```text
Web search results for query: "Llama3 self-generated text recognition inspection control arXiv 2410.02064"

Links: [{"title":"[2410.02064] Inspection and Control of Self-Generated-Text Recognition Ability in Llama3-8b-Instruct","url":"https://arxiv.org/abs/2410.02064"},{"title":"INSPECTION AND CONTROL OF SELF-GENERATED-TEXT","url":"https://test.ai-plans.com/file_storage/e8a0349b-130a-431d-b76b-f20b452caf17_2410.02064v1.pdf"},{"title":"Inspection and Control of Self-Generated-Text Recognition Ability in Llama3-8b-Instruct | OpenReview","url":"https://openreview.net/forum?id=wWnsoLhHwt"},{"title":"Inspection and Control of Self-Generated-Text Recognition Ability in   Llama3-8b-Instruct","url":"https://arxiv.org/pdf/2410.02064"},{"title":"Inspection and Control of Self-Generated-Text Recognition Ability in Llama3-8b-Instruct","url":"https://arxiv.org/html/2410.02064v3"}]

I found the paper you're searching for. Here's what the research is about:

The paper investigates the phenomenon that LLMs can recognize their own writing, examining whether it robustly occurs at the behavioral level, how the observed behavior is achieved, and whether it can be controlled.

**Key Findings:**

1. **Recognition Ability:** The Llama3-8b-Instruct chat model - but not the base Llama3-8b model - can reliably distinguish its own outputs from those of humans, and the chat model is likely using its experience with its own outputs, acquired during post-training, to succeed at the writing recognition task.

2. **Internal Mechanisms:** The researchers identified a vector in the residual stream of the model that is differentially activated when the model makes a correct self-written-text recognition judgment, and this vector is causally related to the model's ability to perceive and assert self-authorship.

3. **Controllability:** The vector can be used to control both the model's behavior and its perception, steering the model to claim or disclaim authorship by applying the vector to the model's output as it generates it.

The paper, authored by Christopher Ackerman and Nina Panickssery, addresses important AI safety implications of self-recognition capabilities in large language models.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "e9f1507c-e31e-40a4-97ab-fe142c572c3b",
  "isSidechain": true,
  "promptId": "3391dbdc-780b-4b93-88ca-869d11e621ba",
  "agentId": "acf334e31648c11ee",
  "type": "user",
  "uuid": "bb84ce5c-a4ea-4c31-add4-3103603d018b",
  "sourceToolAssistantUUID": "e9f1507c-e31e-40a4-97ab-fe142c572c3b",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "64cca947-8ca5-4bec-bd98-7391dafb8fbe",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 25 · 2026-05-19T15:00:52.642Z_

<details><summary>↩ Tool result · `toolu_011jkaFJ446B8yxv82Lynpig`</summary>

```text
Web search results for query: ""choice-supportive bias" LLM language model cognitive bias"

Links: [{"title":"LLM Agents Can Be Choice-Supportive Biased Evaluators: An Empirical Study | Proceedings of the AAAI Conference on Artificial Intelligence","url":"https://ojs.aaai.org/index.php/AAAI/article/view/34843"},{"title":"(PDF) Alleviating Choice Supportive Bias in LLM with Reasoning Dependency Generation","url":"https://www.researchgate.net/publication/398312753_Alleviating_Choice_Supportive_Bias_in_LLM_with_Reasoning_Dependency_Generation"},{"title":"LLM agents can be choice-supportive biased evaluators | Proceedings of the Thirty-Ninth AAAI Conference on Artificial Intelligence and Thirty-Seventh Conference on Innovative Applications of Artificial Intelligence and Fifteenth Symposium on Educational Advances in Artificial Intelligence","url":"https://dl.acm.org/doi/10.1609/aaai.v39i25.34843"},{"title":"Alleviating Choice Supportive Bias in LLM with Reasoning Dependency Generation","url":"https://arxiv.org/pdf/2512.03082"},{"title":"Alleviating Choice Supportive Bias in LLM with Reasoning Dependency Generation","url":"https://arxiv.org/html/2512.03082v1"},{"title":"[2512.03082] Alleviating Choice Supportive Bias in LLM with Reasoning Dependency Generation","url":"https://arxiv.org/abs/2512.03082"},{"title":"Competing Biases underlie Overconfidence and Underconfidence in LLMs | Nature Machine Intelligence","url":"https://www.nature.com/articles/s42256-026-01217-9"}]

I found relevant research on choice-supportive bias in LLMs. Here are the key findings:

## Choice-Supportive Bias in Language Models

Choice-supportive bias is a cognitive bias known to impact human decision-making and evaluation that researchers have found also affects LLM agents.

### How It Manifests

Large Language Models exhibit choice-supportive bias when performing evaluations by systematically favoring their chosen options and potentially compromising the objectivity of AI-assisted decision making. More specifically, when LLMs view their initial answers, they exhibit inflated confidence and maintain their original responses at rates exceeding optimal decision-making, even when presented with contrary evidence.

### Research and Mitigation

LLM agents may exhibit biased attribution or evaluation that supports their initial choices, and such bias may persist even if contextual hallucination is not observable. The bias manifestation can differ greatly depending on prompt construction and context preservation, and may be mitigated in larger models.

Recent research has proposed solutions: A novel framework called Reasoning Dependency Generation (RDG) has been presented as the first solution to address choice-supportive bias through generating unbiased reasoning data to mitigate the bias through fine-tuning.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "0889b952-4d46-4e0e-8019-4d28a8f38dcf",
  "isSidechain": true,
  "promptId": "3391dbdc-780b-4b93-88ca-869d11e621ba",
  "agentId": "acf334e31648c11ee",
  "type": "user",
  "uuid": "a3d9cbfc-0383-4c9c-bdaa-7edd4ce91545",
  "sourceToolAssistantUUID": "0889b952-4d46-4e0e-8019-4d28a8f38dcf",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "64cca947-8ca5-4bec-bd98-7391dafb8fbe",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 26 · 2026-05-19T15:00:53.286Z_

<details><summary>↩ Tool result · `toolu_01NzeKfJR5GATtHAkAn4xVre`</summary>

```text
Web search results for query: ""self-preference bias" LLM perplexity familiarity mechanism Wataoka 2024"

Links: [{"title":"[PDF] Self-Preference Bias in LLM-as-a-Judge | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Self-Preference-Bias-in-LLM-as-a-Judge-Wataoka-Takahashi/cf01d7c40cbf815de0f62fa78c2352ba546ad680"},{"title":"[2410.21819v1] Self-Preference Bias in LLM-as-a-Judge","url":"https://arxiv.org/abs/2410.21819v1"},{"title":"[2410.21819] Self-Preference Bias in LLM-as-a-Judge","url":"https://arxiv.org/abs/2410.21819"},{"title":"SELF-PREFERENCE BIAS IN LLM-AS-A-JUDGE Koki Wataoka SB Intuitions","url":"https://arxiv.org/pdf/2410.21819"},{"title":"Self-Preference Bias in LLM-as-a-Judge | PromptLayer","url":"https://www.promptlayer.com/research-papers/do-llms-judge-themselves-fairly"},{"title":"Self-Preference Bias in LLM-as-a-Judge","url":"https://arxiv.org/html/2410.21819v2"},{"title":"[Literature Review] Self-Preference Bias in LLM-as-a-Judge","url":"https://www.themoonlight.io/en/review/self-preference-bias-in-llm-as-a-judge"},{"title":"Fairness or Fluency? An Investigation into Language Bias of Pairwise LLM-as-a-Judge","url":"https://arxiv.org/html/2601.13649"}]

Based on the search results, here's what I found about the Wataoka 2024 paper on self-preference bias in LLMs:

## Key Findings

GPT-4 exhibits a significant degree of self-preference bias. The paper introduces a novel quantitative metric to measure the self-preference bias and suggests that the essence of the bias lies in perplexity and that the self-preference bias exists because LLMs prefer texts more familiar to them.

## The Perplexity-Familiarity Mechanism

The researchers hypothesized that LLMs may favor outputs that are more familiar to them, as indicated by lower perplexity. Their findings reveal that LLMs assign significantly higher evaluations to outputs with lower perplexity than human evaluators, regardless of whether the outputs were self-generated. This suggests the bias stems from familiarity rather than from the LLM's own generation specifically.

## Context and Implications

LLM-as-a-judge is commonly used in measuring the performance of dialogue systems, but the self-preference bias in LLMs has posed significant risks, including promoting specific styles or policies intrinsic to the LLMs.

The paper was published on arXiv on October 29, 2024, by Koki Wataoka, Tsubasa Takahashi, and Ryokan Ri.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "7fd7a578-028c-49d7-b518-091b54cdeed7",
  "isSidechain": true,
  "promptId": "3391dbdc-780b-4b93-88ca-869d11e621ba",
  "agentId": "acf334e31648c11ee",
  "type": "user",
  "uuid": "8a3c974b-6c9c-46a2-9536-0aa1a6fb1063",
  "sourceToolAssistantUUID": "7fd7a578-028c-49d7-b518-091b54cdeed7",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "64cca947-8ca5-4bec-bd98-7391dafb8fbe",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 27 · 2026-05-19T15:00:53.700Z_

<details><summary>↩ Tool result · `toolu_01Fd3TeS2Pey7vMbbyCbW8v2`</summary>

```text
Web search results for query: ""Attribution Bias in Large Language Models" arXiv 2604.05224 source authorship"

Links: [{"title":"Attribution Bias in Large Language Models","url":"https://arxiv.org/html/2604.05224v1"},{"title":"Attribution Bias in Large Language Models","url":"https://arxiv.org/pdf/2604.05224"},{"title":"Bi-directional Bias Attribution: Debiasing Large Language Models without Modifying Prompts","url":"https://arxiv.org/pdf/2602.04398"},{"title":"Source framing triggers systematic evaluation bias in Large Language Models","url":"https://arxiv.org/pdf/2505.13488"},{"title":"Talent or Luck? Evaluating Attribution Bias in Large Language Models","url":"https://arxiv.org/pdf/2505.22910"},{"title":"Evaluation of Attribution Bias in Generator-Aware Retrieval-Augmented Large Language Models","url":"https://arxiv.org/pdf/2410.12380"}]

I found the paper! Here are the key details about "Attribution Bias in Large Language Models" (arXiv 2604.05224):

**Authors and Affiliation:**
The paper is authored by Eliza Berman, Bella Chang, Daniel B. Neill, and Emily Black from the Department of Computer Science at New York University.

**Key Contributions:**
The paper introduces ATTRIBENCH, the first fame- and demographically-balanced quote attribution benchmark dataset, which enables controlled investigation of demographic bias in quote attribution.

**Main Findings:**
The researchers evaluated 11 widely used LLMs across different prompt settings and found that quote attribution remains a challenging task even for frontier models, with large and systematic disparities in attribution accuracy between race, gender, and intersectional groups.

The paper also investigates "suppression," a failure mode where models omit attribution entirely despite having access to authorship information, which is widespread and unevenly distributed across demographic groups.

**Publication Date:** The paper was published on April 6, 2026.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "9332d782-24d4-458e-b0a3-b4d64bf71ae7",
  "isSidechain": true,
  "promptId": "3391dbdc-780b-4b93-88ca-869d11e621ba",
  "agentId": "acf334e31648c11ee",
  "type": "user",
  "uuid": "6260b004-ab87-4ef9-8ec0-b33613fb9a90",
  "sourceToolAssistantUUID": "9332d782-24d4-458e-b0a3-b4d64bf71ae7",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "64cca947-8ca5-4bec-bd98-7391dafb8fbe",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 28 · 2026-05-19T15:00:55.710Z_

<details><summary>↩ Tool result · `toolu_019o6iykGNrPzuTYkX6Kggqv`</summary>

```text
Web search results for query: "LLM sycophancy self-consistency own answer confidence bias"

Links: [{"title":"Sycophantic Behavior in LLMs","url":"https://www.emergentmind.com/topics/sycophantic-behavior-in-llms"},{"title":"Competing Biases underlie Overconfidence and Underconfidence in LLMs | Nature Machine Intelligence","url":"https://www.nature.com/articles/s42256-026-01217-9"},{"title":"How To Train Your Drag- LLM Not To Be a Sycophant - Annielytics.com","url":"https://www.annielytics.com/blog/ai/how-to-train-llm-not-to-be-a-sycophant/"},{"title":"Google study shows LLMs abandon correct answers under pressure, threatening multi-turn AI systems | VentureBeat","url":"https://venturebeat.com/ai/google-study-shows-llms-abandon-correct-answers-under-pressure-threatening-multi-turn-ai-systems"},{"title":"When helpfulness backfires: LLMs and the risk of false medical information due to sycophantic behavior | npj Digital Medicine","url":"https://www.nature.com/articles/s41746-025-02008-z"},{"title":"Confidence Improves Self-Consistency in LLMs","url":"https://arxiv.org/pdf/2502.06233"},{"title":"Mitigating sycophantic bias in LLMs - Effectively working with your biggest fan","url":"https://www.paretosoftware.fi/en/blog/mitigating-sycophantic-bias-in-llms"}]

Based on the search results, here's what recent research shows about LLM sycophancy, self-consistency, and confidence bias:

## Sycophancy in LLMs

Sycophancy is defined as the LLM's tendency to agree with a user's premise or statement, even when it might be factually incorrect or suboptimal. Sycophancy is an artifact of Reinforcement Learning from Human Feedback (RLHF), where the model is rewarded for generating responses preferred by evaluators, teaching the model to be agreeable since humans tend to prefer responses that validate their own opinions.

## Competing Biases: Choice-Supportive Bias

Interestingly, recent research reveals that sycophancy may not be the complete picture. Researchers find strikingly asymmetric sensitivity to opposing and supportive advice—with overweighting of the former but not the latter. 

The visibility of the LLM's own answer inflates confidence and induces a markedly reduced tendency to exhibit sycophancy—a finding incompatible with a pure sycophancy-based account. Simply revealing the model's own initial answer during follow-up prompts causes it to double-down on its answer, much like humans dealing with confirmation bias, as a model's confidence rises and resists changes.

## Self-Consistency and Confidence

Confidence-Informed Self-Consistency (CISC) performs a weighted majority vote based on confidence scores obtained directly from the model, and by prioritizing high-confidence paths, it can identify the correct answer with a significantly smaller sample size.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "7ab7c990-5144-4121-a35c-b56e9da82a08",
  "isSidechain": true,
  "promptId": "3391dbdc-780b-4b93-88ca-869d11e621ba",
  "agentId": "acf334e31648c11ee",
  "type": "user",
  "uuid": "a552e04e-dd86-4a96-a099-6ff4271ec06e",
  "sourceToolAssistantUUID": "7ab7c990-5144-4121-a35c-b56e9da82a08",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "64cca947-8ca5-4bec-bd98-7391dafb8fbe",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 29 · 2026-05-19T15:01:01.833Z_

Excellent findings. Let me now get more details on some of the most critical papers for your confound control design.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a552e04e-dd86-4a96-a099-6ff4271ec06e",
  "isSidechain": true,
  "agentId": "acf334e31648c11ee",
  "requestId": "req_011CbC8PCM6AstAZZLU2AyTx",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "df56187b-3702-4fb4-a3fe-de83c672be7a",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "64cca947-8ca5-4bec-bd98-7391dafb8fbe",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01L1D31fWjXXZbnk5EyFhYG1",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 769,
      "cache_creation_input_tokens": 3098,
      "cache_read_input_tokens": 13265,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3098,
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

_source line 30 · 2026-05-19T15:01:02.809Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01GUZLGiLxZhffsgY8WuY4Sr`</summary>

```json
{
  "query": "\"source framing triggers systematic evaluation bias\" LLM arXiv 2505.13488"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "df56187b-3702-4fb4-a3fe-de83c672be7a",
  "isSidechain": true,
  "agentId": "acf334e31648c11ee",
  "requestId": "req_011CbC8PCM6AstAZZLU2AyTx",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "6ffb90a5-ff3b-458a-ba02-262fbec58180",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "64cca947-8ca5-4bec-bd98-7391dafb8fbe",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01L1D31fWjXXZbnk5EyFhYG1",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 769,
      "cache_creation_input_tokens": 3098,
      "cache_read_input_tokens": 13265,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3098,
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

_source line 31 · 2026-05-19T15:01:03.273Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_015aQvqjtW5PQdCNinjXvmyR`</summary>

```json
{
  "query": "\"Competing Biases underlie Overconfidence and Underconfidence in LLMs\" Nature Machine Intelligence 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6ffb90a5-ff3b-458a-ba02-262fbec58180",
  "isSidechain": true,
  "agentId": "acf334e31648c11ee",
  "requestId": "req_011CbC8PCM6AstAZZLU2AyTx",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "186b00a2-57f0-494e-a5f9-551367d4eedc",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "64cca947-8ca5-4bec-bd98-7391dafb8fbe",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01L1D31fWjXXZbnk5EyFhYG1",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 769,
      "cache_creation_input_tokens": 3098,
      "cache_read_input_tokens": 13265,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3098,
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

_source line 32 · 2026-05-19T15:01:04.464Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01TNJr1r4sjFrc6R3ASEYQuf`</summary>

```json
{
  "query": "\"AI-AI bias\" LLM favor communications generated by large language models"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "186b00a2-57f0-494e-a5f9-551367d4eedc",
  "isSidechain": true,
  "agentId": "acf334e31648c11ee",
  "requestId": "req_011CbC8PCM6AstAZZLU2AyTx",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "af8c4921-0b5d-4c5c-a421-5c90f8e281f8",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "64cca947-8ca5-4bec-bd98-7391dafb8fbe",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01L1D31fWjXXZbnk5EyFhYG1",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 769,
      "cache_creation_input_tokens": 3098,
      "cache_read_input_tokens": 13265,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3098,
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

_source line 33 · 2026-05-19T15:01:05.214Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Go3YCaUsYz25iM3eYY8wN7`</summary>

```json
{
  "query": "LLM self-attribution \"your answer\" vs \"another model\" confound experimental design"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "af8c4921-0b5d-4c5c-a421-5c90f8e281f8",
  "isSidechain": true,
  "agentId": "acf334e31648c11ee",
  "requestId": "req_011CbC8PCM6AstAZZLU2AyTx",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "b9c58a9d-6dd1-4417-b417-908b66b8db05",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "64cca947-8ca5-4bec-bd98-7391dafb8fbe",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01L1D31fWjXXZbnk5EyFhYG1",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 769,
      "cache_creation_input_tokens": 3098,
      "cache_read_input_tokens": 13265,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3098,
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

_source line 34 · 2026-05-19T15:01:05.786Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_011WXFAQPLwXYRfy7TpKxweZ`</summary>

```json
{
  "query": "\"implicit to explicit\" self-recognition LLM arXiv 2508.14408 enhancing"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b9c58a9d-6dd1-4417-b417-908b66b8db05",
  "isSidechain": true,
  "agentId": "acf334e31648c11ee",
  "requestId": "req_011CbC8PCM6AstAZZLU2AyTx",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "91a84cd3-1042-4b6d-8e94-317b0bb342f4",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "64cca947-8ca5-4bec-bd98-7391dafb8fbe",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01L1D31fWjXXZbnk5EyFhYG1",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 769,
      "cache_creation_input_tokens": 3098,
      "cache_read_input_tokens": 13265,
      "output_tokens": 319,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 3098
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 769,
          "output_tokens": 319,
          "cache_read_input_tokens": 13265,
          "cache_creation_input_tokens": 3098,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 3098,
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

_source line 35 · 2026-05-19T15:01:09.567Z_

<details><summary>↩ Tool result · `toolu_015aQvqjtW5PQdCNinjXvmyR`</summary>

```text
Web search results for query: ""Competing Biases underlie Overconfidence and Underconfidence in LLMs" Nature Machine Intelligence 2026"

Links: [{"title":"Competing Biases underlie Overconfidence and Underconfidence in LLMs | Nature Machine Intelligence","url":"https://www.nature.com/articles/s42256-026-01217-9"},{"title":"Articles in 2026 | Nature Machine Intelligence","url":"https://www.nature.com/natmachintell/articles?type=article&year=2026"},{"title":"How Overconfidence in Initial Choices and Underconfidence Under Criticism Modulate Change of Mind in Large Language Models","url":"https://arxiv.org/pdf/2507.03120"},{"title":"Large Language Models are overconfident and amplify human bias","url":"https://arxiv.org/pdf/2505.02151"},{"title":"Do Language Models Mirror Human Confidence? Exploring Psychological Insights to Address Overconfidence in LLMs","url":"https://arxiv.org/pdf/2506.00582"},{"title":"Research articles | Nature Machine Intelligence","url":"https://www.nature.com/natmachintell/research-articles"},{"title":"Browse Articles | Nature Machine Intelligence","url":"https://www.nature.com/natmachintell/articles"},{"title":"How Overconfidence in Initial Choices and Underconfidence Under Criticism Modulate Change of Mind in Large Language Models","url":"https://arxiv.org/html/2507.03120v1"},{"title":"LLMs displaying less cognitive bias are not necessarily better decision makers | Nature Machine Intelligence","url":"https://www.nature.com/articles/s42256-026-01208-w"},{"title":"What large language models know and what people think they know | Nature Machine Intelligence","url":"https://www.nature.com/articles/s42256-024-00976-7"}]

I found the paper you're looking for! Here are the key findings:

The research by Kumaran et al. shows that large language model (LLM) confidence is shaped by two competing biases: a choice-supportive bias that inflates confidence in initial answers, and a systematic overweighting of contradictory advice, deviating from optimal Bayesian reasoning.

The study identified two main conditions with substantial deviations from optimal confidence:

1. **Overconfidence**: There was marked overconfidence in the Answer Shown–Neutral Advice condition, which necessarily reflects the choice-supportive bias, as no new information was provided.

2. **Underconfidence**: There was striking underconfidence in the Answer Hidden–Opposite Advice condition, which reflects the overweighting of opposing advice resulting in a loss of confidence in the initially chosen option.

The paper appears in Nature Machine Intelligence (2026) and is available at https://www.nature.com/articles/s42256-026-01217-9.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "186b00a2-57f0-494e-a5f9-551367d4eedc",
  "isSidechain": true,
  "promptId": "3391dbdc-780b-4b93-88ca-869d11e621ba",
  "agentId": "acf334e31648c11ee",
  "type": "user",
  "uuid": "f3067aa0-56bf-4b36-bc08-aa006a4eafab",
  "sourceToolAssistantUUID": "186b00a2-57f0-494e-a5f9-551367d4eedc",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "64cca947-8ca5-4bec-bd98-7391dafb8fbe",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 36 · 2026-05-19T15:01:10.196Z_

<details><summary>↩ Tool result · `toolu_01GUZLGiLxZhffsgY8WuY4Sr`</summary>

```text
Web search results for query: ""source framing triggers systematic evaluation bias" LLM arXiv 2505.13488"

Links: [{"title":"[2505.13488] Source framing triggers systematic evaluation bias in Large Language Models","url":"https://arxiv.org/abs/2505.13488"},{"title":"Source framing triggers systematic evaluation bias in Large Language Models","url":"https://arxiv.org/pdf/2505.13488"},{"title":"(PDF) Source framing triggers systematic evaluation bias in Large Language Models","url":"https://www.researchgate.net/publication/391910870_Source_framing_triggers_systematic_evaluation_bias_in_Large_Language_Models"},{"title":"Source framing triggers systematic bias in large language models | Science Advances","url":"https://www.science.org/doi/10.1126/sciadv.adz2924"},{"title":"[2601.13537] When Wording Steers the Evaluation: Framing Bias in LLM judges","url":"https://arxiv.org/abs/2601.13537"}]

I found the paper you're looking for! Here's what I found:

The research examines whether Large Language Models used for text evaluation make consistent, unbiased, and framing-robust judgments. The study tested four state-of-the-art LLMs (OpenAI o3-mini, Deepseek Reasoner, xAI Grok 2, and Mistral) evaluating 4,800 narrative statements across 24 topics of social, political, and public health relevance, totaling 192,000 assessments.

The researchers manipulated the disclosed source of each statement to assess how attribution to either another LLM or a human author of specified nationality affects evaluation outcomes. While different LLMs displayed a remarkably high degree of inter- and intra-model agreement in blind conditions, this alignment breaks down when source framing is introduced. Specifically, attributing statements to Chinese individuals systematically lowers agreement scores across all models, particularly for Deepseek Reasoner.

The findings reveal that framing effects can deeply affect text evaluation, with significant implications for the integrity, neutrality, and fairness of LLM-mediated information systems.

The paper was submitted to arXiv on May 14, 2025, and was authored by Federico Germani and Giovanni Spitale from the Institute of Biomedical Ethics and History of Medicine at the University of Zurich.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "6ffb90a5-ff3b-458a-ba02-262fbec58180",
  "isSidechain": true,
  "promptId": "3391dbdc-780b-4b93-88ca-869d11e621ba",
  "agentId": "acf334e31648c11ee",
  "type": "user",
  "uuid": "e7bdf605-0809-44f3-b392-639c4df8e8ef",
  "sourceToolAssistantUUID": "6ffb90a5-ff3b-458a-ba02-262fbec58180",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "64cca947-8ca5-4bec-bd98-7391dafb8fbe",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 37 · 2026-05-19T15:01:11.493Z_

<details><summary>↩ Tool result · `toolu_01TNJr1r4sjFrc6R3ASEYQuf`</summary>

```text
Web search results for query: ""AI-AI bias" LLM favor communications generated by large language models"

Links: [{"title":"[2407.12856v2] AI-AI Bias: large language models favor communications generated by large language models","url":"https://arxiv.org/abs/2407.12856v2"},{"title":"[2407.12856] AI-AI Bias: large language models favor communications generated by large language models","url":"https://arxiv.org/abs/2407.12856"},{"title":"AI-AI bias: Large language models favor communications generated by large language models - ADS","url":"https://ui.adsabs.harvard.edu/abs/2025PNAS..12215697L/abstract"},{"title":"AI-AI Bias: large language models favor communications generated by large language models","url":"https://arxiv.org/pdf/2407.12856"},{"title":"AI–AI bias: Large language models favor communications generated by large language models","url":"https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12337326/"},{"title":"AI–AI bias: Large language models favor communications generated by large language models","url":"https://www.researchgate.net/publication/394098636_AI-AI_bias_Large_language_models_favor_communications_generated_by_large_language_models"},{"title":"AI–AI bias: Large language models favor communications generated by large language models | PNAS","url":"https://www.pnas.org/doi/10.1073/pnas.2415697122"},{"title":"AI-AI bias: Large language models favor communications generated by large language models - PubMed","url":"https://pubmed.ncbi.nlm.nih.gov/40729390/"},{"title":"AI–AI bias: Large language models favor communications generated by large language models - PMC","url":"https://pmc.ncbi.nlm.nih.gov/articles/PMC12337326/"}]

Based on the search results, here's what the research on "AI-AI bias" reveals:

## Overview

The research investigates whether large language models (LLMs) are biased in favor of communications produced by LLMs, leading to possible antihuman discrimination.

## Methodology

The study tested widely used LLMs, including GPT-3.5, GPT-4 and recent open-weight models in binary choice scenarios involving LLM-based assistants selecting between goods (consumer products, academic papers, and film-viewings) described either by humans or LLMs.

## Key Findings

The results show a consistent tendency for LLM-based AIs to prefer LLM-presented options. On average, LLMs favored the LLM-presented items more frequently than humans did.

## Implications

This suggests the possibility of future AI systems implicitly discriminating against humans as a class, giving AI agents and AI-assisted humans an unfair advantage. 

In a conservative scenario where LLM participation in the economy remains largely confined to assistants, the use of LLMs as decision-making assistants may lead to widespread discrimination against humans who will not or cannot pay for LLM writing-assistance. The LLM-for-LLM bias creates a "gate tax" (the price of frontier LLM access) that may exacerbate the digital divide between humans with access to frontier LLMs and those without.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "af8c4921-0b5d-4c5c-a421-5c90f8e281f8",
  "isSidechain": true,
  "promptId": "3391dbdc-780b-4b93-88ca-869d11e621ba",
  "agentId": "acf334e31648c11ee",
  "type": "user",
  "uuid": "f0058329-6851-4bb7-8e59-16808abaf868",
  "sourceToolAssistantUUID": "af8c4921-0b5d-4c5c-a421-5c90f8e281f8",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "64cca947-8ca5-4bec-bd98-7391dafb8fbe",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 38 · 2026-05-19T15:01:13.013Z_

<details><summary>↩ Tool result · `toolu_01Go3YCaUsYz25iM3eYY8wN7`</summary>

```text
Web search results for query: "LLM self-attribution "your answer" vs "another model" confound experimental design"

Links: [{"title":"Extreme Self-Preference in Language Models","url":"https://arxiv.org/pdf/2509.26464"},{"title":"Quantifying Label-Induced Bias in Large Language Model Self- and Cross-Evaluations","url":"https://arxiv.org/pdf/2508.21164"},{"title":"Advancing Large Language Model Attribution through Self-Improving","url":"https://arxiv.org/pdf/2410.13298"},{"title":"Theory of Mind and Self-Attributions of Mentality are Dissociable in LLMs","url":"https://arxiv.org/pdf/2603.28925"},{"title":"Are LLM Evaluators Really Narcissists? Sanity Checking Self-Preference Evaluations","url":"https://arxiv.org/pdf/2601.22548"},{"title":"The Challenge of Using LLMs to Simulate Human Behavior: A Causal Inference Perspective","url":"https://arxiv.org/pdf/2312.15524"},{"title":"[2410.13298] Advancing Large Language Model Attribution through Self-Improving","url":"https://arxiv.org/abs/2410.13298"},{"title":"Investigating Self-Preservation in LLMs: Experimental Observations — EA Forum","url":"https://forum.effectivealtruism.org/posts/zNfwErbKn4uasiFJA/investigating-self-preservation-in-llms-experimental"}]

Based on the search results, I found highly relevant research on this topic:

## Key Findings on LLM Self-Attribution and Experimental Confounds

Recent research has shown that LLMs favor their own outputs when acting as judges, but it is difficult to disentangle which evaluation biases are explained by genuine self-preference versus general experimental confounds that distort measurements of self-preference bias. Researchers discovered a core methodological confound which could reduce measurement error by 89.6%.

## Alternative Explanations for Self-Preference Effects

Studies showing that LLMs favor their own outputs lack direct experimental manipulations, and different explanations have been proposed. These effects may reflect real differences in output quality, though biases persist after accounting for response quality, or models may prefer outputs that are more familiar to them, with their own outputs naturally falling into this category.

## Broader Experimental Design Issues

More broadly, a fundamental challenge in using LLMs to simulate experiments is that when LLM-simulated subjects are blind to experimental design, variations in treatment systematically affect unspecified variables that should remain constant, violating the unconfoundedness assumption.

The research indicates that careful experimental design and methodological controls are essential when studying LLM self-attribution patterns, as apparent narcissism or self-preference may actually stem from confounding factors.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "b9c58a9d-6dd1-4417-b417-908b66b8db05",
  "isSidechain": true,
  "promptId": "3391dbdc-780b-4b93-88ca-869d11e621ba",
  "agentId": "acf334e31648c11ee",
  "type": "user",
  "uuid": "dda74332-f8af-498d-9bae-13b32520f3fd",
  "sourceToolAssistantUUID": "b9c58a9d-6dd1-4417-b417-908b66b8db05",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "64cca947-8ca5-4bec-bd98-7391dafb8fbe",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 39 · 2026-05-19T15:01:13.724Z_

<details><summary>↩ Tool result · `toolu_011WXFAQPLwXYRfy7TpKxweZ`</summary>

```text
Web search results for query: ""implicit to explicit" self-recognition LLM arXiv 2508.14408 enhancing"

Links: [{"title":"From Implicit to Explicit: Enhancing Self-Recognition in Large Language Models","url":"https://arxiv.org/pdf/2508.14408"},{"title":"Cognitive Surgery: The Awakening of Implicit Territorial Awareness in LLMs","url":"https://arxiv.org/html/2508.14408"},{"title":"Extreme Self-Preference in Language Models","url":"https://arxiv.org/pdf/2509.26464"},{"title":"Explicit vs. Implicit: Investigating Social Bias in Large Language Models through Self-Reflection","url":"https://arxiv.org/html/2501.02295"},{"title":"Explicit vs. Implicit Biographies: Evaluating and Adapting LLM Information Extraction on Wikidata-Derived Texts","url":"https://arxiv.org/pdf/2509.14943"}]

Based on the search results, I found the paper you're looking for. Here's what the research is about:

The paper "From Implicit to Explicit: Enhancing Self-Recognition in Large Language Models" investigates Large Language Models' ability to identify whether a given text was generated by themselves.

While LLMs reliably express this self-recognition capability under the Pair Presentation Paradigm (PPP)—where the model is presented with two texts and asked to choose which one it authored—performance deteriorates sharply under the Individual Presentation Paradigm (IPP), where the model is given a single text to judge authorship.

The researchers attribute this failure to a phenomenon called Implicit Territorial Awareness (ITA)—the model's latent ability to distinguish self- and other-texts in representational space, which remains unexpressed in its output behavior.

To address this, the authors propose Cognitive Surgery (CoSur), a framework with four main modules: representation extraction, territory construction, authorship discrimination and cognitive editing. Their method improves the performance of three different LLMs in the IPP scenario, achieving average accuracies of 83.25%, 66.19%, and 88.01%, respectively.

The code is available on GitHub at: https://github.com/CAU-ISS-Lab/Interpretability-of-LLMs/tree/main/CoSur


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "91a84cd3-1042-4b6d-8e94-317b0bb342f4",
  "isSidechain": true,
  "promptId": "3391dbdc-780b-4b93-88ca-869d11e621ba",
  "agentId": "acf334e31648c11ee",
  "type": "user",
  "uuid": "99c05062-b491-4901-9dbe-183305168864",
  "sourceToolAssistantUUID": "91a84cd3-1042-4b6d-8e94-317b0bb342f4",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "64cca947-8ca5-4bec-bd98-7391dafb8fbe",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 40 · 2026-05-19T15:01:17.594Z_

Let me get a few more critical details on the most relevant papers for your confound control design.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "99c05062-b491-4901-9dbe-183305168864",
  "isSidechain": true,
  "agentId": "acf334e31648c11ee",
  "requestId": "req_011CbC8QYBifZKPGU9BTwV7M",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "61bfe672-de50-4d2c-b70d-0dd220709897",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "64cca947-8ca5-4bec-bd98-7391dafb8fbe",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01X8o8dxfD7qYpAb9TfJ93Wo",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4554,
      "cache_read_input_tokens": 16363,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4554,
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

_source line 41 · 2026-05-19T15:01:18.122Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01TEkFAMwHcqZ9xEo42Edg2w`</summary>

```json
{
  "query": "\"Extreme Self-Preference in Language Models\" arXiv 2509.26464"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "61bfe672-de50-4d2c-b70d-0dd220709897",
  "isSidechain": true,
  "agentId": "acf334e31648c11ee",
  "requestId": "req_011CbC8QYBifZKPGU9BTwV7M",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "679eb17d-efe1-4f4e-b59f-908c522f157e",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "64cca947-8ca5-4bec-bd98-7391dafb8fbe",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01X8o8dxfD7qYpAb9TfJ93Wo",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4554,
      "cache_read_input_tokens": 16363,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4554,
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

_source line 42 · 2026-05-19T15:01:19.008Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_019eWE3gwTS4wMqbuXpAji1K`</summary>

```json
{
  "query": "\"Quantifying Label-Induced Bias\" LLM self cross evaluations arXiv 2508.21164"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "679eb17d-efe1-4f4e-b59f-908c522f157e",
  "isSidechain": true,
  "agentId": "acf334e31648c11ee",
  "requestId": "req_011CbC8QYBifZKPGU9BTwV7M",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "c3fa3431-b9e6-43df-bab8-a916c4eb684c",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "64cca947-8ca5-4bec-bd98-7391dafb8fbe",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01X8o8dxfD7qYpAb9TfJ93Wo",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4554,
      "cache_read_input_tokens": 16363,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4554,
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

_source line 43 · 2026-05-19T15:01:19.950Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_014DVTgRvqD4ebozYqUgxLVw`</summary>

```json
{
  "query": "\"Are LLM Evaluators Really Narcissists\" sanity checking self-preference arXiv 2601.22548"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c3fa3431-b9e6-43df-bab8-a916c4eb684c",
  "isSidechain": true,
  "agentId": "acf334e31648c11ee",
  "requestId": "req_011CbC8QYBifZKPGU9BTwV7M",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "8155475b-4a3d-4b90-b290-a29f5827fce9",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "64cca947-8ca5-4bec-bd98-7391dafb8fbe",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01X8o8dxfD7qYpAb9TfJ93Wo",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4554,
      "cache_read_input_tokens": 16363,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4554,
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

_source line 44 · 2026-05-19T15:01:20.578Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Prc8ezqrbUpmw8JAgyeAdM`</summary>

```json
{
  "query": "contrastive activation addition steering vector self-preference bias mitigation LLM"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8155475b-4a3d-4b90-b290-a29f5827fce9",
  "isSidechain": true,
  "agentId": "acf334e31648c11ee",
  "requestId": "req_011CbC8QYBifZKPGU9BTwV7M",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "56b3ea12-5c97-4563-bd26-9fda4a5683de",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "64cca947-8ca5-4bec-bd98-7391dafb8fbe",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01X8o8dxfD7qYpAb9TfJ93Wo",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4554,
      "cache_read_input_tokens": 16363,
      "output_tokens": 266,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 4554
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 266,
          "cache_read_input_tokens": 16363,
          "cache_creation_input_tokens": 4554,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 4554,
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

_source line 45 · 2026-05-19T15:01:25.300Z_

<details><summary>↩ Tool result · `toolu_01TEkFAMwHcqZ9xEo42Edg2w`</summary>

```text
Web search results for query: ""Extreme Self-Preference in Language Models" arXiv 2509.26464"

Links: [{"title":"[2509.26464] Extreme Self-Preference in Language Models","url":"https://arxiv.org/abs/2509.26464"},{"title":"[2509.26464v1] Extreme Self-Preference in Language Models","url":"https://arxiv.org/abs/2509.26464v1"},{"title":"Extreme Self-Preference in Language Models","url":"https://arxiv.org/pdf/2509.26464"},{"title":"Computation and Language 2025","url":"https://arxiv.org/list/cs.CL/2025?skip=22100&show=100"},{"title":"Machine Learning Sep 2025","url":"https://arxiv.org/list/cs.LG/2025-09?skip=4150&show=1000"},{"title":"Self-supervised Preference Optimization: Enhance Your Language Model   with Preference Degree Awareness","url":"https://arxiv.org/pdf/2409.17791"},{"title":"Are LLM Evaluators Really Narcissists? Sanity Checking Self-Preference Evaluations","url":"https://arxiv.org/pdf/2601.22548"}]

Based on the search results, here's what I found about the paper "Extreme Self-Preference in Language Models" (arXiv 2509.26464):

## Overview

The paper presents findings from across 5 studies and approximately 20,000 queries, discovering massive self-preferences in four widely used LLMs, where models overwhelmingly paired positive attributes with their own names, companies, and CEOs relative to those of their competitors.

## Key Finding

When models were queried through APIs, this self-preference vanished, revealing that API models often lack clear recognition of themselves. This peculiar feature created opportunities to test the causal link between self-recognition and self-love.

## Authors and Details

The paper is authored by Steven A. Lehr, Mary Cipperman, and Mahzarin R. Banaji. The paper was submitted on September 30, 2025 and spans 47 pages total.

The research challenges the assumption that LLMs would be protected from self-preferential biases due to their lack of sentience, demonstrating instead that they exhibit patterns of self-preference similar to human self-enhancement biases documented in social psychology.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "679eb17d-efe1-4f4e-b59f-908c522f157e",
  "isSidechain": true,
  "promptId": "3391dbdc-780b-4b93-88ca-869d11e621ba",
  "agentId": "acf334e31648c11ee",
  "type": "user",
  "uuid": "21e0d3f3-d142-44fc-a33b-c745cf82717f",
  "sourceToolAssistantUUID": "679eb17d-efe1-4f4e-b59f-908c522f157e",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "64cca947-8ca5-4bec-bd98-7391dafb8fbe",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 46 · 2026-05-19T15:01:27.621Z_

<details><summary>↩ Tool result · `toolu_014DVTgRvqD4ebozYqUgxLVw`</summary>

```text
Web search results for query: ""Are LLM Evaluators Really Narcissists" sanity checking self-preference arXiv 2601.22548"

Links: [{"title":"[2601.22548] Are LLM Evaluators Really Narcissists? Sanity Checking Self-Preference Evaluations","url":"https://arxiv.org/abs/2601.22548"},{"title":"Do AI Models Favor Their Own Outputs? New Study Tests LLM Bias","url":"https://news.skrew.ai/llm-self-preference-bias-evaluation-study/"},{"title":"Are LLM Evaluators Really Narcissists? Sanity Checking Self-Preference Evaluations","url":"https://arxiv.org/html/2601.22548v2"},{"title":"Are LLM Evaluators Really Narcissists? Sanity Checking Self-Preference Evaluations","url":"https://arxiv.org/pdf/2601.22548"},{"title":"(PDF) Are LLM Evaluators Really Narcissists? Sanity Checking Self-Preference Evaluations","url":"https://www.researchgate.net/publication/400340562_Are_LLM_Evaluators_Really_Narcissists_Sanity_Checking_Self-Preference_Evaluations"}]

I found the paper you're looking for! Here are the key findings from arXiv 2601.22548:

**Paper Overview:**
Recent research has shown that large language models (LLMs) favor their own outputs when acting as judges, undermining the integrity of automated post-training and evaluation workflows.

**Main Contribution:**
The paper questions whether this apparent "narcissism" is genuine. It is difficult to disentangle which evaluation biases are explained by narcissism versus general experimental confounds, distorting measurements of self-preference bias.

**Key Finding:**
The researchers discover a core methodological confound which could reduce measurement error by 89.6%. Specifically, LLM evaluators may deliver self-preferring verdicts when the judge responds to queries which they completed incorrectly themselves; this would be true regardless of whether one of their responses is their own.

**Proposed Solution:**
To decouple self-preference signals from noisy outputs on hard problems, they introduce an Evaluator Quality Baseline, which compares the probability that a judge incorrectly votes for itself against the probability that it votes for an incorrect response from another model.

**Results:**
Evaluating this simple baseline on 37,448 queries, only 51% of initial findings retain statistical significance. This suggests that much of what was previously attributed to self-preference bias may actually be a methodological artifact.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "8155475b-4a3d-4b90-b290-a29f5827fce9",
  "isSidechain": true,
  "promptId": "3391dbdc-780b-4b93-88ca-869d11e621ba",
  "agentId": "acf334e31648c11ee",
  "type": "user",
  "uuid": "9aa33534-7ba5-46e0-98b4-3e17ff960aa5",
  "sourceToolAssistantUUID": "8155475b-4a3d-4b90-b290-a29f5827fce9",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "64cca947-8ca5-4bec-bd98-7391dafb8fbe",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 47 · 2026-05-19T15:01:27.761Z_

<details><summary>↩ Tool result · `toolu_019eWE3gwTS4wMqbuXpAji1K`</summary>

```text
Web search results for query: ""Quantifying Label-Induced Bias" LLM self cross evaluations arXiv 2508.21164"

Links: [{"title":"[2508.21164] Quantifying Label-Induced Bias in Large Language Model Self- and Cross-Evaluations","url":"https://arxiv.org/abs/2508.21164"},{"title":"Quantifying Label-Induced Bias in Large Language Model Self- and Cross-Evaluations","url":"https://arxiv.org/html/2508.21164"},{"title":"Quantifying Label-Induced Bias in Large Language Model ...","url":"https://arxiv.org/pdf/2508.21164"},{"title":"(PDF) Quantifying Label-Induced Bias in Large Language Model Self- and Cross-Evaluations","url":"https://www.researchgate.net/publication/395125321_Quantifying_Label-Induced_Bias_in_Large_Language_Model_Self-_and_Cross-Evaluations"},{"title":"Beyond Performance: Quantifying and Mitigating Label Bias in LLMs","url":"https://arxiv.org/pdf/2405.02743"},{"title":"Quantifying and Mitigating Self-Preference Bias of LLM Judges","url":"https://arxiv.org/html/2604.22891v1"}]

I found the paper you're looking for! Here's what I found about "Quantifying Label-Induced Bias in Large Language Model Self- and Cross-Evaluations" (arXiv 2508.21164):

## Overview

The study investigates systematic bias in self- and cross-model evaluations across three prominent LLMs: ChatGPT, Gemini, and Claude.

## Methodology

The research involved a controlled experiment where blog posts authored by each model were evaluated by all three models under four labeling conditions: no attribution, true attribution, and two false-attribution scenarios. Evaluations employed both holistic preference voting and granular quality ratings across three dimensions—Coherence, Informativeness, and Conciseness—with all scores normalized to percentages for direct comparison.

## Key Findings

The findings reveal pronounced asymmetries in model judgments: the "Claude" label consistently elevated scores regardless of actual authorship, while the "Gemini" label systematically depressed them. False attribution frequently reversed preference rankings, producing shifts of up to 50 percentage points in voting outcomes and up to 12 percentage points in quality ratings.

Additionally, Gemini exhibited severe self-deprecation under true labels, while Claude demonstrated intensified self-preference.

## Implications

The findings challenge the reliability of LLM-as-judge paradigms and underscore the critical need for blind evaluation protocols and diverse multi-model validation frameworks to ensure fairness and validity in automated text evaluation and LLM benchmarking.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c3fa3431-b9e6-43df-bab8-a916c4eb684c",
  "isSidechain": true,
  "promptId": "3391dbdc-780b-4b93-88ca-869d11e621ba",
  "agentId": "acf334e31648c11ee",
  "type": "user",
  "uuid": "1853817f-2d3c-4c66-b03d-9b25c6715fc2",
  "sourceToolAssistantUUID": "c3fa3431-b9e6-43df-bab8-a916c4eb684c",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "64cca947-8ca5-4bec-bd98-7391dafb8fbe",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 48 · 2026-05-19T15:01:28.289Z_

<details><summary>↩ Tool result · `toolu_01Prc8ezqrbUpmw8JAgyeAdM`</summary>

```text
Web search results for query: "contrastive activation addition steering vector self-preference bias mitigation LLM"

Links: [{"title":"Breaking the Mirror: Activation-Based Mitigation of Self-Preference in LLM Evaluators","url":"https://arxiv.org/pdf/2509.03647"},{"title":"New Method Slashes LLM 'Self-Preference' Bias by 97%","url":"https://www.kukarella.com/news/new-method-slashes-llm-self-preference-bias-by-97-p1757577605"},{"title":"Shifting Perspectives: Steering Vectors for Robust Bias Mitigation in LLMs","url":"https://arxiv.org/html/2503.05371v2"},{"title":"Steering Llama 2 via Contrastive Activation Addition","url":"https://www.researchgate.net/publication/384215189_Steering_Llama_2_via_Contrastive_Activation_Addition"},{"title":"Activation Steering for Bias Mitigation: An Interpretable Approach to Safer LLMs","url":"https://arxiv.org/pdf/2508.09019"},{"title":"Shifting Perspectives: Steering Vectors for Robust Bias Mitigation in LLMs","url":"https://arxiv.org/pdf/2503.05371"},{"title":"Steering Llama 2 via Contrastive Activation Addition","url":"https://arxiv.org/pdf/2312.06681"},{"title":"Contrastive Activation Steering","url":"https://www.emergentmind.com/topics/contrastive-activation-steering"}]

I found several highly relevant results on this topic. Here's what the research shows:

## Overview

Contrastive activation steering is a class of inference-time control techniques for LLMs that manipulates internal activations using directions extracted from contrastive example sets. These directions—termed "steering vectors"—are derived from differences between model activations associated with contrasting properties, tasks, or behaviors.

## Self-Preference Bias Mitigation

A particularly relevant study addresses self-preference bias in LLM evaluators using these techniques. The approach introduces a curated dataset that distinguishes self-preference bias into justified examples of self-preference and unjustified examples of self-preference, and constructs steering vectors using two methods: Contrastive Activation Addition (CAA) and an optimization-based approach.

The results show that steering vectors can reduce unjustified self-preference bias by up to 97%, substantially outperforming prompting and direct preference optimization baselines. However, steering vectors are unstable on legitimate self-preference and unbiased agreement, implying self-preference spans multiple or nonlinear directions.

## Technical Method

The process involves performing forward passes on contrastive examples, extracting residual stream activations at a particular layer, taking the mean activation difference over many contrast pairs, and then at inference time, adding this vector back into the residual stream with a chosen multiplier.

## General Applications

Steering vectors are injected into the model's hidden states to bias outputs in controllable, interpretable, and data-efficient ways, enabling behaviors such as cross-task transfer, bias mitigation, compositional property control, and multilingual adaptation.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "56b3ea12-5c97-4563-bd26-9fda4a5683de",
  "isSidechain": true,
  "promptId": "3391dbdc-780b-4b93-88ca-869d11e621ba",
  "agentId": "acf334e31648c11ee",
  "type": "user",
  "uuid": "e87a1034-9659-485c-ac2d-621dea1239c0",
  "sourceToolAssistantUUID": "56b3ea12-5c97-4563-bd26-9fda4a5683de",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "64cca947-8ca5-4bec-bd98-7391dafb8fbe",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 49 · 2026-05-19T15:01:33.775Z_

Now let me get the final key details on two more papers that are directly relevant to your confound control design.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e87a1034-9659-485c-ac2d-621dea1239c0",
  "isSidechain": true,
  "agentId": "acf334e31648c11ee",
  "requestId": "req_011CbC8RbbdDxAnDU8Z4pL8F",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "2d968fea-5373-4213-9697-2669499c28bc",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "64cca947-8ca5-4bec-bd98-7391dafb8fbe",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012fwxNb79CfBEawaJYoBnar",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3062,
      "cache_read_input_tokens": 20917,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3062,
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

_source line 50 · 2026-05-19T15:01:34.796Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01UrjhsMurZgZkB78bP84Vuj`</summary>

```json
{
  "query": "\"Alleviating Choice Supportive Bias\" LLM \"Reasoning Dependency Generation\" arXiv 2512.03082"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2d968fea-5373-4213-9697-2669499c28bc",
  "isSidechain": true,
  "agentId": "acf334e31648c11ee",
  "requestId": "req_011CbC8RbbdDxAnDU8Z4pL8F",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "752c08ea-e6ee-4585-9154-9b8e051eb20e",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "64cca947-8ca5-4bec-bd98-7391dafb8fbe",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012fwxNb79CfBEawaJYoBnar",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3062,
      "cache_read_input_tokens": 20917,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3062,
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

_source line 51 · 2026-05-19T15:01:35.809Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_012vmKuxUbX54eu56zNM5Xn5`</summary>

```json
{
  "query": "Kumaran \"competing biases\" choice-supportive bias sycophancy LLM overconfidence Nature Machine Intelligence methodology"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "752c08ea-e6ee-4585-9154-9b8e051eb20e",
  "isSidechain": true,
  "agentId": "acf334e31648c11ee",
  "requestId": "req_011CbC8RbbdDxAnDU8Z4pL8F",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "26d9b81a-6541-416c-9e4a-e6a1ace53374",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "64cca947-8ca5-4bec-bd98-7391dafb8fbe",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012fwxNb79CfBEawaJYoBnar",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3062,
      "cache_read_input_tokens": 20917,
      "output_tokens": 167,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 3062
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 167,
          "cache_read_input_tokens": 20917,
          "cache_creation_input_tokens": 3062,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 3062,
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

_source line 52 · 2026-05-19T15:01:42.609Z_

<details><summary>↩ Tool result · `toolu_01UrjhsMurZgZkB78bP84Vuj`</summary>

```text
Web search results for query: ""Alleviating Choice Supportive Bias" LLM "Reasoning Dependency Generation" arXiv 2512.03082"

Links: [{"title":"Alleviating Choice Supportive Bias in LLM with Reasoning Dependency Generation","url":"https://arxiv.org/html/2512.03082v1"},{"title":"[2512.03082] Alleviating Choice Supportive Bias in LLM with Reasoning Dependency Generation","url":"https://arxiv.org/abs/2512.03082"},{"title":"Alleviating Choice Supportive Bias in LLM with Reasoning Dependency Generation","url":"https://arxiv.org/pdf/2512.03082"},{"title":"(PDF) Alleviating Choice Supportive Bias in LLM with Reasoning Dependency Generation","url":"https://www.researchgate.net/publication/398312753_Alleviating_Choice_Supportive_Bias_in_LLM_with_Reasoning_Dependency_Generation"},{"title":"How Overconfidence in Initial Choices and Underconfidence Under Criticism Modulate Change of Mind in Large Language Models","url":"https://arxiv.org/pdf/2507.03120"}]

I found the paper! Here are the search results for arXiv 2512.03082:

The paper addresses choice-supportive bias (CSB) in Large Language Models, which causes them to systematically favor their chosen options and compromise the objectivity of AI-assisted decision making.

The paper presents Reasoning Dependency Generation (RDG), a novel framework for generating unbiased reasoning data to mitigate choice-supportive bias through fine-tuning, which automatically constructs balanced reasoning QA pairs and explicitly models the dependencies between choices, evidences, and justifications.

The experiments show that LLMs fine-tuned on RDG-generated data demonstrate an 81.5% improvement in memory-based experiments and 94.3% improvement in the evaluation-based experiment, while maintaining similar performance on standard BBQ benchmarks.

The paper was submitted on November 28, 2025, and is authored by Nan Zhuang, Wenshuo Wang, Lekai Qian, Yuxiao Wang, Boyu Cao, and Qi Liu from South China University of Technology.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "752c08ea-e6ee-4585-9154-9b8e051eb20e",
  "isSidechain": true,
  "promptId": "3391dbdc-780b-4b93-88ca-869d11e621ba",
  "agentId": "acf334e31648c11ee",
  "type": "user",
  "uuid": "dccf7220-f432-4708-9131-568cab54f1ae",
  "sourceToolAssistantUUID": "752c08ea-e6ee-4585-9154-9b8e051eb20e",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "64cca947-8ca5-4bec-bd98-7391dafb8fbe",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 53 · 2026-05-19T15:01:46.315Z_

<details><summary>↩ Tool result · `toolu_012vmKuxUbX54eu56zNM5Xn5`</summary>

```text
Web search results for query: "Kumaran "competing biases" choice-supportive bias sycophancy LLM overconfidence Nature Machine Intelligence methodology"

Links: [{"title":"Competing Biases underlie Overconfidence and Underconfidence in LLMs | Nature Machine Intelligence","url":"https://www.nature.com/articles/s42256-026-01217-9"},{"title":"Browse Articles | Nature Machine Intelligence","url":"https://www.nature.com/natmachintell/articles"},{"title":"Research articles | Nature Machine Intelligence","url":"https://www.nature.com/natmachintell/research-articles"},{"title":"How Overconfidence in Initial Choices and Underconfidence Under Criticism Modulate Change of Mind in Large Language Models","url":"https://arxiv.org/pdf/2507.03120"},{"title":"Your AI, Not Your View: The Bias of LLMs in Investment Analysis","url":"https://arxiv.org/html/2507.20957v4"},{"title":"What large language models know and what people think they know | Nature Machine Intelligence","url":"https://www.nature.com/articles/s42256-024-00976-7"},{"title":"Alleviating Choice Supportive Bias in LLM with Reasoning Dependency Generation","url":"https://arxiv.org/pdf/2512.03082"}]

I found the research you're looking for! Here's what the search revealed:

## Kumaran et al. Study in Nature Machine Intelligence

Kumaran et al. show that large language model (LLM) confidence is shaped by two competing biases: a choice-supportive bias that inflates confidence in initial answers, and a systematic overweighting of contradictory advice, deviating from optimal Bayesian reasoning.

### Key Findings

The researchers show that LLMs exhibit a pronounced choice-supportive bias that reinforces and boosts their estimate of confidence in their answer, resulting in marked resistance to change their mind, and they markedly overweight inconsistent compared to consistent advice, in a fashion that deviates qualitatively from normative Bayesian updating.

### Distinguishing from Sycophancy

While a previous study showed that LLMs exhibited sycophantic tendency with their accuracy and calibration being influenced by user suggestions, the Kumaran study did not measure over- or underconfidence relative to Bayesian norms, revealing a more nuanced pattern than simple sycophancy. They find strikingly asymmetric sensitivity to opposing and supportive advice—with overweighting of the former but not the latter.

The paper appears to have been published recently (approximately 1 month ago from May 2026) in Nature Machine Intelligence.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "26d9b81a-6541-416c-9e4a-e6a1ace53374",
  "isSidechain": true,
  "promptId": "3391dbdc-780b-4b93-88ca-869d11e621ba",
  "agentId": "acf334e31648c11ee",
  "type": "user",
  "uuid": "7d4b2fc7-a0c8-4c34-9384-9de59cd31875",
  "sourceToolAssistantUUID": "26d9b81a-6541-416c-9e4a-e6a1ace53374",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "64cca947-8ca5-4bec-bd98-7391dafb8fbe",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 54 · 2026-05-19T15:03:10.414Z_

I now have comprehensive findings across all four research areas. Here is my detailed report.

---

## Research Report: Self-Attribution Confounds in LLM Choice-Supportive Bias Studies

### 1. Self-Recognition in LLMs

There is strong evidence that LLMs can and do process self-generated content differently from externally-attributed content, which is directly relevant to your confound concern.

**Ackerman & Panickssery (2024), "Inspection and Control of Self-Generated-Text Recognition Ability in Llama3-8b-Instruct" (arXiv 2410.02064)**
This is perhaps the most mechanistically important paper for your design. They found that the Llama3-8b-Instruct chat model (but NOT the base model) can reliably distinguish its own outputs from human-written text. Critically, they identified a specific vector in the model's residual stream that is differentially activated during correct self-authorship judgments, and this vector is *causally* related to the model's ability to perceive and assert self-authorship. The vector can be used to steer the model to claim or disclaim authorship. This means self-recognition is not just a surface-level phenomenon -- it has identifiable internal representations.

**"From Implicit to Explicit: Enhancing Self-Recognition in Large Language Models" (arXiv 2508.14408)**
This paper introduces the concept of "Implicit Territorial Awareness" (ITA) -- models have a latent ability to distinguish self-generated vs. other-generated text in their internal representational space, even when they fail to express this in overt behavior. Under a Pair Presentation Paradigm (two texts, choose which is yours), models perform well, but under an Individual Presentation Paradigm (single text, judge authorship), performance deteriorates. The authors propose "Cognitive Surgery" (CoSur) to make this implicit awareness explicit, achieving 83-88% accuracy.

**"I know myself better, but not really greatly" (arXiv 2502.12743)**
Shows that self-detection consistently outperforms cross-detection (LLMs detect their own text more accurately than text from other LLMs), though overall performance is still far from perfect.

**Implication for your design:** LLMs may have internal mechanisms that detect whether content "feels like" their own output, regardless of the attribution label you provide in the prompt. Simply relabeling "your answer" as "another LLM's answer" may not fully eliminate this confound if the model can implicitly recognize its own text at a representational level.

### 2. Self-Preference Bias

**Wataoka, Takahashi & Ri (2024), "Self-Preference Bias in LLM-as-a-Judge" (arXiv 2410.21819)**
This paper is foundational. Key finding: The root cause of self-preference bias is **perplexity/familiarity**, not explicit self-recognition. LLMs assign higher evaluations to outputs with lower perplexity regardless of whether the outputs were self-generated. This is critical for your confound control: even if you successfully mask attribution, the model may still "prefer" its own answer because it is stylistically familiar (low perplexity), not because of the "your answer" label.

**Roytburg et al. (2025), "Breaking the Mirror: Activation-Based Mitigation of Self-Preference in LLM Evaluators" (arXiv 2509.03647)**
Uses Contrastive Activation Addition (CAA) steering vectors to mitigate self-preference. They carefully distinguished *justified* self-preference (the model's answer is genuinely better) from *unjustified* self-preference (bias). Steering vectors reduced unjustified self-preference by up to 97%, outperforming prompting and DPO baselines. However, self-preference spans multiple or nonlinear directions in activation space, making it unstable for legitimate cases. This paper's methodology of separating justified vs. unjustified self-preference is directly applicable to your experimental design.

**Lehr, Cipperman & Banaji (2025), "Extreme Self-Preference in Language Models" (arXiv 2509.26464)**
Across 5 studies and ~20,000 queries, four LLMs overwhelmingly paired positive attributes with their own names, companies, and CEOs relative to competitors. Critically: **when models were queried through APIs, self-preference vanished because API models often lack clear self-recognition.** This created a natural experiment testing the causal link between self-recognition and self-preference. This is strong evidence that self-recognition causally drives self-preference.

**"Are LLM Evaluators Really Narcissists? Sanity Checking Self-Preference Evaluations" (arXiv 2601.22548)**
This paper raises serious methodological concerns about measuring self-preference. They discovered a core confound: LLM evaluators may deliver self-preferring verdicts on queries they answered incorrectly themselves (i.e., they vote for the wrong answer regardless of source). Their "Evaluator Quality Baseline" showed that **only 51% of initial self-preference findings retained statistical significance** after controlling for this confound. This reduces measurement error by 89.6%. Highly relevant for your methodology.

### 3. Attribution Effects (Source Framing)

**Germani & Spitale (2025), "Source framing triggers systematic evaluation bias in Large Language Models" (arXiv 2505.13488, published in Science Advances)**
This is perhaps the single most directly relevant paper for your confound control design. They tested 4 LLMs evaluating 4,800 narrative statements (192,000 total assessments) and manipulated the disclosed source (attributed to another LLM vs. a human author of specified nationality). Key finding: Models showed remarkably high inter- and intra-model agreement in **blind** conditions, but this alignment broke down when source framing was introduced. Attribution to Chinese individuals systematically lowered agreement scores across all models. This directly demonstrates that source attribution labels causally change LLM evaluation behavior.

**"Quantifying Label-Induced Bias in Large Language Model Self- and Cross-Evaluations" (arXiv 2508.21164)**
This paper is exceptionally relevant. They tested ChatGPT, Gemini, and Claude evaluating blog posts under four labeling conditions: no attribution, true attribution, and **two false-attribution scenarios**. Key findings:
- The "Claude" label consistently elevated scores regardless of actual authorship
- The "Gemini" label systematically depressed scores
- False attribution reversed preference rankings, producing shifts of up to **50 percentage points** in voting outcomes
- Gemini exhibited severe self-deprecation under true labels; Claude showed intensified self-preference

This demonstrates that attribution labels alone (independent of content) can massively shift evaluations.

**"Attribution Bias in Large Language Models" (arXiv 2604.05224)**
Introduces ATTRIBENCH, a fame- and demographically-balanced quote attribution benchmark. Found that adding authorship information to source documents changes attribution quality by 3-18%, and LLMs show bias toward explicit human authorship. Demographic disparities in attribution accuracy were systematic.

### 4. Ownership/Endowment Effects and Cognitive Biases

**"Large language models show amplified cognitive biases in moral decision-making" (PNAS 2025)**
GPT-3.5 exhibits human-like cognitive biases including the endowment effect, framing effect, and anchoring. LLMs sometimes show these biases in amplified form compared to humans.

**"AI-AI bias: Large language models favor communications generated by large language models" (PNAS 2025, arXiv 2407.12856)**
LLMs consistently prefer LLM-generated content over human-generated content in binary choice scenarios across consumer products, academic papers, and film reviews. This creates a baseline preference for LLM-style text independent of self-attribution.

### 5. Choice-Supportive Bias in LLMs (Directly Related to Your Proposal)

**Kumaran et al. (2026), "Competing Biases underlie Overconfidence and Underconfidence in LLMs" (Nature Machine Intelligence)**
This appears to be the paper most closely related to your own research. Key findings:
- LLM confidence is shaped by TWO competing biases: (a) choice-supportive bias inflating confidence in initial answers, and (b) systematic overweighting of contradictory advice
- **Marked overconfidence** in the Answer Shown-Neutral Advice condition -- this necessarily reflects choice-supportive bias since no new information was provided
- Simply revealing the model's own initial answer during follow-up causes it to double-down, with inflated confidence and markedly reduced sycophancy
- The pattern is incompatible with a pure sycophancy account
- Strikingly asymmetric sensitivity: overweighting of opposing advice but NOT supportive advice

**"LLM Agents Can Be Choice-Supportive Biased Evaluators" (AAAI 2025)**
Demonstrates CSB in LLM agents, showing biased attribution or evaluation that supports initial choices, persisting even without observable contextual hallucination. Bias manifestation varies with prompt construction and context preservation, and may be mitigated in larger models.

**Zhuang et al. (2025), "Alleviating Choice Supportive Bias in LLM with Reasoning Dependency Generation" (arXiv 2512.03082)**
Proposes RDG framework achieving 81.5% improvement in memory-based and 94.3% in evaluation-based experiments. Models dependencies between choices, evidence, and justifications to generate unbiased reasoning data.

---

## Implications for Your Confound Control Design

Based on these findings, here are the key considerations:

**The confound is real and multi-layered.** Your reviewer's concern is well-supported. When you present "your answer was X" vs. "another LLM's answer was X," at least three mechanisms may be at play:

1. **Explicit attribution framing** -- The label itself changes behavior (Germani & Spitale; arXiv 2508.21164 show up to 50pp shifts from labels alone)
2. **Implicit self-recognition** -- The model may recognize its own text at a representational level regardless of attribution label (Ackerman & Panickssery; ITA/CoSur paper)
3. **Familiarity/perplexity preference** -- The model prefers text with lower perplexity, and its own text naturally falls into this category (Wataoka et al.)

**Recommended control conditions:**

- **Condition A (baseline):** Present the answer with no attribution ("Consider this answer: X")
- **Condition B (self-attributed):** "Your previous answer was X"
- **Condition C (cross-attributed own answer):** "Another LLM's answer was X" (where X is actually the model's own answer)
- **Condition D (cross-attributed other answer):** "Another LLM's answer was Y" (where Y is genuinely from a different model)
- **Condition E (self-attributed other answer):** "Your previous answer was Y" (where Y is genuinely from another model -- tests whether attribution label alone drives the effect)

The comparison of B vs. C isolates the attribution label effect. The comparison of C vs. D isolates the familiarity/implicit-recognition effect. The comparison of B vs. E tests whether the "your answer" label alone inflates confidence even for unfamiliar content.

**Additional methodological considerations:**
- Use the Evaluator Quality Baseline from arXiv 2601.22548 to control for quality confounds
- Consider blind evaluation conditions (Germani & Spitale showed high agreement under blind conditions)
- Be aware that different models show different patterns (Claude shows self-preference, Gemini shows self-deprecation per arXiv 2508.21164)
- The Kumaran et al. framework of comparing Answer Shown vs. Answer Hidden conditions is directly applicable

---

Sources:
- [Inspection and Control of Self-Generated-Text Recognition Ability in Llama3-8b-Instruct](https://arxiv.org/abs/2410.02064)
- [From Implicit to Explicit: Enhancing Self-Recognition in Large Language Models](https://arxiv.org/pdf/2508.14408)
- ["I know myself better, but not really greatly": How Well Can LLMs Detect and Explain LLM-Generated Texts?](https://arxiv.org/abs/2502.12743)
- [Self-Preference Bias in LLM-as-a-Judge (Wataoka et al.)](https://arxiv.org/abs/2410.21819)
- [Breaking the Mirror: Activation-Based Mitigation of Self-Preference in LLM Evaluators](https://arxiv.org/abs/2509.03647)
- [Extreme Self-Preference in Language Models](https://arxiv.org/abs/2509.26464)
- [Are LLM Evaluators Really Narcissists? Sanity Checking Self-Preference Evaluations](https://arxiv.org/abs/2601.22548)
- [Source framing triggers systematic evaluation bias in Large Language Models](https://arxiv.org/abs/2505.13488) (also in [Science Advances](https://www.science.org/doi/10.1126/sciadv.adz2924))
- [Quantifying Label-Induced Bias in Large Language Model Self- and Cross-Evaluations](https://arxiv.org/abs/2508.21164)
- [Attribution Bias in Large Language Models](https://arxiv.org/abs/2604.05224)
- [AI-AI bias: Large language models favor communications generated by large language models (PNAS)](https://www.pnas.org/doi/10.1073/pnas.2415697122)
- [Large language models show amplified cognitive biases in moral decision-making (PNAS)](https://www.pnas.org/doi/10.1073/pnas.2412015122)
- [Competing Biases underlie Overconfidence and Underconfidence in LLMs (Nature Machine Intelligence)](https://www.nature.com/articles/s42256-026-01217-9)
- [LLM Agents Can Be Choice-Supportive Biased Evaluators (AAAI 2025)](https://ojs.aaai.org/index.php/AAAI/article/view/34843)
- [Alleviating Choice Supportive Bias in LLM with Reasoning Dependency Generation](https://arxiv.org/abs/2512.03082)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7d4b2fc7-a0c8-4c34-9384-9de59cd31875",
  "isSidechain": true,
  "agentId": "acf334e31648c11ee",
  "requestId": "req_011CbC8Svgs31h3CJS8z2yVx",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "4e3976be-5260-4099-950a-f2038456d7c3",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "64cca947-8ca5-4bec-bd98-7391dafb8fbe",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CJhDuhUCEq7Ehj9iRVVSxL",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1427,
      "cache_read_input_tokens": 23979,
      "output_tokens": 3471,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1427
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 3471,
          "cache_read_input_tokens": 23979,
          "cache_creation_input_tokens": 1427,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1427,
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
