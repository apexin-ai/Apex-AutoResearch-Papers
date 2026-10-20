# Research conversation: You are analyzing the paper "RAGDefender: Rescuing the Unpoisoned — Efficient Defense against Knowledge Corruption Attac

**The Likert Blindspot: Measurement-Mode Divergence in LLM Judge Style Evaluation (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 14
- **Recorded user turns:** 1
- **Tool calls:** 4
- **Original source:** `logs/chats/exported-trajectories/account-2/agent-aff71ea6e5b38efa3.jsonl`
- **Structured JSON:** [`0b3313ebc7a1b89ad965.json`](../../sessions/0b/0b3313ebc7a1b89ad965.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

14 recorded events

### User

_source line 1 · 2026-05-30T06:25:25.865Z_

You are analyzing the paper "RAGDefender: Rescuing the Unpoisoned — Efficient Defense against Knowledge Corruption Attacks on RAG Systems" by Minseok Kim, Hankook Lee, Hyungjoon Koo (ACSAC 2025). URL: https://arxiv.org/abs/2511.01268

Your task:
1. Use WebFetch to read the paper's abstract, introduction, and method from the arxiv page
2. Use WebSearch to find any additional details about the method, comparisons with RobustRAG, performance numbers
3. Focus on: What gap did they identify? What was the key insight? How did they formulate the problem? What techniques did they adapt/combine?

Provide a detailed but concise summary covering:
- Problem identification (what gap, how found)
- Key insight (core intellectual contribution)
- Innovation type
- Method summary (technical approach for identifying and removing poisoned passages)
- Key performance numbers (especially ASR reduction, comparison with RobustRAG)
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
  "agentId": "aff71ea6e5b38efa3",
  "type": "user",
  "uuid": "1eb2b376-9efa-4a25-b436-9281ac14056a",
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

_source line 2 · 2026-05-30T06:25:25.868Z_

```json
{
  "parentUuid": "1eb2b376-9efa-4a25-b436-9281ac14056a",
  "isSidechain": true,
  "agentId": "aff71ea6e5b38efa3",
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
  "uuid": "aa30d200-a936-46f4-8dc0-82970a27fe42",
  "timestamp": "2026-05-30T06:25:25.868Z",
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

_source line 3 · 2026-05-30T06:25:25.869Z_

```json
{
  "parentUuid": "aa30d200-a936-46f4-8dc0-82970a27fe42",
  "isSidechain": true,
  "agentId": "aff71ea6e5b38efa3",
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "a17e88d0-ea1f-44c9-989f-f7f731ec399e",
  "timestamp": "2026-05-30T06:25:25.869Z",
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

_source line 4 · 2026-05-30T06:25:28.042Z_



I'll fetch the paper and search for additional details about RAGDefender.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a17e88d0-ea1f-44c9-989f-f7f731ec399e",
  "isSidechain": true,
  "agentId": "aff71ea6e5b38efa3",
  "requestId": "req_011CbYGyJCWrdh1NvawLfmjK",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "ecfe24ed-deec-4bab-a318-b507e31c50e7",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "92f38cdd-b3e1-453a-8457-65dd6c27cbfd",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016bh8AKZo3nWDXxP2HAjh4A",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1628,
      "cache_read_input_tokens": 7413,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1628,
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

_source line 5 · 2026-05-30T06:25:28.354Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01Xzrrpdifpy3Eo3CCK6rLuC`</summary>

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
  "parentUuid": "ecfe24ed-deec-4bab-a318-b507e31c50e7",
  "isSidechain": true,
  "agentId": "aff71ea6e5b38efa3",
  "requestId": "req_011CbYGyJCWrdh1NvawLfmjK",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "5cc75f42-8d22-4369-9075-386a2addbd88",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "92f38cdd-b3e1-453a-8457-65dd6c27cbfd",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016bh8AKZo3nWDXxP2HAjh4A",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1628,
      "cache_read_input_tokens": 7413,
      "output_tokens": 97,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1628
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 97,
          "cache_read_input_tokens": 7413,
          "cache_creation_input_tokens": 1628,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1628,
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

_source line 6 · 2026-05-30T06:25:28.376Z_

<details><summary>↩ Tool result · `toolu_01Xzrrpdifpy3Eo3CCK6rLuC`</summary>

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
  "parentUuid": "5cc75f42-8d22-4369-9075-386a2addbd88",
  "isSidechain": true,
  "promptId": "bfbb75dd-55f4-4449-8327-dd488e005f06",
  "agentId": "aff71ea6e5b38efa3",
  "type": "user",
  "uuid": "3798aafa-eed4-4382-ae98-364057e1b7f7",
  "sourceToolAssistantUUID": "5cc75f42-8d22-4369-9075-386a2addbd88",
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

_source line 7 · 2026-05-30T06:25:30.665Z_



Now let me fetch the paper and search for additional information in parallel.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3798aafa-eed4-4382-ae98-364057e1b7f7",
  "isSidechain": true,
  "agentId": "aff71ea6e5b38efa3",
  "requestId": "req_011CbYGyV6rdbDSzxFmm32HV",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "57043fe5-8eec-43c8-af6f-32cadae6b3f5",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "92f38cdd-b3e1-453a-8457-65dd6c27cbfd",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014EHwjsGH7xkKUFC31QaKBF",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1119,
      "cache_read_input_tokens": 9041,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1119,
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

_source line 8 · 2026-05-30T06:25:34.005Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01QSxeNZhesax6q1HsaCKwCD`</summary>

```json
{
  "url": "https://arxiv.org/abs/2511.01268",
  "prompt": "Extract the full abstract, introduction details, and method description of this paper. Include: the problem they identify, the gap in existing work, their key insight, the technical approach (how they detect and remove poisoned passages), the formulation of the problem, any techniques they adapt or combine, and key performance numbers (ASR reduction, comparison with RobustRAG, clean accuracy). Be as detailed as possible."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "57043fe5-8eec-43c8-af6f-32cadae6b3f5",
  "isSidechain": true,
  "agentId": "aff71ea6e5b38efa3",
  "requestId": "req_011CbYGyV6rdbDSzxFmm32HV",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "38f2596c-3a26-45fe-bbd8-0cdd1e33746e",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "92f38cdd-b3e1-453a-8457-65dd6c27cbfd",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014EHwjsGH7xkKUFC31QaKBF",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1119,
      "cache_read_input_tokens": 9041,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1119,
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

_source line 9 · 2026-05-30T06:25:37.745Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01AD3PUeNHNgUQ7FjpvLtU6V`</summary>

```json
{
  "url": "https://arxiv.org/html/2511.01268",
  "prompt": "Extract the detailed method section, experimental results, and comparison tables from this paper. Focus on: 1) How RAGDefender identifies poisoned passages (the scoring mechanism, optimization formulation), 2) How it removes/handles them, 3) Performance numbers: ASR (attack success rate) reduction vs baselines especially RobustRAG, 4) Clean accuracy preservation, 5) Computational efficiency comparisons, 6) Any ablation studies, 7) Limitations discussed by the authors. Be very detailed about the technical approach."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "38f2596c-3a26-45fe-bbd8-0cdd1e33746e",
  "isSidechain": true,
  "agentId": "aff71ea6e5b38efa3",
  "requestId": "req_011CbYGyV6rdbDSzxFmm32HV",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "fa00ba79-c7a8-4f76-88d8-4cd3dc956fd4",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "92f38cdd-b3e1-453a-8457-65dd6c27cbfd",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014EHwjsGH7xkKUFC31QaKBF",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1119,
      "cache_read_input_tokens": 9041,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1119,
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

_source line 10 · 2026-05-30T06:25:38.475Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01GT2p2Adx3g7i8krEVEysic`</summary>

```json
{
  "query": "RAGDefender \"knowledge corruption attacks\" RAG defense RobustRAG comparison ACSAC 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "fa00ba79-c7a8-4f76-88d8-4cd3dc956fd4",
  "isSidechain": true,
  "agentId": "aff71ea6e5b38efa3",
  "requestId": "req_011CbYGyV6rdbDSzxFmm32HV",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "9b485f4b-a592-473a-b509-1f42b113dc54",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "92f38cdd-b3e1-453a-8457-65dd6c27cbfd",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014EHwjsGH7xkKUFC31QaKBF",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1119,
      "cache_read_input_tokens": 9041,
      "output_tokens": 421,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1119
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 421,
          "cache_read_input_tokens": 9041,
          "cache_creation_input_tokens": 1119,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1119,
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

_source line 11 · 2026-05-30T06:25:39.829Z_

<details><summary>↩ Tool result · `toolu_01QSxeNZhesax6q1HsaCKwCD`</summary>

```text
# RAGDefender: Defense Against Knowledge Corruption in RAG Systems

## Problem Identification

The paper addresses vulnerabilities in Retrieval-Augmented Generation (RAG) systems. While RAG improves LLM reliability by grounding responses in external knowledge, these systems remain susceptible to "knowledge corruption attacks by injecting misleading information" into knowledge bases.

## Gap in Existing Work

Current defense approaches suffer from computational inefficiency. Existing strategies include:
- Having LLMs individually inspect retrieved passages
- Fine-tuning robust retrievers

The authors note these methods are "effective" but "often come with substantial computational costs."

## Key Innovation

RAGDefender introduces a "resource-efficient defense mechanism" that operates post-retrieval without requiring model training or inference. The system uses "lightweight machine learning techniques to detect and filter out adversarial content."

## Technical Approach

The method leverages a post-retrieval filtering phase—meaning it processes passages after the retriever identifies them but before the generator formulates responses. Rather than retraining components, it applies lightweight ML models to distinguish poisoned from legitimate passages.

## Performance Results

The defense dramatically outperforms competitors:
- Reduces attack success rate (ASR) against Gemini from 0.89 to 0.02 when adversarial passages outnumber legitimate ones 4:1
- RobustRAG achieved 0.69 ASR under identical conditions
- Discern-and-Answer achieved 0.24 ASR

The paper appears in ACSAC 2025 proceedings and contains 15 pages with 7 figures and 10 tables.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "38f2596c-3a26-45fe-bbd8-0cdd1e33746e",
  "isSidechain": true,
  "promptId": "bfbb75dd-55f4-4449-8327-dd488e005f06",
  "agentId": "aff71ea6e5b38efa3",
  "type": "user",
  "uuid": "28db24eb-c697-434e-9381-5a701cad60e8",
  "sourceToolAssistantUUID": "38f2596c-3a26-45fe-bbd8-0cdd1e33746e",
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

_source line 12 · 2026-05-30T06:25:45.120Z_

<details><summary>↩ Tool result · `toolu_01GT2p2Adx3g7i8krEVEysic`</summary>

```text
Web search results for query: "RAGDefender "knowledge corruption attacks" RAG defense RobustRAG comparison ACSAC 2025"

Links: [{"title":"Rescuing the Unpoisoned: Efficient Defense against Knowledge Corruption Attacks","url":"https://kevinkoo001.github.io/assets/pdf/acsac25-ragdefender.pdf"},{"title":"Rescuing the Unpoisoned: Efficient Defense against Knowledge Corruption Attacks on RAG Systems","url":"https://arxiv.org/html/2511.01268v1"},{"title":"[2511.01268v1] Rescuing the Unpoisoned: Efficient Defense against Knowledge Corruption Attacks on RAG Systems","url":"https://arxiv.org/abs/2511.01268v1"},{"title":"[2511.01268] Rescuing the Unpoisoned: Efficient Defense against Knowledge Corruption Attacks on RAG Systems","url":"https://arxiv.org/abs/2511.01268"},{"title":"Rescuing the Unpoisoned: Efficient Defense against Knowledge Corruption Attacks on RAG Systems","url":"https://arxiv.org/pdf/2511.01268"},{"title":"GitHub - SecAI-Lab/RAGDefender: Artifacts for paper \"Rescuing the Unpoisoned: Efficient Defense against Knowledge Corruption Attacks on RAG Systems\" · GitHub","url":"https://github.com/SecAI-Lab/RAGDefender"},{"title":"Certifiably Robust RAG against Retrieval Corruption","url":"https://arxiv.org/html/2405.15556v2"},{"title":"Paper page - Rescuing the Unpoisoned: Efficient Defense against Knowledge Corruption Attacks on RAG Systems","url":"https://huggingface.co/papers/2511.01268"}]

Based on the web search results, here's what I found about RAGDefender and its comparison with RobustRAG:

## Overview

RAGDefender is a resource-efficient defense mechanism against knowledge corruption (i.e., by data poisoning) attacks in practical RAG deployments. RAGDefender operates during the post-retrieval phase, leveraging lightweight machine learning techniques to detect and filter out adversarial content without requiring additional model training or inference.

## Comparison with RobustRAG

RAGDefender defeats RobustRAG with high margins in every setting. More specifically, RAGDefender reduces the attack success rate (ASR) against the Gemini model from 0.89 to as low as 0.02, compared to 0.69 for RobustRAG and 0.24 for Discern-and-Answer when adversarial passages outnumber legitimate ones by a factor of four (4x).

## Defense Approaches

The paper contrasts RAGDefender with existing defense methods: RobustRAG tackles data poisoning by requiring LLMs to inspect each retrieved passage individually before generating responses. Discern-and-Answer attempts to identify conflicting information among retrieved documents by fine-tuning a discriminator or prompting the LLM to identify inconsistencies. While both approaches enhance robustness and reliability, they suffer from additional computational overhead, such as multiple LLM inferences or substantial memory consumption.

## Publication

The paper "Rescuing the Unpoisoned: Efficient Defense against Knowledge Corruption Attacks on RAG Systems" was presented at the Annual Computer Security Applications Conference (ACSAC) in 2025.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "9b485f4b-a592-473a-b509-1f42b113dc54",
  "isSidechain": true,
  "promptId": "bfbb75dd-55f4-4449-8327-dd488e005f06",
  "agentId": "aff71ea6e5b38efa3",
  "type": "user",
  "uuid": "b1045f44-420a-483e-ae56-4192b34b928d",
  "sourceToolAssistantUUID": "9b485f4b-a592-473a-b509-1f42b113dc54",
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

_source line 13 · 2026-05-30T06:26:01.623Z_

<details><summary>↩ Tool result · `toolu_01AD3PUeNHNgUQ7FjpvLtU6V`</summary>

```text
# RAGDefender: Detailed Technical Analysis

## Method Overview

RAGDefender operates through a **two-stage pipeline** to identify and filter adversarial passages:

**Stage 1 - Passage Grouping:** Estimates the number of adversarial passages (N_adv) using either clustering-based or concentration-based strategies depending on question type.

**Stage 2 - Adversarial Identification:** Ranks individual passages and selects the top N_adv as adversarial for removal.

## Technical Approach

### Stage 1: Grouping Retrieved Passages

**Clustering-Based Grouping** (single-hop QA):
- Uses hierarchical agglomerative clustering on passage embeddings
- Incorporates TF-IDF term analysis to identify frequently co-occurring keywords
- Computes N_TF-IDF as the count of passages containing >50% of the top-m most important terms
- Estimates adversarial count via: "if N_TF-IDF ≤ |R|/2, then N_adv = n_min; otherwise |R| - n_min" where n_min is the smaller cluster size

**Concentration-Based Grouping** (multi-hop QA):
- Calculates two concentration factors per passage: mean and median similarity to all other passages
- A passage counts as potentially adversarial if both its mean and median similarity exceed their respective global values
- Formula: N_adv = Σ I(s_i^mean > s̄) · I(s_i^median > s̃)

### Stage 2: Identifying Adversarial Passages

The scoring mechanism ranks passages based on **semantic clustering behavior**:

1. **Pair Identification:** Finds top N_pairs = max(1, C(N_adv,2)) most similar passage pairs using cosine similarity

2. **Frequency Scoring:** For each passage r_i, computes frequency score:
   "f_i = Σ sgn(sim(r_i, r_j)) · |sim(r_i, r_j)^p|" across all pairs in the top set, where p=2 (empirically optimized)

3. **Selection:** Ranks passages by f_i and selects top N_adv as adversarial

4. **Removal:** Safe passages R_safe = R̃ \ R_adv are passed to the generator

## Experimental Results

### Attack Success Rate (ASR) Reduction

**Natural Questions (NQ) Dataset at 4× perturbation ratio:**
- RAGDefender: 0.02-0.03 ASR
- RobustRAG: 0.54-0.84 ASR  
- Discern-and-Answer: 0.24-0.31 ASR

**MS MARCO Dataset:**
- RAGDefender achieved lowest ASR of 0.04 across three retrievers (Contriever, DPR, ANCE)

**HotpotQA Multi-hop (6× ratio, SELF-RAG):**
- Reduced ASR from 0.73 to 0.05 (68% improvement)
- Accuracy increased from 0.07 to 0.45

### Computational Efficiency

**Speed Improvements:**
- 12.36× faster than RobustRAG (0.774 sec vs 9.552 sec average)
- 1.53× faster than Discern-and-Answer
- Negligible computational cost: <$0.01 per iteration across all models

**Memory Footprint:**
- RAGDefender: Zero GPU memory usage
- RobustRAG: 14,732-33,634 MB depending on model size
- Discern-and-Answer: 41,836 MB fine-tuning + 4,742 MB inference

**Cost Comparison (per iteration):**
- RAGDefender: ~$0.00
- RobustRAG: $1.22-$59.00 depending on generator
- Discern-and-Answer: $4.73 training + $0.48 inference

### Clean Accuracy Preservation

Authors reported: "On NQ, Gemini shows only a 2% drop in accuracy, while other language models exhibit no measurable change" when RAGDefender is applied without attacks.

### Adaptability Results

**Across 3 RAG Architectures:**
- BlendedRAG: ASR reduced from 0.90 to 0.62 average
- REPLUG: ASR reduced from 0.74 to 0.19 average  
- SELF-RAG: ASR reduced from 0.64 to 0.13 average

**Across 6 Language Models (GPT-4o, Gemini, LLaMA-7/13B, Vicuna-7/13B):**
- Consistently maintains low ASR across all generators
- Performance remains stable regardless of model size or type

## Ablation Studies

### Clustering Algorithm Comparison (4× ratio, NQ)

| Algorithm | ASR (avg) |
|-----------|-----------|
| Agglomerative | 0.06 |
| K-Means | 0.16 |
| DBSCAN | 0.44 |

Agglomerative clustering significantly outperformed alternatives by handling non-spherical cluster shapes.

### Hyperparameter Sensitivity (6× ratio, NQ)

**Weighting Exponent p:**
- p=1: 0.06 ASR average
- p=2: 0.05 ASR average (optimal)
- p=3: 0.07 ASR average

**TF-IDF Terms m:**
- m=3: 0.07 ASR average
- m=5: 0.05 ASR average (optimal)
- m=7: 0.08 ASR average

### Two-Stage Effectiveness (6× ratio, NQ)

| Approach | LLaMA-7B | LLaMA-13B | Gemini | GPT-4o | Average |
|----------|----------|-----------|--------|--------|---------|
| Stage 1 Only | 0.35 | 0.35 | 0.36 | 0.25 | 0.34 |
| Stage 2 Only | 0.59 | 0.52 | 0.51 | 0.36 | 0.52 |
| Combined | 0.05 | 0.07 | 0.02 | 0.03 | 0.05 |

Combined approach substantially outperformed single-stage methods, confirming design necessity.

## Robustness Evaluation

### Adaptive Evasion Attacks

**Minimizing Adversarial Similarity:**
- RAGDefender ASR: 0.15 (2× ratio)
- RobustRAG: 0.76
- Discern-and-Answer: 0.42

**Synonym Substitution:** RAGDefender 0.12 vs RobustRAG 0.73

**Paraphrasing:** RAGDefender 0.08 vs RobustRAG 0.79

**Mixed Strategies:** RAGDefender 0.13 vs RobustRAG 0.80

### Multi-clustering Content Injection

With 10× adversarial-to-benign ratio on NQ: RAGDefender achieved 0.18 ASR vs 0.99 for undefended systems.

### Integrity Violation Attacks (Phantom Framework, 2× ratio)

- Denial-of-Service style attacks: 0.03 ASR
- Biased opinion generation: 0.05 ASR

## Author-Identified Limitations

1. **Unknown Corpus Applicability:** "Effectiveness on other types of corpora, including multimodal or multilingual datasets, remains underexplored"

2. **Retrieval Set Size:** "Performance may be inconsistent depending on the number of retrieved passages (e.g., k>10); however, this regime lies outside the typical optimal range (k around 3-5)"

3. **Theoretical Guarantees:** "Absence of formal theoretical guarantees that adversarial passages consistently form dense clusters"

4. **Adversarial Passage Detection Rate:** On NQ at 4× ratio, achieved 0.94 detection rate with estimated N_adv of 21.4 (actual: 20)

5. **Mis-partitioning Rate:** On NQ at 1× ratio, only 0.54% of legitimate passages were incorrectly classified as adversarial

6. **Golden Passage Preservation:** Correctly identified golden passages among legitimate ones with 97% accuracy on NQ
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "fa00ba79-c7a8-4f76-88d8-4cd3dc956fd4",
  "isSidechain": true,
  "promptId": "bfbb75dd-55f4-4449-8327-dd488e005f06",
  "agentId": "aff71ea6e5b38efa3",
  "type": "user",
  "uuid": "e33a380c-2818-4b53-90ef-0354ffd045c2",
  "sourceToolAssistantUUID": "fa00ba79-c7a8-4f76-88d8-4cd3dc956fd4",
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

_source line 14 · 2026-05-30T06:26:45.136Z_

Here is the detailed analysis of RAGDefender.

---

## RAGDefender: Analysis Summary

### Problem Identification

RAG systems ground LLM responses in retrieved external knowledge, but attackers can poison the knowledge base by injecting adversarial passages that cause the model to produce incorrect answers. Existing defenses -- RobustRAG (which has the LLM individually inspect each passage) and Discern-and-Answer (which fine-tunes a discriminator) -- are effective but computationally expensive. RobustRAG requires multiple LLM inference passes (14,732-33,634 MB GPU memory), and Discern-and-Answer requires fine-tuning (41,836 MB). The gap: **no efficient, training-free, model-agnostic defense existed** that could operate in the post-retrieval phase without LLM involvement.

### Key Insight (Core Intellectual Contribution)

Adversarial passages in knowledge corruption attacks tend to be **semantically similar to each other** because they are crafted to push the model toward the same incorrect answer. This creates detectable dense clusters in the embedding space. RAGDefender exploits this clustering signal using only lightweight ML techniques (embeddings, cosine similarity, hierarchical clustering, TF-IDF) -- no LLM inference needed for the defense itself.

### Innovation Type

**Efficiency-driven architectural innovation.** The core detection idea (poisoned passages cluster together) is a relatively natural observation; the contribution is operationalizing it into a two-stage pipeline that is 12x faster, costs effectively $0.00 per query (vs. $1.22-$59.00 for RobustRAG), uses zero GPU memory, and still substantially outperforms existing methods.

### Method Summary

**Stage 1 -- Estimate the number of adversarial passages (N_adv):**

- *Single-hop QA (clustering-based):* Uses hierarchical agglomerative clustering on passage embeddings plus TF-IDF term co-occurrence analysis. If passages sharing >50% of the top-m important terms number at most half the retrieval set, N_adv is set to the smaller cluster size; otherwise N_adv = |R| - n_min.
- *Multi-hop QA (concentration-based):* Computes mean and median cosine similarity of each passage to all others. A passage is flagged if both its mean and median exceed the global averages. N_adv = count of flagged passages.

**Stage 2 -- Identify and remove specific adversarial passages:**

1. Compute top N_pairs = max(1, C(N_adv, 2)) most similar passage pairs by cosine similarity.
2. Score each passage by frequency of appearance in these high-similarity pairs, weighted by similarity raised to power p (p=2 optimal): f_i = sum of sgn(sim) * |sim|^p.
3. Rank by f_i, select top N_adv as adversarial, pass remaining safe passages to the generator.

### Key Performance Numbers

| Setting | RAGDefender | RobustRAG | Discern-and-Answer | No Defense |
|---|---|---|---|---|
| NQ, 4x poison ratio, Gemini | **0.02 ASR** | 0.69 | 0.24 | 0.89 |
| NQ, 4x ratio, average across models | **0.02-0.03** | 0.54-0.84 | 0.24-0.31 | -- |
| MS MARCO, 3 retrievers | **0.04** | -- | -- | -- |
| HotpotQA, 6x ratio, SELF-RAG | **0.05** | -- | -- | 0.73 |

**Efficiency:** 12.36x faster than RobustRAG (0.774s vs 9.552s). Zero GPU memory. Cost ~$0.00 vs $1.22-$59.00 per iteration.

**Clean accuracy:** Only 2% drop on NQ with Gemini; no measurable change on other models.

**Adaptive attacks:** Under synonym substitution (0.12 vs 0.73), paraphrasing (0.08 vs 0.79), and mixed strategies (0.13 vs 0.80), RAGDefender maintains superiority over RobustRAG.

**Ablation:** Both stages are necessary -- Stage 1 alone: 0.34 ASR; Stage 2 alone: 0.52 ASR; combined: 0.05 ASR.

### Limitations and Open Questions

1. **No formal guarantees** that adversarial passages always form dense clusters -- the method is empirically validated but lacks theoretical certification.
2. **Untested on multimodal/multilingual corpora.**
3. **Retrieval set size sensitivity:** Performance may degrade for k > 10 (outside the typical k=3-5 range).
4. **Sophisticated adaptive attacks** that deliberately diversify adversarial passage embeddings (anti-clustering) could potentially evade detection, though the paper's adaptive attack experiments show resilience with ASR around 0.13-0.18.
5. **No coverage guarantee** -- unlike conformal prediction approaches, RAGDefender cannot provide probabilistic bounds on false negative rates.

### Building Blocks (Reusable Components)

- Hierarchical agglomerative clustering for passage grouping
- TF-IDF co-occurrence analysis for estimating adversarial set size
- Pairwise cosine similarity frequency scoring for ranking suspiciousness
- The PoisonedRAG attack framework and evaluation protocol (NQ, MS MARCO, HotpotQA datasets with Contriever, DPR, ANCE retrievers)
- Open-source artifacts at [github.com/SecAI-Lab/RAGDefender](https://github.com/SecAI-Lab/RAGDefender)

### Relevance to Conformal Prediction for RAG Under Adversarial Poisoning

RAGDefender and conformal prediction (CP) approaches address complementary aspects of the same threat. RAGDefender is a **point-estimate filter** -- it makes a binary keep/remove decision per passage with no uncertainty quantification or coverage guarantee. CP-based approaches could provide **calibrated confidence sets** with provable coverage under distributional assumptions, which RAGDefender explicitly lacks (the authors acknowledge "absence of formal theoretical guarantees"). A natural synthesis would be: use RAGDefender's clustering signal as a nonconformity score within a CP framework, obtaining both efficient filtering and statistical coverage guarantees. The key tension is that adversarial poisoning violates exchangeability, which is exactly the gap that robust/adversarial conformal prediction methods aim to address. RAGDefender's empirical finding that poisoned passages cluster densely could inform the design of nonconformity measures specifically tailored to retrieval-augmented settings.

---

Sources:
- [RAGDefender arXiv abstract](https://arxiv.org/abs/2511.01268)
- [RAGDefender full HTML paper](https://arxiv.org/html/2511.01268v1)
- [RAGDefender GitHub repository](https://github.com/SecAI-Lab/RAGDefender)
- [RobustRAG paper](https://arxiv.org/html/2405.15556v2)
- [RAGDefender PDF (author site)](https://kevinkoo001.github.io/assets/pdf/acsac25-ragdefender.pdf)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e33a380c-2818-4b53-90ef-0354ffd045c2",
  "isSidechain": true,
  "agentId": "aff71ea6e5b38efa3",
  "requestId": "req_011CbYH1w2df4RfD4armcWYc",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "686f3c7f-9cfc-46d3-9c0f-fa2c5dc42516",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "92f38cdd-b3e1-453a-8457-65dd6c27cbfd",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01J5nAB3BWy3Y1prbYuAmxR3",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 854,
      "cache_creation_input_tokens": 2910,
      "cache_read_input_tokens": 10160,
      "output_tokens": 1762,
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
          "input_tokens": 854,
          "output_tokens": 1762,
          "cache_read_input_tokens": 10160,
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
