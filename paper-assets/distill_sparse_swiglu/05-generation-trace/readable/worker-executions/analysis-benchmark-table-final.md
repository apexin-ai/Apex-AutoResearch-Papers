# analysis benchmark table final

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs** · Worker execution logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 29
- **Recorded user turns:** 0
- **Tool calls:** 8
- **Original source:** `logs/workers/worker_analysis_benchmark-table-final_20260516T165941.log`
- **Structured JSON:** [`f8b100f4350248cdb92c.json`](../../sessions/f8/f8b100f4350248cdb92c.json)

## Before a recorded user message

29 recorded events

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
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu",
  "session_id": "f716b164-a763-4033-b921-7fe9fd43c5b1",
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
  "uuid": "c35fe643-dc2f-42cb-abee-7d873fda3fdd",
  "memory_paths": {
    "auto": "/home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-14-projects-distill-sparse-swiglu/memory/"
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
    "resetsAt": 1778959200,
    "rateLimitType": "five_hour",
    "overageStatus": "rejected",
    "overageDisabledReason": "org_level_disabled",
    "isUsingOverage": false
  },
  "uuid": "44edcab3-20f9-4fd3-86fe-80189b4ee289",
  "session_id": "f716b164-a763-4033-b921-7fe9fd43c5b1"
}
```

---

### Assistant

_source line 4_

Let me start by reading the current table and verifying the data from the registry.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "f716b164-a763-4033-b921-7fe9fd43c5b1",
  "uuid": "5cd8f86f-10b1-4f8a-8d6a-194eab52dec5",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019YuNfxw94LwAp4WBCEeBbD",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12266,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12266
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

<details open><summary>🔧 Tool call — Read · `toolu_01GWFRWmSxpbC2HnQHKsSwYm`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/_project/report/benchmark_comparison_table.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "f716b164-a763-4033-b921-7fe9fd43c5b1",
  "uuid": "4b336b64-e466-4c64-931e-edc36f884b9b",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019YuNfxw94LwAp4WBCEeBbD",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12266,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12266
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

_source line 6 · 2026-05-16T16:59:50.451Z_

<details><summary>↩ Tool result · `toolu_01GWFRWmSxpbC2HnQHKsSwYm`</summary>

```text
1	# Unified Benchmark Comparison Table
2	
3	**Model**: Llama-3.1-8B | **Eval**: benchmark_eval.py (ARC-c=25-shot, WG=5-shot, MMLU=5-shot, GSM8K=8-shot, WikiText-2 PPL)
4	
5	## Main Results
6	
7	| Condition | Sparsity | Allocation | PPL | ARC-c | WG | MMLU | GSM8K |
8	|-----------|----------|------------|-----|-------|-----|------|-------|
9	| Dense (baseline) | 0% | — | 6.117 | 0.5828 | 0.7806 | 0.6527 | 0.4875 |
10	| KL 30% | 30% | uniform | 8.816 | 0.4078 | 0.6859 | 0.4061 | 0.0735 |
11	| KL 40% | 40% | uniform | 8.363 | 0.4181 | 0.6717 | 0.3068 | 0.0394 |
12	| KL 50% | 50% | uniform | 11.960 | 0.3276 | 0.6290 | 0.2777 | 0.0212 |
13	| KL 30% | 30% | global | 8.977 | 0.3968 | 0.7017 | 0.2527 | 0.0879 |
14	| KL 50% | 50% | global | 11.793 | 0.3285 | 0.6346 | 0.2789 | 0.0129 |
15	| BCE v3 (2700 steps) | 50% | learned | 22.510 | 0.2398 | 0.5059 | 0.3002 | 0.0485 |
16	| TEAL 50% † | 50% | magnitude | 27.970* | 0.2910 | 0.5556 | 0.2856 | 0.0190 |
17	| TEAL 50% (unified) | 50% | magnitude | — queued | — queued | — queued | — queued | — queued |
18	| TEAL 30% (unified) | 30% | magnitude | — queued | — queued | — queued | — queued | — queued |
19	
20	† lm_eval_teal_50pct uses lm-evaluation-harness (0-shot default), not directly comparable to unified few-shot results.
21	\* TEAL PPL from eval_bce_v3_s42 `teal_sparse_ppl` measurement (same model, same WikiText-2 split).
22	
23	## Relative Change vs Dense (%)
24	
25	| Condition | PPL ↑ | ARC-c ↓ | WG ↓ | MMLU ↓ | GSM8K ↓ |
26	|-----------|-------|---------|------|--------|---------|
27	| KL 30% uniform | +44.1% | −30.0% | −12.1% | −37.8% | −84.9% |
28	| KL 40% uniform | +36.7% | −28.3% | −14.0% | −53.0% | −91.9% |
29	| KL 50% uniform | +95.5% | −43.8% | −19.4% | −57.4% | −95.7% |
30	| KL 30% global | +46.7% | −31.9% | −10.1% | −61.3% | −82.0% |
31	| KL 50% global | +92.8% | −43.6% | −18.7% | −57.3% | −97.4% |
32	| BCE v3 50% | +268.0% | −58.8% | −35.2% | −54.0% | −90.1% |
33	| TEAL 50% † | +357.2% | −50.1% | −28.8% | −56.2% | −96.1% |
34	
35	## Key Observations
36	
37	1. **KL >> BCE >> TEAL at 50% sparsity**: KL uniform achieves PPL 11.96 vs BCE 22.51 vs TEAL 27.97. KL predictor (1000 steps) dominates both iso-compute BCE (2700 steps) and training-free TEAL.
38	
39	2. **Uniform vs Global allocation**: At 30% sparsity, uniform preserves MMLU (0.4061 vs 0.2527, +60.7% relative) while global collapses it. At 50% both collapse. Global allocation concentrates sparsity on critical layers, destroying knowledge.
40	
41	3. **PPL-downstream dissociation**: KL 40% has lower PPL (8.36) than KL 30% (8.82) yet worse MMLU (0.3068 vs 0.4061). PPL alone does not capture knowledge preservation; downstream metrics are essential.
42	
43	4. **Phase transition 30%→40%**: MMLU drops from 0.4061 to 0.3068 (−24.5pp), GSM8K from 0.0735 to 0.0394 (−3.4pp). The threshold for knowledge/reasoning retention lies between 30–40% sparsity.
44	
45	---
46	*Generated 2026-05-16. Source: distill_sparse_swiglu registry.*
47	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "f716b164-a763-4033-b921-7fe9fd43c5b1",
  "uuid": "6f848cb2-3768-4934-9374-2a59cae5ce49",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/_project/report/benchmark_comparison_table.md",
      "content": "# Unified Benchmark Comparison Table\n\n**Model**: Llama-3.1-8B | **Eval**: benchmark_eval.py (ARC-c=25-shot, WG=5-shot, MMLU=5-shot, GSM8K=8-shot, WikiText-2 PPL)\n\n## Main Results\n\n| Condition | Sparsity | Allocation | PPL | ARC-c | WG | MMLU | GSM8K |\n|-----------|----------|------------|-----|-------|-----|------|-------|\n| Dense (baseline) | 0% | — | 6.117 | 0.5828 | 0.7806 | 0.6527 | 0.4875 |\n| KL 30% | 30% | uniform | 8.816 | 0.4078 | 0.6859 | 0.4061 | 0.0735 |\n| KL 40% | 40% | uniform | 8.363 | 0.4181 | 0.6717 | 0.3068 | 0.0394 |\n| KL 50% | 50% | uniform | 11.960 | 0.3276 | 0.6290 | 0.2777 | 0.0212 |\n| KL 30% | 30% | global | 8.977 | 0.3968 | 0.7017 | 0.2527 | 0.0879 |\n| KL 50% | 50% | global | 11.793 | 0.3285 | 0.6346 | 0.2789 | 0.0129 |\n| BCE v3 (2700 steps) | 50% | learned | 22.510 | 0.2398 | 0.5059 | 0.3002 | 0.0485 |\n| TEAL 50% † | 50% | magnitude | 27.970* | 0.2910 | 0.5556 | 0.2856 | 0.0190 |\n| TEAL 50% (unified) | 50% | magnitude | — queued | — queued | — queued | — queued | — queued |\n| TEAL 30% (unified) | 30% | magnitude | — queued | — queued | — queued | — queued | — queued |\n\n† lm_eval_teal_50pct uses lm-evaluation-harness (0-shot default), not directly comparable to unified few-shot results.\n\\* TEAL PPL from eval_bce_v3_s42 `teal_sparse_ppl` measurement (same model, same WikiText-2 split).\n\n## Relative Change vs Dense (%)\n\n| Condition | PPL ↑ | ARC-c ↓ | WG ↓ | MMLU ↓ | GSM8K ↓ |\n|-----------|-------|---------|------|--------|---------|\n| KL 30% uniform | +44.1% | −30.0% | −12.1% | −37.8% | −84.9% |\n| KL 40% uniform | +36.7% | −28.3% | −14.0% | −53.0% | −91.9% |\n| KL 50% uniform | +95.5% | −43.8% | −19.4% | −57.4% | −95.7% |\n| KL 30% global | +46.7% | −31.9% | −10.1% | −61.3% | −82.0% |\n| KL 50% global | +92.8% | −43.6% | −18.7% | −57.3% | −97.4% |\n| BCE v3 50% | +268.0% | −58.8% | −35.2% | −54.0% | −90.1% |\n| TEAL 50% † | +357.2% | −50.1% | −28.8% | −56.2% | −96.1% |\n\n## Key Observations\n\n1. **KL >> BCE >> TEAL at 50% sparsity**: KL uniform achieves PPL 11.96 vs BCE 22.51 vs TEAL 27.97. KL predictor (1000 steps) dominates both iso-compute BCE (2700 steps) and training-free TEAL.\n\n2. **Uniform vs Global allocation**: At 30% sparsity, uniform preserves MMLU (0.4061 vs 0.2527, +60.7% relative) while global collapses it. At 50% both collapse. Global allocation concentrates sparsity on critical layers, destroying knowledge.\n\n3. **PPL-downstream dissociation**: KL 40% has lower PPL (8.36) than KL 30% (8.82) yet worse MMLU (0.3068 vs 0.4061). PPL alone does not capture knowledge preservation; downstream metrics are essential.\n\n4. **Phase transition 30%→40%**: MMLU drops from 0.4061 to 0.3068 (−24.5pp), GSM8K from 0.0735 to 0.0394 (−3.4pp). The threshold for knowledge/reasoning retention lies between 30–40% sparsity.\n\n---\n*Generated 2026-05-16. Source: distill_sparse_swiglu registry.*\n",
      "numLines": 47,
      "startLine": 1,
      "totalLines": 47
    }
  }
}
```

</details>

---

### Tool call

_source line 7_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01K9AMG9yMyezHFn7bLtonS4`</summary>

```json
{
  "query": "select:mcp__agent-ml-research__read_registry",
  "max_results": 1
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "f716b164-a763-4033-b921-7fe9fd43c5b1",
  "uuid": "dd6c83c3-29fe-4cad-93cd-5e344c1c72bc",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019YuNfxw94LwAp4WBCEeBbD",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12266,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12266
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

_source line 8 · 2026-05-16T16:59:50.465Z_

<details><summary>↩ Tool result · `toolu_01K9AMG9yMyezHFn7bLtonS4`</summary>

````text
```json
{
  "type": "tool_reference",
  "tool_name": "mcp__agent-ml-research__read_registry"
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
  "session_id": "f716b164-a763-4033-b921-7fe9fd43c5b1",
  "uuid": "061b6715-3243-4b6e-9a9d-c223f5f6f4d8",
  "tool_use_result": {
    "matches": [
      "mcp__agent-ml-research__read_registry"
    ],
    "query": "select:mcp__agent-ml-research__read_registry",
    "total_deferred_tools": 25
  }
}
```

</details>

---

### Assistant

_source line 9_

<details><summary>Logged reasoning block</summary>

```text
Let me read the registry to cross-verify the numbers for bench_teal30, bench_teal50, bench_kl40_global, and multi-seed data.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "f716b164-a763-4033-b921-7fe9fd43c5b1",
  "uuid": "766462f3-d6a8-43a7-93a1-1bc843e96616",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BaiV1ehAgQqnDoTVYXEqEK",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 2040,
      "cache_read_input_tokens": 24107,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2040
      },
      "output_tokens": 39,
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

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry · `toolu_01CbkcK8jPLLc2B36S8mfTiN`</summary>

```json
{
  "project": "distill_sparse_swiglu",
  "filters": {
    "exp_id": "bench_teal30"
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
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "f716b164-a763-4033-b921-7fe9fd43c5b1",
  "uuid": "c578e76d-33f7-4452-a63f-9795681d693e",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BaiV1ehAgQqnDoTVYXEqEK",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 2040,
      "cache_read_input_tokens": 24107,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2040
      },
      "output_tokens": 39,
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

_source line 11 · 2026-05-16T16:59:54.444Z_

<details><summary>↩ Tool result · `toolu_01CbkcK8jPLLc2B36S8mfTiN`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"experiments\": {}, \"count\": 0, \"total\": 0, \"baseline\": \"bench_dense\"}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.2486}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "f716b164-a763-4033-b921-7fe9fd43c5b1",
  "uuid": "bf93d86b-fde8-46dd-bee1-2e8740d0c645",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"experiments\\\": {}, \\\"count\\\": 0, \\\"total\\\": 0, \\\"baseline\\\": \\\"bench_dense\\\"}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.2486}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"experiments\": {}, \"count\": 0, \"total\": 0, \"baseline\": \"bench_dense\"}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.2486}}"
    }
  }
}
```

</details>

---

### Tool call

_source line 12_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry · `toolu_01CCRtATB24NwwbspF4Vk8UK`</summary>

```json
{
  "project": "distill_sparse_swiglu",
  "filters": {
    "exp_id": "bench_teal50"
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
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "f716b164-a763-4033-b921-7fe9fd43c5b1",
  "uuid": "9f210c7d-aa38-4192-b056-a2356cf817e5",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BaiV1ehAgQqnDoTVYXEqEK",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 2040,
      "cache_read_input_tokens": 24107,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2040
      },
      "output_tokens": 39,
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

_source line 13 · 2026-05-16T16:59:55.379Z_

<details><summary>↩ Tool result · `toolu_01CCRtATB24NwwbspF4Vk8UK`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"experiments\": {}, \"count\": 0, \"total\": 0, \"baseline\": \"bench_dense\"}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.2037}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "f716b164-a763-4033-b921-7fe9fd43c5b1",
  "uuid": "f7471be0-7b1f-4392-b0ae-100c81812b32",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"experiments\\\": {}, \\\"count\\\": 0, \\\"total\\\": 0, \\\"baseline\\\": \\\"bench_dense\\\"}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.2037}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"experiments\": {}, \"count\": 0, \"total\": 0, \"baseline\": \"bench_dense\"}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.2037}}"
    }
  }
}
```

</details>

---

### Tool call

_source line 14_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry · `toolu_01NeQQoypPuq3gwt192HwNEJ`</summary>

