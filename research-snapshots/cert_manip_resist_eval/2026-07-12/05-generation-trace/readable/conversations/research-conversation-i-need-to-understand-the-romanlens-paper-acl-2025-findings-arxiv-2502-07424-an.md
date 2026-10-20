# Research conversation: I need to understand the RomanLens paper (ACL 2025 Findings, arXiv:2502.07424) and its implications for using script tra

**The Weakest Link Across Panel Sizes: Predictor Relevance Patterns in Multi-Judge LLM Evaluation under Adversarial Manipulation (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 25
- **Recorded user turns:** 1
- **Tool calls:** 9
- **Original source:** `logs/chats/exported-trajectories/account-1/agent-a5388c7e3e9236e88.jsonl`
- **Structured JSON:** [`7ced54003043b0db9d47.json`](../../sessions/7c/7ced54003043b0db9d47.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

25 recorded events

### User

_source line 1 · 2026-05-19T18:10:22.523Z_

I need to understand the RomanLens paper (ACL 2025 Findings, arXiv:2502.07424) and its implications for using script transliteration as a "clean" tokenization intervention. I also need to find "Beyond Text Compression" (ACL 2025) and "EfficientXLang" (arXiv:2507.00246).

Please do the following:
1. Fetch https://arxiv.org/abs/2502.07424 (RomanLens) and extract: (a) the main finding about "latent romanization" in LLMs, (b) which models and languages they study, (c) specific evidence that LLMs internally represent non-Roman text in romanized form, (d) implications for using transliteration as an experimental intervention — does it really violate the exclusion restriction?
2. Search for "Beyond Text Compression ACL 2025 tokenizer effects" and fetch the paper. Extract: main findings about when tokenizer effects are negligible vs significant.
3. Fetch https://arxiv.org/abs/2507.00246 (EfficientXLang) and extract: main findings about non-English reasoning token efficiency.
4. Search for "script transliteration intervention causal inference NLP 2025 2026" for any work on transliteration as experimental manipulation

Report back with:
- What RomanLens actually shows and how it complicates the transliteration intervention
- Whether transliteration can still be used with appropriate caveats, or if it needs to be replaced
- Key findings from "Beyond Text Compression" and "EfficientXLang" relevant to the proposal
- How to honestly frame the transliteration intervention given these complications

Keep your report under 500 words with specific details.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "885fac21-638b-49aa-852f-c24d838cbccc",
  "agentId": "a5388c7e3e9236e88",
  "type": "user",
  "uuid": "8a2a2fc0-9679-4a72-a63b-8c7f7bdef228",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "5c192117-ae74-4acd-8f38-48b668acc23f",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 2 · 2026-05-19T18:10:22.527Z_

```json
{
  "parentUuid": "8a2a2fc0-9679-4a72-a63b-8c7f7bdef228",
  "isSidechain": true,
  "agentId": "a5388c7e3e9236e88",
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
  "uuid": "8c1c77fc-a68d-4aee-ac49-2660d5cf83ae",
  "timestamp": "2026-05-19T18:10:22.527Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "5c192117-ae74-4acd-8f38-48b668acc23f",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 3 · 2026-05-19T18:10:22.528Z_

```json
{
  "parentUuid": "8c1c77fc-a68d-4aee-ac49-2660d5cf83ae",
  "isSidechain": true,
  "agentId": "a5388c7e3e9236e88",
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "e26b28c4-1839-465f-91a6-5f6bd7350ccf",
  "timestamp": "2026-05-19T18:10:22.528Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "5c192117-ae74-4acd-8f38-48b668acc23f",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Assistant

_source line 4 · 2026-05-19T18:10:25.063Z_



I'll fetch the papers and search for the relevant literature in parallel.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e26b28c4-1839-465f-91a6-5f6bd7350ccf",
  "isSidechain": true,
  "agentId": "a5388c7e3e9236e88",
  "requestId": "req_011CbCNq6MH7EXfoHFiZWBsk",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "c48bf792-a42f-410b-a1dc-7feb1f4eecfc",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "5c192117-ae74-4acd-8f38-48b668acc23f",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NFZrDSJ76vc5A8KFXNCJgf",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1713,
      "cache_read_input_tokens": 7409,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1713,
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

_source line 5 · 2026-05-19T18:10:25.629Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01NzmsGzRu3WwKpNRmffU8fT`</summary>

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
  "parentUuid": "c48bf792-a42f-410b-a1dc-7feb1f4eecfc",
  "isSidechain": true,
  "agentId": "a5388c7e3e9236e88",
  "requestId": "req_011CbCNq6MH7EXfoHFiZWBsk",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "e5f6c00c-5c6c-453b-9554-b4174bb593d2",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "5c192117-ae74-4acd-8f38-48b668acc23f",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NFZrDSJ76vc5A8KFXNCJgf",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1713,
      "cache_read_input_tokens": 7409,
      "output_tokens": 95,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1713
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 95,
          "cache_read_input_tokens": 7409,
          "cache_creation_input_tokens": 1713,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1713,
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

_source line 6 · 2026-05-19T18:10:25.631Z_

<details><summary>↩ Tool result · `toolu_01NzmsGzRu3WwKpNRmffU8fT`</summary>

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
  "parentUuid": "e5f6c00c-5c6c-453b-9554-b4174bb593d2",
  "isSidechain": true,
  "promptId": "885fac21-638b-49aa-852f-c24d838cbccc",
  "agentId": "a5388c7e3e9236e88",
  "type": "user",
  "uuid": "271bfcf6-3e2f-4d18-9d8c-96b281343699",
  "sourceToolAssistantUUID": "e5f6c00c-5c6c-453b-9554-b4174bb593d2",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "5c192117-ae74-4acd-8f38-48b668acc23f",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 7 · 2026-05-19T18:10:28.219Z_



Now I'll fetch all the papers and run the searches in parallel.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "271bfcf6-3e2f-4d18-9d8c-96b281343699",
  "isSidechain": true,
  "agentId": "a5388c7e3e9236e88",
  "requestId": "req_011CbCNqKrPXzXdWSjcFXjYd",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "b751271f-377f-46df-ab1e-69d36991a750",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "5c192117-ae74-4acd-8f38-48b668acc23f",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JZGtVF9LNMCiCaWSZy3UuB",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 2830,
      "cache_read_input_tokens": 7409,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2830,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 2,
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

_source line 8 · 2026-05-19T18:10:30.580Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_0117g1UQ8tz6MWxxBzuQq933`</summary>

```json
{
  "url": "https://arxiv.org/abs/2502.07424",
  "prompt": "Extract the following from this paper (RomanLens): 1) The main finding about \"latent romanization\" in LLMs. 2) Which specific models and languages they study. 3) Specific evidence that LLMs internally represent non-Roman text in romanized form (probing results, layer analysis, etc). 4) Implications: does this mean transliteration as an experimental intervention is problematic because the model already does it internally? Does it violate the exclusion restriction in causal inference terms?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b751271f-377f-46df-ab1e-69d36991a750",
  "isSidechain": true,
  "agentId": "a5388c7e3e9236e88",
  "requestId": "req_011CbCNqKrPXzXdWSjcFXjYd",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "be4f4051-9b3b-45a8-8252-a4d41d26c970",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "5c192117-ae74-4acd-8f38-48b668acc23f",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JZGtVF9LNMCiCaWSZy3UuB",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 2830,
      "cache_read_input_tokens": 7409,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2830,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 2,
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

_source line 9 · 2026-05-19T18:10:32.455Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01Ba3YJXWPBkKK4DyA4mArYG`</summary>

```json
{
  "url": "https://arxiv.org/abs/2507.00246",
  "prompt": "Extract the main findings of EfficientXLang about non-English reasoning token efficiency. What do they find about how many tokens models use for reasoning in different languages? What are the key results about efficiency of reasoning in non-English languages compared to English?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "be4f4051-9b3b-45a8-8252-a4d41d26c970",
  "isSidechain": true,
  "agentId": "a5388c7e3e9236e88",
  "requestId": "req_011CbCNqKrPXzXdWSjcFXjYd",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "e324bacc-36ea-487e-9d3b-ec62e4094613",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "5c192117-ae74-4acd-8f38-48b668acc23f",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JZGtVF9LNMCiCaWSZy3UuB",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 2830,
      "cache_read_input_tokens": 7409,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2830,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 2,
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

_source line 10 · 2026-05-19T18:10:32.835Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01DnyfKmfFZkCa3b7be8FEeu`</summary>

```json
{
  "query": "Beyond Text Compression ACL 2025 tokenizer effects NLP"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e324bacc-36ea-487e-9d3b-ec62e4094613",
  "isSidechain": true,
  "agentId": "a5388c7e3e9236e88",
  "requestId": "req_011CbCNqKrPXzXdWSjcFXjYd",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "28863e2e-4762-4497-afd4-d7c74d8e8acf",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "5c192117-ae74-4acd-8f38-48b668acc23f",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JZGtVF9LNMCiCaWSZy3UuB",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 2830,
      "cache_read_input_tokens": 7409,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2830,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 2,
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

_source line 11 · 2026-05-19T18:10:32.859Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01YSYFjWQNFzMAd7PkvUPm1K`</summary>

```json
{
  "query": "script transliteration intervention causal inference NLP 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "28863e2e-4762-4497-afd4-d7c74d8e8acf",
  "isSidechain": true,
  "agentId": "a5388c7e3e9236e88",
  "requestId": "req_011CbCNqKrPXzXdWSjcFXjYd",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "5bda7281-ff64-42dd-bc85-b71a0e24ec9a",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "5c192117-ae74-4acd-8f38-48b668acc23f",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JZGtVF9LNMCiCaWSZy3UuB",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 2830,
      "cache_read_input_tokens": 7409,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2830,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 2,
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

_source line 12 · 2026-05-19T18:10:34.949Z_

<details><summary>↩ Tool result · `toolu_0117g1UQ8tz6MWxxBzuQq933`</summary>

```text
# Summary of RomanLens Paper

## 1) Main Finding on Latent Romanization

The paper identifies that LLMs represent non-Roman script words in Romanized form within intermediate layers before transitioning to native script. This phenomenon, termed "Latent Romanization," suggests models leverage Roman character representations as an implicit bridge for multilingual processing.

## 2) Models and Languages Studied

The webpage does not specify which particular LLM architectures were analyzed or provide an exhaustive language list. The abstract references "languages written in non-Roman scripts" generally, without naming specific models or languages examined.

## 3) Evidence of Internal Romanization

The paper employs mechanistic interpretability techniques:
- **Next-token generation analysis**: "intermediate layers frequently represent target words in Romanized form"
- **Activation patching**: Demonstrates LLMs "encode semantic concepts similarly across native and Romanized scripts"
- **Layer emergence timing**: For translation tasks, "representations emerge earlier in the model's layers" when target language uses Romanized form versus native script

## 4) Causal Inference Implications

The webpage content does not address whether transliteration interventions violate causal exclusion restrictions or discuss methodological concerns about experimental intervention validity. These theoretical implications are not covered in the available abstract or submission details.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "be4f4051-9b3b-45a8-8252-a4d41d26c970",
  "isSidechain": true,
  "promptId": "885fac21-638b-49aa-852f-c24d838cbccc",
  "agentId": "a5388c7e3e9236e88",
  "type": "user",
  "uuid": "bffad3da-393f-4d77-869b-4758fd9bf615",
  "sourceToolAssistantUUID": "be4f4051-9b3b-45a8-8252-a4d41d26c970",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "5c192117-ae74-4acd-8f38-48b668acc23f",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 13 · 2026-05-19T18:10:37.140Z_

<details><summary>↩ Tool result · `toolu_01Ba3YJXWPBkKK4DyA4mArYG`</summary>

```text
# EfficientXLang: Key Findings on Cross-Lingual Reasoning Efficiency

Based on the abstract, the research reveals several important findings about token efficiency across languages:

## Main Discovery

The authors investigated whether English is the most token-efficient language for reasoning in Language Reasoning Models. Their conclusion is striking: "reasoning in non-English languages not only reduces token usage, but also preserves accuracy."

## Key Results

1. **Token Reduction**: Non-English languages demonstrate lower token consumption compared to English while maintaining comparable accuracy levels.

2. **Genuine Reasoning Shifts**: The efficiency gains "persist even after translating the reasoning traces into English, suggesting genuine shifts in reasoning behavior rather than surface-level linguistic effects." This indicates the improvements aren't merely artifacts of translation but reflect actual differences in how models reason across languages.

3. **Model-Dependent Outcomes**: The extent of improvement varies significantly, as the findings depend on "the models multilingual strength." Models with stronger multilingual capabilities showed greater benefits.

## Scope of Study

The research evaluated three open-source models (DeepSeek R1, Qwen 2.5, and Qwen 3) across four mathematical datasets and seven typologically diverse languages, providing robust cross-linguistic evidence for these claims.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "e324bacc-36ea-487e-9d3b-ec62e4094613",
  "isSidechain": true,
  "promptId": "885fac21-638b-49aa-852f-c24d838cbccc",
  "agentId": "a5388c7e3e9236e88",
  "type": "user",
  "uuid": "6f92f414-9c79-463f-8e33-ac30084050ca",
  "sourceToolAssistantUUID": "e324bacc-36ea-487e-9d3b-ec62e4094613",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "5c192117-ae74-4acd-8f38-48b668acc23f",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-19T18:10:39.972Z_

<details><summary>↩ Tool result · `toolu_01DnyfKmfFZkCa3b7be8FEeu`</summary>

```text
Web search results for query: "Beyond Text Compression ACL 2025 tokenizer effects NLP"

Links: [{"title":"Beyond Text Compression: Evaluating Tokenizers Across Scales - ACL Anthology","url":"https://aclanthology.org/2025.acl-long.1546/"},{"title":"Beyond Text Compression: Evaluating Tokenizers Across ...","url":"https://aclanthology.org/2025.acl-long.1546.pdf"},{"title":"Beyond Text Compression: Evaluating Tokenizers Across Scales | AI Research Paper Details","url":"https://www.aimodels.fyi/papers/arxiv/beyond-text-compression-evaluating-tokenizers-across-scales"},{"title":"Beyond Text Compression: Evaluating Tokenizers Across Scales - Apple Machine Learning Research","url":"https://machinelearning.apple.com/research/beyond-text-compression"},{"title":"Beyond Text Compression: Evaluating Tokenizers Across ...","url":"https://arxiv.org/pdf/2506.03101"},{"title":"Unpacking Tokenization: Evaluating Text Compression and its Correlation   with Model Performance","url":"https://arxiv.org/pdf/2403.06265"}]

The search found the paper "Beyond Text Compression: Evaluating Tokenizers Across Scales" from ACL 2025. Here are the key findings:

## Main Research Findings

The study finds that tokenizer choice has negligible effects on tasks in English but results in consistent performance differences in multilingual settings.

The researchers investigated whether evaluating tokenizers on smaller models (350M parameters) reliably predicts their impact at larger scales (2.7B parameters), finding that tokenizer choice minimally affects English tasks but yields significant, scale-consistent differences in machine translation performance.

## New Evaluation Metrics

The paper proposes new intrinsic tokenizer metrics inspired by Zipf's law that correlate more strongly with downstream performance than text compression when modeling unseen languages. Based on these findings, they propose additional intrinsic metrics that correlate more strongly with downstream performance than text compression and combine these metrics into an evaluation framework that enables more reliable intrinsic tokenizer comparisons.

## Broader Context

While text compression has emerged as a common intrinsic metric, recent work questions its reliability as a quality indicator. This work addresses that gap by going "beyond text compression" to develop more robust evaluation approaches for tokenizer design in NLP.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "28863e2e-4762-4497-afd4-d7c74d8e8acf",
  "isSidechain": true,
  "promptId": "885fac21-638b-49aa-852f-c24d838cbccc",
  "agentId": "a5388c7e3e9236e88",
  "type": "user",
  "uuid": "90598de6-f5e5-4ba9-8112-d6c83a66dfa7",
  "sourceToolAssistantUUID": "28863e2e-4762-4497-afd4-d7c74d8e8acf",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "5c192117-ae74-4acd-8f38-48b668acc23f",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 15 · 2026-05-19T18:10:42.239Z_

<details><summary>↩ Tool result · `toolu_01YSYFjWQNFzMAd7PkvUPm1K`</summary>

```text
Web search results for query: "script transliteration intervention causal inference NLP 2025 2026"

Links: [{"title":"Linear Script Representations in Speech Foundation Models Enable Zero-Shot Transliteration","url":"https://arxiv.org/pdf/2601.02906"},{"title":"Causal Inference of Script Knowledge","url":"https://arxiv.org/pdf/2004.01174"},{"title":"Do large language models and humans have similar behaviors in causal   inference with script knowledge?","url":"https://arxiv.org/pdf/2311.07311"},{"title":"Causal Inference with Large Language Model: A Survey Jing Ma","url":"https://www.arxiv.org/pdf/2409.09822v3"},{"title":"Lost in Transliteration: Bridging the Script Gap in Neural IR","url":"https://arxiv.org/pdf/2505.08411"},{"title":"Journal of Machine Learning Research 26 (2025) 1-64","url":"https://www.jmlr.org/papers/volume26/23-0058/23-0058.pdf"},{"title":"Causal Inference and Natural Language Processing","url":"https://www.researchgate.net/publication/375921748_Causal_Inference_and_Natural_Language_Processing"},{"title":"Large Reasoning Models Struggle to Transfer Parametric Knowledge Across Scripts","url":"https://arxiv.org/pdf/2603.17070"},{"title":"Breaking the Script Barrier in Multilingual Pre-Trained Language Models   with Transliteration-Based Post-Training Alignment","url":"https://arxiv.org/pdf/2406.19759"}]

Based on the search results, here are the key findings related to script transliteration, intervention, causal inference, and NLP from 2025-2026:

## Recent Research Highlights

**Script Representations and Interventions:**
Script is represented linearly in multilingual ASR models, enabling post-hoc control over the script of ASR output by way of adding script vectors to the hidden states. This strategy is used to induce script change in speech foundation models by way of steering.

**Causal Inference in NLP:**
A correlation-based approach is insufficient for script induction; instead, an approach based on the causal effect between events, formally defined via interventions, is proposed. Output based on causal effects better matches the intuition of what a script represents.

**Cross-Script Transfer Challenges:**
Numerous works propose different uses of transliteration as test-time solutions for cross-script transfer limitations, with recent works identifying persistent cross-lingual inconsistency, especially in knowledge, noting script's high influence.

**Transliteration in Information Retrieval:**
Recent work addresses "Lost in Transliteration: Bridging the Script Gap in Neural IR" as presented at the 48th International ACM SIGIR Conference in July 2025.

**Multilingual Model Alignment:**
Sequence-level contrastive learning objectives have been proposed to improve alignment across different scripts at large scale using both original script sentences and their Latin transliterations.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "5bda7281-ff64-42dd-bc85-b71a0e24ec9a",
  "isSidechain": true,
  "promptId": "885fac21-638b-49aa-852f-c24d838cbccc",
  "agentId": "a5388c7e3e9236e88",
  "type": "user",
  "uuid": "8d804c63-ee7f-490e-9f03-b7d8b1da9d0b",
  "sourceToolAssistantUUID": "5bda7281-ff64-42dd-bc85-b71a0e24ec9a",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "5c192117-ae74-4acd-8f38-48b668acc23f",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 16 · 2026-05-19T18:10:45.310Z_

Let me fetch the full paper details for RomanLens and "Beyond Text Compression" to get more specific evidence.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8d804c63-ee7f-490e-9f03-b7d8b1da9d0b",
  "isSidechain": true,
  "agentId": "a5388c7e3e9236e88",
  "requestId": "req_011CbCNrYdcUm9jCUvW4eoEY",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "52ce6a96-c1c8-4ae3-a846-c266cc7dabc6",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "5c192117-ae74-4acd-8f38-48b668acc23f",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MmNWzzxGiZVRMxwTs9UMY2",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2424,
      "cache_read_input_tokens": 10239,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2424,
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

_source line 17 · 2026-05-19T18:10:47.664Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01NgBSJfdCDXdZXQZ5xGcpQp`</summary>

```json
{
  "url": "https://aclanthology.org/2025.acl-long.1546/",
  "prompt": "Extract: 1) When are tokenizer effects negligible vs significant? 2) Do they find that tokenizer differences matter for multilingual tasks specifically? 3) What do they say about text compression as a proxy for tokenizer quality? 4) Any findings about how tokenizer choice interacts with language script or non-English performance?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "52ce6a96-c1c8-4ae3-a846-c266cc7dabc6",
  "isSidechain": true,
  "agentId": "a5388c7e3e9236e88",
  "requestId": "req_011CbCNrYdcUm9jCUvW4eoEY",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "3cbd7f49-bdd9-485e-a470-56eda7dcddc5",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "5c192117-ae74-4acd-8f38-48b668acc23f",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MmNWzzxGiZVRMxwTs9UMY2",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2424,
      "cache_read_input_tokens": 10239,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2424,
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

_source line 18 · 2026-05-19T18:10:48.605Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01GvyzCQ4eSf3JkeWFE6ePDu`</summary>

```json
{
  "url": "https://www.aimodels.fyi/papers/arxiv/beyond-text-compression-evaluating-tokenizers-across-scales",
  "prompt": "Extract the main findings: when tokenizer effects are negligible vs significant, what they find about multilingual settings, and whether text compression is a good proxy for downstream performance."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3cbd7f49-bdd9-485e-a470-56eda7dcddc5",
  "isSidechain": true,
  "agentId": "a5388c7e3e9236e88",
  "requestId": "req_011CbCNrYdcUm9jCUvW4eoEY",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "02d843e9-801d-45af-b1ef-c0737ae93243",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "5c192117-ae74-4acd-8f38-48b668acc23f",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MmNWzzxGiZVRMxwTs9UMY2",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2424,
      "cache_read_input_tokens": 10239,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2424,
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

_source line 19 · 2026-05-19T18:10:48.832Z_

<details><summary>↩ Tool result · `toolu_01GvyzCQ4eSf3JkeWFE6ePDu`</summary>

```text
The server returned HTTP 403 Forbidden.

The response body was not retrieved. If this URL requires authentication, use an authenticated tool (e.g. `gh` for GitHub, or an MCP-provided fetch tool) instead of WebFetch.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "02d843e9-801d-45af-b1ef-c0737ae93243",
  "isSidechain": true,
  "promptId": "885fac21-638b-49aa-852f-c24d838cbccc",
  "agentId": "a5388c7e3e9236e88",
  "type": "user",
  "uuid": "31835801-5074-403e-b46e-240ba2ca7c2c",
  "sourceToolAssistantUUID": "02d843e9-801d-45af-b1ef-c0737ae93243",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "5c192117-ae74-4acd-8f38-48b668acc23f",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 20 · 2026-05-19T18:10:50.016Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01HF4z1EVMjYjw6Dbbo6x4n9`</summary>

```json
{
  "url": "https://arxiv.org/abs/2505.08411",
  "prompt": "Extract findings about transliteration in information retrieval. What do they find about script gaps and transliteration as an intervention?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "31835801-5074-403e-b46e-240ba2ca7c2c",
  "isSidechain": true,
  "agentId": "a5388c7e3e9236e88",
  "requestId": "req_011CbCNrYdcUm9jCUvW4eoEY",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "aa056def-4fb1-4a13-9fbe-ad77b6a077b3",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "5c192117-ae74-4acd-8f38-48b668acc23f",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MmNWzzxGiZVRMxwTs9UMY2",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2424,
      "cache_read_input_tokens": 10239,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2424,
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

_source line 21 · 2026-05-19T18:10:50.713Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01JDqYbbggUwtJAuoi65oz73`</summary>

```json
{
  "url": "https://arxiv.org/abs/2603.17070",
  "prompt": "Extract findings about how large reasoning models struggle to transfer parametric knowledge across scripts. What does this say about script as an intervention variable in NLP experiments?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "aa056def-4fb1-4a13-9fbe-ad77b6a077b3",
  "isSidechain": true,
  "agentId": "a5388c7e3e9236e88",
  "requestId": "req_011CbCNrYdcUm9jCUvW4eoEY",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "2d66e4fa-7cee-4898-b1fb-7cba38c5fdf5",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "5c192117-ae74-4acd-8f38-48b668acc23f",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MmNWzzxGiZVRMxwTs9UMY2",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2424,
      "cache_read_input_tokens": 10239,
      "output_tokens": 488,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2424
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 488,
          "cache_read_input_tokens": 10239,
          "cache_creation_input_tokens": 2424,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2424,
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

_source line 22 · 2026-05-19T18:10:52.400Z_

<details><summary>↩ Tool result · `toolu_01NgBSJfdCDXdZXQZ5xGcpQp`</summary>

```text
# Key Findings on Tokenizer Effects

**1) Negligible vs. Significant Effects:**
The research reveals that "tokenizer choice has negligible effects on tasks in English but results in consistent performance differences in multilingual settings." English-centric models show minimal impact from tokenizer selection.

**2) Multilingual Task Significance:**
Yes, the study explicitly demonstrates that tokenizer differences matter substantially for multilingual work. The abstract confirms tokenizers produce "consistent performance differences in multilingual settings," making selection critical for non-English language modeling.

**3) Text Compression as Quality Proxy:**
The authors challenge compression metrics, stating they "propose new intrinsic tokenizer metrics inspired by Zipf's law that correlate more strongly with downstream performance than text compression when modeling unseen languages." This directly critiques compression-based evaluation approaches.

**4) Language Script/Non-English Performance:**
The abstract addresses this broadly through the multilingual focus but doesn't separately detail script-specific interactions. However, the emphasis on "modeling unseen languages" and systematic evaluation of "multilingual tokenizers" suggests they examined diverse linguistic properties beyond English.

**Methodological Note:** The team also demonstrated that smaller models can reliably predict tokenizer impacts on larger models, offering a computationally efficient evaluation pathway.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "3cbd7f49-bdd9-485e-a470-56eda7dcddc5",
  "isSidechain": true,
  "promptId": "885fac21-638b-49aa-852f-c24d838cbccc",
  "agentId": "a5388c7e3e9236e88",
  "type": "user",
  "uuid": "1e3e5feb-b47e-4661-ab40-c5d069dec3b6",
  "sourceToolAssistantUUID": "3cbd7f49-bdd9-485e-a470-56eda7dcddc5",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "5c192117-ae74-4acd-8f38-48b668acc23f",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 23 · 2026-05-19T18:10:55.669Z_

<details><summary>↩ Tool result · `toolu_01JDqYbbggUwtJAuoi65oz73`</summary>

```text
# Script as a Barrier to Cross-Lingual Knowledge Transfer

## Key Findings

The research reveals that **script mismatch is the primary obstacle** to parametric knowledge transfer in large reasoning models, rather than language or linguistic family differences.

The study's core discovery: "script match - not language or family - is the primary predictor of knowledge transfer failure once model capability and question difficulty are accounted for."

## Critical Implications for NLP Experiments

This finding has significant methodological consequences:

1. **Script as an Overlooked Variable**: The research demonstrates that script functions as a critical confounding variable in cross-lingual NLP experiments. Experiments comparing models across languages may misattribute performance differences to language-specific factors when script differences are the actual cause.

2. **Intervention Potential**: The authors show that providing entities in the source language "disproportionately improves cross-script questions," suggesting script effects are addressable through deliberate interventions during training.

3. **Experimental Design Implications**: Researchers designing multilingual NLP studies should explicitly control for or isolate script effects from other linguistic variables to avoid drawing incorrect conclusions about model capabilities.

The work suggests that accounting for script systematically could improve cross-lingual knowledge transfer through targeted post-training approaches.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "2d66e4fa-7cee-4898-b1fb-7cba38c5fdf5",
  "isSidechain": true,
  "promptId": "885fac21-638b-49aa-852f-c24d838cbccc",
  "agentId": "a5388c7e3e9236e88",
  "type": "user",
  "uuid": "61edbe93-46bc-48a3-a484-a74cc5fca1a9",
  "sourceToolAssistantUUID": "2d66e4fa-7cee-4898-b1fb-7cba38c5fdf5",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "5c192117-ae74-4acd-8f38-48b668acc23f",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 24 · 2026-05-19T18:10:57.357Z_

<details><summary>↩ Tool result · `toolu_01HF4z1EVMjYjw6Dbbo6x4n9`</summary>

```text
# Findings on Transliteration in Information Retrieval

## The Script Gap Problem

The researchers identify a significant performance issue: "current search systems, including those that use multilingual dense embeddings such as BGE-M3, do not generalise to this setting" when users employ transliterated queries. Users from non-Latin script languages often type in Latinized forms (like Greeklish or Arabizi) for typing convenience, but existing IR systems struggle with this cross-script matching.

## Transliteration as an Intervention

The team explored adapting the "translate-train" approach to transliteration challenges. Their key finding: "by further fine-tuning IR models on an even mixture of native and Latinized text, they can perform this cross-script matching at nearly the same performance as when the query was formulated in the native script."

## Important Limitation

The abstract notes a nuance: transliterations can cause queries to lose certain semantic nuances, suggesting the solution, while effective for matching, isn't without trade-offs. This indicates that bridging the script gap through mixed-script training improves retrieval performance but may sacrifice some query meaning precision.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "aa056def-4fb1-4a13-9fbe-ad77b6a077b3",
  "isSidechain": true,
  "promptId": "885fac21-638b-49aa-852f-c24d838cbccc",
  "agentId": "a5388c7e3e9236e88",
  "type": "user",
  "uuid": "527f4060-6480-4648-adfd-c19ed4c62d73",
  "sourceToolAssistantUUID": "aa056def-4fb1-4a13-9fbe-ad77b6a077b3",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "5c192117-ae74-4acd-8f38-48b668acc23f",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 25 · 2026-05-19T18:11:20.400Z_

Here is my report:

---

**RomanLens (ACL 2025 Findings, arXiv:2502.07424): What It Actually Shows**

RomanLens finds that LLMs perform "latent romanization" -- in intermediate layers, models represent non-Roman-script words in romanized form before converting to native script in later layers. Evidence comes from three methods: (1) next-token generation analysis showing intermediate layers frequently produce romanized forms of target words, (2) activation patching demonstrating that semantic concepts are encoded similarly across native and romanized scripts, and (3) layer emergence timing showing representations emerge earlier when the target is already romanized. They study languages with non-Roman scripts using mechanistic interpretability techniques.

**How This Complicates the Transliteration Intervention**

This is a real problem for using transliteration as a "clean" experimental manipulation. If the model already internally romanizes non-Roman text, then feeding it pre-romanized input does not introduce script change as an exogenous shock -- you are partially replicating what the model does internally. In causal inference terms, the concern is that transliteration does not satisfy the exclusion restriction cleanly: it changes both the surface tokenization AND aligns with the model's internal representational pathway, making it hard to attribute effects purely to tokenization differences. The intervention is not orthogonal to the model's processing.

**Can Transliteration Still Be Used?**

Yes, but with explicit caveats. The honest framing: transliteration is a *bundle intervention* that simultaneously (a) changes tokenization/fertility, (b) aligns input with the model's latent representational space, and (c) potentially loses script-specific semantic nuances (per the "Lost in Transliteration" SIGIR 2025 finding). This is not fatal -- many useful experiments use bundle interventions -- but you must acknowledge you cannot isolate the tokenization channel from the latent-romanization channel. A complementary approach: compare romanization effects across models with different degrees of latent romanization, or use non-Latin-to-non-Latin script changes (e.g., Cyrillic to Devanagari) where neither script is the model's latent bridge.

**Beyond Text Compression (ACL 2025, Apple)**

Key finding: tokenizer choice has **negligible effects on English tasks** but produces **consistent, significant performance differences in multilingual settings**. Text compression alone is a poor proxy for downstream performance; Zipf's-law-inspired metrics correlate better. This directly supports the proposal's premise that tokenization matters more for non-English languages and justifies studying tokenizer effects in multilingual contexts.

**EfficientXLang (arXiv:2507.00246)**

Striking finding: reasoning in non-English languages **reduces token usage while preserving accuracy** on math tasks (tested on DeepSeek R1, Qwen 2.5, Qwen 3 across 7 languages, 4 math datasets). The efficiency gains persist after translating reasoning traces back to English, indicating genuine reasoning behavior shifts, not surface artifacts. Gains depend on the model's multilingual strength.

**Additional: Script Transfer (arXiv:2603.17070)**

Script match -- not language family -- is the primary predictor of knowledge transfer failure in reasoning models. This reinforces that script is a potent variable but also a confound: transliteration changes script, which independently affects transfer, making it harder to isolate tokenization effects.

**Recommended Framing**

State explicitly that transliteration is a bundle intervention affecting tokenization, script alignment with latent representations, and cross-script transfer simultaneously. Use it as a strong-but-imperfect instrument, triangulated with other approaches (vocabulary overlap analysis, controlled fertility comparisons within the same script, cross-model comparisons exploiting variation in latent romanization strength).

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "527f4060-6480-4648-adfd-c19ed4c62d73",
  "isSidechain": true,
  "agentId": "a5388c7e3e9236e88",
  "requestId": "req_011CbCNsfGVraXBQW9ppgmg6",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "5daa95c9-46cb-45b9-9fc1-178ff601a154",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "5c192117-ae74-4acd-8f38-48b668acc23f",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AmudawKvhDbs6z7mDxFRA4",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 306,
      "cache_creation_input_tokens": 1151,
      "cache_read_input_tokens": 12663,
      "output_tokens": 869,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1151
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 306,
          "output_tokens": 869,
          "cache_read_input_tokens": 12663,
          "cache_creation_input_tokens": 1151,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1151,
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
