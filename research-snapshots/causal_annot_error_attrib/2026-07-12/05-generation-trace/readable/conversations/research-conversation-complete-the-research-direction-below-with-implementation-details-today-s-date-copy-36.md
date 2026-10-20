# Research conversation: Complete the research direction below with implementation details. **Today's date: 2026-05-27 (UTC).** Only recommend ve

**Multi-Class Annotation Errors in Causal Inference: Topology-Dependent Bias, Sensitivity, and Correction (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 29
- **Recorded user turns:** 1
- **Tool calls:** 5
- **Original source:** `logs/chats/exported-trajectories/account-2/17534bdc-c682-449b-afbd-9cd4dfa99aa8.jsonl`
- **Structured JSON:** [`aa8102c37410b5cfcbf5.json`](../../sessions/aa/aa8102c37410b5cfcbf5.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-27T08:03:28.508Z_

```json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-27T08:03:28.508Z",
  "sessionId": "17534bdc-c682-449b-afbd-9cd4dfa99aa8",
  "content": "Complete the research direction below with implementation details.\n\n**Today's date: 2026-05-27 (UTC).** Only recommend venues whose deadline has NOT yet passed.\n\n{\n  \"title\": \"Premise-Graph Contrastive Training for Logic-Grounded Process Reward Models\",\n  \"core_problem\": \"Current process reward models confuse surface fluency with logical validity — 43% of PRM reward gains are attributable to stylistic shortcuts rather than reasoning correctness — leading to catastrophic reward hacking during RL training where policies achieve >0.9 PRM scores but <4% actual accuracy. Can we train PRMs that are invariant to surface form but sensitive to logical structure?\",\n  \"opportunity\": \"PERL (ICML 2025) demonstrated that LLMs can extract premise dependency links between reasoning steps at 90% recall, and that premise-aware verification improves error detection by 6-16%. However, this structural information has only been used at evaluation time, not for PRM training. Simultaneously, DAG-Math (2025) and ProofFlow (2025) have made dependency graph extraction from mathematical reasoning chains feasible. No prior work combines these premise dependency structures with contrastive PRM training to explicitly disentangle logical validity from surface fluency — addressing the documented root cause of PRM fragility at training time rather than through post-hoc corrections.\",\n  \"landscape\": \"The field has documented severe PRM robustness failures: 'Reward Under Attack' (arXiv:2603.06621, March 2026) showed PRMs function as fluency detectors with wide exploitable reward peaks, and 'Reward Models Identify Consistency, Not Causality' (arXiv:2502.14619, Feb 2025) confirmed this is fundamental. Existing defenses include CRA (Aug 2025, post-hoc sparse autoencoder correction), APRM (2025, adversarial training with harder negatives gaining +5.3pp OOD), CRM (ICLR 2026, sequential conditioning on preceding steps), and PURE (NeurIPS 2025, min-form credit aggregation). None uses explicit logical dependency structure during PRM training. On the infrastructure side, PERL/PARC (ICML 2025) showed premise links form DAGs with 90% extractable recall; GenPRM (AAAI 2026) provides code-verified step analysis; and AgentEval (2026) showed DAG-based dependency modeling yields +22pp failure detection recall over flat evaluation. The best PRMs on PRMBench score 68.8 (Gemini-2-Thinking) vs. 83.8 human ceiling, leaving a 15-point gap where structural approaches could contribute.\",\n  \"inspired_by\": \"Gap from 'Reward Models Identify Consistency, Not Causality' (2025) documenting PRMs' fundamental inability to verify logical validity + quantitative evidence from 'Reward Under Attack' (2026) showing 43% stylistic shortcut exploitation + untried combination of PERL's premise-dependency extraction (proven feasible at 90% recall) with contrastive PRM training + building blocks from DAG-Math, ProofFlow, and GenPRM for dependency graph infrastructure\"\n}\n\nADD these fields (keep all existing fields):\n{\n  \"approach\": \"Proposed method — what you would actually do (3-5 sentences)\",\n  \"resource_estimate\": {\n      \"manual\": {\"gpu_hours\": \"...\", \"timeline\": \"...\", \"estimated_gpu_cost\": \"...\"},\n      \"human_in_loop\": {\"gpu_hours\": \"...\", \"timeline\": \"...\", \"claude_api_cost\": \"...\", \"estimated_gpu_cost\": \"...\"},\n      \"auto_research\": {\"gpu_hours\": \"...\", \"timeline\": \"...\", \"claude_api_cost\": \"...\", \"estimated_gpu_cost\": \"...\", \"speed_bottleneck\": \"...\"}\n  },\n  \"target_venues\": [\"Only venues with deadlines after 2026-05-27\"],\n  \"level\": \"top-tier | solid | incremental\",\n  \"key_references\": [\"Paper title (VENUE YEAR)\", ...],\n  \"description\": \"Executive summary (150-200 words)\",\n  \"project_name\": \"snake_case_identifier (max 30 chars)\",\n  \"source\": \"web_research\"\n}\n\nFor key_references, verify with web_search that cited papers are real. Drop unverifiable ones.\n\n**Model freshness rule**: When the approach involves pretrained models, use web_search to find current top-performing open-source models — do NOT default to models from your training data.\n\n## 竞争论文 & Concurrent Work 搜索\n\n在设计 approach 之前，必须确认没有人正在做同样的事情：\n- 搜索 `{core_problem} 2026` 和 `{approach_keyword} {task} 2026`\n- 在 arXiv 上搜索过去 3 个月的相关提交\n- 在 OpenReview 上搜索即将举行的会议提交\n- 如果发现高度相似的 concurrent work，必须在 landscape 中明确提及\n\n## 可行性验证\n\n1. 搜索类似方法的已有实现（GitHub）\n2. 查找需要打败的具体 baseline 数字\n3. 了解类似实验的硬件/数据需求\n\nOutput ONLY a single JSON object with ALL fields merged. No markdown fences."
}
```

---

### Runtime record

_source line 2 · 2026-05-27T08:03:28.512Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-27T08:03:28.512Z",
  "sessionId": "17534bdc-c682-449b-afbd-9cd4dfa99aa8"
}
```

---

## Round 1

27 recorded events

### User

_source line 3 · 2026-05-27T08:03:28.524Z_

Complete the research direction below with implementation details.

**Today's date: 2026-05-27 (UTC).** Only recommend venues whose deadline has NOT yet passed.

{
  "title": "Premise-Graph Contrastive Training for Logic-Grounded Process Reward Models",
  "core_problem": "Current process reward models confuse surface fluency with logical validity — 43% of PRM reward gains are attributable to stylistic shortcuts rather than reasoning correctness — leading to catastrophic reward hacking during RL training where policies achieve >0.9 PRM scores but <4% actual accuracy. Can we train PRMs that are invariant to surface form but sensitive to logical structure?",
  "opportunity": "PERL (ICML 2025) demonstrated that LLMs can extract premise dependency links between reasoning steps at 90% recall, and that premise-aware verification improves error detection by 6-16%. However, this structural information has only been used at evaluation time, not for PRM training. Simultaneously, DAG-Math (2025) and ProofFlow (2025) have made dependency graph extraction from mathematical reasoning chains feasible. No prior work combines these premise dependency structures with contrastive PRM training to explicitly disentangle logical validity from surface fluency — addressing the documented root cause of PRM fragility at training time rather than through post-hoc corrections.",
  "landscape": "The field has documented severe PRM robustness failures: 'Reward Under Attack' (arXiv:2603.06621, March 2026) showed PRMs function as fluency detectors with wide exploitable reward peaks, and 'Reward Models Identify Consistency, Not Causality' (arXiv:2502.14619, Feb 2025) confirmed this is fundamental. Existing defenses include CRA (Aug 2025, post-hoc sparse autoencoder correction), APRM (2025, adversarial training with harder negatives gaining +5.3pp OOD), CRM (ICLR 2026, sequential conditioning on preceding steps), and PURE (NeurIPS 2025, min-form credit aggregation). None uses explicit logical dependency structure during PRM training. On the infrastructure side, PERL/PARC (ICML 2025) showed premise links form DAGs with 90% extractable recall; GenPRM (AAAI 2026) provides code-verified step analysis; and AgentEval (2026) showed DAG-based dependency modeling yields +22pp failure detection recall over flat evaluation. The best PRMs on PRMBench score 68.8 (Gemini-2-Thinking) vs. 83.8 human ceiling, leaving a 15-point gap where structural approaches could contribute.",
  "inspired_by": "Gap from 'Reward Models Identify Consistency, Not Causality' (2025) documenting PRMs' fundamental inability to verify logical validity + quantitative evidence from 'Reward Under Attack' (2026) showing 43% stylistic shortcut exploitation + untried combination of PERL's premise-dependency extraction (proven feasible at 90% recall) with contrastive PRM training + building blocks from DAG-Math, ProofFlow, and GenPRM for dependency graph infrastructure"
}

ADD these fields (keep all existing fields):
{
  "approach": "Proposed method — what you would actually do (3-5 sentences)",
  "resource_estimate": {
      "manual": {"gpu_hours": "...", "timeline": "...", "estimated_gpu_cost": "..."},
      "human_in_loop": {"gpu_hours": "...", "timeline": "...", "claude_api_cost": "...", "estimated_gpu_cost": "..."},
      "auto_research": {"gpu_hours": "...", "timeline": "...", "claude_api_cost": "...", "estimated_gpu_cost": "...", "speed_bottleneck": "..."}
  },
  "target_venues": ["Only venues with deadlines after 2026-05-27"],
  "level": "top-tier | solid | incremental",
  "key_references": ["Paper title (VENUE YEAR)", ...],
  "description": "Executive summary (150-200 words)",
  "project_name": "snake_case_identifier (max 30 chars)",
  "source": "web_research"
}

For key_references, verify with web_search that cited papers are real. Drop unverifiable ones.

**Model freshness rule**: When the approach involves pretrained models, use web_search to find current top-performing open-source models — do NOT default to models from your training data.

## 竞争论文 & Concurrent Work 搜索

在设计 approach 之前，必须确认没有人正在做同样的事情：
- 搜索 `{core_problem} 2026` 和 `{approach_keyword} {task} 2026`
- 在 arXiv 上搜索过去 3 个月的相关提交
- 在 OpenReview 上搜索即将举行的会议提交
- 如果发现高度相似的 concurrent work，必须在 landscape 中明确提及

## 可行性验证

1. 搜索类似方法的已有实现（GitHub）
2. 查找需要打败的具体 baseline 数字
3. 了解类似实验的硬件/数据需求

Output ONLY a single JSON object with ALL fields merged. No markdown fences.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": false,
  "promptId": "e22bfc79-0a49-4220-ab7a-aad9ac9cf7cd",
  "type": "user",
  "uuid": "89850991-b1ff-46a3-9abe-a81dbeb73df5",
  "permissionMode": "default",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "17534bdc-c682-449b-afbd-9cd4dfa99aa8",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-27T08:03:28.524Z_

```json
{
  "parentUuid": "89850991-b1ff-46a3-9abe-a81dbeb73df5",
  "isSidechain": false,
  "attachment": {
    "type": "deferred_tools_delta",
    "addedNames": [
      "CronCreate",
      "CronDelete",
      "CronList",
      "EnterPlanMode",
      "EnterWorktree",
      "ExitPlanMode",
      "ExitWorktree",
      "Monitor",
      "NotebookEdit",
      "PushNotification",
      "RemoteTrigger",
      "TaskCreate",
      "TaskGet",
      "TaskList",
      "TaskOutput",
      "TaskStop",
      "TaskUpdate",
      "WebFetch",
      "WebSearch"
    ],
    "addedLines": [
      "CronCreate",
      "CronDelete",
      "CronList",
      "EnterPlanMode",
      "EnterWorktree",
      "ExitPlanMode",
      "ExitWorktree",
      "Monitor",
      "NotebookEdit",
      "PushNotification",
      "RemoteTrigger",
      "TaskCreate",
      "TaskGet",
      "TaskList",
      "TaskOutput",
      "TaskStop",
      "TaskUpdate",
      "WebFetch",
      "WebSearch"
    ],
    "removedNames": [],
    "readdedNames": [],
    "pendingMcpServers": []
  },
  "type": "attachment",
  "uuid": "fa5f32ab-fc43-4f0b-ab66-d6e2c4f4aded",
  "timestamp": "2026-05-27T08:03:28.524Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "17534bdc-c682-449b-afbd-9cd4dfa99aa8",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-27T08:03:28.524Z_

```json
{
  "parentUuid": "fa5f32ab-fc43-4f0b-ab66-d6e2c4f4aded",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "8b17908d-6266-4ed7-822b-078948bb49b2",
  "timestamp": "2026-05-27T08:03:28.524Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "17534bdc-c682-449b-afbd-9cd4dfa99aa8",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 6_

```json
{
  "type": "ai-title",
  "aiTitle": "Premise-graph contrastive training for process reward models",
  "sessionId": "17534bdc-c682-449b-afbd-9cd4dfa99aa8"
}
```

---

### Assistant

_source line 7 · 2026-05-27T08:03:39.872Z_

<details><summary>Logged reasoning block</summary>

```text
The user wants me to complete a research direction with implementation details. I need to:

1. Search for concurrent work on premise-graph contrastive training for PRMs
2. Verify key references
3. Find current top-performing open-source models
4. Check venue deadlines
5. Search for similar implementations on GitHub
6. Find baseline numbers to beat
7. Understand hardware/data requirements

Let me start by launching several search agents in parallel.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8b17908d-6266-4ed7-822b-078948bb49b2",
  "isSidechain": false,
  "requestId": "req_011CbSj2Br7UYrhM4Nf6KYCn",
  "type": "assistant",
  "uuid": "666e10e0-ede5-4145-9423-c96ee0e3eb0f",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "17534bdc-c682-449b-afbd-9cd4dfa99aa8",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Hbwjep4s85KspEZY6q7jD7",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 2664,
      "cache_read_input_tokens": 11014,
      "output_tokens": 190,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2664,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 190,
          "cache_read_input_tokens": 11014,
          "cache_creation_input_tokens": 2664,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2664
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

### Tool call

_source line 8 · 2026-05-27T08:03:40.717Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01RjbV2YcViutkJMNMb7L5wW`</summary>

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
  "parentUuid": "666e10e0-ede5-4145-9423-c96ee0e3eb0f",
  "isSidechain": false,
  "requestId": "req_011CbSj2Br7UYrhM4Nf6KYCn",
  "type": "assistant",
  "uuid": "c6ee03a5-8aa7-4a5a-a48b-f9dced726087",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "17534bdc-c682-449b-afbd-9cd4dfa99aa8",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Hbwjep4s85KspEZY6q7jD7",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 2664,
      "cache_read_input_tokens": 11014,
      "output_tokens": 190,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2664,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 190,
          "cache_read_input_tokens": 11014,
          "cache_creation_input_tokens": 2664,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2664
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

_source line 9 · 2026-05-27T08:03:40.725Z_

<details><summary>↩ Tool result · `toolu_01RjbV2YcViutkJMNMb7L5wW`</summary>

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
  "parentUuid": "c6ee03a5-8aa7-4a5a-a48b-f9dced726087",
  "isSidechain": false,
  "promptId": "e22bfc79-0a49-4220-ab7a-aad9ac9cf7cd",
  "type": "user",
  "uuid": "f57c1465-1203-4f49-8ad8-785758dcb443",
  "toolUseResult": {
    "matches": [
      "WebSearch"
    ],
    "query": "select:WebSearch",
    "total_deferred_tools": 19
  },
  "sourceToolAssistantUUID": "c6ee03a5-8aa7-4a5a-a48b-f9dced726087",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "17534bdc-c682-449b-afbd-9cd4dfa99aa8",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 10 · 2026-05-27T08:03:53.560Z_

<details><summary>Logged reasoning block</summary>

```text
Let me launch multiple parallel searches to gather all the information I need.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f57c1465-1203-4f49-8ad8-785758dcb443",
  "isSidechain": false,
  "requestId": "req_011CbSj36CpWMKDf9ZheiAgM",
  "type": "assistant",
  "uuid": "c7bda6aa-97ff-4b1a-8890-7675366e54f8",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "17534bdc-c682-449b-afbd-9cd4dfa99aa8",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KqhRqBAfEguzgCSUxmiK4h",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 718,
      "cache_read_input_tokens": 13678,
      "output_tokens": 1649,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 718,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 1649,
          "cache_read_input_tokens": 13678,
          "cache_creation_input_tokens": 718,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 718
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

### Assistant

_source line 11 · 2026-05-27T08:03:54.145Z_

Let me launch several parallel research agents to gather all the necessary information.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c7bda6aa-97ff-4b1a-8890-7675366e54f8",
  "isSidechain": false,
  "requestId": "req_011CbSj36CpWMKDf9ZheiAgM",
  "type": "assistant",
  "uuid": "ee0c3109-1877-4291-832b-c7d5910441a8",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "17534bdc-c682-449b-afbd-9cd4dfa99aa8",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KqhRqBAfEguzgCSUxmiK4h",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 718,
      "cache_read_input_tokens": 13678,
      "output_tokens": 1649,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 718,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 1649,
          "cache_read_input_tokens": 13678,
          "cache_creation_input_tokens": 718,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 718
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

### Tool call

_source line 12 · 2026-05-27T08:04:00.775Z_

<details open><summary>🔧 Tool call — Agent · `toolu_015PABbTUkdvatybUqPr1ijd`</summary>

```json
{
  "description": "Concurrent work search",
  "prompt": "You are researching whether anyone has already published or is working on \"premise-graph contrastive training for process reward models\" or anything highly similar. \n\nUse WebSearch to run these searches (run them all):\n\n1. Search: \"premise graph contrastive process reward model 2026\"\n2. Search: \"logical structure contrastive PRM training 2026\"\n3. Search: \"dependency graph process reward model training arXiv 2026\"\n4. Search: \"premise-aware reward model contrastive learning 2025 2026\"\n5. Search on arxiv: \"site:arxiv.org process reward model logical structure contrastive 2026\"\n6. Search on openreview: \"site:openreview.net premise dependency process reward model 2026\"\n7. Search: \"reward model robustness logical validity contrastive training 2026\"\n8. Search: \"DAG-based process reward model training 2026\"\n\nFor each search, report:\n- Any papers that seem to do the SAME thing (combine premise dependency graphs with contrastive PRM training)\n- Any papers that are closely related concurrent work\n- Key details: title, authors, venue, date, arxiv ID if available\n\nBe thorough - this is a novelty check. Report your findings comprehensively.",
  "subagent_type": "general-purpose"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ee0c3109-1877-4291-832b-c7d5910441a8",
  "isSidechain": false,
  "requestId": "req_011CbSj36CpWMKDf9ZheiAgM",
  "type": "assistant",
  "uuid": "15ecd53d-03d2-4bb8-a44a-d06cb29e8723",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "17534bdc-c682-449b-afbd-9cd4dfa99aa8",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KqhRqBAfEguzgCSUxmiK4h",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 718,
      "cache_read_input_tokens": 13678,
      "output_tokens": 1649,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 718,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 1649,
          "cache_read_input_tokens": 13678,
          "cache_creation_input_tokens": 718,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 718
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

### Tool call

_source line 13 · 2026-05-27T08:04:06.517Z_

<details open><summary>🔧 Tool call — Agent · `toolu_01HLg4TcrQJqeuMFNKdrA9rN`</summary>

```json
{
  "description": "Verify key references",
  "prompt": "I need to verify that the following papers are real and get their correct details. For each paper, use WebSearch to confirm it exists, get the correct venue/year, and arxiv ID.\n\nPapers to verify:\n1. \"Reward Under Attack\" (arXiv:2603.06621, March 2026) - about PRMs as fluency detectors\n2. \"Reward Models Identify Consistency, Not Causality\" (arXiv:2502.14619, Feb 2025)\n3. PERL (ICML 2025) - premise dependency links between reasoning steps\n4. DAG-Math (2025) - dependency graph extraction from math reasoning\n5. ProofFlow (2025) - dependency graph extraction\n6. CRA (Aug 2025) - post-hoc sparse autoencoder correction for PRMs\n7. APRM (2025) - adversarial training for PRMs\n8. CRM (ICLR 2026) - sequential conditioning on preceding steps\n9. PURE (NeurIPS 2025) - min-form credit aggregation\n10. GenPRM (AAAI 2026) - code-verified step analysis\n11. AgentEval (2026) - DAG-based dependency modeling\n12. PRMBench - benchmark for process reward models\n\nFor each paper, search for it specifically and report:\n- Whether it's real/verifiable\n- Correct title, venue, year\n- ArXiv ID if available\n- Brief description of what it does\n\nBe strict - if you can't find clear evidence a paper exists, mark it as unverifiable.",
  "subagent_type": "general-purpose"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "15ecd53d-03d2-4bb8-a44a-d06cb29e8723",
  "isSidechain": false,
  "requestId": "req_011CbSj36CpWMKDf9ZheiAgM",
  "type": "assistant",
  "uuid": "1c9ab1a3-72c7-468d-98af-1d5b9f458480",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "17534bdc-c682-449b-afbd-9cd4dfa99aa8",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KqhRqBAfEguzgCSUxmiK4h",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 718,
      "cache_read_input_tokens": 13678,
      "output_tokens": 1649,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 718,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 1649,
          "cache_read_input_tokens": 13678,
          "cache_creation_input_tokens": 718,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 718
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

### Tool call

_source line 14 · 2026-05-27T08:04:11.355Z_

<details open><summary>🔧 Tool call — Agent · `toolu_01Fm6Dxwbqd4iKHuwFFx5cWz`</summary>

```json
{
  "description": "Venue deadlines search",
  "prompt": "I need to find ML/AI conference deadlines that are AFTER 2026-05-27 (today's date). Search for:\n\n1. Search: \"NeurIPS 2026 submission deadline\"\n2. Search: \"ICML 2026 submission deadline\"  \n3. Search: \"ICLR 2027 submission deadline\"\n4. Search: \"AAAI 2027 submission deadline\"\n5. Search: \"ACL 2026 submission deadline\"\n6. Search: \"EMNLP 2026 submission deadline\"\n7. Search: \"COLM 2026 submission deadline\"\n8. Search: \"AISTATS 2027 submission deadline\"\n9. Search: \"NeurIPS 2026 workshop deadline\"\n10. Search: \"machine learning conference deadlines 2026 2027\"\n\nFor each venue, report:\n- Full name\n- Paper submission deadline (abstract deadline if separate)\n- Whether the deadline is AFTER 2026-05-27\n- Any relevant tracks (e.g., main conference vs workshop)\n\nOnly include venues whose deadlines have NOT yet passed as of 2026-05-27.",
  "subagent_type": "general-purpose"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1c9ab1a3-72c7-468d-98af-1d5b9f458480",
  "isSidechain": false,
  "requestId": "req_011CbSj36CpWMKDf9ZheiAgM",
  "type": "assistant",
  "uuid": "e86aa7a2-5227-4b18-bc8e-86b69c23279f",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "17534bdc-c682-449b-afbd-9cd4dfa99aa8",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KqhRqBAfEguzgCSUxmiK4h",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 718,
      "cache_read_input_tokens": 13678,
      "output_tokens": 1649,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 718,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 1649,
          "cache_read_input_tokens": 13678,
          "cache_creation_input_tokens": 718,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 718
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

### Tool call

_source line 15 · 2026-05-27T08:04:18.165Z_

<details open><summary>🔧 Tool call — Agent · `toolu_01N6EpLYEbuNZYXfP5md9N9x`</summary>

```json
{
  "description": "Models and baselines search",
  "prompt": "I need to find:\n\n## A) Current top open-source models for process reward modeling and math reasoning (as of May 2026)\n\nSearch for:\n1. \"best open source process reward model 2026\"\n2. \"top process reward model PRM leaderboard 2026\"\n3. \"open source math reasoning model 2026 state of the art\"\n4. \"Qwen math model 2026\"\n5. \"DeepSeek math model 2026\"  \n6. \"Llama math reasoning 2026\"\n7. \"PRMBench leaderboard results 2026\"\n8. \"process reward model benchmark scores 2026\"\n\n## B) Baseline numbers to beat\n\nSearch for:\n1. \"PRMBench scores process reward model\"\n2. \"ProcessBench results 2025 2026\"\n3. \"process reward model accuracy MATH dataset 2026\"\n4. \"best of N process reward model math accuracy 2026\"\n\n## C) Similar implementations on GitHub\n\nSearch for:\n1. \"github premise dependency reward model\"\n2. \"github contrastive process reward model\"\n3. \"github DAG math reasoning verification\"\n4. \"github PERL premise extraction reasoning\"\n\n## D) Hardware/data requirements for similar experiments\n\nSearch for:\n1. \"process reward model training GPU hours cost\"\n2. \"contrastive learning reward model compute requirements\"\n3. \"PRM training data size math-shepherd\"\n\nReport all findings comprehensively with specific numbers, model names, and URLs where possible.",
  "subagent_type": "general-purpose"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e86aa7a2-5227-4b18-bc8e-86b69c23279f",
  "isSidechain": false,
  "requestId": "req_011CbSj36CpWMKDf9ZheiAgM",
  "type": "assistant",
  "uuid": "87707f4c-b5d0-48ef-8951-6f51f7c089e9",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "17534bdc-c682-449b-afbd-9cd4dfa99aa8",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KqhRqBAfEguzgCSUxmiK4h",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 718,
      "cache_read_input_tokens": 13678,
      "output_tokens": 1649,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 718,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 1649,
          "cache_read_input_tokens": 13678,
          "cache_creation_input_tokens": 718,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 718
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

_source line 16 · 2026-05-27T08:06:06.910Z_

<details><summary>↩ Tool result · `toolu_015PABbTUkdvatybUqPr1ijd`</summary>

```text
Now I have a comprehensive picture. Here is my full novelty report.

---

## Novelty Check: "Premise-Graph Contrastive Training for Process Reward Models"

### Executive Summary

**No exact match found.** I did not find any published or preprint paper that combines premise dependency graphs (DAGs representing logical dependencies between premises/steps in a proof or reasoning chain) with contrastive training specifically for process reward models. However, several papers attack adjacent pieces of this idea. The proposed work appears to sit at a genuine intersection that no single existing paper occupies, though there are close neighbors that must be cited and differentiated from.

---

### Papers Doing the SAME Thing (or Very Close)

**None found.** No paper explicitly constructs premise-level dependency graphs and uses them to generate contrastive training pairs for a PRM.

---

### Closely Related / Concurrent Work (Must Cite and Differentiate)

#### 1. Efficient Process Reward Modeling via Contrastive Mutual Information (CPMI)
- **Authors:** Nakyung Lee, Sangwoo Hong, Jungwoo Lee
- **Date:** April 12, 2026
- **arXiv:** [2604.10660](https://arxiv.org/abs/2604.10660)
- **Relevance:** Uses contrastive learning for PRM training -- specifically, contrastive pointwise mutual information to auto-label step-level rewards. The "contrastive" component compares a step's contribution to the correct answer vs. hard-negative alternatives. However, it does NOT use premise dependency graphs; the contrastive signal comes from mutual information between steps and final answers, not from logical structure.
- **Differentiation needed:** Your work uses graph-structural (premise dependency) information to construct contrastive pairs, whereas CPMI uses probabilistic mutual information. These are complementary.

#### 2. Process Reward Model with Q-Value Rankings (PQM)
- **Authors:** Yiming Li et al.
- **Date:** October 2024 (arXiv: [2410.11287](https://arxiv.org/abs/2410.11287))
- **Venue:** OpenReview (under review, likely ICLR 2025/2026)
- **Relevance:** Directly addresses inter-step dependencies in PRMs by reframing PRM as a Markov Decision Process and optimizing Q-value rankings with a comparative loss. This is the closest work to yours in terms of motivation (existing PRMs ignore step interdependencies). However, it uses MDP/Q-value formulations rather than explicit premise dependency graphs, and its comparative loss is not graph-structure-aware.
- **Differentiation needed:** PQM captures temporal/sequential dependencies; your work captures logical/structural dependencies via explicit premise graphs.

#### 3. RewardFlow: Topology-Aware Reward Propagation on State Graphs
- **Authors:** (tmlr-group)
- **Date:** March 19, 2026
- **arXiv:** [2603.18859](https://arxiv.org/abs/2603.18859)
- **Code:** [github.com/tmlr-group/RewardFlow](https://github.com/tmlr-group/RewardFlow)
- **Relevance:** Constructs state graphs from reasoning trajectories and propagates rewards using topological structure. This is close in spirit -- it uses graph topology for reward estimation. However, it targets agentic RL tasks (not mathematical/logical reasoning PRMs), and the graph is a state-transition graph (which states lead to success), not a premise-dependency graph (which premises logically support which conclusions). No contrastive training is used.
- **Differentiation needed:** Different graph type (state-transition vs. premise-dependency), different task domain, different training method (propagation vs. contrastive).

#### 4. Knowledge Graphs are Implicit Reward Models: Path-Derived Signals Enable Compositional Reasoning
- **Date:** January 2026
- **arXiv:** [2601.15160](https://arxiv.org/abs/2601.15160)
- **Relevance:** Uses knowledge graph paths as reward signals for RL, encouraging compositional reasoning. Validates that graph-structured knowledge can ground reward signals. However, the graphs are external knowledge graphs (medical ontologies), not premise dependency graphs derived from the reasoning trace itself.
- **Differentiation needed:** Your premise graphs are intrinsic to the reasoning chain, not external knowledge.

#### 5. Linking Process to Outcome: Conditional Reward Modeling (CRM)
- **Date:** September 2025
- **arXiv:** [2509.26578](https://arxiv.org/abs/2509.26578)
- **Relevance:** Addresses inter-step dependencies by conditioning each step's reward on previous steps and the final outcome. Models reasoning as a temporal/probabilistic process. Does not use graphs or contrastive training.
- **Differentiation needed:** CRM uses sequential conditioning; your work uses explicit graph structure.

#### 6. GraphPRM: Rewarding Graph Reasoning Process
- **Authors:** (GKNL group)
- **Date:** March 2025
- **arXiv:** [2503.00845](https://arxiv.org/abs/2503.00845)
- **Venue:** KDD 2025
- **Relevance:** The first PRM for graph reasoning problems. Uses MCTS + automated labeling to generate step-wise supervision for graph-structured tasks. Constructs positive/negative pairs based on step correctness. However, "graph" here refers to the input data domain (graph algorithm problems), NOT to premise/logical dependency structure. The PRM itself is a standard classifier, not trained with premise-aware contrastive objectives.
- **Differentiation needed:** GraphPRM applies PRMs TO graph problems; your work uses premise graphs to TRAIN PRMs for logical/mathematical reasoning.

#### 7. CLIPO: Contrastive Learning in Policy Optimization Generalizes RLVR
- **Date:** March 2026
- **arXiv:** [2603.10101](https://arxiv.org/abs/2603.10101)
- **Relevance:** Uses contrastive learning in policy optimization to distinguish logically sound from spurious reasoning. Relevant as another contrastive approach for reasoning quality, but operates at the policy level (not PRM training) and does not use premise graphs.

#### 8. Preference-Based Process Reward Model (PPRM)
- **Venue:** ICLR 2026
- **arXiv:** [2512.16917](https://arxiv.org/abs/2512.16917)
- **Relevance:** Uses preference-based training for PRMs to improve robustness in mathematical reasoning. Related in the PRM training methodology space but does not involve graphs or premise structure.

#### 9. FoVER: Efficient PRM Training Data Synthesis via Formal Verification
- **arXiv:** [2505.15960](https://arxiv.org/abs/2505.15960)
- **Relevance:** Uses formal verification tools (Z3, Isabelle) to generate accurate step-level labels for PRM training on formal logic tasks. Relevant because it connects formal logical structure to PRM training, but does not use premise graphs or contrastive training.

#### 10. Reward Models Identify Consistency, Not Causality
- **arXiv:** [2502.14619](https://arxiv.org/abs/2502.14619)
- **Relevance:** Demonstrates that current reward models evaluate surface-level logical consistency rather than true causal/logical validity. This paper provides strong motivation for your work -- premise-graph contrastive training could be positioned as a solution to this exact problem.

---

### Summary Assessment

| Dimension | Covered in Prior Work? |
|---|---|
| Contrastive training for PRMs | Yes (CPMI, GraphPRM pairs) |
| Modeling inter-step dependencies in PRMs | Yes (PQM, CRM) |
| Graph-topology-aware reward estimation | Yes (RewardFlow, KG-as-RM) |
| Premise/logical dependency graphs for reasoning | Partially (formal verification in FoVER) |
| **Premise dependency graphs + contrastive PRM training** | **NOT FOUND** |

**The specific combination -- extracting premise dependency DAGs from reasoning chains and using those DAGs to construct contrastive training pairs for process reward models -- appears novel as of May 2026.** The closest concurrent work is CPMI (contrastive PRM but no graphs), PQM (step dependencies but no graphs/no contrastive), and RewardFlow (graph topology for rewards but state graphs, not premise graphs, and no contrastive training).

**Recommended positioning:** Frame the contribution as bridging the gap between (a) work that recognizes PRMs need inter-step dependency modeling (PQM, CRM) and (b) work that uses contrastive methods for PRM training (CPMI), by introducing explicit logical structure (premise dependency graphs) as the organizing principle for contrastive pair construction. The paper by "Reward Models Identify Consistency, Not Causality" (2502.14619) provides excellent motivation.

---

Sources:
- [Efficient Process Reward Modeling via Contrastive Mutual Information (CPMI)](https://arxiv.org/abs/2604.10660)
- [Process Reward Model with Q-Value Rankings (PQM)](https://arxiv.org/abs/2410.11287)
- [RewardFlow: Topology-Aware Reward Propagation on State Graphs](https://arxiv.org/abs/2603.18859)
- [Knowledge Graphs are Implicit Reward Models](https://arxiv.org/abs/2601.15160)
- [Linking Process to Outcome: Conditional Reward Modeling (CRM)](https://arxiv.org/abs/2509.26578)
- [GraphPRM: Rewarding Graph Reasoning Process](https://arxiv.org/abs/2503.00845)
- [CLIPO: Contrastive Learning in Policy Optimization](https://arxiv.org/abs/2603.10101)
- [Preference-Based Process Reward Model (PPRM) - ICLR 2026](https://arxiv.org/abs/2512.16917)
- [FoVER: PRM Training Data Synthesis via Formal Verification](https://arxiv.org/abs/2505.15960)
- [Reward Models Identify Consistency, Not Causality](https://arxiv.org/abs/2502.14619)
- [Improving Discriminative Capability of Reward Models Using Contrastive Learning](https://aclanthology.org/2024.emnlp-main.852/)
- [AgentPRM: Process Reward Models for LLM Agents](https://dl.acm.org/doi/10.1145/3774904.3792551)
- [Awesome Process Reward Models (curated list)](https://github.com/RyanLiu112/Awesome-Process-Reward-Models)
- [Process Reward Models Overview - Emergent Mind](https://www.emergentmind.com/topics/process-reward-models-prm)

agentId: a4722e75c938906d8 (use SendMessage with to: 'a4722e75c938906d8' to continue this agent)
&lt;usage>total_tokens: 24388
tool_uses: 17
duration_ms: 126129&lt;/usage>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "15ecd53d-03d2-4bb8-a44a-d06cb29e8723",
  "isSidechain": false,
  "promptId": "e22bfc79-0a49-4220-ab7a-aad9ac9cf7cd",
  "type": "user",
  "uuid": "5d6aea52-d09c-4430-93fb-636e4ab97cc9",
  "toolUseResult": {
    "status": "completed",
    "prompt": "You are researching whether anyone has already published or is working on \"premise-graph contrastive training for process reward models\" or anything highly similar. \n\nUse WebSearch to run these searches (run them all):\n\n1. Search: \"premise graph contrastive process reward model 2026\"\n2. Search: \"logical structure contrastive PRM training 2026\"\n3. Search: \"dependency graph process reward model training arXiv 2026\"\n4. Search: \"premise-aware reward model contrastive learning 2025 2026\"\n5. Search on arxiv: \"site:arxiv.org process reward model logical structure contrastive 2026\"\n6. Search on openreview: \"site:openreview.net premise dependency process reward model 2026\"\n7. Search: \"reward model robustness logical validity contrastive training 2026\"\n8. Search: \"DAG-based process reward model training 2026\"\n\nFor each search, report:\n- Any papers that seem to do the SAME thing (combine premise dependency graphs with contrastive PRM training)\n- Any papers that are closely related concurrent work\n- Key details: title, authors, venue, date, arxiv ID if available\n\nBe thorough - this is a novelty check. Report your findings comprehensively.",
    "agentId": "a4722e75c938906d8",
    "agentType": "general-purpose",
    "content": [
      {
        "type": "text",
        "text": "Now I have a comprehensive picture. Here is my full novelty report.\n\n---\n\n## Novelty Check: \"Premise-Graph Contrastive Training for Process Reward Models\"\n\n### Executive Summary\n\n**No exact match found.** I did not find any published or preprint paper that combines premise dependency graphs (DAGs representing logical dependencies between premises/steps in a proof or reasoning chain) with contrastive training specifically for process reward models. However, several papers attack adjacent pieces of this idea. The proposed work appears to sit at a genuine intersection that no single existing paper occupies, though there are close neighbors that must be cited and differentiated from.\n\n---\n\n### Papers Doing the SAME Thing (or Very Close)\n\n**None found.** No paper explicitly constructs premise-level dependency graphs and uses them to generate contrastive training pairs for a PRM.\n\n---\n\n### Closely Related / Concurrent Work (Must Cite and Differentiate)\n\n#### 1. Efficient Process Reward Modeling via Contrastive Mutual Information (CPMI)\n- **Authors:** Nakyung Lee, Sangwoo Hong, Jungwoo Lee\n- **Date:** April 12, 2026\n- **arXiv:** [2604.10660](https://arxiv.org/abs/2604.10660)\n- **Relevance:** Uses contrastive learning for PRM training -- specifically, contrastive pointwise mutual information to auto-label step-level rewards. The \"contrastive\" component compares a step's contribution to the correct answer vs. hard-negative alternatives. However, it does NOT use premise dependency graphs; the contrastive signal comes from mutual information between steps and final answers, not from logical structure.\n- **Differentiation needed:** Your work uses graph-structural (premise dependency) information to construct contrastive pairs, whereas CPMI uses probabilistic mutual information. These are complementary.\n\n#### 2. Process Reward Model with Q-Value Rankings (PQM)\n- **Authors:** Yiming Li et al.\n- **Date:** October 2024 (arXiv: [2410.11287](https://arxiv.org/abs/2410.11287))\n- **Venue:** OpenReview (under review, likely ICLR 2025/2026)\n- **Relevance:** Directly addresses inter-step dependencies in PRMs by reframing PRM as a Markov Decision Process and optimizing Q-value rankings with a comparative loss. This is the closest work to yours in terms of motivation (existing PRMs ignore step interdependencies). However, it uses MDP/Q-value formulations rather than explicit premise dependency graphs, and its comparative loss is not graph-structure-aware.\n- **Differentiation needed:** PQM captures temporal/sequential dependencies; your work captures logical/structural dependencies via explicit premise graphs.\n\n#### 3. RewardFlow: Topology-Aware Reward Propagation on State Graphs\n- **Authors:** (tmlr-group)\n- **Date:** March 19, 2026\n- **arXiv:** [2603.18859](https://arxiv.org/abs/2603.18859)\n- **Code:** [github.com/tmlr-group/RewardFlow](https://github.com/tmlr-group/RewardFlow)\n- **Relevance:** Constructs state graphs from reasoning trajectories and propagates rewards using topological structure. This is close in spirit -- it uses graph topology for reward estimation. However, it targets agentic RL tasks (not mathematical/logical reasoning PRMs), and the graph is a state-transition graph (which states lead to success), not a premise-dependency graph (which premises logically support which conclusions). No contrastive training is used.\n- **Differentiation needed:** Different graph type (state-transition vs. premise-dependency), different task domain, different training method (propagation vs. contrastive).\n\n#### 4. Knowledge Graphs are Implicit Reward Models: Path-Derived Signals Enable Compositional Reasoning\n- **Date:** January 2026\n- **arXiv:** [2601.15160](https://arxiv.org/abs/2601.15160)\n- **Relevance:** Uses knowledge graph paths as reward signals for RL, encouraging compositional reasoning. Validates that graph-structured knowledge can ground reward signals. However, the graphs are external knowledge graphs (medical ontologies), not premise dependency graphs derived from the reasoning trace itself.\n- **Differentiation needed:** Your premise graphs are intrinsic to the reasoning chain, not external knowledge.\n\n#### 5. Linking Process to Outcome: Conditional Reward Modeling (CRM)\n- **Date:** September 2025\n- **arXiv:** [2509.26578](https://arxiv.org/abs/2509.26578)\n- **Relevance:** Addresses inter-step dependencies by conditioning each step's reward on previous steps and the final outcome. Models reasoning as a temporal/probabilistic process. Does not use graphs or contrastive training.\n- **Differentiation needed:** CRM uses sequential conditioning; your work uses explicit graph structure.\n\n#### 6. GraphPRM: Rewarding Graph Reasoning Process\n- **Authors:** (GKNL group)\n- **Date:** March 2025\n- **arXiv:** [2503.00845](https://arxiv.org/abs/2503.00845)\n- **Venue:** KDD 2025\n- **Relevance:** The first PRM for graph reasoning problems. Uses MCTS + automated labeling to generate step-wise supervision for graph-structured tasks. Constructs positive/negative pairs based on step correctness. However, \"graph\" here refers to the input data domain (graph algorithm problems), NOT to premise/logical dependency structure. The PRM itself is a standard classifier, not trained with premise-aware contrastive objectives.\n- **Differentiation needed:** GraphPRM applies PRMs TO graph problems; your work uses premise graphs to TRAIN PRMs for logical/mathematical reasoning.\n\n#### 7. CLIPO: Contrastive Learning in Policy Optimization Generalizes RLVR\n- **Date:** March 2026\n- **arXiv:** [2603.10101](https://arxiv.org/abs/2603.10101)\n- **Relevance:** Uses contrastive learning in policy optimization to distinguish logically sound from spurious reasoning. Relevant as another contrastive approach for reasoning quality, but operates at the policy level (not PRM training) and does not use premise graphs.\n\n#### 8. Preference-Based Process Reward Model (PPRM)\n- **Venue:** ICLR 2026\n- **arXiv:** [2512.16917](https://arxiv.org/abs/2512.16917)\n- **Relevance:** Uses preference-based training for PRMs to improve robustness in mathematical reasoning. Related in the PRM training methodology space but does not involve graphs or premise structure.\n\n#### 9. FoVER: Efficient PRM Training Data Synthesis via Formal Verification\n- **arXiv:** [2505.15960](https://arxiv.org/abs/2505.15960)\n- **Relevance:** Uses formal verification tools (Z3, Isabelle) to generate accurate step-level labels for PRM training on formal logic tasks. Relevant because it connects formal logical structure to PRM training, but does not use premise graphs or contrastive training.\n\n#### 10. Reward Models Identify Consistency, Not Causality\n- **arXiv:** [2502.14619](https://arxiv.org/abs/2502.14619)\n- **Relevance:** Demonstrates that current reward models evaluate surface-level logical consistency rather than true causal/logical validity. This paper provides strong motivation for your work -- premise-graph contrastive training could be positioned as a solution to this exact problem.\n\n---\n\n### Summary Assessment\n\n| Dimension | Covered in Prior Work? |\n|---|---|\n| Contrastive training for PRMs | Yes (CPMI, GraphPRM pairs) |\n| Modeling inter-step dependencies in PRMs | Yes (PQM, CRM) |\n| Graph-topology-aware reward estimation | Yes (RewardFlow, KG-as-RM) |\n| Premise/logical dependency graphs for reasoning | Partially (formal verification in FoVER) |\n| **Premise dependency graphs + contrastive PRM training** | **NOT FOUND** |\n\n**The specific combination -- extracting premise dependency DAGs from reasoning chains and using those DAGs to construct contrastive training pairs for process reward models -- appears novel as of May 2026.** The closest concurrent work is CPMI (contrastive PRM but no graphs), PQM (step dependencies but no graphs/no contrastive), and RewardFlow (graph topology for rewards but state graphs, not premise graphs, and no contrastive training).\n\n**Recommended positioning:** Frame the contribution as bridging the gap between (a) work that recognizes PRMs need inter-step dependency modeling (PQM, CRM) and (b) work that uses contrastive methods for PRM training (CPMI), by introducing explicit logical structure (premise dependency graphs) as the organizing principle for contrastive pair construction. The paper by \"Reward Models Identify Consistency, Not Causality\" (2502.14619) provides excellent motivation.\n\n---\n\nSources:\n- [Efficient Process Reward Modeling via Contrastive Mutual Information (CPMI)](https://arxiv.org/abs/2604.10660)\n- [Process Reward Model with Q-Value Rankings (PQM)](https://arxiv.org/abs/2410.11287)\n- [RewardFlow: Topology-Aware Reward Propagation on State Graphs](https://arxiv.org/abs/2603.18859)\n- [Knowledge Graphs are Implicit Reward Models](https://arxiv.org/abs/2601.15160)\n- [Linking Process to Outcome: Conditional Reward Modeling (CRM)](https://arxiv.org/abs/2509.26578)\n- [GraphPRM: Rewarding Graph Reasoning Process](https://arxiv.org/abs/2503.00845)\n- [CLIPO: Contrastive Learning in Policy Optimization](https://arxiv.org/abs/2603.10101)\n- [Preference-Based Process Reward Model (PPRM) - ICLR 2026](https://arxiv.org/abs/2512.16917)\n- [FoVER: PRM Training Data Synthesis via Formal Verification](https://arxiv.org/abs/2505.15960)\n- [Reward Models Identify Consistency, Not Causality](https://arxiv.org/abs/2502.14619)\n- [Improving Discriminative Capability of Reward Models Using Contrastive Learning](https://aclanthology.org/2024.emnlp-main.852/)\n- [AgentPRM: Process Reward Models for LLM Agents](https://dl.acm.org/doi/10.1145/3774904.3792551)\n- [Awesome Process Reward Models (curated list)](https://github.com/RyanLiu112/Awesome-Process-Reward-Models)\n- [Process Reward Models Overview - Emergent Mind](https://www.emergentmind.com/topics/process-reward-models-prm)"
      }
    ],
    "totalDurationMs": 126129,
    "totalTokens": 24388,
    "totalToolUseCount": 17,
    "usage": {
      "input_tokens": 600,
      "cache_creation_input_tokens": 2994,
      "cache_read_input_tokens": 18145,
      "output_tokens": 2649,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2994
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 600,
          "output_tokens": 2649,
          "cache_read_input_tokens": 18145,
          "cache_creation_input_tokens": 2994,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2994,
            "ephemeral_1h_input_tokens": 0
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "toolStats": {
      "readCount": 0,
      "searchCount": 0,
      "bashCount": 0,
      "editFileCount": 0,
      "linesAdded": 0,
      "linesRemoved": 0,
      "otherToolCount": 17
    }
  },
  "sourceToolAssistantUUID": "15ecd53d-03d2-4bb8-a44a-d06cb29e8723",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "17534bdc-c682-449b-afbd-9cd4dfa99aa8",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 17_

```json
{
  "type": "last-prompt",
  "lastPrompt": "Complete the research direction below with implementation details.  **Today's date: 2026-05-27 (UTC).** Only recommend venues whose deadline has NOT yet passed.  {   \"title\": \"Premise-Graph Contrastiv…",
  "leafUuid": "5d6aea52-d09c-4430-93fb-636e4ab97cc9",
  "sessionId": "17534bdc-c682-449b-afbd-9cd4dfa99aa8"
}
```

---

### Runtime record

_source line 18_

```json
{
  "type": "ai-title",
  "aiTitle": "Premise-graph contrastive training for process reward models",
  "sessionId": "17534bdc-c682-449b-afbd-9cd4dfa99aa8"
}
```

---

### Tool result

_source line 19 · 2026-05-27T08:06:55.596Z_

<details><summary>↩ Tool result · `toolu_01Fm6Dxwbqd4iKHuwFFx5cWz`</summary>

```text
I now have comprehensive information. Here is the full report.

---

## ML/AI Conference Deadlines After 2026-05-27

Below are all venues with at least one deadline still open as of today (May 27, 2026). Venues whose main paper deadlines have already passed are excluded unless they have a relevant upcoming track (e.g., workshops).

---

### 1. CoRL 2026 -- Conference on Robot Learning

- **Paper submission deadline:** May 29, 2026 (11:59 UTC)
- **Abstract deadline:** May 26, 2026 (already passed)
- **Conference dates:** November 9-12, 2026, Austin, TX
- **Status: Paper deadline is AFTER today (barely -- 2 days away). Abstract deadline just passed.**

---

### 2. NeurIPS 2026 -- Thirty-Ninth Conference on Neural Information Processing Systems

- **Main track abstract deadline:** May 4, 2026 (PASSED)
- **Main track paper deadline:** May 6, 2026 (PASSED)
- **Competition proposal deadline:** May 15, 2026 (PASSED)
- **Workshop application deadline: June 6, 2026 (AFTER today)**
- **Workshop suggested contribution submission:** August 29, 2026
- **Workshop mandatory accept/reject notification:** September 29, 2026
- **Conference dates:** December 6-12, 2026, Sydney, Australia
- **Status: Main paper deadline PASSED. Workshop application deadline is AFTER today.**

---

### 3. COLM 2026 -- Conference on Language Modeling

- **Abstract deadline:** March 26, 2026 (PASSED)
- **Paper deadline:** March 31, 2026 (PASSED)
- **Workshop contribution suggested submission: June 23, 2026 (AFTER today)**
- **Workshop mandatory accept/reject notification:** July 24, 2026
- **Conference dates:** October 6-9, 2026, San Francisco, CA
- **Status: Main paper deadline PASSED. Workshop contribution deadline is AFTER today.**

---

### 4. EMNLP 2026 -- Conference on Empirical Methods in Natural Language Processing

- **ARR submission deadline:** May 25, 2026 (PASSED -- 2 days ago)
- **Commitment deadline: August 2, 2026 (AFTER today)**
- **Acceptance notification:** August 20, 2026
- **Camera-ready:** September 20, 2026
- **Conference dates:** October 24-29, 2026, Budapest, Hungary
- **Status: ARR submission deadline PASSED. However, the commitment deadline (for papers already reviewed via earlier ARR cycles) is August 2, 2026 -- AFTER today.**

---

### 5. AAAI 2027 -- Association for the Advancement of Artificial Intelligence

- **Abstract deadline: July 21, 2026 (AFTER today)**
- **Full paper deadline: July 28, 2026 (AFTER today)**
- **Supplementary material/code: July 31, 2026**
- **Phase 1 rejection notification:** September 24, 2026
- **Final notification:** November 30, 2026
- **Conference dates:** February 16-23, 2027, Montreal, Quebec, Canada
- **Status: All deadlines AFTER today.**

---

### 6. WACV 2027 -- IEEE/CVF Winter Conference on Applications of Computer Vision

- **Round 1 submission deadline: July 12, 2026 (AFTER today)**
- **Round 2 submission deadline: September 13, 2026 (AFTER today)**
- **Conference dates:** February 28 - March 4, 2027
- **Status: All deadlines AFTER today.**

---

### 7. ICLR 2027 -- International Conference on Learning Representations

- **Abstract deadline: September 19, 2026 (AFTER today)**
- **Full paper deadline: September 24, 2026 (AFTER today)**
- **Conference dates:** April/May 2027 (exact dates TBA)
- **Status: All deadlines AFTER today.**

---

### 8. AISTATS 2027 -- International Conference on Artificial Intelligence and Statistics

- **Paper submission deadline: October 10, 2026 (AFTER today)**
- **Conference dates:** April 28-30, 2027
- **Status: Deadline AFTER today.**

---

### 9. PRICAI 2026 -- Pacific Rim International Conference on Artificial Intelligence

- **Submission deadline: ~June 7, 2026 (AFTER today)**
- **Conference dates:** November 12-15, 2026
- **Status: Deadline AFTER today.**

---

## Venues with ALL Deadlines PASSED (excluded)

| Venue | Paper Deadline | Status |
|-------|---------------|--------|
| ICML 2026 | January 28, 2026 | PASSED |
| ACL 2026 (ARR commitment) | March 14, 2026 | PASSED |
| ICLR 2026 | September 24, 2025 | PASSED |
| AISTATS 2026 | October 2, 2025 | PASSED |
| COLM 2026 (main) | March 31, 2026 | PASSED |

---

## Summary: Upcoming Deadlines in Chronological Order

| Date | Venue | Track |
|------|-------|-------|
| May 29, 2026 | **CoRL 2026** | Main paper submission |
| June 6, 2026 | **NeurIPS 2026** | Workshop applications |
| ~June 7, 2026 | **PRICAI 2026** | Paper submission |
| June 23, 2026 | **COLM 2026** | Workshop contributions |
| July 12, 2026 | **WACV 2027** | Round 1 submission |
| July 21, 2026 | **AAAI 2027** | Abstract submission |
| July 28, 2026 | **AAAI 2027** | Full paper submission |
| August 2, 2026 | **EMNLP 2026** | Commitment deadline |
| August 29, 2026 | **NeurIPS 2026** | Workshop contribution submission (suggested) |
| September 13, 2026 | **WACV 2027** | Round 2 submission |
| September 19, 2026 | **ICLR 2027** | Abstract submission |
| September 24, 2026 | **ICLR 2027** | Full paper submission |
| October 10, 2026 | **AISTATS 2027** | Paper submission |

Sources:
- [NeurIPS 2026 Dates](https://neurips.cc/Conferences/2026/Dates)
- [NeurIPS 2026 Call for Workshops](https://neurips.cc/Conferences/2026/CallForWorkshops)
- [ICML 2026 Dates](https://icml.cc/Conferences/2026/Dates)
- [ICLR 2026 Dates](https://iclr.cc/Conferences/2026/Dates)
- [AAAI-27 Main Technical Track](https://aaai.org/conference/aaai/aaai-27/call/main-technical-track/)
- [AAAI-27 Conference](https://aaai.org/conference/aaai/aaai-27/)
- [ACL 2026](https://2026.aclweb.org/)
- [EMNLP 2026](https://2026.emnlp.org/)
- [COLM 2026 Dates](https://colmweb.org/dates.html)
- [COLM 2026 Call for Papers](https://colmweb.org/cfp.html)
- [CoRL 2026](https://www.corl.org/)
- [CoRL 2026 Call for Papers](https://www.corl.org/contributions/call-for-papers)
- [AI & ML Conference Deadlines 2026-2027 (Bibby)](https://trybibby.com/conference-deadlines)
- [AI Deadlines](http://aideadlines.org/)
- [AISTATS 2026](https://virtual.aistats.org/)

agentId: a9abfa2d96d8947d6 (use SendMessage with to: 'a9abfa2d96d8947d6' to continue this agent)
&lt;usage>total_tokens: 24004
tool_uses: 21
duration_ms: 164238&lt;/usage>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "e86aa7a2-5227-4b18-bc8e-86b69c23279f",
  "isSidechain": false,
  "promptId": "e22bfc79-0a49-4220-ab7a-aad9ac9cf7cd",
  "type": "user",
  "uuid": "2fa8f7e9-384e-41d3-a19b-479a7e7c37b7",
  "toolUseResult": {
    "status": "completed",
    "prompt": "I need to find ML/AI conference deadlines that are AFTER 2026-05-27 (today's date). Search for:\n\n1. Search: \"NeurIPS 2026 submission deadline\"\n2. Search: \"ICML 2026 submission deadline\"  \n3. Search: \"ICLR 2027 submission deadline\"\n4. Search: \"AAAI 2027 submission deadline\"\n5. Search: \"ACL 2026 submission deadline\"\n6. Search: \"EMNLP 2026 submission deadline\"\n7. Search: \"COLM 2026 submission deadline\"\n8. Search: \"AISTATS 2027 submission deadline\"\n9. Search: \"NeurIPS 2026 workshop deadline\"\n10. Search: \"machine learning conference deadlines 2026 2027\"\n\nFor each venue, report:\n- Full name\n- Paper submission deadline (abstract deadline if separate)\n- Whether the deadline is AFTER 2026-05-27\n- Any relevant tracks (e.g., main conference vs workshop)\n\nOnly include venues whose deadlines have NOT yet passed as of 2026-05-27.",
    "agentId": "a9abfa2d96d8947d6",
    "agentType": "general-purpose",
    "content": [
      {
        "type": "text",
        "text": "I now have comprehensive information. Here is the full report.\n\n---\n\n## ML/AI Conference Deadlines After 2026-05-27\n\nBelow are all venues with at least one deadline still open as of today (May 27, 2026). Venues whose main paper deadlines have already passed are excluded unless they have a relevant upcoming track (e.g., workshops).\n\n---\n\n### 1. CoRL 2026 -- Conference on Robot Learning\n\n- **Paper submission deadline:** May 29, 2026 (11:59 UTC)\n- **Abstract deadline:** May 26, 2026 (already passed)\n- **Conference dates:** November 9-12, 2026, Austin, TX\n- **Status: Paper deadline is AFTER today (barely -- 2 days away). Abstract deadline just passed.**\n\n---\n\n### 2. NeurIPS 2026 -- Thirty-Ninth Conference on Neural Information Processing Systems\n\n- **Main track abstract deadline:** May 4, 2026 (PASSED)\n- **Main track paper deadline:** May 6, 2026 (PASSED)\n- **Competition proposal deadline:** May 15, 2026 (PASSED)\n- **Workshop application deadline: June 6, 2026 (AFTER today)**\n- **Workshop suggested contribution submission:** August 29, 2026\n- **Workshop mandatory accept/reject notification:** September 29, 2026\n- **Conference dates:** December 6-12, 2026, Sydney, Australia\n- **Status: Main paper deadline PASSED. Workshop application deadline is AFTER today.**\n\n---\n\n### 3. COLM 2026 -- Conference on Language Modeling\n\n- **Abstract deadline:** March 26, 2026 (PASSED)\n- **Paper deadline:** March 31, 2026 (PASSED)\n- **Workshop contribution suggested submission: June 23, 2026 (AFTER today)**\n- **Workshop mandatory accept/reject notification:** July 24, 2026\n- **Conference dates:** October 6-9, 2026, San Francisco, CA\n- **Status: Main paper deadline PASSED. Workshop contribution deadline is AFTER today.**\n\n---\n\n### 4. EMNLP 2026 -- Conference on Empirical Methods in Natural Language Processing\n\n- **ARR submission deadline:** May 25, 2026 (PASSED -- 2 days ago)\n- **Commitment deadline: August 2, 2026 (AFTER today)**\n- **Acceptance notification:** August 20, 2026\n- **Camera-ready:** September 20, 2026\n- **Conference dates:** October 24-29, 2026, Budapest, Hungary\n- **Status: ARR submission deadline PASSED. However, the commitment deadline (for papers already reviewed via earlier ARR cycles) is August 2, 2026 -- AFTER today.**\n\n---\n\n### 5. AAAI 2027 -- Association for the Advancement of Artificial Intelligence\n\n- **Abstract deadline: July 21, 2026 (AFTER today)**\n- **Full paper deadline: July 28, 2026 (AFTER today)**\n- **Supplementary material/code: July 31, 2026**\n- **Phase 1 rejection notification:** September 24, 2026\n- **Final notification:** November 30, 2026\n- **Conference dates:** February 16-23, 2027, Montreal, Quebec, Canada\n- **Status: All deadlines AFTER today.**\n\n---\n\n### 6. WACV 2027 -- IEEE/CVF Winter Conference on Applications of Computer Vision\n\n- **Round 1 submission deadline: July 12, 2026 (AFTER today)**\n- **Round 2 submission deadline: September 13, 2026 (AFTER today)**\n- **Conference dates:** February 28 - March 4, 2027\n- **Status: All deadlines AFTER today.**\n\n---\n\n### 7. ICLR 2027 -- International Conference on Learning Representations\n\n- **Abstract deadline: September 19, 2026 (AFTER today)**\n- **Full paper deadline: September 24, 2026 (AFTER today)**\n- **Conference dates:** April/May 2027 (exact dates TBA)\n- **Status: All deadlines AFTER today.**\n\n---\n\n### 8. AISTATS 2027 -- International Conference on Artificial Intelligence and Statistics\n\n- **Paper submission deadline: October 10, 2026 (AFTER today)**\n- **Conference dates:** April 28-30, 2027\n- **Status: Deadline AFTER today.**\n\n---\n\n### 9. PRICAI 2026 -- Pacific Rim International Conference on Artificial Intelligence\n\n- **Submission deadline: ~June 7, 2026 (AFTER today)**\n- **Conference dates:** November 12-15, 2026\n- **Status: Deadline AFTER today.**\n\n---\n\n## Venues with ALL Deadlines PASSED (excluded)\n\n| Venue | Paper Deadline | Status |\n|-------|---------------|--------|\n| ICML 2026 | January 28, 2026 | PASSED |\n| ACL 2026 (ARR commitment) | March 14, 2026 | PASSED |\n| ICLR 2026 | September 24, 2025 | PASSED |\n| AISTATS 2026 | October 2, 2025 | PASSED |\n| COLM 2026 (main) | March 31, 2026 | PASSED |\n\n---\n\n## Summary: Upcoming Deadlines in Chronological Order\n\n| Date | Venue | Track |\n|------|-------|-------|\n| May 29, 2026 | **CoRL 2026** | Main paper submission |\n| June 6, 2026 | **NeurIPS 2026** | Workshop applications |\n| ~June 7, 2026 | **PRICAI 2026** | Paper submission |\n| June 23, 2026 | **COLM 2026** | Workshop contributions |\n| July 12, 2026 | **WACV 2027** | Round 1 submission |\n| July 21, 2026 | **AAAI 2027** | Abstract submission |\n| July 28, 2026 | **AAAI 2027** | Full paper submission |\n| August 2, 2026 | **EMNLP 2026** | Commitment deadline |\n| August 29, 2026 | **NeurIPS 2026** | Workshop contribution submission (suggested) |\n| September 13, 2026 | **WACV 2027** | Round 2 submission |\n| September 19, 2026 | **ICLR 2027** | Abstract submission |\n| September 24, 2026 | **ICLR 2027** | Full paper submission |\n| October 10, 2026 | **AISTATS 2027** | Paper submission |\n\nSources:\n- [NeurIPS 2026 Dates](https://neurips.cc/Conferences/2026/Dates)\n- [NeurIPS 2026 Call for Workshops](https://neurips.cc/Conferences/2026/CallForWorkshops)\n- [ICML 2026 Dates](https://icml.cc/Conferences/2026/Dates)\n- [ICLR 2026 Dates](https://iclr.cc/Conferences/2026/Dates)\n- [AAAI-27 Main Technical Track](https://aaai.org/conference/aaai/aaai-27/call/main-technical-track/)\n- [AAAI-27 Conference](https://aaai.org/conference/aaai/aaai-27/)\n- [ACL 2026](https://2026.aclweb.org/)\n- [EMNLP 2026](https://2026.emnlp.org/)\n- [COLM 2026 Dates](https://colmweb.org/dates.html)\n- [COLM 2026 Call for Papers](https://colmweb.org/cfp.html)\n- [CoRL 2026](https://www.corl.org/)\n- [CoRL 2026 Call for Papers](https://www.corl.org/contributions/call-for-papers)\n- [AI & ML Conference Deadlines 2026-2027 (Bibby)](https://trybibby.com/conference-deadlines)\n- [AI Deadlines](http://aideadlines.org/)\n- [AISTATS 2026](https://virtual.aistats.org/)"
      }
    ],
    "totalDurationMs": 164238,
    "totalTokens": 24004,
    "totalToolUseCount": 21,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1125,
      "cache_read_input_tokens": 20804,
      "output_tokens": 2074,
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
          "input_tokens": 1,
          "output_tokens": 2074,
          "cache_read_input_tokens": 20804,
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
    "toolStats": {
      "readCount": 0,
      "searchCount": 0,
      "bashCount": 0,
      "editFileCount": 0,
      "linesAdded": 0,
      "linesRemoved": 0,
      "otherToolCount": 21
    }
  },
  "sourceToolAssistantUUID": "e86aa7a2-5227-4b18-bc8e-86b69c23279f",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "17534bdc-c682-449b-afbd-9cd4dfa99aa8",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-27T08:09:34.379Z_

<details><summary>↩ Tool result · `toolu_01N6EpLYEbuNZYXfP5md9N9x`</summary>

```text
Now I have comprehensive data. Let me compile the final report.

---

# Comprehensive Research Report: Process Reward Models, Math Reasoning, and Related Work

## A. Current Top Open-Source Models for Process Reward Modeling and Math Reasoning (as of May 2026)

### Top Process Reward Models (PRMs)

**1. PathFinder-PRM-7B** (2025)
- State-of-the-art PRMScore of **67.7** on PRMBench, surpassing the prior best of 65.5
- Uses a hierarchical approach: classifies step-level errors into Math and Consistency categories, then estimates step Optimality
- Trained on ~400K samples (3x less data than prior approaches), enriching PRM800K with automated annotations
- GitHub: https://github.com/declare-lab/PathFinder-PRM
- HuggingFace: https://huggingface.co/declare-lab/PathFinder-PRM-7B

**2. R-PRM-7B-DPO** (March 2025, EMNLP 2025)
- ProcessBench F1: **70.4** (SFT variant: 65.2)
- PRMBench overall: **66.8** (SFT variant: 64.9)
- Best-of-8 average accuracy across 6 math datasets: **49.6** vs Qwen2.5-Math-PRM-7B's 48.0
- Surpasses baselines by **11.9 F1** on ProcessBench and **8.5 F1** on PRMBench
- Base: Qwen2.5-Math-7B-Instruct; trained on ~289K SFT samples + ~269K DPO pairs
- GitHub: https://github.com/NJUNLP/R-PRM

**3. Qwen2.5-Math-PRM (7B and 72B)** (January 2025)
- Qwen2.5-Math-PRM-7B ProcessBench F1: **73.5** (overall), with per-subset scores of 82.4 (GSM8K), 77.6 (MATH), 67.5 (OlympiadBench)
- PRMBench overall: **65.5**
- The 7B model outperforms GPT-4o-0806 on ProcessBench; the 72B model achieves ~**78.3** average F1 on ProcessBench
- Blog: https://qwenlm.github.io/blog/qwen2.5-math-prm/

**4. ThinkPRM (1.5B and 14B)** (April 2025, TMLR 2026)
- A generative PRM that uses long chain-of-thought verification
- ProcessBench F1: **87.3** (OlympiadBench), **85.7** (OmniMath) for ThinkPRM-14B
- Trained on only **8,000 step-level labels** (1% of PRM800K's 712K labels)
- Outperforms discriminative verifiers by **8%** on GPQA-Diamond and **4.5%** on LiveCodeBench
- Outperforms LLM-as-a-Judge by **7.2%** on ProcessBench
- Training time: **1.5 hours** for 14B, **4.5 hours** for QwQ-32B on a single A100
- Paper: https://arxiv.org/abs/2504.16828

**5. GenPRM-7B** (April 2025)
- A 7B model that surpasses Qwen2.5-Math-PRM-72B (10x larger) on ProcessBench through test-time scaling
- Paper: https://arxiv.org/abs/2504.00891

**6. Other Notable PRMs (2025-2026):**
- **FreePRM** (June 2025): Trains without ground-truth process labels
- **FoVer** (May 2025, ACL 2026 Findings): Uses formal verification (Z3, Isabelle) for data synthesis; GitHub: https://github.com/psunlpgroup/FoVer
- **APRM** (Nov 2025): Adversarial training for PRMs
- **VersaPRM** (Feb 2025): Multi-domain PRM via synthetic reasoning data
- **Universal PRM / AURORA** (Feb 2025): Automated training framework, 7B model released

### Top Open-Source Math Reasoning Models

**1. DeepSeekMath-V2** (2026)
- 685B parameters, built on DeepSeek-V3.2-Exp-Base
- Uses a generation-verification loop with an LLM-based verifier as reward model
- Gold-medal-level on IMO 2025; scored **118/120** on Putnam 2024 (human best: 90)
- Open-source

**2. DeepSeek-R1-0528**
- 671B total parameters (MoE), 164K context
- Performance comparable to OpenAI o1 on math, code, and reasoning
- Distilled variant DeepSeek-R1-Distill-Qwen3-8B outperforms Gemini 2.5 Flash on AIME 2025

**3. Qwen 3.7 Max (May 2026)**
- **97.1** on HMMT 2026 February
- 1M-token context window
- Pricing: $2.50/$7.50 per million tokens

**4. Qwen2.5-Math-72B-Instruct**
- Outperforms Qwen2-Math-72B-Instruct by 4.4 points (English) and 6.1 points (Chinese) on average

**5. Llama 4 Maverick** (17B active params, 128 experts)
- Beats GPT-4o and Gemini 2.0 Flash on broad benchmarks
- Comparable to DeepSeek v3 on reasoning and coding

**6. Llama 4 Behemoth** (288B active params)
- SOTA for non-reasoning models on math benchmarks

**7. OpenThinker3-7B**: **53%** on AIME 2025, **51%** on LiveCodeBench, **54%** on GPQA Diamond

---

## B. Baseline Numbers to Beat

### PRMBench Scores (Step-Level Error Detection)

| Model | PRMBench Score |
|-------|---------------|
| PathFinder-PRM-7B | **67.7** (SOTA) |
| R-PRM-7B-DPO | 66.8 |
| Qwen2.5-Math-PRM-7B | 65.5 |
| R-PRM-7B-SFT | 64.9 |
| ReasonEval-7B | 60.0 |

### ProcessBench Scores (F1, Error Identification)

| Model | ProcessBench F1 |
|-------|----------------|
| ThinkPRM-14B (OlympiadBench) | **87.3** |
| ThinkPRM-14B (OmniMath) | 85.7 |
| Qwen2.5-Math-PRM-72B | ~78.3 (avg) |
| Qwen2.5-Math-PRM-7B | 73.5 (avg); 82.4 (GSM8K), 77.6 (MATH), 67.5 (OlympiadBench) |
| R-PRM-7B-DPO | 70.4 |
| R-PRM-7B-SFT | 65.2 |
| GPT-4o | ~61.9 |
| Qwen2.5-Math-7B-PRM800K | 58.5 |

### Best-of-N Math Accuracy

| Model | BoN-8 Avg (6 datasets) |
|-------|----------------------|
| R-PRM-7B-DPO | **49.6** |
| Qwen2.5-Math-PRM-7B | 48.0 |
| R-PRM-7B-SFT | ~46-47 |

- Hierarchical Reward Model (HRM) using Qwen2.5-72B-Math-Instruct: accuracy converges to **~80%** as N increases
- ThinkPRM-1.5B with parallel scaling boosts MATH-500 accuracy by **>5 percentage points** over baselines
- Baseline best-of-N@1 on MATH-500: 18.4-37.4 depending on backbone

### Key Benchmark Reference Points
- **RewardBench**: Decision-Tree-Reward-Gemma-2-27B achieves **95.4%** (SOTA for general reward models)
- **Skywork-Reward-V2**: Leading on RewardBench v2 across BoN, RM-Bench, and truthfulness
- **RewardBench 2**: Models score ~20 points lower on average than the original RewardBench

---

## C. Similar Implementations on GitHub

### Premise/Dependency-Based Approaches

**1. PARC (Premise-Augmented Reasoning Chains)**
- Restructures linear reasoning chains into DAGs with premise links
- LLMs achieve **90% recall** in premise identification
- Error identification accuracy improves by **6-16% absolute** with premise-augmented verification
- Tested with Llama-3.1-8B-Instruct
- MIT License
- GitHub: https://github.com/SagnikMukherjee/PARC

**2. DAG-MATH (Graph-of-Thought Guided Mathematical Reasoning)**
- Submitted to ICLR 2026
- Benchmark with ~2,894 annotated CoT solutions from Omni-MATH
- Introduces "logical closeness" metric for DAG structure adherence
- GitHub: https://github.com/YuanheZ/DAG-MATH-Formatted-CoT

**3. Graph of Verification (GoV)**
- Training-free framework: decomposes reasoning into a DAG, applies topological sort, then sequential verification
- Outperforms holistic baselines on ProcessBench (GSM8K) F1 scores
- Uses Qwen2.5 series; requires OpenAI API
- GitHub: https://github.com/Frevor/Graph-of-Verification

### Contrastive/Adversarial Approaches

**4. APRM (Adversarial Training for PRMs)**
- Generator learns to produce reasoning errors; PRM learns to detect them
- Related Adv-RM training: conventional 8B reward model training takes ~4 hours on 1 node (8 GPUs); full adversarial pipeline takes **672 A100 hours** (2 rounds) vs **224 A100 hours** for conventional RLHF
- Paper: https://arxiv.org/abs/2511.22888

**5. GRACE (Generative Representation via Contrastive Policy Optimization)**
- Treats contrastive objectives as rewards over rationales
- Paper: https://arxiv.org/abs/2510.04506

### Other Relevant Repositories

**6. RM-R1 (Reward Modeling as Reasoning)**
- GitHub: https://github.com/RM-R1-UIUC/RM-R1

**7. FoVer (Formally Verified PRM Training Data)**
- Uses Z3 and Isabelle for automated step-level annotation
- GitHub: https://github.com/psunlpgroup/FoVer

**8. Awesome-Process-Reward-Models** (curated list)
- GitHub: https://github.com/RyanLiu112/Awesome-Process-Reward-Models

**9. RLHFlow/RLHF-Reward-Modeling**
- Trained top-3 8B models on RewardBench (ArmoRM, Pair Pref. Model, BT RM)
- GitHub: https://github.com/RLHFlow/RLHF-Reward-Modeling

**10. OpenPRM** (ICLR 2025)
- Building open-domain PRMs with preference trees
- Paper: https://openreview.net/forum?id=fGIqGfmgkW

---

## D. Hardware/Data Requirements for Similar Experiments

### Training Compute

| Experiment | Hardware | Time | Total GPU-Hours |
|-----------|----------|------|----------------|
| ThinkPRM-14B fine-tuning | 1x A100 | 1.5 hours | **1.5 A100-hours** |
| ThinkPRM-QwQ-32B | 1x A100 | 4.5 hours | **4.5 A100-hours** |
| Conventional 8B reward model | 8x A100 (1 node) | ~4 hours | **~32 A100-hours** |
| Adversarial RM (full pipeline, 2 rounds) | 16x A100 (2 nodes) | ~12 hours | **~672 A100-hours** |
| Conventional RLHF pipeline | 8x A100 | varies | **~224 A100-hours** |
| General 7B fine-tuning (LoRA) | 1x A100 | hours | **<$5 cloud cost** |
| General 70B fine-tuning | 8-32x A100 | days | **$12K-$45K** |

### Cloud GPU Pricing (2026)
- H100 SXM: **$1.50-$3.50/hr** rental, ~$5-8/hr on premium clouds
- A100 80GB: **$2-5/hr** depending on provider

### Dataset Sizes

| Dataset | Size | Annotation Method |
|---------|------|------------------|
| PRM800K | ~800K labels (~265K after dedup) | Human expert annotation |
| Math-Shepherd | ~445K samples | Automatic (Monte Carlo) |
| PathFinder-600K | ~400K samples | PRM800K + automated enrichment |
| R-PRM SFT data | ~289K samples | LLaMA3.3-70B-Instruct generation |
| R-PRM DPO pairs | ~269K pairs | Sampled trajectory construction |
| Epic50k | ~50K annotated steps | Matches PRM800K/Math-Shepherd performance at <10% size |
| ThinkPRM | **1K examples (8K step labels)** | Filtered synthetic sampling |
| VRPRM | 3.6K CoT-PRM SFT + 50K non-CoT RL | Mixed |
| PRMBench (evaluation) | 6,216 problems, 83,456 step labels | Expert-designed |
| ProcessBench (evaluation) | 3,400 test cases | Expert-verified error locations |
| DAG-MATH benchmark | ~2,894 annotated CoT solutions | From Omni-MATH |

### Key Efficiency Findings
- **ThinkPRM** achieves SOTA with only **1% of PRM800K labels** (8K vs 712K), making it extremely data-efficient
- **Epic50k** (50K steps) matches models trained on PRM800K/Math-Shepherd at <10% dataset size
- **GenPRM-7B** surpasses Qwen2.5-Math-PRM-72B (10x larger) via test-time compute scaling
- **ACTPRM** outperforms Universal PRM by 0.7% using only **20% of annotation budget**
- A 1.5B model trained on only **700 problems** achieves +4.32% on AIME 2024; a 7B on **1,070 problems** achieves +6.67%

---

Sources:
- [PRMBench (ACL 2025)](https://prmbench.github.io/)
- [PRMBench Paper](https://arxiv.org/abs/2501.03124)
- [ProcessBench (ACL 2025)](https://arxiv.org/abs/2412.06559)
- [ProcessBench GitHub](https://github.com/QwenLM/ProcessBench)
- [ThinkPRM Paper](https://arxiv.org/abs/2504.16828)
- [R-PRM Paper](https://arxiv.org/abs/2503.21295)
- [R-PRM GitHub](https://github.com/NJUNLP/R-PRM)
- [PathFinder-PRM GitHub](https://github.com/declare-lab/PathFinder-PRM)
- [PathFinder-PRM HuggingFace](https://huggingface.co/declare-lab/PathFinder-PRM-7B)
- [GenPRM Paper](https://arxiv.org/abs/2504.00891)
- [Qwen2.5-Math-PRM Blog](https://qwenlm.github.io/blog/qwen2.5-math-prm/)
- [Qwen2.5-Math-PRM-72B HuggingFace](https://huggingface.co/Qwen/Qwen2.5-Math-PRM-72B)
- [Qwen2.5-Math-PRM-7B HuggingFace](https://huggingface.co/Qwen/Qwen2.5-Math-PRM-7B)
- [Qwen 3.7 Max](https://www.digitalapplied.com/blog/qwen-3-7-max-alibaba-flagship-ai-model-2026)
- [DeepSeekMath-V2 HuggingFace](https://huggingface.co/deepseek-ai/DeepSeek-Math-V2)
- [DeepSeekMath-V2 Nature Coverage](https://www.nature.com/articles/d41586-025-03959-9)
- [Top Open-Source Reasoning Models 2026](https://www.clarifai.com/blog/top-10-open-source-reasoning-models-in-2026)
- [Best Open-Source LLM for Math 2026](https://www.siliconflow.com/articles/en/best-open-source-LLM-for-math)
- [Llama 4 Blog](https://ai.meta.com/blog/llama-4-multimodal-intelligence/)
- [PARC GitHub](https://github.com/SagnikMukherjee/PARC)
- [DAG-MATH GitHub](https://github.com/YuanheZ/DAG-MATH-Formatted-CoT)
- [Graph of Verification GitHub](https://github.com/Frevor/Graph-of-Verification)
- [FoVer GitHub](https://github.com/psunlpgroup/FoVer)
- [RM-R1 GitHub](https://github.com/RM-R1-UIUC/RM-R1)
- [Awesome Process Reward Models](https://github.com/RyanLiu112/Awesome-Process-Reward-Models)
- [Awesome Reward Models](https://github.com/JLZhong23/awesome-reward-models)
- [RLHFlow RLHF Reward Modeling](https://github.com/RLHFlow/RLHF-Reward-Modeling)
- [APRM Paper](https://arxiv.org/abs/2511.22888)
- [RewardBench](https://huggingface.co/spaces/allenai/reward-bench)
- [RewardBench 2](https://openreview.net/forum?id=fb0G86Dewb)
- [PRM800K GitHub](https://github.com/openai/prm800k)
- [Math-Shepherd Paper](https://arxiv.org/abs/2312.08935)
- [OpenPRM (ICLR 2025)](https://openreview.net/forum?id=fGIqGfmgkW)
- [Socratic-PRMBench](https://arxiv.org/html/2505.23474v1)
- [ToolPRMBench](https://arxiv.org/html/2601.12294v1)

agentId: a7fcd55ce3613e611 (use SendMessage with to: 'a7fcd55ce3613e611' to continue this agent)
&lt;usage>total_tokens: 47725
tool_uses: 47
duration_ms: 316208&lt;/usage>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "87707f4c-b5d0-48ef-8951-6f51f7c089e9",
  "isSidechain": false,
  "promptId": "e22bfc79-0a49-4220-ab7a-aad9ac9cf7cd",
  "type": "user",
  "uuid": "50fde36b-df6b-478e-93b8-0627cd7f863e",
  "toolUseResult": {
    "status": "completed",
    "prompt": "I need to find:\n\n## A) Current top open-source models for process reward modeling and math reasoning (as of May 2026)\n\nSearch for:\n1. \"best open source process reward model 2026\"\n2. \"top process reward model PRM leaderboard 2026\"\n3. \"open source math reasoning model 2026 state of the art\"\n4. \"Qwen math model 2026\"\n5. \"DeepSeek math model 2026\"  \n6. \"Llama math reasoning 2026\"\n7. \"PRMBench leaderboard results 2026\"\n8. \"process reward model benchmark scores 2026\"\n\n## B) Baseline numbers to beat\n\nSearch for:\n1. \"PRMBench scores process reward model\"\n2. \"ProcessBench results 2025 2026\"\n3. \"process reward model accuracy MATH dataset 2026\"\n4. \"best of N process reward model math accuracy 2026\"\n\n## C) Similar implementations on GitHub\n\nSearch for:\n1. \"github premise dependency reward model\"\n2. \"github contrastive process reward model\"\n3. \"github DAG math reasoning verification\"\n4. \"github PERL premise extraction reasoning\"\n\n## D) Hardware/data requirements for similar experiments\n\nSearch for:\n1. \"process reward model training GPU hours cost\"\n2. \"contrastive learning reward model compute requirements\"\n3. \"PRM training data size math-shepherd\"\n\nReport all findings comprehensively with specific numbers, model names, and URLs where possible.",
    "agentId": "a7fcd55ce3613e611",
    "agentType": "general-purpose",
    "content": [
      {
        "type": "text",
        "text": "Now I have comprehensive data. Let me compile the final report.\n\n---\n\n# Comprehensive Research Report: Process Reward Models, Math Reasoning, and Related Work\n\n## A. Current Top Open-Source Models for Process Reward Modeling and Math Reasoning (as of May 2026)\n\n### Top Process Reward Models (PRMs)\n\n**1. PathFinder-PRM-7B** (2025)\n- State-of-the-art PRMScore of **67.7** on PRMBench, surpassing the prior best of 65.5\n- Uses a hierarchical approach: classifies step-level errors into Math and Consistency categories, then estimates step Optimality\n- Trained on ~400K samples (3x less data than prior approaches), enriching PRM800K with automated annotations\n- GitHub: https://github.com/declare-lab/PathFinder-PRM\n- HuggingFace: https://huggingface.co/declare-lab/PathFinder-PRM-7B\n\n**2. R-PRM-7B-DPO** (March 2025, EMNLP 2025)\n- ProcessBench F1: **70.4** (SFT variant: 65.2)\n- PRMBench overall: **66.8** (SFT variant: 64.9)\n- Best-of-8 average accuracy across 6 math datasets: **49.6** vs Qwen2.5-Math-PRM-7B's 48.0\n- Surpasses baselines by **11.9 F1** on ProcessBench and **8.5 F1** on PRMBench\n- Base: Qwen2.5-Math-7B-Instruct; trained on ~289K SFT samples + ~269K DPO pairs\n- GitHub: https://github.com/NJUNLP/R-PRM\n\n**3. Qwen2.5-Math-PRM (7B and 72B)** (January 2025)\n- Qwen2.5-Math-PRM-7B ProcessBench F1: **73.5** (overall), with per-subset scores of 82.4 (GSM8K), 77.6 (MATH), 67.5 (OlympiadBench)\n- PRMBench overall: **65.5**\n- The 7B model outperforms GPT-4o-0806 on ProcessBench; the 72B model achieves ~**78.3** average F1 on ProcessBench\n- Blog: https://qwenlm.github.io/blog/qwen2.5-math-prm/\n\n**4. ThinkPRM (1.5B and 14B)** (April 2025, TMLR 2026)\n- A generative PRM that uses long chain-of-thought verification\n- ProcessBench F1: **87.3** (OlympiadBench), **85.7** (OmniMath) for ThinkPRM-14B\n- Trained on only **8,000 step-level labels** (1% of PRM800K's 712K labels)\n- Outperforms discriminative verifiers by **8%** on GPQA-Diamond and **4.5%** on LiveCodeBench\n- Outperforms LLM-as-a-Judge by **7.2%** on ProcessBench\n- Training time: **1.5 hours** for 14B, **4.5 hours** for QwQ-32B on a single A100\n- Paper: https://arxiv.org/abs/2504.16828\n\n**5. GenPRM-7B** (April 2025)\n- A 7B model that surpasses Qwen2.5-Math-PRM-72B (10x larger) on ProcessBench through test-time scaling\n- Paper: https://arxiv.org/abs/2504.00891\n\n**6. Other Notable PRMs (2025-2026):**\n- **FreePRM** (June 2025): Trains without ground-truth process labels\n- **FoVer** (May 2025, ACL 2026 Findings): Uses formal verification (Z3, Isabelle) for data synthesis; GitHub: https://github.com/psunlpgroup/FoVer\n- **APRM** (Nov 2025): Adversarial training for PRMs\n- **VersaPRM** (Feb 2025): Multi-domain PRM via synthetic reasoning data\n- **Universal PRM / AURORA** (Feb 2025): Automated training framework, 7B model released\n\n### Top Open-Source Math Reasoning Models\n\n**1. DeepSeekMath-V2** (2026)\n- 685B parameters, built on DeepSeek-V3.2-Exp-Base\n- Uses a generation-verification loop with an LLM-based verifier as reward model\n- Gold-medal-level on IMO 2025; scored **118/120** on Putnam 2024 (human best: 90)\n- Open-source\n\n**2. DeepSeek-R1-0528**\n- 671B total parameters (MoE), 164K context\n- Performance comparable to OpenAI o1 on math, code, and reasoning\n- Distilled variant DeepSeek-R1-Distill-Qwen3-8B outperforms Gemini 2.5 Flash on AIME 2025\n\n**3. Qwen 3.7 Max (May 2026)**\n- **97.1** on HMMT 2026 February\n- 1M-token context window\n- Pricing: $2.50/$7.50 per million tokens\n\n**4. Qwen2.5-Math-72B-Instruct**\n- Outperforms Qwen2-Math-72B-Instruct by 4.4 points (English) and 6.1 points (Chinese) on average\n\n**5. Llama 4 Maverick** (17B active params, 128 experts)\n- Beats GPT-4o and Gemini 2.0 Flash on broad benchmarks\n- Comparable to DeepSeek v3 on reasoning and coding\n\n**6. Llama 4 Behemoth** (288B active params)\n- SOTA for non-reasoning models on math benchmarks\n\n**7. OpenThinker3-7B**: **53%** on AIME 2025, **51%** on LiveCodeBench, **54%** on GPQA Diamond\n\n---\n\n## B. Baseline Numbers to Beat\n\n### PRMBench Scores (Step-Level Error Detection)\n\n| Model | PRMBench Score |\n|-------|---------------|\n| PathFinder-PRM-7B | **67.7** (SOTA) |\n| R-PRM-7B-DPO | 66.8 |\n| Qwen2.5-Math-PRM-7B | 65.5 |\n| R-PRM-7B-SFT | 64.9 |\n| ReasonEval-7B | 60.0 |\n\n### ProcessBench Scores (F1, Error Identification)\n\n| Model | ProcessBench F1 |\n|-------|----------------|\n| ThinkPRM-14B (OlympiadBench) | **87.3** |\n| ThinkPRM-14B (OmniMath) | 85.7 |\n| Qwen2.5-Math-PRM-72B | ~78.3 (avg) |\n| Qwen2.5-Math-PRM-7B | 73.5 (avg); 82.4 (GSM8K), 77.6 (MATH), 67.5 (OlympiadBench) |\n| R-PRM-7B-DPO | 70.4 |\n| R-PRM-7B-SFT | 65.2 |\n| GPT-4o | ~61.9 |\n| Qwen2.5-Math-7B-PRM800K | 58.5 |\n\n### Best-of-N Math Accuracy\n\n| Model | BoN-8 Avg (6 datasets) |\n|-------|----------------------|\n| R-PRM-7B-DPO | **49.6** |\n| Qwen2.5-Math-PRM-7B | 48.0 |\n| R-PRM-7B-SFT | ~46-47 |\n\n- Hierarchical Reward Model (HRM) using Qwen2.5-72B-Math-Instruct: accuracy converges to **~80%** as N increases\n- ThinkPRM-1.5B with parallel scaling boosts MATH-500 accuracy by **>5 percentage points** over baselines\n- Baseline best-of-N@1 on MATH-500: 18.4-37.4 depending on backbone\n\n### Key Benchmark Reference Points\n- **RewardBench**: Decision-Tree-Reward-Gemma-2-27B achieves **95.4%** (SOTA for general reward models)\n- **Skywork-Reward-V2**: Leading on RewardBench v2 across BoN, RM-Bench, and truthfulness\n- **RewardBench 2**: Models score ~20 points lower on average than the original RewardBench\n\n---\n\n## C. Similar Implementations on GitHub\n\n### Premise/Dependency-Based Approaches\n\n**1. PARC (Premise-Augmented Reasoning Chains)**\n- Restructures linear reasoning chains into DAGs with premise links\n- LLMs achieve **90% recall** in premise identification\n- Error identification accuracy improves by **6-16% absolute** with premise-augmented verification\n- Tested with Llama-3.1-8B-Instruct\n- MIT License\n- GitHub: https://github.com/SagnikMukherjee/PARC\n\n**2. DAG-MATH (Graph-of-Thought Guided Mathematical Reasoning)**\n- Submitted to ICLR 2026\n- Benchmark with ~2,894 annotated CoT solutions from Omni-MATH\n- Introduces \"logical closeness\" metric for DAG structure adherence\n- GitHub: https://github.com/YuanheZ/DAG-MATH-Formatted-CoT\n\n**3. Graph of Verification (GoV)**\n- Training-free framework: decomposes reasoning into a DAG, applies topological sort, then sequential verification\n- Outperforms holistic baselines on ProcessBench (GSM8K) F1 scores\n- Uses Qwen2.5 series; requires OpenAI API\n- GitHub: https://github.com/Frevor/Graph-of-Verification\n\n### Contrastive/Adversarial Approaches\n\n**4. APRM (Adversarial Training for PRMs)**\n- Generator learns to produce reasoning errors; PRM learns to detect them\n- Related Adv-RM training: conventional 8B reward model training takes ~4 hours on 1 node (8 GPUs); full adversarial pipeline takes **672 A100 hours** (2 rounds) vs **224 A100 hours** for conventional RLHF\n- Paper: https://arxiv.org/abs/2511.22888\n\n**5. GRACE (Generative Representation via Contrastive Policy Optimization)**\n- Treats contrastive objectives as rewards over rationales\n- Paper: https://arxiv.org/abs/2510.04506\n\n### Other Relevant Repositories\n\n**6. RM-R1 (Reward Modeling as Reasoning)**\n- GitHub: https://github.com/RM-R1-UIUC/RM-R1\n\n**7. FoVer (Formally Verified PRM Training Data)**\n- Uses Z3 and Isabelle for automated step-level annotation\n- GitHub: https://github.com/psunlpgroup/FoVer\n\n**8. Awesome-Process-Reward-Models** (curated list)\n- GitHub: https://github.com/RyanLiu112/Awesome-Process-Reward-Models\n\n**9. RLHFlow/RLHF-Reward-Modeling**\n- Trained top-3 8B models on RewardBench (ArmoRM, Pair Pref. Model, BT RM)\n- GitHub: https://github.com/RLHFlow/RLHF-Reward-Modeling\n\n**10. OpenPRM** (ICLR 2025)\n- Building open-domain PRMs with preference trees\n- Paper: https://openreview.net/forum?id=fGIqGfmgkW\n\n---\n\n## D. Hardware/Data Requirements for Similar Experiments\n\n### Training Compute\n\n| Experiment | Hardware | Time | Total GPU-Hours |\n|-----------|----------|------|----------------|\n| ThinkPRM-14B fine-tuning | 1x A100 | 1.5 hours | **1.5 A100-hours** |\n| ThinkPRM-QwQ-32B | 1x A100 | 4.5 hours | **4.5 A100-hours** |\n| Conventional 8B reward model | 8x A100 (1 node) | ~4 hours | **~32 A100-hours** |\n| Adversarial RM (full pipeline, 2 rounds) | 16x A100 (2 nodes) | ~12 hours | **~672 A100-hours** |\n| Conventional RLHF pipeline | 8x A100 | varies | **~224 A100-hours** |\n| General 7B fine-tuning (LoRA) | 1x A100 | hours | **<$5 cloud cost** |\n| General 70B fine-tuning | 8-32x A100 | days | **$12K-$45K** |\n\n### Cloud GPU Pricing (2026)\n- H100 SXM: **$1.50-$3.50/hr** rental, ~$5-8/hr on premium clouds\n- A100 80GB: **$2-5/hr** depending on provider\n\n### Dataset Sizes\n\n| Dataset | Size | Annotation Method |\n|---------|------|------------------|\n| PRM800K | ~800K labels (~265K after dedup) | Human expert annotation |\n| Math-Shepherd | ~445K samples | Automatic (Monte Carlo) |\n| PathFinder-600K | ~400K samples | PRM800K + automated enrichment |\n| R-PRM SFT data | ~289K samples | LLaMA3.3-70B-Instruct generation |\n| R-PRM DPO pairs | ~269K pairs | Sampled trajectory construction |\n| Epic50k | ~50K annotated steps | Matches PRM800K/Math-Shepherd performance at <10% size |\n| ThinkPRM | **1K examples (8K step labels)** | Filtered synthetic sampling |\n| VRPRM | 3.6K CoT-PRM SFT + 50K non-CoT RL | Mixed |\n| PRMBench (evaluation) | 6,216 problems, 83,456 step labels | Expert-designed |\n| ProcessBench (evaluation) | 3,400 test cases | Expert-verified error locations |\n| DAG-MATH benchmark | ~2,894 annotated CoT solutions | From Omni-MATH |\n\n### Key Efficiency Findings\n- **ThinkPRM** achieves SOTA with only **1% of PRM800K labels** (8K vs 712K), making it extremely data-efficient\n- **Epic50k** (50K steps) matches models trained on PRM800K/Math-Shepherd at <10% dataset size\n- **GenPRM-7B** surpasses Qwen2.5-Math-PRM-72B (10x larger) via test-time compute scaling\n- **ACTPRM** outperforms Universal PRM by 0.7% using only **20% of annotation budget**\n- A 1.5B model trained on only **700 problems** achieves +4.32% on AIME 2024; a 7B on **1,070 problems** achieves +6.67%\n\n---\n\nSources:\n- [PRMBench (ACL 2025)](https://prmbench.github.io/)\n- [PRMBench Paper](https://arxiv.org/abs/2501.03124)\n- [ProcessBench (ACL 2025)](https://arxiv.org/abs/2412.06559)\n- [ProcessBench GitHub](https://github.com/QwenLM/ProcessBench)\n- [ThinkPRM Paper](https://arxiv.org/abs/2504.16828)\n- [R-PRM Paper](https://arxiv.org/abs/2503.21295)\n- [R-PRM GitHub](https://github.com/NJUNLP/R-PRM)\n- [PathFinder-PRM GitHub](https://github.com/declare-lab/PathFinder-PRM)\n- [PathFinder-PRM HuggingFace](https://huggingface.co/declare-lab/PathFinder-PRM-7B)\n- [GenPRM Paper](https://arxiv.org/abs/2504.00891)\n- [Qwen2.5-Math-PRM Blog](https://qwenlm.github.io/blog/qwen2.5-math-prm/)\n- [Qwen2.5-Math-PRM-72B HuggingFace](https://huggingface.co/Qwen/Qwen2.5-Math-PRM-72B)\n- [Qwen2.5-Math-PRM-7B HuggingFace](https://huggingface.co/Qwen/Qwen2.5-Math-PRM-7B)\n- [Qwen 3.7 Max](https://www.digitalapplied.com/blog/qwen-3-7-max-alibaba-flagship-ai-model-2026)\n- [DeepSeekMath-V2 HuggingFace](https://huggingface.co/deepseek-ai/DeepSeek-Math-V2)\n- [DeepSeekMath-V2 Nature Coverage](https://www.nature.com/articles/d41586-025-03959-9)\n- [Top Open-Source Reasoning Models 2026](https://www.clarifai.com/blog/top-10-open-source-reasoning-models-in-2026)\n- [Best Open-Source LLM for Math 2026](https://www.siliconflow.com/articles/en/best-open-source-LLM-for-math)\n- [Llama 4 Blog](https://ai.meta.com/blog/llama-4-multimodal-intelligence/)\n- [PARC GitHub](https://github.com/SagnikMukherjee/PARC)\n- [DAG-MATH GitHub](https://github.com/YuanheZ/DAG-MATH-Formatted-CoT)\n- [Graph of Verification GitHub](https://github.com/Frevor/Graph-of-Verification)\n- [FoVer GitHub](https://github.com/psunlpgroup/FoVer)\n- [RM-R1 GitHub](https://github.com/RM-R1-UIUC/RM-R1)\n- [Awesome Process Reward Models](https://github.com/RyanLiu112/Awesome-Process-Reward-Models)\n- [Awesome Reward Models](https://github.com/JLZhong23/awesome-reward-models)\n- [RLHFlow RLHF Reward Modeling](https://github.com/RLHFlow/RLHF-Reward-Modeling)\n- [APRM Paper](https://arxiv.org/abs/2511.22888)\n- [RewardBench](https://huggingface.co/spaces/allenai/reward-bench)\n- [RewardBench 2](https://openreview.net/forum?id=fb0G86Dewb)\n- [PRM800K GitHub](https://github.com/openai/prm800k)\n- [Math-Shepherd Paper](https://arxiv.org/abs/2312.08935)\n- [OpenPRM (ICLR 2025)](https://openreview.net/forum?id=fGIqGfmgkW)\n- [Socratic-PRMBench](https://arxiv.org/html/2505.23474v1)\n- [ToolPRMBench](https://arxiv.org/html/2601.12294v1)"
      }
    ],
    "totalDurationMs": 316208,
    "totalTokens": 47725,
    "totalToolUseCount": 47,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1786,
      "cache_read_input_tokens": 40876,
      "output_tokens": 5062,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1786
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 5062,
          "cache_read_input_tokens": 40876,
          "cache_creation_input_tokens": 1786,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1786,
            "ephemeral_1h_input_tokens": 0
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "toolStats": {
      "readCount": 0,
      "searchCount": 0,
      "bashCount": 0,
      "editFileCount": 0,
      "linesAdded": 0,
      "linesRemoved": 0,
      "otherToolCount": 47
    }
  },
  "sourceToolAssistantUUID": "87707f4c-b5d0-48ef-8951-6f51f7c089e9",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "17534bdc-c682-449b-afbd-9cd4dfa99aa8",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 21_

```json
{
  "type": "last-prompt",
  "lastPrompt": "Complete the research direction below with implementation details.  **Today's date: 2026-05-27 (UTC).** Only recommend venues whose deadline has NOT yet passed.  {   \"title\": \"Premise-Graph Contrastiv…",
  "leafUuid": "50fde36b-df6b-478e-93b8-0627cd7f863e",
  "sessionId": "17534bdc-c682-449b-afbd-9cd4dfa99aa8"
}
```

---

### Runtime record

_source line 22_

```json
{
  "type": "ai-title",
  "aiTitle": "Premise-graph contrastive training for process reward models",
  "sessionId": "17534bdc-c682-449b-afbd-9cd4dfa99aa8"
}
```

---

### Tool result

_source line 23 · 2026-05-27T08:11:04.393Z_

<details><summary>↩ Tool result · `toolu_01HLg4TcrQJqeuMFNKdrA9rN`</summary>

```text
I now have all the information needed. Here is the complete verification report for all 12 papers.

---

## Paper Verification Report

### 1. "Reward Under Attack" (arXiv:2603.06621, March 2026)
- **Status: REAL -- but date is slightly off**
- **Correct title:** "Reward Under Attack: Analyzing the Robustness and Hackability of Process Reward Models"
- **ArXiv ID:** 2603.06621 (confirmed)
- **Date:** February 20, 2026 (not March 2026 as claimed; the 2603 prefix suggests it was processed/published in the March listing, but submitted Feb 20)
- **Description:** Introduces a three-tiered adversarial diagnostic framework for PRMs. Core finding: current PRMs function as fluency detectors rather than reasoning verifiers, with 43% of reward gains attributable to stylistic exploitation.

### 2. "Reward Models Identify Consistency, Not Causality" (arXiv:2502.14619, Feb 2025)
- **Status: REAL**
- **Correct title:** "Reward Models Identify Consistency, Not Causality"
- **ArXiv ID:** 2502.14619 (confirmed)
- **Date:** February 20, 2025 (confirmed)
- **Authors:** Yuhui Xu, Hanze Dong, Lei Wang, Caiming Xiong, Junnan Li
- **Description:** Shows that state-of-the-art reward models prioritize structural consistency over causal correctness. Removing the problem statement has minimal impact on reward scores, whereas altering numerical values or disrupting reasoning flow significantly affects RM outputs.

### 3. PERL (ICML 2025)
- **Status: REAL -- but the name/description needs correction**
- **Correct title:** "Premise-Augmented Reasoning Chains Improve Error Identification in Math Reasoning with LLMs"
- **ArXiv ID:** 2502.02362
- **Venue:** ICML 2025 (confirmed, presented as poster)
- **Clarification:** PERL is the name of the **dataset** (Premises and ERrors identification in LLMs), not the method. The method is called PARC (Premise Augmented Reasoning Chains). PARC restructures linear reasoning chains into DAGs where nodes are steps and edges are premise links. The description "premise dependency links between reasoning steps" is essentially correct.

### 4. DAG-Math (2025)
- **Status: REAL**
- **Correct title:** "DAG-Math: Graph-of-Thought Guided Mathematical Reasoning in LLMs"
- **ArXiv ID:** 2510.19842
- **Date:** First submitted October 19, 2025; latest version March 1, 2026
- **Description:** Models Chain-of-Thought as a rule-based stochastic process over directed acyclic graphs (DAGs), where nodes represent intermediate derivation states and edges encode rule applications. Introduces "logical closeness" metric. The description "dependency graph extraction from math reasoning" is approximately correct, though the paper is more about using DAG structure to guide and evaluate reasoning rather than purely extracting dependencies.

### 5. ProofFlow (2025)
- **Status: REAL -- but description needs correction**
- **Correct title:** "ProofFlow: A Dependency Graph Approach to Faithful Proof Autoformalization"
- **ArXiv ID:** 2510.15981
- **Date:** October 13, 2025
- **Description:** This is about **proof autoformalization**, not dependency graph extraction from math reasoning per se. It uses a lemma-based approach to formalize each proof step as an intermediate lemma, preserving logical structure. Includes a benchmark of 184 problems with step-by-step solutions and logical dependency graphs, and introduces ProofScore as a composite metric.

### 6. CRA (Aug 2025)
- **Status: REAL**
- **Correct title:** "Causal Reward Adjustment: Mitigating Reward Hacking in External Reasoning via Backdoor Correction"
- **ArXiv ID:** 2508.04216
- **Date:** August 6, 2025 (confirmed)
- **Authors:** Ruike Song, Zeen Song, Huijie Guo, Wenwen Qiang
- **Description:** Trains sparse autoencoders on PRM internal activations to recover interpretable features, identifies confounding features associated with reward hacking, then applies backdoor adjustment to correct confounding. The description "post-hoc sparse autoencoder correction for PRMs" is accurate.

### 7. APRM (2025)
- **Status: REAL**
- **Correct title:** "Adversarial Training for Process Reward Models"
- **ArXiv ID:** 2511.22888
- **Date:** November 28, 2025
- **Authors:** Gurusha Juneja, Deepak Nathani, William Yang Wang
- **Description:** A Generator learns to produce reasoning errors to deceive a PRM, while the PRM concurrently learns to detect them, creating progressively harder negatives. Achieves +3.4pp on in-distribution and +5.3pp on out-of-distribution tasks vs. ReST-MCTS. The description "adversarial training for PRMs" is accurate.

### 8. CRM (ICLR 2026)
- **Status: REAL**
- **Correct title:** "Linking Process to Outcome: Conditional Reward Modeling for LLM Reasoning"
- **ArXiv ID:** 2509.26578
- **Venue:** ICLR 2026 (confirmed -- published as a conference paper)
- **Authors:** Zheng Zhang, Ziwei Shan, Kaitao Song, Yexin Li, Kan Ren
- **Description:** Frames reasoning as a temporal process where each step's reward is conditioned on all preceding steps and explicitly linked to the final outcome. The description "sequential conditioning on preceding steps" is accurate.

### 9. PURE (NeurIPS 2025)
- **Status: REAL**
- **Correct title:** "Stop Summation: Min-Form Credit Assignment Is All Process Reward Model Needs for Reasoning"
- **ArXiv ID:** 2504.15275
- **Venue:** NeurIPS 2025 (confirmed)
- **Authors:** Jie Cheng, Gang Xiong, Ruixi Qiao, Lijun Li, Chao Guo, Junle Wang, Yisheng Lv, Fei-Yue Wang
- **Description:** PURE = Process sUpervised Reinforcement lEarning. Proposes min-form credit assignment (value = minimum of future rewards) instead of summation-form to address PRM-induced reward hacking. The description "min-form credit aggregation" is accurate.

### 10. GenPRM (AAAI 2026)
- **Status: REAL**
- **Correct title:** "GenPRM: Scaling Test-Time Compute of Process Reward Models via Generative Reasoning"
- **ArXiv ID:** 2504.00891
- **Venue:** AAAI 2026 (confirmed)
- **Authors:** Jian Zhao, Runze Liu, Kaiyan Zhang, et al.
- **Description:** A generative PRM that performs explicit CoT reasoning with code verification before judging each reasoning step. Uses Relative Progress Estimation (RPE) for process supervision labels. The description "code-verified step analysis" is accurate.

### 11. AgentEval (2026)
- **Status: REAL**
- **Correct title:** "AgentEval: DAG-Structured Step-Level Evaluation for Agentic Workflows with Error Propagation Tracking"
- **ArXiv ID:** 2604.23581
- **Date:** April 26, 2026
- **Description:** Formalizes agent executions as evaluation DAGs where each node carries typed quality metrics, uses hierarchical failure taxonomy (3 levels, 21 subcategories), and links nodes to upstream dependencies for automated root cause attribution. DAG-based dependency modeling alone contributes +22pp to failure detection recall and +34pp to root cause accuracy. The description "DAG-based dependency modeling" is accurate. Note: this is about **agentic workflow evaluation**, not specifically about PRMs/math reasoning.

### 12. PRMBench
- **Status: REAL**
- **Correct title:** "PRMBench: A Fine-grained and Challenging Benchmark for Process-Level Reward Models"
- **ArXiv ID:** 2501.03124
- **Date:** January 6, 2025
- **Venue:** ACL 2025 (Long Paper)
- **Authors:** Mingyang Song, Zhaochen Su, Xiaoye Qu, Jiawei Zhou, Yu Cheng
- **Description:** Benchmark with 6,216 problems and 83,456 step-level labels evaluating PRMs across simplicity, soundness, and sensitivity. Best model (Gemini-2-Thinking) scores 68.8 vs. human ceiling of 83.8. The description "benchmark for process reward models" is accurate.

---

## Summary

All 12 papers are **real and verifiable**. Minor corrections needed:
- Paper 1: Date is Feb 20, 2026, not "March 2026"
- Paper 3: PERL is the dataset name; the method is PARC; full title is "Premise-Augmented Reasoning Chains Improve Error Identification in Math Reasoning with LLMs"
- Paper 5: ProofFlow is about proof autoformalization, not generic dependency graph extraction from math reasoning
- Paper 11: AgentEval is about agentic workflow evaluation, not specifically PRM-related
- Paper 12: Venue is ACL 2025 (not specified in the original list)

Sources:
- [Reward Under Attack](https://arxiv.org/abs/2603.06621)
- [Reward Models Identify Consistency, Not Causality](https://arxiv.org/abs/2502.14619)
- [PARC/PERL - ICML 2025](https://arxiv.org/abs/2502.02362)
- [DAG-Math](https://arxiv.org/abs/2510.19842)
- [ProofFlow](https://arxiv.org/abs/2510.15981)
- [CRA - Causal Reward Adjustment](https://arxiv.org/abs/2508.04216)
- [APRM - Adversarial Training for PRMs](https://arxiv.org/abs/2511.22888)
- [CRM - Conditional Reward Modeling (ICLR 2026)](https://arxiv.org/abs/2509.26578)
- [PURE - Stop Summation (NeurIPS 2025)](https://arxiv.org/abs/2504.15275)
- [GenPRM (AAAI 2026)](https://arxiv.org/abs/2504.00891)
- [AgentEval](https://arxiv.org/abs/2604.23581)
- [PRMBench (ACL 2025)](https://arxiv.org/abs/2501.03124)

agentId: a534528554d623705 (use SendMessage with to: 'a534528554d623705' to continue this agent)
&lt;usage>total_tokens: 27947
tool_uses: 22
duration_ms: 417872&lt;/usage>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "1c9ab1a3-72c7-468d-98af-1d5b9f458480",
  "isSidechain": false,
  "promptId": "e22bfc79-0a49-4220-ab7a-aad9ac9cf7cd",
  "type": "user",
  "uuid": "dd77d77b-55b3-4d84-9e8c-ab001789267c",
  "toolUseResult": {
    "status": "completed",
    "prompt": "I need to verify that the following papers are real and get their correct details. For each paper, use WebSearch to confirm it exists, get the correct venue/year, and arxiv ID.\n\nPapers to verify:\n1. \"Reward Under Attack\" (arXiv:2603.06621, March 2026) - about PRMs as fluency detectors\n2. \"Reward Models Identify Consistency, Not Causality\" (arXiv:2502.14619, Feb 2025)\n3. PERL (ICML 2025) - premise dependency links between reasoning steps\n4. DAG-Math (2025) - dependency graph extraction from math reasoning\n5. ProofFlow (2025) - dependency graph extraction\n6. CRA (Aug 2025) - post-hoc sparse autoencoder correction for PRMs\n7. APRM (2025) - adversarial training for PRMs\n8. CRM (ICLR 2026) - sequential conditioning on preceding steps\n9. PURE (NeurIPS 2025) - min-form credit aggregation\n10. GenPRM (AAAI 2026) - code-verified step analysis\n11. AgentEval (2026) - DAG-based dependency modeling\n12. PRMBench - benchmark for process reward models\n\nFor each paper, search for it specifically and report:\n- Whether it's real/verifiable\n- Correct title, venue, year\n- ArXiv ID if available\n- Brief description of what it does\n\nBe strict - if you can't find clear evidence a paper exists, mark it as unverifiable.",
    "agentId": "a534528554d623705",
    "agentType": "general-purpose",
    "content": [
      {
        "type": "text",
        "text": "I now have all the information needed. Here is the complete verification report for all 12 papers.\n\n---\n\n## Paper Verification Report\n\n### 1. \"Reward Under Attack\" (arXiv:2603.06621, March 2026)\n- **Status: REAL -- but date is slightly off**\n- **Correct title:** \"Reward Under Attack: Analyzing the Robustness and Hackability of Process Reward Models\"\n- **ArXiv ID:** 2603.06621 (confirmed)\n- **Date:** February 20, 2026 (not March 2026 as claimed; the 2603 prefix suggests it was processed/published in the March listing, but submitted Feb 20)\n- **Description:** Introduces a three-tiered adversarial diagnostic framework for PRMs. Core finding: current PRMs function as fluency detectors rather than reasoning verifiers, with 43% of reward gains attributable to stylistic exploitation.\n\n### 2. \"Reward Models Identify Consistency, Not Causality\" (arXiv:2502.14619, Feb 2025)\n- **Status: REAL**\n- **Correct title:** \"Reward Models Identify Consistency, Not Causality\"\n- **ArXiv ID:** 2502.14619 (confirmed)\n- **Date:** February 20, 2025 (confirmed)\n- **Authors:** Yuhui Xu, Hanze Dong, Lei Wang, Caiming Xiong, Junnan Li\n- **Description:** Shows that state-of-the-art reward models prioritize structural consistency over causal correctness. Removing the problem statement has minimal impact on reward scores, whereas altering numerical values or disrupting reasoning flow significantly affects RM outputs.\n\n### 3. PERL (ICML 2025)\n- **Status: REAL -- but the name/description needs correction**\n- **Correct title:** \"Premise-Augmented Reasoning Chains Improve Error Identification in Math Reasoning with LLMs\"\n- **ArXiv ID:** 2502.02362\n- **Venue:** ICML 2025 (confirmed, presented as poster)\n- **Clarification:** PERL is the name of the **dataset** (Premises and ERrors identification in LLMs), not the method. The method is called PARC (Premise Augmented Reasoning Chains). PARC restructures linear reasoning chains into DAGs where nodes are steps and edges are premise links. The description \"premise dependency links between reasoning steps\" is essentially correct.\n\n### 4. DAG-Math (2025)\n- **Status: REAL**\n- **Correct title:** \"DAG-Math: Graph-of-Thought Guided Mathematical Reasoning in LLMs\"\n- **ArXiv ID:** 2510.19842\n- **Date:** First submitted October 19, 2025; latest version March 1, 2026\n- **Description:** Models Chain-of-Thought as a rule-based stochastic process over directed acyclic graphs (DAGs), where nodes represent intermediate derivation states and edges encode rule applications. Introduces \"logical closeness\" metric. The description \"dependency graph extraction from math reasoning\" is approximately correct, though the paper is more about using DAG structure to guide and evaluate reasoning rather than purely extracting dependencies.\n\n### 5. ProofFlow (2025)\n- **Status: REAL -- but description needs correction**\n- **Correct title:** \"ProofFlow: A Dependency Graph Approach to Faithful Proof Autoformalization\"\n- **ArXiv ID:** 2510.15981\n- **Date:** October 13, 2025\n- **Description:** This is about **proof autoformalization**, not dependency graph extraction from math reasoning per se. It uses a lemma-based approach to formalize each proof step as an intermediate lemma, preserving logical structure. Includes a benchmark of 184 problems with step-by-step solutions and logical dependency graphs, and introduces ProofScore as a composite metric.\n\n### 6. CRA (Aug 2025)\n- **Status: REAL**\n- **Correct title:** \"Causal Reward Adjustment: Mitigating Reward Hacking in External Reasoning via Backdoor Correction\"\n- **ArXiv ID:** 2508.04216\n- **Date:** August 6, 2025 (confirmed)\n- **Authors:** Ruike Song, Zeen Song, Huijie Guo, Wenwen Qiang\n- **Description:** Trains sparse autoencoders on PRM internal activations to recover interpretable features, identifies confounding features associated with reward hacking, then applies backdoor adjustment to correct confounding. The description \"post-hoc sparse autoencoder correction for PRMs\" is accurate.\n\n### 7. APRM (2025)\n- **Status: REAL**\n- **Correct title:** \"Adversarial Training for Process Reward Models\"\n- **ArXiv ID:** 2511.22888\n- **Date:** November 28, 2025\n- **Authors:** Gurusha Juneja, Deepak Nathani, William Yang Wang\n- **Description:** A Generator learns to produce reasoning errors to deceive a PRM, while the PRM concurrently learns to detect them, creating progressively harder negatives. Achieves +3.4pp on in-distribution and +5.3pp on out-of-distribution tasks vs. ReST-MCTS. The description \"adversarial training for PRMs\" is accurate.\n\n### 8. CRM (ICLR 2026)\n- **Status: REAL**\n- **Correct title:** \"Linking Process to Outcome: Conditional Reward Modeling for LLM Reasoning\"\n- **ArXiv ID:** 2509.26578\n- **Venue:** ICLR 2026 (confirmed -- published as a conference paper)\n- **Authors:** Zheng Zhang, Ziwei Shan, Kaitao Song, Yexin Li, Kan Ren\n- **Description:** Frames reasoning as a temporal process where each step's reward is conditioned on all preceding steps and explicitly linked to the final outcome. The description \"sequential conditioning on preceding steps\" is accurate.\n\n### 9. PURE (NeurIPS 2025)\n- **Status: REAL**\n- **Correct title:** \"Stop Summation: Min-Form Credit Assignment Is All Process Reward Model Needs for Reasoning\"\n- **ArXiv ID:** 2504.15275\n- **Venue:** NeurIPS 2025 (confirmed)\n- **Authors:** Jie Cheng, Gang Xiong, Ruixi Qiao, Lijun Li, Chao Guo, Junle Wang, Yisheng Lv, Fei-Yue Wang\n- **Description:** PURE = Process sUpervised Reinforcement lEarning. Proposes min-form credit assignment (value = minimum of future rewards) instead of summation-form to address PRM-induced reward hacking. The description \"min-form credit aggregation\" is accurate.\n\n### 10. GenPRM (AAAI 2026)\n- **Status: REAL**\n- **Correct title:** \"GenPRM: Scaling Test-Time Compute of Process Reward Models via Generative Reasoning\"\n- **ArXiv ID:** 2504.00891\n- **Venue:** AAAI 2026 (confirmed)\n- **Authors:** Jian Zhao, Runze Liu, Kaiyan Zhang, et al.\n- **Description:** A generative PRM that performs explicit CoT reasoning with code verification before judging each reasoning step. Uses Relative Progress Estimation (RPE) for process supervision labels. The description \"code-verified step analysis\" is accurate.\n\n### 11. AgentEval (2026)\n- **Status: REAL**\n- **Correct title:** \"AgentEval: DAG-Structured Step-Level Evaluation for Agentic Workflows with Error Propagation Tracking\"\n- **ArXiv ID:** 2604.23581\n- **Date:** April 26, 2026\n- **Description:** Formalizes agent executions as evaluation DAGs where each node carries typed quality metrics, uses hierarchical failure taxonomy (3 levels, 21 subcategories), and links nodes to upstream dependencies for automated root cause attribution. DAG-based dependency modeling alone contributes +22pp to failure detection recall and +34pp to root cause accuracy. The description \"DAG-based dependency modeling\" is accurate. Note: this is about **agentic workflow evaluation**, not specifically about PRMs/math reasoning.\n\n### 12. PRMBench\n- **Status: REAL**\n- **Correct title:** \"PRMBench: A Fine-grained and Challenging Benchmark for Process-Level Reward Models\"\n- **ArXiv ID:** 2501.03124\n- **Date:** January 6, 2025\n- **Venue:** ACL 2025 (Long Paper)\n- **Authors:** Mingyang Song, Zhaochen Su, Xiaoye Qu, Jiawei Zhou, Yu Cheng\n- **Description:** Benchmark with 6,216 problems and 83,456 step-level labels evaluating PRMs across simplicity, soundness, and sensitivity. Best model (Gemini-2-Thinking) scores 68.8 vs. human ceiling of 83.8. The description \"benchmark for process reward models\" is accurate.\n\n---\n\n## Summary\n\nAll 12 papers are **real and verifiable**. Minor corrections needed:\n- Paper 1: Date is Feb 20, 2026, not \"March 2026\"\n- Paper 3: PERL is the dataset name; the method is PARC; full title is \"Premise-Augmented Reasoning Chains Improve Error Identification in Math Reasoning with LLMs\"\n- Paper 5: ProofFlow is about proof autoformalization, not generic dependency graph extraction from math reasoning\n- Paper 11: AgentEval is about agentic workflow evaluation, not specifically PRM-related\n- Paper 12: Venue is ACL 2025 (not specified in the original list)\n\nSources:\n- [Reward Under Attack](https://arxiv.org/abs/2603.06621)\n- [Reward Models Identify Consistency, Not Causality](https://arxiv.org/abs/2502.14619)\n- [PARC/PERL - ICML 2025](https://arxiv.org/abs/2502.02362)\n- [DAG-Math](https://arxiv.org/abs/2510.19842)\n- [ProofFlow](https://arxiv.org/abs/2510.15981)\n- [CRA - Causal Reward Adjustment](https://arxiv.org/abs/2508.04216)\n- [APRM - Adversarial Training for PRMs](https://arxiv.org/abs/2511.22888)\n- [CRM - Conditional Reward Modeling (ICLR 2026)](https://arxiv.org/abs/2509.26578)\n- [PURE - Stop Summation (NeurIPS 2025)](https://arxiv.org/abs/2504.15275)\n- [GenPRM (AAAI 2026)](https://arxiv.org/abs/2504.00891)\n- [AgentEval](https://arxiv.org/abs/2604.23581)\n- [PRMBench (ACL 2025)](https://arxiv.org/abs/2501.03124)"
      }
    ],
    "totalDurationMs": 417872,
    "totalTokens": 27947,
    "totalToolUseCount": 22,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 667,
      "cache_read_input_tokens": 24552,
      "output_tokens": 2727,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 667
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 2727,
          "cache_read_input_tokens": 24552,
          "cache_creation_input_tokens": 667,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 667,
            "ephemeral_1h_input_tokens": 0
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "toolStats": {
      "readCount": 0,
      "searchCount": 0,
      "bashCount": 0,
      "editFileCount": 0,
      "linesAdded": 0,
      "linesRemoved": 0,
      "otherToolCount": 22
    }
  },
  "sourceToolAssistantUUID": "1c9ab1a3-72c7-468d-98af-1d5b9f458480",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "17534bdc-c682-449b-afbd-9cd4dfa99aa8",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 24 · 2026-05-27T08:12:30.442Z_

<details><summary>Logged reasoning block</summary>

```text
Now I have comprehensive information from all four research agents. Let me synthesize everything into the final JSON output.

Key findings:

**Novelty check:** The specific combination of premise dependency graphs + contrastive PRM training appears NOVEL. Closest concurrent work:
- CPMI (arXiv:2604.10660, April 2026) - contrastive PRM but no graphs
- PQM (arXiv:2410.11287) - step dependencies but no graphs
- RewardFlow (arXiv:2603.18859, March 2026) - graph topology for rewards but state graphs, not premise graphs


- Graph of Verification (GoV) - DAG-based verification but training-free

All 12 papers check out as legitimate. For timing, I'm looking at venue deadlines that fall after the current date: AAAI 2027 in late July, ICLR 2027 in late September, AISTATS 2027 in October, plus some earlier workshop and conference deadlines in June and August. Now I need to identify which models would be most suitable for this approach.

I'm considering Qwen2.5-Math-7B-Instruct as the foundation for a process reward model, along with the ThinkPRM method which is particularly data-efficient, and PathFinder-PRM-7B which currently holds the best performance on PRMBench at 67.7. Looking at what I need to beat: PathFinder achieves 67.7 on PRMBench, Qwen2.5-Math-PRM gets 73.5 F1 on ProcessBench, humans reach 83.8 on PRMBench, and the BoN-8 baseline sits at 49.6. For computational requirements, standard 7B PRM training takes roughly 32 A100-hours, but adversarial training jumps to around 672 A100-hours, with ThinkPRM-14 requiring additional resources.

The training data consists of PRM800K with about 265K samples after deduplication and Math-Shepherd with roughly 445K samples. My approach extracts premise dependency DAGs from reasoning chains using PARC's method which achieves 90% recall, then constructs structure-aware contrastive pairs where positive examples preserve logical dependencies while varying surface form, and hard negatives break those dependencies while remaining fluent. I'll train the PRM with a combined objective that predicts step-level correctness while using contrastive loss to make it invariant to surface form but sensitive to DAG structure, using Qwen2.5-Math-7B as the base model.

For the full pipeline, I'm estimating around 800-1200 A100-hours total: roughly 100 hours for DAG extraction across 300K chains, 150 hours for generating contrastive pairs, 400 hours for PRM training with multiple runs, 50 hours for evaluation, and 300 hours for ablations, which would take about 3-4 months to complete.

Using Claude API to help with DAG extraction and contrastive pair filtering could reduce this to 600-800 GPU hours over 2-3 months, though the API costs would be around $500-800. An automated approach with experiment sweeps would be faster at 500-700 hours over 6-8 weeks, but the main constraint remains the quality of DAG extraction and contrastive pair generation, with API costs around $1,000-1,500.

For publication, AAAI 2027 in July would be tight with just two months, but ICLR 2027 in September is the more realistic target.

I'm also considering AISTATS 2027 in October as a backup option. The work addresses a fundamental problem with a novel combination of techniques, positioning it well for top-tier venues. I've been compiling the key references that support this approach—there's solid recent work on reward model limitations, causal reasoning in code, and process reward models that all feed into this research direction.

Now I'm thinking through the concurrent work landscape more carefully, including recent papers on reward flow and process benchmarking that need to be properly cited. I should finalize the JSON structure for the submission.

Actually, I need to reconsider the resource requirements more carefully. For a manual implementation approach, I'm calculating GPU hours needed for fine-tuning a 7B model, running DAG extraction across roughly 300K chains, and generating contrastive pairs—the DAG extraction alone would take around 28 hours on an A100 given the token throughput, and the contrastive pair generation would be comparable in scale.

For the full manual pipeline including PRM training across multiple epochs and ablations, I'm looking at roughly 500-800 A100-hours total over 3-4 months for a small team, costing around $1,500-$2,400. With human-in-the-loop assistance, the GPU requirements drop to 400-600 hours since fewer experiments fail, reducing both timeline and cost while adding Claude API expenses. The fully automated approach would push GPU usage higher to 600-1000 hours due to more extensive hyperparameter exploration.

Now I'm reconsidering the core methodology—the key insight is using PARC's approach to extract premise dependency graphs from reasoning chains, then constructing contrastive pairs that either preserve the graph structure through rephrasing or deliberately break logical dependencies to create hard negatives.

I'm planning a dual-objective training setup that combines standard step correctness classification with a graph-contrastive loss, optionally adding graph-aware attention masking so steps only attend to their dependencies. The base model will be Qwen2.5-Math-7B-Instruct, trained on PRM800K and Math-Shepherd chains with LLM-generated perturbations for the contrastive pairs.

Now I need to finalize the JSON schema, making sure the project name stays under 30 characters in snake_case and the description hits 150-200 words while covering all required fields. merged with existing ones. I should also note the concurrent work from CPMI and RewardFlow in this landscape.

For the approach, I'm laying out a method that extracts premise dependency DAGs from mathematical reasoning using PARC's extraction technique, then builds contrastive training pairs where surface-level rephrasing that preserves logical structure serves as positives, while fluent perturbations that break premise links act as hard negatives. I'll train a Qwen2.5-Math-7B model with dual objectives—standard step correctness plus a graph-contrastive loss that forces the model to learn representations sensitive to logical dependencies rather than surface form. The training data comes from augmenting PRM800K and Math-Shepherd with roughly 300K DAG-annotated solutions and 600K contrastive pairs generated through LLM paraphrasing and targeted premise corruption, then evaluating across PRMBench, ProcessBench, and adversarial robustness benchmarks to hit >70 on PRMBench and reduce stylistic shortcut exploitation by over 50%. consistency rather than causality (Xu et al., 2025). Our key insight is that premise dependency DAGs, extractable at 90% recall (PARC/PERL, ICML 2025), provide a structural scaffold for contrastive training that disentangles these confounds. We construct graph-preserving surface perturbations (varied phrasing, identical logic) and graph-breaking fluent perturbations (broken premise links, maintained fluency) as contrastive pairs, training with a dual objective that combines step-correctness prediction with InfoNCE loss over DAG-anchored representations. Built on Qwen2.5-Math-7B-Instruct with PRM800K and Math-Shepherd data augmented by ~600K structure-aware contrastive pairs, PGCT targets >70 on PRMBench (vs. 67.7 SOTA) and dramatically reduces adversarial exploitability. No prior work combines premise dependency graphs with contrastive PRM training — concurrent approaches like CPMI, CRM, and RewardFlow tackle related problems but don't incorporate explicit logical structure. Now I'm thinking through the venue timeline: ICLR 2027 looks like the best fit with its September deadline, though AAAI 2027 in July could work if we're aggressive, and AISTATS 2027 serves as a solid backup option. I'm continuing to compile the reference list, adding papers on process reward model benchmarking and evaluation frameworks.

Now I'm finalizing the classification as top-tier because this approach combines novel elements addressing a fundamental problem, has clear empirical motivation, works with existing infrastructure, and shows substantial room for improvement over current baselines—plus no existing work tackles this exact combination.

Writing JSON structure...
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "dd77d77b-55b3-4d84-9e8c-ab001789267c",
  "isSidechain": false,
  "requestId": "req_011CbSjbnpDvANmguNhuwM2A",
  "type": "assistant",
  "uuid": "92604d70-85e3-432e-8ad0-3283487cf456",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "17534bdc-c682-449b-afbd-9cd4dfa99aa8",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015gQFygYU7et7M4HysLVhC4",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7336,
      "cache_creation_input_tokens": 7215,
      "cache_read_input_tokens": 14396,
      "output_tokens": 6593,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 7215,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 7336,
          "output_tokens": 6593,
          "cache_read_input_tokens": 14396,
          "cache_creation_input_tokens": 7215,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 7215
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

### Assistant

_source line 25 · 2026-05-27T08:13:16.314Z_

Now I have comprehensive data from all four research threads. Let me synthesize everything into the final output.

Key findings:
- **Novelty confirmed**: No paper combines premise dependency DAGs with contrastive PRM training. Closest concurrent: CPMI (arXiv:2604.10660) uses contrastive MI but no graphs; RewardFlow (arXiv:2603.18859) uses graph topology but state graphs, not premise DAGs.
- **All 12 papers verified as real**.
- **Venues after 2026-05-27**: AAAI 2027 (July 28), ICLR 2027 (Sept 24), AISTATS 2027 (Oct 10).
- **SOTA baselines**: PRMBench 67.7 (PathFinder-PRM-7B), ProcessBench F1 73.5 (Qwen2.5-Math-PRM-7B), human ceiling 83.8.
- **Best base model**: Qwen2.5-Math-7B-Instruct.

```json
{
  "title": "Premise-Graph Contrastive Training for Logic-Grounded Process Reward Models",
  "core_problem": "Current process reward models confuse surface fluency with logical validity — 43% of PRM reward gains are attributable to stylistic shortcuts rather than reasoning correctness — leading to catastrophic reward hacking during RL training where policies achieve >0.9 PRM scores but <4% actual accuracy. Can we train PRMs that are invariant to surface form but sensitive to logical structure?",
  "opportunity": "PERL (ICML 2025) demonstrated that LLMs can extract premise dependency links between reasoning steps at 90% recall, and that premise-aware verification improves error detection by 6-16%. However, this structural information has only been used at evaluation time, not for PRM training. Simultaneously, DAG-Math (2025) and ProofFlow (2025) have made dependency graph extraction from mathematical reasoning chains feasible. No prior work combines these premise dependency structures with contrastive PRM training to explicitly disentangle logical validity from surface fluency — addressing the documented root cause of PRM fragility at training time rather than through post-hoc corrections.",
  "landscape": "The field has documented severe PRM robustness failures: 'Reward Under Attack' (arXiv:2603.06621, Feb 2026) showed PRMs function as fluency detectors with wide exploitable reward peaks, and 'Reward Models Identify Consistency, Not Causality' (arXiv:2502.14619, Feb 2025) confirmed this is fundamental. Existing defenses include CRA (Aug 2025, post-hoc sparse autoencoder correction), APRM (Nov 2025, adversarial training with harder negatives gaining +5.3pp OOD), CRM (ICLR 2026, sequential conditioning on preceding steps), and PURE (NeurIPS 2025, min-form credit aggregation). None uses explicit logical dependency structure during PRM training. On the infrastructure side, PARC/PERL (ICML 2025) showed premise links form DAGs with 90% extractable recall; GenPRM (AAAI 2026) provides code-verified step analysis; and AgentEval (arXiv:2604.23581, 2026) showed DAG-based dependency modeling yields +22pp failure detection recall over flat evaluation. The best PRMs on PRMBench score 67.7 (PathFinder-PRM-7B) vs. 83.8 human ceiling, leaving a 16-point gap where structural approaches could contribute. Concurrent work: CPMI (arXiv:2604.10660, April 2026) uses contrastive mutual information for PRM auto-labeling but does not employ premise dependency graphs; RewardFlow (arXiv:2603.18859, March 2026) propagates rewards over state-transition graphs in agentic tasks but uses no contrastive training and targets a different graph type; Graph of Verification (GoV) decomposes reasoning into DAGs for verification but is training-free. The specific combination of premise dependency DAGs with contrastive PRM training remains untried.",
  "inspired_by": "Gap from 'Reward Models Identify Consistency, Not Causality' (2025) documenting PRMs' fundamental inability to verify logical validity + quantitative evidence from 'Reward Under Attack' (2026) showing 43% stylistic shortcut exploitation + untried combination of PERL's premise-dependency extraction (proven feasible at 90% recall) with contrastive PRM training + building blocks from DAG-Math, ProofFlow, and GenPRM for dependency graph infrastructure",
  "approach": "Extract premise dependency DAGs from mathematical reasoning chains using PARC's proven extraction method (90% recall on Llama-3.1-8B-Instruct), then construct structure-aware contrastive training pairs: graph-preserving surface perturbations (rephrased steps maintaining identical DAG topology) as positives, and graph-breaking fluent perturbations (severed premise links, dangling references, logically invalid steps preserving surface fluency) as hard negatives. Train a Qwen2.5-Math-7B-Instruct-based PRM with a dual objective combining standard step-correctness classification and a graph-contrastive InfoNCE loss over DAG-anchored step embeddings, forcing the model to learn representations invariant to surface form but sensitive to logical dependency structure. Augment PRM800K and Math-Shepherd seed chains (~300K solutions) with DAG annotations and ~600K contrastive pairs generated via LLM paraphrasing and targeted premise-link corruption. Evaluate on PRMBench (targeting >70 vs. 67.7 SOTA), ProcessBench, and the adversarial robustness suite from 'Reward Under Attack,' measuring both step-level accuracy and reduction in stylistic shortcut exploitability.",
  "resource_estimate": {
    "manual": {
      "gpu_hours": "700-1000 A100-hours (DAG extraction: ~80h, contrastive pair generation: ~120h, PRM training with ablations: ~400h, evaluation and baselines: ~100h)",
      "timeline": "14-18 weeks for 2-3 researchers",
      "estimated_gpu_cost": "$2,100-$3,000 at $3/hr A100 spot pricing"
    },
    "human_in_loop": {
      "gpu_hours": "500-700 A100-hours (Claude accelerates data pipeline debugging, contrastive pair quality filtering, and ablation design, reducing failed experiments ~30%)",
      "timeline": "10-14 weeks for 2 researchers",
      "claude_api_cost": "$400-$700 (data quality analysis, code generation, experiment triage)",
      "estimated_gpu_cost": "$1,500-$2,100 at $3/hr A100 spot pricing"
    },
    "auto_research": {
      "gpu_hours": "800-1200 A100-hours (more parallel sweeps offset by automated experiment selection)",
      "timeline": "6-8 weeks with automated pipeline",
      "claude_api_cost": "$1,000-$1,500 (automated DAG quality validation, contrastive pair generation, hyperparameter sweep orchestration, paper drafting)",
      "estimated_gpu_cost": "$2,400-$3,600 at $3/hr A100 spot pricing",
      "speed_bottleneck": "DAG extraction quality validation — premise link accuracy must be audited per-domain (algebra vs. geometry vs. combinatorics) before contrastive pairs are trustworthy; serial human spot-checks required"
    }
  },
  "target_venues": [
    "AAAI 2027 (abstract: July 21, paper: July 28, 2026)",
    "ICLR 2027 (abstract: Sept 19, paper: Sept 24, 2026)",
    "AISTATS 2027 (paper: Oct 10, 2026)"
  ],
  "level": "top-tier",
  "key_references": [
    "Reward Under Attack: Analyzing the Robustness and Hackability of Process Reward Models (arXiv 2026, arXiv:2603.06621)",
    "Reward Models Identify Consistency, Not Causality (arXiv 2025, arXiv:2502.14619)",
    "Premise-Augmented Reasoning Chains Improve Error Identification in Math Reasoning with LLMs — PARC/PERL (ICML 2025, arXiv:2502.02362)",
    "DAG-Math: Graph-of-Thought Guided Mathematical Reasoning in LLMs (arXiv 2025, arXiv:2510.19842)",
    "ProofFlow: A Dependency Graph Approach to Faithful Proof Autoformalization (arXiv 2025, arXiv:2510.15981)",
    "Causal Reward Adjustment: Mitigating Reward Hacking via Backdoor Correction — CRA (arXiv 2025, arXiv:2508.04216)",
    "Adversarial Training for Process Reward Models — APRM (arXiv 2025, arXiv:2511.22888)",
    "Linking Process to Outcome: Conditional Reward Modeling for LLM Reasoning — CRM (ICLR 2026, arXiv:2509.26578)",
    "Stop Summation: Min-Form Credit Assignment Is All Process Reward Model Needs for Reasoning — PURE (NeurIPS 2025, arXiv:2504.15275)",
    "GenPRM: Scaling Test-Time Compute of Process Reward Models via Generative Reasoning (AAAI 2026, arXiv:2504.00891)",
    "AgentEval: DAG-Structured Step-Level Evaluation for Agentic Workflows with Error Propagation Tracking (arXiv 2026, arXiv:2604.23581)",
    "PRMBench: A Fine-grained and Challenging Benchmark for Process-Level Reward Models (ACL 2025, arXiv:2501.03124)",
    "Efficient Process Reward Modeling via Contrastive Mutual Information — CPMI (arXiv 2026, arXiv:2604.10660)",
    "RewardFlow: Topology-Aware Reward Propagation on State Graphs (arXiv 2026, arXiv:2603.18859)",
    "PathFinder-PRM: Exploring Path Diversity in Step-Level Reward Models (arXiv 2025)"
  ],
  "description": "We propose Premise-Graph Contrastive Training (PGCT), a method that leverages explicit logical dependency structure to train process reward models resistant to surface-form reward hacking. Current PRMs conflate fluency with validity — 43% of reward gains stem from stylistic shortcuts, and PRMs detect consistency rather than causality. Our key insight is that premise dependency DAGs, extractable at 90% recall via PARC (ICML 2025), provide a structural scaffold for contrastive training that disentangles these confounds. We construct graph-preserving surface perturbations (varied phrasing, identical logic) and graph-breaking fluent perturbations (severed premise links, maintained fluency) as contrastive pairs, training with a dual objective combining step-correctness prediction and InfoNCE loss over DAG-anchored representations. Built on Qwen2.5-Math-7B-Instruct with PRM800K and Math-Shepherd data augmented by ~600K structure-aware contrastive pairs, PGCT targets >70 on PRMBench (vs. 67.7 SOTA, 83.8 human ceiling) and substantially reduced adversarial exploitability. No prior work combines premise dependency graphs with contrastive PRM training — concurrent approaches (CPMI, CRM, RewardFlow) address complementary aspects but omit explicit logical structure from the training signal.",
  "project_name": "premise_graph_contrastive_prm",
  "source": "web_research"
}
```

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "92604d70-85e3-432e-8ad0-3283487cf456",
  "isSidechain": false,
  "requestId": "req_011CbSjbnpDvANmguNhuwM2A",
  "type": "assistant",
  "uuid": "074a81db-0324-4672-b956-14f79d8feb9b",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "17534bdc-c682-449b-afbd-9cd4dfa99aa8",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015gQFygYU7et7M4HysLVhC4",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7336,
      "cache_creation_input_tokens": 7215,
      "cache_read_input_tokens": 14396,
      "output_tokens": 6593,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 7215,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 7336,
          "output_tokens": 6593,
          "cache_read_input_tokens": 14396,
          "cache_creation_input_tokens": 7215,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 7215
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

### Runtime record

_source line 26_

```json
{
  "type": "last-prompt",
  "lastPrompt": "Complete the research direction below with implementation details.  **Today's date: 2026-05-27 (UTC).** Only recommend venues whose deadline has NOT yet passed.  {   \"title\": \"Premise-Graph Contrastiv…",
  "leafUuid": "074a81db-0324-4672-b956-14f79d8feb9b",
  "sessionId": "17534bdc-c682-449b-afbd-9cd4dfa99aa8"
}
```

---

### Runtime record

_source line 27_

```json
{
  "type": "ai-title",
  "aiTitle": "Premise-graph contrastive training for process reward models",
  "sessionId": "17534bdc-c682-449b-afbd-9cd4dfa99aa8"
}
```

---

### Runtime record

_source line 28_

```json
{
  "type": "last-prompt",
  "lastPrompt": "Complete the research direction below with implementation details.  **Today's date: 2026-05-27 (UTC).** Only recommend venues whose deadline has NOT yet passed.  {   \"title\": \"Premise-Graph Contrastiv…",
  "leafUuid": "074a81db-0324-4672-b956-14f79d8feb9b",
  "sessionId": "17534bdc-c682-449b-afbd-9cd4dfa99aa8"
}
```

---

### Runtime record

_source line 29_

```json
{
  "type": "ai-title",
  "aiTitle": "Premise-graph contrastive training for process reward models",
  "sessionId": "17534bdc-c682-449b-afbd-9cd4dfa99aa8"
}
```

---
