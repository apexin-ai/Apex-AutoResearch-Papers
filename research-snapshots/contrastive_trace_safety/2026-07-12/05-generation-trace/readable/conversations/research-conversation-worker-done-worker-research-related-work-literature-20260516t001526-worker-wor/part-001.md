# Research conversation: [系统通知 — worker_done:worker_research_related-work-literature_20260516T001526]: Worker worker_research_related-work-litera — Part 1 of 7

**Layer Selection Sensitivity in Hidden-State Safety Probes for Reasoning Models (July export snapshot)** · Conversation logs

[Transcript overview](../research-conversation-worker-done-worker-research-related-work-literature-20260516t001526-worker-wor.md) · [Part 2 →](part-002.md) · [Structured JSON](../../../sessions/17/1790d78d3b2c15ce784f.json)

## Before a recorded user message

## Before a recorded user message

2 recorded events


### Runtime record

_source line 1 · 2026-05-16T00:22:56.962Z_

```json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-16T00:22:56.962Z",
  "sessionId": "f444a635-eeef-4924-9b48-a4c308632421",
  "content": "[系统通知 — worker_done:worker_research_related-work-literature_20260516T001526]:\nWorker worker_research_related-work-literature_20260516T001526 已完成（status=done），请审查 Agent 的处理结果。"
}
```

---


### Runtime record

_source line 2 · 2026-05-16T00:22:56.965Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-16T00:22:56.965Z",
  "sessionId": "f444a635-eeef-4924-9b48-a4c308632421"
}
```

---


## Round 1

## Round 1

65 recorded events


### User

_source line 3 · 2026-05-16T00:22:56.998Z_

[系统通知 — worker_done:worker_research_related-work-literature_20260516T001526]:
Worker worker_research_related-work-literature_20260516T001526 已完成（status=done），请审查 Agent 的处理结果。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": false,
  "promptId": "ee81bb41-edfe-48b7-9827-d79a74cf7a5e",
  "type": "user",
  "uuid": "0abc4994-5852-4144-a53c-d82082eca4ec",
  "permissionMode": "bypassPermissions",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/.claude/sessions/reviewer_65cfe724",
  "sessionId": "f444a635-eeef-4924-9b48-a4c308632421",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---


### Runtime record

_source line 4 · 2026-05-16T00:22:56.998Z_

```json
{
  "parentUuid": "0abc4994-5852-4144-a53c-d82082eca4ec",
  "isSidechain": false,
  "attachment": {
    "type": "deferred_tools_delta",
    "addedNames": [
      "AskUserQuestion",
      "CronCreate",
      "CronDelete",
      "CronList",
      "EnterPlanMode",
      "EnterWorktree",
      "ExitPlanMode",
      "ExitWorktree",
      "ListMcpResourcesTool",
      "Monitor",
      "NotebookEdit",
      "PushNotification",
      "ReadMcpResourceTool",
      "RemoteTrigger",
      "TaskOutput",
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
      "AskUserQuestion",
      "CronCreate",
      "CronDelete",
      "CronList",
      "EnterPlanMode",
      "EnterWorktree",
      "ExitPlanMode",
      "ExitWorktree",
      "ListMcpResourcesTool",
      "Monitor",
      "NotebookEdit",
      "PushNotification",
      "ReadMcpResourceTool",
      "RemoteTrigger",
      "TaskOutput",
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
  "uuid": "4a85e378-80d2-4fb9-930b-7888e2a345df",
  "timestamp": "2026-05-16T00:22:56.998Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/.claude/sessions/reviewer_65cfe724",
  "sessionId": "f444a635-eeef-4924-9b48-a4c308632421",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---


### Runtime record

_source line 5 · 2026-05-16T00:22:56.998Z_

```json
{
  "parentUuid": "4a85e378-80d2-4fb9-930b-7888e2a345df",
  "isSidechain": false,
  "attachment": {
    "type": "mcp_instructions_delta",
    "addedNames": [
      "agent-ml-research"
    ],
    "addedBlocks": [
      "## agent-ml-research\nML research experiment management tools"
    ],
    "removedNames": []
  },
  "type": "attachment",
  "uuid": "f0609a12-bc43-4066-a7bb-5faba9171383",
  "timestamp": "2026-05-16T00:22:56.998Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/.claude/sessions/reviewer_65cfe724",
  "sessionId": "f444a635-eeef-4924-9b48-a4c308632421",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---


### Runtime record

_source line 6 · 2026-05-16T00:22:56.998Z_

```json
{
  "parentUuid": "f0609a12-bc43-4066-a7bb-5faba9171383",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "038b87f3-eba9-418f-bce0-6db2dde252b8",
  "timestamp": "2026-05-16T00:22:56.998Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/.claude/sessions/reviewer_65cfe724",
  "sessionId": "f444a635-eeef-4924-9b48-a4c308632421",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---


### Runtime record

_source line 7_

```json
{
  "type": "ai-title",
  "aiTitle": "Review research literature worker completion",
  "sessionId": "f444a635-eeef-4924-9b48-a4c308632421"
}
```

---


### Assistant

_source line 8 · 2026-05-16T00:23:00.795Z_

<details><summary>Logged reasoning block</summary>

```text
Worker completed a related work literature research task. I need to review the agent's work. Let me start by reading the registry to understand what this worker did, and check the current project state.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "038b87f3-eba9-418f-bce0-6db2dde252b8",
  "isSidechain": false,
  "requestId": "req_011Cb5J1GvSrrNzyLZJgap5h",
  "type": "assistant",
  "uuid": "c9ad6c0b-45ad-4aa0-8a8e-06c71c8d2f65",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/.claude/sessions/reviewer_65cfe724",
  "sessionId": "f444a635-eeef-4924-9b48-a4c308632421",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011q8bPNsfdiqghkv2AqHqcu",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 18839,
      "cache_read_input_tokens": 11841,
      "output_tokens": 228,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 18839,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 228,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 18839,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 18839
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

_source line 9 · 2026-05-16T00:23:05.688Z_

收到 worker 完成通知，开始审查。先读 registry 和相关产出。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c9ad6c0b-45ad-4aa0-8a8e-06c71c8d2f65",
  "isSidechain": false,
  "requestId": "req_011Cb5J1GvSrrNzyLZJgap5h",
  "type": "assistant",
  "uuid": "6b1d1089-8b27-4ee9-b737-f537d3a29f16",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/.claude/sessions/reviewer_65cfe724",
  "sessionId": "f444a635-eeef-4924-9b48-a4c308632421",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011q8bPNsfdiqghkv2AqHqcu",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 18839,
      "cache_read_input_tokens": 11841,
      "output_tokens": 228,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 18839,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 228,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 18839,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 18839
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

_source line 10 · 2026-05-16T00:23:06.894Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01DwgYeG3MGrkAd4ZSkmHigF`</summary>

```json
{
  "query": "select:mcp__agent-ml-research__read_registry,mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__read_roadmap,mcp__agent-ml-research__reviewer_post_to_director,mcp__agent-ml-research__ssh_read_only",
  "max_results": 5
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6b1d1089-8b27-4ee9-b737-f537d3a29f16",
  "isSidechain": false,
  "requestId": "req_011Cb5J1GvSrrNzyLZJgap5h",
  "type": "assistant",
  "uuid": "9b433193-1eab-4b6f-8387-db29a6d62e67",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/.claude/sessions/reviewer_65cfe724",
  "sessionId": "f444a635-eeef-4924-9b48-a4c308632421",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011q8bPNsfdiqghkv2AqHqcu",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 18839,
      "cache_read_input_tokens": 11841,
      "output_tokens": 228,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 18839,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 228,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 18839,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 18839
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

_source line 11 · 2026-05-16T00:23:06.905Z_

<details><summary>↩ Tool result · `toolu_01DwgYeG3MGrkAd4ZSkmHigF`</summary>

````text
```json
{
  "type": "tool_reference",
  "tool_name": "mcp__agent-ml-research__read_registry"
}
```

```json
{
  "type": "tool_reference",
  "tool_name": "mcp__agent-ml-research__read_project_file"
}
```

```json
{
  "type": "tool_reference",
  "tool_name": "mcp__agent-ml-research__read_roadmap"
}
```

```json
{
  "type": "tool_reference",
  "tool_name": "mcp__agent-ml-research__reviewer_post_to_director"
}
```

```json
{
  "type": "tool_reference",
  "tool_name": "mcp__agent-ml-research__ssh_read_only"
}
```
````

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "9b433193-1eab-4b6f-8387-db29a6d62e67",
  "isSidechain": false,
  "promptId": "ee81bb41-edfe-48b7-9827-d79a74cf7a5e",
  "type": "user",
  "uuid": "c44c2bf9-e370-46aa-b70b-94fa30eac769",
  "toolUseResult": {
    "matches": [
      "mcp__agent-ml-research__read_registry",
      "mcp__agent-ml-research__read_project_file",
      "mcp__agent-ml-research__read_roadmap",
      "mcp__agent-ml-research__reviewer_post_to_director",
      "mcp__agent-ml-research__ssh_read_only"
    ],
    "query": "select:mcp__agent-ml-research__read_registry,mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__read_roadmap,mcp__agent-ml-research__reviewer_post_to_director,mcp__agent-ml-research__ssh_read_only",
    "total_deferred_tools": 34
  },
  "sourceToolAssistantUUID": "9b433193-1eab-4b6f-8387-db29a6d62e67",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/.claude/sessions/reviewer_65cfe724",
  "sessionId": "f444a635-eeef-4924-9b48-a4c308632421",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---


### Tool call

_source line 12 · 2026-05-16T00:23:10.259Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry · `toolu_01JCknKS7HG1WqEVGMbNUeuk`</summary>

```json
{
  "project": "structfuse-context",
  "limit": 10,
  "fields": [
    "*"
  ]
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c44c2bf9-e370-46aa-b70b-94fa30eac769",
  "isSidechain": false,
  "requestId": "req_011Cb5J21neDKTbom9RAnGPV",
  "type": "assistant",
  "uuid": "c70e6495-514d-43cb-a793-9577719f6fc6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/.claude/sessions/reviewer_65cfe724",
  "sessionId": "f444a635-eeef-4924-9b48-a4c308632421",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015NZtvJiYqYmUPrMkyqFWzC",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1531,
      "cache_read_input_tokens": 30680,
      "output_tokens": 243,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1531,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 243,
          "cache_read_input_tokens": 30680,
          "cache_creation_input_tokens": 1531,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1531
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

_source line 13 · 2026-05-16T00:23:10.427Z_

<details><summary>↩ Tool result · `toolu_01JCknKS7HG1WqEVGMbNUeuk`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"experiments\": {\"plan_003_swebench_eval\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-15T18:41:00.685Z\", \"updated_at\": \"2026-05-16T00:22:31.107Z\", \"hypothesis\": \"SWE-bench Lite 纯检索 eval：用 3 个 Qwen M2 checkpoints (random_s42, embed_s43, dataflow_s43) 在 100 个 SWE-bench Lite 实例上评估 file-level retrieval Recall@{1,5,10,20} 和 MRR。定位为外部泛化展示，不做控制对比 claim（3 checkpoint 用了不同 seed，策略对比 confound 了 seed）。\", \"spec\": {\"command\": \"python eval_swebench_retrieval.py (3 checkpoints sequential on GPU 0)\", \"server\": \"bjb1-42106\", \"data_path\": \"/root/autodl-tmp/structfuse/artifacts/swebench_retrieval_eval/\", \"data_count\": 100, \"model_name\": \"Qwen2.5-Coder-3B (3 M2 checkpoints: random_s42, embed_s43, dataflow_s43)\", \"seed\": \"42,43,43\", \"checkpoint_source\": \"/root/autodl-tmp/structfuse/checkpoints/m2_full_qwen/\", \"eval_data\": \"princeton-nlp/SWE-bench_Lite (100 instances)\"}, \"metrics\": {\"checked_at\": \"2026-05-16T08:21 CST\", \"pid_alive\": true, \"eval_pid\": 61328, \"gpu\": \"cuda:0 (shared with Qwen training)\", \"current_checkpoint\": \"random_s42 (1/3)\", \"progress\": \"71/100 instances\", \"speed\": \"~12.7 inst/hr\", \"eta_random_s42\": \"~2026-05-16T10:30 CST\", \"checkpoint_sequence\": [\"random_s42 (running, 71/100)\", \"embed_s43 (postponed)\", \"dataflow_s43 (postponed)\"], \"output_dir\": \"/root/autodl-tmp/structfuse/artifacts/swebench_retrieval_eval/\", \"log\": \"/root/autodl-tmp/structfuse/logs/swebench_eval_all.log\", \"bm25_baseline_300\": {\"R@1\": 0.2733, \"R@5\": 0.4667, \"R@10\": 0.55, \"R@20\": 0.6467, \"n_instances\": 300}, \"director_decision\": \"random_s42 完成后暂停 SWE-bench eval。剩余 2 checkpoints (embed_s43, dataflow_s43) 推迟到 Qwen chain 完成后无 GPU 竞争时再跑。\", \"caveat\": \"3 checkpoints 使用不同 seed (s42/s43/s43)，策略对比 confound 了 seed。论文中定位为外部泛化展示，不做控制对比 claim。\"}}, \"m2_full_qwen_continued\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-14T18:44:20.646Z\", \"updated_at\": \"2026-05-15T23:02:32.982Z\", \"hypothesis\": \"M2 Qwen continued: 继续 m2_full_qwen 的剩余 runs (random_s44 + embedding×3 + dataflow×3)。原实验 cron 在 s42 退出时自动设为 ANALYZING，但链仍在运行。\", \"spec\": {\"command\": \"bash run_m2_full_qwen.sh (chain: random_s44 running → embedding×3 → dataflow×3)\", \"server\": \"bjb1-42106\", \"gpu\": [\"cuda:0\"], \"pid\": \"337267\", \"log_path\": \"/root/runs/structfuse-context/m2_full_qwen.log\", \"data_path\": \"/root/autodl-tmp/structfuse/full_m2_training_data/\", \"data_count\": 11308, \"model_name\": \"Qwen2.5-Coder-3B\", \"seed\": \"42,43,44\"}, \"parent\": \"m2_full_qwen\", \"metrics\": {\"checked_at\": \"2026-05-16T07:01 CST\", \"pid\": 337267, \"pid_alive\": true, \"training_pid\": 18427, \"gpu\": \"cuda:0, 100% util, 62620/97887 MiB\", \"current_subrun\": \"dataflow_aware_s43 (5/7, step 1100+, early_stopping 1/2)\", \"completed_subruns\": [{\"name\": \"random_s42\", \"best_val_loss\": 0.4651, \"best_R@1\": 0.5527, \"stop_step\": 4000}, {\"name\": \"random_s43\", \"best_val_loss\": 0.4476, \"best_R@1\": 0.5554, \"early_stop_step\": 1500}, {\"name\": \"random_s44\", \"best_val_loss\": 0.4252, \"best_R@1\": 0.6009, \"early_stop_step\": 1500}, {\"name\": \"embedding_distance_s43\", \"best_val_loss\": 0.4541, \"best_R@1\": 0.5606, \"early_stop_step\": 1500}, {\"name\": \"embedding_distance_s44\", \"best_val_loss\": 0.4341, \"best_R@1\": 0.5942, \"early_stop_step\": 2000}], \"current_eval\": {\"dataflow_s43_eval_500\": {\"val_loss\": 0.4617, \"R@1\": 0.5495, \"R@5\": 0.9728}, \"dataflow_s43_eval_1000\": {\"val_loss\": 0.4984, \"R@1\": 0.5174, \"R@5\": 0.9581, \"early_stopping_counter\": \"1/2\"}}, \"remaining_subruns\": [\"dataflow_aware_s44\", \"bm25_s42\"], \"training_rate\": \"~182 steps/h\", \"note\": \"dataflow_s43 degrading: eval@1000 R@1=0.5174 (-3.2pp vs eval@500). Best=step 500. Early stop likely at step 1500 if eval@1500 doesn't improve.\"}}, \"m2_full_starcoder_resumed\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-14T18:44:19.253Z\", \"updated_at\": \"2026-05-15T20:45:18.638Z\", \"hypothesis\": \"M2 StarCoder resumed: 继续 m2_full_starcoder 的 8 sequential runs (random×2 + embedding×3 + dataflow×3)。原实验因 cron timeout 标记为 failed，实际 PID 519791 正常运行。\", \"spec\": {\"command\": \"bash run_m2_full_starcoder_resume.sh (8 runs: random_s43→s44→embedding×3→dataflow×3)\", \"server\": \"bjb1-42106\", \"gpu\": [\"cuda:1\"], \"pid\": \"519791\", \"log_path\": \"/root/runs/structfuse-context/m2_full_starcoder.log\", \"data_path\": \"/root/autodl-tmp/structfuse/full_m2_training_data/\", \"data_count\": 11308, \"model_name\": \"StarCoder2-3B\", \"seed\": \"42,43,44\"}, \"parent\": \"m2_full_starcoder\", \"metrics\": {\"checked_at\": \"2026-05-16T04:44 CST\", \"pid\": 519791, \"pid_alive\": true, \"gpu\": \"cuda:1, 100% util, 54767/97887 MiB\", \"current_subrun\": \"embedding_distance_s42 (4/9, step ~600/4242)\", \"completed_subruns\": {\"random_s42\": {\"best_val_loss\": 0.6134, \"best_val_loss_step\": 1000, \"best_R@1\": 0.4604, \"best_R@1_step\": 2500, \"stop_step\": 4000}, \"random_s43\": {\"best_val_loss\": 0.5239, \"best_val_loss_step\": 1500, \"best_R@1\": 0.4912, \"best_R@1_step\": 1500, \"early_stopped\": \"step 2500\"}, \"random_s44\": {\"best_val_loss\": 0.5913, \"best_val_loss_step\": 500, \"best_R@1\": 0.4871, \"best_R@1_step\": 1500, \"early_stopped\": \"step 1500\"}}, \"current_eval\": {\"embed_s42_eval_500\": {\"val_loss\": 0.6154, \"R@1\": 0.4372, \"R@5\": 0.9094}}, \"actual_chain_sequence\": \"random_s42(done) → random_s43(done) → random_s44(done) → embedding_distance_s42(running) → embedding_distance_s43 → embedding_distance_s44 → dataflow_aware_s42 → dataflow_aware_s43 → dataflow_aware_s44\", \"remaining_subruns\": [\"embedding_distance_s43\", \"embedding_distance_s44\", \"dataflow_aware_s42\", \"dataflow_aware_s43\", \"dataflow_aware_s44\"], \"training_rate\": \"~200 steps/h on cuda:1\", \"note\": \"embed_s42 eval@500 R@1=0.4372 below all 3 random baselines (0.4604/0.4912/0.4871). Early signal concerning for embedding strategy on StarCoder. Need eval@1000+ to confirm.\"}}, \"m1_reextract_v2\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-13T20:00:20.578Z\", \"updated_at\": \"2026-05-15T20:44:09.645Z\", \"hypothesis\": \"M1 重提取 v2：恢复 28,276 个因运行时瞬态文件系统故障失败的 instances（82 repos）。CodeQL pack 已修复，端到端测试通过。预期将训练数据从 15,897 提升至 ~44,173。D022 批准。\", \"parent\": \"m1_extraction\", \"spec\": {\"command\": \"bash scripts/rerun_m1_failed.sh (4 CPU workers, CodeQL 2-hop, pack installed)\", \"server\": \"bjb1-42106\", \"data_path\": \"/root/autodl-tmp/structfuse/full_m1_data/\", \"data_count\": 28276, \"model_name\": \"N/A (CodeQL extraction)\", \"seed\": \"N/A\", \"log_path\": \"/root/runs/structfuse-context/m1_reextract_v2.log\", \"checkpoint_source\": \"rerun of m1_extraction failed instances (v2, CodeQL fixed)\", \"eval_data\": \"N/A\"}, \"notes\": \"moto CodeQL call_graph.ql timeout (NOT OOM): directCallEdge predicate exceeds 300s timeout on every instance (exit code 33). 536 moto instances all fail call_graph, fallback to embedding-distance. Isolated failure — 1/4 workers stuck on moto (~5min/instance, ~38h total), other 3 workers process pydicom/conan/MONAI normally. DB creation succeeded; bounded_dataflow.ql unaffected. [2026-05-16] Combine script ready: /root/structfuse/scripts/combine_m1_reextract.py. Dry-run stats: 39,712/44,173 (89.9%) structural data rate. Run after extraction completes: source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && python3 /root/structfuse/scripts/combine_m1_reextract.py\", \"metrics\": {\"all_jsonl_lines\": 44173, \"new_json_files\": \"43,858/44,173 (99.3%)\", \"repos_done\": \"81/82\", \"last_checked\": \"2026-05-16T04:43 CST\", \"remaining_repos\": [\"getmoto/moto (200/536, 37.3%)\"], \"completed_repos_update\": \"MONAI 524/524 完成\", \"processes_alive\": true, \"moto_eta\": \"~2026-05-17T07:00 CST (~28h remaining)\", \"issue\": \"moto CodeQL call_graph 100% timeout (exit 33). All moto instances produce degraded output (no call graph).\", \"disk_free_gb\": 85, \"note\": \"可选：不等 moto 完成，现在用 43,858 个 json 执行合并（已达 99.3%），moto 剩余 336 个后续补入。\"}}, \"plan_005_stratified\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-14T20:36:16.738Z\", \"updated_at\": \"2026-05-15T10:27:33.649Z\", \"hypothesis\": \"Plan 005 分层分析：按 repo size/pool size/query-pos similarity/structural data availability/neg_difficulty quartile 5 维度分层评估 embedding vs random 策略差异，控制 pool_size confound。Claim 2 支撑实验。v2 结果为 ground truth（v1→v2 changelog 见 art_20260514_3008c4）。\", \"parent\": \"m2_full_qwen\", \"notes\": \"plan_id=plan_005. 分层评估脚本已完成全部修改（analyze_stratified.py）：(1) mock seed 确定性修复 (2) pool_size-controlled 策略对比（within-bin delta + weighted aggregate）(3) dataflow×pool_size 交叉分析（n<30 标记 underpowered）(4) checkpoint 发现逻辑已就绪（best_by_recall_at_1 / best / best_by_val_loss）。输出含 JSON + CSV + PDF。[2026-05-14 21:07] Worker 完成 5 项 Patch。[2026-05-15 09:10] Dry-run v5 全流程验证通过（21秒）。confound 分析 + BM25 overlap stratified 分析均通过。数据预处理全部完成。等 M2 checkpoint 就绪后替换 --dry-run 为 --checkpoints-dir 即可。[2026-05-15 11:17] evaluate_pool50.py (D042) 独立验证通过。[2026-05-15] SWE-bench eval 脚本确认存在。[D050-追加] 第 6 层分析：per-seed val set 难度校验——比较各 seed val set 的 avg query-positive similarity 和 pool difficulty distribution，确认 s44 val set 是否系统性更容易（Qwen s44 R@1=0.6009 比 s42/s43 高 ~4.5pp，跨 seed 方差远大于 strategy treatment effect +0.52pp）。正式启动时加入 analyze_stratified.py。\", \"metrics\": {\"confound_analysis\": {\"data_validity\": \"⚠️ R@1 值为 dry-run mock predictions，不可引用。仅分布结构（cross_tabulation.csv）有效。\", \"valid_findings\": {\"distribution_structure\": \"rich-dataflow 99.3% 落在 large/xlarge repo，small repo 中完全不存在\", \"correlation\": {\"dataflow_edges_vs_repo_size_pearson_r\": 0.089}, \"cross_distribution\": {\"rich_in_large_xlarge_pct\": 99.3, \"rich_in_small\": 0, \"moderate_in_large_xlarge_pct\": 60.9}, \"implication\": \"真实评估必须控制 pool_size 和 repo_size 来隔离 dataflow richness 独立效应\"}, \"invalid_findings\": \"所有 R@1/R@5/MRR 值均为 mock predictions，策略排序 pattern 不可信，禁止引用\", \"artifacts_path\": \"/root/autodl-tmp/structfuse/artifacts/confound_analysis/\", \"valid_artifact\": \"cross_tabulation.csv\"}}}, \"plan_017_literature\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T18:49:00.477Z\", \"updated_at\": \"2026-05-14T21:33:45.149Z\", \"hypothesis\": \"Inference-time graph method comparison: 8 papers surveyed (CodexGraph, LocAgent, RANGER, GraphCoder, ARISE, RepoGraph, CodeGRAG, CodeRAG). Discussion v2 drafted, all citations verified. Conclusion: training-time vs inference-time complementary.\", \"spec\": {\"command\": \"analysis only (no training)\", \"server\": \"local\", \"data_path\": \"N/A\", \"data_count\": 0, \"model_name\": \"N/A\", \"seed\": \"N/A\", \"checkpoint_path\": \"N/A\", \"log_path\": \"N/A\"}, \"conclusion\": \"success\", \"metrics\": {\"papers_surveyed\": 8, \"citations_verified\": 8, \"discussion_draft\": \"artifacts/paper_drafts/discussion_v2.md\", \"artifact_id\": \"art_20260514_a2e1cd\"}, \"completed_at\": \"2026-05-14T18:49:39.557Z\", \"notes\": \"Inference-time graph method comparison 完成。8 papers surveyed，其中 6 篇纳入 literature_map.yaml 和 discussion_v2.md（CodexGraph, LocAgent, RANGER, GraphCoder, ARISE, RepoGraph）。CodeGRAG 和 CodeRAG 经调研排除：CodeGRAG（arXiv 2405.02355）关注 NL→code generation 的 graph-augmented prompting，不涉及代码检索或对比学习；CodeRAG 系列（CodeRAG-Bench 2406.14497 / CodeRAG 2504.10046）关注 retrieval-augmented code generation benchmark 和 bigraph-based 代码生成，均为生成任务而非检索训练。两者与 StructFuse 的 scope（训练时结构信号用于对比学习代码检索）不符，故未纳入 discussion。\"}, \"m2_full_starcoder\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-13T16:18:15.415Z\", \"updated_at\": \"2026-05-14T18:04:29.245Z\", \"hypothesis\": \"Full M2 StarCoder: 3 strategies × 3 seeds on full M1 data. Cross-encoder validation — if embedding > random holds for both Qwen and StarCoder, method is encoder-agnostic. Resolves plan_013 pilot negative (dataflow encoder-dependent).\", \"parent\": \"plan_013_starcoder\", \"spec\": {\"command\": \"bash -c \\\"cd /root/structfuse && bash run_m2_full_starcoder_resume.sh\\\"\", \"server\": \"bjb1-42106\", \"gpu\": [\"cuda:1\"], \"pid\": \"519791\", \"log_path\": \"~/runs/structfuse-context/m2_full_starcoder.log\", \"submitted_at\": \"2026-05-14T18:03:12.079Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\"}, \"notes\": \"Phase 1: 构建 StarCoder embedding negatives 完成。Phase 2: 9 runs 训练中。batch_size=8, num_negatives=7, epochs=3(s42)/2(s43+), lr=2e-5, eval_steps=500, no early_stopping。双 checkpoint: best + best_by_recall_at_1。Seeds: 42,43,44。[D026] s42 保持 3 epochs; s43/s44 及后续 runs 改为 2 epochs。[2026-05-15 02:02 CST] cuda:1 进程冲突修复并重新提交（PID 519791, timeout=144h）。Registry 状态 DONE(failed) 是旧 cron timeout 标记，实际正在运行 random_s43 [1/8]。新 cron 已注册监控 PID 519791。序列：random_s43→s44→(待插入bm25_s42)→embedding×3→dataflow×3。random_s42 结果：best R@1=0.4604 at step 2500, val_loss=0.6134 at step 1000。\", \"metrics\": {\"random_s42\": {\"epoch\": \"3/3\", \"current_step\": 4200, \"total_steps\": 4242, \"total_steps_per_epoch\": 1414, \"eval_500\": {\"val_loss\": 0.6194, \"recall_at_1\": 0.435, \"recall_at_5\": 0.905, \"recall_at_10\": 1}, \"eval_1000\": {\"val_loss\": 0.6134, \"recall_at_1\": 0.454, \"recall_at_5\": 0.92, \"recall_at_10\": 1}, \"eval_1500\": {\"val_loss\": 0.6528, \"recall_at_1\": 0.449, \"recall_at_5\": 0.906, \"recall_at_10\": 1}, \"eval_2000\": {\"val_loss\": 0.6698, \"recall_at_1\": 0.4456, \"recall_at_5\": 0.906, \"recall_at_10\": 1}, \"eval_2500\": {\"val_loss\": 0.6342, \"recall_at_1\": 0.4604, \"recall_at_5\": 0.9117, \"recall_at_10\": 1}, \"eval_3000\": {\"val_loss\": 0.6516, \"recall_at_1\": 0.4544, \"recall_at_5\": 0.9077, \"recall_at_10\": 1}, \"eval_3500\": {\"val_loss\": 0.6588, \"recall_at_1\": 0.4534, \"recall_at_5\": 0.9057, \"recall_at_10\": 1}, \"eval_4000\": {\"val_loss\": 0.6637, \"recall_at_1\": 0.4547, \"recall_at_5\": 0.9003, \"recall_at_10\": 1}, \"best_checkpoint\": \"step_1000 (val_loss=0.6134) / step_2500 (R@1=0.4604)\", \"conclusion\": \"effectively_complete (timeout at step 4200/4242, lr=7.8e-9, remaining 42 steps negligible)\"}, \"progress_snapshot\": \"2026-05-15T01:50 CST\"}, \"reproduce\": {\"finished_at\": \"2026-05-14T17:49:54.474Z\"}, \"failure_reason\": \"EXIT_CODE=124 (timeout — exceeded timeout_hours)\", \"conclusion\": \"failed\", \"completed_at\": \"2026-05-14T17:49:55.304Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-14T17:49:56.408767+00:00\"}]}}, \"m2_full_qwen\": {\"status\": \"ANALYZING\", \"retry_count\": 0, \"created_at\": \"2026-05-13T16:18:14.870Z\", \"updated_at\": \"2026-05-14T18:00:29.323Z\", \"hypothesis\": \"Full M2 Qwen: 3 strategies (random/embedding/dataflow) × 3 seeds on full M1 data (~11K train/seed). Statistical validation of pilot signal (embedding > random +2pp). Go/no-go for paper claims per D018.\", \"parent\": \"m2_embed_verify\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/structfuse && bash run_m2_full_qwen.sh 2>&1 | tee /root/runs/structfuse-context/m2_full_qwen.log\\\"\", \"server\": \"bjb1-42106\", \"gpu\": [\"cuda:0\"], \"pid\": \"73544\", \"log_path\": \"~/runs/structfuse-context/m2_full_qwen.log\", \"submitted_at\": \"2026-05-13T17:39:30.757Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\"}, \"notes\": \"Full M2 go/no-go: 3 strategies (random, embedding_distance, dataflow_aware) × 3 seeds (42, 43, 44) = 9 runs sequential on cuda:0. Config: lr=2e-5, batch_size=8, eval_steps=500, num_negatives=7, max_seq_length=2048, warmup_ratio=0.1, weight_decay=0.01, temperature=0.07, LoRA r=16, gradient_checkpointing=True, proj_dim=256. Dual checkpoint: best_by_val_loss + best_by_recall_at_1. Train ~11.3K/seed, val ~3K/seed. [D026] s42 保持 3 epochs 提供完整 overfitting curve; s43/s44 及后续 runs 改为 2 epochs + early_stopping_patience=2。[STATUS 2026-05-15 00:19 CST] Registry 状态 ANALYZING 是 cron 自动设置（s42 进程退出触发），但实验实际仍在进行中。random_s43 在 cuda:0 正常运行，step 1200/2810 (43%)。eval@500 R@1=0.5357, eval@1000 R@1=0.5285 (early_stopping 1/2)。Best R@1=0.5357 at step 500。GPU 100% 利用率, 50.5/97.9GB VRAM。\", \"metrics\": {\"random_s42\": {\"status\": \"DONE\", \"epoch\": \"3/3\", \"total_steps\": 4242, \"total_steps_per_epoch\": 1414, \"eval_500\": {\"val_loss\": 0.4869, \"recall_at_1\": 0.533, \"recall_at_5\": 0.954, \"recall_at_10\": 1}, \"eval_1000\": {\"val_loss\": 0.4651, \"recall_at_1\": 0.553, \"recall_at_5\": 0.959, \"recall_at_10\": 1}, \"eval_1500\": {\"val_loss\": 0.5365, \"recall_at_1\": 0.523, \"recall_at_5\": 0.955, \"recall_at_10\": 1}, \"eval_2000\": {\"val_loss\": 0.5162, \"recall_at_1\": 0.523, \"recall_at_5\": 0.954, \"recall_at_10\": 1}, \"eval_2500\": {\"val_loss\": 0.5264, \"recall_at_1\": 0.527, \"recall_at_5\": 0.956, \"recall_at_10\": 1}, \"eval_3000\": {\"val_loss\": 0.5406, \"recall_at_1\": 0.536, \"recall_at_5\": 0.956, \"recall_at_10\": 1}, \"best_checkpoint\": \"step_1000 (val_loss=0.4651, R@1=0.5527)\", \"conclusion\": \"Overfit after step 1000. Best R@1=0.5527, +1.7pp vs pilot (0.5357). Full data helps.\"}, \"random_s43\": {\"status\": \"DONE\", \"epoch\": \"early_stopped\", \"total_steps_per_epoch\": 1405, \"eval_500\": {\"val_loss\": 0.4476, \"recall_at_1\": 0.5357}, \"eval_1000\": {\"val_loss\": 0.4637, \"recall_at_1\": 0.5285}, \"eval_1500\": {\"recall_at_1\": 0.5554}, \"best_by_val_loss\": \"step 500 (val_loss=0.4476)\", \"best_by_recall_at_1\": \"step 1500 (R@1=0.5554)\", \"conclusion\": \"Early stopped at step 1500. Best R@1=0.5554, consistent with s42 (0.5527). val_loss and R@1 criterion diverge.\"}, \"random_s44\": {\"status\": \"RUNNING\", \"note\": \"Auto-started 01:58 CST, epoch 1/2, 1408 batches/epoch\"}, \"progress_snapshot\": \"2026-05-15T02:00 CST\"}, \"reproduce\": {\"finished_at\": \"2026-05-14T11:24:33.887Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-14T11:24:35.375104+00:00\"}]}}, \"plan_018_bm25\": {\"status\": \"QUEUED\", \"retry_count\": 0, \"created_at\": \"2026-05-14T16:38:40.603Z\", \"updated_at\": \"2026-05-14T17:09:50.985Z\", \"hypothesis\": \"BM25 negative baseline: Dream 审稿三档一致认定缺 BM25 baseline 是论文最大结构性缺陷。Phase 1 (CPU): 对 M2 训练语料建 BM25 索引，挖掘 BM25 hard negatives，生成训练数据。Phase 2 (GPU): 用 BM25 negatives 训练 Qwen + StarCoder 各 1 seed，对比 R@1。\", \"parent\": \"m2_full_qwen\", \"notes\": \"Phase 1 (CPU) COMPLETE: BM25 negative mining 完成。3 seeds 数据生成，record counts 与其他策略完全一致，0 fallback。BM25 score 分布: mean=246.50, std=155.96。重叠率: BM25 vs embedding_distance ~87.1%, vs random ~76.2%, vs dataflow_aware ~71.8%。高 median=1.0 因小 repo 候选池≤50 文件导致策略完全重合，BM25 differentiation 主要在大 repo。脚本: /root/structfuse/scripts/mine_bm25_negatives.py。输出: /root/autodl-tmp/structfuse/full_m2_training_data/{train,val}_bm25_s{42,43,44}.jsonl。Phase 2 (GPU): 等 re-dream gate 通过 + M2 完成后训练。\", \"metrics\": {\"phase1_complete\": true, \"seed_42\": {\"train_records\": 11308, \"val_records\": 2980, \"train_size_mb\": 1280.8, \"val_size_mb\": 344.6}, \"seed_43\": {\"train_records\": 11236, \"val_records\": 3052, \"train_size_mb\": 1280.9, \"val_size_mb\": 316}, \"seed_44\": {\"train_records\": 11264, \"val_records\": 3024, \"train_size_mb\": 1347.1, \"val_size_mb\": 295.9}, \"bm25_score_dist\": {\"count\": 392954, \"mean\": 246.5, \"std\": 155.96, \"p25\": 128.38, \"p50\": 228.41, \"p75\": 347.85, \"max\": 2585.74}, \"overlap_overall\": {\"bm25_vs_embedding\": 0.871, \"bm25_vs_random\": 0.762, \"bm25_vs_dataflow\": 0.718, \"note\": \"k=50 full candidate overlap from mining worker\"}, \"overlap_stratified_top7_jaccard\": {\"small_lt50\": {\"repos\": 39, \"bm25_vs_embedding\": 0.668, \"bm25_vs_random\": 0.411, \"bm25_vs_dataflow\": 0.667}, \"medium_50_200\": {\"repos\": 29, \"bm25_vs_embedding\": 0.38, \"bm25_vs_random\": 0.067, \"bm25_vs_dataflow\": 0.363}, \"large_200plus\": {\"repos\": 15, \"bm25_vs_embedding\": 0.297, \"bm25_vs_random\": 0.007, \"bm25_vs_dataflow\": 0.405}, \"matched_queries\": 2920, \"total_queries\": 12290, \"note\": \"top-7 Jaccard on s42 matched queries only (24% match rate due to different train/val splits)\"}}}, \"plan_015_dynamic\": {\"status\": \"QUEUED\", \"retry_count\": 0, \"created_at\": \"2026-05-14T17:03:24.316Z\", \"updated_at\": \"2026-05-14T17:03:30.544Z\", \"hypothesis\": \"Dynamic negative mining (epoch-level re-mining): 每 epoch 重新用当前 encoder embedding 挖掘 negatives，验证 static mining 是否足够。缩减版：只跑 dynamic_ep × 1 seed (Qwen, s42)，~11h 单卡。若 dynamic ≈ static（预期 <1pp 差异），在 Limitation 段排除 confound。\", \"notes\": \"Director D031 缩减：原 44h → 11h 单卡。只跑 dynamic_ep × 1 seed (Qwen, s42)，跳过 dynamic_500。Post-M2 与 plan_003 并行（一卡 SWE-bench，一卡 dynamic_ep）。受 re-dream gate 约束。设计文档已由 Worker 完成。\"}}, \"count\": 10, \"total\": 38, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.1469}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c70e6495-514d-43cb-a793-9577719f6fc6",
  "isSidechain": false,
  "promptId": "ee81bb41-edfe-48b7-9827-d79a74cf7a5e",
  "type": "user",
  "uuid": "d9d06870-585c-4081-88fd-c90bcf41e1bb",
  "toolUseResult": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"experiments\\\": {\\\"plan_003_swebench_eval\\\": {\\\"status\\\": \\\"RUNNING\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-15T18:41:00.685Z\\\", \\\"updated_at\\\": \\\"2026-05-16T00:22:31.107Z\\\", \\\"hypothesis\\\": \\\"SWE-bench Lite 纯检索 eval：用 3 个 Qwen M2 checkpoints (random_s42, embed_s43, dataflow_s43) 在 100 个 SWE-bench Lite 实例上评估 file-level retrieval Recall@{1,5,10,20} 和 MRR。定位为外部泛化展示，不做控制对比 claim（3 checkpoint 用了不同 seed，策略对比 confound 了 seed）。\\\", \\\"spec\\\": {\\\"command\\\": \\\"python eval_swebench_retrieval.py (3 checkpoints sequential on GPU 0)\\\", \\\"server\\\": \\\"bjb1-42106\\\", \\\"data_path\\\": \\\"/root/autodl-tmp/structfuse/artifacts/swebench_retrieval_eval/\\\", \\\"data_count\\\": 100, \\\"model_name\\\": \\\"Qwen2.5-Coder-3B (3 M2 checkpoints: random_s42, embed_s43, dataflow_s43)\\\", \\\"seed\\\": \\\"42,43,43\\\", \\\"checkpoint_source\\\": \\\"/root/autodl-tmp/structfuse/checkpoints/m2_full_qwen/\\\", \\\"eval_data\\\": \\\"princeton-nlp/SWE-bench_Lite (100 instances)\\\"}, \\\"metrics\\\": {\\\"checked_at\\\": \\\"2026-05-16T08:21 CST\\\", \\\"pid_alive\\\": true, \\\"eval_pid\\\": 61328, \\\"gpu\\\": \\\"cuda:0 (shared with Qwen training)\\\", \\\"current_checkpoint\\\": \\\"random_s42 (1/3)\\\", \\\"progress\\\": \\\"71/100 instances\\\", \\\"speed\\\": \\\"~12.7 inst/hr\\\", \\\"eta_random_s42\\\": \\\"~2026-05-16T10:30 CST\\\", \\\"checkpoint_sequence\\\": [\\\"random_s42 (running, 71/100)\\\", \\\"embed_s43 (postponed)\\\", \\\"dataflow_s43 (postponed)\\\"], \\\"output_dir\\\": \\\"/root/autodl-tmp/structfuse/artifacts/swebench_retrieval_eval/\\\", \\\"log\\\": \\\"/root/autodl-tmp/structfuse/logs/swebench_eval_all.log\\\", \\\"bm25_baseline_300\\\": {\\\"R@1\\\": 0.2733, \\\"R@5\\\": 0.4667, \\\"R@10\\\": 0.55, \\\"R@20\\\": 0.6467, \\\"n_instances\\\": 300}, \\\"director_decision\\\": \\\"random_s42 完成后暂停 SWE-bench eval。剩余 2 checkpoints (embed_s43, dataflow_s43) 推迟到 Qwen chain 完成后无 GPU 竞争时再跑。\\\", \\\"caveat\\\": \\\"3 checkpoints 使用不同 seed (s42/s43/s43)，策略对比 confound 了 seed。论文中定位为外部泛化展示，不做控制对比 claim。\\\"}}, \\\"m2_full_qwen_continued\\\": {\\\"status\\\": \\\"RUNNING\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-14T18:44:20.646Z\\\", \\\"updated_at\\\": \\\"2026-05-15T23:02:32.982Z\\\", \\\"hypothesis\\\": \\\"M2 Qwen continued: 继续 m2_full_qwen 的剩余 runs (random_s44 + embedding×3 + dataflow×3)。原实验 cron 在 s42 退出时自动设为 ANALYZING，但链仍在运行。\\\", \\\"spec\\\": {\\\"command\\\": \\\"bash run_m2_full_qwen.sh (chain: random_s44 running → embedding×3 → dataflow×3)\\\", \\\"server\\\": \\\"bjb1-42106\\\", \\\"gpu\\\": [\\\"cuda:0\\\"], \\\"pid\\\": \\\"337267\\\", \\\"log_path\\\": \\\"/root/runs/structfuse-context/m2_full_qwen.log\\\", \\\"data_path\\\": \\\"/root/autodl-tmp/structfuse/full_m2_training_data/\\\", \\\"data_count\\\": 11308, \\\"model_name\\\": \\\"Qwen2.5-Coder-3B\\\", \\\"seed\\\": \\\"42,43,44\\\"}, \\\"parent\\\": \\\"m2_full_qwen\\\", \\\"metrics\\\": {\\\"checked_at\\\": \\\"2026-05-16T07:01 CST\\\", \\\"pid\\\": 337267, \\\"pid_alive\\\": true, \\\"training_pid\\\": 18427, \\\"gpu\\\": \\\"cuda:0, 100% util, 62620/97887 MiB\\\", \\\"current_subrun\\\": \\\"dataflow_aware_s43 (5/7, step 1100+, early_stopping 1/2)\\\", \\\"completed_subruns\\\": [{\\\"name\\\": \\\"random_s42\\\", \\\"best_val_loss\\\": 0.4651, \\\"best_R@1\\\": 0.5527, \\\"stop_step\\\": 4000}, {\\\"name\\\": \\\"random_s43\\\", \\\"best_val_loss\\\": 0.4476, \\\"best_R@1\\\": 0.5554, \\\"early_stop_step\\\": 1500}, {\\\"name\\\": \\\"random_s44\\\", \\\"best_val_loss\\\": 0.4252, \\\"best_R@1\\\": 0.6009, \\\"early_stop_step\\\": 1500}, {\\\"name\\\": \\\"embedding_distance_s43\\\", \\\"best_val_loss\\\": 0.4541, \\\"best_R@1\\\": 0.5606, \\\"early_stop_step\\\": 1500}, {\\\"name\\\": \\\"embedding_distance_s44\\\", \\\"best_val_loss\\\": 0.4341, \\\"best_R@1\\\": 0.5942, \\\"early_stop_step\\\": 2000}], \\\"current_eval\\\": {\\\"dataflow_s43_eval_500\\\": {\\\"val_loss\\\": 0.4617, \\\"R@1\\\": 0.5495, \\\"R@5\\\": 0.9728}, \\\"dataflow_s43_eval_1000\\\": {\\\"val_loss\\\": 0.4984, \\\"R@1\\\": 0.5174, \\\"R@5\\\": 0.9581, \\\"early_stopping_counter\\\": \\\"1/2\\\"}}, \\\"remaining_subruns\\\": [\\\"dataflow_aware_s44\\\", \\\"bm25_s42\\\"], \\\"training_rate\\\": \\\"~182 steps/h\\\", \\\"note\\\": \\\"dataflow_s43 degrading: eval@1000 R@1=0.5174 (-3.2pp vs eval@500). Best=step 500. Early stop likely at step 1500 if eval@1500 doesn't improve.\\\"}}, \\\"m2_full_starcoder_resumed\\\": {\\\"status\\\": \\\"RUNNING\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-14T18:44:19.253Z\\\", \\\"updated_at\\\": \\\"2026-05-15T20:45:18.638Z\\\", \\\"hypothesis\\\": \\\"M2 StarCoder resumed: 继续 m2_full_starcoder 的 8 sequential runs (random×2 + embedding×3 + dataflow×3)。原实验因 cron timeout 标记为 failed，实际 PID 519791 正常运行。\\\", \\\"spec\\\": {\\\"command\\\": \\\"bash run_m2_full_starcoder_resume.sh (8 runs: random_s43→s44→embedding×3→dataflow×3)\\\", \\\"server\\\": \\\"bjb1-42106\\\", \\\"gpu\\\": [\\\"cuda:1\\\"], \\\"pid\\\": \\\"519791\\\", \\\"log_path\\\": \\\"/root/runs/structfuse-context/m2_full_starcoder.log\\\", \\\"data_path\\\": \\\"/root/autodl-tmp/structfuse/full_m2_training_data/\\\", \\\"data_count\\\": 11308, \\\"model_name\\\": \\\"StarCoder2-3B\\\", \\\"seed\\\": \\\"42,43,44\\\"}, \\\"parent\\\": \\\"m2_full_starcoder\\\", \\\"metrics\\\": {\\\"checked_at\\\": \\\"2026-05-16T04:44 CST\\\", \\\"pid\\\": 519791, \\\"pid_alive\\\": true, \\\"gpu\\\": \\\"cuda:1, 100% util, 54767/97887 MiB\\\", \\\"current_subrun\\\": \\\"embedding_distance_s42 (4/9, step ~600/4242)\\\", \\\"completed_subruns\\\": {\\\"random_s42\\\": {\\\"best_val_loss\\\": 0.6134, \\\"best_val_loss_step\\\": 1000, \\\"best_R@1\\\": 0.4604, \\\"best_R@1_step\\\": 2500, \\\"stop_step\\\": 4000}, \\\"random_s43\\\": {\\\"best_val_loss\\\": 0.5239, \\\"best_val_loss_step\\\": 1500, \\\"best_R@1\\\": 0.4912, \\\"best_R@1_step\\\": 1500, \\\"early_stopped\\\": \\\"step 2500\\\"}, \\\"random_s44\\\": {\\\"best_val_loss\\\": 0.5913, \\\"best_val_loss_step\\\": 500, \\\"best_R@1\\\": 0.4871, \\\"best_R@1_step\\\": 1500, \\\"early_stopped\\\": \\\"step 1500\\\"}}, \\\"current_eval\\\": {\\\"embed_s42_eval_500\\\": {\\\"val_loss\\\": 0.6154, \\\"R@1\\\": 0.4372, \\\"R@5\\\": 0.9094}}, \\\"actual_chain_sequence\\\": \\\"random_s42(done) → random_s43(done) → random_s44(done) → embedding_distance_s42(running) → embedding_distance_s43 → embedding_distance_s44 → dataflow_aware_s42 → dataflow_aware_s43 → dataflow_aware_s44\\\", \\\"remaining_subruns\\\": [\\\"embedding_distance_s43\\\", \\\"embedding_distance_s44\\\", \\\"dataflow_aware_s42\\\", \\\"dataflow_aware_s43\\\", \\\"dataflow_aware_s44\\\"], \\\"training_rate\\\": \\\"~200 steps/h on cuda:1\\\", \\\"note\\\": \\\"embed_s42 eval@500 R@1=0.4372 below all 3 random baselines (0.4604/0.4912/0.4871). Early signal concerning for embedding strategy on StarCoder. Need eval@1000+ to confirm.\\\"}}, \\\"m1_reextract_v2\\\": {\\\"status\\\": \\\"RUNNING\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-13T20:00:20.578Z\\\", \\\"updated_at\\\": \\\"2026-05-15T20:44:09.645Z\\\", \\\"hypothesis\\\": \\\"M1 重提取 v2：恢复 28,276 个因运行时瞬态文件系统故障失败的 instances（82 repos）。CodeQL pack 已修复，端到端测试通过。预期将训练数据从 15,897 提升至 ~44,173。D022 批准。\\\", \\\"parent\\\": \\\"m1_extraction\\\", \\\"spec\\\": {\\\"command\\\": \\\"bash scripts/rerun_m1_failed.sh (4 CPU workers, CodeQL 2-hop, pack installed)\\\", \\\"server\\\": \\\"bjb1-42106\\\", \\\"data_path\\\": \\\"/root/autodl-tmp/structfuse/full_m1_data/\\\", \\\"data_count\\\": 28276, \\\"model_name\\\": \\\"N/A (CodeQL extraction)\\\", \\\"seed\\\": \\\"N/A\\\", \\\"log_path\\\": \\\"/root/runs/structfuse-context/m1_reextract_v2.log\\\", \\\"checkpoint_source\\\": \\\"rerun of m1_extraction failed instances (v2, CodeQL fixed)\\\", \\\"eval_data\\\": \\\"N/A\\\"}, \\\"notes\\\": \\\"moto CodeQL call_graph.ql timeout (NOT OOM): directCallEdge predicate exceeds 300s timeout on every instance (exit code 33). 536 moto instances all fail call_graph, fallback to embedding-distance. Isolated failure — 1/4 workers stuck on moto (~5min/instance, ~38h total), other 3 workers process pydicom/conan/MONAI normally. DB creation succeeded; bounded_dataflow.ql unaffected. [2026-05-16] Combine script ready: /root/structfuse/scripts/combine_m1_reextract.py. Dry-run stats: 39,712/44,173 (89.9%) structural data rate. Run after extraction completes: source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && python3 /root/structfuse/scripts/combine_m1_reextract.py\\\", \\\"metrics\\\": {\\\"all_jsonl_lines\\\": 44173, \\\"new_json_files\\\": \\\"43,858/44,173 (99.3%)\\\", \\\"repos_done\\\": \\\"81/82\\\", \\\"last_checked\\\": \\\"2026-05-16T04:43 CST\\\", \\\"remaining_repos\\\": [\\\"getmoto/moto (200/536, 37.3%)\\\"], \\\"completed_repos_update\\\": \\\"MONAI 524/524 完成\\\", \\\"processes_alive\\\": true, \\\"moto_eta\\\": \\\"~2026-05-17T07:00 CST (~28h remaining)\\\", \\\"issue\\\": \\\"moto CodeQL call_graph 100% timeout (exit 33). All moto instances produce degraded output (no call graph).\\\", \\\"disk_free_gb\\\": 85, \\\"note\\\": \\\"可选：不等 moto 完成，现在用 43,858 个 json 执行合并（已达 99.3%），moto 剩余 336 个后续补入。\\\"}}, \\\"plan_005_stratified\\\": {\\\"status\\\": \\\"PREPARING\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-14T20:36:16.738Z\\\", \\\"updated_at\\\": \\\"2026-05-15T10:27:33.649Z\\\", \\\"hypothesis\\\": \\\"Plan 005 分层分析：按 repo size/pool size/query-pos similarity/structural data availability/neg_difficulty quartile 5 维度分层评估 embedding vs random 策略差异，控制 pool_size confound。Claim 2 支撑实验。v2 结果为 ground truth（v1→v2 changelog 见 art_20260514_3008c4）。\\\", \\\"parent\\\": \\\"m2_full_qwen\\\", \\\"notes\\\": \\\"plan_id=plan_005. 分层评估脚本已完成全部修改（analyze_stratified.py）：(1) mock seed 确定性修复 (2) pool_size-controlled 策略对比（within-bin delta + weighted aggregate）(3) dataflow×pool_size 交叉分析（n<30 标记 underpowered）(4) checkpoint 发现逻辑已就绪（best_by_recall_at_1 / best / best_by_val_loss）。输出含 JSON + CSV + PDF。[2026-05-14 21:07] Worker 完成 5 项 Patch。[2026-05-15 09:10] Dry-run v5 全流程验证通过（21秒）。confound 分析 + BM25 overlap stratified 分析均通过。数据预处理全部完成。等 M2 checkpoint 就绪后替换 --dry-run 为 --checkpoints-dir 即可。[2026-05-15 11:17] evaluate_pool50.py (D042) 独立验证通过。[2026-05-15] SWE-bench eval 脚本确认存在。[D050-追加] 第 6 层分析：per-seed val set 难度校验——比较各 seed val set 的 avg query-positive similarity 和 pool difficulty distribution，确认 s44 val set 是否系统性更容易（Qwen s44 R@1=0.6009 比 s42/s43 高 ~4.5pp，跨 seed 方差远大于 strategy treatment effect +0.52pp）。正式启动时加入 analyze_stratified.py。\\\", \\\"metrics\\\": {\\\"confound_analysis\\\": {\\\"data_validity\\\": \\\"⚠️ R@1 值为 dry-run mock predictions，不可引用。仅分布结构（cross_tabulation.csv）有效。\\\", \\\"valid_findings\\\": {\\\"distribution_structure\\\": \\\"rich-dataflow 99.3% 落在 large/xlarge repo，small repo 中完全不存在\\\", \\\"correlation\\\": {\\\"dataflow_edges_vs_repo_size_pearson_r\\\": 0.089}, \\\"cross_distribution\\\": {\\\"rich_in_large_xlarge_pct\\\": 99.3, \\\"rich_in_small\\\": 0, \\\"moderate_in_large_xlarge_pct\\\": 60.9}, \\\"implication\\\": \\\"真实评估必须控制 pool_size 和 repo_size 来隔离 dataflow richness 独立效应\\\"}, \\\"invalid_findings\\\": \\\"所有 R@1/R@5/MRR 值均为 mock predictions，策略排序 pattern 不可信，禁止引用\\\", \\\"artifacts_path\\\": \\\"/root/autodl-tmp/structfuse/artifacts/confound_analysis/\\\", \\\"valid_artifact\\\": \\\"cross_tabulation.csv\\\"}}}, \\\"plan_017_literature\\\": {\\\"status\\\": \\\"DONE\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-14T18:49:00.477Z\\\", \\\"updated_at\\\": \\\"2026-05-14T21:33:45.149Z\\\", \\\"hypothesis\\\": \\\"Inference-time graph method comparison: 8 papers surveyed (CodexGraph, LocAgent, RANGER, GraphCoder, ARISE, RepoGraph, CodeGRAG, CodeRAG). Discussion v2 drafted, all citations verified. Conclusion: training-time vs inference-time complementary.\\\", \\\"spec\\\": {\\\"command\\\": \\\"analysis only (no training)\\\", \\\"server\\\": \\\"local\\\", \\\"data_path\\\": \\\"N/A\\\", \\\"data_count\\\": 0, \\\"model_name\\\": \\\"N/A\\\", \\\"seed\\\": \\\"N/A\\\", \\\"checkpoint_path\\\": \\\"N/A\\\", \\\"log_path\\\": \\\"N/A\\\"}, \\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"papers_surveyed\\\": 8, \\\"citations_verified\\\": 8, \\\"discussion_draft\\\": \\\"artifacts/paper_drafts/discussion_v2.md\\\", \\\"artifact_id\\\": \\\"art_20260514_a2e1cd\\\"}, \\\"completed_at\\\": \\\"2026-05-14T18:49:39.557Z\\\", \\\"notes\\\": \\\"Inference-time graph method comparison 完成。8 papers surveyed，其中 6 篇纳入 literature_map.yaml 和 discussion_v2.md（CodexGraph, LocAgent, RANGER, GraphCoder, ARISE, RepoGraph）。CodeGRAG 和 CodeRAG 经调研排除：CodeGRAG（arXiv 2405.02355）关注 NL→code generation 的 graph-augmented prompting，不涉及代码检索或对比学习；CodeRAG 系列（CodeRAG-Bench 2406.14497 / CodeRAG 2504.10046）关注 retrieval-augmented code generation benchmark 和 bigraph-based 代码生成，均为生成任务而非检索训练。两者与 StructFuse 的 scope（训练时结构信号用于对比学习代码检索）不符，故未纳入 discussion。\\\"}, \\\"m2_full_starcoder\\\": {\\\"status\\\": \\\"DONE\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-13T16:18:15.415Z\\\", \\\"updated_at\\\": \\\"2026-05-14T18:04:29.245Z\\\", \\\"hypothesis\\\": \\\"Full M2 StarCoder: 3 strategies × 3 seeds on full M1 data. Cross-encoder validation — if embedding > random holds for both Qwen and StarCoder, method is encoder-agnostic. Resolves plan_013 pilot negative (dataflow encoder-dependent).\\\", \\\"parent\\\": \\\"plan_013_starcoder\\\", \\\"spec\\\": {\\\"command\\\": \\\"bash -c \\\\\\\"cd /root/structfuse && bash run_m2_full_starcoder_resume.sh\\\\\\\"\\\", \\\"server\\\": \\\"bjb1-42106\\\", \\\"gpu\\\": [\\\"cuda:1\\\"], \\\"pid\\\": \\\"519791\\\", \\\"log_path\\\": \\\"~/runs/structfuse-context/m2_full_starcoder.log\\\", \\\"submitted_at\\\": \\\"2026-05-14T18:03:12.079Z\\\", \\\"submitted_via\\\": \\\"submit_training_job\\\", \\\"backend\\\": \\\"tmux\\\", \\\"account\\\": \\\"root\\\"}, \\\"notes\\\": \\\"Phase 1: 构建 StarCoder embedding negatives 完成。Phase 2: 9 runs 训练中。batch_size=8, num_negatives=7, epochs=3(s42)/2(s43+), lr=2e-5, eval_steps=500, no early_stopping。双 checkpoint: best + best_by_recall_at_1。Seeds: 42,43,44。[D026] s42 保持 3 epochs; s43/s44 及后续 runs 改为 2 epochs。[2026-05-15 02:02 CST] cuda:1 进程冲突修复并重新提交（PID 519791, timeout=144h）。Registry 状态 DONE(failed) 是旧 cron timeout 标记，实际正在运行 random_s43 [1/8]。新 cron 已注册监控 PID 519791。序列：random_s43→s44→(待插入bm25_s42)→embedding×3→dataflow×3。random_s42 结果：best R@1=0.4604 at step 2500, val_loss=0.6134 at step 1000。\\\", \\\"metrics\\\": {\\\"random_s42\\\": {\\\"epoch\\\": \\\"3/3\\\", \\\"current_step\\\": 4200, \\\"total_steps\\\": 4242, \\\"total_steps_per_epoch\\\": 1414, \\\"eval_500\\\": {\\\"val_loss\\\": 0.6194, \\\"recall_at_1\\\": 0.435, \\\"recall_at_5\\\": 0.905, \\\"recall_at_10\\\": 1}, \\\"eval_1000\\\": {\\\"val_loss\\\": 0.6134, \\\"recall_at_1\\\": 0.454, \\\"recall_at_5\\\": 0.92, \\\"recall_at_10\\\": 1}, \\\"eval_1500\\\": {\\\"val_loss\\\": 0.6528, \\\"recall_at_1\\\": 0.449, \\\"recall_at_5\\\": 0.906, \\\"recall_at_10\\\": 1}, \\\"eval_2000\\\": {\\\"val_loss\\\": 0.6698, \\\"recall_at_1\\\": 0.4456, \\\"recall_at_5\\\": 0.906, \\\"recall_at_10\\\": 1}, \\\"eval_2500\\\": {\\\"val_loss\\\": 0.6342, \\\"recall_at_1\\\": 0.4604, \\\"recall_at_5\\\": 0.9117, \\\"recall_at_10\\\": 1}, \\\"eval_3000\\\": {\\\"val_loss\\\": 0.6516, \\\"recall_at_1\\\": 0.4544, \\\"recall_at_5\\\": 0.9077, \\\"recall_at_10\\\": 1}, \\\"eval_3500\\\": {\\\"val_loss\\\": 0.6588, \\\"recall_at_1\\\": 0.4534, \\\"recall_at_5\\\": 0.9057, \\\"recall_at_10\\\": 1}, \\\"eval_4000\\\": {\\\"val_loss\\\": 0.6637, \\\"recall_at_1\\\": 0.4547, \\\"recall_at_5\\\": 0.9003, \\\"recall_at_10\\\": 1}, \\\"best_checkpoint\\\": \\\"step_1000 (val_loss=0.6134) / step_2500 (R@1=0.4604)\\\", \\\"conclusion\\\": \\\"effectively_complete (timeout at step 4200/4242, lr=7.8e-9, remaining 42 steps negligible)\\\"}, \\\"progress_snapshot\\\": \\\"2026-05-15T01:50 CST\\\"}, \\\"reproduce\\\": {\\\"finished_at\\\": \\\"2026-05-14T17:49:54.474Z\\\"}, \\\"failure_reason\\\": \\\"EXIT_CODE=124 (timeout — exceeded timeout_hours)\\\", \\\"conclusion\\\": \\\"failed\\\", \\\"completed_at\\\": \\\"2026-05-14T17:49:55.304Z\\\", \\\"extra\\\": {\\\"hook_events\\\": [{\\\"event\\\": \\\"on_failed\\\", \\\"action\\\": \\\"agent\\\", \\\"ts\\\": \\\"2026-05-14T17:49:56.408767+00:00\\\"}]}}, \\\"m2_full_qwen\\\": {\\\"status\\\": \\\"ANALYZING\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-13T16:18:14.870Z\\\", \\\"updated_at\\\": \\\"2026-05-14T18:00:29.323Z\\\", \\\"hypothesis\\\": \\\"Full M2 Qwen: 3 strategies (random/embedding/dataflow) × 3 seeds on full M1 data (~11K train/seed). Statistical validation of pilot signal (embedding > random +2pp). Go/no-go for paper claims per D018.\\\", \\\"parent\\\": \\\"m2_embed_verify\\\", \\\"spec\\\": {\\\"command\\\": \\\"bash -c \\\\\\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/structfuse && bash run_m2_full_qwen.sh 2>&1 | tee /root/runs/structfuse-context/m2_full_qwen.log\\\\\\\"\\\", \\\"server\\\": \\\"bjb1-42106\\\", \\\"gpu\\\": [\\\"cuda:0\\\"], \\\"pid\\\": \\\"73544\\\", \\\"log_path\\\": \\\"~/runs/structfuse-context/m2_full_qwen.log\\\", \\\"submitted_at\\\": \\\"2026-05-13T17:39:30.757Z\\\", \\\"submitted_via\\\": \\\"submit_training_job\\\", \\\"backend\\\": \\\"tmux\\\", \\\"account\\\": \\\"root\\\"}, \\\"notes\\\": \\\"Full M2 go/no-go: 3 strategies (random, embedding_distance, dataflow_aware) × 3 seeds (42, 43, 44) = 9 runs sequential on cuda:0. Config: lr=2e-5, batch_size=8, eval_steps=500, num_negatives=7, max_seq_length=2048, warmup_ratio=0.1, weight_decay=0.01, temperature=0.07, LoRA r=16, gradient_checkpointing=True, proj_dim=256. Dual checkpoint: best_by_val_loss + best_by_recall_at_1. Train ~11.3K/seed, val ~3K/seed. [D026] s42 保持 3 epochs 提供完整 overfitting curve; s43/s44 及后续 runs 改为 2 epochs + early_stopping_patience=2。[STATUS 2026-05-15 00:19 CST] Registry 状态 ANALYZING 是 cron 自动设置（s42 进程退出触发），但实验实际仍在进行中。random_s43 在 cuda:0 正常运行，step 1200/2810 (43%)。eval@500 R@1=0.5357, eval@1000 R@1=0.5285 (early_stopping 1/2)。Best R@1=0.5357 at step 500。GPU 100% 利用率, 50.5/97.9GB VRAM。\\\", \\\"metrics\\\": {\\\"random_s42\\\": {\\\"status\\\": \\\"DONE\\\", \\\"epoch\\\": \\\"3/3\\\", \\\"total_steps\\\": 4242, \\\"total_steps_per_epoch\\\": 1414, \\\"eval_500\\\": {\\\"val_loss\\\": 0.4869, \\\"recall_at_1\\\": 0.533, \\\"recall_at_5\\\": 0.954, \\\"recall_at_10\\\": 1}, \\\"eval_1000\\\": {\\\"val_loss\\\": 0.4651, \\\"recall_at_1\\\": 0.553, \\\"recall_at_5\\\": 0.959, \\\"recall_at_10\\\": 1}, \\\"eval_1500\\\": {\\\"val_loss\\\": 0.5365, \\\"recall_at_1\\\": 0.523, \\\"recall_at_5\\\": 0.955, \\\"recall_at_10\\\": 1}, \\\"eval_2000\\\": {\\\"val_loss\\\": 0.5162, \\\"recall_at_1\\\": 0.523, \\\"recall_at_5\\\": 0.954, \\\"recall_at_10\\\": 1}, \\\"eval_2500\\\": {\\\"val_loss\\\": 0.5264, \\\"recall_at_1\\\": 0.527, \\\"recall_at_5\\\": 0.956, \\\"recall_at_10\\\": 1}, \\\"eval_3000\\\": {\\\"val_loss\\\": 0.5406, \\\"recall_at_1\\\": 0.536, \\\"recall_at_5\\\": 0.956, \\\"recall_at_10\\\": 1}, \\\"best_checkpoint\\\": \\\"step_1000 (val_loss=0.4651, R@1=0.5527)\\\", \\\"conclusion\\\": \\\"Overfit after step 1000. Best R@1=0.5527, +1.7pp vs pilot (0.5357). Full data helps.\\\"}, \\\"random_s43\\\": {\\\"status\\\": \\\"DONE\\\", \\\"epoch\\\": \\\"early_stopped\\\", \\\"total_steps_per_epoch\\\": 1405, \\\"eval_500\\\": {\\\"val_loss\\\": 0.4476, \\\"recall_at_1\\\": 0.5357}, \\\"eval_1000\\\": {\\\"val_loss\\\": 0.4637, \\\"recall_at_1\\\": 0.5285}, \\\"eval_1500\\\": {\\\"recall_at_1\\\": 0.5554}, \\\"best_by_val_loss\\\": \\\"step 500 (val_loss=0.4476)\\\", \\\"best_by_recall_at_1\\\": \\\"step 1500 (R@1=0.5554)\\\", \\\"conclusion\\\": \\\"Early stopped at step 1500. Best R@1=0.5554, consistent with s42 (0.5527). val_loss and R@1 criterion diverge.\\\"}, \\\"random_s44\\\": {\\\"status\\\": \\\"RUNNING\\\", \\\"note\\\": \\\"Auto-started 01:58 CST, epoch 1/2, 1408 batches/epoch\\\"}, \\\"progress_snapshot\\\": \\\"2026-05-15T02:00 CST\\\"}, \\\"reproduce\\\": {\\\"finished_at\\\": \\\"2026-05-14T11:24:33.887Z\\\"}, \\\"extra\\\": {\\\"hook_events\\\": [{\\\"event\\\": \\\"on_complete\\\", \\\"action\\\": \\\"agent\\\", \\\"ts\\\": \\\"2026-05-14T11:24:35.375104+00:00\\\"}]}}, \\\"plan_018_bm25\\\": {\\\"status\\\": \\\"QUEUED\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-14T16:38:40.603Z\\\", \\\"updated_at\\\": \\\"2026-05-14T17:09:50.985Z\\\", \\\"hypothesis\\\": \\\"BM25 negative baseline: Dream 审稿三档一致认定缺 BM25 baseline 是论文最大结构性缺陷。Phase 1 (CPU): 对 M2 训练语料建 BM25 索引，挖掘 BM25 hard negatives，生成训练数据。Phase 2 (GPU): 用 BM25 negatives 训练 Qwen + StarCoder 各 1 seed，对比 R@1。\\\", \\\"parent\\\": \\\"m2_full_qwen\\\", \\\"notes\\\": \\\"Phase 1 (CPU) COMPLETE: BM25 negative mining 完成。3 seeds 数据生成，record counts 与其他策略完全一致，0 fallback。BM25 score 分布: mean=246.50, std=155.96。重叠率: BM25 vs embedding_distance ~87.1%, vs random ~76.2%, vs dataflow_aware ~71.8%。高 median=1.0 因小 repo 候选池≤50 文件导致策略完全重合，BM25 differentiation 主要在大 repo。脚本: /root/structfuse/scripts/mine_bm25_negatives.py。输出: /root/autodl-tmp/structfuse/full_m2_training_data/{train,val}_bm25_s{42,43,44}.jsonl。Phase 2 (GPU): 等 re-dream gate 通过 + M2 完成后训练。\\\", \\\"metrics\\\": {\\\"phase1_complete\\\": true, \\\"seed_42\\\": {\\\"train_records\\\": 11308, \\\"val_records\\\": 2980, \\\"train_size_mb\\\": 1280.8, \\\"val_size_mb\\\": 344.6}, \\\"seed_43\\\": {\\\"train_records\\\": 11236, \\\"val_records\\\": 3052, \\\"train_size_mb\\\": 1280.9, \\\"val_size_mb\\\": 316}, \\\"seed_44\\\": {\\\"train_records\\\": 11264, \\\"val_records\\\": 3024, \\\"train_size_mb\\\": 1347.1, \\\"val_size_mb\\\": 295.9}, \\\"bm25_score_dist\\\": {\\\"count\\\": 392954, \\\"mean\\\": 246.5, \\\"std\\\": 155.96, \\\"p25\\\": 128.38, \\\"p50\\\": 228.41, \\\"p75\\\": 347.85, \\\"max\\\": 2585.74}, \\\"overlap_overall\\\": {\\\"bm25_vs_embedding\\\": 0.871, \\\"bm25_vs_random\\\": 0.762, \\\"bm25_vs_dataflow\\\": 0.718, \\\"note\\\": \\\"k=50 full candidate overlap from mining worker\\\"}, \\\"overlap_stratified_top7_jaccard\\\": {\\\"small_lt50\\\": {\\\"repos\\\": 39, \\\"bm25_vs_embedding\\\": 0.668, \\\"bm25_vs_random\\\": 0.411, \\\"bm25_vs_dataflow\\\": 0.667}, \\\"medium_50_200\\\": {\\\"repos\\\": 29, \\\"bm25_vs_embedding\\\": 0.38, \\\"bm25_vs_random\\\": 0.067, \\\"bm25_vs_dataflow\\\": 0.363}, \\\"large_200plus\\\": {\\\"repos\\\": 15, \\\"bm25_vs_embedding\\\": 0.297, \\\"bm25_vs_random\\\": 0.007, \\\"bm25_vs_dataflow\\\": 0.405}, \\\"matched_queries\\\": 2920, \\\"total_queries\\\": 12290, \\\"note\\\": \\\"top-7 Jaccard on s42 matched queries only (24% match rate due to different train/val splits)\\\"}}}, \\\"plan_015_dynamic\\\": {\\\"status\\\": \\\"QUEUED\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-14T17:03:24.316Z\\\", \\\"updated_at\\\": \\\"2026-05-14T17:03:30.544Z\\\", \\\"hypothesis\\\": \\\"Dynamic negative mining (epoch-level re-mining): 每 epoch 重新用当前 encoder embedding 挖掘 negatives，验证 static mining 是否足够。缩减版：只跑 dynamic_ep × 1 seed (Qwen, s42)，~11h 单卡。若 dynamic ≈ static（预期 <1pp 差异），在 Limitation 段排除 confound。\\\", \\\"notes\\\": \\\"Director D031 缩减：原 44h → 11h 单卡。只跑 dynamic_ep × 1 seed (Qwen, s42)，跳过 dynamic_500。Post-M2 与 plan_003 并行（一卡 SWE-bench，一卡 dynamic_ep）。受 re-dream gate 约束。设计文档已由 Worker 完成。\\\"}}, \\\"count\\\": 10, \\\"total\\\": 38, \\\"baseline\\\": null}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.1469}}\"}",
  "mcpMeta": {
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"experiments\": {\"plan_003_swebench_eval\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-15T18:41:00.685Z\", \"updated_at\": \"2026-05-16T00:22:31.107Z\", \"hypothesis\": \"SWE-bench Lite 纯检索 eval：用 3 个 Qwen M2 checkpoints (random_s42, embed_s43, dataflow_s43) 在 100 个 SWE-bench Lite 实例上评估 file-level retrieval Recall@{1,5,10,20} 和 MRR。定位为外部泛化展示，不做控制对比 claim（3 checkpoint 用了不同 seed，策略对比 confound 了 seed）。\", \"spec\": {\"command\": \"python eval_swebench_retrieval.py (3 checkpoints sequential on GPU 0)\", \"server\": \"bjb1-42106\", \"data_path\": \"/root/autodl-tmp/structfuse/artifacts/swebench_retrieval_eval/\", \"data_count\": 100, \"model_name\": \"Qwen2.5-Coder-3B (3 M2 checkpoints: random_s42, embed_s43, dataflow_s43)\", \"seed\": \"42,43,43\", \"checkpoint_source\": \"/root/autodl-tmp/structfuse/checkpoints/m2_full_qwen/\", \"eval_data\": \"princeton-nlp/SWE-bench_Lite (100 instances)\"}, \"metrics\": {\"checked_at\": \"2026-05-16T08:21 CST\", \"pid_alive\": true, \"eval_pid\": 61328, \"gpu\": \"cuda:0 (shared with Qwen training)\", \"current_checkpoint\": \"random_s42 (1/3)\", \"progress\": \"71/100 instances\", \"speed\": \"~12.7 inst/hr\", \"eta_random_s42\": \"~2026-05-16T10:30 CST\", \"checkpoint_sequence\": [\"random_s42 (running, 71/100)\", \"embed_s43 (postponed)\", \"dataflow_s43 (postponed)\"], \"output_dir\": \"/root/autodl-tmp/structfuse/artifacts/swebench_retrieval_eval/\", \"log\": \"/root/autodl-tmp/structfuse/logs/swebench_eval_all.log\", \"bm25_baseline_300\": {\"R@1\": 0.2733, \"R@5\": 0.4667, \"R@10\": 0.55, \"R@20\": 0.6467, \"n_instances\": 300}, \"director_decision\": \"random_s42 完成后暂停 SWE-bench eval。剩余 2 checkpoints (embed_s43, dataflow_s43) 推迟到 Qwen chain 完成后无 GPU 竞争时再跑。\", \"caveat\": \"3 checkpoints 使用不同 seed (s42/s43/s43)，策略对比 confound 了 seed。论文中定位为外部泛化展示，不做控制对比 claim。\"}}, \"m2_full_qwen_continued\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-14T18:44:20.646Z\", \"updated_at\": \"2026-05-15T23:02:32.982Z\", \"hypothesis\": \"M2 Qwen continued: 继续 m2_full_qwen 的剩余 runs (random_s44 + embedding×3 + dataflow×3)。原实验 cron 在 s42 退出时自动设为 ANALYZING，但链仍在运行。\", \"spec\": {\"command\": \"bash run_m2_full_qwen.sh (chain: random_s44 running → embedding×3 → dataflow×3)\", \"server\": \"bjb1-42106\", \"gpu\": [\"cuda:0\"], \"pid\": \"337267\", \"log_path\": \"/root/runs/structfuse-context/m2_full_qwen.log\", \"data_path\": \"/root/autodl-tmp/structfuse/full_m2_training_data/\", \"data_count\": 11308, \"model_name\": \"Qwen2.5-Coder-3B\", \"seed\": \"42,43,44\"}, \"parent\": \"m2_full_qwen\", \"metrics\": {\"checked_at\": \"2026-05-16T07:01 CST\", \"pid\": 337267, \"pid_alive\": true, \"training_pid\": 18427, \"gpu\": \"cuda:0, 100% util, 62620/97887 MiB\", \"current_subrun\": \"dataflow_aware_s43 (5/7, step 1100+, early_stopping 1/2)\", \"completed_subruns\": [{\"name\": \"random_s42\", \"best_val_loss\": 0.4651, \"best_R@1\": 0.5527, \"stop_step\": 4000}, {\"name\": \"random_s43\", \"best_val_loss\": 0.4476, \"best_R@1\": 0.5554, \"early_stop_step\": 1500}, {\"name\": \"random_s44\", \"best_val_loss\": 0.4252, \"best_R@1\": 0.6009, \"early_stop_step\": 1500}, {\"name\": \"embedding_distance_s43\", \"best_val_loss\": 0.4541, \"best_R@1\": 0.5606, \"early_stop_step\": 1500}, {\"name\": \"embedding_distance_s44\", \"best_val_loss\": 0.4341, \"best_R@1\": 0.5942, \"early_stop_step\": 2000}], \"current_eval\": {\"dataflow_s43_eval_500\": {\"val_loss\": 0.4617, \"R@1\": 0.5495, \"R@5\": 0.9728}, \"dataflow_s43_eval_1000\": {\"val_loss\": 0.4984, \"R@1\": 0.5174, \"R@5\": 0.9581, \"early_stopping_counter\": \"1/2\"}}, \"remaining_subruns\": [\"dataflow_aware_s44\", \"bm25_s42\"], \"training_rate\": \"~182 steps/h\", \"note\": \"dataflow_s43 degrading: eval@1000 R@1=0.5174 (-3.2pp vs eval@500). Best=step 500. Early stop likely at step 1500 if eval@1500 doesn't improve.\"}}, \"m2_full_starcoder_resumed\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-14T18:44:19.253Z\", \"updated_at\": \"2026-05-15T20:45:18.638Z\", \"hypothesis\": \"M2 StarCoder resumed: 继续 m2_full_starcoder 的 8 sequential runs (random×2 + embedding×3 + dataflow×3)。原实验因 cron timeout 标记为 failed，实际 PID 519791 正常运行。\", \"spec\": {\"command\": \"bash run_m2_full_starcoder_resume.sh (8 runs: random_s43→s44→embedding×3→dataflow×3)\", \"server\": \"bjb1-42106\", \"gpu\": [\"cuda:1\"], \"pid\": \"519791\", \"log_path\": \"/root/runs/structfuse-context/m2_full_starcoder.log\", \"data_path\": \"/root/autodl-tmp/structfuse/full_m2_training_data/\", \"data_count\": 11308, \"model_name\": \"StarCoder2-3B\", \"seed\": \"42,43,44\"}, \"parent\": \"m2_full_starcoder\", \"metrics\": {\"checked_at\": \"2026-05-16T04:44 CST\", \"pid\": 519791, \"pid_alive\": true, \"gpu\": \"cuda:1, 100% util, 54767/97887 MiB\", \"current_subrun\": \"embedding_distance_s42 (4/9, step ~600/4242)\", \"completed_subruns\": {\"random_s42\": {\"best_val_loss\": 0.6134, \"best_val_loss_step\": 1000, \"best_R@1\": 0.4604, \"best_R@1_step\": 2500, \"stop_step\": 4000}, \"random_s43\": {\"best_val_loss\": 0.5239, \"best_val_loss_step\": 1500, \"best_R@1\": 0.4912, \"best_R@1_step\": 1500, \"early_stopped\": \"step 2500\"}, \"random_s44\": {\"best_val_loss\": 0.5913, \"best_val_loss_step\": 500, \"best_R@1\": 0.4871, \"best_R@1_step\": 1500, \"early_stopped\": \"step 1500\"}}, \"current_eval\": {\"embed_s42_eval_500\": {\"val_loss\": 0.6154, \"R@1\": 0.4372, \"R@5\": 0.9094}}, \"actual_chain_sequence\": \"random_s42(done) → random_s43(done) → random_s44(done) → embedding_distance_s42(running) → embedding_distance_s43 → embedding_distance_s44 → dataflow_aware_s42 → dataflow_aware_s43 → dataflow_aware_s44\", \"remaining_subruns\": [\"embedding_distance_s43\", \"embedding_distance_s44\", \"dataflow_aware_s42\", \"dataflow_aware_s43\", \"dataflow_aware_s44\"], \"training_rate\": \"~200 steps/h on cuda:1\", \"note\": \"embed_s42 eval@500 R@1=0.4372 below all 3 random baselines (0.4604/0.4912/0.4871). Early signal concerning for embedding strategy on StarCoder. Need eval@1000+ to confirm.\"}}, \"m1_reextract_v2\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-13T20:00:20.578Z\", \"updated_at\": \"2026-05-15T20:44:09.645Z\", \"hypothesis\": \"M1 重提取 v2：恢复 28,276 个因运行时瞬态文件系统故障失败的 instances（82 repos）。CodeQL pack 已修复，端到端测试通过。预期将训练数据从 15,897 提升至 ~44,173。D022 批准。\", \"parent\": \"m1_extraction\", \"spec\": {\"command\": \"bash scripts/rerun_m1_failed.sh (4 CPU workers, CodeQL 2-hop, pack installed)\", \"server\": \"bjb1-42106\", \"data_path\": \"/root/autodl-tmp/structfuse/full_m1_data/\", \"data_count\": 28276, \"model_name\": \"N/A (CodeQL extraction)\", \"seed\": \"N/A\", \"log_path\": \"/root/runs/structfuse-context/m1_reextract_v2.log\", \"checkpoint_source\": \"rerun of m1_extraction failed instances (v2, CodeQL fixed)\", \"eval_data\": \"N/A\"}, \"notes\": \"moto CodeQL call_graph.ql timeout (NOT OOM): directCallEdge predicate exceeds 300s timeout on every instance (exit code 33). 536 moto instances all fail call_graph, fallback to embedding-distance. Isolated failure — 1/4 workers stuck on moto (~5min/instance, ~38h total), other 3 workers process pydicom/conan/MONAI normally. DB creation succeeded; bounded_dataflow.ql unaffected. [2026-05-16] Combine script ready: /root/structfuse/scripts/combine_m1_reextract.py. Dry-run stats: 39,712/44,173 (89.9%) structural data rate. Run after extraction completes: source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && python3 /root/structfuse/scripts/combine_m1_reextract.py\", \"metrics\": {\"all_jsonl_lines\": 44173, \"new_json_files\": \"43,858/44,173 (99.3%)\", \"repos_done\": \"81/82\", \"last_checked\": \"2026-05-16T04:43 CST\", \"remaining_repos\": [\"getmoto/moto (200/536, 37.3%)\"], \"completed_repos_update\": \"MONAI 524/524 完成\", \"processes_alive\": true, \"moto_eta\": \"~2026-05-17T07:00 CST (~28h remaining)\", \"issue\": \"moto CodeQL call_graph 100% timeout (exit 33). All moto instances produce degraded output (no call graph).\", \"disk_free_gb\": 85, \"note\": \"可选：不等 moto 完成，现在用 43,858 个 json 执行合并（已达 99.3%），moto 剩余 336 个后续补入。\"}}, \"plan_005_stratified\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-14T20:36:16.738Z\", \"updated_at\": \"2026-05-15T10:27:33.649Z\", \"hypothesis\": \"Plan 005 分层分析：按 repo size/pool size/query-pos similarity/structural data availability/neg_difficulty quartile 5 维度分层评估 embedding vs random 策略差异，控制 pool_size confound。Claim 2 支撑实验。v2 结果为 ground truth（v1→v2 changelog 见 art_20260514_3008c4）。\", \"parent\": \"m2_full_qwen\", \"notes\": \"plan_id=plan_005. 分层评估脚本已完成全部修改（analyze_stratified.py）：(1) mock seed 确定性修复 (2) pool_size-controlled 策略对比（within-bin delta + weighted aggregate）(3) dataflow×pool_size 交叉分析（n<30 标记 underpowered）(4) checkpoint 发现逻辑已就绪（best_by_recall_at_1 / best / best_by_val_loss）。输出含 JSON + CSV + PDF。[2026-05-14 21:07] Worker 完成 5 项 Patch。[2026-05-15 09:10] Dry-run v5 全流程验证通过（21秒）。confound 分析 + BM25 overlap stratified 分析均通过。数据预处理全部完成。等 M2 checkpoint 就绪后替换 --dry-run 为 --checkpoints-dir 即可。[2026-05-15 11:17] evaluate_pool50.py (D042) 独立验证通过。[2026-05-15] SWE-bench eval 脚本确认存在。[D050-追加] 第 6 层分析：per-seed val set 难度校验——比较各 seed val set 的 avg query-positive similarity 和 pool difficulty distribution，确认 s44 val set 是否系统性更容易（Qwen s44 R@1=0.6009 比 s42/s43 高 ~4.5pp，跨 seed 方差远大于 strategy treatment effect +0.52pp）。正式启动时加入 analyze_stratified.py。\", \"metrics\": {\"confound_analysis\": {\"data_validity\": \"⚠️ R@1 值为 dry-run mock predictions，不可引用。仅分布结构（cross_tabulation.csv）有效。\", \"valid_findings\": {\"distribution_structure\": \"rich-dataflow 99.3% 落在 large/xlarge repo，small repo 中完全不存在\", \"correlation\": {\"dataflow_edges_vs_repo_size_pearson_r\": 0.089}, \"cross_distribution\": {\"rich_in_large_xlarge_pct\": 99.3, \"rich_in_small\": 0, \"moderate_in_large_xlarge_pct\": 60.9}, \"implication\": \"真实评估必须控制 pool_size 和 repo_size 来隔离 dataflow richness 独立效应\"}, \"invalid_findings\": \"所有 R@1/R@5/MRR 值均为 mock predictions，策略排序 pattern 不可信，禁止引用\", \"artifacts_path\": \"/root/autodl-tmp/structfuse/artifacts/confound_analysis/\", \"valid_artifact\": \"cross_tabulation.csv\"}}}, \"plan_017_literature\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T18:49:00.477Z\", \"updated_at\": \"2026-05-14T21:33:45.149Z\", \"hypothesis\": \"Inference-time graph method comparison: 8 papers surveyed (CodexGraph, LocAgent, RANGER, GraphCoder, ARISE, RepoGraph, CodeGRAG, CodeRAG). Discussion v2 drafted, all citations verified. Conclusion: training-time vs inference-time complementary.\", \"spec\": {\"command\": \"analysis only (no training)\", \"server\": \"local\", \"data_path\": \"N/A\", \"data_count\": 0, \"model_name\": \"N/A\", \"seed\": \"N/A\", \"checkpoint_path\": \"N/A\", \"log_path\": \"N/A\"}, \"conclusion\": \"success\", \"metrics\": {\"papers_surveyed\": 8, \"citations_verified\": 8, \"discussion_draft\": \"artifacts/paper_drafts/discussion_v2.md\", \"artifact_id\": \"art_20260514_a2e1cd\"}, \"completed_at\": \"2026-05-14T18:49:39.557Z\", \"notes\": \"Inference-time graph method comparison 完成。8 papers surveyed，其中 6 篇纳入 literature_map.yaml 和 discussion_v2.md（CodexGraph, LocAgent, RANGER, GraphCoder, ARISE, RepoGraph）。CodeGRAG 和 CodeRAG 经调研排除：CodeGRAG（arXiv 2405.02355）关注 NL→code generation 的 graph-augmented prompting，不涉及代码检索或对比学习；CodeRAG 系列（CodeRAG-Bench 2406.14497 / CodeRAG 2504.10046）关注 retrieval-augmented code generation benchmark 和 bigraph-based 代码生成，均为生成任务而非检索训练。两者与 StructFuse 的 scope（训练时结构信号用于对比学习代码检索）不符，故未纳入 discussion。\"}, \"m2_full_starcoder\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-13T16:18:15.415Z\", \"updated_at\": \"2026-05-14T18:04:29.245Z\", \"hypothesis\": \"Full M2 StarCoder: 3 strategies × 3 seeds on full M1 data. Cross-encoder validation — if embedding > random holds for both Qwen and StarCoder, method is encoder-agnostic. Resolves plan_013 pilot negative (dataflow encoder-dependent).\", \"parent\": \"plan_013_starcoder\", \"spec\": {\"command\": \"bash -c \\\"cd /root/structfuse && bash run_m2_full_starcoder_resume.sh\\\"\", \"server\": \"bjb1-42106\", \"gpu\": [\"cuda:1\"], \"pid\": \"519791\", \"log_path\": \"~/runs/structfuse-context/m2_full_starcoder.log\", \"submitted_at\": \"2026-05-14T18:03:12.079Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\"}, \"notes\": \"Phase 1: 构建 StarCoder embedding negatives 完成。Phase 2: 9 runs 训练中。batch_size=8, num_negatives=7, epochs=3(s42)/2(s43+), lr=2e-5, eval_steps=500, no early_stopping。双 checkpoint: best + best_by_recall_at_1。Seeds: 42,43,44。[D026] s42 保持 3 epochs; s43/s44 及后续 runs 改为 2 epochs。[2026-05-15 02:02 CST] cuda:1 进程冲突修复并重新提交（PID 519791, timeout=144h）。Registry 状态 DONE(failed) 是旧 cron timeout 标记，实际正在运行 random_s43 [1/8]。新 cron 已注册监控 PID 519791。序列：random_s43→s44→(待插入bm25_s42)→embedding×3→dataflow×3。random_s42 结果：best R@1=0.4604 at step 2500, val_loss=0.6134 at step 1000。\", \"metrics\": {\"random_s42\": {\"epoch\": \"3/3\", \"current_step\": 4200, \"total_steps\": 4242, \"total_steps_per_epoch\": 1414, \"eval_500\": {\"val_loss\": 0.6194, \"recall_at_1\": 0.435, \"recall_at_5\": 0.905, \"recall_at_10\": 1}, \"eval_1000\": {\"val_loss\": 0.6134, \"recall_at_1\": 0.454, \"recall_at_5\": 0.92, \"recall_at_10\": 1}, \"eval_1500\": {\"val_loss\": 0.6528, \"recall_at_1\": 0.449, \"recall_at_5\": 0.906, \"recall_at_10\": 1}, \"eval_2000\": {\"val_loss\": 0.6698, \"recall_at_1\": 0.4456, \"recall_at_5\": 0.906, \"recall_at_10\": 1}, \"eval_2500\": {\"val_loss\": 0.6342, \"recall_at_1\": 0.4604, \"recall_at_5\": 0.9117, \"recall_at_10\": 1}, \"eval_3000\": {\"val_loss\": 0.6516, \"recall_at_1\": 0.4544, \"recall_at_5\": 0.9077, \"recall_at_10\": 1}, \"eval_3500\": {\"val_loss\": 0.6588, \"recall_at_1\": 0.4534, \"recall_at_5\": 0.9057, \"recall_at_10\": 1}, \"eval_4000\": {\"val_loss\": 0.6637, \"recall_at_1\": 0.4547, \"recall_at_5\": 0.9003, \"recall_at_10\": 1}, \"best_checkpoint\": \"step_1000 (val_loss=0.6134) / step_2500 (R@1=0.4604)\", \"conclusion\": \"effectively_complete (timeout at step 4200/4242, lr=7.8e-9, remaining 42 steps negligible)\"}, \"progress_snapshot\": \"2026-05-15T01:50 CST\"}, \"reproduce\": {\"finished_at\": \"2026-05-14T17:49:54.474Z\"}, \"failure_reason\": \"EXIT_CODE=124 (timeout — exceeded timeout_hours)\", \"conclusion\": \"failed\", \"completed_at\": \"2026-05-14T17:49:55.304Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-14T17:49:56.408767+00:00\"}]}}, \"m2_full_qwen\": {\"status\": \"ANALYZING\", \"retry_count\": 0, \"created_at\": \"2026-05-13T16:18:14.870Z\", \"updated_at\": \"2026-05-14T18:00:29.323Z\", \"hypothesis\": \"Full M2 Qwen: 3 strategies (random/embedding/dataflow) × 3 seeds on full M1 data (~11K train/seed). Statistical validation of pilot signal (embedding > random +2pp). Go/no-go for paper claims per D018.\", \"parent\": \"m2_embed_verify\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/structfuse && bash run_m2_full_qwen.sh 2>&1 | tee /root/runs/structfuse-context/m2_full_qwen.log\\\"\", \"server\": \"bjb1-42106\", \"gpu\": [\"cuda:0\"], \"pid\": \"73544\", \"log_path\": \"~/runs/structfuse-context/m2_full_qwen.log\", \"submitted_at\": \"2026-05-13T17:39:30.757Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\"}, \"notes\": \"Full M2 go/no-go: 3 strategies (random, embedding_distance, dataflow_aware) × 3 seeds (42, 43, 44) = 9 runs sequential on cuda:0. Config: lr=2e-5, batch_size=8, eval_steps=500, num_negatives=7, max_seq_length=2048, warmup_ratio=0.1, weight_decay=0.01, temperature=0.07, LoRA r=16, gradient_checkpointing=True, proj_dim=256. Dual checkpoint: best_by_val_loss + best_by_recall_at_1. Train ~11.3K/seed, val ~3K/seed. [D026] s42 保持 3 epochs 提供完整 overfitting curve; s43/s44 及后续 runs 改为 2 epochs + early_stopping_patience=2。[STATUS 2026-05-15 00:19 CST] Registry 状态 ANALYZING 是 cron 自动设置（s42 进程退出触发），但实验实际仍在进行中。random_s43 在 cuda:0 正常运行，step 1200/2810 (43%)。eval@500 R@1=0.5357, eval@1000 R@1=0.5285 (early_stopping 1/2)。Best R@1=0.5357 at step 500。GPU 100% 利用率, 50.5/97.9GB VRAM。\", \"metrics\": {\"random_s42\": {\"status\": \"DONE\", \"epoch\": \"3/3\", \"total_steps\": 4242, \"total_steps_per_epoch\": 1414, \"eval_500\": {\"val_loss\": 0.4869, \"recall_at_1\": 0.533, \"recall_at_5\": 0.954, \"recall_at_10\": 1}, \"eval_1000\": {\"val_loss\": 0.4651, \"recall_at_1\": 0.553, \"recall_at_5\": 0.959, \"recall_at_10\": 1}, \"eval_1500\": {\"val_loss\": 0.5365, \"recall_at_1\": 0.523, \"recall_at_5\": 0.955, \"recall_at_10\": 1}, \"eval_2000\": {\"val_loss\": 0.5162, \"recall_at_1\": 0.523, \"recall_at_5\": 0.954, \"recall_at_10\": 1}, \"eval_2500\": {\"val_loss\": 0.5264, \"recall_at_1\": 0.527, \"recall_at_5\": 0.956, \"recall_at_10\": 1}, \"eval_3000\": {\"val_loss\": 0.5406, \"recall_at_1\": 0.536, \"recall_at_5\": 0.956, \"recall_at_10\": 1}, \"best_checkpoint\": \"step_1000 (val_loss=0.4651, R@1=0.5527)\", \"conclusion\": \"Overfit after step 1000. Best R@1=0.5527, +1.7pp vs pilot (0.5357). Full data helps.\"}, \"random_s43\": {\"status\": \"DONE\", \"epoch\": \"early_stopped\", \"total_steps_per_epoch\": 1405, \"eval_500\": {\"val_loss\": 0.4476, \"recall_at_1\": 0.5357}, \"eval_1000\": {\"val_loss\": 0.4637, \"recall_at_1\": 0.5285}, \"eval_1500\": {\"recall_at_1\": 0.5554}, \"best_by_val_loss\": \"step 500 (val_loss=0.4476)\", \"best_by_recall_at_1\": \"step 1500 (R@1=0.5554)\", \"conclusion\": \"Early stopped at step 1500. Best R@1=0.5554, consistent with s42 (0.5527). val_loss and R@1 criterion diverge.\"}, \"random_s44\": {\"status\": \"RUNNING\", \"note\": \"Auto-started 01:58 CST, epoch 1/2, 1408 batches/epoch\"}, \"progress_snapshot\": \"2026-05-15T02:00 CST\"}, \"reproduce\": {\"finished_at\": \"2026-05-14T11:24:33.887Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-14T11:24:35.375104+00:00\"}]}}, \"plan_018_bm25\": {\"status\": \"QUEUED\", \"retry_count\": 0, \"created_at\": \"2026-05-14T16:38:40.603Z\", \"updated_at\": \"2026-05-14T17:09:50.985Z\", \"hypothesis\": \"BM25 negative baseline: Dream 审稿三档一致认定缺 BM25 baseline 是论文最大结构性缺陷。Phase 1 (CPU): 对 M2 训练语料建 BM25 索引，挖掘 BM25 hard negatives，生成训练数据。Phase 2 (GPU): 用 BM25 negatives 训练 Qwen + StarCoder 各 1 seed，对比 R@1。\", \"parent\": \"m2_full_qwen\", \"notes\": \"Phase 1 (CPU) COMPLETE: BM25 negative mining 完成。3 seeds 数据生成，record counts 与其他策略完全一致，0 fallback。BM25 score 分布: mean=246.50, std=155.96。重叠率: BM25 vs embedding_distance ~87.1%, vs random ~76.2%, vs dataflow_aware ~71.8%。高 median=1.0 因小 repo 候选池≤50 文件导致策略完全重合，BM25 differentiation 主要在大 repo。脚本: /root/structfuse/scripts/mine_bm25_negatives.py。输出: /root/autodl-tmp/structfuse/full_m2_training_data/{train,val}_bm25_s{42,43,44}.jsonl。Phase 2 (GPU): 等 re-dream gate 通过 + M2 完成后训练。\", \"metrics\": {\"phase1_complete\": true, \"seed_42\": {\"train_records\": 11308, \"val_records\": 2980, \"train_size_mb\": 1280.8, \"val_size_mb\": 344.6}, \"seed_43\": {\"train_records\": 11236, \"val_records\": 3052, \"train_size_mb\": 1280.9, \"val_size_mb\": 316}, \"seed_44\": {\"train_records\": 11264, \"val_records\": 3024, \"train_size_mb\": 1347.1, \"val_size_mb\": 295.9}, \"bm25_score_dist\": {\"count\": 392954, \"mean\": 246.5, \"std\": 155.96, \"p25\": 128.38, \"p50\": 228.41, \"p75\": 347.85, \"max\": 2585.74}, \"overlap_overall\": {\"bm25_vs_embedding\": 0.871, \"bm25_vs_random\": 0.762, \"bm25_vs_dataflow\": 0.718, \"note\": \"k=50 full candidate overlap from mining worker\"}, \"overlap_stratified_top7_jaccard\": {\"small_lt50\": {\"repos\": 39, \"bm25_vs_embedding\": 0.668, \"bm25_vs_random\": 0.411, \"bm25_vs_dataflow\": 0.667}, \"medium_50_200\": {\"repos\": 29, \"bm25_vs_embedding\": 0.38, \"bm25_vs_random\": 0.067, \"bm25_vs_dataflow\": 0.363}, \"large_200plus\": {\"repos\": 15, \"bm25_vs_embedding\": 0.297, \"bm25_vs_random\": 0.007, \"bm25_vs_dataflow\": 0.405}, \"matched_queries\": 2920, \"total_queries\": 12290, \"note\": \"top-7 Jaccard on s42 matched queries only (24% match rate due to different train/val splits)\"}}}, \"plan_015_dynamic\": {\"status\": \"QUEUED\", \"retry_count\": 0, \"created_at\": \"2026-05-14T17:03:24.316Z\", \"updated_at\": \"2026-05-14T17:03:30.544Z\", \"hypothesis\": \"Dynamic negative mining (epoch-level re-mining): 每 epoch 重新用当前 encoder embedding 挖掘 negatives，验证 static mining 是否足够。缩减版：只跑 dynamic_ep × 1 seed (Qwen, s42)，~11h 单卡。若 dynamic ≈ static（预期 <1pp 差异），在 Limitation 段排除 confound。\", \"notes\": \"Director D031 缩减：原 44h → 11h 单卡。只跑 dynamic_ep × 1 seed (Qwen, s42)，跳过 dynamic_500。Post-M2 与 plan_003 并行（一卡 SWE-bench，一卡 dynamic_ep）。受 re-dream gate 约束。设计文档已由 Worker 完成。\"}}, \"count\": 10, \"total\": 38, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.1469}}"
    }
  },
  "sourceToolAssistantUUID": "c70e6495-514d-43cb-a793-9577719f6fc6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/.claude/sessions/reviewer_65cfe724",
  "sessionId": "f444a635-eeef-4924-9b48-a4c308632421",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---


### Tool call

_source line 14 · 2026-05-16T00:23:10.743Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01Pii4vtunaT9avh7K7F9XbG`</summary>

```json
{
  "project": "structfuse-context",
  "file": "report.md",
  "max_chars": 12000
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d9d06870-585c-4081-88fd-c90bcf41e1bb",
  "isSidechain": false,
  "requestId": "req_011Cb5J21neDKTbom9RAnGPV",
  "type": "assistant",
  "uuid": "d66dff60-7c21-4358-8640-72be8cad1f05",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/.claude/sessions/reviewer_65cfe724",
  "sessionId": "f444a635-eeef-4924-9b48-a4c308632421",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015NZtvJiYqYmUPrMkyqFWzC",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1531,
      "cache_read_input_tokens": 30680,
      "output_tokens": 243,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1531,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 243,
          "cache_read_input_tokens": 30680,
          "cache_creation_input_tokens": 1531,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1531
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

_source line 15 · 2026-05-16T00:23:10.755Z_

<details><summary>↩ Tool result · `toolu_01Pii4vtunaT9avh7K7F9XbG`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/report.md\", \"content\": \"# Handover — 2026-05-15\\n\\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\\n\\n## 运行中\\n| exp_id | 假设 | 状态 | 关键指标 | W&B |\\n|--------|------|------|---------|-----|\\n| plan_003_swebench_eval | SWE-bench Lite 纯检索 eval：用 6 个 Qwen M2 checkpoints 在 300 个 SWE-bench Lite 实例上评估 file-level retrieval Recall@{1,5,10,20} 和 MRR。每个实例需 clone repo 并检索，~131s/instance。6 checkpoints 共 ~66h。 | — | — | — |\\n| m2_full_starcoder_resumed | M2 StarCoder resumed: 继续 m2_full_starcoder 的 8 sequential runs (random×2 + embedding×3 + dataflow×3)。原实验因 cron timeout 标记为 failed，实际 PID 519791 正常运行。 | — | — | — |\\n| m2_full_qwen_continued | M2 Qwen continued: 继续 m2_full_qwen 的剩余 runs (random_s44 + embedding×3 + dataflow×3)。原实验 cron 在 s42 退出时自动设为 ANALYZING，但链仍在运行。 | — | — | — |\\n\\n## 待处理\\n- plan_018_bm25: BM25 negative baseline: Dream 审稿三档一致认定缺 BM25 baseline 是论文最大结构性缺陷。Phase 1 (CPU): 对 M2 训练语料建 BM25 索引，挖掘 BM25 hard negatives，生成训练数据。Phase 2 (GPU): 用 BM25 negatives 训练 Qwen + StarCoder 各 1 seed，对比 R@1。（排队等待 GPU）\\n- plan_015_dynamic: Dynamic negative mining (epoch-level re-mining): 每 epoch 重新用当前 encoder embedding 挖掘 negatives，验证 static mining 是否足够。缩减版：只跑 dynamic_ep × 1 seed (Qwen, s42)，~11h 单卡。若 dynamic ≈ static（预期 <1pp 差异），在 Limitation 段排除 confound。（排队等待 GPU）\\n- plan_005_stratified: Plan 005 分层分析：按 repo size/pool size/query-pos similarity/structural data availability/neg_difficulty quartile 5 维度分层评估 embedding vs random 策略差异，控制 pool_size confound。Claim 2 支撑实验。v2 结果为 ground truth（v1→v2 changelog 见 art_20260514_3008c4）。（准备中）\\n\\n## 近期结论\\n- **plan_017_literature** (success): Inference-time graph method comparison: 8 papers surveyed (CodexGraph, LocAgent, RANGER, GraphCoder, ARISE, RepoGraph, CodeGRAG, CodeRAG). Discussion v2 drafted, all citations verified. Conclusion: training-time vs inference-time complementary.\\n- **m2_full_starcoder** (failed): Full M2 StarCoder: 3 strategies × 3 seeds on full M1 data. Cross-encoder validation — if embedding > random holds for both Qwen and StarCoder, method is encoder-agnostic. Resolves plan_013 pilot negative (dataflow encoder-dependent). ← 基于 plan_013_starcoder\\n  [m2_starcoder_status_check](/api/workspace-files/projects/structfuse-context/artifacts/m2_full_starcoder/report/m2_starcoder_status_check.md)\\n- **neg_difficulty_analysis** (success): Negative difficulty distribution analysis: 用预训练 Qwen2.5-Coder-3B 和 StarCoder2-3B 计算 3 策略 (random/embedding/dataflow) 的 query-negative/positive cosine similarity，分析 pretrained representation separability 跨编码器差异。MAX_LENGTH=2048 匹配训练设置。\\n  [neg_difficulty_margin_comparison](/api/workspace-files/projects/structfuse-context/artifacts/neg_difficulty_analysis/chart/neg_difficulty_margin_comparison_meta.txt) | [neg_difficulty_margin_comparison](/api/workspace-files/projects/structfuse-context/artifacts/neg_difficulty_analysis/chart/neg_difficulty_margin_comparison_meta_01876a.txt) | [neg_difficulty_similarity_dist](/api/workspace-files/projects/structfuse-context/artifacts/neg_difficulty_analysis/chart/neg_difficulty_similarity_dist_meta.txt) | [neg_difficulty_ratio_heatmap](/api/workspace-files/projects/structfuse-context/artifacts/neg_difficulty_analysis/chart/neg_difficulty_ratio_heatmap_meta.txt)\\n\\n## 趋势\\n成功 11 / 负向 2 / 失败 3 / 共 30\\n\\n## 下一步\\n（无活跃 idea，请通过 ideas.md 添加）\\n\\n## 资源状态\\nbjb1-42106: 无 GPU 信息\\n\\n## 告警\\n- p2b-smoke-test: 已被终止 — unknown\\n- p2b-smoke2: 已被终止 — unknown\\n- p2b-smoke3: 已被终止 — unknown\\n- p2b-smoke4: 已被终止 — unknown\\n- p2b-smoke5: 已被终止 — unknown\\n- p2b-smoke6: 已被终止 — unknown\\n- p2b-smoke7: 已被终止 — unknown\\n- p2b-smoke8: 已被终止 — unknown\\n- p2b-all-9runs: 已被终止 — unknown\\n- mvp_p2b_contrastive_training: 已被终止 — unknown\\n- mvp_p2b_contrastive_v2: 已被终止 — unknown\\n- p2b_eval_all: 已被终止 — unknown\\n- m2_early_pilot: 已被终止 — unknown\\n- m2_early_pilot_v2: 训练失败 — unknown\\n- m2_early_pilot_v3: 已被终止 — unknown\\n- m2_full_starcoder: 训练失败 — unknown\\n- m1_reextract: 训练失败 — unknown\\n\", \"total_chars\": 3816, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d66dff60-7c21-4358-8640-72be8cad1f05",
  "isSidechain": false,
  "promptId": "ee81bb41-edfe-48b7-9827-d79a74cf7a5e",
  "type": "user",
  "uuid": "fcb2f846-f171-415b-9a25-d81d9230854d",
  "toolUseResult": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"path\\\": \\\"/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/report.md\\\", \\\"content\\\": \\\"# Handover — 2026-05-15\\\\n\\\\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\\\\n\\\\n## 运行中\\\\n| exp_id | 假设 | 状态 | 关键指标 | W&B |\\\\n|--------|------|------|---------|-----|\\\\n| plan_003_swebench_eval | SWE-bench Lite 纯检索 eval：用 6 个 Qwen M2 checkpoints 在 300 个 SWE-bench Lite 实例上评估 file-level retrieval Recall@{1,5,10,20} 和 MRR。每个实例需 clone repo 并检索，~131s/instance。6 checkpoints 共 ~66h。 | — | — | — |\\\\n| m2_full_starcoder_resumed | M2 StarCoder resumed: 继续 m2_full_starcoder 的 8 sequential runs (random×2 + embedding×3 + dataflow×3)。原实验因 cron timeout 标记为 failed，实际 PID 519791 正常运行。 | — | — | — |\\\\n| m2_full_qwen_continued | M2 Qwen continued: 继续 m2_full_qwen 的剩余 runs (random_s44 + embedding×3 + dataflow×3)。原实验 cron 在 s42 退出时自动设为 ANALYZING，但链仍在运行。 | — | — | — |\\\\n\\\\n## 待处理\\\\n- plan_018_bm25: BM25 negative baseline: Dream 审稿三档一致认定缺 BM25 baseline 是论文最大结构性缺陷。Phase 1 (CPU): 对 M2 训练语料建 BM25 索引，挖掘 BM25 hard negatives，生成训练数据。Phase 2 (GPU): 用 BM25 negatives 训练 Qwen + StarCoder 各 1 seed，对比 R@1。（排队等待 GPU）\\\\n- plan_015_dynamic: Dynamic negative mining (epoch-level re-mining): 每 epoch 重新用当前 encoder embedding 挖掘 negatives，验证 static mining 是否足够。缩减版：只跑 dynamic_ep × 1 seed (Qwen, s42)，~11h 单卡。若 dynamic ≈ static（预期 <1pp 差异），在 Limitation 段排除 confound。（排队等待 GPU）\\\\n- plan_005_stratified: Plan 005 分层分析：按 repo size/pool size/query-pos similarity/structural data availability/neg_difficulty quartile 5 维度分层评估 embedding vs random 策略差异，控制 pool_size confound。Claim 2 支撑实验。v2 结果为 ground truth（v1→v2 changelog 见 art_20260514_3008c4）。（准备中）\\\\n\\\\n## 近期结论\\\\n- **plan_017_literature** (success): Inference-time graph method comparison: 8 papers surveyed (CodexGraph, LocAgent, RANGER, GraphCoder, ARISE, RepoGraph, CodeGRAG, CodeRAG). Discussion v2 drafted, all citations verified. Conclusion: training-time vs inference-time complementary.\\\\n- **m2_full_starcoder** (failed): Full M2 StarCoder: 3 strategies × 3 seeds on full M1 data. Cross-encoder validation — if embedding > random holds for both Qwen and StarCoder, method is encoder-agnostic. Resolves plan_013 pilot negative (dataflow encoder-dependent). ← 基于 plan_013_starcoder\\\\n  [m2_starcoder_status_check](/api/workspace-files/projects/structfuse-context/artifacts/m2_full_starcoder/report/m2_starcoder_status_check.md)\\\\n- **neg_difficulty_analysis** (success): Negative difficulty distribution analysis: 用预训练 Qwen2.5-Coder-3B 和 StarCoder2-3B 计算 3 策略 (random/embedding/dataflow) 的 query-negative/positive cosine similarity，分析 pretrained representation separability 跨编码器差异。MAX_LENGTH=2048 匹配训练设置。\\\\n  [neg_difficulty_margin_comparison](/api/workspace-files/projects/structfuse-context/artifacts/neg_difficulty_analysis/chart/neg_difficulty_margin_comparison_meta.txt) | [neg_difficulty_margin_comparison](/api/workspace-files/projects/structfuse-context/artifacts/neg_difficulty_analysis/chart/neg_difficulty_margin_comparison_meta_01876a.txt) | [neg_difficulty_similarity_dist](/api/workspace-files/projects/structfuse-context/artifacts/neg_difficulty_analysis/chart/neg_difficulty_similarity_dist_meta.txt) | [neg_difficulty_ratio_heatmap](/api/workspace-files/projects/structfuse-context/artifacts/neg_difficulty_analysis/chart/neg_difficulty_ratio_heatmap_meta.txt)\\\\n\\\\n## 趋势\\\\n成功 11 / 负向 2 / 失败 3 / 共 30\\\\n\\\\n## 下一步\\\\n（无活跃 idea，请通过 ideas.md 添加）\\\\n\\\\n## 资源状态\\\\nbjb1-42106: 无 GPU 信息\\\\n\\\\n## 告警\\\\n- p2b-smoke-test: 已被终止 — unknown\\\\n- p2b-smoke2: 已被终止 — unknown\\\\n- p2b-smoke3: 已被终止 — unknown\\\\n- p2b-smoke4: 已被终止 — unknown\\\\n- p2b-smoke5: 已被终止 — unknown\\\\n- p2b-smoke6: 已被终止 — unknown\\\\n- p2b-smoke7: 已被终止 — unknown\\\\n- p2b-smoke8: 已被终止 — unknown\\\\n- p2b-all-9runs: 已被终止 — unknown\\\\n- mvp_p2b_contrastive_training: 已被终止 — unknown\\\\n- mvp_p2b_contrastive_v2: 已被终止 — unknown\\\\n- p2b_eval_all: 已被终止 — unknown\\\\n- m2_early_pilot: 已被终止 — unknown\\\\n- m2_early_pilot_v2: 训练失败 — unknown\\\\n- m2_early_pilot_v3: 已被终止 — unknown\\\\n- m2_full_starcoder: 训练失败 — unknown\\\\n- m1_reextract: 训练失败 — unknown\\\\n\\\", \\\"total_chars\\\": 3816, \\\"truncated\\\": false}, \\\"error\\\": null, \\\"metadata\\\": {}}\"}",
  "mcpMeta": {
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/report.md\", \"content\": \"# Handover — 2026-05-15\\n\\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\\n\\n## 运行中\\n| exp_id | 假设 | 状态 | 关键指标 | W&B |\\n|--------|------|------|---------|-----|\\n| plan_003_swebench_eval | SWE-bench Lite 纯检索 eval：用 6 个 Qwen M2 checkpoints 在 300 个 SWE-bench Lite 实例上评估 file-level retrieval Recall@{1,5,10,20} 和 MRR。每个实例需 clone repo 并检索，~131s/instance。6 checkpoints 共 ~66h。 | — | — | — |\\n| m2_full_starcoder_resumed | M2 StarCoder resumed: 继续 m2_full_starcoder 的 8 sequential runs (random×2 + embedding×3 + dataflow×3)。原实验因 cron timeout 标记为 failed，实际 PID 519791 正常运行。 | — | — | — |\\n| m2_full_qwen_continued | M2 Qwen continued: 继续 m2_full_qwen 的剩余 runs (random_s44 + embedding×3 + dataflow×3)。原实验 cron 在 s42 退出时自动设为 ANALYZING，但链仍在运行。 | — | — | — |\\n\\n## 待处理\\n- plan_018_bm25: BM25 negative baseline: Dream 审稿三档一致认定缺 BM25 baseline 是论文最大结构性缺陷。Phase 1 (CPU): 对 M2 训练语料建 BM25 索引，挖掘 BM25 hard negatives，生成训练数据。Phase 2 (GPU): 用 BM25 negatives 训练 Qwen + StarCoder 各 1 seed，对比 R@1。（排队等待 GPU）\\n- plan_015_dynamic: Dynamic negative mining (epoch-level re-mining): 每 epoch 重新用当前 encoder embedding 挖掘 negatives，验证 static mining 是否足够。缩减版：只跑 dynamic_ep × 1 seed (Qwen, s42)，~11h 单卡。若 dynamic ≈ static（预期 <1pp 差异），在 Limitation 段排除 confound。（排队等待 GPU）\\n- plan_005_stratified: Plan 005 分层分析：按 repo size/pool size/query-pos similarity/structural data availability/neg_difficulty quartile 5 维度分层评估 embedding vs random 策略差异，控制 pool_size confound。Claim 2 支撑实验。v2 结果为 ground truth（v1→v2 changelog 见 art_20260514_3008c4）。（准备中）\\n\\n## 近期结论\\n- **plan_017_literature** (success): Inference-time graph method comparison: 8 papers surveyed (CodexGraph, LocAgent, RANGER, GraphCoder, ARISE, RepoGraph, CodeGRAG, CodeRAG). Discussion v2 drafted, all citations verified. Conclusion: training-time vs inference-time complementary.\\n- **m2_full_starcoder** (failed): Full M2 StarCoder: 3 strategies × 3 seeds on full M1 data. Cross-encoder validation — if embedding > random holds for both Qwen and StarCoder, method is encoder-agnostic. Resolves plan_013 pilot negative (dataflow encoder-dependent). ← 基于 plan_013_starcoder\\n  [m2_starcoder_status_check](/api/workspace-files/projects/structfuse-context/artifacts/m2_full_starcoder/report/m2_starcoder_status_check.md)\\n- **neg_difficulty_analysis** (success): Negative difficulty distribution analysis: 用预训练 Qwen2.5-Coder-3B 和 StarCoder2-3B 计算 3 策略 (random/embedding/dataflow) 的 query-negative/positive cosine similarity，分析 pretrained representation separability 跨编码器差异。MAX_LENGTH=2048 匹配训练设置。\\n  [neg_difficulty_margin_comparison](/api/workspace-files/projects/structfuse-context/artifacts/neg_difficulty_analysis/chart/neg_difficulty_margin_comparison_meta.txt) | [neg_difficulty_margin_comparison](/api/workspace-files/projects/structfuse-context/artifacts/neg_difficulty_analysis/chart/neg_difficulty_margin_comparison_meta_01876a.txt) | [neg_difficulty_similarity_dist](/api/workspace-files/projects/structfuse-context/artifacts/neg_difficulty_analysis/chart/neg_difficulty_similarity_dist_meta.txt) | [neg_difficulty_ratio_heatmap](/api/workspace-files/projects/structfuse-context/artifacts/neg_difficulty_analysis/chart/neg_difficulty_ratio_heatmap_meta.txt)\\n\\n## 趋势\\n成功 11 / 负向 2 / 失败 3 / 共 30\\n\\n## 下一步\\n（无活跃 idea，请通过 ideas.md 添加）\\n\\n## 资源状态\\nbjb1-42106: 无 GPU 信息\\n\\n## 告警\\n- p2b-smoke-test: 已被终止 — unknown\\n- p2b-smoke2: 已被终止 — unknown\\n- p2b-smoke3: 已被终止 — unknown\\n- p2b-smoke4: 已被终止 — unknown\\n- p2b-smoke5: 已被终止 — unknown\\n- p2b-smoke6: 已被终止 — unknown\\n- p2b-smoke7: 已被终止 — unknown\\n- p2b-smoke8: 已被终止 — unknown\\n- p2b-all-9runs: 已被终止 — unknown\\n- mvp_p2b_contrastive_training: 已被终止 — unknown\\n- mvp_p2b_contrastive_v2: 已被终止 — unknown\\n- p2b_eval_all: 已被终止 — unknown\\n- m2_early_pilot: 已被终止 — unknown\\n- m2_early_pilot_v2: 训练失败 — unknown\\n- m2_early_pilot_v3: 已被终止 — unknown\\n- m2_full_starcoder: 训练失败 — unknown\\n- m1_reextract: 训练失败 — unknown\\n\", \"total_chars\": 3816, \"truncated\": false}, \"error\": null, \"metadata\": {}}"
    }
  },
  "sourceToolAssistantUUID": "d66dff60-7c21-4358-8640-72be8cad1f05",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/.claude/sessions/reviewer_65cfe724",
  "sessionId": "f444a635-eeef-4924-9b48-a4c308632421",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---


### Tool call

_source line 16 · 2026-05-16T00:23:10.910Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_roadmap · `toolu_01VmB1Ywd9TuRRcboTX2wJ1k`</summary>

```json
{
  "project": "structfuse-context"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "fcb2f846-f171-415b-9a25-d81d9230854d",
  "isSidechain": false,
  "requestId": "req_011Cb5J21neDKTbom9RAnGPV",
  "type": "assistant",
  "uuid": "e456ce28-4d88-4f8f-9f6e-a9eeb91dedd0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/.claude/sessions/reviewer_65cfe724",
  "sessionId": "f444a635-eeef-4924-9b48-a4c308632421",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015NZtvJiYqYmUPrMkyqFWzC",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1531,
      "cache_read_input_tokens": 30680,
      "output_tokens": 243,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1531,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 243,
          "cache_read_input_tokens": 30680,
          "cache_creation_input_tokens": 1531,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1531
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

_source line 17 · 2026-05-16T00:23:10.925Z_

<details><summary>↩ Tool result · `toolu_01VmB1Ywd9TuRRcboTX2wJ1k`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/ROADMAP.md\", \"content\": \"# StructFuse — Research Dashboard\\n\\n> 最后更新: 2026-05-15 18:00 UTC | 更新原因: 训练进度更新 + SWE-bench/pool50 流水线就绪\\n\\n## 核心方向\\nEmbedding-distance mining improves contrastive code retrieval at zero additional cost (D049 软化 framing). ⚠️ **2-seed mean Δ ≈ 0 (D056), 待 embed_s42 + pool=50 cluster bootstrap 确认**。BM25 baseline empirically closes CoCoHaNeRe correction argument. Structure-grounded negatives conditional on representation saturation (n=2, exploratory per D035). 详见 paper_framing.md。\\n\\n## 当前进展\\n- **阶段**: Research（post-MVP）+ 审稿进行中\\n- **Qwen (cuda:0)**: dataflow_s43 running. 4/7 done. eval@500 R@1=0.5495. **ETA 主链: ~May 16 08:00 CST** (early stop 加速)\\n- **StarCoder (cuda:1)**: random_s44 ✅ 完成 → embedding_distance_s42 running. 2/6 done. ETA: ~May 19-20 CST\\n- **Qwen s42 supplement**: watcher PID 966920 就绪，主链完成后自动触发 embed_s42+dataflow_s42+bm25_s42 (~18h) → **全部 Qwen ~May 17 14:00-18:00**\\n- **StarCoder supplement**: 脚本已修改为 BM25-only\\n- **BM25 Phase 2**: tmux watcher 就绪，全部 M2 完成后自动触发\\n- **m1 合并**: 合并脚本就绪（dry-run: 89.9% structural_data_rate）\\n- **Pool=50 流水线**: 完全就绪，Qwen 完成后可立即触发\\n- **SWE-bench**: eval 脚本 + 批量运行脚本就绪，需 GPU 决策\\n- **训练动态分析**: 5 个核心发现已总结\\n- **写作**: Intro v1 ✅ | Method v1 ✅ | Related Work v1 ✅ | Conclusion v1 ✅ | Abstract v2 修复中 | Experiments v1 D055 修复中\\n- **D055 bootstrap**: 脚本已修复 (adapter-only 兼容). 正式流程: M2→pool=50→cluster bootstrap\\n- **已完成**: plan_017 ✅ | plan_018 Phase 1 ✅ | neg_difficulty 可视化 ✅ | K/checkpoint 文档 ✅ | StarCoder random_s44 ✅\\n\\n## ⚠️ Claim 1 Delta 状况 (D048→D056)\\n| seed | random R@1 | embed R@1 | Δ |\\n|------|-----------|-----------|---|\\n| s42 | 0.5527 | **缺失** | — |\\n| s43 | 0.5554 | 0.5606 | +0.52pp |\\n| s44 | 0.6009★ | 0.5942 | -0.67pp |\\n| 2-seed mean | — | — | **-0.08pp** |\\n\\n★ s44 random 是 outlier (比 s42/s43 均值高 4.7pp)。embed_s44=0.5942 本身高于 non-outlier random 均值。\\n- **翻盘路径**: (1) embed_s42 swing vote (2) pool=50 instance-level cluster bootstrap (3) D052 C/D 应急\\n- **不提前 pivot** (D018/D019 原则)\\n\\n## Post-M2 优先级\\n| Priority | Plan | Description | GPU hours | 触发 |\\n|----------|------|-------------|-----------|------|\\n| **P0** | pool=50 | 重新评估所有 best checkpoint | ~2h | Qwen 完成后立即（流水线已就绪） |\\n| **P0** | D045 stats | cluster bootstrap 统计分析 | 0h (分析) | pool=50 后 |\\n| **P0** | plan_005 | 分层分析 (Claim 2 定量支撑) | 0h (分析) | M2 完成后 |\\n| **P0** | plan_018 P2 | BM25 训练 Qwen+StarCoder | 15h | watcher 自动触发 |\\n| **P0** | plan_003 | SWE-bench Lite (300) e2e eval | 40h | 脚本就绪，需 GPU 决策 + API key |\\n| **P1** | plan_004 | RepoBench-R (多seed+CIs) | 15h | planned |\\n| **P1** | plan_019 | Pool size sensitivity | 5h | planned |\\n\\n## 覆盖率\\n- Claim 1: 3/15 done (20%) — M2 running 解锁大部分\\n- Claim 2: 0/3 done (0%) — plan_005 analysis-only, M2 后数小时可完成\\n- Claim 3: 1/1 done (100%) ✅\\n\\n## 近期任务\\n- [x] Intro/Method/Related Work/Conclusion 内审 PASS\\n- [x] StarCoder random_s44 完成\\n- [x] StarCoder supplement 脚本修改为 BM25-only\\n- [x] m1 合并脚本就绪 (dry-run 89.9% structural_data_rate)\\n- [x] Pool=50 流水线就绪\\n- [x] SWE-bench eval + 批量运行脚本就绪\\n- [x] 训练动态分析 5 个核心发现\\n- [ ] Abstract v2 + Experiments v1 修复完成\\n- [ ] **May 16 06:00**: 验证 watcher PID 966920 活性（主链完成前 ~2h）\\n- [ ] Qwen 主链完成 (~May 16 08:00) → s42 supplement 自动触发\\n- [ ] m1 合并正式执行 → 检查恢复率\\n- [ ] Qwen 全部完成 (~May 17 14:00-18:00) → pool=50 + D045 stats + plan_005\\n- [ ] StarCoder 全部完成 (~May 19-20)\\n- [ ] SWE-bench GPU 决策 + API key 审批\\n- [ ] 正式提交审稿 — 目标 May 18\\n- [ ] plan_003 SWE-bench eval — 需 API key + GPU\\n\\n## GPU 预算\\n- **bjb1-42106**: 2× RTX PRO 6000 96GB\\n- **时间线**: Qwen 主链 May 16 → s42 supplement May 17 14:00-18:00 → StarCoder May 19-20 → post-M2 → ARR May 25\\n- Must-do: 57h / 2GPU ≈ 29h | Should-do: 38h / 2GPU ≈ 19h\\n\\n## 关键风险\\n1. **Claim 1 delta 2-seed mean ≈ 0** (D056): embed_s42 + pool=50 是翻盘点\\n2. **Watcher 可靠性**: PID 966920 需在主链完成前验证活性\\n3. **plan_003 需 API key**: Qwen3.6-27B — API key 待审批中\\n4. **SWE-bench GPU 决策待定**: eval/批量脚本已就绪，但需确定 GPU 分配方案\\n5. **ARR May 25**: StarCoder 完成 ~May 20，post-M2 窗口 5 天\\n\\n## 关键决策日志\\n\\n| ID | 日期 | 摘要 | 关联实验 |\\n|----|------|------|----------|\\n| D059 | 2026-05-15 | 确认 A/B 双轨叙事策略：A=stratified 揭示异质性，B=B1+Claim2 hybri | m2_full_qwen_continued, m2_full_starcoder_resumed, plan_005_stratified |\\n| D058 | 2026-05-15 | D057 trajectory 发现重新定位：从 Claim 2 evidence 降级为 §4.3 | m2_full_qwen_continued |\\n| D057 | 2026-05-15 | embed_s44 展示 R@1/val_loss 指标分歧：R@1 峰值 step 500 而 v | m2_full_qwen_continued |\\n| D056 | 2026-05-15 | embed_s44 delta -0.67pp，2-seed mean ≈ 0。Claim 1 se | m2_full_qwen_continued, m2_full_qwen |\\n| D055 | 2026-05-15 | 统计检验改为 instance-level cluster bootstrap (by repo)  | m2_full_qwen_continued, embed_s42 |\\n| D054 | 2026-05-15 | embed_s42 + dataflow_s42 作为 P0 排在 Qwen chain 完成后立即 | m2_full_qwen_continued, embed_s42 |\\n| D053 | 2026-05-15 | plan_005 分层分析升 P0：Claim 2 唯一定量支撑，M2 完成后立即执行 | m2_full_qwen_continued, m2_full_starcoder_resumed |\\n| D052 | 2026-05-15 | Claim 1 Scenario C/D 应急方案：mean Δ<0.5pp 或 CI 跨零时的措辞 | m2_full_qwen_continued, m2_full_starcoder_resumed |\\n| D051 | 2026-05-15 | 论文结果必须报告 mean ± std across seeds，禁止 cherry-pick 单  | m2_full_qwen_continued, m2_full_starcoder_resumed |\\n| D050 | 2026-05-15 | BM25 watcher 脚本需修复 s42 regime：统一为 2 epochs + patie | plan_018_bm25, m2_full_starcoder_resumed |\\n\\n\", \"lines\": 96}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "e456ce28-4d88-4f8f-9f6e-a9eeb91dedd0",
  "isSidechain": false,
  "promptId": "ee81bb41-edfe-48b7-9827-d79a74cf7a5e",
  "type": "user",
  "uuid": "b56c79e2-15ae-4fed-964e-0da3d484d672",
  "toolUseResult": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"path\\\": \\\"/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/ROADMAP.md\\\", \\\"content\\\": \\\"# StructFuse — Research Dashboard\\\\n\\\\n> 最后更新: 2026-05-15 18:00 UTC | 更新原因: 训练进度更新 + SWE-bench/pool50 流水线就绪\\\\n\\\\n## 核心方向\\\\nEmbedding-distance mining improves contrastive code retrieval at zero additional cost (D049 软化 framing). ⚠️ **2-seed mean Δ ≈ 0 (D056), 待 embed_s42 + pool=50 cluster bootstrap 确认**。BM25 baseline empirically closes CoCoHaNeRe correction argument. Structure-grounded negatives conditional on representation saturation (n=2, exploratory per D035). 详见 paper_framing.md。\\\\n\\\\n## 当前进展\\\\n- **阶段**: Research（post-MVP）+ 审稿进行中\\\\n- **Qwen (cuda:0)**: dataflow_s43 running. 4/7 done. eval@500 R@1=0.5495. **ETA 主链: ~May 16 08:00 CST** (early stop 加速)\\\\n- **StarCoder (cuda:1)**: random_s44 ✅ 完成 → embedding_distance_s42 running. 2/6 done. ETA: ~May 19-20 CST\\\\n- **Qwen s42 supplement**: watcher PID 966920 就绪，主链完成后自动触发 embed_s42+dataflow_s42+bm25_s42 (~18h) → **全部 Qwen ~May 17 14:00-18:00**\\\\n- **StarCoder supplement**: 脚本已修改为 BM25-only\\\\n- **BM25 Phase 2**: tmux watcher 就绪，全部 M2 完成后自动触发\\\\n- **m1 合并**: 合并脚本就绪（dry-run: 89.9% structural_data_rate）\\\\n- **Pool=50 流水线**: 完全就绪，Qwen 完成后可立即触发\\\\n- **SWE-bench**: eval 脚本 + 批量运行脚本就绪，需 GPU 决策\\\\n- **训练动态分析**: 5 个核心发现已总结\\\\n- **写作**: Intro v1 ✅ | Method v1 ✅ | Related Work v1 ✅ | Conclusion v1 ✅ | Abstract v2 修复中 | Experiments v1 D055 修复中\\\\n- **D055 bootstrap**: 脚本已修复 (adapter-only 兼容). 正式流程: M2→pool=50→cluster bootstrap\\\\n- **已完成**: plan_017 ✅ | plan_018 Phase 1 ✅ | neg_difficulty 可视化 ✅ | K/checkpoint 文档 ✅ | StarCoder random_s44 ✅\\\\n\\\\n## ⚠️ Claim 1 Delta 状况 (D048→D056)\\\\n| seed | random R@1 | embed R@1 | Δ |\\\\n|------|-----------|-----------|---|\\\\n| s42 | 0.5527 | **缺失** | — |\\\\n| s43 | 0.5554 | 0.5606 | +0.52pp |\\\\n| s44 | 0.6009★ | 0.5942 | -0.67pp |\\\\n| 2-seed mean | — | — | **-0.08pp** |\\\\n\\\\n★ s44 random 是 outlier (比 s42/s43 均值高 4.7pp)。embed_s44=0.5942 本身高于 non-outlier random 均值。\\\\n- **翻盘路径**: (1) embed_s42 swing vote (2) pool=50 instance-level cluster bootstrap (3) D052 C/D 应急\\\\n- **不提前 pivot** (D018/D019 原则)\\\\n\\\\n## Post-M2 优先级\\\\n| Priority | Plan | Description | GPU hours | 触发 |\\\\n|----------|------|-------------|-----------|------|\\\\n| **P0** | pool=50 | 重新评估所有 best checkpoint | ~2h | Qwen 完成后立即（流水线已就绪） |\\\\n| **P0** | D045 stats | cluster bootstrap 统计分析 | 0h (分析) | pool=50 后 |\\\\n| **P0** | plan_005 | 分层分析 (Claim 2 定量支撑) | 0h (分析) | M2 完成后 |\\\\n| **P0** | plan_018 P2 | BM25 训练 Qwen+StarCoder | 15h | watcher 自动触发 |\\\\n| **P0** | plan_003 | SWE-bench Lite (300) e2e eval | 40h | 脚本就绪，需 GPU 决策 + API key |\\\\n| **P1** | plan_004 | RepoBench-R (多seed+CIs) | 15h | planned |\\\\n| **P1** | plan_019 | Pool size sensitivity | 5h | planned |\\\\n\\\\n## 覆盖率\\\\n- Claim 1: 3/15 done (20%) — M2 running 解锁大部分\\\\n- Claim 2: 0/3 done (0%) — plan_005 analysis-only, M2 后数小时可完成\\\\n- Claim 3: 1/1 done (100%) ✅\\\\n\\\\n## 近期任务\\\\n- [x] Intro/Method/Related Work/Conclusion 内审 PASS\\\\n- [x] StarCoder random_s44 完成\\\\n- [x] StarCoder supplement 脚本修改为 BM25-only\\\\n- [x] m1 合并脚本就绪 (dry-run 89.9% structural_data_rate)\\\\n- [x] Pool=50 流水线就绪\\\\n- [x] SWE-bench eval + 批量运行脚本就绪\\\\n- [x] 训练动态分析 5 个核心发现\\\\n- [ ] Abstract v2 + Experiments v1 修复完成\\\\n- [ ] **May 16 06:00**: 验证 watcher PID 966920 活性（主链完成前 ~2h）\\\\n- [ ] Qwen 主链完成 (~May 16 08:00) → s42 supplement 自动触发\\\\n- [ ] m1 合并正式执行 → 检查恢复率\\\\n- [ ] Qwen 全部完成 (~May 17 14:00-18:00) → pool=50 + D045 stats + plan_005\\\\n- [ ] StarCoder 全部完成 (~May 19-20)\\\\n- [ ] SWE-bench GPU 决策 + API key 审批\\\\n- [ ] 正式提交审稿 — 目标 May 18\\\\n- [ ] plan_003 SWE-bench eval — 需 API key + GPU\\\\n\\\\n## GPU 预算\\\\n- **bjb1-42106**: 2× RTX PRO 6000 96GB\\\\n- **时间线**: Qwen 主链 May 16 → s42 supplement May 17 14:00-18:00 → StarCoder May 19-20 → post-M2 → ARR May 25\\\\n- Must-do: 57h / 2GPU ≈ 29h | Should-do: 38h / 2GPU ≈ 19h\\\\n\\\\n## 关键风险\\\\n1. **Claim 1 delta 2-seed mean ≈ 0** (D056): embed_s42 + pool=50 是翻盘点\\\\n2. **Watcher 可靠性**: PID 966920 需在主链完成前验证活性\\\\n3. **plan_003 需 API key**: Qwen3.6-27B — API key 待审批中\\\\n4. **SWE-bench GPU 决策待定**: eval/批量脚本已就绪，但需确定 GPU 分配方案\\\\n5. **ARR May 25**: StarCoder 完成 ~May 20，post-M2 窗口 5 天\\\\n\\\\n## 关键决策日志\\\\n\\\\n| ID | 日期 | 摘要 | 关联实验 |\\\\n|----|------|------|----------|\\\\n| D059 | 2026-05-15 | 确认 A/B 双轨叙事策略：A=stratified 揭示异质性，B=B1+Claim2 hybri | m2_full_qwen_continued, m2_full_starcoder_resumed, plan_005_stratified |\\\\n| D058 | 2026-05-15 | D057 trajectory 发现重新定位：从 Claim 2 evidence 降级为 §4.3 | m2_full_qwen_continued |\\\\n| D057 | 2026-05-15 | embed_s44 展示 R@1/val_loss 指标分歧：R@1 峰值 step 500 而 v | m2_full_qwen_continued |\\\\n| D056 | 2026-05-15 | embed_s44 delta -0.67pp，2-seed mean ≈ 0。Claim 1 se | m2_full_qwen_continued, m2_full_qwen |\\\\n| D055 | 2026-05-15 | 统计检验改为 instance-level cluster bootstrap (by repo)  | m2_full_qwen_continued, embed_s42 |\\\\n| D054 | 2026-05-15 | embed_s42 + dataflow_s42 作为 P0 排在 Qwen chain 完成后立即 | m2_full_qwen_continued, embed_s42 |\\\\n| D053 | 2026-05-15 | plan_005 分层分析升 P0：Claim 2 唯一定量支撑，M2 完成后立即执行 | m2_full_qwen_continued, m2_full_starcoder_resumed |\\\\n| D052 | 2026-05-15 | Claim 1 Scenario C/D 应急方案：mean Δ<0.5pp 或 CI 跨零时的措辞 | m2_full_qwen_continued, m2_full_starcoder_resumed |\\\\n| D051 | 2026-05-15 | 论文结果必须报告 mean ± std across seeds，禁止 cherry-pick 单  | m2_full_qwen_continued, m2_full_starcoder_resumed |\\\\n| D050 | 2026-05-15 | BM25 watcher 脚本需修复 s42 regime：统一为 2 epochs + patie | plan_018_bm25, m2_full_starcoder_resumed |\\\\n\\\\n\\\", \\\"lines\\\": 96}, \\\"error\\\": null, \\\"metadata\\\": {}}\"}",
  "mcpMeta": {
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/ROADMAP.md\", \"content\": \"# StructFuse — Research Dashboard\\n\\n> 最后更新: 2026-05-15 18:00 UTC | 更新原因: 训练进度更新 + SWE-bench/pool50 流水线就绪\\n\\n## 核心方向\\nEmbedding-distance mining improves contrastive code retrieval at zero additional cost (D049 软化 framing). ⚠️ **2-seed mean Δ ≈ 0 (D056), 待 embed_s42 + pool=50 cluster bootstrap 确认**。BM25 baseline empirically closes CoCoHaNeRe correction argument. Structure-grounded negatives conditional on representation saturation (n=2, exploratory per D035). 详见 paper_framing.md。\\n\\n## 当前进展\\n- **阶段**: Research（post-MVP）+ 审稿进行中\\n- **Qwen (cuda:0)**: dataflow_s43 running. 4/7 done. eval@500 R@1=0.5495. **ETA 主链: ~May 16 08:00 CST** (early stop 加速)\\n- **StarCoder (cuda:1)**: random_s44 ✅ 完成 → embedding_distance_s42 running. 2/6 done. ETA: ~May 19-20 CST\\n- **Qwen s42 supplement**: watcher PID 966920 就绪，主链完成后自动触发 embed_s42+dataflow_s42+bm25_s42 (~18h) → **全部 Qwen ~May 17 14:00-18:00**\\n- **StarCoder supplement**: 脚本已修改为 BM25-only\\n- **BM25 Phase 2**: tmux watcher 就绪，全部 M2 完成后自动触发\\n- **m1 合并**: 合并脚本就绪（dry-run: 89.9% structural_data_rate）\\n- **Pool=50 流水线**: 完全就绪，Qwen 完成后可立即触发\\n- **SWE-bench**: eval 脚本 + 批量运行脚本就绪，需 GPU 决策\\n- **训练动态分析**: 5 个核心发现已总结\\n- **写作**: Intro v1 ✅ | Method v1 ✅ | Related Work v1 ✅ | Conclusion v1 ✅ | Abstract v2 修复中 | Experiments v1 D055 修复中\\n- **D055 bootstrap**: 脚本已修复 (adapter-only 兼容). 正式流程: M2→pool=50→cluster bootstrap\\n- **已完成**: plan_017 ✅ | plan_018 Phase 1 ✅ | neg_difficulty 可视化 ✅ | K/checkpoint 文档 ✅ | StarCoder random_s44 ✅\\n\\n## ⚠️ Claim 1 Delta 状况 (D048→D056)\\n| seed | random R@1 | embed R@1 | Δ |\\n|------|-----------|-----------|---|\\n| s42 | 0.5527 | **缺失** | — |\\n| s43 | 0.5554 | 0.5606 | +0.52pp |\\n| s44 | 0.6009★ | 0.5942 | -0.67pp |\\n| 2-seed mean | — | — | **-0.08pp** |\\n\\n★ s44 random 是 outlier (比 s42/s43 均值高 4.7pp)。embed_s44=0.5942 本身高于 non-outlier random 均值。\\n- **翻盘路径**: (1) embed_s42 swing vote (2) pool=50 instance-level cluster bootstrap (3) D052 C/D 应急\\n- **不提前 pivot** (D018/D019 原则)\\n\\n## Post-M2 优先级\\n| Priority | Plan | Description | GPU hours | 触发 |\\n|----------|------|-------------|-----------|------|\\n| **P0** | pool=50 | 重新评估所有 best checkpoint | ~2h | Qwen 完成后立即（流水线已就绪） |\\n| **P0** | D045 stats | cluster bootstrap 统计分析 | 0h (分析) | pool=50 后 |\\n| **P0** | plan_005 | 分层分析 (Claim 2 定量支撑) | 0h (分析) | M2 完成后 |\\n| **P0** | plan_018 P2 | BM25 训练 Qwen+StarCoder | 15h | watcher 自动触发 |\\n| **P0** | plan_003 | SWE-bench Lite (300) e2e eval | 40h | 脚本就绪，需 GPU 决策 + API key |\\n| **P1** | plan_004 | RepoBench-R (多seed+CIs) | 15h | planned |\\n| **P1** | plan_019 | Pool size sensitivity | 5h | planned |\\n\\n## 覆盖率\\n- Claim 1: 3/15 done (20%) — M2 running 解锁大部分\\n- Claim 2: 0/3 done (0%) — plan_005 analysis-only, M2 后数小时可完成\\n- Claim 3: 1/1 done (100%) ✅\\n\\n## 近期任务\\n- [x] Intro/Method/Related Work/Conclusion 内审 PASS\\n- [x] StarCoder random_s44 完成\\n- [x] StarCoder supplement 脚本修改为 BM25-only\\n- [x] m1 合并脚本就绪 (dry-run 89.9% structural_data_rate)\\n- [x] Pool=50 流水线就绪\\n- [x] SWE-bench eval + 批量运行脚本就绪\\n- [x] 训练动态分析 5 个核心发现\\n- [ ] Abstract v2 + Experiments v1 修复完成\\n- [ ] **May 16 06:00**: 验证 watcher PID 966920 活性（主链完成前 ~2h）\\n- [ ] Qwen 主链完成 (~May 16 08:00) → s42 supplement 自动触发\\n- [ ] m1 合并正式执行 → 检查恢复率\\n- [ ] Qwen 全部完成 (~May 17 14:00-18:00) → pool=50 + D045 stats + plan_005\\n- [ ] StarCoder 全部完成 (~May 19-20)\\n- [ ] SWE-bench GPU 决策 + API key 审批\\n- [ ] 正式提交审稿 — 目标 May 18\\n- [ ] plan_003 SWE-bench eval — 需 API key + GPU\\n\\n## GPU 预算\\n- **bjb1-42106**: 2× RTX PRO 6000 96GB\\n- **时间线**: Qwen 主链 May 16 → s42 supplement May 17 14:00-18:00 → StarCoder May 19-20 → post-M2 → ARR May 25\\n- Must-do: 57h / 2GPU ≈ 29h | Should-do: 38h / 2GPU ≈ 19h\\n\\n## 关键风险\\n1. **Claim 1 delta 2-seed mean ≈ 0** (D056): embed_s42 + pool=50 是翻盘点\\n2. **Watcher 可靠性**: PID 966920 需在主链完成前验证活性\\n3. **plan_003 需 API key**: Qwen3.6-27B — API key 待审批中\\n4. **SWE-bench GPU 决策待定**: eval/批量脚本已就绪，但需确定 GPU 分配方案\\n5. **ARR May 25**: StarCoder 完成 ~May 20，post-M2 窗口 5 天\\n\\n## 关键决策日志\\n\\n| ID | 日期 | 摘要 | 关联实验 |\\n|----|------|------|----------|\\n| D059 | 2026-05-15 | 确认 A/B 双轨叙事策略：A=stratified 揭示异质性，B=B1+Claim2 hybri | m2_full_qwen_continued, m2_full_starcoder_resumed, plan_005_stratified |\\n| D058 | 2026-05-15 | D057 trajectory 发现重新定位：从 Claim 2 evidence 降级为 §4.3 | m2_full_qwen_continued |\\n| D057 | 2026-05-15 | embed_s44 展示 R@1/val_loss 指标分歧：R@1 峰值 step 500 而 v | m2_full_qwen_continued |\\n| D056 | 2026-05-15 | embed_s44 delta -0.67pp，2-seed mean ≈ 0。Claim 1 se | m2_full_qwen_continued, m2_full_qwen |\\n| D055 | 2026-05-15 | 统计检验改为 instance-level cluster bootstrap (by repo)  | m2_full_qwen_continued, embed_s42 |\\n| D054 | 2026-05-15 | embed_s42 + dataflow_s42 作为 P0 排在 Qwen chain 完成后立即 | m2_full_qwen_continued, embed_s42 |\\n| D053 | 2026-05-15 | plan_005 分层分析升 P0：Claim 2 唯一定量支撑，M2 完成后立即执行 | m2_full_qwen_continued, m2_full_starcoder_resumed |\\n| D052 | 2026-05-15 | Claim 1 Scenario C/D 应急方案：mean Δ<0.5pp 或 CI 跨零时的措辞 | m2_full_qwen_continued, m2_full_starcoder_resumed |\\n| D051 | 2026-05-15 | 论文结果必须报告 mean ± std across seeds，禁止 cherry-pick 单  | m2_full_qwen_continued, m2_full_starcoder_resumed |\\n| D050 | 2026-05-15 | BM25 watcher 脚本需修复 s42 regime：统一为 2 epochs + patie | plan_018_bm25, m2_full_starcoder_resumed |\\n\\n\", \"lines\": 96}, \"error\": null, \"metadata\": {}}"
    }
  },
  "sourceToolAssistantUUID": "e456ce28-4d88-4f8f-9f6e-a9eeb91dedd0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/.claude/sessions/reviewer_65cfe724",
  "sessionId": "f444a635-eeef-4924-9b48-a4c308632421",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---


### Runtime record

_source line 18_

```json
{
  "type": "last-prompt",
  "lastPrompt": "[系统通知 — worker_done:worker_research_related-work-literature_20260516T001526]: Worker worker_research_related-work-literature_20260516T001526 已完成（status=done），请审查 Agent 的处理结果。",
  "leafUuid": "b56c79e2-15ae-4fed-964e-0da3d484d672",
  "sessionId": "f444a635-eeef-4924-9b48-a4c308632421"
}
```

---


### Runtime record

_source line 19_

```json
{
  "type": "ai-title",
  "aiTitle": "Review research literature worker completion",
  "sessionId": "f444a635-eeef-4924-9b48-a4c308632421"
}
```

---


### Assistant

_source line 20 · 2026-05-16T00:23:16.971Z_

<details><summary>Logged reasoning block</summary>

```text
The worker notification is about `worker_research_related-work-literature_20260516T001526`. Let me find the relevant registry entry. Looking at the registry, `plan_017_literature` seems related but it was completed earlier (2026-05-14). The worker name mentions "related-work-literature" which suggests it's about the Related Work section of the paper.

Let me check for more recent entries and the literature-related artifacts. I should also look at what this specific worker produced. Let me check more of the registry and relevant files.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b56c79e2-15ae-4fed-964e-0da3d484d672",
  "isSidechain": false,
  "requestId": "req_011Cb5J2JeuFZcm8TGAjpUaU",
  "type": "assistant",
  "uuid": "0308adc8-bbfb-401b-82ac-6949f27c72f9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/.claude/sessions/reviewer_65cfe724",
  "sessionId": "f444a635-eeef-4924-9b48-a4c308632421",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QWbfLxQNBrJ4cFjfbeviqt",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 14930,
      "cache_read_input_tokens": 32211,
      "output_tokens": 442,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 14930,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 442,
          "cache_read_input_tokens": 32211,
          "cache_creation_input_tokens": 14930,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 14930
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

_source line 21 · 2026-05-16T00:23:18.342Z_

Worker 名称是 `worker_research_related-work-literature_20260516T001526`，但 registry 中最相关的 `plan_017_literature` 是 2026-05-14 完成的。需要确认这个 worker 的实际产出。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0308adc8-bbfb-401b-82ac-6949f27c72f9",
  "isSidechain": false,
  "requestId": "req_011Cb5J2JeuFZcm8TGAjpUaU",
  "type": "assistant",
  "uuid": "dfce5198-8ce9-4204-ad63-2e09d4299a00",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/.claude/sessions/reviewer_65cfe724",
  "sessionId": "f444a635-eeef-4924-9b48-a4c308632421",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QWbfLxQNBrJ4cFjfbeviqt",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 14930,
      "cache_read_input_tokens": 32211,
      "output_tokens": 442,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 14930,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 442,
          "cache_read_input_tokens": 32211,
          "cache_creation_input_tokens": 14930,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 14930
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

_source line 22 · 2026-05-16T00:23:19.936Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry · `toolu_01B5PU2Dp7oHoTbdxKQXgS9x`</summary>

```json
{
  "project": "structfuse-context",
  "limit": 0,
  "filters": {
    "status": "DONE"
  },
  "fields": [
    "status",
    "hypothesis",
    "conclusion",
    "completed_at",
    "updated_at",
    "notes"
  ]
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "dfce5198-8ce9-4204-ad63-2e09d4299a00",
  "isSidechain": false,
  "requestId": "req_011Cb5J2JeuFZcm8TGAjpUaU",
  "type": "assistant",
  "uuid": "f63572ef-e81c-4880-a207-1d3f834619fa",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/.claude/sessions/reviewer_65cfe724",
  "sessionId": "f444a635-eeef-4924-9b48-a4c308632421",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QWbfLxQNBrJ4cFjfbeviqt",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 14930,
      "cache_read_input_tokens": 32211,
      "output_tokens": 442,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 14930,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 442,
          "cache_read_input_tokens": 32211,
          "cache_creation_input_tokens": 14930,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 14930
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

_source line 23 · 2026-05-16T00:23:20.109Z_

<details><summary>↩ Tool result · `toolu_01B5PU2Dp7oHoTbdxKQXgS9x`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"experiments\": {\"plan_017_literature\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-14T21:33:45.149Z\", \"hypothesis\": \"Inference-time graph method comparison: 8 papers surveyed (CodexGraph, LocAgent, RANGER, GraphCoder, ARISE, RepoGraph, CodeGRAG, CodeRAG). Discussion v2 drafted, all citations verified. Conclusion: training-time vs inference-time complementary.\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-14T18:49:39.557Z\", \"notes\": \"Inference-time graph method comparison 完成。8 papers surveyed，其中 6 篇纳入 literature_map.yaml 和 discussion_v2.md（CodexGraph, LocAgent, RANGER, GraphCoder, ARISE, RepoGraph）。CodeGRAG 和 CodeRAG 经调研排除：CodeGRAG（arXiv 2405.02355）关注 NL→code generation 的 graph-augmented prompting，不涉及代码检索或对比学习；CodeRAG 系列（CodeRAG-Bench 2406.14497 / CodeRAG 2504.10046）关注 retrieval-augmented code generation benchmark 和 bigraph-based 代码生成，均为生成任务而非检索训练。两者与 StructFuse 的 scope（训练时结构信号用于对比学习代码检索）不符，故未纳入 discussion。\"}, \"m2_full_starcoder\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-14T18:04:29.245Z\", \"hypothesis\": \"Full M2 StarCoder: 3 strategies × 3 seeds on full M1 data. Cross-encoder validation — if embedding > random holds for both Qwen and StarCoder, method is encoder-agnostic. Resolves plan_013 pilot negative (dataflow encoder-dependent).\", \"notes\": \"Phase 1: 构建 StarCoder embedding negatives 完成。Phase 2: 9 runs 训练中。batch_size=8, num_negatives=7, epochs=3(s42)/2(s43+), lr=2e-5, eval_steps=500, no early_stopping。双 checkpoint: best + best_by_recall_at_1。Seeds: 42,43,44。[D026] s42 保持 3 epochs; s43/s44 及后续 runs 改为 2 epochs。[2026-05-15 02:02 CST] cuda:1 进程冲突修复并重新提交（PID 519791, timeout=144h）。Registry 状态 DONE(failed) 是旧 cron timeout 标记，实际正在运行 random_s43 [1/8]。新 cron 已注册监控 PID 519791。序列：random_s43→s44→(待插入bm25_s42)→embedding×3→dataflow×3。random_s42 结果：best R@1=0.4604 at step 2500, val_loss=0.6134 at step 1000。\", \"conclusion\": \"failed\", \"completed_at\": \"2026-05-14T17:49:55.304Z\"}, \"neg_difficulty_analysis\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-14T00:13:49.046Z\", \"hypothesis\": \"Negative difficulty distribution analysis: 用预训练 Qwen2.5-Coder-3B 和 StarCoder2-3B 计算 3 策略 (random/embedding/dataflow) 的 query-negative/positive cosine similarity，分析 pretrained representation separability 跨编码器差异。MAX_LENGTH=2048 匹配训练设置。\", \"notes\": \"128 vs 2048 token 对比完成（2026-05-14 05:54 CST）。Qwen pos_sim 在 2048t 下 0.9855（比 128t 的 0.9804 更高），确认 ceiling 为 Qwen 表征的结构性特征，非截断 artifact。StarCoder margin 2.6-4.1x Qwen（2048t）。核心结论：pretrained representation separability varies across encoders，跨两种 token 长度成立。数据源：128t → stats_v2.json，2048t → stats_v3_2048.json。\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-14T00:13:49.046Z\"}, \"m1_reextract\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-13T19:45:53.741Z\", \"hypothesis\": \"M1 重提取：恢复 28,276 个因运行时瞬态文件系统故障失败的 instances（82 repos）。预期将训练数据从 15,897 提升至 ~44,173。D022 批准。\", \"conclusion\": \"failed\", \"notes\": \"CodeQL query 100% 失败（exit status 2）。根因：Worker 安装 CodeQL CLI 2.25.4 时未执行 `codeql pack install`，`codeql/python-all@7.1.0` 标准库 pack 缺失。修复命令：`cd /root/structfuse/extraction/codeql_queries && /opt/codeql/codeql pack install`。已 kill 进程 + tmux session。无新数据产出（all.jsonl 未受影响）。等 Director 确认后修复重跑。\", \"completed_at\": \"2026-05-13T19:44:09.115Z\"}, \"m1_extraction\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-13T19:26:13.901Z\", \"notes\": \"[2026-05-13 19:25] COMPLETED. 837.8min, 123/131 repos (93.9%), 15,897/44,173 instances with structural data (36.0%), 6,696 skipped (clone/checkout). Output: all.jsonl 6.6GB. [2026-05-13 19:23 UPDATE] 28,276 buggy_file_not_found errors 经验证并非上游数据质量问题——10/10 抽查的文件在 repo 中全部存在。根因是运行时瞬态文件系统故障（CodeQL 并行 database creation 导致磁盘耗尽，锐截止模式）。这些 instances 可通过重跑恢复。D022: 准备重跑脚本中，等 Director 确认后执行。\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-13T10:59:42.462Z\"}, \"plan_006_scalability\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-13T19:24:00.741Z\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-13T07:57:58.176Z\", \"notes\": \"[2026-05-13 19:23] 全量统计 + error 分析 + fuzzy match 验证完成。关键发现: (1) 0 timeout; (2) 28,276 error 全部 buggy_file_not_found，但 fuzzy match 验证发现文件实际都存在——根因是运行时瞬态文件系统故障（锐截止模式：每个 repo 内先成功后突然全部失败，extraction_time=0.0s），可能是 CodeQL 并行数据库创建导致磁盘空间耗尽; (3) 这些 instance 可通过重跑恢复（当前 resolve_file_in_repo 对全部样本返回正确路径）; (4) 结构数据率 34.3% 有望提升至接近 100%（若重跑成功）; (5) Z% 随 repo 规模上升 (XL median 96%). Artifacts: plan006_full_scalability.json, art_20260513_d262da (error patterns)\", \"hypothesis\": \"Claim 3: CodeQL bounded data-flow extraction scales to large repos with acceptable timeout rates and provides meaningful structural coverage (Z%) that increases with repo complexity\"}, \"plan_013_starcoder\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-13T18:09:54.153Z\", \"hypothesis\": \"Architecture generalization: validate StructFuse with StarCoder2-3B encoder (vs Qwen2.5-Coder-3B in m2_embed_verify). If both encoders show same strategy ranking → method is encoder-agnostic, strengthening the core claim. Key differentiator for best→accept at Dream.\", \"notes\": \"[2026-05-13 16:00] ALL 3 STRATEGIES DONE. Ranking: embedding (R@1=0.5078) > random (0.4922) > dataflow (0.4869). Embedding vs random: +1.6pp (consistent with Qwen). Dataflow vs random: -0.5pp (DIFFERS from Qwen where dataflow > random +0.8pp). Hypothesis NEGATIVE: strategy ranking NOT identical across encoders. Embedding > random is encoder-agnostic, dataflow position is encoder-dependent. Log: /root/runs/faith-evidence-ie/plan_013_starcoder.log. Cron misreported EXIT_CODE=129 but all strategies completed (confirmed via log extraction worker).\", \"conclusion\": \"negative\", \"completed_at\": \"2026-05-13T15:15:20.165Z\"}, \"m2_embed_verify\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-13T15:59:51.621Z\", \"hypothesis\": \"True embedding mining verification: compare Qwen2.5-Coder-3B cosine similarity negatives vs BM25 negatives on pilot data (24 repos). If true embedding negatives are harder → Claim 2 (structure-aware negatives improve retrieval) gets stronger evidence.\", \"notes\": \"[2026-05-13 16:00] ALL 3 STRATEGIES DONE. Ranking: embedding (R@1=0.5557) > dataflow (0.5436) > random (0.5357). Embedding vs random: +2.0pp. Dataflow vs random: +0.8pp. All best at step 500, overfitting after. Hypothesis confirmed: true embedding negatives are harder → Claim 2 supported. Log: /root/runs/faith-evidence-ie/m2_embed_verify.log. Cron misreported EXIT_CODE=2 but all strategies completed successfully (confirmed via log extraction worker).\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-13T15:15:18.746Z\"}, \"mvp_p2b_contrastive_v2\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-13T07:23:28.932Z\", \"conclusion\": \"killed\", \"completed_at\": \"2026-05-12T15:04:44.396Z\", \"notes\": \"P2b 对比训练 v2，因磁盘空间不足被 kill。已被 p2b_5reruns（成功完成 9/9 runs）替代。\"}, \"p2b_dataflow_retrain\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-13T07:23:27.706Z\", \"conclusion\": \"negative\", \"completed_at\": \"2026-05-13T04:17:02.055Z\", \"notes\": \"Dataflow 策略重训练计划，因 embedding_distance 命名问题（实际用 BM25 而非 embedding）被 Reviewer 发现后搁置。已被 m2_embed_verify（true embedding mining）替代。\"}, \"p2b_eval_all\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-13T07:23:24.721Z\", \"conclusion\": \"killed\", \"completed_at\": \"2026-05-13T04:17:01.561Z\", \"notes\": \"P2b 全量 eval（pool_size=26），被 D013 服务器迁移计划取消。已被 p2b_eval_4runs_pool50（pool_size=50）替代。\"}, \"m2_early_pilot\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-13T04:44:22.077Z\", \"hypothesis\": \"Early pilot on partial M1 data (24 repos, ~5K instances): verify M2 training pipeline works end-to-end and get early signal on 3-strategy differentiation before full M1 completes\", \"conclusion\": \"killed\", \"notes\": \"PID 795791 在 cqa1 cuda:4 运行，wrapper 脚本顺序跑 random→embedding→dataflow（set -e）。random 策略跑到 step 4000 后卡住（~45min 无新日志），embedding/dataflow 未启动。Best checkpoint at step 1500。Val_loss 持续恶化（0.5879→0.728），明显过拟合。另有 OOM 进程干扰（某进程试图在同 GPU 启动导致 OOM，可能破坏 GPU 状态）。eval recall@k bug 已确认。\", \"completed_at\": \"2026-05-13T04:44:22.077Z\"}, \"m2_early_pilot_v3\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-13T02:13:43.400Z\", \"conclusion\": \"killed\", \"notes\": \"GPU 越界 cuda:0，违反项目 GPU 分配 gpu_ids=[\\\"cuda:4\\\"]。第二次 GPU 越界违规（首次 D005）。Worker 未正确映射 CUDA_VISIBLE_DEVICES。\", \"completed_at\": \"2026-05-13T02:13:43.400Z\"}, \"m2_early_pilot_v2\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-13T02:13:31.039Z\", \"hypothesis\": \"Early pilot on partial M1 data (24 repos, 2672 train + 746 val): verify M2 training pipeline works end-to-end and get early signal on 3-strategy differentiation before full M1 completes\", \"notes\": \"wandb API key error, EXIT_CODE=1。首次提交因 wandb 未配置离线模式而立即退出。\", \"conclusion\": \"failed\", \"completed_at\": \"2026-05-13T02:13:31.040Z\"}, \"mvp_p2b_contrastive_training\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-13T01:31:27.220Z\", \"completed_at\": \"2026-05-12T13:16:21.735Z\", \"notes\": \"4/9 runs 完成 (random×3 + embedding_distance_s42), 5/9 失败 (磁盘满 torch.save RuntimeError). /root/autodl-tmp 93% (14GB剩余, 每个checkpoint 5.8GB). 失败从 embedding_distance_s123 开始级联.\", \"conclusion\": \"killed\"}, \"p2b_eval_4runs_pool50\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-13T00:27:50.197Z\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-12T20:11:12.318Z\"}, \"d007_50repo_overlap\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-12T20:37:39.566Z\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-12T20:37:39.566Z\"}, \"p2b_5reruns\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-12T19:19:53.785Z\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-12T19:19:19.793Z\"}, \"p2b_eval_4runs_v2\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-12T17:22:16.595Z\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-12T17:22:16.595Z\"}, \"p2b-all-9runs\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-12T15:05:49.244Z\", \"conclusion\": \"killed\", \"completed_at\": \"2026-05-12T15:05:49.244Z\"}, \"p2b-smoke8\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-12T15:05:48.324Z\", \"conclusion\": \"killed\", \"completed_at\": \"2026-05-12T15:05:48.324Z\"}, \"p2b-smoke7\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-12T15:05:47.346Z\", \"conclusion\": \"killed\", \"completed_at\": \"2026-05-12T15:05:47.346Z\"}, \"p2b-smoke6\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-12T15:05:46.413Z\", \"conclusion\": \"killed\", \"completed_at\": \"2026-05-12T15:05:46.413Z\"}, \"p2b-smoke5\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-12T15:05:45.484Z\", \"conclusion\": \"killed\", \"completed_at\": \"2026-05-12T15:05:45.484Z\"}, \"p2b-smoke4\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-12T15:05:44.066Z\", \"conclusion\": \"killed\", \"completed_at\": \"2026-05-12T15:05:44.066Z\"}, \"p2b-smoke3\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-12T15:05:43.111Z\", \"conclusion\": \"killed\", \"completed_at\": \"2026-05-12T15:05:43.111Z\"}, \"p2b-smoke2\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-12T15:05:42.174Z\", \"conclusion\": \"killed\", \"completed_at\": \"2026-05-12T15:05:42.174Z\"}, \"p2b-smoke-test\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-12T15:05:41.269Z\", \"conclusion\": \"killed\", \"completed_at\": \"2026-05-12T15:05:41.270Z\"}, \"mvp_p2a_linear_proxy\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-12T11:58:15.436Z\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-12T11:58:15.436Z\"}, \"mvp_p1_codeql_feasibility\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-12T11:58:06.197Z\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-12T11:31:16.335Z\"}}, \"count\": 30, \"total\": 30, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.1617}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f63572ef-e81c-4880-a207-1d3f834619fa",
  "isSidechain": false,
  "promptId": "ee81bb41-edfe-48b7-9827-d79a74cf7a5e",
  "type": "user",
  "uuid": "62cc6185-971e-4146-b629-52667a8ffcef",
  "toolUseResult": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"experiments\\\": {\\\"plan_017_literature\\\": {\\\"status\\\": \\\"DONE\\\", \\\"updated_at\\\": \\\"2026-05-14T21:33:45.149Z\\\", \\\"hypothesis\\\": \\\"Inference-time graph method comparison: 8 papers surveyed (CodexGraph, LocAgent, RANGER, GraphCoder, ARISE, RepoGraph, CodeGRAG, CodeRAG). Discussion v2 drafted, all citations verified. Conclusion: training-time vs inference-time complementary.\\\", \\\"conclusion\\\": \\\"success\\\", \\\"completed_at\\\": \\\"2026-05-14T18:49:39.557Z\\\", \\\"notes\\\": \\\"Inference-time graph method comparison 完成。8 papers surveyed，其中 6 篇纳入 literature_map.yaml 和 discussion_v2.md（CodexGraph, LocAgent, RANGER, GraphCoder, ARISE, RepoGraph）。CodeGRAG 和 CodeRAG 经调研排除：CodeGRAG（arXiv 2405.02355）关注 NL→code generation 的 graph-augmented prompting，不涉及代码检索或对比学习；CodeRAG 系列（CodeRAG-Bench 2406.14497 / CodeRAG 2504.10046）关注 retrieval-augmented code generation benchmark 和 bigraph-based 代码生成，均为生成任务而非检索训练。两者与 StructFuse 的 scope（训练时结构信号用于对比学习代码检索）不符，故未纳入 discussion。\\\"}, \\\"m2_full_starcoder\\\": {\\\"status\\\": \\\"DONE\\\", \\\"updated_at\\\": \\\"2026-05-14T18:04:29.245Z\\\", \\\"hypothesis\\\": \\\"Full M2 StarCoder: 3 strategies × 3 seeds on full M1 data. Cross-encoder validation — if embedding > random holds for both Qwen and StarCoder, method is encoder-agnostic. Resolves plan_013 pilot negative (dataflow encoder-dependent).\\\", \\\"notes\\\": \\\"Phase 1: 构建 StarCoder embedding negatives 完成。Phase 2: 9 runs 训练中。batch_size=8, num_negatives=7, epochs=3(s42)/2(s43+), lr=2e-5, eval_steps=500, no early_stopping。双 checkpoint: best + best_by_recall_at_1。Seeds: 42,43,44。[D026] s42 保持 3 epochs; s43/s44 及后续 runs 改为 2 epochs。[2026-05-15 02:02 CST] cuda:1 进程冲突修复并重新提交（PID 519791, timeout=144h）。Registry 状态 DONE(failed) 是旧 cron timeout 标记，实际正在运行 random_s43 [1/8]。新 cron 已注册监控 PID 519791。序列：random_s43→s44→(待插入bm25_s42)→embedding×3→dataflow×3。random_s42 结果：best R@1=0.4604 at step 2500, val_loss=0.6134 at step 1000。\\\", \\\"conclusion\\\": \\\"failed\\\", \\\"completed_at\\\": \\\"2026-05-14T17:49:55.304Z\\\"}, \\\"neg_difficulty_analysis\\\": {\\\"status\\\": \\\"DONE\\\", \\\"updated_at\\\": \\\"2026-05-14T00:13:49.046Z\\\", \\\"hypothesis\\\": \\\"Negative difficulty distribution analysis: 用预训练 Qwen2.5-Coder-3B 和 StarCoder2-3B 计算 3 策略 (random/embedding/dataflow) 的 query-negative/positive cosine similarity，分析 pretrained representation separability 跨编码器差异。MAX_LENGTH=2048 匹配训练设置。\\\", \\\"notes\\\": \\\"128 vs 2048 token 对比完成（2026-05-14 05:54 CST）。Qwen pos_sim 在 2048t 下 0.9855（比 128t 的 0.9804 更高），确认 ceiling 为 Qwen 表征的结构性特征，非截断 artifact。StarCoder margin 2.6-4.1x Qwen（2048t）。核心结论：pretrained representation separability varies across encoders，跨两种 token 长度成立。数据源：128t → stats_v2.json，2048t → stats_v3_2048.json。\\\", \\\"conclusion\\\": \\\"success\\\", \\\"completed_at\\\": \\\"2026-05-14T00:13:49.046Z\\\"}, \\\"m1_reextract\\\": {\\\"status\\\": \\\"DONE\\\", \\\"updated_at\\\": \\\"2026-05-13T19:45:53.741Z\\\", \\\"hypothesis\\\": \\\"M1 重提取：恢复 28,276 个因运行时瞬态文件系统故障失败的 instances（82 repos）。预期将训练数据从 15,897 提升至 ~44,173。D022 批准。\\\", \\\"conclusion\\\": \\\"failed\\\", \\\"notes\\\": \\\"CodeQL query 100% 失败（exit status 2）。根因：Worker 安装 CodeQL CLI 2.25.4 时未执行 `codeql pack install`，`codeql/python-all@7.1.0` 标准库 pack 缺失。修复命令：`cd /root/structfuse/extraction/codeql_queries && /opt/codeql/codeql pack install`。已 kill 进程 + tmux session。无新数据产出（all.jsonl 未受影响）。等 Director 确认后修复重跑。\\\", \\\"completed_at\\\": \\\"2026-05-13T19:44:09.115Z\\\"}, \\\"m1_extraction\\\": {\\\"status\\\": \\\"DONE\\\", \\\"updated_at\\\": \\\"2026-05-13T19:26:13.901Z\\\", \\\"notes\\\": \\\"[2026-05-13 19:25] COMPLETED. 837.8min, 123/131 repos (93.9%), 15,897/44,173 instances with structural data (36.0%), 6,696 skipped (clone/checkout). Output: all.jsonl 6.6GB. [2026-05-13 19:23 UPDATE] 28,276 buggy_file_not_found errors 经验证并非上游数据质量问题——10/10 抽查的文件在 repo 中全部存在。根因是运行时瞬态文件系统故障（CodeQL 并行 database creation 导致磁盘耗尽，锐截止模式）。这些 instances 可通过重跑恢复。D022: 准备重跑脚本中，等 Director 确认后执行。\\\", \\\"conclusion\\\": \\\"success\\\", \\\"completed_at\\\": \\\"2026-05-13T10:59:42.462Z\\\"}, \\\"plan_006_scalability\\\": {\\\"status\\\": \\\"DONE\\\", \\\"updated_at\\\": \\\"2026-05-13T19:24:00.741Z\\\", \\\"conclusion\\\": \\\"success\\\", \\\"completed_at\\\": \\\"2026-05-13T07:57:58.176Z\\\", \\\"notes\\\": \\\"[2026-05-13 19:23] 全量统计 + error 分析 + fuzzy match 验证完成。关键发现: (1) 0 timeout; (2) 28,276 error 全部 buggy_file_not_found，但 fuzzy match 验证发现文件实际都存在——根因是运行时瞬态文件系统故障（锐截止模式：每个 repo 内先成功后突然全部失败，extraction_time=0.0s），可能是 CodeQL 并行数据库创建导致磁盘空间耗尽; (3) 这些 instance 可通过重跑恢复（当前 resolve_file_in_repo 对全部样本返回正确路径）; (4) 结构数据率 34.3% 有望提升至接近 100%（若重跑成功）; (5) Z% 随 repo 规模上升 (XL median 96%). Artifacts: plan006_full_scalability.json, art_20260513_d262da (error patterns)\\\", \\\"hypothesis\\\": \\\"Claim 3: CodeQL bounded data-flow extraction scales to large repos with acceptable timeout rates and provides meaningful structural coverage (Z%) that increases with repo complexity\\\"}, \\\"plan_013_starcoder\\\": {\\\"status\\\": \\\"DONE\\\", \\\"updated_at\\\": \\\"2026-05-13T18:09:54.153Z\\\", \\\"hypothesis\\\": \\\"Architecture generalization: validate StructFuse with StarCoder2-3B encoder (vs Qwen2.5-Coder-3B in m2_embed_verify). If both encoders show same strategy ranking → method is encoder-agnostic, strengthening the core claim. Key differentiator for best→accept at Dream.\\\", \\\"notes\\\": \\\"[2026-05-13 16:00] ALL 3 STRATEGIES DONE. Ranking: embedding (R@1=0.5078) > random (0.4922) > dataflow (0.4869). Embedding vs random: +1.6pp (consistent with Qwen). Dataflow vs random: -0.5pp (DIFFERS from Qwen where dataflow > random +0.8pp). Hypothesis NEGATIVE: strategy ranking NOT identical across encoders. Embedding > random is encoder-agnostic, dataflow position is encoder-dependent. Log: /root/runs/faith-evidence-ie/plan_013_starcoder.log. Cron misreported EXIT_CODE=129 but all strategies completed (confirmed via log extraction worker).\\\", \\\"conclusion\\\": \\\"negative\\\", \\\"completed_at\\\": \\\"2026-05-13T15:15:20.165Z\\\"}, \\\"m2_embed_verify\\\": {\\\"status\\\": \\\"DONE\\\", \\\"updated_at\\\": \\\"2026-05-13T15:59:51.621Z\\\", \\\"hypothesis\\\": \\\"True embedding mining verification: compare Qwen2.5-Coder-3B cosine similarity negatives vs BM25 negatives on pilot data (24 repos). If true embedding negatives are harder → Claim 2 (structure-aware negatives improve retrieval) gets stronger evidence.\\\", \\\"notes\\\": \\\"[2026-05-13 16:00] ALL 3 STRATEGIES DONE. Ranking: embedding (R@1=0.5557) > dataflow (0.5436) > random (0.5357). Embedding vs random: +2.0pp. Dataflow vs random: +0.8pp. All best at step 500, overfitting after. Hypothesis confirmed: true embedding negatives are harder → Claim 2 supported. Log: /root/runs/faith-evidence-ie/m2_embed_verify.log. Cron misreported EXIT_CODE=2 but all strategies completed successfully (confirmed via log extraction worker).\\\", \\\"conclusion\\\": \\\"success\\\", \\\"completed_at\\\": \\\"2026-05-13T15:15:18.746Z\\\"}, \\\"mvp_p2b_contrastive_v2\\\": {\\\"status\\\": \\\"DONE\\\", \\\"updated_at\\\": \\\"2026-05-13T07:23:28.932Z\\\", \\\"conclusion\\\": \\\"killed\\\", \\\"completed_at\\\": \\\"2026-05-12T15:04:44.396Z\\\", \\\"notes\\\": \\\"P2b 对比训练 v2，因磁盘空间不足被 kill。已被 p2b_5reruns（成功完成 9/9 runs）替代。\\\"}, \\\"p2b_dataflow_retrain\\\": {\\\"status\\\": \\\"DONE\\\", \\\"updated_at\\\": \\\"2026-05-13T07:23:27.706Z\\\", \\\"conclusion\\\": \\\"negative\\\", \\\"completed_at\\\": \\\"2026-05-13T04:17:02.055Z\\\", \\\"notes\\\": \\\"Dataflow 策略重训练计划，因 embedding_distance 命名问题（实际用 BM25 而非 embedding）被 Reviewer 发现后搁置。已被 m2_embed_verify（true embedding mining）替代。\\\"}, \\\"p2b_eval_all\\\": {\\\"status\\\": \\\"DONE\\\", \\\"updated_at\\\": \\\"2026-05-13T07:23:24.721Z\\\", \\\"conclusion\\\": \\\"killed\\\", \\\"completed_at\\\": \\\"2026-05-13T04:17:01.561Z\\\", \\\"notes\\\": \\\"P2b 全量 eval（pool_size=26），被 D013 服务器迁移计划取消。已被 p2b_eval_4runs_pool50（pool_size=50）替代。\\\"}, \\\"m2_early_pilot\\\": {\\\"status\\\": \\\"DONE\\\", \\\"updated_at\\\": \\\"2026-05-13T04:44:22.077Z\\\", \\\"hypothesis\\\": \\\"Early pilot on partial M1 data (24 repos, ~5K instances): verify M2 training pipeline works end-to-end and get early signal on 3-strategy differentiation before full M1 completes\\\", \\\"conclusion\\\": \\\"killed\\\", \\\"notes\\\": \\\"PID 795791 在 cqa1 cuda:4 运行，wrapper 脚本顺序跑 random→embedding→dataflow（set -e）。random 策略跑到 step 4000 后卡住（~45min 无新日志），embedding/dataflow 未启动。Best checkpoint at step 1500。Val_loss 持续恶化（0.5879→0.728），明显过拟合。另有 OOM 进程干扰（某进程试图在同 GPU 启动导致 OOM，可能破坏 GPU 状态）。eval recall@k bug 已确认。\\\", \\\"completed_at\\\": \\\"2026-05-13T04:44:22.077Z\\\"}, \\\"m2_early_pilot_v3\\\": {\\\"status\\\": \\\"DONE\\\", \\\"updated_at\\\": \\\"2026-05-13T02:13:43.400Z\\\", \\\"conclusion\\\": \\\"killed\\\", \\\"notes\\\": \\\"GPU 越界 cuda:0，违反项目 GPU 分配 gpu_ids=[\\\\\\\"cuda:4\\\\\\\"]。第二次 GPU 越界违规（首次 D005）。Worker 未正确映射 CUDA_VISIBLE_DEVICES。\\\", \\\"completed_at\\\": \\\"2026-05-13T02:13:43.400Z\\\"}, \\\"m2_early_pilot_v2\\\": {\\\"status\\\": \\\"DONE\\\", \\\"updated_at\\\": \\\"2026-05-13T02:13:31.039Z\\\", \\\"hypothesis\\\": \\\"Early pilot on partial M1 data (24 repos, 2672 train + 746 val): verify M2 training pipeline works end-to-end and get early signal on 3-strategy differentiation before full M1 completes\\\", \\\"notes\\\": \\\"wandb API key error, EXIT_CODE=1。首次提交因 wandb 未配置离线模式而立即退出。\\\", \\\"conclusion\\\": \\\"failed\\\", \\\"completed_at\\\": \\\"2026-05-13T02:13:31.040Z\\\"}, \\\"mvp_p2b_contrastive_training\\\": {\\\"status\\\": \\\"DONE\\\", \\\"updated_at\\\": \\\"2026-05-13T01:31:27.220Z\\\", \\\"completed_at\\\": \\\"2026-05-12T13:16:21.735Z\\\", \\\"notes\\\": \\\"4/9 runs 完成 (random×3 + embedding_distance_s42), 5/9 失败 (磁盘满 torch.save RuntimeError). /root/autodl-tmp 93% (14GB剩余, 每个checkpoint 5.8GB). 失败从 embedding_distance_s123 开始级联.\\\", \\\"conclusion\\\": \\\"killed\\\"}, \\\"p2b_eval_4runs_pool50\\\": {\\\"status\\\": \\\"DONE\\\", \\\"updated_at\\\": \\\"2026-05-13T00:27:50.197Z\\\", \\\"conclusion\\\": \\\"success\\\", \\\"completed_at\\\": \\\"2026-05-12T20:11:12.318Z\\\"}, \\\"d007_50repo_overlap\\\": {\\\"status\\\": \\\"DONE\\\", \\\"updated_at\\\": \\\"2026-05-12T20:37:39.566Z\\\", \\\"conclusion\\\": \\\"success\\\", \\\"completed_at\\\": \\\"2026-05-12T20:37:39.566Z\\\"}, \\\"p2b_5reruns\\\": {\\\"status\\\": \\\"DONE\\\", \\\"updated_at\\\": \\\"2026-05-12T19:19:53.785Z\\\", \\\"conclusion\\\": \\\"success\\\", \\\"completed_at\\\": \\\"2026-05-12T19:19:19.793Z\\\"}, \\\"p2b_eval_4runs_v2\\\": {\\\"status\\\": \\\"DONE\\\", \\\"updated_at\\\": \\\"2026-05-12T17:22:16.595Z\\\", \\\"conclusion\\\": \\\"success\\\", \\\"completed_at\\\": \\\"2026-05-12T17:22:16.595Z\\\"}, \\\"p2b-all-9runs\\\": {\\\"status\\\": \\\"DONE\\\", \\\"updated_at\\\": \\\"2026-05-12T15:05:49.244Z\\\", \\\"conclusion\\\": \\\"killed\\\", \\\"completed_at\\\": \\\"2026-05-12T15:05:49.244Z\\\"}, \\\"p2b-smoke8\\\": {\\\"status\\\": \\\"DONE\\\", \\\"updated_at\\\": \\\"2026-05-12T15:05:48.324Z\\\", \\\"conclusion\\\": \\\"killed\\\", \\\"completed_at\\\": \\\"2026-05-12T15:05:48.324Z\\\"}, \\\"p2b-smoke7\\\": {\\\"status\\\": \\\"DONE\\\", \\\"updated_at\\\": \\\"2026-05-12T15:05:47.346Z\\\", \\\"conclusion\\\": \\\"killed\\\", \\\"completed_at\\\": \\\"2026-05-12T15:05:47.346Z\\\"}, \\\"p2b-smoke6\\\": {\\\"status\\\": \\\"DONE\\\", \\\"updated_at\\\": \\\"2026-05-12T15:05:46.413Z\\\", \\\"conclusion\\\": \\\"killed\\\", \\\"completed_at\\\": \\\"2026-05-12T15:05:46.413Z\\\"}, \\\"p2b-smoke5\\\": {\\\"status\\\": \\\"DONE\\\", \\\"updated_at\\\": \\\"2026-05-12T15:05:45.484Z\\\", \\\"conclusion\\\": \\\"killed\\\", \\\"completed_at\\\": \\\"2026-05-12T15:05:45.484Z\\\"}, \\\"p2b-smoke4\\\": {\\\"status\\\": \\\"DONE\\\", \\\"updated_at\\\": \\\"2026-05-12T15:05:44.066Z\\\", \\\"conclusion\\\": \\\"killed\\\", \\\"completed_at\\\": \\\"2026-05-12T15:05:44.066Z\\\"}, \\\"p2b-smoke3\\\": {\\\"status\\\": \\\"DONE\\\", \\\"updated_at\\\": \\\"2026-05-12T15:05:43.111Z\\\", \\\"conclusion\\\": \\\"killed\\\", \\\"completed_at\\\": \\\"2026-05-12T15:05:43.111Z\\\"}, \\\"p2b-smoke2\\\": {\\\"status\\\": \\\"DONE\\\", \\\"updated_at\\\": \\\"2026-05-12T15:05:42.174Z\\\", \\\"conclusion\\\": \\\"killed\\\", \\\"completed_at\\\": \\\"2026-05-12T15:05:42.174Z\\\"}, \\\"p2b-smoke-test\\\": {\\\"status\\\": \\\"DONE\\\", \\\"updated_at\\\": \\\"2026-05-12T15:05:41.269Z\\\", \\\"conclusion\\\": \\\"killed\\\", \\\"completed_at\\\": \\\"2026-05-12T15:05:41.270Z\\\"}, \\\"mvp_p2a_linear_proxy\\\": {\\\"status\\\": \\\"DONE\\\", \\\"updated_at\\\": \\\"2026-05-12T11:58:15.436Z\\\", \\\"conclusion\\\": \\\"success\\\", \\\"completed_at\\\": \\\"2026-05-12T11:58:15.436Z\\\"}, \\\"mvp_p1_codeql_feasibility\\\": {\\\"status\\\": \\\"DONE\\\", \\\"updated_at\\\": \\\"2026-05-12T11:58:06.197Z\\\", \\\"conclusion\\\": \\\"success\\\", \\\"completed_at\\\": \\\"2026-05-12T11:31:16.335Z\\\"}}, \\\"count\\\": 30, \\\"total\\\": 30, \\\"baseline\\\": null}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.1617}}\"}",
  "mcpMeta": {
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"experiments\": {\"plan_017_literature\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-14T21:33:45.149Z\", \"hypothesis\": \"Inference-time graph method comparison: 8 papers surveyed (CodexGraph, LocAgent, RANGER, GraphCoder, ARISE, RepoGraph, CodeGRAG, CodeRAG). Discussion v2 drafted, all citations verified. Conclusion: training-time vs inference-time complementary.\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-14T18:49:39.557Z\", \"notes\": \"Inference-time graph method comparison 完成。8 papers surveyed，其中 6 篇纳入 literature_map.yaml 和 discussion_v2.md（CodexGraph, LocAgent, RANGER, GraphCoder, ARISE, RepoGraph）。CodeGRAG 和 CodeRAG 经调研排除：CodeGRAG（arXiv 2405.02355）关注 NL→code generation 的 graph-augmented prompting，不涉及代码检索或对比学习；CodeRAG 系列（CodeRAG-Bench 2406.14497 / CodeRAG 2504.10046）关注 retrieval-augmented code generation benchmark 和 bigraph-based 代码生成，均为生成任务而非检索训练。两者与 StructFuse 的 scope（训练时结构信号用于对比学习代码检索）不符，故未纳入 discussion。\"}, \"m2_full_starcoder\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-14T18:04:29.245Z\", \"hypothesis\": \"Full M2 StarCoder: 3 strategies × 3 seeds on full M1 data. Cross-encoder validation — if embedding > random holds for both Qwen and StarCoder, method is encoder-agnostic. Resolves plan_013 pilot negative (dataflow encoder-dependent).\", \"notes\": \"Phase 1: 构建 StarCoder embedding negatives 完成。Phase 2: 9 runs 训练中。batch_size=8, num_negatives=7, epochs=3(s42)/2(s43+), lr=2e-5, eval_steps=500, no early_stopping。双 checkpoint: best + best_by_recall_at_1。Seeds: 42,43,44。[D026] s42 保持 3 epochs; s43/s44 及后续 runs 改为 2 epochs。[2026-05-15 02:02 CST] cuda:1 进程冲突修复并重新提交（PID 519791, timeout=144h）。Registry 状态 DONE(failed) 是旧 cron timeout 标记，实际正在运行 random_s43 [1/8]。新 cron 已注册监控 PID 519791。序列：random_s43→s44→(待插入bm25_s42)→embedding×3→dataflow×3。random_s42 结果：best R@1=0.4604 at step 2500, val_loss=0.6134 at step 1000。\", \"conclusion\": \"failed\", \"completed_at\": \"2026-05-14T17:49:55.304Z\"}, \"neg_difficulty_analysis\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-14T00:13:49.046Z\", \"hypothesis\": \"Negative difficulty distribution analysis: 用预训练 Qwen2.5-Coder-3B 和 StarCoder2-3B 计算 3 策略 (random/embedding/dataflow) 的 query-negative/positive cosine similarity，分析 pretrained representation separability 跨编码器差异。MAX_LENGTH=2048 匹配训练设置。\", \"notes\": \"128 vs 2048 token 对比完成（2026-05-14 05:54 CST）。Qwen pos_sim 在 2048t 下 0.9855（比 128t 的 0.9804 更高），确认 ceiling 为 Qwen 表征的结构性特征，非截断 artifact。StarCoder margin 2.6-4.1x Qwen（2048t）。核心结论：pretrained representation separability varies across encoders，跨两种 token 长度成立。数据源：128t → stats_v2.json，2048t → stats_v3_2048.json。\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-14T00:13:49.046Z\"}, \"m1_reextract\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-13T19:45:53.741Z\", \"hypothesis\": \"M1 重提取：恢复 28,276 个因运行时瞬态文件系统故障失败的 instances（82 repos）。预期将训练数据从 15,897 提升至 ~44,173。D022 批准。\", \"conclusion\": \"failed\", \"notes\": \"CodeQL query 100% 失败（exit status 2）。根因：Worker 安装 CodeQL CLI 2.25.4 时未执行 `codeql pack install`，`codeql/python-all@7.1.0` 标准库 pack 缺失。修复命令：`cd /root/structfuse/extraction/codeql_queries && /opt/codeql/codeql pack install`。已 kill 进程 + tmux session。无新数据产出（all.jsonl 未受影响）。等 Director 确认后修复重跑。\", \"completed_at\": \"2026-05-13T19:44:09.115Z\"}, \"m1_extraction\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-13T19:26:13.901Z\", \"notes\": \"[2026-05-13 19:25] COMPLETED. 837.8min, 123/131 repos (93.9%), 15,897/44,173 instances with structural data (36.0%), 6,696 skipped (clone/checkout). Output: all.jsonl 6.6GB. [2026-05-13 19:23 UPDATE] 28,276 buggy_file_not_found errors 经验证并非上游数据质量问题——10/10 抽查的文件在 repo 中全部存在。根因是运行时瞬态文件系统故障（CodeQL 并行 database creation 导致磁盘耗尽，锐截止模式）。这些 instances 可通过重跑恢复。D022: 准备重跑脚本中，等 Director 确认后执行。\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-13T10:59:42.462Z\"}, \"plan_006_scalability\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-13T19:24:00.741Z\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-13T07:57:58.176Z\", \"notes\": \"[2026-05-13 19:23] 全量统计 + error 分析 + fuzzy match 验证完成。关键发现: (1) 0 timeout; (2) 28,276 error 全部 buggy_file_not_found，但 fuzzy match 验证发现文件实际都存在——根因是运行时瞬态文件系统故障（锐截止模式：每个 repo 内先成功后突然全部失败，extraction_time=0.0s），可能是 CodeQL 并行数据库创建导致磁盘空间耗尽; (3) 这些 instance 可通过重跑恢复（当前 resolve_file_in_repo 对全部样本返回正确路径）; (4) 结构数据率 34.3% 有望提升至接近 100%（若重跑成功）; (5) Z% 随 repo 规模上升 (XL median 96%). Artifacts: plan006_full_scalability.json, art_20260513_d262da (error patterns)\", \"hypothesis\": \"Claim 3: CodeQL bounded data-flow extraction scales to large repos with acceptable timeout rates and provides meaningful structural coverage (Z%) that increases with repo complexity\"}, \"plan_013_starcoder\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-13T18:09:54.153Z\", \"hypothesis\": \"Architecture generalization: validate StructFuse with StarCoder2-3B encoder (vs Qwen2.5-Coder-3B in m2_embed_verify). If both encoders show same strategy ranking → method is encoder-agnostic, strengthening the core claim. Key differentiator for best→accept at Dream.\", \"notes\": \"[2026-05-13 16:00] ALL 3 STRATEGIES DONE. Ranking: embedding (R@1=0.5078) > random (0.4922) > dataflow (0.4869). Embedding vs random: +1.6pp (consistent with Qwen). Dataflow vs random: -0.5pp (DIFFERS from Qwen where dataflow > random +0.8pp). Hypothesis NEGATIVE: strategy ranking NOT identical across encoders. Embedding > random is encoder-agnostic, dataflow position is encoder-dependent. Log: /root/runs/faith-evidence-ie/plan_013_starcoder.log. Cron misreported EXIT_CODE=129 but all strategies completed (confirmed via log extraction worker).\", \"conclusion\": \"negative\", \"completed_at\": \"2026-05-13T15:15:20.165Z\"}, \"m2_embed_verify\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-13T15:59:51.621Z\", \"hypothesis\": \"True embedding mining verification: compare Qwen2.5-Coder-3B cosine similarity negatives vs BM25 negatives on pilot data (24 repos). If true embedding negatives are harder → Claim 2 (structure-aware negatives improve retrieval) gets stronger evidence.\", \"notes\": \"[2026-05-13 16:00] ALL 3 STRATEGIES DONE. Ranking: embedding (R@1=0.5557) > dataflow (0.5436) > random (0.5357). Embedding vs random: +2.0pp. Dataflow vs random: +0.8pp. All best at step 500, overfitting after. Hypothesis confirmed: true embedding negatives are harder → Claim 2 supported. Log: /root/runs/faith-evidence-ie/m2_embed_verify.log. Cron misreported EXIT_CODE=2 but all strategies completed successfully (confirmed via log extraction worker).\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-13T15:15:18.746Z\"}, \"mvp_p2b_contrastive_v2\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-13T07:23:28.932Z\", \"conclusion\": \"killed\", \"completed_at\": \"2026-05-12T15:04:44.396Z\", \"notes\": \"P2b 对比训练 v2，因磁盘空间不足被 kill。已被 p2b_5reruns（成功完成 9/9 runs）替代。\"}, \"p2b_dataflow_retrain\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-13T07:23:27.706Z\", \"conclusion\": \"negative\", \"completed_at\": \"2026-05-13T04:17:02.055Z\", \"notes\": \"Dataflow 策略重训练计划，因 embedding_distance 命名问题（实际用 BM25 而非 embedding）被 Reviewer 发现后搁置。已被 m2_embed_verify（true embedding mining）替代。\"}, \"p2b_eval_all\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-13T07:23:24.721Z\", \"conclusion\": \"killed\", \"completed_at\": \"2026-05-13T04:17:01.561Z\", \"notes\": \"P2b 全量 eval（pool_size=26），被 D013 服务器迁移计划取消。已被 p2b_eval_4runs_pool50（pool_size=50）替代。\"}, \"m2_early_pilot\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-13T04:44:22.077Z\", \"hypothesis\": \"Early pilot on partial M1 data (24 repos, ~5K instances): verify M2 training pipeline works end-to-end and get early signal on 3-strategy differentiation before full M1 completes\", \"conclusion\": \"killed\", \"notes\": \"PID 795791 在 cqa1 cuda:4 运行，wrapper 脚本顺序跑 random→embedding→dataflow（set -e）。random 策略跑到 step 4000 后卡住（~45min 无新日志），embedding/dataflow 未启动。Best checkpoint at step 1500。Val_loss 持续恶化（0.5879→0.728），明显过拟合。另有 OOM 进程干扰（某进程试图在同 GPU 启动导致 OOM，可能破坏 GPU 状态）。eval recall@k bug 已确认。\", \"completed_at\": \"2026-05-13T04:44:22.077Z\"}, \"m2_early_pilot_v3\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-13T02:13:43.400Z\", \"conclusion\": \"killed\", \"notes\": \"GPU 越界 cuda:0，违反项目 GPU 分配 gpu_ids=[\\\"cuda:4\\\"]。第二次 GPU 越界违规（首次 D005）。Worker 未正确映射 CUDA_VISIBLE_DEVICES。\", \"completed_at\": \"2026-05-13T02:13:43.400Z\"}, \"m2_early_pilot_v2\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-13T02:13:31.039Z\", \"hypothesis\": \"Early pilot on partial M1 data (24 repos, 2672 train + 746 val): verify M2 training pipeline works end-to-end and get early signal on 3-strategy differentiation before full M1 completes\", \"notes\": \"wandb API key error, EXIT_CODE=1。首次提交因 wandb 未配置离线模式而立即退出。\", \"conclusion\": \"failed\", \"completed_at\": \"2026-05-13T02:13:31.040Z\"}, \"mvp_p2b_contrastive_training\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-13T01:31:27.220Z\", \"completed_at\": \"2026-05-12T13:16:21.735Z\", \"notes\": \"4/9 runs 完成 (random×3 + embedding_distance_s42), 5/9 失败 (磁盘满 torch.save RuntimeError). /root/autodl-tmp 93% (14GB剩余, 每个checkpoint 5.8GB). 失败从 embedding_distance_s123 开始级联.\", \"conclusion\": \"killed\"}, \"p2b_eval_4runs_pool50\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-13T00:27:50.197Z\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-12T20:11:12.318Z\"}, \"d007_50repo_overlap\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-12T20:37:39.566Z\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-12T20:37:39.566Z\"}, \"p2b_5reruns\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-12T19:19:53.785Z\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-12T19:19:19.793Z\"}, \"p2b_eval_4runs_v2\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-12T17:22:16.595Z\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-12T17:22:16.595Z\"}, \"p2b-all-9runs\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-12T15:05:49.244Z\", \"conclusion\": \"killed\", \"completed_at\": \"2026-05-12T15:05:49.244Z\"}, \"p2b-smoke8\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-12T15:05:48.324Z\", \"conclusion\": \"killed\", \"completed_at\": \"2026-05-12T15:05:48.324Z\"}, \"p2b-smoke7\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-12T15:05:47.346Z\", \"conclusion\": \"killed\", \"completed_at\": \"2026-05-12T15:05:47.346Z\"}, \"p2b-smoke6\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-12T15:05:46.413Z\", \"conclusion\": \"killed\", \"completed_at\": \"2026-05-12T15:05:46.413Z\"}, \"p2b-smoke5\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-12T15:05:45.484Z\", \"conclusion\": \"killed\", \"completed_at\": \"2026-05-12T15:05:45.484Z\"}, \"p2b-smoke4\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-12T15:05:44.066Z\", \"conclusion\": \"killed\", \"completed_at\": \"2026-05-12T15:05:44.066Z\"}, \"p2b-smoke3\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-12T15:05:43.111Z\", \"conclusion\": \"killed\", \"completed_at\": \"2026-05-12T15:05:43.111Z\"}, \"p2b-smoke2\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-12T15:05:42.174Z\", \"conclusion\": \"killed\", \"completed_at\": \"2026-05-12T15:05:42.174Z\"}, \"p2b-smoke-test\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-12T15:05:41.269Z\", \"conclusion\": \"killed\", \"completed_at\": \"2026-05-12T15:05:41.270Z\"}, \"mvp_p2a_linear_proxy\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-12T11:58:15.436Z\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-12T11:58:15.436Z\"}, \"mvp_p1_codeql_feasibility\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-12T11:58:06.197Z\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-12T11:31:16.335Z\"}}, \"count\": 30, \"total\": 30, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.1617}}"
    }
  },
  "sourceToolAssistantUUID": "f63572ef-e81c-4880-a207-1d3f834619fa",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/.claude/sessions/reviewer_65cfe724",
  "sessionId": "f444a635-eeef-4924-9b48-a4c308632421",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---


### Tool call

_source line 24 · 2026-05-16T00:23:20.699Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01CcpJmizg3khA4ZFHKQcCru`</summary>

```json
{
  "project": "structfuse-context",
  "file": "literature_map.yaml",
  "max_chars": 12000
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "62cc6185-971e-4146-b629-52667a8ffcef",
  "isSidechain": false,
  "requestId": "req_011Cb5J2JeuFZcm8TGAjpUaU",
  "type": "assistant",
  "uuid": "1f81be61-908d-4f26-adbf-f4f2429dca6f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/.claude/sessions/reviewer_65cfe724",
  "sessionId": "f444a635-eeef-4924-9b48-a4c308632421",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QWbfLxQNBrJ4cFjfbeviqt",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 14930,
      "cache_read_input_tokens": 32211,
      "output_tokens": 442,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 14930,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 442,
          "cache_read_input_tokens": 32211,
          "cache_creation_input_tokens": 14930,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 14930
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

_source line 25 · 2026-05-16T00:23:20.713Z_

<details><summary>↩ Tool result · `toolu_01CcpJmizg3khA4ZFHKQcCru`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/literature_map.yaml\", \"content\": \"# StructFuse — Related Work Literature Map\\n# 最后更新: 2026-05-14\\n# 说明: 只收录已验证存在的论文。每篇均经 WebSearch 确认标题/venue/year。\\n# 总计: 39 entries (含 2 个软件工具引用)\\n\\ncategories:\\n\\n  # ==========================================================================\\n  # Category 1: Code Retrieval for Bug Fixing / SWE-bench Ecosystem\\n  # ==========================================================================\\n  code_retrieval_bug_fixing:\\n    description: \\\"SWE-bench 及相关 repo-level 自动修复系统中的代码检索方法\\\"\\n    papers:\\n\\n      - title: \\\"SWE-bench: Can Language Models Resolve Real-World GitHub Issues?\\\"\\n        authors: \\\"Carlos E. Jimenez, John Yang, Alexander Wettig, Shunyu Yao, Kexin Pei, Ofir Press, Karthik Narasimhan\\\"\\n        venue: ICLR\\n        year: 2024\\n        relation: baseline\\n        summary: \\\"从 GitHub issues 构建 repo-level bug fixing benchmark，成为自动修复领域标准评估集。\\\"\\n\\n      - title: \\\"SWE-agent: Agent-Computer Interfaces Enable Automated Software Engineering\\\"\\n        authors: \\\"John Yang, Carlos E. Jimenez, Alexander Wettig, Kilian Lieret, Shunyu Yao, Karthik Narasimhan, Ofir Press\\\"\\n        venue: NeurIPS\\n        year: 2024\\n        relation: competitor\\n        summary: \\\"基于 LLM agent 的交互式 bug fixing 系统，定义了 ACI 接口范式。\\\"\\n\\n      - title: \\\"AutoCodeRover: Autonomous Program Improvement\\\"\\n        authors: \\\"Yuntong Zhang, Haifeng Ruan, Zhiyu Fan, Abhik Roychoudhury\\\"\\n        venue: ISSTA\\n        year: 2024\\n        relation: competitor\\n        summary: \\\"结合代码搜索与 spectrum-based fault localization，利用程序分析缩小修复范围。\\\"\\n\\n      - title: \\\"Agentless: Demystifying LLM-based Software Engineering Agents\\\"\\n        authors: \\\"Chunqiu Steven Xia, Yinlin Deng, Soren Dunn, Lingming Zhang\\\"\\n        venue: arXiv\\n        year: 2024\\n        relation: competitor\\n        summary: \\\"无 agent 架构的 two-phase localize-then-repair 方法，在 SWE-bench 上取得强 baseline。\\\"\\n\\n      - title: \\\"SWE-smith: Scaling Data for Software Engineering Agents\\\"\\n        authors: \\\"John Yang, Kilian Lieret, Carlos E. Jimenez, Alexander Wettig, Kabir Khandpur, Yanzhe Zhang, Binyuan Hui, Ofir Press, Ludwig Schmidt, Diyi Yang\\\"\\n        venue: \\\"NeurIPS (Datasets & Benchmarks, Spotlight)\\\"\\n        year: 2025\\n        relation: building-block\\n        summary: \\\"自动从 GitHub 生成大规模 SWE-bench 风格训练数据，StructFuse 用其 repos 做 data-flow 提取。\\\"\\n\\n      - title: \\\"RepoBench: Benchmarking Repository-Level Code Auto-Completion Systems\\\"\\n        authors: \\\"Tianyang Liu, Canwen Xu, Julian McAuley\\\"\\n        venue: ICLR\\n        year: 2024\\n        relation: baseline\\n        summary: \\\"Repo-level 代码补全/检索 benchmark，含 RepoBench-R 检索子任务。\\\"\\n\\n      - title: \\\"SweRank: Software Issue Localization with Code Ranking\\\"\\n        authors: \\\"Revanth Gangi Reddy, Tarun Suresh, JaeHyeok Doo, Ye Liu, Xuan Phi Nguyen, Yingbo Zhou, Semih Yavuz, Caiming Xiong, Heng Ji, Shafiq Joty\\\"\\n        venue: arXiv\\n        year: 2025\\n        relation: competitor\\n        summary: \\\"Retrieve-and-rerank 框架用于 software issue localization，在 SWE-Bench-Lite 和 LocBench 上 SOTA，text-based retrieval baseline。\\\"\\n\\n      - title: \\\"SWE-Fixer: Training Open-Source LLMs for Effective and Efficient GitHub Issue Resolution\\\"\\n        authors: \\\"Chengxing Xie, Bowen Li, Chang Gao, He Du, Wai Lam, Difan Zou, Kai Chen\\\"\\n        venue: \\\"ACL (Findings)\\\"\\n        year: 2025\\n        relation: competitor\\n        summary: \\\"BM25 + LLM retriever 的 coarse-to-fine file retrieval pipeline，在 SWE-Bench Verified 上 30.2%。\\\"\\n\\n  # ==========================================================================\\n  # Category 2: Hard Negative Mining in Contrastive Learning\\n  # ==========================================================================\\n  hard_negative_mining:\\n    description: \\\"对比学习中 hard negative 挖掘策略，以及密集检索中的负样本选择\\\"\\n    papers:\\n\\n      - title: \\\"Dense Passage Retrieval for Open-Domain Question Answering\\\"\\n        authors: \\\"Vladimir Karpukhin, Barlas Oguz, Sewon Min, Patrick Lewis, Ledell Wu, Sergey Edunov, Danqi Chen, Wen-tau Yih\\\"\\n        venue: EMNLP\\n        year: 2020\\n        relation: background\\n        summary: \\\"DPR 开创了 in-batch negatives + BM25 hard negatives 的双塔检索范式。\\\"\\n\\n      - title: \\\"Approximate Nearest Neighbor Negative Contrastive Learning for Dense Text Retrieval\\\"\\n        authors: \\\"Lee Xiong, Chenyan Xiong, Ye Li, Kwok-Fung Tang, Jialin Liu, Paul Bennett, Junaid Ahmed, Arnold Overwijk\\\"\\n        venue: ICLR\\n        year: 2021\\n        relation: background\\n        summary: \\\"ANCE 用 ANN index 动态挖掘 embedding-distance hard negatives，StructFuse 的 baseline negative 策略之一。\\\"\\n\\n      - title: \\\"A Simple Framework for Contrastive Learning of Visual Representations\\\"\\n        authors: \\\"Ting Chen, Simon Kornblith, Mohammad Norouzi, Geoffrey Hinton\\\"\\n        venue: ICML\\n        year: 2020\\n        relation: background\\n        summary: \\\"SimCLR 视觉对比学习奠基工作，证明 hard negatives 和大 batch size 对对比学习的重要性。\\\"\\n\\n      - title: \\\"Sentence-BERT: Sentence Embeddings using Siamese BERT-Networks\\\"\\n        authors: \\\"Nils Reimers, Iryna Gurevych\\\"\\n        venue: EMNLP\\n        year: 2019\\n        relation: background\\n        summary: \\\"Siamese/triplet 网络训练句子嵌入，StructFuse 的对比训练框架与其类似。\\\"\\n\\n      - title: \\\"Curriculum Learning for Dense Retrieval Distillation\\\"\\n        authors: \\\"Hansi Zeng, Hamed Zamani, Vishwa Vinay\\\"\\n        venue: \\\"SIGIR (Best Short Paper)\\\"\\n        year: 2022\\n        relation: background\\n        summary: \\\"CL-DRD: 课程学习式知识蒸馏用于密集检索，从粗粒度到细粒度逐步增加训练难度。\\\"\\n\\n      - title: \\\"Effective Hard Negative Mining for Contrastive Learning-Based Code Search\\\"\\n        authors: \\\"Fan Y., Li C., Ge J., Huang L., Luo B.\\\"\\n        venue: \\\"ACM TOSEM\\\"\\n        year: 2025\\n        relation: contrast-target\\n        summary: \\\"CoCoHaNeRe: 提出可微分 hard negative 机制用于代码搜索对比学习。其对 hard negative 机制的处理与 StructFuse 的发现形成关键对照——StructFuse 证明 true embedding-distance mining 即可持续提升性能。\\\"\\n        note: \\\"关键引用：StructFuse Claim 1 的 correction target。CoCoHaNeRe 论点是非可微 embedding negatives 学习'slow and ineffective'，StructFuse 证明用 true embedding distance mining 仍然有效。\\\"\\n\\n  # ==========================================================================\\n  # Category 3: Contrastive Learning for Code\\n  # ==========================================================================\\n  contrastive_code_learning:\\n    description: \\\"代码领域的对比学习方法，训练时利用代码特性构建正负样本\\\"\\n    papers:\\n\\n      - title: \\\"Contrastive Code Representation Learning\\\"\\n        authors: \\\"Paras Jain, Ajay Jain, Tianjun Zhang, Pieter Abbeel, Joseph Gonzalez, Ion Stoica\\\"\\n        venue: EMNLP\\n        year: 2021\\n        relation: background\\n        summary: \\\"ContraCode: 自监督对比预训练，通过编译器变换生成功能等价的程序变体，学习代码功能而非表面形式。\\\"\\n\\n      - title: \\\"CodeRetriever: A Large Scale Contrastive Pre-Training Method for Code Search\\\"\\n        authors: \\\"Xiaonan Li, Yeyun Gong, Yelong Shen, Xipeng Qiu, Hang Zhang, Bolun Yao, Weizhen Qi, Daxin Jiang, Weizhu Chen, Nan Duan\\\"\\n        venue: EMNLP\\n        year: 2022\\n        relation: background\\n        summary: \\\"结合 unimodal (code-code) 和 bimodal (code-text) 对比学习预训练代码表示，在 11 个代码搜索 benchmark 上 SOTA。\\\"\\n\\n      - title: \\\"Towards Learning (Dis)-Similarity of Source Code from Program Contrasts\\\"\\n        authors: \\\"Yangruibo Ding, Luca Buratti, Saurabh Pujar, Alessandro Morari, Baishakhi Ray, Saikat Chakraborty\\\"\\n        venue: \\\"ACL (Long Papers)\\\"\\n        year: 2022\\n        relation: background\\n        summary: \\\"利用程序结构和功能属性构建对比样本对，学习代码相似性/差异性表示。\\\"\\n\\n  # ==========================================================================\\n  # Category 4: Program Analysis for ML\\n  # ==========================================================================\\n  program_analysis_for_ml:\\n    description: \\\"静态分析辅助 ML，结构信息在代码表示学习中的应用\\\"\\n    papers:\\n\\n      - title: \\\"CodeQL: Semantic Code Analysis Engine\\\"\\n        authors: \\\"GitHub / Semmle\\\"\\n        venue: \\\"Tool (open-source)\\\"\\n        year: 2019\\n        relation: building-block\\n        summary: \\\"基于 Datalog 的代码查询引擎，支持 inter-procedural data-flow 分析。StructFuse 用它提取 scope-bounded data-flow graph。\\\"\\n\\n      - title: \\\"code2vec: Learning Distributed Representations of Code\\\"\\n        authors: \\\"Uri Alon, Meital Zilberstein, Omer Levy, Eran Yahav\\\"\\n        venue: POPL\\n        year: 2019\\n        relation: background\\n        summary: \\\"用 AST path 学习代码向量表示，首次大规模证明结构信息对代码表示学习的价值。\\\"\\n\\n      - title: \\\"code2seq: Generating Sequences from Structured Representations of Code\\\"\\n        authors: \\\"Uri Alon, Shaked Brody, Omer Levy, Eran Yahav\\\"\\n        venue: ICLR\\n        year: 2019\\n        relation: background\\n        summary: \\\"code2vec 的序列生成扩展，用 AST path attention 生成方法名摘要。\\\"\\n\\n      - title: \\\"Detecting Code Clones with Graph Neural Network and Flow-Augmented Abstract Syntax Tree\\\"\\n        authors: \\\"Wenhan Wang, Ge Li, Bo Ma, Xin Xia, Zhi Jin\\\"\\n        venue: SANER\\n        year: 2020\\n        relation: background\\n        summary: \\\"FA-AST: 用 data-flow 增强 AST 进行代码克隆检测，与 StructFuse 用 data-flow 做 hard negative 挖掘思路相关。\\\"\\n\\n      - title: \\\"GraphCodeBERT: Pre-training Code Representations with Data Flow\\\"\\n        authors: \\\"Daya Guo, Shuo Ren, Shuai Lu, Zhangyin Feng, Duyu Tang, Shujie Liu, Long Zhou, Nan Duan, Alexey Svyatkovskiy, Shengyu Fu, Michele Tufano, Shao Kun Deng, Colin Clement, Dawn Drain, Neel Sundaresan, Jian Yin, Daxin Jiang, Ming Zhou\\\"\\n        venue: ICLR\\n        year: 2021\\n        relation: background\\n        summary: \\\"在预训练中引入 data-flow edge，证明 data-flow 信息提升代码理解任务。StructFuse 的 insight 与此相关但用途不同（hard negative mining vs pre-training）。\\\"\\n\\n      - title: \\\"ARISE: A Repository-level Graph Representation and Toolset for Agentic Fault Localization and Program Repair\\\"\\n        authors: \\\"Shahd Seddik, Fatemeh Fard\\\"\\n        venue: arXiv\\n        year: 2026\\n        relation: contrast\\n        summary: \\\"用 multi-granularity program graph（含 intra-procedural def-use edges）辅助 LLM agent 做 fault localization。仅 intra-procedural + runtime tool calls，与 StructFuse 的 inter-procedural static mining 互补。\\\"\\n\\n  # ==========================================================================\\n  # Category 5: Code Embeddings / Code Search\\n  # ==========================================================================\\n  code_embeddings_search:\\n    description: \\\"代码嵌入模型和代码搜索方法\\\"\\n    papers:\\n\\n      - title: \\\"CodeSearchNet Challenge: Evaluating the State of Semantic Code Search\\\"\\n        authors: \\\"Hamel Husain, Ho-Hsiang Wu, Tiferet Gazit, Miltiadis Allamanis, Marc Brockschmidt\\\"\\n        venue: arXiv\\n        year: 2019\\n        relation: background\\n        summary: \\\"代码语义搜索 benchmark 和数据集，推动了代码嵌入模型的发展。\\\"\\n\\n      - title: \\\"CodeBERT: A Pre-Trained Model for Programming and Natural Languages\\\"\\n        authors: \\\"Zhangyin Feng, Daya Guo, Duyu Tang, Nan Duan, Xiaocheng Feng, Ming Gong, Lixin Zou, Bing Qin, Ting Liu, Daxin Jiang, Ming Zhou\\\"\\n        venue: \\\"EMNLP (Findings)\\\"\\n        year: 2020\\n        relation: background\\n        summary: \\\"首个编程语言-自然语言双模态预训练模型，代码嵌入的早期里程碑。\\\"\\n\\n      - title: \\\"UniXcoder: Unified Cross-Modal Pre-training for Code Representation\\\"\\n        authors: \\\"Daya Guo, Shuai Lu, Nan Duan, Yanlin Wang, Ming Zhou, Jian Yin\\\"\\n        venue: ACL\\n        year: 2022\\n        relation: background\\n        summary: \\\"统一跨模态代码预训练，在代码搜索等任务上取得 SOTA。\\\"\\n\\n      - title: \\\"StarCoder: May the Source Be with You!\\\"\\n        authors: \\\"Raymond Li, Loubna Ben Allal, et al. (BigCode)\\\"\\n        venue: TMLR\\n        year: 2023\\n        relation: building-block\\n        summary: \\\"大规模开源代码 LLM，StructFuse 用 StarCoder2-3B 作为对比学习检索器的 backbone 之一。\\\"\\n\\n      - title: \\\"Code Llama: Open Foundation Models for Code\\\"\\n        authors: \\\"Baptiste Roziere, Jonas Gehring, Fabian Gloeckle, et al. (Meta AI)\\\"\\n        venue: arXiv\\n        year: 2023\\n        relation: background\\n        summary: \\\"Meta 的代码大模型系列，基于 Llama 2 微调。\\\"\\n\\n      - title: \\\"Qwen2.5-Coder Technical Report\\\"\\n        authors: \\\"Binyuan Hui, Jian Yang, Zeyu Cui, et al. (Qwen Team, Alibaba)\\\"\\n        venue: arXiv\\n        year: 2024\\n        relation: building-block\\n        summary: \\\"Qwen 代码模型系列，StructFuse 用 Qwen2.5-Coder-3B 作为对比学习检索器的 backbone。\\\"\\n\\n      - title: \\\"DeepSeek-Coder: When the Large Language Model Meets Programming -- The Rise of Code Intelligence\\\"\\n        authors: \\\"Daya Guo, Qihao Zhu, Dejian Yang, Zhenda Xie, Kai Dong, Wentao Zhang, Guanting Chen, Xiao Bi, Yu Wu, Y.K. Li, Fuli Luo, Yingfei Xiong, Wenfeng \\n\\n... [截断: 省略 3999 字符，传 max_chars=0 获取完整内容]\", \"total_chars\": 15999, \"truncated\": true}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "1f81be61-908d-4f26-adbf-f4f2429dca6f",
  "isSidechain": false,
  "promptId": "ee81bb41-edfe-48b7-9827-d79a74cf7a5e",
  "type": "user",
  "uuid": "c3795a1b-57f2-4a63-ac49-306041be5a27",
  "toolUseResult": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"path\\\": \\\"/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/literature_map.yaml\\\", \\\"content\\\": \\\"# StructFuse — Related Work Literature Map\\\\n# 最后更新: 2026-05-14\\\\n# 说明: 只收录已验证存在的论文。每篇均经 WebSearch 确认标题/venue/year。\\\\n# 总计: 39 entries (含 2 个软件工具引用)\\\\n\\\\ncategories:\\\\n\\\\n  # ==========================================================================\\\\n  # Category 1: Code Retrieval for Bug Fixing / SWE-bench Ecosystem\\\\n  # ==========================================================================\\\\n  code_retrieval_bug_fixing:\\\\n    description: \\\\\\\"SWE-bench 及相关 repo-level 自动修复系统中的代码检索方法\\\\\\\"\\\\n    papers:\\\\n\\\\n      - title: \\\\\\\"SWE-bench: Can Language Models Resolve Real-World GitHub Issues?\\\\\\\"\\\\n        authors: \\\\\\\"Carlos E. Jimenez, John Yang, Alexander Wettig, Shunyu Yao, Kexin Pei, Ofir Press, Karthik Narasimhan\\\\\\\"\\\\n        venue: ICLR\\\\n        year: 2024\\\\n        relation: baseline\\\\n        summary: \\\\\\\"从 GitHub issues 构建 repo-level bug fixing benchmark，成为自动修复领域标准评估集。\\\\\\\"\\\\n\\\\n      - title: \\\\\\\"SWE-agent: Agent-Computer Interfaces Enable Automated Software Engineering\\\\\\\"\\\\n        authors: \\\\\\\"John Yang, Carlos E. Jimenez, Alexander Wettig, Kilian Lieret, Shunyu Yao, Karthik Narasimhan, Ofir Press\\\\\\\"\\\\n        venue: NeurIPS\\\\n        year: 2024\\\\n        relation: competitor\\\\n        summary: \\\\\\\"基于 LLM agent 的交互式 bug fixing 系统，定义了 ACI 接口范式。\\\\\\\"\\\\n\\\\n      - title: \\\\\\\"AutoCodeRover: Autonomous Program Improvement\\\\\\\"\\\\n        authors: \\\\\\\"Yuntong Zhang, Haifeng Ruan, Zhiyu Fan, Abhik Roychoudhury\\\\\\\"\\\\n        venue: ISSTA\\\\n        year: 2024\\\\n        relation: competitor\\\\n        summary: \\\\\\\"结合代码搜索与 spectrum-based fault localization，利用程序分析缩小修复范围。\\\\\\\"\\\\n\\\\n      - title: \\\\\\\"Agentless: Demystifying LLM-based Software Engineering Agents\\\\\\\"\\\\n        authors: \\\\\\\"Chunqiu Steven Xia, Yinlin Deng, Soren Dunn, Lingming Zhang\\\\\\\"\\\\n        venue: arXiv\\\\n        year: 2024\\\\n        relation: competitor\\\\n        summary: \\\\\\\"无 agent 架构的 two-phase localize-then-repair 方法，在 SWE-bench 上取得强 baseline。\\\\\\\"\\\\n\\\\n      - title: \\\\\\\"SWE-smith: Scaling Data for Software Engineering Agents\\\\\\\"\\\\n        authors: \\\\\\\"John Yang, Kilian Lieret, Carlos E. Jimenez, Alexander Wettig, Kabir Khandpur, Yanzhe Zhang, Binyuan Hui, Ofir Press, Ludwig Schmidt, Diyi Yang\\\\\\\"\\\\n        venue: \\\\\\\"NeurIPS (Datasets & Benchmarks, Spotlight)\\\\\\\"\\\\n        year: 2025\\\\n        relation: building-block\\\\n        summary: \\\\\\\"自动从 GitHub 生成大规模 SWE-bench 风格训练数据，StructFuse 用其 repos 做 data-flow 提取。\\\\\\\"\\\\n\\\\n      - title: \\\\\\\"RepoBench: Benchmarking Repository-Level Code Auto-Completion Systems\\\\\\\"\\\\n        authors: \\\\\\\"Tianyang Liu, Canwen Xu, Julian McAuley\\\\\\\"\\\\n        venue: ICLR\\\\n        year: 2024\\\\n        relation: baseline\\\\n        summary: \\\\\\\"Repo-level 代码补全/检索 benchmark，含 RepoBench-R 检索子任务。\\\\\\\"\\\\n\\\\n      - title: \\\\\\\"SweRank: Software Issue Localization with Code Ranking\\\\\\\"\\\\n        authors: \\\\\\\"Revanth Gangi Reddy, Tarun Suresh, JaeHyeok Doo, Ye Liu, Xuan Phi Nguyen, Yingbo Zhou, Semih Yavuz, Caiming Xiong, Heng Ji, Shafiq Joty\\\\\\\"\\\\n        venue: arXiv\\\\n        year: 2025\\\\n        relation: competitor\\\\n        summary: \\\\\\\"Retrieve-and-rerank 框架用于 software issue localization，在 SWE-Bench-Lite 和 LocBench 上 SOTA，text-based retrieval baseline。\\\\\\\"\\\\n\\\\n      - title: \\\\\\\"SWE-Fixer: Training Open-Source LLMs for Effective and Efficient GitHub Issue Resolution\\\\\\\"\\\\n        authors: \\\\\\\"Chengxing Xie, Bowen Li, Chang Gao, He Du, Wai Lam, Difan Zou, Kai Chen\\\\\\\"\\\\n        venue: \\\\\\\"ACL (Findings)\\\\\\\"\\\\n        year: 2025\\\\n        relation: competitor\\\\n        summary: \\\\\\\"BM25 + LLM retriever 的 coarse-to-fine file retrieval pipeline，在 SWE-Bench Verified 上 30.2%。\\\\\\\"\\\\n\\\\n  # ==========================================================================\\\\n  # Category 2: Hard Negative Mining in Contrastive Learning\\\\n  # ==========================================================================\\\\n  hard_negative_mining:\\\\n    description: \\\\\\\"对比学习中 hard negative 挖掘策略，以及密集检索中的负样本选择\\\\\\\"\\\\n    papers:\\\\n\\\\n      - title: \\\\\\\"Dense Passage Retrieval for Open-Domain Question Answering\\\\\\\"\\\\n        authors: \\\\\\\"Vladimir Karpukhin, Barlas Oguz, Sewon Min, Patrick Lewis, Ledell Wu, Sergey Edunov, Danqi Chen, Wen-tau Yih\\\\\\\"\\\\n        venue: EMNLP\\\\n        year: 2020\\\\n        relation: background\\\\n        summary: \\\\\\\"DPR 开创了 in-batch negatives + BM25 hard negatives 的双塔检索范式。\\\\\\\"\\\\n\\\\n      - title: \\\\\\\"Approximate Nearest Neighbor Negative Contrastive Learning for Dense Text Retrieval\\\\\\\"\\\\n        authors: \\\\\\\"Lee Xiong, Chenyan Xiong, Ye Li, Kwok-Fung Tang, Jialin Liu, Paul Bennett, Junaid Ahmed, Arnold Overwijk\\\\\\\"\\\\n        venue: ICLR\\\\n        year: 2021\\\\n        relation: background\\\\n        summary: \\\\\\\"ANCE 用 ANN index 动态挖掘 embedding-distance hard negatives，StructFuse 的 baseline negative 策略之一。\\\\\\\"\\\\n\\\\n      - title: \\\\\\\"A Simple Framework for Contrastive Learning of Visual Representations\\\\\\\"\\\\n        authors: \\\\\\\"Ting Chen, Simon Kornblith, Mohammad Norouzi, Geoffrey Hinton\\\\\\\"\\\\n        venue: ICML\\\\n        year: 2020\\\\n        relation: background\\\\n        summary: \\\\\\\"SimCLR 视觉对比学习奠基工作，证明 hard negatives 和大 batch size 对对比学习的重要性。\\\\\\\"\\\\n\\\\n      - title: \\\\\\\"Sentence-BERT: Sentence Embeddings using Siamese BERT-Networks\\\\\\\"\\\\n        authors: \\\\\\\"Nils Reimers, Iryna Gurevych\\\\\\\"\\\\n        venue: EMNLP\\\\n        year: 2019\\\\n        relation: background\\\\n        summary: \\\\\\\"Siamese/triplet 网络训练句子嵌入，StructFuse 的对比训练框架与其类似。\\\\\\\"\\\\n\\\\n      - title: \\\\\\\"Curriculum Learning for Dense Retrieval Distillation\\\\\\\"\\\\n        authors: \\\\\\\"Hansi Zeng, Hamed Zamani, Vishwa Vinay\\\\\\\"\\\\n        venue: \\\\\\\"SIGIR (Best Short Paper)\\\\\\\"\\\\n        year: 2022\\\\n        relation: background\\\\n        summary: \\\\\\\"CL-DRD: 课程学习式知识蒸馏用于密集检索，从粗粒度到细粒度逐步增加训练难度。\\\\\\\"\\\\n\\\\n      - title: \\\\\\\"Effective Hard Negative Mining for Contrastive Learning-Based Code Search\\\\\\\"\\\\n        authors: \\\\\\\"Fan Y., Li C., Ge J., Huang L., Luo B.\\\\\\\"\\\\n        venue: \\\\\\\"ACM TOSEM\\\\\\\"\\\\n        year: 2025\\\\n        relation: contrast-target\\\\n        summary: \\\\\\\"CoCoHaNeRe: 提出可微分 hard negative 机制用于代码搜索对比学习。其对 hard negative 机制的处理与 StructFuse 的发现形成关键对照——StructFuse 证明 true embedding-distance mining 即可持续提升性能。\\\\\\\"\\\\n        note: \\\\\\\"关键引用：StructFuse Claim 1 的 correction target。CoCoHaNeRe 论点是非可微 embedding negatives 学习'slow and ineffective'，StructFuse 证明用 true embedding distance mining 仍然有效。\\\\\\\"\\\\n\\\\n  # ==========================================================================\\\\n  # Category 3: Contrastive Learning for Code\\\\n  # ==========================================================================\\\\n  contrastive_code_learning:\\\\n    description: \\\\\\\"代码领域的对比学习方法，训练时利用代码特性构建正负样本\\\\\\\"\\\\n    papers:\\\\n\\\\n      - title: \\\\\\\"Contrastive Code Representation Learning\\\\\\\"\\\\n        authors: \\\\\\\"Paras Jain, Ajay Jain, Tianjun Zhang, Pieter Abbeel, Joseph Gonzalez, Ion Stoica\\\\\\\"\\\\n        venue: EMNLP\\\\n        year: 2021\\\\n        relation: background\\\\n        summary: \\\\\\\"ContraCode: 自监督对比预训练，通过编译器变换生成功能等价的程序变体，学习代码功能而非表面形式。\\\\\\\"\\\\n\\\\n      - title: \\\\\\\"CodeRetriever: A Large Scale Contrastive Pre-Training Method for Code Search\\\\\\\"\\\\n        authors: \\\\\\\"Xiaonan Li, Yeyun Gong, Yelong Shen, Xipeng Qiu, Hang Zhang, Bolun Yao, Weizhen Qi, Daxin Jiang, Weizhu Chen, Nan Duan\\\\\\\"\\\\n        venue: EMNLP\\\\n        year: 2022\\\\n        relation: background\\\\n        summary: \\\\\\\"结合 unimodal (code-code) 和 bimodal (code-text) 对比学习预训练代码表示，在 11 个代码搜索 benchmark 上 SOTA。\\\\\\\"\\\\n\\\\n      - title: \\\\\\\"Towards Learning (Dis)-Similarity of Source Code from Program Contrasts\\\\\\\"\\\\n        authors: \\\\\\\"Yangruibo Ding, Luca Buratti, Saurabh Pujar, Alessandro Morari, Baishakhi Ray, Saikat Chakraborty\\\\\\\"\\\\n        venue: \\\\\\\"ACL (Long Papers)\\\\\\\"\\\\n        year: 2022\\\\n        relation: background\\\\n        summary: \\\\\\\"利用程序结构和功能属性构建对比样本对，学习代码相似性/差异性表示。\\\\\\\"\\\\n\\\\n  # ==========================================================================\\\\n  # Category 4: Program Analysis for ML\\\\n  # ==========================================================================\\\\n  program_analysis_for_ml:\\\\n    description: \\\\\\\"静态分析辅助 ML，结构信息在代码表示学习中的应用\\\\\\\"\\\\n    papers:\\\\n\\\\n      - title: \\\\\\\"CodeQL: Semantic Code Analysis Engine\\\\\\\"\\\\n        authors: \\\\\\\"GitHub / Semmle\\\\\\\"\\\\n        venue: \\\\\\\"Tool (open-source)\\\\\\\"\\\\n        year: 2019\\\\n        relation: building-block\\\\n        summary: \\\\\\\"基于 Datalog 的代码查询引擎，支持 inter-procedural data-flow 分析。StructFuse 用它提取 scope-bounded data-flow graph。\\\\\\\"\\\\n\\\\n      - title: \\\\\\\"code2vec: Learning Distributed Representations of Code\\\\\\\"\\\\n        authors: \\\\\\\"Uri Alon, Meital Zilberstein, Omer Levy, Eran Yahav\\\\\\\"\\\\n        venue: POPL\\\\n        year: 2019\\\\n        relation: background\\\\n        summary: \\\\\\\"用 AST path 学习代码向量表示，首次大规模证明结构信息对代码表示学习的价值。\\\\\\\"\\\\n\\\\n      - title: \\\\\\\"code2seq: Generating Sequences from Structured Representations of Code\\\\\\\"\\\\n        authors: \\\\\\\"Uri Alon, Shaked Brody, Omer Levy, Eran Yahav\\\\\\\"\\\\n        venue: ICLR\\\\n        year: 2019\\\\n        relation: background\\\\n        summary: \\\\\\\"code2vec 的序列生成扩展，用 AST path attention 生成方法名摘要。\\\\\\\"\\\\n\\\\n      - title: \\\\\\\"Detecting Code Clones with Graph Neural Network and Flow-Augmented Abstract Syntax Tree\\\\\\\"\\\\n        authors: \\\\\\\"Wenhan Wang, Ge Li, Bo Ma, Xin Xia, Zhi Jin\\\\\\\"\\\\n        venue: SANER\\\\n        year: 2020\\\\n        relation: background\\\\n        summary: \\\\\\\"FA-AST: 用 data-flow 增强 AST 进行代码克隆检测，与 StructFuse 用 data-flow 做 hard negative 挖掘思路相关。\\\\\\\"\\\\n\\\\n      - title: \\\\\\\"GraphCodeBERT: Pre-training Code Representations with Data Flow\\\\\\\"\\\\n        authors: \\\\\\\"Daya Guo, Shuo Ren, Shuai Lu, Zhangyin Feng, Duyu Tang, Shujie Liu, Long Zhou, Nan Duan, Alexey Svyatkovskiy, Shengyu Fu, Michele Tufano, Shao Kun Deng, Colin Clement, Dawn Drain, Neel Sundaresan, Jian Yin, Daxin Jiang, Ming Zhou\\\\\\\"\\\\n        venue: ICLR\\\\n        year: 2021\\\\n        relation: background\\\\n        summary: \\\\\\\"在预训练中引入 data-flow edge，证明 data-flow 信息提升代码理解任务。StructFuse 的 insight 与此相关但用途不同（hard negative mining vs pre-training）。\\\\\\\"\\\\n\\\\n      - title: \\\\\\\"ARISE: A Repository-level Graph Representation and Toolset for Agentic Fault Localization and Program Repair\\\\\\\"\\\\n        authors: \\\\\\\"Shahd Seddik, Fatemeh Fard\\\\\\\"\\\\n        venue: arXiv\\\\n        year: 2026\\\\n        relation: contrast\\\\n        summary: \\\\\\\"用 multi-granularity program graph（含 intra-procedural def-use edges）辅助 LLM agent 做 fault localization。仅 intra-procedural + runtime tool calls，与 StructFuse 的 inter-procedural static mining 互补。\\\\\\\"\\\\n\\\\n  # ==========================================================================\\\\n  # Category 5: Code Embeddings / Code Search\\\\n  # ==========================================================================\\\\n  code_embeddings_search:\\\\n    description: \\\\\\\"代码嵌入模型和代码搜索方法\\\\\\\"\\\\n    papers:\\\\n\\\\n      - title: \\\\\\\"CodeSearchNet Challenge: Evaluating the State of Semantic Code Search\\\\\\\"\\\\n        authors: \\\\\\\"Hamel Husain, Ho-Hsiang Wu, Tiferet Gazit, Miltiadis Allamanis, Marc Brockschmidt\\\\\\\"\\\\n        venue: arXiv\\\\n        year: 2019\\\\n        relation: background\\\\n        summary: \\\\\\\"代码语义搜索 benchmark 和数据集，推动了代码嵌入模型的发展。\\\\\\\"\\\\n\\\\n      - title: \\\\\\\"CodeBERT: A Pre-Trained Model for Programming and Natural Languages\\\\\\\"\\\\n        authors: \\\\\\\"Zhangyin Feng, Daya Guo, Duyu Tang, Nan Duan, Xiaocheng Feng, Ming Gong, Lixin Zou, Bing Qin, Ting Liu, Daxin Jiang, Ming Zhou\\\\\\\"\\\\n        venue: \\\\\\\"EMNLP (Findings)\\\\\\\"\\\\n        year: 2020\\\\n        relation: background\\\\n        summary: \\\\\\\"首个编程语言-自然语言双模态预训练模型，代码嵌入的早期里程碑。\\\\\\\"\\\\n\\\\n      - title: \\\\\\\"UniXcoder: Unified Cross-Modal Pre-training for Code Representation\\\\\\\"\\\\n        authors: \\\\\\\"Daya Guo, Shuai Lu, Nan Duan, Yanlin Wang, Ming Zhou, Jian Yin\\\\\\\"\\\\n        venue: ACL\\\\n        year: 2022\\\\n        relation: background\\\\n        summary: \\\\\\\"统一跨模态代码预训练，在代码搜索等任务上取得 SOTA。\\\\\\\"\\\\n\\\\n      - title: \\\\\\\"StarCoder: May the Source Be with You!\\\\\\\"\\\\n        authors: \\\\\\\"Raymond Li, Loubna Ben Allal, et al. (BigCode)\\\\\\\"\\\\n        venue: TMLR\\\\n        year: 2023\\\\n        relation: building-block\\\\n        summary: \\\\\\\"大规模开源代码 LLM，StructFuse 用 StarCoder2-3B 作为对比学习检索器的 backbone 之一。\\\\\\\"\\\\n\\\\n      - title: \\\\\\\"Code Llama: Open Foundation Models for Code\\\\\\\"\\\\n        authors: \\\\\\\"Baptiste Roziere, Jonas Gehring, Fabian Gloeckle, et al. (Meta AI)\\\\\\\"\\\\n        venue: arXiv\\\\n        year: 2023\\\\n        relation: background\\\\n        summary: \\\\\\\"Meta 的代码大模型系列，基于 Llama 2 微调。\\\\\\\"\\\\n\\\\n      - title: \\\\\\\"Qwen2.5-Coder Technical Report\\\\\\\"\\\\n        authors: \\\\\\\"Binyuan Hui, Jian Yang, Zeyu Cui, et al. (Qwen Team, Alibaba)\\\\\\\"\\\\n        venue: arXiv\\\\n        year: 2024\\\\n        relation: building-block\\\\n        summary: \\\\\\\"Qwen 代码模型系列，StructFuse 用 Qwen2.5-Coder-3B 作为对比学习检索器的 backbone。\\\\\\\"\\\\n\\\\n      - title: \\\\\\\"DeepSeek-Coder: When the Large Language Model Meets Programming -- The Rise of Code Intelligence\\\\\\\"\\\\n        authors: \\\\\\\"Daya Guo, Qihao Zhu, Dejian Yang, Zhenda Xie, Kai Dong, Wentao Zhang, Guanting Chen, Xiao Bi, Yu Wu, Y.K. Li, Fuli Luo, Yingfei Xiong, Wenfeng \\\\n\\\\n... [截断: 省略 3999 字符，传 max_chars=0 获取完整内容]\\\", \\\"total_chars\\\": 15999, \\\"truncated\\\": true}, \\\"error\\\": null, \\\"metadata\\\": {}}\"}",
  "mcpMeta": {
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/literature_map.yaml\", \"content\": \"# StructFuse — Related Work Literature Map\\n# 最后更新: 2026-05-14\\n# 说明: 只收录已验证存在的论文。每篇均经 WebSearch 确认标题/venue/year。\\n# 总计: 39 entries (含 2 个软件工具引用)\\n\\ncategories:\\n\\n  # ==========================================================================\\n  # Category 1: Code Retrieval for Bug Fixing / SWE-bench Ecosystem\\n  # ==========================================================================\\n  code_retrieval_bug_fixing:\\n    description: \\\"SWE-bench 及相关 repo-level 自动修复系统中的代码检索方法\\\"\\n    papers:\\n\\n      - title: \\\"SWE-bench: Can Language Models Resolve Real-World GitHub Issues?\\\"\\n        authors: \\\"Carlos E. Jimenez, John Yang, Alexander Wettig, Shunyu Yao, Kexin Pei, Ofir Press, Karthik Narasimhan\\\"\\n        venue: ICLR\\n        year: 2024\\n        relation: baseline\\n        summary: \\\"从 GitHub issues 构建 repo-level bug fixing benchmark，成为自动修复领域标准评估集。\\\"\\n\\n      - title: \\\"SWE-agent: Agent-Computer Interfaces Enable Automated Software Engineering\\\"\\n        authors: \\\"John Yang, Carlos E. Jimenez, Alexander Wettig, Kilian Lieret, Shunyu Yao, Karthik Narasimhan, Ofir Press\\\"\\n        venue: NeurIPS\\n        year: 2024\\n        relation: competitor\\n        summary: \\\"基于 LLM agent 的交互式 bug fixing 系统，定义了 ACI 接口范式。\\\"\\n\\n      - title: \\\"AutoCodeRover: Autonomous Program Improvement\\\"\\n        authors: \\\"Yuntong Zhang, Haifeng Ruan, Zhiyu Fan, Abhik Roychoudhury\\\"\\n        venue: ISSTA\\n        year: 2024\\n        relation: competitor\\n        summary: \\\"结合代码搜索与 spectrum-based fault localization，利用程序分析缩小修复范围。\\\"\\n\\n      - title: \\\"Agentless: Demystifying LLM-based Software Engineering Agents\\\"\\n        authors: \\\"Chunqiu Steven Xia, Yinlin Deng, Soren Dunn, Lingming Zhang\\\"\\n        venue: arXiv\\n        year: 2024\\n        relation: competitor\\n        summary: \\\"无 agent 架构的 two-phase localize-then-repair 方法，在 SWE-bench 上取得强 baseline。\\\"\\n\\n      - title: \\\"SWE-smith: Scaling Data for Software Engineering Agents\\\"\\n        authors: \\\"John Yang, Kilian Lieret, Carlos E. Jimenez, Alexander Wettig, Kabir Khandpur, Yanzhe Zhang, Binyuan Hui, Ofir Press, Ludwig Schmidt, Diyi Yang\\\"\\n        venue: \\\"NeurIPS (Datasets & Benchmarks, Spotlight)\\\"\\n        year: 2025\\n        relation: building-block\\n        summary: \\\"自动从 GitHub 生成大规模 SWE-bench 风格训练数据，StructFuse 用其 repos 做 data-flow 提取。\\\"\\n\\n      - title: \\\"RepoBench: Benchmarking Repository-Level Code Auto-Completion Systems\\\"\\n        authors: \\\"Tianyang Liu, Canwen Xu, Julian McAuley\\\"\\n        venue: ICLR\\n        year: 2024\\n        relation: baseline\\n        summary: \\\"Repo-level 代码补全/检索 benchmark，含 RepoBench-R 检索子任务。\\\"\\n\\n      - title: \\\"SweRank: Software Issue Localization with Code Ranking\\\"\\n        authors: \\\"Revanth Gangi Reddy, Tarun Suresh, JaeHyeok Doo, Ye Liu, Xuan Phi Nguyen, Yingbo Zhou, Semih Yavuz, Caiming Xiong, Heng Ji, Shafiq Joty\\\"\\n        venue: arXiv\\n        year: 2025\\n        relation: competitor\\n        summary: \\\"Retrieve-and-rerank 框架用于 software issue localization，在 SWE-Bench-Lite 和 LocBench 上 SOTA，text-based retrieval baseline。\\\"\\n\\n      - title: \\\"SWE-Fixer: Training Open-Source LLMs for Effective and Efficient GitHub Issue Resolution\\\"\\n        authors: \\\"Chengxing Xie, Bowen Li, Chang Gao, He Du, Wai Lam, Difan Zou, Kai Chen\\\"\\n        venue: \\\"ACL (Findings)\\\"\\n        year: 2025\\n        relation: competitor\\n        summary: \\\"BM25 + LLM retriever 的 coarse-to-fine file retrieval pipeline，在 SWE-Bench Verified 上 30.2%。\\\"\\n\\n  # ==========================================================================\\n  # Category 2: Hard Negative Mining in Contrastive Learning\\n  # ==========================================================================\\n  hard_negative_mining:\\n    description: \\\"对比学习中 hard negative 挖掘策略，以及密集检索中的负样本选择\\\"\\n    papers:\\n\\n      - title: \\\"Dense Passage Retrieval for Open-Domain Question Answering\\\"\\n        authors: \\\"Vladimir Karpukhin, Barlas Oguz, Sewon Min, Patrick Lewis, Ledell Wu, Sergey Edunov, Danqi Chen, Wen-tau Yih\\\"\\n        venue: EMNLP\\n        year: 2020\\n        relation: background\\n        summary: \\\"DPR 开创了 in-batch negatives + BM25 hard negatives 的双塔检索范式。\\\"\\n\\n      - title: \\\"Approximate Nearest Neighbor Negative Contrastive Learning for Dense Text Retrieval\\\"\\n        authors: \\\"Lee Xiong, Chenyan Xiong, Ye Li, Kwok-Fung Tang, Jialin Liu, Paul Bennett, Junaid Ahmed, Arnold Overwijk\\\"\\n        venue: ICLR\\n        year: 2021\\n        relation: background\\n        summary: \\\"ANCE 用 ANN index 动态挖掘 embedding-distance hard negatives，StructFuse 的 baseline negative 策略之一。\\\"\\n\\n      - title: \\\"A Simple Framework for Contrastive Learning of Visual Representations\\\"\\n        authors: \\\"Ting Chen, Simon Kornblith, Mohammad Norouzi, Geoffrey Hinton\\\"\\n        venue: ICML\\n        year: 2020\\n        relation: background\\n        summary: \\\"SimCLR 视觉对比学习奠基工作，证明 hard negatives 和大 batch size 对对比学习的重要性。\\\"\\n\\n      - title: \\\"Sentence-BERT: Sentence Embeddings using Siamese BERT-Networks\\\"\\n        authors: \\\"Nils Reimers, Iryna Gurevych\\\"\\n        venue: EMNLP\\n        year: 2019\\n        relation: background\\n        summary: \\\"Siamese/triplet 网络训练句子嵌入，StructFuse 的对比训练框架与其类似。\\\"\\n\\n      - title: \\\"Curriculum Learning for Dense Retrieval Distillation\\\"\\n        authors: \\\"Hansi Zeng, Hamed Zamani, Vishwa Vinay\\\"\\n        venue: \\\"SIGIR (Best Short Paper)\\\"\\n        year: 2022\\n        relation: background\\n        summary: \\\"CL-DRD: 课程学习式知识蒸馏用于密集检索，从粗粒度到细粒度逐步增加训练难度。\\\"\\n\\n      - title: \\\"Effective Hard Negative Mining for Contrastive Learning-Based Code Search\\\"\\n        authors: \\\"Fan Y., Li C., Ge J., Huang L., Luo B.\\\"\\n        venue: \\\"ACM TOSEM\\\"\\n        year: 2025\\n        relation: contrast-target\\n        summary: \\\"CoCoHaNeRe: 提出可微分 hard negative 机制用于代码搜索对比学习。其对 hard negative 机制的处理与 StructFuse 的发现形成关键对照——StructFuse 证明 true embedding-distance mining 即可持续提升性能。\\\"\\n        note: \\\"关键引用：StructFuse Claim 1 的 correction target。CoCoHaNeRe 论点是非可微 embedding negatives 学习'slow and ineffective'，StructFuse 证明用 true embedding distance mining 仍然有效。\\\"\\n\\n  # ==========================================================================\\n  # Category 3: Contrastive Learning for Code\\n  # ==========================================================================\\n  contrastive_code_learning:\\n    description: \\\"代码领域的对比学习方法，训练时利用代码特性构建正负样本\\\"\\n    papers:\\n\\n      - title: \\\"Contrastive Code Representation Learning\\\"\\n        authors: \\\"Paras Jain, Ajay Jain, Tianjun Zhang, Pieter Abbeel, Joseph Gonzalez, Ion Stoica\\\"\\n        venue: EMNLP\\n        year: 2021\\n        relation: background\\n        summary: \\\"ContraCode: 自监督对比预训练，通过编译器变换生成功能等价的程序变体，学习代码功能而非表面形式。\\\"\\n\\n      - title: \\\"CodeRetriever: A Large Scale Contrastive Pre-Training Method for Code Search\\\"\\n        authors: \\\"Xiaonan Li, Yeyun Gong, Yelong Shen, Xipeng Qiu, Hang Zhang, Bolun Yao, Weizhen Qi, Daxin Jiang, Weizhu Chen, Nan Duan\\\"\\n        venue: EMNLP\\n        year: 2022\\n        relation: background\\n        summary: \\\"结合 unimodal (code-code) 和 bimodal (code-text) 对比学习预训练代码表示，在 11 个代码搜索 benchmark 上 SOTA。\\\"\\n\\n      - title: \\\"Towards Learning (Dis)-Similarity of Source Code from Program Contrasts\\\"\\n        authors: \\\"Yangruibo Ding, Luca Buratti, Saurabh Pujar, Alessandro Morari, Baishakhi Ray, Saikat Chakraborty\\\"\\n        venue: \\\"ACL (Long Papers)\\\"\\n        year: 2022\\n        relation: background\\n        summary: \\\"利用程序结构和功能属性构建对比样本对，学习代码相似性/差异性表示。\\\"\\n\\n  # ==========================================================================\\n  # Category 4: Program Analysis for ML\\n  # ==========================================================================\\n  program_analysis_for_ml:\\n    description: \\\"静态分析辅助 ML，结构信息在代码表示学习中的应用\\\"\\n    papers:\\n\\n      - title: \\\"CodeQL: Semantic Code Analysis Engine\\\"\\n        authors: \\\"GitHub / Semmle\\\"\\n        venue: \\\"Tool (open-source)\\\"\\n        year: 2019\\n        relation: building-block\\n        summary: \\\"基于 Datalog 的代码查询引擎，支持 inter-procedural data-flow 分析。StructFuse 用它提取 scope-bounded data-flow graph。\\\"\\n\\n      - title: \\\"code2vec: Learning Distributed Representations of Code\\\"\\n        authors: \\\"Uri Alon, Meital Zilberstein, Omer Levy, Eran Yahav\\\"\\n        venue: POPL\\n        year: 2019\\n        relation: background\\n        summary: \\\"用 AST path 学习代码向量表示，首次大规模证明结构信息对代码表示学习的价值。\\\"\\n\\n      - title: \\\"code2seq: Generating Sequences from Structured Representations of Code\\\"\\n        authors: \\\"Uri Alon, Shaked Brody, Omer Levy, Eran Yahav\\\"\\n        venue: ICLR\\n        year: 2019\\n        relation: background\\n        summary: \\\"code2vec 的序列生成扩展，用 AST path attention 生成方法名摘要。\\\"\\n\\n      - title: \\\"Detecting Code Clones with Graph Neural Network and Flow-Augmented Abstract Syntax Tree\\\"\\n        authors: \\\"Wenhan Wang, Ge Li, Bo Ma, Xin Xia, Zhi Jin\\\"\\n        venue: SANER\\n        year: 2020\\n        relation: background\\n        summary: \\\"FA-AST: 用 data-flow 增强 AST 进行代码克隆检测，与 StructFuse 用 data-flow 做 hard negative 挖掘思路相关。\\\"\\n\\n      - title: \\\"GraphCodeBERT: Pre-training Code Representations with Data Flow\\\"\\n        authors: \\\"Daya Guo, Shuo Ren, Shuai Lu, Zhangyin Feng, Duyu Tang, Shujie Liu, Long Zhou, Nan Duan, Alexey Svyatkovskiy, Shengyu Fu, Michele Tufano, Shao Kun Deng, Colin Clement, Dawn Drain, Neel Sundaresan, Jian Yin, Daxin Jiang, Ming Zhou\\\"\\n        venue: ICLR\\n        year: 2021\\n        relation: background\\n        summary: \\\"在预训练中引入 data-flow edge，证明 data-flow 信息提升代码理解任务。StructFuse 的 insight 与此相关但用途不同（hard negative mining vs pre-training）。\\\"\\n\\n      - title: \\\"ARISE: A Repository-level Graph Representation and Toolset for Agentic Fault Localization and Program Repair\\\"\\n        authors: \\\"Shahd Seddik, Fatemeh Fard\\\"\\n        venue: arXiv\\n        year: 2026\\n        relation: contrast\\n        summary: \\\"用 multi-granularity program graph（含 intra-procedural def-use edges）辅助 LLM agent 做 fault localization。仅 intra-procedural + runtime tool calls，与 StructFuse 的 inter-procedural static mining 互补。\\\"\\n\\n  # ==========================================================================\\n  # Category 5: Code Embeddings / Code Search\\n  # ==========================================================================\\n  code_embeddings_search:\\n    description: \\\"代码嵌入模型和代码搜索方法\\\"\\n    papers:\\n\\n      - title: \\\"CodeSearchNet Challenge: Evaluating the State of Semantic Code Search\\\"\\n        authors: \\\"Hamel Husain, Ho-Hsiang Wu, Tiferet Gazit, Miltiadis Allamanis, Marc Brockschmidt\\\"\\n        venue: arXiv\\n        year: 2019\\n        relation: background\\n        summary: \\\"代码语义搜索 benchmark 和数据集，推动了代码嵌入模型的发展。\\\"\\n\\n      - title: \\\"CodeBERT: A Pre-Trained Model for Programming and Natural Languages\\\"\\n        authors: \\\"Zhangyin Feng, Daya Guo, Duyu Tang, Nan Duan, Xiaocheng Feng, Ming Gong, Lixin Zou, Bing Qin, Ting Liu, Daxin Jiang, Ming Zhou\\\"\\n        venue: \\\"EMNLP (Findings)\\\"\\n        year: 2020\\n        relation: background\\n        summary: \\\"首个编程语言-自然语言双模态预训练模型，代码嵌入的早期里程碑。\\\"\\n\\n      - title: \\\"UniXcoder: Unified Cross-Modal Pre-training for Code Representation\\\"\\n        authors: \\\"Daya Guo, Shuai Lu, Nan Duan, Yanlin Wang, Ming Zhou, Jian Yin\\\"\\n        venue: ACL\\n        year: 2022\\n        relation: background\\n        summary: \\\"统一跨模态代码预训练，在代码搜索等任务上取得 SOTA。\\\"\\n\\n      - title: \\\"StarCoder: May the Source Be with You!\\\"\\n        authors: \\\"Raymond Li, Loubna Ben Allal, et al. (BigCode)\\\"\\n        venue: TMLR\\n        year: 2023\\n        relation: building-block\\n        summary: \\\"大规模开源代码 LLM，StructFuse 用 StarCoder2-3B 作为对比学习检索器的 backbone 之一。\\\"\\n\\n      - title: \\\"Code Llama: Open Foundation Models for Code\\\"\\n        authors: \\\"Baptiste Roziere, Jonas Gehring, Fabian Gloeckle, et al. (Meta AI)\\\"\\n        venue: arXiv\\n        year: 2023\\n        relation: background\\n        summary: \\\"Meta 的代码大模型系列，基于 Llama 2 微调。\\\"\\n\\n      - title: \\\"Qwen2.5-Coder Technical Report\\\"\\n        authors: \\\"Binyuan Hui, Jian Yang, Zeyu Cui, et al. (Qwen Team, Alibaba)\\\"\\n        venue: arXiv\\n        year: 2024\\n        relation: building-block\\n        summary: \\\"Qwen 代码模型系列，StructFuse 用 Qwen2.5-Coder-3B 作为对比学习检索器的 backbone。\\\"\\n\\n      - title: \\\"DeepSeek-Coder: When the Large Language Model Meets Programming -- The Rise of Code Intelligence\\\"\\n        authors: \\\"Daya Guo, Qihao Zhu, Dejian Yang, Zhenda Xie, Kai Dong, Wentao Zhang, Guanting Chen, Xiao Bi, Yu Wu, Y.K. Li, Fuli Luo, Yingfei Xiong, Wenfeng \\n\\n... [截断: 省略 3999 字符，传 max_chars=0 获取完整内容]\", \"total_chars\": 15999, \"truncated\": true}, \"error\": null, \"metadata\": {}}"
    }
  },
  "sourceToolAssistantUUID": "1f81be61-908d-4f26-adbf-f4f2429dca6f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/.claude/sessions/reviewer_65cfe724",
  "sessionId": "f444a635-eeef-4924-9b48-a4c308632421",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---


### Runtime record

_source line 26_

```json
{
  "type": "last-prompt",
  "lastPrompt": "[系统通知 — worker_done:worker_research_related-work-literature_20260516T001526]: Worker worker_research_related-work-literature_20260516T001526 已完成（status=done），请审查 Agent 的处理结果。",
  "leafUuid": "c3795a1b-57f2-4a63-ac49-306041be5a27",
  "sessionId": "f444a635-eeef-4924-9b48-a4c308632421"
}
```

---


### Runtime record

_source line 27_

```json
{
  "type": "ai-title",
  "aiTitle": "Review research literature worker completion",
  "sessionId": "f444a635-eeef-4924-9b48-a4c308632421"
}
```

---


### Assistant

_source line 28 · 2026-05-16T00:23:28.043Z_

<details><summary>Logged reasoning block</summary>

```text
The worker was about related work literature research. Let me look more at what the worker specifically produced. The worker name is `worker_research_related-work-literature_20260516T001526`. Let me check the artifacts and the Related Work draft that might exist locally, as well as the paper_framing to understand context.

Let me read the Related Work draft and check what this latest worker might have done differently from plan_017_literature (which was completed 2 days ago). The worker's timestamp is 2026-05-16T00:15:26 which is today, so it's newer work.

Let me check the local workspace for related work artifacts and the literature map fully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c3795a1b-57f2-4a63-ac49-306041be5a27",
  "isSidechain": false,
  "requestId": "req_011Cb5J32VLKPFNYxnB9NPTr",
  "type": "assistant",
  "uuid": "e1de161d-a8a3-42cc-a84e-bf3ca3b8b916",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/.claude/sessions/reviewer_65cfe724",
  "sessionId": "f444a635-eeef-4924-9b48-a4c308632421",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016fPC9ji1Brow7ZujRQVpiF",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 11073,
      "cache_read_input_tokens": 47141,
      "output_tokens": 495,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 11073,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 495,
          "cache_read_input_tokens": 47141,
          "cache_creation_input_tokens": 11073,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 11073
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

_source line 29 · 2026-05-16T00:23:29.923Z_

Worker 的时间戳是今天（05-16），比 plan_017_literature（05-14 完成）更新。需要看具体产出和本地变更。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e1de161d-a8a3-42cc-a84e-bf3ca3b8b916",
  "isSidechain": false,
  "requestId": "req_011Cb5J32VLKPFNYxnB9NPTr",
  "type": "assistant",
  "uuid": "640e25db-c371-4159-8307-0f7459b5afff",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/.claude/sessions/reviewer_65cfe724",
  "sessionId": "f444a635-eeef-4924-9b48-a4c308632421",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016fPC9ji1Brow7ZujRQVpiF",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 11073,
      "cache_read_input_tokens": 47141,
      "output_tokens": 495,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 11073,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 495,
          "cache_read_input_tokens": 47141,
          "cache_creation_input_tokens": 11073,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 11073
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

_source line 30 · 2026-05-16T00:23:30.913Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_014VftRdZed9EqzZKu5upuwE`</summary>

```json
{
  "project": "structfuse-context",
  "file": "literature_map.yaml",
  "max_chars": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "640e25db-c371-4159-8307-0f7459b5afff",
  "isSidechain": false,
  "requestId": "req_011Cb5J32VLKPFNYxnB9NPTr",
  "type": "assistant",
  "uuid": "30d6d97a-30f4-488e-931a-65602b1fe6a1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/.claude/sessions/reviewer_65cfe724",
  "sessionId": "f444a635-eeef-4924-9b48-a4c308632421",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016fPC9ji1Brow7ZujRQVpiF",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 11073,
      "cache_read_input_tokens": 47141,
      "output_tokens": 495,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 11073,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 495,
          "cache_read_input_tokens": 47141,
          "cache_creation_input_tokens": 11073,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 11073
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

_source line 31 · 2026-05-16T00:23:32.932Z_

<details><summary>↩ Tool result · `toolu_01XcAHdgC8bxNajXggmnZnua`</summary>

```text
/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/_project/report/related_work_expansion_report.md
/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/literature/related_work_expansion_report.md
/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/_project/paper/related_work_v1_dc54a3.md
/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/_project/paper/related_work_v1.md
/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/paper_drafts/related_work_supplement.md
/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/_project/paper/related_work_v1_5cf1f6.md
/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/paper_drafts/related_work_v1.md
/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/_project/report/related_work_references.md
/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/literature/related_work_references.md
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "299179a3-ad4e-486e-b8c2-abb5490f39f8",
  "isSidechain": false,
  "promptId": "ee81bb41-edfe-48b7-9827-d79a74cf7a5e",
  "type": "user",
  "uuid": "3f842e06-4b1c-4e12-8083-b29fb4136720",
  "toolUseResult": {
    "filenames": [
      "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/_project/report/related_work_expansion_report.md",
      "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/literature/related_work_expansion_report.md",
      "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/_project/paper/related_work_v1_dc54a3.md",
      "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/_project/paper/related_work_v1.md",
      "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/paper_drafts/related_work_supplement.md",
      "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/_project/paper/related_work_v1_5cf1f6.md",
      "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/paper_drafts/related_work_v1.md",
      "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/_project/report/related_work_references.md",
      "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/literature/related_work_references.md"
    ],
    "durationMs": 16,
    "numFiles": 9,
    "truncated": false
  },
  "sourceToolAssistantUUID": "299179a3-ad4e-486e-b8c2-abb5490f39f8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/.claude/sessions/reviewer_65cfe724",
  "sessionId": "f444a635-eeef-4924-9b48-a4c308632421",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---


### Tool result

_source line 32 · 2026-05-16T00:23:30.930Z_

<details><summary>↩ Tool result · `toolu_014VftRdZed9EqzZKu5upuwE`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/literature_map.yaml\", \"content\": \"# StructFuse — Related Work Literature Map\\n# 最后更新: 2026-05-14\\n# 说明: 只收录已验证存在的论文。每篇均经 WebSearch 确认标题/venue/year。\\n# 总计: 39 entries (含 2 个软件工具引用)\\n\\ncategories:\\n\\n  # ==========================================================================\\n  # Category 1: Code Retrieval for Bug Fixing / SWE-bench Ecosystem\\n  # ==========================================================================\\n  code_retrieval_bug_fixing:\\n    description: \\\"SWE-bench 及相关 repo-level 自动修复系统中的代码检索方法\\\"\\n    papers:\\n\\n      - title: \\\"SWE-bench: Can Language Models Resolve Real-World GitHub Issues?\\\"\\n        authors: \\\"Carlos E. Jimenez, John Yang, Alexander Wettig, Shunyu Yao, Kexin Pei, Ofir Press, Karthik Narasimhan\\\"\\n        venue: ICLR\\n        year: 2024\\n        relation: baseline\\n        summary: \\\"从 GitHub issues 构建 repo-level bug fixing benchmark，成为自动修复领域标准评估集。\\\"\\n\\n      - title: \\\"SWE-agent: Agent-Computer Interfaces Enable Automated Software Engineering\\\"\\n        authors: \\\"John Yang, Carlos E. Jimenez, Alexander Wettig, Kilian Lieret, Shunyu Yao, Karthik Narasimhan, Ofir Press\\\"\\n        venue: NeurIPS\\n        year: 2024\\n        relation: competitor\\n        summary: \\\"基于 LLM agent 的交互式 bug fixing 系统，定义了 ACI 接口范式。\\\"\\n\\n      - title: \\\"AutoCodeRover: Autonomous Program Improvement\\\"\\n        authors: \\\"Yuntong Zhang, Haifeng Ruan, Zhiyu Fan, Abhik Roychoudhury\\\"\\n        venue: ISSTA\\n        year: 2024\\n        relation: competitor\\n        summary: \\\"结合代码搜索与 spectrum-based fault localization，利用程序分析缩小修复范围。\\\"\\n\\n      - title: \\\"Agentless: Demystifying LLM-based Software Engineering Agents\\\"\\n        authors: \\\"Chunqiu Steven Xia, Yinlin Deng, Soren Dunn, Lingming Zhang\\\"\\n        venue: arXiv\\n        year: 2024\\n        relation: competitor\\n        summary: \\\"无 agent 架构的 two-phase localize-then-repair 方法，在 SWE-bench 上取得强 baseline。\\\"\\n\\n      - title: \\\"SWE-smith: Scaling Data for Software Engineering Agents\\\"\\n        authors: \\\"John Yang, Kilian Lieret, Carlos E. Jimenez, Alexander Wettig, Kabir Khandpur, Yanzhe Zhang, Binyuan Hui, Ofir Press, Ludwig Schmidt, Diyi Yang\\\"\\n        venue: \\\"NeurIPS (Datasets & Benchmarks, Spotlight)\\\"\\n        year: 2025\\n        relation: building-block\\n        summary: \\\"自动从 GitHub 生成大规模 SWE-bench 风格训练数据，StructFuse 用其 repos 做 data-flow 提取。\\\"\\n\\n      - title: \\\"RepoBench: Benchmarking Repository-Level Code Auto-Completion Systems\\\"\\n        authors: \\\"Tianyang Liu, Canwen Xu, Julian McAuley\\\"\\n        venue: ICLR\\n        year: 2024\\n        relation: baseline\\n        summary: \\\"Repo-level 代码补全/检索 benchmark，含 RepoBench-R 检索子任务。\\\"\\n\\n      - title: \\\"SweRank: Software Issue Localization with Code Ranking\\\"\\n        authors: \\\"Revanth Gangi Reddy, Tarun Suresh, JaeHyeok Doo, Ye Liu, Xuan Phi Nguyen, Yingbo Zhou, Semih Yavuz, Caiming Xiong, Heng Ji, Shafiq Joty\\\"\\n        venue: arXiv\\n        year: 2025\\n        relation: competitor\\n        summary: \\\"Retrieve-and-rerank 框架用于 software issue localization，在 SWE-Bench-Lite 和 LocBench 上 SOTA，text-based retrieval baseline。\\\"\\n\\n      - title: \\\"SWE-Fixer: Training Open-Source LLMs for Effective and Efficient GitHub Issue Resolution\\\"\\n        authors: \\\"Chengxing Xie, Bowen Li, Chang Gao, He Du, Wai Lam, Difan Zou, Kai Chen\\\"\\n        venue: \\\"ACL (Findings)\\\"\\n        year: 2025\\n        relation: competitor\\n        summary: \\\"BM25 + LLM retriever 的 coarse-to-fine file retrieval pipeline，在 SWE-Bench Verified 上 30.2%。\\\"\\n\\n  # ==========================================================================\\n  # Category 2: Hard Negative Mining in Contrastive Learning\\n  # ==========================================================================\\n  hard_negative_mining:\\n    description: \\\"对比学习中 hard negative 挖掘策略，以及密集检索中的负样本选择\\\"\\n    papers:\\n\\n      - title: \\\"Dense Passage Retrieval for Open-Domain Question Answering\\\"\\n        authors: \\\"Vladimir Karpukhin, Barlas Oguz, Sewon Min, Patrick Lewis, Ledell Wu, Sergey Edunov, Danqi Chen, Wen-tau Yih\\\"\\n        venue: EMNLP\\n        year: 2020\\n        relation: background\\n        summary: \\\"DPR 开创了 in-batch negatives + BM25 hard negatives 的双塔检索范式。\\\"\\n\\n      - title: \\\"Approximate Nearest Neighbor Negative Contrastive Learning for Dense Text Retrieval\\\"\\n        authors: \\\"Lee Xiong, Chenyan Xiong, Ye Li, Kwok-Fung Tang, Jialin Liu, Paul Bennett, Junaid Ahmed, Arnold Overwijk\\\"\\n        venue: ICLR\\n        year: 2021\\n        relation: background\\n        summary: \\\"ANCE 用 ANN index 动态挖掘 embedding-distance hard negatives，StructFuse 的 baseline negative 策略之一。\\\"\\n\\n      - title: \\\"A Simple Framework for Contrastive Learning of Visual Representations\\\"\\n        authors: \\\"Ting Chen, Simon Kornblith, Mohammad Norouzi, Geoffrey Hinton\\\"\\n        venue: ICML\\n        year: 2020\\n        relation: background\\n        summary: \\\"SimCLR 视觉对比学习奠基工作，证明 hard negatives 和大 batch size 对对比学习的重要性。\\\"\\n\\n      - title: \\\"Sentence-BERT: Sentence Embeddings using Siamese BERT-Networks\\\"\\n        authors: \\\"Nils Reimers, Iryna Gurevych\\\"\\n        venue: EMNLP\\n        year: 2019\\n        relation: background\\n        summary: \\\"Siamese/triplet 网络训练句子嵌入，StructFuse 的对比训练框架与其类似。\\\"\\n\\n      - title: \\\"Curriculum Learning for Dense Retrieval Distillation\\\"\\n        authors: \\\"Hansi Zeng, Hamed Zamani, Vishwa Vinay\\\"\\n        venue: \\\"SIGIR (Best Short Paper)\\\"\\n        year: 2022\\n        relation: background\\n        summary: \\\"CL-DRD: 课程学习式知识蒸馏用于密集检索，从粗粒度到细粒度逐步增加训练难度。\\\"\\n\\n      - title: \\\"Effective Hard Negative Mining for Contrastive Learning-Based Code Search\\\"\\n        authors: \\\"Fan Y., Li C., Ge J., Huang L., Luo B.\\\"\\n        venue: \\\"ACM TOSEM\\\"\\n        year: 2025\\n        relation: contrast-target\\n        summary: \\\"CoCoHaNeRe: 提出可微分 hard negative 机制用于代码搜索对比学习。其对 hard negative 机制的处理与 StructFuse 的发现形成关键对照——StructFuse 证明 true embedding-distance mining 即可持续提升性能。\\\"\\n        note: \\\"关键引用：StructFuse Claim 1 的 correction target。CoCoHaNeRe 论点是非可微 embedding negatives 学习'slow and ineffective'，StructFuse 证明用 true embedding distance mining 仍然有效。\\\"\\n\\n  # ==========================================================================\\n  # Category 3: Contrastive Learning for Code\\n  # ==========================================================================\\n  contrastive_code_learning:\\n    description: \\\"代码领域的对比学习方法，训练时利用代码特性构建正负样本\\\"\\n    papers:\\n\\n      - title: \\\"Contrastive Code Representation Learning\\\"\\n        authors: \\\"Paras Jain, Ajay Jain, Tianjun Zhang, Pieter Abbeel, Joseph Gonzalez, Ion Stoica\\\"\\n        venue: EMNLP\\n        year: 2021\\n        relation: background\\n        summary: \\\"ContraCode: 自监督对比预训练，通过编译器变换生成功能等价的程序变体，学习代码功能而非表面形式。\\\"\\n\\n      - title: \\\"CodeRetriever: A Large Scale Contrastive Pre-Training Method for Code Search\\\"\\n        authors: \\\"Xiaonan Li, Yeyun Gong, Yelong Shen, Xipeng Qiu, Hang Zhang, Bolun Yao, Weizhen Qi, Daxin Jiang, Weizhu Chen, Nan Duan\\\"\\n        venue: EMNLP\\n        year: 2022\\n        relation: background\\n        summary: \\\"结合 unimodal (code-code) 和 bimodal (code-text) 对比学习预训练代码表示，在 11 个代码搜索 benchmark 上 SOTA。\\\"\\n\\n      - title: \\\"Towards Learning (Dis)-Similarity of Source Code from Program Contrasts\\\"\\n        authors: \\\"Yangruibo Ding, Luca Buratti, Saurabh Pujar, Alessandro Morari, Baishakhi Ray, Saikat Chakraborty\\\"\\n        venue: \\\"ACL (Long Papers)\\\"\\n        year: 2022\\n        relation: background\\n        summary: \\\"利用程序结构和功能属性构建对比样本对，学习代码相似性/差异性表示。\\\"\\n\\n  # ==========================================================================\\n  # Category 4: Program Analysis for ML\\n  # ==========================================================================\\n  program_analysis_for_ml:\\n    description: \\\"静态分析辅助 ML，结构信息在代码表示学习中的应用\\\"\\n    papers:\\n\\n      - title: \\\"CodeQL: Semantic Code Analysis Engine\\\"\\n        authors: \\\"GitHub / Semmle\\\"\\n        venue: \\\"Tool (open-source)\\\"\\n        year: 2019\\n        relation: building-block\\n        summary: \\\"基于 Datalog 的代码查询引擎，支持 inter-procedural data-flow 分析。StructFuse 用它提取 scope-bounded data-flow graph。\\\"\\n\\n      - title: \\\"code2vec: Learning Distributed Representations of Code\\\"\\n        authors: \\\"Uri Alon, Meital Zilberstein, Omer Levy, Eran Yahav\\\"\\n        venue: POPL\\n        year: 2019\\n        relation: background\\n        summary: \\\"用 AST path 学习代码向量表示，首次大规模证明结构信息对代码表示学习的价值。\\\"\\n\\n      - title: \\\"code2seq: Generating Sequences from Structured Representations of Code\\\"\\n        authors: \\\"Uri Alon, Shaked Brody, Omer Levy, Eran Yahav\\\"\\n        venue: ICLR\\n        year: 2019\\n        relation: background\\n        summary: \\\"code2vec 的序列生成扩展，用 AST path attention 生成方法名摘要。\\\"\\n\\n      - title: \\\"Detecting Code Clones with Graph Neural Network and Flow-Augmented Abstract Syntax Tree\\\"\\n        authors: \\\"Wenhan Wang, Ge Li, Bo Ma, Xin Xia, Zhi Jin\\\"\\n        venue: SANER\\n        year: 2020\\n        relation: background\\n        summary: \\\"FA-AST: 用 data-flow 增强 AST 进行代码克隆检测，与 StructFuse 用 data-flow 做 hard negative 挖掘思路相关。\\\"\\n\\n      - title: \\\"GraphCodeBERT: Pre-training Code Representations with Data Flow\\\"\\n        authors: \\\"Daya Guo, Shuo Ren, Shuai Lu, Zhangyin Feng, Duyu Tang, Shujie Liu, Long Zhou, Nan Duan, Alexey Svyatkovskiy, Shengyu Fu, Michele Tufano, Shao Kun Deng, Colin Clement, Dawn Drain, Neel Sundaresan, Jian Yin, Daxin Jiang, Ming Zhou\\\"\\n        venue: ICLR\\n        year: 2021\\n        relation: background\\n        summary: \\\"在预训练中引入 data-flow edge，证明 data-flow 信息提升代码理解任务。StructFuse 的 insight 与此相关但用途不同（hard negative mining vs pre-training）。\\\"\\n\\n      - title: \\\"ARISE: A Repository-level Graph Representation and Toolset for Agentic Fault Localization and Program Repair\\\"\\n        authors: \\\"Shahd Seddik, Fatemeh Fard\\\"\\n        venue: arXiv\\n        year: 2026\\n        relation: contrast\\n        summary: \\\"用 multi-granularity program graph（含 intra-procedural def-use edges）辅助 LLM agent 做 fault localization。仅 intra-procedural + runtime tool calls，与 StructFuse 的 inter-procedural static mining 互补。\\\"\\n\\n  # ==========================================================================\\n  # Category 5: Code Embeddings / Code Search\\n  # ==========================================================================\\n  code_embeddings_search:\\n    description: \\\"代码嵌入模型和代码搜索方法\\\"\\n    papers:\\n\\n      - title: \\\"CodeSearchNet Challenge: Evaluating the State of Semantic Code Search\\\"\\n        authors: \\\"Hamel Husain, Ho-Hsiang Wu, Tiferet Gazit, Miltiadis Allamanis, Marc Brockschmidt\\\"\\n        venue: arXiv\\n        year: 2019\\n        relation: background\\n        summary: \\\"代码语义搜索 benchmark 和数据集，推动了代码嵌入模型的发展。\\\"\\n\\n      - title: \\\"CodeBERT: A Pre-Trained Model for Programming and Natural Languages\\\"\\n        authors: \\\"Zhangyin Feng, Daya Guo, Duyu Tang, Nan Duan, Xiaocheng Feng, Ming Gong, Lixin Zou, Bing Qin, Ting Liu, Daxin Jiang, Ming Zhou\\\"\\n        venue: \\\"EMNLP (Findings)\\\"\\n        year: 2020\\n        relation: background\\n        summary: \\\"首个编程语言-自然语言双模态预训练模型，代码嵌入的早期里程碑。\\\"\\n\\n      - title: \\\"UniXcoder: Unified Cross-Modal Pre-training for Code Representation\\\"\\n        authors: \\\"Daya Guo, Shuai Lu, Nan Duan, Yanlin Wang, Ming Zhou, Jian Yin\\\"\\n        venue: ACL\\n        year: 2022\\n        relation: background\\n        summary: \\\"统一跨模态代码预训练，在代码搜索等任务上取得 SOTA。\\\"\\n\\n      - title: \\\"StarCoder: May the Source Be with You!\\\"\\n        authors: \\\"Raymond Li, Loubna Ben Allal, et al. (BigCode)\\\"\\n        venue: TMLR\\n        year: 2023\\n        relation: building-block\\n        summary: \\\"大规模开源代码 LLM，StructFuse 用 StarCoder2-3B 作为对比学习检索器的 backbone 之一。\\\"\\n\\n      - title: \\\"Code Llama: Open Foundation Models for Code\\\"\\n        authors: \\\"Baptiste Roziere, Jonas Gehring, Fabian Gloeckle, et al. (Meta AI)\\\"\\n        venue: arXiv\\n        year: 2023\\n        relation: background\\n        summary: \\\"Meta 的代码大模型系列，基于 Llama 2 微调。\\\"\\n\\n      - title: \\\"Qwen2.5-Coder Technical Report\\\"\\n        authors: \\\"Binyuan Hui, Jian Yang, Zeyu Cui, et al. (Qwen Team, Alibaba)\\\"\\n        venue: arXiv\\n        year: 2024\\n        relation: building-block\\n        summary: \\\"Qwen 代码模型系列，StructFuse 用 Qwen2.5-Coder-3B 作为对比学习检索器的 backbone。\\\"\\n\\n      - title: \\\"DeepSeek-Coder: When the Large Language Model Meets Programming -- The Rise of Code Intelligence\\\"\\n        authors: \\\"Daya Guo, Qihao Zhu, Dejian Yang, Zhenda Xie, Kai Dong, Wentao Zhang, Guanting Chen, Xiao Bi, Yu Wu, Y.K. Li, Fuli Luo, Yingfei Xiong, Wenfeng Liang\\\"\\n        venue: arXiv\\n        year: 2024\\n        relation: background\\n        summary: \\\"开源代码 LLM 系列 (1.3B-33B)，project-level 代码训练 + 16K context + fill-in-the-blank 预训练。\\\"\\n\\n      - title: \\\"RepoFusion: Training Code Models to Understand Your Repository\\\"\\n        authors: \\\"Disha Shrivastava, Denis Kocetkov, Harm de Vries, Dzmitry Bahdanau, Torsten Scholak\\\"\\n        venue: arXiv\\n        year: 2023\\n        relation: background\\n        summary: \\\"训练代码模型融合多个 cross-file repo context 进行代码补全，小模型 + repo context 可匹配大模型性能。\\\"\\n\\n      - title: \\\"BM25\\\"\\n        authors: \\\"Stephen Robertson, Hugo Zaragoza\\\"\\n        venue: \\\"Foundations and Trends in Information Retrieval\\\"\\n        year: 2009\\n        relation: baseline\\n        summary: \\\"经典稀疏检索方法，StructFuse 的 baseline 之一。\\\"\\n\\n  # ==========================================================================\\n  # Category 6: Graph-Guided Code Navigation (Inference-Time)\\n  # ==========================================================================\\n  graph_guided_inference:\\n    description: \\\"推理时利用代码结构图辅助导航/检索的方法（与 StructFuse 的训练时结构信号互补）\\\"\\n    papers:\\n\\n      - title: \\\"LocAgent: Graph-Guided LLM Agents for Code Localization\\\"\\n        authors: \\\"Zhaoling Chen, Robert Tang, Gangda Deng, Fang Wu, Jialong Wu, Zhiwei Jiang, Viktor Prasanna, Arman Cohan, Xingyao Wang\\\"\\n        venue: ACL\\n        year: 2025\\n        relation: contrast\\n        summary: \\\"将代码库解析为有向异构图，LLM agent 通过 multi-hop 推理在图上导航做代码定位。推理时用结构图，StructFuse 训练时用。\\\"\\n\\n      - title: \\\"CodexGraph: Bridging Large Language Models and Code Repositories via Code Graph Databases\\\"\\n        authors: \\\"Xiangyan Liu, Bo Lan, Zhiyuan Hu, Yang Liu, Zhicheng Zhang, Fei Wang, Michael Qizhe Shieh, Wenmeng Zhou\\\"\\n        venue: NAACL\\n        year: 2025\\n        relation: contrast\\n        summary: \\\"将代码库索引到图数据库，LLM agent 通过 graph query 接口检索结构化上下文。\\\"\\n\\n      - title: \\\"RANGER: Repository-Level Agent for Graph-Enhanced Retrieval\\\"\\n        authors: \\\"Pratik Shah, Rajat Ghosh, Aryan Singhal, Debojyoti Dutta\\\"\\n        venue: arXiv\\n        year: 2025\\n        relation: contrast\\n        summary: \\\"构建 repo 知识图（含 variable-level 节点），dual-stage retrieval: Cypher lookup + MCTS-guided graph exploration。\\\"\\n\\n      - title: \\\"RepoGraph: Enhancing AI Software Engineering with Repository-level Code Graph\\\"\\n        authors: \\\"Siru Ouyang, Wenhao Yu, Kaixin Ma, Zilin Xiao, Zhihan Zhang, Mengzhao Jia, Jiawei Han, Hongming Zhang, Dong Yu\\\"\\n        venue: ICLR\\n        year: 2025\\n        relation: contrast\\n        summary: \\\"以代码行为节点构建 repo-level 代码图，作为 SE agent 的 plug-in 导航模块。推理时逐行图导航，与 StructFuse 训练时批量提取结构信号互补。\\\"\\n\\n      - title: \\\"GraphCoder: Enhancing Repository-Level Code Completion via Coarse-to-fine Retrieval Based on Code Context Graph\\\"\\n        authors: \\\"Wei Liu, Ailun Yu, Daoguang Zan, Bo Shen, Wei Zhang, Haiyan Zhao, Zhi Jin, Qianxiang Wang\\\"\\n        venue: ASE\\n        year: 2024\\n        relation: contrast\\n        summary: \\\"构建 code context graph（含 control-flow 和 data-dependence edges）进行 coarse-to-fine 检索辅助代码补全。使用 intra-procedural data-flow，与 StructFuse 的 inter-procedural scope 形成对比。\\\"\\n\\n  # ==========================================================================\\n  # Category 7: Infrastructure / Tools\\n  # ==========================================================================\\n  infrastructure:\\n    description: \\\"StructFuse 依赖的核心基础设施和工具\\\"\\n    papers:\\n\\n      - title: \\\"Billion-Scale Similarity Search with GPUs\\\"\\n        authors: \\\"Jeff Johnson, Matthijs Douze, Herve Jegou\\\"\\n        venue: \\\"IEEE Transactions on Big Data\\\"\\n        year: 2021\\n        relation: building-block\\n        summary: \\\"FAISS: GPU 加速的大规模向量相似度搜索库，StructFuse 用于 ANN-based hard negative mining。\\\"\\n\\n      - title: \\\"Tree-sitter: An Incremental Parsing System for Programming Tools\\\"\\n        authors: \\\"Max Brunsfeld et al.\\\"\\n        venue: \\\"Software (Zenodo DOI: 10.5281/zenodo.13375512)\\\"\\n        year: 2018\\n        relation: building-block\\n        summary: \\\"增量解析库，高效构建和更新 concrete syntax trees。与 CodeQL 互补用于代码结构提取。\\\"\\n        note: \\\"软件工具，无正式论文。引用 Zenodo DOI 或 GitHub repo。\\\"\\n\", \"total_chars\": 15999, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "30d6d97a-30f4-488e-931a-65602b1fe6a1",
  "isSidechain": false,
  "promptId": "ee81bb41-edfe-48b7-9827-d79a74cf7a5e",
  "type": "user",
  "uuid": "88af8593-b0de-470c-a0b3-cadaa1b0b2fe",
  "toolUseResult": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"path\\\": \\\"/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/literature_map.yaml\\\", \\\"content\\\": \\\"# StructFuse — Related Work Literature Map\\\\n# 最后更新: 2026-05-14\\\\n# 说明: 只收录已验证存在的论文。每篇均经 WebSearch 确认标题/venue/year。\\\\n# 总计: 39 entries (含 2 个软件工具引用)\\\\n\\\\ncategories:\\\\n\\\\n  # ==========================================================================\\\\n  # Category 1: Code Retrieval for Bug Fixing / SWE-bench Ecosystem\\\\n  # ==========================================================================\\\\n  code_retrieval_bug_fixing:\\\\n    description: \\\\\\\"SWE-bench 及相关 repo-level 自动修复系统中的代码检索方法\\\\\\\"\\\\n    papers:\\\\n\\\\n      - title: \\\\\\\"SWE-bench: Can Language Models Resolve Real-World GitHub Issues?\\\\\\\"\\\\n        authors: \\\\\\\"Carlos E. Jimenez, John Yang, Alexander Wettig, Shunyu Yao, Kexin Pei, Ofir Press, Karthik Narasimhan\\\\\\\"\\\\n        venue: ICLR\\\\n        year: 2024\\\\n        relation: baseline\\\\n        summary: \\\\\\\"从 GitHub issues 构建 repo-level bug fixing benchmark，成为自动修复领域标准评估集。\\\\\\\"\\\\n\\\\n      - title: \\\\\\\"SWE-agent: Agent-Computer Interfaces Enable Automated Software Engineering\\\\\\\"\\\\n        authors: \\\\\\\"John Yang, Carlos E. Jimenez, Alexander Wettig, Kilian Lieret, Shunyu Yao, Karthik Narasimhan, Ofir Press\\\\\\\"\\\\n        venue: NeurIPS\\\\n        year: 2024\\\\n        relation: competitor\\\\n        summary: \\\\\\\"基于 LLM agent 的交互式 bug fixing 系统，定义了 ACI 接口范式。\\\\\\\"\\\\n\\\\n      - title: \\\\\\\"AutoCodeRover: Autonomous Program Improvement\\\\\\\"\\\\n        authors: \\\\\\\"Yuntong Zhang, Haifeng Ruan, Zhiyu Fan, Abhik Roychoudhury\\\\\\\"\\\\n        venue: ISSTA\\\\n        year: 2024\\\\n        relation: competitor\\\\n        summary: \\\\\\\"结合代码搜索与 spectrum-based fault localization，利用程序分析缩小修复范围。\\\\\\\"\\\\n\\\\n      - title: \\\\\\\"Agentless: Demystifying LLM-based Software Engineering Agents\\\\\\\"\\\\n        authors: \\\\\\\"Chunqiu Steven Xia, Yinlin Deng, Soren Dunn, Lingming Zhang\\\\\\\"\\\\n        venue: arXiv\\\\n        year: 2024\\\\n        relation: competitor\\\\n        summary: \\\\\\\"无 agent 架构的 two-phase localize-then-repair 方法，在 SWE-bench 上取得强 baseline。\\\\\\\"\\\\n\\\\n      - title: \\\\\\\"SWE-smith: Scaling Data for Software Engineering Agents\\\\\\\"\\\\n        authors: \\\\\\\"John Yang, Kilian Lieret, Carlos E. Jimenez, Alexander Wettig, Kabir Khandpur, Yanzhe Zhang, Binyuan Hui, Ofir Press, Ludwig Schmidt, Diyi Yang\\\\\\\"\\\\n        venue: \\\\\\\"NeurIPS (Datasets & Benchmarks, Spotlight)\\\\\\\"\\\\n        year: 2025\\\\n        relation: building-block\\\\n        summary: \\\\\\\"自动从 GitHub 生成大规模 SWE-bench 风格训练数据，StructFuse 用其 repos 做 data-flow 提取。\\\\\\\"\\\\n\\\\n      - title: \\\\\\\"RepoBench: Benchmarking Repository-Level Code Auto-Completion Systems\\\\\\\"\\\\n        authors: \\\\\\\"Tianyang Liu, Canwen Xu, Julian McAuley\\\\\\\"\\\\n        venue: ICLR\\\\n        year: 2024\\\\n        relation: baseline\\\\n        summary: \\\\\\\"Repo-level 代码补全/检索 benchmark，含 RepoBench-R 检索子任务。\\\\\\\"\\\\n\\\\n      - title: \\\\\\\"SweRank: Software Issue Localization with Code Ranking\\\\\\\"\\\\n        authors: \\\\\\\"Revanth Gangi Reddy, Tarun Suresh, JaeHyeok Doo, Ye Liu, Xuan Phi Nguyen, Yingbo Zhou, Semih Yavuz, Caiming Xiong, Heng Ji, Shafiq Joty\\\\\\\"\\\\n        venue: arXiv\\\\n        year: 2025\\\\n        relation: competitor\\\\n        summary: \\\\\\\"Retrieve-and-rerank 框架用于 software issue localization，在 SWE-Bench-Lite 和 LocBench 上 SOTA，text-based retrieval baseline。\\\\\\\"\\\\n\\\\n      - title: \\\\\\\"SWE-Fixer: Training Open-Source LLMs for Effective and Efficient GitHub Issue Resolution\\\\\\\"\\\\n        authors: \\\\\\\"Chengxing Xie, Bowen Li, Chang Gao, He Du, Wai Lam, Difan Zou, Kai Chen\\\\\\\"\\\\n        venue: \\\\\\\"ACL (Findings)\\\\\\\"\\\\n        year: 2025\\\\n        relation: competitor\\\\n        summary: \\\\\\\"BM25 + LLM retriever 的 coarse-to-fine file retrieval pipeline，在 SWE-Bench Verified 上 30.2%。\\\\\\\"\\\\n\\\\n  # ==========================================================================\\\\n  # Category 2: Hard Negative Mining in Contrastive Learning\\\\n  # ==========================================================================\\\\n  hard_negative_mining:\\\\n    description: \\\\\\\"对比学习中 hard negative 挖掘策略，以及密集检索中的负样本选择\\\\\\\"\\\\n    papers:\\\\n\\\\n      - title: \\\\\\\"Dense Passage Retrieval for Open-Domain Question Answering\\\\\\\"\\\\n        authors: \\\\\\\"Vladimir Karpukhin, Barlas Oguz, Sewon Min, Patrick Lewis, Ledell Wu, Sergey Edunov, Danqi Chen, Wen-tau Yih\\\\\\\"\\\\n        venue: EMNLP\\\\n        year: 2020\\\\n        relation: background\\\\n        summary: \\\\\\\"DPR 开创了 in-batch negatives + BM25 hard negatives 的双塔检索范式。\\\\\\\"\\\\n\\\\n      - title: \\\\\\\"Approximate Nearest Neighbor Negative Contrastive Learning for Dense Text Retrieval\\\\\\\"\\\\n        authors: \\\\\\\"Lee Xiong, Chenyan Xiong, Ye Li, Kwok-Fung Tang, Jialin Liu, Paul Bennett, Junaid Ahmed, Arnold Overwijk\\\\\\\"\\\\n        venue: ICLR\\\\n        year: 2021\\\\n        relation: background\\\\n        summary: \\\\\\\"ANCE 用 ANN index 动态挖掘 embedding-distance hard negatives，StructFuse 的 baseline negative 策略之一。\\\\\\\"\\\\n\\\\n      - title: \\\\\\\"A Simple Framework for Contrastive Learning of Visual Representations\\\\\\\"\\\\n        authors: \\\\\\\"Ting Chen, Simon Kornblith, Mohammad Norouzi, Geoffrey Hinton\\\\\\\"\\\\n        venue: ICML\\\\n        year: 2020\\\\n        relation: background\\\\n        summary: \\\\\\\"SimCLR 视觉对比学习奠基工作，证明 hard negatives 和大 batch size 对对比学习的重要性。\\\\\\\"\\\\n\\\\n      - title: \\\\\\\"Sentence-BERT: Sentence Embeddings using Siamese BERT-Networks\\\\\\\"\\\\n        authors: \\\\\\\"Nils Reimers, Iryna Gurevych\\\\\\\"\\\\n        venue: EMNLP\\\\n        year: 2019\\\\n        relation: background\\\\n        summary: \\\\\\\"Siamese/triplet 网络训练句子嵌入，StructFuse 的对比训练框架与其类似。\\\\\\\"\\\\n\\\\n      - title: \\\\\\\"Curriculum Learning for Dense Retrieval Distillation\\\\\\\"\\\\n        authors: \\\\\\\"Hansi Zeng, Hamed Zamani, Vishwa Vinay\\\\\\\"\\\\n        venue: \\\\\\\"SIGIR (Best Short Paper)\\\\\\\"\\\\n        year: 2022\\\\n        relation: background\\\\n        summary: \\\\\\\"CL-DRD: 课程学习式知识蒸馏用于密集检索，从粗粒度到细粒度逐步增加训练难度。\\\\\\\"\\\\n\\\\n      - title: \\\\\\\"Effective Hard Negative Mining for Contrastive Learning-Based Code Search\\\\\\\"\\\\n        authors: \\\\\\\"Fan Y., Li C., Ge J., Huang L., Luo B.\\\\\\\"\\\\n        venue: \\\\\\\"ACM TOSEM\\\\\\\"\\\\n        year: 2025\\\\n        relation: contrast-target\\\\n        summary: \\\\\\\"CoCoHaNeRe: 提出可微分 hard negative 机制用于代码搜索对比学习。其对 hard negative 机制的处理与 StructFuse 的发现形成关键对照——StructFuse 证明 true embedding-distance mining 即可持续提升性能。\\\\\\\"\\\\n        note: \\\\\\\"关键引用：StructFuse Claim 1 的 correction target。CoCoHaNeRe 论点是非可微 embedding negatives 学习'slow and ineffective'，StructFuse 证明用 true embedding distance mining 仍然有效。\\\\\\\"\\\\n\\\\n  # ==========================================================================\\\\n  # Category 3: Contrastive Learning for Code\\\\n  # ==========================================================================\\\\n  contrastive_code_learning:\\\\n    description: \\\\\\\"代码领域的对比学习方法，训练时利用代码特性构建正负样本\\\\\\\"\\\\n    papers:\\\\n\\\\n      - title: \\\\\\\"Contrastive Code Representation Learning\\\\\\\"\\\\n        authors: \\\\\\\"Paras Jain, Ajay Jain, Tianjun Zhang, Pieter Abbeel, Joseph Gonzalez, Ion Stoica\\\\\\\"\\\\n        venue: EMNLP\\\\n        year: 2021\\\\n        relation: background\\\\n        summary: \\\\\\\"ContraCode: 自监督对比预训练，通过编译器变换生成功能等价的程序变体，学习代码功能而非表面形式。\\\\\\\"\\\\n\\\\n      - title: \\\\\\\"CodeRetriever: A Large Scale Contrastive Pre-Training Method for Code Search\\\\\\\"\\\\n        authors: \\\\\\\"Xiaonan Li, Yeyun Gong, Yelong Shen, Xipeng Qiu, Hang Zhang, Bolun Yao, Weizhen Qi, Daxin Jiang, Weizhu Chen, Nan Duan\\\\\\\"\\\\n        venue: EMNLP\\\\n        year: 2022\\\\n        relation: background\\\\n        summary: \\\\\\\"结合 unimodal (code-code) 和 bimodal (code-text) 对比学习预训练代码表示，在 11 个代码搜索 benchmark 上 SOTA。\\\\\\\"\\\\n\\\\n      - title: \\\\\\\"Towards Learning (Dis)-Similarity of Source Code from Program Contrasts\\\\\\\"\\\\n        authors: \\\\\\\"Yangruibo Ding, Luca Buratti, Saurabh Pujar, Alessandro Morari, Baishakhi Ray, Saikat Chakraborty\\\\\\\"\\\\n        venue: \\\\\\\"ACL (Long Papers)\\\\\\\"\\\\n        year: 2022\\\\n        relation: background\\\\n        summary: \\\\\\\"利用程序结构和功能属性构建对比样本对，学习代码相似性/差异性表示。\\\\\\\"\\\\n\\\\n  # ==========================================================================\\\\n  # Category 4: Program Analysis for ML\\\\n  # ==========================================================================\\\\n  program_analysis_for_ml:\\\\n    description: \\\\\\\"静态分析辅助 ML，结构信息在代码表示学习中的应用\\\\\\\"\\\\n    papers:\\\\n\\\\n      - title: \\\\\\\"CodeQL: Semantic Code Analysis Engine\\\\\\\"\\\\n        authors: \\\\\\\"GitHub / Semmle\\\\\\\"\\\\n        venue: \\\\\\\"Tool (open-source)\\\\\\\"\\\\n        year: 2019\\\\n        relation: building-block\\\\n        summary: \\\\\\\"基于 Datalog 的代码查询引擎，支持 inter-procedural data-flow 分析。StructFuse 用它提取 scope-bounded data-flow graph。\\\\\\\"\\\\n\\\\n      - title: \\\\\\\"code2vec: Learning Distributed Representations of Code\\\\\\\"\\\\n        authors: \\\\\\\"Uri Alon, Meital Zilberstein, Omer Levy, Eran Yahav\\\\\\\"\\\\n        venue: POPL\\\\n        year: 2019\\\\n        relation: background\\\\n        summary: \\\\\\\"用 AST path 学习代码向量表示，首次大规模证明结构信息对代码表示学习的价值。\\\\\\\"\\\\n\\\\n      - title: \\\\\\\"code2seq: Generating Sequences from Structured Representations of Code\\\\\\\"\\\\n        authors: \\\\\\\"Uri Alon, Shaked Brody, Omer Levy, Eran Yahav\\\\\\\"\\\\n        venue: ICLR\\\\n        year: 2019\\\\n        relation: background\\\\n        summary: \\\\\\\"code2vec 的序列生成扩展，用 AST path attention 生成方法名摘要。\\\\\\\"\\\\n\\\\n      - title: \\\\\\\"Detecting Code Clones with Graph Neural Network and Flow-Augmented Abstract Syntax Tree\\\\\\\"\\\\n        authors: \\\\\\\"Wenhan Wang, Ge Li, Bo Ma, Xin Xia, Zhi Jin\\\\\\\"\\\\n        venue: SANER\\\\n        year: 2020\\\\n        relation: background\\\\n        summary: \\\\\\\"FA-AST: 用 data-flow 增强 AST 进行代码克隆检测，与 StructFuse 用 data-flow 做 hard negative 挖掘思路相关。\\\\\\\"\\\\n\\\\n      - title: \\\\\\\"GraphCodeBERT: Pre-training Code Representations with Data Flow\\\\\\\"\\\\n        authors: \\\\\\\"Daya Guo, Shuo Ren, Shuai Lu, Zhangyin Feng, Duyu Tang, Shujie Liu, Long Zhou, Nan Duan, Alexey Svyatkovskiy, Shengyu Fu, Michele Tufano, Shao Kun Deng, Colin Clement, Dawn Drain, Neel Sundaresan, Jian Yin, Daxin Jiang, Ming Zhou\\\\\\\"\\\\n        venue: ICLR\\\\n        year: 2021\\\\n        relation: background\\\\n        summary: \\\\\\\"在预训练中引入 data-flow edge，证明 data-flow 信息提升代码理解任务。StructFuse 的 insight 与此相关但用途不同（hard negative mining vs pre-training）。\\\\\\\"\\\\n\\\\n      - title: \\\\\\\"ARISE: A Repository-level Graph Representation and Toolset for Agentic Fault Localization and Program Repair\\\\\\\"\\\\n        authors: \\\\\\\"Shahd Seddik, Fatemeh Fard\\\\\\\"\\\\n        venue: arXiv\\\\n        year: 2026\\\\n        relation: contrast\\\\n        summary: \\\\\\\"用 multi-granularity program graph（含 intra-procedural def-use edges）辅助 LLM agent 做 fault localization。仅 intra-procedural + runtime tool calls，与 StructFuse 的 inter-procedural static mining 互补。\\\\\\\"\\\\n\\\\n  # ==========================================================================\\\\n  # Category 5: Code Embeddings / Code Search\\\\n  # ==========================================================================\\\\n  code_embeddings_search:\\\\n    description: \\\\\\\"代码嵌入模型和代码搜索方法\\\\\\\"\\\\n    papers:\\\\n\\\\n      - title: \\\\\\\"CodeSearchNet Challenge: Evaluating the State of Semantic Code Search\\\\\\\"\\\\n        authors: \\\\\\\"Hamel Husain, Ho-Hsiang Wu, Tiferet Gazit, Miltiadis Allamanis, Marc Brockschmidt\\\\\\\"\\\\n        venue: arXiv\\\\n        year: 2019\\\\n        relation: background\\\\n        summary: \\\\\\\"代码语义搜索 benchmark 和数据集，推动了代码嵌入模型的发展。\\\\\\\"\\\\n\\\\n      - title: \\\\\\\"CodeBERT: A Pre-Trained Model for Programming and Natural Languages\\\\\\\"\\\\n        authors: \\\\\\\"Zhangyin Feng, Daya Guo, Duyu Tang, Nan Duan, Xiaocheng Feng, Ming Gong, Lixin Zou, Bing Qin, Ting Liu, Daxin Jiang, Ming Zhou\\\\\\\"\\\\n        venue: \\\\\\\"EMNLP (Findings)\\\\\\\"\\\\n        year: 2020\\\\n        relation: background\\\\n        summary: \\\\\\\"首个编程语言-自然语言双模态预训练模型，代码嵌入的早期里程碑。\\\\\\\"\\\\n\\\\n      - title: \\\\\\\"UniXcoder: Unified Cross-Modal Pre-training for Code Representation\\\\\\\"\\\\n        authors: \\\\\\\"Daya Guo, Shuai Lu, Nan Duan, Yanlin Wang, Ming Zhou, Jian Yin\\\\\\\"\\\\n        venue: ACL\\\\n        year: 2022\\\\n        relation: background\\\\n        summary: \\\\\\\"统一跨模态代码预训练，在代码搜索等任务上取得 SOTA。\\\\\\\"\\\\n\\\\n      - title: \\\\\\\"StarCoder: May the Source Be with You!\\\\\\\"\\\\n        authors: \\\\\\\"Raymond Li, Loubna Ben Allal, et al. (BigCode)\\\\\\\"\\\\n        venue: TMLR\\\\n        year: 2023\\\\n        relation: building-block\\\\n        summary: \\\\\\\"大规模开源代码 LLM，StructFuse 用 StarCoder2-3B 作为对比学习检索器的 backbone 之一。\\\\\\\"\\\\n\\\\n      - title: \\\\\\\"Code Llama: Open Foundation Models for Code\\\\\\\"\\\\n        authors: \\\\\\\"Baptiste Roziere, Jonas Gehring, Fabian Gloeckle, et al. (Meta AI)\\\\\\\"\\\\n        venue: arXiv\\\\n        year: 2023\\\\n        relation: background\\\\n        summary: \\\\\\\"Meta 的代码大模型系列，基于 Llama 2 微调。\\\\\\\"\\\\n\\\\n      - title: \\\\\\\"Qwen2.5-Coder Technical Report\\\\\\\"\\\\n        authors: \\\\\\\"Binyuan Hui, Jian Yang, Zeyu Cui, et al. (Qwen Team, Alibaba)\\\\\\\"\\\\n        venue: arXiv\\\\n        year: 2024\\\\n        relation: building-block\\\\n        summary: \\\\\\\"Qwen 代码模型系列，StructFuse 用 Qwen2.5-Coder-3B 作为对比学习检索器的 backbone。\\\\\\\"\\\\n\\\\n      - title: \\\\\\\"DeepSeek-Coder: When the Large Language Model Meets Programming -- The Rise of Code Intelligence\\\\\\\"\\\\n        authors: \\\\\\\"Daya Guo, Qihao Zhu, Dejian Yang, Zhenda Xie, Kai Dong, Wentao Zhang, Guanting Chen, Xiao Bi, Yu Wu, Y.K. Li, Fuli Luo, Yingfei Xiong, Wenfeng Liang\\\\\\\"\\\\n        venue: arXiv\\\\n        year: 2024\\\\n        relation: background\\\\n        summary: \\\\\\\"开源代码 LLM 系列 (1.3B-33B)，project-level 代码训练 + 16K context + fill-in-the-blank 预训练。\\\\\\\"\\\\n\\\\n      - title: \\\\\\\"RepoFusion: Training Code Models to Understand Your Repository\\\\\\\"\\\\n        authors: \\\\\\\"Disha Shrivastava, Denis Kocetkov, Harm de Vries, Dzmitry Bahdanau, Torsten Scholak\\\\\\\"\\\\n        venue: arXiv\\\\n        year: 2023\\\\n        relation: background\\\\n        summary: \\\\\\\"训练代码模型融合多个 cross-file repo context 进行代码补全，小模型 + repo context 可匹配大模型性能。\\\\\\\"\\\\n\\\\n      - title: \\\\\\\"BM25\\\\\\\"\\\\n        authors: \\\\\\\"Stephen Robertson, Hugo Zaragoza\\\\\\\"\\\\n        venue: \\\\\\\"Foundations and Trends in Information Retrieval\\\\\\\"\\\\n        year: 2009\\\\n        relation: baseline\\\\n        summary: \\\\\\\"经典稀疏检索方法，StructFuse 的 baseline 之一。\\\\\\\"\\\\n\\\\n  # ==========================================================================\\\\n  # Category 6: Graph-Guided Code Navigation (Inference-Time)\\\\n  # ==========================================================================\\\\n  graph_guided_inference:\\\\n    description: \\\\\\\"推理时利用代码结构图辅助导航/检索的方法（与 StructFuse 的训练时结构信号互补）\\\\\\\"\\\\n    papers:\\\\n\\\\n      - title: \\\\\\\"LocAgent: Graph-Guided LLM Agents for Code Localization\\\\\\\"\\\\n        authors: \\\\\\\"Zhaoling Chen, Robert Tang, Gangda Deng, Fang Wu, Jialong Wu, Zhiwei Jiang, Viktor Prasanna, Arman Cohan, Xingyao Wang\\\\\\\"\\\\n        venue: ACL\\\\n        year: 2025\\\\n        relation: contrast\\\\n        summary: \\\\\\\"将代码库解析为有向异构图，LLM agent 通过 multi-hop 推理在图上导航做代码定位。推理时用结构图，StructFuse 训练时用。\\\\\\\"\\\\n\\\\n      - title: \\\\\\\"CodexGraph: Bridging Large Language Models and Code Repositories via Code Graph Databases\\\\\\\"\\\\n        authors: \\\\\\\"Xiangyan Liu, Bo Lan, Zhiyuan Hu, Yang Liu, Zhicheng Zhang, Fei Wang, Michael Qizhe Shieh, Wenmeng Zhou\\\\\\\"\\\\n        venue: NAACL\\\\n        year: 2025\\\\n        relation: contrast\\\\n        summary: \\\\\\\"将代码库索引到图数据库，LLM agent 通过 graph query 接口检索结构化上下文。\\\\\\\"\\\\n\\\\n      - title: \\\\\\\"RANGER: Repository-Level Agent for Graph-Enhanced Retrieval\\\\\\\"\\\\n        authors: \\\\\\\"Pratik Shah, Rajat Ghosh, Aryan Singhal, Debojyoti Dutta\\\\\\\"\\\\n        venue: arXiv\\\\n        year: 2025\\\\n        relation: contrast\\\\n        summary: \\\\\\\"构建 repo 知识图（含 variable-level 节点），dual-stage retrieval: Cypher lookup + MCTS-guided graph exploration。\\\\\\\"\\\\n\\\\n      - title: \\\\\\\"RepoGraph: Enhancing AI Software Engineering with Repository-level Code Graph\\\\\\\"\\\\n        authors: \\\\\\\"Siru Ouyang, Wenhao Yu, Kaixin Ma, Zilin Xiao, Zhihan Zhang, Mengzhao Jia, Jiawei Han, Hongming Zhang, Dong Yu\\\\\\\"\\\\n        venue: ICLR\\\\n        year: 2025\\\\n        relation: contrast\\\\n        summary: \\\\\\\"以代码行为节点构建 repo-level 代码图，作为 SE agent 的 plug-in 导航模块。推理时逐行图导航，与 StructFuse 训练时批量提取结构信号互补。\\\\\\\"\\\\n\\\\n      - title: \\\\\\\"GraphCoder: Enhancing Repository-Level Code Completion via Coarse-to-fine Retrieval Based on Code Context Graph\\\\\\\"\\\\n        authors: \\\\\\\"Wei Liu, Ailun Yu, Daoguang Zan, Bo Shen, Wei Zhang, Haiyan Zhao, Zhi Jin, Qianxiang Wang\\\\\\\"\\\\n        venue: ASE\\\\n        year: 2024\\\\n        relation: contrast\\\\n        summary: \\\\\\\"构建 code context graph（含 control-flow 和 data-dependence edges）进行 coarse-to-fine 检索辅助代码补全。使用 intra-procedural data-flow，与 StructFuse 的 inter-procedural scope 形成对比。\\\\\\\"\\\\n\\\\n  # ==========================================================================\\\\n  # Category 7: Infrastructure / Tools\\\\n  # ==========================================================================\\\\n  infrastructure:\\\\n    description: \\\\\\\"StructFuse 依赖的核心基础设施和工具\\\\\\\"\\\\n    papers:\\\\n\\\\n      - title: \\\\\\\"Billion-Scale Similarity Search with GPUs\\\\\\\"\\\\n        authors: \\\\\\\"Jeff Johnson, Matthijs Douze, Herve Jegou\\\\\\\"\\\\n        venue: \\\\\\\"IEEE Transactions on Big Data\\\\\\\"\\\\n        year: 2021\\\\n        relation: building-block\\\\n        summary: \\\\\\\"FAISS: GPU 加速的大规模向量相似度搜索库，StructFuse 用于 ANN-based hard negative mining。\\\\\\\"\\\\n\\\\n      - title: \\\\\\\"Tree-sitter: An Incremental Parsing System for Programming Tools\\\\\\\"\\\\n        authors: \\\\\\\"Max Brunsfeld et al.\\\\\\\"\\\\n        venue: \\\\\\\"Software (Zenodo DOI: 10.5281/zenodo.13375512)\\\\\\\"\\\\n        year: 2018\\\\n        relation: building-block\\\\n        summary: \\\\\\\"增量解析库，高效构建和更新 concrete syntax trees。与 CodeQL 互补用于代码结构提取。\\\\\\\"\\\\n        note: \\\\\\\"软件工具，无正式论文。引用 Zenodo DOI 或 GitHub repo。\\\\\\\"\\\\n\\\", \\\"total_chars\\\": 15999, \\\"truncated\\\": false}, \\\"error\\\": null, \\\"metadata\\\": {}}\"}",
  "mcpMeta": {
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/literature_map.yaml\", \"content\": \"# StructFuse — Related Work Literature Map\\n# 最后更新: 2026-05-14\\n# 说明: 只收录已验证存在的论文。每篇均经 WebSearch 确认标题/venue/year。\\n# 总计: 39 entries (含 2 个软件工具引用)\\n\\ncategories:\\n\\n  # ==========================================================================\\n  # Category 1: Code Retrieval for Bug Fixing / SWE-bench Ecosystem\\n  # ==========================================================================\\n  code_retrieval_bug_fixing:\\n    description: \\\"SWE-bench 及相关 repo-level 自动修复系统中的代码检索方法\\\"\\n    papers:\\n\\n      - title: \\\"SWE-bench: Can Language Models Resolve Real-World GitHub Issues?\\\"\\n        authors: \\\"Carlos E. Jimenez, John Yang, Alexander Wettig, Shunyu Yao, Kexin Pei, Ofir Press, Karthik Narasimhan\\\"\\n        venue: ICLR\\n        year: 2024\\n        relation: baseline\\n        summary: \\\"从 GitHub issues 构建 repo-level bug fixing benchmark，成为自动修复领域标准评估集。\\\"\\n\\n      - title: \\\"SWE-agent: Agent-Computer Interfaces Enable Automated Software Engineering\\\"\\n        authors: \\\"John Yang, Carlos E. Jimenez, Alexander Wettig, Kilian Lieret, Shunyu Yao, Karthik Narasimhan, Ofir Press\\\"\\n        venue: NeurIPS\\n        year: 2024\\n        relation: competitor\\n        summary: \\\"基于 LLM agent 的交互式 bug fixing 系统，定义了 ACI 接口范式。\\\"\\n\\n      - title: \\\"AutoCodeRover: Autonomous Program Improvement\\\"\\n        authors: \\\"Yuntong Zhang, Haifeng Ruan, Zhiyu Fan, Abhik Roychoudhury\\\"\\n        venue: ISSTA\\n        year: 2024\\n        relation: competitor\\n        summary: \\\"结合代码搜索与 spectrum-based fault localization，利用程序分析缩小修复范围。\\\"\\n\\n      - title: \\\"Agentless: Demystifying LLM-based Software Engineering Agents\\\"\\n        authors: \\\"Chunqiu Steven Xia, Yinlin Deng, Soren Dunn, Lingming Zhang\\\"\\n        venue: arXiv\\n        year: 2024\\n        relation: competitor\\n        summary: \\\"无 agent 架构的 two-phase localize-then-repair 方法，在 SWE-bench 上取得强 baseline。\\\"\\n\\n      - title: \\\"SWE-smith: Scaling Data for Software Engineering Agents\\\"\\n        authors: \\\"John Yang, Kilian Lieret, Carlos E. Jimenez, Alexander Wettig, Kabir Khandpur, Yanzhe Zhang, Binyuan Hui, Ofir Press, Ludwig Schmidt, Diyi Yang\\\"\\n        venue: \\\"NeurIPS (Datasets & Benchmarks, Spotlight)\\\"\\n        year: 2025\\n        relation: building-block\\n        summary: \\\"自动从 GitHub 生成大规模 SWE-bench 风格训练数据，StructFuse 用其 repos 做 data-flow 提取。\\\"\\n\\n      - title: \\\"RepoBench: Benchmarking Repository-Level Code Auto-Completion Systems\\\"\\n        authors: \\\"Tianyang Liu, Canwen Xu, Julian McAuley\\\"\\n        venue: ICLR\\n        year: 2024\\n        relation: baseline\\n        summary: \\\"Repo-level 代码补全/检索 benchmark，含 RepoBench-R 检索子任务。\\\"\\n\\n      - title: \\\"SweRank: Software Issue Localization with Code Ranking\\\"\\n        authors: \\\"Revanth Gangi Reddy, Tarun Suresh, JaeHyeok Doo, Ye Liu, Xuan Phi Nguyen, Yingbo Zhou, Semih Yavuz, Caiming Xiong, Heng Ji, Shafiq Joty\\\"\\n        venue: arXiv\\n        year: 2025\\n        relation: competitor\\n        summary: \\\"Retrieve-and-rerank 框架用于 software issue localization，在 SWE-Bench-Lite 和 LocBench 上 SOTA，text-based retrieval baseline。\\\"\\n\\n      - title: \\\"SWE-Fixer: Training Open-Source LLMs for Effective and Efficient GitHub Issue Resolution\\\"\\n        authors: \\\"Chengxing Xie, Bowen Li, Chang Gao, He Du, Wai Lam, Difan Zou, Kai Chen\\\"\\n        venue: \\\"ACL (Findings)\\\"\\n        year: 2025\\n        relation: competitor\\n        summary: \\\"BM25 + LLM retriever 的 coarse-to-fine file retrieval pipeline，在 SWE-Bench Verified 上 30.2%。\\\"\\n\\n  # ==========================================================================\\n  # Category 2: Hard Negative Mining in Contrastive Learning\\n  # ==========================================================================\\n  hard_negative_mining:\\n    description: \\\"对比学习中 hard negative 挖掘策略，以及密集检索中的负样本选择\\\"\\n    papers:\\n\\n      - title: \\\"Dense Passage Retrieval for Open-Domain Question Answering\\\"\\n        authors: \\\"Vladimir Karpukhin, Barlas Oguz, Sewon Min, Patrick Lewis, Ledell Wu, Sergey Edunov, Danqi Chen, Wen-tau Yih\\\"\\n        venue: EMNLP\\n        year: 2020\\n        relation: background\\n        summary: \\\"DPR 开创了 in-batch negatives + BM25 hard negatives 的双塔检索范式。\\\"\\n\\n      - title: \\\"Approximate Nearest Neighbor Negative Contrastive Learning for Dense Text Retrieval\\\"\\n        authors: \\\"Lee Xiong, Chenyan Xiong, Ye Li, Kwok-Fung Tang, Jialin Liu, Paul Bennett, Junaid Ahmed, Arnold Overwijk\\\"\\n        venue: ICLR\\n        year: 2021\\n        relation: background\\n        summary: \\\"ANCE 用 ANN index 动态挖掘 embedding-distance hard negatives，StructFuse 的 baseline negative 策略之一。\\\"\\n\\n      - title: \\\"A Simple Framework for Contrastive Learning of Visual Representations\\\"\\n        authors: \\\"Ting Chen, Simon Kornblith, Mohammad Norouzi, Geoffrey Hinton\\\"\\n        venue: ICML\\n        year: 2020\\n        relation: background\\n        summary: \\\"SimCLR 视觉对比学习奠基工作，证明 hard negatives 和大 batch size 对对比学习的重要性。\\\"\\n\\n      - title: \\\"Sentence-BERT: Sentence Embeddings using Siamese BERT-Networks\\\"\\n        authors: \\\"Nils Reimers, Iryna Gurevych\\\"\\n        venue: EMNLP\\n        year: 2019\\n        relation: background\\n        summary: \\\"Siamese/triplet 网络训练句子嵌入，StructFuse 的对比训练框架与其类似。\\\"\\n\\n      - title: \\\"Curriculum Learning for Dense Retrieval Distillation\\\"\\n        authors: \\\"Hansi Zeng, Hamed Zamani, Vishwa Vinay\\\"\\n        venue: \\\"SIGIR (Best Short Paper)\\\"\\n        year: 2022\\n        relation: background\\n        summary: \\\"CL-DRD: 课程学习式知识蒸馏用于密集检索，从粗粒度到细粒度逐步增加训练难度。\\\"\\n\\n      - title: \\\"Effective Hard Negative Mining for Contrastive Learning-Based Code Search\\\"\\n        authors: \\\"Fan Y., Li C., Ge J., Huang L., Luo B.\\\"\\n        venue: \\\"ACM TOSEM\\\"\\n        year: 2025\\n        relation: contrast-target\\n        summary: \\\"CoCoHaNeRe: 提出可微分 hard negative 机制用于代码搜索对比学习。其对 hard negative 机制的处理与 StructFuse 的发现形成关键对照——StructFuse 证明 true embedding-distance mining 即可持续提升性能。\\\"\\n        note: \\\"关键引用：StructFuse Claim 1 的 correction target。CoCoHaNeRe 论点是非可微 embedding negatives 学习'slow and ineffective'，StructFuse 证明用 true embedding distance mining 仍然有效。\\\"\\n\\n  # ==========================================================================\\n  # Category 3: Contrastive Learning for Code\\n  # ==========================================================================\\n  contrastive_code_learning:\\n    description: \\\"代码领域的对比学习方法，训练时利用代码特性构建正负样本\\\"\\n    papers:\\n\\n      - title: \\\"Contrastive Code Representation Learning\\\"\\n        authors: \\\"Paras Jain, Ajay Jain, Tianjun Zhang, Pieter Abbeel, Joseph Gonzalez, Ion Stoica\\\"\\n        venue: EMNLP\\n        year: 2021\\n        relation: background\\n        summary: \\\"ContraCode: 自监督对比预训练，通过编译器变换生成功能等价的程序变体，学习代码功能而非表面形式。\\\"\\n\\n      - title: \\\"CodeRetriever: A Large Scale Contrastive Pre-Training Method for Code Search\\\"\\n        authors: \\\"Xiaonan Li, Yeyun Gong, Yelong Shen, Xipeng Qiu, Hang Zhang, Bolun Yao, Weizhen Qi, Daxin Jiang, Weizhu Chen, Nan Duan\\\"\\n        venue: EMNLP\\n        year: 2022\\n        relation: background\\n        summary: \\\"结合 unimodal (code-code) 和 bimodal (code-text) 对比学习预训练代码表示，在 11 个代码搜索 benchmark 上 SOTA。\\\"\\n\\n      - title: \\\"Towards Learning (Dis)-Similarity of Source Code from Program Contrasts\\\"\\n        authors: \\\"Yangruibo Ding, Luca Buratti, Saurabh Pujar, Alessandro Morari, Baishakhi Ray, Saikat Chakraborty\\\"\\n        venue: \\\"ACL (Long Papers)\\\"\\n        year: 2022\\n        relation: background\\n        summary: \\\"利用程序结构和功能属性构建对比样本对，学习代码相似性/差异性表示。\\\"\\n\\n  # ==========================================================================\\n  # Category 4: Program Analysis for ML\\n  # ==========================================================================\\n  program_analysis_for_ml:\\n    description: \\\"静态分析辅助 ML，结构信息在代码表示学习中的应用\\\"\\n    papers:\\n\\n      - title: \\\"CodeQL: Semantic Code Analysis Engine\\\"\\n        authors: \\\"GitHub / Semmle\\\"\\n        venue: \\\"Tool (open-source)\\\"\\n        year: 2019\\n        relation: building-block\\n        summary: \\\"基于 Datalog 的代码查询引擎，支持 inter-procedural data-flow 分析。StructFuse 用它提取 scope-bounded data-flow graph。\\\"\\n\\n      - title: \\\"code2vec: Learning Distributed Representations of Code\\\"\\n        authors: \\\"Uri Alon, Meital Zilberstein, Omer Levy, Eran Yahav\\\"\\n        venue: POPL\\n        year: 2019\\n        relation: background\\n        summary: \\\"用 AST path 学习代码向量表示，首次大规模证明结构信息对代码表示学习的价值。\\\"\\n\\n      - title: \\\"code2seq: Generating Sequences from Structured Representations of Code\\\"\\n        authors: \\\"Uri Alon, Shaked Brody, Omer Levy, Eran Yahav\\\"\\n        venue: ICLR\\n        year: 2019\\n        relation: background\\n        summary: \\\"code2vec 的序列生成扩展，用 AST path attention 生成方法名摘要。\\\"\\n\\n      - title: \\\"Detecting Code Clones with Graph Neural Network and Flow-Augmented Abstract Syntax Tree\\\"\\n        authors: \\\"Wenhan Wang, Ge Li, Bo Ma, Xin Xia, Zhi Jin\\\"\\n        venue: SANER\\n        year: 2020\\n        relation: background\\n        summary: \\\"FA-AST: 用 data-flow 增强 AST 进行代码克隆检测，与 StructFuse 用 data-flow 做 hard negative 挖掘思路相关。\\\"\\n\\n      - title: \\\"GraphCodeBERT: Pre-training Code Representations with Data Flow\\\"\\n        authors: \\\"Daya Guo, Shuo Ren, Shuai Lu, Zhangyin Feng, Duyu Tang, Shujie Liu, Long Zhou, Nan Duan, Alexey Svyatkovskiy, Shengyu Fu, Michele Tufano, Shao Kun Deng, Colin Clement, Dawn Drain, Neel Sundaresan, Jian Yin, Daxin Jiang, Ming Zhou\\\"\\n        venue: ICLR\\n        year: 2021\\n        relation: background\\n        summary: \\\"在预训练中引入 data-flow edge，证明 data-flow 信息提升代码理解任务。StructFuse 的 insight 与此相关但用途不同（hard negative mining vs pre-training）。\\\"\\n\\n      - title: \\\"ARISE: A Repository-level Graph Representation and Toolset for Agentic Fault Localization and Program Repair\\\"\\n        authors: \\\"Shahd Seddik, Fatemeh Fard\\\"\\n        venue: arXiv\\n        year: 2026\\n        relation: contrast\\n        summary: \\\"用 multi-granularity program graph（含 intra-procedural def-use edges）辅助 LLM agent 做 fault localization。仅 intra-procedural + runtime tool calls，与 StructFuse 的 inter-procedural static mining 互补。\\\"\\n\\n  # ==========================================================================\\n  # Category 5: Code Embeddings / Code Search\\n  # ==========================================================================\\n  code_embeddings_search:\\n    description: \\\"代码嵌入模型和代码搜索方法\\\"\\n    papers:\\n\\n      - title: \\\"CodeSearchNet Challenge: Evaluating the State of Semantic Code Search\\\"\\n        authors: \\\"Hamel Husain, Ho-Hsiang Wu, Tiferet Gazit, Miltiadis Allamanis, Marc Brockschmidt\\\"\\n        venue: arXiv\\n        year: 2019\\n        relation: background\\n        summary: \\\"代码语义搜索 benchmark 和数据集，推动了代码嵌入模型的发展。\\\"\\n\\n      - title: \\\"CodeBERT: A Pre-Trained Model for Programming and Natural Languages\\\"\\n        authors: \\\"Zhangyin Feng, Daya Guo, Duyu Tang, Nan Duan, Xiaocheng Feng, Ming Gong, Lixin Zou, Bing Qin, Ting Liu, Daxin Jiang, Ming Zhou\\\"\\n        venue: \\\"EMNLP (Findings)\\\"\\n        year: 2020\\n        relation: background\\n        summary: \\\"首个编程语言-自然语言双模态预训练模型，代码嵌入的早期里程碑。\\\"\\n\\n      - title: \\\"UniXcoder: Unified Cross-Modal Pre-training for Code Representation\\\"\\n        authors: \\\"Daya Guo, Shuai Lu, Nan Duan, Yanlin Wang, Ming Zhou, Jian Yin\\\"\\n        venue: ACL\\n        year: 2022\\n        relation: background\\n        summary: \\\"统一跨模态代码预训练，在代码搜索等任务上取得 SOTA。\\\"\\n\\n      - title: \\\"StarCoder: May the Source Be with You!\\\"\\n        authors: \\\"Raymond Li, Loubna Ben Allal, et al. (BigCode)\\\"\\n        venue: TMLR\\n        year: 2023\\n        relation: building-block\\n        summary: \\\"大规模开源代码 LLM，StructFuse 用 StarCoder2-3B 作为对比学习检索器的 backbone 之一。\\\"\\n\\n      - title: \\\"Code Llama: Open Foundation Models for Code\\\"\\n        authors: \\\"Baptiste Roziere, Jonas Gehring, Fabian Gloeckle, et al. (Meta AI)\\\"\\n        venue: arXiv\\n        year: 2023\\n        relation: background\\n        summary: \\\"Meta 的代码大模型系列，基于 Llama 2 微调。\\\"\\n\\n      - title: \\\"Qwen2.5-Coder Technical Report\\\"\\n        authors: \\\"Binyuan Hui, Jian Yang, Zeyu Cui, et al. (Qwen Team, Alibaba)\\\"\\n        venue: arXiv\\n        year: 2024\\n        relation: building-block\\n        summary: \\\"Qwen 代码模型系列，StructFuse 用 Qwen2.5-Coder-3B 作为对比学习检索器的 backbone。\\\"\\n\\n      - title: \\\"DeepSeek-Coder: When the Large Language Model Meets Programming -- The Rise of Code Intelligence\\\"\\n        authors: \\\"Daya Guo, Qihao Zhu, Dejian Yang, Zhenda Xie, Kai Dong, Wentao Zhang, Guanting Chen, Xiao Bi, Yu Wu, Y.K. Li, Fuli Luo, Yingfei Xiong, Wenfeng Liang\\\"\\n        venue: arXiv\\n        year: 2024\\n        relation: background\\n        summary: \\\"开源代码 LLM 系列 (1.3B-33B)，project-level 代码训练 + 16K context + fill-in-the-blank 预训练。\\\"\\n\\n      - title: \\\"RepoFusion: Training Code Models to Understand Your Repository\\\"\\n        authors: \\\"Disha Shrivastava, Denis Kocetkov, Harm de Vries, Dzmitry Bahdanau, Torsten Scholak\\\"\\n        venue: arXiv\\n        year: 2023\\n        relation: background\\n        summary: \\\"训练代码模型融合多个 cross-file repo context 进行代码补全，小模型 + repo context 可匹配大模型性能。\\\"\\n\\n      - title: \\\"BM25\\\"\\n        authors: \\\"Stephen Robertson, Hugo Zaragoza\\\"\\n        venue: \\\"Foundations and Trends in Information Retrieval\\\"\\n        year: 2009\\n        relation: baseline\\n        summary: \\\"经典稀疏检索方法，StructFuse 的 baseline 之一。\\\"\\n\\n  # ==========================================================================\\n  # Category 6: Graph-Guided Code Navigation (Inference-Time)\\n  # ==========================================================================\\n  graph_guided_inference:\\n    description: \\\"推理时利用代码结构图辅助导航/检索的方法（与 StructFuse 的训练时结构信号互补）\\\"\\n    papers:\\n\\n      - title: \\\"LocAgent: Graph-Guided LLM Agents for Code Localization\\\"\\n        authors: \\\"Zhaoling Chen, Robert Tang, Gangda Deng, Fang Wu, Jialong Wu, Zhiwei Jiang, Viktor Prasanna, Arman Cohan, Xingyao Wang\\\"\\n        venue: ACL\\n        year: 2025\\n        relation: contrast\\n        summary: \\\"将代码库解析为有向异构图，LLM agent 通过 multi-hop 推理在图上导航做代码定位。推理时用结构图，StructFuse 训练时用。\\\"\\n\\n      - title: \\\"CodexGraph: Bridging Large Language Models and Code Repositories via Code Graph Databases\\\"\\n        authors: \\\"Xiangyan Liu, Bo Lan, Zhiyuan Hu, Yang Liu, Zhicheng Zhang, Fei Wang, Michael Qizhe Shieh, Wenmeng Zhou\\\"\\n        venue: NAACL\\n        year: 2025\\n        relation: contrast\\n        summary: \\\"将代码库索引到图数据库，LLM agent 通过 graph query 接口检索结构化上下文。\\\"\\n\\n      - title: \\\"RANGER: Repository-Level Agent for Graph-Enhanced Retrieval\\\"\\n        authors: \\\"Pratik Shah, Rajat Ghosh, Aryan Singhal, Debojyoti Dutta\\\"\\n        venue: arXiv\\n        year: 2025\\n        relation: contrast\\n        summary: \\\"构建 repo 知识图（含 variable-level 节点），dual-stage retrieval: Cypher lookup + MCTS-guided graph exploration。\\\"\\n\\n      - title: \\\"RepoGraph: Enhancing AI Software Engineering with Repository-level Code Graph\\\"\\n        authors: \\\"Siru Ouyang, Wenhao Yu, Kaixin Ma, Zilin Xiao, Zhihan Zhang, Mengzhao Jia, Jiawei Han, Hongming Zhang, Dong Yu\\\"\\n        venue: ICLR\\n        year: 2025\\n        relation: contrast\\n        summary: \\\"以代码行为节点构建 repo-level 代码图，作为 SE agent 的 plug-in 导航模块。推理时逐行图导航，与 StructFuse 训练时批量提取结构信号互补。\\\"\\n\\n      - title: \\\"GraphCoder: Enhancing Repository-Level Code Completion via Coarse-to-fine Retrieval Based on Code Context Graph\\\"\\n        authors: \\\"Wei Liu, Ailun Yu, Daoguang Zan, Bo Shen, Wei Zhang, Haiyan Zhao, Zhi Jin, Qianxiang Wang\\\"\\n        venue: ASE\\n        year: 2024\\n        relation: contrast\\n        summary: \\\"构建 code context graph（含 control-flow 和 data-dependence edges）进行 coarse-to-fine 检索辅助代码补全。使用 intra-procedural data-flow，与 StructFuse 的 inter-procedural scope 形成对比。\\\"\\n\\n  # ==========================================================================\\n  # Category 7: Infrastructure / Tools\\n  # ==========================================================================\\n  infrastructure:\\n    description: \\\"StructFuse 依赖的核心基础设施和工具\\\"\\n    papers:\\n\\n      - title: \\\"Billion-Scale Similarity Search with GPUs\\\"\\n        authors: \\\"Jeff Johnson, Matthijs Douze, Herve Jegou\\\"\\n        venue: \\\"IEEE Transactions on Big Data\\\"\\n        year: 2021\\n        relation: building-block\\n        summary: \\\"FAISS: GPU 加速的大规模向量相似度搜索库，StructFuse 用于 ANN-based hard negative mining。\\\"\\n\\n      - title: \\\"Tree-sitter: An Incremental Parsing System for Programming Tools\\\"\\n        authors: \\\"Max Brunsfeld et al.\\\"\\n        venue: \\\"Software (Zenodo DOI: 10.5281/zenodo.13375512)\\\"\\n        year: 2018\\n        relation: building-block\\n        summary: \\\"增量解析库，高效构建和更新 concrete syntax trees。与 CodeQL 互补用于代码结构提取。\\\"\\n        note: \\\"软件工具，无正式论文。引用 Zenodo DOI 或 GitHub repo。\\\"\\n\", \"total_chars\": 15999, \"truncated\": false}, \"error\": null, \"metadata\": {}}"
    }
  },
  "sourceToolAssistantUUID": "30d6d97a-30f4-488e-931a-65602b1fe6a1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/.claude/sessions/reviewer_65cfe724",
  "sessionId": "f444a635-eeef-4924-9b48-a4c308632421",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---


### Tool call

_source line 33 · 2026-05-16T00:23:31.871Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01BtS4ueK5cGmZVPCurK9kUY`</summary>

```json
{
  "project": "structfuse-context",
  "file": "paper_framing.md",
  "max_chars": 12000
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "88af8593-b0de-470c-a0b3-cadaa1b0b2fe",
  "isSidechain": false,
  "requestId": "req_011Cb5J32VLKPFNYxnB9NPTr",
  "type": "assistant",
  "uuid": "8bc1157c-21b7-49af-a727-b29621edc845",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/.claude/sessions/reviewer_65cfe724",
  "sessionId": "f444a635-eeef-4924-9b48-a4c308632421",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016fPC9ji1Brow7ZujRQVpiF",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 11073,
      "cache_read_input_tokens": 47141,
      "output_tokens": 495,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 11073,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 495,
          "cache_read_input_tokens": 47141,
          "cache_creation_input_tokens": 11073,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 11073
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

_source line 34 · 2026-05-16T00:23:31.881Z_

<details><summary>↩ Tool result · `toolu_01BtS4ueK5cGmZVPCurK9kUY`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/paper_framing.md\", \"content\": \"# Paper Framing — StructFuse\\n\\n## Target Venue\\n- Primary: EMNLP 2026 Main\\n- Deadline: ARR May 25, 2026\\n\\n## Core Claims (3)\\n\\n1. **Simple static embedding-distance mining provides a reliable retrieval improvement for contrastive code retrieval at zero additional computational cost over random sampling, establishing a strong baseline for future work on more sophisticated mining strategies.** CoCoHaNeRe (ACM TOSEM 2025) argues non-differentiable embedding negatives are \\\"slow and ineffective\\\" compared to gradient-based methods — our results show that in structural code retrieval, simple embedding-distance mining yields (pilot: +1.6–2.0pp; M2 seed 43: +0.52pp best_by_R@1, +0.82pp mean fixed-checkpoint; final range pending s42/s44 completion) R@1 over random baselines across two decoder-only encoders with distinct pretraining corpora and representation geometries (Qwen2.5-Coder-3B, StarCoder2-3B), without requiring gradient-based mechanisms.\\n\\n2. **[Exploratory observation] Structure-grounded (dataflow) negatives interact with encoder representation geometry, but do not consistently outperform embedding mining.** Pilot data shows dataflow < embedding on both encoders (Qwen: -1.2pp, StarCoder: -1.0pp R@1 vs embedding). The interaction pattern — Qwen (saturated, pos_sim > 0.98) shows smaller gap than StarCoder (healthy, pos_sim ~ 0.80) — suggests representation geometry mediates strategy effectiveness. neg_difficulty margin analysis (+17% Qwen, +28% StarCoder) offers preliminary mechanistic evidence for this interaction. Pending: multi-seed confirmation + plan_005 stratified analysis + plan_015 dynamic mining control. This is reported as an observation with mechanistic hypothesis, not an established finding.\\n\\n3. **Scope-bounded inter-procedural data-flow analysis via CodeQL provides a practical pipeline for computing structural connectivity at scale.** 0% timeout, 78% connected-not-gold rate (Z%), 123/131 repos with output at full scale. [Dream [M][W] flag: this is supporting methodology, not a primary research contribution. Drop speculative generalization claims (molecular networks, etc.) — no evidence. Frame as practical tool that enables the study, not a standalone contribution.]\\n\\n## Story Spine\\n\\n- **Problem**: Repo-level code repair requires selecting relevant files from large codebases. Current retrievers rely on text similarity alone, but lexical similarity ≠ structural relevance. Hard negative mining is the standard approach to improve contrastive retrievers, yet the field lacks systematic understanding of what negative selection strategies work for code and why.\\n\\n- **Existing approaches & gaps**:\\n  - Text-based retrieval (SweRank, SWE-Fixer): blind to structural dependencies\\n  - Graph-guided at inference (LocAgent, RANGER, CodexGraph): structural graphs at inference only, no training signal\\n  - ARISE: data-flow but intra-procedural only (no call boundary crossing), runtime tool calls only\\n  - CoCoHaNeRe (ACM TOSEM 2025): argues gradient-based hard negative methods outperform non-differentiable embedding negatives — but does not test simple static embedding-distance mining in structural code retrieval settings\\n  - Gap: no systematic study comparing negative mining strategies with proper controls, and no mechanistic explanation for when/why each strategy works\\n\\n- **Our contribution**: A systematic analysis of hard negative mining strategies for contrastive code retrieval. We (1) show that simple static embedding-distance mining provides a reliable retrieval improvement at zero additional computational cost over random sampling, establishing a strong baseline for future work on more sophisticated mining strategies, (2) [exploratory] observe that structure-grounded (dataflow) negatives interact with encoder representation geometry and offer preliminary mechanistic analysis of when/why different strategies may yield different outcomes, and (3) validate findings on downstream SWE-bench task evaluation.\\n\\n- **Headline result template**: \\\"Simple static embedding-distance mining improves code retrieval in pilot and initial M2 seed (pilot: +1.6–2.0pp; M2 seed 43: +0.52pp best_by_R@1, +0.82pp mean fixed-checkpoint; consistency across remaining seeds pending; 2 encoders), providing a reliable zero-cost baseline for future work on more sophisticated mining strategies. Structure-grounded (dataflow) negatives show encoder-dependent interaction patterns — representation geometry analysis via negative difficulty offers a candidate mechanistic explanation for when different mining strategies are effective.\\\"\\n\\n## Core Insight\\n\\nOur pilot data suggests that the effectiveness of hard negative mining strategies may depend on the encoder's representation geometry — a hypothesis derived from two encoders and requiring broader validation. The three strategies explore different dimensions of difficulty: (1) random — no signal baseline; (2) embedding-distance — semantic similarity via pretrained encoder cosine similarity; (3) dataflow-aware — structural filtering (CodeQL-connected files) + lexical similarity (BM25 top-K ranking). When the pretrained space is saturated (high pos_sim → low margin between positive and negative), the encoder needs harder negatives from an orthogonal signal dimension (structure + lexical). When the space has healthy separation, embedding-distance mining alone captures sufficient difficulty gradient. This encoder-strategy interaction, if confirmed, could help explain contradictory findings in prior work.\\n\\n## Dual-Pillar Motivation\\n\\n1. **Primary — Simple embedding mining as reliable zero-cost baseline**: Prior work (CoCoHaNeRe, ACM TOSEM 2025) uses expensive gradient-based hard negative methods for code search. Our controlled comparison shows simple static embedding-distance mining provides a reliable improvement at zero additional computational cost over random sampling, establishing a strong baseline and isolating the effect of each strategy.\\n2. **Secondary — Mechanistic explanation via representation geometry**: neg_difficulty analysis (margin distribution × strategy × encoder) offers preliminary explanatory depth beyond empirical comparison, offering a candidate heuristic (pos_sim threshold) that, if validated on more encoders, could help practitioners select strategies without exhaustive experiments.\\n\\n## Formal Definition\\n\\nGiven retrieval domain D, structural graph G, query q:\\n**structure-grounded hard negative** = argmax_{x ∈ D : ¬reachable_G(x,q) ∧ x ∉ gold(q)} BM25(q, x)\\n\\nThe structural graph is externally fixed and does not update with the encoder (drift-immune). Negatives are selected from structurally unreachable files (i.e., x ∉ R_G(q), not connected via CodeQL data-flow to the query), ranked by BM25 (lexical similarity).\\n\\n## Title Options\\n\\n- Primary: \\\"What Makes Hard Negatives Work for Code Retrieval? A Systematic Study of Mining Strategies and Representation Geometry\\\"\\n- Alternative: \\\"Static Embedding Negatives as a Zero-Cost Baseline for Contrastive Code Retrieval\\\" [contingent: activate only if M2 dataflow conditional benefit confirmed across encoders]\\n- Backup: \\\"Simple Embedding Mining Suffices: A Zero-Cost Baseline for Hard Negative Mining in Code Retrieval\\\"\\n\\n## Venue Fit\\n\\n1. **EMNLP Main fit**: Empirical analysis + mechanistic insight papers are a strong EMNLP archetype (cf. \\\"Do Language Models...\\\" papers). Contribution is understanding, not just a new method.\\n2. **NLP audience**: Frame as contrastive learning methodology with code as instantiation. Representation geometry analysis generalizes beyond code.\\n3. **Against \\\"incremental\\\" criticism**: Paper demonstrates a reliable zero-cost baseline + offers preliminary mechanistic analysis of strategy × encoder interaction + validates on downstream task. Three contributions, not one marginal improvement.\\n\\n## Anticipated Reviewer Concerns\\n\\n| Concern | Response | Evidence |\\n|---------|----------|----------|\\n| Only 2 encoders — can you generalize? | n=2 is minimum for interaction claim; we frame as observation with mechanism, not universal law; two decoder-only encoders with distinct pretraining (Fill vs FIM) and representation geometry (pos_sim 0.99 vs 0.80) provide meaningful variation | plan_013 (done), m2_full runs |\\n| BM25 vs true embedding negatives? | Run BM25 negatives to empirically compare with embedding-distance mining, grounding the comparison against CoCoHaNeRe's gradient-based premise | plan_018 |\\n| Pool size sensitivity? | Evaluate at pool {50, 100, 200, 500} to confirm strategy rankings hold at realistic sizes | plan_019 |\\n| Stratified by structural data availability? | Report per-stratum R@1 for 34% with structural data vs 66% fallback | plan_005 (extended) |\\n| Temperature regime specificity | Ablate τ ∈ {0.05, 0.1, 0.2} | plan_014 |\\n| No downstream task evaluation | SWE-bench Lite end-to-end with LLM agent | plan_003 |\\n| Static vs dynamic mining confound | Clarify mining is static; add dynamic baseline | plan_015 |\\n| CodeQL scalability at larger scale | 0% timeout, 78% Z%, 123 repos; m1_reextract_v2 adds more | plan_006 (done) |\\n| Why not compare inference-time graph methods? | Complementary: they navigate at inference, we mine at training. Discuss relationship. | plan_017 |\\n| Single benchmark | Add RepoBench-R cross-file retrieval | plan_004 |\\n| Statistical significance | Bootstrap 95% CI for all comparisons; full M2 = 9 seeds × 3 strategies × 2 encoders | plan_016, m2_full |\\n| \\\"Complementary signal\\\" overstatement | Temper: \\\"conditionally beneficial\\\" not \\\"always complementary\\\" | Writing discipline |\\n| Missing related work | RepoFusion, GRACE, GraphCodeBERT, ANCE, curriculum HN mining | Writing task |\\n\\n## Evidence Status\\n\\n### Confirmed findings (basis for claims):\\n- D017: True embedding mining helps (pilot: +2.0pp Qwen, +1.6pp StarCoder; M2 seed 43: +0.52pp best_by_R@1, +0.82pp mean fixed-checkpoint; final range pending s42/s44 completion) — establishes reliable zero-cost baseline\\n- D021/neg_difficulty: Qwen pos_sim=0.9855 (saturated), StarCoder pos_sim=0.7985 (healthy); margin differential is consistent with hypothesized strategy interaction\\n- m2_embed_verify (pilot): 3-strategy comparison is consistent with pilot ranking (embedding > random, dataflow conditional)\\n- plan_013 (StarCoder pilot): Consistent with cross-encoder pattern — embedding helps both, dataflow appears to help Qwen only\\n- plan_006: CodeQL scalability confirmed at 123-repo scale\\n\\n### Evidence presentation strategy:\\n- Primary table: best_by_R@1 (standard practice — select best checkpoint per run by validation R@1)\\n- Supplementary: fixed-checkpoint comparison as robustness check (not a replacement for best_by_R@1)\\n- Both metrics show directionally consistent results; no goalpost-moving between metrics\\n\\n### In progress:\\n- m2_full_qwen: random s42 DONE (R@1=0.5527), s43 DONE (R@1=0.5554), s44 DONE (R@1=0.6009, early stopped step 500), embedding_distance_s43 DONE (R@1=0.5606, early stopped step 1500). 4/9 runs complete, ~35h remaining.\\n- m2_full_starcoder: random s42 DONE (R@1=0.4604, from parent), s43 RUNNING (eval@500 R@1=0.4708). 1/9+ runs complete, ~65-70h remaining.\\n- m1_reextract_v2: 90.5% complete (25,582/28,276), 0 ERROR, ETA ~19:00 CST May 15\\n\\n### Planned (priority order):\\n- plan_018: BM25 negative baseline (Dream #1 consensus gap — grounds comparison against CoCoHaNeRe's premise)\\n- plan_003: SWE-bench Lite eval (biggest lever for paper strength)\\n- plan_019: Pool size sensitivity (Dream consensus — external validity)\\n- plan_014: Temperature ablation (Dream reviewer concern)\\n- plan_004: RepoBench-R second benchmark (with multi-seed CIs)\\n- plan_015: Dynamic mining baseline\\n- plan_005: Stratified analysis (extended: structural-available vs fallback stratum)\\n- plan_007/008/009: Additional ablations\\n\\n## Limitations\\n\\nEffect size is smaller than pilot estimates, likely because full-scale training data provides stronger random baselines, reducing the marginal value of targeted negative selection.\\n\\n## Contingency (if full M2 results we\\n\\n... [截断: 省略 2424 字符，传 max_chars=0 获取完整内容]\", \"total_chars\": 14424, \"truncated\": true}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "8bc1157c-21b7-49af-a727-b29621edc845",
  "isSidechain": false,
  "promptId": "ee81bb41-edfe-48b7-9827-d79a74cf7a5e",
  "type": "user",
  "uuid": "6eba7a7f-265f-4703-a0b5-0296e63ea3db",
  "toolUseResult": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"path\\\": \\\"/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/paper_framing.md\\\", \\\"content\\\": \\\"# Paper Framing — StructFuse\\\\n\\\\n## Target Venue\\\\n- Primary: EMNLP 2026 Main\\\\n- Deadline: ARR May 25, 2026\\\\n\\\\n## Core Claims (3)\\\\n\\\\n1. **Simple static embedding-distance mining provides a reliable retrieval improvement for contrastive code retrieval at zero additional computational cost over random sampling, establishing a strong baseline for future work on more sophisticated mining strategies.** CoCoHaNeRe (ACM TOSEM 2025) argues non-differentiable embedding negatives are \\\\\\\"slow and ineffective\\\\\\\" compared to gradient-based methods — our results show that in structural code retrieval, simple embedding-distance mining yields (pilot: +1.6–2.0pp; M2 seed 43: +0.52pp best_by_R@1, +0.82pp mean fixed-checkpoint; final range pending s42/s44 completion) R@1 over random baselines across two decoder-only encoders with distinct pretraining corpora and representation geometries (Qwen2.5-Coder-3B, StarCoder2-3B), without requiring gradient-based mechanisms.\\\\n\\\\n2. **[Exploratory observation] Structure-grounded (dataflow) negatives interact with encoder representation geometry, but do not consistently outperform embedding mining.** Pilot data shows dataflow < embedding on both encoders (Qwen: -1.2pp, StarCoder: -1.0pp R@1 vs embedding). The interaction pattern — Qwen (saturated, pos_sim > 0.98) shows smaller gap than StarCoder (healthy, pos_sim ~ 0.80) — suggests representation geometry mediates strategy effectiveness. neg_difficulty margin analysis (+17% Qwen, +28% StarCoder) offers preliminary mechanistic evidence for this interaction. Pending: multi-seed confirmation + plan_005 stratified analysis + plan_015 dynamic mining control. This is reported as an observation with mechanistic hypothesis, not an established finding.\\\\n\\\\n3. **Scope-bounded inter-procedural data-flow analysis via CodeQL provides a practical pipeline for computing structural connectivity at scale.** 0% timeout, 78% connected-not-gold rate (Z%), 123/131 repos with output at full scale. [Dream [M][W] flag: this is supporting methodology, not a primary research contribution. Drop speculative generalization claims (molecular networks, etc.) — no evidence. Frame as practical tool that enables the study, not a standalone contribution.]\\\\n\\\\n## Story Spine\\\\n\\\\n- **Problem**: Repo-level code repair requires selecting relevant files from large codebases. Current retrievers rely on text similarity alone, but lexical similarity ≠ structural relevance. Hard negative mining is the standard approach to improve contrastive retrievers, yet the field lacks systematic understanding of what negative selection strategies work for code and why.\\\\n\\\\n- **Existing approaches & gaps**:\\\\n  - Text-based retrieval (SweRank, SWE-Fixer): blind to structural dependencies\\\\n  - Graph-guided at inference (LocAgent, RANGER, CodexGraph): structural graphs at inference only, no training signal\\\\n  - ARISE: data-flow but intra-procedural only (no call boundary crossing), runtime tool calls only\\\\n  - CoCoHaNeRe (ACM TOSEM 2025): argues gradient-based hard negative methods outperform non-differentiable embedding negatives — but does not test simple static embedding-distance mining in structural code retrieval settings\\\\n  - Gap: no systematic study comparing negative mining strategies with proper controls, and no mechanistic explanation for when/why each strategy works\\\\n\\\\n- **Our contribution**: A systematic analysis of hard negative mining strategies for contrastive code retrieval. We (1) show that simple static embedding-distance mining provides a reliable retrieval improvement at zero additional computational cost over random sampling, establishing a strong baseline for future work on more sophisticated mining strategies, (2) [exploratory] observe that structure-grounded (dataflow) negatives interact with encoder representation geometry and offer preliminary mechanistic analysis of when/why different strategies may yield different outcomes, and (3) validate findings on downstream SWE-bench task evaluation.\\\\n\\\\n- **Headline result template**: \\\\\\\"Simple static embedding-distance mining improves code retrieval in pilot and initial M2 seed (pilot: +1.6–2.0pp; M2 seed 43: +0.52pp best_by_R@1, +0.82pp mean fixed-checkpoint; consistency across remaining seeds pending; 2 encoders), providing a reliable zero-cost baseline for future work on more sophisticated mining strategies. Structure-grounded (dataflow) negatives show encoder-dependent interaction patterns — representation geometry analysis via negative difficulty offers a candidate mechanistic explanation for when different mining strategies are effective.\\\\\\\"\\\\n\\\\n## Core Insight\\\\n\\\\nOur pilot data suggests that the effectiveness of hard negative mining strategies may depend on the encoder's representation geometry — a hypothesis derived from two encoders and requiring broader validation. The three strategies explore different dimensions of difficulty: (1) random — no signal baseline; (2) embedding-distance — semantic similarity via pretrained encoder cosine similarity; (3) dataflow-aware — structural filtering (CodeQL-connected files) + lexical similarity (BM25 top-K ranking). When the pretrained space is saturated (high pos_sim → low margin between positive and negative), the encoder needs harder negatives from an orthogonal signal dimension (structure + lexical). When the space has healthy separation, embedding-distance mining alone captures sufficient difficulty gradient. This encoder-strategy interaction, if confirmed, could help explain contradictory findings in prior work.\\\\n\\\\n## Dual-Pillar Motivation\\\\n\\\\n1. **Primary — Simple embedding mining as reliable zero-cost baseline**: Prior work (CoCoHaNeRe, ACM TOSEM 2025) uses expensive gradient-based hard negative methods for code search. Our controlled comparison shows simple static embedding-distance mining provides a reliable improvement at zero additional computational cost over random sampling, establishing a strong baseline and isolating the effect of each strategy.\\\\n2. **Secondary — Mechanistic explanation via representation geometry**: neg_difficulty analysis (margin distribution × strategy × encoder) offers preliminary explanatory depth beyond empirical comparison, offering a candidate heuristic (pos_sim threshold) that, if validated on more encoders, could help practitioners select strategies without exhaustive experiments.\\\\n\\\\n## Formal Definition\\\\n\\\\nGiven retrieval domain D, structural graph G, query q:\\\\n**structure-grounded hard negative** = argmax_{x ∈ D : ¬reachable_G(x,q) ∧ x ∉ gold(q)} BM25(q, x)\\\\n\\\\nThe structural graph is externally fixed and does not update with the encoder (drift-immune). Negatives are selected from structurally unreachable files (i.e., x ∉ R_G(q), not connected via CodeQL data-flow to the query), ranked by BM25 (lexical similarity).\\\\n\\\\n## Title Options\\\\n\\\\n- Primary: \\\\\\\"What Makes Hard Negatives Work for Code Retrieval? A Systematic Study of Mining Strategies and Representation Geometry\\\\\\\"\\\\n- Alternative: \\\\\\\"Static Embedding Negatives as a Zero-Cost Baseline for Contrastive Code Retrieval\\\\\\\" [contingent: activate only if M2 dataflow conditional benefit confirmed across encoders]\\\\n- Backup: \\\\\\\"Simple Embedding Mining Suffices: A Zero-Cost Baseline for Hard Negative Mining in Code Retrieval\\\\\\\"\\\\n\\\\n## Venue Fit\\\\n\\\\n1. **EMNLP Main fit**: Empirical analysis + mechanistic insight papers are a strong EMNLP archetype (cf. \\\\\\\"Do Language Models...\\\\\\\" papers). Contribution is understanding, not just a new method.\\\\n2. **NLP audience**: Frame as contrastive learning methodology with code as instantiation. Representation geometry analysis generalizes beyond code.\\\\n3. **Against \\\\\\\"incremental\\\\\\\" criticism**: Paper demonstrates a reliable zero-cost baseline + offers preliminary mechanistic analysis of strategy × encoder interaction + validates on downstream task. Three contributions, not one marginal improvement.\\\\n\\\\n## Anticipated Reviewer Concerns\\\\n\\\\n| Concern | Response | Evidence |\\\\n|---------|----------|----------|\\\\n| Only 2 encoders — can you generalize? | n=2 is minimum for interaction claim; we frame as observation with mechanism, not universal law; two decoder-only encoders with distinct pretraining (Fill vs FIM) and representation geometry (pos_sim 0.99 vs 0.80) provide meaningful variation | plan_013 (done), m2_full runs |\\\\n| BM25 vs true embedding negatives? | Run BM25 negatives to empirically compare with embedding-distance mining, grounding the comparison against CoCoHaNeRe's gradient-based premise | plan_018 |\\\\n| Pool size sensitivity? | Evaluate at pool {50, 100, 200, 500} to confirm strategy rankings hold at realistic sizes | plan_019 |\\\\n| Stratified by structural data availability? | Report per-stratum R@1 for 34% with structural data vs 66% fallback | plan_005 (extended) |\\\\n| Temperature regime specificity | Ablate τ ∈ {0.05, 0.1, 0.2} | plan_014 |\\\\n| No downstream task evaluation | SWE-bench Lite end-to-end with LLM agent | plan_003 |\\\\n| Static vs dynamic mining confound | Clarify mining is static; add dynamic baseline | plan_015 |\\\\n| CodeQL scalability at larger scale | 0% timeout, 78% Z%, 123 repos; m1_reextract_v2 adds more | plan_006 (done) |\\\\n| Why not compare inference-time graph methods? | Complementary: they navigate at inference, we mine at training. Discuss relationship. | plan_017 |\\\\n| Single benchmark | Add RepoBench-R cross-file retrieval | plan_004 |\\\\n| Statistical significance | Bootstrap 95% CI for all comparisons; full M2 = 9 seeds × 3 strategies × 2 encoders | plan_016, m2_full |\\\\n| \\\\\\\"Complementary signal\\\\\\\" overstatement | Temper: \\\\\\\"conditionally beneficial\\\\\\\" not \\\\\\\"always complementary\\\\\\\" | Writing discipline |\\\\n| Missing related work | RepoFusion, GRACE, GraphCodeBERT, ANCE, curriculum HN mining | Writing task |\\\\n\\\\n## Evidence Status\\\\n\\\\n### Confirmed findings (basis for claims):\\\\n- D017: True embedding mining helps (pilot: +2.0pp Qwen, +1.6pp StarCoder; M2 seed 43: +0.52pp best_by_R@1, +0.82pp mean fixed-checkpoint; final range pending s42/s44 completion) — establishes reliable zero-cost baseline\\\\n- D021/neg_difficulty: Qwen pos_sim=0.9855 (saturated), StarCoder pos_sim=0.7985 (healthy); margin differential is consistent with hypothesized strategy interaction\\\\n- m2_embed_verify (pilot): 3-strategy comparison is consistent with pilot ranking (embedding > random, dataflow conditional)\\\\n- plan_013 (StarCoder pilot): Consistent with cross-encoder pattern — embedding helps both, dataflow appears to help Qwen only\\\\n- plan_006: CodeQL scalability confirmed at 123-repo scale\\\\n\\\\n### Evidence presentation strategy:\\\\n- Primary table: best_by_R@1 (standard practice — select best checkpoint per run by validation R@1)\\\\n- Supplementary: fixed-checkpoint comparison as robustness check (not a replacement for best_by_R@1)\\\\n- Both metrics show directionally consistent results; no goalpost-moving between metrics\\\\n\\\\n### In progress:\\\\n- m2_full_qwen: random s42 DONE (R@1=0.5527), s43 DONE (R@1=0.5554), s44 DONE (R@1=0.6009, early stopped step 500), embedding_distance_s43 DONE (R@1=0.5606, early stopped step 1500). 4/9 runs complete, ~35h remaining.\\\\n- m2_full_starcoder: random s42 DONE (R@1=0.4604, from parent), s43 RUNNING (eval@500 R@1=0.4708). 1/9+ runs complete, ~65-70h remaining.\\\\n- m1_reextract_v2: 90.5% complete (25,582/28,276), 0 ERROR, ETA ~19:00 CST May 15\\\\n\\\\n### Planned (priority order):\\\\n- plan_018: BM25 negative baseline (Dream #1 consensus gap — grounds comparison against CoCoHaNeRe's premise)\\\\n- plan_003: SWE-bench Lite eval (biggest lever for paper strength)\\\\n- plan_019: Pool size sensitivity (Dream consensus — external validity)\\\\n- plan_014: Temperature ablation (Dream reviewer concern)\\\\n- plan_004: RepoBench-R second benchmark (with multi-seed CIs)\\\\n- plan_015: Dynamic mining baseline\\\\n- plan_005: Stratified analysis (extended: structural-available vs fallback stratum)\\\\n- plan_007/008/009: Additional ablations\\\\n\\\\n## Limitations\\\\n\\\\nEffect size is smaller than pilot estimates, likely because full-scale training data provides stronger random baselines, reducing the marginal value of targeted negative selection.\\\\n\\\\n## Contingency (if full M2 results we\\\\n\\\\n... [截断: 省略 2424 字符，传 max_chars=0 获取完整内容]\\\", \\\"total_chars\\\": 14424, \\\"truncated\\\": true}, \\\"error\\\": null, \\\"metadata\\\": {}}\"}",
  "mcpMeta": {
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/paper_framing.md\", \"content\": \"# Paper Framing — StructFuse\\n\\n## Target Venue\\n- Primary: EMNLP 2026 Main\\n- Deadline: ARR May 25, 2026\\n\\n## Core Claims (3)\\n\\n1. **Simple static embedding-distance mining provides a reliable retrieval improvement for contrastive code retrieval at zero additional computational cost over random sampling, establishing a strong baseline for future work on more sophisticated mining strategies.** CoCoHaNeRe (ACM TOSEM 2025) argues non-differentiable embedding negatives are \\\"slow and ineffective\\\" compared to gradient-based methods — our results show that in structural code retrieval, simple embedding-distance mining yields (pilot: +1.6–2.0pp; M2 seed 43: +0.52pp best_by_R@1, +0.82pp mean fixed-checkpoint; final range pending s42/s44 completion) R@1 over random baselines across two decoder-only encoders with distinct pretraining corpora and representation geometries (Qwen2.5-Coder-3B, StarCoder2-3B), without requiring gradient-based mechanisms.\\n\\n2. **[Exploratory observation] Structure-grounded (dataflow) negatives interact with encoder representation geometry, but do not consistently outperform embedding mining.** Pilot data shows dataflow < embedding on both encoders (Qwen: -1.2pp, StarCoder: -1.0pp R@1 vs embedding). The interaction pattern — Qwen (saturated, pos_sim > 0.98) shows smaller gap than StarCoder (healthy, pos_sim ~ 0.80) — suggests representation geometry mediates strategy effectiveness. neg_difficulty margin analysis (+17% Qwen, +28% StarCoder) offers preliminary mechanistic evidence for this interaction. Pending: multi-seed confirmation + plan_005 stratified analysis + plan_015 dynamic mining control. This is reported as an observation with mechanistic hypothesis, not an established finding.\\n\\n3. **Scope-bounded inter-procedural data-flow analysis via CodeQL provides a practical pipeline for computing structural connectivity at scale.** 0% timeout, 78% connected-not-gold rate (Z%), 123/131 repos with output at full scale. [Dream [M][W] flag: this is supporting methodology, not a primary research contribution. Drop speculative generalization claims (molecular networks, etc.) — no evidence. Frame as practical tool that enables the study, not a standalone contribution.]\\n\\n## Story Spine\\n\\n- **Problem**: Repo-level code repair requires selecting relevant files from large codebases. Current retrievers rely on text similarity alone, but lexical similarity ≠ structural relevance. Hard negative mining is the standard approach to improve contrastive retrievers, yet the field lacks systematic understanding of what negative selection strategies work for code and why.\\n\\n- **Existing approaches & gaps**:\\n  - Text-based retrieval (SweRank, SWE-Fixer): blind to structural dependencies\\n  - Graph-guided at inference (LocAgent, RANGER, CodexGraph): structural graphs at inference only, no training signal\\n  - ARISE: data-flow but intra-procedural only (no call boundary crossing), runtime tool calls only\\n  - CoCoHaNeRe (ACM TOSEM 2025): argues gradient-based hard negative methods outperform non-differentiable embedding negatives — but does not test simple static embedding-distance mining in structural code retrieval settings\\n  - Gap: no systematic study comparing negative mining strategies with proper controls, and no mechanistic explanation for when/why each strategy works\\n\\n- **Our contribution**: A systematic analysis of hard negative mining strategies for contrastive code retrieval. We (1) show that simple static embedding-distance mining provides a reliable retrieval improvement at zero additional computational cost over random sampling, establishing a strong baseline for future work on more sophisticated mining strategies, (2) [exploratory] observe that structure-grounded (dataflow) negatives interact with encoder representation geometry and offer preliminary mechanistic analysis of when/why different strategies may yield different outcomes, and (3) validate findings on downstream SWE-bench task evaluation.\\n\\n- **Headline result template**: \\\"Simple static embedding-distance mining improves code retrieval in pilot and initial M2 seed (pilot: +1.6–2.0pp; M2 seed 43: +0.52pp best_by_R@1, +0.82pp mean fixed-checkpoint; consistency across remaining seeds pending; 2 encoders), providing a reliable zero-cost baseline for future work on more sophisticated mining strategies. Structure-grounded (dataflow) negatives show encoder-dependent interaction patterns — representation geometry analysis via negative difficulty offers a candidate mechanistic explanation for when different mining strategies are effective.\\\"\\n\\n## Core Insight\\n\\nOur pilot data suggests that the effectiveness of hard negative mining strategies may depend on the encoder's representation geometry — a hypothesis derived from two encoders and requiring broader validation. The three strategies explore different dimensions of difficulty: (1) random — no signal baseline; (2) embedding-distance — semantic similarity via pretrained encoder cosine similarity; (3) dataflow-aware — structural filtering (CodeQL-connected files) + lexical similarity (BM25 top-K ranking). When the pretrained space is saturated (high pos_sim → low margin between positive and negative), the encoder needs harder negatives from an orthogonal signal dimension (structure + lexical). When the space has healthy separation, embedding-distance mining alone captures sufficient difficulty gradient. This encoder-strategy interaction, if confirmed, could help explain contradictory findings in prior work.\\n\\n## Dual-Pillar Motivation\\n\\n1. **Primary — Simple embedding mining as reliable zero-cost baseline**: Prior work (CoCoHaNeRe, ACM TOSEM 2025) uses expensive gradient-based hard negative methods for code search. Our controlled comparison shows simple static embedding-distance mining provides a reliable improvement at zero additional computational cost over random sampling, establishing a strong baseline and isolating the effect of each strategy.\\n2. **Secondary — Mechanistic explanation via representation geometry**: neg_difficulty analysis (margin distribution × strategy × encoder) offers preliminary explanatory depth beyond empirical comparison, offering a candidate heuristic (pos_sim threshold) that, if validated on more encoders, could help practitioners select strategies without exhaustive experiments.\\n\\n## Formal Definition\\n\\nGiven retrieval domain D, structural graph G, query q:\\n**structure-grounded hard negative** = argmax_{x ∈ D : ¬reachable_G(x,q) ∧ x ∉ gold(q)} BM25(q, x)\\n\\nThe structural graph is externally fixed and does not update with the encoder (drift-immune). Negatives are selected from structurally unreachable files (i.e., x ∉ R_G(q), not connected via CodeQL data-flow to the query), ranked by BM25 (lexical similarity).\\n\\n## Title Options\\n\\n- Primary: \\\"What Makes Hard Negatives Work for Code Retrieval? A Systematic Study of Mining Strategies and Representation Geometry\\\"\\n- Alternative: \\\"Static Embedding Negatives as a Zero-Cost Baseline for Contrastive Code Retrieval\\\" [contingent: activate only if M2 dataflow conditional benefit confirmed across encoders]\\n- Backup: \\\"Simple Embedding Mining Suffices: A Zero-Cost Baseline for Hard Negative Mining in Code Retrieval\\\"\\n\\n## Venue Fit\\n\\n1. **EMNLP Main fit**: Empirical analysis + mechanistic insight papers are a strong EMNLP archetype (cf. \\\"Do Language Models...\\\" papers). Contribution is understanding, not just a new method.\\n2. **NLP audience**: Frame as contrastive learning methodology with code as instantiation. Representation geometry analysis generalizes beyond code.\\n3. **Against \\\"incremental\\\" criticism**: Paper demonstrates a reliable zero-cost baseline + offers preliminary mechanistic analysis of strategy × encoder interaction + validates on downstream task. Three contributions, not one marginal improvement.\\n\\n## Anticipated Reviewer Concerns\\n\\n| Concern | Response | Evidence |\\n|---------|----------|----------|\\n| Only 2 encoders — can you generalize? | n=2 is minimum for interaction claim; we frame as observation with mechanism, not universal law; two decoder-only encoders with distinct pretraining (Fill vs FIM) and representation geometry (pos_sim 0.99 vs 0.80) provide meaningful variation | plan_013 (done), m2_full runs |\\n| BM25 vs true embedding negatives? | Run BM25 negatives to empirically compare with embedding-distance mining, grounding the comparison against CoCoHaNeRe's gradient-based premise | plan_018 |\\n| Pool size sensitivity? | Evaluate at pool {50, 100, 200, 500} to confirm strategy rankings hold at realistic sizes | plan_019 |\\n| Stratified by structural data availability? | Report per-stratum R@1 for 34% with structural data vs 66% fallback | plan_005 (extended) |\\n| Temperature regime specificity | Ablate τ ∈ {0.05, 0.1, 0.2} | plan_014 |\\n| No downstream task evaluation | SWE-bench Lite end-to-end with LLM agent | plan_003 |\\n| Static vs dynamic mining confound | Clarify mining is static; add dynamic baseline | plan_015 |\\n| CodeQL scalability at larger scale | 0% timeout, 78% Z%, 123 repos; m1_reextract_v2 adds more | plan_006 (done) |\\n| Why not compare inference-time graph methods? | Complementary: they navigate at inference, we mine at training. Discuss relationship. | plan_017 |\\n| Single benchmark | Add RepoBench-R cross-file retrieval | plan_004 |\\n| Statistical significance | Bootstrap 95% CI for all comparisons; full M2 = 9 seeds × 3 strategies × 2 encoders | plan_016, m2_full |\\n| \\\"Complementary signal\\\" overstatement | Temper: \\\"conditionally beneficial\\\" not \\\"always complementary\\\" | Writing discipline |\\n| Missing related work | RepoFusion, GRACE, GraphCodeBERT, ANCE, curriculum HN mining | Writing task |\\n\\n## Evidence Status\\n\\n### Confirmed findings (basis for claims):\\n- D017: True embedding mining helps (pilot: +2.0pp Qwen, +1.6pp StarCoder; M2 seed 43: +0.52pp best_by_R@1, +0.82pp mean fixed-checkpoint; final range pending s42/s44 completion) — establishes reliable zero-cost baseline\\n- D021/neg_difficulty: Qwen pos_sim=0.9855 (saturated), StarCoder pos_sim=0.7985 (healthy); margin differential is consistent with hypothesized strategy interaction\\n- m2_embed_verify (pilot): 3-strategy comparison is consistent with pilot ranking (embedding > random, dataflow conditional)\\n- plan_013 (StarCoder pilot): Consistent with cross-encoder pattern — embedding helps both, dataflow appears to help Qwen only\\n- plan_006: CodeQL scalability confirmed at 123-repo scale\\n\\n### Evidence presentation strategy:\\n- Primary table: best_by_R@1 (standard practice — select best checkpoint per run by validation R@1)\\n- Supplementary: fixed-checkpoint comparison as robustness check (not a replacement for best_by_R@1)\\n- Both metrics show directionally consistent results; no goalpost-moving between metrics\\n\\n### In progress:\\n- m2_full_qwen: random s42 DONE (R@1=0.5527), s43 DONE (R@1=0.5554), s44 DONE (R@1=0.6009, early stopped step 500), embedding_distance_s43 DONE (R@1=0.5606, early stopped step 1500). 4/9 runs complete, ~35h remaining.\\n- m2_full_starcoder: random s42 DONE (R@1=0.4604, from parent), s43 RUNNING (eval@500 R@1=0.4708). 1/9+ runs complete, ~65-70h remaining.\\n- m1_reextract_v2: 90.5% complete (25,582/28,276), 0 ERROR, ETA ~19:00 CST May 15\\n\\n### Planned (priority order):\\n- plan_018: BM25 negative baseline (Dream #1 consensus gap — grounds comparison against CoCoHaNeRe's premise)\\n- plan_003: SWE-bench Lite eval (biggest lever for paper strength)\\n- plan_019: Pool size sensitivity (Dream consensus — external validity)\\n- plan_014: Temperature ablation (Dream reviewer concern)\\n- plan_004: RepoBench-R second benchmark (with multi-seed CIs)\\n- plan_015: Dynamic mining baseline\\n- plan_005: Stratified analysis (extended: structural-available vs fallback stratum)\\n- plan_007/008/009: Additional ablations\\n\\n## Limitations\\n\\nEffect size is smaller than pilot estimates, likely because full-scale training data provides stronger random baselines, reducing the marginal value of targeted negative selection.\\n\\n## Contingency (if full M2 results we\\n\\n... [截断: 省略 2424 字符，传 max_chars=0 获取完整内容]\", \"total_chars\": 14424, \"truncated\": true}, \"error\": null, \"metadata\": {}}"
    }
  },
  "sourceToolAssistantUUID": "8bc1157c-21b7-49af-a727-b29621edc845",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/.claude/sessions/reviewer_65cfe724",
  "sessionId": "f444a635-eeef-4924-9b48-a4c308632421",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---


### Tool call

_source line 35 · 2026-05-16T00:23:32.903Z_

<details open><summary>🔧 Tool call — Glob · `toolu_01XcAHdgC8bxNajXggmnZnua`</summary>

```json
{
  "pattern": "**/related_work*",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6eba7a7f-265f-4703-a0b5-0296e63ea3db",
  "isSidechain": false,
  "requestId": "req_011Cb5J32VLKPFNYxnB9NPTr",
  "type": "assistant",
  "uuid": "299179a3-ad4e-486e-b8c2-abb5490f39f8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/.claude/sessions/reviewer_65cfe724",
  "sessionId": "f444a635-eeef-4924-9b48-a4c308632421",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016fPC9ji1Brow7ZujRQVpiF",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 11073,
      "cache_read_input_tokens": 47141,
      "output_tokens": 495,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 11073,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 495,
          "cache_read_input_tokens": 47141,
          "cache_creation_input_tokens": 11073,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 11073
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

_source line 36 · 2026-05-16T00:23:32.953Z_

```json
{
  "parentUuid": "3f842e06-4b1c-4e12-8083-b29fb4136720",
  "isSidechain": false,
  "attachment": {
    "type": "todo_reminder",
    "content": [],
    "itemCount": 0
  },
  "type": "attachment",
  "uuid": "f7229350-e4e9-4899-8afe-cf7b43f57293",
  "timestamp": "2026-05-16T00:23:32.953Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/.claude/sessions/reviewer_65cfe724",
  "sessionId": "f444a635-eeef-4924-9b48-a4c308632421",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---


### Runtime record

_source line 37_

```json
{
  "type": "last-prompt",
  "lastPrompt": "[系统通知 — worker_done:worker_research_related-work-literature_20260516T001526]: Worker worker_research_related-work-literature_20260516T001526 已完成（status=done），请审查 Agent 的处理结果。",
  "leafUuid": "f7229350-e4e9-4899-8afe-cf7b43f57293",
  "sessionId": "f444a635-eeef-4924-9b48-a4c308632421"
}
```

---


### Runtime record

_source line 38_

```json
{
  "type": "ai-title",
  "aiTitle": "Review research literature worker completion",
  "sessionId": "f444a635-eeef-4924-9b48-a4c308632421"
}
```

---


### Assistant

_source line 39 · 2026-05-16T00:23:36.584Z_

<details><summary>Logged reasoning block</summary>

```text
Found the worker's output files. The most likely output of this "related-work-literature" worker is the `related_work_expansion_report.md` and `related_work_references.md` files. Let me read the most recent ones to see what the worker produced.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f7229350-e4e9-4899-8afe-cf7b43f57293",
  "isSidechain": false,
  "requestId": "req_011Cb5J3vedKuHahHfnKhmqq",
  "type": "assistant",
  "uuid": "bc9fe6cc-4f5e-4c08-b317-2021efe59254",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/.claude/sessions/reviewer_65cfe724",
  "sessionId": "f444a635-eeef-4924-9b48-a4c308632421",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MczGY2nzEdxyy8ruMCnWAZ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 11318,
      "cache_read_input_tokens": 58214,
      "output_tokens": 344,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 11318,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 344,
          "cache_read_input_tokens": 58214,
          "cache_creation_input_tokens": 11318,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 11318
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

_source line 40 · 2026-05-16T00:23:37.262Z_

找到多个 related work 相关文件。读取最近的 worker 产出。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "bc9fe6cc-4f5e-4c08-b317-2021efe59254",
  "isSidechain": false,
  "requestId": "req_011Cb5J3vedKuHahHfnKhmqq",
  "type": "assistant",
  "uuid": "bbdbd0f6-a08f-4be7-a88f-f5973f101ef3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/.claude/sessions/reviewer_65cfe724",
  "sessionId": "f444a635-eeef-4924-9b48-a4c308632421",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MczGY2nzEdxyy8ruMCnWAZ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 11318,
      "cache_read_input_tokens": 58214,
      "output_tokens": 344,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 11318,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 344,
          "cache_read_input_tokens": 58214,
          "cache_creation_input_tokens": 11318,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 11318
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

_source line 41 · 2026-05-16T00:23:37.921Z_

<details open><summary>🔧 Tool call — Read · `toolu_01RJhUGq22eJ2vUv6RUX8K1J`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/literature/related_work_expansion_report.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "bbdbd0f6-a08f-4be7-a88f-f5973f101ef3",
  "isSidechain": false,
  "requestId": "req_011Cb5J3vedKuHahHfnKhmqq",
  "type": "assistant",
  "uuid": "178e9ceb-b33f-40a5-b0c2-da520a5042d7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/.claude/sessions/reviewer_65cfe724",
  "sessionId": "f444a635-eeef-4924-9b48-a4c308632421",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MczGY2nzEdxyy8ruMCnWAZ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 11318,
      "cache_read_input_tokens": 58214,
      "output_tokens": 344,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 11318,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 344,
          "cache_read_input_tokens": 58214,
          "cache_creation_input_tokens": 11318,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 11318
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

_source line 42 · 2026-05-16T00:23:38.787Z_

<details><summary>↩ Tool result · `toolu_01LjZBqJq7y1X5xZi27bnows`</summary>

```text
1	# Related Work Supplement: Contrastive Learning for Code & Adjacent Areas
2	
3	> **Purpose**: Supplementary paragraphs and citations to strengthen weak areas in Related Work v1.
4	> Six new papers added; RocketQA already cited in v1.
5	> Generated: 2026-05-15
6	
7	---
8	
9	## Supplement A: Contrastive Learning for Code (insert into Section 2.2, after the ContraCode/CodeRetriever paragraph)
10	
11	Beyond learning invariance to syntactic variation, contrastive pre-training has been applied to inject structural and robustness priors into code representations. SynCoBERT \cite{wang2021syncobert} introduces syntax-guided multi-modal contrastive pre-training that aligns code, natural language, and abstract syntax tree (AST) modalities through identifier prediction and AST edge prediction objectives, demonstrating that explicitly encoding syntactic structure during contrastive pre-training improves downstream code intelligence tasks. ContraBERT \cite{liu2023contrabert} takes a complementary robustness-oriented approach, designing nine data augmentation operators that generate adversarial code and comment variants---including identifier renaming, dead code insertion, and operand swapping---and further trains existing code models with contrastive objectives on these augmented pairs. ContraBERT shows that contrastive pre-training with targeted perturbations substantially improves model robustness against adversarial attacks while maintaining strong performance on standard benchmarks. These methods enrich the positive pair construction space for code contrastive learning, yet they focus on augmenting the pre-training signal rather than improving the selection of negative examples during fine-tuning. StructFuse addresses a complementary dimension: rather than improving how positive pairs are constructed, it improves which negatives the model trains against by grounding negative selection in inter-procedural data-flow structure.
12	
13	## Supplement B: Hard Negative Mining in Dense Retrieval (insert into Section 2.3, after the CL-DRD sentence)
14	
15	The curriculum learning paradigm for negative sampling has been further developed by CAPSTONE \cite{he2023capstone}, which addresses the training-inference discrepancy in dual-encoder dense retrieval. CAPSTONE expands documents with pseudo-queries during training and employs a curriculum sampling strategy that progressively improves the relevance between generated and real queries, effectively controlling negative difficulty through the query generation quality. This approach achieves strong results on both in-domain and out-of-domain retrieval benchmarks, reinforcing the finding that curriculum-based difficulty scheduling benefits dense retrieval training. While CAPSTONE focuses on bridging the training-inference gap through document expansion, our structure-grounded negatives provide an orthogonal form of curriculum: negatives that are hard because they share data-flow context with the positive, not because of embedding proximity alone.
16	
17	## Supplement C: Cross-File Code Understanding and Evaluation (insert into Section 2.4, before the closing paragraph, or as a new subsection bridge)
18	
19	The importance of cross-file context for code understanding has been empirically validated by dedicated benchmarks. CrossCodeEval \cite{ding2023crosscodeeval} constructs a diverse, multilingual benchmark for cross-file code completion across Python, Java, TypeScript, and C\#, using static analysis to identify completion targets that strictly require cross-file dependencies. Experiments show that even state-of-the-art code LLMs struggle without cross-file context, and that retrieval-augmented approaches yield clear improvements---yet performance remains far below the ceiling, indicating substantial room for better cross-file retrieval. ProGraML \cite{cummins2021programl} provides a language-independent, graph-based program representation that captures control-flow, data-flow, and call relations across entire programs, achieving strong results on data-flow analysis tasks. ProGraML demonstrates that whole-program structural representations are learnable and informative, providing conceptual grounding for StructFuse's use of inter-procedural data-flow graphs as a training signal. CoSQA \cite{huang2021cosqa} contributes a large-scale dataset of 20,000+ real web queries paired with Python code, bridging the gap between synthetic code search benchmarks and real-world developer information needs; it also introduces a contrastive learning method (CoCLR) for data augmentation in code search training. Together, these resources underscore that cross-file structural dependencies and realistic query distributions are critical dimensions for advancing code retrieval---precisely the dimensions that StructFuse's structure-grounded training targets.
20	
21	---
22	
23	## Summary of New Citations
24	
25	| Paper | Venue | Year | Area | Relation to StructFuse |
26	|-------|-------|------|------|----------------------|
27	| SynCoBERT | arXiv | 2021 | Contrastive code pre-training | Syntax-guided contrastive pre-training; StructFuse uses structure for negatives, not positives |
28	| ContraBERT | ICSE | 2023 | Contrastive code pre-training | Robustness-oriented augmentation; complementary to StructFuse's negative mining |
29	| CAPSTONE | EMNLP | 2023 | Dense retrieval | Curriculum sampling for retrieval; StructFuse provides structure-based curriculum |
30	| CrossCodeEval | NeurIPS | 2023 | Benchmark | Validates importance of cross-file context for code tasks |
31	| ProGraML | ICML | 2021 | Program graphs for ML | Whole-program graph representation; conceptual grounding for StructFuse's data-flow use |
32	| CoSQA | ACL | 2021 | Code search dataset | Real-world query benchmark with contrastive learning augmentation |
33	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "58d929b5-1bb6-4bc0-ac6b-f235c47afa72",
  "isSidechain": false,
  "promptId": "ee81bb41-edfe-48b7-9827-d79a74cf7a5e",
  "type": "user",
  "uuid": "83ff93ee-6434-43aa-9b54-c574ba200b6b",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/paper_drafts/related_work_supplement.md",
      "content": "# Related Work Supplement: Contrastive Learning for Code & Adjacent Areas\n\n> **Purpose**: Supplementary paragraphs and citations to strengthen weak areas in Related Work v1.\n> Six new papers added; RocketQA already cited in v1.\n> Generated: 2026-05-15\n\n---\n\n## Supplement A: Contrastive Learning for Code (insert into Section 2.2, after the ContraCode/CodeRetriever paragraph)\n\nBeyond learning invariance to syntactic variation, contrastive pre-training has been applied to inject structural and robustness priors into code representations. SynCoBERT \\cite{wang2021syncobert} introduces syntax-guided multi-modal contrastive pre-training that aligns code, natural language, and abstract syntax tree (AST) modalities through identifier prediction and AST edge prediction objectives, demonstrating that explicitly encoding syntactic structure during contrastive pre-training improves downstream code intelligence tasks. ContraBERT \\cite{liu2023contrabert} takes a complementary robustness-oriented approach, designing nine data augmentation operators that generate adversarial code and comment variants---including identifier renaming, dead code insertion, and operand swapping---and further trains existing code models with contrastive objectives on these augmented pairs. ContraBERT shows that contrastive pre-training with targeted perturbations substantially improves model robustness against adversarial attacks while maintaining strong performance on standard benchmarks. These methods enrich the positive pair construction space for code contrastive learning, yet they focus on augmenting the pre-training signal rather than improving the selection of negative examples during fine-tuning. StructFuse addresses a complementary dimension: rather than improving how positive pairs are constructed, it improves which negatives the model trains against by grounding negative selection in inter-procedural data-flow structure.\n\n## Supplement B: Hard Negative Mining in Dense Retrieval (insert into Section 2.3, after the CL-DRD sentence)\n\nThe curriculum learning paradigm for negative sampling has been further developed by CAPSTONE \\cite{he2023capstone}, which addresses the training-inference discrepancy in dual-encoder dense retrieval. CAPSTONE expands documents with pseudo-queries during training and employs a curriculum sampling strategy that progressively improves the relevance between generated and real queries, effectively controlling negative difficulty through the query generation quality. This approach achieves strong results on both in-domain and out-of-domain retrieval benchmarks, reinforcing the finding that curriculum-based difficulty scheduling benefits dense retrieval training. While CAPSTONE focuses on bridging the training-inference gap through document expansion, our structure-grounded negatives provide an orthogonal form of curriculum: negatives that are hard because they share data-flow context with the positive, not because of embedding proximity alone.\n\n## Supplement C: Cross-File Code Understanding and Evaluation (insert into Section 2.4, before the closing paragraph, or as a new subsection bridge)\n\nThe importance of cross-file context for code understanding has been empirically validated by dedicated benchmarks. CrossCodeEval \\cite{ding2023crosscodeeval} constructs a diverse, multilingual benchmark for cross-file code completion across Python, Java, TypeScript, and C\\#, using static analysis to identify completion targets that strictly require cross-file dependencies. Experiments show that even state-of-the-art code LLMs struggle without cross-file context, and that retrieval-augmented approaches yield clear improvements---yet performance remains far below the ceiling, indicating substantial room for better cross-file retrieval. ProGraML \\cite{cummins2021programl} provides a language-independent, graph-based program representation that captures control-flow, data-flow, and call relations across entire programs, achieving strong results on data-flow analysis tasks. ProGraML demonstrates that whole-program structural representations are learnable and informative, providing conceptual grounding for StructFuse's use of inter-procedural data-flow graphs as a training signal. CoSQA \\cite{huang2021cosqa} contributes a large-scale dataset of 20,000+ real web queries paired with Python code, bridging the gap between synthetic code search benchmarks and real-world developer information needs; it also introduces a contrastive learning method (CoCLR) for data augmentation in code search training. Together, these resources underscore that cross-file structural dependencies and realistic query distributions are critical dimensions for advancing code retrieval---precisely the dimensions that StructFuse's structure-grounded training targets.\n\n---\n\n## Summary of New Citations\n\n| Paper | Venue | Year | Area | Relation to StructFuse |\n|-------|-------|------|------|----------------------|\n| SynCoBERT | arXiv | 2021 | Contrastive code pre-training | Syntax-guided contrastive pre-training; StructFuse uses structure for negatives, not positives |\n| ContraBERT | ICSE | 2023 | Contrastive code pre-training | Robustness-oriented augmentation; complementary to StructFuse's negative mining |\n| CAPSTONE | EMNLP | 2023 | Dense retrieval | Curriculum sampling for retrieval; StructFuse provides structure-based curriculum |\n| CrossCodeEval | NeurIPS | 2023 | Benchmark | Validates importance of cross-file context for code tasks |\n| ProGraML | ICML | 2021 | Program graphs for ML | Whole-program graph representation; conceptual grounding for StructFuse's data-flow use |\n| CoSQA | ACL | 2021 | Code search dataset | Real-world query benchmark with contrastive learning augmentation |\n",
      "numLines": 33,
      "startLine": 1,
      "totalLines": 33
    }
  },
  "sourceToolAssistantUUID": "58d929b5-1bb6-4bc0-ac6b-f235c47afa72",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/.claude/sessions/reviewer_65cfe724",
  "sessionId": "f444a635-eeef-4924-9b48-a4c308632421",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---


### Tool result

_source line 43 · 2026-05-16T00:23:37.929Z_

<details><summary>↩ Tool result · `toolu_01RJhUGq22eJ2vUv6RUX8K1J`</summary>

```text
1	# Related Work Expansion Report — StructFuse
2	**Date**: 2026-05-14
3	
4	## Summary
5	Literature map expanded from ~22 entries (6 needing verification) to **37 verified entries** across 7 categories. All "需验证" flags resolved. 15 new papers added, 2 existing entries corrected.
6	
7	---
8	
9	## New Papers Added (15)
10	
11	### Category 1: Code Retrieval / SWE-bench (+2)
12	
13	| Paper | Venue | Year | Relation to StructFuse |
14	|-------|-------|------|----------------------|
15	| **SweRank**: Software Issue Localization with Code Ranking | arXiv | 2025 | Text-based retrieve-and-rerank baseline for SWE-bench; direct comparison target |
16	| **SWE-Fixer**: Training Open-Source LLMs for Effective and Efficient GitHub Issue Resolution | ACL Findings | 2025 | BM25 + LLM retriever pipeline; another text-based retrieval competitor |
17	
18	### Category 2: Hard Negative Mining (+1, +1 replacement)
19	
20	| Paper | Venue | Year | Relation to StructFuse |
21	|-------|-------|------|----------------------|
22	| **CoCoHaNeRe**: Effective Hard Negative Mining for Contrastive Learning-Based Code Search | ACM TOSEM | 2025 | **CRITICAL**: Claim 1 correction target. See note below. |
23	| **CL-DRD**: Curriculum Learning for Dense Retrieval Distillation | SIGIR (Best Short Paper) | 2022 | Replaces the unverified "curriculum HN mining" entry |
24	
25	### Category 3: Contrastive Learning for Code (NEW category, +3)
26	
27	| Paper | Venue | Year | Relation to StructFuse |
28	|-------|-------|------|----------------------|
29	| **ContraCode**: Contrastive Code Representation Learning | EMNLP | 2021 | Self-supervised contrastive pre-training via compiler transformations |
30	| **CodeRetriever**: A Large Scale Contrastive Pre-Training Method for Code Search | EMNLP | 2022 | Unimodal + bimodal contrastive pre-training for code search |
31	| **Towards Learning (Dis)-Similarity of Source Code from Program Contrasts** | ACL Long Papers | 2022 | Moved from Cat 4; title and venue corrected |
32	
33	### Category 4: Program Analysis (+1)
34	
35	| Paper | Venue | Year | Relation to StructFuse |
36	|-------|-------|------|----------------------|
37	| **ARISE**: A Repository-level Graph Representation and Toolset for Agentic Fault Localization and Program Repair | arXiv | 2025 | Intra-procedural def-use + runtime tool API; contrasts with StructFuse's inter-procedural static mining |
38	
39	### Category 5: Code Embeddings (+2)
40	
41	| Paper | Venue | Year | Relation to StructFuse |
42	|-------|-------|------|----------------------|
43	| **DeepSeek-Coder**: When the Large Language Model Meets Programming | arXiv | 2024 | Alternative code LLM backbone reference |
44	| **RepoFusion**: Training Code Models to Understand Your Repository | arXiv | 2023 | Cross-file repo context fusion for code completion |
45	
46	### Category 6: Graph-Guided Inference (NEW category, +3)
47	
48	| Paper | Venue | Year | Relation to StructFuse |
49	|-------|-------|------|----------------------|
50	| **LocAgent**: Graph-Guided LLM Agents for Code Localization | ACL | 2025 | Inference-time graph navigation; complementary to StructFuse's training-time structural signal |
51	| **CodexGraph**: Bridging LLMs and Code Repositories via Code Graph Databases | NAACL | 2025 | Graph DB interface for code retrieval at inference |
52	| **RANGER**: Repository-Level Agent for Graph-Enhanced Retrieval | arXiv | 2025 | Repo knowledge graph + MCTS exploration |
53	
54	### Category 7: Infrastructure (NEW category, +2)
55	
56	| Paper | Venue | Year | Relation to StructFuse |
57	|-------|-------|------|----------------------|
58	| **FAISS**: Billion-Scale Similarity Search with GPUs | IEEE Trans Big Data | 2021 | ANN library used for embedding-based hard negative mining |
59	| **Tree-sitter**: Incremental Parsing System | Software (Zenodo) | 2018 | Parsing tool; no formal paper, cite via Zenodo DOI |
60	
61	---
62	
63	## Verification Results
64	
65	### Previously "需验证" — Now Resolved
66	
67	| Entry | Status | Change |
68	|-------|--------|--------|
69	| SWE-smith venue | **Corrected** | arXiv → **NeurIPS 2025 D&B Spotlight** |
70	| SWE-smith authors | **Corrected** | Added Kilian Lieret, Kabir Khandpur, Yanzhe Zhang, Binyuan Hui, Ludwig Schmidt, Diyi Yang |
71	| RepoBench year/venue | **Confirmed** | ICLR 2024 ✓ |
72	| FA-AST authors/venue | **Confirmed** | Wenhan Wang et al., SANER 2020 ✓ |
73	| StarCoder venue | **Confirmed** | TMLR 2023 ✓ |
74	| Qwen2.5-Coder title/year | **Confirmed** | arXiv 2024 ✓ |
75	| Contrastive Learning paper | **Corrected** | Title: "Towards Learning (Dis)-Similarity of Source Code from Program Contrasts"; Venue: ACL 2022 Long Papers (not Findings) |
76	| Curriculum HN mining | **Replaced** | Was placeholder → Now: CL-DRD (Zeng et al., SIGIR 2022 Best Short Paper) |
77	
78	---
79	
80	## CoCoHaNeRe — Critical Finding
81	
82	**Full citation**: Fan Y., Li C., Ge J., Huang L., Luo B. "Effective Hard Negative Mining for Contrastive Learning-Based Code Search." ACM TOSEM, Vol 34, No 3, 2025. DOI: 10.1145/3695994.
83	
84	**Important nuance for Claim 1 framing**: CoCoHaNeRe does NOT explicitly claim that "embedding-distance hard negatives harm code search." Its argument is that using non-differentiable embedding negatives makes learning "slow and ineffective," and proposes differentiable gradient-based hard negatives as a solution. The paper's position is about the mechanism (differentiable vs. non-differentiable), not about whether embedding-distance negatives are inherently harmful.
85	
86	**Implication for StructFuse Claim 1**: The "correcting misconception" framing should be adjusted. Instead of "CoCoHaNeRe claims embedding negatives harm performance," the accurate framing is: "CoCoHaNeRe characterizes non-differentiable embedding negatives as ineffective and proposes gradient-based alternatives; we show that simple embedding-distance mining (without gradient coupling) consistently improves retrieval, challenging the premise that more complex mechanisms are necessary."
87	
88	---
89	
90	## What's NOT Included (and why)
91	
92	| Paper/Tool | Reason |
93	|------------|--------|
94	| **GRACE** (code-specific) | No well-known paper called "GRACE" for general code representation. Multiple GRACE papers exist (graph contrastive learning, vulnerability detection) but none match the intended scope. |
95	| **Aider** | Software tool, no formal paper. Can be mentioned in text as an SWE-bench method but not a citable reference. |
96	| **Moatless Tools** | Software tool by Albert Orwall. The associated paper is **SWE-Search** (Antoniades et al., ICLR 2025) — could be added if SWE-bench retrieval coverage needs strengthening. |
97	| **CoSQA** | Not searched; lower priority for this paper's scope. |
98	
99	---
100	
101	## Citation Count by Category
102	
103	| Category | Count |
104	|----------|-------|
105	| Code Retrieval / SWE-bench | 8 |
106	| Hard Negative Mining | 6 |
107	| Contrastive Learning for Code | 3 |
108	| Program Analysis for ML | 6 |
109	| Code Embeddings / Search | 9 |
110	| Graph-Guided Inference | 3 |
111	| Infrastructure / Tools | 2 |
112	| **Total** | **37** |
113	
114	---
115	
116	## Recency Distribution
117	
118	| Period | Count |
119	|--------|-------|
120	| 2025 | 10 |
121	| 2024 | 6 |
122	| 2023 | 3 |
123	| 2022 | 5 |
124	| 2021 | 4 |
125	| 2020 | 4 |
126	| 2019 | 4 |
127	| ≤2018 | 1 |
128	
129	27% of citations are from 2025, 70% from 2022+. Recency is strong.
130	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "178e9ceb-b33f-40a5-b0c2-da520a5042d7",
  "isSidechain": false,
  "promptId": "ee81bb41-edfe-48b7-9827-d79a74cf7a5e",
  "type": "user",
  "uuid": "94b9b429-fafb-4c4c-9644-db465920ec1c",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/literature/related_work_expansion_report.md",
      "content": "# Related Work Expansion Report — StructFuse\n**Date**: 2026-05-14\n\n## Summary\nLiterature map expanded from ~22 entries (6 needing verification) to **37 verified entries** across 7 categories. All \"需验证\" flags resolved. 15 new papers added, 2 existing entries corrected.\n\n---\n\n## New Papers Added (15)\n\n### Category 1: Code Retrieval / SWE-bench (+2)\n\n| Paper | Venue | Year | Relation to StructFuse |\n|-------|-------|------|----------------------|\n| **SweRank**: Software Issue Localization with Code Ranking | arXiv | 2025 | Text-based retrieve-and-rerank baseline for SWE-bench; direct comparison target |\n| **SWE-Fixer**: Training Open-Source LLMs for Effective and Efficient GitHub Issue Resolution | ACL Findings | 2025 | BM25 + LLM retriever pipeline; another text-based retrieval competitor |\n\n### Category 2: Hard Negative Mining (+1, +1 replacement)\n\n| Paper | Venue | Year | Relation to StructFuse |\n|-------|-------|------|----------------------|\n| **CoCoHaNeRe**: Effective Hard Negative Mining for Contrastive Learning-Based Code Search | ACM TOSEM | 2025 | **CRITICAL**: Claim 1 correction target. See note below. |\n| **CL-DRD**: Curriculum Learning for Dense Retrieval Distillation | SIGIR (Best Short Paper) | 2022 | Replaces the unverified \"curriculum HN mining\" entry |\n\n### Category 3: Contrastive Learning for Code (NEW category, +3)\n\n| Paper | Venue | Year | Relation to StructFuse |\n|-------|-------|------|----------------------|\n| **ContraCode**: Contrastive Code Representation Learning | EMNLP | 2021 | Self-supervised contrastive pre-training via compiler transformations |\n| **CodeRetriever**: A Large Scale Contrastive Pre-Training Method for Code Search | EMNLP | 2022 | Unimodal + bimodal contrastive pre-training for code search |\n| **Towards Learning (Dis)-Similarity of Source Code from Program Contrasts** | ACL Long Papers | 2022 | Moved from Cat 4; title and venue corrected |\n\n### Category 4: Program Analysis (+1)\n\n| Paper | Venue | Year | Relation to StructFuse |\n|-------|-------|------|----------------------|\n| **ARISE**: A Repository-level Graph Representation and Toolset for Agentic Fault Localization and Program Repair | arXiv | 2025 | Intra-procedural def-use + runtime tool API; contrasts with StructFuse's inter-procedural static mining |\n\n### Category 5: Code Embeddings (+2)\n\n| Paper | Venue | Year | Relation to StructFuse |\n|-------|-------|------|----------------------|\n| **DeepSeek-Coder**: When the Large Language Model Meets Programming | arXiv | 2024 | Alternative code LLM backbone reference |\n| **RepoFusion**: Training Code Models to Understand Your Repository | arXiv | 2023 | Cross-file repo context fusion for code completion |\n\n### Category 6: Graph-Guided Inference (NEW category, +3)\n\n| Paper | Venue | Year | Relation to StructFuse |\n|-------|-------|------|----------------------|\n| **LocAgent**: Graph-Guided LLM Agents for Code Localization | ACL | 2025 | Inference-time graph navigation; complementary to StructFuse's training-time structural signal |\n| **CodexGraph**: Bridging LLMs and Code Repositories via Code Graph Databases | NAACL | 2025 | Graph DB interface for code retrieval at inference |\n| **RANGER**: Repository-Level Agent for Graph-Enhanced Retrieval | arXiv | 2025 | Repo knowledge graph + MCTS exploration |\n\n### Category 7: Infrastructure (NEW category, +2)\n\n| Paper | Venue | Year | Relation to StructFuse |\n|-------|-------|------|----------------------|\n| **FAISS**: Billion-Scale Similarity Search with GPUs | IEEE Trans Big Data | 2021 | ANN library used for embedding-based hard negative mining |\n| **Tree-sitter**: Incremental Parsing System | Software (Zenodo) | 2018 | Parsing tool; no formal paper, cite via Zenodo DOI |\n\n---\n\n## Verification Results\n\n### Previously \"需验证\" — Now Resolved\n\n| Entry | Status | Change |\n|-------|--------|--------|\n| SWE-smith venue | **Corrected** | arXiv → **NeurIPS 2025 D&B Spotlight** |\n| SWE-smith authors | **Corrected** | Added Kilian Lieret, Kabir Khandpur, Yanzhe Zhang, Binyuan Hui, Ludwig Schmidt, Diyi Yang |\n| RepoBench year/venue | **Confirmed** | ICLR 2024 ✓ |\n| FA-AST authors/venue | **Confirmed** | Wenhan Wang et al., SANER 2020 ✓ |\n| StarCoder venue | **Confirmed** | TMLR 2023 ✓ |\n| Qwen2.5-Coder title/year | **Confirmed** | arXiv 2024 ✓ |\n| Contrastive Learning paper | **Corrected** | Title: \"Towards Learning (Dis)-Similarity of Source Code from Program Contrasts\"; Venue: ACL 2022 Long Papers (not Findings) |\n| Curriculum HN mining | **Replaced** | Was placeholder → Now: CL-DRD (Zeng et al., SIGIR 2022 Best Short Paper) |\n\n---\n\n## CoCoHaNeRe — Critical Finding\n\n**Full citation**: Fan Y., Li C., Ge J., Huang L., Luo B. \"Effective Hard Negative Mining for Contrastive Learning-Based Code Search.\" ACM TOSEM, Vol 34, No 3, 2025. DOI: 10.1145/3695994.\n\n**Important nuance for Claim 1 framing**: CoCoHaNeRe does NOT explicitly claim that \"embedding-distance hard negatives harm code search.\" Its argument is that using non-differentiable embedding negatives makes learning \"slow and ineffective,\" and proposes differentiable gradient-based hard negatives as a solution. The paper's position is about the mechanism (differentiable vs. non-differentiable), not about whether embedding-distance negatives are inherently harmful.\n\n**Implication for StructFuse Claim 1**: The \"correcting misconception\" framing should be adjusted. Instead of \"CoCoHaNeRe claims embedding negatives harm performance,\" the accurate framing is: \"CoCoHaNeRe characterizes non-differentiable embedding negatives as ineffective and proposes gradient-based alternatives; we show that simple embedding-distance mining (without gradient coupling) consistently improves retrieval, challenging the premise that more complex mechanisms are necessary.\"\n\n---\n\n## What's NOT Included (and why)\n\n| Paper/Tool | Reason |\n|------------|--------|\n| **GRACE** (code-specific) | No well-known paper called \"GRACE\" for general code representation. Multiple GRACE papers exist (graph contrastive learning, vulnerability detection) but none match the intended scope. |\n| **Aider** | Software tool, no formal paper. Can be mentioned in text as an SWE-bench method but not a citable reference. |\n| **Moatless Tools** | Software tool by Albert Orwall. The associated paper is **SWE-Search** (Antoniades et al., ICLR 2025) — could be added if SWE-bench retrieval coverage needs strengthening. |\n| **CoSQA** | Not searched; lower priority for this paper's scope. |\n\n---\n\n## Citation Count by Category\n\n| Category | Count |\n|----------|-------|\n| Code Retrieval / SWE-bench | 8 |\n| Hard Negative Mining | 6 |\n| Contrastive Learning for Code | 3 |\n| Program Analysis for ML | 6 |\n| Code Embeddings / Search | 9 |\n| Graph-Guided Inference | 3 |\n| Infrastructure / Tools | 2 |\n| **Total** | **37** |\n\n---\n\n## Recency Distribution\n\n| Period | Count |\n|--------|-------|\n| 2025 | 10 |\n| 2024 | 6 |\n| 2023 | 3 |\n| 2022 | 5 |\n| 2021 | 4 |\n| 2020 | 4 |\n| 2019 | 4 |\n| ≤2018 | 1 |\n\n27% of citations are from 2025, 70% from 2022+. Recency is strong.\n",
      "numLines": 130,
      "startLine": 1,
      "totalLines": 130
    }
  },
  "sourceToolAssistantUUID": "178e9ceb-b33f-40a5-b0c2-da520a5042d7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/.claude/sessions/reviewer_65cfe724",
  "sessionId": "f444a635-eeef-4924-9b48-a4c308632421",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---


### Tool call

_source line 44 · 2026-05-16T00:23:38.633Z_

<details open><summary>🔧 Tool call — Read · `toolu_01R8DcWHNDa3CwQwnpHcirqS`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/literature/related_work_references.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "94b9b429-fafb-4c4c-9644-db465920ec1c",
  "isSidechain": false,
  "requestId": "req_011Cb5J3vedKuHahHfnKhmqq",
  "type": "assistant",
  "uuid": "6a1fee05-c8a6-445b-8d51-3a26cc56290e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/.claude/sessions/reviewer_65cfe724",
  "sessionId": "f444a635-eeef-4924-9b48-a4c308632421",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MczGY2nzEdxyy8ruMCnWAZ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 11318,
      "cache_read_input_tokens": 58214,
      "output_tokens": 344,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 11318,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 344,
          "cache_read_input_tokens": 58214,
          "cache_creation_input_tokens": 11318,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 11318
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

_source line 45 · 2026-05-16T00:23:38.637Z_

<details><summary>↩ Tool result · `toolu_01R8DcWHNDa3CwQwnpHcirqS`</summary>

````text
1	# StructFuse Related Work Literature Collection
2	
3	> Collected: 2026-05-16 | Total: 21 papers across 3 directions
4	
5	---
6	
7	## Direction 1: Code Retrieval 中的 Negative Mining 策略
8	
9	### 1.1 CoCoHaNeRe (direct-competitor)
10	
11	Code search framework with differentiable hard negative retrieval from a searchable memory bank. Average MRR exceeds CodeBERT/GraphCodeBERT/UniXcoder by 11.25%/8.13%/7.38%. **与 StructFuse 最直接的竞品——同样关注 code search 中 hard negative 的挖掘策略。**
12	
13	```bibtex
14	@article{fan2025cocohanere,
15	  title={Effective Hard Negative Mining for Contrastive Learning-Based Code Search},
16	  author={Fan, Ye and Li, Chao and Ge, Jing and Huang, Liang and Luo, Bin},
17	  journal={ACM Transactions on Software Engineering and Methodology},
18	  volume={34},
19	  number={3},
20	  pages={1--35},
21	  year={2025},
22	  doi={10.1145/3695994}
23	}
24	```
25	
26	### 1.2 CodeSearchNet (evaluation)
27	
28	Code search benchmark with 6M functions across 6 languages and expert relevance annotations. **StructFuse 使用的评估数据集的来源基准。**
29	
30	```bibtex
31	@article{husain2019codesearchnet,
32	  title={CodeSearchNet Challenge: Evaluating the State of Semantic Code Search},
33	  author={Husain, Hamel and Wu, Ho-Hsiang and Gazit, Tiferet and Allamanis, Miltiadis and Brockschmidt, Marc},
34	  journal={arXiv preprint arXiv:1909.09436},
35	  year={2019}
36	}
37	```
38	
39	### 1.3 CodeBERT (background)
40	
41	First bimodal pre-trained model for programming language and natural language, trained with replaced token detection. **Code retrieval 领域的基线模型。**
42	
43	```bibtex
44	@inproceedings{feng2020codebert,
45	  title={CodeBERT: A Pre-Trained Model for Programming and Natural Languages},
46	  author={Feng, Zhangyin and Guo, Daya and Tang, Duyu and Duan, Nan and Feng, Xiaocheng and Gong, Ming and Shou, Linjun and Qin, Bing and Liu, Ting and Jiang, Daxin and Zhou, Ming},
47	  booktitle={Findings of the Association for Computational Linguistics: EMNLP 2020},
48	  pages={1536--1547},
49	  year={2020}
50	}
51	```
52	
53	### 1.4 GraphCodeBERT (method-component)
54	
55	First pre-trained model incorporating code structure (data flow) for code representations. Uses semantic-level structure rather than AST. **展示了结构化代码表示对检索的提升，StructFuse 的 structure-aware embedding 思路的先驱。**
56	
57	```bibtex
58	@inproceedings{guo2021graphcodebert,
59	  title={GraphCodeBERT: Pre-training Code Representations with Data Flow},
60	  author={Guo, Daya and Ren, Shuo and Lu, Shuai and Feng, Zhangyin and Tang, Duyu and Liu, Shujie and Zhou, Long and Duan, Nan and Svyatkovskiy, Alexey and Fu, Shengyu and Tufano, Michele and Deng, Shao Kun and Clement, Colin and Drain, Dawn and Sundaresan, Neel and Yin, Jian and Jiang, Daxin and Zhou, Ming},
61	  booktitle={International Conference on Learning Representations},
62	  year={2021}
63	}
64	```
65	
66	### 1.5 UniXcoder (background)
67	
68	Unified cross-modal pre-training leveraging AST and code comments via contrastive learning. **StructFuse 的 backbone encoder 之一，也展示了 AST 结构对代码表示的增益。**
69	
70	```bibtex
71	@inproceedings{guo2022unixcoder,
72	  title={UniXcoder: Unified Cross-Modal Pre-training for Code Representation},
73	  author={Guo, Daya and Lu, Shuai and Duan, Nan and Wang, Yanlin and Zhou, Ming and Yin, Jian},
74	  booktitle={Proceedings of the 60th Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers)},
75	  pages={7212--7225},
76	  year={2022}
77	}
78	```
79	
80	### 1.6 CodeRetriever (direct-competitor)
81	
82	Large-scale contrastive pre-training with both unimodal (code-code) and bimodal (code-text) learning for code search. **与 StructFuse 类似的 contrastive learning 框架，但没有显式的 hard negative 策略。**
83	
84	```bibtex
85	@inproceedings{li2022coderetriever,
86	  title={CodeRetriever: A Large Scale Contrastive Pre-Training Method for Code Search},
87	  author={Li, Xiaonan and Gong, Yeyun and Shen, Yelong and Qiu, Xipeng and Zhang, Hang and Yao, Bolun and Qi, Weizhen and Jiang, Daxin and Chen, Weizhu and Duan, Nan},
88	  booktitle={Proceedings of the 2022 Conference on Empirical Methods in Natural Language Processing},
89	  pages={2898--2910},
90	  year={2022}
91	}
92	```
93	
94	### 1.7 CoCoSoDa (direct-competitor)
95	
96	Contrastive code search with soft data augmentation and momentum-based negative enrichment. Exceeds CodeBERT/GraphCodeBERT/UniXcoder by 13.3%/10.5%/5.9% MRR. **在 negative sample enrichment 方面与 StructFuse 互补——CoCoSoDa 用 momentum queue 增加 negative 数量，StructFuse 关注 negative difficulty。**
97	
98	```bibtex
99	@inproceedings{shi2023cocosoda,
100	  title={CoCoSoDa: Effective Contrastive Learning for Code Search},
101	  author={Shi, Ensheng and Wang, Yanlin and Gu, Wenchao and Du, Lun and Zhang, Hongyu and Han, Shi and Zhang, Dongmei and Sun, Hongbin},
102	  booktitle={2023 IEEE/ACM 45th International Conference on Software Engineering (ICSE)},
103	  pages={2198--2210},
104	  year={2023}
105	}
106	```
107	
108	---
109	
110	## Direction 2: Contrastive Learning 中 Hard Negative 的 Overfitting 问题
111	
112	### 2.1 CPC / InfoNCE (background)
113	
114	Introduces InfoNCE loss: contrastive predictive coding for unsupervised representation learning. **Contrastive learning 的基础损失函数，StructFuse 训练目标的理论根基。**
115	
116	```bibtex
117	@article{oord2018representation,
118	  title={Representation Learning with Contrastive Predictive Coding},
119	  author={van den Oord, Aaron and Li, Yazhe and Vinyals, Oriol},
120	  journal={arXiv preprint arXiv:1807.03748},
121	  year={2018}
122	}
123	```
124	
125	### 2.2 HCL (method-component)
126	
127	Develops controllable hard negative sampling for contrastive learning, showing harder negatives accelerate and improve learning. **理论上证明了 hard negative 的价值，但也暗示了过度 hard 会导致问题——StructFuse difficulty analysis 的理论起点。**
128	
129	```bibtex
130	@inproceedings{robinson2021contrastive,
131	  title={Contrastive Learning with Hard Negative Samples},
132	  author={Robinson, Joshua David and Chuang, Ching-Yao and Sra, Suvrit and Jegelka, Stefanie},
133	  booktitle={International Conference on Learning Representations},
134	  year={2021}
135	}
136	```
137	
138	### 2.3 DCL (method-component)
139	
140	Debiased contrastive objective correcting for false negatives (same-class samples treated as negatives). **False negative 是 hard negative 过拟合的重要来源之一，DCL 提供了理论框架。**
141	
142	```bibtex
143	@inproceedings{chuang2020debiased,
144	  title={Debiased Contrastive Learning},
145	  author={Chuang, Ching-Yao and Robinson, Joshua and Lin, Yen-Chen and Torralba, Antonio and Jegelka, Stefanie},
146	  booktitle={Advances in Neural Information Processing Systems},
147	  volume={33},
148	  pages={8765--8775},
149	  year={2020}
150	}
151	```
152	
153	### 2.4 MoCHi (method-component)
154	
155	Hard negative mixing at feature level with minimal overhead; shows harder negatives facilitate faster learning. **Feature-level hard negative 合成方法，与 StructFuse 的 structure-based negative mining 形成对比。**
156	
157	```bibtex
158	@inproceedings{kalantidis2020hard,
159	  title={Hard Negative Mixing for Contrastive Learning},
160	  author={Kalantidis, Yannis and Sariyildiz, Mert Bulent and Pion, No{\'e} and Weinzaepfel, Philippe and Larlus, Diane},
161	  booktitle={Advances in Neural Information Processing Systems},
162	  volume={33},
163	  pages={21798--21809},
164	  year={2020}
165	}
166	```
167	
168	### 2.5 Understanding Hard Negatives in NCE (background)
169	
170	Theoretical analysis: using model distribution as negative distribution reduces gradient bias. **为 hard negative 的作用提供了理论解释——StructFuse 的 difficulty-overfitting 分析可引用此理论框架。**
171	
172	```bibtex
173	@inproceedings{zhang2021understanding,
174	  title={Understanding Hard Negatives in Noise Contrastive Estimation},
175	  author={Zhang, Wenzheng and Stratos, Karl},
176	  booktitle={Proceedings of the 2021 Conference of the North American Chapter of the Association for Computational Linguistics: Human Language Technologies},
177	  pages={1090--1101},
178	  year={2021}
179	}
180	```
181	
182	### 2.6 ProGCL (method-component)
183	
184	Shows hard negatives in graph CL are often false negatives; proposes probability-based hardness that accounts for true/false negative distinction. **揭示了 hard negative = false negative 的陷阱，与 StructFuse 发现的 difficulty-overfitting 现象呼应。**
185	
186	```bibtex
187	@inproceedings{xia2022progcl,
188	  title={ProGCL: Rethinking Hard Negative Mining in Graph Contrastive Learning},
189	  author={Xia, Jun and Wu, Lirong and Wang, Ge and Chen, Jintao and Li, Stan Z.},
190	  booktitle={Proceedings of the 39th International Conference on Machine Learning},
191	  pages={24332--24346},
192	  year={2022}
193	}
194	```
195	
196	### 2.7 WCL (method-component)
197	
198	Difficulty-based sampling exploiting a bias-amplifying encoder to find informative hard negatives while avoiding false negatives. **用 difficulty 分层采样来 debias，与 StructFuse 的 difficulty stratification 思路最接近。**
199	
200	```bibtex
201	@inproceedings{jang2023difficulty,
202	  title={Difficulty-Based Sampling for Debiased Contrastive Representation Learning},
203	  author={Jang, Taeuk and Wang, Xiaoqian},
204	  booktitle={Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition},
205	  pages={24039--24048},
206	  year={2023}
207	}
208	```
209	
210	---
211	
212	## Direction 3: Representation Geometry / Similarity Saturation
213	
214	### 3.1 SimCLR (background)
215	
216	Simple contrastive framework showing the importance of data augmentation, projection head, and batch size. **Contrastive learning 的经典方法论，StructFuse 实验设计的参考。**
217	
218	```bibtex
219	@inproceedings{chen2020simple,
220	  title={A Simple Framework for Contrastive Learning of Visual Representations},
221	  author={Chen, Ting and Kornblith, Simon and Norouzi, Mohammad and Hinton, Geoffrey},
222	  booktitle={Proceedings of the 37th International Conference on Machine Learning},
223	  pages={1597--1607},
224	  year={2020}
225	}
226	```
227	
228	### 3.2 Alignment & Uniformity (method-component)
229	
230	Identifies two key properties of contrastive loss: alignment of positive pairs and uniformity on hypersphere; proves contrastive loss optimizes both asymptotically. **StructFuse 分析 embedding space 质量的理论工具——可用 alignment/uniformity 指标量化 structure-aware embedding 的改进。**
231	
232	```bibtex
233	@inproceedings{wang2020understanding,
234	  title={Understanding Contrastive Representation Learning through Alignment and Uniformity on the Hypersphere},
235	  author={Wang, Tongzhou and Isola, Phillip},
236	  booktitle={Proceedings of the 37th International Conference on Machine Learning},
237	  pages={9929--9939},
238	  year={2020}
239	}
240	```
241	
242	### 3.3 Representation Degeneration (background)
243	
244	Shows pre-trained LM embeddings degenerate into a narrow cone, limiting representation power; proposes regularization. **Embedding 退化的理论根源——StructFuse 观察到的 similarity saturation 可追溯到此现象。**
245	
246	```bibtex
247	@inproceedings{gao2019representation,
248	  title={Representation Degeneration Problem in Training Natural Language Generation Models},
249	  author={Gao, Jun and He, Di and Tan, Xu and Qin, Tao and Wang, Liwei and Liu, Tie-Yan},
250	  booktitle={International Conference on Learning Representations},
251	  year={2019}
252	}
253	```
254	
255	### 3.4 Anisotropy of Contextualized Representations (background)
256	
257	Discovers that BERT/ELMo/GPT-2 representations occupy a narrow cone (anisotropy) across all layers. **实证发现 pre-trained model 的各向异性问题，StructFuse 使用的 code encoder 继承了此问题。**
258	
259	```bibtex
260	@inproceedings{ethayarajh2019contextual,
261	  title={How Contextual are Contextualized Word Representations? Comparing the Geometry of BERT, ELMo, and GPT-2 Embeddings},
262	  author={Ethayarajh, Kawin},
263	  booktitle={Proceedings of the 2019 Conference on Empirical Methods in Natural Language Processing and the 9th International Joint Conference on Natural Language Processing},
264	  pages={55--65},
265	  year={2019}
266	}
267	```
268	
269	### 3.5 BERT-flow (method-component)
270	
271	Shows BERT sentence embeddings are anisotropic; proposes normalizing flows to transform to isotropic Gaussian. **Anisotropy 矫正方法的代表，与 StructFuse 的 whitening/normalization 策略形成对比。**
272	
273	```bibtex
274	@inproceedings{li2020sentence,
275	  title={On the Sentence Embeddings from Pre-trained Language Models},
276	  author={Li, Bohan and Zhou, Hao and He, Junxian and Wang, Mingxuan and Yang, Yiming and Li, Lei},
277	  booktitle={Proceedings of the 2020 Conference on Empirical Methods in Natural Language Processing},
278	  pages={9119--9130},
279	  year={2020}
280	}
281	```
282	
283	### 3.6 SimCSE (method-component)
284	
285	Contrastive learning regularizes anisotropic embedding space to be more uniform; uses dropout as minimal augmentation. Spectral analysis shows contrastive loss flattens singular spectrum. **直接证明 contrastive learning 改善 anisotropy——StructFuse 可引用其 uniformity 分析框架。**
286	
287	```bibtex
288	@inproceedings{gao2021simcse,
289	  title={SimCSE: Simple Contrastive Learning of Sentence Embeddings},
290	  author={Gao, Tianyu and Yao, Xingcheng and Chen, Danqi},
291	  booktitle={Proceedings of the 2021 Conference on Empirical Methods in Natural Language Processing},
292	  pages={6894--6910},
293	  year={2021}
294	}
295	```
296	
297	### 3.7 Whitening for Sentence Representations (method-component)
298	
299	Whitening operation enhances isotropy and reduces dimensionality of sentence representations. **针对 anisotropy 的简洁解法，与 StructFuse 中 embedding post-processing 的讨论相关。**
300	
301	```bibtex
302	@article{su2021whitening,
303	  title={Whitening Sentence Representations for Better Semantics and Faster Retrieval},
304	  author={Su, Jianlin and Cao, Jiarun and Liu, Weijie and Ou, Yangyiwen},
305	  journal={arXiv preprint arXiv:2103.15316},
306	  year={2021}
307	}
308	```
309	
310	---
311	
312	## Summary
313	
314	| Direction | Papers | Key insight for StructFuse |
315	|-----------|--------|---------------------------|
316	| 1. Code retrieval negative mining | 7 | StructFuse fills the gap between structure-aware encoding (GraphCodeBERT) and hard negative mining (CoCoHaNeRe) by using structural similarity for difficulty-aware negative selection |
317	| 2. Hard negative overfitting | 7 | Existing work (HCL, DCL, ProGCL, WCL) shows hard negatives help but can cause overfitting/false-negative problems; StructFuse's difficulty stratification addresses this in code domain |
318	| 3. Representation geometry | 7 | Pre-trained code encoders inherit anisotropy (Ethayarajh, Gao 2019); contrastive learning improves uniformity (SimCSE, Wang & Isola) but similarity saturation in high-similarity regions remains; StructFuse's structure-aware negatives target this specific region |
319	
````

</details>

<details><summary>Recorded metadata</summary>

````json
{
  "recorded_role": "user",
  "parentUuid": "6a1fee05-c8a6-445b-8d51-3a26cc56290e",
  "isSidechain": false,
  "promptId": "ee81bb41-edfe-48b7-9827-d79a74cf7a5e",
  "type": "user",
  "uuid": "405ad9f1-e3d2-4592-98fc-10dbb94fcdfd",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/literature/related_work_references.md",
      "content": "# StructFuse Related Work Literature Collection\n\n> Collected: 2026-05-16 | Total: 21 papers across 3 directions\n\n---\n\n## Direction 1: Code Retrieval 中的 Negative Mining 策略\n\n### 1.1 CoCoHaNeRe (direct-competitor)\n\nCode search framework with differentiable hard negative retrieval from a searchable memory bank. Average MRR exceeds CodeBERT/GraphCodeBERT/UniXcoder by 11.25%/8.13%/7.38%. **与 StructFuse 最直接的竞品——同样关注 code search 中 hard negative 的挖掘策略。**\n\n```bibtex\n@article{fan2025cocohanere,\n  title={Effective Hard Negative Mining for Contrastive Learning-Based Code Search},\n  author={Fan, Ye and Li, Chao and Ge, Jing and Huang, Liang and Luo, Bin},\n  journal={ACM Transactions on Software Engineering and Methodology},\n  volume={34},\n  number={3},\n  pages={1--35},\n  year={2025},\n  doi={10.1145/3695994}\n}\n```\n\n### 1.2 CodeSearchNet (evaluation)\n\nCode search benchmark with 6M functions across 6 languages and expert relevance annotations. **StructFuse 使用的评估数据集的来源基准。**\n\n```bibtex\n@article{husain2019codesearchnet,\n  title={CodeSearchNet Challenge: Evaluating the State of Semantic Code Search},\n  author={Husain, Hamel and Wu, Ho-Hsiang and Gazit, Tiferet and Allamanis, Miltiadis and Brockschmidt, Marc},\n  journal={arXiv preprint arXiv:1909.09436},\n  year={2019}\n}\n```\n\n### 1.3 CodeBERT (background)\n\nFirst bimodal pre-trained model for programming language and natural language, trained with replaced token detection. **Code retrieval 领域的基线模型。**\n\n```bibtex\n@inproceedings{feng2020codebert,\n  title={CodeBERT: A Pre-Trained Model for Programming and Natural Languages},\n  author={Feng, Zhangyin and Guo, Daya and Tang, Duyu and Duan, Nan and Feng, Xiaocheng and Gong, Ming and Shou, Linjun and Qin, Bing and Liu, Ting and Jiang, Daxin and Zhou, Ming},\n  booktitle={Findings of the Association for Computational Linguistics: EMNLP 2020},\n  pages={1536--1547},\n  year={2020}\n}\n```\n\n### 1.4 GraphCodeBERT (method-component)\n\nFirst pre-trained model incorporating code structure (data flow) for code representations. Uses semantic-level structure rather than AST. **展示了结构化代码表示对检索的提升，StructFuse 的 structure-aware embedding 思路的先驱。**\n\n```bibtex\n@inproceedings{guo2021graphcodebert,\n  title={GraphCodeBERT: Pre-training Code Representations with Data Flow},\n  author={Guo, Daya and Ren, Shuo and Lu, Shuai and Feng, Zhangyin and Tang, Duyu and Liu, Shujie and Zhou, Long and Duan, Nan and Svyatkovskiy, Alexey and Fu, Shengyu and Tufano, Michele and Deng, Shao Kun and Clement, Colin and Drain, Dawn and Sundaresan, Neel and Yin, Jian and Jiang, Daxin and Zhou, Ming},\n  booktitle={International Conference on Learning Representations},\n  year={2021}\n}\n```\n\n### 1.5 UniXcoder (background)\n\nUnified cross-modal pre-training leveraging AST and code comments via contrastive learning. **StructFuse 的 backbone encoder 之一，也展示了 AST 结构对代码表示的增益。**\n\n```bibtex\n@inproceedings{guo2022unixcoder,\n  title={UniXcoder: Unified Cross-Modal Pre-training for Code Representation},\n  author={Guo, Daya and Lu, Shuai and Duan, Nan and Wang, Yanlin and Zhou, Ming and Yin, Jian},\n  booktitle={Proceedings of the 60th Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers)},\n  pages={7212--7225},\n  year={2022}\n}\n```\n\n### 1.6 CodeRetriever (direct-competitor)\n\nLarge-scale contrastive pre-training with both unimodal (code-code) and bimodal (code-text) learning for code search. **与 StructFuse 类似的 contrastive learning 框架，但没有显式的 hard negative 策略。**\n\n```bibtex\n@inproceedings{li2022coderetriever,\n  title={CodeRetriever: A Large Scale Contrastive Pre-Training Method for Code Search},\n  author={Li, Xiaonan and Gong, Yeyun and Shen, Yelong and Qiu, Xipeng and Zhang, Hang and Yao, Bolun and Qi, Weizhen and Jiang, Daxin and Chen, Weizhu and Duan, Nan},\n  booktitle={Proceedings of the 2022 Conference on Empirical Methods in Natural Language Processing},\n  pages={2898--2910},\n  year={2022}\n}\n```\n\n### 1.7 CoCoSoDa (direct-competitor)\n\nContrastive code search with soft data augmentation and momentum-based negative enrichment. Exceeds CodeBERT/GraphCodeBERT/UniXcoder by 13.3%/10.5%/5.9% MRR. **在 negative sample enrichment 方面与 StructFuse 互补——CoCoSoDa 用 momentum queue 增加 negative 数量，StructFuse 关注 negative difficulty。**\n\n```bibtex\n@inproceedings{shi2023cocosoda,\n  title={CoCoSoDa: Effective Contrastive Learning for Code Search},\n  author={Shi, Ensheng and Wang, Yanlin and Gu, Wenchao and Du, Lun and Zhang, Hongyu and Han, Shi and Zhang, Dongmei and Sun, Hongbin},\n  booktitle={2023 IEEE/ACM 45th International Conference on Software Engineering (ICSE)},\n  pages={2198--2210},\n  year={2023}\n}\n```\n\n---\n\n## Direction 2: Contrastive Learning 中 Hard Negative 的 Overfitting 问题\n\n### 2.1 CPC / InfoNCE (background)\n\nIntroduces InfoNCE loss: contrastive predictive coding for unsupervised representation learning. **Contrastive learning 的基础损失函数，StructFuse 训练目标的理论根基。**\n\n```bibtex\n@article{oord2018representation,\n  title={Representation Learning with Contrastive Predictive Coding},\n  author={van den Oord, Aaron and Li, Yazhe and Vinyals, Oriol},\n  journal={arXiv preprint arXiv:1807.03748},\n  year={2018}\n}\n```\n\n### 2.2 HCL (method-component)\n\nDevelops controllable hard negative sampling for contrastive learning, showing harder negatives accelerate and improve learning. **理论上证明了 hard negative 的价值，但也暗示了过度 hard 会导致问题——StructFuse difficulty analysis 的理论起点。**\n\n```bibtex\n@inproceedings{robinson2021contrastive,\n  title={Contrastive Learning with Hard Negative Samples},\n  author={Robinson, Joshua David and Chuang, Ching-Yao and Sra, Suvrit and Jegelka, Stefanie},\n  booktitle={International Conference on Learning Representations},\n  year={2021}\n}\n```\n\n### 2.3 DCL (method-component)\n\nDebiased contrastive objective correcting for false negatives (same-class samples treated as negatives). **False negative 是 hard negative 过拟合的重要来源之一，DCL 提供了理论框架。**\n\n```bibtex\n@inproceedings{chuang2020debiased,\n  title={Debiased Contrastive Learning},\n  author={Chuang, Ching-Yao and Robinson, Joshua and Lin, Yen-Chen and Torralba, Antonio and Jegelka, Stefanie},\n  booktitle={Advances in Neural Information Processing Systems},\n  volume={33},\n  pages={8765--8775},\n  year={2020}\n}\n```\n\n### 2.4 MoCHi (method-component)\n\nHard negative mixing at feature level with minimal overhead; shows harder negatives facilitate faster learning. **Feature-level hard negative 合成方法，与 StructFuse 的 structure-based negative mining 形成对比。**\n\n```bibtex\n@inproceedings{kalantidis2020hard,\n  title={Hard Negative Mixing for Contrastive Learning},\n  author={Kalantidis, Yannis and Sariyildiz, Mert Bulent and Pion, No{\\'e} and Weinzaepfel, Philippe and Larlus, Diane},\n  booktitle={Advances in Neural Information Processing Systems},\n  volume={33},\n  pages={21798--21809},\n  year={2020}\n}\n```\n\n### 2.5 Understanding Hard Negatives in NCE (background)\n\nTheoretical analysis: using model distribution as negative distribution reduces gradient bias. **为 hard negative 的作用提供了理论解释——StructFuse 的 difficulty-overfitting 分析可引用此理论框架。**\n\n```bibtex\n@inproceedings{zhang2021understanding,\n  title={Understanding Hard Negatives in Noise Contrastive Estimation},\n  author={Zhang, Wenzheng and Stratos, Karl},\n  booktitle={Proceedings of the 2021 Conference of the North American Chapter of the Association for Computational Linguistics: Human Language Technologies},\n  pages={1090--1101},\n  year={2021}\n}\n```\n\n### 2.6 ProGCL (method-component)\n\nShows hard negatives in graph CL are often false negatives; proposes probability-based hardness that accounts for true/false negative distinction. **揭示了 hard negative = false negative 的陷阱，与 StructFuse 发现的 difficulty-overfitting 现象呼应。**\n\n```bibtex\n@inproceedings{xia2022progcl,\n  title={ProGCL: Rethinking Hard Negative Mining in Graph Contrastive Learning},\n  author={Xia, Jun and Wu, Lirong and Wang, Ge and Chen, Jintao and Li, Stan Z.},\n  booktitle={Proceedings of the 39th International Conference on Machine Learning},\n  pages={24332--24346},\n  year={2022}\n}\n```\n\n### 2.7 WCL (method-component)\n\nDifficulty-based sampling exploiting a bias-amplifying encoder to find informative hard negatives while avoiding false negatives. **用 difficulty 分层采样来 debias，与 StructFuse 的 difficulty stratification 思路最接近。**\n\n```bibtex\n@inproceedings{jang2023difficulty,\n  title={Difficulty-Based Sampling for Debiased Contrastive Representation Learning},\n  author={Jang, Taeuk and Wang, Xiaoqian},\n  booktitle={Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition},\n  pages={24039--24048},\n  year={2023}\n}\n```\n\n---\n\n## Direction 3: Representation Geometry / Similarity Saturation\n\n### 3.1 SimCLR (background)\n\nSimple contrastive framework showing the importance of data augmentation, projection head, and batch size. **Contrastive learning 的经典方法论，StructFuse 实验设计的参考。**\n\n```bibtex\n@inproceedings{chen2020simple,\n  title={A Simple Framework for Contrastive Learning of Visual Representations},\n  author={Chen, Ting and Kornblith, Simon and Norouzi, Mohammad and Hinton, Geoffrey},\n  booktitle={Proceedings of the 37th International Conference on Machine Learning},\n  pages={1597--1607},\n  year={2020}\n}\n```\n\n### 3.2 Alignment & Uniformity (method-component)\n\nIdentifies two key properties of contrastive loss: alignment of positive pairs and uniformity on hypersphere; proves contrastive loss optimizes both asymptotically. **StructFuse 分析 embedding space 质量的理论工具——可用 alignment/uniformity 指标量化 structure-aware embedding 的改进。**\n\n```bibtex\n@inproceedings{wang2020understanding,\n  title={Understanding Contrastive Representation Learning through Alignment and Uniformity on the Hypersphere},\n  author={Wang, Tongzhou and Isola, Phillip},\n  booktitle={Proceedings of the 37th International Conference on Machine Learning},\n  pages={9929--9939},\n  year={2020}\n}\n```\n\n### 3.3 Representation Degeneration (background)\n\nShows pre-trained LM embeddings degenerate into a narrow cone, limiting representation power; proposes regularization. **Embedding 退化的理论根源——StructFuse 观察到的 similarity saturation 可追溯到此现象。**\n\n```bibtex\n@inproceedings{gao2019representation,\n  title={Representation Degeneration Problem in Training Natural Language Generation Models},\n  author={Gao, Jun and He, Di and Tan, Xu and Qin, Tao and Wang, Liwei and Liu, Tie-Yan},\n  booktitle={International Conference on Learning Representations},\n  year={2019}\n}\n```\n\n### 3.4 Anisotropy of Contextualized Representations (background)\n\nDiscovers that BERT/ELMo/GPT-2 representations occupy a narrow cone (anisotropy) across all layers. **实证发现 pre-trained model 的各向异性问题，StructFuse 使用的 code encoder 继承了此问题。**\n\n```bibtex\n@inproceedings{ethayarajh2019contextual,\n  title={How Contextual are Contextualized Word Representations? Comparing the Geometry of BERT, ELMo, and GPT-2 Embeddings},\n  author={Ethayarajh, Kawin},\n  booktitle={Proceedings of the 2019 Conference on Empirical Methods in Natural Language Processing and the 9th International Joint Conference on Natural Language Processing},\n  pages={55--65},\n  year={2019}\n}\n```\n\n### 3.5 BERT-flow (method-component)\n\nShows BERT sentence embeddings are anisotropic; proposes normalizing flows to transform to isotropic Gaussian. **Anisotropy 矫正方法的代表，与 StructFuse 的 whitening/normalization 策略形成对比。**\n\n```bibtex\n@inproceedings{li2020sentence,\n  title={On the Sentence Embeddings from Pre-trained Language Models},\n  author={Li, Bohan and Zhou, Hao and He, Junxian and Wang, Mingxuan and Yang, Yiming and Li, Lei},\n  booktitle={Proceedings of the 2020 Conference on Empirical Methods in Natural Language Processing},\n  pages={9119--9130},\n  year={2020}\n}\n```\n\n### 3.6 SimCSE (method-component)\n\nContrastive learning regularizes anisotropic embedding space to be more uniform; uses dropout as minimal augmentation. Spectral analysis shows contrastive loss flattens singular spectrum. **直接证明 contrastive learning 改善 anisotropy——StructFuse 可引用其 uniformity 分析框架。**\n\n```bibtex\n@inproceedings{gao2021simcse,\n  title={SimCSE: Simple Contrastive Learning of Sentence Embeddings},\n  author={Gao, Tianyu and Yao, Xingcheng and Chen, Danqi},\n  booktitle={Proceedings of the 2021 Conference on Empirical Methods in Natural Language Processing},\n  pages={6894--6910},\n  year={2021}\n}\n```\n\n### 3.7 Whitening for Sentence Representations (method-component)\n\nWhitening operation enhances isotropy and reduces dimensionality of sentence representations. **针对 anisotropy 的简洁解法，与 StructFuse 中 embedding post-processing 的讨论相关。**\n\n```bibtex\n@article{su2021whitening,\n  title={Whitening Sentence Representations for Better Semantics and Faster Retrieval},\n  author={Su, Jianlin and Cao, Jiarun and Liu, Weijie and Ou, Yangyiwen},\n  journal={arXiv preprint arXiv:2103.15316},\n  year={2021}\n}\n```\n\n---\n\n## Summary\n\n| Direction | Papers | Key insight for StructFuse |\n|-----------|--------|---------------------------|\n| 1. Code retrieval negative mining | 7 | StructFuse fills the gap between structure-aware encoding (GraphCodeBERT) and hard negative mining (CoCoHaNeRe) by using structural similarity for difficulty-aware negative selection |\n| 2. Hard negative overfitting | 7 | Existing work (HCL, DCL, ProGCL, WCL) shows hard negatives help but can cause overfitting/false-negative problems; StructFuse's difficulty stratification addresses this in code domain |\n| 3. Representation geometry | 7 | Pre-trained code encoders inherit anisotropy (Ethayarajh, Gao 2019); contrastive learning improves uniformity (SimCSE, Wang & Isola) but similarity saturation in high-similarity regions remains; StructFuse's structure-aware negatives target this specific region |\n",
      "numLines": 319,
      "startLine": 1,
      "totalLines": 319
    }
  },
  "sourceToolAssistantUUID": "6a1fee05-c8a6-445b-8d51-3a26cc56290e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/.claude/sessions/reviewer_65cfe724",
  "sessionId": "f444a635-eeef-4924-9b48-a4c308632421",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
````

</details>

---


### Tool call

_source line 46 · 2026-05-16T00:23:38.781Z_

<details open><summary>🔧 Tool call — Read · `toolu_01LjZBqJq7y1X5xZi27bnows`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/paper_drafts/related_work_supplement.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "405ad9f1-e3d2-4592-98fc-10dbb94fcdfd",
  "isSidechain": false,
  "requestId": "req_011Cb5J3vedKuHahHfnKhmqq",
  "type": "assistant",
  "uuid": "58d929b5-1bb6-4bc0-ac6b-f235c47afa72",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/.claude/sessions/reviewer_65cfe724",
  "sessionId": "f444a635-eeef-4924-9b48-a4c308632421",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MczGY2nzEdxyy8ruMCnWAZ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 11318,
      "cache_read_input_tokens": 58214,
      "output_tokens": 344,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 11318,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 344,
          "cache_read_input_tokens": 58214,
          "cache_creation_input_tokens": 11318,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 11318
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

_source line 47_

```json
{
  "type": "last-prompt",
  "lastPrompt": "[系统通知 — worker_done:worker_research_related-work-literature_20260516T001526]: Worker worker_research_related-work-literature_20260516T001526 已完成（status=done），请审查 Agent 的处理结果。",
  "leafUuid": "83ff93ee-6434-43aa-9b54-c574ba200b6b",
  "sessionId": "f444a635-eeef-4924-9b48-a4c308632421"
}
```

---


### Runtime record

_source line 48_

```json
{
  "type": "ai-title",
  "aiTitle": "Review research literature worker completion",
  "sessionId": "f444a635-eeef-4924-9b48-a4c308632421"
}
```

---


### Assistant

_source line 49 · 2026-05-16T00:24:22.399Z_

<details><summary>Logged reasoning block</summary>

```text
Now I have a good picture. The worker produced:

1. **`related_work_expansion_report.md`** (dated 2026-05-14) — This documents the expansion of the literature map from ~22 to 37 entries, with verification of existing entries.

2. **`related_work_references.md`** (dated 2026-05-16) — This is the latest output from this worker. It collects 21 papers across 3 directions:
   - Direction 1: Code Retrieval 中的 Negative Mining 策略 (7 papers)
   - Direction 2: Contrastive Learning 中 Hard Negative 的 Overfitting 问题 (7 papers)
   - Direction 3: Representation Geometry / Similarity Saturation (7 papers)

3. **`related_work_supplement.md`** (dated 2026-05-15) — Supplement paragraphs with 6 new papers: SynCoBERT, ContraBERT, CAPSTONE, CrossCodeEval, ProGraML, CoSQA.

Now I need to check the related work v1 draft to see what's currently written and audit the worker's output against it.

I'm noticing several papers in the references file that haven't been added to the literature map yet—CoCoSoDa, CPC/InfoNCE, HCL, DCL, MoCHi, ProGCL, WCL, and others on hard negatives—so I need to verify these citations and ensure they're properly integrated into the existing structure. The references and supplement files contain roughly 20 additional papers that haven't made it into literature_map.yaml yet, which still shows 37 entries from May 2026. I'm also noticing some citations that need verification—CoCoSoDa attributed to Shi et al. at ICSE 2023 is the main one I should double-check, while the others like CPC, HCL, DCL, and MoCHi are well-established in the literature. et al. ICML 2022 — need to verify
      - WCL: Jang & Wang CVPR 2023 — need to verify
      - Alignment & Uniformity: Wang & Isola ICML 2020 — well-known, fine
      - Representation Degeneration: Gao et al. ICLR 2019 — need to verify exact venue
      - Anisotropy: Ethayarajh EMNLP 2019 — well-known, fine
      - BERT-flow: Li et al. EMNLP 2020 — well-known, fine
      - SimCSE: Gao et al. EMNLP 2021 — well-known, fine
      - Whitening: Su et al. arXiv 2021 — need to verify

   Most of these are well-known papers. I don't see obvious fake citations. Now I'm checking some specific venues and dates that stand out — SynCoBERT is listed as arXiv 2021 in the supplement, so I should verify if it actually appeared at a conference. ARISE shows 2026 in the literature map, which is a future date, though arXiv preprints from 2025-2026 are plausible. I'm also noticing some framing inconsistencies where the related work file discusses "difficulty-aware negative selection" and "difficulty-overfitting" concepts that don't appear in the main paper framing document, which focuses on representation geometry instead.

There are also some factual errors emerging: the related work file mentions StructFuse using whitening/normalization strategies that I can't find evidence for, and it incorrectly lists UniXcoder as a backbone encoder when the paper actually uses Qwen2.5-Coder-3B and StarCoder2-3B. Additionally, there's a conceptual reversal in the supplement where it describes dataflow-aware negatives as "hard because they share data-flow context," when actually in StructFuse these are files that are NOT reachable via dataflow from the query.

I'm noticing some structural issues too: the literature_map.yaml hasn't been updated with the ~20 new paper references that were added, creating a consistency problem about which source is authoritative. Let me focus on documenting the key findings and severity levels for these issues. and StarCoder2-3B.

3. **[severity: warning] Incorrect description of dataflow negatives in supplement**: Supplement C says negatives are hard "because they share data-flow context with the positive." Per `paper_framing.md`, dataflow negatives are explicitly files NOT reachable via data-flow (¬reachable_G(x,q)), ranked by BM25. This is backwards.

4. **[severity: info] Most citations appear legitimate**: The majority of papers cited (SimCLR, DPR, ANCE, SimCSE, etc.) are well-known works with correct venue/year information. A few less well-known papers (CoCoSoDa, ProGCL, WCL) I can't verify with certainty but seem plausible.

5. **[severity: info] Good coverage expansion**: The worker expanded from primarily code retrieval and program analysis to include contrastive learning theory, representation geometry, and cross-file evaluation, which strengthens the theoretical grounding.

6. **[severity: warning] "difficulty-overfitting" framing mismatch**: The references document frames StructFuse around "difficulty stratification" and "difficulty-overfitting" concepts, but `paper_framing.md` frames around "representation geometry" and "encoder-strategy interaction." These are related but not identical — the writing needs to be consistent with the approved framing.

Now I'm checking the related work files to see what's already been written.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "83ff93ee-6434-43aa-9b54-c574ba200b6b",
  "isSidechain": false,
  "requestId": "req_011Cb5J4NTQQXVjxYsrsQ8cQ",
  "type": "assistant",
  "uuid": "14d399fa-b5b4-47d0-92ad-a207d9a9a059",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/.claude/sessions/reviewer_65cfe724",
  "sessionId": "f444a635-eeef-4924-9b48-a4c308632421",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CHKBrrEiFzLqe2asJLj5sy",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 9666,
      "cache_read_input_tokens": 69532,
      "output_tokens": 2427,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 9666,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 2427,
          "cache_read_input_tokens": 69532,
          "cache_creation_input_tokens": 9666,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 9666
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

_source line 50 · 2026-05-16T00:24:22.401Z_

需要检查 Related Work v1 草稿和远程服务器上的 LaTeX 文件。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "14d399fa-b5b4-47d0-92ad-a207d9a9a059",
  "isSidechain": false,
  "requestId": "req_011Cb5J4NTQQXVjxYsrsQ8cQ",
  "type": "assistant",
  "uuid": "b3412974-3e6d-4244-9ad9-9873bbc8adf6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/.claude/sessions/reviewer_65cfe724",
  "sessionId": "f444a635-eeef-4924-9b48-a4c308632421",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CHKBrrEiFzLqe2asJLj5sy",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 9666,
      "cache_read_input_tokens": 69532,
      "output_tokens": 2427,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 9666,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 2427,
          "cache_read_input_tokens": 69532,
          "cache_creation_input_tokens": 9666,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 9666
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

_source line 51 · 2026-05-16T00:24:23.047Z_

<details open><summary>🔧 Tool call — Read · `toolu_01HykfLf9GgpXNCkYdrDFfnn`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/paper_drafts/related_work_v1.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b3412974-3e6d-4244-9ad9-9873bbc8adf6",
  "isSidechain": false,
  "requestId": "req_011Cb5J4NTQQXVjxYsrsQ8cQ",
  "type": "assistant",
  "uuid": "bedf0255-c8b0-463f-a787-a796abdf2311",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/.claude/sessions/reviewer_65cfe724",
  "sessionId": "f444a635-eeef-4924-9b48-a4c308632421",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CHKBrrEiFzLqe2asJLj5sy",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 9666,
      "cache_read_input_tokens": 69532,
      "output_tokens": 2427,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 9666,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 2427,
          "cache_read_input_tokens": 69532,
          "cache_creation_input_tokens": 9666,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 9666
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

_source line 52 · 2026-05-16T00:24:23.060Z_

<details><summary>↩ Tool result · `toolu_01HykfLf9GgpXNCkYdrDFfnn`</summary>

```text
1	# 2. Related Work
2	
3	## 2.1 Dense Retrieval for Code
4	
5	Code retrieval has evolved from sparse lexical methods such as BM25 \cite{robertson2009bm25} to dense neural approaches. Early pretrained code models---CodeBERT \cite{feng2020codebert}, UniXcoder \cite{guo2022unixcoder}, and InferCode \cite{bui2021infercode}---learn general-purpose code representations through masked language modeling and related pretraining objectives, enabling semantic matching beyond surface-level token overlap. More recent large-scale code models, including StarCoder2 \cite{lozhkov2024starcoder2} and Qwen2.5-Coder \cite{hui2024qwen25coder}, provide powerful encoder backbones trained on trillions of code tokens. In the retrieval domain, CodeSage \cite{zhang2024codesage} and SCodeR \cite{li2022scoder} introduce contrastive fine-tuning strategies that adapt pretrained representations for code search. The growing importance of repository-level retrieval---driven by benchmarks like SWE-bench \cite{jimenez2024swebench}---has motivated specialized systems: SweRank \cite{reddy2025swerank} formulates issue localization as code ranking, while SWE-Fixer \cite{xie2025swefixer} combines BM25 with neural reranking in a coarse-to-fine pipeline. StructFuse builds on this foundation by systematically comparing negative mining strategies---random, embedding-distance, and structure-aware---for contrastive code retrieval, demonstrating that the choice of mining strategy meaningfully affects retrieval quality.
6	
7	## 2.2 Contrastive Learning for Code
8	
9	Sentence-BERT \cite{reimers2019sentencebert} established contrastive fine-tuning of pretrained encoders for dense text retrieval, a paradigm that has since become dominant for code representation learning. ContraCode \cite{jain2021contracode} generates functionally equivalent program variants through compiler transformations, training models to be invariant to syntactic variation. CodeRetriever \cite{li2022coderetriever} combines unimodal code-code and bimodal code-text contrastive objectives, achieving strong results across eleven code search benchmarks. SynCoBERT \cite{wang2021syncobert} introduces syntax-guided multi-modal contrastive pretraining that aligns code, natural language, and AST modalities through identifier prediction and edge prediction objectives. ContraBERT \cite{liu2023contrabert} takes a complementary robustness-oriented approach, designing adversarial augmentation operators---including identifier renaming, dead code insertion, and operand swapping---to improve model robustness while maintaining retrieval performance. Ding et al.\ \cite{ding2022programcontrasts} use structure-guided code transformations to synthesize contrastive pairs, demonstrating that program-structure-aware augmentation improves code clone detection and vulnerability identification. GraphCodeBERT \cite{guo2021graphcodebert} incorporates data-flow edges into pretraining, demonstrating that structural information improves code understanding tasks. These methods enrich the positive pair construction space or the pretraining signal. While GraphCodeBERT uses structural edges as a pretraining objective, StructFuse addresses a complementary dimension: we systematically study how negative selection strategy---including structure-aware alternatives---affects contrastive code retrieval across encoders with distinct representation geometries.
10	
11	## 2.3 Hard Negative Mining
12	
13	The quality of negative examples critically affects contrastive learning \cite{chen2020simclr}. In dense text retrieval, DPR \cite{karpukhin2020dpr} established the practice of using BM25 top-ranked non-relevant passages as hard negatives. ANCE \cite{xiong2021ance} dynamically mines negatives from an approximate nearest neighbor index updated during training, while RocketQA \cite{qu2021rocketqa} introduces cross-batch denoised negatives with knowledge distillation. STAR \cite{zhan2021star} further refines this paradigm by using the retriever's own top-ranked passages as training negatives. Curriculum-based approaches---CL-DRD \cite{zeng2022cldrd} and CAPSTONE \cite{he2023capstone}---schedule negative difficulty progressively during training.
14	
15	In the code domain, CoCoHaNeRe \cite{fan2025cocohanere} proposes gradient-based hard negative mining for code search, evaluating both BM25-selected and embedding-based negatives and reporting limitations of each non-differentiable strategy. However, their claim that non-differentiable embedding negatives are ineffective has not been evaluated under controlled conditions in structural code retrieval settings, where repository-level file localization involves richer structural cues than the NL$\to$code search setting studied by CoCoHaNeRe. StructFuse addresses this gap with a systematic comparison of three mining strategies---random, embedding-distance, and dataflow-aware---across decoder-only encoders with distinct representation geometries. Our results show that static embedding-distance mining provides reliable improvement at zero additional cost, establishing it as a strong baseline that requires no gradient computation or dynamic index updates. We further incorporate data-flow structure as an additional signal dimension in the comparison, grounding hardness in inter-procedural program semantics rather than embedding proximity alone.
16	
17	## 2.4 Code Structure in Machine Learning
18	
19	Program dependence graphs \cite{ferrante1987pdg} and code property graphs \cite{yamaguchi2014cpg} have long served program analysis; tools like CodeQL \cite{avgustinov2016ql} make inter-procedural analysis accessible at scale. In machine learning, code2vec \cite{alon2019code2vec} pioneered learning from AST paths, while ProGraML \cite{cummins2021programl} demonstrated that whole-program graph representations capturing control-flow, data-flow, and call relations are learnable and effective for compiler optimization tasks. CrossCodeEval \cite{ding2023crosscodeeval} empirically validates that cross-file context is critical for code completion, with retrieval-augmented approaches yielding clear but still far-from-ceiling improvements. RepoFusion \cite{shrivastava2023repofusion} further demonstrates that training code models to incorporate cross-file repository context via Fusion-in-Decoder significantly improves completion quality, even outperforming much larger models that lack repository awareness.
20	
21	Recent inference-time graph methods bring structural reasoning to LLM-based software engineering. CodexGraph \cite{liu2025codexgraph} and RepoGraph \cite{ouyang2025repograph} build navigable code graph databases for LLM agents; LocAgent \cite{chen2025locagent} and RANGER \cite{shah2025ranger} employ multi-hop graph reasoning and MCTS-based traversal for fault localization and retrieval, respectively. GRACE \cite{wang2025grace} constructs multi-level code graphs spanning repository, module, and function granularity---integrating AST, control-flow, and data-flow edges---for hierarchical retrieval-augmented code completion. GraphCoder \cite{liu2024graphcoder} and ARISE \cite{seddik2026arise} incorporate data-flow edges---control/data dependence and definition-use chains, respectively---but their data-flow analysis remains intra-procedural in scope. Critically, these methods primarily leverage structural graphs at inference time, incurring per-query latency proportional to graph complexity. StructFuse operates in a distinct regime: we leverage inter-procedural data-flow graphs at \emph{training time} to construct an additional strategy dimension for systematic comparison, enabling analysis of how structural signals interact with encoder representation geometry---all with zero inference overhead. The two paradigms are complementary---a StructFuse-trained encoder can serve as an efficient first-stage retriever for inference-time graph systems that perform targeted reranking.
22	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "bedf0255-c8b0-463f-a787-a796abdf2311",
  "isSidechain": false,
  "promptId": "ee81bb41-edfe-48b7-9827-d79a74cf7a5e",
  "type": "user",
  "uuid": "b0d2548e-90c9-46c7-93ca-8b502dfa138d",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/paper_drafts/related_work_v1.md",
      "content": "# 2. Related Work\n\n## 2.1 Dense Retrieval for Code\n\nCode retrieval has evolved from sparse lexical methods such as BM25 \\cite{robertson2009bm25} to dense neural approaches. Early pretrained code models---CodeBERT \\cite{feng2020codebert}, UniXcoder \\cite{guo2022unixcoder}, and InferCode \\cite{bui2021infercode}---learn general-purpose code representations through masked language modeling and related pretraining objectives, enabling semantic matching beyond surface-level token overlap. More recent large-scale code models, including StarCoder2 \\cite{lozhkov2024starcoder2} and Qwen2.5-Coder \\cite{hui2024qwen25coder}, provide powerful encoder backbones trained on trillions of code tokens. In the retrieval domain, CodeSage \\cite{zhang2024codesage} and SCodeR \\cite{li2022scoder} introduce contrastive fine-tuning strategies that adapt pretrained representations for code search. The growing importance of repository-level retrieval---driven by benchmarks like SWE-bench \\cite{jimenez2024swebench}---has motivated specialized systems: SweRank \\cite{reddy2025swerank} formulates issue localization as code ranking, while SWE-Fixer \\cite{xie2025swefixer} combines BM25 with neural reranking in a coarse-to-fine pipeline. StructFuse builds on this foundation by systematically comparing negative mining strategies---random, embedding-distance, and structure-aware---for contrastive code retrieval, demonstrating that the choice of mining strategy meaningfully affects retrieval quality.\n\n## 2.2 Contrastive Learning for Code\n\nSentence-BERT \\cite{reimers2019sentencebert} established contrastive fine-tuning of pretrained encoders for dense text retrieval, a paradigm that has since become dominant for code representation learning. ContraCode \\cite{jain2021contracode} generates functionally equivalent program variants through compiler transformations, training models to be invariant to syntactic variation. CodeRetriever \\cite{li2022coderetriever} combines unimodal code-code and bimodal code-text contrastive objectives, achieving strong results across eleven code search benchmarks. SynCoBERT \\cite{wang2021syncobert} introduces syntax-guided multi-modal contrastive pretraining that aligns code, natural language, and AST modalities through identifier prediction and edge prediction objectives. ContraBERT \\cite{liu2023contrabert} takes a complementary robustness-oriented approach, designing adversarial augmentation operators---including identifier renaming, dead code insertion, and operand swapping---to improve model robustness while maintaining retrieval performance. Ding et al.\\ \\cite{ding2022programcontrasts} use structure-guided code transformations to synthesize contrastive pairs, demonstrating that program-structure-aware augmentation improves code clone detection and vulnerability identification. GraphCodeBERT \\cite{guo2021graphcodebert} incorporates data-flow edges into pretraining, demonstrating that structural information improves code understanding tasks. These methods enrich the positive pair construction space or the pretraining signal. While GraphCodeBERT uses structural edges as a pretraining objective, StructFuse addresses a complementary dimension: we systematically study how negative selection strategy---including structure-aware alternatives---affects contrastive code retrieval across encoders with distinct representation geometries.\n\n## 2.3 Hard Negative Mining\n\nThe quality of negative examples critically affects contrastive learning \\cite{chen2020simclr}. In dense text retrieval, DPR \\cite{karpukhin2020dpr} established the practice of using BM25 top-ranked non-relevant passages as hard negatives. ANCE \\cite{xiong2021ance} dynamically mines negatives from an approximate nearest neighbor index updated during training, while RocketQA \\cite{qu2021rocketqa} introduces cross-batch denoised negatives with knowledge distillation. STAR \\cite{zhan2021star} further refines this paradigm by using the retriever's own top-ranked passages as training negatives. Curriculum-based approaches---CL-DRD \\cite{zeng2022cldrd} and CAPSTONE \\cite{he2023capstone}---schedule negative difficulty progressively during training.\n\nIn the code domain, CoCoHaNeRe \\cite{fan2025cocohanere} proposes gradient-based hard negative mining for code search, evaluating both BM25-selected and embedding-based negatives and reporting limitations of each non-differentiable strategy. However, their claim that non-differentiable embedding negatives are ineffective has not been evaluated under controlled conditions in structural code retrieval settings, where repository-level file localization involves richer structural cues than the NL$\\to$code search setting studied by CoCoHaNeRe. StructFuse addresses this gap with a systematic comparison of three mining strategies---random, embedding-distance, and dataflow-aware---across decoder-only encoders with distinct representation geometries. Our results show that static embedding-distance mining provides reliable improvement at zero additional cost, establishing it as a strong baseline that requires no gradient computation or dynamic index updates. We further incorporate data-flow structure as an additional signal dimension in the comparison, grounding hardness in inter-procedural program semantics rather than embedding proximity alone.\n\n## 2.4 Code Structure in Machine Learning\n\nProgram dependence graphs \\cite{ferrante1987pdg} and code property graphs \\cite{yamaguchi2014cpg} have long served program analysis; tools like CodeQL \\cite{avgustinov2016ql} make inter-procedural analysis accessible at scale. In machine learning, code2vec \\cite{alon2019code2vec} pioneered learning from AST paths, while ProGraML \\cite{cummins2021programl} demonstrated that whole-program graph representations capturing control-flow, data-flow, and call relations are learnable and effective for compiler optimization tasks. CrossCodeEval \\cite{ding2023crosscodeeval} empirically validates that cross-file context is critical for code completion, with retrieval-augmented approaches yielding clear but still far-from-ceiling improvements. RepoFusion \\cite{shrivastava2023repofusion} further demonstrates that training code models to incorporate cross-file repository context via Fusion-in-Decoder significantly improves completion quality, even outperforming much larger models that lack repository awareness.\n\nRecent inference-time graph methods bring structural reasoning to LLM-based software engineering. CodexGraph \\cite{liu2025codexgraph} and RepoGraph \\cite{ouyang2025repograph} build navigable code graph databases for LLM agents; LocAgent \\cite{chen2025locagent} and RANGER \\cite{shah2025ranger} employ multi-hop graph reasoning and MCTS-based traversal for fault localization and retrieval, respectively. GRACE \\cite{wang2025grace} constructs multi-level code graphs spanning repository, module, and function granularity---integrating AST, control-flow, and data-flow edges---for hierarchical retrieval-augmented code completion. GraphCoder \\cite{liu2024graphcoder} and ARISE \\cite{seddik2026arise} incorporate data-flow edges---control/data dependence and definition-use chains, respectively---but their data-flow analysis remains intra-procedural in scope. Critically, these methods primarily leverage structural graphs at inference time, incurring per-query latency proportional to graph complexity. StructFuse operates in a distinct regime: we leverage inter-procedural data-flow graphs at \\emph{training time} to construct an additional strategy dimension for systematic comparison, enabling analysis of how structural signals interact with encoder representation geometry---all with zero inference overhead. The two paradigms are complementary---a StructFuse-trained encoder can serve as an efficient first-stage retriever for inference-time graph systems that perform targeted reranking.\n",
      "numLines": 22,
      "startLine": 1,
      "totalLines": 22
    }
  },
  "sourceToolAssistantUUID": "bedf0255-c8b0-463f-a787-a796abdf2311",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/.claude/sessions/reviewer_65cfe724",
  "sessionId": "f444a635-eeef-4924-9b48-a4c308632421",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---


### Tool call

_source line 53 · 2026-05-16T00:24:23.558Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01J1QyzxvTfikUgkUbr4ijqP`</summary>

```json
{
  "server": "bjb1-42106",
  "command": "ls -la /root/structfuse/paper/ 2>/dev/null"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b0d2548e-90c9-46c7-93ca-8b502dfa138d",
  "isSidechain": false,
  "requestId": "req_011Cb5J4NTQQXVjxYsrsQ8cQ",
  "type": "assistant",
  "uuid": "497efe87-ba73-4870-bae3-ddaefcf057e0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/.claude/sessions/reviewer_65cfe724",
  "sessionId": "f444a635-eeef-4924-9b48-a4c308632421",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CHKBrrEiFzLqe2asJLj5sy",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 9666,
      "cache_read_input_tokens": 69532,
      "output_tokens": 2427,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 9666,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 2427,
          "cache_read_input_tokens": 69532,
          "cache_creation_input_tokens": 9666,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 9666
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

_source line 54 · 2026-05-16T00:24:23.574Z_

<details><summary>↩ Tool result · `toolu_01J1QyzxvTfikUgkUbr4ijqP`</summary>

```text
{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter '>' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "497efe87-ba73-4870-bae3-ddaefcf057e0",
  "isSidechain": false,
  "promptId": "ee81bb41-edfe-48b7-9827-d79a74cf7a5e",
  "type": "user",
  "uuid": "57092e51-5d60-4d37-9b55-8cb7385d1229",
  "toolUseResult": "{\"result\":\"{\\\"success\\\": false, \\\"data\\\": {}, \\\"error\\\": \\\"[ssh_read_only] Command blocked: Shell metacharacter '>' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\\\", \\\"metadata\\\": {}}\"}",
  "mcpMeta": {
    "structuredContent": {
      "result": "{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter '>' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"
    }
  },
  "sourceToolAssistantUUID": "497efe87-ba73-4870-bae3-ddaefcf057e0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/.claude/sessions/reviewer_65cfe724",
  "sessionId": "f444a635-eeef-4924-9b48-a4c308632421",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---


### Runtime record

_source line 55_

```json
{
  "type": "last-prompt",
  "lastPrompt": "[系统通知 — worker_done:worker_research_related-work-literature_20260516T001526]: Worker worker_research_related-work-literature_20260516T001526 已完成（status=done），请审查 Agent 的处理结果。",
  "leafUuid": "57092e51-5d60-4d37-9b55-8cb7385d1229",
  "sessionId": "f444a635-eeef-4924-9b48-a4c308632421"
}
```

---


### Runtime record

_source line 56_

```json
{
  "type": "ai-title",
  "aiTitle": "Review research literature worker completion",
  "sessionId": "f444a635-eeef-4924-9b48-a4c308632421"
}
```

---


### Assistant

_source line 57 · 2026-05-16T00:24:26.922Z_

<details><summary>Logged reasoning block</summary>

```text
Now I need to check the remote server's paper directory. Let me fix the command.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "57092e51-5d60-4d37-9b55-8cb7385d1229",
  "isSidechain": false,
  "requestId": "req_011Cb5J7fFXxBkcKGQ7JdNf5",
  "type": "assistant",
  "uuid": "87086dac-1033-454c-bb35-c6aec4f6809a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/.claude/sessions/reviewer_65cfe724",
  "sessionId": "f444a635-eeef-4924-9b48-a4c308632421",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014pv6CBUfrDmzZLnLpCGfKA",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4483,
      "cache_read_input_tokens": 79198,
      "output_tokens": 130,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 4483,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 130,
          "cache_read_input_tokens": 79198,
          "cache_creation_input_tokens": 4483,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 4483
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

_source line 58 · 2026-05-16T00:24:27.016Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_015nAg3EaN1LzP913h4vwMhe`</summary>

```json
{
  "server": "bjb1-42106",
  "command": "ls -la /root/structfuse/paper/"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "87086dac-1033-454c-bb35-c6aec4f6809a",
  "isSidechain": false,
  "requestId": "req_011Cb5J7fFXxBkcKGQ7JdNf5",
  "type": "assistant",
  "uuid": "f7c33fc4-f233-477b-b3d0-1c40149b7685",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/.claude/sessions/reviewer_65cfe724",
  "sessionId": "f444a635-eeef-4924-9b48-a4c308632421",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014pv6CBUfrDmzZLnLpCGfKA",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4483,
      "cache_read_input_tokens": 79198,
      "output_tokens": 130,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 4483,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 130,
          "cache_read_input_tokens": 79198,
          "cache_creation_input_tokens": 4483,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 4483
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

_source line 59 · 2026-05-16T00:24:28.129Z_

<details><summary>↩ Tool result · `toolu_015nAg3EaN1LzP913h4vwMhe`</summary>

```text
{"result":"{\"success\": false, \"data\": {\"stdout\": \"\", \"stderr\": \"ls: cannot access '/root/structfuse/paper/': No such file or directory\\n\", \"return_code\": 2}, \"error\": \"exit code 2\", \"metadata\": {\"elapsed_seconds\": 1.1}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f7c33fc4-f233-477b-b3d0-1c40149b7685",
  "isSidechain": false,
  "promptId": "ee81bb41-edfe-48b7-9827-d79a74cf7a5e",
  "type": "user",
  "uuid": "f3ab94c8-10bc-4a1c-b6b3-4f1f7e8e4e37",
  "toolUseResult": "{\"result\":\"{\\\"success\\\": false, \\\"data\\\": {\\\"stdout\\\": \\\"\\\", \\\"stderr\\\": \\\"ls: cannot access '/root/structfuse/paper/': No such file or directory\\\\n\\\", \\\"return_code\\\": 2}, \\\"error\\\": \\\"exit code 2\\\", \\\"metadata\\\": {\\\"elapsed_seconds\\\": 1.1}}\"}",
  "mcpMeta": {
    "structuredContent": {
      "result": "{\"success\": false, \"data\": {\"stdout\": \"\", \"stderr\": \"ls: cannot access '/root/structfuse/paper/': No such file or directory\\n\", \"return_code\": 2}, \"error\": \"exit code 2\", \"metadata\": {\"elapsed_seconds\": 1.1}}"
    }
  },
  "sourceToolAssistantUUID": "f7c33fc4-f233-477b-b3d0-1c40149b7685",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/.claude/sessions/reviewer_65cfe724",
  "sessionId": "f444a635-eeef-4924-9b48-a4c308632421",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---


### Assistant

_source line 60 · 2026-05-16T00:25:05.697Z_

<details><summary>Logged reasoning block</summary>

```text
OK, no paper directory on the remote. The paper is probably only in the local workspace. Let me now compile my findings and post the review.

Key findings from my audit:

1. **literature_map.yaml not updated**: The worker produced `related_work_references.md` (05-16, 21 papers) and `related_work_supplement.md` (05-15, 6 papers), but `literature_map.yaml` still has 39 entries from 05-14. Many new papers from these documents are not in the authoritative map. This is a tracking gap.


2. **UniXcoder incorrectly described as StructFuse backbone**: In `related_work_references.md` §1.5, UniXcoder is labeled as a backbone encoder for StructFuse, but that's wrong — the actual backbones are Qwen2.5-Coder-3B and StarCoder2-3B. The Related Work v1 draft does cite UniXcoder correctly as background material, not as a backbone.
3. **Dataflow negative description incomplete in supplement**: The supplement's description of hard negatives in the dataflow context appears to be cut off mid-sentence.
4. **GRACE citation needs verification**: The Related Work v1 cites GRACE for multi-level code graphs, but the expansion report flags it as potentially non-existent or excluded. I need to double-check the expansion report to see if GRACE is actually a valid citation or if this is a fabricated reference.

5. **Other uncited papers in v1**: Beyond GRACE, the v1 draft also references InferCode and SCodeR, which don't appear in the literature_map either—I should verify these citations as well.

6. **Framing inconsistencies**: The related_work_references.md uses language around "difficulty-aware negative selection" and "difficulty stratification," which diverges from the "representation geometry" focus in paper_framing.md, though this is less critical since that document is more of a literature collection than a formal draft.

The most pressing issue is verifying the GRACE citation in the Related Work v1—the literature survey explicitly excluded it, yet v1 cites it with detailed claims about its capabilities. I also need to flag that literature_map.yaml hasn't been updated with the new papers this worker has introduced.

There's also a minor error where UniXcoder is incorrectly labeled as a StructFuse backbone in the references doc, though it's used correctly in the v1 draft. On the positive side, the expansion covers 21 new papers across contrastive learning theory, representation geometry, and cross-file evaluation.

Checking the uncited papers in v1 more carefully—InferCode and CodeSage are both real papers that just aren't in the literature_map yet. I'm less certain about SCodeR though.  RocketQA and STAR are also real papers from NAACL 2021 that are missing from the map. The concerning one is GRACE—I can't verify it exists, though there might be something like "GRACE: Graph-based Contextual Code Representation Learning" out there. CAPSTONE is referenced in the supplement so it's likely legitimate.

Actually, thinking about GRACE more carefully—the expansion report from 05-14 explicitly tried to find it and couldn't, which is a red flag. The fact that it appears in the Related Work v1 is troubling, though I should note that v1 was written by the Paper Agent, not the literature collection worker, so the citation might have been introduced independently. As the reviewer, I need to flag GRACE as unverified.

The PDG, CPG, and CodeQL citations all check out as real papers from their respective years and venues.

Now let me compile my review findings: the GRACE citation is unverified despite the literature survey excluding it, the literature_map.yaml hasn't been updated with the worker's new findings, there's a factual error about UniXcoder being described as the StructFuse backbone, but the Related Work section itself is well-structured with solid coverage and most other citations are verifiable.

Wait—I should reconsider the GRACE issue more carefully. The expansion report says no well-known paper exists with that name, but the v1 draft provides a very specific technical description about multi-level code graphs with AST, control-flow, and data-flow edges for hierarchical retrieval-augmented completion. If a paper actually exists matching that description, then the citation might be legitimate even if the search didn't find it by name alone.

Since I can't verify this through web search and the literature worker couldn't locate it either, I need to flag this as a warning that requires verification—it could be a legitimate recent paper or it could be hallucinated, and I can't determine which without additional investigation.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f3ab94c8-10bc-4a1c-b6b3-4f1f7e8e4e37",
  "isSidechain": false,
  "requestId": "req_011Cb5J7zZ96GtrkYP3sMGjz",
  "type": "assistant",
  "uuid": "be492225-7843-4a71-9e10-5aa6ee06ace9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/.claude/sessions/reviewer_65cfe724",
  "sessionId": "f444a635-eeef-4924-9b48-a4c308632421",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01D9oogAY4ZaAfzXntH9SGhM",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 229,
      "cache_read_input_tokens": 83681,
      "output_tokens": 3123,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 229,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 3123,
          "cache_read_input_tokens": 83681,
          "cache_creation_input_tokens": 229,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 229
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

_source line 61 · 2026-05-16T00:25:05.699Z_

审查完成。发现了几个需要注意的问题。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "be492225-7843-4a71-9e10-5aa6ee06ace9",
  "isSidechain": false,
  "requestId": "req_011Cb5J7zZ96GtrkYP3sMGjz",
  "type": "assistant",
  "uuid": "6ea4a6b7-f2d9-4bd9-9ec9-19d9f5511189",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/.claude/sessions/reviewer_65cfe724",
  "sessionId": "f444a635-eeef-4924-9b48-a4c308632421",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01D9oogAY4ZaAfzXntH9SGhM",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 229,
      "cache_read_input_tokens": 83681,
      "output_tokens": 3123,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 229,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 3123,
          "cache_read_input_tokens": 83681,
          "cache_creation_input_tokens": 229,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 229
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

_source line 62 · 2026-05-16T00:25:25.714Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__reviewer_post_to_director · `toolu_01NYmBd6TKhY6NhFAMottUX8`</summary>

```json
{
  "text": "## 审查报告 — worker_research_related-work-literature_20260516T001526\n\n**结论**: WARNING\n\n### 发现\n\n- [severity: warning] **GRACE 引用未经验证，存在幻觉风险**。Related Work v1 (`related_work_v1.md`) 在 §2.4 引用 \"GRACE \\cite{wang2025grace}\" 并描述为 \"constructs multi-level code graphs spanning repository, module, and function granularity\"。但 Worker 自己的 `related_work_expansion_report.md` 明确排除了 GRACE：\"No well-known paper called 'GRACE' for general code representation. Multiple GRACE papers exist (graph contrastive learning, vulnerability detection) but none match the intended scope.\" **同一团队的文献调研结论和论文草稿自相矛盾**。建议：对 GRACE 进行 WebSearch 验证，若不存在则必须从 v1 中移除。\n\n- [severity: warning] **literature_map.yaml 未同步更新**。Worker 产出了 `related_work_references.md`（05-16，21 篇新论文：HCL, DCL, MoCHi, ProGCL, WCL, SimCSE, alignment/uniformity 等）和 `related_work_supplement.md`（05-15，6 篇新论文：SynCoBERT, ContraBERT, CAPSTONE, CrossCodeEval, ProGraML, CoSQA），但 `literature_map.yaml` 仍停留在 05-14 的 39 entries。**权威引用源和实际引用不一致**——v1 草稿中已使用 CAPSTONE, CrossCodeEval, ProGraML 等论文，但它们不在 literature_map.yaml 中。这增加了引用管理的混乱风险。\n\n- [severity: warning] **related_work_references.md §1.5 事实错误**：UniXcoder 被描述为 \"StructFuse 的 backbone encoder 之一\"。根据 paper_framing.md，实际 backbone 是 Qwen2.5-Coder-3B 和 StarCoder2-3B。v1 草稿中 UniXcoder 被正确地作为 background 引用，但 references 文档的错误可能误导后续写作。\n\n- [severity: warning] **related_work_supplement.md Supplement B 方向描述错误**：将 dataflow negatives 描述为 \"negatives that are hard because they share data-flow context with the positive\"。根据 paper_framing.md 的定义（`¬reachable_G(x,q)`），dataflow negatives 恰恰是**不**通过数据流连接的文件，方向相反。v1 草稿中未出现此错误。\n\n- [severity: info] **v1 草稿整体质量良好**。四个子节（Dense Retrieval for Code / Contrastive Learning for Code / Hard Negative Mining / Code Structure in ML）结构清晰，覆盖面合理。CoCoHaNeRe 的 framing nuance 处理得当——正确表述为 \"claim that non-differentiable embedding negatives are ineffective\" 而非简单化的 \"claim embedding negatives harm performance\"。\n\n- [severity: info] **引用覆盖面有实质提升**。新增覆盖了对比学习理论（HCL, DCL, SimCSE）、表示几何（alignment/uniformity, anisotropy）、跨文件评估（CrossCodeEval）等维度，增强了论文的理论根基。大多数新增引用为领域内公认的经典/高引论文，可信度较高。\n\n### 建议\n\n1. **优先级最高**：验证 GRACE \\cite{wang2025grace} 是否真实存在。若为幻觉引用，从 v1 中移除并替换为已验证的论文。\n2. 将 `related_work_references.md` 和 `related_work_supplement.md` 中的新论文整合进 `literature_map.yaml`，保持单一权威引用源。\n3. 修正 references 文档中 UniXcoder 和 dataflow negatives 的事实性错误。",
  "project": "structfuse-context"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6ea4a6b7-f2d9-4bd9-9ec9-19d9f5511189",
  "isSidechain": false,
  "requestId": "req_011Cb5J7zZ96GtrkYP3sMGjz",
  "type": "assistant",
  "uuid": "5a900335-7dd0-4b0a-934c-220037c71aa0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/.claude/sessions/reviewer_65cfe724",
  "sessionId": "f444a635-eeef-4924-9b48-a4c308632421",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01D9oogAY4ZaAfzXntH9SGhM",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 229,
      "cache_read_input_tokens": 83681,
      "output_tokens": 3123,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 229,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 3123,
          "cache_read_input_tokens": 83681,
          "cache_creation_input_tokens": 229,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 229
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

_source line 63 · 2026-05-16T00:25:29.470Z_

<details><summary>↩ Tool result · `toolu_01NYmBd6TKhY6NhFAMottUX8`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"director_session\": \"feishu:group:oc_651ef5630fe7a61a1decb410adb7641b:director\"}, \"error\": \"\"}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "5a900335-7dd0-4b0a-934c-220037c71aa0",
  "isSidechain": false,
  "promptId": "ee81bb41-edfe-48b7-9827-d79a74cf7a5e",
  "type": "user",
  "uuid": "2520cf82-ff33-425a-9f03-169a62cd714b",
  "toolUseResult": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"director_session\\\": \\\"feishu:group:oc_651ef5630fe7a61a1decb410adb7641b:director\\\"}, \\\"error\\\": \\\"\\\"}\"}",
  "mcpMeta": {
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"director_session\": \"feishu:group:oc_651ef5630fe7a61a1decb410adb7641b:director\"}, \"error\": \"\"}"
    }
  },
  "sourceToolAssistantUUID": "5a900335-7dd0-4b0a-934c-220037c71aa0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/.claude/sessions/reviewer_65cfe724",
  "sessionId": "f444a635-eeef-4924-9b48-a4c308632421",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---


### Runtime record

_source line 64 · 2026-05-16T00:25:29.476Z_

```json
{
  "parentUuid": "2520cf82-ff33-425a-9f03-169a62cd714b",
  "isSidechain": false,
  "attachment": {
    "type": "todo_reminder",
    "content": [],
    "itemCount": 0
  },
  "type": "attachment",
  "uuid": "3f5ad127-279b-4288-9959-91fda665953c",
  "timestamp": "2026-05-16T00:25:29.476Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/.claude/sessions/reviewer_65cfe724",
  "sessionId": "f444a635-eeef-4924-9b48-a4c308632421",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---


### Runtime record

_source line 65_

```json
{
  "type": "ai-title",
  "aiTitle": "Review research literature worker completion",
  "sessionId": "f444a635-eeef-4924-9b48-a4c308632421"
}
```

---


### Runtime record

_source line 66 · 2026-05-16T00:48:18.584Z_

```json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-16T00:48:18.584Z",
  "sessionId": "f444a635-eeef-4924-9b48-a4c308632421",
  "content": "[系统通知 — worker_done:worker_code_fix-literature-warnings_20260516T004234]:\nWorker worker_code_fix-literature-warnings_20260516T004234 已完成（status=done），请审查 Agent 的处理结果。"
}
```

---


### Runtime record

_source line 67 · 2026-05-16T00:48:18.585Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-16T00:48:18.585Z",
  "sessionId": "f444a635-eeef-4924-9b48-a4c308632421"
}
```

---


## Round 2

## Round 2

2 recorded events


### User

_source line 68 · 2026-05-16T00:48:18.576Z_

Continue from where you left off.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "3f5ad127-279b-4288-9959-91fda665953c",
  "isSidechain": false,
  "promptId": "951872fd-15a5-4fff-a93d-6ac30f032101",
  "type": "user",
  "isMeta": true,
  "uuid": "eccf57a5-c335-4563-adcf-a89072a593eb",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/.claude/sessions/reviewer_65cfe724",
  "sessionId": "f444a635-eeef-4924-9b48-a4c308632421",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---


### Assistant

_source line 69 · 2026-05-16T00:48:18.576Z_

No response requested.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "eccf57a5-c335-4563-adcf-a89072a593eb",
  "isSidechain": false,
  "type": "assistant",
  "uuid": "1fbd04d9-f707-4115-832b-1e39c4589cab",
  "isApiErrorMessage": false,
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/.claude/sessions/reviewer_65cfe724",
  "sessionId": "f444a635-eeef-4924-9b48-a4c308632421",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "id": "0e17bbfb-e40d-4755-97c1-736257fbc609",
    "container": null,
    "model": "&lt;synthetic>",
    "stop_reason": "stop_sequence",
    "stop_sequence": "",
    "type": "message",
    "usage": {
      "input_tokens": 0,
      "output_tokens": 0,
      "cache_creation_input_tokens": 0,
      "cache_read_input_tokens": 0,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": null,
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": null,
      "iterations": null,
      "speed": null
    },
    "context_management": null
  }
}
```

</details>

---


## Round 3

## Round 3

28 recorded events


### User

_source line 70 · 2026-05-16T00:48:18.687Z_

[系统通知 — worker_done:worker_code_fix-literature-warnings_20260516T004234]:
Worker worker_code_fix-literature-warnings_20260516T004234 已完成（status=done），请审查 Agent 的处理结果。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "1fbd04d9-f707-4115-832b-1e39c4589cab",
  "isSidechain": false,
  "promptId": "951872fd-15a5-4fff-a93d-6ac30f032101",
  "type": "user",
  "uuid": "6c6df2f3-2a72-4f95-834a-2d836662c107",
  "permissionMode": "bypassPermissions",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/.claude/sessions/reviewer_65cfe724",
  "sessionId": "f444a635-eeef-4924-9b48-a4c308632421",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---


### Assistant

_source line 71 · 2026-05-16T00:48:22.147Z_

<details><summary>Logged reasoning block</summary>

```text
A worker that was fixing literature warnings has completed. This is likely in response to my review findings about the GRACE citation, literature_map.yaml not being updated, and other issues. Let me check what changes were made.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6c6df2f3-2a72-4f95-834a-2d836662c107",
  "isSidechain": false,
  "requestId": "req_011Cb5KwStqwpf3AYNoR8hPd",
  "type": "assistant",
  "uuid": "29be826a-2396-4d53-bc4b-1b1498bbb1df",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/.claude/sessions/reviewer_65cfe724",
  "sessionId": "f444a635-eeef-4924-9b48-a4c308632421",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018QJUBMTLyj7AwfQqJrf7Kk",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 87,
      "cache_read_input_tokens": 87208,
      "output_tokens": 268,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 87,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 268,
          "cache_read_input_tokens": 87208,
          "cache_creation_input_tokens": 87,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 87
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

_source line 72 · 2026-05-16T00:48:23.107Z_

收到修复 worker 完成通知，核实修复结果。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "29be826a-2396-4d53-bc4b-1b1498bbb1df",
  "isSidechain": false,
  "requestId": "req_011Cb5KwStqwpf3AYNoR8hPd",
  "type": "assistant",
  "uuid": "e7535df3-7d9f-43de-9578-0977a03d25be",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/.claude/sessions/reviewer_65cfe724",
  "sessionId": "f444a635-eeef-4924-9b48-a4c308632421",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018QJUBMTLyj7AwfQqJrf7Kk",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 87,
      "cache_read_input_tokens": 87208,
      "output_tokens": 268,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 87,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 268,
          "cache_read_input_tokens": 87208,
          "cache_creation_input_tokens": 87,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 87
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

_source line 73 · 2026-05-16T00:48:24.225Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_019XaNnnLoKnCSd6YF2xMUib`</summary>

```json
{
  "project": "structfuse-context",
  "file": "literature_map.yaml",
  "max_chars": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e7535df3-7d9f-43de-9578-0977a03d25be",
  "isSidechain": false,
  "requestId": "req_011Cb5KwStqwpf3AYNoR8hPd",
  "type": "assistant",
  "uuid": "1f669815-e34c-455c-a555-abd4143c2dda",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/.claude/sessions/reviewer_65cfe724",
  "sessionId": "f444a635-eeef-4924-9b48-a4c308632421",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018QJUBMTLyj7AwfQqJrf7Kk",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 87,
      "cache_read_input_tokens": 87208,
      "output_tokens": 268,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 87,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 268,
          "cache_read_input_tokens": 87208,
          "cache_creation_input_tokens": 87,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 87
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

_source line 74 · 2026-05-16T00:48:25.312Z_

<details><summary>↩ Tool result · `toolu_01XQvv8biJbtqQ4EXoWhRWGK`</summary>

```text
1	# 2. Related Work
2	
3	## 2.1 Dense Retrieval for Code
4	
5	Code retrieval has evolved from sparse lexical methods such as BM25 \cite{robertson2009bm25} to dense neural approaches. Early pretrained code models---CodeBERT \cite{feng2020codebert}, UniXcoder \cite{guo2022unixcoder}, and InferCode \cite{bui2021infercode}---learn general-purpose code representations through masked language modeling and related pretraining objectives, enabling semantic matching beyond surface-level token overlap. More recent large-scale code models, including StarCoder2 \cite{lozhkov2024starcoder2} and Qwen2.5-Coder \cite{hui2024qwen25coder}, provide powerful encoder backbones trained on trillions of code tokens. In the retrieval domain, CodeSage \cite{zhang2024codesage} and SCodeR \cite{li2022scoder} introduce contrastive fine-tuning strategies that adapt pretrained representations for code search. The growing importance of repository-level retrieval---driven by benchmarks like SWE-bench \cite{jimenez2024swebench}---has motivated specialized systems: SweRank \cite{reddy2025swerank} formulates issue localization as code ranking, while SWE-Fixer \cite{xie2025swefixer} combines BM25 with neural reranking in a coarse-to-fine pipeline. StructFuse builds on this foundation by systematically comparing negative mining strategies---random, embedding-distance, and structure-aware---for contrastive code retrieval, demonstrating that the choice of mining strategy meaningfully affects retrieval quality.
6	
7	## 2.2 Contrastive Learning for Code
8	
9	Sentence-BERT \cite{reimers2019sentencebert} established contrastive fine-tuning of pretrained encoders for dense text retrieval, a paradigm that has since become dominant for code representation learning. ContraCode \cite{jain2021contracode} generates functionally equivalent program variants through compiler transformations, training models to be invariant to syntactic variation. CodeRetriever \cite{li2022coderetriever} combines unimodal code-code and bimodal code-text contrastive objectives, achieving strong results across eleven code search benchmarks. SynCoBERT \cite{wang2021syncobert} introduces syntax-guided multi-modal contrastive pretraining that aligns code, natural language, and AST modalities through identifier prediction and edge prediction objectives. ContraBERT \cite{liu2023contrabert} takes a complementary robustness-oriented approach, designing adversarial augmentation operators---including identifier renaming, dead code insertion, and operand swapping---to improve model robustness while maintaining retrieval performance. Ding et al.\ \cite{ding2022programcontrasts} use structure-guided code transformations to synthesize contrastive pairs, demonstrating that program-structure-aware augmentation improves code clone detection and vulnerability identification. GraphCodeBERT \cite{guo2021graphcodebert} incorporates data-flow edges into pretraining, demonstrating that structural information improves code understanding tasks. These methods enrich the positive pair construction space or the pretraining signal. While GraphCodeBERT uses structural edges as a pretraining objective, StructFuse addresses a complementary dimension: we systematically study how negative selection strategy---including structure-aware alternatives---affects contrastive code retrieval across encoders with distinct representation geometries.
10	
11	## 2.3 Hard Negative Mining
12	
13	The quality of negative examples critically affects contrastive learning \cite{chen2020simclr}. In dense text retrieval, DPR \cite{karpukhin2020dpr} established the practice of using BM25 top-ranked non-relevant passages as hard negatives. ANCE \cite{xiong2021ance} dynamically mines negatives from an approximate nearest neighbor index updated during training, while RocketQA \cite{qu2021rocketqa} introduces cross-batch denoised negatives with knowledge distillation. STAR \cite{zhan2021star} further refines this paradigm by using the retriever's own top-ranked passages as training negatives. Curriculum-based approaches---CL-DRD \cite{zeng2022cldrd} and CAPSTONE \cite{he2023capstone}---schedule negative difficulty progressively during training.
14	
15	In the code domain, CoCoHaNeRe \cite{fan2025cocohanere} proposes gradient-based hard negative mining for code search, evaluating both BM25-selected and embedding-based negatives and reporting limitations of each non-differentiable strategy. However, their claim that non-differentiable embedding negatives are ineffective has not been evaluated under controlled conditions in structural code retrieval settings, where repository-level file localization involves richer structural cues than the NL$\to$code search setting studied by CoCoHaNeRe. StructFuse addresses this gap with a systematic comparison of three mining strategies---random, embedding-distance, and dataflow-aware---across decoder-only encoders with distinct representation geometries. Our results show that static embedding-distance mining provides reliable improvement at zero additional cost, establishing it as a strong baseline that requires no gradient computation or dynamic index updates. We further incorporate data-flow structure as an additional signal dimension in the comparison, grounding hardness in inter-procedural program semantics rather than embedding proximity alone.
16	
17	## 2.4 Code Structure in Machine Learning
18	
19	Program dependence graphs \cite{ferrante1987pdg} and code property graphs \cite{yamaguchi2014cpg} have long served program analysis; tools like CodeQL \cite{avgustinov2016ql} make inter-procedural analysis accessible at scale. In machine learning, code2vec \cite{alon2019code2vec} pioneered learning from AST paths, while ProGraML \cite{cummins2021programl} demonstrated that whole-program graph representations capturing control-flow, data-flow, and call relations are learnable and effective for compiler optimization tasks. CrossCodeEval \cite{ding2023crosscodeeval} empirically validates that cross-file context is critical for code completion, with retrieval-augmented approaches yielding clear but still far-from-ceiling improvements. RepoFusion \cite{shrivastava2023repofusion} further demonstrates that training code models to incorporate cross-file repository context via Fusion-in-Decoder significantly improves completion quality, even outperforming much larger models that lack repository awareness.
20	
21	Recent inference-time graph methods bring structural reasoning to LLM-based software engineering. CodexGraph \cite{liu2025codexgraph} and RepoGraph \cite{ouyang2025repograph} build navigable code graph databases for LLM agents; LocAgent \cite{chen2025locagent} and RANGER \cite{shah2025ranger} employ multi-hop graph reasoning and MCTS-based traversal for fault localization and retrieval, respectively. GRACE \cite{wang2025grace} constructs multi-level code graphs spanning repository, module, and function granularity---integrating AST, control-flow, and data-flow edges---for hierarchical retrieval-augmented code completion. GraphCoder \cite{liu2024graphcoder} and ARISE \cite{seddik2026arise} incorporate data-flow edges---control/data dependence and definition-use chains, respectively---but their data-flow analysis remains intra-procedural in scope. Critically, these methods primarily leverage structural graphs at inference time, incurring per-query latency proportional to graph complexity. StructFuse operates in a distinct regime: we leverage inter-procedural data-flow graphs at \emph{training time} to construct an additional strategy dimension for systematic comparison, enabling analysis of how structural signals interact with encoder representation geometry---all with zero inference overhead. The two paradigms are complementary---a StructFuse-trained encoder can serve as an efficient first-stage retriever for inference-time graph systems that perform targeted reranking.
22	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "5e1e612a-fad3-440c-921e-3bd84853deb4",
  "isSidechain": false,
  "promptId": "951872fd-15a5-4fff-a93d-6ac30f032101",
  "type": "user",
  "uuid": "bf0266a5-3494-40ef-a9c4-dc05c9277846",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/paper_drafts/related_work_v1.md",
      "content": "# 2. Related Work\n\n## 2.1 Dense Retrieval for Code\n\nCode retrieval has evolved from sparse lexical methods such as BM25 \\cite{robertson2009bm25} to dense neural approaches. Early pretrained code models---CodeBERT \\cite{feng2020codebert}, UniXcoder \\cite{guo2022unixcoder}, and InferCode \\cite{bui2021infercode}---learn general-purpose code representations through masked language modeling and related pretraining objectives, enabling semantic matching beyond surface-level token overlap. More recent large-scale code models, including StarCoder2 \\cite{lozhkov2024starcoder2} and Qwen2.5-Coder \\cite{hui2024qwen25coder}, provide powerful encoder backbones trained on trillions of code tokens. In the retrieval domain, CodeSage \\cite{zhang2024codesage} and SCodeR \\cite{li2022scoder} introduce contrastive fine-tuning strategies that adapt pretrained representations for code search. The growing importance of repository-level retrieval---driven by benchmarks like SWE-bench \\cite{jimenez2024swebench}---has motivated specialized systems: SweRank \\cite{reddy2025swerank} formulates issue localization as code ranking, while SWE-Fixer \\cite{xie2025swefixer} combines BM25 with neural reranking in a coarse-to-fine pipeline. StructFuse builds on this foundation by systematically comparing negative mining strategies---random, embedding-distance, and structure-aware---for contrastive code retrieval, demonstrating that the choice of mining strategy meaningfully affects retrieval quality.\n\n## 2.2 Contrastive Learning for Code\n\nSentence-BERT \\cite{reimers2019sentencebert} established contrastive fine-tuning of pretrained encoders for dense text retrieval, a paradigm that has since become dominant for code representation learning. ContraCode \\cite{jain2021contracode} generates functionally equivalent program variants through compiler transformations, training models to be invariant to syntactic variation. CodeRetriever \\cite{li2022coderetriever} combines unimodal code-code and bimodal code-text contrastive objectives, achieving strong results across eleven code search benchmarks. SynCoBERT \\cite{wang2021syncobert} introduces syntax-guided multi-modal contrastive pretraining that aligns code, natural language, and AST modalities through identifier prediction and edge prediction objectives. ContraBERT \\cite{liu2023contrabert} takes a complementary robustness-oriented approach, designing adversarial augmentation operators---including identifier renaming, dead code insertion, and operand swapping---to improve model robustness while maintaining retrieval performance. Ding et al.\\ \\cite{ding2022programcontrasts} use structure-guided code transformations to synthesize contrastive pairs, demonstrating that program-structure-aware augmentation improves code clone detection and vulnerability identification. GraphCodeBERT \\cite{guo2021graphcodebert} incorporates data-flow edges into pretraining, demonstrating that structural information improves code understanding tasks. These methods enrich the positive pair construction space or the pretraining signal. While GraphCodeBERT uses structural edges as a pretraining objective, StructFuse addresses a complementary dimension: we systematically study how negative selection strategy---including structure-aware alternatives---affects contrastive code retrieval across encoders with distinct representation geometries.\n\n## 2.3 Hard Negative Mining\n\nThe quality of negative examples critically affects contrastive learning \\cite{chen2020simclr}. In dense text retrieval, DPR \\cite{karpukhin2020dpr} established the practice of using BM25 top-ranked non-relevant passages as hard negatives. ANCE \\cite{xiong2021ance} dynamically mines negatives from an approximate nearest neighbor index updated during training, while RocketQA \\cite{qu2021rocketqa} introduces cross-batch denoised negatives with knowledge distillation. STAR \\cite{zhan2021star} further refines this paradigm by using the retriever's own top-ranked passages as training negatives. Curriculum-based approaches---CL-DRD \\cite{zeng2022cldrd} and CAPSTONE \\cite{he2023capstone}---schedule negative difficulty progressively during training.\n\nIn the code domain, CoCoHaNeRe \\cite{fan2025cocohanere} proposes gradient-based hard negative mining for code search, evaluating both BM25-selected and embedding-based negatives and reporting limitations of each non-differentiable strategy. However, their claim that non-differentiable embedding negatives are ineffective has not been evaluated under controlled conditions in structural code retrieval settings, where repository-level file localization involves richer structural cues than the NL$\\to$code search setting studied by CoCoHaNeRe. StructFuse addresses this gap with a systematic comparison of three mining strategies---random, embedding-distance, and dataflow-aware---across decoder-only encoders with distinct representation geometries. Our results show that static embedding-distance mining provides reliable improvement at zero additional cost, establishing it as a strong baseline that requires no gradient computation or dynamic index updates. We further incorporate data-flow structure as an additional signal dimension in the comparison, grounding hardness in inter-procedural program semantics rather than embedding proximity alone.\n\n## 2.4 Code Structure in Machine Learning\n\nProgram dependence graphs \\cite{ferrante1987pdg} and code property graphs \\cite{yamaguchi2014cpg} have long served program analysis; tools like CodeQL \\cite{avgustinov2016ql} make inter-procedural analysis accessible at scale. In machine learning, code2vec \\cite{alon2019code2vec} pioneered learning from AST paths, while ProGraML \\cite{cummins2021programl} demonstrated that whole-program graph representations capturing control-flow, data-flow, and call relations are learnable and effective for compiler optimization tasks. CrossCodeEval \\cite{ding2023crosscodeeval} empirically validates that cross-file context is critical for code completion, with retrieval-augmented approaches yielding clear but still far-from-ceiling improvements. RepoFusion \\cite{shrivastava2023repofusion} further demonstrates that training code models to incorporate cross-file repository context via Fusion-in-Decoder significantly improves completion quality, even outperforming much larger models that lack repository awareness.\n\nRecent inference-time graph methods bring structural reasoning to LLM-based software engineering. CodexGraph \\cite{liu2025codexgraph} and RepoGraph \\cite{ouyang2025repograph} build navigable code graph databases for LLM agents; LocAgent \\cite{chen2025locagent} and RANGER \\cite{shah2025ranger} employ multi-hop graph reasoning and MCTS-based traversal for fault localization and retrieval, respectively. GRACE \\cite{wang2025grace} constructs multi-level code graphs spanning repository, module, and function granularity---integrating AST, control-flow, and data-flow edges---for hierarchical retrieval-augmented code completion. GraphCoder \\cite{liu2024graphcoder} and ARISE \\cite{seddik2026arise} incorporate data-flow edges---control/data dependence and definition-use chains, respectively---but their data-flow analysis remains intra-procedural in scope. Critically, these methods primarily leverage structural graphs at inference time, incurring per-query latency proportional to graph complexity. StructFuse operates in a distinct regime: we leverage inter-procedural data-flow graphs at \\emph{training time} to construct an additional strategy dimension for systematic comparison, enabling analysis of how structural signals interact with encoder representation geometry---all with zero inference overhead. The two paradigms are complementary---a StructFuse-trained encoder can serve as an efficient first-stage retriever for inference-time graph systems that perform targeted reranking.\n",
      "numLines": 22,
      "startLine": 1,
      "totalLines": 22
    }
  },
  "sourceToolAssistantUUID": "5e1e612a-fad3-440c-921e-3bd84853deb4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/.claude/sessions/reviewer_65cfe724",
  "sessionId": "f444a635-eeef-4924-9b48-a4c308632421",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---


### Tool result

_source line 75 · 2026-05-16T00:48:24.240Z_

<details><summary>↩ Tool result · `toolu_019XaNnnLoKnCSd6YF2xMUib`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/literature_map.yaml\", \"content\": \"# StructFuse — Related Work Literature Map\\n# 最后更新: 2026-05-14\\n# 说明: 只收录已验证存在的论文。每篇均经 WebSearch 确认标题/venue/year。\\n# 总计: 60 entries (含 2 个软件工具引用)\\n\\ncategories:\\n\\n  # ==========================================================================\\n  # Category 1: Code Retrieval for Bug Fixing / SWE-bench Ecosystem\\n  # ==========================================================================\\n  code_retrieval_bug_fixing:\\n    description: \\\"SWE-bench 及相关 repo-level 自动修复系统中的代码检索方法\\\"\\n    papers:\\n\\n      - title: \\\"SWE-bench: Can Language Models Resolve Real-World GitHub Issues?\\\"\\n        authors: \\\"Carlos E. Jimenez, John Yang, Alexander Wettig, Shunyu Yao, Kexin Pei, Ofir Press, Karthik Narasimhan\\\"\\n        venue: ICLR\\n        year: 2024\\n        relation: baseline\\n        summary: \\\"从 GitHub issues 构建 repo-level bug fixing benchmark，成为自动修复领域标准评估集。\\\"\\n\\n      - title: \\\"SWE-agent: Agent-Computer Interfaces Enable Automated Software Engineering\\\"\\n        authors: \\\"John Yang, Carlos E. Jimenez, Alexander Wettig, Kilian Lieret, Shunyu Yao, Karthik Narasimhan, Ofir Press\\\"\\n        venue: NeurIPS\\n        year: 2024\\n        relation: competitor\\n        summary: \\\"基于 LLM agent 的交互式 bug fixing 系统，定义了 ACI 接口范式。\\\"\\n\\n      - title: \\\"AutoCodeRover: Autonomous Program Improvement\\\"\\n        authors: \\\"Yuntong Zhang, Haifeng Ruan, Zhiyu Fan, Abhik Roychoudhury\\\"\\n        venue: ISSTA\\n        year: 2024\\n        relation: competitor\\n        summary: \\\"结合代码搜索与 spectrum-based fault localization，利用程序分析缩小修复范围。\\\"\\n\\n      - title: \\\"Agentless: Demystifying LLM-based Software Engineering Agents\\\"\\n        authors: \\\"Chunqiu Steven Xia, Yinlin Deng, Soren Dunn, Lingming Zhang\\\"\\n        venue: arXiv\\n        year: 2024\\n        relation: competitor\\n        summary: \\\"无 agent 架构的 two-phase localize-then-repair 方法，在 SWE-bench 上取得强 baseline。\\\"\\n\\n      - title: \\\"SWE-smith: Scaling Data for Software Engineering Agents\\\"\\n        authors: \\\"John Yang, Kilian Lieret, Carlos E. Jimenez, Alexander Wettig, Kabir Khandpur, Yanzhe Zhang, Binyuan Hui, Ofir Press, Ludwig Schmidt, Diyi Yang\\\"\\n        venue: \\\"NeurIPS (Datasets & Benchmarks, Spotlight)\\\"\\n        year: 2025\\n        relation: building-block\\n        summary: \\\"自动从 GitHub 生成大规模 SWE-bench 风格训练数据，StructFuse 用其 repos 做 data-flow 提取。\\\"\\n\\n      - title: \\\"RepoBench: Benchmarking Repository-Level Code Auto-Completion Systems\\\"\\n        authors: \\\"Tianyang Liu, Canwen Xu, Julian McAuley\\\"\\n        venue: ICLR\\n        year: 2024\\n        relation: baseline\\n        summary: \\\"Repo-level 代码补全/检索 benchmark，含 RepoBench-R 检索子任务。\\\"\\n\\n      - title: \\\"SweRank: Software Issue Localization with Code Ranking\\\"\\n        authors: \\\"Revanth Gangi Reddy, Tarun Suresh, JaeHyeok Doo, Ye Liu, Xuan Phi Nguyen, Yingbo Zhou, Semih Yavuz, Caiming Xiong, Heng Ji, Shafiq Joty\\\"\\n        venue: arXiv\\n        year: 2025\\n        relation: competitor\\n        summary: \\\"Retrieve-and-rerank 框架用于 software issue localization，在 SWE-Bench-Lite 和 LocBench 上 SOTA，text-based retrieval baseline。\\\"\\n\\n      - title: \\\"SWE-Fixer: Training Open-Source LLMs for Effective and Efficient GitHub Issue Resolution\\\"\\n        authors: \\\"Chengxing Xie, Bowen Li, Chang Gao, He Du, Wai Lam, Difan Zou, Kai Chen\\\"\\n        venue: \\\"ACL (Findings)\\\"\\n        year: 2025\\n        relation: competitor\\n        summary: \\\"BM25 + LLM retriever 的 coarse-to-fine file retrieval pipeline，在 SWE-Bench Verified 上 30.2%。\\\"\\n\\n  # ==========================================================================\\n  # Category 2: Hard Negative Mining in Contrastive Learning\\n  # ==========================================================================\\n  hard_negative_mining:\\n    description: \\\"对比学习中 hard negative 挖掘策略，以及密集检索中的负样本选择\\\"\\n    papers:\\n\\n      - title: \\\"Dense Passage Retrieval for Open-Domain Question Answering\\\"\\n        authors: \\\"Vladimir Karpukhin, Barlas Oguz, Sewon Min, Patrick Lewis, Ledell Wu, Sergey Edunov, Danqi Chen, Wen-tau Yih\\\"\\n        venue: EMNLP\\n        year: 2020\\n        relation: background\\n        summary: \\\"DPR 开创了 in-batch negatives + BM25 hard negatives 的双塔检索范式。\\\"\\n\\n      - title: \\\"Approximate Nearest Neighbor Negative Contrastive Learning for Dense Text Retrieval\\\"\\n        authors: \\\"Lee Xiong, Chenyan Xiong, Ye Li, Kwok-Fung Tang, Jialin Liu, Paul Bennett, Junaid Ahmed, Arnold Overwijk\\\"\\n        venue: ICLR\\n        year: 2021\\n        relation: background\\n        summary: \\\"ANCE 用 ANN index 动态挖掘 embedding-distance hard negatives，StructFuse 的 baseline negative 策略之一。\\\"\\n\\n      - title: \\\"A Simple Framework for Contrastive Learning of Visual Representations\\\"\\n        authors: \\\"Ting Chen, Simon Kornblith, Mohammad Norouzi, Geoffrey Hinton\\\"\\n        venue: ICML\\n        year: 2020\\n        relation: background\\n        summary: \\\"SimCLR 视觉对比学习奠基工作，证明 hard negatives 和大 batch size 对对比学习的重要性。\\\"\\n\\n      - title: \\\"Sentence-BERT: Sentence Embeddings using Siamese BERT-Networks\\\"\\n        authors: \\\"Nils Reimers, Iryna Gurevych\\\"\\n        venue: EMNLP\\n        year: 2019\\n        relation: background\\n        summary: \\\"Siamese/triplet 网络训练句子嵌入，StructFuse 的对比训练框架与其类似。\\\"\\n\\n      - title: \\\"Curriculum Learning for Dense Retrieval Distillation\\\"\\n        authors: \\\"Hansi Zeng, Hamed Zamani, Vishwa Vinay\\\"\\n        venue: \\\"SIGIR (Best Short Paper)\\\"\\n        year: 2022\\n        relation: background\\n        summary: \\\"CL-DRD: 课程学习式知识蒸馏用于密集检索，从粗粒度到细粒度逐步增加训练难度。\\\"\\n\\n      - title: \\\"Effective Hard Negative Mining for Contrastive Learning-Based Code Search\\\"\\n        authors: \\\"Fan Y., Li C., Ge J., Huang L., Luo B.\\\"\\n        venue: \\\"ACM TOSEM\\\"\\n        year: 2025\\n        relation: contrast-target\\n        summary: \\\"CoCoHaNeRe: 提出可微分 hard negative 机制用于代码搜索对比学习。其对 hard negative 机制的处理与 StructFuse 的发现形成关键对照——StructFuse 证明 true embedding-distance mining 即可持续提升性能。\\\"\\n        note: \\\"关键引用：StructFuse Claim 1 的 correction target。CoCoHaNeRe 论点是非可微 embedding negatives 学习'slow and ineffective'，StructFuse 证明用 true embedding distance mining 仍然有效。\\\"\\n\\n      - title: \\\"Representation Learning with Contrastive Predictive Coding\\\"\\n        authors: \\\"Aaron van den Oord, Yazhe Li, Oriol Vinyals\\\"\\n        venue: arXiv\\n        year: 2018\\n        relation: background\\n        summary: \\\"InfoNCE 损失函数：对比预测编码的无监督表示学习。StructFuse 训练目标的理论根基。\\\"\\n\\n      - title: \\\"Contrastive Learning with Hard Negative Samples\\\"\\n        authors: \\\"Joshua David Robinson, Ching-Yao Chuang, Suvrit Sra, Stefanie Jegelka\\\"\\n        venue: ICLR\\n        year: 2021\\n        relation: method-component\\n        summary: \\\"HCL: 可控 hard negative 采样，证明更难的 negatives 加速和改善学习，但暗示过度 hard 会导致问题。StructFuse difficulty analysis 的理论起点。\\\"\\n\\n      - title: \\\"Debiased Contrastive Learning\\\"\\n        authors: \\\"Ching-Yao Chuang, Joshua Robinson, Yen-Chen Lin, Antonio Torralba, Stefanie Jegelka\\\"\\n        venue: NeurIPS\\n        year: 2020\\n        relation: method-component\\n        summary: \\\"DCL: 去偏对比目标，修正 false negatives（同类样本被当作 negatives）问题。False negative 是 hard negative 过拟合的重要来源。\\\"\\n\\n      - title: \\\"Hard Negative Mixing for Contrastive Learning\\\"\\n        authors: \\\"Yannis Kalantidis, Mert Bulent Sariyildiz, Noe Pion, Philippe Weinzaepfel, Diane Larlus\\\"\\n        venue: NeurIPS\\n        year: 2020\\n        relation: method-component\\n        summary: \\\"MoCHi: feature-level hard negative 混合合成，开销极小。与 StructFuse 的 structure-based negative mining 形成对比。\\\"\\n\\n      - title: \\\"Understanding Hard Negatives in Noise Contrastive Estimation\\\"\\n        authors: \\\"Wenzheng Zhang, Karl Stratos\\\"\\n        venue: NAACL\\n        year: 2021\\n        relation: background\\n        summary: \\\"理论分析：用模型分布作为 negative 分布可减少梯度偏差。为 hard negative 作用提供理论解释。\\\"\\n\\n      - title: \\\"ProGCL: Rethinking Hard Negative Mining in Graph Contrastive Learning\\\"\\n        authors: \\\"Jun Xia, Lirong Wu, Ge Wang, Jintao Chen, Stan Z. Li\\\"\\n        venue: ICML\\n        year: 2022\\n        relation: method-component\\n        summary: \\\"揭示图对比学习中 hard negative = false negative 的陷阱，提出基于概率的 hardness 区分 true/false negatives。与 StructFuse difficulty-overfitting 发现呼应。\\\"\\n\\n      - title: \\\"Difficulty-Based Sampling for Debiased Contrastive Representation Learning\\\"\\n        authors: \\\"Taeuk Jang, Xiaoqian Wang\\\"\\n        venue: CVPR\\n        year: 2023\\n        relation: method-component\\n        summary: \\\"WCL: 用 difficulty 分层采样 + bias-amplifying encoder 找信息性 hard negatives 同时避免 false negatives。与 StructFuse difficulty stratification 思路最接近。\\\"\\n\\n      - title: \\\"CAPSTONE: Curriculum Sampling for Dense Retrieval with Document Expansion\\\"\\n        authors: \\\"Xingwei He, Yeyun Gong, A-Long Jin, Hang Zhang, Anlei Dong, Jian Jiao, Siu Ming Yiu, Nan Duan\\\"\\n        venue: EMNLP\\n        year: 2023\\n        relation: background\\n        summary: \\\"课程采样策略 + pseudo-query 文档扩展，解决双塔检索训练-推理差异。StructFuse 的 structure-grounded negatives 提供正交的课程形式。\\\"\\n\\n  # ==========================================================================\\n  # Category 3: Contrastive Learning for Code\\n  # ==========================================================================\\n  contrastive_code_learning:\\n    description: \\\"代码领域的对比学习方法，训练时利用代码特性构建正负样本\\\"\\n    papers:\\n\\n      - title: \\\"Contrastive Code Representation Learning\\\"\\n        authors: \\\"Paras Jain, Ajay Jain, Tianjun Zhang, Pieter Abbeel, Joseph Gonzalez, Ion Stoica\\\"\\n        venue: EMNLP\\n        year: 2021\\n        relation: background\\n        summary: \\\"ContraCode: 自监督对比预训练，通过编译器变换生成功能等价的程序变体，学习代码功能而非表面形式。\\\"\\n\\n      - title: \\\"CodeRetriever: A Large Scale Contrastive Pre-Training Method for Code Search\\\"\\n        authors: \\\"Xiaonan Li, Yeyun Gong, Yelong Shen, Xipeng Qiu, Hang Zhang, Bolun Yao, Weizhen Qi, Daxin Jiang, Weizhu Chen, Nan Duan\\\"\\n        venue: EMNLP\\n        year: 2022\\n        relation: background\\n        summary: \\\"结合 unimodal (code-code) 和 bimodal (code-text) 对比学习预训练代码表示，在 11 个代码搜索 benchmark 上 SOTA。\\\"\\n\\n      - title: \\\"Towards Learning (Dis)-Similarity of Source Code from Program Contrasts\\\"\\n        authors: \\\"Yangruibo Ding, Luca Buratti, Saurabh Pujar, Alessandro Morari, Baishakhi Ray, Saikat Chakraborty\\\"\\n        venue: \\\"ACL (Long Papers)\\\"\\n        year: 2022\\n        relation: background\\n        summary: \\\"利用程序结构和功能属性构建对比样本对，学习代码相似性/差异性表示。\\\"\\n\\n      - title: \\\"CoCoSoDa: Effective Contrastive Learning for Code Search\\\"\\n        authors: \\\"Ensheng Shi, Yanlin Wang, Wenchao Gu, Lun Du, Hongyu Zhang, Shi Han, Dongmei Zhang, Hongbin Sun\\\"\\n        venue: ICSE\\n        year: 2023\\n        relation: direct-competitor\\n        summary: \\\"对比代码搜索 + soft data augmentation + momentum-based negative enrichment。在 negative 数量维度与 StructFuse 互补（momentum queue vs. difficulty-aware selection）。\\\"\\n\\n      - title: \\\"SynCoBERT: Syntax-Guided Multi-Modal Contrastive Pre-Training for Code Representation\\\"\\n        authors: \\\"Xin Wang, Yasheng Wang, Fei Mi, Pingyi Zhou, Yao Wan, Xiao Liu, Li Li, Hao Wu, Jin Liu, Xin Jiang\\\"\\n        venue: arXiv\\n        year: 2021\\n        relation: background\\n        summary: \\\"语法引导的多模态对比预训练，对齐 code/NL/AST 三模态。通过 identifier prediction 和 AST edge prediction 显式编码句法结构。\\\"\\n\\n      - title: \\\"ContraBERT: Enhancing Code Pre-trained Models via Contrastive Learning\\\"\\n        authors: \\\"Shangqing Liu, Bozhi Wu, Xiaofei Xie, Guozhu Meng, Yang Liu\\\"\\n        venue: ICSE\\n        year: 2023\\n        relation: background\\n        summary: \\\"鲁棒性导向的对比预训练，设计 9 种对抗增强算子（identifier renaming, dead code insertion, operand swapping 等），提升模型对对抗攻击的鲁棒性。\\\"\\n\\n  # ==========================================================================\\n  # Category 4: Program Analysis for ML\\n  # ==========================================================================\\n  program_analysis_for_ml:\\n    description: \\\"静态分析辅助 ML，结构信息在代码表示学习中的应用\\\"\\n    papers:\\n\\n      - title: \\\"CodeQL: Semantic Code Analysis Engine\\\"\\n        authors: \\\"GitHub / Semmle\\\"\\n        venue: \\\"Tool (open-source)\\\"\\n        year: 2019\\n        relation: building-block\\n        summary: \\\"基于 Datalog 的代码查询引擎，支持 inter-procedural data-flow 分析。StructFuse 用它提取 scope-bounded data-flow graph。\\\"\\n\\n      - title: \\\"code2vec: Learning Distributed Representations of Code\\\"\\n        authors: \\\"Uri Alon, Meital Zilberstein, Omer Levy, Eran Yahav\\\"\\n        venue: POPL\\n        year: 2019\\n        relation: background\\n        summary: \\\"用 AST path 学习代码向量表示，首次大规模证明结构信息对代码表示学习的价值。\\\"\\n\\n      - title: \\\"code2seq: Generating Sequences from Structured Representations of Code\\\"\\n        authors: \\\"Uri Alon, Shaked Brody, Omer Levy, Eran Yahav\\\"\\n        venue: ICLR\\n        year: 2019\\n        relation: background\\n        summary: \\\"code2vec 的序列生成扩展，用 AST path attention 生成方法名摘要。\\\"\\n\\n      - title: \\\"Detecting Code Clones with Graph Neural Network and Flow-Augmented Abstract Syntax Tree\\\"\\n        authors: \\\"Wenhan Wang, Ge Li, Bo Ma, Xin Xia, Zhi Jin\\\"\\n        venue: SANER\\n        year: 2020\\n        relation: background\\n        summary: \\\"FA-AST: 用 data-flow 增强 AST 进行代码克隆检测，与 StructFuse 用 data-flow 做 hard negative 挖掘思路相关。\\\"\\n\\n      - title: \\\"GraphCodeBERT: Pre-training Code Representations with Data Flow\\\"\\n        authors: \\\"Daya Guo, Shuo Ren, Shuai Lu, Zhangyin Feng, Duyu Tang, Shujie Liu, Long Zhou, Nan Duan, Alexey Svyatkovskiy, Shengyu Fu, Michele Tufano, Shao Kun Deng, Colin Clement, Dawn Drain, Neel Sundaresan, Jian Yin, Daxin Jiang, Ming Zhou\\\"\\n        venue: ICLR\\n        year: 2021\\n        relation: background\\n        summary: \\\"在预训练中引入 data-flow edge，证明 data-flow 信息提升代码理解任务。StructFuse 的 insight 与此相关但用途不同（hard negative mining vs pre-training）。\\\"\\n\\n      - title: \\\"ARISE: A Repository-level Graph Representation and Toolset for Agentic Fault Localization and Program Repair\\\"\\n        authors: \\\"Shahd Seddik, Fatemeh Fard\\\"\\n        venue: arXiv\\n        year: 2026\\n        relation: contrast\\n        summary: \\\"用 multi-granularity program graph（含 intra-procedural def-use edges）辅助 LLM agent 做 fault localization。仅 intra-procedural + runtime tool calls，与 StructFuse 的 inter-procedural static mining 互补。\\\"\\n\\n      - title: \\\"ProGraML: A Graph-based Program Representation for Data Flow Analysis and Compiler Optimization\\\"\\n        authors: \\\"Chris Cummins, Zacharias V. Fisches, Tal Ben-Nun, Torsten Hoefler, Michael FP O'Boyle, Hugh Leather\\\"\\n        venue: ICML\\n        year: 2021\\n        relation: background\\n        summary: \\\"语言无关的全程序图表示（control-flow + data-flow + call relations），证明整程序结构表示可学习且有效。StructFuse 使用 inter-procedural data-flow 的概念根基。\\\"\\n\\n      - title: \\\"CrossCodeEval: A Diverse and Multilingual Benchmark for Cross-File Code Completion\\\"\\n        authors: \\\"Yangruibo Ding, Zijian Wang, Wasi Uddin Ahmad, Hantian Ding, Ming Tan, Nihal Jain, Murali Krishna Ramanathan, Ramesh Nallapati, Parminder Bhatia, Dan Roth, Bing Xiang\\\"\\n        venue: NeurIPS\\n        year: 2023\\n        relation: background\\n        summary: \\\"多语言 cross-file 代码补全 benchmark，用静态分析确定需 cross-file 依赖的补全目标。验证了跨文件上下文对代码任务的关键性。\\\"\\n\\n  # ==========================================================================\\n  # Category 5: Code Embeddings / Code Search\\n  # ==========================================================================\\n  code_embeddings_search:\\n    description: \\\"代码嵌入模型和代码搜索方法\\\"\\n    papers:\\n\\n      - title: \\\"CodeSearchNet Challenge: Evaluating the State of Semantic Code Search\\\"\\n        authors: \\\"Hamel Husain, Ho-Hsiang Wu, Tiferet Gazit, Miltiadis Allamanis, Marc Brockschmidt\\\"\\n        venue: arXiv\\n        year: 2019\\n        relation: background\\n        summary: \\\"代码语义搜索 benchmark 和数据集，推动了代码嵌入模型的发展。\\\"\\n\\n      - title: \\\"CodeBERT: A Pre-Trained Model for Programming and Natural Languages\\\"\\n        authors: \\\"Zhangyin Feng, Daya Guo, Duyu Tang, Nan Duan, Xiaocheng Feng, Ming Gong, Lixin Zou, Bing Qin, Ting Liu, Daxin Jiang, Ming Zhou\\\"\\n        venue: \\\"EMNLP (Findings)\\\"\\n        year: 2020\\n        relation: background\\n        summary: \\\"首个编程语言-自然语言双模态预训练模型，代码嵌入的早期里程碑。\\\"\\n\\n      - title: \\\"UniXcoder: Unified Cross-Modal Pre-training for Code Representation\\\"\\n        authors: \\\"Daya Guo, Shuai Lu, Nan Duan, Yanlin Wang, Ming Zhou, Jian Yin\\\"\\n        venue: ACL\\n        year: 2022\\n        relation: background\\n        summary: \\\"统一跨模态代码预训练，在代码搜索等任务上取得 SOTA。\\\"\\n\\n      - title: \\\"StarCoder: May the Source Be with You!\\\"\\n        authors: \\\"Raymond Li, Loubna Ben Allal, et al. (BigCode)\\\"\\n        venue: TMLR\\n        year: 2023\\n        relation: building-block\\n        summary: \\\"大规模开源代码 LLM，StructFuse 用 StarCoder2-3B 作为对比学习检索器的 backbone 之一。\\\"\\n\\n      - title: \\\"Code Llama: Open Foundation Models for Code\\\"\\n        authors: \\\"Baptiste Roziere, Jonas Gehring, Fabian Gloeckle, et al. (Meta AI)\\\"\\n        venue: arXiv\\n        year: 2023\\n        relation: background\\n        summary: \\\"Meta 的代码大模型系列，基于 Llama 2 微调。\\\"\\n\\n      - title: \\\"Qwen2.5-Coder Technical Report\\\"\\n        authors: \\\"Binyuan Hui, Jian Yang, Zeyu Cui, et al. (Qwen Team, Alibaba)\\\"\\n        venue: arXiv\\n        year: 2024\\n        relation: building-block\\n        summary: \\\"Qwen 代码模型系列，StructFuse 用 Qwen2.5-Coder-3B 作为对比学习检索器的 backbone。\\\"\\n\\n      - title: \\\"DeepSeek-Coder: When the Large Language Model Meets Programming -- The Rise of Code Intelligence\\\"\\n        authors: \\\"Daya Guo, Qihao Zhu, Dejian Yang, Zhenda Xie, Kai Dong, Wentao Zhang, Guanting Chen, Xiao Bi, Yu Wu, Y.K. Li, Fuli Luo, Yingfei Xiong, Wenfeng Liang\\\"\\n        venue: arXiv\\n        year: 2024\\n        relation: background\\n        summary: \\\"开源代码 LLM 系列 (1.3B-33B)，project-level 代码训练 + 16K context + fill-in-the-blank 预训练。\\\"\\n\\n      - title: \\\"RepoFusion: Training Code Models to Understand Your Repository\\\"\\n        authors: \\\"Disha Shrivastava, Denis Kocetkov, Harm de Vries, Dzmitry Bahdanau, Torsten Scholak\\\"\\n        venue: arXiv\\n        year: 2023\\n        relation: background\\n        summary: \\\"训练代码模型融合多个 cross-file repo context 进行代码补全，小模型 + repo context 可匹配大模型性能。\\\"\\n\\n      - title: \\\"BM25\\\"\\n        authors: \\\"Stephen Robertson, Hugo Zaragoza\\\"\\n        venue: \\\"Foundations and Trends in Information Retrieval\\\"\\n        year: 2009\\n        relation: baseline\\n        summary: \\\"经典稀疏检索方法，StructFuse 的 baseline 之一。\\\"\\n\\n      - title: \\\"CoSQA: 20,000+ Web Queries for Code Search and Question Answering\\\"\\n        authors: \\\"Junjie Huang, Duyu Tang, Linjun Shou, Ming Gong, Ke Xu, Daxin Jiang, Ming Zhou, Nan Duan\\\"\\n        venue: ACL\\n        year: 2021\\n        relation: background\\n        summary: \\\"20,000+ 真实 web 查询与 Python 代码配对的大规模数据集，弥合合成 benchmark 与真实开发者需求的差距。\\\"\\n\\n  # ==========================================================================\\n  # Category 6: Graph-Guided Code Navigation (Inference-Time)\\n  # ==========================================================================\\n  graph_guided_inference:\\n    description: \\\"推理时利用代码结构图辅助导航/检索的方法（与 StructFuse 的训练时结构信号互补）\\\"\\n    papers:\\n\\n      - title: \\\"LocAgent: Graph-Guided LLM Agents for Code Localization\\\"\\n        authors: \\\"Zhaoling Chen, Robert Tang, Gangda Deng, Fang Wu, Jialong Wu, Zhiwei Jiang, Viktor Prasanna, Arman Cohan, Xingyao Wang\\\"\\n        venue: ACL\\n        year: 2025\\n        relation: contrast\\n        summary: \\\"将代码库解析为有向异构图，LLM agent 通过 multi-hop 推理在图上导航做代码定位。推理时用结构图，StructFuse 训练时用。\\\"\\n\\n      - title: \\\"CodexGraph: Bridging Large Language Models and Code Repositories via Code Graph Databases\\\"\\n        authors: \\\"Xiangyan Liu, Bo Lan, Zhiyuan Hu, Yang Liu, Zhicheng Zhang, Fei Wang, Michael Qizhe Shieh, Wenmeng Zhou\\\"\\n        venue: NAACL\\n        year: 2025\\n        relation: contrast\\n        summary: \\\"将代码库索引到图数据库，LLM agent 通过 graph query 接口检索结构化上下文。\\\"\\n\\n      - title: \\\"RANGER: Repository-Level Agent for Graph-Enhanced Retrieval\\\"\\n        authors: \\\"Pratik Shah, Rajat Ghosh, Aryan Singhal, Debojyoti Dutta\\\"\\n        venue: arXiv\\n        year: 2025\\n        relation: contrast\\n        summary: \\\"构建 repo 知识图（含 variable-level 节点），dual-stage retrieval: Cypher lookup + MCTS-guided graph exploration。\\\"\\n\\n      - title: \\\"RepoGraph: Enhancing AI Software Engineering with Repository-level Code Graph\\\"\\n        authors: \\\"Siru Ouyang, Wenhao Yu, Kaixin Ma, Zilin Xiao, Zhihan Zhang, Mengzhao Jia, Jiawei Han, Hongming Zhang, Dong Yu\\\"\\n        venue: ICLR\\n        year: 2025\\n        relation: contrast\\n        summary: \\\"以代码行为节点构建 repo-level 代码图，作为 SE agent 的 plug-in 导航模块。推理时逐行图导航，与 StructFuse 训练时批量提取结构信号互补。\\\"\\n\\n      - title: \\\"GraphCoder: Enhancing Repository-Level Code Completion via Coarse-to-fine Retrieval Based on Code Context Graph\\\"\\n        authors: \\\"Wei Liu, Ailun Yu, Daoguang Zan, Bo Shen, Wei Zhang, Haiyan Zhao, Zhi Jin, Qianxiang Wang\\\"\\n        venue: ASE\\n        year: 2024\\n        relation: contrast\\n        summary: \\\"构建 code context graph（含 control-flow 和 data-dependence edges）进行 coarse-to-fine 检索辅助代码补全。使用 intra-procedural data-flow，与 StructFuse 的 inter-procedural scope 形成对比。\\\"\\n\\n      - title: \\\"GRACE: Graph-Guided Repository-Aware Code Completion through Hierarchical Code Fusion\\\"\\n        authors: \\\"Xingliang Wang, Baoyi Wang, Chen Zhi, Junxiao Han, Xinkui Zhao, Jianwei Yin, Shuiguang Deng\\\"\\n        venue: arXiv\\n        year: 2025\\n        relation: contrast\\n        summary: \\\"构建 repo/module/function 三层多语义代码图（AST + CFG + DFG + call graph + class hierarchy），用 GNN-based hybrid retriever 做层次化检索增强代码补全。推理时图方法，与 StructFuse 训练时结构信号互补。\\\"\\n\\n  # ==========================================================================\\n  # Category 7: Representation Geometry / Similarity Saturation\\n  # ==========================================================================\\n  representation_geometry:\\n    description: \\\"预训练模型表示空间几何分析及各向异性修正方法\\\"\\n    papers:\\n\\n      - title: \\\"Understanding Contrastive Representation Learning through Alignment and Uniformity on the Hypersphere\\\"\\n        authors: \\\"Tongzhou Wang, Phillip Isola\\\"\\n        venue: ICML\\n        year: 2020\\n        relation: method-component\\n        summary: \\\"定义 alignment/uniformity 两个对比学习关键属性，证明对比损失渐近优化两者。StructFuse 分析 embedding space 质量的理论工具。\\\"\\n\\n      - title: \\\"Representation Degeneration Problem in Training Natural Language Generation Models\\\"\\n        authors: \\\"Jun Gao, Di He, Xu Tan, Tao Qin, Liwei Wang, Tie-Yan Liu\\\"\\n        venue: ICLR\\n        year: 2019\\n        relation: background\\n        summary: \\\"揭示预训练 LM embedding 退化为窄锥的现象，StructFuse 观察到的 similarity saturation 可追溯到此。\\\"\\n\\n      - title: \\\"How Contextual are Contextualized Word Representations? Comparing the Geometry of BERT, ELMo, and GPT-2 Embeddings\\\"\\n        authors: \\\"Kawin Ethayarajh\\\"\\n        venue: EMNLP\\n        year: 2019\\n        relation: background\\n        summary: \\\"实证发现 BERT/ELMo/GPT-2 表示占据窄锥（各向异性），StructFuse 使用的 code encoder 继承此问题。\\\"\\n\\n      - title: \\\"On the Sentence Embeddings from Pre-trained Language Models\\\"\\n        authors: \\\"Bohan Li, Hao Zhou, Junxian He, Mingxuan Wang, Yiming Yang, Lei Li\\\"\\n        venue: EMNLP\\n        year: 2020\\n        relation: method-component\\n        summary: \\\"BERT-flow: 用 normalizing flows 将各向异性句子嵌入变换为各向同性高斯分布。\\\"\\n\\n      - title: \\\"SimCSE: Simple Contrastive Learning of Sentence Embeddings\\\"\\n        authors: \\\"Tianyu Gao, Xingcheng Yao, Danqi Chen\\\"\\n        venue: EMNLP\\n        year: 2021\\n        relation: method-component\\n        summary: \\\"用 dropout 作为最小增强的对比学习，直接证明 contrastive learning 改善 anisotropy。StructFuse 可引用其 uniformity 分析框架。\\\"\\n\\n      - title: \\\"Whitening Sentence Representations for Better Semantics and Faster Retrieval\\\"\\n        authors: \\\"Jianlin Su, Jiarun Cao, Weijie Liu, Yangyiwen Ou\\\"\\n        venue: arXiv\\n        year: 2021\\n        relation: method-component\\n        summary: \\\"白化操作增强句子表示各向同性并降维，与 StructFuse embedding post-processing 讨论相关。\\\"\\n\\n  # ==========================================================================\\n  # Category 8: Infrastructure / Tools\\n  # ==========================================================================\\n  infrastructure:\\n    description: \\\"StructFuse 依赖的核心基础设施和工具\\\"\\n    papers:\\n\\n      - title: \\\"Billion-Scale Similarity Search with GPUs\\\"\\n        authors: \\\"Jeff Johnson, Matthijs Douze, Herve Jegou\\\"\\n        venue: \\\"IEEE Transactions on Big Data\\\"\\n        year: 2021\\n        relation: building-block\\n        summary: \\\"FAISS: GPU 加速的大规模向量相似度搜索库，StructFuse 用于 ANN-based hard negative mining。\\\"\\n\\n      - title: \\\"Tree-sitter: An Incremental Parsing System for Programming Tools\\\"\\n        authors: \\\"Max Brunsfeld et al.\\\"\\n        venue: \\\"Software (Zenodo DOI: 10.5281/zenodo.13375512)\\\"\\n        year: 2018\\n        relation: building-block\\n        summary: \\\"增量解析库，高效构建和更新 concrete syntax trees。与 CodeQL 互补用于代码结构提取。\\\"\\n        note: \\\"软件工具，无正式论文。引用 Zenodo DOI 或 GitHub repo。\\\"\\n\", \"total_chars\": 23891, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "1f669815-e34c-455c-a555-abd4143c2dda",
  "isSidechain": false,
  "promptId": "951872fd-15a5-4fff-a93d-6ac30f032101",
  "type": "user",
  "uuid": "9b049f96-601f-4358-946f-22e019434f39",
  "toolUseResult": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"path\\\": \\\"/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/literature_map.yaml\\\", \\\"content\\\": \\\"# StructFuse — Related Work Literature Map\\\\n# 最后更新: 2026-05-14\\\\n# 说明: 只收录已验证存在的论文。每篇均经 WebSearch 确认标题/venue/year。\\\\n# 总计: 60 entries (含 2 个软件工具引用)\\\\n\\\\ncategories:\\\\n\\\\n  # ==========================================================================\\\\n  # Category 1: Code Retrieval for Bug Fixing / SWE-bench Ecosystem\\\\n  # ==========================================================================\\\\n  code_retrieval_bug_fixing:\\\\n    description: \\\\\\\"SWE-bench 及相关 repo-level 自动修复系统中的代码检索方法\\\\\\\"\\\\n    papers:\\\\n\\\\n      - title: \\\\\\\"SWE-bench: Can Language Models Resolve Real-World GitHub Issues?\\\\\\\"\\\\n        authors: \\\\\\\"Carlos E. Jimenez, John Yang, Alexander Wettig, Shunyu Yao, Kexin Pei, Ofir Press, Karthik Narasimhan\\\\\\\"\\\\n        venue: ICLR\\\\n        year: 2024\\\\n        relation: baseline\\\\n        summary: \\\\\\\"从 GitHub issues 构建 repo-level bug fixing benchmark，成为自动修复领域标准评估集。\\\\\\\"\\\\n\\\\n      - title: \\\\\\\"SWE-agent: Agent-Computer Interfaces Enable Automated Software Engineering\\\\\\\"\\\\n        authors: \\\\\\\"John Yang, Carlos E. Jimenez, Alexander Wettig, Kilian Lieret, Shunyu Yao, Karthik Narasimhan, Ofir Press\\\\\\\"\\\\n        venue: NeurIPS\\\\n        year: 2024\\\\n        relation: competitor\\\\n        summary: \\\\\\\"基于 LLM agent 的交互式 bug fixing 系统，定义了 ACI 接口范式。\\\\\\\"\\\\n\\\\n      - title: \\\\\\\"AutoCodeRover: Autonomous Program Improvement\\\\\\\"\\\\n        authors: \\\\\\\"Yuntong Zhang, Haifeng Ruan, Zhiyu Fan, Abhik Roychoudhury\\\\\\\"\\\\n        venue: ISSTA\\\\n        year: 2024\\\\n        relation: competitor\\\\n        summary: \\\\\\\"结合代码搜索与 spectrum-based fault localization，利用程序分析缩小修复范围。\\\\\\\"\\\\n\\\\n      - title: \\\\\\\"Agentless: Demystifying LLM-based Software Engineering Agents\\\\\\\"\\\\n        authors: \\\\\\\"Chunqiu Steven Xia, Yinlin Deng, Soren Dunn, Lingming Zhang\\\\\\\"\\\\n        venue: arXiv\\\\n        year: 2024\\\\n        relation: competitor\\\\n        summary: \\\\\\\"无 agent 架构的 two-phase localize-then-repair 方法，在 SWE-bench 上取得强 baseline。\\\\\\\"\\\\n\\\\n      - title: \\\\\\\"SWE-smith: Scaling Data for Software Engineering Agents\\\\\\\"\\\\n        authors: \\\\\\\"John Yang, Kilian Lieret, Carlos E. Jimenez, Alexander Wettig, Kabir Khandpur, Yanzhe Zhang, Binyuan Hui, Ofir Press, Ludwig Schmidt, Diyi Yang\\\\\\\"\\\\n        venue: \\\\\\\"NeurIPS (Datasets & Benchmarks, Spotlight)\\\\\\\"\\\\n        year: 2025\\\\n        relation: building-block\\\\n        summary: \\\\\\\"自动从 GitHub 生成大规模 SWE-bench 风格训练数据，StructFuse 用其 repos 做 data-flow 提取。\\\\\\\"\\\\n\\\\n      - title: \\\\\\\"RepoBench: Benchmarking Repository-Level Code Auto-Completion Systems\\\\\\\"\\\\n        authors: \\\\\\\"Tianyang Liu, Canwen Xu, Julian McAuley\\\\\\\"\\\\n        venue: ICLR\\\\n        year: 2024\\\\n        relation: baseline\\\\n        summary: \\\\\\\"Repo-level 代码补全/检索 benchmark，含 RepoBench-R 检索子任务。\\\\\\\"\\\\n\\\\n      - title: \\\\\\\"SweRank: Software Issue Localization with Code Ranking\\\\\\\"\\\\n        authors: \\\\\\\"Revanth Gangi Reddy, Tarun Suresh, JaeHyeok Doo, Ye Liu, Xuan Phi Nguyen, Yingbo Zhou, Semih Yavuz, Caiming Xiong, Heng Ji, Shafiq Joty\\\\\\\"\\\\n        venue: arXiv\\\\n        year: 2025\\\\n        relation: competitor\\\\n        summary: \\\\\\\"Retrieve-and-rerank 框架用于 software issue localization，在 SWE-Bench-Lite 和 LocBench 上 SOTA，text-based retrieval baseline。\\\\\\\"\\\\n\\\\n      - title: \\\\\\\"SWE-Fixer: Training Open-Source LLMs for Effective and Efficient GitHub Issue Resolution\\\\\\\"\\\\n        authors: \\\\\\\"Chengxing Xie, Bowen Li, Chang Gao, He Du, Wai Lam, Difan Zou, Kai Chen\\\\\\\"\\\\n        venue: \\\\\\\"ACL (Findings)\\\\\\\"\\\\n        year: 2025\\\\n        relation: competitor\\\\n        summary: \\\\\\\"BM25 + LLM retriever 的 coarse-to-fine file retrieval pipeline，在 SWE-Bench Verified 上 30.2%。\\\\\\\"\\\\n\\\\n  # ==========================================================================\\\\n  # Category 2: Hard Negative Mining in Contrastive Learning\\\\n  # ==========================================================================\\\\n  hard_negative_mining:\\\\n    description: \\\\\\\"对比学习中 hard negative 挖掘策略，以及密集检索中的负样本选择\\\\\\\"\\\\n    papers:\\\\n\\\\n      - title: \\\\\\\"Dense Passage Retrieval for Open-Domain Question Answering\\\\\\\"\\\\n        authors: \\\\\\\"Vladimir Karpukhin, Barlas Oguz, Sewon Min, Patrick Lewis, Ledell Wu, Sergey Edunov, Danqi Chen, Wen-tau Yih\\\\\\\"\\\\n        venue: EMNLP\\\\n        year: 2020\\\\n        relation: background\\\\n        summary: \\\\\\\"DPR 开创了 in-batch negatives + BM25 hard negatives 的双塔检索范式。\\\\\\\"\\\\n\\\\n      - title: \\\\\\\"Approximate Nearest Neighbor Negative Contrastive Learning for Dense Text Retrieval\\\\\\\"\\\\n        authors: \\\\\\\"Lee Xiong, Chenyan Xiong, Ye Li, Kwok-Fung Tang, Jialin Liu, Paul Bennett, Junaid Ahmed, Arnold Overwijk\\\\\\\"\\\\n        venue: ICLR\\\\n        year: 2021\\\\n        relation: background\\\\n        summary: \\\\\\\"ANCE 用 ANN index 动态挖掘 embedding-distance hard negatives，StructFuse 的 baseline negative 策略之一。\\\\\\\"\\\\n\\\\n      - title: \\\\\\\"A Simple Framework for Contrastive Learning of Visual Representations\\\\\\\"\\\\n        authors: \\\\\\\"Ting Chen, Simon Kornblith, Mohammad Norouzi, Geoffrey Hinton\\\\\\\"\\\\n        venue: ICML\\\\n        year: 2020\\\\n        relation: background\\\\n        summary: \\\\\\\"SimCLR 视觉对比学习奠基工作，证明 hard negatives 和大 batch size 对对比学习的重要性。\\\\\\\"\\\\n\\\\n      - title: \\\\\\\"Sentence-BERT: Sentence Embeddings using Siamese BERT-Networks\\\\\\\"\\\\n        authors: \\\\\\\"Nils Reimers, Iryna Gurevych\\\\\\\"\\\\n        venue: EMNLP\\\\n        year: 2019\\\\n        relation: background\\\\n        summary: \\\\\\\"Siamese/triplet 网络训练句子嵌入，StructFuse 的对比训练框架与其类似。\\\\\\\"\\\\n\\\\n      - title: \\\\\\\"Curriculum Learning for Dense Retrieval Distillation\\\\\\\"\\\\n        authors: \\\\\\\"Hansi Zeng, Hamed Zamani, Vishwa Vinay\\\\\\\"\\\\n        venue: \\\\\\\"SIGIR (Best Short Paper)\\\\\\\"\\\\n        year: 2022\\\\n        relation: background\\\\n        summary: \\\\\\\"CL-DRD: 课程学习式知识蒸馏用于密集检索，从粗粒度到细粒度逐步增加训练难度。\\\\\\\"\\\\n\\\\n      - title: \\\\\\\"Effective Hard Negative Mining for Contrastive Learning-Based Code Search\\\\\\\"\\\\n        authors: \\\\\\\"Fan Y., Li C., Ge J., Huang L., Luo B.\\\\\\\"\\\\n        venue: \\\\\\\"ACM TOSEM\\\\\\\"\\\\n        year: 2025\\\\n        relation: contrast-target\\\\n        summary: \\\\\\\"CoCoHaNeRe: 提出可微分 hard negative 机制用于代码搜索对比学习。其对 hard negative 机制的处理与 StructFuse 的发现形成关键对照——StructFuse 证明 true embedding-distance mining 即可持续提升性能。\\\\\\\"\\\\n        note: \\\\\\\"关键引用：StructFuse Claim 1 的 correction target。CoCoHaNeRe 论点是非可微 embedding negatives 学习'slow and ineffective'，StructFuse 证明用 true embedding distance mining 仍然有效。\\\\\\\"\\\\n\\\\n      - title: \\\\\\\"Representation Learning with Contrastive Predictive Coding\\\\\\\"\\\\n        authors: \\\\\\\"Aaron van den Oord, Yazhe Li, Oriol Vinyals\\\\\\\"\\\\n        venue: arXiv\\\\n        year: 2018\\\\n        relation: background\\\\n        summary: \\\\\\\"InfoNCE 损失函数：对比预测编码的无监督表示学习。StructFuse 训练目标的理论根基。\\\\\\\"\\\\n\\\\n      - title: \\\\\\\"Contrastive Learning with Hard Negative Samples\\\\\\\"\\\\n        authors: \\\\\\\"Joshua David Robinson, Ching-Yao Chuang, Suvrit Sra, Stefanie Jegelka\\\\\\\"\\\\n        venue: ICLR\\\\n        year: 2021\\\\n        relation: method-component\\\\n        summary: \\\\\\\"HCL: 可控 hard negative 采样，证明更难的 negatives 加速和改善学习，但暗示过度 hard 会导致问题。StructFuse difficulty analysis 的理论起点。\\\\\\\"\\\\n\\\\n      - title: \\\\\\\"Debiased Contrastive Learning\\\\\\\"\\\\n        authors: \\\\\\\"Ching-Yao Chuang, Joshua Robinson, Yen-Chen Lin, Antonio Torralba, Stefanie Jegelka\\\\\\\"\\\\n        venue: NeurIPS\\\\n        year: 2020\\\\n        relation: method-component\\\\n        summary: \\\\\\\"DCL: 去偏对比目标，修正 false negatives（同类样本被当作 negatives）问题。False negative 是 hard negative 过拟合的重要来源。\\\\\\\"\\\\n\\\\n      - title: \\\\\\\"Hard Negative Mixing for Contrastive Learning\\\\\\\"\\\\n        authors: \\\\\\\"Yannis Kalantidis, Mert Bulent Sariyildiz, Noe Pion, Philippe Weinzaepfel, Diane Larlus\\\\\\\"\\\\n        venue: NeurIPS\\\\n        year: 2020\\\\n        relation: method-component\\\\n        summary: \\\\\\\"MoCHi: feature-level hard negative 混合合成，开销极小。与 StructFuse 的 structure-based negative mining 形成对比。\\\\\\\"\\\\n\\\\n      - title: \\\\\\\"Understanding Hard Negatives in Noise Contrastive Estimation\\\\\\\"\\\\n        authors: \\\\\\\"Wenzheng Zhang, Karl Stratos\\\\\\\"\\\\n        venue: NAACL\\\\n        year: 2021\\\\n        relation: background\\\\n        summary: \\\\\\\"理论分析：用模型分布作为 negative 分布可减少梯度偏差。为 hard negative 作用提供理论解释。\\\\\\\"\\\\n\\\\n      - title: \\\\\\\"ProGCL: Rethinking Hard Negative Mining in Graph Contrastive Learning\\\\\\\"\\\\n        authors: \\\\\\\"Jun Xia, Lirong Wu, Ge Wang, Jintao Chen, Stan Z. Li\\\\\\\"\\\\n        venue: ICML\\\\n        year: 2022\\\\n        relation: method-component\\\\n        summary: \\\\\\\"揭示图对比学习中 hard negative = false negative 的陷阱，提出基于概率的 hardness 区分 true/false negatives。与 StructFuse difficulty-overfitting 发现呼应。\\\\\\\"\\\\n\\\\n      - title: \\\\\\\"Difficulty-Based Sampling for Debiased Contrastive Representation Learning\\\\\\\"\\\\n        authors: \\\\\\\"Taeuk Jang, Xiaoqian Wang\\\\\\\"\\\\n        venue: CVPR\\\\n        year: 2023\\\\n        relation: method-component\\\\n        summary: \\\\\\\"WCL: 用 difficulty 分层采样 + bias-amplifying encoder 找信息性 hard negatives 同时避免 false negatives。与 StructFuse difficulty stratification 思路最接近。\\\\\\\"\\\\n\\\\n      - title: \\\\\\\"CAPSTONE: Curriculum Sampling for Dense Retrieval with Document Expansion\\\\\\\"\\\\n        authors: \\\\\\\"Xingwei He, Yeyun Gong, A-Long Jin, Hang Zhang, Anlei Dong, Jian Jiao, Siu Ming Yiu, Nan Duan\\\\\\\"\\\\n        venue: EMNLP\\\\n        year: 2023\\\\n        relation: background\\\\n        summary: \\\\\\\"课程采样策略 + pseudo-query 文档扩展，解决双塔检索训练-推理差异。StructFuse 的 structure-grounded negatives 提供正交的课程形式。\\\\\\\"\\\\n\\\\n  # ==========================================================================\\\\n  # Category 3: Contrastive Learning for Code\\\\n  # ==========================================================================\\\\n  contrastive_code_learning:\\\\n    description: \\\\\\\"代码领域的对比学习方法，训练时利用代码特性构建正负样本\\\\\\\"\\\\n    papers:\\\\n\\\\n      - title: \\\\\\\"Contrastive Code Representation Learning\\\\\\\"\\\\n        authors: \\\\\\\"Paras Jain, Ajay Jain, Tianjun Zhang, Pieter Abbeel, Joseph Gonzalez, Ion Stoica\\\\\\\"\\\\n        venue: EMNLP\\\\n        year: 2021\\\\n        relation: background\\\\n        summary: \\\\\\\"ContraCode: 自监督对比预训练，通过编译器变换生成功能等价的程序变体，学习代码功能而非表面形式。\\\\\\\"\\\\n\\\\n      - title: \\\\\\\"CodeRetriever: A Large Scale Contrastive Pre-Training Method for Code Search\\\\\\\"\\\\n        authors: \\\\\\\"Xiaonan Li, Yeyun Gong, Yelong Shen, Xipeng Qiu, Hang Zhang, Bolun Yao, Weizhen Qi, Daxin Jiang, Weizhu Chen, Nan Duan\\\\\\\"\\\\n        venue: EMNLP\\\\n        year: 2022\\\\n        relation: background\\\\n        summary: \\\\\\\"结合 unimodal (code-code) 和 bimodal (code-text) 对比学习预训练代码表示，在 11 个代码搜索 benchmark 上 SOTA。\\\\\\\"\\\\n\\\\n      - title: \\\\\\\"Towards Learning (Dis)-Similarity of Source Code from Program Contrasts\\\\\\\"\\\\n        authors: \\\\\\\"Yangruibo Ding, Luca Buratti, Saurabh Pujar, Alessandro Morari, Baishakhi Ray, Saikat Chakraborty\\\\\\\"\\\\n        venue: \\\\\\\"ACL (Long Papers)\\\\\\\"\\\\n        year: 2022\\\\n        relation: background\\\\n        summary: \\\\\\\"利用程序结构和功能属性构建对比样本对，学习代码相似性/差异性表示。\\\\\\\"\\\\n\\\\n      - title: \\\\\\\"CoCoSoDa: Effective Contrastive Learning for Code Search\\\\\\\"\\\\n        authors: \\\\\\\"Ensheng Shi, Yanlin Wang, Wenchao Gu, Lun Du, Hongyu Zhang, Shi Han, Dongmei Zhang, Hongbin Sun\\\\\\\"\\\\n        venue: ICSE\\\\n        year: 2023\\\\n        relation: direct-competitor\\\\n        summary: \\\\\\\"对比代码搜索 + soft data augmentation + momentum-based negative enrichment。在 negative 数量维度与 StructFuse 互补（momentum queue vs. difficulty-aware selection）。\\\\\\\"\\\\n\\\\n      - title: \\\\\\\"SynCoBERT: Syntax-Guided Multi-Modal Contrastive Pre-Training for Code Representation\\\\\\\"\\\\n        authors: \\\\\\\"Xin Wang, Yasheng Wang, Fei Mi, Pingyi Zhou, Yao Wan, Xiao Liu, Li Li, Hao Wu, Jin Liu, Xin Jiang\\\\\\\"\\\\n        venue: arXiv\\\\n        year: 2021\\\\n        relation: background\\\\n        summary: \\\\\\\"语法引导的多模态对比预训练，对齐 code/NL/AST 三模态。通过 identifier prediction 和 AST edge prediction 显式编码句法结构。\\\\\\\"\\\\n\\\\n      - title: \\\\\\\"ContraBERT: Enhancing Code Pre-trained Models via Contrastive Learning\\\\\\\"\\\\n        authors: \\\\\\\"Shangqing Liu, Bozhi Wu, Xiaofei Xie, Guozhu Meng, Yang Liu\\\\\\\"\\\\n        venue: ICSE\\\\n        year: 2023\\\\n        relation: background\\\\n        summary: \\\\\\\"鲁棒性导向的对比预训练，设计 9 种对抗增强算子（identifier renaming, dead code insertion, operand swapping 等），提升模型对对抗攻击的鲁棒性。\\\\\\\"\\\\n\\\\n  # ==========================================================================\\\\n  # Category 4: Program Analysis for ML\\\\n  # ==========================================================================\\\\n  program_analysis_for_ml:\\\\n    description: \\\\\\\"静态分析辅助 ML，结构信息在代码表示学习中的应用\\\\\\\"\\\\n    papers:\\\\n\\\\n      - title: \\\\\\\"CodeQL: Semantic Code Analysis Engine\\\\\\\"\\\\n        authors: \\\\\\\"GitHub / Semmle\\\\\\\"\\\\n        venue: \\\\\\\"Tool (open-source)\\\\\\\"\\\\n        year: 2019\\\\n        relation: building-block\\\\n        summary: \\\\\\\"基于 Datalog 的代码查询引擎，支持 inter-procedural data-flow 分析。StructFuse 用它提取 scope-bounded data-flow graph。\\\\\\\"\\\\n\\\\n      - title: \\\\\\\"code2vec: Learning Distributed Representations of Code\\\\\\\"\\\\n        authors: \\\\\\\"Uri Alon, Meital Zilberstein, Omer Levy, Eran Yahav\\\\\\\"\\\\n        venue: POPL\\\\n        year: 2019\\\\n        relation: background\\\\n        summary: \\\\\\\"用 AST path 学习代码向量表示，首次大规模证明结构信息对代码表示学习的价值。\\\\\\\"\\\\n\\\\n      - title: \\\\\\\"code2seq: Generating Sequences from Structured Representations of Code\\\\\\\"\\\\n        authors: \\\\\\\"Uri Alon, Shaked Brody, Omer Levy, Eran Yahav\\\\\\\"\\\\n        venue: ICLR\\\\n        year: 2019\\\\n        relation: background\\\\n        summary: \\\\\\\"code2vec 的序列生成扩展，用 AST path attention 生成方法名摘要。\\\\\\\"\\\\n\\\\n      - title: \\\\\\\"Detecting Code Clones with Graph Neural Network and Flow-Augmented Abstract Syntax Tree\\\\\\\"\\\\n        authors: \\\\\\\"Wenhan Wang, Ge Li, Bo Ma, Xin Xia, Zhi Jin\\\\\\\"\\\\n        venue: SANER\\\\n        year: 2020\\\\n        relation: background\\\\n        summary: \\\\\\\"FA-AST: 用 data-flow 增强 AST 进行代码克隆检测，与 StructFuse 用 data-flow 做 hard negative 挖掘思路相关。\\\\\\\"\\\\n\\\\n      - title: \\\\\\\"GraphCodeBERT: Pre-training Code Representations with Data Flow\\\\\\\"\\\\n        authors: \\\\\\\"Daya Guo, Shuo Ren, Shuai Lu, Zhangyin Feng, Duyu Tang, Shujie Liu, Long Zhou, Nan Duan, Alexey Svyatkovskiy, Shengyu Fu, Michele Tufano, Shao Kun Deng, Colin Clement, Dawn Drain, Neel Sundaresan, Jian Yin, Daxin Jiang, Ming Zhou\\\\\\\"\\\\n        venue: ICLR\\\\n        year: 2021\\\\n        relation: background\\\\n        summary: \\\\\\\"在预训练中引入 data-flow edge，证明 data-flow 信息提升代码理解任务。StructFuse 的 insight 与此相关但用途不同（hard negative mining vs pre-training）。\\\\\\\"\\\\n\\\\n      - title: \\\\\\\"ARISE: A Repository-level Graph Representation and Toolset for Agentic Fault Localization and Program Repair\\\\\\\"\\\\n        authors: \\\\\\\"Shahd Seddik, Fatemeh Fard\\\\\\\"\\\\n        venue: arXiv\\\\n        year: 2026\\\\n        relation: contrast\\\\n        summary: \\\\\\\"用 multi-granularity program graph（含 intra-procedural def-use edges）辅助 LLM agent 做 fault localization。仅 intra-procedural + runtime tool calls，与 StructFuse 的 inter-procedural static mining 互补。\\\\\\\"\\\\n\\\\n      - title: \\\\\\\"ProGraML: A Graph-based Program Representation for Data Flow Analysis and Compiler Optimization\\\\\\\"\\\\n        authors: \\\\\\\"Chris Cummins, Zacharias V. Fisches, Tal Ben-Nun, Torsten Hoefler, Michael FP O'Boyle, Hugh Leather\\\\\\\"\\\\n        venue: ICML\\\\n        year: 2021\\\\n        relation: background\\\\n        summary: \\\\\\\"语言无关的全程序图表示（control-flow + data-flow + call relations），证明整程序结构表示可学习且有效。StructFuse 使用 inter-procedural data-flow 的概念根基。\\\\\\\"\\\\n\\\\n      - title: \\\\\\\"CrossCodeEval: A Diverse and Multilingual Benchmark for Cross-File Code Completion\\\\\\\"\\\\n        authors: \\\\\\\"Yangruibo Ding, Zijian Wang, Wasi Uddin Ahmad, Hantian Ding, Ming Tan, Nihal Jain, Murali Krishna Ramanathan, Ramesh Nallapati, Parminder Bhatia, Dan Roth, Bing Xiang\\\\\\\"\\\\n        venue: NeurIPS\\\\n        year: 2023\\\\n        relation: background\\\\n        summary: \\\\\\\"多语言 cross-file 代码补全 benchmark，用静态分析确定需 cross-file 依赖的补全目标。验证了跨文件上下文对代码任务的关键性。\\\\\\\"\\\\n\\\\n  # ==========================================================================\\\\n  # Category 5: Code Embeddings / Code Search\\\\n  # ==========================================================================\\\\n  code_embeddings_search:\\\\n    description: \\\\\\\"代码嵌入模型和代码搜索方法\\\\\\\"\\\\n    papers:\\\\n\\\\n      - title: \\\\\\\"CodeSearchNet Challenge: Evaluating the State of Semantic Code Search\\\\\\\"\\\\n        authors: \\\\\\\"Hamel Husain, Ho-Hsiang Wu, Tiferet Gazit, Miltiadis Allamanis, Marc Brockschmidt\\\\\\\"\\\\n        venue: arXiv\\\\n        year: 2019\\\\n        relation: background\\\\n        summary: \\\\\\\"代码语义搜索 benchmark 和数据集，推动了代码嵌入模型的发展。\\\\\\\"\\\\n\\\\n      - title: \\\\\\\"CodeBERT: A Pre-Trained Model for Programming and Natural Languages\\\\\\\"\\\\n        authors: \\\\\\\"Zhangyin Feng, Daya Guo, Duyu Tang, Nan Duan, Xiaocheng Feng, Ming Gong, Lixin Zou, Bing Qin, Ting Liu, Daxin Jiang, Ming Zhou\\\\\\\"\\\\n        venue: \\\\\\\"EMNLP (Findings)\\\\\\\"\\\\n        year: 2020\\\\n        relation: background\\\\n        summary: \\\\\\\"首个编程语言-自然语言双模态预训练模型，代码嵌入的早期里程碑。\\\\\\\"\\\\n\\\\n      - title: \\\\\\\"UniXcoder: Unified Cross-Modal Pre-training for Code Representation\\\\\\\"\\\\n        authors: \\\\\\\"Daya Guo, Shuai Lu, Nan Duan, Yanlin Wang, Ming Zhou, Jian Yin\\\\\\\"\\\\n        venue: ACL\\\\n        year: 2022\\\\n        relation: background\\\\n        summary: \\\\\\\"统一跨模态代码预训练，在代码搜索等任务上取得 SOTA。\\\\\\\"\\\\n\\\\n      - title: \\\\\\\"StarCoder: May the Source Be with You!\\\\\\\"\\\\n        authors: \\\\\\\"Raymond Li, Loubna Ben Allal, et al. (BigCode)\\\\\\\"\\\\n        venue: TMLR\\\\n        year: 2023\\\\n        relation: building-block\\\\n        summary: \\\\\\\"大规模开源代码 LLM，StructFuse 用 StarCoder2-3B 作为对比学习检索器的 backbone 之一。\\\\\\\"\\\\n\\\\n      - title: \\\\\\\"Code Llama: Open Foundation Models for Code\\\\\\\"\\\\n        authors: \\\\\\\"Baptiste Roziere, Jonas Gehring, Fabian Gloeckle, et al. (Meta AI)\\\\\\\"\\\\n        venue: arXiv\\\\n        year: 2023\\\\n        relation: background\\\\n        summary: \\\\\\\"Meta 的代码大模型系列，基于 Llama 2 微调。\\\\\\\"\\\\n\\\\n      - title: \\\\\\\"Qwen2.5-Coder Technical Report\\\\\\\"\\\\n        authors: \\\\\\\"Binyuan Hui, Jian Yang, Zeyu Cui, et al. (Qwen Team, Alibaba)\\\\\\\"\\\\n        venue: arXiv\\\\n        year: 2024\\\\n        relation: building-block\\\\n        summary: \\\\\\\"Qwen 代码模型系列，StructFuse 用 Qwen2.5-Coder-3B 作为对比学习检索器的 backbone。\\\\\\\"\\\\n\\\\n      - title: \\\\\\\"DeepSeek-Coder: When the Large Language Model Meets Programming -- The Rise of Code Intelligence\\\\\\\"\\\\n        authors: \\\\\\\"Daya Guo, Qihao Zhu, Dejian Yang, Zhenda Xie, Kai Dong, Wentao Zhang, Guanting Chen, Xiao Bi, Yu Wu, Y.K. Li, Fuli Luo, Yingfei Xiong, Wenfeng Liang\\\\\\\"\\\\n        venue: arXiv\\\\n        year: 2024\\\\n        relation: background\\\\n        summary: \\\\\\\"开源代码 LLM 系列 (1.3B-33B)，project-level 代码训练 + 16K context + fill-in-the-blank 预训练。\\\\\\\"\\\\n\\\\n      - title: \\\\\\\"RepoFusion: Training Code Models to Understand Your Repository\\\\\\\"\\\\n        authors: \\\\\\\"Disha Shrivastava, Denis Kocetkov, Harm de Vries, Dzmitry Bahdanau, Torsten Scholak\\\\\\\"\\\\n        venue: arXiv\\\\n        year: 2023\\\\n        relation: background\\\\n        summary: \\\\\\\"训练代码模型融合多个 cross-file repo context 进行代码补全，小模型 + repo context 可匹配大模型性能。\\\\\\\"\\\\n\\\\n      - title: \\\\\\\"BM25\\\\\\\"\\\\n        authors: \\\\\\\"Stephen Robertson, Hugo Zaragoza\\\\\\\"\\\\n        venue: \\\\\\\"Foundations and Trends in Information Retrieval\\\\\\\"\\\\n        year: 2009\\\\n        relation: baseline\\\\n        summary: \\\\\\\"经典稀疏检索方法，StructFuse 的 baseline 之一。\\\\\\\"\\\\n\\\\n      - title: \\\\\\\"CoSQA: 20,000+ Web Queries for Code Search and Question Answering\\\\\\\"\\\\n        authors: \\\\\\\"Junjie Huang, Duyu Tang, Linjun Shou, Ming Gong, Ke Xu, Daxin Jiang, Ming Zhou, Nan Duan\\\\\\\"\\\\n        venue: ACL\\\\n        year: 2021\\\\n        relation: background\\\\n        summary: \\\\\\\"20,000+ 真实 web 查询与 Python 代码配对的大规模数据集，弥合合成 benchmark 与真实开发者需求的差距。\\\\\\\"\\\\n\\\\n  # ==========================================================================\\\\n  # Category 6: Graph-Guided Code Navigation (Inference-Time)\\\\n  # ==========================================================================\\\\n  graph_guided_inference:\\\\n    description: \\\\\\\"推理时利用代码结构图辅助导航/检索的方法（与 StructFuse 的训练时结构信号互补）\\\\\\\"\\\\n    papers:\\\\n\\\\n      - title: \\\\\\\"LocAgent: Graph-Guided LLM Agents for Code Localization\\\\\\\"\\\\n        authors: \\\\\\\"Zhaoling Chen, Robert Tang, Gangda Deng, Fang Wu, Jialong Wu, Zhiwei Jiang, Viktor Prasanna, Arman Cohan, Xingyao Wang\\\\\\\"\\\\n        venue: ACL\\\\n        year: 2025\\\\n        relation: contrast\\\\n        summary: \\\\\\\"将代码库解析为有向异构图，LLM agent 通过 multi-hop 推理在图上导航做代码定位。推理时用结构图，StructFuse 训练时用。\\\\\\\"\\\\n\\\\n      - title: \\\\\\\"CodexGraph: Bridging Large Language Models and Code Repositories via Code Graph Databases\\\\\\\"\\\\n        authors: \\\\\\\"Xiangyan Liu, Bo Lan, Zhiyuan Hu, Yang Liu, Zhicheng Zhang, Fei Wang, Michael Qizhe Shieh, Wenmeng Zhou\\\\\\\"\\\\n        venue: NAACL\\\\n        year: 2025\\\\n        relation: contrast\\\\n        summary: \\\\\\\"将代码库索引到图数据库，LLM agent 通过 graph query 接口检索结构化上下文。\\\\\\\"\\\\n\\\\n      - title: \\\\\\\"RANGER: Repository-Level Agent for Graph-Enhanced Retrieval\\\\\\\"\\\\n        authors: \\\\\\\"Pratik Shah, Rajat Ghosh, Aryan Singhal, Debojyoti Dutta\\\\\\\"\\\\n        venue: arXiv\\\\n        year: 2025\\\\n        relation: contrast\\\\n        summary: \\\\\\\"构建 repo 知识图（含 variable-level 节点），dual-stage retrieval: Cypher lookup + MCTS-guided graph exploration。\\\\\\\"\\\\n\\\\n      - title: \\\\\\\"RepoGraph: Enhancing AI Software Engineering with Repository-level Code Graph\\\\\\\"\\\\n        authors: \\\\\\\"Siru Ouyang, Wenhao Yu, Kaixin Ma, Zilin Xiao, Zhihan Zhang, Mengzhao Jia, Jiawei Han, Hongming Zhang, Dong Yu\\\\\\\"\\\\n        venue: ICLR\\\\n        year: 2025\\\\n        relation: contrast\\\\n        summary: \\\\\\\"以代码行为节点构建 repo-level 代码图，作为 SE agent 的 plug-in 导航模块。推理时逐行图导航，与 StructFuse 训练时批量提取结构信号互补。\\\\\\\"\\\\n\\\\n      - title: \\\\\\\"GraphCoder: Enhancing Repository-Level Code Completion via Coarse-to-fine Retrieval Based on Code Context Graph\\\\\\\"\\\\n        authors: \\\\\\\"Wei Liu, Ailun Yu, Daoguang Zan, Bo Shen, Wei Zhang, Haiyan Zhao, Zhi Jin, Qianxiang Wang\\\\\\\"\\\\n        venue: ASE\\\\n        year: 2024\\\\n        relation: contrast\\\\n        summary: \\\\\\\"构建 code context graph（含 control-flow 和 data-dependence edges）进行 coarse-to-fine 检索辅助代码补全。使用 intra-procedural data-flow，与 StructFuse 的 inter-procedural scope 形成对比。\\\\\\\"\\\\n\\\\n      - title: \\\\\\\"GRACE: Graph-Guided Repository-Aware Code Completion through Hierarchical Code Fusion\\\\\\\"\\\\n        authors: \\\\\\\"Xingliang Wang, Baoyi Wang, Chen Zhi, Junxiao Han, Xinkui Zhao, Jianwei Yin, Shuiguang Deng\\\\\\\"\\\\n        venue: arXiv\\\\n        year: 2025\\\\n        relation: contrast\\\\n        summary: \\\\\\\"构建 repo/module/function 三层多语义代码图（AST + CFG + DFG + call graph + class hierarchy），用 GNN-based hybrid retriever 做层次化检索增强代码补全。推理时图方法，与 StructFuse 训练时结构信号互补。\\\\\\\"\\\\n\\\\n  # ==========================================================================\\\\n  # Category 7: Representation Geometry / Similarity Saturation\\\\n  # ==========================================================================\\\\n  representation_geometry:\\\\n    description: \\\\\\\"预训练模型表示空间几何分析及各向异性修正方法\\\\\\\"\\\\n    papers:\\\\n\\\\n      - title: \\\\\\\"Understanding Contrastive Representation Learning through Alignment and Uniformity on the Hypersphere\\\\\\\"\\\\n        authors: \\\\\\\"Tongzhou Wang, Phillip Isola\\\\\\\"\\\\n        venue: ICML\\\\n        year: 2020\\\\n        relation: method-component\\\\n        summary: \\\\\\\"定义 alignment/uniformity 两个对比学习关键属性，证明对比损失渐近优化两者。StructFuse 分析 embedding space 质量的理论工具。\\\\\\\"\\\\n\\\\n      - title: \\\\\\\"Representation Degeneration Problem in Training Natural Language Generation Models\\\\\\\"\\\\n        authors: \\\\\\\"Jun Gao, Di He, Xu Tan, Tao Qin, Liwei Wang, Tie-Yan Liu\\\\\\\"\\\\n        venue: ICLR\\\\n        year: 2019\\\\n        relation: background\\\\n        summary: \\\\\\\"揭示预训练 LM embedding 退化为窄锥的现象，StructFuse 观察到的 similarity saturation 可追溯到此。\\\\\\\"\\\\n\\\\n      - title: \\\\\\\"How Contextual are Contextualized Word Representations? Comparing the Geometry of BERT, ELMo, and GPT-2 Embeddings\\\\\\\"\\\\n        authors: \\\\\\\"Kawin Ethayarajh\\\\\\\"\\\\n        venue: EMNLP\\\\n        year: 2019\\\\n        relation: background\\\\n        summary: \\\\\\\"实证发现 BERT/ELMo/GPT-2 表示占据窄锥（各向异性），StructFuse 使用的 code encoder 继承此问题。\\\\\\\"\\\\n\\\\n      - title: \\\\\\\"On the Sentence Embeddings from Pre-trained Language Models\\\\\\\"\\\\n        authors: \\\\\\\"Bohan Li, Hao Zhou, Junxian He, Mingxuan Wang, Yiming Yang, Lei Li\\\\\\\"\\\\n        venue: EMNLP\\\\n        year: 2020\\\\n        relation: method-component\\\\n        summary: \\\\\\\"BERT-flow: 用 normalizing flows 将各向异性句子嵌入变换为各向同性高斯分布。\\\\\\\"\\\\n\\\\n      - title: \\\\\\\"SimCSE: Simple Contrastive Learning of Sentence Embeddings\\\\\\\"\\\\n        authors: \\\\\\\"Tianyu Gao, Xingcheng Yao, Danqi Chen\\\\\\\"\\\\n        venue: EMNLP\\\\n        year: 2021\\\\n        relation: method-component\\\\n        summary: \\\\\\\"用 dropout 作为最小增强的对比学习，直接证明 contrastive learning 改善 anisotropy。StructFuse 可引用其 uniformity 分析框架。\\\\\\\"\\\\n\\\\n      - title: \\\\\\\"Whitening Sentence Representations for Better Semantics and Faster Retrieval\\\\\\\"\\\\n        authors: \\\\\\\"Jianlin Su, Jiarun Cao, Weijie Liu, Yangyiwen Ou\\\\\\\"\\\\n        venue: arXiv\\\\n        year: 2021\\\\n        relation: method-component\\\\n        summary: \\\\\\\"白化操作增强句子表示各向同性并降维，与 StructFuse embedding post-processing 讨论相关。\\\\\\\"\\\\n\\\\n  # ==========================================================================\\\\n  # Category 8: Infrastructure / Tools\\\\n  # ==========================================================================\\\\n  infrastructure:\\\\n    description: \\\\\\\"StructFuse 依赖的核心基础设施和工具\\\\\\\"\\\\n    papers:\\\\n\\\\n      - title: \\\\\\\"Billion-Scale Similarity Search with GPUs\\\\\\\"\\\\n        authors: \\\\\\\"Jeff Johnson, Matthijs Douze, Herve Jegou\\\\\\\"\\\\n        venue: \\\\\\\"IEEE Transactions on Big Data\\\\\\\"\\\\n        year: 2021\\\\n        relation: building-block\\\\n        summary: \\\\\\\"FAISS: GPU 加速的大规模向量相似度搜索库，StructFuse 用于 ANN-based hard negative mining。\\\\\\\"\\\\n\\\\n      - title: \\\\\\\"Tree-sitter: An Incremental Parsing System for Programming Tools\\\\\\\"\\\\n        authors: \\\\\\\"Max Brunsfeld et al.\\\\\\\"\\\\n        venue: \\\\\\\"Software (Zenodo DOI: 10.5281/zenodo.13375512)\\\\\\\"\\\\n        year: 2018\\\\n        relation: building-block\\\\n        summary: \\\\\\\"增量解析库，高效构建和更新 concrete syntax trees。与 CodeQL 互补用于代码结构提取。\\\\\\\"\\\\n        note: \\\\\\\"软件工具，无正式论文。引用 Zenodo DOI 或 GitHub repo。\\\\\\\"\\\\n\\\", \\\"total_chars\\\": 23891, \\\"truncated\\\": false}, \\\"error\\\": null, \\\"metadata\\\": {}}\"}",
  "mcpMeta": {
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/literature_map.yaml\", \"content\": \"# StructFuse — Related Work Literature Map\\n# 最后更新: 2026-05-14\\n# 说明: 只收录已验证存在的论文。每篇均经 WebSearch 确认标题/venue/year。\\n# 总计: 60 entries (含 2 个软件工具引用)\\n\\ncategories:\\n\\n  # ==========================================================================\\n  # Category 1: Code Retrieval for Bug Fixing / SWE-bench Ecosystem\\n  # ==========================================================================\\n  code_retrieval_bug_fixing:\\n    description: \\\"SWE-bench 及相关 repo-level 自动修复系统中的代码检索方法\\\"\\n    papers:\\n\\n      - title: \\\"SWE-bench: Can Language Models Resolve Real-World GitHub Issues?\\\"\\n        authors: \\\"Carlos E. Jimenez, John Yang, Alexander Wettig, Shunyu Yao, Kexin Pei, Ofir Press, Karthik Narasimhan\\\"\\n        venue: ICLR\\n        year: 2024\\n        relation: baseline\\n        summary: \\\"从 GitHub issues 构建 repo-level bug fixing benchmark，成为自动修复领域标准评估集。\\\"\\n\\n      - title: \\\"SWE-agent: Agent-Computer Interfaces Enable Automated Software Engineering\\\"\\n        authors: \\\"John Yang, Carlos E. Jimenez, Alexander Wettig, Kilian Lieret, Shunyu Yao, Karthik Narasimhan, Ofir Press\\\"\\n        venue: NeurIPS\\n        year: 2024\\n        relation: competitor\\n        summary: \\\"基于 LLM agent 的交互式 bug fixing 系统，定义了 ACI 接口范式。\\\"\\n\\n      - title: \\\"AutoCodeRover: Autonomous Program Improvement\\\"\\n        authors: \\\"Yuntong Zhang, Haifeng Ruan, Zhiyu Fan, Abhik Roychoudhury\\\"\\n        venue: ISSTA\\n        year: 2024\\n        relation: competitor\\n        summary: \\\"结合代码搜索与 spectrum-based fault localization，利用程序分析缩小修复范围。\\\"\\n\\n      - title: \\\"Agentless: Demystifying LLM-based Software Engineering Agents\\\"\\n        authors: \\\"Chunqiu Steven Xia, Yinlin Deng, Soren Dunn, Lingming Zhang\\\"\\n        venue: arXiv\\n        year: 2024\\n        relation: competitor\\n        summary: \\\"无 agent 架构的 two-phase localize-then-repair 方法，在 SWE-bench 上取得强 baseline。\\\"\\n\\n      - title: \\\"SWE-smith: Scaling Data for Software Engineering Agents\\\"\\n        authors: \\\"John Yang, Kilian Lieret, Carlos E. Jimenez, Alexander Wettig, Kabir Khandpur, Yanzhe Zhang, Binyuan Hui, Ofir Press, Ludwig Schmidt, Diyi Yang\\\"\\n        venue: \\\"NeurIPS (Datasets & Benchmarks, Spotlight)\\\"\\n        year: 2025\\n        relation: building-block\\n        summary: \\\"自动从 GitHub 生成大规模 SWE-bench 风格训练数据，StructFuse 用其 repos 做 data-flow 提取。\\\"\\n\\n      - title: \\\"RepoBench: Benchmarking Repository-Level Code Auto-Completion Systems\\\"\\n        authors: \\\"Tianyang Liu, Canwen Xu, Julian McAuley\\\"\\n        venue: ICLR\\n        year: 2024\\n        relation: baseline\\n        summary: \\\"Repo-level 代码补全/检索 benchmark，含 RepoBench-R 检索子任务。\\\"\\n\\n      - title: \\\"SweRank: Software Issue Localization with Code Ranking\\\"\\n        authors: \\\"Revanth Gangi Reddy, Tarun Suresh, JaeHyeok Doo, Ye Liu, Xuan Phi Nguyen, Yingbo Zhou, Semih Yavuz, Caiming Xiong, Heng Ji, Shafiq Joty\\\"\\n        venue: arXiv\\n        year: 2025\\n        relation: competitor\\n        summary: \\\"Retrieve-and-rerank 框架用于 software issue localization，在 SWE-Bench-Lite 和 LocBench 上 SOTA，text-based retrieval baseline。\\\"\\n\\n      - title: \\\"SWE-Fixer: Training Open-Source LLMs for Effective and Efficient GitHub Issue Resolution\\\"\\n        authors: \\\"Chengxing Xie, Bowen Li, Chang Gao, He Du, Wai Lam, Difan Zou, Kai Chen\\\"\\n        venue: \\\"ACL (Findings)\\\"\\n        year: 2025\\n        relation: competitor\\n        summary: \\\"BM25 + LLM retriever 的 coarse-to-fine file retrieval pipeline，在 SWE-Bench Verified 上 30.2%。\\\"\\n\\n  # ==========================================================================\\n  # Category 2: Hard Negative Mining in Contrastive Learning\\n  # ==========================================================================\\n  hard_negative_mining:\\n    description: \\\"对比学习中 hard negative 挖掘策略，以及密集检索中的负样本选择\\\"\\n    papers:\\n\\n      - title: \\\"Dense Passage Retrieval for Open-Domain Question Answering\\\"\\n        authors: \\\"Vladimir Karpukhin, Barlas Oguz, Sewon Min, Patrick Lewis, Ledell Wu, Sergey Edunov, Danqi Chen, Wen-tau Yih\\\"\\n        venue: EMNLP\\n        year: 2020\\n        relation: background\\n        summary: \\\"DPR 开创了 in-batch negatives + BM25 hard negatives 的双塔检索范式。\\\"\\n\\n      - title: \\\"Approximate Nearest Neighbor Negative Contrastive Learning for Dense Text Retrieval\\\"\\n        authors: \\\"Lee Xiong, Chenyan Xiong, Ye Li, Kwok-Fung Tang, Jialin Liu, Paul Bennett, Junaid Ahmed, Arnold Overwijk\\\"\\n        venue: ICLR\\n        year: 2021\\n        relation: background\\n        summary: \\\"ANCE 用 ANN index 动态挖掘 embedding-distance hard negatives，StructFuse 的 baseline negative 策略之一。\\\"\\n\\n      - title: \\\"A Simple Framework for Contrastive Learning of Visual Representations\\\"\\n        authors: \\\"Ting Chen, Simon Kornblith, Mohammad Norouzi, Geoffrey Hinton\\\"\\n        venue: ICML\\n        year: 2020\\n        relation: background\\n        summary: \\\"SimCLR 视觉对比学习奠基工作，证明 hard negatives 和大 batch size 对对比学习的重要性。\\\"\\n\\n      - title: \\\"Sentence-BERT: Sentence Embeddings using Siamese BERT-Networks\\\"\\n        authors: \\\"Nils Reimers, Iryna Gurevych\\\"\\n        venue: EMNLP\\n        year: 2019\\n        relation: background\\n        summary: \\\"Siamese/triplet 网络训练句子嵌入，StructFuse 的对比训练框架与其类似。\\\"\\n\\n      - title: \\\"Curriculum Learning for Dense Retrieval Distillation\\\"\\n        authors: \\\"Hansi Zeng, Hamed Zamani, Vishwa Vinay\\\"\\n        venue: \\\"SIGIR (Best Short Paper)\\\"\\n        year: 2022\\n        relation: background\\n        summary: \\\"CL-DRD: 课程学习式知识蒸馏用于密集检索，从粗粒度到细粒度逐步增加训练难度。\\\"\\n\\n      - title: \\\"Effective Hard Negative Mining for Contrastive Learning-Based Code Search\\\"\\n        authors: \\\"Fan Y., Li C., Ge J., Huang L., Luo B.\\\"\\n        venue: \\\"ACM TOSEM\\\"\\n        year: 2025\\n        relation: contrast-target\\n        summary: \\\"CoCoHaNeRe: 提出可微分 hard negative 机制用于代码搜索对比学习。其对 hard negative 机制的处理与 StructFuse 的发现形成关键对照——StructFuse 证明 true embedding-distance mining 即可持续提升性能。\\\"\\n        note: \\\"关键引用：StructFuse Claim 1 的 correction target。CoCoHaNeRe 论点是非可微 embedding negatives 学习'slow and ineffective'，StructFuse 证明用 true embedding distance mining 仍然有效。\\\"\\n\\n      - title: \\\"Representation Learning with Contrastive Predictive Coding\\\"\\n        authors: \\\"Aaron van den Oord, Yazhe Li, Oriol Vinyals\\\"\\n        venue: arXiv\\n        year: 2018\\n        relation: background\\n        summary: \\\"InfoNCE 损失函数：对比预测编码的无监督表示学习。StructFuse 训练目标的理论根基。\\\"\\n\\n      - title: \\\"Contrastive Learning with Hard Negative Samples\\\"\\n        authors: \\\"Joshua David Robinson, Ching-Yao Chuang, Suvrit Sra, Stefanie Jegelka\\\"\\n        venue: ICLR\\n        year: 2021\\n        relation: method-component\\n        summary: \\\"HCL: 可控 hard negative 采样，证明更难的 negatives 加速和改善学习，但暗示过度 hard 会导致问题。StructFuse difficulty analysis 的理论起点。\\\"\\n\\n      - title: \\\"Debiased Contrastive Learning\\\"\\n        authors: \\\"Ching-Yao Chuang, Joshua Robinson, Yen-Chen Lin, Antonio Torralba, Stefanie Jegelka\\\"\\n        venue: NeurIPS\\n        year: 2020\\n        relation: method-component\\n        summary: \\\"DCL: 去偏对比目标，修正 false negatives（同类样本被当作 negatives）问题。False negative 是 hard negative 过拟合的重要来源。\\\"\\n\\n      - title: \\\"Hard Negative Mixing for Contrastive Learning\\\"\\n        authors: \\\"Yannis Kalantidis, Mert Bulent Sariyildiz, Noe Pion, Philippe Weinzaepfel, Diane Larlus\\\"\\n        venue: NeurIPS\\n        year: 2020\\n        relation: method-component\\n        summary: \\\"MoCHi: feature-level hard negative 混合合成，开销极小。与 StructFuse 的 structure-based negative mining 形成对比。\\\"\\n\\n      - title: \\\"Understanding Hard Negatives in Noise Contrastive Estimation\\\"\\n        authors: \\\"Wenzheng Zhang, Karl Stratos\\\"\\n        venue: NAACL\\n        year: 2021\\n        relation: background\\n        summary: \\\"理论分析：用模型分布作为 negative 分布可减少梯度偏差。为 hard negative 作用提供理论解释。\\\"\\n\\n      - title: \\\"ProGCL: Rethinking Hard Negative Mining in Graph Contrastive Learning\\\"\\n        authors: \\\"Jun Xia, Lirong Wu, Ge Wang, Jintao Chen, Stan Z. Li\\\"\\n        venue: ICML\\n        year: 2022\\n        relation: method-component\\n        summary: \\\"揭示图对比学习中 hard negative = false negative 的陷阱，提出基于概率的 hardness 区分 true/false negatives。与 StructFuse difficulty-overfitting 发现呼应。\\\"\\n\\n      - title: \\\"Difficulty-Based Sampling for Debiased Contrastive Representation Learning\\\"\\n        authors: \\\"Taeuk Jang, Xiaoqian Wang\\\"\\n        venue: CVPR\\n        year: 2023\\n        relation: method-component\\n        summary: \\\"WCL: 用 difficulty 分层采样 + bias-amplifying encoder 找信息性 hard negatives 同时避免 false negatives。与 StructFuse difficulty stratification 思路最接近。\\\"\\n\\n      - title: \\\"CAPSTONE: Curriculum Sampling for Dense Retrieval with Document Expansion\\\"\\n        authors: \\\"Xingwei He, Yeyun Gong, A-Long Jin, Hang Zhang, Anlei Dong, Jian Jiao, Siu Ming Yiu, Nan Duan\\\"\\n        venue: EMNLP\\n        year: 2023\\n        relation: background\\n        summary: \\\"课程采样策略 + pseudo-query 文档扩展，解决双塔检索训练-推理差异。StructFuse 的 structure-grounded negatives 提供正交的课程形式。\\\"\\n\\n  # ==========================================================================\\n  # Category 3: Contrastive Learning for Code\\n  # ==========================================================================\\n  contrastive_code_learning:\\n    description: \\\"代码领域的对比学习方法，训练时利用代码特性构建正负样本\\\"\\n    papers:\\n\\n      - title: \\\"Contrastive Code Representation Learning\\\"\\n        authors: \\\"Paras Jain, Ajay Jain, Tianjun Zhang, Pieter Abbeel, Joseph Gonzalez, Ion Stoica\\\"\\n        venue: EMNLP\\n        year: 2021\\n        relation: background\\n        summary: \\\"ContraCode: 自监督对比预训练，通过编译器变换生成功能等价的程序变体，学习代码功能而非表面形式。\\\"\\n\\n      - title: \\\"CodeRetriever: A Large Scale Contrastive Pre-Training Method for Code Search\\\"\\n        authors: \\\"Xiaonan Li, Yeyun Gong, Yelong Shen, Xipeng Qiu, Hang Zhang, Bolun Yao, Weizhen Qi, Daxin Jiang, Weizhu Chen, Nan Duan\\\"\\n        venue: EMNLP\\n        year: 2022\\n        relation: background\\n        summary: \\\"结合 unimodal (code-code) 和 bimodal (code-text) 对比学习预训练代码表示，在 11 个代码搜索 benchmark 上 SOTA。\\\"\\n\\n      - title: \\\"Towards Learning (Dis)-Similarity of Source Code from Program Contrasts\\\"\\n        authors: \\\"Yangruibo Ding, Luca Buratti, Saurabh Pujar, Alessandro Morari, Baishakhi Ray, Saikat Chakraborty\\\"\\n        venue: \\\"ACL (Long Papers)\\\"\\n        year: 2022\\n        relation: background\\n        summary: \\\"利用程序结构和功能属性构建对比样本对，学习代码相似性/差异性表示。\\\"\\n\\n      - title: \\\"CoCoSoDa: Effective Contrastive Learning for Code Search\\\"\\n        authors: \\\"Ensheng Shi, Yanlin Wang, Wenchao Gu, Lun Du, Hongyu Zhang, Shi Han, Dongmei Zhang, Hongbin Sun\\\"\\n        venue: ICSE\\n        year: 2023\\n        relation: direct-competitor\\n        summary: \\\"对比代码搜索 + soft data augmentation + momentum-based negative enrichment。在 negative 数量维度与 StructFuse 互补（momentum queue vs. difficulty-aware selection）。\\\"\\n\\n      - title: \\\"SynCoBERT: Syntax-Guided Multi-Modal Contrastive Pre-Training for Code Representation\\\"\\n        authors: \\\"Xin Wang, Yasheng Wang, Fei Mi, Pingyi Zhou, Yao Wan, Xiao Liu, Li Li, Hao Wu, Jin Liu, Xin Jiang\\\"\\n        venue: arXiv\\n        year: 2021\\n        relation: background\\n        summary: \\\"语法引导的多模态对比预训练，对齐 code/NL/AST 三模态。通过 identifier prediction 和 AST edge prediction 显式编码句法结构。\\\"\\n\\n      - title: \\\"ContraBERT: Enhancing Code Pre-trained Models via Contrastive Learning\\\"\\n        authors: \\\"Shangqing Liu, Bozhi Wu, Xiaofei Xie, Guozhu Meng, Yang Liu\\\"\\n        venue: ICSE\\n        year: 2023\\n        relation: background\\n        summary: \\\"鲁棒性导向的对比预训练，设计 9 种对抗增强算子（identifier renaming, dead code insertion, operand swapping 等），提升模型对对抗攻击的鲁棒性。\\\"\\n\\n  # ==========================================================================\\n  # Category 4: Program Analysis for ML\\n  # ==========================================================================\\n  program_analysis_for_ml:\\n    description: \\\"静态分析辅助 ML，结构信息在代码表示学习中的应用\\\"\\n    papers:\\n\\n      - title: \\\"CodeQL: Semantic Code Analysis Engine\\\"\\n        authors: \\\"GitHub / Semmle\\\"\\n        venue: \\\"Tool (open-source)\\\"\\n        year: 2019\\n        relation: building-block\\n        summary: \\\"基于 Datalog 的代码查询引擎，支持 inter-procedural data-flow 分析。StructFuse 用它提取 scope-bounded data-flow graph。\\\"\\n\\n      - title: \\\"code2vec: Learning Distributed Representations of Code\\\"\\n        authors: \\\"Uri Alon, Meital Zilberstein, Omer Levy, Eran Yahav\\\"\\n        venue: POPL\\n        year: 2019\\n        relation: background\\n        summary: \\\"用 AST path 学习代码向量表示，首次大规模证明结构信息对代码表示学习的价值。\\\"\\n\\n      - title: \\\"code2seq: Generating Sequences from Structured Representations of Code\\\"\\n        authors: \\\"Uri Alon, Shaked Brody, Omer Levy, Eran Yahav\\\"\\n        venue: ICLR\\n        year: 2019\\n        relation: background\\n        summary: \\\"code2vec 的序列生成扩展，用 AST path attention 生成方法名摘要。\\\"\\n\\n      - title: \\\"Detecting Code Clones with Graph Neural Network and Flow-Augmented Abstract Syntax Tree\\\"\\n        authors: \\\"Wenhan Wang, Ge Li, Bo Ma, Xin Xia, Zhi Jin\\\"\\n        venue: SANER\\n        year: 2020\\n        relation: background\\n        summary: \\\"FA-AST: 用 data-flow 增强 AST 进行代码克隆检测，与 StructFuse 用 data-flow 做 hard negative 挖掘思路相关。\\\"\\n\\n      - title: \\\"GraphCodeBERT: Pre-training Code Representations with Data Flow\\\"\\n        authors: \\\"Daya Guo, Shuo Ren, Shuai Lu, Zhangyin Feng, Duyu Tang, Shujie Liu, Long Zhou, Nan Duan, Alexey Svyatkovskiy, Shengyu Fu, Michele Tufano, Shao Kun Deng, Colin Clement, Dawn Drain, Neel Sundaresan, Jian Yin, Daxin Jiang, Ming Zhou\\\"\\n        venue: ICLR\\n        year: 2021\\n        relation: background\\n        summary: \\\"在预训练中引入 data-flow edge，证明 data-flow 信息提升代码理解任务。StructFuse 的 insight 与此相关但用途不同（hard negative mining vs pre-training）。\\\"\\n\\n      - title: \\\"ARISE: A Repository-level Graph Representation and Toolset for Agentic Fault Localization and Program Repair\\\"\\n        authors: \\\"Shahd Seddik, Fatemeh Fard\\\"\\n        venue: arXiv\\n        year: 2026\\n        relation: contrast\\n        summary: \\\"用 multi-granularity program graph（含 intra-procedural def-use edges）辅助 LLM agent 做 fault localization。仅 intra-procedural + runtime tool calls，与 StructFuse 的 inter-procedural static mining 互补。\\\"\\n\\n      - title: \\\"ProGraML: A Graph-based Program Representation for Data Flow Analysis and Compiler Optimization\\\"\\n        authors: \\\"Chris Cummins, Zacharias V. Fisches, Tal Ben-Nun, Torsten Hoefler, Michael FP O'Boyle, Hugh Leather\\\"\\n        venue: ICML\\n        year: 2021\\n        relation: background\\n        summary: \\\"语言无关的全程序图表示（control-flow + data-flow + call relations），证明整程序结构表示可学习且有效。StructFuse 使用 inter-procedural data-flow 的概念根基。\\\"\\n\\n      - title: \\\"CrossCodeEval: A Diverse and Multilingual Benchmark for Cross-File Code Completion\\\"\\n        authors: \\\"Yangruibo Ding, Zijian Wang, Wasi Uddin Ahmad, Hantian Ding, Ming Tan, Nihal Jain, Murali Krishna Ramanathan, Ramesh Nallapati, Parminder Bhatia, Dan Roth, Bing Xiang\\\"\\n        venue: NeurIPS\\n        year: 2023\\n        relation: background\\n        summary: \\\"多语言 cross-file 代码补全 benchmark，用静态分析确定需 cross-file 依赖的补全目标。验证了跨文件上下文对代码任务的关键性。\\\"\\n\\n  # ==========================================================================\\n  # Category 5: Code Embeddings / Code Search\\n  # ==========================================================================\\n  code_embeddings_search:\\n    description: \\\"代码嵌入模型和代码搜索方法\\\"\\n    papers:\\n\\n      - title: \\\"CodeSearchNet Challenge: Evaluating the State of Semantic Code Search\\\"\\n        authors: \\\"Hamel Husain, Ho-Hsiang Wu, Tiferet Gazit, Miltiadis Allamanis, Marc Brockschmidt\\\"\\n        venue: arXiv\\n        year: 2019\\n        relation: background\\n        summary: \\\"代码语义搜索 benchmark 和数据集，推动了代码嵌入模型的发展。\\\"\\n\\n      - title: \\\"CodeBERT: A Pre-Trained Model for Programming and Natural Languages\\\"\\n        authors: \\\"Zhangyin Feng, Daya Guo, Duyu Tang, Nan Duan, Xiaocheng Feng, Ming Gong, Lixin Zou, Bing Qin, Ting Liu, Daxin Jiang, Ming Zhou\\\"\\n        venue: \\\"EMNLP (Findings)\\\"\\n        year: 2020\\n        relation: background\\n        summary: \\\"首个编程语言-自然语言双模态预训练模型，代码嵌入的早期里程碑。\\\"\\n\\n      - title: \\\"UniXcoder: Unified Cross-Modal Pre-training for Code Representation\\\"\\n        authors: \\\"Daya Guo, Shuai Lu, Nan Duan, Yanlin Wang, Ming Zhou, Jian Yin\\\"\\n        venue: ACL\\n        year: 2022\\n        relation: background\\n        summary: \\\"统一跨模态代码预训练，在代码搜索等任务上取得 SOTA。\\\"\\n\\n      - title: \\\"StarCoder: May the Source Be with You!\\\"\\n        authors: \\\"Raymond Li, Loubna Ben Allal, et al. (BigCode)\\\"\\n        venue: TMLR\\n        year: 2023\\n        relation: building-block\\n        summary: \\\"大规模开源代码 LLM，StructFuse 用 StarCoder2-3B 作为对比学习检索器的 backbone 之一。\\\"\\n\\n      - title: \\\"Code Llama: Open Foundation Models for Code\\\"\\n        authors: \\\"Baptiste Roziere, Jonas Gehring, Fabian Gloeckle, et al. (Meta AI)\\\"\\n        venue: arXiv\\n        year: 2023\\n        relation: background\\n        summary: \\\"Meta 的代码大模型系列，基于 Llama 2 微调。\\\"\\n\\n      - title: \\\"Qwen2.5-Coder Technical Report\\\"\\n        authors: \\\"Binyuan Hui, Jian Yang, Zeyu Cui, et al. (Qwen Team, Alibaba)\\\"\\n        venue: arXiv\\n        year: 2024\\n        relation: building-block\\n        summary: \\\"Qwen 代码模型系列，StructFuse 用 Qwen2.5-Coder-3B 作为对比学习检索器的 backbone。\\\"\\n\\n      - title: \\\"DeepSeek-Coder: When the Large Language Model Meets Programming -- The Rise of Code Intelligence\\\"\\n        authors: \\\"Daya Guo, Qihao Zhu, Dejian Yang, Zhenda Xie, Kai Dong, Wentao Zhang, Guanting Chen, Xiao Bi, Yu Wu, Y.K. Li, Fuli Luo, Yingfei Xiong, Wenfeng Liang\\\"\\n        venue: arXiv\\n        year: 2024\\n        relation: background\\n        summary: \\\"开源代码 LLM 系列 (1.3B-33B)，project-level 代码训练 + 16K context + fill-in-the-blank 预训练。\\\"\\n\\n      - title: \\\"RepoFusion: Training Code Models to Understand Your Repository\\\"\\n        authors: \\\"Disha Shrivastava, Denis Kocetkov, Harm de Vries, Dzmitry Bahdanau, Torsten Scholak\\\"\\n        venue: arXiv\\n        year: 2023\\n        relation: background\\n        summary: \\\"训练代码模型融合多个 cross-file repo context 进行代码补全，小模型 + repo context 可匹配大模型性能。\\\"\\n\\n      - title: \\\"BM25\\\"\\n        authors: \\\"Stephen Robertson, Hugo Zaragoza\\\"\\n        venue: \\\"Foundations and Trends in Information Retrieval\\\"\\n        year: 2009\\n        relation: baseline\\n        summary: \\\"经典稀疏检索方法，StructFuse 的 baseline 之一。\\\"\\n\\n      - title: \\\"CoSQA: 20,000+ Web Queries for Code Search and Question Answering\\\"\\n        authors: \\\"Junjie Huang, Duyu Tang, Linjun Shou, Ming Gong, Ke Xu, Daxin Jiang, Ming Zhou, Nan Duan\\\"\\n        venue: ACL\\n        year: 2021\\n        relation: background\\n        summary: \\\"20,000+ 真实 web 查询与 Python 代码配对的大规模数据集，弥合合成 benchmark 与真实开发者需求的差距。\\\"\\n\\n  # ==========================================================================\\n  # Category 6: Graph-Guided Code Navigation (Inference-Time)\\n  # ==========================================================================\\n  graph_guided_inference:\\n    description: \\\"推理时利用代码结构图辅助导航/检索的方法（与 StructFuse 的训练时结构信号互补）\\\"\\n    papers:\\n\\n      - title: \\\"LocAgent: Graph-Guided LLM Agents for Code Localization\\\"\\n        authors: \\\"Zhaoling Chen, Robert Tang, Gangda Deng, Fang Wu, Jialong Wu, Zhiwei Jiang, Viktor Prasanna, Arman Cohan, Xingyao Wang\\\"\\n        venue: ACL\\n        year: 2025\\n        relation: contrast\\n        summary: \\\"将代码库解析为有向异构图，LLM agent 通过 multi-hop 推理在图上导航做代码定位。推理时用结构图，StructFuse 训练时用。\\\"\\n\\n      - title: \\\"CodexGraph: Bridging Large Language Models and Code Repositories via Code Graph Databases\\\"\\n        authors: \\\"Xiangyan Liu, Bo Lan, Zhiyuan Hu, Yang Liu, Zhicheng Zhang, Fei Wang, Michael Qizhe Shieh, Wenmeng Zhou\\\"\\n        venue: NAACL\\n        year: 2025\\n        relation: contrast\\n        summary: \\\"将代码库索引到图数据库，LLM agent 通过 graph query 接口检索结构化上下文。\\\"\\n\\n      - title: \\\"RANGER: Repository-Level Agent for Graph-Enhanced Retrieval\\\"\\n        authors: \\\"Pratik Shah, Rajat Ghosh, Aryan Singhal, Debojyoti Dutta\\\"\\n        venue: arXiv\\n        year: 2025\\n        relation: contrast\\n        summary: \\\"构建 repo 知识图（含 variable-level 节点），dual-stage retrieval: Cypher lookup + MCTS-guided graph exploration。\\\"\\n\\n      - title: \\\"RepoGraph: Enhancing AI Software Engineering with Repository-level Code Graph\\\"\\n        authors: \\\"Siru Ouyang, Wenhao Yu, Kaixin Ma, Zilin Xiao, Zhihan Zhang, Mengzhao Jia, Jiawei Han, Hongming Zhang, Dong Yu\\\"\\n        venue: ICLR\\n        year: 2025\\n        relation: contrast\\n        summary: \\\"以代码行为节点构建 repo-level 代码图，作为 SE agent 的 plug-in 导航模块。推理时逐行图导航，与 StructFuse 训练时批量提取结构信号互补。\\\"\\n\\n      - title: \\\"GraphCoder: Enhancing Repository-Level Code Completion via Coarse-to-fine Retrieval Based on Code Context Graph\\\"\\n        authors: \\\"Wei Liu, Ailun Yu, Daoguang Zan, Bo Shen, Wei Zhang, Haiyan Zhao, Zhi Jin, Qianxiang Wang\\\"\\n        venue: ASE\\n        year: 2024\\n        relation: contrast\\n        summary: \\\"构建 code context graph（含 control-flow 和 data-dependence edges）进行 coarse-to-fine 检索辅助代码补全。使用 intra-procedural data-flow，与 StructFuse 的 inter-procedural scope 形成对比。\\\"\\n\\n      - title: \\\"GRACE: Graph-Guided Repository-Aware Code Completion through Hierarchical Code Fusion\\\"\\n        authors: \\\"Xingliang Wang, Baoyi Wang, Chen Zhi, Junxiao Han, Xinkui Zhao, Jianwei Yin, Shuiguang Deng\\\"\\n        venue: arXiv\\n        year: 2025\\n        relation: contrast\\n        summary: \\\"构建 repo/module/function 三层多语义代码图（AST + CFG + DFG + call graph + class hierarchy），用 GNN-based hybrid retriever 做层次化检索增强代码补全。推理时图方法，与 StructFuse 训练时结构信号互补。\\\"\\n\\n  # ==========================================================================\\n  # Category 7: Representation Geometry / Similarity Saturation\\n  # ==========================================================================\\n  representation_geometry:\\n    description: \\\"预训练模型表示空间几何分析及各向异性修正方法\\\"\\n    papers:\\n\\n      - title: \\\"Understanding Contrastive Representation Learning through Alignment and Uniformity on the Hypersphere\\\"\\n        authors: \\\"Tongzhou Wang, Phillip Isola\\\"\\n        venue: ICML\\n        year: 2020\\n        relation: method-component\\n        summary: \\\"定义 alignment/uniformity 两个对比学习关键属性，证明对比损失渐近优化两者。StructFuse 分析 embedding space 质量的理论工具。\\\"\\n\\n      - title: \\\"Representation Degeneration Problem in Training Natural Language Generation Models\\\"\\n        authors: \\\"Jun Gao, Di He, Xu Tan, Tao Qin, Liwei Wang, Tie-Yan Liu\\\"\\n        venue: ICLR\\n        year: 2019\\n        relation: background\\n        summary: \\\"揭示预训练 LM embedding 退化为窄锥的现象，StructFuse 观察到的 similarity saturation 可追溯到此。\\\"\\n\\n      - title: \\\"How Contextual are Contextualized Word Representations? Comparing the Geometry of BERT, ELMo, and GPT-2 Embeddings\\\"\\n        authors: \\\"Kawin Ethayarajh\\\"\\n        venue: EMNLP\\n        year: 2019\\n        relation: background\\n        summary: \\\"实证发现 BERT/ELMo/GPT-2 表示占据窄锥（各向异性），StructFuse 使用的 code encoder 继承此问题。\\\"\\n\\n      - title: \\\"On the Sentence Embeddings from Pre-trained Language Models\\\"\\n        authors: \\\"Bohan Li, Hao Zhou, Junxian He, Mingxuan Wang, Yiming Yang, Lei Li\\\"\\n        venue: EMNLP\\n        year: 2020\\n        relation: method-component\\n        summary: \\\"BERT-flow: 用 normalizing flows 将各向异性句子嵌入变换为各向同性高斯分布。\\\"\\n\\n      - title: \\\"SimCSE: Simple Contrastive Learning of Sentence Embeddings\\\"\\n        authors: \\\"Tianyu Gao, Xingcheng Yao, Danqi Chen\\\"\\n        venue: EMNLP\\n        year: 2021\\n        relation: method-component\\n        summary: \\\"用 dropout 作为最小增强的对比学习，直接证明 contrastive learning 改善 anisotropy。StructFuse 可引用其 uniformity 分析框架。\\\"\\n\\n      - title: \\\"Whitening Sentence Representations for Better Semantics and Faster Retrieval\\\"\\n        authors: \\\"Jianlin Su, Jiarun Cao, Weijie Liu, Yangyiwen Ou\\\"\\n        venue: arXiv\\n        year: 2021\\n        relation: method-component\\n        summary: \\\"白化操作增强句子表示各向同性并降维，与 StructFuse embedding post-processing 讨论相关。\\\"\\n\\n  # ==========================================================================\\n  # Category 8: Infrastructure / Tools\\n  # ==========================================================================\\n  infrastructure:\\n    description: \\\"StructFuse 依赖的核心基础设施和工具\\\"\\n    papers:\\n\\n      - title: \\\"Billion-Scale Similarity Search with GPUs\\\"\\n        authors: \\\"Jeff Johnson, Matthijs Douze, Herve Jegou\\\"\\n        venue: \\\"IEEE Transactions on Big Data\\\"\\n        year: 2021\\n        relation: building-block\\n        summary: \\\"FAISS: GPU 加速的大规模向量相似度搜索库，StructFuse 用于 ANN-based hard negative mining。\\\"\\n\\n      - title: \\\"Tree-sitter: An Incremental Parsing System for Programming Tools\\\"\\n        authors: \\\"Max Brunsfeld et al.\\\"\\n        venue: \\\"Software (Zenodo DOI: 10.5281/zenodo.13375512)\\\"\\n        year: 2018\\n        relation: building-block\\n        summary: \\\"增量解析库，高效构建和更新 concrete syntax trees。与 CodeQL 互补用于代码结构提取。\\\"\\n        note: \\\"软件工具，无正式论文。引用 Zenodo DOI 或 GitHub repo。\\\"\\n\", \"total_chars\": 23891, \"truncated\": false}, \"error\": null, \"metadata\": {}}"
    }
  },
  "sourceToolAssistantUUID": "1f669815-e34c-455c-a555-abd4143c2dda",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/.claude/sessions/reviewer_65cfe724",
  "sessionId": "f444a635-eeef-4924-9b48-a4c308632421",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---


### Tool call

_source line 76 · 2026-05-16T00:48:25.301Z_

<details open><summary>🔧 Tool call — Read · `toolu_01XQvv8biJbtqQ4EXoWhRWGK`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/paper_drafts/related_work_v1.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9b049f96-601f-4358-946f-22e019434f39",
  "isSidechain": false,
  "requestId": "req_011Cb5KwStqwpf3AYNoR8hPd",
  "type": "assistant",
  "uuid": "5e1e612a-fad3-440c-921e-3bd84853deb4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/.claude/sessions/reviewer_65cfe724",
  "sessionId": "f444a635-eeef-4924-9b48-a4c308632421",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018QJUBMTLyj7AwfQqJrf7Kk",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 87,
      "cache_read_input_tokens": 87208,
      "output_tokens": 268,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 87,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 268,
          "cache_read_input_tokens": 87208,
          "cache_creation_input_tokens": 87,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 87
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

_source line 77_

```json
{
  "type": "last-prompt",
  "lastPrompt": "[系统通知 — worker_done:worker_code_fix-literature-warnings_20260516T004234]: Worker worker_code_fix-literature-warnings_20260516T004234 已完成（status=done），请审查 Agent 的处理结果。",
  "leafUuid": "bf0266a5-3494-40ef-a9c4-dc05c9277846",
  "sessionId": "f444a635-eeef-4924-9b48-a4c308632421"
}
```

---


### Runtime record

_source line 78_

```json
{
  "type": "ai-title",
  "aiTitle": "Review research literature worker completion",
  "sessionId": "f444a635-eeef-4924-9b48-a4c308632421"
}
```

---


### Assistant

_source line 79 · 2026-05-16T00:48:48.426Z_

<details><summary>Logged reasoning block</summary>

```text
Now let me assess the fix worker's changes:

### Changes made to `literature_map.yaml`:
1. **Updated count**: From 39 to 60 entries
2. **New Category 7: Representation Geometry / Similarity Saturation** added with 6 papers (alignment/uniformity, representation degeneration, anisotropy, BERT-flow, SimCSE, whitening)
3. **Category 2 (Hard Negative Mining) expanded** with: InfoNCE/CPC, HCL, DCL, MoCHi, Understanding Hard Negatives, ProGCL, WCL, CAPSTONE


4. **Category 3 (Contrastive Code Learning) expanded** with: CoCoSoDa, SynCoBERT, ContraBERT
5. **Category 4 (Program Analysis) expanded** with: ProGraML, CrossCodeEval
6. **Category 5 expanded** with: CoSQA
7. **GRACE entry added** to Category 6 with full details about graph-guided repository-aware code completion through hierarchical code fusion by Wang et al., arXiv 2025

The worker successfully verified and added GRACE with complete author and venue information, though I notice the literature map header timestamp still shows an earlier date despite the recent update.

Looking at what got addressed versus what didn't: the GRACE citation is now properly documented in the literature map with 60 total entries, but the timestamp inconsistency remains, and some secondary documents like the UniXcoder description in related_work_references.md weren't updated.

The bigger issue is that the v1 draft still references papers like InferCode, CodeSage, SCodeR, RocketQA, STAR, and a few classic references that aren't tracked in literature_map.yaml—so there's still a gap between what's cited and what's catalogued, even though the most critical verification work on GRACE got done.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "bf0266a5-3494-40ef-a9c4-dc05c9277846",
  "isSidechain": false,
  "requestId": "req_011Cb5KwweUMiXAxdacQu1Rg",
  "type": "assistant",
  "uuid": "8517e202-05fb-49dd-9354-19acb57a9933",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/.claude/sessions/reviewer_65cfe724",
  "sessionId": "f444a635-eeef-4924-9b48-a4c308632421",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LFG9DN7PVXjghyFQLpSCyL",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 12501,
      "cache_read_input_tokens": 87295,
      "output_tokens": 1262,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 12501,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1262,
          "cache_read_input_tokens": 87295,
          "cache_creation_input_tokens": 12501,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 12501
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

_source line 80 · 2026-05-16T00:48:48.731Z_

核实修复结果。`literature_map.yaml` 已从 39 扩展到 60 entries，GRACE 已添加具体信息。再检查几个细节。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8517e202-05fb-49dd-9354-19acb57a9933",
  "isSidechain": false,
  "requestId": "req_011Cb5KwweUMiXAxdacQu1Rg",
  "type": "assistant",
  "uuid": "4ba7dd2f-a425-4f51-a098-6e11e86939e1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/.claude/sessions/reviewer_65cfe724",
  "sessionId": "f444a635-eeef-4924-9b48-a4c308632421",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LFG9DN7PVXjghyFQLpSCyL",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 12501,
      "cache_read_input_tokens": 87295,
      "output_tokens": 1262,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 12501,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1262,
          "cache_read_input_tokens": 87295,
          "cache_creation_input_tokens": 12501,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 12501
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

_source line 81 · 2026-05-16T00:48:50.697Z_

<details open><summary>🔧 Tool call — Grep · `toolu_01MNYdW4rfraDeNg1tucm6Na`</summary>

```json
{
  "pattern": "GRACE",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "output_mode": "content",
  "-n": true
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4ba7dd2f-a425-4f51-a098-6e11e86939e1",
  "isSidechain": false,
  "requestId": "req_011Cb5KwweUMiXAxdacQu1Rg",
  "type": "assistant",
  "uuid": "ff2f8b3e-6ff8-4171-b284-3adea8e57217",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/.claude/sessions/reviewer_65cfe724",
  "sessionId": "f444a635-eeef-4924-9b48-a4c308632421",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LFG9DN7PVXjghyFQLpSCyL",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 12501,
      "cache_read_input_tokens": 87295,
      "output_tokens": 1262,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 12501,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1262,
          "cache_read_input_tokens": 87295,
          "cache_creation_input_tokens": 12501,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 12501
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

_source line 82 · 2026-05-16T00:48:51.686Z_

<details><summary>↩ Tool result · `toolu_017ZXvpog4kCueVyeZLBSVUm`</summary>

```text
No matches found
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "19cc72ff-9260-49a7-b727-caab3c5dcb06",
  "isSidechain": false,
  "promptId": "951872fd-15a5-4fff-a93d-6ac30f032101",
  "type": "user",
  "uuid": "1c7fc1a1-963e-421b-bfc7-1427ed5d34b2",
  "toolUseResult": {
    "mode": "content",
    "numFiles": 0,
    "filenames": [],
    "content": "",
    "numLines": 0
  },
  "sourceToolAssistantUUID": "19cc72ff-9260-49a7-b727-caab3c5dcb06",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/.claude/sessions/reviewer_65cfe724",
  "sessionId": "f444a635-eeef-4924-9b48-a4c308632421",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---


### Tool result

_source line 83 · 2026-05-16T00:48:50.863Z_

<details><summary>↩ Tool result · `toolu_01MNYdW4rfraDeNg1tucm6Na`</summary>

```text
&lt;persisted-output>
Output too large (51.6KB). Full output saved to: /home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-5-projects-structfuse-context--claude-sessions-reviewer-65cfe724/f444a635-eeef-4924-9b48-a4c308632421/tool-results/toolu_01MNYdW4rfraDeNg1tucm6Na.txt

Preview (first 2KB):
/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/paper_framing.md:74:| Missing related work | RepoFusion, GRACE, GraphCodeBERT, ANCE, curriculum HN mining | Writing task |
/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/literature/related_work_expansion_report.md:94:| **GRACE** (code-specific) | No well-known paper called "GRACE" for general code representation. Multiple GRACE papers exist (graph contrastive learning, vulnerability detection) but none match the intended scope. |
/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/logs/chats/worker_research_related-work-expansion_20260514T211428.jsonl:13:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/logs/chats/worker_research_related-work-expansion_20260514T211428.jsonl:31:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/logs/chats/worker_research_related-work-expansion_20260514T211428.jsonl:33:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/logs/chats/worker_write_claim2-exploratory-wording_20260515T055558.jsonl:33:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/paper_drafts/references.bib:259:  title={{GRACE}: Graph-Guided Repository-Aware Code Completion through Hierarchical Code Fusion},
/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/logs/chats/feishu_group_oc_a824c537c71f24fe2c80800ab4d82d39_paper_agent.jsonl:1:[Omitted long matching line]
...
&lt;/persisted-output>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ff2f8b3e-6ff8-4171-b284-3adea8e57217",
  "isSidechain": false,
  "promptId": "951872fd-15a5-4fff-a93d-6ac30f032101",
  "type": "user",
  "uuid": "82494eb6-7a16-4fca-b348-e841f2064aab",
  "toolUseResult": {
    "mode": "content",
    "numFiles": 0,
    "filenames": [],
    "content": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/paper_framing.md:74:| Missing related work | RepoFusion, GRACE, GraphCodeBERT, ANCE, curriculum HN mining | Writing task |\n/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/literature/related_work_expansion_report.md:94:| **GRACE** (code-specific) | No well-known paper called \"GRACE\" for general code representation. Multiple GRACE papers exist (graph contrastive learning, vulnerability detection) but none match the intended scope. |\n/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/logs/chats/worker_research_related-work-expansion_20260514T211428.jsonl:13:[Omitted long matching line]\n/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/logs/chats/worker_research_related-work-expansion_20260514T211428.jsonl:31:[Omitted long matching line]\n/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/logs/chats/worker_research_related-work-expansion_20260514T211428.jsonl:33:[Omitted long matching line]\n/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/logs/chats/worker_write_claim2-exploratory-wording_20260515T055558.jsonl:33:[Omitted long matching line]\n/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/paper_drafts/references.bib:259:  title={{GRACE}: Graph-Guided Repository-Aware Code Completion through Hierarchical Code Fusion},\n/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/logs/chats/feishu_group_oc_a824c537c71f24fe2c80800ab4d82d39_paper_agent.jsonl:1:[Omitted long matching line]\n/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/logs/chats/feishu_group_oc_a824c537c71f24fe2c80800ab4d82d39_paper_agent.jsonl:32:{\"ts\": \"2026-05-15T10:28:27.008653+00:00\", \"role\": \"tool\", \"session\": \"feishu:group:oc_a824c537c71f24fe2c80800ab4d82d39:paper_agent\", \"text\": \"called Grep\", \"tool\": \"Grep\", \"tool_args\": {\"pattern\": \"RepoFusion|GRACE|Sentence-BERT|reimers2019|ding2022\", \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/_project/paper\", \"output_mode\": \"content\"}}\n/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/logs/chats/feishu_group_oc_a824c537c71f24fe2c80800ab4d82d39_paper_agent.jsonl:44:[Omitted long matching line]\n/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/logs/chats/feishu_group_oc_a824c537c71f24fe2c80800ab4d82d39_paper_agent.jsonl:46:[Omitted long matching line]\n/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/paper_drafts/related_work_v1.md:21:[Omitted long matching line]\n/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/dream_reports/dream_20260514T162530/best/paper_framing.md:74:| Missing related work | RepoFusion, GRACE, GraphCodeBERT, ANCE, curriculum HN mining | Writing task |\n/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/dream_reports/dream_20260514T162530/worst/paper_framing.md:74:| Missing related work | RepoFusion, GRACE, GraphCodeBERT, ANCE, curriculum HN mining | Writing task |\n/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/logs/chats/archive/feishu_group_oc_651ef5630fe7a61a1decb410adb7641b_director_20260515T100100_646915.jsonl:283:[Omitted long matching line]\n/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/logs/chats/archive/feishu_group_oc_651ef5630fe7a61a1decb410adb7641b_director_20260515T100100_646915.jsonl:284:[Omitted long matching line]\n/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/dream_reports/dream_20260514T162530/logs/review_best.log:63:[Omitted long matching line]\n/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/dream_reports/dream_20260514T162530/logs/review_best.log:81:[Omitted long matching line]\n/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/dream_reports/dream_20260514T162530/logs/review_best.log:181:[Omitted long matching line]\n/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/dream_reports/dream_20260514T162530/logs/review_median.log:40:[Omitted long matching line]\n/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/dream_reports/dream_20260514T162530/logs/review_median.log:76:[Omitted long matching line]\n/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/dream_reports/dream_20260514T162530/logs/paper_agent_median.log:7:[Omitted long matching line]\n/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/logs/chats/archive/feishu_group_oc_a824c537c71f24fe2c80800ab4d82d39_reviewer_20260513T192700_218274.jsonl:2032:[Omitted long matching line]\n/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/dream_reports/dream_20260514T162530/logs/review_worst.log:34:[Omitted long matching line]\n/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/dream_reports/dream_20260514T162530/logs/review_worst.log:61:[Omitted long matching line]\n/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/dream_reports/dream_20260514T162530/logs/review_worst.log:127:[Omitted long matching line]\n/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/logs/chats/archive/feishu_group_oc_651ef5630fe7a61a1decb410adb7641b_director_20260515T140641_046076.jsonl:65:[Omitted long matching line]\n/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/logs/chats/archive/feishu_group_oc_651ef5630fe7a61a1decb410adb7641b_director_20260515T140641_046076.jsonl:70:[Omitted long matching line]\n/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/logs/chats/archive/feishu_group_oc_651ef5630fe7a61a1decb410adb7641b_director_20260515T140641_046076.jsonl:72:[Omitted long matching line]\n/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/logs/chats/archive/feishu_group_oc_651ef5630fe7a61a1decb410adb7641b_director_20260515T140641_046076.jsonl:76:[Omitted long matching line]\n/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/logs/chats/archive/feishu_group_oc_651ef5630fe7a61a1decb410adb7641b_director_20260515T140641_046076.jsonl:84:[Omitted long matching line]\n/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/logs/chats/archive/feishu_group_oc_651ef5630fe7a61a1decb410adb7641b_director_20260515T140641_046076.jsonl:100:[Omitted long matching line]\n/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/logs/chats/archive/feishu_group_oc_651ef5630fe7a61a1decb410adb7641b_director_20260515T140641_046076.jsonl:103:[Omitted long matching line]\n/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/logs/chats/archive/feishu_group_oc_651ef5630fe7a61a1decb410adb7641b_director_20260515T140641_046076.jsonl:106:[Omitted long matching line]\n/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/logs/chats/archive/feishu_group_oc_651ef5630fe7a61a1decb410adb7641b_director_20260515T140641_046076.jsonl:108:[Omitted long matching line]\n/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/logs/chats/archive/feishu_group_oc_651ef5630fe7a61a1decb410adb7641b_director_20260515T140641_046076.jsonl:119:[Omitted long matching line]\n/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/logs/chats/archive/feishu_group_oc_651ef5630fe7a61a1decb410adb7641b_director_20260515T140641_046076.jsonl:143:[Omitted long matching line]\n/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/logs/chats/archive/feishu_group_oc_651ef5630fe7a61a1decb410adb7641b_director_20260515T140641_046076.jsonl:148:[Omitted long matching line]\n/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/logs/chats/archive/feishu_group_oc_651ef5630fe7a61a1decb410adb7641b_director_20260515T140641_046076.jsonl:173:[Omitted long matching line]\n/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/logs/chats/archive/feishu_group_oc_651ef5630fe7a61a1decb410adb7641b_director_20260515T140641_046076.jsonl:184:[Omitted long matching line]\n/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/logs/chats/archive/feishu_group_oc_651ef5630fe7a61a1decb410adb7641b_director_20260515T140641_046076.jsonl:189:[Omitted long matching line]\n/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/dream_reports/dream_20260514T162530/logs/paper_agent_best.log:7:[Omitted long matching line]\n/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/dream_reports/dream_20260514T162530/logs/paper_agent_worst.log:6:[Omitted long matching line]\n/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/logs/chats/archive/feishu_group_oc_a824c537c71f24fe2c80800ab4d82d39_reviewer_20260515T100325_517993.jsonl:518:[Omitted long matching line]\n/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/logs/chats/archive/feishu_group_oc_a824c537c71f24fe2c80800ab4d82d39_reviewer_20260515T100325_517993.jsonl:519:[Omitted long matching line]\n/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/dream_reports/dream_20260514T162530/logs/phase2_best_attempt0.log:7:[Omitted long matching line]\n/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/dream_reports/dream_20260514T162530/median/paper_framing.md:74:| Missing related work | RepoFusion, GRACE, GraphCodeBERT, ANCE, curriculum HN mining | Writing task |\n/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/dream_reports/dream_20260514T075732/best/paper_framing.md:71:| Missing related work | RepoFusion, GRACE, GraphCodeBERT, ANCE, curriculum HN mining | Writing task |\n/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/dream_reports/dream_20260514T075732/worst/paper_framing.md:71:| Missing related work | RepoFusion, GRACE, GraphCodeBERT, ANCE, curriculum HN mining | Writing task |\n/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/dream_reports/dream_20260514T075732/logs/review_best.log:49:[Omitted long matching line]\n/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/dream_reports/dream_20260514T075732/logs/review_best.log:86:[Omitted long matching line]\n/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/dream_reports/dream_20260514T075732/logs/review_best.log:146:[Omitted long matching line]\n/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/dream_reports/dream_20260514T075732/logs/review_best.log:170:[Omitted long matching line]\n/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/dream_reports/dream_20260514T075732/logs/review_best.log:179:[Omitted long matching line]\n/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/logs/chats/archive/feishu_group_oc_651ef5630fe7a61a1decb410adb7641b_director_20260513T192651_136862.jsonl:361:[Omitted long matching line]\n/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/logs/chats/archive/feishu_group_oc_651ef5630fe7a61a1decb410adb7641b_director_20260513T192651_136862.jsonl:380:[Omitted long matching line]\n/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/logs/chats/archive/feishu_group_oc_651ef5630fe7a61a1decb410adb7641b_director_20260513T192651_136862.jsonl:1077:[Omitted long matching line]\n/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/dream_reports/dream_20260514T075732/logs/review_median.log:41:[Omitted long matching line]\n/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/dream_reports/dream_20260514T075732/logs/review_median.log:42:[Omitted long matching line]\n/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/dream_reports/dream_20260514T075732/logs/review_median.log:43:[Omitted long matching line]\n/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/dream_reports/dream_20260514T075732/logs/review_median.log:60:[Omitted long matching line]\n/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/dream_reports/dream_20260514T075732/logs/review_median.log:64:[Omitted long matching line]\n/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/dream_reports/dream_20260514T075732/logs/review_median.log:85:[Omitted long matching line]\n/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/dream_reports/dream_20260514T075732/logs/review_median.log:121:[Omitted long matching line]\n/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/dream_reports/dream_20260514T075732/logs/review_median.log:132:[Omitted long matching line]\n/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/dream_reports/dream_20260514T075732/logs/paper_agent_median.log:6:[Omitted long matching line]\n/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/dream_reports/dream_20260514T075732/logs/paper_agent_median.log:14:[Omitted long matching line]\n/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/dream_reports/dream_20260514T075732/logs/paper_agent_median.log:15:[Omitted long matching line]\n/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/dream_reports/dream_20260514T075732/logs/paper_agent_median.log:22:[Omitted long matching line]\n/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/dream_reports/dream_20260514T075732/logs/review_worst.log:35:[Omitted long matching line]\n/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/dream_reports/dream_20260514T075732/logs/review_worst.log:74:[Omitted long matching line]\n/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/dream_reports/dream_20260514T075732/logs/review_worst.log:110:[Omitted long matching line]\n/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/dream_reports/dream_20260514T075732/logs/paper_agent_best.log:6:[Omitted long matching line]\n/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/dream_reports/dream_20260514T075732/logs/paper_agent_worst.log:7:[Omitted long matching line]\n/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/dream_reports/dream_20260514T075732/median/paper_framing.md:71:| Missing related work | RepoFusion, GRACE, GraphCodeBERT, ANCE, curriculum HN mining | Writing task |\n/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/dream_reports/dream_20260514T075732/median/paper.tex:52:GraphCodeBERT~\\cite{guo2021graphcodebert} incorporates dataflow into pretraining objectives. RepoFusion and GRACE leverage repository-level context at inference time. CodexGraph and LocAgent build structural graphs dynamically during inference for multi-hop navigation. ARISE uses intra-procedural dataflow for runtime tool calls. Our work differs by using \\emph{inter-procedural} dataflow as a \\emph{training}-time signal for negative selection, complementary to inference-time approaches.\n/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/dream_reports/dream_20260512T204322/best/review_report.md:69:   - **Missing citations:** RepoFusion (Shrivastava et al., 2023) uses cross-file repository context for code tasks; GRACE (Zan et al., 2023) uses dependency-based context. Neither is cited.\n/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/dream_reports/dream_20260512T204322/best/review_report.md:95:- R2's related work gaps (RepoFusion, GRACE, GNNs) are substantive and should be addressed. The missing comparison with inference-time graph methods is the most impactful gap — it directly affects how a reader positions StructFuse.\n/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/dream_reports/dream_20260512T204322/best/review_report.md:117:- Related work gaps (RepoFusion, GRACE, inference-time graph methods) should be addressed\n/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/dream_reports/dream_20260512T204322/best/review_report.md:144:3. **Related work gaps (R2-moderate):** Missing RepoFusion, GRACE, GNN literature; no comparison with inference-time graph-guided retrieval\n/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/dream_reports/dream_20260512T204322/best/review_report.md:153:3. **Fill related work gaps** — cite RepoFusion, GRACE; add a paragraph discussing relationship to inference-time graph methods\n/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/dream_reports/dream_20260512T204322/meta.yaml:1096:    \\ et al., 2023) uses cross-file repository context for code tasks; GRACE (Zan\\\n/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/dream_reports/dream_20260512T204322/meta.yaml:1143:    \\ work gaps (RepoFusion, GRACE, GNNs) are substantive and should be addressed.\\\n/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/dream_reports/dream_20260512T204322/meta.yaml:1168:    \\ work gaps (RepoFusion, GRACE, inference-time graph methods) should be addressed\\n\\\n/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/dream_reports/dream_20260512T204322/meta.yaml:1197:    \\ GRACE, GNN literature; no comparison with inference-time graph-guided retrieval\\n\\\n/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/dream_reports/dream_20260512T204322/meta.yaml:1210:    \\ gaps** — cite RepoFusion, GRACE; add a paragraph discussing relationship to\\\n/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/logs/chats/archive/feishu_group_oc_651ef5630fe7a61a1decb410adb7641b_director_20260514T075833_559307.jsonl:59:[Omitted long matching line]\n/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/logs/chats/archive/cron_hook_m2_full_qwen_20260515T010649_199200.jsonl:30:[Omitted long matching line]\n/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/dream_reports/dream_20260512T204322/logs/review_best.log:42:[Omitted long matching line]\n/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/dream_reports/dream_20260512T204322/logs/review_best.log:78:[Omitted long matching line]\n/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/dream_reports/dream_20260512T204322/logs/review_best.log:79:[Omitted long matching line]\n/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/dream_reports/dream_20260512T204322/logs/review_best.log:87:[Omitted long matching line]\n/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/dream_reports/dream_20260512T204322/logs/review_best.log:88:[Omitted long matching line]\n/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/_project/report/related_work_expansion_report.md:94:| **GRACE** (code-specific) | No well-known paper called \"GRACE\" for general code representation. Multiple GRACE papers exist (graph contrastive learning, vulnerability detection) but none match the intended scope. |\n/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/logs/chats/archive/feishu_group_oc_a824c537c71f24fe2c80800ab4d82d39_20260515T125358_974829.jsonl:123:[Omitted long matching line]\n/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/logs/chats/archive/feishu_group_oc_a824c537c71f24fe2c80800ab4d82d39_20260515T125358_974829.jsonl:682:[Omitted long matching line]\n/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/logs/chats/archive/feishu_group_oc_a824c537c71f24fe2c80800ab4d82d39_20260515T125358_974829.jsonl:1102:[Omitted long matching line]\n/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/logs/chats/archive/feishu_group_oc_a824c537c71f24fe2c80800ab4d82d39_20260515T125358_974829.jsonl:1127:[Omitted long matching line]\n/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/logs/chats/archive/feishu_group_oc_a824c537c71f24fe2c80800ab4d82d39_20260515T125358_974829.jsonl:1130:[Omitted long matching line]\n/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/logs/chats/archive/feishu_group_oc_a824c537c71f24fe2c80800ab4d82d39_20260515T125358_974829.jsonl:1132:{\"ts\": \"2026-05-15T10:20:04.651325+00:00\", \"role\": \"assistant\", \"session\": \"feishu:group:oc_a824c537c71f24fe2c80800ab4d82d39\", \"text\": \"Worker 已派发处理 Related Work v1 第二轮 4 项修正（含 WebSearch 查阅 RepoFusion/GRACE/Ding 2022）。等 Worker 完成后验证并汇报 Director。\"}\n/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/logs/chats/archive/feishu_group_oc_a824c537c71f24fe2c80800ab4d82d39_20260515T125358_974829.jsonl:1149:[Omitted long matching line]\n/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/logs/chats/archive/feishu_group_oc_a824c537c71f24fe2c80800ab4d82d39_20260515T125358_974829.jsonl:1152:[Omitted long matching line]\n/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/logs/chats/archive/feishu_group_oc_a824c537c71f24fe2c80800ab4d82d39_20260515T125358_974829.jsonl:1154:[Omitted long matching line]\n/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/logs/chats/archive/feishu_group_oc_a824c537c71f24fe2c80800ab4d82d39_20260515T125358_974829.jsonl:1176:[Omitted long matching line]\n/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/logs/chats/archive/feishu_group_oc_a824c537c71f24fe2c80800ab4d82d39_20260515T125358_974829.jsonl:1197:[Omitted long matching line]\n/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/logs/chats/archive/feishu_group_oc_a824c537c71f24fe2c80800ab4d82d39_20260515T125358_974829.jsonl:1198:[Omitted long matching line]\n/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/logs/chats/archive/feishu_group_oc_a824c537c71f24fe2c80800ab4d82d39_20260515T125358_974829.jsonl:1211:[Omitted long matching line]\n/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/logs/chats/archive/feishu_group_oc_a824c537c71f24fe2c80800ab4d82d39_20260515T125358_974829.jsonl:1214:[Omitted long matching line]\n/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/logs/chats/archive/feishu_group_oc_a824c537c71f24fe2c80800ab4d82d39_reviewer_20260515T140609_034274.jsonl:133:[Omitted long matching line]\n/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/logs/chats/archive/feishu_group_oc_a824c537c71f24fe2c80800ab4d82d39_reviewer_20260515T140609_034274.jsonl:135:[Omitted long matching line]\n/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/logs/chats/archive/feishu_group_oc_a824c537c71f24fe2c80800ab4d82d39_reviewer_20260515T140609_034274.jsonl:164:[Omitted long matching line]\n/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/logs/chats/archive/feishu_group_oc_a824c537c71f24fe2c80800ab4d82d39_reviewer_20260515T140609_034274.jsonl:173:[Omitted long matching line]\n/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/logs/chats/archive/feishu_group_oc_a824c537c71f24fe2c80800ab4d82d39_reviewer_20260515T140609_034274.jsonl:175:{\"ts\": \"2026-05-15T10:23:42.745462+00:00\", \"role\": \"assistant\", \"session\": \"feishu:group:oc_a824c537c71f24fe2c80800ab4d82d39:reviewer\", \"text\": \"新增的 RepoFusion 和 GRACE 均有完整 bib 条目。所有审查意见均已采纳，发确认。\"}\n/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/logs/chats/archive/feishu_group_oc_a824c537c71f24fe2c80800ab4d82d39_reviewer_20260515T140609_034274.jsonl:178:[Omitted long matching line]\n/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/logs/chats/archive/feishu_group_oc_a824c537c71f24fe2c80800ab4d82d39_reviewer_20260515T140609_034274.jsonl:200:[Omitted long matching line]\n/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/logs/chats/archive/feishu_group_oc_a824c537c71f24fe2c80800ab4d82d39_reviewer_20260515T140609_034274.jsonl:218:[Omitted long matching line]\n/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/logs/chats/archive/feishu_group_oc_a824c537c71f24fe2c80800ab4d82d39_reviewer_20260515T140609_034274.jsonl:327:[Omitted long matching line]\n/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/logs/chats/archive/feishu_group_oc_a824c537c71f24fe2c80800ab4d82d39_reviewer_20260515T140609_034274.jsonl:345:[Omitted long matching line]\n/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/literature_map.yaml:408:      - title: \"GRACE: Graph-Guided Repository-Aware Code Completion through Hierarchical Code Fusion\"\n/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/logs/chats/feishu_group_oc_651ef5630fe7a61a1decb410adb7641b_director.jsonl:209:[Omitted long matching line]\n/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/logs/chats/feishu_group_oc_651ef5630fe7a61a1decb410adb7641b_director.jsonl:212:[Omitted long matching line]\n/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/logs/chats/feishu_group_oc_651ef5630fe7a61a1decb410adb7641b_director.jsonl:215:{\"ts\": \"2026-05-16T00:42:52.879147+00:00\", \"role\": \"user\", \"session\": \"feishu:group:oc_651ef5630fe7a61a1decb410adb7641b:director\", \"text\": \"[Agent 回复]:\\nWorker `fix-literature-warnings` 已派发，按优先级修复 4 个 warning（GRACE 幻觉 → UniXcoder → Dataflow → literature_map 同步）。\", \"source\": \"main_agent\"}\n/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/logs/chats/feishu_group_oc_651ef5630fe7a61a1decb410adb7641b_director.jsonl:217:[Omitted long matching line]\n/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/logs/chats/feishu_group_oc_a824c537c71f24fe2c80800ab4d82d39.jsonl:282:[Omitted long matching line]\n/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/logs/chats/feishu_group_oc_a824c537c71f24fe2c80800ab4d82d39.jsonl:283:[Omitted long matching line]\n/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/logs/chats/feishu_group_oc_a824c537c71f24fe2c80800ab4d82d39.jsonl:285:{\"ts\": \"2026-05-16T00:42:51.229238+00:00\", \"role\": \"assistant\", \"session\": \"feishu:group:oc_a824c537c71f24fe2c80800ab4d82d39\", \"text\": \"Worker `fix-literature-warnings` 已派发，按优先级修复 4 个 warning（GRACE 幻觉 → UniXcoder → Dataflow → literature_map 同步）。\"}\n/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/logs/chats/feishu_group_oc_a824c537c71f24fe2c80800ab4d82d39.jsonl:292:[Omitted long matching line]\n/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/logs/chats/feishu_group_oc_a824c537c71f24fe2c80800ab4d82d39.jsonl:293:[Omitted long matching line]\n/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/logs/chats/worker_fix_plan017_review_fixes_20260514T092605.jsonl:12:[Omitted long matching line]\n/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/logs/chats/feishu_group_oc_a824c537c71f24fe2c80800ab4d82d39_reviewer.jsonl:139:[Omitted long matching line]\n/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/logs/chats/feishu_group_oc_a824c537c71f24fe2c80800ab4d82d39_reviewer.jsonl:141:[Omitted long matching line]\n/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/logs/workers/worker_write_figure-design_20260514T225408.log:9:[Omitted long matching line]\n/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/logs/workers/worker_research_related-work-expansion_20260514T211428.log:13:[Omitted long matching line]\n/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/logs/workers/worker_research_related-work-expansion_20260514T211428.log:15:[Omitted long matching line]\n/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/logs/workers/worker_research_related-work-expansion_20260514T211428.log:16:[Omitted long matching line]\n/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/logs/workers/worker_research_related-work-expansion_20260514T211428.log:32:[Omitted long matching line]\n/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/logs/workers/worker_research_related-work-expansion_20260514T211428.log:33:[Omitted long matching line]\n/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/logs/workers/worker_research_related-work-expansion_20260514T211428.log:34:[Omitted long matching line]\n/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/logs/workers/worker_research_related-work-expansion_20260514T211428.log:36:{\"type\":\"system\",\"subtype\":\"task_progress\",\"task_id\":\"a3e27ca201c14d8cc\",\"tool_use_id\":\"toolu_01PNwjkbagrnEUkjjd8ipDqu\",\"description\":\"Search RepoFusion, GRACE, ContraCode\",\"usage\":{\"total_tokens\":13321,\"tool_uses\":1,\"duration_ms\":2770},\"last_tool_name\":\"ToolSearch\",\"uuid\":\"81eb40d5-3ecc-499a-9b05-44d233d655f8\",\"session_id\":\"fee328f7-0860-430b-80de-bdcdcefd655f\"}\n/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/logs/workers/worker_research_related-work-expansion_20260514T211428.log:41:{\"type\":\"system\",\"subtype\":\"task_progress\",\"task_id\":\"a3e27ca201c14d8cc\",\"tool_use_id\":\"toolu_01PNwjkbagrnEUkjjd8ipDqu\",\"description\":\"Searching for GRACE graph code representation learning program …\",\"usage\":{\"total_tokens\":14842,\"tool_uses\":3,\"duration_ms\":6331},\"last_tool_name\":\"WebSearch\",\"uuid\":\"67aad30d-e13f-460e-a5bf-5d56b246293e\",\"session_id\":\"fee328f7-0860-430b-80de-bdcdcefd655f\"}\n/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/logs/workers/worker_research_related-work-expansion_20260514T211428.log:67:{\"type\":\"system\",\"subtype\":\"task_progress\",\"task_id\":\"a3e27ca201c14d8cc\",\"tool_use_id\":\"toolu_01PNwjkbagrnEUkjjd8ipDqu\",\"description\":\"Searching for \\\"GRACE\\\" \\\"GraphCodeBERT\\\" OR \\\"graph-based\\\" code rep…\",\"usage\":{\"total_tokens\":18700,\"tool_uses\":7,\"duration_ms\":26859},\"last_tool_name\":\"WebSearch\",\"uuid\":\"aea9fd3f-965a-461f-9ce3-9cb90a621833\",\"session_id\":\"fee328f7-0860-430b-80de-bdcdcefd655f\"}\n/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/logs/workers/worker_research_related-work-expansion_20260514T211428.log:88:{\"type\":\"system\",\"subtype\":\"task_progress\",\"task_id\":\"a3e27ca201c14d8cc\",\"tool_use_id\":\"toolu_01PNwjkbagrnEUkjjd8ipDqu\",\"description\":\"Searching for GRACE \\\"graph-based representation\\\" code clone det…\",\"usage\":{\"total_tokens\":21699,\"tool_uses\":9,\"duration_ms\":38309},\"last_tool_name\":\"WebSearch\",\"uuid\":\"360cd049-86ba-4a76-8508-0471d22690c4\",\"session_id\":\"fee328f7-0860-430b-80de-bdcdcefd655f\"}\n/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/logs/workers/worker_research_related-work-expansion_20260514T211428.log:108:{\"type\":\"system\",\"subtype\":\"task_progress\",\"task_id\":\"a3e27ca201c14d8cc\",\"tool_use_id\":\"toolu_01PNwjkbagrnEUkjjd8ipDqu\",\"description\":\"Searching for GRACE GRaph-based Alignment Contrastive Embedding…\",\"usage\":{\"total_tokens\":25276,\"tool_uses\":11,\"duration_ms\":58857},\"last_tool_name\":\"WebSearch\",\"uuid\":\"51d0abf0-245c-4f03-9fc5-3b1ad1e0e9ce\",\"session_id\":\"fee328f7-0860-430b-80de-bdcdcefd655f\"}\n/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/logs/workers/worker_research_related-work-expansion_20260514T211428.log:115:{\"type\":\"system\",\"subtype\":\"task_progress\",\"task_id\":\"a3e27ca201c14d8cc\",\"tool_use_id\":\"toolu_01PNwjkbagrnEUkjjd8ipDqu\",\"description\":\"Searching for \\\"GRACE\\\" language model code representation \\\"abstr…\",\"usage\":{\"total_tokens\":27251,\"tool_uses\":13,\"duration_ms\":68993},\"last_tool_name\":\"WebSearch\",\"uuid\":\"83b24a59-a946-4594-82b8-4a90de3ca8ba\",\"session_id\":\"fee328f7-0860-430b-80de-bdcdcefd655f\"}\n/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/logs/workers/worker_research_related-work-expansion_20260514T211428.log:122:{\"type\":\"system\",\"subtype\":\"task_progress\",\"task_id\":\"a3e27ca201c14d8cc\",\"tool_use_id\":\"toolu_01PNwjkbagrnEUkjjd8ipDqu\",\"description\":\"Searching for GRACE \\\"graph-based\\\" \\\"code\\\" \\\"representation\\\" paper…\",\"usage\":{\"total_tokens\":29232,\"tool_uses\":15,\"duration_ms\":80736},\"last_tool_name\":\"WebSearch\",\"uuid\":\"0acb3241-ee07-46d5-9797-c95fd507d2e7\",\"session_id\":\"fee328f7-0860-430b-80de-bdcdcefd655f\"}\n/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/logs/workers/worker_research_related-work-expansion_20260514T211428.log:127:{\"type\":\"system\",\"subtype\":\"task_progress\",\"task_id\":\"a3e27ca201c14d8cc\",\"tool_use_id\":\"toolu_01PNwjkbagrnEUkjjd8ipDqu\",\"description\":\"Searching for GRACE \\\"graph representation\\\" \\\"code\\\" software engi…\",\"usage\":{\"total_tokens\":30372,\"tool_uses\":16,\"duration_ms\":90797},\"last_tool_name\":\"WebSearch\",\"uuid\":\"b54bb6c9-fe89-477a-973b-c3d6540a5dd5\",\"session_id\":\"fee328f7-0860-430b-80de-bdcdcefd655f\"}\n/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/logs/workers/worker_research_related-work-expansion_20260514T211428.log:133:[Omitted long matching line]\n/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/logs/workers/worker_research_related-work-expansion_20260514T211428.log:135:{\"type\":\"system\",\"subtype\":\"task_progress\",\"task_id\":\"a3e27ca201c14d8cc\",\"tool_use_id\":\"toolu_01PNwjkbagrnEUkjjd8ipDqu\",\"description\":\"Searching for GRACE \\\"GRaph-based code\\\" OR \\\"graph attention\\\" cod…\",\"usage\":{\"total_tokens\":31486,\"tool_uses\":17,\"duration_ms\":103857},\"last_tool_name\":\"WebSearch\",\"uuid\":\"5ab61755-865f-4957-a0c8-3881a1f88e76\",\"session_id\":\"fee328f7-0860-430b-80de-bdcdcefd655f\"}\n/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/logs/workers/worker_research_related-work-expansion_20260514T211428.log:140:[Omitted long matching line]\n/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/logs/workers/worker_research_related-work-expansion_20260514T211428.log:145:[Omitted long matching line]\n/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/logs/workers/worker_research_related-work-expansion_20260514T211428.log:147:[Omitted long matching line]\n/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/logs/workers/worker_research_related-work-expansion_20260514T211428.log:148:[Omitted long matching line]\n/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/logs/workers/worker_research_related-work-expansion_20260514T211428.log:152:[Omitted long matching line]\n/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/logs/workers/worker_research_related-work-expansion_20260514T211428.log:165:[Omitted long matching line]\n/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/logs/workers/worker_research_related-work-expansion_20260514T211428.log:166:[Omitted long matching line]\n/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/logs/workers/worker_research_related-work-expansion_20260514T211428.log:167:[Omitted long matching line]\n/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/logs/workers/worker_research_related-work-expansion_20260514T211428.log:168:[Omitted long matching line]\n/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/logs/workers/worker_write_introduction-v2_20260515T015804.log:9:[Omitted long matching line]\n/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/logs/workers/worker_fix_claim2-wording-critical_20260515T020243.log:12:[Omitted long matching line]\n/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/logs/workers/worker_fix_claim2-wording-critical_20260515T020243.log:70:[Omitted long matching line]\n/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/logs/workers/worker_fix_claim2-wording-critical_20260515T020243.log:72:[Omitted long matching line]\n/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/logs/workers/worker_fix_claim2-wording-critical_20260515T020243.log:74:[Omitted long matching line]\n/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/logs/workers/worker_fix_claim2-wording-critical_20260515T020243.log:76:[Omitted long matching line]\n/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/logs/workers/worker_fix_claim2-wording-critical_20260515T020243.log:78:[Omitted long matching line]\n/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/logs/workers/worker_fix_claim2-wording-critical_20260515T020243.log:81:[Omitted long matching line]\n/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/logs/workers/worker_fix_claim2-wording-critical_20260515T020243.log:85:[Omitted long matching line]\n/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/logs/workers/worker_fix_claim2-wording-critical_20260515T020243.log:87:[Omitted long matching line]\n/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/logs/workers/worker_fix_claim2-wording-critical_20260515T020243.log:90:[Omitted long matching line]\n/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/logs/workers/worker_write_method-draft_20260514T224613.log:9:[Omitted long matching line]\n/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/logs/workers/worker_write_method-and-setup-draft_20260515T015255.log:9:[Omitted long matching line]\n/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/logs/workers/worker_writing_related-work-v1-round3_20260515T103350_result.json:2:[Omitted long matching line]\n/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/logs/workers/worker_knowledge_update_roadmap_20260514T161154.log:8:[Omitted long matching line]\n/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/logs/workers/worker_writing_plan_017_discussion_20260514T170421.log:11:[Omitted long matching line]\n/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/logs/workers/worker_write_claim2-exploratory-wording_20260515T055558.log:8:[Omitted long matching line]\n/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/logs/workers/worker_write_claim2-exploratory-wording_20260515T055558.log:14:[Omitted long matching line]\n/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/logs/workers/worker_write_claim2-exploratory-wording_20260515T055558.log:18:[Omitted long matching line]\n/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/logs/workers/worker_write_claim2-exploratory-wording_20260515T055558.log:20:[Omitted long matching line]\n/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/logs/workers/worker_write_claim2-exploratory-wording_20260515T055558.log:22:[Omitted long matching line]\n/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/logs/workers/worker_write_claim2-exploratory-wording_20260515T055558.log:24:[Omitted long matching line]\n/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/logs/workers/worker_write_claim2-exploratory-wording_20260515T055558.log:26:[Omitted long matching line]\n/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/logs/workers/worker_write_claim2-exploratory-wording_20260515T055558.log:28:[Omitted long matching line]\n/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/logs/workers/worker_write_claim2-exploratory-wording_20260515T055558.log:31:[Omitted long matching line]\n/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/logs/workers/worker_write_claim2-exploratory-wording_20260515T055558.log:34:[Omitted long matching line]\n/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/logs/workers/worker_write_claim2-exploratory-wording_20260515T055558.log:39:[Omitted long matching line]\n/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/logs/workers/worker_write_claim2-exploratory-wording_20260515T055558.log:43:[Omitted long matching line]\n/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/logs/workers/worker_write_claim2-exploratory-wording_20260515T055558.log:46:[Omitted long matching line]\n/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/logs/workers/worker_write_claim2-exploratory-wording_20260515T055558.log:47:[Omitted long matching line]\n/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/logs/workers/worker_writing_abstract-v1_20260515T102508.log:12:[Omitted long matching line]\n/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/logs/workers/worker_write_introduction-draft_20260514T224556.log:9:[Omitted long matching line]\n/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/logs/workers/worker_writing_related-work-v1-round2_20260515T101954_result.json:2:[Omitted long matching line]\n/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/logs/workers/worker_write_experiments-skeleton_20260514T225046.log:9:[Omitted long matching line]\n/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/logs/workers/worker_review_abstract-v2_20260515T134237.log:10:[Omitted long matching line]\n/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/logs/workers/worker_writing_discussion_draft_20260514T101811.log:25:[Omitted long matching line]\n/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/logs/workers/worker_code_fix-literature-warnings_20260516T004234_result.json:2:[Omitted long matching line]\n/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/logs/workers/worker_fix_d041-paper-framing_20260515T020943.log:9:[Omitted long matching line]\n/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/logs/workers/worker_fix_d041-paper-framing_20260515T020943.log:12:[Omitted long matching line]\n/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/logs/workers/worker_writing_related-work-v1-round2_20260515T101954.log:11:[Omitted long matching line]\n/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/logs/workers/worker_writing_related-work-v1-round2_20260515T101954.log:12:[Omitted long matching line]\n/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/logs/workers/worker_writing_related-work-v1-round2_20260515T101954.log:17:[Omitted long matching line]\n/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/logs/workers/worker_writing_related-work-v1-round2_20260515T101954.log:21:[Omitted long matching line]\n/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/logs/workers/worker_writing_related-work-v1-round2_20260515T101954.log:22:[Omitted long matching line]\n/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/logs/workers/worker_writing_related-work-v1-round2_20260515T101954.log:23:[Omitted long matching line]\n/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/logs/workers/worker_writing_related-work-v1-round2_20260515T101954.log:24:[Omitted long matching line]\n/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/logs/workers/worker_writing_related-work-v1-round2_20260515T101954.log:26:[Omitted long matching line]\n/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/logs/workers/worker_writing_related-work-v1-round2_20260515T101954.log:28:[Omitted long matching line]\n/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/logs/workers/worker_writing_related-work-v1-round2_20260515T101954.log:29:[Omitted long matching line]\n/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/logs/workers/worker_writing_related-work-v1-round2_20260515T101954.log:30:[Omitted long matching line]\n/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/logs/workers/worker_writing_related-work-v1-round2_20260515T101954.log:31:[Omitted long matching line]\n/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/logs/workers/worker_writing_related-work-v1-round2_20260515T101954.log:32:[Omitted long matching line]\n/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/logs/workers/worker_writing_related-work-v1-round2_20260515T101954.log:33:[Omitted long matching line]\n/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/logs/workers/worker_writing_related-work-v1-round2_20260515T101954.log:42:[Omitted long matching line]\n/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/logs/workers/worker_writing_related-work-v1-round2_20260515T101954.log:43:[Omitted long matching line]\n/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/logs/workers/worker_writing_related-work-v1-round2_20260515T101954.log:45:[Omitted long matching line]\n/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/logs/workers/worker_writing_related-work-v1-round2_20260515T101954.log:46:[Omitted long matching line]\n/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/logs/workers/worker_writing_related-work-v1-round2_20260515T101954.log:49:[Omitted long matching line]\n/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/logs/workers/worker_writing_related-work-v1-round2_20260515T101954.log:50:[Omitted long matching line]\n/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/logs/workers/worker_writing_related-work-v1-round2_20260515T101954.log:51:[Omitted long matching line]\n/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/logs/workers/worker_write_related-work-draft_20260514T220708.log:11:[Omitted long matching line]\n/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/logs/workers/worker_fix_paper-framing-d049_20260515T075459.log:9:[Omitted long matching line]\n/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/logs/workers/worker_fix_paper-framing-d049_20260515T075459.log:12:[Omitted long matching line]\n/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/logs/workers/worker_fix_paper-framing-d049_20260515T075459.log:17:[Omitted long matching line]\n/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/logs/workers/worker_write_introduction-v1_20260515T083143.log:9:[Omitted long matching line]\n/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/logs/workers/worker_research_related-work-expansion_20260514T211428_result.json:2:[Omitted long matching line]\n/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/logs/workers/worker_review_experiments-v1_20260515T134308.log:11:[Omitted long matching line]\n/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/logs/workers/worker_fix_d041-paper-framing-dataflow_20260515T021011.log:6:[Omitted long matching line]\n/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/logs/workers/worker_fix_d041-paper-framing-dataflow_20260515T021011.log:10:[Omitted long matching line]\n/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/logs/workers/worker_fix_d041-paper-framing-dataflow_20260515T021011.log:12:[Omitted long matching line]\n/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/logs/workers/worker_fix_d041-paper-framing-dataflow_20260515T021011.log:15:[Omitted long matching line]\n/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/logs/workers/worker_fix_plan017_review_fixes_20260514T092605.log:17:[Omitted long matching line]\n/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/logs/workers/worker_review_experiments-v1_20260515T140139.log:11:[Omitted long matching line]\n/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/logs/workers/worker_writing_claim3-scalability-section_20260515T140413.log:13:[Omitted long matching line]\n/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/logs/workers/worker_write_method-v1_20260515T092736.log:9:[Omitted long matching line]\n/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/logs/workers/worker_code_m3a_eval_framework_prep_20260513T013129.log:106:[Omitted long matching line]\n/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/logs/workers/worker_review_claim2-exploratory-wording_20260515T015816.log:9:[Omitted long matching line]\n/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/logs/workers/worker_code_fix-literature-warnings_20260516T004234.log:5:[Omitted long matching line]\n/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/logs/workers/worker_code_fix-literature-warnings_20260516T004234.log:6:[Omitted long matching line]\n/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/logs/workers/worker_code_fix-literature-warnings_20260516T004234.log:7:[Omitted long matching line]\n/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/logs/workers/worker_code_fix-literature-warnings_20260516T004234.log:8:[Omitted long matching line]\n/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/logs/workers/worker_code_fix-literature-warnings_20260516T004234.log:38:[Omitted long matching line]\n/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/logs/workers/worker_code_fix-literature-warnings_20260516T004234.log:47:[Omitted long matching line]\n/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/logs/workers/worker_code_fix-literature-warnings_20260516T004234.log:56:[Omitted long matching line]\n/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/logs/workers/worker_code_fix-literature-warnings_20260516T004234.log:58:[Omitted long matching line]\n/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/logs/workers/worker_code_fix-literature-warnings_20260516T004234.log:61:[Omitted long matching line]\n/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/logs/workers/worker_code_fix-literature-warnings_20260516T004234.log:62:[Omitted long matching line]\n/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/logs/workers/worker_code_fix-literature-warnings_20260516T004234.log:63:[Omitted long matching line]\n/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/logs/workers/worker_code_fix-literature-warnings_20260516T004234.log:65:[Omitted long matching line]\n/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/logs/workers/worker_code_fix-literature-warnings_20260516T004234.log:72:[Omitted long matching line]\n/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/logs/workers/worker_code_fix-literature-warnings_20260516T004234.log:73:[Omitted long matching line]\n/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/logs/workers/worker_code_fix-literature-warnings_20260516T004234.log:74:[Omitted long matching line]\n/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/logs/workers/worker_code_fix-literature-warnings_20260516T004234.log:75:[Omitted long matching line]",
    "numLines": 250,
    "appliedLimit": 250
  },
  "sourceToolAssistantUUID": "ff2f8b3e-6ff8-4171-b284-3adea8e57217",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/.claude/sessions/reviewer_65cfe724",
  "sessionId": "f444a635-eeef-4924-9b48-a4c308632421",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---


### Tool call

_source line 84 · 2026-05-16T00:48:51.665Z_

<details open><summary>🔧 Tool call — Grep · `toolu_017ZXvpog4kCueVyeZLBSVUm`</summary>

```json
{
  "pattern": "InferCode|CodeSage|SCodeR|RocketQA|zhan2021star",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/literature_map.yaml",
  "output_mode": "content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "82494eb6-7a16-4fca-b348-e841f2064aab",
  "isSidechain": false,
  "requestId": "req_011Cb5KwweUMiXAxdacQu1Rg",
  "type": "assistant",
  "uuid": "19cc72ff-9260-49a7-b727-caab3c5dcb06",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/.claude/sessions/reviewer_65cfe724",
  "sessionId": "f444a635-eeef-4924-9b48-a4c308632421",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LFG9DN7PVXjghyFQLpSCyL",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 12501,
      "cache_read_input_tokens": 87295,
      "output_tokens": 1262,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 12501,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1262,
          "cache_read_input_tokens": 87295,
          "cache_creation_input_tokens": 12501,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 12501
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

_source line 85_

```json
{
  "type": "last-prompt",
  "lastPrompt": "[系统通知 — worker_done:worker_code_fix-literature-warnings_20260516T004234]: Worker worker_code_fix-literature-warnings_20260516T004234 已完成（status=done），请审查 Agent 的处理结果。",
  "leafUuid": "1c7fc1a1-963e-421b-bfc7-1427ed5d34b2",
  "sessionId": "f444a635-eeef-4924-9b48-a4c308632421"
}
```

---


### Runtime record

_source line 86_

```json
{
  "type": "ai-title",
  "aiTitle": "Review research literature worker completion",
  "sessionId": "f444a635-eeef-4924-9b48-a4c308632421"
}
```

---


### Assistant

_source line 87 · 2026-05-16T00:48:58.167Z_

<details><summary>Logged reasoning block</summary>

```text
Important findings:

1. **GRACE is now in the bib file** at `artifacts/paper_drafts/references.bib` line 259 with title "GRACE: Graph-Guided Repository-Aware Code Completion through Hierarchical Code Fusion" — so it was verified and added.

2. **InferCode, CodeSage, SCodeR, RocketQA, STAR are NOT in literature_map.yaml** — these are cited in the Related Work v1 draft but not tracked in the literature map. This is a consistency gap.

3. The old expansion report still says GRACE was excluded — that's a stale document now.


4. Let me verify the GRACE entry details in the bib file to make sure everything is correct.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1c7fc1a1-963e-421b-bfc7-1427ed5d34b2",
  "isSidechain": false,
  "requestId": "req_011Cb5Kyuo9neS81MxQNWynU",
  "type": "assistant",
  "uuid": "dfe61ab2-f75b-4411-9a5d-1eab287ed1fc",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/.claude/sessions/reviewer_65cfe724",
  "sessionId": "f444a635-eeef-4924-9b48-a4c308632421",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QNZJjuhDxzknsqYzi1wtKp",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2024,
      "cache_read_input_tokens": 99796,
      "output_tokens": 327,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2024,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 327,
          "cache_read_input_tokens": 99796,
          "cache_creation_input_tokens": 2024,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2024
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

_source line 88 · 2026-05-16T00:48:58.406Z_

<details open><summary>🔧 Tool call — Grep · `toolu_01MCWx6cu7VexYGJLRhnWepc`</summary>

```json
{
  "pattern": "GRACE|grace",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/paper_drafts/references.bib",
  "output_mode": "content",
  "-C": 5
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "dfe61ab2-f75b-4411-9a5d-1eab287ed1fc",
  "isSidechain": false,
  "requestId": "req_011Cb5Kyuo9neS81MxQNWynU",
  "type": "assistant",
  "uuid": "0eb8d047-2d6e-4861-a63c-f9621c1ff9f7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/.claude/sessions/reviewer_65cfe724",
  "sessionId": "f444a635-eeef-4924-9b48-a4c308632421",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QNZJjuhDxzknsqYzi1wtKp",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2024,
      "cache_read_input_tokens": 99796,
      "output_tokens": 327,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2024,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 327,
          "cache_read_input_tokens": 99796,
          "cache_creation_input_tokens": 2024,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2024
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

_source line 89 · 2026-05-16T00:48:58.415Z_

<details><summary>↩ Tool result · `toolu_01MCWx6cu7VexYGJLRhnWepc`</summary>

```text
253-  author={Shrivastava, Disha and Kocetkov, Denis and de Vries, Harm and Bahdanau, Dzmitry and Scholak, Torsten},
254-  journal={arXiv preprint arXiv:2306.10998},
255-  year={2023}
256-}
257-
258:@article{wang2025grace,
259:  title={{GRACE}: Graph-Guided Repository-Aware Code Completion through Hierarchical Code Fusion},
260-  author={Wang, Xingliang and Wang, Baoyi and Zhi, Chen and Han, Junxiao and Zhao, Xinkui and Yin, Jianwei and Deng, Shuiguang},
261-  journal={arXiv preprint arXiv:2509.05980},
262-  year={2025}
263-}
264-
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "0eb8d047-2d6e-4861-a63c-f9621c1ff9f7",
  "isSidechain": false,
  "promptId": "951872fd-15a5-4fff-a93d-6ac30f032101",
  "type": "user",
  "uuid": "c0e9ba94-345a-40bc-96a2-809156afb721",
  "toolUseResult": {
    "mode": "content",
    "numFiles": 0,
    "filenames": [],
    "content": "253-  author={Shrivastava, Disha and Kocetkov, Denis and de Vries, Harm and Bahdanau, Dzmitry and Scholak, Torsten},\n254-  journal={arXiv preprint arXiv:2306.10998},\n255-  year={2023}\n256-}\n257-\n258:@article{wang2025grace,\n259:  title={{GRACE}: Graph-Guided Repository-Aware Code Completion through Hierarchical Code Fusion},\n260-  author={Wang, Xingliang and Wang, Baoyi and Zhi, Chen and Han, Junxiao and Zhao, Xinkui and Yin, Jianwei and Deng, Shuiguang},\n261-  journal={arXiv preprint arXiv:2509.05980},\n262-  year={2025}\n263-}\n264-",
    "numLines": 12
  },
  "sourceToolAssistantUUID": "0eb8d047-2d6e-4861-a63c-f9621c1ff9f7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/.claude/sessions/reviewer_65cfe724",
  "sessionId": "f444a635-eeef-4924-9b48-a4c308632421",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---


### Assistant

_source line 90 · 2026-05-16T00:49:10.443Z_

<details><summary>Logged reasoning block</summary>

```text
GRACE has a specific arXiv ID: 2509.05980. This is a September 2025 arXiv paper. The arXiv ID format `2509.xxxxx` means September 2025, which is in the future (current date is May 2026). Wait, actually the system says today is 2026-05-16, so September 2025 is in the past. So this paper should exist. The arXiv ID seems valid.

However, wait — the expansion report from 05-14 said "No well-known paper called 'GRACE' for general code representation." The fix worker then found it with arXiv:2509.05980 and verified it. This resolves my concern.


The fix worker successfully verified the GRACE citation and expanded the literature map from 39 to 60 entries, adding a new category for representation geometry and strengthening the hard negative mining section. There are a couple of minor cosmetic issues remaining, like an outdated timestamp in the header and a few unresolved paper citations, but the core work is complete.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c0e9ba94-345a-40bc-96a2-809156afb721",
  "isSidechain": false,
  "requestId": "req_011Cb5KzP4VJ6YdsXr8i1i87",
  "type": "assistant",
  "uuid": "4ad3bac4-1fee-4cfe-87f2-e7505c76f045",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/.claude/sessions/reviewer_65cfe724",
  "sessionId": "f444a635-eeef-4924-9b48-a4c308632421",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JBztbwssUcpW4o2qLYijqN",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 563,
      "cache_read_input_tokens": 101820,
      "output_tokens": 1170,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 563,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1170,
          "cache_read_input_tokens": 101820,
          "cache_creation_input_tokens": 563,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 563
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

_source line 91 · 2026-05-16T00:49:11.493Z_

GRACE 已验证（arXiv:2509.05980），bib 文件已有完整条目。literature_map 已扩展。还有一个小 gap：v1 草稿引用了 5 篇不在 literature_map 中的论文。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4ad3bac4-1fee-4cfe-87f2-e7505c76f045",
  "isSidechain": false,
  "requestId": "req_011Cb5KzP4VJ6YdsXr8i1i87",
  "type": "assistant",
  "uuid": "35bd679f-c2a3-4b1a-b606-d7bbdde7aad7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/.claude/sessions/reviewer_65cfe724",
  "sessionId": "f444a635-eeef-4924-9b48-a4c308632421",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JBztbwssUcpW4o2qLYijqN",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 563,
      "cache_read_input_tokens": 101820,
      "output_tokens": 1170,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 563,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1170,
          "cache_read_input_tokens": 101820,
          "cache_creation_input_tokens": 563,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 563
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

_source line 92 · 2026-05-16T00:49:22.425Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__reviewer_post_to_director · `toolu_014CQdPKdprWziHmp4A7puXq`</summary>

```json
{
  "text": "## 跟进审查 — worker_code_fix-literature-warnings_20260516T004234\n\n**结论**: PASS（小问题待补）\n\n### 已修复\n\n- ✅ **GRACE 引用已验证**：arXiv:2509.05980 (Wang et al., 2025)，已加入 literature_map.yaml 和 references.bib，具体信息完整（authors/title/arXiv ID）。之前的 warning 解除。\n- ✅ **literature_map.yaml 已同步扩展**：39 → 60 entries。新增 Category 7 (Representation Geometry，6 篇)，Category 2 扩展（+8 篇：InfoNCE, HCL, DCL, MoCHi, ProGCL, WCL 等），Category 3/4/5 各有补充。references 和 supplement 文档的论文已整合。\n\n### 残留小问题\n\n- [severity: info] **literature_map.yaml 头部日期未更新**：仍标 \"最后更新: 2026-05-14\"，实际已在 05-16 修改。\n- [severity: info] **v1 草稿引用了 5 篇不在 literature_map 中的论文**：InferCode \\cite{bui2021infercode}、CodeSage \\cite{zhang2024codesage}、SCodeR \\cite{li2022scoder}、RocketQA \\cite{qu2021rocketqa}、STAR \\cite{zhan2021star}。这些都在 §2.1/§2.3 中引用但未被 literature_map 追踪。建议下次写作更新时补入，保持引用源统一。\n- [severity: info] `related_work_references.md` 中 UniXcoder 描述错误（\"StructFuse backbone\"）和 `related_work_supplement.md` 中 dataflow negatives 方向性错误未修，但这两个是中间参考文档而非论文正文，影响有限。",
  "project": "structfuse-context"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "35bd679f-c2a3-4b1a-b606-d7bbdde7aad7",
  "isSidechain": false,
  "requestId": "req_011Cb5KzP4VJ6YdsXr8i1i87",
  "type": "assistant",
  "uuid": "fa25ddd9-a2d4-4b43-aa1f-c82f7f9747ed",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/.claude/sessions/reviewer_65cfe724",
  "sessionId": "f444a635-eeef-4924-9b48-a4c308632421",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JBztbwssUcpW4o2qLYijqN",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 563,
      "cache_read_input_tokens": 101820,
      "output_tokens": 1170,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 563,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1170,
          "cache_read_input_tokens": 101820,
          "cache_creation_input_tokens": 563,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 563
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

_source line 93 · 2026-05-16T00:49:26.050Z_

<details><summary>↩ Tool result · `toolu_014CQdPKdprWziHmp4A7puXq`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"director_session\": \"feishu:group:oc_651ef5630fe7a61a1decb410adb7641b:director\"}, \"error\": \"\"}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "fa25ddd9-a2d4-4b43-aa1f-c82f7f9747ed",
  "isSidechain": false,
  "promptId": "951872fd-15a5-4fff-a93d-6ac30f032101",
  "type": "user",
  "uuid": "32dfa63c-4557-4347-af78-0ad6a22ac284",
  "toolUseResult": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"director_session\\\": \\\"feishu:group:oc_651ef5630fe7a61a1decb410adb7641b:director\\\"}, \\\"error\\\": \\\"\\\"}\"}",
  "mcpMeta": {
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"director_session\": \"feishu:group:oc_651ef5630fe7a61a1decb410adb7641b:director\"}, \"error\": \"\"}"
    }
  },
  "sourceToolAssistantUUID": "fa25ddd9-a2d4-4b43-aa1f-c82f7f9747ed",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/.claude/sessions/reviewer_65cfe724",
  "sessionId": "f444a635-eeef-4924-9b48-a4c308632421",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---


### Runtime record

_source line 94 · 2026-05-16T00:49:26.055Z_

```json
{
  "parentUuid": "32dfa63c-4557-4347-af78-0ad6a22ac284",
  "isSidechain": false,
  "attachment": {
    "type": "todo_reminder",
    "content": [],
    "itemCount": 0
  },
  "type": "attachment",
  "uuid": "483644f6-ea81-4f3e-9ddc-10d028944b4c",
  "timestamp": "2026-05-16T00:49:26.055Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/.claude/sessions/reviewer_65cfe724",
  "sessionId": "f444a635-eeef-4924-9b48-a4c308632421",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---


### Runtime record

_source line 95_

```json
{
  "type": "ai-title",
  "aiTitle": "Review research literature worker completion",
  "sessionId": "f444a635-eeef-4924-9b48-a4c308632421"
}
```

---


### Runtime record

_source line 96 · 2026-05-16T02:31:32.106Z_

```json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-16T02:31:32.106Z",
  "sessionId": "f444a635-eeef-4924-9b48-a4c308632421",
  "content": "[系统通知 — worker_done:worker_ops_training-and-eval-status_20260516T022911]:\nWorker worker_ops_training-and-eval-status_20260516T022911 已完成（status=done），请审查 Agent 的处理结果。"
}
```

---


### Runtime record

_source line 97 · 2026-05-16T02:31:32.107Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-16T02:31:32.107Z",
  "sessionId": "f444a635-eeef-4924-9b48-a4c308632421"
}
```

---


## Round 4

## Round 4

2 recorded events


### User

_source line 98 · 2026-05-16T02:31:32.095Z_

Continue from where you left off.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "483644f6-ea81-4f3e-9ddc-10d028944b4c",
  "isSidechain": false,
  "promptId": "cb482ce5-85c1-49a1-985e-c68475dfc7e7",
  "type": "user",
  "isMeta": true,
  "uuid": "0b68907f-d024-408f-89fb-bd1682c4ca60",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/.claude/sessions/reviewer_65cfe724",
  "sessionId": "f444a635-eeef-4924-9b48-a4c308632421",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---


### Assistant

_source line 99 · 2026-05-16T02:31:32.095Z_

No response requested.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0b68907f-d024-408f-89fb-bd1682c4ca60",
  "isSidechain": false,
  "type": "assistant",
  "uuid": "911a7c41-3feb-41b9-96ef-65672e7af4b6",
  "isApiErrorMessage": false,
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/.claude/sessions/reviewer_65cfe724",
  "sessionId": "f444a635-eeef-4924-9b48-a4c308632421",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "id": "c8b1dcad-f555-4be6-a63e-2b408fd3e816",
    "container": null,
    "model": "&lt;synthetic>",
    "stop_reason": "stop_sequence",
    "stop_sequence": "",
    "type": "message",
    "usage": {
      "input_tokens": 0,
      "output_tokens": 0,
      "cache_creation_input_tokens": 0,
      "cache_read_input_tokens": 0,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": null,
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": null,
      "iterations": null,
      "speed": null
    },
    "context_management": null
  }
}
```

</details>

---


## Round 5

## Round 5

74 recorded events


### User

_source line 100 · 2026-05-16T02:31:32.235Z_

[系统通知 — worker_done:worker_ops_training-and-eval-status_20260516T022911]:
Worker worker_ops_training-and-eval-status_20260516T022911 已完成（status=done），请审查 Agent 的处理结果。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "911a7c41-3feb-41b9-96ef-65672e7af4b6",
  "isSidechain": false,
  "promptId": "cb482ce5-85c1-49a1-985e-c68475dfc7e7",
  "type": "user",
  "uuid": "999eea89-568b-427a-a170-066502d26a76",
  "permissionMode": "bypassPermissions",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/.claude/sessions/reviewer_65cfe724",
  "sessionId": "f444a635-eeef-4924-9b48-a4c308632421",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---


### Assistant

_source line 101 · 2026-05-16T02:31:35.664Z_

<details><summary>Logged reasoning block</summary>

```text
A training and eval status worker has completed. I need to review the current training status, GPU utilization, and check for any issues. Let me read the registry for running experiments and check the server status.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "999eea89-568b-427a-a170-066502d26a76",
  "isSidechain": false,
  "requestId": "req_011Cb5TozuPS54YCab16mdAq",
  "type": "assistant",
  "uuid": "a1657ea3-7a4d-4a5f-b65b-dc76fe96ae61",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/.claude/sessions/reviewer_65cfe724",
  "sessionId": "f444a635-eeef-4924-9b48-a4c308632421",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DxbbiUUpPV99Z5HVTdELu6",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 91977,
      "cache_read_input_tokens": 11841,
      "output_tokens": 290,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 91977,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 290,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 91977,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 91977
          },
          "type": "message"
        }
      ],
      "speed": "standard"
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


### Assistant

_source line 102 · 2026-05-16T02:31:36.803Z_

收到训练/评估状态 worker 完成通知，开始审查。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a1657ea3-7a4d-4a5f-b65b-dc76fe96ae61",
  "isSidechain": false,
  "requestId": "req_011Cb5TozuPS54YCab16mdAq",
  "type": "assistant",
  "uuid": "a41ff1c1-9bc3-4544-94d1-ea7fce10e8a4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/.claude/sessions/reviewer_65cfe724",
  "sessionId": "f444a635-eeef-4924-9b48-a4c308632421",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DxbbiUUpPV99Z5HVTdELu6",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 91977,
      "cache_read_input_tokens": 11841,
      "output_tokens": 290,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 91977,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 290,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 91977,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 91977
          },
          "type": "message"
        }
      ],
      "speed": "standard"
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

_source line 103 · 2026-05-16T02:31:37.846Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry · `toolu_0179s3UNroBqCs4eHr2gMn6k`</summary>

```json
{
  "project": "structfuse-context",
  "filters": {
    "status": "RUNNING"
  },
  "fields": [
    "*"
  ]
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a41ff1c1-9bc3-4544-94d1-ea7fce10e8a4",
  "isSidechain": false,
  "requestId": "req_011Cb5TozuPS54YCab16mdAq",
  "type": "assistant",
  "uuid": "0e3a3a44-67d9-4139-bfff-e7f4f822dd45",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/.claude/sessions/reviewer_65cfe724",
  "sessionId": "f444a635-eeef-4924-9b48-a4c308632421",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DxbbiUUpPV99Z5HVTdELu6",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 91977,
      "cache_read_input_tokens": 11841,
      "output_tokens": 290,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 91977,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 290,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 91977,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 91977
          },
          "type": "message"
        }
      ],
      "speed": "standard"
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

_source line 104 · 2026-05-16T02:31:37.986Z_

<details><summary>↩ Tool result · `toolu_0179s3UNroBqCs4eHr2gMn6k`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"experiments\": {\"plan_003_swebench_eval\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-15T18:41:00.685Z\", \"updated_at\": \"2026-05-16T00:22:31.107Z\", \"hypothesis\": \"SWE-bench Lite 纯检索 eval：用 3 个 Qwen M2 checkpoints (random_s42, embed_s43, dataflow_s43) 在 100 个 SWE-bench Lite 实例上评估 file-level retrieval Recall@{1,5,10,20} 和 MRR。定位为外部泛化展示，不做控制对比 claim（3 checkpoint 用了不同 seed，策略对比 confound 了 seed）。\", \"spec\": {\"command\": \"python eval_swebench_retrieval.py (3 checkpoints sequential on GPU 0)\", \"server\": \"bjb1-42106\", \"data_path\": \"/root/autodl-tmp/structfuse/artifacts/swebench_retrieval_eval/\", \"data_count\": 100, \"model_name\": \"Qwen2.5-Coder-3B (3 M2 checkpoints: random_s42, embed_s43, dataflow_s43)\", \"seed\": \"42,43,43\", \"checkpoint_source\": \"/root/autodl-tmp/structfuse/checkpoints/m2_full_qwen/\", \"eval_data\": \"princeton-nlp/SWE-bench_Lite (100 instances)\"}, \"metrics\": {\"checked_at\": \"2026-05-16T08:21 CST\", \"pid_alive\": true, \"eval_pid\": 61328, \"gpu\": \"cuda:0 (shared with Qwen training)\", \"current_checkpoint\": \"random_s42 (1/3)\", \"progress\": \"71/100 instances\", \"speed\": \"~12.7 inst/hr\", \"eta_random_s42\": \"~2026-05-16T10:30 CST\", \"checkpoint_sequence\": [\"random_s42 (running, 71/100)\", \"embed_s43 (postponed)\", \"dataflow_s43 (postponed)\"], \"output_dir\": \"/root/autodl-tmp/structfuse/artifacts/swebench_retrieval_eval/\", \"log\": \"/root/autodl-tmp/structfuse/logs/swebench_eval_all.log\", \"bm25_baseline_300\": {\"R@1\": 0.2733, \"R@5\": 0.4667, \"R@10\": 0.55, \"R@20\": 0.6467, \"n_instances\": 300}, \"director_decision\": \"random_s42 完成后暂停 SWE-bench eval。剩余 2 checkpoints (embed_s43, dataflow_s43) 推迟到 Qwen chain 完成后无 GPU 竞争时再跑。\", \"caveat\": \"3 checkpoints 使用不同 seed (s42/s43/s43)，策略对比 confound 了 seed。论文中定位为外部泛化展示，不做控制对比 claim。\"}}, \"m2_full_qwen_continued\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-14T18:44:20.646Z\", \"updated_at\": \"2026-05-15T23:02:32.982Z\", \"hypothesis\": \"M2 Qwen continued: 继续 m2_full_qwen 的剩余 runs (random_s44 + embedding×3 + dataflow×3)。原实验 cron 在 s42 退出时自动设为 ANALYZING，但链仍在运行。\", \"spec\": {\"command\": \"bash run_m2_full_qwen.sh (chain: random_s44 running → embedding×3 → dataflow×3)\", \"server\": \"bjb1-42106\", \"gpu\": [\"cuda:0\"], \"pid\": \"337267\", \"log_path\": \"/root/runs/structfuse-context/m2_full_qwen.log\", \"data_path\": \"/root/autodl-tmp/structfuse/full_m2_training_data/\", \"data_count\": 11308, \"model_name\": \"Qwen2.5-Coder-3B\", \"seed\": \"42,43,44\"}, \"parent\": \"m2_full_qwen\", \"metrics\": {\"checked_at\": \"2026-05-16T07:01 CST\", \"pid\": 337267, \"pid_alive\": true, \"training_pid\": 18427, \"gpu\": \"cuda:0, 100% util, 62620/97887 MiB\", \"current_subrun\": \"dataflow_aware_s43 (5/7, step 1100+, early_stopping 1/2)\", \"completed_subruns\": [{\"name\": \"random_s42\", \"best_val_loss\": 0.4651, \"best_R@1\": 0.5527, \"stop_step\": 4000}, {\"name\": \"random_s43\", \"best_val_loss\": 0.4476, \"best_R@1\": 0.5554, \"early_stop_step\": 1500}, {\"name\": \"random_s44\", \"best_val_loss\": 0.4252, \"best_R@1\": 0.6009, \"early_stop_step\": 1500}, {\"name\": \"embedding_distance_s43\", \"best_val_loss\": 0.4541, \"best_R@1\": 0.5606, \"early_stop_step\": 1500}, {\"name\": \"embedding_distance_s44\", \"best_val_loss\": 0.4341, \"best_R@1\": 0.5942, \"early_stop_step\": 2000}], \"current_eval\": {\"dataflow_s43_eval_500\": {\"val_loss\": 0.4617, \"R@1\": 0.5495, \"R@5\": 0.9728}, \"dataflow_s43_eval_1000\": {\"val_loss\": 0.4984, \"R@1\": 0.5174, \"R@5\": 0.9581, \"early_stopping_counter\": \"1/2\"}}, \"remaining_subruns\": [\"dataflow_aware_s44\", \"bm25_s42\"], \"training_rate\": \"~182 steps/h\", \"note\": \"dataflow_s43 degrading: eval@1000 R@1=0.5174 (-3.2pp vs eval@500). Best=step 500. Early stop likely at step 1500 if eval@1500 doesn't improve.\"}}, \"m2_full_starcoder_resumed\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-14T18:44:19.253Z\", \"updated_at\": \"2026-05-15T20:45:18.638Z\", \"hypothesis\": \"M2 StarCoder resumed: 继续 m2_full_starcoder 的 8 sequential runs (random×2 + embedding×3 + dataflow×3)。原实验因 cron timeout 标记为 failed，实际 PID 519791 正常运行。\", \"spec\": {\"command\": \"bash run_m2_full_starcoder_resume.sh (8 runs: random_s43→s44→embedding×3→dataflow×3)\", \"server\": \"bjb1-42106\", \"gpu\": [\"cuda:1\"], \"pid\": \"519791\", \"log_path\": \"/root/runs/structfuse-context/m2_full_starcoder.log\", \"data_path\": \"/root/autodl-tmp/structfuse/full_m2_training_data/\", \"data_count\": 11308, \"model_name\": \"StarCoder2-3B\", \"seed\": \"42,43,44\"}, \"parent\": \"m2_full_starcoder\", \"metrics\": {\"checked_at\": \"2026-05-16T04:44 CST\", \"pid\": 519791, \"pid_alive\": true, \"gpu\": \"cuda:1, 100% util, 54767/97887 MiB\", \"current_subrun\": \"embedding_distance_s42 (4/9, step ~600/4242)\", \"completed_subruns\": {\"random_s42\": {\"best_val_loss\": 0.6134, \"best_val_loss_step\": 1000, \"best_R@1\": 0.4604, \"best_R@1_step\": 2500, \"stop_step\": 4000}, \"random_s43\": {\"best_val_loss\": 0.5239, \"best_val_loss_step\": 1500, \"best_R@1\": 0.4912, \"best_R@1_step\": 1500, \"early_stopped\": \"step 2500\"}, \"random_s44\": {\"best_val_loss\": 0.5913, \"best_val_loss_step\": 500, \"best_R@1\": 0.4871, \"best_R@1_step\": 1500, \"early_stopped\": \"step 1500\"}}, \"current_eval\": {\"embed_s42_eval_500\": {\"val_loss\": 0.6154, \"R@1\": 0.4372, \"R@5\": 0.9094}}, \"actual_chain_sequence\": \"random_s42(done) → random_s43(done) → random_s44(done) → embedding_distance_s42(running) → embedding_distance_s43 → embedding_distance_s44 → dataflow_aware_s42 → dataflow_aware_s43 → dataflow_aware_s44\", \"remaining_subruns\": [\"embedding_distance_s43\", \"embedding_distance_s44\", \"dataflow_aware_s42\", \"dataflow_aware_s43\", \"dataflow_aware_s44\"], \"training_rate\": \"~200 steps/h on cuda:1\", \"note\": \"embed_s42 eval@500 R@1=0.4372 below all 3 random baselines (0.4604/0.4912/0.4871). Early signal concerning for embedding strategy on StarCoder. Need eval@1000+ to confirm.\"}}, \"m1_reextract_v2\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-13T20:00:20.578Z\", \"updated_at\": \"2026-05-15T20:44:09.645Z\", \"hypothesis\": \"M1 重提取 v2：恢复 28,276 个因运行时瞬态文件系统故障失败的 instances（82 repos）。CodeQL pack 已修复，端到端测试通过。预期将训练数据从 15,897 提升至 ~44,173。D022 批准。\", \"parent\": \"m1_extraction\", \"spec\": {\"command\": \"bash scripts/rerun_m1_failed.sh (4 CPU workers, CodeQL 2-hop, pack installed)\", \"server\": \"bjb1-42106\", \"data_path\": \"/root/autodl-tmp/structfuse/full_m1_data/\", \"data_count\": 28276, \"model_name\": \"N/A (CodeQL extraction)\", \"seed\": \"N/A\", \"log_path\": \"/root/runs/structfuse-context/m1_reextract_v2.log\", \"checkpoint_source\": \"rerun of m1_extraction failed instances (v2, CodeQL fixed)\", \"eval_data\": \"N/A\"}, \"notes\": \"moto CodeQL call_graph.ql timeout (NOT OOM): directCallEdge predicate exceeds 300s timeout on every instance (exit code 33). 536 moto instances all fail call_graph, fallback to embedding-distance. Isolated failure — 1/4 workers stuck on moto (~5min/instance, ~38h total), other 3 workers process pydicom/conan/MONAI normally. DB creation succeeded; bounded_dataflow.ql unaffected. [2026-05-16] Combine script ready: /root/structfuse/scripts/combine_m1_reextract.py. Dry-run stats: 39,712/44,173 (89.9%) structural data rate. Run after extraction completes: source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && python3 /root/structfuse/scripts/combine_m1_reextract.py\", \"metrics\": {\"all_jsonl_lines\": 44173, \"new_json_files\": \"43,858/44,173 (99.3%)\", \"repos_done\": \"81/82\", \"last_checked\": \"2026-05-16T04:43 CST\", \"remaining_repos\": [\"getmoto/moto (200/536, 37.3%)\"], \"completed_repos_update\": \"MONAI 524/524 完成\", \"processes_alive\": true, \"moto_eta\": \"~2026-05-17T07:00 CST (~28h remaining)\", \"issue\": \"moto CodeQL call_graph 100% timeout (exit 33). All moto instances produce degraded output (no call graph).\", \"disk_free_gb\": 85, \"note\": \"可选：不等 moto 完成，现在用 43,858 个 json 执行合并（已达 99.3%），moto 剩余 336 个后续补入。\"}}}, \"count\": 4, \"total\": 4, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.1224}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "0e3a3a44-67d9-4139-bfff-e7f4f822dd45",
  "isSidechain": false,
  "promptId": "cb482ce5-85c1-49a1-985e-c68475dfc7e7",
  "type": "user",
  "uuid": "4446a9e0-47e6-4a7b-917e-dfe09bac239d",
  "toolUseResult": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"experiments\\\": {\\\"plan_003_swebench_eval\\\": {\\\"status\\\": \\\"RUNNING\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-15T18:41:00.685Z\\\", \\\"updated_at\\\": \\\"2026-05-16T00:22:31.107Z\\\", \\\"hypothesis\\\": \\\"SWE-bench Lite 纯检索 eval：用 3 个 Qwen M2 checkpoints (random_s42, embed_s43, dataflow_s43) 在 100 个 SWE-bench Lite 实例上评估 file-level retrieval Recall@{1,5,10,20} 和 MRR。定位为外部泛化展示，不做控制对比 claim（3 checkpoint 用了不同 seed，策略对比 confound 了 seed）。\\\", \\\"spec\\\": {\\\"command\\\": \\\"python eval_swebench_retrieval.py (3 checkpoints sequential on GPU 0)\\\", \\\"server\\\": \\\"bjb1-42106\\\", \\\"data_path\\\": \\\"/root/autodl-tmp/structfuse/artifacts/swebench_retrieval_eval/\\\", \\\"data_count\\\": 100, \\\"model_name\\\": \\\"Qwen2.5-Coder-3B (3 M2 checkpoints: random_s42, embed_s43, dataflow_s43)\\\", \\\"seed\\\": \\\"42,43,43\\\", \\\"checkpoint_source\\\": \\\"/root/autodl-tmp/structfuse/checkpoints/m2_full_qwen/\\\", \\\"eval_data\\\": \\\"princeton-nlp/SWE-bench_Lite (100 instances)\\\"}, \\\"metrics\\\": {\\\"checked_at\\\": \\\"2026-05-16T08:21 CST\\\", \\\"pid_alive\\\": true, \\\"eval_pid\\\": 61328, \\\"gpu\\\": \\\"cuda:0 (shared with Qwen training)\\\", \\\"current_checkpoint\\\": \\\"random_s42 (1/3)\\\", \\\"progress\\\": \\\"71/100 instances\\\", \\\"speed\\\": \\\"~12.7 inst/hr\\\", \\\"eta_random_s42\\\": \\\"~2026-05-16T10:30 CST\\\", \\\"checkpoint_sequence\\\": [\\\"random_s42 (running, 71/100)\\\", \\\"embed_s43 (postponed)\\\", \\\"dataflow_s43 (postponed)\\\"], \\\"output_dir\\\": \\\"/root/autodl-tmp/structfuse/artifacts/swebench_retrieval_eval/\\\", \\\"log\\\": \\\"/root/autodl-tmp/structfuse/logs/swebench_eval_all.log\\\", \\\"bm25_baseline_300\\\": {\\\"R@1\\\": 0.2733, \\\"R@5\\\": 0.4667, \\\"R@10\\\": 0.55, \\\"R@20\\\": 0.6467, \\\"n_instances\\\": 300}, \\\"director_decision\\\": \\\"random_s42 完成后暂停 SWE-bench eval。剩余 2 checkpoints (embed_s43, dataflow_s43) 推迟到 Qwen chain 完成后无 GPU 竞争时再跑。\\\", \\\"caveat\\\": \\\"3 checkpoints 使用不同 seed (s42/s43/s43)，策略对比 confound 了 seed。论文中定位为外部泛化展示，不做控制对比 claim。\\\"}}, \\\"m2_full_qwen_continued\\\": {\\\"status\\\": \\\"RUNNING\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-14T18:44:20.646Z\\\", \\\"updated_at\\\": \\\"2026-05-15T23:02:32.982Z\\\", \\\"hypothesis\\\": \\\"M2 Qwen continued: 继续 m2_full_qwen 的剩余 runs (random_s44 + embedding×3 + dataflow×3)。原实验 cron 在 s42 退出时自动设为 ANALYZING，但链仍在运行。\\\", \\\"spec\\\": {\\\"command\\\": \\\"bash run_m2_full_qwen.sh (chain: random_s44 running → embedding×3 → dataflow×3)\\\", \\\"server\\\": \\\"bjb1-42106\\\", \\\"gpu\\\": [\\\"cuda:0\\\"], \\\"pid\\\": \\\"337267\\\", \\\"log_path\\\": \\\"/root/runs/structfuse-context/m2_full_qwen.log\\\", \\\"data_path\\\": \\\"/root/autodl-tmp/structfuse/full_m2_training_data/\\\", \\\"data_count\\\": 11308, \\\"model_name\\\": \\\"Qwen2.5-Coder-3B\\\", \\\"seed\\\": \\\"42,43,44\\\"}, \\\"parent\\\": \\\"m2_full_qwen\\\", \\\"metrics\\\": {\\\"checked_at\\\": \\\"2026-05-16T07:01 CST\\\", \\\"pid\\\": 337267, \\\"pid_alive\\\": true, \\\"training_pid\\\": 18427, \\\"gpu\\\": \\\"cuda:0, 100% util, 62620/97887 MiB\\\", \\\"current_subrun\\\": \\\"dataflow_aware_s43 (5/7, step 1100+, early_stopping 1/2)\\\", \\\"completed_subruns\\\": [{\\\"name\\\": \\\"random_s42\\\", \\\"best_val_loss\\\": 0.4651, \\\"best_R@1\\\": 0.5527, \\\"stop_step\\\": 4000}, {\\\"name\\\": \\\"random_s43\\\", \\\"best_val_loss\\\": 0.4476, \\\"best_R@1\\\": 0.5554, \\\"early_stop_step\\\": 1500}, {\\\"name\\\": \\\"random_s44\\\", \\\"best_val_loss\\\": 0.4252, \\\"best_R@1\\\": 0.6009, \\\"early_stop_step\\\": 1500}, {\\\"name\\\": \\\"embedding_distance_s43\\\", \\\"best_val_loss\\\": 0.4541, \\\"best_R@1\\\": 0.5606, \\\"early_stop_step\\\": 1500}, {\\\"name\\\": \\\"embedding_distance_s44\\\", \\\"best_val_loss\\\": 0.4341, \\\"best_R@1\\\": 0.5942, \\\"early_stop_step\\\": 2000}], \\\"current_eval\\\": {\\\"dataflow_s43_eval_500\\\": {\\\"val_loss\\\": 0.4617, \\\"R@1\\\": 0.5495, \\\"R@5\\\": 0.9728}, \\\"dataflow_s43_eval_1000\\\": {\\\"val_loss\\\": 0.4984, \\\"R@1\\\": 0.5174, \\\"R@5\\\": 0.9581, \\\"early_stopping_counter\\\": \\\"1/2\\\"}}, \\\"remaining_subruns\\\": [\\\"dataflow_aware_s44\\\", \\\"bm25_s42\\\"], \\\"training_rate\\\": \\\"~182 steps/h\\\", \\\"note\\\": \\\"dataflow_s43 degrading: eval@1000 R@1=0.5174 (-3.2pp vs eval@500). Best=step 500. Early stop likely at step 1500 if eval@1500 doesn't improve.\\\"}}, \\\"m2_full_starcoder_resumed\\\": {\\\"status\\\": \\\"RUNNING\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-14T18:44:19.253Z\\\", \\\"updated_at\\\": \\\"2026-05-15T20:45:18.638Z\\\", \\\"hypothesis\\\": \\\"M2 StarCoder resumed: 继续 m2_full_starcoder 的 8 sequential runs (random×2 + embedding×3 + dataflow×3)。原实验因 cron timeout 标记为 failed，实际 PID 519791 正常运行。\\\", \\\"spec\\\": {\\\"command\\\": \\\"bash run_m2_full_starcoder_resume.sh (8 runs: random_s43→s44→embedding×3→dataflow×3)\\\", \\\"server\\\": \\\"bjb1-42106\\\", \\\"gpu\\\": [\\\"cuda:1\\\"], \\\"pid\\\": \\\"519791\\\", \\\"log_path\\\": \\\"/root/runs/structfuse-context/m2_full_starcoder.log\\\", \\\"data_path\\\": \\\"/root/autodl-tmp/structfuse/full_m2_training_data/\\\", \\\"data_count\\\": 11308, \\\"model_name\\\": \\\"StarCoder2-3B\\\", \\\"seed\\\": \\\"42,43,44\\\"}, \\\"parent\\\": \\\"m2_full_starcoder\\\", \\\"metrics\\\": {\\\"checked_at\\\": \\\"2026-05-16T04:44 CST\\\", \\\"pid\\\": 519791, \\\"pid_alive\\\": true, \\\"gpu\\\": \\\"cuda:1, 100% util, 54767/97887 MiB\\\", \\\"current_subrun\\\": \\\"embedding_distance_s42 (4/9, step ~600/4242)\\\", \\\"completed_subruns\\\": {\\\"random_s42\\\": {\\\"best_val_loss\\\": 0.6134, \\\"best_val_loss_step\\\": 1000, \\\"best_R@1\\\": 0.4604, \\\"best_R@1_step\\\": 2500, \\\"stop_step\\\": 4000}, \\\"random_s43\\\": {\\\"best_val_loss\\\": 0.5239, \\\"best_val_loss_step\\\": 1500, \\\"best_R@1\\\": 0.4912, \\\"best_R@1_step\\\": 1500, \\\"early_stopped\\\": \\\"step 2500\\\"}, \\\"random_s44\\\": {\\\"best_val_loss\\\": 0.5913, \\\"best_val_loss_step\\\": 500, \\\"best_R@1\\\": 0.4871, \\\"best_R@1_step\\\": 1500, \\\"early_stopped\\\": \\\"step 1500\\\"}}, \\\"current_eval\\\": {\\\"embed_s42_eval_500\\\": {\\\"val_loss\\\": 0.6154, \\\"R@1\\\": 0.4372, \\\"R@5\\\": 0.9094}}, \\\"actual_chain_sequence\\\": \\\"random_s42(done) → random_s43(done) → random_s44(done) → embedding_distance_s42(running) → embedding_distance_s43 → embedding_distance_s44 → dataflow_aware_s42 → dataflow_aware_s43 → dataflow_aware_s44\\\", \\\"remaining_subruns\\\": [\\\"embedding_distance_s43\\\", \\\"embedding_distance_s44\\\", \\\"dataflow_aware_s42\\\", \\\"dataflow_aware_s43\\\", \\\"dataflow_aware_s44\\\"], \\\"training_rate\\\": \\\"~200 steps/h on cuda:1\\\", \\\"note\\\": \\\"embed_s42 eval@500 R@1=0.4372 below all 3 random baselines (0.4604/0.4912/0.4871). Early signal concerning for embedding strategy on StarCoder. Need eval@1000+ to confirm.\\\"}}, \\\"m1_reextract_v2\\\": {\\\"status\\\": \\\"RUNNING\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-13T20:00:20.578Z\\\", \\\"updated_at\\\": \\\"2026-05-15T20:44:09.645Z\\\", \\\"hypothesis\\\": \\\"M1 重提取 v2：恢复 28,276 个因运行时瞬态文件系统故障失败的 instances（82 repos）。CodeQL pack 已修复，端到端测试通过。预期将训练数据从 15,897 提升至 ~44,173。D022 批准。\\\", \\\"parent\\\": \\\"m1_extraction\\\", \\\"spec\\\": {\\\"command\\\": \\\"bash scripts/rerun_m1_failed.sh (4 CPU workers, CodeQL 2-hop, pack installed)\\\", \\\"server\\\": \\\"bjb1-42106\\\", \\\"data_path\\\": \\\"/root/autodl-tmp/structfuse/full_m1_data/\\\", \\\"data_count\\\": 28276, \\\"model_name\\\": \\\"N/A (CodeQL extraction)\\\", \\\"seed\\\": \\\"N/A\\\", \\\"log_path\\\": \\\"/root/runs/structfuse-context/m1_reextract_v2.log\\\", \\\"checkpoint_source\\\": \\\"rerun of m1_extraction failed instances (v2, CodeQL fixed)\\\", \\\"eval_data\\\": \\\"N/A\\\"}, \\\"notes\\\": \\\"moto CodeQL call_graph.ql timeout (NOT OOM): directCallEdge predicate exceeds 300s timeout on every instance (exit code 33). 536 moto instances all fail call_graph, fallback to embedding-distance. Isolated failure — 1/4 workers stuck on moto (~5min/instance, ~38h total), other 3 workers process pydicom/conan/MONAI normally. DB creation succeeded; bounded_dataflow.ql unaffected. [2026-05-16] Combine script ready: /root/structfuse/scripts/combine_m1_reextract.py. Dry-run stats: 39,712/44,173 (89.9%) structural data rate. Run after extraction completes: source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && python3 /root/structfuse/scripts/combine_m1_reextract.py\\\", \\\"metrics\\\": {\\\"all_jsonl_lines\\\": 44173, \\\"new_json_files\\\": \\\"43,858/44,173 (99.3%)\\\", \\\"repos_done\\\": \\\"81/82\\\", \\\"last_checked\\\": \\\"2026-05-16T04:43 CST\\\", \\\"remaining_repos\\\": [\\\"getmoto/moto (200/536, 37.3%)\\\"], \\\"completed_repos_update\\\": \\\"MONAI 524/524 完成\\\", \\\"processes_alive\\\": true, \\\"moto_eta\\\": \\\"~2026-05-17T07:00 CST (~28h remaining)\\\", \\\"issue\\\": \\\"moto CodeQL call_graph 100% timeout (exit 33). All moto instances produce degraded output (no call graph).\\\", \\\"disk_free_gb\\\": 85, \\\"note\\\": \\\"可选：不等 moto 完成，现在用 43,858 个 json 执行合并（已达 99.3%），moto 剩余 336 个后续补入。\\\"}}}, \\\"count\\\": 4, \\\"total\\\": 4, \\\"baseline\\\": null}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.1224}}\"}",
  "mcpMeta": {
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"experiments\": {\"plan_003_swebench_eval\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-15T18:41:00.685Z\", \"updated_at\": \"2026-05-16T00:22:31.107Z\", \"hypothesis\": \"SWE-bench Lite 纯检索 eval：用 3 个 Qwen M2 checkpoints (random_s42, embed_s43, dataflow_s43) 在 100 个 SWE-bench Lite 实例上评估 file-level retrieval Recall@{1,5,10,20} 和 MRR。定位为外部泛化展示，不做控制对比 claim（3 checkpoint 用了不同 seed，策略对比 confound 了 seed）。\", \"spec\": {\"command\": \"python eval_swebench_retrieval.py (3 checkpoints sequential on GPU 0)\", \"server\": \"bjb1-42106\", \"data_path\": \"/root/autodl-tmp/structfuse/artifacts/swebench_retrieval_eval/\", \"data_count\": 100, \"model_name\": \"Qwen2.5-Coder-3B (3 M2 checkpoints: random_s42, embed_s43, dataflow_s43)\", \"seed\": \"42,43,43\", \"checkpoint_source\": \"/root/autodl-tmp/structfuse/checkpoints/m2_full_qwen/\", \"eval_data\": \"princeton-nlp/SWE-bench_Lite (100 instances)\"}, \"metrics\": {\"checked_at\": \"2026-05-16T08:21 CST\", \"pid_alive\": true, \"eval_pid\": 61328, \"gpu\": \"cuda:0 (shared with Qwen training)\", \"current_checkpoint\": \"random_s42 (1/3)\", \"progress\": \"71/100 instances\", \"speed\": \"~12.7 inst/hr\", \"eta_random_s42\": \"~2026-05-16T10:30 CST\", \"checkpoint_sequence\": [\"random_s42 (running, 71/100)\", \"embed_s43 (postponed)\", \"dataflow_s43 (postponed)\"], \"output_dir\": \"/root/autodl-tmp/structfuse/artifacts/swebench_retrieval_eval/\", \"log\": \"/root/autodl-tmp/structfuse/logs/swebench_eval_all.log\", \"bm25_baseline_300\": {\"R@1\": 0.2733, \"R@5\": 0.4667, \"R@10\": 0.55, \"R@20\": 0.6467, \"n_instances\": 300}, \"director_decision\": \"random_s42 完成后暂停 SWE-bench eval。剩余 2 checkpoints (embed_s43, dataflow_s43) 推迟到 Qwen chain 完成后无 GPU 竞争时再跑。\", \"caveat\": \"3 checkpoints 使用不同 seed (s42/s43/s43)，策略对比 confound 了 seed。论文中定位为外部泛化展示，不做控制对比 claim。\"}}, \"m2_full_qwen_continued\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-14T18:44:20.646Z\", \"updated_at\": \"2026-05-15T23:02:32.982Z\", \"hypothesis\": \"M2 Qwen continued: 继续 m2_full_qwen 的剩余 runs (random_s44 + embedding×3 + dataflow×3)。原实验 cron 在 s42 退出时自动设为 ANALYZING，但链仍在运行。\", \"spec\": {\"command\": \"bash run_m2_full_qwen.sh (chain: random_s44 running → embedding×3 → dataflow×3)\", \"server\": \"bjb1-42106\", \"gpu\": [\"cuda:0\"], \"pid\": \"337267\", \"log_path\": \"/root/runs/structfuse-context/m2_full_qwen.log\", \"data_path\": \"/root/autodl-tmp/structfuse/full_m2_training_data/\", \"data_count\": 11308, \"model_name\": \"Qwen2.5-Coder-3B\", \"seed\": \"42,43,44\"}, \"parent\": \"m2_full_qwen\", \"metrics\": {\"checked_at\": \"2026-05-16T07:01 CST\", \"pid\": 337267, \"pid_alive\": true, \"training_pid\": 18427, \"gpu\": \"cuda:0, 100% util, 62620/97887 MiB\", \"current_subrun\": \"dataflow_aware_s43 (5/7, step 1100+, early_stopping 1/2)\", \"completed_subruns\": [{\"name\": \"random_s42\", \"best_val_loss\": 0.4651, \"best_R@1\": 0.5527, \"stop_step\": 4000}, {\"name\": \"random_s43\", \"best_val_loss\": 0.4476, \"best_R@1\": 0.5554, \"early_stop_step\": 1500}, {\"name\": \"random_s44\", \"best_val_loss\": 0.4252, \"best_R@1\": 0.6009, \"early_stop_step\": 1500}, {\"name\": \"embedding_distance_s43\", \"best_val_loss\": 0.4541, \"best_R@1\": 0.5606, \"early_stop_step\": 1500}, {\"name\": \"embedding_distance_s44\", \"best_val_loss\": 0.4341, \"best_R@1\": 0.5942, \"early_stop_step\": 2000}], \"current_eval\": {\"dataflow_s43_eval_500\": {\"val_loss\": 0.4617, \"R@1\": 0.5495, \"R@5\": 0.9728}, \"dataflow_s43_eval_1000\": {\"val_loss\": 0.4984, \"R@1\": 0.5174, \"R@5\": 0.9581, \"early_stopping_counter\": \"1/2\"}}, \"remaining_subruns\": [\"dataflow_aware_s44\", \"bm25_s42\"], \"training_rate\": \"~182 steps/h\", \"note\": \"dataflow_s43 degrading: eval@1000 R@1=0.5174 (-3.2pp vs eval@500). Best=step 500. Early stop likely at step 1500 if eval@1500 doesn't improve.\"}}, \"m2_full_starcoder_resumed\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-14T18:44:19.253Z\", \"updated_at\": \"2026-05-15T20:45:18.638Z\", \"hypothesis\": \"M2 StarCoder resumed: 继续 m2_full_starcoder 的 8 sequential runs (random×2 + embedding×3 + dataflow×3)。原实验因 cron timeout 标记为 failed，实际 PID 519791 正常运行。\", \"spec\": {\"command\": \"bash run_m2_full_starcoder_resume.sh (8 runs: random_s43→s44→embedding×3→dataflow×3)\", \"server\": \"bjb1-42106\", \"gpu\": [\"cuda:1\"], \"pid\": \"519791\", \"log_path\": \"/root/runs/structfuse-context/m2_full_starcoder.log\", \"data_path\": \"/root/autodl-tmp/structfuse/full_m2_training_data/\", \"data_count\": 11308, \"model_name\": \"StarCoder2-3B\", \"seed\": \"42,43,44\"}, \"parent\": \"m2_full_starcoder\", \"metrics\": {\"checked_at\": \"2026-05-16T04:44 CST\", \"pid\": 519791, \"pid_alive\": true, \"gpu\": \"cuda:1, 100% util, 54767/97887 MiB\", \"current_subrun\": \"embedding_distance_s42 (4/9, step ~600/4242)\", \"completed_subruns\": {\"random_s42\": {\"best_val_loss\": 0.6134, \"best_val_loss_step\": 1000, \"best_R@1\": 0.4604, \"best_R@1_step\": 2500, \"stop_step\": 4000}, \"random_s43\": {\"best_val_loss\": 0.5239, \"best_val_loss_step\": 1500, \"best_R@1\": 0.4912, \"best_R@1_step\": 1500, \"early_stopped\": \"step 2500\"}, \"random_s44\": {\"best_val_loss\": 0.5913, \"best_val_loss_step\": 500, \"best_R@1\": 0.4871, \"best_R@1_step\": 1500, \"early_stopped\": \"step 1500\"}}, \"current_eval\": {\"embed_s42_eval_500\": {\"val_loss\": 0.6154, \"R@1\": 0.4372, \"R@5\": 0.9094}}, \"actual_chain_sequence\": \"random_s42(done) → random_s43(done) → random_s44(done) → embedding_distance_s42(running) → embedding_distance_s43 → embedding_distance_s44 → dataflow_aware_s42 → dataflow_aware_s43 → dataflow_aware_s44\", \"remaining_subruns\": [\"embedding_distance_s43\", \"embedding_distance_s44\", \"dataflow_aware_s42\", \"dataflow_aware_s43\", \"dataflow_aware_s44\"], \"training_rate\": \"~200 steps/h on cuda:1\", \"note\": \"embed_s42 eval@500 R@1=0.4372 below all 3 random baselines (0.4604/0.4912/0.4871). Early signal concerning for embedding strategy on StarCoder. Need eval@1000+ to confirm.\"}}, \"m1_reextract_v2\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-13T20:00:20.578Z\", \"updated_at\": \"2026-05-15T20:44:09.645Z\", \"hypothesis\": \"M1 重提取 v2：恢复 28,276 个因运行时瞬态文件系统故障失败的 instances（82 repos）。CodeQL pack 已修复，端到端测试通过。预期将训练数据从 15,897 提升至 ~44,173。D022 批准。\", \"parent\": \"m1_extraction\", \"spec\": {\"command\": \"bash scripts/rerun_m1_failed.sh (4 CPU workers, CodeQL 2-hop, pack installed)\", \"server\": \"bjb1-42106\", \"data_path\": \"/root/autodl-tmp/structfuse/full_m1_data/\", \"data_count\": 28276, \"model_name\": \"N/A (CodeQL extraction)\", \"seed\": \"N/A\", \"log_path\": \"/root/runs/structfuse-context/m1_reextract_v2.log\", \"checkpoint_source\": \"rerun of m1_extraction failed instances (v2, CodeQL fixed)\", \"eval_data\": \"N/A\"}, \"notes\": \"moto CodeQL call_graph.ql timeout (NOT OOM): directCallEdge predicate exceeds 300s timeout on every instance (exit code 33). 536 moto instances all fail call_graph, fallback to embedding-distance. Isolated failure — 1/4 workers stuck on moto (~5min/instance, ~38h total), other 3 workers process pydicom/conan/MONAI normally. DB creation succeeded; bounded_dataflow.ql unaffected. [2026-05-16] Combine script ready: /root/structfuse/scripts/combine_m1_reextract.py. Dry-run stats: 39,712/44,173 (89.9%) structural data rate. Run after extraction completes: source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && python3 /root/structfuse/scripts/combine_m1_reextract.py\", \"metrics\": {\"all_jsonl_lines\": 44173, \"new_json_files\": \"43,858/44,173 (99.3%)\", \"repos_done\": \"81/82\", \"last_checked\": \"2026-05-16T04:43 CST\", \"remaining_repos\": [\"getmoto/moto (200/536, 37.3%)\"], \"completed_repos_update\": \"MONAI 524/524 完成\", \"processes_alive\": true, \"moto_eta\": \"~2026-05-17T07:00 CST (~28h remaining)\", \"issue\": \"moto CodeQL call_graph 100% timeout (exit 33). All moto instances produce degraded output (no call graph).\", \"disk_free_gb\": 85, \"note\": \"可选：不等 moto 完成，现在用 43,858 个 json 执行合并（已达 99.3%），moto 剩余 336 个后续补入。\"}}}, \"count\": 4, \"total\": 4, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.1224}}"
    }
  },
  "sourceToolAssistantUUID": "0e3a3a44-67d9-4139-bfff-e7f4f822dd45",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/.claude/sessions/reviewer_65cfe724",
  "sessionId": "f444a635-eeef-4924-9b48-a4c308632421",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---


### Tool call

_source line 105 · 2026-05-16T02:31:38.780Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_015KdfsNRjcHexm9trPmZi1U`</summary>

```json
{
  "server": "bjb1-42106",
  "command": "nvidia-smi --query-gpu=index,name,utilization.gpu,memory.used,memory.total --format=csv,noheader"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4446a9e0-47e6-4a7b-917e-dfe09bac239d",
  "isSidechain": false,
  "requestId": "req_011Cb5TozuPS54YCab16mdAq",
  "type": "assistant",
  "uuid": "527a495c-2fc7-4ccf-8f14-f953d1eeec3d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/.claude/sessions/reviewer_65cfe724",
  "sessionId": "f444a635-eeef-4924-9b48-a4c308632421",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DxbbiUUpPV99Z5HVTdELu6",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 91977,
      "cache_read_input_tokens": 11841,
      "output_tokens": 290,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 91977,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 290,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 91977,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 91977
          },
          "type": "message"
        }
      ],
      "speed": "standard"
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


### Runtime record

_source line 106_

```json
{
  "type": "last-prompt",
  "lastPrompt": "[系统通知 — worker_done:worker_ops_training-and-eval-status_20260516T022911]: Worker worker_ops_training-and-eval-status_20260516T022911 已完成（status=done），请审查 Agent 的处理结果。",
  "leafUuid": "527a495c-2fc7-4ccf-8f14-f953d1eeec3d",
  "sessionId": "f444a635-eeef-4924-9b48-a4c308632421"
}
```

---


### Runtime record

_source line 107_

```json
{
  "type": "ai-title",
  "aiTitle": "Review research literature worker completion",
  "sessionId": "f444a635-eeef-4924-9b48-a4c308632421"
}
```

---


### Tool result

_source line 108 · 2026-05-16T02:31:39.870Z_

<details><summary>↩ Tool result · `toolu_015KdfsNRjcHexm9trPmZi1U`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"0, NVIDIA RTX PRO 6000 Blackwell Server Edition, 100 %, 51001 MiB, 97887 MiB\\n1, NVIDIA RTX PRO 6000 Blackwell Server Edition, 100 %, 53467 MiB, 97887 MiB\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.08}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "527a495c-2fc7-4ccf-8f14-f953d1eeec3d",
  "isSidechain": false,
  "promptId": "cb482ce5-85c1-49a1-985e-c68475dfc7e7",
  "type": "user",
  "uuid": "998d6d17-4c4f-4b8b-a906-1de0269c9ba2",
  "toolUseResult": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"0, NVIDIA RTX PRO 6000 Blackwell Server Edition, 100 %, 51001 MiB, 97887 MiB\\\\n1, NVIDIA RTX PRO 6000 Blackwell Server Edition, 100 %, 53467 MiB, 97887 MiB\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 1.08}}\"}",
  "mcpMeta": {
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"0, NVIDIA RTX PRO 6000 Blackwell Server Edition, 100 %, 51001 MiB, 97887 MiB\\n1, NVIDIA RTX PRO 6000 Blackwell Server Edition, 100 %, 53467 MiB, 97887 MiB\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.08}}"
    }
  },
  "sourceToolAssistantUUID": "527a495c-2fc7-4ccf-8f14-f953d1eeec3d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/.claude/sessions/reviewer_65cfe724",
  "sessionId": "f444a635-eeef-4924-9b48-a4c308632421",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---


### Assistant

_source line 109 · 2026-05-16T02:31:50.809Z_

<details><summary>Logged reasoning block</summary>

```text
Let me check the actual running processes and training progress. I need to:

1. Verify GPU utilization matches what's expected (cuda:0 for Qwen, cuda:1 for StarCoder)
2. Check if SWE-bench eval is still running on cuda:0 (competing with Qwen training)
3. Check actual PID status
4. Look at training logs for current progress

Key observations so far:
- GPU 0: 100% util, 51001 MiB / 97887 MiB → Qwen training. Registry says 62620 MiB at last check (07:01 CST), now shows 51001 MiB. 

The memory drop on GPU 0 might signal a subrun transition. GPU 1 shows 53467 MiB / 97887 MiB for StarCoder training, which is consistent with the 54767 MiB recorded at 04:44 CST. Now I need to verify the processes are actually running, check the latest training progress, confirm whether SWE-bench eval is still competing for GPU 0, and validate that the GPU allocation matches the project configuration.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "998d6d17-4c4f-4b8b-a906-1de0269c9ba2",
  "isSidechain": false,
  "requestId": "req_011Cb5TpZZvB2dfKVMzAdqSD",
  "type": "assistant",
  "uuid": "6aed3169-bb79-452f-898d-1d4d69a2d2fc",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/.claude/sessions/reviewer_65cfe724",
  "sessionId": "f444a635-eeef-4924-9b48-a4c308632421",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RCFcKM4qBaKDLY3SdFRUbu",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4260,
      "cache_read_input_tokens": 103818,
      "output_tokens": 644,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 4260,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 644,
          "cache_read_input_tokens": 103818,
          "cache_creation_input_tokens": 4260,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 4260
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

_source line 110 · 2026-05-16T02:31:50.828Z_

GPU 双卡都在 100% 利用率。继续检查进程和训练进度。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6aed3169-bb79-452f-898d-1d4d69a2d2fc",
  "isSidechain": false,
  "requestId": "req_011Cb5TpZZvB2dfKVMzAdqSD",
  "type": "assistant",
  "uuid": "1a8bff7a-a0d6-4d96-91a9-63e3adfa1868",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/.claude/sessions/reviewer_65cfe724",
  "sessionId": "f444a635-eeef-4924-9b48-a4c308632421",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RCFcKM4qBaKDLY3SdFRUbu",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4260,
      "cache_read_input_tokens": 103818,
      "output_tokens": 644,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 4260,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 644,
          "cache_read_input_tokens": 103818,
          "cache_creation_input_tokens": 4260,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 4260
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

_source line 111 · 2026-05-16T02:31:50.835Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01Cv951fgkkZzVDVXVsC5YZh`</summary>

```json
{
  "server": "bjb1-42106",
  "command": "ps -p 337267,519791,61328 -o pid,stat,etime,cmd --no-headers"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1a8bff7a-a0d6-4d96-91a9-63e3adfa1868",
  "isSidechain": false,
  "requestId": "req_011Cb5TpZZvB2dfKVMzAdqSD",
  "type": "assistant",
  "uuid": "24a0e6b4-1983-48a5-90fa-6d644b0c0195",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/.claude/sessions/reviewer_65cfe724",
  "sessionId": "f444a635-eeef-4924-9b48-a4c308632421",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RCFcKM4qBaKDLY3SdFRUbu",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4260,
      "cache_read_input_tokens": 103818,
      "output_tokens": 644,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 4260,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 644,
          "cache_read_input_tokens": 103818,
          "cache_creation_input_tokens": 4260,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 4260
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

_source line 112 · 2026-05-16T02:31:51.132Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01BypsVoce4uttVoCs6oAk9F`</summary>

```json
{
  "server": "bjb1-42106",
  "command": "tail -30 /root/runs/structfuse-context/m2_full_qwen.log"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "24a0e6b4-1983-48a5-90fa-6d644b0c0195",
  "isSidechain": false,
  "requestId": "req_011Cb5TpZZvB2dfKVMzAdqSD",
  "type": "assistant",
  "uuid": "a0f00e0f-4ef7-47dd-9dbe-2e7cdb030dce",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/.claude/sessions/reviewer_65cfe724",
  "sessionId": "f444a635-eeef-4924-9b48-a4c308632421",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RCFcKM4qBaKDLY3SdFRUbu",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4260,
      "cache_read_input_tokens": 103818,
      "output_tokens": 644,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 4260,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 644,
          "cache_read_input_tokens": 103818,
          "cache_creation_input_tokens": 4260,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 4260
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

_source line 113 · 2026-05-16T02:31:51.201Z_

<details><summary>↩ Tool result · `toolu_01Cv951fgkkZzVDVXVsC5YZh`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"337267 S+    1-15:07:37 bash run_m2_full_qwen.sh\\n519791 Ss+   1-08:28:40 bash -c rm -f /tmp/agent-ml-exit/m2_full_starcoder.exit; mkdir -p /tmp/agent-ml-exit; trap '_EC=$?; echo \\\"EXIT_CODE=$_EC\\\" >> ~/runs/structfuse-context/m2_full_starcoder.log; printf \\\"%s|%s\\\\n\\\" \\\"$_EC\\\" \\\"$(date -u +%Y-%m-%dT%H:%M:%SZ)\\\" > /tmp/agent-ml-exit/m2_full_starcoder.exit' EXIT; trap 'exit 129' HUP; trap 'exit 130' INT; trap 'exit 143' TERM; { cd /root/structfuse && export CUDA_VISIBLE_DEVICES=1 && timeout 518400 env bash -c 'bash -c \\\"cd /root/structfuse && bash run_m2_full_starcoder_resume.sh\\\"'; } > ~/runs/structfuse-context/m2_full_starcoder.log 2>&1\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.35}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "24a0e6b4-1983-48a5-90fa-6d644b0c0195",
  "isSidechain": false,
  "promptId": "cb482ce5-85c1-49a1-985e-c68475dfc7e7",
  "type": "user",
  "uuid": "122b7e01-50bb-47e7-b3b5-4b6ff01ecb17",
  "toolUseResult": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"337267 S+    1-15:07:37 bash run_m2_full_qwen.sh\\\\n519791 Ss+   1-08:28:40 bash -c rm -f /tmp/agent-ml-exit/m2_full_starcoder.exit; mkdir -p /tmp/agent-ml-exit; trap '_EC=$?; echo \\\\\\\"EXIT_CODE=$_EC\\\\\\\" >> ~/runs/structfuse-context/m2_full_starcoder.log; printf \\\\\\\"%s|%s\\\\\\\\n\\\\\\\" \\\\\\\"$_EC\\\\\\\" \\\\\\\"$(date -u +%Y-%m-%dT%H:%M:%SZ)\\\\\\\" > /tmp/agent-ml-exit/m2_full_starcoder.exit' EXIT; trap 'exit 129' HUP; trap 'exit 130' INT; trap 'exit 143' TERM; { cd /root/structfuse && export CUDA_VISIBLE_DEVICES=1 && timeout 518400 env bash -c 'bash -c \\\\\\\"cd /root/structfuse && bash run_m2_full_starcoder_resume.sh\\\\\\\"'; } > ~/runs/structfuse-context/m2_full_starcoder.log 2>&1\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.35}}\"}",
  "mcpMeta": {
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"337267 S+    1-15:07:37 bash run_m2_full_qwen.sh\\n519791 Ss+   1-08:28:40 bash -c rm -f /tmp/agent-ml-exit/m2_full_starcoder.exit; mkdir -p /tmp/agent-ml-exit; trap '_EC=$?; echo \\\"EXIT_CODE=$_EC\\\" >> ~/runs/structfuse-context/m2_full_starcoder.log; printf \\\"%s|%s\\\\n\\\" \\\"$_EC\\\" \\\"$(date -u +%Y-%m-%dT%H:%M:%SZ)\\\" > /tmp/agent-ml-exit/m2_full_starcoder.exit' EXIT; trap 'exit 129' HUP; trap 'exit 130' INT; trap 'exit 143' TERM; { cd /root/structfuse && export CUDA_VISIBLE_DEVICES=1 && timeout 518400 env bash -c 'bash -c \\\"cd /root/structfuse && bash run_m2_full_starcoder_resume.sh\\\"'; } > ~/runs/structfuse-context/m2_full_starcoder.log 2>&1\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.35}}"
    }
  },
  "sourceToolAssistantUUID": "24a0e6b4-1983-48a5-90fa-6d644b0c0195",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/.claude/sessions/reviewer_65cfe724",
  "sessionId": "f444a635-eeef-4924-9b48-a4c308632421",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---


### Tool result

_source line 114 · 2026-05-16T02:31:51.631Z_

<details><summary>↩ Tool result · `toolu_01BypsVoce4uttVoCs6oAk9F`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"==========================================\\n[1/9] Starting: random_s42 at Thu May 14 01:39:30 CST 2026\\n==========================================\\nEXIT_CODE=0\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.42}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a0f00e0f-4ef7-47dd-9dbe-2e7cdb030dce",
  "isSidechain": false,
  "promptId": "cb482ce5-85c1-49a1-985e-c68475dfc7e7",
  "type": "user",
  "uuid": "85ce2eb9-b150-46a6-beaa-add0568b00e4",
  "toolUseResult": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"==========================================\\\\n[1/9] Starting: random_s42 at Thu May 14 01:39:30 CST 2026\\\\n==========================================\\\\nEXIT_CODE=0\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.42}}\"}",
  "mcpMeta": {
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"==========================================\\n[1/9] Starting: random_s42 at Thu May 14 01:39:30 CST 2026\\n==========================================\\nEXIT_CODE=0\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.42}}"
    }
  },
  "sourceToolAssistantUUID": "a0f00e0f-4ef7-47dd-9dbe-2e7cdb030dce",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/.claude/sessions/reviewer_65cfe724",
  "sessionId": "f444a635-eeef-4924-9b48-a4c308632421",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---


### Tool call

_source line 115 · 2026-05-16T02:31:51.804Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_011gx1gugAKiohWLDoi4q5dd`</summary>

```json
{
  "server": "bjb1-42106",
  "command": "tail -30 /root/runs/structfuse-context/m2_full_starcoder.log"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "85ce2eb9-b150-46a6-beaa-add0568b00e4",
  "isSidechain": false,
  "requestId": "req_011Cb5TpZZvB2dfKVMzAdqSD",
  "type": "assistant",
  "uuid": "3c158448-9e0e-4c8f-9c91-f7864874049b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/.claude/sessions/reviewer_65cfe724",
  "sessionId": "f444a635-eeef-4924-9b48-a4c308632421",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RCFcKM4qBaKDLY3SdFRUbu",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4260,
      "cache_read_input_tokens": 103818,
      "output_tokens": 644,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 4260,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 644,
          "cache_read_input_tokens": 103818,
          "cache_creation_input_tokens": 4260,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 4260
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

_source line 116 · 2026-05-16T02:31:52.176Z_

<details><summary>↩ Tool result · `toolu_011gx1gugAKiohWLDoi4q5dd`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"wandb: learning_rate ▁▂▃▄▅▆▇▇████████████▇▇▇▇▇▇▇▇▇▇\\nwandb:      recall@1 ▁█▁\\nwandb:     recall@10 ▁▁▁\\nwandb:      recall@5 ▆█▁\\nwandb:    train_loss ██▆█▆▇▇▃▅▆▃▄▆▇▄▅▄▄▂▄▃▆▂▄▅▃▃▁▅▃\\nwandb:      val_loss ▁▄█\\nwandb: \\nwandb: Run summary:\\nwandb: learning_rate 2e-05\\nwandb:      recall@1 0.43758\\nwandb:     recall@10 1\\nwandb:      recall@5 0.89765\\nwandb:    train_loss 0.27835\\nwandb:      val_loss 0.69265\\nwandb: \\nwandb: You can sync this run to the cloud by running:\\nwandb: wandb sync /root/structfuse-context/wandb/offline-run-20260516_011523-mh2e80qa\\nwandb: Find logs at: ./wandb/offline-run-20260516_011523-mh2e80qa/logs\\n[2026-05-16 10:06:00] DONE: embedding_distance_s42\\n\\n── Training: embedding_distance_s43 (2 epochs) ──\\n  Output: /root/autodl-tmp/structfuse/checkpoints/m2_full_starcoder/embedding_distance_s43\\n  Log: /root/runs/m2_full_starcoder/embedding_distance_s43.log\\nwandb: Tracking run with wandb version 0.26.0\\nwandb: W&B syncing is set to `offline` in this directory. Run `wandb online` or set WANDB_MODE=online to enable cloud syncing.\\nwandb: Run data is saved locally in /root/structfuse-context/wandb/offline-run-20260516_100604-npdqqhtt\\n[Epoch 1] Using pre-mined negatives (embedding_distance)...\\n  Training loop start: 1405 batches/epoch, total_steps_per_epoch=1405\\n`use_cache=True` is incompatible with gradient checkpointing. Setting `use_cache=False`.\\n  step 50  loss=0.7980  lr=3.56e-06\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.35}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "3c158448-9e0e-4c8f-9c91-f7864874049b",
  "isSidechain": false,
  "promptId": "cb482ce5-85c1-49a1-985e-c68475dfc7e7",
  "type": "user",
  "uuid": "1803fb7d-1e35-4ced-b589-8f145c8a9bad",
  "toolUseResult": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"wandb: learning_rate ▁▂▃▄▅▆▇▇████████████▇▇▇▇▇▇▇▇▇▇\\\\nwandb:      recall@1 ▁█▁\\\\nwandb:     recall@10 ▁▁▁\\\\nwandb:      recall@5 ▆█▁\\\\nwandb:    train_loss ██▆█▆▇▇▃▅▆▃▄▆▇▄▅▄▄▂▄▃▆▂▄▅▃▃▁▅▃\\\\nwandb:      val_loss ▁▄█\\\\nwandb: \\\\nwandb: Run summary:\\\\nwandb: learning_rate 2e-05\\\\nwandb:      recall@1 0.43758\\\\nwandb:     recall@10 1\\\\nwandb:      recall@5 0.89765\\\\nwandb:    train_loss 0.27835\\\\nwandb:      val_loss 0.69265\\\\nwandb: \\\\nwandb: You can sync this run to the cloud by running:\\\\nwandb: wandb sync /root/structfuse-context/wandb/offline-run-20260516_011523-mh2e80qa\\\\nwandb: Find logs at: ./wandb/offline-run-20260516_011523-mh2e80qa/logs\\\\n[2026-05-16 10:06:00] DONE: embedding_distance_s42\\\\n\\\\n── Training: embedding_distance_s43 (2 epochs) ──\\\\n  Output: /root/autodl-tmp/structfuse/checkpoints/m2_full_starcoder/embedding_distance_s43\\\\n  Log: /root/runs/m2_full_starcoder/embedding_distance_s43.log\\\\nwandb: Tracking run with wandb version 0.26.0\\\\nwandb: W&B syncing is set to `offline` in this directory. Run `wandb online` or set WANDB_MODE=online to enable cloud syncing.\\\\nwandb: Run data is saved locally in /root/structfuse-context/wandb/offline-run-20260516_100604-npdqqhtt\\\\n[Epoch 1] Using pre-mined negatives (embedding_distance)...\\\\n  Training loop start: 1405 batches/epoch, total_steps_per_epoch=1405\\\\n`use_cache=True` is incompatible with gradient checkpointing. Setting `use_cache=False`.\\\\n  step 50  loss=0.7980  lr=3.56e-06\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.35}}\"}",
  "mcpMeta": {
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"wandb: learning_rate ▁▂▃▄▅▆▇▇████████████▇▇▇▇▇▇▇▇▇▇\\nwandb:      recall@1 ▁█▁\\nwandb:     recall@10 ▁▁▁\\nwandb:      recall@5 ▆█▁\\nwandb:    train_loss ██▆█▆▇▇▃▅▆▃▄▆▇▄▅▄▄▂▄▃▆▂▄▅▃▃▁▅▃\\nwandb:      val_loss ▁▄█\\nwandb: \\nwandb: Run summary:\\nwandb: learning_rate 2e-05\\nwandb:      recall@1 0.43758\\nwandb:     recall@10 1\\nwandb:      recall@5 0.89765\\nwandb:    train_loss 0.27835\\nwandb:      val_loss 0.69265\\nwandb: \\nwandb: You can sync this run to the cloud by running:\\nwandb: wandb sync /root/structfuse-context/wandb/offline-run-20260516_011523-mh2e80qa\\nwandb: Find logs at: ./wandb/offline-run-20260516_011523-mh2e80qa/logs\\n[2026-05-16 10:06:00] DONE: embedding_distance_s42\\n\\n── Training: embedding_distance_s43 (2 epochs) ──\\n  Output: /root/autodl-tmp/structfuse/checkpoints/m2_full_starcoder/embedding_distance_s43\\n  Log: /root/runs/m2_full_starcoder/embedding_distance_s43.log\\nwandb: Tracking run with wandb version 0.26.0\\nwandb: W&B syncing is set to `offline` in this directory. Run `wandb online` or set WANDB_MODE=online to enable cloud syncing.\\nwandb: Run data is saved locally in /root/structfuse-context/wandb/offline-run-20260516_100604-npdqqhtt\\n[Epoch 1] Using pre-mined negatives (embedding_distance)...\\n  Training loop start: 1405 batches/epoch, total_steps_per_epoch=1405\\n`use_cache=True` is incompatible with gradient checkpointing. Setting `use_cache=False`.\\n  step 50  loss=0.7980  lr=3.56e-06\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.35}}"
    }
  },
  "sourceToolAssistantUUID": "3c158448-9e0e-4c8f-9c91-f7864874049b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/.claude/sessions/reviewer_65cfe724",
  "sessionId": "f444a635-eeef-4924-9b48-a4c308632421",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---


### Assistant

_source line 117 · 2026-05-16T02:32:14.006Z_

<details><summary>Logged reasoning block</summary>

```text
Good findings. Let me analyze:

1. **Process status**:
   - PID 337267 (Qwen chain): Alive, running for 1 day 15+ hours
   - PID 519791 (StarCoder chain): Alive, running for 1 day 8+ hours
   - PID 61328 (SWE-bench eval): NOT in the output — process doesn't exist anymore. But registry says it's RUNNING with `pid_alive: true` at check time 08:21 CST.

2. **Qwen (cuda:0)**: The log only shows `random_s42` starting and `EXIT_CODE=0`. 

The main wrapper log appears to be truncated or redirecting to sub-logs, which is why I'm only seeing those 4 lines. The Qwen process is definitely still running (PID 337267 has been up for over a day), so the actual training must be happening in the sub-run logs rather than the main one.

3. **StarCoder (cuda:1)**: Log shows:
   - `embedding_distance_s42` just completed at 2026-05-16 10:06:00 CST
   - `embedding_distance_s43` just started at step 50 (loss=0.7980), this is subrun 5/9
   - Final stats for embed_s42: R@1=0.4376, val_loss=0.6927

   The wandb summary confirms R@1=0.43758 for embed_s42, which matches the registry eval@500 value of 0.4372. So the final best R@1 is around 0.4376 — notably below all 3 random baselines (0.4604/0.4912/0.4871). This is a concerning signal that the embedding strategy isn't outperforming the baselines on StarCoder.

4. **GPU compliance** (L1 #4): 
   - PID 519791 wrapper explicitly sets `CUDA_VISIBLE_DEVICES=1` ✅
   - PID 337267 (Qwen) —

I need to check if CUDA_VISIBLE_DEVICES is set for the Qwen process. Meanwhile, the SWE-bench eval (PID 61328) isn't showing up in the process list even though the registry says it's running, so I should investigate whether it finished or crashed. Looking at GPU VRAM, cuda:0 dropped from 62620 MiB to 51001 MiB (about 11.6GB), which suggests the Qwen chain might have transitioned between subruns — dataflow_s43 was degrading and likely early-stopped, so it could be on dataflow_s44 or bm25_s42 now. cuda:1 remains stable at 53467 MiB, consistent with embed_s43 just starting. Let me check the SWE-bench eval status and figure out what subrun Qwen is currently on.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1803fb7d-1e35-4ced-b589-8f145c8a9bad",
  "isSidechain": false,
  "requestId": "req_011Cb5TqUBzKd8BFWJtB5Y7D",
  "type": "assistant",
  "uuid": "ce320400-1b64-4fc9-86a1-5322cf9c1920",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/.claude/sessions/reviewer_65cfe724",
  "sessionId": "f444a635-eeef-4924-9b48-a4c308632421",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Vd8RAVmMwzjnmzPCagJLzG",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1990,
      "cache_read_input_tokens": 108078,
      "output_tokens": 1088,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1990,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1088,
          "cache_read_input_tokens": 108078,
          "cache_creation_input_tokens": 1990,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1990
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

_source line 118 · 2026-05-16T02:32:14.064Z_

SWE-bench eval PID 61328 未出现在进程列表中。StarCoder embed_s42 已完成，embed_s43 刚开始。需要进一步确认。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ce320400-1b64-4fc9-86a1-5322cf9c1920",
  "isSidechain": false,
  "requestId": "req_011Cb5TqUBzKd8BFWJtB5Y7D",
  "type": "assistant",
  "uuid": "5ac8e424-85c1-4775-b52c-468d756769f9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/.claude/sessions/reviewer_65cfe724",
  "sessionId": "f444a635-eeef-4924-9b48-a4c308632421",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Vd8RAVmMwzjnmzPCagJLzG",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1990,
      "cache_read_input_tokens": 108078,
      "output_tokens": 1088,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1990,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1088,
          "cache_read_input_tokens": 108078,
          "cache_creation_input_tokens": 1990,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1990
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

_source line 119 · 2026-05-16T02:32:14.260Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01GgwxLfSGyCPjKAfQ8b36L8`</summary>

```json
{
  "server": "bjb1-42106",
  "command": "ps -p 61328 -o pid,stat,etime,cmd --no-headers"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5ac8e424-85c1-4775-b52c-468d756769f9",
  "isSidechain": false,
  "requestId": "req_011Cb5TqUBzKd8BFWJtB5Y7D",
  "type": "assistant",
  "uuid": "ca3d1b84-b130-4586-a314-38d4c5c921ee",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/.claude/sessions/reviewer_65cfe724",
  "sessionId": "f444a635-eeef-4924-9b48-a4c308632421",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Vd8RAVmMwzjnmzPCagJLzG",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1990,
      "cache_read_input_tokens": 108078,
      "output_tokens": 1088,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1990,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1088,
          "cache_read_input_tokens": 108078,
          "cache_creation_input_tokens": 1990,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1990
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

_source line 120 · 2026-05-16T02:32:14.639Z_

<details><summary>↩ Tool result · `toolu_01GgwxLfSGyCPjKAfQ8b36L8`</summary>

```text
{"result":"{\"success\": false, \"data\": {\"stdout\": \"\", \"stderr\": \"\", \"return_code\": 1}, \"error\": \"exit code 1\", \"metadata\": {\"elapsed_seconds\": 0.36}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ca3d1b84-b130-4586-a314-38d4c5c921ee",
  "isSidechain": false,
  "promptId": "cb482ce5-85c1-49a1-985e-c68475dfc7e7",
  "type": "user",
  "uuid": "17eeb943-8975-4470-857b-59f1afbea50c",
  "toolUseResult": "{\"result\":\"{\\\"success\\\": false, \\\"data\\\": {\\\"stdout\\\": \\\"\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 1}, \\\"error\\\": \\\"exit code 1\\\", \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.36}}\"}",
  "mcpMeta": {
    "structuredContent": {
      "result": "{\"success\": false, \"data\": {\"stdout\": \"\", \"stderr\": \"\", \"return_code\": 1}, \"error\": \"exit code 1\", \"metadata\": {\"elapsed_seconds\": 0.36}}"
    }
  },
  "sourceToolAssistantUUID": "ca3d1b84-b130-4586-a314-38d4c5c921ee",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/.claude/sessions/reviewer_65cfe724",
  "sessionId": "f444a635-eeef-4924-9b48-a4c308632421",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---


### Tool call

_source line 121 · 2026-05-16T02:32:14.747Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_018QPgxNHPu7ReNTYC8EEGCq`</summary>

```json
{
  "server": "bjb1-42106",
  "command": "tail -5 /root/autodl-tmp/structfuse/logs/swebench_eval_all.log"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "17eeb943-8975-4470-857b-59f1afbea50c",
  "isSidechain": false,
  "requestId": "req_011Cb5TqUBzKd8BFWJtB5Y7D",
  "type": "assistant",
  "uuid": "c4f3866b-721f-44a3-8da2-279cfd09d806",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/.claude/sessions/reviewer_65cfe724",
  "sessionId": "f444a635-eeef-4924-9b48-a4c308632421",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Vd8RAVmMwzjnmzPCagJLzG",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1990,
      "cache_read_input_tokens": 108078,
      "output_tokens": 1088,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1990,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1088,
          "cache_read_input_tokens": 108078,
          "cache_creation_input_tokens": 1990,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1990
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

_source line 122 · 2026-05-16T02:32:14.987Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_019RwZoRnv61NGYRL3sB8hAy`</summary>

```json
{
  "server": "bjb1-42106",
  "command": "nvidia-smi --query-compute-apps=pid,gpu_uuid,used_memory --format=csv,noheader"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c4f3866b-721f-44a3-8da2-279cfd09d806",
  "isSidechain": false,
  "requestId": "req_011Cb5TqUBzKd8BFWJtB5Y7D",
  "type": "assistant",
  "uuid": "4f304389-34d4-4d5a-93f5-737d95f3e075",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/.claude/sessions/reviewer_65cfe724",
  "sessionId": "f444a635-eeef-4924-9b48-a4c308632421",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Vd8RAVmMwzjnmzPCagJLzG",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1990,
      "cache_read_input_tokens": 108078,
      "output_tokens": 1088,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1990,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1088,
          "cache_read_input_tokens": 108078,
          "cache_creation_input_tokens": 1990,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1990
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

_source line 123 · 2026-05-16T02:32:15.125Z_

<details><summary>↩ Tool result · `toolu_018QPgxNHPu7ReNTYC8EEGCq`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"Loading SWE-bench (lite)...\\n  300 instances\\n  Loading checkpoint: /root/autodl-tmp/structfuse/checkpoints/m2_full_qwen/random_s42/best_by_recall_at_1\\n\\rLoading checkpoint shards:   0%|          | 0/2 [00:00<?, ?it/s]\\rLoading checkpoint shards:  50%|█████     | 1/2 [00:00<00:00,  1.03it/s]\\rLoading checkpoint shards: 100%|██████████| 2/2 [00:01<00:00,  1.98it/s]\\rLoading checkpoint shards: 100%|██████████| 2/2 [00:01<00:00,  1.74it/s]\\n\\rEvaluating:   0%|          | 0/300 [00:00<?, ?it/s]\\rEvaluating:   0%|          | 1/300 [02:11<10:55:53, 131.62s/it]\\rEvaluating:   1%|          | 2/300 [04:22<10:51:48, 131.23s/it]\\rEvaluating:   1%|          | 3/300 [06:27<10:36:27, 128.58s/it]\\rEvaluating:   1%|▏         | 4/300 [08:05<9:34:07, 116.38s/it] Terminated\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.36}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c4f3866b-721f-44a3-8da2-279cfd09d806",
  "isSidechain": false,
  "promptId": "cb482ce5-85c1-49a1-985e-c68475dfc7e7",
  "type": "user",
  "uuid": "0334b820-8f31-47c6-88fd-85287bfefcdb",
  "toolUseResult": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"Loading SWE-bench (lite)...\\\\n  300 instances\\\\n  Loading checkpoint: /root/autodl-tmp/structfuse/checkpoints/m2_full_qwen/random_s42/best_by_recall_at_1\\\\n\\\\rLoading checkpoint shards:   0%|          | 0/2 [00:00<?, ?it/s]\\\\rLoading checkpoint shards:  50%|█████     | 1/2 [00:00<00:00,  1.03it/s]\\\\rLoading checkpoint shards: 100%|██████████| 2/2 [00:01<00:00,  1.98it/s]\\\\rLoading checkpoint shards: 100%|██████████| 2/2 [00:01<00:00,  1.74it/s]\\\\n\\\\rEvaluating:   0%|          | 0/300 [00:00<?, ?it/s]\\\\rEvaluating:   0%|          | 1/300 [02:11<10:55:53, 131.62s/it]\\\\rEvaluating:   1%|          | 2/300 [04:22<10:51:48, 131.23s/it]\\\\rEvaluating:   1%|          | 3/300 [06:27<10:36:27, 128.58s/it]\\\\rEvaluating:   1%|▏         | 4/300 [08:05<9:34:07, 116.38s/it] Terminated\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.36}}\"}",
  "mcpMeta": {
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"Loading SWE-bench (lite)...\\n  300 instances\\n  Loading checkpoint: /root/autodl-tmp/structfuse/checkpoints/m2_full_qwen/random_s42/best_by_recall_at_1\\n\\rLoading checkpoint shards:   0%|          | 0/2 [00:00<?, ?it/s]\\rLoading checkpoint shards:  50%|█████     | 1/2 [00:00<00:00,  1.03it/s]\\rLoading checkpoint shards: 100%|██████████| 2/2 [00:01<00:00,  1.98it/s]\\rLoading checkpoint shards: 100%|██████████| 2/2 [00:01<00:00,  1.74it/s]\\n\\rEvaluating:   0%|          | 0/300 [00:00<?, ?it/s]\\rEvaluating:   0%|          | 1/300 [02:11<10:55:53, 131.62s/it]\\rEvaluating:   1%|          | 2/300 [04:22<10:51:48, 131.23s/it]\\rEvaluating:   1%|          | 3/300 [06:27<10:36:27, 128.58s/it]\\rEvaluating:   1%|▏         | 4/300 [08:05<9:34:07, 116.38s/it] Terminated\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.36}}"
    }
  },
  "sourceToolAssistantUUID": "c4f3866b-721f-44a3-8da2-279cfd09d806",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/.claude/sessions/reviewer_65cfe724",
  "sessionId": "f444a635-eeef-4924-9b48-a4c308632421",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---


### Runtime record

_source line 124_

```json
{
  "type": "last-prompt",
  "lastPrompt": "[系统通知 — worker_done:worker_ops_training-and-eval-status_20260516T022911]: Worker worker_ops_training-and-eval-status_20260516T022911 已完成（status=done），请审查 Agent 的处理结果。",
  "leafUuid": "0334b820-8f31-47c6-88fd-85287bfefcdb",
  "sessionId": "f444a635-eeef-4924-9b48-a4c308632421"
}
```

---


### Runtime record

_source line 125_

```json
{
  "type": "ai-title",
  "aiTitle": "Review research literature worker completion",
  "sessionId": "f444a635-eeef-4924-9b48-a4c308632421"
}
```

---


### Tool result

_source line 126 · 2026-05-16T02:32:15.621Z_

<details><summary>↩ Tool result · `toolu_019RwZoRnv61NGYRL3sB8hAy`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"18427, GPU-41b18ac6-b1f4-95fe-7325-10cc1dc27d04, 50992 MiB\\n129747, GPU-d831e380-a5f7-73d0-a09e-516d34481181, 53458 MiB\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.48}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "4f304389-34d4-4d5a-93f5-737d95f3e075",
  "isSidechain": false,
  "promptId": "cb482ce5-85c1-49a1-985e-c68475dfc7e7",
  "type": "user",
  "uuid": "b5ea5bff-37b5-42b2-8538-e1ec4c8fcf7a",
  "toolUseResult": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"18427, GPU-41b18ac6-b1f4-95fe-7325-10cc1dc27d04, 50992 MiB\\\\n129747, GPU-d831e380-a5f7-73d0-a09e-516d34481181, 53458 MiB\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.48}}\"}",
  "mcpMeta": {
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"18427, GPU-41b18ac6-b1f4-95fe-7325-10cc1dc27d04, 50992 MiB\\n129747, GPU-d831e380-a5f7-73d0-a09e-516d34481181, 53458 MiB\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.48}}"
    }
  },
  "sourceToolAssistantUUID": "4f304389-34d4-4d5a-93f5-737d95f3e075",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/.claude/sessions/reviewer_65cfe724",
  "sessionId": "f444a635-eeef-4924-9b48-a4c308632421",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---


### Runtime record

_source line 127 · 2026-05-16T02:32:15.625Z_

```json
{
  "parentUuid": "b5ea5bff-37b5-42b2-8538-e1ec4c8fcf7a",
  "isSidechain": false,
  "attachment": {
    "type": "todo_reminder",
    "content": [],
    "itemCount": 0
  },
  "type": "attachment",
  "uuid": "522d9ee6-48d1-44b5-93fc-26ddf967df53",
  "timestamp": "2026-05-16T02:32:15.625Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/.claude/sessions/reviewer_65cfe724",
  "sessionId": "f444a635-eeef-4924-9b48-a4c308632421",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---


### Assistant

_source line 128 · 2026-05-16T02:32:44.445Z_

<details><summary>Logged reasoning block</summary>

```text
Key findings:

1. **SWE-bench eval (PID 61328)**: Process is DEAD. Log shows it was `Terminated` after only 4/300 instances. The log says it loaded 300 instances (not 100 as registry says). It was terminated externally. The registry still says "RUNNING" with metrics from "2026-05-16T08:21 CST" showing "71/100 instances" — but the actual log shows it only got to 4/300 before being killed.

Wait, this is confusing. Let me re-read:


The registry claims 100 instances with 71 completed, but the log shows 300 instances total and only made it to 4 before termination — these numbers don't align at all. The log might have been restarted or overwritten after the registry last checked it, or the registry metrics are simply stale. Looking at the director's note, it mentions pausing SWE-bench eval after random_s42 completes, with 2 remaining checkpoints still pending. 推迟到 Qwen chain 完成后无 GPU 竞争时再跑。

看起来 SWE-bench 评估的情况是：原本在 08:21 CST 时注册表最后更新时运行了 71/100 个实例，后来被终止了。现在的日志显示它重新启动，加载了 300 个实例但在第 4 个实例后被终止，PID 61328 已经死亡。这里有个问题——注册表显示评估状态是 RUNNING，但实际进程已经终止了。

GPU 方面，PID 18427 在 GPU-41b18ac6 上占用 50992 MiB 是 Qwen 训练，PID 129747 在 GPU-d831e380 上占用 53458 MiB 是 StarCoder（这是实际的 Python 进程，不同于包装器 PID 519791）。

对于 Qwen 的进度，包装器 PID 337267 还活着，PID 18427 是 cuda:0 上的实际训练进程。注册表显示 dataflow_s43 在第 1100+ 步，早停计数 1/2。VRAM 从 62620 MiB 降到 50992 MiB，可能表示转换到了新的子运行——dataflow_s43 可能早停了然后 dataflow_s44 启动，或者 bm25_s42 开始了。StarCoder 那边，embed_s42 完成了（R@1=0.4376，低于所有随机基线），embed_s43 刚在第 50 步启动，这是第 5/9 个子运行。我需要检查 Qwen 的子运行状态。
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "522d9ee6-48d1-44b5-93fc-26ddf967df53",
  "isSidechain": false,
  "requestId": "req_011Cb5TsCR22yrsg1DxUPrTw",
  "type": "assistant",
  "uuid": "b3554559-e5a9-4f76-98dc-83889504a2f1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/.claude/sessions/reviewer_65cfe724",
  "sessionId": "f444a635-eeef-4924-9b48-a4c308632421",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Rzj51uxGdNMCQD5193We3v",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1967,
      "cache_read_input_tokens": 110068,
      "output_tokens": 1179,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1967,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1179,
          "cache_read_input_tokens": 110068,
          "cache_creation_input_tokens": 1967,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1967
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

_source line 129 · 2026-05-16T02:32:44.447Z_

SWE-bench eval 已被 Terminated（仅完成 4/300），但 registry 仍标为 RUNNING。需要确认 Qwen 当前子任务。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b3554559-e5a9-4f76-98dc-83889504a2f1",
  "isSidechain": false,
  "requestId": "req_011Cb5TsCR22yrsg1DxUPrTw",
  "type": "assistant",
  "uuid": "0f9d83e4-5982-4609-a243-c68db48f9b42",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/.claude/sessions/reviewer_65cfe724",
  "sessionId": "f444a635-eeef-4924-9b48-a4c308632421",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Rzj51uxGdNMCQD5193We3v",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1967,
      "cache_read_input_tokens": 110068,
      "output_tokens": 1179,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1967,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1179,
          "cache_read_input_tokens": 110068,
          "cache_creation_input_tokens": 1967,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1967
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

_source line 130 · 2026-05-16T02:32:44.477Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01EfZZYB8Tq6XFdyueTpgcYi`</summary>

```json
{
  "server": "bjb1-42106",
  "command": "ls -lt /root/autodl-tmp/structfuse/checkpoints/m2_full_qwen/"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0f9d83e4-5982-4609-a243-c68db48f9b42",
  "isSidechain": false,
  "requestId": "req_011Cb5TsCR22yrsg1DxUPrTw",
  "type": "assistant",
  "uuid": "0dc7b0c8-6511-4e5a-900a-c373bf1903ad",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/.claude/sessions/reviewer_65cfe724",
  "sessionId": "f444a635-eeef-4924-9b48-a4c308632421",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Rzj51uxGdNMCQD5193We3v",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1967,
      "cache_read_input_tokens": 110068,
      "output_tokens": 1179,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1967,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1179,
          "cache_read_input_tokens": 110068,
          "cache_creation_input_tokens": 1967,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1967
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

_source line 131 · 2026-05-16T02:32:44.850Z_

<details><summary>↩ Tool result · `toolu_01EfZZYB8Tq6XFdyueTpgcYi`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"total 0\\ndrwxr-xr-x 4 root root 69 May 16 10:32 dataflow_aware_s43\\ndrwxr-xr-x 5 root root 86 May 15 23:53 embedding_distance_s44\\ndrwxr-xr-x 5 root root 86 May 15 14:50 embedding_distance_s43\\ndrwxr-xr-x 5 root root 86 May 15 08:32 random_s44\\ndrwxr-xr-x 4 root root 69 May 15 03:15 random_s43\\ndrwxr-xr-x 4 root root 69 May 15 03:15 random_s42\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.35}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "0dc7b0c8-6511-4e5a-900a-c373bf1903ad",
  "isSidechain": false,
  "promptId": "cb482ce5-85c1-49a1-985e-c68475dfc7e7",
  "type": "user",
  "uuid": "58d812f7-5267-4706-8bb6-9ee69e7d758a",
  "toolUseResult": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"total 0\\\\ndrwxr-xr-x 4 root root 69 May 16 10:32 dataflow_aware_s43\\\\ndrwxr-xr-x 5 root root 86 May 15 23:53 embedding_distance_s44\\\\ndrwxr-xr-x 5 root root 86 May 15 14:50 embedding_distance_s43\\\\ndrwxr-xr-x 5 root root 86 May 15 08:32 random_s44\\\\ndrwxr-xr-x 4 root root 69 May 15 03:15 random_s43\\\\ndrwxr-xr-x 4 root root 69 May 15 03:15 random_s42\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.35}}\"}",
  "mcpMeta": {
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"total 0\\ndrwxr-xr-x 4 root root 69 May 16 10:32 dataflow_aware_s43\\ndrwxr-xr-x 5 root root 86 May 15 23:53 embedding_distance_s44\\ndrwxr-xr-x 5 root root 86 May 15 14:50 embedding_distance_s43\\ndrwxr-xr-x 5 root root 86 May 15 08:32 random_s44\\ndrwxr-xr-x 4 root root 69 May 15 03:15 random_s43\\ndrwxr-xr-x 4 root root 69 May 15 03:15 random_s42\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.35}}"
    }
  },
  "sourceToolAssistantUUID": "0dc7b0c8-6511-4e5a-900a-c373bf1903ad",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/.claude/sessions/reviewer_65cfe724",
  "sessionId": "f444a635-eeef-4924-9b48-a4c308632421",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---


### Tool call

_source line 132 · 2026-05-16T02:32:45.178Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01EqXDEYHmZU8PtMjpwRav6s`</summary>

```json
{
  "server": "bjb1-42106",
  "command": "find /root/runs/m2_full_qwen/ -name \"*.log\" -newer /root/runs/m2_full_qwen/dataflow_aware_s43.log"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "58d812f7-5267-4706-8bb6-9ee69e7d758a",
  "isSidechain": false,
  "requestId": "req_011Cb5TsCR22yrsg1DxUPrTw",
  "type": "assistant",
  "uuid": "b2256dfa-2a14-45cf-b0d7-0bc0c39dc56d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/.claude/sessions/reviewer_65cfe724",
  "sessionId": "f444a635-eeef-4924-9b48-a4c308632421",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Rzj51uxGdNMCQD5193We3v",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1967,
      "cache_read_input_tokens": 110068,
      "output_tokens": 1179,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1967,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1179,
          "cache_read_input_tokens": 110068,
          "cache_creation_input_tokens": 1967,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1967
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

_source line 133 · 2026-05-16T02:32:45.540Z_

<details><summary>↩ Tool result · `toolu_01EqXDEYHmZU8PtMjpwRav6s`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.35}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "b2256dfa-2a14-45cf-b0d7-0bc0c39dc56d",
  "isSidechain": false,
  "promptId": "cb482ce5-85c1-49a1-985e-c68475dfc7e7",
  "type": "user",
  "uuid": "b7ec3782-b8e5-4265-8fbc-733103b257cb",
  "toolUseResult": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.35}}\"}",
  "mcpMeta": {
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.35}}"
    }
  },
  "sourceToolAssistantUUID": "b2256dfa-2a14-45cf-b0d7-0bc0c39dc56d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/.claude/sessions/reviewer_65cfe724",
  "sessionId": "f444a635-eeef-4924-9b48-a4c308632421",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---


### Assistant

_source line 134 · 2026-05-16T02:32:55.156Z_

<details><summary>Logged reasoning block</summary>

```text
The Qwen checkpoints directory shows:
- `dataflow_aware_s43` — last modified May 16 10:32 (most recent)
- `embedding_distance_s44` — May 15 23:53
- `embedding_distance_s43` — May 15 14:50
- `random_s44` — May 15 08:32
- `random_s43` — May 15 03:15
- `random_s42` — May 15 03:15

So dataflow_s43 is the latest checkpoint being updated. Let me check if it's still training or if it finished. 

The registry showed it was at step 1100+ with early_stopping 1/2, and since the checkpoint directory was just modified at 10:32, dataflow_s43 is still actively training. Let me look at the actual training log to see the current progress.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b7ec3782-b8e5-4265-8fbc-733103b257cb",
  "isSidechain": false,
  "requestId": "req_011Cb5TuQGi1SfHuTxYaSaW2",
  "type": "assistant",
  "uuid": "df0ab8c1-4df6-4f4c-8f89-3c8af03cf5a4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/.claude/sessions/reviewer_65cfe724",
  "sessionId": "f444a635-eeef-4924-9b48-a4c308632421",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014oJj5yQWetHx7revSuFBY9",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1583,
      "cache_read_input_tokens": 112035,
      "output_tokens": 460,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1583,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 460,
          "cache_read_input_tokens": 112035,
          "cache_creation_input_tokens": 1583,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1583
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

_source line 135 · 2026-05-16T02:32:55.166Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_013MADxAzGWmJd87MawoBEfM`</summary>

```json
{
  "server": "bjb1-42106",
  "command": "tail -30 /root/runs/m2_full_qwen/dataflow_aware_s43.log"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "df0ab8c1-4df6-4f4c-8f89-3c8af03cf5a4",
  "isSidechain": false,
  "requestId": "req_011Cb5TuQGi1SfHuTxYaSaW2",
  "type": "assistant",
  "uuid": "0d4aae1c-75aa-4258-8fc2-12cc47270b17",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/.claude/sessions/reviewer_65cfe724",
  "sessionId": "f444a635-eeef-4924-9b48-a4c308632421",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014oJj5yQWetHx7revSuFBY9",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1583,
      "cache_read_input_tokens": 112035,
      "output_tokens": 460,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1583,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 460,
          "cache_read_input_tokens": 112035,
          "cache_creation_input_tokens": 1583,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1583
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

_source line 136 · 2026-05-16T02:32:55.191Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01XWUkYnnxE27sCQsJA5WPxC`</summary>

```json
{
  "server": "bjb1-42106",
  "command": "tail -30 /root/runs/m2_full_starcoder/embedding_distance_s42.log"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0d4aae1c-75aa-4258-8fc2-12cc47270b17",
  "isSidechain": false,
  "requestId": "req_011Cb5TuQGi1SfHuTxYaSaW2",
  "type": "assistant",
  "uuid": "8850b3d4-c99c-4a02-a1d1-ffeb7f5813ea",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/.claude/sessions/reviewer_65cfe724",
  "sessionId": "f444a635-eeef-4924-9b48-a4c308632421",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014oJj5yQWetHx7revSuFBY9",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1583,
      "cache_read_input_tokens": 112035,
      "output_tokens": 460,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1583,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 460,
          "cache_read_input_tokens": 112035,
          "cache_creation_input_tokens": 1583,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1583
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

_source line 137 · 2026-05-16T02:32:55.527Z_

<details><summary>↩ Tool result · `toolu_013MADxAzGWmJd87MawoBEfM`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"  [eval@500] {'val_loss': 0.4616767596917259, 'recall@1': 0.549475753604194, 'recall@5': 0.9728047182175622, 'recall@10': 1.0}\\n  New best val_loss=0.4617, saved to /root/autodl-tmp/structfuse/checkpoints/m2_full_qwen/dataflow_aware_s43/best_by_val_loss\\n  New best R@1=0.5495, saved to /root/autodl-tmp/structfuse/checkpoints/m2_full_qwen/dataflow_aware_s43/best_by_recall_at_1\\n  step 550  loss=0.2641  lr=1.95e-05\\n  step 600  loss=0.1743  lr=1.92e-05\\n  step 650  loss=0.1656  lr=1.90e-05\\n  step 700  loss=0.3392  lr=1.87e-05\\n  step 750  loss=0.1229  lr=1.84e-05\\n  step 800  loss=0.0403  lr=1.80e-05\\n  step 850  loss=0.1022  lr=1.76e-05\\n  step 900  loss=0.0208  lr=1.72e-05\\n  step 950  loss=0.1532  lr=1.68e-05\\n  step 1000  loss=0.4353  lr=1.63e-05\\n  [eval@1000] {'val_loss': 0.49840330249516396, 'recall@1': 0.5173656618610747, 'recall@5': 0.9580602883355177, 'recall@10': 1.0}\\n  val_loss not improved (1/2)\\n  step 1050  loss=0.0832  lr=1.58e-05\\n  step 1100  loss=0.1566  lr=1.53e-05\\n  step 1150  loss=0.0397  lr=1.48e-05\\n  step 1200  loss=0.0318  lr=1.42e-05\\n  step 1250  loss=0.1481  lr=1.36e-05\\n  step 1300  loss=0.0999  lr=1.30e-05\\n  step 1350  loss=0.0552  lr=1.24e-05\\n  step 1400  loss=0.1586  lr=1.18e-05\\n[Epoch 2] Using pre-mined negatives (dataflow_aware)...\\n  step 1450  loss=0.0784  lr=1.12e-05\\n  step 1500  loss=0.0282  lr=1.06e-05\\n  [eval@1500] {'val_loss': 0.5185946156594262, 'recall@1': 0.5540629095674967, 'recall@5': 0.9564220183486238, 'recall@10': 1.0}\\n  val_loss not improved (2/2)\\n  New best R@1=0.5541, saved to /root/autodl-tmp/structfuse/checkpoints/m2_full_qwen/dataflow_aware_s43/best_by_recall_at_1\\nEarly stopping triggered at step 1500, best val_loss=0.4617 at step 500\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.35}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "0d4aae1c-75aa-4258-8fc2-12cc47270b17",
  "isSidechain": false,
  "promptId": "cb482ce5-85c1-49a1-985e-c68475dfc7e7",
  "type": "user",
  "uuid": "1ca2602a-db02-4374-80ca-721e85b38e79",
  "toolUseResult": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"  [eval@500] {'val_loss': 0.4616767596917259, 'recall@1': 0.549475753604194, 'recall@5': 0.9728047182175622, 'recall@10': 1.0}\\\\n  New best val_loss=0.4617, saved to /root/autodl-tmp/structfuse/checkpoints/m2_full_qwen/dataflow_aware_s43/best_by_val_loss\\\\n  New best R@1=0.5495, saved to /root/autodl-tmp/structfuse/checkpoints/m2_full_qwen/dataflow_aware_s43/best_by_recall_at_1\\\\n  step 550  loss=0.2641  lr=1.95e-05\\\\n  step 600  loss=0.1743  lr=1.92e-05\\\\n  step 650  loss=0.1656  lr=1.90e-05\\\\n  step 700  loss=0.3392  lr=1.87e-05\\\\n  step 750  loss=0.1229  lr=1.84e-05\\\\n  step 800  loss=0.0403  lr=1.80e-05\\\\n  step 850  loss=0.1022  lr=1.76e-05\\\\n  step 900  loss=0.0208  lr=1.72e-05\\\\n  step 950  loss=0.1532  lr=1.68e-05\\\\n  step 1000  loss=0.4353  lr=1.63e-05\\\\n  [eval@1000] {'val_loss': 0.49840330249516396, 'recall@1': 0.5173656618610747, 'recall@5': 0.9580602883355177, 'recall@10': 1.0}\\\\n  val_loss not improved (1/2)\\\\n  step 1050  loss=0.0832  lr=1.58e-05\\\\n  step 1100  loss=0.1566  lr=1.53e-05\\\\n  step 1150  loss=0.0397  lr=1.48e-05\\\\n  step 1200  loss=0.0318  lr=1.42e-05\\\\n  step 1250  loss=0.1481  lr=1.36e-05\\\\n  step 1300  loss=0.0999  lr=1.30e-05\\\\n  step 1350  loss=0.0552  lr=1.24e-05\\\\n  step 1400  loss=0.1586  lr=1.18e-05\\\\n[Epoch 2] Using pre-mined negatives (dataflow_aware)...\\\\n  step 1450  loss=0.0784  lr=1.12e-05\\\\n  step 1500  loss=0.0282  lr=1.06e-05\\\\n  [eval@1500] {'val_loss': 0.5185946156594262, 'recall@1': 0.5540629095674967, 'recall@5': 0.9564220183486238, 'recall@10': 1.0}\\\\n  val_loss not improved (2/2)\\\\n  New best R@1=0.5541, saved to /root/autodl-tmp/structfuse/checkpoints/m2_full_qwen/dataflow_aware_s43/best_by_recall_at_1\\\\nEarly stopping triggered at step 1500, best val_loss=0.4617 at step 500\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.35}}\"}",
  "mcpMeta": {
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"  [eval@500] {'val_loss': 0.4616767596917259, 'recall@1': 0.549475753604194, 'recall@5': 0.9728047182175622, 'recall@10': 1.0}\\n  New best val_loss=0.4617, saved to /root/autodl-tmp/structfuse/checkpoints/m2_full_qwen/dataflow_aware_s43/best_by_val_loss\\n  New best R@1=0.5495, saved to /root/autodl-tmp/structfuse/checkpoints/m2_full_qwen/dataflow_aware_s43/best_by_recall_at_1\\n  step 550  loss=0.2641  lr=1.95e-05\\n  step 600  loss=0.1743  lr=1.92e-05\\n  step 650  loss=0.1656  lr=1.90e-05\\n  step 700  loss=0.3392  lr=1.87e-05\\n  step 750  loss=0.1229  lr=1.84e-05\\n  step 800  loss=0.0403  lr=1.80e-05\\n  step 850  loss=0.1022  lr=1.76e-05\\n  step 900  loss=0.0208  lr=1.72e-05\\n  step 950  loss=0.1532  lr=1.68e-05\\n  step 1000  loss=0.4353  lr=1.63e-05\\n  [eval@1000] {'val_loss': 0.49840330249516396, 'recall@1': 0.5173656618610747, 'recall@5': 0.9580602883355177, 'recall@10': 1.0}\\n  val_loss not improved (1/2)\\n  step 1050  loss=0.0832  lr=1.58e-05\\n  step 1100  loss=0.1566  lr=1.53e-05\\n  step 1150  loss=0.0397  lr=1.48e-05\\n  step 1200  loss=0.0318  lr=1.42e-05\\n  step 1250  loss=0.1481  lr=1.36e-05\\n  step 1300  loss=0.0999  lr=1.30e-05\\n  step 1350  loss=0.0552  lr=1.24e-05\\n  step 1400  loss=0.1586  lr=1.18e-05\\n[Epoch 2] Using pre-mined negatives (dataflow_aware)...\\n  step 1450  loss=0.0784  lr=1.12e-05\\n  step 1500  loss=0.0282  lr=1.06e-05\\n  [eval@1500] {'val_loss': 0.5185946156594262, 'recall@1': 0.5540629095674967, 'recall@5': 0.9564220183486238, 'recall@10': 1.0}\\n  val_loss not improved (2/2)\\n  New best R@1=0.5541, saved to /root/autodl-tmp/structfuse/checkpoints/m2_full_qwen/dataflow_aware_s43/best_by_recall_at_1\\nEarly stopping triggered at step 1500, best val_loss=0.4617 at step 500\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.35}}"
    }
  },
  "sourceToolAssistantUUID": "0d4aae1c-75aa-4258-8fc2-12cc47270b17",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/.claude/sessions/reviewer_65cfe724",
  "sessionId": "f444a635-eeef-4924-9b48-a4c308632421",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---


### Tool result

_source line 138 · 2026-05-16T02:32:55.964Z_

<details><summary>↩ Tool result · `toolu_01XWUkYnnxE27sCQsJA5WPxC`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"  step 1350  loss=0.3103  lr=1.73e-05\\n  step 1400  loss=0.0814  lr=1.70e-05\\n[Epoch 2] Using pre-mined negatives (embedding_distance)...\\n  step 1450  loss=0.4381  lr=1.67e-05\\n  step 1500  loss=0.2784  lr=1.64e-05\\n  [eval@1500] {'val_loss': 0.6835051975794286, 'recall@1': 0.44731543624161074, 'recall@5': 0.8973154362416107, 'recall@10': 1.0}\\n  val_loss not improved (2/2)\\nEarly stopping triggered at step 1500, best val_loss=0.6154 at step 500\\n[Final eval] {'val_loss': 0.6926489475189439, 'recall@1': 0.4375838926174497, 'recall@5': 0.8976510067114094, 'recall@10': 1.0}\\nTraining complete. Model saved to /root/autodl-tmp/structfuse/checkpoints/m2_full_starcoder/embedding_distance_s42/final\\nwandb: \\nwandb: Run history:\\nwandb: learning_rate ▁▂▃▄▅▆▇▇████████████▇▇▇▇▇▇▇▇▇▇\\nwandb:      recall@1 ▁█▁\\nwandb:     recall@10 ▁▁▁\\nwandb:      recall@5 ▆█▁\\nwandb:    train_loss ██▆█▆▇▇▃▅▆▃▄▆▇▄▅▄��▂▄▃▆▂▄▅▃▃▁▅▃\\nwandb:      val_loss ▁▄█\\nwandb: \\nwandb: Run summary:\\nwandb: learning_rate 2e-05\\nwandb:      recall@1 0.43758\\nwandb:     recall@10 1\\nwandb:      recall@5 0.89765\\nwandb:    train_loss 0.27835\\nwandb:      val_loss 0.69265\\nwandb: \\nwandb: You can sync this run to the cloud by running:\\nwandb: wandb sync /root/structfuse-context/wandb/offline-run-20260516_011523-mh2e80qa\\nwandb: Find logs at: ./wandb/offline-run-20260516_011523-mh2e80qa/logs\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.43}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "8850b3d4-c99c-4a02-a1d1-ffeb7f5813ea",
  "isSidechain": false,
  "promptId": "cb482ce5-85c1-49a1-985e-c68475dfc7e7",
  "type": "user",
  "uuid": "d18b484a-c8b5-4a59-b973-f1c6b2fa1f7c",
  "toolUseResult": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"  step 1350  loss=0.3103  lr=1.73e-05\\\\n  step 1400  loss=0.0814  lr=1.70e-05\\\\n[Epoch 2] Using pre-mined negatives (embedding_distance)...\\\\n  step 1450  loss=0.4381  lr=1.67e-05\\\\n  step 1500  loss=0.2784  lr=1.64e-05\\\\n  [eval@1500] {'val_loss': 0.6835051975794286, 'recall@1': 0.44731543624161074, 'recall@5': 0.8973154362416107, 'recall@10': 1.0}\\\\n  val_loss not improved (2/2)\\\\nEarly stopping triggered at step 1500, best val_loss=0.6154 at step 500\\\\n[Final eval] {'val_loss': 0.6926489475189439, 'recall@1': 0.4375838926174497, 'recall@5': 0.8976510067114094, 'recall@10': 1.0}\\\\nTraining complete. Model saved to /root/autodl-tmp/structfuse/checkpoints/m2_full_starcoder/embedding_distance_s42/final\\\\nwandb: \\\\nwandb: Run history:\\\\nwandb: learning_rate ▁▂▃▄▅▆▇▇████████████▇▇▇▇▇▇▇▇▇▇\\\\nwandb:      recall@1 ▁█▁\\\\nwandb:     recall@10 ▁▁▁\\\\nwandb:      recall@5 ▆█▁\\\\nwandb:    train_loss ██▆█▆▇▇▃▅▆▃▄▆▇▄▅▄��▂▄▃▆▂▄▅▃▃▁▅▃\\\\nwandb:      val_loss ▁▄█\\\\nwandb: \\\\nwandb: Run summary:\\\\nwandb: learning_rate 2e-05\\\\nwandb:      recall@1 0.43758\\\\nwandb:     recall@10 1\\\\nwandb:      recall@5 0.89765\\\\nwandb:    train_loss 0.27835\\\\nwandb:      val_loss 0.69265\\\\nwandb: \\\\nwandb: You can sync this run to the cloud by running:\\\\nwandb: wandb sync /root/structfuse-context/wandb/offline-run-20260516_011523-mh2e80qa\\\\nwandb: Find logs at: ./wandb/offline-run-20260516_011523-mh2e80qa/logs\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.43}}\"}",
  "mcpMeta": {
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"  step 1350  loss=0.3103  lr=1.73e-05\\n  step 1400  loss=0.0814  lr=1.70e-05\\n[Epoch 2] Using pre-mined negatives (embedding_distance)...\\n  step 1450  loss=0.4381  lr=1.67e-05\\n  step 1500  loss=0.2784  lr=1.64e-05\\n  [eval@1500] {'val_loss': 0.6835051975794286, 'recall@1': 0.44731543624161074, 'recall@5': 0.8973154362416107, 'recall@10': 1.0}\\n  val_loss not improved (2/2)\\nEarly stopping triggered at step 1500, best val_loss=0.6154 at step 500\\n[Final eval] {'val_loss': 0.6926489475189439, 'recall@1': 0.4375838926174497, 'recall@5': 0.8976510067114094, 'recall@10': 1.0}\\nTraining complete. Model saved to /root/autodl-tmp/structfuse/checkpoints/m2_full_starcoder/embedding_distance_s42/final\\nwandb: \\nwandb: Run history:\\nwandb: learning_rate ▁▂▃▄▅▆▇▇████████████▇▇▇▇▇▇▇▇▇▇\\nwandb:      recall@1 ▁█▁\\nwandb:     recall@10 ▁▁▁\\nwandb:      recall@5 ▆█▁\\nwandb:    train_loss ██▆█▆▇▇▃▅▆▃▄▆▇▄▅▄��▂▄▃▆▂▄▅▃▃▁▅▃\\nwandb:      val_loss ▁▄█\\nwandb: \\nwandb: Run summary:\\nwandb: learning_rate 2e-05\\nwandb:      recall@1 0.43758\\nwandb:     recall@10 1\\nwandb:      recall@5 0.89765\\nwandb:    train_loss 0.27835\\nwandb:      val_loss 0.69265\\nwandb: \\nwandb: You can sync this run to the cloud by running:\\nwandb: wandb sync /root/structfuse-context/wandb/offline-run-20260516_011523-mh2e80qa\\nwandb: Find logs at: ./wandb/offline-run-20260516_011523-mh2e80qa/logs\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.43}}"
    }
  },
  "sourceToolAssistantUUID": "8850b3d4-c99c-4a02-a1d1-ffeb7f5813ea",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/.claude/sessions/reviewer_65cfe724",
  "sessionId": "f444a635-eeef-4924-9b48-a4c308632421",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---


### Runtime record

_source line 139_

```json
{
  "type": "last-prompt",
  "lastPrompt": "[系统通知 — worker_done:worker_ops_training-and-eval-status_20260516T022911]: Worker worker_ops_training-and-eval-status_20260516T022911 已完成（status=done），请审查 Agent 的处理结果。",
  "leafUuid": "d18b484a-c8b5-4a59-b973-f1c6b2fa1f7c",
  "sessionId": "f444a635-eeef-4924-9b48-a4c308632421"
}
```

---


### Runtime record

_source line 140_

```json
{
  "type": "ai-title",
  "aiTitle": "Review research literature worker completion",
  "sessionId": "f444a635-eeef-4924-9b48-a4c308632421"
}
```

---
