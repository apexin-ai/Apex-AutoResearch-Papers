# analysis nli combo data reconcile

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Worker execution logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 40
- **Recorded user turns:** 0
- **Tool calls:** 13
- **Original source:** `logs/workers/worker_analysis_nli-combo-data-reconcile_20260522T145105.log`
- **Structured JSON:** [`0b329c292d124decb6f9.json`](../../sessions/0b/0b329c292d124decb6f9.json)

## Before a recorded user message

40 recorded events

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
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus",
  "session_id": "259e8c74-cee8-43ee-8c2a-b39b28aafca2",
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
    "mcp__agent-ml-research__read_project_file",
    "mcp__agent-ml-research__read_registry",
    "mcp__agent-ml-research__register_artifact",
    "mcp__agent-ml-research__save_project_file",
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
  "uuid": "014e4d83-8e97-423d-b321-fa738dd64558",
  "memory_paths": {
    "auto": "/home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0513-3-projects-symb-invariant-consensus/memory/"
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
    "resetsAt": 1779463800,
    "rateLimitType": "five_hour",
    "overageStatus": "rejected",
    "overageDisabledReason": "org_level_disabled",
    "isUsingOverage": false
  },
  "uuid": "26f42c20-b7a0-46d6-b4d3-2763c75d166e",
  "session_id": "259e8c74-cee8-43ee-8c2a-b39b28aafca2"
}
```

---

### Assistant

_source line 4_

我来排查这个数据不一致问题。先并行读取 registry 和相关文件。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "259e8c74-cee8-43ee-8c2a-b39b28aafca2",
  "uuid": "87496e5c-f33d-4f92-a22b-9d786c395587",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SJZVwcZqJZJGVdyQdNFwK6",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12181,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12181
      },
      "output_tokens": 2,
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

_source line 5_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01YbywZyVUiaDm6Msw3EBDag`</summary>

```json
{
  "query": "select:mcp__agent-ml-research__read_registry,mcp__agent-ml-research__read_project_file",
  "max_results": 2
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "259e8c74-cee8-43ee-8c2a-b39b28aafca2",
  "uuid": "69e3f2a8-37b0-4c10-8d04-643a4eee598c",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SJZVwcZqJZJGVdyQdNFwK6",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12181,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12181
      },
      "output_tokens": 2,
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

_source line 6 · 2026-05-22T14:51:18.463Z_

<details><summary>↩ Tool result · `toolu_01YbywZyVUiaDm6Msw3EBDag`</summary>

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
````

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "259e8c74-cee8-43ee-8c2a-b39b28aafca2",
  "uuid": "cde6ab32-37ec-4265-9a5c-50e3cbf63a2c",
  "tool_use_result": {
    "matches": [
      "mcp__agent-ml-research__read_registry",
      "mcp__agent-ml-research__read_project_file"
    ],
    "query": "select:mcp__agent-ml-research__read_registry,mcp__agent-ml-research__read_project_file",
    "total_deferred_tools": 25
  }
}
```

</details>

---

### Assistant

_source line 7_

<details><summary>Logged reasoning block</summary>

```text
Now let me read the registry for exp-090 and search for NLI/combo related experiments, plus read paper_framing.md in parallel.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "259e8c74-cee8-43ee-8c2a-b39b28aafca2",
  "uuid": "1e2ddf3d-a624-44df-a68b-9201a80641b8",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PnSoFx6LXaz6xGNSLwjRSX",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 812,
      "cache_read_input_tokens": 24022,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 812
      },
      "output_tokens": 33,
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

_source line 8_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry · `toolu_01971TigczC2fuHdvVSbYDmm`</summary>

```json
{
  "filters": {
    "exp_id": "exp-090"
  },
  "project": "symb_invariant_consensus",
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
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "259e8c74-cee8-43ee-8c2a-b39b28aafca2",
  "uuid": "b19b06ab-4a4a-423b-88f7-d32956c48881",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PnSoFx6LXaz6xGNSLwjRSX",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 812,
      "cache_read_input_tokens": 24022,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 812
      },
      "output_tokens": 33,
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

_source line 9 · 2026-05-22T14:51:23.078Z_

<details><summary>↩ Tool result · `toolu_01971TigczC2fuHdvVSbYDmm`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"experiments\": {}, \"count\": 0, \"total\": 0, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.4874}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "259e8c74-cee8-43ee-8c2a-b39b28aafca2",
  "uuid": "158c9d6d-5e75-44cb-988d-feac3888930a",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"experiments\\\": {}, \\\"count\\\": 0, \\\"total\\\": 0, \\\"baseline\\\": null}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.4874}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"experiments\": {}, \"count\": 0, \"total\": 0, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.4874}}"
    }
  }
}
```

</details>

---

### Tool call

_source line 10_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry · `toolu_01XEZDwiogwt8W978WB5TYG9`</summary>

```json
{
  "filters": {
    "exp_id": "exp-048"
  },
  "project": "symb_invariant_consensus",
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
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "259e8c74-cee8-43ee-8c2a-b39b28aafca2",
  "uuid": "a4d0af20-e6e0-472c-b95d-49b5920a5930",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PnSoFx6LXaz6xGNSLwjRSX",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 812,
      "cache_read_input_tokens": 24022,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 812
      },
      "output_tokens": 33,
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

_source line 11 · 2026-05-22T14:51:23.966Z_

<details><summary>↩ Tool result · `toolu_01XEZDwiogwt8W978WB5TYG9`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"experiments\": {}, \"count\": 0, \"total\": 0, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.4346}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "259e8c74-cee8-43ee-8c2a-b39b28aafca2",
  "uuid": "65fed21d-9918-4eaa-a8ef-28f69483c14b",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"experiments\\\": {}, \\\"count\\\": 0, \\\"total\\\": 0, \\\"baseline\\\": null}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.4346}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"experiments\": {}, \"count\": 0, \"total\": 0, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.4346}}"
    }
  }
}
```

</details>

---

### Tool call

_source line 12_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry · `toolu_016d1mtnGS9CWhfPJ6tsfu7i`</summary>

```json
{
  "project": "symb_invariant_consensus",
  "limit": 0,
  "fields": [
    "exp_id",
    "hypothesis",
    "status",
    "conclusion",
    "metrics",
    "notes",
    "tags"
  ]
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "259e8c74-cee8-43ee-8c2a-b39b28aafca2",
  "uuid": "035eb330-8005-4175-94a0-6cf2af8f20d2",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PnSoFx6LXaz6xGNSLwjRSX",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 812,
      "cache_read_input_tokens": 24022,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 812
      },
      "output_tokens": 33,
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

_source line 13_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_012G1AFdwChAccCBGv5XFSLP`</summary>

```json
{
  "project": "symb_invariant_consensus",
  "file": "paper_framing.md",
  "max_chars": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "259e8c74-cee8-43ee-8c2a-b39b28aafca2",
  "uuid": "4e5343c9-c08a-4c0f-8130-6efb40c437dc",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PnSoFx6LXaz6xGNSLwjRSX",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 812,
      "cache_read_input_tokens": 24022,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 812
      },
      "output_tokens": 33,
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

_source line 14 · 2026-05-22T14:51:25.461Z_

<details><summary>↩ Tool result · `toolu_016d1mtnGS9CWhfPJ6tsfu7i`</summary>

```text
Error: result (117,040 characters) exceeds maximum allowed tokens. Output has been saved to /home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0513-3-projects-symb-invariant-consensus/259e8c74-cee8-43ee-8c2a-b39b28aafca2/tool-results/mcp-agent-ml-research-read_registry-1779461485443.txt.
Format: JSON with schema: {result: string}
Use offset and limit parameters to read specific portions of the file, search within it for specific content, and jq to make structured queries.
REQUIREMENTS FOR SUMMARIZATION/ANALYSIS/REVIEW:
- You MUST read the content from the file at /home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0513-3-projects-symb-invariant-consensus/259e8c74-cee8-43ee-8c2a-b39b28aafca2/tool-results/mcp-agent-ml-research-read_registry-1779461485443.txt in sequential chunks until 100% of the content has been read.
- If you receive truncation warnings when reading the file, reduce the chunk size until you have read 100% of the content without truncation.
- Before producing ANY summary or analysis, you MUST explicitly describe what portion of the content you have read. ***If you did not read the entire content, you MUST explicitly state this.***

```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "259e8c74-cee8-43ee-8c2a-b39b28aafca2",
  "uuid": "f4a276a6-19ca-4b2f-87d6-847ce6e13c53",
  "tool_use_result": {
    "content": "Error: result (117,040 characters) exceeds maximum allowed tokens. Output has been saved to /home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0513-3-projects-symb-invariant-consensus/259e8c74-cee8-43ee-8c2a-b39b28aafca2/tool-results/mcp-agent-ml-research-read_registry-1779461485443.txt.\nFormat: JSON with schema: {result: string}\nUse offset and limit parameters to read specific portions of the file, search within it for specific content, and jq to make structured queries.\nREQUIREMENTS FOR SUMMARIZATION/ANALYSIS/REVIEW:\n- You MUST read the content from the file at /home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0513-3-projects-symb-invariant-consensus/259e8c74-cee8-43ee-8c2a-b39b28aafca2/tool-results/mcp-agent-ml-research-read_registry-1779461485443.txt in sequential chunks until 100% of the content has been read.\n- If you receive truncation warnings when reading the file, reduce the chunk size until you have read 100% of the content without truncation.\n- Before producing ANY summary or analysis, you MUST explicitly describe what portion of the content you have read. ***If you did not read the entire content, you MUST explicitly state this.***\n",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"experiments\": {\"exp-multi-seed-mistral-folio\": {\"status\": \"PREPARING\", \"hypothesis\": \"Multi-seed replication (seeds 123,456,789) of Mistral-7B × FOLIO-204 shows consistent Δ(SICA-SC) direction across seeds. Baseline seed=42 already available. Combined with Mistral×PW and Qwen2.5×FOLIO/PW multi-seed, provides comprehensive reproducibility evidence for W4 reviewer response.\", \"notes\": \"DATA AUDIT COMPLETE. multi_seed/seed123: SC=57.84% (differs from exp052 SC=53.92% by 4pp — different run, code version mismatch). multi_seed/seed456: CORRUPTED — vLLM crash, 111/204 empty problems, invalid. multi_seed/seed789: CLEAN — backup matches main, normal runtime 4798s. PAPER USES: exp052 (seed=123, D064-corrected SC=54.41%) + exp053 (seed=456, D064-corrected SC=55.88%) + PID 576938 seed=789 (SC=59.31%). Earlier report of 67.16% was LLaMA FOLIO seed=123 misattributed to Mistral.\", \"conclusion\": \"success\", \"metrics\": {\"d064_corrected\": true, \"seed123\": {\"sc_acc\": 54.41, \"sica_acc\": 57.35, \"delta\": 2.94, \"n\": 204, \"source\": \"exp052 D064-reeval\"}, \"seed456\": {\"sc_acc\": 55.88, \"sica_acc\": 55.88, \"delta\": 0, \"n\": 204, \"source\": \"exp053 D064-reeval\"}, \"seed789\": {\"sc_acc\": 59.31, \"sica_acc\": 56.86, \"delta\": -2.45, \"n\": 204, \"source\": \"PID 576938 (D064 built-in)\"}, \"mean_3seed\": {\"sc\": 56.53, \"sc_sd\": 2.51, \"sica\": 56.7, \"sica_sd\": 0.75, \"delta\": 0.16, \"delta_sd\": 2.7, \"n_seeds\": 3}}}, \"exp-multi-seed-llama-pw\": {\"status\": \"PREPARING\", \"hypothesis\": \"Multi-seed replication (seeds 42,123,456) of LLaMA-3.1-8B × ProofWriter-600 adds cross-dataset evidence for the third model family. If Δ(SICA-SC)≤0 holds on PW as well as FOLIO, it confirms SCB is dataset-invariant within LLaMA-8B. Addresses W4 reviewer concern.\", \"notes\": \"PID 614142 on westd-16639 cuda:3 port 8004. vLLM PID 613151 (LLaMA-3.1-8B, max-model-len=8192, max_tokens=2048). 3-seed sequence: 42→123→456. Each seed ~600 problems. Model: /root/autodl-tmp/models/Meta-Llama-3.1-8B-Instruct. Script: scripts/multiseed_llama8b_pw_cuda3.sh\", \"metrics\": {\"pw_seed42\": {\"status\": \"running\", \"progress\": \"60/600\"}, \"pw_seed123\": {\"status\": \"pending\"}, \"pw_seed456\": {\"status\": \"pending\"}}}, \"exp-multi-seed-llama-folio\": {\"status\": \"PREPARING\", \"hypothesis\": \"Multi-seed replication (seeds 123,456,789) of LLaMA-3.1-8B × FOLIO-204 shows consistent Δ(SICA-SC) direction across seeds, adding a third model family (beyond Qwen2.5 and Mistral) for cross-family consistency evidence. Addresses W4 reviewer concern.\", \"notes\": \"PID 596151 on westd-16639 cuda:1 port 8002. vLLM PID 595261 (max-model-len=8192, max_tokens=2048). Previous attempt failed: max-model-len=4096 caused HTTP 400 on all requests. Fixed by increasing to 8192 + reducing max_tokens to 2048. ~70s/prob, 3 seeds sequential, ETA ~12h (~23:00 UTC May 22). Output: results/multi_seed/llama8b_folio_seed{123,456,789}/\", \"metrics\": {\"seed123\": {\"sc_acc\": 67.16, \"sica_acc\": 63.73, \"delta\": -3.43, \"n\": 204, \"extraction_rate\": 0.959, \"status\": \"COMPLETE\"}, \"seed456\": {\"status\": \"running\", \"progress\": \"125/204\"}, \"seed789\": {\"status\": \"pending\"}}}, \"exp-multi-seed-mistral-pw\": {\"status\": \"PREPARING\", \"hypothesis\": \"Multi-seed replication (seeds 42,123,456,789) of Mistral-7B × ProofWriter-600 shows consistent Δ(SICA-SC) direction across seeds, confirming single-seed results are not artifacts of random sampling. Addresses W4 reviewer concern about reproducibility.\", \"notes\": \"PID 510987 on westd-16639 cuda:2 port 8003. Running 4-seed sequence (42→123→456→789). Note: seed=42 is being re-run (should have used existing baseline), wasting ~4.5h. Each seed ~4.5h (600q × 27s). Total ETA ~18h. Cron registered (600s). Output: results/multi_seed/mistral_pw_seed{X}/results.json\", \"metrics\": {\"pw_seed42\": {\"sc_acc\": 40, \"sica_acc\": 36.67, \"delta\": -3.33, \"n\": 600, \"status\": \"COMPLETE\"}, \"pw_seed123\": {\"sc_acc\": 40.8, \"sica_acc\": 37.5, \"delta\": -3.3, \"n\": 600, \"status\": \"COMPLETE\"}, \"pw_seed456\": {\"status\": \"running\", \"progress\": \"43/600\"}, \"pw_seed789\": {\"status\": \"pending\"}}}, \"exp-multi-seed-qwen25-7b-folio\": {\"status\": \"PREPARING\", \"hypothesis\": \"Multi-seed replication (seeds 123,456,789) of Qwen2.5-7B × FOLIO-204 adds a fourth model family (beyond Qwen2.5-14B, Mistral-7B, LLaMA-8B) for cross-family consistency of SCB. If Δ(SICA-SC)≤0 holds across 7B-scale Qwen as well, it strengthens the scale+architecture invariance claim.\"}, \"exp-multi-seed-qwen25\": {\"status\": \"PREPARING\", \"hypothesis\": \"Multi-seed replication (seeds 123,456,789) of Qwen2.5-14B × FOLIO-204 and ProofWriter-600 shows consistent Δ(SICA-SC) direction across seeds. Baseline seed=42: FOLIO Δ=-1.96pp, PW Δ=-2.00pp. Addresses W4 reviewer concern.\", \"notes\": \"FOLIO 4-seed COMPLETE (guard killed cuda:1 master PID 510872 as designed). Cron auto-resolved DONE(failed) is misleading — FOLIO portion is success. PW 3-seed still running on cuda:0 PID 552333 (independent process, not tracked by this cron). FOLIO results: mean Δ=-1.24±0.86pp, 4/4 seeds ≤0.\", \"metrics\": {\"folio_seed42\": {\"sc_acc\": 77.5, \"sica_acc\": 75.49, \"delta\": -2.01, \"n\": 204, \"source\": \"baseline\"}, \"folio_seed123\": {\"sc_acc\": 74.51, \"sica_acc\": 73.04, \"delta\": -1.47, \"n\": 204}, \"folio_seed456\": {\"sc_acc\": 74.02, \"sica_acc\": 74.02, \"delta\": 0, \"n\": 204}, \"folio_seed789\": {\"sc_acc\": 74.02, \"sica_acc\": 72.55, \"delta\": -1.47, \"n\": 204, \"status\": \"FINAL\"}, \"folio_mean\": {\"sc\": 75.01, \"sica\": 73.78, \"delta\": -1.24, \"sc_sd\": 1.67, \"sica_sd\": 1.3, \"delta_sd\": 0.86, \"n_seeds\": 4}, \"pw_seed123\": {\"status\": \"running\", \"progress\": \"190/600\", \"pid\": 552333, \"gpu\": \"cuda:0\"}, \"pw_seed456\": {\"status\": \"pending\", \"note\": \"directory has garbage from cuda:1 (max_model_len bug), cuda:0 will overwrite\"}, \"pw_seed789\": {\"status\": \"pending\"}, \"pw_eta\": \"2026-05-23T17:40Z\"}, \"conclusion\": \"failed\"}, \"exp-013-constraint-ablation\": {\"status\": \"PREPARING\", \"hypothesis\": \"MaxSAT satisfiability checking contributes minimal accuracy gains over naive constraint counting, because extracted constraints are too homogeneous (trace co-sourcing) to provide discriminative satisfiability signals. If SICA-MaxSAT ≈ SICA-count-only, the SAT solver is not the bottleneck — constraint quality is.\", \"metrics\": {\"alpha_ablation\": {\"mistral_folio\": {\"alpha_0.1\": {\"sica_acc\": 54.9, \"countonly_acc\": 54.9, \"agreement\": 100}, \"alpha_0.3\": {\"sica_acc\": 54.9, \"countonly_acc\": 54.9, \"agreement\": 100}, \"alpha_0.5\": {\"sica_acc\": 54.9, \"countonly_acc\": 54.9, \"agreement\": 100}, \"alpha_0.7\": {\"sica_acc\": 53.92, \"countonly_acc\": 54.41, \"agreement\": 99}, \"alpha_0.9\": {\"sica_acc\": 54.9, \"countonly_acc\": 55.39, \"agreement\": 99}}, \"qwen25_folio\": {\"alpha_0.1\": {\"sica_acc\": 75, \"countonly_acc\": 75, \"agreement\": 100}, \"alpha_0.3\": {\"sica_acc\": 75, \"countonly_acc\": 75, \"agreement\": 100}, \"alpha_0.5\": {\"sica_acc\": 75, \"countonly_acc\": 75, \"agreement\": 100}, \"alpha_0.7\": {\"sica_acc\": 74.51, \"countonly_acc\": 74.51, \"agreement\": 100}, \"alpha_0.9\": {\"sica_acc\": 74.02, \"countonly_acc\": 74.02, \"agreement\": 100}}, \"conclusion\": \"Agreement >= 99% across all alpha for both conditions. MAX-SAT equiv count-only is alpha-insensitive.\"}}, \"conclusion\": \"success\", \"notes\": \"V16 rerun with correct Qwen2.5-14B (exp036+exp032) and R1-Distill-8B data. MaxSAT ≈ count-only or worse. Strongly supports SCB narrative: constraints vote, not reason. Random-weight -6.4pp confirms count structure matters but SAT solving adds nothing.\"}, \"exp-folio-2x2-crossmodel\": {\"status\": \"DONE\", \"hypothesis\": \"Cross-model extraction on FOLIO-204 replicates ProofWriter 2×2 finding: extractor capability dominates SICA accuracy regardless of generator, and BR>1 persists in all cells. If confirmed, this generalizes the SCB universality + extractor dominance finding across two distinct reasoning datasets.\", \"notes\": \"FOLIO 2×2 completed. All 4 cells 204 items. Sentinel found. BR>1 all cells (1.94-2.70). Qwen3 ext improves Mistral gen by +3.92pp but Mistral ext reduces Qwen3 gen by -1.47pp. McNemar p≈0 both directions. Results saved: folio_2x2_metrics.json. Log: master.log. Checkpoint: results/exp_folio_2x2/\", \"conclusion\": \"success\", \"metrics\": {\"folio_2x2\": {\"mistral_gen_mistral_ext\": {\"SICA\": 56.86, \"delta_pp\": 0.98, \"BR_mean\": 2.7}, \"mistral_gen_qwen3_ext\": {\"SICA\": 59.8, \"delta_pp\": 3.92, \"BR_mean\": 1.94}, \"qwen3_gen_mistral_ext\": {\"SICA\": 81.86, \"delta_pp\": -1.47, \"BR_mean\": 2.66}, \"qwen3_gen_qwen3_ext\": {\"SICA\": 84.8, \"delta_pp\": 1.47, \"BR_mean\": 2.35}}, \"SC_mistral\": 55.88, \"SC_qwen3\": 83.33, \"kappa_mistral\": 0.46, \"kappa_qwen3\": 0.79, \"mcnemar_mistral_ext_p\": 0, \"mcnemar_qwen3_ext_p\": 0}}, \"exp-d126-70b-sica\": {\"status\": \"DONE\", \"hypothesis\": \"Symbolic confirmation bias persists at 72B scale: Qwen2.5-72B self-extracted constraints will show BR > 1 and κ ≥ 0.40, with SICA ≈ SC (no significant improvement), demonstrating that the independence bottleneck is scale-invariant beyond the 7B-14B range tested so far.\", \"notes\": \"westd-16639 单卡 70B (PID 436077) 已被 D136 主动终止（25/204, ETA 45h 不经济）。实验转移到 westd-25068 tp=4 (PID 40007, vLLM PID 39013 port 8002, AWQ 39GB confirmed)。westd-25068 进度 52/204, ETA ~2.6h, avg 61.8s/prob。folio_0-folio_11 (12题) 在 westd-25068 标为 SKIPPED，合并时需用 westd-16639 实际结果替换。\", \"conclusion\": \"failed\"}, \"exp-d126-crossmodel-sica\": {\"status\": \"DONE\", \"hypothesis\": \"Cross-model constraint extraction (Generator: Qwen3-14B, Extractor: Mistral-7B, and vice versa) reduces symbolic confirmation bias compared to same-model extraction. If SCB stems from same-model distributional overlap, cross-model extraction should lower BR and improve SICA accuracy on ProofWriter N=204.\", \"notes\": \"2×2 cross-model SICA completed 05:39 UTC. SCB universality confirmed, extractor dominance as key finding (D140). Cron auto-fail was false alarm — process exited normally after completion. 2×2 matrix: Qwen3 ext ~79.9% regardless of generator, Mistral ext 34-38%. BR>1 all 4 cells. Process-κ generator-intrinsic. JSON: crossmodel_2x2_metrics.json\", \"metrics\": {\"2x2_matrix\": {\"mistral_gen_mistral_ext\": {\"SICA\": 34.31, \"delta_pp\": -5.88, \"BR_mean\": 3.44, \"BR_inf_rate\": 32.1, \"process_kappa\": 0.619}, \"mistral_gen_qwen3_ext\": {\"SICA\": 79.9, \"delta_pp\": 39.71, \"BR_mean\": 2.85, \"BR_inf_rate\": 17.1, \"process_kappa\": 0.619}, \"qwen3_gen_mistral_ext\": {\"SICA\": 37.75, \"delta_pp\": -49.02, \"BR_mean\": 2.16, \"BR_inf_rate\": 45.7, \"process_kappa\": 0.836}, \"qwen3_gen_qwen3_ext\": {\"SICA\": 79.9, \"delta_pp\": -6.86, \"BR_mean\": 1.16, \"BR_inf_rate\": 63.4, \"process_kappa\": 0.836}}, \"SC_mistral\": 40.2, \"SC_qwen3\": 86.8, \"key_finding\": \"Extractor capability dominates SICA accuracy; BR>1 in all 4 cells confirming SCB universality\"}, \"conclusion\": \"success\"}, \"exp-d135-frontier-scb\": {\"status\": \"PREPARING\", \"hypothesis\": \"2026 frontier closed-source models (Claude/GPT/Gemini via OpenRouter) also exhibit SCB: self-extracted constraints will show BR≥2× with SICA≈SC, extending the scale-invariance finding from open-source 7B-72B to frontier closed-source models.\", \"notes\": \"Multi-model frontier SCB experiment, still active. Cron false alarm: tracked PID 473361 (o3 extraction, completed 196/196), auto-failed on 5th dead check — reverted to PREPARING. Active sub-experiments: exp-d126-70b-sica (70B AWQ tp=4, westd-25068), exp-d126-crossmodel-sica (cross-model 2×2, westd-16639). Gemini SC running via API (westd-25068). Completed sub-components: gpt-4o ✅, gpt-4.1 ✅, gpt-5.5 ✅, o3 extraction ✅, R1-Distill ✅.\", \"metrics\": {\"gpt4o_self\": {\"SC\": 73.9, \"SICA\": 72.1, \"BR_mean\": 2.94, \"process_kappa\": 0.79, \"answer_kappa\": 0.8}, \"gpt41_cross_mistral\": {\"SC\": 82.84, \"SICA\": 81.37, \"delta_pp\": -1.47, \"BR_mean\": 2.7, \"process_kappa\": 0.79, \"answer_kappa\": 0.86}, \"gpt55_cross_mistral\": {\"SC\": 84.31, \"SICA\": 84.8, \"delta_pp\": 0.49, \"BR_mean\": 3.48, \"process_kappa\": 0.56, \"answer_kappa\": 0.96}, \"r1distill_cross_mistral\": {\"SC\": 74.51, \"SICA\": 76.96, \"delta_pp\": 2.45, \"BR_mean\": 2.92, \"process_kappa\": 0.25, \"answer_kappa\": 0.69}, \"o3_cross_mistral\": {\"SC\": 82.65, \"SICA\": 82.65, \"delta_pp\": 0, \"BR_mean\": 1.66, \"process_kappa\": 0.6, \"answer_kappa\": 0.92}, \"gemini_interim_95q\": {\"SC\": 87.4, \"cross_SICA\": 86.3, \"delta_pp\": -1.1, \"process_kappa\": 0.79, \"n_questions\": 95, \"status\": \"extraction_complete_95q\"}}, \"conclusion\": \"failed\"}, \"exp-text-ablation\": {\"status\": \"DONE\", \"hypothesis\": \"Constraint extraction temperature (T_ext) affects SICA accuracy: moderate T_ext (0.3-0.5) produces more diverse yet valid constraints than extremes (0.1 too deterministic, 1.0 too noisy), yielding higher SICA-SC delta on FOLIO-204.\", \"conclusion\": \"success\"}, \"exp-d126-r1-distill-sica\": {\"status\": \"PREPARING\", \"hypothesis\": \"Reasoning-distilled model (DeepSeek-R1-Distill-LLaMA-8B) does not escape SCB: self-extracted constraints will show BR≥2× and SICA≈SC, demonstrating that SCB is a structural property of autoregressive self-extraction that reasoning training cannot eliminate.\", \"notes\": \"Pipeline re-run PID 451580: 130/204 intermediates, ETA ~17:10 UTC. Cross-extraction v2 has 93/204. Plan: pipeline finishes → kill R1-Distill vLLM (cuda:3) → deploy Mistral port 8004 → run reextract_bpe_fix.py for remaining ~111 problems → merge 204 → compute full SICA+BR+κ. Mistral model: /root/autodl-tmp/models/Mistral-7B-Instruct-v0.3\", \"conclusion\": \"success\", \"metrics\": {\"cross_model_extraction_93\": {\"n_problems\": 93, \"sc_accuracy\": 0.7527, \"sica_accuracy\": 0.7849, \"delta_pp\": 3.22, \"mean_br\": 2.97, \"median_br\": 2, \"process_kappa_tfidf\": 0.2386, \"answer_fleiss_kappa\": 0.703, \"extractor\": \"Mistral-7B\"}, \"cross_model_extraction_204\": {\"n_problems\": 204, \"sc_accuracy\": 0.7451, \"sica_accuracy\": 0.7647, \"delta_pp\": 1.96, \"extraction_rate\": 0.933, \"total_constraints\": 14602, \"unique_constraints\": 8653, \"mean_br\": 2.85, \"median_br\": 2, \"process_kappa_tfidf\": 0.2477, \"answer_fleiss_kappa\": 0.6944, \"extractor\": \"Mistral-7B\", \"note\": \"Full 204 questions. Cross-model: R1-Distill traces extracted by Mistral-7B. BPE fix applied.\"}}}, \"exp-d134-e6-closed-model\": {\"status\": \"PREPARING\", \"hypothesis\": \"Closed-source frontier models (GPT-4o, Claude, etc.) also exhibit symbolic confirmation bias when self-extracting FOL constraints. If SCB persists at frontier scale with different architectures, this strengthens the claim that SCB is a fundamental property of self-verification rather than a scale or architecture artifact.\", \"notes\": \"Partial run: 154/204 (75.5%). SICA=71.4%, SC=73.4%. Process exited without error at problem 155. Per-class SICA/SC: True 94.8%/93.1%, False 82.9%/82.9%, Unknown 38.2%/45.5%. 9 SICA-SC disagreements (SC wins 5, SICA wins 2).\", \"conclusion\": \"success\", \"metrics\": {\"gpt4o_folio\": {\"completed\": 161, \"total\": 204, \"sc_accuracy\": 0.7391, \"sica_accuracy\": 0.7205, \"delta_pp\": -1.86, \"n_sica_wrong\": 45, \"mean_br\": 2.94, \"median_br\": 1.91, \"weighted_br\": 3.07, \"n_br_finite\": 25, \"n_br_infinite\": 20, \"process_kappa_tfidf\": 0.7884, \"answer_fleiss_kappa\": 0.8009}}}, \"exp-d134-cil\": {\"status\": \"PREPARING\", \"hypothesis\": \"CIL (Cumulative Information Lift) unifies combo gain prediction: CIL>0 iff verifier adds independent signal beyond generator. Cross-architecture NLI pairs show CIL>0 (predicting significant combo gain), while same-model SICA shows CIL≈0 (predicting no gain), validating CIL as the mechanistic criterion for escape.\", \"conclusion\": \"success\", \"metrics\": {\"n_pairs_computed\": 8, \"n_pairs_missing\": 2, \"spearman_rho\": 0.881, \"spearman_p\": 0.0039, \"pearson_r\": 0.8481, \"pearson_p\": 0.0078, \"cil_deberta_mistral_pw\": 1.67, \"cil_sica_mistral_pw\": -4.61, \"cil_deberta_qwen14b_pw\": -0.21, \"cil_sica_qwen14b_pw\": -4.21, \"corrected_v2\": \"Qwen14B canonical SC=74.00% (exp032). Gains: DeBERTa +0.33pp, SICA -2.50pp. Spearman 0.881 p=0.004.\"}}, \"exp-d134-baf-decoupled\": {\"status\": \"PREPARING\", \"hypothesis\": \"Truncating CoT traces before the answer sentence reduces SCB: truncated-trace BR < full-trace BR, because answer leakage into FOL constraints is the primary SCB mechanism (Dir-H provenance showed late-step leakage 27.23% >> early 22.00%).\", \"conclusion\": \"negative\", \"metrics\": {\"full_trace_acc\": 0.5931, \"conservative_acc\": 0.5392, \"standard_acc\": 0.5441, \"aggressive_acc\": 0.5392, \"conservative_br_delta\": -0.049, \"conservative_wilcoxon_p\": 0.122, \"conservative_mcnemar_p\": 0.001, \"aggressive_br_delta\": -0.145, \"aggressive_wilcoxon_p\": 0.256, \"aggressive_mcnemar_p\": 0.013}}, \"exp-d134-process-br\": {\"status\": \"PREPARING\", \"hypothesis\": \"SCB concentrates in late-step/answer-adjacent constraints: BR(late-step) >> BR(early-step), and BR(hard questions SC≤6/12) >> BR(easy questions SC≥10/12). If confirmed, SCB is driven by answer leakage into constraint extraction rather than uniform distributional bias.\", \"conclusion\": \"success\", \"metrics\": {\"position_br_early\": 5.37, \"position_br_mid\": 5.25, \"position_br_late\": 5.16, \"fisher_early_vs_late_p\": 0.708, \"difficulty_br_easy\": 18.82, \"difficulty_br_hard\": 2.71, \"fisher_diff_p\": 0, \"conditional_br\": 5.69, \"other_br\": 4.91, \"fisher_type_p\": 0.061}}, \"exp-d126-drc-folio\": {\"status\": \"PREPARING\", \"hypothesis\": \"DRC (Disagreement-Routed Cascade) with DeBERTa NLI verification on FOLIO-204 recovers ≥80% of full NLI combo gain at ≤50% verification cost, extending the ProofWriter DRC result to a second dataset and demonstrating the generality of disagreement-based routing.\", \"conclusion\": \"success\", \"metrics\": {\"sc_acc\": 55.88, \"full_combo_w3_acc\": 58.82, \"drc_tau07_w3_acc\": 58.33, \"drc_tau07_gain_pp\": 2.45, \"drc_tau07_nli_calls\": \"71/204\", \"drc_tau07_cost_pct\": 34.8, \"drc_tau07_gain_recovery_pct\": 83.3, \"drc_tau08_w3_acc\": 58.82, \"drc_tau08_gain_recovery_pct\": 100, \"drc_tau08_cost_pct\": 48.5}}, \"exp_text_ablation\": {\"status\": \"DONE\", \"hypothesis\": \"Constraint extraction temperature (T_ext) does not significantly affect SICA accuracy because confirmation bias is inherent to self-extraction regardless of temperature — constraints at any T_ext will project the model's distributional bias rather than provide independent verification signal\", \"conclusion\": \"success\", \"metrics\": {\"t_ext_0.1\": {\"sica_acc\": 57.35, \"delta_pp\": 1.47, \"p\": 0.581}, \"t_ext_0.3\": {\"sica_acc\": 59.31, \"delta_pp\": 4.9, \"p\": 0.013}, \"t_ext_0.5\": {\"sica_acc\": 56.37, \"delta_pp\": 0.49, \"p\": 1}, \"t_ext_0.7\": {\"sica_acc\": 53.43, \"delta_pp\": -2.45, \"p\": 0.302}, \"t_ext_1.0\": {\"sica_acc\": 55.39, \"delta_pp\": -0.49, \"p\": 1}, \"sc_baseline\": 55.88}}, \"exp-092-llama8b-pw-nli-combo\": {\"status\": \"DONE\", \"hypothesis\": \"LLaMA-3.1-8B ProofWriter NLI combo: DeBERTa-large-MNLI standalone (55%) < SC (70%)，capability gap = -15pp。验证 NLI combo 是否在第二个 model family 上也能提升 SC accuracy。\", \"conclusion\": \"success\", \"metrics\": {\"n\": 600, \"sc_accuracy\": 0.7, \"nli_standalone\": 0.55, \"capability_gap_pp\": -15, \"combo_w1\": 0.7283, \"combo_w3\": 0.7417, \"combo_w5\": 0.7167, \"delta_w1_pp\": 2.83, \"delta_w3_pp\": 4.17, \"delta_w5_pp\": 1.67, \"mcnemar_w1_p\": 0.0001, \"mcnemar_w3_p\": 0.0035, \"mcnemar_w5_p\": 0.4335, \"nli_correct_sc_wrong\": 120, \"sc_correct_nli_wrong\": 210}}, \"exp-091-qwen14b-pw-nli-combo\": {\"status\": \"DONE\", \"hypothesis\": \"Qwen2.5-14B ProofWriter NLI combo: DeBERTa-large-MNLI standalone (55%) < SC (73.50%)，capability gap = -18.50pp。根据 Push A capability gap 单调关系，combo gain 应介于 Qwen3 (+1.83pp) 和 Mistral (+10.67pp) 之间。\", \"conclusion\": \"success\", \"metrics\": {\"n\": 600, \"sc_accuracy\": 0.735, \"nli_standalone\": 0.55, \"capability_gap_pp\": -18.5, \"combo_w1\": 0.7417, \"combo_w3\": 0.7433, \"combo_w5\": 0.7533, \"delta_w1_pp\": 0.67, \"delta_w3_pp\": 0.83, \"delta_w5_pp\": 1.83, \"mcnemar_w1_p\": 0.344, \"mcnemar_w3_p\": 0.405, \"mcnemar_w5_p\": 0.144}}, \"exp-wave3-dir-g-decoupling\": {\"status\": \"DONE\", \"hypothesis\": \"Decoupling: 将 FOL 约束提取与答案生成解耦——先生成答案 trace，再独立提取 FOL 约束（不暴露答案给约束提取 prompt），可以打破 confirmation bias 因果链。Conservative 策略：截断 trace 中答案相关内容后再提取约束。\", \"conclusion\": \"negative\", \"metrics\": {\"n\": 204, \"sc_baseline\": 0.5441, \"sc_correct\": 111, \"sica_original\": 0.5931, \"sica_correct\": 121, \"conservative_accuracy\": 0.5392, \"conservative_correct\": 110, \"conservative_avg_trunc_pct\": 4.3, \"conservative_match_pct\": 98.4, \"standard_accuracy\": 0.5441, \"standard_correct\": 111, \"standard_avg_trunc_pct\": 18.9, \"standard_match_pct\": 98.4, \"aggressive_accuracy\": 0.5392, \"aggressive_correct\": 110, \"aggressive_avg_trunc_pct\": 35.3, \"aggressive_match_pct\": 100, \"best_strategy\": \"standard\", \"best_delta_vs_sc_pp\": 0, \"best_delta_vs_sica_pp\": -4.9}}, \"exp-090-r-nli-proofwriter\": {\"status\": \"DONE\", \"hypothesis\": \"Cross-architecture NLI verification (DeBERTa-large-MNLI) 在 ProofWriter-D5 上也能提升 SC accuracy，验证 FOLIO 上 R 方法的跨数据集泛化能力。来源: R5-N4 审稿修复 + Claim 1 (cross-architecture escape generalization)。\", \"conclusion\": \"success\", \"metrics\": {\"n\": 600, \"sc_accuracy\": 0.3933, \"sica_accuracy\": 0.365, \"nli_standalone\": 0.55, \"combo_w1\": 0.4017, \"combo_w3\": 0.4283, \"combo_w5\": 0.5, \"delta_w1_pp\": 0.83, \"delta_w3_pp\": 3.5, \"delta_w5_pp\": 10.67, \"mcnemar_w1_p\": 0.2668, \"mcnemar_w1_b\": 4, \"mcnemar_w1_c\": 9, \"mcnemar_w3_p\": 0.0125, \"mcnemar_w3_b\": 22, \"mcnemar_w3_c\": 43, \"mcnemar_w5_p\": 0.0001, \"mcnemar_w5_b\": 35, \"mcnemar_w5_c\": 99, \"nli_true_acc\": 0.64, \"nli_false_acc\": 0.975, \"nli_unknown_acc\": 0.035, \"nli_correct_sc_wrong\": 274, \"sc_correct_nli_wrong\": 180, \"agreement_acc\": 0.808}}, \"exp-089-oracle-mistral-7b\": {\"status\": \"DONE\", \"hypothesis\": \"Mistral-7B的oracle SICA（用FOLIO gold FOL替换自提取FOL）ceiling gap应显著大于Qwen-14B的+14.22pp，因为更弱模型的自提取FOL质量更差，gold FOL替换带来的提升更大。\", \"conclusion\": \"success\", \"metrics\": {\"sc_accuracy\": 0.5588, \"oracle_sica_accuracy\": 0.8578, \"sica_self_accuracy\": 0.5931, \"delta_oracle_sc_pp\": 29.9, \"delta_oracle_sica_pp\": 26.47, \"mcnemar_oracle_vs_sc_p\": 9.99e-14, \"mcnemar_oracle_vs_sc_b\": 63, \"mcnemar_oracle_vs_sc_c\": 2, \"mcnemar_oracle_vs_sica_p\": 7.84e-12, \"mcnemar_oracle_vs_sica_b\": 57, \"mcnemar_oracle_vs_sica_c\": 3, \"z3_gold_agreement\": 0.951, \"fol_parse_success\": 1, \"oracle_true_acc\": 0.875, \"oracle_false_acc\": 0.778, \"oracle_unknown_acc\": 0.913, \"n\": 204, \"utilization_pct\": 11.5}}, \"exp-wave3-dir-r-nli-verifier\": {\"status\": \"DONE\", \"hypothesis\": \"DeBERTa External Verifier: encoder-only NLI 模型 (cross-encoder/nli-deberta-v3-base) 与 decoder-only LLM 架构独立，作为额外 vote 加入 SC traces 可打破 confirmation bias。NLI 擅长 contradiction 检测（False label），LLM 擅长 Unknown 推理，两者互补。\", \"metrics\": {\"sc_accuracy\": 0.5441, \"nli_standalone\": 0.4951, \"combo_w1\": 0.5784, \"combo_w3\": 0.5882, \"intersection_acc\": 0.6848, \"intersection_coverage\": 0.451, \"delta_w1_pp\": 3.43, \"delta_w3_pp\": 4.41, \"mcnemar_w1_p\": 0.0391, \"mcnemar_w1_b\": 1, \"mcnemar_w1_c\": 8, \"mcnemar_w3_p\": 0.0784, \"mcnemar_w3_b\": 6, \"mcnemar_w3_c\": 15, \"ci95_w1\": [0.98, 6.37], \"ci95_w3\": [0, 8.82], \"nli_false_acc\": 0.7143, \"sc_false_acc\": 0.381, \"nli_unknown_acc\": 0.1884, \"sc_unknown_acc\": 0.6812, \"model_nli\": \"microsoft/deberta-large-mnli\", \"n\": 204}, \"conclusion\": \"success\"}, \"exp-wave3-dir-r-combo-extended\": {\"status\": \"DONE\", \"hypothesis\": \"R combo 策略扩展：测试 NLI 作为不同权重投票（w=1/3/5）、intersection+fallback、cascade（按 NLI confidence 分流）、weighted averaging 等策略。寻找 NLI+SICA/SC 最优融合方式。\", \"conclusion\": \"success\", \"metrics\": {\"sc_accuracy\": 0.5441, \"sica_accuracy\": 0.5931, \"nli_standalone\": 0.4951, \"best_combo\": \"nli_sc_vote_w5\", \"best_combo_acc\": 0.6029, \"best_delta_sc_pp\": 5.88, \"best_delta_sica_pp\": 0.98, \"nli_sc_vote_w3\": 0.5882, \"intersection_sica_fallback\": 0.5931, \"intersection_sc_fallback\": 0.5735, \"oracle_upper_bound\": 0.7549, \"sica_nli_agreement\": 0.475, \"agreement_accuracy\": 0.701, \"n\": 204}}, \"exp-wave3-dir-k-minority\": {\"status\": \"DONE\", \"hypothesis\": \"Minority Report: 当 SICA 错误时，少数派 traces 可能更 consistent（Z3 约束内部自洽性更高）。如果少数派 consistency > 多数派，用 consistency-weighted voting 替代 majority vote 可以纠正部分错误。测试 strict/moderate/combined 三种策略。\", \"metrics\": {\"sc_accuracy\": 0.5441, \"strict_accuracy\": 0.5441, \"strict_delta_pp\": 0, \"moderate_accuracy\": 0.4951, \"moderate_delta_pp\": -4.9, \"combined_accuracy\": 0.5441, \"combined_delta_pp\": 0, \"minority_consistency_precision\": 0.3553, \"minority_gt_rate\": 0.3373, \"majority_gt_rate\": 0.488, \"moderate_flips\": 76, \"moderate_correct_flips\": 27, \"moderate_wrong_flips\": 49, \"n\": 204}, \"conclusion\": \"negative\"}, \"exp-wave3-dir-i-z3-filter\": {\"status\": \"DONE\", \"hypothesis\": \"Z3 Trace Filter: Per-trace FOL constraint set SAT/UNSAT check can identify internally contradictory traces; filtering them before SC voting will improve accuracy by removing logically flawed reasoning.\", \"conclusion\": \"negative\", \"metrics\": {\"n\": 204, \"sc_baseline\": 54.41, \"filtered_sc\": 53.92, \"delta_pp\": -0.49, \"unsat_traces\": 142, \"unsat_rate_pct\": 5.8, \"filter_precision_pct\": 49.12, \"questions_affected\": 7, \"improved\": 3, \"degraded\": 4}}, \"exp-wave3-dir-j-bootstrap\": {\"status\": \"DONE\", \"hypothesis\": \"Bootstrapped Gold Approximation: Iterative conditional FOL extraction (using current best answer as condition) with Z3 consistency checks will progressively refine answers across rounds, converging to higher accuracy than single-pass SC.\", \"conclusion\": \"negative\", \"metrics\": {\"n\": 204, \"sc_baseline\": 54.41, \"r1_accuracy\": 56.86, \"r1_delta_pp\": 2.45, \"r1_flips\": 32, \"r1_improved\": 15, \"r1_degraded\": 10, \"r2_accuracy\": 54.41, \"r3_accuracy\": 54.9, \"r4_accuracy\": 54.41, \"r5_accuracy\": 52.45, \"convergence\": \"oscillating, no convergence\"}}, \"exp-cross-model-phase2\": {\"status\": \"DONE\", \"hypothesis\": \"Cross-model SICA: Aggregating traces from 3 model families (Mistral+LLaMA+Qwen, K=12 total) via SICA MAX-SAT will outperform cross-model SC by leveraging constraint diversity across architectures.\", \"conclusion\": \"negative\", \"metrics\": {\"n\": 204, \"cross_sc_accuracy\": 74.51, \"cross_sica_accuracy\": 74.02, \"delta_pp\": -0.49, \"mcnemar_p\": 1, \"config\": \"Mistral-7B(4) + LLaMA-8B(4) + Qwen-7B(4), K=12\"}}, \"exp-direction-d-cegis\": {\"status\": \"DONE\", \"hypothesis\": \"CEGIS: Iterative counterexample-guided constraint refinement will improve SICA by using Z3 counterexamples to strengthen constraints across multiple rounds, breaking the single-pass extraction bottleneck.\", \"conclusion\": \"negative\", \"metrics\": {\"n\": 204, \"sc_baseline\": 54.41, \"r1_accuracy\": 57.84, \"r1_delta_pp\": 3.43, \"r2_accuracy\": 57.35, \"r2_delta_pp\": 2.94, \"r3_accuracy\": 57.84, \"r3_delta_pp\": 3.43, \"r1_unsat_traces\": 127, \"r2_unsat_traces\": 48, \"r3_unsat_traces\": 25, \"wall_time_min\": 51, \"extraction_calls\": 2448, \"refinement_calls\": 175}}, \"exp-confirmation-bias\": {\"status\": \"DONE\", \"hypothesis\": \"Confirmation Bias quantification: Self-extracted constraints systematically point toward the majority answer even when it is wrong, creating a bias ratio significantly above 1.0 that explains SICA's failure mode.\", \"conclusion\": \"success\", \"metrics\": {\"bias_ratio\": 4.97, \"wrong_constraints_when_sica_errs\": 0.833, \"sica_errors_follow_sc\": 0.94}}, \"exp-cross-model-phase1\": {\"status\": \"DONE\", \"hypothesis\": \"Cross-model aggregation: Mixing traces from different model families (Mistral/LLaMA/Qwen) will reduce inter-trace κ below the same-model ceiling of 0.41, increasing effective sample size.\", \"conclusion\": \"success\", \"metrics\": {\"kappa_cross\": 0.422, \"kappa_within\": 0.532, \"eff_k_cross\": 2.11, \"eff_k_within\": 1.52, \"accuracy_gain\": 0}}, \"exp-direction-e-abstention\": {\"status\": \"DONE\", \"hypothesis\": \"Selective Abstention: Per-question answer entropy can serve as a reliable uncertainty signal; abstaining on high-entropy questions will improve accuracy on the remaining covered set.\", \"conclusion\": \"success\", \"metrics\": {\"auroc\": 0.673, \"coverage_80pct_delta_pp\": 4.4, \"coverage_60pct_delta_pp\": 8.8}}, \"exp-wild6-kappa-aware-sc\": {\"status\": \"DONE\", \"hypothesis\": \"κ-aware SC: Weighting traces by per-question agreement level (inverse κ) in majority voting will improve SC by giving more weight to diverse-opinion questions where voting has more signal.\", \"conclusion\": \"negative\", \"metrics\": {\"conditions_tested\": 11, \"delta_pp_all\": 0, \"finding\": \"accuracy monotonically increases with agreement, SC already optimal\"}}, \"exp-wild1-max-unsat\": {\"status\": \"DONE\", \"hypothesis\": \"MAX-UNSAT: Penalizing constraints in the unsatisfiable set (MIN-UNSAT variant) will improve SICA by actively downweighting contradictory constraints rather than only rewarding satisfiable ones.\", \"conclusion\": \"negative\", \"metrics\": {\"min_unsat_delta_pp\": -6.5, \"mean_excluded_constraints\": 1.3}}, \"exp-wild4-process-kappa\": {\"status\": \"DONE\", \"hypothesis\": \"Process-κ: CoT reasoning process similarity (cosine) correlates with answer agreement, and measuring process-level κ reveals whether traces that agree on answers actually use similar reasoning paths.\", \"conclusion\": \"negative\", \"metrics\": {\"answer_kappa\": 0.4093, \"process_cosine_mean\": 0.6902, \"pearson_r\": -0.064, \"pearson_p\": 0.36, \"same_answer_diff_process_pct\": 9.3}}, \"exp-direction-a-prove\": {\"status\": \"DONE\", \"hypothesis\": \"PROVE: LLM-generated verification code (verify() functions) can serve as external verifiers to rerank SC candidates, bypassing the self-extraction bottleneck.\", \"conclusion\": \"negative\", \"metrics\": {\"code_gen_rate\": 0.152, \"conclusive_rate\": 0.078, \"conclusive_accuracy\": 0.5, \"prove_fallback_accuracy\": 0.716, \"sc_baseline\": 0.735, \"delta_pp\": -1.9}}, \"exp-direction-b-deepconf\": {\"status\": \"DONE\", \"hypothesis\": \"DeepConf: Low-confidence traces (by logprob) produce low-quality constraints; filtering them before SICA will improve accuracy by removing noise from the constraint pool.\", \"conclusion\": \"negative\", \"metrics\": {\"filtered_sc_75pct\": 52.9, \"filtered_sica_75pct\": 54.4, \"filtered_sc_50pct\": 52.9, \"logprob_correct\": -0.135, \"logprob_incorrect\": -0.141, \"delta_pp\": 0}}, \"exp-wild3-perturbation\": {\"status\": \"DONE\", \"hypothesis\": \"Problem perturbation (variable renaming, premise reordering) will reduce inter-trace kappa by producing different reasoning paths for semantically equivalent problems, testing whether correlation comes from surface form vs model bias.\", \"conclusion\": \"negative\", \"metrics\": {\"original_k4_kappa\": 0.59, \"perturbed_k4_kappa\": 0.696, \"mixed_k8_kappa\": 0.627, \"original_sc_acc\": 80, \"perturbed_sc_acc\": 76.7, \"mixed_sc_acc\": 80}}, \"exp-wild2-ascii\": {\"status\": \"DONE\", \"hypothesis\": \"ASCII padding in FOLIO prompts will reduce inter-trace Fleiss kappa by disrupting shared surface-level patterns, testing whether trace correlation comes from prompt content vs model architecture bias.\", \"conclusion\": \"negative\", \"metrics\": {\"group_a_standard_kappa\": 0.3906, \"group_b_fixed_padding_kappa\": 0.4006, \"group_c_variable_padding_kappa\": 0.3638, \"group_a_sc_acc\": 53.92, \"group_b_sc_acc\": 57.84, \"group_c_sc_acc\": 53.92}}, \"exp-084-debate-mistral-logiqa-seed123\": {\"status\": \"DONE\", \"hypothesis\": \"Debate × Mistral-7B × LogiQA-200 seed=123 replication. exp-078 (seed=42) Δ=-23.0pp (catastrophic negative). Multi-seed 确认 Debate 在 LogiQA 上的大幅 negative 结果是否跨 seed 稳定。\", \"conclusion\": \"negative\", \"metrics\": {\"n\": 200, \"debate_accuracy\": 0.29, \"sc_accuracy\": 0.505, \"delta\": -0.215, \"fallbacks\": 14, \"total_constraints\": 3220, \"wall_time_min\": 226.3}}, \"exp-082-contrastive-mistral-folio-seed123\": {\"status\": \"DONE\", \"hypothesis\": \"Contrastive × Mistral-7B × FOLIO-204 seed=123 replication: verifying that the contrastive constraint generation pipeline produces consistent accuracy improvements over SC baseline when controlling for random seed, expecting accuracy within ±2pp of seed=42 run (exp-075b)\", \"metrics\": {\"sc_accuracy\": 0.549, \"contrastive_accuracy\": 0.4951, \"delta\": -0.0539, \"n_samples\": 204, \"wall_time_min\": 206.3, \"degenerate_count\": 35, \"pro_constraints\": 1036, \"con_constraints\": 920}, \"conclusion\": \"negative\"}, \"exp-081-debate-mistral-folio-seed123\": {\"status\": \"DONE\", \"hypothesis\": \"Debate × Mistral-7B × FOLIO-204 seed=123 replication: verifying that the debate-augmented constraint extraction pipeline produces consistent accuracy improvements over SC baseline when controlling for random seed, expecting accuracy within ±2pp of seed=42 run (exp-076)\", \"metrics\": {\"sc_accuracy\": 0.5588, \"debate_accuracy\": 0.4069, \"delta\": -0.152, \"n_samples\": 204, \"wall_time_min\": 177.6, \"fallbacks\": 18, \"both_correct\": 56, \"debate_improved\": 27, \"debate_degraded\": 58, \"both_wrong\": 63}, \"conclusion\": \"negative\"}, \"exp-085-contrastive-mistral-logiqa-seed123\": {\"status\": \"DONE\", \"hypothesis\": \"Contrastive × Mistral-7B × LogiQA-200 seed=123 multi-seed replication。exp-080 (seed=42) Δ=-4.5pp (negative)。跨 seed 确认 Contrastive 在 LogiQA 上的 negative 结果稳定性，排除单 seed 偶然。\", \"conclusion\": \"negative\", \"metrics\": {\"n\": 200, \"contrastive_accuracy\": 0.535, \"sc_accuracy\": 0.56, \"delta\": -0.025, \"delta_pp\": -2.5, \"contrastive_correct\": 107, \"sc_correct\": 112, \"k\": 12, \"k_contrast\": 3, \"temperature\": 0.7, \"seed\": 123, \"degenerate_count\": 51, \"total_pro_constraints\": 736, \"total_con_constraints\": 1059, \"wall_time_min\": 100.9}}, \"exp-075b-contrastive-mistral-folio\": {\"status\": \"DONE\", \"hypothesis\": \"Contrastive × Mistral-7B × FOLIO-204 重跑（修复 normalization bug 后）。对每个候选答案生成 pro/con FOL 约束，用 normalized contrastive 评分代替同源约束。exp-075 因 session crash + normalization bug 失败。如果 normalized contrastive 约束提供独立于 traces 的判别信号，delta(Contrastive vs SC) > delta(SICA vs SC)。\", \"conclusion\": \"negative\", \"metrics\": {\"sc_accuracy\": 0.5686, \"contrastive_accuracy\": 0.4755, \"delta\": -0.0931, \"n_samples\": 204, \"wall_time_min\": 193.6, \"degenerate_count\": 41}}, \"exp-080-contrastive-mistral-logiqa200\": {\"status\": \"DONE\", \"hypothesis\": \"Contrastive constraint generation with MAX-SAT consensus (SICA) transfers from FOLIO to LogiQA, improving accuracy over self-consistency baseline on 200 LogiQA problems with Mistral-7B (seed=42).\", \"conclusion\": \"negative\", \"metrics\": {\"n\": 200, \"contrastive_accuracy\": 0.455, \"sc_accuracy\": 0.5, \"delta\": -0.045, \"k\": 12, \"k_contrast\": 3, \"temperature\": 0.7, \"seed\": 42, \"total_wall_time_s\": 6645.9, \"total_pro_constraints\": 762, \"total_con_constraints\": 1192, \"degenerate_count\": 42}}, \"exp-078-debate-mistral-logiqa200\": {\"status\": \"DONE\", \"hypothesis\": \"Debate-augmented extraction with MAX-SAT consensus (SICA) transfers cross-dataset from FOLIO (3-class) to LogiQA (4-choice multichoice), maintaining accuracy gains over self-consistency baseline on 200 LogiQA problems with Mistral-7B.\", \"conclusion\": \"negative\", \"metrics\": {\"sc_accuracy\": 0.5, \"debate_accuracy\": 0.27, \"delta\": -0.23, \"n_samples\": 200, \"wall_time_min\": 211.5, \"fallbacks\": 16}}, \"exp-078\": {\"status\": \"DONE\", \"conclusion\": \"negative\", \"metrics\": {\"sc_accuracy\": 0.5, \"debate_accuracy\": 0.27, \"delta\": -0.23, \"n_samples\": 200, \"fallbacks\": 16, \"wall_time_min\": 211.5}, \"hypothesis\": \"Multi-agent debate among Mistral-7B instances on LogiQA improves accuracy over self-consistency because inter-agent argumentation corrects reasoning errors that independent sampling cannot, yielding a positive delta on 200 problems.\"}, \"exp-083-icg-mistral-logiqa-seed123\": {\"status\": \"DONE\", \"hypothesis\": \"ICG × Mistral-7B × LogiQA-200 seed=123 multi-seed replication。exp-079 (seed=42) Δ=-0.5pp (negative)。跨数据集 multi-seed 确认 ICG 方法在 LogiQA 上的 negative 结果稳定性。\", \"conclusion\": \"negative\", \"metrics\": {\"n\": 200, \"sc_accuracy\": 0.365, \"icg_accuracy\": 0.33, \"delta_pp\": -3.5, \"sc_correct\": 73, \"icg_correct\": 66, \"both_correct\": 62, \"sc_only\": 11, \"icg_only\": 4, \"neither\": 123, \"mean_constraints_generated\": 31.4, \"mean_constraints_unique\": 27.9, \"mean_maxsat_satisfied\": 27.7, \"mean_maxsat_excluded\": 0.2, \"wall_time_s\": 3653.7, \"mean_wall_time_s\": 18.3}}, \"exp-074d-icg-mistral-folio-seed456\": {\"status\": \"DONE\", \"hypothesis\": \"ICG × Mistral-7B × FOLIO-204 seed=456 第三组 seed replication。exp-074 (seed=42) Δ=-2.0pp, exp-074c (seed=123) 运行中。3-seed 数据确认 ICG 方法的 negative 结果跨 seed 稳定性，堵住 reviewer 单 seed 质疑。ICG 是三方法中 Δ 最接近零的，3-seed 数据最有论文价值。\", \"conclusion\": \"negative\", \"metrics\": {\"sc_accuracy\": 0.5588, \"icg_accuracy\": 0.549, \"delta\": -0.0098, \"n_samples\": 204, \"wall_time_min\": 57.3, \"three_seed_mean_sc\": 0.5572, \"three_seed_mean_icg\": 0.5523, \"three_seed_mean_delta\": -0.0049, \"three_seed_std_delta\": 0.0177, \"three_seed_details\": {\"seed_42\": {\"sc\": 0.5392, \"icg\": 0.5196, \"delta\": -0.0196}, \"seed_123\": {\"sc\": 0.5735, \"icg\": 0.5882, \"delta\": 0.0147}, \"seed_456\": {\"sc\": 0.5588, \"icg\": 0.549, \"delta\": -0.0098}}}}, \"exp-077-kappa-generalization\": {\"status\": \"DONE\", \"hypothesis\": \"High Fleiss kappa (low independence) is a general property of same-model aggregation, not specific to SC+SICA. LLM-Debate and Diverse-Prompt aggregation on Mistral-7B will also exhibit high kappa and low Effective K, confirming the independence bottleneck is fundamental to single-model ensembles regardless of aggregation method.\", \"conclusion\": \"negative\", \"metrics\": {\"sc_kappa\": 0.4384, \"sc_eff_k\": 2.02, \"sc_nominal_k\": 10, \"debate_kappa\": 0.1549, \"debate_eff_k\": 4.44, \"debate_nominal_k\": 12, \"diverse_prompt_kappa\": 0.403, \"diverse_prompt_eff_k\": 2.21, \"diverse_prompt_nominal_k\": 12, \"n_samples\": 204}}, \"exp-077\": {\"status\": \"DONE\", \"metrics\": {\"sc_kappa\": 0.4384, \"sc_eff_k\": 2.02, \"debate_kappa\": 0.1549, \"debate_eff_k\": 4.44, \"diverse_prompt_kappa\": 0.403, \"diverse_prompt_eff_k\": 2.21, \"n_questions\": 204, \"all_kappa_gt_04\": false, \"wall_time_min\": 184.9}, \"conclusion\": \"negative\", \"hypothesis\": \"All three LLM aggregation methods (Self-Consistency, LLM-Debate, Diverse-Prompt) suffer from the same independence bottleneck (Fleiss' κ > 0.4), because the shared model backbone forces correlated reasoning traces regardless of the aggregation strategy used.\"}, \"exp-075b\": {\"status\": \"DONE\", \"conclusion\": \"negative\", \"metrics\": {\"sc_accuracy\": 0.5686, \"contrastive_accuracy\": 0.4755, \"delta\": -0.0931, \"n_samples\": 204, \"degenerate\": 41, \"wall_time_min\": 193.6}, \"hypothesis\": \"Contrastive pro/con argumentation with normalized scoring improves self-consistency accuracy on FOLIO logical reasoning over standard SC majority voting, by surfacing symbolic invariants through structured debate.\"}, \"exp-074c-icg-mistral-folio-seed123\": {\"status\": \"DONE\", \"hypothesis\": \"ICG × Mistral-7B × FOLIO-204 seed=123 replication. exp-074 (seed=42) Δ=-2.0pp (negative). Multi-seed replication 确认 ICG 方法的 negative 结果是否跨 seed 稳定。如果 seed=123 也 negative，堵住 reviewer 单 seed 质疑。\", \"metrics\": {\"sc_accuracy\": 0.5735, \"icg_accuracy\": 0.5882, \"delta\": 0.0147, \"n_samples\": 204, \"wall_time_min\": 56.5}, \"conclusion\": \"negative\"}, \"exp-076-debate-mistral-folio\": {\"status\": \"DONE\", \"hypothesis\": \"Debate-Augmented Extraction: 同模型 Proposer/Critic 对抗辩论生成多样化推理路径，从完整辩论记录提取 FOL 约束 + MAX-SAT 评分。在 Mistral-7B FOLIO-204 上测试。Dry-run 3 题 Debate 100% vs SC 67%。如果辩论打破 trace 同源性，delta(Debate vs SC) > delta(SICA vs SC)。parent=exp-033\", \"conclusion\": \"negative\", \"metrics\": {\"sc_accuracy\": 0.5686, \"debate_accuracy\": 0.3824, \"delta\": -0.1863, \"n_samples\": 204, \"wall_time_min\": 186.4, \"fallbacks\": 10, \"total_debate_constraints\": 3677}}, \"exp-079-icg-mistral-logiqa200\": {\"status\": \"DONE\", \"hypothesis\": \"ICG × Mistral-7B × LogiQA-200 cross-dataset validation. 验证 ICG 方法在 LogiQA 多选题上是否有效。与 exp-074 (ICG×FOLIO) 和 exp-078 (Debate×LogiQA) 对比，构建方法×数据集交叉矩阵。如果 ICG 在 LogiQA 上也无效，进一步确认 independence bottleneck 的普遍性。\", \"conclusion\": \"negative\", \"metrics\": {\"sc_accuracy\": 0.475, \"icg_accuracy\": 0.47, \"delta\": -0.005, \"n_samples\": 200, \"wall_time_min\": 54.3}}, \"exp-072b-llama8b-logiqa200\": {\"status\": \"DONE\", \"hypothesis\": \"LLaMA-3.1-8B-Instruct on LogiQA-200 with canonical SICA code (k=12, seed=42)（重跑）。exp-072 因 session crash 失败。产出 valid comparable SICA scores，replacing exp-069 which used outdated code.\", \"conclusion\": \"negative\", \"metrics\": {\"sc_accuracy\": 0.595, \"sica_accuracy\": 0.585, \"delta\": -0.01, \"n_samples\": 200, \"k\": 12, \"wall_time_s\": 7310.5, \"extraction_success\": 2292, \"extraction_fail_json_parse\": 108}}, \"exp-074-icg-mistral-folio\": {\"status\": \"DONE\", \"hypothesis\": \"ICG (Independent Constraint Generation): 独立于 reasoning traces 生成 FOL 约束，绕过 trace-sourced confirmation bias。直接从问题 premises 提取逻辑约束（不解题），用独立约束 + MAX-SAT 评分候选答案。在 Mistral-7B FOLIO-204 上测试，与标准 SICA (同源约束) 对比。预期：如果独立约束有效，delta(ICG vs SC) > delta(SICA vs SC)。\", \"metrics\": {\"sc_accuracy\": 0.5392, \"icg_accuracy\": 0.5196, \"delta\": -0.0196, \"n_samples\": 204, \"k\": 12, \"k_icg\": 10, \"wall_time_s\": 3368}, \"conclusion\": \"negative\"}, \"exp-073b-qwen7b-logiqa200-seed456\": {\"status\": \"DONE\", \"hypothesis\": \"Qwen2.5-7B LogiQA seed=456 第三组 seed replication（重跑）。exp-073 因 session crash 失败。exp-070 (seed=42) SC=68.5% Δ=+2.5pp, exp-071 (seed=123) SC=69% Δ=-0.5pp。seed=456 是 Goldilocks tie-breaker。\", \"metrics\": {\"sc_accuracy\": 0.695, \"sica_accuracy\": 0.715, \"delta\": 0.02, \"n_samples\": 200, \"k\": 12, \"wall_time_s\": 3517.3}, \"conclusion\": \"success\"}, \"exp-073-qwen7b-logiqa200-seed456\": {\"status\": \"DONE\", \"hypothesis\": \"Qwen2.5-7B LogiQA seed=456 第三组 seed replication。exp-070 (seed=42) SC=68.5% Δ=+2.5pp, exp-071 (seed=123) 进行中。seed=456 加固第二个 Goldilocks 数据点。如果 3 seeds 方向一致，累积证据支持 Qwen2.5-7B 在 LogiQA 上处于 Goldilocks regime。\", \"conclusion\": \"success\", \"metrics\": {\"sc_accuracy\": 0.7, \"sica_accuracy\": 0.705, \"delta\": 0.005, \"n_samples\": 200}}, \"exp-072-llama8b-logiqa200\": {\"status\": \"DONE\", \"hypothesis\": \"LLaMA-3.1-8B-Instruct on LogiQA-200 with canonical SICA code (k=12, seed=42) will produce valid comparable SICA scores, replacing exp-069 which used outdated code.\", \"conclusion\": \"success\", \"metrics\": {\"sc_accuracy\": 0.62, \"sica_accuracy\": 0.63, \"delta\": 0.01, \"n_samples\": 200}}, \"exp-064-deepseek-r1-qwen3-8b-folio204\": {\"status\": \"DONE\", \"hypothesis\": \"DeepSeek-R1-0528-Qwen3-8B (reasoning distill) 在 FOLIO-204 上 SICA vs SC。测试 reasoning 模型在 8B scale 是否出现 degenerate regime (C₀<5%) 或因 8B 能力较弱落入 error amplification / Goldilocks zone。\", \"conclusion\": \"success\", \"notes\": \"code_version=westd-16639-legacy, sica_not_comparable. 旧代码启动，SC 数据可用（不受代码版本影响），SICA/delta 不入 Table 1。Director 指令 2026-05-19T15:25 UTC。\", \"metrics\": {\"sc_accuracy\": 0.8382, \"sica_accuracy\": 0.8382, \"delta\": 0, \"n_samples\": 204, \"extraction_rate\": 0.3818, \"contradiction_rate\": 0.0165, \"wall_time_min\": 355.6}}, \"exp-075-contrastive-mistral-folio\": {\"status\": \"DONE\", \"hypothesis\": \"Contrastive Constraint Generation: 对每个候选答案生成 pro/con FOL 约束，用对比评分代替同源约束。在 Mistral-7B FOLIO-204 上测试。如果 contrastive 约束提供独立于 traces 的判别信号，delta(Contrastive vs SC) > delta(SICA vs SC)。parent=exp-033\", \"conclusion\": \"failed\"}, \"exp-077-generalization-kappa\": {\"status\": \"PREPARING\", \"hypothesis\": \"Generalization: independence bottleneck (high κ) applies to Debate and Diverse-Prompt aggregation, not just SC+SICA. 在 Mistral-7B FOLIO-204 上测量 3 种聚合方式的 Fleiss' κ + Eff-K: (a) Standard SC (复用 exp-033 traces), (b) LLM-Debate traces (4组×3轮=12 answer points), (c) Diverse-Prompt traces (4种 prompt×3次=12). 如果三种方式 κ 均 > 0.4，证明 independence bottleneck 是 same-model aggregation 的通病。\"}, \"exp-071-qwen7b-logiqa200-seed123\": {\"status\": \"DONE\", \"hypothesis\": \"exp-070 seed replication: Qwen2.5-7B-Instruct 在 LogiQA-200 上 SICA vs SC, seed=123。exp-070 (seed=42) SC=68.5% Δ=+2.5pp p=0.125, 7 个 discordant pairs 统计功效不足。seed replication 加固 Goldilocks zone claim。如果 seed=123 也给出正向 Δ 且方向一致，则累积证据支持 Qwen2.5-7B 在 LogiQA 上处于 Goldilocks regime。\", \"conclusion\": \"negative\", \"metrics\": {\"sc_accuracy\": 0.69, \"sica_accuracy\": 0.685, \"delta\": -0.005, \"n_samples\": 200}}, \"exp-048-llama8b-pw600\": {\"status\": \"DONE\", \"hypothesis\": \"LLaMA-3.1-8B-Instruct 在 ProofWriter-600 上 SICA vs SC。FOLIO-204 上 LLaMA-8B SC=63.2% delta=-2.45pp (exp-020)。PW 是更结构化的形式推理数据集，测试 SICA 在 PW 上对低能力模型是否有效（补充 regime boundary 跨域证据）。parent=exp-020\", \"conclusion\": \"negative\", \"notes\": \"code_version=westd-16639-legacy, sica_not_comparable. Reviewer verified: SC=70%, SICA=64.8%, delta=-5.2pp, n=600.\", \"metrics\": {\"sc_accuracy\": 0.7, \"sica_accuracy\": 0.648, \"delta\": -0.052, \"n_samples\": 600}}, \"exp-053-mistral-folio204-seed456\": {\"status\": \"DONE\", \"hypothesis\": \"exp-033 replication (seed=456): Mistral-7B FOLIO-204 K=12 T=0.7，第二组独立 replication。与 exp-052 (seed=123) 一起验证 exp-033 结论 robustness。parent=exp-033\", \"conclusion\": \"killed\", \"notes\": \"Stale duplicate. 实际实验已在 exp-053 (短 ID) 下完成 (DONE)。本条目是重复创建的长名称版本，清理。\"}, \"exp-052-mistral-folio204-seed123\": {\"status\": \"DONE\", \"hypothesis\": \"exp-033 replication (seed=123): Mistral-7B FOLIO-204 K=12 T=0.7，与 exp-033 (seed=42, delta=+4.90pp, p=0.013) 完全相同配置，仅 seed 不同。验证正向结果是否 seed-robust。parent=exp-033\", \"conclusion\": \"killed\", \"notes\": \"Stale duplicate. 实际实验已在 exp-052 (短 ID) 下完成 (DONE)。本条目是重复创建的长名称版本，清理。\"}, \"exp-069-llama8b-logiqa200\": {\"status\": \"DONE\", \"hypothesis\": \"LLaMA-3.1-8B-Instruct 在 LogiQA-200 上 SICA vs SC。FOLIO-204 上 LLaMA-8B SC=66.18% delta=-4.41pp (exp-063, negative/error amplification)。LogiQA 上 Mistral-7B SC=51% delta=+0.5pp (exp-049b)，Qwen2.5-14B SC=78.5% delta=-0.50pp (exp-038)。测试 LLaMA-8B 在 LogiQA 上的 regime（SC 预计 50-60%，可能在 error amplification zone）。parent=exp-063-llama8b-folio204-16639\", \"notes\": \"code_version=westd-16639-legacy. Reviewer verified: SC=61%, SICA=58.5%, delta=-2.5pp, n=200.\", \"conclusion\": \"negative\", \"metrics\": {\"sc_accuracy\": 0.61, \"sica_accuracy\": 0.585, \"delta\": -0.025, \"n_samples\": 200}}, \"exp-065-qwen7b-pw600\": {\"status\": \"DONE\", \"hypothesis\": \"Qwen2.5-7B 在 PW-D5-600 上 SICA vs SC。FOLIO SC=75.98% (confirmation bias)，PW 更难 SC 预计更低，测试不同 regime。parent=exp-061\", \"conclusion\": \"negative\", \"metrics\": {\"sc_accuracy\": 0.72, \"sica_accuracy\": 0.68, \"delta\": -0.04, \"n_samples\": 600}}, \"exp-062-gemma27b-folio204\": {\"status\": \"DONE\", \"hypothesis\": \"Gemma-3-27B-IT (Google 架构) FOLIO-204 SICA vs SC。跨模型家族验证 regime-dependent pattern。27B 能力预计在 Qwen2.5-14B (~75% SC) 和 Qwen3-14B (~85% SC) 之间。\", \"conclusion\": \"negative\", \"metrics\": {\"sc_accuracy\": 0.809, \"sica_accuracy\": 0.804, \"delta\": -0.005, \"n_samples\": 204}}, \"exp-069-mistral-logiqa200\": {\"status\": \"DONE\", \"hypothesis\": \"Mistral-7B-Instruct-v0.3 在 LogiQA-200 上 SICA vs SC。FOLIO-204 上 Mistral 是唯一 Goldilocks 候选 (SC≈55%, Δ=+4.90pp seed=42)。如果 LogiQA SC 也在 55-65% 且 Δ>0，则跨数据集验证 Goldilocks zone 存在。parent=exp-033\", \"conclusion\": \"negative\", \"metrics\": {\"sc_accuracy\": 0.495, \"sica_accuracy\": 0.465, \"delta\": -0.03, \"n_samples\": 200}, \"notes\": \"与 exp-049b 结果不一致调查：5/7 SICA 核心模块代码版本不同（md5 全部不匹配）。关键差异：scorer.py tie-breaking（049b: max() 随机 vs 069: sorted() 字母序）、constraint_extractor/z3_maxsat/pipeline 均有变化。049b 还设了 VLLM_USE_FLASHINFER_SAMPLER=0。prompt 模板相同。两组数据不可直接比较。exp-069 使用 westd-25068 上的最新代码版本。\"}, \"exp-070-qwen7b-logiqa200\": {\"status\": \"DONE\", \"hypothesis\": \"Qwen2.5-7B-Instruct 在 LogiQA-200 上 SICA vs SC。FOLIO 上 SC=75.98% (Type A confirmation bias, Δ=+0.49pp)。LogiQA 可能更难，SC 可能降到 55-65% 进入 Goldilocks zone，或保持 >75% 继续 Type A。验证 regime 跨数据集一致性。parent=exp-061\", \"conclusion\": \"success\", \"metrics\": {\"sc_accuracy\": 0.685, \"sica_accuracy\": 0.71, \"delta\": 0.025, \"n_samples\": 200, \"sc_correct\": 137, \"sica_correct\": 142, \"discordant_b\": 1, \"discordant_c\": 6, \"mcnemar_chi2\": 2.2857, \"mcnemar_p\": 0.131, \"mcnemar_p_exact\": 0.125, \"significant_005\": false, \"cohens_kappa\": 0.917, \"kappa_interpretation\": \"almost_perfect\"}, \"notes\": \"Reviewer 独立验证（从 exp070_results.json 确认）：SC=137/200=68.5%, SICA=142/200=71.0%, Δ=+2.5pp。原 diagnostic worker 读取了错误数据源，误报 SC=SICA=79.5%（差距 11pp/22题）。已由 Director 指令修正。\"}, \"exp-068-qwen3-logiqa200\": {\"status\": \"DONE\", \"hypothesis\": \"Qwen3-14B non-thinking 在 LogiQA-200 上 SICA vs SC。FOLIO SC=84.80%, PW SC=85.0%，LogiQA 预计也在 confirmation bias zone。验证跨数据集 Type A 一致性。parent=exp-040\", \"notes\": \"Reviewer 独立验证：输出文件完整，200/200 样本已处理。SC=SICA=0.81，null effect。原被 CRON 错误标记为 failed（无 W&B 数据时默认标 failed）。\", \"conclusion\": \"negative\", \"metrics\": {\"sc_accuracy\": 0.81, \"sica_accuracy\": 0.81, \"delta\": 0, \"n_samples\": 200}}, \"exp-064\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"exp-067-mistral-folio-seed789\": {\"status\": \"DONE\", \"hypothesis\": \"Mistral-7B FOLIO seed=789 第4 seed replication。已有 s42 +3.43pp, s123 +2.94pp, s456 0.00pp。增加统计样本验证 seed variance 和 SC-Δ 相关性。parent=exp-033\", \"conclusion\": \"success\", \"metrics\": {\"sc_accuracy\": 0.5441, \"sica_accuracy\": 0.5392, \"delta_pp\": -0.49, \"n\": 204, \"mcnemar_b\": 6, \"mcnemar_c\": 5, \"mcnemar_p\": 1, \"mcnemar_significant\": false, \"fleiss_kappa_raw\": 0.4124, \"eff_k\": 2.17}}, \"exp-063-llama8b-folio204-16639\": {\"status\": \"DONE\", \"hypothesis\": \"LLaMA-3.1-8B-Instruct 在 FOLIO-204 上 SICA vs SC。此前 exp-020 在不同服务器上跑过 (SC=63.2%, delta=-2.45pp)，本实验在 westd-16639 复现并用修正后的 alphabetical tie-breaking SC。parent=exp-020\", \"conclusion\": \"negative\", \"metrics\": {\"sc_accuracy\": 0.6618, \"sica_accuracy\": 0.6176, \"delta_pp\": -4.41, \"n\": 204, \"mcnemar_b\": 16, \"mcnemar_c\": 7, \"mcnemar_p\": 0.0931, \"mcnemar_significant\": false}}, \"exp-063-llama8b-folio204\": {\"status\": \"PREPARING\", \"conclusion\": \"negative\", \"metrics\": {\"n\": 204, \"sc_accuracy\": 0.6618, \"sica_accuracy\": 0.6176, \"delta_pp\": -4.41}}, \"exp-061-qwen7b-folio204\": {\"status\": \"DONE\", \"hypothesis\": \"Qwen2.5-7B-Instruct 在 FOLIO-204 上 SICA vs SC。SC 预计 55-65%（介于 Mistral-7B ~55% 和 Qwen2.5-14B ~75% 之间），可能在 Goldilocks zone。\", \"conclusion\": \"negative\", \"metrics\": {\"n\": 204, \"sc_accuracy\": 0.7598, \"sica_accuracy\": 0.7647, \"delta_pp\": 0.49}}, \"exp-059-cross-qwen3-extractor\": {\"status\": \"DONE\", \"hypothesis\": \"Qwen3-14B cross-model extraction should produce higher quality FOL constraints than Mistral-7B self-extraction (breaking confirmation bias), leading to higher SICA discriminative rate and accuracy delta over SC baseline.\", \"conclusion\": \"success\", \"metrics\": {\"n\": 204, \"cross_sica_accuracy\": 0.6029, \"orig_sica_accuracy\": 0.5931, \"sc_accuracy\": 0.5588, \"delta_cross_vs_sc_pp\": 4.41, \"delta_cross_vs_orig_pp\": 0.98}}, \"exp-063\": {\"status\": \"DONE\", \"hypothesis\": \"LLaMA-3.1-8B-Instruct FOLIO-204 SICA vs SC（Meta 架构覆盖）。exp-020 旧数据 SC=63.2% delta=-2.45pp，本实验用修正 tie-breaking 重跑。parent=exp-020\", \"conclusion\": \"negative\", \"metrics\": {\"n\": 204, \"sc_accuracy\": 0.6618, \"sica_accuracy\": 0.6176, \"delta_pp\": -4.41}}, \"exp-040-qwen3-pw600-16639\": {\"status\": \"DONE\", \"hypothesis\": \"Qwen3-14B non-thinking 在 ProofWriter-600 全量上 SICA vs SC：跨模型代际验证 capability trap 在 PW 数据集上是否持续。与 exp-039 (Qwen2.5-14B PW-600) 对比代际差异。\", \"notes\": \"westd-16639 实际目录: exp033_qwen3_14b_pw600_nonthinking, tmux: exp033, port: 8001, GPU 1. 162/600 (27.0%) at 22:28 UTC. Qwen3-14B thinking=false, 推理速度约为 Qwen2.5-14B 的一半。\", \"conclusion\": \"negative\", \"metrics\": {\"n\": 600, \"sc_accuracy\": 0.85, \"sica_accuracy\": 0.8567, \"delta_pp\": 0.67, \"extraction_rate\": 0.997, \"contradiction_rate\": 0.004, \"wall_time_min\": 1032.2, \"failure_type\": \"Type A (confirmation bias)\"}}, \"exp-060-cross-qwen25-14b-extractor\": {\"status\": \"DONE\", \"hypothesis\": \"Qwen2.5-14B 跨模型提取 FOL 约束。与 exp-033 (Mistral self-extraction) 和 exp-059 (Qwen3 cross-extraction) 对比。parent=exp-033\", \"conclusion\": \"negative\", \"metrics\": {\"n\": 204, \"cross_sica_accuracy\": 0.5833, \"orig_sica_accuracy\": 0.5931, \"sc_accuracy\": 0.5588, \"delta_cross_vs_sc_pp\": 2.45, \"delta_cross_vs_orig_pp\": -0.98, \"divergence_rate\": 0.059, \"wall_time_min\": 106.1}}, \"exp-057-mistral-folio204-t03\": {\"status\": \"DONE\", \"hypothesis\": \"T=0.3 低温 traces 更确定性更一致，SICA delta < T=0.7 的 +4.90pp。与 exp-054 (T=1.0, +0.49pp) 共同形成 T sensitivity ablation curve。parent=exp-033, D060 analysis paper\", \"conclusion\": \"negative\", \"metrics\": {\"n\": 204, \"sc_accuracy\": 0.5833, \"sica_accuracy\": 0.5686, \"delta_pp\": -1.47, \"mcnemar_p\": 0.5488}}, \"exp-034\": {\"status\": \"DONE\", \"hypothesis\": \"Qwen2.5-14B-Instruct 在 ProofWriter-600 上 SICA vs SC（westd-25068 重跑）：在 full 600 题上验证 capability trap，复现 sica_expanded_14b 的 PW 子集结果（delta=+0.3pp）。代替原 StrategyQA 实验（exp-034 v1 因 extraction prompt bug + 平台 kill 失败）。\", \"conclusion\": \"negative\", \"metrics\": {\"n_problems\": 93, \"n_target\": 600, \"completion_pct\": 15.5, \"sica_accuracy\": 77.42, \"sc_accuracy\": 74.19, \"delta_pp\": 3.23, \"sica_correct\": 72, \"sc_correct\": 69, \"mcnemar_discordant_b\": 6, \"mcnemar_discordant_c\": 3, \"mcnemar_p_value\": 0.5078, \"c0_non_unanimous_rate\": 0.581, \"avg_majority_frac\": 0.8324, \"extraction_rate\": 99.19, \"contradiction_rate\": 11.83, \"problems_with_contradictions\": 11, \"avg_unique_constraints\": 35.6, \"total_constraints\": 14437, \"unique_constraints\": 3308, \"dedup_ratio\": 22.9, \"k\": 12, \"level\": \"OWA-D5\", \"gt_distribution\": {\"True\": 32, \"False\": 28, \"Unknown\": 33}, \"wall_time_s\": 6086.4, \"status_note\": \"INCOMPLETE: crashed at 93/600 (python not found after conda env lost)\"}, \"notes\": \"v4 完成。tmux=exp034_run, westd-25068 cuda:1。Qwen2.5-14B on PW-600, delta=+0.50pp (不显著)。\"}, \"exp-039-14b-pw600-16639\": {\"status\": \"DONE\", \"hypothesis\": \"Qwen2.5-14B-Instruct 在 ProofWriter-600 全量上 SICA vs SC（westd-16639 重跑）：验证 capability trap 在 PW 数据集全量规模上是否持续。复现 sica_expanded_14b 的 PW 子集结果（delta=+0.3pp）。\", \"notes\": \"westd-16639 实际目录: exp032_qwen25_14b_pw600, tmux: exp032, port: 8000, GPU 0. 263/600 (43.8%) at 22:28 UTC.\", \"conclusion\": \"negative\", \"metrics\": {\"sica_accuracy\": 71.5, \"sc_accuracy\": 73.5, \"delta_pp\": -2.0, \"n_problems\": 600, \"extraction_rate\": 99.2, \"wall_time_min\": 659.6}}, \"exp-058-mistral-folio204-t05\": {\"status\": \"DONE\", \"hypothesis\": \"T=0.5 delta 介于 T=0.3 和 T=0.7 之间，形成温度-SICA delta 曲线。与 exp-033 (T=0.7, +4.90pp) 和 exp-054 (T=1.0, +0.49pp) 共同构成 4 点 T sensitivity ablation。parent=exp-033, D060 analysis paper\", \"conclusion\": \"negative\", \"metrics\": {\"sc_accuracy\": 57.84, \"sica_accuracy\": 57.35, \"delta_pp\": -0.49, \"mcnemar_p\": 1, \"discordant_b\": 3, \"discordant_c\": 2, \"n_problems\": 204, \"n_completed\": 204, \"extraction_rate\": 97, \"wall_time_min\": 80}}, \"exp-051-mistral-k-sensitivity\": {\"status\": \"DONE\", \"hypothesis\": \"Mistral-7B K sensitivity on FOLIO-204: K=[4,8,16,20]（K=12 已有 exp-033 delta=+4.90pp）。验证正向结果对 K 选择是否稳健。Reviewer 必问 ablation。parent=exp-033\", \"metrics\": {\"K4\": {\"SC\": 54.41, \"SICA\": 52.94, \"delta\": -1.47, \"b\": 7, \"c\": 10, \"McNemar_p\": 0.6291}, \"K8\": {\"SC\": 57.35, \"SICA\": 56.37, \"delta\": -0.98, \"b\": 4, \"c\": 6, \"McNemar_p\": 0.7539}, \"K12_exp033\": {\"SC\": 54.41, \"SICA\": 59.31, \"delta\": 4.9, \"b\": 12, \"c\": 2, \"McNemar_p\": 0.0129}, \"K16\": {\"SC\": 55.88, \"SICA\": 57.35, \"delta\": 1.47, \"b\": 10, \"c\": 7, \"McNemar_p\": 0.6291}, \"K20\": {\"SC\": 57.35, \"SICA\": 59.31, \"delta\": 1.96, \"b\": 5, \"c\": 1, \"McNemar_p\": 0.2188}}, \"conclusion\": \"success\", \"notes\": \"K sensitivity 完整 5 点数据确认 K=12 是最优点（delta=+4.90pp, p=0.013）。K<12 SICA 不如 SC（K=4: -1.47pp, K=8: -0.98pp），K>12 delta 回落但仍为正（K=16: +1.47pp, K=20: +1.96pp）。整体呈 peaked 曲线（非严格倒 U，K=20 略高于 K=16），但 K=12 peak 显著且两侧衰减明确。McNemar 仅 K=12 显著（p=0.013），其余 K 值均不显著。\"}, \"exp-055-multitemp-mistral-folio\": {\"status\": \"DONE\", \"hypothesis\": \"Multi-temperature sampling 通过强制 trace diversity 提升 Effective-K，预期 SICA delta > exp-033 的 +4.9pp。混合 T=0.3/0.7/1.2 各 4 traces 比单一 T=0.7 的 12 traces 产生更多独立视角，从而让 MAX-SAT 有更多 discriminative 信号。parent=exp-033, D059\", \"conclusion\": \"negative\", \"metrics\": {\"n\": 204, \"sc_accuracy\": 57.84, \"sica_accuracy\": 57.84, \"delta_pp\": 0, \"discordant_b\": 5, \"discordant_c\": 5, \"mcnemar_p\": 1, \"significant\": false, \"agreement_rate\": 0.951, \"wall_time_min\": 83.2, \"temperatures\": \"0.3,0.7,1.2\", \"k_per_temp\": \"4,4,4\"}}, \"exp-028b-qwen3-thinking-folio204\": {\"status\": \"DONE\", \"hypothesis\": \"Qwen3-14B thinking mode (enable_thinking=True, 32K context) 在 FOLIO-204 上 SICA vs SC。D028 pilot (35/204, delta=+2.86pp) 被 kill。thinking mode 产生更 diverse+higher-quality reasoning traces，如果同时提升 trace quality 和 diversity，可能打破 14B 级别的 capability trap。parent=exp-028\", \"conclusion\": \"killed\", \"notes\": \"失败根因：exp-058 部署到 cuda:3+port:8003 覆盖了 exp-028b 的 vLLM（非 OOM）。166/204 已完成，intermediates 完整保存。支持 resume（仅需 38 题 ~90min），但需等 exp-058 完成释放 cuda:3。\"}, \"exp-052\": {\"status\": \"DONE\", \"hypothesis\": \"Seed replication of exp-033: the +4.90pp improvement on FOLIO-204 with Mistral-7B using symbolic invariant consensus (K=12) is reproducible across different random seeds, confirming the result is not a statistical fluke.\", \"metrics\": {\"n\": 204, \"sc_accuracy\": 53.9, \"sica_accuracy\": 57.4, \"sc_correct\": 110, \"sica_correct\": 117, \"delta_pp\": 3.43, \"discordant_b\": 8, \"discordant_c\": 1, \"extraction_rate\": 0.971, \"contradiction_rate\": 0.034, \"wall_time_min\": 81.9, \"mcnemar_p\": 0.0391, \"significant\": true}, \"conclusion\": \"success\", \"notes\": \"Seed=123: SICA=57.35% vs SC=53.92%, delta=+3.43pp, b=8, c=1, p=0.039. High entropy 区域 delta=+7.14pp。2/3 seeds 显著。\"}, \"exp-054-mistral-folio204-t10\": {\"status\": \"DONE\", \"hypothesis\": \"T=1.0 增大 trace diversity，Adaptive SICA（high entropy 子集）delta 应 ≥ T=0.7 的 +4.9pp。更高温度 → 更多 high-entropy 问题 → SICA 在更大子集上有效 → overall delta 可能更大。同时测试 exp-033 (+4.9pp at T=0.7) 对温度的敏感性。parent=exp-033\", \"conclusion\": \"negative\", \"metrics\": {\"n\": 204, \"sc_accuracy\": 54.9, \"sica_accuracy\": 55.4, \"delta_pp\": 0.49, \"discordant_b\": 5, \"discordant_c\": 4, \"mcnemar_chi2\": 0.1111, \"mcnemar_p\": 0.7389, \"extraction_rate\": 97.3, \"contradiction_rate\": 3, \"wall_time_min\": 83}}, \"exp-046-mistral-pw600\": {\"status\": \"DONE\", \"hypothesis\": \"Mistral-7B-Instruct-v0.3 在 ProofWriter-600 上 SICA vs SC：验证 regime boundary 跨域泛化。exp-033 (Mistral FOLIO-204) 显示 +4.90pp (p=0.013)，如果 PW-600 也显示正向 delta，则 regime-dependent capability trap 不是 FOLIO-specific artifact。\", \"conclusion\": \"negative\", \"metrics\": {\"n\": 600, \"sc_accuracy\": 39.33, \"sica_accuracy\": 36.5, \"delta_pp\": -2.83, \"sc_wins\": 30, \"sica_wins\": 13, \"mcnemar_p\": 0.0095, \"significant\": true, \"dataset\": \"ProofWriter-D5-600\", \"model\": \"Mistral-7B-Instruct-v0.3\"}}, \"exp-053\": {\"status\": \"DONE\", \"hypothesis\": \"Seed replication of exp-033: the +4.90pp improvement on FOLIO-204 with Mistral-7B using symbolic invariant consensus (K=12) is reproducible across different random seeds, confirming the result is not a statistical fluke.\", \"metrics\": {\"n\": 204, \"sc_accuracy\": 56.37, \"sica_accuracy\": 55.88, \"sc_correct\": 115, \"sica_correct\": 114, \"delta_pp\": -0.49, \"discordant_b\": 2, \"discordant_c\": 3, \"extraction_rate\": 0.97, \"contradiction_rate\": 0.033, \"wall_time_min\": 80.8, \"mcnemar_p\": 1.0, \"significant\": false}, \"conclusion\": \"negative\", \"notes\": \"Seed=456: SICA=55.88% vs SC=56.37%, delta=-0.49pp, b=2, c=3, p=1.0. SC baseline 最高，capability trap 确认。跨 seed SC vs delta Pearson r=-0.8973。\"}, \"exp-050b-mistral-icl-oracle\": {\"status\": \"DONE\", \"hypothesis\": \"Increasing vLLM max_model_len from 8192 to 16384 will resolve the context length overflow (input ~4400 + max_tokens 4096 > 8192) that caused 86% failure in exp-050, allowing Mistral-7B ICL Oracle with 5 gold FOL examples to complete evaluation on all 199 FOLIO problems.\", \"metrics\": {\"n\": 199, \"sc_accuracy\": 57.79, \"sica_accuracy\": 54.27, \"delta_pp\": -3.52, \"sc_correct\": 115, \"sica_correct\": 108, \"discordant_b\": 6, \"discordant_c\": 13, \"mcnemar_p\": 0.167, \"significant\": false, \"wall_time_min\": 93.8, \"extraction_success\": 2333, \"extraction_fail\": 55, \"per_answer\": {\"True\": {\"n\": 70, \"sica_acc\": 50, \"sc_acc\": 54.29}, \"False\": {\"n\": 61, \"sica_acc\": 36.07, \"sc_acc\": 44.26}, \"Unknown\": {\"n\": 68, \"sica_acc\": 75, \"sc_acc\": 73.53}}}, \"conclusion\": \"negative\", \"notes\": \"ICL Oracle (5 gold FOL examples) on Mistral-7B FOLIO-199: SICA=54.27% vs SC=57.79%, delta=-3.52pp (p=0.167, ns). ICL boosted SC from vanilla 54.41% (exp-033) to 57.79% (+3.38pp), but SICA did not benefit. ICL improves individual trace quality enough to boost majority vote, but the resulting constraints become less diverse/discriminative for MaxSAT weighting. Confirms capability trap: better extraction quality does not translate to SICA gains when it also reduces beneficial disagreement.\"}, \"exp-050-mistral-icl-oracle-folio199\": {\"status\": \"DONE\", \"hypothesis\": \"Providing 5 gold FOL annotations as in-context learning examples will significantly improve the quality of symbolic constraint extraction from Mistral-7B reasoning traces, leading to higher SICA accuracy over SC baseline on FOLIO-199\", \"conclusion\": \"failed\"}, \"exp-049b-mistral-logiqa200\": {\"status\": \"DONE\", \"hypothesis\": \"Mistral-7B LogiQA-200 v2: 修复 exp-049 部署失败（vLLM 启动但 pipeline 未运行，tmux session 丢失）。验证 Mistral 的 +4.90pp FOLIO 增益是否跨 LogiQA 复现。parent=exp-033\", \"metrics\": {\"n\": 200, \"sc_accuracy\": 51, \"sica_accuracy\": 51.5, \"delta_pp\": 0.5, \"sc_correct\": 102, \"sica_correct\": 103, \"discordant_b\": 6, \"discordant_c\": 5, \"mcnemar_p\": 1, \"significant\": false, \"wall_time_min\": 78.6, \"extraction_rate\": 0.9725, \"total_constraints\": 10659, \"unique_constraints\": 8934, \"contradiction_rate\": 0.0196}, \"conclusion\": \"negative\", \"notes\": \"Mistral-7B LogiQA-200: SICA=51.50% vs SC=51.00%, delta=+0.50pp (p=1.000, ns). Mistral's +4.90pp FOLIO advantage (exp-033) does not transfer to LogiQA. SC baseline 51% is near random for 4-choice MCQ. Consistent with exp-038 (14B LogiQA delta=-0.50pp): SICA provides no benefit on LogiQA regardless of model, likely because LogiQA's pragmatic reasoning resists symbolic constraint formalization.\"}, \"exp-044b-icl-oracle\": {\"status\": \"DONE\", \"hypothesis\": \"ICL with Oracle Examples (v2, 正确模型 Qwen2.5-14B): 用 5 个 gold FOL annotations 作为 few-shot examples 教 LLM 提取高质量约束。如果 extraction quality 是 capability trap 瓶颈，oracle-guided extraction 应能产生更 discriminative 的约束，使 ICL-SICA > vanilla SICA (74.51%)。评测 199 题。v1 因使用错误模型 (Mistral-7B) 被 kill。\", \"metrics\": {\"n\": 199, \"dataset\": \"FOLIO-199\", \"model\": \"Qwen2.5-14B-Instruct\", \"k\": 12, \"sica_accuracy\": 74.87, \"sc_accuracy\": 74.37, \"delta_pp\": 0.5, \"sica_correct\": 149, \"sc_correct\": 148, \"icl_examples\": 5, \"extraction_failure_rate\": 0.008}, \"conclusion\": \"negative\"}, \"exp-049-mistral-logiqa200\": {\"status\": \"DONE\", \"hypothesis\": \"Mistral-7B-Instruct-v0.3 在 LogiQA-200 上 SICA vs SC。FOLIO-204 上 Mistral delta=+4.90pp (exp-033, p=0.013)。14B 在 LogiQA 上 delta=-0.50pp (exp-038)。测试 regime boundary：Mistral 低 SC + 高 diversity 是否在 LogiQA 上也产生正向 SICA delta。parent=exp-033\", \"conclusion\": \"failed\"}, \"exp-041-14b-folio204-16639\": {\"status\": \"DONE\", \"hypothesis\": \"Qwen2.5-14B-Instruct 在 FOLIO-204 上 SICA vs SC（westd-16639 独立重跑）：在不同服务器上复现 exp-001/026 结果，验证 capability trap 的可复现性和排除服务器环境差异。\", \"conclusion\": \"negative\", \"metrics\": {\"n\": 204, \"dataset\": \"FOLIO-204\", \"model\": \"Qwen2.5-14B-Instruct\", \"k\": 12, \"sica_accuracy\": 75.49, \"sc_accuracy\": 77.45, \"delta_pp\": -1.96, \"sica_correct\": 154, \"sc_correct\": 158, \"mcnemar_discordant_b\": 0, \"mcnemar_discordant_c\": 4, \"mcnemar_p_value\": 0.125, \"extraction_rate\": 0.98, \"contradiction_rate\": 0.0097}}, \"exp-045b-backward-verify\": {\"status\": \"DONE\", \"hypothesis\": \"Backward Verification v2 (正确模型 Qwen2.5-14B): 翻转验证方向，对每个候选答案反向推理 premises，用 Z3 检查一致性。v1 使用错误模型 (Qwen-7B) 得到 -21pp，需确认 Qwen-14B 上是否仍为强 negative（预期是，因为根因是 FOL quality 而非 model capacity）。\", \"conclusion\": \"killed\"}, \"exp-045-backward-verification\": {\"status\": \"DONE\", \"hypothesis\": \"Backward Verification: 翻转验证方向，对每个候选答案反向推理需要哪些 premises 成立/矛盾，用 Z3 检查哪个答案与 premises 最一致（矛盾最少）。如果 forward extraction 质量是瓶颈，backward verification 绕过 extraction 直接用 solver 判断一致性，可能打破 capability trap。\", \"conclusion\": \"negative\", \"notes\": \"v1: 可能使用了 Qwen-7B 残留 vLLM (exp-035 遗留 port 8003)。BV=53.92% vs SC=75.00%, delta=-21.08pp。Z3 SAT rate 95.3%=无判别力。True bias 72.5% vs gold 35.3%。根因：backward FOL generation 质量同样差，验证方向不解决 capability trap。即使换正确模型 (-21pp 幅度过大) 可能仍 negative。建议 Director 决策是否用 Qwen2.5-14B 重跑 v2。\"}, \"exp-038-14b-logiqa200-16639\": {\"status\": \"DONE\", \"hypothesis\": \"Qwen2.5-14B-Instruct 在 LogiQA 2.0 (200题) 上 SICA vs SC：跨数据集验证 capability trap。LogiQA 是多选逻辑推理（非二元分类），constraint extraction 和 Z3 formalization 需要适配不同推理类型。\", \"conclusion\": \"negative\", \"metrics\": {\"n\": 200, \"dataset\": \"LogiQA-200\", \"model\": \"Qwen2.5-14B-Instruct\", \"k\": 12, \"sica_accuracy\": 78, \"sc_accuracy\": 78.5, \"delta_pp\": -0.5, \"mcnemar_p\": 1, \"sica_correct\": 156, \"sc_correct\": 157, \"discordant_b\": 1, \"discordant_c\": 2, \"both_correct\": 155, \"both_wrong\": 42, \"extraction_rate\": 0.864, \"fail_empty_rate\": 0.122, \"avg_unique_constraints\": 26.7, \"contradiction_rate\": 0.008, \"wall_time_min\": 126.8}, \"notes\": \"实验成功完成200/200题，之前被自动监控误判为failed。结果：SICA略逊于SC(-0.5%)，McNemar p=1.0完全不显著。仅3例disagreement(sica_only=1, sc_only=2)。extraction_rate=86.4%低于FOLIO实验(~90%+)，fail_empty=12.2%较高——LogiQA的非形式化推理对constraint extraction更难。contradiction_rate仅0.8%，几乎无矛盾检测。结论：SICA在LogiQA非形式逻辑推理上无增益，capability trap假设在此数据集上未验证。\"}, \"exp-033\": {\"status\": \"DONE\", \"hypothesis\": \"Cross-family validation: Mistral-7B-Instruct-v0.3 在 FOLIO-204 全量上 SICA vs SC。验证 capability trap 跨模型家族在 full dataset 上是否持续（D012 pilot exp-010 已确认 delta=0, n=60）。\", \"metrics\": {\"n_problems\": 204, \"sica_accuracy\": 59.31, \"sc_accuracy\": 54.41, \"delta_pp\": 4.9, \"sica_correct\": 121, \"sc_correct\": 111, \"mcnemar_discordant_b\": 12, \"mcnemar_discordant_c\": 2, \"mcnemar_p_value\": 0.0129, \"c0_non_unanimous_rate\": 0.8137, \"avg_majority_frac\": 0.7515, \"extraction_rate\": 97.14, \"contradiction_rate\": 3.5, \"problems_with_contradictions\": 128, \"avg_unique_constraints\": 39.3, \"maxsat_mean_sat_ratio\": 0.9609, \"total_constraints\": 14042, \"unique_constraints\": 8021, \"wall_time_min\": 81.4, \"k\": 12}, \"conclusion\": \"success\", \"notes\": \"Mistral-7B FOLIO-204: SICA 59.31% vs SC 54.41%, delta=+4.90pp (McNemar p=0.013, significant). 首次 SICA 显著超越 SC。关键因素：C0=81.37%（远高于 Qwen-7B 的 55%），高 diversity 使 SC majority vote 退化，而 SICA MaxSAT 仍能从 noisy traces 中提取信号。Discordant: SICA-only=12, SC-only=2, 高度不对称。但绝对准确率低（59% vs Qwen-7B 77%），说明 Mistral-7B 基础推理能力弱。结论：capability trap 非普遍现象，依赖 diversity/quality 平衡——高 diversity + 低 quality 时 SICA 有优势。\"}, \"exp-042b-premise-formal\": {\"status\": \"DONE\", \"hypothesis\": \"Premise-Only Formalization (重启): 绕过 CoT trace extraction，直接让 LLM 将 FOLIO premises + conclusion 形式化为 FOL，用 Z3 验证逻辑蕴含。K=12 独立 formalization + majority vote。如果 extraction quality 是 capability trap 的瓶颈，直接 formalization 应能产生更准确的约束，使 Premise-FOL > vanilla SICA。exp-042 因 vLLM 未启动失败，本次重启。\", \"conclusion\": \"failed\", \"notes\": \"失败根因：run_premise_formalization.sh 参数顺序是 PORT GPU，但调用传了 GPU PORT (2 8002)，导致 CUDA_VISIBLE_DEVICES=8002 → NVMLError_InvalidArgument。vLLM 未启动，0 题完成。将在 cleanup Worker 中用显式命令重部署。\"}, \"exp-044-icl-oracle\": {\"status\": \"DONE\", \"hypothesis\": \"ICL with Oracle Examples: 用 5 个 gold FOL annotations 作为 few-shot examples 教 LLM 提取高质量约束。如果 extraction quality 是 capability trap 瓶颈，oracle-guided extraction 应能产生更 discriminative 的约束，使 ICL-SICA > vanilla SICA (74.51%)。评测 199 题（排除 5 个 ICL examples）。\", \"conclusion\": \"failed\", \"notes\": \"v2 失败: vLLM server 连接中断 (httpx.ConnectError: All connection attempts failed)，EXIT_CODE=129 (SIGHUP)。实验跑完但数据无效：extraction 成功率仅 17.1% (307/1800, 1490 json_fail)，SC=46.23% 远低于 Qwen2.5-14B 预期 75.49%。结果不可用，需在 vLLM 稳定后重跑。worker_infra_westd25068-gpu-cleanup-redeploy 正在处理 westd-25068 基础设施。\"}, \"exp-035\": {\"status\": \"DONE\", \"hypothesis\": \"Qwen2.5-7B-Instruct 在 FOLIO-204 上 SICA vs SC：within-family scaling 下界验证。弱模型 C0 更高（更多 diversity），但 constraint quality 更差，SICA 仍无法 outperform SC。与 exp-004-qwen7b (D012 delta=0) 在 full FOLIO 上的扩展验证。代替原 ARC-60 实验（exp-035 v1 因平台 kill 失败）。\", \"conclusion\": \"negative\", \"notes\": \"v2 完成: Qwen2.5-7B FOLIO-204, 203/204题有结果(1题缺失)。JSON summary是stale的(n=195时计算)，实际数据从results数组203条计算。SICA与SC仅3个discordant pairs，几乎完全一致。假设验证：SICA无法outperform SC on 7B，delta=-0.49pp (p=1.0)。C0=0.55高于14B但未能转化为SICA优势。注意7B SC(77.34%)意外高于14B SC(75.49%)，可能因FOLIO数据特性。\", \"metrics\": {\"n_problems\": 203, \"sc_accuracy\": 77.34, \"sica_accuracy\": 76.85, \"delta_pp\": -0.49, \"sica_correct\": 156, \"sc_correct\": 157, \"mcnemar_discordant_b\": 1, \"mcnemar_discordant_c\": 2, \"mcnemar_p_value\": 1, \"c0_non_unanimous_rate\": 0.5517, \"extraction_rate\": 98.19, \"contradiction_rate\": 1.58, \"problems_with_contradictions\": 60, \"total_constraints\": 12950, \"unique_constraints\": 6515, \"dedup_ratio\": 50.3, \"wall_time_min\": 78.2, \"avg_per_problem_s\": 23.1}}, \"exp-036b-cross-trace-unsat\": {\"status\": \"DONE\", \"hypothesis\": \"Cross-trace UNSAT: 合并不同候选答案的 constraints，检查 answer_A 与 answer_B 的约束是否 UNSAT（矛盾）。预期 cross-answer 对比的 UNSAT rate 远高于 within-trace 检查，因为不同答案的约束应该矛盾。如果 UNSAT 信号强，可用于增强 SICA 打分的 discriminative power。\", \"conclusion\": \"negative\", \"metrics\": {\"cross_unsat_rate_pair\": 0.087, \"cross_unsat_rate_problem\": 0.107, \"within_trace_unsat_rate\": 0.009, \"unsat_pairs\": 11, \"total_pairs\": 126, \"problems_with_unsat\": 9, \"multi_answer_problems\": 84, \"single_answer_skip\": 120, \"zero_shared_var_pairs_pct\": 0.564, \"avg_shared_vars\": 2.7, \"false_true_unsat_rate\": 0.467, \"sica_cross_ut_accuracy\": 0.745, \"sc_accuracy\": 0.75, \"accuracy_impact\": 0}, \"notes\": \"Cross-trace UNSAT 验证了 Director 假设：cross-answer UNSAT rate (8.7%) 约为 within-trace (0.9%) 的 10x。但主要瓶颈是 Z3 变量命名不一致：56.4% 的 answer pairs 共享零变量，Z3 无法跨 trace 比较。False-True 对最具辨别力 (non-empty 中 46.7% UNSAT)。最终对准确率无影响（仅覆盖 9/204 问题），第 6 个 negative constructive。核心诊断价值：变量命名不一致是 capability trap 的关键机制之一。\"}, \"exp-042-premise-formalization\": {\"status\": \"DONE\", \"hypothesis\": \"Premise-Only Formalization: 绕过 CoT trace extraction，直接让 LLM 将 FOLIO premises + conclusion 形式化为 FOL，用 Z3 验证逻辑蕴含。K=12 独立 formalization + majority vote。如果 extraction quality 是 capability trap 的瓶颈，直接 formalization 应能产生更准确的约束，使 Premise-FOL > vanilla SICA。\", \"conclusion\": \"failed\"}, \"exp-043-consistency-filtering\": {\"status\": \"DONE\", \"hypothesis\": \"Constraint Consistency Filtering: 从已有 exp-001 数据中，只保留在 ≥T/K 条 trace 中出现的约束（T=4,6,8），用筛选后的约束跑 MAX-SAT。假设跨 trace 一致出现的约束质量更高，filtered SICA > full SICA。\", \"conclusion\": \"negative\", \"metrics\": {\"sc_accuracy\": 0.75, \"sica_t1_all\": 0.7794, \"sica_t4\": 0.75, \"sica_t6\": 0.7549, \"sica_t8\": 0.7549, \"avg_unique_constraints\": 13.2, \"avg_filtered_t4\": 1.8, \"avg_filtered_t6\": 0.8, \"avg_filtered_t8\": 0.3}, \"notes\": \"Consistency filtering NEGATIVE: 过滤后约束数量骤降（T≥4 仅 1.8/题, T≥8 仅 0.3/题），MaxSAT 无法区分答案，退化为 SC。根因：Z3 变量命名不一致导致语义等价约束被视为不同（avg 13.2 unique constraints/problem），跨 trace 一致性极低。第 5 个 negative constructive intervention。注意：T=1 的 77.94% 与 exp-001 的 74.51% 差异是已知 pipeline 非确定性问题（code path confound）。\"}, \"exp-036-z3-feedback-folio204\": {\"status\": \"DONE\", \"hypothesis\": \"Z3 UNSAT core feedback refinement: closed-loop 方法用 Z3 solver 的 UNSAT core 指导 LLM 修正矛盾约束（最多 3 轮）。如果约束质量是瓶颈，solver 反馈应能提升 constraint discriminative power，使 Z3-feedback SICA > vanilla SICA。目标 recovery_rate > 0%（recovery_rate = Z3fb_delta / oracle_delta × 100%）。与之前 open-loop interventions（contrastive/cross-model/generational 全部失败）对比，closed-loop 利用 formal verification 信号可能是打破 capability trap 的关键。\", \"conclusion\": \"negative\", \"notes\": \"Z3 feedback mechanism had zero real impact. Apparent +3.0pp (77.5% vs 74.5%) entirely due to code path confound: JSON serialization vs in-memory processing caused different dedup/scoring behavior. UNSAT trigger rate 0.9% (22/2448 traces), too low for feedback loop to meaningfully activate. All observed delta on discordant problems came from pipeline non-determinism, not Z3 refinement. Fourth negative constructive intervention after contrastive, cross-model, generational.\", \"metrics\": {\"z3fb_sica_accuracy\": 0.775, \"vanilla_sica_accuracy\": 0.745, \"sc_accuracy\": 0.75, \"z3fb_vs_vanilla_delta\": 0.03, \"unsat_traces\": 22, \"total_traces\": 2448, \"unsat_rate\": 0.009, \"unsat_resolve_rate\": 0.864, \"problems_flipped\": 0, \"real_impact\": 0}}, \"exp-028-qwen3-14b-thinking\": {\"status\": \"DONE\", \"hypothesis\": \"Qwen3-14B thinking mode 在 FOLIO 204 上 SICA vs SC：原生推理能力（内置 CoT）是否改变 capability trap？两种可能：(a) thinking mode 使 traces 更确定性（类似 QwQ-32B），C0 极低→SICA≡SC；(b) thinking mode 提升 constraint extraction 质量，打破 capability trap。预期 (a) 更可能。\", \"conclusion\": \"killed\", \"notes\": \"Killed per D049: extraction_rate 73% below 80% threshold. Partial results (35/204): SICA 88.57%, SC 85.71%, delta +2.86pp. But extraction_rate degrading and ETA 16h+ made continued run not worthwhile. GPU freed for D050 constructive experiments.\"}, \"exp-033-qwen3-pw600-nonthinking\": {\"status\": \"DONE\", \"hypothesis\": \"Qwen3-14B in non-thinking mode on ProofWriter 600 will show whether SICA's constraint-based consensus improves over SC@K for a model without chain-of-thought reasoning overhead, providing a controlled comparison against thinking-mode results.\", \"conclusion\": \"failed\", \"notes\": \"FAILED: AutoDL 平台级 SIGTERM 导致 vLLM EngineCore 崩溃 (00:05:54)，后紧急清理 Worker 误杀 tmux server 连带终止。518/600 intermediates 有效可恢复。\"}, \"exp-004-qwen7b-rerun\": {\"status\": \"DONE\", \"hypothesis\": \"Qwen2.5-7B-Instruct 在 D012 60 题上 SICA vs SC rerun（修复后代码）：弱模型 C0 更高（更多 diversity），但 constraint quality 更差，SICA 仍无法 outperform SC。验证 capability trap 在 within-family scaling 的下界。与之前 exp-004-qwen7b (delta=0) 对比验证一致性。\", \"conclusion\": \"failed\", \"notes\": \"FAILED: ModelScope 下载失败，Qwen2.5-7B-Instruct 模型下载未完成。实验从未开始运行。需要 HF 镜像修复后重试。\"}, \"exp-007-qwen72b-awq\": {\"status\": \"DONE\", \"hypothesis\": \"Qwen2.5-72B-Instruct-AWQ (4-bit) 在 D012 60 题上 SICA vs SC：72B scaling 是否打破 capability trap？预期 SC baseline 更高（模型更强），但 SICA≈SC（extraction quality bottleneck 不随 model scale 改善），证明 scaling 不是 rescue path。\", \"conclusion\": \"failed\", \"notes\": \"FAILED: HuggingFace 网络不通 (Network unreachable)，模型下载失败。72B AWQ 模型从未下载完成，实验从未开始运行。需要 HF 镜像修复后重试。\"}, \"exp-027-qwen3-14b-non-thinking\": {\"status\": \"DONE\", \"hypothesis\": \"Qwen3-14B（代际升级）在 non-thinking mode 下 FOLIO 204 的 SICA vs SC：capability trap 是否在次世代模型持续？预期 Qwen3 基础能力提升使 SC baseline 更高，但 self-extraction 质量仍不足以产生 SICA 增益（delta≈0），证明 capability trap 是结构性的而非模型能力不足。\", \"conclusion\": \"success\", \"metrics\": {\"n\": 204, \"k\": 12, \"sica_accuracy\": 0.8431, \"sc_accuracy\": 0.8382, \"delta_pp\": 0.49, \"extraction_rate\": 0.995, \"contradiction_rate\": 0.0283, \"problems_with_contradictions\": 69, \"total_constraints\": 16153, \"unique_constraints\": 7031, \"wall_time_s\": 11017, \"model\": \"Qwen3-14B\", \"dataset\": \"FOLIO-204\", \"mode\": \"non-thinking\"}, \"notes\": \"Qwen3-14B non-thinking FOLIO-204: SICA 84.31% vs SC 83.82%, delta=+0.49pp。Qwen3 SC baseline 83.82% 远高于 Qwen2.5-14B 的 75.00% (+8.82pp)，证明 Qwen3 基础能力显著提升。但 SICA-SC gap 仍≈0 (+0.49pp)，capability trap 在次世代模型上持续。Extraction rate 99.5% (vs 14B 98.5%)，contradiction rate 2.83%。论文价值：(1) 证明 capability trap 是结构性的，非模型能力不足；(2) 代际升级提升 SC 不提升 SICA delta。\"}, \"exp-030-crossmodel-mistral-folio204\": {\"status\": \"DONE\", \"hypothesis\": \"Cross-model extraction: Mistral-7B 从 Qwen2.5-14B 的 FOLIO 204 traces 中提取 constraints，能否打破 same-model capability trap？不同模型有不同的 extraction bias，Mistral 可能提取出 Qwen self-extraction 遗漏的 discriminative constraints。目标 discriminative_rate >8.2%（baseline），recovery_rate >0%。\", \"conclusion\": \"negative\", \"metrics\": {\"n\": 204, \"k\": 12, \"crossmodel_sica_accuracy\": 0.75, \"sc_accuracy\": 0.75, \"delta_pp\": 0, \"discriminative_rate\": 0, \"recovery_rate\": 0, \"model_extraction\": \"Mistral-7B-Instruct-v0.3\", \"model_traces\": \"Qwen2.5-14B-Instruct\", \"dataset\": \"FOLIO-204\"}, \"notes\": \"NEGATIVE. Cross-model extraction (Mistral-7B extracts constraints from Qwen2.5-14B traces) 完全无效：SICA = SC = 75.00%, discriminative_rate=0%, recovery_rate=0%. Mistral 虽然是不同模型家族，但提取的 constraints 同样缺乏判别力。这进一步强化 capability trap 结论：问题不在 same-model bias，而在 LLM extraction 本身的能力限制——无论哪个模型做 extraction，都无法从 CoT traces 中提取出对答案有判别力的 symbolic constraints。论文 claim: cross-model 不是 rescue path。\"}, \"exp-031-oracle-folio-regen\": {\"status\": \"DONE\", \"hypothesis\": \"Oracle SICA with gold FOL annotations on exp-026 regenerated traces (post normalization-fix): if constraint quality is the bottleneck, replacing self-extracted constraints with gold FOL + Z3 entailment should significantly outperform SC and SICA(self), replicating exp-021's finding on fixed code.\", \"conclusion\": \"success\", \"metrics\": {\"n\": 204, \"k\": 12, \"oracle_sica_accuracy\": 0.8971, \"sc_accuracy\": 0.7549, \"sica_self_accuracy\": 0.7451, \"oracle_vs_sc_delta_pp\": 14.22, \"oracle_vs_sica_delta_pp\": 15.2, \"mcnemar_p_oracle_vs_sc\": 2.0024e-07, \"mcnemar_b_c\": {\"b_oracle_right_sc_wrong\": 29, \"c_oracle_wrong_sc_right\": 0}, \"z3_gold_agreement\": 0.951, \"z3_gold_agree_n\": 194, \"z3_in_candidates_n\": 178, \"fol_parse_success\": 1, \"model\": \"Qwen2.5-14B-Instruct\", \"dataset\": \"FOLIO-204\", \"constraint_source\": \"gold FOL annotations\", \"traces_source\": \"exp-026-folio204-trace-regen\"}, \"notes\": \"KEY RESULT. Oracle-SICA (gold FOL + Z3 entailment + consistency-weighted voting) 89.71% vs SC 75.49% vs SICA(self) 74.51%, +14.22pp over SC, McNemar p=2.0e-07 极显著, b=29 c=0 (oracle 从未输给 SC)。Z3 gold agreement 95.10% (194/204), FOL parser 204/204 全成功。Per-type: True 97.2% (+4.1pp), False 93.6% (+6.3pp), Unknown 78.3% (+31.9pp)。与 exp-021 (88.24%, 旧 traces) 对比：oracle 准确率从 88.24% 提升至 89.71%（+1.47pp），delta 从 +8.82pp 增至 +14.22pp。差异来源：(1) exp-026 traces 的 SC baseline 更低 (75.49% vs 79.41%)；(2) Z3 agreement 从 94.6% 提升至 95.1%。结论与 exp-021 一致：MAX-SAT 聚合机制有效——瓶颈在约束提取质量。\"}, \"exp-029-contrastive-folio204\": {\"status\": \"DONE\", \"hypothesis\": \"Contrastive constraint extraction (answer-conditioned supporting/opposing constraints with structured JSON output and MaxSAT integration) will achieve discriminative_rate >20% (vs baseline 8.2%) and positive recovery_rate on FOLIO 204, because per-candidate opposing constraints provide stronger signal than simple majority voting for disambiguating closely-scored answers.\", \"conclusion\": \"negative\", \"metrics\": {\"contrastive_accuracy\": 0.7253, \"sc_accuracy\": 0.7363, \"delta_pp\": -1.1, \"discriminative_rate\": 0.0604, \"discriminative_count\": 11, \"n\": 182, \"recovery_rate_pct\": -8.3, \"mcnemar_chi2\": 0.1, \"mcnemar_p\": 0.7518, \"cont_only_correct\": 4, \"sc_only_correct\": 6, \"both_correct\": 128, \"both_wrong\": 44, \"supporting_pct\": 43.2, \"opposing_pct\": 56.8, \"avg_constraints_per_problem\": 24.4, \"avg_unique_per_problem\": 10.4, \"wall_time_min\": 47.2}}, \"exp-026-folio204-trace-regen\": {\"status\": \"DONE\", \"hypothesis\": \"FOLIO 204 全量 trace 重生成（Qwen2.5-14B, K=12, T=0.7 trace gen, T_ext=0.3 extraction）：在 westd-25068 上生成 FOLIO traces，用于 cross-model extraction 和 case study 选取。归一化 bug 已修复（startswith 方案），温度双参数已正确分离。\", \"conclusion\": \"success\", \"metrics\": {\"n\": 204, \"k\": 12, \"sica_accuracy\": 0.7451, \"sc_accuracy\": 0.7549, \"delta_pp\": -0.98, \"extraction_rate\": 0.9853, \"model\": \"Qwen2.5-14B-Instruct\", \"dataset\": \"FOLIO-204\", \"temperature_trace\": 0.7, \"temperature_extraction\": 0.3, \"wall_time_h\": 2.5}, \"notes\": \"FOLIO 204 全量 trace 重生成完成 (204/204)。SICA 74.51% vs SC 75.00%, delta=-0.49pp，与 sica_expanded_14b FOLIO 子集 (79.4%/79.4%, delta=0) 一致——capability trap 在重生成 traces 上仍成立。归一化 bug 修复 + 温度双参数分离后 extraction_rate=98.53% (vs 之前 89%)。Traces 已被 exp-029 contrastive 实验复用。结果路径: /root/symb_invariant_consensus/results/folio_204_14b/folio_204_results.json\"}, \"exp-023-discriminative-rate\": {\"status\": \"DONE\", \"hypothesis\": \"Full-dataset discriminative rate analysis (W1+W3 合并): Qwen2.5-14B 在 804 题上 self-extracted constraints 的 source-trace discriminativeness 和 Z3 semantic discriminativeness 均低于 15%，证明即使用 Z3 per-answer evaluation，self-extracted constraints 仍无判别力，封堵 oracle scoring confound。\", \"metrics\": {\"n_total\": 804, \"n_multi_candidate\": 307, \"source_disc_rate_weight\": 0.392, \"source_disc_rate_weight_ci95\": [0.387, 0.398], \"source_disc_rate_count_est\": 0.121, \"source_disc_rate_count_ci95\": [0.12, 0.123], \"z3_semantic_disc_rate\": 0.082, \"z3_semantic_disc_ci95\": [0.076, 0.088], \"problems_with_disc\": 289, \"problems_with_disc_rate\": 0.941, \"pw_source_disc_weight\": 0.364, \"folio_source_disc_weight\": 0.54, \"pw_n_multi\": 235, \"folio_n_multi\": 72, \"pilot_rate_reported_count\": 0.115, \"pilot_rate_reported_weight\": 0.372, \"pilot_validation_weight\": 0.376, \"pilot_delta_pp\": 0.38, \"z3_answer_assertions\": 642, \"z3_total_unique_constraints\": 7844, \"model\": \"Qwen2.5-14B-Instruct\", \"dataset\": \"FOLIO+ProofWriter-804\"}, \"conclusion\": \"success\", \"notes\": \"Full 804-instance discriminative rate (R3 W1+W3, v1+v2 合并). By weight: 39.2% [38.7, 39.8]; by count (est): 12.1% [12.0, 12.3]. Z3 semantic disc: 8.2% [7.6, 8.8]. Per-domain: FOLIO 54.0% > PW 36.4% (by weight). 289/307 multi-candidate 问题有≥1 discriminative constraint (94.1%). Pilot validation: weight 37.6% vs 报告 37.2% (delta 0.38pp); count 12.1% vs 报告 11.5% (delta 0.6pp)——高度一致。v2 修复了 v1 的 assertion weight 不对称问题。数据: /root/symb_invariant_consensus/analysis/discriminative_rate_full_804.json\"}, \"exp-022-oracle-proofwriter\": {\"status\": \"DONE\", \"hypothesis\": \"ProofWriter oracle: gold DSL (raw_logic_programs) 通过 Z3 consistency checking 加权 K=12 traces，Oracle-SICA 应显著超越 SC 和 SICA(self)，在 ProofWriter 600 题上复现 FOLIO oracle (+8.82pp) 的 extraction bottleneck 结论。\", \"conclusion\": \"success\", \"metrics\": {\"n\": 600, \"k\": 12, \"oracle_sica_accuracy\": 0.8667, \"sc_accuracy\": 0.7517, \"sica_self_accuracy\": 0.755, \"oracle_vs_sc_delta_pp\": 11.5, \"mcnemar_p_oracle_vs_sc\": 9.21e-15, \"z3_gold_agreement\": 0.9714, \"z3_gold_agree_n\": 577, \"z3_gold_total\": 594, \"parse_errors\": 6, \"parse_error_rate\": 0.01, \"solver_errors\": 0, \"solver_total\": 7128, \"relneg_oracle\": 0.7786, \"relneg_sc\": 0.6, \"relneg_delta_pp\": 17.86, \"relnoneg_oracle\": 0.7945, \"relnoneg_sc\": 0.6644, \"relnoneg_delta_pp\": 13.01, \"attnoneg_oracle\": 0.961, \"attnoneg_sc\": 0.8701, \"attnoneg_delta_pp\": 9.09, \"attneg_oracle\": 0.9188, \"attneg_sc\": 0.85, \"attneg_delta_pp\": 6.87, \"model\": \"Qwen2.5-14B-Instruct\", \"dataset\": \"ProofWriter-OWA-D5-600\", \"constraint_source\": \"gold DSL (raw_logic_programs)\"}, \"notes\": \"KEY RESULT. ProofWriter Oracle-SICA (gold DSL + Z3 + MAX-SAT) 86.67% vs SC 75.17% vs SICA(self) 75.50%, +11.50pp, McNemar p=9.21e-15 极显著。Z3 gold agreement 97.14% (577/594), parse errors 仅 6/600 (1%), solver errors 0/7128。Per-subtype: RelNeg +17.86pp > RelNoneg +13.01pp > AttNoneg +9.09pp > AttNeg +6.87pp——关系谓词（推理链更长）获益远大于属性谓词。与 FOLIO oracle (exp-021, +8.82pp, p=6.15e-5) 对比：ProofWriter delta 更大 (+11.50 vs +8.82) 且统计显著性高 6 个数量级。两个子域 Oracle 实验一致证明：MAX-SAT 聚合机制有效，瓶颈在 LLM self-extraction 质量。\"}, \"temperature-ablation-t07\": {\"status\": \"DONE\", \"hypothesis\": \"Temperature ablation T=0.7 同源补跑：消除 T=0.7 数据来自不同 run (sica_d012_14b) 的混淆。预期 Δ=0（与 T=0.3/0.5/1.0 一致），C0 值可直接与其他温度点比较。\", \"metrics\": {\"n\": 60, \"k\": 12, \"sica_accuracy\": 0.7167, \"sc_accuracy\": 0.75, \"delta_pp\": -3.33, \"multi_candidate_rate\": 0.4, \"extraction_rate\": 0.9208, \"answer_extraction_rate\": 1, \"contradiction_rate\": 0.022, \"discordant_sica_wins\": 0, \"discordant_sc_wins\": 2, \"truncated_traces\": 0, \"model\": \"Qwen2.5-14B-Instruct\", \"dataset\": \"D012\", \"temperature\": 0.7, \"proofwriter_sica\": 0.6333, \"proofwriter_sc\": 0.7, \"proofwriter_n\": 30, \"folio_sica\": 0.8, \"folio_sc\": 0.8, \"folio_n\": 30, \"wall_time_s\": 3498.3}, \"notes\": \"T=0.7 同源补跑完成（60/60 题）。C0=40.0%，介于 T=0.5(38.3%) 和 T=1.0(43.3%) 之间，消除了旧数据 T=0.7(53.3%) 来自不同 run 的混淆。四温度点 C0 现呈单调递增：T=0.3(30%) → T=0.5(38.3%) → T=0.7(40.0%) → T=1.0(43.3%)。SICA 71.67% < SC 75.00%，delta=-3.33pp，discordant 0:2（SC wins only）。FOLIO 80%=80%，PW SICA 63.33% < SC 70%。结论与其他温度点一致：diversity 增加但 constraint quality 无改善，delta≈0。\", \"conclusion\": \"negative\"}, \"sica_constraint_ablation_013\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"hypothesis\": \"exp-013: MaxSAT 加权聚合是否比 count-only 或 random-weight 有显著优势？验证 SICA 核心机制（约束加权）的实际贡献\", \"metrics\": {\"maxsat_accuracy\": 0.7649, \"count_only_accuracy\": 0.7662, \"random_weight_accuracy\": 0.7587, \"sc_baseline_accuracy\": 0.7624, \"n_problems\": 804, \"maxsat_correct\": 615, \"count_only_correct\": 616, \"random_weight_correct\": 610, \"sc_correct\": 613, \"agreement_maxsat_vs_countonly\": \"803/804\", \"agreement_maxsat_vs_randomwt\": \"785/804\", \"agreement_maxsat_vs_sc\": \"773/804\", \"agreement_countonly_vs_randomwt\": \"786/804\", \"agreement_countonly_vs_sc\": \"774/804\", \"agreement_randomwt_vs_sc\": \"764/804\", \"mcnemar_p_all_gt_0.7\": true}, \"notes\": \"exp-013 constraint ablation 完成，数据已从 ablation_results.json 交叉验证。关键修正：(1) 802/804 不存在于任何 pairwise comparison，原 registry 数据错误；(2) random-weight accuracy 修正为 75.87% (610/804)，原 76.37% 是近似值。核心发现：MaxSAT vs Count-only 803/804 agreement 确认 SAT solver 无增量。MaxSAT vs SC 773/804 (31 disagreements, 16 SICA wins / 14 SC wins / 1 both wrong diff)——SICA 改了 31 题但 wins/losses 几乎抵消。数据文件：/root/symb_invariant_consensus/analysis/exp013_agreement_matrix.json\"}, \"exp-004-qwen7b\": {\"status\": \"DONE\", \"hypothesis\": \"Within-family scaling: Qwen2.5-7B-Instruct 在 D012 60 题上 SICA vs SC。弱模型预期 C0 > 14B（更多 diversity），但 constraint quality 预期更低，SICA-SC gap 预期≈0——验证 capability trap 的 scaling 维度。\", \"conclusion\": \"negative\", \"notes\": \"Qwen2.5-7B within-family scaling: SICA=SC=68.33% (41/60), Δ=0.00pp, C0=43.3%, McNemar p=1.0。60 题全部完成（run.log 确认）。C0=43.3% 高于 14B 的 38.2%（弱模型更多 diversity），但 Δ=0 确认 capability trap 在 7B scale 同样成立。Discordant 2:2 完全对称。Per-domain: FOLIO SICA 76.7% vs SC 73.3% (+3.3pp), PW SICA 60.0% vs SC 63.3% (-3.3pp)，方向相反互相抵消。extraction_rate=94.2%。\", \"metrics\": {\"n\": 60, \"k\": 12, \"sica_accuracy\": 0.6833, \"sc_accuracy\": 0.6833, \"delta_pp\": 0, \"multi_candidate_rate\": 0.433, \"extraction_rate\": 0.9417, \"answer_extraction_rate\": 1, \"contradiction_rate\": 0.0274, \"discordant_sica_wins\": 2, \"discordant_sc_wins\": 2, \"mcnemar_p\": 1, \"wall_time_s\": 1838, \"truncated_traces\": 0, \"model\": \"Qwen2.5-7B-Instruct\", \"dataset\": \"D012\", \"temperature\": 0.7, \"folio_sica\": 0.7667, \"folio_sc\": 0.7333, \"folio_n\": 30, \"proofwriter_sica\": 0.6, \"proofwriter_sc\": 0.6333, \"proofwriter_n\": 30}}, \"temperature-ablation-t10\": {\"status\": \"DONE\", \"hypothesis\": \"Temperature ablation T=1.0: 高温下 Qwen2.5-14B trace diversity 最大化（C0 预期>60%），SICA-SC gap 预期≈0 或负——验证最大 diversity 仍不能拯救 SICA，因为 constraint discriminative power 不随 diversity 增加\", \"notes\": \"T=1.0 高温：C0=43.3%，低于 T=0.7 的 53.3%（注意：T=0.7 数据来自 sica_d012_14b 不同 run）。SICA=SC=75.00%，delta=0，discordant=0。最大温度仍不能拯救 SICA。Temperature ablation 结论：T=0.3(30%) → T=0.5(38.3%) → T=1.0(43.3%) 三点 C0 递增，但加上 T=0.7(53.3%, 来自 sica_d012_14b) 后整体非单调（T=0.7 > T=1.0）。不同 run 间 C0 有随机波动。核心结论不变：delta 始终=0，diversity 不是瓶颈。\", \"metrics\": {\"n\": 60, \"k\": 12, \"sica_accuracy\": 0.75, \"sc_accuracy\": 0.75, \"delta_pp\": 0, \"multi_candidate_rate\": 0.433, \"discordant_total\": 0, \"model\": \"Qwen2.5-14B-Instruct\", \"dataset\": \"D012\", \"temperature\": 1}, \"conclusion\": \"negative\"}, \"exp-012-gsm8k-pilot\": {\"status\": \"DONE\", \"hypothesis\": \"Cross-domain validation: Qwen2.5-14B-Instruct 在 GSM8K (开放答案数学域) 30 题上 SICA vs SC。预期 C0<20%（14B 在 GSM8K 太强），验证 C0 作为 SICA 无效性预测指标。\", \"metrics\": {\"n\": 30, \"k\": 12, \"sica_accuracy\": 0.9667, \"sc_accuracy\": 0.9667, \"delta_pp\": 0, \"multi_candidate_rate\": 0.133, \"extraction_success_rate\": 0.147, \"model\": \"Qwen2.5-14B-Instruct\", \"dataset\": \"GSM8K\", \"temperature\": 0.7}, \"conclusion\": \"negative\", \"notes\": \"GSM8K 30题：SICA=SC=96.67%，delta=0，C0=13.3%。开放答案数学域 baseline 极高（96.67%），几乎无 diversity（C0=13.3%），extraction_success_rate 仅 14.7%——数学域的 symbolic constraints 难以提取。支持 C0 作为 SICA 无效性预测指标。\"}, \"exp-021-oracle-folio\": {\"status\": \"DONE\", \"hypothesis\": \"If we replace self-extracted constraints with gold FOL annotations verified by Z3, Oracle-SICA should significantly outperform both SC and SICA, demonstrating that constraint quality is the bottleneck for SICA gains on formal logic tasks.\", \"conclusion\": \"success\", \"metrics\": {\"n\": 204, \"k\": 12, \"oracle_sica_accuracy\": 0.8824, \"sc_accuracy\": 0.7941, \"sica_self_accuracy\": 0.7941, \"oracle_vs_sc_delta_pp\": 8.82, \"oracle_vs_sica_delta_pp\": 8.82, \"mcnemar_p_oracle_vs_sc\": 6.15e-05, \"z3_gold_agreement\": 0.946, \"fol_parse_success\": 1, \"model\": \"Qwen2.5-14B-Instruct\", \"dataset\": \"FOLIO-204\", \"constraint_source\": \"gold FOL annotations\"}, \"notes\": \"KEY RESULT. Oracle-SICA (gold FOL + Z3 consistency check + MAX-SAT) 88.24% vs SC 79.41% vs SICA(self-extracted) 79.41%, +8.82pp, McNemar p=6.15e-05 高度显著。Z3 solver 与 gold answer 一致率 94.6%（193/204），FOL parser 204/204 全部成功。SICA(self)=SC 确认 LLM 自提取约束在 formal logic 上无有效信号。结论：MAX-SAT 聚合机制本身有效——瓶颈在约束提取质量，不在聚合算法。这直接回答了 Reviewer 的核心 confound 质疑。\"}, \"temperature-ablation-t05\": {\"status\": \"DONE\", \"hypothesis\": \"Temperature ablation T=0.5: 中温下 Qwen2.5-14B trace diversity 中等（C0 预期 30-45%），SICA-SC gap 预期≈0——验证即使 diversity 适中，constraint quality 仍为瓶颈\", \"notes\": \"T=0.5 中温：C0=38.3%，SICA=SC=76.67%，delta=0，discordant=0。中等 diversity 下 SICA 仍完全等于 SC。\", \"metrics\": {\"n\": 60, \"k\": 12, \"sica_accuracy\": 0.7667, \"sc_accuracy\": 0.7667, \"delta_pp\": 0, \"multi_candidate_rate\": 0.383, \"discordant_total\": 0, \"model\": \"Qwen2.5-14B-Instruct\", \"dataset\": \"D012\", \"temperature\": 0.5}, \"conclusion\": \"negative\"}, \"temperature-ablation-t03\": {\"status\": \"DONE\", \"hypothesis\": \"Temperature ablation T=0.3: 低温下 Qwen2.5-14B trace diversity 降低（C0 预期<30%），SICA-SC gap 预期≈0——验证 diversity 不足时 SICA 无操作空间，capability trap 的下界\", \"metrics\": {\"n\": 60, \"k\": 12, \"sica_accuracy\": 0.7333, \"sc_accuracy\": 0.7333, \"delta_pp\": 0, \"multi_candidate_rate\": 0.3, \"discordant_total\": 0, \"model\": \"Qwen2.5-14B-Instruct\", \"dataset\": \"D012\", \"temperature\": 0.3}, \"conclusion\": \"negative\", \"notes\": \"T=0.3 低温：C0=30%（符合预期低于 T=0.7 的 53%），SICA=SC=73.33%，delta=0，discordant=0。低温降低 diversity 但 SICA 无任何改变——约束完全无判别力。\"}, \"exp-014-deepseek-r1-7b\": {\"status\": \"DONE\", \"hypothesis\": \"DeepSeek-R1-Distill-Qwen-7B（reasoning distill 模型）在 D012 上 SICA vs SC——预期 C0<5%（类似 QwQ-32B，reasoning model 的确定性链消灭多样性），作为第二个 reasoning model 数据点验证 capability trap\", \"metrics\": {\"n\": 60, \"k\": 12, \"sica_accuracy\": 0.6833, \"sc_accuracy\": 0.7167, \"delta_pp\": -3.33, \"multi_candidate_rate\": 0.583, \"extraction_rate\": 0.839, \"answer_extraction_rate\": 0.939, \"truncated_traces\": 72, \"contradiction_rate\": 0.037, \"wall_time_min\": 100.3, \"mcnemar_p\": 0.4795, \"discordant_sica_wins\": 0, \"discordant_sc_wins\": 2, \"model\": \"DeepSeek-R1-Distill-Qwen-7B\", \"dataset\": \"D012\"}, \"conclusion\": \"negative\", \"notes\": \"假设预判错误：预期 C0<5%（类似 QwQ-32B reasoning model），实际 C0=58.3%。DeepSeek-R1-Distill-Qwen-7B 因 7B 容量不足以维持确定性推理链，表现为 instruction-scale model。SICA -3.3pp，两子域对称（FOLIO -3.3pp, PW -3.3pp）。重新定位为第四个 instruction-scale 模型验证 capability trap。\"}, \"exp-010-mistral-v3\": {\"status\": \"DONE\", \"hypothesis\": \"Cross-family validation: Mistral-7B-Instruct-v0.3 在 D012 数据集(30PW+30FOLIO)上是否复现 SICA≈SC pattern——验证 capability trap 跨模型家族泛化（v3: 脚本内含 vLLM 清理+conda 环境，解决 v2 SIGTERM 问题）\", \"metrics\": {\"n\": 60, \"k\": 12, \"sica_accuracy\": 0.4833, \"sc_accuracy\": 0.4833, \"delta_pp\": 0, \"multi_candidate_rate\": 0.5, \"extraction_rate\": 0.8819, \"answer_extraction_rate\": 1, \"contradiction_rate\": 0.0562, \"discordant_sica_wins\": 2, \"discordant_sc_wins\": 2, \"mcnemar_p\": 1, \"proofwriter_sica\": 0.4, \"proofwriter_sc\": 0.4, \"proofwriter_delta_pp\": 0, \"folio_sica\": 0.5667, \"folio_sc\": 0.5667, \"folio_delta_pp\": 0, \"truncated_traces\": 0, \"model\": \"Mistral-7B-Instruct-v0.3\", \"dataset\": \"D012\"}, \"conclusion\": \"negative\", \"notes\": \"Mistral-7B cross-family: SICA 48.33% = SC 48.33%, delta=0.00pp。Multi-candidate rate 50%（30/60 题非 unanimous），SICA 仅改变 4 题（6.67% flip rate）。模型太弱：SC baseline 48.33%（近随机），trace 缺乏质量但有多样性。Discordant 2:2 平局，McNemar p=1.0。支持 operating regime 有下界：模型必须足够强才能生成有意义的 diverse traces。PW 40%/40%, FOLIO 56.67%/56.67%。\"}, \"sica_expanded_14b\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"sica_accuracy\": 0.765, \"sc_accuracy\": 0.762, \"sica_sc_gap_pp\": 0.3, \"n_problems\": 804, \"multi_candidate_rate\": 0.3818, \"folio_sica\": 0.794, \"folio_sc\": 0.794, \"folio_gap_pp\": 0, \"folio_n\": 204, \"proofwriter_sica\": 0.755, \"proofwriter_sc\": 0.752, \"proofwriter_gap_pp\": 0.3, \"proofwriter_n\": 600, \"extraction_rate\": 0.89, \"answer_extraction_rate\": 1, \"contradiction_rate\": 0.022, \"problems_with_contradictions\": 331, \"truncated_traces\": 0, \"wall_time_min\": 826}, \"notes\": \"实验完整完成 804/804 题并保存结果。EXIT_CODE=129 是 SIGHUP 伪信号（进程退出阶段收到），非真实失败。日志末尾打印 \\\"FULL_MVP_DONE\\\" 后才出现 exit code。D025 pivot 确认：SICA≈SC (+0.3pp, N=804)，D012 +3.3pp 是小样本噪声。FOLIO sub-claim dead (0pp)。\", \"hypothesis\": \"Qwen2.5-14B-Instruct 在 N=804 (600PW+204FOLIO) 上 SICA 相比 SC 有统计显著优势（p<0.05）——full-scale validation of D012 preliminary +3.3pp signal\"}, \"exp-019-llama8b-strategyqa-200\": {\"status\": \"DONE\", \"hypothesis\": \"Powered test: SICA 在弱模型（LLaMA-3.1-8B）上的增益在 n=200 StrategyQA 题时达到统计显著（p<0.05）——验证 operating regime 假设（D031 + exp-011 directionally positive +6.67pp）\", \"metrics\": {\"n\": 200, \"k\": 12, \"sica_accuracy\": 0.74, \"sc_accuracy\": 0.72, \"delta_pp\": 2, \"multi_candidate_rate\": 0.41, \"mcnemar_p\": 0.424, \"bootstrap_ci_95\": [-1.5, 5.5], \"bootstrap_p_delta_le_0\": 0.12, \"discordant_sica_wins\": 9, \"discordant_sc_wins\": 5, \"discordant_total\": 14, \"discordant_rate\": 0.07, \"sc_unanimous_rate\": 0.545, \"model\": \"LLaMA-3.1-8B-Instruct\", \"dataset\": \"StrategyQA\", \"wall_time_min\": 52}, \"conclusion\": \"negative\", \"notes\": \"StrategyQA 200题 powered test: SICA 74% vs SC 72%, +2.00pp, McNemar p=0.424, bootstrap CI [-1.5, +5.5] 跨零。统计不显著。exp-011 的 +6.67pp 在扩大样本后缩水 70%——小样本噪声。关键发现：(1) LLaMA-8B 在 StrategyQA 上 SC=72%，高于预期的 sweet spot (55-65%)，(2) 仅 14/200 (7%) discordant pairs，54.5% 全票一致，(3) SICA 仅充当 tiebreaker（9 wins 中 6 个是平票）。StrategyQA 不在 operating regime sweet spot 内。exp-020 FOLIO (SC≈60%) 是真正的 definitive test。\"}, \"exp-018-arc-v2\": {\"status\": \"DONE\", \"hypothesis\": \"Cross-domain validation: Qwen2.5-14B-Instruct 在 ARC-Challenge (科学多选, ABCD) 上 SICA vs SC——验证 capability trap 是否跨任务类型泛化（v2: build_generator bug 已修复）\", \"conclusion\": \"success\", \"metrics\": {\"n\": 60, \"k\": 12, \"sica_accuracy\": 0.95, \"sc_accuracy\": 0.9667, \"delta_pp\": -1.67, \"multi_candidate_rate\": 0.05, \"extraction_rate\": 1, \"contradiction_detected\": 3, \"discordant_sica_wins\": 0, \"discordant_sc_wins\": 1, \"dataset\": \"ARC-Challenge\", \"model\": \"Qwen2.5-14B-Instruct\"}, \"notes\": \"ARC-Challenge cross-domain: SICA 95.00% vs SC 96.67%, gap=-1.67pp. SICA 略逊于 SC。模型在 ARC 上 baseline 极高(96.67%)，接近天花板——高准确率区间多样性低，SICA 无操作空间。与 StrategyQA (+3.33pp n.s.) 对比：简单任务（高 baseline）SICA 无效或有害，中等难度任务有微弱正向趋势但不显著。整体支持 capability trap：模型能力越强/任务越简单 → SC 已近最优 → SICA 无增量。\"}, \"exp-009-overhead-analysis\": {\"status\": \"DONE\", \"hypothesis\": \"SICA pipeline 的 wall-time overhead breakdown: trace generation vs constraint extraction vs MaxSAT solving 各占多少——量化 SICA 相对 SC 的额外计算成本\", \"metrics\": {\"n\": 804, \"mean_total_wall_s\": 61.6, \"mean_trace_gen_s\": 31.6, \"trace_gen_pct\": 51.3, \"mean_extract_s\": 29, \"extract_pct\": 47, \"mean_dedup_s\": 1, \"dedup_pct\": 1.6, \"mean_maxsat_s\": 0.003, \"maxsat_pct\": 0.005, \"sica_overhead_s\": 30, \"sica_overhead_pct\": 48.7, \"pw_overhead_pct\": 51.3, \"folio_overhead_pct\": 38.6, \"p50_overhead_pct\": 48.9, \"p90_overhead_pct\": 57.6}, \"conclusion\": \"success\", \"notes\": \"SICA overhead 分析 (804题)：总时间 61.6s/题，其中 trace 生成 31.6s (51.3%)，约束提取 29.0s (47.0%)，去重 1.0s (1.6%)，MaxSAT 0.003s (≈0%)。SICA vs SC 多花 30.0s/题 (+48.7%)，开销几乎全部来自 constraint extraction LLM 调用。MaxSAT 求解可忽略。论文 insight：SICA 的计算瓶颈不在 formal reasoning (SAT) 而在 LLM extraction，且 extraction 产出的约束缺乏判别力——高成本低回报。\"}, \"exp-020-llama8b-folio-204\": {\"status\": \"DONE\", \"hypothesis\": \"Powered FOLIO test: SICA 在弱模型（LLaMA-3.1-8B）上 FOLIO 全量 204 题是否达到统计显著——FOLIO 在 exp-011 中信号最强（+10pp, bootstrap p≈0.04），n=204 几乎必然显著。保险实验：若 StrategyQA discordant rate 低导致 underpowered。\", \"metrics\": {\"n\": 204, \"k\": 12, \"sica_accuracy\": 0.608, \"sc_accuracy\": 0.632, \"delta_pp\": -2.45, \"mcnemar_p\": 0.2668, \"bootstrap_ci_95\": [-5.88, 0.98], \"bootstrap_p_sica_ge_sc\": 0.1, \"discordant_sica_wins\": 4, \"discordant_sc_wins\": 9, \"discordant_total\": 13, \"discordant_rate\": 0.064, \"multi_candidate_rate\": 0.618, \"extraction_rate\": 0.942, \"answer_extraction_rate\": 0.951, \"contradiction_rate\": 0.062, \"both_wrong\": 71, \"model\": \"LLaMA-3.1-8B-Instruct\", \"dataset\": \"FOLIO-204\", \"wall_time_min\": 131.7}, \"conclusion\": \"negative\", \"notes\": \"DEFINITIVE NEGATIVE。LLaMA-8B FOLIO 204题：SICA 60.8% vs SC 63.2%, delta=-2.45pp, McNemar p=0.2668, CI [-5.88, +0.98]。Discordant 4:9 SICA 输多赢少。exp-011 FOLIO +10pp 在 n=204 完全反转为 -2.45pp——确认为 Type I error (n=30 随机波动)。C0=61.8% 高（SICA 有操作空间），但约束改票时反而引入更多错误(9 SC wins vs 4 SICA wins)。Sweet spot hypothesis 被否定。SICA≤SC everywhere 确认。\"}, \"pilot-contrastive-prompt\": {\"status\": \"DONE\", \"hypothesis\": \"Contrastive Prompt Extraction: 将 prompt 改为\\\"列出支持答案X/反对答案Y的证据\\\"能否将 discriminative ratio 从 37.2% 提升至 >70%，并使 SICA(contrastive) > SC ≥3pp——验证 answer-conditioned 约束是否解决 SICA 机制 vacuous 问题\", \"conclusion\": \"failed\", \"notes\": \"脚本已验证可用（run_pilot_contrastive_v2.sh + pilot_contrastive_constraints.py）。修复方案：submit 时用 bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && bash /root/symb_invariant_consensus/scripts/run_pilot_contrastive_v2.sh\\\" 包裹。当前 GPU 被 exp-010-mistral-v3 占用（vLLM 87880MiB），等其完成后提交。\"}, \"exp-011-llama8b-v3\": {\"status\": \"DONE\", \"hypothesis\": \"Cross-family validation: LLaMA-3.1-8B-Instruct 在 D012 数据集(30PW+30FOLIO)上是否复现 SICA≈SC pattern——验证 capability trap 非 Qwen-specific（v3: 模型 shard 已修复，GPU 空闲后提交）\", \"conclusion\": \"success\", \"metrics\": {\"n\": 60, \"k\": 12, \"sica_accuracy\": 0.6667, \"sc_accuracy\": 0.6, \"delta_pp\": 6.67, \"multi_candidate_rate\": 0.6167, \"extraction_rate\": 0.8556, \"answer_extraction_rate\": 0.8958, \"contradiction_rate\": 0.0527, \"problems_with_contradictions\": 43, \"truncated_traces\": 44, \"discordant_sica_wins\": 5, \"discordant_sc_wins\": 1, \"mcnemar_p\": 0.2188, \"proofwriter_sica\": 0.6333, \"proofwriter_sc\": 0.6, \"proofwriter_delta_pp\": 3.33, \"folio_sica\": 0.7, \"folio_sc\": 0.6, \"folio_delta_pp\": 10, \"model\": \"LLaMA-3.1-8B-Instruct\", \"dataset\": \"D012\", \"wall_time_min\": 66.4}, \"notes\": \"LLaMA-3.1-8B cross-family: SICA 66.7% vs SC 60.0%, +6.67pp (最大增益)。Discordant 5:1 强烈倾向 SICA。FOLIO +10pp, PW +3.33pp。McNemar p=0.22（n=60 受限）。Multi-candidate rate 61.7%（vs Qwen-14B 46%）——弱模型更多样→SICA 有更大操作空间。44 条 truncated traces（max-tokens 可能偏短），但仍有效。关键：SC baseline 60%（远低于 Qwen-14B 的 76%），验证 capability trap 的正面——模型弱时 SICA 有用。\"}, \"exp-010-mistral-v2\": {\"status\": \"DONE\", \"hypothesis\": \"Cross-family validation: Mistral-7B-Instruct-v0.3 在 D012 数据集(30PW+30FOLIO)上是否复现 SICA≈SC pattern——验证 capability trap 跨模型家族泛化（v2: 修复 max-model-len=8192 防 400 循环）\", \"conclusion\": \"failed\", \"notes\": \"SIGTERM (exit 143) 在提交后 ~15s。根因：compound command 中 pkill -f \\\"vllm.entrypoints\\\" 可能误杀 tmux 父进程链。Director 已明确禁止 pkill 和 bash 脚本写在同一行。需要 v3：先手动清理 vLLM，再独立提交脚本。\"}, \"pilot-constraint-filtering\": {\"status\": \"DONE\", \"hypothesis\": \"Constraint Consistency Filtering: 只保留在≥T条traces中重复出现的约束能否提升SICA accuracy超过SC——验证约束质量过滤是否解决capability trap\", \"conclusion\": \"negative\", \"notes\": \"NEGATIVE confirmed. T=1/2/3 结果完全一致(+2.33pp=1题翻转), T≥5 SICA退化为SC。Discriminative analysis: unique constraints 中 11.5% 是 discriminative (by count), 37.2% (by weight)。但有效 flip 率仅 4/23=17.4%。根本原因：提取的约束是 domain facts (kind_charlie==True, Implies(...)) — 无论答案是什么，中间推理步骤大部分共通。约束系统未提取答案级别判别谓词。Constraint filtering 天花板极低，不是 rescue path。\", \"metrics\": {\"n\": 43, \"thresholds_tested\": [1, 2, 3, 5, 7], \"best_gap_pp\": 2.33, \"best_T\": 1, \"sica_T1\": 0.7674, \"sc\": 0.7442, \"T5_gap\": 0, \"T7_gap\": 0, \"discriminative_ratio_count\": 0.115, \"discriminative_ratio_weight\": 0.372, \"effective_flip_rate\": 0.174, \"multi_answer_problems\": 23, \"unanimous_problems\": 20, \"problems_disc_favors_different\": 4}}, \"exp-018-arc\": {\"status\": \"DONE\", \"hypothesis\": \"Cross-domain validation: Qwen2.5-14B-Instruct 在 ARC-Challenge (科学多选, ABCD) 上 SICA vs SC——验证 capability trap 是否跨任务类型泛化（多选题型）\", \"conclusion\": \"failed\", \"notes\": \"NameError: name 'build_generator' is not defined in eval_arc.py:142. 代码bug——函数未定义/未导入。Worker 诊断修复中。\"}, \"exp-017-strategyqa-v3\": {\"status\": \"DONE\", \"hypothesis\": \"Cross-domain validation: Qwen2.5-14B-Instruct 在 StrategyQA (常识推理, Yes/No) 上 SICA vs SC——验证 capability trap 是否跨任务类型泛化（v3: 修复 True/False→Yes/No 提取 bug）\", \"conclusion\": \"success\", \"metrics\": {\"n\": 60, \"k\": 12, \"sica_accuracy\": 0.5667, \"sc_accuracy\": 0.5333, \"delta_pp\": 3.33, \"mcnemar_chi2\": 0.5, \"mcnemar_p\": \"n.s.\", \"bootstrap_ci_95\": [0, 8.33], \"bootstrap_p_delta_le_0\": 0.1346, \"multi_candidate_rate\": 0.1, \"contradiction_detected\": 5, \"extraction_rate_problem\": 1, \"extraction_rate_trace\": 0.704, \"discordant_sica_wins\": 2, \"discordant_sc_wins\": 0}, \"notes\": \"StrategyQA跨域验证: SICA 56.67% vs SC 53.33%, +3.33pp n.s. (p=0.13), 支持capability trap跨任务泛化; v3修复提取bug确认成功(100%问题级提取率); 2个discordant pairs均SICA胜出\"}, \"exp-017-strategyqa-v2\": {\"status\": \"DONE\", \"hypothesis\": \"Cross-domain validation: Qwen2.5-14B-Instruct 在 StrategyQA (常识推理, Yes/No) 上 SICA vs SC——验证 capability trap 是否跨任务类型泛化（非逻辑/数学域）\", \"conclusion\": \"failed\"}, \"exp-017-strategyqa\": {\"status\": \"DONE\", \"hypothesis\": \"Cross-domain validation: Qwen2.5-14B-Instruct 在 StrategyQA (常识推理, Yes/No) 上 SICA vs SC——验证 capability trap 是否跨任务类型泛化（非逻辑/数学域）\", \"conclusion\": \"failed\"}, \"exp-010-mistral\": {\"status\": \"DONE\", \"hypothesis\": \"Cross-family validation: Mistral-7B-Instruct-v0.3 在 D012 数据集上是否复现 SICA≈SC pattern——验证 capability trap 跨模型家族泛化\", \"notes\": \"模型已确认完整下载：3 shards (4.95+5.00+4.55GB) + consolidated.safetensors (14.5GB)。排在 exp-018 之后启动。需要 Worker 准备启动脚本（参照 exp-011 模式）。\", \"conclusion\": \"failed\"}, \"exp-011-llama8b-v2\": {\"status\": \"DONE\", \"hypothesis\": \"Cross-family validation: LLaMA-3.1-8B-Instruct 在 D012 数据集(30PW+30FOLIO)上是否复现 SICA≈SC pattern——验证 capability trap 非 Qwen-specific (v2: 修复 GPU OOM，kill 旧 vLLM 后重跑)\", \"conclusion\": \"failed\"}, \"sica_temp_diversity\": {\"status\": \"DONE\", \"hypothesis\": \"不同 temperature (0.7/0.9/1.0) 下 QwQ-32B 是否产生足够的 trace 分歧以触发 MAX-SAT 矛盾检测\", \"conclusion\": \"negative\", \"metrics\": {\"temperatures_tested\": [0.7, 0.9, 1], \"problems_tested\": 3, \"problems_with_divergence\": 0, \"finding\": \"QwQ-32B produces zero answer divergence at all temperatures on MATH L4-5. Reasoning model's deterministic chain dominates sampling randomness.\", \"max_tokens_issue\": \"4096 tokens insufficient for some L5 problems (truncation)\", \"recommendation\": \"Use AIME 2024 (harder, ~79.5% acc) or non-reasoning model for trace diversity\"}}, \"sica_d012_14b\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"sica_accuracy\": 0.7333, \"sc_accuracy\": 0.7, \"sica_sc_gap_pp\": 3.3, \"c0_multi_candidate_rate\": 0.5333, \"c1_extraction_rate\": 1, \"c2_contradiction_problems\": 34, \"c3_gap_pp\": 3.3, \"bootstrap_p\": 0.2261, \"proofwriter_sica\": 0.6667, \"proofwriter_sc\": 0.6667, \"folio_sica\": 0.8, \"folio_sc\": 0.7333, \"total_constraints_raw\": 5849, \"total_constraints_unique\": 1735, \"maxsat_exclusion_rate\": 0.0259, \"wall_time_min\": 58.3, \"d012_verdict\": \"ALL_PASS\"}, \"hypothesis\": \"Qwen2.5-14B-Instruct 在 D012 (30PW+30FOLIO) 上 SICA pipeline 端到端有效：C0(多候选率≥20%) + C1(提取率≥80%) + C2(矛盾率≥10%) + C3(SICA>SC) 四项 sanity check 全通过\"}, \"sica_k_sensitivity_14b\": {\"status\": \"DONE\", \"hypothesis\": \"K-ablation: K={6,8,11,12,16,20} 对 SICA 效果的影响。K=11(奇数)无平票，若 gap=0 则证明 SICA 仅靠 tiebreak 生效\", \"conclusion\": \"success\", \"metrics\": {\"K6_sica\": 0.733, \"K6_sc\": 0.733, \"K6_gap_pp\": 0, \"K8_sica\": 0.733, \"K8_sc\": 0.75, \"K8_gap_pp\": -1.7, \"K11_sica\": 0.733, \"K11_sc\": 0.733, \"K11_gap_pp\": 0, \"K12_sica\": 0.7, \"K12_sc\": 0.75, \"K12_gap_pp\": -5, \"K16_sica\": 0.717, \"K16_sc\": 0.75, \"K16_gap_pp\": -3.3, \"K20_sica\": 0.7, \"K20_sc\": 0.733, \"K20_gap_pp\": -3.3, \"all_K_sica_leq_sc\": true, \"larger_K_degrades_sica\": true}, \"notes\": \"K-ablation 实际完成（EXIT_CODE=129 为 SIGHUP 假失败，同 sica_expanded_14b 模式）。结果：SICA ≤ SC for all K。K=11(奇数)验证 tiebreak 无贡献(gap=0)。K=12/16/20 SICA 退化 -3~5pp，表明更多 traces 引入更多低质量约束反而有害。直接强化 C1 (mechanism vacuous)。Artifact: art_20260517_2c1577。\"}, \"exp-011-llama8b\": {\"status\": \"DONE\", \"hypothesis\": \"Cross-family validation: LLaMA-3.1-8B-Instruct 在 D012 数据集(30PW+30FOLIO)上是否复现 SICA≈SC pattern——验证 capability trap 非 Qwen-specific\", \"notes\": \"Prep done by worker_prep_exp-011-llama8b_20260516T204635. Model: LLaMA-3.1-8B-Instruct (14GB, 4 shards). Script: /root/symb_invariant_consensus/scripts/run_exp011_llama8b.sh. Dataset: D012 (30 PW + 30 FOLIO = 60 题). 预估 ~25-30GB GPU, ~1-1.5h runtime. 等 sica_k_sensitivity_14b 完成后启动。\", \"conclusion\": \"failed\"}, \"exp-016-weighted-sc\": {\"status\": \"DONE\", \"hypothesis\": \"加权投票变体(inverse-length/length-weighted/constraint-count)是否比 uniform SC 有统计显著优势——验证简单启发式能否替代 SICA 或超越 SC\", \"conclusion\": \"success\", \"metrics\": {\"sica_accuracy\": 0.7649, \"sc_uniform_accuracy\": 0.7624, \"inv_length_accuracy\": 0.7674, \"length_weighted_accuracy\": 0.7525, \"constraint_count_accuracy\": 0.7525, \"inv_length_vs_sc_p\": 0.453, \"length_vs_sc_p\": 0.153, \"inv_length_vs_sica_p\": 0.864, \"length_vs_sica_p\": 0.066, \"n_problems\": 804, \"all_nonsignificant\": true}, \"notes\": \"exp-016 weighted SC baselines 完成。804题上所有加权变体 vs SC/SICA 均不显著(p>0.05)。Length-weighting 反而 -1pp（长 trace 略不可靠），inv-length +0.5pp 但非显著。结论：简单启发式加权不能替代也不能超越 uniform voting。支持 C1 (mechanism vacuous) — 问题不在聚合方式，而在约束质量本身。Artifacts: art_20260516_c7cc07 (report), art_20260516_7eef43 (data).\"}, \"exp-005\": {\"status\": \"DONE\", \"hypothesis\": \"QwQ-32B 作为 reasoning model 展示 SICA 的 operating regime boundary: 模型过强→diversity 消失→SICA≡SC\", \"metrics\": {\"qwq_aggregate_c0_nominal_pct\": 10.3, \"qwq_aggregate_c0_effective_pct\": 2.6, \"qwen14b_c0_pct\": 46, \"diversity_ratio_effective\": 17.7, \"aime_delta_pp\": 0, \"proofwriter_delta_pp\": -5.9, \"aime_n\": 22, \"proofwriter_n\": 17, \"temp_diversity_n\": 5, \"folio_n\": 2, \"total_problems\": 46, \"c0_threshold\": 20, \"qwq_below_threshold\": true}, \"conclusion\": \"negative\", \"notes\": \"exp-005 Operating Regime Analysis 完成。QwQ-32B 综合 46 题数据：effective C0=2.6%，远低于 20% 阈值。数学域 SICA≡SC (Δ=0pp, AIME 22题)，逻辑域 SICA&lt;SC (Δ=−5.9pp, PW 17题)。对比 Qwen2.5-14B C0=46% (17.7x)。直接支持 paper Claim 2 (operating regime boundary)。Artifacts: art_20260516_bf444f (data), art_20260516_d6966d (report)。\"}, \"sica_folio30\": {\"status\": \"DONE\", \"hypothesis\": \"逻辑域（FOLIO）上 SICA 能否利用 FOL 标注检测跨路径矛盾并超越 SC@K=12——FOLIO 有天然 FOL 标注，是 SICA 约束提取的理想场景\", \"notes\": \"废弃：QwQ-32B spec（max_tokens=12288），已被 sica_d012_14b（Qwen2.5-14B-Instruct 全量 D012 评估）覆盖。QwQ-32B 全域 C0 FAIL (3.6%)，模型已 pivot。\", \"conclusion\": \"killed\"}, \"sica_d016_c0_precheck\": {\"status\": \"DONE\", \"hypothesis\": \"D016 模型 pivot C0 预检：Qwen2.5-14B-Instruct 在逻辑域是否产生足够 trace 多样性（多候选率 ≥20%）\", \"metrics\": {\"multi_candidate_rate_combined\": 0.46, \"multi_candidate_rate_folio\": 0.4, \"multi_candidate_rate_proofwriter\": 0.5, \"sc_accuracy_combined\": 0.73, \"sc_accuracy_folio\": 0.8, \"sc_accuracy_proofwriter\": 0.69, \"n_problems\": 26, \"n_folio\": 10, \"n_proofwriter\": 16, \"K\": 6, \"T\": 0.7, \"total_time_s\": 280, \"c0_gate\": \"PASS (46% >= 20%)\", \"model\": \"Qwen2.5-14B-Instruct\", \"vllm_gpu_mem_gib\": 27.6, \"smoke_test\": \"2 problems end-to-end OK, constraints 21-26 per problem\"}, \"conclusion\": \"success\", \"notes\": \"C0 PASS: Qwen2.5-14B-Instruct 多候选率 46% (FOLIO 40%, ProofWriter 50%)，远超 20% 阈值。对比 QwQ-32B 全域 3.6%，提升 12.8x。SC accuracy 73% (FOLIO 80%, PW 69%)。Smoke test 2题 SICA pipeline 端到端通过。vLLM PID 174291, 27.6 GiB, max-model-len=8192。Report: art_20260516_e2774d。\"}, \"sica_proofwriter30_v2\": {\"status\": \"DONE\", \"hypothesis\": \"逻辑域（ProofWriter D5）上 SICA 能否检测跨路径 FOL 约束矛盾并超越 SC@K=12（v2: max_tokens=12288 修复）\", \"notes\": \"16/30 killed (Director 指令)。D012 四项全 FAIL。MaxSAT 根因诊断结论：三层问题叠加——(1) 约束提取失败 54.4%，QwQ-32B 收到 extraction prompt 后重新推理而非输出 JSON，3/4 多候选题提取为零；(2) 一致投票=一致约束，14/17 题 12/12 同一答案，约束天然不矛盾（正确行为非 bug）；(3) 评分偏差，唯一 SICA≠SC 的题 498_Q8，SICA 给少数派 38 分 > 多数派 27 分，因提取失败非随机。MaxSAT 求解器本身无 bug（注入测试 6/6 通过）。推荐修复：L3 自动注入 answer==trace_answer 约束使不同答案 trace 必有冲突；L1 提取用 system prompt 强制 JSON-only。\", \"conclusion\": \"killed\"}, \"sica_proofwriter30\": {\"status\": \"DONE\", \"hypothesis\": \"逻辑域（ProofWriter D5）上 SICA 能否检测跨路径 FOL 约束矛盾并超越 SC@K=12——验证 SICA 在逻辑推理域的有效性\", \"conclusion\": \"failed\", \"notes\": \"配置错误导致完全失败。--max-tokens 16384 等于 vLLM 的 --max-model-len 16384，prompt 输入空间为 0，所有 30 题从第 1 题起全部 400 Bad Request。没有生成任何 trace，没有提取约束，没有投票。4 分钟内跑完（全是 retry 耗时）。无法评估 sanity check 标准。需要用 --max-tokens 12288 或更小值重跑（AIME 实验用的 10240 正常工作）。\", \"metrics\": {\"sica_accuracy\": \"0/30 (0.0%)\", \"sc_accuracy\": \"0/30 (0.0%)\", \"sica_sc_gap_pp\": 0, \"total_wall_time_s\": 238.9, \"total_wall_time_min\": 4, \"avg_time_per_problem_s\": 8, \"traces_generated\": 0, \"constraints_extracted\": 0, \"traces_with_constraints\": 0, \"unique_constraints\": 0, \"maxsat_satisfied\": 0, \"maxsat_excluded\": 0, \"multi_candidate_rate\": \"N/A (no traces generated)\", \"vote_diversity\": \"N/A\", \"z3_errors\": 0, \"z3_timeouts\": 0, \"problems_with_contradiction\": 0, \"problems_with_votes\": 0, \"failure_mode\": \"ALL_400_BAD_REQUEST\", \"failure_count\": \"30/30\", \"root_cause\": \"max_tokens=16384 equals max_model_len=16384, leaving 0 tokens for prompt input. Every API call returns 400.\"}}, \"sica_aime30_v3\": {\"status\": \"DONE\", \"hypothesis\": \"AIME 2024 上 SICA 能否检测跨路径矛盾并超越 SC@K=12（v3: timeout=1800s, 从v2 P5恢复继续）\", \"notes\": \"v3 killed at 22/30 (PID 129992, 6h11m). Vote diversity analysis: multi-candidate rate = 0.0%, all valid problems have exactly 1 candidate. SICA≡SC confirmed structural. 6/22 problems with 0 votes (extraction failure). 数学域结论锁定，转逻辑域。\", \"metrics\": {\"progress\": \"22/30\", \"sica_accuracy_interim\": \"16/22 (72.7%)\", \"sc_accuracy_interim\": \"16/22 (72.7%)\", \"sica_sc_gap_pp\": 0, \"avg_time_per_problem_s\": 645.9, \"runtime_h\": 5.9, \"remaining_problems\": 8, \"vote_diversity_analysis\": {\"valid_problems\": 16, \"total_problems\": 22, \"multi_candidate_rate\": 0, \"zero_vote_problems\": 6, \"zero_vote_indices\": [1, 7, 8, 10, 13, 14], \"constraints_extracted\": \"19/22\", \"exclusion_rate\": 0.387, \"conclusion\": \"All 16 valid problems have exactly 1 candidate answer. SICA≡SC structurally. MaxSAT exclusion operates but cannot change final selection with only 1 candidate.\"}, \"process_status\": \"gone (cron miss 1/5)\"}, \"conclusion\": \"killed\"}, \"sica_aime30_v2\": {\"status\": \"DONE\", \"hypothesis\": \"AIME 2024 上 SICA 能否检测跨路径矛盾并超越 SC@K=12（v2: 修复 timeout/hang bug 后重跑）\", \"conclusion\": \"killed\", \"metrics\": {\"progress\": \"4/30\", \"sica_accuracy_interim\": \"3/4 (75%)\", \"sc_accuracy_interim\": \"3/4 (75%)\", \"avg_time_per_problem_s\": 557, \"p2_z3_error\": \"Z3Exception on z3_maxsat.py:163, 0 constraints extracted\", \"p5_vllm_stuck\": \"vLLM timeout since ~22:11, retried multiple rounds\", \"issue\": \"vLLM service likely crashed or OOM at Problem 5\", \"analysis_contradiction_rate_aime\": \"50% (2/4)\", \"analysis_contradiction_rate_math\": \"20% (1/5)\", \"analysis_unique_constraints_per_problem_aime\": 18.7, \"analysis_exclusion_rate\": \"10.7%\", \"analysis_sica_sc_agreement\": \"9/9 (100%)\", \"analysis_signal\": \"weak positive - mechanism works but SC too unanimous to flip\", \"analysis_p2_failure\": \"0 constraints, 0 votes - answer extraction failure\"}, \"notes\": \"失败原因: Problem 5 (aime2024_II_05, 凸六边形几何题) 12条并发trace在单GPU上竞争资源→每条trace吞吐极低→客户端~600s超时后重试→旧请求仍在vLLM running→恶性循环卡死~1h47min | 已有成果: 4/30题完成 SICA 3/4=75% SC 3/4=75%, P2有Z3Exception(0 constraints extracted) | vLLM本身健康(test request <1s) | 建议: 降低并发k或分批处理trace(如4条/批), 增大client timeout, kill stuck requests后重启\"}, \"sica_aime30_t07\": {\"status\": \"DONE\", \"hypothesis\": \"AIME 2024（QwQ-32B 弱项，~79.5% acc）上 SICA 能否检测更多跨路径矛盾并超越 SC@K=12——验证\\\"SICA 价值随问题难度递增\\\"假设\", \"conclusion\": \"killed\"}, \"mvp_math50_t07\": {\"status\": \"DONE\", \"hypothesis\": \"SICA MVP: 50题MATH-500上跨路径MAX-SAT约束共识能否检测矛盾并超越SC@K=12\", \"conclusion\": \"killed\"}, \"sica_smoke_5q\": {\"status\": \"DONE\", \"hypothesis\": \"SICA smoke test: 验证端到端 pipeline 可行性（5题 MATH-500, K=12, QwQ-32B）\", \"conclusion\": \"success\", \"metrics\": {\"sica_accuracy\": 0.8, \"sc_accuracy\": 0.8, \"extraction_rate\": 1, \"problems_with_contradictions\": 1, \"total_problems\": 5, \"total_time_s\": 3505, \"avg_time_per_problem_s\": 701, \"per_problem\": [{\"id\": \"algebra/2470\", \"level\": 1, \"sica_correct\": true, \"sc_correct\": true, \"constraints\": 27, \"unique\": 9, \"excluded\": 0}, {\"id\": \"prealgebra/65\", \"level\": 2, \"sica_correct\": true, \"sc_correct\": true, \"constraints\": 26, \"unique\": 2, \"excluded\": 0}, {\"id\": \"number_theory/847\", \"level\": 3, \"sica_correct\": true, \"sc_correct\": true, \"constraints\": 21, \"unique\": 11, \"excluded\": 0, \"note\": \"14 JSON parse failures, 1693s\"}, {\"id\": \"precalculus/1199\", \"level\": 4, \"sica_correct\": false, \"sc_correct\": false, \"constraints\": 35, \"unique\": 6, \"excluded\": 0, \"note\": \"graph-reading problem, model cannot see image\"}, {\"id\": \"algebra/2277\", \"level\": 5, \"sica_correct\": true, \"sc_correct\": true, \"constraints\": 60, \"unique\": 6, \"satisfied\": 3, \"excluded\": 3}]}}, \"smoke-test-5q\": {\"status\": \"PREPARING\", \"conclusion\": \"failed\"}, \"crd_folio_main\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"hypothesis\": \"CRD: 双表征(FOL+SymPy)分歧检测+定向修复能提升逻辑推理准确率（非SICA方法）\", \"metrics\": {\"divergence_rate\": 0.422, \"diagnosis_rate\": 0.872, \"error_types\": 4, \"directed_advantage_pp\": 4.7, \"directed_p_value\": 0.63, \"localization_accuracy\": 0.946, \"fol_accuracy\": 0.789, \"code_accuracy\": 0.598, \"oracle_accuracy\": 0.878, \"pipeline_accuracy\": 0.814, \"baseline_accuracy\": 0.74, \"cost_multiplier\": 5.76, \"dataset\": \"FOLIO\", \"n\": 204}}}, \"count\": 165, \"total\": 165, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.4728}}"
    }
  }
}
```

</details>

---

### Tool result

_source line 15 · 2026-05-22T14:51:25.484Z_

<details><summary>↩ Tool result · `toolu_012G1AFdwChAccCBGv5XFSLP`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/paper_framing.md\", \"content\": \"# Paper Framing — symb_invariant_consensus\\n\\n## Target Venue\\n- Primary: EMNLP 2026 Main (ARR May 25)\\n- Deadline: May 25, 2026 (ARR submission)\\n\\n## D063 Direction: Entropy Decomposition + Quality Ladder — 目标 4.0\\n\\n**从 D060 \\\"Pure Analysis / negative result\\\" 升级为 \\\"Regime-Dependent Mechanism Analysis with Entropy Decomposition\\\"。** 用户决定冲 4.0。\\n\\n### Entropy Breakdown 验证结果 (2026-05-19 completed)\\n\\n**跨模型 entropy mechanism 一致性: 不成立。Selective SICA 非 universal 方案。**\\n\\n但 entropy decomposition 揭示了更有价值的 regime mechanism：\\n\\n| Experiment | Model | Dataset | High-E n | High-E Δpp | Low-E n | Low-E Δpp |\\n|-----------|-------|---------|----------|-----------|---------|----------|\\n| exp-033 s42 | Mistral-7B | FOLIO | 78 | **+12.8** | 126 | 0.0 |\\n| exp-052 s123 | Mistral-7B | FOLIO | 77 | **+9.1** | 127 | 0.0 |\\n| exp-053 s456 | Mistral-7B | FOLIO | 75 | -1.3 | 129 | 0.0 |\\n| exp-046 | Mistral-7B | PW-600 | 267 | -4.9 | 333 | -1.2 |\\n| exp-036 | Qwen2.5-14B | FOLIO | 37 | **-8.2** | 167 | -0.6 |\\n| exp-038 | Qwen2.5-14B | LogiQA | 23 | -4.3 | 177 | 0.0 |\\n| exp-035 | Qwen2.5-7B | FOLIO | 47 | -2.1 | 157 | 0.0 |\\n| exp-048 | LLaMA-8B | PW-600 | 76 | -3.9 | 104 | -1.9 |\\n\\n(注: SC/Δ 使用 pre-tiebreaking 值，entropy grouping 不受 tiebreaking 影响。D064 修正后 deltas 会略有变化但 pattern 不变。)\\n\\n**三个核心发现：**\\n1. **Low-entropy: SICA≈SC 跨模型一致** (8/8 experiments Δ≈0) → traces 一致时 constraints 无新信息\\n2. **High-entropy 方向因 regime 而异**：Goldilocks +12.8pp vs Type A -8.2pp vs Type C -4.9pp\\n3. **Mechanism 解释**：\\n   - Goldilocks (SC~55%, κ~0.46): 真实不确定性 → constraints 打破平局正确方向\\n   - Type A (SC>75%, κ>0.65): 偶发错误 → constraints 放大 confirmation bias\\n   - Type C (SC<40%, κ~0.20): 系统性错误 → constraints 是噪声\\n\\n### 调整后核心转变\\n\\n论文以 \\\"entropy decomposition 揭示 regime-dependent mechanism\\\" 为核心分析贡献（不是 universal diagnostic）：\\n- **Entropy decomposition 作为分析工具**：分离 SICA 作用点（high-entropy）vs 不作用点（low-entropy）\\n- **Regime mechanism 量化**：同样是 high-entropy 问题，direction depends on SC+κ → 完美支持 dual bottleneck\\n- **Abandoned**: Selective SICA 作为 universal practical contribution（只在 Goldilocks zone 有效）\\n- **Upgraded**: 核心图 = high-entropy Δ vs SC scatter（8 points, 3 regimes 清晰分离）\\n- **Quality Ladder** (D067: L1 NULL CONFIRMED)\\n  - L0: Self-extraction (Mistral→Mistral): 59.31%, Δ=+3.43pp ns\\n  - L1a: Qwen3-14B→Mistral traces: 60.29%, Δ=+4.41pp (+0.98pp vs self = 2题/204 = noise)\\n  - L1b: Qwen2.5-14B→Mistral traces: 58.33%, Δ=+2.45pp (-0.98pp vs self = 2题/204 = noise)\\n  - L3: Oracle 100% disc, Δ=+14.22pp p<0.001\\n  - **结论**: L1 ≈ L0 << L3。Bottleneck 在 traces（同源输入），不在 extractor（换模型无效）\\n  - **Paper contribution**: \\\"bottleneck is fundamental to extraction, not just model capability\\\" — 强化 structural limitation 论点\\n- **CJT/Eff-K 保留**：解释 why high-entropy behavior differs across regimes\\n\\nD060 要素全部保留：\\n- Condorcet independence 框架 → 理论基础\\n- 9 种修复全部失败 → structural limitation 证据\\n- 2/3 seeds positive trend but **0/3 significant** (D066: p=0.092/0.070/1.0) → Goldilocks zone 作为 directional trend, not confirmed effect\\n- K/T sensitivity non-monotonic → SC confound insight\\n- 用户指示: 投 May 25 不变，冲 4.0\\n\\n## Core Claims (5 条) — D060 纯 Analysis Framing\\n\\n### Analysis Claims (已验证)\\n\\n1. **Independence Bottleneck**: Self-consistency 隐含 Condorcet Jury Theorem 的独立性假设，但同模型采样的 traces 高度相关。Worker 验证的 κ 值：\\n   - Qwen-14B FOLIO: κ=0.744, Eff-K=1.31 (SC=75.49%, Δ=+0.25pp n.s.)\\n   - Qwen-14B LogiQA: κ=0.821, Eff-K=1.20 (SC=78.5%, Δ=+0.50pp n.s.)\\n   - Mistral-7B FOLIO s42 (exp-033): κ=0.501, Eff-K=1.84 (SC=55.88%, Δ=+3.43pp **p=0.092 ns**) ← primary seed [D064+D066]\\n   - Mistral-7B FOLIO s123: κ=0.491, Eff-K=1.88 (SC=54.41%, Δ=+2.94pp **p=0.070 ns**)\\n   - Mistral-7B FOLIO s456: κ=0.507, Eff-K=1.82 (SC=55.88%, Δ=0.00pp p=1.0 ns)\\n   - Mistral-7B PW-600 (exp-046): κ=0.210, Eff-K=3.63 (Δ=-2.83pp p=0.010, SC=39%)\\n   规律：跨模型对比清晰（Qwen Eff-K≈1.2-1.3 → 0 gain; Mistral Eff-K≈1.85-2.22 → variable gain）。但 Mistral seeds 内部，Eff-K 与 delta 非单调（exp-033 Eff-K 最低 1.85 却 delta 最高 +3.43pp）→ Eff-K 是跨模型必要条件，seed 内 variance 仍主导。exp-046 Eff-K 最高(3.63) 但 SC 太低(39%) 导致 delta 为负 → 需同时满足 sufficient Eff-K AND sufficient SC。\\n\\n2. **Oracle Gap Localizes Extraction Bottleneck**: Gold FOL + MAX-SAT = +14.22pp (p=2.0e-7)，自提取仅 +3.43pp (best seed, D064 corrected) = 24% utilization。聚合机制本身有效，瓶颈在自提取质量。Two-layer analysis:\\n   - **Constraint taxonomy**: 43% trivially_satisfied（被所有候选答案满足的约束，不排除任何答案）\\n   - **Discriminative filtering**: 仅 ~8% 约束在 MAX-SAT scoring 中完全 non-discriminative（移除后 0 gains）\\n   - **关键区分**: 43% 和 8% 度量不同。trivially_satisfied 约束在 MAX-SAT 中仍可有不同满足程度（partial vs full），所以不全是 non-discriminative。但即使 constraints 是 discriminative 的，它们的\\\"区分方向\\\"与模型自身偏差一致（confirmation bias）。both_wrong 组 score_range=29.4。九种修复全部失败。\\n\\n3. **Regime-Dependent Capability Trap**: SICA 有效性取决于提取模型的基线准确率，存在双边界：\\n   - Type A (SC ≥ ~60%): 确认偏差，constraints 镜像模型自身答案。**exp-034 vs exp-039 同配置 delta 翻转**: exp-034 Δ=+0.51pp (n=589), exp-039 Δ=-2.00pp (n=600)。SC baseline 方差 (3.38pp) >> SICA 效应 → Type A delta 是 trace sampling noise。SICA 比 SC 更稳定 (跨运行方差 0.87pp vs 3.38pp，仅 2 点，需更多 seed 验证)\\n   - Type C (SC ≤ ~40%): traces 主要错误，constraints 是噪声 (exp-046: Δ=-2.83pp, p=0.0095)\\n   - Goldilocks zone (~50-56% SC): 部分独立性 + 部分正确性 (exp-033: Δ=+3.43pp, p=0.092 ns; mean of 3 seeds: +2.12pp) ⚠️ D076 Reviewer: 0/3 seeds significant, 不应作为核心叙事支柱。作为 directional observation 保留，不做强 claim。\\n   - Type B: 领域不可形式化 (LogiQA: contradiction rate 0.8%)\\n\\n4. **C0+SC Two-Dimensional Diagnostic**: C0 (multi-candidate rate) + SC accuracy 形成零成本部署诊断。C0<5% → degenerate; high C0 + high SC → trap; high C0 + low SC → potential gains。\\n\\n### Remediation Evidence (D060: 全部失败 — 强化 analysis narrative)\\n\\n5. **Nine Remediation Attempts All Failed**: 原 6 种 + 3 种靶向修复全部无效，证明 independence bottleneck 是结构性的：\\n   - D059 三路 method improvement 全部失败：\\n     - Discriminative Filtering: 119/204 处理后 0 gains 1 loss，~92% 约束本身就是 discriminative，过滤是 near-no-op\\n     - T=1.0 (exp-054): delta 从 +3.43pp 崩塌到 0.00pp（D064 corrected），温度敏感性极端\\n     - Multi-Temp (exp-055): ✅ 完成，delta=+0.00pp (b=5,c=5 完美对称), SC=57.84%. 混合 T=0.3/0.7/1.2 各 4 traces 未改善 SICA。附带发现：multi-temp 提升 SC baseline (+3.4pp vs 单温度 54.41%)，说明混合温度对 majority voting 有帮助，但 SICA constraint extraction 无法利用这种 diversity → bottleneck 在 extraction 而非 trace diversity\\n   - 原 6 种：contrastive prompting, cross-model extraction, generational scaling, solver-guided refinement, consistency filtering, cross-trace UNSAT\\n   - 9 种修复涵盖 prompting / architecture / capability / verification / diversity / filtering 全维度，全部失败 → trap is fundamental\\n\\n## D070/D074 Update: Method-Level Interventions Also Fail — \\\"Fundamental Limitation\\\" Confirmed\\n\\n### Three Method Lines × Two Datasets = All Negative (D074)\\n\\nD070 从纯 analysis 升级为 analysis + method paper，但三条方法线全面失败（D074 确认），反而强化了原始 analysis 结论。\\n\\n**方法×数据集完整结果**：\\n| Method | FOLIO-204 | LogiQA-200 | Failure Mode |\\n|--------|-----------|------------|--------------|\\n| ICG (Independent Constraint Gen.) | Δ=-2.0pp (3-seed: -2.0/+1.5/-1.0, mean=-0.5pp±1.8pp, 噪声) | Δ=-0.5pp | Neutral — 独立约束质量≈trace-sourced约束 |\\n| Contrastive (Pro/Con Scoring) | Δ≈-16pp | Δ≈-7pp (interim) | Harmful — 26% degenerate scoring, pro/con 不平衡 |\\n| Debate (Proposer/Critic) | Δ=-18.6pp | Δ≈-28pp (interim) | Catastrophic — 7B 模型角色扮演严重退化推理 |\\n\\n**三种失败模式的分析价值**（论文 \\\"Why Methods Fail\\\" section）：\\n1. **ICG (neutral)**: 独立于 traces 生成的约束不比 trace-sourced 约束更好。说明 bottleneck 不仅是 \\\"约束来自 traces\\\"，而是模型的推理偏差从问题理解阶段就存在——独立约束和 trace-sourced 约束继承相同的 model bias。\\n2. **Contrastive (harmful)**: 强制 pro/con 评估引入 degenerate scoring（26% 问题无法有效区分）。7B 模型无法可靠生成平衡的对立约束——pro 约束系统性多于 con（94 pro vs 65 con），confirmation bias 从约束提取转移到了约束生成。\\n3. **Debate (catastrophic)**: Proposer/Critic/Defense 多角色链在 7B 模型上导致答案质量严重退化。辩论不仅未增加多样性，反而引入了角色扮演的额外认知负担。同模型辩论 = 同源性 + 角色扮演退化，双重损失。\\n\\n**Scale limitation caveat**: 所有方法测试在 7B 模型上。7B 模型生成 Z3 格式 FOL 约束的能力不足（ICG 多题 \\\"0/N constraints parsed\\\"）。14B+ 模型可能有不同结果——这既是 limitation 也是 future work 入口。\\n\\n### κ Generalization — Independence-Accuracy Trade-off (D075, CAPSTONE FINDING)\\n\\nexp-077 测量三种聚合方式在 Mistral-7B FOLIO-204 上的 κ 和 Eff-K：\\n| 聚合方式 | Fleiss' κ | Eff-K | 名义 K |\\n|----------|----------|-------|--------|\\n| Self-Consistency | 0.4384 | 2.02 | 10 |\\n| Diverse-Prompt | 0.4030 | 2.21 | 12 |\\n| LLM-Debate | 0.1549 | 4.44 | 12 |\\n\\n结合 exp-076 Debate Δ=-18.6pp 的准确率数据，揭示**同模型框架下的 fundamental independence-accuracy trade-off**：\\n- **SC/Diverse-Prompt**: κ~0.4，traces 高度相关但准确率正常。换 prompt 策略不改善独立性（Δκ=0.04）。\\n- **Debate**: κ=0.15，成功打破 trace 相关性（Eff-K 从 2.0 跃升到 4.4），但准确率崩溃 -18.6pp。低 κ 不代表\\\"更独立的推理\\\"——是 disagreement amplification（系统性噪声）。\\n- **Trade-off 本质**: 同一模型的推理能力是固定的。要么输出一致（高 κ, 正确但不独立），要么输出分歧（低 κ, 独立但不正确）。Condorcet Jury Theorem 要求 both independent AND accurate，同模型框架下无法同时满足。\\n\\n**论文叙事升级**: 从 \\\"methods fail\\\" → \\\"independence-accuracy trade-off is fundamental to same-model reasoning\\\"。突破瓶颈需要跨模型方案（不同模型天然更独立），Oracle 实验（gold FOL 来自外部知识源）已间接验证了这一点。\\n\\n### New Claim 6 (D070/D074)\\n\\n6. **Method-Level Interventions Cannot Break the Bottleneck**: 三种针对 independence bottleneck 不同环节的方法（ICG→循环依赖, Contrastive→confirmation bias, Debate→trace 同质性）在 2 个数据集上全部失败。加上之前 9 种 prompt-level 修复，共 12 种修复尝试全败。这证明 independence bottleneck 不是单一环节的问题，而是 same-model self-extraction 的根本性限制。\\n\\n### New Claim 7: Symbolic Confirmation Bias (D082 — CORE FINDING)\\n\\n7. **Symbolic Confirmation Bias**: LLM 从 CoT traces 提取的 FOL 约束系统性确认 trace 自身（可能错误的）答案，而非独立验证 ground truth。\\n   - SICA 判对题：gold constraint 78.1%，bias ratio = 0.28\\n   - SICA 判错题：错误 constraint 83.3%，bias ratio = **4.97×**\\n   - 97.6% SICA 错误与 SC 错误完全重合\\n   - SICA 翻盘的 12 例来自 minority trace diversity（43% gold support），不是 symbolic reasoning\\n   - **因果链**：模型推理→答案→从含答案 trace 提取 FOL→约束确认答案→聚合≈SC\\n   - **CEGIS 验证**：迭代精炼 R1 +3.43pp < 原始 SICA +4.9pp → 约束一致性不是瓶颈，偏向性才是\\n   - **Quality Ladder 验证**：L1 ≈ L0 << L3 → bottleneck 在 traces（同源输入），不在 extractor\\n\\n### New Claim 8: Process-κ (D082 — NEW METRIC)\\n\\n8. **Process-Level Independence (Process-κ)**: answer-κ 低估真实独立性瓶颈。CoT 推理过程相似性远高于答案一致性。\\n   - Mistral-7B FOLIO-204：CoT cosine similarity **0.69** >> answer-κ **0.41**\\n   - 两者几乎无相关性：r = -0.06, p = 0.36\\n   - 仅 **9.3%** trace 对是\\\"殊途同归\\\"（同答案不同路径）\\n   - answer-κ 是 true independence bottleneck 的 lower bound\\n   - 适用于所有 LLM trace aggregation 方法，不限于 SICA\\n\\n## D082/D085: Comprehensive Method Exhaustion — 25+ ALL Fail\\n\\nD080 启动全方向并行探索（Wave 1-3），在 D074 的 12 种修复基础上又测试 13+ 新干预：\\n\\n| 方法 | 类型 | 结果 | 关键数据 |\\n|------|------|------|----------|\\n| PROVE 代码验证 | paradigm shift | ❌ | Code gen 15.2%, accuracy=random |\\n| CEGIS 迭代精炼 | multi-round | ❌ | R1 +3.43pp < SICA +4.9pp |\\n| DeepConf 置信度 | filtering | ❌ | logprob 与正确性零相关 |\\n| Cross-model SICA | cross-model | ❌ | Δ=-0.49pp despite lower κ |\\n| Problem Perturbation | input diversity | ❌ | κ 升至 0.696 (反效果) |\\n| MIN-UNSAT | solver objective | ❌ | 49.5% < SC 54.4% |\\n| κ-aware SC | voting rule | ❌ | 11/11 Δ=0 |\\n| Z3 Trace Filter | trace filtering | ❌ | negative |\\n| Bootstrapped Gold | iterative | ❌ | negative |\\n| Selective Abstention | diagnostic | ⚡ | AUROC=0.673, +4.4pp@80%cov |\\n\\n**D085 总结**: 9 prompt-level + 3 method-level + 13 新方向 = **25+ 干预全部 negative**。Independence bottleneck 在 same-model self-extraction 框架下无解，所有维度（diversity/architecture/capability/verification/filtering/voting/solver/paradigm）已穷尽。\\n\\n## D090: Cross-Architecture External Verification — POSITIVE BREAKTHROUGH\\n\\n### New Claim 9: Cross-Architecture NLI Verification Breaks the Bottleneck\\n\\n9. **Cross-Architecture External Verification**: A lightweight encoder-only NLI model (microsoft/deberta-large-mnli) provides structurally complementary signal to decoder-only LLMs.\\n   - DeBERTa standalone: 49.51% (101/204) — not competitive alone, expected\\n   - **NLI+SC combo w=1 (NLI as 13th voter): 57.84% (118/204), +3.43pp vs SC** ← PRIMARY (has McNemar)\\n   - NLI+SC combo w=3: 58.82% (120/204), +4.41pp vs SC — McNemar p=0.078 NOT significant (b=6, c=15). Higher weight amplifies NLI weakness on Unknown.\\n   - NLI+SC combo w=5: 60.29% (+5.88pp) — Reviewer: w=5 overfitting risk, NOT main result\\n   - NLI∩SC agreement subset: 68.48% accuracy on 45% coverage — selective verification evidence\\n   - NLI-as-verifier (trust NLI on disagreement): 49.51% — FAILED (NLI only 34% correct when disagreeing)\\n   - SC baseline: 54.41% (111/204, primary Mistral-7B FOLIO eval, seed=None)\\n   - **McNemar (w=1 ONLY)**: p=0.039, significant at α=0.05. 9 discordant pairs (b=1, c=8). 95% CI [0.59pp, 6.28pp]. ⚠️ w=3 and w=5 McNemar NOT YET COMPUTED — do NOT attribute this p-value to other weights\\n   - **Model**: microsoft/deberta-large-mnli, **406M** parameters (not 350M, not 44M)\\n   - **Per-label complementarity (key insight)**:\\n     - False (contradiction): NLI **71.43%** vs SC 38.10% → NLI dominates (+33pp)\\n     - Unknown: NLI 18.84% vs SC **68.12%** → SC dominates (+49pp)\\n     - True: NLI 59.72% vs SC 55.56% → NLI slightly better\\n   - **Why it works**: DeBERTa is encoder-only + NLI fine-tuned → strong at contradiction detection (its training task). LLM is strong at uncertainty reasoning. Structurally complementary error profiles.\\n   - **Oracle connection**: Oracle (+14.22pp) proved aggregation works with quality constraints; DeBERTa provides partial external signal → partial oracle effect\\n   - **Narrative**: \\\"25+ same-model interventions fail, but even a simple cross-architecture voter provides modest positive signal — proof-of-concept for external architectural complementarity\\\"\\n\\n### New Claim 10: Constraint-Answer Decoupling — CONDITIONAL on full results (D092)\\n\\n10. **Constraint-Answer Decoupling (G)**: Removing conclusion sentences from reasoning traces before FOL extraction causally breaks Symbolic Confirmation Bias.\\n   - **⚠️ INTERMEDIATE results only (70/204 = 34%)**: 65.7% accuracy (+11.3pp vs SC 54.41%, +6.4pp vs SICA 59.31%)\\n   - Avg truncation ratio: **4.1%** — removing ~4% of trace text yields +11pp improvement\\n   - **Causal mechanism**: trace contains conclusion → FOL extractor reads conclusion → extracted constraints confirm conclusion → aggregation ≈ SC. G cuts this chain by removing the conclusion before extraction.\\n   - **Potential strengths**: (a) largest positive effect in the project, (b) minimal intervention (4.1% text removal), (c) directly tests the confirmed mechanism (confirmation bias)\\n   - **Risk (Reviewer critical)**: FOLIO 难度分布不均匀，前 70 题可能偏简单。历史先例：Direction F 42%→39.6%，Direction H 56.1%→微降。中间值可能虚高。\\n   - **Residual bias risk**: 即使截断显式结论，推理步骤仍可能暗示答案方向（\\\"the premises suggest...\\\"），extraction 模型仍可能产生 biased constraints。\\n   - **Full results pending**: PID 384984 on westd-16639, running to 204/204\\n   - **McNemar**: pending full results\\n   - **Narrative (if confirmed)**: \\\"25+ methods fail because they don't break the answer→constraint coupling. G directly severs this coupling via conclusion truncation — the diagnosis drives the fix.\\\"\\n\\n### Framing Decision Threshold (Reviewer-approved)\\n- G ≥+5pp AND p<0.05 → **commit V3** (G+R dual method, G as core)\\n- G +3-5pp AND p<0.10 → **V3 weak** (G as \\\"encouraging pilot\\\", not core method)\\n- G <+3pp OR n.s. → **fall back to V2** (R proof-of-concept) or **V1** (pure negative)\\n\\n### Updated Headline Result (D092 — V3 CONDITIONAL, awaiting G full results)\\n\\n\\\"Across 6+ models and 4 domains, symbolic consensus aggregation shows no statistically significant positive effect under same-model self-extraction. 25+ interventions fail. Root cause: Symbolic Confirmation Bias (4.97×). Two independent cures both succeed: (1) Constraint-Answer Decoupling removes conclusion sentences before FOL extraction, cutting the causal chain — +11.3pp (70/204 intermediate, PENDING FULL); (2) Cross-architecture NLI verification (DeBERTa) provides structurally complementary signal — +4.41pp (p=0.039). Both validate the diagnosis from orthogonal angles: G attacks the information flow, R attacks the architectural homogeneity.\\\"\\n\\n### Updated Headline Result (D090 — V2 FALLBACK, if G full results weaker than intermediate)\\n\\n\\\"Across 6+ models and 4 domains, symbolic consensus aggregation shows no statistically significant positive effect under same-model self-extraction. 25+ interventions fail. Root cause: Symbolic Confirmation Bias (4.97×). A cross-architecture proof-of-concept (DeBERTa NLI w=3) achieves +4.41pp (p=0.039) — the only positive result across 25+ attempts. Per-label analysis reveals structural complementarity: NLI dominates contradiction detection (71% vs SC 38%), while LLMs dominate uncertainty reasoning (68% vs NLI 19%).\\\"\\n\\n### Updated Story Spine (D092 — V3, G+R dual method)\\n\\n- **Problem**: [unchanged]\\n- **Theoretical lens**: [unchanged]\\n- **Systematic evaluation**: [unchanged]\\n- **Regime characterization**: [unchanged]\\n- **Remediation failures strengthen thesis (D085 FINAL)**: 9 prompt-level + 3 method-level + 13 new directions = **25+ interventions** across ALL dimensions (diversity/architecture/capability/verification/filtering/voting/solver/paradigm), all fail → bottleneck is fundamental and exhaustively proven\\n- **Method failure analysis**: Three methods targeting different bottleneck aspects show three distinct failure modes (neutral/harmful/catastrophic), revealing that the bottleneck operates at multiple levels simultaneously\\n- **Independence-accuracy trade-off (HERO FINDING, D075)**: Debate breaks trace correlation (κ 0.44→0.15, Eff-K 2.0→4.4) but accuracy collapses (-18.6pp/-23.0pp). Same-model traces can be independent OR accurate, not both.\\n- **Symbolic Confirmation Bias (CORE FINDING, D082)**: Root cause identified — self-extracted FOL constraints systematically confirm the trace's own answer (bias ratio 4.97× on incorrect problems). Causal chain: model reasons → answer → FOL extraction confirms answer → aggregation ≈ SC. This is WHY 25+ methods fail.\\n- **Process-κ (NEW METRIC, D082)**: CoT reasoning similarity (0.69) >> answer-κ (0.41), r=-0.06. Only 9.3% of trace pairs are \\\"convergent reasoning.\\\" answer-κ underestimates the true bottleneck. Novel metric applicable to all LLM trace aggregation.\\n- **NEW — Constraint-Answer Decoupling (CORE METHOD, D092)**: Having diagnosed the causal chain (conclusion→FOL→bias), we sever it: remove conclusion sentences before extraction. 4.1% text removal → +11.3pp (70/204). Minimal intervention, maximal effect. Directly proves the mechanism IS the cause.\\n- **NEW — Cross-Architecture Verification (COMPLEMENTARY METHOD, D092)**: DeBERTa NLI (406M) w=1 **+3.43pp (p=0.039, McNemar exact)** PRIMARY; w=3 +4.41pp (p=0.078 n.s.); NLI∩SC 68.48%@45%. Orthogonal fix: instead of fixing the extraction pipeline, add an architecturally independent voter. Per-label complementarity (NLI: False 71% vs SC 38%; SC: Unknown 68% vs NLI 19%).\\n- **Dual cure narrative**: G attacks information flow (removes biased input to extractor), R attacks architectural homogeneity (adds independent voter). Both work independently. Validates diagnosis from two angles.\\n- **Actionable contribution**: C0+SC diagnostic + κ-based Eff-K estimation + Decoupling method + NLI combo = complete toolkit from diagnosis to fix.\\n- **Universal across architectures (D078)**: Three families: Mistral-7B κ=0.438, LLaMA-8B κ=0.412, Qwen2.5-7B κ=0.658, Qwen2.5-14B κ=0.738. Family effect (Δκ=0.22) >> scale effect (Δκ=0.08).\\n- **Headline (D092)**: Independence bottleneck is structural to same-model extraction, universal across architectures, rooted in Symbolic Confirmation Bias. 25+ same-model interventions fail. Two independent cures succeed: Decoupling (+11.3pp, CONDITIONAL on full 204) attacks the causal chain, Cross-Architecture NLI (+3.43pp, p=0.039) provides external diversity. Both prove the diagnosis and provide practical solutions.\\n\\n## Core Insight (D060 Updated — Dual Bottleneck)\\n\\n**Dual Requirement Framework**: SICA 效应需要同时满足两个条件，缺一不可：\\n1. **Sufficient Independence** (Eff-K > threshold): traces 需要提供足够多的独立视角\\n2. **Sufficient Quality** (SC > ~50%): traces 需要有足够的正确率，否则约束是噪声\\n\\nCondorcet Jury Theorem 要求投票者独立且 p>0.5。同模型采样的 reasoning traces 严重违反独立性假设（Fleiss' κ = 0.21–0.82，Eff-K 仅 1.20–3.63），解释了为什么简单增加 K 或添加符号约束不能突破 SC 的天花板。\\n\\n实验数据完美支持 dual requirement（κ 使用统一脚本 compute_fleiss_kappa_unified.py，SC/Δpp 使用 registry 原始值）：\\n- **Qwen family**: κ=0.66-0.82, Eff-K≈1.20-1.46（独立性不足）→ all near-zero delta，无论 SC 多高\\n- **Mistral-7B FOLIO**: κ≈0.46, Eff-K≈2.0（中等独立性）+ SC≈55%（中等质量）→ +3.43pp best seed, mean +2.12pp (2/3 seeds positive, 1 null)\\n- **Mistral-7B PW-600**: κ=0.20, Eff-K=3.76（最高独立性）但 SC=39%（质量不足）→ -2.83pp\\n- 只有 Goldilocks zone（中等 Eff-K + 中等 SC）出现正向 delta\\n- **Dual bottleneck 直接验证 (exp-055)**：Multi-temp κ=0.427 Eff-K=2.11（比单温度 κ≈0.46 Eff-K≈2.0 更独立）但 delta=0.00pp → 提高 independence 不够，还需要 extraction quality\\n- **T sensitivity 孤立尖峰 (4/4 complete, D064 corrected)**：T=0.3(Δ=-1.47), T=0.5(Δ=-0.98), T=0.7(Δ=+3.43, κ=0.460, Eff-K=1.98), T=1.0(Δ=0.00, κ=0.394, Eff-K=2.25)。T=0.7 孤立尖峰更突出。T=0.7 SC=55.88%（最低）→ entropy 最高 → SICA 操作空间最大。温度效应与 SC 效应互为 confound，论文需讨论\\n- **Thinking mode κ=0.913, Eff-K=1.09 (exp-028b)**：近乎确定性。思维模式让 traces 更一致 → 独立性更差。\\\"更好的推理\\\"反而加剧 independence bottleneck。\\n\\n**κ 是 model-level 稳定属性**：统一处理后 Mistral 三 seed κ 收敛至 0.457-0.460（之前 0.41-0.50 差异是非标准 answer 处理的 artifact）。κ 跨 seed 几乎相同，但 delta 差异大（+3.43 vs +2.94 vs 0.00）→ seed-level constraint quality variance 主导，非 κ。\\n\\n完整 κ 表（⚠️ D062: κ 将用 raw answers 重算，当前 unified 值为临时值。Qwen 无变化，Mistral 条件将更新）：\\n| Exp | Model | κ(unified→raw pending) | Eff-K | SC%(registry) | Δpp(registry) |\\n|-----|-------|------------|-------|---------------|---------------|\\n| exp-028b | Qwen3-14B thinking | 0.913 | 1.09 | ~84% | ~0 |\\n| exp-038 | Qwen-14B LogiQA | 0.821 | 1.20 | 78.50 | -0.50 |\\n| exp-027 | Qwen3-14B | 0.773 | 1.26 | 84.31 | +0.49 |\\n| exp-036 | Qwen2.5-14B | 0.744 | 1.31 | 75.49 | +0.25 |\\n| exp-035 | Qwen2.5-7B | 0.658 | 1.46 | 76.47 | -0.49 |\\n| exp-049b | Mistral-7B LogiQA | 0.512 | 1.81 | 51.00 | +0.50 |\\n| exp-057 | Mistral-7B T=0.3 | 0.502 | 1.84 | 58.33 | -1.47 |\\n| exp-058 | Mistral-7B T=0.5 | 0.516 | 1.80 | 58.33 | -0.98 |\\n| exp-033 | Mistral-7B s42 | 0.460 | 1.98 | 55.88 | +3.43 |\\n| exp-052 | Mistral-7B s123 | 0.457 | 1.99 | 54.41 | +2.94 |\\n| exp-053 | Mistral-7B s456 | 0.457 | 1.99 | 55.88 | 0.00 |\\n| exp-055 | Mistral-7B multi-T | 0.427 | 2.11 | 57.84 | 0.00 |\\n| exp-054 | Mistral-7B T=1.0 | 0.394 | 2.25 | 55.39 | 0.00 |\\n| exp-046 | Mistral-7B PW-600 | 0.200 | 3.76 | 39.33 | -2.83 |\\n注：κ 基于 T/F/U 三类归一化，Mistral-7B 约 12-16% traces 被归一化（Qwen 100% valid）。Mistral SC/Δpp 已更新为 D064 tiebreaking 修正值；Qwen 不受影响。\\n\\nOracle control (+14.22pp) 证明 MAX-SAT 聚合机制本身有效，但自提取约束仅利用了 24% 的理论上限。Discriminative filtering 实验揭示关键机制：~92% 约束 ARE discriminative，但过滤掉 ~8% non-discriminative 约束后 delta 不变（0 gains）。问题不在约束缺乏判别力，而在于 discriminative constraints 的区分方向与模型偏差一致（confirmation bias）。\\n\\n**Remediation insight (D060)**: 9 种修复尝试全部失败，包括直接靶向 independence（multi-temp diversity, exp-055: Eff-K 从 2.0→2.11 但 delta 仍为 0）和 constraint quality（discriminative filtering）。这证明 bottleneck 不是简单的 diversity 或 quality 问题，而是 same-model self-extraction 的根本性限制。\\n\\n**Key evidence**:\\n- **Condorcet independence quantification (统一脚本, 公式: Eff-K=K/(1+(K-1)κ))**: Mistral-7B FOLIO κ≈0.46 (Eff-K≈2.0, 三 seed 高度稳定), Mistral-7B PW-600 κ=0.200 (Eff-K=3.76), Qwen2.5-14B FOLIO κ=0.744 (Eff-K=1.31), Qwen2.5-14B LogiQA κ=0.821 (Eff-K=1.20), Qwen3-14B κ=0.773 (Eff-K=1.26), Qwen2.5-7B κ=0.658 (Eff-K=1.46). 跨模型清晰: Qwen Eff-K≈1.2-1.5→0 gain, Mistral FOLIO Eff-K≈2.0→variable gain, Mistral PW Eff-K=3.76 but SC too low→negative. κ stable across seeds (0.457-0.460), delta varies → seed-level constraint quality dominates.\\n- **Oracle control (exp-031)**: Gold FOL + MAX-SAT = 89.71% vs SC 75.49% (+14.22pp, p=2.0e-7). Unknown-type +31.9pp.\\n- **Two-layer constraint analysis**: 43% trivially_satisfied (taxonomy: satisfied by ALL answers) vs ~8% non-discriminative (filtering: same MAX-SAT score). Difference: trivially_satisfied constraints can still have different satisfaction DEGREES. Removing the 8% yields 0 gains → problem is not quality but confirmation bias direction.\\n- **K sensitivity (non-monotonic peak at K=12, 5/5 complete, D064+D066)**: K=4(-1.47pp), K=8(-1.96pp), K=12(+3.43pp p=0.092 ns), K=16(+1.47pp), K=20(+1.96pp). Peak at K=12, drops at K=16 but partially recovers at K=20. NOT clean inverted-U. K=12 SC=55.88% (post-fix). SC-confound with T sensitivity still holds. SICA at K=4 vs K=12 differs by ~4.9pp despite similar SC — proves SICA extracts different information than SC.\\n- **SC-confound (cross-cutting insight)**: K=12 和 T=0.7 都是 SC 最低 (54.41%) 的配置 → SICA \\\"最佳超参\\\"可能反映 entropy/operating-window 效应而非 K 或 T 的因果贡献。论文需要讨论这个 confound，但也可以正面利用：SC level 是更基本的预测变量，K 和 T 通过影响 SC 来间接影响 SICA delta。\\n- **T sensitivity (isolated peak, 4/4 complete, D064 corrected)**: T=0.3(Δ=-1.47pp), T=0.5(Δ=-0.98pp), T=0.7(Δ=+3.43pp p=0.092 ns), T=1.0(Δ=0.00pp). NOT smooth inverted-U — T=0.7 is an isolated spike. T=0.7 has lowest SC (55.88%) → highest entropy → largest SICA operating window. Temperature and SC effects confounded. Strengthens fragility narrative.\\n- **Regime boundary**: Qwen-14B (SC=75.49%) Δ=-0.98pp vs Mistral-7B (SC=55.88%) Δ=+3.43pp p=0.092 ns\\n- **Type C failure (exp-046)**: Mistral PW-D5 SC=39.33%, Δ=-2.83pp, p=0.010, κ=0.210, Eff-K=3.63, contradiction rate 5.5%. Highest Eff-K yet worst delta → independence alone insufficient when SC too low.\\n- **Seed replication (D064+D066)**: 2/3 seeds positive but **0/3 significant** after tiebreaking correction: s42 Δ=+3.43pp p=0.092, s123 Δ=+2.94pp p=0.070, s456 Δ=0.00pp p=1.0. Mean +2.12pp. Only significant McNemar effects are NEGATIVE: exp-046 Δ=-2.83pp p=0.014, exp-039 Δ=-2.50pp p=0.011. Paper must frame as \\\"positive directional trend\\\" not \\\"significant positive effect\\\".\\n- **Nine remediation failures (ALL CONFIRMED)**: contrastive prompting, cross-model, generational scaling, solver-guided, consistency filtering, cross-trace UNSAT, discriminative filtering (0 gains), T=1.0 (delta collapse +3.43→0.00pp, D064 corrected), multi-temp (delta=+0.00pp, b=5 c=5). All 9 failed → trap is fundamental, bottleneck is structural.\\n- **Entropy decomposition (VERIFIED 2026-05-19)**: High-entropy proportion: Mistral FOLIO 38% (78/204) vs Qwen FOLIO 18% (37/204) vs Qwen LogiQA 12% (23/200). SICA on high-entropy: Mistral FOLIO s42 +12.8pp, s123 +9.1pp, s456 -1.3pp; Qwen FOLIO -8.2pp; all others negative. Low-entropy: SICA≈SC across all 8 experiments (Δ≈0). Entropy decomposition reveals regime-dependent mechanism, NOT universal diagnostic.\\n- **Confirmation bias quantification**: ⚠️ \\\"62.3%\\\" and \\\"28.6%\\\" confirmed NOT present in any .tex file — likely hallucinated in earlier draft. DO NOT USE. Replace with verified metrics from experiment outputs only.\\n\\n## Story Spine (D059 Updated)\\n\\n- **Problem**: LLMs' reasoning can be improved by sampling multiple chains-of-thought and aggregating via majority voting (self-consistency). Recent work proposes symbolic augmentation: extract formal constraints from traces and use SAT solvers for answer selection. But does symbolic aggregation actually outperform simple voting?\\n- **Theoretical lens**: Condorcet Jury Theorem requires voter independence. We quantify trace independence via Fleiss' κ and show Effective-K << nominal K. This explains the fundamental limitation of same-model trace aggregation.\\n- **Systematic evaluation**: SICA (MAX-SAT over FOL constraints) across 3 domains × 5 model families. Oracle control separates extraction vs aggregation failure. Discriminative filtering reveals ~92% constraints are discriminative, yet SICA gains are fragile — confirmation bias, not constraint quality, is the bottleneck.\\n- **Regime characterization**: Three failure modes (Type A/B/C) + narrow Goldilocks zone. C0+SC as deployment diagnostic.\\n- **Remediation failures strengthen thesis**: 9 targeted interventions (prompting, architecture, capability, verification, diversity, filtering) all fail to close the oracle gap, proving the bottleneck is fundamental to same-model self-extraction.\\n- **Headline result (D066 McNemar corrected)**: \\\"Across 6 models and 4 domains, symbolic consensus aggregation shows no statistically significant positive effect under corrected tiebreaking (best seed +3.43pp, p=0.092). The only significant effects are negative (PW-600: -2.83pp p=0.014, -2.50pp p=0.011). However, entropy decomposition reveals a striking regime-dependent pattern: SICA's entire effect concentrates on high-entropy questions, with +12.8pp in the Goldilocks zone but -2 to -8pp elsewhere. Oracle constraints prove the aggregation mechanism works (+14.22pp, p<0.001), localizing the bottleneck to extraction quality (24% utilization). Condorcet analysis (Eff-K=1.2-2.0 for nominal K=12) explains trace non-independence. Nine remediation strategies all fail, confirming the bottleneck is structural to same-model self-extraction.\\\"\\n\\n## Anticipated Reviewer Concerns & Defensive Experiments\\n\\n1. **\\\"Gains not statistically significant\\\"** → Correct: no positive effect reaches significance (best p=0.092). This IS the finding. Oracle p=2.0e-7 proves the mechanism works; the insignificance of self-extraction gains demonstrates the extraction bottleneck. Regime pattern (8 entropy conditions) provides systematic evidence beyond any single p-value.\\n2. **\\\"Only one positive result (exp-033)\\\"** → Seed replication: 2/3 positive (s42 +3.43pp, s123 +2.94pp), 1/3 null (s456 0.00pp). Mean +2.12pp. Effect IS real but fragile — the fragility itself IS the finding.\\n3. **\\\"Condorcet framework is trivial\\\"** → Fleiss' κ quantification is novel in SC/SICA context. Eff-K is actionable: tells practitioners how many truly independent traces they get.\\n4. **\\\"Multi-temp / filtering should work\\\"** → We tried both. Multi-temp (exp-055): negative. Disc. filtering: 0 gains. T=1.0: delta collapse. These failures STRENGTHEN the structural bottleneck thesis.\\n5. **\\\"Only Qwen models\\\"** → 5 families: Qwen-14B, Mistral-7B, LLaMA-8B, DeepSeek-R1-7B, QwQ-32B.\\n6. **\\\"Only logic domain\\\"** → FOLIO + ProofWriter + LogiQA + StrategyQA + ARC-Challenge. Type B (domain formalizability) is itself a finding.\\n7. **\\\"Oracle is unfair comparison\\\"** → Diagnostic tool, not competing method. Separates extraction from aggregation.\\n8. **\\\"MAX-SAT is over-engineering\\\"** → exp-013: MaxSAT ≈ count-only. This IS the independence bottleneck evidence.\\n9. **\\\"Self-extraction confound\\\"** → Oracle control resolves completely.\\n10. **\\\"Published methods achieve gains (DyLoS, Aristotle, FoVer)\\\"** → Different paradigm (external verifiers/trained extractors). We characterize same-model self-extraction.\\n11. **\\\"C0 is trivially derived\\\"** → Zero-cost early stopping. Practical value.\\n12. **\\\"Why not just use a reasoning model?\\\"** → QwQ-32B: C0<5%, SICA≡SC.\\n13. **\\\"Random tiebreak baseline\\\"** → exp-003: SICA tiebreak 80% vs random 50%.\\n14. **\\\"Method improvement is incremental\\\"** → Grounded in diagnosis (independence + taxonomy), not ad-hoc.\\n15. **\\\"Weighted SC is simpler\\\"** → exp-016 planned. Weighted SC doesn't address independence.\\n16. **\\\"Within-model ICL transition contradicts regime theory\\\"** → exp-050b (SC=57.79%, Δ=-3.52pp): ICL changes trace generation characteristics, not just SC level. Paper must distinguish \\\"same model, different prompt\\\" from \\\"same model, same prompt, different accuracy.\\\"\\n\\n## Working Title (D092 V3 — G+R dual method)\\n**\\\"Breaking Symbolic Confirmation Bias: Constraint-Answer Decoupling and Cross-Architecture Verification for LLM Logical Reasoning\\\"**\\n(Alternatives:\\n- \\\"Two Cures for One Disease: Decoupling and Architectural Diversity Against Symbolic Confirmation Bias in LLM Reasoning\\\"\\n- \\\"The Independence Bottleneck in Symbolic LLM Reasoning: Diagnosis, 25+ Failed Interventions, and Two Independent Solutions\\\"\\n- V2 fallback (R only): \\\"Breaking the Self-Consistency Ceiling: How Cross-Architecture Verification Overcomes Symbolic Confirmation Bias in LLM Reasoning\\\"\\n- V1 fallback (pure negative): \\\"Beyond Self-Consistency: How Trace Independence Limits Symbolic Consensus in LLM Reasoning\\\")\\n\\nNOTE (Dream D037): Title MUST be scoped to \\\"self-extracted constraints\\\" / \\\"SICA\\\". Published methods (DyLoS, Aristotle, FoVer) use different approaches.\\n\\n## Paper Structure (D092 V3 — EMNLP 8pp + appendix)\\n\\n### Sections\\n- §1 Introduction: 25+ same-model interventions all fail → independence bottleneck → two independent cures\\n- §2 Related Work: SC, neuro-symbolic, Condorcet/voting, verification\\n- §3 Diagnostic Framework: Independence Bottleneck (Eff-K, process-κ), Oracle Gap\\n- §4 Symbolic Confirmation Bias: bias ratio 4.97×, overlap 94%, causal chain\\n- §5 Method 1: Constraint-Answer Decoupling (G) — core method, detailed\\n- §6 Method 2: Cross-Architecture NLI Verification (R) — complementary method\\n- §7 Combined Analysis: G+R combo, ablation, cross-dataset if available\\n- §8 Discussion + Conclusion\\n\\n### Main Tables\\n- T1: Main Results — models × domains, SC% / SICA% / Δpp / p-value, regime boundary\\n- T2: Oracle Control — Gold-FOL+MAX-SAT vs SC vs SICA-self, causal separation\\n- T3: Independence Quantification — Fleiss' κ / Eff-K / trace agreement per model\\n- T4: Confirmation Bias — bias ratio per condition, overlap rate, per-label breakdown\\n- T5: Decoupling Results (G) — SC / SICA / G-Decoupled, Δpp, McNemar, per-label\\n- T6: NLI Verification Results (R) — SC / NLI standalone / combo w=1,3 / intersection, Δpp, McNemar\\n- T7: 25+ Intervention Summary — method / type / dataset / result / failure mode (compact)\\n\\n### Main Tables (continued)\\n- T6: Method-Level Intervention Results — 3 methods × 2 datasets, SC% / Method% / Δpp, failure mode classification\\n- T7: κ Generalization — SC / Debate / Diverse-Prompt κ and Eff-K (from exp-077, pending)\\n\\n### Main Figures\\n- F1: Method Pipeline (SICA + oracle control design)\\n- F2: SC Accuracy vs SICA Δ scatter (hero figure, regime boundary)\\n- F3: K Sensitivity with diversity metrics (K vs Δ, K vs Eff-K)\\n- F4: Extraction error breakdown (stacked bar)\\n- F5: Method intervention failure modes (grouped bar: ICG/Contrastive/Debate × FOLIO/LogiQA)\\n\\n### Appendix\\n- K ablation details, temperature sensitivity, per-domain results, overhead analysis\\n- Entropy-conditioned analysis (continuous scatter + bin sensitivity)\\n- Six remediation strategy details\\n- Confirmation bias quantification\\n- Seed replication analysis\\n- QwQ-32B / DeepSeek-R1 negative control\\n\\n## Claim Risk Notes (D059)\\n- **Seed replication**: 0/3 significant after D066 correction (p=0.092, 0.070, 1.0). 2/3 positive trend, 1/3 null. Mean +2.12pp. Frame as \\\"directional trend, not significant effect\\\" — fragility IS the finding.\\n- **Method claims DEAD (D060)**: All three method improvements failed. Paper is pure analysis. 9 remediation failures are EVIDENCE, not limitation.\\n- **Condorcet novelty**: ✅ VERIFIED. arXiv:2409.00094 applies CJT to cross-model LLM ensembles (different angle). No prior work applies Fleiss' κ or Eff-K to within-model SC traces. Our framing is novel.\\n- **exp-050b complication**: ICL transition Δ=-3.52pp at SC=57.79% complicates simple \\\"SC determines SICA.\\\" Explain via trace generation characteristic change.\\n- **Variable naming inconsistency**: 56.4% cross-trace pairs share zero Z3 variables. Key mechanism evidence.\\n\\n## Required Citations (minimum 30 references)\\n\\n- **SC & extensions**: Wang et al. 2023 (SC), Chen et al. 2023 (USC), Loo et al. 2025 (SC scaling plateaus), Taubenfeld et al. 2025 (weighted SC), DiVeRSe (Li et al. 2023)\\n- **Neuro-symbolic reasoning**: DyLoS (EACL 2026), Aristotle (ACL 2025), FoVer (TACL 2025), LogicAgent (2025), Logic-LM (Pan et al. 2023), LINC (Olausson et al. 2023)\\n- **Condorcet/voting theory**: Condorcet 1785, Austen-Smith & Banks 1996, **arXiv:2409.00094 (Examining Independence in Ensemble Sentiment Analysis, Sept 2024)** — closest prior work, applies CJT to cross-model LLM ensembles, finds independence violation. Our novelty: within-model trace independence + Fleiss' κ quantification + Eff-K + connection to symbolic aggregation\\n- **Test-time compute**: Snell et al. 2025, DeepSeek-R1, Diversity-Aware Training\\n- **Verification & reranking**: ORM (Cobbe et al. 2021), PRM (Lightman et al. 2023), Math-Shepherd\\n- **Constraint satisfaction**: SATBench (EMNLP 2025), LLM Meets Constraint Propagation (IJCAI 2025)\\n- **Debate & multi-agent**: Liang et al. 2023, Du et al. 2023\\n\\n## Additional Reviewer Concerns (D070/D074 Methods)\\n\\n17. **\\\"Why not use a larger model for constraint generation?\\\"** → Valid. All methods tested at 7B scale. ICG constraint parsing failures + Debate role-play degradation may be scale-dependent. This is explicitly noted as limitation and future work. The contribution is diagnosing the bottleneck and showing it's not trivially fixable, not claiming no fix exists at any scale.\\n18. **\\\"Only tested one model (Mistral-7B) for methods\\\"** → Methods are interventions on the extraction pipeline, not the base model. Testing on the same model that showed the clearest Goldilocks signal (Mistral-7B FOLIO) is the strongest test — if methods can't improve the best-case scenario, they won't help elsewhere.\\n19. **\\\"ICG multi-seed shows 1/3 positive\\\"** → Magnitudes (-2.0, +1.5, -1.0) are within SC baseline noise (3.5pp cross-seed). Mean ≈-0.5pp, std=1.8pp. No statistical significance. Properly framed as \\\"noise-level, neither improving nor degrading.\\\"\\n20. **\\\"Debate working in other papers\\\"** → Multi-agent debate literature uses diverse models or much larger models. Same-model 7B debate is a different regime. Our finding is specifically about same-model self-extraction limitations.\\n\\n## Claim Scoping Rules\\n- n=60 conditions: \\\"suggestive/consistent with\\\" NOT \\\"confirming\\\"\\n- n≥200 conditions: can \\\"confirm\\\"\\n- Combined N>1,300: acceptable if breakdown clearly stated\\n- Method claims: must show statistically significant improvement OR clear directional improvement with analysis\\n- \\\"Independence bottleneck\\\" framing: systematic quantification + theoretical grounding\\n\\n## V16 Frontier Model Extension (D135–D139)\\n\\n### New Claim 11: SCB is Universal — 7B to Frontier (D135)\\n\\nSymbolic Confirmation Bias persists across ALL tested models, from 7B open-source to frontier closed-source:\\n\\n| Model | Extraction | SC% | SICA% | Δpp | BR(mean) | BR=∞ rate | Process-κ | Answer-κ |\\n|-------|-----------|-----|-------|-----|----------|-----------|-----------|----------|\\n| Mistral-7B | self | 55.88 | 59.31 | +3.43 | 4.97 | 30% | 0.69* | 0.46 |\\n| LLaMA-8B | self | — | — | — | 2.88 | — | — | — |\\n| Qwen-14B | self | 75.49 | 75.74 | +0.25 | 3.93 | — | — | 0.74 |\\n| R1-Distill-8B | cross→Mistral | 74.51 | 76.96 | +2.45 | 2.92 | — | 0.248 | 0.69 |\\n| gpt-4o | self | 73.91 | 72.05 | -1.86 | 2.94 | 44% | 0.79 | 0.80 |\\n| gpt-4.1 | cross→Mistral | 82.84 | 81.37 | -1.47 | 2.70 | 58% | 0.792 | 0.86 |\\n| gpt-5.5 | cross→Mistral | 84.31 | 84.80 | +0.49(n.s.) | 3.48 | 87% | 0.563 | 0.96 |\\n| o3 | cross→Mistral | 82.65 | 82.65 | 0.00 | 1.66 | 82% | 0.596 | 0.92 |\\n| Gemini-2.5-Pro* | cross→Mistral | 87.37 | 86.32 | -1.05 | 2.79 | — | 0.790 | 0.75 |\\n\\n*Gemini: 95/204 interim. Mistral Process-κ is CoT cosine sim (different metric from cross-model TF-IDF κ).\\n\\nBR > 1 across ALL models (1.66–4.97×). BR=∞ rates high in frontier models (44–87%).\\nTable footnote MUST distinguish self vs cross extraction context.\\n\\n### New Claim 12: Process-κ Gradient Predicts Cross-Model Extraction Effectiveness (D137–D139)\\n\\nCross-model extraction (Mistral-7B extracts FOL from other models' traces) effectiveness is monotonically predicted by Process-κ:\\n\\n| Model | Process-κ | Δ(SICA-SC) | BR(mean) |\\n|-------|-----------|------------|----------|\\n| R1-Distill | 0.248 | +2.45pp ✓ | 2.92 |\\n| gpt-5.5 | 0.563 | +0.49pp(n.s.) | 3.48 |\\n| o3 | 0.596 | 0.00pp | 1.66 |\\n| Gemini-2.5-Pro* | 0.790 | -1.05pp | 2.79 |\\n| gpt-4.1 | 0.792 | -1.47pp | 2.70 |\\n\\n**Spearman ρ(κ→Δ) = -1.0, n=5, one-tailed p=0.0083** (statistically significant).\\n\\n**Paper language constraints (D138)**:\\n- Use \\\"decreases monotonically\\\" — NOT \\\"predictive\\\" or \\\"significant correlation\\\"\\n- Dual-variable framing: \\\"two necessary conditions\\\" (qualitative mechanism), NOT regression model\\n  - Low κ (diverse traces) → cross-model extractor can contribute novel constraints\\n  - High BR (strong self-bias) → there IS bias to escape from\\n  - Both conditions required: o3 (BR=1.66, near-unbiased) → Δ=0 despite moderate κ=0.596\\n- o3 BR=1.66 is observation (\\\"bimodal error pattern: 82% BR=∞ but low finite-BR\\\"), NOT sub-finding\\n- BR=∞ ordering does NOT strictly follow \\\"model capability\\\" (o3 82% < gpt-5.5 87%). Drop ordering claim.\\n\\n### Updated Headline (V16)\\n\\n\\\"Symbolic Confirmation Bias is universal from 7B open-source to frontier closed-source models (BR 1.66–4.97×). Cross-model extraction effectiveness decreases monotonically with Process-κ (ρ=-1.0, n=5, p=0.008), modulated by bias severity: gain requires both diverse traces (low κ) AND substantial self-bias (high BR). 25+ same-model interventions fail; two cross-architecture cures succeed.\\\"\\n\\n### V16 Paper Structure Impact\\n\\n- §4 SCB: Add frontier model BR table (Table 4 or expanded T4)\\n- §3 or new §: Process-κ gradient analysis (Table + scatter plot)\\n- §1 Intro: Scale claim upgraded from \\\"7B-32B\\\" to \\\"7B to frontier\\\"\\n- Limitations: Update \\\"7B to 32B parameters\\\" scope claim\\n- New Figure: Process-κ vs Δ scatter with dual-variable annotation (5 points + regression-free narrative)\\n\", \"total_chars\": 40785, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "259e8c74-cee8-43ee-8c2a-b39b28aafca2",
  "uuid": "d21be4c9-f006-43b3-b57d-de3b76c4ca81",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"path\\\": \\\"/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/paper_framing.md\\\", \\\"content\\\": \\\"# Paper Framing — symb_invariant_consensus\\\\n\\\\n## Target Venue\\\\n- Primary: EMNLP 2026 Main (ARR May 25)\\\\n- Deadline: May 25, 2026 (ARR submission)\\\\n\\\\n## D063 Direction: Entropy Decomposition + Quality Ladder — 目标 4.0\\\\n\\\\n**从 D060 \\\\\\\"Pure Analysis / negative result\\\\\\\" 升级为 \\\\\\\"Regime-Dependent Mechanism Analysis with Entropy Decomposition\\\\\\\"。** 用户决定冲 4.0。\\\\n\\\\n### Entropy Breakdown 验证结果 (2026-05-19 completed)\\\\n\\\\n**跨模型 entropy mechanism 一致性: 不成立。Selective SICA 非 universal 方案。**\\\\n\\\\n但 entropy decomposition 揭示了更有价值的 regime mechanism：\\\\n\\\\n| Experiment | Model | Dataset | High-E n | High-E Δpp | Low-E n | Low-E Δpp |\\\\n|-----------|-------|---------|----------|-----------|---------|----------|\\\\n| exp-033 s42 | Mistral-7B | FOLIO | 78 | **+12.8** | 126 | 0.0 |\\\\n| exp-052 s123 | Mistral-7B | FOLIO | 77 | **+9.1** | 127 | 0.0 |\\\\n| exp-053 s456 | Mistral-7B | FOLIO | 75 | -1.3 | 129 | 0.0 |\\\\n| exp-046 | Mistral-7B | PW-600 | 267 | -4.9 | 333 | -1.2 |\\\\n| exp-036 | Qwen2.5-14B | FOLIO | 37 | **-8.2** | 167 | -0.6 |\\\\n| exp-038 | Qwen2.5-14B | LogiQA | 23 | -4.3 | 177 | 0.0 |\\\\n| exp-035 | Qwen2.5-7B | FOLIO | 47 | -2.1 | 157 | 0.0 |\\\\n| exp-048 | LLaMA-8B | PW-600 | 76 | -3.9 | 104 | -1.9 |\\\\n\\\\n(注: SC/Δ 使用 pre-tiebreaking 值，entropy grouping 不受 tiebreaking 影响。D064 修正后 deltas 会略有变化但 pattern 不变。)\\\\n\\\\n**三个核心发现：**\\\\n1. **Low-entropy: SICA≈SC 跨模型一致** (8/8 experiments Δ≈0) → traces 一致时 constraints 无新信息\\\\n2. **High-entropy 方向因 regime 而异**：Goldilocks +12.8pp vs Type A -8.2pp vs Type C -4.9pp\\\\n3. **Mechanism 解释**：\\\\n   - Goldilocks (SC~55%, κ~0.46): 真实不确定性 → constraints 打破平局正确方向\\\\n   - Type A (SC>75%, κ>0.65): 偶发错误 → constraints 放大 confirmation bias\\\\n   - Type C (SC<40%, κ~0.20): 系统性错误 → constraints 是噪声\\\\n\\\\n### 调整后核心转变\\\\n\\\\n论文以 \\\\\\\"entropy decomposition 揭示 regime-dependent mechanism\\\\\\\" 为核心分析贡献（不是 universal diagnostic）：\\\\n- **Entropy decomposition 作为分析工具**：分离 SICA 作用点（high-entropy）vs 不作用点（low-entropy）\\\\n- **Regime mechanism 量化**：同样是 high-entropy 问题，direction depends on SC+κ → 完美支持 dual bottleneck\\\\n- **Abandoned**: Selective SICA 作为 universal practical contribution（只在 Goldilocks zone 有效）\\\\n- **Upgraded**: 核心图 = high-entropy Δ vs SC scatter（8 points, 3 regimes 清晰分离）\\\\n- **Quality Ladder** (D067: L1 NULL CONFIRMED)\\\\n  - L0: Self-extraction (Mistral→Mistral): 59.31%, Δ=+3.43pp ns\\\\n  - L1a: Qwen3-14B→Mistral traces: 60.29%, Δ=+4.41pp (+0.98pp vs self = 2题/204 = noise)\\\\n  - L1b: Qwen2.5-14B→Mistral traces: 58.33%, Δ=+2.45pp (-0.98pp vs self = 2题/204 = noise)\\\\n  - L3: Oracle 100% disc, Δ=+14.22pp p<0.001\\\\n  - **结论**: L1 ≈ L0 << L3。Bottleneck 在 traces（同源输入），不在 extractor（换模型无效）\\\\n  - **Paper contribution**: \\\\\\\"bottleneck is fundamental to extraction, not just model capability\\\\\\\" — 强化 structural limitation 论点\\\\n- **CJT/Eff-K 保留**：解释 why high-entropy behavior differs across regimes\\\\n\\\\nD060 要素全部保留：\\\\n- Condorcet independence 框架 → 理论基础\\\\n- 9 种修复全部失败 → structural limitation 证据\\\\n- 2/3 seeds positive trend but **0/3 significant** (D066: p=0.092/0.070/1.0) → Goldilocks zone 作为 directional trend, not confirmed effect\\\\n- K/T sensitivity non-monotonic → SC confound insight\\\\n- 用户指示: 投 May 25 不变，冲 4.0\\\\n\\\\n## Core Claims (5 条) — D060 纯 Analysis Framing\\\\n\\\\n### Analysis Claims (已验证)\\\\n\\\\n1. **Independence Bottleneck**: Self-consistency 隐含 Condorcet Jury Theorem 的独立性假设，但同模型采样的 traces 高度相关。Worker 验证的 κ 值：\\\\n   - Qwen-14B FOLIO: κ=0.744, Eff-K=1.31 (SC=75.49%, Δ=+0.25pp n.s.)\\\\n   - Qwen-14B LogiQA: κ=0.821, Eff-K=1.20 (SC=78.5%, Δ=+0.50pp n.s.)\\\\n   - Mistral-7B FOLIO s42 (exp-033): κ=0.501, Eff-K=1.84 (SC=55.88%, Δ=+3.43pp **p=0.092 ns**) ← primary seed [D064+D066]\\\\n   - Mistral-7B FOLIO s123: κ=0.491, Eff-K=1.88 (SC=54.41%, Δ=+2.94pp **p=0.070 ns**)\\\\n   - Mistral-7B FOLIO s456: κ=0.507, Eff-K=1.82 (SC=55.88%, Δ=0.00pp p=1.0 ns)\\\\n   - Mistral-7B PW-600 (exp-046): κ=0.210, Eff-K=3.63 (Δ=-2.83pp p=0.010, SC=39%)\\\\n   规律：跨模型对比清晰（Qwen Eff-K≈1.2-1.3 → 0 gain; Mistral Eff-K≈1.85-2.22 → variable gain）。但 Mistral seeds 内部，Eff-K 与 delta 非单调（exp-033 Eff-K 最低 1.85 却 delta 最高 +3.43pp）→ Eff-K 是跨模型必要条件，seed 内 variance 仍主导。exp-046 Eff-K 最高(3.63) 但 SC 太低(39%) 导致 delta 为负 → 需同时满足 sufficient Eff-K AND sufficient SC。\\\\n\\\\n2. **Oracle Gap Localizes Extraction Bottleneck**: Gold FOL + MAX-SAT = +14.22pp (p=2.0e-7)，自提取仅 +3.43pp (best seed, D064 corrected) = 24% utilization。聚合机制本身有效，瓶颈在自提取质量。Two-layer analysis:\\\\n   - **Constraint taxonomy**: 43% trivially_satisfied（被所有候选答案满足的约束，不排除任何答案）\\\\n   - **Discriminative filtering**: 仅 ~8% 约束在 MAX-SAT scoring 中完全 non-discriminative（移除后 0 gains）\\\\n   - **关键区分**: 43% 和 8% 度量不同。trivially_satisfied 约束在 MAX-SAT 中仍可有不同满足程度（partial vs full），所以不全是 non-discriminative。但即使 constraints 是 discriminative 的，它们的\\\\\\\"区分方向\\\\\\\"与模型自身偏差一致（confirmation bias）。both_wrong 组 score_range=29.4。九种修复全部失败。\\\\n\\\\n3. **Regime-Dependent Capability Trap**: SICA 有效性取决于提取模型的基线准确率，存在双边界：\\\\n   - Type A (SC ≥ ~60%): 确认偏差，constraints 镜像模型自身答案。**exp-034 vs exp-039 同配置 delta 翻转**: exp-034 Δ=+0.51pp (n=589), exp-039 Δ=-2.00pp (n=600)。SC baseline 方差 (3.38pp) >> SICA 效应 → Type A delta 是 trace sampling noise。SICA 比 SC 更稳定 (跨运行方差 0.87pp vs 3.38pp，仅 2 点，需更多 seed 验证)\\\\n   - Type C (SC ≤ ~40%): traces 主要错误，constraints 是噪声 (exp-046: Δ=-2.83pp, p=0.0095)\\\\n   - Goldilocks zone (~50-56% SC): 部分独立性 + 部分正确性 (exp-033: Δ=+3.43pp, p=0.092 ns; mean of 3 seeds: +2.12pp) ⚠️ D076 Reviewer: 0/3 seeds significant, 不应作为核心叙事支柱。作为 directional observation 保留，不做强 claim。\\\\n   - Type B: 领域不可形式化 (LogiQA: contradiction rate 0.8%)\\\\n\\\\n4. **C0+SC Two-Dimensional Diagnostic**: C0 (multi-candidate rate) + SC accuracy 形成零成本部署诊断。C0<5% → degenerate; high C0 + high SC → trap; high C0 + low SC → potential gains。\\\\n\\\\n### Remediation Evidence (D060: 全部失败 — 强化 analysis narrative)\\\\n\\\\n5. **Nine Remediation Attempts All Failed**: 原 6 种 + 3 种靶向修复全部无效，证明 independence bottleneck 是结构性的：\\\\n   - D059 三路 method improvement 全部失败：\\\\n     - Discriminative Filtering: 119/204 处理后 0 gains 1 loss，~92% 约束本身就是 discriminative，过滤是 near-no-op\\\\n     - T=1.0 (exp-054): delta 从 +3.43pp 崩塌到 0.00pp（D064 corrected），温度敏感性极端\\\\n     - Multi-Temp (exp-055): ✅ 完成，delta=+0.00pp (b=5,c=5 完美对称), SC=57.84%. 混合 T=0.3/0.7/1.2 各 4 traces 未改善 SICA。附带发现：multi-temp 提升 SC baseline (+3.4pp vs 单温度 54.41%)，说明混合温度对 majority voting 有帮助，但 SICA constraint extraction 无法利用这种 diversity → bottleneck 在 extraction 而非 trace diversity\\\\n   - 原 6 种：contrastive prompting, cross-model extraction, generational scaling, solver-guided refinement, consistency filtering, cross-trace UNSAT\\\\n   - 9 种修复涵盖 prompting / architecture / capability / verification / diversity / filtering 全维度，全部失败 → trap is fundamental\\\\n\\\\n## D070/D074 Update: Method-Level Interventions Also Fail — \\\\\\\"Fundamental Limitation\\\\\\\" Confirmed\\\\n\\\\n### Three Method Lines × Two Datasets = All Negative (D074)\\\\n\\\\nD070 从纯 analysis 升级为 analysis + method paper，但三条方法线全面失败（D074 确认），反而强化了原始 analysis 结论。\\\\n\\\\n**方法×数据集完整结果**：\\\\n| Method | FOLIO-204 | LogiQA-200 | Failure Mode |\\\\n|--------|-----------|------------|--------------|\\\\n| ICG (Independent Constraint Gen.) | Δ=-2.0pp (3-seed: -2.0/+1.5/-1.0, mean=-0.5pp±1.8pp, 噪声) | Δ=-0.5pp | Neutral — 独立约束质量≈trace-sourced约束 |\\\\n| Contrastive (Pro/Con Scoring) | Δ≈-16pp | Δ≈-7pp (interim) | Harmful — 26% degenerate scoring, pro/con 不平衡 |\\\\n| Debate (Proposer/Critic) | Δ=-18.6pp | Δ≈-28pp (interim) | Catastrophic — 7B 模型角色扮演严重退化推理 |\\\\n\\\\n**三种失败模式的分析价值**（论文 \\\\\\\"Why Methods Fail\\\\\\\" section）：\\\\n1. **ICG (neutral)**: 独立于 traces 生成的约束不比 trace-sourced 约束更好。说明 bottleneck 不仅是 \\\\\\\"约束来自 traces\\\\\\\"，而是模型的推理偏差从问题理解阶段就存在——独立约束和 trace-sourced 约束继承相同的 model bias。\\\\n2. **Contrastive (harmful)**: 强制 pro/con 评估引入 degenerate scoring（26% 问题无法有效区分）。7B 模型无法可靠生成平衡的对立约束——pro 约束系统性多于 con（94 pro vs 65 con），confirmation bias 从约束提取转移到了约束生成。\\\\n3. **Debate (catastrophic)**: Proposer/Critic/Defense 多角色链在 7B 模型上导致答案质量严重退化。辩论不仅未增加多样性，反而引入了角色扮演的额外认知负担。同模型辩论 = 同源性 + 角色扮演退化，双重损失。\\\\n\\\\n**Scale limitation caveat**: 所有方法测试在 7B 模型上。7B 模型生成 Z3 格式 FOL 约束的能力不足（ICG 多题 \\\\\\\"0/N constraints parsed\\\\\\\"）。14B+ 模型可能有不同结果——这既是 limitation 也是 future work 入口。\\\\n\\\\n### κ Generalization — Independence-Accuracy Trade-off (D075, CAPSTONE FINDING)\\\\n\\\\nexp-077 测量三种聚合方式在 Mistral-7B FOLIO-204 上的 κ 和 Eff-K：\\\\n| 聚合方式 | Fleiss' κ | Eff-K | 名义 K |\\\\n|----------|----------|-------|--------|\\\\n| Self-Consistency | 0.4384 | 2.02 | 10 |\\\\n| Diverse-Prompt | 0.4030 | 2.21 | 12 |\\\\n| LLM-Debate | 0.1549 | 4.44 | 12 |\\\\n\\\\n结合 exp-076 Debate Δ=-18.6pp 的准确率数据，揭示**同模型框架下的 fundamental independence-accuracy trade-off**：\\\\n- **SC/Diverse-Prompt**: κ~0.4，traces 高度相关但准确率正常。换 prompt 策略不改善独立性（Δκ=0.04）。\\\\n- **Debate**: κ=0.15，成功打破 trace 相关性（Eff-K 从 2.0 跃升到 4.4），但准确率崩溃 -18.6pp。低 κ 不代表\\\\\\\"更独立的推理\\\\\\\"——是 disagreement amplification（系统性噪声）。\\\\n- **Trade-off 本质**: 同一模型的推理能力是固定的。要么输出一致（高 κ, 正确但不独立），要么输出分歧（低 κ, 独立但不正确）。Condorcet Jury Theorem 要求 both independent AND accurate，同模型框架下无法同时满足。\\\\n\\\\n**论文叙事升级**: 从 \\\\\\\"methods fail\\\\\\\" → \\\\\\\"independence-accuracy trade-off is fundamental to same-model reasoning\\\\\\\"。突破瓶颈需要跨模型方案（不同模型天然更独立），Oracle 实验（gold FOL 来自外部知识源）已间接验证了这一点。\\\\n\\\\n### New Claim 6 (D070/D074)\\\\n\\\\n6. **Method-Level Interventions Cannot Break the Bottleneck**: 三种针对 independence bottleneck 不同环节的方法（ICG→循环依赖, Contrastive→confirmation bias, Debate→trace 同质性）在 2 个数据集上全部失败。加上之前 9 种 prompt-level 修复，共 12 种修复尝试全败。这证明 independence bottleneck 不是单一环节的问题，而是 same-model self-extraction 的根本性限制。\\\\n\\\\n### New Claim 7: Symbolic Confirmation Bias (D082 — CORE FINDING)\\\\n\\\\n7. **Symbolic Confirmation Bias**: LLM 从 CoT traces 提取的 FOL 约束系统性确认 trace 自身（可能错误的）答案，而非独立验证 ground truth。\\\\n   - SICA 判对题：gold constraint 78.1%，bias ratio = 0.28\\\\n   - SICA 判错题：错误 constraint 83.3%，bias ratio = **4.97×**\\\\n   - 97.6% SICA 错误与 SC 错误完全重合\\\\n   - SICA 翻盘的 12 例来自 minority trace diversity（43% gold support），不是 symbolic reasoning\\\\n   - **因果链**：模型推理→答案→从含答案 trace 提取 FOL→约束确认答案→聚合≈SC\\\\n   - **CEGIS 验证**：迭代精炼 R1 +3.43pp < 原始 SICA +4.9pp → 约束一致性不是瓶颈，偏向性才是\\\\n   - **Quality Ladder 验证**：L1 ≈ L0 << L3 → bottleneck 在 traces（同源输入），不在 extractor\\\\n\\\\n### New Claim 8: Process-κ (D082 — NEW METRIC)\\\\n\\\\n8. **Process-Level Independence (Process-κ)**: answer-κ 低估真实独立性瓶颈。CoT 推理过程相似性远高于答案一致性。\\\\n   - Mistral-7B FOLIO-204：CoT cosine similarity **0.69** >> answer-κ **0.41**\\\\n   - 两者几乎无相关性：r = -0.06, p = 0.36\\\\n   - 仅 **9.3%** trace 对是\\\\\\\"殊途同归\\\\\\\"（同答案不同路径）\\\\n   - answer-κ 是 true independence bottleneck 的 lower bound\\\\n   - 适用于所有 LLM trace aggregation 方法，不限于 SICA\\\\n\\\\n## D082/D085: Comprehensive Method Exhaustion — 25+ ALL Fail\\\\n\\\\nD080 启动全方向并行探索（Wave 1-3），在 D074 的 12 种修复基础上又测试 13+ 新干预：\\\\n\\\\n| 方法 | 类型 | 结果 | 关键数据 |\\\\n|------|------|------|----------|\\\\n| PROVE 代码验证 | paradigm shift | ❌ | Code gen 15.2%, accuracy=random |\\\\n| CEGIS 迭代精炼 | multi-round | ❌ | R1 +3.43pp < SICA +4.9pp |\\\\n| DeepConf 置信度 | filtering | ❌ | logprob 与正确性零相关 |\\\\n| Cross-model SICA | cross-model | ❌ | Δ=-0.49pp despite lower κ |\\\\n| Problem Perturbation | input diversity | ❌ | κ 升至 0.696 (反效果) |\\\\n| MIN-UNSAT | solver objective | ❌ | 49.5% < SC 54.4% |\\\\n| κ-aware SC | voting rule | ❌ | 11/11 Δ=0 |\\\\n| Z3 Trace Filter | trace filtering | ❌ | negative |\\\\n| Bootstrapped Gold | iterative | ❌ | negative |\\\\n| Selective Abstention | diagnostic | ⚡ | AUROC=0.673, +4.4pp@80%cov |\\\\n\\\\n**D085 总结**: 9 prompt-level + 3 method-level + 13 新方向 = **25+ 干预全部 negative**。Independence bottleneck 在 same-model self-extraction 框架下无解，所有维度（diversity/architecture/capability/verification/filtering/voting/solver/paradigm）已穷尽。\\\\n\\\\n## D090: Cross-Architecture External Verification — POSITIVE BREAKTHROUGH\\\\n\\\\n### New Claim 9: Cross-Architecture NLI Verification Breaks the Bottleneck\\\\n\\\\n9. **Cross-Architecture External Verification**: A lightweight encoder-only NLI model (microsoft/deberta-large-mnli) provides structurally complementary signal to decoder-only LLMs.\\\\n   - DeBERTa standalone: 49.51% (101/204) — not competitive alone, expected\\\\n   - **NLI+SC combo w=1 (NLI as 13th voter): 57.84% (118/204), +3.43pp vs SC** ← PRIMARY (has McNemar)\\\\n   - NLI+SC combo w=3: 58.82% (120/204), +4.41pp vs SC — McNemar p=0.078 NOT significant (b=6, c=15). Higher weight amplifies NLI weakness on Unknown.\\\\n   - NLI+SC combo w=5: 60.29% (+5.88pp) — Reviewer: w=5 overfitting risk, NOT main result\\\\n   - NLI∩SC agreement subset: 68.48% accuracy on 45% coverage — selective verification evidence\\\\n   - NLI-as-verifier (trust NLI on disagreement): 49.51% — FAILED (NLI only 34% correct when disagreeing)\\\\n   - SC baseline: 54.41% (111/204, primary Mistral-7B FOLIO eval, seed=None)\\\\n   - **McNemar (w=1 ONLY)**: p=0.039, significant at α=0.05. 9 discordant pairs (b=1, c=8). 95% CI [0.59pp, 6.28pp]. ⚠️ w=3 and w=5 McNemar NOT YET COMPUTED — do NOT attribute this p-value to other weights\\\\n   - **Model**: microsoft/deberta-large-mnli, **406M** parameters (not 350M, not 44M)\\\\n   - **Per-label complementarity (key insight)**:\\\\n     - False (contradiction): NLI **71.43%** vs SC 38.10% → NLI dominates (+33pp)\\\\n     - Unknown: NLI 18.84% vs SC **68.12%** → SC dominates (+49pp)\\\\n     - True: NLI 59.72% vs SC 55.56% → NLI slightly better\\\\n   - **Why it works**: DeBERTa is encoder-only + NLI fine-tuned → strong at contradiction detection (its training task). LLM is strong at uncertainty reasoning. Structurally complementary error profiles.\\\\n   - **Oracle connection**: Oracle (+14.22pp) proved aggregation works with quality constraints; DeBERTa provides partial external signal → partial oracle effect\\\\n   - **Narrative**: \\\\\\\"25+ same-model interventions fail, but even a simple cross-architecture voter provides modest positive signal — proof-of-concept for external architectural complementarity\\\\\\\"\\\\n\\\\n### New Claim 10: Constraint-Answer Decoupling — CONDITIONAL on full results (D092)\\\\n\\\\n10. **Constraint-Answer Decoupling (G)**: Removing conclusion sentences from reasoning traces before FOL extraction causally breaks Symbolic Confirmation Bias.\\\\n   - **⚠️ INTERMEDIATE results only (70/204 = 34%)**: 65.7% accuracy (+11.3pp vs SC 54.41%, +6.4pp vs SICA 59.31%)\\\\n   - Avg truncation ratio: **4.1%** — removing ~4% of trace text yields +11pp improvement\\\\n   - **Causal mechanism**: trace contains conclusion → FOL extractor reads conclusion → extracted constraints confirm conclusion → aggregation ≈ SC. G cuts this chain by removing the conclusion before extraction.\\\\n   - **Potential strengths**: (a) largest positive effect in the project, (b) minimal intervention (4.1% text removal), (c) directly tests the confirmed mechanism (confirmation bias)\\\\n   - **Risk (Reviewer critical)**: FOLIO 难度分布不均匀，前 70 题可能偏简单。历史先例：Direction F 42%→39.6%，Direction H 56.1%→微降。中间值可能虚高。\\\\n   - **Residual bias risk**: 即使截断显式结论，推理步骤仍可能暗示答案方向（\\\\\\\"the premises suggest...\\\\\\\"），extraction 模型仍可能产生 biased constraints。\\\\n   - **Full results pending**: PID 384984 on westd-16639, running to 204/204\\\\n   - **McNemar**: pending full results\\\\n   - **Narrative (if confirmed)**: \\\\\\\"25+ methods fail because they don't break the answer→constraint coupling. G directly severs this coupling via conclusion truncation — the diagnosis drives the fix.\\\\\\\"\\\\n\\\\n### Framing Decision Threshold (Reviewer-approved)\\\\n- G ≥+5pp AND p<0.05 → **commit V3** (G+R dual method, G as core)\\\\n- G +3-5pp AND p<0.10 → **V3 weak** (G as \\\\\\\"encouraging pilot\\\\\\\", not core method)\\\\n- G <+3pp OR n.s. → **fall back to V2** (R proof-of-concept) or **V1** (pure negative)\\\\n\\\\n### Updated Headline Result (D092 — V3 CONDITIONAL, awaiting G full results)\\\\n\\\\n\\\\\\\"Across 6+ models and 4 domains, symbolic consensus aggregation shows no statistically significant positive effect under same-model self-extraction. 25+ interventions fail. Root cause: Symbolic Confirmation Bias (4.97×). Two independent cures both succeed: (1) Constraint-Answer Decoupling removes conclusion sentences before FOL extraction, cutting the causal chain — +11.3pp (70/204 intermediate, PENDING FULL); (2) Cross-architecture NLI verification (DeBERTa) provides structurally complementary signal — +4.41pp (p=0.039). Both validate the diagnosis from orthogonal angles: G attacks the information flow, R attacks the architectural homogeneity.\\\\\\\"\\\\n\\\\n### Updated Headline Result (D090 — V2 FALLBACK, if G full results weaker than intermediate)\\\\n\\\\n\\\\\\\"Across 6+ models and 4 domains, symbolic consensus aggregation shows no statistically significant positive effect under same-model self-extraction. 25+ interventions fail. Root cause: Symbolic Confirmation Bias (4.97×). A cross-architecture proof-of-concept (DeBERTa NLI w=3) achieves +4.41pp (p=0.039) — the only positive result across 25+ attempts. Per-label analysis reveals structural complementarity: NLI dominates contradiction detection (71% vs SC 38%), while LLMs dominate uncertainty reasoning (68% vs NLI 19%).\\\\\\\"\\\\n\\\\n### Updated Story Spine (D092 — V3, G+R dual method)\\\\n\\\\n- **Problem**: [unchanged]\\\\n- **Theoretical lens**: [unchanged]\\\\n- **Systematic evaluation**: [unchanged]\\\\n- **Regime characterization**: [unchanged]\\\\n- **Remediation failures strengthen thesis (D085 FINAL)**: 9 prompt-level + 3 method-level + 13 new directions = **25+ interventions** across ALL dimensions (diversity/architecture/capability/verification/filtering/voting/solver/paradigm), all fail → bottleneck is fundamental and exhaustively proven\\\\n- **Method failure analysis**: Three methods targeting different bottleneck aspects show three distinct failure modes (neutral/harmful/catastrophic), revealing that the bottleneck operates at multiple levels simultaneously\\\\n- **Independence-accuracy trade-off (HERO FINDING, D075)**: Debate breaks trace correlation (κ 0.44→0.15, Eff-K 2.0→4.4) but accuracy collapses (-18.6pp/-23.0pp). Same-model traces can be independent OR accurate, not both.\\\\n- **Symbolic Confirmation Bias (CORE FINDING, D082)**: Root cause identified — self-extracted FOL constraints systematically confirm the trace's own answer (bias ratio 4.97× on incorrect problems). Causal chain: model reasons → answer → FOL extraction confirms answer → aggregation ≈ SC. This is WHY 25+ methods fail.\\\\n- **Process-κ (NEW METRIC, D082)**: CoT reasoning similarity (0.69) >> answer-κ (0.41), r=-0.06. Only 9.3% of trace pairs are \\\\\\\"convergent reasoning.\\\\\\\" answer-κ underestimates the true bottleneck. Novel metric applicable to all LLM trace aggregation.\\\\n- **NEW — Constraint-Answer Decoupling (CORE METHOD, D092)**: Having diagnosed the causal chain (conclusion→FOL→bias), we sever it: remove conclusion sentences before extraction. 4.1% text removal → +11.3pp (70/204). Minimal intervention, maximal effect. Directly proves the mechanism IS the cause.\\\\n- **NEW — Cross-Architecture Verification (COMPLEMENTARY METHOD, D092)**: DeBERTa NLI (406M) w=1 **+3.43pp (p=0.039, McNemar exact)** PRIMARY; w=3 +4.41pp (p=0.078 n.s.); NLI∩SC 68.48%@45%. Orthogonal fix: instead of fixing the extraction pipeline, add an architecturally independent voter. Per-label complementarity (NLI: False 71% vs SC 38%; SC: Unknown 68% vs NLI 19%).\\\\n- **Dual cure narrative**: G attacks information flow (removes biased input to extractor), R attacks architectural homogeneity (adds independent voter). Both work independently. Validates diagnosis from two angles.\\\\n- **Actionable contribution**: C0+SC diagnostic + κ-based Eff-K estimation + Decoupling method + NLI combo = complete toolkit from diagnosis to fix.\\\\n- **Universal across architectures (D078)**: Three families: Mistral-7B κ=0.438, LLaMA-8B κ=0.412, Qwen2.5-7B κ=0.658, Qwen2.5-14B κ=0.738. Family effect (Δκ=0.22) >> scale effect (Δκ=0.08).\\\\n- **Headline (D092)**: Independence bottleneck is structural to same-model extraction, universal across architectures, rooted in Symbolic Confirmation Bias. 25+ same-model interventions fail. Two independent cures succeed: Decoupling (+11.3pp, CONDITIONAL on full 204) attacks the causal chain, Cross-Architecture NLI (+3.43pp, p=0.039) provides external diversity. Both prove the diagnosis and provide practical solutions.\\\\n\\\\n## Core Insight (D060 Updated — Dual Bottleneck)\\\\n\\\\n**Dual Requirement Framework**: SICA 效应需要同时满足两个条件，缺一不可：\\\\n1. **Sufficient Independence** (Eff-K > threshold): traces 需要提供足够多的独立视角\\\\n2. **Sufficient Quality** (SC > ~50%): traces 需要有足够的正确率，否则约束是噪声\\\\n\\\\nCondorcet Jury Theorem 要求投票者独立且 p>0.5。同模型采样的 reasoning traces 严重违反独立性假设（Fleiss' κ = 0.21–0.82，Eff-K 仅 1.20–3.63），解释了为什么简单增加 K 或添加符号约束不能突破 SC 的天花板。\\\\n\\\\n实验数据完美支持 dual requirement（κ 使用统一脚本 compute_fleiss_kappa_unified.py，SC/Δpp 使用 registry 原始值）：\\\\n- **Qwen family**: κ=0.66-0.82, Eff-K≈1.20-1.46（独立性不足）→ all near-zero delta，无论 SC 多高\\\\n- **Mistral-7B FOLIO**: κ≈0.46, Eff-K≈2.0（中等独立性）+ SC≈55%（中等质量）→ +3.43pp best seed, mean +2.12pp (2/3 seeds positive, 1 null)\\\\n- **Mistral-7B PW-600**: κ=0.20, Eff-K=3.76（最高独立性）但 SC=39%（质量不足）→ -2.83pp\\\\n- 只有 Goldilocks zone（中等 Eff-K + 中等 SC）出现正向 delta\\\\n- **Dual bottleneck 直接验证 (exp-055)**：Multi-temp κ=0.427 Eff-K=2.11（比单温度 κ≈0.46 Eff-K≈2.0 更独立）但 delta=0.00pp → 提高 independence 不够，还需要 extraction quality\\\\n- **T sensitivity 孤立尖峰 (4/4 complete, D064 corrected)**：T=0.3(Δ=-1.47), T=0.5(Δ=-0.98), T=0.7(Δ=+3.43, κ=0.460, Eff-K=1.98), T=1.0(Δ=0.00, κ=0.394, Eff-K=2.25)。T=0.7 孤立尖峰更突出。T=0.7 SC=55.88%（最低）→ entropy 最高 → SICA 操作空间最大。温度效应与 SC 效应互为 confound，论文需讨论\\\\n- **Thinking mode κ=0.913, Eff-K=1.09 (exp-028b)**：近乎确定性。思维模式让 traces 更一致 → 独立性更差。\\\\\\\"更好的推理\\\\\\\"反而加剧 independence bottleneck。\\\\n\\\\n**κ 是 model-level 稳定属性**：统一处理后 Mistral 三 seed κ 收敛至 0.457-0.460（之前 0.41-0.50 差异是非标准 answer 处理的 artifact）。κ 跨 seed 几乎相同，但 delta 差异大（+3.43 vs +2.94 vs 0.00）→ seed-level constraint quality variance 主导，非 κ。\\\\n\\\\n完整 κ 表（⚠️ D062: κ 将用 raw answers 重算，当前 unified 值为临时值。Qwen 无变化，Mistral 条件将更新）：\\\\n| Exp | Model | κ(unified→raw pending) | Eff-K | SC%(registry) | Δpp(registry) |\\\\n|-----|-------|------------|-------|---------------|---------------|\\\\n| exp-028b | Qwen3-14B thinking | 0.913 | 1.09 | ~84% | ~0 |\\\\n| exp-038 | Qwen-14B LogiQA | 0.821 | 1.20 | 78.50 | -0.50 |\\\\n| exp-027 | Qwen3-14B | 0.773 | 1.26 | 84.31 | +0.49 |\\\\n| exp-036 | Qwen2.5-14B | 0.744 | 1.31 | 75.49 | +0.25 |\\\\n| exp-035 | Qwen2.5-7B | 0.658 | 1.46 | 76.47 | -0.49 |\\\\n| exp-049b | Mistral-7B LogiQA | 0.512 | 1.81 | 51.00 | +0.50 |\\\\n| exp-057 | Mistral-7B T=0.3 | 0.502 | 1.84 | 58.33 | -1.47 |\\\\n| exp-058 | Mistral-7B T=0.5 | 0.516 | 1.80 | 58.33 | -0.98 |\\\\n| exp-033 | Mistral-7B s42 | 0.460 | 1.98 | 55.88 | +3.43 |\\\\n| exp-052 | Mistral-7B s123 | 0.457 | 1.99 | 54.41 | +2.94 |\\\\n| exp-053 | Mistral-7B s456 | 0.457 | 1.99 | 55.88 | 0.00 |\\\\n| exp-055 | Mistral-7B multi-T | 0.427 | 2.11 | 57.84 | 0.00 |\\\\n| exp-054 | Mistral-7B T=1.0 | 0.394 | 2.25 | 55.39 | 0.00 |\\\\n| exp-046 | Mistral-7B PW-600 | 0.200 | 3.76 | 39.33 | -2.83 |\\\\n注：κ 基于 T/F/U 三类归一化，Mistral-7B 约 12-16% traces 被归一化（Qwen 100% valid）。Mistral SC/Δpp 已更新为 D064 tiebreaking 修正值；Qwen 不受影响。\\\\n\\\\nOracle control (+14.22pp) 证明 MAX-SAT 聚合机制本身有效，但自提取约束仅利用了 24% 的理论上限。Discriminative filtering 实验揭示关键机制：~92% 约束 ARE discriminative，但过滤掉 ~8% non-discriminative 约束后 delta 不变（0 gains）。问题不在约束缺乏判别力，而在于 discriminative constraints 的区分方向与模型偏差一致（confirmation bias）。\\\\n\\\\n**Remediation insight (D060)**: 9 种修复尝试全部失败，包括直接靶向 independence（multi-temp diversity, exp-055: Eff-K 从 2.0→2.11 但 delta 仍为 0）和 constraint quality（discriminative filtering）。这证明 bottleneck 不是简单的 diversity 或 quality 问题，而是 same-model self-extraction 的根本性限制。\\\\n\\\\n**Key evidence**:\\\\n- **Condorcet independence quantification (统一脚本, 公式: Eff-K=K/(1+(K-1)κ))**: Mistral-7B FOLIO κ≈0.46 (Eff-K≈2.0, 三 seed 高度稳定), Mistral-7B PW-600 κ=0.200 (Eff-K=3.76), Qwen2.5-14B FOLIO κ=0.744 (Eff-K=1.31), Qwen2.5-14B LogiQA κ=0.821 (Eff-K=1.20), Qwen3-14B κ=0.773 (Eff-K=1.26), Qwen2.5-7B κ=0.658 (Eff-K=1.46). 跨模型清晰: Qwen Eff-K≈1.2-1.5→0 gain, Mistral FOLIO Eff-K≈2.0→variable gain, Mistral PW Eff-K=3.76 but SC too low→negative. κ stable across seeds (0.457-0.460), delta varies → seed-level constraint quality dominates.\\\\n- **Oracle control (exp-031)**: Gold FOL + MAX-SAT = 89.71% vs SC 75.49% (+14.22pp, p=2.0e-7). Unknown-type +31.9pp.\\\\n- **Two-layer constraint analysis**: 43% trivially_satisfied (taxonomy: satisfied by ALL answers) vs ~8% non-discriminative (filtering: same MAX-SAT score). Difference: trivially_satisfied constraints can still have different satisfaction DEGREES. Removing the 8% yields 0 gains → problem is not quality but confirmation bias direction.\\\\n- **K sensitivity (non-monotonic peak at K=12, 5/5 complete, D064+D066)**: K=4(-1.47pp), K=8(-1.96pp), K=12(+3.43pp p=0.092 ns), K=16(+1.47pp), K=20(+1.96pp). Peak at K=12, drops at K=16 but partially recovers at K=20. NOT clean inverted-U. K=12 SC=55.88% (post-fix). SC-confound with T sensitivity still holds. SICA at K=4 vs K=12 differs by ~4.9pp despite similar SC — proves SICA extracts different information than SC.\\\\n- **SC-confound (cross-cutting insight)**: K=12 和 T=0.7 都是 SC 最低 (54.41%) 的配置 → SICA \\\\\\\"最佳超参\\\\\\\"可能反映 entropy/operating-window 效应而非 K 或 T 的因果贡献。论文需要讨论这个 confound，但也可以正面利用：SC level 是更基本的预测变量，K 和 T 通过影响 SC 来间接影响 SICA delta。\\\\n- **T sensitivity (isolated peak, 4/4 complete, D064 corrected)**: T=0.3(Δ=-1.47pp), T=0.5(Δ=-0.98pp), T=0.7(Δ=+3.43pp p=0.092 ns), T=1.0(Δ=0.00pp). NOT smooth inverted-U — T=0.7 is an isolated spike. T=0.7 has lowest SC (55.88%) → highest entropy → largest SICA operating window. Temperature and SC effects confounded. Strengthens fragility narrative.\\\\n- **Regime boundary**: Qwen-14B (SC=75.49%) Δ=-0.98pp vs Mistral-7B (SC=55.88%) Δ=+3.43pp p=0.092 ns\\\\n- **Type C failure (exp-046)**: Mistral PW-D5 SC=39.33%, Δ=-2.83pp, p=0.010, κ=0.210, Eff-K=3.63, contradiction rate 5.5%. Highest Eff-K yet worst delta → independence alone insufficient when SC too low.\\\\n- **Seed replication (D064+D066)**: 2/3 seeds positive but **0/3 significant** after tiebreaking correction: s42 Δ=+3.43pp p=0.092, s123 Δ=+2.94pp p=0.070, s456 Δ=0.00pp p=1.0. Mean +2.12pp. Only significant McNemar effects are NEGATIVE: exp-046 Δ=-2.83pp p=0.014, exp-039 Δ=-2.50pp p=0.011. Paper must frame as \\\\\\\"positive directional trend\\\\\\\" not \\\\\\\"significant positive effect\\\\\\\".\\\\n- **Nine remediation failures (ALL CONFIRMED)**: contrastive prompting, cross-model, generational scaling, solver-guided, consistency filtering, cross-trace UNSAT, discriminative filtering (0 gains), T=1.0 (delta collapse +3.43→0.00pp, D064 corrected), multi-temp (delta=+0.00pp, b=5 c=5). All 9 failed → trap is fundamental, bottleneck is structural.\\\\n- **Entropy decomposition (VERIFIED 2026-05-19)**: High-entropy proportion: Mistral FOLIO 38% (78/204) vs Qwen FOLIO 18% (37/204) vs Qwen LogiQA 12% (23/200). SICA on high-entropy: Mistral FOLIO s42 +12.8pp, s123 +9.1pp, s456 -1.3pp; Qwen FOLIO -8.2pp; all others negative. Low-entropy: SICA≈SC across all 8 experiments (Δ≈0). Entropy decomposition reveals regime-dependent mechanism, NOT universal diagnostic.\\\\n- **Confirmation bias quantification**: ⚠️ \\\\\\\"62.3%\\\\\\\" and \\\\\\\"28.6%\\\\\\\" confirmed NOT present in any .tex file — likely hallucinated in earlier draft. DO NOT USE. Replace with verified metrics from experiment outputs only.\\\\n\\\\n## Story Spine (D059 Updated)\\\\n\\\\n- **Problem**: LLMs' reasoning can be improved by sampling multiple chains-of-thought and aggregating via majority voting (self-consistency). Recent work proposes symbolic augmentation: extract formal constraints from traces and use SAT solvers for answer selection. But does symbolic aggregation actually outperform simple voting?\\\\n- **Theoretical lens**: Condorcet Jury Theorem requires voter independence. We quantify trace independence via Fleiss' κ and show Effective-K << nominal K. This explains the fundamental limitation of same-model trace aggregation.\\\\n- **Systematic evaluation**: SICA (MAX-SAT over FOL constraints) across 3 domains × 5 model families. Oracle control separates extraction vs aggregation failure. Discriminative filtering reveals ~92% constraints are discriminative, yet SICA gains are fragile — confirmation bias, not constraint quality, is the bottleneck.\\\\n- **Regime characterization**: Three failure modes (Type A/B/C) + narrow Goldilocks zone. C0+SC as deployment diagnostic.\\\\n- **Remediation failures strengthen thesis**: 9 targeted interventions (prompting, architecture, capability, verification, diversity, filtering) all fail to close the oracle gap, proving the bottleneck is fundamental to same-model self-extraction.\\\\n- **Headline result (D066 McNemar corrected)**: \\\\\\\"Across 6 models and 4 domains, symbolic consensus aggregation shows no statistically significant positive effect under corrected tiebreaking (best seed +3.43pp, p=0.092). The only significant effects are negative (PW-600: -2.83pp p=0.014, -2.50pp p=0.011). However, entropy decomposition reveals a striking regime-dependent pattern: SICA's entire effect concentrates on high-entropy questions, with +12.8pp in the Goldilocks zone but -2 to -8pp elsewhere. Oracle constraints prove the aggregation mechanism works (+14.22pp, p<0.001), localizing the bottleneck to extraction quality (24% utilization). Condorcet analysis (Eff-K=1.2-2.0 for nominal K=12) explains trace non-independence. Nine remediation strategies all fail, confirming the bottleneck is structural to same-model self-extraction.\\\\\\\"\\\\n\\\\n## Anticipated Reviewer Concerns & Defensive Experiments\\\\n\\\\n1. **\\\\\\\"Gains not statistically significant\\\\\\\"** → Correct: no positive effect reaches significance (best p=0.092). This IS the finding. Oracle p=2.0e-7 proves the mechanism works; the insignificance of self-extraction gains demonstrates the extraction bottleneck. Regime pattern (8 entropy conditions) provides systematic evidence beyond any single p-value.\\\\n2. **\\\\\\\"Only one positive result (exp-033)\\\\\\\"** → Seed replication: 2/3 positive (s42 +3.43pp, s123 +2.94pp), 1/3 null (s456 0.00pp). Mean +2.12pp. Effect IS real but fragile — the fragility itself IS the finding.\\\\n3. **\\\\\\\"Condorcet framework is trivial\\\\\\\"** → Fleiss' κ quantification is novel in SC/SICA context. Eff-K is actionable: tells practitioners how many truly independent traces they get.\\\\n4. **\\\\\\\"Multi-temp / filtering should work\\\\\\\"** → We tried both. Multi-temp (exp-055): negative. Disc. filtering: 0 gains. T=1.0: delta collapse. These failures STRENGTHEN the structural bottleneck thesis.\\\\n5. **\\\\\\\"Only Qwen models\\\\\\\"** → 5 families: Qwen-14B, Mistral-7B, LLaMA-8B, DeepSeek-R1-7B, QwQ-32B.\\\\n6. **\\\\\\\"Only logic domain\\\\\\\"** → FOLIO + ProofWriter + LogiQA + StrategyQA + ARC-Challenge. Type B (domain formalizability) is itself a finding.\\\\n7. **\\\\\\\"Oracle is unfair comparison\\\\\\\"** → Diagnostic tool, not competing method. Separates extraction from aggregation.\\\\n8. **\\\\\\\"MAX-SAT is over-engineering\\\\\\\"** → exp-013: MaxSAT ≈ count-only. This IS the independence bottleneck evidence.\\\\n9. **\\\\\\\"Self-extraction confound\\\\\\\"** → Oracle control resolves completely.\\\\n10. **\\\\\\\"Published methods achieve gains (DyLoS, Aristotle, FoVer)\\\\\\\"** → Different paradigm (external verifiers/trained extractors). We characterize same-model self-extraction.\\\\n11. **\\\\\\\"C0 is trivially derived\\\\\\\"** → Zero-cost early stopping. Practical value.\\\\n12. **\\\\\\\"Why not just use a reasoning model?\\\\\\\"** → QwQ-32B: C0<5%, SICA≡SC.\\\\n13. **\\\\\\\"Random tiebreak baseline\\\\\\\"** → exp-003: SICA tiebreak 80% vs random 50%.\\\\n14. **\\\\\\\"Method improvement is incremental\\\\\\\"** → Grounded in diagnosis (independence + taxonomy), not ad-hoc.\\\\n15. **\\\\\\\"Weighted SC is simpler\\\\\\\"** → exp-016 planned. Weighted SC doesn't address independence.\\\\n16. **\\\\\\\"Within-model ICL transition contradicts regime theory\\\\\\\"** → exp-050b (SC=57.79%, Δ=-3.52pp): ICL changes trace generation characteristics, not just SC level. Paper must distinguish \\\\\\\"same model, different prompt\\\\\\\" from \\\\\\\"same model, same prompt, different accuracy.\\\\\\\"\\\\n\\\\n## Working Title (D092 V3 — G+R dual method)\\\\n**\\\\\\\"Breaking Symbolic Confirmation Bias: Constraint-Answer Decoupling and Cross-Architecture Verification for LLM Logical Reasoning\\\\\\\"**\\\\n(Alternatives:\\\\n- \\\\\\\"Two Cures for One Disease: Decoupling and Architectural Diversity Against Symbolic Confirmation Bias in LLM Reasoning\\\\\\\"\\\\n- \\\\\\\"The Independence Bottleneck in Symbolic LLM Reasoning: Diagnosis, 25+ Failed Interventions, and Two Independent Solutions\\\\\\\"\\\\n- V2 fallback (R only): \\\\\\\"Breaking the Self-Consistency Ceiling: How Cross-Architecture Verification Overcomes Symbolic Confirmation Bias in LLM Reasoning\\\\\\\"\\\\n- V1 fallback (pure negative): \\\\\\\"Beyond Self-Consistency: How Trace Independence Limits Symbolic Consensus in LLM Reasoning\\\\\\\")\\\\n\\\\nNOTE (Dream D037): Title MUST be scoped to \\\\\\\"self-extracted constraints\\\\\\\" / \\\\\\\"SICA\\\\\\\". Published methods (DyLoS, Aristotle, FoVer) use different approaches.\\\\n\\\\n## Paper Structure (D092 V3 — EMNLP 8pp + appendix)\\\\n\\\\n### Sections\\\\n- §1 Introduction: 25+ same-model interventions all fail → independence bottleneck → two independent cures\\\\n- §2 Related Work: SC, neuro-symbolic, Condorcet/voting, verification\\\\n- §3 Diagnostic Framework: Independence Bottleneck (Eff-K, process-κ), Oracle Gap\\\\n- §4 Symbolic Confirmation Bias: bias ratio 4.97×, overlap 94%, causal chain\\\\n- §5 Method 1: Constraint-Answer Decoupling (G) — core method, detailed\\\\n- §6 Method 2: Cross-Architecture NLI Verification (R) — complementary method\\\\n- §7 Combined Analysis: G+R combo, ablation, cross-dataset if available\\\\n- §8 Discussion + Conclusion\\\\n\\\\n### Main Tables\\\\n- T1: Main Results — models × domains, SC% / SICA% / Δpp / p-value, regime boundary\\\\n- T2: Oracle Control — Gold-FOL+MAX-SAT vs SC vs SICA-self, causal separation\\\\n- T3: Independence Quantification — Fleiss' κ / Eff-K / trace agreement per model\\\\n- T4: Confirmation Bias — bias ratio per condition, overlap rate, per-label breakdown\\\\n- T5: Decoupling Results (G) — SC / SICA / G-Decoupled, Δpp, McNemar, per-label\\\\n- T6: NLI Verification Results (R) — SC / NLI standalone / combo w=1,3 / intersection, Δpp, McNemar\\\\n- T7: 25+ Intervention Summary — method / type / dataset / result / failure mode (compact)\\\\n\\\\n### Main Tables (continued)\\\\n- T6: Method-Level Intervention Results — 3 methods × 2 datasets, SC% / Method% / Δpp, failure mode classification\\\\n- T7: κ Generalization — SC / Debate / Diverse-Prompt κ and Eff-K (from exp-077, pending)\\\\n\\\\n### Main Figures\\\\n- F1: Method Pipeline (SICA + oracle control design)\\\\n- F2: SC Accuracy vs SICA Δ scatter (hero figure, regime boundary)\\\\n- F3: K Sensitivity with diversity metrics (K vs Δ, K vs Eff-K)\\\\n- F4: Extraction error breakdown (stacked bar)\\\\n- F5: Method intervention failure modes (grouped bar: ICG/Contrastive/Debate × FOLIO/LogiQA)\\\\n\\\\n### Appendix\\\\n- K ablation details, temperature sensitivity, per-domain results, overhead analysis\\\\n- Entropy-conditioned analysis (continuous scatter + bin sensitivity)\\\\n- Six remediation strategy details\\\\n- Confirmation bias quantification\\\\n- Seed replication analysis\\\\n- QwQ-32B / DeepSeek-R1 negative control\\\\n\\\\n## Claim Risk Notes (D059)\\\\n- **Seed replication**: 0/3 significant after D066 correction (p=0.092, 0.070, 1.0). 2/3 positive trend, 1/3 null. Mean +2.12pp. Frame as \\\\\\\"directional trend, not significant effect\\\\\\\" — fragility IS the finding.\\\\n- **Method claims DEAD (D060)**: All three method improvements failed. Paper is pure analysis. 9 remediation failures are EVIDENCE, not limitation.\\\\n- **Condorcet novelty**: ✅ VERIFIED. arXiv:2409.00094 applies CJT to cross-model LLM ensembles (different angle). No prior work applies Fleiss' κ or Eff-K to within-model SC traces. Our framing is novel.\\\\n- **exp-050b complication**: ICL transition Δ=-3.52pp at SC=57.79% complicates simple \\\\\\\"SC determines SICA.\\\\\\\" Explain via trace generation characteristic change.\\\\n- **Variable naming inconsistency**: 56.4% cross-trace pairs share zero Z3 variables. Key mechanism evidence.\\\\n\\\\n## Required Citations (minimum 30 references)\\\\n\\\\n- **SC & extensions**: Wang et al. 2023 (SC), Chen et al. 2023 (USC), Loo et al. 2025 (SC scaling plateaus), Taubenfeld et al. 2025 (weighted SC), DiVeRSe (Li et al. 2023)\\\\n- **Neuro-symbolic reasoning**: DyLoS (EACL 2026), Aristotle (ACL 2025), FoVer (TACL 2025), LogicAgent (2025), Logic-LM (Pan et al. 2023), LINC (Olausson et al. 2023)\\\\n- **Condorcet/voting theory**: Condorcet 1785, Austen-Smith & Banks 1996, **arXiv:2409.00094 (Examining Independence in Ensemble Sentiment Analysis, Sept 2024)** — closest prior work, applies CJT to cross-model LLM ensembles, finds independence violation. Our novelty: within-model trace independence + Fleiss' κ quantification + Eff-K + connection to symbolic aggregation\\\\n- **Test-time compute**: Snell et al. 2025, DeepSeek-R1, Diversity-Aware Training\\\\n- **Verification & reranking**: ORM (Cobbe et al. 2021), PRM (Lightman et al. 2023), Math-Shepherd\\\\n- **Constraint satisfaction**: SATBench (EMNLP 2025), LLM Meets Constraint Propagation (IJCAI 2025)\\\\n- **Debate & multi-agent**: Liang et al. 2023, Du et al. 2023\\\\n\\\\n## Additional Reviewer Concerns (D070/D074 Methods)\\\\n\\\\n17. **\\\\\\\"Why not use a larger model for constraint generation?\\\\\\\"** → Valid. All methods tested at 7B scale. ICG constraint parsing failures + Debate role-play degradation may be scale-dependent. This is explicitly noted as limitation and future work. The contribution is diagnosing the bottleneck and showing it's not trivially fixable, not claiming no fix exists at any scale.\\\\n18. **\\\\\\\"Only tested one model (Mistral-7B) for methods\\\\\\\"** → Methods are interventions on the extraction pipeline, not the base model. Testing on the same model that showed the clearest Goldilocks signal (Mistral-7B FOLIO) is the strongest test — if methods can't improve the best-case scenario, they won't help elsewhere.\\\\n19. **\\\\\\\"ICG multi-seed shows 1/3 positive\\\\\\\"** → Magnitudes (-2.0, +1.5, -1.0) are within SC baseline noise (3.5pp cross-seed). Mean ≈-0.5pp, std=1.8pp. No statistical significance. Properly framed as \\\\\\\"noise-level, neither improving nor degrading.\\\\\\\"\\\\n20. **\\\\\\\"Debate working in other papers\\\\\\\"** → Multi-agent debate literature uses diverse models or much larger models. Same-model 7B debate is a different regime. Our finding is specifically about same-model self-extraction limitations.\\\\n\\\\n## Claim Scoping Rules\\\\n- n=60 conditions: \\\\\\\"suggestive/consistent with\\\\\\\" NOT \\\\\\\"confirming\\\\\\\"\\\\n- n≥200 conditions: can \\\\\\\"confirm\\\\\\\"\\\\n- Combined N>1,300: acceptable if breakdown clearly stated\\\\n- Method claims: must show statistically significant improvement OR clear directional improvement with analysis\\\\n- \\\\\\\"Independence bottleneck\\\\\\\" framing: systematic quantification + theoretical grounding\\\\n\\\\n## V16 Frontier Model Extension (D135–D139)\\\\n\\\\n### New Claim 11: SCB is Universal — 7B to Frontier (D135)\\\\n\\\\nSymbolic Confirmation Bias persists across ALL tested models, from 7B open-source to frontier closed-source:\\\\n\\\\n| Model | Extraction | SC% | SICA% | Δpp | BR(mean) | BR=∞ rate | Process-κ | Answer-κ |\\\\n|-------|-----------|-----|-------|-----|----------|-----------|-----------|----------|\\\\n| Mistral-7B | self | 55.88 | 59.31 | +3.43 | 4.97 | 30% | 0.69* | 0.46 |\\\\n| LLaMA-8B | self | — | — | — | 2.88 | — | — | — |\\\\n| Qwen-14B | self | 75.49 | 75.74 | +0.25 | 3.93 | — | — | 0.74 |\\\\n| R1-Distill-8B | cross→Mistral | 74.51 | 76.96 | +2.45 | 2.92 | — | 0.248 | 0.69 |\\\\n| gpt-4o | self | 73.91 | 72.05 | -1.86 | 2.94 | 44% | 0.79 | 0.80 |\\\\n| gpt-4.1 | cross→Mistral | 82.84 | 81.37 | -1.47 | 2.70 | 58% | 0.792 | 0.86 |\\\\n| gpt-5.5 | cross→Mistral | 84.31 | 84.80 | +0.49(n.s.) | 3.48 | 87% | 0.563 | 0.96 |\\\\n| o3 | cross→Mistral | 82.65 | 82.65 | 0.00 | 1.66 | 82% | 0.596 | 0.92 |\\\\n| Gemini-2.5-Pro* | cross→Mistral | 87.37 | 86.32 | -1.05 | 2.79 | — | 0.790 | 0.75 |\\\\n\\\\n*Gemini: 95/204 interim. Mistral Process-κ is CoT cosine sim (different metric from cross-model TF-IDF κ).\\\\n\\\\nBR > 1 across ALL models (1.66–4.97×). BR=∞ rates high in frontier models (44–87%).\\\\nTable footnote MUST distinguish self vs cross extraction context.\\\\n\\\\n### New Claim 12: Process-κ Gradient Predicts Cross-Model Extraction Effectiveness (D137–D139)\\\\n\\\\nCross-model extraction (Mistral-7B extracts FOL from other models' traces) effectiveness is monotonically predicted by Process-κ:\\\\n\\\\n| Model | Process-κ | Δ(SICA-SC) | BR(mean) |\\\\n|-------|-----------|------------|----------|\\\\n| R1-Distill | 0.248 | +2.45pp ✓ | 2.92 |\\\\n| gpt-5.5 | 0.563 | +0.49pp(n.s.) | 3.48 |\\\\n| o3 | 0.596 | 0.00pp | 1.66 |\\\\n| Gemini-2.5-Pro* | 0.790 | -1.05pp | 2.79 |\\\\n| gpt-4.1 | 0.792 | -1.47pp | 2.70 |\\\\n\\\\n**Spearman ρ(κ→Δ) = -1.0, n=5, one-tailed p=0.0083** (statistically significant).\\\\n\\\\n**Paper language constraints (D138)**:\\\\n- Use \\\\\\\"decreases monotonically\\\\\\\" — NOT \\\\\\\"predictive\\\\\\\" or \\\\\\\"significant correlation\\\\\\\"\\\\n- Dual-variable framing: \\\\\\\"two necessary conditions\\\\\\\" (qualitative mechanism), NOT regression model\\\\n  - Low κ (diverse traces) → cross-model extractor can contribute novel constraints\\\\n  - High BR (strong self-bias) → there IS bias to escape from\\\\n  - Both conditions required: o3 (BR=1.66, near-unbiased) → Δ=0 despite moderate κ=0.596\\\\n- o3 BR=1.66 is observation (\\\\\\\"bimodal error pattern: 82% BR=∞ but low finite-BR\\\\\\\"), NOT sub-finding\\\\n- BR=∞ ordering does NOT strictly follow \\\\\\\"model capability\\\\\\\" (o3 82% < gpt-5.5 87%). Drop ordering claim.\\\\n\\\\n### Updated Headline (V16)\\\\n\\\\n\\\\\\\"Symbolic Confirmation Bias is universal from 7B open-source to frontier closed-source models (BR 1.66–4.97×). Cross-model extraction effectiveness decreases monotonically with Process-κ (ρ=-1.0, n=5, p=0.008), modulated by bias severity: gain requires both diverse traces (low κ) AND substantial self-bias (high BR). 25+ same-model interventions fail; two cross-architecture cures succeed.\\\\\\\"\\\\n\\\\n### V16 Paper Structure Impact\\\\n\\\\n- §4 SCB: Add frontier model BR table (Table 4 or expanded T4)\\\\n- §3 or new §: Process-κ gradient analysis (Table + scatter plot)\\\\n- §1 Intro: Scale claim upgraded from \\\\\\\"7B-32B\\\\\\\" to \\\\\\\"7B to frontier\\\\\\\"\\\\n- Limitations: Update \\\\\\\"7B to 32B parameters\\\\\\\" scope claim\\\\n- New Figure: Process-κ vs Δ scatter with dual-variable annotation (5 points + regression-free narrative)\\\\n\\\", \\\"total_chars\\\": 40785, \\\"truncated\\\": false}, \\\"error\\\": null, \\\"metadata\\\": {}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/paper_framing.md\", \"content\": \"# Paper Framing — symb_invariant_consensus\\n\\n## Target Venue\\n- Primary: EMNLP 2026 Main (ARR May 25)\\n- Deadline: May 25, 2026 (ARR submission)\\n\\n## D063 Direction: Entropy Decomposition + Quality Ladder — 目标 4.0\\n\\n**从 D060 \\\"Pure Analysis / negative result\\\" 升级为 \\\"Regime-Dependent Mechanism Analysis with Entropy Decomposition\\\"。** 用户决定冲 4.0。\\n\\n### Entropy Breakdown 验证结果 (2026-05-19 completed)\\n\\n**跨模型 entropy mechanism 一致性: 不成立。Selective SICA 非 universal 方案。**\\n\\n但 entropy decomposition 揭示了更有价值的 regime mechanism：\\n\\n| Experiment | Model | Dataset | High-E n | High-E Δpp | Low-E n | Low-E Δpp |\\n|-----------|-------|---------|----------|-----------|---------|----------|\\n| exp-033 s42 | Mistral-7B | FOLIO | 78 | **+12.8** | 126 | 0.0 |\\n| exp-052 s123 | Mistral-7B | FOLIO | 77 | **+9.1** | 127 | 0.0 |\\n| exp-053 s456 | Mistral-7B | FOLIO | 75 | -1.3 | 129 | 0.0 |\\n| exp-046 | Mistral-7B | PW-600 | 267 | -4.9 | 333 | -1.2 |\\n| exp-036 | Qwen2.5-14B | FOLIO | 37 | **-8.2** | 167 | -0.6 |\\n| exp-038 | Qwen2.5-14B | LogiQA | 23 | -4.3 | 177 | 0.0 |\\n| exp-035 | Qwen2.5-7B | FOLIO | 47 | -2.1 | 157 | 0.0 |\\n| exp-048 | LLaMA-8B | PW-600 | 76 | -3.9 | 104 | -1.9 |\\n\\n(注: SC/Δ 使用 pre-tiebreaking 值，entropy grouping 不受 tiebreaking 影响。D064 修正后 deltas 会略有变化但 pattern 不变。)\\n\\n**三个核心发现：**\\n1. **Low-entropy: SICA≈SC 跨模型一致** (8/8 experiments Δ≈0) → traces 一致时 constraints 无新信息\\n2. **High-entropy 方向因 regime 而异**：Goldilocks +12.8pp vs Type A -8.2pp vs Type C -4.9pp\\n3. **Mechanism 解释**：\\n   - Goldilocks (SC~55%, κ~0.46): 真实不确定性 → constraints 打破平局正确方向\\n   - Type A (SC>75%, κ>0.65): 偶发错误 → constraints 放大 confirmation bias\\n   - Type C (SC<40%, κ~0.20): 系统性错误 → constraints 是噪声\\n\\n### 调整后核心转变\\n\\n论文以 \\\"entropy decomposition 揭示 regime-dependent mechanism\\\" 为核心分析贡献（不是 universal diagnostic）：\\n- **Entropy decomposition 作为分析工具**：分离 SICA 作用点（high-entropy）vs 不作用点（low-entropy）\\n- **Regime mechanism 量化**：同样是 high-entropy 问题，direction depends on SC+κ → 完美支持 dual bottleneck\\n- **Abandoned**: Selective SICA 作为 universal practical contribution（只在 Goldilocks zone 有效）\\n- **Upgraded**: 核心图 = high-entropy Δ vs SC scatter（8 points, 3 regimes 清晰分离）\\n- **Quality Ladder** (D067: L1 NULL CONFIRMED)\\n  - L0: Self-extraction (Mistral→Mistral): 59.31%, Δ=+3.43pp ns\\n  - L1a: Qwen3-14B→Mistral traces: 60.29%, Δ=+4.41pp (+0.98pp vs self = 2题/204 = noise)\\n  - L1b: Qwen2.5-14B→Mistral traces: 58.33%, Δ=+2.45pp (-0.98pp vs self = 2题/204 = noise)\\n  - L3: Oracle 100% disc, Δ=+14.22pp p<0.001\\n  - **结论**: L1 ≈ L0 << L3。Bottleneck 在 traces（同源输入），不在 extractor（换模型无效）\\n  - **Paper contribution**: \\\"bottleneck is fundamental to extraction, not just model capability\\\" — 强化 structural limitation 论点\\n- **CJT/Eff-K 保留**：解释 why high-entropy behavior differs across regimes\\n\\nD060 要素全部保留：\\n- Condorcet independence 框架 → 理论基础\\n- 9 种修复全部失败 → structural limitation 证据\\n- 2/3 seeds positive trend but **0/3 significant** (D066: p=0.092/0.070/1.0) → Goldilocks zone 作为 directional trend, not confirmed effect\\n- K/T sensitivity non-monotonic → SC confound insight\\n- 用户指示: 投 May 25 不变，冲 4.0\\n\\n## Core Claims (5 条) — D060 纯 Analysis Framing\\n\\n### Analysis Claims (已验证)\\n\\n1. **Independence Bottleneck**: Self-consistency 隐含 Condorcet Jury Theorem 的独立性假设，但同模型采样的 traces 高度相关。Worker 验证的 κ 值：\\n   - Qwen-14B FOLIO: κ=0.744, Eff-K=1.31 (SC=75.49%, Δ=+0.25pp n.s.)\\n   - Qwen-14B LogiQA: κ=0.821, Eff-K=1.20 (SC=78.5%, Δ=+0.50pp n.s.)\\n   - Mistral-7B FOLIO s42 (exp-033): κ=0.501, Eff-K=1.84 (SC=55.88%, Δ=+3.43pp **p=0.092 ns**) ← primary seed [D064+D066]\\n   - Mistral-7B FOLIO s123: κ=0.491, Eff-K=1.88 (SC=54.41%, Δ=+2.94pp **p=0.070 ns**)\\n   - Mistral-7B FOLIO s456: κ=0.507, Eff-K=1.82 (SC=55.88%, Δ=0.00pp p=1.0 ns)\\n   - Mistral-7B PW-600 (exp-046): κ=0.210, Eff-K=3.63 (Δ=-2.83pp p=0.010, SC=39%)\\n   规律：跨模型对比清晰（Qwen Eff-K≈1.2-1.3 → 0 gain; Mistral Eff-K≈1.85-2.22 → variable gain）。但 Mistral seeds 内部，Eff-K 与 delta 非单调（exp-033 Eff-K 最低 1.85 却 delta 最高 +3.43pp）→ Eff-K 是跨模型必要条件，seed 内 variance 仍主导。exp-046 Eff-K 最高(3.63) 但 SC 太低(39%) 导致 delta 为负 → 需同时满足 sufficient Eff-K AND sufficient SC。\\n\\n2. **Oracle Gap Localizes Extraction Bottleneck**: Gold FOL + MAX-SAT = +14.22pp (p=2.0e-7)，自提取仅 +3.43pp (best seed, D064 corrected) = 24% utilization。聚合机制本身有效，瓶颈在自提取质量。Two-layer analysis:\\n   - **Constraint taxonomy**: 43% trivially_satisfied（被所有候选答案满足的约束，不排除任何答案）\\n   - **Discriminative filtering**: 仅 ~8% 约束在 MAX-SAT scoring 中完全 non-discriminative（移除后 0 gains）\\n   - **关键区分**: 43% 和 8% 度量不同。trivially_satisfied 约束在 MAX-SAT 中仍可有不同满足程度（partial vs full），所以不全是 non-discriminative。但即使 constraints 是 discriminative 的，它们的\\\"区分方向\\\"与模型自身偏差一致（confirmation bias）。both_wrong 组 score_range=29.4。九种修复全部失败。\\n\\n3. **Regime-Dependent Capability Trap**: SICA 有效性取决于提取模型的基线准确率，存在双边界：\\n   - Type A (SC ≥ ~60%): 确认偏差，constraints 镜像模型自身答案。**exp-034 vs exp-039 同配置 delta 翻转**: exp-034 Δ=+0.51pp (n=589), exp-039 Δ=-2.00pp (n=600)。SC baseline 方差 (3.38pp) >> SICA 效应 → Type A delta 是 trace sampling noise。SICA 比 SC 更稳定 (跨运行方差 0.87pp vs 3.38pp，仅 2 点，需更多 seed 验证)\\n   - Type C (SC ≤ ~40%): traces 主要错误，constraints 是噪声 (exp-046: Δ=-2.83pp, p=0.0095)\\n   - Goldilocks zone (~50-56% SC): 部分独立性 + 部分正确性 (exp-033: Δ=+3.43pp, p=0.092 ns; mean of 3 seeds: +2.12pp) ⚠️ D076 Reviewer: 0/3 seeds significant, 不应作为核心叙事支柱。作为 directional observation 保留，不做强 claim。\\n   - Type B: 领域不可形式化 (LogiQA: contradiction rate 0.8%)\\n\\n4. **C0+SC Two-Dimensional Diagnostic**: C0 (multi-candidate rate) + SC accuracy 形成零成本部署诊断。C0<5% → degenerate; high C0 + high SC → trap; high C0 + low SC → potential gains。\\n\\n### Remediation Evidence (D060: 全部失败 — 强化 analysis narrative)\\n\\n5. **Nine Remediation Attempts All Failed**: 原 6 种 + 3 种靶向修复全部无效，证明 independence bottleneck 是结构性的：\\n   - D059 三路 method improvement 全部失败：\\n     - Discriminative Filtering: 119/204 处理后 0 gains 1 loss，~92% 约束本身就是 discriminative，过滤是 near-no-op\\n     - T=1.0 (exp-054): delta 从 +3.43pp 崩塌到 0.00pp（D064 corrected），温度敏感性极端\\n     - Multi-Temp (exp-055): ✅ 完成，delta=+0.00pp (b=5,c=5 完美对称), SC=57.84%. 混合 T=0.3/0.7/1.2 各 4 traces 未改善 SICA。附带发现：multi-temp 提升 SC baseline (+3.4pp vs 单温度 54.41%)，说明混合温度对 majority voting 有帮助，但 SICA constraint extraction 无法利用这种 diversity → bottleneck 在 extraction 而非 trace diversity\\n   - 原 6 种：contrastive prompting, cross-model extraction, generational scaling, solver-guided refinement, consistency filtering, cross-trace UNSAT\\n   - 9 种修复涵盖 prompting / architecture / capability / verification / diversity / filtering 全维度，全部失败 → trap is fundamental\\n\\n## D070/D074 Update: Method-Level Interventions Also Fail — \\\"Fundamental Limitation\\\" Confirmed\\n\\n### Three Method Lines × Two Datasets = All Negative (D074)\\n\\nD070 从纯 analysis 升级为 analysis + method paper，但三条方法线全面失败（D074 确认），反而强化了原始 analysis 结论。\\n\\n**方法×数据集完整结果**：\\n| Method | FOLIO-204 | LogiQA-200 | Failure Mode |\\n|--------|-----------|------------|--------------|\\n| ICG (Independent Constraint Gen.) | Δ=-2.0pp (3-seed: -2.0/+1.5/-1.0, mean=-0.5pp±1.8pp, 噪声) | Δ=-0.5pp | Neutral — 独立约束质量≈trace-sourced约束 |\\n| Contrastive (Pro/Con Scoring) | Δ≈-16pp | Δ≈-7pp (interim) | Harmful — 26% degenerate scoring, pro/con 不平衡 |\\n| Debate (Proposer/Critic) | Δ=-18.6pp | Δ≈-28pp (interim) | Catastrophic — 7B 模型角色扮演严重退化推理 |\\n\\n**三种失败模式的分析价值**（论文 \\\"Why Methods Fail\\\" section）：\\n1. **ICG (neutral)**: 独立于 traces 生成的约束不比 trace-sourced 约束更好。说明 bottleneck 不仅是 \\\"约束来自 traces\\\"，而是模型的推理偏差从问题理解阶段就存在——独立约束和 trace-sourced 约束继承相同的 model bias。\\n2. **Contrastive (harmful)**: 强制 pro/con 评估引入 degenerate scoring（26% 问题无法有效区分）。7B 模型无法可靠生成平衡的对立约束——pro 约束系统性多于 con（94 pro vs 65 con），confirmation bias 从约束提取转移到了约束生成。\\n3. **Debate (catastrophic)**: Proposer/Critic/Defense 多角色链在 7B 模型上导致答案质量严重退化。辩论不仅未增加多样性，反而引入了角色扮演的额外认知负担。同模型辩论 = 同源性 + 角色扮演退化，双重损失。\\n\\n**Scale limitation caveat**: 所有方法测试在 7B 模型上。7B 模型生成 Z3 格式 FOL 约束的能力不足（ICG 多题 \\\"0/N constraints parsed\\\"）。14B+ 模型可能有不同结果——这既是 limitation 也是 future work 入口。\\n\\n### κ Generalization — Independence-Accuracy Trade-off (D075, CAPSTONE FINDING)\\n\\nexp-077 测量三种聚合方式在 Mistral-7B FOLIO-204 上的 κ 和 Eff-K：\\n| 聚合方式 | Fleiss' κ | Eff-K | 名义 K |\\n|----------|----------|-------|--------|\\n| Self-Consistency | 0.4384 | 2.02 | 10 |\\n| Diverse-Prompt | 0.4030 | 2.21 | 12 |\\n| LLM-Debate | 0.1549 | 4.44 | 12 |\\n\\n结合 exp-076 Debate Δ=-18.6pp 的准确率数据，揭示**同模型框架下的 fundamental independence-accuracy trade-off**：\\n- **SC/Diverse-Prompt**: κ~0.4，traces 高度相关但准确率正常。换 prompt 策略不改善独立性（Δκ=0.04）。\\n- **Debate**: κ=0.15，成功打破 trace 相关性（Eff-K 从 2.0 跃升到 4.4），但准确率崩溃 -18.6pp。低 κ 不代表\\\"更独立的推理\\\"——是 disagreement amplification（系统性噪声）。\\n- **Trade-off 本质**: 同一模型的推理能力是固定的。要么输出一致（高 κ, 正确但不独立），要么输出分歧（低 κ, 独立但不正确）。Condorcet Jury Theorem 要求 both independent AND accurate，同模型框架下无法同时满足。\\n\\n**论文叙事升级**: 从 \\\"methods fail\\\" → \\\"independence-accuracy trade-off is fundamental to same-model reasoning\\\"。突破瓶颈需要跨模型方案（不同模型天然更独立），Oracle 实验（gold FOL 来自外部知识源）已间接验证了这一点。\\n\\n### New Claim 6 (D070/D074)\\n\\n6. **Method-Level Interventions Cannot Break the Bottleneck**: 三种针对 independence bottleneck 不同环节的方法（ICG→循环依赖, Contrastive→confirmation bias, Debate→trace 同质性）在 2 个数据集上全部失败。加上之前 9 种 prompt-level 修复，共 12 种修复尝试全败。这证明 independence bottleneck 不是单一环节的问题，而是 same-model self-extraction 的根本性限制。\\n\\n### New Claim 7: Symbolic Confirmation Bias (D082 — CORE FINDING)\\n\\n7. **Symbolic Confirmation Bias**: LLM 从 CoT traces 提取的 FOL 约束系统性确认 trace 自身（可能错误的）答案，而非独立验证 ground truth。\\n   - SICA 判对题：gold constraint 78.1%，bias ratio = 0.28\\n   - SICA 判错题：错误 constraint 83.3%，bias ratio = **4.97×**\\n   - 97.6% SICA 错误与 SC 错误完全重合\\n   - SICA 翻盘的 12 例来自 minority trace diversity（43% gold support），不是 symbolic reasoning\\n   - **因果链**：模型推理→答案→从含答案 trace 提取 FOL→约束确认答案→聚合≈SC\\n   - **CEGIS 验证**：迭代精炼 R1 +3.43pp < 原始 SICA +4.9pp → 约束一致性不是瓶颈，偏向性才是\\n   - **Quality Ladder 验证**：L1 ≈ L0 << L3 → bottleneck 在 traces（同源输入），不在 extractor\\n\\n### New Claim 8: Process-κ (D082 — NEW METRIC)\\n\\n8. **Process-Level Independence (Process-κ)**: answer-κ 低估真实独立性瓶颈。CoT 推理过程相似性远高于答案一致性。\\n   - Mistral-7B FOLIO-204：CoT cosine similarity **0.69** >> answer-κ **0.41**\\n   - 两者几乎无相关性：r = -0.06, p = 0.36\\n   - 仅 **9.3%** trace 对是\\\"殊途同归\\\"（同答案不同路径）\\n   - answer-κ 是 true independence bottleneck 的 lower bound\\n   - 适用于所有 LLM trace aggregation 方法，不限于 SICA\\n\\n## D082/D085: Comprehensive Method Exhaustion — 25+ ALL Fail\\n\\nD080 启动全方向并行探索（Wave 1-3），在 D074 的 12 种修复基础上又测试 13+ 新干预：\\n\\n| 方法 | 类型 | 结果 | 关键数据 |\\n|------|------|------|----------|\\n| PROVE 代码验证 | paradigm shift | ❌ | Code gen 15.2%, accuracy=random |\\n| CEGIS 迭代精炼 | multi-round | ❌ | R1 +3.43pp < SICA +4.9pp |\\n| DeepConf 置信度 | filtering | ❌ | logprob 与正确性零相关 |\\n| Cross-model SICA | cross-model | ❌ | Δ=-0.49pp despite lower κ |\\n| Problem Perturbation | input diversity | ❌ | κ 升至 0.696 (反效果) |\\n| MIN-UNSAT | solver objective | ❌ | 49.5% < SC 54.4% |\\n| κ-aware SC | voting rule | ❌ | 11/11 Δ=0 |\\n| Z3 Trace Filter | trace filtering | ❌ | negative |\\n| Bootstrapped Gold | iterative | ❌ | negative |\\n| Selective Abstention | diagnostic | ⚡ | AUROC=0.673, +4.4pp@80%cov |\\n\\n**D085 总结**: 9 prompt-level + 3 method-level + 13 新方向 = **25+ 干预全部 negative**。Independence bottleneck 在 same-model self-extraction 框架下无解，所有维度（diversity/architecture/capability/verification/filtering/voting/solver/paradigm）已穷尽。\\n\\n## D090: Cross-Architecture External Verification — POSITIVE BREAKTHROUGH\\n\\n### New Claim 9: Cross-Architecture NLI Verification Breaks the Bottleneck\\n\\n9. **Cross-Architecture External Verification**: A lightweight encoder-only NLI model (microsoft/deberta-large-mnli) provides structurally complementary signal to decoder-only LLMs.\\n   - DeBERTa standalone: 49.51% (101/204) — not competitive alone, expected\\n   - **NLI+SC combo w=1 (NLI as 13th voter): 57.84% (118/204), +3.43pp vs SC** ← PRIMARY (has McNemar)\\n   - NLI+SC combo w=3: 58.82% (120/204), +4.41pp vs SC — McNemar p=0.078 NOT significant (b=6, c=15). Higher weight amplifies NLI weakness on Unknown.\\n   - NLI+SC combo w=5: 60.29% (+5.88pp) — Reviewer: w=5 overfitting risk, NOT main result\\n   - NLI∩SC agreement subset: 68.48% accuracy on 45% coverage — selective verification evidence\\n   - NLI-as-verifier (trust NLI on disagreement): 49.51% — FAILED (NLI only 34% correct when disagreeing)\\n   - SC baseline: 54.41% (111/204, primary Mistral-7B FOLIO eval, seed=None)\\n   - **McNemar (w=1 ONLY)**: p=0.039, significant at α=0.05. 9 discordant pairs (b=1, c=8). 95% CI [0.59pp, 6.28pp]. ⚠️ w=3 and w=5 McNemar NOT YET COMPUTED — do NOT attribute this p-value to other weights\\n   - **Model**: microsoft/deberta-large-mnli, **406M** parameters (not 350M, not 44M)\\n   - **Per-label complementarity (key insight)**:\\n     - False (contradiction): NLI **71.43%** vs SC 38.10% → NLI dominates (+33pp)\\n     - Unknown: NLI 18.84% vs SC **68.12%** → SC dominates (+49pp)\\n     - True: NLI 59.72% vs SC 55.56% → NLI slightly better\\n   - **Why it works**: DeBERTa is encoder-only + NLI fine-tuned → strong at contradiction detection (its training task). LLM is strong at uncertainty reasoning. Structurally complementary error profiles.\\n   - **Oracle connection**: Oracle (+14.22pp) proved aggregation works with quality constraints; DeBERTa provides partial external signal → partial oracle effect\\n   - **Narrative**: \\\"25+ same-model interventions fail, but even a simple cross-architecture voter provides modest positive signal — proof-of-concept for external architectural complementarity\\\"\\n\\n### New Claim 10: Constraint-Answer Decoupling — CONDITIONAL on full results (D092)\\n\\n10. **Constraint-Answer Decoupling (G)**: Removing conclusion sentences from reasoning traces before FOL extraction causally breaks Symbolic Confirmation Bias.\\n   - **⚠️ INTERMEDIATE results only (70/204 = 34%)**: 65.7% accuracy (+11.3pp vs SC 54.41%, +6.4pp vs SICA 59.31%)\\n   - Avg truncation ratio: **4.1%** — removing ~4% of trace text yields +11pp improvement\\n   - **Causal mechanism**: trace contains conclusion → FOL extractor reads conclusion → extracted constraints confirm conclusion → aggregation ≈ SC. G cuts this chain by removing the conclusion before extraction.\\n   - **Potential strengths**: (a) largest positive effect in the project, (b) minimal intervention (4.1% text removal), (c) directly tests the confirmed mechanism (confirmation bias)\\n   - **Risk (Reviewer critical)**: FOLIO 难度分布不均匀，前 70 题可能偏简单。历史先例：Direction F 42%→39.6%，Direction H 56.1%→微降。中间值可能虚高。\\n   - **Residual bias risk**: 即使截断显式结论，推理步骤仍可能暗示答案方向（\\\"the premises suggest...\\\"），extraction 模型仍可能产生 biased constraints。\\n   - **Full results pending**: PID 384984 on westd-16639, running to 204/204\\n   - **McNemar**: pending full results\\n   - **Narrative (if confirmed)**: \\\"25+ methods fail because they don't break the answer→constraint coupling. G directly severs this coupling via conclusion truncation — the diagnosis drives the fix.\\\"\\n\\n### Framing Decision Threshold (Reviewer-approved)\\n- G ≥+5pp AND p<0.05 → **commit V3** (G+R dual method, G as core)\\n- G +3-5pp AND p<0.10 → **V3 weak** (G as \\\"encouraging pilot\\\", not core method)\\n- G <+3pp OR n.s. → **fall back to V2** (R proof-of-concept) or **V1** (pure negative)\\n\\n### Updated Headline Result (D092 — V3 CONDITIONAL, awaiting G full results)\\n\\n\\\"Across 6+ models and 4 domains, symbolic consensus aggregation shows no statistically significant positive effect under same-model self-extraction. 25+ interventions fail. Root cause: Symbolic Confirmation Bias (4.97×). Two independent cures both succeed: (1) Constraint-Answer Decoupling removes conclusion sentences before FOL extraction, cutting the causal chain — +11.3pp (70/204 intermediate, PENDING FULL); (2) Cross-architecture NLI verification (DeBERTa) provides structurally complementary signal — +4.41pp (p=0.039). Both validate the diagnosis from orthogonal angles: G attacks the information flow, R attacks the architectural homogeneity.\\\"\\n\\n### Updated Headline Result (D090 — V2 FALLBACK, if G full results weaker than intermediate)\\n\\n\\\"Across 6+ models and 4 domains, symbolic consensus aggregation shows no statistically significant positive effect under same-model self-extraction. 25+ interventions fail. Root cause: Symbolic Confirmation Bias (4.97×). A cross-architecture proof-of-concept (DeBERTa NLI w=3) achieves +4.41pp (p=0.039) — the only positive result across 25+ attempts. Per-label analysis reveals structural complementarity: NLI dominates contradiction detection (71% vs SC 38%), while LLMs dominate uncertainty reasoning (68% vs NLI 19%).\\\"\\n\\n### Updated Story Spine (D092 — V3, G+R dual method)\\n\\n- **Problem**: [unchanged]\\n- **Theoretical lens**: [unchanged]\\n- **Systematic evaluation**: [unchanged]\\n- **Regime characterization**: [unchanged]\\n- **Remediation failures strengthen thesis (D085 FINAL)**: 9 prompt-level + 3 method-level + 13 new directions = **25+ interventions** across ALL dimensions (diversity/architecture/capability/verification/filtering/voting/solver/paradigm), all fail → bottleneck is fundamental and exhaustively proven\\n- **Method failure analysis**: Three methods targeting different bottleneck aspects show three distinct failure modes (neutral/harmful/catastrophic), revealing that the bottleneck operates at multiple levels simultaneously\\n- **Independence-accuracy trade-off (HERO FINDING, D075)**: Debate breaks trace correlation (κ 0.44→0.15, Eff-K 2.0→4.4) but accuracy collapses (-18.6pp/-23.0pp). Same-model traces can be independent OR accurate, not both.\\n- **Symbolic Confirmation Bias (CORE FINDING, D082)**: Root cause identified — self-extracted FOL constraints systematically confirm the trace's own answer (bias ratio 4.97× on incorrect problems). Causal chain: model reasons → answer → FOL extraction confirms answer → aggregation ≈ SC. This is WHY 25+ methods fail.\\n- **Process-κ (NEW METRIC, D082)**: CoT reasoning similarity (0.69) >> answer-κ (0.41), r=-0.06. Only 9.3% of trace pairs are \\\"convergent reasoning.\\\" answer-κ underestimates the true bottleneck. Novel metric applicable to all LLM trace aggregation.\\n- **NEW — Constraint-Answer Decoupling (CORE METHOD, D092)**: Having diagnosed the causal chain (conclusion→FOL→bias), we sever it: remove conclusion sentences before extraction. 4.1% text removal → +11.3pp (70/204). Minimal intervention, maximal effect. Directly proves the mechanism IS the cause.\\n- **NEW — Cross-Architecture Verification (COMPLEMENTARY METHOD, D092)**: DeBERTa NLI (406M) w=1 **+3.43pp (p=0.039, McNemar exact)** PRIMARY; w=3 +4.41pp (p=0.078 n.s.); NLI∩SC 68.48%@45%. Orthogonal fix: instead of fixing the extraction pipeline, add an architecturally independent voter. Per-label complementarity (NLI: False 71% vs SC 38%; SC: Unknown 68% vs NLI 19%).\\n- **Dual cure narrative**: G attacks information flow (removes biased input to extractor), R attacks architectural homogeneity (adds independent voter). Both work independently. Validates diagnosis from two angles.\\n- **Actionable contribution**: C0+SC diagnostic + κ-based Eff-K estimation + Decoupling method + NLI combo = complete toolkit from diagnosis to fix.\\n- **Universal across architectures (D078)**: Three families: Mistral-7B κ=0.438, LLaMA-8B κ=0.412, Qwen2.5-7B κ=0.658, Qwen2.5-14B κ=0.738. Family effect (Δκ=0.22) >> scale effect (Δκ=0.08).\\n- **Headline (D092)**: Independence bottleneck is structural to same-model extraction, universal across architectures, rooted in Symbolic Confirmation Bias. 25+ same-model interventions fail. Two independent cures succeed: Decoupling (+11.3pp, CONDITIONAL on full 204) attacks the causal chain, Cross-Architecture NLI (+3.43pp, p=0.039) provides external diversity. Both prove the diagnosis and provide practical solutions.\\n\\n## Core Insight (D060 Updated — Dual Bottleneck)\\n\\n**Dual Requirement Framework**: SICA 效应需要同时满足两个条件，缺一不可：\\n1. **Sufficient Independence** (Eff-K > threshold): traces 需要提供足够多的独立视角\\n2. **Sufficient Quality** (SC > ~50%): traces 需要有足够的正确率，否则约束是噪声\\n\\nCondorcet Jury Theorem 要求投票者独立且 p>0.5。同模型采样的 reasoning traces 严重违反独立性假设（Fleiss' κ = 0.21–0.82，Eff-K 仅 1.20–3.63），解释了为什么简单增加 K 或添加符号约束不能突破 SC 的天花板。\\n\\n实验数据完美支持 dual requirement（κ 使用统一脚本 compute_fleiss_kappa_unified.py，SC/Δpp 使用 registry 原始值）：\\n- **Qwen family**: κ=0.66-0.82, Eff-K≈1.20-1.46（独立性不足）→ all near-zero delta，无论 SC 多高\\n- **Mistral-7B FOLIO**: κ≈0.46, Eff-K≈2.0（中等独立性）+ SC≈55%（中等质量）→ +3.43pp best seed, mean +2.12pp (2/3 seeds positive, 1 null)\\n- **Mistral-7B PW-600**: κ=0.20, Eff-K=3.76（最高独立性）但 SC=39%（质量不足）→ -2.83pp\\n- 只有 Goldilocks zone（中等 Eff-K + 中等 SC）出现正向 delta\\n- **Dual bottleneck 直接验证 (exp-055)**：Multi-temp κ=0.427 Eff-K=2.11（比单温度 κ≈0.46 Eff-K≈2.0 更独立）但 delta=0.00pp → 提高 independence 不够，还需要 extraction quality\\n- **T sensitivity 孤立尖峰 (4/4 complete, D064 corrected)**：T=0.3(Δ=-1.47), T=0.5(Δ=-0.98), T=0.7(Δ=+3.43, κ=0.460, Eff-K=1.98), T=1.0(Δ=0.00, κ=0.394, Eff-K=2.25)。T=0.7 孤立尖峰更突出。T=0.7 SC=55.88%（最低）→ entropy 最高 → SICA 操作空间最大。温度效应与 SC 效应互为 confound，论文需讨论\\n- **Thinking mode κ=0.913, Eff-K=1.09 (exp-028b)**：近乎确定性。思维模式让 traces 更一致 → 独立性更差。\\\"更好的推理\\\"反而加剧 independence bottleneck。\\n\\n**κ 是 model-level 稳定属性**：统一处理后 Mistral 三 seed κ 收敛至 0.457-0.460（之前 0.41-0.50 差异是非标准 answer 处理的 artifact）。κ 跨 seed 几乎相同，但 delta 差异大（+3.43 vs +2.94 vs 0.00）→ seed-level constraint quality variance 主导，非 κ。\\n\\n完整 κ 表（⚠️ D062: κ 将用 raw answers 重算，当前 unified 值为临时值。Qwen 无变化，Mistral 条件将更新）：\\n| Exp | Model | κ(unified→raw pending) | Eff-K | SC%(registry) | Δpp(registry) |\\n|-----|-------|------------|-------|---------------|---------------|\\n| exp-028b | Qwen3-14B thinking | 0.913 | 1.09 | ~84% | ~0 |\\n| exp-038 | Qwen-14B LogiQA | 0.821 | 1.20 | 78.50 | -0.50 |\\n| exp-027 | Qwen3-14B | 0.773 | 1.26 | 84.31 | +0.49 |\\n| exp-036 | Qwen2.5-14B | 0.744 | 1.31 | 75.49 | +0.25 |\\n| exp-035 | Qwen2.5-7B | 0.658 | 1.46 | 76.47 | -0.49 |\\n| exp-049b | Mistral-7B LogiQA | 0.512 | 1.81 | 51.00 | +0.50 |\\n| exp-057 | Mistral-7B T=0.3 | 0.502 | 1.84 | 58.33 | -1.47 |\\n| exp-058 | Mistral-7B T=0.5 | 0.516 | 1.80 | 58.33 | -0.98 |\\n| exp-033 | Mistral-7B s42 | 0.460 | 1.98 | 55.88 | +3.43 |\\n| exp-052 | Mistral-7B s123 | 0.457 | 1.99 | 54.41 | +2.94 |\\n| exp-053 | Mistral-7B s456 | 0.457 | 1.99 | 55.88 | 0.00 |\\n| exp-055 | Mistral-7B multi-T | 0.427 | 2.11 | 57.84 | 0.00 |\\n| exp-054 | Mistral-7B T=1.0 | 0.394 | 2.25 | 55.39 | 0.00 |\\n| exp-046 | Mistral-7B PW-600 | 0.200 | 3.76 | 39.33 | -2.83 |\\n注：κ 基于 T/F/U 三类归一化，Mistral-7B 约 12-16% traces 被归一化（Qwen 100% valid）。Mistral SC/Δpp 已更新为 D064 tiebreaking 修正值；Qwen 不受影响。\\n\\nOracle control (+14.22pp) 证明 MAX-SAT 聚合机制本身有效，但自提取约束仅利用了 24% 的理论上限。Discriminative filtering 实验揭示关键机制：~92% 约束 ARE discriminative，但过滤掉 ~8% non-discriminative 约束后 delta 不变（0 gains）。问题不在约束缺乏判别力，而在于 discriminative constraints 的区分方向与模型偏差一致（confirmation bias）。\\n\\n**Remediation insight (D060)**: 9 种修复尝试全部失败，包括直接靶向 independence（multi-temp diversity, exp-055: Eff-K 从 2.0→2.11 但 delta 仍为 0）和 constraint quality（discriminative filtering）。这证明 bottleneck 不是简单的 diversity 或 quality 问题，而是 same-model self-extraction 的根本性限制。\\n\\n**Key evidence**:\\n- **Condorcet independence quantification (统一脚本, 公式: Eff-K=K/(1+(K-1)κ))**: Mistral-7B FOLIO κ≈0.46 (Eff-K≈2.0, 三 seed 高度稳定), Mistral-7B PW-600 κ=0.200 (Eff-K=3.76), Qwen2.5-14B FOLIO κ=0.744 (Eff-K=1.31), Qwen2.5-14B LogiQA κ=0.821 (Eff-K=1.20), Qwen3-14B κ=0.773 (Eff-K=1.26), Qwen2.5-7B κ=0.658 (Eff-K=1.46). 跨模型清晰: Qwen Eff-K≈1.2-1.5→0 gain, Mistral FOLIO Eff-K≈2.0→variable gain, Mistral PW Eff-K=3.76 but SC too low→negative. κ stable across seeds (0.457-0.460), delta varies → seed-level constraint quality dominates.\\n- **Oracle control (exp-031)**: Gold FOL + MAX-SAT = 89.71% vs SC 75.49% (+14.22pp, p=2.0e-7). Unknown-type +31.9pp.\\n- **Two-layer constraint analysis**: 43% trivially_satisfied (taxonomy: satisfied by ALL answers) vs ~8% non-discriminative (filtering: same MAX-SAT score). Difference: trivially_satisfied constraints can still have different satisfaction DEGREES. Removing the 8% yields 0 gains → problem is not quality but confirmation bias direction.\\n- **K sensitivity (non-monotonic peak at K=12, 5/5 complete, D064+D066)**: K=4(-1.47pp), K=8(-1.96pp), K=12(+3.43pp p=0.092 ns), K=16(+1.47pp), K=20(+1.96pp). Peak at K=12, drops at K=16 but partially recovers at K=20. NOT clean inverted-U. K=12 SC=55.88% (post-fix). SC-confound with T sensitivity still holds. SICA at K=4 vs K=12 differs by ~4.9pp despite similar SC — proves SICA extracts different information than SC.\\n- **SC-confound (cross-cutting insight)**: K=12 和 T=0.7 都是 SC 最低 (54.41%) 的配置 → SICA \\\"最佳超参\\\"可能反映 entropy/operating-window 效应而非 K 或 T 的因果贡献。论文需要讨论这个 confound，但也可以正面利用：SC level 是更基本的预测变量，K 和 T 通过影响 SC 来间接影响 SICA delta。\\n- **T sensitivity (isolated peak, 4/4 complete, D064 corrected)**: T=0.3(Δ=-1.47pp), T=0.5(Δ=-0.98pp), T=0.7(Δ=+3.43pp p=0.092 ns), T=1.0(Δ=0.00pp). NOT smooth inverted-U — T=0.7 is an isolated spike. T=0.7 has lowest SC (55.88%) → highest entropy → largest SICA operating window. Temperature and SC effects confounded. Strengthens fragility narrative.\\n- **Regime boundary**: Qwen-14B (SC=75.49%) Δ=-0.98pp vs Mistral-7B (SC=55.88%) Δ=+3.43pp p=0.092 ns\\n- **Type C failure (exp-046)**: Mistral PW-D5 SC=39.33%, Δ=-2.83pp, p=0.010, κ=0.210, Eff-K=3.63, contradiction rate 5.5%. Highest Eff-K yet worst delta → independence alone insufficient when SC too low.\\n- **Seed replication (D064+D066)**: 2/3 seeds positive but **0/3 significant** after tiebreaking correction: s42 Δ=+3.43pp p=0.092, s123 Δ=+2.94pp p=0.070, s456 Δ=0.00pp p=1.0. Mean +2.12pp. Only significant McNemar effects are NEGATIVE: exp-046 Δ=-2.83pp p=0.014, exp-039 Δ=-2.50pp p=0.011. Paper must frame as \\\"positive directional trend\\\" not \\\"significant positive effect\\\".\\n- **Nine remediation failures (ALL CONFIRMED)**: contrastive prompting, cross-model, generational scaling, solver-guided, consistency filtering, cross-trace UNSAT, discriminative filtering (0 gains), T=1.0 (delta collapse +3.43→0.00pp, D064 corrected), multi-temp (delta=+0.00pp, b=5 c=5). All 9 failed → trap is fundamental, bottleneck is structural.\\n- **Entropy decomposition (VERIFIED 2026-05-19)**: High-entropy proportion: Mistral FOLIO 38% (78/204) vs Qwen FOLIO 18% (37/204) vs Qwen LogiQA 12% (23/200). SICA on high-entropy: Mistral FOLIO s42 +12.8pp, s123 +9.1pp, s456 -1.3pp; Qwen FOLIO -8.2pp; all others negative. Low-entropy: SICA≈SC across all 8 experiments (Δ≈0). Entropy decomposition reveals regime-dependent mechanism, NOT universal diagnostic.\\n- **Confirmation bias quantification**: ⚠️ \\\"62.3%\\\" and \\\"28.6%\\\" confirmed NOT present in any .tex file — likely hallucinated in earlier draft. DO NOT USE. Replace with verified metrics from experiment outputs only.\\n\\n## Story Spine (D059 Updated)\\n\\n- **Problem**: LLMs' reasoning can be improved by sampling multiple chains-of-thought and aggregating via majority voting (self-consistency). Recent work proposes symbolic augmentation: extract formal constraints from traces and use SAT solvers for answer selection. But does symbolic aggregation actually outperform simple voting?\\n- **Theoretical lens**: Condorcet Jury Theorem requires voter independence. We quantify trace independence via Fleiss' κ and show Effective-K << nominal K. This explains the fundamental limitation of same-model trace aggregation.\\n- **Systematic evaluation**: SICA (MAX-SAT over FOL constraints) across 3 domains × 5 model families. Oracle control separates extraction vs aggregation failure. Discriminative filtering reveals ~92% constraints are discriminative, yet SICA gains are fragile — confirmation bias, not constraint quality, is the bottleneck.\\n- **Regime characterization**: Three failure modes (Type A/B/C) + narrow Goldilocks zone. C0+SC as deployment diagnostic.\\n- **Remediation failures strengthen thesis**: 9 targeted interventions (prompting, architecture, capability, verification, diversity, filtering) all fail to close the oracle gap, proving the bottleneck is fundamental to same-model self-extraction.\\n- **Headline result (D066 McNemar corrected)**: \\\"Across 6 models and 4 domains, symbolic consensus aggregation shows no statistically significant positive effect under corrected tiebreaking (best seed +3.43pp, p=0.092). The only significant effects are negative (PW-600: -2.83pp p=0.014, -2.50pp p=0.011). However, entropy decomposition reveals a striking regime-dependent pattern: SICA's entire effect concentrates on high-entropy questions, with +12.8pp in the Goldilocks zone but -2 to -8pp elsewhere. Oracle constraints prove the aggregation mechanism works (+14.22pp, p<0.001), localizing the bottleneck to extraction quality (24% utilization). Condorcet analysis (Eff-K=1.2-2.0 for nominal K=12) explains trace non-independence. Nine remediation strategies all fail, confirming the bottleneck is structural to same-model self-extraction.\\\"\\n\\n## Anticipated Reviewer Concerns & Defensive Experiments\\n\\n1. **\\\"Gains not statistically significant\\\"** → Correct: no positive effect reaches significance (best p=0.092). This IS the finding. Oracle p=2.0e-7 proves the mechanism works; the insignificance of self-extraction gains demonstrates the extraction bottleneck. Regime pattern (8 entropy conditions) provides systematic evidence beyond any single p-value.\\n2. **\\\"Only one positive result (exp-033)\\\"** → Seed replication: 2/3 positive (s42 +3.43pp, s123 +2.94pp), 1/3 null (s456 0.00pp). Mean +2.12pp. Effect IS real but fragile — the fragility itself IS the finding.\\n3. **\\\"Condorcet framework is trivial\\\"** → Fleiss' κ quantification is novel in SC/SICA context. Eff-K is actionable: tells practitioners how many truly independent traces they get.\\n4. **\\\"Multi-temp / filtering should work\\\"** → We tried both. Multi-temp (exp-055): negative. Disc. filtering: 0 gains. T=1.0: delta collapse. These failures STRENGTHEN the structural bottleneck thesis.\\n5. **\\\"Only Qwen models\\\"** → 5 families: Qwen-14B, Mistral-7B, LLaMA-8B, DeepSeek-R1-7B, QwQ-32B.\\n6. **\\\"Only logic domain\\\"** → FOLIO + ProofWriter + LogiQA + StrategyQA + ARC-Challenge. Type B (domain formalizability) is itself a finding.\\n7. **\\\"Oracle is unfair comparison\\\"** → Diagnostic tool, not competing method. Separates extraction from aggregation.\\n8. **\\\"MAX-SAT is over-engineering\\\"** → exp-013: MaxSAT ≈ count-only. This IS the independence bottleneck evidence.\\n9. **\\\"Self-extraction confound\\\"** → Oracle control resolves completely.\\n10. **\\\"Published methods achieve gains (DyLoS, Aristotle, FoVer)\\\"** → Different paradigm (external verifiers/trained extractors). We characterize same-model self-extraction.\\n11. **\\\"C0 is trivially derived\\\"** → Zero-cost early stopping. Practical value.\\n12. **\\\"Why not just use a reasoning model?\\\"** → QwQ-32B: C0<5%, SICA≡SC.\\n13. **\\\"Random tiebreak baseline\\\"** → exp-003: SICA tiebreak 80% vs random 50%.\\n14. **\\\"Method improvement is incremental\\\"** → Grounded in diagnosis (independence + taxonomy), not ad-hoc.\\n15. **\\\"Weighted SC is simpler\\\"** → exp-016 planned. Weighted SC doesn't address independence.\\n16. **\\\"Within-model ICL transition contradicts regime theory\\\"** → exp-050b (SC=57.79%, Δ=-3.52pp): ICL changes trace generation characteristics, not just SC level. Paper must distinguish \\\"same model, different prompt\\\" from \\\"same model, same prompt, different accuracy.\\\"\\n\\n## Working Title (D092 V3 — G+R dual method)\\n**\\\"Breaking Symbolic Confirmation Bias: Constraint-Answer Decoupling and Cross-Architecture Verification for LLM Logical Reasoning\\\"**\\n(Alternatives:\\n- \\\"Two Cures for One Disease: Decoupling and Architectural Diversity Against Symbolic Confirmation Bias in LLM Reasoning\\\"\\n- \\\"The Independence Bottleneck in Symbolic LLM Reasoning: Diagnosis, 25+ Failed Interventions, and Two Independent Solutions\\\"\\n- V2 fallback (R only): \\\"Breaking the Self-Consistency Ceiling: How Cross-Architecture Verification Overcomes Symbolic Confirmation Bias in LLM Reasoning\\\"\\n- V1 fallback (pure negative): \\\"Beyond Self-Consistency: How Trace Independence Limits Symbolic Consensus in LLM Reasoning\\\")\\n\\nNOTE (Dream D037): Title MUST be scoped to \\\"self-extracted constraints\\\" / \\\"SICA\\\". Published methods (DyLoS, Aristotle, FoVer) use different approaches.\\n\\n## Paper Structure (D092 V3 — EMNLP 8pp + appendix)\\n\\n### Sections\\n- §1 Introduction: 25+ same-model interventions all fail → independence bottleneck → two independent cures\\n- §2 Related Work: SC, neuro-symbolic, Condorcet/voting, verification\\n- §3 Diagnostic Framework: Independence Bottleneck (Eff-K, process-κ), Oracle Gap\\n- §4 Symbolic Confirmation Bias: bias ratio 4.97×, overlap 94%, causal chain\\n- §5 Method 1: Constraint-Answer Decoupling (G) — core method, detailed\\n- §6 Method 2: Cross-Architecture NLI Verification (R) — complementary method\\n- §7 Combined Analysis: G+R combo, ablation, cross-dataset if available\\n- §8 Discussion + Conclusion\\n\\n### Main Tables\\n- T1: Main Results — models × domains, SC% / SICA% / Δpp / p-value, regime boundary\\n- T2: Oracle Control — Gold-FOL+MAX-SAT vs SC vs SICA-self, causal separation\\n- T3: Independence Quantification — Fleiss' κ / Eff-K / trace agreement per model\\n- T4: Confirmation Bias — bias ratio per condition, overlap rate, per-label breakdown\\n- T5: Decoupling Results (G) — SC / SICA / G-Decoupled, Δpp, McNemar, per-label\\n- T6: NLI Verification Results (R) — SC / NLI standalone / combo w=1,3 / intersection, Δpp, McNemar\\n- T7: 25+ Intervention Summary — method / type / dataset / result / failure mode (compact)\\n\\n### Main Tables (continued)\\n- T6: Method-Level Intervention Results — 3 methods × 2 datasets, SC% / Method% / Δpp, failure mode classification\\n- T7: κ Generalization — SC / Debate / Diverse-Prompt κ and Eff-K (from exp-077, pending)\\n\\n### Main Figures\\n- F1: Method Pipeline (SICA + oracle control design)\\n- F2: SC Accuracy vs SICA Δ scatter (hero figure, regime boundary)\\n- F3: K Sensitivity with diversity metrics (K vs Δ, K vs Eff-K)\\n- F4: Extraction error breakdown (stacked bar)\\n- F5: Method intervention failure modes (grouped bar: ICG/Contrastive/Debate × FOLIO/LogiQA)\\n\\n### Appendix\\n- K ablation details, temperature sensitivity, per-domain results, overhead analysis\\n- Entropy-conditioned analysis (continuous scatter + bin sensitivity)\\n- Six remediation strategy details\\n- Confirmation bias quantification\\n- Seed replication analysis\\n- QwQ-32B / DeepSeek-R1 negative control\\n\\n## Claim Risk Notes (D059)\\n- **Seed replication**: 0/3 significant after D066 correction (p=0.092, 0.070, 1.0). 2/3 positive trend, 1/3 null. Mean +2.12pp. Frame as \\\"directional trend, not significant effect\\\" — fragility IS the finding.\\n- **Method claims DEAD (D060)**: All three method improvements failed. Paper is pure analysis. 9 remediation failures are EVIDENCE, not limitation.\\n- **Condorcet novelty**: ✅ VERIFIED. arXiv:2409.00094 applies CJT to cross-model LLM ensembles (different angle). No prior work applies Fleiss' κ or Eff-K to within-model SC traces. Our framing is novel.\\n- **exp-050b complication**: ICL transition Δ=-3.52pp at SC=57.79% complicates simple \\\"SC determines SICA.\\\" Explain via trace generation characteristic change.\\n- **Variable naming inconsistency**: 56.4% cross-trace pairs share zero Z3 variables. Key mechanism evidence.\\n\\n## Required Citations (minimum 30 references)\\n\\n- **SC & extensions**: Wang et al. 2023 (SC), Chen et al. 2023 (USC), Loo et al. 2025 (SC scaling plateaus), Taubenfeld et al. 2025 (weighted SC), DiVeRSe (Li et al. 2023)\\n- **Neuro-symbolic reasoning**: DyLoS (EACL 2026), Aristotle (ACL 2025), FoVer (TACL 2025), LogicAgent (2025), Logic-LM (Pan et al. 2023), LINC (Olausson et al. 2023)\\n- **Condorcet/voting theory**: Condorcet 1785, Austen-Smith & Banks 1996, **arXiv:2409.00094 (Examining Independence in Ensemble Sentiment Analysis, Sept 2024)** — closest prior work, applies CJT to cross-model LLM ensembles, finds independence violation. Our novelty: within-model trace independence + Fleiss' κ quantification + Eff-K + connection to symbolic aggregation\\n- **Test-time compute**: Snell et al. 2025, DeepSeek-R1, Diversity-Aware Training\\n- **Verification & reranking**: ORM (Cobbe et al. 2021), PRM (Lightman et al. 2023), Math-Shepherd\\n- **Constraint satisfaction**: SATBench (EMNLP 2025), LLM Meets Constraint Propagation (IJCAI 2025)\\n- **Debate & multi-agent**: Liang et al. 2023, Du et al. 2023\\n\\n## Additional Reviewer Concerns (D070/D074 Methods)\\n\\n17. **\\\"Why not use a larger model for constraint generation?\\\"** → Valid. All methods tested at 7B scale. ICG constraint parsing failures + Debate role-play degradation may be scale-dependent. This is explicitly noted as limitation and future work. The contribution is diagnosing the bottleneck and showing it's not trivially fixable, not claiming no fix exists at any scale.\\n18. **\\\"Only tested one model (Mistral-7B) for methods\\\"** → Methods are interventions on the extraction pipeline, not the base model. Testing on the same model that showed the clearest Goldilocks signal (Mistral-7B FOLIO) is the strongest test — if methods can't improve the best-case scenario, they won't help elsewhere.\\n19. **\\\"ICG multi-seed shows 1/3 positive\\\"** → Magnitudes (-2.0, +1.5, -1.0) are within SC baseline noise (3.5pp cross-seed). Mean ≈-0.5pp, std=1.8pp. No statistical significance. Properly framed as \\\"noise-level, neither improving nor degrading.\\\"\\n20. **\\\"Debate working in other papers\\\"** → Multi-agent debate literature uses diverse models or much larger models. Same-model 7B debate is a different regime. Our finding is specifically about same-model self-extraction limitations.\\n\\n## Claim Scoping Rules\\n- n=60 conditions: \\\"suggestive/consistent with\\\" NOT \\\"confirming\\\"\\n- n≥200 conditions: can \\\"confirm\\\"\\n- Combined N>1,300: acceptable if breakdown clearly stated\\n- Method claims: must show statistically significant improvement OR clear directional improvement with analysis\\n- \\\"Independence bottleneck\\\" framing: systematic quantification + theoretical grounding\\n\\n## V16 Frontier Model Extension (D135–D139)\\n\\n### New Claim 11: SCB is Universal — 7B to Frontier (D135)\\n\\nSymbolic Confirmation Bias persists across ALL tested models, from 7B open-source to frontier closed-source:\\n\\n| Model | Extraction | SC% | SICA% | Δpp | BR(mean) | BR=∞ rate | Process-κ | Answer-κ |\\n|-------|-----------|-----|-------|-----|----------|-----------|-----------|----------|\\n| Mistral-7B | self | 55.88 | 59.31 | +3.43 | 4.97 | 30% | 0.69* | 0.46 |\\n| LLaMA-8B | self | — | — | — | 2.88 | — | — | — |\\n| Qwen-14B | self | 75.49 | 75.74 | +0.25 | 3.93 | — | — | 0.74 |\\n| R1-Distill-8B | cross→Mistral | 74.51 | 76.96 | +2.45 | 2.92 | — | 0.248 | 0.69 |\\n| gpt-4o | self | 73.91 | 72.05 | -1.86 | 2.94 | 44% | 0.79 | 0.80 |\\n| gpt-4.1 | cross→Mistral | 82.84 | 81.37 | -1.47 | 2.70 | 58% | 0.792 | 0.86 |\\n| gpt-5.5 | cross→Mistral | 84.31 | 84.80 | +0.49(n.s.) | 3.48 | 87% | 0.563 | 0.96 |\\n| o3 | cross→Mistral | 82.65 | 82.65 | 0.00 | 1.66 | 82% | 0.596 | 0.92 |\\n| Gemini-2.5-Pro* | cross→Mistral | 87.37 | 86.32 | -1.05 | 2.79 | — | 0.790 | 0.75 |\\n\\n*Gemini: 95/204 interim. Mistral Process-κ is CoT cosine sim (different metric from cross-model TF-IDF κ).\\n\\nBR > 1 across ALL models (1.66–4.97×). BR=∞ rates high in frontier models (44–87%).\\nTable footnote MUST distinguish self vs cross extraction context.\\n\\n### New Claim 12: Process-κ Gradient Predicts Cross-Model Extraction Effectiveness (D137–D139)\\n\\nCross-model extraction (Mistral-7B extracts FOL from other models' traces) effectiveness is monotonically predicted by Process-κ:\\n\\n| Model | Process-κ | Δ(SICA-SC) | BR(mean) |\\n|-------|-----------|------------|----------|\\n| R1-Distill | 0.248 | +2.45pp ✓ | 2.92 |\\n| gpt-5.5 | 0.563 | +0.49pp(n.s.) | 3.48 |\\n| o3 | 0.596 | 0.00pp | 1.66 |\\n| Gemini-2.5-Pro* | 0.790 | -1.05pp | 2.79 |\\n| gpt-4.1 | 0.792 | -1.47pp | 2.70 |\\n\\n**Spearman ρ(κ→Δ) = -1.0, n=5, one-tailed p=0.0083** (statistically significant).\\n\\n**Paper language constraints (D138)**:\\n- Use \\\"decreases monotonically\\\" — NOT \\\"predictive\\\" or \\\"significant correlation\\\"\\n- Dual-variable framing: \\\"two necessary conditions\\\" (qualitative mechanism), NOT regression model\\n  - Low κ (diverse traces) → cross-model extractor can contribute novel constraints\\n  - High BR (strong self-bias) → there IS bias to escape from\\n  - Both conditions required: o3 (BR=1.66, near-unbiased) → Δ=0 despite moderate κ=0.596\\n- o3 BR=1.66 is observation (\\\"bimodal error pattern: 82% BR=∞ but low finite-BR\\\"), NOT sub-finding\\n- BR=∞ ordering does NOT strictly follow \\\"model capability\\\" (o3 82% < gpt-5.5 87%). Drop ordering claim.\\n\\n### Updated Headline (V16)\\n\\n\\\"Symbolic Confirmation Bias is universal from 7B open-source to frontier closed-source models (BR 1.66–4.97×). Cross-model extraction effectiveness decreases monotonically with Process-κ (ρ=-1.0, n=5, p=0.008), modulated by bias severity: gain requires both diverse traces (low κ) AND substantial self-bias (high BR). 25+ same-model interventions fail; two cross-architecture cures succeed.\\\"\\n\\n### V16 Paper Structure Impact\\n\\n- §4 SCB: Add frontier model BR table (Table 4 or expanded T4)\\n- §3 or new §: Process-κ gradient analysis (Table + scatter plot)\\n- §1 Intro: Scale claim upgraded from \\\"7B-32B\\\" to \\\"7B to frontier\\\"\\n- Limitations: Update \\\"7B to 32B parameters\\\" scope claim\\n- New Figure: Process-κ vs Δ scatter with dual-variable annotation (5 points + regression-free narrative)\\n\", \"total_chars\": 40785, \"truncated\": false}, \"error\": null, \"metadata\": {}}"
    }
  }
}
```

</details>

---

### Assistant

_source line 16_

<details><summary>Logged reasoning block</summary>

```text
The registry query for exp-090 and exp-048 returned empty. The experiments might use different ID formats. Let me search the full registry dump for NLI/combo related experiments. Let me also read the large registry output file. Let me search for specific terms in the registry and look at the artifacts directory.

The paper_framing.md has extensive detail. Key things about NLI:
- NLI+SC combo w=1: 57.84% (118/204), +3.43pp vs SC (has McNemar p=0.039)
- NLI+SC combo w=3: 58.82% (120/204), +4.41pp vs SC — McNemar p=0.078 NOT significant


- NLI+SC combo w=5: 60.29% (+5.88pp)
- SC baseline: 54.41% (111/204)

There's a discrepancy here. The paper claims Mistral-7B w=3 NLI combo shows +6.67pp with p<0.001, but the registry exp-090 records +3.50pp with p=0.0125, and paper_framing.md shows +4.41pp with p=0.078. None of these match each other.

I need to track down where the +6.67pp figure comes from and verify whether exp-090 actually exists in the registry. Let me search through the registry file for relevant keywords like "nli", "combo", "090", and "wave3", and check the artifacts directory for the nli_multi_verifier_recomputed.json file.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "259e8c74-cee8-43ee-8c2a-b39b28aafca2",
  "uuid": "6405bf35-ff71-43aa-abfd-e30eed5e066d",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GadASt6nKhBRZLmyN4cYKb",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 18726,
      "cache_read_input_tokens": 24834,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 18726
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

_source line 17_

exp-090 和 exp-048 在 registry 查询返回空。让我搜索 registry 大文件和 artifacts 目录。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "259e8c74-cee8-43ee-8c2a-b39b28aafca2",
  "uuid": "219392d5-efc5-4759-8223-21aab43ec70b",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GadASt6nKhBRZLmyN4cYKb",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 18726,
      "cache_read_input_tokens": 24834,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 18726
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

_source line 18_

<details open><summary>🔧 Tool call — Bash · `toolu_01XnKuj1zFdeetHpnyc15Soq`</summary>

```json
{
  "command": "cat /home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0513-3-projects-symb-invariant-consensus/259e8c74-cee8-43ee-8c2a-b39b28aafca2/tool-results/mcp-agent-ml-research-read_registry-1779461485443.txt | python3 -c \"\nimport json, sys\ndata = json.loads(json.loads(sys.stdin.read())['result'])\nexps = data['data']['experiments']\n# Search for NLI, combo, cross-arch, deberta, wave3, 090, 048\nkeywords = ['nli', 'combo', 'cross-arch', 'deberta', 'wave3', 'wave3-dir-r', '090', '048', '+6.67', '+3.50', '6.67', '3.50']\nfor exp_id, exp_data in exps.items():\n    exp_str = json.dumps(exp_data, default=str).lower()\n    for kw in keywords:\n        if kw.lower() in exp_str:\n            print(f'=== {exp_id} matches [{kw}] ===')\n            print(json.dumps(exp_data, indent=2, default=str)[:2000])\n            print('---')\n            break\n\" 2>&1 | head -500",
  "description": "Search registry for NLI/combo/deberta related experiments"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "259e8c74-cee8-43ee-8c2a-b39b28aafca2",
  "uuid": "cd5bb0ec-6964-42e9-b6c8-86558508908b",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GadASt6nKhBRZLmyN4cYKb",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 18726,
      "cache_read_input_tokens": 24834,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 18726
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

_source line 19 · 2026-05-22T14:51:46.018Z_

<details><summary>↩ Tool result · `toolu_01XnKuj1zFdeetHpnyc15Soq`</summary>

```text
=== exp-multi-seed-llama-pw matches [048] ===
{
  "status": "PREPARING",
  "hypothesis": "Multi-seed replication (seeds 42,123,456) of LLaMA-3.1-8B \u00d7 ProofWriter-600 adds cross-dataset evidence for the third model family. If \u0394(SICA-SC)\u22640 holds on PW as well as FOLIO, it confirms SCB is dataset-invariant within LLaMA-8B. Addresses W4 reviewer concern.",
  "notes": "PID 614142 on westd-16639 cuda:3 port 8004. vLLM PID 613151 (LLaMA-3.1-8B, max-model-len=8192, max_tokens=2048). 3-seed sequence: 42\u2192123\u2192456. Each seed ~600 problems. Model: /root/autodl-tmp/models/Meta-Llama-3.1-8B-Instruct. Script: scripts/multiseed_llama8b_pw_cuda3.sh",
  "metrics": {
    "pw_seed42": {
      "status": "running",
      "progress": "60/600"
    },
    "pw_seed123": {
      "status": "pending"
    },
    "pw_seed456": {
      "status": "pending"
    }
  }
}
---
=== exp-multi-seed-llama-folio matches [048] ===
{
  "status": "PREPARING",
  "hypothesis": "Multi-seed replication (seeds 123,456,789) of LLaMA-3.1-8B \u00d7 FOLIO-204 shows consistent \u0394(SICA-SC) direction across seeds, adding a third model family (beyond Qwen2.5 and Mistral) for cross-family consistency evidence. Addresses W4 reviewer concern.",
  "notes": "PID 596151 on westd-16639 cuda:1 port 8002. vLLM PID 595261 (max-model-len=8192, max_tokens=2048). Previous attempt failed: max-model-len=4096 caused HTTP 400 on all requests. Fixed by increasing to 8192 + reducing max_tokens to 2048. ~70s/prob, 3 seeds sequential, ETA ~12h (~23:00 UTC May 22). Output: results/multi_seed/llama8b_folio_seed{123,456,789}/",
  "metrics": {
    "seed123": {
      "sc_acc": 67.16,
      "sica_acc": 63.73,
      "delta": -3.43,
      "n": 204,
      "extraction_rate": 0.959,
      "status": "COMPLETE"
    },
    "seed456": {
      "status": "running",
      "progress": "125/204"
    },
    "seed789": {
      "status": "pending"
    }
  }
}
---
=== exp-multi-seed-mistral-pw matches [6.67] ===
{
  "status": "PREPARING",
  "hypothesis": "Multi-seed replication (seeds 42,123,456,789) of Mistral-7B \u00d7 ProofWriter-600 shows consistent \u0394(SICA-SC) direction across seeds, confirming single-seed results are not artifacts of random sampling. Addresses W4 reviewer concern about reproducibility.",
  "notes": "PID 510987 on westd-16639 cuda:2 port 8003. Running 4-seed sequence (42\u2192123\u2192456\u2192789). Note: seed=42 is being re-run (should have used existing baseline), wasting ~4.5h. Each seed ~4.5h (600q \u00d7 27s). Total ETA ~18h. Cron registered (600s). Output: results/multi_seed/mistral_pw_seed{X}/results.json",
  "metrics": {
    "pw_seed42": {
      "sc_acc": 40,
      "sica_acc": 36.67,
      "delta": -3.33,
      "n": 600,
      "status": "COMPLETE"
    },
    "pw_seed123": {
      "sc_acc": 40.8,
      "sica_acc": 37.5,
      "delta": -3.3,
      "n": 600,
      "status": "COMPLETE"
    },
    "pw_seed456": {
      "status": "running",
      "progress": "43/600"
    },
    "pw_seed789": {
      "status": "pending"
    }
  }
}
---
=== exp-d134-cil matches [nli] ===
{
  "status": "PREPARING",
  "hypothesis": "CIL (Cumulative Information Lift) unifies combo gain prediction: CIL>0 iff verifier adds independent signal beyond generator. Cross-architecture NLI pairs show CIL>0 (predicting significant combo gain), while same-model SICA shows CIL\u22480 (predicting no gain), validating CIL as the mechanistic criterion for escape.",
  "conclusion": "success",
  "metrics": {
    "n_pairs_computed": 8,
    "n_pairs_missing": 2,
    "spearman_rho": 0.881,
    "spearman_p": 0.0039,
    "pearson_r": 0.8481,
    "pearson_p": 0.0078,
    "cil_deberta_mistral_pw": 1.67,
    "cil_sica_mistral_pw": -4.61,
    "cil_deberta_qwen14b_pw": -0.21,
    "cil_sica_qwen14b_pw": -4.21,
    "corrected_v2": "Qwen14B canonical SC=74.00% (exp032). Gains: DeBERTa +0.33pp, SICA -2.50pp. Spearman 0.881 p=0.004."
  }
}
---
=== exp-d126-drc-folio matches [nli] ===
{
  "status": "PREPARING",
  "hypothesis": "DRC (Disagreement-Routed Cascade) with DeBERTa NLI verification on FOLIO-204 recovers \u226580% of full NLI combo gain at \u226450% verification cost, extending the ProofWriter DRC result to a second dataset and demonstrating the generality of disagreement-based routing.",
  "conclusion": "success",
  "metrics": {
    "sc_acc": 55.88,
    "full_combo_w3_acc": 58.82,
    "drc_tau07_w3_acc": 58.33,
    "drc_tau07_gain_pp": 2.45,
    "drc_tau07_nli_calls": "71/204",
    "drc_tau07_cost_pct": 34.8,
    "drc_tau07_gain_recovery_pct": 83.3,
    "drc_tau08_w3_acc": 58.82,
    "drc_tau08_gain_recovery_pct": 100,
    "drc_tau08_cost_pct": 48.5
  }
}
---
=== exp-092-llama8b-pw-nli-combo matches [nli] ===
{
  "status": "DONE",
  "hypothesis": "LLaMA-3.1-8B ProofWriter NLI combo: DeBERTa-large-MNLI standalone (55%) < SC (70%)\uff0ccapability gap = -15pp\u3002\u9a8c\u8bc1 NLI combo \u662f\u5426\u5728\u7b2c\u4e8c\u4e2a model family \u4e0a\u4e5f\u80fd\u63d0\u5347 SC accuracy\u3002",
  "conclusion": "success",
  "metrics": {
    "n": 600,
    "sc_accuracy": 0.7,
    "nli_standalone": 0.55,
    "capability_gap_pp": -15,
    "combo_w1": 0.7283,
    "combo_w3": 0.7417,
    "combo_w5": 0.7167,
    "delta_w1_pp": 2.83,
    "delta_w3_pp": 4.17,
    "delta_w5_pp": 1.67,
    "mcnemar_w1_p": 0.0001,
    "mcnemar_w3_p": 0.0035,
    "mcnemar_w5_p": 0.4335,
    "nli_correct_sc_wrong": 120,
    "sc_correct_nli_wrong": 210
  }
}
---
=== exp-091-qwen14b-pw-nli-combo matches [nli] ===
{
  "status": "DONE",
  "hypothesis": "Qwen2.5-14B ProofWriter NLI combo: DeBERTa-large-MNLI standalone (55%) < SC (73.50%)\uff0ccapability gap = -18.50pp\u3002\u6839\u636e Push A capability gap \u5355\u8c03\u5173\u7cfb\uff0ccombo gain \u5e94\u4ecb\u4e8e Qwen3 (+1.83pp) \u548c Mistral (+10.67pp) \u4e4b\u95f4\u3002",
  "conclusion": "success",
  "metrics": {
    "n": 600,
    "sc_accuracy": 0.735,
    "nli_standalone": 0.55,
    "capability_gap_pp": -18.5,
    "combo_w1": 0.7417,
    "combo_w3": 0.7433,
    "combo_w5": 0.7533,
    "delta_w1_pp": 0.67,
    "delta_w3_pp": 0.83,
    "delta_w5_pp": 1.83,
    "mcnemar_w1_p": 0.344,
    "mcnemar_w3_p": 0.405,
    "mcnemar_w5_p": 0.144
  }
}
---
=== exp-090-r-nli-proofwriter matches [nli] ===
{
  "status": "DONE",
  "hypothesis": "Cross-architecture NLI verification (DeBERTa-large-MNLI) \u5728 ProofWriter-D5 \u4e0a\u4e5f\u80fd\u63d0\u5347 SC accuracy\uff0c\u9a8c\u8bc1 FOLIO \u4e0a R \u65b9\u6cd5\u7684\u8de8\u6570\u636e\u96c6\u6cdb\u5316\u80fd\u529b\u3002\u6765\u6e90: R5-N4 \u5ba1\u7a3f\u4fee\u590d + Claim 1 (cross-architecture escape generalization)\u3002",
  "conclusion": "success",
  "metrics": {
    "n": 600,
    "sc_accuracy": 0.3933,
    "sica_accuracy": 0.365,
    "nli_standalone": 0.55,
    "combo_w1": 0.4017,
    "combo_w3": 0.4283,
    "combo_w5": 0.5,
    "delta_w1_pp": 0.83,
    "delta_w3_pp": 3.5,
    "delta_w5_pp": 10.67,
    "mcnemar_w1_p": 0.2668,
    "mcnemar_w1_b": 4,
    "mcnemar_w1_c": 9,
    "mcnemar_w3_p": 0.0125,
    "mcnemar_w3_b": 22,
    "mcnemar_w3_c": 43,
    "mcnemar_w5_p": 0.0001,
    "mcnemar_w5_b": 35,
    "mcnemar_w5_c": 99,
    "nli_true_acc": 0.64,
    "nli_false_acc": 0.975,
    "nli_unknown_acc": 0.035,
    "nli_correct_sc_wrong": 274,
    "sc_correct_nli_wrong": 180,
    "agreement_acc": 0.808
  }
}
---
=== exp-wave3-dir-r-nli-verifier matches [nli] ===
{
  "status": "DONE",
  "hypothesis": "DeBERTa External Verifier: encoder-only NLI \u6a21\u578b (cross-encoder/nli-deberta-v3-base) \u4e0e decoder-only LLM \u67b6\u6784\u72ec\u7acb\uff0c\u4f5c\u4e3a\u989d\u5916 vote \u52a0\u5165 SC traces \u53ef\u6253\u7834 confirmation bias\u3002NLI \u64c5\u957f contradiction \u68c0\u6d4b\uff08False label\uff09\uff0cLLM \u64c5\u957f Unknown \u63a8\u7406\uff0c\u4e24\u8005\u4e92\u8865\u3002",
  "metrics": {
    "sc_accuracy": 0.5441,
    "nli_standalone": 0.4951,
    "combo_w1": 0.5784,
    "combo_w3": 0.5882,
    "intersection_acc": 0.6848,
    "intersection_coverage": 0.451,
    "delta_w1_pp": 3.43,
    "delta_w3_pp": 4.41,
    "mcnemar_w1_p": 0.0391,
    "mcnemar_w1_b": 1,
    "mcnemar_w1_c": 8,
    "mcnemar_w3_p": 0.0784,
    "mcnemar_w3_b": 6,
    "mcnemar_w3_c": 15,
    "ci95_w1": [
      0.98,
      6.37
    ],
    "ci95_w3": [
      0,
      8.82
    ],
    "nli_false_acc": 0.7143,
    "sc_false_acc": 0.381,
    "nli_unknown_acc": 0.1884,
    "sc_unknown_acc": 0.6812,
    "model_nli": "microsoft/deberta-large-mnli",
    "n": 204
  },
  "conclusion": "success"
}
---
=== exp-wave3-dir-r-combo-extended matches [nli] ===
{
  "status": "DONE",
  "hypothesis": "R combo \u7b56\u7565\u6269\u5c55\uff1a\u6d4b\u8bd5 NLI \u4f5c\u4e3a\u4e0d\u540c\u6743\u91cd\u6295\u7968\uff08w=1/3/5\uff09\u3001intersection+fallback\u3001cascade\uff08\u6309 NLI confidence \u5206\u6d41\uff09\u3001weighted averaging \u7b49\u7b56\u7565\u3002\u5bfb\u627e NLI+SICA/SC \u6700\u4f18\u878d\u5408\u65b9\u5f0f\u3002",
  "conclusion": "success",
  "metrics": {
    "sc_accuracy": 0.5441,
    "sica_accuracy": 0.5931,
    "nli_standalone": 0.4951,
    "best_combo": "nli_sc_vote_w5",
    "best_combo_acc": 0.6029,
    "best_delta_sc_pp": 5.88,
    "best_delta_sica_pp": 0.98,
    "nli_sc_vote_w3": 0.5882,
    "intersection_sica_fallback": 0.5931,
    "intersection_sc_fallback": 0.5735,
    "oracle_upper_bound": 0.7549,
    "sica_nli_agreement": 0.475,
    "agreement_accuracy": 0.701,
    "n": 204
  }
}
---
=== exp-022-oracle-proofwriter matches [6.67] ===
{
  "status": "DONE",
  "hypothesis": "ProofWriter oracle: gold DSL (raw_logic_programs) \u901a\u8fc7 Z3 consistency checking \u52a0\u6743 K=12 traces\uff0cOracle-SICA \u5e94\u663e\u8457\u8d85\u8d8a SC \u548c SICA(self)\uff0c\u5728 ProofWriter 600 \u9898\u4e0a\u590d\u73b0 FOLIO oracle (+8.82pp) \u7684 extraction bottleneck \u7ed3\u8bba\u3002",
  "conclusion": "success",
  "metrics": {
    "n": 600,
    "k": 12,
    "oracle_sica_accuracy": 0.8667,
    "sc_accuracy": 0.7517,
    "sica_self_accuracy": 0.755,
    "oracle_vs_sc_delta_pp": 11.5,
    "mcnemar_p_oracle_vs_sc": 9.21e-15,
    "z3_gold_agreement": 0.9714,
    "z3_gold_agree_n": 577,
    "z3_gold_total": 594,
    "parse_errors": 6,
    "parse_error_rate": 0.01,
    "solver_errors": 0,
    "solver_total": 7128,
    "relneg_oracle": 0.7786,
    "relneg_sc": 0.6,
    "relneg_delta_pp": 17.86,
    "relnoneg_oracle": 0.7945,
    "relnoneg_sc": 0.6644,
    "relnoneg_delta_pp": 13.01,
    "attnoneg_oracle": 0.961,
    "attnoneg_sc": 0.8701,
    "attnoneg_delta_pp": 9.09,
    "attneg_oracle": 0.9188,
    "attneg_sc": 0.85,
    "attneg_delta_pp": 6.87,
    "model": "Qwen2.5-14B-Instruct",
    "dataset": "ProofWriter-OWA-D5-600",
    "constraint_source": "gold DSL (raw_logic_programs)"
  },
  "notes": "KEY RESULT. ProofWriter Oracle-SICA (gold DSL + Z3 + MAX-SAT) 86.67% vs SC 75.17% vs SICA(self) 75.50%, +11.50pp, McNemar p=9.21e-15 \u6781\u663e\u8457\u3002Z3 gold agreement 97.14% (577/594), parse errors \u4ec5 6/600 (1%), solver errors 0/7128\u3002Per-subtype: RelNeg +17.86pp > RelNoneg +13.01pp > AttNoneg +9.09pp > AttNeg +6.87pp\u2014\u2014\u5173\u7cfb\u8c13\u8bcd\uff08\u63a8\u7406\u94fe\u66f4\u957f\uff09\u83b7\u76ca\u8fdc\u5927\u4e8e\u5c5e\u6027\u8c13\u8bcd\u3002\u4e0e FOLIO oracle (exp-021, +8.82pp, p=6.15e-5) \u5bf9\u6bd4\uff1aProofWriter delta \u66f4\u5927 (+11.50 vs +8.82) \u4e14\u7edf\u8ba1\u663e\u8457\u6027\u9ad8 6 \u4e2a\u6570\u91cf\u7ea7\u3002\u4e24\u4e2a\u5b50\u57df Oracle \u5b9e\u9a8c\u4e00\u81f4\u8bc1\u660
---
=== exp-012-gsm8k-pilot matches [6.67] ===
{
  "status": "DONE",
  "hypothesis": "Cross-domain validation: Qwen2.5-14B-Instruct \u5728 GSM8K (\u5f00\u653e\u7b54\u6848\u6570\u5b66\u57df) 30 \u9898\u4e0a SICA vs SC\u3002\u9884\u671f C0<20%\uff0814B \u5728 GSM8K \u592a\u5f3a\uff09\uff0c\u9a8c\u8bc1 C0 \u4f5c\u4e3a SICA \u65e0\u6548\u6027\u9884\u6d4b\u6307\u6807\u3002",
  "metrics": {
    "n": 30,
    "k": 12,
    "sica_accuracy": 0.9667,
    "sc_accuracy": 0.9667,
    "delta_pp": 0,
    "multi_candidate_rate": 0.133,
    "extraction_success_rate": 0.147,
    "model": "Qwen2.5-14B-Instruct",
    "dataset": "GSM8K",
    "temperature": 0.7
  },
  "conclusion": "negative",
  "notes": "GSM8K 30\u9898\uff1aSICA=SC=96.67%\uff0cdelta=0\uff0cC0=13.3%\u3002\u5f00\u653e\u7b54\u6848\u6570\u5b66\u57df baseline \u6781\u9ad8\uff0896.67%\uff09\uff0c\u51e0\u4e4e\u65e0 diversity\uff08C0=13.3%\uff09\uff0cextraction_success_rate \u4ec5 14.7%\u2014\u2014\u6570\u5b66\u57df\u7684 symbolic constraints \u96be\u4ee5\u63d0\u53d6\u3002\u652f\u6301 C0 \u4f5c\u4e3a SICA \u65e0\u6548\u6027\u9884\u6d4b\u6307\u6807\u3002"
}
---
=== temperature-ablation-t05 matches [6.67] ===
{
  "status": "DONE",
  "hypothesis": "Temperature ablation T=0.5: \u4e2d\u6e29\u4e0b Qwen2.5-14B trace diversity \u4e2d\u7b49\uff08C0 \u9884\u671f 30-45%\uff09\uff0cSICA-SC gap \u9884\u671f\u22480\u2014\u2014\u9a8c\u8bc1\u5373\u4f7f diversity \u9002\u4e2d\uff0cconstraint quality \u4ecd\u4e3a\u74f6\u9888",
  "notes": "T=0.5 \u4e2d\u6e29\uff1aC0=38.3%\uff0cSICA=SC=76.67%\uff0cdelta=0\uff0cdiscordant=0\u3002\u4e2d\u7b49 diversity \u4e0b SICA \u4ecd\u5b8c\u5168\u7b49\u4e8e SC\u3002",
  "metrics": {
    "n": 60,
    "k": 12,
    "sica_accuracy": 0.7667,
    "sc_accuracy": 0.7667,
    "delta_pp": 0,
    "multi_candidate_rate": 0.383,
    "discordant_total": 0,
    "model": "Qwen2.5-14B-Instruct",
    "dataset": "D012",
    "temperature": 0.5
  },
  "conclusion": "negative"
}
---
=== exp-010-mistral-v3 matches [6.67] ===
{
  "status": "DONE",
  "hypothesis": "Cross-family validation: Mistral-7B-Instruct-v0.3 \u5728 D012 \u6570\u636e\u96c6(30PW+30FOLIO)\u4e0a\u662f\u5426\u590d\u73b0 SICA\u2248SC pattern\u2014\u2014\u9a8c\u8bc1 capability trap \u8de8\u6a21\u578b\u5bb6\u65cf\u6cdb\u5316\uff08v3: \u811a\u672c\u5185\u542b vLLM \u6e05\u7406+conda \u73af\u5883\uff0c\u89e3\u51b3 v2 SIGTERM \u95ee\u9898\uff09",
  "metrics": {
    "n": 60,
    "k": 12,
    "sica_accuracy": 0.4833,
    "sc_accuracy": 0.4833,
    "delta_pp": 0,
    "multi_candidate_rate": 0.5,
    "extraction_rate": 0.8819,
    "answer_extraction_rate": 1,
    "contradiction_rate": 0.0562,
    "discordant_sica_wins": 2,
    "discordant_sc_wins": 2,
    "mcnemar_p": 1,
    "proofwriter_sica": 0.4,
    "proofwriter_sc": 0.4,
    "proofwriter_delta_pp": 0,
    "folio_sica": 0.5667,
    "folio_sc": 0.5667,
    "folio_delta_pp": 0,
    "truncated_traces": 0,
    "model": "Mistral-7B-Instruct-v0.3",
    "dataset": "D012"
  },
  "conclusion": "negative",
  "notes": "Mistral-7B cross-family: SICA 48.33% = SC 48.33%, delta=0.00pp\u3002Multi-candidate rate 50%\uff0830/60 \u9898\u975e unanimous\uff09\uff0cSICA \u4ec5\u6539\u53d8 4 \u9898\uff086.67% flip rate\uff09\u3002\u6a21\u578b\u592a\u5f31\uff1aSC baseline 48.33%\uff08\u8fd1\u968f\u673a\uff09\uff0ctrace \u7f3a\u4e4f\u8d28\u91cf\u4f46\u6709\u591a\u6837\u6027\u3002Discordant 2:2 \u5e73\u5c40\uff0cMcNemar p=1.0\u3002\u652f\u6301 operating regime \u6709\u4e0b\u754c\uff1a\u6a21\u578b\u5fc5\u987b\u8db3\u591f\u5f3a\u624d\u80fd\u751f\u6210\u6709\u610f\u4e49\u7684 diverse traces\u3002PW 40%/40%, FOLIO 56.67%/56.67%\u3002"
}
---
=== exp-019-llama8b-strategyqa-200 matches [+6.67] ===
{
  "status": "DONE",
  "hypothesis": "Powered test: SICA \u5728\u5f31\u6a21\u578b\uff08LLaMA-3.1-8B\uff09\u4e0a\u7684\u589e\u76ca\u5728 n=200 StrategyQA \u9898\u65f6\u8fbe\u5230\u7edf\u8ba1\u663e\u8457\uff08p<0.05\uff09\u2014\u2014\u9a8c\u8bc1 operating regime \u5047\u8bbe\uff08D031 + exp-011 directionally positive +6.67pp\uff09",
  "metrics": {
    "n": 200,
    "k": 12,
    "sica_accuracy": 0.74,
    "sc_accuracy": 0.72,
    "delta_pp": 2,
    "multi_candidate_rate": 0.41,
    "mcnemar_p": 0.424,
    "bootstrap_ci_95": [
      -1.5,
      5.5
    ],
    "bootstrap_p_delta_le_0": 0.12,
    "discordant_sica_wins": 9,
    "discordant_sc_wins": 5,
    "discordant_total": 14,
    "discordant_rate": 0.07,
    "sc_unanimous_rate": 0.545,
    "model": "LLaMA-3.1-8B-Instruct",
    "dataset": "StrategyQA",
    "wall_time_min": 52
  },
  "conclusion": "negative",
  "notes": "StrategyQA 200\u9898 powered test: SICA 74% vs SC 72%, +2.00pp, McNemar p=0.424, bootstrap CI [-1.5, +5.5] \u8de8\u96f6\u3002\u7edf\u8ba1\u4e0d\u663e\u8457\u3002exp-011 \u7684 +6.67pp \u5728\u6269\u5927\u6837\u672c\u540e\u7f29\u6c34 70%\u2014\u2014\u5c0f\u6837\u672c\u566a\u58f0\u3002\u5173\u952e\u53d1\u73b0\uff1a(1) LLaMA-8B \u5728 StrategyQA \u4e0a SC=72%\uff0c\u9ad8\u4e8e\u9884\u671f\u7684 sweet spot (55-65%)\uff0c(2) \u4ec5 14/200 (7%) discordant pairs\uff0c54.5% \u5168\u7968\u4e00\u81f4\uff0c(3) SICA \u4ec5\u5145\u5f53 tiebreaker\uff089 wins \u4e2d 6 \u4e2a\u662f\u5e73\u7968\uff09\u3002StrategyQA \u4e0d\u5728 operating regime sweet spot \u5185\u3002exp-020 FOLIO (SC\u224860%) \u662f\u771f\u6b63\u7684 definitive test\u3002"
}
---
=== exp-018-arc-v2 matches [6.67] ===
{
  "status": "DONE",
  "hypothesis": "Cross-domain validation: Qwen2.5-14B-Instruct \u5728 ARC-Challenge (\u79d1\u5b66\u591a\u9009, ABCD) \u4e0a SICA vs SC\u2014\u2014\u9a8c\u8bc1 capability trap \u662f\u5426\u8de8\u4efb\u52a1\u7c7b\u578b\u6cdb\u5316\uff08v2: build_generator bug \u5df2\u4fee\u590d\uff09",
  "conclusion": "success",
  "metrics": {
    "n": 60,
    "k": 12,
    "sica_accuracy": 0.95,
    "sc_accuracy": 0.9667,
    "delta_pp": -1.67,
    "multi_candidate_rate": 0.05,
    "extraction_rate": 1,
    "contradiction_detected": 3,
    "discordant_sica_wins": 0,
    "discordant_sc_wins": 1,
    "dataset": "ARC-Challenge",
    "model": "Qwen2.5-14B-Instruct"
  },
  "notes": "ARC-Challenge cross-domain: SICA 95.00% vs SC 96.67%, gap=-1.67pp. SICA \u7565\u900a\u4e8e SC\u3002\u6a21\u578b\u5728 ARC \u4e0a baseline \u6781\u9ad8(96.67%)\uff0c\u63a5\u8fd1\u5929\u82b1\u677f\u2014\u2014\u9ad8\u51c6\u786e\u7387\u533a\u95f4\u591a\u6837\u6027\u4f4e\uff0cSICA \u65e0\u64cd\u4f5c\u7a7a\u95f4\u3002\u4e0e StrategyQA (+3.33pp n.s.) \u5bf9\u6bd4\uff1a\u7b80\u5355\u4efb\u52a1\uff08\u9ad8 baseline\uff09SICA \u65e0\u6548\u6216\u6709\u5bb3\uff0c\u4e2d\u7b49\u96be\u5ea6\u4efb\u52a1\u6709\u5fae\u5f31\u6b63\u5411\u8d8b\u52bf\u4f46\u4e0d\u663e\u8457\u3002\u6574\u4f53\u652f\u6301 capability trap\uff1a\u6a21\u578b\u80fd\u529b\u8d8a\u5f3a/\u4efb\u52a1\u8d8a\u7b80\u5355 \u2192 SC \u5df2\u8fd1\u6700\u4f18 \u2192 SICA \u65e0\u589e\u91cf\u3002"
}
---
=== exp-011-llama8b-v3 matches [+6.67] ===
{
  "status": "DONE",
  "hypothesis": "Cross-family validation: LLaMA-3.1-8B-Instruct \u5728 D012 \u6570\u636e\u96c6(30PW+30FOLIO)\u4e0a\u662f\u5426\u590d\u73b0 SICA\u2248SC pattern\u2014\u2014\u9a8c\u8bc1 capability trap \u975e Qwen-specific\uff08v3: \u6a21\u578b shard \u5df2\u4fee\u590d\uff0cGPU \u7a7a\u95f2\u540e\u63d0\u4ea4\uff09",
  "conclusion": "success",
  "metrics": {
    "n": 60,
    "k": 12,
    "sica_accuracy": 0.6667,
    "sc_accuracy": 0.6,
    "delta_pp": 6.67,
    "multi_candidate_rate": 0.6167,
    "extraction_rate": 0.8556,
    "answer_extraction_rate": 0.8958,
    "contradiction_rate": 0.0527,
    "problems_with_contradictions": 43,
    "truncated_traces": 44,
    "discordant_sica_wins": 5,
    "discordant_sc_wins": 1,
    "mcnemar_p": 0.2188,
    "proofwriter_sica": 0.6333,
    "proofwriter_sc": 0.6,
    "proofwriter_delta_pp": 3.33,
    "folio_sica": 0.7,
    "folio_sc": 0.6,
    "folio_delta_pp": 10,
    "model": "LLaMA-3.1-8B-Instruct",
    "dataset": "D012",
    "wall_time_min": 66.4
  },
  "notes": "LLaMA-3.1-8B cross-family: SICA 66.7% vs SC 60.0%, +6.67pp (\u6700\u5927\u589e\u76ca)\u3002Discordant 5:1 \u5f3a\u70c8\u503e\u5411 SICA\u3002FOLIO +10pp, PW +3.33pp\u3002McNemar p=0.22\uff08n=60 \u53d7\u9650\uff09\u3002Multi-candidate rate 61.7%\uff08vs Qwen-14B 46%\uff09\u2014\u2014\u5f31\u6a21\u578b\u66f4\u591a\u6837\u2192SICA \u6709\u66f4\u5927\u64cd\u4f5c\u7a7a\u95f4\u300244 \u6761 truncated traces\uff08max-tokens \u53ef\u80fd\u504f\u77ed\uff09\uff0c\u4f46\u4ecd\u6709\u6548\u3002\u5173\u952e\uff1aSC baseline 60%\uff08\u8fdc\u4f4e\u4e8e Qwen-14B \u7684 76%\uff09\uff0c\u9a8c\u8bc1 capability trap \u7684\u6b63\u9762\u2014\u2014\u6a21\u578b\u5f31\u65f6 SICA \u6709\u7528\u3002"
}
---
=== exp-017-strategyqa-v3 matches [6.67] ===
{
  "status": "DONE",
  "hypothesis": "Cross-domain validation: Qwen2.5-14B-Instruct \u5728 StrategyQA (\u5e38\u8bc6\u63a8\u7406, Yes/No) \u4e0a SICA vs SC\u2014\u2014\u9a8c\u8bc1 capability trap \u662f\u5426\u8de8\u4efb\u52a1\u7c7b\u578b\u6cdb\u5316\uff08v3: \u4fee\u590d True/False\u2192Yes/No \u63d0\u53d6 bug\uff09",
  "conclusion": "success",
  "metrics": {
    "n": 60,
    "k": 12,
    "sica_accuracy": 0.5667,
    "sc_accuracy": 0.5333,
    "delta_pp": 3.33,
    "mcnemar_chi2": 0.5,
    "mcnemar_p": "n.s.",
    "bootstrap_ci_95": [
      0,
      8.33
    ],
    "bootstrap_p_delta_le_0": 0.1346,
    "multi_candidate_rate": 0.1,
    "contradiction_detected": 5,
    "extraction_rate_problem": 1,
    "extraction_rate_trace": 0.704,
    "discordant_sica_wins": 2,
    "discordant_sc_wins": 0
  },
  "notes": "StrategyQA\u8de8\u57df\u9a8c\u8bc1: SICA 56.67% vs SC 53.33%, +3.33pp n.s. (p=0.13), \u652f\u6301capability trap\u8de8\u4efb\u52a1\u6cdb\u5316; v3\u4fee\u590d\u63d0\u53d6bug\u786e\u8ba4\u6210\u529f(100%\u95ee\u9898\u7ea7\u63d0\u53d6\u7387); 2\u4e2adiscordant pairs\u5747SICA\u80dc\u51fa"
}
---
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "259e8c74-cee8-43ee-8c2a-b39b28aafca2",
  "uuid": "a57c3459-9d35-4eb6-a4cd-a711b0247220",
  "tool_use_result": {
    "stdout": "=== exp-multi-seed-llama-pw matches [048] ===\n{\n  \"status\": \"PREPARING\",\n  \"hypothesis\": \"Multi-seed replication (seeds 42,123,456) of LLaMA-3.1-8B \\u00d7 ProofWriter-600 adds cross-dataset evidence for the third model family. If \\u0394(SICA-SC)\\u22640 holds on PW as well as FOLIO, it confirms SCB is dataset-invariant within LLaMA-8B. Addresses W4 reviewer concern.\",\n  \"notes\": \"PID 614142 on westd-16639 cuda:3 port 8004. vLLM PID 613151 (LLaMA-3.1-8B, max-model-len=8192, max_tokens=2048). 3-seed sequence: 42\\u2192123\\u2192456. Each seed ~600 problems. Model: /root/autodl-tmp/models/Meta-Llama-3.1-8B-Instruct. Script: scripts/multiseed_llama8b_pw_cuda3.sh\",\n  \"metrics\": {\n    \"pw_seed42\": {\n      \"status\": \"running\",\n      \"progress\": \"60/600\"\n    },\n    \"pw_seed123\": {\n      \"status\": \"pending\"\n    },\n    \"pw_seed456\": {\n      \"status\": \"pending\"\n    }\n  }\n}\n---\n=== exp-multi-seed-llama-folio matches [048] ===\n{\n  \"status\": \"PREPARING\",\n  \"hypothesis\": \"Multi-seed replication (seeds 123,456,789) of LLaMA-3.1-8B \\u00d7 FOLIO-204 shows consistent \\u0394(SICA-SC) direction across seeds, adding a third model family (beyond Qwen2.5 and Mistral) for cross-family consistency evidence. Addresses W4 reviewer concern.\",\n  \"notes\": \"PID 596151 on westd-16639 cuda:1 port 8002. vLLM PID 595261 (max-model-len=8192, max_tokens=2048). Previous attempt failed: max-model-len=4096 caused HTTP 400 on all requests. Fixed by increasing to 8192 + reducing max_tokens to 2048. ~70s/prob, 3 seeds sequential, ETA ~12h (~23:00 UTC May 22). Output: results/multi_seed/llama8b_folio_seed{123,456,789}/\",\n  \"metrics\": {\n    \"seed123\": {\n      \"sc_acc\": 67.16,\n      \"sica_acc\": 63.73,\n      \"delta\": -3.43,\n      \"n\": 204,\n      \"extraction_rate\": 0.959,\n      \"status\": \"COMPLETE\"\n    },\n    \"seed456\": {\n      \"status\": \"running\",\n      \"progress\": \"125/204\"\n    },\n    \"seed789\": {\n      \"status\": \"pending\"\n    }\n  }\n}\n---\n=== exp-multi-seed-mistral-pw matches [6.67] ===\n{\n  \"status\": \"PREPARING\",\n  \"hypothesis\": \"Multi-seed replication (seeds 42,123,456,789) of Mistral-7B \\u00d7 ProofWriter-600 shows consistent \\u0394(SICA-SC) direction across seeds, confirming single-seed results are not artifacts of random sampling. Addresses W4 reviewer concern about reproducibility.\",\n  \"notes\": \"PID 510987 on westd-16639 cuda:2 port 8003. Running 4-seed sequence (42\\u2192123\\u2192456\\u2192789). Note: seed=42 is being re-run (should have used existing baseline), wasting ~4.5h. Each seed ~4.5h (600q \\u00d7 27s). Total ETA ~18h. Cron registered (600s). Output: results/multi_seed/mistral_pw_seed{X}/results.json\",\n  \"metrics\": {\n    \"pw_seed42\": {\n      \"sc_acc\": 40,\n      \"sica_acc\": 36.67,\n      \"delta\": -3.33,\n      \"n\": 600,\n      \"status\": \"COMPLETE\"\n    },\n    \"pw_seed123\": {\n      \"sc_acc\": 40.8,\n      \"sica_acc\": 37.5,\n      \"delta\": -3.3,\n      \"n\": 600,\n      \"status\": \"COMPLETE\"\n    },\n    \"pw_seed456\": {\n      \"status\": \"running\",\n      \"progress\": \"43/600\"\n    },\n    \"pw_seed789\": {\n      \"status\": \"pending\"\n    }\n  }\n}\n---\n=== exp-d134-cil matches [nli] ===\n{\n  \"status\": \"PREPARING\",\n  \"hypothesis\": \"CIL (Cumulative Information Lift) unifies combo gain prediction: CIL>0 iff verifier adds independent signal beyond generator. Cross-architecture NLI pairs show CIL>0 (predicting significant combo gain), while same-model SICA shows CIL\\u22480 (predicting no gain), validating CIL as the mechanistic criterion for escape.\",\n  \"conclusion\": \"success\",\n  \"metrics\": {\n    \"n_pairs_computed\": 8,\n    \"n_pairs_missing\": 2,\n    \"spearman_rho\": 0.881,\n    \"spearman_p\": 0.0039,\n    \"pearson_r\": 0.8481,\n    \"pearson_p\": 0.0078,\n    \"cil_deberta_mistral_pw\": 1.67,\n    \"cil_sica_mistral_pw\": -4.61,\n    \"cil_deberta_qwen14b_pw\": -0.21,\n    \"cil_sica_qwen14b_pw\": -4.21,\n    \"corrected_v2\": \"Qwen14B canonical SC=74.00% (exp032). Gains: DeBERTa +0.33pp, SICA -2.50pp. Spearman 0.881 p=0.004.\"\n  }\n}\n---\n=== exp-d126-drc-folio matches [nli] ===\n{\n  \"status\": \"PREPARING\",\n  \"hypothesis\": \"DRC (Disagreement-Routed Cascade) with DeBERTa NLI verification on FOLIO-204 recovers \\u226580% of full NLI combo gain at \\u226450% verification cost, extending the ProofWriter DRC result to a second dataset and demonstrating the generality of disagreement-based routing.\",\n  \"conclusion\": \"success\",\n  \"metrics\": {\n    \"sc_acc\": 55.88,\n    \"full_combo_w3_acc\": 58.82,\n    \"drc_tau07_w3_acc\": 58.33,\n    \"drc_tau07_gain_pp\": 2.45,\n    \"drc_tau07_nli_calls\": \"71/204\",\n    \"drc_tau07_cost_pct\": 34.8,\n    \"drc_tau07_gain_recovery_pct\": 83.3,\n    \"drc_tau08_w3_acc\": 58.82,\n    \"drc_tau08_gain_recovery_pct\": 100,\n    \"drc_tau08_cost_pct\": 48.5\n  }\n}\n---\n=== exp-092-llama8b-pw-nli-combo matches [nli] ===\n{\n  \"status\": \"DONE\",\n  \"hypothesis\": \"LLaMA-3.1-8B ProofWriter NLI combo: DeBERTa-large-MNLI standalone (55%) < SC (70%)\\uff0ccapability gap = -15pp\\u3002\\u9a8c\\u8bc1 NLI combo \\u662f\\u5426\\u5728\\u7b2c\\u4e8c\\u4e2a model family \\u4e0a\\u4e5f\\u80fd\\u63d0\\u5347 SC accuracy\\u3002\",\n  \"conclusion\": \"success\",\n  \"metrics\": {\n    \"n\": 600,\n    \"sc_accuracy\": 0.7,\n    \"nli_standalone\": 0.55,\n    \"capability_gap_pp\": -15,\n    \"combo_w1\": 0.7283,\n    \"combo_w3\": 0.7417,\n    \"combo_w5\": 0.7167,\n    \"delta_w1_pp\": 2.83,\n    \"delta_w3_pp\": 4.17,\n    \"delta_w5_pp\": 1.67,\n    \"mcnemar_w1_p\": 0.0001,\n    \"mcnemar_w3_p\": 0.0035,\n    \"mcnemar_w5_p\": 0.4335,\n    \"nli_correct_sc_wrong\": 120,\n    \"sc_correct_nli_wrong\": 210\n  }\n}\n---\n=== exp-091-qwen14b-pw-nli-combo matches [nli] ===\n{\n  \"status\": \"DONE\",\n  \"hypothesis\": \"Qwen2.5-14B ProofWriter NLI combo: DeBERTa-large-MNLI standalone (55%) < SC (73.50%)\\uff0ccapability gap = -18.50pp\\u3002\\u6839\\u636e Push A capability gap \\u5355\\u8c03\\u5173\\u7cfb\\uff0ccombo gain \\u5e94\\u4ecb\\u4e8e Qwen3 (+1.83pp) \\u548c Mistral (+10.67pp) \\u4e4b\\u95f4\\u3002\",\n  \"conclusion\": \"success\",\n  \"metrics\": {\n    \"n\": 600,\n    \"sc_accuracy\": 0.735,\n    \"nli_standalone\": 0.55,\n    \"capability_gap_pp\": -18.5,\n    \"combo_w1\": 0.7417,\n    \"combo_w3\": 0.7433,\n    \"combo_w5\": 0.7533,\n    \"delta_w1_pp\": 0.67,\n    \"delta_w3_pp\": 0.83,\n    \"delta_w5_pp\": 1.83,\n    \"mcnemar_w1_p\": 0.344,\n    \"mcnemar_w3_p\": 0.405,\n    \"mcnemar_w5_p\": 0.144\n  }\n}\n---\n=== exp-090-r-nli-proofwriter matches [nli] ===\n{\n  \"status\": \"DONE\",\n  \"hypothesis\": \"Cross-architecture NLI verification (DeBERTa-large-MNLI) \\u5728 ProofWriter-D5 \\u4e0a\\u4e5f\\u80fd\\u63d0\\u5347 SC accuracy\\uff0c\\u9a8c\\u8bc1 FOLIO \\u4e0a R \\u65b9\\u6cd5\\u7684\\u8de8\\u6570\\u636e\\u96c6\\u6cdb\\u5316\\u80fd\\u529b\\u3002\\u6765\\u6e90: R5-N4 \\u5ba1\\u7a3f\\u4fee\\u590d + Claim 1 (cross-architecture escape generalization)\\u3002\",\n  \"conclusion\": \"success\",\n  \"metrics\": {\n    \"n\": 600,\n    \"sc_accuracy\": 0.3933,\n    \"sica_accuracy\": 0.365,\n    \"nli_standalone\": 0.55,\n    \"combo_w1\": 0.4017,\n    \"combo_w3\": 0.4283,\n    \"combo_w5\": 0.5,\n    \"delta_w1_pp\": 0.83,\n    \"delta_w3_pp\": 3.5,\n    \"delta_w5_pp\": 10.67,\n    \"mcnemar_w1_p\": 0.2668,\n    \"mcnemar_w1_b\": 4,\n    \"mcnemar_w1_c\": 9,\n    \"mcnemar_w3_p\": 0.0125,\n    \"mcnemar_w3_b\": 22,\n    \"mcnemar_w3_c\": 43,\n    \"mcnemar_w5_p\": 0.0001,\n    \"mcnemar_w5_b\": 35,\n    \"mcnemar_w5_c\": 99,\n    \"nli_true_acc\": 0.64,\n    \"nli_false_acc\": 0.975,\n    \"nli_unknown_acc\": 0.035,\n    \"nli_correct_sc_wrong\": 274,\n    \"sc_correct_nli_wrong\": 180,\n    \"agreement_acc\": 0.808\n  }\n}\n---\n=== exp-wave3-dir-r-nli-verifier matches [nli] ===\n{\n  \"status\": \"DONE\",\n  \"hypothesis\": \"DeBERTa External Verifier: encoder-only NLI \\u6a21\\u578b (cross-encoder/nli-deberta-v3-base) \\u4e0e decoder-only LLM \\u67b6\\u6784\\u72ec\\u7acb\\uff0c\\u4f5c\\u4e3a\\u989d\\u5916 vote \\u52a0\\u5165 SC traces \\u53ef\\u6253\\u7834 confirmation bias\\u3002NLI \\u64c5\\u957f contradiction \\u68c0\\u6d4b\\uff08False label\\uff09\\uff0cLLM \\u64c5\\u957f Unknown \\u63a8\\u7406\\uff0c\\u4e24\\u8005\\u4e92\\u8865\\u3002\",\n  \"metrics\": {\n    \"sc_accuracy\": 0.5441,\n    \"nli_standalone\": 0.4951,\n    \"combo_w1\": 0.5784,\n    \"combo_w3\": 0.5882,\n    \"intersection_acc\": 0.6848,\n    \"intersection_coverage\": 0.451,\n    \"delta_w1_pp\": 3.43,\n    \"delta_w3_pp\": 4.41,\n    \"mcnemar_w1_p\": 0.0391,\n    \"mcnemar_w1_b\": 1,\n    \"mcnemar_w1_c\": 8,\n    \"mcnemar_w3_p\": 0.0784,\n    \"mcnemar_w3_b\": 6,\n    \"mcnemar_w3_c\": 15,\n    \"ci95_w1\": [\n      0.98,\n      6.37\n    ],\n    \"ci95_w3\": [\n      0,\n      8.82\n    ],\n    \"nli_false_acc\": 0.7143,\n    \"sc_false_acc\": 0.381,\n    \"nli_unknown_acc\": 0.1884,\n    \"sc_unknown_acc\": 0.6812,\n    \"model_nli\": \"microsoft/deberta-large-mnli\",\n    \"n\": 204\n  },\n  \"conclusion\": \"success\"\n}\n---\n=== exp-wave3-dir-r-combo-extended matches [nli] ===\n{\n  \"status\": \"DONE\",\n  \"hypothesis\": \"R combo \\u7b56\\u7565\\u6269\\u5c55\\uff1a\\u6d4b\\u8bd5 NLI \\u4f5c\\u4e3a\\u4e0d\\u540c\\u6743\\u91cd\\u6295\\u7968\\uff08w=1/3/5\\uff09\\u3001intersection+fallback\\u3001cascade\\uff08\\u6309 NLI confidence \\u5206\\u6d41\\uff09\\u3001weighted averaging \\u7b49\\u7b56\\u7565\\u3002\\u5bfb\\u627e NLI+SICA/SC \\u6700\\u4f18\\u878d\\u5408\\u65b9\\u5f0f\\u3002\",\n  \"conclusion\": \"success\",\n  \"metrics\": {\n    \"sc_accuracy\": 0.5441,\n    \"sica_accuracy\": 0.5931,\n    \"nli_standalone\": 0.4951,\n    \"best_combo\": \"nli_sc_vote_w5\",\n    \"best_combo_acc\": 0.6029,\n    \"best_delta_sc_pp\": 5.88,\n    \"best_delta_sica_pp\": 0.98,\n    \"nli_sc_vote_w3\": 0.5882,\n    \"intersection_sica_fallback\": 0.5931,\n    \"intersection_sc_fallback\": 0.5735,\n    \"oracle_upper_bound\": 0.7549,\n    \"sica_nli_agreement\": 0.475,\n    \"agreement_accuracy\": 0.701,\n    \"n\": 204\n  }\n}\n---\n=== exp-022-oracle-proofwriter matches [6.67] ===\n{\n  \"status\": \"DONE\",\n  \"hypothesis\": \"ProofWriter oracle: gold DSL (raw_logic_programs) \\u901a\\u8fc7 Z3 consistency checking \\u52a0\\u6743 K=12 traces\\uff0cOracle-SICA \\u5e94\\u663e\\u8457\\u8d85\\u8d8a SC \\u548c SICA(self)\\uff0c\\u5728 ProofWriter 600 \\u9898\\u4e0a\\u590d\\u73b0 FOLIO oracle (+8.82pp) \\u7684 extraction bottleneck \\u7ed3\\u8bba\\u3002\",\n  \"conclusion\": \"success\",\n  \"metrics\": {\n    \"n\": 600,\n    \"k\": 12,\n    \"oracle_sica_accuracy\": 0.8667,\n    \"sc_accuracy\": 0.7517,\n    \"sica_self_accuracy\": 0.755,\n    \"oracle_vs_sc_delta_pp\": 11.5,\n    \"mcnemar_p_oracle_vs_sc\": 9.21e-15,\n    \"z3_gold_agreement\": 0.9714,\n    \"z3_gold_agree_n\": 577,\n    \"z3_gold_total\": 594,\n    \"parse_errors\": 6,\n    \"parse_error_rate\": 0.01,\n    \"solver_errors\": 0,\n    \"solver_total\": 7128,\n    \"relneg_oracle\": 0.7786,\n    \"relneg_sc\": 0.6,\n    \"relneg_delta_pp\": 17.86,\n    \"relnoneg_oracle\": 0.7945,\n    \"relnoneg_sc\": 0.6644,\n    \"relnoneg_delta_pp\": 13.01,\n    \"attnoneg_oracle\": 0.961,\n    \"attnoneg_sc\": 0.8701,\n    \"attnoneg_delta_pp\": 9.09,\n    \"attneg_oracle\": 0.9188,\n    \"attneg_sc\": 0.85,\n    \"attneg_delta_pp\": 6.87,\n    \"model\": \"Qwen2.5-14B-Instruct\",\n    \"dataset\": \"ProofWriter-OWA-D5-600\",\n    \"constraint_source\": \"gold DSL (raw_logic_programs)\"\n  },\n  \"notes\": \"KEY RESULT. ProofWriter Oracle-SICA (gold DSL + Z3 + MAX-SAT) 86.67% vs SC 75.17% vs SICA(self) 75.50%, +11.50pp, McNemar p=9.21e-15 \\u6781\\u663e\\u8457\\u3002Z3 gold agreement 97.14% (577/594), parse errors \\u4ec5 6/600 (1%), solver errors 0/7128\\u3002Per-subtype: RelNeg +17.86pp > RelNoneg +13.01pp > AttNoneg +9.09pp > AttNeg +6.87pp\\u2014\\u2014\\u5173\\u7cfb\\u8c13\\u8bcd\\uff08\\u63a8\\u7406\\u94fe\\u66f4\\u957f\\uff09\\u83b7\\u76ca\\u8fdc\\u5927\\u4e8e\\u5c5e\\u6027\\u8c13\\u8bcd\\u3002\\u4e0e FOLIO oracle (exp-021, +8.82pp, p=6.15e-5) \\u5bf9\\u6bd4\\uff1aProofWriter delta \\u66f4\\u5927 (+11.50 vs +8.82) \\u4e14\\u7edf\\u8ba1\\u663e\\u8457\\u6027\\u9ad8 6 \\u4e2a\\u6570\\u91cf\\u7ea7\\u3002\\u4e24\\u4e2a\\u5b50\\u57df Oracle \\u5b9e\\u9a8c\\u4e00\\u81f4\\u8bc1\\u660\n---\n=== exp-012-gsm8k-pilot matches [6.67] ===\n{\n  \"status\": \"DONE\",\n  \"hypothesis\": \"Cross-domain validation: Qwen2.5-14B-Instruct \\u5728 GSM8K (\\u5f00\\u653e\\u7b54\\u6848\\u6570\\u5b66\\u57df) 30 \\u9898\\u4e0a SICA vs SC\\u3002\\u9884\\u671f C0<20%\\uff0814B \\u5728 GSM8K \\u592a\\u5f3a\\uff09\\uff0c\\u9a8c\\u8bc1 C0 \\u4f5c\\u4e3a SICA \\u65e0\\u6548\\u6027\\u9884\\u6d4b\\u6307\\u6807\\u3002\",\n  \"metrics\": {\n    \"n\": 30,\n    \"k\": 12,\n    \"sica_accuracy\": 0.9667,\n    \"sc_accuracy\": 0.9667,\n    \"delta_pp\": 0,\n    \"multi_candidate_rate\": 0.133,\n    \"extraction_success_rate\": 0.147,\n    \"model\": \"Qwen2.5-14B-Instruct\",\n    \"dataset\": \"GSM8K\",\n    \"temperature\": 0.7\n  },\n  \"conclusion\": \"negative\",\n  \"notes\": \"GSM8K 30\\u9898\\uff1aSICA=SC=96.67%\\uff0cdelta=0\\uff0cC0=13.3%\\u3002\\u5f00\\u653e\\u7b54\\u6848\\u6570\\u5b66\\u57df baseline \\u6781\\u9ad8\\uff0896.67%\\uff09\\uff0c\\u51e0\\u4e4e\\u65e0 diversity\\uff08C0=13.3%\\uff09\\uff0cextraction_success_rate \\u4ec5 14.7%\\u2014\\u2014\\u6570\\u5b66\\u57df\\u7684 symbolic constraints \\u96be\\u4ee5\\u63d0\\u53d6\\u3002\\u652f\\u6301 C0 \\u4f5c\\u4e3a SICA \\u65e0\\u6548\\u6027\\u9884\\u6d4b\\u6307\\u6807\\u3002\"\n}\n---\n=== temperature-ablation-t05 matches [6.67] ===\n{\n  \"status\": \"DONE\",\n  \"hypothesis\": \"Temperature ablation T=0.5: \\u4e2d\\u6e29\\u4e0b Qwen2.5-14B trace diversity \\u4e2d\\u7b49\\uff08C0 \\u9884\\u671f 30-45%\\uff09\\uff0cSICA-SC gap \\u9884\\u671f\\u22480\\u2014\\u2014\\u9a8c\\u8bc1\\u5373\\u4f7f diversity \\u9002\\u4e2d\\uff0cconstraint quality \\u4ecd\\u4e3a\\u74f6\\u9888\",\n  \"notes\": \"T=0.5 \\u4e2d\\u6e29\\uff1aC0=38.3%\\uff0cSICA=SC=76.67%\\uff0cdelta=0\\uff0cdiscordant=0\\u3002\\u4e2d\\u7b49 diversity \\u4e0b SICA \\u4ecd\\u5b8c\\u5168\\u7b49\\u4e8e SC\\u3002\",\n  \"metrics\": {\n    \"n\": 60,\n    \"k\": 12,\n    \"sica_accuracy\": 0.7667,\n    \"sc_accuracy\": 0.7667,\n    \"delta_pp\": 0,\n    \"multi_candidate_rate\": 0.383,\n    \"discordant_total\": 0,\n    \"model\": \"Qwen2.5-14B-Instruct\",\n    \"dataset\": \"D012\",\n    \"temperature\": 0.5\n  },\n  \"conclusion\": \"negative\"\n}\n---\n=== exp-010-mistral-v3 matches [6.67] ===\n{\n  \"status\": \"DONE\",\n  \"hypothesis\": \"Cross-family validation: Mistral-7B-Instruct-v0.3 \\u5728 D012 \\u6570\\u636e\\u96c6(30PW+30FOLIO)\\u4e0a\\u662f\\u5426\\u590d\\u73b0 SICA\\u2248SC pattern\\u2014\\u2014\\u9a8c\\u8bc1 capability trap \\u8de8\\u6a21\\u578b\\u5bb6\\u65cf\\u6cdb\\u5316\\uff08v3: \\u811a\\u672c\\u5185\\u542b vLLM \\u6e05\\u7406+conda \\u73af\\u5883\\uff0c\\u89e3\\u51b3 v2 SIGTERM \\u95ee\\u9898\\uff09\",\n  \"metrics\": {\n    \"n\": 60,\n    \"k\": 12,\n    \"sica_accuracy\": 0.4833,\n    \"sc_accuracy\": 0.4833,\n    \"delta_pp\": 0,\n    \"multi_candidate_rate\": 0.5,\n    \"extraction_rate\": 0.8819,\n    \"answer_extraction_rate\": 1,\n    \"contradiction_rate\": 0.0562,\n    \"discordant_sica_wins\": 2,\n    \"discordant_sc_wins\": 2,\n    \"mcnemar_p\": 1,\n    \"proofwriter_sica\": 0.4,\n    \"proofwriter_sc\": 0.4,\n    \"proofwriter_delta_pp\": 0,\n    \"folio_sica\": 0.5667,\n    \"folio_sc\": 0.5667,\n    \"folio_delta_pp\": 0,\n    \"truncated_traces\": 0,\n    \"model\": \"Mistral-7B-Instruct-v0.3\",\n    \"dataset\": \"D012\"\n  },\n  \"conclusion\": \"negative\",\n  \"notes\": \"Mistral-7B cross-family: SICA 48.33% = SC 48.33%, delta=0.00pp\\u3002Multi-candidate rate 50%\\uff0830/60 \\u9898\\u975e unanimous\\uff09\\uff0cSICA \\u4ec5\\u6539\\u53d8 4 \\u9898\\uff086.67% flip rate\\uff09\\u3002\\u6a21\\u578b\\u592a\\u5f31\\uff1aSC baseline 48.33%\\uff08\\u8fd1\\u968f\\u673a\\uff09\\uff0ctrace \\u7f3a\\u4e4f\\u8d28\\u91cf\\u4f46\\u6709\\u591a\\u6837\\u6027\\u3002Discordant 2:2 \\u5e73\\u5c40\\uff0cMcNemar p=1.0\\u3002\\u652f\\u6301 operating regime \\u6709\\u4e0b\\u754c\\uff1a\\u6a21\\u578b\\u5fc5\\u987b\\u8db3\\u591f\\u5f3a\\u624d\\u80fd\\u751f\\u6210\\u6709\\u610f\\u4e49\\u7684 diverse traces\\u3002PW 40%/40%, FOLIO 56.67%/56.67%\\u3002\"\n}\n---\n=== exp-019-llama8b-strategyqa-200 matches [+6.67] ===\n{\n  \"status\": \"DONE\",\n  \"hypothesis\": \"Powered test: SICA \\u5728\\u5f31\\u6a21\\u578b\\uff08LLaMA-3.1-8B\\uff09\\u4e0a\\u7684\\u589e\\u76ca\\u5728 n=200 StrategyQA \\u9898\\u65f6\\u8fbe\\u5230\\u7edf\\u8ba1\\u663e\\u8457\\uff08p<0.05\\uff09\\u2014\\u2014\\u9a8c\\u8bc1 operating regime \\u5047\\u8bbe\\uff08D031 + exp-011 directionally positive +6.67pp\\uff09\",\n  \"metrics\": {\n    \"n\": 200,\n    \"k\": 12,\n    \"sica_accuracy\": 0.74,\n    \"sc_accuracy\": 0.72,\n    \"delta_pp\": 2,\n    \"multi_candidate_rate\": 0.41,\n    \"mcnemar_p\": 0.424,\n    \"bootstrap_ci_95\": [\n      -1.5,\n      5.5\n    ],\n    \"bootstrap_p_delta_le_0\": 0.12,\n    \"discordant_sica_wins\": 9,\n    \"discordant_sc_wins\": 5,\n    \"discordant_total\": 14,\n    \"discordant_rate\": 0.07,\n    \"sc_unanimous_rate\": 0.545,\n    \"model\": \"LLaMA-3.1-8B-Instruct\",\n    \"dataset\": \"StrategyQA\",\n    \"wall_time_min\": 52\n  },\n  \"conclusion\": \"negative\",\n  \"notes\": \"StrategyQA 200\\u9898 powered test: SICA 74% vs SC 72%, +2.00pp, McNemar p=0.424, bootstrap CI [-1.5, +5.5] \\u8de8\\u96f6\\u3002\\u7edf\\u8ba1\\u4e0d\\u663e\\u8457\\u3002exp-011 \\u7684 +6.67pp \\u5728\\u6269\\u5927\\u6837\\u672c\\u540e\\u7f29\\u6c34 70%\\u2014\\u2014\\u5c0f\\u6837\\u672c\\u566a\\u58f0\\u3002\\u5173\\u952e\\u53d1\\u73b0\\uff1a(1) LLaMA-8B \\u5728 StrategyQA \\u4e0a SC=72%\\uff0c\\u9ad8\\u4e8e\\u9884\\u671f\\u7684 sweet spot (55-65%)\\uff0c(2) \\u4ec5 14/200 (7%) discordant pairs\\uff0c54.5% \\u5168\\u7968\\u4e00\\u81f4\\uff0c(3) SICA \\u4ec5\\u5145\\u5f53 tiebreaker\\uff089 wins \\u4e2d 6 \\u4e2a\\u662f\\u5e73\\u7968\\uff09\\u3002StrategyQA \\u4e0d\\u5728 operating regime sweet spot \\u5185\\u3002exp-020 FOLIO (SC\\u224860%) \\u662f\\u771f\\u6b63\\u7684 definitive test\\u3002\"\n}\n---\n=== exp-018-arc-v2 matches [6.67] ===\n{\n  \"status\": \"DONE\",\n  \"hypothesis\": \"Cross-domain validation: Qwen2.5-14B-Instruct \\u5728 ARC-Challenge (\\u79d1\\u5b66\\u591a\\u9009, ABCD) \\u4e0a SICA vs SC\\u2014\\u2014\\u9a8c\\u8bc1 capability trap \\u662f\\u5426\\u8de8\\u4efb\\u52a1\\u7c7b\\u578b\\u6cdb\\u5316\\uff08v2: build_generator bug \\u5df2\\u4fee\\u590d\\uff09\",\n  \"conclusion\": \"success\",\n  \"metrics\": {\n    \"n\": 60,\n    \"k\": 12,\n    \"sica_accuracy\": 0.95,\n    \"sc_accuracy\": 0.9667,\n    \"delta_pp\": -1.67,\n    \"multi_candidate_rate\": 0.05,\n    \"extraction_rate\": 1,\n    \"contradiction_detected\": 3,\n    \"discordant_sica_wins\": 0,\n    \"discordant_sc_wins\": 1,\n    \"dataset\": \"ARC-Challenge\",\n    \"model\": \"Qwen2.5-14B-Instruct\"\n  },\n  \"notes\": \"ARC-Challenge cross-domain: SICA 95.00% vs SC 96.67%, gap=-1.67pp. SICA \\u7565\\u900a\\u4e8e SC\\u3002\\u6a21\\u578b\\u5728 ARC \\u4e0a baseline \\u6781\\u9ad8(96.67%)\\uff0c\\u63a5\\u8fd1\\u5929\\u82b1\\u677f\\u2014\\u2014\\u9ad8\\u51c6\\u786e\\u7387\\u533a\\u95f4\\u591a\\u6837\\u6027\\u4f4e\\uff0cSICA \\u65e0\\u64cd\\u4f5c\\u7a7a\\u95f4\\u3002\\u4e0e StrategyQA (+3.33pp n.s.) \\u5bf9\\u6bd4\\uff1a\\u7b80\\u5355\\u4efb\\u52a1\\uff08\\u9ad8 baseline\\uff09SICA \\u65e0\\u6548\\u6216\\u6709\\u5bb3\\uff0c\\u4e2d\\u7b49\\u96be\\u5ea6\\u4efb\\u52a1\\u6709\\u5fae\\u5f31\\u6b63\\u5411\\u8d8b\\u52bf\\u4f46\\u4e0d\\u663e\\u8457\\u3002\\u6574\\u4f53\\u652f\\u6301 capability trap\\uff1a\\u6a21\\u578b\\u80fd\\u529b\\u8d8a\\u5f3a/\\u4efb\\u52a1\\u8d8a\\u7b80\\u5355 \\u2192 SC \\u5df2\\u8fd1\\u6700\\u4f18 \\u2192 SICA \\u65e0\\u589e\\u91cf\\u3002\"\n}\n---\n=== exp-011-llama8b-v3 matches [+6.67] ===\n{\n  \"status\": \"DONE\",\n  \"hypothesis\": \"Cross-family validation: LLaMA-3.1-8B-Instruct \\u5728 D012 \\u6570\\u636e\\u96c6(30PW+30FOLIO)\\u4e0a\\u662f\\u5426\\u590d\\u73b0 SICA\\u2248SC pattern\\u2014\\u2014\\u9a8c\\u8bc1 capability trap \\u975e Qwen-specific\\uff08v3: \\u6a21\\u578b shard \\u5df2\\u4fee\\u590d\\uff0cGPU \\u7a7a\\u95f2\\u540e\\u63d0\\u4ea4\\uff09\",\n  \"conclusion\": \"success\",\n  \"metrics\": {\n    \"n\": 60,\n    \"k\": 12,\n    \"sica_accuracy\": 0.6667,\n    \"sc_accuracy\": 0.6,\n    \"delta_pp\": 6.67,\n    \"multi_candidate_rate\": 0.6167,\n    \"extraction_rate\": 0.8556,\n    \"answer_extraction_rate\": 0.8958,\n    \"contradiction_rate\": 0.0527,\n    \"problems_with_contradictions\": 43,\n    \"truncated_traces\": 44,\n    \"discordant_sica_wins\": 5,\n    \"discordant_sc_wins\": 1,\n    \"mcnemar_p\": 0.2188,\n    \"proofwriter_sica\": 0.6333,\n    \"proofwriter_sc\": 0.6,\n    \"proofwriter_delta_pp\": 3.33,\n    \"folio_sica\": 0.7,\n    \"folio_sc\": 0.6,\n    \"folio_delta_pp\": 10,\n    \"model\": \"LLaMA-3.1-8B-Instruct\",\n    \"dataset\": \"D012\",\n    \"wall_time_min\": 66.4\n  },\n  \"notes\": \"LLaMA-3.1-8B cross-family: SICA 66.7% vs SC 60.0%, +6.67pp (\\u6700\\u5927\\u589e\\u76ca)\\u3002Discordant 5:1 \\u5f3a\\u70c8\\u503e\\u5411 SICA\\u3002FOLIO +10pp, PW +3.33pp\\u3002McNemar p=0.22\\uff08n=60 \\u53d7\\u9650\\uff09\\u3002Multi-candidate rate 61.7%\\uff08vs Qwen-14B 46%\\uff09\\u2014\\u2014\\u5f31\\u6a21\\u578b\\u66f4\\u591a\\u6837\\u2192SICA \\u6709\\u66f4\\u5927\\u64cd\\u4f5c\\u7a7a\\u95f4\\u300244 \\u6761 truncated traces\\uff08max-tokens \\u53ef\\u80fd\\u504f\\u77ed\\uff09\\uff0c\\u4f46\\u4ecd\\u6709\\u6548\\u3002\\u5173\\u952e\\uff1aSC baseline 60%\\uff08\\u8fdc\\u4f4e\\u4e8e Qwen-14B \\u7684 76%\\uff09\\uff0c\\u9a8c\\u8bc1 capability trap \\u7684\\u6b63\\u9762\\u2014\\u2014\\u6a21\\u578b\\u5f31\\u65f6 SICA \\u6709\\u7528\\u3002\"\n}\n---\n=== exp-017-strategyqa-v3 matches [6.67] ===\n{\n  \"status\": \"DONE\",\n  \"hypothesis\": \"Cross-domain validation: Qwen2.5-14B-Instruct \\u5728 StrategyQA (\\u5e38\\u8bc6\\u63a8\\u7406, Yes/No) \\u4e0a SICA vs SC\\u2014\\u2014\\u9a8c\\u8bc1 capability trap \\u662f\\u5426\\u8de8\\u4efb\\u52a1\\u7c7b\\u578b\\u6cdb\\u5316\\uff08v3: \\u4fee\\u590d True/False\\u2192Yes/No \\u63d0\\u53d6 bug\\uff09\",\n  \"conclusion\": \"success\",\n  \"metrics\": {\n    \"n\": 60,\n    \"k\": 12,\n    \"sica_accuracy\": 0.5667,\n    \"sc_accuracy\": 0.5333,\n    \"delta_pp\": 3.33,\n    \"mcnemar_chi2\": 0.5,\n    \"mcnemar_p\": \"n.s.\",\n    \"bootstrap_ci_95\": [\n      0,\n      8.33\n    ],\n    \"bootstrap_p_delta_le_0\": 0.1346,\n    \"multi_candidate_rate\": 0.1,\n    \"contradiction_detected\": 5,\n    \"extraction_rate_problem\": 1,\n    \"extraction_rate_trace\": 0.704,\n    \"discordant_sica_wins\": 2,\n    \"discordant_sc_wins\": 0\n  },\n  \"notes\": \"StrategyQA\\u8de8\\u57df\\u9a8c\\u8bc1: SICA 56.67% vs SC 53.33%, +3.33pp n.s. (p=0.13), \\u652f\\u6301capability trap\\u8de8\\u4efb\\u52a1\\u6cdb\\u5316; v3\\u4fee\\u590d\\u63d0\\u53d6bug\\u786e\\u8ba4\\u6210\\u529f(100%\\u95ee\\u9898\\u7ea7\\u63d0\\u53d6\\u7387); 2\\u4e2adiscordant pairs\\u5747SICA\\u80dc\\u51fa\"\n}\n---",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  }
}
```

</details>

---

### Tool call

_source line 20_

<details open><summary>🔧 Tool call — Glob · `toolu_01Krv8SewJKTQo4DABTXpCNL`</summary>

```json
{
  "pattern": "**/nli_multi_verifier*",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "259e8c74-cee8-43ee-8c2a-b39b28aafca2",
  "uuid": "533831e9-0d3d-445d-a2f1-2aff3789d82d",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GadASt6nKhBRZLmyN4cYKb",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 18726,
      "cache_read_input_tokens": 24834,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 18726
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

_source line 21 · 2026-05-22T14:51:46.782Z_

<details><summary>↩ Tool result · `toolu_01Krv8SewJKTQo4DABTXpCNL`</summary>

```text
artifacts/_project/data/nli_multi_verifier_recomputed.json
artifacts/_project/data/nli_multi_verifier_recomputed_b79bf3.json
artifacts/nli_multi_verifier_recomputed.json
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "259e8c74-cee8-43ee-8c2a-b39b28aafca2",
  "uuid": "8756e64b-7aac-43f6-86fd-dbe46c32d200",
  "tool_use_result": {
    "filenames": [
      "artifacts/_project/data/nli_multi_verifier_recomputed.json",
      "artifacts/_project/data/nli_multi_verifier_recomputed_b79bf3.json",
      "artifacts/nli_multi_verifier_recomputed.json"
    ],
    "durationMs": 13,
    "numFiles": 3,
    "truncated": false
  }
}
```

</details>

---

### Tool call

_source line 22_

<details open><summary>🔧 Tool call — Glob · `toolu_016yCMQFJdPCXFxiPdJp4sUz`</summary>

```json
{
  "pattern": "**/*nli*",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "259e8c74-cee8-43ee-8c2a-b39b28aafca2",
  "uuid": "3a12d1a6-cb59-49f1-9b9a-94f685555140",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GadASt6nKhBRZLmyN4cYKb",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 18726,
      "cache_read_input_tokens": 24834,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 18726
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

_source line 23 · 2026-05-22T14:51:47.124Z_

<details><summary>↩ Tool result · `toolu_016yCMQFJdPCXFxiPdJp4sUz`</summary>

```text
artifacts/direction_r_nli_large/data/direction_r_nli_large_pointer.txt
artifacts/dir_j2_nli_qwen3.py
artifacts/dir_j3_nli_multi_verifier.py
artifacts/push_b_stronger_nli.py
artifacts/_project/report/nli_tiebreaking_audit.json
artifacts/nli_tiebreaking_audit.json
artifacts/_project/data/nli_combo_recomputed.json
artifacts/nli_combo_recomputed.json
artifacts/_project/data/nli_multi_verifier_recomputed.json
artifacts/_project/data/nli_multi_verifier_recomputed_b79bf3.json
artifacts/nli_multi_verifier_recomputed.json
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "259e8c74-cee8-43ee-8c2a-b39b28aafca2",
  "uuid": "b27dfa73-82df-40a0-8198-8b0e17b3f76e",
  "tool_use_result": {
    "filenames": [
      "artifacts/direction_r_nli_large/data/direction_r_nli_large_pointer.txt",
      "artifacts/dir_j2_nli_qwen3.py",
      "artifacts/dir_j3_nli_multi_verifier.py",
      "artifacts/push_b_stronger_nli.py",
      "artifacts/_project/report/nli_tiebreaking_audit.json",
      "artifacts/nli_tiebreaking_audit.json",
      "artifacts/_project/data/nli_combo_recomputed.json",
      "artifacts/nli_combo_recomputed.json",
      "artifacts/_project/data/nli_multi_verifier_recomputed.json",
      "artifacts/_project/data/nli_multi_verifier_recomputed_b79bf3.json",
      "artifacts/nli_multi_verifier_recomputed.json"
    ],
    "durationMs": 11,
    "numFiles": 11,
    "truncated": false
  }
}
```

</details>

---

### Assistant

_source line 24_

<details><summary>Logged reasoning block</summary>

```text
Now I have key data. Let me trace the +6.67pp:

1. **exp-011-llama8b-v3**: LLaMA-3.1-8B on D012 (30PW+30FOLIO), n=60, SICA 66.7% vs SC 60.0%, **+6.67pp**, McNemar p=0.22. This is the source of "+6.67pp"!

2. **exp-090-r-nli-proofwriter**: Mistral-7B ProofWriter NLI combo. 

Looking at the actual metrics for exp-090: n=600, SC baseline is 39.33%, the combo with w=3 reaches 42.83%, giving a delta of 3.50pp with McNemar p=0.0125. But the user is claiming this experiment showed +6.67pp with p<0.001, which doesn't match what I'm seeing in the data.

The +6.67pp figure appears to come from a different experiment entirely—exp-011 with LLaMA-3.1-8B on a different dataset. I need to check the actual NLI combo results to see if there's a discrepancy between what the paper claims and what the registry shows. I'm checking the recomputed JSON files to see if there's a different calculation method that might explain the +6.67pp figure. Looking at the multi-seed Mistral ProofWriter experiment, the results don't match either—seed 42 shows a delta of -3.33pp, not +6.67pp. I need to trace through whether this larger improvement might be coming from a different experimental setup or dataset altogether.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "259e8c74-cee8-43ee-8c2a-b39b28aafca2",
  "uuid": "360fdf51-8a0c-400c-b2fe-c963c9f0dc3f",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Nc6GR5KkxdHtWyhHY8ZuyQ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 12550,
      "cache_read_input_tokens": 43560,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12550
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

_source line 25_

找到关键线索。exp-090 是 PW-600 上的 NLI combo (w=3: +3.50pp)，而唯一的 +6.67pp 来自 exp-011 (LLaMA-8B D012 n=60)。让我读 NLI 相关 artifacts 确认。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "259e8c74-cee8-43ee-8c2a-b39b28aafca2",
  "uuid": "fc34cb7f-9ef8-4e8b-b9f6-4c865f78b422",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Nc6GR5KkxdHtWyhHY8ZuyQ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 12550,
      "cache_read_input_tokens": 43560,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12550
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

_source line 26_

<details open><summary>🔧 Tool call — Read · `toolu_01JMFfX6UbXzHsUA6LSAUcx3`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/nli_multi_verifier_recomputed.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "259e8c74-cee8-43ee-8c2a-b39b28aafca2",
  "uuid": "1018abaf-e608-4892-829c-13af8af4a019",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Nc6GR5KkxdHtWyhHY8ZuyQ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 12550,
      "cache_read_input_tokens": 43560,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12550
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

_source line 27 · 2026-05-22T14:52:11.194Z_

<details><summary>↩ Tool result · `toolu_01JMFfX6UbXzHsUA6LSAUcx3`</summary>

```text
1	{
2	  "roberta_mnli": {
3	    "standalone_acc": 37.67,
4	    "standalone_correct": 226,
5	    "n": 600,
6	    "mistral_pw_combo": {
7	      "w1": {
8	        "acc": 39.17,
9	        "correct": 235,
10	        "delta_pp": -0.17,
11	        "mcnemar_p": 1.0,
12	        "b": 8,
13	        "c": 7
14	      },
15	      "w3": {
16	        "acc": 43.5,
17	        "correct": 261,
18	        "delta_pp": 4.17,
19	        "mcnemar_p": 0.002626,
20	        "b": 20,
21	        "c": 45
22	      },
23	      "w5": {
24	        "acc": 43.67,
25	        "correct": 262,
26	        "delta_pp": 4.33,
27	        "mcnemar_p": 0.036852,
28	        "b": 59,
29	        "c": 85
30	      }
31	    }
32	  },
33	  "bart_mnli": {
34	    "standalone_acc": 46.17,
35	    "standalone_correct": 277,
36	    "n": 600,
37	    "mistral_pw_combo": {
38	      "w1": {
39	        "acc": 39.33,
40	        "correct": 236,
41	        "delta_pp": 0.0,
42	        "mcnemar_p": 1.0,
43	        "b": 9,
44	        "c": 9
45	      },
46	      "w3": {
47	        "acc": 44.5,
48	        "correct": 267,
49	        "delta_pp": 5.17,
50	        "mcnemar_p": 0.000244,
51	        "b": 19,
52	        "c": 50
53	      },
54	      "w5": {
55	        "acc": 45.67,
56	        "correct": 274,
57	        "delta_pp": 6.33,
58	        "mcnemar_p": 0.002749,
59	        "b": 58,
60	        "c": 96
61	      }
62	    }
63	  },
64	  "deberta_mnli_crosscheck": {
65	    "standalone_acc": 55.0,
66	    "standalone_correct": 330,
67	    "w3_combo_acc": 46.0,
68	    "w3_combo_correct": 276,
69	    "w3_gain": 6.67,
70	    "matches_recomputed": true
71	  },
72	  "sc_baseline_crosscheck": {
73	    "alpha_sc_acc": 39.33,
74	    "alpha_sc_correct": 236,
75	    "expected": 39.33,
76	    "matches": true
77	  },
78	  "spearman_pw6": {
79	    "description": "6 ProofWriter points, all w=3",
80	    "points": [
81	      {
82	        "label": "DeBERTa-L \u00d7 Mistral-7B",
83	        "gap": 15.67,
84	        "gain": 6.67
85	      },
86	      {
87	        "label": "DeBERTa-L \u00d7 LLaMA-3.1-8B",
88	        "gap": -17.5,
89	        "gain": 0.83
90	      },
91	      {
92	        "label": "DeBERTa-L \u00d7 Qwen2.5-14B",
93	        "gap": -19.0,
94	        "gain": 0.67
95	      },
96	      {
97	        "label": "DeBERTa-L \u00d7 Qwen3-14B",
98	        "gap": -30.83,
99	        "gain": 0.5
100	      },
101	      {
102	        "label": "RoBERTa-L \u00d7 Mistral-7B",
103	        "gap": -1.66,
104	        "gain": 4.17
105	      },
106	      {
107	        "label": "BART-L \u00d7 Mistral-7B",
108	        "gap": 6.84,
109	        "gain": 5.17
110	      }
111	    ],
112	    "rho": 1.0,
113	    "exact_p_two_tailed": 0.002778,
114	    "exact_p_one_tailed": 0.001389,
115	    "n_permutations": 720,
116	    "asymptotic_p": 0.0
117	  },
118	  "spearman_all9": {
119	    "description": "6 ProofWriter + 3 FOLIO points",
120	    "points": [
121	      {
122	        "label": "DeBERTa-L \u00d7 Mistral-7B",
123	        "gap": 15.67,
124	        "gain": 6.67
125	      },
126	      {
127	        "label": "DeBERTa-L \u00d7 LLaMA-3.1-8B",
128	        "gap": -17.5,
129	        "gain": 0.83
130	      },
131	      {
132	        "label": "DeBERTa-L \u00d7 Qwen2.5-14B",
133	        "gap": -19.0,
134	        "gain": 0.67
135	      },
136	      {
137	        "label": "DeBERTa-L \u00d7 Qwen3-14B",
138	        "gap": -30.83,
139	        "gain": 0.5
140	      },
141	      {
142	        "label": "RoBERTa-L \u00d7 Mistral-7B",
143	        "gap": -1.66,
144	        "gain": 4.17
145	      },
146	      {
147	        "label": "BART-L \u00d7 Mistral-7B",
148	        "gap": 6.84,
149	        "gain": 5.17
150	      },
151	      {
152	        "label": "DeBERTa-L \u00d7 Mistral-7B FOLIO w=1",
153	        "gap": -6.37,
154	        "gain": 0.49
155	      },
156	      {
157	        "label": "DeBERTa-L \u00d7 Mistral-7B FOLIO w=3",
158	        "gap": -6.37,
159	        "gain": 2.94
160	      },
161	      {
162	        "label": "DeBERTa-L \u00d7 Qwen3 FOLIO w=3",
163	        "gap": -36.76,
164	        "gain": 0.49
165	      }
166	    ],
167	    "rho": 0.836134,
168	    "exact_p_two_tailed": 0.007033,
169	    "exact_p_one_tailed": 0.003538,
170	    "n_permutations": 362880,
171	    "asymptotic_p": 0.004977
172	  }
173	}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "259e8c74-cee8-43ee-8c2a-b39b28aafca2",
  "uuid": "7e81afb1-36e2-4f0e-92f9-549ff6ec78d5",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/nli_multi_verifier_recomputed.json",
      "content": "{\n  \"roberta_mnli\": {\n    \"standalone_acc\": 37.67,\n    \"standalone_correct\": 226,\n    \"n\": 600,\n    \"mistral_pw_combo\": {\n      \"w1\": {\n        \"acc\": 39.17,\n        \"correct\": 235,\n        \"delta_pp\": -0.17,\n        \"mcnemar_p\": 1.0,\n        \"b\": 8,\n        \"c\": 7\n      },\n      \"w3\": {\n        \"acc\": 43.5,\n        \"correct\": 261,\n        \"delta_pp\": 4.17,\n        \"mcnemar_p\": 0.002626,\n        \"b\": 20,\n        \"c\": 45\n      },\n      \"w5\": {\n        \"acc\": 43.67,\n        \"correct\": 262,\n        \"delta_pp\": 4.33,\n        \"mcnemar_p\": 0.036852,\n        \"b\": 59,\n        \"c\": 85\n      }\n    }\n  },\n  \"bart_mnli\": {\n    \"standalone_acc\": 46.17,\n    \"standalone_correct\": 277,\n    \"n\": 600,\n    \"mistral_pw_combo\": {\n      \"w1\": {\n        \"acc\": 39.33,\n        \"correct\": 236,\n        \"delta_pp\": 0.0,\n        \"mcnemar_p\": 1.0,\n        \"b\": 9,\n        \"c\": 9\n      },\n      \"w3\": {\n        \"acc\": 44.5,\n        \"correct\": 267,\n        \"delta_pp\": 5.17,\n        \"mcnemar_p\": 0.000244,\n        \"b\": 19,\n        \"c\": 50\n      },\n      \"w5\": {\n        \"acc\": 45.67,\n        \"correct\": 274,\n        \"delta_pp\": 6.33,\n        \"mcnemar_p\": 0.002749,\n        \"b\": 58,\n        \"c\": 96\n      }\n    }\n  },\n  \"deberta_mnli_crosscheck\": {\n    \"standalone_acc\": 55.0,\n    \"standalone_correct\": 330,\n    \"w3_combo_acc\": 46.0,\n    \"w3_combo_correct\": 276,\n    \"w3_gain\": 6.67,\n    \"matches_recomputed\": true\n  },\n  \"sc_baseline_crosscheck\": {\n    \"alpha_sc_acc\": 39.33,\n    \"alpha_sc_correct\": 236,\n    \"expected\": 39.33,\n    \"matches\": true\n  },\n  \"spearman_pw6\": {\n    \"description\": \"6 ProofWriter points, all w=3\",\n    \"points\": [\n      {\n        \"label\": \"DeBERTa-L \\u00d7 Mistral-7B\",\n        \"gap\": 15.67,\n        \"gain\": 6.67\n      },\n      {\n        \"label\": \"DeBERTa-L \\u00d7 LLaMA-3.1-8B\",\n        \"gap\": -17.5,\n        \"gain\": 0.83\n      },\n      {\n        \"label\": \"DeBERTa-L \\u00d7 Qwen2.5-14B\",\n        \"gap\": -19.0,\n        \"gain\": 0.67\n      },\n      {\n        \"label\": \"DeBERTa-L \\u00d7 Qwen3-14B\",\n        \"gap\": -30.83,\n        \"gain\": 0.5\n      },\n      {\n        \"label\": \"RoBERTa-L \\u00d7 Mistral-7B\",\n        \"gap\": -1.66,\n        \"gain\": 4.17\n      },\n      {\n        \"label\": \"BART-L \\u00d7 Mistral-7B\",\n        \"gap\": 6.84,\n        \"gain\": 5.17\n      }\n    ],\n    \"rho\": 1.0,\n    \"exact_p_two_tailed\": 0.002778,\n    \"exact_p_one_tailed\": 0.001389,\n    \"n_permutations\": 720,\n    \"asymptotic_p\": 0.0\n  },\n  \"spearman_all9\": {\n    \"description\": \"6 ProofWriter + 3 FOLIO points\",\n    \"points\": [\n      {\n        \"label\": \"DeBERTa-L \\u00d7 Mistral-7B\",\n        \"gap\": 15.67,\n        \"gain\": 6.67\n      },\n      {\n        \"label\": \"DeBERTa-L \\u00d7 LLaMA-3.1-8B\",\n        \"gap\": -17.5,\n        \"gain\": 0.83\n      },\n      {\n        \"label\": \"DeBERTa-L \\u00d7 Qwen2.5-14B\",\n        \"gap\": -19.0,\n        \"gain\": 0.67\n      },\n      {\n        \"label\": \"DeBERTa-L \\u00d7 Qwen3-14B\",\n        \"gap\": -30.83,\n        \"gain\": 0.5\n      },\n      {\n        \"label\": \"RoBERTa-L \\u00d7 Mistral-7B\",\n        \"gap\": -1.66,\n        \"gain\": 4.17\n      },\n      {\n        \"label\": \"BART-L \\u00d7 Mistral-7B\",\n        \"gap\": 6.84,\n        \"gain\": 5.17\n      },\n      {\n        \"label\": \"DeBERTa-L \\u00d7 Mistral-7B FOLIO w=1\",\n        \"gap\": -6.37,\n        \"gain\": 0.49\n      },\n      {\n        \"label\": \"DeBERTa-L \\u00d7 Mistral-7B FOLIO w=3\",\n        \"gap\": -6.37,\n        \"gain\": 2.94\n      },\n      {\n        \"label\": \"DeBERTa-L \\u00d7 Qwen3 FOLIO w=3\",\n        \"gap\": -36.76,\n        \"gain\": 0.49\n      }\n    ],\n    \"rho\": 0.836134,\n    \"exact_p_two_tailed\": 0.007033,\n    \"exact_p_one_tailed\": 0.003538,\n    \"n_permutations\": 362880,\n    \"asymptotic_p\": 0.004977\n  }\n}",
      "numLines": 173,
      "startLine": 1,
      "totalLines": 173
    }
  }
}
```

</details>

---

### Tool call

_source line 28_

<details open><summary>🔧 Tool call — Read · `toolu_01UDPfHnaDUJS2st3fHQ1YSD`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/nli_combo_recomputed.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "259e8c74-cee8-43ee-8c2a-b39b28aafca2",
  "uuid": "596648f9-70e7-4921-b42c-8bd9223fb4c5",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Nc6GR5KkxdHtWyhHY8ZuyQ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 12550,
      "cache_read_input_tokens": 43560,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12550
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

_source line 29 · 2026-05-22T14:52:12.138Z_

<details><summary>↩ Tool result · `toolu_01UDPfHnaDUJS2st3fHQ1YSD`</summary>

```text
1	{
2	  "proofwriter": {
3	    "Mistral-7B": {
4	      "n": 600,
5	      "sc": {
6	        "acc": 39.33,
7	        "n_correct": 236
8	      },
9	      "w1": {
10	        "acc": 40.17,
11	        "n_correct": 241,
12	        "delta_pp": 0.83,
13	        "mcnemar_p": 0.359283447265625,
14	        "b": 12,
15	        "c": 7
16	      },
17	      "w3": {
18	        "acc": 46.0,
19	        "n_correct": 276,
20	        "delta_pp": 6.67,
21	        "mcnemar_p": 1.1296023055413025e-05,
22	        "b": 61,
23	        "c": 21
24	      },
25	      "w5": {
26	        "acc": 50.33,
27	        "n_correct": 302,
28	        "delta_pp": 11.0,
29	        "mcnemar_p": 6.178035816936483e-07,
30	        "b": 120,
31	        "c": 54
32	      }
33	    },
34	    "LLaMA-3.1-8B": {
35	      "n": 600,
36	      "sc": {
37	        "acc": 72.5,
38	        "n_correct": 435
39	      },
40	      "w1": {
41	        "acc": 73.33,
42	        "n_correct": 440,
43	        "delta_pp": 0.83,
44	        "mcnemar_p": 0.359283447265625,
45	        "b": 12,
46	        "c": 7
47	      },
48	      "w3": {
49	        "acc": 73.33,
50	        "n_correct": 440,
51	        "delta_pp": 0.83,
52	        "mcnemar_p": 0.6646454904132133,
53	        "b": 45,
54	        "c": 40
55	      },
56	      "w5": {
57	        "acc": 72.0,
58	        "n_correct": 432,
59	        "delta_pp": -0.5,
60	        "mcnemar_p": 0.8707787409560847,
61	        "b": 74,
62	        "c": 77
63	      }
64	    },
65	    "Qwen2.5-14B": {
66	      "n": 600,
67	      "sc": {
68	        "acc": 74.0,
69	        "n_correct": 444
70	      },
71	      "w1": {
72	        "acc": 74.17,
73	        "n_correct": 445,
74	        "delta_pp": 0.17,
75	        "mcnemar_p": 1.0,
76	        "b": 3,
77	        "c": 2
78	      },
79	      "w3": {
80	        "acc": 74.67,
81	        "n_correct": 448,
82	        "delta_pp": 0.67,
83	        "mcnemar_p": 0.5034446716308594,
84	        "b": 12,
85	        "c": 8
86	      },
87	      "w5": {
88	        "acc": 75.17,
89	        "n_correct": 451,
90	        "delta_pp": 1.17,
91	        "mcnemar_p": 0.3603776529357674,
92	        "b": 25,
93	        "c": 18
94	      }
95	    },
96	    "Qwen3-14B": {
97	      "n": 600,
98	      "sc": {
99	        "acc": 85.83,
100	        "n_correct": 515
101	      },
102	      "w1": {
103	        "acc": 86.0,
104	        "n_correct": 516,
105	        "delta_pp": 0.17,
106	        "mcnemar_p": 1.0,
107	        "b": 1,
108	        "c": 0
109	      },
110	      "w3": {
111	        "acc": 86.33,
112	        "n_correct": 518,
113	        "delta_pp": 0.5,
114	        "mcnemar_p": 0.453125,
115	        "b": 5,
116	        "c": 2
117	      },
118	      "w5": {
119	        "acc": 87.0,
120	        "n_correct": 522,
121	        "delta_pp": 1.17,
122	        "mcnemar_p": 0.21003961563110352,
123	        "b": 15,
124	        "c": 8
125	      }
126	    }
127	  },
128	  "folio": {
129	    "Mistral-7B": {
130	      "n": 204,
131	      "sc": {
132	        "acc": 55.88,
133	        "n_correct": 114
134	      },
135	      "w1": {
136	        "acc": 56.37,
137	        "n_correct": 115,
138	        "delta_pp": 0.49,
139	        "mcnemar_p": 1.0,
140	        "b": 4,
141	        "c": 3
142	      },
143	      "w3": {
144	        "acc": 58.82,
145	        "n_correct": 120,
146	        "delta_pp": 2.94,
147	        "mcnemar_p": 0.210113525390625,
148	        "b": 11,
149	        "c": 5
150	      }
151	    }
152	  },
153	  "spearman": {
154	    "generators": [
155	      "Mistral-7B",
156	      "LLaMA-3.1-8B",
157	      "Qwen2.5-14B",
158	      "Qwen3-14B"
159	    ],
160	    "deberta_standalone": 55.0,
161	    "gaps": [
162	      15.67,
163	      -17.5,
164	      -19.0,
165	      -30.83
166	    ],
167	    "gains": [
168	      6.67,
169	      0.83,
170	      0.67,
171	      0.5
172	    ],
173	    "rho": 1.0,
174	    "p": 0.0
175	  },
176	  "bh_correction": {
177	    "m": 12,
178	    "test_labels": [
179	      "Mistral-7B_w1",
180	      "Mistral-7B_w3",
181	      "Mistral-7B_w5",
182	      "LLaMA-3.1-8B_w1",
183	      "LLaMA-3.1-8B_w3",
184	      "LLaMA-3.1-8B_w5",
185	      "Qwen2.5-14B_w1",
186	      "Qwen2.5-14B_w3",
187	      "Qwen2.5-14B_w5",
188	      "Qwen3-14B_w1",
189	      "Qwen3-14B_w3",
190	      "Qwen3-14B_w5"
191	    ],
192	    "raw_pvals": [
193	      0.3592834473,
194	      1.1296e-05,
195	      6.178e-07,
196	      0.3592834473,
197	      0.6646454904,
198	      0.870778741,
199	      1.0,
200	      0.5034446716,
201	      0.3603776529,
202	      1.0,
203	      0.453125,
204	      0.2100396156
205	    ],
206	    "adjusted_pvals": [
207	      0.7207553059,
208	      6.77761e-05,
209	      7.4136e-06,
210	      0.7207553059,
211	      0.8861939872,
212	      1.0,
213	      1.0,
214	      0.7551670074,
215	      0.7207553059,
216	      1.0,
217	      0.7551670074,
218	      0.7207553059
219	    ],
220	    "significant_after_bh": [
221	      false,
222	      true,
223	      true,
224	      false,
225	      false,
226	      false,
227	      false,
228	      false,
229	      false,
230	      false,
231	      false,
232	      false
233	    ],
234	    "n_significant": 2
235	  },
236	  "sc_baseline_shift": {
237	    "note": "Alphabetical tiebreaking (with invalid-answer filtering) changes SC baselines from combo traces",
238	    "changes": {
239	      "Mistral-7B": {
240	        "counter_n": 236,
241	        "alpha_n": 236,
242	        "diff": 0
243	      },
244	      "LLaMA-3.1-8B": {
245	        "counter_n": 420,
246	        "alpha_n": 435,
247	        "diff": 15
248	      },
249	      "Qwen2.5-14B": {
250	        "counter_n": 441,
251	        "alpha_n": 444,
252	        "diff": 3
253	      },
254	      "Qwen3-14B": {
255	        "counter_n": 510,
256	        "alpha_n": 515,
257	        "diff": 5
258	      }
259	    }
260	  },
261	  "paper_changes_needed": [
262	    {
263	      "section": "NLI Combo Table",
264	      "description": "SC baselines shift: LLaMA 420\u2192435(+15), Qwen2.5 441\u2192444(+3), Qwen3 510\u2192515(+5), Mistral unchanged. Combo gains shrink. Only Mistral w3/w5 remain significant after BH.",
265	      "old_significant_count": 4,
266	      "new_significant_count": 2
267	    },
268	    {
269	      "section": "Spearman correlation (capability gap vs combo gain)",
270	      "description": "rho=1.0, p=0.0"
271	    },
272	    {
273	      "section": "FOLIO combo",
274	      "description": "Mistral FOLIO SC=55.88%(114/204), w1=56.37%(+0.49pp,p=1.0), w3=58.82%(+2.94pp,p=0.21)"
275	    }
276	  ]
277	}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "259e8c74-cee8-43ee-8c2a-b39b28aafca2",
  "uuid": "559ae19d-0313-4444-9637-e13184bfc1c4",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/nli_combo_recomputed.json",
      "content": "{\n  \"proofwriter\": {\n    \"Mistral-7B\": {\n      \"n\": 600,\n      \"sc\": {\n        \"acc\": 39.33,\n        \"n_correct\": 236\n      },\n      \"w1\": {\n        \"acc\": 40.17,\n        \"n_correct\": 241,\n        \"delta_pp\": 0.83,\n        \"mcnemar_p\": 0.359283447265625,\n        \"b\": 12,\n        \"c\": 7\n      },\n      \"w3\": {\n        \"acc\": 46.0,\n        \"n_correct\": 276,\n        \"delta_pp\": 6.67,\n        \"mcnemar_p\": 1.1296023055413025e-05,\n        \"b\": 61,\n        \"c\": 21\n      },\n      \"w5\": {\n        \"acc\": 50.33,\n        \"n_correct\": 302,\n        \"delta_pp\": 11.0,\n        \"mcnemar_p\": 6.178035816936483e-07,\n        \"b\": 120,\n        \"c\": 54\n      }\n    },\n    \"LLaMA-3.1-8B\": {\n      \"n\": 600,\n      \"sc\": {\n        \"acc\": 72.5,\n        \"n_correct\": 435\n      },\n      \"w1\": {\n        \"acc\": 73.33,\n        \"n_correct\": 440,\n        \"delta_pp\": 0.83,\n        \"mcnemar_p\": 0.359283447265625,\n        \"b\": 12,\n        \"c\": 7\n      },\n      \"w3\": {\n        \"acc\": 73.33,\n        \"n_correct\": 440,\n        \"delta_pp\": 0.83,\n        \"mcnemar_p\": 0.6646454904132133,\n        \"b\": 45,\n        \"c\": 40\n      },\n      \"w5\": {\n        \"acc\": 72.0,\n        \"n_correct\": 432,\n        \"delta_pp\": -0.5,\n        \"mcnemar_p\": 0.8707787409560847,\n        \"b\": 74,\n        \"c\": 77\n      }\n    },\n    \"Qwen2.5-14B\": {\n      \"n\": 600,\n      \"sc\": {\n        \"acc\": 74.0,\n        \"n_correct\": 444\n      },\n      \"w1\": {\n        \"acc\": 74.17,\n        \"n_correct\": 445,\n        \"delta_pp\": 0.17,\n        \"mcnemar_p\": 1.0,\n        \"b\": 3,\n        \"c\": 2\n      },\n      \"w3\": {\n        \"acc\": 74.67,\n        \"n_correct\": 448,\n        \"delta_pp\": 0.67,\n        \"mcnemar_p\": 0.5034446716308594,\n        \"b\": 12,\n        \"c\": 8\n      },\n      \"w5\": {\n        \"acc\": 75.17,\n        \"n_correct\": 451,\n        \"delta_pp\": 1.17,\n        \"mcnemar_p\": 0.3603776529357674,\n        \"b\": 25,\n        \"c\": 18\n      }\n    },\n    \"Qwen3-14B\": {\n      \"n\": 600,\n      \"sc\": {\n        \"acc\": 85.83,\n        \"n_correct\": 515\n      },\n      \"w1\": {\n        \"acc\": 86.0,\n        \"n_correct\": 516,\n        \"delta_pp\": 0.17,\n        \"mcnemar_p\": 1.0,\n        \"b\": 1,\n        \"c\": 0\n      },\n      \"w3\": {\n        \"acc\": 86.33,\n        \"n_correct\": 518,\n        \"delta_pp\": 0.5,\n        \"mcnemar_p\": 0.453125,\n        \"b\": 5,\n        \"c\": 2\n      },\n      \"w5\": {\n        \"acc\": 87.0,\n        \"n_correct\": 522,\n        \"delta_pp\": 1.17,\n        \"mcnemar_p\": 0.21003961563110352,\n        \"b\": 15,\n        \"c\": 8\n      }\n    }\n  },\n  \"folio\": {\n    \"Mistral-7B\": {\n      \"n\": 204,\n      \"sc\": {\n        \"acc\": 55.88,\n        \"n_correct\": 114\n      },\n      \"w1\": {\n        \"acc\": 56.37,\n        \"n_correct\": 115,\n        \"delta_pp\": 0.49,\n        \"mcnemar_p\": 1.0,\n        \"b\": 4,\n        \"c\": 3\n      },\n      \"w3\": {\n        \"acc\": 58.82,\n        \"n_correct\": 120,\n        \"delta_pp\": 2.94,\n        \"mcnemar_p\": 0.210113525390625,\n        \"b\": 11,\n        \"c\": 5\n      }\n    }\n  },\n  \"spearman\": {\n    \"generators\": [\n      \"Mistral-7B\",\n      \"LLaMA-3.1-8B\",\n      \"Qwen2.5-14B\",\n      \"Qwen3-14B\"\n    ],\n    \"deberta_standalone\": 55.0,\n    \"gaps\": [\n      15.67,\n      -17.5,\n      -19.0,\n      -30.83\n    ],\n    \"gains\": [\n      6.67,\n      0.83,\n      0.67,\n      0.5\n    ],\n    \"rho\": 1.0,\n    \"p\": 0.0\n  },\n  \"bh_correction\": {\n    \"m\": 12,\n    \"test_labels\": [\n      \"Mistral-7B_w1\",\n      \"Mistral-7B_w3\",\n      \"Mistral-7B_w5\",\n      \"LLaMA-3.1-8B_w1\",\n      \"LLaMA-3.1-8B_w3\",\n      \"LLaMA-3.1-8B_w5\",\n      \"Qwen2.5-14B_w1\",\n      \"Qwen2.5-14B_w3\",\n      \"Qwen2.5-14B_w5\",\n      \"Qwen3-14B_w1\",\n      \"Qwen3-14B_w3\",\n      \"Qwen3-14B_w5\"\n    ],\n    \"raw_pvals\": [\n      0.3592834473,\n      1.1296e-05,\n      6.178e-07,\n      0.3592834473,\n      0.6646454904,\n      0.870778741,\n      1.0,\n      0.5034446716,\n      0.3603776529,\n      1.0,\n      0.453125,\n      0.2100396156\n    ],\n    \"adjusted_pvals\": [\n      0.7207553059,\n      6.77761e-05,\n      7.4136e-06,\n      0.7207553059,\n      0.8861939872,\n      1.0,\n      1.0,\n      0.7551670074,\n      0.7207553059,\n      1.0,\n      0.7551670074,\n      0.7207553059\n    ],\n    \"significant_after_bh\": [\n      false,\n      true,\n      true,\n      false,\n      false,\n      false,\n      false,\n      false,\n      false,\n      false,\n      false,\n      false\n    ],\n    \"n_significant\": 2\n  },\n  \"sc_baseline_shift\": {\n    \"note\": \"Alphabetical tiebreaking (with invalid-answer filtering) changes SC baselines from combo traces\",\n    \"changes\": {\n      \"Mistral-7B\": {\n        \"counter_n\": 236,\n        \"alpha_n\": 236,\n        \"diff\": 0\n      },\n      \"LLaMA-3.1-8B\": {\n        \"counter_n\": 420,\n        \"alpha_n\": 435,\n        \"diff\": 15\n      },\n      \"Qwen2.5-14B\": {\n        \"counter_n\": 441,\n        \"alpha_n\": 444,\n        \"diff\": 3\n      },\n      \"Qwen3-14B\": {\n        \"counter_n\": 510,\n        \"alpha_n\": 515,\n        \"diff\": 5\n      }\n    }\n  },\n  \"paper_changes_needed\": [\n    {\n      \"section\": \"NLI Combo Table\",\n      \"description\": \"SC baselines shift: LLaMA 420\\u2192435(+15), Qwen2.5 441\\u2192444(+3), Qwen3 510\\u2192515(+5), Mistral unchanged. Combo gains shrink. Only Mistral w3/w5 remain significant after BH.\",\n      \"old_significant_count\": 4,\n      \"new_significant_count\": 2\n    },\n    {\n      \"section\": \"Spearman correlation (capability gap vs combo gain)\",\n      \"description\": \"rho=1.0, p=0.0\"\n    },\n    {\n      \"section\": \"FOLIO combo\",\n      \"description\": \"Mistral FOLIO SC=55.88%(114/204), w1=56.37%(+0.49pp,p=1.0), w3=58.82%(+2.94pp,p=0.21)\"\n    }\n  ]\n}",
      "numLines": 277,
      "startLine": 1,
      "totalLines": 277
    }
  }
}
```

</details>

---

### Tool call

_source line 30_

<details open><summary>🔧 Tool call — Read · `toolu_01XQBzj5zi4ecjTZMa8cu4Fd`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/_project/data/nli_multi_verifier_recomputed.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "259e8c74-cee8-43ee-8c2a-b39b28aafca2",
  "uuid": "a838c2a6-02f5-41a9-83c4-a908e14a17e1",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Nc6GR5KkxdHtWyhHY8ZuyQ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 12550,
      "cache_read_input_tokens": 43560,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12550
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

_source line 31 · 2026-05-22T14:52:12.331Z_

<details><summary>↩ Tool result · `toolu_01XQBzj5zi4ecjTZMa8cu4Fd`</summary>

```text
1	{
2	  "roberta_mnli": {
3	    "standalone_acc": 37.67,
4	    "standalone_correct": 226,
5	    "n": 600,
6	    "mistral_pw_combo": {
7	      "w1": {
8	        "acc": 39.17,
9	        "correct": 235,
10	        "delta_pp": -0.17,
11	        "mcnemar_p": 1.0,
12	        "b": 8,
13	        "c": 7
14	      },
15	      "w3": {
16	        "acc": 43.5,
17	        "correct": 261,
18	        "delta_pp": 4.17,
19	        "mcnemar_p": 0.002626,
20	        "b": 20,
21	        "c": 45
22	      },
23	      "w5": {
24	        "acc": 43.67,
25	        "correct": 262,
26	        "delta_pp": 4.33,
27	        "mcnemar_p": 0.036852,
28	        "b": 59,
29	        "c": 85
30	      }
31	    }
32	  },
33	  "bart_mnli": {
34	    "standalone_acc": 46.17,
35	    "standalone_correct": 277,
36	    "n": 600,
37	    "mistral_pw_combo": {
38	      "w1": {
39	        "acc": 39.33,
40	        "correct": 236,
41	        "delta_pp": 0.0,
42	        "mcnemar_p": 1.0,
43	        "b": 9,
44	        "c": 9
45	      },
46	      "w3": {
47	        "acc": 44.5,
48	        "correct": 267,
49	        "delta_pp": 5.17,
50	        "mcnemar_p": 0.000244,
51	        "b": 19,
52	        "c": 50
53	      },
54	      "w5": {
55	        "acc": 45.67,
56	        "correct": 274,
57	        "delta_pp": 6.33,
58	        "mcnemar_p": 0.002749,
59	        "b": 58,
60	        "c": 96
61	      }
62	    }
63	  },
64	  "deberta_mnli_crosscheck": {
65	    "standalone_acc": 55.0,
66	    "standalone_correct": 330,
67	    "w3_combo_acc": 46.0,
68	    "w3_combo_correct": 276,
69	    "w3_gain": 6.67,
70	    "matches_recomputed": true
71	  },
72	  "sc_baseline_crosscheck": {
73	    "alpha_sc_acc": 39.33,
74	    "alpha_sc_correct": 236,
75	    "expected": 39.33,
76	    "matches": true
77	  },
78	  "spearman_pw6": {
79	    "description": "6 ProofWriter points, all w=3",
80	    "points": [
81	      {
82	        "label": "DeBERTa-L \u00d7 Mistral-7B",
83	        "gap": 15.67,
84	        "gain": 6.67
85	      },
86	      {
87	        "label": "DeBERTa-L \u00d7 LLaMA-3.1-8B",
88	        "gap": -17.5,
89	        "gain": 0.83
90	      },
91	      {
92	        "label": "DeBERTa-L \u00d7 Qwen2.5-14B",
93	        "gap": -19.0,
94	        "gain": 0.67
95	      },
96	      {
97	        "label": "DeBERTa-L \u00d7 Qwen3-14B",
98	        "gap": -30.83,
99	        "gain": 0.5
100	      },
101	      {
102	        "label": "RoBERTa-L \u00d7 Mistral-7B",
103	        "gap": -1.66,
104	        "gain": 4.17
105	      },
106	      {
107	        "label": "BART-L \u00d7 Mistral-7B",
108	        "gap": 6.84,
109	        "gain": 5.17
110	      }
111	    ],
112	    "rho": 1.0,
113	    "exact_p_two_tailed": 0.002778,
114	    "exact_p_one_tailed": 0.001389,
115	    "n_permutations": 720,
116	    "asymptotic_p": 0.0
117	  },
118	  "spearman_all9": {
119	    "description": "6 ProofWriter + 3 FOLIO points",
120	    "points": [
121	      {
122	        "label": "DeBERTa-L \u00d7 Mistral-7B",
123	        "gap": 15.67,
124	        "gain": 6.67
125	      },
126	      {
127	        "label": "DeBERTa-L \u00d7 LLaMA-3.1-8B",
128	        "gap": -17.5,
129	        "gain": 0.83
130	      },
131	      {
132	        "label": "DeBERTa-L \u00d7 Qwen2.5-14B",
133	        "gap": -19.0,
134	        "gain": 0.67
135	      },
136	      {
137	        "label": "DeBERTa-L \u00d7 Qwen3-14B",
138	        "gap": -30.83,
139	        "gain": 0.5
140	      },
141	      {
142	        "label": "RoBERTa-L \u00d7 Mistral-7B",
143	        "gap": -1.66,
144	        "gain": 4.17
145	      },
146	      {
147	        "label": "BART-L \u00d7 Mistral-7B",
148	        "gap": 6.84,
149	        "gain": 5.17
150	      },
151	      {
152	        "label": "DeBERTa-L \u00d7 Mistral-7B FOLIO w=1",
153	        "gap": -6.37,
154	        "gain": 0.49
155	      },
156	      {
157	        "label": "DeBERTa-L \u00d7 Mistral-7B FOLIO w=3",
158	        "gap": -6.37,
159	        "gain": 2.94
160	      },
161	      {
162	        "label": "DeBERTa-L \u00d7 Qwen3 FOLIO w=3",
163	        "gap": -36.76,
164	        "gain": 0.49
165	      }
166	    ],
167	    "rho": 0.836134,
168	    "exact_p_two_tailed": 0.007033,
169	    "exact_p_one_tailed": 0.003538,
170	    "n_permutations": 362880,
171	    "asymptotic_p": 0.004977
172	  }
173	}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "259e8c74-cee8-43ee-8c2a-b39b28aafca2",
  "uuid": "6b6361f3-93dc-422f-91d6-b77011f702e7",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/_project/data/nli_multi_verifier_recomputed.json",
      "content": "{\n  \"roberta_mnli\": {\n    \"standalone_acc\": 37.67,\n    \"standalone_correct\": 226,\n    \"n\": 600,\n    \"mistral_pw_combo\": {\n      \"w1\": {\n        \"acc\": 39.17,\n        \"correct\": 235,\n        \"delta_pp\": -0.17,\n        \"mcnemar_p\": 1.0,\n        \"b\": 8,\n        \"c\": 7\n      },\n      \"w3\": {\n        \"acc\": 43.5,\n        \"correct\": 261,\n        \"delta_pp\": 4.17,\n        \"mcnemar_p\": 0.002626,\n        \"b\": 20,\n        \"c\": 45\n      },\n      \"w5\": {\n        \"acc\": 43.67,\n        \"correct\": 262,\n        \"delta_pp\": 4.33,\n        \"mcnemar_p\": 0.036852,\n        \"b\": 59,\n        \"c\": 85\n      }\n    }\n  },\n  \"bart_mnli\": {\n    \"standalone_acc\": 46.17,\n    \"standalone_correct\": 277,\n    \"n\": 600,\n    \"mistral_pw_combo\": {\n      \"w1\": {\n        \"acc\": 39.33,\n        \"correct\": 236,\n        \"delta_pp\": 0.0,\n        \"mcnemar_p\": 1.0,\n        \"b\": 9,\n        \"c\": 9\n      },\n      \"w3\": {\n        \"acc\": 44.5,\n        \"correct\": 267,\n        \"delta_pp\": 5.17,\n        \"mcnemar_p\": 0.000244,\n        \"b\": 19,\n        \"c\": 50\n      },\n      \"w5\": {\n        \"acc\": 45.67,\n        \"correct\": 274,\n        \"delta_pp\": 6.33,\n        \"mcnemar_p\": 0.002749,\n        \"b\": 58,\n        \"c\": 96\n      }\n    }\n  },\n  \"deberta_mnli_crosscheck\": {\n    \"standalone_acc\": 55.0,\n    \"standalone_correct\": 330,\n    \"w3_combo_acc\": 46.0,\n    \"w3_combo_correct\": 276,\n    \"w3_gain\": 6.67,\n    \"matches_recomputed\": true\n  },\n  \"sc_baseline_crosscheck\": {\n    \"alpha_sc_acc\": 39.33,\n    \"alpha_sc_correct\": 236,\n    \"expected\": 39.33,\n    \"matches\": true\n  },\n  \"spearman_pw6\": {\n    \"description\": \"6 ProofWriter points, all w=3\",\n    \"points\": [\n      {\n        \"label\": \"DeBERTa-L \\u00d7 Mistral-7B\",\n        \"gap\": 15.67,\n        \"gain\": 6.67\n      },\n      {\n        \"label\": \"DeBERTa-L \\u00d7 LLaMA-3.1-8B\",\n        \"gap\": -17.5,\n        \"gain\": 0.83\n      },\n      {\n        \"label\": \"DeBERTa-L \\u00d7 Qwen2.5-14B\",\n        \"gap\": -19.0,\n        \"gain\": 0.67\n      },\n      {\n        \"label\": \"DeBERTa-L \\u00d7 Qwen3-14B\",\n        \"gap\": -30.83,\n        \"gain\": 0.5\n      },\n      {\n        \"label\": \"RoBERTa-L \\u00d7 Mistral-7B\",\n        \"gap\": -1.66,\n        \"gain\": 4.17\n      },\n      {\n        \"label\": \"BART-L \\u00d7 Mistral-7B\",\n        \"gap\": 6.84,\n        \"gain\": 5.17\n      }\n    ],\n    \"rho\": 1.0,\n    \"exact_p_two_tailed\": 0.002778,\n    \"exact_p_one_tailed\": 0.001389,\n    \"n_permutations\": 720,\n    \"asymptotic_p\": 0.0\n  },\n  \"spearman_all9\": {\n    \"description\": \"6 ProofWriter + 3 FOLIO points\",\n    \"points\": [\n      {\n        \"label\": \"DeBERTa-L \\u00d7 Mistral-7B\",\n        \"gap\": 15.67,\n        \"gain\": 6.67\n      },\n      {\n        \"label\": \"DeBERTa-L \\u00d7 LLaMA-3.1-8B\",\n        \"gap\": -17.5,\n        \"gain\": 0.83\n      },\n      {\n        \"label\": \"DeBERTa-L \\u00d7 Qwen2.5-14B\",\n        \"gap\": -19.0,\n        \"gain\": 0.67\n      },\n      {\n        \"label\": \"DeBERTa-L \\u00d7 Qwen3-14B\",\n        \"gap\": -30.83,\n        \"gain\": 0.5\n      },\n      {\n        \"label\": \"RoBERTa-L \\u00d7 Mistral-7B\",\n        \"gap\": -1.66,\n        \"gain\": 4.17\n      },\n      {\n        \"label\": \"BART-L \\u00d7 Mistral-7B\",\n        \"gap\": 6.84,\n        \"gain\": 5.17\n      },\n      {\n        \"label\": \"DeBERTa-L \\u00d7 Mistral-7B FOLIO w=1\",\n        \"gap\": -6.37,\n        \"gain\": 0.49\n      },\n      {\n        \"label\": \"DeBERTa-L \\u00d7 Mistral-7B FOLIO w=3\",\n        \"gap\": -6.37,\n        \"gain\": 2.94\n      },\n      {\n        \"label\": \"DeBERTa-L \\u00d7 Qwen3 FOLIO w=3\",\n        \"gap\": -36.76,\n        \"gain\": 0.49\n      }\n    ],\n    \"rho\": 0.836134,\n    \"exact_p_two_tailed\": 0.007033,\n    \"exact_p_one_tailed\": 0.003538,\n    \"n_permutations\": 362880,\n    \"asymptotic_p\": 0.004977\n  }\n}",
      "numLines": 173,
      "startLine": 1,
      "totalLines": 173
    }
  }
}
```

</details>

---

### Assistant

_source line 32_

<details><summary>Logged reasoning block</summary>

```text
Now I have the complete picture. Let me piece it together:

**The +6.67pp comes from `nli_combo_recomputed.json`:**
- ProofWriter, Mistral-7B, w=3: acc=46.0%, SC=39.33%, delta_pp=**6.67**, mcnemar_p=**1.13e-05** (≈0.00001, which is <0.001)
- This is also crosschecked in `nli_multi_verifier_recomputed.json`: deberta_mnli_crosscheck w3_gain=6.67


- But `exp-090-r-nli-proofwriter` shows the same configuration yielding only +3.50pp with p=0.0125, suggesting a discrepancy in how the results were computed or which subset of data was used.

Looking closer at the numbers, the baseline SC is identical at 39.33% (236/600), but the combo accuracies diverge significantly: 46.0% (276/600) versus 42.83% (257/600). That's a difference of 19 correct predictions between the two runs.

The culprit appears to be the DeBERTa model itself—`exp-090` uses `microsoft/deberta-large-mnli` while `nli_combo_recomputed` references a different variant, likely causing the divergence in predictions. Same standalone accuracy but different combo results suggests the discrepancy comes from either different NLI model checkpoints being used, different semantic checker traces in the combination, or a variation in how the combo computation itself was performed. The exp-090 experiment is specifically testing cross-architecture NLI verification on ProofWriter, and while both use DeBERTa-large-MNLI at 55% standalone, I need to trace whether they're actually using identical model outputs or if something in the pipeline differs.

Looking at the FOLIO results more carefully, the recomputed data used a different random seed for the semantic checker baseline (seed=42 giving 55.88% vs seed=None giving 54.41%), which explains why the same NLI model produces different combo gains. For ProofWriter though, both exp-090 and the recomputed version show the same 39.33% SC baseline, yet the combo results diverge significantly at 42.83% versus 46.0%, so the difference must lie elsewhere—likely in which specific semantic checker traces are being combined or how the combination algorithm itself is implemented. I'm realizing the McNemar contingency table definitions might be flipped between these two experiments. In exp-090, the positive delta of 3.50pp aligns with c=43 being larger than b=22, suggesting c represents cases where combo is correct and SC is wrong. But in nli_combo_recomputed, if b=61 and c=21 with a positive delta, that would only make sense if b and c are defined in the opposite convention—meaning b represents combo correct & SC wrong, and c represents combo wrong & SC correct. I'm realizing the b and c columns have opposite meanings between these two files. In exp-090, c represents cases where combo wins and b represents cases where SC wins, but in nli_combo_recomputed it's flipped. The actual underlying numbers are different too—exp-090 shows 43 vs 22, while nli_combo_recomputed shows 61 vs 21—so these aren't just relabeled versions of the same data.

Let me verify the math: exp-090 has 236 SC correct, plus 43 combo-only wins minus 22 SC-only wins gives 257 combo correct (42.83%). For nli_combo_recomputed, the same 236 SC correct plus 61 combo wins minus 21 SC wins yields 276 combo correct (46.0%). The SC performance is identical across both, so the divergence must come from different NLI predictions, even though both supposedly use the same deberta-large-mnli model.

This is puzzling—if they're using the same model, I'd expect the same predictions unless the inference setup differs somehow. Let me dig into whether there's actually a model mismatch or if the inference conditions changed between runs.

Looking at exp-090, it shows nli_standalone at 55%, and nli_multi_verifier_recomputed also reports 55% standalone accuracy with the same DeBERTa model. That matches overall, but individual predictions could still diverge.

Wait, I'm noticing something in exp-wave3-dir-r-nli-verifier—it specifies microsoft/deberta-large-mnli with n=204, and nli_combo_recomputed shows 55.88% (114/204) with seed=42, whereas the original exp-wave3-dir-r had 54.41% with a different seed. So they're working from different trace sets entirely.

For ProofWriter, both exp-090 and nli_combo_recomputed hit 39.33% with the same Mistral-7B baseline, but the combo results still differ somehow. Maybe nli_combo_recomputed used a different NLI configuration—different threshold, premise formatting, or even a different model variant altogether.

Let me check if the two nli_multi_verifier_recomputed.json files are actually identical or if there's a version mismatch between the project data and the top-level version. me look for a version difference. The file nli_multi_verifier_recomputed_b79bf3.json might be a different version.

Also, let me look at what DeBERTa model was used. paper_framing.md says exp-wave3-dir-r uses "microsoft/deberta-large-mnli" (406M parameters). But there's also "cross-encoder/nli-deberta-v3-base" mentioned in exp-wave3-dir-r's hypothesis. Those are TWO DIFFERENT MODELS.

exp-wave3-dir-r-nli-verifier hypothesis: "encoder-only NLI 模型 (cross-encoder/nli-deberta-v3-base) 与 decoder-only LLM 架构独立"
But exp-wave3-dir-r-nli-verifier metrics: model_nli = "microsoft/deberta-large-mnli"

So the experiment was supposed to use cross-encoder/nli-deberta-v3-base but actually ran with microsoft/deberta-large-mnli instead. And exp-090 uses nli_standalone=0.55, which matches deberta-large-mnli. Let me check if nli_combo_recomputed was computed from a different set of NLI predictions entirely—the "recomputed" suffix suggests it was recomputed after some correction. The core discrepancy I need to resolve is why nli_combo_recomputed.json shows Mistral-7B PW w=3 = 46.0% (+6.67pp) while exp-090 shows w=3 = 42.83% (+3.50pp), even though both use the same SC baseline. Looking at the two experiments, nli_combo_recomputed shows a larger improvement (+6.67pp) compared to exp-090 (+3.50pp), even though both use the same NLI model accuracy of 55%. This discrepancy suggests the actual NLI predictions differ between them—possibly due to different model checkpoints, how the ProofWriter problems were formatted as NLI pairs, or variations in the voting aggregation method.

I need to check the tiebreaking audit file to see if that's where the difference lies, and also look at the _b79bf3 version to understand what changed.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "259e8c74-cee8-43ee-8c2a-b39b28aafca2",
  "uuid": "4eb399fd-8562-4f64-a29e-036c20db4f3e",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VCDtvLbmMGeF7UDdg5rJgb",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8591,
      "cache_read_input_tokens": 56110,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 8591
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

_source line 33_

找到关键分歧点了。让我进一步确认 NLI tiebreaking audit 和另一个版本的 recomputed 文件。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "259e8c74-cee8-43ee-8c2a-b39b28aafca2",
  "uuid": "55c777ab-b9dc-4a11-8653-bdf4dcdc1280",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VCDtvLbmMGeF7UDdg5rJgb",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8591,
      "cache_read_input_tokens": 56110,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 8591
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

_source line 34_

<details open><summary>🔧 Tool call — Read · `toolu_01TeZWFpVy4oQ5t53tjeEBfx`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/nli_tiebreaking_audit.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "259e8c74-cee8-43ee-8c2a-b39b28aafca2",
  "uuid": "ca2a9d74-f2f8-468c-a9c7-6a2f45125b95",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VCDtvLbmMGeF7UDdg5rJgb",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8591,
      "cache_read_input_tokens": 56110,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 8591
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

_source line 35 · 2026-05-22T14:53:29.355Z_

<details><summary>↩ Tool result · `toolu_01TeZWFpVy4oQ5t53tjeEBfx`</summary>

```text
1	{
2	  "investigation": {
3	    "affected_scripts": [
4	      "direction_r_deberta_proofwriter.py",
5	      "dir_j3_nli_multi_verifier.py",
6	      "dir_k_nli_qwen3_pw600.py",
7	      "direction_rg_combo.py",
8	      "direction_r_nli_verifier.py (FOLIO)"
9	    ],
10	    "tiebreaking_method": "Counter.most_common(1)[0][0] — insertion-order tiebreaking under ties",
11	    "correct_method": "sorted(tied_candidates)[0] — alphabetical (consistent with SC baseline standard)",
12	    "drc_cascade_pilot_method": "alphabetical (correct, in scripts/drc_cascade_pilot.py)",
13	    "code_snippet": "combo_answer = votes.most_common(1)[0][0]  # BUG: non-alphabetical tiebreaking"
14	  },
15	  "experiments": {
16	    "exp-090 (Mistral-7B PW)": {
17	      "n": 600,
18	      "sc_baseline_alpha": "39.33% (236/600)",
19	      "sc_baseline_counter": "39.33% (236/600)",
20	      "sc_tiebreak_diffs": 11,
21	      "combo_w1": {
22	        "current_counter": "40.17% (241/600)",
23	        "corrected_alpha": "40.17% (241/600)",
24	        "delta": "0.00pp",
25	        "changed_questions": 17,
26	        "mcnemar_alpha_vs_sc": {"p": 0.359283, "b": 7, "c": 12},
27	        "mcnemar_counter_vs_sc": {"p": 0.266846, "b": 4, "c": 9}
28	      },
29	      "combo_w3": {
30	        "current_counter": "42.83% (257/600)",
31	        "corrected_alpha": "46.00% (276/600)",
32	        "delta": "+3.17pp",
33	        "changed_questions": 30,
34	        "mcnemar_alpha_vs_sc": {"p": 1.1e-05, "b": 21, "c": 61},
35	        "mcnemar_counter_vs_sc": {"p": 0.012503, "b": 22, "c": 43}
36	      },
37	      "combo_w5": {
38	        "current_counter": "50.00% (300/600)",
39	        "corrected_alpha": "50.33% (302/600)",
40	        "delta": "+0.33pp",
41	        "changed_questions": 53,
42	        "mcnemar_alpha_vs_sc": {"p": 1e-06, "b": 54, "c": 120},
43	        "mcnemar_counter_vs_sc": {"p": 0.0, "b": 35, "c": 99}
44	      }
45	    },
46	    "exp-091 (Qwen3 PW)": {
47	      "status": "NEEDS_RECOMPUTATION",
48	      "data_location": "westd-16639:d116_qwen3_pw_deberta_large",
49	      "paper_reported_sc": "85.0%",
50	      "paper_reported_combo_w3": "86.0%",
51	      "expected_impact": "Small — high SC accuracy means few ties"
52	    },
53	    "exp-092 (LLaMA PW)": {
54	      "status": "NEEDS_RECOMPUTATION",
55	      "data_location": "westd-16639:exp092_llama8b_pw_nli_combo",
56	      "paper_reported_sc": "70.0%",
57	      "paper_reported_combo_w3": "74.17%",
58	      "expected_impact": "Moderate — some ties possible"
59	    },
60	    "exp-093 (Qwen2.5 PW)": {
61	      "status": "NEEDS_RECOMPUTATION",
62	      "data_location": "westd-16639:qwen14b_pw_nli_combo",
63	      "paper_reported_sc": "73.5%",
64	      "paper_reported_combo_w3": "74.33%",
65	      "expected_impact": "Moderate — some ties possible"
66	    }
67	  },
68	  "folio_combo": {
69	    "n_questions": 204,
70	    "n_changed_by_tiebreak": 8,
71	    "alpha_accuracy": "56.37% (115/204)",
72	    "counter_accuracy": "57.84% (118/204)",
73	    "delta": "-1.47pp (alphabetical is WORSE for FOLIO)",
74	    "note": "FOLIO NLI combo uses w=1 (direction_r_nli_verifier.py), different from PW weighted combo"
75	  },
76	  "drc_cascade_pilot_crosscheck": {
77	    "drc_pilot_combo_w3": "46.0% (276/600) — alphabetical tiebreaking",
78	    "our_recomputed_alpha_w3": "46.0% (276/600)",
79	    "match": true
80	  },
81	  "impact_summary": "BUG CONFIRMED: All NLI combo scripts use Counter.most_common() (insertion-order tiebreaking) while the paper's SC baselines use alphabetical. The biggest impact is Mistral-7B combo_w3: paper reports 42.83% but alphabetical gives 46.00% (+3.17pp, 30 questions affected). This changes McNemar p from 0.0125 to 1.1e-05 (much more significant). DRC cascade pilot already uses alphabetical and gives 46.0%, confirming the discrepancy source. w=1 and w=5 are minimally affected. Other 3 models (exp-091 to 093) need recomputation from westd-16639 data but expected impact is smaller. FOLIO combo (w=1) has 8 questions affected with -1.47pp delta (alpha worse).",
82	  "recommended_action": "1) Recompute all 4 PW models' NLI combo with alphabetical tiebreaking. 2) For Mistral w=3: update paper from 42.83% to 46.00%, update McNemar p-value. 3) Rerun BH correction table with new numbers. 4) FOLIO combo numbers also need checking if reported in paper. 5) Fix all combo scripts to use alphabetical tiebreaking."
83	}
84	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "259e8c74-cee8-43ee-8c2a-b39b28aafca2",
  "uuid": "f90cb27e-922b-45e8-8c6a-d6ea18b42fcf",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/nli_tiebreaking_audit.json",
      "content": "{\n  \"investigation\": {\n    \"affected_scripts\": [\n      \"direction_r_deberta_proofwriter.py\",\n      \"dir_j3_nli_multi_verifier.py\",\n      \"dir_k_nli_qwen3_pw600.py\",\n      \"direction_rg_combo.py\",\n      \"direction_r_nli_verifier.py (FOLIO)\"\n    ],\n    \"tiebreaking_method\": \"Counter.most_common(1)[0][0] — insertion-order tiebreaking under ties\",\n    \"correct_method\": \"sorted(tied_candidates)[0] — alphabetical (consistent with SC baseline standard)\",\n    \"drc_cascade_pilot_method\": \"alphabetical (correct, in scripts/drc_cascade_pilot.py)\",\n    \"code_snippet\": \"combo_answer = votes.most_common(1)[0][0]  # BUG: non-alphabetical tiebreaking\"\n  },\n  \"experiments\": {\n    \"exp-090 (Mistral-7B PW)\": {\n      \"n\": 600,\n      \"sc_baseline_alpha\": \"39.33% (236/600)\",\n      \"sc_baseline_counter\": \"39.33% (236/600)\",\n      \"sc_tiebreak_diffs\": 11,\n      \"combo_w1\": {\n        \"current_counter\": \"40.17% (241/600)\",\n        \"corrected_alpha\": \"40.17% (241/600)\",\n        \"delta\": \"0.00pp\",\n        \"changed_questions\": 17,\n        \"mcnemar_alpha_vs_sc\": {\"p\": 0.359283, \"b\": 7, \"c\": 12},\n        \"mcnemar_counter_vs_sc\": {\"p\": 0.266846, \"b\": 4, \"c\": 9}\n      },\n      \"combo_w3\": {\n        \"current_counter\": \"42.83% (257/600)\",\n        \"corrected_alpha\": \"46.00% (276/600)\",\n        \"delta\": \"+3.17pp\",\n        \"changed_questions\": 30,\n        \"mcnemar_alpha_vs_sc\": {\"p\": 1.1e-05, \"b\": 21, \"c\": 61},\n        \"mcnemar_counter_vs_sc\": {\"p\": 0.012503, \"b\": 22, \"c\": 43}\n      },\n      \"combo_w5\": {\n        \"current_counter\": \"50.00% (300/600)\",\n        \"corrected_alpha\": \"50.33% (302/600)\",\n        \"delta\": \"+0.33pp\",\n        \"changed_questions\": 53,\n        \"mcnemar_alpha_vs_sc\": {\"p\": 1e-06, \"b\": 54, \"c\": 120},\n        \"mcnemar_counter_vs_sc\": {\"p\": 0.0, \"b\": 35, \"c\": 99}\n      }\n    },\n    \"exp-091 (Qwen3 PW)\": {\n      \"status\": \"NEEDS_RECOMPUTATION\",\n      \"data_location\": \"westd-16639:d116_qwen3_pw_deberta_large\",\n      \"paper_reported_sc\": \"85.0%\",\n      \"paper_reported_combo_w3\": \"86.0%\",\n      \"expected_impact\": \"Small — high SC accuracy means few ties\"\n    },\n    \"exp-092 (LLaMA PW)\": {\n      \"status\": \"NEEDS_RECOMPUTATION\",\n      \"data_location\": \"westd-16639:exp092_llama8b_pw_nli_combo\",\n      \"paper_reported_sc\": \"70.0%\",\n      \"paper_reported_combo_w3\": \"74.17%\",\n      \"expected_impact\": \"Moderate — some ties possible\"\n    },\n    \"exp-093 (Qwen2.5 PW)\": {\n      \"status\": \"NEEDS_RECOMPUTATION\",\n      \"data_location\": \"westd-16639:qwen14b_pw_nli_combo\",\n      \"paper_reported_sc\": \"73.5%\",\n      \"paper_reported_combo_w3\": \"74.33%\",\n      \"expected_impact\": \"Moderate — some ties possible\"\n    }\n  },\n  \"folio_combo\": {\n    \"n_questions\": 204,\n    \"n_changed_by_tiebreak\": 8,\n    \"alpha_accuracy\": \"56.37% (115/204)\",\n    \"counter_accuracy\": \"57.84% (118/204)\",\n    \"delta\": \"-1.47pp (alphabetical is WORSE for FOLIO)\",\n    \"note\": \"FOLIO NLI combo uses w=1 (direction_r_nli_verifier.py), different from PW weighted combo\"\n  },\n  \"drc_cascade_pilot_crosscheck\": {\n    \"drc_pilot_combo_w3\": \"46.0% (276/600) — alphabetical tiebreaking\",\n    \"our_recomputed_alpha_w3\": \"46.0% (276/600)\",\n    \"match\": true\n  },\n  \"impact_summary\": \"BUG CONFIRMED: All NLI combo scripts use Counter.most_common() (insertion-order tiebreaking) while the paper's SC baselines use alphabetical. The biggest impact is Mistral-7B combo_w3: paper reports 42.83% but alphabetical gives 46.00% (+3.17pp, 30 questions affected). This changes McNemar p from 0.0125 to 1.1e-05 (much more significant). DRC cascade pilot already uses alphabetical and gives 46.0%, confirming the discrepancy source. w=1 and w=5 are minimally affected. Other 3 models (exp-091 to 093) need recomputation from westd-16639 data but expected impact is smaller. FOLIO combo (w=1) has 8 questions affected with -1.47pp delta (alpha worse).\",\n  \"recommended_action\": \"1) Recompute all 4 PW models' NLI combo with alphabetical tiebreaking. 2) For Mistral w=3: update paper from 42.83% to 46.00%, update McNemar p-value. 3) Rerun BH correction table with new numbers. 4) FOLIO combo numbers also need checking if reported in paper. 5) Fix all combo scripts to use alphabetical tiebreaking.\"\n}\n",
      "numLines": 84,
      "startLine": 1,
      "totalLines": 84
    }
  }
}
```

</details>

---

### Tool call

_source line 36_

<details open><summary>🔧 Tool call — Read · `toolu_01KYHTSPMy3Hp3PhL79DKins`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/_project/data/nli_multi_verifier_recomputed_b79bf3.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "259e8c74-cee8-43ee-8c2a-b39b28aafca2",
  "uuid": "1cffe0d7-6cdf-4fa3-b63c-840d4657dc38",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VCDtvLbmMGeF7UDdg5rJgb",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8591,
      "cache_read_input_tokens": 56110,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 8591
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

_source line 37 · 2026-05-22T14:53:29.624Z_

<details><summary>↩ Tool result · `toolu_01KYHTSPMy3Hp3PhL79DKins`</summary>

```text
1	{
2	  "roberta_mnli": {
3	    "standalone_acc": 37.67,
4	    "standalone_correct": 226,
5	    "n": 600,
6	    "mistral_pw_combo": {
7	      "w1": {
8	        "acc": 39.17,
9	        "correct": 235,
10	        "delta_pp": -0.17,
11	        "mcnemar_p": 1.0,
12	        "b": 8,
13	        "c": 7
14	      },
15	      "w3": {
16	        "acc": 43.5,
17	        "correct": 261,
18	        "delta_pp": 4.17,
19	        "mcnemar_p": 0.002626,
20	        "b": 20,
21	        "c": 45
22	      },
23	      "w5": {
24	        "acc": 43.67,
25	        "correct": 262,
26	        "delta_pp": 4.33,
27	        "mcnemar_p": 0.036852,
28	        "b": 59,
29	        "c": 85
30	      }
31	    }
32	  },
33	  "bart_mnli": {
34	    "standalone_acc": 46.17,
35	    "standalone_correct": 277,
36	    "n": 600,
37	    "mistral_pw_combo": {
38	      "w1": {
39	        "acc": 39.33,
40	        "correct": 236,
41	        "delta_pp": 0.0,
42	        "mcnemar_p": 1.0,
43	        "b": 9,
44	        "c": 9
45	      },
46	      "w3": {
47	        "acc": 44.5,
48	        "correct": 267,
49	        "delta_pp": 5.17,
50	        "mcnemar_p": 0.000244,
51	        "b": 19,
52	        "c": 50
53	      },
54	      "w5": {
55	        "acc": 45.67,
56	        "correct": 274,
57	        "delta_pp": 6.33,
58	        "mcnemar_p": 0.002749,
59	        "b": 58,
60	        "c": 96
61	      }
62	    }
63	  },
64	  "deberta_mnli_crosscheck": {
65	    "standalone_acc": 55.0,
66	    "standalone_correct": 330,
67	    "w3_combo_acc": 46.0,
68	    "w3_combo_correct": 276,
69	    "w3_gain": 6.67,
70	    "matches_recomputed": true
71	  },
72	  "sc_baseline_crosscheck": {
73	    "alpha_sc_acc": 39.33,
74	    "alpha_sc_correct": 236,
75	    "expected": 39.33,
76	    "matches": true
77	  },
78	  "spearman_pw6": {
79	    "description": "6 ProofWriter points, all w=3",
80	    "points": [
81	      {
82	        "label": "DeBERTa-L \u00d7 Mistral-7B",
83	        "gap": 15.67,
84	        "gain": 6.67
85	      },
86	      {
87	        "label": "DeBERTa-L \u00d7 LLaMA-3.1-8B",
88	        "gap": -17.5,
89	        "gain": 0.83
90	      },
91	      {
92	        "label": "DeBERTa-L \u00d7 Qwen2.5-14B",
93	        "gap": -19.0,
94	        "gain": 0.67
95	      },
96	      {
97	        "label": "DeBERTa-L \u00d7 Qwen3-14B",
98	        "gap": -30.83,
99	        "gain": 0.5
100	      },
101	      {
102	        "label": "RoBERTa-L \u00d7 Mistral-7B",
103	        "gap": -1.66,
104	        "gain": 4.17
105	      },
106	      {
107	        "label": "BART-L \u00d7 Mistral-7B",
108	        "gap": 6.84,
109	        "gain": 5.17
110	      }
111	    ],
112	    "rho": 1.0,
113	    "exact_p_two_tailed": 0.002778,
114	    "exact_p_one_tailed": 0.001389,
115	    "n_permutations": 720,
116	    "asymptotic_p": 0.0
117	  },
118	  "spearman_all9": {
119	    "description": "6 ProofWriter + 3 FOLIO points",
120	    "points": [
121	      {
122	        "label": "DeBERTa-L \u00d7 Mistral-7B",
123	        "gap": 15.67,
124	        "gain": 6.67
125	      },
126	      {
127	        "label": "DeBERTa-L \u00d7 LLaMA-3.1-8B",
128	        "gap": -17.5,
129	        "gain": 0.83
130	      },
131	      {
132	        "label": "DeBERTa-L \u00d7 Qwen2.5-14B",
133	        "gap": -19.0,
134	        "gain": 0.67
135	      },
136	      {
137	        "label": "DeBERTa-L \u00d7 Qwen3-14B",
138	        "gap": -30.83,
139	        "gain": 0.5
140	      },
141	      {
142	        "label": "RoBERTa-L \u00d7 Mistral-7B",
143	        "gap": -1.66,
144	        "gain": 4.17
145	      },
146	      {
147	        "label": "BART-L \u00d7 Mistral-7B",
148	        "gap": 6.84,
149	        "gain": 5.17
150	      },
151	      {
152	        "label": "DeBERTa-L \u00d7 Mistral-7B FOLIO w=1",
153	        "gap": -6.37,
154	        "gain": 0.49
155	      },
156	      {
157	        "label": "DeBERTa-L \u00d7 Mistral-7B FOLIO w=3",
158	        "gap": -6.37,
159	        "gain": 2.94
160	      },
161	      {
162	        "label": "DeBERTa-L \u00d7 Qwen3 FOLIO w=3",
163	        "gap": -36.76,
164	        "gain": 0.49
165	      }
166	    ],
167	    "rho": 0.836134,
168	    "exact_p_two_tailed": 0.007033,
169	    "exact_p_one_tailed": 0.003538,
170	    "n_permutations": 362880,
171	    "asymptotic_p": 0.004977
172	  }
173	}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "259e8c74-cee8-43ee-8c2a-b39b28aafca2",
  "uuid": "8d5ddb6a-5fa7-43c2-96c1-88788810597f",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/_project/data/nli_multi_verifier_recomputed_b79bf3.json",
      "content": "{\n  \"roberta_mnli\": {\n    \"standalone_acc\": 37.67,\n    \"standalone_correct\": 226,\n    \"n\": 600,\n    \"mistral_pw_combo\": {\n      \"w1\": {\n        \"acc\": 39.17,\n        \"correct\": 235,\n        \"delta_pp\": -0.17,\n        \"mcnemar_p\": 1.0,\n        \"b\": 8,\n        \"c\": 7\n      },\n      \"w3\": {\n        \"acc\": 43.5,\n        \"correct\": 261,\n        \"delta_pp\": 4.17,\n        \"mcnemar_p\": 0.002626,\n        \"b\": 20,\n        \"c\": 45\n      },\n      \"w5\": {\n        \"acc\": 43.67,\n        \"correct\": 262,\n        \"delta_pp\": 4.33,\n        \"mcnemar_p\": 0.036852,\n        \"b\": 59,\n        \"c\": 85\n      }\n    }\n  },\n  \"bart_mnli\": {\n    \"standalone_acc\": 46.17,\n    \"standalone_correct\": 277,\n    \"n\": 600,\n    \"mistral_pw_combo\": {\n      \"w1\": {\n        \"acc\": 39.33,\n        \"correct\": 236,\n        \"delta_pp\": 0.0,\n        \"mcnemar_p\": 1.0,\n        \"b\": 9,\n        \"c\": 9\n      },\n      \"w3\": {\n        \"acc\": 44.5,\n        \"correct\": 267,\n        \"delta_pp\": 5.17,\n        \"mcnemar_p\": 0.000244,\n        \"b\": 19,\n        \"c\": 50\n      },\n      \"w5\": {\n        \"acc\": 45.67,\n        \"correct\": 274,\n        \"delta_pp\": 6.33,\n        \"mcnemar_p\": 0.002749,\n        \"b\": 58,\n        \"c\": 96\n      }\n    }\n  },\n  \"deberta_mnli_crosscheck\": {\n    \"standalone_acc\": 55.0,\n    \"standalone_correct\": 330,\n    \"w3_combo_acc\": 46.0,\n    \"w3_combo_correct\": 276,\n    \"w3_gain\": 6.67,\n    \"matches_recomputed\": true\n  },\n  \"sc_baseline_crosscheck\": {\n    \"alpha_sc_acc\": 39.33,\n    \"alpha_sc_correct\": 236,\n    \"expected\": 39.33,\n    \"matches\": true\n  },\n  \"spearman_pw6\": {\n    \"description\": \"6 ProofWriter points, all w=3\",\n    \"points\": [\n      {\n        \"label\": \"DeBERTa-L \\u00d7 Mistral-7B\",\n        \"gap\": 15.67,\n        \"gain\": 6.67\n      },\n      {\n        \"label\": \"DeBERTa-L \\u00d7 LLaMA-3.1-8B\",\n        \"gap\": -17.5,\n        \"gain\": 0.83\n      },\n      {\n        \"label\": \"DeBERTa-L \\u00d7 Qwen2.5-14B\",\n        \"gap\": -19.0,\n        \"gain\": 0.67\n      },\n      {\n        \"label\": \"DeBERTa-L \\u00d7 Qwen3-14B\",\n        \"gap\": -30.83,\n        \"gain\": 0.5\n      },\n      {\n        \"label\": \"RoBERTa-L \\u00d7 Mistral-7B\",\n        \"gap\": -1.66,\n        \"gain\": 4.17\n      },\n      {\n        \"label\": \"BART-L \\u00d7 Mistral-7B\",\n        \"gap\": 6.84,\n        \"gain\": 5.17\n      }\n    ],\n    \"rho\": 1.0,\n    \"exact_p_two_tailed\": 0.002778,\n    \"exact_p_one_tailed\": 0.001389,\n    \"n_permutations\": 720,\n    \"asymptotic_p\": 0.0\n  },\n  \"spearman_all9\": {\n    \"description\": \"6 ProofWriter + 3 FOLIO points\",\n    \"points\": [\n      {\n        \"label\": \"DeBERTa-L \\u00d7 Mistral-7B\",\n        \"gap\": 15.67,\n        \"gain\": 6.67\n      },\n      {\n        \"label\": \"DeBERTa-L \\u00d7 LLaMA-3.1-8B\",\n        \"gap\": -17.5,\n        \"gain\": 0.83\n      },\n      {\n        \"label\": \"DeBERTa-L \\u00d7 Qwen2.5-14B\",\n        \"gap\": -19.0,\n        \"gain\": 0.67\n      },\n      {\n        \"label\": \"DeBERTa-L \\u00d7 Qwen3-14B\",\n        \"gap\": -30.83,\n        \"gain\": 0.5\n      },\n      {\n        \"label\": \"RoBERTa-L \\u00d7 Mistral-7B\",\n        \"gap\": -1.66,\n        \"gain\": 4.17\n      },\n      {\n        \"label\": \"BART-L \\u00d7 Mistral-7B\",\n        \"gap\": 6.84,\n        \"gain\": 5.17\n      },\n      {\n        \"label\": \"DeBERTa-L \\u00d7 Mistral-7B FOLIO w=1\",\n        \"gap\": -6.37,\n        \"gain\": 0.49\n      },\n      {\n        \"label\": \"DeBERTa-L \\u00d7 Mistral-7B FOLIO w=3\",\n        \"gap\": -6.37,\n        \"gain\": 2.94\n      },\n      {\n        \"label\": \"DeBERTa-L \\u00d7 Qwen3 FOLIO w=3\",\n        \"gap\": -36.76,\n        \"gain\": 0.49\n      }\n    ],\n    \"rho\": 0.836134,\n    \"exact_p_two_tailed\": 0.007033,\n    \"exact_p_one_tailed\": 0.003538,\n    \"n_permutations\": 362880,\n    \"asymptotic_p\": 0.004977\n  }\n}",
      "numLines": 173,
      "startLine": 1,
      "totalLines": 173
    }
  }
}
```

</details>

---

### Assistant

_source line 38_

<details><summary>Logged reasoning block</summary>

```text
Now I have the complete picture. The `nli_tiebreaking_audit.json` explains everything perfectly.

## Root Cause: Tiebreaking Bug

The NLI combo scripts used `Counter.most_common(1)[0][0]` (insertion-order tiebreaking), while the paper's SC baselines use alphabetical tiebreaking. When this bug was discovered and corrected:

**exp-090 (original, buggy tiebreaking):**
- combo_w3 = 42.83% (257/600), using Counter.most_common() insertion-order tiebreaking


- delta = +3.50pp, McNemar p=0.0125

**nli_combo_recomputed.json (corrected, alphabetical tiebreaking):**
- combo_w3 = 46.00% (276/600), using alphabetical tiebreaking
- delta = +6.67pp, McNemar p=1.1e-05

The audit confirms the fix: 30 questions changed when switching from insertion-order to alphabetical tiebreaking, accounting for the 3.17 percentage point improvement and the much stronger statistical significance.

The DRC cascade pilot independently validated this same 46.0% result using alphabetical tiebreaking, confirming the corrected approach aligns with the standard baseline convention. The root cause is clear: the original experiment used Counter.most_common() which applied insertion-order tiebreaking, creating an inconsistency with how the SC baseline was computed. I see the paper is already citing the corrected value of +6.67pp, which matches the recomputed McNemar result. The registry entry showing +3.50pp reflects the original buggy calculation, but that's been superseded. The p-value claim of p<0.001 holds up even after Benjamini-Hochberg correction across the 12 tests, so the paper's statistical claims are sound.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "259e8c74-cee8-43ee-8c2a-b39b28aafca2",
  "uuid": "8ed02b11-788b-4d58-aa64-445c864ae65f",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AJrfhqpqA8GuLyi7hT3Q8U",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7836,
      "cache_read_input_tokens": 64701,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 7836
      },
      "output_tokens": 11,
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

_source line 39_

完整的证据链已找到。根因是 **tiebreaking bug**。

---

## 排查结果

### 1. +6.67pp 来自哪个实验

来自 `nli_combo_recomputed.json`（tiebreaking 修正后的版本）：
- **配置**: DeBERTa-large-MNLI × Mistral-7B × ProofWriter-600, w=3, n=600
- **SC baseline**: 39.33% (236/600)
- **combo w=3**: 46.00% (276/600), **+6.67pp**, McNemar p=1.13e-05
- **tiebreaking**: 字母序（alphabetical），与 SC baseline 一致

### 2. exp-090 是什么实验

`exp-090-r-nli-proofwriter`，**同一实验的原始版本**（未修正 tiebreaking）：
- 完全相同的模型、数据集、配置
- **combo w=3**: 42.83% (257/600), **+3.50pp**, McNemar p=0.0125
- **tiebreaking**: `Counter.most_common(1)[0][0]`——插入序（insertion-order），与 SC baseline 不一致

### 3. 数据不一致的根因

**Tiebreaking bug**。详见 `nli_tiebreaking_audit.json`：

| 项目 | exp-090 (buggy) | recomputed (corrected) |
|------|-----------------|----------------------|
| tiebreaking | `Counter.most_common()` 插入序 | `sorted(tied)[0]` 字母序 |
| combo w3 correct | 257/600 | 276/600 |
| delta | +3.50pp | +6.67pp |
| McNemar p | 0.0125 | 1.13e-05 |
| 受影响题数 | — | 30题 |

combo 脚本用 `votes.most_common(1)[0][0]` 做 tie resolution，而 SC baseline 用字母序。两套 tiebreaking 标准导致 combo 在 30 个平票问题上选了不同答案。DRC cascade pilot 独立使用字母序也得到 46.0%，交叉验证了修正值。

### 4. 论文应引用哪组数据

**+6.67pp (recomputed)**。理由：
- 字母序 tiebreaking 与 SC baseline convention 一致（同一 comparand 同一标准）
- DRC cascade pilot 独立确认 46.0%
- BH 校正后 p=6.78e-05，仍 <0.001
- tiebreaking audit 明确建议更新到修正值

**需要做的**：将 exp-090 registry 的 metrics 更新为修正后数值，避免未来再次产生混淆。exp-091/092/093 也需要同步 recompute（audit 标记为 `NEEDS_RECOMPUTATION`）。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "259e8c74-cee8-43ee-8c2a-b39b28aafca2",
  "uuid": "719d4896-34a7-478e-9a07-af2fc2b8fb60",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AJrfhqpqA8GuLyi7hT3Q8U",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7836,
      "cache_read_input_tokens": 64701,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 7836
      },
      "output_tokens": 11,
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

### Task result

_source line 40_

完整的证据链已找到。根因是 **tiebreaking bug**。

---

## 排查结果

### 1. +6.67pp 来自哪个实验

来自 `nli_combo_recomputed.json`（tiebreaking 修正后的版本）：
- **配置**: DeBERTa-large-MNLI × Mistral-7B × ProofWriter-600, w=3, n=600
- **SC baseline**: 39.33% (236/600)
- **combo w=3**: 46.00% (276/600), **+6.67pp**, McNemar p=1.13e-05
- **tiebreaking**: 字母序（alphabetical），与 SC baseline 一致

### 2. exp-090 是什么实验

`exp-090-r-nli-proofwriter`，**同一实验的原始版本**（未修正 tiebreaking）：
- 完全相同的模型、数据集、配置
- **combo w=3**: 42.83% (257/600), **+3.50pp**, McNemar p=0.0125
- **tiebreaking**: `Counter.most_common(1)[0][0]`——插入序（insertion-order），与 SC baseline 不一致

### 3. 数据不一致的根因

**Tiebreaking bug**。详见 `nli_tiebreaking_audit.json`：

| 项目 | exp-090 (buggy) | recomputed (corrected) |
|------|-----------------|----------------------|
| tiebreaking | `Counter.most_common()` 插入序 | `sorted(tied)[0]` 字母序 |
| combo w3 correct | 257/600 | 276/600 |
| delta | +3.50pp | +6.67pp |
| McNemar p | 0.0125 | 1.13e-05 |
| 受影响题数 | — | 30题 |

combo 脚本用 `votes.most_common(1)[0][0]` 做 tie resolution，而 SC baseline 用字母序。两套 tiebreaking 标准导致 combo 在 30 个平票问题上选了不同答案。DRC cascade pilot 独立使用字母序也得到 46.0%，交叉验证了修正值。

### 4. 论文应引用哪组数据

**+6.67pp (recomputed)**。理由：
- 字母序 tiebreaking 与 SC baseline convention 一致（同一 comparand 同一标准）
- DRC cascade pilot 独立确认 46.0%
- BH 校正后 p=6.78e-05，仍 <0.001
- tiebreaking audit 明确建议更新到修正值

**需要做的**：将 exp-090 registry 的 metrics 更新为修正后数值，避免未来再次产生混淆。exp-091/092/093 也需要同步 recompute（audit 标记为 `NEEDS_RECOMPUTATION`）。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "type": "result",
  "subtype": "success",
  "is_error": false,
  "api_error_status": null,
  "duration_ms": 168047,
  "duration_api_ms": 168514,
  "num_turns": 14,
  "stop_reason": "end_turn",
  "session_id": "259e8c74-cee8-43ee-8c2a-b39b28aafca2",
  "total_cost_usd": 0.7119310000000001,
  "usage": {
    "input_tokens": 10,
    "cache_creation_input_tokens": 60696,
    "cache_read_input_tokens": 225068,
    "output_tokens": 8746,
    "server_tool_use": {
      "web_search_requests": 0,
      "web_fetch_requests": 0
    },
    "service_tier": "standard",
    "cache_creation": {
      "ephemeral_1h_input_tokens": 60696,
      "ephemeral_5m_input_tokens": 0
    },
    "inference_geo": "",
    "iterations": [
      {
        "input_tokens": 1,
        "output_tokens": 1760,
        "cache_read_input_tokens": 64701,
        "cache_creation_input_tokens": 7836,
        "cache_creation": {
          "ephemeral_5m_input_tokens": 0,
          "ephemeral_1h_input_tokens": 7836
        },
        "type": "message"
      }
    ],
    "speed": "standard"
  },
  "modelUsage": {
    "claude-haiku-4-5-20251001": {
      "inputTokens": 1227,
      "outputTokens": 24,
      "cacheReadInputTokens": 0,
      "cacheCreationInputTokens": 0,
      "webSearchRequests": 0,
      "costUSD": 0.001347,
      "contextWindow": 200000,
      "maxOutputTokens": 32000
    },
    "claude-opus-4-6": {
      "inputTokens": 10,
      "outputTokens": 8746,
      "cacheReadInputTokens": 225068,
      "cacheCreationInputTokens": 60696,
      "webSearchRequests": 0,
      "costUSD": 0.7105840000000001,
      "contextWindow": 200000,
      "maxOutputTokens": 64000
    }
  },
  "permission_denials": [],
  "terminal_reason": "completed",
  "fast_mode_state": "off",
  "uuid": "e06f4226-b8d6-421e-90fc-7f9d02f93fdf"
}
```

</details>

---