```json
{
  "project": "distill_sparse_swiglu",
  "filters": {
    "exp_id": "bench_kl40_global"
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
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "f716b164-a763-4033-b921-7fe9fd43c5b1",
  "uuid": "0d6234fc-a267-4bb2-b4c8-749839b285ab",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BaiV1ehAgQqnDoTVYXEqEK",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 2040,
      "cache_read_input_tokens": 24107,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2040
      },
      "output_tokens": 39,
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

_source line 15 · 2026-05-16T16:59:55.708Z_

<details><summary>↩ Tool result · `toolu_01NeQQoypPuq3gwt192HwNEJ`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"experiments\": {}, \"count\": 0, \"total\": 0, \"baseline\": \"bench_dense\"}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.2461}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "f716b164-a763-4033-b921-7fe9fd43c5b1",
  "uuid": "a2a0a022-7f97-4e03-aa0d-d5e66ac2969d",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"experiments\\\": {}, \\\"count\\\": 0, \\\"total\\\": 0, \\\"baseline\\\": \\\"bench_dense\\\"}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.2461}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"experiments\": {}, \"count\": 0, \"total\": 0, \"baseline\": \"bench_dense\"}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.2461}}"
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
The exact exp_id filter didn't match. Let me try broader searches to find these experiments.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "f716b164-a763-4033-b921-7fe9fd43c5b1",
  "uuid": "cf26bd2a-6625-4a4b-bbdf-1ceff96a4bbb",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Rpyz9tEJvZVX5g8c1RUQg7",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 693,
      "cache_read_input_tokens": 26147,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 693
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

Exact IDs didn't match. Let me search more broadly.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "f716b164-a763-4033-b921-7fe9fd43c5b1",
  "uuid": "f5321655-e0d0-4deb-a96d-7b0a2b9bd7cd",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Rpyz9tEJvZVX5g8c1RUQg7",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 693,
      "cache_read_input_tokens": 26147,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 693
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

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry · `toolu_01EHNzr2AoxC3hsqQ96HuiVr`</summary>

```json
{
  "project": "distill_sparse_swiglu",
  "filters": {
    "status": "DONE"
  },
  "fields": [
    "exp_id",
    "status",
    "metrics",
    "conclusion"
  ],
  "limit": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "f716b164-a763-4033-b921-7fe9fd43c5b1",
  "uuid": "4d4edf3e-39d8-4926-8b4c-10285610da67",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Rpyz9tEJvZVX5g8c1RUQg7",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 693,
      "cache_read_input_tokens": 26147,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 693
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

_source line 19 · 2026-05-16T17:00:00.298Z_

<details><summary>↩ Tool result · `toolu_01EHNzr2AoxC3hsqQ96HuiVr`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"experiments\": {\"longbench_dense_v6\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"longbench_narrativeqa\": 7.3, \"longbench_qasper\": 13.4, \"longbench_gov_report\": 30.5, \"longbench_multi_news\": 2.5}}, \"bench_kl50_uniform_s456\": {\"status\": \"DONE\", \"metrics\": {\"wikitext2_ppl\": 11.9604, \"arc_challenge_acc_norm\": 0.3345, \"winogrande_acc\": 0.6275, \"mmlu_acc\": 0.2874, \"gsm8k_exact_match\": 0.0212, \"actual_sparsity\": 0.5}, \"conclusion\": \"success\"}, \"bench_kl50_uniform_s123\": {\"status\": \"DONE\", \"metrics\": {\"wikitext2_ppl\": 11.83, \"arc_challenge_acc_norm\": 0.3515, \"winogrande_acc\": 0.6298, \"mmlu_acc\": 0.2751, \"gsm8k_exact_match\": 0.0235, \"actual_sparsity\": 0.5}, \"conclusion\": \"success\"}, \"latency_benchmark\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"gpu_model\": \"NVIDIA RTX PRO 6000 Blackwell Server Edition\", \"dtype\": \"float16\", \"attn\": \"flash_attention_2\", \"batch\": 1, \"seq_len\": 2048, \"warmup\": 10, \"iters\": 100, \"dense_ms\": 119.11, \"dense_std\": 0.57, \"dense_tokens_per_s\": 17194.5, \"kl_30pct_ms\": 126.64, \"kl_30pct_std\": 0.7, \"kl_30pct_tokens_per_s\": 16171.8, \"kl_30pct_speedup\": 0.941, \"kl_50pct_ms\": 126.78, \"kl_50pct_std\": 0.31, \"kl_50pct_tokens_per_s\": 16154.2, \"kl_50pct_speedup\": 0.939, \"comp_30pct_ms\": 129.94, \"comp_30pct_std\": 0.75, \"comp_30pct_tokens_per_s\": 15761.4, \"comp_30pct_speedup\": 0.917, \"comp_50pct_ms\": 129.71, \"comp_50pct_std\": 0.53, \"comp_50pct_tokens_per_s\": 15788.8, \"comp_50pct_speedup\": 0.918, \"predictor_overhead_ms\": 3.17, \"predictor_overhead_pct\": 2.7, \"per_layer_predictor_ms\": 0.099, \"dense_ffn_per_layer_ms\": 2.427, \"sparse_ffn_pred_per_layer_ms\": 2.686, \"compensation_overhead_ms\": 3.3}}, \"longbench_dense_v4\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"longbench_dense\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"longbench_kl30_uniform\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"bench_kl40_global\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"wikitext2_ppl\": 10.117, \"arc_challenge_acc_norm\": 0.4096, \"winogrande_acc\": 0.6535, \"mmlu_acc\": 0.3806, \"gsm8k_exact_match\": 0.05, \"actual_sparsity\": 0.4}}, \"bench_kl50_uniform\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"wikitext2_ppl\": 11.963, \"arc_challenge_acc_norm\": 0.3276, \"winogrande_acc\": 0.629, \"mmlu_acc\": 0.2777, \"gsm8k_exact_match\": 0.0212, \"actual_sparsity\": 0.5}}, \"bench_teal50\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"wikitext2_ppl\": 23.31, \"arc_challenge_acc_norm\": 0.2841, \"winogrande_acc\": 0.5304, \"mmlu_acc\": 0.2832, \"gsm8k_exact_match\": 0.0197, \"actual_sparsity\": 0.5}}, \"bench_teal30\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"wikitext2_ppl\": 10.97, \"arc_challenge_acc_norm\": 0.4232, \"winogrande_acc\": 0.6606, \"mmlu_acc\": 0.3861, \"gsm8k_exact_match\": 0.0788, \"actual_sparsity\": 0.3}}, \"bench_kl50_global\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"wikitext2_ppl\": 11.7933, \"arc_challenge_acc_norm\": 0.3285, \"winogrande_acc\": 0.6346, \"mmlu_acc\": 0.2789, \"gsm8k_exact_match\": 0.0129, \"actual_sparsity\": 0.5}}, \"bench_kl30_global\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"wikitext2_ppl\": 8.9768, \"arc_challenge_acc_norm\": 0.3968, \"winogrande_acc\": 0.7017, \"mmlu_acc\": 0.2527, \"gsm8k_exact_match\": 0.0879, \"actual_sparsity\": 0.3}}, \"bench_kl30_uniform\": {\"status\": \"DONE\", \"metrics\": {\"wikitext2_ppl\": 8.8157, \"arc_challenge_acc_norm\": 0.4078, \"winogrande_acc\": 0.6859, \"mmlu_acc\": 0.4061, \"gsm8k_exact_match\": 0.0735, \"actual_sparsity\": 0.3}, \"conclusion\": \"success\"}, \"d030_kl40_uniform\": {\"status\": \"DONE\", \"metrics\": {\"wikitext2_ppl\": 8.3627, \"arc_challenge_acc_norm\": 0.4181, \"winogrande_acc\": 0.6717, \"mmlu_acc\": 0.3068, \"gsm8k_exact_match\": 0.0394, \"actual_sparsity\": 0.398}, \"conclusion\": \"success\"}, \"eval_bce_v3_s42\": {\"status\": \"DONE\", \"metrics\": {\"dense_ppl\": 6.12, \"predictor_hard_mask_ppl\": 22.51, \"teal_sparse_ppl\": 27.97, \"model_level_sparsity\": 0.5, \"arc_challenge_acc\": 0.2048, \"arc_challenge_acc_norm\": 0.2398, \"arc_challenge_acc_norm_stderr\": 0.0125, \"winogrande_acc\": 0.5059, \"winogrande_acc_stderr\": 0.0141, \"mmlu_acc\": 0.3002, \"mmlu_acc_stderr\": 0.0038, \"gsm8k_exact_match\": 0.0485, \"gsm8k_exact_match_strict\": 0.0425, \"gsm8k_exact_match_stderr\": 0.0059}, \"conclusion\": \"success\"}, \"bench_dense\": {\"status\": \"DONE\", \"metrics\": {\"wikitext2_ppl\": 6.1173, \"arc_challenge_acc\": 0.5478, \"arc_challenge_acc_norm\": 0.5828, \"winogrande_acc\": 0.7806, \"mmlu_acc\": 0.6527, \"gsm8k_exact_match\": 0.4875}, \"conclusion\": \"success\"}, \"kl_sparsity30_s42_v3\": {\"status\": \"DONE\", \"metrics\": {\"loss\": 0.165, \"kl_normalized\": 0.165, \"kl_raw\": 0.165, \"sparsity\": 0.285, \"lambda_sparse\": 5000, \"tau\": 0.1, \"constraint_loss\": 0, \"steps\": 1000, \"true_dense_ppl\": 6.12, \"predictor_hard_mask_ppl\": 7.3, \"teal_sparse_ppl\": 8.98, \"teal_sparse_ppl_note\": \"已通过 eval_kl30_teal_30pct 独立验证 (sparsity_target=0.3, D034)\", \"model_level_sparsity\": 0.3, \"eval_dataset\": \"wikitext-2\", \"eval_seq_len\": 2048}, \"conclusion\": \"success\"}, \"eval_kl30_teal_30pct\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"dense_ppl\": 6.12, \"predictor_hard_mask_ppl\": 7.3, \"teal_sparse_ppl\": 8.98, \"sparsity_target\": 0.3, \"actual_sparsity\": 0.3}}, \"bce_isocompute_v3_s42\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"steps\": 2700, \"loss\": 0.6382, \"bce_loss\": 0.6371, \"reg_loss\": 0.001, \"sparsity\": 0.51, \"training_time_seconds\": 2828, \"note\": \"BCE saturation confirmed: step 500→2700 only 0.006 improvement\"}}, \"bench_mistral_kl50_s42\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"d030_kl50_uniform\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"wikitext2_ppl\": 11.96, \"arc_challenge_acc_norm\": 0.3276, \"winogrande_acc\": 0.629, \"mmlu_acc\": 0.2777, \"gsm8k_exact_match\": 0.0212, \"actual_sparsity\": 0.5, \"allocation\": \"uniform\", \"per_layer_sparsity\": \"uniform 0.500 across all 32 layers\", \"mmlu_change_vs_global\": \"+1.86pp (0.2591 → 0.2777, not significant)\", \"gsm8k_change_vs_global\": \"+0.91pp (0.0121 → 0.0212, not significant)\", \"conclusion_note\": \"50% uniform 未能修复 MMLU/GSM8K collapse. Uniform allocation 的修复效应在 50% sparsity 下消失。\"}}, \"lm_eval_teal_50pct\": {\"status\": \"DONE\", \"metrics\": {\"method\": \"vanilla_teal\", \"sparsity\": 0.5, \"actual_sparsity\": 0.5, \"arc_challenge_acc_norm\": 0.291, \"winogrande_acc\": 0.5556, \"mmlu_acc\": 0.2856, \"gsm8k_exact_match_flexible\": 0.019, \"gsm8k_exact_match_strict\": 0.0114, \"arc_challenge_drop_vs_dense\": -0.5, \"winogrande_drop_vs_dense\": -0.289, \"mmlu_drop_vs_dense\": -0.563, \"gsm8k_drop_vs_dense\": -0.962, \"model\": \"Llama-3.1-8B\", \"condition\": \"TEAL 50% training-free sparsity\"}, \"conclusion\": \"success\"}, \"d030_kl30_uniform\": {\"status\": \"DONE\", \"metrics\": {\"wikitext2_ppl\": 8.8157, \"arc_challenge_acc_norm\": 0.4078, \"winogrande_acc\": 0.6859, \"mmlu_acc\": 0.4061, \"gsm8k_exact_match\": 0.0735, \"actual_sparsity\": 0.3, \"allocation\": \"uniform\", \"per_layer_sparsity\": \"uniform 0.301 across all 32 layers\", \"mmlu_improvement_vs_global\": \"+11.87pp (0.2874 → 0.4061)\", \"gsm8k_change_vs_global\": \"no change (0.0743 → 0.0735, within noise)\"}, \"conclusion\": \"success\"}, \"mistral_kl_s42\": {\"status\": \"DONE\", \"metrics\": {\"train_final_loss\": 0.2188, \"train_final_kl_raw\": 0.2188, \"train_final_kl_norm\": 0.2188, \"train_final_constraint\": 0, \"train_final_sparsity\": 0.48, \"train_final_lambda\": 1000, \"train_final_tau\": 0.1, \"train_steps_completed\": 1000, \"true_dense_ppl\": 5.52, \"predictor_hard_mask_ppl\": 7.3, \"teal_sparse_ppl\": 8.98, \"model_level_sparsity\": 0.5, \"eval_dataset\": \"wikitext-2\", \"eval_seq_len\": 2048, \"calibration_samples\": 32, \"eval_samples\": 159}, \"conclusion\": \"success\"}, \"lm_eval_mistral_kl_50pct\": {\"status\": \"DONE\", \"conclusion\": \"negative\", \"metrics\": {\"arc_challenge_acc\": 0.2927, \"arc_challenge_acc_norm\": 0.3183, \"arc_challenge_acc_norm_stderr\": 0.0136, \"winogrande_acc\": 0.629, \"winogrande_acc_stderr\": 0.0136, \"mmlu_acc\": 0.2295, \"mmlu_acc_stderr\": 0.0035, \"mmlu_stem_acc\": 0.2125, \"mmlu_humanities_acc\": 0.2421, \"mmlu_social_sciences_acc\": 0.2171, \"mmlu_other_acc\": 0.2398, \"gsm8k_exact_match_strict\": 0.0045, \"gsm8k_exact_match_flexible\": 0.0212, \"model\": \"Mistral-7B-v0.3\", \"condition\": \"kl_distill_50pct_sparsity_s42\", \"arc_challenge_retention_vs_dense\": 0.528, \"winogrande_retention_vs_dense\": 0.799, \"mmlu_retention_vs_dense\": 0.368, \"gsm8k_retention_vs_dense\": 0.012}}, \"lm_eval_teal_30pct\": {\"status\": \"DONE\", \"metrics\": {\"arc_challenge\": {\"acc\": 0.3933, \"acc_norm\": 0.4155, \"acc_stderr\": 0.0143, \"acc_norm_stderr\": 0.0144}, \"winogrande\": {\"acc\": 0.6559, \"acc_stderr\": 0.0134}, \"mmlu\": {\"acc\": 0.3598, \"acc_stderr\": 0.004}, \"mmlu_stem\": {\"acc\": 0.313}, \"mmlu_humanities\": {\"acc\": 0.3305}, \"mmlu_social_sciences\": {\"acc\": 0.4108}, \"mmlu_other\": {\"acc\": 0.401}, \"gsm8k\": {\"exact_match_strict\": 0.0849, \"exact_match_flexible\": 0.0925, \"strict_stderr\": 0.0077, \"flexible_stderr\": 0.008}, \"actual_sparsity\": 0.3}, \"conclusion\": \"negative\"}, \"lm_eval_kl_30pct_s42\": {\"status\": \"DONE\", \"metrics\": {\"arc_challenge_acc\": 0.3575, \"arc_challenge_acc_norm\": 0.3737, \"winogrande_acc\": 0.6756, \"mmlu_acc\": 0.2874, \"gsm8k_exact_match_strict\": 0.0743, \"gsm8k_exact_match_flexible\": 0.0781, \"actual_sparsity\": 0.3, \"model\": \"llama-3.1-8b\", \"condition\": \"kl_distill_30pct_sparsity_s42\", \"mmlu_stem_acc\": 0.2499, \"mmlu_social_sciences_acc\": 0.2896, \"mmlu_humanities_acc\": 0.2786, \"mmlu_other_acc\": 0.3363}, \"conclusion\": \"negative\"}, \"bce_isocompute_s42_v2\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval_spon_supp_retry\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"lm_eval_dense_test\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"lm_eval_mistral_downstream\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"mvp_kl_s123\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"mvp_kl_s456\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"lm_eval_mistral_dense\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"arc_challenge_acc_norm\": 0.6024, \"winogrande_acc\": 0.7869, \"mmlu_acc\": 0.6244, \"gsm8k_exact_match\": 0.3654, \"model\": \"Mistral-7B-v0.3\", \"condition\": \"dense\", \"server\": \"westd-34887\"}}, \"lm_eval_kl_s42\": {\"status\": \"DONE\", \"metrics\": {\"arc_challenge_acc_norm\": 0.3771, \"winogrande_acc\": 0.6156, \"mmlu_acc\": 0.2591, \"gsm8k_exact_match\": 0.0121, \"eval_tasks\": [\"arc_challenge\", \"winogrande\", \"mmlu\", \"gsm8k\"], \"model\": \"llama-3.1-8b\", \"condition\": \"kl_sparse_50pct\", \"server\": \"westd-34887\", \"exit_code\": 129, \"wall_time_sec\": 3010, \"flag\": \"SUSPECT — gsm8k 0.50→0.01 catastrophic drop; PID 179918 rerunning with lm_eval_sparse.py\"}, \"conclusion\": \"negative\"}, \"gsm8k_gen_compare\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"kl_sparsity70_s42_v2\": {\"status\": \"DONE\", \"metrics\": {\"true_dense_ppl\": 6.12, \"predictor_hard_mask_ppl\": 13.84, \"predictor_teal_sparse_ppl\": 17.91, \"vanilla_teal_sparse_ppl\": 100.11, \"teal_sparse_ppl\": 17.91, \"teal_sparse_ppl_static_baseline\": 17.91, \"model_level_sparsity\": 0.7, \"teal_sparse_note\": \"17.91 = predictor-based TEAL (teal_global_masks: predictor-gated magnitude scoring + global topk @70%). vanilla TEAL @70% = 100.11. 代码来源: quick_sp70.py L10 imports teal_global_masks, L60 调用. plan_007_all_ppl_fixed.json 的 mode=static_mask_70pct metadata 有误导性.\", \"eval_dataset\": \"wikitext-2\", \"eval_seq_len\": 2048, \"calibration_samples\": 32, \"per_layer_sparsity_range\": [0.508, 0.876]}, \"conclusion\": \"success\"}, \"training_free_baselines\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"dense_ppl\": 6.12, \"vanilla_teal_global_ppl_30pct\": 10.97, \"vanilla_teal_global_ppl_50pct\": 23.31, \"vanilla_teal_global_ppl_70pct\": 100.11, \"wina_global_ppl_30pct\": 11.45, \"wina_global_ppl_50pct\": 27.93, \"wina_global_ppl_70pct\": 137.24, \"uniform_50pct_ppl\": 23.9, \"teal_greedy_ppl\": 33.47, \"vanilla_teal_global_ppl\": 23.31, \"wina_global_ppl\": 27.93, \"rsparse_global_ppl\": 151.2}}, \"lm_eval_dense\": {\"status\": \"DONE\", \"metrics\": {\"arc_challenge_acc_norm\": 0.5819, \"winogrande_acc\": 0.7814, \"mmlu_acc\": 0.6532, \"gsm8k_exact_match\": 0.5004, \"eval_tasks\": [\"arc_challenge\", \"winogrande\", \"mmlu\", \"gsm8k\"], \"model\": \"llama-3.1-8b\", \"condition\": \"dense\", \"server\": \"westd-34887\"}, \"conclusion\": \"success\"}, \"kl_sparsity30_s42_v2\": {\"status\": \"DONE\", \"conclusion\": \"negative\", \"metrics\": {\"final_loss\": 0.1465, \"kl_normalized\": 0.1465, \"kl_raw\": 0.1465, \"model_level_sparsity\": 0.281, \"sparsity_target\": 0.3, \"lambda_sparse_final\": 1000, \"lambda_max_cap\": 1000, \"tau_final\": 0.1, \"constraint_loss_final\": 0, \"training_steps\": 1000, \"wall_clock_seconds\": 2662.6, \"gpu_hours\": 0.74, \"note\": \"No PPL evaluation in training script. Sparsity stuck at 0.281 (same as v1). Lambda hit cap=1000 by step 220 and could not push sparsity further. W&B run was offline (not synced).\"}}, \"bce_isocompute_v2_s42\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"final_loss\": 0.6637, \"final_bce_loss\": 0.6586, \"final_reg_loss\": 0.0051, \"final_sparsity\": 0.502, \"training_steps\": 1000, \"training_time_sec\": 1047.8, \"reg_weight\": 2, \"true_dense_ppl\": 6.12, \"predictor_hard_mask_ppl\": 26.76, \"teal_sparse_ppl\": 54.84, \"eval_seq_len\": 2048, \"eval_dataset\": \"wikitext-2\"}}, \"kl_sparsity70_s42\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"kl_sparsity30_s42\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"plan_005_subsumption_s42\": {\"status\": \"DONE\", \"metrics\": {\"linearity_ratio\": 0.2644, \"linearity_ratio_std\": 0.0073, \"magnitude_ratio\": 0.1578, \"magnitude_ratio_std\": 0.0088, \"cosine_similarity\": 0.1962, \"cosine_similarity_std\": 0.0268, \"predictor_effect_norm\": 482.65, \"spon_correction_norm\": 76.2, \"interaction_norm\": 147.74, \"num_samples\": 50, \"seq_len\": 2048, \"conclusion_type\": \"weak_subsumption\"}, \"conclusion\": \"success\"}, \"ste_baseline_s42\": {\"status\": \"DONE\", \"metrics\": {\"true_dense_ppl\": 6.12, \"predictor_hard_mask_ppl\": 8.18, \"teal_sparse_ppl\": 15.77, \"model_level_sparsity\": 0.47, \"ppl_increase_vs_true_dense_pct\": 157.7, \"eval_seq_len\": 2048, \"calibration_samples\": 32, \"eval_dataset\": \"wikitext-2\", \"per_token_sparsity\": 0.47, \"lambda_stats\": {\"steps_70_130_mean\": 66.4, \"steps_70_130_std\": 94.87, \"first_500_mean\": 688.07, \"first_500_std\": 440.57, \"last_500_mean\": 965.69, \"last_500_std\": 141.59, \"overall_mean\": 826.88, \"overall_std\": 354.23}}, \"conclusion\": \"success\"}, \"spon_supp_eval_retry\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"spon_2048_s42\": {\"status\": \"DONE\", \"conclusion\": \"negative\", \"metrics\": {\"true_dense_ppl\": 6.1173, \"predictor_hard_mask_ppl\": 9.2165, \"spon_sparse_ppl\": 8.991, \"spon_recovery_pct\": 7.3, \"ppl_improvement_from_spon\": 0.2255, \"mean_bias_norm\": 0.05312, \"max_bias_norm\": 0.065918, \"model_level_sparsity\": 0.498, \"eval_seq_len\": 2048, \"training_seq_len\": 2048, \"eval_samples\": 141, \"trainable_params\": 458752, \"trainable_pct\": 0.0057, \"training_steps\": 1000, \"final_loss\": 0.377, \"dense_with_spon_ppl\": 6.1823, \"dense_ppl_degradation\": 0.0651, \"teal_sparse_no_spon_ppl\": 12.0776, \"teal_sparse_with_spon_ppl\": 11.7907, \"spon_recovery_teal_pct\": 4.8, \"teal_sparsity\": 0.4979}}, \"bce_isocompute_s42\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"mvp_kl_norm_v2_s456\": {\"status\": \"DONE\", \"metrics\": {\"true_dense_ppl\": 6.1173, \"predictor_hard_mask_ppl\": 9.14, \"teal_sparse_ppl\": 13.58, \"model_level_sparsity\": 0.498, \"ppl_increase_vs_true_dense_pct\": 121.9, \"eval_md5\": \"f4086818bb55dc354ea4c6fe8ed8899a\", \"calibration_samples\": 32, \"vanilla_teal_sparse_ppl_INVALID\": 66036.4062}, \"conclusion\": \"success\"}, \"spon_training\": {\"status\": \"DONE\", \"conclusion\": \"negative\", \"metrics\": {\"true_dense_ppl\": 6.1193, \"predictor_hard_mask_ppl\": 9.2165, \"spon_sparse_ppl\": 9.0977, \"spon_recovery_pct\": 3.8, \"ppl_improvement_from_spon\": 0.1188, \"ppl_increase_vs_true_dense_pct\": 48.7, \"ppl_increase_no_spon_vs_true_dense_pct\": 50.6, \"mean_bias_norm\": 0.040596, \"max_bias_norm\": 0.054199, \"teal_sparse_ppl\": 12.08, \"teal_with_spon_ppl\": 11.93, \"spon_dense_ppl_degradation\": 6.19, \"model_level_sparsity\": 0.5, \"eval_seq_len\": 2048, \"eval_samples\": 141, \"trainable_params\": 458752, \"trainable_pct\": 0.0057}}, \"training_free_wina_greedy\": {\"status\": \"DONE\", \"conclusion\": \"negative\", \"metrics\": {\"wina_greedy_ppl\": 2126.03, \"dense_ppl\": 6.12, \"model_level_sparsity\": 0.5, \"eval_dataset\": \"WikiText-2\", \"eval_seq_len\": 2048, \"greedy_allocation_summary\": \"layers 0-11: 0.90, layer 12: 0.85, layer 13: 0.80, layer 14: 0.70, layers 15-16: 0.50-0.55, layers 17-20: 0.30-0.35, layers 21-24: 0.05-0.15, layers 25-31: 0.00\"}}, \"ste_kl_s42\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"bce_comp_staged_s42\": {\"status\": \"DONE\", \"conclusion\": \"negative\", \"metrics\": {\"true_dense_ppl\": 6.12, \"predictor_hard_mask_ppl\": 25.44, \"predictor_hard_mask_ppl_no_comp\": 27.96, \"teal_sparse_ppl\": 44.54, \"model_level_sparsity\": 0.558, \"ppl_increase_vs_true_dense_pct\": 315.7, \"comp_loss_final\": 0.0033, \"bce_loss_final\": 0.6379, \"eval_seq_len\": 2048, \"calibration_samples\": 32}}, \"spon_training_seq2048\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"kl_only_s0\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"true_dense_ppl\": 6.12, \"predictor_hard_mask_ppl\": 9.19, \"teal_sparse_ppl\": 12.03, \"model_level_sparsity\": 0.499, \"ppl_increase_vs_true_dense_pct\": 96.57, \"eval_seq_len\": 2048, \"calibration_samples\": 32}}, \"kl_only_s1\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"true_dense_ppl\": 6.12, \"predictor_hard_mask_ppl\": 9.15, \"teal_sparse_ppl\": 11.99, \"model_level_sparsity\": 0.498, \"ppl_increase_vs_true_dense_pct\": 96}}, \"mvp_bce_s456\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"true_dense_ppl\": 6.1173, \"predictor_hard_mask_ppl\": 28.1437, \"teal_sparse_ppl\": 43.033, \"model_level_sparsity\": 0.4957, \"ppl_increase_vs_true_dense_pct\": 603.3, \"eval_md5\": \"f4086818bb55dc354ea4c6fe8ed8899a\", \"calibration_samples\": 32, \"vanilla_teal_sparse_ppl_INVALID\": 66036.4062}}, \"mvp_bce_s123\": {\"status\": \"DONE\", \"metrics\": {\"true_dense_ppl\": 6.1173, \"predictor_hard_mask_ppl\": 28.3817, \"teal_sparse_ppl\": 44.5864, \"model_level_sparsity\": 0.4957, \"ppl_increase_vs_true_dense_pct\": 629, \"eval_md5\": \"f4086818bb55dc354ea4c6fe8ed8899a\", \"calibration_samples\": 32, \"vanilla_teal_sparse_ppl_INVALID\": 66036.4062}, \"conclusion\": \"success\"}, \"mvp_bce_s42\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"true_dense_ppl\": 6.1173, \"predictor_hard_mask_ppl\": 27.9603, \"teal_sparse_ppl\": 44.537, \"model_level_sparsity\": 0.4957, \"ppl_increase_vs_true_dense_pct\": 628, \"eval_md5\": \"f4086818bb55dc354ea4c6fe8ed8899a\", \"calibration_samples\": 32, \"vanilla_teal_sparse_ppl_INVALID\": 66036.4062}}, \"mvp_kl_norm_v2_s123\": {\"status\": \"DONE\", \"metrics\": {\"true_dense_ppl\": 6.1173, \"predictor_hard_mask_ppl\": 9.2474, \"teal_sparse_ppl\": 11.9128, \"model_level_sparsity\": 0.4979, \"ppl_increase_vs_true_dense_pct\": 94.7, \"eval_md5\": \"f4086818bb55dc354ea4c6fe8ed8899a\", \"calibration_samples\": 32, \"vanilla_teal_sparse_ppl_INVALID\": 66036.4062}, \"conclusion\": \"success\"}, \"mvp_kl_norm_v2_s42\": {\"status\": \"DONE\", \"metrics\": {\"true_dense_ppl\": 6.1173, \"predictor_hard_mask_ppl\": 9.2142, \"teal_sparse_ppl\": 12.0776, \"model_level_sparsity\": 0.4979, \"ppl_increase_vs_true_dense_pct\": 97.4, \"eval_md5\": \"f4086818bb55dc354ea4c6fe8ed8899a\", \"calibration_samples\": 32, \"vanilla_teal_sparse_ppl_INVALID\": 66036.4062}, \"conclusion\": \"success\"}, \"mvp_kl_norm_s123\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"mvp_kl_norm_s42\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"kl_normalized_quicktest\": {\"status\": \"DONE\", \"conclusion\": \"failed\", \"metrics\": {\"step1_kl\": 1.18, \"step200_kl\": 0.641, \"step200_sparsity\": 0.504, \"final_lambda\": 8, \"sparsity_converged_step\": 80, \"sparsity_trajectory\": [0.406, 0.398, 0.398, 0.457, 0.52, 0.506, 0.504, 0.504], \"lambda_trajectory\": [1, 2, 4, 8, 8, 8, 8, 8]}}, \"kl_lagrangian_quicktest\": {\"status\": \"DONE\", \"conclusion\": \"negative\", \"metrics\": {\"final_kl_loss\": 418, \"final_constraint_loss\": 1.211, \"final_sparsity\": 0.141, \"final_lambda\": 5.06, \"steps\": 200, \"sparsity_trajectory\": [0.406, 0.387, 0.289, 0.168, 0.141]}}, \"mvp_kl_s42\": {\"status\": \"DONE\", \"conclusion\": \"negative\", \"metrics\": {\"final_total_loss\": 3.3438, \"final_kl_loss\": 3.2969, \"final_reg_loss\": 0.05, \"final_sparsity\": 0, \"steps\": 1000, \"tau_final\": 0.1, \"wikitext2_ppl_dense\": 6.12, \"wikitext2_ppl_sparse\": 455.93, \"wikitext2_ppl_increase_pct\": 7349, \"model_level_sparsity\": 0.372, \"checkpoint_path\": \"/root/distill_sparse_swiglu/checkpoints/mvp_kl_s42/predictor_kl.pt\"}}}, \"count\": 67, \"total\": 67, \"baseline\": \"bench_dense\"}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.2689}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "f716b164-a763-4033-b921-7fe9fd43c5b1",
  "uuid": "0ca6fa19-96bd-44a8-8eff-1916010101c5",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"experiments\\\": {\\\"longbench_dense_v6\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"longbench_narrativeqa\\\": 7.3, \\\"longbench_qasper\\\": 13.4, \\\"longbench_gov_report\\\": 30.5, \\\"longbench_multi_news\\\": 2.5}}, \\\"bench_kl50_uniform_s456\\\": {\\\"status\\\": \\\"DONE\\\", \\\"metrics\\\": {\\\"wikitext2_ppl\\\": 11.9604, \\\"arc_challenge_acc_norm\\\": 0.3345, \\\"winogrande_acc\\\": 0.6275, \\\"mmlu_acc\\\": 0.2874, \\\"gsm8k_exact_match\\\": 0.0212, \\\"actual_sparsity\\\": 0.5}, \\\"conclusion\\\": \\\"success\\\"}, \\\"bench_kl50_uniform_s123\\\": {\\\"status\\\": \\\"DONE\\\", \\\"metrics\\\": {\\\"wikitext2_ppl\\\": 11.83, \\\"arc_challenge_acc_norm\\\": 0.3515, \\\"winogrande_acc\\\": 0.6298, \\\"mmlu_acc\\\": 0.2751, \\\"gsm8k_exact_match\\\": 0.0235, \\\"actual_sparsity\\\": 0.5}, \\\"conclusion\\\": \\\"success\\\"}, \\\"latency_benchmark\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"gpu_model\\\": \\\"NVIDIA RTX PRO 6000 Blackwell Server Edition\\\", \\\"dtype\\\": \\\"float16\\\", \\\"attn\\\": \\\"flash_attention_2\\\", \\\"batch\\\": 1, \\\"seq_len\\\": 2048, \\\"warmup\\\": 10, \\\"iters\\\": 100, \\\"dense_ms\\\": 119.11, \\\"dense_std\\\": 0.57, \\\"dense_tokens_per_s\\\": 17194.5, \\\"kl_30pct_ms\\\": 126.64, \\\"kl_30pct_std\\\": 0.7, \\\"kl_30pct_tokens_per_s\\\": 16171.8, \\\"kl_30pct_speedup\\\": 0.941, \\\"kl_50pct_ms\\\": 126.78, \\\"kl_50pct_std\\\": 0.31, \\\"kl_50pct_tokens_per_s\\\": 16154.2, \\\"kl_50pct_speedup\\\": 0.939, \\\"comp_30pct_ms\\\": 129.94, \\\"comp_30pct_std\\\": 0.75, \\\"comp_30pct_tokens_per_s\\\": 15761.4, \\\"comp_30pct_speedup\\\": 0.917, \\\"comp_50pct_ms\\\": 129.71, \\\"comp_50pct_std\\\": 0.53, \\\"comp_50pct_tokens_per_s\\\": 15788.8, \\\"comp_50pct_speedup\\\": 0.918, \\\"predictor_overhead_ms\\\": 3.17, \\\"predictor_overhead_pct\\\": 2.7, \\\"per_layer_predictor_ms\\\": 0.099, \\\"dense_ffn_per_layer_ms\\\": 2.427, \\\"sparse_ffn_pred_per_layer_ms\\\": 2.686, \\\"compensation_overhead_ms\\\": 3.3}}, \\\"longbench_dense_v4\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"failed\\\"}, \\\"longbench_dense\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"failed\\\"}, \\\"longbench_kl30_uniform\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"failed\\\"}, \\\"bench_kl40_global\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"wikitext2_ppl\\\": 10.117, \\\"arc_challenge_acc_norm\\\": 0.4096, \\\"winogrande_acc\\\": 0.6535, \\\"mmlu_acc\\\": 0.3806, \\\"gsm8k_exact_match\\\": 0.05, \\\"actual_sparsity\\\": 0.4}}, \\\"bench_kl50_uniform\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"wikitext2_ppl\\\": 11.963, \\\"arc_challenge_acc_norm\\\": 0.3276, \\\"winogrande_acc\\\": 0.629, \\\"mmlu_acc\\\": 0.2777, \\\"gsm8k_exact_match\\\": 0.0212, \\\"actual_sparsity\\\": 0.5}}, \\\"bench_teal50\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"wikitext2_ppl\\\": 23.31, \\\"arc_challenge_acc_norm\\\": 0.2841, \\\"winogrande_acc\\\": 0.5304, \\\"mmlu_acc\\\": 0.2832, \\\"gsm8k_exact_match\\\": 0.0197, \\\"actual_sparsity\\\": 0.5}}, \\\"bench_teal30\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"wikitext2_ppl\\\": 10.97, \\\"arc_challenge_acc_norm\\\": 0.4232, \\\"winogrande_acc\\\": 0.6606, \\\"mmlu_acc\\\": 0.3861, \\\"gsm8k_exact_match\\\": 0.0788, \\\"actual_sparsity\\\": 0.3}}, \\\"bench_kl50_global\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"wikitext2_ppl\\\": 11.7933, \\\"arc_challenge_acc_norm\\\": 0.3285, \\\"winogrande_acc\\\": 0.6346, \\\"mmlu_acc\\\": 0.2789, \\\"gsm8k_exact_match\\\": 0.0129, \\\"actual_sparsity\\\": 0.5}}, \\\"bench_kl30_global\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"wikitext2_ppl\\\": 8.9768, \\\"arc_challenge_acc_norm\\\": 0.3968, \\\"winogrande_acc\\\": 0.7017, \\\"mmlu_acc\\\": 0.2527, \\\"gsm8k_exact_match\\\": 0.0879, \\\"actual_sparsity\\\": 0.3}}, \\\"bench_kl30_uniform\\\": {\\\"status\\\": \\\"DONE\\\", \\\"metrics\\\": {\\\"wikitext2_ppl\\\": 8.8157, \\\"arc_challenge_acc_norm\\\": 0.4078, \\\"winogrande_acc\\\": 0.6859, \\\"mmlu_acc\\\": 0.4061, \\\"gsm8k_exact_match\\\": 0.0735, \\\"actual_sparsity\\\": 0.3}, \\\"conclusion\\\": \\\"success\\\"}, \\\"d030_kl40_uniform\\\": {\\\"status\\\": \\\"DONE\\\", \\\"metrics\\\": {\\\"wikitext2_ppl\\\": 8.3627, \\\"arc_challenge_acc_norm\\\": 0.4181, \\\"winogrande_acc\\\": 0.6717, \\\"mmlu_acc\\\": 0.3068, \\\"gsm8k_exact_match\\\": 0.0394, \\\"actual_sparsity\\\": 0.398}, \\\"conclusion\\\": \\\"success\\\"}, \\\"eval_bce_v3_s42\\\": {\\\"status\\\": \\\"DONE\\\", \\\"metrics\\\": {\\\"dense_ppl\\\": 6.12, \\\"predictor_hard_mask_ppl\\\": 22.51, \\\"teal_sparse_ppl\\\": 27.97, \\\"model_level_sparsity\\\": 0.5, \\\"arc_challenge_acc\\\": 0.2048, \\\"arc_challenge_acc_norm\\\": 0.2398, \\\"arc_challenge_acc_norm_stderr\\\": 0.0125, \\\"winogrande_acc\\\": 0.5059, \\\"winogrande_acc_stderr\\\": 0.0141, \\\"mmlu_acc\\\": 0.3002, \\\"mmlu_acc_stderr\\\": 0.0038, \\\"gsm8k_exact_match\\\": 0.0485, \\\"gsm8k_exact_match_strict\\\": 0.0425, \\\"gsm8k_exact_match_stderr\\\": 0.0059}, \\\"conclusion\\\": \\\"success\\\"}, \\\"bench_dense\\\": {\\\"status\\\": \\\"DONE\\\", \\\"metrics\\\": {\\\"wikitext2_ppl\\\": 6.1173, \\\"arc_challenge_acc\\\": 0.5478, \\\"arc_challenge_acc_norm\\\": 0.5828, \\\"winogrande_acc\\\": 0.7806, \\\"mmlu_acc\\\": 0.6527, \\\"gsm8k_exact_match\\\": 0.4875}, \\\"conclusion\\\": \\\"success\\\"}, \\\"kl_sparsity30_s42_v3\\\": {\\\"status\\\": \\\"DONE\\\", \\\"metrics\\\": {\\\"loss\\\": 0.165, \\\"kl_normalized\\\": 0.165, \\\"kl_raw\\\": 0.165, \\\"sparsity\\\": 0.285, \\\"lambda_sparse\\\": 5000, \\\"tau\\\": 0.1, \\\"constraint_loss\\\": 0, \\\"steps\\\": 1000, \\\"true_dense_ppl\\\": 6.12, \\\"predictor_hard_mask_ppl\\\": 7.3, \\\"teal_sparse_ppl\\\": 8.98, \\\"teal_sparse_ppl_note\\\": \\\"已通过 eval_kl30_teal_30pct 独立验证 (sparsity_target=0.3, D034)\\\", \\\"model_level_sparsity\\\": 0.3, \\\"eval_dataset\\\": \\\"wikitext-2\\\", \\\"eval_seq_len\\\": 2048}, \\\"conclusion\\\": \\\"success\\\"}, \\\"eval_kl30_teal_30pct\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"dense_ppl\\\": 6.12, \\\"predictor_hard_mask_ppl\\\": 7.3, \\\"teal_sparse_ppl\\\": 8.98, \\\"sparsity_target\\\": 0.3, \\\"actual_sparsity\\\": 0.3}}, \\\"bce_isocompute_v3_s42\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"steps\\\": 2700, \\\"loss\\\": 0.6382, \\\"bce_loss\\\": 0.6371, \\\"reg_loss\\\": 0.001, \\\"sparsity\\\": 0.51, \\\"training_time_seconds\\\": 2828, \\\"note\\\": \\\"BCE saturation confirmed: step 500→2700 only 0.006 improvement\\\"}}, \\\"bench_mistral_kl50_s42\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"killed\\\"}, \\\"d030_kl50_uniform\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"wikitext2_ppl\\\": 11.96, \\\"arc_challenge_acc_norm\\\": 0.3276, \\\"winogrande_acc\\\": 0.629, \\\"mmlu_acc\\\": 0.2777, \\\"gsm8k_exact_match\\\": 0.0212, \\\"actual_sparsity\\\": 0.5, \\\"allocation\\\": \\\"uniform\\\", \\\"per_layer_sparsity\\\": \\\"uniform 0.500 across all 32 layers\\\", \\\"mmlu_change_vs_global\\\": \\\"+1.86pp (0.2591 → 0.2777, not significant)\\\", \\\"gsm8k_change_vs_global\\\": \\\"+0.91pp (0.0121 → 0.0212, not significant)\\\", \\\"conclusion_note\\\": \\\"50% uniform 未能修复 MMLU/GSM8K collapse. Uniform allocation 的修复效应在 50% sparsity 下消失。\\\"}}, \\\"lm_eval_teal_50pct\\\": {\\\"status\\\": \\\"DONE\\\", \\\"metrics\\\": {\\\"method\\\": \\\"vanilla_teal\\\", \\\"sparsity\\\": 0.5, \\\"actual_sparsity\\\": 0.5, \\\"arc_challenge_acc_norm\\\": 0.291, \\\"winogrande_acc\\\": 0.5556, \\\"mmlu_acc\\\": 0.2856, \\\"gsm8k_exact_match_flexible\\\": 0.019, \\\"gsm8k_exact_match_strict\\\": 0.0114, \\\"arc_challenge_drop_vs_dense\\\": -0.5, \\\"winogrande_drop_vs_dense\\\": -0.289, \\\"mmlu_drop_vs_dense\\\": -0.563, \\\"gsm8k_drop_vs_dense\\\": -0.962, \\\"model\\\": \\\"Llama-3.1-8B\\\", \\\"condition\\\": \\\"TEAL 50% training-free sparsity\\\"}, \\\"conclusion\\\": \\\"success\\\"}, \\\"d030_kl30_uniform\\\": {\\\"status\\\": \\\"DONE\\\", \\\"metrics\\\": {\\\"wikitext2_ppl\\\": 8.8157, \\\"arc_challenge_acc_norm\\\": 0.4078, \\\"winogrande_acc\\\": 0.6859, \\\"mmlu_acc\\\": 0.4061, \\\"gsm8k_exact_match\\\": 0.0735, \\\"actual_sparsity\\\": 0.3, \\\"allocation\\\": \\\"uniform\\\", \\\"per_layer_sparsity\\\": \\\"uniform 0.301 across all 32 layers\\\", \\\"mmlu_improvement_vs_global\\\": \\\"+11.87pp (0.2874 → 0.4061)\\\", \\\"gsm8k_change_vs_global\\\": \\\"no change (0.0743 → 0.0735, within noise)\\\"}, \\\"conclusion\\\": \\\"success\\\"}, \\\"mistral_kl_s42\\\": {\\\"status\\\": \\\"DONE\\\", \\\"metrics\\\": {\\\"train_final_loss\\\": 0.2188, \\\"train_final_kl_raw\\\": 0.2188, \\\"train_final_kl_norm\\\": 0.2188, \\\"train_final_constraint\\\": 0, \\\"train_final_sparsity\\\": 0.48, \\\"train_final_lambda\\\": 1000, \\\"train_final_tau\\\": 0.1, \\\"train_steps_completed\\\": 1000, \\\"true_dense_ppl\\\": 5.52, \\\"predictor_hard_mask_ppl\\\": 7.3, \\\"teal_sparse_ppl\\\": 8.98, \\\"model_level_sparsity\\\": 0.5, \\\"eval_dataset\\\": \\\"wikitext-2\\\", \\\"eval_seq_len\\\": 2048, \\\"calibration_samples\\\": 32, \\\"eval_samples\\\": 159}, \\\"conclusion\\\": \\\"success\\\"}, \\\"lm_eval_mistral_kl_50pct\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"negative\\\", \\\"metrics\\\": {\\\"arc_challenge_acc\\\": 0.2927, \\\"arc_challenge_acc_norm\\\": 0.3183, \\\"arc_challenge_acc_norm_stderr\\\": 0.0136, \\\"winogrande_acc\\\": 0.629, \\\"winogrande_acc_stderr\\\": 0.0136, \\\"mmlu_acc\\\": 0.2295, \\\"mmlu_acc_stderr\\\": 0.0035, \\\"mmlu_stem_acc\\\": 0.2125, \\\"mmlu_humanities_acc\\\": 0.2421, \\\"mmlu_social_sciences_acc\\\": 0.2171, \\\"mmlu_other_acc\\\": 0.2398, \\\"gsm8k_exact_match_strict\\\": 0.0045, \\\"gsm8k_exact_match_flexible\\\": 0.0212, \\\"model\\\": \\\"Mistral-7B-v0.3\\\", \\\"condition\\\": \\\"kl_distill_50pct_sparsity_s42\\\", \\\"arc_challenge_retention_vs_dense\\\": 0.528, \\\"winogrande_retention_vs_dense\\\": 0.799, \\\"mmlu_retention_vs_dense\\\": 0.368, \\\"gsm8k_retention_vs_dense\\\": 0.012}}, \\\"lm_eval_teal_30pct\\\": {\\\"status\\\": \\\"DONE\\\", \\\"metrics\\\": {\\\"arc_challenge\\\": {\\\"acc\\\": 0.3933, \\\"acc_norm\\\": 0.4155, \\\"acc_stderr\\\": 0.0143, \\\"acc_norm_stderr\\\": 0.0144}, \\\"winogrande\\\": {\\\"acc\\\": 0.6559, \\\"acc_stderr\\\": 0.0134}, \\\"mmlu\\\": {\\\"acc\\\": 0.3598, \\\"acc_stderr\\\": 0.004}, \\\"mmlu_stem\\\": {\\\"acc\\\": 0.313}, \\\"mmlu_humanities\\\": {\\\"acc\\\": 0.3305}, \\\"mmlu_social_sciences\\\": {\\\"acc\\\": 0.4108}, \\\"mmlu_other\\\": {\\\"acc\\\": 0.401}, \\\"gsm8k\\\": {\\\"exact_match_strict\\\": 0.0849, \\\"exact_match_flexible\\\": 0.0925, \\\"strict_stderr\\\": 0.0077, \\\"flexible_stderr\\\": 0.008}, \\\"actual_sparsity\\\": 0.3}, \\\"conclusion\\\": \\\"negative\\\"}, \\\"lm_eval_kl_30pct_s42\\\": {\\\"status\\\": \\\"DONE\\\", \\\"metrics\\\": {\\\"arc_challenge_acc\\\": 0.3575, \\\"arc_challenge_acc_norm\\\": 0.3737, \\\"winogrande_acc\\\": 0.6756, \\\"mmlu_acc\\\": 0.2874, \\\"gsm8k_exact_match_strict\\\": 0.0743, \\\"gsm8k_exact_match_flexible\\\": 0.0781, \\\"actual_sparsity\\\": 0.3, \\\"model\\\": \\\"llama-3.1-8b\\\", \\\"condition\\\": \\\"kl_distill_30pct_sparsity_s42\\\", \\\"mmlu_stem_acc\\\": 0.2499, \\\"mmlu_social_sciences_acc\\\": 0.2896, \\\"mmlu_humanities_acc\\\": 0.2786, \\\"mmlu_other_acc\\\": 0.3363}, \\\"conclusion\\\": \\\"negative\\\"}, \\\"bce_isocompute_s42_v2\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"killed\\\"}, \\\"eval_spon_supp_retry\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"failed\\\"}, \\\"lm_eval_dense_test\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"failed\\\"}, \\\"lm_eval_mistral_downstream\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"failed\\\"}, \\\"mvp_kl_s123\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"killed\\\"}, \\\"mvp_kl_s456\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"killed\\\"}, \\\"lm_eval_mistral_dense\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"arc_challenge_acc_norm\\\": 0.6024, \\\"winogrande_acc\\\": 0.7869, \\\"mmlu_acc\\\": 0.6244, \\\"gsm8k_exact_match\\\": 0.3654, \\\"model\\\": \\\"Mistral-7B-v0.3\\\", \\\"condition\\\": \\\"dense\\\", \\\"server\\\": \\\"westd-34887\\\"}}, \\\"lm_eval_kl_s42\\\": {\\\"status\\\": \\\"DONE\\\", \\\"metrics\\\": {\\\"arc_challenge_acc_norm\\\": 0.3771, \\\"winogrande_acc\\\": 0.6156, \\\"mmlu_acc\\\": 0.2591, \\\"gsm8k_exact_match\\\": 0.0121, \\\"eval_tasks\\\": [\\\"arc_challenge\\\", \\\"winogrande\\\", \\\"mmlu\\\", \\\"gsm8k\\\"], \\\"model\\\": \\\"llama-3.1-8b\\\", \\\"condition\\\": \\\"kl_sparse_50pct\\\", \\\"server\\\": \\\"westd-34887\\\", \\\"exit_code\\\": 129, \\\"wall_time_sec\\\": 3010, \\\"flag\\\": \\\"SUSPECT — gsm8k 0.50→0.01 catastrophic drop; PID 179918 rerunning with lm_eval_sparse.py\\\"}, \\\"conclusion\\\": \\\"negative\\\"}, \\\"gsm8k_gen_compare\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"negative\\\"}, \\\"kl_sparsity70_s42_v2\\\": {\\\"status\\\": \\\"DONE\\\", \\\"metrics\\\": {\\\"true_dense_ppl\\\": 6.12, \\\"predictor_hard_mask_ppl\\\": 13.84, \\\"predictor_teal_sparse_ppl\\\": 17.91, \\\"vanilla_teal_sparse_ppl\\\": 100.11, \\\"teal_sparse_ppl\\\": 17.91, \\\"teal_sparse_ppl_static_baseline\\\": 17.91, \\\"model_level_sparsity\\\": 0.7, \\\"teal_sparse_note\\\": \\\"17.91 = predictor-based TEAL (teal_global_masks: predictor-gated magnitude scoring + global topk @70%). vanilla TEAL @70% = 100.11. 代码来源: quick_sp70.py L10 imports teal_global_masks, L60 调用. plan_007_all_ppl_fixed.json 的 mode=static_mask_70pct metadata 有误导性.\\\", \\\"eval_dataset\\\": \\\"wikitext-2\\\", \\\"eval_seq_len\\\": 2048, \\\"calibration_samples\\\": 32, \\\"per_layer_sparsity_range\\\": [0.508, 0.876]}, \\\"conclusion\\\": \\\"success\\\"}, \\\"training_free_baselines\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"dense_ppl\\\": 6.12, \\\"vanilla_teal_global_ppl_30pct\\\": 10.97, \\\"vanilla_teal_global_ppl_50pct\\\": 23.31, \\\"vanilla_teal_global_ppl_70pct\\\": 100.11, \\\"wina_global_ppl_30pct\\\": 11.45, \\\"wina_global_ppl_50pct\\\": 27.93, \\\"wina_global_ppl_70pct\\\": 137.24, \\\"uniform_50pct_ppl\\\": 23.9, \\\"teal_greedy_ppl\\\": 33.47, \\\"vanilla_teal_global_ppl\\\": 23.31, \\\"wina_global_ppl\\\": 27.93, \\\"rsparse_global_ppl\\\": 151.2}}, \\\"lm_eval_dense\\\": {\\\"status\\\": \\\"DONE\\\", \\\"metrics\\\": {\\\"arc_challenge_acc_norm\\\": 0.5819, \\\"winogrande_acc\\\": 0.7814, \\\"mmlu_acc\\\": 0.6532, \\\"gsm8k_exact_match\\\": 0.5004, \\\"eval_tasks\\\": [\\\"arc_challenge\\\", \\\"winogrande\\\", \\\"mmlu\\\", \\\"gsm8k\\\"], \\\"model\\\": \\\"llama-3.1-8b\\\", \\\"condition\\\": \\\"dense\\\", \\\"server\\\": \\\"westd-34887\\\"}, \\\"conclusion\\\": \\\"success\\\"}, \\\"kl_sparsity30_s42_v2\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"negative\\\", \\\"metrics\\\": {\\\"final_loss\\\": 0.1465, \\\"kl_normalized\\\": 0.1465, \\\"kl_raw\\\": 0.1465, \\\"model_level_sparsity\\\": 0.281, \\\"sparsity_target\\\": 0.3, \\\"lambda_sparse_final\\\": 1000, \\\"lambda_max_cap\\\": 1000, \\\"tau_final\\\": 0.1, \\\"constraint_loss_final\\\": 0, \\\"training_steps\\\": 1000, \\\"wall_clock_seconds\\\": 2662.6, \\\"gpu_hours\\\": 0.74, \\\"note\\\": \\\"No PPL evaluation in training script. Sparsity stuck at 0.281 (same as v1). Lambda hit cap=1000 by step 220 and could not push sparsity further. W&B run was offline (not synced).\\\"}}, \\\"bce_isocompute_v2_s42\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"final_loss\\\": 0.6637, \\\"final_bce_loss\\\": 0.6586, \\\"final_reg_loss\\\": 0.0051, \\\"final_sparsity\\\": 0.502, \\\"training_steps\\\": 1000, \\\"training_time_sec\\\": 1047.8, \\\"reg_weight\\\": 2, \\\"true_dense_ppl\\\": 6.12, \\\"predictor_hard_mask_ppl\\\": 26.76, \\\"teal_sparse_ppl\\\": 54.84, \\\"eval_seq_len\\\": 2048, \\\"eval_dataset\\\": \\\"wikitext-2\\\"}}, \\\"kl_sparsity70_s42\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"killed\\\"}, \\\"kl_sparsity30_s42\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"killed\\\"}, \\\"plan_005_subsumption_s42\\\": {\\\"status\\\": \\\"DONE\\\", \\\"metrics\\\": {\\\"linearity_ratio\\\": 0.2644, \\\"linearity_ratio_std\\\": 0.0073, \\\"magnitude_ratio\\\": 0.1578, \\\"magnitude_ratio_std\\\": 0.0088, \\\"cosine_similarity\\\": 0.1962, \\\"cosine_similarity_std\\\": 0.0268, \\\"predictor_effect_norm\\\": 482.65, \\\"spon_correction_norm\\\": 76.2, \\\"interaction_norm\\\": 147.74, \\\"num_samples\\\": 50, \\\"seq_len\\\": 2048, \\\"conclusion_type\\\": \\\"weak_subsumption\\\"}, \\\"conclusion\\\": \\\"success\\\"}, \\\"ste_baseline_s42\\\": {\\\"status\\\": \\\"DONE\\\", \\\"metrics\\\": {\\\"true_dense_ppl\\\": 6.12, \\\"predictor_hard_mask_ppl\\\": 8.18, \\\"teal_sparse_ppl\\\": 15.77, \\\"model_level_sparsity\\\": 0.47, \\\"ppl_increase_vs_true_dense_pct\\\": 157.7, \\\"eval_seq_len\\\": 2048, \\\"calibration_samples\\\": 32, \\\"eval_dataset\\\": \\\"wikitext-2\\\", \\\"per_token_sparsity\\\": 0.47, \\\"lambda_stats\\\": {\\\"steps_70_130_mean\\\": 66.4, \\\"steps_70_130_std\\\": 94.87, \\\"first_500_mean\\\": 688.07, \\\"first_500_std\\\": 440.57, \\\"last_500_mean\\\": 965.69, \\\"last_500_std\\\": 141.59, \\\"overall_mean\\\": 826.88, \\\"overall_std\\\": 354.23}}, \\\"conclusion\\\": \\\"success\\\"}, \\\"spon_supp_eval_retry\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"failed\\\"}, \\\"spon_2048_s42\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"negative\\\", \\\"metrics\\\": {\\\"true_dense_ppl\\\": 6.1173, \\\"predictor_hard_mask_ppl\\\": 9.2165, \\\"spon_sparse_ppl\\\": 8.991, \\\"spon_recovery_pct\\\": 7.3, \\\"ppl_improvement_from_spon\\\": 0.2255, \\\"mean_bias_norm\\\": 0.05312, \\\"max_bias_norm\\\": 0.065918, \\\"model_level_sparsity\\\": 0.498, \\\"eval_seq_len\\\": 2048, \\\"training_seq_len\\\": 2048, \\\"eval_samples\\\": 141, \\\"trainable_params\\\": 458752, \\\"trainable_pct\\\": 0.0057, \\\"training_steps\\\": 1000, \\\"final_loss\\\": 0.377, \\\"dense_with_spon_ppl\\\": 6.1823, \\\"dense_ppl_degradation\\\": 0.0651, \\\"teal_sparse_no_spon_ppl\\\": 12.0776, \\\"teal_sparse_with_spon_ppl\\\": 11.7907, \\\"spon_recovery_teal_pct\\\": 4.8, \\\"teal_sparsity\\\": 0.4979}}, \\\"bce_isocompute_s42\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"failed\\\"}, \\\"mvp_kl_norm_v2_s456\\\": {\\\"status\\\": \\\"DONE\\\", \\\"metrics\\\": {\\\"true_dense_ppl\\\": 6.1173, \\\"predictor_hard_mask_ppl\\\": 9.14, \\\"teal_sparse_ppl\\\": 13.58, \\\"model_level_sparsity\\\": 0.498, \\\"ppl_increase_vs_true_dense_pct\\\": 121.9, \\\"eval_md5\\\": \\\"f4086818bb55dc354ea4c6fe8ed8899a\\\", \\\"calibration_samples\\\": 32, \\\"vanilla_teal_sparse_ppl_INVALID\\\": 66036.4062}, \\\"conclusion\\\": \\\"success\\\"}, \\\"spon_training\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"negative\\\", \\\"metrics\\\": {\\\"true_dense_ppl\\\": 6.1193, \\\"predictor_hard_mask_ppl\\\": 9.2165, \\\"spon_sparse_ppl\\\": 9.0977, \\\"spon_recovery_pct\\\": 3.8, \\\"ppl_improvement_from_spon\\\": 0.1188, \\\"ppl_increase_vs_true_dense_pct\\\": 48.7, \\\"ppl_increase_no_spon_vs_true_dense_pct\\\": 50.6, \\\"mean_bias_norm\\\": 0.040596, \\\"max_bias_norm\\\": 0.054199, \\\"teal_sparse_ppl\\\": 12.08, \\\"teal_with_spon_ppl\\\": 11.93, \\\"spon_dense_ppl_degradation\\\": 6.19, \\\"model_level_sparsity\\\": 0.5, \\\"eval_seq_len\\\": 2048, \\\"eval_samples\\\": 141, \\\"trainable_params\\\": 458752, \\\"trainable_pct\\\": 0.0057}}, \\\"training_free_wina_greedy\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"negative\\\", \\\"metrics\\\": {\\\"wina_greedy_ppl\\\": 2126.03, \\\"dense_ppl\\\": 6.12, \\\"model_level_sparsity\\\": 0.5, \\\"eval_dataset\\\": \\\"WikiText-2\\\", \\\"eval_seq_len\\\": 2048, \\\"greedy_allocation_summary\\\": \\\"layers 0-11: 0.90, layer 12: 0.85, layer 13: 0.80, layer 14: 0.70, layers 15-16: 0.50-0.55, layers 17-20: 0.30-0.35, layers 21-24: 0.05-0.15, layers 25-31: 0.00\\\"}}, \\\"ste_kl_s42\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"killed\\\"}, \\\"bce_comp_staged_s42\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"negative\\\", \\\"metrics\\\": {\\\"true_dense_ppl\\\": 6.12, \\\"predictor_hard_mask_ppl\\\": 25.44, \\\"predictor_hard_mask_ppl_no_comp\\\": 27.96, \\\"teal_sparse_ppl\\\": 44.54, \\\"model_level_sparsity\\\": 0.558, \\\"ppl_increase_vs_true_dense_pct\\\": 315.7, \\\"comp_loss_final\\\": 0.0033, \\\"bce_loss_final\\\": 0.6379, \\\"eval_seq_len\\\": 2048, \\\"calibration_samples\\\": 32}}, \\\"spon_training_seq2048\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"killed\\\"}, \\\"kl_only_s0\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"true_dense_ppl\\\": 6.12, \\\"predictor_hard_mask_ppl\\\": 9.19, \\\"teal_sparse_ppl\\\": 12.03, \\\"model_level_sparsity\\\": 0.499, \\\"ppl_increase_vs_true_dense_pct\\\": 96.57, \\\"eval_seq_len\\\": 2048, \\\"calibration_samples\\\": 32}}, \\\"kl_only_s1\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"true_dense_ppl\\\": 6.12, \\\"predictor_hard_mask_ppl\\\": 9.15, \\\"teal_sparse_ppl\\\": 11.99, \\\"model_level_sparsity\\\": 0.498, \\\"ppl_increase_vs_true_dense_pct\\\": 96}}, \\\"mvp_bce_s456\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"true_dense_ppl\\\": 6.1173, \\\"predictor_hard_mask_ppl\\\": 28.1437, \\\"teal_sparse_ppl\\\": 43.033, \\\"model_level_sparsity\\\": 0.4957, \\\"ppl_increase_vs_true_dense_pct\\\": 603.3, \\\"eval_md5\\\": \\\"f4086818bb55dc354ea4c6fe8ed8899a\\\", \\\"calibration_samples\\\": 32, \\\"vanilla_teal_sparse_ppl_INVALID\\\": 66036.4062}}, \\\"mvp_bce_s123\\\": {\\\"status\\\": \\\"DONE\\\", \\\"metrics\\\": {\\\"true_dense_ppl\\\": 6.1173, \\\"predictor_hard_mask_ppl\\\": 28.3817, \\\"teal_sparse_ppl\\\": 44.5864, \\\"model_level_sparsity\\\": 0.4957, \\\"ppl_increase_vs_true_dense_pct\\\": 629, \\\"eval_md5\\\": \\\"f4086818bb55dc354ea4c6fe8ed8899a\\\", \\\"calibration_samples\\\": 32, \\\"vanilla_teal_sparse_ppl_INVALID\\\": 66036.4062}, \\\"conclusion\\\": \\\"success\\\"}, \\\"mvp_bce_s42\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"true_dense_ppl\\\": 6.1173, \\\"predictor_hard_mask_ppl\\\": 27.9603, \\\"teal_sparse_ppl\\\": 44.537, \\\"model_level_sparsity\\\": 0.4957, \\\"ppl_increase_vs_true_dense_pct\\\": 628, \\\"eval_md5\\\": \\\"f4086818bb55dc354ea4c6fe8ed8899a\\\", \\\"calibration_samples\\\": 32, \\\"vanilla_teal_sparse_ppl_INVALID\\\": 66036.4062}}, \\\"mvp_kl_norm_v2_s123\\\": {\\\"status\\\": \\\"DONE\\\", \\\"metrics\\\": {\\\"true_dense_ppl\\\": 6.1173, \\\"predictor_hard_mask_ppl\\\": 9.2474, \\\"teal_sparse_ppl\\\": 11.9128, \\\"model_level_sparsity\\\": 0.4979, \\\"ppl_increase_vs_true_dense_pct\\\": 94.7, \\\"eval_md5\\\": \\\"f4086818bb55dc354ea4c6fe8ed8899a\\\", \\\"calibration_samples\\\": 32, \\\"vanilla_teal_sparse_ppl_INVALID\\\": 66036.4062}, \\\"conclusion\\\": \\\"success\\\"}, \\\"mvp_kl_norm_v2_s42\\\": {\\\"status\\\": \\\"DONE\\\", \\\"metrics\\\": {\\\"true_dense_ppl\\\": 6.1173, \\\"predictor_hard_mask_ppl\\\": 9.2142, \\\"teal_sparse_ppl\\\": 12.0776, \\\"model_level_sparsity\\\": 0.4979, \\\"ppl_increase_vs_true_dense_pct\\\": 97.4, \\\"eval_md5\\\": \\\"f4086818bb55dc354ea4c6fe8ed8899a\\\", \\\"calibration_samples\\\": 32, \\\"vanilla_teal_sparse_ppl_INVALID\\\": 66036.4062}, \\\"conclusion\\\": \\\"success\\\"}, \\\"mvp_kl_norm_s123\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"failed\\\"}, \\\"mvp_kl_norm_s42\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"failed\\\"}, \\\"kl_normalized_quicktest\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"failed\\\", \\\"metrics\\\": {\\\"step1_kl\\\": 1.18, \\\"step200_kl\\\": 0.641, \\\"step200_sparsity\\\": 0.504, \\\"final_lambda\\\": 8, \\\"sparsity_converged_step\\\": 80, \\\"sparsity_trajectory\\\": [0.406, 0.398, 0.398, 0.457, 0.52, 0.506, 0.504, 0.504], \\\"lambda_trajectory\\\": [1, 2, 4, 8, 8, 8, 8, 8]}}, \\\"kl_lagrangian_quicktest\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"negative\\\", \\\"metrics\\\": {\\\"final_kl_loss\\\": 418, \\\"final_constraint_loss\\\": 1.211, \\\"final_sparsity\\\": 0.141, \\\"final_lambda\\\": 5.06, \\\"steps\\\": 200, \\\"sparsity_trajectory\\\": [0.406, 0.387, 0.289, 0.168, 0.141]}}, \\\"mvp_kl_s42\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"negative\\\", \\\"metrics\\\": {\\\"final_total_loss\\\": 3.3438, \\\"final_kl_loss\\\": 3.2969, \\\"final_reg_loss\\\": 0.05, \\\"final_sparsity\\\": 0, \\\"steps\\\": 1000, \\\"tau_final\\\": 0.1, \\\"wikitext2_ppl_dense\\\": 6.12, \\\"wikitext2_ppl_sparse\\\": 455.93, \\\"wikitext2_ppl_increase_pct\\\": 7349, \\\"model_level_sparsity\\\": 0.372, \\\"checkpoint_path\\\": \\\"/root/distill_sparse_swiglu/checkpoints/mvp_kl_s42/predictor_kl.pt\\\"}}}, \\\"count\\\": 67, \\\"total\\\": 67, \\\"baseline\\\": \\\"bench_dense\\\"}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.2689}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"experiments\": {\"longbench_dense_v6\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"longbench_narrativeqa\": 7.3, \"longbench_qasper\": 13.4, \"longbench_gov_report\": 30.5, \"longbench_multi_news\": 2.5}}, \"bench_kl50_uniform_s456\": {\"status\": \"DONE\", \"metrics\": {\"wikitext2_ppl\": 11.9604, \"arc_challenge_acc_norm\": 0.3345, \"winogrande_acc\": 0.6275, \"mmlu_acc\": 0.2874, \"gsm8k_exact_match\": 0.0212, \"actual_sparsity\": 0.5}, \"conclusion\": \"success\"}, \"bench_kl50_uniform_s123\": {\"status\": \"DONE\", \"metrics\": {\"wikitext2_ppl\": 11.83, \"arc_challenge_acc_norm\": 0.3515, \"winogrande_acc\": 0.6298, \"mmlu_acc\": 0.2751, \"gsm8k_exact_match\": 0.0235, \"actual_sparsity\": 0.5}, \"conclusion\": \"success\"}, \"latency_benchmark\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"gpu_model\": \"NVIDIA RTX PRO 6000 Blackwell Server Edition\", \"dtype\": \"float16\", \"attn\": \"flash_attention_2\", \"batch\": 1, \"seq_len\": 2048, \"warmup\": 10, \"iters\": 100, \"dense_ms\": 119.11, \"dense_std\": 0.57, \"dense_tokens_per_s\": 17194.5, \"kl_30pct_ms\": 126.64, \"kl_30pct_std\": 0.7, \"kl_30pct_tokens_per_s\": 16171.8, \"kl_30pct_speedup\": 0.941, \"kl_50pct_ms\": 126.78, \"kl_50pct_std\": 0.31, \"kl_50pct_tokens_per_s\": 16154.2, \"kl_50pct_speedup\": 0.939, \"comp_30pct_ms\": 129.94, \"comp_30pct_std\": 0.75, \"comp_30pct_tokens_per_s\": 15761.4, \"comp_30pct_speedup\": 0.917, \"comp_50pct_ms\": 129.71, \"comp_50pct_std\": 0.53, \"comp_50pct_tokens_per_s\": 15788.8, \"comp_50pct_speedup\": 0.918, \"predictor_overhead_ms\": 3.17, \"predictor_overhead_pct\": 2.7, \"per_layer_predictor_ms\": 0.099, \"dense_ffn_per_layer_ms\": 2.427, \"sparse_ffn_pred_per_layer_ms\": 2.686, \"compensation_overhead_ms\": 3.3}}, \"longbench_dense_v4\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"longbench_dense\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"longbench_kl30_uniform\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"bench_kl40_global\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"wikitext2_ppl\": 10.117, \"arc_challenge_acc_norm\": 0.4096, \"winogrande_acc\": 0.6535, \"mmlu_acc\": 0.3806, \"gsm8k_exact_match\": 0.05, \"actual_sparsity\": 0.4}}, \"bench_kl50_uniform\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"wikitext2_ppl\": 11.963, \"arc_challenge_acc_norm\": 0.3276, \"winogrande_acc\": 0.629, \"mmlu_acc\": 0.2777, \"gsm8k_exact_match\": 0.0212, \"actual_sparsity\": 0.5}}, \"bench_teal50\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"wikitext2_ppl\": 23.31, \"arc_challenge_acc_norm\": 0.2841, \"winogrande_acc\": 0.5304, \"mmlu_acc\": 0.2832, \"gsm8k_exact_match\": 0.0197, \"actual_sparsity\": 0.5}}, \"bench_teal30\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"wikitext2_ppl\": 10.97, \"arc_challenge_acc_norm\": 0.4232, \"winogrande_acc\": 0.6606, \"mmlu_acc\": 0.3861, \"gsm8k_exact_match\": 0.0788, \"actual_sparsity\": 0.3}}, \"bench_kl50_global\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"wikitext2_ppl\": 11.7933, \"arc_challenge_acc_norm\": 0.3285, \"winogrande_acc\": 0.6346, \"mmlu_acc\": 0.2789, \"gsm8k_exact_match\": 0.0129, \"actual_sparsity\": 0.5}}, \"bench_kl30_global\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"wikitext2_ppl\": 8.9768, \"arc_challenge_acc_norm\": 0.3968, \"winogrande_acc\": 0.7017, \"mmlu_acc\": 0.2527, \"gsm8k_exact_match\": 0.0879, \"actual_sparsity\": 0.3}}, \"bench_kl30_uniform\": {\"status\": \"DONE\", \"metrics\": {\"wikitext2_ppl\": 8.8157, \"arc_challenge_acc_norm\": 0.4078, \"winogrande_acc\": 0.6859, \"mmlu_acc\": 0.4061, \"gsm8k_exact_match\": 0.0735, \"actual_sparsity\": 0.3}, \"conclusion\": \"success\"}, \"d030_kl40_uniform\": {\"status\": \"DONE\", \"metrics\": {\"wikitext2_ppl\": 8.3627, \"arc_challenge_acc_norm\": 0.4181, \"winogrande_acc\": 0.6717, \"mmlu_acc\": 0.3068, \"gsm8k_exact_match\": 0.0394, \"actual_sparsity\": 0.398}, \"conclusion\": \"success\"}, \"eval_bce_v3_s42\": {\"status\": \"DONE\", \"metrics\": {\"dense_ppl\": 6.12, \"predictor_hard_mask_ppl\": 22.51, \"teal_sparse_ppl\": 27.97, \"model_level_sparsity\": 0.5, \"arc_challenge_acc\": 0.2048, \"arc_challenge_acc_norm\": 0.2398, \"arc_challenge_acc_norm_stderr\": 0.0125, \"winogrande_acc\": 0.5059, \"winogrande_acc_stderr\": 0.0141, \"mmlu_acc\": 0.3002, \"mmlu_acc_stderr\": 0.0038, \"gsm8k_exact_match\": 0.0485, \"gsm8k_exact_match_strict\": 0.0425, \"gsm8k_exact_match_stderr\": 0.0059}, \"conclusion\": \"success\"}, \"bench_dense\": {\"status\": \"DONE\", \"metrics\": {\"wikitext2_ppl\": 6.1173, \"arc_challenge_acc\": 0.5478, \"arc_challenge_acc_norm\": 0.5828, \"winogrande_acc\": 0.7806, \"mmlu_acc\": 0.6527, \"gsm8k_exact_match\": 0.4875}, \"conclusion\": \"success\"}, \"kl_sparsity30_s42_v3\": {\"status\": \"DONE\", \"metrics\": {\"loss\": 0.165, \"kl_normalized\": 0.165, \"kl_raw\": 0.165, \"sparsity\": 0.285, \"lambda_sparse\": 5000, \"tau\": 0.1, \"constraint_loss\": 0, \"steps\": 1000, \"true_dense_ppl\": 6.12, \"predictor_hard_mask_ppl\": 7.3, \"teal_sparse_ppl\": 8.98, \"teal_sparse_ppl_note\": \"已通过 eval_kl30_teal_30pct 独立验证 (sparsity_target=0.3, D034)\", \"model_level_sparsity\": 0.3, \"eval_dataset\": \"wikitext-2\", \"eval_seq_len\": 2048}, \"conclusion\": \"success\"}, \"eval_kl30_teal_30pct\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"dense_ppl\": 6.12, \"predictor_hard_mask_ppl\": 7.3, \"teal_sparse_ppl\": 8.98, \"sparsity_target\": 0.3, \"actual_sparsity\": 0.3}}, \"bce_isocompute_v3_s42\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"steps\": 2700, \"loss\": 0.6382, \"bce_loss\": 0.6371, \"reg_loss\": 0.001, \"sparsity\": 0.51, \"training_time_seconds\": 2828, \"note\": \"BCE saturation confirmed: step 500→2700 only 0.006 improvement\"}}, \"bench_mistral_kl50_s42\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"d030_kl50_uniform\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"wikitext2_ppl\": 11.96, \"arc_challenge_acc_norm\": 0.3276, \"winogrande_acc\": 0.629, \"mmlu_acc\": 0.2777, \"gsm8k_exact_match\": 0.0212, \"actual_sparsity\": 0.5, \"allocation\": \"uniform\", \"per_layer_sparsity\": \"uniform 0.500 across all 32 layers\", \"mmlu_change_vs_global\": \"+1.86pp (0.2591 → 0.2777, not significant)\", \"gsm8k_change_vs_global\": \"+0.91pp (0.0121 → 0.0212, not significant)\", \"conclusion_note\": \"50% uniform 未能修复 MMLU/GSM8K collapse. Uniform allocation 的修复效应在 50% sparsity 下消失。\"}}, \"lm_eval_teal_50pct\": {\"status\": \"DONE\", \"metrics\": {\"method\": \"vanilla_teal\", \"sparsity\": 0.5, \"actual_sparsity\": 0.5, \"arc_challenge_acc_norm\": 0.291, \"winogrande_acc\": 0.5556, \"mmlu_acc\": 0.2856, \"gsm8k_exact_match_flexible\": 0.019, \"gsm8k_exact_match_strict\": 0.0114, \"arc_challenge_drop_vs_dense\": -0.5, \"winogrande_drop_vs_dense\": -0.289, \"mmlu_drop_vs_dense\": -0.563, \"gsm8k_drop_vs_dense\": -0.962, \"model\": \"Llama-3.1-8B\", \"condition\": \"TEAL 50% training-free sparsity\"}, \"conclusion\": \"success\"}, \"d030_kl30_uniform\": {\"status\": \"DONE\", \"metrics\": {\"wikitext2_ppl\": 8.8157, \"arc_challenge_acc_norm\": 0.4078, \"winogrande_acc\": 0.6859, \"mmlu_acc\": 0.4061, \"gsm8k_exact_match\": 0.0735, \"actual_sparsity\": 0.3, \"allocation\": \"uniform\", \"per_layer_sparsity\": \"uniform 0.301 across all 32 layers\", \"mmlu_improvement_vs_global\": \"+11.87pp (0.2874 → 0.4061)\", \"gsm8k_change_vs_global\": \"no change (0.0743 → 0.0735, within noise)\"}, \"conclusion\": \"success\"}, \"mistral_kl_s42\": {\"status\": \"DONE\", \"metrics\": {\"train_final_loss\": 0.2188, \"train_final_kl_raw\": 0.2188, \"train_final_kl_norm\": 0.2188, \"train_final_constraint\": 0, \"train_final_sparsity\": 0.48, \"train_final_lambda\": 1000, \"train_final_tau\": 0.1, \"train_steps_completed\": 1000, \"true_dense_ppl\": 5.52, \"predictor_hard_mask_ppl\": 7.3, \"teal_sparse_ppl\": 8.98, \"model_level_sparsity\": 0.5, \"eval_dataset\": \"wikitext-2\", \"eval_seq_len\": 2048, \"calibration_samples\": 32, \"eval_samples\": 159}, \"conclusion\": \"success\"}, \"lm_eval_mistral_kl_50pct\": {\"status\": \"DONE\", \"conclusion\": \"negative\", \"metrics\": {\"arc_challenge_acc\": 0.2927, \"arc_challenge_acc_norm\": 0.3183, \"arc_challenge_acc_norm_stderr\": 0.0136, \"winogrande_acc\": 0.629, \"winogrande_acc_stderr\": 0.0136, \"mmlu_acc\": 0.2295, \"mmlu_acc_stderr\": 0.0035, \"mmlu_stem_acc\": 0.2125, \"mmlu_humanities_acc\": 0.2421, \"mmlu_social_sciences_acc\": 0.2171, \"mmlu_other_acc\": 0.2398, \"gsm8k_exact_match_strict\": 0.0045, \"gsm8k_exact_match_flexible\": 0.0212, \"model\": \"Mistral-7B-v0.3\", \"condition\": \"kl_distill_50pct_sparsity_s42\", \"arc_challenge_retention_vs_dense\": 0.528, \"winogrande_retention_vs_dense\": 0.799, \"mmlu_retention_vs_dense\": 0.368, \"gsm8k_retention_vs_dense\": 0.012}}, \"lm_eval_teal_30pct\": {\"status\": \"DONE\", \"metrics\": {\"arc_challenge\": {\"acc\": 0.3933, \"acc_norm\": 0.4155, \"acc_stderr\": 0.0143, \"acc_norm_stderr\": 0.0144}, \"winogrande\": {\"acc\": 0.6559, \"acc_stderr\": 0.0134}, \"mmlu\": {\"acc\": 0.3598, \"acc_stderr\": 0.004}, \"mmlu_stem\": {\"acc\": 0.313}, \"mmlu_humanities\": {\"acc\": 0.3305}, \"mmlu_social_sciences\": {\"acc\": 0.4108}, \"mmlu_other\": {\"acc\": 0.401}, \"gsm8k\": {\"exact_match_strict\": 0.0849, \"exact_match_flexible\": 0.0925, \"strict_stderr\": 0.0077, \"flexible_stderr\": 0.008}, \"actual_sparsity\": 0.3}, \"conclusion\": \"negative\"}, \"lm_eval_kl_30pct_s42\": {\"status\": \"DONE\", \"metrics\": {\"arc_challenge_acc\": 0.3575, \"arc_challenge_acc_norm\": 0.3737, \"winogrande_acc\": 0.6756, \"mmlu_acc\": 0.2874, \"gsm8k_exact_match_strict\": 0.0743, \"gsm8k_exact_match_flexible\": 0.0781, \"actual_sparsity\": 0.3, \"model\": \"llama-3.1-8b\", \"condition\": \"kl_distill_30pct_sparsity_s42\", \"mmlu_stem_acc\": 0.2499, \"mmlu_social_sciences_acc\": 0.2896, \"mmlu_humanities_acc\": 0.2786, \"mmlu_other_acc\": 0.3363}, \"conclusion\": \"negative\"}, \"bce_isocompute_s42_v2\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval_spon_supp_retry\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"lm_eval_dense_test\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"lm_eval_mistral_downstream\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"mvp_kl_s123\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"mvp_kl_s456\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"lm_eval_mistral_dense\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"arc_challenge_acc_norm\": 0.6024, \"winogrande_acc\": 0.7869, \"mmlu_acc\": 0.6244, \"gsm8k_exact_match\": 0.3654, \"model\": \"Mistral-7B-v0.3\", \"condition\": \"dense\", \"server\": \"westd-34887\"}}, \"lm_eval_kl_s42\": {\"status\": \"DONE\", \"metrics\": {\"arc_challenge_acc_norm\": 0.3771, \"winogrande_acc\": 0.6156, \"mmlu_acc\": 0.2591, \"gsm8k_exact_match\": 0.0121, \"eval_tasks\": [\"arc_challenge\", \"winogrande\", \"mmlu\", \"gsm8k\"], \"model\": \"llama-3.1-8b\", \"condition\": \"kl_sparse_50pct\", \"server\": \"westd-34887\", \"exit_code\": 129, \"wall_time_sec\": 3010, \"flag\": \"SUSPECT — gsm8k 0.50→0.01 catastrophic drop; PID 179918 rerunning with lm_eval_sparse.py\"}, \"conclusion\": \"negative\"}, \"gsm8k_gen_compare\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"kl_sparsity70_s42_v2\": {\"status\": \"DONE\", \"metrics\": {\"true_dense_ppl\": 6.12, \"predictor_hard_mask_ppl\": 13.84, \"predictor_teal_sparse_ppl\": 17.91, \"vanilla_teal_sparse_ppl\": 100.11, \"teal_sparse_ppl\": 17.91, \"teal_sparse_ppl_static_baseline\": 17.91, \"model_level_sparsity\": 0.7, \"teal_sparse_note\": \"17.91 = predictor-based TEAL (teal_global_masks: predictor-gated magnitude scoring + global topk @70%). vanilla TEAL @70% = 100.11. 代码来源: quick_sp70.py L10 imports teal_global_masks, L60 调用. plan_007_all_ppl_fixed.json 的 mode=static_mask_70pct metadata 有误导性.\", \"eval_dataset\": \"wikitext-2\", \"eval_seq_len\": 2048, \"calibration_samples\": 32, \"per_layer_sparsity_range\": [0.508, 0.876]}, \"conclusion\": \"success\"}, \"training_free_baselines\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"dense_ppl\": 6.12, \"vanilla_teal_global_ppl_30pct\": 10.97, \"vanilla_teal_global_ppl_50pct\": 23.31, \"vanilla_teal_global_ppl_70pct\": 100.11, \"wina_global_ppl_30pct\": 11.45, \"wina_global_ppl_50pct\": 27.93, \"wina_global_ppl_70pct\": 137.24, \"uniform_50pct_ppl\": 23.9, \"teal_greedy_ppl\": 33.47, \"vanilla_teal_global_ppl\": 23.31, \"wina_global_ppl\": 27.93, \"rsparse_global_ppl\": 151.2}}, \"lm_eval_dense\": {\"status\": \"DONE\", \"metrics\": {\"arc_challenge_acc_norm\": 0.5819, \"winogrande_acc\": 0.7814, \"mmlu_acc\": 0.6532, \"gsm8k_exact_match\": 0.5004, \"eval_tasks\": [\"arc_challenge\", \"winogrande\", \"mmlu\", \"gsm8k\"], \"model\": \"llama-3.1-8b\", \"condition\": \"dense\", \"server\": \"westd-34887\"}, \"conclusion\": \"success\"}, \"kl_sparsity30_s42_v2\": {\"status\": \"DONE\", \"conclusion\": \"negative\", \"metrics\": {\"final_loss\": 0.1465, \"kl_normalized\": 0.1465, \"kl_raw\": 0.1465, \"model_level_sparsity\": 0.281, \"sparsity_target\": 0.3, \"lambda_sparse_final\": 1000, \"lambda_max_cap\": 1000, \"tau_final\": 0.1, \"constraint_loss_final\": 0, \"training_steps\": 1000, \"wall_clock_seconds\": 2662.6, \"gpu_hours\": 0.74, \"note\": \"No PPL evaluation in training script. Sparsity stuck at 0.281 (same as v1). Lambda hit cap=1000 by step 220 and could not push sparsity further. W&B run was offline (not synced).\"}}, \"bce_isocompute_v2_s42\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"final_loss\": 0.6637, \"final_bce_loss\": 0.6586, \"final_reg_loss\": 0.0051, \"final_sparsity\": 0.502, \"training_steps\": 1000, \"training_time_sec\": 1047.8, \"reg_weight\": 2, \"true_dense_ppl\": 6.12, \"predictor_hard_mask_ppl\": 26.76, \"teal_sparse_ppl\": 54.84, \"eval_seq_len\": 2048, \"eval_dataset\": \"wikitext-2\"}}, \"kl_sparsity70_s42\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"kl_sparsity30_s42\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"plan_005_subsumption_s42\": {\"status\": \"DONE\", \"metrics\": {\"linearity_ratio\": 0.2644, \"linearity_ratio_std\": 0.0073, \"magnitude_ratio\": 0.1578, \"magnitude_ratio_std\": 0.0088, \"cosine_similarity\": 0.1962, \"cosine_similarity_std\": 0.0268, \"predictor_effect_norm\": 482.65, \"spon_correction_norm\": 76.2, \"interaction_norm\": 147.74, \"num_samples\": 50, \"seq_len\": 2048, \"conclusion_type\": \"weak_subsumption\"}, \"conclusion\": \"success\"}, \"ste_baseline_s42\": {\"status\": \"DONE\", \"metrics\": {\"true_dense_ppl\": 6.12, \"predictor_hard_mask_ppl\": 8.18, \"teal_sparse_ppl\": 15.77, \"model_level_sparsity\": 0.47, \"ppl_increase_vs_true_dense_pct\": 157.7, \"eval_seq_len\": 2048, \"calibration_samples\": 32, \"eval_dataset\": \"wikitext-2\", \"per_token_sparsity\": 0.47, \"lambda_stats\": {\"steps_70_130_mean\": 66.4, \"steps_70_130_std\": 94.87, \"first_500_mean\": 688.07, \"first_500_std\": 440.57, \"last_500_mean\": 965.69, \"last_500_std\": 141.59, \"overall_mean\": 826.88, \"overall_std\": 354.23}}, \"conclusion\": \"success\"}, \"spon_supp_eval_retry\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"spon_2048_s42\": {\"status\": \"DONE\", \"conclusion\": \"negative\", \"metrics\": {\"true_dense_ppl\": 6.1173, \"predictor_hard_mask_ppl\": 9.2165, \"spon_sparse_ppl\": 8.991, \"spon_recovery_pct\": 7.3, \"ppl_improvement_from_spon\": 0.2255, \"mean_bias_norm\": 0.05312, \"max_bias_norm\": 0.065918, \"model_level_sparsity\": 0.498, \"eval_seq_len\": 2048, \"training_seq_len\": 2048, \"eval_samples\": 141, \"trainable_params\": 458752, \"trainable_pct\": 0.0057, \"training_steps\": 1000, \"final_loss\": 0.377, \"dense_with_spon_ppl\": 6.1823, \"dense_ppl_degradation\": 0.0651, \"teal_sparse_no_spon_ppl\": 12.0776, \"teal_sparse_with_spon_ppl\": 11.7907, \"spon_recovery_teal_pct\": 4.8, \"teal_sparsity\": 0.4979}}, \"bce_isocompute_s42\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"mvp_kl_norm_v2_s456\": {\"status\": \"DONE\", \"metrics\": {\"true_dense_ppl\": 6.1173, \"predictor_hard_mask_ppl\": 9.14, \"teal_sparse_ppl\": 13.58, \"model_level_sparsity\": 0.498, \"ppl_increase_vs_true_dense_pct\": 121.9, \"eval_md5\": \"f4086818bb55dc354ea4c6fe8ed8899a\", \"calibration_samples\": 32, \"vanilla_teal_sparse_ppl_INVALID\": 66036.4062}, \"conclusion\": \"success\"}, \"spon_training\": {\"status\": \"DONE\", \"conclusion\": \"negative\", \"metrics\": {\"true_dense_ppl\": 6.1193, \"predictor_hard_mask_ppl\": 9.2165, \"spon_sparse_ppl\": 9.0977, \"spon_recovery_pct\": 3.8, \"ppl_improvement_from_spon\": 0.1188, \"ppl_increase_vs_true_dense_pct\": 48.7, \"ppl_increase_no_spon_vs_true_dense_pct\": 50.6, \"mean_bias_norm\": 0.040596, \"max_bias_norm\": 0.054199, \"teal_sparse_ppl\": 12.08, \"teal_with_spon_ppl\": 11.93, \"spon_dense_ppl_degradation\": 6.19, \"model_level_sparsity\": 0.5, \"eval_seq_len\": 2048, \"eval_samples\": 141, \"trainable_params\": 458752, \"trainable_pct\": 0.0057}}, \"training_free_wina_greedy\": {\"status\": \"DONE\", \"conclusion\": \"negative\", \"metrics\": {\"wina_greedy_ppl\": 2126.03, \"dense_ppl\": 6.12, \"model_level_sparsity\": 0.5, \"eval_dataset\": \"WikiText-2\", \"eval_seq_len\": 2048, \"greedy_allocation_summary\": \"layers 0-11: 0.90, layer 12: 0.85, layer 13: 0.80, layer 14: 0.70, layers 15-16: 0.50-0.55, layers 17-20: 0.30-0.35, layers 21-24: 0.05-0.15, layers 25-31: 0.00\"}}, \"ste_kl_s42\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"bce_comp_staged_s42\": {\"status\": \"DONE\", \"conclusion\": \"negative\", \"metrics\": {\"true_dense_ppl\": 6.12, \"predictor_hard_mask_ppl\": 25.44, \"predictor_hard_mask_ppl_no_comp\": 27.96, \"teal_sparse_ppl\": 44.54, \"model_level_sparsity\": 0.558, \"ppl_increase_vs_true_dense_pct\": 315.7, \"comp_loss_final\": 0.0033, \"bce_loss_final\": 0.6379, \"eval_seq_len\": 2048, \"calibration_samples\": 32}}, \"spon_training_seq2048\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"kl_only_s0\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"true_dense_ppl\": 6.12, \"predictor_hard_mask_ppl\": 9.19, \"teal_sparse_ppl\": 12.03, \"model_level_sparsity\": 0.499, \"ppl_increase_vs_true_dense_pct\": 96.57, \"eval_seq_len\": 2048, \"calibration_samples\": 32}}, \"kl_only_s1\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"true_dense_ppl\": 6.12, \"predictor_hard_mask_ppl\": 9.15, \"teal_sparse_ppl\": 11.99, \"model_level_sparsity\": 0.498, \"ppl_increase_vs_true_dense_pct\": 96}}, \"mvp_bce_s456\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"true_dense_ppl\": 6.1173, \"predictor_hard_mask_ppl\": 28.1437, \"teal_sparse_ppl\": 43.033, \"model_level_sparsity\": 0.4957, \"ppl_increase_vs_true_dense_pct\": 603.3, \"eval_md5\": \"f4086818bb55dc354ea4c6fe8ed8899a\", \"calibration_samples\": 32, \"vanilla_teal_sparse_ppl_INVALID\": 66036.4062}}, \"mvp_bce_s123\": {\"status\": \"DONE\", \"metrics\": {\"true_dense_ppl\": 6.1173, \"predictor_hard_mask_ppl\": 28.3817, \"teal_sparse_ppl\": 44.5864, \"model_level_sparsity\": 0.4957, \"ppl_increase_vs_true_dense_pct\": 629, \"eval_md5\": \"f4086818bb55dc354ea4c6fe8ed8899a\", \"calibration_samples\": 32, \"vanilla_teal_sparse_ppl_INVALID\": 66036.4062}, \"conclusion\": \"success\"}, \"mvp_bce_s42\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"true_dense_ppl\": 6.1173, \"predictor_hard_mask_ppl\": 27.9603, \"teal_sparse_ppl\": 44.537, \"model_level_sparsity\": 0.4957, \"ppl_increase_vs_true_dense_pct\": 628, \"eval_md5\": \"f4086818bb55dc354ea4c6fe8ed8899a\", \"calibration_samples\": 32, \"vanilla_teal_sparse_ppl_INVALID\": 66036.4062}}, \"mvp_kl_norm_v2_s123\": {\"status\": \"DONE\", \"metrics\": {\"true_dense_ppl\": 6.1173, \"predictor_hard_mask_ppl\": 9.2474, \"teal_sparse_ppl\": 11.9128, \"model_level_sparsity\": 0.4979, \"ppl_increase_vs_true_dense_pct\": 94.7, \"eval_md5\": \"f4086818bb55dc354ea4c6fe8ed8899a\", \"calibration_samples\": 32, \"vanilla_teal_sparse_ppl_INVALID\": 66036.4062}, \"conclusion\": \"success\"}, \"mvp_kl_norm_v2_s42\": {\"status\": \"DONE\", \"metrics\": {\"true_dense_ppl\": 6.1173, \"predictor_hard_mask_ppl\": 9.2142, \"teal_sparse_ppl\": 12.0776, \"model_level_sparsity\": 0.4979, \"ppl_increase_vs_true_dense_pct\": 97.4, \"eval_md5\": \"f4086818bb55dc354ea4c6fe8ed8899a\", \"calibration_samples\": 32, \"vanilla_teal_sparse_ppl_INVALID\": 66036.4062}, \"conclusion\": \"success\"}, \"mvp_kl_norm_s123\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"mvp_kl_norm_s42\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"kl_normalized_quicktest\": {\"status\": \"DONE\", \"conclusion\": \"failed\", \"metrics\": {\"step1_kl\": 1.18, \"step200_kl\": 0.641, \"step200_sparsity\": 0.504, \"final_lambda\": 8, \"sparsity_converged_step\": 80, \"sparsity_trajectory\": [0.406, 0.398, 0.398, 0.457, 0.52, 0.506, 0.504, 0.504], \"lambda_trajectory\": [1, 2, 4, 8, 8, 8, 8, 8]}}, \"kl_lagrangian_quicktest\": {\"status\": \"DONE\", \"conclusion\": \"negative\", \"metrics\": {\"final_kl_loss\": 418, \"final_constraint_loss\": 1.211, \"final_sparsity\": 0.141, \"final_lambda\": 5.06, \"steps\": 200, \"sparsity_trajectory\": [0.406, 0.387, 0.289, 0.168, 0.141]}}, \"mvp_kl_s42\": {\"status\": \"DONE\", \"conclusion\": \"negative\", \"metrics\": {\"final_total_loss\": 3.3438, \"final_kl_loss\": 3.2969, \"final_reg_loss\": 0.05, \"final_sparsity\": 0, \"steps\": 1000, \"tau_final\": 0.1, \"wikitext2_ppl_dense\": 6.12, \"wikitext2_ppl_sparse\": 455.93, \"wikitext2_ppl_increase_pct\": 7349, \"model_level_sparsity\": 0.372, \"checkpoint_path\": \"/root/distill_sparse_swiglu/checkpoints/mvp_kl_s42/predictor_kl.pt\"}}}, \"count\": 67, \"total\": 67, \"baseline\": \"bench_dense\"}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.2689}}"
    }
  }
}
```

</details>

---

### Assistant

_source line 20_

<details><summary>Logged reasoning block</summary>

```text
I now have all the registry data. Let me cross-verify:

