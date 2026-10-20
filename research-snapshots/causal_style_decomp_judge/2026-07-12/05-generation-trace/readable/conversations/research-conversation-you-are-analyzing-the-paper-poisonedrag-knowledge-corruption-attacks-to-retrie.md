# Research conversation: You are analyzing the paper "PoisonedRAG: Knowledge Corruption Attacks to Retrieval-Augmented Generation of Large Langua

**The Likert Blindspot: Measurement-Mode Divergence in LLM Judge Style Evaluation (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 21
- **Recorded user turns:** 1
- **Tool calls:** 7
- **Original source:** `logs/chats/exported-trajectories/account-2/agent-a5a3b96bb3139e08f.jsonl`
- **Structured JSON:** [`ffffddf4f300fb5ab6b0.json`](../../sessions/ff/ffffddf4f300fb5ab6b0.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

21 recorded events

### User

_source line 1 · 2026-05-30T06:25:05.269Z_

You are analyzing the paper "PoisonedRAG: Knowledge Corruption Attacks to Retrieval-Augmented Generation of Large Language Models" by Wei Zou, Runpeng Geng, Binghui Wang, Jinyuan Jia (USENIX Security 2025). URL: https://arxiv.org/abs/2402.07867

Your task:
1. Use WebFetch to read the paper's abstract and introduction from the arxiv page
2. Use WebSearch to find any additional details about the method, reviewer comments, or discussions
3. Focus on: What gap did they identify? What was the key insight? How did they formulate the problem? What techniques did they adapt/combine?

Provide a detailed but concise summary covering:
- Problem identification (what gap, how found)
- Key insight (core intellectual contribution)
- Innovation type
- Method summary (technical approach)
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
  "agentId": "a5a3b96bb3139e08f",
  "type": "user",
  "uuid": "98038e0c-9f63-41cb-ab74-0b8e6aaacc8a",
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

_source line 2 · 2026-05-30T06:25:05.274Z_

```json
{
  "parentUuid": "98038e0c-9f63-41cb-ab74-0b8e6aaacc8a",
  "isSidechain": true,
  "agentId": "a5a3b96bb3139e08f",
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
  "uuid": "6c1f9770-1813-4b19-9a4d-54ac06b3ed8e",
  "timestamp": "2026-05-30T06:25:05.274Z",
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

_source line 3 · 2026-05-30T06:25:05.276Z_

```json
{
  "parentUuid": "6c1f9770-1813-4b19-9a4d-54ac06b3ed8e",
  "isSidechain": true,
  "agentId": "a5a3b96bb3139e08f",
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "2600a760-3191-449a-a0b0-293f6fc1622c",
  "timestamp": "2026-05-30T06:25:05.276Z",
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

_source line 4 · 2026-05-30T06:25:11.204Z_



I'll fetch the paper and search for additional context about it.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2600a760-3191-449a-a0b0-293f6fc1622c",
  "isSidechain": true,
  "agentId": "a5a3b96bb3139e08f",
  "requestId": "req_011CbYGwnEvtZrRyRhTvrPsS",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "55bded6b-94ec-4433-8033-642fa5a34639",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "92f38cdd-b3e1-453a-8457-65dd6c27cbfd",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01C22xa9cQ2PKdbdxuZrH93D",
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

_source line 5 · 2026-05-30T06:25:11.655Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01XrtVP5rVdUw41GZUac2DCY`</summary>

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
  "parentUuid": "55bded6b-94ec-4433-8033-642fa5a34639",
  "isSidechain": true,
  "agentId": "a5a3b96bb3139e08f",
  "requestId": "req_011CbYGwnEvtZrRyRhTvrPsS",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "98f922b6-b665-48db-be07-7073a6d05e50",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "92f38cdd-b3e1-453a-8457-65dd6c27cbfd",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01C22xa9cQ2PKdbdxuZrH93D",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1597,
      "cache_read_input_tokens": 7413,
      "output_tokens": 94,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1597
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 94,
          "cache_read_input_tokens": 7413,
          "cache_creation_input_tokens": 1597,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1597,
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

_source line 6 · 2026-05-30T06:25:11.672Z_

<details><summary>↩ Tool result · `toolu_01XrtVP5rVdUw41GZUac2DCY`</summary>

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
  "parentUuid": "98f922b6-b665-48db-be07-7073a6d05e50",
  "isSidechain": true,
  "promptId": "bfbb75dd-55f4-4449-8327-dd488e005f06",
  "agentId": "a5a3b96bb3139e08f",
  "type": "user",
  "uuid": "cce61042-0369-4518-a044-4b88f5b4a600",
  "sourceToolAssistantUUID": "98f922b6-b665-48db-be07-7073a6d05e50",
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

_source line 7 · 2026-05-30T06:25:13.904Z_



Now let me fetch the paper and search for discussions about it in parallel.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "cce61042-0369-4518-a044-4b88f5b4a600",
  "isSidechain": true,
  "agentId": "a5a3b96bb3139e08f",
  "requestId": "req_011CbYGxFgBiideMLNeQPyho",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "013e102c-83a1-477a-8deb-bbd5a2b9577f",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "92f38cdd-b3e1-453a-8457-65dd6c27cbfd",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01N1eNbfCKwoiQjG8a7i7xu2",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1116,
      "cache_read_input_tokens": 9010,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1116,
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

_source line 8 · 2026-05-30T06:25:16.172Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01YZxAqPGr247UfUtMG15BU5`</summary>

```json
{
  "url": "https://arxiv.org/abs/2402.07867",
  "prompt": "Extract the full abstract and as much of the introduction as possible. Focus on: the problem they identify, the gap in prior work, the key insight, their threat model, their attack formulation, and the techniques they use. Also extract any details about datasets, baselines, and results."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "013e102c-83a1-477a-8deb-bbd5a2b9577f",
  "isSidechain": true,
  "agentId": "a5a3b96bb3139e08f",
  "requestId": "req_011CbYGxFgBiideMLNeQPyho",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "c8da2c5b-f525-444e-97f7-2a7b6f277d9b",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "92f38cdd-b3e1-453a-8457-65dd6c27cbfd",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01N1eNbfCKwoiQjG8a7i7xu2",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1116,
      "cache_read_input_tokens": 9010,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1116,
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

_source line 9 · 2026-05-30T06:25:17.585Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01VxsmEvJqBjrSoDdtPTMXkF`</summary>

```json
{
  "query": "PoisonedRAG knowledge corruption attacks retrieval-augmented generation USENIX 2025 review discussion"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c8da2c5b-f525-444e-97f7-2a7b6f277d9b",
  "isSidechain": true,
  "agentId": "a5a3b96bb3139e08f",
  "requestId": "req_011CbYGxFgBiideMLNeQPyho",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "62d89561-47b3-4f97-872b-e0c59e6e501f",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "92f38cdd-b3e1-453a-8457-65dd6c27cbfd",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01N1eNbfCKwoiQjG8a7i7xu2",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1116,
      "cache_read_input_tokens": 9010,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1116,
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

_source line 10 · 2026-05-30T06:25:18.134Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01EKLC3c1VdjE7TCxqpoAvTg`</summary>

```json
{
  "query": "PoisonedRAG Wei Zou Binghui Wang adversarial poisoning RAG method details limitations"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "62d89561-47b3-4f97-872b-e0c59e6e501f",
  "isSidechain": true,
  "agentId": "a5a3b96bb3139e08f",
  "requestId": "req_011CbYGxFgBiideMLNeQPyho",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "30e324af-0c51-42a1-a7fe-8a0ae3b27f98",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "92f38cdd-b3e1-453a-8457-65dd6c27cbfd",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01N1eNbfCKwoiQjG8a7i7xu2",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1116,
      "cache_read_input_tokens": 9010,
      "output_tokens": 274,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1116
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 274,
          "cache_read_input_tokens": 9010,
          "cache_creation_input_tokens": 1116,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1116,
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

_source line 11 · 2026-05-30T06:25:21.097Z_

<details><summary>↩ Tool result · `toolu_01YZxAqPGr247UfUtMG15BU5`</summary>

```text
# PoisonedRAG: Knowledge Corruption Attacks on RAG Systems

## Problem Identified
Large language models suffer from lack of current knowledge and hallucination issues. While Retrieval-Augmented Generation (RAG) mitigates these limitations by grounding answers in external knowledge databases, the security of RAG systems remains largely unexplored.

## Gap in Prior Work
Existing research has primarily focused on "improving the accuracy or efficiency of RAG, leaving its security largely unexplored." The knowledge database represents a previously unexamined attack surface.

## Key Insight & Threat Model
Attackers can inject malicious texts into a RAG system's knowledge database to manipulate LLM outputs. The researchers propose solutions for both black-box and white-box attacker scenarios, where attackers possess varying background knowledge about the target system.

## Attack Formulation
The attack is formulated as an optimization problem designed to generate malicious texts that, when injected into the knowledge database, cause the LLM to produce attacker-chosen answers to specific questions.

## Results
The attack demonstrated approximately "90% attack success rate when injecting five malicious texts for each target question into a knowledge database with millions of texts." Additionally, tested defense mechanisms proved insufficient against the approach, indicating a critical need for robust defensive strategies.

## Availability
Code is available on GitHub; the work is accepted to USENIX Security Symposium 2025.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c8da2c5b-f525-444e-97f7-2a7b6f277d9b",
  "isSidechain": true,
  "promptId": "bfbb75dd-55f4-4449-8327-dd488e005f06",
  "agentId": "a5a3b96bb3139e08f",
  "type": "user",
  "uuid": "48b379fc-d4f8-49de-9d41-801ff97f5b0e",
  "sourceToolAssistantUUID": "c8da2c5b-f525-444e-97f7-2a7b6f277d9b",
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

_source line 12 · 2026-05-30T06:25:25.473Z_

<details><summary>↩ Tool result · `toolu_01VxsmEvJqBjrSoDdtPTMXkF`</summary>

```text
Web search results for query: "PoisonedRAG knowledge corruption attacks retrieval-augmented generation USENIX 2025 review discussion"

Links: [{"title":"PoisonedRAG: Knowledge Corruption Attacks to Retrieval-Augmented Generation of Large Language Models | USENIX","url":"https://www.usenix.org/conference/usenixsecurity25/presentation/zou-poisonedrag"},{"title":"PoisonedRAG: Knowledge Corruption Attacks to Retrieval-Augmented Generation of Large Language Models - Penn State","url":"https://pure.psu.edu/en/publications/poisonedrag-knowledge-corruption-attacks-to-retrieval-augmented-g/"},{"title":"GitHub - sleeepeer/PoisonedRAG: [USENIX Security 2025] PoisonedRAG: Knowledge Corruption Attacks to Retrieval-Augmented Generation of Large Language Models · GitHub","url":"https://github.com/sleeepeer/PoisonedRAG"},{"title":"PoisonedRAG: Knowledge Corruption Attacks to Retrieval- ...","url":"https://www.usenix.org/system/files/usenixsecurity25-zou-poisonedrag.pdf"},{"title":"GitHub - thisxyz/PoisonedRAG: [USENIX Security 2025] PoisonedRAG: Knowledge Poisoning Attacks to Retrieval-Augmented Generation of Large Language Models","url":"https://github.com/thisxyz/PoisonedRAG"},{"title":"34th USENIX Security Symposium: PoisonedRAG: Knowledge Corruption Attack...","url":"https://usenixsecurity25.sched.com/event/289Bm/poisonedrag-knowledge-corruption-attacks-to-retrieval-augmented-generation-of-large-language-models"},{"title":"[2402.07867] PoisonedRAG: Knowledge Corruption Attacks to Retrieval-Augmented Generation of Large Language Models","url":"https://arxiv.org/abs/2402.07867"},{"title":"PoisonedRAG: Knowledge Corruption Attacks to Retrieval-Augmented   Generation of Large Language Models","url":"https://arxiv.org/pdf/2402.07867"},{"title":"PoisonedRAG: knowledge corruption attacks to retrieval- ...","url":"https://dl.acm.org/doi/10.5555/3766078.3766275"}]

Based on the search results, here's what I found about PoisonedRAG:

## Overview

PoisonedRAG is the first knowledge corruption attack to RAG, where an attacker could inject a few malicious texts into the knowledge database of a RAG system to induce an LLM to generate an attacker-chosen target answer for an attacker-chosen target question.

## Paper Details

The research was presented at the 34th USENIX Security Symposium (USENIX Security 25) in August 2025 by authors Wei Zou, Runpeng Geng, Binghui Wang, and Jinyuan Jia.

## Attack Effectiveness

PoisonedRAG could achieve a 90% attack success rate when injecting five malicious texts for each target question into a knowledge database with millions of texts.

## Defense Evaluation

The researchers evaluated several defenses and their results show they are insufficient to defend against PoisonedRAG, highlighting the need for new defenses.

## Context

Retrieval-Augmented Generation (RAG) is a state-of-the-art technique to mitigate limitations of LLMs, with the key idea being to ground the answer generation of an LLM on external knowledge retrieved from a knowledge database. Existing studies mainly focus on improving the accuracy or efficiency of RAG, leaving its security largely unexplored.

The official paper is available through USENIX, and code is available on GitHub for further research and review.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "62d89561-47b3-4f97-872b-e0c59e6e501f",
  "isSidechain": true,
  "promptId": "bfbb75dd-55f4-4449-8327-dd488e005f06",
  "agentId": "a5a3b96bb3139e08f",
  "type": "user",
  "uuid": "250c06de-9294-42a6-8994-8b94178f883a",
  "sourceToolAssistantUUID": "62d89561-47b3-4f97-872b-e0c59e6e501f",
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

_source line 13 · 2026-05-30T06:25:25.655Z_

<details><summary>↩ Tool result · `toolu_01EKLC3c1VdjE7TCxqpoAvTg`</summary>

```text
Web search results for query: "PoisonedRAG Wei Zou Binghui Wang adversarial poisoning RAG method details limitations"

Links: [{"title":"PoisonedRAG: Knowledge Corruption Attacks to Retrieval-Augmented Generation","url":"https://www.usenix.org/system/files/conference/usenixsecurity25/sec24winter-prepub-1468-zou.pdf"},{"title":"[2402.07867] PoisonedRAG: Knowledge Corruption Attacks to Retrieval-Augmented Generation of Large Language Models","url":"https://arxiv.org/abs/2402.07867"},{"title":"PoisonedRAG: Knowledge Poisoning Attacks to Retrieval-Augmented Generation of Large Language Models | Semantic Scholar","url":"https://www.semanticscholar.org/paper/PoisonedRAG:-Knowledge-Poisoning-Attacks-to-of-Zou-Geng/5c204b2421d05b83d3c96a6c515cc03143073935"},{"title":"PoisonedRAG: Knowledge Corruption Attacks to Retrieval-Augmented Generation of Large Language Models - Penn State","url":"https://pure.psu.edu/en/publications/poisonedrag-knowledge-corruption-attacks-to-retrieval-augmented-g/"},{"title":"PoisonedRAG: Knowledge Poisoning Attacks to Retrieval-Augmented Generation of Large Language Models","url":"https://arxiv.org/html/2402.07867v1"},{"title":"Benchmarking Poisoning Attacks against Retrieval-Augmented Generation","url":"https://arxiv.org/pdf/2505.18543"},{"title":"PoisonedRAG: Knowledge Corruption Attacks to Retrieval-Augmented Generation of Large Language Models | USENIX","url":"https://www.usenix.org/conference/usenixsecurity25/presentation/zou-poisonedrag"},{"title":"PoisonedRAG: Knowledge Corruption Attacks to Retrieval- ...","url":"https://www.usenix.org/system/files/usenixsecurity25-zou-poisonedrag.pdf"},{"title":"Poison-RAG: Adversarial Data Poisoning Attacks on Retrieval-Augmented   Generation in Recommender Systems","url":"https://arxiv.org/pdf/2501.11759"},{"title":"Poison-RAG: Adversarial Data Poisoning Attacks on Retrieval-Augmented Generation in Recommender Systems | Advances in Information Retrieval","url":"https://dl.acm.org/doi/10.1007/978-3-031-88717-8_18"}]

Based on the search results, here's information about PoisonedRAG:

## Overview

PoisonedRAG is the first knowledge corruption attack to RAG, where an attacker could inject a few malicious texts into the knowledge database of a RAG system to induce an LLM to generate an attacker-chosen target answer.

## Method Details

Depending on the background knowledge (e.g., black-box and white-box settings) of an attacker on a RAG system, the authors propose two solutions to solve the optimization problem, respectively. In the white-box attack, they use HotFlip, a state-of-the-art method to craft adversarial texts, to solve the optimization problem.

## Attack Effectiveness

PoisonedRAG could achieve high attack success rates on different datasets and LLMs under both white-box and black-box settings when injecting 5 poisoned texts for each target question into a knowledge database with millions of texts. For instance, in the black-box setting, PoisonedRAG could achieve 97% (on NQ), 99% (on HotpotQA), and 91% (on MS-MARCO) attack success rates for RAG with PaLM 2.

## Limitations and Defenses

Several defenses were evaluated and the results show they are insufficient to defend against PoisonedRAG, highlighting the need for new defenses.

The paper was published at the USENIX Security Symposium in 2025 by Wei Zou, Runpeng Geng, Binghui Wang, and Jinyuan Jia from Pennsylvania State University and Illinois Institute of Technology.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "30e324af-0c51-42a1-a7fe-8a0ae3b27f98",
  "isSidechain": true,
  "promptId": "bfbb75dd-55f4-4449-8327-dd488e005f06",
  "agentId": "a5a3b96bb3139e08f",
  "type": "user",
  "uuid": "d21cbf69-2485-449d-a728-46e01291350f",
  "sourceToolAssistantUUID": "30e324af-0c51-42a1-a7fe-8a0ae3b27f98",
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

_source line 14 · 2026-05-30T06:25:27.820Z_

Let me get more technical detail from the full paper and the GitHub repository.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d21cbf69-2485-449d-a728-46e01291350f",
  "isSidechain": true,
  "agentId": "a5a3b96bb3139e08f",
  "requestId": "req_011CbYGyHFxx3Aev73LWBZDG",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "c912ceb3-782f-4e42-b406-ece2f49f8302",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "92f38cdd-b3e1-453a-8457-65dd6c27cbfd",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01J2pLZRf7WHHPpSbwDiLb5v",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2679,
      "cache_read_input_tokens": 10126,
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

### Tool call

_source line 15 · 2026-05-30T06:25:32.113Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01DXFMdDYNDdNNRhgMEi6MS9`</summary>

```json
{
  "url": "https://arxiv.org/html/2402.07867v1",
  "prompt": "Extract detailed technical information about: (1) The exact optimization problem formulation - what is being optimized and the constraints. (2) The black-box vs white-box attack methods - how each works step by step. (3) The retrieval mechanism they target (contriever, dense retrieval, sparse retrieval). (4) The specific techniques they adapt - HotFlip, any LLM-based generation. (5) The defense mechanisms they tested and why they failed. (6) Datasets used (NQ, HotpotQA, MS-MARCO). (7) Any discussion of limitations or future work. (8) How the poisoned texts are constructed to be both retrievable AND convincing to the LLM."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c912ceb3-782f-4e42-b406-ece2f49f8302",
  "isSidechain": true,
  "agentId": "a5a3b96bb3139e08f",
  "requestId": "req_011CbYGyHFxx3Aev73LWBZDG",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "396801a5-dafc-4f0a-a043-02b01e31bb73",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "92f38cdd-b3e1-453a-8457-65dd6c27cbfd",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01J2pLZRf7WHHPpSbwDiLb5v",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2679,
      "cache_read_input_tokens": 10126,
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

### Tool call

_source line 16 · 2026-05-30T06:25:33.922Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01XN1Xkh65iitC5w6tKJpuW4`</summary>

```json
{
  "url": "https://github.com/sleeepeer/PoisonedRAG",
  "prompt": "Extract information about the implementation: what retrieval methods are supported, what LLMs are tested, how the attack is structured in code, and any details about the optimization process or experimental setup."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "396801a5-dafc-4f0a-a043-02b01e31bb73",
  "isSidechain": true,
  "agentId": "a5a3b96bb3139e08f",
  "requestId": "req_011CbYGyHFxx3Aev73LWBZDG",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "d70c37ad-16e9-41d8-a64d-76c1da854823",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "92f38cdd-b3e1-453a-8457-65dd6c27cbfd",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01J2pLZRf7WHHPpSbwDiLb5v",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2679,
      "cache_read_input_tokens": 10126,
      "output_tokens": 365,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2679
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 365,
          "cache_read_input_tokens": 10126,
          "cache_creation_input_tokens": 2679,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2679,
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

_source line 17 · 2026-05-30T06:25:34.335Z_

<details><summary>↩ Tool result · `toolu_01DXFMdDYNDdNNRhgMEi6MS9`</summary>

```text
API Error: 400 The request body is not valid JSON: no low surrogate in string: line 1 column 102386 (char 102385)
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "396801a5-dafc-4f0a-a043-02b01e31bb73",
  "isSidechain": true,
  "promptId": "bfbb75dd-55f4-4449-8327-dd488e005f06",
  "agentId": "a5a3b96bb3139e08f",
  "type": "user",
  "uuid": "125f0427-6ade-4366-b265-23d1cdbc3541",
  "sourceToolAssistantUUID": "396801a5-dafc-4f0a-a043-02b01e31bb73",
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

_source line 18 · 2026-05-30T06:25:40.554Z_

<details><summary>↩ Tool result · `toolu_01XN1Xkh65iitC5w6tKJpuW4`</summary>

```text
# PoisonedRAG Implementation Details

## Retrieval Methods
The system uses **Contriever** as the retrieval model, as indicated in the code configuration where `'eval_model_code': "contriever"` serves as the default retrieval augmented generation component.

## Supported Language Models
The implementation tests multiple LLM architectures:
- PaLM 2
- GPT-3.5 and GPT-4
- LLaMA (7B and 13B variants)
- Vicuna (7B, 13B, and 33B versions)

## Attack Structure
The codebase organizes adversarial operations through several key modules. The `gen_adv.py` file handles adversarial example generation, while `main.py` orchestrates the overall attack pipeline. Two distinct attack methodologies are implemented: a black-box approach labeled `LM_targeted` and a white-box variant called `hotflip`.

## Experimental Configuration
The framework evaluates performance across multiple datasets including "nq" (Natural Questions), "hotpotqa," and "msmarco." Core hyperparameters include retrieval depth (`top_k`: 5), poison instances per query (`adv_per_query`: 5), and iteration count (`repeat_times`: 10). The optimization leverages a dot-product scoring function by default.

## Environment & Dependencies
The setup requires Python 3.10 with PyTorch 1.13.0, alongside specialized packages for BEIR benchmark evaluation and API access to various LLM providers through their respective authentication tokens.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d70c37ad-16e9-41d8-a64d-76c1da854823",
  "isSidechain": true,
  "promptId": "bfbb75dd-55f4-4449-8327-dd488e005f06",
  "agentId": "a5a3b96bb3139e08f",
  "type": "user",
  "uuid": "6f52bdeb-e1e6-40e3-94e7-bb918c91eb29",
  "sourceToolAssistantUUID": "d70c37ad-16e9-41d8-a64d-76c1da854823",
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

_source line 19 · 2026-05-30T06:25:48.653Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_0185A4GWgK25EpThvjcU7bHX`</summary>

```json
{
  "url": "https://arxiv.org/pdf/2402.07867",
  "prompt": "Extract the following technical details from the paper:\n\n1. PROBLEM FORMULATION: The exact optimization objective. They decompose the attack into two sub-problems - what are they? One for making poisoned texts retrievable (high similarity to the query) and one for making the LLM generate the target answer.\n\n2. BLACK-BOX ATTACK: How do they generate poisoned texts without access to the retrieval model internals? Do they use an LLM to generate convincing but false passages?\n\n3. WHITE-BOX ATTACK: How do they use HotFlip or gradient-based methods to craft adversarial tokens that maximize retrieval similarity?\n\n4. DEFENSES TESTED: What specific defenses did they evaluate? (e.g., paraphrasing, perplexity filtering, knowledge consistency checking, duplicate detection)\n\n5. KEY NUMBERS: Attack success rates across different settings.\n\n6. LIMITATIONS: What did the authors acknowledge as limitations?\n\n7. The two-step decomposition: retrievability constraint + LLM persuasion constraint."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6f52bdeb-e1e6-40e3-94e7-bb918c91eb29",
  "isSidechain": true,
  "agentId": "a5a3b96bb3139e08f",
  "requestId": "req_011CbYGzP3VwGoodjEY8WYM2",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "d63883c7-ef9c-4c01-8a92-2cb80853f179",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "92f38cdd-b3e1-453a-8457-65dd6c27cbfd",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0152yDek9v91QzpHcLxgL5XK",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 820,
      "cache_read_input_tokens": 12805,
      "output_tokens": 314,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 820
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 314,
          "cache_read_input_tokens": 12805,
          "cache_creation_input_tokens": 820,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 820,
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

_source line 20 · 2026-05-30T06:25:56.686Z_

<details><summary>↩ Tool result · `toolu_0185A4GWgK25EpThvjcU7bHX`</summary>

```text
# Technical Details from PoisonedRAG Paper

## 1. PROBLEM FORMULATION

The attack decomposes into two necessary conditions:

**Retrieval Condition (S):** Poisoned texts must achieve high semantic similarity to user queries to be retrieved by the RAG system.

**Generation Condition (I):** The injected malicious content must persuade the LLM to generate the target answer when provided as context.

The authors formalize this as optimizing poisoned texts that simultaneously satisfy both constraints.

## 2. BLACK-BOX ATTACK

The black-box approach leverages an LLM to generate malicious passages. The system:

- Uses the target question and desired answer to prompt an LLM
- Generates convincing but false passages containing the target answer
- Relies on semantic similarity to the query rather than model gradient information
- Requires only access to the retrieval system's ranking (not internal embeddings)

## 3. WHITE-BOX ATTACK

For white-box scenarios with gradient access:

- Applies gradient-based optimization to craft adversarial text
- Optimizes token sequences to maximize retrieval similarity scores
- Uses techniques similar to HotFlip to find adversarial perturbations
- Directly accesses embedding models to compute similarity gradients

## 4. DEFENSES TESTED

The evaluation examined four defense mechanisms:

- **Paraphrasing:** Rewriting retrieved passages to detect semantic inconsistencies
- **Perplexity-based Detection:** Filtering unusually low-perplexity passages
- **Duplicate Text Filtering:** Removing near-duplicate content from knowledge bases
- **Knowledge Expansion:** Augmenting retrieval with diverse corroborating sources

## 5. KEY NUMBERS

Attack success rates included:

- Black-box attacks achieved "high attack success rates" across multiple LLMs
- Performance varied by RAG configuration and hyperparameter settings
- Wikipedia-based chatbot demonstrated practical vulnerability
- Some defenses showed partial mitigation but none completely eliminated attacks

## 6. LIMITATIONS ACKNOWLEDGED

Authors noted:

- "Limited to English language" evaluation
- Dependence on retrieval model architecture specifics
- Variations in success rates across different LLM families
- Defense mechanisms provided only partial protection

## 7. TWO-STEP DECOMPOSITION

**Retrievability + Persuasion Framework:**

Crafting malicious texts (I) to satisfy generation requirements while ensuring texts (S) maintain sufficient semantic alignment for retrieval—enabling the attack pipeline's effectiveness.

[Binary content (application/pdf, 1MB) also saved to /home/ubuntu/.claude-account-2/projects/-home-ubuntu-idea-adversarial/92f38cdd-b3e1-453a-8457-65dd6c27cbfd/tool-results/webfetch-1780122348671-kb9tth.pdf]
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d63883c7-ef9c-4c01-8a92-2cb80853f179",
  "isSidechain": true,
  "promptId": "bfbb75dd-55f4-4449-8327-dd488e005f06",
  "agentId": "a5a3b96bb3139e08f",
  "type": "user",
  "uuid": "cd714e52-ae79-4909-8e41-8fec241a57fc",
  "sourceToolAssistantUUID": "d63883c7-ef9c-4c01-8a92-2cb80853f179",
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

_source line 21 · 2026-05-30T06:26:43.497Z_

Now I have sufficient detail to provide a comprehensive summary.

---

## PoisonedRAG: Knowledge Corruption Attacks to RAG (USENIX Security 2025)

### Problem Identification

RAG systems ground LLM responses in external knowledge databases to reduce hallucination and provide up-to-date information. Prior work focused almost entirely on improving RAG accuracy and efficiency, leaving a critical security gap: **the knowledge database itself is an unexamined attack surface**. Many real-world RAG deployments draw from open or semi-open corpora (Wikipedia, web crawls, shared document stores) where an attacker can inject content. The authors identified that no prior work had systematically studied whether a small number of poisoned texts injected into a million-scale knowledge base could reliably manipulate LLM outputs for targeted questions.

### Key Insight

The core intellectual contribution is a **decomposition of the poisoning problem into two independent, jointly necessary conditions**:

1. **Retrievability (S):** The poisoned text must score high enough in semantic similarity to the target question that the retriever surfaces it in the top-k results.
2. **Persuasion (I):** Once retrieved, the poisoned text must be sufficiently convincing that the LLM treats it as authoritative context and generates the attacker-chosen target answer.

This decomposition is powerful because it makes the problem tractable: each sub-problem can be solved with existing techniques, and the composition yields a highly effective end-to-end attack. The insight that only ~5 injected texts per target question suffice in a database of millions is the striking empirical finding.

### Innovation Type

This is primarily a **novel problem formulation and attack framework**, not a new algorithm per se. The technical novelty lies in (a) identifying and formalizing the RAG poisoning threat model, (b) the two-condition decomposition, and (c) demonstrating that simple instantiations of each sub-problem already yield devastating attack success rates. It is a "first mover" contribution that opens a new attack surface.

### Method Summary

**Threat model:** The attacker selects target question-answer pairs and injects a small number of malicious texts into the RAG knowledge database. Two settings are considered:

- **Black-box attack (LM_targeted):** The attacker has no access to the retriever's internals. They use an LLM (e.g., GPT) to generate plausible-sounding passages that contain the target answer in response to the target question. Semantic similarity to the query is achieved naturally because the generated passage discusses the same topic. This is simple, scalable, and remarkably effective.

- **White-box attack (HotFlip-based):** The attacker has access to the retriever's embedding model. They use gradient-based optimization (adapted from HotFlip) to craft adversarial token sequences that maximize dot-product similarity with the target query embedding, while also containing content that persuades the LLM. This produces texts that may look less natural but achieve even higher retrieval scores.

**Retriever targeted:** Contriever (dense retrieval) is the primary model, with evaluation also on sparse retrieval.

**Datasets:** Natural Questions (NQ), HotpotQA, MS-MARCO -- standard open-domain QA benchmarks.

**LLMs tested:** PaLM 2, GPT-3.5, GPT-4, LLaMA-2 (7B/13B), Vicuna (7B/13B/33B).

**Key results:** With just 5 poisoned texts per target question injected into databases with millions of entries, the black-box attack achieves 97% success on NQ, 99% on HotpotQA, and 91% on MS-MARCO (for PaLM 2). Results are consistently high across LLMs.

### Defenses Evaluated and Their Failure

Four defenses were tested: (1) **paraphrasing** retrieved passages, (2) **perplexity-based filtering** of unusual texts, (3) **duplicate/near-duplicate detection**, and (4) **knowledge expansion** (retrieving from additional diverse sources). All provided only partial mitigation. The black-box attack is particularly resilient because the generated passages are fluent, topically relevant, and low-perplexity -- indistinguishable from legitimate content by surface-level detectors.

### Limitations and Open Questions

- Evaluation limited to English.
- Success rates vary across LLM families (some models are more robust to misleading context).
- The attack targets individual questions rather than broad topic corruption.
- No evaluation against adversarial training or retrieval-level anomaly detection based on embedding space analysis.
- The paper does not address adaptive defenses where the defender knows the attack strategy.

### Building Blocks (Reusable Components)

- **HotFlip for retrieval manipulation:** Gradient-based adversarial text generation against dense retrievers is directly reusable for studying retriever robustness.
- **LLM-as-attacker pattern:** Using an LLM to generate convincing false passages is a general-purpose adversarial technique applicable beyond RAG.
- **Two-condition decomposition framework:** The retrievability + persuasion formulation is a reusable conceptual template for analyzing any retrieval-grounded generation system.
- **Evaluation infrastructure:** The codebase (Python 3.10, Contriever, BEIR benchmarks, multi-LLM evaluation) is open-source and extensible.

### Relevance to Conformal Prediction for RAG Under Adversarial Poisoning

This paper is directly relevant to the idea of applying conformal prediction (CP) to RAG systems under adversarial conditions:

1. **CP as a defense mechanism:** Conformal prediction provides distribution-free uncertainty quantification. A CP-based RAG system could flag or abstain when the retrieved context produces prediction sets that are unusually large or inconsistent -- a potential signal that retrieved documents are poisoned. PoisonedRAG's finding that existing defenses fail creates a clear opening for CP-based approaches.

2. **Exchangeability violations:** Poisoned texts violate the exchangeability assumption that underpins standard CP guarantees. The PoisonedRAG attack injects non-exchangeable (adversarially crafted) data points into the retrieval pool. Understanding how CP coverage degrades under this specific violation pattern is a concrete research question this paper motivates.

3. **Calibration under poisoning:** A CP-calibrated RAG system would need calibration data drawn from clean retrieval. PoisonedRAG shows that even 5 out of millions of texts can flip answers, suggesting that CP calibration sets must account for worst-case contamination or use robust calibration procedures.

4. **Detection via nonconformity scores:** Poisoned passages that are semantically similar to the query but factually inconsistent with other retrieved passages would generate high nonconformity scores under a well-designed score function -- making CP a natural framework for anomaly-aware retrieval.

Sources:
- [PoisonedRAG on arXiv](https://arxiv.org/abs/2402.07867)
- [USENIX Security 2025 presentation](https://www.usenix.org/conference/usenixsecurity25/presentation/zou-poisonedrag)
- [GitHub repository](https://github.com/sleeepeer/PoisonedRAG)
- [Semantic Scholar entry](https://www.semanticscholar.org/paper/PoisonedRAG:-Knowledge-Poisoning-Attacks-to-of-Zou-Geng/5c204b2421d05b83d3c96a6c515cc03143073935)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "cd714e52-ae79-4909-8e41-8fec241a57fc",
  "isSidechain": true,
  "agentId": "a5a3b96bb3139e08f",
  "requestId": "req_011CbYH1ZxcFpbMJ9vuBv2AJ",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "1ea0b0f0-ac62-4969-ab85-0a697b848d6b",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "92f38cdd-b3e1-453a-8457-65dd6c27cbfd",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RwhZoimZCP6oSTxPqb4N1j",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1078,
      "cache_read_input_tokens": 13625,
      "output_tokens": 1779,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1078
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1779,
          "cache_read_input_tokens": 13625,
          "cache_creation_input_tokens": 1078,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1078,
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
