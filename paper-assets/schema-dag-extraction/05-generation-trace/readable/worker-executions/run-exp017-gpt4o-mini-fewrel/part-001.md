# run exp017 gpt4o mini fewrel — Part 1 of 23

**How Does Schema Complexity Predict Performance in Training-Free LLM Information Extraction?** · Worker execution logs

[Transcript overview](../run-exp017-gpt4o-mini-fewrel.md) · [Part 2 →](part-002.md) · [Structured JSON](../../../sessions/7b/7bbf6c44b2febbb72496.json)

## Before a recorded user message

## Before a recorded user message

311 recorded events


### Log line

_source line 1_

Warning: no stdin data received in 3s, proceeding without it. If piping from a slow command, redirect stdin explicitly: < /dev/null to skip, or wait longer.

---


### System

_source line 2_

```json
{
  "type": "system",
  "subtype": "init",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction",
  "session_id": "a81aceed-1d72-4aba-b0b2-803e0752c9ed",
  "tools": [
    "Task",
    "AskUserQuestion",
    "Bash",
    "CronCreate",
    "CronDelete",
    "CronList",
    "Edit",
    "EnterPlanMode",
    "EnterWorktree",
    "ExitPlanMode",
    "ExitWorktree",
    "Glob",
    "Grep",
    "ListMcpResourcesTool",
    "Monitor",
    "NotebookEdit",
    "PushNotification",
    "Read",
    "ReadMcpResourceTool",
    "RemoteTrigger",
    "ScheduleWakeup",
    "Skill",
    "TaskOutput",
    "TaskStop",
    "TodoWrite",
    "ToolSearch",
    "WebFetch",
    "WebSearch",
    "Write",
    "mcp__agent-ml-research__append_idea",
    "mcp__agent-ml-research__detect_image",
    "mcp__agent-ml-research__kill_job",
    "mcp__agent-ml-research__read_project_file",
    "mcp__agent-ml-research__read_registry",
    "mcp__agent-ml-research__register_artifact",
    "mcp__agent-ml-research__save_project_file",
    "mcp__agent-ml-research__ssh_execute",
    "mcp__agent-ml-research__ssh_read_only",
    "mcp__agent-ml-research__update_registry"
  ],
  "mcp_servers": [
    {
      "name": "agent-ml-research",
      "status": "connected"
    }
  ],
  "model": "claude-opus-4-6",
  "permissionMode": "bypassPermissions",
  "slash_commands": [
    "update-config",
    "debug",
    "simplify",
    "batch",
    "fewer-permission-prompts",
    "loop",
    "schedule",
    "claude-api",
    "clear",
    "compact",
    "context",
    "heapdump",
    "init",
    "review",
    "security-review",
    "extra-usage",
    "usage",
    "insights",
    "team-onboarding"
  ],
  "apiKeySource": "none",
  "claude_code_version": "2.1.126",
  "output_style": "default",
  "agents": [
    "claude",
    "Explore",
    "general-purpose",
    "Plan",
    "statusline-setup"
  ],
  "skills": [
    "update-config",
    "debug",
    "simplify",
    "batch",
    "fewer-permission-prompts",
    "loop",
    "schedule",
    "claude-api"
  ],
  "plugins": [],
  "analytics_disabled": false,
  "uuid": "ab9d78c7-ea9c-40c2-b9aa-ba6d183af6d1",
  "memory_paths": {
    "auto": "/home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-18-projects-schema-dag-extraction/memory/"
  },
  "fast_mode_state": "off"
}
```

---


### Runtime record

_source line 3_

```json
{
  "type": "rate_limit_event",
  "rate_limit_info": {
    "status": "allowed",
    "resetsAt": 1778929200,
    "rateLimitType": "five_hour",
    "overageStatus": "rejected",
    "overageDisabledReason": "org_level_disabled",
    "isUsingOverage": false
  },
  "uuid": "20423d6d-4a13-4d8e-bc7c-9b25f56e2932",
  "session_id": "a81aceed-1d72-4aba-b0b2-803e0752c9ed"
}
```

---


### Assistant

_source line 4_

<details><summary>Logged reasoning block</summary>

```text
Let me start by understanding the task. I need to run an experiment (exp-017) using GPT-4o-mini on FewRel dataset for relation extraction, replicating count curve and BCS-controlled experiments. This is an API-based experiment that doesn't need GPU.

Let me begin by:
1. Connecting to the server to explore existing code
2. Finding the FewRel experiment framework
3. Setting up the GPT-4o-mini version

Let me first load the necessary MCP tools.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "a81aceed-1d72-4aba-b0b2-803e0752c9ed",
  "uuid": "d3c0a204-b922-4bed-95e0-bf033d8626f5",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013XVanaxzDsJEkL3AjR3c1V",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12214,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12214
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### Assistant

_source line 5_

开始执行 exp-017。先加载工具，然后连接服务器探查已有代码。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "a81aceed-1d72-4aba-b0b2-803e0752c9ed",
  "uuid": "9be938b9-aa47-4382-8e77-ff914dc3e0b4",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013XVanaxzDsJEkL3AjR3c1V",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12214,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12214
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### Tool call

_source line 6_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01VAetDJYDca9eyoRKaztwkL`</summary>

```json
{
  "query": "select:mcp__agent-ml-research__ssh_read_only,mcp__agent-ml-research__ssh_execute,mcp__agent-ml-research__update_registry,mcp__agent-ml-research__detect_image,mcp__agent-ml-research__register_artifact",
  "max_results": 5
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "a81aceed-1d72-4aba-b0b2-803e0752c9ed",
  "uuid": "ae225bb6-57de-44f5-87f3-8085d4526816",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013XVanaxzDsJEkL3AjR3c1V",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12214,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12214
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### Tool result

_source line 7 · 2026-05-16T06:40:33.257Z_

<details><summary>↩ Tool result · `toolu_01VAetDJYDca9eyoRKaztwkL`</summary>

````text
```json
{
  "type": "tool_reference",
  "tool_name": "mcp__agent-ml-research__ssh_read_only"
}
```

```json
{
  "type": "tool_reference",
  "tool_name": "mcp__agent-ml-research__ssh_execute"
}
```

```json
{
  "type": "tool_reference",
  "tool_name": "mcp__agent-ml-research__update_registry"
}
```

```json
{
  "type": "tool_reference",
  "tool_name": "mcp__agent-ml-research__detect_image"
}
```

```json
{
  "type": "tool_reference",
  "tool_name": "mcp__agent-ml-research__register_artifact"
}
```
````

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "a81aceed-1d72-4aba-b0b2-803e0752c9ed",
  "uuid": "2a5fba8e-def8-4b1e-a7d5-ff47276d582b",
  "tool_use_result": {
    "matches": [
      "mcp__agent-ml-research__ssh_read_only",
      "mcp__agent-ml-research__ssh_execute",
      "mcp__agent-ml-research__update_registry",
      "mcp__agent-ml-research__detect_image",
      "mcp__agent-ml-research__register_artifact"
    ],
    "query": "select:mcp__agent-ml-research__ssh_read_only,mcp__agent-ml-research__ssh_execute,mcp__agent-ml-research__update_registry,mcp__agent-ml-research__detect_image,mcp__agent-ml-research__register_artifact",
    "total_deferred_tools": 29
  }
}
```

</details>

---


### Assistant

_source line 8_

<details><summary>Logged reasoning block</summary>

```text
Good, tools are loaded. Let me start by connecting to the server and exploring the existing FewRel experiment code.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "a81aceed-1d72-4aba-b0b2-803e0752c9ed",
  "uuid": "64883e64-a9b4-4a28-a145-77af14b50641",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VRbzPH2TJpiHiw3yaSfaSu",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 2054,
      "cache_read_input_tokens": 24055,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2054
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### Tool call

_source line 9_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__detect_image · `toolu_012uBApNHvPjrATd4WoAT6eY`</summary>

```json
{
  "server": "cqa1-38874",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "a81aceed-1d72-4aba-b0b2-803e0752c9ed",
  "uuid": "de8d08eb-0ec8-4cb5-8034-0fa897bfa0ca",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VRbzPH2TJpiHiw3yaSfaSu",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 2054,
      "cache_read_input_tokens": 24055,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2054
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### Tool call

_source line 10_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01Re7Rg3tZ3AL7wuymLQ6KPZ`</summary>

```json
{
  "server": "cqa1-38874",
  "command": "ls /root/schema-dag-extraction/src/run_fewrel*.py",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "a81aceed-1d72-4aba-b0b2-803e0752c9ed",
  "uuid": "dc8f4dfd-fbfa-488a-b82f-203cabe1875b",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VRbzPH2TJpiHiw3yaSfaSu",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 2054,
      "cache_read_input_tokens": 24055,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2054
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### Tool result

_source line 11 · 2026-05-16T06:40:37.880Z_

<details><summary>↩ Tool result · `toolu_012uBApNHvPjrATd4WoAT6eY`</summary>

```text
{"result":"{\n  \"detected\": false,\n  \"status\": \"unknown\",\n  \"skip_base_setup\": false,\n  \"message\": \"No image marker file found. Use traditional env-setup flow.\"\n}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "a81aceed-1d72-4aba-b0b2-803e0752c9ed",
  "uuid": "a744ae0f-e852-4fdd-8ed7-6a7c1b9da214",
  "tool_use_result": {
    "content": "{\"result\":\"{\\n  \\\"detected\\\": false,\\n  \\\"status\\\": \\\"unknown\\\",\\n  \\\"skip_base_setup\\\": false,\\n  \\\"message\\\": \\\"No image marker file found. Use traditional env-setup flow.\\\"\\n}\"}",
    "structuredContent": {
      "result": "{\n  \"detected\": false,\n  \"status\": \"unknown\",\n  \"skip_base_setup\": false,\n  \"message\": \"No image marker file found. Use traditional env-setup flow.\"\n}"
    }
  }
}
```

</details>

---


### Tool result

_source line 12 · 2026-05-16T06:40:38.381Z_

<details><summary>↩ Tool result · `toolu_01Re7Rg3tZ3AL7wuymLQ6KPZ`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"/root/schema-dag-extraction/src/run_fewrel_16rel_bootstrap.py\\n/root/schema-dag-extraction/src/run_fewrel_40rel.py\\n/root/schema-dag-extraction/src/run_fewrel_80pool_16sub_bootstrap.py\\n/root/schema-dag-extraction/src/run_fewrel_formal.py\\n/root/schema-dag-extraction/src/run_fewrel_pilot.py\\n/root/schema-dag-extraction/src/run_fewrel_v2_bcs.py\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.47}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "a81aceed-1d72-4aba-b0b2-803e0752c9ed",
  "uuid": "fbe10dd9-71cd-4575-ac41-5fe5298b1be8",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"/root/schema-dag-extraction/src/run_fewrel_16rel_bootstrap.py\\\\n/root/schema-dag-extraction/src/run_fewrel_40rel.py\\\\n/root/schema-dag-extraction/src/run_fewrel_80pool_16sub_bootstrap.py\\\\n/root/schema-dag-extraction/src/run_fewrel_formal.py\\\\n/root/schema-dag-extraction/src/run_fewrel_pilot.py\\\\n/root/schema-dag-extraction/src/run_fewrel_v2_bcs.py\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.47}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"/root/schema-dag-extraction/src/run_fewrel_16rel_bootstrap.py\\n/root/schema-dag-extraction/src/run_fewrel_40rel.py\\n/root/schema-dag-extraction/src/run_fewrel_80pool_16sub_bootstrap.py\\n/root/schema-dag-extraction/src/run_fewrel_formal.py\\n/root/schema-dag-extraction/src/run_fewrel_pilot.py\\n/root/schema-dag-extraction/src/run_fewrel_v2_bcs.py\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.47}}"
    }
  }
}
```

</details>

---


### Assistant

_source line 13_

找到多个 FewRel 实验脚本。让我查看最相关的——`run_fewrel_formal.py` 和 `run_fewrel_v2_bcs.py`，以及 OpenAI API 配置方式。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "a81aceed-1d72-4aba-b0b2-803e0752c9ed",
  "uuid": "ce72033f-464b-4223-b346-8b4a9833b3c5",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01H1Mxts92ge8RP731uJ7KQJ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 580,
      "cache_read_input_tokens": 26109,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 580
      },
      "output_tokens": 1,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### Tool call

_source line 14_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01TKtgznoti2ZpbbrHj4KYMP`</summary>

```json
{
  "server": "cqa1-38874",
  "command": "head -80 /root/schema-dag-extraction/src/run_fewrel_formal.py",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "a81aceed-1d72-4aba-b0b2-803e0752c9ed",
  "uuid": "9ddeb036-6f7b-4300-80d2-f0991188fee9",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01H1Mxts92ge8RP731uJ7KQJ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 580,
      "cache_read_input_tokens": 26109,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 580
      },
      "output_tokens": 1,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### Tool result

_source line 15 · 2026-05-16T06:40:42.961Z_

<details><summary>↩ Tool result · `toolu_01TKtgznoti2ZpbbrHj4KYMP`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"\\\"\\\"\\\"FewRel formal study: BCS-confusion hypothesis on relation extraction.\\n\\nexp1 (Count curve): count={1,4,8,16,32,64,80}, 5 random batches per count,\\n    count_1 = 80 solo batches (one per relation type).\\n    1000 samples balanced across active relations.\\n\\nexp2 (BCS controlled): count={8,16}, 1 low-BCS + 1 high-BCS + 25 random = 27 per count.\\n    Same 1000 samples.\\n\\nMetric: accuracy (RE is single-label classification per sample).\\n\\nUsage:\\n    # Auto two-stage (recommended — avoids vLLM fork deadlock):\\n    python3 src/run_fewrel_formal.py --mode exp1 --use_all\\n\\n    # Manual two-stage:\\n    python3 src/run_fewrel_formal.py --stage preprocess --mode exp1 --use_all\\n    python3 src/run_fewrel_formal.py --stage extract --mode exp1\\n\\n    # Dry run:\\n    python3 src/run_fewrel_formal.py --mode exp1 --use_all --dry_run\\n\\\"\\\"\\\"\\nimport argparse\\nimport json\\nimport logging\\nimport random\\nimport subprocess\\nimport sys\\nimport time\\nfrom collections import defaultdict\\nfrom pathlib import Path\\n\\nlogger = logging.getLogger(__name__)\\n\\nBASE_DIR = Path(\\\"/root/schema-dag-extraction\\\")\\n\\nEXP1_COUNTS = [1, 4, 8, 16, 32, 64, 80]\\nEXP2_COUNTS = [8, 16]\\nEXP1_RANDOM_PER_COUNT = 5\\nEXP2_RANDOM_PER_COUNT = 25\\nDEFAULT_N_SAMPLES = 1000\\n\\n\\ndef evaluate_re(results):\\n    \\\"\\\"\\\"Per-batch accuracy and per-type accuracy breakdown.\\\"\\\"\\\"\\n    batch_stats = defaultdict(lambda: {\\\"correct\\\": 0, \\\"total\\\": 0, \\\"bcs\\\": 0.0,\\n                                       \\\"count_key\\\": \\\"\\\", \\\"num_types\\\": 0,\\n                                       \\\"batch_types\\\": [], \\\"per_type\\\": defaultdict(lambda: {\\\"correct\\\": 0, \\\"total\\\": 0})})\\n    for r in results:\\n        bid = r[\\\"batch_id\\\"]\\n        s = batch_stats[bid]\\n        s[\\\"total\\\"] += 1\\n        s[\\\"bcs\\\"] = r[\\\"batch_bcs\\\"]\\n        s[\\\"count_key\\\"] = r[\\\"count_key\\\"]\\n        s[\\\"num_types\\\"] = len(r[\\\"batch_types\\\"])\\n        s[\\\"batch_types\\\"] = r[\\\"batch_types\\\"]\\n        gold = r[\\\"ground_truth\\\"]\\n        pred = r[\\\"prediction\\\"]\\n        s[\\\"per_type\\\"][gold][\\\"total\\\"] += 1\\n        if pred == gold:\\n            s[\\\"correct\\\"] += 1\\n            s[\\\"per_type\\\"][gold][\\\"correct\\\"] += 1\\n\\n    out = {}\\n    for bid, s in batch_stats.items():\\n        per_type_acc = {}\\n        for t, ts in s[\\\"per_type\\\"].items():\\n            per_type_acc[t] = {\\n                \\\"accuracy\\\": ts[\\\"correct\\\"] / ts[\\\"total\\\"] if ts[\\\"total\\\"] else 0.0,\\n                \\\"correct\\\": ts[\\\"correct\\\"], \\\"total\\\": ts[\\\"total\\\"],\\n            }\\n        out[bid] = {\\n            \\\"accuracy\\\": s[\\\"correct\\\"] / s[\\\"total\\\"] if s[\\\"total\\\"] else 0.0,\\n            \\\"correct\\\": s[\\\"correct\\\"], \\\"total\\\": s[\\\"total\\\"], \\\"bcs\\\": s[\\\"bcs\\\"],\\n            \\\"count_key\\\": s[\\\"count_key\\\"], \\\"num_types\\\": s[\\\"num_types\\\"],\\n            \\\"batch_types\\\": s[\\\"batch_types\\\"], \\\"per_type_accuracy\\\": per_type_acc,\\n        }\\n    return out\\n\\n\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.4}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "a81aceed-1d72-4aba-b0b2-803e0752c9ed",
  "uuid": "0836436e-a731-40c7-82a8-6143f39b7ad1",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"\\\\\\\"\\\\\\\"\\\\\\\"FewRel formal study: BCS-confusion hypothesis on relation extraction.\\\\n\\\\nexp1 (Count curve): count={1,4,8,16,32,64,80}, 5 random batches per count,\\\\n    count_1 = 80 solo batches (one per relation type).\\\\n    1000 samples balanced across active relations.\\\\n\\\\nexp2 (BCS controlled): count={8,16}, 1 low-BCS + 1 high-BCS + 25 random = 27 per count.\\\\n    Same 1000 samples.\\\\n\\\\nMetric: accuracy (RE is single-label classification per sample).\\\\n\\\\nUsage:\\\\n    # Auto two-stage (recommended — avoids vLLM fork deadlock):\\\\n    python3 src/run_fewrel_formal.py --mode exp1 --use_all\\\\n\\\\n    # Manual two-stage:\\\\n    python3 src/run_fewrel_formal.py --stage preprocess --mode exp1 --use_all\\\\n    python3 src/run_fewrel_formal.py --stage extract --mode exp1\\\\n\\\\n    # Dry run:\\\\n    python3 src/run_fewrel_formal.py --mode exp1 --use_all --dry_run\\\\n\\\\\\\"\\\\\\\"\\\\\\\"\\\\nimport argparse\\\\nimport json\\\\nimport logging\\\\nimport random\\\\nimport subprocess\\\\nimport sys\\\\nimport time\\\\nfrom collections import defaultdict\\\\nfrom pathlib import Path\\\\n\\\\nlogger = logging.getLogger(__name__)\\\\n\\\\nBASE_DIR = Path(\\\\\\\"/root/schema-dag-extraction\\\\\\\")\\\\n\\\\nEXP1_COUNTS = [1, 4, 8, 16, 32, 64, 80]\\\\nEXP2_COUNTS = [8, 16]\\\\nEXP1_RANDOM_PER_COUNT = 5\\\\nEXP2_RANDOM_PER_COUNT = 25\\\\nDEFAULT_N_SAMPLES = 1000\\\\n\\\\n\\\\ndef evaluate_re(results):\\\\n    \\\\\\\"\\\\\\\"\\\\\\\"Per-batch accuracy and per-type accuracy breakdown.\\\\\\\"\\\\\\\"\\\\\\\"\\\\n    batch_stats = defaultdict(lambda: {\\\\\\\"correct\\\\\\\": 0, \\\\\\\"total\\\\\\\": 0, \\\\\\\"bcs\\\\\\\": 0.0,\\\\n                                       \\\\\\\"count_key\\\\\\\": \\\\\\\"\\\\\\\", \\\\\\\"num_types\\\\\\\": 0,\\\\n                                       \\\\\\\"batch_types\\\\\\\": [], \\\\\\\"per_type\\\\\\\": defaultdict(lambda: {\\\\\\\"correct\\\\\\\": 0, \\\\\\\"total\\\\\\\": 0})})\\\\n    for r in results:\\\\n        bid = r[\\\\\\\"batch_id\\\\\\\"]\\\\n        s = batch_stats[bid]\\\\n        s[\\\\\\\"total\\\\\\\"] += 1\\\\n        s[\\\\\\\"bcs\\\\\\\"] = r[\\\\\\\"batch_bcs\\\\\\\"]\\\\n        s[\\\\\\\"count_key\\\\\\\"] = r[\\\\\\\"count_key\\\\\\\"]\\\\n        s[\\\\\\\"num_types\\\\\\\"] = len(r[\\\\\\\"batch_types\\\\\\\"])\\\\n        s[\\\\\\\"batch_types\\\\\\\"] = r[\\\\\\\"batch_types\\\\\\\"]\\\\n        gold = r[\\\\\\\"ground_truth\\\\\\\"]\\\\n        pred = r[\\\\\\\"prediction\\\\\\\"]\\\\n        s[\\\\\\\"per_type\\\\\\\"][gold][\\\\\\\"total\\\\\\\"] += 1\\\\n        if pred == gold:\\\\n            s[\\\\\\\"correct\\\\\\\"] += 1\\\\n            s[\\\\\\\"per_type\\\\\\\"][gold][\\\\\\\"correct\\\\\\\"] += 1\\\\n\\\\n    out = {}\\\\n    for bid, s in batch_stats.items():\\\\n        per_type_acc = {}\\\\n        for t, ts in s[\\\\\\\"per_type\\\\\\\"].items():\\\\n            per_type_acc[t] = {\\\\n                \\\\\\\"accuracy\\\\\\\": ts[\\\\\\\"correct\\\\\\\"] / ts[\\\\\\\"total\\\\\\\"] if ts[\\\\\\\"total\\\\\\\"] else 0.0,\\\\n                \\\\\\\"correct\\\\\\\": ts[\\\\\\\"correct\\\\\\\"], \\\\\\\"total\\\\\\\": ts[\\\\\\\"total\\\\\\\"],\\\\n            }\\\\n        out[bid] = {\\\\n            \\\\\\\"accuracy\\\\\\\": s[\\\\\\\"correct\\\\\\\"] / s[\\\\\\\"total\\\\\\\"] if s[\\\\\\\"total\\\\\\\"] else 0.0,\\\\n            \\\\\\\"correct\\\\\\\": s[\\\\\\\"correct\\\\\\\"], \\\\\\\"total\\\\\\\": s[\\\\\\\"total\\\\\\\"], \\\\\\\"bcs\\\\\\\": s[\\\\\\\"bcs\\\\\\\"],\\\\n            \\\\\\\"count_key\\\\\\\": s[\\\\\\\"count_key\\\\\\\"], \\\\\\\"num_types\\\\\\\": s[\\\\\\\"num_types\\\\\\\"],\\\\n            \\\\\\\"batch_types\\\\\\\": s[\\\\\\\"batch_types\\\\\\\"], \\\\\\\"per_type_accuracy\\\\\\\": per_type_acc,\\\\n        }\\\\n    return out\\\\n\\\\n\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.4}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"\\\"\\\"\\\"FewRel formal study: BCS-confusion hypothesis on relation extraction.\\n\\nexp1 (Count curve): count={1,4,8,16,32,64,80}, 5 random batches per count,\\n    count_1 = 80 solo batches (one per relation type).\\n    1000 samples balanced across active relations.\\n\\nexp2 (BCS controlled): count={8,16}, 1 low-BCS + 1 high-BCS + 25 random = 27 per count.\\n    Same 1000 samples.\\n\\nMetric: accuracy (RE is single-label classification per sample).\\n\\nUsage:\\n    # Auto two-stage (recommended — avoids vLLM fork deadlock):\\n    python3 src/run_fewrel_formal.py --mode exp1 --use_all\\n\\n    # Manual two-stage:\\n    python3 src/run_fewrel_formal.py --stage preprocess --mode exp1 --use_all\\n    python3 src/run_fewrel_formal.py --stage extract --mode exp1\\n\\n    # Dry run:\\n    python3 src/run_fewrel_formal.py --mode exp1 --use_all --dry_run\\n\\\"\\\"\\\"\\nimport argparse\\nimport json\\nimport logging\\nimport random\\nimport subprocess\\nimport sys\\nimport time\\nfrom collections import defaultdict\\nfrom pathlib import Path\\n\\nlogger = logging.getLogger(__name__)\\n\\nBASE_DIR = Path(\\\"/root/schema-dag-extraction\\\")\\n\\nEXP1_COUNTS = [1, 4, 8, 16, 32, 64, 80]\\nEXP2_COUNTS = [8, 16]\\nEXP1_RANDOM_PER_COUNT = 5\\nEXP2_RANDOM_PER_COUNT = 25\\nDEFAULT_N_SAMPLES = 1000\\n\\n\\ndef evaluate_re(results):\\n    \\\"\\\"\\\"Per-batch accuracy and per-type accuracy breakdown.\\\"\\\"\\\"\\n    batch_stats = defaultdict(lambda: {\\\"correct\\\": 0, \\\"total\\\": 0, \\\"bcs\\\": 0.0,\\n                                       \\\"count_key\\\": \\\"\\\", \\\"num_types\\\": 0,\\n                                       \\\"batch_types\\\": [], \\\"per_type\\\": defaultdict(lambda: {\\\"correct\\\": 0, \\\"total\\\": 0})})\\n    for r in results:\\n        bid = r[\\\"batch_id\\\"]\\n        s = batch_stats[bid]\\n        s[\\\"total\\\"] += 1\\n        s[\\\"bcs\\\"] = r[\\\"batch_bcs\\\"]\\n        s[\\\"count_key\\\"] = r[\\\"count_key\\\"]\\n        s[\\\"num_types\\\"] = len(r[\\\"batch_types\\\"])\\n        s[\\\"batch_types\\\"] = r[\\\"batch_types\\\"]\\n        gold = r[\\\"ground_truth\\\"]\\n        pred = r[\\\"prediction\\\"]\\n        s[\\\"per_type\\\"][gold][\\\"total\\\"] += 1\\n        if pred == gold:\\n            s[\\\"correct\\\"] += 1\\n            s[\\\"per_type\\\"][gold][\\\"correct\\\"] += 1\\n\\n    out = {}\\n    for bid, s in batch_stats.items():\\n        per_type_acc = {}\\n        for t, ts in s[\\\"per_type\\\"].items():\\n            per_type_acc[t] = {\\n                \\\"accuracy\\\": ts[\\\"correct\\\"] / ts[\\\"total\\\"] if ts[\\\"total\\\"] else 0.0,\\n                \\\"correct\\\": ts[\\\"correct\\\"], \\\"total\\\": ts[\\\"total\\\"],\\n            }\\n        out[bid] = {\\n            \\\"accuracy\\\": s[\\\"correct\\\"] / s[\\\"total\\\"] if s[\\\"total\\\"] else 0.0,\\n            \\\"correct\\\": s[\\\"correct\\\"], \\\"total\\\": s[\\\"total\\\"], \\\"bcs\\\": s[\\\"bcs\\\"],\\n            \\\"count_key\\\": s[\\\"count_key\\\"], \\\"num_types\\\": s[\\\"num_types\\\"],\\n            \\\"batch_types\\\": s[\\\"batch_types\\\"], \\\"per_type_accuracy\\\": per_type_acc,\\n        }\\n    return out\\n\\n\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.4}}"
    }
  }
}
```

</details>

---


### Tool call

_source line 16_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_019WUoYn7VHLdxpDgbDmjZVV`</summary>

```json
{
  "server": "cqa1-38874",
  "command": "head -80 /root/schema-dag-extraction/src/run_fewrel_v2_bcs.py",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "a81aceed-1d72-4aba-b0b2-803e0752c9ed",
  "uuid": "f2f870ad-dbeb-4ba8-a47c-4c1a337bb75d",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01H1Mxts92ge8RP731uJ7KQJ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 580,
      "cache_read_input_tokens": 26109,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 580
      },
      "output_tokens": 1,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### Tool call

_source line 17_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01T6Yn5NstWBiZVCAWtEzpMQ`</summary>

```json
{
  "server": "cqa1-38874",
  "command": "grep -r \"tum\\|base_url\\|openai\\|OPENAI\" /root/schema-dag-extraction/src/ --include=\"*.py\" -l",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "a81aceed-1d72-4aba-b0b2-803e0752c9ed",
  "uuid": "48def65a-6767-438f-b8a8-5fa8679f49bd",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01H1Mxts92ge8RP731uJ7KQJ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 580,
      "cache_read_input_tokens": 26109,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 580
      },
      "output_tokens": 1,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### Tool result

_source line 18 · 2026-05-16T06:40:44.165Z_

<details><summary>↩ Tool result · `toolu_019WUoYn7VHLdxpDgbDmjZVV`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"#!/usr/bin/env python3\\n\\\"\\\"\\\"FewRel v2 prompt BCS-controlled experiment (C1b).\\n\\nPurpose: Verify Channel 2 (BCS → type confusion) holds under v2 anti-hallucination prompt.\\nDesign:  count=8, 5 low-BCS batches + 5 high-BCS batches from 80-rel pool.\\nBatches: Reused from exp_fewrel_formal_80rel batch_config_exp2.json — all 27 count_8\\n         batches ranked by BCS, bottom 5 = low group, top 5 = high group.\\nPrompt:  v2 RE prompt (build_prompt_v2_re from run_extraction.py) — no offsets,\\n         adds \\\"none\\\" fallback, constrained JSON output.\\nMetric:  per-batch accuracy, Δ(low−high) mean ± bootstrap 95% CI.\\n\\nInput:  FewRel train+val parquet (80 relations), batch_config_exp2.json, Qwen3-32B-FP8\\nOutput: artifacts/fewrel_v2_bcs/ — results_incremental.jsonl, eval_results.json, bootstrap_ci.json\\n\\nTwo-stage execution to avoid vLLM fork deadlock:\\n    python3 src/run_fewrel_v2_bcs.py --stage all\\n    python3 src/run_fewrel_v2_bcs.py --stage all --dry_run\\n    python3 src/run_fewrel_v2_bcs.py --stage extract [--resume]\\n    python3 src/run_fewrel_v2_bcs.py --analysis_only\\n\\\"\\\"\\\"\\nimport argparse\\nimport json\\nimport logging\\nimport random\\nimport subprocess\\nimport sys\\nimport time\\nfrom collections import defaultdict\\nfrom pathlib import Path\\n\\nimport numpy as np\\n\\nlogger = logging.getLogger(__name__)\\n\\nBASE_DIR = Path(\\\"/root/schema-dag-extraction\\\")\\nOUTPUT_DIR = BASE_DIR / \\\"artifacts\\\" / \\\"fewrel_v2_bcs\\\"\\n# Reuse batch definitions from the formal 80-rel experiment\\nBATCH_CONFIG_PATH = BASE_DIR / \\\"artifacts\\\" / \\\"fewrel_formal_full\\\" / \\\"batch_config_exp2.json\\\"\\nN_LOW = 5\\nN_HIGH = 5\\nCOUNT_KEY = \\\"count_8\\\"\\nDEFAULT_N_SAMPLES = 1000\\n\\n\\ndef select_bcs_groups(batch_config_path, count_key=\\\"count_8\\\", n_low=5, n_high=5):\\n    \\\"\\\"\\\"Rank all count_8 batches by BCS, return bottom-n as low group and top-n as high.\\\"\\\"\\\"\\n    with open(batch_config_path) as f:\\n        config = json.load(f)\\n\\n    entry = config[count_key]\\n    all_batches = []\\n\\n    if \\\"low_bcs\\\" in entry:\\n        all_batches.append({\\n            \\\"types\\\": entry[\\\"low_bcs\\\"][\\\"types\\\"],\\n            \\\"bcs\\\": entry[\\\"low_bcs\\\"][\\\"bcs\\\"],\\n            \\\"source\\\": \\\"greedy_low\\\",\\n        })\\n    if \\\"high_bcs\\\" in entry:\\n        all_batches.append({\\n            \\\"types\\\": entry[\\\"high_bcs\\\"][\\\"types\\\"],\\n            \\\"bcs\\\": entry[\\\"high_bcs\\\"][\\\"bcs\\\"],\\n            \\\"source\\\": \\\"greedy_high\\\",\\n        })\\n    for ri, rb in enumerate(entry.get(\\\"random\\\", [])):\\n        all_batches.append({\\n            \\\"types\\\": rb[\\\"types\\\"],\\n            \\\"bcs\\\": rb[\\\"bcs\\\"],\\n            \\\"source\\\": f\\\"random_{ri}\\\",\\n        })\\n\\n    all_batches.sort(key=lambda x: x[\\\"bcs\\\"])\\n\\n    low_group = all_batches[:n_low]\\n    high_group = all_batches[-n_high:]\\n\\n    return low_group, high_group\\n\\n\\ndef evaluate_re(results):\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.67}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "a81aceed-1d72-4aba-b0b2-803e0752c9ed",
  "uuid": "91d82c99-9552-414f-8d45-6bac0ff46cb9",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"#!/usr/bin/env python3\\\\n\\\\\\\"\\\\\\\"\\\\\\\"FewRel v2 prompt BCS-controlled experiment (C1b).\\\\n\\\\nPurpose: Verify Channel 2 (BCS → type confusion) holds under v2 anti-hallucination prompt.\\\\nDesign:  count=8, 5 low-BCS batches + 5 high-BCS batches from 80-rel pool.\\\\nBatches: Reused from exp_fewrel_formal_80rel batch_config_exp2.json — all 27 count_8\\\\n         batches ranked by BCS, bottom 5 = low group, top 5 = high group.\\\\nPrompt:  v2 RE prompt (build_prompt_v2_re from run_extraction.py) — no offsets,\\\\n         adds \\\\\\\"none\\\\\\\" fallback, constrained JSON output.\\\\nMetric:  per-batch accuracy, Δ(low−high) mean ± bootstrap 95% CI.\\\\n\\\\nInput:  FewRel train+val parquet (80 relations), batch_config_exp2.json, Qwen3-32B-FP8\\\\nOutput: artifacts/fewrel_v2_bcs/ — results_incremental.jsonl, eval_results.json, bootstrap_ci.json\\\\n\\\\nTwo-stage execution to avoid vLLM fork deadlock:\\\\n    python3 src/run_fewrel_v2_bcs.py --stage all\\\\n    python3 src/run_fewrel_v2_bcs.py --stage all --dry_run\\\\n    python3 src/run_fewrel_v2_bcs.py --stage extract [--resume]\\\\n    python3 src/run_fewrel_v2_bcs.py --analysis_only\\\\n\\\\\\\"\\\\\\\"\\\\\\\"\\\\nimport argparse\\\\nimport json\\\\nimport logging\\\\nimport random\\\\nimport subprocess\\\\nimport sys\\\\nimport time\\\\nfrom collections import defaultdict\\\\nfrom pathlib import Path\\\\n\\\\nimport numpy as np\\\\n\\\\nlogger = logging.getLogger(__name__)\\\\n\\\\nBASE_DIR = Path(\\\\\\\"/root/schema-dag-extraction\\\\\\\")\\\\nOUTPUT_DIR = BASE_DIR / \\\\\\\"artifacts\\\\\\\" / \\\\\\\"fewrel_v2_bcs\\\\\\\"\\\\n# Reuse batch definitions from the formal 80-rel experiment\\\\nBATCH_CONFIG_PATH = BASE_DIR / \\\\\\\"artifacts\\\\\\\" / \\\\\\\"fewrel_formal_full\\\\\\\" / \\\\\\\"batch_config_exp2.json\\\\\\\"\\\\nN_LOW = 5\\\\nN_HIGH = 5\\\\nCOUNT_KEY = \\\\\\\"count_8\\\\\\\"\\\\nDEFAULT_N_SAMPLES = 1000\\\\n\\\\n\\\\ndef select_bcs_groups(batch_config_path, count_key=\\\\\\\"count_8\\\\\\\", n_low=5, n_high=5):\\\\n    \\\\\\\"\\\\\\\"\\\\\\\"Rank all count_8 batches by BCS, return bottom-n as low group and top-n as high.\\\\\\\"\\\\\\\"\\\\\\\"\\\\n    with open(batch_config_path) as f:\\\\n        config = json.load(f)\\\\n\\\\n    entry = config[count_key]\\\\n    all_batches = []\\\\n\\\\n    if \\\\\\\"low_bcs\\\\\\\" in entry:\\\\n        all_batches.append({\\\\n            \\\\\\\"types\\\\\\\": entry[\\\\\\\"low_bcs\\\\\\\"][\\\\\\\"types\\\\\\\"],\\\\n            \\\\\\\"bcs\\\\\\\": entry[\\\\\\\"low_bcs\\\\\\\"][\\\\\\\"bcs\\\\\\\"],\\\\n            \\\\\\\"source\\\\\\\": \\\\\\\"greedy_low\\\\\\\",\\\\n        })\\\\n    if \\\\\\\"high_bcs\\\\\\\" in entry:\\\\n        all_batches.append({\\\\n            \\\\\\\"types\\\\\\\": entry[\\\\\\\"high_bcs\\\\\\\"][\\\\\\\"types\\\\\\\"],\\\\n            \\\\\\\"bcs\\\\\\\": entry[\\\\\\\"high_bcs\\\\\\\"][\\\\\\\"bcs\\\\\\\"],\\\\n            \\\\\\\"source\\\\\\\": \\\\\\\"greedy_high\\\\\\\",\\\\n        })\\\\n    for ri, rb in enumerate(entry.get(\\\\\\\"random\\\\\\\", [])):\\\\n        all_batches.append({\\\\n            \\\\\\\"types\\\\\\\": rb[\\\\\\\"types\\\\\\\"],\\\\n            \\\\\\\"bcs\\\\\\\": rb[\\\\\\\"bcs\\\\\\\"],\\\\n            \\\\\\\"source\\\\\\\": f\\\\\\\"random_{ri}\\\\\\\",\\\\n        })\\\\n\\\\n    all_batches.sort(key=lambda x: x[\\\\\\\"bcs\\\\\\\"])\\\\n\\\\n    low_group = all_batches[:n_low]\\\\n    high_group = all_batches[-n_high:]\\\\n\\\\n    return low_group, high_group\\\\n\\\\n\\\\ndef evaluate_re(results):\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.67}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"#!/usr/bin/env python3\\n\\\"\\\"\\\"FewRel v2 prompt BCS-controlled experiment (C1b).\\n\\nPurpose: Verify Channel 2 (BCS → type confusion) holds under v2 anti-hallucination prompt.\\nDesign:  count=8, 5 low-BCS batches + 5 high-BCS batches from 80-rel pool.\\nBatches: Reused from exp_fewrel_formal_80rel batch_config_exp2.json — all 27 count_8\\n         batches ranked by BCS, bottom 5 = low group, top 5 = high group.\\nPrompt:  v2 RE prompt (build_prompt_v2_re from run_extraction.py) — no offsets,\\n         adds \\\"none\\\" fallback, constrained JSON output.\\nMetric:  per-batch accuracy, Δ(low−high) mean ± bootstrap 95% CI.\\n\\nInput:  FewRel train+val parquet (80 relations), batch_config_exp2.json, Qwen3-32B-FP8\\nOutput: artifacts/fewrel_v2_bcs/ — results_incremental.jsonl, eval_results.json, bootstrap_ci.json\\n\\nTwo-stage execution to avoid vLLM fork deadlock:\\n    python3 src/run_fewrel_v2_bcs.py --stage all\\n    python3 src/run_fewrel_v2_bcs.py --stage all --dry_run\\n    python3 src/run_fewrel_v2_bcs.py --stage extract [--resume]\\n    python3 src/run_fewrel_v2_bcs.py --analysis_only\\n\\\"\\\"\\\"\\nimport argparse\\nimport json\\nimport logging\\nimport random\\nimport subprocess\\nimport sys\\nimport time\\nfrom collections import defaultdict\\nfrom pathlib import Path\\n\\nimport numpy as np\\n\\nlogger = logging.getLogger(__name__)\\n\\nBASE_DIR = Path(\\\"/root/schema-dag-extraction\\\")\\nOUTPUT_DIR = BASE_DIR / \\\"artifacts\\\" / \\\"fewrel_v2_bcs\\\"\\n# Reuse batch definitions from the formal 80-rel experiment\\nBATCH_CONFIG_PATH = BASE_DIR / \\\"artifacts\\\" / \\\"fewrel_formal_full\\\" / \\\"batch_config_exp2.json\\\"\\nN_LOW = 5\\nN_HIGH = 5\\nCOUNT_KEY = \\\"count_8\\\"\\nDEFAULT_N_SAMPLES = 1000\\n\\n\\ndef select_bcs_groups(batch_config_path, count_key=\\\"count_8\\\", n_low=5, n_high=5):\\n    \\\"\\\"\\\"Rank all count_8 batches by BCS, return bottom-n as low group and top-n as high.\\\"\\\"\\\"\\n    with open(batch_config_path) as f:\\n        config = json.load(f)\\n\\n    entry = config[count_key]\\n    all_batches = []\\n\\n    if \\\"low_bcs\\\" in entry:\\n        all_batches.append({\\n            \\\"types\\\": entry[\\\"low_bcs\\\"][\\\"types\\\"],\\n            \\\"bcs\\\": entry[\\\"low_bcs\\\"][\\\"bcs\\\"],\\n            \\\"source\\\": \\\"greedy_low\\\",\\n        })\\n    if \\\"high_bcs\\\" in entry:\\n        all_batches.append({\\n            \\\"types\\\": entry[\\\"high_bcs\\\"][\\\"types\\\"],\\n            \\\"bcs\\\": entry[\\\"high_bcs\\\"][\\\"bcs\\\"],\\n            \\\"source\\\": \\\"greedy_high\\\",\\n        })\\n    for ri, rb in enumerate(entry.get(\\\"random\\\", [])):\\n        all_batches.append({\\n            \\\"types\\\": rb[\\\"types\\\"],\\n            \\\"bcs\\\": rb[\\\"bcs\\\"],\\n            \\\"source\\\": f\\\"random_{ri}\\\",\\n        })\\n\\n    all_batches.sort(key=lambda x: x[\\\"bcs\\\"])\\n\\n    low_group = all_batches[:n_low]\\n    high_group = all_batches[-n_high:]\\n\\n    return low_group, high_group\\n\\n\\ndef evaluate_re(results):\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.67}}"
    }
  }
}
```

</details>

---


### Tool result

_source line 19 · 2026-05-16T06:40:44.185Z_

<details><summary>↩ Tool result · `toolu_01T6Yn5NstWBiZVCAWtEzpMQ`</summary>

```text
{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter '|' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "a81aceed-1d72-4aba-b0b2-803e0752c9ed",
  "uuid": "d44828e1-7dff-469c-bc5b-821f759b074e",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": false, \\\"data\\\": {}, \\\"error\\\": \\\"[ssh_read_only] Command blocked: Shell metacharacter '|' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\\\", \\\"metadata\\\": {}}\"}",
    "structuredContent": {
      "result": "{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter '|' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"
    }
  }
}
```

</details>

---


### Tool call

_source line 20_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01P3fJSeB74iWX4DJTbJhEUU`</summary>

```json
{
  "server": "cqa1-38874",
  "command": "grep -rl \"tum\\|base_url\\|openai\\|OPENAI\" /root/schema-dag-extraction/src/ --include=\"*.py\"",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "a81aceed-1d72-4aba-b0b2-803e0752c9ed",
  "uuid": "4e6120fd-7cf2-4fb5-895f-3297831e175e",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LvbQvuArjkkqxQatoburjU",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3234,
      "cache_read_input_tokens": 26689,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3234
      },
      "output_tokens": 64,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### Tool result

_source line 21 · 2026-05-16T06:40:47.706Z_

<details><summary>↩ Tool result · `toolu_01P3fJSeB74iWX4DJTbJhEUU`</summary>

```text
{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter '|' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "a81aceed-1d72-4aba-b0b2-803e0752c9ed",
  "uuid": "e1581ef2-23e2-45b6-ae43-0a59d9faa8f6",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": false, \\\"data\\\": {}, \\\"error\\\": \\\"[ssh_read_only] Command blocked: Shell metacharacter '|' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\\\", \\\"metadata\\\": {}}\"}",
    "structuredContent": {
      "result": "{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter '|' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"
    }
  }
}
```

</details>

---


### Tool call

_source line 22_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_019QERBrLmMByvejnkx9zUhF`</summary>

```json
{
  "server": "cqa1-38874",
  "command": "find /root/schema-dag-extraction -name \"*.env\" -o -name \".env\"",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "a81aceed-1d72-4aba-b0b2-803e0752c9ed",
  "uuid": "a6f8e266-5ec9-45ef-9fd5-d32e848e6570",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LvbQvuArjkkqxQatoburjU",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3234,
      "cache_read_input_tokens": 26689,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3234
      },
      "output_tokens": 64,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### Tool result

_source line 23 · 2026-05-16T06:40:48.672Z_

<details><summary>↩ Tool result · `toolu_019QERBrLmMByvejnkx9zUhF`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.42}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "a81aceed-1d72-4aba-b0b2-803e0752c9ed",
  "uuid": "c93a0507-7a1a-4505-9572-8a41f6291d62",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.42}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.42}}"
    }
  }
}
```

</details>

---


### Tool call

_source line 24_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01TKFuWvkd9KDYpNs5jryndu`</summary>

```json
{
  "server": "cqa1-38874",
  "command": "grep -rl \"base_url\" /root/schema-dag-extraction/src/ --include=\"*.py\"",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "a81aceed-1d72-4aba-b0b2-803e0752c9ed",
  "uuid": "b164cfd6-3920-470c-b813-048ab1e78b99",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012HsMiJHrHz2nC8jXjXMDuV",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 578,
      "cache_read_input_tokens": 29923,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 578
      },
      "output_tokens": 66,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### Tool result

_source line 25 · 2026-05-16T06:40:52.741Z_

<details><summary>↩ Tool result · `toolu_01TKFuWvkd9KDYpNs5jryndu`</summary>

```text
{"result":"{\"success\": false, \"data\": {\"stdout\": \"\", \"stderr\": \"\", \"return_code\": 1}, \"error\": \"exit code 1\", \"metadata\": {\"elapsed_seconds\": 0.69}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "a81aceed-1d72-4aba-b0b2-803e0752c9ed",
  "uuid": "c1c8b515-5c47-47e7-ae8c-a98e1d4569a5",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": false, \\\"data\\\": {\\\"stdout\\\": \\\"\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 1}, \\\"error\\\": \\\"exit code 1\\\", \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.69}}\"}",
    "structuredContent": {
      "result": "{\"success\": false, \"data\": {\"stdout\": \"\", \"stderr\": \"\", \"return_code\": 1}, \"error\": \"exit code 1\", \"metadata\": {\"elapsed_seconds\": 0.69}}"
    }
  }
}
```

</details>

---


### Tool call

_source line 26_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01E65fESrjrGi9Mxs77BJVj1`</summary>

```json
{
  "server": "cqa1-38874",
  "command": "grep -rl \"openai\" /root/schema-dag-extraction/src/ --include=\"*.py\"",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "a81aceed-1d72-4aba-b0b2-803e0752c9ed",
  "uuid": "e62cf489-04dc-4c3b-be89-a9cc558a1e11",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012HsMiJHrHz2nC8jXjXMDuV",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 578,
      "cache_read_input_tokens": 29923,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 578
      },
      "output_tokens": 66,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### Tool call

_source line 27_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01H2r2p9bqjPficTJdRuhFEy`</summary>

```json
{
  "server": "cqa1-38874",
  "command": "grep -rl \"openai\" /root/schema-dag-extraction/ --include=\"*.py\"",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "a81aceed-1d72-4aba-b0b2-803e0752c9ed",
  "uuid": "c6c9c983-55c1-4e28-8ffc-50fa508fb06c",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012HsMiJHrHz2nC8jXjXMDuV",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 578,
      "cache_read_input_tokens": 29923,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 578
      },
      "output_tokens": 66,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### Tool result

_source line 28 · 2026-05-16T06:40:53.482Z_

<details><summary>↩ Tool result · `toolu_01E65fESrjrGi9Mxs77BJVj1`</summary>

```text
{"result":"{\"success\": false, \"data\": {\"stdout\": \"\", \"stderr\": \"\", \"return_code\": 1}, \"error\": \"exit code 1\", \"metadata\": {\"elapsed_seconds\": 0.41}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "a81aceed-1d72-4aba-b0b2-803e0752c9ed",
  "uuid": "6365d5ac-d339-4498-807f-2dd14f952d0d",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": false, \\\"data\\\": {\\\"stdout\\\": \\\"\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 1}, \\\"error\\\": \\\"exit code 1\\\", \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.41}}\"}",
    "structuredContent": {
      "result": "{\"success\": false, \"data\": {\"stdout\": \"\", \"stderr\": \"\", \"return_code\": 1}, \"error\": \"exit code 1\", \"metadata\": {\"elapsed_seconds\": 0.41}}"
    }
  }
}
```

</details>

---


### Tool result

_source line 29 · 2026-05-16T06:40:54.257Z_

<details><summary>↩ Tool result · `toolu_01H2r2p9bqjPficTJdRuhFEy`</summary>

```text
{"result":"{\"success\": false, \"data\": {\"stdout\": \"\", \"stderr\": \"\", \"return_code\": 1}, \"error\": \"exit code 1\", \"metadata\": {\"elapsed_seconds\": 0.76}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "a81aceed-1d72-4aba-b0b2-803e0752c9ed",
  "uuid": "4c872264-e73d-4925-bf82-f9dd15aa50c2",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": false, \\\"data\\\": {\\\"stdout\\\": \\\"\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 1}, \\\"error\\\": \\\"exit code 1\\\", \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.76}}\"}",
    "structuredContent": {
      "result": "{\"success\": false, \"data\": {\"stdout\": \"\", \"stderr\": \"\", \"return_code\": 1}, \"error\": \"exit code 1\", \"metadata\": {\"elapsed_seconds\": 0.76}}"
    }
  }
}
```

</details>

---


### Assistant

_source line 30_

<details><summary>Logged reasoning block</summary>

```text
No existing OpenAI code found. Let me look at more of the existing FewRel formal script to understand how it calls vLLM/local model, then I'll write a GPT-4o-mini variant. Let me also check the run_extraction.py for the prompt builder.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "a81aceed-1d72-4aba-b0b2-803e0752c9ed",
  "uuid": "0d975f86-c259-4946-9dee-6716a10a76e6",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014MyXh5ToK3eZkD2KQzDxLf",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 665,
      "cache_read_input_tokens": 30501,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 665
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### Assistant

_source line 31_

项目中没有现有的 OpenAI 代码。让我继续看 `run_fewrel_formal.py` 的推理部分和 prompt builder。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "a81aceed-1d72-4aba-b0b2-803e0752c9ed",
  "uuid": "56a5e01b-5cba-4ef3-becf-224201ee7c23",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014MyXh5ToK3eZkD2KQzDxLf",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 665,
      "cache_read_input_tokens": 30501,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 665
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### Tool call

_source line 32_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_013sXRvNWWEtA8Mx5fRMy6JT`</summary>

```json
{
  "server": "cqa1-38874",
  "command": "wc -l /root/schema-dag-extraction/src/run_fewrel_formal.py",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "a81aceed-1d72-4aba-b0b2-803e0752c9ed",
  "uuid": "1ad7295d-0380-47f4-84d0-af05e4d11e8c",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014MyXh5ToK3eZkD2KQzDxLf",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 665,
      "cache_read_input_tokens": 30501,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 665
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### Tool call

_source line 33_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01P8vHxC9KzR6vuTpgH6jpHR`</summary>

```json
{
  "server": "cqa1-38874",
  "command": "grep -n \"def \" /root/schema-dag-extraction/src/run_fewrel_formal.py",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "a81aceed-1d72-4aba-b0b2-803e0752c9ed",
  "uuid": "17d6c7f8-5a11-4526-80e6-96351baeffdb",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014MyXh5ToK3eZkD2KQzDxLf",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 665,
      "cache_read_input_tokens": 30501,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 665
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### Tool result

_source line 34 · 2026-05-16T06:41:01.265Z_

<details><summary>↩ Tool result · `toolu_013sXRvNWWEtA8Mx5fRMy6JT`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"399 /root/schema-dag-extraction/src/run_fewrel_formal.py\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.67}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "a81aceed-1d72-4aba-b0b2-803e0752c9ed",
  "uuid": "c12e3001-f492-4e36-a46d-65c5c1ccf4f9",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"399 /root/schema-dag-extraction/src/run_fewrel_formal.py\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.67}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"399 /root/schema-dag-extraction/src/run_fewrel_formal.py\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.67}}"
    }
  }
}
```

</details>

---


### Tool result

_source line 35 · 2026-05-16T06:41:01.742Z_

<details><summary>↩ Tool result · `toolu_01P8vHxC9KzR6vuTpgH6jpHR`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"44:def evaluate_re(results):\\n81:def run_re_extraction(model_path, samples, batch_config, relation_defs, max_model_len=4096, gpu_memory_utilization=0.95):\\n169:def stage_preprocess(args):\\n316:def stage_extract(args):\\n351:def main():\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.47}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "a81aceed-1d72-4aba-b0b2-803e0752c9ed",
  "uuid": "8ce4e743-6842-40e9-bc55-1583dc526747",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"44:def evaluate_re(results):\\\\n81:def run_re_extraction(model_path, samples, batch_config, relation_defs, max_model_len=4096, gpu_memory_utilization=0.95):\\\\n169:def stage_preprocess(args):\\\\n316:def stage_extract(args):\\\\n351:def main():\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.47}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"44:def evaluate_re(results):\\n81:def run_re_extraction(model_path, samples, batch_config, relation_defs, max_model_len=4096, gpu_memory_utilization=0.95):\\n169:def stage_preprocess(args):\\n316:def stage_extract(args):\\n351:def main():\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.47}}"
    }
  }
}
```

</details>

---


### Tool call

_source line 36_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_012Zshy2dpj59GnoyVbJEPyn`</summary>

```json
{
  "server": "cqa1-38874",
  "command": "grep -n \"def \" /root/schema-dag-extraction/src/run_fewrel_v2_bcs.py",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "a81aceed-1d72-4aba-b0b2-803e0752c9ed",
  "uuid": "016f8686-e29f-4635-9fcb-e0e46d13dd9e",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014MyXh5ToK3eZkD2KQzDxLf",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 665,
      "cache_read_input_tokens": 30501,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 665
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### Tool result

_source line 37 · 2026-05-16T06:41:02.599Z_

<details><summary>↩ Tool result · `toolu_012Zshy2dpj59GnoyVbJEPyn`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"45:def select_bcs_groups(batch_config_path, count_key=\\\"count_8\\\", n_low=5, n_high=5):\\n80:def evaluate_re(results):\\n107:def bootstrap_delta_ci(low_accs, high_accs, n_bootstrap=10000, seed=42):\\n139:def stage_preprocess(args):\\n221:def stage_extract(args):\\n363:def run_analysis(results, n_bootstrap=10000, seed=42):\\n414:def main():\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.4}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "a81aceed-1d72-4aba-b0b2-803e0752c9ed",
  "uuid": "7624b996-0e58-494b-b67a-39f33b5dc80b",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"45:def select_bcs_groups(batch_config_path, count_key=\\\\\\\"count_8\\\\\\\", n_low=5, n_high=5):\\\\n80:def evaluate_re(results):\\\\n107:def bootstrap_delta_ci(low_accs, high_accs, n_bootstrap=10000, seed=42):\\\\n139:def stage_preprocess(args):\\\\n221:def stage_extract(args):\\\\n363:def run_analysis(results, n_bootstrap=10000, seed=42):\\\\n414:def main():\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.4}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"45:def select_bcs_groups(batch_config_path, count_key=\\\"count_8\\\", n_low=5, n_high=5):\\n80:def evaluate_re(results):\\n107:def bootstrap_delta_ci(low_accs, high_accs, n_bootstrap=10000, seed=42):\\n139:def stage_preprocess(args):\\n221:def stage_extract(args):\\n363:def run_analysis(results, n_bootstrap=10000, seed=42):\\n414:def main():\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.4}}"
    }
  }
}
```

</details>

---


### Tool call

_source line 38_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_013YshZ2khzd3THviPkgMKQF`</summary>

```json
{
  "server": "cqa1-38874",
  "command": "tail -n +81 /root/schema-dag-extraction/src/run_fewrel_formal.py",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "a81aceed-1d72-4aba-b0b2-803e0752c9ed",
  "uuid": "6a324359-0586-4a45-a1cc-b82eaa0e3098",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BXFt4rvTeYMo9565CdtSmT",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1028,
      "cache_read_input_tokens": 31166,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1028
      },
      "output_tokens": 64,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### Tool result

_source line 39 · 2026-05-16T06:41:06.496Z_

<details><summary>↩ Tool result · `toolu_013YshZ2khzd3THviPkgMKQF`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"def run_re_extraction(model_path, samples, batch_config, relation_defs, max_model_len=4096, gpu_memory_utilization=0.95):\\n    \\\"\\\"\\\"Run RE extraction using vLLM with constrained JSON decoding.\\\"\\\"\\\"\\n    sys.path.insert(0, str(BASE_DIR / \\\"src\\\"))\\n    from run_extraction import build_json_schema_re, build_prompt_v2_re\\n    from vllm import LLM, SamplingParams\\n    from vllm.sampling_params import StructuredOutputsParams\\n\\n    llm = LLM(model=model_path, max_model_len=max_model_len,\\n              trust_remote_code=True, dtype=\\\"bfloat16\\\",\\n              gpu_memory_utilization=gpu_memory_utilization, enforce_eager=True, disable_log_stats=True)\\n\\n    tokenizer = llm.get_tokenizer()\\n    _model_id = getattr(tokenizer, 'name_or_path', '') or model_path\\n    _needs_chat_template = any(kw in _model_id.lower() for kw in ['llama', 'mistral', 'gemma', 'phi'])\\n    if _needs_chat_template:\\n        logger.info(\\\"Chat template enabled for model: %s\\\", _model_id)\\n\\n    all_results = []\\n    sample_id_map = {id(s): i for i, s in enumerate(samples)}\\n\\n    for count_key, strategies in batch_config.items():\\n        batches_to_run = []\\n        if \\\"low_bcs\\\" in strategies:\\n            batches_to_run.append((\\\"low_bcs\\\", strategies[\\\"low_bcs\\\"][\\\"types\\\"], strategies[\\\"low_bcs\\\"][\\\"bcs\\\"]))\\n        if \\\"high_bcs\\\" in strategies:\\n            batches_to_run.append((\\\"high_bcs\\\", strategies[\\\"high_bcs\\\"][\\\"types\\\"], strategies[\\\"high_bcs\\\"][\\\"bcs\\\"]))\\n        if \\\"random\\\" in strategies:\\n            for ri, rb in enumerate(strategies[\\\"random\\\"]):\\n                batches_to_run.append((f\\\"random_{ri}\\\", rb[\\\"types\\\"], rb[\\\"bcs\\\"]))\\n\\n        for batch_id, batch_types, batch_bcs in batches_to_run:\\n            full_bid = f\\\"{count_key}_{batch_id}\\\"\\n            type_set = set(batch_types)\\n            batch_samples = [s for s in samples if s[\\\"relation_type\\\"] in type_set]\\n            if not batch_samples:\\n                logger.warning(\\\"No samples for batch %s\\\", full_bid)\\n                continue\\n\\n            logger.info(\\\"Batch %s: %d types, BCS=%.4f, %d samples\\\",\\n                        full_bid, len(batch_types), batch_bcs, len(batch_samples))\\n            schema = build_json_schema_re(batch_types)\\n            structured = StructuredOutputsParams(json=schema)\\n            sampling_params = SamplingParams(max_tokens=64, temperature=0.0, structured_outputs=structured)\\n\\n            prompts = []\\n            sample_refs = []\\n            for s in batch_samples:\\n                p = build_prompt_v2_re(s[\\\"text\\\"], s[\\\"head_entity\\\"], s[\\\"tail_entity\\\"], relation_defs, batch_types)\\n                prompts.append(p)\\n                sample_refs.append(s)\\n\\n            if _needs_chat_template:\\n                prompts = [\\n                    tokenizer.apply_chat_template(\\n                        [{\\\"role\\\": \\\"user\\\", \\\"content\\\": p}],\\n                        tokenize=False,\\n                        add_generation_prompt=True,\\n                    )\\n                    for p in prompts\\n                ]\\n\\n            t0 = time.time()\\n            outputs = llm.generate(prompts, sampling_params)\\n            elapsed = time.time() - t0\\n\\n            for oi, output in enumerate(outputs):\\n                s = sample_refs[oi]\\n                gen_text = output.outputs[0].text\\n                try:\\n                    parsed = json.loads(gen_text)\\n                    pred_rel = parsed.get(\\\"relation\\\", \\\"none\\\")\\n                except json.JSONDecodeError:\\n                    pred_rel = \\\"none\\\"\\n\\n                all_results.append({\\n                    \\\"sample_id\\\": sample_id_map[id(s)], \\\"batch_id\\\": full_bid,\\n                    \\\"count_key\\\": count_key, \\\"batch_types\\\": batch_types, \\\"batch_bcs\\\": batch_bcs,\\n                    \\\"prediction\\\": pred_rel, \\\"ground_truth\\\": s[\\\"relation_type\\\"],\\n                    \\\"head_entity\\\": s[\\\"head_entity\\\"], \\\"tail_entity\\\": s[\\\"tail_entity\\\"],\\n                    \\\"prompt_tokens\\\": len(output.prompt_token_ids),\\n                    \\\"gen_tokens\\\": len(output.outputs[0].token_ids),\\n                    \\\"latency_s\\\": elapsed / len(prompts),\\n      \\n\\n... [截断: 输出过长，省略 6587 字符] ...\\n\\n ~%.0f min (@%.1fs/sample)\\\", total_inferences * est_sec / 60, est_sec)\\n\\n    return str(preprocess_path)\\n\\n\\ndef stage_extract(args):\\n    \\\"\\\"\\\"GPU stage: vLLM imported first inside run_re_extraction, read preprocess config.\\\"\\\"\\\"\\n    preprocess_path = args.preprocess_path or str(\\n        Path(args.output_dir) / f\\\"preprocess_{args.mode}.json\\\"\\n    )\\n    with open(preprocess_path) as f:\\n        config = json.load(f)\\n\\n    results = run_re_extraction(\\n        config[\\\"model_path\\\"], config[\\\"samples\\\"], config[\\\"batch_config\\\"],\\n        config[\\\"relation_defs\\\"], config[\\\"max_model_len\\\"],\\n        config.get(\\\"gpu_memory_utilization\\\", 0.95),\\n    )\\n\\n    output_dir = Path(config[\\\"output_dir\\\"])\\n    mode = config[\\\"mode\\\"]\\n\\n    pred_path = output_dir / f\\\"predictions_{mode}.json\\\"\\n    with open(pred_path, \\\"w\\\") as f:\\n        json.dump(results, f, ensure_ascii=False, indent=2)\\n    logger.info(\\\"Saved %d predictions to %s\\\", len(results), pred_path)\\n\\n    eval_results = evaluate_re(results)\\n    eval_path = output_dir / f\\\"eval_{mode}.json\\\"\\n    with open(eval_path, \\\"w\\\") as f:\\n        json.dump(eval_results, f, indent=2)\\n\\n    logger.info(\\\"=\\\" * 60)\\n    logger.info(\\\"RESULTS (%s)\\\", mode)\\n    logger.info(\\\"=\\\" * 60)\\n    for bid, m in sorted(eval_results.items()):\\n        logger.info(\\\"  %-40s acc=%.4f (%3d/%3d) BCS=%.4f\\\",\\n                    bid, m[\\\"accuracy\\\"], m[\\\"correct\\\"], m[\\\"total\\\"], m[\\\"bcs\\\"])\\n\\n\\ndef main():\\n    parser = argparse.ArgumentParser(description=\\\"FewRel Formal Study\\\")\\n    parser.add_argument(\\\"--model_path\\\", default=\\\"/root/autodl-tmp/.hf_cache/qwen3-32b-fp8/\\\")\\n    parser.add_argument(\\\"--data_path\\\", default=str(BASE_DIR / \\\"data/fewrel_parquet/val.parquet\\\"),\\n                        help=\\\"Primary data parquet (val split)\\\")\\n    parser.add_argument(\\\"--data_path_extra\\\", nargs=\\\"*\\\", default=None,\\n                        help=\\\"Additional parquet files (e.g. train split for full 80 relations)\\\")\\n    parser.add_argument(\\\"--use_all\\\", action=\\\"store_true\\\",\\n                        help=\\\"Load both train+val splits (all 80 relations)\\\")\\n    parser.add_argument(\\\"--types_file\\\", default=str(BASE_DIR / \\\"configs/fewrel_relation_types.json\\\"))\\n    parser.add_argument(\\\"--embeddings_path\\\", default=None, help=\\\"Pre-computed embeddings .pt (Qwen3 or MiniLM)\\\")\\n    parser.add_argument(\\\"--output_dir\\\", default=str(BASE_DIR / \\\"artifacts/fewrel_formal\\\"))\\n    parser.add_argument(\\\"--mode\\\", choices=[\\\"exp1\\\", \\\"exp2\\\", \\\"dry_run\\\"], required=True)\\n    parser.add_argument(\\\"--n_samples\\\", type=int, default=DEFAULT_N_SAMPLES)\\n    parser.add_argument(\\\"--max_model_len\\\", type=int, default=4096)\\n    parser.add_argument(\\\"--seed\\\", type=int, default=42)\\n    parser.add_argument(\\\"--gpu_memory_utilization\\\", type=float, default=0.95)\\n    parser.add_argument(\\\"--dry_run\\\", action=\\\"store_true\\\", help=\\\"Build batches + print summary, no GPU\\\")\\n    parser.add_argument(\\\"--stage\\\", choices=[\\\"preprocess\\\", \\\"extract\\\", \\\"all\\\"], default=\\\"all\\\",\\n                        help=\\\"preprocess=CPU only, extract=GPU only, all=subprocess both\\\")\\n    parser.add_argument(\\\"--preprocess_path\\\", default=None,\\n                        help=\\\"Path to preprocess JSON (for --stage extract)\\\")\\n    args = parser.parse_args()\\n\\n    logging.basicConfig(level=logging.INFO, format=\\\"%(asctime)s %(levelname)s %(message)s\\\")\\n    random.seed(args.seed)\\n\\n    if args.stage == \\\"preprocess\\\":\\n        stage_preprocess(args)\\n    elif args.stage == \\\"extract\\\":\\n        stage_extract(args)\\n    elif args.stage == \\\"all\\\":\\n        preprocess_path = stage_preprocess(args)\\n\\n        if args.dry_run or args.mode == \\\"dry_run\\\":\\n            logger.info(\\\"DRY RUN - stopping before GPU extraction.\\\")\\n            return\\n\\n        logger.info(\\\"=== Launching extract subprocess (vLLM-first) ===\\\")\\n        cmd = [sys.executable, str(Path(__file__).resolve()),\\n               \\\"--stage\\\", \\\"extract\\\",\\n               \\\"--mode\\\", args.mode,\\n               \\\"--output_dir\\\", args.output_dir,\\n               \\\"--preprocess_path\\\", preprocess_path]\\n        subprocess.run(cmd, check=True)\\n\\n\\nif __name__ == \\\"__main__\\\":\\n    main()\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.46}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "a81aceed-1d72-4aba-b0b2-803e0752c9ed",
  "uuid": "0c94e710-e5b4-4fc8-9be9-06d8b88d29e1",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"def run_re_extraction(model_path, samples, batch_config, relation_defs, max_model_len=4096, gpu_memory_utilization=0.95):\\\\n    \\\\\\\"\\\\\\\"\\\\\\\"Run RE extraction using vLLM with constrained JSON decoding.\\\\\\\"\\\\\\\"\\\\\\\"\\\\n    sys.path.insert(0, str(BASE_DIR / \\\\\\\"src\\\\\\\"))\\\\n    from run_extraction import build_json_schema_re, build_prompt_v2_re\\\\n    from vllm import LLM, SamplingParams\\\\n    from vllm.sampling_params import StructuredOutputsParams\\\\n\\\\n    llm = LLM(model=model_path, max_model_len=max_model_len,\\\\n              trust_remote_code=True, dtype=\\\\\\\"bfloat16\\\\\\\",\\\\n              gpu_memory_utilization=gpu_memory_utilization, enforce_eager=True, disable_log_stats=True)\\\\n\\\\n    tokenizer = llm.get_tokenizer()\\\\n    _model_id = getattr(tokenizer, 'name_or_path', '') or model_path\\\\n    _needs_chat_template = any(kw in _model_id.lower() for kw in ['llama', 'mistral', 'gemma', 'phi'])\\\\n    if _needs_chat_template:\\\\n        logger.info(\\\\\\\"Chat template enabled for model: %s\\\\\\\", _model_id)\\\\n\\\\n    all_results = []\\\\n    sample_id_map = {id(s): i for i, s in enumerate(samples)}\\\\n\\\\n    for count_key, strategies in batch_config.items():\\\\n        batches_to_run = []\\\\n        if \\\\\\\"low_bcs\\\\\\\" in strategies:\\\\n            batches_to_run.append((\\\\\\\"low_bcs\\\\\\\", strategies[\\\\\\\"low_bcs\\\\\\\"][\\\\\\\"types\\\\\\\"], strategies[\\\\\\\"low_bcs\\\\\\\"][\\\\\\\"bcs\\\\\\\"]))\\\\n        if \\\\\\\"high_bcs\\\\\\\" in strategies:\\\\n            batches_to_run.append((\\\\\\\"high_bcs\\\\\\\", strategies[\\\\\\\"high_bcs\\\\\\\"][\\\\\\\"types\\\\\\\"], strategies[\\\\\\\"high_bcs\\\\\\\"][\\\\\\\"bcs\\\\\\\"]))\\\\n        if \\\\\\\"random\\\\\\\" in strategies:\\\\n            for ri, rb in enumerate(strategies[\\\\\\\"random\\\\\\\"]):\\\\n                batches_to_run.append((f\\\\\\\"random_{ri}\\\\\\\", rb[\\\\\\\"types\\\\\\\"], rb[\\\\\\\"bcs\\\\\\\"]))\\\\n\\\\n        for batch_id, batch_types, batch_bcs in batches_to_run:\\\\n            full_bid = f\\\\\\\"{count_key}_{batch_id}\\\\\\\"\\\\n            type_set = set(batch_types)\\\\n            batch_samples = [s for s in samples if s[\\\\\\\"relation_type\\\\\\\"] in type_set]\\\\n            if not batch_samples:\\\\n                logger.warning(\\\\\\\"No samples for batch %s\\\\\\\", full_bid)\\\\n                continue\\\\n\\\\n            logger.info(\\\\\\\"Batch %s: %d types, BCS=%.4f, %d samples\\\\\\\",\\\\n                        full_bid, len(batch_types), batch_bcs, len(batch_samples))\\\\n            schema = build_json_schema_re(batch_types)\\\\n            structured = StructuredOutputsParams(json=schema)\\\\n            sampling_params = SamplingParams(max_tokens=64, temperature=0.0, structured_outputs=structured)\\\\n\\\\n            prompts = []\\\\n            sample_refs = []\\\\n            for s in batch_samples:\\\\n                p = build_prompt_v2_re(s[\\\\\\\"text\\\\\\\"], s[\\\\\\\"head_entity\\\\\\\"], s[\\\\\\\"tail_entity\\\\\\\"], relation_defs, batch_types)\\\\n                prompts.append(p)\\\\n                sample_refs.append(s)\\\\n\\\\n            if _needs_chat_template:\\\\n                prompts = [\\\\n                    tokenizer.apply_chat_template(\\\\n                        [{\\\\\\\"role\\\\\\\": \\\\\\\"user\\\\\\\", \\\\\\\"content\\\\\\\": p}],\\\\n                        tokenize=False,\\\\n                        add_generation_prompt=True,\\\\n                    )\\\\n                    for p in prompts\\\\n                ]\\\\n\\\\n            t0 = time.time()\\\\n            outputs = llm.generate(prompts, sampling_params)\\\\n            elapsed = time.time() - t0\\\\n\\\\n            for oi, output in enumerate(outputs):\\\\n                s = sample_refs[oi]\\\\n                gen_text = output.outputs[0].text\\\\n                try:\\\\n                    parsed = json.loads(gen_text)\\\\n                    pred_rel = parsed.get(\\\\\\\"relation\\\\\\\", \\\\\\\"none\\\\\\\")\\\\n                except json.JSONDecodeError:\\\\n                    pred_rel = \\\\\\\"none\\\\\\\"\\\\n\\\\n                all_results.append({\\\\n                    \\\\\\\"sample_id\\\\\\\": sample_id_map[id(s)], \\\\\\\"batch_id\\\\\\\": full_bid,\\\\n                    \\\\\\\"count_key\\\\\\\": count_key, \\\\\\\"batch_types\\\\\\\": batch_types, \\\\\\\"batch_bcs\\\\\\\": batch_bcs,\\\\n                    \\\\\\\"prediction\\\\\\\": pred_rel, \\\\\\\"ground_truth\\\\\\\": s[\\\\\\\"relation_type\\\\\\\"],\\\\n                    \\\\\\\"head_entity\\\\\\\": s[\\\\\\\"head_entity\\\\\\\"], \\\\\\\"tail_entity\\\\\\\": s[\\\\\\\"tail_entity\\\\\\\"],\\\\n                    \\\\\\\"prompt_tokens\\\\\\\": len(output.prompt_token_ids),\\\\n                    \\\\\\\"gen_tokens\\\\\\\": len(output.outputs[0].token_ids),\\\\n                    \\\\\\\"latency_s\\\\\\\": elapsed / len(prompts),\\\\n      \\\\n\\\\n... [截断: 输出过长，省略 6587 字符] ...\\\\n\\\\n ~%.0f min (@%.1fs/sample)\\\\\\\", total_inferences * est_sec / 60, est_sec)\\\\n\\\\n    return str(preprocess_path)\\\\n\\\\n\\\\ndef stage_extract(args):\\\\n    \\\\\\\"\\\\\\\"\\\\\\\"GPU stage: vLLM imported first inside run_re_extraction, read preprocess config.\\\\\\\"\\\\\\\"\\\\\\\"\\\\n    preprocess_path = args.preprocess_path or str(\\\\n        Path(args.output_dir) / f\\\\\\\"preprocess_{args.mode}.json\\\\\\\"\\\\n    )\\\\n    with open(preprocess_path) as f:\\\\n        config = json.load(f)\\\\n\\\\n    results = run_re_extraction(\\\\n        config[\\\\\\\"model_path\\\\\\\"], config[\\\\\\\"samples\\\\\\\"], config[\\\\\\\"batch_config\\\\\\\"],\\\\n        config[\\\\\\\"relation_defs\\\\\\\"], config[\\\\\\\"max_model_len\\\\\\\"],\\\\n        config.get(\\\\\\\"gpu_memory_utilization\\\\\\\", 0.95),\\\\n    )\\\\n\\\\n    output_dir = Path(config[\\\\\\\"output_dir\\\\\\\"])\\\\n    mode = config[\\\\\\\"mode\\\\\\\"]\\\\n\\\\n    pred_path = output_dir / f\\\\\\\"predictions_{mode}.json\\\\\\\"\\\\n    with open(pred_path, \\\\\\\"w\\\\\\\") as f:\\\\n        json.dump(results, f, ensure_ascii=False, indent=2)\\\\n    logger.info(\\\\\\\"Saved %d predictions to %s\\\\\\\", len(results), pred_path)\\\\n\\\\n    eval_results = evaluate_re(results)\\\\n    eval_path = output_dir / f\\\\\\\"eval_{mode}.json\\\\\\\"\\\\n    with open(eval_path, \\\\\\\"w\\\\\\\") as f:\\\\n        json.dump(eval_results, f, indent=2)\\\\n\\\\n    logger.info(\\\\\\\"=\\\\\\\" * 60)\\\\n    logger.info(\\\\\\\"RESULTS (%s)\\\\\\\", mode)\\\\n    logger.info(\\\\\\\"=\\\\\\\" * 60)\\\\n    for bid, m in sorted(eval_results.items()):\\\\n        logger.info(\\\\\\\"  %-40s acc=%.4f (%3d/%3d) BCS=%.4f\\\\\\\",\\\\n                    bid, m[\\\\\\\"accuracy\\\\\\\"], m[\\\\\\\"correct\\\\\\\"], m[\\\\\\\"total\\\\\\\"], m[\\\\\\\"bcs\\\\\\\"])\\\\n\\\\n\\\\ndef main():\\\\n    parser = argparse.ArgumentParser(description=\\\\\\\"FewRel Formal Study\\\\\\\")\\\\n    parser.add_argument(\\\\\\\"--model_path\\\\\\\", default=\\\\\\\"/root/autodl-tmp/.hf_cache/qwen3-32b-fp8/\\\\\\\")\\\\n    parser.add_argument(\\\\\\\"--data_path\\\\\\\", default=str(BASE_DIR / \\\\\\\"data/fewrel_parquet/val.parquet\\\\\\\"),\\\\n                        help=\\\\\\\"Primary data parquet (val split)\\\\\\\")\\\\n    parser.add_argument(\\\\\\\"--data_path_extra\\\\\\\", nargs=\\\\\\\"*\\\\\\\", default=None,\\\\n                        help=\\\\\\\"Additional parquet files (e.g. train split for full 80 relations)\\\\\\\")\\\\n    parser.add_argument(\\\\\\\"--use_all\\\\\\\", action=\\\\\\\"store_true\\\\\\\",\\\\n                        help=\\\\\\\"Load both train+val splits (all 80 relations)\\\\\\\")\\\\n    parser.add_argument(\\\\\\\"--types_file\\\\\\\", default=str(BASE_DIR / \\\\\\\"configs/fewrel_relation_types.json\\\\\\\"))\\\\n    parser.add_argument(\\\\\\\"--embeddings_path\\\\\\\", default=None, help=\\\\\\\"Pre-computed embeddings .pt (Qwen3 or MiniLM)\\\\\\\")\\\\n    parser.add_argument(\\\\\\\"--output_dir\\\\\\\", default=str(BASE_DIR / \\\\\\\"artifacts/fewrel_formal\\\\\\\"))\\\\n    parser.add_argument(\\\\\\\"--mode\\\\\\\", choices=[\\\\\\\"exp1\\\\\\\", \\\\\\\"exp2\\\\\\\", \\\\\\\"dry_run\\\\\\\"], required=True)\\\\n    parser.add_argument(\\\\\\\"--n_samples\\\\\\\", type=int, default=DEFAULT_N_SAMPLES)\\\\n    parser.add_argument(\\\\\\\"--max_model_len\\\\\\\", type=int, default=4096)\\\\n    parser.add_argument(\\\\\\\"--seed\\\\\\\", type=int, default=42)\\\\n    parser.add_argument(\\\\\\\"--gpu_memory_utilization\\\\\\\", type=float, default=0.95)\\\\n    parser.add_argument(\\\\\\\"--dry_run\\\\\\\", action=\\\\\\\"store_true\\\\\\\", help=\\\\\\\"Build batches + print summary, no GPU\\\\\\\")\\\\n    parser.add_argument(\\\\\\\"--stage\\\\\\\", choices=[\\\\\\\"preprocess\\\\\\\", \\\\\\\"extract\\\\\\\", \\\\\\\"all\\\\\\\"], default=\\\\\\\"all\\\\\\\",\\\\n                        help=\\\\\\\"preprocess=CPU only, extract=GPU only, all=subprocess both\\\\\\\")\\\\n    parser.add_argument(\\\\\\\"--preprocess_path\\\\\\\", default=None,\\\\n                        help=\\\\\\\"Path to preprocess JSON (for --stage extract)\\\\\\\")\\\\n    args = parser.parse_args()\\\\n\\\\n    logging.basicConfig(level=logging.INFO, format=\\\\\\\"%(asctime)s %(levelname)s %(message)s\\\\\\\")\\\\n    random.seed(args.seed)\\\\n\\\\n    if args.stage == \\\\\\\"preprocess\\\\\\\":\\\\n        stage_preprocess(args)\\\\n    elif args.stage == \\\\\\\"extract\\\\\\\":\\\\n        stage_extract(args)\\\\n    elif args.stage == \\\\\\\"all\\\\\\\":\\\\n        preprocess_path = stage_preprocess(args)\\\\n\\\\n        if args.dry_run or args.mode == \\\\\\\"dry_run\\\\\\\":\\\\n            logger.info(\\\\\\\"DRY RUN - stopping before GPU extraction.\\\\\\\")\\\\n            return\\\\n\\\\n        logger.info(\\\\\\\"=== Launching extract subprocess (vLLM-first) ===\\\\\\\")\\\\n        cmd = [sys.executable, str(Path(__file__).resolve()),\\\\n               \\\\\\\"--stage\\\\\\\", \\\\\\\"extract\\\\\\\",\\\\n               \\\\\\\"--mode\\\\\\\", args.mode,\\\\n               \\\\\\\"--output_dir\\\\\\\", args.output_dir,\\\\n               \\\\\\\"--preprocess_path\\\\\\\", preprocess_path]\\\\n        subprocess.run(cmd, check=True)\\\\n\\\\n\\\\nif __name__ == \\\\\\\"__main__\\\\\\\":\\\\n    main()\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.46}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"def run_re_extraction(model_path, samples, batch_config, relation_defs, max_model_len=4096, gpu_memory_utilization=0.95):\\n    \\\"\\\"\\\"Run RE extraction using vLLM with constrained JSON decoding.\\\"\\\"\\\"\\n    sys.path.insert(0, str(BASE_DIR / \\\"src\\\"))\\n    from run_extraction import build_json_schema_re, build_prompt_v2_re\\n    from vllm import LLM, SamplingParams\\n    from vllm.sampling_params import StructuredOutputsParams\\n\\n    llm = LLM(model=model_path, max_model_len=max_model_len,\\n              trust_remote_code=True, dtype=\\\"bfloat16\\\",\\n              gpu_memory_utilization=gpu_memory_utilization, enforce_eager=True, disable_log_stats=True)\\n\\n    tokenizer = llm.get_tokenizer()\\n    _model_id = getattr(tokenizer, 'name_or_path', '') or model_path\\n    _needs_chat_template = any(kw in _model_id.lower() for kw in ['llama', 'mistral', 'gemma', 'phi'])\\n    if _needs_chat_template:\\n        logger.info(\\\"Chat template enabled for model: %s\\\", _model_id)\\n\\n    all_results = []\\n    sample_id_map = {id(s): i for i, s in enumerate(samples)}\\n\\n    for count_key, strategies in batch_config.items():\\n        batches_to_run = []\\n        if \\\"low_bcs\\\" in strategies:\\n            batches_to_run.append((\\\"low_bcs\\\", strategies[\\\"low_bcs\\\"][\\\"types\\\"], strategies[\\\"low_bcs\\\"][\\\"bcs\\\"]))\\n        if \\\"high_bcs\\\" in strategies:\\n            batches_to_run.append((\\\"high_bcs\\\", strategies[\\\"high_bcs\\\"][\\\"types\\\"], strategies[\\\"high_bcs\\\"][\\\"bcs\\\"]))\\n        if \\\"random\\\" in strategies:\\n            for ri, rb in enumerate(strategies[\\\"random\\\"]):\\n                batches_to_run.append((f\\\"random_{ri}\\\", rb[\\\"types\\\"], rb[\\\"bcs\\\"]))\\n\\n        for batch_id, batch_types, batch_bcs in batches_to_run:\\n            full_bid = f\\\"{count_key}_{batch_id}\\\"\\n            type_set = set(batch_types)\\n            batch_samples = [s for s in samples if s[\\\"relation_type\\\"] in type_set]\\n            if not batch_samples:\\n                logger.warning(\\\"No samples for batch %s\\\", full_bid)\\n                continue\\n\\n            logger.info(\\\"Batch %s: %d types, BCS=%.4f, %d samples\\\",\\n                        full_bid, len(batch_types), batch_bcs, len(batch_samples))\\n            schema = build_json_schema_re(batch_types)\\n            structured = StructuredOutputsParams(json=schema)\\n            sampling_params = SamplingParams(max_tokens=64, temperature=0.0, structured_outputs=structured)\\n\\n            prompts = []\\n            sample_refs = []\\n            for s in batch_samples:\\n                p = build_prompt_v2_re(s[\\\"text\\\"], s[\\\"head_entity\\\"], s[\\\"tail_entity\\\"], relation_defs, batch_types)\\n                prompts.append(p)\\n                sample_refs.append(s)\\n\\n            if _needs_chat_template:\\n                prompts = [\\n                    tokenizer.apply_chat_template(\\n                        [{\\\"role\\\": \\\"user\\\", \\\"content\\\": p}],\\n                        tokenize=False,\\n                        add_generation_prompt=True,\\n                    )\\n                    for p in prompts\\n                ]\\n\\n            t0 = time.time()\\n            outputs = llm.generate(prompts, sampling_params)\\n            elapsed = time.time() - t0\\n\\n            for oi, output in enumerate(outputs):\\n                s = sample_refs[oi]\\n                gen_text = output.outputs[0].text\\n                try:\\n                    parsed = json.loads(gen_text)\\n                    pred_rel = parsed.get(\\\"relation\\\", \\\"none\\\")\\n                except json.JSONDecodeError:\\n                    pred_rel = \\\"none\\\"\\n\\n                all_results.append({\\n                    \\\"sample_id\\\": sample_id_map[id(s)], \\\"batch_id\\\": full_bid,\\n                    \\\"count_key\\\": count_key, \\\"batch_types\\\": batch_types, \\\"batch_bcs\\\": batch_bcs,\\n                    \\\"prediction\\\": pred_rel, \\\"ground_truth\\\": s[\\\"relation_type\\\"],\\n                    \\\"head_entity\\\": s[\\\"head_entity\\\"], \\\"tail_entity\\\": s[\\\"tail_entity\\\"],\\n                    \\\"prompt_tokens\\\": len(output.prompt_token_ids),\\n                    \\\"gen_tokens\\\": len(output.outputs[0].token_ids),\\n                    \\\"latency_s\\\": elapsed / len(prompts),\\n      \\n\\n... [截断: 输出过长，省略 6587 字符] ...\\n\\n ~%.0f min (@%.1fs/sample)\\\", total_inferences * est_sec / 60, est_sec)\\n\\n    return str(preprocess_path)\\n\\n\\ndef stage_extract(args):\\n    \\\"\\\"\\\"GPU stage: vLLM imported first inside run_re_extraction, read preprocess config.\\\"\\\"\\\"\\n    preprocess_path = args.preprocess_path or str(\\n        Path(args.output_dir) / f\\\"preprocess_{args.mode}.json\\\"\\n    )\\n    with open(preprocess_path) as f:\\n        config = json.load(f)\\n\\n    results = run_re_extraction(\\n        config[\\\"model_path\\\"], config[\\\"samples\\\"], config[\\\"batch_config\\\"],\\n        config[\\\"relation_defs\\\"], config[\\\"max_model_len\\\"],\\n        config.get(\\\"gpu_memory_utilization\\\", 0.95),\\n    )\\n\\n    output_dir = Path(config[\\\"output_dir\\\"])\\n    mode = config[\\\"mode\\\"]\\n\\n    pred_path = output_dir / f\\\"predictions_{mode}.json\\\"\\n    with open(pred_path, \\\"w\\\") as f:\\n        json.dump(results, f, ensure_ascii=False, indent=2)\\n    logger.info(\\\"Saved %d predictions to %s\\\", len(results), pred_path)\\n\\n    eval_results = evaluate_re(results)\\n    eval_path = output_dir / f\\\"eval_{mode}.json\\\"\\n    with open(eval_path, \\\"w\\\") as f:\\n        json.dump(eval_results, f, indent=2)\\n\\n    logger.info(\\\"=\\\" * 60)\\n    logger.info(\\\"RESULTS (%s)\\\", mode)\\n    logger.info(\\\"=\\\" * 60)\\n    for bid, m in sorted(eval_results.items()):\\n        logger.info(\\\"  %-40s acc=%.4f (%3d/%3d) BCS=%.4f\\\",\\n                    bid, m[\\\"accuracy\\\"], m[\\\"correct\\\"], m[\\\"total\\\"], m[\\\"bcs\\\"])\\n\\n\\ndef main():\\n    parser = argparse.ArgumentParser(description=\\\"FewRel Formal Study\\\")\\n    parser.add_argument(\\\"--model_path\\\", default=\\\"/root/autodl-tmp/.hf_cache/qwen3-32b-fp8/\\\")\\n    parser.add_argument(\\\"--data_path\\\", default=str(BASE_DIR / \\\"data/fewrel_parquet/val.parquet\\\"),\\n                        help=\\\"Primary data parquet (val split)\\\")\\n    parser.add_argument(\\\"--data_path_extra\\\", nargs=\\\"*\\\", default=None,\\n                        help=\\\"Additional parquet files (e.g. train split for full 80 relations)\\\")\\n    parser.add_argument(\\\"--use_all\\\", action=\\\"store_true\\\",\\n                        help=\\\"Load both train+val splits (all 80 relations)\\\")\\n    parser.add_argument(\\\"--types_file\\\", default=str(BASE_DIR / \\\"configs/fewrel_relation_types.json\\\"))\\n    parser.add_argument(\\\"--embeddings_path\\\", default=None, help=\\\"Pre-computed embeddings .pt (Qwen3 or MiniLM)\\\")\\n    parser.add_argument(\\\"--output_dir\\\", default=str(BASE_DIR / \\\"artifacts/fewrel_formal\\\"))\\n    parser.add_argument(\\\"--mode\\\", choices=[\\\"exp1\\\", \\\"exp2\\\", \\\"dry_run\\\"], required=True)\\n    parser.add_argument(\\\"--n_samples\\\", type=int, default=DEFAULT_N_SAMPLES)\\n    parser.add_argument(\\\"--max_model_len\\\", type=int, default=4096)\\n    parser.add_argument(\\\"--seed\\\", type=int, default=42)\\n    parser.add_argument(\\\"--gpu_memory_utilization\\\", type=float, default=0.95)\\n    parser.add_argument(\\\"--dry_run\\\", action=\\\"store_true\\\", help=\\\"Build batches + print summary, no GPU\\\")\\n    parser.add_argument(\\\"--stage\\\", choices=[\\\"preprocess\\\", \\\"extract\\\", \\\"all\\\"], default=\\\"all\\\",\\n                        help=\\\"preprocess=CPU only, extract=GPU only, all=subprocess both\\\")\\n    parser.add_argument(\\\"--preprocess_path\\\", default=None,\\n                        help=\\\"Path to preprocess JSON (for --stage extract)\\\")\\n    args = parser.parse_args()\\n\\n    logging.basicConfig(level=logging.INFO, format=\\\"%(asctime)s %(levelname)s %(message)s\\\")\\n    random.seed(args.seed)\\n\\n    if args.stage == \\\"preprocess\\\":\\n        stage_preprocess(args)\\n    elif args.stage == \\\"extract\\\":\\n        stage_extract(args)\\n    elif args.stage == \\\"all\\\":\\n        preprocess_path = stage_preprocess(args)\\n\\n        if args.dry_run or args.mode == \\\"dry_run\\\":\\n            logger.info(\\\"DRY RUN - stopping before GPU extraction.\\\")\\n            return\\n\\n        logger.info(\\\"=== Launching extract subprocess (vLLM-first) ===\\\")\\n        cmd = [sys.executable, str(Path(__file__).resolve()),\\n               \\\"--stage\\\", \\\"extract\\\",\\n               \\\"--mode\\\", args.mode,\\n               \\\"--output_dir\\\", args.output_dir,\\n               \\\"--preprocess_path\\\", preprocess_path]\\n        subprocess.run(cmd, check=True)\\n\\n\\nif __name__ == \\\"__main__\\\":\\n    main()\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.46}}"
    }
  }
}
```

</details>

---


### Assistant

_source line 40_

<details><summary>Logged reasoning block</summary>

```text
Now I need to look at the `run_extraction.py` to understand `build_prompt_v2_re` and `build_json_schema_re`. Let me also look at the preprocess stage to understand how batches and samples are prepared.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "a81aceed-1d72-4aba-b0b2-803e0752c9ed",
  "uuid": "60b44a51-fe20-4192-b384-8dd16ed8ae68",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014eNqVEu7BxmCECqQSjBAxk",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3354,
      "cache_read_input_tokens": 32194,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3354
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### Assistant

_source line 41_

Now let me look at the prompt builder functions and the preprocess stage.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "a81aceed-1d72-4aba-b0b2-803e0752c9ed",
  "uuid": "b0f5dc19-78b8-45dd-ada3-0020b252f16c",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014eNqVEu7BxmCECqQSjBAxk",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3354,
      "cache_read_input_tokens": 32194,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3354
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### Tool call

_source line 42_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_016BShoupDy6kQzvEfJEVG1a`</summary>

```json
{
  "server": "cqa1-38874",
  "command": "grep -n \"def build_prompt_v2_re\\|def build_json_schema_re\" /root/schema-dag-extraction/src/run_extraction.py",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "a81aceed-1d72-4aba-b0b2-803e0752c9ed",
  "uuid": "f4a0cbd0-707f-45c9-8c34-6ffe4d84212c",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014eNqVEu7BxmCECqQSjBAxk",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3354,
      "cache_read_input_tokens": 32194,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3354
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### Tool result

_source line 43 · 2026-05-16T06:41:11.212Z_

<details><summary>↩ Tool result · `toolu_016BShoupDy6kQzvEfJEVG1a`</summary>

```text
{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter '|' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "a81aceed-1d72-4aba-b0b2-803e0752c9ed",
  "uuid": "ba7643e5-5a76-4b8e-837c-c6b5f5833d65",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": false, \\\"data\\\": {}, \\\"error\\\": \\\"[ssh_read_only] Command blocked: Shell metacharacter '|' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\\\", \\\"metadata\\\": {}}\"}",
    "structuredContent": {
      "result": "{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter '|' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"
    }
  }
}
```

</details>

---


### Tool call

_source line 44_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01LwgFNwYNZaKHvVUrSHWfZf`</summary>

```json
{
  "server": "cqa1-38874",
  "command": "tail -n +169 /root/schema-dag-extraction/src/run_fewrel_formal.py",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "a81aceed-1d72-4aba-b0b2-803e0752c9ed",
  "uuid": "cdd989b8-cf5d-4d89-a6bc-5e0d2d1c22b5",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014eNqVEu7BxmCECqQSjBAxk",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3354,
      "cache_read_input_tokens": 32194,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3354
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### Tool result

_source line 45 · 2026-05-16T06:41:12.212Z_

<details><summary>↩ Tool result · `toolu_01LwgFNwYNZaKHvVUrSHWfZf`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"def stage_preprocess(args):\\n    \\\"\\\"\\\"CPU stage: load data, compute BCS, build batch config, save JSON.\\\"\\\"\\\"\\n    sys.path.insert(0, str(BASE_DIR / \\\"src\\\"))\\n    from fewrel_utils import load_fewrel, get_all_relation_types, sample_balanced\\n    from compute_bcs import load_embeddings, compute_similarity_matrix, compute_bcs\\n    from select_type_batches import select_low_bcs, select_high_bcs, select_random_batches\\n\\n    logger.info(\\\"Loading FewRel data...\\\")\\n    data_paths = [args.data_path]\\n    if args.use_all:\\n        data_paths = [str(BASE_DIR / \\\"data/fewrel_parquet/train.parquet\\\"),\\n                      str(BASE_DIR / \\\"data/fewrel_parquet/val.parquet\\\")]\\n    elif args.data_path_extra:\\n        data_paths.extend(args.data_path_extra)\\n\\n    all_samples = []\\n    for dp in data_paths:\\n        all_samples.extend(load_fewrel(data_path=dp))\\n    all_relations = get_all_relation_types(all_samples)\\n    logger.info(\\\"%d samples, %d relation types from %d file(s)\\\",\\n                len(all_samples), len(all_relations), len(data_paths))\\n\\n    n_per_rel = args.n_samples // len(all_relations)\\n    samples = sample_balanced(all_samples, n_per_rel, seed=args.seed)\\n    logger.info(\\\"Sampled %d (%d per relation, %d relations)\\\",\\n                len(samples), n_per_rel, len(all_relations))\\n\\n    with open(args.types_file) as f:\\n        pid2name = json.load(f)\\n    relation_defs = {name: name for name in pid2name.values()}\\n\\n    if args.embeddings_path:\\n        logger.info(\\\"Loading pre-computed embeddings from %s\\\", args.embeddings_path)\\n        embeddings = load_embeddings(args.embeddings_path)\\n        sample_keys = list(embeddings.keys())[:3]\\n        if sample_keys and all(k in pid2name for k in sample_keys):\\n            embeddings = {pid2name[k]: v for k, v in embeddings.items() if k in pid2name}\\n            logger.info(\\\"Remapped %d PID-keyed embeddings to relation names\\\", len(embeddings))\\n    else:\\n        logger.info(\\\"No --embeddings_path; computing MiniLM embeddings (CPU fallback)\\\")\\n        from run_fewrel_pilot import compute_relation_embeddings_st\\n        embeddings = compute_relation_embeddings_st(pid2name)\\n\\n    import torch\\n    sim_matrix, type_names, type_to_idx = compute_similarity_matrix(embeddings)\\n    logger.info(\\\"Similarity matrix: %d types\\\", len(type_names))\\n\\n    active_types = [t for t in type_names if t in set(all_relations)]\\n    active_idx = {t: type_to_idx[t] for t in active_types}\\n    n_active = len(active_types)\\n    logger.info(\\\"Active types (in both embeddings and data): %d\\\", n_active)\\n\\n    mode = args.mode if args.mode != \\\"dry_run\\\" else \\\"exp1\\\"\\n    batch_config = {}\\n    seen_counts = set()\\n\\n    if mode == \\\"exp1\\\":\\n        for count in EXP1_COUNTS:\\n            count = min(count, n_active)\\n            if count in seen_counts:\\n                continue\\n            seen_counts.add(count)\\n            if count == 1:\\n                solo_batches = [{\\\"types\\\": [t], \\\"bcs\\\": 0.0} for t in active_types]\\n                batch_config[\\\"count_1\\\"] = {\\\"random\\\": solo_batches}\\n            else:\\n                rand = select_random_batches(count, EXP1_RANDOM_PER_COUNT, active_types,\\n                                             sim_matrix, active_idx, args.seed + count)\\n                batch_config[f\\\"count_{count}\\\"] = {\\\"random\\\": rand}\\n\\n    elif mode == \\\"exp2\\\":\\n        for count in EXP2_COUNTS:\\n            count = min(count, n_active)\\n            if count in seen_counts:\\n                continue\\n            seen_counts.add(count)\\n            low = select_low_bcs(count, sim_matrix, active_types, active_idx)\\n            high = select_high_bcs(count, sim_matrix, active_types, active_idx)\\n            rand = select_random_batches(count, EXP2_RANDOM_PER_COUNT, active_types,\\n                                         sim_matrix, active_idx, args.seed + count)\\n            batch_config[f\\\"count_{count}\\\"] = {\\n                \\\"low_bcs\\\": {\\\"types\\\": low, \\\"bcs\\\": compute_bcs(low, sim_matrix, type_to_idx)},\\n                \\\"high_bcs\\\": {\\\"types\\\": high, \\\"bcs\\\": compute_bcs(high, sim_matrix, typ\\n\\n... [截断: 输出过长，省略 2453 字符] ...\\n\\n ~%.0f min (@%.1fs/sample)\\\", total_inferences * est_sec / 60, est_sec)\\n\\n    return str(preprocess_path)\\n\\n\\ndef stage_extract(args):\\n    \\\"\\\"\\\"GPU stage: vLLM imported first inside run_re_extraction, read preprocess config.\\\"\\\"\\\"\\n    preprocess_path = args.preprocess_path or str(\\n        Path(args.output_dir) / f\\\"preprocess_{args.mode}.json\\\"\\n    )\\n    with open(preprocess_path) as f:\\n        config = json.load(f)\\n\\n    results = run_re_extraction(\\n        config[\\\"model_path\\\"], config[\\\"samples\\\"], config[\\\"batch_config\\\"],\\n        config[\\\"relation_defs\\\"], config[\\\"max_model_len\\\"],\\n        config.get(\\\"gpu_memory_utilization\\\", 0.95),\\n    )\\n\\n    output_dir = Path(config[\\\"output_dir\\\"])\\n    mode = config[\\\"mode\\\"]\\n\\n    pred_path = output_dir / f\\\"predictions_{mode}.json\\\"\\n    with open(pred_path, \\\"w\\\") as f:\\n        json.dump(results, f, ensure_ascii=False, indent=2)\\n    logger.info(\\\"Saved %d predictions to %s\\\", len(results), pred_path)\\n\\n    eval_results = evaluate_re(results)\\n    eval_path = output_dir / f\\\"eval_{mode}.json\\\"\\n    with open(eval_path, \\\"w\\\") as f:\\n        json.dump(eval_results, f, indent=2)\\n\\n    logger.info(\\\"=\\\" * 60)\\n    logger.info(\\\"RESULTS (%s)\\\", mode)\\n    logger.info(\\\"=\\\" * 60)\\n    for bid, m in sorted(eval_results.items()):\\n        logger.info(\\\"  %-40s acc=%.4f (%3d/%3d) BCS=%.4f\\\",\\n                    bid, m[\\\"accuracy\\\"], m[\\\"correct\\\"], m[\\\"total\\\"], m[\\\"bcs\\\"])\\n\\n\\ndef main():\\n    parser = argparse.ArgumentParser(description=\\\"FewRel Formal Study\\\")\\n    parser.add_argument(\\\"--model_path\\\", default=\\\"/root/autodl-tmp/.hf_cache/qwen3-32b-fp8/\\\")\\n    parser.add_argument(\\\"--data_path\\\", default=str(BASE_DIR / \\\"data/fewrel_parquet/val.parquet\\\"),\\n                        help=\\\"Primary data parquet (val split)\\\")\\n    parser.add_argument(\\\"--data_path_extra\\\", nargs=\\\"*\\\", default=None,\\n                        help=\\\"Additional parquet files (e.g. train split for full 80 relations)\\\")\\n    parser.add_argument(\\\"--use_all\\\", action=\\\"store_true\\\",\\n                        help=\\\"Load both train+val splits (all 80 relations)\\\")\\n    parser.add_argument(\\\"--types_file\\\", default=str(BASE_DIR / \\\"configs/fewrel_relation_types.json\\\"))\\n    parser.add_argument(\\\"--embeddings_path\\\", default=None, help=\\\"Pre-computed embeddings .pt (Qwen3 or MiniLM)\\\")\\n    parser.add_argument(\\\"--output_dir\\\", default=str(BASE_DIR / \\\"artifacts/fewrel_formal\\\"))\\n    parser.add_argument(\\\"--mode\\\", choices=[\\\"exp1\\\", \\\"exp2\\\", \\\"dry_run\\\"], required=True)\\n    parser.add_argument(\\\"--n_samples\\\", type=int, default=DEFAULT_N_SAMPLES)\\n    parser.add_argument(\\\"--max_model_len\\\", type=int, default=4096)\\n    parser.add_argument(\\\"--seed\\\", type=int, default=42)\\n    parser.add_argument(\\\"--gpu_memory_utilization\\\", type=float, default=0.95)\\n    parser.add_argument(\\\"--dry_run\\\", action=\\\"store_true\\\", help=\\\"Build batches + print summary, no GPU\\\")\\n    parser.add_argument(\\\"--stage\\\", choices=[\\\"preprocess\\\", \\\"extract\\\", \\\"all\\\"], default=\\\"all\\\",\\n                        help=\\\"preprocess=CPU only, extract=GPU only, all=subprocess both\\\")\\n    parser.add_argument(\\\"--preprocess_path\\\", default=None,\\n                        help=\\\"Path to preprocess JSON (for --stage extract)\\\")\\n    args = parser.parse_args()\\n\\n    logging.basicConfig(level=logging.INFO, format=\\\"%(asctime)s %(levelname)s %(message)s\\\")\\n    random.seed(args.seed)\\n\\n    if args.stage == \\\"preprocess\\\":\\n        stage_preprocess(args)\\n    elif args.stage == \\\"extract\\\":\\n        stage_extract(args)\\n    elif args.stage == \\\"all\\\":\\n        preprocess_path = stage_preprocess(args)\\n\\n        if args.dry_run or args.mode == \\\"dry_run\\\":\\n            logger.info(\\\"DRY RUN - stopping before GPU extraction.\\\")\\n            return\\n\\n        logger.info(\\\"=== Launching extract subprocess (vLLM-first) ===\\\")\\n        cmd = [sys.executable, str(Path(__file__).resolve()),\\n               \\\"--stage\\\", \\\"extract\\\",\\n               \\\"--mode\\\", args.mode,\\n               \\\"--output_dir\\\", args.output_dir,\\n               \\\"--preprocess_path\\\", preprocess_path]\\n        subprocess.run(cmd, check=True)\\n\\n\\nif __name__ == \\\"__main__\\\":\\n    main()\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.41}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "a81aceed-1d72-4aba-b0b2-803e0752c9ed",
  "uuid": "bfcb92ad-68c8-4913-84b6-8e3c3a140591",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"def stage_preprocess(args):\\\\n    \\\\\\\"\\\\\\\"\\\\\\\"CPU stage: load data, compute BCS, build batch config, save JSON.\\\\\\\"\\\\\\\"\\\\\\\"\\\\n    sys.path.insert(0, str(BASE_DIR / \\\\\\\"src\\\\\\\"))\\\\n    from fewrel_utils import load_fewrel, get_all_relation_types, sample_balanced\\\\n    from compute_bcs import load_embeddings, compute_similarity_matrix, compute_bcs\\\\n    from select_type_batches import select_low_bcs, select_high_bcs, select_random_batches\\\\n\\\\n    logger.info(\\\\\\\"Loading FewRel data...\\\\\\\")\\\\n    data_paths = [args.data_path]\\\\n    if args.use_all:\\\\n        data_paths = [str(BASE_DIR / \\\\\\\"data/fewrel_parquet/train.parquet\\\\\\\"),\\\\n                      str(BASE_DIR / \\\\\\\"data/fewrel_parquet/val.parquet\\\\\\\")]\\\\n    elif args.data_path_extra:\\\\n        data_paths.extend(args.data_path_extra)\\\\n\\\\n    all_samples = []\\\\n    for dp in data_paths:\\\\n        all_samples.extend(load_fewrel(data_path=dp))\\\\n    all_relations = get_all_relation_types(all_samples)\\\\n    logger.info(\\\\\\\"%d samples, %d relation types from %d file(s)\\\\\\\",\\\\n                len(all_samples), len(all_relations), len(data_paths))\\\\n\\\\n    n_per_rel = args.n_samples // len(all_relations)\\\\n    samples = sample_balanced(all_samples, n_per_rel, seed=args.seed)\\\\n    logger.info(\\\\\\\"Sampled %d (%d per relation, %d relations)\\\\\\\",\\\\n                len(samples), n_per_rel, len(all_relations))\\\\n\\\\n    with open(args.types_file) as f:\\\\n        pid2name = json.load(f)\\\\n    relation_defs = {name: name for name in pid2name.values()}\\\\n\\\\n    if args.embeddings_path:\\\\n        logger.info(\\\\\\\"Loading pre-computed embeddings from %s\\\\\\\", args.embeddings_path)\\\\n        embeddings = load_embeddings(args.embeddings_path)\\\\n        sample_keys = list(embeddings.keys())[:3]\\\\n        if sample_keys and all(k in pid2name for k in sample_keys):\\\\n            embeddings = {pid2name[k]: v for k, v in embeddings.items() if k in pid2name}\\\\n            logger.info(\\\\\\\"Remapped %d PID-keyed embeddings to relation names\\\\\\\", len(embeddings))\\\\n    else:\\\\n        logger.info(\\\\\\\"No --embeddings_path; computing MiniLM embeddings (CPU fallback)\\\\\\\")\\\\n        from run_fewrel_pilot import compute_relation_embeddings_st\\\\n        embeddings = compute_relation_embeddings_st(pid2name)\\\\n\\\\n    import torch\\\\n    sim_matrix, type_names, type_to_idx = compute_similarity_matrix(embeddings)\\\\n    logger.info(\\\\\\\"Similarity matrix: %d types\\\\\\\", len(type_names))\\\\n\\\\n    active_types = [t for t in type_names if t in set(all_relations)]\\\\n    active_idx = {t: type_to_idx[t] for t in active_types}\\\\n    n_active = len(active_types)\\\\n    logger.info(\\\\\\\"Active types (in both embeddings and data): %d\\\\\\\", n_active)\\\\n\\\\n    mode = args.mode if args.mode != \\\\\\\"dry_run\\\\\\\" else \\\\\\\"exp1\\\\\\\"\\\\n    batch_config = {}\\\\n    seen_counts = set()\\\\n\\\\n    if mode == \\\\\\\"exp1\\\\\\\":\\\\n        for count in EXP1_COUNTS:\\\\n            count = min(count, n_active)\\\\n            if count in seen_counts:\\\\n                continue\\\\n            seen_counts.add(count)\\\\n            if count == 1:\\\\n                solo_batches = [{\\\\\\\"types\\\\\\\": [t], \\\\\\\"bcs\\\\\\\": 0.0} for t in active_types]\\\\n                batch_config[\\\\\\\"count_1\\\\\\\"] = {\\\\\\\"random\\\\\\\": solo_batches}\\\\n            else:\\\\n                rand = select_random_batches(count, EXP1_RANDOM_PER_COUNT, active_types,\\\\n                                             sim_matrix, active_idx, args.seed + count)\\\\n                batch_config[f\\\\\\\"count_{count}\\\\\\\"] = {\\\\\\\"random\\\\\\\": rand}\\\\n\\\\n    elif mode == \\\\\\\"exp2\\\\\\\":\\\\n        for count in EXP2_COUNTS:\\\\n            count = min(count, n_active)\\\\n            if count in seen_counts:\\\\n                continue\\\\n            seen_counts.add(count)\\\\n            low = select_low_bcs(count, sim_matrix, active_types, active_idx)\\\\n            high = select_high_bcs(count, sim_matrix, active_types, active_idx)\\\\n            rand = select_random_batches(count, EXP2_RANDOM_PER_COUNT, active_types,\\\\n                                         sim_matrix, active_idx, args.seed + count)\\\\n            batch_config[f\\\\\\\"count_{count}\\\\\\\"] = {\\\\n                \\\\\\\"low_bcs\\\\\\\": {\\\\\\\"types\\\\\\\": low, \\\\\\\"bcs\\\\\\\": compute_bcs(low, sim_matrix, type_to_idx)},\\\\n                \\\\\\\"high_bcs\\\\\\\": {\\\\\\\"types\\\\\\\": high, \\\\\\\"bcs\\\\\\\": compute_bcs(high, sim_matrix, typ\\\\n\\\\n... [截断: 输出过长，省略 2453 字符] ...\\\\n\\\\n ~%.0f min (@%.1fs/sample)\\\\\\\", total_inferences * est_sec / 60, est_sec)\\\\n\\\\n    return str(preprocess_path)\\\\n\\\\n\\\\ndef stage_extract(args):\\\\n    \\\\\\\"\\\\\\\"\\\\\\\"GPU stage: vLLM imported first inside run_re_extraction, read preprocess config.\\\\\\\"\\\\\\\"\\\\\\\"\\\\n    preprocess_path = args.preprocess_path or str(\\\\n        Path(args.output_dir) / f\\\\\\\"preprocess_{args.mode}.json\\\\\\\"\\\\n    )\\\\n    with open(preprocess_path) as f:\\\\n        config = json.load(f)\\\\n\\\\n    results = run_re_extraction(\\\\n        config[\\\\\\\"model_path\\\\\\\"], config[\\\\\\\"samples\\\\\\\"], config[\\\\\\\"batch_config\\\\\\\"],\\\\n        config[\\\\\\\"relation_defs\\\\\\\"], config[\\\\\\\"max_model_len\\\\\\\"],\\\\n        config.get(\\\\\\\"gpu_memory_utilization\\\\\\\", 0.95),\\\\n    )\\\\n\\\\n    output_dir = Path(config[\\\\\\\"output_dir\\\\\\\"])\\\\n    mode = config[\\\\\\\"mode\\\\\\\"]\\\\n\\\\n    pred_path = output_dir / f\\\\\\\"predictions_{mode}.json\\\\\\\"\\\\n    with open(pred_path, \\\\\\\"w\\\\\\\") as f:\\\\n        json.dump(results, f, ensure_ascii=False, indent=2)\\\\n    logger.info(\\\\\\\"Saved %d predictions to %s\\\\\\\", len(results), pred_path)\\\\n\\\\n    eval_results = evaluate_re(results)\\\\n    eval_path = output_dir / f\\\\\\\"eval_{mode}.json\\\\\\\"\\\\n    with open(eval_path, \\\\\\\"w\\\\\\\") as f:\\\\n        json.dump(eval_results, f, indent=2)\\\\n\\\\n    logger.info(\\\\\\\"=\\\\\\\" * 60)\\\\n    logger.info(\\\\\\\"RESULTS (%s)\\\\\\\", mode)\\\\n    logger.info(\\\\\\\"=\\\\\\\" * 60)\\\\n    for bid, m in sorted(eval_results.items()):\\\\n        logger.info(\\\\\\\"  %-40s acc=%.4f (%3d/%3d) BCS=%.4f\\\\\\\",\\\\n                    bid, m[\\\\\\\"accuracy\\\\\\\"], m[\\\\\\\"correct\\\\\\\"], m[\\\\\\\"total\\\\\\\"], m[\\\\\\\"bcs\\\\\\\"])\\\\n\\\\n\\\\ndef main():\\\\n    parser = argparse.ArgumentParser(description=\\\\\\\"FewRel Formal Study\\\\\\\")\\\\n    parser.add_argument(\\\\\\\"--model_path\\\\\\\", default=\\\\\\\"/root/autodl-tmp/.hf_cache/qwen3-32b-fp8/\\\\\\\")\\\\n    parser.add_argument(\\\\\\\"--data_path\\\\\\\", default=str(BASE_DIR / \\\\\\\"data/fewrel_parquet/val.parquet\\\\\\\"),\\\\n                        help=\\\\\\\"Primary data parquet (val split)\\\\\\\")\\\\n    parser.add_argument(\\\\\\\"--data_path_extra\\\\\\\", nargs=\\\\\\\"*\\\\\\\", default=None,\\\\n                        help=\\\\\\\"Additional parquet files (e.g. train split for full 80 relations)\\\\\\\")\\\\n    parser.add_argument(\\\\\\\"--use_all\\\\\\\", action=\\\\\\\"store_true\\\\\\\",\\\\n                        help=\\\\\\\"Load both train+val splits (all 80 relations)\\\\\\\")\\\\n    parser.add_argument(\\\\\\\"--types_file\\\\\\\", default=str(BASE_DIR / \\\\\\\"configs/fewrel_relation_types.json\\\\\\\"))\\\\n    parser.add_argument(\\\\\\\"--embeddings_path\\\\\\\", default=None, help=\\\\\\\"Pre-computed embeddings .pt (Qwen3 or MiniLM)\\\\\\\")\\\\n    parser.add_argument(\\\\\\\"--output_dir\\\\\\\", default=str(BASE_DIR / \\\\\\\"artifacts/fewrel_formal\\\\\\\"))\\\\n    parser.add_argument(\\\\\\\"--mode\\\\\\\", choices=[\\\\\\\"exp1\\\\\\\", \\\\\\\"exp2\\\\\\\", \\\\\\\"dry_run\\\\\\\"], required=True)\\\\n    parser.add_argument(\\\\\\\"--n_samples\\\\\\\", type=int, default=DEFAULT_N_SAMPLES)\\\\n    parser.add_argument(\\\\\\\"--max_model_len\\\\\\\", type=int, default=4096)\\\\n    parser.add_argument(\\\\\\\"--seed\\\\\\\", type=int, default=42)\\\\n    parser.add_argument(\\\\\\\"--gpu_memory_utilization\\\\\\\", type=float, default=0.95)\\\\n    parser.add_argument(\\\\\\\"--dry_run\\\\\\\", action=\\\\\\\"store_true\\\\\\\", help=\\\\\\\"Build batches + print summary, no GPU\\\\\\\")\\\\n    parser.add_argument(\\\\\\\"--stage\\\\\\\", choices=[\\\\\\\"preprocess\\\\\\\", \\\\\\\"extract\\\\\\\", \\\\\\\"all\\\\\\\"], default=\\\\\\\"all\\\\\\\",\\\\n                        help=\\\\\\\"preprocess=CPU only, extract=GPU only, all=subprocess both\\\\\\\")\\\\n    parser.add_argument(\\\\\\\"--preprocess_path\\\\\\\", default=None,\\\\n                        help=\\\\\\\"Path to preprocess JSON (for --stage extract)\\\\\\\")\\\\n    args = parser.parse_args()\\\\n\\\\n    logging.basicConfig(level=logging.INFO, format=\\\\\\\"%(asctime)s %(levelname)s %(message)s\\\\\\\")\\\\n    random.seed(args.seed)\\\\n\\\\n    if args.stage == \\\\\\\"preprocess\\\\\\\":\\\\n        stage_preprocess(args)\\\\n    elif args.stage == \\\\\\\"extract\\\\\\\":\\\\n        stage_extract(args)\\\\n    elif args.stage == \\\\\\\"all\\\\\\\":\\\\n        preprocess_path = stage_preprocess(args)\\\\n\\\\n        if args.dry_run or args.mode == \\\\\\\"dry_run\\\\\\\":\\\\n            logger.info(\\\\\\\"DRY RUN - stopping before GPU extraction.\\\\\\\")\\\\n            return\\\\n\\\\n        logger.info(\\\\\\\"=== Launching extract subprocess (vLLM-first) ===\\\\\\\")\\\\n        cmd = [sys.executable, str(Path(__file__).resolve()),\\\\n               \\\\\\\"--stage\\\\\\\", \\\\\\\"extract\\\\\\\",\\\\n               \\\\\\\"--mode\\\\\\\", args.mode,\\\\n               \\\\\\\"--output_dir\\\\\\\", args.output_dir,\\\\n               \\\\\\\"--preprocess_path\\\\\\\", preprocess_path]\\\\n        subprocess.run(cmd, check=True)\\\\n\\\\n\\\\nif __name__ == \\\\\\\"__main__\\\\\\\":\\\\n    main()\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.41}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"def stage_preprocess(args):\\n    \\\"\\\"\\\"CPU stage: load data, compute BCS, build batch config, save JSON.\\\"\\\"\\\"\\n    sys.path.insert(0, str(BASE_DIR / \\\"src\\\"))\\n    from fewrel_utils import load_fewrel, get_all_relation_types, sample_balanced\\n    from compute_bcs import load_embeddings, compute_similarity_matrix, compute_bcs\\n    from select_type_batches import select_low_bcs, select_high_bcs, select_random_batches\\n\\n    logger.info(\\\"Loading FewRel data...\\\")\\n    data_paths = [args.data_path]\\n    if args.use_all:\\n        data_paths = [str(BASE_DIR / \\\"data/fewrel_parquet/train.parquet\\\"),\\n                      str(BASE_DIR / \\\"data/fewrel_parquet/val.parquet\\\")]\\n    elif args.data_path_extra:\\n        data_paths.extend(args.data_path_extra)\\n\\n    all_samples = []\\n    for dp in data_paths:\\n        all_samples.extend(load_fewrel(data_path=dp))\\n    all_relations = get_all_relation_types(all_samples)\\n    logger.info(\\\"%d samples, %d relation types from %d file(s)\\\",\\n                len(all_samples), len(all_relations), len(data_paths))\\n\\n    n_per_rel = args.n_samples // len(all_relations)\\n    samples = sample_balanced(all_samples, n_per_rel, seed=args.seed)\\n    logger.info(\\\"Sampled %d (%d per relation, %d relations)\\\",\\n                len(samples), n_per_rel, len(all_relations))\\n\\n    with open(args.types_file) as f:\\n        pid2name = json.load(f)\\n    relation_defs = {name: name for name in pid2name.values()}\\n\\n    if args.embeddings_path:\\n        logger.info(\\\"Loading pre-computed embeddings from %s\\\", args.embeddings_path)\\n        embeddings = load_embeddings(args.embeddings_path)\\n        sample_keys = list(embeddings.keys())[:3]\\n        if sample_keys and all(k in pid2name for k in sample_keys):\\n            embeddings = {pid2name[k]: v for k, v in embeddings.items() if k in pid2name}\\n            logger.info(\\\"Remapped %d PID-keyed embeddings to relation names\\\", len(embeddings))\\n    else:\\n        logger.info(\\\"No --embeddings_path; computing MiniLM embeddings (CPU fallback)\\\")\\n        from run_fewrel_pilot import compute_relation_embeddings_st\\n        embeddings = compute_relation_embeddings_st(pid2name)\\n\\n    import torch\\n    sim_matrix, type_names, type_to_idx = compute_similarity_matrix(embeddings)\\n    logger.info(\\\"Similarity matrix: %d types\\\", len(type_names))\\n\\n    active_types = [t for t in type_names if t in set(all_relations)]\\n    active_idx = {t: type_to_idx[t] for t in active_types}\\n    n_active = len(active_types)\\n    logger.info(\\\"Active types (in both embeddings and data): %d\\\", n_active)\\n\\n    mode = args.mode if args.mode != \\\"dry_run\\\" else \\\"exp1\\\"\\n    batch_config = {}\\n    seen_counts = set()\\n\\n    if mode == \\\"exp1\\\":\\n        for count in EXP1_COUNTS:\\n            count = min(count, n_active)\\n            if count in seen_counts:\\n                continue\\n            seen_counts.add(count)\\n            if count == 1:\\n                solo_batches = [{\\\"types\\\": [t], \\\"bcs\\\": 0.0} for t in active_types]\\n                batch_config[\\\"count_1\\\"] = {\\\"random\\\": solo_batches}\\n            else:\\n                rand = select_random_batches(count, EXP1_RANDOM_PER_COUNT, active_types,\\n                                             sim_matrix, active_idx, args.seed + count)\\n                batch_config[f\\\"count_{count}\\\"] = {\\\"random\\\": rand}\\n\\n    elif mode == \\\"exp2\\\":\\n        for count in EXP2_COUNTS:\\n            count = min(count, n_active)\\n            if count in seen_counts:\\n                continue\\n            seen_counts.add(count)\\n            low = select_low_bcs(count, sim_matrix, active_types, active_idx)\\n            high = select_high_bcs(count, sim_matrix, active_types, active_idx)\\n            rand = select_random_batches(count, EXP2_RANDOM_PER_COUNT, active_types,\\n                                         sim_matrix, active_idx, args.seed + count)\\n            batch_config[f\\\"count_{count}\\\"] = {\\n                \\\"low_bcs\\\": {\\\"types\\\": low, \\\"bcs\\\": compute_bcs(low, sim_matrix, type_to_idx)},\\n                \\\"high_bcs\\\": {\\\"types\\\": high, \\\"bcs\\\": compute_bcs(high, sim_matrix, typ\\n\\n... [截断: 输出过长，省略 2453 字符] ...\\n\\n ~%.0f min (@%.1fs/sample)\\\", total_inferences * est_sec / 60, est_sec)\\n\\n    return str(preprocess_path)\\n\\n\\ndef stage_extract(args):\\n    \\\"\\\"\\\"GPU stage: vLLM imported first inside run_re_extraction, read preprocess config.\\\"\\\"\\\"\\n    preprocess_path = args.preprocess_path or str(\\n        Path(args.output_dir) / f\\\"preprocess_{args.mode}.json\\\"\\n    )\\n    with open(preprocess_path) as f:\\n        config = json.load(f)\\n\\n    results = run_re_extraction(\\n        config[\\\"model_path\\\"], config[\\\"samples\\\"], config[\\\"batch_config\\\"],\\n        config[\\\"relation_defs\\\"], config[\\\"max_model_len\\\"],\\n        config.get(\\\"gpu_memory_utilization\\\", 0.95),\\n    )\\n\\n    output_dir = Path(config[\\\"output_dir\\\"])\\n    mode = config[\\\"mode\\\"]\\n\\n    pred_path = output_dir / f\\\"predictions_{mode}.json\\\"\\n    with open(pred_path, \\\"w\\\") as f:\\n        json.dump(results, f, ensure_ascii=False, indent=2)\\n    logger.info(\\\"Saved %d predictions to %s\\\", len(results), pred_path)\\n\\n    eval_results = evaluate_re(results)\\n    eval_path = output_dir / f\\\"eval_{mode}.json\\\"\\n    with open(eval_path, \\\"w\\\") as f:\\n        json.dump(eval_results, f, indent=2)\\n\\n    logger.info(\\\"=\\\" * 60)\\n    logger.info(\\\"RESULTS (%s)\\\", mode)\\n    logger.info(\\\"=\\\" * 60)\\n    for bid, m in sorted(eval_results.items()):\\n        logger.info(\\\"  %-40s acc=%.4f (%3d/%3d) BCS=%.4f\\\",\\n                    bid, m[\\\"accuracy\\\"], m[\\\"correct\\\"], m[\\\"total\\\"], m[\\\"bcs\\\"])\\n\\n\\ndef main():\\n    parser = argparse.ArgumentParser(description=\\\"FewRel Formal Study\\\")\\n    parser.add_argument(\\\"--model_path\\\", default=\\\"/root/autodl-tmp/.hf_cache/qwen3-32b-fp8/\\\")\\n    parser.add_argument(\\\"--data_path\\\", default=str(BASE_DIR / \\\"data/fewrel_parquet/val.parquet\\\"),\\n                        help=\\\"Primary data parquet (val split)\\\")\\n    parser.add_argument(\\\"--data_path_extra\\\", nargs=\\\"*\\\", default=None,\\n                        help=\\\"Additional parquet files (e.g. train split for full 80 relations)\\\")\\n    parser.add_argument(\\\"--use_all\\\", action=\\\"store_true\\\",\\n                        help=\\\"Load both train+val splits (all 80 relations)\\\")\\n    parser.add_argument(\\\"--types_file\\\", default=str(BASE_DIR / \\\"configs/fewrel_relation_types.json\\\"))\\n    parser.add_argument(\\\"--embeddings_path\\\", default=None, help=\\\"Pre-computed embeddings .pt (Qwen3 or MiniLM)\\\")\\n    parser.add_argument(\\\"--output_dir\\\", default=str(BASE_DIR / \\\"artifacts/fewrel_formal\\\"))\\n    parser.add_argument(\\\"--mode\\\", choices=[\\\"exp1\\\", \\\"exp2\\\", \\\"dry_run\\\"], required=True)\\n    parser.add_argument(\\\"--n_samples\\\", type=int, default=DEFAULT_N_SAMPLES)\\n    parser.add_argument(\\\"--max_model_len\\\", type=int, default=4096)\\n    parser.add_argument(\\\"--seed\\\", type=int, default=42)\\n    parser.add_argument(\\\"--gpu_memory_utilization\\\", type=float, default=0.95)\\n    parser.add_argument(\\\"--dry_run\\\", action=\\\"store_true\\\", help=\\\"Build batches + print summary, no GPU\\\")\\n    parser.add_argument(\\\"--stage\\\", choices=[\\\"preprocess\\\", \\\"extract\\\", \\\"all\\\"], default=\\\"all\\\",\\n                        help=\\\"preprocess=CPU only, extract=GPU only, all=subprocess both\\\")\\n    parser.add_argument(\\\"--preprocess_path\\\", default=None,\\n                        help=\\\"Path to preprocess JSON (for --stage extract)\\\")\\n    args = parser.parse_args()\\n\\n    logging.basicConfig(level=logging.INFO, format=\\\"%(asctime)s %(levelname)s %(message)s\\\")\\n    random.seed(args.seed)\\n\\n    if args.stage == \\\"preprocess\\\":\\n        stage_preprocess(args)\\n    elif args.stage == \\\"extract\\\":\\n        stage_extract(args)\\n    elif args.stage == \\\"all\\\":\\n        preprocess_path = stage_preprocess(args)\\n\\n        if args.dry_run or args.mode == \\\"dry_run\\\":\\n            logger.info(\\\"DRY RUN - stopping before GPU extraction.\\\")\\n            return\\n\\n        logger.info(\\\"=== Launching extract subprocess (vLLM-first) ===\\\")\\n        cmd = [sys.executable, str(Path(__file__).resolve()),\\n               \\\"--stage\\\", \\\"extract\\\",\\n               \\\"--mode\\\", args.mode,\\n               \\\"--output_dir\\\", args.output_dir,\\n               \\\"--preprocess_path\\\", preprocess_path]\\n        subprocess.run(cmd, check=True)\\n\\n\\nif __name__ == \\\"__main__\\\":\\n    main()\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.41}}"
    }
  }
}
```

</details>

---


### Assistant

_source line 46_

<details><summary>Logged reasoning block</summary>

```text
Now let me look at the prompt builder functions in `run_extraction.py`.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "a81aceed-1d72-4aba-b0b2-803e0752c9ed",
  "uuid": "2efbebfb-95ad-4e78-9de7-f1c14cc34d72",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016oJAwLF8P2nAyjXAw2Be3j",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3809,
      "cache_read_input_tokens": 35548,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3809
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### Assistant

_source line 47_

Let me look at the prompt builder and check existing artifacts/batch configs.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "a81aceed-1d72-4aba-b0b2-803e0752c9ed",
  "uuid": "0005c020-3987-4174-9144-bcaedd040d14",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016oJAwLF8P2nAyjXAw2Be3j",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3809,
      "cache_read_input_tokens": 35548,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3809
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### Tool call

_source line 48_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_019HEWmouasz2roLaT2hwjw3`</summary>

```json
{
  "server": "cqa1-38874",
  "command": "grep -n \"def build_prompt_v2_re\" /root/schema-dag-extraction/src/run_extraction.py",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "a81aceed-1d72-4aba-b0b2-803e0752c9ed",
  "uuid": "b142d928-a0e3-4ca8-89c0-3fc1973a1b0e",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016oJAwLF8P2nAyjXAw2Be3j",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3809,
      "cache_read_input_tokens": 35548,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3809
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### Tool result

_source line 49 · 2026-05-16T06:41:16.986Z_

<details><summary>↩ Tool result · `toolu_019HEWmouasz2roLaT2hwjw3`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"151:def build_prompt_v2_re(sentence: str, head: str, tail: str,\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.53}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "a81aceed-1d72-4aba-b0b2-803e0752c9ed",
  "uuid": "e5f52244-65ba-4cd1-8a8d-8b5d6b13b413",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"151:def build_prompt_v2_re(sentence: str, head: str, tail: str,\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.53}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"151:def build_prompt_v2_re(sentence: str, head: str, tail: str,\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.53}}"
    }
  }
}
```

</details>

---


### Tool call

_source line 50_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01R4NNYYvaH3oRfSi6PUPnCd`</summary>

```json
{
  "server": "cqa1-38874",
  "command": "grep -n \"def build_json_schema_re\" /root/schema-dag-extraction/src/run_extraction.py",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "a81aceed-1d72-4aba-b0b2-803e0752c9ed",
  "uuid": "86df827f-f985-437d-91f2-a201eaf984e3",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016oJAwLF8P2nAyjXAw2Be3j",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3809,
      "cache_read_input_tokens": 35548,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3809
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### Tool result

_source line 51 · 2026-05-16T06:41:17.737Z_

<details><summary>↩ Tool result · `toolu_01R4NNYYvaH3oRfSi6PUPnCd`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"138:def build_json_schema_re(relation_types: List[str]) -> dict:\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.4}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "a81aceed-1d72-4aba-b0b2-803e0752c9ed",
  "uuid": "011428cc-8e51-4cc9-b02d-34cb91780cc1",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"138:def build_json_schema_re(relation_types: List[str]) -> dict:\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.4}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"138:def build_json_schema_re(relation_types: List[str]) -> dict:\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.4}}"
    }
  }
}
```

</details>

---


### Tool call

_source line 52_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_0162He9Sx5rGyXkDgUMDq4yq`</summary>

```json
{
  "server": "cqa1-38874",
  "command": "ls /root/schema-dag-extraction/artifacts/fewrel_formal_full/",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "a81aceed-1d72-4aba-b0b2-803e0752c9ed",
  "uuid": "bf4c9f6c-5ebe-4406-8a27-49f13075add5",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016oJAwLF8P2nAyjXAw2Be3j",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3809,
      "cache_read_input_tokens": 35548,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3809
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### Tool result

_source line 53 · 2026-05-16T06:41:18.313Z_

<details><summary>↩ Tool result · `toolu_0162He9Sx5rGyXkDgUMDq4yq`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"batch_config_exp1.json\\nbatch_config_exp2.json\\neval_exp1.json\\neval_exp2.json\\npredictions_exp1.json\\npredictions_exp2.json\\npreprocess_exp1.json\\npreprocess_exp2.json\\nrelation_sim_matrix.pt\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.4}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "a81aceed-1d72-4aba-b0b2-803e0752c9ed",
  "uuid": "c7128518-aab1-43c1-a091-97535b588c77",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"batch_config_exp1.json\\\\nbatch_config_exp2.json\\\\neval_exp1.json\\\\neval_exp2.json\\\\npredictions_exp1.json\\\\npredictions_exp2.json\\\\npreprocess_exp1.json\\\\npreprocess_exp2.json\\\\nrelation_sim_matrix.pt\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.4}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"batch_config_exp1.json\\nbatch_config_exp2.json\\neval_exp1.json\\neval_exp2.json\\npredictions_exp1.json\\npredictions_exp2.json\\npreprocess_exp1.json\\npreprocess_exp2.json\\nrelation_sim_matrix.pt\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.4}}"
    }
  }
}
```

</details>

---


### Tool call

_source line 54_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01Gi3MnSyMiLt1w1jnGppvS7`</summary>

```json
{
  "server": "cqa1-38874",
  "command": "tail -n +138 /root/schema-dag-extraction/src/run_extraction.py",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "a81aceed-1d72-4aba-b0b2-803e0752c9ed",
  "uuid": "5341f8fd-0862-4cf2-bcd7-4b6bbf410b1a",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KPKqU8FtcHFmjtvAzRz1XN",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 834,
      "cache_read_input_tokens": 39357,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 834
      },
      "output_tokens": 64,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### Tool result

_source line 55 · 2026-05-16T06:41:22.631Z_

<details><summary>↩ Tool result · `toolu_01Gi3MnSyMiLt1w1jnGppvS7`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"def build_json_schema_re(relation_types: List[str]) -> dict:\\n    return {\\n        \\\"type\\\": \\\"object\\\",\\n        \\\"properties\\\": {\\n            \\\"relation\\\": {\\n                \\\"type\\\": \\\"string\\\",\\n                \\\"enum\\\": sorted(relation_types) + [\\\"none\\\"],\\n            },\\n        },\\n        \\\"required\\\": [\\\"relation\\\"],\\n    }\\n\\n\\ndef build_prompt_v2_re(sentence: str, head: str, tail: str,\\n                       relation_defs: Dict[str, str],\\n                       relation_types: List[str]) -> str:\\n    candidates = \\\", \\\".join(sorted(relation_types))\\n    return (\\n        \\\"Given the following sentence and two entities, \\\"\\n        \\\"classify the relation between them.\\\\n\\\\n\\\"\\n        f'Sentence: \\\"{sentence}\\\"\\\\n'\\n        f'Head entity: \\\"{head}\\\"\\\\n'\\n        f'Tail entity: \\\"{tail}\\\"\\\\n\\\\n'\\n        f\\\"Candidate relations: {candidates}\\\\n\\\\n\\\"\\n        'Output a single JSON object: {\\\"relation\\\": \\\"&lt;relation_type>\\\"}\\\\n'\\n        'If none of the candidate relations apply, output: {\\\"relation\\\": \\\"none\\\"}'\\n    )\\n\\n\\n\\n\\n\\n\\ndef run_extraction(\\n    model_path: str,\\n    samples: List[Dict],\\n    batch_config: Dict,\\n    type_definitions: Dict[str, str],\\n    max_model_len: int = 4096,\\n    prompt_version: str = \\\"v1\\\",\\n    task: str = \\\"ner\\\",\\n    gpu_memory_utilization: float = 0.95,\\n) -> List[Dict]:\\n    \\\"\\\"\\\"Run NER extraction for all (sample, type_batch) combinations.\\n\\n    Args:\\n        model_path: Path to model directory.\\n        samples: List of {\\\"text\\\": str, \\\"entities\\\": [...]}.\\n        batch_config: Output of select_type_batches.py (nested dict by count).\\n        type_definitions: {type_name: definition}.\\n        max_model_len: vLLM max sequence length.\\n        prompt_version: \\\"v1\\\" (with offsets) or \\\"v2\\\" (text+type only).\\n\\n    Returns:\\n        List of result dicts with predictions and metadata.\\n    \\\"\\\"\\\"\\n    from vllm import LLM, SamplingParams\\n    from vllm.sampling_params import StructuredOutputsParams\\n\\n    if task == \\\"re\\\":\\n        schema_fn = build_json_schema_re\\n        prompt_fn = None  # RE uses build_prompt_v2_re with different signature\\n    elif prompt_version == \\\"v2\\\":\\n        schema_fn = build_json_schema_v2\\n        prompt_fn = build_prompt_v2_event if task == \\\"event_detection\\\" else build_prompt_v2\\n    else:\\n        schema_fn = build_json_schema_v1\\n        prompt_fn = build_prompt_v1_event if task == \\\"event_detection\\\" else build_prompt_v1\\n\\n    logger.info(\\\"Loading vLLM model from %s (prompt_version=%s)\\\", model_path, prompt_version)\\n    llm = LLM(\\n        model=model_path,\\n        dtype=\\\"bfloat16\\\",\\n        gpu_memory_utilization=gpu_memory_utilization,\\n        enforce_eager=True,\\n        max_model_len=max_model_len,\\n        trust_remote_code=True,\\n        disable_log_stats=True,\\n    )\\n\\n    tokenizer = llm.get_tokenizer()\\n    _model_id = getattr(tokenizer, 'name_or_path', '') or model_path\\n    _needs_chat_template = any(kw in _model_id.lower() for kw in ['llama', 'mistral', 'gemma', 'phi'])\\n    if _needs_chat_template:\\n        logger.info(\\\"Chat template enabled for model: %s\\\", _model_id)\\n\\n    all_results = []\\n\\n    for count_key, strategies in batch_config.items():\\n        batches_to_run = []\\n\\n        for strat_key in [\\\"low_bcs\\\", \\\"high_bcs\\\"]:\\n            if strat_key not in strategies:\\n                continue\\n            strat = strategies[strat_key]\\n            if isinstance(strat, list):\\n                for bi, b in enumerate(strat):\\n                    batches_to_run.append((f\\\"{strat_key}/{bi}\\\", b[\\\"types\\\"], b[\\\"bcs\\\"]))\\n            else:\\n                batches_to_run.append((strat_key, strat[\\\"types\\\"], strat[\\\"bcs\\\"]))\\n\\n        if \\\"random\\\" in strategies:\\n            for ri, rb in enumerate(strategies[\\\"random\\\"]):\\n                batches_to_run.append((f\\\"random/{ri}\\\", rb[\\\"types\\\"], rb[\\\"bcs\\\"]))\\n\\n        for batch_id, batch_types, batch_bcs in batches_to_run:\\n            full_batch_id = f\\\"{count_key}/{batch_id}\\\"\\n            type_set = set(batch_types)\\n            logger.info(\\\"Running batch %s (%d types, BCS=%.4f) on %d samples\\\",\\n                        full_batch_id, len(batch_types), batch_bcs\\n\\n... [截断: 输出过长，省略 1064 字符] ...\\n\\n    continue\\n            else:\\n                for si, sample in enumerate(samples):\\n                    prompt = prompt_fn(sample[\\\"text\\\"], type_definitions, batch_types)\\n                    prompts.append(prompt)\\n                    sample_indices.append(si)\\n\\n            if _needs_chat_template:\\n                prompts = [\\n                    tokenizer.apply_chat_template(\\n                        [{\\\"role\\\": \\\"user\\\", \\\"content\\\": p}],\\n                        tokenize=False,\\n                        add_generation_prompt=True,\\n                    )\\n                    for p in prompts\\n                ]\\n\\n            t0 = time.time()\\n            outputs = llm.generate(prompts, sampling_params)\\n            elapsed = time.time() - t0\\n\\n            for oi, output in enumerate(outputs):\\n                si = sample_indices[oi]\\n                generated_text = output.outputs[0].text\\n                prompt_tokens = len(output.prompt_token_ids)\\n                gen_tokens = len(output.outputs[0].token_ids)\\n\\n                try:\\n                    predictions = json.loads(generated_text)\\n                except json.JSONDecodeError:\\n                    logger.warning(\\\"Failed to parse JSON for sample %d batch %s: %s\\\",\\n                                   si, full_batch_id, generated_text[:200])\\n                    predictions = []\\n\\n                all_results.append({\\n                    \\\"sample_id\\\": si,\\n                    \\\"batch_id\\\": full_batch_id,\\n                    \\\"count_key\\\": count_key,\\n                    \\\"batch_types\\\": batch_types,\\n                    \\\"batch_bcs\\\": batch_bcs,\\n                    \\\"predictions\\\": predictions,\\n                    \\\"prompt_tokens\\\": prompt_tokens,\\n                    \\\"gen_tokens\\\": gen_tokens,\\n                    \\\"latency_s\\\": elapsed / len(prompts),\\n                    \\\"prompt_version\\\": prompt_version,\\n                })\\n\\n            logger.info(\\\"  Batch %s done: %.1fs total, %d outputs\\\", full_batch_id, elapsed, len(outputs))\\n\\n    return all_results\\n\\n\\ndef main():\\n    parser = argparse.ArgumentParser(description=\\\"Run constrained JSON NER extraction with vLLM\\\")\\n    parser.add_argument(\\\"--model_path\\\", required=True, help=\\\"Path to model directory\\\")\\n    parser.add_argument(\\\"--data_dir\\\", default=\\\"/root/schema-dag-extraction/data\\\", help=\\\"Data directory\\\")\\n    parser.add_argument(\\\"--batch_config\\\", required=True, help=\\\"Type batch JSON from select_type_batches.py\\\")\\n    parser.add_argument(\\\"--output_path\\\", required=True, help=\\\"Output results JSON path\\\")\\n    parser.add_argument(\\\"--max_samples\\\", type=int, default=None, help=\\\"Max test samples\\\")\\n    parser.add_argument(\\\"--types_file\\\", required=True, help=\\\"Type definitions JSON path\\\")\\n    parser.add_argument(\\\"--max_model_len\\\", type=int, default=4096, help=\\\"vLLM max model len\\\")\\n    parser.add_argument(\\\"--prompt_version\\\", choices=[\\\"v1\\\", \\\"v2\\\"], default=\\\"v1\\\",\\n                        help=\\\"Prompt version: v1 (with offsets) or v2 (text+type only)\\\")\\n    args = parser.parse_args()\\n\\n    logging.basicConfig(level=logging.INFO, format=\\\"%(asctime)s %(levelname)s %(message)s\\\")\\n\\n    import sys\\n    sys.path.insert(0, str(Path(__file__).parent))\\n    from few_nerd_utils import load_few_nerd, load_type_definitions\\n\\n    logger.info(\\\"Loading data...\\\")\\n    samples = load_few_nerd(split=\\\"test\\\", max_samples=args.max_samples)\\n    type_definitions = load_type_definitions(args.types_file)\\n\\n    with open(args.batch_config, \\\"r\\\") as f:\\n        batch_config = json.load(f)\\n\\n    results = run_extraction(\\n        model_path=args.model_path,\\n        samples=samples,\\n        batch_config=batch_config,\\n        type_definitions=type_definitions,\\n        max_model_len=args.max_model_len,\\n        prompt_version=args.prompt_version,\\n    )\\n\\n    Path(args.output_path).parent.mkdir(parents=True, exist_ok=True)\\n    with open(args.output_path, \\\"w\\\") as f:\\n        json.dump(results, f, ensure_ascii=False, indent=2)\\n    logger.info(\\\"Saved %d results to %s\\\", len(results), args.output_path)\\n\\n\\nif __name__ == \\\"__main__\\\":\\n    main()\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.67}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "a81aceed-1d72-4aba-b0b2-803e0752c9ed",
  "uuid": "184dd8a4-ba0b-44ba-a22c-e8ea398bbca9",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"def build_json_schema_re(relation_types: List[str]) -> dict:\\\\n    return {\\\\n        \\\\\\\"type\\\\\\\": \\\\\\\"object\\\\\\\",\\\\n        \\\\\\\"properties\\\\\\\": {\\\\n            \\\\\\\"relation\\\\\\\": {\\\\n                \\\\\\\"type\\\\\\\": \\\\\\\"string\\\\\\\",\\\\n                \\\\\\\"enum\\\\\\\": sorted(relation_types) + [\\\\\\\"none\\\\\\\"],\\\\n            },\\\\n        },\\\\n        \\\\\\\"required\\\\\\\": [\\\\\\\"relation\\\\\\\"],\\\\n    }\\\\n\\\\n\\\\ndef build_prompt_v2_re(sentence: str, head: str, tail: str,\\\\n                       relation_defs: Dict[str, str],\\\\n                       relation_types: List[str]) -> str:\\\\n    candidates = \\\\\\\", \\\\\\\".join(sorted(relation_types))\\\\n    return (\\\\n        \\\\\\\"Given the following sentence and two entities, \\\\\\\"\\\\n        \\\\\\\"classify the relation between them.\\\\\\\\n\\\\\\\\n\\\\\\\"\\\\n        f'Sentence: \\\\\\\"{sentence}\\\\\\\"\\\\\\\\n'\\\\n        f'Head entity: \\\\\\\"{head}\\\\\\\"\\\\\\\\n'\\\\n        f'Tail entity: \\\\\\\"{tail}\\\\\\\"\\\\\\\\n\\\\\\\\n'\\\\n        f\\\\\\\"Candidate relations: {candidates}\\\\\\\\n\\\\\\\\n\\\\\\\"\\\\n        'Output a single JSON object: {\\\\\\\"relation\\\\\\\": \\\\\\\"&lt;relation_type>\\\\\\\"}\\\\\\\\n'\\\\n        'If none of the candidate relations apply, output: {\\\\\\\"relation\\\\\\\": \\\\\\\"none\\\\\\\"}'\\\\n    )\\\\n\\\\n\\\\n\\\\n\\\\n\\\\n\\\\ndef run_extraction(\\\\n    model_path: str,\\\\n    samples: List[Dict],\\\\n    batch_config: Dict,\\\\n    type_definitions: Dict[str, str],\\\\n    max_model_len: int = 4096,\\\\n    prompt_version: str = \\\\\\\"v1\\\\\\\",\\\\n    task: str = \\\\\\\"ner\\\\\\\",\\\\n    gpu_memory_utilization: float = 0.95,\\\\n) -> List[Dict]:\\\\n    \\\\\\\"\\\\\\\"\\\\\\\"Run NER extraction for all (sample, type_batch) combinations.\\\\n\\\\n    Args:\\\\n        model_path: Path to model directory.\\\\n        samples: List of {\\\\\\\"text\\\\\\\": str, \\\\\\\"entities\\\\\\\": [...]}.\\\\n        batch_config: Output of select_type_batches.py (nested dict by count).\\\\n        type_definitions: {type_name: definition}.\\\\n        max_model_len: vLLM max sequence length.\\\\n        prompt_version: \\\\\\\"v1\\\\\\\" (with offsets) or \\\\\\\"v2\\\\\\\" (text+type only).\\\\n\\\\n    Returns:\\\\n        List of result dicts with predictions and metadata.\\\\n    \\\\\\\"\\\\\\\"\\\\\\\"\\\\n    from vllm import LLM, SamplingParams\\\\n    from vllm.sampling_params import StructuredOutputsParams\\\\n\\\\n    if task == \\\\\\\"re\\\\\\\":\\\\n        schema_fn = build_json_schema_re\\\\n        prompt_fn = None  # RE uses build_prompt_v2_re with different signature\\\\n    elif prompt_version == \\\\\\\"v2\\\\\\\":\\\\n        schema_fn = build_json_schema_v2\\\\n        prompt_fn = build_prompt_v2_event if task == \\\\\\\"event_detection\\\\\\\" else build_prompt_v2\\\\n    else:\\\\n        schema_fn = build_json_schema_v1\\\\n        prompt_fn = build_prompt_v1_event if task == \\\\\\\"event_detection\\\\\\\" else build_prompt_v1\\\\n\\\\n    logger.info(\\\\\\\"Loading vLLM model from %s (prompt_version=%s)\\\\\\\", model_path, prompt_version)\\\\n    llm = LLM(\\\\n        model=model_path,\\\\n        dtype=\\\\\\\"bfloat16\\\\\\\",\\\\n        gpu_memory_utilization=gpu_memory_utilization,\\\\n        enforce_eager=True,\\\\n        max_model_len=max_model_len,\\\\n        trust_remote_code=True,\\\\n        disable_log_stats=True,\\\\n    )\\\\n\\\\n    tokenizer = llm.get_tokenizer()\\\\n    _model_id = getattr(tokenizer, 'name_or_path', '') or model_path\\\\n    _needs_chat_template = any(kw in _model_id.lower() for kw in ['llama', 'mistral', 'gemma', 'phi'])\\\\n    if _needs_chat_template:\\\\n        logger.info(\\\\\\\"Chat template enabled for model: %s\\\\\\\", _model_id)\\\\n\\\\n    all_results = []\\\\n\\\\n    for count_key, strategies in batch_config.items():\\\\n        batches_to_run = []\\\\n\\\\n        for strat_key in [\\\\\\\"low_bcs\\\\\\\", \\\\\\\"high_bcs\\\\\\\"]:\\\\n            if strat_key not in strategies:\\\\n                continue\\\\n            strat = strategies[strat_key]\\\\n            if isinstance(strat, list):\\\\n                for bi, b in enumerate(strat):\\\\n                    batches_to_run.append((f\\\\\\\"{strat_key}/{bi}\\\\\\\", b[\\\\\\\"types\\\\\\\"], b[\\\\\\\"bcs\\\\\\\"]))\\\\n            else:\\\\n                batches_to_run.append((strat_key, strat[\\\\\\\"types\\\\\\\"], strat[\\\\\\\"bcs\\\\\\\"]))\\\\n\\\\n        if \\\\\\\"random\\\\\\\" in strategies:\\\\n            for ri, rb in enumerate(strategies[\\\\\\\"random\\\\\\\"]):\\\\n                batches_to_run.append((f\\\\\\\"random/{ri}\\\\\\\", rb[\\\\\\\"types\\\\\\\"], rb[\\\\\\\"bcs\\\\\\\"]))\\\\n\\\\n        for batch_id, batch_types, batch_bcs in batches_to_run:\\\\n            full_batch_id = f\\\\\\\"{count_key}/{batch_id}\\\\\\\"\\\\n            type_set = set(batch_types)\\\\n            logger.info(\\\\\\\"Running batch %s (%d types, BCS=%.4f) on %d samples\\\\\\\",\\\\n                        full_batch_id, len(batch_types), batch_bcs\\\\n\\\\n... [截断: 输出过长，省略 1064 字符] ...\\\\n\\\\n    continue\\\\n            else:\\\\n                for si, sample in enumerate(samples):\\\\n                    prompt = prompt_fn(sample[\\\\\\\"text\\\\\\\"], type_definitions, batch_types)\\\\n                    prompts.append(prompt)\\\\n                    sample_indices.append(si)\\\\n\\\\n            if _needs_chat_template:\\\\n                prompts = [\\\\n                    tokenizer.apply_chat_template(\\\\n                        [{\\\\\\\"role\\\\\\\": \\\\\\\"user\\\\\\\", \\\\\\\"content\\\\\\\": p}],\\\\n                        tokenize=False,\\\\n                        add_generation_prompt=True,\\\\n                    )\\\\n                    for p in prompts\\\\n                ]\\\\n\\\\n            t0 = time.time()\\\\n            outputs = llm.generate(prompts, sampling_params)\\\\n            elapsed = time.time() - t0\\\\n\\\\n            for oi, output in enumerate(outputs):\\\\n                si = sample_indices[oi]\\\\n                generated_text = output.outputs[0].text\\\\n                prompt_tokens = len(output.prompt_token_ids)\\\\n                gen_tokens = len(output.outputs[0].token_ids)\\\\n\\\\n                try:\\\\n                    predictions = json.loads(generated_text)\\\\n                except json.JSONDecodeError:\\\\n                    logger.warning(\\\\\\\"Failed to parse JSON for sample %d batch %s: %s\\\\\\\",\\\\n                                   si, full_batch_id, generated_text[:200])\\\\n                    predictions = []\\\\n\\\\n                all_results.append({\\\\n                    \\\\\\\"sample_id\\\\\\\": si,\\\\n                    \\\\\\\"batch_id\\\\\\\": full_batch_id,\\\\n                    \\\\\\\"count_key\\\\\\\": count_key,\\\\n                    \\\\\\\"batch_types\\\\\\\": batch_types,\\\\n                    \\\\\\\"batch_bcs\\\\\\\": batch_bcs,\\\\n                    \\\\\\\"predictions\\\\\\\": predictions,\\\\n                    \\\\\\\"prompt_tokens\\\\\\\": prompt_tokens,\\\\n                    \\\\\\\"gen_tokens\\\\\\\": gen_tokens,\\\\n                    \\\\\\\"latency_s\\\\\\\": elapsed / len(prompts),\\\\n                    \\\\\\\"prompt_version\\\\\\\": prompt_version,\\\\n                })\\\\n\\\\n            logger.info(\\\\\\\"  Batch %s done: %.1fs total, %d outputs\\\\\\\", full_batch_id, elapsed, len(outputs))\\\\n\\\\n    return all_results\\\\n\\\\n\\\\ndef main():\\\\n    parser = argparse.ArgumentParser(description=\\\\\\\"Run constrained JSON NER extraction with vLLM\\\\\\\")\\\\n    parser.add_argument(\\\\\\\"--model_path\\\\\\\", required=True, help=\\\\\\\"Path to model directory\\\\\\\")\\\\n    parser.add_argument(\\\\\\\"--data_dir\\\\\\\", default=\\\\\\\"/root/schema-dag-extraction/data\\\\\\\", help=\\\\\\\"Data directory\\\\\\\")\\\\n    parser.add_argument(\\\\\\\"--batch_config\\\\\\\", required=True, help=\\\\\\\"Type batch JSON from select_type_batches.py\\\\\\\")\\\\n    parser.add_argument(\\\\\\\"--output_path\\\\\\\", required=True, help=\\\\\\\"Output results JSON path\\\\\\\")\\\\n    parser.add_argument(\\\\\\\"--max_samples\\\\\\\", type=int, default=None, help=\\\\\\\"Max test samples\\\\\\\")\\\\n    parser.add_argument(\\\\\\\"--types_file\\\\\\\", required=True, help=\\\\\\\"Type definitions JSON path\\\\\\\")\\\\n    parser.add_argument(\\\\\\\"--max_model_len\\\\\\\", type=int, default=4096, help=\\\\\\\"vLLM max model len\\\\\\\")\\\\n    parser.add_argument(\\\\\\\"--prompt_version\\\\\\\", choices=[\\\\\\\"v1\\\\\\\", \\\\\\\"v2\\\\\\\"], default=\\\\\\\"v1\\\\\\\",\\\\n                        help=\\\\\\\"Prompt version: v1 (with offsets) or v2 (text+type only)\\\\\\\")\\\\n    args = parser.parse_args()\\\\n\\\\n    logging.basicConfig(level=logging.INFO, format=\\\\\\\"%(asctime)s %(levelname)s %(message)s\\\\\\\")\\\\n\\\\n    import sys\\\\n    sys.path.insert(0, str(Path(__file__).parent))\\\\n    from few_nerd_utils import load_few_nerd, load_type_definitions\\\\n\\\\n    logger.info(\\\\\\\"Loading data...\\\\\\\")\\\\n    samples = load_few_nerd(split=\\\\\\\"test\\\\\\\", max_samples=args.max_samples)\\\\n    type_definitions = load_type_definitions(args.types_file)\\\\n\\\\n    with open(args.batch_config, \\\\\\\"r\\\\\\\") as f:\\\\n        batch_config = json.load(f)\\\\n\\\\n    results = run_extraction(\\\\n        model_path=args.model_path,\\\\n        samples=samples,\\\\n        batch_config=batch_config,\\\\n        type_definitions=type_definitions,\\\\n        max_model_len=args.max_model_len,\\\\n        prompt_version=args.prompt_version,\\\\n    )\\\\n\\\\n    Path(args.output_path).parent.mkdir(parents=True, exist_ok=True)\\\\n    with open(args.output_path, \\\\\\\"w\\\\\\\") as f:\\\\n        json.dump(results, f, ensure_ascii=False, indent=2)\\\\n    logger.info(\\\\\\\"Saved %d results to %s\\\\\\\", len(results), args.output_path)\\\\n\\\\n\\\\nif __name__ == \\\\\\\"__main__\\\\\\\":\\\\n    main()\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.67}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"def build_json_schema_re(relation_types: List[str]) -> dict:\\n    return {\\n        \\\"type\\\": \\\"object\\\",\\n        \\\"properties\\\": {\\n            \\\"relation\\\": {\\n                \\\"type\\\": \\\"string\\\",\\n                \\\"enum\\\": sorted(relation_types) + [\\\"none\\\"],\\n            },\\n        },\\n        \\\"required\\\": [\\\"relation\\\"],\\n    }\\n\\n\\ndef build_prompt_v2_re(sentence: str, head: str, tail: str,\\n                       relation_defs: Dict[str, str],\\n                       relation_types: List[str]) -> str:\\n    candidates = \\\", \\\".join(sorted(relation_types))\\n    return (\\n        \\\"Given the following sentence and two entities, \\\"\\n        \\\"classify the relation between them.\\\\n\\\\n\\\"\\n        f'Sentence: \\\"{sentence}\\\"\\\\n'\\n        f'Head entity: \\\"{head}\\\"\\\\n'\\n        f'Tail entity: \\\"{tail}\\\"\\\\n\\\\n'\\n        f\\\"Candidate relations: {candidates}\\\\n\\\\n\\\"\\n        'Output a single JSON object: {\\\"relation\\\": \\\"&lt;relation_type>\\\"}\\\\n'\\n        'If none of the candidate relations apply, output: {\\\"relation\\\": \\\"none\\\"}'\\n    )\\n\\n\\n\\n\\n\\n\\ndef run_extraction(\\n    model_path: str,\\n    samples: List[Dict],\\n    batch_config: Dict,\\n    type_definitions: Dict[str, str],\\n    max_model_len: int = 4096,\\n    prompt_version: str = \\\"v1\\\",\\n    task: str = \\\"ner\\\",\\n    gpu_memory_utilization: float = 0.95,\\n) -> List[Dict]:\\n    \\\"\\\"\\\"Run NER extraction for all (sample, type_batch) combinations.\\n\\n    Args:\\n        model_path: Path to model directory.\\n        samples: List of {\\\"text\\\": str, \\\"entities\\\": [...]}.\\n        batch_config: Output of select_type_batches.py (nested dict by count).\\n        type_definitions: {type_name: definition}.\\n        max_model_len: vLLM max sequence length.\\n        prompt_version: \\\"v1\\\" (with offsets) or \\\"v2\\\" (text+type only).\\n\\n    Returns:\\n        List of result dicts with predictions and metadata.\\n    \\\"\\\"\\\"\\n    from vllm import LLM, SamplingParams\\n    from vllm.sampling_params import StructuredOutputsParams\\n\\n    if task == \\\"re\\\":\\n        schema_fn = build_json_schema_re\\n        prompt_fn = None  # RE uses build_prompt_v2_re with different signature\\n    elif prompt_version == \\\"v2\\\":\\n        schema_fn = build_json_schema_v2\\n        prompt_fn = build_prompt_v2_event if task == \\\"event_detection\\\" else build_prompt_v2\\n    else:\\n        schema_fn = build_json_schema_v1\\n        prompt_fn = build_prompt_v1_event if task == \\\"event_detection\\\" else build_prompt_v1\\n\\n    logger.info(\\\"Loading vLLM model from %s (prompt_version=%s)\\\", model_path, prompt_version)\\n    llm = LLM(\\n        model=model_path,\\n        dtype=\\\"bfloat16\\\",\\n        gpu_memory_utilization=gpu_memory_utilization,\\n        enforce_eager=True,\\n        max_model_len=max_model_len,\\n        trust_remote_code=True,\\n        disable_log_stats=True,\\n    )\\n\\n    tokenizer = llm.get_tokenizer()\\n    _model_id = getattr(tokenizer, 'name_or_path', '') or model_path\\n    _needs_chat_template = any(kw in _model_id.lower() for kw in ['llama', 'mistral', 'gemma', 'phi'])\\n    if _needs_chat_template:\\n        logger.info(\\\"Chat template enabled for model: %s\\\", _model_id)\\n\\n    all_results = []\\n\\n    for count_key, strategies in batch_config.items():\\n        batches_to_run = []\\n\\n        for strat_key in [\\\"low_bcs\\\", \\\"high_bcs\\\"]:\\n            if strat_key not in strategies:\\n                continue\\n            strat = strategies[strat_key]\\n            if isinstance(strat, list):\\n                for bi, b in enumerate(strat):\\n                    batches_to_run.append((f\\\"{strat_key}/{bi}\\\", b[\\\"types\\\"], b[\\\"bcs\\\"]))\\n            else:\\n                batches_to_run.append((strat_key, strat[\\\"types\\\"], strat[\\\"bcs\\\"]))\\n\\n        if \\\"random\\\" in strategies:\\n            for ri, rb in enumerate(strategies[\\\"random\\\"]):\\n                batches_to_run.append((f\\\"random/{ri}\\\", rb[\\\"types\\\"], rb[\\\"bcs\\\"]))\\n\\n        for batch_id, batch_types, batch_bcs in batches_to_run:\\n            full_batch_id = f\\\"{count_key}/{batch_id}\\\"\\n            type_set = set(batch_types)\\n            logger.info(\\\"Running batch %s (%d types, BCS=%.4f) on %d samples\\\",\\n                        full_batch_id, len(batch_types), batch_bcs\\n\\n... [截断: 输出过长，省略 1064 字符] ...\\n\\n    continue\\n            else:\\n                for si, sample in enumerate(samples):\\n                    prompt = prompt_fn(sample[\\\"text\\\"], type_definitions, batch_types)\\n                    prompts.append(prompt)\\n                    sample_indices.append(si)\\n\\n            if _needs_chat_template:\\n                prompts = [\\n                    tokenizer.apply_chat_template(\\n                        [{\\\"role\\\": \\\"user\\\", \\\"content\\\": p}],\\n                        tokenize=False,\\n                        add_generation_prompt=True,\\n                    )\\n                    for p in prompts\\n                ]\\n\\n            t0 = time.time()\\n            outputs = llm.generate(prompts, sampling_params)\\n            elapsed = time.time() - t0\\n\\n            for oi, output in enumerate(outputs):\\n                si = sample_indices[oi]\\n                generated_text = output.outputs[0].text\\n                prompt_tokens = len(output.prompt_token_ids)\\n                gen_tokens = len(output.outputs[0].token_ids)\\n\\n                try:\\n                    predictions = json.loads(generated_text)\\n                except json.JSONDecodeError:\\n                    logger.warning(\\\"Failed to parse JSON for sample %d batch %s: %s\\\",\\n                                   si, full_batch_id, generated_text[:200])\\n                    predictions = []\\n\\n                all_results.append({\\n                    \\\"sample_id\\\": si,\\n                    \\\"batch_id\\\": full_batch_id,\\n                    \\\"count_key\\\": count_key,\\n                    \\\"batch_types\\\": batch_types,\\n                    \\\"batch_bcs\\\": batch_bcs,\\n                    \\\"predictions\\\": predictions,\\n                    \\\"prompt_tokens\\\": prompt_tokens,\\n                    \\\"gen_tokens\\\": gen_tokens,\\n                    \\\"latency_s\\\": elapsed / len(prompts),\\n                    \\\"prompt_version\\\": prompt_version,\\n                })\\n\\n            logger.info(\\\"  Batch %s done: %.1fs total, %d outputs\\\", full_batch_id, elapsed, len(outputs))\\n\\n    return all_results\\n\\n\\ndef main():\\n    parser = argparse.ArgumentParser(description=\\\"Run constrained JSON NER extraction with vLLM\\\")\\n    parser.add_argument(\\\"--model_path\\\", required=True, help=\\\"Path to model directory\\\")\\n    parser.add_argument(\\\"--data_dir\\\", default=\\\"/root/schema-dag-extraction/data\\\", help=\\\"Data directory\\\")\\n    parser.add_argument(\\\"--batch_config\\\", required=True, help=\\\"Type batch JSON from select_type_batches.py\\\")\\n    parser.add_argument(\\\"--output_path\\\", required=True, help=\\\"Output results JSON path\\\")\\n    parser.add_argument(\\\"--max_samples\\\", type=int, default=None, help=\\\"Max test samples\\\")\\n    parser.add_argument(\\\"--types_file\\\", required=True, help=\\\"Type definitions JSON path\\\")\\n    parser.add_argument(\\\"--max_model_len\\\", type=int, default=4096, help=\\\"vLLM max model len\\\")\\n    parser.add_argument(\\\"--prompt_version\\\", choices=[\\\"v1\\\", \\\"v2\\\"], default=\\\"v1\\\",\\n                        help=\\\"Prompt version: v1 (with offsets) or v2 (text+type only)\\\")\\n    args = parser.parse_args()\\n\\n    logging.basicConfig(level=logging.INFO, format=\\\"%(asctime)s %(levelname)s %(message)s\\\")\\n\\n    import sys\\n    sys.path.insert(0, str(Path(__file__).parent))\\n    from few_nerd_utils import load_few_nerd, load_type_definitions\\n\\n    logger.info(\\\"Loading data...\\\")\\n    samples = load_few_nerd(split=\\\"test\\\", max_samples=args.max_samples)\\n    type_definitions = load_type_definitions(args.types_file)\\n\\n    with open(args.batch_config, \\\"r\\\") as f:\\n        batch_config = json.load(f)\\n\\n    results = run_extraction(\\n        model_path=args.model_path,\\n        samples=samples,\\n        batch_config=batch_config,\\n        type_definitions=type_definitions,\\n        max_model_len=args.max_model_len,\\n        prompt_version=args.prompt_version,\\n    )\\n\\n    Path(args.output_path).parent.mkdir(parents=True, exist_ok=True)\\n    with open(args.output_path, \\\"w\\\") as f:\\n        json.dump(results, f, ensure_ascii=False, indent=2)\\n    logger.info(\\\"Saved %d results to %s\\\", len(results), args.output_path)\\n\\n\\nif __name__ == \\\"__main__\\\":\\n    main()\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.67}}"
    }
  }
}
```

</details>

---


### Assistant

_source line 56_

<details><summary>Logged reasoning block</summary>

```text
Now I have the full picture. Let me also look at the existing preprocess JSON to understand what data I can reuse, and check what the fewrel_utils module provides.

Key understanding:
- `build_prompt_v2_re(sentence, head, tail, relation_defs, relation_types)` builds the prompt
- `build_json_schema_re(relation_types)` builds the JSON schema for constrained decoding
- The formal experiment uses vLLM for local inference
- I need to create a GPT-4o-mini version that uses OpenAI API instead

Let me check what batch configs already exist and what preprocess files contain so I can reuse them.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "a81aceed-1d72-4aba-b0b2-803e0752c9ed",
  "uuid": "2b967dba-5228-45de-8a1c-56a40d414ef4",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EpY1CY2LW8WJaKPxCrXWPh",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3181,
      "cache_read_input_tokens": 40191,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3181
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### Assistant

_source line 57_

Now let me check the existing preprocess config (to reuse batch definitions) and the fewrel_utils module.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "a81aceed-1d72-4aba-b0b2-803e0752c9ed",
  "uuid": "180f63fc-997b-4baa-b2c7-a8f6abc1fab3",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EpY1CY2LW8WJaKPxCrXWPh",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3181,
      "cache_read_input_tokens": 40191,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3181
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### Tool call

_source line 58_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_016YqKAQW1jC8WoF7UtZXPV4`</summary>

```json
{
  "server": "cqa1-38874",
  "command": "head -50 /root/schema-dag-extraction/artifacts/fewrel_formal_full/batch_config_exp1.json",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "a81aceed-1d72-4aba-b0b2-803e0752c9ed",
  "uuid": "cb180516-c536-457e-8105-3ae8db7ba302",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EpY1CY2LW8WJaKPxCrXWPh",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3181,
      "cache_read_input_tokens": 40191,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3181
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### Tool result

_source line 59 · 2026-05-16T06:41:30.982Z_

<details><summary>↩ Tool result · `toolu_016YqKAQW1jC8WoF7UtZXPV4`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"count_1\\\": {\\n    \\\"random\\\": [\\n      {\\n        \\\"types\\\": [\\n          \\\"after a work by\\\"\\n        ],\\n        \\\"bcs\\\": 0.0\\n      },\\n      {\\n        \\\"types\\\": [\\n          \\\"applies to jurisdiction\\\"\\n        ],\\n        \\\"bcs\\\": 0.0\\n      },\\n      {\\n        \\\"types\\\": [\\n          \\\"architect\\\"\\n        ],\\n        \\\"bcs\\\": 0.0\\n      },\\n      {\\n        \\\"types\\\": [\\n          \\\"characters\\\"\\n        ],\\n        \\\"bcs\\\": 0.0\\n      },\\n      {\\n        \\\"types\\\": [\\n          \\\"child\\\"\\n        ],\\n        \\\"bcs\\\": 0.0\\n      },\\n      {\\n        \\\"types\\\": [\\n          \\\"competition class\\\"\\n        ],\\n        \\\"bcs\\\": 0.0\\n      },\\n      {\\n        \\\"types\\\": [\\n          \\\"composer\\\"\\n        ],\\n        \\\"bcs\\\": 0.0\\n      },\\n      {\\n        \\\"types\\\": [\\n          \\\"constellation\\\"\\n        ],\\n        \\\"bcs\\\": 0.0\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.39}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "a81aceed-1d72-4aba-b0b2-803e0752c9ed",
  "uuid": "27594686-93b9-49ed-9391-4ef459e910ea",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"{\\\\n  \\\\\\\"count_1\\\\\\\": {\\\\n    \\\\\\\"random\\\\\\\": [\\\\n      {\\\\n        \\\\\\\"types\\\\\\\": [\\\\n          \\\\\\\"after a work by\\\\\\\"\\\\n        ],\\\\n        \\\\\\\"bcs\\\\\\\": 0.0\\\\n      },\\\\n      {\\\\n        \\\\\\\"types\\\\\\\": [\\\\n          \\\\\\\"applies to jurisdiction\\\\\\\"\\\\n        ],\\\\n        \\\\\\\"bcs\\\\\\\": 0.0\\\\n      },\\\\n      {\\\\n        \\\\\\\"types\\\\\\\": [\\\\n          \\\\\\\"architect\\\\\\\"\\\\n        ],\\\\n        \\\\\\\"bcs\\\\\\\": 0.0\\\\n      },\\\\n      {\\\\n        \\\\\\\"types\\\\\\\": [\\\\n          \\\\\\\"characters\\\\\\\"\\\\n        ],\\\\n        \\\\\\\"bcs\\\\\\\": 0.0\\\\n      },\\\\n      {\\\\n        \\\\\\\"types\\\\\\\": [\\\\n          \\\\\\\"child\\\\\\\"\\\\n        ],\\\\n        \\\\\\\"bcs\\\\\\\": 0.0\\\\n      },\\\\n      {\\\\n        \\\\\\\"types\\\\\\\": [\\\\n          \\\\\\\"competition class\\\\\\\"\\\\n        ],\\\\n        \\\\\\\"bcs\\\\\\\": 0.0\\\\n      },\\\\n      {\\\\n        \\\\\\\"types\\\\\\\": [\\\\n          \\\\\\\"composer\\\\\\\"\\\\n        ],\\\\n        \\\\\\\"bcs\\\\\\\": 0.0\\\\n      },\\\\n      {\\\\n        \\\\\\\"types\\\\\\\": [\\\\n          \\\\\\\"constellation\\\\\\\"\\\\n        ],\\\\n        \\\\\\\"bcs\\\\\\\": 0.0\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.39}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"count_1\\\": {\\n    \\\"random\\\": [\\n      {\\n        \\\"types\\\": [\\n          \\\"after a work by\\\"\\n        ],\\n        \\\"bcs\\\": 0.0\\n      },\\n      {\\n        \\\"types\\\": [\\n          \\\"applies to jurisdiction\\\"\\n        ],\\n        \\\"bcs\\\": 0.0\\n      },\\n      {\\n        \\\"types\\\": [\\n          \\\"architect\\\"\\n        ],\\n        \\\"bcs\\\": 0.0\\n      },\\n      {\\n        \\\"types\\\": [\\n          \\\"characters\\\"\\n        ],\\n        \\\"bcs\\\": 0.0\\n      },\\n      {\\n        \\\"types\\\": [\\n          \\\"child\\\"\\n        ],\\n        \\\"bcs\\\": 0.0\\n      },\\n      {\\n        \\\"types\\\": [\\n          \\\"competition class\\\"\\n        ],\\n        \\\"bcs\\\": 0.0\\n      },\\n      {\\n        \\\"types\\\": [\\n          \\\"composer\\\"\\n        ],\\n        \\\"bcs\\\": 0.0\\n      },\\n      {\\n        \\\"types\\\": [\\n          \\\"constellation\\\"\\n        ],\\n        \\\"bcs\\\": 0.0\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.39}}"
    }
  }
}
```

</details>

---


### Tool call

_source line 60_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01DNZm6CFw5ByQuj2Tm4eDjc`</summary>

```json
{
  "server": "cqa1-38874",
  "command": "grep -n \"def \" /root/schema-dag-extraction/src/fewrel_utils.py",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "a81aceed-1d72-4aba-b0b2-803e0752c9ed",
  "uuid": "fad2193a-1060-4b5a-a1ab-24666f9b60bb",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EpY1CY2LW8WJaKPxCrXWPh",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3181,
      "cache_read_input_tokens": 40191,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3181
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### Tool result

_source line 61 · 2026-05-16T06:41:31.939Z_

<details><summary>↩ Tool result · `toolu_01DNZm6CFw5ByQuj2Tm4eDjc`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"20:def load_fewrel(\\n56:def get_all_relation_types(dataset: List[Dict]) -> List[str]:\\n61:def sample_balanced(\\n86:def filter_samples_by_relations(\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.4}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "a81aceed-1d72-4aba-b0b2-803e0752c9ed",
  "uuid": "b9c301ce-aea5-4f84-90c8-aabaf6de0ce5",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"20:def load_fewrel(\\\\n56:def get_all_relation_types(dataset: List[Dict]) -> List[str]:\\\\n61:def sample_balanced(\\\\n86:def filter_samples_by_relations(\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.4}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"20:def load_fewrel(\\n56:def get_all_relation_types(dataset: List[Dict]) -> List[str]:\\n61:def sample_balanced(\\n86:def filter_samples_by_relations(\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.4}}"
    }
  }
}
```

</details>

---


### Tool call

_source line 62_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01CWptwhFxbkcRRgBoX2CMqK`</summary>

```json
{
  "server": "cqa1-38874",
  "command": "cat /root/schema-dag-extraction/configs/fewrel_relation_types.json",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "a81aceed-1d72-4aba-b0b2-803e0752c9ed",
  "uuid": "b8d4b2cb-74db-42d7-b4aa-2ae972fca09f",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EpY1CY2LW8WJaKPxCrXWPh",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3181,
      "cache_read_input_tokens": 40191,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3181
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### Tool result

_source line 63 · 2026-05-16T06:41:32.509Z_

<details><summary>↩ Tool result · `toolu_01CWptwhFxbkcRRgBoX2CMqK`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"P931\\\": \\\"place served by transport hub\\\",\\n  \\\"P4552\\\": \\\"mountain range\\\",\\n  \\\"P140\\\": \\\"religion\\\",\\n  \\\"P1303\\\": \\\"instrument\\\",\\n  \\\"P991\\\": \\\"successful candidate\\\",\\n  \\\"P178\\\": \\\"developer\\\",\\n  \\\"P1344\\\": \\\"participant of\\\",\\n  \\\"P39\\\": \\\"position held\\\",\\n  \\\"P527\\\": \\\"has part\\\",\\n  \\\"P740\\\": \\\"location of formation\\\",\\n  \\\"P706\\\": \\\"located on terrain feature\\\",\\n  \\\"P84\\\": \\\"architect\\\",\\n  \\\"P495\\\": \\\"country of origin\\\",\\n  \\\"P123\\\": \\\"publisher\\\",\\n  \\\"P57\\\": \\\"director\\\",\\n  \\\"P22\\\": \\\"father\\\",\\n  \\\"P750\\\": \\\"distributor\\\",\\n  \\\"P58\\\": \\\"screenwriter\\\",\\n  \\\"P3373\\\": \\\"sibling\\\",\\n  \\\"P127\\\": \\\"owned by\\\",\\n  \\\"P1877\\\": \\\"after a work by\\\",\\n  \\\"P407\\\": \\\"language of work or name\\\",\\n  \\\"P1001\\\": \\\"applies to jurisdiction\\\",\\n  \\\"P800\\\": \\\"notable work\\\",\\n  \\\"P131\\\": \\\"located in the administrative territorial entity\\\",\\n  \\\"P176\\\": \\\"manufacturer\\\",\\n  \\\"P17\\\": \\\"country\\\",\\n  \\\"P175\\\": \\\"performer\\\",\\n  \\\"P31\\\": \\\"instance of\\\",\\n  \\\"P1346\\\": \\\"winner\\\",\\n  \\\"P86\\\": \\\"composer\\\",\\n  \\\"P118\\\": \\\"league\\\",\\n  \\\"P264\\\": \\\"record label\\\",\\n  \\\"P105\\\": \\\"taxon rank\\\",\\n  \\\"P449\\\": \\\"original network\\\",\\n  \\\"P27\\\": \\\"country of citizenship\\\",\\n  \\\"P551\\\": \\\"residence\\\",\\n  \\\"P400\\\": \\\"platform\\\",\\n  \\\"P159\\\": \\\"headquarters location\\\",\\n  \\\"P136\\\": \\\"genre\\\",\\n  \\\"P306\\\": \\\"operating system\\\",\\n  \\\"P276\\\": \\\"location\\\",\\n  \\\"P937\\\": \\\"work location\\\",\\n  \\\"P355\\\": \\\"subsidiary\\\",\\n  \\\"P106\\\": \\\"occupation\\\",\\n  \\\"P1923\\\": \\\"participating team\\\",\\n  \\\"P102\\\": \\\"member of political party\\\",\\n  \\\"P1408\\\": \\\"licensed to broadcast to\\\",\\n  \\\"P674\\\": \\\"characters\\\",\\n  \\\"P241\\\": \\\"military branch\\\",\\n  \\\"P403\\\": \\\"mouth of the watercourse\\\",\\n  \\\"P1411\\\": \\\"nominated for\\\",\\n  \\\"P135\\\": \\\"movement\\\",\\n  \\\"P6\\\": \\\"head of government\\\",\\n  \\\"P3450\\\": \\\"sports season of league or competition\\\",\\n  \\\"P710\\\": \\\"participant\\\",\\n  \\\"P137\\\": \\\"operator\\\",\\n  \\\"P974\\\": \\\"tributary\\\",\\n  \\\"P466\\\": \\\"occupant\\\",\\n  \\\"P101\\\": \\\"field of work\\\",\\n  \\\"P150\\\": \\\"contains administrative territorial entity\\\",\\n  \\\"P460\\\": \\\"said to be the same as\\\",\\n  \\\"P156\\\": \\\"followed by\\\",\\n  \\\"P1435\\\": \\\"heritage designation\\\",\\n  \\\"P155\\\": \\\"follows\\\",\\n  \\\"P177\\\": \\\"crosses\\\",\\n  \\\"P206\\\": \\\"located in or next to body of water\\\",\\n  \\\"P2094\\\": \\\"competition class\\\",\\n  \\\"P25\\\": \\\"mother\\\",\\n  \\\"P26\\\": \\\"spouse\\\",\\n  \\\"P361\\\": \\\"part of\\\",\\n  \\\"P364\\\": \\\"original language of film or TV show\\\",\\n  \\\"P40\\\": \\\"child\\\",\\n  \\\"P410\\\": \\\"military rank\\\",\\n  \\\"P412\\\": \\\"voice type\\\",\\n  \\\"P413\\\": \\\"position played on team\\\",\\n  \\\"P463\\\": \\\"member of\\\",\\n  \\\"P59\\\": \\\"constellation\\\",\\n  \\\"P641\\\": \\\"sport\\\",\\n  \\\"P921\\\": \\\"main subject\\\"\\n}\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.39}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "a81aceed-1d72-4aba-b0b2-803e0752c9ed",
  "uuid": "39274c35-b2f8-4abf-912e-1d6f174a3212",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"{\\\\n  \\\\\\\"P931\\\\\\\": \\\\\\\"place served by transport hub\\\\\\\",\\\\n  \\\\\\\"P4552\\\\\\\": \\\\\\\"mountain range\\\\\\\",\\\\n  \\\\\\\"P140\\\\\\\": \\\\\\\"religion\\\\\\\",\\\\n  \\\\\\\"P1303\\\\\\\": \\\\\\\"instrument\\\\\\\",\\\\n  \\\\\\\"P991\\\\\\\": \\\\\\\"successful candidate\\\\\\\",\\\\n  \\\\\\\"P178\\\\\\\": \\\\\\\"developer\\\\\\\",\\\\n  \\\\\\\"P1344\\\\\\\": \\\\\\\"participant of\\\\\\\",\\\\n  \\\\\\\"P39\\\\\\\": \\\\\\\"position held\\\\\\\",\\\\n  \\\\\\\"P527\\\\\\\": \\\\\\\"has part\\\\\\\",\\\\n  \\\\\\\"P740\\\\\\\": \\\\\\\"location of formation\\\\\\\",\\\\n  \\\\\\\"P706\\\\\\\": \\\\\\\"located on terrain feature\\\\\\\",\\\\n  \\\\\\\"P84\\\\\\\": \\\\\\\"architect\\\\\\\",\\\\n  \\\\\\\"P495\\\\\\\": \\\\\\\"country of origin\\\\\\\",\\\\n  \\\\\\\"P123\\\\\\\": \\\\\\\"publisher\\\\\\\",\\\\n  \\\\\\\"P57\\\\\\\": \\\\\\\"director\\\\\\\",\\\\n  \\\\\\\"P22\\\\\\\": \\\\\\\"father\\\\\\\",\\\\n  \\\\\\\"P750\\\\\\\": \\\\\\\"distributor\\\\\\\",\\\\n  \\\\\\\"P58\\\\\\\": \\\\\\\"screenwriter\\\\\\\",\\\\n  \\\\\\\"P3373\\\\\\\": \\\\\\\"sibling\\\\\\\",\\\\n  \\\\\\\"P127\\\\\\\": \\\\\\\"owned by\\\\\\\",\\\\n  \\\\\\\"P1877\\\\\\\": \\\\\\\"after a work by\\\\\\\",\\\\n  \\\\\\\"P407\\\\\\\": \\\\\\\"language of work or name\\\\\\\",\\\\n  \\\\\\\"P1001\\\\\\\": \\\\\\\"applies to jurisdiction\\\\\\\",\\\\n  \\\\\\\"P800\\\\\\\": \\\\\\\"notable work\\\\\\\",\\\\n  \\\\\\\"P131\\\\\\\": \\\\\\\"located in the administrative territorial entity\\\\\\\",\\\\n  \\\\\\\"P176\\\\\\\": \\\\\\\"manufacturer\\\\\\\",\\\\n  \\\\\\\"P17\\\\\\\": \\\\\\\"country\\\\\\\",\\\\n  \\\\\\\"P175\\\\\\\": \\\\\\\"performer\\\\\\\",\\\\n  \\\\\\\"P31\\\\\\\": \\\\\\\"instance of\\\\\\\",\\\\n  \\\\\\\"P1346\\\\\\\": \\\\\\\"winner\\\\\\\",\\\\n  \\\\\\\"P86\\\\\\\": \\\\\\\"composer\\\\\\\",\\\\n  \\\\\\\"P118\\\\\\\": \\\\\\\"league\\\\\\\",\\\\n  \\\\\\\"P264\\\\\\\": \\\\\\\"record label\\\\\\\",\\\\n  \\\\\\\"P105\\\\\\\": \\\\\\\"taxon rank\\\\\\\",\\\\n  \\\\\\\"P449\\\\\\\": \\\\\\\"original network\\\\\\\",\\\\n  \\\\\\\"P27\\\\\\\": \\\\\\\"country of citizenship\\\\\\\",\\\\n  \\\\\\\"P551\\\\\\\": \\\\\\\"residence\\\\\\\",\\\\n  \\\\\\\"P400\\\\\\\": \\\\\\\"platform\\\\\\\",\\\\n  \\\\\\\"P159\\\\\\\": \\\\\\\"headquarters location\\\\\\\",\\\\n  \\\\\\\"P136\\\\\\\": \\\\\\\"genre\\\\\\\",\\\\n  \\\\\\\"P306\\\\\\\": \\\\\\\"operating system\\\\\\\",\\\\n  \\\\\\\"P276\\\\\\\": \\\\\\\"location\\\\\\\",\\\\n  \\\\\\\"P937\\\\\\\": \\\\\\\"work location\\\\\\\",\\\\n  \\\\\\\"P355\\\\\\\": \\\\\\\"subsidiary\\\\\\\",\\\\n  \\\\\\\"P106\\\\\\\": \\\\\\\"occupation\\\\\\\",\\\\n  \\\\\\\"P1923\\\\\\\": \\\\\\\"participating team\\\\\\\",\\\\n  \\\\\\\"P102\\\\\\\": \\\\\\\"member of political party\\\\\\\",\\\\n  \\\\\\\"P1408\\\\\\\": \\\\\\\"licensed to broadcast to\\\\\\\",\\\\n  \\\\\\\"P674\\\\\\\": \\\\\\\"characters\\\\\\\",\\\\n  \\\\\\\"P241\\\\\\\": \\\\\\\"military branch\\\\\\\",\\\\n  \\\\\\\"P403\\\\\\\": \\\\\\\"mouth of the watercourse\\\\\\\",\\\\n  \\\\\\\"P1411\\\\\\\": \\\\\\\"nominated for\\\\\\\",\\\\n  \\\\\\\"P135\\\\\\\": \\\\\\\"movement\\\\\\\",\\\\n  \\\\\\\"P6\\\\\\\": \\\\\\\"head of government\\\\\\\",\\\\n  \\\\\\\"P3450\\\\\\\": \\\\\\\"sports season of league or competition\\\\\\\",\\\\n  \\\\\\\"P710\\\\\\\": \\\\\\\"participant\\\\\\\",\\\\n  \\\\\\\"P137\\\\\\\": \\\\\\\"operator\\\\\\\",\\\\n  \\\\\\\"P974\\\\\\\": \\\\\\\"tributary\\\\\\\",\\\\n  \\\\\\\"P466\\\\\\\": \\\\\\\"occupant\\\\\\\",\\\\n  \\\\\\\"P101\\\\\\\": \\\\\\\"field of work\\\\\\\",\\\\n  \\\\\\\"P150\\\\\\\": \\\\\\\"contains administrative territorial entity\\\\\\\",\\\\n  \\\\\\\"P460\\\\\\\": \\\\\\\"said to be the same as\\\\\\\",\\\\n  \\\\\\\"P156\\\\\\\": \\\\\\\"followed by\\\\\\\",\\\\n  \\\\\\\"P1435\\\\\\\": \\\\\\\"heritage designation\\\\\\\",\\\\n  \\\\\\\"P155\\\\\\\": \\\\\\\"follows\\\\\\\",\\\\n  \\\\\\\"P177\\\\\\\": \\\\\\\"crosses\\\\\\\",\\\\n  \\\\\\\"P206\\\\\\\": \\\\\\\"located in or next to body of water\\\\\\\",\\\\n  \\\\\\\"P2094\\\\\\\": \\\\\\\"competition class\\\\\\\",\\\\n  \\\\\\\"P25\\\\\\\": \\\\\\\"mother\\\\\\\",\\\\n  \\\\\\\"P26\\\\\\\": \\\\\\\"spouse\\\\\\\",\\\\n  \\\\\\\"P361\\\\\\\": \\\\\\\"part of\\\\\\\",\\\\n  \\\\\\\"P364\\\\\\\": \\\\\\\"original language of film or TV show\\\\\\\",\\\\n  \\\\\\\"P40\\\\\\\": \\\\\\\"child\\\\\\\",\\\\n  \\\\\\\"P410\\\\\\\": \\\\\\\"military rank\\\\\\\",\\\\n  \\\\\\\"P412\\\\\\\": \\\\\\\"voice type\\\\\\\",\\\\n  \\\\\\\"P413\\\\\\\": \\\\\\\"position played on team\\\\\\\",\\\\n  \\\\\\\"P463\\\\\\\": \\\\\\\"member of\\\\\\\",\\\\n  \\\\\\\"P59\\\\\\\": \\\\\\\"constellation\\\\\\\",\\\\n  \\\\\\\"P641\\\\\\\": \\\\\\\"sport\\\\\\\",\\\\n  \\\\\\\"P921\\\\\\\": \\\\\\\"main subject\\\\\\\"\\\\n}\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.39}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"P931\\\": \\\"place served by transport hub\\\",\\n  \\\"P4552\\\": \\\"mountain range\\\",\\n  \\\"P140\\\": \\\"religion\\\",\\n  \\\"P1303\\\": \\\"instrument\\\",\\n  \\\"P991\\\": \\\"successful candidate\\\",\\n  \\\"P178\\\": \\\"developer\\\",\\n  \\\"P1344\\\": \\\"participant of\\\",\\n  \\\"P39\\\": \\\"position held\\\",\\n  \\\"P527\\\": \\\"has part\\\",\\n  \\\"P740\\\": \\\"location of formation\\\",\\n  \\\"P706\\\": \\\"located on terrain feature\\\",\\n  \\\"P84\\\": \\\"architect\\\",\\n  \\\"P495\\\": \\\"country of origin\\\",\\n  \\\"P123\\\": \\\"publisher\\\",\\n  \\\"P57\\\": \\\"director\\\",\\n  \\\"P22\\\": \\\"father\\\",\\n  \\\"P750\\\": \\\"distributor\\\",\\n  \\\"P58\\\": \\\"screenwriter\\\",\\n  \\\"P3373\\\": \\\"sibling\\\",\\n  \\\"P127\\\": \\\"owned by\\\",\\n  \\\"P1877\\\": \\\"after a work by\\\",\\n  \\\"P407\\\": \\\"language of work or name\\\",\\n  \\\"P1001\\\": \\\"applies to jurisdiction\\\",\\n  \\\"P800\\\": \\\"notable work\\\",\\n  \\\"P131\\\": \\\"located in the administrative territorial entity\\\",\\n  \\\"P176\\\": \\\"manufacturer\\\",\\n  \\\"P17\\\": \\\"country\\\",\\n  \\\"P175\\\": \\\"performer\\\",\\n  \\\"P31\\\": \\\"instance of\\\",\\n  \\\"P1346\\\": \\\"winner\\\",\\n  \\\"P86\\\": \\\"composer\\\",\\n  \\\"P118\\\": \\\"league\\\",\\n  \\\"P264\\\": \\\"record label\\\",\\n  \\\"P105\\\": \\\"taxon rank\\\",\\n  \\\"P449\\\": \\\"original network\\\",\\n  \\\"P27\\\": \\\"country of citizenship\\\",\\n  \\\"P551\\\": \\\"residence\\\",\\n  \\\"P400\\\": \\\"platform\\\",\\n  \\\"P159\\\": \\\"headquarters location\\\",\\n  \\\"P136\\\": \\\"genre\\\",\\n  \\\"P306\\\": \\\"operating system\\\",\\n  \\\"P276\\\": \\\"location\\\",\\n  \\\"P937\\\": \\\"work location\\\",\\n  \\\"P355\\\": \\\"subsidiary\\\",\\n  \\\"P106\\\": \\\"occupation\\\",\\n  \\\"P1923\\\": \\\"participating team\\\",\\n  \\\"P102\\\": \\\"member of political party\\\",\\n  \\\"P1408\\\": \\\"licensed to broadcast to\\\",\\n  \\\"P674\\\": \\\"characters\\\",\\n  \\\"P241\\\": \\\"military branch\\\",\\n  \\\"P403\\\": \\\"mouth of the watercourse\\\",\\n  \\\"P1411\\\": \\\"nominated for\\\",\\n  \\\"P135\\\": \\\"movement\\\",\\n  \\\"P6\\\": \\\"head of government\\\",\\n  \\\"P3450\\\": \\\"sports season of league or competition\\\",\\n  \\\"P710\\\": \\\"participant\\\",\\n  \\\"P137\\\": \\\"operator\\\",\\n  \\\"P974\\\": \\\"tributary\\\",\\n  \\\"P466\\\": \\\"occupant\\\",\\n  \\\"P101\\\": \\\"field of work\\\",\\n  \\\"P150\\\": \\\"contains administrative territorial entity\\\",\\n  \\\"P460\\\": \\\"said to be the same as\\\",\\n  \\\"P156\\\": \\\"followed by\\\",\\n  \\\"P1435\\\": \\\"heritage designation\\\",\\n  \\\"P155\\\": \\\"follows\\\",\\n  \\\"P177\\\": \\\"crosses\\\",\\n  \\\"P206\\\": \\\"located in or next to body of water\\\",\\n  \\\"P2094\\\": \\\"competition class\\\",\\n  \\\"P25\\\": \\\"mother\\\",\\n  \\\"P26\\\": \\\"spouse\\\",\\n  \\\"P361\\\": \\\"part of\\\",\\n  \\\"P364\\\": \\\"original language of film or TV show\\\",\\n  \\\"P40\\\": \\\"child\\\",\\n  \\\"P410\\\": \\\"military rank\\\",\\n  \\\"P412\\\": \\\"voice type\\\",\\n  \\\"P413\\\": \\\"position played on team\\\",\\n  \\\"P463\\\": \\\"member of\\\",\\n  \\\"P59\\\": \\\"constellation\\\",\\n  \\\"P641\\\": \\\"sport\\\",\\n  \\\"P921\\\": \\\"main subject\\\"\\n}\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.39}}"
    }
  }
}
```

</details>

---


### Assistant

_source line 64_

<details><summary>Logged reasoning block</summary>

```text
I have all the information I need. Let me check the `fewrel_utils.py` to understand `load_fewrel` function signatures, and check if there's a TUM proxy base_url in any config or env.

Now let me write the GPT-4o-mini experiment script. The plan:
1. Reuse the same batch_config from fewrel_formal_full (exp1 and exp2)
2. Reuse `load_fewrel`, `sample_balanced`, `build_prompt_v2_re`, `evaluate_re`


3. Replace vLLM with OpenAI API calls using the `openai` Python package
4. Use structured output via OpenAI's JSON mode for response formatting

I need to find the TUM proxy base_url—the "tum_" prefix suggests it's for a Technical University of Munich proxy, likely in a .env file or project config somewhere.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "a81aceed-1d72-4aba-b0b2-803e0752c9ed",
  "uuid": "9390d7fc-099b-434e-9c02-c54294d09cf8",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016V5UM33rFi2fY46BhbJFPY",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2866,
      "cache_read_input_tokens": 43372,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2866
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### Tool call

_source line 65_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_012AbQ1A4vbAmLsiYyWQJGMZ`</summary>

```json
{
  "server": "cqa1-38874",
  "command": "find /root/schema-dag-extraction -name \".env\" -type f",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "a81aceed-1d72-4aba-b0b2-803e0752c9ed",
  "uuid": "de220fda-fb23-46d9-b662-16f0435fbbdc",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016V5UM33rFi2fY46BhbJFPY",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2866,
      "cache_read_input_tokens": 43372,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2866
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### Tool result

_source line 66 · 2026-05-16T06:41:43.765Z_

<details><summary>↩ Tool result · `toolu_012AbQ1A4vbAmLsiYyWQJGMZ`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.4}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "a81aceed-1d72-4aba-b0b2-803e0752c9ed",
  "uuid": "74991a0a-5af6-4532-9a78-e64ad40a7923",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.4}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.4}}"
    }
  }
}
```

</details>

---


### Tool call

_source line 67_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01MowMH6Btaa1N9Qyoi2ep5J`</summary>

```json
{
  "server": "cqa1-38874",
  "command": "find /root/schema-dag-extraction -name \"*.yaml\" -type f",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "a81aceed-1d72-4aba-b0b2-803e0752c9ed",
  "uuid": "ef578646-70a0-42c0-a22f-9357ea59febc",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016V5UM33rFi2fY46BhbJFPY",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2866,
      "cache_read_input_tokens": 43372,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2866
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### Tool result

_source line 68 · 2026-05-16T06:41:44.578Z_

<details><summary>↩ Tool result · `toolu_01MowMH6Btaa1N9Qyoi2ep5J`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.41}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "a81aceed-1d72-4aba-b0b2-803e0752c9ed",
  "uuid": "e9e354ae-4952-45ee-880b-d2a13153ce4b",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.41}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.41}}"
    }
  }
}
```

</details>

---


### Tool call

_source line 69_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01WJ5qJs67GiEYFb9jZd4e2A`</summary>

```json
{
  "server": "cqa1-38874",
  "command": "cat /root/schema-dag-extraction/src/fewrel_utils.py",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "a81aceed-1d72-4aba-b0b2-803e0752c9ed",
  "uuid": "00f9b4d2-374c-4cb3-9724-b5c779b932c1",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016V5UM33rFi2fY46BhbJFPY",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2866,
      "cache_read_input_tokens": 43372,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2866
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### Tool result

_source line 70 · 2026-05-16T06:41:45.200Z_

<details><summary>↩ Tool result · `toolu_01WJ5qJs67GiEYFb9jZd4e2A`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"\\\"\\\"\\\"FewRel relation extraction data loading utilities.\\n\\nInput: FewRel parquet files (pre-processed by preprocess_fewrel.py)\\n       Each row: text, head_entity, head_pos, tail_entity, tail_pos, relation_type, relation_pid\\nOutput: List of {\\\"text\\\": str, \\\"head_entity\\\": str, \\\"tail_entity\\\": str, \\\"relation_type\\\": str, ...}\\nDependencies: pandas\\n\\\"\\\"\\\"\\nimport json\\nimport logging\\nimport random\\nfrom typing import Dict, List, Optional, Set\\n\\nimport pandas as pd\\n\\nlogger = logging.getLogger(__name__)\\n\\nDEFAULT_DATA_PATH = \\\"/root/schema-dag-extraction/data/fewrel_parquet/val.parquet\\\"\\n\\n\\ndef load_fewrel(\\n    data_path: str = DEFAULT_DATA_PATH,\\n    max_samples: Optional[int] = None,\\n    relation_filter: Optional[List[str]] = None,\\n) -> List[Dict]:\\n    \\\"\\\"\\\"Load FewRel RE data from parquet.\\n\\n    Args:\\n        data_path: Path to parquet file.\\n        max_samples: If set, only return first N samples.\\n        relation_filter: If set, only keep samples with these relation types.\\n\\n    Returns:\\n        List of dicts with: text, head_entity, tail_entity, relation_type, relation_pid\\n    \\\"\\\"\\\"\\n    df = pd.read_parquet(data_path)\\n    if relation_filter:\\n        df = df[df[\\\"relation_type\\\"].isin(relation_filter)]\\n    if max_samples is not None:\\n        df = df.head(max_samples)\\n\\n    samples = []\\n    for _, row in df.iterrows():\\n        samples.append({\\n            \\\"text\\\": row[\\\"text\\\"],\\n            \\\"head_entity\\\": row[\\\"head_entity\\\"],\\n            \\\"tail_entity\\\": row[\\\"tail_entity\\\"],\\n            \\\"relation_type\\\": row[\\\"relation_type\\\"],\\n            \\\"relation_pid\\\": row[\\\"relation_pid\\\"],\\n        })\\n\\n    logger.info(\\\"Loaded %d FewRel samples from %s (%d unique relations)\\\",\\n                len(samples), data_path, df[\\\"relation_type\\\"].nunique())\\n    return samples\\n\\n\\ndef get_all_relation_types(dataset: List[Dict]) -> List[str]:\\n    \\\"\\\"\\\"Extract all unique relation type names from dataset.\\\"\\\"\\\"\\n    return sorted(set(s[\\\"relation_type\\\"] for s in dataset))\\n\\n\\ndef sample_balanced(\\n    dataset: List[Dict],\\n    n_per_relation: int,\\n    relations: Optional[List[str]] = None,\\n    seed: int = 42,\\n) -> List[Dict]:\\n    \\\"\\\"\\\"Sample n_per_relation samples per relation type (balanced).\\\"\\\"\\\"\\n    rng = random.Random(seed)\\n\\n    by_rel: Dict[str, List[Dict]] = {}\\n    for s in dataset:\\n        by_rel.setdefault(s[\\\"relation_type\\\"], []).append(s)\\n\\n    if relations is None:\\n        relations = sorted(by_rel.keys())\\n\\n    sampled = []\\n    for rel in relations:\\n        pool = by_rel.get(rel, [])\\n        k = min(n_per_relation, len(pool))\\n        sampled.extend(rng.sample(pool, k))\\n\\n    return sampled\\n\\n\\ndef filter_samples_by_relations(\\n    samples: List[Dict], relation_set: Set[str]\\n) -> List[Dict]:\\n    \\\"\\\"\\\"Keep only samples whose relation_type is in relation_set.\\\"\\\"\\\"\\n    return [s for s in samples if s[\\\"relation_type\\\"] in relation_set]\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.39}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "a81aceed-1d72-4aba-b0b2-803e0752c9ed",
  "uuid": "eb56092d-72fb-4ded-898a-e8ca140d09fa",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"\\\\\\\"\\\\\\\"\\\\\\\"FewRel relation extraction data loading utilities.\\\\n\\\\nInput: FewRel parquet files (pre-processed by preprocess_fewrel.py)\\\\n       Each row: text, head_entity, head_pos, tail_entity, tail_pos, relation_type, relation_pid\\\\nOutput: List of {\\\\\\\"text\\\\\\\": str, \\\\\\\"head_entity\\\\\\\": str, \\\\\\\"tail_entity\\\\\\\": str, \\\\\\\"relation_type\\\\\\\": str, ...}\\\\nDependencies: pandas\\\\n\\\\\\\"\\\\\\\"\\\\\\\"\\\\nimport json\\\\nimport logging\\\\nimport random\\\\nfrom typing import Dict, List, Optional, Set\\\\n\\\\nimport pandas as pd\\\\n\\\\nlogger = logging.getLogger(__name__)\\\\n\\\\nDEFAULT_DATA_PATH = \\\\\\\"/root/schema-dag-extraction/data/fewrel_parquet/val.parquet\\\\\\\"\\\\n\\\\n\\\\ndef load_fewrel(\\\\n    data_path: str = DEFAULT_DATA_PATH,\\\\n    max_samples: Optional[int] = None,\\\\n    relation_filter: Optional[List[str]] = None,\\\\n) -> List[Dict]:\\\\n    \\\\\\\"\\\\\\\"\\\\\\\"Load FewRel RE data from parquet.\\\\n\\\\n    Args:\\\\n        data_path: Path to parquet file.\\\\n        max_samples: If set, only return first N samples.\\\\n        relation_filter: If set, only keep samples with these relation types.\\\\n\\\\n    Returns:\\\\n        List of dicts with: text, head_entity, tail_entity, relation_type, relation_pid\\\\n    \\\\\\\"\\\\\\\"\\\\\\\"\\\\n    df = pd.read_parquet(data_path)\\\\n    if relation_filter:\\\\n        df = df[df[\\\\\\\"relation_type\\\\\\\"].isin(relation_filter)]\\\\n    if max_samples is not None:\\\\n        df = df.head(max_samples)\\\\n\\\\n    samples = []\\\\n    for _, row in df.iterrows():\\\\n        samples.append({\\\\n            \\\\\\\"text\\\\\\\": row[\\\\\\\"text\\\\\\\"],\\\\n            \\\\\\\"head_entity\\\\\\\": row[\\\\\\\"head_entity\\\\\\\"],\\\\n            \\\\\\\"tail_entity\\\\\\\": row[\\\\\\\"tail_entity\\\\\\\"],\\\\n            \\\\\\\"relation_type\\\\\\\": row[\\\\\\\"relation_type\\\\\\\"],\\\\n            \\\\\\\"relation_pid\\\\\\\": row[\\\\\\\"relation_pid\\\\\\\"],\\\\n        })\\\\n\\\\n    logger.info(\\\\\\\"Loaded %d FewRel samples from %s (%d unique relations)\\\\\\\",\\\\n                len(samples), data_path, df[\\\\\\\"relation_type\\\\\\\"].nunique())\\\\n    return samples\\\\n\\\\n\\\\ndef get_all_relation_types(dataset: List[Dict]) -> List[str]:\\\\n    \\\\\\\"\\\\\\\"\\\\\\\"Extract all unique relation type names from dataset.\\\\\\\"\\\\\\\"\\\\\\\"\\\\n    return sorted(set(s[\\\\\\\"relation_type\\\\\\\"] for s in dataset))\\\\n\\\\n\\\\ndef sample_balanced(\\\\n    dataset: List[Dict],\\\\n    n_per_relation: int,\\\\n    relations: Optional[List[str]] = None,\\\\n    seed: int = 42,\\\\n) -> List[Dict]:\\\\n    \\\\\\\"\\\\\\\"\\\\\\\"Sample n_per_relation samples per relation type (balanced).\\\\\\\"\\\\\\\"\\\\\\\"\\\\n    rng = random.Random(seed)\\\\n\\\\n    by_rel: Dict[str, List[Dict]] = {}\\\\n    for s in dataset:\\\\n        by_rel.setdefault(s[\\\\\\\"relation_type\\\\\\\"], []).append(s)\\\\n\\\\n    if relations is None:\\\\n        relations = sorted(by_rel.keys())\\\\n\\\\n    sampled = []\\\\n    for rel in relations:\\\\n        pool = by_rel.get(rel, [])\\\\n        k = min(n_per_relation, len(pool))\\\\n        sampled.extend(rng.sample(pool, k))\\\\n\\\\n    return sampled\\\\n\\\\n\\\\ndef filter_samples_by_relations(\\\\n    samples: List[Dict], relation_set: Set[str]\\\\n) -> List[Dict]:\\\\n    \\\\\\\"\\\\\\\"\\\\\\\"Keep only samples whose relation_type is in relation_set.\\\\\\\"\\\\\\\"\\\\\\\"\\\\n    return [s for s in samples if s[\\\\\\\"relation_type\\\\\\\"] in relation_set]\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.39}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"\\\"\\\"\\\"FewRel relation extraction data loading utilities.\\n\\nInput: FewRel parquet files (pre-processed by preprocess_fewrel.py)\\n       Each row: text, head_entity, head_pos, tail_entity, tail_pos, relation_type, relation_pid\\nOutput: List of {\\\"text\\\": str, \\\"head_entity\\\": str, \\\"tail_entity\\\": str, \\\"relation_type\\\": str, ...}\\nDependencies: pandas\\n\\\"\\\"\\\"\\nimport json\\nimport logging\\nimport random\\nfrom typing import Dict, List, Optional, Set\\n\\nimport pandas as pd\\n\\nlogger = logging.getLogger(__name__)\\n\\nDEFAULT_DATA_PATH = \\\"/root/schema-dag-extraction/data/fewrel_parquet/val.parquet\\\"\\n\\n\\ndef load_fewrel(\\n    data_path: str = DEFAULT_DATA_PATH,\\n    max_samples: Optional[int] = None,\\n    relation_filter: Optional[List[str]] = None,\\n) -> List[Dict]:\\n    \\\"\\\"\\\"Load FewRel RE data from parquet.\\n\\n    Args:\\n        data_path: Path to parquet file.\\n        max_samples: If set, only return first N samples.\\n        relation_filter: If set, only keep samples with these relation types.\\n\\n    Returns:\\n        List of dicts with: text, head_entity, tail_entity, relation_type, relation_pid\\n    \\\"\\\"\\\"\\n    df = pd.read_parquet(data_path)\\n    if relation_filter:\\n        df = df[df[\\\"relation_type\\\"].isin(relation_filter)]\\n    if max_samples is not None:\\n        df = df.head(max_samples)\\n\\n    samples = []\\n    for _, row in df.iterrows():\\n        samples.append({\\n            \\\"text\\\": row[\\\"text\\\"],\\n            \\\"head_entity\\\": row[\\\"head_entity\\\"],\\n            \\\"tail_entity\\\": row[\\\"tail_entity\\\"],\\n            \\\"relation_type\\\": row[\\\"relation_type\\\"],\\n            \\\"relation_pid\\\": row[\\\"relation_pid\\\"],\\n        })\\n\\n    logger.info(\\\"Loaded %d FewRel samples from %s (%d unique relations)\\\",\\n                len(samples), data_path, df[\\\"relation_type\\\"].nunique())\\n    return samples\\n\\n\\ndef get_all_relation_types(dataset: List[Dict]) -> List[str]:\\n    \\\"\\\"\\\"Extract all unique relation type names from dataset.\\\"\\\"\\\"\\n    return sorted(set(s[\\\"relation_type\\\"] for s in dataset))\\n\\n\\ndef sample_balanced(\\n    dataset: List[Dict],\\n    n_per_relation: int,\\n    relations: Optional[List[str]] = None,\\n    seed: int = 42,\\n) -> List[Dict]:\\n    \\\"\\\"\\\"Sample n_per_relation samples per relation type (balanced).\\\"\\\"\\\"\\n    rng = random.Random(seed)\\n\\n    by_rel: Dict[str, List[Dict]] = {}\\n    for s in dataset:\\n        by_rel.setdefault(s[\\\"relation_type\\\"], []).append(s)\\n\\n    if relations is None:\\n        relations = sorted(by_rel.keys())\\n\\n    sampled = []\\n    for rel in relations:\\n        pool = by_rel.get(rel, [])\\n        k = min(n_per_relation, len(pool))\\n        sampled.extend(rng.sample(pool, k))\\n\\n    return sampled\\n\\n\\ndef filter_samples_by_relations(\\n    samples: List[Dict], relation_set: Set[str]\\n) -> List[Dict]:\\n    \\\"\\\"\\\"Keep only samples whose relation_type is in relation_set.\\\"\\\"\\\"\\n    return [s for s in samples if s[\\\"relation_type\\\"] in relation_set]\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.39}}"
    }
  }
}
```

</details>

---


### Assistant

_source line 71_

<details><summary>Logged reasoning block</summary>

```text
Now I have all the pieces. Let me look for TUM proxy configuration. The key starts with "tum_" which is a common format for TUM AI proxies. Let me search for the base_url in other locations or check if there's a known TUM OpenAI proxy.

Actually, based on the key format "tum_XXB3sZ..." - this appears to be for the TUM AI/OpenAI proxy service. The typical base_url for TUM's proxy to OpenAI is `https://2mz.me/v1` or `https://go.2mz.me/v1`. 

Rather than guessing, I should search the server more systematically and check what Python environment and OpenAI packages are already available.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "a81aceed-1d72-4aba-b0b2-803e0752c9ed",
  "uuid": "b4b9765f-946b-4db3-becc-b8c0b49bdac1",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018LTkaMYpGKGci9aRs3pWZh",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2127,
      "cache_read_input_tokens": 46238,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2127
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### Tool call

_source line 72_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01VuhULvf63WwxreHiVRzXbg`</summary>

```json
{
  "server": "cqa1-38874",
  "command": "grep -rn \"base_url\" /root/schema-dag-extraction/",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "a81aceed-1d72-4aba-b0b2-803e0752c9ed",
  "uuid": "2cfd2965-a41e-4ded-89cb-a7ec4d2994fc",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018LTkaMYpGKGci9aRs3pWZh",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2127,
      "cache_read_input_tokens": 46238,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2127
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### Tool call

_source line 73_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01AtvFX2R4LwYQqQmSLWsAP5`</summary>

```json
{
  "server": "cqa1-38874",
  "command": "grep -rn \"tum\" /root/schema-dag-extraction/",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "a81aceed-1d72-4aba-b0b2-803e0752c9ed",
  "uuid": "d3d0399a-1242-418d-8d49-ec45b462c4b1",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018LTkaMYpGKGci9aRs3pWZh",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2127,
      "cache_read_input_tokens": 46238,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2127
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### Tool call

_source line 74_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01EutA84PxH9r3d9RbAa6qaR`</summary>

```json
{
  "server": "cqa1-38874",
  "command": "find /root -name \".env\" -type f",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "a81aceed-1d72-4aba-b0b2-803e0752c9ed",
  "uuid": "392903be-79ed-401b-8bdf-f4084bbf36d6",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018LTkaMYpGKGci9aRs3pWZh",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2127,
      "cache_read_input_tokens": 46238,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2127
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### Tool result

_source line 75 · 2026-05-16T06:41:56.053Z_

<details><summary>↩ Tool result · `toolu_01VuhULvf63WwxreHiVRzXbg`</summary>

```text
{"result":"{\"success\": false, \"data\": {\"stdout\": \"\", \"stderr\": \"\", \"return_code\": 1}, \"error\": \"exit code 1\", \"metadata\": {\"elapsed_seconds\": 3.86}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "a81aceed-1d72-4aba-b0b2-803e0752c9ed",
  "uuid": "f11338fc-4a2b-40b3-a981-d97507877fd0",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": false, \\\"data\\\": {\\\"stdout\\\": \\\"\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 1}, \\\"error\\\": \\\"exit code 1\\\", \\\"metadata\\\": {\\\"elapsed_seconds\\\": 3.86}}\"}",
    "structuredContent": {
      "result": "{\"success\": false, \"data\": {\"stdout\": \"\", \"stderr\": \"\", \"return_code\": 1}, \"error\": \"exit code 1\", \"metadata\": {\"elapsed_seconds\": 3.86}}"
    }
  }
}
```

</details>

---


### Large event (continued)

````text
### Tool result

_source line 76 · 2026-05-16T06:42:45.646Z_

&lt;details>&lt;summary>↩ Tool result · `toolu_01AtvFX2R4LwYQqQmSLWsAP5`&lt;/summary>

```text
Error: result (9,076,835 characters) exceeds maximum allowed tokens. Output has been saved to /home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-18-projects-schema-dag-extraction/a81aceed-1d72-4aba-b0b2-803e0752c9ed/tool-results/mcp-agent-ml-research-ssh_read_only-1778913765599.txt.
Format: JSON with schema: {result: string}
Use offset and limit parameters to read specific portions of the file, search within it for specific content, and jq to make structured queries.
REQUIREMENTS FOR SUMMARIZATION/ANALYSIS/REVIEW:
- You MUST read the content from the file at /home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-18-projects-schema-dag-extraction/a81aceed-1d72-4aba-b0b2-803e0752c9ed/tool-results/mcp-agent-ml-research-ssh_read_only-1778913765599.txt in sequential chunks until 100% of the content has been read.
- If you receive truncation warnings when reading the file, reduce the chunk size until you have read 100% of the content without truncation.
- Before producing ANY summary or analysis, you MUST explicitly describe what portion of the content you have read. ***If you did not read the entire content, you MUST explicitly state this.***

```

&lt;/details>

&lt;details>&lt;summary>Recorded metadata&lt;/summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "a81aceed-1d72-4aba-b0b2-803e0752c9ed",
  "uuid": "826e974b-f71d-42b7-ae3c-e6cc5a2fcfdf",
  "tool_use_result": {
    "content": "Error: result (9,076,835 characters) exceeds maximum allowed tokens. Output has been saved to /home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-18-projects-schema-dag-extraction/a81aceed-1d72-4aba-b0b2-803e0752c9ed/tool-results/mcp-agent-ml-research-ssh_read_only-1778913765599.txt.\nFormat: JSON with schema: {result: string}\nUse offset and limit parameters to read specific portions of the file, search within it for specific content, and jq to make structured queries.\nREQUIREMENTS FOR SUMMARIZATION/ANALYSIS/REVIEW:\n- You MUST read the content from the file at /home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-18-projects-schema-dag-extraction/a81aceed-1d72-4aba-b0b2-803e0752c9ed/tool-results/mcp-agent-ml-research-ssh_read_only-1778913765599.txt in sequential chunks until 100% of the content has been read.\n- If you receive truncation warnings when reading the file, reduce the chunk size until you have read 100% of the content without truncation.\n- Before producing ANY summary or analysis, you MUST explicitly describe what portion of the content you have read. ***If you did not read the entire content, you MUST explicitly state this.***\n",
    "structuredContent": {

````

---

### Large event (continued)

```text
      "result": "{\"success\": false, \"data\": {}, \"error\": \"Command did not complete within 30 seconds!\\n\\nCommand: 'grep -rn \\\"tum\\\" /root/schema-dag-extraction/'\\n\\nStdout:\\n\\n/root/schema-dag-extraction/data/maven/test.jsonl:440:{\\\"title\\\": \\\"Hue–Da Nang Campaign\\\", \\\"id\\\": \\\"f1e2992b53865bdb1077529beac466bf\\\", \\\"content\\\": [{\\\"sentence\\\": \\\"The Hue–Da Nang Campaign was a series of military actions conducted by the People's Army of Vietnam (PAVN) against the Army of the Republic of Vietnam (ARVN) during the Vietnam War, also known in Vietnam as the American War.\\\", \\\"tokens\\\": [\\\"The\\\", \\\"Hue–Da\\\", \\\"Nang\\\", \\\"Campaign\\\", \\\"was\\\", \\\"a\\\", \\\"series\\\", \\\"of\\\", \\\"military\\\", \\\"actions\\\", \\\"conducted\\\", \\\"by\\\", \\\"the\\\", \\\"People\\\", \\\"'s\\\", \\\"Army\\\", \\\"of\\\", \\\"Vietnam\\\", \\\"(\\\", \\\"PAVN\\\", \\\")\\\", \\\"against\\\", \\\"the\\\", \\\"Army\\\", \\\"of\\\", \\\"the\\\", \\\"Republic\\\", \\\"of\\\", \\\"Vietnam\\\", \\\"(\\\", \\\"ARVN\\\", \\\")\\\", \\\"during\\\", \\\"the\\\", \\\"Vietnam\\\", \\\"War\\\", \\\",\\\", \\\"also\\\", \\\"known\\\", \\\"in\\\", \\\"Vietnam\\\", \\\"as\\\", \\\"the\\\", \\\"American\\\", \\\"War\\\", \\\".\\\"]}, {\\\"sentence\\\": \\\"The campaign was centred on the cities of Huế (Thừa Thiên-Huế Province) and Da Nang (Quảng Nam Province), with secondary fronts in the provinces of Quảng Trị and Quảng Ngãi.\\\", \\\"tokens\\\": [\\\"The\\\", \\\"campaign\\\", \\\"was\\\", \\\"centred\\\", \\\"on\\\", \\\"the\\\", \\\"cities\\\", \\\"of\\\", \\\"Huế\\\", \\\"(\\\", \\\"Thừa\\\", \\\"Thiên-Huế\\\", \\\"Province\\\", \\\")\\\", \\\"and\\\", \\\"Da\\\", \\\"Nang\\\", \\\"(\\\", \\\"Quảng\\\", \\\"Nam\\\", \\\"Province\\\", \\\")\\\", \\\",\\\", \\\"with\\\", \\\"secondary\\\", \\\"fronts\\\", \\\"in\\\", \\\"the\\\", \\\"provinces\\\", \\\"of\\\", \\\"Quảng\\\", \\\"Trị\\\", \\\"and\\\", \\\"Quảng\\\", \\\"Ngãi\\\", \\\".\\\"]}, {\\\"sentence\\\": \\\"The campaign began on March 5 and concluded on April 2, 1975.\\\", \\\"tokens\\\": [\\\"The\\\", \\\"campaign\\\", \\\"began\\\", \\\"on\\\", \\\"March\\\", \\\"5\\\", \\\"and\\\", \\\"concluded\\\", \\\"on\\\", \\\"April\\\", \\\"2\\\", \\\",\\\", \\\"1975\\\", \\\".\\\"]}, {\\\"sentence\\\": \\\"During the spring season of 1975, the PAVN High Command in Hanoi made the decision to seize the major South Vietnamese cities of Huế and Da Nang, and also destroy the various South Vietnamese units in I Corps Tactical Zone, led by ARVN General Ngô Quang Trưởng.\\\", \\\"tokens\\\": [\\\"During\\\", \\\"the\\\", \\\"spring\\\", \\\"season\\\", \\\"of\\\", \\\"1975\\\", \\\",\\\", \\\"the\\\", \\\"PAVN\\\", \\\"High\\\", \\\"Command\\\", \\\"in\\\", \\\"Hanoi\\\", \\\"made\\\", \\\"the\\\", \\\"decision\\\", \\\"to\\\", \\\"seize\\\", \\\"the\\\", \\\"major\\\", \\\"South\\\", \\\"Vietnamese\\\", \\\"cities\\\", \\\"of\\\", \\\"Huế\\\", \\\"and\\\", \\\"Da\\\", \\\"Nang\\\", \\\",\\\", \\\"and\\\", \\\"also\\\", \\\"destroy\\\", \\\"the\\\", \\\"various\\\", \\\"South\\\", \\\"Vietnamese\\\", \\\"units\\\", \\\"in\\\", \\\"I\\\", \\\"Corps\\\", \\\"Tactical\\\", \\\"Zone\\\", \\\",\\\", \\\"led\\\", \\\"by\\\", \\\"ARVN\\\", \\\"General\\\", \\\"Ngô\\\", \\\"Quang\\\", \\\"Trưởng\\\", \\\".\\\"]}, {\\\"sentence\\\": \\\"Originally, the campaign was planned to take place over two phases; during the seasons of spring-summer and autumn.\\\", \\\"tokens\\\": [\\\"Originally\\\", \\\",\\\", \\\"the\\\", \\\"campaign\\\", \\\"was\\\", \\\"planned\\\", \\\"to\\\", \\\"take\\\", \\\"place\\\", \\\"over\\\", \\\"two\\\", \\\"phases\\\", \\\";\\\", \\\"during\\\", \\\"the\\\", \\\"seasons\\\", \\\"of\\\", \\\"spring-summer\\\", \\\"and\\\", \\\"autumn\\\", \\\".\\\"]}, {\\\"sentence\\\": \\\"However, as the North Vietnamese forces rolled over South Vietnamese defences on the outskirts of Huế and Da Nang, President Nguyễn Văn Thiệu ordered General Trưởng to abandon all territories under his control, and pull his forces back to the coastal areas of I Corps.\\\", \\\"tokens\\\": [\\\"However\\\", \\\",\\\", \\\"as\\\", \\\"the\\\", \\\"North\\\", \\\"Vietnamese\\\", \\\"forces\\\", \\\"rolled\\\", \\\"over\\\", \\\"South\\\", \\\"Vietnamese\\\", \\\"defences\\\", \\\"on\\\", \\\"the\\\", \\\"outskirts\\\", \\\"of\\\", \\\"Huế\\\", \\\"and\\\", \\\"Da\\\", \\\"Nang\\\", \\\",\\\", \\\"President\\\", \\\"Nguyễn\\\", \\\"Văn\\\", \\\"Thiệu\\\", \\\"ordered\\\", \\\"General\\\", \\\"Trưởng\\\", \\\"to\\\", \\\"abandon\\\", \\\"all\\\", \\\"territories\\\", \\\"under\\\", \\\"his\\\", \\\"control\\\", \\\",\\\", \\\"and\\\", \\\"pull\\\", \\\"his\\\", \\\"forces\\\", \\\"back\\\", \\\"to\\\", \\\"the\\\", \\\"coastal\\\", \\\"areas\\\", \\\"of\\\", \\\"I\\\", \\\"Corps\\\", \\\".\\\"]}, {\\\"sentence\\\": \\\"The South Vietnamese withdrawal quickly turned into a rout, as the PAVN 2nd Army Corps picked off one South Vietnamese unit after another, until Huế and Da Nang were completely surrounded.\\\", \\\"tokens\\\": [\\\"The\\\", \\\"South\\\", \\\"Vietnamese\\\", \\\"withdrawal\\\", \\\"quickly\\\", \\\"turned\\\", \\\"into\\\", \\\"a\\\", \\\"rout\\\", \\\",\\\", \\\"as\\\", \\\"the\\\", \\\"PAVN\\\", \\\"2nd\\\", \\\"Army\\\", \\\"Corps\\\", \\\"picked\\\", \\\"off\\\", \\\"one\\\", \\\"South\\\", \\\"Vietnamese\\\", \\\"unit\\\", \\\"after\\\", \\\"another\\\", \\\",\\\", \\\"until\\\", \\\"Huế\\\", \\\"and\\\", \\\"Da\\\", \\\"Nang\\\", \\\"were\\\", \\\"completely\\\", \\\"surrounded\\\", \\\".\\\"]}, {\\\"sentence\\\": \\\"By March 29, 1975, PAVN troops had full control of Huế and Da Nang, while South Vietnam lost all territories and most of the units belonging to I Corps.\\\", \\\"tokens\\\": [\\\"By\\\", \\\"March\\\", \\\"29\\\", \\\",\\\", \\\"1975\\\", \\\",\\\", \\\"PAVN\\\", \\\"troops\\\", \\\"had\\\", \\\"full\\\", \\\"control\\\", \\\"of\\\", \\\"Huế\\\", \\\"and\\\", \\\"Da\\\", \\\"Nang\\\", \\\",\\\", \\\"while\\\", \\\"South\\\", \\\"Vietnam\\\", \\\"lost\\\", \\\"all\\\", \\\"territories\\\", \\\"and\\\", \\\"most\\\", \\\"of\\\", \\\"the\\\", \\\"units\\\", \\\"belonging\\\", \\\"to\\\", \\\"I\\\", \\\"Corps\\\", \\\".\\\"]}, {\\\"sentence\\\": \\\"The fall of Huế and Da Nang did not spell the end of the misery suffered by the ARVN.\\\", \\\"tokens\\\": [\\\"The\\\", \\\"fall\\\", \\\"of\\\", \\\"Huế\\\", \\\"and\\\", \\\"Da\\\", \\\"Nang\\\", \\\"did\\\", \\\"not\\\", \\\"spell\\\", \\\"the\\\", \\\"end\\\", \\\"of\\\", \\\"the\\\", \\\"misery\\\", \\\"suffered\\\", \\\"by\\\", \\\"the\\\", \\\"ARVN\\\", \\\".\\\"]}, {\\\"sentence\\\": \\\"On March 31, ARVN General Phạm Văn Phú—commander of II Corps Tactical Zone—attempted to form a new defensive line from Qui Nhơn to cover the retreat of the ARVN 22nd Infantry Division, but they too were destroyed by the PAVN.\\\", \\\"tokens\\\": [\\\"On\\\", \\\"March\\\", \\\"31\\\", \\\",\\\", \\\"ARVN\\\", \\\"General\\\", \\\"Phạm\\\", \\\"Văn\\\", \\\"Phú—commander\\\", \\\"of\\\", \\\"II\\\", \\\"Corps\\\", \\\"Tactical\\\", \\\"Zone—attempted\\\", \\\"to\\\", \\\"form\\\", \\\"a\\\", \\\"new\\\", \\\"defensive\\\", \\\"line\\\", \\\"from\\\", \\\"Qui\\\", \\\"Nhơn\\\", \\\"to\\\", \\\"cover\\\", \\\"the\\\", \\\"retreat\\\", \\\"of\\\", \\\"the\\\", \\\"ARVN\\\", \\\"22nd\\\", \\\"Infantry\\\", \\\"Division\\\", \\\",\\\", \\\"but\\\", \\\"they\\\", \\\"too\\\", \\\"were\\\", \\\"destroyed\\\", \\\"by\\\", \\\"the\\\", \\\"PAVN\\\", \\\".\\\"]}, {\\\"sentence\\\": \\\"By April 2, South Vietnam had lost control of the northern provinces, as well as two army corps.\\\", \\\"tokens\\\": [\\\"By\\\", \\\"April\\\", \\\"2\\\", \\\",\\\", \\\"South\\\", \\\"Vietnam\\\", \\\"had\\\", \\\"lost\\\", \\\"control\\\", \\\"of\\\", \\\"the\\\", \\\"northern\\\", \\\"provinces\\\", \\\",\\\", \\\"as\\\", \\\"well\\\", \\\"as\\\", \\\"two\\\", \\\"army\\\", \\\"corps\\\", \\\".\\\"]}], \\\"candidates\\\": [{\\\"trigger_word\\\": \\\"Hue–Da\\\", \\\"sent_id\\\": 0, \\\"offset\\\": [1, 2], \\\"id\\\": \\\"233215802adc2c0bc41af9ee0739057c\\\"}, {\\\"trigger_word\\\": \\\"Nang\\\", \\\"sent_id\\\": 0, \\\"offset\\\": [2, 3], \\\"id\\\": \\\"8382944847cefe3fdd23384a6d42776d\\\"}, {\\\"trigger_word\\\": \\\"Campaign\\\", \\\"sent_id\\\": 0, \\\"offset\\\": [3, 4], \\\"id\\\": \\\"4f93019ec220d9ca7146c16634b4f0ec\\\"}, {\\\"trigger_word\\\": \\\"series\\\", \\\"sent_id\\\": 0, \\\"offset\\\": [6, 7], \\\"id\\\": \\\"581b770d8b9475ebf64d2cfff9d58c21\\\"}, {\\\"trigger_word\\\": \\\"military\\\", \\\"sent_id\\\": 0, \\\"offset\\\": [8, 9], \\\"id\\\": \\\"521350650386a70feb63fa4215598b5b\\\"}, {\\\"trigger_word\\\": \\\"actions\\\", \\\"sent_id\\\": 0, \\\"offset\\\": [9, 10], \\\"id\\\": \\\"2c2e2a6aa2e3f8188a2105d33505fa6a\\\"}, {\\\"trigger_word\\\": \\\"conducted\\\", \\\"sent_id\\\": 0, \\\"offset\\\": [10, 11], \\\"id\\\": \\\"8550d4921e0e0540350f89e0140d7004\\\"}, {\\\"trigger_word\\\": \\\"People\\\", \\\"sent_id\\\": 0, \\\"offset\\\": [13, 14], \\\"id\\\": \\\"bc02518ef522161df69314960a08d759\\\"}, {\\\"trigger_word\\\": \\\"Army\\\", \\\"sent_id\\\": 0, \\\"offset\\\": [15, 16], \\\"id\\\": \\\"9f38dabe12cc000e91bd76abab354c98\\\"}, {\\\"trigger_word\\\": \\\"Vietnam\\\", \\\"sent_id\\\": 0, \\\"offset\\\": [17, 18], \\\"id\\\": \\\"eea465af451692b2e89845b58cff26c5\\\"}, {\\\"trigger_word\\\": \\\"PAVN\\\", \\\"sent_id\\\": 0, \\\"offset\\\": [19, 20], \\\"id\\\": \\\"0282d79c45ef27b1af41013721362c48\\\"}, {\\\"trigger_word\\\": \\\"Army\\\", \\\"sent_id\\\": 0, \\\"offset\\\": [23, 24], \\\"id\\\": \\\"dcf6643ab4437e3d3550d6b7f0098e92\\\"}, {\\\"trigger_word\\\": \\\"Republic\\\", \\\"sent_id\\\": 0, \\\"offset\\\": [26, 27], \\\"id\\\": \\\"bb635b81cec60de72a3ca716abcc8054\\\"}, {\\\"trigger_word\\\": \\\"Vietnam\\\", \\\"sent_id\\\": 0, \\\"offset\\\": [28, 29], \\\"id\\\": \\\"64049307da3daca238b99786c11248bf\\\"}, {\\\"trigger_word\\\": \\\"ARVN\\\", \\\"sent_id\\\": 0, \\\"offset\\\": [30, 31], \\\"id\\\": \\\"b46995828aff4889ecbab16a8f3378a7\\\"}, {\\\"trigger_word\\\": \\\"Vietnam\\\", \\\"sent_id\\\": 0, \\\"offset\\\": [34, 35], \\\"id\\\": \\\"302ecc99a68e641d56e21b55e11b9f75\\\"}, {\\\"trigger_word\\\": \\\"War\\\", \\\"sent_id\\\": 0, \\\"offset\\\": [35, 36], \\\"id\\\": \\\"eeee48f8c53e0dac9166a82527aa587b\\\"}, {\\\"trigger_word\\\": \\\"also\\\", \\\"sent_id\\\": 0, \\\"offset\\\": [37, 38], \\\"id\\\": \\\"83089b475b23fb6406a895adaf21ef45\\\"}, {\\\"trigger_word\\\": \\\"known\\\", \\\"sent_id\\\": 0, \\\"offset\\\": [38, 39], \\\"id\\\": \\\"f5debbfc21380b50c177cb78dfeaad32\\\"}, {\\\"trigger_word\\\": \\\"Vietnam\\\", \\\"sent_id\\\": 0, \\\"offset\\\": [40, 41], \\\"id\\\": \\\"bc7e8bf7f64a25414a5f0961ac0760ce\\\"}, {\\\"trigger_word\\\": \\\"American\\\", \\\"sent_id\\\": 0, \\\"offset\\\": [43, 44], \\\"id\\\": \\\"a692b09b07809b331ec12f0ea0c52ca3\\\"}, {\\\"trigger_word\\\": \\\"War\\\", \\\"sent_id\\\": 0, \\\"offset\\\": [44, 45], \\\"id\\\": \\\"0ef81ab4ec82729fc9b24da7f2b9a970\\\"}, {\\\"trigger_word\\\": \\\"campaign\\\", \\\"sent_id\\\": 1, \\\"offset\\\": [1, 2], \\\"id\\\": \\\"1becb72ff147b31d614082cfda399aa7\\\"}, {\\\"trigger_word\\\": \\\"centred\\\", \\\"sent_id\\\": 1, \\\"offset\\\": [3, 4], \\\"id\\\": \\\"8569532188417b3805e7ed96abc1fd58\\\"}, {\\\"trigger_word\\\": \\\"cities\\\", \\\"sent_id\\\": 1, \\\"offset\\\": [6, 7], \\\"id\\\": \\\"64b6bc1a63a4fa2514cb1ee5016df1ef\\\"}, {\\\"trigger_word\\\": \\\"Huế\\\", \\\"sent_id\\\": 1, \\\"offset\\\": [8, 9], \\\"id\\\": \\\"67beed5547ea70d9b3ae48fc8f899e74\\\"}, {\\\"trigger_word\\\": \\\"Thừa\\\", \\\"sent_id\\\": 1, \\\"offset\\\": [10, 11], \\\"id\\\": \\\"68949b252bc55385b4f6009448bf6421\\\"}, {\\\"trigger_word\\\": \\\"Thiên-Huế\\\", \\\"sent_id\\\": 1, \\\"offset\\\": [11, 12], \\\"id\\\": \\\"29044ee39138d2f61b25ef3adddb3f2c\\\"}, {\\\"trigger_word\\\": \\\"Province\\\", \\\"sent_id\\\": 1, \\\"offset\\\": [12, 13], \\\"id\\\": \\\"1a6fc6dea0edca75a32bd0c751e67bd8\\\"}, {\\\"trigger_word\\\": \\\"Da\\\", \\\"sent_id\\\": 1, \\\"offset\\\": [15, 16], \\\"id\\\": \\\"e824a81cfbe5b4406d5c58e0c094bd1c\\\"}, {\\\"trigger_word\\\": \\\"Nang\\\", \\\"sent_id\\\": 1, \\\"offset\\\": [16, 17], \\\"id\\\": \\\"a7c9273c1d4407d566a29af57f39ae26\\\"}, {\\\"trigger_word\\\": \\\"Quảng\\\", \\\"sent_id\\\": 1, \\\"offset\\\": [18, 19], \\\"id\\\": \\\"e17ff1288b85403cb8b1f8ce356a8c8a\\\"}, {\\\"trigger_word\\\": \\\"Nam\\\", \\\"sent_id\\\": 1, \\\"offset\\\": [19, 20], \\\"id\\\": \\\"aea75561bec5cc57d3d34c6af0267b20\\\"}, {\\\"trigger_word\\\": \\\"Province\\\", \\\"sent_id\\\": 1, \\\"offset\\\": [20, 21], \\\"id\\\": \\\"8f527e9ac1dd0aafbe7d90a9ea1b2ef8\\\"}, {\\\"trigger_word\\\": \\\"secondary\\\", \\\"sent_id\\\": 1, \\\"offset\\\": [24, 25], \\\"id\\\": \\\"9ccee7be31c727a8e5b41589930ad138\\\"}, {\\\"trigger_word\\\": \\\"fronts\\\", \\\"sent_id\\\": 1, \\\"offset\\\": [25, 26], \\\"id\\\": \\\"b24450e1a66d33d6ae6bf3a6298a88ce\\\"}, {\\\"trigger_word\\\": \\\"provinces\\\", \\\"sent_id\\\": 1, \\\"offset\\\": [28, 29], \\\"id\\\": \\\"9fe9310879c3b9d3c1999631e60899c9\\\"}, {\\\"trigger_word\\\": \\\"Quảng\\\", \\\"sent_id\\\": 1, \\\"offset\\\": [30, 31], \\\"id\\\": \\\"2714d62023df700e8b2801eb49f40434\\\"}, {\\\"trigger_word\\\": \\\"Trị\\\", \\\"sent_id\\\": 1, \\\"offset\\\": [31, 32], \\\"id\\\": \\\"353d7a03115c3c55f0036b971bc6b413\\\"}, {\\\"trigger_word\\\": \\\"Quảng\\\", \\\"sent_id\\\": 1, \\\"offset\\\": [33, 34], \\\"id\\\": \\\"ba028e8b0f0c9259dc103e204852bdd6\\\"}, {\\\"trigger_word\\\": \\\"Ngãi\\\", \\\"sent_id\\\": 1, \\\"offset\\\": [34, 35], \\\"id\\\": \\\"b682730ddaf7c2cc846da1aec9b636cf\\\"}, {\\\"trigger_word\\\": \\\"campaign\\\", \\\"sent_id\\\": 2, \\\"offset\\\": [1, 2], \\\"id\\\": \\\"f6d22f86b6b37323f3a116b388b37cf2\\\"}, {\\\"trigger_word\\\": \\\"began\\\", \\\"sent_id\\\": 2, \\\"offset\\\": [2, 3], \\\"id\\\": \\\"fd2d283211dbe0f2ab0dfca74b845a88\\\"}, {\\\"trigger_word\\\": \\\"March\\\", \\\"sent_id\\\": 2, \\\"offset\\\": [4, 5], \\\"id\\\": \\\"776ca7fbe417da88ca188d5200aa60d3\\\"}, {\\\"trigger_word\\\": \\\"concluded\\\", \\\"sent_id\\\": 2, \\\"offset\\\": [7, 8], \\\"id\\\": \\\"8bce2f493a9109d1314a11d6ebc690b2\\\"}, {\\\"trigger_word\\\": \\\"April\\\", \\\"sent_id\\\": 2, \\\"offset\\\": [9, 10], \\\"id\\\": \\\"ee40c0e441e54b86e75b1d39096d7177\\\"}, {\\\"trigger_word\\\": \\\"spring\\\", \\\"sent_id\\\": 3, \\\"offset\\\": [2, 3], \\\"id\\\": \\\"257b9a17fed0c83c972a66ba34778d17\\\"}, {\\\"trigger_word\\\": \\\"season\\\", \\\"sent_id\\\": 3, \\\"offset\\\": [3, 4], \\\"id\\\": \\\"69dbca96190efc140a037f05329e0d64\\\"}, {\\\"trigger_word\\\": \\\"PAVN\\\", \\\"sent_id\\\": 3, \\\"offset\\\": [8, 9], \\\"id\\\": \\\"339bfdc52996ed19ecebbc5cc21435b0\\\"}, {\\\"trigger_word\\\": \\\"High\\\", \\\"sent_id\\\": 3, \\\"offset\\\": [9, 10], \\\"id\\\": \\\"b3c6c2852fb05403ace01396e126e311\\\"}, {\\\"trigger_word\\\": \\\"Command\\\", \\\"sent_id\\\": 3, \\\"offset\\\": [10, 11], \\\"id\\\": \\\"2c51e7ce57f26a6f17a6b909c718350c\\\"}, {\\\"trigger_word\\\": \\\"Hanoi\\\", \\\"sent_id\\\": 3, \\\"offset\\\": [12, 13], \\\"id\\\": \\\"29148d6ae4b428d566aa5f19eab155cc\\\"}, {\\\"trigger_word\\\": \\\"made\\\", \\\"sent_id\\\": 3, \\\"offset\\\": [13, 14], \\\"id\\\": \\\"0f06a4ac7dbe571521a176b14d6dc375\\\"}, {\\\"trigger_word\\\": \\\"decision\\\", \\\"sent_id\\\": 3, \\\"offset\\\": [15, 16], \\\"id\\\": \\\"899236f07eced5133544edf84ca6c0fd\\\"}, {\\\"trigger_word\\\": \\\"seize\\\", \\\"sent_id\\\": 3, \\\"offset\\\": [17, 18], \\\"id\\\": \\\"d265ec21ba8dd8b4977ed3b4208bbbe4\\\"}, {\\\"trigger_word\\\": \\\"major\\\", \\\"sent_id\\\": 3, \\\"offset\\\": [19, 20], \\\"id\\\": \\\"c6dd74bbc7caf5d1cf51d06ac70b5d0f\\\"}, {\\\"trigger_word\\\": \\\"South\\\", \\\"sent_id\\\": 3, \\\"offset\\\": [20, 21], \\\"id\\\": \\\"dc0a65aa6c3c0ebf49d794c45e755653\\\"}, {\\\"trigger_word\\\": \\\"Vietnamese\\\", \\\"sent_id\\\": 3, \\\"offset\\\": [21, 22], \\\"id\\\": \\\"f508e178eb146b4f4398bf8339443fd6\\\"}, {\\\"trigger_word\\\": \\\"cities\\\", \\\"sent_id\\\": 3, \\\"offset\\\": [22, 23], \\\"id\\\": \\\"a5e627df8620a7f184814ae6523c94ce\\\"}, {\\\"trigger_word\\\": \\\"Huế\\\", \\\"sent_id\\\": 3, \\\"offset\\\": [24, 25], \\\"id\\\": \\\"06a8b19a81ba24d1cb8a0f3c2e49a0d0\\\"}, {\\\"trigger_word\\\": \\\"Da\\\", \\\"sent_id\\\": 3, \\\"offset\\\": [26, 27], \\\"id\\\": \\\"0115ccdaf8d4ccfb248465698eb23497\\\"}, {\\\"trigger_word\\\": \\\"Nang\\\", \\\"sent_id\\\": 3, \\\"offset\\\": [27, 28], \\\"id\\\": \\\"e595dc5ec3103352a169fd5f1130d88b\\\"}, {\\\"trigger_word\\\": \\\"also\\\", \\\"sent_id\\\": 3, \\\"offset\\\": [30, 31], \\\"id\\\": \\\"0eb8faea771aafb8efd36878b9227f49\\\"}, {\\\"trigger_word\\\": \\\"destroy\\\", \\\"sent_id\\\": 3, \\\"offset\\\": [31, 32], \\\"id\\\": \\\"5491ca8d3588f5faf7ae5d41fbd3ba72\\\"}, {\\\"trigger_word\\\": \\\"various\\\", \\\"sent_id\\\": 3, \\\"offset\\\": [33, 34], \\\"id\\\": \\\"14f2b230944f97baba17e35988966014\\\"}, {\\\"trigger_word\\\": \\\"South\\\", \\\"sent_id\\\": 3, \\\"offset\\\": [34, 35], \\\"id\\\": \\\"21b92998a59db6ed6187ecaf5498cace\\\"}, {\\\"trigger_word\\\": \\\"Vietnamese\\\", \\\"sent_id\\\": 3, \\\"offset\\\": [35, 36], \\\"id\\\": \\\"a815a985ce865dcb0d8e07972869f177\\\"}, {\\\"trigger_word\\\": \\\"units\\\", \\\"sent_id\\\": 3, \\\"offset\\\": [36, 37], \\\"id\\\": \\\"9b11aeb636608c68af009b801a9679b2\\\"}, {\\\"trigger_word\\\": \\\"Corps\\\", \\\"sent_id\\\": 3, \\\"offset\\\": [39, 40], \\\"id\\\": \\\"0933edb85bce97ca7bbd2f207c3c25d2\\\"}, {\\\"trigger_word\\\": \\\"Tactical\\\", \\\"sent_id\\\": 3, \\\"offset\\\": [40, 41], \\\"id\\\": \\\"341a3964aa3f07ce8503f97d3f2906c3\\\"}, {\\\"trigger_word\\\": \\\"Zone\\\", \\\"sent_id\\\": 3, \\\"offset\\\": [41, 42], \\\"id\\\": \\\"991702376aade1a3314bf1599dbaf3c3\\\"}, {\\\"trigger_word\\\": \\\"led\\\", \\\"sent_id\\\": 3, \\\"offset\\\": [43, 44], \\\"id\\\": \\\"b8a2c2d66d2a11cc5b6175aedc4d6a69\\\"}, {\\\"trigger_word\\\": \\\"ARVN\\\", \\\"sent_id\\\": 3, \\\"offset\\\": [45, 46], \\\"id\\\": \\\"33d48cd1bd6611499822624958692aa5\\\"}, {\\\"trigger_word\\\": \\\"General\\\", \\\"sent_id\\\": 3, \\\"offset\\\": [46, 47], \\\"id\\\": \\\"fbb80746fcf63289da15b08b252ad824\\\"}, {\\\"trigger_word\\\": \\\"Ngô\\\", \\\"sent_id\\\": 3, \\\"offset\\\": [47, 48], \\\"id\\\": \\\"56683837e449c43a1c07d516a9f7977d\\\"}, {\\\"trigger_word\\\": \\\"Quang\\\", \\\"sent_id\\\": 3, \\\"offset\\\": [48, 49], \\\"id\\\": \\\"a70e99903c8f2669c3e5e4cd733b3644\\\"}, {\\\"trigger_word\\\": \\\"Trưởng\\\", \\\"sent_id\\\": 3, \\\"offset\\\": [49, 50], \\\"id\\\": \\\"2d47223e4c354449f6398352989fb638\\\"}, {\\\"trigger_word\\\": \\\"Originally\\\", \\\"sent_id\\\": 4, \\\"offset\\\": [0, 1], \\\"id\\\": \\\"2292c38b99fbab85e7fe557bb800e9c8\\\"}, {\\\"trigger_word\\\": \\\"campaign\\\", \\\"sent_id\\\": 4, \\\"offset\\\": [3, 4], \\\"id\\\": \\\"3b5fd983eaaa925090cf2e9fa20bf223\\\"}, {\\\"trigger_word\\\": \\\"planned\\\", \\\"sent_id\\\": 4, \\\"offset\\\": [5, 6], \\\"id\\\": \\\"e54efebab15db1f4245bea83d9c56aff\\\"}, {\\\"trigger_word\\\": \\\"take place\\\", \\\"sent_id\\\": 4, \\\"offset\\\": [7, 9], \\\"id\\\": \\\"574c1dde85b7b1c9fb5706cba35f597e\\\"}, {\\\"trigger_word\\\": \\\"phases\\\", \\\"sent_id\\\": 4, \\\"offset\\\": [11, 12], \\\"id\\\": \\\"f06cd6e8229509f8844ef2e677c22b1c\\\"}, {\\\"trigger_word\\\": \\\"seasons\\\", \\\"sent_id\\\": 4, \\\"offset\\\": [15, 16], \\\"id\\\": \\\"02d2b6a9133aa00a6864139387b735ef\\\"}, {\\\"trigger_word\\\": \\\"spring-summer\\\", \\\"sent_id\\\": 4, \\\"offset\\\": [17, 18], \\\"id\\\": \\\"ee7d98136cbfc7b073829baba2c9def8\\\"}, {\\\"trigger_word\\\": \\\"autumn\\\", \\\"sent_id\\\": 4, \\\"offset\\\": [19, 20], \\\"id\\\": \\\"caef810f5ad925a0f8288bc0e2fba10b\\\"}, {\\\"trigger_word\\\": \\\"However\\\", \\\"sent_id\\\": 5, \\\"offset\\\": [0, 1], \\\"id\\\": \\\"46dbfba27cd337e4fb221e3ff3a0db0c\\\"}, {\\\"trigger_word\\\": \\\"North\\\", \\\"sent_id\\\": 5, \\\"offset\\\": [4, 5], \\\"id\\\": \\\"777d73f214517d2e8dc2debca49213a5\\\"}, {\\\"trigger_word\\\": \\\"Vietnamese\\\", \\\"sent_id\\\": 5, \\\"offset\\\": [5, 6], \\\"id\\\": \\\"ebb4acde94a50e8451b6a63fcccf9a63\\\"}, {\\\"trigger_word\\\": \\\"forces\\\", \\\"sent_id\\\": 5, \\\"offset\\\": [6, 7], \\\"id\\\": \\\"062e51ab634a7b5735ecb915f971a971\\\"}, {\\\"trigger_word\\\": \\\"rolled\\\", \\\"sent_id\\\": 5, \\\"offset\\\": [7, 8], \\\"id\\\": \\\"907cf482386a5b4ce790d8d362accbad\\\"}, {\\\"trigger_word\\\": \\\"South\\\", \\\"sent_id\\\": 5, \\\"offset\\\": [9, 10], \\\"id\\\": \\\"15ba1aa21053c4dfc4e6d3e488da9c21\\\"}, {\\\"trigger_word\\\": \\\"Vietnamese\\\", \\\"sent_id\\\": 5, \\\"offset\\\": [10, 11], \\\"id\\\": \\\"0aa45a59533c5cca3c80034382d46349\\\"}, {\\\"trigger_word\\\": \\\"defences\\\", \\\"sent_id\\\": 5, \\\"offset\\\": [11, 12], \\\"id\\\": \\\"46b42c8895d32e7f67cd0fb52900f9bf\\\"}, {\\\"trigger_word\\\": \\\"outskirts\\\", \\\"sent_id\\\": 5, \\\"offset\\\": [14, 15], \\\"id\\\": \\\"7fb815bac1e8a16c814fc8b7e86bcb22\\\"}, {\\\"trigger_word\\\": \\\"Huế\\\", \\\"sent_id\\\": 5, \\\"offset\\\": [16, 17], \\\"id\\\": \\\"a4aa5a767744e7ac963c994b6849a7cb\\\"}, {\\\"trigger_word\\\": \\\"Da\\\", \\\"sent_id\\\": 5, \\\"offset\\\": [18, 19], \\\"id\\\": \\\"83203b62fb3d860c40cc641bcb2ff699\\\"}, {\\\"trigger_word\\\": \\\"Nang\\\", \\\"sent_id\\\": 5, \\\"offset\\\": [19, 20], \\\"id\\\": \\\"5bb65dbf3e995e975bdd1884d3508652\\\"}, {\\\"trigger_word\\\": \\\"President\\\", \\\"sent_id\\\": 5, \\\"offset\\\": [21, 22], \\\"id\\\": \\\"11910e0a9d2876438c5d73474a634d26\\\"}, {\\\"trigger_word\\\": \\\"Nguyễn\\\", \\\"sent_id\\\": 5, \\\"offset\\\": [22, 23], \\\"id\\\": \\\"518542a3a0208601f7b45202354c0b08\\\"}, {\\\"trigger_word\\\": \\\"Văn\\\", \\\"sent_id\\\": 5, \\\"offset\\\": [23, 24], \\\"id\\\": \\\"9f398794440413febae16b264ee19bb8\\\"}, {\\\"trigger_word\\\": \\\"Thiệu\\\", \\\"sent_id\\\": 5, \\\"offset\\\": [24, 25], \\\"id\\\": \\\"331916ad36c2fc151bb383db00c1dfb2\\\"}, {\\\"trigger_word\\\": \\\"ordered\\\", \\\"sent_id\\\": 5, \\\"offset\\\": [25, 26], \\\"id\\\": \\\"ae20f59a77162429f195a7e56f5c75ea\\\"}, {\\\"trigger_word\\\": \\\"General\\\", \\\"sent_id\\\": 5, \\\"offset\\\": [26, 27], \\\"id\\\": \\\"d45af80ccfa7118438b5c65322a3cde4\\\"}, {\\\"trigger_word\\\": \\\"Trưởng\\\", \\\"sent_id\\\": 5, \\\"offset\\\": [27, 28], \\\"id\\\": \\\"02ed0523d08ec712fbcc39557dc48dde\\\"}, {\\\"trigger_word\\\": \\\"abandon\\\", \\\"sent_id\\\": 5, \\\"offset\\\": [29, 30], \\\"id\\\": \\\"21581d2d1bcda004cfd88557a680b603\\\"}, {\\\"trigger_word\\\": \\\"territories\\\", \\\"sent_id\\\": 5, \\\"offset\\\": [31, 32], \\\"id\\\": \\\"0bc490b5e82958756244b194036a8e2d\\\"}, {\\\"trigger_word\\\": \\\"control\\\", \\\"sent_id\\\": 5, \\\"offset\\\": [34, 35], \\\"id\\\": \\\"c33a7a5d8e4a42069b9272640ba88cd0\\\"}, {\\\"trigger_word\\\": \\\"pull\\\", \\\"sent_id\\\": 5, \\\"offset\\\": [37, 38], \\\"id\\\": \\\"8d95094e944a187f174726092fe05ee5\\\"}, {\\\"trigger_word\\\": \\\"forces\\\", \\\"sent_id\\\": 5, \\\"offset\\\": [39, 40], \\\"id\\\": \\\"c37d3bb567c4d4f208d2fc92a24ddc21\\\"}, {\\\"trigger_word\\\": \\\"back\\\", \\\"sent_id\\\": 5, \\\"offset\\\": [40, 41], \\\"id\\\": \\\"f8f371d9b2754bad38db312628a2550e\\\"}, {\\\"trigger_word\\\": \\\"coastal\\\", \\\"sent_id\\\": 5, \\\"offset\\\": [43, 44], \\\"id\\\": \\\"ccc8e40e62120d381327648736cf90dc\\\"}, {\\\"trigger_word\\\": \\\"areas\\\", \\\"sent_id\\\": 5, \\\"offset\\\": [44, 45], \\\"id\\\": \\\"b9dd3bf208efee7dfe229c482a01ec1d\\\"}, {\\\"trigger_word\\\": \\\"Corps\\\", \\\"sent_id\\\": 5, \\\"offset\\\": [47, 48], \\\"id\\\": \\\"44577f357b29f901f409dbd9cc683c71\\\"}, {\\\"trigger_word\\\": \\\"South\\\", \\\"sent_id\\\": 6, \\\"offset\\\": [1, 2], \\\"id\\\": \\\"98048e3447969052850fbd886dede4e3\\\"}, {\\\"trigger_word\\\": \\\"Vietnamese\\\", \\\"sent_id\\\": 6, \\\"offset\\\": [2, 3], \\\"id\\\": \\\"9201815352afa7c4623f927e25a6b1d2\\\"}, {\\\"trigger_word\\\": \\\"withdrawal\\\", \\\"sent_id\\\": 6, \\\"offset\\\": [3, 4], \\\"id\\\": \\\"07a63d382199fa309288110c74659045\\\"}, {\\\"trigger_word\\\": \\\"quickly\\\", \\\"sent_id\\\": 6, \\\"offset\\\": [4, 5], \\\"id\\\": \\\"edbba9e3431ee434809cd540724978ac\\\"}, {\\\"trigger_word\\\": \\\"turned\\\", \\\"sent_id\\\": 6, \\\"offset\\\": [5, 6], \\\"id\\\": \\\"638df8052db1c38f8567e37a31f68fa7\\\"}, {\\\"trigger_word\\\": \\\"PAVN\\\", \\\"sent_id\\\": 6, \\\"offset\\\": [12, 13], \\\"id\\\": \\\"dd3ac07130d2e32839de9fb0b3ca6cf1\\\"}, {\\\"trigger_word\\\": \\\"Army\\\", \\\"sent_id\\\": 6, \\\"offset\\\": [14, 15], \\\"id\\\": \\\"1ecf559d2127a502145eab6360ba6734\\\"}, {\\\"trigger_word\\\": \\\"Corps\\\", \\\"sent_id\\\": 6, \\\"offset\\\": [15, 16], \\\"id\\\": \\\"f4d0603818c1c85bdbc9614fb0a59ca1\\\"}, {\\\"trigger_word\\\": \\\"picked off\\\", \\\"sent_id\\\": 6, \\\"offset\\\": [16, 18], \\\"id\\\": \\\"f122a917523850faeaf18dd626ca6bef\\\"}, {\\\"trigger_word\\\": \\\"South\\\", \\\"sent_id\\\": 6, \\\"offset\\\": [19, 20], \\\"id\\\": \\\"7d954078b27cfb79e0c450ae3ce95447\\\"}, {\\\"trigger_word\\\": \\\"Vietnamese\\\", \\\"sent_id\\\": 6, \\\"offset\\\": [20, 21], \\\"id\\\": \\\"99b2ba8720705b15aa7e6c05855090d7\\\"}, {\\\"trigger_word\\\": \\\"unit\\\", \\\"sent_id\\\": 6, \\\"offset\\\": [21, 22], \\\"id\\\": \\\"826f9a7db692544f25dee44e12953d3b\\\"}, {\\\"trigger_word\\\": \\\"Huế\\\", \\\"sent_id\\\": 6, \\\"offset\\\": [26, 27], \\\"id\\\": \\\"40bc20c45c68eba01c98458c27df4b94\\\"}, {\\\"trigger_word\\\": \\\"Da\\\", \\\"sent_id\\\": 6, \\\"offset\\\": [28, 29], \\\"id\\\": \\\"e9a265409a332421427cc693ab09e204\\\"}, {\\\"trigger_word\\\": \\\"Nang\\\", \\\"sent_id\\\": 6, \\\"offset\\\": [29, 30], \\\"id\\\": \\\"7b295b0970bbbebfe14521b9382ea16b\\\"}, {\\\"trigger_word\\\": \\\"completely\\\", \\\"sent_id\\\": 6, \\\"offset\\\": [31, 32], \\\"id\\\": \\\"87041cb78647cca090c3901c253e3797\\\"}, {\\\"trigger_word\\\": \\\"surrounded\\\", \\\"sent_id\\\": 6, \\\"offset\\\": [32, 33], \\\"id\\\": \\\"a052ed845853bc5cd39bcdd4ad02541e\\\"}, {\\\"trigger_word\\\": \\\"March\\\", \\\"sent_id\\\": 7, \\\"offset\\\": [1, 2], \\\"id\\\": \\\"6c78dce56efc6eff45e2f07c981df5aa\\\"}, {\\\"trigger_word\\\": \\\"PAVN\\\", \\\"sent_id\\\": 7, \\\"offset\\\": [6, 7], \\\"id\\\": \\\"4be4482cf45ad4a72b8bdf9534281c06\\\"}, {\\\"trigger_word\\\": \\\"troops\\\", \\\"sent_id\\\": 7, \\\"offset\\\": [7, 8], \\\"id\\\": \\\"30d17639f2a33aeccbecd83b03800342\\\"}, {\\\"trigger_word\\\": \\\"full\\\", \\\"sent_id\\\": 7, \\\"offset\\\": [9, 10], \\\"id\\\": \\\"82d086929e03d457081eda02cf929f00\\\"}, {\\\"trigger_word\\\": \\\"control\\\", \\\"sent_id\\\": 7, \\\"offset\\\": [10, 11], \\\"id\\\": \\\"519a472ed0dcc6920f81620d090d9d0d\\\"}, {\\\"trigger_word\\\": \\\"Huế\\\", \\\"sent_id\\\": 7, \\\"offset\\\": [12, 13], \\\"id\\\": \\\"4d24662587fd31d8d6c336acbe642366\\\"}, {\\\"trigger_word\\\": \\\"Da\\\", \\\"sent_id\\\": 7, \\\"offset\\\": [14, 15], \\\"id\\\": \\\"f806aee655aebed0a78c7fffcb0c6dd5\\\"}, {\\\"trigger_word\\\": \\\"Nang\\\", \\\"sent_id\\\": 7, \\\"offset\\\": [15, 16], \\\"id\\\": \\\"8dbbfcdb1fdd5fc08cc32a5bc6e351f0\\\"}, {\\\"trigger_word\\\": \\\"South\\\", \\\"sent_id\\\": 7, \\\"offset\\\": [18, 19], \\\"id\\\": \\\"c1ea7eeef996a0de9ef95b404ffdfcf0\\\"}, {\\\"trigger_word\\\": \\\"Vietnam\\\", \\\"sent_id\\\": 7, \\\"offset\\\": [19, 20], \\\"id\\\": \\\"cd7e23fc26ab4312f9af73a4ec333aa6\\\"}, {\\\"trigger_word\\\": \\\"lost\\\", \\\"sent_id\\\": 7, \\\"offset\\\": [20, 21], \\\"id\\\": \\\"299f4d4628c751901444e72f39a8a045\\\"}, {\\\"trigger_word\\\": \\\"territories\\\", \\\"sent_id\\\": 7, \\\"offset\\\": [22, 23], \\\"id\\\": \\\"a2ecee3d339875800b92254baaf95b0b\\\"}, {\\\"trigger_word\\\": \\\"units\\\", \\\"sent_id\\\": 7, \\\"offset\\\": [27, 28], \\\"id\\\": \\\"0af999f27cba728ca54402c6720b6587\\\"}, {\\\"trigger_word\\\": \\\"belonging\\\", \\\"sent_id\\\": 7, \\\"offset\\\": [28, 29], \\\"id\\\": \\\"6b4e9cda0f532fff7ef5e74bfde1f2d9\\\"}, {\\\"trigger_word\\\": \\\"Corps\\\", \\\"sent_id\\\": 7, \\\"offset\\\": [31, 32], \\\"id\\\": \\\"cc8973af4fc9d7471455b8c7526afc71\\\"}, {\\\"trigger_word\\\": \\\"fall\\\", \\\"sent_id\\\": 8, \\\"offset\\\": [1, 2], \\\"id\\\": \\\"2eae156b222d5f8d70c4ba565443294c\\\"}, {\\\"trigger_word\\\": \\\"Huế\\\", \\\"sent_id\\\": 8, \\\"offset\\\": [3, 4], \\\"id\\\": \\\"cd076ba245a7a088dfd4b7e5b783a2fe\\\"}, {\\\"trigger_word\\\": \\\"Da\\\", \\\"sent_id\\\": 8, \\\"offset\\\": [5, 6], \\\"id\\\": \\\"57d78a8638a41c305e7229749c49c8bf\\\"}, {\\\"trigger_word\\\": \\\"Nang\\\", \\\"sent_id\\\": 8, \\\"offset\\\": [6, 7], \\\"id\\\": \\\"0c82c3d34dd7c0648d14e28bf33c3d9d\\\"}, {\\\"trigger_word\\\": \\\"spell\\\", \\\"sent_id\\\": 8, \\\"offset\\\": [9, 10], \\\"id\\\": \\\"35bb3f0152b07b0457016259f9bf3f40\\\"}, {\\\"trigger_word\\\": \\\"end\\\", \\\"sent_id\\\": 8, \\\"offset\\\": [11, 12], \\\"id\\\": \\\"81145928115a4b4a1eae12133134af0e\\\"}, {\\\"trigger_word\\\": \\\"misery\\\", \\\"sent_id\\\": 8, \\\"offset\\\": [14, 15], \\\"id\\\": \\\"34fdde1210ca5d801ab4d40b2b737ae4\\\"}, {\\\"trigger_word\\\": \\\"suffered\\\", \\\"sent_id\\\": 8, \\\"offset\\\": [15, 16], \\\"id\\\": \\\"88cbefb27de064dc4c6176f6ad38b997\\\"}, {\\\"trigger_word\\\": \\\"ARVN\\\", \\\"sent_id\\\": 8, \\\"offset\\\": [18, 19], \\\"id\\\": \\\"27d2c8971bed1e31a7cf5aa1656faea2\\\"}, {\\\"trigger_word\\\": \\\"March\\\", \\\"sent_id\\\": 9, \\\"offset\\\": [1, 2], \\\"id\\\": \\\"20707350e3cd5ac615e53385cc4977de\\\"}, {\\\"trigger_word\\\": \\\"ARVN\\\", \\\"sent_id\\\": 9, \\\"offset\\\": [4, 5], \\\"id\\\": \\\"fbcbb6c1d0b387c79e170fbfd80e77e4\\\"}, {\\\"trigger_word\\\": \\\"General\\\", \\\"sent_id\\\": 9, \\\"offset\\\": [5, 6], \\\"id\\\": \\\"85e7d65b94ad5faf1c4b5196b6b14f6b\\\"}, {\\\"trigger_word\\\": \\\"Phạm\\\", \\\"sent_id\\\": 9, \\\"offset\\\": [6, 7], \\\"id\\\": \\\"fe9306dd136a79b438acc2f137721d8e\\\"}, {\\\"trigger_word\\\": \\\"Văn\\\", \\\"sent_id\\\": 9, \\\"offset\\\": [7, 8], \\\"id\\\": \\\"61dcbf45872b71d05a8cb69778a0cbd3\\\"}, {\\\"trigger_word\\\": \\\"Phú—commander\\\", \\\"sent_id\\\": 9, \\\"offset\\\": [8, 9], \\\"id\\\": \\\"38509af9bca8396e3527cd9dec8696c5\\\"}, {\\\"trigger_word\\\": \\\"II\\\", \\\"sent_id\\\": 9, \\\"offset\\\": [10, 11], \\\"id\\\": \\\"3a40f65cb16325c5ab76bfe9ca5982dc\\\"}, {\\\"trigger_word\\\": \\\"Corps\\\", \\\"sent_id\\\": 9, \\\"offset\\\": [11, 12], \\\"id\\\": \\\"f55c40c103cedf94a81399dc61c11850\\\"}, {\\\"trigger_word\\\": \\\"Tactical\\\", \\\"sent_id\\\": 9, \\\"offset\\\": [12, 13], \\\"id\\\": \\\"d69b813e0d15a957ff87129e1a41b870\\\"}, {\\\"trigger_word\\\": \\\"Zone—attempted\\\", \\\"sent_id\\\": 9, \\\"offset\\\": [13, 14], \\\"id\\\": \\\"4df9ecc3ce825525950f58940b37cdf6\\\"}, {\\\"trigger_word\\\": \\\"form\\\", \\\"sent_id\\\": 9, \\\"offset\\\": [15, 16], \\\"id\\\": \\\"85802d94bc46ee2416f6e88b468301c3\\\"}, {\\\"trigger_word\\\": \\\"new\\\", \\\"sent_id\\\": 9, \\\"offset\\\": [17, 18], \\\"id\\\": \\\"38a23ea559b94dcd835a73d676b55062\\\"}, {\\\"trigger_word\\\": \\\"defensive\\\", \\\"sent_id\\\": 9, \\\"offset\\\": [18, 19], \\\"id\\\": \\\"6225daa01cd09a72aede9dc0508a028b\\\"}, {\\\"trigger_word\\\": \\\"line\\\", \\\"sent_id\\\": 9, \\\"offset\\\": [19, 20], \\\"id\\\": \\\"4901edecb3f75751905aaad96d7320d0\\\"}, {\\\"trigger_word\\\": \\\"Qui\\\", \\\"sent_id\\\": 9, \\\"offset\\\": [21, 22], \\\"id\\\": \\\"d91d9d315e39667e59c82cf8ffbbde87\\\"}, {\\\"trigger_word\\\": \\\"Nhơn\\\", \\\"sent_id\\\": 9, \\\"offset\\\": [22, 23], \\\"id\\\": \\\"5ca0b9fd1d35d83bbf8d37fd77dfc5ac\\\"}, {\\\"trigger_word\\\": \\\"cover\\\", \\\"sent_id\\\": 9, \\\"offset\\\": [24, 25], \\\"id\\\": \\\"661f214c4b3aea3dd369f5c8997570b2\\\"}, {\\\"trigger_word\\\": \\\"retreat\\\", \\\"sent_id\\\": 9, \\\"offset\\\": [26, 27], \\\"id\\\": \\\"5d5e6da664845701e49470e92c22298f\\\"}, {\\\"trigger_word\\\": \\\"ARVN\\\", \\\"sent_id\\\": 9, \\\"offset\\\": [29, 30], \\\"id\\\": \\\"b68c1c50310d981fc684ff815773232d\\\"}, {\\\"trigger_word\\\": \\\"Infantry\\\", \\\"sent_id\\\": 9, \\\"offset\\\": [31, 32], \\\"id\\\": \\\"e956db6846b78863b2fe18c47db572b8\\\"}, {\\\"trigger_word\\\": \\\"Division\\\", \\\"sent_id\\\": 9, \\\"offset\\\": [32, 33], \\\"id\\\": \\\"dee2cc917f2d6042ecd9def30626e441\\\"}, {\\\"trigger_word\\\": \\\"destroyed\\\", \\\"sent_id\\\": 9, \\\"offset\\\": [38, 39], \\\"id\\\": \\\"7f794510042f8cfe31573a7d86fd3b1e\\\"}, {\\\"trigger_word\\\": \\\"PAVN\\\", \\\"sent_id\\\": 9, \\\"offset\\\": [41, 42], \\\"id\\\": \\\"1158e449f4ed781772778a2c630f6933\\\"}, {\\\"trigger_word\\\": \\\"April\\\", \\\"sent_id\\\": 10, \\\"offset\\\": [1, 2], \\\"id\\\": \\\"bc99d7c6056ff0992f2534d2ff058c96\\\"}, {\\\"trigger_word\\\": \\\"South\\\", \\\"sent_id\\\": 10, \\\"offset\\\": [4, 5], \\\"id\\\": \\\"624327af9d642baecdb084b35cf4edf9\\\"}, {\\\"trigger_word\\\": \\\"Vietnam\\\", \\\"sent_id\\\": 10, \\\"offset\\\": [5, 6], \\\"id\\\": \\\"8af9301944de00f0e48b134db363b50f\\\"}, {\\\"trigger_word\\\": \\\"lost\\\", \\\"sent_id\\\": 10, \\\"offset\\\": [7, 8], \\\"id\\\": \\\"f8f76889f76a2bc1c3bd7b62feae1204\\\"}, {\\\"trigger_word\\\": \\\"control\\\", \\\"sent_id\\\": 10, \\\"offset\\\": [8, 9], \\\"id\\\": \\\"c706e5f38e8d2650cfd01f600564e812\\\"}, {\\\"trigger_word\\\": \\\"northern\\\", \\\"sent_id\\\": 10, \\\"offset\\\": [11, 12], \\\"id\\\": \\\"55588fa7274223e018b61dcc98174d38\\\"}, {\\\"trigger_word\\\": \\\"provinces\\\", \\\"sent_id\\\": 10, \\\"offset\\\": [12, 13], \\\"id\\\": \\\"601e31a94ef5694b32d58e9e6a274098\\\"}, {\\\"trigger_word\\\": \\\"well\\\", \\\"sent_id\\\": 10, \\\"offset\\\": [15, 16], \\\"id\\\": \\\"db1df6813503dbb55e9803a2f89b47d6\\\"}, {\\\"trigger_word\\\": \\\"army\\\", \\\"sent_id\\\": 10, \\\"offset\\\": [18, 19], \\\"id\\\": \\\"e07c7f4d6914f93f33cb8b06857215d1\\\"}, {\\\"trigger_word\\\": \\\"corps\\\", \\\"sent_id\\\": 10, \\\"offset\\\": [19, 20], \\\"id\\\": \\\"fce08a87ac12ef89194e6372cbe9090c\\\"}]}\\n/root/schema-dag-extraction/data/maven/test.jsonl:487:{\\\"title\\\": \\\"ArtRave_ The Artpop Ball\\\", \\\"id\\\": \\\"d3a339c5567ef286d77d281e60de9d53\\\", \\\"content\\\": [{\\\"sentence\\\": \\\"ArtRave: The Artpop Ball (stylized as artRAVE: the ARTPOP ball) was the fourth headlining concert tour by American singer Lady Gaga.\\\", \\\"tokens\\\": [\\\"ArtRave\\\", \\\":\\\", \\\"The\\\", \\\"Artpop\\\", \\\"Ball\\\", \\\"(\\\", \\\"stylized\\\", \\\"as\\\", \\\"artRAVE\\\", \\\":\\\", \\\"the\\\", \\\"ARTPOP\\\", \\\"ball\\\", \\\")\\\", \\\"was\\\", \\\"the\\\", \\\"fourth\\\", \\\"headlining\\\", \\\"concert\\\", \\\"tour\\\", \\\"by\\\", \\\"American\\\", \\\"singer\\\", \\\"Lady\\\", \\\"Gaga\\\", \\\".\\\"]}, {\\\"sentence\\\": \\\"Supporting her third studio album \\\\\\\"Artpop\\\\\\\" (2013), the tour ran from May 4, 2014 to November 24, 2014.\\\", \\\"tokens\\\": [\\\"Supporting\\\", \\\"her\\\", \\\"third\\\", \\\"studio\\\", \\\"album\\\", \\\"``\\\", \\\"Artpop\\\", \\\"''\\\", \\\"(\\\", \\\"2013\\\", \\\")\\\", \\\",\\\", \\\"the\\\", \\\"tour\\\", \\\"ran\\\", \\\"from\\\", \\\"May\\\", \\\"4\\\", \\\",\\\", \\\"2014\\\", \\\"to\\\", \\\"November\\\", \\\"24\\\", \\\",\\\", \\\"2014\\\", \\\".\\\"]}, {\\\"sentence\\\": \\\"The tour dates included cities where Gaga had canceled shows of her previous Born This Way Ball tour after suffering a hip injury.\\\", \\\"tokens\\\": [\\\"the\\\", \\\"tour\\\", \\\"dates\\\", \\\"included\\\", \\\"cities\\\", \\\"where\\\", \\\"gaga\\\", \\\"had\\\", \\\"canceled\\\", \\\"shows\\\", \\\"of\\\", \\\"her\\\", \\\"previous\\\", \\\"born\\\", \\\"this\\\", \\\"way\\\", \\\"ball\\\", \\\"tour\\\", \\\"after\\\", \\\"suffering\\\", \\\"a\\\", \\\"hip\\\", \\\"injury\\\", \\\".\\\"]}, {\\\"sentence\\\": \\\"The ArtRave tour was preceded by a performance at the South by Southwest music festival, which drew controversy due to a segment where an artist vomited on Gaga, and a seven-day residency at the Roseland Ballroom in Manhattan, New York.\\\", \\\"tokens\\\": [\\\"The\\\", \\\"ArtRave\\\", \\\"tour\\\", \\\"was\\\", \\\"preceded\\\", \\\"by\\\", \\\"a\\\", \\\"performance\\\", \\\"at\\\", \\\"the\\\", \\\"South\\\", \\\"by\\\", \\\"Southwest\\\", \\\"music\\\", \\\"festival\\\", \\\",\\\", \\\"which\\\", \\\"drew\\\", \\\"controversy\\\", \\\"due\\\", \\\"to\\\", \\\"a\\\", \\\"segment\\\", \\\"where\\\", \\\"an\\\", \\\"artist\\\", \\\"vomited\\\", \\\"on\\\", \\\"Gaga\\\", \\\",\\\", \\\"and\\\", \\\"a\\\", \\\"seven-day\\\", \\\"residency\\\", \\\"at\\\", \\\"the\\\", \\\"Roseland\\\", \\\"Ballroom\\\", \\\"in\\\", \\\"Manhattan\\\", \\\",\\\", \\\"New\\\", \\\"York\\\", \\\".\\\"]}, {\\\"sentence\\\": \\\"ArtRave's concept and name are derived from the similarly named release party for \\\\\\\"Artpop\\\\\\\".\\\", \\\"tokens\\\": [\\\"ArtRave\\\", \\\"'s\\\", \\\"concept\\\", \\\"and\\\", \\\"name\\\", \\\"are\\\", \\\"derived\\\", \\\"from\\\", \\\"the\\\", \\\"similarly\\\", \\\"named\\\", \\\"release\\\", \\\"party\\\", \\\"for\\\", \\\"``\\\", \\\"Artpop\\\", \\\"''\\\", \\\".\\\"]}, {\\\"sentence\\\": \\\"The stage resembled a cave and consisted of two sections connected by catwalks made of translucent lucite, allowing the audience to move underneath the catwalks while still being able to watch the show.\\\", \\\"tokens\\\": [\\\"The\\\", \\\"stage\\\", \\\"resembled\\\", \\\"a\\\", \\\"cave\\\", \\\"and\\\", \\\"consisted\\\", \\\"of\\\", \\\"two\\\", \\\"sections\\\", \\\"connected\\\", \\\"by\\\", \\\"catwalks\\\", \\\"made\\\", \\\"of\\\", \\\"translucent\\\", \\\"lucite\\\", \\\",\\\", \\\"allowing\\\", \\\"the\\\", \\\"audience\\\", \\\"to\\\", \\\"move\\\", \\\"underneath\\\", \\\"the\\\", \\\"catwalks\\\", \\\"while\\\", \\\"still\\\", \\\"being\\\", \\\"able\\\", \\\"to\\\", \\\"watch\\\", \\\"the\\\", \\\"show\\\", \\\".\\\"]}, {\\\"sentence\\\": \\\"Gaga's costumes in the show included one with tentacles, one with bejeweled wings, a rave-inspired outfit and a necklace made of marijuana leaves.\\\", \\\"tokens\\\": [\\\"Gaga\\\", \\\"'s\\\", \\\"costumes\\\", \\\"in\\\", \\\"the\\\", \\\"show\\\", \\\"included\\\", \\\"one\\\", \\\"with\\\", \\\"tentacles\\\", \\\",\\\", \\\"one\\\", \\\"with\\\", \\\"bejeweled\\\", \\\"wings\\\", \\\",\\\", \\\"a\\\", \\\"rave-inspired\\\", \\\"outfit\\\", \\\"and\\\", \\\"a\\\", \\\"necklace\\\", \\\"made\\\", \\\"of\\\", \\\"marijuana\\\", \\\"leaves\\\", \\\".\\\"]}, {\\\"sentence\\\": \\\"Costume designers and choreographers aspired to make a single, coherent show.\\\", \\\"tokens\\\": [\\\"Costume\\\", \\\"designers\\\", \\\"and\\\", \\\"choreographers\\\", \\\"aspired\\\", \\\"to\\\", \\\"make\\\", \\\"a\\\", \\\"single\\\", \\\",\\\", \\\"coherent\\\", \\\"show\\\", \\\".\\\"]}, {\\\"sentence\\\": \\\"The lighting fixtures used for the concert were from Clay Paky and the main idea was to create an immersive rave experience with the lights.\\\", \\\"tokens\\\": [\\\"The\\\", \\\"lighting\\\", \\\"fixtures\\\", \\\"used\\\", \\\"for\\\", \\\"the\\\", \\\"concert\\\", \\\"were\\\", \\\"from\\\", \\\"Clay\\\", \\\"Paky\\\", \\\"and\\\", \\\"the\\\", \\\"main\\\", \\\"idea\\\", \\\"was\\\", \\\"to\\\", \\\"create\\\", \\\"an\\\", \\\"immersive\\\", \\\"rave\\\", \\\"experience\\\", \\\"with\\\", \\\"the\\\", \\\"lights\\\", \\\".\\\"]}, {\\\"sentence\\\": \\\"They were also designed to accommodate minor changes in the show sequences.\\\", \\\"tokens\\\": [\\\"They\\\", \\\"were\\\", \\\"also\\\", \\\"designed\\\", \\\"to\\\", \\\"accommodate\\\", \\\"minor\\\", \\\"changes\\\", \\\"in\\\", \\\"the\\\", \\\"show\\\", \\\"sequences\\\", \\\".\\\"]}, {\\\"sentence\\\": \\\"The tour was produced by Live Nation, and promoted by Absolut Vodka in the United States and O in the United Kingdom.\\\", \\\"tokens\\\": [\\\"The\\\", \\\"tour\\\", \\\"was\\\", \\\"produced\\\", \\\"by\\\", \\\"Live\\\", \\\"Nation\\\", \\\",\\\", \\\"and\\\", \\\"promoted\\\", \\\"by\\\", \\\"Absolut\\\", \\\"Vodka\\\", \\\"in\\\", \\\"the\\\", \\\"United\\\", \\\"States\\\", \\\"and\\\", \\\"O\\\", \\\"in\\\", \\\"the\\\", \\\"United\\\", \\\"Kingdom\\\", \\\".\\\"]}, {\\\"sentence\\\": \\\"Tickets for several shows sold out immediately once available, prompting additional dates.\\\", \\\"tokens\\\": [\\\"Tickets\\\", \\\"for\\\", \\\"several\\\", \\\"shows\\\", \\\"sold\\\", \\\"out\\\", \\\"immediately\\\", \\\"once\\\", \\\"available\\\", \\\",\\\", \\\"prompting\\\", \\\"additional\\\", \\\"dates\\\", \\\".\\\"]}, {\\\"sentence\\\": \\\"Negative reports about the tour's commercial performance were dismissed by Live Nation chairman Arthur Fogel.\\\", \\\"tokens\\\": [\\\"Negative\\\", \\\"reports\\\", \\\"about\\\", \\\"the\\\", \\\"tour\\\", \\\"'s\\\", \\\"commercial\\\", \\\"performance\\\", \\\"were\\\", \\\"dismissed\\\", \\\"by\\\", \\\"Live\\\", \\\"Nation\\\", \\\"chairman\\\", \\\"Arthur\\\", \\\"Fogel\\\", \\\".\\\"]}, {\\\"sentence\\\": \\\"Gaga repeatedly placed within the top-ten of the \\\\\\\"Billboard\\\\\\\" Boxscore lists for the 2014 tour grosses.\\\", \\\"tokens\\\": [\\\"Gaga\\\", \\\"repeatedly\\\", \\\"placed\\\", \\\"within\\\", \\\"the\\\", \\\"top-ten\\\", \\\"of\\\", \\\"the\\\", \\\"``\\\", \\\"Billboard\\\", \\\"''\\\", \\\"Boxscore\\\", \\\"lists\\\", \\\"for\\\", \\\"the\\\", \\\"2014\\\", \\\"tour\\\", \\\"grosses\\\", \\\".\\\"]}, {\\\"sentence\\\": \\\"At the end, ArtRave: The Artpop Ball grossed a total of $83 million from 920,088 sold tickets at the 74 reported performances.\\\", \\\"tokens\\\": [\\\"at\\\", \\\"the\\\", \\\"end\\\", \\\",\\\", \\\"unk\\\", \\\":\\\", \\\"the\\\", \\\"artpop\\\", \\\"ball\\\", \\\"grossed\\\", \\\"a\\\", \\\"total\\\", \\\"of\\\", \\\"$\\\", \\\"83\\\", \\\"million\\\", \\\"from\\\", \\\"unk\\\", \\\"sold\\\", \\\"tickets\\\", \\\"at\\\", \\\"the\\\", \\\"74\\\", \\\"reported\\\", \\\"performances\\\", \\\".\\\"]}, {\\\"sentence\\\": \\\"\\\\\\\"Billboard\\\\\\\" also listed it as the ninth best concert tour of the year with 76 reported shows.\\\", \\\"tokens\\\": [\\\"``\\\", \\\"Billboard\\\", \\\"''\\\", \\\"also\\\", \\\"listed\\\", \\\"it\\\", \\\"as\\\", \\\"the\\\", \\\"ninth\\\", \\\"best\\\", \\\"concert\\\", \\\"tour\\\", \\\"of\\\", \\\"the\\\", \\\"year\\\", \\\"with\\\", \\\"76\\\", \\\"reported\\\", \\\"shows\\\", \\\".\\\"]}, {\\\"sentence\\\": \\\"The tour additionally received positive response from reviewers, but some criticized it for being disjointed.\\\", \\\"tokens\\\": [\\\"The\\\", \\\"tour\\\", \\\"additionally\\\", \\\"received\\\", \\\"positive\\\", \\\"response\\\", \\\"from\\\", \\\"reviewers\\\", \\\",\\\", \\\"but\\\", \\\"some\\\", \\\"criticized\\\", \\\"it\\\", \\\"for\\\", \\\"being\\\", \\\"disjointed\\\", \\\".\\\"]}, {\\\"sentence\\\": \\\"On November 24, 2014, the concert was streamed live from Bercy Arena in France.\\\", \\\"tokens\\\": [\\\"On\\\", \\\"November\\\", \\\"24\\\", \\\",\\\", \\\"2014\\\", \\\",\\\", \\\"the\\\", \\\"concert\\\", \\\"was\\\", \\\"streamed\\\", \\\"live\\\", \\\"from\\\", \\\"Bercy\\\", \\\"Arena\\\", \\\"in\\\", \\\"France\\\", \\\".\\\"]}], \\\"candidates\\\": [{\\\"trigger_word\\\": \\\"ArtRave\\\", \\\"sent_id\\\": 0, \\\"offset\\\": [0, 1], \\\"id\\\": \\\"de82fb0b3d89a47893b4457c8e39ea9f\\\"}, {\\\"trigger_word\\\": \\\"Artpop\\\", \\\"sent_id\\\": 0, \\\"offset\\\": [3, 4], \\\"id\\\": \\\"1cbbc279b4096b92d9d030536a0b3901\\\"}, {\\\"trigger_word\\\": \\\"Ball\\\", \\\"sent_id\\\": 0, \\\"offset\\\": [4, 5], \\\"id\\\": \\\"467895887993a3f956bf268fc692a655\\\"}, {\\\"trigger_word\\\": \\\"stylized\\\", \\\"sent_id\\\": 0, \\\"offset\\\": [6, 7], \\\"id\\\": \\\"f94bce875a9397a37d1272a8f2c8c851\\\"}, {\\\"trigger_word\\\": \\\"artRAVE\\\", \\\"sent_id\\\": 0, \\\"offset\\\": [8, 9], \\\"id\\\": \\\"146c6b4aaf16a2aa0ccffe7272e8bf4a\\\"}, {\\\"trigger_word\\\": \\\"ARTPOP\\\", \\\"sent_id\\\": 0, \\\"offset\\\": [11, 12], \\\"id\\\": \\\"4ed246bc9ed05d60818ada27d65addaa\\\"}, {\\\"trigger_word\\\": \\\"ball\\\", \\\"sent_id\\\": 0, \\\"offset\\\": [12, 13], \\\"id\\\": \\\"2c424cb7ee7c96be5810285f69713c02\\\"}, {\\\"trigger_word\\\": \\\"fourth\\\", \\\"sent_id\\\": 0, \\\"offset\\\": [16, 17], \\\"id\\\": \\\"f885079dce1e48d91c77dd488c64c6a5\\\"}, {\\\"trigger_word\\\": \\\"headlining\\\", \\\"sent_id\\\": 0, \\\"offset\\\": [17, 18], \\\"id\\\": \\\"655edfb66b9b6ada99de3edb1b855d8d\\\"}, {\\\"trigger_word\\\": \\\"concert\\\", \\\"sent_id\\\": 0, \\\"offset\\\": [18, 19], \\\"id\\\": \\\"9ea5498c671d554436b0bca37bed8eda\\\"}, {\\\"trigger_word\\\": \\\"tour\\\", \\\"sent_id\\\": 0, \\\"offset\\\": [19, 20], \\\"id\\\": \\\"3645f925861e5a1159a1018ab9021cf9\\\"}, {\\\"trigger_word\\\": \\\"American\\\", \\\"sent_id\\\": 0, \\\"offset\\\": [21, 22], \\\"id\\\": \\\"28a7f62c50831acd5ed5ffc4ef6f67e5\\\"}, {\\\"trigger_word\\\": \\\"singer\\\", \\\"sent_id\\\": 0, \\\"offset\\\": [22, 23], \\\"id\\\": \\\"48572e3997a4d243bab0cc6efe6f48b5\\\"}, {\\\"trigger_word\\\": \\\"Lady\\\", \\\"sent_id\\\": 0, \\\"offset\\\": [23, 24], \\\"id\\\": \\\"bbc55c96871e67bd02e2728660a26a7f\\\"}, {\\\"trigger_word\\\": \\\"Gaga\\\", \\\"sent_id\\\": 0, \\\"offset\\\": [24, 25], \\\"id\\\": \\\"83ebbadf418a1619b72a5c58b0fdafd0\\\"}, {\\\"trigger_word\\\": \\\"Supporting\\\", \\\"sent_id\\\": 1, \\\"offset\\\": [0, 1], \\\"id\\\": \\\"ca099123e2afaec1dcef9bb45cd12d96\\\"}, {\\\"trigger_word\\\": \\\"third\\\", \\\"sent_id\\\": 1, \\\"offset\\\": [2, 3], \\\"id\\\": \\\"205b57118e432582bf9a95f4daea1c82\\\"}, {\\\"trigger_word\\\": \\\"studio\\\", \\\"sent_id\\\": 1, \\\"offset\\\": [3, 4], \\\"id\\\": \\\"ef46ecfcbb08b5d1ebcbbb1526465742\\\"}, {\\\"trigger_word\\\": \\\"Artpop\\\", \\\"sent_id\\\": 1, \\\"offset\\\": [6, 7], \\\"id\\\": \\\"42851c49804ca905a9a3fd7d4c98d169\\\"}, {\\\"trigger_word\\\": \\\"tour\\\", \\\"sent_id\\\": 1, \\\"offset\\\": [13, 14], \\\"id\\\": \\\"3d57f31edddfc21ee63f62a7a0d7f7e8\\\"}, {\\\"trigger_word\\\": \\\"ran\\\", \\\"sent_id\\\": 1, \\\"offset\\\": [14, 15], \\\"id\\\": \\\"c47ddf370284cf80e5ccd3dab2955c56\\\"}, {\\\"trigger_word\\\": \\\"May\\\", \\\"sent_id\\\": 1, \\\"offset\\\": [16, 17], \\\"id\\\": \\\"1de6df845a55650dbe5672e599c6eb62\\\"}, {\\\"trigger_word\\\": \\\"November\\\", \\\"sent_id\\\": 1, \\\"offset\\\": [21, 22], \\\"id\\\": \\\"f28c30deb3ae5358f4c7e3047daa6291\\\"}, {\\\"trigger_word\\\": \\\"tour\\\", \\\"sent_id\\\": 2, \\\"offset\\\": [1, 2], \\\"id\\\": \\\"cc26547e42546537fc190f49432ad60d\\\"}, {\\\"trigger_word\\\": \\\"dates\\\", \\\"sent_id\\\": 2, \\\"offset\\\": [2, 3], \\\"id\\\": \\\"6b3401e29a58971f6a24ed9635c705ff\\\"}, {\\\"trigger_word\\\": \\\"included\\\", \\\"sent_id\\\": 2, \\\"offset\\\": [3, 4], \\\"id\\\": \\\"65d2054e206ad2eb15ff6c9aa37f4e72\\\"}, {\\\"trigger_word\\\": \\\"cities\\\", \\\"sent_id\\\": 2, \\\"offset\\\": [4, 5], \\\"id\\\": \\\"4341234fea5fc4ac06921359d6e04b2a\\\"}, {\\\"trigger_word\\\": \\\"gaga\\\", \\\"sent_id\\\": 2, \\\"offset\\\": [6, 7], \\\"id\\\": \\\"918bac7ec6c714be38b06a5a5659507d\\\"}, {\\\"trigger_word\\\": \\\"canceled\\\", \\\"sent_id\\\": 2, \\\"offset\\\": [8, 9], \\\"id\\\": \\\"09493ac05eb1c5029d390c2072ae9dbc\\\"}, {\\\"trigger_word\\\": \\\"shows\\\", \\\"sent_id\\\": 2, \\\"offset\\\": [9, 10], \\\"id\\\": \\\"5176b98d87e39b3fc6d97a36b1a44fe6\\\"}, {\\\"trigger_word\\\": \\\"previous\\\", \\\"sent_id\\\": 2, \\\"offset\\\": [12, 13], \\\"id\\\": \\\"a47b7cca2a60f26755537b1f376db3c7\\\"}, {\\\"trigger_word\\\": \\\"born\\\", \\\"sent_id\\\": 2, \\\"offset\\\": [13, 14], \\\"id\\\": \\\"cc689b5407c25208b62fa37c7533901e\\\"}, {\\\"trigger_word\\\": \\\"way\\\", \\\"sent_id\\\": 2, \\\"offset\\\": [15, 16], \\\"id\\\": \\\"38e6f3817690a0c0e1ce166f000bcb37\\\"}, {\\\"trigger_word\\\": \\\"ball\\\", \\\"sent_id\\\": 2, \\\"offset\\\": [16, 17], \\\"id\\\": \\\"ddfab052f445febcc8007498a7e890f7\\\"}, {\\\"trigger_word\\\": \\\"tour\\\", \\\"sent_id\\\": 2, \\\"offset\\\": [17, 18], \\\"id\\\": \\\"351bc0f6040575e43ca9eccf5208027c\\\"}, {\\\"trigger_word\\\": \\\"suffering\\\", \\\"sent_id\\\": 2, \\\"offset\\\": [19, 20], \\\"id\\\": \\\"5584966987250f35919d9809c4f506ac\\\"}, {\\\"trigger_word\\\": \\\"hip\\\", \\\"sent_id\\\": 2, \\\"offset\\\": [21, 22], \\\"id\\\": \\\"ee06cc709ae9dfd12c8f3854fbfa3ce1\\\"}, {\\\"trigger_word\\\": \\\"injury\\\", \\\"sent_id\\\": 2, \\\"offset\\\": [22, 23], \\\"id\\\": \\\"38d44146509d6042628f11dd14644ef6\\\"}, {\\\"trigger_word\\\": \\\"ArtRave\\\", \\\"sent_id\\\": 3, \\\"offset\\\": [1, 2], \\\"id\\\": \\\"66b2f78d9bba86719dd52b9d9924aff8\\\"}, {\\\"trigger_word\\\": \\\"tour\\\", \\\"sent_id\\\": 3, \\\"offset\\\": [2, 3], \\\"id\\\": \\\"bb1d084a35e26d0d058f360d7a0e9bfe\\\"}, {\\\"trigger_word\\\": \\\"preceded\\\", \\\"sent_id\\\": 3, \\\"offset\\\": [4, 5], \\\"id\\\": \\\"adc26a0809f385191f31b30c1578f501\\\"}, {\\\"trigger_word\\\": \\\"performance\\\", \\\"sent_id\\\": 3, \\\"offset\\\": [7, 8], \\\"id\\\": \\\"c95023f35d45a761812e959d6cd57f1c\\\"}, {\\\"trigger_word\\\": \\\"South\\\", \\\"sent_id\\\": 3, \\\"offset\\\": [10, 11], \\\"id\\\": \\\"d9de8360ea13d02ebf2f896e60bdc69e\\\"}, {\\\"trigger_word\\\": \\\"Southwest\\\", \\\"sent_id\\\": 3, \\\"offset\\\": [12, 13], \\\"id\\\": \\\"a34e368ed7ef3a15cf1c73c189855df0\\\"}, {\\\"trigger_word\\\": \\\"music\\\", \\\"sent_id\\\": 3, \\\"offset\\\": [13, 14], \\\"id\\\": \\\"794c7743ca9603daa488ea4c6a4dba2b\\\"}, {\\\"trigger_word\\\": \\\"festival\\\", \\\"sent_id\\\": 3, \\\"offset\\\": [14, 15], \\\"id\\\": \\\"af587899aa649a4f0f059cfd304d1e11\\\"}, {\\\"trigger_word\\\": \\\"drew\\\", \\\"sent_id\\\": 3, \\\"offset\\\": [17, 18], \\\"id\\\": \\\"12fdcf584ea1443046e902af21fff14d\\\"}, {\\\"trigger_word\\\": \\\"controversy\\\", \\\"sent_id\\\": 3, \\\"offset\\\": [18, 19], \\\"id\\\": \\\"e9f149649e47fa20ba19b1ec6ea3b163\\\"}, {\\\"trigger_word\\\": \\\"due\\\", \\\"sent_id\\\": 3, \\\"offset\\\": [19, 20], \\\"id\\\": \\\"2b85587a149fc462a23db7c1eafb73ee\\\"}, {\\\"trigger_word\\\": \\\"segment\\\", \\\"sent_id\\\": 3, \\\"offset\\\": [22, 23], \\\"id\\\": \\\"1303f28ee16a766b2f9ff344dfa25eb7\\\"}, {\\\"trigger_word\\\": \\\"artist\\\", \\\"sent_id\\\": 3, \\\"offset\\\": [25, 26], \\\"id\\\": \\\"5cb897d95af713337f53bce79f1461cc\\\"}, {\\\"trigger_word\\\": \\\"vomited\\\", \\\"sent_id\\\": 3, \\\"offset\\\": [26, 27], \\\"id\\\": \\\"cd028823f5b56b99efca770e75b81c11\\\"}, {\\\"trigger_word\\\": \\\"Gaga\\\", \\\"sent_id\\\": 3, \\\"offset\\\": [28, 29], \\\"id\\\": \\\"11fec42120fa97e9cc826eecbb558a95\\\"}, {\\\"trigger_word\\\": \\\"seven-day\\\", \\\"sent_id\\\": 3, \\\"offset\\\": [32, 33], \\\"id\\\": \\\"044ccf53769947cb6a3299685288ebc3\\\"}, {\\\"trigger_word\\\": \\\"residency\\\", \\\"sent_id\\\": 3, \\\"offset\\\": [33, 34], \\\"id\\\": \\\"09b068d6ecbc74b79f86cb070ccb93b4\\\"}, {\\\"trigger_word\\\": \\\"Roseland\\\", \\\"sent_id\\\": 3, \\\"offset\\\": [36, 37], \\\"id\\\": \\\"e01c5ecaf0c3258182408cd51e6de8a7\\\"}, {\\\"trigger_word\\\": \\\"Ballroom\\\", \\\"sent_id\\\": 3, \\\"offset\\\": [37, 38], \\\"id\\\": \\\"e7145951de4842c651049705db0ca73f\\\"}, {\\\"trigger_word\\\": \\\"Manhattan\\\", \\\"sent_id\\\": 3, \\\"offset\\\": [39, 40], \\\"id\\\": \\\"ef95a16dd7ea3ae80334515be2c06d65\\\"}, {\\\"trigger_word\\\": \\\"New\\\", \\\"sent_id\\\": 3, \\\"offset\\\": [41, 42], \\\"id\\\": \\\"3605494b7c833f09d6492d82889d1e86\\\"}, {\\\"trigger_word\\\": \\\"York\\\", \\\"sent_id\\\": 3, \\\"offset\\\": [42, 43], \\\"id\\\": \\\"ae0e60dd2905ac6df605002ae86db5d3\\\"}, {\\\"trigger_word\\\": \\\"ArtRave\\\", \\\"sent_id\\\": 4, \\\"offset\\\": [0, 1], \\\"id\\\": \\\"82c46e922ade8445172fc3fa01fc9bb2\\\"}, {\\\"trigger_word\\\": \\\"concept\\\", \\\"sent_id\\\": 4, \\\"offset\\\": [2, 3], \\\"id\\\": \\\"697bc019587750b3b164823a05dc1080\\\"}, {\\\"trigger_word\\\": \\\"name\\\", \\\"sent_id\\\": 4, \\\"offset\\\": [4, 5], \\\"id\\\": \\\"e8990580711a5f1cc26b139346ded756\\\"}, {\\\"trigger_word\\\": \\\"similarly\\\", \\\"sent_id\\\": 4, \\\"offset\\\": [9, 10], \\\"id\\\": \\\"13d2fc5f0eecb0a9a3e8eca23a78c695\\\"}, {\\\"trigger_word\\\": \\\"named\\\", \\\"sent_id\\\": 4, \\\"offset\\\": [10, 11], \\\"id\\\": \\\"9c5fb35ac4a386e255731ee35ceb317c\\\"}, {\\\"trigger_word\\\": \\\"release\\\", \\\"sent_id\\\": 4, \\\"offset\\\": [11, 12], \\\"id\\\": \\\"8220e060ffa4e99fb70d44386b5faaa5\\\"}, {\\\"trigger_word\\\": \\\"party\\\", \\\"sent_id\\\": 4, \\\"offset\\\": [12, 13], \\\"id\\\": \\\"3a16eac70f90ee80d65aa42a79ed8469\\\"}, {\\\"trigger_word\\\": \\\"Artpop\\\", \\\"sent_id\\\": 4, \\\"offset\\\": [15, 16], \\\"id\\\": \\\"b9d956ed5326f8dfb853cc34d112b011\\\"}, {\\\"trigger_word\\\": \\\"stage\\\", \\\"sent_id\\\": 5, \\\"offset\\\": [1, 2], \\\"id\\\": \\\"2003b3534c4f58f33104c3fbb9fb7f24\\\"}, {\\\"trigger_word\\\": \\\"resembled\\\", \\\"sent_id\\\": 5, \\\"offset\\\": [2, 3], \\\"id\\\": \\\"15862f2f311fecbf71c8eb3a07dbba85\\\"}, {\\\"trigger_word\\\": \\\"cave\\\", \\\"sent_id\\\": 5, \\\"offset\\\": [4, 5], \\\"id\\\": \\\"16655a3237ba248afc6c8f6a4ff5b11d\\\"}, {\\\"trigger_word\\\": \\\"consisted\\\", \\\"sent_id\\\": 5, \\\"offset\\\": [6, 7], \\\"id\\\": \\\"848b5a3275d0bdb0e92d4d90a88d15f4\\\"}, {\\\"trigger_word\\\": \\\"sections\\\", \\\"sent_id\\\": 5, \\\"offset\\\": [9, 10], \\\"id\\\": \\\"e15a840b6ada274ead47fe9441feb653\\\"}, {\\\"trigger_word\\\": \\\"connected\\\", \\\"sent_id\\\": 5, \\\"offset\\\": [10, 11], \\\"id\\\": \\\"d535de87178b517f509837bde65f44c5\\\"}, {\\\"trigger_word\\\": \\\"catwalks\\\", \\\"sent_id\\\": 5, \\\"offset\\\": [12, 13], \\\"id\\\": \\\"47b1c7c9e8933db668eed62718e72e32\\\"}, {\\\"trigger_word\\\": \\\"made\\\", \\\"sent_id\\\": 5, \\\"offset\\\": [13, 14], \\\"id\\\": \\\"78216f807d37c46c27b4d6a56d34b69c\\\"}, {\\\"trigger_word\\\": \\\"translucent\\\", \\\"sent_id\\\": 5, \\\"offset\\\": [15, 16], \\\"id\\\": \\\"47a644ebf9611c26bc3b7ca5e75fc2ec\\\"}, {\\\"trigger_word\\\": \\\"lucite\\\", \\\"sent_id\\\": 5, \\\"offset\\\": [16, 17], \\\"id\\\": \\\"f90d41ee3cb95f74cbe1facc810aaa3b\\\"}, {\\\"trigger_word\\\": \\\"allowing\\\", \\\"sent_id\\\": 5, \\\"offset\\\": [18, 19], \\\"id\\\": \\\"2f5ec5c55f43faace3070284c5622bfb\\\"}, {\\\"trigger_word\\\": \\\"audience\\\", \\\"sent_id\\\": 5, \\\"offset\\\": [20, 21], \\\"id\\\": \\\"d588c324fca3a2e12ad88e80cfedb8cd\\\"}, {\\\"trigger_word\\\": \\\"move\\\", \\\"sent_id\\\": 5, \\\"offset\\\": [22, 23], \\\"id\\\": \\\"77fe41b7b52800dc163aa7188ef5a389\\\"}, {\\\"trigger_word\\\": \\\"catwalks\\\", \\\"sent_id\\\": 5, \\\"offset\\\": [25, 26], \\\"id\\\": \\\"a6dd530aa6fde2f8b784e7c4465f6cdb\\\"}, {\\\"trigger_word\\\": \\\"still\\\", \\\"sent_id\\\": 5, \\\"offset\\\": [27, 28], \\\"id\\\": \\\"4a697581a447f2928abe5303cd989253\\\"}, {\\\"trigger_word\\\": \\\"able\\\", \\\"sent_id\\\": 5, \\\"offset\\\": [29, 30], \\\"id\\\": \\\"c3ba9fa694ce066cc9033c66441cbfef\\\"}, {\\\"trigger_word\\\": \\\"watch\\\", \\\"sent_id\\\": 5, \\\"offset\\\": [31, 32], \\\"id\\\": \\\"7b3253eca3c04f81c5b2417d4d661986\\\"}, {\\\"trigger_word\\\": \\\"show\\\", \\\"sent_id\\\": 5, \\\"offset\\\": [33, 34], \\\"id\\\": \\\"261affc1b8cd812cc252776074714089\\\"}, {\\\"trigger_word\\\": \\\"Gaga\\\", \\\"sent_id\\\": 6, \\\"offset\\\": [0, 1], \\\"id\\\": \\\"96be8ab4774c65a7176b14e573068759\\\"}, {\\\"trigger_word\\\": \\\"costumes\\\", \\\"sent_id\\\": 6, \\\"offset\\\": [2, 3], \\\"id\\\": \\\"eacec6224694a129449f19ea02f42141\\\"}, {\\\"trigger_word\\\": \\\"show\\\", \\\"sent_id\\\": 6, \\\"offset\\\": [5, 6], \\\"id\\\": \\\"aeb82c4f2314b33bf84bed40d50496fc\\\"}, {\\\"trigger_word\\\": \\\"included\\\", \\\"sent_id\\\": 6, \\\"offset\\\": [6, 7], \\\"id\\\": \\\"e605d35dec492d6702820161b96c6ac8\\\"}, {\\\"trigger_word\\\": \\\"tentacles\\\", \\\"sent_id\\\": 6, \\\"offset\\\": [9, 10], \\\"id\\\": \\\"03922551861b558f332326ae76ecd4d6\\\"}, {\\\"trigger_word\\\": \\\"bejeweled\\\", \\\"sent_id\\\": 6, \\\"offset\\\": [13, 14], \\\"id\\\": \\\"dfa4787eab4afda0e572bf616e3cd136\\\"}, {\\\"trigger_word\\\": \\\"wings\\\", \\\"sent_id\\\": 6, \\\"offset\\\": [14, 15], \\\"id\\\": \\\"e3d45fea33bae185d862fe45a57e98a5\\\"}, {\\\"trigger_word\\\": \\\"rave-inspired\\\", \\\"sent_id\\\": 6, \\\"offset\\\": [17, 18], \\\"id\\\": \\\"4d04c5f16116c390ac1af8e1aed67f24\\\"}, {\\\"trigger_word\\\": \\\"outfit\\\", \\\"sent_id\\\": 6, \\\"offset\\\": [18, 19], \\\"id\\\": \\\"5f21646cb05de9f91191c709ee83a889\\\"}, {\\\"trigger_word\\\": \\\"necklace\\\", \\\"sent_id\\\": 6, \\\"offset\\\": [21, 22], \\\"id\\\": \\\"ddbd4a106fa7053ea0e7043960fe804a\\\"}, {\\\"trigger_word\\\": \\\"made\\\", \\\"sent_id\\\": 6, \\\"offset\\\": [22, 23], \\\"id\\\": \\\"9c301fa13c840fbf74f7ec7eed988aba\\\"}, {\\\"trigger_word\\\": \\\"marijuana\\\", \\\"sent_id\\\": 6, \\\"offset\\\": [24, 25], \\\"id\\\": \\\"ce205c1ad65aa38209173fc5e0cbda85\\\"}, {\\\"trigger_word\\\": \\\"leaves\\\", \\\"sent_id\\\": 6, \\\"offset\\\": [25, 26], \\\"id\\\": \\\"5911204ba662876bc346c2c3befa3f06\\\"}, {\\\"trigger_word\\\": \\\"Costume\\\", \\\"sent_id\\\": 7, \\\"offset\\\": [0, 1], \\\"id\\\": \\\"dcacdacc0e5d992774124f0795fbd9a4\\\"}, {\\\"trigger_word\\\": \\\"designers\\\", \\\"sent_id\\\": 7, \\\"offset\\\": [1, 2], \\\"id\\\": \\\"fe841d4a1e1e4485dd67a2a852c5170c\\\"}, {\\\"trigger_word\\\": \\\"choreographers\\\", \\\"sent_id\\\": 7, \\\"offset\\\": [3, 4], \\\"id\\\": \\\"d19fab5875ef6b53556ed34ef38115f2\\\"}, {\\\"trigger_word\\\": \\\"make\\\", \\\"sent_id\\\": 7, \\\"offset\\\": [6, 7], \\\"id\\\": \\\"fde1aabad29cde3bb720bf62abd76c52\\\"}, {\\\"trigger_word\\\": \\\"single\\\", \\\"sent_id\\\": 7, \\\"offset\\\": [8, 9], \\\"id\\\": \\\"b18259c93aa0230d220a65694b6dd5c1\\\"}, {\\\"trigger_word\\\": \\\"coherent\\\", \\\"sent_id\\\": 7, \\\"offset\\\": [10, 11], \\\"id\\\": \\\"5664b57ba4c4e99db800f9285c008970\\\"}, {\\\"trigger_word\\\": \\\"show\\\", \\\"sent_id\\\": 7, \\\"offset\\\": [11, 12], \\\"id\\\": \\\"3a7636199a4a3c675c6c11b70c131c0b\\\"}, {\\\"trigger_word\\\": \\\"lighting\\\", \\\"sent_id\\\": 8, \\\"offset\\\": [1, 2], \\\"id\\\": \\\"31e37cb39e579bf66c80b5f04d401759\\\"}, {\\\"trigger_word\\\": \\\"fixtures\\\", \\\"sent_id\\\": 8, \\\"offset\\\": [2, 3], \\\"id\\\": \\\"ae53c7d03821cb167901205eda9762d9\\\"}, {\\\"trigger_word\\\": \\\"used\\\", \\\"sent_id\\\": 8, \\\"offset\\\": [3, 4], \\\"id\\\": \\\"71fb725e9042ab3b7d3626364b47849d\\\"}, {\\\"trigger_word\\\": \\\"concert\\\", \\\"sent_id\\\": 8, \\\"offset\\\": [6, 7], \\\"id\\\": \\\"20e007ba2d7d5766779af978b9b41206\\\"}, {\\\"trigger_word\\\": \\\"Clay\\\", \\\"sent_id\\\": 8, \\\"offset\\\": [9, 10], \\\"id\\\": \\\"d8b90c23a1eb9727b447367db1c9e0a6\\\"}, {\\\"trigger_word\\\": \\\"Paky\\\", \\\"sent_id\\\": 8, \\\"offset\\\": [10, 11], \\\"id\\\": \\\"16e29932ea16d90d26163e1c26fd1203\\\"}, {\\\"trigger_word\\\": \\\"main\\\", \\\"sent_id\\\": 8, \\\"offset\\\": [13, 14], \\\"id\\\": \\\"fdf4f43eff879eac495de326692924cf\\\"}, {\\\"trigger_word\\\": \\\"idea\\\", \\\"sent_id\\\": 8, \\\"offset\\\": [14, 15], \\\"id\\\": \\\"ebc7d83c009f7e0ff2e294a474b5d862\\\"}, {\\\"trigger_word\\\": \\\"create\\\", \\\"sent_id\\\": 8, \\\"offset\\\": [17, 18], \\\"id\\\": \\\"611c26660457b1ff6c30999ce0a102fe\\\"}, {\\\"trigger_word\\\": \\\"immersive\\\", \\\"sent_id\\\": 8, \\\"offset\\\": [19, 20], \\\"id\\\": \\\"b584aef1c85cda8be9e018bc75ca9abe\\\"}, {\\\"trigger_word\\\": \\\"rave\\\", \\\"sent_id\\\": 8, \\\"offset\\\": [20, 21], \\\"id\\\": \\\"45ee64fd76419428789a894124d13f10\\\"}, {\\\"trigger_word\\\": \\\"experience\\\", \\\"sent_id\\\": 8, \\\"offset\\\": [21, 22], \\\"id\\\": \\\"94f51c1289f219b819953de3f5126604\\\"}, {\\\"trigger_word\\\": \\\"lights\\\", \\\"sent_id\\\": 8, \\\"offset\\\": [24, 25], \\\"id\\\": \\\"6cd5af18f4074548d180fa150f7110ce\\\"}, {\\\"trigger_word\\\": \\\"also\\\", \\\"sent_id\\\": 9, \\\"offset\\\": [2, 3], \\\"id\\\": \\\"89a357179c20350fc97d3d6c46bc90b8\\\"}, {\\\"trigger_word\\\": \\\"designed\\\", \\\"sent_id\\\": 9, \\\"offset\\\": [3, 4], \\\"id\\\": \\\"48fd4f7ae2db17a29a6af54290b052a7\\\"}, {\\\"trigger_word\\\": \\\"accommodate\\\", \\\"sent_id\\\": 9, \\\"offset\\\": [5, 6], \\\"id\\\": \\\"eb8d6a92aa22660cb5cfab0b0d03183b\\\"}, {\\\"trigger_word\\\": \\\"minor\\\", \\\"sent_id\\\": 9, \\\"offset\\\": [6, 7], \\\"id\\\": \\\"38d716a310b83c9a29f3c5c671f5a6a7\\\"}, {\\\"trigger_word\\\": \\\"changes\\\", \\\"sent_id\\\": 9, \\\"offset\\\": [7, 8], \\\"id\\\": \\\"399e4841626ad25f723e8e641df910bc\\\"}, {\\\"trigger_word\\\": \\\"show\\\", \\\"sent_id\\\": 9, \\\"offset\\\": [10, 11], \\\"id\\\": \\\"9e3225e0c42c89c714618adb830377dd\\\"}, {\\\"trigger_word\\\": \\\"sequences\\\", \\\"sent_id\\\": 9, \\\"offset\\\": [11, 12], \\\"id\\\": \\\"8c2c45b675e65add6f78774047a47c60\\\"}, {\\\"trigger_word\\\": \\\"tour\\\", \\\"sent_id\\\": 10, \\\"offset\\\": [1, 2], \\\"id\\\": \\\"549182fbeeae41be0512aed2a709fa18\\\"}, {\\\"trigger_word\\\": \\\"produced\\\", \\\"sent_id\\\": 10, \\\"offset\\\": [3, 4], \\\"id\\\": \\\"fb09fefec331e096e51134c1cd406df3\\\"}, {\\\"trigger_word\\\": \\\"Live\\\", \\\"sent_id\\\": 10, \\\"offset\\\": [5, 6], \\\"id\\\": \\\"9a463dae1eb672606cf33f3fd11b3b55\\\"}, {\\\"trigger_word\\\": \\\"Nation\\\", \\\"sent_id\\\": 10, \\\"offset\\\": [6, 7], \\\"id\\\": \\\"05fd82d13f24f39f98fa082adb22c984\\\"}, {\\\"trigger_word\\\": \\\"promoted\\\", \\\"sent_id\\\": 10, \\\"offset\\\": [9, 10], \\\"id\\\": \\\"4ab11e62a8b8d9c388aef7b5f354abdb\\\"}, {\\\"trigger_word\\\": \\\"Absolut\\\", \\\"sent_id\\\": 10, \\\"offset\\\": [11, 12], \\\"id\\\": \\\"90f807d37c4ff314b720c5167727adcf\\\"}, {\\\"trigger_word\\\": \\\"Vodka\\\", \\\"sent_id\\\": 10, \\\"offset\\\": [12, 13], \\\"id\\\": \\\"0f7255e6cecd6efec7bfe45bd8e22170\\\"}, {\\\"trigger_word\\\": \\\"United\\\", \\\"sent_id\\\": 10, \\\"offset\\\": [15, 16], \\\"id\\\": \\\"6a49ff6ca65ef79dcb5a2b02c862c98b\\\"}, {\\\"trigger_word\\\": \\\"States\\\", \\\"sent_id\\\": 10, \\\"offset\\\": [16, 17], \\\"id\\\": \\\"163f80eee6aa20c8680ce29dc750bcff\\\"}, {\\\"trigger_word\\\": \\\"O\\\", \\\"sent_id\\\": 10, \\\"offset\\\": [18, 19], \\\"id\\\": \\\"21efd8fc91d97a6e9b43cfcde827a541\\\"}, {\\\"trigger_word\\\": \\\"United\\\", \\\"sent_id\\\": 10, \\\"offset\\\": [21, 22], \\\"id\\\": \\\"7add67f696d5fe2b0cd25fa0534454a2\\\"}, {\\\"trigger_word\\\": \\\"Kingdom\\\", \\\"sent_id\\\": 10, \\\"offset\\\": [22, 23], \\\"id\\\": \\\"7431468137d08efe336d079753d16dcb\\\"}, {\\\"trigger_word\\\": \\\"Tickets\\\", \\\"sent_id\\\": 11, \\\"offset\\\": [0, 1], \\\"id\\\": \\\"20c92a55be8cb3d99594212c55f899a6\\\"}, {\\\"trigger_word\\\": \\\"several\\\", \\\"sent_id\\\": 11, \\\"offset\\\": [2, 3], \\\"id\\\": \\\"ed010ef337b469fff5932621813988d9\\\"}, {\\\"trigger_word\\\": \\\"shows\\\", \\\"sent_id\\\": 11, \\\"offset\\\": [3, 4], \\\"id\\\": \\\"d79cf1bd09edba670d540a617d83e0fe\\\"}, {\\\"trigger_word\\\": \\\"sold\\\", \\\"sent_id\\\": 11, \\\"offset\\\": [4, 5], \\\"id\\\": \\\"7b297e74e7848e66b799c57e9c190176\\\"}, {\\\"trigger_word\\\": \\\"immediately\\\", \\\"sent_id\\\": 11, \\\"offset\\\": [6, 7], \\\"id\\\": \\\"635ed1e20535f2ef5caac24ca8dbe2df\\\"}, {\\\"trigger_word\\\": \\\"available\\\", \\\"sent_id\\\": 11, \\\"offset\\\": [8, 9], \\\"id\\\": \\\"eda79d24aa7ea3a7365381241c71202f\\\"}, {\\\"trigger_word\\\": \\\"prompting\\\", \\\"sent_id\\\": 11, \\\"offset\\\": [10, 11], \\\"id\\\": \\\"a26f292dbf08c42b2d404fe7088fbab3\\\"}, {\\\"trigger_word\\\": \\\"additional\\\", \\\"sent_id\\\": 11, \\\"offset\\\": [11, 12], \\\"id\\\": \\\"13a1acc18213ce07d5e759998c56540d\\\"}, {\\\"trigger_word\\\": \\\"dates\\\", \\\"sent_id\\\": 11, \\\"offset\\\": [12, 13], \\\"id\\\": \\\"eae9deb0217850147089c92db3a5171d\\\"}, {\\\"trigger_word\\\": \\\"Negative\\\", \\\"sent_id\\\": 12, \\\"offset\\\": [0, 1], \\\"id\\\": \\\"d9c41b12871d4f175279ef70a4d15221\\\"}, {\\\"trigger_word\\\": \\\"reports\\\", \\\"sent_id\\\": 12, \\\"offset\\\": [1, 2], \\\"id\\\": \\\"79b32d0234de4da179cd2923c608eb34\\\"}, {\\\"trigger_word\\\": \\\"tour\\\", \\\"sent_id\\\": 12, \\\"offset\\\": [4, 5], \\\"id\\\": \\\"78a11507ccee56692ecce3966f9c7094\\\"}, {\\\"trigger_word\\\": \\\"commercial\\\", \\\"sent_id\\\": 12, \\\"offset\\\": [6, 7], \\\"id\\\": \\\"c311811a5ceda66bd3db01f20d65632c\\\"}, {\\\"trigger_word\\\": \\\"performance\\\", \\\"sent_id\\\": 12, \\\"offset\\\": [7, 8], \\\"id\\\": \\\"220df1b5ca662f2feeab37acd25a070d\\\"}, {\\\"trigger_word\\\": \\\"Live\\\", \\\"sent_id\\\": 12, \\\"offset\\\": [11, 12], \\\"id\\\": \\\"bd34aa56e463db7b8ed371ce3f171cfc\\\"}, {\\\"trigger_word\\\": \\\"Nation\\\", \\\"sent_id\\\": 12, \\\"offset\\\": [12, 13], \\\"id\\\": \\\"490c1d986bd68cafae2a5d02e58a404d\\\"}, {\\\"trigger_word\\\": \\\"chairman\\\", \\\"sent_id\\\": 12, \\\"offset\\\": [13, 14], \\\"id\\\": \\\"6270c9c8bf973f9162c16fb604ef1492\\\"}, {\\\"trigger_word\\\": \\\"Arthur\\\", \\\"sent_id\\\": 12, \\\"offset\\\": [14, 15], \\\"id\\\": \\\"7de4ef29b99981e6fbe625f71ee2211b\\\"}, {\\\"trigger_word\\\": \\\"Fogel\\\", \\\"sent_id\\\": 12, \\\"offset\\\": [15, 16], \\\"id\\\": \\\"1102373a24b5ddf61089409c9f6d6fd6\\\"}, {\\\"trigger_word\\\": \\\"Gaga\\\", \\\"sent_id\\\": 13, \\\"offset\\\": [0, 1], \\\"id\\\": \\\"8567d08aa195fe6b2498f0e556ab8d1f\\\"}, {\\\"trigger_word\\\": \\\"repeatedly\\\", \\\"sent_id\\\": 13, \\\"offset\\\": [1, 2], \\\"id\\\": \\\"c6e279c501ab6adc3b658151fad2b98d\\\"}, {\\\"trigger_word\\\": \\\"placed\\\", \\\"sent_id\\\": 13, \\\"offset\\\": [2, 3], \\\"id\\\": \\\"a2f9fb5c40d2084f92a46a6cbd66ab92\\\"}, {\\\"trigger_word\\\": \\\"top-ten\\\", \\\"sent_id\\\": 13, \\\"offset\\\": [5, 6], \\\"id\\\": \\\"df64c4ef4d050a95fd371e30b19d2530\\\"}, {\\\"trigger_word\\\": \\\"Billboard\\\", \\\"sent_id\\\": 13, \\\"offset\\\": [9, 10], \\\"id\\\": \\\"9a97d5aa9fd705fe8011c2a84ef1658f\\\"}, {\\\"trigger_word\\\": \\\"Boxscore\\\", \\\"sent_id\\\": 13, \\\"offset\\\": [11, 12], \\\"id\\\": \\\"6cb105609f49f56673bfcdfe1f546360\\\"}, {\\\"trigger_word\\\": \\\"lists\\\", \\\"sent_id\\\": 13, \\\"offset\\\": [12, 13], \\\"id\\\": \\\"bbf3cf50e91cbb5b6e343b87d7f784b0\\\"}, {\\\"trigger_word\\\": \\\"tour\\\", \\\"sent_id\\\": 13, \\\"offset\\\": [16, 17], \\\"id\\\": \\\"9856c17111e54ff66399464cb033a374\\\"}, {\\\"trigger_word\\\": \\\"grosses\\\", \\\"sent_id\\\": 13, \\\"offset\\\": [17, 18], \\\"id\\\": \\\"a5b14df4016b632dddfaa4cd2a8e2887\\\"}, {\\\"trigger_word\\\": \\\"end\\\", \\\"sent_id\\\": 14, \\\"offset\\\": [2, 3], \\\"id\\\": \\\"b5d45241ebf3c2c420717010a514cd61\\\"}, {\\\"trigger_word\\\": \\\"unk\\\", \\\"sent_id\\\": 14, \\\"offset\\\": [4, 5], \\\"id\\\": \\\"f2793f1f9f5319c3710bb57bc26cc9af\\\"}, {\\\"trigger_word\\\": \\\"artpop\\\", \\\"sent_id\\\": 14, \\\"offset\\\": [7, 8], \\\"id\\\": \\\"8c4f4b2573792b7834a2b64758aa95d4\\\"}, {\\\"trigger_word\\\": \\\"ball\\\", \\\"sent_id\\\": 14, \\\"offset\\\": [8, 9], \\\"id\\\": \\\"c2784c2d5cc608a3ce268da218c190cc\\\"}, {\\\"trigger_word\\\": \\\"grossed\\\", \\\"sent_id\\\": 14, \\\"offset\\\": [9, 10], \\\"id\\\": \\\"b63a59e2ced3268fe1f769f7ad8ece43\\\"}, {\\\"trigger_word\\\": \\\"total\\\", \\\"sent_id\\\": 14, \\\"offset\\\": [11, 12], \\\"id\\\": \\\"ab48d1f36e10aff4a3c1621a97e52027\\\"}, {\\\"trigger_word\\\": \\\"unk\\\", \\\"sent_id\\\": 14, \\\"offset\\\": [17, 18], \\\"id\\\": \\\"4844fbe7c482c97ccf272da01cfa150a\\\"}, {\\\"trigger_word\\\": \\\"sold\\\", \\\"sent_id\\\": 14, \\\"offset\\\": [18, 19], \\\"id\\\": \\\"efeb3f8e136577d9843d1140ca268a9e\\\"}, {\\\"trigger_word\\\": \\\"tickets\\\", \\\"sent_id\\\": 14, \\\"offset\\\": [19, 20], \\\"id\\\": \\\"42eaced0846633b99869022f3c168478\\\"}, {\\\"trigger_word\\\": \\\"reported\\\", \\\"sent_id\\\": 14, \\\"offset\\\": [23, 24], \\\"id\\\": \\\"bfe27eda2a7e0d59dc90c3faf0a22181\\\"}, {\\\"trigger_word\\\": \\\"performances\\\", \\\"sent_id\\\": 14, \\\"offset\\\": [24, 25], \\\"id\\\": \\\"9cb212ee0b9f60e21ec50da85a7afebb\\\"}, {\\\"trigger_word\\\": \\\"Billboard\\\", \\\"sent_id\\\": 15, \\\"offset\\\": [1, 2], \\\"id\\\": \\\"f9ca1f83415def7ee152be4db868c9f4\\\"}, {\\\"trigger_word\\\": \\\"also\\\", \\\"sent_id\\\": 15, \\\"offset\\\": [3, 4], \\\"id\\\": \\\"8244f430bd24358cf14a34ebab74833b\\\"}, {\\\"trigger_word\\\": \\\"listed\\\", \\\"sent_id\\\": 15, \\\"offset\\\": [4, 5], \\\"id\\\": \\\"b19e65fe5d0ca6d769b6dca441cd2b71\\\"}, {\\\"trigger_word\\\": \\\"ninth\\\", \\\"sent_id\\\": 15, \\\"offset\\\": [8, 9], \\\"id\\\": \\\"541d1386cf6fdbc811561b36a83eb63d\\\"}, {\\\"trigger_word\\\": \\\"best\\\", \\\"sent_id\\\": 15, \\\"offset\\\": [9, 10], \\\"id\\\": \\\"cc1e1891371dadbb88840d738aab36c7\\\"}, {\\\"trigger_word\\\": \\\"concert\\\", \\\"sent_id\\\": 15, \\\"offset\\\": [10, 11], \\\"id\\\": \\\"fd5026550688daf42f53d8c9811060aa\\\"}, {\\\"trigger_word\\\": \\\"tour\\\", \\\"sent_id\\\": 15, \\\"offset\\\": [11, 12], \\\"id\\\": \\\"b8b0e9a850f64be0fac6a7aea2f9014f\\\"}, {\\\"trigger_word\\\": \\\"year\\\", \\\"sent_id\\\": 15, \\\"offset\\\": [14, 15], \\\"id\\\": \\\"ae0e9bc61db4f425f399d50509e8d3f2\\\"}, {\\\"trigger_word\\\": \\\"reported\\\", \\\"sent_id\\\": 15, \\\"offset\\\": [17, 18], \\\"id\\\": \\\"27c64be766bdb171edcb84a0bad8550d\\\"}, {\\\"trigger_word\\\": \\\"shows\\\", \\\"sent_id\\\": 15, \\\"offset\\\": [18, 19], \\\"id\\\": \\\"ebee51fb81d34ce42a52a24c5a1e9d53\\\"}, {\\\"trigger_word\\\": \\\"tour\\\", \\\"sent_id\\\": 16, \\\"offset\\\": [1, 2], \\\"id\\\": \\\"a37b988a256fd2579d499002299ae121\\\"}, {\\\"trigger_word\\\": \\\"additionally\\\", \\\"sent_id\\\": 16, \\\"offset\\\": [2, 3], \\\"id\\\": \\\"30e5514f26bacfd2d886f76b12a7f8c1\\\"}, {\\\"trigger_word\\\": \\\"received\\\", \\\"sent_id\\\": 16, \\\"offset\\\": [3, 4], \\\"id\\\": \\\"bb27dc24414d5c3171b3a23771c5c30b\\\"}, {\\\"trigger_word\\\": \\\"positive\\\", \\\"sent_id\\\": 16, \\\"offset\\\": [4, 5], \\\"id\\\": \\\"44aaba3e86f69ac3fa192184364d06c5\\\"}, {\\\"trigger_word\\\": \\\"response\\\", \\\"sent_id\\\": 16, \\\"offset\\\": [5, 6], \\\"id\\\": \\\"21f3baae726f7b76f275fd0e8a642c74\\\"}, {\\\"trigger_word\\\": \\\"reviewers\\\", \\\"sent_id\\\": 16, \\\"offset\\\": [7, 8], \\\"id\\\": \\\"6477327f4461d3e566c652c163ca14eb\\\"}, {\\\"trigger_word\\\": \\\"criticized\\\", \\\"sent_id\\\": 16, \\\"offset\\\": [11, 12], \\\"id\\\": \\\"d0c0bfb7704afcd590af10860f846729\\\"}, {\\\"trigger_word\\\": \\\"disjointed\\\", \\\"sent_id\\\": 16, \\\"offset\\\": [15, 16], \\\"id\\\": \\\"d41d4411f8c16fb96999e1b6d151fa6b\\\"}, {\\\"trigger_word\\\": \\\"November\\\", \\\"sent_id\\\": 17, \\\"offset\\\": [1, 2], \\\"id\\\": \\\"b6a480ee28160e63d0dd79fee0720e3e\\\"}, {\\\"trigger_word\\\": \\\"concert\\\", \\\"sent_id\\\": 17, \\\"offset\\\": [7, 8], \\\"id\\\": \\\"147a0a40e5d8d1088449cca95b2dcfad\\\"}, {\\\"trigger_word\\\": \\\"live\\\", \\\"sent_id\\\": 17, \\\"offset\\\": [10, 11], \\\"id\\\": \\\"34a4c2d22ba22ce9a132ed4107c894e1\\\"}, {\\\"trigger_word\\\": \\\"Bercy\\\", \\\"sent_id\\\": 17, \\\"offset\\\": [12, 13], \\\"id\\\": \\\"f6821f713cbd54110dcdd89d16c9629d\\\"}, {\\\"trigger_word\\\": \\\"Arena\\\", \\\"sent_id\\\": 17, \\\"offset\\\": [13, 14], \\\"id\\\": \\\"61c1ca2c2ae90f6f74fa54be1749e326\\\"}, {\\\"trigger_word\\\": \\\"France\\\", \\\"sent_id\\\": 17, \\\"offset\\\": [15, 16], \\\"id\\\": \\\"440251ff844b93b191f901d23a1a0c28\\\"}]}\\n/root/schema-dag-extraction/data/maven/test.jsonl:488:{\\\"title\\\": \\\"Rebel Heart Tour\\\", \\\"id\\\": \\\"f80622671404b8331c59d53ed4769274\\\", \\\"content\\\": [{\\\"sentence\\\": \\\"Rebel Heart Tour was the tenth concert tour by American singer Madonna, staged in support of her 13th studio album, \\\\\\\"Rebel Heart\\\\\\\" (2015).\\\", \\\"tokens\\\": [\\\"Rebel\\\", \\\"Heart\\\", \\\"Tour\\\", \\\"was\\\", \\\"the\\\", \\\"tenth\\\", \\\"concert\\\", \\\"tour\\\", \\\"by\\\", \\\"American\\\", \\\"singer\\\", \\\"Madonna\\\", \\\",\\\", \\\"staged\\\", \\\"in\\\", \\\"support\\\", \\\"of\\\", \\\"her\\\", \\\"13th\\\", \\\"studio\\\", \\\"album\\\", \\\",\\\", \\\"``\\\", \\\"Rebel\\\", \\\"Heart\\\", \\\"''\\\", \\\"(\\\", \\\"2015\\\", \\\")\\\", \\\".\\\"]}, {\\\"sentence\\\": \\\"Comprising 82 shows, the tour visited North America, Asia, Europe, and Oceania.\\\", \\\"tokens\\\": [\\\"Comprising\\\", \\\"82\\\", \\\"shows\\\", \\\",\\\", \\\"the\\\", \\\"tour\\\", \\\"visited\\\", \\\"North\\\", \\\"America\\\", \\\",\\\", \\\"Asia\\\", \\\",\\\", \\\"Europe\\\", \\\",\\\", \\\"and\\\", \\\"Oceania\\\", \\\".\\\"]}, {\\\"sentence\\\": \\\"It began on September 9, 2015, in Montreal, Canada, at the Bell Centre and concluded on March 20, 2016, in Sydney, Australia at Allphones Arena.\\\", \\\"tokens\\\": [\\\"It\\\", \\\"began\\\", \\\"on\\\", \\\"September\\\", \\\"9\\\", \\\",\\\", \\\"2015\\\", \\\",\\\", \\\"in\\\", \\\"Montreal\\\", \\\",\\\", \\\"Canada\\\", \\\",\\\", \\\"at\\\", \\\"the\\\", \\\"Bell\\\", \\\"Centre\\\", \\\"and\\\", \\\"concluded\\\", \\\"on\\\", \\\"March\\\", \\\"20\\\", \\\",\\\", \\\"2016\\\", \\\",\\\", \\\"in\\\", \\\"Sydney\\\", \\\",\\\", \\\"Australia\\\", \\\"at\\\", \\\"Allphones\\\", \\\"Arena\\\", \\\".\\\"]}, {\\\"sentence\\\": \\\"The tour was officially announced on March 1, 2015, through Madonna's website and was led by Live Nation Entertainment's Global Touring Division, helmed by Arthur Fogel; this was the fifth collaboration between Madonna and Live Nation as well as her third tour to be promoted by the company.\\\", \\\"tokens\\\": [\\\"The\\\", \\\"tour\\\", \\\"was\\\", \\\"officially\\\", \\\"announced\\\", \\\"on\\\", \\\"March\\\", \\\"1\\\", \\\",\\\", \\\"2015\\\", \\\",\\\", \\\"through\\\", \\\"Madonna\\\", \\\"'s\\\", \\\"website\\\", \\\"and\\\", \\\"was\\\", \\\"led\\\", \\\"by\\\", \\\"Live\\\", \\\"Nation\\\", \\\"Entertainment\\\", \\\"'s\\\", \\\"Global\\\", \\\"Touring\\\", \\\"Division\\\", \\\",\\\", \\\"helmed\\\", \\\"by\\\", \\\"Arthur\\\", \\\"Fogel\\\", \\\";\\\", \\\"this\\\", \\\"was\\\", \\\"the\\\", \\\"fifth\\\", \\\"collaboration\\\", \\\"between\\\", \\\"Madonna\\\", \\\"and\\\", \\\"Live\\\", \\\"Nation\\\", \\\"as\\\", \\\"well\\\", \\\"as\\\", \\\"her\\\", \\\"third\\\", \\\"tour\\\", \\\"to\\\", \\\"be\\\", \\\"promoted\\\", \\\"by\\\", \\\"the\\\", \\\"company\\\", \\\".\\\"]}, {\\\"sentence\\\": \\\"The all-arena Rebel Heart Tour also visited cities where the singer had not performed before, and was her first to visit Australia since The Girlie Show World Tour (1993).\\\", \\\"tokens\\\": [\\\"The\\\", \\\"all-arena\\\", \\\"Rebel\\\", \\\"Heart\\\", \\\"Tour\\\", \\\"also\\\", \\\"visited\\\", \\\"cities\\\", \\\"where\\\", \\\"the\\\", \\\"singer\\\", \\\"had\\\", \\\"not\\\", \\\"performed\\\", \\\"before\\\", \\\",\\\", \\\"and\\\", \\\"was\\\", \\\"her\\\", \\\"first\\\", \\\"to\\\", \\\"visit\\\", \\\"Australia\\\", \\\"since\\\", \\\"The\\\", \\\"Girlie\\\", \\\"Show\\\", \\\"World\\\", \\\"Tour\\\", \\\"(\\\", \\\"1993\\\", \\\")\\\", \\\".\\\"]}, {\\\"sentence\\\": \\\"Rehearsals for the tour commenced following its announcement and lasted 10–12 hours per day, with involvement from Madonna's team of creative directors, producers, designers and choreographers.\\\", \\\"tokens\\\": [\\\"Rehearsals\\\", \\\"for\\\", \\\"the\\\", \\\"tour\\\", \\\"commenced\\\", \\\"following\\\", \\\"its\\\", \\\"announcement\\\", \\\"and\\\", \\\"lasted\\\", \\\"10–12\\\", \\\"hours\\\", \\\"per\\\", \\\"day\\\", \\\",\\\", \\\"with\\\", \\\"involvement\\\", \\\"from\\\", \\\"Madonna\\\", \\\"'s\\\", \\\"team\\\", \\\"of\\\", \\\"creative\\\", \\\"directors\\\", \\\",\\\", \\\"producers\\\", \\\",\\\", \\\"designers\\\", \\\"and\\\", \\\"choreographers\\\", \\\".\\\"]}, {\\\"sentence\\\": \\\"It was inspired by shows like Cirque du Soleil and Chinese New Year, as well as the films \\\\\\\"300\\\\\\\" (2006) and \\\\\\\"Grease\\\\\\\" (1978).\\\", \\\"tokens\\\": [\\\"It\\\", \\\"was\\\", \\\"inspired\\\", \\\"by\\\", \\\"shows\\\", \\\"like\\\", \\\"Cirque\\\", \\\"du\\\", \\\"Soleil\\\", \\\"and\\\", \\\"Chinese\\\", \\\"New\\\", \\\"Year\\\", \\\",\\\", \\\"as\\\", \\\"well\\\", \\\"as\\\", \\\"the\\\", \\\"films\\\", \\\"``\\\", \\\"300\\\", \\\"''\\\", \\\"(\\\", \\\"2006\\\", \\\")\\\", \\\"and\\\", \\\"``\\\", \\\"Grease\\\", \\\"''\\\", \\\"(\\\", \\\"1978\\\", \\\")\\\", \\\".\\\"]}, {\\\"sentence\\\": \\\"Madonna enlisted Jamie King as the creative director, and Megan Lawson and Jason Yong as choreographers.\\\", \\\"tokens\\\": [\\\"Madonna\\\", \\\"enlisted\\\", \\\"Jamie\\\", \\\"King\\\", \\\"as\\\", \\\"the\\\", \\\"creative\\\", \\\"director\\\", \\\",\\\", \\\"and\\\", \\\"Megan\\\", \\\"Lawson\\\", \\\"and\\\", \\\"Jason\\\", \\\"Yong\\\", \\\"as\\\", \\\"choreographers\\\", \\\".\\\"]}, {\\\"sentence\\\": \\\"The tour featured costumes from Moschino, Prada, Miu Miu, Gucci and Swarovski jewelry, and an elevated stage with a runway and a heart-shaped front.\\\", \\\"tokens\\\": [\\\"The\\\", \\\"tour\\\", \\\"featured\\\", \\\"costumes\\\", \\\"from\\\", \\\"Moschino\\\", \\\",\\\", \\\"Prada\\\", \\\",\\\", \\\"Miu\\\", \\\"Miu\\\", \\\",\\\", \\\"Gucci\\\", \\\"and\\\", \\\"Swarovski\\\", \\\"jewelry\\\", \\\",\\\", \\\"and\\\", \\\"an\\\", \\\"elevated\\\", \\\"stage\\\", \\\"with\\\", \\\"a\\\", \\\"runway\\\", \\\"and\\\", \\\"a\\\", \\\"heart-shaped\\\", \\\"front\\\", \\\".\\\"]}, {\\\"sentence\\\": \\\"Multimedia was created by Moment Factory, while sound and light were produced by Clay Paky and DiGiCo, respectively.\\\", \\\"tokens\\\": [\\\"Multimedia\\\", \\\"was\\\", \\\"created\\\", \\\"by\\\", \\\"Moment\\\", \\\"Factory\\\", \\\",\\\", \\\"while\\\", \\\"sound\\\", \\\"and\\\", \\\"light\\\", \\\"were\\\", \\\"produced\\\", \\\"by\\\", \\\"Clay\\\", \\\"Paky\\\", \\\"and\\\", \\\"DiGiCo\\\", \\\",\\\", \\\"respectively\\\", \\\".\\\"]}, {\\\"sentence\\\": \\\"The central theme of the show was love and romance, and consisted of four segments, with each inspired by different topics.\\\", \\\"tokens\\\": [\\\"The\\\", \\\"central\\\", \\\"theme\\\", \\\"of\\\", \\\"the\\\", \\\"show\\\", \\\"was\\\", \\\"love\\\", \\\"and\\\", \\\"romance\\\", \\\",\\\", \\\"and\\\", \\\"consisted\\\", \\\"of\\\", \\\"four\\\", \\\"segments\\\", \\\",\\\", \\\"with\\\", \\\"each\\\", \\\"inspired\\\", \\\"by\\\", \\\"different\\\", \\\"topics\\\", \\\".\\\"]}, {\\\"sentence\\\": \\\"Inspirations varied from the cover artwork of \\\\\\\"Rebel Heart\\\\\\\", Joan of Arc and Tokyo to rock and roll, Latin culture and partying.\\\", \\\"tokens\\\": [\\\"Inspirations\\\", \\\"varied\\\", \\\"from\\\", \\\"the\\\", \\\"cover\\\", \\\"artwork\\\", \\\"of\\\", \\\"``\\\", \\\"Rebel\\\", \\\"Heart\\\", \\\"''\\\", \\\",\\\", \\\"Joan\\\", \\\"of\\\", \\\"Arc\\\", \\\"and\\\", \\\"Tokyo\\\", \\\"to\\\", \\\"rock\\\", \\\"and\\\", \\\"roll\\\", \\\",\\\", \\\"Latin\\\", \\\"culture\\\", \\\"and\\\", \\\"partying\\\", \\\".\\\"]}, {\\\"sentence\\\": \\\"The set list had more than 20 songs picked from Madonna's career along with material from \\\\\\\"Rebel Heart\\\\\\\".\\\", \\\"tokens\\\": [\\\"The\\\", \\\"set\\\", \\\"list\\\", \\\"had\\\", \\\"more\\\", \\\"than\\\", \\\"20\\\", \\\"songs\\\", \\\"picked\\\", \\\"from\\\", \\\"Madonna\\\", \\\"'s\\\", \\\"career\\\", \\\"along\\\", \\\"with\\\", \\\"material\\\", \\\"from\\\", \\\"``\\\", \\\"Rebel\\\", \\\"Heart\\\", \\\"''\\\", \\\".\\\"]}, {\\\"sentence\\\": \\\"Critics gave the tour generally positive reviews, praising Madonna's stage presence, vocals and the imagery presented.\\\", \\\"tokens\\\": [\\\"Critics\\\", \\\"gave\\\", \\\"the\\\", \\\"tour\\\", \\\"generally\\\", \\\"positive\\\", \\\"reviews\\\", \\\",\\\", \\\"praising\\\", \\\"Madonna\\\", \\\"'s\\\", \\\"stage\\\", \\\"presence\\\", \\\",\\\", \\\"vocals\\\", \\\"and\\\", \\\"the\\\", \\\"imagery\\\", \\\"presented\\\", \\\".\\\"]}, {\\\"sentence\\\": \\\"The tour courted a number of controversies, but attained commercial success.\\\", \\\"tokens\\\": [\\\"The\\\", \\\"tour\\\", \\\"courted\\\", \\\"a\\\", \\\"number\\\", \\\"of\\\", \\\"controversies\\\", \\\",\\\", \\\"but\\\", \\\"attained\\\", \\\"commercial\\\", \\\"success\\\", \\\".\\\"]}, {\\\"sentence\\\": \\\"It was attended by an audience of over 1.05 million with all the shows being sold out.\\\", \\\"tokens\\\": [\\\"It\\\", \\\"was\\\", \\\"attended\\\", \\\"by\\\", \\\"an\\\", \\\"audience\\\", \\\"of\\\", \\\"over\\\", \\\"1.05\\\", \\\"million\\\", \\\"with\\\", \\\"all\\\", \\\"the\\\", \\\"shows\\\", \\\"being\\\", \\\"sold\\\", \\\"out\\\", \\\".\\\"]}, {\\\"sentence\\\": \\\"Rebel Heart Tour grossed $169.8 million, extending Madonna's record as the highest-grossing solo touring artist with total gross of $1.131 billion, beginning with the Blond Ambition Tour (1990).\\\", \\\"tokens\\\": [\\\"Rebel\\\", \\\"Heart\\\", \\\"Tour\\\", \\\"grossed\\\", \\\"$\\\", \\\"169.8\\\", \\\"million\\\", \\\",\\\", \\\"extending\\\", \\\"Madonna\\\", \\\"'s\\\", \\\"record\\\", \\\"as\\\", \\\"the\\\", \\\"highest-grossing\\\", \\\"solo\\\", \\\"touring\\\", \\\"artist\\\", \\\"with\\\", \\\"total\\\", \\\"gross\\\", \\\"of\\\", \\\"$\\\", \\\"1.131\\\", \\\"billion\\\", \\\",\\\", \\\"beginning\\\", \\\"with\\\", \\\"the\\\", \\\"Blond\\\", \\\"Ambition\\\", \\\"Tour\\\", \\\"(\\\", \\\"1990\\\", \\\")\\\", \\\".\\\"]}, {\\\"sentence\\\": \\\"This ranked her in third place on the all-time top-grossing \\\\\\\"Billboard\\\\\\\" Boxscore list, only behind the Rolling Stones and U2.\\\", \\\"tokens\\\": [\\\"This\\\", \\\"ranked\\\", \\\"her\\\", \\\"in\\\", \\\"third\\\", \\\"place\\\", \\\"on\\\", \\\"the\\\", \\\"all-time\\\", \\\"top-grossing\\\", \\\"``\\\", \\\"Billboard\\\", \\\"''\\\", \\\"Boxscore\\\", \\\"list\\\", \\\",\\\", \\\"only\\\", \\\"behind\\\", \\\"the\\\", \\\"Rolling\\\", \\\"Stones\\\", \\\"and\\\", \\\"U2\\\", \\\".\\\"]}, {\\\"sentence\\\": \\\"The shows of March 19–20, 2016, performed at the Allphones Arena, were filmed by Danny Tull and Nathan Rissman for the film \\\\\\\"Madonna: The Rebel Heart Tour\\\\\\\".\\\", \\\"tokens\\\": [\\\"The\\\", \\\"shows\\\", \\\"of\\\", \\\"March\\\", \\\"19–20\\\", \\\",\\\", \\\"2016\\\", \\\",\\\", \\\"performed\\\", \\\"at\\\", \\\"the\\\", \\\"Allphones\\\", \\\"Arena\\\", \\\",\\\", \\\"were\\\", \\\"filmed\\\", \\\"by\\\", \\\"Danny\\\", \\\"Tull\\\", \\\"and\\\", \\\"Nathan\\\", \\\"Rissman\\\", \\\"for\\\", \\\"the\\\", \\\"film\\\", \\\"``\\\", \\\"Madonna\\\", \\\":\\\", \\\"The\\\", \\\"Rebel\\\", \\\"Heart\\\", \\\"Tour\\\", \\\"''\\\", \\\".\\\"]}, {\\\"sentence\\\": \\\"It premiered on December 9, 2016, on American cable channel Showtime while a live CD/DVD and Blu-ray was released on September 15, 2017.\\\", \\\"tokens\\\": [\\\"It\\\", \\\"premiered\\\", \\\"on\\\", \\\"December\\\", \\\"9\\\", \\\",\\\", \\\"2016\\\", \\\",\\\", \\\"on\\\", \\\"American\\\", \\\"cable\\\", \\\"channel\\\", \\\"Showtime\\\", \\\"while\\\", \\\"a\\\", \\\"live\\\", \\\"CD/DVD\\\", \\\"and\\\", \\\"Blu-ray\\\", \\\"was\\\", \\\"released\\\", \\\"on\\\", \\\"September\\\", \\\"15\\\", \\\",\\\", \\\"2017\\\", \\\".\\\"]}], \\\"candidates\\\": [{\\\"trigger_word\\\": \\\"Rebel\\\", \\\"sent_id\\\": 0, \\\"offset\\\": [0, 1], \\\"id\\\": \\\"6754c69ad5b16ffb8c879a303ca343c5\\\"}, {\\\"trigger_word\\\": \\\"Heart\\\", \\\"sent_id\\\": 0, \\\"offset\\\": [1, 2], \\\"id\\\": \\\"f6e08da06594f7bddfb8892f0d322438\\\"}, {\\\"trigger_word\\\": \\\"Tour\\\", \\\"sent_id\\\": 0, \\\"offset\\\": [2, 3], \\\"id\\\": \\\"a138c45c9bcd2ae1e75b0869d73f10c3\\\"}, {\\\"trigger_word\\\": \\\"tenth\\\", \\\"sent_id\\\": 0, \\\"offset\\\": [5, 6], \\\"id\\\": \\\"cbecae0e110a09df765e5f880aae92ec\\\"}, {\\\"trigger_word\\\": \\\"concert\\\", \\\"sent_id\\\": 0, \\\"offset\\\": [6, 7], \\\"id\\\": \\\"503c880215294f48d826cdc58a36bb95\\\"}, {\\\"trigger_word\\\": \\\"tour\\\", \\\"sent_id\\\": 0, \\\"offset\\\": [7, 8], \\\"id\\\": \\\"52d47637725d3bae5f3cfe77d0d12cad\\\"}, {\\\"trigger_word\\\": \\\"American\\\", \\\"sent_id\\\": 0, \\\"offset\\\": [9, 10], \\\"id\\\": \\\"db2f94c33426a4d18c5e99b8f6f13af3\\\"}, {\\\"trigger_word\\\": \\\"singer\\\", \\\"sent_id\\\": 0, \\\"offset\\\": [10, 11], \\\"id\\\": \\\"a70fa1115b80655eed1e0d6f198b7348\\\"}, {\\\"trigger_word\\\": \\\"Madonna\\\", \\\"sent_id\\\": 0, \\\"offset\\\": [11, 12], \\\"id\\\": \\\"35f63d6c9b671116575a40bb46471642\\\"}, {\\\"trigger_word\\\": \\\"support\\\", \\\"sent_id\\\": 0, \\\"offset\\\": [15, 16], \\\"id\\\": \\\"44f2783c0230fc3db134fa4d690f403f\\\"}, {\\\"trigger_word\\\": \\\"studio\\\", \\\"sent_id\\\": 0, \\\"offset\\\": [19, 20], \\\"id\\\": \\\"6f6ae29b67383b24e739c0bc811b32d0\\\"}, {\\\"trigger_word\\\": \\\"album\\\", \\\"sent_id\\\": 0, \\\"offset\\\": [20, 21], \\\"id\\\": \\\"3dc10118126ec124f7d0ddff76edc5e4\\\"}, {\\\"trigger_word\\\": \\\"Rebel\\\", \\\"sent_id\\\": 0, \\\"offset\\\": [23, 24], \\\"id\\\": \\\"0ec431f5da92ded100c3a84c46b2dccc\\\"}, {\\\"trigger_word\\\": \\\"Heart\\\", \\\"sent_id\\\": 0, \\\"offset\\\": [24, 25], \\\"id\\\": \\\"d0e3eae96db59c69d4319380efb28111\\\"}, {\\\"trigger_word\\\": \\\"Comprising\\\", \\\"sent_id\\\": 1, \\\"offset\\\": [0, 1], \\\"id\\\": \\\"f9157b92707d0016de194b6ae8eba9ba\\\"}, {\\\"trigger_word\\\": \\\"shows\\\", \\\"sent_id\\\": 1, \\\"offset\\\": [2, 3], \\\"id\\\": \\\"ff712793feac7167b012ed344d1d88bd\\\"}, {\\\"trigger_word\\\": \\\"tour\\\", \\\"sent_id\\\": 1, \\\"offset\\\": [5, 6], \\\"id\\\": \\\"929fb57ca54c6c425bb82eda56ab2f2a\\\"}, {\\\"trigger_word\\\": \\\"visited\\\", \\\"sent_id\\\": 1, \\\"offset\\\": [6, 7], \\\"id\\\": \\\"2cec0c41dcaabbc4d43496b3a74bcad4\\\"}, {\\\"trigger_word\\\": \\\"North\\\", \\\"sent_id\\\": 1, \\\"offset\\\": [7, 8], \\\"id\\\": \\\"eb1d4765a38557fef351bb40bc4ddda5\\\"}, {\\\"trigger_word\\\": \\\"America\\\", \\\"sent_id\\\": 1, \\\"offset\\\": [8, 9], \\\"id\\\": \\\"6c90d76c2b841db48cc7ebf218f5513d\\\"}, {\\\"trigger_word\\\": \\\"Asia\\\", \\\"sent_id\\\": 1, \\\"offset\\\": [10, 11], \\\"id\\\": \\\"0a3a8815afc57ee0e0027abaa25a3428\\\"}, {\\\"trigger_word\\\": \\\"Europe\\\", \\\"sent_id\\\": 1, \\\"offset\\\": [12, 13], \\\"id\\\": \\\"ccc76791343127e916d4dfad089165bb\\\"}, {\\\"trigger_word\\\": \\\"Oceania\\\", \\\"sent_id\\\": 1, \\\"offset\\\": [15, 16], \\\"id\\\": \\\"861188840fba6e4d398278d16e25eb6d\\\"}, {\\\"trigger_word\\\": \\\"began\\\", \\\"sent_id\\\": 2, \\\"offset\\\": [1, 2], \\\"id\\\": \\\"b2927279820d6b05b4c4d20496f6752d\\\"}, {\\\"trigger_word\\\": \\\"September\\\", \\\"sent_id\\\": 2, \\\"offset\\\": [3, 4], \\\"id\\\": \\\"07c7d722a6f5b5342be3dd230ac5dba0\\\"}, {\\\"trigger_word\\\": \\\"Montreal\\\", \\\"sent_id\\\": 2, \\\"offset\\\": [9, 10], \\\"id\\\": \\\"7cced583723487cb19aaafece3ebc018\\\"}, {\\\"trigger_word\\\": \\\"Canada\\\", \\\"sent_id\\\": 2, \\\"offset\\\": [11, 12], \\\"id\\\": \\\"60d8abec7baf5fdafbc1fc196ba4780d\\\"}, {\\\"trigger_word\\\": \\\"Bell\\\", \\\"sent_id\\\": 2, \\\"offset\\\": [15, 16], \\\"id\\\": \\\"b55fdb0fdf4de4303108cf6456305dfe\\\"}, {\\\"trigger_word\\\": \\\"Centre\\\", \\\"sent_id\\\": 2, \\\"offset\\\": [16, 17], \\\"id\\\": \\\"5ff37b8205f4eae44671fc72d865d55e\\\"}, {\\\"trigger_word\\\": \\\"concluded\\\", \\\"sent_id\\\": 2, \\\"offset\\\": [18, 19], \\\"id\\\": \\\"f32171bc46ffdc5433d1590c36e946a8\\\"}, {\\\"trigger_word\\\": \\\"March\\\", \\\"sent_id\\\": 2, \\\"offset\\\": [20, 21], \\\"id\\\": \\\"c208114cfeb3477af022835c6a710bb5\\\"}, {\\\"trigger_word\\\": \\\"Sydney\\\", \\\"sent_id\\\": 2, \\\"offset\\\": [26, 27], \\\"id\\\": \\\"2032efabecff104539f8d3fea57ce017\\\"}, {\\\"trigger_word\\\": \\\"Australia\\\", \\\"sent_id\\\": 2, \\\"offset\\\": [28, 29], \\\"id\\\": \\\"ba5273021b7929cba6deb5fd6e51979b\\\"}, {\\\"trigger_word\\\": \\\"Allphones\\\", \\\"sent_id\\\": 2, \\\"offset\\\": [30, 31], \\\"id\\\": \\\"0e11109e8bb2ed08d2859b785cf966b7\\\"}, {\\\"trigger_word\\\": \\\"Arena\\\", \\\"sent_id\\\": 2, \\\"offset\\\": [31, 32], \\\"id\\\": \\\"55aba66f100a3afb0d31523be6e8025a\\\"}, {\\\"trigger_word\\\": \\\"tour\\\", \\\"sent_id\\\": 3, \\\"offset\\\": [1, 2], \\\"id\\\": \\\"7b52f379a1c285f2c607197fd010d4e7\\\"}, {\\\"trigger_word\\\": \\\"officially\\\", \\\"sent_id\\\": 3, \\\"offset\\\": [3, 4], \\\"id\\\": \\\"0565f20f9461f01cb3fd782daefb77dc\\\"}, {\\\"trigger_word\\\": \\\"announced\\\", \\\"sent_id\\\": 3, \\\"offset\\\": [4, 5], \\\"id\\\": \\\"0cc1ae6104266a3bbc9eeb196faa6061\\\"}, {\\\"trigger_word\\\": \\\"March\\\", \\\"sent_id\\\": 3, \\\"offset\\\": [6, 7], \\\"id\\\": \\\"ddf24e8c9c91918f5dde3f8c9a5028db\\\"}, {\\\"trigger_word\\\": \\\"Madonna\\\", \\\"sent_id\\\": 3, \\\"offset\\\": [12, 13], \\\"id\\\": \\\"77f169d278c83dffe571feb3108918d0\\\"}, {\\\"trigger_word\\\": \\\"website\\\", \\\"sent_id\\\": 3, \\\"offset\\\": [14, 15], \\\"id\\\": \\\"fe7c571ccd176a972cb6d3b94fdf23f2\\\"}, {\\\"trigger_word\\\": \\\"Live\\\", \\\"sent_id\\\": 3, \\\"offset\\\": [19, 20], \\\"id\\\": \\\"26cb2c8b3eca1cc059af95b93e97ae32\\\"}, {\\\"trigger_word\\\": \\\"Nation\\\", \\\"sent_id\\\": 3, \\\"offset\\\": [20, 21], \\\"id\\\": \\\"6ca54ec3a3b04c5026a3dae98f47f257\\\"}, {\\\"trigger_word\\\": \\\"Entertainment\\\", \\\"sent_id\\\": 3, \\\"offset\\\": [21, 22], \\\"id\\\": \\\"518cd400cee022d99af390abef2e375f\\\"}, {\\\"trigger_word\\\": \\\"Global\\\", \\\"sent_id\\\": 3, \\\"offset\\\": [23, 24], \\\"id\\\": \\\"d3121335450c90c528658d7ab218ea8c\\\"}, {\\\"trigger_word\\\": \\\"Touring\\\", \\\"sent_id\\\": 3, \\\"offset\\\": [24, 25], \\\"id\\\": \\\"03bac610f8c55aae13ac8d11fd4e4289\\\"}, {\\\"trigger_word\\\": \\\"Division\\\", \\\"sent_id\\\": 3, \\\"offset\\\": [25, 26], \\\"id\\\": \\\"8b9dbcf9624ef1bba9be4c9189557e55\\\"}, {\\\"trigger_word\\\": \\\"Arthur\\\", \\\"sent_id\\\": 3, \\\"offset\\\": [29, 30], \\\"id\\\": \\\"1402b28a6435788ac0d6b3a0fd50e596\\\"}, {\\\"trigger_word\\\": \\\"Fogel\\\", \\\"sent_id\\\": 3, \\\"offset\\\": [30, 31], \\\"id\\\": \\\"357457e09285617ba1af37e09f5bb589\\\"}, {\\\"trigger_word\\\": \\\"fifth\\\", \\\"sent_id\\\": 3, \\\"offset\\\": [35, 36], \\\"id\\\": \\\"0ec614949e8484f1d317a85579d0d321\\\"}, {\\\"trigger_word\\\": \\\"collaboration\\\", \\\"sent_id\\\": 3, \\\"offset\\\": [36, 37], \\\"id\\\": \\\"69611055530ddcc3419232f4b8f5f279\\\"}, {\\\"trigger_word\\\": \\\"Madonna\\\", \\\"sent_id\\\": 3, \\\"offset\\\": [38, 39], \\\"id\\\": \\\"3bf4750ffa7ec1e1498549e077578847\\\"}, {\\\"trigger_word\\\": \\\"Live\\\", \\\"sent_id\\\": 3, \\\"offset\\\": [40, 41], \\\"id\\\": \\\"96eb740c044c085067f8c7334d59763a\\\"}, {\\\"trigger_word\\\": \\\"Nation\\\", \\\"sent_id\\\": 3, \\\"offset\\\": [41, 42], \\\"id\\\": \\\"286336aa89530f5a442e043fc67e09cc\\\"}, {\\\"trigger_word\\\": \\\"well\\\", \\\"sent_id\\\": 3, \\\"offset\\\": [43, 44], \\\"id\\\": \\\"83b3df493f8cb2f38b518c57125c2774\\\"}, {\\\"trigger_word\\\": \\\"third\\\", \\\"sent_id\\\": 3, \\\"offset\\\": [46, 47], \\\"id\\\": \\\"3e867a71dc7fbe0a672cd0f686ecab43\\\"}, {\\\"trigger_word\\\": \\\"tour\\\", \\\"sent_id\\\": 3, \\\"offset\\\": [47, 48], \\\"id\\\": \\\"86498c5d864fa59da3da4b154e2cc195\\\"}, {\\\"trigger_word\\\": \\\"promoted\\\", \\\"sent_id\\\": 3, \\\"offset\\\": [50, 51], \\\"id\\\": \\\"b54cdb03f1b257ca8b024dd693c949b2\\\"}, {\\\"trigger_word\\\": \\\"company\\\", \\\"sent_id\\\": 3, \\\"offset\\\": [53, 54], \\\"id\\\": \\\"63601864b556042d0bc51fbe8b3f6a96\\\"}, {\\\"trigger_word\\\": \\\"all-arena\\\", \\\"sent_id\\\": 4, \\\"offset\\\": [1, 2], \\\"id\\\": \\\"37520496f7ca6a044ec93422154a3ad9\\\"}, {\\\"trigger_word\\\": \\\"Rebel\\\", \\\"sent_id\\\": 4, \\\"offset\\\": [2, 3], \\\"id\\\": \\\"0e5676319543f067dc0d5bc833eb928f\\\"}, {\\\"trigger_word\\\": \\\"Heart\\\", \\\"sent_id\\\": 4, \\\"offset\\\": [3, 4], \\\"id\\\": \\\"6ce2b0a562b3409ef925e5d5a8369899\\\"}, {\\\"trigger_word\\\": \\\"Tour\\\", \\\"sent_id\\\": 4, \\\"offset\\\": [4, 5], \\\"id\\\": \\\"2d6824a416b8791ed296cbf0e5b75ff5\\\"}, {\\\"trigger_word\\\": \\\"also\\\", \\\"sent_id\\\": 4, \\\"offset\\\": [5, 6], \\\"id\\\": \\\"caaa37df63655aeb38322ed7fed0169a\\\"}, {\\\"trigger_word\\\": \\\"visited\\\", \\\"sent_id\\\": 4, \\\"offset\\\": [6, 7], \\\"id\\\": \\\"0311f91d901e4a809b1fd3adf8c14b6f\\\"}, {\\\"trigger_word\\\": \\\"cities\\\", \\\"sent_id\\\": 4, \\\"offset\\\": [7, 8], \\\"id\\\": \\\"59544b7c4c4c2c752bac26f18d99132c\\\"}, {\\\"trigger_word\\\": \\\"singer\\\", \\\"sent_id\\\": 4, \\\"offset\\\": [10, 11], \\\"id\\\": \\\"4c39d940aa26ca20b5f5fddcc2081526\\\"}, {\\\"trigger_word\\\": \\\"performed\\\", \\\"sent_id\\\": 4, \\\"offset\\\": [13, 14], \\\"id\\\": \\\"6022b181ffeeef1e461d2c273b5f07f4\\\"}, {\\\"trigger_word\\\": \\\"first\\\", \\\"sent_id\\\": 4, \\\"offset\\\": [19, 20], \\\"id\\\": \\\"31de07a9cf2bae55b387945f354d17db\\\"}, {\\\"trigger_word\\\": \\\"visit\\\", \\\"sent_id\\\": 4, \\\"offset\\\": [21, 22], \\\"id\\\": \\\"14c70594089a7a01c5332ccaaf72d8b5\\\"}, {\\\"trigger_word\\\": \\\"Australia\\\", \\\"sent_id\\\": 4, \\\"offset\\\": [22, 23], \\\"id\\\": \\\"9f8578bf7bb95a1a09b79c283afad94e\\\"}, {\\\"trigger_word\\\": \\\"Girlie\\\", \\\"sent_id\\\": 4, \\\"offset\\\": [25, 26], \\\"id\\\": \\\"775fb1508f1b46b538328aa4c476ffff\\\"}, {\\\"trigger_word\\\": \\\"Show\\\", \\\"sent_id\\\": 4, \\\"offset\\\": [26, 27], \\\"id\\\": \\\"b91d43ea0cded0f9fbe36060667a6cab\\\"}, {\\\"trigger_word\\\": \\\"World\\\", \\\"sent_id\\\": 4, \\\"offset\\\": [27, 28], \\\"id\\\": \\\"acfd8105995639677d9d70d2cd4450a2\\\"}, {\\\"trigger_word\\\": \\\"Tour\\\", \\\"sent_id\\\": 4, \\\"offset\\\": [28, 29], \\\"id\\\": \\\"530bcdfabe96feb521421dfb0aa0794d\\\"}, {\\\"trigger_word\\\": \\\"Rehearsals\\\", \\\"sent_id\\\": 5, \\\"offset\\\": [0, 1], \\\"id\\\": \\\"91083be0dbc48abfa3c9a935e82e421a\\\"}, {\\\"trigger_word\\\": \\\"tour\\\", \\\"sent_id\\\": 5, \\\"offset\\\": [3, 4], \\\"id\\\": \\\"b9bf83b49b880dde028211303829515d\\\"}, {\\\"trigger_word\\\": \\\"commenced\\\", \\\"sent_id\\\": 5, \\\"offset\\\": [4, 5], \\\"id\\\": \\\"903285235577bb534e17bc64c95e3e40\\\"}, {\\\"trigger_word\\\": \\\"following\\\", \\\"sent_id\\\": 5, \\\"offset\\\": [5, 6], \\\"id\\\": \\\"62019deaeeb25bb7b4cff079384814b0\\\"}, {\\\"trigger_word\\\": \\\"announcement\\\", \\\"sent_id\\\": 5, \\\"offset\\\": [7, 8], \\\"id\\\": \\\"297afd6f7c126b47cde6c0709c018079\\\"}, {\\\"trigger_word\\\": \\\"hours\\\", \\\"sent_id\\\": 5, \\\"offset\\\": [11, 12], \\\"id\\\": \\\"f0d486de159c9e4ca924a321fd698af9\\\"}, {\\\"trigger_word\\\": \\\"day\\\", \\\"sent_id\\\": 5, \\\"offset\\\": [13, 14], \\\"id\\\": \\\"8da37e0559cf9cfc29fa3fe269fe57da\\\"}, {\\\"trigger_word\\\": \\\"involvement\\\", \\\"sent_id\\\": 5, \\\"offset\\\": [16, 17], \\\"id\\\": \\\"000f50d298cb7800b69ef1f467c84bd0\\\"}, {\\\"trigger_word\\\": \\\"Madonna\\\", \\\"sent_id\\\": 5, \\\"offset\\\": [18, 19], \\\"id\\\": \\\"e20fb2eeab29a2c18bc9531c3d0ce3ee\\\"}, {\\\"trigger_word\\\": \\\"team\\\", \\\"sent_id\\\": 5, \\\"offset\\\": [20, 21], \\\"id\\\": \\\"de91223907ada5c53d26f01af14bdf28\\\"}, {\\\"trigger_word\\\": \\\"creative\\\", \\\"sent_id\\\": 5, \\\"offset\\\": [22, 23], \\\"id\\\": \\\"145a37d5152eb73f0079fd9ff5ee6a8a\\\"}, {\\\"trigger_word\\\": \\\"directors\\\", \\\"sent_id\\\": 5, \\\"offset\\\": [23, 24], \\\"id\\\": \\\"fd6ee958eb1c314fd32b9ee5e06de314\\\"}, {\\\"trigger_word\\\": \\\"producers\\\", \\\"sent_id\\\": 5, \\\"offset\\\": [25, 26], \\\"id\\\": \\\"5000b07fc616f8a2de9e0e86bcf69c15\\\"}, {\\\"trigger_word\\\": \\\"designers\\\", \\\"sent_id\\\": 5, \\\"offset\\\": [27, 28], \\\"id\\\": \\\"64a953af241db965de9d43e7599d622a\\\"}, {\\\"trigger_word\\\": \\\"choreographers\\\", \\\"sent_id\\\": 5, \\\"offset\\\": [29, 30], \\\"id\\\": \\\"3ba969d39a445cad506022d009ec1423\\\"}, {\\\"trigger_word\\\": \\\"inspired\\\", \\\"sent_id\\\": 6, \\\"offset\\\": [2, 3], \\\"id\\\": \\\"dd3c9c4ad6b4e1af2204dbed6f7e2c41\\\"}, {\\\"trigger_word\\\": \\\"shows\\\", \\\"sent_id\\\": 6, \\\"offset\\\": [4, 5], \\\"id\\\": \\\"316cf4419176e198b35e8f37e2ca4753\\\"}, {\\\"trigger_word\\\": \\\"Cirque\\\", \\\"sent_id\\\": 6, \\\"offset\\\": [6, 7], \\\"id\\\": \\\"d2896a7ac44a5e07e7581f875bb08d4e\\\"}, {\\\"trigger_word\\\": \\\"du\\\", \\\"sent_id\\\": 6, \\\"offset\\\": [7, 8], \\\"id\\\": \\\"2dd0075227e789a9c56a6749fd8aed59\\\"}, {\\\"trigger_word\\\": \\\"Soleil\\\", \\\"sent_id\\\": 6, \\\"offset\\\": [8, 9], \\\"id\\\": \\\"95dda981a79cadae4bc8fa173bd12dfc\\\"}, {\\\"trigger_word\\\": \\\"Chinese\\\", \\\"sent_id\\\": 6, \\\"offset\\\": [10, 11], \\\"id\\\": \\\"da573c25bee44da2ca4ff98182a2f21a\\\"}, {\\\"trigger_word\\\": \\\"New\\\", \\\"sent_id\\\": 6, \\\"offset\\\": [11, 12], \\\"id\\\": \\\"5e537c0851978f4651bf35fd82325cc6\\\"}, {\\\"trigger_word\\\": \\\"Year\\\", \\\"sent_id\\\": 6, \\\"offset\\\": [12, 13], \\\"id\\\": \\\"15c144351f8cc472cfa051be9cd926e4\\\"}, {\\\"trigger_word\\\": \\\"well\\\", \\\"sent_id\\\": 6, \\\"offset\\\": [15, 16], \\\"id\\\": \\\"ca3e9e763a84cb59d13c60df7c886ce0\\\"}, {\\\"trigger_word\\\": \\\"films\\\", \\\"sent_id\\\": 6, \\\"offset\\\": [18, 19], \\\"id\\\": \\\"4312d902abdf894d2efc36dd14c1f47b\\\"}, {\\\"trigger_word\\\": \\\"Grease\\\", \\\"sent_id\\\": 6, \\\"offset\\\": [27, 28], \\\"id\\\": \\\"be7c1b22c8cdb15e1ff515c178879459\\\"}, {\\\"trigger_word\\\": \\\"Madonna\\\", \\\"sent_id\\\": 7, \\\"offset\\\": [0, 1], \\\"id\\\": \\\"2c954c4dd07d805753ae92390fb7aaca\\\"}, {\\\"trigger_word\\\": \\\"enlisted\\\", \\\"sent_id\\\": 7, \\\"offset\\\": [1, 2], \\\"id\\\": \\\"7b93060ffe824bb23f0ca454113ffc2e\\\"}, {\\\"trigger_word\\\": \\\"Jamie\\\", \\\"sent_id\\\": 7, \\\"offset\\\": [2, 3], \\\"id\\\": \\\"1b44f80095c331636ce01ea8e66bf952\\\"}, {\\\"trigger_word\\\": \\\"King\\\", \\\"sent_id\\\": 7, \\\"offset\\\": [3, 4], \\\"id\\\": \\\"78e3502ddcefd7711eb7f116712777b8\\\"}, {\\\"trigger_word\\\": \\\"creative\\\", \\\"sent_id\\\": 7, \\\"offset\\\": [6, 7], \\\"id\\\": \\\"2687ef98572bbd8b529632dc8a1e67da\\\"}, {\\\"trigger_word\\\": \\\"director\\\", \\\"sent_id\\\": 7, \\\"offset\\\": [7, 8], \\\"id\\\": \\\"13469e69cb6da25c25608352e63c6c52\\\"}, {\\\"trigger_word\\\": \\\"Megan\\\", \\\"sent_id\\\": 7, \\\"offset\\\": [10, 11], \\\"id\\\": \\\"cb015ad3193459eda92df4fe040751f6\\\"}, {\\\"trigger_word\\\": \\\"Lawson\\\", \\\"sent_id\\\": 7, \\\"offset\\\": [11, 12], \\\"id\\\": \\\"8446dc287b90f8e235f10465c12c1c9a\\\"}, {\\\"trigger_word\\\": \\\"Jason\\\", \\\"sent_id\\\": 7, \\\"offset\\\": [13, 14], \\\"id\\\": \\\"ff3998422fc531cf1cd722afbedda78f\\\"}, {\\\"trigger_word\\\": \\\"Yong\\\", \\\"sent_id\\\": 7, \\\"offset\\\": [14, 15], \\\"id\\\": \\\"d0941ccbd3a03c31d00852b610deaf4b\\\"}, {\\\"trigger_word\\\": \\\"choreographers\\\", \\\"sent_id\\\": 7, \\\"offset\\\": [16, 17], \\\"id\\\": \\\"7e88061ec1c72ebc053044acea259633\\\"}, {\\\"trigger_word\\\": \\\"tour\\\", \\\"sent_id\\\": 8, \\\"offset\\\": [1, 2], \\\"id\\\": \\\"89a9bb445c6aeae1279a8e14031c3473\\\"}, {\\\"trigger_word\\\": \\\"featured\\\", \\\"sent_id\\\": 8, \\\"offset\\\": [2, 3], \\\"id\\\": \\\"fc5363656408ed99e5c6b3224897a786\\\"}, {\\\"trigger_word\\\": \\\"costumes\\\", \\\"sent_id\\\": 8, \\\"offset\\\": [3, 4], \\\"id\\\": \\\"7237feb6d852d2dd93832b759f8424a0\\\"}, {\\\"trigger_word\\\": \\\"Moschino\\\", \\\"sent_id\\\": 8, \\\"offset\\\": [5, 6], \\\"id\\\": \\\"ad48c4145ebc85efe9bd3dfd58697cc4\\\"}, {\\\"trigger_word\\\": \\\"Prada\\\", \\\"sent_id\\\": 8, \\\"offset\\\": [7, 8], \\\"id\\\": \\\"6f3d4fc4e1d417d94e9956275c450ba5\\\"}, {\\\"trigger_word\\\": \\\"Miu\\\", \\\"sent_id\\\": 8, \\\"offset\\\": [9, 10], \\\"id\\\": \\\"a8902d3b27a440a489c385c1e7b78bb8\\\"}, {\\\"trigger_word\\\": \\\"Miu\\\", \\\"sent_id\\\": 8, \\\"offset\\\": [10, 11], \\\"id\\\": \\\"68b16b60505a84656b7d8a31d59ea107\\\"}, {\\\"trigger_word\\\": \\\"Gucci\\\", \\\"sent_id\\\": 8, \\\"offset\\\": [12, 13], \\\"id\\\": \\\"acee4358fba0aa45e7e74c337de078e9\\\"}, {\\\"trigger_word\\\": \\\"Swarovski\\\", \\\"sent_id\\\": 8, \\\"offset\\\": [14, 15], \\\"id\\\": \\\"d815e95e63f1430dd20134b433cbf739\\\"}, {\\\"trigger_word\\\": \\\"jewelry\\\", \\\"sent_id\\\": 8, \\\"offset\\\": [15, 16], \\\"id\\\": \\\"783da45679adb05d1d9e8dd7b6ed0ead\\\"}, {\\\"trigger_word\\\": \\\"elevated\\\", \\\"sent_id\\\": 8, \\\"offset\\\": [19, 20], \\\"id\\\": \\\"15f976ec837fdf979e5e65c25ace5dec\\\"}, {\\\"trigger_word\\\": \\\"stage\\\", \\\"sent_id\\\": 8, \\\"offset\\\": [20, 21], \\\"id\\\": \\\"a3ee8ca4d14472790df98f3e9bfe577c\\\"}, {\\\"trigger_word\\\": \\\"runway\\\", \\\"sent_id\\\": 8, \\\"offset\\\": [23, 24], \\\"id\\\": \\\"c6dc273111f30167514b43636d2d3caa\\\"}, {\\\"trigger_word\\\": \\\"heart-shaped\\\", \\\"sent_id\\\": 8, \\\"offset\\\": [26, 27], \\\"id\\\": \\\"411cc9b9dd99ea04743d9c33b31d03f8\\\"}, {\\\"trigger_word\\\": \\\"front\\\", \\\"sent_id\\\": 8, \\\"offset\\\": [27, 28], \\\"id\\\": \\\"665ced106b33d5d78eb50214b44a6a7c\\\"}, {\\\"trigger_word\\\": \\\"Multimedia\\\", \\\"sent_id\\\": 9, \\\"offset\\\": [0, 1], \\\"id\\\": \\\"63af0c4ad2a6a26f055713b55019b03f\\\"}, {\\\"trigger_word\\\": \\\"created\\\", \\\"sent_id\\\": 9, \\\"offset\\\": [2, 3], \\\"id\\\": \\\"cbd6ab8ffd9b48ef29f8f70954148665\\\"}, {\\\"trigger_word\\\": \\\"Moment\\\", \\\"sent_id\\\": 9, \\\"offset\\\": [4, 5], \\\"id\\\": \\\"0f0dd8973b4aeb873cf0fe8619d4f095\\\"}, {\\\"trigger_word\\\": \\\"Factory\\\", \\\"sent_id\\\": 9, \\\"offset\\\": [5, 6], \\\"id\\\": \\\"edab1b2ae913a2a64bb2f14ef9ee02ae\\\"}, {\\\"trigger_word\\\": \\\"sound\\\", \\\"sent_id\\\": 9, \\\"offset\\\": [8, 9], \\\"id\\\": \\\"f51da524fea4f7cdeeebed10f04749f9\\\"}, {\\\"trigger_word\\\": \\\"light\\\", \\\"sent_id\\\": 9, \\\"offset\\\": [10, 11], \\\"id\\\": \\\"5645ab5166892462597e65437bfc6714\\\"}, {\\\"trigger_word\\\": \\\"produced\\\", \\\"sent_id\\\": 9, \\\"offset\\\": [12, 13], \\\"id\\\": \\\"4ce1d5cf3f46b225c4b2173d249bf475\\\"}, {\\\"trigger_word\\\": \\\"Clay\\\", \\\"sent_id\\\": 9, \\\"offset\\\": [14, 15], \\\"id\\\": \\\"04599a8609bfe590e5bec0252fb9caec\\\"}, {\\\"trigger_word\\\": \\\"Paky\\\", \\\"sent_id\\\": 9, \\\"offset\\\": [15, 16], \\\"id\\\": \\\"a07ec12103e0e8b5732c94bfd4a9cb35\\\"}, {\\\"trigger_word\\\": \\\"DiGiCo\\\", \\\"sent_id\\\": 9, \\\"offset\\\": [17, 18], \\\"id\\\": \\\"f4ade8c90cda7920fb7f30e6a141fe69\\\"}, {\\\"trigger_word\\\": \\\"respectively\\\", \\\"sent_id\\\": 9, \\\"offset\\\": [19, 20], \\\"id\\\": \\\"787911b8d27c100af64f26c37cf52486\\\"}, {\\\"trigger_word\\\": \\\"central\\\", \\\"sent_id\\\": 10, \\\"offset\\\": [1, 2], \\\"id\\\": \\\"23eeb7d38d5853ad5d94d2dd9db498eb\\\"}, {\\\"trigger_word\\\": \\\"theme\\\", \\\"sent_id\\\": 10, \\\"offset\\\": [2, 3], \\\"id\\\": \\\"8f950ba7df86cf6037a410aa0fb53691\\\"}, {\\\"trigger_word\\\": \\\"show\\\", \\\"sent_id\\\": 10, \\\"offset\\\": [5, 6], \\\"id\\\": \\\"2cb5b4b2fd2e3c6695bfcaa4aa27522b\\\"}, {\\\"trigger_word\\\": \\\"love\\\", \\\"sent_id\\\": 10, \\\"offset\\\": [7, 8], \\\"id\\\": \\\"f94e5d67cec8e960b5759949665625d8\\\"}, {\\\"trigger_word\\\": \\\"romance\\\", \\\"sent_id\\\": 10, \\\"offset\\\": [9, 10], \\\"id\\\": \\\"e462ba0513e730e355a522f22b788a6f\\\"}, {\\\"trigger_word\\\": \\\"consisted\\\", \\\"sent_id\\\": 10, \\\"offset\\\": [12, 13], \\\"id\\\": \\\"9b78392fd8d679b77c27cd87a519d36c\\\"}, {\\\"trigger_word\\\": \\\"segments\\\", \\\"sent_id\\\": 10, \\\"offset\\\": [15, 16], \\\"id\\\": \\\"67bcfae47c1357bbeaf6bcb6fc969622\\\"}, {\\\"trigger_word\\\": \\\"inspired\\\", \\\"sent_id\\\": 10, \\\"offset\\\": [19, 20], \\\"id\\\": \\\"eaae5a0c0aa4b38c58be86f8c743212b\\\"}, {\\\"trigger_word\\\": \\\"different\\\", \\\"sent_id\\\": 10, \\\"offset\\\": [21, 22], \\\"id\\\": \\\"5a318b7c2d5a2f2f11ebdeb8871e3160\\\"}, {\\\"trigger_word\\\": \\\"topics\\\", \\\"sent_id\\\": 10, \\\"offset\\\": [22, 23], \\\"id\\\": \\\"8fc1c58832f19d29d3f1e912f8e65e65\\\"}, {\\\"trigger_word\\\": \\\"Inspirations\\\", \\\"sent_id\\\": 11, \\\"offset\\\": [0, 1], \\\"id\\\": \\\"66ec89d364d58eba9925821dce4d5fa1\\\"}, {\\\"trigger_word\\\": \\\"varied\\\", \\\"sent_id\\\": 11, \\\"offset\\\": [1, 2], \\\"id\\\": \\\"abfc94c3a9a0c8811efc3635f29f8397\\\"}, {\\\"trigger_word\\\": \\\"cover\\\", \\\"sent_id\\\": 11, \\\"offset\\\": [4, 5], \\\"id\\\": \\\"34f4ee4e0f8b4c87a06f4bf3bf46b0ea\\\"}, {\\\"trigger_word\\\": \\\"artwork\\\", \\\"sent_id\\\": 11, \\\"offset\\\": [5, 6], \\\"id\\\": \\\"8c794cd548ff109c02aabac643c49ed4\\\"}, {\\\"trigger_word\\\": \\\"Rebel\\\", \\\"sent_id\\\": 11, \\\"offset\\\": [8, 9], \\\"id\\\": \\\"2c4621754596ebb33006341353f1dfeb\\\"}, {\\\"trigger_word\\\": \\\"Heart\\\", \\\"sent_id\\\": 11, \\\"offset\\\": [9, 10], \\\"id\\\": \\\"b0a1e2aa77ba756ae8427ece7219d000\\\"}, {\\\"trigger_word\\\": \\\"Joan\\\", \\\"sent_id\\\": 11, \\\"offset\\\": [12, 13], \\\"id\\\": \\\"9dca3466250345719690afdb5ed67e39\\\"}, {\\\"trigger_word\\\": \\\"Arc\\\", \\\"sent_id\\\": 11, \\\"offset\\\": [14, 15], \\\"id\\\": \\\"5d33d940fa3403c92e64556437fadd5f\\\"}, {\\\"trigger_word\\\": \\\"Tokyo\\\", \\\"sent_id\\\": 11, \\\"offset\\\": [16, 17], \\\"id\\\": \\\"7435604b38950ad99d71193d7449ee80\\\"}, {\\\"trigger_word\\\": \\\"rock\\\", \\\"sent_id\\\": 11, \\\"offset\\\": [18, 19], \\\"id\\\": \\\"8c9470f6202c7a59a0922623edd90820\\\"}, {\\\"trigger_word\\\": \\\"roll\\\", \\\"sent_id\\\": 11, \\\"offset\\\": [20, 21], \\\"id\\\": \\\"d7824a968e077fb9bced5dcebe620560\\\"}, {\\\"trigger_word\\\": \\\"Latin\\\", \\\"sent_id\\\": 11, \\\"offset\\\": [22, 23], \\\"id\\\": \\\"dd9967eef37d9cba2c9f845153a4da71\\\"}, {\\\"trigger_word\\\": \\\"culture\\\", \\\"sent_id\\\": 11, \\\"offset\\\": [23, 24], \\\"id\\\": \\\"86f7386531ec59691b5b557f7811a6e2\\\"}, {\\\"trigger_word\\\": \\\"partying\\\", \\\"sent_id\\\": 11, \\\"offset\\\": [25, 26], \\\"id\\\": \\\"4a3566a372ad7b89e415bfa5ae0af1c4\\\"}, {\\\"trigger_word\\\": \\\"set\\\", \\\"sent_id\\\": 12, \\\"offset\\\": [1, 2], \\\"id\\\": \\\"067ab4382254900681d92a4a91d0bb49\\\"}, {\\\"trigger_word\\\": \\\"list\\\", \\\"sent_id\\\": 12, \\\"offset\\\": [2, 3], \\\"id\\\": \\\"696360df4e1f5cf3cc14daefb895b035\\\"}, {\\\"trigger_word\\\": \\\"songs\\\", \\\"sent_id\\\": 12, \\\"offset\\\": [7, 8], \\\"id\\\": \\\"3e62efa8d35164e3f21b6a91e93de061\\\"}, {\\\"trigger_word\\\": \\\"picked\\\", \\\"sent_id\\\": 12, \\\"offset\\\": [8, 9], \\\"id\\\": \\\"0e703739fb596ce4850d5b7022906525\\\"}, {\\\"trigger_word\\\": \\\"Madonna\\\", \\\"sent_id\\\": 12, \\\"offset\\\": [10, 11], \\\"id\\\": \\\"308975218ca17166c5d6406ff415c9b8\\\"}, {\\\"trigger_word\\\": \\\"career\\\", \\\"sent_id\\\": 12, \\\"offset\\\": [12, 13], \\\"id\\\": \\\"54a0930359563b20e294202ee5840cd0\\\"}, {\\\"trigger_word\\\": \\\"material\\\", \\\"sent_id\\\": 12, \\\"offset\\\": [15, 16], \\\"id\\\": \\\"c00a5e6bfa0358fc5e404d1864affa14\\\"}, {\\\"trigger_word\\\": \\\"Rebel\\\", \\\"sent_id\\\": 12, \\\"offset\\\": [18, 19], \\\"id\\\": \\\"d668bca8a99075cc0babecb36fd48045\\\"}, {\\\"trigger_word\\\": \\\"Heart\\\", \\\"sent_id\\\": 12, \\\"offset\\\": [19, 20], \\\"id\\\": \\\"76ac8897ab73b3661f5040a797acf943\\\"}, {\\\"trigger_word\\\": \\\"Critics\\\", \\\"sent_id\\\": 13, \\\"offset\\\": [0, 1], \\\"id\\\": \\\"4e8d39580349e5ccef69a353304c7e68\\\"}, {\\\"trigger_word\\\": \\\"gave\\\", \\\"sent_id\\\": 13, \\\"offset\\\": [1, 2], \\\"id\\\": \\\"9b8dfc5a20ecb0a2e16032ee627a3d0d\\\"}, {\\\"trigger_word\\\": \\\"tour\\\", \\\"sent_id\\\": 13, \\\"offset\\\": [3, 4], \\\"id\\\": \\\"710ac80aa51ec560d322a3915f4812c2\\\"}, {\\\"trigger_word\\\": \\\"generally\\\", \\\"sent_id\\\": 13, \\\"offset\\\": [4, 5], \\\"id\\\": \\\"fc963ee923242fd0f96f358a2cefb4ca\\\"}, {\\\"trigger_word\\\": \\\"positive\\\", \\\"sent_id\\\": 13, \\\"offset\\\": [5, 6], \\\"id\\\": \\\"2ff3d5b54e828b4ef310d5a4178cd1d3\\\"}, {\\\"trigger_word\\\": \\\"reviews\\\", \\\"sent_id\\\": 13, \\\"offset\\\": [6, 7], \\\"id\\\": \\\"b2dce6b870133e15bba9b383637966d6\\\"}, {\\\"trigger_word\\\": \\\"praising\\\", \\\"sent_id\\\": 13, \\\"offset\\\": [8, 9], \\\"id\\\": \\\"f42562db7ed206f17846074407b0bda6\\\"}, {\\\"trigger_word\\\": \\\"Madonna\\\", \\\"sent_id\\\": 13, \\\"offset\\\": [9, 10], \\\"id\\\": \\\"3211e8301ab90d08bb3d3a8bff4ed64a\\\"}, {\\\"trigger_word\\\": \\\"stage\\\", \\\"sent_id\\\": 13, \\\"offset\\\": [11, 12], \\\"id\\\": \\\"fbfd9495b88f518b564d3b18f824b199\\\"}, {\\\"trigger_word\\\": \\\"presence\\\", \\\"sent_id\\\": 13, \\\"offset\\\": [12, 13], \\\"id\\\": \\\"cff8e225eeef2d658a351287b9dfd8d7\\\"}, {\\\"trigger_word\\\": \\\"vocals\\\", \\\"sent_id\\\": 13, \\\"offset\\\": [14, 15], \\\"id\\\": \\\"eb1296f5f8f606478cbd4ba2df0ce7ec\\\"}, {\\\"trigger_word\\\": \\\"imagery\\\", \\\"sent_id\\\": 13, \\\"offset\\\": [17, 18], \\\"id\\\": \\\"9616aedb370c829f6cd43902ee23c5d5\\\"}, {\\\"trigger_word\\\": \\\"presented\\\", \\\"sent_id\\\": 13, \\\"offset\\\": [18, 19], \\\"id\\\": \\\"6041e75bded81df575accf8f110c6a6e\\\"}, {\\\"trigger_word\\\": \\\"tour\\\", \\\"sent_id\\\": 14, \\\"offset\\\": [1, 2], \\\"id\\\": \\\"b1b105e1cceae40cd7c6e9c86fdef7c0\\\"}, {\\\"trigger_word\\\": \\\"courted\\\", \\\"sent_id\\\": 14, \\\"offset\\\": [2, 3], \\\"id\\\": \\\"c5c91b6df138ceb165c0b924f28ce68a\\\"}, {\\\"trigger_word\\\": \\\"number\\\", \\\"sent_id\\\": 14, \\\"offset\\\": [4, 5], \\\"id\\\": \\\"7da8c7fafd85db0117b060faf85d512d\\\"}, {\\\"trigger_word\\\": \\\"controversies\\\", \\\"sent_id\\\": 14, \\\"offset\\\": [6, 7], \\\"id\\\": \\\"e115e452b556dcaa66a5bd1c674e8fd9\\\"}, {\\\"trigger_word\\\": \\\"attained\\\", \\\"sent_id\\\": 14, \\\"offset\\\": [9, 10], \\\"id\\\": \\\"5b1c9ae5064e0803c0fb1f416433d5ad\\\"}, {\\\"trigger_word\\\": \\\"commercial\\\", \\\"sent_id\\\": 14, \\\"offset\\\": [10, 11], \\\"id\\\": \\\"0eb5202ca7070338d0e24333de179070\\\"}, {\\\"trigger_word\\\": \\\"success\\\", \\\"sent_id\\\": 14, \\\"offset\\\": [11, 12], \\\"id\\\": \\\"3dfd1770578da705bdde0ad8a1e07123\\\"}, {\\\"trigger_word\\\": \\\"attended\\\", \\\"sent_id\\\": 15, \\\"offset\\\": [2, 3], \\\"id\\\": \\\"6a36b6cf8d8a811760ee8b665beb8451\\\"}, {\\\"trigger_word\\\": \\\"audience\\\", \\\"sent_id\\\": 15, \\\"offset\\\": [5, 6], \\\"id\\\": \\\"a8ca0cf7123b664c019c97ac831a96a7\\\"}, {\\\"trigger_word\\\": \\\"shows\\\", \\\"sent_id\\\": 15, \\\"offset\\\": [13, 14], \\\"id\\\": \\\"e02817624f39ae3fa08e01c06a0d3a5c\\\"}, {\\\"trigger_word\\\": \\\"sold\\\", \\\"sent_id\\\": 15, \\\"offset\\\": [15, 16], \\\"id\\\": \\\"cbb5c0dcd0bf0f3abd487dee5f11c3aa\\\"}, {\\\"trigger_word\\\": \\\"Rebel\\\", \\\"sent_id\\\": 16, \\\"offset\\\": [0, 1], \\\"id\\\": \\\"3fe20ad7d870423add429cb5910284aa\\\"}, {\\\"trigger_word\\\": \\\"Heart\\\", \\\"sent_id\\\": 16, \\\"offset\\\": [1, 2], \\\"id\\\": \\\"55ee02cc2d3909c8afb63a7a389ad199\\\"}, {\\\"trigger_word\\\": \\\"Tour\\\", \\\"sent_id\\\": 16, \\\"offset\\\": [2, 3], \\\"id\\\": \\\"7d5b1380979c978e8ae909e349321389\\\"}, {\\\"trigger_word\\\": \\\"grossed\\\", \\\"sent_id\\\": 16, \\\"offset\\\": [3, 4], \\\"id\\\": \\\"5b533c5ea4317f0cd09e5d97cebb3cb6\\\"}, {\\\"trigger_word\\\": \\\"extending\\\", \\\"sent_id\\\": 16, \\\"offset\\\": [8, 9], \\\"id\\\": \\\"acdcfca7ef600d9b142370bc28ffcff9\\\"}, {\\\"trigger_word\\\": \\\"Madonna\\\", \\\"sent_id\\\": 16, \\\"offset\\\": [9, 10], \\\"id\\\": \\\"a5829114ba6c931f6f4d9da63a669e3e\\\"}, {\\\"trigger_word\\\": \\\"record\\\", \\\"sent_id\\\": 16, \\\"offset\\\": [11, 12], \\\"id\\\": \\\"c84d1586ef381773471ca4bbc7b5fb9d\\\"}, {\\\"trigger_word\\\": \\\"highest-grossing\\\", \\\"sent_id\\\": 16, \\\"offset\\\": [14, 15], \\\"id\\\": \\\"e6f4e6a8f982a4dafc7968a976ee9192\\\"}, {\\\"trigger_word\\\": \\\"solo\\\", \\\"sent_id\\\": 16, \\\"offset\\\": [15, 16], \\\"id\\\": \\\"6ed231172dc9d78b1d602c904cd6a9b8\\\"}, {\\\"trigger_word\\\": \\\"touring\\\", \\\"sent_id\\\": 16, \\\"offset\\\": [16, 17], \\\"id\\\": \\\"2dcc6aeb7766fd0aedf691d5062c0fc2\\\"}, {\\\"trigger_word\\\": \\\"artist\\\", \\\"sent_id\\\": 16, \\\"offset\\\": [17, 18], \\\"id\\\": \\\"84f1accaf642b678a65cd3453631c509\\\"}, {\\\"trigger_word\\\": \\\"total\\\", \\\"sent_id\\\": 16, \\\"offset\\\": [19, 20], \\\"id\\\": \\\"e3cd0aa8f63a758b35e7a28067ec32f1\\\"}, {\\\"trigger_word\\\": \\\"gross\\\", \\\"sent_id\\\": 16, \\\"offset\\\": [20, 21], \\\"id\\\": \\\"000e4389d40093f66f6f7dff9b1958c6\\\"}, {\\\"trigger_word\\\": \\\"beginning\\\", \\\"sent_id\\\": 16, \\\"offset\\\": [26, 27], \\\"id\\\": \\\"18ba91111dd843ae6b14f381c7153108\\\"}, {\\\"trigger_word\\\": \\\"Blond\\\", \\\"sent_id\\\": 16, \\\"offset\\\": [29, 30], \\\"id\\\": \\\"a3222812ac1b94ad7d4c79e2d924a768\\\"}, {\\\"trigger_word\\\": \\\"Ambition\\\", \\\"sent_id\\\": 16, \\\"offset\\\": [30, 31], \\\"id\\\": \\\"7ae90ac4a1ed6c5d875bd1f82d041e9f\\\"}, {\\\"trigger_word\\\": \\\"Tour\\\", \\\"sent_id\\\": 16, \\\"offset\\\": [31, 32], \\\"id\\\": \\\"635e5e6a9b8a1a444a940d81e62fab29\\\"}, {\\\"trigger_word\\\": \\\"ranked\\\", \\\"sent_id\\\": 17, \\\"offset\\\": [1, 2], \\\"id\\\": \\\"aef97c5f23549e0c0c473d3ccdc4aacd\\\"}, {\\\"trigger_word\\\": \\\"third\\\", \\\"sent_id\\\": 17, \\\"offset\\\": [4, 5], \\\"id\\\": \\\"5cc81891b3fab771b60ca07409cb47bc\\\"}, {\\\"trigger_word\\\": \\\"place\\\", \\\"sent_id\\\": 17, \\\"offset\\\": [5, 6], \\\"id\\\": \\\"cbc5809d3d1ea26a11a1317454f227e1\\\"}, {\\\"trigger_word\\\": \\\"all-time\\\", \\\"sent_id\\\": 17, \\\"offset\\\": [8, 9], \\\"id\\\": \\\"8202e94a638e749e6464e51e98bc8818\\\"}, {\\\"trigger_word\\\": \\\"top-grossing\\\", \\\"sent_id\\\": 17, \\\"offset\\\": [9, 10], \\\"id\\\": \\\"a8d4235e0b1e7b9e306c97324c606f15\\\"}, {\\\"trigger_word\\\": \\\"Billboard\\\", \\\"sent_id\\\": 17, \\\"offset\\\": [11, 12], \\\"id\\\": \\\"fed78120bb0ffa7d0f1999f25b9a5680\\\"}, {\\\"trigger_word\\\": \\\"Boxscore\\\", \\\"sent_id\\\": 17, \\\"offset\\\": [13, 14], \\\"id\\\": \\\"cd4a4af394e790dffe1e14d9e304d7bc\\\"}, {\\\"trigger_word\\\": \\\"list\\\", \\\"sent_id\\\": 17, \\\"offset\\\": [14, 15], \\\"id\\\": \\\"51719876c05a3dc31ac6749eea274771\\\"}, {\\\"trigger_word\\\": \\\"Rolling\\\", \\\"sent_id\\\": 17, \\\"offset\\\": [19, 20], \\\"id\\\": \\\"06b2d01a112181ec620139217d500274\\\"}, {\\\"trigger_word\\\": \\\"Stones\\\", \\\"sent_id\\\": 17, \\\"offset\\\": [20, 21], \\\"id\\\": \\\"a15f037e6320c1ca2cd26d110faf8f25\\\"}, {\\\"trigger_word\\\": \\\"U2\\\", \\\"sent_id\\\": 17, \\\"offset\\\": [22, 23], \\\"id\\\": \\\"e3f31bf291b43455a7048285539e4f63\\\"}, {\\\"trigger_word\\\": \\\"shows\\\", \\\"sent_id\\\": 18, \\\"offset\\\": [1, 2], \\\"id\\\": \\\"a8c65a6c5d6fbad46a74263c8bfe1769\\\"}, {\\\"trigger_word\\\": \\\"March\\\", \\\"sent_id\\\": 18, \\\"offset\\\": [3, 4], \\\"id\\\": \\\"e5b45e4cbd7771725d7cc331cf2d229f\\\"}, {\\\"trigger_word\\\": \\\"performed\\\", \\\"sent_id\\\": 18, \\\"offset\\\": [8, 9], \\\"id\\\": \\\"0fcf206b044757ff5317cee42c4c038e\\\"}, {\\\"trigger_word\\\": \\\"Allphones\\\", \\\"sent_id\\\": 18, \\\"offset\\\": [11, 12], \\\"id\\\": \\\"17d429a665c807fb12fce56e26fe6e63\\\"}, {\\\"trigger_word\\\": \\\"Arena\\\", \\\"sent_id\\\": 18, \\\"offset\\\": [12, 13], \\\"id\\\": \\\"5059512d07468cd1b931bd769cf7b9c8\\\"}, {\\\"trigger_word\\\": \\\"filmed\\\", \\\"sent_id\\\": 18, \\\"offset\\\": [15, 16], \\\"id\\\": \\\"9ca970ee21475ff4952677d284580083\\\"}, {\\\"trigger_word\\\": \\\"Danny\\\", \\\"sent_id\\\": 18, \\\"offset\\\": [17, 18], \\\"id\\\": \\\"a7a9c129db31ca021e85458deabea202\\\"}, {\\\"trigger_word\\\": \\\"Tull\\\", \\\"sent_id\\\": 18, \\\"offset\\\": [18, 19], \\\"id\\\": \\\"5e990a0cdbae026d6159d9f6de566528\\\"}, {\\\"trigger_word\\\": \\\"Nathan\\\", \\\"sent_id\\\": 18, \\\"offset\\\": [20, 21], \\\"id\\\": \\\"0bad88d96741957c98c44a7c816ca806\\\"}, {\\\"trigger_word\\\": \\\"Rissman\\\", \\\"sent_id\\\": 18, \\\"offset\\\": [21, 22], \\\"id\\\": \\\"1e4996058f21dad7b584c51aae85783f\\\"}, {\\\"trigger_word\\\": \\\"film\\\", \\\"sent_id\\\": 18, \\\"offset\\\": [24, 25], \\\"id\\\": \\\"bc3fa4c2e4a8ce48a1b0375a41e23baf\\\"}, {\\\"trigger_word\\\": \\\"Madonna\\\", \\\"sent_id\\\": 18, \\\"offset\\\": [26, 27], \\\"id\\\": \\\"7cf98d1bcc77788dcad1d23a36df7167\\\"}, {\\\"trigger_word\\\": \\\"Rebel\\\", \\\"sent_id\\\": 18, \\\"offset\\\": [29, 30], \\\"id\\\": \\\"4ac49e873b4b06f392209cec7cb2c614\\\"}, {\\\"trigger_word\\\": \\\"Heart\\\", \\\"sent_id\\\": 18, \\\"offset\\\": [30, 31], \\\"id\\\": \\\"3e1b318b83737c45a35ee852bf1aa9c6\\\"}, {\\\"trigger_word\\\": \\\"Tour\\\", \\\"sent_id\\\": 18, \\\"offset\\\": [31, 32], \\\"id\\\": \\\"38d2594e826555a3ba3ef3db634e4994\\\"}, {\\\"trigger_word\\\": \\\"premiered\\\", \\\"sent_id\\\": 19, \\\"offset\\\": [1, 2], \\\"id\\\": \\\"ab24fe134d3e076756006c285a7265fb\\\"}, {\\\"trigger_word\\\": \\\"December\\\", \\\"sent_id\\\": 19, \\\"offset\\\": [3, 4], \\\"id\\\": \\\"9f35b79c652e9708a22be7f258f410bc\\\"}, {\\\"trigger_word\\\": \\\"American\\\", \\\"sent_id\\\": 19, \\\"offset\\\": [9, 10], \\\"id\\\": \\\"50c3b02b5739ae54c1b91f4a04551dff\\\"}, {\\\"trigger_word\\\": \\\"cable\\\", \\\"sent_id\\\": 19, \\\"offset\\\": [10, 11], \\\"id\\\": \\\"612392916d2451648f4b5d23729b837a\\\"}, {\\\"trigger_word\\\": \\\"channel\\\", \\\"sent_id\\\": 19, \\\"offset\\\": [11, 12], \\\"id\\\": \\\"147c39132a2aae0eac64b81904c284b9\\\"}, {\\\"trigger_word\\\": \\\"Showtime\\\", \\\"sent_id\\\": 19, \\\"offset\\\": [12, 13], \\\"id\\\": \\\"a38bb49aac7ac2aab98309f227818e21\\\"}, {\\\"trigger_word\\\": \\\"live\\\", \\\"sent_id\\\": 19, \\\"offset\\\": [15, 16], \\\"id\\\": \\\"2f7f1d1004ecc94b7fc5c49ce490a442\\\"}, {\\\"trigger_word\\\": \\\"CD/DVD\\\", \\\"sent_id\\\": 19, \\\"offset\\\": [16, 17], \\\"id\\\": \\\"50c14f6e06b84d96c9db427bd6f2e593\\\"}, {\\\"trigger_word\\\": \\\"Blu-ray\\\", \\\"sent_id\\\": 19, \\\"offset\\\": [18, 19], \\\"id\\\": \\\"09bc0693163025380a7eedf4216b3fdb\\\"}, {\\\"trigger_word\\\": \\\"released\\\", \\\"sent_id\\\": 19, \\\"offset\\\": [20, 21], \\\"id\\\": \\\"5da1cbdbe83a82c70ab21696c0980053\\\"}, {\\\"trigger_word\\\": \\\"September\\\", \\\"sent_id\\\": 19, \\\"offset\\\": [22, 23], \\\"id\\\": \\\"e2433774653cdef55c0584bc058f51fd\\\"}]}\\n/root/schema-dag-extraction/data/maven/test.jsonl:521:{\\\"title\\\": \\\"Operation Cobra\\\", \\\"id\\\": \\\"19c145f04a911b1c8414569637557a31\\\", \\\"content\\\": [{\\\"sentence\\\": \\\"Operation Cobra was the codename for an offensive launched by the First United States Army (Lieutenant General Omar Bradley) seven weeks after the D-Day landings, during the Normandy Campaign of World War II.\\\", \\\"tokens\\\": [\\\"Operation\\\", \\\"Cobra\\\", \\\"was\\\", \\\"the\\\", \\\"codename\\\", \\\"for\\\", \\\"an\\\", \\\"offensive\\\", \\\"launched\\\", \\\"by\\\", \\\"the\\\", \\\"First\\\", \\\"United\\\", \\\"States\\\", \\\"Army\\\", \\\"(\\\", \\\"Lieutenant\\\", \\\"General\\\", \\\"Omar\\\", \\\"Bradley\\\", \\\")\\\", \\\"seven\\\", \\\"weeks\\\", \\\"after\\\", \\\"the\\\", \\\"D-Day\\\", \\\"landings\\\", \\\",\\\", \\\"during\\\", \\\"the\\\", \\\"Normandy\\\", \\\"Campaign\\\", \\\"of\\\", \\\"World\\\", \\\"War\\\", \\\"II\\\", \\\".\\\"]}, {\\\"sentence\\\": \\\"The intention was to take advantage of the distraction of the Germans by the British and Canadian attacks around Caen, in Operation Goodwood and break through the German defenses that were penning in his troops, while the Germans were unbalanced.\\\", \\\"tokens\\\": [\\\"The\\\", \\\"intention\\\", \\\"was\\\", \\\"to\\\", \\\"take\\\", \\\"advantage\\\", \\\"of\\\", \\\"the\\\", \\\"distraction\\\", \\\"of\\\", \\\"the\\\", \\\"Germans\\\", \\\"by\\\", \\\"the\\\", \\\"British\\\", \\\"and\\\", \\\"Canadian\\\", \\\"attacks\\\", \\\"around\\\", \\\"Caen\\\", \\\",\\\", \\\"in\\\", \\\"Operation\\\", \\\"Goodwood\\\", \\\"and\\\", \\\"break\\\", \\\"through\\\", \\\"the\\\", \\\"German\\\", \\\"defenses\\\", \\\"that\\\", \\\"were\\\", \\\"penning\\\", \\\"in\\\", \\\"his\\\", \\\"troops\\\", \\\",\\\", \\\"while\\\", \\\"the\\\", \\\"Germans\\\", \\\"were\\\", \\\"unbalanced\\\", \\\".\\\"]}, {\\\"sentence\\\": \\\"Once a corridor had been created, the First Army would then be able to advance into Brittany, rolling up the German flanks once free of the constraints of the bocage country.\\\", \\\"tokens\\\": [\\\"Once\\\", \\\"a\\\", \\\"corridor\\\", \\\"had\\\", \\\"been\\\", \\\"created\\\", \\\",\\\", \\\"the\\\", \\\"First\\\", \\\"Army\\\", \\\"would\\\", \\\"then\\\", \\\"be\\\", \\\"able\\\", \\\"to\\\", \\\"advance\\\", \\\"into\\\", \\\"Brittany\\\", \\\",\\\", \\\"rolling\\\", \\\"up\\\", \\\"the\\\", \\\"German\\\", \\\"flanks\\\", \\\"once\\\", \\\"free\\\", \\\"of\\\", \\\"the\\\", \\\"constraints\\\", \\\"of\\\", \\\"the\\\", \\\"bocage\\\", \\\"country\\\", \\\".\\\"]}, {\\\"sentence\\\": \\\"After a slow start the offensive gathered momentum and German resistance collapsed as scattered remnants of broken units fought to escape to the Seine.\\\", \\\"tokens\\\": [\\\"After\\\", \\\"a\\\", \\\"slow\\\", \\\"start\\\", \\\"the\\\", \\\"offensive\\\", \\\"gathered\\\", \\\"momentum\\\", \\\"and\\\", \\\"German\\\", \\\"resistance\\\", \\\"collapsed\\\", \\\"as\\\", \\\"scattered\\\", \\\"remnants\\\", \\\"of\\\", \\\"broken\\\", \\\"units\\\", \\\"fought\\\", \\\"to\\\", \\\"escape\\\", \\\"to\\\", \\\"the\\\", \\\"Seine\\\", \\\".\\\"]}, {\\\"sentence\\\": \\\"Lacking the resources to cope with the situation, the German response was ineffectual and the entire Normandy front soon collapsed.\\\", \\\"tokens\\\": [\\\"Lacking\\\", \\\"the\\\", \\\"resources\\\", \\\"to\\\", \\\"cope\\\", \\\"with\\\", \\\"the\\\", \\\"situation\\\", \\\",\\\", \\\"the\\\", \\\"German\\\", \\\"response\\\", \\\"was\\\", \\\"ineffectual\\\", \\\"and\\\", \\\"the\\\", \\\"entire\\\", \\\"Normandy\\\", \\\"front\\\", \\\"soon\\\", \\\"collapsed\\\", \\\".\\\"]}, {\\\"sentence\\\": \\\"Operation Cobra, together with concurrent offensives by the British Second Army and the Canadian First Army, was decisive in securing an Allied victory in the Normandy Campaign.\\\", \\\"tokens\\\": [\\\"Operation\\\", \\\"Cobra\\\", \\\",\\\", \\\"together\\\", \\\"with\\\", \\\"concurrent\\\", \\\"offensives\\\", \\\"by\\\", \\\"the\\\", \\\"British\\\", \\\"Second\\\", \\\"Army\\\", \\\"and\\\", \\\"the\\\", \\\"Canadian\\\", \\\"First\\\", \\\"Army\\\", \\\",\\\", \\\"was\\\", \\\"decisive\\\", \\\"in\\\", \\\"securing\\\", \\\"an\\\", \\\"Allied\\\", \\\"victory\\\", \\\"in\\\", \\\"the\\\", \\\"Normandy\\\", \\\"Campaign\\\", \\\".\\\"]}, {\\\"sentence\\\": \\\"Having been delayed several times by poor weather, Operation Cobra commenced on 25 July, with a concentrated aerial bombardment from thousands of Allied aircraft.\\\", \\\"tokens\\\": [\\\"Having\\\", \\\"been\\\", \\\"delayed\\\", \\\"several\\\", \\\"times\\\", \\\"by\\\", \\\"poor\\\", \\\"weather\\\", \\\",\\\", \\\"Operation\\\", \\\"Cobra\\\", \\\"commenced\\\", \\\"on\\\", \\\"25\\\", \\\"July\\\", \\\",\\\", \\\"with\\\", \\\"a\\\", \\\"concentrated\\\", \\\"aerial\\\", \\\"bombardment\\\", \\\"from\\\", \\\"thousands\\\", \\\"of\\\", \\\"Allied\\\", \\\"aircraft\\\", \\\".\\\"]}, {\\\"sentence\\\": \\\"Supporting offensives had drawn the bulk of German armored reserves toward the British and Canadian sector and coupled with the general lack of men and materiel available to the Germans, it was impossible for them to form successive lines of defense.\\\", \\\"tokens\\\": [\\\"Supporting\\\", \\\"offensives\\\", \\\"had\\\", \\\"drawn\\\", \\\"the\\\", \\\"bulk\\\", \\\"of\\\", \\\"German\\\", \\\"armored\\\", \\\"reserves\\\", \\\"toward\\\", \\\"the\\\", \\\"British\\\", \\\"and\\\", \\\"Canadian\\\", \\\"sector\\\", \\\"and\\\", \\\"coupled\\\", \\\"with\\\", \\\"the\\\", \\\"general\\\", \\\"lack\\\", \\\"of\\\", \\\"men\\\", \\\"and\\\", \\\"materiel\\\", \\\"available\\\", \\\"to\\\", \\\"the\\\", \\\"Germans\\\", \\\",\\\", \\\"it\\\", \\\"was\\\", \\\"impossible\\\", \\\"for\\\", \\\"them\\\", \\\"to\\\", \\\"form\\\", \\\"successive\\\", \\\"lines\\\", \\\"of\\\", \\\"defense\\\", \\\".\\\"]}, {\\\"sentence\\\": \\\"Units of the U.S. VII Corps led the initial two-division assault, while other First U.S. Army corps mounted supporting attacks designed to pin German units in place.\\\", \\\"tokens\\\": [\\\"Units\\\", \\\"of\\\", \\\"the\\\", \\\"U.S.\\\", \\\"VII\\\", \\\"Corps\\\", \\\"led\\\", \\\"the\\\", \\\"initial\\\", \\\"two-division\\\", \\\"assault\\\", \\\",\\\", \\\"while\\\", \\\"other\\\", \\\"First\\\", \\\"U.S.\\\", \\\"Army\\\", \\\"corps\\\", \\\"mounted\\\", \\\"supporting\\\", \\\"attacks\\\", \\\"designed\\\", \\\"to\\\", \\\"pin\\\", \\\"German\\\", \\\"units\\\", \\\"in\\\", \\\"place\\\", \\\".\\\"]}, {\\\"sentence\\\": \\\"Progress was slow on the first day but opposition started to crumble once the defensive crust had been broken.\\\", \\\"tokens\\\": [\\\"Progress\\\", \\\"was\\\", \\\"slow\\\", \\\"on\\\", \\\"the\\\", \\\"first\\\", \\\"day\\\", \\\"but\\\", \\\"opposition\\\", \\\"started\\\", \\\"to\\\", \\\"crumble\\\", \\\"once\\\", \\\"the\\\", \\\"defensive\\\", \\\"crust\\\", \\\"had\\\", \\\"been\\\", \\\"broken\\\", \\\".\\\"]}, {\\\"sentence\\\": \\\"By 27 July, most organized resistance had been overcome and the VII and VIII Corps advanced rapidly, isolating the Cotentin Peninsula.\\\", \\\"tokens\\\": [\\\"By\\\", \\\"27\\\", \\\"July\\\", \\\",\\\", \\\"most\\\", \\\"organized\\\", \\\"resistance\\\", \\\"had\\\", \\\"been\\\", \\\"overcome\\\", \\\"and\\\", \\\"the\\\", \\\"VII\\\", \\\"and\\\", \\\"VIII\\\", \\\"Corps\\\", \\\"advanced\\\", \\\"rapidly\\\", \\\",\\\", \\\"isolating\\\", \\\"the\\\", \\\"Cotentin\\\", \\\"Peninsula\\\", \\\".\\\"]}, {\\\"sentence\\\": \\\"By 31 July, XIX Corps had destroyed the last forces opposing the First Army, which emerged from the bocage.\\\", \\\"tokens\\\": [\\\"By\\\", \\\"31\\\", \\\"July\\\", \\\",\\\", \\\"XIX\\\", \\\"Corps\\\", \\\"had\\\", \\\"destroyed\\\", \\\"the\\\", \\\"last\\\", \\\"forces\\\", \\\"opposing\\\", \\\"the\\\", \\\"First\\\", \\\"Army\\\", \\\",\\\", \\\"which\\\", \\\"emerged\\\", \\\"from\\\", \\\"the\\\", \\\"bocage\\\", \\\".\\\"]}, {\\\"sentence\\\": \\\"Reinforcements were moved west by Field Marshal Günther von Kluge and employed in various counterattacks, the largest of which, \\\\\\\"Unternehmen Lüttich\\\\\\\" (Operation Liège), was launched on 7 August between Mortain and Avranches.\\\", \\\"tokens\\\": [\\\"Reinforcements\\\", \\\"were\\\", \\\"moved\\\", \\\"west\\\", \\\"by\\\", \\\"Field\\\", \\\"Marshal\\\", \\\"Günther\\\", \\\"von\\\", \\\"Kluge\\\", \\\"and\\\", \\\"employed\\\", \\\"in\\\", \\\"various\\\", \\\"counterattacks\\\", \\\",\\\", \\\"the\\\", \\\"largest\\\", \\\"of\\\", \\\"which\\\", \\\",\\\", \\\"``\\\", \\\"Unternehmen\\\", \\\"Lüttich\\\", \\\"''\\\", \\\"(\\\", \\\"Operation\\\", \\\"Liège\\\", \\\")\\\", \\\",\\\", \\\"was\\\", \\\"launched\\\", \\\"on\\\", \\\"7\\\", \\\"August\\\", \\\"between\\\", \\\"Mortain\\\", \\\"and\\\", \\\"Avranches\\\", \\\".\\\"]}, {\\\"sentence\\\": \\\"Although this led to the bloodiest phase of the battle, it was mounted by already exhausted and understrength units and was a costly failure.\\\", \\\"tokens\\\": [\\\"although\\\", \\\"this\\\", \\\"led\\\", \\\"to\\\", \\\"the\\\", \\\"bloodiest\\\", \\\"phase\\\", \\\"of\\\", \\\"the\\\", \\\"battle\\\", \\\",\\\", \\\"it\\\", \\\"was\\\", \\\"mounted\\\", \\\"by\\\", \\\"already\\\", \\\"exhausted\\\", \\\"and\\\", \\\"understrength\\\", \\\"units\\\", \\\"and\\\", \\\"was\\\", \\\"a\\\", \\\"costly\\\", \\\"failure\\\", \\\".\\\"]}, {\\\"sentence\\\": \\\"On 8 August, troops of the newly activated Third United States Army captured the city of Le Mans, formerly the German 7th Army headquarters.\\\", \\\"tokens\\\": [\\\"On\\\", \\\"8\\\", \\\"August\\\", \\\",\\\", \\\"troops\\\", \\\"of\\\", \\\"the\\\", \\\"newly\\\", \\\"activated\\\", \\\"Third\\\", \\\"United\\\", \\\"States\\\", \\\"Army\\\", \\\"captured\\\", \\\"the\\\", \\\"city\\\", \\\"of\\\", \\\"Le\\\", \\\"Mans\\\", \\\",\\\", \\\"formerly\\\", \\\"the\\\", \\\"German\\\", \\\"7th\\\", \\\"Army\\\", \\\"headquarters\\\", \\\".\\\"]}, {\\\"sentence\\\": \\\"Operation Cobra transformed the high-intensity infantry combat of Normandy into rapid maneuver warfare and led to the creation of the Falaise pocket and the loss of the German position in northwestern France.\\\", \\\"tokens\\\": [\\\"Operation\\\", \\\"Cobra\\\", \\\"transformed\\\", \\\"the\\\", \\\"high-intensity\\\", \\\"infantry\\\", \\\"combat\\\", \\\"of\\\", \\\"Normandy\\\", \\\"into\\\", \\\"rapid\\\", \\\"maneuver\\\", \\\"warfare\\\", \\\"and\\\", \\\"led\\\", \\\"to\\\", \\\"the\\\", \\\"creation\\\", \\\"of\\\", \\\"the\\\", \\\"Falaise\\\", \\\"pocket\\\", \\\"and\\\", \\\"the\\\", \\\"loss\\\", \\\"of\\\", \\\"the\\\", \\\"German\\\", \\\"position\\\", \\\"in\\\", \\\"northwestern\\\", \\\"France\\\", \\\".\\\"]}], \\\"candidates\\\": [{\\\"trigger_word\\\": \\\"Operation\\\", \\\"sent_id\\\": 0, \\\"offset\\\": [0, 1], \\\"id\\\": \\\"62d1cefc694de5e51aba6afad7510cb8\\\"}, {\\\"trigger_word\\\": \\\"Cobra\\\", \\\"sent_id\\\": 0, \\\"offset\\\": [1, 2], \\\"id\\\": \\\"ce65769224c9362dea43ed98e149ba72\\\"}, {\\\"trigger_word\\\": \\\"codename\\\", \\\"sent_id\\\": 0, \\\"offset\\\": [4, 5], \\\"id\\\": \\\"62d8b98bb39d42d166f94281faf716e7\\\"}, {\\\"trigger_word\\\": \\\"offensive\\\", \\\"sent_id\\\": 0, \\\"offset\\\": [7, 8], \\\"id\\\": \\\"92678237771eb3e3d77da365ef22fbd4\\\"}, {\\\"trigger_word\\\": \\\"launched\\\", \\\"sent_id\\\": 0, \\\"offset\\\": [8, 9], \\\"id\\\": \\\"1d0123c080893e291ffb29e14e58effa\\\"}, {\\\"trigger_word\\\": \\\"First\\\", \\\"sent_id\\\": 0, \\\"offset\\\": [11, 12], \\\"id\\\": \\\"94ebd77d8ee73632d8c73b44ae6dc284\\\"}, {\\\"trigger_word\\\": \\\"United\\\", \\\"sent_id\\\": 0, \\\"offset\\\": [12, 13], \\\"id\\\": \\\"ea3f407e9ab4b9e66321175d350bc844\\\"}, {\\\"trigger_word\\\": \\\"States\\\", \\\"sent_id\\\": 0, \\\"offset\\\": [13, 14], \\\"id\\\": \\\"f52aac645248d71ccfdb308c9e74ccc1\\\"}, {\\\"trigger_word\\\": \\\"Army\\\", \\\"sent_id\\\": 0, \\\"offset\\\": [14, 15], \\\"id\\\": \\\"6e498df8a2124c282ccdf656e22bc56c\\\"}, {\\\"trigger_word\\\": \\\"Lieutenant\\\", \\\"sent_id\\\": 0, \\\"offset\\\": [16, 17], \\\"id\\\": \\\"c3452316b5475e32dc5610cf5c5f4790\\\"}, {\\\"trigger_word\\\": \\\"General\\\", \\\"sent_id\\\": 0, \\\"offset\\\": [17, 18], \\\"id\\\": \\\"f1a433f4de5a5e291f37b333bf6a7154\\\"}, {\\\"trigger_word\\\": \\\"Omar\\\", \\\"sent_id\\\": 0, \\\"offset\\\": [18, 19], \\\"id\\\": \\\"4ab1c4bbb3cd45be710bb43955f31133\\\"}, {\\\"trigger_word\\\": \\\"Bradley\\\", \\\"sent_id\\\": 0, \\\"offset\\\": [19, 20], \\\"id\\\": \\\"6abb16ab7fcca450727e403d355fb9c9\\\"}, {\\\"trigger_word\\\": \\\"weeks\\\", \\\"sent_id\\\": 0, \\\"offset\\\": [22, 23], \\\"id\\\": \\\"ecb50a9b0035df7615df4478df94bd3f\\\"}, {\\\"trigger_word\\\": \\\"D-Day\\\", \\\"sent_id\\\": 0, \\\"offset\\\": [25, 26], \\\"id\\\": \\\"3dd5e2d9772492cf07af14e825266af6\\\"}, {\\\"trigger_word\\\": \\\"landings\\\", \\\"sent_id\\\": 0, \\\"offset\\\": [26, 27], \\\"id\\\": \\\"b45a68f5b14288698f3f580099f92af9\\\"}, {\\\"trigger_word\\\": \\\"Normandy\\\", \\\"sent_id\\\": 0, \\\"offset\\\": [30, 31], \\\"id\\\": \\\"7e28f18be9149fa51134af0701308bce\\\"}, {\\\"trigger_word\\\": \\\"Campaign\\\", \\\"sent_id\\\": 0, \\\"offset\\\": [31, 32], \\\"id\\\": \\\"d8f8c12c89ab3926cf15c33daf1230ba\\\"}, {\\\"trigger_word\\\": \\\"World\\\", \\\"sent_id\\\": 0, \\\"offset\\\": [33, 34], \\\"id\\\": \\\"4d1760b37115620a520f592d157f05e3\\\"}, {\\\"trigger_word\\\": \\\"War\\\", \\\"sent_id\\\": 0, \\\"offset\\\": [34, 35], \\\"id\\\": \\\"93759c4cda917f0f199acf2a5b58010c\\\"}, {\\\"trigger_word\\\": \\\"II\\\", \\\"sent_id\\\": 0, \\\"offset\\\": [35, 36], \\\"id\\\": \\\"9191a46973528a8b9eb1f38d3f096b3e\\\"}, {\\\"trigger_word\\\": \\\"intention\\\", \\\"sent_id\\\": 1, \\\"offset\\\": [1, 2], \\\"id\\\": \\\"674c9e1c739ae01b5f0f87a7079b4c03\\\"}, {\\\"trigger_word\\\": \\\"take\\\", \\\"sent_id\\\": 1, \\\"offset\\\": [4, 5], \\\"id\\\": \\\"72f4b5481575ca258f2ada61ec10fc8e\\\"}, {\\\"trigger_word\\\": \\\"advantage\\\", \\\"sent_id\\\": 1, \\\"offset\\\": [5, 6], \\\"id\\\": \\\"1084144ac530c5b4b626f092e5f8502e\\\"}, {\\\"trigger_word\\\": \\\"distraction\\\", \\\"sent_id\\\": 1, \\\"offset\\\": [8, 9], \\\"id\\\": \\\"5afc071c99aa0897fc23e59818366e7e\\\"}, {\\\"trigger_word\\\": \\\"Germans\\\", \\\"sent_id\\\": 1, \\\"offset\\\": [11, 12], \\\"id\\\": \\\"9fd0d1b897cb3ff469420fb7227498f6\\\"}, {\\\"trigger_word\\\": \\\"British\\\", \\\"sent_id\\\": 1, \\\"offset\\\": [14, 15], \\\"id\\\": \\\"7e0099205397a3ca000a5499248e0522\\\"}, {\\\"trigger_word\\\": \\\"Canadian\\\", \\\"sent_id\\\": 1, \\\"offset\\\": [16, 17], \\\"id\\\": \\\"21505b9b2934c16476c3d30814cb6e89\\\"}, {\\\"trigger_word\\\": \\\"attacks\\\", \\\"sent_id\\\": 1, \\\"offset\\\": [17, 18], \\\"id\\\": \\\"8d4c9be1609a2a27f373e37145e514a8\\\"}, {\\\"trigger_word\\\": \\\"Caen\\\", \\\"sent_id\\\": 1, \\\"offset\\\": [19, 20], \\\"id\\\": \\\"1224205571bb0cb5022a01ee729d1fa7\\\"}, {\\\"trigger_word\\\": \\\"Operation\\\", \\\"sent_id\\\": 1, \\\"offset\\\": [22, 23], \\\"id\\\": \\\"cd620b993d07fd34c65a9cdb47ff3c54\\\"}, {\\\"trigger_word\\\": \\\"Goodwood\\\", \\\"sent_id\\\": 1, \\\"offset\\\": [23, 24], \\\"id\\\": \\\"0eba37b555949f4a7ae10b7c88136591\\\"}, {\\\"trigger_word\\\": \\\"break\\\", \\\"sent_id\\\": 1, \\\"offset\\\": [25, 26], \\\"id\\\": \\\"bba9a446c235dcc37ace9d36ce64995f\\\"}, {\\\"trigger_word\\\": \\\"German\\\", \\\"sent_id\\\": 1, \\\"offset\\\": [28, 29], \\\"id\\\": \\\"5c766fc8619862750fac5d264e1ed97e\\\"}, {\\\"trigger_word\\\": \\\"defenses\\\", \\\"sent_id\\\": 1, \\\"offset\\\": [29, 30], \\\"id\\\": \\\"23edece67c0eebc202c8a6bce66efafa\\\"}, {\\\"trigger_word\\\": \\\"penning\\\", \\\"sent_id\\\": 1, \\\"offset\\\": [32, 33], \\\"id\\\": \\\"d255e716424ee5b191c80d7fadc64d2e\\\"}, {\\\"trigger_word\\\": \\\"troops\\\", \\\"sent_id\\\": 1, \\\"offset\\\": [35, 36], \\\"id\\\": \\\"7f456be26391ff78bc67c5b363d216e9\\\"}, {\\\"trigger_word\\\": \\\"Germans\\\", \\\"sent_id\\\": 1, \\\"offset\\\": [39, 40], \\\"id\\\": \\\"2cb3787b561f5065abe074b2420553a0\\\"}, {\\\"trigger_word\\\": \\\"unbalanced\\\", \\\"sent_id\\\": 1, \\\"offset\\\": [41, 42], \\\"id\\\": \\\"2905738f1aa2783746033d39b71d2728\\\"}, {\\\"trigger_word\\\": \\\"Once\\\", \\\"sent_id\\\": 2, \\\"offset\\\": [0, 1], \\\"id\\\": \\\"82589f47ec22a4f80b0c5cbf5624f7e4\\\"}, {\\\"trigger_word\\\": \\\"corridor\\\", \\\"sent_id\\\": 2, \\\"offset\\\": [2, 3], \\\"id\\\": \\\"44f88d6e6434332dc8e0425ec5564096\\\"}, {\\\"trigger_word\\\": \\\"created\\\", \\\"sent_id\\\": 2, \\\"offset\\\": [5, 6], \\\"id\\\": \\\"b282f7213c393c57e147f36aa7b05448\\\"}, {\\\"trigger_word\\\": \\\"First\\\", \\\"sent_id\\\": 2, \\\"offset\\\": [8, 9], \\\"id\\\": \\\"524be324139b783286aa608fe0226a07\\\"}, {\\\"trigger_word\\\": \\\"Army\\\", \\\"sent_id\\\": 2, \\\"offset\\\": [9, 10], \\\"id\\\": \\\"8216cd5b129a2117480f49690b672b63\\\"}, {\\\"trigger_word\\\": \\\"able\\\", \\\"sent_id\\\": 2, \\\"offset\\\": [13, 14], \\\"id\\\": \\\"982e0e8b863ffe55dcddee4324dccfa0\\\"}, {\\\"trigger_word\\\": \\\"advance\\\", \\\"sent_id\\\": 2, \\\"offset\\\": [15, 16], \\\"id\\\": \\\"7ae4920d83acbcda644afac6101fb08a\\\"}, {\\\"trigger_word\\\": \\\"Brittany\\\", \\\"sent_id\\\": 2, \\\"offset\\\": [17, 18], \\\"id\\\": \\\"c8db84d0a4f4fc06125669af8eed513b\\\"}, {\\\"trigger_word\\\": \\\"rolling\\\", \\\"sent_id\\\": 2, \\\"offset\\\": [19, 20], \\\"id\\\": \\\"19032bd636d21f16d00d52ba7be52f2e\\\"}, {\\\"trigger_word\\\": \\\"German\\\", \\\"sent_id\\\": 2, \\\"offset\\\": [22, 23], \\\"id\\\": \\\"743855d5905d6b5007dc5edd15ecf860\\\"}, {\\\"trigger_word\\\": \\\"flanks\\\", \\\"sent_id\\\": 2, \\\"offset\\\": [23, 24], \\\"id\\\": \\\"3faaf8018dffe26dedea3a1422baa2a4\\\"}, {\\\"trigger_word\\\": \\\"free\\\", \\\"sent_id\\\": 2, \\\"offset\\\": [25, 26], \\\"id\\\": \\\"aa53c181b479b31a15255d72ee273d71\\\"}, {\\\"trigger_word\\\": \\\"constraints\\\", \\\"sent_id\\\": 2, \\\"offset\\\": [28, 29], \\\"id\\\": \\\"ff29ee690ff85c9de1fb1e652314da3a\\\"}, {\\\"trigger_word\\\": \\\"bocage\\\", \\\"sent_id\\\": 2, \\\"offset\\\": [31, 32], \\\"id\\\": \\\"031fcbfca324042eb109a4b04ad4ae0b\\\"}, {\\\"trigger_word\\\": \\\"country\\\", \\\"sent_id\\\": 2, \\\"offset\\\": [32, 33], \\\"id\\\": \\\"041ddbbd10ffea042dbd5388582e6752\\\"}, {\\\"trigger_word\\\": \\\"slow\\\", \\\"sent_id\\\": 3, \\\"offset\\\": [2, 3], \\\"id\\\": \\\"266888ca2ae16d354254a426c465e90f\\\"}, {\\\"trigger_word\\\": \\\"start\\\", \\\"sent_id\\\": 3, \\\"offset\\\": [3, 4], \\\"id\\\": \\\"3df10d79a78a6c5e2596649bc0e9c716\\\"}, {\\\"trigger_word\\\": \\\"offensive\\\", \\\"sent_id\\\": 3, \\\"offset\\\": [5, 6], \\\"id\\\": \\\"0fa1edb89b750dea091859f82c0f3d72\\\"}, {\\\"trigger_word\\\": \\\"gathered\\\", \\\"sent_id\\\": 3, \\\"offset\\\": [6, 7], \\\"id\\\": \\\"8dbdbc2130cbc05021a83e62e0cc0e7e\\\"}, {\\\"trigger_word\\\": \\\"momentum\\\", \\\"sent_id\\\": 3, \\\"offset\\\": [7, 8], \\\"id\\\": \\\"cdb8909ad22fe4becaa6af204e91c126\\\"}, {\\\"trigger_word\\\": \\\"German\\\", \\\"sent_id\\\": 3, \\\"offset\\\": [9, 10], \\\"id\\\": \\\"f895dc5b3c9e1f1b350bccb6f37e27c0\\\"}, {\\\"trigger_word\\\": \\\"resistance\\\", \\\"sent_id\\\": 3, \\\"offset\\\": [10, 11], \\\"id\\\": \\\"76686ad8e92c8e0295176bcd8965e4a5\\\"}, {\\\"trigger_word\\\": \\\"collapsed\\\", \\\"sent_id\\\": 3, \\\"offset\\\": [11, 12], \\\"id\\\": \\\"ec69fc8c1993521072b786bff30d5d5d\\\"}, {\\\"trigger_word\\\": \\\"scattered\\\", \\\"sent_id\\\": 3, \\\"offset\\\": [13, 14], \\\"id\\\": \\\"b393528aef7fbfee4543164e0167102b\\\"}, {\\\"trigger_word\\\": \\\"remnants\\\", \\\"sent_id\\\": 3, \\\"offset\\\": [14, 15], \\\"id\\\": \\\"f2de6ac0a3c9a61892bd8b071b9cf5b5\\\"}, {\\\"trigger_word\\\": \\\"broken\\\", \\\"sent_id\\\": 3, \\\"offset\\\": [16, 17], \\\"id\\\": \\\"122e62d75cc3231bc798291e5489b6e5\\\"}, {\\\"trigger_word\\\": \\\"units\\\", \\\"sent_id\\\": 3, \\\"offset\\\": [17, 18], \\\"id\\\": \\\"7e22e5bdce56d47808d938ce2ec82094\\\"}, {\\\"trigger_word\\\": \\\"fought\\\", \\\"sent_id\\\": 3, \\\"offset\\\": [18, 19], \\\"id\\\": \\\"2482e42d7b0cab667f8c33a63737e79e\\\"}, {\\\"trigger_word\\\": \\\"escape\\\", \\\"sent_id\\\": 3, \\\"offset\\\": [20, 21], \\\"id\\\": \\\"618bfea18d1e0419520a6b943067937c\\\"}, {\\\"trigger_word\\\": \\\"Seine\\\", \\\"sent_id\\\": 3, \\\"offset\\\": [23, 24], \\\"id\\\": \\\"322aaf08fc1c56e436c7dfb52d7253b4\\\"}, {\\\"trigger_word\\\": \\\"Lacking\\\", \\\"sent_id\\\": 4, \\\"offset\\\": [0, 1], \\\"id\\\": \\\"ff9463b55de5e480105931767693b5a8\\\"}, {\\\"trigger_word\\\": \\\"resources\\\", \\\"sent_id\\\": 4, \\\"offset\\\": [2, 3], \\\"id\\\": \\\"87d9c17c87568140946f164b83d3ece4\\\"}, {\\\"trigger_word\\\": \\\"cope\\\", \\\"sent_id\\\": 4, \\\"offset\\\": [4, 5], \\\"id\\\": \\\"c87ca61c5ff0a10df4a83a82cdffae21\\\"}, {\\\"trigger_word\\\": \\\"situation\\\", \\\"sent_id\\\": 4, \\\"offset\\\": [7, 8], \\\"id\\\": \\\"af9bfcec2f6fd7e903539725010eb912\\\"}, {\\\"trigger_word\\\": \\\"German\\\", \\\"sent_id\\\": 4, \\\"offset\\\": [10, 11], \\\"id\\\": \\\"bbcbec4c880a407cd95f52bbf9ba77d9\\\"}, {\\\"trigger_word\\\": \\\"response\\\", \\\"sent_id\\\": 4, \\\"offset\\\": [11, 12], \\\"id\\\": \\\"00600c43c5ac05d5677a8c814dd5925d\\\"}, {\\\"trigger_word\\\": \\\"ineffectual\\\", \\\"sent_id\\\": 4, \\\"offset\\\": [13, 14], \\\"id\\\": \\\"12d7ecd2418e7d1887cc4e429e3255a2\\\"}, {\\\"trigger_word\\\": \\\"entire\\\", \\\"sent_id\\\": 4, \\\"offset\\\": [16, 17], \\\"id\\\": \\\"7ae726fb29abd1b7ce798fa7a0e87571\\\"}, {\\\"trigger_word\\\": \\\"Normandy\\\", \\\"sent_id\\\": 4, \\\"offset\\\": [17, 18], \\\"id\\\": \\\"9602c46a7a5352e56cd835f2925a6d6e\\\"}, {\\\"trigger_word\\\": \\\"front\\\", \\\"sent_id\\\": 4, \\\"offset\\\": [18, 19], \\\"id\\\": \\\"2f899d54bcbafa5a3610b4df7429716e\\\"}, {\\\"trigger_word\\\": \\\"soon\\\", \\\"sent_id\\\": 4, \\\"offset\\\": [19, 20], \\\"id\\\": \\\"e5656675e8140d1e4efbfdd1bb628460\\\"}, {\\\"trigger_word\\\": \\\"collapsed\\\", \\\"sent_id\\\": 4, \\\"offset\\\": [20, 21], \\\"id\\\": \\\"be83ead27e54cc76356d241ba322905d\\\"}, {\\\"trigger_word\\\": \\\"Operation\\\", \\\"sent_id\\\": 5, \\\"offset\\\": [0, 1], \\\"id\\\": \\\"1269f16467ba64b559805e923e8388c9\\\"}, {\\\"trigger_word\\\": \\\"Cobra\\\", \\\"sent_id\\\": 5, \\\"offset\\\": [1, 2], \\\"id\\\": \\\"d17ab967fc72927ba5fa8b888f6b1152\\\"}, {\\\"trigger_word\\\": \\\"together\\\", \\\"sent_id\\\": 5, \\\"offset\\\": [3, 4], \\\"id\\\": \\\"4325ba90542982e9a96d6305ed64161c\\\"}, {\\\"trigger_word\\\": \\\"concurrent\\\", \\\"sent_id\\\": 5, \\\"offset\\\": [5, 6], \\\"id\\\": \\\"ae6fec63ed84368fa6ba3ad64b72d55d\\\"}, {\\\"trigger_word\\\": \\\"offensives\\\", \\\"sent_id\\\": 5, \\\"offset\\\": [6, 7], \\\"id\\\": \\\"8898e87cacf4d0dcfe8ff792b78f0351\\\"}, {\\\"trigger_word\\\": \\\"British\\\", \\\"sent_id\\\": 5, \\\"offset\\\": [9, 10], \\\"id\\\": \\\"e4db3430d4f83673dd08aac6582fee40\\\"}, {\\\"trigger_word\\\": \\\"Second\\\", \\\"sent_id\\\": 5, \\\"offset\\\": [10, 11], \\\"id\\\": \\\"6b2da944e7b7674115dadb1560709a22\\\"}, {\\\"trigger_word\\\": \\\"Army\\\", \\\"sent_id\\\": 5, \\\"offset\\\": [11, 12], \\\"id\\\": \\\"8447418e5bc5c9d6bff381be7fb7c350\\\"}, {\\\"trigger_word\\\": \\\"Canadian\\\", \\\"sent_id\\\": 5, \\\"offset\\\": [14, 15], \\\"id\\\": \\\"5ccc75c7b2be2db20864696562f581bf\\\"}, {\\\"trigger_word\\\": \\\"First\\\", \\\"sent_id\\\": 5, \\\"offset\\\": [15, 16], \\\"id\\\": \\\"9872c4fc415d99605b057844f83b3d1f\\\"}, {\\\"trigger_word\\\": \\\"Army\\\", \\\"sent_id\\\": 5, \\\"offset\\\": [16, 17], \\\"id\\\": \\\"c9e443effd6fd971d2a1bc1d0250b1fb\\\"}, {\\\"trigger_word\\\": \\\"decisive\\\", \\\"sent_id\\\": 5, \\\"offset\\\": [19, 20], \\\"id\\\": \\\"ebd8ba7e06a9540390ab75f1ae5034a7\\\"}, {\\\"trigger_word\\\": \\\"securing\\\", \\\"sent_id\\\": 5, \\\"offset\\\": [21, 22], \\\"id\\\": \\\"ef04ea374444b2162c74d7da4dcdc0d5\\\"}, {\\\"trigger_word\\\": \\\"Allied\\\", \\\"sent_id\\\": 5, \\\"offset\\\": [23, 24], \\\"id\\\": \\\"eda560ed0c530bdb2b3241ea3e94befd\\\"}, {\\\"trigger_word\\\": \\\"victory\\\", \\\"sent_id\\\": 5, \\\"offset\\\": [24, 25], \\\"id\\\": \\\"49e1a3960201e7c6173809032d499848\\\"}, {\\\"trigger_word\\\": \\\"Normandy\\\", \\\"sent_id\\\": 5, \\\"offset\\\": [27, 28], \\\"id\\\": \\\"f7906196561f5ec2bf592187f24f1abf\\\"}, {\\\"trigger_word\\\": \\\"Campaign\\\", \\\"sent_id\\\": 5, \\\"offset\\\": [28, 29], \\\"id\\\": \\\"0cf456c261afda6d0762a2e3c5999d7e\\\"}, {\\\"trigger_word\\\": \\\"Having\\\", \\\"sent_id\\\": 6, \\\"offset\\\": [0, 1], \\\"id\\\": \\\"aa4b8b66c7e7954f5782cdb4b54d0c7a\\\"}, {\\\"trigger_word\\\": \\\"delayed\\\", \\\"sent_id\\\": 6, \\\"offset\\\": [2, 3], \\\"id\\\": \\\"097bf82bb5ccb51b21d6b59eb6b08398\\\"}, {\\\"trigger_word\\\": \\\"several\\\", \\\"sent_id\\\": 6, \\\"offset\\\": [3, 4], \\\"id\\\": \\\"cb04e9c596e6be240a070bc7610308af\\\"}, {\\\"trigger_word\\\": \\\"times\\\", \\\"sent_id\\\": 6, \\\"offset\\\": [4, 5], \\\"id\\\": \\\"ca003d9b780665ccd1cad90d8842881f\\\"}, {\\\"trigger_word\\\": \\\"poor\\\", \\\"sent_id\\\": 6, \\\"offset\\\": [6, 7], \\\"id\\\": \\\"5e0c3d04f3525692f2e41039681a40ef\\\"}, {\\\"trigger_word\\\": \\\"weather\\\", \\\"sent_id\\\": 6, \\\"offset\\\": [7, 8], \\\"id\\\": \\\"547b10276e9d7b1e2665452e86543da1\\\"}, {\\\"trigger_word\\\": \\\"Operation\\\", \\\"sent_id\\\": 6, \\\"offset\\\": [9, 10], \\\"id\\\": \\\"0d7e35795b0adc297b9371230034291e\\\"}, {\\\"trigger_word\\\": \\\"Cobra\\\", \\\"sent_id\\\": 6, \\\"offset\\\": [10, 11], \\\"id\\\": \\\"6070d14b09138bd230a1399e1ec38b08\\\"}, {\\\"trigger_word\\\": \\\"commenced\\\", \\\"sent_id\\\": 6, \\\"offset\\\": [11, 12], \\\"id\\\": \\\"627c9fae6db416340e8f00631d5c7d82\\\"}, {\\\"trigger_word\\\": \\\"July\\\", \\\"sent_id\\\": 6, \\\"offset\\\": [14, 15], \\\"id\\\": \\\"0afa7e32cd8da06ac95bde688f6837e4\\\"}, {\\\"trigger_word\\\": \\\"concentrated\\\", \\\"sent_id\\\": 6, \\\"offset\\\": [18, 19], \\\"id\\\": \\\"ac4f59f9012d31585fe016712d725b74\\\"}, {\\\"trigger_word\\\": \\\"aerial\\\", \\\"sent_id\\\": 6, \\\"offset\\\": [19, 20], \\\"id\\\": \\\"9ba1d760bee13ce2d690dd6450cfaca1\\\"}, {\\\"trigger_word\\\": \\\"bombardment\\\", \\\"sent_id\\\": 6, \\\"offset\\\": [20, 21], \\\"id\\\": \\\"de39a043e517af4d5a43c11e9eadf20e\\\"}, {\\\"trigger_word\\\": \\\"thousands\\\", \\\"sent_id\\\": 6, \\\"offset\\\": [22, 23], \\\"id\\\": \\\"76ae8172b8011b144baca9b9b8bde0b4\\\"}, {\\\"trigger_word\\\": \\\"Allied\\\", \\\"sent_id\\\": 6, \\\"offset\\\": [24, 25], \\\"id\\\": \\\"9e0f0475c597f822c50c159b363d19e6\\\"}, {\\\"trigger_word\\\": \\\"aircraft\\\", \\\"sent_id\\\": 6, \\\"offset\\\": [25, 26], \\\"id\\\": \\\"b8953caa0acecbbf9e33ba7057117628\\\"}, {\\\"trigger_word\\\": \\\"Supporting\\\", \\\"sent_id\\\": 7, \\\"offset\\\": [0, 1], \\\"id\\\": \\\"6be50d406b4dc45d93cdb8225b859e14\\\"}, {\\\"trigger_word\\\": \\\"offensives\\\", \\\"sent_id\\\": 7, \\\"offset\\\": [1, 2], \\\"id\\\": \\\"f60b665344baf9c803fb627c31c27b0d\\\"}, {\\\"trigger_word\\\": \\\"drawn\\\", \\\"sent_id\\\": 7, \\\"offset\\\": [3, 4], \\\"id\\\": \\\"5de1e18c469e0a58a46c78283db6f6d9\\\"}, {\\\"trigger_word\\\": \\\"bulk\\\", \\\"sent_id\\\": 7, \\\"offset\\\": [5, 6], \\\"id\\\": \\\"837eeaf2418eb5e76d382841afa7054f\\\"}, {\\\"trigger_word\\\": \\\"German\\\", \\\"sent_id\\\": 7, \\\"offset\\\": [7, 8], \\\"id\\\": \\\"fbea37a7990ee090553349f9bfcaa3a6\\\"}, {\\\"trigger_word\\\": \\\"armored\\\", \\\"sent_id\\\": 7, \\\"offset\\\": [8, 9], \\\"id\\\": \\\"cfd4da86ca629efcc4104cb4e787fa22\\\"}, {\\\"trigger_word\\\": \\\"reserves\\\", \\\"sent_id\\\": 7, \\\"offset\\\": [9, 10], \\\"id\\\": \\\"4cde6ca497c5df940c78135cb5ca90e0\\\"}, {\\\"trigger_word\\\": \\\"British\\\", \\\"sent_id\\\": 7, \\\"offset\\\": [12, 13], \\\"id\\\": \\\"ca7898dcb84508bce3fc5c67b363d49f\\\"}, {\\\"trigger_word\\\": \\\"Canadian\\\", \\\"sent_id\\\": 7, \\\"offset\\\": [14, 15], \\\"id\\\": \\\"23033a0647705770be5f8b197aa8eee6\\\"}, {\\\"trigger_word\\\": \\\"sector\\\", \\\"sent_id\\\": 7, \\\"offset\\\": [15, 16], \\\"id\\\": \\\"e635cb2666668786f9e5559772fe2610\\\"}, {\\\"trigger_word\\\": \\\"coupled\\\", \\\"sent_id\\\": 7, \\\"offset\\\": [17, 18], \\\"id\\\": \\\"6f87ed54023897be85da726f705b2b8e\\\"}, {\\\"trigger_word\\\": \\\"general\\\", \\\"sent_id\\\": 7, \\\"offset\\\": [20, 21], \\\"id\\\": \\\"fd459ea42ad616206f32549c5256ea17\\\"}, {\\\"trigger_word\\\": \\\"lack\\\", \\\"sent_id\\\": 7, \\\"offset\\\": [21, 22], \\\"id\\\": \\\"8cf63974ac8c65e0d62b63cb78482e07\\\"}, {\\\"trigger_word\\\": \\\"men\\\", \\\"sent_id\\\": 7, \\\"offset\\\": [23, 24], \\\"id\\\": \\\"54b91dad727af6f284e3c13f0eb8c9c3\\\"}, {\\\"trigger_word\\\": \\\"materiel\\\", \\\"sent_id\\\": 7, \\\"offset\\\": [25, 26], \\\"id\\\": \\\"788baf7c70debe2662ae79d1881bea04\\\"}, {\\\"trigger_word\\\": \\\"available\\\", \\\"sent_id\\\": 7, \\\"offset\\\": [26, 27], \\\"id\\\": \\\"4c818a146e470a46cf18a4c014afc335\\\"}, {\\\"trigger_word\\\": \\\"Germans\\\", \\\"sent_id\\\": 7, \\\"offset\\\": [29, 30], \\\"id\\\": \\\"d777a893b7b3d92b5556c3f041cdf101\\\"}, {\\\"trigger_word\\\": \\\"impossible\\\", \\\"sent_id\\\": 7, \\\"offset\\\": [33, 34], \\\"id\\\": \\\"1f418a25715a9e0642e3fb0edb90abc3\\\"}, {\\\"trigger_word\\\": \\\"form\\\", \\\"sent_id\\\": 7, \\\"offset\\\": [37, 38], \\\"id\\\": \\\"a9572c29084c7055ab9160e7a1c0001a\\\"}, {\\\"trigger_word\\\": \\\"successive\\\", \\\"sent_id\\\": 7, \\\"offset\\\": [38, 39], \\\"id\\\": \\\"82e8ca845e87e647e08991794617373e\\\"}, {\\\"trigger_word\\\": \\\"lines\\\", \\\"sent_id\\\": 7, \\\"offset\\\": [39, 40], \\\"id\\\": \\\"c06f6b24456a5610f068076383199414\\\"}, {\\\"trigger_word\\\": \\\"defense\\\", \\\"sent_id\\\": 7, \\\"offset\\\": [41, 42], \\\"id\\\": \\\"6c01c2a80a804e6d333dc4e7a406ed65\\\"}, {\\\"trigger_word\\\": \\\"Units\\\", \\\"sent_id\\\": 8, \\\"offset\\\": [0, 1], \\\"id\\\": \\\"a5bc4eca8f2ed6b8f49a141593fbe941\\\"}, {\\\"trigger_word\\\": \\\"U.S.\\\", \\\"sent_id\\\": 8, \\\"offset\\\": [3, 4], \\\"id\\\": \\\"7c0f6df718cdabce383228813b25d16f\\\"}, {\\\"trigger_word\\\": \\\"VII\\\", \\\"sent_id\\\": 8, \\\"offset\\\": [4, 5], \\\"id\\\": \\\"03321fb78c97558097382a323c1312eb\\\"}, {\\\"trigger_word\\\": \\\"Corps\\\", \\\"sent_id\\\": 8, \\\"offset\\\": [5, 6], \\\"id\\\": \\\"4ef51fa50776f6a3f0b5842b6196f7dd\\\"}, {\\\"trigger_word\\\": \\\"led\\\", \\\"sent_id\\\": 8, \\\"offset\\\": [6, 7], \\\"id\\\": \\\"8fa536aa5e3792423111764d9fd53cb9\\\"}, {\\\"trigger_word\\\": \\\"initial\\\", \\\"sent_id\\\": 8, \\\"offset\\\": [8, 9], \\\"id\\\": \\\"15017f01f630f17d5e049bece8842fa9\\\"}, {\\\"trigger_word\\\": \\\"two-division\\\", \\\"sent_id\\\": 8, \\\"offset\\\": [9, 10], \\\"id\\\": \\\"fc186584e58aa130df710bae27253227\\\"}, {\\\"trigger_word\\\": \\\"assault\\\", \\\"sent_id\\\": 8, \\\"offset\\\": [10, 11], \\\"id\\\": \\\"28bf3e901aaabf78e710c3f8517551b2\\\"}, {\\\"trigger_word\\\": \\\"First\\\", \\\"sent_id\\\": 8, \\\"offset\\\": [14, 15], \\\"id\\\": \\\"67f4e662c619bf4436577c805efe693b\\\"}, {\\\"trigger_word\\\": \\\"U.S.\\\", \\\"sent_id\\\": 8, \\\"offset\\\": [15, 16], \\\"id\\\": \\\"9dfe4e14cbc2401cbb5593616bb144f6\\\"}, {\\\"trigger_word\\\": \\\"Army\\\", \\\"sent_id\\\": 8, \\\"offset\\\": [16, 17], \\\"id\\\": \\\"6addd71b3190ab9c2f6bd5f18c21cf48\\\"}, {\\\"trigger_word\\\": \\\"corps\\\", \\\"sent_id\\\": 8, \\\"offset\\\": [17, 18], \\\"id\\\": \\\"abe62c1e4faca89fcdd105d3137ad09b\\\"}, {\\\"trigger_word\\\": \\\"mounted\\\", \\\"sent_id\\\": 8, \\\"offset\\\": [18, 19], \\\"id\\\": \\\"d321c1e9a7ca86dbaec1219bce57a6b4\\\"}, {\\\"trigger_word\\\": \\\"supporting\\\", \\\"sent_id\\\": 8, \\\"offset\\\": [19, 20], \\\"id\\\": \\\"31d787acadab6f0d5bf455fa8b3a9f89\\\"}, {\\\"trigger_word\\\": \\\"attacks\\\", \\\"sent_id\\\": 8, \\\"offset\\\": [20, 21], \\\"id\\\": \\\"91ca0bbad3c8038e07d502d2cfd326ef\\\"}, {\\\"trigger_word\\\": \\\"designed\\\", \\\"sent_id\\\": 8, \\\"offset\\\": [21, 22], \\\"id\\\": \\\"70f32672629556aaeabce1b04ffff7f4\\\"}, {\\\"trigger_word\\\": \\\"pin\\\", \\\"sent_id\\\": 8, \\\"offset\\\": [23, 24], \\\"id\\\": \\\"915c1637e5fa3bb40489e070b27addee\\\"}, {\\\"trigger_word\\\": \\\"German\\\", \\\"sent_id\\\": 8, \\\"offset\\\": [24, 25], \\\"id\\\": \\\"6d10d593feac44b5f059ce8143f4e8b0\\\"}, {\\\"trigger_word\\\": \\\"units\\\", \\\"sent_id\\\": 8, \\\"offset\\\": [25, 26], \\\"id\\\": \\\"b3138a146c4c23950b42c4c74e12d087\\\"}, {\\\"trigger_word\\\": \\\"place\\\", \\\"sent_id\\\": 8, \\\"offset\\\": [27, 28], \\\"id\\\": \\\"fbf0c6d524b0133f0443b3dca54cc80b\\\"}, {\\\"trigger_word\\\": \\\"Progress\\\", \\\"sent_id\\\": 9, \\\"offset\\\": [0, 1], \\\"id\\\": \\\"bfdb4381cd2fc1baff6a28025f44ef91\\\"}, {\\\"trigger_word\\\": \\\"slow\\\", \\\"sent_id\\\": 9, \\\"offset\\\": [2, 3], \\\"id\\\": \\\"48ab092c7d8067fb84371ab1ac727cbc\\\"}, {\\\"trigger_word\\\": \\\"first\\\", \\\"sent_id\\\": 9, \\\"offset\\\": [5, 6], \\\"id\\\": \\\"61287bfed38609f5427c5b87b6e07ff3\\\"}, {\\\"trigger_word\\\": \\\"day\\\", \\\"sent_id\\\": 9, \\\"offset\\\": [6, 7], \\\"id\\\": \\\"f6795809e1d0481fcdd08458affef957\\\"}, {\\\"trigger_word\\\": \\\"opposition\\\", \\\"sent_id\\\": 9, \\\"offset\\\": [8, 9], \\\"id\\\": \\\"2e34357726a51b168fbcdebd3e4ffe5d\\\"}, {\\\"trigger_word\\\": \\\"started\\\", \\\"sent_id\\\": 9, \\\"offset\\\": [9, 10], \\\"id\\\": \\\"5d275491a042812cf50f23f8484f6bfe\\\"}, {\\\"trigger_word\\\": \\\"crumble\\\", \\\"sent_id\\\": 9, \\\"offset\\\": [11, 12], \\\"id\\\": \\\"abe4ed1307cd28b059e35878d84a73a8\\\"}, {\\\"trigger_word\\\": \\\"defensive\\\", \\\"sent_id\\\": 9, \\\"offset\\\": [14, 15], \\\"id\\\": \\\"14603a515be70cbfb01fa330923deade\\\"}, {\\\"trigger_word\\\": \\\"crust\\\", \\\"sent_id\\\": 9, \\\"offset\\\": [15, 16], \\\"id\\\": \\\"9ebbb391684f70e3d0d3f88bf2078a8b\\\"}, {\\\"trigger_word\\\": \\\"broken\\\", \\\"sent_id\\\": 9, \\\"offset\\\": [18, 19], \\\"id\\\": \\\"7aa0054c770502714e909842e48c8120\\\"}, {\\\"trigger_word\\\": \\\"July\\\", \\\"sent_id\\\": 10, \\\"offset\\\": [2, 3], \\\"id\\\": \\\"7713fac58cdf82fa329a8c25a9ec3e7c\\\"}, {\\\"trigger_word\\\": \\\"organized\\\", \\\"sent_id\\\": 10, \\\"offset\\\": [5, 6], \\\"id\\\": \\\"8eabbd46a762db9a194178d800dcbd2c\\\"}, {\\\"trigger_word\\\": \\\"resistance\\\", \\\"sent_id\\\": 10, \\\"offset\\\": [6, 7], \\\"id\\\": \\\"113c8398491cb3ec6db9f7cf1e63d1c3\\\"}, {\\\"trigger_word\\\": \\\"overcome\\\", \\\"sent_id\\\": 10, \\\"offset\\\": [9, 10], \\\"id\\\": \\\"feea9bc58422f1886611ae6372fd25c7\\\"}, {\\\"trigger_word\\\": \\\"VII\\\", \\\"sent_id\\\": 10, \\\"offset\\\": [12, 13], \\\"id\\\": \\\"fac1e271873cb8ade8d69996ac4d5acd\\\"}, {\\\"trigger_word\\\": \\\"VIII\\\", \\\"sent_id\\\": 10, \\\"offset\\\": [14, 15], \\\"id\\\": \\\"0473400cea5ca71c020a03e29bd78c8f\\\"}, {\\\"trigger_word\\\": \\\"Corps\\\", \\\"sent_id\\\": 10, \\\"offset\\\": [15, 16], \\\"id\\\": \\\"74be8bc68955162c195c112055011220\\\"}, {\\\"trigger_word\\\": \\\"advanced\\\", \\\"sent_id\\\": 10, \\\"offset\\\": [16, 17], \\\"id\\\": \\\"b39509192c341b7cede22ca671f5c613\\\"}, {\\\"trigger_word\\\": \\\"rapidly\\\", \\\"sent_id\\\": 10, \\\"offset\\\": [17, 18], \\\"id\\\": \\\"f86edd3ec57bb01fdd2a2d08a8a7ed55\\\"}, {\\\"trigger_word\\\": \\\"isolating\\\", \\\"sent_id\\\": 10, \\\"offset\\\": [19, 20], \\\"id\\\": \\\"d688ed6ef458df2a102188fa6133225e\\\"}, {\\\"trigger_word\\\": \\\"Cotentin\\\", \\\"sent_id\\\": 10, \\\"offset\\\": [21, 22], \\\"id\\\": \\\"ae3c7c3e041975555d74293fc1beb041\\\"}, {\\\"trigger_word\\\": \\\"Peninsula\\\", \\\"sent_id\\\": 10, \\\"offset\\\": [22, 23], \\\"id\\\": \\\"19a2e9bef75abe3dda65dee3ca03feab\\\"}, {\\\"trigger_word\\\": \\\"July\\\", \\\"sent_id\\\": 11, \\\"offset\\\": [2, 3], \\\"id\\\": \\\"6dbcd95fa87aeb5f632855d417b49cbb\\\"}, {\\\"trigger_word\\\": \\\"XIX\\\", \\\"sent_id\\\": 11, \\\"offset\\\": [4, 5], \\\"id\\\": \\\"b817477a4c6cef27ca14a39f7e2df801\\\"}, {\\\"trigger_word\\\": \\\"Corps\\\", \\\"sent_id\\\": 11, \\\"offset\\\": [5, 6], \\\"id\\\": \\\"6fa7f824e1d69b84804edfaec544255b\\\"}, {\\\"trigger_word\\\": \\\"destroyed\\\", \\\"sent_id\\\": 11, \\\"offset\\\": [7, 8], \\\"id\\\": \\\"c0966b5b4e431f42f8142e8a8b8595ec\\\"}, {\\\"trigger_word\\\": \\\"last\\\", \\\"sent_id\\\": 11, \\\"offset\\\": [9, 10], \\\"id\\\": \\\"f424788758ccb80c510dec72b4691c26\\\"}, {\\\"trigger_word\\\": \\\"forces\\\", \\\"sent_id\\\": 11, \\\"offset\\\": [10, 11], \\\"id\\\": \\\"c974d81cc733b3a9adaa467d2b3e21af\\\"}, {\\\"trigger_word\\\": \\\"opposing\\\", \\\"sent_id\\\": 11, \\\"offset\\\": [11, 12], \\\"id\\\": \\\"2d06bfb0bd5792d1f648fcc6a37e7329\\\"}, {\\\"trigger_word\\\": \\\"First\\\", \\\"sent_id\\\": 11, \\\"offset\\\": [13, 14], \\\"id\\\": \\\"ebcb117b252c00cacb52584251ca496b\\\"}, {\\\"trigger_word\\\": \\\"Army\\\", \\\"sent_id\\\": 11, \\\"offset\\\": [14, 15], \\\"id\\\": \\\"369b3e6a23f4412f54914dea1eb921f8\\\"}, {\\\"trigger_word\\\": \\\"emerged\\\", \\\"sent_id\\\": 11, \\\"offset\\\": [17, 18], \\\"id\\\": \\\"f110839ce2399aa640429dc386903713\\\"}, {\\\"trigger_word\\\": \\\"bocage\\\", \\\"sent_id\\\": 11, \\\"offset\\\": [20, 21], \\\"id\\\": \\\"337b7672216c490b4aa2c1d858b4b287\\\"}, {\\\"trigger_word\\\": \\\"Reinforcements\\\", \\\"sent_id\\\": 12, \\\"offset\\\": [0, 1], \\\"id\\\": \\\"a56349fcf6fbaef0637c42a07ce5b8f0\\\"}, {\\\"trigger_word\\\": \\\"moved\\\", \\\"sent_id\\\": 12, \\\"offset\\\": [2, 3], \\\"id\\\": \\\"9346d914cc95ec2ad48de9640b3a429d\\\"}, {\\\"trigger_word\\\": \\\"west\\\", \\\"sent_id\\\": 12, \\\"offset\\\": [3, 4], \\\"id\\\": \\\"ef8309dfd7244d68cec20021c262e99d\\\"}, {\\\"trigger_word\\\": \\\"Field\\\", \\\"sent_id\\\": 12, \\\"offset\\\": [5, 6], \\\"id\\\": \\\"7d7dc8cb90c161d133481167ac253837\\\"}, {\\\"trigger_word\\\": \\\"Marshal\\\", \\\"sent_id\\\": 12, \\\"offset\\\": [6, 7], \\\"id\\\": \\\"fa858613331718c7c589bcf1b9056c7a\\\"}, {\\\"trigger_word\\\": \\\"Günther\\\", \\\"sent_id\\\": 12, \\\"offset\\\": [7, 8], \\\"id\\\": \\\"175c182da22919d4f3bed3430d5e03af\\\"}, {\\\"trigger_word\\\": \\\"von\\\", \\\"sent_id\\\": 12, \\\"offset\\\": [8, 9], \\\"id\\\": \\\"fc9d6ec478de435ea98f13a7f7e321a8\\\"}, {\\\"trigger_word\\\": \\\"Kluge\\\", \\\"sent_id\\\": 12, \\\"offset\\\": [9, 10], \\\"id\\\": \\\"101bad90e034ab5aeb5d6301dbad506f\\\"}, {\\\"trigger_word\\\": \\\"employed\\\", \\\"sent_id\\\": 12, \\\"offset\\\": [11, 12], \\\"id\\\": \\\"d88a16a023d67d9e1d8e30db85e253fb\\\"}, {\\\"trigger_word\\\": \\\"various\\\", \\\"sent_id\\\": 12, \\\"offset\\\": [13, 14], \\\"id\\\": \\\"7c0477b91b284c87ff23307729030d49\\\"}, {\\\"trigger_word\\\": \\\"counterattacks\\\", \\\"sent_id\\\": 12, \\\"offset\\\": [14, 15], \\\"id\\\": \\\"f6df2baec6510b8886b9578446854f50\\\"}, {\\\"trigger_word\\\": \\\"largest\\\", \\\"sent_id\\\": 12, \\\"offset\\\": [17, 18], \\\"id\\\": \\\"bf762ab26d7047e1e88321eeaed8bf20\\\"}, {\\\"trigger_word\\\": \\\"Unternehmen\\\", \\\"sent_id\\\": 12, \\\"offset\\\": [22, 23], \\\"id\\\": \\\"8ac0bc73b61ca11ea5802f3793047c10\\\"}, {\\\"trigger_word\\\": \\\"Lüttich\\\", \\\"sent_id\\\": 12, \\\"offset\\\": [23, 24], \\\"id\\\": \\\"d36566bc12c996e333e5b94f466e7048\\\"}, {\\\"trigger_word\\\": \\\"Operation\\\", \\\"sent_id\\\": 12, \\\"offset\\\": [26, 27], \\\"id\\\": \\\"3d723dc3d54d59ad02355bb385ada9d4\\\"}, {\\\"trigger_word\\\": \\\"Liège\\\", \\\"sent_id\\\": 12, \\\"offset\\\": [27, 28], \\\"id\\\": \\\"94d17fe7b8b8a13ebdad86031daf596d\\\"}, {\\\"trigger_word\\\": \\\"launched\\\", \\\"sent_id\\\": 12, \\\"offset\\\": [31, 32], \\\"id\\\": \\\"943d8207a4f0ab05a7690401a8ec9786\\\"}, {\\\"trigger_word\\\": \\\"August\\\", \\\"sent_id\\\": 12, \\\"offset\\\": [34, 35], \\\"id\\\": \\\"43c4ea081436aba2037abba805f9334f\\\"}, {\\\"trigger_word\\\": \\\"Mortain\\\", \\\"sent_id\\\": 12, \\\"offset\\\": [36, 37], \\\"id\\\": \\\"c91657177a18bf44c7c0f0b1ad16a01f\\\"}, {\\\"trigger_word\\\": \\\"Avranches\\\", \\\"sent_id\\\": 12, \\\"offset\\\": [38, 39], \\\"id\\\": \\\"d05dc82f8b3b7f57b5cfa6d9c4f578b3\\\"}, {\\\"trigger_word\\\": \\\"led to\\\", \\\"sent_id\\\": 13, \\\"offset\\\": [2, 4], \\\"id\\\": \\\"a9b8df41c9a30b5a0dfe821a3ea96594\\\"}, {\\\"trigger_word\\\": \\\"bloodiest\\\", \\\"sent_id\\\": 13, \\\"offset\\\": [5, 6], \\\"id\\\": \\\"f76bb2cf546a1bf72b19fe5f79d93631\\\"}, {\\\"trigger_word\\\": \\\"phase\\\", \\\"sent_id\\\": 13, \\\"offset\\\": [6, 7], \\\"id\\\": \\\"5e435d6b3f573e2a0af6d9603e53e592\\\"}, {\\\"trigger_word\\\": \\\"battle\\\", \\\"sent_id\\\": 13, \\\"offset\\\": [9, 10], \\\"id\\\": \\\"86d82bfeb5202702a9719b02c1a52713\\\"}, {\\\"trigger_word\\\": \\\"already\\\", \\\"sent_id\\\": 13, \\\"offset\\\": [15, 16], \\\"id\\\": \\\"30954f962e4424476496fdb1607ab8d6\\\"}, {\\\"trigger_word\\\": \\\"exhausted\\\", \\\"sent_id\\\": 13, \\\"offset\\\": [16, 17], \\\"id\\\": \\\"ecc5c0e062c1b2a51377297a8531c462\\\"}, {\\\"trigger_word\\\": \\\"understrength\\\", \\\"sent_id\\\": 13, \\\"offset\\\": [18, 19], \\\"id\\\": \\\"d4a6a6c3f38ae69aa01aa0756ab8cbd4\\\"}, {\\\"trigger_word\\\": \\\"units\\\", \\\"sent_id\\\": 13, \\\"offset\\\": [19, 20], \\\"id\\\": \\\"4253c79889effee3c678b2601c668fc2\\\"}, {\\\"trigger_word\\\": \\\"costly\\\", \\\"sent_id\\\": 13, \\\"offset\\\": [23, 24], \\\"id\\\": \\\"eb8cbede5fe7e845cb1646bb7e3e8850\\\"}, {\\\"trigger_word\\\": \\\"failure\\\", \\\"sent_id\\\": 13, \\\"offset\\\": [24, 25], \\\"id\\\": \\\"6ea4a7b62046660fa74b8dd9ff9d66b4\\\"}, {\\\"trigger_word\\\": \\\"August\\\", \\\"sent_id\\\": 14, \\\"offset\\\": [2, 3], \\\"id\\\": \\\"fa38baa7753ba74036b6bdc1ff16d8ef\\\"}, {\\\"trigger_word\\\": \\\"troops\\\", \\\"sent_id\\\": 14, \\\"offset\\\": [4, 5], \\\"id\\\": \\\"7a78d458bbabef3ec4a1215793f851ca\\\"}, {\\\"trigger_word\\\": \\\"newly\\\", \\\"sent_id\\\": 14, \\\"offset\\\": [7, 8], \\\"id\\\": \\\"74d4172d88edb457ab7f09acd751d9bc\\\"}, {\\\"trigger_word\\\": \\\"activated\\\", \\\"sent_id\\\": 14, \\\"offset\\\": [8, 9], \\\"id\\\": \\\"2ca245a2413410b36562052b7cb2cc1c\\\"}, {\\\"trigger_word\\\": \\\"Third\\\", \\\"sent_id\\\": 14, \\\"offset\\\": [9, 10], \\\"id\\\": \\\"705212a1abee7ff745a983fff63cf57d\\\"}, {\\\"trigger_word\\\": \\\"United\\\", \\\"sent_id\\\": 14, \\\"offset\\\": [10, 11], \\\"id\\\": \\\"b64ab993c1c49402ba9e1f1203514d24\\\"}, {\\\"trigger_word\\\": \\\"States\\\", \\\"sent_id\\\": 14, \\\"offset\\\": [11, 12], \\\"id\\\": \\\"91a5af8ab00ba998b7ceb4cdae76ae68\\\"}, {\\\"trigger_word\\\": \\\"Army\\\", \\\"sent_id\\\": 14, \\\"offset\\\": [12, 13], \\\"id\\\": \\\"ecaf1efdf4bad79bd79baef7ec29c85d\\\"}, {\\\"trigger_word\\\": \\\"captured\\\", \\\"sent_id\\\": 14, \\\"offset\\\": [13, 14], \\\"id\\\": \\\"ae2a3ce953ab069bab72ace95ae28adc\\\"}, {\\\"trigger_word\\\": \\\"city\\\", \\\"sent_id\\\": 14, \\\"offset\\\": [15, 16], \\\"id\\\": \\\"fb2a37e58af2f46d3532bd9a4e80c636\\\"}, {\\\"trigger_word\\\": \\\"Le\\\", \\\"sent_id\\\": 14, \\\"offset\\\": [17, 18], \\\"id\\\": \\\"0de1bafea83b371305e7e6f75127e041\\\"}, {\\\"trigger_word\\\": \\\"Mans\\\", \\\"sent_id\\\": 14, \\\"offset\\\": [18, 19], \\\"id\\\": \\\"9c037c1679ef82d0fb7e9fd4191c97ec\\\"}, {\\\"trigger_word\\\": \\\"formerly\\\", \\\"sent_id\\\": 14, \\\"offset\\\": [20, 21], \\\"id\\\": \\\"68a32355a1e472e24ac20f0a7de756d8\\\"}, {\\\"trigger_word\\\": \\\"German\\\", \\\"sent_id\\\": 14, \\\"offset\\\": [22, 23], \\\"id\\\": \\\"6533e15c9f6d0d0bedd122c30d84390d\\\"}, {\\\"trigger_word\\\": \\\"Army\\\", \\\"sent_id\\\": 14, \\\"offset\\\": [24, 25], \\\"id\\\": \\\"2029bcb4e389f5149b901ad4c321057d\\\"}, {\\\"trigger_word\\\": \\\"headquarters\\\", \\\"sent_id\\\": 14, \\\"offset\\\": [25, 26], \\\"id\\\": \\\"f0b2e712a952d69c350230c8de80178b\\\"}, {\\\"trigger_word\\\": \\\"Operation\\\", \\\"sent_id\\\": 15, \\\"offset\\\": [0, 1], \\\"id\\\": \\\"a4974e5e0abe6a6a75f8be34afa7f3f3\\\"}, {\\\"trigger_word\\\": \\\"Cobra\\\", \\\"sent_id\\\": 15, \\\"offset\\\": [1, 2], \\\"id\\\": \\\"c6b82aef8a46befab2a041f19f3d8262\\\"}, {\\\"trigger_word\\\": \\\"transformed\\\", \\\"sent_id\\\": 15, \\\"offset\\\": [2, 3], \\\"id\\\": \\\"f5909925217146abf1cfc00b5897e4f8\\\"}, {\\\"trigger_word\\\": \\\"high-intensity\\\", \\\"sent_id\\\": 15, \\\"offset\\\": [4, 5], \\\"id\\\": \\\"939b7854c460189ccc112a4cc5b826ba\\\"}, {\\\"trigger_word\\\": \\\"infantry\\\", \\\"sent_id\\\": 15, \\\"offset\\\": [5, 6], \\\"id\\\": \\\"393ab039bf55eb4095bbea1bba672863\\\"}, {\\\"trigger_word\\\": \\\"combat\\\", \\\"sent_id\\\": 15, \\\"offset\\\": [6, 7], \\\"id\\\": \\\"e7fb22fd72de7e9566c4023b49d7c64d\\\"}, {\\\"trigger_word\\\": \\\"Normandy\\\", \\\"sent_id\\\": 15, \\\"offset\\\": [8, 9], \\\"id\\\": \\\"bfdb8cbb8a6d748a97a42f562962198f\\\"}, {\\\"trigger_word\\\": \\\"rapid\\\", \\\"sent_id\\\": 15, \\\"offset\\\": [10, 11], \\\"id\\\": \\\"fc40689c215e02b612e7c2870b18fcbb\\\"}, {\\\"trigger_word\\\": \\\"maneuver\\\", \\\"sent_id\\\": 15, \\\"offset\\\": [11, 12], \\\"id\\\": \\\"b7445e4512d7cf351edac2b95ab2659f\\\"}, {\\\"trigger_word\\\": \\\"warfare\\\", \\\"sent_id\\\": 15, \\\"offset\\\": [12, 13], \\\"id\\\": \\\"a05abc5cf1b9947f0de44009985c75d5\\\"}, {\\\"trigger_word\\\": \\\"led to\\\", \\\"sent_id\\\": 15, \\\"offset\\\": [14, 16], \\\"id\\\": \\\"97a64d6f060039dd0ac2c2732bd2f76c\\\"}, {\\\"trigger_word\\\": \\\"creation\\\", \\\"sent_id\\\": 15, \\\"offset\\\": [17, 18], \\\"id\\\": \\\"bf7c95a15fee622436d28bdd83886588\\\"}, {\\\"trigger_word\\\": \\\"Falaise\\\", \\\"sent_id\\\": 15, \\\"offset\\\": [20, 21], \\\"id\\\": \\\"b9567e81b7720667cb5dff022cb77438\\\"}, {\\\"trigger_word\\\": \\\"pocket\\\", \\\"sent_id\\\": 15, \\\"offset\\\": [21, 22], \\\"id\\\": \\\"0bdd54d45579e2de4a14a1d0d0466c21\\\"}, {\\\"trigger_word\\\": \\\"loss\\\", \\\"sent_id\\\": 15, \\\"offset\\\": [24, 25], \\\"id\\\": \\\"4f1384a9b06ac7bbf9c216e2fcaad57a\\\"}, {\\\"trigger_word\\\": \\\"German\\\", \\\"sent_id\\\": 15, \\\"offset\\\": [27, 28], \\\"id\\\": \\\"21f1502642a9e61987dd344f19fe2b82\\\"}, {\\\"trigger_word\\\": \\\"position\\\", \\\"sent_id\\\": 15, \\\"offset\\\": [28, 29], \\\"id\\\": \\\"f9b894a0728be480f671399440138904\\\"}, {\\\"trigger_word\\\": \\\"northwestern\\\", \\\"sent_id\\\": 15, \\\"offset\\\": [30, 31], \\\"id\\\": \\\"d4ee063a5445d1a4ecbec464f438bba1\\\"}, {\\\"trigger_word\\\": \\\"France\\\", \\\"sent_id\\\": 15, \\\"offset\\\": [31, 32], \\\"id\\\": \\\"5e93fdd212af9b3ee1a2f56ba1ef5033\\\"}]}\\n/root/schema-dag-extraction/data/maven/test.jsonl:523:{\\\"title\\\": \\\"Operation Desert Thunder\\\", \\\"id\\\": \\\"a1e54403f77a2df1ace404d534ee99d0\\\", \\\"content\\\": [{\\\"sentence\\\": \\\"Operation Desert Thunder was a response to threats by Iraq's president Saddam Hussein to shoot down U-2 spy planes, and violate the no-fly zone set up over his country.\\\", \\\"tokens\\\": [\\\"Operation\\\", \\\"Desert\\\", \\\"Thunder\\\", \\\"was\\\", \\\"a\\\", \\\"response\\\", \\\"to\\\", \\\"threats\\\", \\\"by\\\", \\\"Iraq\\\", \\\"'s\\\", \\\"president\\\", \\\"Saddam\\\", \\\"Hussein\\\", \\\"to\\\", \\\"shoot\\\", \\\"down\\\", \\\"U-2\\\", \\\"spy\\\", \\\"planes\\\", \\\",\\\", \\\"and\\\", \\\"violate\\\", \\\"the\\\", \\\"no-fly\\\", \\\"zone\\\", \\\"set\\\", \\\"up\\\", \\\"over\\\", \\\"his\\\", \\\"country\\\", \\\".\\\"]}, {\\\"sentence\\\": \\\"The operation was designed to bring stability to the region by bringing in a military presence during the negotiations between Iraq and the UN over weapons of mass destruction.\\\", \\\"tokens\\\": [\\\"The\\\", \\\"operation\\\", \\\"was\\\", \\\"designed\\\", \\\"to\\\", \\\"bring\\\", \\\"stability\\\", \\\"to\\\", \\\"the\\\", \\\"region\\\", \\\"by\\\", \\\"bringing\\\", \\\"in\\\", \\\"a\\\", \\\"military\\\", \\\"presence\\\", \\\"during\\\", \\\"the\\\", \\\"negotiations\\\", \\\"between\\\", \\\"Iraq\\\", \\\"and\\\", \\\"the\\\", \\\"UN\\\", \\\"over\\\", \\\"weapons\\\", \\\"of\\\", \\\"mass\\\", \\\"destruction\\\", \\\".\\\"]}, {\\\"sentence\\\": \\\"The name Operation Desert Thunder has been applied to the build-up of forces in the Persian Gulf region during 1998.\\\", \\\"tokens\\\": [\\\"The\\\", \\\"name\\\", \\\"Operation\\\", \\\"Desert\\\", \\\"Thunder\\\", \\\"has\\\", \\\"been\\\", \\\"applied\\\", \\\"to\\\", \\\"the\\\", \\\"build-up\\\", \\\"of\\\", \\\"forces\\\", \\\"in\\\", \\\"the\\\", \\\"Persian\\\", \\\"Gulf\\\", \\\"region\\\", \\\"during\\\", \\\"1998\\\", \\\".\\\"]}, {\\\"sentence\\\": \\\"If an actual attack had been ordered and executed, the name would have changed to Operation Desert Viper.\\\", \\\"tokens\\\": [\\\"If\\\", \\\"an\\\", \\\"actual\\\", \\\"attack\\\", \\\"had\\\", \\\"been\\\", \\\"ordered\\\", \\\"and\\\", \\\"executed\\\", \\\",\\\", \\\"the\\\", \\\"name\\\", \\\"would\\\", \\\"have\\\", \\\"changed\\\", \\\"to\\\", \\\"Operation\\\", \\\"Desert\\\", \\\"Viper\\\", \\\".\\\"]}, {\\\"sentence\\\": \\\"In the autumn of 1997 CENTCOM established a force of 35,000 air, land, and sea forces in response to Iraq's non-compliance of UN resolutions.\\\", \\\"tokens\\\": [\\\"In\\\", \\\"the\\\", \\\"autumn\\\", \\\"of\\\", \\\"1997\\\", \\\"CENTCOM\\\", \\\"established\\\", \\\"a\\\", \\\"force\\\", \\\"of\\\", \\\"35,000\\\", \\\"air\\\", \\\",\\\", \\\"land\\\", \\\",\\\", \\\"and\\\", \\\"sea\\\", \\\"forces\\\", \\\"in\\\", \\\"response\\\", \\\"to\\\", \\\"Iraq\\\", \\\"'s\\\", \\\"non-compliance\\\", \\\"of\\\", \\\"UN\\\", \\\"resolutions\\\", \\\".\\\"]}, {\\\"sentence\\\": \\\"CENTCOM Commander-in-Chief General Anthony Zinni established a permanent Coalition/Joint Task Force (C/JTF) at Camp Doha in Kuwait under command of Lieutenant General Tommy Franks to lead this force.\\\", \\\"tokens\\\": [\\\"centcom\\\", \\\"commander-in-chief\\\", \\\"general\\\", \\\"anthony\\\", \\\"zinni\\\", \\\"established\\\", \\\"a\\\", \\\"permanent\\\", \\\"unk\\\", \\\"task\\\", \\\"force\\\", \\\"(\\\", \\\"unk\\\", \\\")\\\", \\\"at\\\", \\\"camp\\\", \\\"doha\\\", \\\"in\\\", \\\"kuwait\\\", \\\"under\\\", \\\"command\\\", \\\"of\\\", \\\"lieutenant\\\", \\\"general\\\", \\\"tommy\\\", \\\"franks\\\", \\\"to\\\", \\\"lead\\\", \\\"this\\\", \\\"force\\\", \\\".\\\"]}, {\\\"sentence\\\": \\\"The coalition would consist of forces from Argentina, Australia, Canada, Czech Republic, Hungary, New Zealand, Poland, Romania, United Kingdom, United States, and Kuwait.\\\", \\\"tokens\\\": [\\\"The\\\", \\\"coalition\\\", \\\"would\\\", \\\"consist\\\", \\\"of\\\", \\\"forces\\\", \\\"from\\\", \\\"Argentina\\\", \\\",\\\", \\\"Australia\\\", \\\",\\\", \\\"Canada\\\", \\\",\\\", \\\"Czech\\\", \\\"Republic\\\", \\\",\\\", \\\"Hungary\\\", \\\",\\\", \\\"New\\\", \\\"Zealand\\\", \\\",\\\", \\\"Poland\\\", \\\",\\\", \\\"Romania\\\", \\\",\\\", \\\"United\\\", \\\"Kingdom\\\", \\\",\\\", \\\"United\\\", \\\"States\\\", \\\",\\\", \\\"and\\\", \\\"Kuwait\\\", \\\".\\\"]}, {\\\"sentence\\\": \\\"On 18 January 1998 additional forces were brought in to support the U.S.-led coalition forces in the region.\\\", \\\"tokens\\\": [\\\"On\\\", \\\"18\\\", \\\"January\\\", \\\"1998\\\", \\\"additional\\\", \\\"forces\\\", \\\"were\\\", \\\"brought\\\", \\\"in\\\", \\\"to\\\", \\\"support\\\", \\\"the\\\", \\\"U.S.-led\\\", \\\"coalition\\\", \\\"forces\\\", \\\"in\\\", \\\"the\\\", \\\"region\\\", \\\".\\\"]}, {\\\"sentence\\\": \\\"The U.S. 3d Infantry Division of Fort Stewart, Georgia, deployed 4,000 personnel and 2,900 short tons of equipment on 120 aircraft.\\\", \\\"tokens\\\": [\\\"The\\\", \\\"U.S.\\\", \\\"3d\\\", \\\"Infantry\\\", \\\"Division\\\", \\\"of\\\", \\\"Fort\\\", \\\"Stewart\\\", \\\",\\\", \\\"Georgia\\\", \\\",\\\", \\\"deployed\\\", \\\"4,000\\\", \\\"personnel\\\", \\\"and\\\", \\\"2,900\\\", \\\"short\\\", \\\"tons\\\", \\\"of\\\", \\\"equipment\\\", \\\"on\\\", \\\"120\\\", \\\"aircraft\\\", \\\".\\\"]}, {\\\"sentence\\\": \\\"Elements of 32nd Air and Missile Defense Command and 2nd Battalion 504th Parachute Infantry Regiment (82nd Airborne Division, Fort Bragg, NC) deployed to Saudi Arabia, Kuwait and Bahrain.\\\", \\\"tokens\\\": [\\\"elements\\\", \\\"of\\\", \\\"32nd\\\", \\\"air\\\", \\\"and\\\", \\\"missile\\\", \\\"defense\\\", \\\"command\\\", \\\"and\\\", \\\"2nd\\\", \\\"battalion\\\", \\\"504th\\\", \\\"parachute\\\", \\\"infantry\\\", \\\"regiment\\\", \\\"(\\\", \\\"82nd\\\", \\\"airborne\\\", \\\"division\\\", \\\",\\\", \\\"fort\\\", \\\"bragg\\\", \\\",\\\", \\\"nc\\\", \\\")\\\", \\\"deployed\\\", \\\"to\\\", \\\"saudi\\\", \\\"arabia\\\", \\\",\\\", \\\"kuwait\\\", \\\"and\\\", \\\"bahrain\\\", \\\".\\\"]}, {\\\"sentence\\\": \\\"The 366th Air Expeditionary Wing from Mountain Home Air Force Base, ID replaced the 347th Air Expeditionary Wing of Moody AFB, Georgia on 1 April 1998 after 120 days of deployment.\\\", \\\"tokens\\\": [\\\"the\\\", \\\"366th\\\", \\\"air\\\", \\\"expeditionary\\\", \\\"wing\\\", \\\"from\\\", \\\"mountain\\\", \\\"home\\\", \\\"air\\\", \\\"force\\\", \\\"base\\\", \\\",\\\", \\\"id\\\", \\\"replaced\\\", \\\"the\\\", \\\"347th\\\", \\\"air\\\", \\\"expeditionary\\\", \\\"wing\\\", \\\"of\\\", \\\"moody\\\", \\\"afb\\\", \\\",\\\", \\\"georgia\\\", \\\"on\\\", \\\"1\\\", \\\"april\\\", \\\"1998\\\", \\\"after\\\", \\\"120\\\", \\\"days\\\", \\\"of\\\", \\\"deployment\\\", \\\".\\\"]}, {\\\"sentence\\\": \\\"USS \\\\\\\"George Washington\\\\\\\" (CVN-73) joined USS \\\\\\\"Nimitz\\\\\\\" (CVN-68) (relieved on-station by USS \\\\\\\"Independence\\\\\\\" (CV-62) a few months later) in the Gulf.\\\", \\\"tokens\\\": [\\\"USS\\\", \\\"``\\\", \\\"George\\\", \\\"Washington\\\", \\\"''\\\", \\\"(\\\", \\\"CVN-73\\\", \\\")\\\", \\\"joined\\\", \\\"USS\\\", \\\"``\\\", \\\"Nimitz\\\", \\\"''\\\", \\\"(\\\", \\\"CVN-68\\\", \\\")\\\", \\\"(\\\", \\\"relieved\\\", \\\"on-station\\\", \\\"by\\\", \\\"USS\\\", \\\"``\\\", \\\"Independence\\\", \\\"''\\\", \\\"(\\\", \\\"CV-62\\\", \\\")\\\", \\\"a\\\", \\\"few\\\", \\\"months\\\", \\\"later\\\", \\\")\\\", \\\"in\\\", \\\"the\\\", \\\"Gulf\\\", \\\".\\\"]}, {\\\"sentence\\\": \\\"Combined with the British HMS\\\\\\\" Invincible\\\\\\\" (R05) and HMS\\\\\\\" Illustrious\\\\\\\" (R06), there were now 50 ships and submarines with 200 naval aircraft, a floating brigade (Army) and the 11th Marine Expeditionary Unit in the Persian Gulf.\\\", \\\"tokens\\\": [\\\"Combined\\\", \\\"with\\\", \\\"the\\\", \\\"British\\\", \\\"HMS\\\", \\\"''\\\", \\\"Invincible\\\", \\\"''\\\", \\\"(\\\", \\\"R05\\\", \\\")\\\", \\\"and\\\", \\\"HMS\\\", \\\"''\\\", \\\"Illustrious\\\", \\\"''\\\", \\\"(\\\", \\\"R06\\\", \\\")\\\", \\\",\\\", \\\"there\\\", \\\"were\\\", \\\"now\\\", \\\"50\\\", \\\"ships\\\", \\\"and\\\", \\\"submarines\\\", \\\"with\\\", \\\"200\\\", \\\"naval\\\", \\\"aircraft\\\", \\\",\\\", \\\"a\\\", \\\"floating\\\", \\\"brigade\\\", \\\"(\\\", \\\"Army\\\", \\\")\\\", \\\"and\\\", \\\"the\\\", \\\"11th\\\", \\\"Marine\\\", \\\"Expeditionary\\\", \\\"Unit\\\", \\\"in\\\", \\\"the\\\", \\\"Persian\\\", \\\"Gulf\\\", \\\".\\\"]}, {\\\"sentence\\\": \\\"This combined muscle forced Saddam to back down, and the \\\\\\\"Independence\\\\\\\" returned to Yokosuka, Japan in early June 1998.\\\", \\\"tokens\\\": [\\\"This\\\", \\\"combined\\\", \\\"muscle\\\", \\\"forced\\\", \\\"Saddam\\\", \\\"to\\\", \\\"back\\\", \\\"down\\\", \\\",\\\", \\\"and\\\", \\\"the\\\", \\\"``\\\", \\\"Independence\\\", \\\"''\\\", \\\"returned\\\", \\\"to\\\", \\\"Yokosuka\\\", \\\",\\\", \\\"Japan\\\", \\\"in\\\", \\\"early\\\", \\\"June\\\", \\\"1998\\\", \\\".\\\"]}, {\\\"sentence\\\": \\\"In July 1998 the 3-101st Attk Avn Bn deployed two AH-64A Companies to Ali Al Salem AB to maintain a strong presence in the region.\\\", \\\"tokens\\\": [\\\"In\\\", \\\"July\\\", \\\"1998\\\", \\\"the\\\", \\\"3-101st\\\", \\\"Attk\\\", \\\"Avn\\\", \\\"Bn\\\", \\\"deployed\\\", \\\"two\\\", \\\"AH-64A\\\", \\\"Companies\\\", \\\"to\\\", \\\"Ali\\\", \\\"Al\\\", \\\"Salem\\\", \\\"AB\\\", \\\"to\\\", \\\"maintain\\\", \\\"a\\\", \\\"strong\\\", \\\"presence\\\", \\\"in\\\", \\\"the\\\", \\\"region\\\", \\\".\\\"]}, {\\\"sentence\\\": \\\"Then in November 1998, the U.S. 3d Infantry Division returned to Kuwait.\\\", \\\"tokens\\\": [\\\"Then\\\", \\\"in\\\", \\\"November\\\", \\\"1998\\\", \\\",\\\", \\\"the\\\", \\\"U.S.\\\", \\\"3d\\\", \\\"Infantry\\\", \\\"Division\\\", \\\"returned\\\", \\\"to\\\", \\\"Kuwait\\\", \\\".\\\"]}, {\\\"sentence\\\": \\\"Using the C/JTF already in place advanced elements of the U.S. 3d Infantry Division and 32nd Air & Missile Defense Command, Theatre Support Command, and Air Support Operations Center deployed.\\\", \\\"tokens\\\": [\\\"using\\\", \\\"the\\\", \\\"unk\\\", \\\"already\\\", \\\"in\\\", \\\"place\\\", \\\"advanced\\\", \\\"elements\\\", \\\"of\\\", \\\"the\\\", \\\"u.s.\\\", \\\"3d\\\", \\\"infantry\\\", \\\"division\\\", \\\"and\\\", \\\"32nd\\\", \\\"air\\\", \\\"&\\\", \\\"missile\\\", \\\"defense\\\", \\\"command\\\", \\\",\\\", \\\"theatre\\\", \\\"support\\\", \\\"command\\\", \\\",\\\", \\\"and\\\", \\\"air\\\", \\\"support\\\", \\\"operations\\\", \\\"center\\\", \\\"deployed\\\", \\\".\\\"]}, {\\\"sentence\\\": \\\"In addition the 2nd Marine Expeditionary Force joined the 1st Marine Expeditionary Force already in place.\\\", \\\"tokens\\\": [\\\"in\\\", \\\"addition\\\", \\\"the\\\", \\\"2nd\\\", \\\"marine\\\", \\\"expeditionary\\\", \\\"force\\\", \\\"joined\\\", \\\"the\\\", \\\"1st\\\", \\\"marine\\\", \\\"expeditionary\\\", \\\"force\\\", \\\"already\\\", \\\"in\\\", \\\"place\\\", \\\".\\\"]}, {\\\"sentence\\\": \\\"During this build-up, UN Secretary-General Kofi Annan flew to Baghdad to meet with Saddam Hussein and negotiated to allow uninterrupted inspections.\\\", \\\"tokens\\\": [\\\"During\\\", \\\"this\\\", \\\"build-up\\\", \\\",\\\", \\\"UN\\\", \\\"Secretary-General\\\", \\\"Kofi\\\", \\\"Annan\\\", \\\"flew\\\", \\\"to\\\", \\\"Baghdad\\\", \\\"to\\\", \\\"meet\\\", \\\"with\\\", \\\"Saddam\\\", \\\"Hussein\\\", \\\"and\\\", \\\"negotiated\\\", \\\"to\\\", \\\"allow\\\", \\\"uninterrupted\\\", \\\"inspections\\\", \\\".\\\"]}, {\\\"sentence\\\": \\\"On 11 November 1998, further non-compliance by Iraq resulted in the initiation of Operation Desert Thunder.\\\", \\\"tokens\\\": [\\\"On\\\", \\\"11\\\", \\\"November\\\", \\\"1998\\\", \\\",\\\", \\\"further\\\", \\\"non-compliance\\\", \\\"by\\\", \\\"Iraq\\\", \\\"resulted\\\", \\\"in\\\", \\\"the\\\", \\\"initiation\\\", \\\"of\\\", \\\"Operation\\\", \\\"Desert\\\", \\\"Thunder\\\", \\\".\\\"]}, {\\\"sentence\\\": \\\"CENTCOM moved its forces into position to initiate strikes into Iraq; 2,300 additional personnel were deployed during this operation.\\\", \\\"tokens\\\": [\\\"CENTCOM\\\", \\\"moved\\\", \\\"its\\\", \\\"forces\\\", \\\"into\\\", \\\"position\\\", \\\"to\\\", \\\"initiate\\\", \\\"strikes\\\", \\\"into\\\", \\\"Iraq\\\", \\\";\\\", \\\"2,300\\\", \\\"additional\\\", \\\"personnel\\\", \\\"were\\\", \\\"deployed\\\", \\\"during\\\", \\\"this\\\", \\\"operation\\\", \\\".\\\"]}, {\\\"sentence\\\": \\\"On the evening of 15 November, USS \\\\\\\"Dwight D. Eisenhower\\\\\\\" (CVN-69) was just minutes away from launching air strikes on targets in Iraq when Saddam Hussein again backed down.\\\", \\\"tokens\\\": [\\\"On\\\", \\\"the\\\", \\\"evening\\\", \\\"of\\\", \\\"15\\\", \\\"November\\\", \\\",\\\", \\\"USS\\\", \\\"``\\\", \\\"Dwight\\\", \\\"D.\\\", \\\"Eisenhower\\\", \\\"''\\\", \\\"(\\\", \\\"CVN-69\\\", \\\")\\\", \\\"was\\\", \\\"just\\\", \\\"minutes\\\", \\\"away\\\", \\\"from\\\", \\\"launching\\\", \\\"air\\\", \\\"strikes\\\", \\\"on\\\", \\\"targets\\\", \\\"in\\\", \\\"Iraq\\\", \\\"when\\\", \\\"Saddam\\\", \\\"Hussein\\\", \\\"again\\\", \\\"backed\\\", \\\"down\\\", \\\".\\\"]}, {\\\"sentence\\\": \\\"In December 1998, Iraq again refused to allow inspections and Operation Desert Fox began.\\\", \\\"tokens\\\": [\\\"In\\\", \\\"December\\\", \\\"1998\\\", \\\",\\\", \\\"Iraq\\\", \\\"again\\\", \\\"refused\\\", \\\"to\\\", \\\"allow\\\", \\\"inspections\\\", \\\"and\\\", \\\"Operation\\\", \\\"Desert\\\", \\\"Fox\\\", \\\"began\\\", \\\".\\\"]}, {\\\"sentence\\\": \\\"Several key Iraqi facilities and specialized equipment were destroyed during several days of air strikes including from the flight deck of USS \\\\\\\"Enterprise\\\\\\\" (CVN-65) .\\\", \\\"tokens\\\": [\\\"Several\\\", \\\"key\\\", \\\"Iraqi\\\", \\\"facilities\\\", \\\"and\\\", \\\"specialized\\\", \\\"equipment\\\", \\\"were\\\", \\\"destroyed\\\", \\\"during\\\", \\\"several\\\", \\\"days\\\", \\\"of\\\", \\\"air\\\", \\\"strikes\\\", \\\"including\\\", \\\"from\\\", \\\"the\\\", \\\"flight\\\", \\\"deck\\\", \\\"of\\\", \\\"USS\\\", \\\"``\\\", \\\"Enterprise\\\", \\\"''\\\", \\\"(\\\", \\\"CVN-65\\\", \\\")\\\", \\\".\\\"]}, {\\\"sentence\\\": \\\"This set back the Iraqi ballistic missile program by several years.\\\", \\\"tokens\\\": [\\\"This\\\", \\\"set\\\", \\\"back\\\", \\\"the\\\", \\\"Iraqi\\\", \\\"ballistic\\\", \\\"missile\\\", \\\"program\\\", \\\"by\\\", \\\"several\\\", \\\"years\\\", \\\".\\\"]}], \\\"candidates\\\": [{\\\"trigger_word\\\": \\\"Operation\\\", \\\"sent_id\\\": 0, \\\"offset\\\": [0, 1], \\\"id\\\": \\\"74f2743dde4ced07110539b0aad862af\\\"}, {\\\"trigger_word\\\": \\\"Desert\\\", \\\"sent_id\\\": 0, \\\"offset\\\": [1, 2], \\\"id\\\": \\\"74a7ec15901939f1e4461e92d326ee33\\\"}, {\\\"trigger_word\\\": \\\"Thunder\\\", \\\"sent_id\\\": 0, \\\"offset\\\": [2, 3], \\\"id\\\": \\\"45567d666c7a6c0ce74af0267439f7a7\\\"}, {\\\"trigger_word\\\": \\\"response\\\", \\\"sent_id\\\": 0, \\\"offset\\\": [5, 6], \\\"id\\\": \\\"6925856a980fdc593fdc83649da964ef\\\"}, {\\\"trigger_word\\\": \\\"threats\\\", \\\"sent_id\\\": 0, \\\"offset\\\": [7, 8], \\\"id\\\": \\\"1c253b9d883187feb7cd3d4ab19723ca\\\"}, {\\\"trigger_word\\\": \\\"Iraq\\\", \\\"sent_id\\\": 0, \\\"offset\\\": [9, 10], \\\"id\\\": \\\"7d8df33c522f4ce4e1dc48c55fbfc7cc\\\"}, {\\\"trigger_word\\\": \\\"president\\\", \\\"sent_id\\\": 0, \\\"offset\\\": [11, 12], \\\"id\\\": \\\"a6b952755499588c3a06cc14a24f58d2\\\"}, {\\\"trigger_word\\\": \\\"Saddam\\\", \\\"sent_id\\\": 0, \\\"offset\\\": [12, 13], \\\"id\\\": \\\"a7c073663cd2fb3da14147e8e3f3b25d\\\"}, {\\\"trigger_word\\\": \\\"Hussein\\\", \\\"sent_id\\\": 0, \\\"offset\\\": [13, 14], \\\"id\\\": \\\"a0e2bb391aab20feb6080309607d0b6c\\\"}, {\\\"trigger_word\\\": \\\"shoot\\\", \\\"sent_id\\\": 0, \\\"offset\\\": [15, 16], \\\"id\\\": \\\"1aa90bc43a1cc818f55136fe42e68971\\\"}, {\\\"trigger_word\\\": \\\"U-2\\\", \\\"sent_id\\\": 0, \\\"offset\\\": [17, 18], \\\"id\\\": \\\"f55d59671b304d4a76be6dd0fa67ca5f\\\"}, {\\\"trigger_word\\\": \\\"spy\\\", \\\"sent_id\\\": 0, \\\"offset\\\": [18, 19], \\\"id\\\": \\\"f700fc79fa829610e838b1568f137354\\\"}, {\\\"trigger_word\\\": \\\"planes\\\", \\\"sent_id\\\": 0, \\\"offset\\\": [19, 20], \\\"id\\\": \\\"bd8947756f304ac57eb9aa40d5a89304\\\"}, {\\\"trigger_word\\\": \\\"violate\\\", \\\"sent_id\\\": 0, \\\"offset\\\": [22, 23], \\\"id\\\": \\\"e99ce52748b7cb2ba2f57e8202ac80ae\\\"}, {\\\"trigger_word\\\": \\\"no-fly\\\", \\\"sent_id\\\": 0, \\\"offset\\\": [24, 25], \\\"id\\\": \\\"bf69cc28e38b6121291e33136f162d7e\\\"}, {\\\"trigger_word\\\": \\\"zone\\\", \\\"sent_id\\\": 0, \\\"offset\\\": [25, 26], \\\"id\\\": \\\"b329f37a3a6ac086349e15606e04916b\\\"}, {\\\"trigger_word\\\": \\\"set\\\", \\\"sent_id\\\": 0, \\\"offset\\\": [26, 27], \\\"id\\\": \\\"1938f340c87a8f5dca797c2924c43762\\\"}, {\\\"trigger_word\\\": \\\"country\\\", \\\"sent_id\\\": 0, \\\"offset\\\": [30, 31], \\\"id\\\": \\\"def3ab4b0fcc1ab0226e4f5fa8c22446\\\"}, {\\\"trigger_word\\\": \\\"operation\\\", \\\"sent_id\\\": 1, \\\"offset\\\": [1, 2], \\\"id\\\": \\\"34deaf3cff91ca21390a4859171db5ef\\\"}, {\\\"trigger_word\\\": \\\"designed\\\", \\\"sent_id\\\": 1, \\\"offset\\\": [3, 4], \\\"id\\\": \\\"2b9bac18715129370563c583790aadfd\\\"}, {\\\"trigger_word\\\": \\\"bring\\\", \\\"sent_id\\\": 1, \\\"offset\\\": [5, 6], \\\"id\\\": \\\"5b306eb0bf9ba4afa69e52d0de437099\\\"}, {\\\"trigger_word\\\": \\\"stability\\\", \\\"sent_id\\\": 1, \\\"offset\\\": [6, 7], \\\"id\\\": \\\"a7c8ef70395b61aff55c24ad85ca4acb\\\"}, {\\\"trigger_word\\\": \\\"region\\\", \\\"sent_id\\\": 1, \\\"offset\\\": [9, 10], \\\"id\\\": \\\"257b643b857ed0a050a1ce94dc08ffc2\\\"}, {\\\"trigger_word\\\": \\\"bringing\\\", \\\"sent_id\\\": 1, \\\"offset\\\": [11, 12], \\\"id\\\": \\\"3f9a6937c0bbd23c740e8fb1e415397d\\\"}, {\\\"trigger_word\\\": \\\"military\\\", \\\"sent_id\\\": 1, \\\"offset\\\": [14, 15], \\\"id\\\": \\\"71e521f35c11e2d48f40bc89b67fdd7c\\\"}, {\\\"trigger_word\\\": \\\"presence\\\", \\\"sent_id\\\": 1, \\\"offset\\\": [15, 16], \\\"id\\\": \\\"75d094396479e5a8e0c3b239c66dd193\\\"}, {\\\"trigger_word\\\": \\\"negotiations\\\", \\\"sent_id\\\": 1, \\\"offset\\\": [18, 19], \\\"id\\\": \\\"808baffe0ae132c7a78174f6332d8075\\\"}, {\\\"trigger_word\\\": \\\"Iraq\\\", \\\"sent_id\\\": 1, \\\"offset\\\": [20, 21], \\\"id\\\": \\\"2ddfe1825e3e68c9599fd4a2633e1091\\\"}, {\\\"trigger_word\\\": \\\"UN\\\", \\\"sent_id\\\": 1, \\\"offset\\\": [23, 24], \\\"id\\\": \\\"d8b3c50f1fd3903fde0d9d0ae81005b7\\\"}, {\\\"trigger_word\\\": \\\"weapons\\\", \\\"sent_id\\\": 1, \\\"offset\\\": [25, 26], \\\"id\\\": \\\"b96f5bcb5447c8dfd8daf5122ce91f5e\\\"}, {\\\"trigger_word\\\": \\\"mass\\\", \\\"sent_id\\\": 1, \\\"offset\\\": [27, 28], \\\"id\\\": \\\"e91b6233a4b566577119b9758785b561\\\"}, {\\\"trigger_word\\\": \\\"destruction\\\", \\\"sent_id\\\": 1, \\\"offset\\\": [28, 29], \\\"id\\\": \\\"2f3a44b58a00a840ab3db7ab6d9f8a88\\\"}, {\\\"trigger_word\\\": \\\"name\\\", \\\"sent_id\\\": 2, \\\"offset\\\": [1, 2], \\\"id\\\": \\\"0d7c3d34ac99ca513358739685149bbe\\\"}, {\\\"trigger_word\\\": \\\"Operation\\\", \\\"sent_id\\\": 2, \\\"offset\\\": [2, 3], \\\"id\\\": \\\"d8d931a2cfeaad47d628412af71da9c1\\\"}, {\\\"trigger_word\\\": \\\"Desert\\\", \\\"sent_id\\\": 2, \\\"offset\\\": [3, 4], \\\"id\\\": \\\"f8cdca46e2d941c319d5967e80b26b9c\\\"}, {\\\"trigger_word\\\": \\\"Thunder\\\", \\\"sent_id\\\": 2, \\\"offset\\\": [4, 5], \\\"id\\\": \\\"3c215006d8acf794724fcafd65fdc81a\\\"}, {\\\"trigger_word\\\": \\\"applied\\\", \\\"sent_id\\\": 2, \\\"offset\\\": [7, 8], \\\"id\\\": \\\"2a3e6dca3dad5fbef0a393f82511b5e9\\\"}, {\\\"trigger_word\\\": \\\"build-up\\\", \\\"sent_id\\\": 2, \\\"offset\\\": [10, 11], \\\"id\\\": \\\"15cf7c9d3391044d3a65c3372d16b4d4\\\"}, {\\\"trigger_word\\\": \\\"forces\\\", \\\"sent_id\\\": 2, \\\"offset\\\": [12, 13], \\\"id\\\": \\\"72b422c853f7a777f14d68c6ae1d2812\\\"}, {\\\"trigger_word\\\": \\\"Persian\\\", \\\"sent_id\\\": 2, \\\"offset\\\": [15, 16], \\\"id\\\": \\\"ea1044e6484bd24a8d27b28e08f99f3c\\\"}, {\\\"trigger_word\\\": \\\"Gulf\\\", \\\"sent_id\\\": 2, \\\"offset\\\": [16, 17], \\\"id\\\": \\\"e5a3a62f736e7dd4f42c750dd2cd419d\\\"}, {\\\"trigger_word\\\": \\\"region\\\", \\\"sent_id\\\": 2, \\\"offset\\\": [17, 18], \\\"id\\\": \\\"0b3072dcaf5a2a4bb464e999831efb83\\\"}, {\\\"trigger_word\\\": \\\"actual\\\", \\\"sent_id\\\": 3, \\\"offset\\\": [2, 3], \\\"id\\\": \\\"c1b14c2cda1c7dff3a4929baac81fdb3\\\"}, {\\\"trigger_word\\\": \\\"attack\\\", \\\"sent_id\\\": 3, \\\"offset\\\": [3, 4], \\\"id\\\": \\\"337f2db0d004b2c828d99170bbe8340f\\\"}, {\\\"trigger_word\\\": \\\"ordered\\\", \\\"sent_id\\\": 3, \\\"offset\\\": [6, 7], \\\"id\\\": \\\"948a91ac20387985c1e4ce4d73615a0d\\\"}, {\\\"trigger_word\\\": \\\"executed\\\", \\\"sent_id\\\": 3, \\\"offset\\\": [8, 9], \\\"id\\\": \\\"21df00d5abb387d7bda06692f7c3218b\\\"}, {\\\"trigger_word\\\": \\\"name\\\", \\\"sent_id\\\": 3, \\\"offset\\\": [11, 12], \\\"id\\\": \\\"f218be0ad57155a158bb7a9b00b5b674\\\"}, {\\\"trigger_word\\\": \\\"changed\\\", \\\"sent_id\\\": 3, \\\"offset\\\": [14, 15], \\\"id\\\": \\\"9658622044796a53660531b59f461ae3\\\"}, {\\\"trigger_word\\\": \\\"Operation\\\", \\\"sent_id\\\": 3, \\\"offset\\\": [16, 17], \\\"id\\\": \\\"137b7e269fb1df5e89d14ef7446da2e6\\\"}, {\\\"trigger_word\\\": \\\"Desert\\\", \\\"sent_id\\\": 3, \\\"offset\\\": [17, 18], \\\"id\\\": \\\"b80fb95f66e9e34c22f6d2ec0d6158ac\\\"}, {\\\"trigger_word\\\": \\\"Viper\\\", \\\"sent_id\\\": 3, \\\"offset\\\": [18, 19], \\\"id\\\": \\\"c888eb15094af591f1829d22682e989b\\\"}, {\\\"trigger_word\\\": \\\"autumn\\\", \\\"sent_id\\\": 4, \\\"offset\\\": [2, 3], \\\"id\\\": \\\"30745211547def5e9fc8760d33df9e9b\\\"}, {\\\"trigger_word\\\": \\\"CENTCOM\\\", \\\"sent_id\\\": 4, \\\"offset\\\": [5, 6], \\\"id\\\": \\\"1bb4d453a57b2625b1e0e1ccff0f18b9\\\"}, {\\\"trigger_word\\\": \\\"established\\\", \\\"sent_id\\\": 4, \\\"offset\\\": [6, 7], \\\"id\\\": \\\"afcb77a2058a394f9bfbab38352604a0\\\"}, {\\\"trigger_word\\\": \\\"force\\\", \\\"sent_id\\\": 4, \\\"offset\\\": [8, 9], \\\"id\\\": \\\"c7e30d00dfc777ab74edf35cfbe823b3\\\"}, {\\\"trigger_word\\\": \\\"air\\\", \\\"sent_id\\\": 4, \\\"offset\\\": [11, 12], \\\"id\\\": \\\"ca6cbab0111ef9815b2dfe06857b2220\\\"}, {\\\"trigger_word\\\": \\\"land\\\", \\\"sent_id\\\": 4, \\\"offset\\\": [13, 14], \\\"id\\\": \\\"f98589e0efed817ddb6651337a71d425\\\"}, {\\\"trigger_word\\\": \\\"sea\\\", \\\"sent_id\\\": 4, \\\"offset\\\": [16, 17], \\\"id\\\": \\\"af1b7ccb7556aa1790cba5b4b8a04204\\\"}, {\\\"trigger_word\\\": \\\"forces\\\", \\\"sent_id\\\": 4, \\\"offset\\\": [17, 18], \\\"id\\\": \\\"21a94eccdab7938691c91a02796b4c5c\\\"}, {\\\"trigger_word\\\": \\\"response\\\", \\\"sent_id\\\": 4, \\\"offset\\\": [19, 20], \\\"id\\\": \\\"372a3397c8b83b2e7aba81a577015c78\\\"}, {\\\"trigger_word\\\": \\\"Iraq\\\", \\\"sent_id\\\": 4, \\\"offset\\\": [21, 22], \\\"id\\\": \\\"159228e28d4c03bdeab15f4b32171026\\\"}, {\\\"trigger_word\\\": \\\"non-compliance\\\", \\\"sent_id\\\": 4, \\\"offset\\\": [23, 24], \\\"id\\\": \\\"97a9b971793ffb129fe0c5e5ac0b8150\\\"}, {\\\"trigger_word\\\": \\\"UN\\\", \\\"sent_id\\\": 4, \\\"offset\\\": [25, 26], \\\"id\\\": \\\"bb930fb719110996fd8dc08f1bbcbaa4\\\"}, {\\\"trigger_word\\\": \\\"resolutions\\\", \\\"sent_id\\\": 4, \\\"offset\\\": [26, 27], \\\"id\\\": \\\"8480a855b7e6b195238df87828e46ee1\\\"}, {\\\"trigger_word\\\": \\\"centcom\\\", \\\"sent_id\\\": 5, \\\"offset\\\": [0, 1], \\\"id\\\": \\\"eefd45951f59361abc2d9b140dcbd26a\\\"}, {\\\"trigger_word\\\": \\\"commander-in-chief\\\", \\\"sent_id\\\": 5, \\\"offset\\\": [1, 2], \\\"id\\\": \\\"0900b6b66b72f72499b65b4110752d81\\\"}, {\\\"trigger_word\\\": \\\"general\\\", \\\"sent_id\\\": 5, \\\"offset\\\": [2, 3], \\\"id\\\": \\\"18e0c2c288ab5e3c5d102b1d92b5873d\\\"}, {\\\"trigger_word\\\": \\\"anthony\\\", \\\"sent_id\\\": 5, \\\"offset\\\": [3, 4], \\\"id\\\": \\\"002e05853611b8ca42afc050d86e7566\\\"}, {\\\"trigger_word\\\": \\\"zinni\\\", \\\"sent_id\\\": 5, \\\"offset\\\": [4, 5], \\\"id\\\": \\\"25f39c8aa2af8c7d6cc9fa5f77dbd5be\\\"}, {\\\"trigger_word\\\": \\\"established\\\", \\\"sent_id\\\": 5, \\\"offset\\\": [5, 6], \\\"id\\\": \\\"eca12db448a4a965c2c748eb9fdbfc89\\\"}, {\\\"trigger_word\\\": \\\"permanent\\\", \\\"sent_id\\\": 5, \\\"offset\\\": [7, 8], \\\"id\\\": \\\"0c9e7c2ba5cb4c85b8c3accc8da18b7d\\\"}, {\\\"trigger_word\\\": \\\"unk\\\", \\\"sent_id\\\": 5, \\\"offset\\\": [8, 9], \\\"id\\\": \\\"4e5203c468a6d0a2ef6482e01fe38f66\\\"}, {\\\"trigger_word\\\": \\\"task\\\", \\\"sent_id\\\": 5, \\\"offset\\\": [9, 10], \\\"id\\\": \\\"51445be58d67337790b4dfde14e783d0\\\"}, {\\\"trigger_word\\\": \\\"force\\\", \\\"sent_id\\\": 5, \\\"offset\\\": [10, 11], \\\"id\\\": \\\"855b43aaccb95d98db33785eff641a1a\\\"}, {\\\"trigger_word\\\": \\\"unk\\\", \\\"sent_id\\\": 5, \\\"offset\\\": [12, 13], \\\"id\\\": \\\"e95ce219712865c69ff2dc09e7aa0ace\\\"}, {\\\"trigger_word\\\": \\\"camp\\\", \\\"sent_id\\\": 5, \\\"offset\\\": [15, 16], \\\"id\\\": \\\"de4d859f195b2db44cbb33016295e284\\\"}, {\\\"trigger_word\\\": \\\"doha\\\", \\\"sent_id\\\": 5, \\\"offset\\\": [16, 17], \\\"id\\\": \\\"d65cf9da15b5866bea8c8726069d6ef7\\\"}, {\\\"trigger_word\\\": \\\"kuwait\\\", \\\"sent_id\\\": 5, \\\"offset\\\": [18, 19], \\\"id\\\": \\\"4dbe2fc69d86af86dda3a594249cee68\\\"}, {\\\"trigger_word\\\": \\\"command\\\", \\\"sent_id\\\": 5, \\\"offset\\\": [20, 21], \\\"id\\\": \\\"d9569b684fccf30274fc19f0b5a8af3e\\\"}, {\\\"trigger_word\\\": \\\"lieutenant\\\", \\\"sent_id\\\": 5, \\\"offset\\\": [22, 23], \\\"id\\\": \\\"8c02466cbd4523eb4e142481da1809fe\\\"}, {\\\"trigger_word\\\": \\\"general\\\", \\\"sent_id\\\": 5, \\\"offset\\\": [23, 24], \\\"id\\\": \\\"a0e664cb3ce19d45fd26bdcc80021132\\\"}, {\\\"trigger_word\\\": \\\"tommy\\\", \\\"sent_id\\\": 5, \\\"offset\\\": [24, 25], \\\"id\\\": \\\"7895c4a6b07dc4ba701b44302d9ca39e\\\"}, {\\\"trigger_word\\\": \\\"franks\\\", \\\"sent_id\\\": 5, \\\"offset\\\": [25, 26], \\\"id\\\": \\\"01131ef4793c6a433a5e46b28299c54e\\\"}, {\\\"trigger_word\\\": \\\"lead\\\", \\\"sent_id\\\": 5, \\\"offset\\\": [27, 28], \\\"id\\\": \\\"d074c3f3c92263e6187dec338b54932c\\\"}, {\\\"trigger_word\\\": \\\"force\\\", \\\"sent_id\\\": 5, \\\"offset\\\": [29, 30], \\\"id\\\": \\\"f39cabfe0fb8206345dd1546040083e0\\\"}, {\\\"trigger_word\\\": \\\"coalition\\\", \\\"sent_id\\\": 6, \\\"offset\\\": [1, 2], \\\"id\\\": \\\"d19c0e6fbc5793ea69e62d47593d419b\\\"}, {\\\"trigger_word\\\": \\\"forces\\\", \\\"sent_id\\\": 6, \\\"offset\\\": [5, 6], \\\"id\\\": \\\"9e80a36cf5fd752dec373fac96b5d8cd\\\"}, {\\\"trigger_word\\\": \\\"Argentina\\\", \\\"sent_id\\\": 6, \\\"offset\\\": [7, 8], \\\"id\\\": \\\"8ec58b0a9d1f3311ee21a3540d4d6496\\\"}, {\\\"trigger_word\\\": \\\"Australia\\\", \\\"sent_id\\\": 6, \\\"offset\\\": [9, 10], \\\"id\\\": \\\"c77ea4fccf0f4b374756a989b7da1b28\\\"}, {\\\"trigger_word\\\": \\\"Canada\\\", \\\"sent_id\\\": 6, \\\"offset\\\": [11, 12], \\\"id\\\": \\\"37bb99c5821c7fb5be5cdb6a6edaf4b3\\\"}, {\\\"trigger_word\\\": \\\"Czech\\\", \\\"sent_id\\\": 6, \\\"offset\\\": [13, 14], \\\"id\\\": \\\"ba872c91329c484c51ead7b625c655ec\\\"}, {\\\"trigger_word\\\": \\\"Republic\\\", \\\"sent_id\\\": 6, \\\"offset\\\": [14, 15], \\\"id\\\": \\\"2a9b688c02779c2be110e8dd337f1637\\\"}, {\\\"trigger_word\\\": \\\"Hungary\\\", \\\"sent_id\\\": 6, \\\"offset\\\": [16, 17], \\\"id\\\": \\\"65cc7557c40538e7bda8d0b3ea7ff8bd\\\"}, {\\\"trigger_word\\\": \\\"New\\\", \\\"sent_id\\\": 6, \\\"offset\\\": [18, 19], \\\"id\\\": \\\"ca79a20cd2e61f3df119b1da57bdbbd8\\\"}, {\\\"trigger_word\\\": \\\"Zealand\\\", \\\"sent_id\\\": 6, \\\"offset\\\": [19, 20], \\\"id\\\": \\\"3c85c0978bb9edbbef76c5d64c71dd5c\\\"}, {\\\"trigger_word\\\": \\\"Poland\\\", \\\"sent_id\\\": 6, \\\"offset\\\": [21, 22], \\\"id\\\": \\\"2de05d2246aad82afa7b08a29d907cfa\\\"}, {\\\"trigger_word\\\": \\\"Romania\\\", \\\"sent_id\\\": 6, \\\"offset\\\": [23, 24], \\\"id\\\": \\\"78c7a1c0a7aadec0a85feaed0e04df33\\\"}, {\\\"trigger_word\\\": \\\"United\\\", \\\"sent_id\\\": 6, \\\"offset\\\": [25, 26], \\\"id\\\": \\\"d83c676f37acacb68a537aaad73ff256\\\"}, {\\\"trigger_word\\\": \\\"Kingdom\\\", \\\"sent_id\\\": 6, \\\"offset\\\": [26, 27], \\\"id\\\": \\\"a32a2d5deafbbba3f20014573c28bf9c\\\"}, {\\\"trigger_word\\\": \\\"United\\\", \\\"sent_id\\\": 6, \\\"offset\\\": [28, 29], \\\"id\\\": \\\"03906ea06fe81827cabcad0749ed3eda\\\"}, {\\\"trigger_word\\\": \\\"States\\\", \\\"sent_id\\\": 6, \\\"offset\\\": [29, 30], \\\"id\\\": \\\"462ad3fcaa81be67ab02ff2c228e9b50\\\"}, {\\\"trigger_word\\\": \\\"Kuwait\\\", \\\"sent_id\\\": 6, \\\"offset\\\": [32, 33], \\\"id\\\": \\\"d8b302168c00b8de18c0e1441e1f3e76\\\"}, {\\\"trigger_word\\\": \\\"January\\\", \\\"sent_id\\\": 7, \\\"offset\\\": [2, 3], \\\"id\\\": \\\"64e04ba05a2c94a49dbad09730b2b9c7\\\"}, {\\\"trigger_word\\\": \\\"additional\\\", \\\"sent_id\\\": 7, \\\"offset\\\": [4, 5], \\\"id\\\": \\\"f172bfa91259b6bf629ab405b3beb0db\\\"}, {\\\"trigger_word\\\": \\\"forces\\\", \\\"sent_id\\\": 7, \\\"offset\\\": [5, 6], \\\"id\\\": \\\"73bf17d40b9759082ddca200f2cf2f71\\\"}, {\\\"trigger_word\\\": \\\"brought in\\\", \\\"sent_id\\\": 7, \\\"offset\\\": [7, 9], \\\"id\\\": \\\"92602edeb221d1e9163913f254c8a69f\\\"}, {\\\"trigger_word\\\": \\\"support\\\", \\\"sent_id\\\": 7, \\\"offset\\\": [10, 11], \\\"id\\\": \\\"e1aefc52d539318a000d56503567260f\\\"}, {\\\"trigger_word\\\": \\\"U.S.-led\\\", \\\"sent_id\\\": 7, \\\"offset\\\": [12, 13], \\\"id\\\": \\\"4293c2d1e91a273905becf63bb38a0fa\\\"}, {\\\"trigger_word\\\": \\\"coalition\\\", \\\"sent_id\\\": 7, \\\"offset\\\": [13, 14], \\\"id\\\": \\\"cf3cbb5e25ed7b0cb434dae77093bd26\\\"}, {\\\"trigger_word\\\": \\\"forces\\\", \\\"sent_id\\\": 7, \\\"offset\\\": [14, 15], \\\"id\\\": \\\"511e21b448bdeffdd9160be520c155fc\\\"}, {\\\"trigger_word\\\": \\\"region\\\", \\\"sent_id\\\": 7, \\\"offset\\\": [17, 18], \\\"id\\\": \\\"5cbc331b4ab41801594c98f1311efdb2\\\"}, {\\\"trigger_word\\\": \\\"U.S.\\\", \\\"sent_id\\\": 8, \\\"offset\\\": [1, 2], \\\"id\\\": \\\"fa2cea98e38daf82b6ebab1d379601bd\\\"}, {\\\"trigger_word\\\": \\\"Infantry\\\", \\\"sent_id\\\": 8, \\\"offset\\\": [3, 4], \\\"id\\\": \\\"f9a8c9c9b1bd8c2d2d7c144022b3cda3\\\"}, {\\\"trigger_word\\\": \\\"Division\\\", \\\"sent_id\\\": 8, \\\"offset\\\": [4, 5], \\\"id\\\": \\\"ad1e1c86573a6b86cfb1bf2620f48a96\\\"}, {\\\"trigger_word\\\": \\\"Fort\\\", \\\"sent_id\\\": 8, \\\"offset\\\": [6, 7], \\\"id\\\": \\\"2d40c8f5846bbe4d1ec19862b35a99e3\\\"}, {\\\"trigger_word\\\": \\\"Stewart\\\", \\\"sent_id\\\": 8, \\\"offset\\\": [7, 8], \\\"id\\\": \\\"4c394237da29796601b84edf480faa4e\\\"}, {\\\"trigger_word\\\": \\\"Georgia\\\", \\\"sent_id\\\": 8, \\\"offset\\\": [9, 10], \\\"id\\\": \\\"9069cd33b2aa804796bbbef7acd42953\\\"}, {\\\"trigger_word\\\": \\\"deployed\\\", \\\"sent_id\\\": 8, \\\"offset\\\": [11, 12], \\\"id\\\": \\\"3f67eeb95dd29ca1760b77357fb48891\\\"}, {\\\"trigger_word\\\": \\\"personnel\\\", \\\"sent_id\\\": 8, \\\"offset\\\": [13, 14], \\\"id\\\": \\\"129ef3ee47b5caa903e5709be58c7059\\\"}, {\\\"trigger_word\\\": \\\"short\\\", \\\"sent_id\\\": 8, \\\"offset\\\": [16, 17], \\\"id\\\": \\\"103f994831c6b3eaa06deef129cdb261\\\"}, {\\\"trigger_word\\\": \\\"tons\\\", \\\"sent_id\\\": 8, \\\"offset\\\": [17, 18], \\\"id\\\": \\\"aab21f938b25d486d1c04872b301a37a\\\"}, {\\\"trigger_word\\\": \\\"equipment\\\", \\\"sent_id\\\": 8, \\\"offset\\\": [19, 20], \\\"id\\\": \\\"020cb20e0355ee3f3af90e84f95a894b\\\"}, {\\\"trigger_word\\\": \\\"aircraft\\\", \\\"sent_id\\\": 8, \\\"offset\\\": [22, 23], \\\"id\\\": \\\"1321da38c9de335ab787aa8a73b10907\\\"}, {\\\"trigger_word\\\": \\\"elements\\\", \\\"sent_id\\\": 9, \\\"offset\\\": [0, 1], \\\"id\\\": \\\"ed54bd3491ccb327f76d472a10a900ca\\\"}, {\\\"trigger_word\\\": \\\"air\\\", \\\"sent_id\\\": 9, \\\"offset\\\": [3, 4], \\\"id\\\": \\\"5ca0e03cd41f2e7da33b32afeb5e27f9\\\"}, {\\\"trigger_word\\\": \\\"missile\\\", \\\"sent_id\\\": 9, \\\"offset\\\": [5, 6], \\\"id\\\": \\\"44395b07303d3687a18d4415f63e0559\\\"}, {\\\"trigger_word\\\": \\\"defense\\\", \\\"sent_id\\\": 9, \\\"offset\\\": [6, 7], \\\"id\\\": \\\"f805893485cd432b753524b1a2a1f443\\\"}, {\\\"trigger_word\\\": \\\"command\\\", \\\"sent_id\\\": 9, \\\"offset\\\": [7, 8], \\\"id\\\": \\\"9cfac640a0d5ca175566198ac7f591cb\\\"}, {\\\"trigger_word\\\": \\\"battalion\\\", \\\"sent_id\\\": 9, \\\"offset\\\": [10, 11], \\\"id\\\": \\\"9dd9070b24945db19c100365dc5374ff\\\"}, {\\\"trigger_word\\\": \\\"parachute\\\", \\\"sent_id\\\": 9, \\\"offset\\\": [12, 13], \\\"id\\\": \\\"7e3118314cc33653009ba8c63e23cd11\\\"}, {\\\"trigger_word\\\": \\\"infantry\\\", \\\"sent_id\\\": 9, \\\"offset\\\": [13, 14], \\\"id\\\": \\\"eb729e2145cd74d1a3039c5df05013f8\\\"}, {\\\"trigger_word\\\": \\\"regiment\\\", \\\"sent_id\\\": 9, \\\"offset\\\": [14, 15], \\\"id\\\": \\\"cb17817ff5f1cfbb1a54a9869f9da63e\\\"}, {\\\"trigger_word\\\": \\\"airborne\\\", \\\"sent_id\\\": 9, \\\"offset\\\": [17, 18], \\\"id\\\": \\\"9acda512c595cfed6498df7311c6158b\\\"}, {\\\"trigger_word\\\": \\\"division\\\", \\\"sent_id\\\": 9, \\\"offset\\\": [18, 19], \\\"id\\\": \\\"f51845f4120fd5d50bed492deda29891\\\"}, {\\\"trigger_word\\\": \\\"fort\\\", \\\"sent_id\\\": 9, \\\"offset\\\": [20, 21], \\\"id\\\": \\\"6912c75e1d357097cf42af6d29864396\\\"}, {\\\"trigger_word\\\": \\\"bragg\\\", \\\"sent_id\\\": 9, \\\"offset\\\": [21, 22], \\\"id\\\": \\\"cb66ca3976a1a3666f4a38c4c5a7f095\\\"}, {\\\"trigger_word\\\": \\\"nc\\\", \\\"sent_id\\\": 9, \\\"offset\\\": [23, 24], \\\"id\\\": \\\"ddce78a02d497865d387583b5a369fa7\\\"}, {\\\"trigger_word\\\": \\\"deployed\\\", \\\"sent_id\\\": 9, \\\"offset\\\": [25, 26], \\\"id\\\": \\\"33f2b088b83ad15f918e6bf1982fa966\\\"}, {\\\"trigger_word\\\": \\\"saudi\\\", \\\"sent_id\\\": 9, \\\"offset\\\": [27, 28], \\\"id\\\": \\\"32cc9b116bf11cec17249134d74ac632\\\"}, {\\\"trigger_word\\\": \\\"arabia\\\", \\\"sent_id\\\": 9, \\\"offset\\\": [28, 29], \\\"id\\\": \\\"3118e00a69c3096a8e7552f7bf0bae0b\\\"}, {\\\"trigger_word\\\": \\\"kuwait\\\", \\\"sent_id\\\": 9, \\\"offset\\\": [30, 31], \\\"id\\\": \\\"e4334a26cc8c1a37e56c3ea7b0eab3e8\\\"}, {\\\"trigger_word\\\": \\\"bahrain\\\", \\\"sent_id\\\": 9, \\\"offset\\\": [32, 33], \\\"id\\\": \\\"62a823f913577419c007a133c4837da8\\\"}, {\\\"trigger_word\\\": \\\"air\\\", \\\"sent_id\\\": 10, \\\"offset\\\": [2, 3], \\\"id\\\": \\\"172fd2d8c1e31ba9ced7b71c44c885d1\\\"}, {\\\"trigger_word\\\": \\\"expeditionary\\\", \\\"sent_id\\\": 10, \\\"offset\\\": [3, 4], \\\"id\\\": \\\"f8c23fb6e338ec4f8328218badb53590\\\"}, {\\\"trigger_word\\\": \\\"wing\\\", \\\"sent_id\\\": 10, \\\"offset\\\": [4, 5], \\\"id\\\": \\\"4ee407cef8229a63c505b6c059302de3\\\"}, {\\\"trigger_word\\\": \\\"mountain\\\", \\\"sent_id\\\": 10, \\\"offset\\\": [6, 7], \\\"id\\\": \\\"6d53fdf1674608dc0c4f798f470b2b23\\\"}, {\\\"trigger_word\\\": \\\"home\\\", \\\"sent_id\\\": 10, \\\"offset\\\": [7, 8], \\\"id\\\": \\\"b79e5a5fdbd02e5518fc59d8cc91cfa6\\\"}, {\\\"trigger_word\\\": \\\"air\\\", \\\"sent_id\\\": 10, \\\"offset\\\": [8, 9], \\\"id\\\": \\\"09722961589ae2f428b4c562512334b3\\\"}, {\\\"trigger_word\\\": \\\"force\\\", \\\"sent_id\\\": 10, \\\"offset\\\": [9, 10], \\\"id\\\": \\\"a83d024a3b56b75e095d2753d0e16a87\\\"}, {\\\"trigger_word\\\": \\\"base\\\", \\\"sent_id\\\": 10, \\\"offset\\\": [10, 11], \\\"id\\\": \\\"d28e0b75851e621b9a7bb2c1685e7079\\\"}, {\\\"trigger_word\\\": \\\"id\\\", \\\"sent_id\\\": 10, \\\"offset\\\": [12, 13], \\\"id\\\": \\\"bc7a13fbbe6d84bf8070272a8d2c3fdf\\\"}, {\\\"trigger_word\\\": \\\"air\\\", \\\"sent_id\\\": 10, \\\"offset\\\": [16, 17], \\\"id\\\": \\\"b44ee1db3b43e7f7030707cb38e23368\\\"}, {\\\"trigger_word\\\": \\\"expeditionary\\\", \\\"sent_id\\\": 10, \\\"offset\\\": [17, 18], \\\"id\\\": \\\"10d5abde1465319f6bac56652bfe0475\\\"}, {\\\"trigger_word\\\": \\\"wing\\\", \\\"sent_id\\\": 10, \\\"offset\\\": [18, 19], \\\"id\\\": \\\"1561aaa4492b10f14f1fda14993685ee\\\"}, {\\\"trigger_word\\\": \\\"moody\\\", \\\"sent_id\\\": 10, \\\"offset\\\": [20, 21], \\\"id\\\": \\\"76bf18622ccdba98d505e38d52326a19\\\"}, {\\\"trigger_word\\\": \\\"afb\\\", \\\"sent_id\\\": 10, \\\"offset\\\": [21, 22], \\\"id\\\": \\\"ee928eff21ed00c163c14d33a1c5a8d6\\\"}, {\\\"trigger_word\\\": \\\"georgia\\\", \\\"sent_id\\\": 10, \\\"offset\\\": [23, 24], \\\"id\\\": \\\"b81f0d0561810350abdbb48d8402a262\\\"}, {\\\"trigger_word\\\": \\\"april\\\", \\\"sent_id\\\": 10, \\\"offset\\\": [26, 27], \\\"id\\\": \\\"0db06a221c1d9939eaf0ac7d49a308bb\\\"}, {\\\"trigger_word\\\": \\\"days\\\", \\\"sent_id\\\": 10, \\\"offset\\\": [30, 31], \\\"id\\\": \\\"f020b730472a7e0d74317404e81b69a2\\\"}, {\\\"trigger_word\\\": \\\"deployment\\\", \\\"sent_id\\\": 10, \\\"offset\\\": [32, 33], \\\"id\\\": \\\"8d5a9b89066c7537417581bfb4c83191\\\"}, {\\\"trigger_word\\\": \\\"USS\\\", \\\"sent_id\\\": 11, \\\"offset\\\": [0, 1], \\\"id\\\": \\\"b69237b31ac803522eead5dc99ec06c5\\\"}, {\\\"trigger_word\\\": \\\"George\\\", \\\"sent_id\\\": 11, \\\"offset\\\": [2, 3], \\\"id\\\": \\\"ea0262944e8ab10ad2eb13fbbfc3754e\\\"}, {\\\"trigger_word\\\": \\\"Washington\\\", \\\"sent_id\\\": 11, \\\"offset\\\": [3, 4], \\\"id\\\": \\\"2396665e3becdd9c6168db80cc0b1ba5\\\"}, {\\\"trigger_word\\\": \\\"CVN-73\\\", \\\"sent_id\\\": 11, \\\"offset\\\": [6, 7], \\\"id\\\": \\\"438c0deb7f641d382efa02d02bd4fddb\\\"}, {\\\"trigger_word\\\": \\\"joined\\\", \\\"sent_id\\\": 11, \\\"offset\\\": [8, 9], \\\"id\\\": \\\"763852765abfbee1f591e7d17e3f18a7\\\"}, {\\\"trigger_word\\\": \\\"USS\\\", \\\"sent_id\\\": 11, \\\"offset\\\": [9, 10], \\\"id\\\": \\\"e7a315af885c7b7d294379c5d8cfed0a\\\"}, {\\\"trigger_word\\\": \\\"Nimitz\\\", \\\"sent_id\\\": 11, \\\"offset\\\": [11, 12], \\\"id\\\": \\\"acccb53ee8396a904be15ae200e93c8c\\\"}, {\\\"trigger_word\\\": \\\"CVN-68\\\", \\\"sent_id\\\": 11, \\\"offset\\\": [14, 15], \\\"id\\\": \\\"c2ca6b55aa22d2b1b52d0e2bc2436329\\\"}, {\\\"trigger_word\\\": \\\"relieved\\\", \\\"sent_id\\\": 11, \\\"offset\\\": [17, 18], \\\"id\\\": \\\"f87dcd755840580a6e09f10cc10fae20\\\"}, {\\\"trigger_word\\\": \\\"on-station\\\", \\\"sent_id\\\": 11, \\\"offset\\\": [18, 19], \\\"id\\\": \\\"16576e786b06ea0357219af508aebb78\\\"}, {\\\"trigger_word\\\": \\\"USS\\\", \\\"sent_id\\\": 11, \\\"offset\\\": [20, 21], \\\"id\\\": \\\"f2d63544d18770c236b3ca465a5c481f\\\"}, {\\\"trigger_word\\\": \\\"Independence\\\", \\\"sent_id\\\": 11, \\\"offset\\\": [22, 23], \\\"id\\\": \\\"84dbc73f6ef064dbb9c363f49f3f9be8\\\"}, {\\\"trigger_word\\\": \\\"CV-62\\\", \\\"sent_id\\\": 11, \\\"offset\\\": [25, 26], \\\"id\\\": \\\"429ccd6c5a4cb8cb3ab693e59e5bbc9b\\\"}, {\\\"trigger_word\\\": \\\"months\\\", \\\"sent_id\\\": 11, \\\"offset\\\": [29, 30], \\\"id\\\": \\\"3df526e687ad197cb1266673af9ac383\\\"}, {\\\"trigger_word\\\": \\\"later\\\", \\\"sent_id\\\": 11, \\\"offset\\\": [30, 31], \\\"id\\\": \\\"965ef678216993c6e956d58a64ca52e9\\\"}, {\\\"trigger_word\\\": \\\"Gulf\\\", \\\"sent_id\\\": 11, \\\"offset\\\": [34, 35], \\\"id\\\": \\\"4f06fec5b34318573ada722b3a4e4a88\\\"}, {\\\"trigger_word\\\": \\\"Combined\\\", \\\"sent_id\\\": 12, \\\"offset\\\": [0, 1], \\\"id\\\": \\\"2a46ab88086e8db350d8b8cae6b06039\\\"}, {\\\"trigger_word\\\": \\\"British\\\", \\\"sent_id\\\": 12, \\\"offset\\\": [3, 4], \\\"id\\\": \\\"0e5ab094203fc7848c02737d4b51f159\\\"}, {\\\"trigger_word\\\": \\\"HMS\\\", \\\"sent_id\\\": 12, \\\"offset\\\": [4, 5], \\\"id\\\": \\\"2648ebfef5a171ae9d244a8713df1ba3\\\"}, {\\\"trigger_word\\\": \\\"Invincible\\\", \\\"sent_id\\\": 12, \\\"offset\\\": [6, 7], \\\"id\\\": \\\"ebfa5aef9f02f09c7c64bb02787b8668\\\"}, {\\\"trigger_word\\\": \\\"R05\\\", \\\"sent_id\\\": 12, \\\"offset\\\": [9, 10], \\\"id\\\": \\\"baef8791cba8637cccf23c2912186963\\\"}, {\\\"trigger_word\\\": \\\"HMS\\\", \\\"sent_id\\\": 12, \\\"offset\\\": [12, 13], \\\"id\\\": \\\"77a72b2cc89cb7f52d8cea36c7b5a100\\\"}, {\\\"trigger_word\\\": \\\"Illustrious\\\", \\\"sent_id\\\": 12, \\\"offset\\\": [14, 15], \\\"id\\\": \\\"c09b52ca92305183e688fabe5a661f8d\\\"}, {\\\"trigger_word\\\": \\\"R06\\\", \\\"sent_id\\\": 12, \\\"offset\\\": [17, 18], \\\"id\\\": \\\"dc6736ad519bb38557d7c3ca40b81b2f\\\"}, {\\\"trigger_word\\\": \\\"ships\\\", \\\"sent_id\\\": 12, \\\"offset\\\": [24, 25], \\\"id\\\": \\\"f396cea59f5ad33d2544daeccfb1b143\\\"}, {\\\"trigger_word\\\": \\\"submarines\\\", \\\"sent_id\\\": 12, \\\"offset\\\": [26, 27], \\\"id\\\": \\\"752338df02d5fb6581aac5ffab7bf802\\\"}, {\\\"trigger_word\\\": \\\"naval\\\", \\\"sent_id\\\": 12, \\\"offset\\\": [29, 30], \\\"id\\\": \\\"1707d071ca4401cbe48576a1de4988bf\\\"}, {\\\"trigger_word\\\": \\\"aircraft\\\", \\\"sent_id\\\": 12, \\\"offset\\\": [30, 31], \\\"id\\\": \\\"ca03f256d120c65e65996d7ea6587b39\\\"}, {\\\"trigger_word\\\": \\\"floating\\\", \\\"sent_id\\\": 12, \\\"offset\\\": [33, 34], \\\"id\\\": \\\"4b788249679af7e26b0d77d387f38bf9\\\"}, {\\\"trigger_word\\\": \\\"brigade\\\", \\\"sent_id\\\": 12, \\\"offset\\\": [34, 35], \\\"id\\\": \\\"c1922dac057f1b6ac076360f3ae19f26\\\"}, {\\\"trigger_word\\\": \\\"Army\\\", \\\"sent_id\\\": 12, \\\"offset\\\": [36, 37], \\\"id\\\": \\\"36cc23ff6b1fdf5908745a41e4ab69ed\\\"}, {\\\"trigger_word\\\": \\\"Marine\\\", \\\"sent_id\\\": 12, \\\"offset\\\": [41, 42], \\\"id\\\": \\\"3d824d71349e8d822a674fdc788e6715\\\"}, {\\\"trigger_word\\\": \\\"Expeditionary\\\", \\\"sent_id\\\": 12, \\\"offset\\\": [42, 43], \\\"id\\\": \\\"9e525a86e023c3a539ebc9be490b48e4\\\"}, {\\\"trigger_word\\\": \\\"Unit\\\", \\\"sent_id\\\": 12, \\\"offset\\\": [43, 44], \\\"id\\\": \\\"53145385e51e4ace36b979e8982f6c19\\\"}, {\\\"trigger_word\\\": \\\"Persian\\\", \\\"sent_id\\\": 12, \\\"offset\\\": [46, 47], \\\"id\\\": \\\"857f549e524e19b0b458f2fdcced5c5a\\\"}, {\\\"trigger_word\\\": \\\"Gulf\\\", \\\"sent_id\\\": 12, \\\"offset\\\": [47, 48], \\\"id\\\": \\\"8b02f1f9d68bf99caff604fc4c513982\\\"}, {\\\"trigger_word\\\": \\\"combined\\\", \\\"sent_id\\\": 13, \\\"offset\\\": [1, 2], \\\"id\\\": \\\"68760ac099f42764abf2d7948b73dbbc\\\"}, {\\\"trigger_word\\\": \\\"muscle\\\", \\\"sent_id\\\": 13, \\\"offset\\\": [2, 3], \\\"id\\\": \\\"39d14444ee62fb66500157ccde877764\\\"}, {\\\"trigger_word\\\": \\\"forced\\\", \\\"sent_id\\\": 13, \\\"offset\\\": [3, 4], \\\"id\\\": \\\"4429b11654c956187e2e8ad0e893cf9b\\\"}, {\\\"trigger_word\\\": \\\"Saddam\\\", \\\"sent_id\\\": 13, \\\"offset\\\": [4, 5], \\\"id\\\": \\\"cac5d1d61a837634b0d835775c121821\\\"}, {\\\"trigger_word\\\": \\\"back\\\", \\\"sent_id\\\": 13, \\\"offset\\\": [6, 7], \\\"id\\\": \\\"08b80bc3355320c28ad69eba7c141784\\\"}, {\\\"trigger_word\\\": \\\"Independence\\\", \\\"sent_id\\\": 13, \\\"offset\\\": [12, 13], \\\"id\\\": \\\"feb574020eaeaf6d2b7cba37101b329d\\\"}, {\\\"trigger_word\\\": \\\"returned\\\", \\\"sent_id\\\": 13, \\\"offset\\\": [14, 15], \\\"id\\\": \\\"35c9110395ef1143ec8622641e03fb0b\\\"}, {\\\"trigger_word\\\": \\\"Yokosuka\\\", \\\"sent_id\\\": 13, \\\"offset\\\": [16, 17], \\\"id\\\": \\\"1d1b892d9360cd8b63c440e75134beba\\\"}, {\\\"trigger_word\\\": \\\"Japan\\\", \\\"sent_id\\\": 13, \\\"offset\\\": [18, 19], \\\"id\\\": \\\"04305dfc4c971ef4f0e3274d09c7a2d9\\\"}, {\\\"trigger_word\\\": \\\"early\\\", \\\"sent_id\\\": 13, \\\"offset\\\": [20, 21], \\\"id\\\": \\\"d0a5d38149b085d788f01f8d3a45ee6c\\\"}, {\\\"trigger_word\\\": \\\"June\\\", \\\"sent_id\\\": 13, \\\"offset\\\": [21, 22], \\\"id\\\": \\\"2b8889cbaf7bc93ad9a4c9893ddf3531\\\"}, {\\\"trigger_word\\\": \\\"July\\\", \\\"sent_id\\\": 14, \\\"offset\\\": [1, 2], \\\"id\\\": \\\"2887c843a19b66b48d565aac6a033eb5\\\"}, {\\\"trigger_word\\\": \\\"3-101st\\\", \\\"sent_id\\\": 14, \\\"offset\\\": [4, 5], \\\"id\\\": \\\"f696a22afacfb8f1dbadf1f12b104989\\\"}, {\\\"trigger_word\\\": \\\"Attk\\\", \\\"sent_id\\\": 14, \\\"offset\\\": [5, 6], \\\"id\\\": \\\"cc9fdb3c27a2e9424b74afdf33a15b27\\\"}, {\\\"trigger_word\\\": \\\"Avn\\\", \\\"sent_id\\\": 14, \\\"offset\\\": [6, 7], \\\"id\\\": \\\"b80168871fe93598208929b1c23ccefd\\\"}, {\\\"trigger_word\\\": \\\"Bn\\\", \\\"sent_id\\\": 14, \\\"offset\\\": [7, 8], \\\"id\\\": \\\"a892332ba7854c9300df82a45265adfa\\\"}, {\\\"trigger_word\\\": \\\"deployed\\\", \\\"sent_id\\\": 14, \\\"offset\\\": [8, 9], \\\"id\\\": \\\"b83b4ae00fac446d328a9bff536f1d8e\\\"}, {\\\"trigger_word\\\": \\\"AH-64A\\\", \\\"sent_id\\\": 14, \\\"offset\\\": [10, 11], \\\"id\\\": \\\"4c37c3f5e13accc9fa9175c19dc6b7a8\\\"}, {\\\"trigger_word\\\": \\\"Companies\\\", \\\"sent_id\\\": 14, \\\"offset\\\": [11, 12], \\\"id\\\": \\\"f47f7753118965072442ff48afa6d112\\\"}, {\\\"trigger_word\\\": \\\"Ali\\\", \\\"sent_id\\\": 14, \\\"offset\\\": [13, 14], \\\"id\\\": \\\"d3084af766c866cd067c0fe4a6114b8a\\\"}, {\\\"trigger_word\\\": \\\"Al\\\", \\\"sent_id\\\": 14, \\\"offset\\\": [14, 15], \\\"id\\\": \\\"0116b1e6ab305205ba854c244f5acbe9\\\"}, {\\\"trigger_word\\\": \\\"Salem\\\", \\\"sent_id\\\": 14, \\\"offset\\\": [15, 16], \\\"id\\\": \\\"42dd7ca56ea429b7ce30c14adbd8e642\\\"}, {\\\"trigger_word\\\": \\\"AB\\\", \\\"sent_id\\\": 14, \\\"offset\\\": [16, 17], \\\"id\\\": \\\"198ad96432bee603eda3ecbbce0bdd92\\\"}, {\\\"trigger_word\\\": \\\"maintain\\\", \\\"sent_id\\\": 14, \\\"offset\\\": [18, 19], \\\"id\\\": \\\"ab89582e0bd3a7fbc54426de86d02d34\\\"}, {\\\"trigger_word\\\": \\\"strong\\\", \\\"sent_id\\\": 14, \\\"offset\\\": [20, 21], \\\"id\\\": \\\"aa62c896a517796ccf62c09d5637a706\\\"}, {\\\"trigger_word\\\": \\\"presence\\\", \\\"sent_id\\\": 14, \\\"offset\\\": [21, 22], \\\"id\\\": \\\"1a78ce0b707f645216b2ba2c4c3d1dc6\\\"}, {\\\"trigger_word\\\": \\\"region\\\", \\\"sent_id\\\": 14, \\\"offset\\\": [24, 25], \\\"id\\\": \\\"ffe3a96b219b834750e94363fb366267\\\"}, {\\\"trigger_word\\\": \\\"Then\\\", \\\"sent_id\\\": 15, \\\"offset\\\": [0, 1], \\\"id\\\": \\\"814d6cfef76c9b33ead9d0d06f998270\\\"}, {\\\"trigger_word\\\": \\\"November\\\", \\\"sent_id\\\": 15, \\\"offset\\\": [2, 3], \\\"id\\\": \\\"e2157342a86eec2336c2fdc46df77585\\\"}, {\\\"trigger_word\\\": \\\"U.S.\\\", \\\"sent_id\\\": 15, \\\"offset\\\": [6, 7], \\\"id\\\": \\\"51c7ff065dabaaa45e4ed4201bdaa902\\\"}, {\\\"trigger_word\\\": \\\"Infantry\\\", \\\"sent_id\\\": 15, \\\"offset\\\": [8, 9], \\\"id\\\": \\\"f6f99f5d9caa0549cae7374a62b9150f\\\"}, {\\\"trigger_word\\\": \\\"Division\\\", \\\"sent_id\\\": 15, \\\"offset\\\": [9, 10], \\\"id\\\": \\\"e523533dd9dfe5527214a3eef402b10e\\\"}, {\\\"trigger_word\\\": \\\"returned\\\", \\\"sent_id\\\": 15, \\\"offset\\\": [10, 11], \\\"id\\\": \\\"2ec9b0f06378b4b657d531fbe51005d9\\\"}, {\\\"trigger_word\\\": \\\"Kuwait\\\", \\\"sent_id\\\": 15, \\\"offset\\\": [12, 13], \\\"id\\\": \\\"193c8347a6cd498fa08531e67f77b300\\\"}, {\\\"trigger_word\\\": \\\"using\\\", \\\"sent_id\\\": 16, \\\"offset\\\": [0, 1], \\\"id\\\": \\\"17daf05711fd7242c3d0712a6ffa7985\\\"}, {\\\"trigger_word\\\": \\\"unk\\\", \\\"sent_id\\\": 16, \\\"offset\\\": [2, 3], \\\"id\\\": \\\"921c98d3ff390860f3db8ccf4c714340\\\"}, {\\\"trigger_word\\\": \\\"already\\\", \\\"sent_id\\\": 16, \\\"offset\\\": [3, 4], \\\"id\\\": \\\"e075cc8ab05409b6d947ba1ce00502a0\\\"}, {\\\"trigger_word\\\": \\\"place\\\", \\\"sent_id\\\": 16, \\\"offset\\\": [5, 6], \\\"id\\\": \\\"02bd94e0b0e5f4d93a983f7af4699481\\\"}, {\\\"trigger_word\\\": \\\"advanced\\\", \\\"sent_id\\\": 16, \\\"offset\\\": [6, 7], \\\"id\\\": \\\"d6e2308afb56204b7341cff5ab03edcd\\\"}, {\\\"trigger_word\\\": \\\"elements\\\", \\\"sent_id\\\": 16, \\\"offset\\\": [7, 8], \\\"id\\\": \\\"7b4cb2dc4837895987cf99a349977381\\\"}, {\\\"trigger_word\\\": \\\"u.s.\\\", \\\"sent_id\\\": 16, \\\"offset\\\": [10, 11], \\\"id\\\": \\\"a3c41462b7b2f7392477a6454c7e9125\\\"}, {\\\"trigger_word\\\": \\\"infantry\\\", \\\"sent_id\\\": 16, \\\"offset\\\": [12, 13], \\\"id\\\": \\\"526d0fe180703e6cdc4142237c92814c\\\"}, {\\\"trigger_word\\\": \\\"division\\\", \\\"sent_id\\\": 16, \\\"offset\\\": [13, 14], \\\"id\\\": \\\"f07b954dac004814582faa40946e54be\\\"}, {\\\"trigger_word\\\": \\\"air\\\", \\\"sent_id\\\": 16, \\\"offset\\\": [16, 17], \\\"id\\\": \\\"7e5d2af909a1333867872e6c3dd0cfa9\\\"}, {\\\"trigger_word\\\": \\\"missile\\\", \\\"sent_id\\\": 16, \\\"offset\\\": [18, 19], \\\"id\\\": \\\"ccc889aa6d1e5fd250adeef6091e6602\\\"}, {\\\"trigger_word\\\": \\\"defense\\\", \\\"sent_id\\\": 16, \\\"offset\\\": [19, 20], \\\"id\\\": \\\"55be1a859ab50f70c5d070bfefb2ed41\\\"}, {\\\"trigger_word\\\": \\\"command\\\", \\\"sent_id\\\": 16, \\\"offset\\\": [20, 21], \\\"id\\\": \\\"fd8f0b473952eede5d7f65fdb1ce3aae\\\"}, {\\\"trigger_word\\\": \\\"theatre\\\", \\\"sent_id\\\": 16, \\\"offset\\\": [22, 23], \\\"id\\\": \\\"c753c1fcd34e4228e92281b6ab6e7beb\\\"}, {\\\"trigger_word\\\": \\\"support\\\", \\\"sent_id\\\": 16, \\\"offset\\\": [23, 24], \\\"id\\\": \\\"03ac67e4170dfad11019543f10c463ff\\\"}, {\\\"trigger_word\\\": \\\"command\\\", \\\"sent_id\\\": 16, \\\"offset\\\": [24, 25], \\\"id\\\": \\\"ee42e877182cc2db069e8dea8cb06ef1\\\"}, {\\\"trigger_word\\\": \\\"air\\\", \\\"sent_id\\\": 16, \\\"offset\\\": [27, 28], \\\"id\\\": \\\"311447dce207e2fd8c64d6cac3ebe160\\\"}, {\\\"trigger_word\\\": \\\"support\\\", \\\"sent_id\\\": 16, \\\"offset\\\": [28, 29], \\\"id\\\": \\\"8d2fa717a795060a598510b9e8df74d9\\\"}, {\\\"trigger_word\\\": \\\"operations\\\", \\\"sent_id\\\": 16, \\\"offset\\\": [29, 30], \\\"id\\\": \\\"c1020a755608dfec81e5a0ff374ca4be\\\"}, {\\\"trigger_word\\\": \\\"center\\\", \\\"sent_id\\\": 16, \\\"offset\\\": [30, 31], \\\"id\\\": \\\"adfa7b8abb44d468509f89d1fdcca61b\\\"}, {\\\"trigger_word\\\": \\\"deployed\\\", \\\"sent_id\\\": 16, \\\"offset\\\": [31, 32], \\\"id\\\": \\\"3bb5602f2c121be0530df1d4277bf0f9\\\"}, {\\\"trigger_word\\\": \\\"addition\\\", \\\"sent_id\\\": 17, \\\"offset\\\": [1, 2], \\\"id\\\": \\\"1a4615047ab3360b1f301a267f9db1da\\\"}, {\\\"trigger_word\\\": \\\"marine\\\", \\\"sent_id\\\": 17, \\\"offset\\\": [4, 5], \\\"id\\\": \\\"f8065eaa457847ad770e3ee52f26b423\\\"}, {\\\"trigger_word\\\": \\\"expeditionary\\\", \\\"sent_id\\\": 17, \\\"offset\\\": [5, 6], \\\"id\\\": \\\"ff6b3b55d9710201235af9484d4c8977\\\"}, {\\\"trigger_word\\\": \\\"force\\\", \\\"sent_id\\\": 17, \\\"offset\\\": [6, 7], \\\"id\\\": \\\"e40a61d9281182229803594f4c46f9c4\\\"}, {\\\"trigger_word\\\": \\\"joined\\\", \\\"sent_id\\\": 17, \\\"offset\\\": [7, 8], \\\"id\\\": \\\"c6533f7c9c9e025ec2943e02d48bd804\\\"}, {\\\"trigger_word\\\": \\\"marine\\\", \\\"sent_id\\\": 17, \\\"offset\\\": [10, 11], \\\"id\\\": \\\"f0de73fdfaecabb2bc70b582f4b95a16\\\"}, {\\\"trigger_word\\\": \\\"expeditionary\\\", \\\"sent_id\\\": 17, \\\"offset\\\": [11, 12], \\\"id\\\": \\\"0262baea27f8c3180c4bcebfc0086ae4\\\"}, {\\\"trigger_word\\\": \\\"force\\\", \\\"sent_id\\\": 17, \\\"offset\\\": [12, 13], \\\"id\\\": \\\"6c7e930f23b3a42e24b0baa859a4079f\\\"}, {\\\"trigger_word\\\": \\\"already\\\", \\\"sent_id\\\": 17, \\\"offset\\\": [13, 14], \\\"id\\\": \\\"a414f521d9f1940a5d7e6f95b7db7627\\\"}, {\\\"trigger_word\\\": \\\"place\\\", \\\"sent_id\\\": 17, \\\"offset\\\": [15, 16], \\\"id\\\": \\\"53713b84f01221937aed1de02173e9a5\\\"}, {\\\"trigger_word\\\": \\\"build-up\\\", \\\"sent_id\\\": 18, \\\"offset\\\": [2, 3], \\\"id\\\": \\\"f632f070292568d21bd5849f8ccf4b9b\\\"}, {\\\"trigger_word\\\": \\\"UN\\\", \\\"sent_id\\\": 18, \\\"offset\\\": [4, 5], \\\"id\\\": \\\"d045885cfbd6437b2183de944f585e0f\\\"}, {\\\"trigger_word\\\": \\\"Secretary-General\\\", \\\"sent_id\\\": 18, \\\"offset\\\": [5, 6], \\\"id\\\": \\\"03a4dc6939e4f0d70f0651097ded847a\\\"}, {\\\"trigger_word\\\": \\\"Kofi\\\", \\\"sent_id\\\": 18, \\\"offset\\\": [6, 7], \\\"id\\\": \\\"d1da2de2c7dcf08816c3e835df0230d6\\\"}, {\\\"trigger_word\\\": \\\"Annan\\\", \\\"sent_id\\\": 18, \\\"offset\\\": [7, 8], \\\"id\\\": \\\"9099e66417b3dbea3e8236d47a4fd2af\\\"}, {\\\"trigger_word\\\": \\\"flew\\\", \\\"sent_id\\\": 18, \\\"offset\\\": [8, 9], \\\"id\\\": \\\"7220508903ba7f94ffdb537b9505cfac\\\"}, {\\\"trigger_word\\\": \\\"Baghdad\\\", \\\"sent_id\\\": 18, \\\"offset\\\": [10, 11], \\\"id\\\": \\\"ce1cebd551cacf9a04f1fcd8e769b793\\\"}, {\\\"trigger_word\\\": \\\"meet\\\", \\\"sent_id\\\": 18, \\\"offset\\\": [12, 13], \\\"id\\\": \\\"e75f5935d321ffc1af6b34ebf29b9341\\\"}, {\\\"trigger_word\\\": \\\"Saddam\\\", \\\"sent_id\\\": 18, \\\"offset\\\": [14, 15], \\\"id\\\": \\\"7764eb68a382254e38d56453dc152eda\\\"}, {\\\"trigger_word\\\": \\\"Hussein\\\", \\\"sent_id\\\": 18, \\\"offset\\\": [15, 16], \\\"id\\\": \\\"fce62e3d0482236a27800174445821d4\\\"}, {\\\"trigger_word\\\": \\\"negotiated\\\", \\\"sent_id\\\": 18, \\\"offset\\\": [17, 18], \\\"id\\\": \\\"de861ba22321e0c4e87af6bc557653d6\\\"}, {\\\"trigger_word\\\": \\\"allow\\\", \\\"sent_id\\\": 18, \\\"offset\\\": [19, 20], \\\"id\\\": \\\"a44c194882e3556b4e99ee6afe50b8ee\\\"}, {\\\"trigger_word\\\": \\\"uninterrupted\\\", \\\"sent_id\\\": 18, \\\"offset\\\": [20, 21], \\\"id\\\": \\\"66a78d7c7e665ec698e63a4bbf3a4096\\\"}, {\\\"trigger_word\\\": \\\"inspections\\\", \\\"sent_id\\\": 18, \\\"offset\\\": [21, 22], \\\"id\\\": \\\"76e971505ca7dad40e74907d63db3f43\\\"}, {\\\"trigger_word\\\": \\\"November\\\", \\\"sent_id\\\": 19, \\\"offset\\\": [2, 3], \\\"id\\\": \\\"7822d23240f6cef22e3789fdde74a748\\\"}, {\\\"trigger_word\\\": \\\"non-compliance\\\", \\\"sent_id\\\": 19, \\\"offset\\\": [6, 7], \\\"id\\\": \\\"966e19879d0b73e094ed11352fae3913\\\"}, {\\\"trigger_word\\\": \\\"Iraq\\\", \\\"sent_id\\\": 19, \\\"offset\\\": [8, 9], \\\"id\\\": \\\"4b72df7ddcd1736c294cb05e96c32c8e\\\"}, {\\\"trigger_word\\\": \\\"resulted in\\\", \\\"sent_id\\\": 19, \\\"offset\\\": [9, 11], \\\"id\\\": \\\"6e8c3a3013cafceea5396fec4d701b64\\\"}, {\\\"trigger_word\\\": \\\"initiation\\\", \\\"sent_id\\\": 19, \\\"offset\\\": [12, 13], \\\"id\\\": \\\"4cb52102b7990031ef23ed7ba1bb7a64\\\"}, {\\\"trigger_word\\\": \\\"Operation\\\", \\\"sent_id\\\": 19, \\\"offset\\\": [14, 15], \\\"id\\\": \\\"56560f89a60d1b22e9d028f925fda47e\\\"}, {\\\"trigger_word\\\": \\\"Desert\\\", \\\"sent_id\\\": 19, \\\"offset\\\": [15, 16], \\\"id\\\": \\\"eff6c397d28022e78fa9f1cfea2e9c28\\\"}, {\\\"trigger_word\\\": \\\"Thunder\\\", \\\"sent_id\\\": 19, \\\"offset\\\": [16, 17], \\\"id\\\": \\\"3060d2a73e8b8df07b4e7dc13d2320c2\\\"}, {\\\"trigger_word\\\": \\\"CENTCOM\\\", \\\"sent_id\\\": 20, \\\"offset\\\": [0, 1], \\\"id\\\": \\\"f415f4eaead6308820f5c27366e463c5\\\"}, {\\\"trigger_word\\\": \\\"moved\\\", \\\"sent_id\\\": 20, \\\"offset\\\": [1, 2], \\\"id\\\": \\\"f6e12377ebb62c586a3b1d3e3ab8bdbb\\\"}, {\\\"trigger_word\\\": \\\"forces\\\", \\\"sent_id\\\": 20, \\\"offset\\\": [3, 4], \\\"id\\\": \\\"a0305d07ada21a8f752f0963bbfb352f\\\"}, {\\\"trigger_word\\\": \\\"position\\\", \\\"sent_id\\\": 20, \\\"offset\\\": [5, 6], \\\"id\\\": \\\"c2a3a6ab94e5724e086d201b13b70905\\\"}, {\\\"trigger_word\\\": \\\"initiate\\\", \\\"sent_id\\\": 20, \\\"offset\\\": [7, 8], \\\"id\\\": \\\"1d255567c93e67151f8bb9847e1f25b0\\\"}, {\\\"trigger_word\\\": \\\"strikes\\\", \\\"sent_id\\\": 20, \\\"offset\\\": [8, 9], \\\"id\\\": \\\"81d503d3022caaa04bc715407c60d19d\\\"}, {\\\"trigger_word\\\": \\\"Iraq\\\", \\\"sent_id\\\": 20, \\\"offset\\\": [10, 11], \\\"id\\\": \\\"10db085bb08765d5a2314541304e20d8\\\"}, {\\\"trigger_word\\\": \\\"additional\\\", \\\"sent_id\\\": 20, \\\"offset\\\": [13, 14], \\\"id\\\": \\\"4765371de27dcc86b92017c5e62cb802\\\"}, {\\\"trigger_word\\\": \\\"personnel\\\", \\\"sent_id\\\": 20, \\\"offset\\\": [14, 15], \\\"id\\\": \\\"634f3db01bbd650ca459267a96856e59\\\"}, {\\\"trigger_word\\\": \\\"deployed\\\", \\\"sent_id\\\": 20, \\\"offset\\\": [16, 17], \\\"id\\\": \\\"ef16e207699de1db88a98ca1f635fb91\\\"}, {\\\"trigger_word\\\": \\\"operation\\\", \\\"sent_id\\\": 20, \\\"offset\\\": [19, 20], \\\"id\\\": \\\"96b119f7e7fae26c041a1e05b97526de\\\"}, {\\\"trigger_word\\\": \\\"evening\\\", \\\"sent_id\\\": 21, \\\"offset\\\": [2, 3], \\\"id\\\": \\\"a56cf929aa9ba4c2aadd1aae14769f96\\\"}, {\\\"trigger_word\\\": \\\"November\\\", \\\"sent_id\\\": 21, \\\"offset\\\": [5, 6], \\\"id\\\": \\\"f09c2a6b2ff012a21341aba3b9b7b7ee\\\"}, {\\\"trigger_word\\\": \\\"USS\\\", \\\"sent_id\\\": 21, \\\"offset\\\": [7, 8], \\\"id\\\": \\\"ad044fc8b3732ce5f839df00a4fba319\\\"}, {\\\"trigger_word\\\": \\\"Dwight\\\", \\\"sent_id\\\": 21, \\\"offset\\\": [9, 10], \\\"id\\\": \\\"0a0009bc15a324b9442a9241d7b55411\\\"}, {\\\"trigger_word\\\": \\\"D.\\\", \\\"sent_id\\\": 21, \\\"offset\\\": [10, 11], \\\"id\\\": \\\"088884229dd2bb107d43968a658a6438\\\"}, {\\\"trigger_word\\\": \\\"Eisenhower\\\", \\\"sent_id\\\": 21, \\\"offset\\\": [11, 12], \\\"id\\\": \\\"94d3b2bfe891b14113c015d1ae8c7324\\\"}, {\\\"trigger_word\\\": \\\"CVN-69\\\", \\\"sent_id\\\": 21, \\\"offset\\\": [14, 15], \\\"id\\\": \\\"84b4a09b1694106d564b8d6581bc3cf5\\\"}, {\\\"trigger_word\\\": \\\"minutes\\\", \\\"sent_id\\\": 21, \\\"offset\\\": [18, 19], \\\"id\\\": \\\"f00490b8a5a75dbf0397b3fa18ef6358\\\"}, {\\\"trigger_word\\\": \\\"away\\\", \\\"sent_id\\\": 21, \\\"offset\\\": [19, 20], \\\"id\\\": \\\"ba94eb3491f8c6bfc49228f848bf46bf\\\"}, {\\\"trigger_word\\\": \\\"launching\\\", \\\"sent_id\\\": 21, \\\"offset\\\": [21, 22], \\\"id\\\": \\\"dc80d1419a6f5c61cf41cc3e9c3e2c91\\\"}, {\\\"trigger_word\\\": \\\"air\\\", \\\"sent_id\\\": 21, \\\"offset\\\": [22, 23], \\\"id\\\": \\\"02062b0207741b96c54bb18e3b1811b7\\\"}, {\\\"trigger_word\\\": \\\"strikes\\\", \\\"sent_id\\\": 21, \\\"offset\\\": [23, 24], \\\"id\\\": \\\"06dc70be211eeec5a7f8d6359628910d\\\"}, {\\\"trigger_word\\\": \\\"targets\\\", \\\"sent_id\\\": 21, \\\"offset\\\": [25, 26], \\\"id\\\": \\\"4e0f11e0a5379ec170b6b8b9ae7a5203\\\"}, {\\\"trigger_word\\\": \\\"Iraq\\\", \\\"sent_id\\\": 21, \\\"offset\\\": [27, 28], \\\"id\\\": \\\"16c9d1bc4c255feb71c40bbf08b4795c\\\"}, {\\\"trigger_word\\\": \\\"Saddam\\\", \\\"sent_id\\\": 21, \\\"offset\\\": [29, 30], \\\"id\\\": \\\"1a92aed29686d0be6e652d748ebf29ea\\\"}, {\\\"trigger_word\\\": \\\"Hussein\\\", \\\"sent_id\\\": 21, \\\"offset\\\": [30, 31], \\\"id\\\": \\\"293ba406560652b23a8f4f3b02ef53c2\\\"}, {\\\"trigger_word\\\": \\\"backed\\\", \\\"sent_id\\\": 21, \\\"offset\\\": [32, 33], \\\"id\\\": \\\"6b961e6022165383e89bb3a4e63739b1\\\"}, {\\\"trigger_word\\\": \\\"December\\\", \\\"sent_id\\\": 22, \\\"offset\\\": [1, 2], \\\"id\\\": \\\"9f21e4cfb1a7f976a81d965b8c8386d6\\\"}, {\\\"trigger_word\\\": \\\"Iraq\\\", \\\"sent_id\\\": 22, \\\"offset\\\": [4, 5], \\\"id\\\": \\\"3bae580da32a086e4ba2980cc07b4317\\\"}, {\\\"trigger_word\\\": \\\"refused\\\", \\\"sent_id\\\": 22, \\\"offset\\\": [6, 7], \\\"id\\\": \\\"e7d43ac4932e973113ae5e0c6a39b5af\\\"}, {\\\"trigger_word\\\": \\\"allow\\\", \\\"sent_id\\\": 22, \\\"offset\\\": [8, 9], \\\"id\\\": \\\"ed5c4249a4b3c15d1bff511a50e2843b\\\"}, {\\\"trigger_word\\\": \\\"inspections\\\", \\\"sent_id\\\": 22, \\\"offset\\\": [9, 10], \\\"id\\\": \\\"116497d32259ea400ccce1c3d4d75f99\\\"}, {\\\"trigger_word\\\": \\\"Operation\\\", \\\"sent_id\\\": 22, \\\"offset\\\": [11, 12], \\\"id\\\": \\\"1d15ec870b4ac40203475b25819e52b4\\\"}, {\\\"trigger_word\\\": \\\"Desert\\\", \\\"sent_id\\\": 22, \\\"offset\\\": [12, 13], \\\"id\\\": \\\"1c66e96431fbd829e1ecfa030625b419\\\"}, {\\\"trigger_word\\\": \\\"Fox\\\", \\\"sent_id\\\": 22, \\\"offset\\\": [13, 14], \\\"id\\\": \\\"d8fa63b64e49820f19494788e3badd52\\\"}, {\\\"trigger_word\\\": \\\"began\\\", \\\"sent_id\\\": 22, \\\"offset\\\": [14, 15], \\\"id\\\": \\\"c9c8c28ab33f3e64ea9ba438c759541b\\\"}, {\\\"trigger_word\\\": \\\"Several\\\", \\\"sent_id\\\": 23, \\\"offset\\\": [0, 1], \\\"id\\\": \\\"42abfbb4ff54075b49ac9b41820bff69\\\"}, {\\\"trigger_word\\\": \\\"key\\\", \\\"sent_id\\\": 23, \\\"offset\\\": [1, 2], \\\"id\\\": \\\"1c4eb4d1866e2bc812418e5297eeaf87\\\"}, {\\\"trigger_word\\\": \\\"Iraqi\\\", \\\"sent_id\\\": 23, \\\"offset\\\": [2, 3], \\\"id\\\": \\\"eac0669f29fbdde71318232e7963014d\\\"}, {\\\"trigger_word\\\": \\\"facilities\\\", \\\"sent_id\\\": 23, \\\"offset\\\": [3, 4], \\\"id\\\": \\\"be764cff8854095bc6f0d172a15b5121\\\"}, {\\\"trigger_word\\\": \\\"specialized\\\", \\\"sent_id\\\": 23, \\\"offset\\\": [5, 6], \\\"id\\\": \\\"c4ec9c0e52505f715db4a65e24d27ade\\\"}, {\\\"trigger_word\\\": \\\"equipment\\\", \\\"sent_id\\\": 23, \\\"offset\\\": [6, 7], \\\"id\\\": \\\"f30b9be00cf8693e5157bd03e2f11d27\\\"}, {\\\"trigger_word\\\": \\\"destroyed\\\", \\\"sent_id\\\": 23, \\\"offset\\\": [8, 9], \\\"id\\\": \\\"bbbdf8a5751860d5a226d6b89eb0c1fa\\\"}, {\\\"trigger_word\\\": \\\"several\\\", \\\"sent_id\\\": 23, \\\"offset\\\": [10, 11], \\\"id\\\": \\\"eed91f8b6ad0a66359ebd47e82ea1a6b\\\"}, {\\\"trigger_word\\\": \\\"days\\\", \\\"sent_id\\\": 23, \\\"offset\\\": [11, 12], \\\"id\\\": \\\"c52337c1a6c1efd267b11b5263b776d2\\\"}, {\\\"trigger_word\\\": \\\"air\\\", \\\"sent_id\\\": 23, \\\"offset\\\": [13, 14], \\\"id\\\": \\\"422710923e383b9bdb9f7c7dd9c8d30b\\\"}, {\\\"trigger_word\\\": \\\"strikes\\\", \\\"sent_id\\\": 23, \\\"offset\\\": [14, 15], \\\"id\\\": \\\"d5a2c749a86637b9fa4eb40724afe260\\\"}, {\\\"trigger_word\\\": \\\"including\\\", \\\"sent_id\\\": 23, \\\"offset\\\": [15, 16], \\\"id\\\": \\\"6569583f78526b0cc11babd86b043496\\\"}, {\\\"trigger_word\\\": \\\"flight\\\", \\\"sent_id\\\": 23, \\\"offset\\\": [18, 19], \\\"id\\\": \\\"267505b67557839539be27572038caa5\\\"}, {\\\"trigger_word\\\": \\\"deck\\\", \\\"sent_id\\\": 23, \\\"offset\\\": [19, 20], \\\"id\\\": \\\"0f9087338c1c9d4a52d115e571a0ac8a\\\"}, {\\\"trigger_word\\\": \\\"USS\\\", \\\"sent_id\\\": 23, \\\"offset\\\": [21, 22], \\\"id\\\": \\\"afaa823e14b89dcd50f0fd6c1256035f\\\"}, {\\\"trigger_word\\\": \\\"Enterprise\\\", \\\"sent_id\\\": 23, \\\"offset\\\": [23, 24], \\\"id\\\": \\\"9258c8eaacf28b2e9a3a29848de60a75\\\"}, {\\\"trigger_word\\\": \\\"CVN-65\\\", \\\"sent_id\\\": 23, \\\"offset\\\": [26, 27], \\\"id\\\": \\\"9d5e62ae51b2e51e8109aa1a1cc0e8cf\\\"}, {\\\"trigger_word\\\": \\\"back\\\", \\\"sent_id\\\": 24, \\\"offset\\\": [2, 3], \\\"id\\\": \\\"13f696f979370ddfb9e9da55e2616dcb\\\"}, {\\\"trigger_word\\\": \\\"Iraqi\\\", \\\"sent_id\\\": 24, \\\"offset\\\": [4, 5], \\\"id\\\": \\\"e1ef8382fccb8cf440e344a8e8340ae2\\\"}, {\\\"trigger_word\\\": \\\"ballistic\\\", \\\"sent_id\\\": 24, \\\"offset\\\": [5, 6], \\\"id\\\": \\\"f1957f37175bc6d7d6ba3a8e542949f5\\\"}, {\\\"trigger_word\\\": \\\"missile\\\", \\\"sent_id\\\": 24, \\\"offset\\\": [6, 7], \\\"id\\\": \\\"d418d5858dd872039fec37bc6e0cf66f\\\"}, {\\\"trigger_word\\\": \\\"program\\\", \\\"sent_id\\\": 24, \\\"offset\\\": [7, 8], \\\"id\\\": \\\"1355056bed538d5c6fc3f69258ba1a5f\\\"}, {\\\"trigger_word\\\": \\\"several\\\", \\\"sent_id\\\": 24, \\\"offset\\\": [9, 10], \\\"id\\\": \\\"a804e36a000c4fe38df8de10c7613635\\\"}, {\\\"trigger_word\\\": \\\"years\\\", \\\"sent_id\\\": 24, \\\"offset\\\": [10, 11], \\\"id\\\": \\\"56a1815670461c76be09ad0e713a4eb2\\\"}]}\\n/root/schema-dag-extraction/data/maven/test.jsonl:551:{\\\"title\\\": \\\"Fanaticon\\\", \\\"id\\\": \\\"bac4cc29a8a185067e20f28bf372ff1f\\\", \\\"content\\\": [{\\\"sentence\\\": \\\"Fanaticon is an annual multi-genre, science-fiction, fantasy, comic book, anime, and gaming convention held in the southeastern area of Alabama.\\\", \\\"tokens\\\": [\\\"Fanaticon\\\", \\\"is\\\", \\\"an\\\", \\\"annual\\\", \\\"multi-genre\\\", \\\",\\\", \\\"science-fiction\\\", \\\",\\\", \\\"fantasy\\\", \\\",\\\", \\\"comic\\\", \\\"book\\\", \\\",\\\", \\\"anime\\\", \\\",\\\", \\\"and\\\", \\\"gaming\\\", \\\"convention\\\", \\\"held\\\", \\\"in\\\", \\\"the\\\", \\\"southeastern\\\", \\\"area\\\", \\\"of\\\", \\\"Alabama\\\", \\\".\\\"]}, {\\\"sentence\\\": \\\"Its inaugural event was held on November 16, 2013, in Dothan, Alabama.\\\", \\\"tokens\\\": [\\\"Its\\\", \\\"inaugural\\\", \\\"event\\\", \\\"was\\\", \\\"held\\\", \\\"on\\\", \\\"November\\\", \\\"16\\\", \\\",\\\", \\\"2013\\\", \\\",\\\", \\\"in\\\", \\\"Dothan\\\", \\\",\\\", \\\"Alabama\\\", \\\".\\\"]}, {\\\"sentence\\\": \\\"Phillip Chalker, the event's organizer, is the owner of Fanatix Card and Game Shop and says that the idea came from a joke, but then took it a step further and held a Kickstarter campaign that generated the necessary revenue in about two hours.\\\", \\\"tokens\\\": [\\\"Phillip\\\", \\\"Chalker\\\", \\\",\\\", \\\"the\\\", \\\"event\\\", \\\"'s\\\", \\\"organizer\\\", \\\",\\\", \\\"is\\\", \\\"the\\\", \\\"owner\\\", \\\"of\\\", \\\"Fanatix\\\", \\\"Card\\\", \\\"and\\\", \\\"Game\\\", \\\"Shop\\\", \\\"and\\\", \\\"says\\\", \\\"that\\\", \\\"the\\\", \\\"idea\\\", \\\"came\\\", \\\"from\\\", \\\"a\\\", \\\"joke\\\", \\\",\\\", \\\"but\\\", \\\"then\\\", \\\"took\\\", \\\"it\\\", \\\"a\\\", \\\"step\\\", \\\"further\\\", \\\"and\\\", \\\"held\\\", \\\"a\\\", \\\"Kickstarter\\\", \\\"campaign\\\", \\\"that\\\", \\\"generated\\\", \\\"the\\\", \\\"necessary\\\", \\\"revenue\\\", \\\"in\\\", \\\"about\\\", \\\"two\\\", \\\"hours\\\", \\\".\\\"]}, {\\\"sentence\\\": \\\"The first convention hosted a Pro Tour Qualifier in which the winner received $1,000 in cash and prizes and a ticket to the next round of competition held in Spain.\\\", \\\"tokens\\\": [\\\"The\\\", \\\"first\\\", \\\"convention\\\", \\\"hosted\\\", \\\"a\\\", \\\"Pro\\\", \\\"Tour\\\", \\\"Qualifier\\\", \\\"in\\\", \\\"which\\\", \\\"the\\\", \\\"winner\\\", \\\"received\\\", \\\"$\\\", \\\"1,000\\\", \\\"in\\\", \\\"cash\\\", \\\"and\\\", \\\"prizes\\\", \\\"and\\\", \\\"a\\\", \\\"ticket\\\", \\\"to\\\", \\\"the\\\", \\\"next\\\", \\\"round\\\", \\\"of\\\", \\\"competition\\\", \\\"held\\\", \\\"in\\\", \\\"Spain\\\", \\\".\\\"]}, {\\\"sentence\\\": \\\"Fanaticon also hosts a costume contest of 100 average number of competitors.\\\", \\\"tokens\\\": [\\\"Fanaticon\\\", \\\"also\\\", \\\"hosts\\\", \\\"a\\\", \\\"costume\\\", \\\"contest\\\", \\\"of\\\", \\\"100\\\", \\\"average\\\", \\\"number\\\", \\\"of\\\", \\\"competitors\\\", \\\".\\\"]}, {\\\"sentence\\\": \\\"Fanaticon is committed to bringing a great family experience to the Wiregrass.\\\", \\\"tokens\\\": [\\\"Fanaticon\\\", \\\"is\\\", \\\"committed\\\", \\\"to\\\", \\\"bringing\\\", \\\"a\\\", \\\"great\\\", \\\"family\\\", \\\"experience\\\", \\\"to\\\", \\\"the\\\", \\\"Wiregrass\\\", \\\".\\\"]}], \\\"candidates\\\": [{\\\"trigger_word\\\": \\\"Fanaticon\\\", \\\"sent_id\\\": 0, \\\"offset\\\": [0, 1], \\\"id\\\": \\\"054982e97e7b44cb31dd8d1167dfb03e\\\"}, {\\\"trigger_word\\\": \\\"annual\\\", \\\"sent_id\\\": 0, \\\"offset\\\": [3, 4], \\\"id\\\": \\\"51fe5b83c7ea4eed7cb02920f574947b\\\"}, {\\\"trigger_word\\\": \\\"multi-genre\\\", \\\"sent_id\\\": 0, \\\"offset\\\": [4, 5], \\\"id\\\": \\\"e76d73ecdeac976b4708e13b35f23c6e\\\"}, {\\\"trigger_word\\\": \\\"science-fiction\\\", \\\"sent_id\\\": 0, \\\"offset\\\": [6, 7], \\\"id\\\": \\\"11d0d3e29764c96b6bdb8fba6a689b32\\\"}, {\\\"trigger_word\\\": \\\"fantasy\\\", \\\"sent_id\\\": 0, \\\"offset\\\": [8, 9], \\\"id\\\": \\\"147e18eba88ad90c3eb7c24edd0e1a7e\\\"}, {\\\"trigger_word\\\": \\\"comic\\\", \\\"sent_id\\\": 0, \\\"offset\\\": [10, 11], \\\"id\\\": \\\"c5227e395fef6567632427198bd9848d\\\"}, {\\\"trigger_word\\\": \\\"book\\\", \\\"sent_id\\\": 0, \\\"offset\\\": [11, 12], \\\"id\\\": \\\"395195776dd3ff7ca903bd0b33951aed\\\"}, {\\\"trigger_word\\\": \\\"anime\\\", \\\"sent_id\\\": 0, \\\"offset\\\": [13, 14], \\\"id\\\": \\\"e1aebab615b640b970e7a867fd85826e\\\"}, {\\\"trigger_word\\\": \\\"gaming\\\", \\\"sent_id\\\": 0, \\\"offset\\\": [16, 17], \\\"id\\\": \\\"603e9b51149395a401f80230c5177045\\\"}, {\\\"trigger_word\\\": \\\"convention\\\", \\\"sent_id\\\": 0, \\\"offset\\\": [17, 18], \\\"id\\\": \\\"42db0af7eff5dd278a74b354554c66a8\\\"}, {\\\"trigger_word\\\": \\\"held\\\", \\\"sent_id\\\": 0, \\\"offset\\\": [18, 19], \\\"id\\\": \\\"ec1c46213be20c341ccf2006409436e1\\\"}, {\\\"trigger_word\\\": \\\"southeastern\\\", \\\"sent_id\\\": 0, \\\"offset\\\": [21, 22], \\\"id\\\": \\\"3d5f19da2cee8fefe0c27f9d628150ae\\\"}, {\\\"trigger_word\\\": \\\"area\\\", \\\"sent_id\\\": 0, \\\"offset\\\": [22, 23], \\\"id\\\": \\\"c810e48ba50928ee376f8074153148b2\\\"}, {\\\"trigger_word\\\": \\\"Alabama\\\", \\\"sent_id\\\": 0, \\\"offset\\\": [24, 25], \\\"id\\\": \\\"7de409cfcbdb92fdbaddb02401012fca\\\"}, {\\\"trigger_word\\\": \\\"inaugural\\\", \\\"sent_id\\\": 1, \\\"offset\\\": [1, 2], \\\"id\\\": \\\"d60aee8a27879e2f2ed6ab7f891417ba\\\"}, {\\\"trigger_word\\\": \\\"event\\\", \\\"sent_id\\\": 1, \\\"offset\\\": [2, 3], \\\"id\\\": \\\"44adabfb5f822a0e83c99b0edcb9a160\\\"}, {\\\"trigger_word\\\": \\\"held\\\", \\\"sent_id\\\": 1, \\\"offset\\\": [4, 5], \\\"id\\\": \\\"9f244f8b99902382ab311feb91c5c5b9\\\"}, {\\\"trigger_word\\\": \\\"November\\\", \\\"sent_id\\\": 1, \\\"offset\\\": [6, 7], \\\"id\\\": \\\"a8b9e527458a6485cbc3e95e0ea01196\\\"}, {\\\"trigger_word\\\": \\\"Dothan\\\", \\\"sent_id\\\": 1, \\\"offset\\\": [12, 13], \\\"id\\\": \\\"1206213788e99602b9adf4d349ec8e3e\\\"}, {\\\"trigger_word\\\": \\\"Alabama\\\", \\\"sent_id\\\": 1, \\\"offset\\\": [14, 15], \\\"id\\\": \\\"dd6f98d5d69e9d3d534d3b4d652326d1\\\"}, {\\\"trigger_word\\\": \\\"Phillip\\\", \\\"sent_id\\\": 2, \\\"offset\\\": [0, 1], \\\"id\\\": \\\"7f4b7e01f538c33b2aad0f6b0ce1dfd6\\\"}, {\\\"trigger_word\\\": \\\"Chalker\\\", \\\"sent_id\\\": 2, \\\"offset\\\": [1, 2], \\\"id\\\": \\\"c4e330ab0aaef2acb15cee501ba55107\\\"}, {\\\"trigger_word\\\": \\\"event\\\", \\\"sent_id\\\": 2, \\\"offset\\\": [4, 5], \\\"id\\\": \\\"679a7f2b800371740081fc3809d35d77\\\"}, {\\\"trigger_word\\\": \\\"organizer\\\", \\\"sent_id\\\": 2, \\\"offset\\\": [6, 7], \\\"id\\\": \\\"3a2213c0f055448d185c6c6320ff0cc6\\\"}, {\\\"trigger_word\\\": \\\"owner\\\", \\\"sent_id\\\": 2, \\\"offset\\\": [10, 11], \\\"id\\\": \\\"a204d02f2e20f022b46345c78811dd50\\\"}, {\\\"trigger_word\\\": \\\"Fanatix\\\", \\\"sent_id\\\": 2, \\\"offset\\\": [12, 13], \\\"id\\\": \\\"d6e2caef09292581eb869775b646fb19\\\"}, {\\\"trigger_word\\\": \\\"Card\\\", \\\"sent_id\\\": 2, \\\"offset\\\": [13, 14], \\\"id\\\": \\\"f5d9e7f5350bd602cba1b97f56d5a661\\\"}, {\\\"trigger_word\\\": \\\"Game\\\", \\\"sent_id\\\": 2, \\\"offset\\\": [15, 16], \\\"id\\\": \\\"3d02be2207c65ba8f636c25ad491074d\\\"}, {\\\"trigger_word\\\": \\\"Shop\\\", \\\"sent_id\\\": 2, \\\"offset\\\": [16, 17], \\\"id\\\": \\\"ad5c7a602038987c9f3c7b1617af85ea\\\"}, {\\\"trigger_word\\\": \\\"says\\\", \\\"sent_id\\\": 2, \\\"offset\\\": [18, 19], \\\"id\\\": \\\"bf6c43aecb0087a69338b1ae88bcf7ba\\\"}, {\\\"trigger_word\\\": \\\"idea\\\", \\\"sent_id\\\": 2, \\\"offset\\\": [21, 22], \\\"id\\\": \\\"f55adb524339c46e8d4eb9dbf990b3fd\\\"}, {\\\"trigger_word\\\": \\\"came from\\\", \\\"sent_id\\\": 2, \\\"offset\\\": [22, 24], \\\"id\\\": \\\"63d911655fa2fd9b3c438dcd503886d9\\\"}, {\\\"trigger_word\\\": \\\"joke\\\", \\\"sent_id\\\": 2, \\\"offset\\\": [25, 26], \\\"id\\\": \\\"b2f5ac7444116d2b0fb35f8e73118386\\\"}, {\\\"trigger_word\\\": \\\"took\\\", \\\"sent_id\\\": 2, \\\"offset\\\": [29, 30], \\\"id\\\": \\\"4bc4b2febec5dfc98451bd5f40767bb6\\\"}, {\\\"trigger_word\\\": \\\"step\\\", \\\"sent_id\\\": 2, \\\"offset\\\": [32, 33], \\\"id\\\": \\\"21640e4fee7f3a6b3b6ed70780074678\\\"}, {\\\"trigger_word\\\": \\\"held\\\", \\\"sent_id\\\": 2, \\\"offset\\\": [35, 36], \\\"id\\\": \\\"ad9e98b480e2c245d410c60d8085c1f3\\\"}, {\\\"trigger_word\\\": \\\"Kickstarter\\\", \\\"sent_id\\\": 2, \\\"offset\\\": [37, 38], \\\"id\\\": \\\"9071c0d119784d534c0284ab6c6b820c\\\"}, {\\\"trigger_word\\\": \\\"campaign\\\", \\\"sent_id\\\": 2, \\\"offset\\\": [38, 39], \\\"id\\\": \\\"56dee977a3c529c0409b9c7055accc15\\\"}, {\\\"trigger_word\\\": \\\"generated\\\", \\\"sent_id\\\": 2, \\\"offset\\\": [40, 41], \\\"id\\\": \\\"fce29972250713056e0581959b57fa15\\\"}, {\\\"trigger_word\\\": \\\"necessary\\\", \\\"sent_id\\\": 2, \\\"offset\\\": [42, 43], \\\"id\\\": \\\"6bab7449c9e3d3609720ab2433d91cca\\\"}, {\\\"trigger_word\\\": \\\"revenue\\\", \\\"sent_id\\\": 2, \\\"offset\\\": [43, 44], \\\"id\\\": \\\"2ff94e7cb983fe8545a6ff6c7472847f\\\"}, {\\\"trigger_word\\\": \\\"hours\\\", \\\"sent_id\\\": 2, \\\"offset\\\": [47, 48], \\\"id\\\": \\\"11b427f3a8511678d22305d77b593466\\\"}, {\\\"trigger_word\\\": \\\"first\\\", \\\"sent_id\\\": 3, \\\"offset\\\": [1, 2], \\\"id\\\": \\\"125ff1d440cf2c187cbda0911dc18725\\\"}, {\\\"trigger_word\\\": \\\"convention\\\", \\\"sent_id\\\": 3, \\\"offset\\\": [2, 3], \\\"id\\\": \\\"14177ad74716d91264e13ab9a50594f0\\\"}, {\\\"trigger_word\\\": \\\"hosted\\\", \\\"sent_id\\\": 3, \\\"offset\\\": [3, 4], \\\"id\\\": \\\"347e55d8a482bffa266bebd30a863bdb\\\"}, {\\\"trigger_word\\\": \\\"Pro\\\", \\\"sent_id\\\": 3, \\\"offset\\\": [5, 6], \\\"id\\\": \\\"49bbe94da760b5146ec922fb7bfc075a\\\"}, {\\\"trigger_word\\\": \\\"Tour\\\", \\\"sent_id\\\": 3, \\\"offset\\\": [6, 7], \\\"id\\\": \\\"d9b34e894d67c5fb98d319ba0a1de83c\\\"}, {\\\"trigger_word\\\": \\\"Qualifier\\\", \\\"sent_id\\\": 3, \\\"offset\\\": [7, 8], \\\"id\\\": \\\"46ecfce97a269d8d9fbec85dfcb927d6\\\"}, {\\\"trigger_word\\\": \\\"winner\\\", \\\"sent_id\\\": 3, \\\"offset\\\": [11, 12], \\\"id\\\": \\\"028678d85542e89ca9c9a9a57d8694a7\\\"}, {\\\"trigger_word\\\": \\\"received\\\", \\\"sent_id\\\": 3, \\\"offset\\\": [12, 13], \\\"id\\\": \\\"e0057b7ae00888ea4e109cf987a909a6\\\"}, {\\\"trigger_word\\\": \\\"cash\\\", \\\"sent_id\\\": 3, \\\"offset\\\": [16, 17], \\\"id\\\": \\\"366f8dc4393b194e4c6a2d793b3040e6\\\"}, {\\\"trigger_word\\\": \\\"prizes\\\", \\\"sent_id\\\": 3, \\\"offset\\\": [18, 19], \\\"id\\\": \\\"9101322144f351955600946de289918c\\\"}, {\\\"trigger_word\\\": \\\"ticket\\\", \\\"sent_id\\\": 3, \\\"offset\\\": [21, 22], \\\"id\\\": \\\"59d71e48877043d28fdf14d472f97f26\\\"}, {\\\"trigger_word\\\": \\\"next\\\", \\\"sent_id\\\": 3, \\\"offset\\\": [24, 25], \\\"id\\\": \\\"ac79626bf41f1fa47f27eefcdbe2c84d\\\"}, {\\\"trigger_word\\\": \\\"round\\\", \\\"sent_id\\\": 3, \\\"offset\\\": [25, 26], \\\"id\\\": \\\"371788f704b74ee909fe1e51dfcc338b\\\"}, {\\\"trigger_word\\\": \\\"competition\\\", \\\"sent_id\\\": 3, \\\"offset\\\": [27, 28], \\\"id\\\": \\\"c0610e387d4944d9f35a52d3672b0f79\\\"}, {\\\"trigger_word\\\": \\\"held\\\", \\\"sent_id\\\": 3, \\\"offset\\\": [28, 29], \\\"id\\\": \\\"e572d02d691a08d972c945f975e587b4\\\"}, {\\\"trigger_word\\\": \\\"Spain\\\", \\\"sent_id\\\": 3, \\\"offset\\\": [30, 31], \\\"id\\\": \\\"03b4008c5083e7a98a5fa3adb17e2cdc\\\"}, {\\\"trigger_word\\\": \\\"Fanaticon\\\", \\\"sent_id\\\": 4, \\\"offset\\\": [0, 1], \\\"id\\\": \\\"a46115a4528ebfc3fda7ba46f43f4b0a\\\"}, {\\\"trigger_word\\\": \\\"also\\\", \\\"sent_id\\\": 4, \\\"offset\\\": [1, 2], \\\"id\\\": \\\"7702fc0a3bf9e6f3ba34c265f9e2b9da\\\"}, {\\\"trigger_word\\\": \\\"hosts\\\", \\\"sent_id\\\": 4, \\\"offset\\\": [2, 3], \\\"id\\\": \\\"70273a3ba3c4ff932c54a384361a6b8b\\\"}, {\\\"trigger_word\\\": \\\"costume\\\", \\\"sent_id\\\": 4, \\\"offset\\\": [4, 5], \\\"id\\\": \\\"5c5ddbdef1c4323143255b5c7b63758c\\\"}, {\\\"trigger_word\\\": \\\"contest\\\", \\\"sent_id\\\": 4, \\\"offset\\\": [5, 6], \\\"id\\\": \\\"54d9a8826210b68efe440c0c9703ae3e\\\"}, {\\\"trigger_word\\\": \\\"average\\\", \\\"sent_id\\\": 4, \\\"offset\\\": [8, 9], \\\"id\\\": \\\"a14aafc86910c55ba0bcb7ad2a135a99\\\"}, {\\\"trigger_word\\\": \\\"number\\\", \\\"sent_id\\\": 4, \\\"offset\\\": [9, 10], \\\"id\\\": \\\"146e63b03ecc850b99163069436537e7\\\"}, {\\\"trigger_word\\\": \\\"competitors\\\", \\\"sent_id\\\": 4, \\\"offset\\\": [11, 12], \\\"id\\\": \\\"85ca7f3cb8a2e0d04147d9dacddd7b43\\\"}, {\\\"trigger_word\\\": \\\"Fanaticon\\\", \\\"sent_id\\\": 5, \\\"offset\\\": [0, 1], \\\"id\\\": \\\"43a5ab177643d558c808421829912438\\\"}, {\\\"trigger_word\\\": \\\"committed\\\", \\\"sent_id\\\": 5, \\\"offset\\\": [2, 3], \\\"id\\\": \\\"2ea2ffc8f3d59330931b16beb541889d\\\"}, {\\\"trigger_word\\\": \\\"bringing\\\", \\\"sent_id\\\": 5, \\\"offset\\\": [4, 5], \\\"id\\\": \\\"0163f90ea0d1a42c8d1823fe75ac479e\\\"}, {\\\"trigger_word\\\": \\\"great\\\", \\\"sent_id\\\": 5, \\\"offset\\\": [6, 7], \\\"id\\\": \\\"a56d37f25b18f14a821ba0b864675239\\\"}, {\\\"trigger_word\\\": \\\"family\\\", \\\"sent_id\\\": 5, \\\"offset\\\": [7, 8], \\\"id\\\": \\\"1ebcdf2ad9edcffe247b4bc1328d4539\\\"}, {\\\"trigger_word\\\": \\\"experience\\\", \\\"sent_id\\\": 5, \\\"offset\\\": [8, 9], \\\"id\\\": \\\"63eb015d3f5652450ad802787103ba60\\\"}, {\\\"trigger_word\\\": \\\"Wiregrass\\\", \\\"sent_id\\\": 5, \\\"offset\\\": [11, 12], \\\"id\\\": \\\"a585c6952260fd26b177ebadea0d7444\\\"}]}\\n/root/schema-dag-extraction/data/maven/test.jsonl:674:{\\\"title\\\": \\\"Iraqi revolt against the British\\\", \\\"id\\\": \\\"6abfbef8787b861e35dd98e9ad4d5fc1\\\", \\\"content\\\": [{\\\"sentence\\\": \\\"The Iraqi revolt against the British, also known as the 1920 Iraqi Revolt or Great Iraqi Revolution, started in Baghdad in the summer of 1920 with mass demonstrations by Iraqis, including protests by embittered officers from the old Ottoman army, against the British occupation of Iraq.\\\", \\\"tokens\\\": [\\\"the\\\", \\\"iraqi\\\", \\\"revolt\\\", \\\"against\\\", \\\"the\\\", \\\"british\\\", \\\",\\\", \\\"also\\\", \\\"known\\\", \\\"as\\\", \\\"the\\\", \\\"1920\\\", \\\"iraqi\\\", \\\"revolt\\\", \\\"or\\\", \\\"great\\\", \\\"iraqi\\\", \\\"revolution\\\", \\\",\\\", \\\"started\\\", \\\"in\\\", \\\"baghdad\\\", \\\"in\\\", \\\"the\\\", \\\"summer\\\", \\\"of\\\", \\\"1920\\\", \\\"with\\\", \\\"mass\\\", \\\"demonstrations\\\", \\\"by\\\", \\\"iraqis\\\", \\\",\\\", \\\"including\\\", \\\"protests\\\", \\\"by\\\", \\\"embittered\\\", \\\"officers\\\", \\\"from\\\", \\\"the\\\", \\\"old\\\", \\\"ottoman\\\", \\\"army\\\", \\\",\\\", \\\"against\\\", \\\"the\\\", \\\"british\\\", \\\"occupation\\\", \\\"of\\\", \\\"iraq\\\", \\\".\\\"]}, {\\\"sentence\\\": \\\"The revolt gained momentum when it spread to the largely tribal Shia regions of the middle and lower Euphrates.\\\", \\\"tokens\\\": [\\\"The\\\", \\\"revolt\\\", \\\"gained\\\", \\\"momentum\\\", \\\"when\\\", \\\"it\\\", \\\"spread\\\", \\\"to\\\", \\\"the\\\", \\\"largely\\\", \\\"tribal\\\", \\\"Shia\\\", \\\"regions\\\", \\\"of\\\", \\\"the\\\", \\\"middle\\\", \\\"and\\\", \\\"lower\\\", \\\"Euphrates\\\", \\\".\\\"]}, {\\\"sentence\\\": \\\"Sheikh Mehdi Al-Khalissi was a prominent Shia leader of the revolt.\\\", \\\"tokens\\\": [\\\"Sheikh\\\", \\\"Mehdi\\\", \\\"Al-Khalissi\\\", \\\"was\\\", \\\"a\\\", \\\"prominent\\\", \\\"Shia\\\", \\\"leader\\\", \\\"of\\\", \\\"the\\\", \\\"revolt\\\", \\\".\\\"]}, {\\\"sentence\\\": \\\"Sunni and Shia religious communities cooperated during the revolution as well as tribal communities, the urban masses, and many Iraqi officers in Syria.\\\", \\\"tokens\\\": [\\\"Sunni\\\", \\\"and\\\", \\\"Shia\\\", \\\"religious\\\", \\\"communities\\\", \\\"cooperated\\\", \\\"during\\\", \\\"the\\\", \\\"revolution\\\", \\\"as\\\", \\\"well\\\", \\\"as\\\", \\\"tribal\\\", \\\"communities\\\", \\\",\\\", \\\"the\\\", \\\"urban\\\", \\\"masses\\\", \\\",\\\", \\\"and\\\", \\\"many\\\", \\\"Iraqi\\\", \\\"officers\\\", \\\"in\\\", \\\"Syria\\\", \\\".\\\"]}, {\\\"sentence\\\": \\\"The objectives of the revolution were independence from British rule and creation of an Arab government.\\\", \\\"tokens\\\": [\\\"The\\\", \\\"objectives\\\", \\\"of\\\", \\\"the\\\", \\\"revolution\\\", \\\"were\\\", \\\"independence\\\", \\\"from\\\", \\\"British\\\", \\\"rule\\\", \\\"and\\\", \\\"creation\\\", \\\"of\\\", \\\"an\\\", \\\"Arab\\\", \\\"government\\\", \\\".\\\"]}, {\\\"sentence\\\": \\\"Though the revolt achieved some initial success, by the end of October 1920, the British had crushed the revolt.\\\", \\\"tokens\\\": [\\\"though\\\", \\\"the\\\", \\\"revolt\\\", \\\"achieved\\\", \\\"some\\\", \\\"initial\\\", \\\"success\\\", \\\",\\\", \\\"by\\\", \\\"the\\\", \\\"end\\\", \\\"of\\\", \\\"october\\\", \\\"1920\\\", \\\",\\\", \\\"the\\\", \\\"british\\\", \\\"had\\\", \\\"crushed\\\", \\\"the\\\", \\\"revolt\\\", \\\".\\\"]}, {\\\"sentence\\\": \\\"Although the revolt was largely over by the end of 1920, elements of it dragged on until 1922.\\\", \\\"tokens\\\": [\\\"although\\\", \\\"the\\\", \\\"revolt\\\", \\\"was\\\", \\\"largely\\\", \\\"over\\\", \\\"by\\\", \\\"the\\\", \\\"end\\\", \\\"of\\\", \\\"1920\\\", \\\",\\\", \\\"elements\\\", \\\"of\\\", \\\"it\\\", \\\"dragged\\\", \\\"on\\\", \\\"until\\\", \\\"1922\\\", \\\".\\\"]}, {\\\"sentence\\\": \\\"During the 1920 revolt, another anti-British rebellion took place in the north Iraq by the Kurds, who were trying to gain independence.\\\", \\\"tokens\\\": [\\\"During\\\", \\\"the\\\", \\\"1920\\\", \\\"revolt\\\", \\\",\\\", \\\"another\\\", \\\"anti-British\\\", \\\"rebellion\\\", \\\"took\\\", \\\"place\\\", \\\"in\\\", \\\"the\\\", \\\"north\\\", \\\"Iraq\\\", \\\"by\\\", \\\"the\\\", \\\"Kurds\\\", \\\",\\\", \\\"who\\\", \\\"were\\\", \\\"trying\\\", \\\"to\\\", \\\"gain\\\", \\\"independence\\\", \\\".\\\"]}, {\\\"sentence\\\": \\\"One of the major Kurdish leaders of the Kurdish revolt was Sheikh Mahmoud Barzanji.\\\", \\\"tokens\\\": [\\\"One\\\", \\\"of\\\", \\\"the\\\", \\\"major\\\", \\\"Kurdish\\\", \\\"leaders\\\", \\\"of\\\", \\\"the\\\", \\\"Kurdish\\\", \\\"revolt\\\", \\\"was\\\", \\\"Sheikh\\\", \\\"Mahmoud\\\", \\\"Barzanji\\\", \\\".\\\"]}], \\\"candidates\\\": [{\\\"trigger_word\\\": \\\"iraqi\\\", \\\"sent_id\\\": 0, \\\"offset\\\": [1, 2], \\\"id\\\": \\\"71e250b81fc2021e0f2ede6fa559406d\\\"}, {\\\"trigger_word\\\": \\\"revolt\\\", \\\"sent_id\\\": 0, \\\"offset\\\": [2, 3], \\\"id\\\": \\\"1853419096e16ca5cb43b5c96f1f1067\\\"}, {\\\"trigger_word\\\": \\\"british\\\", \\\"sent_id\\\": 0, \\\"offset\\\": [5, 6], \\\"id\\\": \\\"a2699c8ade616c4880713aadd6288f36\\\"}, {\\\"trigger_word\\\": \\\"also known as\\\", \\\"sent_id\\\": 0, \\\"offset\\\": [7, 10], \\\"id\\\": \\\"408bd6e6eb4149485d93a4da9f27a75d\\\"}, {\\\"trigger_word\\\": \\\"iraqi\\\", \\\"sent_id\\\": 0, \\\"offset\\\": [12, 13], \\\"id\\\": \\\"87f31b24f0db81ee28859e68caf026da\\\"}, {\\\"trigger_word\\\": \\\"revolt\\\", \\\"sent_id\\\": 0, \\\"offset\\\": [13, 14], \\\"id\\\": \\\"92d459c399b284dfc2cf6adb9888f8f3\\\"}, {\\\"trigger_word\\\": \\\"great\\\", \\\"sent_id\\\": 0, \\\"offset\\\": [15, 16], \\\"id\\\": \\\"43aadb7baeb99182e92b9565801310c8\\\"}, {\\\"trigger_word\\\": \\\"iraqi\\\", \\\"sent_id\\\": 0, \\\"offset\\\": [16, 17], \\\"id\\\": \\\"3501f5fded73defe7f518c01db559a31\\\"}, {\\\"trigger_word\\\": \\\"revolution\\\", \\\"sent_id\\\": 0, \\\"offset\\\": [17, 18], \\\"id\\\": \\\"2b9b6f79703f03defeaeaaaa6d8c77f8\\\"}, {\\\"trigger_word\\\": \\\"started\\\", \\\"sent_id\\\": 0, \\\"offset\\\": [19, 20], \\\"id\\\": \\\"71d18128738454679cd613d953ec89d5\\\"}, {\\\"trigger_word\\\": \\\"baghdad\\\", \\\"sent_id\\\": 0, \\\"offset\\\": [21, 22], \\\"id\\\": \\\"4914b97de956264e78511b7c510f5cfd\\\"}, {\\\"trigger_word\\\": \\\"summer\\\", \\\"sent_id\\\": 0, \\\"offset\\\": [24, 25], \\\"id\\\": \\\"c97894d0f615ea79d14ad0e07f379b1e\\\"}, {\\\"trigger_word\\\": \\\"mass\\\", \\\"sent_id\\\": 0, \\\"offset\\\": [28, 29], \\\"id\\\": \\\"9f6681ed860adceee1ce0bc1b9d14032\\\"}, {\\\"trigger_word\\\": \\\"demonstrations\\\", \\\"sent_id\\\": 0, \\\"offset\\\": [29, 30], \\\"id\\\": \\\"52a64af0dad9130e354a4b0071dc5dad\\\"}, {\\\"trigger_word\\\": \\\"iraqis\\\", \\\"sent_id\\\": 0, \\\"offset\\\": [31, 32], \\\"id\\\": \\\"7b15416feffbb0f828b516a5d4df771a\\\"}, {\\\"trigger_word\\\": \\\"including\\\", \\\"sent_id\\\": 0, \\\"offset\\\": [33, 34], \\\"id\\\": \\\"e0a1bcdb8f858064599712c921024b68\\\"}, {\\\"trigger_word\\\": \\\"protests\\\", \\\"sent_id\\\": 0, \\\"offset\\\": [34, 35], \\\"id\\\": \\\"29d27c161dbd1650e9a527127a943b4a\\\"}, {\\\"trigger_word\\\": \\\"embittered\\\", \\\"sent_id\\\": 0, \\\"offset\\\": [36, 37], \\\"id\\\": \\\"173d34225aa228a0a1aba416ed830d6c\\\"}, {\\\"trigger_word\\\": \\\"officers\\\", \\\"sent_id\\\": 0, \\\"offset\\\": [37, 38], \\\"id\\\": \\\"7b4a09e5481c952c86465503a35482c5\\\"}, {\\\"trigger_word\\\": \\\"old\\\", \\\"sent_id\\\": 0, \\\"offset\\\": [40, 41], \\\"id\\\": \\\"38f047cf08ace975d90bf9f4bcf93ad5\\\"}, {\\\"trigger_word\\\": \\\"ottoman\\\", \\\"sent_id\\\": 0, \\\"offset\\\": [41, 42], \\\"id\\\": \\\"5a33db8ea3d03fd96df24846cd37cd6b\\\"}, {\\\"trigger_word\\\": \\\"army\\\", \\\"sent_id\\\": 0, \\\"offset\\\": [42, 43], \\\"id\\\": \\\"2fbc4e396bdf0715f6da773a708341d3\\\"}, {\\\"trigger_word\\\": \\\"british\\\", \\\"sent_id\\\": 0, \\\"offset\\\": [46, 47], \\\"id\\\": \\\"1ed2e209c679705b0bc68998d65c9b39\\\"}, {\\\"trigger_word\\\": \\\"occupation\\\", \\\"sent_id\\\": 0, \\\"offset\\\": [47, 48], \\\"id\\\": \\\"10d8227ab24daaeb465d248348d698dc\\\"}, {\\\"trigger_word\\\": \\\"iraq\\\", \\\"sent_id\\\": 0, \\\"offset\\\": [49, 50], \\\"id\\\": \\\"c61d44437ac741e595e62cfcd22c18cf\\\"}, {\\\"trigger_word\\\": \\\"revolt\\\", \\\"sent_id\\\": 1, \\\"offset\\\": [1, 2], \\\"id\\\": \\\"868f4d7dd1e75e55572a208710cd7e89\\\"}, {\\\"trigger_word\\\": \\\"gained\\\", \\\"sent_id\\\": 1, \\\"offset\\\": [2, 3], \\\"id\\\": \\\"6ed683978d3208aadc2832b949fe8208\\\"}, {\\\"trigger_word\\\": \\\"momentum\\\", \\\"sent_id\\\": 1, \\\"offset\\\": [3, 4], \\\"id\\\": \\\"0852caa80b0d0db64cc49848f979b7be\\\"}, {\\\"trigger_word\\\": \\\"spread\\\", \\\"sent_id\\\": 1, \\\"offset\\\": [6, 7], \\\"id\\\": \\\"fdd2d9b9c9010e71da367a6b773a3868\\\"}, {\\\"trigger_word\\\": \\\"largely\\\", \\\"sent_id\\\": 1, \\\"offset\\\": [9, 10], \\\"id\\\": \\\"e33a8ac717fed5d4698e8ff8560ac4ae\\\"}, {\\\"trigger_word\\\": \\\"tribal\\\", \\\"sent_id\\\": 1, \\\"offset\\\": [10, 11], \\\"id\\\": \\\"1fdec2000be9d9405a45a3452f95cd3d\\\"}, {\\\"trigger_word\\\": \\\"Shia\\\", \\\"sent_id\\\": 1, \\\"offset\\\": [11, 12], \\\"id\\\": \\\"87393622952e2e2ab4d31d5b81d2e355\\\"}, {\\\"trigger_word\\\": \\\"regions\\\", \\\"sent_id\\\": 1, \\\"offset\\\": [12, 13], \\\"id\\\": \\\"ff1274f408c104a67d8383efd2d68289\\\"}, {\\\"trigger_word\\\": \\\"middle\\\", \\\"sent_id\\\": 1, \\\"offset\\\": [15, 16], \\\"id\\\": \\\"7bcf034f3ec185751bea9c7c15177993\\\"}, {\\\"trigger_word\\\": \\\"lower\\\", \\\"sent_id\\\": 1, \\\"offset\\\": [17, 18], \\\"id\\\": \\\"13382e944ce59e16f0b953ba90e8872c\\\"}, {\\\"trigger_word\\\": \\\"Euphrates\\\", \\\"sent_id\\\": 1, \\\"offset\\\": [18, 19], \\\"id\\\": \\\"9edc442452316a1027a08ed2bffe7d4e\\\"}, {\\\"trigger_word\\\": \\\"Sheikh\\\", \\\"sent_id\\\": 2, \\\"offset\\\": [0, 1], \\\"id\\\": \\\"d6a8156592e1a166e047a90d4c5747df\\\"}, {\\\"trigger_word\\\": \\\"Mehdi\\\", \\\"sent_id\\\": 2, \\\"offset\\\": [1, 2], \\\"id\\\": \\\"58f500cc8a4290278bb0e0889e0e14f0\\\"}, {\\\"trigger_word\\\": \\\"Al-Khalissi\\\", \\\"sent_id\\\": 2, \\\"offset\\\": [2, 3], \\\"id\\\": \\\"d53cc9245d3e2147ad47457a83f62ff3\\\"}, {\\\"trigger_word\\\": \\\"prominent\\\", \\\"sent_id\\\": 2, \\\"offset\\\": [5, 6], \\\"id\\\": \\\"0cc55fd3afbe811d856678e8f64d365b\\\"}, {\\\"trigger_word\\\": \\\"Shia\\\", \\\"sent_id\\\": 2, \\\"offset\\\": [6, 7], \\\"id\\\": \\\"ac590b8b2de1bea1e223c77a84e6123d\\\"}, {\\\"trigger_word\\\": \\\"leader\\\", \\\"sent_id\\\": 2, \\\"offset\\\": [7, 8], \\\"id\\\": \\\"0c6c9b3f6824ac424a7889db47217573\\\"}, {\\\"trigger_word\\\": \\\"revolt\\\", \\\"sent_id\\\": 2, \\\"offset\\\": [10, 11], \\\"id\\\": \\\"aaecd2a690b3de7c9fbf7509e3ae96bd\\\"}, {\\\"trigger_word\\\": \\\"Sunni\\\", \\\"sent_id\\\": 3, \\\"offset\\\": [0, 1], \\\"id\\\": \\\"044083103e1542bddb03ed77f9d0b43e\\\"}, {\\\"trigger_word\\\": \\\"Shia\\\", \\\"sent_id\\\": 3, \\\"offset\\\": [2, 3], \\\"id\\\": \\\"2fa65564ee52591d50de5115d468c971\\\"}, {\\\"trigger_word\\\": \\\"religious\\\", \\\"sent_id\\\": 3, \\\"offset\\\": [3, 4], \\\"id\\\": \\\"f8684dd0e7eec7d3034093885365f200\\\"}, {\\\"trigger_word\\\": \\\"communities\\\", \\\"sent_id\\\": 3, \\\"offset\\\": [4, 5], \\\"id\\\": \\\"1adec2b4be4ea22e0c3cb3d57f7b140b\\\"}, {\\\"trigger_word\\\": \\\"cooperated\\\", \\\"sent_id\\\": 3, \\\"offset\\\": [5, 6], \\\"id\\\": \\\"37b5a18e24db03f5e7a594e5378ff99f\\\"}, {\\\"trigger_word\\\": \\\"revolution\\\", \\\"sent_id\\\": 3, \\\"offset\\\": [8, 9], \\\"id\\\": \\\"13dc9b31f3334521556ca7abd52304f7\\\"}, {\\\"trigger_word\\\": \\\"well\\\", \\\"sent_id\\\": 3, \\\"offset\\\": [10, 11], \\\"id\\\": \\\"e614f74aee9b4f761e6e8a8826229681\\\"}, {\\\"trigger_word\\\": \\\"tribal\\\", \\\"sent_id\\\": 3, \\\"offset\\\": [12, 13], \\\"id\\\": \\\"8133d0e78f7c66854f4deac34dee7f37\\\"}, {\\\"trigger_word\\\": \\\"communities\\\", \\\"sent_id\\\": 3, \\\"offset\\\": [13, 14], \\\"id\\\": \\\"6f8735ffa650f1927392c90e2132038a\\\"}, {\\\"trigger_word\\\": \\\"urban\\\", \\\"sent_id\\\": 3, \\\"offset\\\": [16, 17], \\\"id\\\": \\\"dfaaed3af99fd5bed612c4dd750a9c77\\\"}, {\\\"trigger_word\\\": \\\"masses\\\", \\\"sent_id\\\": 3, \\\"offset\\\": [17, 18], \\\"id\\\": \\\"5490d2868cc755efd8f544ff8f548036\\\"}, {\\\"trigger_word\\\": \\\"many\\\", \\\"sent_id\\\": 3, \\\"offset\\\": [20, 21], \\\"id\\\": \\\"40e124d3b12169fee55513ee5139adbb\\\"}, {\\\"trigger_word\\\": \\\"Iraqi\\\", \\\"sent_id\\\": 3, \\\"offset\\\": [21, 22], \\\"id\\\": \\\"ebe1fa5bf44ab3d5020d40c7565f7e17\\\"}, {\\\"trigger_word\\\": \\\"officers\\\", \\\"sent_id\\\": 3, \\\"offset\\\": [22, 23], \\\"id\\\": \\\"855da28bc81b611b462a147b2519e867\\\"}, {\\\"trigger_word\\\": \\\"Syria\\\", \\\"sent_id\\\": 3, \\\"offset\\\": [24, 25], \\\"id\\\": \\\"9dab67f3a4cb6505a791f9bceaae6bc7\\\"}, {\\\"trigger_word\\\": \\\"objectives\\\", \\\"sent_id\\\": 4, \\\"offset\\\": [1, 2], \\\"id\\\": \\\"259bd6406ee6b4d21bd6f991c3efef97\\\"}, {\\\"trigger_word\\\": \\\"revolution\\\", \\\"sent_id\\\": 4, \\\"offset\\\": [4, 5], \\\"id\\\": \\\"9969b7fe2844a05737f3fecd1aadfbc6\\\"}, {\\\"trigger_word\\\": \\\"independence\\\", \\\"sent_id\\\": 4, \\\"offset\\\": [6, 7], \\\"id\\\": \\\"0c7039ff15d6ecf14ca079d4530dbe3d\\\"}, {\\\"trigger_word\\\": \\\"British\\\", \\\"sent_id\\\": 4, \\\"offset\\\": [8, 9], \\\"id\\\": \\\"dea13c8c76cd7d7ac627cfce7def1723\\\"}, {\\\"trigger_word\\\": \\\"rule\\\", \\\"sent_id\\\": 4, \\\"offset\\\": [9, 10], \\\"id\\\": \\\"b1c474782f0c1488da7490f303e0d411\\\"}, {\\\"trigger_word\\\": \\\"creation\\\", \\\"sent_id\\\": 4, \\\"offset\\\": [11, 12], \\\"id\\\": \\\"e7f8cf21a975365b44c47b68895794db\\\"}, {\\\"trigger_word\\\": \\\"Arab\\\", \\\"sent_id\\\": 4, \\\"offset\\\": [14, 15], \\\"id\\\": \\\"9b365f78295cf8b3e748fe0525e7fecb\\\"}, {\\\"trigger_word\\\": \\\"government\\\", \\\"sent_id\\\": 4, \\\"offset\\\": [15, 16], \\\"id\\\": \\\"3ccb4c0102533e8b2ed384dbab2e3d16\\\"}, {\\\"trigger_word\\\": \\\"revolt\\\", \\\"sent_id\\\": 5, \\\"offset\\\": [2, 3], \\\"id\\\": \\\"598d44347826b3697ba546b8e1e1554c\\\"}, {\\\"trigger_word\\\": \\\"achieved\\\", \\\"sent_id\\\": 5, \\\"offset\\\": [3, 4], \\\"id\\\": \\\"eff814b718b9af1fd318f52a28ab98b2\\\"}, {\\\"trigger_word\\\": \\\"initial\\\", \\\"sent_id\\\": 5, \\\"offset\\\": [5, 6], \\\"id\\\": \\\"3db518c9de0390bea5a1af8ec924fcd9\\\"}, {\\\"trigger_word\\\": \\\"success\\\", \\\"sent_id\\\": 5, \\\"offset\\\": [6, 7], \\\"id\\\": \\\"5b0b5f006a7fd80539fa50197cd8d551\\\"}, {\\\"trigger_word\\\": \\\"end\\\", \\\"sent_id\\\": 5, \\\"offset\\\": [10, 11], \\\"id\\\": \\\"562c0c9e9f467a0d0e6e3ba69d38c06f\\\"}, {\\\"trigger_word\\\": \\\"october\\\", \\\"sent_id\\\": 5, \\\"offset\\\": [12, 13], \\\"id\\\": \\\"f28134a33526852eee454b94bb782dd4\\\"}, {\\\"trigger_word\\\": \\\"british\\\", \\\"sent_id\\\": 5, \\\"offset\\\": [16, 17], \\\"id\\\": \\\"f6d457853ec536a9ce876482af8e3e24\\\"}, {\\\"trigger_word\\\": \\\"crushed\\\", \\\"sent_id\\\": 5, \\\"offset\\\": [18, 19], \\\"id\\\": \\\"70fca5880a55dc848ad3f7847bb98129\\\"}, {\\\"trigger_word\\\": \\\"revolt\\\", \\\"sent_id\\\": 5, \\\"offset\\\": [20, 21], \\\"id\\\": \\\"5bafa7dfab7b272a390ec8004d37e7fe\\\"}, {\\\"trigger_word\\\": \\\"revolt\\\", \\\"sent_id\\\": 6, \\\"offset\\\": [2, 3], \\\"id\\\": \\\"9d58d9e8783438fe4b6764bdc1e7d365\\\"}, {\\\"trigger_word\\\": \\\"largely\\\", \\\"sent_id\\\": 6, \\\"offset\\\": [4, 5], \\\"id\\\": \\\"03e9d24ee721329cc82c8ee5ef194109\\\"}, {\\\"trigger_word\\\": \\\"end\\\", \\\"sent_id\\\": 6, \\\"offset\\\": [8, 9], \\\"id\\\": \\\"6c721dc577862ac8403dbde266dded8f\\\"}, {\\\"trigger_word\\\": \\\"elements\\\", \\\"sent_id\\\": 6, \\\"offset\\\": [12, 13], \\\"id\\\": \\\"36dcad6839ccc7b5097574133f4c2367\\\"}, {\\\"trigger_word\\\": \\\"dragged on\\\", \\\"sent_id\\\": 6, \\\"offset\\\": [15, 17], \\\"id\\\": \\\"8be53faf6a7835a6fdda20e57bf48fda\\\"}, {\\\"trigger_word\\\": \\\"revolt\\\", \\\"sent_id\\\": 7, \\\"offset\\\": [3, 4], \\\"id\\\": \\\"8282f65032c0fbd818eaddb7414114d7\\\"}, {\\\"trigger_word\\\": \\\"anti-British\\\", \\\"sent_id\\\": 7, \\\"offset\\\": [6, 7], \\\"id\\\": \\\"7b31ec3f338cd23ce5932c6deeb30a92\\\"}, {\\\"trigger_word\\\": \\\"rebellion\\\", \\\"sent_id\\\": 7, \\\"offset\\\": [7, 8], \\\"id\\\": \\\"ec88175eea8c84f7b8c35a59389465a2\\\"}, {\\\"trigger_word\\\": \\\"took place\\\", \\\"sent_id\\\": 7, \\\"offset\\\": [8, 10], \\\"id\\\": \\\"f6b19859700eae71a98c3f6cde80fa18\\\"}, {\\\"trigger_word\\\": \\\"north\\\", \\\"sent_id\\\": 7, \\\"offset\\\": [12, 13], \\\"id\\\": \\\"2d68a1fca5f6a658a940f08059ebe957\\\"}, {\\\"trigger_word\\\": \\\"Iraq\\\", \\\"sent_id\\\": 7, \\\"offset\\\": [13, 14], \\\"id\\\": \\\"dbb156ff4b0d2371f4322dc0ca39d020\\\"}, {\\\"trigger_word\\\": \\\"Kurds\\\", \\\"sent_id\\\": 7, \\\"offset\\\": [16, 17], \\\"id\\\": \\\"f3783137f95a01dc2f30a8bbb21a39a1\\\"}, {\\\"trigger_word\\\": \\\"trying\\\", \\\"sent_id\\\": 7, \\\"offset\\\": [20, 21], \\\"id\\\": \\\"372afda88393607c8a59a9c0b6a91349\\\"}, {\\\"trigger_word\\\": \\\"gain\\\", \\\"sent_id\\\": 7, \\\"offset\\\": [22, 23], \\\"id\\\": \\\"cb9fb4d2c241402f588177a05c2b8efe\\\"}, {\\\"trigger_word\\\": \\\"independence\\\", \\\"sent_id\\\": 7, \\\"offset\\\": [23, 24], \\\"id\\\": \\\"7b332863d600e8151ebaadcc1569919d\\\"}, {\\\"trigger_word\\\": \\\"major\\\", \\\"sent_id\\\": 8, \\\"offset\\\": [3, 4], \\\"id\\\": \\\"639196093213cdeb190d7bc0cfdb0088\\\"}, {\\\"trigger_word\\\": \\\"Kurdish\\\", \\\"sent_id\\\": 8, \\\"offset\\\": [4, 5], \\\"id\\\": \\\"d9c1b6f254fc4be7f07b1a9427cc2876\\\"}, {\\\"trigger_word\\\": \\\"leaders\\\", \\\"sent_id\\\": 8, \\\"offset\\\": [5, 6], \\\"id\\\": \\\"611c087f544b7cab5b1586e25426cd2d\\\"}, {\\\"trigger_word\\\": \\\"Kurdish\\\", \\\"sent_id\\\": 8, \\\"offset\\\": [8, 9], \\\"id\\\": \\\"7d3198f266defd184bc5d354478314ab\\\"}, {\\\"trigger_word\\\": \\\"revolt\\\", \\\"sent_id\\\": 8, \\\"offset\\\": [9, 10], \\\"id\\\": \\\"de8068a8d973db0645633e8bd07336d4\\\"}, {\\\"trigger_word\\\": \\\"Sheikh\\\", \\\"sent_id\\\": 8, \\\"offset\\\": [11, 12], \\\"id\\\": \\\"c485a2b7bd07e83abf80648475702def\\\"}, {\\\"trigger_word\\\": \\\"Mahmoud\\\", \\\"sent_id\\\": 8, \\\"offset\\\": [12, 13], \\\"id\\\": \\\"f2235a966efb40a6ca77121983732f65\\\"}, {\\\"trigger_word\\\": \\\"Barzanji\\\", \\\"sent_id\\\": 8, \\\"offset\\\": [13, 14], \\\"id\\\": \\\"9719050598dbbef539802e55a2df2707\\\"}]}\\n/root/schema-dag-extraction/data/maven/test.jsonl:676:{\\\"title\\\": \\\"Reformasi (Malaysia)\\\", \\\"id\\\": \\\"21058ede1dfb67fc38928ebcab75cbbd\\\", \\\"content\\\": [{\\\"sentence\\\": \\\"The Reformasi was a protest movement that began in September 1998 throughout Malaysia initiated by Anwar Ibrahim after his sacking as Deputy Prime Minister by the country's then-Prime Minister, Mahathir Mohamad in the same month.\\\", \\\"tokens\\\": [\\\"The\\\", \\\"Reformasi\\\", \\\"was\\\", \\\"a\\\", \\\"protest\\\", \\\"movement\\\", \\\"that\\\", \\\"began\\\", \\\"in\\\", \\\"September\\\", \\\"1998\\\", \\\"throughout\\\", \\\"Malaysia\\\", \\\"initiated\\\", \\\"by\\\", \\\"Anwar\\\", \\\"Ibrahim\\\", \\\"after\\\", \\\"his\\\", \\\"sacking\\\", \\\"as\\\", \\\"Deputy\\\", \\\"Prime\\\", \\\"Minister\\\", \\\"by\\\", \\\"the\\\", \\\"country\\\", \\\"'s\\\", \\\"then-Prime\\\", \\\"Minister\\\", \\\",\\\", \\\"Mahathir\\\", \\\"Mohamad\\\", \\\"in\\\", \\\"the\\\", \\\"same\\\", \\\"month\\\", \\\".\\\"]}, {\\\"sentence\\\": \\\"The massive movement, which occurred while the country hosted the Commonwealth Games, consisted of civil disobedience, demonstrations, sit-ins, rioting, occupations and online activism, involving thousands across Malaysia protesting against the Barisan Nasional (BN) government under the Mahathir Cabinet.\\\", \\\"tokens\\\": [\\\"The\\\", \\\"massive\\\", \\\"movement\\\", \\\",\\\", \\\"which\\\", \\\"occurred\\\", \\\"while\\\", \\\"the\\\", \\\"country\\\", \\\"hosted\\\", \\\"the\\\", \\\"Commonwealth\\\", \\\"Games\\\", \\\",\\\", \\\"consisted\\\", \\\"of\\\", \\\"civil\\\", \\\"disobedience\\\", \\\",\\\", \\\"demonstrations\\\", \\\",\\\", \\\"sit-ins\\\", \\\",\\\", \\\"rioting\\\", \\\",\\\", \\\"occupations\\\", \\\"and\\\", \\\"online\\\", \\\"activism\\\", \\\",\\\", \\\"involving\\\", \\\"thousands\\\", \\\"across\\\", \\\"Malaysia\\\", \\\"protesting\\\", \\\"against\\\", \\\"the\\\", \\\"Barisan\\\", \\\"Nasional\\\", \\\"(\\\", \\\"BN\\\", \\\")\\\", \\\"government\\\", \\\"under\\\", \\\"the\\\", \\\"Mahathir\\\", \\\"Cabinet\\\", \\\".\\\"]}, {\\\"sentence\\\": \\\"The movement started off as a political campaign calling for the resignation of Mahathir, Malaysia's longest-serving Prime Minister and the end of corruption and cronyism allegedly associated with the government of the day.\\\", \\\"tokens\\\": [\\\"The\\\", \\\"movement\\\", \\\"started\\\", \\\"off\\\", \\\"as\\\", \\\"a\\\", \\\"political\\\", \\\"campaign\\\", \\\"calling\\\", \\\"for\\\", \\\"the\\\", \\\"resignation\\\", \\\"of\\\", \\\"Mahathir\\\", \\\",\\\", \\\"Malaysia\\\", \\\"'s\\\", \\\"longest-serving\\\", \\\"Prime\\\", \\\"Minister\\\", \\\"and\\\", \\\"the\\\", \\\"end\\\", \\\"of\\\", \\\"corruption\\\", \\\"and\\\", \\\"cronyism\\\", \\\"allegedly\\\", \\\"associated\\\", \\\"with\\\", \\\"the\\\", \\\"government\\\", \\\"of\\\", \\\"the\\\", \\\"day\\\", \\\".\\\"]}, {\\\"sentence\\\": \\\"Building on the momentum of the Reformasi, a political movement called the Social Justice Movement () (ADIL) was formed and led by Wan Azizah Wan Ismail, Anwar's wife in 1998.\\\", \\\"tokens\\\": [\\\"Building\\\", \\\"on\\\", \\\"the\\\", \\\"momentum\\\", \\\"of\\\", \\\"the\\\", \\\"Reformasi\\\", \\\",\\\", \\\"a\\\", \\\"political\\\", \\\"movement\\\", \\\"called\\\", \\\"the\\\", \\\"Social\\\", \\\"Justice\\\", \\\"Movement\\\", \\\"(\\\", \\\")\\\", \\\"(\\\", \\\"ADIL\\\", \\\")\\\", \\\"was\\\", \\\"formed\\\", \\\"and\\\", \\\"led\\\", \\\"by\\\", \\\"Wan\\\", \\\"Azizah\\\", \\\"Wan\\\", \\\"Ismail\\\", \\\",\\\", \\\"Anwar\\\", \\\"'s\\\", \\\"wife\\\", \\\"in\\\", \\\"1998\\\", \\\".\\\"]}, {\\\"sentence\\\": \\\"However, after facing difficulties in registering Adil as a political party, the reformasi movement took over a small dormant party \\\\\\\"Ikatan Masyarakat Islam Malaysia\\\\\\\" (IKATAN) and led to the formation of a new multiracial-based party named \\\\\\\"Parti Keadilan Nasional\\\\\\\" or National Justice Party (KEADILAN) in 1999.\\\", \\\"tokens\\\": [\\\"however\\\", \\\",\\\", \\\"after\\\", \\\"facing\\\", \\\"difficulties\\\", \\\"in\\\", \\\"registering\\\", \\\"adil\\\", \\\"as\\\", \\\"a\\\", \\\"political\\\", \\\"party\\\", \\\",\\\", \\\"the\\\", \\\"reformasi\\\", \\\"movement\\\", \\\"took\\\", \\\"over\\\", \\\"a\\\", \\\"small\\\", \\\"dormant\\\", \\\"party\\\", \\\"``\\\", \\\"unk\\\", \\\"masyarakat\\\", \\\"islam\\\", \\\"malaysia\\\", \\\"''\\\", \\\"(\\\", \\\"unk\\\", \\\")\\\", \\\"and\\\", \\\"led\\\", \\\"to\\\", \\\"the\\\", \\\"formation\\\", \\\"of\\\", \\\"a\\\", \\\"new\\\", \\\"unk\\\", \\\"party\\\", \\\"named\\\", \\\"``\\\", \\\"parti\\\", \\\"keadilan\\\", \\\"nasional\\\", \\\"''\\\", \\\"or\\\", \\\"national\\\", \\\"justice\\\", \\\"party\\\", \\\"(\\\", \\\"keadilan\\\", \\\")\\\", \\\"in\\\", \\\"1999\\\", \\\".\\\"]}, {\\\"sentence\\\": \\\"On 3 August 2003, the newly merged entity of KEADILAN and \\\\\\\"Parti Rakyat Malaysia\\\\\\\" (PRM) was officially launched and assumed its current name, \\\\\\\"Parti Keadilan Rakyat (PKR).\\\", \\\"tokens\\\": [\\\"On\\\", \\\"3\\\", \\\"August\\\", \\\"2003\\\", \\\",\\\", \\\"the\\\", \\\"newly\\\", \\\"merged\\\", \\\"entity\\\", \\\"of\\\", \\\"KEADILAN\\\", \\\"and\\\", \\\"``\\\", \\\"Parti\\\", \\\"Rakyat\\\", \\\"Malaysia\\\", \\\"''\\\", \\\"(\\\", \\\"PRM\\\", \\\")\\\", \\\"was\\\", \\\"officially\\\", \\\"launched\\\", \\\"and\\\", \\\"assumed\\\", \\\"its\\\", \\\"current\\\", \\\"name\\\", \\\",\\\", \\\"``\\\", \\\"Parti\\\", \\\"Keadilan\\\", \\\"Rakyat\\\", \\\"(\\\", \\\"PKR\\\", \\\")\\\", \\\".\\\"]}, {\\\"sentence\\\": \\\"The Reformasi movement is still considered to be ongoing even after the 2018 Malaysian general election which saw Barisan Nasional (BN) lose its parliamentary majority to the Pakatan Harapan (PH) coalition and for the first time since Malaysia's independence become the official opposition.\\\", \\\"tokens\\\": [\\\"The\\\", \\\"Reformasi\\\", \\\"movement\\\", \\\"is\\\", \\\"still\\\", \\\"considered\\\", \\\"to\\\", \\\"be\\\", \\\"ongoing\\\", \\\"even\\\", \\\"after\\\", \\\"the\\\", \\\"2018\\\", \\\"Malaysian\\\", \\\"general\\\", \\\"election\\\", \\\"which\\\", \\\"saw\\\", \\\"Barisan\\\", \\\"Nasional\\\", \\\"(\\\", \\\"BN\\\", \\\")\\\", \\\"lose\\\", \\\"its\\\", \\\"parliamentary\\\", \\\"majority\\\", \\\"to\\\", \\\"the\\\", \\\"Pakatan\\\", \\\"Harapan\\\", \\\"(\\\", \\\"PH\\\", \\\")\\\", \\\"coalition\\\", \\\"and\\\", \\\"for\\\", \\\"the\\\", \\\"first\\\", \\\"time\\\", \\\"since\\\", \\\"Malaysia\\\", \\\"'s\\\", \\\"independence\\\", \\\"become\\\", \\\"the\\\", \\\"official\\\", \\\"opposition\\\", \\\".\\\"]}], \\\"candidates\\\": [{\\\"trigger_word\\\": \\\"Reformasi\\\", \\\"sent_id\\\": 0, \\\"offset\\\": [1, 2], \\\"id\\\": \\\"f435c44849b672c26dee5863452c1c76\\\"}, {\\\"trigger_word\\\": \\\"protest\\\", \\\"sent_id\\\": 0, \\\"offset\\\": [4, 5], \\\"id\\\": \\\"06605cbd4d540ffdf80bbf2c3ba2f6be\\\"}, {\\\"trigger_word\\\": \\\"movement\\\", \\\"sent_id\\\": 0, \\\"offset\\\": [5, 6], \\\"id\\\": \\\"fe4f8a715612fa627777e795175bb3e3\\\"}, {\\\"trigger_word\\\": \\\"began\\\", \\\"sent_id\\\": 0, \\\"offset\\\": [7, 8], \\\"id\\\": \\\"8fd311a219a848106f99cb25cfebd2f9\\\"}, {\\\"trigger_word\\\": \\\"September\\\", \\\"sent_id\\\": 0, \\\"offset\\\": [9, 10], \\\"id\\\": \\\"ff25ac1b531f245986f0102ffa249836\\\"}, {\\\"trigger_word\\\": \\\"Malaysia\\\", \\\"sent_id\\\": 0, \\\"offset\\\": [12, 13], \\\"id\\\": \\\"d156b5a0eded704e627b747f3a536a53\\\"}, {\\\"trigger_word\\\": \\\"initiated\\\", \\\"sent_id\\\": 0, \\\"offset\\\": [13, 14], \\\"id\\\": \\\"19f4a8984704f96384385c30e78a5db4\\\"}, {\\\"trigger_word\\\": \\\"Anwar\\\", \\\"sent_id\\\": 0, \\\"offset\\\": [15, 16], \\\"id\\\": \\\"087e6d8987e5ccfa0bd09948629ab9ef\\\"}, {\\\"trigger_word\\\": \\\"Ibrahim\\\", \\\"sent_id\\\": 0, \\\"offset\\\": [16, 17], \\\"id\\\": \\\"b4ddc34d6b16107742f26d7326b98cf0\\\"}, {\\\"trigger_word\\\": \\\"sacking\\\", \\\"sent_id\\\": 0, \\\"offset\\\": [19, 20], \\\"id\\\": \\\"e9619e8cf0d1cd5fdc90bba2a0737e13\\\"}, {\\\"trigger_word\\\": \\\"Deputy\\\", \\\"sent_id\\\": 0, \\\"offset\\\": [21, 22], \\\"id\\\": \\\"7def2447858058feb639e0527b4200ac\\\"}, {\\\"trigger_word\\\": \\\"Prime\\\", \\\"sent_id\\\": 0, \\\"offset\\\": [22, 23], \\\"id\\\": \\\"d65d14264b4088d787f4ce4b9c362268\\\"}, {\\\"trigger_word\\\": \\\"Minister\\\", \\\"sent_id\\\": 0, \\\"offset\\\": [23, 24], \\\"id\\\": \\\"4d652e86937846e8eaf319cdc7357794\\\"}, {\\\"trigger_word\\\": \\\"country\\\", \\\"sent_id\\\": 0, \\\"offset\\\": [26, 27], \\\"id\\\": \\\"5c0381f950cf6441dd372efddaa22629\\\"}, {\\\"trigger_word\\\": \\\"then-Prime\\\", \\\"sent_id\\\": 0, \\\"offset\\\": [28, 29], \\\"id\\\": \\\"43b7a1876a9ee139b5157371ce021417\\\"}, {\\\"trigger_word\\\": \\\"Minister\\\", \\\"sent_id\\\": 0, \\\"offset\\\": [29, 30], \\\"id\\\": \\\"3a2e5584e8fa9676e3485a6b841e74b9\\\"}, {\\\"trigger_word\\\": \\\"Mahathir\\\", \\\"sent_id\\\": 0, \\\"offset\\\": [31, 32], \\\"id\\\": \\\"6c3b9d4c14588a28a6115a3d0c6b0cdf\\\"}, {\\\"trigger_word\\\": \\\"Mohamad\\\", \\\"sent_id\\\": 0, \\\"offset\\\": [32, 33], \\\"id\\\": \\\"59b9aa9e6f013c659555508b4252f3dd\\\"}, {\\\"trigger_word\\\": \\\"month\\\", \\\"sent_id\\\": 0, \\\"offset\\\": [36, 37], \\\"id\\\": \\\"69fa00a2a4191498d4ab4ddafd6e9246\\\"}, {\\\"trigger_word\\\": \\\"massive\\\", \\\"sent_id\\\": 1, \\\"offset\\\": [1, 2], \\\"id\\\": \\\"3bbbebb1afa321a24befc48bc9e91cee\\\"}, {\\\"trigger_word\\\": \\\"movement\\\", \\\"sent_id\\\": 1, \\\"offset\\\": [2, 3], \\\"id\\\": \\\"343df7fbc71573b3767f411396bfd075\\\"}, {\\\"trigger_word\\\": \\\"occurred\\\", \\\"sent_id\\\": 1, \\\"offset\\\": [5, 6], \\\"id\\\": \\\"1de87ca97013c04d4835cf4fff95ff7a\\\"}, {\\\"trigger_word\\\": \\\"country\\\", \\\"sent_id\\\": 1, \\\"offset\\\": [8, 9], \\\"id\\\": \\\"83234c69c6cbdde42002e08d0107303b\\\"}, {\\\"trigger_word\\\": \\\"hosted\\\", \\\"sent_id\\\": 1, \\\"offset\\\": [9, 10], \\\"id\\\": \\\"14c44db634311871590b895e0083b0f9\\\"}, {\\\"trigger_word\\\": \\\"Commonwealth\\\", \\\"sent_id\\\": 1, \\\"offset\\\": [11, 12], \\\"id\\\": \\\"521a3eeac2ced978fc8f26ec9d4dd988\\\"}, {\\\"trigger_word\\\": \\\"Games\\\", \\\"sent_id\\\": 1, \\\"offset\\\": [12, 13], \\\"id\\\": \\\"3b605a75082a313c7bc6e65e751e49ef\\\"}, {\\\"trigger_word\\\": \\\"consisted\\\", \\\"sent_id\\\": 1, \\\"offset\\\": [14, 15], \\\"id\\\": \\\"a65ce743cc4865022eebcc22366c8af7\\\"}, {\\\"trigger_word\\\": \\\"civil\\\", \\\"sent_id\\\": 1, \\\"offset\\\": [16, 17], \\\"id\\\": \\\"47bc98b3d2d45f80d9008f2399c525c4\\\"}, {\\\"trigger_word\\\": \\\"disobedience\\\", \\\"sent_id\\\": 1, \\\"offset\\\": [17, 18], \\\"id\\\": \\\"be323b92f979363b945c564296c7e02a\\\"}, {\\\"trigger_word\\\": \\\"demonstrations\\\", \\\"sent_id\\\": 1, \\\"offset\\\": [19, 20], \\\"id\\\": \\\"ce3f731fc753a78563872f0e1b3e0dc6\\\"}, {\\\"trigger_word\\\": \\\"sit-ins\\\", \\\"sent_id\\\": 1, \\\"offset\\\": [21, 22], \\\"id\\\": \\\"e1aa0a07f9a85f5bbc000150d640606c\\\"}, {\\\"trigger_word\\\": \\\"rioting\\\", \\\"sent_id\\\": 1, \\\"offset\\\": [23, 24], \\\"id\\\": \\\"edbb0e1ca69b4aee31b96d712a2c6cb3\\\"}, {\\\"trigger_word\\\": \\\"occupations\\\", \\\"sent_id\\\": 1, \\\"offset\\\": [25, 26], \\\"id\\\": \\\"cb5b8334b9ec84e0b17d0256f06f3b0c\\\"}, {\\\"trigger_word\\\": \\\"online\\\", \\\"sent_id\\\": 1, \\\"offset\\\": [27, 28], \\\"id\\\": \\\"062c8ca117bdcd73e1a13b078a46ce27\\\"}, {\\\"trigger_word\\\": \\\"activism\\\", \\\"sent_id\\\": 1, \\\"offset\\\": [28, 29], \\\"id\\\": \\\"bd7943e362c789a14044c4b19ca23d48\\\"}, {\\\"trigger_word\\\": \\\"involving\\\", \\\"sent_id\\\": 1, \\\"offset\\\": [30, 31], \\\"id\\\": \\\"e497623b6d7b7641c4ef61eb89eebfc7\\\"}, {\\\"trigger_word\\\": \\\"thousands\\\", \\\"sent_id\\\": 1, \\\"offset\\\": [31, 32], \\\"id\\\": \\\"bc16b5e0b91f4c20e093578ceb96a0b5\\\"}, {\\\"trigger_word\\\": \\\"Malaysia\\\", \\\"sent_id\\\": 1, \\\"offset\\\": [33, 34], \\\"id\\\": \\\"a08a86cb44eaf9c09e329ae937588a94\\\"}, {\\\"trigger_word\\\": \\\"protesting\\\", \\\"sent_id\\\": 1, \\\"offset\\\": [34, 35], \\\"id\\\": \\\"1ee4319364e12c7601b3610787d4f30c\\\"}, {\\\"trigger_word\\\": \\\"Barisan\\\", \\\"sent_id\\\": 1, \\\"offset\\\": [37, 38], \\\"id\\\": \\\"48a4e24a194936b1deda806d3294d27c\\\"}, {\\\"trigger_word\\\": \\\"Nasional\\\", \\\"sent_id\\\": 1, \\\"offset\\\": [38, 39], \\\"id\\\": \\\"33906c8a422293dbca83ebb23647cf0d\\\"}, {\\\"trigger_word\\\": \\\"BN\\\", \\\"sent_id\\\": 1, \\\"offset\\\": [40, 41], \\\"id\\\": \\\"298ec89806e72e173416b6ab998757c1\\\"}, {\\\"trigger_word\\\": \\\"government\\\", \\\"sent_id\\\": 1, \\\"offset\\\": [42, 43], \\\"id\\\": \\\"a51231108ad30b26be6ddae6c93d1eb6\\\"}, {\\\"trigger_word\\\": \\\"Mahathir\\\", \\\"sent_id\\\": 1, \\\"offset\\\": [45, 46], \\\"id\\\": \\\"2131a1b2834b6df58d43e798686cd656\\\"}, {\\\"trigger_word\\\": \\\"Cabinet\\\", \\\"sent_id\\\": 1, \\\"offset\\\": [46, 47], \\\"id\\\": \\\"a5fe4da888bf966446ce67114595ac27\\\"}, {\\\"trigger_word\\\": \\\"movement\\\", \\\"sent_id\\\": 2, \\\"offset\\\": [1, 2], \\\"id\\\": \\\"8050f9a5ec589e83aa060100e679158a\\\"}, {\\\"trigger_word\\\": \\\"started\\\", \\\"sent_id\\\": 2, \\\"offset\\\": [2, 3], \\\"id\\\": \\\"b7e639d484951dec9a3babfb7a02370e\\\"}, {\\\"trigger_word\\\": \\\"political\\\", \\\"sent_id\\\": 2, \\\"offset\\\": [6, 7], \\\"id\\\": \\\"e810babace3637cede8b40750d967e88\\\"}, {\\\"trigger_word\\\": \\\"campaign\\\", \\\"sent_id\\\": 2, \\\"offset\\\": [7, 8], \\\"id\\\": \\\"0a0a66e7645cc0c94cad190e8df97256\\\"}, {\\\"trigger_word\\\": \\\"calling\\\", \\\"sent_id\\\": 2, \\\"offset\\\": [8, 9], \\\"id\\\": \\\"76f2e4b95243f58b86eb1b40c1aa67b4\\\"}, {\\\"trigger_word\\\": \\\"resignation\\\", \\\"sent_id\\\": 2, \\\"offset\\\": [11, 12], \\\"id\\\": \\\"de03a1dbcb5fc9a9135d5bce008cb174\\\"}, {\\\"trigger_word\\\": \\\"Mahathir\\\", \\\"sent_id\\\": 2, \\\"offset\\\": [13, 14], \\\"id\\\": \\\"d3c0d950e68bc0bfd5f5c06409debedd\\\"}, {\\\"trigger_word\\\": \\\"Malaysia\\\", \\\"sent_id\\\": 2, \\\"offset\\\": [15, 16], \\\"id\\\": \\\"6a3ed737266b4b45e7835b35925454e7\\\"}, {\\\"trigger_word\\\": \\\"longest-serving\\\", \\\"sent_id\\\": 2, \\\"offset\\\": [17, 18], \\\"id\\\": \\\"5ec42e9ad73c5a5a27db187105181772\\\"}, {\\\"trigger_word\\\": \\\"Prime\\\", \\\"sent_id\\\": 2, \\\"offset\\\": [18, 19], \\\"id\\\": \\\"bbc8fcd2e0d1d0fef9d873dcf281b28a\\\"}, {\\\"trigger_word\\\": \\\"Minister\\\", \\\"sent_id\\\": 2, \\\"offset\\\": [19, 20], \\\"id\\\": \\\"115f403fb6004307a82c6e464eb921ac\\\"}, {\\\"trigger_word\\\": \\\"end\\\", \\\"sent_id\\\": 2, \\\"offset\\\": [22, 23], \\\"id\\\": \\\"eceb52f71cdb5c6a4db5e36da590c26a\\\"}, {\\\"trigger_word\\\": \\\"corruption\\\", \\\"sent_id\\\": 2, \\\"offset\\\": [24, 25], \\\"id\\\": \\\"6cff498c08d413e72c11af92d6673846\\\"}, {\\\"trigger_word\\\": \\\"cronyism\\\", \\\"sent_id\\\": 2, \\\"offset\\\": [26, 27], \\\"id\\\": \\\"1a9fa0639ae2625a7bdd77d6b9bb2c2c\\\"}, {\\\"trigger_word\\\": \\\"allegedly\\\", \\\"sent_id\\\": 2, \\\"offset\\\": [27, 28], \\\"id\\\": \\\"25a0a063007c116f8074c352abdf02ba\\\"}, {\\\"trigger_word\\\": \\\"associated\\\", \\\"sent_id\\\": 2, \\\"offset\\\": [28, 29], \\\"id\\\": \\\"9f642825190acdb7a52e8ea26c3bc24a\\\"}, {\\\"trigger_word\\\": \\\"government\\\", \\\"sent_id\\\": 2, \\\"offset\\\": [31, 32], \\\"id\\\": \\\"ae426548ee1757102b8088d16ff02f50\\\"}, {\\\"trigger_word\\\": \\\"day\\\", \\\"sent_id\\\": 2, \\\"offset\\\": [34, 35], \\\"id\\\": \\\"eb48302996cc2acd646fbb9a836241af\\\"}, {\\\"trigger_word\\\": \\\"Building\\\", \\\"sent_id\\\": 3, \\\"offset\\\": [0, 1], \\\"id\\\": \\\"af00c8f7b87cb042f1f244acbb315fee\\\"}, {\\\"trigger_word\\\": \\\"momentum\\\", \\\"sent_id\\\": 3, \\\"offset\\\": [3, 4], \\\"id\\\": \\\"3f8d401ee0a1b9fa1d979a60afc990e1\\\"}, {\\\"trigger_word\\\": \\\"Reformasi\\\", \\\"sent_id\\\": 3, \\\"offset\\\": [6, 7], \\\"id\\\": \\\"172ca440da2080bfbb13fb03fcfd8746\\\"}, {\\\"trigger_word\\\": \\\"political\\\", \\\"sent_id\\\": 3, \\\"offset\\\": [9, 10], \\\"id\\\": \\\"9397af29d2c827e8ac6c65a542b31a4d\\\"}, {\\\"trigger_word\\\": \\\"movement\\\", \\\"sent_id\\\": 3, \\\"offset\\\": [10, 11], \\\"id\\\": \\\"145d2c1e80c54edf89efc2427f3b3216\\\"}, {\\\"trigger_word\\\": \\\"called\\\", \\\"sent_id\\\": 3, \\\"offset\\\": [11, 12], \\\"id\\\": \\\"3a80ad8d4aed47caf92c30e35f469f74\\\"}, {\\\"trigger_word\\\": \\\"Social\\\", \\\"sent_id\\\": 3, \\\"offset\\\": [13, 14], \\\"id\\\": \\\"bad7e2777e145a76416c127369b37ecb\\\"}, {\\\"trigger_word\\\": \\\"Justice\\\", \\\"sent_id\\\": 3, \\\"offset\\\": [14, 15], \\\"id\\\": \\\"3b895de54c6f7ee9d19eb23a94dfeb50\\\"}, {\\\"trigger_word\\\": \\\"Movement\\\", \\\"sent_id\\\": 3, \\\"offset\\\": [15, 16], \\\"id\\\": \\\"33bfd13007f4b766246b655a202fb2e0\\\"}, {\\\"trigger_word\\\": \\\"ADIL\\\", \\\"sent_id\\\": 3, \\\"offset\\\": [19, 20], \\\"id\\\": \\\"e98e70ba49adfa9b8ea5360fbc5288d1\\\"}, {\\\"trigger_word\\\": \\\"formed\\\", \\\"sent_id\\\": 3, \\\"offset\\\": [22, 23], \\\"id\\\": \\\"6b929da4cd63f538fc265e592df7a9fd\\\"}, {\\\"trigger_word\\\": \\\"led\\\", \\\"sent_id\\\": 3, \\\"offset\\\": [24, 25], \\\"id\\\": \\\"9687d7d0bf3f74adb64b0ea110d6228f\\\"}, {\\\"trigger_word\\\": \\\"Wan\\\", \\\"sent_id\\\": 3, \\\"offset\\\": [26, 27], \\\"id\\\": \\\"65eba5b14d3618d6527df8702224fac5\\\"}, {\\\"trigger_word\\\": \\\"Azizah\\\", \\\"sent_id\\\": 3, \\\"offset\\\": [27, 28], \\\"id\\\": \\\"ad20bfc68656eeadf24c5d961bf8cce5\\\"}, {\\\"trigger_word\\\": \\\"Wan\\\", \\\"sent_id\\\": 3, \\\"offset\\\": [28, 29], \\\"id\\\": \\\"aea0a2f6045d901f6f6c9f80896d9ca7\\\"}, {\\\"trigger_word\\\": \\\"Ismail\\\", \\\"sent_id\\\": 3, \\\"offset\\\": [29, 30], \\\"id\\\": \\\"03041c9d7ad3fd4f9179fd8ab4080144\\\"}, {\\\"trigger_word\\\": \\\"Anwar\\\", \\\"sent_id\\\": 3, \\\"offset\\\": [31, 32], \\\"id\\\": \\\"b80c5a2a8b55501140fd83931d0d712e\\\"}, {\\\"trigger_word\\\": \\\"wife\\\", \\\"sent_id\\\": 3, \\\"offset\\\": [33, 34], \\\"id\\\": \\\"da6e49c87d679332e3c11d7a3220e44c\\\"}, {\\\"trigger_word\\\": \\\"however\\\", \\\"sent_id\\\": 4, \\\"offset\\\": [0, 1], \\\"id\\\": \\\"96b1f49126164745cc256ecb5b07f302\\\"}, {\\\"trigger_word\\\": \\\"facing\\\", \\\"sent_id\\\": 4, \\\"offset\\\": [3, 4], \\\"id\\\": \\\"d7037a7db4fec1050a9ab2b9cbcb990a\\\"}, {\\\"trigger_word\\\": \\\"difficulties\\\", \\\"sent_id\\\": 4, \\\"offset\\\": [4, 5], \\\"id\\\": \\\"383d15d8db1c6bf5f2ffd1ecbac13902\\\"}, {\\\"trigger_word\\\": \\\"registering\\\", \\\"sent_id\\\": 4, \\\"offset\\\": [6, 7], \\\"id\\\": \\\"b1fca65e2d8eaddc58d98ab5a731b6be\\\"}, {\\\"trigger_word\\\": \\\"adil\\\", \\\"sent_id\\\": 4, \\\"offset\\\": [7, 8], \\\"id\\\": \\\"64e0ec2e327b49f0720e9c9fff42bc98\\\"}, {\\\"trigger_word\\\": \\\"political\\\", \\\"sent_id\\\": 4, \\\"offset\\\": [10, 11], \\\"id\\\": \\\"dcdfe6e6dc00ac7665228107ead39c43\\\"}, {\\\"trigger_word\\\": \\\"party\\\", \\\"sent_id\\\": 4, \\\"offset\\\": [11, 12], \\\"id\\\": \\\"0f2f3a74cb2e7b6a905ce7e2c19e3a5d\\\"}, {\\\"trigger_word\\\": \\\"reformasi\\\", \\\"sent_id\\\": 4, \\\"offset\\\": [14, 15], \\\"id\\\": \\\"4bf52beeb2a06b491b7fbae38337134d\\\"}, {\\\"trigger_word\\\": \\\"movement\\\", \\\"sent_id\\\": 4, \\\"offset\\\": [15, 16], \\\"id\\\": \\\"a3e6e39a6e31fc9fb5690db4c9531bb6\\\"}, {\\\"trigger_word\\\": \\\"took over\\\", \\\"sent_id\\\": 4, \\\"offset\\\": [16, 18], \\\"id\\\": \\\"6c67ec78f439c973ada47e96b55e3aeb\\\"}, {\\\"trigger_word\\\": \\\"small\\\", \\\"sent_id\\\": 4, \\\"offset\\\": [19, 20], \\\"id\\\": \\\"a5abab7406dce6ca2cb1eaf4fbbdfb18\\\"}, {\\\"trigger_word\\\": \\\"dormant\\\", \\\"sent_id\\\": 4, \\\"offset\\\": [20, 21], \\\"id\\\": \\\"8cdcb4e2f89261fa480910b8d7cb3b2d\\\"}, {\\\"trigger_word\\\": \\\"party\\\", \\\"sent_id\\\": 4, \\\"offset\\\": [21, 22], \\\"id\\\": \\\"e9e384e91e639603b0228235ed30c41e\\\"}, {\\\"trigger_word\\\": \\\"unk\\\", \\\"sent_id\\\": 4, \\\"offset\\\": [23, 24], \\\"id\\\": \\\"01bf795a6634ed5205a248a77d35d036\\\"}, {\\\"trigger_word\\\": \\\"masyarakat\\\", \\\"sent_id\\\": 4, \\\"offset\\\": [24, 25], \\\"id\\\": \\\"b34548c21bab27606a810474f6ffd993\\\"}, {\\\"trigger_word\\\": \\\"islam\\\", \\\"sent_id\\\": 4, \\\"offset\\\": [25, 26], \\\"id\\\": \\\"a30a9d4557b38dc113b70493e63049dd\\\"}, {\\\"trigger_word\\\": \\\"malaysia\\\", \\\"sent_id\\\": 4, \\\"offset\\\": [26, 27], \\\"id\\\": \\\"1b8fad39f3a9d7c061203c64d2f67368\\\"}, {\\\"trigger_word\\\": \\\"unk\\\", \\\"sent_id\\\": 4, \\\"offset\\\": [29, 30], \\\"id\\\": \\\"c1887067b1e872c19023364619191463\\\"}, {\\\"trigger_word\\\": \\\"led to\\\", \\\"sent_id\\\": 4, \\\"offset\\\": [32, 34], \\\"id\\\": \\\"1ed5d66fe05442a8351adee55591ab2f\\\"}, {\\\"trigger_word\\\": \\\"formation\\\", \\\"sent_id\\\": 4, \\\"offset\\\": [35, 36], \\\"id\\\": \\\"5456cb879f368e7a2d1dff0152811fc1\\\"}, {\\\"trigger_word\\\": \\\"new\\\", \\\"sent_id\\\": 4, \\\"offset\\\": [38, 39], \\\"id\\\": \\\"228f7a79fa433c6b6a4b313cf999a5e7\\\"}, {\\\"trigger_word\\\": \\\"unk\\\", \\\"sent_id\\\": 4, \\\"offset\\\": [39, 40], \\\"id\\\": \\\"9ccd5a4df33c1345be681ac808acc2dc\\\"}, {\\\"trigger_word\\\": \\\"party\\\", \\\"sent_id\\\": 4, \\\"offset\\\": [40, 41], \\\"id\\\": \\\"82f3665b87751aa7391c65d672c7ba8b\\\"}, {\\\"trigger_word\\\": \\\"named\\\", \\\"sent_id\\\": 4, \\\"offset\\\": [41, 42], \\\"id\\\": \\\"cfc27a8f7a53b6c24047064432941e7b\\\"}, {\\\"trigger_word\\\": \\\"parti\\\", \\\"sent_id\\\": 4, \\\"offset\\\": [43, 44], \\\"id\\\": \\\"d857583073444c456e702c1ea96fb7d3\\\"}, {\\\"trigger_word\\\": \\\"keadilan\\\", \\\"sent_id\\\": 4, \\\"offset\\\": [44, 45], \\\"id\\\": \\\"928e95c3a62872a31067f8f053ca5ce7\\\"}, {\\\"trigger_word\\\": \\\"nasional\\\", \\\"sent_id\\\": 4, \\\"offset\\\": [45, 46], \\\"id\\\": \\\"c1f29ce7ab7d8d45c05fc46a9e314099\\\"}, {\\\"trigger_word\\\": \\\"national\\\", \\\"sent_id\\\": 4, \\\"offset\\\": [48, 49], \\\"id\\\": \\\"d6f641236d36204ea260d77aeec0e0fa\\\"}, {\\\"trigger_word\\\": \\\"justice\\\", \\\"sent_id\\\": 4, \\\"offset\\\": [49, 50], \\\"id\\\": \\\"521c15426a0394e84e15a2f16dfdcf33\\\"}, {\\\"trigger_word\\\": \\\"party\\\", \\\"sent_id\\\": 4, \\\"offset\\\": [50, 51], \\\"id\\\": \\\"9908ab44a0db512c67528deea9613435\\\"}, {\\\"trigger_word\\\": \\\"keadilan\\\", \\\"sent_id\\\": 4, \\\"offset\\\": [52, 53], \\\"id\\\": \\\"d7e45d3516996a512286174d57ee187b\\\"}, {\\\"trigger_word\\\": \\\"August\\\", \\\"sent_id\\\": 5, \\\"offset\\\": [2, 3], \\\"id\\\": \\\"88289be23c487058ec93f3571f7d4d8e\\\"}, {\\\"trigger_word\\\": \\\"newly\\\", \\\"sent_id\\\": 5, \\\"offset\\\": [6, 7], \\\"id\\\": \\\"aed49d550c3b3629d9e5b01c42693858\\\"}, {\\\"trigger_word\\\": \\\"merged\\\", \\\"sent_id\\\": 5, \\\"offset\\\": [7, 8], \\\"id\\\": \\\"185bafeac5e27407149f9b7e1fb82081\\\"}, {\\\"trigger_word\\\": \\\"entity\\\", \\\"sent_id\\\": 5, \\\"offset\\\": [8, 9], \\\"id\\\": \\\"ca2af89bc65348fa033d9b2aea722313\\\"}, {\\\"trigger_word\\\": \\\"KEADILAN\\\", \\\"sent_id\\\": 5, \\\"offset\\\": [10, 11], \\\"id\\\": \\\"a5992283d83aa1f54a82b0dba99f9a92\\\"}, {\\\"trigger_word\\\": \\\"Parti\\\", \\\"sent_id\\\": 5, \\\"offset\\\": [13, 14], \\\"id\\\": \\\"3f58deeaeaf147083d68d0088bba1e35\\\"}, {\\\"trigger_word\\\": \\\"Rakyat\\\", \\\"sent_id\\\": 5, \\\"offset\\\": [14, 15], \\\"id\\\": \\\"c778c9d0dcb1f3be66270113603f5c1e\\\"}, {\\\"trigger_word\\\": \\\"Malaysia\\\", \\\"sent_id\\\": 5, \\\"offset\\\": [15, 16], \\\"id\\\": \\\"61a8d53b636dc24ccd49158a89fa13a8\\\"}, {\\\"trigger_word\\\": \\\"PRM\\\", \\\"sent_id\\\": 5, \\\"offset\\\": [18, 19], \\\"id\\\": \\\"3021c4be6861837aeb6d95e279e744f8\\\"}, {\\\"trigger_word\\\": \\\"officially\\\", \\\"sent_id\\\": 5, \\\"offset\\\": [21, 22], \\\"id\\\": \\\"35c890f7d65a5b67d94ca6d60b356790\\\"}, {\\\"trigger_word\\\": \\\"launched\\\", \\\"sent_id\\\": 5, \\\"offset\\\": [22, 23], \\\"id\\\": \\\"5bd47223c5979787022498a409b60afd\\\"}, {\\\"trigger_word\\\": \\\"assumed\\\", \\\"sent_id\\\": 5, \\\"offset\\\": [24, 25], \\\"id\\\": \\\"b005d927c60be1fa3ef69bd78e3e4742\\\"}, {\\\"trigger_word\\\": \\\"current\\\", \\\"sent_id\\\": 5, \\\"offset\\\": [26, 27], \\\"id\\\": \\\"d9906c8ed10f15e897dbfab02405dba4\\\"}, {\\\"trigger_word\\\": \\\"name\\\", \\\"sent_id\\\": 5, \\\"offset\\\": [27, 28], \\\"id\\\": \\\"540ef7f7af9231b5ffe7a898bc31009e\\\"}, {\\\"trigger_word\\\": \\\"Parti\\\", \\\"sent_id\\\": 5, \\\"offset\\\": [30, 31], \\\"id\\\": \\\"036c2acc0e9cdeff797053fa718d2f77\\\"}, {\\\"trigger_word\\\": \\\"Keadilan\\\", \\\"sent_id\\\": 5, \\\"offset\\\": [31, 32], \\\"id\\\": \\\"cbec5145e14d372142118024298cf21b\\\"}, {\\\"trigger_word\\\": \\\"Rakyat\\\", \\\"sent_id\\\": 5, \\\"offset\\\": [32, 33], \\\"id\\\": \\\"c788e68cbe901b3ff71fd3c6a5c894d3\\\"}, {\\\"trigger_word\\\": \\\"PKR\\\", \\\"sent_id\\\": 5, \\\"offset\\\": [34, 35], \\\"id\\\": \\\"c90aa54ac832b1f9097408f2e832443e\\\"}, {\\\"trigger_word\\\": \\\"Reformasi\\\", \\\"sent_id\\\": 6, \\\"offset\\\": [1, 2], \\\"id\\\": \\\"099a1e3361eb81f6a753f5991d7b4263\\\"}, {\\\"trigger_word\\\": \\\"movement\\\", \\\"sent_id\\\": 6, \\\"offset\\\": [2, 3], \\\"id\\\": \\\"b1742bc3c74a76bd20e755ed9ae58048\\\"}, {\\\"trigger_word\\\": \\\"still\\\", \\\"sent_id\\\": 6, \\\"offset\\\": [4, 5], \\\"id\\\": \\\"e0a330485e92cbdd5e356c664b7fd909\\\"}, {\\\"trigger_word\\\": \\\"ongoing\\\", \\\"sent_id\\\": 6, \\\"offset\\\": [8, 9], \\\"id\\\": \\\"23b3cbb768eb2ea728f68dd3fc277615\\\"}, {\\\"trigger_word\\\": \\\"even\\\", \\\"sent_id\\\": 6, \\\"offset\\\": [9, 10], \\\"id\\\": \\\"959f0c3b9bf3c12d556e8e454daabb34\\\"}, {\\\"trigger_word\\\": \\\"Malaysian\\\", \\\"sent_id\\\": 6, \\\"offset\\\": [13, 14], \\\"id\\\": \\\"bbdd42adbf2c3f6cafb9bfb97f03a653\\\"}, {\\\"trigger_word\\\": \\\"general\\\", \\\"sent_id\\\": 6, \\\"offset\\\": [14, 15], \\\"id\\\": \\\"bf049bce8b40521ba29a35a1f9298412\\\"}, {\\\"trigger_word\\\": \\\"election\\\", \\\"sent_id\\\": 6, \\\"offset\\\": [15, 16], \\\"id\\\": \\\"dd8cd68412403aac5a4b92fa73814b4c\\\"}, {\\\"trigger_word\\\": \\\"saw\\\", \\\"sent_id\\\": 6, \\\"offset\\\": [17, 18], \\\"id\\\": \\\"daa3c7337b3ba05396abda9722c03915\\\"}, {\\\"trigger_word\\\": \\\"Barisan\\\", \\\"sent_id\\\": 6, \\\"offset\\\": [18, 19], \\\"id\\\": \\\"4937cbc48cc4d392f5e29f54fcf43f1e\\\"}, {\\\"trigger_word\\\": \\\"Nasional\\\", \\\"sent_id\\\": 6, \\\"offset\\\": [19, 20], \\\"id\\\": \\\"e655b5de9c7df96f52ef7c314710ffe1\\\"}, {\\\"trigger_word\\\": \\\"BN\\\", \\\"sent_id\\\": 6, \\\"offset\\\": [21, 22], \\\"id\\\": \\\"afaa608ca3f829db72c0f4713e38e79a\\\"}, {\\\"trigger_word\\\": \\\"lose\\\", \\\"sent_id\\\": 6, \\\"offset\\\": [23, 24], \\\"id\\\": \\\"3fdc46ec00591374ef801a9a8dc14952\\\"}, {\\\"trigger_word\\\": \\\"parliamentary\\\", \\\"sent_id\\\": 6, \\\"offset\\\": [25, 26], \\\"id\\\": \\\"9ada8f94ab70c8c87687b8e84fe0a78e\\\"}, {\\\"trigger_word\\\": \\\"majority\\\", \\\"sent_id\\\": 6, \\\"offset\\\": [26, 27], \\\"id\\\": \\\"fe3b41ec7aecd812afd4609fb78bfad1\\\"}, {\\\"trigger_word\\\": \\\"Pakatan\\\", \\\"sent_id\\\": 6, \\\"offset\\\": [29, 30], \\\"id\\\": \\\"6c3d106cc3c7f3b3161a8a1c53c82966\\\"}, {\\\"trigger_word\\\": \\\"Harapan\\\", \\\"sent_id\\\": 6, \\\"offset\\\": [30, 31], \\\"id\\\": \\\"be43a849dcb5e9e9b7f5332da156ab5d\\\"}, {\\\"trigger_word\\\": \\\"PH\\\", \\\"sent_id\\\": 6, \\\"offset\\\": [32, 33], \\\"id\\\": \\\"318ba5c3343013c68c3aaf339afe344a\\\"}, {\\\"trigger_word\\\": \\\"coalition\\\", \\\"sent_id\\\": 6, \\\"offset\\\": [34, 35], \\\"id\\\": \\\"6f32b0b26056fa0a8ac19e438ad6aca6\\\"}, {\\\"trigger_word\\\": \\\"first\\\", \\\"sent_id\\\": 6, \\\"offset\\\": [38, 39], \\\"id\\\": \\\"997bdced0fd30b6bd6cf63da5e102dea\\\"}, {\\\"trigger_word\\\": \\\"time\\\", \\\"sent_id\\\": 6, \\\"offset\\\": [39, 40], \\\"id\\\": \\\"74948931fb67cf0ba0931b4c691f6c7d\\\"}, {\\\"trigger_word\\\": \\\"Malaysia\\\", \\\"sent_id\\\": 6, \\\"offset\\\": [41, 42], \\\"id\\\": \\\"a4c1eb76922a239033cd39934469bc53\\\"}, {\\\"trigger_word\\\": \\\"independence\\\", \\\"sent_id\\\": 6, \\\"offset\\\": [43, 44], \\\"id\\\": \\\"3ee4047ce83ea3171c1cb82145234664\\\"}, {\\\"trigger_word\\\": \\\"become\\\", \\\"sent_id\\\": 6, \\\"offset\\\": [44, 45], \\\"id\\\": \\\"9a0662169ef9c97d8e52231ed5e7dbd9\\\"}, {\\\"trigger_word\\\": \\\"official\\\", \\\"sent_id\\\": 6, \\\"offset\\\": [46, 47], \\\"id\\\": \\\"7d6956cc2d09892df454b260834dbf24\\\"}, {\\\"trigger_word\\\": \\\"opposition\\\", \\\"sent_id\\\": 6, \\\"offset\\\": [47, 48], \\\"id\\\": \\\"0ba64c0a600c0d788b49476cfe864bc5\\\"}]}\\n/root/schema-dag-extraction/data/maven/test.jsonl:751:{\\\"title\\\": \\\"Subsonic Music Festival\\\", \\\"id\\\": \\\"762757b43ac997d469e2f8d99a459cd0\\\", \\\"content\\\": [{\\\"sentence\\\": \\\"Subsonic Music Festival is an annual electronic music festival held since December 2008 in a camping setting in Monkerai, Australia.\\\", \\\"tokens\\\": [\\\"Subsonic\\\", \\\"Music\\\", \\\"Festival\\\", \\\"is\\\", \\\"an\\\", \\\"annual\\\", \\\"electronic\\\", \\\"music\\\", \\\"festival\\\", \\\"held\\\", \\\"since\\\", \\\"December\\\", \\\"2008\\\", \\\"in\\\", \\\"a\\\", \\\"camping\\\", \\\"setting\\\", \\\"in\\\", \\\"Monkerai\\\", \\\",\\\", \\\"Australia\\\", \\\".\\\"]}, {\\\"sentence\\\": \\\"It was established by Scott Commens (Sydney-based DJ as MSG) and Marco Mazzucco (Sydney-based DJ as Marcotix).\\\", \\\"tokens\\\": [\\\"It\\\", \\\"was\\\", \\\"established\\\", \\\"by\\\", \\\"Scott\\\", \\\"Commens\\\", \\\"(\\\", \\\"Sydney-based\\\", \\\"DJ\\\", \\\"as\\\", \\\"MSG\\\", \\\")\\\", \\\"and\\\", \\\"Marco\\\", \\\"Mazzucco\\\", \\\"(\\\", \\\"Sydney-based\\\", \\\"DJ\\\", \\\"as\\\", \\\"Marcotix\\\", \\\")\\\", \\\".\\\"]}, {\\\"sentence\\\": \\\"\\\\\\\"TimeOut Sydney\\\\\\\"s Erin Moy said genres in 2012 included \\\\\\\"beats.\\\", \\\"tokens\\\": [\\\"``\\\", \\\"TimeOut\\\", \\\"Sydney\\\", \\\"''\\\", \\\"s\\\", \\\"Erin\\\", \\\"Moy\\\", \\\"said\\\", \\\"genres\\\", \\\"in\\\", \\\"2012\\\", \\\"included\\\", \\\"``\\\", \\\"beats\\\", \\\".\\\"]}, {\\\"sentence\\\": \\\"From thumping four to the floor and tummy-rumbling bass,\\\\\\\" including dub, techno and hip hop.\\\", \\\"tokens\\\": [\\\"From\\\", \\\"thumping\\\", \\\"four\\\", \\\"to\\\", \\\"the\\\", \\\"floor\\\", \\\"and\\\", \\\"tummy-rumbling\\\", \\\"bass\\\", \\\",\\\", \\\"''\\\", \\\"including\\\", \\\"dub\\\", \\\",\\\", \\\"techno\\\", \\\"and\\\", \\\"hip\\\", \\\"hop\\\", \\\".\\\"]}, {\\\"sentence\\\": \\\"Pulse Radio in Australia gave the 2012 event a positive review.\\\", \\\"tokens\\\": [\\\"Pulse\\\", \\\"Radio\\\", \\\"in\\\", \\\"Australia\\\", \\\"gave\\\", \\\"the\\\", \\\"2012\\\", \\\"event\\\", \\\"a\\\", \\\"positive\\\", \\\"review\\\", \\\".\\\"]}, {\\\"sentence\\\": \\\"Among the artists that have performed are DJ Kentaro James Holden, Factory Floor, and Mike Huckaby.\\\", \\\"tokens\\\": [\\\"Among\\\", \\\"the\\\", \\\"artists\\\", \\\"that\\\", \\\"have\\\", \\\"performed\\\", \\\"are\\\", \\\"DJ\\\", \\\"Kentaro\\\", \\\"James\\\", \\\"Holden\\\", \\\",\\\", \\\"Factory\\\", \\\"Floor\\\", \\\",\\\", \\\"and\\\", \\\"Mike\\\", \\\"Huckaby\\\", \\\".\\\"]}, {\\\"sentence\\\": \\\"In 2014 it took place at Riverwood Downs Mountain Valley Resort.\\\", \\\"tokens\\\": [\\\"In\\\", \\\"2014\\\", \\\"it\\\", \\\"took\\\", \\\"place\\\", \\\"at\\\", \\\"Riverwood\\\", \\\"Downs\\\", \\\"Mountain\\\", \\\"Valley\\\", \\\"Resort\\\", \\\".\\\"]}, {\\\"sentence\\\": \\\"\\\\\\\"Resident Advisor\\\\\\\" editors described that year's festival: \\\\\\\"Subsonic has gradually embraced house, techno and other forms of dance music alongside its original staples: psytrance and dub.\\\\\\\"\\\", \\\"tokens\\\": [\\\"``\\\", \\\"Resident\\\", \\\"Advisor\\\", \\\"''\\\", \\\"editors\\\", \\\"described\\\", \\\"that\\\", \\\"year\\\", \\\"'s\\\", \\\"festival\\\", \\\":\\\", \\\"``\\\", \\\"Subsonic\\\", \\\"has\\\", \\\"gradually\\\", \\\"embraced\\\", \\\"house\\\", \\\",\\\", \\\"techno\\\", \\\"and\\\", \\\"other\\\", \\\"forms\\\", \\\"of\\\", \\\"dance\\\", \\\"music\\\", \\\"alongside\\\", \\\"its\\\", \\\"original\\\", \\\"staples\\\", \\\":\\\", \\\"psytrance\\\", \\\"and\\\", \\\"dub\\\", \\\".\\\", \\\"''\\\"]}, {\\\"sentence\\\": \\\"\\\\\\\"Resident Advisor\\\\\\\" also listed Subsonic on its Top 10 November / December 2014 Festivals, from around the world.\\\", \\\"tokens\\\": [\\\"``\\\", \\\"Resident\\\", \\\"Advisor\\\", \\\"''\\\", \\\"also\\\", \\\"listed\\\", \\\"Subsonic\\\", \\\"on\\\", \\\"its\\\", \\\"Top\\\", \\\"10\\\", \\\"November\\\", \\\"/\\\", \\\"December\\\", \\\"2014\\\", \\\"Festivals\\\", \\\",\\\", \\\"from\\\", \\\"around\\\", \\\"the\\\", \\\"world\\\", \\\".\\\"]}], \\\"candidates\\\": [{\\\"trigger_word\\\": \\\"Subsonic\\\", \\\"sent_id\\\": 0, \\\"offset\\\": [0, 1], \\\"id\\\": \\\"95d9d84bd9e1cc48d38b5b19c64de628\\\"}, {\\\"trigger_word\\\": \\\"Music\\\", \\\"sent_id\\\": 0, \\\"offset\\\": [1, 2], \\\"id\\\": \\\"a053a686e254111e6b45acf64b545df2\\\"}, {\\\"trigger_word\\\": \\\"Festival\\\", \\\"sent_id\\\": 0, \\\"offset\\\": [2, 3], \\\"id\\\": \\\"23cf32e75324ab72f61f36f428946d14\\\"}, {\\\"trigger_word\\\": \\\"annual\\\", \\\"sent_id\\\": 0, \\\"offset\\\": [5, 6], \\\"id\\\": \\\"ecbb73d8dbcf501d11360198d39b92a8\\\"}, {\\\"trigger_word\\\": \\\"electronic\\\", \\\"sent_id\\\": 0, \\\"offset\\\": [6, 7], \\\"id\\\": \\\"6eb9675d1495b14b2b62938eb557d7f1\\\"}, {\\\"trigger_word\\\": \\\"music\\\", \\\"sent_id\\\": 0, \\\"offset\\\": [7, 8], \\\"id\\\": \\\"00ea29909cb411b9cd7dfa1d0217bec6\\\"}, {\\\"trigger_word\\\": \\\"festival\\\", \\\"sent_id\\\": 0, \\\"offset\\\": [8, 9], \\\"id\\\": \\\"bafd4f60af4a052be73c988e807b179a\\\"}, {\\\"trigger_word\\\": \\\"held\\\", \\\"sent_id\\\": 0, \\\"offset\\\": [9, 10], \\\"id\\\": \\\"1eb8c0349b6f5ce0c227ff8ae7ffdd02\\\"}, {\\\"trigger_word\\\": \\\"December\\\", \\\"sent_id\\\": 0, \\\"offset\\\": [11, 12], \\\"id\\\": \\\"87173faac0ffb8e70cf851bc7b2a6f4f\\\"}, {\\\"trigger_word\\\": \\\"camping\\\", \\\"sent_id\\\": 0, \\\"offset\\\": [15, 16], \\\"id\\\": \\\"749a1352ccbf7a7cc39591eec6274214\\\"}, {\\\"trigger_word\\\": \\\"setting\\\", \\\"sent_id\\\": 0, \\\"offset\\\": [16, 17], \\\"id\\\": \\\"9aa2e0882137986161b87338204c1c19\\\"}, {\\\"trigger_word\\\": \\\"Monkerai\\\", \\\"sent_id\\\": 0, \\\"offset\\\": [18, 19], \\\"id\\\": \\\"63bd3d7c6fee5ffe7d127c68afe0776b\\\"}, {\\\"trigger_word\\\": \\\"Australia\\\", \\\"sent_id\\\": 0, \\\"offset\\\": [20, 21], \\\"id\\\": \\\"b9dbde2a4902329e78f562e4dacfd936\\\"}, {\\\"trigger_word\\\": \\\"established\\\", \\\"sent_id\\\": 1, \\\"offset\\\": [2, 3], \\\"id\\\": \\\"4f37c937e2f661a4dbe13b1dcc780501\\\"}, {\\\"trigger_word\\\": \\\"Scott\\\", \\\"sent_id\\\": 1, \\\"offset\\\": [4, 5], \\\"id\\\": \\\"f9a5c1f75985eb1a955a7ee0c186e6c2\\\"}, {\\\"trigger_word\\\": \\\"Commens\\\", \\\"sent_id\\\": 1, \\\"offset\\\": [5, 6], \\\"id\\\": \\\"a6d680858477c597bb878e24a1cbac13\\\"}, {\\\"trigger_word\\\": \\\"Sydney-based\\\", \\\"sent_id\\\": 1, \\\"offset\\\": [7, 8], \\\"id\\\": \\\"699aec6ce9b53e6d2414acfa9c0700c7\\\"}, {\\\"trigger_word\\\": \\\"DJ\\\", \\\"sent_id\\\": 1, \\\"offset\\\": [8, 9], \\\"id\\\": \\\"3b13129e7993ede75297a8f6d2c8d164\\\"}, {\\\"trigger_word\\\": \\\"MSG\\\", \\\"sent_id\\\": 1, \\\"offset\\\": [10, 11], \\\"id\\\": \\\"5c837ca562c69289426d993411c28c01\\\"}, {\\\"trigger_word\\\": \\\"Marco\\\", \\\"sent_id\\\": 1, \\\"offset\\\": [13, 14], \\\"id\\\": \\\"69d29c85cbf15abd70e6e054ca83df6d\\\"}, {\\\"trigger_word\\\": \\\"Mazzucco\\\", \\\"sent_id\\\": 1, \\\"offset\\\": [14, 15], \\\"id\\\": \\\"f72f1fd6afeb81e2f622aef4ed025b11\\\"}, {\\\"trigger_word\\\": \\\"Sydney-based\\\", \\\"sent_id\\\": 1, \\\"offset\\\": [16, 17], \\\"id\\\": \\\"e0813b84c1e3ffe666dd8c8d391c375c\\\"}, {\\\"trigger_word\\\": \\\"DJ\\\", \\\"sent_id\\\": 1, \\\"offset\\\": [17, 18], \\\"id\\\": \\\"4eaba7cd9c4eb6002f82c0a5520bd2b4\\\"}, {\\\"trigger_word\\\": \\\"Marcotix\\\", \\\"sent_id\\\": 1, \\\"offset\\\": [19, 20], \\\"id\\\": \\\"f9666daf9d4be45f24793b5d8c33d8a4\\\"}, {\\\"trigger_word\\\": \\\"Sydney\\\", \\\"sent_id\\\": 2, \\\"offset\\\": [2, 3], \\\"id\\\": \\\"1e3f7e879a70d8c164297c8804f7ba9a\\\"}, {\\\"trigger_word\\\": \\\"Erin\\\", \\\"sent_id\\\": 2, \\\"offset\\\": [5, 6], \\\"id\\\": \\\"d5d1a95486c7001bf3394c1e93e779e8\\\"}, {\\\"trigger_word\\\": \\\"Moy\\\", \\\"sent_id\\\": 2, \\\"offset\\\": [6, 7], \\\"id\\\": \\\"92fdd71f71c09cb9c6fdcedc6462321a\\\"}, {\\\"trigger_word\\\": \\\"said\\\", \\\"sent_id\\\": 2, \\\"offset\\\": [7, 8], \\\"id\\\": \\\"b1aed14495db4cbc18e377a7f05f54a1\\\"}, {\\\"trigger_word\\\": \\\"genres\\\", \\\"sent_id\\\": 2, \\\"offset\\\": [8, 9], \\\"id\\\": \\\"6e54fb39611e0eca0252981edb688838\\\"}, {\\\"trigger_word\\\": \\\"included\\\", \\\"sent_id\\\": 2, \\\"offset\\\": [11, 12], \\\"id\\\": \\\"c5d988efe5c9f29c53cf1f6a481b2dd2\\\"}, {\\\"trigger_word\\\": \\\"beats\\\", \\\"sent_id\\\": 2, \\\"offset\\\": [13, 14], \\\"id\\\": \\\"0fbc8814d7901f19c1e6707bec2113f6\\\"}, {\\\"trigger_word\\\": \\\"thumping\\\", \\\"sent_id\\\": 3, \\\"offset\\\": [1, 2], \\\"id\\\": \\\"9ed0699aa2945ae64bc06b3de6411594\\\"}, {\\\"trigger_word\\\": \\\"floor\\\", \\\"sent_id\\\": 3, \\\"offset\\\": [5, 6], \\\"id\\\": \\\"491b4d9aa510df4846395149789c2e1a\\\"}, {\\\"trigger_word\\\": \\\"tummy-rumbling\\\", \\\"sent_id\\\": 3, \\\"offset\\\": [7, 8], \\\"id\\\": \\\"b0d0f5887e1f09b0e2e18ce501301124\\\"}, {\\\"trigger_word\\\": \\\"bass\\\", \\\"sent_id\\\": 3, \\\"offset\\\": [8, 9], \\\"id\\\": \\\"2300439c71cf66635d2dbc47f0f80caa\\\"}, {\\\"trigger_word\\\": \\\"including\\\", \\\"sent_id\\\": 3, \\\"offset\\\": [11, 12], \\\"id\\\": \\\"541931627bf76a8ab1cb28519882df6a\\\"}, {\\\"trigger_word\\\": \\\"dub\\\", \\\"sent_id\\\": 3, \\\"offset\\\": [12, 13], \\\"id\\\": \\\"e8f113e2034a2b7d638b2feb29f883d7\\\"}, {\\\"trigger_word\\\": \\\"techno\\\", \\\"sent_id\\\": 3, \\\"offset\\\": [14, 15], \\\"id\\\": \\\"bac1aeb48408d1c9def57a4fe5f8ef5c\\\"}, {\\\"trigger_word\\\": \\\"hip\\\", \\\"sent_id\\\": 3, \\\"offset\\\": [16, 17], \\\"id\\\": \\\"2ea658fd2373c21821cd5a7088ca8125\\\"}, {\\\"trigger_word\\\": \\\"hop\\\", \\\"sent_id\\\": 3, \\\"offset\\\": [17, 18], \\\"id\\\": \\\"2f7cc248369e370bbe50b7a4a6b7e51b\\\"}, {\\\"trigger_word\\\": \\\"Pulse\\\", \\\"sent_id\\\": 4, \\\"offset\\\": [0, 1], \\\"id\\\": \\\"647f95b78ad3a11d19183034f0ea1271\\\"}, {\\\"trigger_word\\\": \\\"Radio\\\", \\\"sent_id\\\": 4, \\\"offset\\\": [1, 2], \\\"id\\\": \\\"234b2d8f2bda483cf7c746df25b4ce58\\\"}, {\\\"trigger_word\\\": \\\"Australia\\\", \\\"sent_id\\\": 4, \\\"offset\\\": [3, 4], \\\"id\\\": \\\"abed7bced9e1b412c3d6613d7595ca82\\\"}, {\\\"trigger_word\\\": \\\"gave\\\", \\\"sent_id\\\": 4, \\\"offset\\\": [4, 5], \\\"id\\\": \\\"6c90d8d1f4ea27a6016cd43ca8eb7adb\\\"}, {\\\"trigger_word\\\": \\\"event\\\", \\\"sent_id\\\": 4, \\\"offset\\\": [7, 8], \\\"id\\\": \\\"f0ff2511c0b390c26b740e3aecad1259\\\"}, {\\\"trigger_word\\\": \\\"positive\\\", \\\"sent_id\\\": 4, \\\"offset\\\": [9, 10], \\\"id\\\": \\\"d4bbf6c796672e580c08194aa08315bb\\\"}, {\\\"trigger_word\\\": \\\"review\\\", \\\"sent_id\\\": 4, \\\"offset\\\": [10, 11], \\\"id\\\": \\\"07b09ebaef6af1a5329446335c92557c\\\"}, {\\\"trigger_word\\\": \\\"artists\\\", \\\"sent_id\\\": 5, \\\"offset\\\": [2, 3], \\\"id\\\": \\\"10690bbf3ec5e041b19424d548f886d4\\\"}, {\\\"trigger_word\\\": \\\"performed\\\", \\\"sent_id\\\": 5, \\\"offset\\\": [5, 6], \\\"id\\\": \\\"b625eaa1063ef8795f7b9bd5c66755ce\\\"}, {\\\"trigger_word\\\": \\\"DJ\\\", \\\"sent_id\\\": 5, \\\"offset\\\": [7, 8], \\\"id\\\": \\\"612a4ea9f58673061d6a643dd38e2aef\\\"}, {\\\"trigger_word\\\": \\\"Kentaro\\\", \\\"sent_id\\\": 5, \\\"offset\\\": [8, 9], \\\"id\\\": \\\"0f9736bc96d339f9a3b65c2b9b11641b\\\"}, {\\\"trigger_word\\\": \\\"James\\\", \\\"sent_id\\\": 5, \\\"offset\\\": [9, 10], \\\"id\\\": \\\"209162b2c2e0004f858ae678bc2cc158\\\"}, {\\\"trigger_word\\\": \\\"Holden\\\", \\\"sent_id\\\": 5, \\\"offset\\\": [10, 11], \\\"id\\\": \\\"c00fe539b91d566b05165638b1f662ba\\\"}, {\\\"trigger_word\\\": \\\"Factory\\\", \\\"sent_id\\\": 5, \\\"offset\\\": [12, 13], \\\"id\\\": \\\"36cf4227da06e8b664171d8c9db7c0a6\\\"}, {\\\"trigger_word\\\": \\\"Floor\\\", \\\"sent_id\\\": 5, \\\"offset\\\": [13, 14], \\\"id\\\": \\\"f731ee80d2d00103dd130e89e0a16f03\\\"}, {\\\"trigger_word\\\": \\\"Mike\\\", \\\"sent_id\\\": 5, \\\"offset\\\": [16, 17], \\\"id\\\": \\\"c4d7cb9d74a1800eab043e68f9dc584f\\\"}, {\\\"trigger_word\\\": \\\"Huckaby\\\", \\\"sent_id\\\": 5, \\\"offset\\\": [17, 18], \\\"id\\\": \\\"c22401e69f59bec75451eaf228011f4a\\\"}, {\\\"trigger_word\\\": \\\"took place\\\", \\\"sent_id\\\": 6, \\\"offset\\\": [3, 5], \\\"id\\\": \\\"1a1e4f40974675184e9940b3e64094b4\\\"}, {\\\"trigger_word\\\": \\\"Riverwood\\\", \\\"sent_id\\\": 6, \\\"offset\\\": [6, 7], \\\"id\\\": \\\"0367c4dcba424fef414fc689dc8d732b\\\"}, {\\\"trigger_word\\\": \\\"Downs\\\", \\\"sent_id\\\": 6, \\\"offset\\\": [7, 8], \\\"id\\\": \\\"63c7241f41d05f4af946426cf0c382ce\\\"}, {\\\"trigger_word\\\": \\\"Mountain\\\", \\\"sent_id\\\": 6, \\\"offset\\\": [8, 9], \\\"id\\\": \\\"8f9184ef056d8606f80d9eff7af41af9\\\"}, {\\\"trigger_word\\\": \\\"Valley\\\", \\\"sent_id\\\": 6, \\\"offset\\\": [9, 10], \\\"id\\\": \\\"217b7b1edaec1eac6d38b31b5746093e\\\"}, {\\\"trigger_word\\\": \\\"Resort\\\", \\\"sent_id\\\": 6, \\\"offset\\\": [10, 11], \\\"id\\\": \\\"62455d6f9d0de4b1ecf7a9d49f87b77d\\\"}, {\\\"trigger_word\\\": \\\"Resident\\\", \\\"sent_id\\\": 7, \\\"offset\\\": [1, 2], \\\"id\\\": \\\"706651e041c30c5c12663f43dfa2cc9a\\\"}, {\\\"trigger_word\\\": \\\"Advisor\\\", \\\"sent_id\\\": 7, \\\"offset\\\": [2, 3], \\\"id\\\": \\\"afaa05126e949db48e9ff47e52bc6e29\\\"}, {\\\"trigger_word\\\": \\\"editors\\\", \\\"sent_id\\\": 7, \\\"offset\\\": [4, 5], \\\"id\\\": \\\"d4b6ba17aa3e03d89a9c204e48633e90\\\"}, {\\\"trigger_word\\\": \\\"described\\\", \\\"sent_id\\\": 7, \\\"offset\\\": [5, 6], \\\"id\\\": \\\"1fa7be25e8d6cfdaa701e4faff6aaf04\\\"}, {\\\"trigger_word\\\": \\\"year\\\", \\\"sent_id\\\": 7, \\\"offset\\\": [7, 8], \\\"id\\\": \\\"0b6b3b5ffe96525ec20926b34efa6f8f\\\"}, {\\\"trigger_word\\\": \\\"festival\\\", \\\"sent_id\\\": 7, \\\"offset\\\": [9, 10], \\\"id\\\": \\\"4f1be9099ab965288152ab911066dae6\\\"}, {\\\"trigger_word\\\": \\\"Subsonic\\\", \\\"sent_id\\\": 7, \\\"offset\\\": [12, 13], \\\"id\\\": \\\"d065886fb8cf6ff0b96bd0255974b324\\\"}, {\\\"trigger_word\\\": \\\"gradually\\\", \\\"sent_id\\\": 7, \\\"offset\\\": [14, 15], \\\"id\\\": \\\"9630c6879dd41dae78658f9ffbfcf905\\\"}, {\\\"trigger_word\\\": \\\"house\\\", \\\"sent_id\\\": 7, \\\"offset\\\": [16, 17], \\\"id\\\": \\\"007d0bc835fa777e4fdb494165b99e8b\\\"}, {\\\"trigger_word\\\": \\\"techno\\\", \\\"sent_id\\\": 7, \\\"offset\\\": [18, 19], \\\"id\\\": \\\"256b22dd902d8e4afc62cf686b915cff\\\"}, {\\\"trigger_word\\\": \\\"forms\\\", \\\"sent_id\\\": 7, \\\"offset\\\": [21, 22], \\\"id\\\": \\\"11ff9aa96ac41cd9c321908eb1d3e641\\\"}, {\\\"trigger_word\\\": \\\"dance\\\", \\\"sent_id\\\": 7, \\\"offset\\\": [23, 24], \\\"id\\\": \\\"cb7c64c018b6ca2c678a8cc5da67298f\\\"}, {\\\"trigger_word\\\": \\\"music\\\", \\\"sent_id\\\": 7, \\\"offset\\\": [24, 25], \\\"id\\\": \\\"837273da461725123bbaf77606d6f1c7\\\"}, {\\\"trigger_word\\\": \\\"original\\\", \\\"sent_id\\\": 7, \\\"offset\\\": [27, 28], \\\"id\\\": \\\"cf0b71ab4eccfc27d8a23272a154bb49\\\"}, {\\\"trigger_word\\\": \\\"staples\\\", \\\"sent_id\\\": 7, \\\"offset\\\": [28, 29], \\\"id\\\": \\\"148ea27d529cb446e0834b47e738e970\\\"}, {\\\"trigger_word\\\": \\\"psytrance\\\", \\\"sent_id\\\": 7, \\\"offset\\\": [30, 31], \\\"id\\\": \\\"3088d0103a7b9e170c8e28bcb5736a57\\\"}, {\\\"trigger_word\\\": \\\"dub\\\", \\\"sent_id\\\": 7, \\\"offset\\\": [32, 33], \\\"id\\\": \\\"ac8701fb75f00ebb88e829a7cb93d5e4\\\"}, {\\\"trigger_word\\\": \\\"Resident\\\", \\\"sent_id\\\": 8, \\\"offset\\\": [1, 2], \\\"id\\\": \\\"9a5f1cc491e5a22e931cc66f7b15eb72\\\"}, {\\\"trigger_word\\\": \\\"Advisor\\\", \\\"sent_id\\\": 8, \\\"offset\\\": [2, 3], \\\"id\\\": \\\"20045a777351d2e293d49408f8b2c4b3\\\"}, {\\\"trigger_word\\\": \\\"also\\\", \\\"sent_id\\\": 8, \\\"offset\\\": [4, 5], \\\"id\\\": \\\"095344835171bb180ac01a395a355a7b\\\"}, {\\\"trigger_word\\\": \\\"Subsonic\\\", \\\"sent_id\\\": 8, \\\"offset\\\": [6, 7], \\\"id\\\": \\\"2aabb064c0655bd2620a34e47b740cd9\\\"}, {\\\"trigger_word\\\": \\\"Top\\\", \\\"sent_id\\\": 8, \\\"offset\\\": [9, 10], \\\"id\\\": \\\"e1fe3b56d276fee2884fdbf3270bc5b4\\\"}, {\\\"trigger_word\\\": \\\"November\\\", \\\"sent_id\\\": 8, \\\"offset\\\": [11, 12], \\\"id\\\": \\\"b08747a5aeaf3bd3217a32e9f7b7148b\\\"}, {\\\"trigger_word\\\": \\\"/\\\", \\\"sent_id\\\": 8, \\\"offset\\\": [12, 13], \\\"id\\\": \\\"9781cf12c2a1e0df26e61be8c4197742\\\"}, {\\\"trigger_word\\\": \\\"December\\\", \\\"sent_id\\\": 8, \\\"offset\\\": [13, 14], \\\"id\\\": \\\"82860fedf6d183928fd0b70cbe38bafb\\\"}, {\\\"trigger_word\\\": \\\"Festivals\\\", \\\"sent_id\\\": 8, \\\"offset\\\": [15, 16], \\\"id\\\": \\\"d8517e67fc994e75b31adc48280474d9\\\"}, {\\\"trigger_word\\\": \\\"world\\\", \\\"sent_id\\\": 8, \\\"offset\\\": [20, 21], \\\"id\\\": \\\"7c6600f9ff3be8268ad966d93a6d353a\\\"}]}\\n/root/schema-dag-extraction/data/fewrel/train_wiki.json:1:{\\\"P931\\\": [{\\\"tokens\\\": [\\\"Merpati\\\", \\\"flight\\\", \\\"106\\\", \\\"departed\\\", \\\"Jakarta\\\", \\\"(\\\", \\\"CGK\\\", \\\")\\\", \\\"on\\\", \\\"a\\\", \\\"domestic\\\", \\\"flight\\\", \\\"to\\\", \\\"Tanjung\\\", \\\"Pandan\\\", \\\"(\\\", \\\"TJQ\\\", \\\")\\\", \\\".\\\"], \\\"h\\\": [\\\"tjq\\\", \\\"Q1331049\\\", [[16]]], \\\"t\\\": [\\\"tanjung pandan\\\", \\\"Q3056359\\\", [[13, 14]]]}, {\\\"tokens\\\": [\\\"The\\\", \\\"name\\\", \\\"was\\\", \\\"at\\\", \\\"one\\\", \\\"point\\\", \\\"changed\\\", \\\"to\\\", \\\"Nottingham\\\", \\\"East\\\", \\\"Midlands\\\", \\\"Airport\\\", \\\"so\\\", \\\"as\\\", \\\"to\\\", \\\"include\\\", \\\"the\\\", \\\"name\\\", \\\"of\\\", \\\"the\\\", \\\"city\\\", \\\"that\\\", \\\"is\\\", \\\"supposedly\\\", \\\"most\\\", \\\"internationally\\\", \\\"recognisable\\\", \\\",\\\", \\\"mainly\\\", \\\"due\\\", \\\"to\\\", \\\"the\\\", \\\"Robin\\\", \\\"Hood\\\", \\\"legend\\\", \\\".\\\"], \\\"h\\\": [\\\"east midlands airport\\\", \\\"Q8977\\\", [[9, 10, 11]]], \\\"t\\\": [\\\"nottingham\\\", \\\"Q41262\\\", [[8]]]}, {\\\"tokens\\\": [\\\"It\\\", \\\"is\\\", \\\"a\\\", \\\"four\\\", \\\"-\\\", \\\"level\\\", \\\"stack\\\", \\\"interchange\\\", \\\"near\\\", \\\"Fort\\\", \\\"Lauderdale\\\", \\\"-\\\", \\\"Hollywood\\\", \\\"International\\\", \\\"Airport\\\", \\\"in\\\", \\\"Fort\\\", \\\"Lauderdale\\\", \\\",\\\", \\\"Florida\\\", \\\".\\\"], \\\"h\\\": [\\\"fort lauderdale-hollywood international airport\\\", \\\"Q635361\\\", [[9, 10, 11, 12, 13, 14]]], \\\"t\\\": [\\\"fort lauderdale, florida\\\", \\\"Q165972\\\", [[16, 17, 18, 19]]]}, {\\\"tokens\\\": [\\\"It\\\", \\\"is\\\", \\\"the\\\", \\\"main\\\", \\\"alternate\\\", \\\"of\\\", \\\"Jinnah\\\", \\\"International\\\", \\\"Airport\\\", \\\"in\\\", \\\"Karachi\\\", \\\"with\\\", \\\"a\\\", \\\"distance\\\", \\\"of\\\", \\\"about\\\", \\\"350\\\", \\\"\\\\u00a0\\\", \\\"km/220\\\", \\\"miles\\\", \\\";\\\", \\\"well\\\", \\\"under\\\", \\\"an\\\", \\\"hour\\\", \\\"'s\\\", \\\"flight\\\", \\\"time\\\", \\\"in\\\", \\\"turboprop\\\", \\\"aircraft\\\", \\\".\\\"], \\\"h\\\": [\\\"jinnah international airport\\\", \\\"Q61052\\\", [[6, 7, 8]]], \\\"t\\\": [\\\"karachi\\\", \\\"Q8660\\\", [[10]]]}, {\\\"tokens\\\": [\\\"Nearby\\\", \\\"airports\\\", \\\"include\\\", \\\"Akwa\\\", \\\"Ibom\\\", \\\"Airport\\\", \\\"at\\\", \\\"Okobo\\\", \\\"and\\\", \\\"Margaret\\\", \\\"Ekpo\\\", \\\"International\\\", \\\"Airport\\\", \\\"in\\\", \\\"Calabar\\\", \\\".\\\"], \\\"h\\\": [\\\"margaret ekpo international airport\\\", \\\"Q1030578\\\", [[9, 10, 11, 12]]], \\\"t\\\": [\\\"calabar\\\", \\\"Q844091\\\", [[14]]]}, {\\\"tokens\\\": [\\\"Pakyong\\\", \\\"Airport\\\", \\\",\\\", \\\"a\\\", \\\"Greenfield\\\", \\\"project\\\", \\\",\\\", \\\"is\\\", \\\"under\\\", \\\"construction\\\", \\\"southeast\\\", \\\"of\\\", \\\"Gangtok\\\", \\\".\\\"], \\\"h\\\": [\\\"pakyong airport\\\", \\\"Q7126092\\\", [[0, 1]]], \\\"t\\\": [\\\"gangtok\\\", \\\"Q186141\\\", [[12]]]}, {\\\"tokens\\\": [\\\"Its\\\", \\\"hub\\\", \\\"is\\\", \\\"Tinson\\\", \\\"Pen\\\", \\\"Aerodrome\\\", \\\"in\\\", \\\"Kingston\\\", \\\"(\\\", \\\"KTP\\\", \\\")\\\", \\\",\\\", \\\"and\\\", \\\"its\\\", \\\"other\\\", \\\"major\\\", \\\"gateway\\\", \\\"was\\\", \\\"Sangster\\\", \\\"International\\\", \\\"Airport\\\", \\\"in\\\", \\\"Montego\\\", \\\"Bay\\\", \\\"(\\\", \\\"MBJ\\\", \\\")\\\", \\\".\\\"], \\\"h\\\": [\\\"tinson pen aerodrome\\\", \\\"Q2320308\\\", [[3, 4, 5]]], \\\"t\\\": [\\\"kingston\\\", \\\"Q34692\\\", [[7]]]}, {\\\"tokens\\\": [\\\"He\\\", \\\"has\\\", \\\"postage\\\", \\\"stamps\\\", \\\"issued\\\", \\\"in\\\", \\\"his\\\", \\\"honour\\\", \\\"and\\\", \\\"Noum\\\\u00e9rat\\\", \\\"\\\\u2013\\\", \\\"Moufdi\\\", \\\"Zakaria\\\", \\\"Airport\\\", \\\"in\\\", \\\"Gharda\\\\u00efa\\\", \\\",\\\", \\\"Algeria\\\", \\\"is\\\", \\\"named\\\", \\\"in\\\", \\\"his\\\", \\\"honour\\\", \\\".\\\"], \\\"h\\\": [\\\"noum\\\\u00e9rat \\\\u2013 moufdi zakaria airport\\\", \\\"Q1432199\\\", [[9, 10, 11, 12, 13]]], \\\"t\\\": [\\\"gharda\\\\u00efa\\\", \\\"Q622841\\\", [[15]]]}, {\\\"tokens\\\": [\\\"By\\\", \\\"Airway\\\", \\\";\\\", \\\"\\\\n\\\", \\\"Nearest\\\", \\\"airport\\\", \\\"is\\\", \\\"Kazi\\\", \\\"Nazrul\\\", \\\"Islam\\\", \\\"Airport\\\", \\\",\\\", \\\"Durgapur\\\", \\\"(\\\", \\\"RDP\\\", \\\")\\\", \\\"West\\\", \\\"Bengal\\\", \\\"and\\\", \\\"1\\\", \\\"hour\\\", \\\"drive\\\", \\\"from\\\", \\\"airport\\\", \\\".\\\"], \\\"h\\\": [\\\"kazi nazrul islam airport\\\", \\\"Q14941562\\\", [[7, 8, 9, 10]]], \\\"t\\\": [\\\"durgapur\\\", \\\"Q5088\\\", [[12]]]}, {\\\"tokens\\\": [\\\"The\\\", \\\"nearest\\\", \\\"airport\\\", \\\"is\\\", \\\"Robin\\\", \\\"Hood\\\", \\\"Airport\\\", \\\"at\\\", \\\"Doncaster\\\", \\\"and\\\", \\\"the\\\", \\\"nearest\\\", \\\"train\\\", \\\"and\\\", \\\"bus\\\", \\\"stations\\\", \\\"are\\\", \\\"in\\\", \\\"Chesterfield\\\", \\\".\\\"], \\\"h\\\": [\\\"robin hood airport\\\", \\\"Q8996\\\", [[4, 5, 6]]], \\\"t\\\": [\\\"doncaster\\\", \\\"Q58900\\\", [[8]]]}, {\\\"tokens\\\": [\\\"Manchester\\\", \\\"boasts\\\", \\\"a\\\", \\\"large\\\", \\\"regional\\\", \\\"airport\\\", \\\",\\\", \\\"with\\\", \\\"scheduled\\\", \\\"commercial\\\", \\\"services\\\", \\\".\\\"], \\\"h\\\": [\\\"large regional airport\\\", \\\"Q180129\\\", [[3, 4, 5]]], \\\"t\\\": [\\\"manchester\\\", \\\"Q48370\\\", [[0]]]}, {\\\"tokens\\\": [\\\"Route\\\", \\\"41\\\", \\\"ends\\\", \\\"just\\\", \\\"north\\\", \\\"of\\\", \\\"the\\\", \\\"Richmond\\\", \\\"-\\\", \\\"Pittsfield\\\", \\\"line\\\", \\\"at\\\", \\\"U.S.\\\", \\\"Route\\\", \\\"20\\\", \\\",\\\", \\\"just\\\", \\\"east\\\", \\\"of\\\", \\\"the\\\", \\\"Hancock\\\", \\\"Shaker\\\", \\\"Village\\\", \\\"in\\\", \\\"Hancock\\\", \\\"and\\\", \\\"southwest\\\", \\\"of\\\", \\\"Pittsfield\\\", \\\"'s\\\", \\\"airport\\\", \\\"and\\\", \\\"city\\\", \\\"center\\\", \\\".\\\"], \\\"h\\\": [\\\"airport\\\", \\\"Q7199486\\\", [[30]]], \\\"t\\\": [\\\"pittsfield\\\", \\\"Q49184\\\", [[9], [28]]]}, {\\\"tokens\\\": [\\\"Casilda\\\", \\\"is\\\", \\\"the\\\", \\\"southern\\\", \\\"terminus\\\", \\\"of\\\", \\\"the\\\", \\\"railway\\\", \\\"line\\\", \\\"which\\\", \\\"links\\\", \\\"Placetas\\\", \\\"and\\\", \\\"Fomento\\\", \\\"to\\\", \\\"Trinidad\\\", \\\",\\\", \\\"has\\\", \\\"a\\\", \\\"small\\\", \\\"harbor\\\", \\\",\\\", \\\"and\\\", \\\"is\\\", \\\"4\\\", \\\"km\\\", \\\"from\\\", \\\"Alberto\\\", \\\"Delgado\\\", \\\"Airport\\\", \\\".\\\"], \\\"h\\\": [\\\"alberto delgado airport\\\", \\\"Q4711997\\\", [[27, 28, 29]]], \\\"t\\\": [\\\"trinidad\\\", \\\"Q319272\\\", [[15]]]}, {\\\"tokens\\\": [\\\"Aeropark\\\", \\\"is\\\", \\\"an\\\", \\\"open\\\", \\\"-\\\", \\\"air\\\", \\\"aviation\\\", \\\"museum\\\", \\\"next\\\", \\\"to\\\", \\\"Ferenc\\\", \\\"Liszt\\\", \\\"International\\\", \\\"Airport\\\", \\\",\\\", \\\"Budapest\\\", \\\",\\\", \\\"Hungary\\\", \\\".\\\"], \\\"h\\\": [\\\"ferenc liszt international airport\\\", \\\"Q500945\\\", [[10, 11, 12, 13]]], \\\"t\\\": [\\\"budapest\\\", \\\"Q1781\\\", [[15]]]}, {\\\"tokens\\\": [\\\"The\\\", \\\"nearest\\\", \\\"airport\\\", \\\"is\\\", \\\"the\\\", \\\"Menominee\\\", \\\"-\\\", \\\"Marinette\\\", \\\"Twin\\\", \\\"County\\\", \\\"Airport\\\", \\\"in\\\", \\\"Menominee\\\", \\\",\\\", \\\"Michigan\\\", \\\".\\\"], \\\"h\\\": [\\\"menominee-marinette twin county airport\\\", \\\"Q27308800\\\", [[5, 6, 7, 8, 9, 10]]], \\\"t\\\": [\\\"menominee, michigan\\\", \\\"Q2635319\\\", [[12, 13, 14]]]}, {\\\"tokens\\\": [\\\"Peshawar\\\", \\\"'s\\\", \\\"Bacha\\\", \\\"Khan\\\", \\\"International\\\", \\\"Airport\\\", \\\"is\\\", \\\"155\\\", \\\"kilometres\\\", \\\"away\\\", \\\"by\\\", \\\"road\\\", \\\".\\\"], \\\"h\\\": [\\\"bacha khan international airport\\\", \\\"Q1516769\\\", [[2, 3, 4, 5]]], \\\"t\\\": [\\\"peshawar\\\", \\\"Q1113311\\\", [[0]]]}, {\\\"tokens\\\": [\\\"Currently\\\", \\\"it\\\", \\\"is\\\", \\\"the\\\", \\\"second\\\", \\\"largest\\\", \\\"airport\\\", \\\"in\\\", \\\"Kalimantan\\\", \\\"in\\\", \\\"terms\\\", \\\"of\\\", \\\"terminal\\\", \\\"size\\\", \\\",\\\", \\\"after\\\", \\\"Sultan\\\", \\\"Aji\\\", \\\"Muhammad\\\", \\\"Sulaiman\\\", \\\"Airport\\\", \\\"in\\\", \\\"Balikpapan\\\", \\\".\\\"], \\\"h\\\": [\\\"sultan aji muhammad sulaiman airport\\\", \\\"Q263652\\\", [[16, 17, 18, 19, 20]]], \\\"t\\\": [\\\"balikpapan\\\", \\\"Q14492\\\", [[22]]]}, {\\\"tokens\\\": [\\\"Presidente\\\", \\\"M\\\\u00e9dici\\\", \\\"International\\\", \\\"Airport\\\", \\\",\\\", \\\"formerly\\\", \\\",\\\", \\\"was\\\", \\\"the\\\", \\\"airport\\\", \\\"that\\\", \\\"served\\\", \\\"Rio\\\", \\\"Branco\\\", \\\",\\\", \\\"Brazil\\\", \\\"until\\\", \\\"1999\\\", \\\",\\\", \\\"when\\\", \\\"Pl\\\\u00e1cido\\\", \\\"de\\\", \\\"Castro\\\", \\\"International\\\", \\\"Airport\\\", \\\"was\\\", \\\"opened\\\", \\\".\\\"], \\\"h\\\": [\\\"presidente m\\\\u00e9dici international airport\\\", \\\"Q6587048\\\", [[0, 1, 2, 3]]], \\\"t\\\": [\\\"rio branco\\\", \\\"Q171612\\\", [[12, 13]]]}, {\\\"tokens\\\": [\\\"Temple\\\", \\\"Bar\\\", \\\"Marina\\\", \\\"has\\\", \\\"its\\\", \\\"own\\\", \\\"post\\\", \\\"office\\\", \\\"with\\\", \\\"ZIP\\\", \\\"code\\\", \\\"86443.ZIP\\\", \\\"Code\\\", \\\"Lookup\\\", \\\"Temple\\\", \\\"Bar\\\", \\\"Airport\\\", \\\"is\\\", \\\"located\\\", \\\"near\\\", \\\"the\\\", \\\"marina\\\", \\\".\\\"], \\\"h\\\": [\\\"temple bar airport\\\", \\\"Q6588459\\\", [[14, 15, 16]]], \\\"t\\\": [\\\"temple bar marina\\\", \\\"Q7698447\\\", [[0, 1, 2]]]}, {\\\"tokens\\\": [\\\"Bishop\\\", \\\"International\\\", \\\"Airport\\\", \\\"in\\\", \\\"Flint\\\", \\\"and\\\", \\\"Toledo\\\", \\\"Express\\\", \\\"Airport\\\", \\\"in\\\", \\\"Toledo\\\", \\\",\\\", \\\"Ohio\\\", \\\"are\\\", \\\"other\\\", \\\"commercial\\\", \\\"passenger\\\", \\\"airports\\\", \\\".\\\"], \\\"h\\\": [\\\"toledo express airport\\\", \\\"Q6588637\\\", [[6, 7, 8]]], \\\"t\\\": [\\\"toledo, ohio\\\", \\\"Q49239\\\", [[10, 11, 12]]]}, {\\\"tokens\\\": [\\\"Greenbrier\\\", \\\"Valley\\\", \\\"Airport\\\", \\\"is\\\", \\\"a\\\", \\\"single\\\", \\\"runway\\\", \\\"airport\\\", \\\"3\\\", \\\"miles\\\", \\\"north\\\", \\\"of\\\", \\\"Lewisburg\\\", \\\",\\\", \\\"West\\\", \\\"Virginia\\\", \\\".\\\"], \\\"h\\\": [\\\"greenbrier valley airport\\\", \\\"Q3914326\\\", [[0, 1, 2]]], \\\"t\\\": [\\\"lewisburg, west virginia\\\", \\\"Q731071\\\", [[12, 13, 14, 15]]]}, {\\\"tokens\\\": [\\\"The\\\", \\\"international\\\", \\\"airport\\\", \\\"of\\\", \\\"Chania\\\", \\\"(\\\", \\\"CHQ\\\", \\\"/\\\", \\\"LGSA\\\", \\\")\\\", \\\"bears\\\", \\\"Daskalogiannis\\\", \\\"'\\\", \\\"name\\\", \\\".\\\", \\\"Ioannis\\\", \\\"Daskalogiannis\\\", \\\"International\\\", \\\"Airport\\\", \\\"A\\\", \\\"memorial\\\", \\\"statue\\\", \\\"can\\\", \\\"be\\\", \\\"seen\\\", \\\"in\\\", \\\"his\\\", \\\"hometown\\\", \\\"Anopolis\\\", \\\".\\\"], \\\"h\\\": [\\\"international airport\\\", \\\"Q1232348\\\", [[1, 2], [17, 18]]], \\\"t\\\": [\\\"chania\\\", \\\"Q182299\\\", [[4]]]}, {\\\"tokens\\\": [\\\"2\\\", \\\"\\\\u2013\\\", \\\"30\\\", \\\"days\\\", \\\",\\\", \\\"also\\\", \\\"available\\\", \\\"at\\\", \\\"Gurney\\\", \\\"Airport\\\", \\\"(\\\", \\\"Alotau\\\", \\\")\\\", \\\"and\\\", \\\"Mount\\\", \\\"Hagen\\\", \\\"Airport\\\", \\\".\\\"], \\\"h\\\": [\\\"gurney airport\\\", \\\"Q1069088\\\", [[8, 9]]], \\\"t\\\": [\\\"alotau\\\", \\\"Q568137\\\", [[11]]]}, {\\\"tokens\\\": [\\\"They\\\", \\\"are\\\", \\\"still\\\", \\\"deployed\\\", \\\"at\\\", \\\"Kisangani\\\", \\\"'s\\\", \\\"Bangoka\\\", \\\"airport\\\", \\\",\\\", \\\"where\\\", \\\"they\\\", \\\"appear\\\", \\\"to\\\", \\\"answer\\\", \\\"to\\\", \\\"no\\\", \\\"local\\\", \\\"commander\\\", \\\"and\\\", \\\"have\\\", \\\"caused\\\", \\\"trouble\\\", \\\"with\\\", \\\"MONUC\\\", \\\"troops\\\", \\\"there\\\", \\\".\\\"], \\\"h\\\": [\\\"bangoka airport\\\", \\\"Q27596\\\", [[7, 8]]], \\\"t\\\": [\\\"kisangani\\\", \\\"Q146723\\\", [[5]]]}, {\\\"tokens\\\": [\\\"The\\\", \\\"airline\\\", \\\"is\\\", \\\"based\\\", \\\"at\\\", \\\"Alexandria\\\", \\\"'s\\\", \\\"Borg\\\", \\\"El\\\", \\\"Arab\\\", \\\"Airport\\\", \\\".\\\"], \\\"h\\\": [\\\"borg el arab airport\\\", \\\"Q1194015\\\", [[7, 8, 9, 10]]], \\\"t\\\": [\\\"alexandria\\\", \\\"Q87\\\", [[5]]]}, {\\\"tokens\\\": [\\\"LIFESTAR\\\", \\\"2\\\", \\\"is\\\", \\\"based\\\", \\\"in\\\", \\\"Rockwood\\\", \\\",\\\", \\\"Tennessee\\\", \\\"at\\\", \\\"the\\\", \\\"Rockwood\\\", \\\"Municipal\\\", \\\"Airport\\\", \\\".\\\"], \\\"h\\\": [\\\"rockwood municipal airport\\\", \\\"Q10851312\\\", [[10, 11, 12]]], \\\"t\\\": [\\\"rockwood, tennessee\\\", \\\"Q979056\\\", [[5, 6, 7]]]}, {\\\"tokens\\\": [\\\"Bluffton\\\", \\\"is\\\", \\\"served\\\", \\\"by\\\", \\\"the\\\", \\\"Savannah\\\", \\\"/\\\", \\\"Hilton\\\", \\\"Head\\\", \\\"International\\\", \\\"Airport\\\", \\\",\\\", \\\"which\\\", \\\"is\\\", \\\"located\\\", \\\"in\\\", \\\"Savannah\\\", \\\",\\\", \\\"Georgia\\\", \\\",\\\", \\\"and\\\", \\\"the\\\", \\\"Hilton\\\", \\\"Head\\\", \\\"Island\\\", \\\"Airport\\\", \\\".\\\"], \\\"h\\\": [\\\"savannah/hilton head international airport\\\", \\\"Q1432789\\\", [[5, 6, 7, 8, 9, 10]]], \\\"t\\\": [\\\"savannah, georgia\\\", \\\"Q83813\\\", [[16, 17, 18]]]}, {\\\"tokens\\\": [\\\"Air\\\", \\\"Costa\\\", \\\"Rica\\\", \\\"is\\\", \\\"a\\\", \\\"planned\\\", \\\"airline\\\", \\\"based\\\", \\\"in\\\", \\\"Juan\\\", \\\"Santamar\\\\u00eda\\\", \\\"International\\\", \\\"Airport\\\", \\\",\\\", \\\"San\\\", \\\"Jos\\\\u00e9\\\", \\\",\\\", \\\"Costa\\\", \\\"Rica\\\", \\\".\\\"], \\\"h\\\": [\\\"juan santamar\\\\u00eda international airport\\\", \\\"Q555940\\\", [[9, 10, 11, 12]]], \\\"t\\\": [\\\"san jos\\\\u00e9\\\", \\\"Q3070\\\", [[14, 15]]]}, {\\\"tokens\\\": [\\\"The\\\", \\\"Djibouti\\\", \\\"\\\\u2013\\\", \\\"Ambouli\\\", \\\"International\\\", \\\"Airport\\\", \\\",\\\", \\\"the\\\", \\\"country\\\", \\\"'s\\\", \\\"only\\\", \\\"international\\\", \\\"airport\\\", \\\"in\\\", \\\"Djibouti\\\", \\\"City\\\", \\\"serves\\\", \\\"many\\\", \\\"intercontinental\\\", \\\"routes\\\", \\\"with\\\", \\\"scheduled\\\", \\\"and\\\", \\\"chartered\\\", \\\"flights\\\", \\\".\\\"], \\\"h\\\": [\\\"djibouti\\\\u2013ambouli international airport\\\", \\\"Q620706\\\", [[1, 2, 3, 4, 5]]], \\\"t\\\": [\\\"djibouti city\\\", \\\"Q3604\\\", [[14, 15]]]}, {\\\"tokens\\\": [\\\"An\\\", \\\"ASOS\\\", \\\"station\\\", \\\"was\\\", \\\"install\\\", \\\"at\\\", \\\"the\\\", \\\"Magic\\\", \\\"Valley\\\", \\\"Regional\\\", \\\"Airport\\\", \\\"south\\\", \\\"of\\\", \\\"Twin\\\", \\\"Falls\\\", \\\",\\\", \\\"Idaho\\\", \\\"on\\\", \\\"January\\\", \\\"28\\\", \\\",\\\", \\\"1997\\\", \\\".\\\"], \\\"h\\\": [\\\"magic valley regional airport\\\", \\\"Q6730879\\\", [[7, 8, 9, 10]]], \\\"t\\\": [\\\"twin falls, idaho\\\", \\\"Q548384\\\", [[13, 14, 15, 16]]]}, {\\\"tokens\\\": [\\\"Abernathy\\\", \\\"Field\\\", \\\"is\\\", \\\"a\\\", \\\"public\\\", \\\"use\\\", \\\"airport\\\", \\\"owned\\\", \\\"by\\\", \\\"Giles\\\", \\\"County\\\", \\\"and\\\", \\\"the\\\", \\\"City\\\", \\\"of\\\", \\\"Pulaski\\\", \\\".\\\"], \\\"h\\\": [\\\"abernathy field\\\", \\\"Q428353\\\", [[0, 1]]], \\\"t\\\": [\\\"city of pulaski\\\", \\\"Q1410885\\\", [[13, 14, 15]]]}, {\\\"tokens\\\": [\\\"He\\\", \\\"died\\\", \\\"at\\\", \\\"43\\\", \\\"from\\\", \\\"injuries\\\", \\\"suffered\\\", \\\"in\\\", \\\"crash\\\", \\\"while\\\", \\\"piloting\\\", \\\"an\\\", \\\"ultralight\\\", \\\"aircraft\\\", \\\",\\\", \\\"soon\\\", \\\"after\\\", \\\"taking\\\", \\\"off\\\", \\\"from\\\", \\\"the\\\", \\\"Tuscola\\\", \\\"Area\\\", \\\"Airport\\\", \\\"near\\\", \\\"Caro\\\", \\\",\\\", \\\"Michigan\\\", \\\".\\\"], \\\"h\\\": [\\\"tuscola area airport\\\", \\\"Q7856724\\\", [[21, 22, 23]]], \\\"t\\\": [\\\"caro, michigan\\\", \\\"Q14032\\\", [[25, 26, 27]]]}, {\\\"tokens\\\": [\\\"The\\\", \\\"nearest\\\", \\\"airport\\\", \\\"is\\\", \\\"Raja\\\", \\\"Bhoj\\\", \\\"Airport\\\", \\\"Bhopal\\\", \\\".\\\"], \\\"h\\\": [\\\"raja bhoj airport\\\", \\\"Q7285421\\\", [[4, 5, 6]]], \\\"t\\\": [\\\"bhopal\\\", \\\"Q80989\\\", [[7]]]}, {\\\"tokens\\\": [\\\"The\\\", \\\"airline\\\", \\\"'s\\\", \\\"hub\\\", \\\"is\\\", \\\"Maya\\\", \\\"-\\\", \\\"Maya\\\", \\\"Airport\\\", \\\",\\\", \\\"in\\\", \\\"Brazzaville\\\", \\\".\\\"], \\\"h\\\": [\\\"maya-maya airport\\\", \\\"Q644963\\\", [[5, 6, 7, 8]]], \\\"t\\\": [\\\"brazzaville\\\", \\\"Q3844\\\", [[11]]]}, {\\\"tokens\\\": [\\\"In\\\", \\\"1954\\\", \\\"USAF\\\", \\\"C-124\\\", \\\"transports\\\", \\\"assisted\\\", \\\"the\\\", \\\"French\\\", \\\"by\\\", \\\"airlifting\\\", \\\"500\\\", \\\"paratroop\\\", \\\"/\\\", \\\"commandos\\\", \\\"and\\\", \\\"their\\\", \\\"equipment\\\", \\\"to\\\", \\\"Indochina\\\", \\\",\\\", \\\"landing\\\", \\\"at\\\", \\\"Da\\\", \\\"Nang\\\", \\\"'s\\\", \\\"Tourane\\\", \\\"Airfield\\\", \\\".\\\"], \\\"h\\\": [\\\"tourane airfield\\\", \\\"Q773330\\\", [[25, 26]]], \\\"t\\\": [\\\"da nang\\\", \\\"Q25282\\\", [[22, 23]]]}, {\\\"tokens\\\": [\\\"The\\\", \\\"other\\\", \\\"airports\\\", \\\"in\\\", \\\"Tibet\\\", \\\"are\\\", \\\"Lhasa\\\", \\\"Gonggar\\\", \\\"Airport\\\", \\\"in\\\", \\\"Lhasa\\\", \\\",\\\", \\\"Qamdo\\\", \\\"Bamda\\\", \\\"Airport\\\", \\\"in\\\", \\\"Chamdo\\\", \\\"and\\\", \\\"Nyingchi\\\", \\\"Mainling\\\", \\\"Airport\\\", \\\".\\\"], \\\"h\\\": [\\\"qamdo bamda airport\\\", \\\"Q531800\\\", [[12, 13, 14]]], \\\"t\\\": [\\\"chamdo\\\", \\\"Q1012419\\\", [[16]]]}, {\\\"tokens\\\": [\\\"After\\\", \\\"successfully\\\", \\\"transporting\\\", \\\"the\\\", \\\"patient\\\", \\\"from\\\", \\\"Tingwall\\\", \\\"Airport\\\", \\\"in\\\", \\\"the\\\", \\\"Shetland\\\", \\\"Islands\\\", \\\"to\\\", \\\"Inverness\\\", \\\",\\\", \\\"the\\\", \\\"pilot\\\", \\\",\\\", \\\"nurse\\\", \\\",\\\", \\\"and\\\", \\\"physician\\\", \\\"were\\\", \\\"returning\\\", \\\"to\\\", \\\"their\\\", \\\"home\\\", \\\"base\\\", \\\"in\\\", \\\"Tingwall\\\", \\\".\\\"], \\\"h\\\": [\\\"tingwall airport\\\", \\\"Q2875973\\\", [[6, 7]]], \\\"t\\\": [\\\"shetland islands\\\", \\\"Q47134\\\", [[10, 11]]]}, {\\\"tokens\\\": [\\\"It\\\", \\\"is\\\", \\\"by\\\", \\\"State\\\", \\\"Highway\\\", \\\"947\\\", \\\"from\\\", \\\"Jamnagar\\\", \\\",\\\", \\\"where\\\", \\\"there\\\", \\\"is\\\", \\\"a\\\", \\\"domestic\\\", \\\"airport\\\", \\\".\\\"], \\\"h\\\": [\\\"domestic airport\\\", \\\"Q1595059\\\", [[13, 14]]], \\\"t\\\": [\\\"jamnagar\\\", \\\"Q1154\\\", [[7]]]}, {\\\"tokens\\\": [\\\"Diori\\\", \\\"Hamani\\\", \\\"International\\\", \\\"Airport\\\", \\\"is\\\", \\\"an\\\", \\\"airport\\\", \\\"in\\\", \\\"Niamey\\\", \\\",\\\", \\\"the\\\", \\\"capital\\\", \\\"of\\\", \\\"Niger\\\", \\\".\\\"], \\\"h\\\": [\\\"diori hamani international airport\\\", \\\"Q905933\\\", [[0, 1, 2, 3]]], \\\"t\\\": [\\\"niamey\\\", \\\"Q3674\\\", [[8]]]}, {\\\"tokens\\\": [\\\"The\\\", \\\"Quad\\\", \\\"City\\\", \\\"Airshow\\\", \\\"is\\\", \\\"an\\\", \\\"annual\\\", \\\"event\\\", \\\"at\\\", \\\"the\\\", \\\"Davenport\\\", \\\"Municipal\\\", \\\"Airport\\\", \\\"in\\\", \\\"Davenport\\\", \\\",\\\", \\\"Iowa\\\", \\\"and\\\", \\\"was\\\", \\\"the\\\", \\\"largest\\\", \\\"airshow\\\", \\\"in\\\", \\\"the\\\", \\\"state\\\", \\\"of\\\", \\\"Iowa\\\", \\\".\\\"], \\\"h\\\": [\\\"davenport municipal airport\\\", \\\"Q1707887\\\", [[10, 11, 12]]], \\\"t\\\": [\\\"davenport, iowa\\\", \\\"Q26887\\\", [[14, 15, 16]]]}, {\\\"tokens\\\": [\\\"In\\\", \\\"1912\\\", \\\",\\\", \\\"Bell\\\", \\\"flew\\\", \\\"the\\\", \\\"first\\\", \\\"recorded\\\", \\\"flight\\\", \\\"into\\\", \\\"Billings\\\", \\\"Logan\\\", \\\"International\\\", \\\"Airport\\\", \\\"in\\\", \\\"Billings\\\", \\\",\\\", \\\"Montana\\\", \\\".\\\"], \\\"h\\\": [\\\"billings logan international airport\\\", \\\"Q598269\\\", [[10, 11, 12, 13]]], \\\"t\\\": [\\\"billings, montana\\\", \\\"Q166304\\\", [[15, 16, 17]]]}, {\\\"tokens\\\": [\\\"Warsaw\\\", \\\"-\\\", \\\"Modlin\\\", \\\"Airport\\\", \\\"is\\\", \\\"located\\\", \\\"within\\\", \\\"the\\\", \\\"county\\\", \\\".\\\"], \\\"h\\\": [\\\"modlin airport\\\", \\\"Q1401995\\\", [[2, 3]]], \\\"t\\\": [\\\"warsaw\\\", \\\"Q270\\\", [[0]]]}, {\\\"tokens\\\": [\\\"Tom\\\\u00e1s\\\", \\\"de\\\", \\\"Heres\\\", \\\"Airport\\\", \\\"(\\\", \\\",\\\", \\\")\\\", \\\"is\\\", \\\"an\\\", \\\"airport\\\", \\\"serving\\\", \\\"Ciudad\\\", \\\"Bol\\\\u00edvar\\\", \\\",\\\", \\\"the\\\", \\\"capital\\\", \\\"of\\\", \\\"the\\\", \\\"Bol\\\\u00edvar\\\", \\\"state\\\", \\\"of\\\", \\\"Venezuela\\\", \\\".\\\"], \\\"h\\\": [\\\"tom\\\\u00e1s de heres airport\\\", \\\"Q1931117\\\", [[0, 1, 2, 3]]], \\\"t\\\": [\\\"ciudad bol\\\\u00edvar\\\", \\\"Q26906\\\", [[11, 12]]]}, {\\\"tokens\\\": [\\\"The\\\", \\\"Rockford\\\", \\\"Airfest\\\", \\\"was\\\", \\\"a\\\", \\\"two\\\", \\\"-\\\", \\\"day\\\", \\\"air\\\", \\\"show\\\", \\\"that\\\", \\\"happened\\\", \\\"every\\\", \\\"year\\\", \\\"at\\\", \\\"Chicago\\\", \\\"Rockford\\\", \\\"International\\\", \\\"Airport\\\", \\\"located\\\", \\\"in\\\", \\\"Rockford\\\", \\\",\\\", \\\"Illinois\\\", \\\",\\\", \\\"USA\\\", \\\".\\\"], \\\"h\\\": [\\\"chicago rockford international airport\\\", \\\"Q1071990\\\", [[15, 16, 17, 18]]], \\\"t\\\": [\\\"rockford, illinois\\\", \\\"Q233892\\\", [[21, 22, 23]]]}, {\\\"tokens\\\": [\\\"Yolo\\\", \\\"County\\\", \\\"Airport\\\", \\\"is\\\", \\\"six\\\", \\\"miles\\\", \\\"northeast\\\", \\\"of\\\", \\\"Winters\\\", \\\",\\\", \\\"five\\\", \\\"miles\\\", \\\"northwest\\\", \\\"of\\\", \\\"Davis\\\", \\\"and\\\", \\\"five\\\", \\\"miles\\\", \\\"southwest\\\", \\\"of\\\", \\\"Woodland\\\", \\\",\\\", \\\"all\\\", \\\"in\\\", \\\"Yolo\\\", \\\"County\\\", \\\",\\\", \\\"California\\\", \\\".\\\"], \\\"h\\\": [\\\"yolo county airport\\\", \\\"Q10853689\\\", [[0, 1, 2]]], \\\"t\\\": [\\\"davis\\\", \\\"Q668546\\\", [[14]]]}, {\\\"tokens\\\": [\\\"They\\\", \\\"are\\\", \\\"based\\\", \\\"at\\\", \\\"Newcastle\\\", \\\"Airport\\\", \\\",\\\", \\\"Tyne\\\", \\\"and\\\", \\\"Wear\\\", \\\",\\\", \\\"and\\\", \\\"at\\\", \\\"Carlisle\\\", \\\"Lake\\\", \\\"District\\\", \\\"Airport\\\", \\\",\\\", \\\"Cumbria\\\", \\\".\\\"], \\\"h\\\": [\\\"newcastle airport\\\", \\\"Q8975\\\", [[4, 5]]], \\\"t\\\": [\\\"tyne and wear\\\", \\\"Q23080\\\", [[7, 8, 9]]]}, {\\\"tokens\\\": [\\\"Noum\\\\u00e9a\\\", \\\"'s\\\", \\\"international\\\", \\\"airport\\\", \\\"is\\\", \\\"La\\\", \\\"Tontouta\\\", \\\"International\\\", \\\"Airport\\\", \\\",\\\", \\\"from\\\", \\\"the\\\", \\\"city\\\", \\\".\\\"], \\\"h\\\": [\\\"la tontouta international airport\\\", \\\"Q892783\\\", [[5, 6, 7, 8]]], \\\"t\\\": [\\\"noum\\\\u00e9a\\\", \\\"Q9733\\\", [[0]]]}, {\\\"tokens\\\": [\\\"Zvartnots\\\", \\\"International\\\", \\\"Airport\\\", \\\",\\\", \\\"Yerevan\\\", \\\"'s\\\", \\\"international\\\", \\\"airport\\\", \\\",\\\", \\\"is\\\", \\\"located\\\", \\\"near\\\", \\\"the\\\", \\\"town\\\", \\\"of\\\", \\\"Zvartnots\\\", \\\",\\\", \\\"as\\\", \\\"is\\\", \\\"the\\\", \\\"Zvartnots\\\", \\\"Cathedral\\\", \\\".\\\"], \\\"h\\\": [\\\"zvartnots international airport\\\", \\\"Q1124922\\\", [[0, 1, 2]]], \\\"t\\\": [\\\"yerevan\\\", \\\"Q1953\\\", [[4]]]}, {\\\"tokens\\\": [\\\"Mohawk\\\", \\\"Valley\\\", \\\"Airport\\\", \\\"is\\\", \\\"located\\\", \\\"three\\\", \\\"nautical\\\", \\\"miles\\\", \\\"(\\\", \\\"6\\\", \\\"\\\\u00a0\\\", \\\"km\\\", \\\")\\\", \\\"northwest\\\", \\\"of\\\", \\\"the\\\", \\\"central\\\", \\\"business\\\", \\\"district\\\", \\\"of\\\", \\\"Scotia\\\", \\\".\\\"], \\\"h\\\": [\\\"mohawk valley airport\\\", \\\"Q3565424\\\", [[0, 1, 2]]], \\\"t\\\": [\\\"scotia\\\", \\\"Q1020602\\\", [[20]]]}, {\\\"tokens\\\": [\\\"M-553\\\", \\\"connects\\\", \\\"Marquette\\\", \\\"with\\\", \\\"Sawyer\\\", \\\"International\\\", \\\"Airport\\\", \\\"at\\\", \\\"the\\\", \\\"unincorporated\\\", \\\"community\\\", \\\"of\\\", \\\"K.I.\\\"], \\\"h\\\": [\\\"sawyer international airport\\\", \\\"Q4568758\\\", [[4, 5, 6]]], \\\"t\\\": [\\\"marquette\\\", \\\"Q12443\\\", [[2]]]}, {\\\"tokens\\\": [\\\"Isiro\\\", \\\"is\\\", \\\"served\\\", \\\"by\\\", \\\"Matari\\\", \\\"Airport\\\", \\\",\\\", \\\"a\\\", \\\"national\\\", \\\"airport\\\", \\\"with\\\", \\\"flights\\\", \\\"to\\\", \\\"Kinshasa\\\", \\\",\\\", \\\"the\\\", \\\"capital\\\", \\\".\\\"], \\\"h\\\": [\\\"matari airport\\\", \\\"Q652383\\\", [[4, 5]]], \\\"t\\\": [\\\"isiro\\\", \\\"Q899873\\\", [[0]]]}, {\\\"tokens\\\": [\\\"Canadair\\\", \\\"'s\\\", \\\"origins\\\", \\\"lie\\\", \\\"in\\\", \\\"the\\\", \\\"foundation\\\", \\\"of\\\", \\\"a\\\", \\\"manufacturing\\\", \\\"centre\\\", \\\"for\\\", \\\"Canadian\\\", \\\"Vickers\\\", \\\"in\\\", \\\"the\\\", \\\"Montreal\\\", \\\"suburb\\\", \\\"of\\\", \\\"Saint\\\", \\\"-\\\", \\\"Laurent\\\", \\\",\\\", \\\"at\\\", \\\"Cartierville\\\", \\\"Airport\\\", \\\".\\\"], \\\"h\\\": [\\\"cartierville airport\\\", \\\"Q1961318\\\", [[24, 25]]], \\\"t\\\": [\\\"saint-laurent\\\", \\\"Q2117999\\\", [[19, 20, 21]]]}, {\\\"tokens\\\": [\\\"The\\\", \\\"wing\\\", \\\"headquarters\\\", \\\"is\\\", \\\"at\\\", \\\"the\\\", \\\"Rapid\\\", \\\"City\\\", \\\"Regional\\\", \\\"Airport\\\", \\\"in\\\", \\\"Rapid\\\", \\\"City\\\", \\\",\\\", \\\"South\\\", \\\"Dakota\\\", \\\".\\\"], \\\"h\\\": [\\\"rapid city regional airport\\\", \\\"Q2876124\\\", [[6, 7, 8, 9]]], \\\"t\\\": [\\\"rapid city, south dakota\\\", \\\"Q213325\\\", [[11, 12, 13, 14, 15]]]}, {\\\"tokens\\\": [\\\"10,000\\\", \\\"at\\\", \\\"Baiyun\\\", \\\"Airport\\\", \\\"in\\\", \\\"Guangzhou\\\", \\\"were\\\", \\\"stranded\\\", \\\"after\\\", \\\"55\\\", \\\"flights\\\", \\\"were\\\", \\\"cancelled\\\", \\\".\\\"], \\\"h\\\": [\\\"baiyun airport\\\", \\\"Q44868\\\", [[2, 3]]], \\\"t\\\": [\\\"guangzhou\\\", \\\"Q16572\\\", [[5]]]}, {\\\"tokens\\\": [\\\"As\\\", \\\"of\\\", \\\"2013\\\", \\\",\\\", \\\"services\\\", \\\"between\\\", \\\"Bangkok\\\", \\\"and\\\", \\\"Los\\\", \\\"Angeles\\\", \\\"were\\\", \\\"served\\\", \\\"via\\\", \\\"Incheon\\\", \\\"International\\\", \\\"Airport\\\", \\\"near\\\", \\\"Seoul\\\", \\\",\\\", \\\"however\\\", \\\",\\\", \\\"it\\\", \\\"ended\\\", \\\"its\\\", \\\"service\\\", \\\"to\\\", \\\"the\\\", \\\"US\\\", \\\"on\\\", \\\"25\\\", \\\"October\\\", \\\"2015\\\", \\\".\\\"], \\\"h\\\": [\\\"incheon international airport\\\", \\\"Q20932\\\", [[13, 14, 15]]], \\\"t\\\": [\\\"seoul\\\", \\\"Q8684\\\", [[17]]]}, {\\\"tokens\\\": [\\\"C\\\\u00e9sar\\\", \\\"Gaviria\\\", \\\"Trujillo\\\", \\\"Airport\\\", \\\"is\\\", \\\"an\\\", \\\"airport\\\", \\\"serving\\\", \\\"the\\\", \\\"town\\\", \\\"of\\\", \\\"In\\\\u00edrida\\\", \\\"in\\\", \\\"the\\\", \\\"Guain\\\\u00eda\\\", \\\"Department\\\", \\\"of\\\", \\\"Colombia\\\", \\\".\\\"], \\\"h\\\": [\\\"c\\\\u00e9sar gaviria trujillo airport\\\", \\\"Q1323400\\\", [[0, 1, 2, 3]]], \\\"t\\\": [\\\"in\\\\u00edrida\\\", \\\"Q130281\\\", [[11]]]}, {\\\"tokens\\\": [\\\"The\\\", \\\"Solar\\\", \\\"Riser\\\", \\\"made\\\", \\\"the\\\", \\\"first\\\", \\\"man\\\", \\\"-\\\", \\\"carrying\\\", \\\"flight\\\", \\\"on\\\", \\\"solar\\\", \\\"power\\\", \\\"at\\\", \\\"noon\\\", \\\"on\\\", \\\"29\\\", \\\"April\\\", \\\"1979\\\", \\\"at\\\", \\\"Flabob\\\", \\\"Airport\\\", \\\"in\\\", \\\"Riverside\\\", \\\",\\\", \\\"California\\\", \\\".\\\"], \\\"h\\\": [\\\"flabob airport\\\", \\\"Q5456581\\\", [[20, 21]]], \\\"t\\\": [\\\"riverside, california\\\", \\\"Q49243\\\", [[23, 24, 25]]]}, {\\\"tokens\\\": [\\\"The\\\", \\\"aircraft\\\", \\\"involved\\\", \\\"was\\\", \\\"a\\\", \\\"Boeing\\\", \\\"737\\\", \\\"-\\\", \\\"3H4\\\", \\\"N387SW\\\", \\\",\\\", \\\"serial\\\", \\\"number\\\", \\\"26602\\\", \\\",\\\", \\\"operating\\\", \\\"a\\\", \\\"scheduled\\\", \\\"flight\\\", \\\"between\\\", \\\"Nashville\\\", \\\",\\\", \\\"Tennessee\\\", \\\"(\\\", \\\"KBNA\\\", \\\")\\\", \\\",\\\", \\\"and\\\", \\\"Baltimore\\\", \\\",\\\", \\\"Maryland\\\", \\\"(\\\", \\\"KBWI\\\", \\\")\\\", \\\".\\\"], \\\"h\\\": [\\\"kbwi\\\", \\\"Q94895\\\", [[32]]], \\\"t\\\": [\\\"baltimore, maryland\\\", \\\"Q5092\\\", [[28, 29, 30]]]}, {\\\"tokens\\\": [\\\"Its\\\", \\\"main\\\", \\\"base\\\", \\\"was\\\", \\\"Moi\\\", \\\"International\\\", \\\"Airport\\\", \\\",\\\", \\\"Mombasa\\\", \\\".\\\"], \\\"h\\\": [\\\"moi international airport\\\", \\\"Q392784\\\", [[4, 5, 6]]], \\\"t\\\": [\\\"mombasa\\\", \\\"Q225641\\\", [[8]]]}, {\\\"tokens\\\": [\\\"Leo\\\", \\\"Wattimena\\\", \\\"Airport\\\", \\\",\\\", \\\"formerly\\\", \\\"known\\\", \\\"as\\\", \\\"Pitu\\\", \\\"Airport\\\", \\\"is\\\", \\\"a\\\", \\\"private\\\", \\\"airport\\\", \\\"located\\\", \\\"on\\\", \\\"the\\\", \\\"southern\\\", \\\"coast\\\", \\\"of\\\", \\\"Morotai\\\", \\\"Island\\\", \\\",\\\", \\\"North\\\", \\\"Maluku\\\", \\\",\\\", \\\"Indonesia\\\", \\\".\\\"], \\\"h\\\": [\\\"leo wattimena airport\\\", \\\"Q4272507\\\", [[0, 1, 2]]], \\\"t\\\": [\\\"morotai island\\\", \\\"Q19146\\\", [[19, 20]]]}, {\\\"tokens\\\": [\\\"La\\\", \\\"Mina\\\", \\\"Airport\\\", \\\",\\\", \\\"or\\\", \\\"Jorge\\\", \\\"Isaacs\\\", \\\"Airport\\\", \\\"(\\\", \\\")\\\", \\\",\\\", \\\"is\\\", \\\"an\\\", \\\"airport\\\", \\\"serving\\\", \\\"Maicao\\\", \\\",\\\", \\\"a\\\", \\\"municipality\\\", \\\"in\\\", \\\"the\\\", \\\"La\\\", \\\"Guajira\\\", \\\"Department\\\", \\\"in\\\", \\\"Colombia\\\", \\\".\\\"], \\\"h\\\": [\\\"jorge isaacs airport\\\", \\\"Q2902722\\\", [[5, 6, 7]]], \\\"t\\\": [\\\"maicao\\\", \\\"Q1937427\\\", [[15]]]}, {\\\"tokens\\\": [\\\"Bu\\\\u00f4n\\\", \\\"Ma\\\", \\\"Thu\\\\u1ed9t\\\", \\\"is\\\", \\\"served\\\", \\\"by\\\", \\\"Buon\\\", \\\"Ma\\\", \\\"Thuot\\\", \\\"Airport\\\", \\\".\\\"], \\\"h\\\": [\\\"buon ma thuot airport\\\", \\\"Q695570\\\", [[6, 7, 8, 9]]], \\\"t\\\": [\\\"bu\\\\u00f4n ma thu\\\\u1ed9t\\\", \\\"Q33469\\\", [[0, 1, 2]]]}, {\\\"tokens\\\": [\\\"The\\\", \\\"crash\\\", \\\"occurred\\\", \\\"off\\\", \\\"the\\\", \\\"coast\\\", \\\"of\\\", \\\"Jeju\\\", \\\"Island\\\", \\\"after\\\", \\\"the\\\", \\\"crew\\\", \\\"reported\\\", \\\"a\\\", \\\"fire\\\", \\\"in\\\", \\\"the\\\", \\\"cargo\\\", \\\"compartment\\\", \\\"and\\\", \\\"had\\\", \\\"been\\\", \\\"attempting\\\", \\\"to\\\", \\\"divert\\\", \\\"to\\\", \\\"Jeju\\\", \\\"International\\\", \\\"Airport\\\", \\\".\\\"], \\\"h\\\": [\\\"jeju international airport\\\", \\\"Q482497\\\", [[26, 27, 28]]], \\\"t\\\": [\\\"jeju island\\\", \\\"Q29151\\\", [[7, 8]]]}, {\\\"tokens\\\": [\\\"Childress\\\", \\\"Municipal\\\", \\\"Airport\\\", \\\"is\\\", \\\"a\\\", \\\"commercial\\\", \\\"airport\\\", \\\"located\\\", \\\"within\\\", \\\"city\\\", \\\"limits\\\", \\\",\\\", \\\"4\\\", \\\"miles\\\", \\\"west\\\", \\\"of\\\", \\\"central\\\", \\\"Childress\\\", \\\",\\\", \\\"Texas\\\", \\\".\\\"], \\\"h\\\": [\\\"childress municipal airport\\\", \\\"Q3274003\\\", [[0, 1, 2]]], \\\"t\\\": [\\\"childress, texas\\\", \\\"Q982513\\\", [[17, 18, 19]]]}, {\\\"tokens\\\": [\\\"Jos\\\\u00e9\\\", \\\"Leonardo\\\", \\\"Chirino\\\", \\\"Airport\\\", \\\",\\\", \\\"is\\\", \\\"an\\\", \\\"airport\\\", \\\"serving\\\", \\\"Coro\\\", \\\",\\\", \\\"the\\\", \\\"capital\\\", \\\"of\\\", \\\"Falc\\\\u00f3n\\\", \\\"state\\\", \\\"in\\\", \\\"Venezuela\\\", \\\".\\\"], \\\"h\\\": [\\\"jos\\\\u00e9 leonardo chirino airport\\\", \\\"Q1322397\\\", [[0, 1, 2, 3]]], \\\"t\\\": [\\\"coro\\\", \\\"Q1134454\\\", [[9]]]}, {\\\"tokens\\\": [\\\"The\\\", \\\"Mid\\\", \\\"-\\\", \\\"Atlantic\\\", \\\"Air\\\", \\\"Museum\\\", \\\"(\\\", \\\"MAAM\\\", \\\")\\\", \\\"is\\\", \\\"membership\\\", \\\"supported\\\", \\\"museum\\\", \\\"and\\\", \\\"aircraft\\\", \\\"restoration\\\", \\\"facility\\\", \\\"located\\\", \\\"at\\\", \\\"Reading\\\", \\\"Regional\\\", \\\"Airport\\\", \\\"in\\\", \\\"Reading\\\", \\\",\\\", \\\"Pennsylvania\\\", \\\".\\\"], \\\"h\\\": [\\\"reading regional airport\\\", \\\"Q7300558\\\", [[19, 20, 21]]], \\\"t\\\": [\\\"reading, pennsylvania\\\", \\\"Q237896\\\", [[23, 24, 25]]]}, {\\\"tokens\\\": [\\\"Destinations\\\", \\\"served\\\", \\\"as\\\", \\\"of\\\", \\\"2014\\\", \\\"are\\\", \\\"London\\\", \\\"(\\\", \\\"Stansted\\\", \\\"&\\\", \\\"Luton\\\", \\\")\\\", \\\",\\\", \\\"Frankfurt\\\", \\\"-\\\", \\\"Hahn\\\", \\\"Airport\\\", \\\",\\\", \\\"Faro\\\", \\\",\\\", \\\"Portugal\\\", \\\"and\\\", \\\"Alicante\\\", \\\"all\\\", \\\"operated\\\", \\\"by\\\", \\\"Ryanair\\\", \\\".\\\"], \\\"h\\\": [\\\"stansted\\\", \\\"Q8709\\\", [[8]]], \\\"t\\\": [\\\"london\\\", \\\"Q84\\\", [[6]]]}, {\\\"tokens\\\": [\\\"Steamboat\\\", \\\"Springs\\\", \\\"Airport\\\", \\\"(\\\", \\\"Bob\\\", \\\"Adams\\\", \\\"Field\\\", \\\")\\\", \\\"is\\\", \\\"a\\\", \\\"city\\\", \\\"owned\\\", \\\"airport\\\", \\\"three\\\", \\\"miles\\\", \\\"northwest\\\", \\\"of\\\", \\\"Steamboat\\\", \\\"Springs\\\", \\\",\\\", \\\"in\\\", \\\"Routt\\\", \\\"County\\\", \\\",\\\", \\\"Colorado\\\", \\\".\\\"], \\\"h\\\": [\\\"bob adams field\\\", \\\"Q7605416\\\", [[4, 5, 6]]], \\\"t\\\": [\\\"steamboat springs\\\", \\\"Q984721\\\", [[0, 1], [17, 18]]]}, {\\\"tokens\\\": [\\\"Bullfrog\\\", \\\"Basin\\\", \\\"Airport\\\", \\\"is\\\", \\\"a\\\", \\\"public\\\", \\\"airport\\\", \\\"located\\\", \\\"north\\\", \\\"of\\\", \\\"the\\\", \\\"central\\\", \\\"business\\\", \\\"district\\\", \\\"of\\\", \\\"the\\\", \\\"Glen\\\", \\\"Canyon\\\", \\\"National\\\", \\\"Recreation\\\", \\\"Area\\\", \\\",\\\", \\\"in\\\", \\\"Kane\\\", \\\"County\\\", \\\",\\\", \\\"Utah\\\", \\\",\\\", \\\"United\\\", \\\"States\\\", \\\".\\\"], \\\"h\\\": [\\\"bullfrog basin airport\\\", \\\"Q3887489\\\", [[0, 1, 2]]], \\\"t\\\": [\\\"glen canyon national recreation area\\\", \\\"Q1373278\\\", [[16, 17, 18, 19, 20]]]}, {\\\"tokens\\\": [\\\"Las\\\", \\\"Breas\\\", \\\"Airport\\\", \\\"(\\\", \\\",\\\", \\\")\\\", \\\"is\\\", \\\"an\\\", \\\"airport\\\", \\\"south\\\", \\\"-\\\", \\\"southeast\\\", \\\"of\\\", \\\"Taltal\\\", \\\",\\\", \\\"a\\\", \\\"Pacific\\\", \\\"coastal\\\", \\\"town\\\", \\\"in\\\", \\\"the\\\", \\\"Antofagasta\\\", \\\"Region\\\", \\\"of\\\", \\\"Chile\\\", \\\".\\\"], \\\"h\\\": [\\\"las breas airport\\\", \\\"Q16893977\\\", [[0, 1, 2]]], \\\"t\\\": [\\\"taltal\\\", \\\"Q188049\\\", [[13]]]}, {\\\"tokens\\\": [\\\"There\\\", \\\"is\\\", \\\"an\\\", \\\"airport\\\", \\\"in\\\", \\\"the\\\", \\\"district\\\", \\\"located\\\", \\\"in\\\", \\\"Puttaparthi\\\", \\\",\\\", \\\"known\\\", \\\"as\\\", \\\"Sri\\\", \\\"Sathya\\\", \\\"Sai\\\", \\\"Airport\\\", \\\";\\\", \\\"however\\\", \\\"this\\\", \\\"airport\\\", \\\"currently\\\", \\\"has\\\", \\\"no\\\", \\\"scheduled\\\", \\\"service\\\", \\\".\\\"], \\\"h\\\": [\\\"sri sathya sai airport\\\", \\\"Q1939560\\\", [[13, 14, 15, 16]]], \\\"t\\\": [\\\"puttaparthi\\\", \\\"Q1068595\\\", [[9]]]}, {\\\"tokens\\\": [\\\"In\\\", \\\"1959\\\", \\\",\\\", \\\"the\\\", \\\"larger\\\", \\\"Boryspil\\\", \\\"International\\\", \\\"Airport\\\", \\\"was\\\", \\\"built\\\", \\\"near\\\", \\\"the\\\", \\\"city\\\", \\\"of\\\", \\\"Boryspil\\\", \\\",\\\", \\\"gradually\\\", \\\"replacing\\\", \\\"Zhuliany\\\", \\\"as\\\", \\\"the\\\", \\\"main\\\", \\\"airport\\\", \\\"serving\\\", \\\"Kyiv\\\", \\\".\\\"], \\\"h\\\": [\\\"boryspil international airport\\\", \\\"Q477677\\\", [[5, 6, 7]]], \\\"t\\\": [\\\"kyiv\\\", \\\"Q1899\\\", [[24]]]}, {\\\"tokens\\\": [\\\"Badanjilin\\\", \\\"Airport\\\", \\\"is\\\", \\\"one\\\", \\\"of\\\", \\\"the\\\", \\\"three\\\", \\\"airports\\\", \\\"of\\\", \\\"Alxa\\\", \\\"League\\\", \\\"in\\\", \\\"western\\\", \\\"Inner\\\", \\\"Mongolia\\\", \\\",\\\", \\\"the\\\", \\\"other\\\", \\\"two\\\", \\\"being\\\", \\\"Alxa\\\", \\\"Left\\\", \\\"Banner\\\", \\\"Bayanhot\\\", \\\"Airport\\\", \\\"and\\\", \\\"Ejin\\\", \\\"Banner\\\", \\\"Taolai\\\", \\\"Airport\\\", \\\".\\\"], \\\"h\\\": [\\\"alxa left banner bayanhot airport\\\", \\\"Q16258986\\\", [[20, 21, 22, 23, 24]]], \\\"t\\\": [\\\"alxa league\\\", \\\"Q449963\\\", [[9, 10]]]}, {\\\"tokens\\\": [\\\"Capital\\\", \\\"City\\\", \\\"Airport\\\", \\\"(\\\", \\\"currently\\\", \\\"used\\\", \\\"by\\\", \\\"general\\\", \\\"aviation\\\", \\\";\\\", \\\"formerly\\\", \\\"Harrisburg\\\", \\\"'s\\\", \\\"principal\\\", \\\"airport\\\", \\\")\\\", \\\"and\\\", \\\"the\\\", \\\"New\\\", \\\"Cumberland\\\", \\\"Army\\\", \\\"Depot\\\", \\\"both\\\", \\\"lie\\\", \\\"in\\\", \\\"Fairview\\\", \\\"Township\\\", \\\".\\\"], \\\"h\\\": [\\\"capital city airport\\\", \\\"Q3274856\\\", [[0, 1, 2]]], \\\"t\\\": [\\\"harrisburg\\\", \\\"Q25280\\\", [[11]]]}, {\\\"tokens\\\": [\\\"Meythet\\\", \\\"Airport\\\", \\\"in\\\", \\\"Annecy\\\", \\\"has\\\", \\\"Air\\\", \\\"France\\\", \\\"Regional\\\", \\\"round\\\", \\\"-\\\", \\\"trip\\\", \\\"service\\\", \\\"to\\\", \\\"Paris\\\", \\\"Orly\\\", \\\".\\\"], \\\"h\\\": [\\\"meythet airport\\\", \\\"Q1430810\\\", [[0, 1]]], \\\"t\\\": [\\\"annecy\\\", \\\"Q50189\\\", [[3]]]}, {\\\"tokens\\\": [\\\"During\\\", \\\"the\\\", \\\"late\\\", \\\"morning\\\", \\\"of\\\", \\\"April\\\", \\\"3\\\", \\\",\\\", \\\"1964\\\", \\\",\\\", \\\"a\\\", \\\"destructive\\\", \\\"tornado\\\", \\\"ripped\\\", \\\"through\\\", \\\"the\\\", \\\"City\\\", \\\"View\\\", \\\"section\\\", \\\"of\\\", \\\"northwestern\\\", \\\"Wichita\\\", \\\"Falls\\\", \\\"and\\\", \\\"neighboring\\\", \\\"Sheppard\\\", \\\"Air\\\", \\\"Force\\\", \\\"Base\\\", \\\".\\\"], \\\"h\\\": [\\\"sheppard air force base\\\", \\\"Q176146\\\", [[25, 26, 27, 28]]], \\\"t\\\": [\\\"wichita falls\\\", \\\"Q128349\\\", [[21, 22]]]}, {\\\"tokens\\\": [\\\"44\\\", \\\"-\\\", \\\"73287\\\", \\\")\\\", \\\"currently\\\", \\\"based\\\", \\\"at\\\", \\\"the\\\", \\\"Air\\\", \\\"Combat\\\", \\\"Museum\\\", \\\"at\\\", \\\"Abraham\\\", \\\"Lincoln\\\", \\\"Capital\\\", \\\"Airport\\\", \\\"in\\\", \\\"Springfield\\\", \\\",\\\", \\\"Illinois\\\", \\\".\\\"], \\\"h\\\": [\\\"abraham lincoln capital airport\\\", \\\"Q1320523\\\", [[12, 13, 14, 15]]], \\\"t\\\": [\\\"springfield\\\", \\\"Q28515\\\", [[17]]]}, {\\\"tokens\\\": [\\\"Employed\\\", \\\"by\\\", \\\"Australian\\\", \\\"National\\\", \\\"Airways\\\", \\\"(\\\", \\\"ANA\\\", \\\")\\\", \\\"after\\\", \\\"leaving\\\", \\\"the\\\", \\\"Air\\\", \\\"Force\\\", \\\",\\\", \\\"Lukis\\\", \\\"become\\\", \\\"airfield\\\", \\\"manager\\\", \\\"at\\\", \\\"Essendon\\\", \\\",\\\", \\\"Melbourne\\\", \\\".\\\"], \\\"h\\\": [\\\"essendon\\\", \\\"Q1319272\\\", [[19]]], \\\"t\\\": [\\\"melbourne\\\", \\\"Q3141\\\", [[21]]]}, {\\\"tokens\\\": [\\\"The\\\", \\\"Laurel\\\", \\\"Municipal\\\", \\\"Airport\\\", \\\"is\\\", \\\"a\\\", \\\"publicly\\\", \\\"owned\\\", \\\"public\\\", \\\"-\\\", \\\"use\\\", \\\"airport\\\", \\\"in\\\", \\\"Laurel\\\", \\\",\\\", \\\"Montana\\\", \\\",\\\", \\\"which\\\", \\\"is\\\", \\\"located\\\", \\\"southwest\\\", \\\"of\\\", \\\"downtown\\\", \\\"Billings\\\", \\\".\\\"], \\\"h\\\": [\\\"laurel municipal airport\\\", \\\"Q6499928\\\", [[1, 2, 3]]], \\\"t\\\": [\\\"laurel, montana\\\", \\\"Q768628\\\", [[13, 14, 15]]]}, {\\\"tokens\\\": [\\\"Hualien\\\", \\\"City\\\", \\\"is\\\", \\\"served\\\", \\\"by\\\", \\\"Hualien\\\", \\\"Airport\\\", \\\"located\\\", \\\"at\\\", \\\"the\\\", \\\"neighboring\\\", \\\"Xincheng\\\", \\\"Township\\\", \\\"of\\\", \\\"Hualien\\\", \\\"County\\\", \\\".\\\"], \\\"h\\\": [\\\"hualien airport\\\", \\\"Q703921\\\", [[5, 6]]], \\\"t\\\": [\\\"hualien city\\\", \\\"Q713310\\\", [[0, 1]]]}, {\\\"tokens\\\": [\\\"Merlin\\\", \\\"Airways\\\", \\\",\\\", \\\"Inc.\\\", \\\"is\\\", \\\"a\\\", \\\"cargo\\\", \\\"airline\\\", \\\"based\\\", \\\"in\\\", \\\"Rafael\\\", \\\"Hern\\\\u00e1ndez\\\", \\\"International\\\", \\\"Airport\\\", \\\"in\\\", \\\"Aguadilla\\\", \\\",\\\", \\\"Puerto\\\", \\\"Rico\\\", \\\".\\\"], \\\"h\\\": [\\\"rafael hern\\\\u00e1ndez international airport\\\", \\\"Q2276582\\\", [[10, 11, 12, 13]]], \\\"t\\\": [\\\"aguadilla, puerto rico\\\", \\\"Q397826\\\", [[15, 16, 17, 18]]]}, {\\\"tokens\\\": [\\\"Due\\\", \\\"to\\\", \\\"the\\\", \\\"extensive\\\", \\\"military\\\", \\\"cooperation\\\", \\\"between\\\", \\\"both\\\", \\\"countries\\\", \\\",\\\", \\\"there\\\", \\\"are\\\", \\\"also\\\", \\\"around\\\", \\\"3,500\\\", \\\"American\\\", \\\"military\\\", \\\"personnel\\\", \\\"stationed\\\", \\\"at\\\", \\\"the\\\", \\\"Al\\\", \\\"Dhafra\\\", \\\"Air\\\", \\\"Base\\\", \\\"in\\\", \\\"Abu\\\", \\\"Dhabi\\\", \\\".\\\"], \\\"h\\\": [\\\"al dhafra air base\\\", \\\"Q2886453\\\", [[21, 22, 23, 24]]], \\\"t\\\": [\\\"abu dhabi\\\", \\\"Q1519\\\", [[26, 27]]]}, {\\\"tokens\\\": [\\\"Johan\\\", \\\"Pienaar\\\", \\\"Airport\\\", \\\"is\\\", \\\"an\\\", \\\"airport\\\", \\\"serving\\\", \\\"Kuruman\\\", \\\",\\\", \\\"a\\\", \\\"town\\\", \\\"in\\\", \\\"Northern\\\", \\\"Cape\\\", \\\"province\\\", \\\",\\\", \\\"South\\\", \\\"Africa\\\", \\\".\\\"], \\\"h\\\": [\\\"johan pienaar airport\\\", \\\"Q1580098\\\", [[0, 1, 2]]], \\\"t\\\": [\\\"kuruman\\\", \\\"Q1025965\\\", [[7]]]}, {\\\"tokens\\\": [\\\"Its\\\", \\\"main\\\", \\\"hub\\\", \\\"is\\\", \\\"at\\\", \\\"Shahjalal\\\", \\\"International\\\", \\\"Airport\\\", \\\"in\\\", \\\"Dhaka\\\", \\\"and\\\", \\\"it\\\", \\\"also\\\", \\\"operates\\\", \\\"flights\\\", \\\"from\\\", \\\"its\\\", \\\"secondary\\\", \\\"hubs\\\", \\\"at\\\", \\\"Shah\\\", \\\"Amanat\\\", \\\"International\\\", \\\"Airport\\\", \\\"in\\\", \\\"Chittagong\\\", \\\"and\\\", \\\"Osmani\\\", \\\"International\\\", \\\"Airport\\\", \\\"in\\\", \\\"Sylhet\\\", \\\".\\\"], \\\"h\\\": [\\\"shah amanat international airport\\\", \\\"Q525609\\\", [[20, 21, 22, 23]]], \\\"t\\\": [\\\"chittagong\\\", \\\"Q376749\\\", [[25]]]}, {\\\"tokens\\\": [\\\"Nodaway\\\", \\\"County\\\", \\\"is\\\", \\\"served\\\", \\\"by\\\", \\\"Northwest\\\", \\\"Missouri\\\", \\\"Regional\\\", \\\"Airport\\\", \\\"in\\\", \\\"Maryville\\\", \\\",\\\", \\\"which\\\", \\\"is\\\", \\\"a\\\", \\\"general\\\", \\\"aviation\\\", \\\"airport\\\", \\\"with\\\", \\\"no\\\", \\\"commercial\\\", \\\"service\\\", \\\".\\\"], \\\"h\\\": [\\\"northwest missouri regional airport\\\", \\\"Q7060119\\\", [[5, 6, 7, 8]]], \\\"t\\\": [\\\"maryville\\\", \\\"Q957284\\\", [[10]]]}, {\\\"tokens\\\": [\\\"In\\\", \\\"2007\\\", \\\",\\\", \\\"they\\\", \\\"moved\\\", \\\"to\\\", \\\"a\\\", \\\"new\\\", \\\"custom\\\", \\\"built\\\", \\\"facility\\\", \\\"at\\\", \\\"Portsmouth\\\", \\\"International\\\", \\\"Airport\\\", \\\"at\\\", \\\"Pease\\\", \\\"in\\\", \\\"Portsmouth\\\", \\\",\\\", \\\"New\\\", \\\"Hampshire\\\", \\\".\\\", \\\"Shir\\\", \\\"Haberman\\\", \\\"(\\\", \\\"2\\\", \\\"June\\\", \\\"2008\\\", \\\")\\\", \\\".\\\"], \\\"h\\\": [\\\"portsmouth international airport at pease\\\", \\\"Q6587102\\\", [[12, 13, 14, 15, 16]]], \\\"t\\\": [\\\"portsmouth, new hampshire\\\", \\\"Q49191\\\", [[18, 19, 20, 21]]]}, {\\\"tokens\\\": [\\\"Thai\\\", \\\"Airways\\\", \\\"International\\\", \\\"Flight\\\", \\\"311\\\", \\\"was\\\", \\\"a\\\", \\\"flight\\\", \\\"from\\\", \\\"Bangkok\\\", \\\",\\\", \\\"Thailand\\\", \\\"'s\\\", \\\"Don\\\", \\\"Mueang\\\", \\\"International\\\", \\\"Airport\\\", \\\"to\\\", \\\"Kathmandu\\\", \\\",\\\", \\\"Nepal\\\", \\\"'s\\\", \\\"Tribhuvan\\\", \\\"International\\\", \\\"Airport\\\", \\\".\\\"], \\\"h\\\": [\\\"tribhuvan international airport\\\", \\\"Q61066\\\", [[22, 23, 24]]], \\\"t\\\": [\\\"kathmandu\\\", \\\"Q3037\\\", [[18]]]}, {\\\"tokens\\\": [\\\"Most\\\", \\\"of\\\", \\\"the\\\", \\\"scheduled\\\", \\\"flights\\\", \\\"are\\\", \\\"to\\\", \\\"the\\\", \\\"Bahamas\\\", \\\",\\\", \\\"with\\\", \\\"flights\\\", \\\"to\\\", \\\"Albert\\\", \\\"Whitted\\\", \\\"Airport\\\", \\\"in\\\", \\\"St\\\", \\\"Petersburg\\\", \\\",\\\", \\\"Florida\\\", \\\".\\\"], \\\"h\\\": [\\\"albert whitted airport\\\", \\\"Q4711466\\\", [[13, 14, 15]]], \\\"t\\\": [\\\"st petersburg\\\", \\\"Q49236\\\", [[17, 18]]]}, {\\\"tokens\\\": [\\\"Mammoth\\\", \\\"Yosemite\\\", \\\"Airport\\\", \\\"is\\\", \\\"a\\\", \\\"town\\\", \\\"-\\\", \\\"owned\\\", \\\"public\\\", \\\"airport\\\", \\\"seven\\\", \\\"miles\\\", \\\"east\\\", \\\"of\\\", \\\"Mammoth\\\", \\\"Lakes\\\", \\\",\\\", \\\"in\\\", \\\"Mono\\\", \\\"County\\\", \\\",\\\", \\\"California\\\", \\\".\\\"], \\\"h\\\": [\\\"mammoth yosemite airport\\\", \\\"Q6745883\\\", [[0, 1, 2]]], \\\"t\\\": [\\\"mammoth lakes\\\", \\\"Q983604\\\", [[14, 15]]]}, {\\\"tokens\\\": [\\\"It\\\", \\\"replaces\\\", \\\"Tena\\\", \\\"'s\\\", \\\"Mayor\\\", \\\"Galo\\\", \\\"de\\\", \\\"la\\\", \\\"Torre\\\", \\\"Airport\\\", \\\",\\\", \\\"which\\\", \\\"closed\\\", \\\"in\\\", \\\"2001\\\", \\\".\\\"], \\\"h\\\": [\\\"mayor galo de la torre airport\\\", \\\"Q22632230\\\", [[4, 5, 6, 7, 8, 9]]], \\\"t\\\": [\\\"tena\\\", \\\"Q994312\\\", [[2]]]}, {\\\"tokens\\\": [\\\"Alamosa\\\", \\\"is\\\", \\\"served\\\", \\\"by\\\", \\\"San\\\", \\\"Luis\\\", \\\"Valley\\\", \\\"Regional\\\", \\\"Airport\\\", \\\".\\\"], \\\"h\\\": [\\\"san luis valley regional airport\\\", \\\"Q7414773\\\", [[4, 5, 6, 7, 8]]], \\\"t\\\": [\\\"alamosa\\\", \\\"Q1010247\\\", [[0]]]}, {\\\"tokens\\\": [\\\"The\\\", \\\"Dallas\\\", \\\"-\\\", \\\"Fort\\\", \\\"Worth\\\", \\\"Metroplex\\\", \\\"'s\\\", \\\"major\\\", \\\"international\\\", \\\"airport\\\", \\\",\\\", \\\"Dallas\\\", \\\"-\\\", \\\"Fort\\\", \\\"Worth\\\", \\\"International\\\", \\\"Airport\\\", \\\",\\\", \\\"is\\\", \\\"located\\\", \\\"a\\\", \\\"short\\\", \\\"distance\\\", \\\"to\\\", \\\"the\\\", \\\"northwest\\\", \\\".\\\"], \\\"h\\\": [\\\"dallas-fort worth international airport\\\", \\\"Q459096\\\", [[11, 12, 13, 14, 15, 16]]], \\\"t\\\": [\\\"dallas-fort worth metroplex\\\", \\\"Q179295\\\", [[1, 2, 3, 4, 5]]]}, {\\\"tokens\\\": [\\\"P\\\\u00e9rigueux\\\", \\\"-\\\", \\\"Bassillac\\\", \\\"Airport\\\", \\\"(\\\", \\\")\\\", \\\"is\\\", \\\"an\\\", \\\"airport\\\", \\\"in\\\", \\\"the\\\", \\\"village\\\", \\\"of\\\", \\\"Bassillac\\\", \\\"in\\\", \\\"the\\\", \\\"Dordogne\\\", \\\"department\\\", \\\",\\\", \\\"Nouvelle\\\", \\\"-\\\", \\\"Aquitaine\\\", \\\"region\\\", \\\",\\\", \\\"France\\\", \\\".\\\"], \\\"h\\\": [\\\"bassillac airport\\\", \\\"Q1432520\\\", [[2, 3]]], \\\"t\\\": [\\\"p\\\\u00e9rigueux\\\", \\\"Q6588\\\", [[0]]]}, {\\\"tokens\\\": [\\\"The\\\", \\\"main\\\", \\\"settlement\\\", \\\"is\\\", \\\"Seronera\\\", \\\",\\\", \\\"which\\\", \\\"houses\\\", \\\"the\\\", \\\"majority\\\", \\\"of\\\", \\\"research\\\", \\\"staff\\\", \\\"and\\\", \\\"the\\\", \\\"park\\\", \\\"'s\\\", \\\"main\\\", \\\"headquarters\\\", \\\",\\\", \\\"including\\\", \\\"its\\\", \\\"primary\\\", \\\"airstrip\\\", \\\".\\\"], \\\"h\\\": [\\\"airstrip\\\", \\\"Q7455033\\\", [[23]]], \\\"t\\\": [\\\"seronera\\\", \\\"Q6273481\\\", [[4]]]}, {\\\"tokens\\\": [\\\"Jakar\\\", \\\"is\\\", \\\"also\\\", \\\"the\\\", \\\"site\\\", \\\"of\\\", \\\"Bathpalathang\\\", \\\"Airport\\\", \\\".\\\"], \\\"h\\\": [\\\"bathpalathang airport\\\", \\\"Q153191\\\", [[6, 7]]], \\\"t\\\": [\\\"jakar\\\", \\\"Q2468415\\\", [[0]]]}, {\\\"tokens\\\": [\\\"A\\\", \\\"runway\\\", \\\"at\\\", \\\"the\\\", \\\"Cape\\\", \\\"Canaveral\\\", \\\"Air\\\", \\\"Force\\\", \\\"Station\\\", \\\"is\\\", \\\"still\\\", \\\"known\\\", \\\"as\\\", \\\"the\\\", \\\"\\\\\\\"\\\", \\\"Skid\\\", \\\"Strip\\\", \\\"\\\\\\\"\\\", \\\".\\\"], \\\"h\\\": [\\\"\\\\\\\"skid strip\\\\\\\"\\\", \\\"Q3275436\\\", [[14, 15, 16, 17]]], \\\"t\\\": [\\\"cape canaveral air force station\\\", \\\"Q334465\\\", [[4, 5, 6, 7, 8]]]}, {\\\"tokens\\\": [\\\"Siglufj\\\\u00f6r\\\\u00f0ur\\\", \\\"Airport\\\", \\\"or\\\", \\\"Siglufjordur\\\", \\\"Airport\\\", \\\"is\\\", \\\"an\\\", \\\"airport\\\", \\\"serving\\\", \\\"Siglufj\\\\u00f6r\\\\u00f0ur\\\", \\\",\\\", \\\"Iceland\\\", \\\".\\\"], \\\"h\\\": [\\\"siglufjordur airport\\\", \\\"Q2875922\\\", [[3, 4]]], \\\"t\\\": [\\\"siglufj\\\\u00f6r\\\\u00f0ur\\\", \\\"Q1887662\\\", [[0], [9]]]}, {\\\"tokens\\\": [\\\"In\\\", \\\"February\\\", \\\"1935\\\", \\\",\\\", \\\"Hardy\\\", \\\"entered\\\", \\\"aviation\\\", \\\"cadet\\\", \\\"training\\\", \\\"at\\\", \\\"Randolph\\\", \\\"Field\\\", \\\"in\\\", \\\"San\\\", \\\"Antonio\\\", \\\".\\\"], \\\"h\\\": [\\\"randolph field\\\", \\\"Q980034\\\", [[10, 11]]], \\\"t\\\": [\\\"san antonio\\\", \\\"Q975\\\", [[13, 14]]]}, {\\\"tokens\\\": [\\\"APS\\\", \\\"is\\\", \\\"headquartered\\\", \\\"at\\\", \\\"the\\\", \\\"Phoenix\\\", \\\"-\\\", \\\"Mesa\\\", \\\"Gateway\\\", \\\"Airport\\\", \\\"(\\\", \\\"KIWA\\\", \\\")\\\", \\\"in\\\", \\\"Mesa\\\", \\\",\\\", \\\"Arizona\\\", \\\".\\\"], \\\"h\\\": [\\\"phoenix-mesa gateway airport\\\", \\\"Q493759\\\", [[5, 6, 7, 8, 9]]], \\\"t\\\": [\\\"mesa, arizona\\\", \\\"Q49261\\\", [[14, 15, 16]]]}, {\\\"tokens\\\": [\\\"Its\\\", \\\"main\\\", \\\"hub\\\", \\\"is\\\", \\\"Golos\\\\u00f3n\\\", \\\"International\\\", \\\"Airport\\\", \\\",\\\", \\\"La\\\", \\\"Ceiba\\\", \\\".\\\"], \\\"h\\\": [\\\"golos\\\\u00f3n international airport\\\", \\\"Q2231517\\\", [[4, 5, 6]]], \\\"t\\\": [\\\"la ceiba\\\", \\\"Q916536\\\", [[8, 9]]]}, {\\\"tokens\\\": [\\\"On\\\", \\\"March\\\", \\\"24\\\", \\\",\\\", \\\"the\\\", \\\"production\\\", \\\"moved\\\", \\\"to\\\", \\\"Raymond\\\", \\\",\\\", \\\"Mississippi\\\", \\\",\\\", \\\"where\\\", \\\"the\\\", \\\"crew\\\", \\\"filmed\\\", \\\"a\\\", \\\"scene\\\", \\\"at\\\", \\\"the\\\", \\\"John\\\", \\\"Bell\\\", \\\"Williams\\\", \\\"Airport\\\", \\\".\\\"], \\\"h\\\": [\\\"john bell williams airport\\\", \\\"Q2901886\\\", [[20, 21, 22, 23]]], \\\"t\\\": [\\\"raymond, mississippi\\\", \\\"Q1779125\\\", [[8, 9, 10]]]}, {\\\"tokens\\\": [\\\"The\\\", \\\"Bell\\\", \\\"430\\\", \\\"helicopter\\\", \\\"took\\\", \\\"off\\\", \\\"from\\\", \\\"Begumpet\\\", \\\"Airport\\\", \\\",\\\", \\\"Hyderabad\\\", \\\",\\\", \\\"and\\\", \\\"soon\\\", \\\"encountered\\\", \\\"bad\\\", \\\"weather\\\", \\\".\\\"], \\\"h\\\": [\\\"begumpet airport\\\", \\\"Q1657769\\\", [[7, 8]]], \\\"t\\\": [\\\"hyderabad\\\", \\\"Q1361\\\", [[10]]]}, {\\\"tokens\\\": [\\\"The\\\", \\\"Visalia\\\", \\\"Municipal\\\", \\\"Airport\\\", \\\"is\\\", \\\"a\\\", \\\"city\\\", \\\"-\\\", \\\"owned\\\", \\\"airport\\\", \\\"for\\\", \\\"the\\\", \\\"city\\\", \\\"of\\\", \\\"Visalia\\\", \\\",\\\", \\\"California\\\", \\\".\\\"], \\\"h\\\": [\\\"visalia municipal airport\\\", \\\"Q7935607\\\", [[1, 2, 3]]], \\\"t\\\": [\\\"visalia, california\\\", \\\"Q495373\\\", [[14, 15, 16]]]}, {\\\"tokens\\\": [\\\"Stinson\\\", \\\"Field\\\", \\\"Municipal\\\", \\\"Airport\\\", \\\"is\\\", \\\"closed\\\", \\\"airport\\\", \\\"located\\\", \\\"3\\\", \\\"miles\\\", \\\"northwest\\\", \\\"of\\\", \\\"Aberdeen\\\", \\\",\\\", \\\"Mississippi\\\", \\\".\\\"], \\\"h\\\": [\\\"stinson field municipal airport\\\", \\\"Q7617473\\\", [[0, 1, 2, 3]]], \\\"t\\\": [\\\"aberdeen, mississippi\\\", \\\"Q1065452\\\", [[12, 13, 14]]]}, {\\\"tokens\\\": [\\\"Sua\\\", \\\"Pan\\\", \\\"Airport\\\", \\\"or\\\", \\\"Sowa\\\", \\\"Airport\\\", \\\"is\\\", \\\"an\\\", \\\"airport\\\", \\\"west\\\", \\\"of\\\", \\\"Sowa\\\", \\\",\\\", \\\"a\\\", \\\"town\\\", \\\"in\\\", \\\"the\\\", \\\"Central\\\", \\\"District\\\", \\\"of\\\", \\\"Botswana\\\", \\\".\\\"], \\\"h\\\": [\\\"sua pan airport\\\", \\\"Q7630421\\\", [[0, 1, 2]]], \\\"t\\\": [\\\"sowa\\\", \\\"Q141310\\\", [[4], [11]]]}, {\\\"tokens\\\": [\\\"They\\\", \\\"operated\\\", \\\"the\\\", \\\"first\\\", \\\"services\\\", \\\"to\\\", \\\"Dunedin\\\", \\\"'s\\\", \\\"new\\\", \\\"Momona\\\", \\\"Airport\\\", \\\"in\\\", \\\"1962\\\", \\\"until\\\", \\\"traffic\\\", \\\"built\\\", \\\"up\\\", \\\"enough\\\", \\\"to\\\", \\\"use\\\", \\\"the\\\", \\\"Viscounts\\\", \\\"there\\\", \\\".\\\"], \\\"h\\\": [\\\"momona airport\\\", \\\"Q1364375\\\", [[9, 10]]], \\\"t\\\": [\\\"dunedin\\\", \\\"Q133073\\\", [[6]]]}, {\\\"tokens\\\": [\\\"Tepper\\\", \\\"Aviation\\\", \\\",\\\", \\\"Inc.\\\", \\\"is\\\", \\\"based\\\", \\\"at\\\", \\\"the\\\", \\\"Bob\\\", \\\"Sikes\\\", \\\"Airport\\\", \\\"in\\\", \\\"Crestview\\\", \\\",\\\", \\\"Florida\\\", \\\".\\\"], \\\"h\\\": [\\\"bob sikes airport\\\", \\\"Q597487\\\", [[8, 9, 10]]], \\\"t\\\": [\\\"crestview, florida\\\", \\\"Q2153124\\\", [[12, 13, 14]]]}, {\\\"tokens\\\": [\\\"Northern\\\", \\\"Area\\\", \\\"CFTSU\\\", \\\"is\\\", \\\"based\\\", \\\"at\\\", \\\"HMNZS\\\", \\\"Philomel\\\", \\\"in\\\", \\\"Auckland\\\", \\\",\\\", \\\"Central\\\", \\\"Area\\\", \\\"CFTSU\\\", \\\"at\\\", \\\"RNZAF\\\", \\\"Base\\\", \\\"Ohakea\\\", \\\"near\\\", \\\"Palmerston\\\", \\\"North\\\", \\\"and\\\", \\\"Southern\\\", \\\"Area\\\", \\\"CFTSU\\\", \\\"at\\\", \\\"Burnham\\\", \\\"Military\\\", \\\"Camp\\\", \\\"just\\\", \\\"South\\\", \\\"of\\\", \\\"Christchurch\\\", \\\".\\\"], \\\"h\\\": [\\\"rnzaf base ohakea\\\", \\\"Q7277291\\\", [[15, 16, 17]]], \\\"t\\\": [\\\"palmerston north\\\", \\\"Q212289\\\", [[19, 20]]]}, {\\\"tokens\\\": [\\\"Br\\\\u010dko\\\", \\\"was\\\", \\\"a\\\", \\\"geographic\\\", \\\"point\\\", \\\"of\\\", \\\"contention\\\", \\\"in\\\", \\\"1996\\\", \\\"when\\\", \\\"the\\\", \\\"U.S\\\", \\\".-\\\", \\\"led\\\", \\\"Implementation\\\", \\\"Force\\\", \\\"(\\\", \\\"IFOR\\\", \\\")\\\", \\\"built\\\", \\\"Camp\\\", \\\"McGovern\\\", \\\"on\\\", \\\"the\\\", \\\"outskirts\\\", \\\"of\\\", \\\"the\\\", \\\"city\\\", \\\".\\\"], \\\"h\\\": [\\\"camp mcgovern\\\", \\\"Q16890056\\\", [[20, 21]]], \\\"t\\\": [\\\"br\\\\u010dko\\\", \\\"Q322828\\\", [[0]]]}, {\\\"tokens\\\": [\\\"The\\\", \\\"Potomac\\\", \\\"Highlands\\\", \\\"Airport\\\", \\\"Authority\\\", \\\"is\\\", \\\"an\\\", \\\"Interstate\\\", \\\"Agency\\\", \\\"that\\\", \\\"operates\\\", \\\"the\\\", \\\"Greater\\\", \\\"Cumberland\\\", \\\"Regional\\\", \\\"Airport\\\", \\\",\\\", \\\"two\\\", \\\"miles\\\", \\\"south\\\", \\\"of\\\", \\\"Cumberland\\\", \\\",\\\", \\\"Maryland\\\", \\\"in\\\", \\\"the\\\", \\\"state\\\", \\\"of\\\", \\\"West\\\", \\\"Virginia\\\", \\\".\\\"], \\\"h\\\": [\\\"greater cumberland regional airport\\\", \\\"Q3913914\\\", [[12, 13, 14, 15]]], \\\"t\\\": [\\\"cumberland, maryland\\\", \\\"Q754868\\\", [[21, 22, 23]]]}, {\\\"tokens\\\": [\\\"Baucau\\\", \\\"Airport\\\", \\\",\\\", \\\"former\\\", \\\"Cakung\\\", \\\"Airport\\\", \\\",\\\", \\\"is\\\", \\\"an\\\", \\\"unattended\\\", \\\"airport\\\", \\\"located\\\", \\\"west\\\", \\\"of\\\", \\\"Baucau\\\", \\\",\\\", \\\"a\\\", \\\"city\\\", \\\"in\\\", \\\"East\\\", \\\"Timor\\\", \\\"(\\\", \\\"\\\\\\\"\\\", \\\"Timor\\\", \\\"-\\\", \\\"Leste\\\", \\\"\\\\\\\"\\\", \\\")\\\", \\\".\\\"], \\\"h\\\": [\\\"cakung airport\\\", \\\"Q1430948\\\", [[4, 5]]], \\\"t\\\": [\\\"baucau\\\", \\\"Q811130\\\", [[0], [14]]]}, {\\\"tokens\\\": [\\\"Its\\\", \\\"operations\\\", \\\"initially\\\", \\\"focused\\\", \\\"on\\\", \\\"providing\\\", \\\"air\\\", \\\"service\\\", \\\"into\\\", \\\"Borrego\\\", \\\"Springs\\\", \\\",\\\", \\\"California\\\", \\\"via\\\", \\\"the\\\", \\\"Borrego\\\", \\\"Valley\\\", \\\"Airport\\\", \\\"from\\\", \\\"other\\\", \\\"destinations\\\", \\\"in\\\", \\\"southern\\\", \\\"California\\\", \\\"such\\\", \\\"as\\\", \\\"San\\\", \\\"Diego\\\", \\\"and\\\", \\\"Palm\\\", \\\"Springs\\\", \\\".\\\"], \\\"h\\\": [\\\"borrego valley airport\\\", \\\"Q3606044\\\", [[15, 16, 17]]], \\\"t\\\": [\\\"borrego springs, california\\\", \\\"Q2049424\\\", [[9, 10, 11, 12]]]}, {\\\"tokens\\\": [\\\"Maria\\\", \\\"Cristina\\\", \\\"Airport\\\", \\\",\\\", \\\"is\\\", \\\"located\\\", \\\"in\\\", \\\"Balo\\\", \\\"-\\\", \\\"i\\\", \\\",\\\", \\\"Lanao\\\", \\\"del\\\", \\\"Norte\\\", \\\",\\\", \\\"and\\\", \\\"was\\\", \\\"the\\\", \\\"main\\\", \\\"airport\\\", \\\"of\\\", \\\"Iligan\\\", \\\"in\\\", \\\"the\\\", \\\"late\\\", \\\"1980s\\\", \\\".\\\"], \\\"h\\\": [\\\"maria cristina airport\\\", \\\"Q1031517\\\", [[0, 1, 2]]], \\\"t\\\": [\\\"iligan\\\", \\\"Q285488\\\", [[21]]]}, {\\\"tokens\\\": [\\\"Ondangwa\\\", \\\"town\\\", \\\"has\\\", \\\"a\\\", \\\"population\\\", \\\"of\\\", \\\"36,800\\\", \\\"according\\\", \\\"to\\\", \\\"the\\\", \\\"2011\\\", \\\"census\\\", \\\"data\\\", \\\"and\\\", \\\"has\\\", \\\"a\\\", \\\"small\\\", \\\"airport\\\", \\\"serviced\\\", \\\"by\\\", \\\"two\\\", \\\"daily\\\", \\\"Air\\\", \\\"Namibia\\\", \\\"commercial\\\", \\\"flights\\\", \\\"from\\\", \\\"Windhoek\\\", \\\"\\\\u2019s\\\", \\\"Eros\\\", \\\"Airport\\\", \\\".\\\"], \\\"h\\\": [\\\"eros airport\\\", \\\"Q1321635\\\", [[29, 30]]], \\\"t\\\": [\\\"windhoek\\\", \\\"Q3935\\\", [[27]]]}, {\\\"tokens\\\": [\\\"Despite\\\", \\\"his\\\", \\\"injury\\\", \\\",\\\", \\\"Cena\\\", \\\"attended\\\", \\\"the\\\", \\\"annual\\\", \\\"WWE\\\", \\\"'s\\\", \\\"\\\\\\\"\\\", \\\"Tribute\\\", \\\"to\\\", \\\"the\\\", \\\"Troops\\\", \\\"\\\\\\\"\\\", \\\"show\\\", \\\"filmed\\\", \\\"at\\\", \\\"Camp\\\", \\\"Speicher\\\", \\\"in\\\", \\\"Tikrit\\\", \\\",\\\", \\\"Iraq\\\", \\\"on\\\", \\\"December\\\", \\\"7\\\", \\\",\\\", \\\"and\\\", \\\"aired\\\", \\\"on\\\", \\\"December\\\", \\\"24\\\", \\\".\\\"], \\\"h\\\": [\\\"camp speicher\\\", \\\"Q5013269\\\", [[19, 20]]], \\\"t\\\": [\\\"tikrit\\\", \\\"Q165444\\\", [[22]]]}, {\\\"tokens\\\": [\\\"In\\\", \\\"mid-1951\\\", \\\",\\\", \\\"IMCO\\\", \\\"expanded\\\", \\\"to\\\", \\\"the\\\", \\\"Brady\\\", \\\",\\\", \\\"Texas\\\", \\\"area\\\", \\\",\\\", \\\"starting\\\", \\\"up\\\", \\\"Brady\\\", \\\"Aviation\\\", \\\"at\\\", \\\"Curtis\\\", \\\"Field\\\", \\\".\\\"], \\\"h\\\": [\\\"curtis field\\\", \\\"Q1656327\\\", [[17, 18]]], \\\"t\\\": [\\\"brady, texas\\\", \\\"Q981872\\\", [[7, 8, 9]]]}, {\\\"tokens\\\": [\\\"Every\\\", \\\"major\\\", \\\"form\\\", \\\"of\\\", \\\"transportation\\\", \\\"serves\\\", \\\"Long\\\", \\\"Island\\\", \\\",\\\", \\\"including\\\", \\\"three\\\", \\\"major\\\", \\\"airports\\\", \\\",\\\", \\\"railroads\\\", \\\"and\\\", \\\"subways\\\", \\\",\\\", \\\"and\\\", \\\"several\\\", \\\"major\\\", \\\"highways\\\", \\\".\\\"], \\\"h\\\": [\\\"airports\\\", \\\"Q937590\\\", [[12]]], \\\"t\\\": [\\\"long island\\\", \\\"Q18438\\\", [[6, 7]]]}, {\\\"tokens\\\": [\\\"While\\\", \\\"owned\\\", \\\"by\\\", \\\"Jenista\\\", \\\"the\\\", \\\"aircraft\\\", \\\"was\\\", \\\"destroyed\\\", \\\"in\\\", \\\"an\\\", \\\"accident\\\", \\\"on\\\", \\\"11\\\", \\\"June\\\", \\\"1994\\\", \\\"at\\\", \\\"the\\\", \\\"Jean\\\", \\\"Airport\\\", \\\"in\\\", \\\"Jean\\\", \\\",\\\", \\\"Nevada\\\", \\\".\\\"], \\\"h\\\": [\\\"jean airport\\\", \\\"Q2901394\\\", [[17, 18]]], \\\"t\\\": [\\\"jean, nevada\\\", \\\"Q3709757\\\", [[20, 21, 22]]]}, {\\\"tokens\\\": [\\\"Like\\\", \\\"the\\\", \\\"rest\\\", \\\"of\\\", \\\"the\\\", \\\"island\\\", \\\"of\\\", \\\"Trinidad\\\", \\\",\\\", \\\"Port\\\", \\\"of\\\", \\\"Spain\\\", \\\"is\\\", \\\"served\\\", \\\"by\\\", \\\"the\\\", \\\"Piarco\\\", \\\"International\\\", \\\"Airport\\\", \\\"located\\\", \\\"in\\\", \\\"Piarco\\\", \\\",\\\", \\\"approximately\\\", \\\"east\\\", \\\"of\\\", \\\"Port\\\", \\\"of\\\", \\\"Spain\\\", \\\".\\\"], \\\"h\\\": [\\\"piarco international airport\\\", \\\"Q788810\\\", [[16, 17, 18]]], \\\"t\\\": [\\\"port of spain\\\", \\\"Q39178\\\", [[9, 10, 11], [26, 27, 28]]]}, {\\\"tokens\\\": [\\\"The\\\", \\\"nearest\\\", \\\"commercial\\\", \\\"airline\\\", \\\"airports\\\", \\\"are\\\", \\\"Alpena\\\", \\\"County\\\", \\\"Regional\\\", \\\"Airport\\\", \\\"and\\\", \\\"Cherry\\\", \\\"Capital\\\", \\\"Airport\\\", \\\"(\\\", \\\"Traverse\\\", \\\"City\\\", \\\")\\\", \\\".\\\"], \\\"h\\\": [\\\"cherry capital airport\\\", \\\"Q1433080\\\", [[11, 12, 13]]], \\\"t\\\": [\\\"traverse city\\\", \\\"Q984544\\\", [[15, 16]]]}, {\\\"tokens\\\": [\\\"General\\\", \\\"aviation\\\", \\\"airports\\\", \\\"include\\\", \\\"Camarillo\\\", \\\"Airport\\\", \\\",\\\", \\\"approximately\\\", \\\"west\\\", \\\"of\\\", \\\"the\\\", \\\"city\\\", \\\";\\\", \\\"Oxnard\\\", \\\"Airport\\\", \\\",\\\", \\\"approximately\\\", \\\"west\\\", \\\"of\\\", \\\"the\\\", \\\"city\\\", \\\"in\\\", \\\"Oxnard\\\", \\\",\\\", \\\"California\\\", \\\";\\\", \\\"and\\\", \\\"Van\\\", \\\"Nuys\\\", \\\"Airport\\\", \\\",\\\", \\\"east\\\", \\\"of\\\", \\\"the\\\", \\\"city\\\", \\\".\\\"], \\\"h\\\": [\\\"oxnard airport\\\", \\\"Q7115707\\\", [[13, 14]]], \\\"t\\\": [\\\"oxnard, california\\\", \\\"Q209338\\\", [[22, 23, 24]]]}, {\\\"tokens\\\": [\\\"AAI\\\", \\\"had\\\", \\\"earlier\\\", \\\"estimated\\\", \\\"a\\\", \\\"requirement\\\", \\\"of\\\", \\\"600\\\", \\\"acres\\\", \\\"of\\\", \\\"land\\\", \\\"for\\\", \\\"the\\\", \\\"first\\\", \\\"Phase\\\", \\\"and\\\", \\\"another\\\", \\\"790\\\", \\\"acres\\\", \\\"for\\\", \\\"the\\\", \\\"second\\\", \\\"Phase\\\", \\\"in\\\", \\\"lieu\\\", \\\"of\\\", \\\"the\\\", \\\"existing\\\", \\\"Jay\\\", \\\"Prakash\\\", \\\"Narayan\\\", \\\"International\\\", \\\"Airport\\\", \\\"in\\\", \\\"Patna\\\", \\\".\\\"], \\\"h\\\": [\\\"jay prakash narayan international airport\\\", \\\"Q2673010\\\", [[28, 29, 30, 31, 32]]], \\\"t\\\": [\\\"patna\\\", \\\"Q80484\\\", [[34]]]}, {\\\"tokens\\\": [\\\"Pune\\\", \\\"International\\\", \\\"Airport\\\", \\\"(\\\", \\\"IATA\\\", \\\":\\\", \\\"PNQ\\\", \\\")\\\", \\\"is\\\", \\\"a\\\", \\\"civil\\\", \\\"enclave\\\", \\\"located\\\", \\\"at\\\", \\\"Lohegaon\\\", \\\"Air\\\", \\\"Base\\\", \\\",\\\", \\\"northeast\\\", \\\"of\\\", \\\"Pune\\\", \\\"city\\\", \\\".\\\"], \\\"h\\\": [\\\"pnq\\\", \\\"Q1432525\\\", [[6]]], \\\"t\\\": [\\\"pune\\\", \\\"Q1538\\\", [[0], [20]]]}, {\\\"tokens\\\": [\\\"Presently\\\", \\\",\\\", \\\"the\\\", \\\"airport\\\", \\\"serving\\\", \\\"Araraquara\\\", \\\",\\\", \\\"Brazil\\\", \\\"is\\\", \\\"named\\\", \\\"Bartolomeu\\\", \\\"de\\\", \\\"Gusm\\\\u00e3o\\\", \\\"Airport\\\", \\\".\\\"], \\\"h\\\": [\\\"bartolomeu de gusm\\\\u00e3o airport\\\", \\\"Q4784257\\\", [[10, 11, 12, 13]]], \\\"t\\\": [\\\"araraquara\\\", \\\"Q626247\\\", [[5]]]}, {\\\"tokens\\\": [\\\"Phu\\\", \\\"Bai\\\", \\\"International\\\", \\\"Airport\\\", \\\",\\\", \\\"the\\\", \\\"largest\\\", \\\"domestic\\\", \\\"airport\\\", \\\"in\\\", \\\"terms\\\", \\\"of\\\", \\\"passengers\\\", \\\"per\\\", \\\"year\\\", \\\"is\\\", \\\"situated\\\", \\\"15\\\", \\\"\\\\u00a0\\\", \\\"km\\\", \\\"south\\\", \\\"of\\\", \\\"Hu\\\\u1ebf\\\", \\\".\\\"], \\\"h\\\": [\\\"phu bai international airport\\\", \\\"Q160094\\\", [[0, 1, 2, 3]]], \\\"t\\\": [\\\"hu\\\\u1ebf\\\", \\\"Q36167\\\", [[22]]]}, {\\\"tokens\\\": [\\\"In\\\", \\\"the\\\", \\\"1970s\\\", \\\",\\\", \\\"the\\\", \\\"original\\\", \\\"airport\\\", \\\"in\\\", \\\"Taipei\\\", \\\"City\\\", \\\"\\\\u2014\\\", \\\"Taipei\\\", \\\"Songshan\\\", \\\"Airport\\\", \\\"\\\\u2014\\\", \\\"had\\\", \\\"become\\\", \\\"overcrowded\\\", \\\"and\\\", \\\"could\\\", \\\"not\\\", \\\"be\\\", \\\"expanded\\\", \\\"due\\\", \\\"to\\\", \\\"space\\\", \\\"limitations\\\", \\\".\\\"], \\\"h\\\": [\\\"taipei songshan airport\\\", \\\"Q702019\\\", [[11, 12, 13]]], \\\"t\\\": [\\\"taipei city\\\", \\\"Q1867\\\", [[8, 9]]]}, {\\\"tokens\\\": [\\\"The\\\", \\\"Mid\\\", \\\"-\\\", \\\"America\\\", \\\"Air\\\", \\\"Museum\\\", \\\"is\\\", \\\"in\\\", \\\"southwest\\\", \\\"Kansas\\\", \\\",\\\", \\\"in\\\", \\\"Liberal\\\", \\\",\\\", \\\"Kansas\\\", \\\",\\\", \\\"at\\\", \\\"the\\\", \\\"Liberal\\\", \\\"Mid\\\", \\\"-\\\", \\\"America\\\", \\\"Regional\\\", \\\"Airport\\\", \\\",\\\", \\\"near\\\", \\\"U.S.\\\", \\\"Highway\\\", \\\"54\\\", \\\".\\\"], \\\"h\\\": [\\\"liberal mid-america regional airport\\\", \\\"Q6540690\\\", [[18, 19, 20, 21, 22, 23]]], \\\"t\\\": [\\\"liberal, kansas\\\", \\\"Q1003630\\\", [[12, 13, 14]]]}, {\\\"tokens\\\": [\\\"It\\\", \\\"broadcasts\\\", \\\"from\\\", \\\"the\\\", \\\"former\\\", \\\"KDLH\\\", \\\"tower\\\", \\\"on\\\", \\\"Duluth\\\", \\\"'s\\\", \\\"Observation\\\", \\\"Hill\\\", \\\".\\\"], \\\"h\\\": [\\\"kdlh\\\", \\\"Q3277758\\\", [[5]]], \\\"t\\\": [\\\"duluth\\\", \\\"Q485708\\\", [[8]]]}, {\\\"tokens\\\": [\\\"The\\\", \\\"closest\\\", \\\"airports\\\", \\\"are\\\", \\\"Chandigarh\\\", \\\"International\\\", \\\"Airport\\\", \\\",\\\", \\\"located\\\", \\\"away\\\", \\\",\\\", \\\"and\\\", \\\"Sri\\\", \\\"Guru\\\", \\\"Ram\\\", \\\"Dass\\\", \\\"Jee\\\", \\\"International\\\", \\\"Airport\\\", \\\",\\\", \\\"away\\\", \\\"in\\\", \\\"the\\\", \\\"city\\\", \\\"of\\\", \\\"Amritsar\\\", \\\".\\\"], \\\"h\\\": [\\\"sri guru ram dass jee international airport\\\", \\\"Q385356\\\", [[12, 13, 14, 15, 16, 17, 18]]], \\\"t\\\": [\\\"amritsar\\\", \\\"Q48403\\\", [[25]]]}, {\\\"tokens\\\": [\\\"The\\\", \\\"A-23\\\", \\\"Arusha\\\", \\\"-\\\", \\\"Himo\\\", \\\"road\\\", \\\"runs\\\", \\\"east\\\", \\\"-\\\", \\\"west\\\", \\\"and\\\", \\\"enters\\\", \\\"the\\\", \\\"region\\\", \\\"near\\\", \\\"Kilimanjaro\\\", \\\"International\\\", \\\"Airport\\\", \\\".\\\"], \\\"h\\\": [\\\"kilimanjaro international airport\\\", \\\"Q1365099\\\", [[15, 16, 17]]], \\\"t\\\": [\\\"arusha\\\", \\\"Q4301\\\", [[2]]]}, {\\\"tokens\\\": [\\\"Taravella\\\", \\\"International\\\", \\\"Airport\\\", \\\",\\\", \\\"C\\\\u00f3rdoba\\\", \\\",\\\", \\\"to\\\", \\\"General\\\", \\\"Enrique\\\", \\\"Mosconi\\\", \\\"International\\\", \\\"Airport\\\", \\\",\\\", \\\"Comodoro\\\", \\\"Rivadavia\\\", \\\",\\\", \\\"with\\\", \\\"stopovers\\\", \\\"at\\\", \\\"Governor\\\", \\\"Francisco\\\", \\\"Gabrielli\\\", \\\"International\\\", \\\"Airport\\\", \\\",\\\", \\\"Mendoza\\\", \\\",\\\", \\\"and\\\", \\\"Presidente\\\", \\\"Per\\\\u00f3n\\\", \\\"International\\\", \\\"Airport\\\", \\\",\\\", \\\"Neuqu\\\\u00e9n\\\", \\\".\\\"], \\\"h\\\": [\\\"governor francisco gabrielli international airport\\\", \\\"Q1432029\\\", [[19, 20, 21, 22, 23]]], \\\"t\\\": [\\\"mendoza\\\", \\\"Q44237\\\", [[25]]]}, {\\\"tokens\\\": [\\\"The\\\", \\\"London\\\", \\\"qualifying\\\", \\\"competition\\\", \\\",\\\", \\\"the\\\", \\\"British\\\", \\\"Open\\\", \\\",\\\", \\\"was\\\", \\\"held\\\", \\\"August\\\", \\\"2011\\\", \\\"in\\\", \\\"Heathrow\\\", \\\"at\\\", \\\"Stoke\\\", \\\"Mandeville\\\", \\\",\\\", \\\"with\\\", \\\"Rudio\\\", \\\"competing\\\", \\\"to\\\", \\\"try\\\", \\\"to\\\", \\\"earn\\\", \\\"Spain\\\", \\\"one\\\", \\\"of\\\", \\\"the\\\", \\\"twenty\\\", \\\"qualifying\\\", \\\"sports\\\", \\\"on\\\", \\\"offer\\\", \\\".\\\"], \\\"h\\\": [\\\"heathrow\\\", \\\"Q8691\\\", [[14]]], \\\"t\\\": [\\\"london\\\", \\\"Q84\\\", [[1]]]}, {\\\"tokens\\\": [\\\"Breeder\\\", \\\"George\\\", \\\"Brunacini\\\", \\\"was\\\", \\\"notably\\\", \\\"killed\\\", \\\"in\\\", \\\"the\\\", \\\"August\\\", \\\"27\\\", \\\",\\\", \\\"2006\\\", \\\",\\\", \\\"crash\\\", \\\"of\\\", \\\"Comair\\\", \\\"Flight\\\", \\\"5191\\\", \\\"at\\\", \\\"Blue\\\", \\\"Grass\\\", \\\"Airport\\\", \\\"in\\\", \\\"Lexington\\\", \\\",\\\", \\\"Kentucky\\\", \\\".\\\"], \\\"h\\\": [\\\"blue grass airport\\\", \\\"Q598259\\\", [[19, 20, 21]]], \\\"t\\\": [\\\"lexington, kentucky\\\", \\\"Q49241\\\", [[23, 24, 25]]]}, {\\\"tokens\\\": [\\\"Aeroflot\\\", \\\"Flight\\\", \\\"498\\\", \\\"was\\\", \\\"originally\\\", \\\"scheduled\\\", \\\"to\\\", \\\"fly\\\", \\\"from\\\", \\\"Severomuysk\\\", \\\"to\\\", \\\"Baikal\\\", \\\"International\\\", \\\"Airport\\\", \\\"in\\\", \\\"Ulan\\\", \\\"-\\\", \\\"Ude\\\", \\\",\\\", \\\"with\\\", \\\"a\\\", \\\"planned\\\", \\\"en\\\", \\\"-\\\", \\\"route\\\", \\\"stop\\\", \\\"at\\\", \\\"Nizhneangarsk\\\", \\\"Airport\\\", \\\"in\\\", \\\"Nizhneangarsk\\\", \\\".\\\"], \\\"h\\\": [\\\"baikal international airport\\\", \\\"Q2719346\\\", [[11, 12, 13]]], \\\"t\\\": [\\\"ulan-ude\\\", \\\"Q6816\\\", [[15, 16, 17]]]}, {\\\"tokens\\\": [\\\"Kbely\\\", \\\"Airport\\\", \\\"was\\\", \\\"built\\\", \\\"in\\\", \\\"1918\\\", \\\"and\\\", \\\"was\\\", \\\"Prague\\\", \\\"'s\\\", \\\"only\\\", \\\"airport\\\", \\\"until\\\", \\\"the\\\", \\\"construction\\\", \\\"of\\\", \\\"Ruzyn\\\\u011b\\\", \\\"Airport\\\", \\\"in\\\", \\\"1937\\\", \\\",\\\", \\\"on\\\", \\\"the\\\", \\\"northwest\\\", \\\"side\\\", \\\"of\\\", \\\"the\\\", \\\"city\\\", \\\".\\\"], \\\"h\\\": [\\\"kbely airport\\\", \\\"Q1935013\\\", [[0, 1]]], \\\"t\\\": [\\\"prague\\\", \\\"Q1085\\\", [[8]]]}, {\\\"tokens\\\": [\\\"Bikini\\\", \\\"Atoll\\\", \\\"Airport\\\", \\\",\\\", \\\"also\\\", \\\"known\\\", \\\"as\\\", \\\"Enyu\\\", \\\"Airfield\\\", \\\",\\\", \\\"is\\\", \\\"a\\\", \\\"public\\\", \\\"use\\\", \\\"airstrip\\\", \\\"at\\\", \\\"Enyu\\\", \\\"on\\\", \\\"Bikini\\\", \\\"Atoll\\\", \\\",\\\", \\\"Marshall\\\", \\\"Islands\\\", \\\".\\\"], \\\"h\\\": [\\\"enyu airfield\\\", \\\"Q598311\\\", [[7, 8]]], \\\"t\\\": [\\\"bikini atoll\\\", \\\"Q152225\\\", [[0, 1], [18, 19]]]}, {\\\"tokens\\\": [\\\"Retrieved\\\", \\\"on\\\", \\\"January\\\", \\\"26\\\", \\\",\\\", \\\"2011\\\", \\\".\\\", \\\"operating\\\", \\\"as\\\", \\\"Aerol\\\\u00ednea\\\", \\\"de\\\", \\\"Antioquia\\\", \\\"(\\\", \\\"ADA\\\", \\\")\\\", \\\",\\\", \\\"is\\\", \\\"a\\\", \\\"regional\\\", \\\"airline\\\", \\\"with\\\", \\\"its\\\", \\\"headquarters\\\", \\\"on\\\", \\\"the\\\", \\\"property\\\", \\\"of\\\", \\\"Olaya\\\", \\\"Herrera\\\", \\\"Airport\\\", \\\"in\\\", \\\"Medell\\\\u00edn\\\", \\\",\\\", \\\"Colombia\\\", \\\".\\\"], \\\"h\\\": [\\\"olaya herrera airport\\\", \\\"Q1431257\\\", [[27, 28, 29]]], \\\"t\\\": [\\\"medell\\\\u00edn\\\", \\\"Q48278\\\", [[31]]]}, {\\\"tokens\\\": [\\\"Littlefield\\\", \\\"Municipal\\\", \\\"Airport\\\", \\\"is\\\", \\\"located\\\", \\\"in\\\", \\\"Lamb\\\", \\\"County\\\", \\\",\\\", \\\"three\\\", \\\"nautical\\\", \\\"miles\\\", \\\"(\\\", \\\"6\\\", \\\"\\\\u00a0\\\", \\\"km\\\", \\\")\\\", \\\"west\\\", \\\"of\\\", \\\"the\\\", \\\"central\\\", \\\"business\\\", \\\"district\\\", \\\"of\\\", \\\"Littlefield\\\", \\\",\\\", \\\"Texas\\\", \\\".\\\"], \\\"h\\\": [\\\"littlefield municipal airport\\\", \\\"Q6652959\\\", [[0, 1, 2]]], \\\"t\\\": [\\\"littlefield, texas\\\", \\\"Q202736\\\", [[24, 25, 26]]]}, {\\\"tokens\\\": [\\\"Capit\\\\u00e1n\\\", \\\"Germ\\\\u00e1n\\\", \\\"Quiroga\\\", \\\"Guardia\\\", \\\"Airport\\\", \\\"is\\\", \\\"an\\\", \\\"airport\\\", \\\"serving\\\", \\\"San\\\", \\\"Borja\\\", \\\",\\\", \\\"a\\\", \\\"town\\\", \\\"in\\\", \\\"the\\\", \\\"Beni\\\", \\\"Department\\\", \\\"of\\\", \\\"Bolivia\\\", \\\".\\\"], \\\"h\\\": [\\\"capit\\\\u00e1n germ\\\\u00e1n quiroga guardia airport\\\", \\\"Q2875720\\\", [[0, 1, 2, 3, 4]]], \\\"t\\\": [\\\"san borja\\\", \\\"Q2307472\\\", [[9, 10]]]}, {\\\"tokens\\\": [\\\"Moses\\\", \\\"Point\\\", \\\"Airport\\\", \\\"is\\\", \\\"an\\\", \\\"airport\\\", \\\"located\\\", \\\"in\\\", \\\"Elim\\\", \\\",\\\", \\\"a\\\", \\\"city\\\", \\\"in\\\", \\\"the\\\", \\\"Nome\\\", \\\"Census\\\", \\\"Area\\\", \\\"of\\\", \\\"the\\\", \\\"U.S.\\\", \\\"state\\\", \\\"of\\\", \\\"Alaska\\\", \\\".\\\"], \\\"h\\\": [\\\"moses point airport\\\", \\\"Q3886700\\\", [[0, 1, 2]]], \\\"t\\\": [\\\"elim\\\", \\\"Q79557\\\", [[8]]]}, {\\\"tokens\\\": [\\\"It\\\", \\\"is\\\", \\\"under\\\", \\\"the\\\", \\\"administration\\\", \\\"of\\\", \\\"Haixi\\\", \\\"Mongol\\\", \\\"and\\\", \\\"Tibetan\\\", \\\"Autonomous\\\", \\\"Prefecture\\\", \\\".The\\\", \\\"Huatugou\\\", \\\"Airport\\\", \\\"is\\\", \\\"located\\\", \\\"in\\\", \\\"Mangnai\\\", \\\".\\\"], \\\"h\\\": [\\\"huatugou airport\\\", \\\"Q3207552\\\", [[13, 14]]], \\\"t\\\": [\\\"mangnai\\\", \\\"Q1201941\\\", [[18]]]}, {\\\"tokens\\\": [\\\"Kulob\\\", \\\"Airport\\\", \\\"or\\\", \\\"Kulyab\\\", \\\"Airport\\\", \\\"is\\\", \\\"an\\\", \\\"airport\\\", \\\"serving\\\", \\\"Kulob\\\", \\\"(\\\", \\\"also\\\", \\\"spelled\\\", \\\"Kulyab\\\", \\\")\\\", \\\",\\\", \\\"a\\\", \\\"city\\\", \\\"in\\\", \\\"the\\\", \\\"Khatlon\\\", \\\"province\\\", \\\"in\\\", \\\"Tajikistan\\\", \\\".\\\"], \\\"h\\\": [\\\"kulyab airport\\\", \\\"Q2231909\\\", [[3, 4]]], \\\"t\\\": [\\\"kulob\\\", \\\"Q132043\\\", [[0], [9]]]}, {\\\"tokens\\\": [\\\"Most\\\", \\\"trains\\\", \\\"from\\\", \\\"the\\\", \\\"Gold\\\", \\\"Coast\\\", \\\"run\\\", \\\"through\\\", \\\"to\\\", \\\"Brisbane\\\", \\\"Airport\\\", \\\",\\\", \\\"allowing\\\", \\\"tourists\\\", \\\"and\\\", \\\"locals\\\", \\\"access\\\", \\\"to\\\", \\\"more\\\", \\\"international\\\", \\\"destinations\\\", \\\"than\\\", \\\"from\\\", \\\"the\\\", \\\"Gold\\\", \\\"Coast\\\", \\\"'s\\\", \\\"own\\\", \\\"airport\\\", \\\".\\\"], \\\"h\\\": [\\\"own airport\\\", \\\"Q1175431\\\", [[27, 28]]], \\\"t\\\": [\\\"gold coast\\\", \\\"Q140075\\\", [[4, 5], [24, 25]]]}, {\\\"tokens\\\": [\\\"Soledad\\\", \\\"International\\\", \\\"Airport\\\", \\\"was\\\", \\\"the\\\", \\\"main\\\", \\\"airport\\\", \\\"of\\\", \\\"Barranquilla\\\", \\\",\\\", \\\"Colombia\\\", \\\"from\\\", \\\"1936\\\", \\\"to\\\", \\\"1981\\\", \\\"when\\\", \\\"it\\\", \\\"was\\\", \\\"replaced\\\", \\\"by\\\", \\\"Ernesto\\\", \\\"Cortissoz\\\", \\\"International\\\", \\\"Airport\\\", \\\".\\\"], \\\"h\\\": [\\\"ernesto cortissoz international airport\\\", \\\"Q645151\\\", [[20, 21, 22, 23]]], \\\"t\\\": [\\\"barranquilla\\\", \\\"Q62823\\\", [[8]]]}, {\\\"tokens\\\": [\\\"Hubs\\\", \\\"of\\\", \\\"Panalpina\\\", \\\"are\\\", \\\"situated\\\", \\\"in\\\", \\\"Luxembourg\\\", \\\",\\\", \\\"at\\\", \\\"Findel\\\", \\\"Airport\\\", \\\",\\\", \\\"Prague\\\", \\\"and\\\", \\\"in\\\", \\\"Huntsville\\\", \\\",\\\", \\\"Alabama\\\", \\\",\\\", \\\"at\\\", \\\"Huntsville\\\", \\\"International\\\", \\\"Airport\\\", \\\".\\\"], \\\"h\\\": [\\\"huntsville international airport\\\", \\\"Q2213419\\\", [[20, 21, 22]]], \\\"t\\\": [\\\"huntsville, alabama\\\", \\\"Q79860\\\", [[15, 16, 17]]]}, {\\\"tokens\\\": [\\\"Maota\\\", \\\"Airport\\\", \\\"is\\\", \\\"the\\\", \\\"main\\\", \\\"airfield\\\", \\\"on\\\", \\\"the\\\", \\\"island\\\", \\\",\\\", \\\"located\\\", \\\"10\\\", \\\"minutes\\\", \\\"south\\\", \\\"of\\\", \\\"Salelologa\\\", \\\".\\\"], \\\"h\\\": [\\\"maota airport\\\", \\\"Q1030546\\\", [[0, 1]]], \\\"t\\\": [\\\"salelologa\\\", \\\"Q2214151\\\", [[15]]]}, {\\\"tokens\\\": [\\\"This\\\", \\\"new\\\", \\\"airport\\\", \\\"for\\\", \\\"West\\\", \\\"Java\\\", \\\"is\\\", \\\"set\\\", \\\"to\\\", \\\"replace\\\", \\\"the\\\", \\\"current\\\", \\\"airport\\\", \\\"in\\\", \\\"Bandung\\\", \\\",\\\", \\\"and\\\", \\\"is\\\", \\\"named\\\", \\\"\\\\\\\"\\\", \\\"Kertajati\\\", \\\"International\\\", \\\"Airport\\\", \\\"\\\\\\\"\\\", \\\".\\\"], \\\"h\\\": [\\\"kertajati international airport\\\", \\\"Q889070\\\", [[20, 21, 22]]], \\\"t\\\": [\\\"west java\\\", \\\"Q3724\\\", [[4, 5]]]}, {\\\"tokens\\\": [\\\"In\\\", \\\"2018\\\", \\\",\\\", \\\"Commercial\\\", \\\"Flight\\\", \\\"Again\\\", \\\"Started\\\", \\\"at\\\", \\\"Sonari\\\", \\\"Airport\\\", \\\"In\\\", \\\"Jamshedpur\\\", \\\".\\\"], \\\"h\\\": [\\\"sonari airport\\\", \\\"Q7560814\\\", [[8, 9]]], \\\"t\\\": [\\\"jamshedpur\\\", \\\"Q200054\\\", [[11]]]}, {\\\"tokens\\\": [\\\"Parna\\\\u00edba\\\", \\\"has\\\", \\\"an\\\", \\\"international\\\", \\\"airport\\\", \\\"with\\\", \\\"a\\\", \\\"runway\\\", \\\"of\\\", \\\"2500\\\", \\\"m\\\", \\\".\\\"], \\\"h\\\": [\\\"an international airport\\\", \\\"Q6587028\\\", [[2, 3, 4]]], \\\"t\\\": [\\\"parna\\\\u00edba\\\", \\\"Q1643864\\\", [[0]]]}, {\\\"tokens\\\": [\\\"It\\\", \\\"was\\\", \\\"further\\\", \\\"planned\\\", \\\"to\\\", \\\"fly\\\", \\\"them\\\", \\\"to\\\", \\\"Copenhagen\\\", \\\"from\\\", \\\"Damascus\\\", \\\"'s\\\", \\\"international\\\", \\\"airport\\\", \\\".\\\"], \\\"h\\\": [\\\"international airport\\\", \\\"Q570873\\\", [[12, 13]]], \\\"t\\\": [\\\"damascus\\\", \\\"Q3766\\\", [[10]]]}, {\\\"tokens\\\": [\\\"The\\\", \\\"district\\\", \\\"comprises\\\", \\\"Tob\\\\u00edas\\\", \\\"Bola\\\\u00f1os\\\", \\\"International\\\", \\\"Airport\\\", \\\",\\\", \\\"San\\\", \\\"Jos\\\\u00e9\\\", \\\"'s\\\", \\\"domestic\\\", \\\"airport\\\", \\\".\\\"], \\\"h\\\": [\\\"tob\\\\u00edas bola\\\\u00f1os international airport\\\", \\\"Q3500191\\\", [[3, 4, 5, 6]]], \\\"t\\\": [\\\"san jos\\\\u00e9\\\", \\\"Q3070\\\", [[8, 9]]]}, {\\\"tokens\\\": [\\\"Stands\\\", \\\"were\\\", \\\"specially\\\", \\\"erected\\\", \\\"for\\\", \\\"him\\\", \\\"at\\\", \\\"Luis\\\", \\\"Mu\\\\u00f1oz\\\", \\\"Mar\\\\u00edn\\\", \\\"International\\\", \\\"Airport\\\", \\\"in\\\", \\\"San\\\", \\\"Juan\\\", \\\",\\\", \\\"where\\\", \\\"he\\\", \\\"met\\\", \\\"with\\\", \\\"governor\\\", \\\"Carlos\\\", \\\"Romero\\\", \\\"Barcel\\\\u00f3\\\", \\\",\\\", \\\"and\\\", \\\"at\\\", \\\"Plaza\\\", \\\"Las\\\", \\\"Americas\\\", \\\".\\\"], \\\"h\\\": [\\\"luis mu\\\\u00f1oz mar\\\\u00edn international airport\\\", \\\"Q1360523\\\", [[7, 8, 9, 10, 11]]], \\\"t\\\": [\\\"san juan\\\", \\\"Q41211\\\", [[13, 14]]]}, {\\\"tokens\\\": [\\\"Monterrey\\\", \\\"International\\\", \\\"Airport\\\", \\\",\\\", \\\"(\\\", \\\")\\\", \\\";\\\", \\\"ceremonial\\\", \\\"name\\\", \\\"General\\\", \\\"Mariano\\\", \\\"Escobedo\\\", \\\"International\\\", \\\"Airport\\\", \\\",\\\", \\\"is\\\", \\\"an\\\", \\\"international\\\", \\\"airport\\\", \\\"located\\\", \\\"in\\\", \\\"Apodaca\\\", \\\",\\\", \\\"Nuevo\\\", \\\"Le\\\\u00f3n\\\", \\\",\\\", \\\"Mexico\\\", \\\".\\\"], \\\"h\\\": [\\\"general mariano escobedo international airport\\\", \\\"Q767660\\\", [[9, 10, 11, 12, 13]]], \\\"t\\\": [\\\"monterrey\\\", \\\"Q81033\\\", [[0]]]}, {\\\"tokens\\\": [\\\"Msalato\\\", \\\"International\\\", \\\"Airport\\\", \\\"(\\\", \\\")\\\", \\\"is\\\", \\\"a\\\", \\\"proposed\\\", \\\"international\\\", \\\"airport\\\", \\\"intended\\\", \\\"to\\\", \\\"serve\\\", \\\"the\\\", \\\"Tanzanian\\\", \\\"capital\\\", \\\"of\\\", \\\"Dodoma\\\", \\\".\\\"], \\\"h\\\": [\\\"msalato international airport\\\", \\\"Q16895494\\\", [[0, 1, 2]]], \\\"t\\\": [\\\"dodoma\\\", \\\"Q3866\\\", [[17]]]}, {\\\"tokens\\\": [\\\"The\\\", \\\"aircraft\\\", \\\"involved\\\", \\\",\\\", \\\"an\\\", \\\"Antonov\\\", \\\"An-24\\\", \\\",\\\", \\\"was\\\", \\\"operating\\\", \\\"Angara\\\", \\\"Airlines\\\", \\\"'\\\", \\\"scheduled\\\", \\\"domestic\\\", \\\"service\\\", \\\"from\\\", \\\"Bogashevo\\\", \\\"Airport\\\", \\\",\\\", \\\"Tomsk\\\", \\\"to\\\", \\\"Surgut\\\", \\\"International\\\", \\\"Airport\\\", \\\",\\\", \\\"Surgut\\\", \\\".\\\"], \\\"h\\\": [\\\"bogashevo airport\\\", \\\"Q1322435\\\", [[17, 18]]], \\\"t\\\": [\\\"tomsk\\\", \\\"Q976\\\", [[20]]]}, {\\\"tokens\\\": [\\\"(\\\", \\\"IATA\\\", \\\"assigned\\\", \\\"PJC\\\", \\\"to\\\", \\\"Pedro\\\", \\\"Juan\\\", \\\"Caballero\\\", \\\"Airport\\\", \\\"in\\\", \\\"Pedro\\\", \\\"Juan\\\", \\\"Caballero\\\", \\\",\\\", \\\"Paraguay\\\", \\\".\\\"], \\\"h\\\": [\\\"pedro juan caballero airport\\\", \\\"Q1657937\\\", [[5, 6, 7, 8]]], \\\"t\\\": [\\\"pedro juan caballero, paraguay\\\", \\\"Q849292\\\", [[10, 11, 12, 13, 14]]]}, {\\\"tokens\\\": [\\\"This\\\", \\\"is\\\", \\\"approximately\\\", \\\",\\\", \\\"by\\\", \\\"air\\\", \\\",\\\", \\\"northeast\\\", \\\"of\\\", \\\"Jomo\\\", \\\"Kenyatta\\\", \\\"International\\\", \\\"Airport\\\", \\\"in\\\", \\\"Nairobi\\\", \\\",\\\", \\\"the\\\", \\\"largest\\\", \\\"civilian\\\", \\\"airport\\\", \\\"in\\\", \\\"the\\\", \\\"country\\\", \\\".\\\"], \\\"h\\\": [\\\"jomo kenyatta international airport\\\", \\\"Q206349\\\", [[9, 10, 11, 12]]], \\\"t\\\": [\\\"nairobi\\\", \\\"Q3870\\\", [[14]]]}, {\\\"tokens\\\": [\\\"In\\\", \\\"San\\\", \\\"Pedro\\\", \\\"Sula\\\", \\\"in\\\", \\\"northwestern\\\", \\\"Honduras\\\", \\\",\\\", \\\"flooding\\\", \\\"covered\\\", \\\"several\\\", \\\"neighborhoods\\\", \\\"and\\\", \\\"the\\\", \\\"international\\\", \\\"airport\\\", \\\".\\\"], \\\"h\\\": [\\\"international airport\\\", \\\"Q2308399\\\", [[14, 15]]], \\\"t\\\": [\\\"san pedro sula\\\", \\\"Q274584\\\", [[1, 2, 3]]]}, {\\\"tokens\\\": [\\\"Hill\\\", \\\"had\\\", \\\"left\\\", \\\"his\\\", \\\"luggage\\\", \\\"at\\\", \\\"Lee\\\", \\\"Bird\\\", \\\"Field\\\", \\\"Airport\\\", \\\"in\\\", \\\"North\\\", \\\"Platte\\\", \\\",\\\", \\\"Nebraska\\\", \\\",\\\", \\\"containing\\\", \\\"drug\\\", \\\"paraphernalia\\\", \\\",\\\", \\\"glass\\\", \\\"tubes\\\", \\\"with\\\", \\\"cocaine\\\", \\\"and\\\", \\\"methamphetamine\\\", \\\"residue\\\", \\\".\\\"], \\\"h\\\": [\\\"lee bird field\\\", \\\"Q7056358\\\", [[6, 7, 8]]], \\\"t\\\": [\\\"north platte, nebraska\\\", \\\"Q989960\\\", [[11, 12, 13, 14]]]}, {\\\"tokens\\\": [\\\"The\\\", \\\"1000\\\", \\\"hectare\\\", \\\"(\\\", \\\"2,472\\\", \\\"acres\\\", \\\")\\\", \\\"site\\\", \\\"is\\\", \\\"located\\\", \\\"12\\\", \\\"kilometers\\\", \\\"from\\\", \\\"Cartagena\\\", \\\"\\\\u2019s\\\", \\\"historic\\\", \\\"old\\\", \\\"city\\\", \\\"and\\\", \\\"8\\\", \\\"kilometers\\\", \\\"from\\\", \\\"Rafael\\\", \\\"N\\\\u00fa\\\\u00f1ez\\\", \\\"International\\\", \\\"Airport\\\", \\\".\\\"], \\\"h\\\": [\\\"rafael n\\\\u00fa\\\\u00f1ez international airport\\\", \\\"Q2670003\\\", [[22, 23, 24, 25]]], \\\"t\\\": [\\\"cartagena\\\", \\\"Q657461\\\", [[13]]]}, {\\\"tokens\\\": [\\\"Retrieved\\\", \\\"2007\\\", \\\"-\\\", \\\"07\\\", \\\"-\\\", \\\"22\\\", \\\".\\\", \\\",\\\", \\\"also\\\", \\\"known\\\", \\\"as\\\", \\\"Easton\\\", \\\"/\\\", \\\"Newnam\\\", \\\"Field\\\", \\\",\\\", \\\"ESN\\\", \\\"-\\\", \\\"Easton\\\", \\\"/\\\", \\\"Newnam\\\", \\\"Field\\\", \\\"at\\\", \\\"Maryland\\\", \\\"Aviation\\\", \\\"Authority\\\", \\\".\\\"], \\\"h\\\": [\\\"newnam field\\\", \\\"Q5330836\\\", [[13, 14], [20, 21]]], \\\"t\\\": [\\\"easton\\\", \\\"Q754306\\\", [[11], [18]]]}, {\\\"tokens\\\": [\\\"Altman\\\", \\\"was\\\", \\\"given\\\", \\\"clearance\\\", \\\"from\\\", \\\"the\\\", \\\"tower\\\", \\\"at\\\", \\\"Teterboro\\\", \\\"Airport\\\", \\\"in\\\", \\\"Teterboro\\\", \\\",\\\", \\\"New\\\", \\\"Jersey\\\", \\\"at\\\", \\\"11:48\\\", \\\"\\\\u00a0\\\", \\\"a.m.\\\", \\\"to\\\", \\\"take\\\", \\\"off\\\", \\\".\\\"], \\\"h\\\": [\\\"teterboro airport\\\", \\\"Q1433053\\\", [[8, 9]]], \\\"t\\\": [\\\"teterboro, new jersey\\\", \\\"Q936782\\\", [[11, 12, 13, 14]]]}, {\\\"tokens\\\": [\\\"Juan\\\", \\\"Enrique\\\", \\\"Airport\\\", \\\",\\\", \\\"is\\\", \\\"an\\\", \\\"airport\\\", \\\"west\\\", \\\"-\\\", \\\"southwest\\\", \\\"of\\\", \\\"Paine\\\", \\\",\\\", \\\"a\\\", \\\"city\\\", \\\"in\\\", \\\"the\\\", \\\"Santiago\\\", \\\"Metropolitan\\\", \\\"Region\\\", \\\"of\\\", \\\"Chile\\\", \\\".\\\"], \\\"h\\\": [\\\"juan enrique airport\\\", \\\"Q16896327\\\", [[0, 1, 2]]], \\\"t\\\": [\\\"paine\\\", \\\"Q51070\\\", [[11]]]}, {\\\"tokens\\\": [\\\"Burnie\\\", \\\"Airport\\\", \\\",\\\", \\\"also\\\", \\\"called\\\", \\\"Burnie\\\", \\\"Wynyard\\\", \\\"Airport\\\", \\\"or\\\", \\\"Wynyard\\\", \\\"Airport\\\", \\\",\\\", \\\"is\\\", \\\"a\\\", \\\"regional\\\", \\\"airport\\\", \\\"located\\\", \\\"adjacent\\\", \\\"to\\\", \\\"the\\\", \\\"town\\\", \\\"of\\\", \\\"Wynyard\\\", \\\",\\\", \\\"about\\\", \\\"west\\\", \\\"from\\\", \\\"Burnie\\\", \\\",\\\", \\\"Tasmania\\\", \\\",\\\", \\\"Australia\\\", \\\".\\\"], \\\"h\\\": [\\\"wynyard airport\\\", \\\"Q15540\\\", [[6, 7], [9, 10]]], \\\"t\\\": [\\\"burnie\\\", \\\"Q175262\\\", [[0], [5], [27]]]}, {\\\"tokens\\\": [\\\"Tirana\\\", \\\"International\\\", \\\"Airport\\\", \\\"N\\\\u00ebn\\\\u00eb\\\", \\\"Tereza\\\", \\\"(\\\", \\\",\\\", \\\")\\\", \\\",\\\", \\\"commonly\\\", \\\"Rinas\\\", \\\"International\\\", \\\"Airport\\\", \\\",\\\", \\\"is\\\", \\\"Albania\\\", \\\"'s\\\", \\\"main\\\", \\\"international\\\", \\\"airport\\\", \\\".\\\"], \\\"h\\\": [\\\"rinas international airport\\\", \\\"Q217226\\\", [[10, 11, 12]]], \\\"t\\\": [\\\"tirana\\\", \\\"Q19689\\\", [[0]]]}, {\\\"tokens\\\": [\\\"Currently\\\", \\\",\\\", \\\"Rach\\\", \\\"Gia\\\", \\\"Airport\\\", \\\"is\\\", \\\"the\\\", \\\"biggest\\\", \\\"airport\\\", \\\"in\\\", \\\"R\\\\u1ea1ch\\\", \\\"Gi\\\\u00e1\\\", \\\".\\\"], \\\"h\\\": [\\\"rach gia airport\\\", \\\"Q1993204\\\", [[2, 3, 4]]], \\\"t\\\": [\\\"r\\\\u1ea1ch gi\\\\u00e1\\\", \\\"Q36093\\\", [[10, 11]]]}, {\\\"tokens\\\": [\\\"\\\\\\\"\\\", \\\"Head\\\", \\\"Office\\\", \\\":\\\", \\\"Aerogem\\\", \\\"Aviation\\\", \\\"Ltd\\\", \\\"1\\\", \\\"Gemini\\\", \\\"Airlines\\\", \\\"Building\\\", \\\",\\\", \\\"Old\\\", \\\"Cargo\\\", \\\"Village\\\", \\\",\\\", \\\"Kotoka\\\", \\\"International\\\", \\\"Airport\\\", \\\"Accra\\\", \\\"\\\\\\\"\\\", \\\"It\\\", \\\"operates\\\", \\\"worldwide\\\", \\\"non\\\", \\\"-\\\", \\\"scheduled\\\", \\\"cargo\\\", \\\"flights\\\", \\\".\\\"], \\\"h\\\": [\\\"kotoka international airport\\\", \\\"Q177689\\\", [[16, 17, 18]]], \\\"t\\\": [\\\"accra\\\", \\\"Q3761\\\", [[19]]]}, {\\\"tokens\\\": [\\\"Madurai\\\", \\\"international\\\", \\\"Airport\\\", \\\"(\\\", \\\"IATA\\\", \\\":\\\", \\\"IXM\\\", \\\",\\\", \\\"ICAO\\\", \\\":\\\", \\\"VOMD\\\", \\\")\\\", \\\"is\\\", \\\"a\\\", \\\"customs\\\", \\\"airport\\\", \\\"serving\\\", \\\"Madurai\\\", \\\"in\\\", \\\"the\\\", \\\"state\\\", \\\"of\\\", \\\"Tamil\\\", \\\"Nadu\\\", \\\".\\\"], \\\"h\\\": [\\\"vomd\\\", \\\"Q3465662\\\", [[10]]], \\\"t\\\": [\\\"madurai\\\", \\\"Q228405\\\", [[0], [17]]]}, {\\\"tokens\\\": [\\\"Its\\\", \\\"main\\\", \\\"base\\\", \\\"is\\\", \\\"Ford\\\", \\\"Airport\\\", \\\"in\\\", \\\"Iron\\\", \\\"Mountain\\\", \\\",\\\", \\\"Michigan\\\", \\\"and\\\", \\\"its\\\", \\\"air\\\", \\\"traffic\\\", \\\"control\\\", \\\"call\\\", \\\"sign\\\", \\\"Iron\\\", \\\"Air\\\", \\\"is\\\", \\\"derived\\\", \\\"from\\\", \\\"that\\\", \\\"city\\\", \\\".\\\"], \\\"h\\\": [\\\"ford airport\\\", \\\"Q5467650\\\", [[4, 5]]], \\\"t\\\": [\\\"iron mountain, michigan\\\", \\\"Q567814\\\", [[7, 8, 9, 10]]]}, {\\\"tokens\\\": [\\\"The\\\", \\\"nearest\\\", \\\"airports\\\", \\\"are\\\", \\\"at\\\", \\\"Poitiers\\\", \\\"(\\\", \\\"Poitiers\\\", \\\"-\\\", \\\"Biard\\\", \\\"Airport\\\", \\\")\\\", \\\"and\\\", \\\"Nantes\\\", \\\"(\\\", \\\"Nantes\\\", \\\"Atlantique\\\", \\\"Airport\\\", \\\")\\\", \\\".\\\"], \\\"h\\\": [\\\"biard airport\\\", \\\"Q1432405\\\", [[9, 10]]], \\\"t\\\": [\\\"poitiers\\\", \\\"Q6616\\\", [[5], [7]]]}, {\\\"tokens\\\": [\\\"Calhoun\\\", \\\"County\\\", \\\"Airport\\\", \\\",\\\", \\\"a\\\", \\\"general\\\", \\\"aviation\\\", \\\"airport\\\", \\\",\\\", \\\"is\\\", \\\"located\\\", \\\"in\\\", \\\"unincorporated\\\", \\\"Calhoun\\\", \\\"County\\\", \\\"northwest\\\", \\\"of\\\", \\\"Port\\\", \\\"Lavaca\\\", \\\".\\\"], \\\"h\\\": [\\\"calhoun county airport\\\", \\\"Q3813482\\\", [[0, 1, 2]]], \\\"t\\\": [\\\"port lavaca\\\", \\\"Q982477\\\", [[17, 18]]]}, {\\\"tokens\\\": [\\\"Governador\\\", \\\"Aluizio\\\", \\\"Alves\\\", \\\"International\\\", \\\"Airport\\\", \\\",\\\", \\\"the\\\", \\\"new\\\", \\\"airport\\\", \\\"that\\\", \\\"serves\\\", \\\"the\\\", \\\"metropolitan\\\", \\\"area\\\", \\\"of\\\", \\\"Natal\\\", \\\",\\\", \\\"was\\\", \\\"opened\\\", \\\"in\\\", \\\"2014\\\", \\\"and\\\", \\\"is\\\", \\\"located\\\", \\\"in\\\", \\\"the\\\", \\\"municipality\\\", \\\".\\\"], \\\"h\\\": [\\\"governador aluizio alves international airport\\\", \\\"Q2090101\\\", [[0, 1, 2, 3, 4]]], \\\"t\\\": [\\\"natal\\\", \\\"Q131620\\\", [[15]]]}, {\\\"tokens\\\": [\\\"Ordos\\\", \\\"Ejin\\\", \\\"Horo\\\", \\\"Airport\\\", \\\"is\\\", \\\"an\\\", \\\"airport\\\", \\\"serving\\\", \\\"Ordos\\\", \\\"City\\\", \\\"in\\\", \\\"China\\\", \\\"'s\\\", \\\"Inner\\\", \\\"Mongolia\\\", \\\"Autonomous\\\", \\\"Region\\\", \\\".\\\"], \\\"h\\\": [\\\"ordos ejin horo airport\\\", \\\"Q3538450\\\", [[0, 1, 2, 3]]], \\\"t\\\": [\\\"ordos city\\\", \\\"Q570937\\\", [[8, 9]]]}, {\\\"tokens\\\": [\\\"Rennell\\\", \\\"/\\\", \\\"Tingoa\\\", \\\"Airport\\\", \\\"is\\\", \\\"an\\\", \\\"airport\\\", \\\"in\\\", \\\"Tigoa\\\", \\\"on\\\", \\\"Rennell\\\", \\\"Island\\\", \\\"in\\\", \\\"the\\\", \\\"Solomon\\\", \\\"Islands\\\", \\\".\\\"], \\\"h\\\": [\\\"tingoa airport\\\", \\\"Q3436133\\\", [[2, 3]]], \\\"t\\\": [\\\"tigoa\\\", \\\"Q987011\\\", [[8]]]}, {\\\"tokens\\\": [\\\"It\\\", \\\"subsequently\\\", \\\"became\\\", \\\"a\\\", \\\"non\\\", \\\"-\\\", \\\"flying\\\", \\\"general\\\", \\\"reserve\\\", \\\"squadron\\\", \\\"headquartered\\\", \\\"at\\\", \\\"RAAF\\\", \\\"Williams\\\", \\\"near\\\", \\\"Melbourne\\\", \\\".\\\"], \\\"h\\\": [\\\"raaf williams\\\", \\\"Q1551483\\\", [[12, 13]]], \\\"t\\\": [\\\"melbourne\\\", \\\"Q3141\\\", [[15]]]}, {\\\"tokens\\\": [\\\"Nearby\\\", \\\"airports\\\", \\\"are\\\", \\\"San\\\", \\\"Pedro\\\", \\\"de\\\", \\\"Atacama\\\", \\\"Airport\\\", \\\"and\\\", \\\"Salar\\\", \\\"de\\\", \\\"Atacama\\\", \\\"Airport\\\", \\\"for\\\", \\\"private\\\", \\\"aircraft\\\", \\\",\\\", \\\"and\\\", \\\"the\\\", \\\"larger\\\", \\\"El\\\", \\\"Loa\\\", \\\"Airport\\\", \\\"/\\\", \\\"Calama\\\", \\\"100\\\", \\\"\\\\u00a0\\\", \\\"km\\\", \\\"away\\\", \\\"for\\\", \\\"scheduled\\\", \\\"aircraft\\\", \\\".\\\"], \\\"h\\\": [\\\"el loa airport\\\", \\\"Q3299637\\\", [[20, 21, 22]]], \\\"t\\\": [\\\"calama\\\", \\\"Q3685\\\", [[24]]]}, {\\\"tokens\\\": [\\\"The\\\", \\\"first\\\", \\\"community\\\", \\\"it\\\", \\\"enters\\\", \\\"is\\\", \\\"Grant\\\", \\\"-\\\", \\\"Valkaria\\\", \\\",\\\", \\\"with\\\", \\\"intersections\\\", \\\"with\\\", \\\"Micco\\\", \\\"Road\\\", \\\",\\\", \\\"followed\\\", \\\"by\\\", \\\"Valkaria\\\", \\\"Road\\\", \\\"just\\\", \\\"east\\\", \\\"of\\\", \\\"the\\\", \\\"Valkaria\\\", \\\"Airport\\\", \\\".\\\"], \\\"h\\\": [\\\"valkaria airport\\\", \\\"Q7911753\\\", [[24, 25]]], \\\"t\\\": [\\\"grant-valkaria\\\", \\\"Q2154617\\\", [[6, 7, 8]]]}, {\\\"tokens\\\": [\\\"However\\\", \\\",\\\", \\\"the\\\", \\\"company\\\", \\\"'s\\\", \\\"contracts\\\", \\\"are\\\", \\\"managed\\\", \\\"from\\\", \\\"its\\\", \\\"office\\\", \\\"at\\\", \\\"Alliance\\\", \\\"Airport\\\", \\\"in\\\", \\\"Fort\\\", \\\"Worth\\\", \\\",\\\", \\\"Texas\\\", \\\".\\\"], \\\"h\\\": [\\\"alliance airport\\\", \\\"Q5472378\\\", [[12, 13]]], \\\"t\\\": [\\\"fort worth, texas\\\", \\\"Q16558\\\", [[15, 16, 17, 18]]]}, {\\\"tokens\\\": [\\\"Retiro\\\", \\\"Los\\\", \\\"Maitenes\\\", \\\"Airport\\\", \\\"(\\\", \\\",\\\", \\\")\\\", \\\"is\\\", \\\"an\\\", \\\"airport\\\", \\\"northeast\\\", \\\"of\\\", \\\"Retiro\\\", \\\",\\\", \\\"a\\\", \\\"town\\\", \\\"in\\\", \\\"the\\\", \\\"Maule\\\", \\\"Region\\\", \\\"of\\\", \\\"Chile\\\", \\\".\\\"], \\\"h\\\": [\\\"los maitenes airport\\\", \\\"Q16899238\\\", [[1, 2, 3]]], \\\"t\\\": [\\\"retiro\\\", \\\"Q56122\\\", [[0], [12]]]}, {\\\"tokens\\\": [\\\"Claremont\\\", \\\"Airport\\\", \\\",\\\", \\\"also\\\", \\\"known\\\", \\\"as\\\", \\\"Cecil\\\", \\\"County\\\", \\\"Airport\\\", \\\",\\\", \\\"is\\\", \\\"an\\\", \\\"airport\\\", \\\"located\\\", \\\"south\\\", \\\"of\\\", \\\"Elkton\\\", \\\",\\\", \\\"Maryland\\\", \\\".\\\"], \\\"h\\\": [\\\"cecil county airport\\\", \\\"Q19574884\\\", [[6, 7, 8]]], \\\"t\\\": [\\\"elkton, maryland\\\", \\\"Q754338\\\", [[16, 17, 18]]]}, {\\\"tokens\\\": [\\\"The\\\", \\\"route\\\", \\\"between\\\", \\\"Gothenburg\\\", \\\"and\\\", \\\"Stockholm\\\", \\\"ended\\\", \\\"in\\\", \\\"January\\\", \\\"2015\\\", \\\"due\\\", \\\"to\\\", \\\"the\\\", \\\"sudden\\\", \\\"closure\\\", \\\"of\\\", \\\"G\\\\u00f6teborg\\\", \\\"City\\\", \\\"Airport\\\", \\\"by\\\", \\\"Swedavia\\\", \\\".\\\"], \\\"h\\\": [\\\"g\\\\u00f6teborg city airport\\\", \\\"Q844281\\\", [[16, 17, 18]]], \\\"t\\\": [\\\"gothenburg\\\", \\\"Q25287\\\", [[3]]]}, {\\\"tokens\\\": [\\\"David\\\", \\\"Jay\\\", \\\"Perry\\\", \\\"Airport\\\", \\\"is\\\", \\\"a\\\", \\\"town\\\", \\\"-\\\", \\\"owned\\\", \\\"public\\\", \\\"-\\\", \\\"use\\\", \\\"airport\\\", \\\"in\\\", \\\"Goldsby\\\", \\\",\\\", \\\"a\\\", \\\"town\\\", \\\"in\\\", \\\"McClain\\\", \\\"County\\\", \\\",\\\", \\\"Oklahoma\\\", \\\",\\\", \\\"United\\\", \\\"States\\\", \\\".\\\"], \\\"h\\\": [\\\"david jay perry airport\\\", \\\"Q1709203\\\", [[0, 1, 2, 3]]], \\\"t\\\": [\\\"goldsby\\\", \\\"Q2456775\\\", [[14]]]}, {\\\"tokens\\\": [\\\"Wiley\\\", \\\"Post\\\", \\\"Airport\\\", \\\"in\\\", \\\"Bethany\\\", \\\"and\\\", \\\"Max\\\", \\\"Westheimer\\\", \\\"Airport\\\", \\\"in\\\", \\\"Norman\\\", \\\"serve\\\", \\\"as\\\", \\\"reliever\\\", \\\"airports\\\", \\\"for\\\", \\\"Will\\\", \\\"Rogers\\\", \\\"Airport\\\", \\\".\\\"], \\\"h\\\": [\\\"max westheimer airport\\\", \\\"Q10853586\\\", [[6, 7, 8]]], \\\"t\\\": [\\\"norman\\\", \\\"Q40347\\\", [[10]]]}, {\\\"tokens\\\": [\\\"Nearest\\\", \\\"airport\\\", \\\"to\\\", \\\"this\\\", \\\"airstrip\\\", \\\"is\\\", \\\"Savitri\\\", \\\"Jindal\\\", \\\"Airport\\\", \\\"in\\\", \\\"Angul\\\", \\\",\\\", \\\"Odisha\\\", \\\".\\\"], \\\"h\\\": [\\\"savitri jindal airport\\\", \\\"Q18355676\\\", [[6, 7, 8]]], \\\"t\\\": [\\\"angul\\\", \\\"Q518237\\\", [[10]]]}, {\\\"tokens\\\": [\\\"The\\\", \\\"facility\\\", \\\"is\\\", \\\"located\\\", \\\"in\\\", \\\"the\\\", \\\"west\\\", \\\"part\\\", \\\"of\\\", \\\"Regina\\\", \\\",\\\", \\\"Saskatchewan\\\", \\\",\\\", \\\"near\\\", \\\"the\\\", \\\"airport\\\", \\\",\\\", \\\"and\\\", \\\"consists\\\", \\\"of\\\", \\\"several\\\", \\\"buildings\\\", \\\".\\\"], \\\"h\\\": [\\\"airport\\\", \\\"Q1571015\\\", [[15]]], \\\"t\\\": [\\\"regina, saskatchewan\\\", \\\"Q2123\\\", [[9, 10, 11]]]}, {\\\"tokens\\\": [\\\"Also\\\", \\\",\\\", \\\"the\\\", \\\"service\\\", \\\"to\\\", \\\"Washington\\\", \\\"Dulles\\\", \\\"airport\\\", \\\"resumed\\\", \\\"1\\\", \\\"May\\\", \\\"2015\\\", \\\",\\\", \\\"with\\\", \\\"four\\\", \\\"flights\\\", \\\"weekly\\\", \\\".\\\"], \\\"h\\\": [\\\"dulles\\\", \\\"Q466835\\\", [[6]]], \\\"t\\\": [\\\"washington\\\", \\\"Q61\\\", [[5]]]}, {\\\"tokens\\\": [\\\"In\\\", \\\"2003\\\", \\\",\\\", \\\"Benoit\\\", \\\"produced\\\", \\\"two\\\", \\\"canvases\\\", \\\",\\\", \\\"\\\\\\\"\\\", \\\"Orly\\\", \\\"(\\\", \\\"South\\\", \\\")\\\", \\\"\\\\\\\"\\\", \\\",\\\", \\\"inspired\\\", \\\"by\\\", \\\"the\\\", \\\"Orly\\\", \\\"Airport\\\", \\\"in\\\", \\\"Paris\\\", \\\".\\\"], \\\"h\\\": [\\\"orly airport\\\", \\\"Q223416\\\", [[18, 19]]], \\\"t\\\": [\\\"paris\\\", \\\"Q90\\\", [[21]]]}, {\\\"tokens\\\": [\\\"Dr.\\\", \\\"Ferdinand\\\", \\\"Lumban\\\", \\\"Tobing\\\", \\\"Airport\\\", \\\"(\\\", \\\"also\\\", \\\"known\\\", \\\"as\\\", \\\"\\\\\\\"\\\", \\\"Pinangsori\\\", \\\"Airport\\\", \\\"\\\\\\\"\\\", \\\")\\\", \\\"is\\\", \\\"an\\\", \\\"airport\\\", \\\"serving\\\", \\\"the\\\", \\\"city\\\", \\\"of\\\", \\\"Sibolga\\\", \\\"in\\\", \\\"the\\\", \\\"North\\\", \\\"Sumatra\\\", \\\"province\\\", \\\"of\\\", \\\"Indonesia\\\", \\\".\\\"], \\\"h\\\": [\\\"ferdinand lumban tobing airport\\\", \\\"Q4272430\\\", [[1, 2, 3, 4]]], \\\"t\\\": [\\\"sibolga\\\", \\\"Q5984\\\", [[21]]]}, {\\\"tokens\\\": [\\\"Franco\\\", \\\"Bianco\\\", \\\"Airport\\\", \\\"is\\\", \\\"an\\\", \\\"airport\\\", \\\"northwest\\\", \\\"of\\\", \\\"Cerro\\\", \\\"Sombrero\\\", \\\",\\\", \\\"a\\\", \\\"petroleum\\\", \\\"production\\\", \\\"town\\\", \\\"in\\\", \\\"the\\\", \\\"Magallanes\\\", \\\"Region\\\", \\\"of\\\", \\\"Chile\\\", \\\".\\\"], \\\"h\\\": [\\\"franco bianco airport\\\", \\\"Q16891421\\\", [[0, 1, 2]]], \\\"t\\\": [\\\"cerro sombrero\\\", \\\"Q1006493\\\", [[8, 9]]]
```

---