1. **bench_teal30**: PPL=10.97, ARC=0.4232, WG=0.6606, MMLU=0.3861, GSM8K=0.0788 ✓
2. **bench_teal50**: PPL=23.31, ARC=0.2841, WG=0.5304, MMLU=0.2832, GSM8K=0.0197 ✓
3. **bench_kl40_global**: PPL=10.117, ARC=0.4096, WG=0.6535, MMLU=0.3806, GSM8K=0.05 ✓


4. **Multi-seed KL 50% uniform**: I'm checking the three seed variants (s42, s123, s456) with their respective performance metrics across PPL, ARC, WG, MMLU, and GSM8K benchmarks.

Now I'm calculating the mean and standard deviation across seeds for MMLU and PPL to understand the variance in these metrics. For MMLU, the three scores average to about 0.2801 with a standard deviation of roughly 0.0065, while PPL values cluster around 11.918 with relatively tight variance. The sum of squared differences gives me a sample variance of about 0.0058, which means the standard deviation is roughly 0.076—so the PPL std checks out at around 0.08 when rounded, and the coefficient of variation is well under 1% as required. Now I'm calculating the relative performance changes compared to the dense baseline across all the metrics. Now I'm looking at the performance degradation across different configurations—TEAL with 50% unified shows even steeper drops across all benchmarks, with GSM8K plummeting to 96% worse, while KL with 40% global starts to show some recovery in perplexity but the calculation appears to be cut off. Updating the table structure now—I'll insert the KL 40% global row in the right position, replace the queued entries with actual TEAL unified data, and then revise the key observations to reflect the new numbers.

