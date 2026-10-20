# Research conversation: I need to find and read the paper "Navigating by Old Maps" by Chen et al. (arXiv 2605.06076, May 7, 2026) about Transfor

**Multi-Class Annotation Errors in Causal Inference: Topology-Dependent Bias, Sensitivity, and Correction (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 29
- **Recorded user turns:** 1
- **Tool calls:** 10
- **Original source:** `logs/chats/exported-trajectories/account-2/agent-af045b478874480c9.jsonl`
- **Structured JSON:** [`43d76460b3ec5e7e4d67.json`](../../sessions/43/43d76460b3ec5e7e4d67.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

29 recorded events

### User

_source line 1 · 2026-05-19T12:04:20.189Z_

I need to find and read the paper "Navigating by Old Maps" by Chen et al. (arXiv 2605.06076, May 7, 2026) about Transformer circuits undergoing "Free Evolution" during SFT. 

Search for this paper using multiple approaches:
1. Search arxiv for "Navigating by Old Maps" Chen 2605.06076
2. Search for "Free Evolution" transformer circuits SFT
3. Search for "circuit temporal evolution" or "circuit stability training"

For each paper found, use WebFetch to read the abstract and key sections. I need to understand:
- What is "Free Evolution" in the context of circuits?
- What are the "Circuit Distance/Stability/Conflict metrics" they propose?
- What is the "Locate-then-Update" framework?
- How do they show that circuits extracted at one checkpoint become "temporally outdated"?
- What are their key experimental findings about circuit change during SFT?
- What model sizes and tasks do they study?

Be thorough - this is a critical issue for my research proposal about tracking calibration circuits across post-training stages.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "4ded1197-994d-445a-b6d7-39fbfd900429",
  "agentId": "af045b478874480c9",
  "type": "user",
  "uuid": "7b84d838-d892-4762-8314-1a5c9a8a6ea5",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "f997c3df-2e9d-4031-b144-f643e039c80c",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 2 · 2026-05-19T12:04:20.193Z_

```json
{
  "parentUuid": "7b84d838-d892-4762-8314-1a5c9a8a6ea5",
  "isSidechain": true,
  "agentId": "af045b478874480c9",
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
      "TaskStop",
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
      "TaskStop",
      "WebFetch",
      "WebSearch"
    ],
    "removedNames": [],
    "readdedNames": []
  },
  "type": "attachment",
  "uuid": "9ac3d95e-e7f2-42d8-b6af-b6d99b7602d8",
  "timestamp": "2026-05-19T12:04:20.193Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "f997c3df-2e9d-4031-b144-f643e039c80c",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 3 · 2026-05-19T12:04:20.194Z_

```json
{
  "parentUuid": "9ac3d95e-e7f2-42d8-b6af-b6d99b7602d8",
  "isSidechain": true,
  "agentId": "af045b478874480c9",
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "476fc6cb-9507-45cb-aef8-2f701d47b120",
  "timestamp": "2026-05-19T12:04:20.194Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "f997c3df-2e9d-4031-b144-f643e039c80c",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Assistant

_source line 4 · 2026-05-19T12:04:23.328Z_



I'll search for this paper using multiple approaches. Let me first load the WebSearch and WebFetch tools.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "476fc6cb-9507-45cb-aef8-2f701d47b120",
  "isSidechain": true,
  "agentId": "af045b478874480c9",
  "requestId": "req_011CbBtv9zC2KFbbvkoCDyyp",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "e335c51c-5a4e-4344-9d25-3752c4be27c8",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "f997c3df-2e9d-4031-b144-f643e039c80c",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018WPiyJ4voiD4y9GYWAm449",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 9366,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 9366,
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

_source line 5 · 2026-05-19T12:04:23.604Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01WHKsy832UTr9fbMRvbQjox`</summary>

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
  "parentUuid": "e335c51c-5a4e-4344-9d25-3752c4be27c8",
  "isSidechain": true,
  "agentId": "af045b478874480c9",
  "requestId": "req_011CbBtv9zC2KFbbvkoCDyyp",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "76ff4d8e-49df-45ba-a648-ab7bd4e941b5",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "f997c3df-2e9d-4031-b144-f643e039c80c",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018WPiyJ4voiD4y9GYWAm449",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 9366,
      "cache_read_input_tokens": 0,
      "output_tokens": 104,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 9366
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 104,
          "cache_read_input_tokens": 0,
          "cache_creation_input_tokens": 9366,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 9366,
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

_source line 6 · 2026-05-19T12:04:23.609Z_

<details><summary>↩ Tool result · `toolu_01WHKsy832UTr9fbMRvbQjox`</summary>

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
  "parentUuid": "76ff4d8e-49df-45ba-a648-ab7bd4e941b5",
  "isSidechain": true,
  "promptId": "4ded1197-994d-445a-b6d7-39fbfd900429",
  "agentId": "af045b478874480c9",
  "type": "user",
  "uuid": "4c5e2a11-9642-4c4b-96aa-5b2967f02eca",
  "sourceToolAssistantUUID": "76ff4d8e-49df-45ba-a648-ab7bd4e941b5",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "f997c3df-2e9d-4031-b144-f643e039c80c",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 7 · 2026-05-19T12:04:26.191Z_



Now let me search for this paper using all three approaches in parallel.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4c5e2a11-9642-4c4b-96aa-5b2967f02eca",
  "isSidechain": true,
  "agentId": "af045b478874480c9",
  "requestId": "req_011CbBtvR1KZzrKUQc4Mnaq8",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "f7477204-834f-4ce6-94d6-be20150552d7",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "f997c3df-2e9d-4031-b144-f643e039c80c",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SfY9sLLafXxdECumA29rgw",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1126,
      "cache_read_input_tokens": 9366,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1126,
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

_source line 8 · 2026-05-19T12:04:26.671Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01B2Yzv12Vc3Ag8wd7K7wQwo`</summary>

```json
{
  "query": "\"Navigating by Old Maps\" Chen 2605.06076 arXiv"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f7477204-834f-4ce6-94d6-be20150552d7",
  "isSidechain": true,
  "agentId": "af045b478874480c9",
  "requestId": "req_011CbBtvR1KZzrKUQc4Mnaq8",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "c4c2e08a-a910-4d74-9d6e-826fd694d253",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "f997c3df-2e9d-4031-b144-f643e039c80c",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SfY9sLLafXxdECumA29rgw",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1126,
      "cache_read_input_tokens": 9366,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1126,
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

_source line 9 · 2026-05-19T12:04:27.145Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_016DhPQRwLsJxK486Qm62DML`</summary>

```json
{
  "query": "\"Free Evolution\" transformer circuits SFT supervised fine-tuning 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c4c2e08a-a910-4d74-9d6e-826fd694d253",
  "isSidechain": true,
  "agentId": "af045b478874480c9",
  "requestId": "req_011CbBtvR1KZzrKUQc4Mnaq8",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "49e8a353-9d3d-4334-a31f-15ff250f0a43",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "f997c3df-2e9d-4031-b144-f643e039c80c",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SfY9sLLafXxdECumA29rgw",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1126,
      "cache_read_input_tokens": 9366,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1126,
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

_source line 10 · 2026-05-19T12:04:27.707Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01HKUqmcWCsENf4PUL6PzmWj`</summary>

```json
{
  "query": "circuit temporal evolution stability training transformer arXiv 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "49e8a353-9d3d-4334-a31f-15ff250f0a43",
  "isSidechain": true,
  "agentId": "af045b478874480c9",
  "requestId": "req_011CbBtvR1KZzrKUQc4Mnaq8",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "7e998849-9b86-4576-b4ce-00392738d740",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "f997c3df-2e9d-4031-b144-f643e039c80c",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SfY9sLLafXxdECumA29rgw",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1126,
      "cache_read_input_tokens": 9366,
      "output_tokens": 183,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1126
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 183,
          "cache_read_input_tokens": 9366,
          "cache_creation_input_tokens": 1126,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1126,
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

_source line 11 · 2026-05-19T12:04:32.640Z_

<details><summary>↩ Tool result · `toolu_01B2Yzv12Vc3Ag8wd7K7wQwo`</summary>

```text
Web search results for query: ""Navigating by Old Maps" Chen 2605.06076 arXiv"

Links: [{"title":"[2605.06076] Navigating by Old Maps: The Pitfalls of Static Mechanistic Localization in LLM Post-Training","url":"https://arxiv.org/abs/2605.06076"},{"title":"Navigating by Old Maps: The Pitfalls of Static Mechanistic Localization in LLM Post-Training","url":"https://arxiv.org/html/2605.06076"},{"title":"Navigating by Old Maps: The Pitfalls of Static","url":"https://arxiv.org/pdf/2605.06076"},{"title":"Emergence of Maps in the Memories of Blind Navigation Agents","url":"https://arxiv.org/pdf/2301.13261"},{"title":"Navigating in Virtual Environments: Does a Map or a Map-Based Description Presented Beforehand Help?","url":"https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8230476/"}]

Based on the search results, I found the paper you're looking for:

"Navigating by Old Maps: The Pitfalls of Static Mechanistic Localization in LLM Post-Training" is by Hang Chen and 5 other authors. The paper was submitted on 7 May 2026.

The paper investigates the "Locate-then-Update" paradigm in large language model post-training, which uses mechanistic interpretability to identify critical components for targeted parameter updates. However, it examines the fundamental assumption of whether mechanisms derived from current static parameters can reliably guide future dynamic parameter updates.

The authors introduce three novel metrics—Circuit Distance, Circuit Stability, and Circuit Conflict—to analyze circuit evolution across three dimensions: neural migration, semantic stability, and cross-task interference. Their empirical results reveal that circuits inherently exhibit "Free Evolution" during parameter updates.

You can access the full paper at: https://arxiv.org/abs/2605.06076


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c4c2e08a-a910-4d74-9d6e-826fd694d253",
  "isSidechain": true,
  "promptId": "4ded1197-994d-445a-b6d7-39fbfd900429",
  "agentId": "af045b478874480c9",
  "type": "user",
  "uuid": "9117bacc-6b44-4672-9d44-04afabef2da5",
  "sourceToolAssistantUUID": "c4c2e08a-a910-4d74-9d6e-826fd694d253",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "f997c3df-2e9d-4031-b144-f643e039c80c",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-19T12:04:34.096Z_

<details><summary>↩ Tool result · `toolu_016DhPQRwLsJxK486Qm62DML`</summary>

```text
Web search results for query: ""Free Evolution" transformer circuits SFT supervised fine-tuning 2026"

Links: [{"title":"How to Fine-Tune LLMs in 2026: Costs, GPUs, and Code | Spheron Blog","url":"https://www.spheron.network/blog/how-to-fine-tune-llm-2026/"},{"title":"Data Repetition Beats Data Scaling in Long-CoT Supervised Fine-Tuning","url":"https://arxiv.org/pdf/2602.11149"},{"title":"Supervised Fine-Tuning (SFT) | MindSpore Transformers master documentation | MindSpore","url":"https://www.mindspore.cn/mindformers/docs/en/master/guide/supervised_fine_tuning.html"},{"title":"Eliciting Fine-Tuned Transformer Capabilities via Inference-Time Techniques","url":"https://arxiv.org/pdf/2506.08060"},{"title":"Transformers with RL or SFT Provably Learn Sparse Boolean Functions, But Differently","url":"https://arxiv.org/pdf/2511.17852"},{"title":"FisherSFT: Data-Efficient Supervised Fine-Tuning of Language Models Using Information Gain","url":"https://arxiv.org/pdf/2505.14826"},{"title":"Supervised Fine-Tuning (SFT) | huggingface/trl | DeepWiki","url":"https://deepwiki.com/huggingface/trl/3-supervised-fine-tuning-(sft)"},{"title":"SRFT: A Single-Stage Method with Supervised and Reinforcement Fine-Tuning for Reasoning","url":"https://arxiv.org/pdf/2506.19767"},{"title":"SED-SFT: Selectively Encouraging Diversity in Supervised Fine-Tuning","url":"https://arxiv.org/pdf/2602.07464"}]

Based on the search results, I found several relevant papers and resources from 2026 related to transformer circuits, SFT (supervised fine-tuning), and related techniques:

**Key findings:**

1. **SFT Evolution in 2026**: GRPO has replaced pure supervised fine-tuning as the hot technique, whereas in 2023, everyone talked about SFT (Supervised Fine-Tuning).

2. **Data Repetition Research**: For reasoning-focused models, post-training typically begins with supervised fine-tuning (SFT) on long Chain-of-Thought (CoT) demonstrations, with research showing that training for many epochs on a small random subset of SFT data can substantially reduce compute while improving downstream reasoning performance.

3. **Transformer Circuits and Inference-Time Techniques**: A recent paper formally proves that capabilities acquired through SFT can be approximated by a base transformer model using inference-time techniques, specifically in-context learning (ICL), without altering model parameters, under idealized assumptions.

4. **Learning Mechanisms**: Supervised fine-tuning (SFT) involves training transformers to minimize a loss over pairs of inputs and labeled outputs, but is restricted by the demand of a large amount of labeled CoT data.

5. **Integrated Approaches**: Recent work has shown a movement towards integrated frameworks that unify SFT and RL paradigms, or dynamically switch between the two fine-tuning methods during the LLM training process.

However, I did not find results specifically about a paper or framework called "Free Evolution" in relation to transformer circuits. If you're looking for more specific information about that particular work, please let me know and I can search more specifically.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "49e8a353-9d3d-4334-a31f-15ff250f0a43",
  "isSidechain": true,
  "promptId": "4ded1197-994d-445a-b6d7-39fbfd900429",
  "agentId": "af045b478874480c9",
  "type": "user",
  "uuid": "9d17f37f-c5e7-4537-bbf4-4e16201b6ac6",
  "sourceToolAssistantUUID": "49e8a353-9d3d-4334-a31f-15ff250f0a43",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "f997c3df-2e9d-4031-b144-f643e039c80c",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 13 · 2026-05-19T12:04:41.524Z_

<details><summary>↩ Tool result · `toolu_01HKUqmcWCsENf4PUL6PzmWj`</summary>

```text
Web search results for query: "circuit temporal evolution stability training transformer arXiv 2026"

Links: [{"title":"Quantifying LLM Attention-Head Stability: Implications for Circuit Universality","url":"https://arxiv.org/pdf/2602.16740"},{"title":"Stabilizing Transformer Training by Preventing Attention Entropy   Collapse","url":"https://arxiv.org/pdf/2303.06296"},{"title":"[2601.22614] Stabilizing Transformer Training Through Consensus","url":"https://arxiv.org/abs/2601.22614"},{"title":"Stability of Transformers under Layer Normalization","url":"https://arxiv.org/pdf/2510.09904"},{"title":"An evolutionary perspective on modes of learning in Transformers","url":"https://arxiv.org/pdf/2505.09855"},{"title":"CircuitProbe: Predicting Reasoning Circuits in Transformers via Stability Zone Detection","url":"https://arxiv.org/pdf/2604.00716"}]

Based on the search results, I found several relevant papers on arXiv from 2026 related to transformers, stability, and circuit-like concepts:

**Most Relevant Results:**

1. "Quantifying LLM Attention-Head Stability: Implications for Circuit Universality" (February 20, 2026) - This paper appears to directly address circuit stability in transformers, examining whether transformers learn similar or different computational schemes.

2. "Stabilizing Transformer Training Through Consensus" (January 30, 2026) - Standard attention-based transformers exhibit instability under learning rate overspecification, and the consensus mechanism stabilizes transformer training across a wider effective range of learning rates.

3. "CircuitProbe: Predicting Reasoning Circuits in Transformers via Stability Zone Detection" - Transformer models appear to develop specialized "reasoning circuits" during training: contiguous blocks of layers that perform coherent cognitive operations.

4. "Stability of Transformers under Layer Normalization" - This paper theoretically analyzes how layer normalization placement affects Transformer stability during both evaluation and training.

5. "An evolutionary perspective on modes of learning in Transformers" - A Transformer initially reliant on prompts will consolidate capability into its weights under stable training conditions.

The search returned papers examining circuit properties, training stability, and temporal evolution of transformer internals, which align with your search query.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "7e998849-9b86-4576-b4ce-00392738d740",
  "isSidechain": true,
  "promptId": "4ded1197-994d-445a-b6d7-39fbfd900429",
  "agentId": "af045b478874480c9",
  "type": "user",
  "uuid": "d3e58e0b-62d1-4212-b6fb-4e22bb5442b9",
  "sourceToolAssistantUUID": "7e998849-9b86-4576-b4ce-00392738d740",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "f997c3df-2e9d-4031-b144-f643e039c80c",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 14 · 2026-05-19T12:04:44.270Z_

I found the paper. Now let me fetch the full content from multiple sources to get comprehensive details.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d3e58e0b-62d1-4212-b6fb-4e22bb5442b9",
  "isSidechain": true,
  "agentId": "af045b478874480c9",
  "requestId": "req_011CbBtwjBjmh1yEjKnQbMBP",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "19092642-059d-4bcf-bcdc-561adc121d62",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "f997c3df-2e9d-4031-b144-f643e039c80c",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NXQ7bxU41h69ueQrxDgEiW",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2221,
      "cache_read_input_tokens": 10492,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2221,
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

_source line 15 · 2026-05-19T12:04:46.138Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_015XYEJiP9WFa9HSiW2yDKbL`</summary>

```json
{
  "url": "https://arxiv.org/abs/2605.06076",
  "prompt": "Extract the complete abstract, author list, all section headings, and any summary information available on this page for the paper \"Navigating by Old Maps\". I need the full abstract text, the list of all authors and affiliations, and the structure of the paper."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "19092642-059d-4bcf-bcdc-561adc121d62",
  "isSidechain": true,
  "agentId": "af045b478874480c9",
  "requestId": "req_011CbBtwjBjmh1yEjKnQbMBP",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "c4aca63b-da7b-4214-a966-57589ead9402",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "f997c3df-2e9d-4031-b144-f643e039c80c",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NXQ7bxU41h69ueQrxDgEiW",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2221,
      "cache_read_input_tokens": 10492,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2221,
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

_source line 16 · 2026-05-19T12:04:48.762Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01NsESZAMYqVG3b5cS3XToc5`</summary>

```json
{
  "url": "https://arxiv.org/html/2605.06076",
  "prompt": "Extract ALL content from this paper. I need:\n1. The complete abstract\n2. All section headings and subheadings\n3. The definition of \"Free Evolution\" in the context of circuits\n4. The definitions and formulas for Circuit Distance, Circuit Stability, and Circuit Conflict metrics\n5. The \"Locate-then-Update\" framework explanation\n6. How circuits become \"temporally outdated\"\n7. All experimental details: model sizes, tasks, datasets\n8. Key experimental findings and results\n9. The conclusion and implications\nBe as thorough and detailed as possible - extract all technical content."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c4aca63b-da7b-4214-a966-57589ead9402",
  "isSidechain": true,
  "agentId": "af045b478874480c9",
  "requestId": "req_011CbBtwjBjmh1yEjKnQbMBP",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "7b813cfd-e838-4ac5-be8e-03ea722b8ecf",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "f997c3df-2e9d-4031-b144-f643e039c80c",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NXQ7bxU41h69ueQrxDgEiW",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2221,
      "cache_read_input_tokens": 10492,
      "output_tokens": 354,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2221
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 354,
          "cache_read_input_tokens": 10492,
          "cache_creation_input_tokens": 2221,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2221,
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

_source line 17 · 2026-05-19T12:04:56.911Z_

<details><summary>↩ Tool result · `toolu_015XYEJiP9WFa9HSiW2yDKbL`</summary>

```text
# Paper Summary: "Navigating by Old Maps"

## Abstract
The research challenges the "Locate-then-Update" approach in LLM post-training. The authors argue that "static mechanisms extracted from current states" cannot reliably guide future parameter updates. They introduce three metrics—Circuit Distance, Circuit Stability, and Circuit Conflict—to examine how Transformer circuits evolve during supervised fine-tuning. Their findings indicate circuits undergo "Free Evolution," making static mechanistic localization temporally inadequate for directing future training states.

## Authors
- Hang Chen
- Jiaying Zhu
- Hongyang Chen
- Hongxu Liu
- Xinyu Yang
- Wenya Wang

*Note: Author affiliations are not provided on this arXiv abstract page.*

## Document Structure
The page displays standard arXiv metadata including:
- Submission date: May 7, 2026
- Subject classification: Computation and Language (cs.CL)
- Paper length: 26 pages
- Available formats: PDF, HTML (experimental), TeX source
- DOI: https://doi.org/10.48550/arXiv.2605.06076

**Section headings beyond the abstract are not visible** on this abstract page. Full structural details would require accessing the complete PDF or HTML versions.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c4aca63b-da7b-4214-a966-57589ead9402",
  "isSidechain": true,
  "promptId": "4ded1197-994d-445a-b6d7-39fbfd900429",
  "agentId": "af045b478874480c9",
  "type": "user",
  "uuid": "076aa713-dff1-4a6f-adfb-d3ec9e49f080",
  "sourceToolAssistantUUID": "c4aca63b-da7b-4214-a966-57589ead9402",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "f997c3df-2e9d-4031-b144-f643e039c80c",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-19T12:05:00.000Z_

<details><summary>↩ Tool result · `toolu_01NsESZAMYqVG3b5cS3XToc5`</summary>

```text
# Summary of "Navigating by Old Maps: The Pitfalls of Static Mechanistic Localization in LLM Post-Training"

## Abstract
The paper challenges the "Locate-then-Update" paradigm in LLM post-training, questioning whether mechanistic interpretability findings from current parameters can reliably guide future parameter updates. The authors track circuit evolution during supervised fine-tuning using three novel metrics.

## Core Definitions

**Free Evolution**: The phenomenon where task-critical components naturally shift during parameter updates without localization constraints. Attention mechanisms exhibit drastic structural changes while MLP components remain relatively stable.

**Circuit Distance (CD)**: Measures component migration using Manhattan distance over computational graphs. Formula aggregates absolute shifts in causal effects: CD = Σ|I(Wi→Wj)^θ - I(Wi→Wj)^θ'| across all edges.

**Circuit Stability (CS)**: Quantifies knowledge consolidation via Spearman rank correlation between circuits from different dataset subsets. High stability indicates effective knowledge consolidation; low stability suggests ongoing refinement.

**Circuit Conflict (CC)**: Identifies shared critical components across multiple tasks' circuits using Boolean satisfiability. Computed as the minimum UNSAT core size when combining target and pervasiveness circuits.

## Locate-then-Update Framework
Two-step process: (1) mechanistic interpretability identifies critical components for target task; (2) non-critical components freeze, enabling targeted fine-tuning. The paper argues this approach suffers "temporal lag" because static circuits don't represent future parameter states.

## Experimental Setup
- **Models**: Mistral-7B, LLaMA3-8B
- **Tasks**: 15 datasets including Arithmetic, SST2, Winogrande, Bool, Gender, OpenBookQA
- **Duration**: 10 SFT epochs with 20 observation steps each
- **Strategies Compared**: Free evolution, mechanistic localization, random localization

## Key Findings

1. **Divergent Evolution Patterns**: Attention-dominated skill tasks experience drastic circuit migration; MLP-dominated knowledge tasks evolve gradually.

2. **Temporal Inadequacy**: Static mechanistic localization provides "no substantial advantage over random localization" on skill-centric tasks due to inherent circuit evolution.

3. **Illusion of Effectiveness**: Apparent successes in knowledge-editing applications stem from MLP stability masking the latency problem, not genuine mechanistic guidance.

4. **Predictive Alternative**: Using future circuits (from completed training) as localization targets substantially improves both target and pervasiveness task performance.

## Implications
The findings suggest mechanistic localization requires "foresight"—predictive capability regarding future mechanisms—rather than relying solely on current parameter snapshots.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "7b813cfd-e838-4ac5-be8e-03ea722b8ecf",
  "isSidechain": true,
  "promptId": "4ded1197-994d-445a-b6d7-39fbfd900429",
  "agentId": "af045b478874480c9",
  "type": "user",
  "uuid": "2bf43f80-6053-4a55-ad4c-52923823b0d3",
  "sourceToolAssistantUUID": "7b813cfd-e838-4ac5-be8e-03ea722b8ecf",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "f997c3df-2e9d-4031-b144-f643e039c80c",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 19 · 2026-05-19T12:05:03.253Z_

Good, I have substantial content. Let me now fetch more details from the HTML version to get the full technical depth, particularly on the metrics formulas, experimental results, and methodology.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2bf43f80-6053-4a55-ad4c-52923823b0d3",
  "isSidechain": true,
  "agentId": "af045b478874480c9",
  "requestId": "req_011CbBty696R3xEsKkf7Er87",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "379c5e1c-9fcb-4883-b22e-7d725538030b",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "f997c3df-2e9d-4031-b144-f643e039c80c",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014USAr7m92zRwpeDbaVM4cC",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1339,
      "cache_read_input_tokens": 12713,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1339,
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

_source line 20 · 2026-05-19T12:05:07.548Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01E5eVPEGbS97WSa13QCEQVX`</summary>

```json
{
  "url": "https://arxiv.org/html/2605.06076",
  "prompt": "Focus on sections 3 and 4 (or wherever the methodology and metrics are defined). Extract:\n1. The exact mathematical formulations for Circuit Distance, Circuit Stability, and Circuit Conflict\n2. How they extract circuits (what method - activation patching, causal tracing, etc.)\n3. The precise definition of \"computational graph\" they use\n4. How they define \"edges\" and \"nodes\" in the circuit\n5. What is the \"causal effect\" I(Wi->Wj) they reference?\n6. How do they measure circuit evolution over training steps?\n7. Any figures or tables describing the evolution patterns\nBe very precise about mathematical details."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "379c5e1c-9fcb-4883-b22e-7d725538030b",
  "isSidechain": true,
  "agentId": "af045b478874480c9",
  "requestId": "req_011CbBty696R3xEsKkf7Er87",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "fb6d6562-205e-4af2-b217-0afc58df3768",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "f997c3df-2e9d-4031-b144-f643e039c80c",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014USAr7m92zRwpeDbaVM4cC",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1339,
      "cache_read_input_tokens": 12713,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1339,
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

_source line 21 · 2026-05-19T12:05:11.371Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01FKoFvG3nTVHe8YrqVKkt1z`</summary>

```json
{
  "url": "https://arxiv.org/html/2605.06076",
  "prompt": "Focus on the experimental results sections (likely sections 5 and 6). Extract:\n1. Specific numerical results for Circuit Distance across training steps\n2. Comparison between attention heads vs MLP layers in terms of evolution\n3. The \"skill tasks\" vs \"knowledge tasks\" distinction and which datasets fall into each category\n4. Results showing mechanistic localization vs random localization vs free evolution\n5. The \"future circuit\" oracle experiment results\n6. Any ablation studies\n7. The specific 15 datasets used and how they were categorized\n8. Performance metrics and tables\n9. Key quantitative findings (percentages, correlation values, etc.)\nBe very detailed about numerical results."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "fb6d6562-205e-4af2-b217-0afc58df3768",
  "isSidechain": true,
  "agentId": "af045b478874480c9",
  "requestId": "req_011CbBty696R3xEsKkf7Er87",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "6d36b12d-59f0-4a86-9b30-600a0c12a7eb",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "f997c3df-2e9d-4031-b144-f643e039c80c",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014USAr7m92zRwpeDbaVM4cC",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1339,
      "cache_read_input_tokens": 12713,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1339,
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

_source line 22 · 2026-05-19T12:05:14.957Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01MSyPbPt6z6Fqm6uZ4Uxrrc`</summary>

```json
{
  "url": "https://arxiv.org/html/2605.06076",
  "prompt": "Focus on the introduction and related work sections. Extract:\n1. What specific prior work on \"Locate-then-Update\" do they cite? (e.g., knowledge editing papers, ROME, MEMIT, etc.)\n2. What mechanistic interpretability methods do they build on?\n3. Their specific research questions\n4. The motivation for studying circuit temporal evolution\n5. How they frame the gap in existing literature\n6. Any discussion of how this relates to knowledge editing, PEFT methods, or model surgery\n7. The conclusion section - what are their recommendations for future work?\nAlso extract any discussion of limitations."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6d36b12d-59f0-4a86-9b30-600a0c12a7eb",
  "isSidechain": true,
  "agentId": "af045b478874480c9",
  "requestId": "req_011CbBty696R3xEsKkf7Er87",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "ad73c2cf-348a-41b4-bd25-96874008ca57",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "f997c3df-2e9d-4031-b144-f643e039c80c",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014USAr7m92zRwpeDbaVM4cC",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1339,
      "cache_read_input_tokens": 12713,
      "output_tokens": 678,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1339
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 678,
          "cache_read_input_tokens": 12713,
          "cache_creation_input_tokens": 1339,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1339,
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

_source line 23 · 2026-05-19T12:05:20.122Z_

<details><summary>↩ Tool result · `toolu_01E5eVPEGbS97WSa13QCEQVX`</summary>

```text
# Methodology and Metrics Extraction: Circuit Evolution in LLM Post-Training

## 1. Mathematical Formulations for Core Metrics

### Circuit Distance (CD)
The paper defines CD as the Manhattan distance over causal effects across edges:

$$CD = D_{\mathcal{G}}(\mathcal{G}^\theta, \mathcal{G}^{\theta'}) = \sum_{(W_i,W_j \in \mathcal{E})} |I(W_i \to W_j)^\theta - I(W_i \to W_j)^{\theta'}|$$

where $I(W_i \to W_j)$ represents "the causal effect" quantifying edge importance through intervention-based measurement.

### Circuit Stability (CS)
Stability measures consistency across data subsets using Spearman rank correlation:

$$CS(\theta') = \mathbb{E}_{s,s' \in \mathcal{D}_t}[\rho(\mathcal{C}^{\theta'}_s, \mathcal{C}^{\theta'}_s')]$$

This evaluates whether "different sampled subsets of $\mathcal{D}_t$ yield significantly divergent circuits."

### Circuit Conflict (CC)
Conflict leverages logical circuit representations converted to Conjunctive Normal Form, using SAT solving:

$$CC(\theta) = \min_n \text{UNSAT}(\Phi_t^\theta \land \Phi_p^\theta)$$

where UNSAT computes "the minimum number of conflicting clauses."

## 2. Circuit Extraction Method

The paper employs **activation patching** (interchange ablation) for circuit discovery. An edge is retained when:

$$I(W_i \to W_j) = |\mathbb{L}(x|\text{do}(W_i \to W_j)) - \mathbb{L}(x)| > \tau$$

where $\text{do}(\cdot)$ represents "activation patching." The approach combines noising-based and denoising-based interventions to recover AND, OR, and ADDER logical gates completely.

## 3. Computational Graph Definition

The model is formalized as $\mathcal{M} = \langle \mathcal{G}, \theta \rangle$ where:
- $\mathcal{G} = \langle \mathcal{V}, \mathcal{E} \rangle$ represents "the computational graph" in the forward pass
- $\mathcal{V}$ comprises "all components (i.e., parameter matrices such as $W_q, W_k, W_v, W_o, W_{up}, W_{down}$)"
- $\mathcal{E}$ denotes "their activation connections"

## 4. Edges and Nodes Definition

**Nodes**: Individual parameter matrices including attention projections ($W_q, W_k, W_v, W_o$) and MLP weights ($W_{up}, W_{down}$), termed "the minimal update unit."

**Edges**: Directional connections between nodes (e.g., $W_o \to W_{up}$) representing "activation connections." The paper distinguishes between Attention and MLP components, observing that "Attention-driven skill tasks experience drastic structural shifts."

## 5. Causal Effect Measurement

The causal effect $I(W_i \to W_j)$ quantifies edge importance through intervention magnitude—specifically, "the output variance under causal interventions." When intervention exceeds threshold $\tau$, the edge is "deemed the most critical components."

## 6. Evolution Measurement Over Training

The paper tracks circuits at discrete SFT steps by:
- Extracting circuits at multiple checkpoints during 10 epochs (subdivided into 20 observation steps)
- Computing CD as differences between consecutive parameter states: $\mathcal{G}^\theta$ (initial) to $\mathcal{G}^{\theta_s}$ (current step)
- Computing CS across randomly sampled 20% subsets at each state

## 7. Key Evolution Patterns (Figures/Tables)

**Table 2** summarizes five factors influencing circuit evolution:
- Task Type: "Skill-centric tasks (Attention-dominated) are highly susceptible to component migration"
- Pervasiveness degree and dataset size increase migration
- Conflict proportion and initial mastery inversely affect stability

**Figure 2** demonstrates divergent patterns: "Attention components consistently exhibit significantly higher CD than MLP components throughout SFT," while stability metrics show the opposite trend, revealing that "skill-centric Attention circuits are highly volatile" versus knowledge-centric MLPs remaining "largely inert."
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "fb6d6562-205e-4af2-b217-0afc58df3768",
  "isSidechain": true,
  "promptId": "4ded1197-994d-445a-b6d7-39fbfd900429",
  "agentId": "af045b478874480c9",
  "type": "user",
  "uuid": "d779250b-e30e-4fbc-91bc-cb6ebb6d8b5d",
  "sourceToolAssistantUUID": "fb6d6562-205e-4af2-b217-0afc58df3768",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "f997c3df-2e9d-4031-b144-f643e039c80c",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 24 · 2026-05-19T12:05:26.846Z_

<details><summary>↩ Tool result · `toolu_01MSyPbPt6z6Fqm6uZ4Uxrrc`</summary>

```text
# Research Paper Analysis: Mechanistic Localization in LLM Post-Training

## 1. Prior Work on "Locate-then-Update" Paradigm

The authors cite several applications of this paradigm:
- **Knowledge editing**: Meng et al. (2022) "Locating and editing factual associations in GPT"
- **Model unlearning**: Wu et al. (2023) and Li et al. (2025) on "unlearning privacy neurons" and "skill unlearning through intervention"
- **Parameter editing**: Yao et al. (2023) on "Editing large language models"
- **Vector steering**: Cao et al. (2024) on "Personalized steering of LLMs"

Recent advances they reference include jointly considering target and pervasiveness tasks, ensembling multiple interpretability methods, and low-dimensional projections for unlearning.

## 2. Mechanistic Interpretability Methods

The paper emphasizes **circuit discovery** as their chosen technique, selecting it over alternatives because it:
- Better "deconfounds correlations" versus gradient/magnitude methods
- Captures "holistic mechanisms" versus causal interventions
- Provides "stronger theoretical foundations" versus probing approaches

They implement this through three approaches detailed in appendices:
- ACDC (greedy search)
- EAP (linear estimation)
- EdgePruning (differentiable masks)

## 3. Research Questions

**RQ1**: Do critical components change during parameter updates without localization, and if so, what patterns emerge?

**RQ2**: Does static localization actually improve target task performance and reduce conflicts with existing capabilities?

These decompose into sub-questions examining whether mechanisms evolve, underlying patterns, and influencing factors.

## 4. Motivation for Studying Circuit Temporal Evolution

The fundamental motivation stems from questioning a core assumption: "can mechanisms derived from current static parameters reliably guide future dynamic parameter updates?" The authors note that prior work raises concerns about mechanistic localization's "completeness" and "exclusiveness," prompting investigation into whether it functions merely as a "placebo."

## 5. Literature Gap Framing

The paper frames a critical disconnect: existing "locate-then-update" methods assume static interpretability findings can guide dynamic updates, yet no systematic study examines whether circuits actually remain stable during parameter modification. They highlight that recent studies question whether localization genuinely prevents conflicts or merely constrains natural mechanism evolution.

## 6. Connections to Related Areas

The paper discusses implications for:
- **Knowledge editing applications** where MLP-dominated tasks show stability
- **Model unlearning** where attention-driven skills exhibit volatility
- **PEFT methods** implicitly through parameter-constrained optimization
- The distinction between "skill-centric" (attention) and "knowledge-centric" (MLP) mechanisms affects all these domains

## 7. Future Work Recommendations

The conclusion advocates for "predictive localization" endowing mechanistic interpretation with "foresight"—the ability to forecast post-update circuits. They suggest:
- Using "future mechanistic localization" (circuits after free evolution) as surrogates
- Leveraging gradient signals to approximate or extrapolate future mechanistic structures
- Moving beyond circuit-centric approaches toward gradient-based methods

## 8. Limitations Discussion

Appendix G (referenced but not fully provided) addresses limitations. The paper notes their framework uses SFT as a representative post-training process, acknowledges this may not generalize equally to all optimization paradigms, and recognizes that computational constraints limited certain experimental scales.

---

**Key Insight**: The authors demonstrate that attention mechanisms undergo "drastic shifts" while MLP components remain "relatively stable," explaining why existing methods appear effective on knowledge-editing tasks but fail on skill-centric objectives—a critical distinction for practitioners designing localization strategies.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ad73c2cf-348a-41b4-bd25-96874008ca57",
  "isSidechain": true,
  "promptId": "4ded1197-994d-445a-b6d7-39fbfd900429",
  "agentId": "af045b478874480c9",
  "type": "user",
  "uuid": "52121c5b-fd2e-46f9-be50-50331fad8c31",
  "sourceToolAssistantUUID": "ad73c2cf-348a-41b4-bd25-96874008ca57",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "f997c3df-2e9d-4031-b144-f643e039c80c",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 25 · 2026-05-19T12:05:27.093Z_

<details><summary>↩ Tool result · `toolu_01FKoFvG3nTVHe8YrqVKkt1z`</summary>

```text
# Experimental Results Summary: Static Mechanistic Localization in LLM Post-Training

## Circuit Evolution Metrics

The paper introduces three novel metrics to track mechanism evolution:

1. **Circuit Distance (CD)**: Measures component migration using Manhattan distance across causal effects
2. **Circuit Stability (CS)**: Quantifies knowledge consolidation via Spearman's rank correlation between circuits from dataset subsets
3. **Circuit Conflict (CC)**: Uses SAT solving to identify mechanistic interference between tasks

## Free Evolution Results (Section 4.1)

### Attention vs MLP Differentiation
The research reveals stark contrasts in component behavior:

- **Attention layers** (Wq, Wk, Wv, Wo) exhibit "substantially higher Circuit Distance than MLP components throughout SFT"
- **MLP components** (Wup, Wdown) demonstrate minimal migration despite parameter updates
- MLP Circuit Stability "substantially exceeds Attention stability"

This pattern reflects mechanistic roles: attention handles inter-token "skills" while MLPs encode semantic "knowledge." The vastly larger parameter volume in MLPs makes stored information "more deeply entrenched and harder to migrate."

### Five Identified Factors Influencing Evolution

Table 2 summarizes key correlations:

| Factor | CD Attention | CD MLP | CS Attention | CS MLP |
|--------|-------------|--------|--------------|--------|
| Skill tasks | ↑ | — | ↓ | — |
| Knowledge tasks | — | ↓ | — | ↑ |
| Pervasiveness ↑ | ↑ | ↑ | ↓ | ↓ |
| Dataset size ↑ | — | — | ↑ | ↑ |
| Conflict ↑ | ↑ | ↑ | ↓ | ↓ |
| Mastered tasks | ↓ | ↓ | ↑ | ↑ |
| Unmastered tasks | ↑ | ↑ | ↓ | ↓ |

## Localization Evolution Results (Section 4.2)

### RQ2-a: Static Localization Efficacy

Testing three strategies on Arithmetic task with OpenBookQA as pervasiveness:

- **Mechanistic (Mech) vs Random**: "Mech strategy significantly outperforms the Free baseline in accuracy and maintains lower conflict level, yet exhibits no substantial advantage over Random strategy"
- **Circuit Conflict trends**: Both localization approaches reduce conflicts compared to free evolution, but mechanistic guidance provides no additional benefit
- **Surprising finding**: CD and CS metrics show "localization induces greater Circuit Distance and variations in Circuit Stability"

This demonstrates that "static mechanistic conclusions suffer from severe temporal latency."

### RQ2-b: The "Illusion of Effectiveness"

Unlearning experiments on WMDP-Bio (knowledge-centric) vs Induction (skill-centric):

**WMDP-Bio Results** (MLP-dominated):
- Forget efficacy: Mech=0.736 vs Random=0.716 vs Free=0.685
- CD_Attn: 1.0519 (Mech) vs 1.1243 (Random)
- CD_MLP: 0.7391 (Mech) vs 0.9557 (Random)

**Induction Results** (Attention-dominated):
- Forget efficacy: Mech=0.955 vs Random=0.952 vs Free=0.873
- CD_Attn: 1.5593 (Mech) vs 1.5866 (Random)
- Mech provides "no meaningful advantage" despite dominance on knowledge tasks

The stark difference reveals: "circuits of knowledge-centric tasks are largely composed of MLPs and their associated edges... highly resistant to neural migration" while skill-centric tasks undergo "drastic transformations."

## Future Mechanistic Localization (Section 5)

The oracle experiment using free-evolved circuits as reference demonstrates substantial improvements:
- Target accuracy improvements over baseline mechanistic localization
- Pervasiveness accuracy gains
- These results "powerfully corroborate our hypothesis and chart a clear trajectory"

Additionally, gradient-based localization methods show "markedly superior performance in Circuit Distance," suggesting gradient signals better approximate future mechanistic structures.

## Dataset Categorization

**15 datasets employed**, categorized by mechanistic type:

**Skill-Centric (Attention-Dominated)**: Arithmetic, Bool, Gender, SST2, Winogrande, Induction, IOI, Reverse, Greater Than, Docstring

**Knowledge-Centric (MLP-Dominated)**: OpenBookQA, FEVER, zsRE, RTE, SA

## Key Quantitative Findings

- Even "well-mastered tasks like Gender (initial accuracy >85%) undergo drastic migration, replacing numerous critical components"
- Circuit evolution continues across 10 epochs with 20 observation steps per epoch
- "95% confidence interval (t=2.776)" maintained across 5 random seeds
- Mechanistic advantage over random disappears when circuit scale expands to encompass more undiscovered components

The central conclusion: static circuit snapshots fundamentally fail to guide dynamic parameter evolution, with success in prior work attributable to MLP resistance to migration rather than mechanistic insight quality.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "6d36b12d-59f0-4a86-9b30-600a0c12a7eb",
  "isSidechain": true,
  "promptId": "4ded1197-994d-445a-b6d7-39fbfd900429",
  "agentId": "af045b478874480c9",
  "type": "user",
  "uuid": "b5636cd4-2593-4bee-9d9f-28667d01849a",
  "sourceToolAssistantUUID": "6d36b12d-59f0-4a86-9b30-600a0c12a7eb",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "f997c3df-2e9d-4031-b144-f643e039c80c",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 26 · 2026-05-19T12:05:30.809Z_

Let me also fetch more details about the specific model architectures, the SAT-based conflict metric, and the oracle/future-circuit experiment.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b5636cd4-2593-4bee-9d9f-28667d01849a",
  "isSidechain": true,
  "agentId": "af045b478874480c9",
  "requestId": "req_011CbBu163SrZwwQcbeJXhfi",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "b8eb557e-4149-4a85-9d65-e2544086dc7e",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "f997c3df-2e9d-4031-b144-f643e039c80c",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018Ed8PGYjvydmGuXvNe2rSK",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 891,
      "cache_creation_input_tokens": 3106,
      "cache_read_input_tokens": 14052,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3106,
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

_source line 27 · 2026-05-19T12:05:35.320Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01QV6sxiSbLvKoJeSuf2ta94`</summary>

```json
{
  "url": "https://arxiv.org/html/2605.06076",
  "prompt": "Extract details about:\n1. Section 5 - the \"future mechanistic localization\" oracle experiment. What exactly did they do? What were the specific accuracy numbers comparing static localization vs future localization vs free evolution?\n2. The gradient-based localization comparison - what methods did they compare and what were the results?\n3. Any details about the SAT/UNSAT formulation for Circuit Conflict - how do they convert circuits to CNF? What does the UNSAT core represent?\n4. The exact experimental protocol: how many random seeds, what optimizer, learning rate, batch size?\n5. Any discussion of how this relates to calibration or confidence/uncertainty in model outputs\n6. The specific layer-by-layer or head-by-head analysis if any exists\n7. Table 1 or any main results table with full numerical values"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b8eb557e-4149-4a85-9d65-e2544086dc7e",
  "isSidechain": true,
  "agentId": "af045b478874480c9",
  "requestId": "req_011CbBu163SrZwwQcbeJXhfi",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "cbcce99a-1c96-4ee0-8f81-ef22c9d52a8d",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "f997c3df-2e9d-4031-b144-f643e039c80c",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018Ed8PGYjvydmGuXvNe2rSK",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 891,
      "cache_creation_input_tokens": 3106,
      "cache_read_input_tokens": 14052,
      "output_tokens": 297,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 3106
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 891,
          "output_tokens": 297,
          "cache_read_input_tokens": 14052,
          "cache_creation_input_tokens": 3106,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 3106,
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

_source line 28 · 2026-05-19T12:05:49.150Z_

<details><summary>↩ Tool result · `toolu_01QV6sxiSbLvKoJeSuf2ta94`</summary>

```text
# Analysis of Research Paper: Mechanistic Localization in LLM Post-Training

## 1. Future Mechanistic Localization Experiment

The authors conducted an oracle experiment using circuits obtained **after** free evolution SFT as a proxy for future mechanisms. Key findings from Figure 4:

- **Future Localization approach**: Used the circuit discovered post-SFT to guide parameter updates, representing the ideal scenario with perfect foresight
- **Results**: This method "yields substantial advantages in both Target and Pervasiveness Accuracy" on the Arithmetic task
- **Implication**: Successfully forecasting post-update circuits would enable effective localization, validating their core hypothesis about temporal lag

Specific accuracy numbers aren't provided in the main text for this comparison, though the paper indicates results are in Appendix F.

## 2. Gradient-Based Localization Comparison

The authors evaluated three localization paradigms beyond circuit-centric approaches:
- Gradient-based methods
- Intervention-based methods  
- Circuit discovery methods

Their finding: "critical components localized via gradient-based techniques exhibit markedly superior performance in terms of Circuit Distance." They suggest "leveraging current gradient signals to approximate or extrapolate the mechanistic structures of future parameter states represents a highly promising frontier."

## 3. SAT/UNSAT Formulation for Circuit Conflict

The process involves:

**Conversion**: Task circuits are mapped into Conjunctive Normal Form (CNF) clauses, converting the problem into Boolean satisfiability

**UNSAT Core**: Defined as "the minimum number of conflicting clauses" identified using SAT solvers (Selsam & Bjørler, 2019)

**Formulation**: For target circuit Φₜ and pervasiveness circuit Φₚ: Circuit Conflict = min_n UNSAT(Φₜ ∧ Φₚ)

This avoids bias from simple set intersection due to component redundancy.

## 4. Experimental Protocol Details

**Random Seeds**: 5 random seeds with tight 95% confidence intervals (t=2.776)

**Optimizer**: AdamW

**Learning Rate**: Grid-searched at 1×10⁻⁵ for each dataset

**Hardware**: 16 NVIDIA RTX A100 GPUs

**Training Duration**: 10 epochs with 20 observation steps each

Batch size not explicitly stated in provided sections.

## 5. Calibration/Confidence Discussion

The paper does **not** discuss calibration or confidence/uncertainty in model outputs. Focus remains on mechanistic circuit evolution rather than predictive uncertainty.

## 6. Layer/Head-by-Head Analysis

The paper distinguishes between **component types** rather than individual layers:
- Attention components (Wq, Wk, Wv, Wo) show "drastic shifts"
- MLP components (Wup, Wdown) remain "relatively stable"

No granular head-level analysis is provided.

## 7. Main Results Table with Numerical Values

**Table 3** (most detailed quantitative results) compares WMDP-Bio vs. Induction unlearning:

| Dataset | Localization | Forget Efficacy | Retain Utility | CD_Attn | CD_MLP |
|---------|--------------|-----------------|----------------|---------|--------|
| WMDP-Bio | Mechanistic | 0.736 | 0.457 | 1.0519 | 0.7391 |
| WMDP-Bio | Random | 0.716 | 0.441 | 1.1243 | 0.9557 |
| Induction | Mechanistic | 0.955 | 0.367 | 1.5593 | 1.1134 |
| Induction | Random | 0.952 | 0.359 | 1.5866 | 1.0547 |

Key insight: Mechanistic localization shows minimal advantage over random localization on attention-dominated tasks, contradicting domain expectations.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "cbcce99a-1c96-4ee0-8f81-ef22c9d52a8d",
  "isSidechain": true,
  "promptId": "4ded1197-994d-445a-b6d7-39fbfd900429",
  "agentId": "af045b478874480c9",
  "type": "user",
  "uuid": "0e1d8c3b-4eba-4b0b-836f-624befa991dd",
  "sourceToolAssistantUUID": "cbcce99a-1c96-4ee0-8f81-ef22c9d52a8d",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "f997c3df-2e9d-4031-b144-f643e039c80c",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 29 · 2026-05-19T12:06:35.862Z_

Now I have comprehensive information about the paper. Here is my thorough synthesis:

---

## Paper: "Navigating by Old Maps: The Pitfalls of Static Mechanistic Localization in LLM Post-Training"

**Authors:** Hang Chen, Jiaying Zhu, Hongyang Chen, Hongxu Liu, Xinyu Yang, Wenya Wang
**arXiv:** [2605.06076](https://arxiv.org/abs/2605.06076) (May 7, 2026), 26 pages

---

### What is "Free Evolution"?

"Free Evolution" refers to the phenomenon where task-critical circuit components naturally shift and migrate during parameter updates (e.g., SFT) when no localization constraints are imposed. In other words, if you simply fine-tune a model without freezing any parameters, the internal circuits that implement specific capabilities will reorganize themselves -- attention mechanisms exhibit drastic structural changes while MLP components remain relatively stable. This is the baseline behavior the paper contrasts against "Locate-then-Update" approaches.

---

### The Three Metrics: Circuit Distance, Stability, and Conflict

The paper formalizes the model as M = &lt;G, theta> where G = &lt;V, E> is a computational graph. Nodes V are individual parameter matrices (Wq, Wk, Wv, Wo for attention; Wup, Wdown for MLPs) -- these are the "minimal update units." Edges E represent activation connections between nodes. Circuits are extracted via **activation patching** (interchange ablation), where an edge is retained when its causal intervention effect exceeds a threshold tau.

**1. Circuit Distance (CD)** -- measures neural migration:

CD = sum over all edges (Wi, Wj) of |I(Wi -> Wj)^theta - I(Wi -> Wj)^theta'|

This is a Manhattan distance over causal effects across the computational graph, comparing circuit structure at parameters theta vs theta'. It captures how much circuit components physically relocate during training.

**2. Circuit Stability (CS)** -- measures knowledge consolidation:

CS(theta') = E_{s,s' in D_t} [rho(C^theta'_s, C^theta'_s')]

This uses Spearman rank correlation between circuits extracted from different random 20% subsets of the same task's data at a given checkpoint. High stability means the model has consolidated its knowledge; low stability means the circuit is still in flux and data-dependent.

**3. Circuit Conflict (CC)** -- measures cross-task interference:

CC(theta) = min_n UNSAT(Phi_t^theta AND Phi_p^theta)

Circuits for the target task (Phi_t) and a "pervasiveness" task (Phi_p) are converted to Conjunctive Normal Form (CNF), and a SAT solver finds the minimum UNSAT core -- the minimum number of conflicting clauses. This avoids bias from simple set intersection due to component redundancy. Higher CC means more mechanistic interference between tasks.

---

### The "Locate-then-Update" Framework

This is the paradigm the paper critiques. It consists of two steps:

1. **Locate**: Use mechanistic interpretability (circuit discovery) to identify which components are critical for a target task.
2. **Update**: Freeze non-critical components and fine-tune only the critical ones, aiming to improve the target task while preserving other capabilities.

The fundamental assumption is that mechanisms extracted from the current parameter state can reliably guide future parameter updates. The paper demonstrates this assumption is flawed due to "temporal lag" -- the circuits you extract now will not represent what the circuits look like after training.

---

### How Circuits Become "Temporally Outdated"

The paper tracks circuits at 20 observation steps across 10 SFT epochs. The key findings are:

- **Attention components** (skill-centric circuits) undergo drastic migration throughout training. Even well-mastered tasks like Gender (>85% initial accuracy) see numerous critical components replaced.
- **MLP components** (knowledge-centric circuits) remain relatively inert due to their vastly larger parameter volume making stored information "more deeply entrenched."
- A circuit snapshot from step 0 increasingly diverges from the actual circuit at step N, meaning any localization strategy based on the initial snapshot becomes progressively less relevant.
- The paper shows that static mechanistic localization provides **"no substantial advantage over random localization"** on skill-centric tasks -- a devastating finding.

---

### Key Experimental Findings

**Models:** Mistral-7B, LLaMA3-8B

**Tasks:** 15 datasets split into two categories:
- **Skill-centric (Attention-dominated):** Arithmetic, Bool, Gender, SST2, Winogrande, Induction, IOI, Reverse, Greater Than, Docstring
- **Knowledge-centric (MLP-dominated):** OpenBookQA, FEVER, zsRE, RTE, SA

**Protocol:** AdamW optimizer, LR = 1e-5, 10 epochs with 20 observation steps, 5 random seeds (95% CI, t=2.776), 16x NVIDIA A100 GPUs. Circuit extraction via ACDC (greedy search), EAP (linear estimation), and EdgePruning (differentiable masks).

**Key quantitative results (Table 3 -- unlearning comparison):**

| Task | Localization | Forget Efficacy | CD_Attn | CD_MLP |
|------|-------------|----------------|---------|--------|
| WMDP-Bio (knowledge) | Mechanistic | 0.736 | 1.0519 | 0.7391 |
| WMDP-Bio (knowledge) | Random | 0.716 | 1.1243 | 0.9557 |
| Induction (skill) | Mechanistic | 0.955 | 1.5593 | 1.1134 |
| Induction (skill) | Random | 0.952 | 1.5866 | 1.0547 |

**Five factors influencing circuit evolution (Table 2):**
- Skill tasks increase attention CD; knowledge tasks decrease MLP CD
- Higher pervasiveness (more competing tasks) increases migration for both component types
- Larger dataset size increases stability
- Higher conflict increases distance and decreases stability
- Already-mastered tasks show lower migration; unmastered tasks show higher migration

**Critical findings:**

1. **Mechanistic localization ~ Random localization** for skill-centric tasks. The supposed advantage of using interpretability to guide updates vanishes for attention-dominated capabilities.

2. **"Illusion of Effectiveness"**: Prior successes with knowledge editing (e.g., ROME, MEMIT) are explained by MLP stability, not by genuine mechanistic guidance. MLPs are naturally resistant to migration, so any localization strategy appears to work.

3. **Future-circuit oracle**: When using circuits from the end of training (perfect foresight) to guide localization, substantial improvements appear in both target and pervasiveness accuracy. This confirms the temporal lag hypothesis -- if you could predict future circuits, localization would work.

4. **Gradient-based methods outperform circuit-based methods** in terms of Circuit Distance, suggesting gradient signals better approximate future mechanistic structures.

---

### Relevance to Your Research on Calibration Circuits

The paper does **not** directly discuss calibration or confidence/uncertainty. However, the implications are critical for your proposal about tracking calibration circuits across post-training stages:

- If calibration is an attention-dominated "skill" (which is plausible since it involves integrating uncertainty signals across tokens), the paper predicts its circuits will undergo drastic Free Evolution during SFT, making static circuit snapshots unreliable.
- If calibration is more MLP-dominated (stored knowledge about when the model should be confident), circuits may be more stable.
- Either way, you will need to account for temporal evolution -- any circuit analysis at one checkpoint cannot be assumed valid at another.
- The paper's three metrics (CD, CS, CC) provide a ready-made toolkit for measuring how calibration circuits change across post-training stages.
- Their finding that gradient-based localization better approximates future states suggests this may be a more practical approach for tracking calibration circuits.

---

Sources:
- [Navigating by Old Maps (arXiv abstract)](https://arxiv.org/abs/2605.06076)
- [Navigating by Old Maps (HTML full text)](https://arxiv.org/html/2605.06076)
- [Navigating by Old Maps (PDF)](https://arxiv.org/pdf/2605.06076)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0e1d8c3b-4eba-4b0b-836f-624befa991dd",
  "isSidechain": true,
  "agentId": "af045b478874480c9",
  "requestId": "req_011CbBu2iK3aUQqU4WqCgP7J",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "6f6cbf13-0a0c-4872-8906-a0f6fa784f50",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "f997c3df-2e9d-4031-b144-f643e039c80c",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SNctaD7vGSbAdYFRGFXh5Z",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2135,
      "cache_read_input_tokens": 17158,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2135,
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
