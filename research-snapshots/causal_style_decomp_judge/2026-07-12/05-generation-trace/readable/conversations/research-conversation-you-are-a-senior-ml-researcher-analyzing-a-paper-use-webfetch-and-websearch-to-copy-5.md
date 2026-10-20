# Research conversation: You are a senior ML researcher analyzing a paper. Use WebFetch and WebSearch to gather detailed information about this p

**The Likert Blindspot: Measurement-Mode Divergence in LLM Judge Style Evaluation (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 39
- **Recorded user turns:** 1
- **Tool calls:** 14
- **Original source:** `logs/chats/exported-trajectories/account-2/agent-a5512f66970097acf.jsonl`
- **Structured JSON:** [`fc7815050e7cd2faf4d7.json`](../../sessions/fc/fc7815050e7cd2faf4d7.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

39 recorded events

### User

_source line 1 · 2026-05-29T10:06:20.632Z_

You are a senior ML researcher analyzing a paper. Use WebFetch and WebSearch to gather detailed information about this paper:

**Paper:** "Scaling LLM Inference with Optimized Sample Compute Allocation (OSCA)" by Zhang et al., NAACL 2025, https://arxiv.org/abs/2410.22480

Tasks:
1. Use WebFetch on https://arxiv.org/abs/2410.22480 to read the abstract and introduction.
2. Use WebFetch on https://arxiv.org/html/2410.22480 to read the full paper (method, key results, experiments).
3. Search for OpenReview or reviewer comments: search "OSCA Optimized Sample Compute Allocation NAACL 2025 review" and try to fetch any review page if found.

For your final response, provide a detailed analysis covering:
- What gap did they identify and HOW? (specific prior work limitations)
- What was the key insight others missed?
- How did they formulate the problem differently?
- What existing techniques did they adapt/combine/simplify?
- What are the main experimental findings (specific numbers, benchmarks)?
- Reviewer comments if found (what was praised, what was criticized)?
- What are the limitations and open questions?
- What building blocks (methods, datasets, frameworks) could be reused?

Be thorough and specific — cite specific numbers, dataset names, method details. This paper is highly relevant because it optimizes allocation across inference configurations similar to our K-d optimization.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "295c0657-e121-425c-967b-f63279f1549e",
  "agentId": "a5512f66970097acf",
  "type": "user",
  "uuid": "0a327f22-c8d7-46c5-9cc4-8547428bc4ca",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "393d191a-0034-4130-a331-edb9d3156024",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 2 · 2026-05-29T10:06:20.634Z_

```json
{
  "parentUuid": "0a327f22-c8d7-46c5-9cc4-8547428bc4ca",
  "isSidechain": true,
  "agentId": "a5512f66970097acf",
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
  "uuid": "03ca20d7-2084-4679-8a15-21608c5bcbfb",
  "timestamp": "2026-05-29T10:06:20.634Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "393d191a-0034-4130-a331-edb9d3156024",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 3 · 2026-05-29T10:06:20.634Z_

```json
{
  "parentUuid": "03ca20d7-2084-4679-8a15-21608c5bcbfb",
  "isSidechain": true,
  "agentId": "a5512f66970097acf",
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "4db2a202-6441-4e32-9d94-ba2653dcbac8",
  "timestamp": "2026-05-29T10:06:20.634Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "393d191a-0034-4130-a331-edb9d3156024",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Assistant

_source line 4 · 2026-05-29T10:06:25.520Z_



I'll start by fetching the paper's abstract page and the full HTML version, plus searching for reviews.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4db2a202-6441-4e32-9d94-ba2653dcbac8",
  "isSidechain": true,
  "agentId": "a5512f66970097acf",
  "requestId": "req_011CbWg1T3JzVEKUQA7FkHH9",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "8093fc3d-78e9-455e-8160-b121fc52f2c8",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "393d191a-0034-4130-a331-edb9d3156024",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01P74ri4VZc7SuyHV3DcgBsY",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1694,
      "cache_read_input_tokens": 7413,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1694,
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

_source line 5 · 2026-05-29T10:06:25.949Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_016g7rKBzChbWSVkh7CLsspG`</summary>

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
  "parentUuid": "8093fc3d-78e9-455e-8160-b121fc52f2c8",
  "isSidechain": true,
  "agentId": "a5512f66970097acf",
  "requestId": "req_011CbWg1T3JzVEKUQA7FkHH9",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "437de94c-ff69-43bd-9ce3-82e014e3762b",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "393d191a-0034-4130-a331-edb9d3156024",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01P74ri4VZc7SuyHV3DcgBsY",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1694,
      "cache_read_input_tokens": 7413,
      "output_tokens": 103,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1694
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 103,
          "cache_read_input_tokens": 7413,
          "cache_creation_input_tokens": 1694,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1694,
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

_source line 6 · 2026-05-29T10:06:25.952Z_

<details><summary>↩ Tool result · `toolu_016g7rKBzChbWSVkh7CLsspG`</summary>

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
  "parentUuid": "437de94c-ff69-43bd-9ce3-82e014e3762b",
  "isSidechain": true,
  "promptId": "295c0657-e121-425c-967b-f63279f1549e",
  "agentId": "a5512f66970097acf",
  "type": "user",
  "uuid": "2f433517-956a-4443-8b00-5fdea138e5ec",
  "sourceToolAssistantUUID": "437de94c-ff69-43bd-9ce3-82e014e3762b",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "393d191a-0034-4130-a331-edb9d3156024",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 7 · 2026-05-29T10:06:28.814Z_



Now let me fetch the paper from multiple sources and search for reviews in parallel.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2f433517-956a-4443-8b00-5fdea138e5ec",
  "isSidechain": true,
  "agentId": "a5512f66970097acf",
  "requestId": "req_011CbWg1r5eM5kX38BATrBvp",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "fef3399a-1a1a-49ef-b4f1-941aa52d61b0",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "393d191a-0034-4130-a331-edb9d3156024",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019HfBG84QafqDZ4DV3K8rXw",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1125,
      "cache_read_input_tokens": 9107,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1125,
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

_source line 8 · 2026-05-29T10:06:30.248Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_016mo7zn4KUG3XK7mnMt5x4C`</summary>

```json
{
  "url": "https://arxiv.org/abs/2410.22480",
  "prompt": "Extract the full abstract, author list, and any introductory information about this paper. Include all details about the paper's contributions, methodology overview, and key results mentioned in the abstract."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "fef3399a-1a1a-49ef-b4f1-941aa52d61b0",
  "isSidechain": true,
  "agentId": "a5512f66970097acf",
  "requestId": "req_011CbWg1r5eM5kX38BATrBvp",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "33feb821-2d2f-44f4-b932-ac3c494e6353",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "393d191a-0034-4130-a331-edb9d3156024",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019HfBG84QafqDZ4DV3K8rXw",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1125,
      "cache_read_input_tokens": 9107,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1125,
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

_source line 9 · 2026-05-29T10:06:35.192Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_017ue2yKGCq32smXZUsqsRZ1`</summary>

```json
{
  "url": "https://arxiv.org/html/2410.22480",
  "prompt": "Extract the full content of this paper in detail. I need:\n1. The complete Introduction section - what gap/problem do they identify, what prior work do they cite and what are its limitations?\n2. The complete Method section - how do they formulate the optimization problem? What is OSCA exactly? What mathematical formulation do they use? How do they allocate compute across samples?\n3. The complete Experiments section - what benchmarks, models, baselines do they use? What are the specific numerical results (accuracy percentages, compute savings)?\n4. The Results and Analysis - what are the key findings and ablations?\n5. The Limitations and Conclusion sections.\n6. Any tables and figures descriptions with specific numbers.\nBe as thorough and specific as possible - include exact numbers, dataset names, model names, and mathematical formulations."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "33feb821-2d2f-44f4-b932-ac3c494e6353",
  "isSidechain": true,
  "agentId": "a5512f66970097acf",
  "requestId": "req_011CbWg1r5eM5kX38BATrBvp",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "58a0f938-c8e0-47b3-8420-3b5a6fd5a1fb",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "393d191a-0034-4130-a331-edb9d3156024",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019HfBG84QafqDZ4DV3K8rXw",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1125,
      "cache_read_input_tokens": 9107,
      "output_tokens": 440,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1125
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 440,
          "cache_read_input_tokens": 9107,
          "cache_creation_input_tokens": 1125,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1125,
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

_source line 10 · 2026-05-29T10:06:35.903Z_

<details><summary>↩ Tool result · `toolu_016mo7zn4KUG3XK7mnMt5x4C`</summary>

```text
# Paper Summary: Scaling LLM Inference with Optimized Sample Compute Allocation

**Authors:** Kexun Zhang, Shang Zhou, Danqing Wang, William Yang Wang, and Lei Li

**arXiv ID:** 2410.22480 (Submitted: October 29, 2024)

## Abstract Overview

The research addresses the challenge of efficiently scaling language model inference under computational constraints. The core problem involves determining optimal configurations for sampling operations, including which models, temperature settings, and languages to employ, and how many samples to generate per configuration.

## Key Contribution

The team developed OSCA (Optimized Sample Compute Allocation), an algorithm designed to discover the best mixture of different inference configurations. Rather than relying on a single configuration, this approach identifies a strategic blend that improves performance while reducing resource requirements.

## Major Results

The methodology demonstrated substantial efficiency gains across multiple domains:

- **Code generation:** "achieve accuracy better than the best single configuration with 128x less compute"
- **Reasoning tasks:** Improved performance on four reasoning benchmarks using 25x fewer resources
- **Real-world application:** When tested on SWE-Bench within agentic workflows, the approach achieved superior accuracy with "3x less compute than the default configuration"

The authors have made their code and generated outputs publicly available through GitHub, supporting reproducibility and community engagement with their work.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "33feb821-2d2f-44f4-b932-ac3c494e6353",
  "isSidechain": true,
  "promptId": "295c0657-e121-425c-967b-f63279f1549e",
  "agentId": "a5512f66970097acf",
  "type": "user",
  "uuid": "2225c4a2-fc19-4459-8824-a31760c6ab7a",
  "sourceToolAssistantUUID": "33feb821-2d2f-44f4-b932-ac3c494e6353",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "393d191a-0034-4130-a331-edb9d3156024",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-29T10:06:35.916Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_015grRUfMaEn61jjRKrTdG6A`</summary>

```json
{
  "query": "OSCA Optimized Sample Compute Allocation NAACL 2025 review OpenReview"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2225c4a2-fc19-4459-8824-a31760c6ab7a",
  "isSidechain": true,
  "agentId": "a5512f66970097acf",
  "requestId": "req_011CbWg1r5eM5kX38BATrBvp",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "b4b213f1-303b-4f3f-b752-3e36070cb57b",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "393d191a-0034-4130-a331-edb9d3156024",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019HfBG84QafqDZ4DV3K8rXw",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1125,
      "cache_read_input_tokens": 9107,
      "output_tokens": 440,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1125
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 440,
          "cache_read_input_tokens": 9107,
          "cache_creation_input_tokens": 1125,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1125,
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

_source line 12 · 2026-05-29T10:06:42.554Z_

<details><summary>↩ Tool result · `toolu_015grRUfMaEn61jjRKrTdG6A`</summary>

```text
Web search results for query: "OSCA Optimized Sample Compute Allocation NAACL 2025 review OpenReview"

Links: [{"title":"Scaling LLM Inference Efficiently with Optimized Sample Compute Allocation - ACL Anthology","url":"https://aclanthology.org/2025.naacl-long.404/"},{"title":"Scaling LLM Inference with Optimized Sample Compute Allocation","url":"https://arxiv.org/pdf/2410.22480"},{"title":"[2410.22480] Scaling LLM Inference with Optimized Sample Compute Allocation","url":"https://arxiv.org/abs/2410.22480"},{"title":"[Literature Review] Scaling LLM Inference with Optimized Sample Compute Allocation","url":"https://www.themoonlight.io/en/review/scaling-llm-inference-with-optimized-sample-compute-allocation"},{"title":"Scaling LLM Inference Efficiently with Optimized Sample ...","url":"https://aclanthology.org/2025.naacl-long.404.pdf"},{"title":"Scaling LLM Inference Efficiently with Optimized Sample Compute Allocation | Request PDF","url":"https://www.researchgate.net/publication/392505821_Scaling_LLM_Inference_Efficiently_with_Optimized_Sample_Compute_Allocation"}]

Based on the search results, I found information about OSCA (Optimized Sample Compute Allocation):

OSCA is an algorithm that optimizes sample compute allocation by finding an optimal mix of different inference configurations. The paper was published in the Proceedings of the 2025 Conference of the Nations of the Americas Chapter of the Association for Computational Linguistics (NAACL 2025).

The research shows that with the learned mixed allocation, they can achieve accuracy better than the best single configuration with 128x less compute on code generation and 25x less compute on 4 reasoning tasks. OSCA is also effective in agentic workflows beyond single-turn tasks, achieving better accuracy on SWE-Bench with 3x less compute than the default configuration.

The paper addresses the challenge of efficiently allocating compute resources across different sampling configurations when scaling LLM inference. OSCA utilizes a hill-climbing approach, beginning with a randomly initialized allocation and iteratively exploring neighboring allocations to find a better one by maximizing the expected pass rate.

You can find the published paper at the ACL Anthology (aclanthology.org/2025.naacl-long.404/) and the code has been released on GitHub.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "b4b213f1-303b-4f3f-b752-3e36070cb57b",
  "isSidechain": true,
  "promptId": "295c0657-e121-425c-967b-f63279f1549e",
  "agentId": "a5512f66970097acf",
  "type": "user",
  "uuid": "e2dcc26f-c9ae-4288-9cf1-332860aedba8",
  "sourceToolAssistantUUID": "b4b213f1-303b-4f3f-b752-3e36070cb57b",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "393d191a-0034-4130-a331-edb9d3156024",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 13 · 2026-05-29T10:07:00.352Z_

<details><summary>↩ Tool result · `toolu_017ue2yKGCq32smXZUsqsRZ1`</summary>

````text
# Comprehensive Summary of "Scaling LLM Inference with Optimized Sample Compute Allocation"

## 1. Introduction & Problem Identification

The paper identifies a critical gap in LLM inference scaling. While prior work optimizes individual sampling configurations (temperature, model, prompt), the authors observe that "not all problems require the same optimal sampling configuration." Their key insight: rather than choosing one configuration, splitting compute budgets across multiple configurations yields better results.

The motivation is empirically demonstrated through Figure 1, where uniform mixed allocation achieves 64% accuracy with 4 samples on LiveCodeBench, while optimal pure allocation requires 16x more samples for comparable performance.

**Prior work limitations cited:**
- Wang et al. (2023b) searched for optimal single configurations but missed cross-configuration benefits
- Existing hyperparameter optimization approaches focus on pure allocations
- Previous scaling studies (AlphaCode, Brown et al. 2024) didn't explore mixed allocation strategies

## 2. Method Section: OSCA Algorithm

### Problem Formulation

The authors formulate sample compute allocation as an optimization problem:

**Inputs:**
- Set of m sampling configurations ℋ = {h₁, h₂, ..., hₘ} (varying temperature, model, language, prompts)
- Training problem set 𝒟_train
- Compute budget C (per problem)
- Estimation budget C₀ (for learning)

**Objective:** Find allocation π: ℋ → ℕ maximizing expected pass@C

### Core Mathematical Formulation

**Step 1: Pass Probability Estimation**

For each configuration hᵢ and problem xⱼ, they estimate:
```
pᵢⱼ ≈ cᵢⱼ / C₀
```
where cᵢⱼ is the count of correct samples from C₀ attempts.

**Step 2: Optimization Problem**

Maximize expected pass@C:
```
max_π E[pass@C] = (1/|𝒟|) Σⱼ(1 - ∏ᵢ(1-pᵢⱼ)^πᵢ)

Subject to:
- 0 ≤ πᵢ ≤ C
- Σᵢ πᵢ = C
- πᵢ ∈ ℕ
```

The key insight: this objective is convex (proof in Appendix A.1), enabling efficient optimization.

### OSCA Algorithm

The algorithm uses **hill climbing** on the relaxed continuous problem:

1. **EstimatePassProb**: Generate C₀ samples per (configuration, problem) pair; compute success frequencies
2. **OptimizeAllocation**: 
   - Initialize random allocation satisfying budget constraint
   - Iteratively test neighboring allocations (differing by moving 1 sample unit between configurations)
   - Climb to better neighbors until convergence
   - Return final allocation π

**Why mixed allocation works:** The paper's example (Section 3.2) demonstrates that for two problems and configurations where h₁ excels on x₁ but h₂ on x₂, mixed allocation achieves 43.8% vs. 37.3% for pure allocation.

## 3. Experiments: Benchmarks & Setup

### Benchmarks

**LiveCodeBench (LCB):**
- 305 training problems (released before 2024)
- 205 test problems (released after 2024)
- LeetCode, Codeforces, AtCoder coding problems
- Configurations: GPT-4o, temperature 0-1.6, Python/C++

**LiveBench (LB):**
- 201 training, 471 test problems
- Four task categories: math, reasoning, language, data analysis
- Configurations: Llama3/Qwen2/DeepSeek, temperature 0-1.8
- C₀ = 50 for estimation across all tasks

**SWE-Bench Lite:**
- 300 real-world software engineering issues
- 150 training, 150 test (random split)
- Configurations: 3 models (GPT-4o, DeepSeek, Qwen), 4 temperatures (0.4-1.6), 2 prompt sets
- C₀ = 16, C = 16 (smaller due to computational cost)

### Baselines

1. **Default pure allocation**: Leaderboard standard (single configuration)
2. **Optimal pure allocation**: Best single configuration on C₀ samples
3. **Uniform mixed allocation**: Equal distribution across all configurations

## 4. Key Numerical Results

### LiveCodeBench Results (Table 2)

| Budget | Default | Optimal Pure | Uniform Mixed | Learned Mixed |
|--------|---------|--------------|---------------|---------------|
| 2¹ | 47.1% | +1.8% | +4.3% | **+17.4%** |
| 2⁴ | 53.9% | +6.6% | +24.4% | **+25.2%** |
| 2⁸ | 59.5% | +8.4% | +27.6% | **+27.2%** |

**Key claim:** Osca achieves optimal pure performance with 128x less compute.

### LiveBench Results

| Budget | Default | Optimal Pure | Uniform Mixed | Learned Mixed |
|--------|---------|--------------|---------------|---------------|
| 2³ | 55.9% | +9.3% | +3.1% | **+11.1%** |
| 2⁵ | 62.6% | +11.2% | +10.5% | **+13.0%** |
| 2⁸ | 68.3% | +14.7% | +12.8% | **+14.7%** |

Note: Uniform mixed underperforms on this heterogeneous benchmark, validating need for optimization.

### SWE-Bench Results

Osca achieves "better accuracy with 3x less compute than default configuration" on the Agentless workflow, demonstrating applicability beyond single-turn tasks.

## 5. Ablation Studies

### Training Data Requirements (Figure 3)
- Full training data yields near-optimal allocations
- Performance degrades at large C values (2⁶+) with reduced training data
- Hypothesis: large budgets require learning on hard problems, prone to overfitting

### Estimation Budget C₀ Sensitivity (Figure 4)
- Even with 26% of original C₀, Osca maintains near-optimal performance
- Algorithm is robust to estimation noise

### Hyperparameter Importance (Figure 5)
- Banning multiple temperatures: performance drops to optimal pure levels
- Banning multiple models: accuracy degrades below optimal pure
- **Conclusion:** Mixed allocation needs diverse configurations to be effective

### Domain Specificity (Table 3)
Testing on LiveBench subtasks separately:
- Math (T1): Osca best in 7/12 cases
- Reasoning (T2): Strong but not dominant
- Language (T3): Consistently strong
- Data Analysis (T4): Competitive

Shows allocations learn domain patterns but aren't perfectly general.

### Instance-Level Learning (Table 4)
k-NN approach at k=64 achieved 86.2% accuracy at 2⁷ budget, while Osca reached 86.7%. Instance-specific allocation proved suboptimal to domain-level allocation.

## 6. Limitations & Conclusion

### Stated Limitations
- Focuses on four hyperparameters (model, temperature, language, prompt); doesn't explore top-k, top-p, repetition penalty
- Maximum compute budget tested: 512 samples
- Computationally expensive for very large problem sets

### Conclusion

The paper establishes that "mixed allocation of sample budgets is necessary" for efficient LLM scaling. Osca demonstrates significant compute savings: **128x fewer samples on code generation, 25x on reasoning tasks**. The method's applicability to agentic workflows (SWE-Bench) suggests broader utility beyond single-turn inference. The convex optimization foundation provides theoretical justification for the hill-climbing approach.

---

**Code and generations:** Released at https://github.com/LeiLiLab/OSCA
````

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "58a0f938-c8e0-47b3-8420-3b5a6fd5a1fb",
  "isSidechain": true,
  "promptId": "295c0657-e121-425c-967b-f63279f1549e",
  "agentId": "a5512f66970097acf",
  "type": "user",
  "uuid": "9fe4ed62-05a7-4cf8-be1c-99f0cca04631",
  "sourceToolAssistantUUID": "58a0f938-c8e0-47b3-8420-3b5a6fd5a1fb",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "393d191a-0034-4130-a331-edb9d3156024",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 14 · 2026-05-29T10:07:05.457Z_

Good, I have the abstract and full paper content. Let me now try to fetch the ACL Anthology page for any additional info, the Moonlight review page, and search for OpenReview comments specifically.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9fe4ed62-05a7-4cf8-be1c-99f0cca04631",
  "isSidechain": true,
  "agentId": "a5512f66970097acf",
  "requestId": "req_011CbWg4P7FWZXms5dfV8Gi9",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "6a4a5610-3dba-4eac-af66-85b0cf14258c",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "393d191a-0034-4130-a331-edb9d3156024",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VdEEctJ9WmYhUmvdH6MGt1",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 658,
      "cache_creation_input_tokens": 2799,
      "cache_read_input_tokens": 10232,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2799,
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

_source line 15 · 2026-05-29T10:07:07.344Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01GWg6VJDboTzrzb4nhFAwAa`</summary>

```json
{
  "url": "https://www.themoonlight.io/en/review/scaling-llm-inference-with-optimized-sample-compute-allocation",
  "prompt": "Extract all reviewer comments, reviews, criticisms, praise, scores, and detailed feedback about this paper. Include any specific strengths, weaknesses, questions raised by reviewers, and overall recommendations."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6a4a5610-3dba-4eac-af66-85b0cf14258c",
  "isSidechain": true,
  "agentId": "a5512f66970097acf",
  "requestId": "req_011CbWg4P7FWZXms5dfV8Gi9",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "4a3ede82-4321-486d-8dc5-eb0bb9a4b207",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "393d191a-0034-4130-a331-edb9d3156024",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VdEEctJ9WmYhUmvdH6MGt1",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 658,
      "cache_creation_input_tokens": 2799,
      "cache_read_input_tokens": 10232,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2799,
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

_source line 16 · 2026-05-29T10:07:08.401Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_0154tTL2NWVqd3zGRLjNQVGM`</summary>

```json
{
  "url": "https://aclanthology.org/2025.naacl-long.404/",
  "prompt": "Extract all metadata about this paper: authors, venue, pages, DOI, citation count, any linked resources, and any reviewer or editorial information available."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4a3ede82-4321-486d-8dc5-eb0bb9a4b207",
  "isSidechain": true,
  "agentId": "a5512f66970097acf",
  "requestId": "req_011CbWg4P7FWZXms5dfV8Gi9",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "3562ee3b-10e2-418b-9826-f2350ef61580",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "393d191a-0034-4130-a331-edb9d3156024",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VdEEctJ9WmYhUmvdH6MGt1",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 658,
      "cache_creation_input_tokens": 2799,
      "cache_read_input_tokens": 10232,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2799,
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

_source line 17 · 2026-05-29T10:07:08.960Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_0141PTzwQ4kUNeb3YCFGzUcz`</summary>

```json
{
  "query": "\"Scaling LLM Inference\" \"Optimized Sample Compute Allocation\" reviewer feedback strengths weaknesses OpenReview 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3562ee3b-10e2-418b-9826-f2350ef61580",
  "isSidechain": true,
  "agentId": "a5512f66970097acf",
  "requestId": "req_011CbWg4P7FWZXms5dfV8Gi9",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "e062c84f-7259-4402-826a-e7633d7edb29",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "393d191a-0034-4130-a331-edb9d3156024",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VdEEctJ9WmYhUmvdH6MGt1",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 658,
      "cache_creation_input_tokens": 2799,
      "cache_read_input_tokens": 10232,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2799,
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

_source line 18 · 2026-05-29T10:07:11.212Z_

<details><summary>↩ Tool result · `toolu_01GWg6VJDboTzrzb4nhFAwAa`</summary>

```text
# Reviewer Comments and Feedback Analysis

Based on the provided web page content, **no reviewer comments, reviews, criticisms, praise, scores, or detailed feedback about this paper are present**.

The page contains a literature review summary of "Scaling LLM Inference with Optimized Sample Compute Allocation" by Kexun Zhang et al., including sections on introduction, methodology, evaluations, and conclusions. However, it does not include:

- Peer reviewer comments or critiques
- Numerical scores or ratings
- Strengths and weaknesses assessments from reviewers
- Questions raised during review processes
- Specific recommendations from the review community
- Any formal review feedback

The content appears to be a **descriptive summary generated by Moonlight** (an AI research tool) rather than a peer-reviewed publication page with accompanying reviewer feedback. To locate actual reviewer comments, one would need to access the paper through academic venues such as conference proceedings, journal publications, or preprint servers that display peer review information.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "4a3ede82-4321-486d-8dc5-eb0bb9a4b207",
  "isSidechain": true,
  "promptId": "295c0657-e121-425c-967b-f63279f1549e",
  "agentId": "a5512f66970097acf",
  "type": "user",
  "uuid": "b1db42cc-f278-491b-b579-9eafc078f570",
  "sourceToolAssistantUUID": "4a3ede82-4321-486d-8dc5-eb0bb9a4b207",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "393d191a-0034-4130-a331-edb9d3156024",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 19 · 2026-05-29T10:07:12.899Z_

<details><summary>↩ Tool result · `toolu_0154tTL2NWVqd3zGRLjNQVGM`</summary>

```text
# Paper Metadata Extraction

## Core Information
**Title:** Scaling LLM Inference Efficiently with Optimized Sample Compute Allocation

**Authors:** Kexun Zhang, Shang Zhou, Danqing Wang, William Yang Wang, Lei Li

**Venue:** NAACL 2025 (Nations of the Americas Chapter of the Association for Computational Linguistics)

**Conference Details:**
- Location: Albuquerque, New Mexico
- Month: April 2025
- Volume: Proceedings of the 2025 NAACL Conference (Volume 1: Long Papers)

## Publication Details
**Pages:** 7959–7973

**DOI:** 10.18653/v1/2025.naacl-long.404

**Anthology ID:** 2025.naacl-long.404

**Bibkey:** zhang-etal-2025-scaling

**PDF URL:** https://aclanthology.org/2025.naacl-long.404.pdf

## Editors
Luis Chiruzzo, Alan Ritter, Lu Wang

## Publisher
Association for Computational Linguistics

## ISBN
979-8-89176-189-6

## Additional Resources
**Code Repository:** https://github.com/LeiLiLab/OSCA

## Note on Availability
Citation count information is not provided on this ACL Anthology page. The document appears to be a recent conference paper with no reviewer comments or editorial notes displayed.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "3562ee3b-10e2-418b-9826-f2350ef61580",
  "isSidechain": true,
  "promptId": "295c0657-e121-425c-967b-f63279f1549e",
  "agentId": "a5512f66970097acf",
  "type": "user",
  "uuid": "add090db-f455-4552-8e12-cdef35d1a395",
  "sourceToolAssistantUUID": "3562ee3b-10e2-418b-9826-f2350ef61580",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "393d191a-0034-4130-a331-edb9d3156024",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-29T10:07:13.758Z_

<details><summary>↩ Tool result · `toolu_0141PTzwQ4kUNeb3YCFGzUcz`</summary>

```text
Web search results for query: ""Scaling LLM Inference" "Optimized Sample Compute Allocation" reviewer feedback strengths weaknesses OpenReview 2025"

Links: [{"title":"Scaling LLM Inference with Optimized Sample Compute Allocation","url":"https://arxiv.org/pdf/2410.22480"},{"title":"Scaling LLM Inference with Optimized Sample Compute Allocation","url":"https://arxiv.org/html/2410.22480v1"},{"title":"Paper page - Scaling LLM Inference with Optimized Sample Compute Allocation","url":"https://huggingface.co/papers/2410.22480"},{"title":"[Literature Review] Scaling LLM Inference with Optimized Sample Compute Allocation","url":"https://www.themoonlight.io/en/review/scaling-llm-inference-with-optimized-sample-compute-allocation"},{"title":"[2410.22480] Scaling LLM Inference with Optimized Sample Compute Allocation","url":"https://arxiv.org/abs/2410.22480"},{"title":"Scaling LLM Inference Efficiently with Optimized Sample Compute Allocation - ACL Anthology","url":"https://aclanthology.org/2025.naacl-long.404/"}]

I found the paper "Scaling LLM Inference with Optimized Sample Compute Allocation" by Zhang et al., which was accepted to NAACL 2025. However, the search results don't contain OpenReview 2025 reviewer feedback with specific strengths and weaknesses. 

The paper presents OSCA, an algorithm that Optimizes Sample Compute Allocation by finding an optimal mix of different inference configurations. The experiments show that with their learned mixed allocation, they can achieve accuracy better than the best single configuration with 128x less compute on code generation and 25x less compute on 4 reasoning tasks. Additionally, OSCA is shown to be effective in agentic workflows beyond single-turn tasks, achieving a better accuracy on SWE-Bench with 3x less compute than the default configuration.

The paper was published on arXiv on October 29, 2024, and has been accepted to the 2025 Conference of the Nations of the Americas Chapter of the Association for Computational Linguistics (NAACL 2025). However, the search results don't include the specific OpenReview reviewer feedback on strengths and weaknesses. To access those detailed reviews, you would need to visit the paper's OpenReview page directly at openreview.net.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "e062c84f-7259-4402-826a-e7633d7edb29",
  "isSidechain": true,
  "promptId": "295c0657-e121-425c-967b-f63279f1549e",
  "agentId": "a5512f66970097acf",
  "type": "user",
  "uuid": "af6c6984-7227-48a6-88c3-e0fc92a5d084",
  "sourceToolAssistantUUID": "e062c84f-7259-4402-826a-e7633d7edb29",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "393d191a-0034-4130-a331-edb9d3156024",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 21 · 2026-05-29T10:07:16.629Z_

Let me try to find the OpenReview page directly and also check the HuggingFace paper page for community discussion.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "af6c6984-7227-48a6-88c3-e0fc92a5d084",
  "isSidechain": true,
  "agentId": "a5512f66970097acf",
  "requestId": "req_011CbWg5N3Xyk4wWZrHesTg5",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "5ed6cc3c-c530-4fc8-8e58-de5188140e4e",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "393d191a-0034-4130-a331-edb9d3156024",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RMLhqeVehJbZGeZ7kDUyee",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2359,
      "cache_read_input_tokens": 13031,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2359,
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

_source line 22 · 2026-05-29T10:07:17.116Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01BMxztp5ejvsSavKVZqJTTK`</summary>

```json
{
  "query": "site:openreview.net \"Optimized Sample Compute Allocation\" OR \"OSCA\" Zhang 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5ed6cc3c-c530-4fc8-8e58-de5188140e4e",
  "isSidechain": true,
  "agentId": "a5512f66970097acf",
  "requestId": "req_011CbWg5N3Xyk4wWZrHesTg5",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "b19d2a57-4723-458e-9ca3-1657f401ee38",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "393d191a-0034-4130-a331-edb9d3156024",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RMLhqeVehJbZGeZ7kDUyee",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2359,
      "cache_read_input_tokens": 13031,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2359,
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

_source line 23 · 2026-05-29T10:07:18.107Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_012QWTugmBMzSHmjdci8BRvq`</summary>

```json
{
  "url": "https://huggingface.co/papers/2410.22480",
  "prompt": "Extract all community comments, discussions, upvotes, criticisms, and any feedback about this paper. Include any specific points of praise or criticism from the community."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b19d2a57-4723-458e-9ca3-1657f401ee38",
  "isSidechain": true,
  "agentId": "a5512f66970097acf",
  "requestId": "req_011CbWg5N3Xyk4wWZrHesTg5",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "8f298da1-a795-46d7-b41e-60f92a376706",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "393d191a-0034-4130-a331-edb9d3156024",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RMLhqeVehJbZGeZ7kDUyee",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2359,
      "cache_read_input_tokens": 13031,
      "output_tokens": 205,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2359
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 205,
          "cache_read_input_tokens": 13031,
          "cache_creation_input_tokens": 2359,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2359,
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

_source line 24 · 2026-05-29T10:07:18.773Z_

<details><summary>↩ Tool result · `toolu_012QWTugmBMzSHmjdci8BRvq`</summary>

```text
&lt;persisted-output>
Output too large (69.2KB). Full output saved to: /home/ubuntu/.claude-account-2/projects/-home-ubuntu-idea-adversarial/393d191a-0034-4130-a331-edb9d3156024/tool-results/toolu_012QWTugmBMzSHmjdci8BRvq.txt

Preview (first 2KB):
Title: Scaling LLM Inference with Optimized Sample Compute Allocation

URL Source: https://arxiv.org/html/2410.22480

Markdown Content:
Kexun Zhang 1, Shang Zhou 2∗, Danqing Wang 1, William Yang Wang 3, Lei Li 1
1 Carnegie Mellon University, 2 UC San Diego, 3 UC Santa Barbara

###### Abstract

Sampling is a basic operation in many inference-time algorithms of large language models (LLMs). To scale up inference efficiently with a limited compute, it is crucial to find an optimal allocation for sample compute budgets: Which sampling configurations (model, temperature, language, etc.) do we use? How many samples do we generate in each configuration? We formulate these choices as a learning problem and propose Osca, an algorithm that O ptimizes S ample C ompute A llocation by finding an optimal mix of different inference configurations. Our experiments show that with our learned mixed allocation, we can achieve accuracy better than the best single configuration with 128x less compute on code generation and 25x less compute on 4 reasoning tasks. Osca is also shown to be effective in agentic workflows beyond single-turn tasks, achieving a better accuracy on SWE-Bench with 3x less compute than the default configuration. Our code and generations are released at [https://github.com/LeiLiLab/OSCA](https://github.com/LeiLiLab/OSCA).

Scaling LLM Inference with Optimized Sample Compute Allocation

Kexun Zhang 1††thanks: Equal contribution. Correspondence to kexun@cmu.edu., Shang Zhou 2∗, Danqing Wang 1, William Yang Wang 3, Lei Li 1 1 Carnegie Mellon University, 2 UC San Diego, 3 UC Santa Barbara

1 Introduction
--------------

...
&lt;/persisted-output>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "8f298da1-a795-46d7-b41e-60f92a376706",
  "isSidechain": true,
  "promptId": "295c0657-e121-425c-967b-f63279f1549e",
  "agentId": "a5512f66970097acf",
  "type": "user",
  "uuid": "8a3c8d82-2888-4188-b25a-5b8aed9bae8f",
  "sourceToolAssistantUUID": "8f298da1-a795-46d7-b41e-60f92a376706",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "393d191a-0034-4130-a331-edb9d3156024",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 25 · 2026-05-29T10:07:27.315Z_

<details><summary>↩ Tool result · `toolu_01BMxztp5ejvsSavKVZqJTTK`</summary>

```text
Web search results for query: "site:openreview.net "Optimized Sample Compute Allocation" OR "OSCA" Zhang 2025"

Links: [{"title":"Scaling LLM Inference Efficiently with Optimized Sample Compute Allocation - ACL Anthology","url":"https://aclanthology.org/2025.naacl-long.404/"},{"title":"Scaling LLM Inference with Optimized Sample Compute Allocation","url":"https://arxiv.org/pdf/2410.22480"},{"title":"[2410.22480] Scaling LLM Inference with Optimized Sample Compute Allocation","url":"https://arxiv.org/abs/2410.22480"},{"title":"[Literature Review] Scaling LLM Inference with Optimized Sample Compute Allocation","url":"https://www.themoonlight.io/en/review/scaling-llm-inference-with-optimized-sample-compute-allocation"},{"title":"Scaling LLM Inference Efficiently with Optimized Sample Compute Allocation | Request PDF","url":"https://www.researchgate.net/publication/392505821_Scaling_LLM_Inference_Efficiently_with_Optimized_Sample_Compute_Allocation"},{"title":"Bring Future Vision: Dynamic Computation Allocation Guided by Lightweight Feature Forecaster | OpenReview","url":"https://openreview.net/forum?id=wPemGNb66V"},{"title":"Published as a conference paper at ICLR 2026","url":"https://openreview.net/pdf?id=2i6Rp0gCq6"}]

Based on the search results, I found information about the OSCA paper by Zhang et al. However, the results show that this work was published at NAACL 2025 (and is also available on arXiv), rather than on OpenReview specifically.

The paper "Scaling LLM Inference Efficiently with Optimized Sample Compute Allocation" proposes OSCA, an algorithm that Optimizes Sample Compute Allocation by finding an optimal mix of different inference configurations. The paper demonstrates that with their learned mixed allocation, they can achieve accuracy better than the best single configuration with 128x less compute on code generation and 25x less compute on 4 reasoning tasks. OSCA is also shown to be effective in agentic workflows beyond single-turn tasks, achieving a better accuracy on SWE-Bench with 3x less compute than the default configuration.

The paper appears to have been published as a conference paper at NAACL 2025 rather than being hosted on OpenReview's main submission platform, though it may be referenced there in some contexts.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "b19d2a57-4723-458e-9ca3-1657f401ee38",
  "isSidechain": true,
  "promptId": "295c0657-e121-425c-967b-f63279f1549e",
  "agentId": "a5512f66970097acf",
  "type": "user",
  "uuid": "332a15f9-e3cd-4817-91e1-c4261b7b4a9b",
  "sourceToolAssistantUUID": "b19d2a57-4723-458e-9ca3-1657f401ee38",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "393d191a-0034-4130-a331-edb9d3156024",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 26 · 2026-05-29T10:07:30.566Z_

The HuggingFace page returned the full paper HTML. Let me read the persisted output for additional details, and also try to find the NAACL 2025 OpenReview page directly.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "332a15f9-e3cd-4817-91e1-c4261b7b4a9b",
  "isSidechain": true,
  "agentId": "a5512f66970097acf",
  "requestId": "req_011CbWg6N2a9jwVN2S7p3Zws",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "f77d4e20-7983-4aa3-8906-efa6ac16e631",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "393d191a-0034-4130-a331-edb9d3156024",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01X6xHzaUSQCEwxqLxX5bvSd",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 585,
      "cache_creation_input_tokens": 885,
      "cache_read_input_tokens": 15390,
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

_source line 27 · 2026-05-29T10:07:31.555Z_

<details open><summary>🔧 Tool call — Read · `toolu_01Rq4WZqfZoU6ayN59q56zto`</summary>

```json
{
  "file_path": "/home/ubuntu/.claude-account-2/projects/-home-ubuntu-idea-adversarial/393d191a-0034-4130-a331-edb9d3156024/tool-results/toolu_012QWTugmBMzSHmjdci8BRvq.txt",
  "limit": 200
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f77d4e20-7983-4aa3-8906-efa6ac16e631",
  "isSidechain": true,
  "agentId": "a5512f66970097acf",
  "requestId": "req_011CbWg6N2a9jwVN2S7p3Zws",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "cc4e00cc-906d-468c-96fc-e8c5315469c2",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "393d191a-0034-4130-a331-edb9d3156024",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01X6xHzaUSQCEwxqLxX5bvSd",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 585,
      "cache_creation_input_tokens": 885,
      "cache_read_input_tokens": 15390,
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

_source line 28 · 2026-05-29T10:07:31.834Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01RYpTfHEDWmnPXUTVyX35sj`</summary>

```json
{
  "query": "openreview.net NAACL 2025 \"Scaling LLM Inference\" \"sample compute allocation\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "cc4e00cc-906d-468c-96fc-e8c5315469c2",
  "isSidechain": true,
  "agentId": "a5512f66970097acf",
  "requestId": "req_011CbWg6N2a9jwVN2S7p3Zws",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "05e9cf58-0039-4c27-9534-7b1f87149770",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "393d191a-0034-4130-a331-edb9d3156024",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01X6xHzaUSQCEwxqLxX5bvSd",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 585,
      "cache_creation_input_tokens": 885,
      "cache_read_input_tokens": 15390,
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

### Tool result

_source line 29 · 2026-05-29T10:07:31.867Z_

<details><summary>↩ Tool result · `toolu_01Rq4WZqfZoU6ayN59q56zto`</summary>

```text
1	Title: Scaling LLM Inference with Optimized Sample Compute Allocation
2	
3	URL Source: https://arxiv.org/html/2410.22480
4	
5	Markdown Content:
6	Kexun Zhang 1, Shang Zhou 2∗, Danqing Wang 1, William Yang Wang 3, Lei Li 1
7	1 Carnegie Mellon University, 2 UC San Diego, 3 UC Santa Barbara
8	
9	###### Abstract
10	
11	Sampling is a basic operation in many inference-time algorithms of large language models (LLMs). To scale up inference efficiently with a limited compute, it is crucial to find an optimal allocation for sample compute budgets: Which sampling configurations (model, temperature, language, etc.) do we use? How many samples do we generate in each configuration? We formulate these choices as a learning problem and propose Osca, an algorithm that O ptimizes S ample C ompute A llocation by finding an optimal mix of different inference configurations. Our experiments show that with our learned mixed allocation, we can achieve accuracy better than the best single configuration with 128x less compute on code generation and 25x less compute on 4 reasoning tasks. Osca is also shown to be effective in agentic workflows beyond single-turn tasks, achieving a better accuracy on SWE-Bench with 3x less compute than the default configuration. Our code and generations are released at [https://github.com/LeiLiLab/OSCA](https://github.com/LeiLiLab/OSCA).
12	
13	Scaling LLM Inference with Optimized Sample Compute Allocation
14	
15	Kexun Zhang 1††thanks: Equal contribution. Correspondence to kexun@cmu.edu., Shang Zhou 2∗, Danqing Wang 1, William Yang Wang 3, Lei Li 1 1 Carnegie Mellon University, 2 UC San Diego, 3 UC Santa Barbara
16	
17	1 Introduction
18	--------------
19	
20	Large language models (LLMs) solve more problems with more inference compute. Different ways of scaling up LLM inference include sampling (Chen et al., [2021](https://arxiv.org/html/2410.22480v1#bib.bib3)), self-consistency (Wang et al., [2023c](https://arxiv.org/html/2410.22480v1#bib.bib26)), tree search (Yao et al., [2024](https://arxiv.org/html/2410.22480v1#bib.bib31)), and multi-agent systems (Du et al., [2023](https://arxiv.org/html/2410.22480v1#bib.bib8)), etc. Among these, sampling is the most basic and serves as an atomic operation needed in all other more complicated methods. Therefore, it is crucial to do it well.
21	
22	![Image 1: Refer to caption](https://arxiv.org/html/2410.22480v1/x1.png)
23	
24	![Image 2: Refer to caption](https://arxiv.org/html/2410.22480v1/x2.png)
25	
26	![Image 3: Refer to caption](https://arxiv.org/html/2410.22480v1/x3.png)
27	
28	Figure 1: On 2 single-turn benchmarks and 1 agentic benchmark with a total of 6 tasks, our optimized allocations of sample compute are better than both optimal pure allocations and uniform allocations in most cases, especially when the compute budget is small.
29	
30	Previous studies (Wang et al., [2023b](https://arxiv.org/html/2410.22480v1#bib.bib24)) have investigated how to find the optimal sampling configuration, such as the best temperature, model, and prompt. While these methods are effective, they miss one key fact: Not all problems require the same optimal sampling configuration. Some problems are easier solved with higher temperatures while others with lower temperatures (Li et al., [2022](https://arxiv.org/html/2410.22480v1#bib.bib16)). In this case, the best way to use a limited compute budget is not to choose between high or low temperatures, but to split the budget between both. This highlights the need for a mixed allocation of the sample budget instead of a pure allocation that uses a single configuration.
31	
32	As shown in [Figure 1](https://arxiv.org/html/2410.22480v1#S1.F1 "Figure 1 ‣ 1 Introduction ‣ Scaling LLM Inference with Optimized Sample Compute Allocation"), just by uniformly allocating the compute budget over all possible inference configurations (dubbed “uniform mixed”), LLMs’ accuracy can already surpass the optimal pure allocation on LiveCodeBench. Uniform mixed allocation gets 64% accuracy with 4 samples, while optimal pure needs 16x more samples to get a similar accuracy. Since uniform allocation is only one of the exponentially many allocations in the search space, it is natural to ask: How do we find the optimal sample budget allocation for LLM inference?
33	
34	We formulate this as a learning problem: given a set of different inference configurations, a training problem set, and a compute budget, we need to distribute the budget over different configurations such that the expected accuracy is maximized. To solve this problem, we propose a hill-climbing algorithm and demonstrate its effectiveness with both theoretical justification and experiments. As shown in [Figure 1](https://arxiv.org/html/2410.22480v1#S1.F1 "Figure 1 ‣ 1 Introduction ‣ Scaling LLM Inference with Optimized Sample Compute Allocation"), the learned allocation from Osca is significantly better than the optimal pure allocation, especially when the sample size is small.
35	
36	To provide further insights for future adopters of Osca, we conduct ablation studies on the effectiveness of different hyperparameters in the mix, the number of problems needed in the training set, and scenarios where mixed allocations do not offer significant improvements. Moreover, we show on SWE-Bench, a benchmark for LLM agents, that replacing pure sampling with Osca’s learned allocation in just one step boosts the entire workflow’s performance. This demonstrates that a mixed sampling strategy not only improves single-turn tasks but also enhances complex inference algorithms, leading to better reasoning and decision-making.
37	
38	Our contributions are the following:
39	
40	*   •
41	We highlight the need for mixed allocation of LLM sample compute and formulate it as a learning problem.
42	
43	*   •
44	We propose an effective algorithm Osca for optimizing sample compute allocations and demonstrate its effectiveness on 3 benchmarks consisting of 6 LLM tasks.
45	
46	*   •
47	We provide detailed analyses of when and why mixed allocations work, as well as their role in more complicated inference time algorithms.
48	
49	2 Related Work
50	--------------
51	
52	Inference Time Algorithms. Following the taxonomy of Welleck et al. ([2024](https://arxiv.org/html/2410.22480v1#bib.bib27)) on inference-time algorithms, chained meta-generators run multiple LLM calls sequentially and use the output sample from each call as the input to the next one (Dohan et al., [2022](https://arxiv.org/html/2410.22480v1#bib.bib7); Schlag et al., [2023](https://arxiv.org/html/2410.22480v1#bib.bib19)). Parallel meta-generators samples multiple candidates for a problem and selects the best candidate (Wang et al., [2023c](https://arxiv.org/html/2410.22480v1#bib.bib26); Chen et al., [2022](https://arxiv.org/html/2410.22480v1#bib.bib2); Jiang et al., [2023](https://arxiv.org/html/2410.22480v1#bib.bib12); Zhang et al., [2023](https://arxiv.org/html/2410.22480v1#bib.bib32); Huang et al., [2023](https://arxiv.org/html/2410.22480v1#bib.bib10)). Step-level search methods regards problem-solving as a multi-step process and sample candidate next steps at each intermediate state, using algorithms like tree search (Yao et al., [2024](https://arxiv.org/html/2410.22480v1#bib.bib31)), graph search, and Monte-Carlo Tree Search (Lample et al., [2022](https://arxiv.org/html/2410.22480v1#bib.bib14); Tian et al., [2024](https://arxiv.org/html/2410.22480v1#bib.bib22); Chi et al., [2024](https://arxiv.org/html/2410.22480v1#bib.bib4)). Refinement-based methods samples candidate solutions sequentially, relying on some feedback to revise the next candidate (Madaan et al., [2024](https://arxiv.org/html/2410.22480v1#bib.bib17); Shinn et al., [2024](https://arxiv.org/html/2410.22480v1#bib.bib20)). Although these algorithms scale up inference differently, they all need LLM sampling as a basic operation.
53	
54	Scaling Inference. Many studies investigate how scaling in inference affects LLM performance. AlphaCode(Li et al., [2022](https://arxiv.org/html/2410.22480v1#bib.bib16); Leblond et al., [2023](https://arxiv.org/html/2410.22480v1#bib.bib15)) scales up the sample number and finds the solve rates scale log-linearly with more samples. Brown et al. ([2024](https://arxiv.org/html/2410.22480v1#bib.bib1)) improves LLMs’ performance on math problems by repetitively sampling candidate solutions with a high temperature. Wu et al. ([2024](https://arxiv.org/html/2410.22480v1#bib.bib29)) and Snell et al. ([2024](https://arxiv.org/html/2410.22480v1#bib.bib21)) study the scaling behaviors of various inference time algorithms, reward models, and the model sizes. In this paper, we investigate the allocation algorithm between various inference configurations for scaling up inference.
55	
56	Inference Compute Optimization. There are two typical ways to optimize inference compute. One is to search for a single optimal configuration. For example, Wang et al. ([2023a](https://arxiv.org/html/2410.22480v1#bib.bib23)) proposes EcoOptiGen to optimize the inference hyperparameter under a limited compute budget, and Wang et al. ([2024](https://arxiv.org/html/2410.22480v1#bib.bib25)) finetunes LLMs to self-regularize its generation with the best hyperparameter set. The other is to find the optimal allocation between various inference configurations(Graves, [2016](https://arxiv.org/html/2410.22480v1#bib.bib9); Dehghani et al., [2019](https://arxiv.org/html/2410.22480v1#bib.bib6)). Damani et al. ([2024](https://arxiv.org/html/2410.22480v1#bib.bib5)) allocates the compute budget based on the estimation of problem difficulty. Here, we optimize the compute allocation to different inference configurations.
57	
58	![Image 4: Refer to caption](https://arxiv.org/html/2410.22480v1/x4.png)
59	
60	Figure 2: With 4 sampling configurations and a compute budget of 1, pure allocation spends all the budget on one configuration. Uniform allocation evenly distributes the budget across configurations. Optimized allocation learns where to spend more budget.
61	
62	3 Method
63	--------
64	
65	### 3.1 Problem: Sample Compute Allocation
66	
67	LLM Problem-Solving. We study how to improve LLM-based solvers for problems with binary correctness values. Formally, a problem is a pair (x,v)𝑥 𝑣(x,v)( italic_x , italic_v ), where x∈𝒳 𝑥 𝒳 x\in\mathcal{X}italic_x ∈ caligraphic_X is the problem specifications, v:𝒳×𝒴→{True,False}:𝑣→𝒳 𝒴 True False v:\mathcal{X}\times\mathcal{Y}\rightarrow\{\texttt{True},\texttt{False}\}italic_v : caligraphic_X × caligraphic_Y → { True , False } is the verifier that maps a solution of the problem to a truth value, and 𝒴 𝒴\mathcal{Y}caligraphic_Y is the space of solutions. An LLM solver is given the problem specification and produces a distribution Pr LM⁡(y|x)subscript Pr LM conditional 𝑦 𝑥\Pr_{\text{LM}}(y|x)roman_Pr start_POSTSUBSCRIPT LM end_POSTSUBSCRIPT ( italic_y | italic_x ) over the solution space conditioned on the problem specification.
68	
69	Compute Budget and pass@C 𝐶 C italic_C. We evaluate LLM-based problem solvers with the average solve rate of test set problems given a fixed compute budget C 𝐶 C italic_C, which can be defined as the maximum number of samples, the maximum number of tokens, the maximum FLOPs, etc. For any definition of compute budget C 𝐶 C italic_C, we generate as many samples as possible from Pr LM⁡(y|x)subscript Pr LM conditional 𝑦 𝑥\Pr_{\text{LM}}(y|x)roman_Pr start_POSTSUBSCRIPT LM end_POSTSUBSCRIPT ( italic_y | italic_x ) within the compute limit. The solver can be evaluated using pass@C C C italic_C, which is defined as the probability of at least one sample among the candidates being correct. In our experiments, we use the number of samples as a metric for C 𝐶 C italic_C.
70	
71	Sampling Configurations. Given a problem specification x 𝑥 x italic_x, there are multiple inference hyperparameters to decide when solving it with an LLM – the model to use, inference temperature, language of the output, prompt, etc. For the i 𝑖 i italic_i-th hyperparameter, we use H i subscript 𝐻 𝑖 H_{i}italic_H start_POSTSUBSCRIPT italic_i end_POSTSUBSCRIPT to denote the set of feasible values and h i subscript ℎ 𝑖 h_{i}italic_h start_POSTSUBSCRIPT italic_i end_POSTSUBSCRIPT to denote an element in H i subscript 𝐻 𝑖 H_{i}italic_H start_POSTSUBSCRIPT italic_i end_POSTSUBSCRIPT that is actually chosen. Assuming the number of tunable hyperparameters is d 𝑑 d italic_d, we call an d 𝑑 d italic_d-tuple 𝒉=(h 1,h 2,⋯,h d)∈ℋ=H 1×H 2×⋯×H d 𝒉 subscript ℎ 1 subscript ℎ 2⋯subscript ℎ 𝑑 ℋ subscript 𝐻 1 subscript 𝐻 2⋯subscript 𝐻 𝑑\bm{h}=(h_{1},h_{2},\cdots,h_{d})\in\mathcal{H}=H_{1}\times H_{2}\times\cdots% \times H_{d}bold_italic_h = ( italic_h start_POSTSUBSCRIPT 1 end_POSTSUBSCRIPT , italic_h start_POSTSUBSCRIPT 2 end_POSTSUBSCRIPT , ⋯ , italic_h start_POSTSUBSCRIPT italic_d end_POSTSUBSCRIPT ) ∈ caligraphic_H = italic_H start_POSTSUBSCRIPT 1 end_POSTSUBSCRIPT × italic_H start_POSTSUBSCRIPT 2 end_POSTSUBSCRIPT × ⋯ × italic_H start_POSTSUBSCRIPT italic_d end_POSTSUBSCRIPT a sampling configuration.
72	
73	Sample Compute Allocation. Suppose there are |ℋ|=m ℋ 𝑚|\mathcal{H}|=m| caligraphic_H | = italic_m sampling configurations, and we want to allocate a compute budget C 𝐶 C italic_C across them. We define an allocation as a mapping function π:ℋ→ℕ:𝜋→ℋ ℕ\pi:\mathcal{H}\rightarrow\mathbb{N}italic_π : caligraphic_H → blackboard_N to represent the amount of compute assigned to each sampling configuration and it should satisfy ∑𝒉∈ℋ π⁢(𝒉)=C subscript 𝒉 ℋ 𝜋 𝒉 𝐶\sum_{\bm{h}\in\mathcal{H}}\pi(\bm{h})=C∑ start_POSTSUBSCRIPT bold_italic_h ∈ caligraphic_H end_POSTSUBSCRIPT italic_π ( bold_italic_h ) = italic_C. For convenience we use π i subscript 𝜋 𝑖\pi_{i}italic_π start_POSTSUBSCRIPT italic_i end_POSTSUBSCRIPT to denote π⁢(𝒉 i)𝜋 subscript 𝒉 𝑖\pi(\bm{h}_{i})italic_π ( bold_italic_h start_POSTSUBSCRIPT italic_i end_POSTSUBSCRIPT ). We categorize sample budget allocations into two types: A pure allocation spends all the compute on one sampling configuration, i.e., there exists exactly one i 𝑖 i italic_i for which π i>0 subscript 𝜋 𝑖 0\pi_{i}>0 italic_π start_POSTSUBSCRIPT italic_i end_POSTSUBSCRIPT > 0; while a mixed allocation spends compute on more than one sampling configurations. Examples of different types of allocations can be found in Figure [2](https://arxiv.org/html/2410.22480v1#S2.F2 "Figure 2 ‣ 2 Related Work ‣ Scaling LLM Inference with Optimized Sample Compute Allocation").
74	
75	Learning Allocations. We want to find for a test set of problems 𝒟 test subscript 𝒟 test\mathcal{D}_{\text{test}}caligraphic_D start_POSTSUBSCRIPT test end_POSTSUBSCRIPT and a given per-problem compute budget C 𝐶 C italic_C, a sample compute allocation π 𝜋\pi italic_π, such that the problem solve-rate pass@C 𝐶 C italic_C can be maximized given the same amount of compute. We assume access to an i.i.d. training problem set 𝒟 train subscript 𝒟 train\mathcal{D}_{\text{train}}caligraphic_D start_POSTSUBSCRIPT train end_POSTSUBSCRIPT and a per-problem allocation-learning compute budget C 0 subscript 𝐶 0 C_{0}italic_C start_POSTSUBSCRIPT 0 end_POSTSUBSCRIPT that can be used for trying out different sampling configurations.
76	
77	### 3.2 Why Mixed Allocation?
78	
79	We show an example that demonstrates why it is sometimes necessary to use a mixed allocation of sample compute. Consider two problems x 1 subscript 𝑥 1 x_{1}italic_x start_POSTSUBSCRIPT 1 end_POSTSUBSCRIPT and x 2 subscript 𝑥 2 x_{2}italic_x start_POSTSUBSCRIPT 2 end_POSTSUBSCRIPT, and two configurations 𝒉 1 subscript 𝒉 1\bm{h}_{1}bold_italic_h start_POSTSUBSCRIPT 1 end_POSTSUBSCRIPT and 𝒉 2 subscript 𝒉 2\bm{h}_{2}bold_italic_h start_POSTSUBSCRIPT 2 end_POSTSUBSCRIPT. We use Pr⁡(pass|𝒉,x)Pr conditional pass 𝒉 𝑥\Pr(\text{pass}|\bm{h},x)roman_Pr ( pass | bold_italic_h , italic_x ) to denote the probability of generating a correct solution to the problem x 𝑥 x italic_x under configuration 𝒉 𝒉\bm{h}bold_italic_h. Let’s assume that Pr⁡(pass|𝒉 𝟏,x 1)=10%,Pr⁡(pass|𝒉 𝟐,x 1)=1%,Pr⁡(pass|𝒉 𝟏,x 2)=1%,Pr⁡(pass|𝒉 𝟐,x 2)=10%formulae-sequence Pr conditional pass subscript 𝒉 1 subscript 𝑥 1 percent 10 formulae-sequence Pr conditional pass subscript 𝒉 2 subscript 𝑥 1 percent 1 formulae-sequence Pr conditional pass subscript 𝒉 1 subscript 𝑥 2 percent 1 Pr conditional pass subscript 𝒉 2 subscript 𝑥 2 percent 10\Pr(\text{pass}|\bm{h_{1}},x_{1})=10\%,\Pr(\text{pass}|\bm{h_{2}},x_{1})=1\%,% \Pr(\text{pass}|\bm{h_{1}},x_{2})=1\%,\Pr(\text{pass}|\bm{h_{2}},x_{2})=10\%roman_Pr ( pass | bold_italic_h start_POSTSUBSCRIPT bold_1 end_POSTSUBSCRIPT , italic_x start_POSTSUBSCRIPT 1 end_POSTSUBSCRIPT ) = 10 % , roman_Pr ( pass | bold_italic_h start_POSTSUBSCRIPT bold_2 end_POSTSUBSCRIPT , italic_x start_POSTSUBSCRIPT 1 end_POSTSUBSCRIPT ) = 1 % , roman_Pr ( pass | bold_italic_h start_POSTSUBSCRIPT bold_1 end_POSTSUBSCRIPT , italic_x start_POSTSUBSCRIPT 2 end_POSTSUBSCRIPT ) = 1 % , roman_Pr ( pass | bold_italic_h start_POSTSUBSCRIPT bold_2 end_POSTSUBSCRIPT , italic_x start_POSTSUBSCRIPT 2 end_POSTSUBSCRIPT ) = 10 %. In other words, 𝒉 1 subscript 𝒉 1\bm{h}_{1}bold_italic_h start_POSTSUBSCRIPT 1 end_POSTSUBSCRIPT is better at solving x 1 subscript 𝑥 1 x_{1}italic_x start_POSTSUBSCRIPT 1 end_POSTSUBSCRIPT and 𝒉 2 subscript 𝒉 2\bm{h}_{2}bold_italic_h start_POSTSUBSCRIPT 2 end_POSTSUBSCRIPT is better at solving x 2 subscript 𝑥 2 x_{2}italic_x start_POSTSUBSCRIPT 2 end_POSTSUBSCRIPT.
80	
81	Consider the allocation of 10 samples per problem to these two configurations. If we use a pure allocation, all 10 samples will be entirely given to either 𝒉 1 subscript 𝒉 1\bm{h}_{1}bold_italic_h start_POSTSUBSCRIPT 1 end_POSTSUBSCRIPT or 𝒉 2 subscript 𝒉 2\bm{h}_{2}bold_italic_h start_POSTSUBSCRIPT 2 end_POSTSUBSCRIPT, the expected pass@10 would be
82	
83	1−(1−0.1)10+1−(1−0.01)10 2=37.3%.1 superscript 1 0.1 10 1 superscript 1 0.01 10 2 percent 37.3\displaystyle\frac{1-(1-0.1)^{10}+1-(1-0.01)^{10}}{2}=37.3\%.divide start_ARG 1 - ( 1 - 0.1 ) start_POSTSUPERSCRIPT 10 end_POSTSUPERSCRIPT + 1 - ( 1 - 0.01 ) start_POSTSUPERSCRIPT 10 end_POSTSUPERSCRIPT end_ARG start_ARG 2 end_ARG = 37.3 % .
84	
85	On the other hand, if we use a mixed allocation and split 10 samples evenly between 𝒉 1 subscript 𝒉 1\bm{h}_{1}bold_italic_h start_POSTSUBSCRIPT 1 end_POSTSUBSCRIPT and 𝒉 2 subscript 𝒉 2\bm{h}_{2}bold_italic_h start_POSTSUBSCRIPT 2 end_POSTSUBSCRIPT, the expected pass@10 would be
86	
87	1−(1−0.1)5×(1−0.01)5=43.8%,1 superscript 1 0.1 5 superscript 1 0.01 5 percent 43.8\displaystyle 1-(1-0.1)^{5}\times(1-0.01)^{5}=43.8\%,1 - ( 1 - 0.1 ) start_POSTSUPERSCRIPT 5 end_POSTSUPERSCRIPT × ( 1 - 0.01 ) start_POSTSUPERSCRIPT 5 end_POSTSUPERSCRIPT = 43.8 % ,
88	
89	which is significantly higher than the pure allocation’s result.
90	
91	### 3.3 Our Algorithm
92	
93	The proposed Osca is described in Algorithm [1](https://arxiv.org/html/2410.22480v1#alg1 "Algorithm 1 ‣ 3.3 Our Algorithm ‣ 3 Method ‣ Scaling LLM Inference with Optimized Sample Compute Allocation").
94	
95	Estimating pass probability. For each sampling configuration 𝒉 i subscript 𝒉 𝑖\bm{h}_{i}bold_italic_h start_POSTSUBSCRIPT italic_i end_POSTSUBSCRIPT and each problem x j subscript 𝑥 𝑗 x_{j}italic_x start_POSTSUBSCRIPT italic_j end_POSTSUBSCRIPT in the training set, we estimate a probability matrix P 𝑃 P italic_P with |ℋ|×|𝒟|ℋ 𝒟|\mathcal{H}|\times|\mathcal{D}|| caligraphic_H | × | caligraphic_D | elements. Each element p i⁢j subscript 𝑝 𝑖 𝑗 p_{ij}italic_p start_POSTSUBSCRIPT italic_i italic_j end_POSTSUBSCRIPT indicates the probability of a sample from 𝒉 i subscript 𝒉 𝑖\bm{h}_{i}bold_italic_h start_POSTSUBSCRIPT italic_i end_POSTSUBSCRIPT solving x j subscript 𝑥 𝑗 x_{j}italic_x start_POSTSUBSCRIPT italic_j end_POSTSUBSCRIPT. We estimate p i⁢j subscript 𝑝 𝑖 𝑗 p_{ij}italic_p start_POSTSUBSCRIPT italic_i italic_j end_POSTSUBSCRIPT by sampling C 0 subscript 𝐶 0 C_{0}italic_C start_POSTSUBSCRIPT 0 end_POSTSUBSCRIPT times from 𝒉 i subscript 𝒉 𝑖\bm{h}_{i}bold_italic_h start_POSTSUBSCRIPT italic_i end_POSTSUBSCRIPT and computing the frequency of correct solutions,
96	
97	p i⁢j≈c i⁢j C 0,subscript 𝑝 𝑖 𝑗 subscript 𝑐 𝑖 𝑗 subscript 𝐶 0\displaystyle p_{ij}\approx\frac{c_{ij}}{C_{0}},italic_p start_POSTSUBSCRIPT italic_i italic_j end_POSTSUBSCRIPT ≈ divide start_ARG italic_c start_POSTSUBSCRIPT italic_i italic_j end_POSTSUBSCRIPT end_ARG start_ARG italic_C start_POSTSUBSCRIPT 0 end_POSTSUBSCRIPT end_ARG ,(1)
98	
99	where c i⁢j subscript 𝑐 𝑖 𝑗 c_{ij}italic_c start_POSTSUBSCRIPT italic_i italic_j end_POSTSUBSCRIPT is the number of correct samples generated for the problem x j subscript 𝑥 𝑗 x_{j}italic_x start_POSTSUBSCRIPT italic_j end_POSTSUBSCRIPT with the configuration 𝒉 i subscript 𝒉 𝑖\bm{h}_{i}bold_italic_h start_POSTSUBSCRIPT italic_i end_POSTSUBSCRIPT. Note that to save compute, the estimation compute budget C 0 subscript 𝐶 0 C_{0}italic_C start_POSTSUBSCRIPT 0 end_POSTSUBSCRIPT is much smaller than the actual compute budget C 𝐶 C italic_C.
100	
101	Maximizing expected pass@C 𝐶 C italic_C on training set. Assuming that the test set is i.i.d. with the training set, we optimize π 𝜋\pi italic_π to maximize pass@C 𝐶 C italic_C on training data. For a single problem x j subscript 𝑥 𝑗 x_{j}italic_x start_POSTSUBSCRIPT italic_j end_POSTSUBSCRIPT and a single configuration 𝒉 i∈ℋ subscript 𝒉 𝑖 ℋ\bm{h}_{i}\in\mathcal{H}bold_italic_h start_POSTSUBSCRIPT italic_i end_POSTSUBSCRIPT ∈ caligraphic_H, its pass@C i subscript 𝐶 𝑖 C_{i}italic_C start_POSTSUBSCRIPT italic_i end_POSTSUBSCRIPT is defined as it probability of being solved with compute C i subscript 𝐶 𝑖 C_{i}italic_C start_POSTSUBSCRIPT italic_i end_POSTSUBSCRIPT, which can be derived as
102	
103	Pr⁡(x j solved with C i samples from 𝒉 i)Pr x j solved with C i samples from 𝒉 i\displaystyle\Pr(\text{$x_{j}$ solved with $C_{i}$ samples from $\bm{h}_{i}$})roman_Pr ( italic_x start_POSTSUBSCRIPT italic_j end_POSTSUBSCRIPT solved with italic_C start_POSTSUBSCRIPT italic_i end_POSTSUBSCRIPT samples from bold_italic_h start_POSTSUBSCRIPT italic_i end_POSTSUBSCRIPT )
104	=1−(1−p i⁢j)C i.absent 1 superscript 1 subscript 𝑝 𝑖 𝑗 subscript 𝐶 𝑖\displaystyle=1-(1-p_{ij})^{C_{i}}.= 1 - ( 1 - italic_p start_POSTSUBSCRIPT italic_i italic_j end_POSTSUBSCRIPT ) start_POSTSUPERSCRIPT italic_C start_POSTSUBSCRIPT italic_i end_POSTSUBSCRIPT end_POSTSUPERSCRIPT .(2)
105	
106	By aggregating all problems and all configurations, we can obtain this optimization problem:
107	
108	max π subscript 𝜋\displaystyle\max_{\pi}\ roman_max start_POSTSUBSCRIPT italic_π end_POSTSUBSCRIPT 𝔼⁢[pass@⁢C]𝔼 delimited-[]pass@𝐶\displaystyle\mathbb{E}[\text{pass@}C]blackboard_E [ pass@ italic_C ]
109	=\displaystyle==1|𝒟|⁢∑j=1|𝒟|(1−∏i=1|ℋ|(1−p i⁢j)π i),1 𝒟 superscript subscript 𝑗 1 𝒟 1 superscript subscript product 𝑖 1 ℋ superscript 1 subscript 𝑝 𝑖 𝑗 subscript 𝜋 𝑖\displaystyle\frac{1}{|\mathcal{D}|}\sum_{j=1}^{|\mathcal{D}|}\left(1-\prod_{i% =1}^{|\mathcal{H}|}(1-p_{ij})^{\pi_{i}}\right),divide start_ARG 1 end_ARG start_ARG | caligraphic_D | end_ARG ∑ start_POSTSUBSCRIPT italic_j = 1 end_POSTSUBSCRIPT start_POSTSUPERSCRIPT | caligraphic_D | end_POSTSUPERSCRIPT ( 1 - ∏ start_POSTSUBSCRIPT italic_i = 1 end_POSTSUBSCRIPT start_POSTSUPERSCRIPT | caligraphic_H | end_POSTSUPERSCRIPT ( 1 - italic_p start_POSTSUBSCRIPT italic_i italic_j end_POSTSUBSCRIPT ) start_POSTSUPERSCRIPT italic_π start_POSTSUBSCRIPT italic_i end_POSTSUBSCRIPT end_POSTSUPERSCRIPT ) ,
110	s.t.0≤π i≤C,0 subscript 𝜋 𝑖 𝐶\displaystyle 0\leq\pi_{i}\leq C,0 ≤ italic_π start_POSTSUBSCRIPT italic_i end_POSTSUBSCRIPT ≤ italic_C ,
111	∑i=1|ℋ|π i=C,π i∈ℕ.formulae-sequence superscript subscript 𝑖 1 ℋ subscript 𝜋 𝑖 𝐶 subscript 𝜋 𝑖 ℕ\displaystyle\sum_{i=1}^{|\mathcal{H}|}\pi_{i}=C,\pi_{i}\in\mathbb{N}.∑ start_POSTSUBSCRIPT italic_i = 1 end_POSTSUBSCRIPT start_POSTSUPERSCRIPT | caligraphic_H | end_POSTSUPERSCRIPT italic_π start_POSTSUBSCRIPT italic_i end_POSTSUBSCRIPT = italic_C , italic_π start_POSTSUBSCRIPT italic_i end_POSTSUBSCRIPT ∈ blackboard_N .(3)
112	
113	Note that if we remove the integral constraint π i∈ℕ subscript 𝜋 𝑖 ℕ\pi_{i}\in\mathbb{N}italic_π start_POSTSUBSCRIPT italic_i end_POSTSUBSCRIPT ∈ blackboard_N from Problem ([3](https://arxiv.org/html/2410.22480v1#S3.E3 "In 3.3 Our Algorithm ‣ 3 Method ‣ Scaling LLM Inference with Optimized Sample Compute Allocation")), the relaxed problem is convex (Proof in Appendix [A.1](https://arxiv.org/html/2410.22480v1#A1.SS1 "A.1 Proof of Convexity ‣ Appendix A Appendix ‣ Scaling LLM Inference with Optimized Sample Compute Allocation")) that can be solved optimally by hill climbing algorithm (Russell and Norvig, [2016](https://arxiv.org/html/2410.22480v1#bib.bib18)). We start from a randomly picked distribution of compute π(0)superscript 𝜋 0\pi^{(0)}italic_π start_POSTSUPERSCRIPT ( 0 ) end_POSTSUPERSCRIPT. At each iteration t 𝑡 t italic_t, we examine all the neighbors of the current distribution that differ slightly from π(t)superscript 𝜋 𝑡\pi^{(t)}italic_π start_POSTSUPERSCRIPT ( italic_t ) end_POSTSUPERSCRIPT and “climb” to the neighbor if it’s better than the current distribution to obtain π(t+1)superscript 𝜋 𝑡 1\pi^{(t+1)}italic_π start_POSTSUPERSCRIPT ( italic_t + 1 ) end_POSTSUPERSCRIPT. The algorithm stops once there is no better neighbor. Though the algorithm is not guaranteed to produce global optima for integral solutions, it works well empirically.
114	
115	This algorithm can be extended to problems with real scores with some slight modification, as discussed in Appendix [A.4](https://arxiv.org/html/2410.22480v1#A1.SS4 "A.4 Mathematical Formulas for Evaluating Results with Fractional Scores ‣ Appendix A Appendix ‣ Scaling LLM Inference with Optimized Sample Compute Allocation").
116	
117	Algorithm 1 Osca: Algorithm for Optimizing Sample Compute Allocation
118	
119	1 Input: Inference budget
120	
121	C 𝐶 C italic_C
122	, estimation budget
123	
124	C 0 subscript 𝐶 0 C_{0}italic_C start_POSTSUBSCRIPT 0 end_POSTSUBSCRIPT
125	, sampling configurations
126	
127	ℋ ℋ\mathcal{H}caligraphic_H
128	, training problem set
129	
130	𝒟 train subscript 𝒟 train\mathcal{D}_{\text{train}}caligraphic_D start_POSTSUBSCRIPT train end_POSTSUBSCRIPT
131	, where
132	
133	(x i,v i)∈D train subscript 𝑥 𝑖 subscript 𝑣 𝑖 subscript 𝐷 train(x_{i},v_{i})\in D_{\text{train}}( italic_x start_POSTSUBSCRIPT italic_i end_POSTSUBSCRIPT , italic_v start_POSTSUBSCRIPT italic_i end_POSTSUBSCRIPT ) ∈ italic_D start_POSTSUBSCRIPT train end_POSTSUBSCRIPT
134	is a problem specification and its verifier.
135	
136	2 Output: Inference strategy
137	
138	π 𝜋\pi italic_π
139	.
140	
141	3
142	
143	4 function OptimizeAllocation(
144	
145	C,C 0,ℋ,𝒟 train 𝐶 subscript 𝐶 0 ℋ subscript 𝒟 train C,C_{0},\mathcal{H},\mathcal{D}_{\text{train}}italic_C , italic_C start_POSTSUBSCRIPT 0 end_POSTSUBSCRIPT , caligraphic_H , caligraphic_D start_POSTSUBSCRIPT train end_POSTSUBSCRIPT
146	)
147	
148	5
149	
150	P←EstimatePassProb⁢(C,C 0,ℋ)←𝑃 EstimatePassProb 𝐶 subscript 𝐶 0 ℋ P\leftarrow\textsc{EstimatePassProb}(C,C_{0},\mathcal{H})italic_P ← EstimatePassProb ( italic_C , italic_C start_POSTSUBSCRIPT 0 end_POSTSUBSCRIPT , caligraphic_H )
151	
152	6 Randomly initialize allocation
153	
154	π={π 1,…,π m}𝜋 subscript 𝜋 1…subscript 𝜋 𝑚\pi=\{\pi_{1},\dots,\pi_{m}\}italic_π = { italic_π start_POSTSUBSCRIPT 1 end_POSTSUBSCRIPT , … , italic_π start_POSTSUBSCRIPT italic_m end_POSTSUBSCRIPT }
155	such that
156	
157	∑i=1 m π i=C superscript subscript 𝑖 1 𝑚 subscript 𝜋 𝑖 𝐶\sum_{i=1}^{m}\pi_{i}=C∑ start_POSTSUBSCRIPT italic_i = 1 end_POSTSUBSCRIPT start_POSTSUPERSCRIPT italic_m end_POSTSUPERSCRIPT italic_π start_POSTSUBSCRIPT italic_i end_POSTSUBSCRIPT = italic_C
158	.
159	
160	7 repeat
161	
162	8 improved
163	
164	←←\leftarrow←
165	False
166	
167	9// Enumerating all neighboring strategies
168	
169	10 for
170	
171	i←1⁢to⁢m←𝑖 1 to 𝑚 i\leftarrow 1\text{ to }m italic_i ← 1 to italic_m
172	,
173	
174	j←1⁢to⁢m←𝑗 1 to 𝑚 j\leftarrow 1\text{ to }m italic_j ← 1 to italic_m
175	and
176	
177	i≠j 𝑖 𝑗 i\neq j italic_i ≠ italic_j
178	and
179	
180	π i>0 subscript 𝜋 𝑖 0\pi_{i}>0 italic_π start_POSTSUBSCRIPT italic_i end_POSTSUBSCRIPT > 0
181	do
182	
183	11
184	
185	q←π←𝑞 𝜋 q\leftarrow\pi italic_q ← italic_π
186	
187	12
188	
189	q i,q j←π i−1,π j+1 formulae-sequence←subscript 𝑞 𝑖 subscript 𝑞 𝑗 subscript 𝜋 𝑖 1 subscript 𝜋 𝑗 1 q_{i},q_{j}\leftarrow\pi_{i}-1,\pi_{j}+1 italic_q start_POSTSUBSCRIPT italic_i end_POSTSUBSCRIPT , italic_q start_POSTSUBSCRIPT italic_j end_POSTSUBSCRIPT ← italic_π start_POSTSUBSCRIPT italic_i end_POSTSUBSCRIPT - 1 , italic_π start_POSTSUBSCRIPT italic_j end_POSTSUBSCRIPT + 1
190	
191	13 if PredAcc(
192	
193	q,P 𝑞 𝑃 q,P italic_q , italic_P
194	)
195	
196	>>>
197	PredAcc(π,P 𝜋 𝑃\pi,P italic_π , italic_P)then
198	
199	14
200	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "cc4e00cc-906d-468c-96fc-e8c5315469c2",
  "isSidechain": true,
  "promptId": "295c0657-e121-425c-967b-f63279f1549e",
  "agentId": "a5512f66970097acf",
  "type": "user",
  "uuid": "ef3cb01a-e2ad-4c4b-a5f1-6935cf94a564",
  "sourceToolAssistantUUID": "cc4e00cc-906d-468c-96fc-e8c5315469c2",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "393d191a-0034-4130-a331-edb9d3156024",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 30 · 2026-05-29T10:07:39.345Z_

<details><summary>↩ Tool result · `toolu_01RYpTfHEDWmnPXUTVyX35sj`</summary>

```text
Web search results for query: "openreview.net NAACL 2025 "Scaling LLM Inference" "sample compute allocation""

Links: [{"title":"Scaling LLM Inference with Optimized Sample Compute Allocation","url":"https://arxiv.org/pdf/2410.22480"},{"title":"Scaling LLM Inference Efficiently with Optimized Sample Compute Allocation - ACL Anthology","url":"https://aclanthology.org/2025.naacl-long.404/"},{"title":"[2410.22480] Scaling LLM Inference with Optimized Sample Compute Allocation","url":"https://arxiv.org/abs/2410.22480"},{"title":"Scaling LLM Inference Efficiently with Optimized Sample ...","url":"https://aclanthology.org/2025.naacl-long.404.pdf"},{"title":"Parameter vs. Test-Time Scaling in LLMs: FLOPs-Aware, Cross-Domain, Domain-Dependent, Pareto-Optimal Compute Allocation | OpenReview","url":"https://openreview.net/forum?id=wU35L1GZud"}]

I found the paper you're looking for! The paper "Scaling LLM Inference Efficiently with Optimized Sample Compute Allocation" was published at the 2025 Conference of the Nations of the Americas Chapter of the Association for Computational Linguistics (NAACL 2025) in Albuquerque, New Mexico.

The paper proposes OSCA, an algorithm that Optimizes Sample Compute Allocation by finding an optimal mix of different inference configurations. The experiments show that with their learned mixed allocation, they can achieve accuracy better than the best single configuration with 128x less compute on code generation and 25x less compute on 4 reasoning tasks.

The paper is available on both the ACL Anthology (at aclanthology.org/2025.naacl-long.404/) and on arXiv. The authors are Kexun Zhang, Shang Zhou, Danqing Wang, William Yang Wang, and Lei Li.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "05e9cf58-0039-4c27-9534-7b1f87149770",
  "isSidechain": true,
  "promptId": "295c0657-e121-425c-967b-f63279f1549e",
  "agentId": "a5512f66970097acf",
  "type": "user",
  "uuid": "2dc81923-53c6-401c-a1b2-fe1377b55ec5",
  "sourceToolAssistantUUID": "05e9cf58-0039-4c27-9534-7b1f87149770",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "393d191a-0034-4130-a331-edb9d3156024",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 31 · 2026-05-29T10:07:42.543Z_

Let me continue reading the rest of the paper for the experiments section and results tables, and also try to find the OpenReview page directly.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2dc81923-53c6-401c-a1b2-fe1377b55ec5",
  "isSidechain": true,
  "agentId": "a5512f66970097acf",
  "requestId": "req_011CbWg7FNVv2W33rhPmqDQa",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "f6fb2866-7c5d-46ba-af82-24f49aa64eab",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "393d191a-0034-4130-a331-edb9d3156024",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EvH3iadU4Ch6xiKkpeYVm9",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 12873,
      "cache_read_input_tokens": 16275,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 12873,
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

_source line 32 · 2026-05-29T10:07:45.771Z_

<details open><summary>🔧 Tool call — Read · `toolu_011bx2NtWnWNZZb6gVo6Mw2u`</summary>

```json
{
  "file_path": "/home/ubuntu/.claude-account-2/projects/-home-ubuntu-idea-adversarial/393d191a-0034-4130-a331-edb9d3156024/tool-results/toolu_012QWTugmBMzSHmjdci8BRvq.txt",
  "offset": 200,
  "limit": 300
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f6fb2866-7c5d-46ba-af82-24f49aa64eab",
  "isSidechain": true,
  "agentId": "a5512f66970097acf",
  "requestId": "req_011CbWg7FNVv2W33rhPmqDQa",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "6a2fa690-a045-40cb-9c33-1c6d18929eb8",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "393d191a-0034-4130-a331-edb9d3156024",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EvH3iadU4Ch6xiKkpeYVm9",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 12873,
      "cache_read_input_tokens": 16275,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 12873,
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

_source line 33 · 2026-05-29T10:07:46.058Z_

<details><summary>↩ Tool result · `toolu_011bx2NtWnWNZZb6gVo6Mw2u`</summary>

```text
200	
201	π←q←𝜋 𝑞\pi\leftarrow q italic_π ← italic_q
202	// Climb to a better strategy.
203	
204	15 improved
205	
206	←←\leftarrow←
207	True.
208	
209	16 end if
210	
211	17 end for
212	
213	18 until not improved
214	
215	19 end function
216	
217	20
218	
219	21
220	
221	22 function EstimatePassProb(
222	
223	C,C 0,ℋ 𝐶 subscript 𝐶 0 ℋ C,C_{0},\mathcal{H}italic_C , italic_C start_POSTSUBSCRIPT 0 end_POSTSUBSCRIPT , caligraphic_H
224	)
225	
226	23 for
227	
228	𝒉 i∈ℋ subscript 𝒉 𝑖 ℋ\bm{h}_{i}\in\mathcal{H}bold_italic_h start_POSTSUBSCRIPT italic_i end_POSTSUBSCRIPT ∈ caligraphic_H
229	do
230	
231	24 for
232	
233	(x j,v j)∈𝒟 train subscript 𝑥 𝑗 subscript 𝑣 𝑗 subscript 𝒟 train(x_{j},v_{j})\in\mathcal{D}_{\text{train}}( italic_x start_POSTSUBSCRIPT italic_j end_POSTSUBSCRIPT , italic_v start_POSTSUBSCRIPT italic_j end_POSTSUBSCRIPT ) ∈ caligraphic_D start_POSTSUBSCRIPT train end_POSTSUBSCRIPT
234	do
235	
236	25 Generate
237	
238	C 0 subscript 𝐶 0 C_{0}italic_C start_POSTSUBSCRIPT 0 end_POSTSUBSCRIPT
239	samples
240	
241	y 1,y 2,⋯,y C 0 subscript 𝑦 1 subscript 𝑦 2⋯subscript 𝑦 subscript 𝐶 0 y_{1},y_{2},\cdots,y_{C_{0}}italic_y start_POSTSUBSCRIPT 1 end_POSTSUBSCRIPT , italic_y start_POSTSUBSCRIPT 2 end_POSTSUBSCRIPT , ⋯ , italic_y start_POSTSUBSCRIPT italic_C start_POSTSUBSCRIPT 0 end_POSTSUBSCRIPT end_POSTSUBSCRIPT
242	,
243	
244	y i∼Pr LM⁡(y|x,𝒉)similar-to subscript 𝑦 𝑖 subscript Pr LM conditional 𝑦 𝑥 𝒉 y_{i}\sim\Pr_{\text{LM}}(y|x,\bm{h})italic_y start_POSTSUBSCRIPT italic_i end_POSTSUBSCRIPT ∼ roman_Pr start_POSTSUBSCRIPT LM end_POSTSUBSCRIPT ( italic_y | italic_x , bold_italic_h )
245	.
246	
247	26
248	
249	c←|{y i:v j⁢(y i)=True}|←𝑐 conditional-set subscript 𝑦 𝑖 subscript 𝑣 𝑗 subscript 𝑦 𝑖 True c\leftarrow\left|\{y_{i}:v_{j}(y_{i})=\texttt{True}\}\right|italic_c ← | { italic_y start_POSTSUBSCRIPT italic_i end_POSTSUBSCRIPT : italic_v start_POSTSUBSCRIPT italic_j end_POSTSUBSCRIPT ( italic_y start_POSTSUBSCRIPT italic_i end_POSTSUBSCRIPT ) = True } |
250	.
251	
252	27
253	
254	p i⁢j←c/C 0←subscript 𝑝 𝑖 𝑗 𝑐 subscript 𝐶 0 p_{ij}\leftarrow c/C_{0}italic_p start_POSTSUBSCRIPT italic_i italic_j end_POSTSUBSCRIPT ← italic_c / italic_C start_POSTSUBSCRIPT 0 end_POSTSUBSCRIPT
255	.
256	
257	28 end for
258	
259	29 end for
260	
261	30 end function
262	
263	31
264	
265	32 function PredAcc(
266	
267	π,P 𝜋 𝑃\pi,P italic_π , italic_P
268	)
269	
270	33 return
271	
272	1|𝒟|⁢∑j=1|𝒟|(1−∏i=1|ℋ|(1−p i⁢j)π⁢(𝒉 i))1 𝒟 superscript subscript 𝑗 1 𝒟 1 superscript subscript product 𝑖 1 ℋ superscript 1 subscript 𝑝 𝑖 𝑗 𝜋 subscript 𝒉 𝑖\frac{1}{|\mathcal{D}|}\sum_{j=1}^{|\mathcal{D}|}\left(1-\prod_{i=1}^{|% \mathcal{H}|}(1-p_{ij})^{\pi(\bm{h}_{i})}\right)divide start_ARG 1 end_ARG start_ARG | caligraphic_D | end_ARG ∑ start_POSTSUBSCRIPT italic_j = 1 end_POSTSUBSCRIPT start_POSTSUPERSCRIPT | caligraphic_D | end_POSTSUPERSCRIPT ( 1 - ∏ start_POSTSUBSCRIPT italic_i = 1 end_POSTSUBSCRIPT start_POSTSUPERSCRIPT | caligraphic_H | end_POSTSUPERSCRIPT ( 1 - italic_p start_POSTSUBSCRIPT italic_i italic_j end_POSTSUBSCRIPT ) start_POSTSUPERSCRIPT italic_π ( bold_italic_h start_POSTSUBSCRIPT italic_i end_POSTSUBSCRIPT ) end_POSTSUPERSCRIPT )
273	
274	34 end function
275	
276	Discussion on the definition of compute budget. In our experiments, we use the number of samples as a metric for compute, which is reasonable when the compute/price to generate each sample is similar for different configurations. However, there are other cases when the model sizes differ greatly or when the FLOPs budget for each sampling configuration varies significantly. For those cases, sample budget is not a good proxy for compute budget, and Problem ([3](https://arxiv.org/html/2410.22480v1#S3.E3 "In 3.3 Our Algorithm ‣ 3 Method ‣ Scaling LLM Inference with Optimized Sample Compute Allocation")) will need to be modified to accommodate different definitions of compute budget, possibly by adding a coefficient to weight the sample budget for each problem. Nonetheless, such modification does not change the convexity of the relaxed problem. Thus our algorithm can still apply.
277	
278	4 Evaluation on Single-Turn Tasks
279	---------------------------------
280	
281	We first evaluate Osca on single-turn tasks, where a solution to a problem can be generated with a single LLM call. For these tasks, the only way to scale up LLM inference is to sample more solutions.
282	
283	### 4.1 Baselines
284	
285	We consider three baselines in our experiments – default pure allocation, optimal pure allocation, and uniform mixed allocation:
286	
287	Default pure allocation is the one used to produce the leaderboard results on the benchmarks. These benchmarks usually run LLM inference once for each problem instance, with a very basic prompt and a low temperature for reproducibility and fair comparison. Therefore, the default pure allocation is not optimized for scaling up.
288	
289	Optimal pure allocation is the one that has the highest pass@C 0 subscript 𝐶 0 C_{0}italic_C start_POSTSUBSCRIPT 0 end_POSTSUBSCRIPT on the training set given a compute budget of C 0 subscript 𝐶 0 C_{0}italic_C start_POSTSUBSCRIPT 0 end_POSTSUBSCRIPT. Since the actual C 𝐶 C italic_C is larger than C 0 subscript 𝐶 0 C_{0}italic_C start_POSTSUBSCRIPT 0 end_POSTSUBSCRIPT in most cases, we use pass@C 0 subscript 𝐶 0 C_{0}italic_C start_POSTSUBSCRIPT 0 end_POSTSUBSCRIPT to select the optimal configuration. Comparison between the optimal pure allocation and the default pure allocation indicates whether it is necessary to search for a good set of inference hyperparameters, which is what existing hyperparameter optimization techniques do.
290	
291	Uniform mixed allocation naively distributes the compute budget evenly to every sampling configuration 𝒉 i subscript 𝒉 𝑖\bm{h}_{i}bold_italic_h start_POSTSUBSCRIPT italic_i end_POSTSUBSCRIPT in 𝑯 𝑯\bm{H}bold_italic_H. We compare the uniform mixed allocation with our learned mixed allocation to examine whether it is necessary to optimize sample compute allocations for them to perform well.
292	
293	### 4.2 Tasks and Benchmarks
294	
295	We evaluate Osca on five tasks from two benchmarks – LiveCodeBench (Jain et al., [2024](https://arxiv.org/html/2410.22480v1#bib.bib11)) and LiveBench (White et al., [2024](https://arxiv.org/html/2410.22480v1#bib.bib28)). These two benchmarks are built with periodically released examinations and competitions so that the possibility of contamination can be minimized. To further avoid contamination, we choose the earlier released problems as training set 𝒟 train subscript 𝒟 train\mathcal{D}_{\text{train}}caligraphic_D start_POSTSUBSCRIPT train end_POSTSUBSCRIPT.
296	
297	LiveCodeBench (Jain et al., [2024](https://arxiv.org/html/2410.22480v1#bib.bib11)) collects LeetCode-style problems from weekly held online programming competitions such as LeetCode, Codeforces, and AtCoder. Each problem comes with a natural language specification that includes problem description, sample test cases, and input range. When given a problem, an LLM is supposed to create a program that can pass both the sample tests visible to the model and the hidden tests that are usually more comprehensive. Within each category among the three (LeetCode, AtCoder, Codeforces) in LiveCodeBench, we sort the problems according to the time they were released and use the first 3/5 of the problems as training data. This split gives us 305 problems for training and 205 problems for evaluation. Most training problems are released before 2024, while the evaluation problems are after 2024.
298	
299	LiveBench (White et al., [2024](https://arxiv.org/html/2410.22480v1#bib.bib28)) shares the same spirit as LiveCodeBench but extends the scope of problems. There are 6 problem categories in LiveBench: data analysis, language, reasoning, math, instruction following, and coding. The responses to the instruction-following problems are not easy to verify, and their coding problems are mostly taken from LiveCodeBench. The remaining four categories are used for evaluation. The problems have two release dates (2024-06-24 and 2024-07-26), but most categories have only one release. Therefore, we mixed these two versions and randomly split each category by 3:7, resulting in 201 training and 471 testing problems. Compared to LiveCodeBench, optimizing sample compute allocation is harder on LiveBench, because there are problems from different domains.
300	
301	Table 1: Implementation details for the two benchmarks, including the hyperparameters we consider, the default inference strategy on the leaderboard, and the budget for strategy learning and inference. Temp. and Lang. are the temperature and the programming language used when sampling. 
302	
303	Table 2: Accuracy at different compute budgets (C 𝐶 C italic_C) using different sample compute allocations. We report the difference in accuracy for non-default allocations. LCB stands for code generation tasks in LiveCodeBench. LB stands for subtask categories in LiveBench. The best result for each setting is in bold.
304	
305	We list the sampling configurations in Table [1](https://arxiv.org/html/2410.22480v1#S4.T1 "Table 1 ‣ 4.2 Tasks and Benchmarks ‣ 4 Evaluation on Single-Turn Tasks ‣ Scaling LLM Inference with Optimized Sample Compute Allocation"). The temperatures we consider are multiples of 0.2. For all configurations, we set C 0 subscript 𝐶 0 C_{0}italic_C start_POSTSUBSCRIPT 0 end_POSTSUBSCRIPT to 50. Note that there is one more hyperparameter to optimize for LiveCodeBench – the programming language. For LiveBench, the open-weight models we choose all have about 70B parameters. We also provide the values of hyperparameters for the pure allocation baselines and the budgets for learning and testing.
306	
307	### 4.3 Key Observations
308	
309	We present the pass rates for different sample compute allocations in Table [2](https://arxiv.org/html/2410.22480v1#S4.T2 "Table 2 ‣ 4.2 Tasks and Benchmarks ‣ 4 Evaluation on Single-Turn Tasks ‣ Scaling LLM Inference with Optimized Sample Compute Allocation"). For allocations other than the default pure, we show the difference between their pass rate and that of default pure. Several key observations can be made from these results:
310	
311	Pure allocation is not enough, mixed allocation is necessary. By finding the optimal pure allocation on the training set, we get much better accuracy than the default allocation, highlighting the importance of a suitable inference configuration. However, pure allocation is not enough on LiveCodeBench. We find that code problems require a more diverse solution set, making the pure configuration not enough. On LiveCodeBench, just by allocating sample compute evenly across inference settings, we achieve a pass@8 of 73.3%, which is better than the pass rate of optimal pure allocation with 512 samples.
312	
313	Uniform mixed allocation is not enough, Osca’s optimized allocation is necessary. On LiveBench, uniform mixed allocation does not outperform optimal pure, suggesting that we can’t always opt for uniform mixed. However, Osca’s optimized allocation does. With 8 samples, Osca’s pass rate comes to 67%, which is higher than the pass rate of the default pure allocation with 128 samples. In fact, Osca outperforms all others in all but two cases.
314	
315	Osca scales well with larger compute budgets. Although the sample compute budget (C 0)subscript 𝐶 0(C_{0})( italic_C start_POSTSUBSCRIPT 0 end_POSTSUBSCRIPT ) used for estimating the solve rate matrix was merely 50, Osca can still produce strong sample compute allocations even when the test time compute budget C 𝐶 C italic_C is as large as 1024 per problem.
316	
317	![Image 5: Refer to caption](https://arxiv.org/html/2410.22480v1/x5.png)
318	
319	Figure 3: Osca’s pass rates on LiveBench when trained with different proportions of the training data.
320	
321	### 4.4 Ablation Studies
322	
323	We conduct ablation experiments on LiveBench to answer the following questions.
324	
325	How many problems do we need in training to learn a good mixed allocation? We run Osca on different proportions of the original training set and plot the results in Figure [3](https://arxiv.org/html/2410.22480v1#S4.F3 "Figure 3 ‣ 4.3 Key Observations ‣ 4 Evaluation on Single-Turn Tasks ‣ Scaling LLM Inference with Optimized Sample Compute Allocation"). Since there are multiple ways of subsampling the training set, we run it multiple times and compute the average. For reference, we also plot the results when we train on the test set, which should be the upperbound of Osca. We observe that with the full training data, the allocation learned is very close to the upperbound. At smaller sample compute C 𝐶 C italic_C, the allocation trained from less data is not much worse than the allocation from full training data. However, as C 𝐶 C italic_C gets to over 2 6 superscript 2 6 2^{6}2 start_POSTSUPERSCRIPT 6 end_POSTSUPERSCRIPT, the allocation gets much worse with less training data. We hypothesize that this is because when C 𝐶 C italic_C is large, only the hard problems contribute to the difference in accuracy, which are prone to overfitting when training data is small.
326	
327	![Image 6: Refer to caption](https://arxiv.org/html/2410.22480v1/x6.png)
328	
329	Figure 4: Osca with different sample compute for estimating pass rates. C 0=50 subscript 𝐶 0 50 C_{0}=50 italic_C start_POSTSUBSCRIPT 0 end_POSTSUBSCRIPT = 50.
330	
331	![Image 7: Refer to caption](https://arxiv.org/html/2410.22480v1/x7.png)
332	
333	Figure 5: Osca’s pass rates on LiveBench when it is banned from allocating compute to multiple temperatures or multiple models.
334	
335	How large does C 0 subscript 𝐶 0 C_{0}italic_C start_POSTSUBSCRIPT 0 end_POSTSUBSCRIPT need to be in order to estimate pass rates on training data?C 0 subscript 𝐶 0 C_{0}italic_C start_POSTSUBSCRIPT 0 end_POSTSUBSCRIPT, the sample compute budget for estimating pass rates on training data, can be much smaller than C 𝐶 C italic_C, which might affect Osca’s performance. We study how estimating with different values of C 0 subscript 𝐶 0 C_{0}italic_C start_POSTSUBSCRIPT 0 end_POSTSUBSCRIPT might affect the learning process. As Figure[4](https://arxiv.org/html/2410.22480v1#S4.F4 "Figure 4 ‣ 4.4 Ablation Studies ‣ 4 Evaluation on Single-Turn Tasks ‣ Scaling LLM Inference with Optimized Sample Compute Allocation") shows, even with 26% of the original C 0 subscript 𝐶 0 C_{0}italic_C start_POSTSUBSCRIPT 0 end_POSTSUBSCRIPT, Osca can still get an accuracy very close to its upperbound, indicating that it is not really sensitive to C 0 subscript 𝐶 0 C_{0}italic_C start_POSTSUBSCRIPT 0 end_POSTSUBSCRIPT.
336	
337	Which hyperparameter in sampling configurations needs mixed allocation? To study whether mixed allocation is needed for the two hyperparameters – temperature or model, we consider two limited versions of Osca by banning it from using more than one temperature or more than one model. As shown in Figure[5](https://arxiv.org/html/2410.22480v1#S4.F5 "Figure 5 ‣ 4.4 Ablation Studies ‣ 4 Evaluation on Single-Turn Tasks ‣ Scaling LLM Inference with Optimized Sample Compute Allocation"), when Osca is not allowed to use multiple models, its accuracy degrades to that of optimal pure. When Osca is not allowed to use multiple temperatures, its accuracy degrades to be worse than optimal pure. These results suggest that in order for Osca to perform well, we need more diverse sampling configurations.
338	
339	Table 3: Accuracy of different allocations on subtasks of LiveBench – math (T1), reasoning (T2), language (T3), data analysis (T4).
340	
341	How general is Osca’s learned allocation? In Table [2](https://arxiv.org/html/2410.22480v1#S4.T2 "Table 2 ‣ 4.2 Tasks and Benchmarks ‣ 4 Evaluation on Single-Turn Tasks ‣ Scaling LLM Inference with Optimized Sample Compute Allocation"), we report the overall performance on LiveBench, because Osca’s training data is a combination of 4 subtasks from LiveBench – math, reasoning, language and data analysis. To evaluate the generality of the learned allocation, we examine its performance on the 4 tasks separately. As Table[3](https://arxiv.org/html/2410.22480v1#S4.T3 "Table 3 ‣ 4.4 Ablation Studies ‣ 4 Evaluation on Single-Turn Tasks ‣ Scaling LLM Inference with Optimized Sample Compute Allocation") shows, Osca is the best in 7/12 cases and the second best in the remaining 5. This indicates that the Osca’s learned allocation is domain-specific to some extent. Example problems of these 4 categories can be found in Appendix[A.3](https://arxiv.org/html/2410.22480v1#A1.SS3 "A.3 Example Problems from LiveBench ‣ Appendix A Appendix ‣ Scaling LLM Inference with Optimized Sample Compute Allocation").
342	
343	Can we learn the best configuration at instance level? Ideally, there is no need to use mixed allocation of sampling compute because there is only one optimal configuration for a specific problem. Therefore, we investigate whether it is possible to learn instance-level optimal configuration. We conduct this experiment on LiveCodeBench, as it has a larger training set and more homogeneous problems and is thus easier to learn. We propose a k-nearest neighbor algorithm under the assumption that similar problems need similar sampling configurations. For each test problem x 𝑥 x italic_x, we retrieve the k 𝑘 k italic_k problems in the training set that are most similar to x 𝑥 x italic_x, and allocate compute according to the distribution of optimal configuration over these problems. We use OpenAI’s text-embedding-3-large to create semantic embeddings and compute the similarity between problems. As shown in Table[4](https://arxiv.org/html/2410.22480v1#S4.T4 "Table 4 ‣ 4.4 Ablation Studies ‣ 4 Evaluation on Single-Turn Tasks ‣ Scaling LLM Inference with Optimized Sample Compute Allocation"), Osca outperforms the problem-specific kNN allocation of compute, no matter what value k 𝑘 k italic_k is. This suggests that it is not straightforward to learn problem-specific sampling configurations, justifying the need for a domain-specific allocation.
344	
345	Table 4: Accuracy of problem-specific sample allocation computed using k-nearest neighbor under different values of k 𝑘 k italic_k is consistently lower than Osca, especially when the compute budget is small.
346	
347	5 Evaluation on Agentic Tasks
348	-----------------------------
349	
350	Optimizing sample compute allocation is not just useful for its own purpose, it is also useful for more complicated LLM inference algorithms, such as tree search and agentic workflows, because sampling is a basic operation in these. To demonstrate such usefulness, we apply Osca to an agentic workflow for SWE-Bench, which needs 2 stages and 7 steps involving numerous LLM calls to resolve software engineering issues in repository-level code.
351	
352	### 5.1 Benchmark and Workflow
353	
354	SWE-Bench ([Jimenez et al.,](https://arxiv.org/html/2410.22480v1#bib.bib13)) collects real-world software engineering issues from open-source GitHub repositories such as django and matplotlib. Each issue is paired with human-written unit tests. To resolve an issue, one needs to understand the issue description, examine the codebase (often hundreds of thousands of lines long), locate where to make changes and make necessary modifications by generating a patch. Decent solutions on this benchmark often takes an agentic approach by giving an LLM multiple tools to use and multiple actions to take and guiding it through a multi-stage workflow. We consider a subset of SWE-Bench curated by the authors called SWE-Bench Lite, which contains 300 issues.
355	
356	Agentless (Xia et al., [2024](https://arxiv.org/html/2410.22480v1#bib.bib30)) is one of the best-performing open-source solutions to SWE-Bench. An overview of how Agentless works can be found in Appendix [A.5](https://arxiv.org/html/2410.22480v1#A1.SS5 "A.5 Agentless Workflow on SWE-Bench ‣ Appendix A Appendix ‣ Scaling LLM Inference with Optimized Sample Compute Allocation") Figure [6](https://arxiv.org/html/2410.22480v1#A1.F6 "Figure 6 ‣ A.4 Mathematical Formulas for Evaluating Results with Fractional Scores ‣ Appendix A Appendix ‣ Scaling LLM Inference with Optimized Sample Compute Allocation"). It needs two stages – bug localization and bug repairing – to resolve a software engineering issue. There are 7 steps in total and 4 of them needs LLM sampling. We apply Osca to one crucial step in the workflow – generating patches. Since SWE-Bench is really expensive to evaluate, we set both C 0 subscript 𝐶 0 C_{0}italic_C start_POSTSUBSCRIPT 0 end_POSTSUBSCRIPT and C 𝐶 C italic_C to be a smaller value 16.
357	
358	Implementation Details. We use the same baselines from single-turn tasks – default pure allocation, optimal pure allocation, and uniform mixed allocation. We randomly sample 150 from the 300 issues as Osca’s training set, and use the remaining ones for testing. We consider three dimensions in sampling configuration – model choice, temperature, and prompting. The model choices we consider are gpt-4o-2024-05-13, deepseek-coder-2.5, and qwen-2.5-70B. The temperatures we consider are 0.4, 0.8, 1.2, and 1.6. The prompts are the intermediate results generated from the earlier stages of the workflow. We consider the two sets of intermediate results provided by the authors of Agentless 1 1 1 The prompt sets can downloaded at [https://github.com/OpenAutoCoder/Agentless/releases/tag/v0.1.0](https://github.com/OpenAutoCoder/Agentless/releases/tag/v0.1.0). Prompt set 1 is in [results/location_merged/loc_merged_0-1_outputs.jsonl](https://arxiv.org/html/2410.22480v1/results/location_merged/loc_merged_0-1_outputs.jsonl). Prompt set 2 is in [results/location_merged/loc_merged_2-3_outputs.jsonl](https://arxiv.org/html/2410.22480v1/results/location_merged/loc_merged_2-3_outputs.jsonl). . They contain the relevant contexts in code files that the system finds relevant to the specific issue descriptions.
359	
360	Both the default and optimal settings are gpt-4o, temperature 0.8 and prompt set 1.
361	
362	### 5.2 Results
363	
364	As demonstrated in Figure [1](https://arxiv.org/html/2410.22480v1#S1.F1 "Figure 1 ‣ 1 Introduction ‣ Scaling LLM Inference with Optimized Sample Compute Allocation"), Osca can also improve the performance of Agentless by improving one of the steps in its agentic workflow. Compared to both the pure allocation (Temperature is set to 1 in both default and optimal pure allocation) and uniform mixed allocation, Osca’s learned allocation can get a similar accuracy with fewer samples. The gap between Osca and the optimal pure allocation enlarges as sample compute gets larger, while uniform mixed allocation approaches and outperforms optimal pure with larger sample sizes.
365	
366	These findings further demonstrate the necessity of optimizing sample budget allocation, as it can be used in more complicated workflows to make them more efficient.
367	
368	6 Conclusion
369	------------
370	
371	In conclusion, this paper presents Osca, an algorithm designed to optimize sample compute allocation for large language models (LLMs) during inference. Through various experiments on both single-turn and agentic tasks, the study demonstrates that Osca significantly improves accuracy with reduced compute resources compared to traditional methods, such as pure or uniform mixed allocations. By leveraging a mixed allocation allocation, Osca balances different inference configurations, proving particularly effective in code generation and reasoning tasks, as seen in benchmarks like LiveCodeBench and LiveBench. This work demonstrates the importance of adapting sampling allocation to the specific characteristics of the problem at hand. Furthermore, Osca’s application to more complex workflows, such as multi-step agentic tasks, shows potential for broader utility in improving the efficiency of LLMs in various real-world applications. However, future work could explore optimizing additional hyperparameters and testing the scalability of the method with larger compute budgets.
372	
373	Limitation
374	----------
375	
376	Although Osca demonstrates an effective way to allocate sample compute there are still several limitations. First, this paper mainly focuses on four representative inference hyperparameters: model types, temperatures, response languages, and prompts. In addition to these aspects, there are other hyperparameters such as top k, top p, repetition penalty, etc. Combining these hyperparameters can make the sample configuration set more diverse. Besides, due to the computation limitation, we limited our inference compute budget to 512. It would be interesting to see how further scaling up will affect the performance.
377	
378	Ethics Statement
379	----------------
380	
381	We acknowledge that there might be some ethical considerations in enhancing LLMs’ capability such as the Osca presented in this paper. However, we believe that none must be specifically highlighted here.
382	
383	References
384	----------
385	
386	*   Brown et al. (2024) Bradley Brown, Jordan Juravsky, Ryan Ehrlich, Ronald Clark, Quoc V Le, Christopher Ré, and Azalia Mirhoseini. 2024. Large language monkeys: Scaling inference compute with repeated sampling. _arXiv preprint arXiv:2407.21787_. 
387	*   Chen et al. (2022) Bei Chen, Fengji Zhang, Anh Nguyen, Daoguang Zan, Zeqi Lin, Jian-Guang Lou, and Weizhu Chen. 2022. Codet: Code generation with generated tests. _arXiv e-prints_, pages arXiv–2207. 
388	*   Chen et al. (2021) Mark Chen, Jerry Tworek, Heewoo Jun, Qiming Yuan, Henrique Ponde De Oliveira Pinto, Jared Kaplan, Harri Edwards, Yuri Burda, Nicholas Joseph, Greg Brockman, et al. 2021. Evaluating large language models trained on code. _arXiv preprint arXiv:2107.03374_. 
389	*   Chi et al. (2024) Yizhou Chi, Kevin Yang, and Dan Klein. 2024. Thoughtsculpt: Reasoning with intermediate revision and search. _arXiv preprint arXiv:2404.05966_. 
390	*   Damani et al. (2024) Mehul Damani, Idan Shenfeld, Andi Peng, Andreea Bobu, and Jacob Andreas. 2024. [Learning How Hard to Think: Input-Adaptive Allocation of LM Computation](https://doi.org/10.48550/arXiv.2410.04707). 
391	*   Dehghani et al. (2019) Mostafa Dehghani, Stephan Gouws, Oriol Vinyals, Jakob Uszkoreit, and Lukasz Kaiser. 2019. [Universal transformers](https://openreview.net/forum?id=HyzdRiR9Y7). In _International Conference on Learning Representations_. 
392	*   Dohan et al. (2022) David Dohan, Winnie Xu, Aitor Lewkowycz, Jacob Austin, David Bieber, Raphael Gontijo Lopes, Yuhuai Wu, Henryk Michalewski, Rif A Saurous, Jascha Sohl-Dickstein, et al. 2022. Language model cascades. _arXiv preprint arXiv:2207.10342_. 
393	*   Du et al. (2023) Yilun Du, Shuang Li, Antonio Torralba, Joshua B Tenenbaum, and Igor Mordatch. 2023. Improving factuality and reasoning in language models through multiagent debate. In _Forty-first International Conference on Machine Learning_. 
394	*   Graves (2016) Alex Graves. 2016. Adaptive computation time for recurrent neural networks. _arXiv preprint arXiv:1603.08983_. 
395	*   Huang et al. (2023) Baizhou Huang, Shuai Lu, Weizhu Chen, Xiaojun Wan, and Nan Duan. 2023. Enhancing large language models in coding through multi-perspective self-consistency. _arXiv preprint arXiv:2309.17272_. 
396	*   Jain et al. (2024) Naman Jain, King Han, Alex Gu, Wen-Ding Li, Fanjia Yan, Tianjun Zhang, Sida Wang, Armando Solar-Lezama, Koushik Sen, and Ion Stoica. 2024. Livecodebench: Holistic and contamination free evaluation of large language models for code. _arXiv preprint arXiv:2403.07974_. 
397	*   Jiang et al. (2023) Dongfu Jiang, Xiang Ren, and Bill Yuchen Lin. 2023. [LLM-Blender: Ensembling Large Language Models with Pairwise Ranking and Generative Fusion](https://doi.org/10.18653/v1/2023.acl-long.792). In _Proceedings of the 61st Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers)_, pages 14165–14178, Toronto, Canada. Association for Computational Linguistics. 
398	*   (13) Carlos E Jimenez, John Yang, Alexander Wettig, Shunyu Yao, Kexin Pei, Ofir Press, and Karthik R Narasimhan. Swe-bench: Can language models resolve real-world github issues? In _The Twelfth International Conference on Learning Representations_. 
399	*   Lample et al. (2022) Guillaume Lample, Timothee Lacroix, Marie-Anne Lachaux, Aurelien Rodriguez, Amaury Hayat, Thibaut Lavril, Gabriel Ebner, and Xavier Martinet. 2022. Hypertree proof search for neural theorem proving. _Advances in neural information processing systems_, 35:26337–26349. 
400	*   Leblond et al. (2023) Rémi Leblond et al. 2023. [Alphacode 2 technical report](https://storage.googleapis.com/deepmind-media/AlphaCode2/AlphaCode2_Tech_Report.pdf). Technical report, DeepMind. 
401	*   Li et al. (2022) Yujia Li, David Choi, Junyoung Chung, Nate Kushman, Julian Schrittwieser, Rémi Leblond, Tom Eccles, James Keeling, Felix Gimeno, Agustin Dal Lago, et al. 2022. Competition-level code generation with alphacode. _Science_, 378(6624):1092–1097. 
402	*   Madaan et al. (2024) Aman Madaan, Niket Tandon, Prakhar Gupta, Skyler Hallinan, Luyu Gao, Sarah Wiegreffe, Uri Alon, Nouha Dziri, Shrimai Prabhumoye, Yiming Yang, et al. 2024. Self-refine: Iterative refinement with self-feedback. _Advances in Neural Information Processing Systems_, 36. 
403	*   Russell and Norvig (2016) Stuart J Russell and Peter Norvig. 2016. _Artificial intelligence: a modern approach_. Pearson. 
404	*   Schlag et al. (2023) Imanol Schlag, Sainbayar Sukhbaatar, Asli Celikyilmaz, Wen-tau Yih, Jason Weston, Jürgen Schmidhuber, and Xian Li. 2023. Large language model programs. _arXiv preprint arXiv:2305.05364_. 
405	*   Shinn et al. (2024) Noah Shinn, Federico Cassano, Ashwin Gopinath, Karthik Narasimhan, and Shunyu Yao. 2024. Reflexion: Language agents with verbal reinforcement learning. _Advances in Neural Information Processing Systems_, 36. 
406	*   Snell et al. (2024) Charlie Snell, Jaehoon Lee, Kelvin Xu, and Aviral Kumar. 2024. [Scaling llm test-time compute optimally can be more effective than scaling model parameters](https://arxiv.org/abs/2408.03314). 
407	*   Tian et al. (2024) Ye Tian, Baolin Peng, Linfeng Song, Lifeng Jin, Dian Yu, Haitao Mi, and Dong Yu. 2024. [Toward self-improvement of llms via imagination, searching, and criticizing](https://arxiv.org/abs/2404.12253). _Preprint_, arXiv:2404.12253. 
408	*   Wang et al. (2023a) Chi Wang, Susan Xueqing Liu, and Ahmed H. Awadallah. 2023a. [Cost-effective hyperparameter optimization for large language model generation inference](https://doi.org/10.48550/arXiv.2303.04673). 
409	*   Wang et al. (2023b) Chi Wang, Xueqing Liu, and Ahmed Hassan Awadallah. 2023b. Cost-effective hyperparameter optimization for large language model generation inference. In _International Conference on Automated Machine Learning_, pages 21–1. PMLR. 
410	*   Wang et al. (2024) Siyin Wang, Shimin Li, Tianxiang Sun, Jinlan Fu, Qinyuan Cheng, Jiasheng Ye, Junjie Ye, Xipeng Qiu, Xuanjing Huang, Lun-Wei Ku, Andre Martins, and Vivek Srikumar. 2024. [Llm can achieve self-regulation via hyperparameter aware generation](https://doi.org/10.18653/v1/2024.findings-acl.396). In _Findings of the Association for Computational Linguistics ACL 2024_, pages 6632–6646. Association for Computational Linguistics. 
411	*   Wang et al. (2023c) Xuezhi Wang, Jason Wei, Dale Schuurmans, Quoc V Le, Ed H Chi, Sharan Narang, Aakanksha Chowdhery, and Denny Zhou. 2023c. Self-consistency improves chain of thought reasoning in language models. In _The Eleventh International Conference on Learning Representations_. 
412	*   Welleck et al. (2024) Sean Welleck, Amanda Bertsch, Matthew Finlayson, Hailey Schoelkopf, Alex Xie, Graham Neubig, Ilia Kulikov, and Zaid Harchaoui. 2024. From decoding to meta-generation: Inference-time algorithms for large language models. _arXiv preprint arXiv:2406.16838_. 
413	*   White et al. (2024) Colin White, Samuel Dooley, Manley Roberts, Arka Pal, Ben Feuer, Siddhartha Jain, Ravid Shwartz-Ziv, Neel Jain, Khalid Saifullah, Siddartha Naidu, et al. 2024. Livebench: A challenging, contamination-free llm benchmark. _arXiv preprint arXiv:2406.19314_. 
414	*   Wu et al. (2024) Yangzhen Wu, Zhiqing Sun, Shanda Li, Sean Welleck, and Yiming Yang. 2024. An empirical analysis of compute-optimal inference for problem-solving with language models. _arXiv preprint arXiv:2408.00724_. 
415	*   Xia et al. (2024) Chunqiu Steven Xia, Yinlin Deng, Soren Dunn, and Lingming Zhang. 2024. Agentless: Demystifying llm-based software engineering agents. _arXiv preprint arXiv:2407.01489_. 
416	*   Yao et al. (2024) Shunyu Yao, Dian Yu, Jeffrey Zhao, Izhak Shafran, Tom Griffiths, Yuan Cao, and Karthik Narasimhan. 2024. Tree of thoughts: Deliberate problem solving with large language models. _Advances in Neural Information Processing Systems_, 36. 
417	*   Zhang et al. (2023) Kexun Zhang, Danqing Wang, Jingtao Xia, William Yang Wang, and Lei Li. 2023. Algo: Synthesizing algorithmic programs with generated oracle verifiers. _Advances in Neural Information Processing Systems_, 36:54769–54784. 
418	
419	Appendix A Appendix
420	-------------------
421	
422	### A.1 Proof of Convexity
423	
424	We aim to minimize the following objective function:
425	
426	min π⁡O⁢(π)=∑j=1 m∏i=1 n(1−p i⁢j)π i subscript 𝜋 𝑂 𝜋 superscript subscript 𝑗 1 𝑚 superscript subscript product 𝑖 1 𝑛 superscript 1 subscript 𝑝 𝑖 𝑗 subscript 𝜋 𝑖\min_{\pi}O(\pi)=\sum_{j=1}^{m}\prod_{i=1}^{n}(1-p_{ij})^{\pi_{i}}roman_min start_POSTSUBSCRIPT italic_π end_POSTSUBSCRIPT italic_O ( italic_π ) = ∑ start_POSTSUBSCRIPT italic_j = 1 end_POSTSUBSCRIPT start_POSTSUPERSCRIPT italic_m end_POSTSUPERSCRIPT ∏ start_POSTSUBSCRIPT italic_i = 1 end_POSTSUBSCRIPT start_POSTSUPERSCRIPT italic_n end_POSTSUPERSCRIPT ( 1 - italic_p start_POSTSUBSCRIPT italic_i italic_j end_POSTSUBSCRIPT ) start_POSTSUPERSCRIPT italic_π start_POSTSUBSCRIPT italic_i end_POSTSUBSCRIPT end_POSTSUPERSCRIPT
427	
428	subject to:
429	
430	*   •
431	0≤π i≤C 0 subscript 𝜋 𝑖 𝐶 0\leq\pi_{i}\leq C 0 ≤ italic_π start_POSTSUBSCRIPT italic_i end_POSTSUBSCRIPT ≤ italic_C, with π i∈ℕ subscript 𝜋 𝑖 ℕ\pi_{i}\in\mathbb{N}italic_π start_POSTSUBSCRIPT italic_i end_POSTSUBSCRIPT ∈ blackboard_N
432	
433	*   •
434	∑i=1 n π i=C superscript subscript 𝑖 1 𝑛 subscript 𝜋 𝑖 𝐶\sum_{i=1}^{n}\pi_{i}=C∑ start_POSTSUBSCRIPT italic_i = 1 end_POSTSUBSCRIPT start_POSTSUPERSCRIPT italic_n end_POSTSUPERSCRIPT italic_π start_POSTSUBSCRIPT italic_i end_POSTSUBSCRIPT = italic_C
435	
436	To simplify the analysis, we take the negative logarithm of the objective function, which preserves convexity properties:
437	
438	O⁢(π)=∑j=1 m exp⁡(∑i=1 n π i⁢ln⁡(1−p i⁢j))𝑂 𝜋 superscript subscript 𝑗 1 𝑚 superscript subscript 𝑖 1 𝑛 subscript 𝜋 𝑖 1 subscript 𝑝 𝑖 𝑗 O(\pi)=\sum_{j=1}^{m}\exp\left(\sum_{i=1}^{n}\pi_{i}\ln(1-p_{ij})\right)italic_O ( italic_π ) = ∑ start_POSTSUBSCRIPT italic_j = 1 end_POSTSUBSCRIPT start_POSTSUPERSCRIPT italic_m end_POSTSUPERSCRIPT roman_exp ( ∑ start_POSTSUBSCRIPT italic_i = 1 end_POSTSUBSCRIPT start_POSTSUPERSCRIPT italic_n end_POSTSUPERSCRIPT italic_π start_POSTSUBSCRIPT italic_i end_POSTSUBSCRIPT roman_ln ( 1 - italic_p start_POSTSUBSCRIPT italic_i italic_j end_POSTSUBSCRIPT ) )
439	
440	Define:
441	
442	g j⁢(π)=∑i=1 n π i⁢ln⁡(1−p i⁢j)subscript 𝑔 𝑗 𝜋 superscript subscript 𝑖 1 𝑛 subscript 𝜋 𝑖 1 subscript 𝑝 𝑖 𝑗 g_{j}(\pi)=\sum_{i=1}^{n}\pi_{i}\ln(1-p_{ij})italic_g start_POSTSUBSCRIPT italic_j end_POSTSUBSCRIPT ( italic_π ) = ∑ start_POSTSUBSCRIPT italic_i = 1 end_POSTSUBSCRIPT start_POSTSUPERSCRIPT italic_n end_POSTSUPERSCRIPT italic_π start_POSTSUBSCRIPT italic_i end_POSTSUBSCRIPT roman_ln ( 1 - italic_p start_POSTSUBSCRIPT italic_i italic_j end_POSTSUBSCRIPT )
443	
444	Since g j(π g_{j}(\pi italic_g start_POSTSUBSCRIPT italic_j end_POSTSUBSCRIPT ( italic_π is a linear combination of π i subscript 𝜋 𝑖\pi_{i}italic_π start_POSTSUBSCRIPT italic_i end_POSTSUBSCRIPT, it is an affine function in π 𝜋\pi italic_π. As affine functions are both convex and concave, g j⁢(π)subscript 𝑔 𝑗 𝜋 g_{j}(\mathbf{\pi})italic_g start_POSTSUBSCRIPT italic_j end_POSTSUBSCRIPT ( italic_π ) is convex.
445	
446	The exponential function, exp⁡(z)𝑧\exp(z)roman_exp ( italic_z ), is convex. Since the composition of a convex function with an affine function remains convex, it follows that:
447	
448	h j⁢(π)=exp⁡(g j⁢(π))subscript ℎ 𝑗 𝜋 subscript 𝑔 𝑗 𝜋 h_{j}(\pi)=\exp(g_{j}(\pi))italic_h start_POSTSUBSCRIPT italic_j end_POSTSUBSCRIPT ( italic_π ) = roman_exp ( italic_g start_POSTSUBSCRIPT italic_j end_POSTSUBSCRIPT ( italic_π ) )
449	
450	is convex in π 𝜋\pi italic_π.
451	
452	Thus, the overall objective function:
453	
454	f⁢(π)𝑓 𝜋\displaystyle f(\pi)italic_f ( italic_π )=∑j=1 m h j⁢(π)absent superscript subscript 𝑗 1 𝑚 subscript ℎ 𝑗 𝜋\displaystyle=\sum_{j=1}^{m}h_{j}(\pi)= ∑ start_POSTSUBSCRIPT italic_j = 1 end_POSTSUBSCRIPT start_POSTSUPERSCRIPT italic_m end_POSTSUPERSCRIPT italic_h start_POSTSUBSCRIPT italic_j end_POSTSUBSCRIPT ( italic_π )
455	=∑j=1 m exp⁡(∑i=1 n π i⁢ln⁡(1−p i⁢j))absent superscript subscript 𝑗 1 𝑚 superscript subscript 𝑖 1 𝑛 subscript 𝜋 𝑖 1 subscript 𝑝 𝑖 𝑗\displaystyle=\sum_{j=1}^{m}\exp\left(\sum_{i=1}^{n}\pi_{i}\ln(1-p_{ij})\right)= ∑ start_POSTSUBSCRIPT italic_j = 1 end_POSTSUBSCRIPT start_POSTSUPERSCRIPT italic_m end_POSTSUPERSCRIPT roman_exp ( ∑ start_POSTSUBSCRIPT italic_i = 1 end_POSTSUBSCRIPT start_POSTSUPERSCRIPT italic_n end_POSTSUPERSCRIPT italic_π start_POSTSUBSCRIPT italic_i end_POSTSUBSCRIPT roman_ln ( 1 - italic_p start_POSTSUBSCRIPT italic_i italic_j end_POSTSUBSCRIPT ) )
456	
457	is a sum of convex functions, implying that f⁢(π)𝑓 𝜋 f(\pi)italic_f ( italic_π ) is convex.
458	
459	∎
460	
461	### A.2 Example Problems from LiveCodeBench
462	
463	### A.3 Example Problems from LiveBench
464	
465	Example questions from the Data Analysis category can be lengthy, so examples can be viewed [here](https://huggingface.co/datasets/livebench/data_analysis/viewer/default/test?row=0).
466	
467	### A.4 Mathematical Formulas for Evaluating Results with Fractional Scores
468	
469	Probability Mass Function (PMF) for the Maximum Score When Sampling k 𝑘 k italic_k Scores
470	
471	To calculate the probability that the maximum score X max subscript 𝑋 max X_{\text{max}}italic_X start_POSTSUBSCRIPT max end_POSTSUBSCRIPT among k 𝑘 k italic_k samples is exactly x 𝑥 x italic_x:
472	
473	P⁢(X max=x)=(c≤x k)−(c<x k)(m k)𝑃 subscript 𝑋 max 𝑥 binomial subscript 𝑐 absent 𝑥 𝑘 binomial subscript 𝑐 absent 𝑥 𝑘 binomial 𝑚 𝑘 P(X_{\text{max}}=x)=\frac{\binom{c_{\leq x}}{k}-\binom{c_{<x}}{k}}{\binom{m}{k}}italic_P ( italic_X start_POSTSUBSCRIPT max end_POSTSUBSCRIPT = italic_x ) = divide start_ARG ( FRACOP start_ARG italic_c start_POSTSUBSCRIPT ≤ italic_x end_POSTSUBSCRIPT end_ARG start_ARG italic_k end_ARG ) - ( FRACOP start_ARG italic_c start_POSTSUBSCRIPT < italic_x end_POSTSUBSCRIPT end_ARG start_ARG italic_k end_ARG ) end_ARG start_ARG ( FRACOP start_ARG italic_m end_ARG start_ARG italic_k end_ARG ) end_ARG
474	
475	Where:
476	
477	*   •
478	m=∑x c x 𝑚 subscript 𝑥 subscript 𝑐 𝑥 m=\sum_{x}c_{x}italic_m = ∑ start_POSTSUBSCRIPT italic_x end_POSTSUBSCRIPT italic_c start_POSTSUBSCRIPT italic_x end_POSTSUBSCRIPT is the total sample size.
479	
480	*   •
481	c≤x=∑y≤x c y subscript 𝑐 absent 𝑥 subscript 𝑦 𝑥 subscript 𝑐 𝑦 c_{\leq x}=\sum_{y\leq x}c_{y}italic_c start_POSTSUBSCRIPT ≤ italic_x end_POSTSUBSCRIPT = ∑ start_POSTSUBSCRIPT italic_y ≤ italic_x end_POSTSUBSCRIPT italic_c start_POSTSUBSCRIPT italic_y end_POSTSUBSCRIPT is the cumulative count of scores less than or equal to x 𝑥 x italic_x.
482	
483	*   •
484	c<x=∑y<x c y subscript 𝑐 absent 𝑥 subscript 𝑦 𝑥 subscript 𝑐 𝑦 c_{<x}=\sum_{y<x}c_{y}italic_c start_POSTSUBSCRIPT < italic_x end_POSTSUBSCRIPT = ∑ start_POSTSUBSCRIPT italic_y < italic_x end_POSTSUBSCRIPT italic_c start_POSTSUBSCRIPT italic_y end_POSTSUBSCRIPT is the cumulative count of scores strictly less than x 𝑥 x italic_x.
485	
486	Expected Maximum Score Across Multiple Settings with Known PMF
487	
488	The expected value E⁢[X]𝐸 delimited-[]𝑋 E[X]italic_E [ italic_X ] of the maximum score across multiple settings is:
489	
490	E⁢[X]=∑x x⋅P⁢(X=x)𝐸 delimited-[]𝑋 subscript 𝑥⋅𝑥 𝑃 𝑋 𝑥 E[X]=\sum_{x}x\cdot P(X=x)italic_E [ italic_X ] = ∑ start_POSTSUBSCRIPT italic_x end_POSTSUBSCRIPT italic_x ⋅ italic_P ( italic_X = italic_x )
491	
492	Where P⁢(X=x)𝑃 𝑋 𝑥 P(X=x)italic_P ( italic_X = italic_x ) is computed as:
493	
494	P⁢(X=x)=∏j=1 s P j⁢(X j≤x)−∏j=1 s P j⁢(X j<x)𝑃 𝑋 𝑥 superscript subscript product 𝑗 1 𝑠 subscript 𝑃 𝑗 subscript 𝑋 𝑗 𝑥 superscript subscript product 𝑗 1 𝑠 subscript 𝑃 𝑗 subscript 𝑋 𝑗 𝑥 P(X=x)=\prod_{j=1}^{s}P_{j}(X_{j}\leq x)-\prod_{j=1}^{s}P_{j}(X_{j}<x)italic_P ( italic_X = italic_x ) = ∏ start_POSTSUBSCRIPT italic_j = 1 end_POSTSUBSCRIPT start_POSTSUPERSCRIPT italic_s end_POSTSUPERSCRIPT italic_P start_POSTSUBSCRIPT italic_j end_POSTSUBSCRIPT ( italic_X start_POSTSUBSCRIPT italic_j end_POSTSUBSCRIPT ≤ italic_x ) - ∏ start_POSTSUBSCRIPT italic_j = 1 end_POSTSUBSCRIPT start_POSTSUPERSCRIPT italic_s end_POSTSUPERSCRIPT italic_P start_POSTSUBSCRIPT italic_j end_POSTSUBSCRIPT ( italic_X start_POSTSUBSCRIPT italic_j end_POSTSUBSCRIPT < italic_x )
495	
496	Here, P j⁢(X j≤x)subscript 𝑃 𝑗 subscript 𝑋 𝑗 𝑥 P_{j}(X_{j}\leq x)italic_P start_POSTSUBSCRIPT italic_j end_POSTSUBSCRIPT ( italic_X start_POSTSUBSCRIPT italic_j end_POSTSUBSCRIPT ≤ italic_x ) represents the probability that the maximum score in setting j 𝑗 j italic_j is less than or equal to x 𝑥 x italic_x. The difference between the products isolates the probability that the maximum score is exactly x 𝑥 x italic_x.
497	
498	Expected Maximum Score with Excess Samples
499	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "6a2fa690-a045-40cb-9c33-1c6d18929eb8",
  "isSidechain": true,
  "promptId": "295c0657-e121-425c-967b-f63279f1549e",
  "agentId": "a5512f66970097acf",
  "type": "user",
  "uuid": "f6316a43-262f-49c5-8678-4f23f28253de",
  "sourceToolAssistantUUID": "6a2fa690-a045-40cb-9c33-1c6d18929eb8",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "393d191a-0034-4130-a331-edb9d3156024",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 34 · 2026-05-29T10:07:46.935Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_015ZVw5eVqHTbqu5NZkMQ57N`</summary>

```json
{
  "url": "https://openreview.net/forum?id=wU35L1GZud",
  "prompt": "Is this the paper about OSCA (Optimized Sample Compute Allocation) by Zhang et al.? If so, extract all reviewer comments, scores, strengths, weaknesses, and questions. If not, describe what paper this is."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f6316a43-262f-49c5-8678-4f23f28253de",
  "isSidechain": true,
  "agentId": "a5512f66970097acf",
  "requestId": "req_011CbWg7FNVv2W33rhPmqDQa",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "34a4cfca-bb7b-4861-8973-d67df4d4e0fe",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "393d191a-0034-4130-a331-edb9d3156024",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EvH3iadU4Ch6xiKkpeYVm9",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 12873,
      "cache_read_input_tokens": 16275,
      "output_tokens": 312,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 12873
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 312,
          "cache_read_input_tokens": 16275,
          "cache_creation_input_tokens": 12873,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 12873,
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

_source line 35 · 2026-05-29T10:07:50.019Z_

<details><summary>↩ Tool result · `toolu_015ZVw5eVqHTbqu5NZkMQ57N`</summary>

```text
This is **not** the OSCA paper by Zhang et al. 

This paper, titled "Parameter vs. Test-Time Scaling in LLMs," is authored by **Bumjun Jung** and was published on October 8, 2025, for the Agents4Science 2025 Conference on OpenReview.

The paper investigates how to distribute computational resources between model parameters and test-time scaling (inference-time reasoning) for cost-effective accuracy. It compares internal reasoning mechanisms with external Chain-of-Thought approaches on mathematical reasoning and knowledge retrieval tasks, introducing the "redundancy principle" to quantify overlaps between these mechanisms. The research provides domain-specific cost-accuracy Pareto frontiers to guide practical LLM deployment decisions.

**Note:** The webpage content provided does not include reviewer comments, scores, strengths, weaknesses, or detailed questions—only the paper's abstract, metadata, and publication details.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "34a4cfca-bb7b-4861-8973-d67df4d4e0fe",
  "isSidechain": true,
  "promptId": "295c0657-e121-425c-967b-f63279f1549e",
  "agentId": "a5512f66970097acf",
  "type": "user",
  "uuid": "0db74dae-007b-45a6-b633-d8b56691a17b",
  "sourceToolAssistantUUID": "34a4cfca-bb7b-4861-8973-d67df4d4e0fe",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "393d191a-0034-4130-a331-edb9d3156024",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 36 · 2026-05-29T10:07:53.659Z_

Now I have comprehensive information about the paper. Let me search one more time specifically for NAACL 2025 reviews, since NAACL uses ARR (ACL Rolling Review) on OpenReview.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0db74dae-007b-45a6-b633-d8b56691a17b",
  "isSidechain": true,
  "agentId": "a5512f66970097acf",
  "requestId": "req_011CbWg83GWtVWtiqMHir1v3",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "2a08cedf-30d7-405d-a33b-b5af63c456d5",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "393d191a-0034-4130-a331-edb9d3156024",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CdykmptK9FVaAexkea6cou",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 15654,
      "cache_read_input_tokens": 29148,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 15654,
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

_source line 37 · 2026-05-29T10:07:54.650Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01JQ5ZeNmt6arzdnhLDsa1VM`</summary>

```json
{
  "query": "ACL Rolling Review openreview \"Scaling LLM Inference\" \"sample compute\" Zhang Zhou Wang Li"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2a08cedf-30d7-405d-a33b-b5af63c456d5",
  "isSidechain": true,
  "agentId": "a5512f66970097acf",
  "requestId": "req_011CbWg83GWtVWtiqMHir1v3",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "77542604-5350-4afe-b393-c3b29179fb5e",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "393d191a-0034-4130-a331-edb9d3156024",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CdykmptK9FVaAexkea6cou",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 15654,
      "cache_read_input_tokens": 29148,
      "output_tokens": 122,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 15654
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 122,
          "cache_read_input_tokens": 29148,
          "cache_creation_input_tokens": 15654,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 15654,
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

_source line 38 · 2026-05-29T10:08:01.899Z_

<details><summary>↩ Tool result · `toolu_01JQ5ZeNmt6arzdnhLDsa1VM`</summary>

```text
Web search results for query: "ACL Rolling Review openreview "Scaling LLM Inference" "sample compute" Zhang Zhou Wang Li"

Links: [{"title":"Scaling LLM Inference Efficiently with Optimized Sample Compute Allocation - ACL Anthology","url":"https://aclanthology.org/2025.naacl-long.404/"},{"title":"Scaling LLM Inference with Optimized Sample Compute Allocation","url":"https://arxiv.org/pdf/2410.22480"},{"title":"Scaling LLM Test-Time Compute Optimally Can be More Effective than Scaling Parameters for Reasoning | OpenReview","url":"https://openreview.net/forum?id=4FWAwZtd2n"},{"title":"Scaling LLM Inference Efficiently with Optimized Sample ...","url":"https://aclanthology.org/2025.naacl-long.404.pdf"},{"title":"Improving LLM Reasoning through Scaling Inference Computation with Collaborative Verification | OpenReview","url":"https://openreview.net/forum?id=Qyile3DctL"},{"title":"The Art of Scaling Test-Time Compute for Large Language Models","url":"https://arxiv.org/pdf/2512.02008"},{"title":"Inference Scaling Laws: An Empirical Analysis of Compute-Optimal   Inference for Problem-Solving with Language Models","url":"https://arxiv.org/pdf/2408.00724"},{"title":"Accepted Papers - NAACL-HLT 2025","url":"https://2025.naacl.org/program/accepted_papers/"}]

Based on the search results, I found the paper you're looking for:

"Scaling LLM Inference Efficiently with Optimized Sample Compute Allocation" by Kexun Zhang, Shang Zhou, Danqing Wang, William Yang Wang, and Lei Li, published in the Proceedings of the 2025 Conference of the Nations of the Americas Chapter of the Association for Computational Linguistics: Human Language Technologies (NAACL 2025).

The paper addresses sampling in large language models, focusing on how to sample correct trajectories within a given compute budget for reinforcement learning rollouts and meta generation algorithms such as Best-of-N.

The paper has been accepted to NAACL 2025 and is also available on arXiv. You can find the full paper at the ACL Anthology (aclanthology.org/2025.naacl-long.404/) or on arXiv (arxiv.org/pdf/2410.22480).


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "77542604-5350-4afe-b393-c3b29179fb5e",
  "isSidechain": true,
  "promptId": "295c0657-e121-425c-967b-f63279f1549e",
  "agentId": "a5512f66970097acf",
  "type": "user",
  "uuid": "43080ef3-a669-43d3-a00b-24e203d115fe",
  "sourceToolAssistantUUID": "77542604-5350-4afe-b393-c3b29179fb5e",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "393d191a-0034-4130-a331-edb9d3156024",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 39 · 2026-05-29T10:09:43.838Z_

I now have thorough information about the paper. Here is my detailed analysis.

---

## Detailed Analysis: "Scaling LLM Inference with Optimized Sample Compute Allocation" (OSCA)

**Authors:** Kexun Zhang (CMU), Shang Zhou (UC San Diego), Danqing Wang (CMU), William Yang Wang (UC Santa Barbara), Lei Li (CMU)
**Venue:** NAACL 2025 (Albuquerque, NM), pages 7959-7973
**DOI:** 10.18653/v1/2025.naacl-long.404
**Code:** https://github.com/LeiLiLab/OSCA

---

### 1. The Gap They Identified and HOW

The paper identifies a gap at the intersection of two prior lines of work:

**Prior Work Line 1 -- Hyperparameter search for a single optimal configuration:** Wang et al. (2023b) proposed EcoOptiGen to find the single best inference hyperparameter set (temperature, model, prompt) under a compute budget. Wang et al. (2024) fine-tuned LLMs to self-regularize with the best hyperparameter set. These approaches all converge on a **pure allocation** -- spending 100% of the compute budget on one configuration.

**Prior Work Line 2 -- Inference scaling studies:** AlphaCode (Li et al., 2022), Brown et al. (2024, "Large Language Monkeys"), Wu et al. (2024), and Snell et al. (2024) study how accuracy scales with the number of samples or the type of inference-time algorithm. But they do not explore mixing configurations -- they scale up a single fixed sampling setup.

**The specific gap:** Nobody had formulated the question "given a fixed compute budget, how should we *distribute* samples across multiple inference configurations (different models, temperatures, languages, prompts) to maximize pass@C?" Prior work chose *one* configuration; this paper shows that *mixing* configurations and *optimizing the mixture* yields dramatically better compute efficiency.

They demonstrated this gap empirically in Figure 1: on LiveCodeBench, a naive uniform mixed allocation achieves 64% accuracy with just 4 samples, while the optimal *pure* allocation needs 16x more samples (64 samples) to reach similar accuracy. This was the smoking gun that motivated the paper.

---

### 2. The Key Insight Others Missed

**"Not all problems require the same optimal sampling configuration."**

The core insight is that different problems within a benchmark are best solved by different configurations. Some problems benefit from high temperature (more exploration), others from low temperature (more precision). Some are better solved by one model, others by another. When you commit all compute to a single configuration, you optimize for one problem type at the expense of others.

The mathematical intuition is demonstrated with their worked example (Section 3.2): Given two problems where h1 solves x1 with p=10% but x2 with p=1%, and h2 is the reverse -- a pure allocation using all 10 samples on h1 yields expected pass@10 of 37.3%, while splitting 5/5 between h1 and h2 yields **43.8%**. The mixed allocation exploits the complementarity of configurations.

This is a classic portfolio diversification argument, but nobody had applied it to LLM inference configurations.

---

### 3. How They Formulated the Problem Differently

They formulated sample compute allocation as a **constrained optimization problem over integer allocations**:

**Decision variable:** An allocation pi: H -> N, mapping each configuration h_i to a number of samples pi_i.

**Objective:**
```
max_pi  E[pass@C] = (1/|D|) * sum_j [1 - prod_i (1 - p_ij)^{pi_i}]
```

**Constraints:**
- 0 <= pi_i <= C for all i
- sum_i pi_i = C
- pi_i in N (integers)

Where p_ij is the probability that configuration h_i solves problem x_j (estimated from training data).

**Critical theoretical contribution:** They proved (Appendix A.1) that the relaxed continuous version of this problem is **convex**. The proof works by showing that the objective (in its minimization form) is a sum of exponentials of affine functions of pi, which is convex. This convexity guarantee means hill climbing on the relaxed problem will find the global optimum, justifying their simple optimization algorithm.

**The two-phase approach:**
1. **EstimatePassProb:** Sample C_0 times per (configuration, problem) pair to build a probability matrix P of size |H| x |D|
2. **OptimizeAllocation:** Hill climbing -- start from random allocation, iteratively move one sample unit between configurations if it improves the objective, until convergence

This is notably **not instance-level** -- the allocation pi is the same for all test problems. They explicitly tested instance-level allocation via k-NN and showed it performs *worse* (Table 4), justifying the domain-level approach.

---

### 4. Existing Techniques Adapted/Combined/Simplified

OSCA is remarkably simple in terms of algorithmic machinery:

- **Monte Carlo estimation** for pass probabilities (frequency of correct solutions in C_0 samples)
- **Hill climbing** (from Russell & Norvig) for discrete optimization on a convex landscape
- **pass@k metric formulation** from Chen et al. (2021) -- the standard code generation evaluation framework
- **Agentless framework** (Xia et al., 2024) for the SWE-Bench experiments -- they plugged OSCA into one step of an existing agentic workflow

The novelty is not in any individual component but in:
1. The problem formulation itself (mixed allocation over configurations)
2. The convexity proof justifying simple optimization
3. The empirical demonstration across diverse benchmarks

They also handled fractional scores (not just binary pass/fail) with an extension in Appendix A.4 using PMF-based computation for expected maximum scores.

---

### 5. Main Experimental Findings (Specific Numbers)

#### LiveCodeBench (Code Generation, 205 test problems)
- Configurations: GPT-4o, temperatures 0-1.6 (multiples of 0.2), Python + C++
- C_0 = 50

| Budget C | Default Pure | Optimal Pure | Uniform Mixed | OSCA Learned |
|----------|-------------|-------------|--------------|-------------|
| 2 (2^1)  | 47.1%       | +1.8%       | +4.3%        | **+17.4%**  |
| 16 (2^4) | 53.9%       | +6.6%       | +24.4%       | **+25.2%**  |
| 256 (2^8)| 59.5%       | +8.4%       | +27.6%       | **+27.2%**  |

**Headline result:** OSCA achieves accuracy better than the best single configuration with **128x less compute**.

Key finding: On code generation, even uniform mixed allocation dramatically outperforms optimal pure (pass@8 of 73.3% for uniform vs. needing 512 samples for optimal pure to match). Code problems benefit hugely from diverse solution strategies.

#### LiveBench (4 Reasoning Tasks, 471 test problems)
- Configurations: Llama3-70B, Qwen2-70B, DeepSeek-70B, temperatures 0-1.8
- C_0 = 50

| Budget C | Default Pure | Optimal Pure | Uniform Mixed | OSCA Learned |
|----------|-------------|-------------|--------------|-------------|
| 8 (2^3)  | 55.9%       | +9.3%       | +3.1%        | **+11.1%**  |
| 32 (2^5) | 62.6%       | +11.2%      | +10.5%       | **+13.0%**  |
| 256 (2^8)| 68.3%       | +14.7%      | +12.8%       | **+14.7%**  |

**Headline result:** OSCA achieves 25x compute savings on reasoning tasks. With 8 samples, OSCA's 67% pass rate exceeds default pure's pass rate at 128 samples.

Critical finding: On LiveBench, uniform mixed allocation does **not** outperform optimal pure (unlike LiveCodeBench). This validates that optimization of the mixture is essential -- naive uniform mixing is insufficient for heterogeneous problem domains.

#### SWE-Bench Lite (Agentic Task, 150 test problems)
- Configurations: GPT-4o, DeepSeek-Coder-2.5, Qwen-2.5-70B; temperatures 0.4/0.8/1.2/1.6; 2 prompt sets
- C_0 = C = 16 (smaller due to cost)

OSCA achieved **better accuracy with 3x less compute** than the default configuration when applied to the patch generation step of the Agentless workflow.

#### Ablation Results on LiveBench
- **Training data:** Full training data nearly matches the upper bound (training on test set). With reduced data, performance degrades mainly at large C (>2^6), suggesting overfitting on hard problems.
- **Estimation budget C_0:** Even at 26% of original C_0, OSCA maintains near-optimal performance -- robust to estimation noise.
- **Banning multiple temperatures:** Accuracy drops below optimal pure -- temperature diversity is critical.
- **Banning multiple models:** Accuracy drops to optimal pure level -- model diversity is important but temperature diversity matters more.
- **Domain specificity (Table 3):** OSCA is best in 7/12 (task x budget) settings and second-best in the remaining 5 across the 4 LiveBench subtasks.
- **Instance-level k-NN allocation (Table 4):** k-NN at k=64 achieves 86.2% at budget 2^7 vs. OSCA's 86.7%. Instance-specific allocation is suboptimal compared to domain-level optimization, likely because per-instance estimation is too noisy.

---

### 6. Reviewer Comments

I was unable to locate the formal peer review comments. NAACL 2025 uses ACL Rolling Review (ARR) on OpenReview, but the specific submission page for this paper was not publicly indexed or accessible in my searches. The paper was accepted as a long paper (pages 7959-7973), which indicates it passed full peer review. The Moonlight and HuggingFace pages contained only AI-generated summaries, not actual reviewer feedback.

**Inferred likely praise** (based on the paper's strengths):
- Clean problem formulation with theoretical backing (convexity proof)
- Impressive headline numbers (128x, 25x, 3x compute savings)
- Practical applicability demonstrated across code, reasoning, and agentic tasks
- Thorough ablations addressing natural follow-up questions
- Released code and generations

**Inferred likely criticisms** (based on visible limitations):
- The compute budget definition uses sample count, which is an imperfect proxy when models have vastly different costs/sizes
- Only 4 hyperparameter dimensions explored (model, temperature, language, prompt); no top-k, top-p, repetition penalty
- Maximum budget tested was only 512 samples
- The allocation is domain-level, not instance-level -- a reviewer likely asked about this (they address it in Table 4)
- The convexity guarantee is for the relaxed continuous problem, not the integer program they actually solve
- SWE-Bench experiments are limited (C_0 = C = 16, only 150 test problems)

---

### 7. Limitations and Open Questions

**Stated limitations:**
1. Only 4 hyperparameter dimensions (model, temperature, language, prompt). Adding top-k, top-p, repetition penalty could expand the configuration space.
2. Maximum compute budget of 512 -- unclear how the method scales to much larger budgets.
3. Compute-intensive estimation phase: need C_0 samples per (configuration, problem) pair on the training set.

**Unstated but important open questions:**
1. **Non-uniform sample costs:** When models differ significantly in cost (e.g., GPT-4o vs. a 7B model), the sample-count budget is misleading. They acknowledge this and note the formulation can accommodate cost coefficients without breaking convexity, but do not experiment with it.
2. **Dynamic/adaptive allocation:** The allocation is static -- every test problem gets the same pi. An adaptive approach that adjusts allocation based on partial observations (e.g., first few samples reveal the problem is "easy") could be more efficient.
3. **Interaction with verification/ranking:** OSCA optimizes pass@C (any-correct), but in practice you need to select one solution. How does OSCA interact with reward models or verifiers for best-of-N?
4. **Transfer across time/distribution shift:** LiveCodeBench uses temporal splits, but how robust is the allocation when the test distribution shifts significantly?
5. **Scaling beyond sampling:** How does mixed allocation interact with tree search, MCTS, or iterative refinement where sampling is just one sub-operation?
6. **Per-problem difficulty-aware allocation:** Damani et al. (2024) allocate compute based on problem difficulty estimation. Combining difficulty-aware per-problem budgets with OSCA's cross-configuration allocation could be complementary.

---

### 8. Reusable Building Blocks for Our K-d Optimization

This paper is highly relevant to K-d configuration optimization. Key reusable elements:

**Methods:**
- **The mixed allocation formulation itself:** The idea that pi should be a distribution over configurations, not a single point, directly applies to any setting where you search over discrete inference configurations.
- **The convexity result:** The proof that the relaxed pass@C maximization is convex (as a sum of exp-of-linear forms) can be reused for any setting with independent Bernoulli success probabilities across configurations.
- **Hill climbing with unit moves:** The neighbor-search algorithm (move 1 sample from config i to config j) is simple, efficient, and theoretically grounded. It scales as O(m^2) per iteration where m is the number of configurations.
- **Probability matrix estimation:** The empirical estimation of p_ij via frequency counting with a small C_0 is a practical and robust approach (shown to work even at 26% of the original C_0).

**Datasets/Benchmarks:**
- **LiveCodeBench** (305 train / 205 test coding problems, temporal split)
- **LiveBench** (201 train / 471 test, 4 reasoning categories, random split)
- **SWE-Bench Lite** (150 train / 150 test real-world SE issues)

**Frameworks:**
- **Agentless** (Xia et al., 2024) for SWE-Bench experiments
- Code released at https://github.com/LeiLiLab/OSCA

**Key practical parameters for reproduction:**
- C_0 = 50 for estimation on single-turn tasks
- C_0 = 16 for agentic tasks (cost constraints)
- Temperature grid: multiples of 0.2 from 0 to 1.6 (LiveCodeBench) or 0 to 1.8 (LiveBench)
- Models used: GPT-4o, Llama3-70B, Qwen2-70B, DeepSeek-70B/DeepSeek-Coder-2.5

---

### Relevance to Our Work

The OSCA formulation is essentially solving the same core problem as K-d optimization: given a discrete set of inference configurations and a fixed compute budget, find the optimal allocation. The key differences to consider:

1. OSCA assumes **independent** Bernoulli success across configurations for the same problem. If our K-d settings have correlated failures (e.g., similar models fail on the same inputs), the product-of-failure-probabilities assumption in Equation 3 may overestimate the benefit of mixing.
2. OSCA's allocation is **uniform across test instances** -- the same pi for every problem. If our setting allows per-instance adaptation, we could potentially do better (though OSCA's k-NN experiment suggests this is hard).
3. The convexity result is specific to the pass@C (any-correct) objective. If our objective function is different (e.g., expected reward, ranked output quality), the convexity guarantee may not hold and the hill-climbing approach may need modification.

Sources:
- [ACL Anthology - NAACL 2025 Paper](https://aclanthology.org/2025.naacl-long.404/)
- [arXiv Abstract](https://arxiv.org/abs/2410.22480)
- [arXiv Full HTML](https://arxiv.org/html/2410.22480)
- [HuggingFace Paper Page](https://huggingface.co/papers/2410.22480)
- [NAACL 2025 Accepted Papers](https://2025.naacl.org/program/accepted_papers/)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "43080ef3-a669-43d3-a00b-24e203d115fe",
  "isSidechain": true,
  "agentId": "a5512f66970097acf",
  "requestId": "req_011CbWg8usYfzdFWbL5KbJWS",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "dfb3f924-a3d6-45b9-a21d-348571baebb5",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "393d191a-0034-4130-a331-edb9d3156024",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BTmN9Dr1PULdqqRBo6cTE2",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 869,
      "cache_read_input_tokens": 44802,
      "output_tokens": 4137,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 869
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 4137,
          "cache_read_input_tokens": 44802,
          "cache_creation_input_tokens": 869,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 869,
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