For the multi-seed results, I'm calculating the means and standard deviations across the three runs: PPL averages around 11.92 with minimal variance, ARC sits at about 0.338, and I need to finish compiling the WG metrics. Now I'm calculating the coefficient of variation for perplexity and MMLU to compare their relative variability—PPL shows about 0.64% CV while MMLU is higher at 2.3% CV. The PPL values align with what was mentioned in the task header, so I'll use these computed statistics to build out the full results table.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "f716b164-a763-4033-b921-7fe9fd43c5b1",
  "uuid": "db3236d9-9c2a-4c34-9b01-258e2ef22def",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016v4KrmUAXcPXa2g2fqrCv9",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 10391,
      "cache_read_input_tokens": 26840,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 10391
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

_source line 21_

Registry data verified. All numbers match the task description. Now computing relative changes and updating the table.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "f716b164-a763-4033-b921-7fe9fd43c5b1",
  "uuid": "69c8fed9-d4fe-423c-bb18-cbb72cac68fe",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016v4KrmUAXcPXa2g2fqrCv9",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 10391,
      "cache_read_input_tokens": 26840,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 10391
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

_source line 22_

<details open><summary>🔧 Tool call — Write · `toolu_01Mb3miMyr1wKCWi9CsqTdUf`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/_project/report/benchmark_comparison_table.md",
  "content": "# Unified Benchmark Comparison Table\n\n**Model**: Llama-3.1-8B | **Eval**: benchmark_eval.py (ARC-c=25-shot, WG=5-shot, MMLU=5-shot, GSM8K=8-shot, WikiText-2 PPL)\n\n## Main Results\n\n| Condition | Sparsity | Allocation | PPL | ARC-c | WG | MMLU | GSM8K |\n|-----------|----------|------------|-----|-------|-----|------|-------|\n| Dense (baseline) | 0% | — | 6.117 | 0.5828 | 0.7806 | 0.6527 | 0.4875 |\n| KL 30% | 30% | uniform | 8.816 | 0.4078 | 0.6859 | 0.4061 | 0.0735 |\n| KL 40% | 40% | uniform | 8.363 | 0.4181 | 0.6717 | 0.3068 | 0.0394 |\n| KL 50% | 50% | uniform | 11.960 | 0.3276 | 0.6290 | 0.2777 | 0.0212 |\n| KL 30% | 30% | global | 8.977 | 0.3968 | 0.7017 | 0.2527 | 0.0879 |\n| KL 40% | 40% | global | 10.117 | 0.4096 | 0.6535 | 0.3806 | 0.0500 |\n| KL 50% | 50% | global | 11.793 | 0.3285 | 0.6346 | 0.2789 | 0.0129 |\n| BCE v3 (2700 steps) | 50% | learned | 22.510 | 0.2398 | 0.5059 | 0.3002 | 0.0485 |\n| TEAL 30% | 30% | magnitude | 10.970 | 0.4232 | 0.6606 | 0.3861 | 0.0788 |\n| TEAL 50% | 50% | magnitude | 23.310 | 0.2841 | 0.5304 | 0.2832 | 0.0197 |\n| TEAL 50% † | 50% | magnitude | 27.970* | 0.2910 | 0.5556 | 0.2856 | 0.0190 |\n\n† lm_eval_teal_50pct uses lm-evaluation-harness (0-shot default), not directly comparable to unified few-shot results. Retained for reference only.\n\\* TEAL PPL from eval_bce_v3_s42 `teal_sparse_ppl` measurement (same model, same WikiText-2 split).\n\n**Multi-seed stability (KL 50% uniform, seeds 42/123/456):**\n\n| Metric | s42 | s123 | s456 | Mean | Std | CV |\n|--------|-----|------|------|------|-----|-----|\n| PPL | 11.963 | 11.830 | 11.960 | 11.918 | 0.076 | 0.64% |\n| ARC-c | 0.3276 | 0.3515 | 0.3345 | 0.3379 | 0.012 | 3.6% |\n| WG | 0.6290 | 0.6298 | 0.6275 | 0.6288 | 0.001 | 0.2% |\n| MMLU | 0.2777 | 0.2751 | 0.2874 | 0.2801 | 0.0065 | 2.3% |\n| GSM8K | 0.0212 | 0.0235 | 0.0212 | 0.0220 | 0.0013 | 6.0% |\n\n## Relative Change vs Dense (%)\n\n| Condition | PPL ↑ | ARC-c ↓ | WG ↓ | MMLU ↓ | GSM8K ↓ |\n|-----------|-------|---------|------|--------|---------|\n| KL 30% uniform | +44.1% | −30.0% | −12.1% | −37.8% | −84.9% |\n| KL 40% uniform | +36.7% | −28.3% | −14.0% | −53.0% | −91.9% |\n| KL 50% uniform | +95.5% | −43.8% | −19.4% | −57.4% | −95.7% |\n| KL 30% global | +46.7% | −31.9% | −10.1% | −61.3% | −82.0% |\n| KL 40% global | +65.4% | −29.7% | −16.3% | −41.7% | −89.7% |\n| KL 50% global | +92.8% | −43.6% | −18.7% | −57.3% | −97.4% |\n| BCE v3 50% | +268.0% | −58.8% | −35.2% | −54.0% | −90.1% |\n| TEAL 30% | +79.3% | −27.4% | −15.4% | −40.8% | −83.8% |\n| TEAL 50% | +281.1% | −51.3% | −32.1% | −56.6% | −96.0% |\n\n## Key Observations\n\n1. **KL >> BCE >> TEAL at 50% sparsity**: KL uniform achieves PPL 11.96 vs BCE 22.51 vs TEAL 23.31 (unified). KL predictor (1000 steps) dominates both iso-compute BCE (2700 steps) and training-free TEAL.\n\n2. **Uniform vs Global allocation**: At 30% sparsity, uniform preserves MMLU (0.4061 vs 0.2527, +60.7% relative) while global collapses it. At 40%, global surprisingly preserves MMLU better (0.3806 vs 0.3068) with higher PPL (10.12 vs 8.36). At 50% both collapse.\n\n3. **PPL-downstream dissociation**: KL 40% uniform has lower PPL (8.36) than KL 30% (8.82) yet worse MMLU (0.3068 vs 0.4061). PPL alone does not capture knowledge preservation; downstream metrics are essential.\n\n4. **Phase transition 30%→40%**: MMLU drops from 0.4061 to 0.3068 (−24.5pp), GSM8K from 0.0735 to 0.0394 (−3.4pp). The threshold for knowledge/reasoning retention lies between 30–40% sparsity.\n\n5. **KL 30% uniform ≈ TEAL 30% on downstream**: ARC-c (0.4078 vs 0.4232), WG (0.6859 vs 0.6606), MMLU (0.4061 vs 0.3861), GSM8K (0.0735 vs 0.0788). KL's advantage is primarily in PPL (8.82 vs 10.97, −19.6%) rather than downstream accuracy at 30% sparsity.\n\n6. **Multi-seed stability**: KL 50% uniform shows low variance across 3 seeds — PPL CV=0.64%, MMLU CV=2.3%. Results are reproducible.\n\n---\n*Generated 2026-05-16. Source: distill_sparse_swiglu registry.*\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "f716b164-a763-4033-b921-7fe9fd43c5b1",
  "uuid": "ebde8e4a-be7f-45f5-8a95-d16927095747",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016v4KrmUAXcPXa2g2fqrCv9",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 10391,
      "cache_read_input_tokens": 26840,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 10391
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

