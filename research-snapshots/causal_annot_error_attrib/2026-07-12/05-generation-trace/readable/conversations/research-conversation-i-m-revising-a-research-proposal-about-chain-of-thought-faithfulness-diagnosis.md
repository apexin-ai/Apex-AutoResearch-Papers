# Research conversation: I'm revising a research proposal about chain-of-thought faithfulness diagnosis. A key reviewer concern is that linear pr

**Multi-Class Annotation Errors in Causal Inference: Topology-Dependent Bias, Sensitivity, and Correction (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 64
- **Recorded user turns:** 1
- **Tool calls:** 26
- **Original source:** `logs/chats/exported-trajectories/account-3/agent-acc4b077cc6fe4048.jsonl`
- **Structured JSON:** [`9dbc6f83cd61c543f05c.json`](../../sessions/9d/9dbc6f83cd61c543f05c.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

64 recorded events

### User

_source line 1 · 2026-05-19T12:00:55.537Z_

I'm revising a research proposal about chain-of-thought faithfulness diagnosis. A key reviewer concern is that linear probes on LLM hidden states may capture correlative/epiphenomenal information rather than causally relevant information, making probe accuracy uniformly high regardless of actual faithfulness. This is the "probe inflation" problem.

I need to research:
1. Methods for calibrating probes to distinguish genuine vs correlative information — especially "null probe" or "control probe" baselines (e.g., training probes on shuffled labels, selectivity scores, etc.)
2. Chun et al. (2602.20338) "Emergent Manifold Separability during Reasoning in LLMs" — their finding that probe accuracy ≠ computational readiness
3. Any work on probe selectivity, amnesic probing, or causal probing that addresses the concern that high probe accuracy doesn't mean the information is being used
4. Methods for distinguishing trajectory shapes even when absolute values are inflated

Please search for:
- "probe selectivity score control task" neural network probing
- "amnesic probing" OR "causal probing" language models 2024 2025 2026
- "null probe" baseline linear probing hidden states
- Chun et al 2602.20338 manifold separability reasoning

For key papers found, use WebFetch to read the abstracts/key findings. Report back with concrete methods I could use for probe calibration.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "f76ab8f1-cf60-4739-be49-0817894703ea",
  "agentId": "acc4b077cc6fe4048",
  "type": "user",
  "uuid": "f2d4cc53-a4f3-44b0-b9d8-cdab9d42fc0b",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "a600395c-52af-4483-884f-a0137eaa6f5f",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 2 · 2026-05-19T12:00:55.540Z_

```json
{
  "parentUuid": "f2d4cc53-a4f3-44b0-b9d8-cdab9d42fc0b",
  "isSidechain": true,
  "agentId": "acc4b077cc6fe4048",
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
  "uuid": "5aac488e-83e4-47fe-874b-d9ad100e9e34",
  "timestamp": "2026-05-19T12:00:55.540Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "a600395c-52af-4483-884f-a0137eaa6f5f",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 3 · 2026-05-19T12:00:55.541Z_

```json
{
  "parentUuid": "5aac488e-83e4-47fe-874b-d9ad100e9e34",
  "isSidechain": true,
  "agentId": "acc4b077cc6fe4048",
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "1bedb465-2671-4398-a130-5b0cda1d5de0",
  "timestamp": "2026-05-19T12:00:55.541Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "a600395c-52af-4483-884f-a0137eaa6f5f",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Assistant

_source line 4 · 2026-05-19T12:00:58.465Z_



I'll research these topics systematically. Let me start by loading the WebSearch and WebFetch tools, then conduct multiple searches in parallel.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1bedb465-2671-4398-a130-5b0cda1d5de0",
  "isSidechain": true,
  "agentId": "acc4b077cc6fe4048",
  "requestId": "req_011CbBtf4xede8ZpiPFojXNE",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "667da293-1b5a-4ac9-827a-088ed022598d",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "a600395c-52af-4483-884f-a0137eaa6f5f",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01W1PZqE2d9nuQYsNhcVUqf1",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 9454,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 9454,
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

_source line 5 · 2026-05-19T12:00:58.790Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_018vpXEL2qvNucmJjKnAwrkE`</summary>

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
  "parentUuid": "667da293-1b5a-4ac9-827a-088ed022598d",
  "isSidechain": true,
  "agentId": "acc4b077cc6fe4048",
  "requestId": "req_011CbBtf4xede8ZpiPFojXNE",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "08c7a166-cddf-47dc-917e-974409861ddb",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "a600395c-52af-4483-884f-a0137eaa6f5f",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01W1PZqE2d9nuQYsNhcVUqf1",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 9454,
      "cache_read_input_tokens": 0,
      "output_tokens": 110,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 9454
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 110,
          "cache_read_input_tokens": 0,
          "cache_creation_input_tokens": 9454,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 9454,
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

_source line 6 · 2026-05-19T12:00:58.798Z_

<details><summary>↩ Tool result · `toolu_018vpXEL2qvNucmJjKnAwrkE`</summary>

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
  "parentUuid": "08c7a166-cddf-47dc-917e-974409861ddb",
  "isSidechain": true,
  "promptId": "f76ab8f1-cf60-4739-be49-0817894703ea",
  "agentId": "acc4b077cc6fe4048",
  "type": "user",
  "uuid": "4ec3569b-2cb1-4b25-bb07-26f1122fd0f1",
  "sourceToolAssistantUUID": "08c7a166-cddf-47dc-917e-974409861ddb",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "a600395c-52af-4483-884f-a0137eaa6f5f",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 7 · 2026-05-19T12:01:01.075Z_



Now let me run all four searches in parallel.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4ec3569b-2cb1-4b25-bb07-26f1122fd0f1",
  "isSidechain": true,
  "agentId": "acc4b077cc6fe4048",
  "requestId": "req_011CbBtfKCeoDWQrR7SDKWVV",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "2792c708-5230-4ba1-a859-3994f1e3a24a",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "a600395c-52af-4483-884f-a0137eaa6f5f",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BpLMSb4NJrXPBD8dxw18x8",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1132,
      "cache_read_input_tokens": 9454,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1132,
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

_source line 8 · 2026-05-19T12:01:01.812Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_014Du4YhM3MFvTWe61vcoqXy`</summary>

```json
{
  "query": "probe selectivity score control task neural network probing NLP"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2792c708-5230-4ba1-a859-3994f1e3a24a",
  "isSidechain": true,
  "agentId": "acc4b077cc6fe4048",
  "requestId": "req_011CbBtfKCeoDWQrR7SDKWVV",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "87bdd730-c8fa-461d-a766-e0ab1d2f5d31",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "a600395c-52af-4483-884f-a0137eaa6f5f",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BpLMSb4NJrXPBD8dxw18x8",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1132,
      "cache_read_input_tokens": 9454,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1132,
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

_source line 9 · 2026-05-19T12:01:02.050Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01X3xDoAfi649Ct3z2s8U3pz`</summary>

```json
{
  "query": "\"amnesic probing\" OR \"causal probing\" language models 2024 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "87bdd730-c8fa-461d-a766-e0ab1d2f5d31",
  "isSidechain": true,
  "agentId": "acc4b077cc6fe4048",
  "requestId": "req_011CbBtfKCeoDWQrR7SDKWVV",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "23c28040-6149-4726-bc3c-976eb8a61376",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "a600395c-52af-4483-884f-a0137eaa6f5f",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BpLMSb4NJrXPBD8dxw18x8",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1132,
      "cache_read_input_tokens": 9454,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1132,
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

_source line 10 · 2026-05-19T12:01:02.497Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01GvXzUabQvW5GKvywgBLzmR`</summary>

```json
{
  "query": "\"null probe\" baseline linear probing hidden states language models"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "23c28040-6149-4726-bc3c-976eb8a61376",
  "isSidechain": true,
  "agentId": "acc4b077cc6fe4048",
  "requestId": "req_011CbBtfKCeoDWQrR7SDKWVV",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "e2b44769-bf7d-4c1d-afc4-8a45c278f3e1",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "a600395c-52af-4483-884f-a0137eaa6f5f",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BpLMSb4NJrXPBD8dxw18x8",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1132,
      "cache_read_input_tokens": 9454,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1132,
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

_source line 11 · 2026-05-19T12:01:02.724Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01JAHwabvrcSDt6BNQzmza2n`</summary>

```json
{
  "query": "Chun et al 2602.20338 \"manifold separability\" reasoning LLM probing"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e2b44769-bf7d-4c1d-afc4-8a45c278f3e1",
  "isSidechain": true,
  "agentId": "acc4b077cc6fe4048",
  "requestId": "req_011CbBtfKCeoDWQrR7SDKWVV",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "177146c1-bbf2-47c5-9b2a-e02120fbb62a",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "a600395c-52af-4483-884f-a0137eaa6f5f",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BpLMSb4NJrXPBD8dxw18x8",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1132,
      "cache_read_input_tokens": 9454,
      "output_tokens": 235,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1132
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 235,
          "cache_read_input_tokens": 9454,
          "cache_creation_input_tokens": 1132,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1132,
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

_source line 12 · 2026-05-19T12:01:10.019Z_

<details><summary>↩ Tool result · `toolu_014Du4YhM3MFvTWe61vcoqXy`</summary>

```text
Web search results for query: "probe selectivity score control task neural network probing NLP"

Links: [{"title":"Probing Classifiers: Decoding What Language Models Learn - Interactive | Michael Brenndoerfer | Michael Brenndoerfer","url":"https://mbrenndoerfer.com/writing/probing-classifiers"},{"title":"Linear Probes: Neural Network Diagnostics","url":"https://www.emergentmind.com/topics/linear-probes"},{"title":"Designing and Interpreting Probes · John Hewitt","url":"https://www.cs.columbia.edu/~johnhew/interpreting-probes.html"},{"title":"Linguistics Wisdom of NLP Models | Towards Data Science","url":"https://towardsdatascience.com/linguistics-wisdom-of-nlp-models-8c8554bc8c66/"},{"title":"Designing and Interpreting Probes with Control Tasks","url":"https://arxiv.org/pdf/1909.03368"},{"title":"Probing","url":"https://sidn.baulab.info/probing/"},{"title":"Designing and Interpreting Probes with Control Tasks John Hewitt","url":"https://nlp.stanford.edu/pubs/hewitt2019control.pdf"},{"title":"Designing and Interpreting Probes with Control Tasks","url":"https://aclanthology.org/D19-1275.pdf"},{"title":"Probing Classifiers: Promises, Shortcomings, and Advances | Computational Linguistics | MIT Press","url":"https://direct.mit.edu/coli/article/48/1/207/107571/Probing-Classifiers-Promises-Shortcomings-and"},{"title":"Overview Core method Probing or learning a new model? Selectivity","url":"http://web.stanford.edu/class/cs224u/2022/slides/cs224u-analysis-part4-handout.pdf"}]

Based on the search results, here's what I found about probe selectivity scores, control tasks, and neural network probing in NLP:

## Probe Selectivity and Control Tasks

Selectivity is defined as the difference between linguistic task accuracy and control task accuracy. The selectivity score isolates what the real labels contribute over and above arbitrary label assignment, and a large gap means the probe succeeded specifically because of the linguistic structure in the labels.

## Control Task Design

Control tasks put into action the intuition that the more a probe is able to make memorized output decisions independently of the linguistic properties of a representation, the less its performance on a task necessarily reflects properties of the representation, and through control tasks selectivity is defined.

## Key Findings on Different Probe Types

Research has shown important differences between probe architectures:

- MLP probes achieve very low selectivity with popular hyperparameter settings, such as achieving 97.3 accuracy on part-of-speech tagging compared to 92.8 control task accuracy, resulting in 4.5 selectivity.

- Linear and bilinear probes achieve relatively high selectivity across a range of hyperparameters, for example a linear probe on part-of-speech tagging achieves 97.2 accuracy and 71.2 control task accuracy, for 26.0 selectivity.

## Importance for Interpretation

High selectivity from a linear probe indicates features are truly encoded in representation, rather than artifacts of the probe. This is important because complex neural network probes are able to memorize a large number of labeling decisions independently of the linguistic properties of the representations.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "87bdd730-c8fa-461d-a766-e0ab1d2f5d31",
  "isSidechain": true,
  "promptId": "f76ab8f1-cf60-4739-be49-0817894703ea",
  "agentId": "acc4b077cc6fe4048",
  "type": "user",
  "uuid": "2ed0f718-6ecf-4cc3-b42a-6efe9fa4ba76",
  "sourceToolAssistantUUID": "87bdd730-c8fa-461d-a766-e0ab1d2f5d31",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "a600395c-52af-4483-884f-a0137eaa6f5f",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 13 · 2026-05-19T12:01:10.082Z_

<details><summary>↩ Tool result · `toolu_01JAHwabvrcSDt6BNQzmza2n`</summary>

```text
Web search results for query: "Chun et al 2602.20338 "manifold separability" reasoning LLM probing"

Links: [{"title":"[2602.20338] Emergent Manifold Separability during Reasoning in Large Language Models","url":"https://arxiv.org/abs/2602.20338"},{"title":"Emergent Manifold Separability during Reasoning in Large Language Models","url":"https://arxiv.org/pdf/2602.20338"},{"title":"From Chains to DAGs: Probing the Graph Structure of Reasoning in LLMs","url":"https://arxiv.org/pdf/2601.17593"},{"title":"Emergent Manifold Separability during Reasoning in Large Language Models","url":"https://arxiv.org/html/2602.20338"},{"title":"Truth as a Trajectory: What Internal Representations Reveal About Large Language Model Reasoning","url":"https://arxiv.org/pdf/2603.01326"}]

Based on the search results, here's what I found:

The paper arXiv:2602.20338 is titled "Emergent Manifold Separability during Reasoning in Large Language Models" by Alexandre Polo, Chanwoo Chun, and SueYeon Chung.

The paper investigates Chain-of-Thought (CoT) prompting and the temporal dynamics of representation geometry in Large Language Models. The authors apply Manifold Capacity Theory (MCT) to a compositional Boolean logic task to quantify the linear separability of latent representations without the confounding factors of probe training.

The analysis reveals that reasoning manifests as a transient geometric pulse, where concept manifolds are untangled into linearly separable subspaces immediately prior to computation and rapidly compressed thereafter. This behavior diverges from standard linear probe accuracy, which remains high long after computation, suggesting a fundamental distinction between information that is merely retrievable and information that is geometrically prepared for processing.

The authors interpret this phenomenon as "Dynamic Manifold Management," a mechanism where the model dynamically modulates representational capacity to optimize the bandwidth of the residual stream throughout the reasoning chain.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "177146c1-bbf2-47c5-9b2a-e02120fbb62a",
  "isSidechain": true,
  "promptId": "f76ab8f1-cf60-4739-be49-0817894703ea",
  "agentId": "acc4b077cc6fe4048",
  "type": "user",
  "uuid": "88a5e14b-c1db-4cf1-9d99-e2863a522b49",
  "sourceToolAssistantUUID": "177146c1-bbf2-47c5-9b2a-e02120fbb62a",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "a600395c-52af-4483-884f-a0137eaa6f5f",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-19T12:01:11.426Z_

<details><summary>↩ Tool result · `toolu_01GvXzUabQvW5GKvywgBLzmR`</summary>

```text
Web search results for query: ""null probe" baseline linear probing hidden states language models"

Links: [{"title":"Probing LLM Hidden States","url":"https://apxml.com/courses/how-to-build-a-large-language-model/chapter-23-analyzing-model-behavior/probing-internal-representations"},{"title":"Probing Classifiers: Decoding What Language Models Learn - Interactive | Michael Brenndoerfer | Michael Brenndoerfer","url":"https://mbrenndoerfer.com/writing/probing-classifiers"},{"title":"Probing Hidden States for Calibrated, Alignment-Resistant Predictions in LLMs","url":"https://www.medrxiv.org/content/10.1101/2025.09.17.25336018.full.pdf"},{"title":"A Little Confidence Goes a Long Way","url":"https://arxiv.org/pdf/2408.11239"},{"title":"Probing Hidden States for Calibrated, Alignment-Resistant Predictions in LLMs","url":"https://www.medrxiv.org/content/10.1101/2025.09.17.25336018v2.full.pdf"},{"title":"Probing Hidden States for Calibrated, Alignment-Resistant Predictions in LLMs | medRxiv","url":"https://www.medrxiv.org/content/10.1101/2025.09.17.25336018v2.full"},{"title":"Hitting \"Probe\"rty with Non-Linearity, and More","url":"https://arxiv.org/pdf/2402.16168"},{"title":"Linearly Decoding Refused Knowledge in Aligned Language Models","url":"https://arxiv.org/pdf/2507.00239"},{"title":"Neural Probe-Based Hallucination Detection for Large Language Models","url":"https://arxiv.org/pdf/2512.20949"},{"title":"Language Models Encode the Value of Numbers Linearly","url":"https://arxiv.org/pdf/2401.03735"}]

Based on the search results, I found information about linear probing techniques for analyzing hidden states in language models. Here are the key findings:

## Linear Probing Overview

A probing classifier is a lightweight supervised model trained on frozen representations extracted from a pretrained neural network, and its accuracy on a linguistic task measures how much information about that task is encoded in the representations.

A linear model (logistic regression) is the standard choice because it can only succeed if the information is linearly decodable from the representations.

## Baseline Comparisons

Comparing against baseline probes (e.g., trained on random vectors or static word embeddings) helps establish whether probed information is genuinely encoded in the model's representations rather than being an artifact of the probing method.

## Applications

The search results demonstrate several applications of linear probing:

- Language models encode the value of numbers linearly, as revealed by utilizing linear probes to probe encoded number values in the hidden states of language models.

- Linear probes trained on language models' hidden states are often highly predictive of jailbroken responses, and probes trained on base LMs (which do not refuse) are capable of revealing much of the same information that jailbreak prompts reveal in instruction-tuned versions.

However, the search results did not provide specific details about a technique explicitly called "null probe" as a baseline. If you're looking for information about a specific paper or technique with that name, you may want to search for more specific author names or publication details.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "e2b44769-bf7d-4c1d-afc4-8a45c278f3e1",
  "isSidechain": true,
  "promptId": "f76ab8f1-cf60-4739-be49-0817894703ea",
  "agentId": "acc4b077cc6fe4048",
  "type": "user",
  "uuid": "f31dbce2-29b8-45a0-8d8e-ae07125bee06",
  "sourceToolAssistantUUID": "e2b44769-bf7d-4c1d-afc4-8a45c278f3e1",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "a600395c-52af-4483-884f-a0137eaa6f5f",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 15 · 2026-05-19T12:01:11.907Z_

<details><summary>↩ Tool result · `toolu_01X3xDoAfi649Ct3z2s8U3pz`</summary>

```text
Web search results for query: ""amnesic probing" OR "causal probing" language models 2024 2025"

Links: [{"title":"Improving Causal Interventions in Amnesic Probing with Mean Projection or LEACE - ACL Anthology","url":"https://aclanthology.org/2025.findings-acl.674/"},{"title":"Amnesic Probing: Behavioral Explanation with Amnesic Counterfactuals","url":"https://arxiv.org/pdf/2006.00995"},{"title":"Latent Causal Probing: A Formal Perspective on Probing with Causal   Models of Data","url":"https://arxiv.org/pdf/2407.13765"},{"title":"Improving Causal Interventions in Amnesic Probing with Mean Projection or LEACE","url":"https://arxiv.org/html/2506.11673"},{"title":"[2506.11673] Improving Causal Interventions in Amnesic Probing with Mean Projection or LEACE","url":"https://arxiv.org/abs/2506.11673"},{"title":"Improving Causal Interventions in Amnesic Probing with Mean Projection or LEACE","url":"https://arxiv.org/pdf/2506.11673"},{"title":"On the Reliability of Large Language Models for Causal ...","url":"https://aclanthology.org/2025.acl-long.471.pdf"}]

Based on the search results, here's what I found about amnesic probing and causal probing in language models from 2024-2025:

## Amnesic Probing

Amnesic Probing is a counterfactual approach to causal attribution that operates on the intuition that if a property is being used for a task, then the removal of that property should negatively influence the model's ability to solve the task.

Amnesic probing is a technique used to examine the influence of specific linguistic information on the behavior of a model by identifying and removing the relevant information and then assessing whether the model's performance on the main task changes; if the removed information is relevant, the model's performance should decline.

## Recent Developments (2024-2025)

It has been shown that Iterative Nullspace Projection (INLP), a widely used removal technique, introduces random modifications to representations when eliminating target information, while Mean Projection (MP) and LEACE are proposed alternatives that remove information in a more targeted manner, thereby enhancing the potential for obtaining behavioral explanations through Amnesic Probing.

The LEACE method, proposed in Belrose et al. (2024), removes target information in a more precise manner similar to MP, with both LEACE and MP performing linear projection-based concept erasure using label-driven subspaces.

A 2025 paper by Dobrzeniecka et al. (published in ACL 2025 Findings) specifically focuses on improving causal interventions in amnesic probing by comparing these different removal techniques.

## Causal Probing

Latent Causal Probing is a framework based on causal mediation analysis that isolates the causal path through language models while excluding the probe's influence, allowing for precise conclusions about the causal relationship between latent dynamics and what is learned by the model.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "23c28040-6149-4726-bc3c-976eb8a61376",
  "isSidechain": true,
  "promptId": "f76ab8f1-cf60-4739-be49-0817894703ea",
  "agentId": "acc4b077cc6fe4048",
  "type": "user",
  "uuid": "844d3d12-8718-49ec-8801-027e9fb6772a",
  "sourceToolAssistantUUID": "23c28040-6149-4726-bc3c-976eb8a61376",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "a600395c-52af-4483-884f-a0137eaa6f5f",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 16 · 2026-05-19T12:01:14.690Z_

Excellent results. Now let me fetch the key papers for detailed findings.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "844d3d12-8718-49ec-8801-027e9fb6772a",
  "isSidechain": true,
  "agentId": "acc4b077cc6fe4048",
  "requestId": "req_011CbBtgH1E1SbyrNKYhhtTB",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "abf2dfbc-204f-4790-afc1-54730aabee71",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "a600395c-52af-4483-884f-a0137eaa6f5f",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GwkXd8f9Qdup5YoZ6CAJHB",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1405,
      "cache_creation_input_tokens": 1939,
      "cache_read_input_tokens": 10586,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1939,
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

_source line 17 · 2026-05-19T12:01:17.565Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01HDH9RRK4DLjaVkQxfPPHip`</summary>

```json
{
  "url": "https://arxiv.org/abs/2602.20338",
  "prompt": "Extract the full abstract and key findings. Specifically: (1) What is Manifold Capacity Theory (MCT) and how does it differ from linear probes? (2) What is the \"geometric pulse\" finding? (3) What exactly do they show about probe accuracy vs computational readiness? (4) What is \"Dynamic Manifold Management\"? (5) Any concrete metrics or methods they propose as alternatives to probe accuracy."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "abf2dfbc-204f-4790-afc1-54730aabee71",
  "isSidechain": true,
  "agentId": "acc4b077cc6fe4048",
  "requestId": "req_011CbBtgH1E1SbyrNKYhhtTB",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "cf507444-7d8a-4f98-96f1-5fc5304d9e6f",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "a600395c-52af-4483-884f-a0137eaa6f5f",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GwkXd8f9Qdup5YoZ6CAJHB",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1405,
      "cache_creation_input_tokens": 1939,
      "cache_read_input_tokens": 10586,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1939,
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

_source line 18 · 2026-05-19T12:01:19.464Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01X3SEKnyJhmZtbPa3jZyjak`</summary>

```json
{
  "url": "https://arxiv.org/abs/2506.11673",
  "prompt": "Extract the full abstract and key findings. What are the specific methods compared (INLP, Mean Projection, LEACE)? How do they improve amnesic probing? What do they find about when probe accuracy does NOT correspond to causal relevance? What are the concrete recommendations for practitioners?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "cf507444-7d8a-4f98-96f1-5fc5304d9e6f",
  "isSidechain": true,
  "agentId": "acc4b077cc6fe4048",
  "requestId": "req_011CbBtgH1E1SbyrNKYhhtTB",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "c95dbe09-762e-4c8e-b8b0-ae2c345570a9",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "a600395c-52af-4483-884f-a0137eaa6f5f",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GwkXd8f9Qdup5YoZ6CAJHB",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1405,
      "cache_creation_input_tokens": 1939,
      "cache_read_input_tokens": 10586,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1939,
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

_source line 19 · 2026-05-19T12:01:21.803Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01VcE6NRgjSMXeeaVHu8hbwk`</summary>

```json
{
  "url": "https://nlp.stanford.edu/pubs/hewitt2019control.pdf",
  "prompt": "Extract the key methods and findings about control tasks and selectivity. Specifically: (1) How is the control task defined? (2) What is the selectivity formula? (3) What did they find about MLP vs linear probes in terms of selectivity? (4) How should researchers use control tasks to calibrate probes? (5) Any concrete recommendations for what selectivity score threshold indicates genuine encoding."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c95dbe09-762e-4c8e-b8b0-ae2c345570a9",
  "isSidechain": true,
  "agentId": "acc4b077cc6fe4048",
  "requestId": "req_011CbBtgH1E1SbyrNKYhhtTB",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "b32a5b09-8ecf-4a11-885c-273589cc5fdf",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "a600395c-52af-4483-884f-a0137eaa6f5f",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GwkXd8f9Qdup5YoZ6CAJHB",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1405,
      "cache_creation_input_tokens": 1939,
      "cache_read_input_tokens": 10586,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1939,
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

_source line 20 · 2026-05-19T12:01:23.426Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_017g3NSe7zgkLb6MYvW92gjx`</summary>

```json
{
  "url": "https://arxiv.org/abs/2407.13765",
  "prompt": "Extract the full abstract and key findings about Latent Causal Probing. How does it formalize the relationship between probing and causation? What framework do they propose? How does it address the problem that high probe accuracy doesn't mean the information is causally used by the model?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b32a5b09-8ecf-4a11-885c-273589cc5fdf",
  "isSidechain": true,
  "agentId": "acc4b077cc6fe4048",
  "requestId": "req_011CbBtgH1E1SbyrNKYhhtTB",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "f4cfefe4-1f7a-4af1-a943-ad18cc4cf3d4",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "a600395c-52af-4483-884f-a0137eaa6f5f",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GwkXd8f9Qdup5YoZ6CAJHB",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1405,
      "cache_creation_input_tokens": 1939,
      "cache_read_input_tokens": 10586,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1939,
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

_source line 21 · 2026-05-19T12:01:23.743Z_

<details><summary>↩ Tool result · `toolu_01HDH9RRK4DLjaVkQxfPPHip`</summary>

```text
# Analysis of "Emergent Manifold Separability during Reasoning in Large Language Models"

## (1) Manifold Capacity Theory vs. Linear Probes

MCT enables researchers to "quantify the linear separability of latent representations without the confounding factors of probe training." Unlike traditional linear probes that measure information retrievability through trained classifiers, MCT directly measures geometric organization of concept manifolds in representation space without requiring additional training procedures.

## (2) The "Geometric Pulse" Finding

The research reveals that during reasoning tasks, concept manifolds exhibit transient geometric behavior: they become "untangled into linearly separable subspaces immediately prior to computation and rapidly compressed thereafter." This temporal pattern appears across multiple models and tasks tested.

## (3) Probe Accuracy vs. Computational Readiness

A critical distinction emerges: "standard linear probe accuracy...remains high long after computation," whereas geometric separability peaks just before and during computation. This suggests information can be present yet not geometrically organized for actual processing—a fundamental difference between information availability and information preparation.

## (4) Dynamic Manifold Management

This proposed mechanism describes how models "dynamically modulate representational capacity to optimize the bandwidth of the residual stream throughout the reasoning chain." Rather than maintaining constant representational geometry, models actively reshape it for computational efficiency.

## (5) Alternative Metrics

MCT itself serves as the proposed alternative, measuring linear separability directly without probe-training artifacts, offering a geometry-based assessment of representational readiness distinct from traditional accuracy metrics.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "cf507444-7d8a-4f98-96f1-5fc5304d9e6f",
  "isSidechain": true,
  "promptId": "f76ab8f1-cf60-4739-be49-0817894703ea",
  "agentId": "acc4b077cc6fe4048",
  "type": "user",
  "uuid": "e073d418-7040-4aa4-a301-60ec2acf9826",
  "sourceToolAssistantUUID": "cf507444-7d8a-4f98-96f1-5fc5304d9e6f",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "a600395c-52af-4483-884f-a0137eaa6f5f",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 22 · 2026-05-19T12:01:24.613Z_

<details><summary>↩ Tool result · `toolu_01X3SEKnyJhmZtbPa3jZyjak`</summary>

```text
# Summary of arXiv:2506.11673

## Full Abstract
"Amnesic probing is a technique used to examine the influence of specific linguistic information on the behaviour of a model. This involves identifying and removing the relevant information and then assessing whether the model's performance on the main task changes. If the removed information is relevant, the model's performance should decline. The difficulty with this approach lies in removing only the target information while leaving other information unchanged. It has been shown that Iterative Nullspace Projection (INLP), a widely used removal technique, introduces random modifications to representations when eliminating target information. We demonstrate that Mean Projection (MP) and LEACE, two proposed alternatives, remove information in a more targeted manner, thereby enhancing the potential for obtaining behavioural explanations through Amnesic Probing."

## Methods Compared
Three information removal techniques are examined:
- **INLP (Iterative Nullspace Projection)**: The baseline approach, which creates unintended random modifications to representations
- **Mean Projection (MP)**: A proposed alternative offering more targeted removal
- **LEACE**: Another alternative approach providing more precise information elimination

## Key Improvement
Both MP and LEACE accomplish more surgical information removal compared to INLP's collateral modifications, thereby strengthening the validity of behavioral conclusions drawn from amnesic probing experiments.

## Limitations & Findings
The document does not provide specific details regarding discrepancies between probe accuracy and causal relevance or concrete practitioner recommendations beyond the general superiority of the MP and LEACE methods.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c95dbe09-762e-4c8e-b8b0-ae2c345570a9",
  "isSidechain": true,
  "promptId": "f76ab8f1-cf60-4739-be49-0817894703ea",
  "agentId": "acc4b077cc6fe4048",
  "type": "user",
  "uuid": "6b040e35-960d-4ac7-b347-e559a14247f3",
  "sourceToolAssistantUUID": "c95dbe09-762e-4c8e-b8b0-ae2c345570a9",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "a600395c-52af-4483-884f-a0137eaa6f5f",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 23 · 2026-05-19T12:01:28.950Z_

<details><summary>↩ Tool result · `toolu_017g3NSe7zgkLb6MYvW92gjx`</summary>

```text
# Latent Causal Probing: Framework and Key Insights

## Full Abstract

The authors describe their work as addressing challenges in designing robust probing experiments for language models. They propose using structural causal models (SCMs) to formally analyze whether LMs learn to represent latent variables underlying text. Their empirical validation uses a synthetic grid-world navigation task where the exact causal structure is known, allowing them to draw stronger conclusions about LMs' ability to induce latent concepts.

## Core Framework

The researchers employ **structural causal models** as their theoretical foundation. Rather than treating probing as a simple classification task, they frame the central question as: "whether the LM has learned to represent the latent variables of the SCM" (from the abstract).

## Addressing the Core Problem

The key innovation addresses a fundamental limitation in probing methodology. Traditional probing suffers from an interpretability gap—high accuracy on auxiliary tasks doesn't guarantee the model uses that information causally. By anchoring analysis in SCMs with known causal structure, the authors establish formal grounds to distinguish between:

1. **Correlation**: Information present in representations
2. **Causal use**: Information actually employed by the model

Their synthetic task design—where true causal relationships are explicitly defined—enables them to validate that detected representations reflect genuine learned concepts rather than spurious correlations. This formalization provides methodological rigor previously absent from probing studies.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f4cfefe4-1f7a-4af1-a943-ad18cc4cf3d4",
  "isSidechain": true,
  "promptId": "f76ab8f1-cf60-4739-be49-0817894703ea",
  "agentId": "acc4b077cc6fe4048",
  "type": "user",
  "uuid": "b7ca7d38-1885-4082-b385-205bc886abbb",
  "sourceToolAssistantUUID": "f4cfefe4-1f7a-4af1-a943-ad18cc4cf3d4",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "a600395c-52af-4483-884f-a0137eaa6f5f",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 24 · 2026-05-19T12:01:29.334Z_

<details><summary>↩ Tool result · `toolu_01VcE6NRgjSMXeeaVHu8hbwk`</summary>

```text
# Control Tasks and Selectivity in Neural Probes

I'm unable to extract the requested information from the provided content. The material appears to be a PDF file containing encoded binary/compressed data rather than readable text about control tasks, selectivity formulas, or probe methods.

To properly address your questions about:
1. Control task definitions
2. Selectivity formulas
3. MLP vs linear probe comparisons
4. Calibration guidance
5. Threshold recommendations

I would need access to the actual readable text content of the research paper. Could you provide either:
- The plain text version of the paper
- A properly formatted PDF excerpt
- The paper's title or DOI so I can reference the work accurately

This would allow me to give you precise, properly cited information while respecting the 125-character quote limit and attribution requirements you've specified.

[Binary content (application/pdf, 819.7KB) also saved to /home/ubuntu/.claude-account-3/projects/-home-ubuntu-idea-gen-pipeline/a600395c-52af-4483-884f-a0137eaa6f5f/tool-results/webfetch-1779192084913-fmzfpr.pdf]
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "b32a5b09-8ecf-4a11-885c-273589cc5fdf",
  "isSidechain": true,
  "promptId": "f76ab8f1-cf60-4739-be49-0817894703ea",
  "agentId": "acc4b077cc6fe4048",
  "type": "user",
  "uuid": "1c2f753e-91ff-49db-adfb-5a2ddd0b3211",
  "sourceToolAssistantUUID": "b32a5b09-8ecf-4a11-885c-273589cc5fdf",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "a600395c-52af-4483-884f-a0137eaa6f5f",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 25 · 2026-05-19T12:01:32.486Z_

Good. Let me now search for additional key papers and methods.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1c2f753e-91ff-49db-adfb-5a2ddd0b3211",
  "isSidechain": true,
  "agentId": "acc4b077cc6fe4048",
  "requestId": "req_011CbBthZVC2qXESrbqqkb7j",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "dc5c029e-c135-432d-a162-2475444fd6df",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "a600395c-52af-4483-884f-a0137eaa6f5f",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KpkZRWK5r2sT55T6arBAoC",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 337,
      "cache_creation_input_tokens": 3136,
      "cache_read_input_tokens": 12525,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3136,
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

_source line 26 · 2026-05-19T12:01:32.959Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01PcMSxN9nFzsW31oiBNg1cn`</summary>

```json
{
  "query": "Hewitt Manning 2019 \"control tasks\" selectivity probing classifiers EMNLP"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "dc5c029e-c135-432d-a162-2475444fd6df",
  "isSidechain": true,
  "agentId": "acc4b077cc6fe4048",
  "requestId": "req_011CbBthZVC2qXESrbqqkb7j",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "4d797ca7-68b9-4987-8a1c-ff49a4874b0b",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "a600395c-52af-4483-884f-a0137eaa6f5f",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KpkZRWK5r2sT55T6arBAoC",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 337,
      "cache_creation_input_tokens": 3136,
      "cache_read_input_tokens": 12525,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3136,
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

_source line 27 · 2026-05-19T12:01:34.034Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01EUEvmZCPDfzzSdfC9zdknn`</summary>

```json
{
  "query": "Elazar Ravfogel \"amnesic probing\" INLP nullspace projection causal information usage"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4d797ca7-68b9-4987-8a1c-ff49a4874b0b",
  "isSidechain": true,
  "agentId": "acc4b077cc6fe4048",
  "requestId": "req_011CbBthZVC2qXESrbqqkb7j",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "a65b4f01-1f0a-4399-b933-ccffa4d68ffe",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "a600395c-52af-4483-884f-a0137eaa6f5f",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KpkZRWK5r2sT55T6arBAoC",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 337,
      "cache_creation_input_tokens": 3136,
      "cache_read_input_tokens": 12525,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3136,
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

_source line 28 · 2026-05-19T12:01:34.734Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01KdC4HGVzemRUirHG3obdLj`</summary>

```json
{
  "query": "probe accuracy inflation random baselines shuffled labels probing neural networks interpretability 2024 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a65b4f01-1f0a-4399-b933-ccffa4d68ffe",
  "isSidechain": true,
  "agentId": "acc4b077cc6fe4048",
  "requestId": "req_011CbBthZVC2qXESrbqqkb7j",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "fd8b1d05-972b-4008-ab2f-e75a4eb4f7da",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "a600395c-52af-4483-884f-a0137eaa6f5f",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KpkZRWK5r2sT55T6arBAoC",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 337,
      "cache_creation_input_tokens": 3136,
      "cache_read_input_tokens": 12525,
      "output_tokens": 203,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 3136
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 337,
          "output_tokens": 203,
          "cache_read_input_tokens": 12525,
          "cache_creation_input_tokens": 3136,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 3136,
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

_source line 29 · 2026-05-19T12:01:39.765Z_

<details><summary>↩ Tool result · `toolu_01PcMSxN9nFzsW31oiBNg1cn`</summary>

```text
Web search results for query: "Hewitt Manning 2019 "control tasks" selectivity probing classifiers EMNLP"

Links: [{"title":"Designing and Interpreting Probes with Control Tasks - ACL Anthology","url":"https://aclanthology.org/D19-1275/"},{"title":"Probing Classifiers: Decoding What Language Models Learn - Interactive | Michael Brenndoerfer | Michael Brenndoerfer","url":"https://mbrenndoerfer.com/writing/probing-classifiers"},{"title":"Designing and Interpreting Probes with Control Tasks","url":"https://aclanthology.org/D19-1275.pdf"},{"title":"Designing and Interpreting Probes · John Hewitt","url":"https://www.cs.columbia.edu/~johnhew/interpreting-probes.html"},{"title":"Designing and Interpreting Probes with Control Tasks | papers_we_read","url":"https://vlgiitr.github.io/papers_we_read/summaries/control_tasks.html"},{"title":"Designing and Interpreting Probes with Control Tasks","url":"https://www.researchgate.net/publication/335713697_Designing_and_Interpreting_Probes_with_Control_Tasks"},{"title":"[PDF] Designing and Interpreting Probes with Control Tasks | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Designing-and-Interpreting-Probes-with-Control-Hewitt-Liang/199ff73d2f728e997f860b62a2322823d3e3d9e8"},{"title":"Designing and Interpreting Probes with Control Tasks John Hewitt","url":"https://nlp.stanford.edu/pubs/hewitt2019control.pdf"}]

I found the paper! Here's what the search returned:

"Designing and Interpreting Probes with Control Tasks" is a paper by John Hewitt and Percy Liang published at the 2019 Conference on Empirical Methods in Natural Language Processing and the 9th International Joint Conference on Natural Language Processing (EMNLP-IJCNLP).

The paper examines probes—supervised models trained to predict linguistic properties from representations—and questions whether high accuracy means the representations encode linguistic structure or if the probe has simply learned the task.

The authors found that probes, especially complex neural network probes, are able to memorize a large number of labeling decisions independently of the linguistic properties of the representations. They constructed control tasks for English part-of-speech tagging and dependency edge prediction, and showed that popular probes on ELMo representations are not selective.

They define a metric called "selectivity" as: linguistic task accuracy minus control task accuracy, which measures whether a probe achieves high linguistic task accuracy while achieving low control task accuracy.

The paper received the Best Paper Runner Up Award at EMNLP 2019.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "4d797ca7-68b9-4987-8a1c-ff49a4874b0b",
  "isSidechain": true,
  "promptId": "f76ab8f1-cf60-4739-be49-0817894703ea",
  "agentId": "acc4b077cc6fe4048",
  "type": "user",
  "uuid": "e4191120-4a2a-4be7-b2ba-080366ab2720",
  "sourceToolAssistantUUID": "4d797ca7-68b9-4987-8a1c-ff49a4874b0b",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "a600395c-52af-4483-884f-a0137eaa6f5f",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 30 · 2026-05-19T12:01:41.110Z_

<details><summary>↩ Tool result · `toolu_01EUEvmZCPDfzzSdfC9zdknn`</summary>

```text
Web search results for query: "Elazar Ravfogel "amnesic probing" INLP nullspace projection causal information usage"

Links: [{"title":"Amnesic Probing: Behavioral Explanation with Amnesic Counterfactuals | Transactions of the Association for Computational Linguistics | MIT Press","url":"https://direct.mit.edu/tacl/article/doi/10.1162/tacl_a_00359/98091/Amnesic-Probing-Behavioral-Explanation-with"},{"title":"Amnesic Probing: Behavioral Explanation with Amnesic Counterfactuals | Shauli Ravfogel","url":"https://shauli-ravfogel.netlify.app/publication/amnesic-probing/"},{"title":"LEACE: Perfect linear concept erasure in closed form Nora Belrose1","url":"https://openreview.net/pdf?id=awIpKpwTwF"},{"title":"Improving Causal Interventions in Amnesic Probing with Mean Projection or LEACE","url":"https://arxiv.org/html/2506.11673v1"},{"title":"Interventional Probing in High Dimensions: An NLI Case ...","url":"https://aclanthology.org/2023.findings-eacl.188.pdf"},{"title":"(PDF) Interventional Probing in High Dimensions: An NLI Case Study","url":"https://www.researchgate.net/publication/370152810_Interventional_Probing_in_High_Dimensions_An_NLI_Case_Study"},{"title":"Iterative Nullspace Projection (INLP) | Shauli Ravfogel","url":"https://shauli-ravfogel.netlify.app/post/inlp/"},{"title":"[PDF] Amnesic Probing: Behavioral Explanation with Amnesic Counterfactuals | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Amnesic-Probing:-Behavioral-Explanation-with-Elazar-Ravfogel/1d7f3297924a9dd90cfc0df522ebe9138c28b46f"},{"title":"Null It Out: Guarding Protected Attributes by Iterative Nullspace Projection - ACL Anthology","url":"https://aclanthology.org/2020.acl-main.647/"}]

Based on the search results, here's what I found about Elazar Ravfogel's work on amnesic probing, INLP, and related concepts:

## Amnesic Probing

Amnesic probing focuses on how information is being used, rather than on what information is encoded. Amnesic probing is a causal intervention that aims to test the importance of a given concept (e.g. part-of-speech tag) to some main task (e.g. language modeling).

## Iterative Nullspace Projection (INLP)

INLP is a novel method for removing information from neural representations based on repeated training of linear classifiers that predict a certain property to be removed, followed by projection of the representations on their null-space. 

More specifically, INLP neutralizes the ability to linearly predict a property from representations by training a sequence of linear classifiers (probes) that predict the property, interpreting each one as conveying information on a unique direction in the latent space that corresponds to that property, and iteratively removing each of these directions.

## Causal Information Usage

This approach allows asking the counterfactual question: "How will the prediction of a task differ without access to some property?" and relies on the assumption that the usefulness of some information can be measured by neutralizing it from the representation, and witnessing the resulting behavioral change.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a65b4f01-1f0a-4399-b933-ccffa4d68ffe",
  "isSidechain": true,
  "promptId": "f76ab8f1-cf60-4739-be49-0817894703ea",
  "agentId": "acc4b077cc6fe4048",
  "type": "user",
  "uuid": "24967926-0649-4d6e-bbc8-d0ef0d062207",
  "sourceToolAssistantUUID": "a65b4f01-1f0a-4399-b933-ccffa4d68ffe",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "a600395c-52af-4483-884f-a0137eaa6f5f",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 31 · 2026-05-19T12:01:41.885Z_

<details><summary>↩ Tool result · `toolu_01KdC4HGVzemRUirHG3obdLj`</summary>

```text
Web search results for query: "probe accuracy inflation random baselines shuffled labels probing neural networks interpretability 2024 2025"

Links: [{"title":"Understanding Mechanistic Interpretability in AI Models 8/16/2025 • 40 min read","url":"https://intuitionlabs.ai/pdfs/understanding-mechanistic-interpretability-in-ai-models.pdf"},{"title":"Linear Probes: Neural Network Diagnostics","url":"https://www.emergentmind.com/topics/linear-probes"},{"title":"What is Probing Classifiers?","url":"https://h2o.ai/wiki/probing-classifiers/"},{"title":"A Benchmark for Interpretability Methods in Deep Neural Networks","url":"http://papers.neurips.cc/paper/9167-a-benchmark-for-interpretability-methods-in-deep-neural-networks.pdf"},{"title":"Probing Network Decisions: Capturing Uncertainties and Unveiling   Vulnerabilities Without Label Information","url":"https://arxiv.org/pdf/2503.09068"},{"title":"Probing the Probing Paradigm: Does Probing Accuracy Entail Task   Relevance?","url":"https://arxiv.org/pdf/2005.00719"}]

Based on the search results, I found relevant research on probing neural networks and interpretability issues. Here are the key findings:

## Probe Accuracy and Control Tasks

The notion of selectivity—defined as the gap between linguistic and control task accuracy—is central for meaningful interpretation, with high selectivity from a linear probe indicating features are truly encoded in representation, rather than artifacts of the probe.

## Issues with Probe Accuracy Inflation

Probes with too high capacity (deep MLPs, large hidden layers) can memorize or exploit superficial cues, such as word identity rather than true encoded structure.

Models can encode linguistic properties considerably above chance-level even when distributed in the data as random noise, calling into question the interpretation of absolute claims on probing tasks. This demonstrates that high probe accuracy doesn't necessarily entail that features are meaningful for the model's actual task.

## Random Baselines in Interpretability Methods

A random baseline allows answering the question: is the interpretability method more accurate than a random guess as to which features are important?

## Task Relevance Concerns

Research examining the probing paradigm shows that models can learn to encode linguistic properties even if they are not needed for the task on which the model was trained, and pretrained word embeddings play a considerable role in encoding these properties rather than the training task itself.

The search results highlight that probe accuracy can be inflated and may not reflect actual task relevance, emphasizing the importance of using proper controls and baselines when interpreting probing results.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "fd8b1d05-972b-4008-ab2f-e75a4eb4f7da",
  "isSidechain": true,
  "promptId": "f76ab8f1-cf60-4739-be49-0817894703ea",
  "agentId": "acc4b077cc6fe4048",
  "type": "user",
  "uuid": "cc775545-1f44-4157-a809-78916baccace",
  "sourceToolAssistantUUID": "fd8b1d05-972b-4008-ab2f-e75a4eb4f7da",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "a600395c-52af-4483-884f-a0137eaa6f5f",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 32 · 2026-05-19T12:01:44.464Z_

Let me get the details on two more critical papers.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "cc775545-1f44-4157-a809-78916baccace",
  "isSidechain": true,
  "agentId": "acc4b077cc6fe4048",
  "requestId": "req_011CbBtiV8XwbwUyGwo6p4wv",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "78ae46fb-cac7-42e3-84c8-887a39755001",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "a600395c-52af-4483-884f-a0137eaa6f5f",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018QysiCnAwVwaw4yottN5o9",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2921,
      "cache_read_input_tokens": 15661,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2921,
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

_source line 33 · 2026-05-19T12:01:46.292Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_014et698W9UGbb6ZA7DdvbP8`</summary>

```json
{
  "url": "https://arxiv.org/abs/2005.00719",
  "prompt": "Extract the full abstract and key findings. This paper \"Probing the Probing Paradigm\" seems directly relevant. What exactly do they find about when probe accuracy does NOT entail task relevance? What methods do they propose? What concrete evidence do they provide that probing accuracy can be misleading?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "78ae46fb-cac7-42e3-84c8-887a39755001",
  "isSidechain": true,
  "agentId": "acc4b077cc6fe4048",
  "requestId": "req_011CbBtiV8XwbwUyGwo6p4wv",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "e19aa377-f7d2-4fbd-aea3-ce51b40c3e0e",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "a600395c-52af-4483-884f-a0137eaa6f5f",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018QysiCnAwVwaw4yottN5o9",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2921,
      "cache_read_input_tokens": 15661,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2921,
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

_source line 34 · 2026-05-19T12:01:48.722Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01CBQsUn4mCN58YKAgbKmPA7`</summary>

```json
{
  "url": "https://direct.mit.edu/tacl/article/doi/10.1162/tacl_a_00359/98091/Amnesic-Probing-Behavioral-Explanation-with",
  "prompt": "Extract the full abstract and key findings of the amnesic probing paper. What is the core method? What do they find about probe accuracy vs actual information usage? What concrete examples show that high probe accuracy doesn't mean the information is causally used? What is their recommended methodology?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e19aa377-f7d2-4fbd-aea3-ce51b40c3e0e",
  "isSidechain": true,
  "agentId": "acc4b077cc6fe4048",
  "requestId": "req_011CbBtiV8XwbwUyGwo6p4wv",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "bc430e4f-1ae1-4202-8adb-37fd1190801d",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "a600395c-52af-4483-884f-a0137eaa6f5f",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018QysiCnAwVwaw4yottN5o9",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2921,
      "cache_read_input_tokens": 15661,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2921,
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

_source line 35 · 2026-05-19T12:01:48.941Z_

<details><summary>↩ Tool result · `toolu_01CBQsUn4mCN58YKAgbKmPA7`</summary>

```text
The server returned HTTP 403 Forbidden.

The response body was not retrieved. If this URL requires authentication, use an authenticated tool (e.g. `gh` for GitHub, or an MCP-provided fetch tool) instead of WebFetch.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "bc430e4f-1ae1-4202-8adb-37fd1190801d",
  "isSidechain": true,
  "promptId": "f76ab8f1-cf60-4739-be49-0817894703ea",
  "agentId": "acc4b077cc6fe4048",
  "type": "user",
  "uuid": "8fa5adfe-5fa1-4c52-9c3b-1c35b9f3750f",
  "sourceToolAssistantUUID": "bc430e4f-1ae1-4202-8adb-37fd1190801d",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "a600395c-52af-4483-884f-a0137eaa6f5f",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 36 · 2026-05-19T12:01:50.453Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01Mc4FQRPBnHkvUgbDvNVgrt`</summary>

```json
{
  "url": "https://direct.mit.edu/coli/article/48/1/207/107571/Probing-Classifiers-Promises-Shortcomings-and",
  "prompt": "Extract the abstract and key findings of this survey on probing classifiers. What shortcomings do they identify? What advances address probe inflation / overestimation? What is the state of the art in calibrating probes? What methods do they recommend?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8fa5adfe-5fa1-4c52-9c3b-1c35b9f3750f",
  "isSidechain": true,
  "agentId": "acc4b077cc6fe4048",
  "requestId": "req_011CbBtiV8XwbwUyGwo6p4wv",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "593bb2d1-7d3d-4da7-bf78-426af27c6fdd",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "a600395c-52af-4483-884f-a0137eaa6f5f",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018QysiCnAwVwaw4yottN5o9",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2921,
      "cache_read_input_tokens": 15661,
      "output_tokens": 457,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2921
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 457,
          "cache_read_input_tokens": 15661,
          "cache_creation_input_tokens": 2921,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2921,
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

_source line 37 · 2026-05-19T12:01:50.485Z_

<details><summary>↩ Tool result · `toolu_01Mc4FQRPBnHkvUgbDvNVgrt`</summary>

```text
The server returned HTTP 403 Forbidden.

The response body was not retrieved. If this URL requires authentication, use an authenticated tool (e.g. `gh` for GitHub, or an MCP-provided fetch tool) instead of WebFetch.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "593bb2d1-7d3d-4da7-bf78-426af27c6fdd",
  "isSidechain": true,
  "promptId": "f76ab8f1-cf60-4739-be49-0817894703ea",
  "agentId": "acc4b077cc6fe4048",
  "type": "user",
  "uuid": "775ae667-775a-4680-94eb-6a415e6b0b37",
  "sourceToolAssistantUUID": "593bb2d1-7d3d-4da7-bf78-426af27c6fdd",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "a600395c-52af-4483-884f-a0137eaa6f5f",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 38 · 2026-05-19T12:01:51.662Z_

<details><summary>↩ Tool result · `toolu_014et698W9UGbb6ZA7DdvbP8`</summary>

```text
# Summary: "Probing the Probing Paradigm"

## Full Abstract
The paper examines whether high probing task accuracy actually indicates that neural models use the discovered linguistic properties for their primary task. Through Natural Language Inference case studies, the authors demonstrate that models encode linguistic information even when unnecessary for task completion.

## Key Findings on Misleading Probe Accuracy

**Three main discoveries showing probe accuracy ≠ task relevance:**

1. **Unnecessary Information Encoding**: Models learn to encode linguistic properties that aren't required for the actual task they were trained on.

2. **Embedding Bias**: "pretrained word embeddings play a considerable role in encoding these properties rather than the training task itself," meaning probes may detect properties from embeddings rather than task-learned representations.

3. **Random Noise Encoding**: Through controlled synthetic experiments, the researchers found that "models can encode these properties considerably above chance-level even when distributed in the data as random noise," demonstrating that high probe accuracy provides misleading confidence about what models actually learned.

## Methods & Evidence
The authors used controlled synthetic tasks and Natural Language Inference experiments to isolate variables and test whether models encode information beyond what's functionally necessary, revealing fundamental issues with interpreting absolute probing claims.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "e19aa377-f7d2-4fbd-aea3-ce51b40c3e0e",
  "isSidechain": true,
  "promptId": "f76ab8f1-cf60-4739-be49-0817894703ea",
  "agentId": "acc4b077cc6fe4048",
  "type": "user",
  "uuid": "e2231720-7063-45a8-b643-99b0ed2b4dd3",
  "sourceToolAssistantUUID": "e19aa377-f7d2-4fbd-aea3-ce51b40c3e0e",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "a600395c-52af-4483-884f-a0137eaa6f5f",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 39 · 2026-05-19T12:01:55.014Z_

Let me try the arxiv versions of those papers, and also search for a few more methods.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e2231720-7063-45a8-b643-99b0ed2b4dd3",
  "isSidechain": true,
  "agentId": "acc4b077cc6fe4048",
  "requestId": "req_011CbBtjCwyc53VEiobw8XrD",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "4f4683d2-50e9-43e4-b399-c30e1cb5e529",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "a600395c-52af-4483-884f-a0137eaa6f5f",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015R1sgtwPj4aBbu74ahNQFz",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 163,
      "cache_creation_input_tokens": 761,
      "cache_read_input_tokens": 18582,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 761,
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

_source line 40 · 2026-05-19T12:01:56.823Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01NLY6cuCvLbcsSxQLeSgs4e`</summary>

```json
{
  "url": "https://arxiv.org/abs/2006.00995",
  "prompt": "Extract the full abstract and key findings of the amnesic probing paper by Elazar et al. What is the core method? What do they find about cases where high probe accuracy doesn't mean information is causally used? What concrete results show the gap between encoding and usage?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4f4683d2-50e9-43e4-b399-c30e1cb5e529",
  "isSidechain": true,
  "agentId": "acc4b077cc6fe4048",
  "requestId": "req_011CbBtjCwyc53VEiobw8XrD",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "7d91a8d1-d8a5-45d2-a63f-59ee75cb1215",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "a600395c-52af-4483-884f-a0137eaa6f5f",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015R1sgtwPj4aBbu74ahNQFz",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 163,
      "cache_creation_input_tokens": 761,
      "cache_read_input_tokens": 18582,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 761,
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

_source line 41 · 2026-05-19T12:01:57.268Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01WVgarwd4UiEFFCNB7K29g7`</summary>

```json
{
  "query": "Belinkov 2022 \"probing classifiers\" survey promises shortcomings advances computational linguistics"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7d91a8d1-d8a5-45d2-a63f-59ee75cb1215",
  "isSidechain": true,
  "agentId": "acc4b077cc6fe4048",
  "requestId": "req_011CbBtjCwyc53VEiobw8XrD",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "1b833178-64e6-4c19-84b9-fee6df4e8ba5",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "a600395c-52af-4483-884f-a0137eaa6f5f",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015R1sgtwPj4aBbu74ahNQFz",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 163,
      "cache_creation_input_tokens": 761,
      "cache_read_input_tokens": 18582,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 761,
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

_source line 42 · 2026-05-19T12:01:58.068Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01JrpsKGyeFQuhS4zwUidZ3B`</summary>

```json
{
  "query": "LEACE concept erasure Belrose 2024 linear probing calibration"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1b833178-64e6-4c19-84b9-fee6df4e8ba5",
  "isSidechain": true,
  "agentId": "acc4b077cc6fe4048",
  "requestId": "req_011CbBtjCwyc53VEiobw8XrD",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "9f20e458-d84d-4c44-a0a9-5486075a7352",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "a600395c-52af-4483-884f-a0137eaa6f5f",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015R1sgtwPj4aBbu74ahNQFz",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 163,
      "cache_creation_input_tokens": 761,
      "cache_read_input_tokens": 18582,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 761,
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

_source line 43 · 2026-05-19T12:01:58.802Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_013PdzWSgYhFrySEA4PiaE3R`</summary>

```json
{
  "query": "trajectory shape probing analysis chain-of-thought \"probe calibration\" OR \"normalized probe\" OR \"relative probe\" faithfulness 2024 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9f20e458-d84d-4c44-a0a9-5486075a7352",
  "isSidechain": true,
  "agentId": "acc4b077cc6fe4048",
  "requestId": "req_011CbBtjCwyc53VEiobw8XrD",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "cfa092fb-e825-4bd0-a52e-1e8878c0eb52",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "a600395c-52af-4483-884f-a0137eaa6f5f",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015R1sgtwPj4aBbu74ahNQFz",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 163,
      "cache_creation_input_tokens": 761,
      "cache_read_input_tokens": 18582,
      "output_tokens": 336,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 761
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 163,
          "output_tokens": 336,
          "cache_read_input_tokens": 18582,
          "cache_creation_input_tokens": 761,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 761,
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

_source line 44 · 2026-05-19T12:02:01.798Z_

<details><summary>↩ Tool result · `toolu_01NLY6cuCvLbcsSxQLeSgs4e`</summary>

```text
# Amnesic Probing: Core Method and Findings

## Full Abstract

The paper addresses limitations in probing methodology for neural models. The authors introduce **Amnesic Probing**, a technique that assesses information utility "by measuring the influence of a causal intervention that removes it from the representation" rather than simply detecting what information is encoded.

## Core Method

Amnesic Probing uses counterfactual analysis—removing specific linguistic properties from model representations and observing task performance changes. This shift from *what is encoded* to *how information is used* enables new research questions, such as determining whether part-of-speech tags actually matter for word prediction in BERT.

## Key Disconnect: Encoding vs. Usage

The critical finding is that "conventional probing performance is not correlated to task importance." The authors demonstrate a significant gap: properties may be detectable in model representations (high probe accuracy) yet remain causally irrelevant to model predictions.

## Concrete Evidence

While the provided content doesn't detail specific numerical results, the paper's initial title—"When Bert Forgets How To POS"—suggests their analysis revealed that BERT's part-of-speech information, despite being encodable, isn't actually necessary for masked language modeling. This exemplifies cases where high probe accuracy masks functional irrelevance.

The work fundamentally challenges drawing behavioral conclusions from probing results alone.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "7d91a8d1-d8a5-45d2-a63f-59ee75cb1215",
  "isSidechain": true,
  "promptId": "f76ab8f1-cf60-4739-be49-0817894703ea",
  "agentId": "acc4b077cc6fe4048",
  "type": "user",
  "uuid": "cf499c26-2cfb-439a-9afe-9cb4169e583d",
  "sourceToolAssistantUUID": "7d91a8d1-d8a5-45d2-a63f-59ee75cb1215",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "a600395c-52af-4483-884f-a0137eaa6f5f",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 45 · 2026-05-19T12:02:06.762Z_

<details><summary>↩ Tool result · `toolu_013PdzWSgYhFrySEA4PiaE3R`</summary>

```text
Web search results for query: "trajectory shape probing analysis chain-of-thought "probe calibration" OR "normalized probe" OR "relative probe" faithfulness 2024 2025"

Links: [{"title":"Mechanistic Evidence for Faithfulness Decay in Chain-of-Thought Reasoning","url":"https://arxiv.org/html/2602.11201v1"},{"title":"Entropy trajectory shape predicts LLM reasoning reliability: A diagnostic study of uncertainty dynamics in chain-of-thought","url":"https://arxiv.org/pdf/2603.18940"},{"title":"Making Reasoning Matter: Measuring and Improving Faithfulness of Chain-of-Thought Reasoning | Request PDF","url":"https://www.researchgate.net/publication/386203451_Making_Reasoning_Matter_Measuring_and_Improving_Faithfulness_of_Chain-of-Thought_Reasoning"},{"title":"MECHANISTIC EVIDENCE FOR FAITHFULNESS DECAY","url":"https://openreview.net/pdf?id=wVj7dB7waI"},{"title":"Task Difficulty Shapes Chain-of-Thought Faithfulness","url":"https://openreview.net/pdf/f2beacfb65623c951a3c9017791b7501159a3250.pdf"},{"title":"FaithCoT-Bench: Benchmarking Instance-Level Faithfulness of Chain-of-Thought Reasoning","url":"https://arxiv.org/html/2510.04040v1"},{"title":"Mechanistic Evidence for Faithfulness Decay in Chain-of-Thought Reasoning","url":"https://arxiv.org/pdf/2602.11201"}]

Based on the search results, I found several highly relevant papers that address your query about trajectory shape probing analysis in chain-of-thought reasoning with probe calibration and faithfulness:

## Key Papers Found:

**1. "Mechanistic Evidence for Faithfulness Decay in Chain-of-Thought Reasoning" (2026)**

This paper utilizes Trajectory Alignment Score (TAS) to characterize the geometry of reasoning paths. Notably, the paper operates in logit space and normalizes for cross-model comparison through NLDD, which addresses the problem that raw sensitivity metrics are not comparable across architectures due to differences in output scaling and baseline confidence.

The authors couple linear probes with Representational Similarity Analysis (RSA) to track the evolution of solution-relevant information across layers and measure alignment between clean and counterfactually corrupted reasoning trajectories.

**2. "Entropy trajectory shape predicts LLM reasoning reliability" (2025)**

This paper shows that token log-probability scores are systematically miscalibrated, with expected calibration error rising from 0.186 at step 0 to 0.312 at step 7. Entropy-trajectory monotonicity achieves +5.8 percentage points at 73.7% coverage, outperforming scalar baselines for predicting reasoning reliability.

**3. "FaithCoT-Bench: Benchmarking Instance-Level Faithfulness of Chain-of-Thought Reasoning" (2025)**

This benchmark evaluates eleven methods across four paradigms including counterfactual-based approaches (adding mistakes, removing steps), logit-based approaches (analyzing token-level logits), and LLM-as-Judge methods.

All papers directly address the intersection of trajectory analysis, probing methods, and faithfulness evaluation in chain-of-thought reasoning during 2024-2025.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "cfa092fb-e825-4bd0-a52e-1e8878c0eb52",
  "isSidechain": true,
  "promptId": "f76ab8f1-cf60-4739-be49-0817894703ea",
  "agentId": "acc4b077cc6fe4048",
  "type": "user",
  "uuid": "12b022ec-a2eb-436b-9714-a1935545e1ab",
  "sourceToolAssistantUUID": "cfa092fb-e825-4bd0-a52e-1e8878c0eb52",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "a600395c-52af-4483-884f-a0137eaa6f5f",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 46 · 2026-05-19T12:02:07.092Z_

<details><summary>↩ Tool result · `toolu_01JrpsKGyeFQuhS4zwUidZ3B`</summary>

```text
Web search results for query: "LEACE concept erasure Belrose 2024 linear probing calibration"

Links: [{"title":"LEACE: Perfect linear concept erasure in closed form","url":"https://www.researchgate.net/publication/401445190_LEACE_Perfect_linear_concept_erasure_in_closed_form"},{"title":"LEACE: Perfect linear concept erasure in closed form","url":"https://proceedings.neurips.cc/paper_files/paper/2023/hash/d066d21c619d0a78c5b557fa3291a8f4-Abstract-Conference.html"},{"title":"LEACE: Perfect linear concept erasure in closed form Nora Belrose1","url":"https://openreview.net/pdf?id=awIpKpwTwF"},{"title":"NeurIPS Poster LEACE: Perfect linear concept erasure in closed form","url":"https://neurips.cc/virtual/2023/poster/71176"},{"title":"LEACE: Perfect linear concept erasure in closed form","url":"https://arxiv.org/pdf/2306.03819"},{"title":"[2306.03819] LEACE: Perfect linear concept erasure in closed form","url":"https://arxiv.org/abs/2306.03819"},{"title":"(PDF) LEACE: Perfect linear concept erasure in closed form","url":"https://www.researchgate.net/publication/371347168_LEACE_Perfect_linear_concept_erasure_in_closed_form"}]

Based on the search results, here's what I found about LEACE and concept erasure:

## LEACE: Concept Erasure Overview

LEACE (LEAst-squares Concept Erasure) is a closed-form method which provably prevents all linear classifiers from detecting a concept while changing the representation as little as possible, as measured by various norms.

## Key Applications

LEACE is applied to large language models with a procedure called concept scrubbing, which erases target concept information from every layer in the network, and has been demonstrated on tasks like measuring the reliance of language models on part-of-speech information and reducing gender bias in BERT embeddings.

## Relationship to Linear Probing

The linear representation hypothesis posits that concepts are encoded as directions in representation space, with empirical support including linear probes and concept erasure. This connects to the linear probing and calibration aspects mentioned in your query.

## Historical Context

R-LACE was introduced for erasing linear concept subspaces via an adversarial game, and Belrose et al. (2023) later gave a closed-form solution (LEACE) that provably prevents all linear classifiers from detecting a concept.

The paper appears to be from NeurIPS 2023, authored by Nora Belrose and colleagues, and has become a significant contribution to the interpretability and fairness literature in machine learning.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "9f20e458-d84d-4c44-a0a9-5486075a7352",
  "isSidechain": true,
  "promptId": "f76ab8f1-cf60-4739-be49-0817894703ea",
  "agentId": "acc4b077cc6fe4048",
  "type": "user",
  "uuid": "3cf0b123-49cb-4263-b9b4-3e1bbe8ea716",
  "sourceToolAssistantUUID": "9f20e458-d84d-4c44-a0a9-5486075a7352",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "a600395c-52af-4483-884f-a0137eaa6f5f",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 47 · 2026-05-19T12:02:07.521Z_

<details><summary>↩ Tool result · `toolu_01WVgarwd4UiEFFCNB7K29g7`</summary>

```text
Web search results for query: "Belinkov 2022 "probing classifiers" survey promises shortcomings advances computational linguistics"

Links: [{"title":"Probing Classifiers: Promises, Shortcomings, and Advances | Computational Linguistics | MIT Press","url":"https://direct.mit.edu/coli/article/48/1/207/107571/Probing-Classifiers-Promises-Shortcomings-and"},{"title":"@article{belinkov-2022-probing,","url":"https://aclanthology.org/2022.cl-1.7.bib"},{"title":"[PDF] Probing Classifiers: Promises, Shortcomings, and Advances | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Probing-Classifiers:-Promises,-Shortcomings,-and-Belinkov/3dcfa05a1c162e6cab927c5b08d0444f7b6691f4"},{"title":"Probing Classifiers: Promises, Shortcomings, and Advances - ACL Anthology","url":"https://aclanthology.org/2022.cl-1.7/"},{"title":"Probing Classifiers: Promises, Shortcomings, and Advances - Technion - Israel Institute of Technology","url":"https://cris.technion.ac.il/en/publications/probing-classifiers-promises-shortcomings-and-advances/"},{"title":"Probing Classifiers: Promises, Shortcomings, and Advances - Israeli Research Community Portal","url":"https://cris.iucc.ac.il/en/publications/probing-classifiers-promises-shortcomings-and-advances/"},{"title":"Yonatan Belinkov | publications","url":"https://belinkov.com/publications/publicationstype/"},{"title":"[2102.12452] Probing Classifiers: Promises, Shortcomings, and Advances","url":"https://arxiv.org/abs/2102.12452"}]

I found the paper! Yonatan Belinkov published "Probing Classifiers: Promises, Shortcomings, and Advances" in Computational Linguistics 2022; 48(1): 207–219.

Probing classifiers have emerged as one of the prominent methodologies for interpreting and analyzing deep neural network models of natural language processing, with the basic idea being that a classifier is trained to predict some linguistic property from a model's representations—and has been used to examine a wide variety of models and properties. However, recent studies have demonstrated various methodological limitations of this approach, and this article critically reviews the probing classifiers framework, highlighting their promises, shortcomings, and advances.

The paper is available through multiple sources, including MIT Press, ACL Anthology, and arXiv.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "1b833178-64e6-4c19-84b9-fee6df4e8ba5",
  "isSidechain": true,
  "promptId": "f76ab8f1-cf60-4739-be49-0817894703ea",
  "agentId": "acc4b077cc6fe4048",
  "type": "user",
  "uuid": "4f1bb94c-3dd2-48de-920e-5f92859d0a13",
  "sourceToolAssistantUUID": "1b833178-64e6-4c19-84b9-fee6df4e8ba5",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "a600395c-52af-4483-884f-a0137eaa6f5f",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 48 · 2026-05-19T12:02:10.143Z_

Let me fetch the most relevant remaining papers for detailed findings.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4f1bb94c-3dd2-48de-920e-5f92859d0a13",
  "isSidechain": true,
  "agentId": "acc4b077cc6fe4048",
  "requestId": "req_011CbBtkNk7p26yzJECEBdTb",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "1355ae60-2caa-401d-b8d1-4d9cf83028e2",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "a600395c-52af-4483-884f-a0137eaa6f5f",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WcaLUKv51GVhByFGikjDFM",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1586,
      "cache_creation_input_tokens": 1648,
      "cache_read_input_tokens": 19343,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1648,
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

_source line 49 · 2026-05-19T12:02:12.646Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_016sKpt48ExHaz997wNxD3jb`</summary>

```json
{
  "url": "https://arxiv.org/abs/2602.11201",
  "prompt": "Extract the full abstract and key findings. Specifically: (1) What is the Trajectory Alignment Score (TAS)? (2) How do they use probes and what calibration do they apply? (3) What is NLDD and how does it normalize across models? (4) What do they find about faithfulness decay mechanistically? (5) How do they distinguish trajectory shapes when absolute values may be inflated?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1355ae60-2caa-401d-b8d1-4d9cf83028e2",
  "isSidechain": true,
  "agentId": "acc4b077cc6fe4048",
  "requestId": "req_011CbBtkNk7p26yzJECEBdTb",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "2b717eb2-368b-4b07-9ac5-b7fea097234b",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "a600395c-52af-4483-884f-a0137eaa6f5f",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WcaLUKv51GVhByFGikjDFM",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1586,
      "cache_creation_input_tokens": 1648,
      "cache_read_input_tokens": 19343,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1648,
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

_source line 50 · 2026-05-19T12:02:14.120Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01MTtxeGGogHtpBuGAZpfPg7`</summary>

```json
{
  "url": "https://arxiv.org/abs/2102.12452",
  "prompt": "Extract the full abstract and key findings of Belinkov's survey on probing classifiers. What specific shortcomings do they identify? What advances are discussed for addressing probe overestimation? What is the recommended methodology for practitioners? List all calibration techniques mentioned."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2b717eb2-368b-4b07-9ac5-b7fea097234b",
  "isSidechain": true,
  "agentId": "acc4b077cc6fe4048",
  "requestId": "req_011CbBtkNk7p26yzJECEBdTb",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "d45b0e48-e447-43a7-8ab2-38cda786e0f5",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "a600395c-52af-4483-884f-a0137eaa6f5f",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WcaLUKv51GVhByFGikjDFM",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1586,
      "cache_creation_input_tokens": 1648,
      "cache_read_input_tokens": 19343,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1648,
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

_source line 51 · 2026-05-19T12:02:15.931Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01Cqvx3nJo7rMrtPoDfTrx4Z`</summary>

```json
{
  "url": "https://arxiv.org/abs/2306.03819",
  "prompt": "Extract the full abstract and key findings of LEACE. How does it achieve concept erasure? How does it relate to probing? What is the key theoretical guarantee? How can it be used as a probe calibration tool (e.g., by erasing a concept and checking if probe accuracy drops)?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d45b0e48-e447-43a7-8ab2-38cda786e0f5",
  "isSidechain": true,
  "agentId": "acc4b077cc6fe4048",
  "requestId": "req_011CbBtkNk7p26yzJECEBdTb",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "1af0b7b6-d86f-47d0-9715-62babb52b22a",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "a600395c-52af-4483-884f-a0137eaa6f5f",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WcaLUKv51GVhByFGikjDFM",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1586,
      "cache_creation_input_tokens": 1648,
      "cache_read_input_tokens": 19343,
      "output_tokens": 434,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1648
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1586,
          "output_tokens": 434,
          "cache_read_input_tokens": 19343,
          "cache_creation_input_tokens": 1648,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1648,
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

_source line 52 · 2026-05-19T12:02:17.934Z_

<details><summary>↩ Tool result · `toolu_016sKpt48ExHaz997wNxD3jb`</summary>

```text
# Analysis of arXiv:2602.11201

Based on the webpage content provided, I can address some of your questions, though not all requested information appears in the available abstract:

## What is Available

**NLDD (Normalized Logit Difference Decay):**
The paper introduces NLDD as a metric that "measures whether individual reasoning steps are faithful to the model's decision-making process." It works by corrupting individual reasoning steps and measuring confidence drops, standardizing measurements to enable "rigorous cross-model comparison across different architectures."

**Key Mechanistic Finding:**
The research identifies a consistent "Reasoning Horizon (k*) at 70--85% of chain length, beyond which reasoning tokens have little or negative effect on the final answer."

**Faithfulness Insight:**
A notable discovery is that "models can encode correct internal representations while completely failing the task," demonstrating that "accuracy alone does not reveal whether a model actually reasons through its chain."

## What is Not in the Abstract

The webpage content does not include information about:
- Trajectory Alignment Score (TAS)
- Specific probe methodology and calibration approaches
- Methods for distinguishing trajectory shapes when absolute values may be inflated

The full paper (accessible via PDF link) would contain these methodological details. The abstract focuses on the NLDD metric and empirical findings rather than technical implementation details.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "2b717eb2-368b-4b07-9ac5-b7fea097234b",
  "isSidechain": true,
  "promptId": "f76ab8f1-cf60-4739-be49-0817894703ea",
  "agentId": "acc4b077cc6fe4048",
  "type": "user",
  "uuid": "3c694ccc-efc2-4f00-96d0-f24c5c4bfd81",
  "sourceToolAssistantUUID": "2b717eb2-368b-4b07-9ac5-b7fea097234b",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "a600395c-52af-4483-884f-a0137eaa6f5f",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 53 · 2026-05-19T12:02:21.068Z_

<details><summary>↩ Tool result · `toolu_01Cqvx3nJo7rMrtPoDfTrx4Z`</summary>

```text
# LEACE: Concept Erasure Overview

## Full Abstract

"Concept erasure aims to remove specified features from an embedding. It can improve fairness (e.g. preventing a classifier from using gender or race) and interpretability (e.g. removing a concept to observe changes in model behavior)." The method introduces LEACE (LEAst-squares Concept Erasure), which provides "a closed-form method which provably prevents all linear classifiers from detecting a concept while changing the embedding as little as possible."

## How It Achieves Concept Erasure

LEACE operates through a closed-form mathematical solution that projects embeddings to remove linear information about target concepts. The authors apply this via "concept scrubbing," a procedure that "erases target concept information from every layer in the network."

## Key Theoretical Guarantee

The critical guarantee is that LEACE "provably prevents all linear classifiers from detecting a concept" while simultaneously minimizing embedding changes across "a broad class of norms." This provides formal assurance of concept removal within the linear space.

## Relationship to Probing & Calibration

While the webpage doesn't explicitly detail probing relationships, the methodology inherently enables calibration: one can erase a concept then measure whether downstream probes fail to recover it, thereby validating the erasure's effectiveness and calibrating probe sensitivity thresholds.

## Demonstrated Applications

The authors tested LEACE on measuring language models' reliance on part-of-speech information and reducing gender bias in BERT embeddings.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "1af0b7b6-d86f-47d0-9715-62babb52b22a",
  "isSidechain": true,
  "promptId": "f76ab8f1-cf60-4739-be49-0817894703ea",
  "agentId": "acc4b077cc6fe4048",
  "type": "user",
  "uuid": "880c53e6-2f83-44cf-9807-0dbf0aabec17",
  "sourceToolAssistantUUID": "1af0b7b6-d86f-47d0-9715-62babb52b22a",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "a600395c-52af-4483-884f-a0137eaa6f5f",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 54 · 2026-05-19T12:02:28.235Z_

<details><summary>↩ Tool result · `toolu_01MTtxeGGogHtpBuGAZpfPg7`</summary>

```text
# Analysis of Belinkov's Probing Classifiers Survey

## Full Abstract

The webpage provides this abstract: "Probing classifiers have emerged as one of the prominent methodologies for interpreting and analyzing deep neural network models of natural language processing. The basic idea is simple -- a classifier is trained to predict some linguistic property from a model's representations -- and has been used to examine a wide variety of models and properties. However, recent studies have demonstrated various methodological limitations of this approach. This article critically reviews the probing classifiers framework, highlighting their promises, shortcomings, and advances."

## Limitations

The webpage content does **not** include:
- Specific shortcomings identified in the paper
- Details about advances for addressing probe overestimation
- Recommended methodology for practitioners
- Any calibration techniques mentioned

## What Is Available

The page only provides:
- Bibliographic metadata (submission dates, DOI, citation format)
- A high-level abstract describing the paper's general scope
- Links to access the full PDF

## Recommendation

To obtain the specific technical findings regarding shortcomings, advances, and methodological recommendations, you would need to access the full PDF of the paper via the arXiv link provided.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d45b0e48-e447-43a7-8ab2-38cda786e0f5",
  "isSidechain": true,
  "promptId": "f76ab8f1-cf60-4739-be49-0817894703ea",
  "agentId": "acc4b077cc6fe4048",
  "type": "user",
  "uuid": "7efd81fb-6e96-442e-a55c-6722aff9f59d",
  "sourceToolAssistantUUID": "d45b0e48-e447-43a7-8ab2-38cda786e0f5",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "a600395c-52af-4483-884f-a0137eaa6f5f",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 55 · 2026-05-19T12:02:31.054Z_

Now let me do one final round of targeted searches for additional methods.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7efd81fb-6e96-442e-a55c-6722aff9f59d",
  "isSidechain": true,
  "agentId": "acc4b077cc6fe4048",
  "requestId": "req_011CbBtmuHgMr2cHmZ43scvm",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "4b0c27c7-5e5e-4424-88d0-7a629985d408",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "a600395c-52af-4483-884f-a0137eaa6f5f",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WJGacbzvEDBpejegqcTUtA",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 367,
      "cache_creation_input_tokens": 2640,
      "cache_read_input_tokens": 20991,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2640,
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

_source line 56 · 2026-05-19T12:02:31.996Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01K7siaExA7f5KZZoKWh6qjK`</summary>

```json
{
  "query": "manifold capacity theory MCT separability probing alternative 2025 2026 representation geometry"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4b0c27c7-5e5e-4424-88d0-7a629985d408",
  "isSidechain": true,
  "agentId": "acc4b077cc6fe4048",
  "requestId": "req_011CbBtmuHgMr2cHmZ43scvm",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "2dbc7fe1-47a3-4020-b504-27e9bff928c2",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "a600395c-52af-4483-884f-a0137eaa6f5f",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WJGacbzvEDBpejegqcTUtA",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 367,
      "cache_creation_input_tokens": 2640,
      "cache_read_input_tokens": 20991,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2640,
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

_source line 57 · 2026-05-19T12:02:32.772Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01MCenxBSX9iTZPieFYXFHqp`</summary>

```json
{
  "query": "\"minimum description length\" probing OR MDL probe complexity linguistic representations Voita 2020"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2dbc7fe1-47a3-4020-b504-27e9bff928c2",
  "isSidechain": true,
  "agentId": "acc4b077cc6fe4048",
  "requestId": "req_011CbBtmuHgMr2cHmZ43scvm",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "716d5f43-135d-4ec7-b320-f8651be3cca6",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "a600395c-52af-4483-884f-a0137eaa6f5f",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WJGacbzvEDBpejegqcTUtA",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 367,
      "cache_creation_input_tokens": 2640,
      "cache_read_input_tokens": 20991,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2640,
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

_source line 58 · 2026-05-19T12:02:39.759Z_

<details><summary>↩ Tool result · `toolu_01K7siaExA7f5KZZoKWh6qjK`</summary>

```text
Web search results for query: "manifold capacity theory MCT separability probing alternative 2025 2026 representation geometry"

Links: [{"title":"Emergent Manifold Separability during Reasoning in Large Language Models","url":"https://arxiv.org/html/2602.20338"},{"title":"[2602.20338] Emergent Manifold Separability during Reasoning in Large Language Models","url":"https://arxiv.org/abs/2602.20338"},{"title":"Emergent Manifold Separability during Reasoning in Large Language Models","url":"https://arxiv.org/pdf/2602.20338"},{"title":"Probing Biological and Artificial Neural Networks with Task ...","url":"https://proceedings.mlr.press/v234/kuoch24a/kuoch24a.pdf"},{"title":"Probing Biological and Artificial Neural Networks with Task-dependent Neural Manifolds","url":"https://arxiv.org/html/2312.14285"},{"title":"The geometry of primary visual cortex representations is dynamically","url":"https://2025.ccneuro.org/abstract_pdf/Caglar_2025_The_geometry_primary_visual_cortex_representations.pdf"},{"title":"(PDF) Structural Manifold Compression: A Geometric Theory of Computational Limits","url":"https://www.academia.edu/150260707/Structural_Manifold_Compression_A_Geometric_Theory_of_Computational_Limits"}]

I found relevant search results for your query. Here are the key findings:

## Recent Research on Manifold Capacity Theory and Representation Geometry (2025-2026)

Manifold Capacity Theory (MCT) is used to analyze latent spaces, quantifying linear separability as an intrinsic geometric property without needing to train a classifier, unlike probing approaches.

### Current Applications in Large Language Models (2026)

A recent February 2026 paper examines MCT in the context of reasoning. The research applies Manifold Capacity Theory to a compositional Boolean logic task, allowing quantification of linear separability of latent representations without the confounding factors of probe training. The analysis reveals that reasoning manifests as a transient geometric pulse, where concept manifolds are untangled into linearly separable subspaces immediately prior to computation and rapidly compressed thereafter.

### Alternative to Standard Probing

This behavior diverges from standard linear probe accuracy, which remains high long after computation, suggesting a fundamental distinction between information that is merely retrievable and information that is geometrically prepared for processing.

### Broader Applications

The manifold capacity theory framework examines a system's capacity to linearly separate neural representational manifolds, and has shown that changes in the manifold's radius, dimensionality, and alignment predict the classification capacity of a system and its ability to generalize.

These recent works demonstrate MCT as an alternative to traditional linear probing for understanding representation geometry in neural networks.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "2dbc7fe1-47a3-4020-b504-27e9bff928c2",
  "isSidechain": true,
  "promptId": "f76ab8f1-cf60-4739-be49-0817894703ea",
  "agentId": "acc4b077cc6fe4048",
  "type": "user",
  "uuid": "f44e7c0a-aef3-4a6d-b1e9-ab8fe9eb89e9",
  "sourceToolAssistantUUID": "2dbc7fe1-47a3-4020-b504-27e9bff928c2",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "a600395c-52af-4483-884f-a0137eaa6f5f",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 59 · 2026-05-19T12:02:40.897Z_

<details><summary>↩ Tool result · `toolu_01MCenxBSX9iTZPieFYXFHqp`</summary>

```text
Web search results for query: ""minimum description length" probing OR MDL probe complexity linguistic representations Voita 2020"

Links: [{"title":"Information-Theoretic Probing with Minimum Description Length | Request PDF","url":"https://www.researchgate.net/publication/347232984_Information-Theoretic_Probing_with_Minimum_Description_Length"},{"title":"Information-Theoretic Probing with Minimum Description Length - ACL Anthology","url":"https://aclanthology.org/2020.emnlp-main.14/"},{"title":"GitHub - lena-voita/description-length-probing: This is a repository with the code for the EMNLP 2020 paper \"Information-Theoretic Probing with Minimum Description Length\"","url":"https://github.com/lena-voita/description-length-probing"},{"title":"[2003.12298] Information-Theoretic Probing with Minimum Description Length","url":"https://arxiv.org/abs/2003.12298"},{"title":"Information-Theoretic Probing with MDL","url":"https://lena-voita.github.io/posts/mdl_probes.html"},{"title":"Webinar: Information-Theoretic Probing with Minimum Description Length, 23 July 2020 | DOU","url":"https://dou.ua/calendar/33492/"},{"title":"Information-Theoretic Probing with Minimum Description Length","url":"https://scite.ai/reports/information-theoretic-probing-with-minimum-description-xX0Adl1J"},{"title":"[Quick Review] Information-Theoretic Probing with Minimum Description Length","url":"https://liner.com/review/informationtheoretic-probing-with-minimum-description-length"}]

I found relevant results for your query. Here's what the search returned:

## Information-Theoretic Probing with Minimum Description Length (Voita & Titov, 2020)

Elena Voita and Ivan Titov published "Information-Theoretic Probing with Minimum Description Length" in 2020 at the Conference on Empirical Methods in Natural Language Processing (EMNLP).

### Key Concept

The paper proposes information-theoretic probing which measures minimum description length (MDL) of labels given representations, characterizing both probe quality and the amount of effort needed to achieve it. The measure changes from probe accuracy to the description length of labels given representations, which evaluates "the amount of effort" needed to achieve quality, characterized by either the size of a probing model or the amount of data needed to achieve high quality.

### Methods and Results

The authors consider two methods for estimating MDL which can be easily implemented on top of standard probing pipelines: variational coding and online coding, showing that these methods agree in results and are more informative and stable than standard probes.

### Motivation

While probes have been widely adopted, differences in their accuracy fail to adequately reflect differences in representations, and do not substantially favor pretrained representations over randomly initialized ones.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "716d5f43-135d-4ec7-b320-f8651be3cca6",
  "isSidechain": true,
  "promptId": "f76ab8f1-cf60-4739-be49-0817894703ea",
  "agentId": "acc4b077cc6fe4048",
  "type": "user",
  "uuid": "519ac25d-b1e2-47b7-ad4e-fa4142794972",
  "sourceToolAssistantUUID": "716d5f43-135d-4ec7-b320-f8651be3cca6",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "a600395c-52af-4483-884f-a0137eaa6f5f",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 60 · 2026-05-19T12:02:45.402Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01VHZarhjBLmBmCDCLwJ3ADb`</summary>

```json
{
  "url": "https://arxiv.org/abs/2003.12298",
  "prompt": "Extract the full abstract and key findings. (1) How does MDL probing differ from standard accuracy-based probing? (2) What specific problem does it solve regarding probe inflation/overestimation? (3) What are the two methods (variational coding, online coding)? (4) What did they find when comparing pretrained vs random representations? (5) How can this be used as a calibration baseline?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "519ac25d-b1e2-47b7-ad4e-fa4142794972",
  "isSidechain": true,
  "agentId": "acc4b077cc6fe4048",
  "requestId": "req_011CbBtnqSXQKR9CQrk1fvAR",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "e36bb376-a40c-48d4-9ecd-15cc0be187f7",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "a600395c-52af-4483-884f-a0137eaa6f5f",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012DX6ZBiqPQXP1FsNJjEnrC",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2001,
      "cache_read_input_tokens": 23631,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2001,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 66,
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

_source line 61 · 2026-05-19T12:02:48.663Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01PKpr2fccKp14421Wi3ezDX`</summary>

```json
{
  "url": "https://www.cs.columbia.edu/~johnhew/interpreting-probes.html",
  "prompt": "Extract the key methodological details about control tasks and selectivity from John Hewitt's page. (1) Exact definition of selectivity. (2) How to construct a control task (e.g., random word-to-label mapping). (3) What selectivity scores indicate good vs bad probes. (4) The key finding about MLP probes having low selectivity. (5) Concrete practical advice for researchers using probes."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e36bb376-a40c-48d4-9ecd-15cc0be187f7",
  "isSidechain": true,
  "agentId": "acc4b077cc6fe4048",
  "requestId": "req_011CbBtnqSXQKR9CQrk1fvAR",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "bbc327a6-2425-4095-9759-56e6384be329",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "a600395c-52af-4483-884f-a0137eaa6f5f",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012DX6ZBiqPQXP1FsNJjEnrC",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2001,
      "cache_read_input_tokens": 23631,
      "output_tokens": 339,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2001
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 339,
          "cache_read_input_tokens": 23631,
          "cache_creation_input_tokens": 2001,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2001,
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

_source line 62 · 2026-05-19T12:02:52.044Z_

<details><summary>↩ Tool result · `toolu_01VHZarhjBLmBmCDCLwJ3ADb`</summary>

```text
# Information-Theoretic Probing with Minimum Description Length: Key Findings

## Full Abstract Summary
The paper addresses a fundamental limitation in how researchers evaluate linguistic representations. Standard probe accuracy fails to meaningfully distinguish between pretrained and randomly initialized representations, and cannot reliably differentiate genuine linguistic tasks from synthetic random tasks without artificial constraints.

## Key Differences from Standard Probing

MDL probing reframes the problem fundamentally: instead of measuring "how accurately can we predict labels," it asks "how much information must we transmit to encode those labels given representations?" As stated: "the measure of interest changes from probe accuracy to the description length of labels given representations."

This shift captures not just prediction quality but "the amount of effort needed to achieve the quality," reflecting either model size or data requirements.

## Problem Solved: Probe Inflation

Standard probes suffer from inflated accuracy metrics. The paper demonstrates that standard approaches "do not substantially favour pretrained representations over randomly initialized ones" and show similar accuracy "when probing for genuine linguistic labels and probing for random synthetic tasks." MDL's dual-component measurement (quality + effort) prevents this overestimation by penalizing unnecessary model complexity.

## Two Implementation Methods

1. **Variational coding** - A probabilistic approach to estimate description length
2. **Online coding** - A sequential method for MDL estimation

Both methods "can be easily implemented on top of the standard probing pipelines" and "agree in results."

## Comparison Results

The paper demonstrates these methods are "more informative and stable than the standard probes," providing meaningful differentiation where standard accuracy-based approaches fail.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "e36bb376-a40c-48d4-9ecd-15cc0be187f7",
  "isSidechain": true,
  "promptId": "f76ab8f1-cf60-4739-be49-0817894703ea",
  "agentId": "acc4b077cc6fe4048",
  "type": "user",
  "uuid": "5fa36497-1319-419c-87c7-3c872e223364",
  "sourceToolAssistantUUID": "e36bb376-a40c-48d4-9ecd-15cc0be187f7",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "a600395c-52af-4483-884f-a0137eaa6f5f",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 63 · 2026-05-19T12:02:55.962Z_

<details><summary>↩ Tool result · `toolu_01PKpr2fccKp14421Wi3ezDX`</summary>

```text
# Key Methodological Details on Control Tasks and Selectivity

## (1) Exact Definition of Selectivity

Selectivity is mathematically defined as: "the difference between control task accuracy and linguistic task accuracy achievable by a probe family for a given representation." In practical terms, it measures how much a probe's performance on real linguistic tasks exceeds its performance on random, memorized assignments.

## (2) Constructing Control Tasks

Control tasks employ a two-step process. First, assign each word type (vocabulary entry) a random label: "independently sample a control behavior C(v) for each v ∈ V." Second, apply this mapping consistently: "the control task maps each token to the label specified by the behavior C(x_i)." Crucially, "control tasks associate word types with random labels; by construction, they can only be learned by the probe itself."

## (3) Interpreting Selectivity Scores

Higher selectivity indicates healthier probes. Low selectivity suggests the probe memorizes word identities rather than discovering linguistic structure. When comparing representations, "probes on ELMo2 are considerably less able to rely on word identities," indicating they capture genuine linguistic properties rather than surface features.

## (4) MLP Probe Finding

The research demonstrates that "linear and bilinear probes are considerably more selective than multi-layer perceptron probes," with MLPs showing "significant loss of selectivity" despite marginal accuracy gains.

## (5) Practical Researcher Guidance

Use 10-dimensional MLPs instead of standard 100-1000 dimensional architectures to improve selectivity while maintaining performance. Always report both linguistic and control task accuracies together when publishing probing results.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "bbc327a6-2425-4095-9759-56e6384be329",
  "isSidechain": true,
  "promptId": "f76ab8f1-cf60-4739-be49-0817894703ea",
  "agentId": "acc4b077cc6fe4048",
  "type": "user",
  "uuid": "c0b3df2c-f814-432f-a700-4702e5429559",
  "sourceToolAssistantUUID": "bbc327a6-2425-4095-9759-56e6384be329",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "a600395c-52af-4483-884f-a0137eaa6f5f",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 64 · 2026-05-19T12:04:09.089Z_

Now I have comprehensive information. Let me compile the findings into a thorough report.

---

Here is a structured research report with concrete methods you can use for probe calibration in your chain-of-thought faithfulness diagnosis proposal.

---

## 1. Control Tasks and Selectivity Scores (Hewitt & Liang, EMNLP 2019)

**Paper:** "Designing and Interpreting Probes with Control Tasks" -- [ACL Anthology](https://aclanthology.org/D19-1275/) | [Stanford PDF](https://nlp.stanford.edu/pubs/hewitt2019control.pdf) | [John Hewitt's blog](https://www.cs.columbia.edu/~johnhew/interpreting-probes.html)

**Core method:**
- Define a **control task** by assigning each word type a random label (independently sampled). By construction, this task can only be "solved" by the probe memorizing word identities, not by detecting genuine structure in representations.
- **Selectivity** = linguistic task accuracy - control task accuracy.
- High selectivity means the probe succeeds *because of* linguistic structure in the labels, not because the probe memorizes surface features.

**Key finding for your proposal:** MLP probes achieve very low selectivity (e.g., 97.3% on POS tagging but 92.8% on the control task = 4.5 selectivity), while linear probes achieve much higher selectivity (97.2% vs 71.2% = 26.0 selectivity). This directly addresses your reviewer's concern: you should report selectivity alongside accuracy, and use linear probes rather than MLPs.

**How to apply:** For your CoT faithfulness probes, train a parallel "null probe" on shuffled labels (random assignment of faithfulness labels to hidden states). Report `selectivity = real_accuracy - shuffled_accuracy`. If selectivity is low, the probe is capturing correlative/epiphenomenal information.

---

## 2. MDL Probing (Voita & Titov, EMNLP 2020)

**Paper:** "Information-Theoretic Probing with Minimum Description Length" -- [arXiv:2003.12298](https://arxiv.org/abs/2003.12298) | [Lena Voita's blog](https://lena-voita.github.io/posts/mdl_probes.html) | [GitHub](https://github.com/lena-voita/description-length-probing)

**Core method:**
- Replace probe accuracy with **minimum description length (MDL)** of labels given representations. This measures both quality AND the effort needed to achieve it (model size or data requirements).
- Two estimation methods: **variational coding** and **online coding**, both easily implemented on top of standard probing pipelines.

**Key finding:** Standard probe accuracy does NOT substantially favor pretrained representations over randomly initialized ones, and shows similar accuracy for genuine linguistic tasks vs. random synthetic tasks. MDL probing solves this by penalizing unnecessary complexity -- it is "more informative and stable than standard probes."

**How to apply:** Instead of reporting only probe accuracy for faithfulness detection, report MDL (codelength). If a probe on genuine faithfulness labels requires similar codelength to a probe on random labels, the information is not genuinely structured in the representations. This directly addresses the "uniformly high accuracy" concern.

---

## 3. Amnesic Probing (Elazar et al., TACL 2021)

**Paper:** "Amnesic Probing: Behavioral Explanation with Amnesic Counterfactuals" -- [arXiv:2006.00995](https://arxiv.org/abs/2006.00995) | [MIT Press](https://direct.mit.edu/tacl/article/doi/10.1162/tacl_a_00359/98091/Amnesic-Probing-Behavioral-Explanation-with)

**Core method:**
- Use **Iterative Nullspace Projection (INLP)** to remove a property from representations, then test whether the model's downstream performance changes.
- The key shift: from "what is encoded?" to "how is information used?" -- a counterfactual causal intervention.

**Critical finding:** "Conventional probing performance is not correlated to task importance." Properties may be detectable (high probe accuracy) yet causally irrelevant to model predictions. For example, BERT encodes POS information but removing it via INLP does not hurt masked language modeling -- the information is epiphenomenal.

**How to apply:** After training your faithfulness probes, use INLP/LEACE to erase the detected "faithfulness-relevant" directions from hidden states, then check if the model's CoT behavior actually changes. If erasing the information doesn't change outputs, the probe was detecting correlative rather than causally relevant information.

**Important caveat:** INLP introduces random modifications. Use **LEACE** or **Mean Projection** instead for cleaner erasure (see next item).

---

## 4. LEACE and Improved Amnesic Probing (Belrose et al., NeurIPS 2023; Dobrzeniecka et al., ACL 2025)

**Papers:**
- "LEACE: Perfect linear concept erasure in closed form" -- [arXiv:2306.03819](https://arxiv.org/abs/2306.03819)
- "Improving Causal Interventions in Amnesic Probing with Mean Projection or LEACE" -- [arXiv:2506.11673](https://arxiv.org/abs/2506.11673) | [ACL 2025 Findings](https://aclanthology.org/2025.findings-acl.674/)

**Core method:**
- LEACE provides a closed-form projection that **provably prevents all linear classifiers** from detecting a concept while changing representations minimally.
- The 2025 paper shows that LEACE and Mean Projection are strictly better than INLP for amnesic probing because INLP introduces random noise, while LEACE/MP perform surgical, minimal-perturbation erasure.

**How to apply:** Use LEACE as your concept erasure method when doing amnesic probing of faithfulness information. LEACE's theoretical guarantee (no linear classifier can recover the erased concept) makes it the strongest tool for testing whether detected information is causally used.

---

## 5. Latent Causal Probing (2024)

**Paper:** "Latent Causal Probing: A Formal Perspective on Probing with Causal Models of Data" -- [arXiv:2407.13765](https://arxiv.org/abs/2407.13765)

**Core method:**
- Formalizes probing using **structural causal models (SCMs)**, isolating the causal path through the language model while excluding the probe's influence.
- Distinguishes between **correlation** (information present in representations) and **causal use** (information actually employed by the model).
- Validated on synthetic tasks where the true causal structure is known.

**How to apply:** If you can design tasks where the ground-truth causal relationship between CoT faithfulness and internal representations is known (e.g., synthetic reasoning tasks), this framework lets you formally verify that your probes capture causal rather than correlative information.

---

## 6. Manifold Capacity Theory -- Chun et al. (arXiv:2602.20338)

**Paper:** "Emergent Manifold Separability during Reasoning in Large Language Models" by Polo, Chun, & Chung -- [arXiv:2602.20338](https://arxiv.org/abs/2602.20338)

**Core method:**
- Applies **Manifold Capacity Theory (MCT)** to quantify linear separability of concept manifolds *without training a probe at all*. MCT measures intrinsic geometric properties of the representation space (radius, dimensionality, alignment of concept manifolds).

**Critical finding for your proposal:** Linear probe accuracy remains high long after computation is complete, but **geometric separability (MCT) peaks transiently just before computation and compresses rapidly afterward**. They call this a "geometric pulse." This is direct evidence that probe accuracy captures information that is *merely retrievable* (epiphenomenal), not information that is *geometrically prepared for processing* (causally relevant).

The mechanism they propose -- **Dynamic Manifold Management** -- describes how models dynamically modulate representational capacity to optimize the residual stream's bandwidth during reasoning chains.

**How to apply:** This is perhaps the strongest paper for your reviewer response. MCT gives you a probe-free metric of representational readiness that dissociates from probe accuracy. You could:
1. Track MCT separability across CoT reasoning steps alongside probe accuracy.
2. Show that MCT separability has a characteristic temporal profile (the "geometric pulse") even when probe accuracy is flat/high.
3. Use the *shape* of the MCT trajectory (timing and magnitude of the pulse) as your diagnostic, rather than absolute probe accuracy values.

---

## 7. Trajectory-Shape Methods for CoT Faithfulness

**Paper:** "Mechanistic Evidence for Faithfulness Decay in Chain-of-Thought Reasoning" -- [arXiv:2602.11201](https://arxiv.org/abs/2602.11201)

**Key methods relevant to your concern about trajectory shapes vs. absolute values:**
- **Normalized Logit Difference Decay (NLDD):** Corrupts individual reasoning steps and measures confidence drops, with normalization that enables rigorous cross-model comparison regardless of output scaling differences. This addresses the problem that raw sensitivity metrics are inflated/incomparable across architectures.
- **Reasoning Horizon (k*):** They identify a consistent point at 70-85% of chain length beyond which reasoning tokens have little or negative effect on the final answer.
- Critical finding: "Models can encode correct internal representations while completely failing the task" -- accuracy alone does not reveal whether a model actually reasons through its chain.

**Paper:** "Entropy trajectory shape predicts LLM reasoning reliability" -- [arXiv:2603.18940](https://arxiv.org/pdf/2603.18940)
- Uses **entropy-trajectory monotonicity** rather than absolute values. Achieves +5.8pp at 73.7% coverage, outperforming scalar baselines.
- Shows that token log-probability scores are systematically miscalibrated (ECE rises from 0.186 to 0.312 across reasoning steps).

**How to apply:** Use NLDD-style normalization so your probe trajectories are comparable across models and robust to inflation. Focus on trajectory *shape* features (timing of peaks, monotonicity, inflection points) rather than absolute accuracy values.

---

## 8. "Probing the Probing Paradigm" (Ravichander et al., 2020)

**Paper:** "Probing the Probing Paradigm: Does Probing Accuracy Entail Task Relevance?" -- [arXiv:2005.00719](https://arxiv.org/abs/2005.00719)

**Key finding directly addressing your reviewer's concern:** Models encode linguistic properties "considerably above chance-level even when distributed in the data as random noise." Pretrained word embeddings, not task training, account for much of the encoded information. This means high probe accuracy can be entirely epiphenomenal.

---

## 9. Belinkov Survey (Computational Linguistics, 2022)

**Paper:** "Probing Classifiers: Promises, Shortcomings, and Advances" -- [arXiv:2102.12452](https://arxiv.org/abs/2102.12452) | [MIT Press](https://direct.mit.edu/coli/article/48/1/207/107571/Probing-Classifiers-Promises-Shortcomings-and)

A comprehensive survey covering all the methodological limitations. Useful as a reference for motivating your calibration approach.

---

## Concrete Recommendations for Your Proposal

Here is a calibration toolkit you could propose, ordered from simplest to most rigorous:

**Tier 1 -- Baselines (minimal effort, should always do):**
1. **Shuffled-label control probes** (Hewitt & Liang 2019): Train probes on randomly assigned faithfulness labels. Report selectivity = real accuracy - control accuracy.
2. **Random-representation baseline**: Train probes on random vectors of the same dimensionality. If accuracy is still high, your probe is too expressive.

**Tier 2 -- Information-theoretic calibration (moderate effort):**
3. **MDL probing** (Voita & Titov 2020): Replace accuracy with codelength. Genuine structure requires less description length than random assignments. Implementations available on GitHub.

**Tier 3 -- Causal validation (higher effort, strongest evidence):**
4. **Amnesic probing with LEACE** (Belrose et al. 2023; Dobrzeniecka et al. 2025): Erase the detected "faithfulness" directions from hidden states using LEACE, then check if model behavior changes. If not, the information is epiphenomenal.
5. **Latent Causal Probing** (2024): For synthetic tasks where you control ground truth, use SCM-based probing to formally distinguish correlation from causation.

**Tier 4 -- Geometry-based alternatives (probe-free, addresses inflation directly):**
6. **Manifold Capacity Theory** (Polo, Chun & Chung 2026): Track geometric separability across reasoning steps without training a probe. Compare MCT trajectory shape with probe accuracy trajectory -- the divergence between them is itself diagnostic of epiphenomenal encoding.

**For trajectory analysis specifically:**
7. **NLDD normalization** (arXiv:2602.11201): Normalize probe/sensitivity metrics across models to make trajectory shapes comparable despite absolute value inflation.
8. **Trajectory shape features**: Analyze timing of peaks, monotonicity, inflection points rather than absolute accuracy values. The "geometric pulse" pattern from MCT provides a template for what genuine computational readiness looks like vs. flat/high epiphenomenal encoding.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c0b3df2c-f814-432f-a700-4702e5429559",
  "isSidechain": true,
  "agentId": "acc4b077cc6fe4048",
  "requestId": "req_011CbBtowqmuvXkbmFoYbGeZ",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "232968b9-ba1b-466d-8075-3f023863db6f",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "a600395c-52af-4483-884f-a0137eaa6f5f",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MgNTtStvdpBhTZF3PMs4bH",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1129,
      "cache_read_input_tokens": 25632,
      "output_tokens": 3358,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1129
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 3358,
          "cache_read_input_tokens": 25632,
          "cache_creation_input_tokens": 1129,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1129,
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