_source line 23 · 2026-05-16T17:01:18.238Z_

<details><summary>↩ Tool result · `toolu_01Mb3miMyr1wKCWi9CsqTdUf`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/_project/report/benchmark_comparison_table.md has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "f716b164-a763-4033-b921-7fe9fd43c5b1",
  "uuid": "fcb2ec2f-0da2-41f1-9061-035a6e291747",
  "tool_use_result": {
    "type": "update",
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/_project/report/benchmark_comparison_table.md",
    "content": "# Unified Benchmark Comparison Table\n\n**Model**: Llama-3.1-8B | **Eval**: benchmark_eval.py (ARC-c=25-shot, WG=5-shot, MMLU=5-shot, GSM8K=8-shot, WikiText-2 PPL)\n\n## Main Results\n\n| Condition | Sparsity | Allocation | PPL | ARC-c | WG | MMLU | GSM8K |\n|-----------|----------|------------|-----|-------|-----|------|-------|\n| Dense (baseline) | 0% | — | 6.117 | 0.5828 | 0.7806 | 0.6527 | 0.4875 |\n| KL 30% | 30% | uniform | 8.816 | 0.4078 | 0.6859 | 0.4061 | 0.0735 |\n| KL 40% | 40% | uniform | 8.363 | 0.4181 | 0.6717 | 0.3068 | 0.0394 |\n| KL 50% | 50% | uniform | 11.960 | 0.3276 | 0.6290 | 0.2777 | 0.0212 |\n| KL 30% | 30% | global | 8.977 | 0.3968 | 0.7017 | 0.2527 | 0.0879 |\n| KL 40% | 40% | global | 10.117 | 0.4096 | 0.6535 | 0.3806 | 0.0500 |\n| KL 50% | 50% | global | 11.793 | 0.3285 | 0.6346 | 0.2789 | 0.0129 |\n| BCE v3 (2700 steps) | 50% | learned | 22.510 | 0.2398 | 0.5059 | 0.3002 | 0.0485 |\n| TEAL 30% | 30% | magnitude | 10.970 | 0.4232 | 0.6606 | 0.3861 | 0.0788 |\n| TEAL 50% | 50% | magnitude | 23.310 | 0.2841 | 0.5304 | 0.2832 | 0.0197 |\n| TEAL 50% † | 50% | magnitude | 27.970* | 0.2910 | 0.5556 | 0.2856 | 0.0190 |\n\n† lm_eval_teal_50pct uses lm-evaluation-harness (0-shot default), not directly comparable to unified few-shot results. Retained for reference only.\n\\* TEAL PPL from eval_bce_v3_s42 `teal_sparse_ppl` measurement (same model, same WikiText-2 split).\n\n**Multi-seed stability (KL 50% uniform, seeds 42/123/456):**\n\n| Metric | s42 | s123 | s456 | Mean | Std | CV |\n|--------|-----|------|------|------|-----|-----|\n| PPL | 11.963 | 11.830 | 11.960 | 11.918 | 0.076 | 0.64% |\n| ARC-c | 0.3276 | 0.3515 | 0.3345 | 0.3379 | 0.012 | 3.6% |\n| WG | 0.6290 | 0.6298 | 0.6275 | 0.6288 | 0.001 | 0.2% |\n| MMLU | 0.2777 | 0.2751 | 0.2874 | 0.2801 | 0.0065 | 2.3% |\n| GSM8K | 0.0212 | 0.0235 | 0.0212 | 0.0220 | 0.0013 | 6.0% |\n\n## Relative Change vs Dense (%)\n\n| Condition | PPL ↑ | ARC-c ↓ | WG ↓ | MMLU ↓ | GSM8K ↓ |\n|-----------|-------|---------|------|--------|---------|\n| KL 30% uniform | +44.1% | −30.0% | −12.1% | −37.8% | −84.9% |\n| KL 40% uniform | +36.7% | −28.3% | −14.0% | −53.0% | −91.9% |\n| KL 50% uniform | +95.5% | −43.8% | −19.4% | −57.4% | −95.7% |\n| KL 30% global | +46.7% | −31.9% | −10.1% | −61.3% | −82.0% |\n| KL 40% global | +65.4% | −29.7% | −16.3% | −41.7% | −89.7% |\n| KL 50% global | +92.8% | −43.6% | −18.7% | −57.3% | −97.4% |\n| BCE v3 50% | +268.0% | −58.8% | −35.2% | −54.0% | −90.1% |\n| TEAL 30% | +79.3% | −27.4% | −15.4% | −40.8% | −83.8% |\n| TEAL 50% | +281.1% | −51.3% | −32.1% | −56.6% | −96.0% |\n\n## Key Observations\n\n1. **KL >> BCE >> TEAL at 50% sparsity**: KL uniform achieves PPL 11.96 vs BCE 22.51 vs TEAL 23.31 (unified). KL predictor (1000 steps) dominates both iso-compute BCE (2700 steps) and training-free TEAL.\n\n2. **Uniform vs Global allocation**: At 30% sparsity, uniform preserves MMLU (0.4061 vs 0.2527, +60.7% relative) while global collapses it. At 40%, global surprisingly preserves MMLU better (0.3806 vs 0.3068) with higher PPL (10.12 vs 8.36). At 50% both collapse.\n\n3. **PPL-downstream dissociation**: KL 40% uniform has lower PPL (8.36) than KL 30% (8.82) yet worse MMLU (0.3068 vs 0.4061). PPL alone does not capture knowledge preservation; downstream metrics are essential.\n\n4. **Phase transition 30%→40%**: MMLU drops from 0.4061 to 0.3068 (−24.5pp), GSM8K from 0.0735 to 0.0394 (−3.4pp). The threshold for knowledge/reasoning retention lies between 30–40% sparsity.\n\n5. **KL 30% uniform ≈ TEAL 30% on downstream**: ARC-c (0.4078 vs 0.4232), WG (0.6859 vs 0.6606), MMLU (0.4061 vs 0.3861), GSM8K (0.0735 vs 0.0788). KL's advantage is primarily in PPL (8.82 vs 10.97, −19.6%) rather than downstream accuracy at 30% sparsity.\n\n6. **Multi-seed stability**: KL 50% uniform shows low variance across 3 seeds — PPL CV=0.64%, MMLU CV=2.3%. Results are reproducible.\n\n---\n*Generated 2026-05-16. Source: distill_sparse_swiglu registry.*\n",
    "structuredPatch": [
      {
        "oldStart": 11,
        "oldLines": 15,
        "newStart": 11,
        "newLines": 26,
        "lines": [
          " | KL 40% | 40% | uniform | 8.363 | 0.4181 | 0.6717 | 0.3068 | 0.0394 |",
          " | KL 50% | 50% | uniform | 11.960 | 0.3276 | 0.6290 | 0.2777 | 0.0212 |",
          " | KL 30% | 30% | global | 8.977 | 0.3968 | 0.7017 | 0.2527 | 0.0879 |",
          "+| KL 40% | 40% | global | 10.117 | 0.4096 | 0.6535 | 0.3806 | 0.0500 |",
          " | KL 50% | 50% | global | 11.793 | 0.3285 | 0.6346 | 0.2789 | 0.0129 |",
          " | BCE v3 (2700 steps) | 50% | learned | 22.510 | 0.2398 | 0.5059 | 0.3002 | 0.0485 |",
          "+| TEAL 30% | 30% | magnitude | 10.970 | 0.4232 | 0.6606 | 0.3861 | 0.0788 |",
          "+| TEAL 50% | 50% | magnitude | 23.310 | 0.2841 | 0.5304 | 0.2832 | 0.0197 |",
          " | TEAL 50% † | 50% | magnitude | 27.970* | 0.2910 | 0.5556 | 0.2856 | 0.0190 |",
          "-| TEAL 50% (unified) | 50% | magnitude | — queued | — queued | — queued | — queued | — queued |",
          "-| TEAL 30% (unified) | 30% | magnitude | — queued | — queued | — queued | — queued | — queued |",
          " ",
          "-† lm_eval_teal_50pct uses lm-evaluation-harness (0-shot default), not directly comparable to unified few-shot results.",
          "+† lm_eval_teal_50pct uses lm-evaluation-harness (0-shot default), not directly comparable to unified few-shot results. Retained for reference only.",
          " \\* TEAL PPL from eval_bce_v3_s42 `teal_sparse_ppl` measurement (same model, same WikiText-2 split).",
          " ",
          "+**Multi-seed stability (KL 50% uniform, seeds 42/123/456):**",
          "+",
          "+| Metric | s42 | s123 | s456 | Mean | Std | CV |",
          "+|--------|-----|------|------|------|-----|-----|",
          "+| PPL | 11.963 | 11.830 | 11.960 | 11.918 | 0.076 | 0.64% |",
          "+| ARC-c | 0.3276 | 0.3515 | 0.3345 | 0.3379 | 0.012 | 3.6% |",
          "+| WG | 0.6290 | 0.6298 | 0.6275 | 0.6288 | 0.001 | 0.2% |",
          "+| MMLU | 0.2777 | 0.2751 | 0.2874 | 0.2801 | 0.0065 | 2.3% |",
          "+| GSM8K | 0.0212 | 0.0235 | 0.0212 | 0.0220 | 0.0013 | 6.0% |",
          "+",
          " ## Relative Change vs Dense (%)",
          " ",
          " | Condition | PPL ↑ | ARC-c ↓ | WG ↓ | MMLU ↓ | GSM8K ↓ |"
        ]
      },
      {
        "oldStart": 28,
        "oldLines": 19,
        "newStart": 39,
        "newLines": 25,
        "lines": [
          " | KL 40% uniform | +36.7% | −28.3% | −14.0% | −53.0% | −91.9% |",
          " | KL 50% uniform | +95.5% | −43.8% | −19.4% | −57.4% | −95.7% |",
          " | KL 30% global | +46.7% | −31.9% | −10.1% | −61.3% | −82.0% |",
          "+| KL 40% global | +65.4% | −29.7% | −16.3% | −41.7% | −89.7% |",
          " | KL 50% global | +92.8% | −43.6% | −18.7% | −57.3% | −97.4% |",
          " | BCE v3 50% | +268.0% | −58.8% | −35.2% | −54.0% | −90.1% |",
          "-| TEAL 50% † | +357.2% | −50.1% | −28.8% | −56.2% | −96.1% |",
          "+| TEAL 30% | +79.3% | −27.4% | −15.4% | −40.8% | −83.8% |",
          "+| TEAL 50% | +281.1% | −51.3% | −32.1% | −56.6% | −96.0% |",
          " ",
          " ## Key Observations",
          " ",
          "-1. **KL >> BCE >> TEAL at 50% sparsity**: KL uniform achieves PPL 11.96 vs BCE 22.51 vs TEAL 27.97. KL predictor (1000 steps) dominates both iso-compute BCE (2700 steps) and training-free TEAL.",
          "+1. **KL >> BCE >> TEAL at 50% sparsity**: KL uniform achieves PPL 11.96 vs BCE 22.51 vs TEAL 23.31 (unified). KL predictor (1000 steps) dominates both iso-compute BCE (2700 steps) and training-free TEAL.",
          " ",
          "-2. **Uniform vs Global allocation**: At 30% sparsity, uniform preserves MMLU (0.4061 vs 0.2527, +60.7% relative) while global collapses it. At 50% both collapse. Global allocation concentrates sparsity on critical layers, destroying knowledge.",
          "+2. **Uniform vs Global allocation**: At 30% sparsity, uniform preserves MMLU (0.4061 vs 0.2527, +60.7% relative) while global collapses it. At 40%, global surprisingly preserves MMLU better (0.3806 vs 0.3068) with higher PPL (10.12 vs 8.36). At 50% both collapse.",
          " ",
          "-3. **PPL-downstream dissociation**: KL 40% has lower PPL (8.36) than KL 30% (8.82) yet worse MMLU (0.3068 vs 0.4061). PPL alone does not capture knowledge preservation; downstream metrics are essential.",
          "+3. **PPL-downstream dissociation**: KL 40% uniform has lower PPL (8.36) than KL 30% (8.82) yet worse MMLU (0.3068 vs 0.4061). PPL alone does not capture knowledge preservation; downstream metrics are essential.",
          " ",
          " 4. **Phase transition 30%→40%**: MMLU drops from 0.4061 to 0.3068 (−24.5pp), GSM8K from 0.0735 to 0.0394 (−3.4pp). The threshold for knowledge/reasoning retention lies between 30–40% sparsity.",
          " ",
          "+5. **KL 30% uniform ≈ TEAL 30% on downstream**: ARC-c (0.4078 vs 0.4232), WG (0.6859 vs 0.6606), MMLU (0.4061 vs 0.3861), GSM8K (0.0735 vs 0.0788). KL's advantage is primarily in PPL (8.82 vs 10.97, −19.6%) rather than downstream accuracy at 30% sparsity.",
          "+",
          "+6. **Multi-seed stability**: KL 50% uniform shows low variance across 3 seeds — PPL CV=0.64%, MMLU CV=2.3%. Results are reproducible.",
          "+",
          " ---",
          " *Generated 2026-05-16. Source: distill_sparse_swiglu registry.*"
        ]
      }
    ],
    "originalFile": "# Unified Benchmark Comparison Table\n\n**Model**: Llama-3.1-8B | **Eval**: benchmark_eval.py (ARC-c=25-shot, WG=5-shot, MMLU=5-shot, GSM8K=8-shot, WikiText-2 PPL)\n\n## Main Results\n\n| Condition | Sparsity | Allocation | PPL | ARC-c | WG | MMLU | GSM8K |\n|-----------|----------|------------|-----|-------|-----|------|-------|\n| Dense (baseline) | 0% | — | 6.117 | 0.5828 | 0.7806 | 0.6527 | 0.4875 |\n| KL 30% | 30% | uniform | 8.816 | 0.4078 | 0.6859 | 0.4061 | 0.0735 |\n| KL 40% | 40% | uniform | 8.363 | 0.4181 | 0.6717 | 0.3068 | 0.0394 |\n| KL 50% | 50% | uniform | 11.960 | 0.3276 | 0.6290 | 0.2777 | 0.0212 |\n| KL 30% | 30% | global | 8.977 | 0.3968 | 0.7017 | 0.2527 | 0.0879 |\n| KL 50% | 50% | global | 11.793 | 0.3285 | 0.6346 | 0.2789 | 0.0129 |\n| BCE v3 (2700 steps) | 50% | learned | 22.510 | 0.2398 | 0.5059 | 0.3002 | 0.0485 |\n| TEAL 50% † | 50% | magnitude | 27.970* | 0.2910 | 0.5556 | 0.2856 | 0.0190 |\n| TEAL 50% (unified) | 50% | magnitude | — queued | — queued | — queued | — queued | — queued |\n| TEAL 30% (unified) | 30% | magnitude | — queued | — queued | — queued | — queued | — queued |\n\n† lm_eval_teal_50pct uses lm-evaluation-harness (0-shot default), not directly comparable to unified few-shot results.\n\\* TEAL PPL from eval_bce_v3_s42 `teal_sparse_ppl` measurement (same model, same WikiText-2 split).\n\n## Relative Change vs Dense (%)\n\n| Condition | PPL ↑ | ARC-c ↓ | WG ↓ | MMLU ↓ | GSM8K ↓ |\n|-----------|-------|---------|------|--------|---------|\n| KL 30% uniform | +44.1% | −30.0% | −12.1% | −37.8% | −84.9% |\n| KL 40% uniform | +36.7% | −28.3% | −14.0% | −53.0% | −91.9% |\n| KL 50% uniform | +95.5% | −43.8% | −19.4% | −57.4% | −95.7% |\n| KL 30% global | +46.7% | −31.9% | −10.1% | −61.3% | −82.0% |\n| KL 50% global | +92.8% | −43.6% | −18.7% | −57.3% | −97.4% |\n| BCE v3 50% | +268.0% | −58.8% | −35.2% | −54.0% | −90.1% |\n| TEAL 50% † | +357.2% | −50.1% | −28.8% | −56.2% | −96.1% |\n\n## Key Observations\n\n1. **KL >> BCE >> TEAL at 50% sparsity**: KL uniform achieves PPL 11.96 vs BCE 22.51 vs TEAL 27.97. KL predictor (1000 steps) dominates both iso-compute BCE (2700 steps) and training-free TEAL.\n\n2. **Uniform vs Global allocation**: At 30% sparsity, uniform preserves MMLU (0.4061 vs 0.2527, +60.7% relative) while global collapses it. At 50% both collapse. Global allocation concentrates sparsity on critical layers, destroying knowledge.\n\n3. **PPL-downstream dissociation**: KL 40% has lower PPL (8.36) than KL 30% (8.82) yet worse MMLU (0.3068 vs 0.4061). PPL alone does not capture knowledge preservation; downstream metrics are essential.\n\n4. **Phase transition 30%→40%**: MMLU drops from 0.4061 to 0.3068 (−24.5pp), GSM8K from 0.0735 to 0.0394 (−3.4pp). The threshold for knowledge/reasoning retention lies between 30–40% sparsity.\n\n---\n*Generated 2026-05-16. Source: distill_sparse_swiglu registry.*\n",
    "userModified": false
  }
}
```

</details>

---

### Assistant

_source line 24_

<details><summary>Logged reasoning block</summary>

```text
Let me verify the file was written correctly by reading it back.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "f716b164-a763-4033-b921-7fe9fd43c5b1",
  "uuid": "8f6302b1-a2e7-4ef2-913f-59923f36f57e",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011Pb3x1emJFVHHThgvoEdUT",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5026,
      "cache_read_input_tokens": 37231,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 5026
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

Updated. Let me verify the file.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "f716b164-a763-4033-b921-7fe9fd43c5b1",
  "uuid": "5a7560c0-4366-4dab-8ea8-05269417ae07",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011Pb3x1emJFVHHThgvoEdUT",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5026,
      "cache_read_input_tokens": 37231,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 5026
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

<details open><summary>🔧 Tool call — Read · `toolu_01Tkxn8sKrbBKfdtYoJupjMk`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/_project/report/benchmark_comparison_table.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "f716b164-a763-4033-b921-7fe9fd43c5b1",
  "uuid": "000ea919-577c-4b74-ad5e-76480b2a9b09",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011Pb3x1emJFVHHThgvoEdUT",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5026,
      "cache_read_input_tokens": 37231,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 5026
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

_source line 27 · 2026-05-16T17:01:21.721Z_

<details><summary>↩ Tool result · `toolu_01Tkxn8sKrbBKfdtYoJupjMk`</summary>

```text
1	# Unified Benchmark Comparison Table
2	
3	**Model**: Llama-3.1-8B | **Eval**: benchmark_eval.py (ARC-c=25-shot, WG=5-shot, MMLU=5-shot, GSM8K=8-shot, WikiText-2 PPL)
4	
5	## Main Results
6	
7	| Condition | Sparsity | Allocation | PPL | ARC-c | WG | MMLU | GSM8K |
8	|-----------|----------|------------|-----|-------|-----|------|-------|
9	| Dense (baseline) | 0% | — | 6.117 | 0.5828 | 0.7806 | 0.6527 | 0.4875 |
10	| KL 30% | 30% | uniform | 8.816 | 0.4078 | 0.6859 | 0.4061 | 0.0735 |
11	| KL 40% | 40% | uniform | 8.363 | 0.4181 | 0.6717 | 0.3068 | 0.0394 |
12	| KL 50% | 50% | uniform | 11.960 | 0.3276 | 0.6290 | 0.2777 | 0.0212 |
13	| KL 30% | 30% | global | 8.977 | 0.3968 | 0.7017 | 0.2527 | 0.0879 |
14	| KL 40% | 40% | global | 10.117 | 0.4096 | 0.6535 | 0.3806 | 0.0500 |
15	| KL 50% | 50% | global | 11.793 | 0.3285 | 0.6346 | 0.2789 | 0.0129 |
16	| BCE v3 (2700 steps) | 50% | learned | 22.510 | 0.2398 | 0.5059 | 0.3002 | 0.0485 |
17	| TEAL 30% | 30% | magnitude | 10.970 | 0.4232 | 0.6606 | 0.3861 | 0.0788 |
18	| TEAL 50% | 50% | magnitude | 23.310 | 0.2841 | 0.5304 | 0.2832 | 0.0197 |
19	| TEAL 50% † | 50% | magnitude | 27.970* | 0.2910 | 0.5556 | 0.2856 | 0.0190 |
20	
21	† lm_eval_teal_50pct uses lm-evaluation-harness (0-shot default), not directly comparable to unified few-shot results. Retained for reference only.
22	\* TEAL PPL from eval_bce_v3_s42 `teal_sparse_ppl` measurement (same model, same WikiText-2 split).
23	
24	**Multi-seed stability (KL 50% uniform, seeds 42/123/456):**
25	
26	| Metric | s42 | s123 | s456 | Mean | Std | CV |
27	|--------|-----|------|------|------|-----|-----|
28	| PPL | 11.963 | 11.830 | 11.960 | 11.918 | 0.076 | 0.64% |
29	| ARC-c | 0.3276 | 0.3515 | 0.3345 | 0.3379 | 0.012 | 3.6% |
30	| WG | 0.6290 | 0.6298 | 0.6275 | 0.6288 | 0.001 | 0.2% |
31	| MMLU | 0.2777 | 0.2751 | 0.2874 | 0.2801 | 0.0065 | 2.3% |
32	| GSM8K | 0.0212 | 0.0235 | 0.0212 | 0.0220 | 0.0013 | 6.0% |
33	
34	## Relative Change vs Dense (%)
35	
36	| Condition | PPL ↑ | ARC-c ↓ | WG ↓ | MMLU ↓ | GSM8K ↓ |
37	|-----------|-------|---------|------|--------|---------|
38	| KL 30% uniform | +44.1% | −30.0% | −12.1% | −37.8% | −84.9% |
39	| KL 40% uniform | +36.7% | −28.3% | −14.0% | −53.0% | −91.9% |
40	| KL 50% uniform | +95.5% | −43.8% | −19.4% | −57.4% | −95.7% |
41	| KL 30% global | +46.7% | −31.9% | −10.1% | −61.3% | −82.0% |
42	| KL 40% global | +65.4% | −29.7% | −16.3% | −41.7% | −89.7% |
43	| KL 50% global | +92.8% | −43.6% | −18.7% | −57.3% | −97.4% |
44	| BCE v3 50% | +268.0% | −58.8% | −35.2% | −54.0% | −90.1% |
45	| TEAL 30% | +79.3% | −27.4% | −15.4% | −40.8% | −83.8% |
46	| TEAL 50% | +281.1% | −51.3% | −32.1% | −56.6% | −96.0% |
47	
48	## Key Observations
49	
50	1. **KL >> BCE >> TEAL at 50% sparsity**: KL uniform achieves PPL 11.96 vs BCE 22.51 vs TEAL 23.31 (unified). KL predictor (1000 steps) dominates both iso-compute BCE (2700 steps) and training-free TEAL.
51	
52	2. **Uniform vs Global allocation**: At 30% sparsity, uniform preserves MMLU (0.4061 vs 0.2527, +60.7% relative) while global collapses it. At 40%, global surprisingly preserves MMLU better (0.3806 vs 0.3068) with higher PPL (10.12 vs 8.36). At 50% both collapse.
53	
54	3. **PPL-downstream dissociation**: KL 40% uniform has lower PPL (8.36) than KL 30% (8.82) yet worse MMLU (0.3068 vs 0.4061). PPL alone does not capture knowledge preservation; downstream metrics are essential.
55	
56	4. **Phase transition 30%→40%**: MMLU drops from 0.4061 to 0.3068 (−24.5pp), GSM8K from 0.0735 to 0.0394 (−3.4pp). The threshold for knowledge/reasoning retention lies between 30–40% sparsity.
57	
58	5. **KL 30% uniform ≈ TEAL 30% on downstream**: ARC-c (0.4078 vs 0.4232), WG (0.6859 vs 0.6606), MMLU (0.4061 vs 0.3861), GSM8K (0.0735 vs 0.0788). KL's advantage is primarily in PPL (8.82 vs 10.97, −19.6%) rather than downstream accuracy at 30% sparsity.
59	
60	6. **Multi-seed stability**: KL 50% uniform shows low variance across 3 seeds — PPL CV=0.64%, MMLU CV=2.3%. Results are reproducible.
61	
62	---
63	*Generated 2026-05-16. Source: distill_sparse_swiglu registry.*
64	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "f716b164-a763-4033-b921-7fe9fd43c5b1",
  "uuid": "f74c81de-5d1d-4db6-ac40-18e50c0c67c3",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/_project/report/benchmark_comparison_table.md",
      "content": "# Unified Benchmark Comparison Table\n\n**Model**: Llama-3.1-8B | **Eval**: benchmark_eval.py (ARC-c=25-shot, WG=5-shot, MMLU=5-shot, GSM8K=8-shot, WikiText-2 PPL)\n\n## Main Results\n\n| Condition | Sparsity | Allocation | PPL | ARC-c | WG | MMLU | GSM8K |\n|-----------|----------|------------|-----|-------|-----|------|-------|\n| Dense (baseline) | 0% | — | 6.117 | 0.5828 | 0.7806 | 0.6527 | 0.4875 |\n| KL 30% | 30% | uniform | 8.816 | 0.4078 | 0.6859 | 0.4061 | 0.0735 |\n| KL 40% | 40% | uniform | 8.363 | 0.4181 | 0.6717 | 0.3068 | 0.0394 |\n| KL 50% | 50% | uniform | 11.960 | 0.3276 | 0.6290 | 0.2777 | 0.0212 |\n| KL 30% | 30% | global | 8.977 | 0.3968 | 0.7017 | 0.2527 | 0.0879 |\n| KL 40% | 40% | global | 10.117 | 0.4096 | 0.6535 | 0.3806 | 0.0500 |\n| KL 50% | 50% | global | 11.793 | 0.3285 | 0.6346 | 0.2789 | 0.0129 |\n| BCE v3 (2700 steps) | 50% | learned | 22.510 | 0.2398 | 0.5059 | 0.3002 | 0.0485 |\n| TEAL 30% | 30% | magnitude | 10.970 | 0.4232 | 0.6606 | 0.3861 | 0.0788 |\n| TEAL 50% | 50% | magnitude | 23.310 | 0.2841 | 0.5304 | 0.2832 | 0.0197 |\n| TEAL 50% † | 50% | magnitude | 27.970* | 0.2910 | 0.5556 | 0.2856 | 0.0190 |\n\n† lm_eval_teal_50pct uses lm-evaluation-harness (0-shot default), not directly comparable to unified few-shot results. Retained for reference only.\n\\* TEAL PPL from eval_bce_v3_s42 `teal_sparse_ppl` measurement (same model, same WikiText-2 split).\n\n**Multi-seed stability (KL 50% uniform, seeds 42/123/456):**\n\n| Metric | s42 | s123 | s456 | Mean | Std | CV |\n|--------|-----|------|------|------|-----|-----|\n| PPL | 11.963 | 11.830 | 11.960 | 11.918 | 0.076 | 0.64% |\n| ARC-c | 0.3276 | 0.3515 | 0.3345 | 0.3379 | 0.012 | 3.6% |\n| WG | 0.6290 | 0.6298 | 0.6275 | 0.6288 | 0.001 | 0.2% |\n| MMLU | 0.2777 | 0.2751 | 0.2874 | 0.2801 | 0.0065 | 2.3% |\n| GSM8K | 0.0212 | 0.0235 | 0.0212 | 0.0220 | 0.0013 | 6.0% |\n\n## Relative Change vs Dense (%)\n\n| Condition | PPL ↑ | ARC-c ↓ | WG ↓ | MMLU ↓ | GSM8K ↓ |\n|-----------|-------|---------|------|--------|---------|\n| KL 30% uniform | +44.1% | −30.0% | −12.1% | −37.8% | −84.9% |\n| KL 40% uniform | +36.7% | −28.3% | −14.0% | −53.0% | −91.9% |\n| KL 50% uniform | +95.5% | −43.8% | −19.4% | −57.4% | −95.7% |\n| KL 30% global | +46.7% | −31.9% | −10.1% | −61.3% | −82.0% |\n| KL 40% global | +65.4% | −29.7% | −16.3% | −41.7% | −89.7% |\n| KL 50% global | +92.8% | −43.6% | −18.7% | −57.3% | −97.4% |\n| BCE v3 50% | +268.0% | −58.8% | −35.2% | −54.0% | −90.1% |\n| TEAL 30% | +79.3% | −27.4% | −15.4% | −40.8% | −83.8% |\n| TEAL 50% | +281.1% | −51.3% | −32.1% | −56.6% | −96.0% |\n\n## Key Observations\n\n1. **KL >> BCE >> TEAL at 50% sparsity**: KL uniform achieves PPL 11.96 vs BCE 22.51 vs TEAL 23.31 (unified). KL predictor (1000 steps) dominates both iso-compute BCE (2700 steps) and training-free TEAL.\n\n2. **Uniform vs Global allocation**: At 30% sparsity, uniform preserves MMLU (0.4061 vs 0.2527, +60.7% relative) while global collapses it. At 40%, global surprisingly preserves MMLU better (0.3806 vs 0.3068) with higher PPL (10.12 vs 8.36). At 50% both collapse.\n\n3. **PPL-downstream dissociation**: KL 40% uniform has lower PPL (8.36) than KL 30% (8.82) yet worse MMLU (0.3068 vs 0.4061). PPL alone does not capture knowledge preservation; downstream metrics are essential.\n\n4. **Phase transition 30%→40%**: MMLU drops from 0.4061 to 0.3068 (−24.5pp), GSM8K from 0.0735 to 0.0394 (−3.4pp). The threshold for knowledge/reasoning retention lies between 30–40% sparsity.\n\n5. **KL 30% uniform ≈ TEAL 30% on downstream**: ARC-c (0.4078 vs 0.4232), WG (0.6859 vs 0.6606), MMLU (0.4061 vs 0.3861), GSM8K (0.0735 vs 0.0788). KL's advantage is primarily in PPL (8.82 vs 10.97, −19.6%) rather than downstream accuracy at 30% sparsity.\n\n6. **Multi-seed stability**: KL 50% uniform shows low variance across 3 seeds — PPL CV=0.64%, MMLU CV=2.3%. Results are reproducible.\n\n---\n*Generated 2026-05-16. Source: distill_sparse_swiglu registry.*\n",
      "numLines": 64,
      "startLine": 1,
      "totalLines": 64
    }
  }
}
```

</details>

---

### Assistant

_source line 28_

表格已更新完成。变更摘要：

**Main Results 表**：
- 替换 TEAL 30%/50% unified 的 "— queued" 为实际数据
- 新增 KL 40% global 行 (PPL=10.117, ARC=0.4096, WG=0.6535, MMLU=0.3806, GSM8K=0.05)
- 保留 TEAL 50% † (lm_eval) 行作为参考，标注 "retained for reference only"

**新增 Multi-seed stability 表**：3 seeds 全部 5 个指标的逐种子值 + mean/std/CV

**Relative Change 表**：新增 KL 40% global (+65.4% PPL, −41.7% MMLU)、TEAL 30% (+79.3% PPL)、TEAL 50% unified (+281.1% PPL)

**Key Observations 更新**：
- Obs 1: TEAL 数据从旧 27.97 更新为 unified 23.31
- Obs 2: 新增 40% uniform vs global 的反转现象（global MMLU 0.3806 > uniform 0.3068）
- 新增 Obs 5: KL 30% ≈ TEAL 30% 在 downstream 上差异不大，KL 优势主要在 PPL
- 新增 Obs 6: Multi-seed stability

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "f716b164-a763-4033-b921-7fe9fd43c5b1",
  "uuid": "f0c1e1d6-12ea-499d-97df-a781b7eaab39",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0145h33kauUZdGG6bhgwkFiH",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2282,
      "cache_read_input_tokens": 42257,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2282
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

### Task result

_source line 29_

表格已更新完成。变更摘要：

**Main Results 表**：
- 替换 TEAL 30%/50% unified 的 "— queued" 为实际数据
- 新增 KL 40% global 行 (PPL=10.117, ARC=0.4096, WG=0.6535, MMLU=0.3806, GSM8K=0.05)
- 保留 TEAL 50% † (lm_eval) 行作为参考，标注 "retained for reference only"

**新增 Multi-seed stability 表**：3 seeds 全部 5 个指标的逐种子值 + mean/std/CV

**Relative Change 表**：新增 KL 40% global (+65.4% PPL, −41.7% MMLU)、TEAL 30% (+79.3% PPL)、TEAL 50% unified (+281.1% PPL)

**Key Observations 更新**：
- Obs 1: TEAL 数据从旧 27.97 更新为 unified 23.31
- Obs 2: 新增 40% uniform vs global 的反转现象（global MMLU 0.3806 > uniform 0.3068）
- 新增 Obs 5: KL 30% ≈ TEAL 30% 在 downstream 上差异不大，KL 优势主要在 PPL
- 新增 Obs 6: Multi-seed stability

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "type": "result",
  "subtype": "success",
  "is_error": false,
  "api_error_status": null,
  "duration_ms": 103959,
  "duration_api_ms": 104445,
  "num_turns": 9,
  "stop_reason": "end_turn",
  "session_id": "f716b164-a763-4033-b921-7fe9fd43c5b1",
  "total_cost_usd": 0.44381000000000004,
  "usage": {
    "input_tokens": 10,
    "cache_creation_input_tokens": 32698,
    "cache_read_input_tokens": 168423,
    "output_tokens": 6139,
    "server_tool_use": {
      "web_search_requests": 0,
      "web_fetch_requests": 0
    },
    "service_tier": "standard",
    "cache_creation": {
      "ephemeral_1h_input_tokens": 32698,
      "ephemeral_5m_input_tokens": 0
    },
    "inference_geo": "",
    "iterations": [
      {
        "input_tokens": 1,
        "output_tokens": 395,
        "cache_read_input_tokens": 42257,
        "cache_creation_input_tokens": 2282,
        "cache_creation": {
          "ephemeral_5m_input_tokens": 0,
          "ephemeral_1h_input_tokens": 2282
        },
        "type": "message"
      }
    ],
    "speed": "standard"
  },
  "modelUsage": {
    "claude-haiku-4-5-20251001": {
      "inputTokens": 1636,
      "outputTokens": 15,
      "cacheReadInputTokens": 0,
      "cacheCreationInputTokens": 0,
      "webSearchRequests": 0,
      "costUSD": 0.001711,
      "contextWindow": 200000,
      "maxOutputTokens": 32000
    },
    "claude-opus-4-6": {
      "inputTokens": 10,
      "outputTokens": 6139,
      "cacheReadInputTokens": 168423,
      "cacheCreationInputTokens": 32698,
      "webSearchRequests": 0,
      "costUSD": 0.442099,
      "contextWindow": 200000,
      "maxOutputTokens": 64000
    }
  },
  "permission_denials": [],
  "terminal_reason": "completed",
  "fast_mode_state": "off",
  "uuid": "fede2714-cc6b-4ab7-a287-953c7d61d975"
}
```

</details>

---
