# analyze eval pi05 random k07 spatial seed42

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Worker execution logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 39
- **Recorded user turns:** 0
- **Tool calls:** 13
- **Original source:** `logs/workers/worker_analyze_eval_pi05_random_k07_spatial_seed42_20260521T222809.log`
- **Structured JSON:** [`79cbf77395b01bf1faa8.json`](../../sessions/79/79cbf77395b01bf1faa8.json)

## Before a recorded user message

39 recorded events

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
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress",
  "session_id": "bcd9e5e6-c86c-4bf9-9402-037b79b77b15",
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
    "mcp__agent-ml-research__compare_wandb_runs",
    "mcp__agent-ml-research__detect_image",
    "mcp__agent-ml-research__fetch_wandb_metrics",
    "mcp__agent-ml-research__fetch_wandb_run_history",
    "mcp__agent-ml-research__get_best_wandb_run",
    "mcp__agent-ml-research__kill_job",
    "mcp__agent-ml-research__list_wandb_runs",
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
  "uuid": "51afe5f2-5fa5-4770-8a70-64e7c62dcd63",
  "memory_paths": {
    "auto": "/home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-be-idea-gen-0515-2-projects-importance-margin-vla-compress/memory/"
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
    "resetsAt": 1779405000,
    "rateLimitType": "five_hour",
    "overageStatus": "rejected",
    "overageDisabledReason": "org_level_disabled",
    "isUsingOverage": false
  },
  "uuid": "8b7c3759-66b0-4ef5-a769-262a5ea6a1ad",
  "session_id": "bcd9e5e6-c86c-4bf9-9402-037b79b77b15"
}
```

---

### Assistant

_source line 4_

I'll analyze the experiment results. Let me start by reading the log and fetching W&B data in parallel.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "bcd9e5e6-c86c-4bf9-9402-037b79b77b15",
  "uuid": "b7d443fc-a147-46d9-9a8d-bf0389e01f3b",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CqqgED2VCRaVxuxxX44znz",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 11986,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 11986
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

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01SZgzWBiCdbc1XAB2RSUADW`</summary>

```json
{
  "query": "select:mcp__agent-ml-research__ssh_read_only,mcp__agent-ml-research__fetch_wandb_metrics,mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__update_registry,mcp__agent-ml-research__save_project_file,mcp__agent-ml-research__read_registry",
  "max_results": 6
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "bcd9e5e6-c86c-4bf9-9402-037b79b77b15",
  "uuid": "d896279d-942b-4c0f-bfc3-fb7958cabc00",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CqqgED2VCRaVxuxxX44znz",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 11986,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 11986
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

_source line 6 · 2026-05-21T22:28:19.794Z_

<details><summary>↩ Tool result · `toolu_01SZgzWBiCdbc1XAB2RSUADW`</summary>

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
  "tool_name": "mcp__agent-ml-research__fetch_wandb_metrics"
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
  "tool_name": "mcp__agent-ml-research__update_registry"
}
```

```json
{
  "type": "tool_reference",
  "tool_name": "mcp__agent-ml-research__save_project_file"
}
```

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
  "session_id": "bcd9e5e6-c86c-4bf9-9402-037b79b77b15",
  "uuid": "fd8ed890-f980-4df6-a151-313200d4361f",
  "tool_use_result": {
    "matches": [
      "mcp__agent-ml-research__ssh_read_only",
      "mcp__agent-ml-research__fetch_wandb_metrics",
      "mcp__agent-ml-research__read_project_file",
      "mcp__agent-ml-research__update_registry",
      "mcp__agent-ml-research__save_project_file",
      "mcp__agent-ml-research__read_registry"
    ],
    "query": "select:mcp__agent-ml-research__ssh_read_only,mcp__agent-ml-research__fetch_wandb_metrics,mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__update_registry,mcp__agent-ml-research__save_project_file,mcp__agent-ml-research__read_registry",
    "total_deferred_tools": 34
  }
}
```

</details>

---

### Assistant

_source line 7_

<details><summary>Logged reasoning block</summary>

```text
Let me read the log, fetch registry data, and read the report file in parallel.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "bcd9e5e6-c86c-4bf9-9402-037b79b77b15",
  "uuid": "537a646e-bc89-4d98-8adb-5edff5166d19",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01X8dzHXQWKBaKhpUcMHPiuQ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 2210,
      "cache_read_input_tokens": 23827,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2210
      },
      "output_tokens": 20,
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

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01X94CQoLb11k6KecKrM71Ps`</summary>

```json
{
  "server": "westd-38929",
  "command": "tail -200 ~/runs/importance_margin_vla_compress/eval_pi05_random_k07_spatial_seed42.log",
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
  "session_id": "bcd9e5e6-c86c-4bf9-9402-037b79b77b15",
  "uuid": "0ec065c3-f8a0-44e6-a3ce-a25aaebd940c",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01X8dzHXQWKBaKhpUcMHPiuQ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 2210,
      "cache_read_input_tokens": 23827,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2210
      },
      "output_tokens": 20,
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

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry · `toolu_017ZVkHPTstoZTXBuyLBLbsU`</summary>

```json
{
  "project": "importance_margin_vla_compress",
  "filters": {
    "exp_id": "eval_pi05_random_k07_spatial_seed42"
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
  "session_id": "bcd9e5e6-c86c-4bf9-9402-037b79b77b15",
  "uuid": "588c2a6b-6af0-477e-b3ac-585810f15f32",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01X8dzHXQWKBaKhpUcMHPiuQ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 2210,
      "cache_read_input_tokens": 23827,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2210
      },
      "output_tokens": 20,
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

_source line 10 · 2026-05-21T22:28:26.370Z_

<details><summary>↩ Tool result · `toolu_01X94CQoLb11k6KecKrM71Ps`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"2026-05-22 04:55:35,265 Config: suite=libero_spatial, prune=random, keep=0.7, eps=50, gpu=0\\n2026-05-22 04:55:35,265 Loading π0.5 from /root/autodl-tmp/pi05_libero_finetuned ...\\nThe PI05 model is a direct port of the OpenPI implementation. \\nThis implementation follows the original OpenPI structure for compatibility. \\nOriginal implementation: https://github.com/Physical-Intelligence/openpi\\n2026-05-22 04:57:08,796 Enabled gradient checkpointing for PI05Pytorch model\\nLoading model from: /root/autodl-tmp/pi05_libero_finetuned\\n✓ Loaded state dict from model.safetensors\\n2026-05-22 04:57:11,987 Vision embedding key might need handling: model.paligemma_with_expert.paligemma.model.vision_tower.vision_model.embeddings.patch_embedding.bias\\n2026-05-22 04:57:11,987 Vision embedding key might need handling: model.paligemma_with_expert.paligemma.model.vision_tower.vision_model.embeddings.patch_embedding.weight\\nAll keys loaded successfully!\\n2026-05-22 04:57:14,325 Patched embed_image\\n2026-05-22 04:57:14,331 Model: 4143.4M params\\n2026-05-22 04:57:14,331 Vision tokens: 256/image, 3 slots -> 768 total\\n2026-05-22 04:57:14,331 Pruning: random, keep 179/256 tokens/image (537 total)\\n2026-05-22 04:57:15,084 Preprocessor/postprocessor loaded\\n[robosuite WARNING] No private macro file found! (macros.py:53)\\n2026-05-22 04:57:15,117 No private macro file found!\\n[robosuite WARNING] It is recommended to use a private macro file (macros.py:54)\\n2026-05-22 04:57:15,117 It is recommended to use a private macro file\\n[robosuite WARNING] To setup, run: python /root/miniconda3/lib/python3.12/site-packages/robosuite/scripts/setup_macros.py (macros.py:55)\\n2026-05-22 04:57:15,117 To setup, run: python /root/miniconda3/lib/python3.12/site-packages/robosuite/scripts/setup_macros.py\\n2026-05-22 04:57:15,163 No OpenGL_accelerate module loaded: No module named 'OpenGL_accelerate'\\nGym has been unmaintained since 2022 and does not support NumPy 2.0 amongst other critical functionality.\\nPlease upgrade to Gymnasium, the maintained drop-in replacement of Gym, or contact the authors of your software and request that they upgrade.\\nSee the migration guide at https://gymnasium.farama.org/introduction/migration_guide/ for additional information.\\n[info] using task orders [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]\\n2026-05-22 04:57:15,568 Suite: libero_spatial, 10 tasks, max_steps=400\\n[PRUNE-DIAG] random: n_keep=179/256, first_indices=[1, 2, 3, 6, 7]\\n2026-05-22 04:58:29,729   T0 [pick up the black bowl between the plate] ep=10: 10/10=100%\\n2026-05-22 04:59:59,433   T0 [pick up the black bowl between the plate] ep=20: 18/20=90%\\n2026-05-22 05:01:02,318   T0 [pick up the black bowl between the plate] ep=30: 28/30=93%\\n2026-05-22 05:02:38,124   T0 [pick up the black bowl between the plate] ep=40: 37/40=92%\\n2026-05-22 05:04:01,457   T0 [pick up the black bowl between the plate] ep=50: 45/50=90%\\n2026-05-22 05:04:01,457 Task 0: SR=90.0% | Total: 45/50=90.0% | Time: 6.8min\\n2026-05-22 05:05:35,691   T1 [pick up the black bowl next to the ramek] ep=10: 9/10=90%\\n2026-05-22 05:06:55,414   T1 [pick up the black bowl next to the ramek] ep=20: 18/20=90%\\n2026-05-22 05:08:08,568   T1 [pick up the black bowl next to the ramek] ep=30: 28/30=93%\\n2026-05-22 05:09:30,687   T1 [pick up the black bowl next to the ramek] ep=40: 38/40=95%\\n2026-05-22 05:10:49,283   T1 [pick up the black bowl next to the ramek] ep=50: 48/50=96%\\n2026-05-22 05:10:49,283 Task 1: SR=96.0% | Total: 93/100=93.0% | Time: 13.6min\\n2026-05-22 05:11:54,443   T2 [pick up the black bowl from table center] ep=10: 10/10=100%\\n2026-05-22 05:12:59,144   T2 [pick up the black bowl from table center] ep=20: 20/20=100%\\n2026-05-22 05:14:01,109   T2 [pick up the black bowl from table center] ep=30: 30/30=100%\\n2026-05-22 05:15:45,331   T2 [pick up the black bowl from table center] ep=40: 37/40=92%\\n2026-05-22 05:16:50,245   T2 [pick up the black bowl from table center] ep=50: 47/50=94%\\n2026-05-22 05:16:50,245 Task 2: SR=94.0% | Total: 140/150=93.3% | Time: 19.6min\\n2026-0\\n\\n... [截断: 输出过长，省略 63 字符] ...\\n\\nx] ep=10: 5/10=50%\\n2026-05-22 05:20:50,090   T3 [pick up the black bowl on the cookie box] ep=20: 11/20=55%\\n2026-05-22 05:23:29,540   T3 [pick up the black bowl on the cookie box] ep=30: 14/30=47%\\n2026-05-22 05:25:40,319   T3 [pick up the black bowl on the cookie box] ep=40: 19/40=48%\\n2026-05-22 05:27:20,946   T3 [pick up the black bowl on the cookie box] ep=50: 26/50=52%\\n2026-05-22 05:27:20,946 Task 3: SR=52.0% | Total: 166/200=83.0% | Time: 30.1min\\n2026-05-22 05:29:46,108   T4 [pick up the black bowl in the top drawer] ep=10: 5/10=50%\\n2026-05-22 05:31:57,868   T4 [pick up the black bowl in the top drawer] ep=20: 11/20=55%\\n2026-05-22 05:34:21,815   T4 [pick up the black bowl in the top drawer] ep=30: 16/30=53%\\n2026-05-22 05:36:26,766   T4 [pick up the black bowl in the top drawer] ep=40: 23/40=57%\\n2026-05-22 05:38:25,165   T4 [pick up the black bowl in the top drawer] ep=50: 30/50=60%\\n2026-05-22 05:38:25,165 Task 4: SR=60.0% | Total: 196/250=78.4% | Time: 41.2min\\n2026-05-22 05:40:58,916   T5 [pick up the black bowl on the ramekin an] ep=10: 5/10=50%\\n2026-05-22 05:44:00,872   T5 [pick up the black bowl on the ramekin an] ep=20: 7/20=35%\\n2026-05-22 05:46:56,376   T5 [pick up the black bowl on the ramekin an] ep=30: 10/30=33%\\n2026-05-22 05:49:08,084   T5 [pick up the black bowl on the ramekin an] ep=40: 16/40=40%\\n2026-05-22 05:51:32,710   T5 [pick up the black bowl on the ramekin an] ep=50: 21/50=42%\\n2026-05-22 05:51:32,710 Task 5: SR=42.0% | Total: 217/300=72.3% | Time: 54.3min\\n2026-05-22 05:53:50,516   T6 [pick up the black bowl next to the cooki] ep=10: 5/10=50%\\n2026-05-22 05:55:26,374   T6 [pick up the black bowl next to the cooki] ep=20: 13/20=65%\\n2026-05-22 05:57:20,829   T6 [pick up the black bowl next to the cooki] ep=30: 20/30=67%\\n2026-05-22 06:00:10,324   T6 [pick up the black bowl next to the cooki] ep=40: 23/40=57%\\n2026-05-22 06:02:23,446   T6 [pick up the black bowl next to the cooki] ep=50: 29/50=58%\\n2026-05-22 06:02:23,447 Task 6: SR=58.0% | Total: 246/350=70.3% | Time: 65.1min\\n2026-05-22 06:04:19,644   T7 [pick up the black bowl on the stove and ] ep=10: 7/10=70%\\n2026-05-22 06:06:15,688   T7 [pick up the black bowl on the stove and ] ep=20: 14/20=70%\\n2026-05-22 06:07:53,317   T7 [pick up the black bowl on the stove and ] ep=30: 23/30=77%\\n2026-05-22 06:09:42,375   T7 [pick up the black bowl on the stove and ] ep=40: 31/40=78%\\n2026-05-22 06:11:49,172   T7 [pick up the black bowl on the stove and ] ep=50: 38/50=76%\\n2026-05-22 06:11:49,173 Task 7: SR=76.0% | Total: 284/400=71.0% | Time: 74.6min\\n2026-05-22 06:13:38,800   T8 [pick up the black bowl next to the plate] ep=10: 7/10=70%\\n2026-05-22 06:15:10,557   T8 [pick up the black bowl next to the plate] ep=20: 16/20=80%\\n2026-05-22 06:16:29,371   T8 [pick up the black bowl next to the plate] ep=30: 25/30=83%\\n2026-05-22 06:18:36,922   T8 [pick up the black bowl next to the plate] ep=40: 31/40=78%\\n2026-05-22 06:20:02,056   T8 [pick up the black bowl next to the plate] ep=50: 40/50=80%\\n2026-05-22 06:20:02,056 Task 8: SR=80.0% | Total: 324/450=72.0% | Time: 82.8min\\n2026-05-22 06:21:14,721   T9 [pick up the black bowl on the wooden cab] ep=10: 10/10=100%\\n2026-05-22 06:22:27,535   T9 [pick up the black bowl on the wooden cab] ep=20: 20/20=100%\\n2026-05-22 06:23:39,399   T9 [pick up the black bowl on the wooden cab] ep=30: 30/30=100%\\n2026-05-22 06:25:02,620   T9 [pick up the black bowl on the wooden cab] ep=40: 39/40=98%\\n2026-05-22 06:26:26,260   T9 [pick up the black bowl on the wooden cab] ep=50: 48/50=96%\\n2026-05-22 06:26:26,260 Task 9: SR=96.0% | Total: 372/500=74.4% | Time: 89.2min\\n2026-05-22 06:26:26,469 \\n============================================================\\n2026-05-22 06:26:26,470 RESULT: libero_spatial prune=random keep=0.7 SR=74.4%\\n2026-05-22 06:26:26,470 Saved: /root/autodl-tmp/importance_margin_vla_compress/eval_results/pi05_random_k0.70_libero_spatial_seed42.json\\n2026-05-22 06:26:26,470 ============================================================\\nEXIT_CODE=0\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.11}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "bcd9e5e6-c86c-4bf9-9402-037b79b77b15",
  "uuid": "4c44ee79-0f8c-4d0b-8e96-3a8d9af562b1",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"2026-05-22 04:55:35,265 Config: suite=libero_spatial, prune=random, keep=0.7, eps=50, gpu=0\\\\n2026-05-22 04:55:35,265 Loading π0.5 from /root/autodl-tmp/pi05_libero_finetuned ...\\\\nThe PI05 model is a direct port of the OpenPI implementation. \\\\nThis implementation follows the original OpenPI structure for compatibility. \\\\nOriginal implementation: https://github.com/Physical-Intelligence/openpi\\\\n2026-05-22 04:57:08,796 Enabled gradient checkpointing for PI05Pytorch model\\\\nLoading model from: /root/autodl-tmp/pi05_libero_finetuned\\\\n✓ Loaded state dict from model.safetensors\\\\n2026-05-22 04:57:11,987 Vision embedding key might need handling: model.paligemma_with_expert.paligemma.model.vision_tower.vision_model.embeddings.patch_embedding.bias\\\\n2026-05-22 04:57:11,987 Vision embedding key might need handling: model.paligemma_with_expert.paligemma.model.vision_tower.vision_model.embeddings.patch_embedding.weight\\\\nAll keys loaded successfully!\\\\n2026-05-22 04:57:14,325 Patched embed_image\\\\n2026-05-22 04:57:14,331 Model: 4143.4M params\\\\n2026-05-22 04:57:14,331 Vision tokens: 256/image, 3 slots -> 768 total\\\\n2026-05-22 04:57:14,331 Pruning: random, keep 179/256 tokens/image (537 total)\\\\n2026-05-22 04:57:15,084 Preprocessor/postprocessor loaded\\\\n[robosuite WARNING] No private macro file found! (macros.py:53)\\\\n2026-05-22 04:57:15,117 No private macro file found!\\\\n[robosuite WARNING] It is recommended to use a private macro file (macros.py:54)\\\\n2026-05-22 04:57:15,117 It is recommended to use a private macro file\\\\n[robosuite WARNING] To setup, run: python /root/miniconda3/lib/python3.12/site-packages/robosuite/scripts/setup_macros.py (macros.py:55)\\\\n2026-05-22 04:57:15,117 To setup, run: python /root/miniconda3/lib/python3.12/site-packages/robosuite/scripts/setup_macros.py\\\\n2026-05-22 04:57:15,163 No OpenGL_accelerate module loaded: No module named 'OpenGL_accelerate'\\\\nGym has been unmaintained since 2022 and does not support NumPy 2.0 amongst other critical functionality.\\\\nPlease upgrade to Gymnasium, the maintained drop-in replacement of Gym, or contact the authors of your software and request that they upgrade.\\\\nSee the migration guide at https://gymnasium.farama.org/introduction/migration_guide/ for additional information.\\\\n[info] using task orders [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]\\\\n2026-05-22 04:57:15,568 Suite: libero_spatial, 10 tasks, max_steps=400\\\\n[PRUNE-DIAG] random: n_keep=179/256, first_indices=[1, 2, 3, 6, 7]\\\\n2026-05-22 04:58:29,729   T0 [pick up the black bowl between the plate] ep=10: 10/10=100%\\\\n2026-05-22 04:59:59,433   T0 [pick up the black bowl between the plate] ep=20: 18/20=90%\\\\n2026-05-22 05:01:02,318   T0 [pick up the black bowl between the plate] ep=30: 28/30=93%\\\\n2026-05-22 05:02:38,124   T0 [pick up the black bowl between the plate] ep=40: 37/40=92%\\\\n2026-05-22 05:04:01,457   T0 [pick up the black bowl between the plate] ep=50: 45/50=90%\\\\n2026-05-22 05:04:01,457 Task 0: SR=90.0% | Total: 45/50=90.0% | Time: 6.8min\\\\n2026-05-22 05:05:35,691   T1 [pick up the black bowl next to the ramek] ep=10: 9/10=90%\\\\n2026-05-22 05:06:55,414   T1 [pick up the black bowl next to the ramek] ep=20: 18/20=90%\\\\n2026-05-22 05:08:08,568   T1 [pick up the black bowl next to the ramek] ep=30: 28/30=93%\\\\n2026-05-22 05:09:30,687   T1 [pick up the black bowl next to the ramek] ep=40: 38/40=95%\\\\n2026-05-22 05:10:49,283   T1 [pick up the black bowl next to the ramek] ep=50: 48/50=96%\\\\n2026-05-22 05:10:49,283 Task 1: SR=96.0% | Total: 93/100=93.0% | Time: 13.6min\\\\n2026-05-22 05:11:54,443   T2 [pick up the black bowl from table center] ep=10: 10/10=100%\\\\n2026-05-22 05:12:59,144   T2 [pick up the black bowl from table center] ep=20: 20/20=100%\\\\n2026-05-22 05:14:01,109   T2 [pick up the black bowl from table center] ep=30: 30/30=100%\\\\n2026-05-22 05:15:45,331   T2 [pick up the black bowl from table center] ep=40: 37/40=92%\\\\n2026-05-22 05:16:50,245   T2 [pick up the black bowl from table center] ep=50: 47/50=94%\\\\n2026-05-22 05:16:50,245 Task 2: SR=94.0% | Total: 140/150=93.3% | Time: 19.6min\\\\n2026-0\\\\n\\\\n... [截断: 输出过长，省略 63 字符] ...\\\\n\\\\nx] ep=10: 5/10=50%\\\\n2026-05-22 05:20:50,090   T3 [pick up the black bowl on the cookie box] ep=20: 11/20=55%\\\\n2026-05-22 05:23:29,540   T3 [pick up the black bowl on the cookie box] ep=30: 14/30=47%\\\\n2026-05-22 05:25:40,319   T3 [pick up the black bowl on the cookie box] ep=40: 19/40=48%\\\\n2026-05-22 05:27:20,946   T3 [pick up the black bowl on the cookie box] ep=50: 26/50=52%\\\\n2026-05-22 05:27:20,946 Task 3: SR=52.0% | Total: 166/200=83.0% | Time: 30.1min\\\\n2026-05-22 05:29:46,108   T4 [pick up the black bowl in the top drawer] ep=10: 5/10=50%\\\\n2026-05-22 05:31:57,868   T4 [pick up the black bowl in the top drawer] ep=20: 11/20=55%\\\\n2026-05-22 05:34:21,815   T4 [pick up the black bowl in the top drawer] ep=30: 16/30=53%\\\\n2026-05-22 05:36:26,766   T4 [pick up the black bowl in the top drawer] ep=40: 23/40=57%\\\\n2026-05-22 05:38:25,165   T4 [pick up the black bowl in the top drawer] ep=50: 30/50=60%\\\\n2026-05-22 05:38:25,165 Task 4: SR=60.0% | Total: 196/250=78.4% | Time: 41.2min\\\\n2026-05-22 05:40:58,916   T5 [pick up the black bowl on the ramekin an] ep=10: 5/10=50%\\\\n2026-05-22 05:44:00,872   T5 [pick up the black bowl on the ramekin an] ep=20: 7/20=35%\\\\n2026-05-22 05:46:56,376   T5 [pick up the black bowl on the ramekin an] ep=30: 10/30=33%\\\\n2026-05-22 05:49:08,084   T5 [pick up the black bowl on the ramekin an] ep=40: 16/40=40%\\\\n2026-05-22 05:51:32,710   T5 [pick up the black bowl on the ramekin an] ep=50: 21/50=42%\\\\n2026-05-22 05:51:32,710 Task 5: SR=42.0% | Total: 217/300=72.3% | Time: 54.3min\\\\n2026-05-22 05:53:50,516   T6 [pick up the black bowl next to the cooki] ep=10: 5/10=50%\\\\n2026-05-22 05:55:26,374   T6 [pick up the black bowl next to the cooki] ep=20: 13/20=65%\\\\n2026-05-22 05:57:20,829   T6 [pick up the black bowl next to the cooki] ep=30: 20/30=67%\\\\n2026-05-22 06:00:10,324   T6 [pick up the black bowl next to the cooki] ep=40: 23/40=57%\\\\n2026-05-22 06:02:23,446   T6 [pick up the black bowl next to the cooki] ep=50: 29/50=58%\\\\n2026-05-22 06:02:23,447 Task 6: SR=58.0% | Total: 246/350=70.3% | Time: 65.1min\\\\n2026-05-22 06:04:19,644   T7 [pick up the black bowl on the stove and ] ep=10: 7/10=70%\\\\n2026-05-22 06:06:15,688   T7 [pick up the black bowl on the stove and ] ep=20: 14/20=70%\\\\n2026-05-22 06:07:53,317   T7 [pick up the black bowl on the stove and ] ep=30: 23/30=77%\\\\n2026-05-22 06:09:42,375   T7 [pick up the black bowl on the stove and ] ep=40: 31/40=78%\\\\n2026-05-22 06:11:49,172   T7 [pick up the black bowl on the stove and ] ep=50: 38/50=76%\\\\n2026-05-22 06:11:49,173 Task 7: SR=76.0% | Total: 284/400=71.0% | Time: 74.6min\\\\n2026-05-22 06:13:38,800   T8 [pick up the black bowl next to the plate] ep=10: 7/10=70%\\\\n2026-05-22 06:15:10,557   T8 [pick up the black bowl next to the plate] ep=20: 16/20=80%\\\\n2026-05-22 06:16:29,371   T8 [pick up the black bowl next to the plate] ep=30: 25/30=83%\\\\n2026-05-22 06:18:36,922   T8 [pick up the black bowl next to the plate] ep=40: 31/40=78%\\\\n2026-05-22 06:20:02,056   T8 [pick up the black bowl next to the plate] ep=50: 40/50=80%\\\\n2026-05-22 06:20:02,056 Task 8: SR=80.0% | Total: 324/450=72.0% | Time: 82.8min\\\\n2026-05-22 06:21:14,721   T9 [pick up the black bowl on the wooden cab] ep=10: 10/10=100%\\\\n2026-05-22 06:22:27,535   T9 [pick up the black bowl on the wooden cab] ep=20: 20/20=100%\\\\n2026-05-22 06:23:39,399   T9 [pick up the black bowl on the wooden cab] ep=30: 30/30=100%\\\\n2026-05-22 06:25:02,620   T9 [pick up the black bowl on the wooden cab] ep=40: 39/40=98%\\\\n2026-05-22 06:26:26,260   T9 [pick up the black bowl on the wooden cab] ep=50: 48/50=96%\\\\n2026-05-22 06:26:26,260 Task 9: SR=96.0% | Total: 372/500=74.4% | Time: 89.2min\\\\n2026-05-22 06:26:26,469 \\\\n============================================================\\\\n2026-05-22 06:26:26,470 RESULT: libero_spatial prune=random keep=0.7 SR=74.4%\\\\n2026-05-22 06:26:26,470 Saved: /root/autodl-tmp/importance_margin_vla_compress/eval_results/pi05_random_k0.70_libero_spatial_seed42.json\\\\n2026-05-22 06:26:26,470 ============================================================\\\\nEXIT_CODE=0\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 1.11}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"2026-05-22 04:55:35,265 Config: suite=libero_spatial, prune=random, keep=0.7, eps=50, gpu=0\\n2026-05-22 04:55:35,265 Loading π0.5 from /root/autodl-tmp/pi05_libero_finetuned ...\\nThe PI05 model is a direct port of the OpenPI implementation. \\nThis implementation follows the original OpenPI structure for compatibility. \\nOriginal implementation: https://github.com/Physical-Intelligence/openpi\\n2026-05-22 04:57:08,796 Enabled gradient checkpointing for PI05Pytorch model\\nLoading model from: /root/autodl-tmp/pi05_libero_finetuned\\n✓ Loaded state dict from model.safetensors\\n2026-05-22 04:57:11,987 Vision embedding key might need handling: model.paligemma_with_expert.paligemma.model.vision_tower.vision_model.embeddings.patch_embedding.bias\\n2026-05-22 04:57:11,987 Vision embedding key might need handling: model.paligemma_with_expert.paligemma.model.vision_tower.vision_model.embeddings.patch_embedding.weight\\nAll keys loaded successfully!\\n2026-05-22 04:57:14,325 Patched embed_image\\n2026-05-22 04:57:14,331 Model: 4143.4M params\\n2026-05-22 04:57:14,331 Vision tokens: 256/image, 3 slots -> 768 total\\n2026-05-22 04:57:14,331 Pruning: random, keep 179/256 tokens/image (537 total)\\n2026-05-22 04:57:15,084 Preprocessor/postprocessor loaded\\n[robosuite WARNING] No private macro file found! (macros.py:53)\\n2026-05-22 04:57:15,117 No private macro file found!\\n[robosuite WARNING] It is recommended to use a private macro file (macros.py:54)\\n2026-05-22 04:57:15,117 It is recommended to use a private macro file\\n[robosuite WARNING] To setup, run: python /root/miniconda3/lib/python3.12/site-packages/robosuite/scripts/setup_macros.py (macros.py:55)\\n2026-05-22 04:57:15,117 To setup, run: python /root/miniconda3/lib/python3.12/site-packages/robosuite/scripts/setup_macros.py\\n2026-05-22 04:57:15,163 No OpenGL_accelerate module loaded: No module named 'OpenGL_accelerate'\\nGym has been unmaintained since 2022 and does not support NumPy 2.0 amongst other critical functionality.\\nPlease upgrade to Gymnasium, the maintained drop-in replacement of Gym, or contact the authors of your software and request that they upgrade.\\nSee the migration guide at https://gymnasium.farama.org/introduction/migration_guide/ for additional information.\\n[info] using task orders [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]\\n2026-05-22 04:57:15,568 Suite: libero_spatial, 10 tasks, max_steps=400\\n[PRUNE-DIAG] random: n_keep=179/256, first_indices=[1, 2, 3, 6, 7]\\n2026-05-22 04:58:29,729   T0 [pick up the black bowl between the plate] ep=10: 10/10=100%\\n2026-05-22 04:59:59,433   T0 [pick up the black bowl between the plate] ep=20: 18/20=90%\\n2026-05-22 05:01:02,318   T0 [pick up the black bowl between the plate] ep=30: 28/30=93%\\n2026-05-22 05:02:38,124   T0 [pick up the black bowl between the plate] ep=40: 37/40=92%\\n2026-05-22 05:04:01,457   T0 [pick up the black bowl between the plate] ep=50: 45/50=90%\\n2026-05-22 05:04:01,457 Task 0: SR=90.0% | Total: 45/50=90.0% | Time: 6.8min\\n2026-05-22 05:05:35,691   T1 [pick up the black bowl next to the ramek] ep=10: 9/10=90%\\n2026-05-22 05:06:55,414   T1 [pick up the black bowl next to the ramek] ep=20: 18/20=90%\\n2026-05-22 05:08:08,568   T1 [pick up the black bowl next to the ramek] ep=30: 28/30=93%\\n2026-05-22 05:09:30,687   T1 [pick up the black bowl next to the ramek] ep=40: 38/40=95%\\n2026-05-22 05:10:49,283   T1 [pick up the black bowl next to the ramek] ep=50: 48/50=96%\\n2026-05-22 05:10:49,283 Task 1: SR=96.0% | Total: 93/100=93.0% | Time: 13.6min\\n2026-05-22 05:11:54,443   T2 [pick up the black bowl from table center] ep=10: 10/10=100%\\n2026-05-22 05:12:59,144   T2 [pick up the black bowl from table center] ep=20: 20/20=100%\\n2026-05-22 05:14:01,109   T2 [pick up the black bowl from table center] ep=30: 30/30=100%\\n2026-05-22 05:15:45,331   T2 [pick up the black bowl from table center] ep=40: 37/40=92%\\n2026-05-22 05:16:50,245   T2 [pick up the black bowl from table center] ep=50: 47/50=94%\\n2026-05-22 05:16:50,245 Task 2: SR=94.0% | Total: 140/150=93.3% | Time: 19.6min\\n2026-0\\n\\n... [截断: 输出过长，省略 63 字符] ...\\n\\nx] ep=10: 5/10=50%\\n2026-05-22 05:20:50,090   T3 [pick up the black bowl on the cookie box] ep=20: 11/20=55%\\n2026-05-22 05:23:29,540   T3 [pick up the black bowl on the cookie box] ep=30: 14/30=47%\\n2026-05-22 05:25:40,319   T3 [pick up the black bowl on the cookie box] ep=40: 19/40=48%\\n2026-05-22 05:27:20,946   T3 [pick up the black bowl on the cookie box] ep=50: 26/50=52%\\n2026-05-22 05:27:20,946 Task 3: SR=52.0% | Total: 166/200=83.0% | Time: 30.1min\\n2026-05-22 05:29:46,108   T4 [pick up the black bowl in the top drawer] ep=10: 5/10=50%\\n2026-05-22 05:31:57,868   T4 [pick up the black bowl in the top drawer] ep=20: 11/20=55%\\n2026-05-22 05:34:21,815   T4 [pick up the black bowl in the top drawer] ep=30: 16/30=53%\\n2026-05-22 05:36:26,766   T4 [pick up the black bowl in the top drawer] ep=40: 23/40=57%\\n2026-05-22 05:38:25,165   T4 [pick up the black bowl in the top drawer] ep=50: 30/50=60%\\n2026-05-22 05:38:25,165 Task 4: SR=60.0% | Total: 196/250=78.4% | Time: 41.2min\\n2026-05-22 05:40:58,916   T5 [pick up the black bowl on the ramekin an] ep=10: 5/10=50%\\n2026-05-22 05:44:00,872   T5 [pick up the black bowl on the ramekin an] ep=20: 7/20=35%\\n2026-05-22 05:46:56,376   T5 [pick up the black bowl on the ramekin an] ep=30: 10/30=33%\\n2026-05-22 05:49:08,084   T5 [pick up the black bowl on the ramekin an] ep=40: 16/40=40%\\n2026-05-22 05:51:32,710   T5 [pick up the black bowl on the ramekin an] ep=50: 21/50=42%\\n2026-05-22 05:51:32,710 Task 5: SR=42.0% | Total: 217/300=72.3% | Time: 54.3min\\n2026-05-22 05:53:50,516   T6 [pick up the black bowl next to the cooki] ep=10: 5/10=50%\\n2026-05-22 05:55:26,374   T6 [pick up the black bowl next to the cooki] ep=20: 13/20=65%\\n2026-05-22 05:57:20,829   T6 [pick up the black bowl next to the cooki] ep=30: 20/30=67%\\n2026-05-22 06:00:10,324   T6 [pick up the black bowl next to the cooki] ep=40: 23/40=57%\\n2026-05-22 06:02:23,446   T6 [pick up the black bowl next to the cooki] ep=50: 29/50=58%\\n2026-05-22 06:02:23,447 Task 6: SR=58.0% | Total: 246/350=70.3% | Time: 65.1min\\n2026-05-22 06:04:19,644   T7 [pick up the black bowl on the stove and ] ep=10: 7/10=70%\\n2026-05-22 06:06:15,688   T7 [pick up the black bowl on the stove and ] ep=20: 14/20=70%\\n2026-05-22 06:07:53,317   T7 [pick up the black bowl on the stove and ] ep=30: 23/30=77%\\n2026-05-22 06:09:42,375   T7 [pick up the black bowl on the stove and ] ep=40: 31/40=78%\\n2026-05-22 06:11:49,172   T7 [pick up the black bowl on the stove and ] ep=50: 38/50=76%\\n2026-05-22 06:11:49,173 Task 7: SR=76.0% | Total: 284/400=71.0% | Time: 74.6min\\n2026-05-22 06:13:38,800   T8 [pick up the black bowl next to the plate] ep=10: 7/10=70%\\n2026-05-22 06:15:10,557   T8 [pick up the black bowl next to the plate] ep=20: 16/20=80%\\n2026-05-22 06:16:29,371   T8 [pick up the black bowl next to the plate] ep=30: 25/30=83%\\n2026-05-22 06:18:36,922   T8 [pick up the black bowl next to the plate] ep=40: 31/40=78%\\n2026-05-22 06:20:02,056   T8 [pick up the black bowl next to the plate] ep=50: 40/50=80%\\n2026-05-22 06:20:02,056 Task 8: SR=80.0% | Total: 324/450=72.0% | Time: 82.8min\\n2026-05-22 06:21:14,721   T9 [pick up the black bowl on the wooden cab] ep=10: 10/10=100%\\n2026-05-22 06:22:27,535   T9 [pick up the black bowl on the wooden cab] ep=20: 20/20=100%\\n2026-05-22 06:23:39,399   T9 [pick up the black bowl on the wooden cab] ep=30: 30/30=100%\\n2026-05-22 06:25:02,620   T9 [pick up the black bowl on the wooden cab] ep=40: 39/40=98%\\n2026-05-22 06:26:26,260   T9 [pick up the black bowl on the wooden cab] ep=50: 48/50=96%\\n2026-05-22 06:26:26,260 Task 9: SR=96.0% | Total: 372/500=74.4% | Time: 89.2min\\n2026-05-22 06:26:26,469 \\n============================================================\\n2026-05-22 06:26:26,470 RESULT: libero_spatial prune=random keep=0.7 SR=74.4%\\n2026-05-22 06:26:26,470 Saved: /root/autodl-tmp/importance_margin_vla_compress/eval_results/pi05_random_k0.70_libero_spatial_seed42.json\\n2026-05-22 06:26:26,470 ============================================================\\nEXIT_CODE=0\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.11}}"
    }
  }
}
```

</details>

---

### Tool result

_source line 11 · 2026-05-21T22:28:27.114Z_

<details><summary>↩ Tool result · `toolu_017ZVkHPTstoZTXBuyLBLbsU`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"experiments\": {}, \"count\": 0, \"total\": 0, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.7339}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "bcd9e5e6-c86c-4bf9-9402-037b79b77b15",
  "uuid": "319adc8d-1c6e-410a-8019-d2a70cd35228",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"experiments\\\": {}, \\\"count\\\": 0, \\\"total\\\": 0, \\\"baseline\\\": null}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.7339}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"experiments\": {}, \"count\": 0, \"total\": 0, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.7339}}"
    }
  }
}
```

</details>

---

### Tool call

_source line 12_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_016oBo9Dkxf6a4xRmVBJK7XJ`</summary>

```json
{
  "project": "importance_margin_vla_compress",
  "file": "report.md",
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
  "session_id": "bcd9e5e6-c86c-4bf9-9402-037b79b77b15",
  "uuid": "ccb38b8c-7d42-4d9d-9da5-1b6b367301cc",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01X8dzHXQWKBaKhpUcMHPiuQ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 2210,
      "cache_read_input_tokens": 23827,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2210
      },
      "output_tokens": 20,
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

_source line 13 · 2026-05-21T22:28:27.204Z_

<details><summary>↩ Tool result · `toolu_016oBo9Dkxf6a4xRmVBJK7XJ`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/report.md\", \"content\": \"&lt;!-- AUTO-FACTS-BEGIN (generated 2026-05-21T22:26:57Z; do not edit — regenerated by auto_build_report_facts) -->\\n## 📊 当前状态（auto-derived from registry）\\n\\n**总计**: 330 个实验 — ANALYZING 9, DONE 287, PREPARING 23, RUNNING 11\\n**DONE 分布**: failed 47, killed 22, negative 27, success 191\\n\\n### GPU 占用\\n- **分配**: 14 张 — westd-27271:cuda:0, westd-27271:cuda:1, cqa1-33015:cuda:0, cqa1-33015:cuda:1, cqa1-33015:cuda:2, cqa1-33015:cuda:3, westd-41074:cuda:0, westd-41074:cuda:1, westd-41074:cuda:2, westd-41074:cuda:3, westd-38929:cuda:0, westd-38929:cuda:1, westd-38929:cuda:2, westd-38929:cuda:3\\n- **实际运行**: 4 张 — westd-27271:cuda:1(train_openvla_sc_m32_vtconly_seed42), westd-41074:cuda:2(train_openvla_sc_m96_seed42_v3), westd-38929:cuda:0(eval_pi05_random_k03_spatial_seed42), westd-38929:cuda:1(eval_pi05_l2norm_k07_spatial_seed42)\\n- **空闲（分配了没跑）**: cqa1-33015:cuda:0, westd-41074:cuda:1, westd-41074:cuda:3, westd-38929:cuda:3\\n\\n### 💾 磁盘余量\\n- **westd-27271**:\\n  - `/autodl-pub`: 5.3T/7.3T 可用（已用 24%）\\n  - `/init`: 150M/150M 可用（已用 1%）\\n  - `/usr/bin/nvidia-smi`: 819G/879G 可用（已用 2%）\\n- **cqa1-33015**:\\n  - `/autodl-pub`: 595G/7.0T 可用（已用 92%） ⚠️\\n  - `/autodl-pub/data`: 1.5T/4.0T 可用（已用 65%）\\n  - `/usr/bin/nvidia-smi`: 818G/879G 可用（已用 2%）\\n- **westd-41074**:\\n  - `/autodl-pub`: 5.3T/7.3T 可用（已用 24%）\\n  - `/init`: 150M/150M 可用（已用 0%）\\n  - `/usr/bin/nvidia-smi`: 812G/879G 可用（已用 3%）\\n- **westd-38929**:\\n  - `/autodl-pub`: 5.3T/7.3T 可用（已用 24%）\\n  - `/init`: 150M/150M 可用（已用 1%）\\n  - `/usr/bin/nvidia-smi`: 645G/879G 可用（已用 23%）\\n\\n### 🏃 RUNNING\\n| exp_id | server | gpu | pid | log |\\n|--------|--------|-----|-----|-----|\\n| `train_openvla_sc_m32_vtconly_seed42` | westd-27271 | cuda:1 | 921279 | `…in_vla_compress/logs/train_openvla_sc_m32_seed42_resume.log` |\\n| `train_openvla_sc_m96_seed42_v3` | westd-41074 | cuda:2 | 68539 | `—` |\\n| `train_openvla_sc_m64_seed42_v6` | westd-41074 | ? | 59671 | `—` |\\n| `eval_pi05_random_k03_spatial_seed42` | westd-38929 | cuda:0 | 788113 | `…margin_vla_compress/eval_pi05_random_k03_spatial_seed42.log` |\\n| `eval_pi05_random_k085_object_seed42_v2` | westd-38929 | ? | 824147 | `/tmp/eval_pi05_random_k085_object_seed42_v2.log` |\\n| `eval_pi05_l2norm_k07_spatial_seed42` | westd-38929 | cuda:1 | ? | `—` |\\n| `eval_pi05_l2norm_k085_object_seed42` | cqa1-33015 | ? | ? | `—` |\\n| `eval_pi05_random_k03_object_seed43` | cqa1-33015 | ? | ? | `—` |\\n| `eval_pi05_random_k0925_object_seed42` | westd-41074 | ? | ? | `—` |\\n| `eval_pi05_random_k085_object_seed43` | cqa1-33015 | ? | 719435 | `…oot/autodl-tmp/logs/eval_pi05_random_k085_object_seed43.log` |\\n| `eval_pi05_random_k095_object_seed43` | westd-41074 | ? | ? | `—` |\\n\\n### 📌 最近完成 (top 5)\\n- `eval_openvla_random_k05_object_seed42` [success] — 2026-05-21T22:19:26\\n- `eval_openvla_random_k07_object_seed42_v2` [success] — 2026-05-21T22:16:17\\n- `eval_openvla_random_k09_object_seed42` [killed] — 2026-05-21T22:16:10\\n- `eval_pi05_l2norm_k03_object_seed43` [success] — 2026-05-21T22:09:26\\n- `eval_openvla_l2norm_k09_object_seed42` [success] — 2026-05-21T22:07:51\\n\\n### 🔴 最近失败原因 (top 3)\\n- `eval_openvla_random_k09_object_seed42`: _(no failure_reason — pre-2026-04-24 entry)_\\n\\n&lt;!-- AUTO-FACTS-END -->\\n\\n---\\n\\n# Handover — 2026-05-21\\n\\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\\n\\n## 运行中\\n| exp_id | 假设 | 状态 | 关键指标 | W&B |\\n|--------|------|------|---------|-----|\\n| eval_pi05_random_k095_object_seed43 | π0.5 random k=0.95 Object seed43: V-dip 入口点 seed 验证。seed42=69.4%。dual-seed 给论文 figure 加 error bar。 | — | — | — |\\n| eval_pi05_random_k085_object_seed43 | π0.5 random k=0.85 Object seed43: seed 验证。seed42 v2 正在 westd-38929 跑（早期数据 ~8% SR）。如果 seed43 也崩→确认 cliff 在 k=0.7-0.85 之间。 | — | — | — |\\n| eval_pi05_random_k03_object_seed43 | π0.5 random k=0.3 Object seed43: seed 验证，seed42=36.4%。确认 random k=0.3 的 SR 在 seed 间可重复。 | — | — | — |\\n\\n## 待处理\\n- eval_oft_baseline_goal_seed42（准备中）\\n- eval_oft_object_std_v3（准备中）\\n- eval_oft_object_nolora_v2（准备中）\\n- eval_openvla_sc_m64_50k_seed42（准备中）\\n- openvla-spatial-maxsteps600-quick（准备中）\\n- openvla-spatial-maxsteps600-test（准备中）\\n- eval_openvla_prune_random_k03_seed42: OpenVLA random pruning k=0.3 seed42 provides 3rd seed for MF-3 validation at 70% pruning. seed7=20.6%. Auto-queued by Director to start when current seed42 batch completes.（准备中）\\n- eval_openvla_prune_seed43_sweep: OpenVLA-OFT random pruning seed=43 sweep (k=0.7, k=0.5) to verify reproducibility of seed=7 results. If seed43 results match seed=7 (k=0.7→49%, k=0.5→37.4%), confirms graded degradation pattern is robust across seeds.（准备中）\\n- eval_openvla_prune_l2norm_sweep: OpenVLA L2 norm pruning eval (k=0.7/0.5/0.3) on LIBERO-Object. Unifies pruning method with X-VLA (both use L2 norm-based token selection). L2NormPruningHook: after projector output, sort vision tokens by L2 norm, keep top-k highest norm tokens (true removal, spatial order preserved). If L2 norm curve differs significantly from random removal curve (k=0.7: 49%, k=0.5: 37.4%, k=0.3: 20.6%), demonstrates importance-aware pruning matters for MLP projector.（准备中）\\n- analysis_smolvla_importance_cv: SmolVLA (pixel-shuffle connector) token importance CV analysis. D103 verification: if SmolVLA CV is low like π0 (0.038), entropy+CV cannot distinguish compressible/non-compressible; if high, CV is a useful predictor of connector behavior.（准备中）\\n- …另有 13 项\\n\\n## 近期结论\\n- **eval_openvla_random_k05_object_seed42** (success): OpenVLA random k=0.5 Object seed42 (新脚本，D125 env.seed 已修复): 补全 OpenVLA random 曲线。已知 random k=0.9=62.9%(3-seed), k=0.7=44.4%。L2norm k=0.5=39.2%。CV=0.215 中等，预期 random 与 L2norm 接近或略低。 ← 基于 eval_openvla_l2norm_k05_object_seed42_v2\\n- **eval_openvla_random_k07_object_seed42_v2** (success): OpenVLA random k=0.7 Object seed42 (新脚本): 与 L2norm k=0.7(49.8%) 配对对比。CV=0.215 中等，验证 L2norm vs random 在 k=0.7 下的选择优势。用修复后的脚本重跑。\\n- **eval_openvla_random_k09_object_seed42** (killed): OpenVLA random k=0.9 Object seed42: 与 L2norm k=0.9(70.6%) 配对对比。CV=0.215（中等），如果 random 也接近 70% → 中等 CV 下 method indifferent；如果明显更低 → 中等 CV 下 L2norm 仍有选择优势。与 π0.5(CV=0.055) 的极端分化(98.2% vs 10.8%)对比。 ← 基于 eval_openvla_l2norm_k09_object_seed42\\n\\n## 趋势\\n成功 194 / 负向 27 / 失败 47 / 共 290\\ntotal_episodes: 500 →（近 3 次 success）\\n\\n## 下一步\\n（无活跃 idea，请通过 ideas.md 添加）\\n\\n## 资源状态\\ncqa1-33015: 无 GPU 信息\\nwestd-27271: 无 GPU 信息\\nwestd-38929: 无 GPU 信息\\nwestd-41074: 无 GPU 信息\\n\\n## 告警\\n- mvp_baseline: 训练失败 — unknown\\n- mvp_imm_anchor: 训练失败 — unknown\\n- mvp_baseline_v2: 训练失败 — unknown\\n- mvp_imm_anchor_v2: 训练失败 — unknown\\n- mvp_baseline_v3: 训练失败 — unknown\\n- mvp_imm_anchor_v4: 训练失败 — unknown\\n- mvp_baseline_v4: 已被终止 — unknown\\n- mvp_imm_anchor_v5: 训练失败 — unknown\\n- mvp_imm_anchor_v6: 训练失败 — unknown\\n- mvp_imm_anchor_v7: 训练失败 — unknown\\n- mvp_imm_anchor_v7_1: 训练失败 — unknown\\n- plan_008_pruning_sweep: 训练失败 — unknown\\n- libero_imm_twostage_v1: 已被终止 — unknown\\n- libero_fullft_batch64: 训练失败 — unknown\\n- eval_k07_bypass_v2: 训练失败 — unknown\\n- eval_stage1only_spatial: 已被终止 — unknown\\n- libero_fullft_batch64_v2: 已被终止 — unknown\\n- train_acis_stage1only_k03: 训练失败 — unknown\\n- eval_openvla_pruning_k03: 已被终止 — unknown\\n- train_smart_compress_m128: 训练失败 — unknown\\n- train_baseline_control_100k: 训练失败 — unknown\\n- eval_official_smolvla_pruning: 训练失败 — unknown\\n- eval_acis_k05_supplement_200eps: 训练失败 — unknown\\n- eval_smart_compress_m96_seed43: 训练失败 — unknown\\n- train_smart_compress_m16_seed44: 训练失败 — unknown\\n- eval_smolvla_prune_k05_spatial: 训练失败 — unknown\\n- eval_smolvla_official_baseline_spatial: 训练失败 — unknown\\n- eval_official_smolvla_prune_k05_spatial: 训练失败 — unknown\\n- train_smart_compress_m16_seed44_v2: 训练失败 — unknown\\n- train_openvla_sc_m128_seed42: 训练失败 — unknown\\n- train_openvla_sc_m128_lora_seed42: 已被终止 — unknown\\n- train_openvla_sc_m128_seed42_v2: 已被终止 — unknown\\n- train_openvla_sc_m128_vtconly_seed42: 已被终止 — unknown\\n- train_c5_roboflamingo_libero_object: 已被终止 — unknown\\n- train_c5_roboflamingo_v2: 已被终止 — unknown\\n- train_openvla_sc_m96_vtconly_seed42: 训练失败 — unknown\\n- train_openvla_sc_m64_vtconly_seed42: 训练失败 — unknown\\n- train_openvla_sc_m64_seed42_v3: 训练失败 — unknown\\n- eval_openvla_sc_m128_vtconly_20k_seed42: 已被终止 — unknown\\n- eval_oft_baseline_k10: 训练失败 — unknown\\n- eval_openvla_prune_random_k07_seed43: 训练失败 — unknown\\n- eval_openvla_prune_random_k05_seed43: 训练失败 — unknown\\n- eval_openvla_prune_l2norm_k07_seed43: 训练失败 — unknown\\n- eval_openvla_prune_random_k095_seed42: 已被终止 — unknown\\n- eval_openvla_prune_random_k07_seed42: 已被终止 — unknown\\n- eval_openvla_prune_random_k03_seed43: 已被终止 — unknown\\n- eval_openvla_prune_l2norm_k09_seed43: 已被终止 — unknown\\n- eval_openvla_sc_m128_spatial_seed42: 训练失败 — unknown\\n- eval_openvla_baseline_spatial_seed42_v2: 训练失败 — unknown\\n- eval_smolvla_baseline_spatial_seed42: 训练失败 — unknown\\n- eval_oft_baseline_object_seed42: 已被终止 — unknown\\n- eval_oft_baseline_object_seed42_v2: 训练失败 — unknown\\n- train_openvla_sc_m64_seed42_v4: 训练失败 — unknown\\n- eval_openvla_sc_m128_object_seed42: 训练失败 — unknown\\n- eval_openvla_random_k03_object_seed42: 训练失败 — unknown\\n- eval_openvla_l2norm_k07_object_seed42: 训练失败 — unknown\\n- eval_xvla_random_k07_object_seed43: 训练失败 — unknown\\n- eval_openvla_sc_m128_object_seed42_v2: 训练失败 — unknown\\n- eval_openvla_random_k07_object_seed42: 训练失败 — unknown\\n- eval_openvla_l2norm_k05_object_seed42_v3: 已被终止 — unknown\\n- train_openvla_sc_m64_seed42_v5: 训练失败 — unknown\\n- eval_pi05_random_k07_object_seed42_v2: 已被终止 — unknown\\n- eval_pi05_random_k07_object_seed42_v3: 已被终止 — unknown\\n- eval_xvla_l2norm_k085_object_seed43: 已被终止 — unknown\\n- eval_xvla_l2norm_k03_object_seed42_v2: 已被终止 — unknown\\n- eval_pi05_random_k095_object_seed42: 训练失败 — unknown\\n- eval_pi05_random_k085_object_seed42: 训练失败 — unknown\\n- eval_pi05_random_k09_fixedmask_object_seed42: 训练失败 — unknown\\n- eval_openvla_random_k09_object_seed42: 已被终止 — unknown\\n\", \"total_chars\": 9602, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "bcd9e5e6-c86c-4bf9-9402-037b79b77b15",
  "uuid": "db3d05a3-6919-41c2-be18-3121d0aaea17",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"path\\\": \\\"/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/report.md\\\", \\\"content\\\": \\\"&lt;!-- AUTO-FACTS-BEGIN (generated 2026-05-21T22:26:57Z; do not edit — regenerated by auto_build_report_facts) -->\\\\n## 📊 当前状态（auto-derived from registry）\\\\n\\\\n**总计**: 330 个实验 — ANALYZING 9, DONE 287, PREPARING 23, RUNNING 11\\\\n**DONE 分布**: failed 47, killed 22, negative 27, success 191\\\\n\\\\n### GPU 占用\\\\n- **分配**: 14 张 — westd-27271:cuda:0, westd-27271:cuda:1, cqa1-33015:cuda:0, cqa1-33015:cuda:1, cqa1-33015:cuda:2, cqa1-33015:cuda:3, westd-41074:cuda:0, westd-41074:cuda:1, westd-41074:cuda:2, westd-41074:cuda:3, westd-38929:cuda:0, westd-38929:cuda:1, westd-38929:cuda:2, westd-38929:cuda:3\\\\n- **实际运行**: 4 张 — westd-27271:cuda:1(train_openvla_sc_m32_vtconly_seed42), westd-41074:cuda:2(train_openvla_sc_m96_seed42_v3), westd-38929:cuda:0(eval_pi05_random_k03_spatial_seed42), westd-38929:cuda:1(eval_pi05_l2norm_k07_spatial_seed42)\\\\n- **空闲（分配了没跑）**: cqa1-33015:cuda:0, westd-41074:cuda:1, westd-41074:cuda:3, westd-38929:cuda:3\\\\n\\\\n### 💾 磁盘余量\\\\n- **westd-27271**:\\\\n  - `/autodl-pub`: 5.3T/7.3T 可用（已用 24%）\\\\n  - `/init`: 150M/150M 可用（已用 1%）\\\\n  - `/usr/bin/nvidia-smi`: 819G/879G 可用（已用 2%）\\\\n- **cqa1-33015**:\\\\n  - `/autodl-pub`: 595G/7.0T 可用（已用 92%） ⚠️\\\\n  - `/autodl-pub/data`: 1.5T/4.0T 可用（已用 65%）\\\\n  - `/usr/bin/nvidia-smi`: 818G/879G 可用（已用 2%）\\\\n- **westd-41074**:\\\\n  - `/autodl-pub`: 5.3T/7.3T 可用（已用 24%）\\\\n  - `/init`: 150M/150M 可用（已用 0%）\\\\n  - `/usr/bin/nvidia-smi`: 812G/879G 可用（已用 3%）\\\\n- **westd-38929**:\\\\n  - `/autodl-pub`: 5.3T/7.3T 可用（已用 24%）\\\\n  - `/init`: 150M/150M 可用（已用 1%）\\\\n  - `/usr/bin/nvidia-smi`: 645G/879G 可用（已用 23%）\\\\n\\\\n### 🏃 RUNNING\\\\n| exp_id | server | gpu | pid | log |\\\\n|--------|--------|-----|-----|-----|\\\\n| `train_openvla_sc_m32_vtconly_seed42` | westd-27271 | cuda:1 | 921279 | `…in_vla_compress/logs/train_openvla_sc_m32_seed42_resume.log` |\\\\n| `train_openvla_sc_m96_seed42_v3` | westd-41074 | cuda:2 | 68539 | `—` |\\\\n| `train_openvla_sc_m64_seed42_v6` | westd-41074 | ? | 59671 | `—` |\\\\n| `eval_pi05_random_k03_spatial_seed42` | westd-38929 | cuda:0 | 788113 | `…margin_vla_compress/eval_pi05_random_k03_spatial_seed42.log` |\\\\n| `eval_pi05_random_k085_object_seed42_v2` | westd-38929 | ? | 824147 | `/tmp/eval_pi05_random_k085_object_seed42_v2.log` |\\\\n| `eval_pi05_l2norm_k07_spatial_seed42` | westd-38929 | cuda:1 | ? | `—` |\\\\n| `eval_pi05_l2norm_k085_object_seed42` | cqa1-33015 | ? | ? | `—` |\\\\n| `eval_pi05_random_k03_object_seed43` | cqa1-33015 | ? | ? | `—` |\\\\n| `eval_pi05_random_k0925_object_seed42` | westd-41074 | ? | ? | `—` |\\\\n| `eval_pi05_random_k085_object_seed43` | cqa1-33015 | ? | 719435 | `…oot/autodl-tmp/logs/eval_pi05_random_k085_object_seed43.log` |\\\\n| `eval_pi05_random_k095_object_seed43` | westd-41074 | ? | ? | `—` |\\\\n\\\\n### 📌 最近完成 (top 5)\\\\n- `eval_openvla_random_k05_object_seed42` [success] — 2026-05-21T22:19:26\\\\n- `eval_openvla_random_k07_object_seed42_v2` [success] — 2026-05-21T22:16:17\\\\n- `eval_openvla_random_k09_object_seed42` [killed] — 2026-05-21T22:16:10\\\\n- `eval_pi05_l2norm_k03_object_seed43` [success] — 2026-05-21T22:09:26\\\\n- `eval_openvla_l2norm_k09_object_seed42` [success] — 2026-05-21T22:07:51\\\\n\\\\n### 🔴 最近失败原因 (top 3)\\\\n- `eval_openvla_random_k09_object_seed42`: _(no failure_reason — pre-2026-04-24 entry)_\\\\n\\\\n&lt;!-- AUTO-FACTS-END -->\\\\n\\\\n---\\\\n\\\\n# Handover — 2026-05-21\\\\n\\\\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\\\\n\\\\n## 运行中\\\\n| exp_id | 假设 | 状态 | 关键指标 | W&B |\\\\n|--------|------|------|---------|-----|\\\\n| eval_pi05_random_k095_object_seed43 | π0.5 random k=0.95 Object seed43: V-dip 入口点 seed 验证。seed42=69.4%。dual-seed 给论文 figure 加 error bar。 | — | — | — |\\\\n| eval_pi05_random_k085_object_seed43 | π0.5 random k=0.85 Object seed43: seed 验证。seed42 v2 正在 westd-38929 跑（早期数据 ~8% SR）。如果 seed43 也崩→确认 cliff 在 k=0.7-0.85 之间。 | — | — | — |\\\\n| eval_pi05_random_k03_object_seed43 | π0.5 random k=0.3 Object seed43: seed 验证，seed42=36.4%。确认 random k=0.3 的 SR 在 seed 间可重复。 | — | — | — |\\\\n\\\\n## 待处理\\\\n- eval_oft_baseline_goal_seed42（准备中）\\\\n- eval_oft_object_std_v3（准备中）\\\\n- eval_oft_object_nolora_v2（准备中）\\\\n- eval_openvla_sc_m64_50k_seed42（准备中）\\\\n- openvla-spatial-maxsteps600-quick（准备中）\\\\n- openvla-spatial-maxsteps600-test（准备中）\\\\n- eval_openvla_prune_random_k03_seed42: OpenVLA random pruning k=0.3 seed42 provides 3rd seed for MF-3 validation at 70% pruning. seed7=20.6%. Auto-queued by Director to start when current seed42 batch completes.（准备中）\\\\n- eval_openvla_prune_seed43_sweep: OpenVLA-OFT random pruning seed=43 sweep (k=0.7, k=0.5) to verify reproducibility of seed=7 results. If seed43 results match seed=7 (k=0.7→49%, k=0.5→37.4%), confirms graded degradation pattern is robust across seeds.（准备中）\\\\n- eval_openvla_prune_l2norm_sweep: OpenVLA L2 norm pruning eval (k=0.7/0.5/0.3) on LIBERO-Object. Unifies pruning method with X-VLA (both use L2 norm-based token selection). L2NormPruningHook: after projector output, sort vision tokens by L2 norm, keep top-k highest norm tokens (true removal, spatial order preserved). If L2 norm curve differs significantly from random removal curve (k=0.7: 49%, k=0.5: 37.4%, k=0.3: 20.6%), demonstrates importance-aware pruning matters for MLP projector.（准备中）\\\\n- analysis_smolvla_importance_cv: SmolVLA (pixel-shuffle connector) token importance CV analysis. D103 verification: if SmolVLA CV is low like π0 (0.038), entropy+CV cannot distinguish compressible/non-compressible; if high, CV is a useful predictor of connector behavior.（准备中）\\\\n- …另有 13 项\\\\n\\\\n## 近期结论\\\\n- **eval_openvla_random_k05_object_seed42** (success): OpenVLA random k=0.5 Object seed42 (新脚本，D125 env.seed 已修复): 补全 OpenVLA random 曲线。已知 random k=0.9=62.9%(3-seed), k=0.7=44.4%。L2norm k=0.5=39.2%。CV=0.215 中等，预期 random 与 L2norm 接近或略低。 ← 基于 eval_openvla_l2norm_k05_object_seed42_v2\\\\n- **eval_openvla_random_k07_object_seed42_v2** (success): OpenVLA random k=0.7 Object seed42 (新脚本): 与 L2norm k=0.7(49.8%) 配对对比。CV=0.215 中等，验证 L2norm vs random 在 k=0.7 下的选择优势。用修复后的脚本重跑。\\\\n- **eval_openvla_random_k09_object_seed42** (killed): OpenVLA random k=0.9 Object seed42: 与 L2norm k=0.9(70.6%) 配对对比。CV=0.215（中等），如果 random 也接近 70% → 中等 CV 下 method indifferent；如果明显更低 → 中等 CV 下 L2norm 仍有选择优势。与 π0.5(CV=0.055) 的极端分化(98.2% vs 10.8%)对比。 ← 基于 eval_openvla_l2norm_k09_object_seed42\\\\n\\\\n## 趋势\\\\n成功 194 / 负向 27 / 失败 47 / 共 290\\\\ntotal_episodes: 500 →（近 3 次 success）\\\\n\\\\n## 下一步\\\\n（无活跃 idea，请通过 ideas.md 添加）\\\\n\\\\n## 资源状态\\\\ncqa1-33015: 无 GPU 信息\\\\nwestd-27271: 无 GPU 信息\\\\nwestd-38929: 无 GPU 信息\\\\nwestd-41074: 无 GPU 信息\\\\n\\\\n## 告警\\\\n- mvp_baseline: 训练失败 — unknown\\\\n- mvp_imm_anchor: 训练失败 — unknown\\\\n- mvp_baseline_v2: 训练失败 — unknown\\\\n- mvp_imm_anchor_v2: 训练失败 — unknown\\\\n- mvp_baseline_v3: 训练失败 — unknown\\\\n- mvp_imm_anchor_v4: 训练失败 — unknown\\\\n- mvp_baseline_v4: 已被终止 — unknown\\\\n- mvp_imm_anchor_v5: 训练失败 — unknown\\\\n- mvp_imm_anchor_v6: 训练失败 — unknown\\\\n- mvp_imm_anchor_v7: 训练失败 — unknown\\\\n- mvp_imm_anchor_v7_1: 训练失败 — unknown\\\\n- plan_008_pruning_sweep: 训练失败 — unknown\\\\n- libero_imm_twostage_v1: 已被终止 — unknown\\\\n- libero_fullft_batch64: 训练失败 — unknown\\\\n- eval_k07_bypass_v2: 训练失败 — unknown\\\\n- eval_stage1only_spatial: 已被终止 — unknown\\\\n- libero_fullft_batch64_v2: 已被终止 — unknown\\\\n- train_acis_stage1only_k03: 训练失败 — unknown\\\\n- eval_openvla_pruning_k03: 已被终止 — unknown\\\\n- train_smart_compress_m128: 训练失败 — unknown\\\\n- train_baseline_control_100k: 训练失败 — unknown\\\\n- eval_official_smolvla_pruning: 训练失败 — unknown\\\\n- eval_acis_k05_supplement_200eps: 训练失败 — unknown\\\\n- eval_smart_compress_m96_seed43: 训练失败 — unknown\\\\n- train_smart_compress_m16_seed44: 训练失败 — unknown\\\\n- eval_smolvla_prune_k05_spatial: 训练失败 — unknown\\\\n- eval_smolvla_official_baseline_spatial: 训练失败 — unknown\\\\n- eval_official_smolvla_prune_k05_spatial: 训练失败 — unknown\\\\n- train_smart_compress_m16_seed44_v2: 训练失败 — unknown\\\\n- train_openvla_sc_m128_seed42: 训练失败 — unknown\\\\n- train_openvla_sc_m128_lora_seed42: 已被终止 — unknown\\\\n- train_openvla_sc_m128_seed42_v2: 已被终止 — unknown\\\\n- train_openvla_sc_m128_vtconly_seed42: 已被终止 — unknown\\\\n- train_c5_roboflamingo_libero_object: 已被终止 — unknown\\\\n- train_c5_roboflamingo_v2: 已被终止 — unknown\\\\n- train_openvla_sc_m96_vtconly_seed42: 训练失败 — unknown\\\\n- train_openvla_sc_m64_vtconly_seed42: 训练失败 — unknown\\\\n- train_openvla_sc_m64_seed42_v3: 训练失败 — unknown\\\\n- eval_openvla_sc_m128_vtconly_20k_seed42: 已被终止 — unknown\\\\n- eval_oft_baseline_k10: 训练失败 — unknown\\\\n- eval_openvla_prune_random_k07_seed43: 训练失败 — unknown\\\\n- eval_openvla_prune_random_k05_seed43: 训练失败 — unknown\\\\n- eval_openvla_prune_l2norm_k07_seed43: 训练失败 — unknown\\\\n- eval_openvla_prune_random_k095_seed42: 已被终止 — unknown\\\\n- eval_openvla_prune_random_k07_seed42: 已被终止 — unknown\\\\n- eval_openvla_prune_random_k03_seed43: 已被终止 — unknown\\\\n- eval_openvla_prune_l2norm_k09_seed43: 已被终止 — unknown\\\\n- eval_openvla_sc_m128_spatial_seed42: 训练失败 — unknown\\\\n- eval_openvla_baseline_spatial_seed42_v2: 训练失败 — unknown\\\\n- eval_smolvla_baseline_spatial_seed42: 训练失败 — unknown\\\\n- eval_oft_baseline_object_seed42: 已被终止 — unknown\\\\n- eval_oft_baseline_object_seed42_v2: 训练失败 — unknown\\\\n- train_openvla_sc_m64_seed42_v4: 训练失败 — unknown\\\\n- eval_openvla_sc_m128_object_seed42: 训练失败 — unknown\\\\n- eval_openvla_random_k03_object_seed42: 训练失败 — unknown\\\\n- eval_openvla_l2norm_k07_object_seed42: 训练失败 — unknown\\\\n- eval_xvla_random_k07_object_seed43: 训练失败 — unknown\\\\n- eval_openvla_sc_m128_object_seed42_v2: 训练失败 — unknown\\\\n- eval_openvla_random_k07_object_seed42: 训练失败 — unknown\\\\n- eval_openvla_l2norm_k05_object_seed42_v3: 已被终止 — unknown\\\\n- train_openvla_sc_m64_seed42_v5: 训练失败 — unknown\\\\n- eval_pi05_random_k07_object_seed42_v2: 已被终止 — unknown\\\\n- eval_pi05_random_k07_object_seed42_v3: 已被终止 — unknown\\\\n- eval_xvla_l2norm_k085_object_seed43: 已被终止 — unknown\\\\n- eval_xvla_l2norm_k03_object_seed42_v2: 已被终止 — unknown\\\\n- eval_pi05_random_k095_object_seed42: 训练失败 — unknown\\\\n- eval_pi05_random_k085_object_seed42: 训练失败 — unknown\\\\n- eval_pi05_random_k09_fixedmask_object_seed42: 训练失败 — unknown\\\\n- eval_openvla_random_k09_object_seed42: 已被终止 — unknown\\\\n\\\", \\\"total_chars\\\": 9602, \\\"truncated\\\": false}, \\\"error\\\": null, \\\"metadata\\\": {}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/report.md\", \"content\": \"&lt;!-- AUTO-FACTS-BEGIN (generated 2026-05-21T22:26:57Z; do not edit — regenerated by auto_build_report_facts) -->\\n## 📊 当前状态（auto-derived from registry）\\n\\n**总计**: 330 个实验 — ANALYZING 9, DONE 287, PREPARING 23, RUNNING 11\\n**DONE 分布**: failed 47, killed 22, negative 27, success 191\\n\\n### GPU 占用\\n- **分配**: 14 张 — westd-27271:cuda:0, westd-27271:cuda:1, cqa1-33015:cuda:0, cqa1-33015:cuda:1, cqa1-33015:cuda:2, cqa1-33015:cuda:3, westd-41074:cuda:0, westd-41074:cuda:1, westd-41074:cuda:2, westd-41074:cuda:3, westd-38929:cuda:0, westd-38929:cuda:1, westd-38929:cuda:2, westd-38929:cuda:3\\n- **实际运行**: 4 张 — westd-27271:cuda:1(train_openvla_sc_m32_vtconly_seed42), westd-41074:cuda:2(train_openvla_sc_m96_seed42_v3), westd-38929:cuda:0(eval_pi05_random_k03_spatial_seed42), westd-38929:cuda:1(eval_pi05_l2norm_k07_spatial_seed42)\\n- **空闲（分配了没跑）**: cqa1-33015:cuda:0, westd-41074:cuda:1, westd-41074:cuda:3, westd-38929:cuda:3\\n\\n### 💾 磁盘余量\\n- **westd-27271**:\\n  - `/autodl-pub`: 5.3T/7.3T 可用（已用 24%）\\n  - `/init`: 150M/150M 可用（已用 1%）\\n  - `/usr/bin/nvidia-smi`: 819G/879G 可用（已用 2%）\\n- **cqa1-33015**:\\n  - `/autodl-pub`: 595G/7.0T 可用（已用 92%） ⚠️\\n  - `/autodl-pub/data`: 1.5T/4.0T 可用（已用 65%）\\n  - `/usr/bin/nvidia-smi`: 818G/879G 可用（已用 2%）\\n- **westd-41074**:\\n  - `/autodl-pub`: 5.3T/7.3T 可用（已用 24%）\\n  - `/init`: 150M/150M 可用（已用 0%）\\n  - `/usr/bin/nvidia-smi`: 812G/879G 可用（已用 3%）\\n- **westd-38929**:\\n  - `/autodl-pub`: 5.3T/7.3T 可用（已用 24%）\\n  - `/init`: 150M/150M 可用（已用 1%）\\n  - `/usr/bin/nvidia-smi`: 645G/879G 可用（已用 23%）\\n\\n### 🏃 RUNNING\\n| exp_id | server | gpu | pid | log |\\n|--------|--------|-----|-----|-----|\\n| `train_openvla_sc_m32_vtconly_seed42` | westd-27271 | cuda:1 | 921279 | `…in_vla_compress/logs/train_openvla_sc_m32_seed42_resume.log` |\\n| `train_openvla_sc_m96_seed42_v3` | westd-41074 | cuda:2 | 68539 | `—` |\\n| `train_openvla_sc_m64_seed42_v6` | westd-41074 | ? | 59671 | `—` |\\n| `eval_pi05_random_k03_spatial_seed42` | westd-38929 | cuda:0 | 788113 | `…margin_vla_compress/eval_pi05_random_k03_spatial_seed42.log` |\\n| `eval_pi05_random_k085_object_seed42_v2` | westd-38929 | ? | 824147 | `/tmp/eval_pi05_random_k085_object_seed42_v2.log` |\\n| `eval_pi05_l2norm_k07_spatial_seed42` | westd-38929 | cuda:1 | ? | `—` |\\n| `eval_pi05_l2norm_k085_object_seed42` | cqa1-33015 | ? | ? | `—` |\\n| `eval_pi05_random_k03_object_seed43` | cqa1-33015 | ? | ? | `—` |\\n| `eval_pi05_random_k0925_object_seed42` | westd-41074 | ? | ? | `—` |\\n| `eval_pi05_random_k085_object_seed43` | cqa1-33015 | ? | 719435 | `…oot/autodl-tmp/logs/eval_pi05_random_k085_object_seed43.log` |\\n| `eval_pi05_random_k095_object_seed43` | westd-41074 | ? | ? | `—` |\\n\\n### 📌 最近完成 (top 5)\\n- `eval_openvla_random_k05_object_seed42` [success] — 2026-05-21T22:19:26\\n- `eval_openvla_random_k07_object_seed42_v2` [success] — 2026-05-21T22:16:17\\n- `eval_openvla_random_k09_object_seed42` [killed] — 2026-05-21T22:16:10\\n- `eval_pi05_l2norm_k03_object_seed43` [success] — 2026-05-21T22:09:26\\n- `eval_openvla_l2norm_k09_object_seed42` [success] — 2026-05-21T22:07:51\\n\\n### 🔴 最近失败原因 (top 3)\\n- `eval_openvla_random_k09_object_seed42`: _(no failure_reason — pre-2026-04-24 entry)_\\n\\n&lt;!-- AUTO-FACTS-END -->\\n\\n---\\n\\n# Handover — 2026-05-21\\n\\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\\n\\n## 运行中\\n| exp_id | 假设 | 状态 | 关键指标 | W&B |\\n|--------|------|------|---------|-----|\\n| eval_pi05_random_k095_object_seed43 | π0.5 random k=0.95 Object seed43: V-dip 入口点 seed 验证。seed42=69.4%。dual-seed 给论文 figure 加 error bar。 | — | — | — |\\n| eval_pi05_random_k085_object_seed43 | π0.5 random k=0.85 Object seed43: seed 验证。seed42 v2 正在 westd-38929 跑（早期数据 ~8% SR）。如果 seed43 也崩→确认 cliff 在 k=0.7-0.85 之间。 | — | — | — |\\n| eval_pi05_random_k03_object_seed43 | π0.5 random k=0.3 Object seed43: seed 验证，seed42=36.4%。确认 random k=0.3 的 SR 在 seed 间可重复。 | — | — | — |\\n\\n## 待处理\\n- eval_oft_baseline_goal_seed42（准备中）\\n- eval_oft_object_std_v3（准备中）\\n- eval_oft_object_nolora_v2（准备中）\\n- eval_openvla_sc_m64_50k_seed42（准备中）\\n- openvla-spatial-maxsteps600-quick（准备中）\\n- openvla-spatial-maxsteps600-test（准备中）\\n- eval_openvla_prune_random_k03_seed42: OpenVLA random pruning k=0.3 seed42 provides 3rd seed for MF-3 validation at 70% pruning. seed7=20.6%. Auto-queued by Director to start when current seed42 batch completes.（准备中）\\n- eval_openvla_prune_seed43_sweep: OpenVLA-OFT random pruning seed=43 sweep (k=0.7, k=0.5) to verify reproducibility of seed=7 results. If seed43 results match seed=7 (k=0.7→49%, k=0.5→37.4%), confirms graded degradation pattern is robust across seeds.（准备中）\\n- eval_openvla_prune_l2norm_sweep: OpenVLA L2 norm pruning eval (k=0.7/0.5/0.3) on LIBERO-Object. Unifies pruning method with X-VLA (both use L2 norm-based token selection). L2NormPruningHook: after projector output, sort vision tokens by L2 norm, keep top-k highest norm tokens (true removal, spatial order preserved). If L2 norm curve differs significantly from random removal curve (k=0.7: 49%, k=0.5: 37.4%, k=0.3: 20.6%), demonstrates importance-aware pruning matters for MLP projector.（准备中）\\n- analysis_smolvla_importance_cv: SmolVLA (pixel-shuffle connector) token importance CV analysis. D103 verification: if SmolVLA CV is low like π0 (0.038), entropy+CV cannot distinguish compressible/non-compressible; if high, CV is a useful predictor of connector behavior.（准备中）\\n- …另有 13 项\\n\\n## 近期结论\\n- **eval_openvla_random_k05_object_seed42** (success): OpenVLA random k=0.5 Object seed42 (新脚本，D125 env.seed 已修复): 补全 OpenVLA random 曲线。已知 random k=0.9=62.9%(3-seed), k=0.7=44.4%。L2norm k=0.5=39.2%。CV=0.215 中等，预期 random 与 L2norm 接近或略低。 ← 基于 eval_openvla_l2norm_k05_object_seed42_v2\\n- **eval_openvla_random_k07_object_seed42_v2** (success): OpenVLA random k=0.7 Object seed42 (新脚本): 与 L2norm k=0.7(49.8%) 配对对比。CV=0.215 中等，验证 L2norm vs random 在 k=0.7 下的选择优势。用修复后的脚本重跑。\\n- **eval_openvla_random_k09_object_seed42** (killed): OpenVLA random k=0.9 Object seed42: 与 L2norm k=0.9(70.6%) 配对对比。CV=0.215（中等），如果 random 也接近 70% → 中等 CV 下 method indifferent；如果明显更低 → 中等 CV 下 L2norm 仍有选择优势。与 π0.5(CV=0.055) 的极端分化(98.2% vs 10.8%)对比。 ← 基于 eval_openvla_l2norm_k09_object_seed42\\n\\n## 趋势\\n成功 194 / 负向 27 / 失败 47 / 共 290\\ntotal_episodes: 500 →（近 3 次 success）\\n\\n## 下一步\\n（无活跃 idea，请通过 ideas.md 添加）\\n\\n## 资源状态\\ncqa1-33015: 无 GPU 信息\\nwestd-27271: 无 GPU 信息\\nwestd-38929: 无 GPU 信息\\nwestd-41074: 无 GPU 信息\\n\\n## 告警\\n- mvp_baseline: 训练失败 — unknown\\n- mvp_imm_anchor: 训练失败 — unknown\\n- mvp_baseline_v2: 训练失败 — unknown\\n- mvp_imm_anchor_v2: 训练失败 — unknown\\n- mvp_baseline_v3: 训练失败 — unknown\\n- mvp_imm_anchor_v4: 训练失败 — unknown\\n- mvp_baseline_v4: 已被终止 — unknown\\n- mvp_imm_anchor_v5: 训练失败 — unknown\\n- mvp_imm_anchor_v6: 训练失败 — unknown\\n- mvp_imm_anchor_v7: 训练失败 — unknown\\n- mvp_imm_anchor_v7_1: 训练失败 — unknown\\n- plan_008_pruning_sweep: 训练失败 — unknown\\n- libero_imm_twostage_v1: 已被终止 — unknown\\n- libero_fullft_batch64: 训练失败 — unknown\\n- eval_k07_bypass_v2: 训练失败 — unknown\\n- eval_stage1only_spatial: 已被终止 — unknown\\n- libero_fullft_batch64_v2: 已被终止 — unknown\\n- train_acis_stage1only_k03: 训练失败 — unknown\\n- eval_openvla_pruning_k03: 已被终止 — unknown\\n- train_smart_compress_m128: 训练失败 — unknown\\n- train_baseline_control_100k: 训练失败 — unknown\\n- eval_official_smolvla_pruning: 训练失败 — unknown\\n- eval_acis_k05_supplement_200eps: 训练失败 — unknown\\n- eval_smart_compress_m96_seed43: 训练失败 — unknown\\n- train_smart_compress_m16_seed44: 训练失败 — unknown\\n- eval_smolvla_prune_k05_spatial: 训练失败 — unknown\\n- eval_smolvla_official_baseline_spatial: 训练失败 — unknown\\n- eval_official_smolvla_prune_k05_spatial: 训练失败 — unknown\\n- train_smart_compress_m16_seed44_v2: 训练失败 — unknown\\n- train_openvla_sc_m128_seed42: 训练失败 — unknown\\n- train_openvla_sc_m128_lora_seed42: 已被终止 — unknown\\n- train_openvla_sc_m128_seed42_v2: 已被终止 — unknown\\n- train_openvla_sc_m128_vtconly_seed42: 已被终止 — unknown\\n- train_c5_roboflamingo_libero_object: 已被终止 — unknown\\n- train_c5_roboflamingo_v2: 已被终止 — unknown\\n- train_openvla_sc_m96_vtconly_seed42: 训练失败 — unknown\\n- train_openvla_sc_m64_vtconly_seed42: 训练失败 — unknown\\n- train_openvla_sc_m64_seed42_v3: 训练失败 — unknown\\n- eval_openvla_sc_m128_vtconly_20k_seed42: 已被终止 — unknown\\n- eval_oft_baseline_k10: 训练失败 — unknown\\n- eval_openvla_prune_random_k07_seed43: 训练失败 — unknown\\n- eval_openvla_prune_random_k05_seed43: 训练失败 — unknown\\n- eval_openvla_prune_l2norm_k07_seed43: 训练失败 — unknown\\n- eval_openvla_prune_random_k095_seed42: 已被终止 — unknown\\n- eval_openvla_prune_random_k07_seed42: 已被终止 — unknown\\n- eval_openvla_prune_random_k03_seed43: 已被终止 — unknown\\n- eval_openvla_prune_l2norm_k09_seed43: 已被终止 — unknown\\n- eval_openvla_sc_m128_spatial_seed42: 训练失败 — unknown\\n- eval_openvla_baseline_spatial_seed42_v2: 训练失败 — unknown\\n- eval_smolvla_baseline_spatial_seed42: 训练失败 — unknown\\n- eval_oft_baseline_object_seed42: 已被终止 — unknown\\n- eval_oft_baseline_object_seed42_v2: 训练失败 — unknown\\n- train_openvla_sc_m64_seed42_v4: 训练失败 — unknown\\n- eval_openvla_sc_m128_object_seed42: 训练失败 — unknown\\n- eval_openvla_random_k03_object_seed42: 训练失败 — unknown\\n- eval_openvla_l2norm_k07_object_seed42: 训练失败 — unknown\\n- eval_xvla_random_k07_object_seed43: 训练失败 — unknown\\n- eval_openvla_sc_m128_object_seed42_v2: 训练失败 — unknown\\n- eval_openvla_random_k07_object_seed42: 训练失败 — unknown\\n- eval_openvla_l2norm_k05_object_seed42_v3: 已被终止 — unknown\\n- train_openvla_sc_m64_seed42_v5: 训练失败 — unknown\\n- eval_pi05_random_k07_object_seed42_v2: 已被终止 — unknown\\n- eval_pi05_random_k07_object_seed42_v3: 已被终止 — unknown\\n- eval_xvla_l2norm_k085_object_seed43: 已被终止 — unknown\\n- eval_xvla_l2norm_k03_object_seed42_v2: 已被终止 — unknown\\n- eval_pi05_random_k095_object_seed42: 训练失败 — unknown\\n- eval_pi05_random_k085_object_seed42: 训练失败 — unknown\\n- eval_pi05_random_k09_fixedmask_object_seed42: 训练失败 — unknown\\n- eval_openvla_random_k09_object_seed42: 已被终止 — unknown\\n\", \"total_chars\": 9602, \"truncated\": false}, \"error\": null, \"metadata\": {}}"
    }
  }
}
```

</details>

---

### Assistant

_source line 14_

<details><summary>Logged reasoning block</summary>

```text
Good, I have all the data I need. Let me summarize the results:

**Experiment: eval_pi05_random_k07_spatial_seed42**

Log results:
- Suite: libero_spatial, 10 tasks, 50 episodes each = 500 total
- Pruning: random, keep 179/256 tokens/image (k=0.7)
- Overall SR: 74.4% (372/500)
- All 500 episodes completed, EXIT_CODE=0, no errors

Per-task results:
- T0: pick up the black bowl between the plate — 45/50 = 90.0%


- T1: pick up the black bowl next to the ramekin — 48/50 = 96.0%
- T2: pick up the black bowl from table center — 47/50 = 94.0%
- T3: pick up the black bowl on the cookie box — 26/50 = 52.0%
- T4: pick up the black bowl in the top drawer — 30/50 = 60.0%
- T5: pick up the black bowl on the ramekin — 21/50 = 42.0%
- T6 and beyond are still loading...

Looking at the performance metrics across these tasks, I notice the random approach with k=0.7 is outperforming the L2norm variant by about 22 percentage points, which is a significant gap. The registry doesn't have this experiment recorded yet, so I'll move forward with the analysis I can do.

For the spatial suite, random k=0.7 achieves 74.4%, but I'm still waiting on the L2norm spatial result to complete the comparison—that experiment is currently running on the cluster. Once that finishes, I'll be able to verify whether the random advantage holds consistently across both object and spatial suites. I'm noticing the random method at k=0.7 shows a slight dip from 77.2% to 74.4% when moving from Object to Spatial suite, while L2norm scored 55.0% on Object. I need to update the registry with this completed experiment, but since the L2norm Spatial result isn't ready yet, I can't fully validate the cross-suite consistency hypothesis—though the random result is holding reasonably well so far.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "bcd9e5e6-c86c-4bf9-9402-037b79b77b15",
  "uuid": "e0d429c1-3443-4b97-829a-d122d876863b",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018wgsK9ggcHA4H5wDiQgJPp",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 9391,
      "cache_read_input_tokens": 26037,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 9391
      },
      "output_tokens": 10,
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

_source line 15_

实验已完成，500 episodes 全部跑完，无报错。Overall SR = **74.4%**。

Per-task results:

| Task | Description | SR |
|------|-------------|-----|
| T0 | pick up the black bowl between the plate | 90.0% |
| T1 | pick up the black bowl next to the ramekin | 96.0% |
| T2 | pick up the black bowl from table center | 94.0% |
| T3 | pick up the black bowl on the cookie box | 52.0% |
| T4 | pick up the black bowl in the top drawer | 60.0% |
| T5 | pick up the black bowl on the ramekin and... | 42.0% |
| T6 | pick up the black bowl next to the cookie... | 58.0% |
| T7 | pick up the black bowl on the stove and... | 76.0% |
| T8 | pick up the black bowl next to the plate | 80.0% |
| T9 | pick up the black bowl on the wooden cab... | 96.0% |

`eval_pi05_l2norm_k07_spatial_seed42` 仍在 westd-38929:cuda:1 运行中，完整的 cross-suite 对比需要等它完成。

现在更新 registry。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "bcd9e5e6-c86c-4bf9-9402-037b79b77b15",
  "uuid": "4e10adb0-8f76-46fa-938f-d86478d4707b",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018wgsK9ggcHA4H5wDiQgJPp",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 9391,
      "cache_read_input_tokens": 26037,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 9391
      },
      "output_tokens": 10,
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

_source line 16_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry · `toolu_01T9TkYqhWpaZY5J3ecjevsf`</summary>

```json
{
  "exp_id": "eval_pi05_random_k07_spatial_seed42",
  "field": "status",
  "value": "DONE",
  "project": "importance_margin_vla_compress",
  "spec": {
    "command": "eval_pi05_random_k07_spatial_seed42",
    "server": "westd-38929",
    "data_path": "libero_spatial",
    "data_count": 500,
    "model_name": "pi05",
    "seed": 42,
    "eval_data": "libero_spatial",
    "checkpoint_source": "/root/autodl-tmp/pi05_libero_finetuned",
    "checkpoint_path": "/root/autodl-tmp/pi05_libero_finetuned",
    "log_path": "~/runs/importance_margin_vla_compress/eval_pi05_random_k07_spatial_seed42.log"
  }
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "bcd9e5e6-c86c-4bf9-9402-037b79b77b15",
  "uuid": "0fdbb985-a88c-42da-a553-52fe844eb8cd",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018wgsK9ggcHA4H5wDiQgJPp",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 9391,
      "cache_read_input_tokens": 26037,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 9391
      },
      "output_tokens": 10,
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

_source line 17 · 2026-05-21T22:29:09.304Z_

<details><summary>↩ Tool result · `toolu_01T9TkYqhWpaZY5J3ecjevsf`</summary>

```text
{"result":"{\"success\": false, \"data\": {}, \"error\": \"Cannot transition to DONE without a 'conclusion' field. Set conclusion first.\", \"metadata\": {\"elapsed_seconds\": 0.7327}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "bcd9e5e6-c86c-4bf9-9402-037b79b77b15",
  "uuid": "f234cf21-c8a8-4c56-9957-b4d5d617520a",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": false, \\\"data\\\": {}, \\\"error\\\": \\\"Cannot transition to DONE without a 'conclusion' field. Set conclusion first.\\\", \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.7327}}\"}",
    "structuredContent": {
      "result": "{\"success\": false, \"data\": {}, \"error\": \"Cannot transition to DONE without a 'conclusion' field. Set conclusion first.\", \"metadata\": {\"elapsed_seconds\": 0.7327}}"
    }
  }
}
```

</details>

---

### Tool call

_source line 18_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry · `toolu_01E9a9a3SHpKhRrwQmo6Gv5f`</summary>

```json
{
  "exp_id": "eval_pi05_random_k07_spatial_seed42",
  "field": "hypothesis",
  "value": "π0.5 random k=0.7 on LIBERO-Spatial seed42. Object suite 上 random k=0.7=77.2% > L2norm k=0.7=55.0%。验证低 CV(0.055) 模型的 method preference (random > L2norm at k=0.7) 是否跨 suite 一致。",
  "project": "importance_margin_vla_compress"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "bcd9e5e6-c86c-4bf9-9402-037b79b77b15",
  "uuid": "18e14aaa-fc16-4112-aad9-e28d01e020b6",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012ktHTDhTwc4xdsUv9Wbhp8",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2053,
      "cache_read_input_tokens": 35428,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2053
      },
      "output_tokens": 72,
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

_source line 19 · 2026-05-21T22:29:15.454Z_

<details><summary>↩ Tool result · `toolu_01E9a9a3SHpKhRrwQmo6Gv5f`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval_pi05_random_k07_spatial_seed42\", \"experiment\": {\"status\": \"ANALYZING\", \"retry_count\": 0, \"created_at\": \"2026-05-21T20:55:22.277Z\", \"updated_at\": \"2026-05-21T22:29:14.974Z\", \"hypothesis\": \"π0.5 random k=0.7 on LIBERO-Spatial seed42. Object suite 上 random k=0.7=77.2% > L2norm k=0.7=55.0%。验证低 CV(0.055) 模型的 method preference (random > L2norm at k=0.7) 是否跨 suite 一致。\", \"spec\": {\"data_path\": \"libero_spatial (10 tasks x 50 eps)\", \"data_count\": 500, \"model_name\": \"pi05_libero_finetuned\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/pi05_libero_finetuned\", \"eval_data\": \"libero_spatial\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/importance_margin_vla_compress && HF_HUB_OFFLINE=1 python -u eval_pi05_pruning_libero.py --prune_mode random --keep_ratio 0.7 --suite libero_spatial --n_episodes 50 --seed 42 --gpu 0\\\"\", \"server\": \"westd-38929\", \"gpu\": [\"cuda:2\"], \"pid\": \"788353\", \"log_path\": \"~/runs/importance_margin_vla_compress/eval_pi05_random_k07_spatial_seed42.log\"}, \"reproduce\": {\"finished_at\": \"2026-05-21T22:26:50.626Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-21T22:26:58.674174+00:00\"}]}}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.2023}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "bcd9e5e6-c86c-4bf9-9402-037b79b77b15",
  "uuid": "43b94065-5b9e-4acf-a5f9-cb68595d454e",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"exp_id\\\": \\\"eval_pi05_random_k07_spatial_seed42\\\", \\\"experiment\\\": {\\\"status\\\": \\\"ANALYZING\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-21T20:55:22.277Z\\\", \\\"updated_at\\\": \\\"2026-05-21T22:29:14.974Z\\\", \\\"hypothesis\\\": \\\"π0.5 random k=0.7 on LIBERO-Spatial seed42. Object suite 上 random k=0.7=77.2% > L2norm k=0.7=55.0%。验证低 CV(0.055) 模型的 method preference (random > L2norm at k=0.7) 是否跨 suite 一致。\\\", \\\"spec\\\": {\\\"data_path\\\": \\\"libero_spatial (10 tasks x 50 eps)\\\", \\\"data_count\\\": 500, \\\"model_name\\\": \\\"pi05_libero_finetuned\\\", \\\"seed\\\": 42, \\\"checkpoint_source\\\": \\\"/root/autodl-tmp/pi05_libero_finetuned\\\", \\\"eval_data\\\": \\\"libero_spatial\\\", \\\"command\\\": \\\"bash -c \\\\\\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/importance_margin_vla_compress && HF_HUB_OFFLINE=1 python -u eval_pi05_pruning_libero.py --prune_mode random --keep_ratio 0.7 --suite libero_spatial --n_episodes 50 --seed 42 --gpu 0\\\\\\\"\\\", \\\"server\\\": \\\"westd-38929\\\", \\\"gpu\\\": [\\\"cuda:2\\\"], \\\"pid\\\": \\\"788353\\\", \\\"log_path\\\": \\\"~/runs/importance_margin_vla_compress/eval_pi05_random_k07_spatial_seed42.log\\\"}, \\\"reproduce\\\": {\\\"finished_at\\\": \\\"2026-05-21T22:26:50.626Z\\\"}, \\\"extra\\\": {\\\"hook_events\\\": [{\\\"event\\\": \\\"on_complete\\\", \\\"action\\\": \\\"agent\\\", \\\"ts\\\": \\\"2026-05-21T22:26:58.674174+00:00\\\"}]}}}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 1.2023}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"exp_id\": \"eval_pi05_random_k07_spatial_seed42\", \"experiment\": {\"status\": \"ANALYZING\", \"retry_count\": 0, \"created_at\": \"2026-05-21T20:55:22.277Z\", \"updated_at\": \"2026-05-21T22:29:14.974Z\", \"hypothesis\": \"π0.5 random k=0.7 on LIBERO-Spatial seed42. Object suite 上 random k=0.7=77.2% > L2norm k=0.7=55.0%。验证低 CV(0.055) 模型的 method preference (random > L2norm at k=0.7) 是否跨 suite 一致。\", \"spec\": {\"data_path\": \"libero_spatial (10 tasks x 50 eps)\", \"data_count\": 500, \"model_name\": \"pi05_libero_finetuned\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/pi05_libero_finetuned\", \"eval_data\": \"libero_spatial\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/importance_margin_vla_compress && HF_HUB_OFFLINE=1 python -u eval_pi05_pruning_libero.py --prune_mode random --keep_ratio 0.7 --suite libero_spatial --n_episodes 50 --seed 42 --gpu 0\\\"\", \"server\": \"westd-38929\", \"gpu\": [\"cuda:2\"], \"pid\": \"788353\", \"log_path\": \"~/runs/importance_margin_vla_compress/eval_pi05_random_k07_spatial_seed42.log\"}, \"reproduce\": {\"finished_at\": \"2026-05-21T22:26:50.626Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-21T22:26:58.674174+00:00\"}]}}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.2023}}"
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
Good, the experiment already exists in the registry with status ANALYZING. Now I need to set the conclusion and then transition to DONE.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "bcd9e5e6-c86c-4bf9-9402-037b79b77b15",
  "uuid": "aafa99cf-4fd5-4600-86dd-e5dd74be5cbb",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JCKETthWq1FxYChiCz4o7g",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 853,
      "cache_read_input_tokens": 37481,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 853
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

_source line 21_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry · `toolu_01EfT5KuCjdJYikjah4mRqVA`</summary>

```json
{
  "exp_id": "eval_pi05_random_k07_spatial_seed42",
  "field": "conclusion",
  "value": "success",
  "project": "importance_margin_vla_compress"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "bcd9e5e6-c86c-4bf9-9402-037b79b77b15",
  "uuid": "fdcc3f80-a94c-447e-8390-2e5f5d05abd4",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JCKETthWq1FxYChiCz4o7g",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 853,
      "cache_read_input_tokens": 37481,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 853
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

_source line 22 · 2026-05-21T22:29:20.867Z_

<details><summary>↩ Tool result · `toolu_01EfT5KuCjdJYikjah4mRqVA`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval_pi05_random_k07_spatial_seed42\", \"experiment\": {\"status\": \"ANALYZING\", \"retry_count\": 0, \"created_at\": \"2026-05-21T20:55:22.277Z\", \"updated_at\": \"2026-05-21T22:29:19.845Z\", \"hypothesis\": \"π0.5 random k=0.7 on LIBERO-Spatial seed42. Object suite 上 random k=0.7=77.2% > L2norm k=0.7=55.0%。验证低 CV(0.055) 模型的 method preference (random > L2norm at k=0.7) 是否跨 suite 一致。\", \"spec\": {\"data_path\": \"libero_spatial (10 tasks x 50 eps)\", \"data_count\": 500, \"model_name\": \"pi05_libero_finetuned\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/pi05_libero_finetuned\", \"eval_data\": \"libero_spatial\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/importance_margin_vla_compress && HF_HUB_OFFLINE=1 python -u eval_pi05_pruning_libero.py --prune_mode random --keep_ratio 0.7 --suite libero_spatial --n_episodes 50 --seed 42 --gpu 0\\\"\", \"server\": \"westd-38929\", \"gpu\": [\"cuda:2\"], \"pid\": \"788353\", \"log_path\": \"~/runs/importance_margin_vla_compress/eval_pi05_random_k07_spatial_seed42.log\"}, \"reproduce\": {\"finished_at\": \"2026-05-21T22:26:50.626Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-21T22:26:58.674174+00:00\"}]}, \"conclusion\": \"success\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.7793}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "bcd9e5e6-c86c-4bf9-9402-037b79b77b15",
  "uuid": "1b6836e1-bd88-4901-ad82-4e66fd9ef983",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"exp_id\\\": \\\"eval_pi05_random_k07_spatial_seed42\\\", \\\"experiment\\\": {\\\"status\\\": \\\"ANALYZING\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-21T20:55:22.277Z\\\", \\\"updated_at\\\": \\\"2026-05-21T22:29:19.845Z\\\", \\\"hypothesis\\\": \\\"π0.5 random k=0.7 on LIBERO-Spatial seed42. Object suite 上 random k=0.7=77.2% > L2norm k=0.7=55.0%。验证低 CV(0.055) 模型的 method preference (random > L2norm at k=0.7) 是否跨 suite 一致。\\\", \\\"spec\\\": {\\\"data_path\\\": \\\"libero_spatial (10 tasks x 50 eps)\\\", \\\"data_count\\\": 500, \\\"model_name\\\": \\\"pi05_libero_finetuned\\\", \\\"seed\\\": 42, \\\"checkpoint_source\\\": \\\"/root/autodl-tmp/pi05_libero_finetuned\\\", \\\"eval_data\\\": \\\"libero_spatial\\\", \\\"command\\\": \\\"bash -c \\\\\\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/importance_margin_vla_compress && HF_HUB_OFFLINE=1 python -u eval_pi05_pruning_libero.py --prune_mode random --keep_ratio 0.7 --suite libero_spatial --n_episodes 50 --seed 42 --gpu 0\\\\\\\"\\\", \\\"server\\\": \\\"westd-38929\\\", \\\"gpu\\\": [\\\"cuda:2\\\"], \\\"pid\\\": \\\"788353\\\", \\\"log_path\\\": \\\"~/runs/importance_margin_vla_compress/eval_pi05_random_k07_spatial_seed42.log\\\"}, \\\"reproduce\\\": {\\\"finished_at\\\": \\\"2026-05-21T22:26:50.626Z\\\"}, \\\"extra\\\": {\\\"hook_events\\\": [{\\\"event\\\": \\\"on_complete\\\", \\\"action\\\": \\\"agent\\\", \\\"ts\\\": \\\"2026-05-21T22:26:58.674174+00:00\\\"}]}, \\\"conclusion\\\": \\\"success\\\"}}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 1.7793}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"exp_id\": \"eval_pi05_random_k07_spatial_seed42\", \"experiment\": {\"status\": \"ANALYZING\", \"retry_count\": 0, \"created_at\": \"2026-05-21T20:55:22.277Z\", \"updated_at\": \"2026-05-21T22:29:19.845Z\", \"hypothesis\": \"π0.5 random k=0.7 on LIBERO-Spatial seed42. Object suite 上 random k=0.7=77.2% > L2norm k=0.7=55.0%。验证低 CV(0.055) 模型的 method preference (random > L2norm at k=0.7) 是否跨 suite 一致。\", \"spec\": {\"data_path\": \"libero_spatial (10 tasks x 50 eps)\", \"data_count\": 500, \"model_name\": \"pi05_libero_finetuned\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/pi05_libero_finetuned\", \"eval_data\": \"libero_spatial\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/importance_margin_vla_compress && HF_HUB_OFFLINE=1 python -u eval_pi05_pruning_libero.py --prune_mode random --keep_ratio 0.7 --suite libero_spatial --n_episodes 50 --seed 42 --gpu 0\\\"\", \"server\": \"westd-38929\", \"gpu\": [\"cuda:2\"], \"pid\": \"788353\", \"log_path\": \"~/runs/importance_margin_vla_compress/eval_pi05_random_k07_spatial_seed42.log\"}, \"reproduce\": {\"finished_at\": \"2026-05-21T22:26:50.626Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-21T22:26:58.674174+00:00\"}]}, \"conclusion\": \"success\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.7793}}"
    }
  }
}
```

</details>

---

### Tool call

_source line 23_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry · `toolu_01Nf158Ng1xWgbAPSsC1CdHy`</summary>

```json
{
  "exp_id": "eval_pi05_random_k07_spatial_seed42",
  "field": "metrics",
  "value": {
    "success_rate": 74.4,
    "total_episodes": 500,
    "per_task_sr": {
      "T0_between_plate": 90,
      "T1_next_to_ramekin": 96,
      "T2_table_center": 94,
      "T3_on_cookie_box": 52,
      "T4_in_top_drawer": 60,
      "T5_on_ramekin": 42,
      "T6_next_to_cookie": 58,
      "T7_on_stove": 76,
      "T8_next_to_plate": 80,
      "T9_on_wooden_cab": 96
    }
  },
  "project": "importance_margin_vla_compress"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "bcd9e5e6-c86c-4bf9-9402-037b79b77b15",
  "uuid": "bc6ebf29-617c-4a0e-ad78-b0bb1fedf3fa",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01L74ZxaSbxw28VVUSZbPHqp",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 811,
      "cache_read_input_tokens": 38334,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 811
      },
      "output_tokens": 69,
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

_source line 24 · 2026-05-21T22:29:29.570Z_

<details><summary>↩ Tool result · `toolu_01Nf158Ng1xWgbAPSsC1CdHy`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval_pi05_random_k07_spatial_seed42\", \"experiment\": {\"status\": \"ANALYZING\", \"retry_count\": 0, \"created_at\": \"2026-05-21T20:55:22.277Z\", \"updated_at\": \"2026-05-21T22:29:28.023Z\", \"hypothesis\": \"π0.5 random k=0.7 on LIBERO-Spatial seed42. Object suite 上 random k=0.7=77.2% > L2norm k=0.7=55.0%。验证低 CV(0.055) 模型的 method preference (random > L2norm at k=0.7) 是否跨 suite 一致。\", \"spec\": {\"data_path\": \"libero_spatial (10 tasks x 50 eps)\", \"data_count\": 500, \"model_name\": \"pi05_libero_finetuned\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/pi05_libero_finetuned\", \"eval_data\": \"libero_spatial\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/importance_margin_vla_compress && HF_HUB_OFFLINE=1 python -u eval_pi05_pruning_libero.py --prune_mode random --keep_ratio 0.7 --suite libero_spatial --n_episodes 50 --seed 42 --gpu 0\\\"\", \"server\": \"westd-38929\", \"gpu\": [\"cuda:2\"], \"pid\": \"788353\", \"log_path\": \"~/runs/importance_margin_vla_compress/eval_pi05_random_k07_spatial_seed42.log\"}, \"reproduce\": {\"finished_at\": \"2026-05-21T22:26:50.626Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-21T22:26:58.674174+00:00\"}]}, \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 74.4, \"total_episodes\": 500, \"per_task_sr\": {\"T0_between_plate\": 90, \"T1_next_to_ramekin\": 96, \"T2_table_center\": 94, \"T3_on_cookie_box\": 52, \"T4_in_top_drawer\": 60, \"T5_on_ramekin\": 42, \"T6_next_to_cookie\": 58, \"T7_on_stove\": 76, \"T8_next_to_plate\": 80, \"T9_on_wooden_cab\": 96}}}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 2.7061}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "bcd9e5e6-c86c-4bf9-9402-037b79b77b15",
  "uuid": "662d6ab6-ee95-4bee-9a35-df62c512deec",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"exp_id\\\": \\\"eval_pi05_random_k07_spatial_seed42\\\", \\\"experiment\\\": {\\\"status\\\": \\\"ANALYZING\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-21T20:55:22.277Z\\\", \\\"updated_at\\\": \\\"2026-05-21T22:29:28.023Z\\\", \\\"hypothesis\\\": \\\"π0.5 random k=0.7 on LIBERO-Spatial seed42. Object suite 上 random k=0.7=77.2% > L2norm k=0.7=55.0%。验证低 CV(0.055) 模型的 method preference (random > L2norm at k=0.7) 是否跨 suite 一致。\\\", \\\"spec\\\": {\\\"data_path\\\": \\\"libero_spatial (10 tasks x 50 eps)\\\", \\\"data_count\\\": 500, \\\"model_name\\\": \\\"pi05_libero_finetuned\\\", \\\"seed\\\": 42, \\\"checkpoint_source\\\": \\\"/root/autodl-tmp/pi05_libero_finetuned\\\", \\\"eval_data\\\": \\\"libero_spatial\\\", \\\"command\\\": \\\"bash -c \\\\\\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/importance_margin_vla_compress && HF_HUB_OFFLINE=1 python -u eval_pi05_pruning_libero.py --prune_mode random --keep_ratio 0.7 --suite libero_spatial --n_episodes 50 --seed 42 --gpu 0\\\\\\\"\\\", \\\"server\\\": \\\"westd-38929\\\", \\\"gpu\\\": [\\\"cuda:2\\\"], \\\"pid\\\": \\\"788353\\\", \\\"log_path\\\": \\\"~/runs/importance_margin_vla_compress/eval_pi05_random_k07_spatial_seed42.log\\\"}, \\\"reproduce\\\": {\\\"finished_at\\\": \\\"2026-05-21T22:26:50.626Z\\\"}, \\\"extra\\\": {\\\"hook_events\\\": [{\\\"event\\\": \\\"on_complete\\\", \\\"action\\\": \\\"agent\\\", \\\"ts\\\": \\\"2026-05-21T22:26:58.674174+00:00\\\"}]}, \\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"success_rate\\\": 74.4, \\\"total_episodes\\\": 500, \\\"per_task_sr\\\": {\\\"T0_between_plate\\\": 90, \\\"T1_next_to_ramekin\\\": 96, \\\"T2_table_center\\\": 94, \\\"T3_on_cookie_box\\\": 52, \\\"T4_in_top_drawer\\\": 60, \\\"T5_on_ramekin\\\": 42, \\\"T6_next_to_cookie\\\": 58, \\\"T7_on_stove\\\": 76, \\\"T8_next_to_plate\\\": 80, \\\"T9_on_wooden_cab\\\": 96}}}}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 2.7061}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"exp_id\": \"eval_pi05_random_k07_spatial_seed42\", \"experiment\": {\"status\": \"ANALYZING\", \"retry_count\": 0, \"created_at\": \"2026-05-21T20:55:22.277Z\", \"updated_at\": \"2026-05-21T22:29:28.023Z\", \"hypothesis\": \"π0.5 random k=0.7 on LIBERO-Spatial seed42. Object suite 上 random k=0.7=77.2% > L2norm k=0.7=55.0%。验证低 CV(0.055) 模型的 method preference (random > L2norm at k=0.7) 是否跨 suite 一致。\", \"spec\": {\"data_path\": \"libero_spatial (10 tasks x 50 eps)\", \"data_count\": 500, \"model_name\": \"pi05_libero_finetuned\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/pi05_libero_finetuned\", \"eval_data\": \"libero_spatial\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/importance_margin_vla_compress && HF_HUB_OFFLINE=1 python -u eval_pi05_pruning_libero.py --prune_mode random --keep_ratio 0.7 --suite libero_spatial --n_episodes 50 --seed 42 --gpu 0\\\"\", \"server\": \"westd-38929\", \"gpu\": [\"cuda:2\"], \"pid\": \"788353\", \"log_path\": \"~/runs/importance_margin_vla_compress/eval_pi05_random_k07_spatial_seed42.log\"}, \"reproduce\": {\"finished_at\": \"2026-05-21T22:26:50.626Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-21T22:26:58.674174+00:00\"}]}, \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 74.4, \"total_episodes\": 500, \"per_task_sr\": {\"T0_between_plate\": 90, \"T1_next_to_ramekin\": 96, \"T2_table_center\": 94, \"T3_on_cookie_box\": 52, \"T4_in_top_drawer\": 60, \"T5_on_ramekin\": 42, \"T6_next_to_cookie\": 58, \"T7_on_stove\": 76, \"T8_next_to_plate\": 80, \"T9_on_wooden_cab\": 96}}}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 2.7061}}"
    }
  }
}
```

</details>

---

### Tool call

_source line 25_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry · `toolu_019YQZLsaNb6XdspUhCYbTeR`</summary>

```json
{
  "exp_id": "eval_pi05_random_k07_spatial_seed42",
  "field": "status",
  "value": "DONE",
  "project": "importance_margin_vla_compress"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "bcd9e5e6-c86c-4bf9-9402-037b79b77b15",
  "uuid": "891edf76-db78-4791-8d64-59fd35d4c4ef",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FHAu7RPaqGcxZMdnrbH7gN",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1194,
      "cache_read_input_tokens": 39145,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1194
      },
      "output_tokens": 54,
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

_source line 26 · 2026-05-21T22:29:36.043Z_

<details><summary>↩ Tool result · `toolu_019YQZLsaNb6XdspUhCYbTeR`</summary>

```text
{"result":"{\"success\": false, \"data\": {}, \"error\": \"Cannot transition to DONE without output fields: ['checkpoint_path']. Set these fields first or pass them in spec.\", \"metadata\": {\"elapsed_seconds\": 0.8679}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "bcd9e5e6-c86c-4bf9-9402-037b79b77b15",
  "uuid": "bde25590-cf29-4ce9-abcd-64d2a843b055",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": false, \\\"data\\\": {}, \\\"error\\\": \\\"Cannot transition to DONE without output fields: ['checkpoint_path']. Set these fields first or pass them in spec.\\\", \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.8679}}\"}",
    "structuredContent": {
      "result": "{\"success\": false, \"data\": {}, \"error\": \"Cannot transition to DONE without output fields: ['checkpoint_path']. Set these fields first or pass them in spec.\", \"metadata\": {\"elapsed_seconds\": 0.8679}}"
    }
  }
}
```

</details>

---

### Tool call

_source line 27_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry · `toolu_01A6Upx7zoq57QVcrfUGvLiC`</summary>

```json
{
  "exp_id": "eval_pi05_random_k07_spatial_seed42",
  "field": "checkpoint_path",
  "value": "/root/autodl-tmp/pi05_libero_finetuned",
  "project": "importance_margin_vla_compress"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "bcd9e5e6-c86c-4bf9-9402-037b79b77b15",
  "uuid": "61a9b63f-d2d9-4904-b640-6eb3f3db7567",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013yJFPkWDux2hHuRQa3CDMy",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 213,
      "cache_read_input_tokens": 40339,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 213
      },
      "output_tokens": 72,
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

_source line 28 · 2026-05-21T22:29:42.913Z_

<details><summary>↩ Tool result · `toolu_01A6Upx7zoq57QVcrfUGvLiC`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval_pi05_random_k07_spatial_seed42\", \"experiment\": {\"status\": \"ANALYZING\", \"retry_count\": 0, \"created_at\": \"2026-05-21T20:55:22.277Z\", \"updated_at\": \"2026-05-21T22:29:42.417Z\", \"hypothesis\": \"π0.5 random k=0.7 on LIBERO-Spatial seed42. Object suite 上 random k=0.7=77.2% > L2norm k=0.7=55.0%。验证低 CV(0.055) 模型的 method preference (random > L2norm at k=0.7) 是否跨 suite 一致。\", \"spec\": {\"data_path\": \"libero_spatial (10 tasks x 50 eps)\", \"data_count\": 500, \"model_name\": \"pi05_libero_finetuned\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/pi05_libero_finetuned\", \"eval_data\": \"libero_spatial\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/importance_margin_vla_compress && HF_HUB_OFFLINE=1 python -u eval_pi05_pruning_libero.py --prune_mode random --keep_ratio 0.7 --suite libero_spatial --n_episodes 50 --seed 42 --gpu 0\\\"\", \"server\": \"westd-38929\", \"gpu\": [\"cuda:2\"], \"pid\": \"788353\", \"log_path\": \"~/runs/importance_margin_vla_compress/eval_pi05_random_k07_spatial_seed42.log\"}, \"reproduce\": {\"finished_at\": \"2026-05-21T22:26:50.626Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-21T22:26:58.674174+00:00\"}]}, \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 74.4, \"total_episodes\": 500, \"per_task_sr\": {\"T0_between_plate\": 90, \"T1_next_to_ramekin\": 96, \"T2_table_center\": 94, \"T3_on_cookie_box\": 52, \"T4_in_top_drawer\": 60, \"T5_on_ramekin\": 42, \"T6_next_to_cookie\": 58, \"T7_on_stove\": 76, \"T8_next_to_plate\": 80, \"T9_on_wooden_cab\": 96}}, \"checkpoint_path\": \"/root/autodl-tmp/pi05_libero_finetuned\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.2318}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "bcd9e5e6-c86c-4bf9-9402-037b79b77b15",
  "uuid": "6aefa792-f8e6-4ab4-889e-d65ac744ebdf",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"exp_id\\\": \\\"eval_pi05_random_k07_spatial_seed42\\\", \\\"experiment\\\": {\\\"status\\\": \\\"ANALYZING\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-21T20:55:22.277Z\\\", \\\"updated_at\\\": \\\"2026-05-21T22:29:42.417Z\\\", \\\"hypothesis\\\": \\\"π0.5 random k=0.7 on LIBERO-Spatial seed42. Object suite 上 random k=0.7=77.2% > L2norm k=0.7=55.0%。验证低 CV(0.055) 模型的 method preference (random > L2norm at k=0.7) 是否跨 suite 一致。\\\", \\\"spec\\\": {\\\"data_path\\\": \\\"libero_spatial (10 tasks x 50 eps)\\\", \\\"data_count\\\": 500, \\\"model_name\\\": \\\"pi05_libero_finetuned\\\", \\\"seed\\\": 42, \\\"checkpoint_source\\\": \\\"/root/autodl-tmp/pi05_libero_finetuned\\\", \\\"eval_data\\\": \\\"libero_spatial\\\", \\\"command\\\": \\\"bash -c \\\\\\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/importance_margin_vla_compress && HF_HUB_OFFLINE=1 python -u eval_pi05_pruning_libero.py --prune_mode random --keep_ratio 0.7 --suite libero_spatial --n_episodes 50 --seed 42 --gpu 0\\\\\\\"\\\", \\\"server\\\": \\\"westd-38929\\\", \\\"gpu\\\": [\\\"cuda:2\\\"], \\\"pid\\\": \\\"788353\\\", \\\"log_path\\\": \\\"~/runs/importance_margin_vla_compress/eval_pi05_random_k07_spatial_seed42.log\\\"}, \\\"reproduce\\\": {\\\"finished_at\\\": \\\"2026-05-21T22:26:50.626Z\\\"}, \\\"extra\\\": {\\\"hook_events\\\": [{\\\"event\\\": \\\"on_complete\\\", \\\"action\\\": \\\"agent\\\", \\\"ts\\\": \\\"2026-05-21T22:26:58.674174+00:00\\\"}]}, \\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"success_rate\\\": 74.4, \\\"total_episodes\\\": 500, \\\"per_task_sr\\\": {\\\"T0_between_plate\\\": 90, \\\"T1_next_to_ramekin\\\": 96, \\\"T2_table_center\\\": 94, \\\"T3_on_cookie_box\\\": 52, \\\"T4_in_top_drawer\\\": 60, \\\"T5_on_ramekin\\\": 42, \\\"T6_next_to_cookie\\\": 58, \\\"T7_on_stove\\\": 76, \\\"T8_next_to_plate\\\": 80, \\\"T9_on_wooden_cab\\\": 96}}, \\\"checkpoint_path\\\": \\\"/root/autodl-tmp/pi05_libero_finetuned\\\"}}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 1.2318}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"exp_id\": \"eval_pi05_random_k07_spatial_seed42\", \"experiment\": {\"status\": \"ANALYZING\", \"retry_count\": 0, \"created_at\": \"2026-05-21T20:55:22.277Z\", \"updated_at\": \"2026-05-21T22:29:42.417Z\", \"hypothesis\": \"π0.5 random k=0.7 on LIBERO-Spatial seed42. Object suite 上 random k=0.7=77.2% > L2norm k=0.7=55.0%。验证低 CV(0.055) 模型的 method preference (random > L2norm at k=0.7) 是否跨 suite 一致。\", \"spec\": {\"data_path\": \"libero_spatial (10 tasks x 50 eps)\", \"data_count\": 500, \"model_name\": \"pi05_libero_finetuned\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/pi05_libero_finetuned\", \"eval_data\": \"libero_spatial\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/importance_margin_vla_compress && HF_HUB_OFFLINE=1 python -u eval_pi05_pruning_libero.py --prune_mode random --keep_ratio 0.7 --suite libero_spatial --n_episodes 50 --seed 42 --gpu 0\\\"\", \"server\": \"westd-38929\", \"gpu\": [\"cuda:2\"], \"pid\": \"788353\", \"log_path\": \"~/runs/importance_margin_vla_compress/eval_pi05_random_k07_spatial_seed42.log\"}, \"reproduce\": {\"finished_at\": \"2026-05-21T22:26:50.626Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-21T22:26:58.674174+00:00\"}]}, \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 74.4, \"total_episodes\": 500, \"per_task_sr\": {\"T0_between_plate\": 90, \"T1_next_to_ramekin\": 96, \"T2_table_center\": 94, \"T3_on_cookie_box\": 52, \"T4_in_top_drawer\": 60, \"T5_on_ramekin\": 42, \"T6_next_to_cookie\": 58, \"T7_on_stove\": 76, \"T8_next_to_plate\": 80, \"T9_on_wooden_cab\": 96}}, \"checkpoint_path\": \"/root/autodl-tmp/pi05_libero_finetuned\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.2318}}"
    }
  }
}
```

</details>

---

### Tool call

_source line 29_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry · `toolu_01FqZZygCwFWgrNTX4KDx2t3`</summary>

```json
{
  "exp_id": "eval_pi05_random_k07_spatial_seed42",
  "field": "status",
  "value": "DONE",
  "project": "importance_margin_vla_compress"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "bcd9e5e6-c86c-4bf9-9402-037b79b77b15",
  "uuid": "d0052969-9c0f-46b3-94f1-d8842308e721",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01C3eJTCwtjuTCW54ov6qqqE",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 986,
      "cache_read_input_tokens": 40552,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 986
      },
      "output_tokens": 72,
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

_source line 30 · 2026-05-21T22:29:47.668Z_

<details><summary>↩ Tool result · `toolu_01FqZZygCwFWgrNTX4KDx2t3`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval_pi05_random_k07_spatial_seed42\", \"experiment\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-21T20:55:22.277Z\", \"updated_at\": \"2026-05-21T22:29:46.227Z\", \"hypothesis\": \"π0.5 random k=0.7 on LIBERO-Spatial seed42. Object suite 上 random k=0.7=77.2% > L2norm k=0.7=55.0%。验证低 CV(0.055) 模型的 method preference (random > L2norm at k=0.7) 是否跨 suite 一致。\", \"spec\": {\"data_path\": \"libero_spatial (10 tasks x 50 eps)\", \"data_count\": 500, \"model_name\": \"pi05_libero_finetuned\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/pi05_libero_finetuned\", \"eval_data\": \"libero_spatial\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/importance_margin_vla_compress && HF_HUB_OFFLINE=1 python -u eval_pi05_pruning_libero.py --prune_mode random --keep_ratio 0.7 --suite libero_spatial --n_episodes 50 --seed 42 --gpu 0\\\"\", \"server\": \"westd-38929\", \"gpu\": [\"cuda:2\"], \"pid\": \"788353\", \"log_path\": \"~/runs/importance_margin_vla_compress/eval_pi05_random_k07_spatial_seed42.log\"}, \"reproduce\": {\"finished_at\": \"2026-05-21T22:26:50.626Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-21T22:26:58.674174+00:00\"}]}, \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 74.4, \"total_episodes\": 500, \"per_task_sr\": {\"T0_between_plate\": 90, \"T1_next_to_ramekin\": 96, \"T2_table_center\": 94, \"T3_on_cookie_box\": 52, \"T4_in_top_drawer\": 60, \"T5_on_ramekin\": 42, \"T6_next_to_cookie\": 58, \"T7_on_stove\": 76, \"T8_next_to_plate\": 80, \"T9_on_wooden_cab\": 96}}, \"checkpoint_path\": \"/root/autodl-tmp/pi05_libero_finetuned\", \"completed_at\": \"2026-05-21T22:29:46.227Z\"}, \"hint\": \"💡 建议将成功经验写入 memory.md（什么 work、关键参数）\"}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 2.2078}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "bcd9e5e6-c86c-4bf9-9402-037b79b77b15",
  "uuid": "fa421da4-a23b-4d67-ad8e-7908058794b9",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"exp_id\\\": \\\"eval_pi05_random_k07_spatial_seed42\\\", \\\"experiment\\\": {\\\"status\\\": \\\"DONE\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-21T20:55:22.277Z\\\", \\\"updated_at\\\": \\\"2026-05-21T22:29:46.227Z\\\", \\\"hypothesis\\\": \\\"π0.5 random k=0.7 on LIBERO-Spatial seed42. Object suite 上 random k=0.7=77.2% > L2norm k=0.7=55.0%。验证低 CV(0.055) 模型的 method preference (random > L2norm at k=0.7) 是否跨 suite 一致。\\\", \\\"spec\\\": {\\\"data_path\\\": \\\"libero_spatial (10 tasks x 50 eps)\\\", \\\"data_count\\\": 500, \\\"model_name\\\": \\\"pi05_libero_finetuned\\\", \\\"seed\\\": 42, \\\"checkpoint_source\\\": \\\"/root/autodl-tmp/pi05_libero_finetuned\\\", \\\"eval_data\\\": \\\"libero_spatial\\\", \\\"command\\\": \\\"bash -c \\\\\\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/importance_margin_vla_compress && HF_HUB_OFFLINE=1 python -u eval_pi05_pruning_libero.py --prune_mode random --keep_ratio 0.7 --suite libero_spatial --n_episodes 50 --seed 42 --gpu 0\\\\\\\"\\\", \\\"server\\\": \\\"westd-38929\\\", \\\"gpu\\\": [\\\"cuda:2\\\"], \\\"pid\\\": \\\"788353\\\", \\\"log_path\\\": \\\"~/runs/importance_margin_vla_compress/eval_pi05_random_k07_spatial_seed42.log\\\"}, \\\"reproduce\\\": {\\\"finished_at\\\": \\\"2026-05-21T22:26:50.626Z\\\"}, \\\"extra\\\": {\\\"hook_events\\\": [{\\\"event\\\": \\\"on_complete\\\", \\\"action\\\": \\\"agent\\\", \\\"ts\\\": \\\"2026-05-21T22:26:58.674174+00:00\\\"}]}, \\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"success_rate\\\": 74.4, \\\"total_episodes\\\": 500, \\\"per_task_sr\\\": {\\\"T0_between_plate\\\": 90, \\\"T1_next_to_ramekin\\\": 96, \\\"T2_table_center\\\": 94, \\\"T3_on_cookie_box\\\": 52, \\\"T4_in_top_drawer\\\": 60, \\\"T5_on_ramekin\\\": 42, \\\"T6_next_to_cookie\\\": 58, \\\"T7_on_stove\\\": 76, \\\"T8_next_to_plate\\\": 80, \\\"T9_on_wooden_cab\\\": 96}}, \\\"checkpoint_path\\\": \\\"/root/autodl-tmp/pi05_libero_finetuned\\\", \\\"completed_at\\\": \\\"2026-05-21T22:29:46.227Z\\\"}, \\\"hint\\\": \\\"💡 建议将成功经验写入 memory.md（什么 work、关键参数）\\\"}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 2.2078}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"exp_id\": \"eval_pi05_random_k07_spatial_seed42\", \"experiment\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-21T20:55:22.277Z\", \"updated_at\": \"2026-05-21T22:29:46.227Z\", \"hypothesis\": \"π0.5 random k=0.7 on LIBERO-Spatial seed42. Object suite 上 random k=0.7=77.2% > L2norm k=0.7=55.0%。验证低 CV(0.055) 模型的 method preference (random > L2norm at k=0.7) 是否跨 suite 一致。\", \"spec\": {\"data_path\": \"libero_spatial (10 tasks x 50 eps)\", \"data_count\": 500, \"model_name\": \"pi05_libero_finetuned\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/pi05_libero_finetuned\", \"eval_data\": \"libero_spatial\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/importance_margin_vla_compress && HF_HUB_OFFLINE=1 python -u eval_pi05_pruning_libero.py --prune_mode random --keep_ratio 0.7 --suite libero_spatial --n_episodes 50 --seed 42 --gpu 0\\\"\", \"server\": \"westd-38929\", \"gpu\": [\"cuda:2\"], \"pid\": \"788353\", \"log_path\": \"~/runs/importance_margin_vla_compress/eval_pi05_random_k07_spatial_seed42.log\"}, \"reproduce\": {\"finished_at\": \"2026-05-21T22:26:50.626Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-21T22:26:58.674174+00:00\"}]}, \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 74.4, \"total_episodes\": 500, \"per_task_sr\": {\"T0_between_plate\": 90, \"T1_next_to_ramekin\": 96, \"T2_table_center\": 94, \"T3_on_cookie_box\": 52, \"T4_in_top_drawer\": 60, \"T5_on_ramekin\": 42, \"T6_next_to_cookie\": 58, \"T7_on_stove\": 76, \"T8_next_to_plate\": 80, \"T9_on_wooden_cab\": 96}}, \"checkpoint_path\": \"/root/autodl-tmp/pi05_libero_finetuned\", \"completed_at\": \"2026-05-21T22:29:46.227Z\"}, \"hint\": \"💡 建议将成功经验写入 memory.md（什么 work、关键参数）\"}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 2.2078}}"
    }
  }
}
```

</details>

---

### Assistant

_source line 31_

Registry 已更新为 DONE/success。现在将分析写入 report.md。由于 report.md 的 save_project_file 不支持直接写入（需要用专用工具），让我读取 memory.md 看看现有内容再更新。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "bcd9e5e6-c86c-4bf9-9402-037b79b77b15",
  "uuid": "ba0c9076-c54f-47ef-8259-15ca4ba3fea2",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01X5TWFWTkDaJvLzS8u3ZC8h",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1025,
      "cache_read_input_tokens": 41538,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1025
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

_source line 32_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01AzQofvw6T39DhT7DvgBBYN`</summary>

```json
{
  "project": "importance_margin_vla_compress",
  "file": "memory.md",
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
  "session_id": "bcd9e5e6-c86c-4bf9-9402-037b79b77b15",
  "uuid": "85501813-9b34-48f6-9248-f49a1c59d4c9",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01X5TWFWTkDaJvLzS8u3ZC8h",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1025,
      "cache_read_input_tokens": 41538,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1025
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

_source line 33 · 2026-05-21T22:29:55.575Z_

<details><summary>↩ Tool result · `toolu_01AzQofvw6T39DhT7DvgBBYN`</summary>

````text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/memory.md\", \"content\": \"# VLA 模型全面调研报告\\n\\n**调研日期**: 2026-05-20\\n**目的**: 寻找不同 connector 架构的开源 VLA 模型，扩展 vision connector 对 token 可压缩性影响的实验\\n\\n---\\n\\n## 已有实验数据\\n\\n| 模型 | Connector | 压缩行为 |\\n|------|-----------|----------|\\n| SmolVLA | Pixel-shuffle | Cliff-edge collapse (k=0.95 → 0% SR) |\\n| OpenVLA | 2-layer MLP projector | Graded degradation (线性下降) |\\n| RoboFlamingo | Perceiver Resampler | 尝试失败（gripper loss 无法训练） |\\n| **X-VLA** | **Linear projection** | **Nearly lossless (k=0.3 → norm=1.0014)** |\\n\\n---\\n\\n## 完整模型调研表\\n\\n### 1. Octo (UC Berkeley, 2024)\\n\\n| 字段 | 信息 |\\n|------|------|\\n| 参数量 | 27M (Small) / 93M (Base) |\\n| Vision encoder | Shallow CNN (从头训练，非预训练 ViT) |\\n| **Connector 类型** | **CNN patch encoder → 直接拼接进 transformer（无独立 connector）** |\\n| LLM backbone | 纯 transformer（非预训练 LLM），decoder-only |\\n| 开源状态 | ✅ weights + code, GitHub: [octo-models/octo](https://github.com/octo-models/octo), HF: rail-berkeley/octo-base |\\n| LIBERO 支持 | ✅ 原生支持，fine-tune 后 ~72% SR |\\n| 改造成本 | 低（已有 LIBERO fine-tune 代码） |\\n| 论文 LIBERO 结果 | 有: ~72% (fine-tuned) |\\n| 备注 | 非标准 VLM→LLM 架构，是 transformer-based diffusion policy。图像通过浅层 CNN 编码为 16×16 patches 后直接拼入 transformer 序列。语言用 T5 tokenizer/encoder。Action head 是 diffusion policy。 |\\n\\n### 2. CogACT (Microsoft/Tsinghua, 2024)\\n\\n| 字段 | 信息 |\\n|------|------|\\n| 参数量 | ~7.1B (7B Prismatic VLM + 89M-300M DiT action module) |\\n| Vision encoder | DINOv2 + SigLIP (双 encoder，channel 拼接) |\\n| **Connector 类型** | **2-layer MLP projector**（Prismatic 架构：DINOv2+SigLIP feature → channel concat → 2-layer MLP → Llama-2 embedding space） |\\n| LLM backbone | Llama-2 7B (via Prismatic-7B) |\\n| 开源状态 | ✅ weights + code, GitHub: [microsoft/CogACT](https://github.com/microsoft/CogACT), HF: CogACT/CogACT-Base, CogACT/CogACT-Small |\\n| LIBERO 支持 | 需改造（paper 用 SimplerEnv + 真机） |\\n| 改造成本 | 中（需接 LIBERO data pipeline + action space） |\\n| 论文 LIBERO 结果 | 无 |\\n| 备注 | 核心创新在 DiT action module（将 VLM 认知特征作为 condition 输入扩散 transformer 生成动作）。Connector 与 OpenVLA 相同（都基于 Prismatic） |\\n\\n### 3. HPT (MIT, NeurIPS 2024)\\n\\n| 字段 | 信息 |\\n|------|------|\\n| 参数量 | 3.1M (S) / 12.6M (B) / 50.5M (L) / 226.8M (XL) / 1.1B (Huge) |\\n| Vision encoder | 预训练冻结 ResNet18 |\\n| **Connector 类型** | **Cross-attention tokenizer**（learnable tokens 通过 cross-attention 聚合 vision features → 固定 16 tokens，每个 camera view 有独立 MLP projector） |\\n| LLM backbone | 无（纯 decoder-only transformer，从头训练） |\\n| 开源状态 | ✅ weights + code, GitHub: [liruiw/HPT](https://github.com/liruiw/HPT), HF: liruiw/hpt |\\n| LIBERO 支持 | 未确认（paper 评测 6 个 benchmark） |\\n| 改造成本 | 中（非标准 VLM 架构，需改 stem + action head） |\\n| 论文 LIBERO 结果 | 无 |\\n| 备注 | 非 VLM→LLM 架构。Cross-attention tokenizer 类似 Perceiver 但更轻量（8 heads, 64 dim/head）。跨 embodiment 预训练。 |\\n\\n### 4. RT-2-X (Google DeepMind, 2023)\\n\\n| 字段 | 信息 |\\n|------|------|\\n| 参数量 | 55B |\\n| Vision encoder | ViT (PaLI-X 的视觉编码器) |\\n| **Connector 类型** | 未公开（闭源） |\\n| LLM backbone | PaLI-X / PaLM-E |\\n| 开源状态 | ❌ **闭源**，权重不公开 |\\n| LIBERO 支持 | 不可行 |\\n| 改造成本 | 不可行 |\\n| 论文 LIBERO 结果 | 无 |\\n| 备注 | 闭源模型，无法使用 |\\n\\n### 5. GR-1 (ByteDance, 2023)\\n\\n| 字段 | 信息 |\\n|------|------|\\n| 参数量 | 未明确公布 |\\n| Vision encoder | MAE ViT-Base (预训练) |\\n| **Connector 类型** | **Perceiver Resampler**（将 MAE ViT 视觉 token 数量压缩）+ linear layers 对齐维度 |\\n| LLM backbone | GPT-style causal transformer（非预训练 LLM） |\\n| 开源状态 | ✅ weights + code, GitHub: [bytedance/GR-1](https://github.com/bytedance/GR-1), Apache-2.0 |\\n| LIBERO 支持 | 需改造（paper 只有 CALVIN） |\\n| 改造成本 | 高（需改 data pipeline、action space、视频生成部分可能要适配） |\\n| 论文 LIBERO 结果 | 无（CALVIN: 94.9%） |\\n| 备注 | 既做动作预测又做视频生成（future image prediction）。语言用 CLIP text encoder。使用 Perceiver Resampler 这一点很有价值——与 RoboFlamingo 类似但架构不同。 |\\n\\n### 6. GR-2 (ByteDance, 2024)\\n\\n| 字段 | 信息 |\\n|------|------|\\n| 参数量 | 未公布 |\\n| Vision encoder | 未公布 |\\n| **Connector 类型** | 未公布 |\\n| LLM backbone | 未公布 |\\n| 开源状态 | ❌ **未开源**，代码/权重未释放 |\\n| LIBERO 支持 | 不可行 |\\n| 改造成本 | 不可行 |\\n| 论文 LIBERO 结果 | 无 |\\n| 备注 | GR-1 的后续，但未开源 |\\n\\n### 7. LLARVA (2024)\\n\\n| 字段 | 信息 |\\n|------|------|\\n| 参数量 | 7B |\\n| Vision encoder | CLIP ViT-L/14 |\\n| **Connector 类型** | **MLP projector**（LLaVA-style，2-layer MLP with GELU） |\\n| LLM backbone | Llama-2 7B |\\n| 开源状态 | ✅ code + LoRA weights, GitHub: [Dantong88/LLARVA](https://github.com/Dantong88/LLARVA), Apache-2.0 |\\n| LIBERO 支持 | 需改造 |\\n| 改造成本 | 中（需接 action head + LIBERO data pipeline） |\\n| 论文 LIBERO 结果 | 无 |\\n| 备注 | 预测 visual traces (2D 轨迹) 作为中间表示。Connector 与 OpenVLA 类似（都是 MLP projector），但用 CLIP 而非 Prismatic 双 encoder |\\n\\n### 8. RoboVLMs (2024)\\n\\n| 字段 | 信息 |\\n|------|------|\\n| 参数量 | 不定（框架） |\\n| Vision encoder | 支持多种 VLM backbone |\\n| **Connector 类型** | 取决于所选 VLM（框架支持多种） |\\n| LLM backbone | 取决于所选 VLM |\\n| 开源状态 | ✅ code + models, GitHub: [Robot-VLAs/RoboVLMs](https://github.com/Robot-VLAs/RoboVLMs) |\\n| LIBERO 支持 | 需确认 |\\n| 改造成本 | 低-中（框架设计灵活） |\\n| 论文 LIBERO 结果 | 未确认 |\\n| 备注 | 这是一个**框架**而非单一模型。实验了 8+ VLM backbone × 4 policy 架构。最佳模型用 Kosmos backbone。对我们的 connector 对比研究有参考价值但不直接使用。 |\\n\\n### 9. 3D-VLA (UMass, ICML 2024)\\n\\n| 字段 | 信息 |\\n|------|------|\\n| 参数量 | 未明确 |\\n| Vision encoder | 3D feature extraction（point cloud based） |\\n| **Connector 类型** | **Interaction tokens**（3D-LLM 架构，用交互 token 嵌入 embodied 环境） |\\n| LLM backbone | 基于 3D-LLM |\\n| 开源状态 | ✅ code + diffusion models, GitHub: [UMass-Embodied-AGI/3D-VLA](https://github.com/UMass-Embodied-AGI/3D-VLA), HF: anyezhy |\\n| LIBERO 支持 | 需大量改造（paper 用 RLBench） |\\n| 改造成本 | 高（3D 点云输入，与 LIBERO 2D 图像差异大） |\\n| 论文 LIBERO 结果 | 无 |\\n| 备注 | 基于 3D 点云的 VLA，与我们研究的 2D 图像 → connector → LLM 管道差异太大，不推荐 |\\n\\n### 10. π0 / pi-zero (Physical Intelligence, 2024-2025)\\n\\n| 字段 | 信息 |\\n|------|------|\\n| 参数量 | ~3.3B (400M SigLIP + 2.6B Gemma + ~300M action expert) |\\n| Vision encoder | SigLIP-So400m (400M params) |\\n| **Connector 类型** | **Linear projection**（单层线性层，将 SigLIP token 投影到 Gemma embedding space） |\\n| LLM backbone | Gemma 2B (via PaliGemma) |\\n| 开源状态 | ✅ weights + code, GitHub: [Physical-Intelligence/openpi](https://github.com/Physical-Intelligence/openpi), HF 有 PyTorch port |\\n| LIBERO 支持 | ✅ 有评测（LIBERO-PRO 中被评测） |\\n| 改造成本 | 低（已有 LIBERO 评测代码） |\\n| 论文 LIBERO 结果 | 有（LIBERO-PRO 中有结果） |\\n| 备注 | **强力推荐**。Linear projection 是最简单的 connector，与 OpenVLA 的 2-layer MLP 形成鲜明对比。Action expert 通过 MoE 架构耦合。Flow matching 生成动作。 |\\n\\n### 11. OpenVLA-OFT (Stanford, 2025)\\n\\n| 字段 | 信息 |\\n|------|------|\\n| 参数量 | 7B |\\n| Vision encoder | SigLIP + DINOv2 (Prismatic) |\\n| **Connector 类型** | **2-layer MLP projector**（与 OpenVLA 相同的 Prismatic connector） |\\n| LLM backbone | Llama-2 7B |\\n| 开源状态 | ✅ weights + code, GitHub: [moojink/openvla-oft](https://github.com/moojink/openvla-oft) |\\n| LIBERO 支持 | ✅ 原生支持，SOTA 97.1% |\\n| 改造成本 | 极低（已有完整 LIBERO fine-tune + eval） |\\n| 论文 LIBERO 结果 | 有: 97.1% SR (4 suite avg) |\\n| 备注 | Connector 与 OpenVLA 完全相同。改进在 fine-tuning recipe（continuous actions, action chunking, bidirectional attention）。对压缩实验来说，connector 级别的差异与 OpenVLA 相同，但 action generation 方式不同，可能影响压缩行为。 |\\n\\n### 12. RoboMM (2024)\\n\\n| 字段 | 信息 |\\n|------|------|\\n| 参数量 | 未明确公布 |\\n| Vision encoder | CLIP (via OpenFlamingo) |\\n| **Connector 类型** | **3D Perception Adapter (UVFormer)** + **Cross-attention**（OpenFlamingo 风格：text queries attend to visual features through cross-attention layers） |\\n| LLM backbone | OpenFlamingo (cross-attention decoder) |\\n| 开源状态 | ✅ code, GitHub: [RoboUniview/RoboMM](https://github.com/RoboUniview/RoboMM) |\\n| LIBERO 支持 | ✅ 有评测 |\\n| 改造成本 | 低-中 |\\n| 论文 LIBERO 结果 | 有: 90.7% SR |\\n| 备注 | Cross-attention connector 是独特的融合方式（与 MLP/linear 的 \\\"先投射再拼接\\\" 不同）。还有 occupancy supervision 的 3D adapter。多模态解码器增强感知。 |\\n\\n### 13. SpatialVLA (2025, RSS)\\n\\n| 字段 | 信息 |\\n|------|------|\\n| 参数量 | ~4B |\\n| Vision encoder | SigLIP |\\n| **Connector 类型** | **Linear projection + Ego3D Position Encoding**（PaliGemma2 的 linear connector + MLP(sinusoidal(3D positions)) 叠加到 visual tokens 上） |\\n| LLM backbone | Gemma (via PaliGemma2) |\\n| 开源状态 | ✅ weights + code, GitHub: [SpatialVLA/SpatialVLA](https://github.com/SpatialVLA/SpatialVLA), HF: IPEC-COMMUNITY/spatialvla-4b-224-pt |\\n| LIBERO 支持 | 未确认 |\\n| 改造成本 | 中（需接 LIBERO data pipeline） |\\n| 论文 LIBERO 结果 | 无 |\\n| 备注 | 基于 PaliGemma2，connector 本质上是 linear projection（与 π0 相同），加了 3D spatial encoding。Adaptive Action Grids 只输出 3 个 action token（其他模型 7 个）。 |\\n\\n### 14. DeeR-VLA (2024)\\n\\n| 字段 | 信息 |\\n|------|------|\\n| 参数量 | 3B / 9B (OpenFlamingo 变体) |\\n| Vision encoder | CLIP ViT-L/14 (428M params) |\\n| **Connector 类型** | **Perceiver Resampler + Cross-attention**（OpenFlamingo 架构：CLIP features → Perceiver Resampler → learnable cross-attention blocks 注入 LLM 层间） |\\n| LLM backbone | MPT-1B (3B 版) / MPT-7B (9B 版) |\\n| 开源状态 | ✅ code + checkpoints, GitHub: [yueyang130/DeeR-VLA](https://github.com/yueyang130/DeeR-VLA) |\\n| LIBERO 支持 | 需改造（paper 只有 CALVIN） |\\n| 改造成本 | 中-高（需接 LIBERO pipeline，且多 exit 架构增加复杂度） |\\n| 论文 LIBERO 结果 | 无（CALVIN benchmark） |\\n| 备注 | **Perceiver Resampler** 与 RoboFlamingo 相同架构基础。动态 early exit 是额外功能。可作为 Perceiver Resampler 实验的替代方案。 |\\n\\n### 15. TraceVLA (UMD, ICLR 2025)\\n\\n| 字段 | 信息 |\\n|------|------|\\n| 参数量 | 7B (OpenVLA-based) / 4B (Phi-3-Vision-based) |\\n| Vision encoder | SigLIP + DINOv2 (OpenVLA 版) / CLIP ViT (Phi-3 版) |\\n| **Connector 类型** | **2-layer MLP projector**（与 OpenVLA 相同） |\\n| LLM backbone | Llama-2 7B (OpenVLA 版) / Phi-3 4B |\\n| 开源状态 | ✅ code + weights, GitHub: [umd-huang-lab/tracevla](https://github.com/umd-huang-lab/tracevla), HF: furonghuang-lab/tracevla_7b, MIT license |\\n| LIBERO 支持 | 未确认（SimplerEnv + 真机） |\\n| 改造成本 | 低（基于 OpenVLA 改造） |\\n| 论文 LIBERO 结果 | 无 |\\n| 备注 | Connector 与 OpenVLA 相同，改进在于 visual trace prompting（在图像上叠加动作历史轨迹）。压缩行为预期与 OpenVLA 相似。 |\\n\\n### 16. X-VLA (ICLR 2026)\\n\\n| 字段 | 信息 |\\n|------|------|\\n| 参数量 | 0.9B |\\n| Vision encoder | Florence-Large (DaViT) |\\n| **Connector 类型** | **Linear projection + Soft Prompts**（vision features 通过 lightweight linear layer 投影到高维空间 + 每个 embodiment 有独立 learnable prompt embeddings 注入 transformer） |\\n| LLM backbone | Standard transformer 24 layers (非预训练 LLM，但使用 Florence 预训练 VLM 初始化) |\\n| 开源状态 | ✅ weights + code, GitHub: [2toinf/X-VLA](https://github.com/2toinf/X-VLA), HF: 2toINF/X-VLA, Apache-2.0 |\\n| LIBERO 支持 | ✅ 原生支持，98% SR |\\n| 改造成本 | 极低（已有 LIBERO 训练权重） |\\n| 论文 LIBERO 结果 | 有: 98% SR |\\n| 备注 | **强力推荐**。Linear projection connector + flow matching action generation。LIBERO SOTA 之一。小模型(0.9B)便于实验。 |\\n\\n### 17. ECoT / Embodied Chain-of-Thought (2024)\\n\\n| 字段 | 信息 |\\n|------|------|\\n| 参数量 | 7B (基于 OpenVLA) |\\n| Vision encoder | SigLIP + DINOv2 (Prismatic) |\\n| **Connector 类型** | **2-layer MLP projector**（与 OpenVLA 相同） |\\n| LLM backbone | Llama-2 7B |\\n| 开源状态 | ✅ code + weights, GitHub: [MichalZawalski/embodied-CoT](https://github.com/MichalZawalski/embodied-CoT), HF: ecot-openvla-7b-bridge/oxe |\\n| LIBERO 支持 | 需改造 |\\n| 改造成本 | 低（基于 OpenVLA） |\\n| 论文 LIBERO 结果 | 无 |\\n| 备注 | Connector 与 OpenVLA 完全相同，增加了 chain-of-thought reasoning。对 connector 压缩研究无新增价值。 |\\n\\n### 18. LingBot-VLA (Ant Group/Robbyant, 2026)\\n\\n| 字段 | 信息 |\\n|------|------|\\n| 参数量 | 4B |\\n| Vision encoder | Qwen2.5-VL 的 ViT（2D-RoPE + window attention） |\\n| **Connector 类型** | **MLP merger**（2-layer MLP with ReLU，2×2 spatial grouping 后投影 + LLM decoder 中有 cross-attention 层融合 visual features） |\\n| LLM backbone | Qwen2.5-VL-3B |\\n| 开源状态 | ✅ weights + code, GitHub: [Robbyant/lingbot-vla](https://github.com/Robbyant/lingbot-vla) |\\n| LIBERO 支持 | 未确认 |\\n| 改造成本 | 中 |\\n| 论文 LIBERO 结果 | 未确认 |\\n| 备注 | Qwen2.5-VL 的 MLP merger 是一种混合 connector：先做 spatial grouping（类似 pixel-shuffle 的空间压缩）再 MLP 投射。Mixture of Transformers 架构。 |\\n\\n---\\n\\n## Connector 类型覆盖分析\\n\\n### 已有数据的 Connector 类型\\n| Connector 类型 | 代表模型 | 压缩行为 |\\n|---------------|----------|----------|\\n| Pixel-shuffle | SmolVLA | Cliff-edge collapse |\\n| 2-layer MLP projector | OpenVLA (Prismatic) | Graded degradation |\\n| Perceiver Resampler | RoboFlamingo | 尝试失败 |\\n| **Linear projection** | **X-VLA** | **Nearly lossless pruning** |\\n\\n### 可新增的 Connector 类型\\n| Connector 类型 | 候选模型 | 特点 | 可行性 |\\n|---------------|----------|------|--------|\\n| **Linear projection** | **π0**, SpatialVLA | 验证 X-VLA 发现的一致性 | ⭐⭐⭐ 高 |\\n| **Cross-attention (Flamingo-style)** | **RoboMM** | 不在 encoder 端压缩，而是 decoder 端通过 cross-attention 选择性融合 | ⭐⭐ 中 |\\n| **CNN patch → direct concat** | Octo | 无独立 connector，图像 patches 直接拼入 transformer | ⭐ 低（架构差异太大） |\\n| **MLP merger + spatial grouping** | LingBot-VLA | 先空间合并再 MLP 投射 + cross-attention | ⭐⭐ 中 |\\n| **Cross-attention tokenizer** | HPT | learnable tokens 通过 cross-attention 聚合 vision features | ⭐ 低（非 VLM 架构） |\\n\\n### 关键发现\\n1. **Linear projection** 是最有价值的新增类型——π0 和 X-VLA 都用这种最简单的 connector，与 OpenVLA 的 2-layer MLP 形成对比\\n2. **Cross-attention** (RoboMM 的 OpenFlamingo 架构) 从根本上不同：不投射拼接，而是 decoder 层间交叉注意力\\n3. 大量模型共享 connector：OpenVLA, CogACT, LLARVA, TraceVLA, ECoT, OpenVLA-OFT 都用 **2-layer MLP**（Prismatic 或 LLaVA 架构）\\n\\n---\\n\\n## Top 推荐：最适合扩展实验的 5 个模型\\n\\n### 🥇 1. π0 (Physical Intelligence)\\n- **Connector**: Linear projection (单层线性)\\n- **推荐理由**: \\n  - 与 OpenVLA 的 2-layer MLP 形成直接对比（linear vs MLP）\\n  - 开源权重 + 代码，社区活跃\\n  - 已有 LIBERO 评测代码\\n  - PaliGemma 架构广为人知\\n  - 3B 参数可在单卡运行\\n- **预期价值**: Linear projection 不增加非线性变换，token 可能保留更多原始 visual feature 结构 → 压缩行为可能与 MLP 不同\\n\\n### 🥈 2. X-VLA\\n- **Connector**: Linear projection + soft prompts\\n- **推荐理由**:\\n  - 同样是 linear projection，与 π0 对比看 soft prompt 的影响\\n  - LIBERO 98% SR，已有训练好的 LIBERO 权重直接可用\\n  - 0.9B 参数，实验成本最低\\n  - ICLR 2026，最新模型\\n  - Apache-2.0 开源\\n- **预期价值**: 验证 linear projection 的压缩行为是否 consistent across models\\n\\n### 🥉 3. DeeR-VLA\\n- **Connector**: Perceiver Resampler + Cross-attention (OpenFlamingo)\\n- **推荐理由**:\\n  - Perceiver Resampler 与 RoboFlamingo 相同架构，但 DeeR-VLA 已验证可训练（CALVIN benchmark 正常工作）\\n  - 给 Perceiver Resampler 第二次机会\\n  - 可对比 RoboFlamingo 的训练失败是架构问题还是实现问题\\n  - Open source with checkpoints\\n- **预期价值**: Perceiver Resampler 本身就做了 attention-based compression → 压缩行为可能与 MLP/linear 截然不同\\n- **风险**: LIBERO 需要自己改造\\n\\n### 4. RoboMM\\n- **Connector**: Cross-attention (OpenFlamingo) + 3D Adapter\\n- **推荐理由**:\\n  - Cross-attention 融合方式从根本上不同于 projection-based connectors\\n  - 已有 LIBERO 结果 (90.7%)\\n  - Open source\\n- **预期价值**: Cross-attention 在 decoder 端动态选择 visual features → 可能展现出与 projection-based 完全不同的压缩模式\\n- **风险**: 架构较复杂，3D adapter 增加变量\\n\\n### 5. OpenVLA-OFT\\n- **Connector**: 2-layer MLP projector (与 OpenVLA 相同)\\n- **推荐理由**:\\n  - Connector 与 OpenVLA 相同，但 action generation 完全不同（continuous + chunking）\\n  - LIBERO 97.1% SOTA\\n  - 可验证 \\\"相同 connector + 不同 action head\\\" 是否影响压缩行为\\n  - 已有完整 LIBERO 代码\\n- **预期价值**: 作为 OpenVLA 的对照组，隔离 connector vs action head 对压缩的影响\\n\\n---\\n\\n## 不推荐的模型及原因\\n\\n| 模型 | 排除原因 |\\n|------|----------|\\n| RT-2-X | 闭源，权重不可用 |\\n| GR-2 | 未开源 |\\n| 3D-VLA | 3D 点云输入，与 2D VLA 差异太大 |\\n| CogACT | Connector 与 OpenVLA 相同（Prismatic MLP），不新增类型 |\\n| LLARVA | Connector 与 OpenVLA 类似（MLP projector），不新增类型 |\\n| TraceVLA | Connector 与 OpenVLA 相同，不新增类型 |\\n| ECoT | Connector 与 OpenVLA 相同，不新增类型 |\\n| HPT | 非 VLM 架构，不适合 connector 压缩叙事 |\\n| GR-1 | 有 Perceiver Resampler（有价值），但无 LIBERO 支持 + 视频生成架构改造成本高 |\\n| Octo | 无独立 connector（CNN patch 直接拼入），架构与标准 VLM 差异太大 |\\n\\n---\\n\\n## 总结：Connector 类型 × 模型矩阵\\n\\n| Connector 类型 | 已有 | 推荐新增 |\\n|---------------|------|----------|\\n| Pixel-shuffle | SmolVLA ✅ | — |\\n| 2-layer MLP projector | OpenVLA ✅ | OpenVLA-OFT（同 connector 不同 action head） |\\n| Perceiver Resampler | RoboFlamingo ❌(失败) | **DeeR-VLA** |\\n| **Linear projection** | **X-VLA ✅** | **π0** |\\n| **Cross-attention** | — | **RoboMM** |\\n\\n实现后可达 **5 种 connector 类型 × 6+ 模型**的全面对比。\\n\\n---\\n\\n## X-VLA 详细架构调研（2026-05-20 新增）\\n\\n### 模型身份确认\\n- **名称**: X-VLA (Soft-Prompted Transformer as Scalable Cross-Embodiment Vision-Language-Action Model)\\n- **论文**: arXiv:2510.10274, ICLR 2026\\n- **GitHub**: [2toinf/X-VLA](https://github.com/2toinf/X-VLA)\\n- **HuggingFace**: [2toINF/X-VLA](https://huggingface.co/collections/2toINF/x-vla)\\n- **参数量**: 0.9B\\n- **许可**: Apache-2.0\\n- **LIBERO SR**: 98.1%\\n\\n### 架构详解\\n\\n```\\nImage (224×224) → Florence-Large (DaViT) → Vision Tokens [B, N, 2048]\\n    → Linear Projection + LayerNorm → [B, N, 1024]\\n    → Merge with Text Token Embeddings → Florence2 Encoder (self-attention)\\n    → Context Features → SoftPromptedTransformer (24 layers, hidden=1024)\\n        + Soft Prompts (32 learnable embeddings per embodiment)\\n        + Noised Action Tokens (flow matching)\\n    → Denoised Action Trajectory [B, 30, 20]\\n```\\n\\n**各组件详情**:\\n\\n| 组件 | 规格 |\\n|------|------|\\n| Vision Encoder | Florence-Large (DaViT): patch_stride=[4,2,2,2] → total stride 32 |\\n| Vision Token 数量 | ~49 tokens (7×7 at 224×224) 或 ~576 tokens (24×24 at 768×768) — **需实际加载模型验证** |\\n| Projection | Linear + LayerNorm, dim 2048 → 1024 (projection_dim=1024) |\\n| Soft Prompts | 32 tokens/embodiment, 0.04% of total params |\\n| Transformer | 24 layers, hidden=1024, 16 heads, mlp_ratio=4.0 |\\n| Action Head | Flow matching, 30 anchor points × 20 dims (EE6D), 10 denoising steps |\\n| Max Sequence | 512 tokens |\\n\\n### HuggingFace 权重\\n| Checkpoint | 用途 | 地址 |\\n|------------|------|------|\\n| X-VLA-Pt | 预训练基座 (cross-embodiment) | 2toINF/X-VLA-Pt |\\n| X-VLA-Libero | LIBERO 全参数微调 (98.1% SR) | 2toINF/X-VLA-Libero |\\n| X-VLA-libero-*-peft | LIBERO LoRA 微调 (各 suite) | 2toINF/X-VLA-libero-spatial-peft 等 |\\n\\n### 环境依赖\\n```\\ntransformers<=4.51.3, torch, einops==0.8.1, timm==1.0.12, \\naccelerate==1.2.1, peft==0.17.1, safetensors==0.4.5,\\nnumpy==1.26.3, scipy==1.15.0, mmengine==0.10.5,\\nfastapi, uvicorn==0.34.3, h5py==3.12.1, pyarrow==20.0.0,\\nav==15.0.0, mediapy==1.2.4\\n```\\nLIBERO 评估另需 Python 3.8 环境。\\n\\n### VTC 集成方案\\n**插入点**: Florence2 `_encode_image()` 输出 → **VTC** → `_merge_input_ids_with_image_features()`\\n\\n**改造清单**:\\n1. 创建 `xvla_vtc_adapter.py`（复用 VisionTokenCompressor，hidden_dim 改 1024）\\n2. 创建 XVLASmartCompressWrapper，hook Florence2 vision 输出\\n3. 修改 merge 逻辑以适应压缩后的 token 数量\\n4. 创建 `train_xvla_smart_compress.py`（参考 X-VLA 的 train.py + peft_train.py）\\n5. 适配 flow matching loss（不同于 OpenVLA 的 cross-entropy）\\n\\n**与 OpenVLA VTC 的关键差异**:\\n| 维度 | OpenVLA | X-VLA |\\n|------|---------|-------|\\n| hidden_dim | 4096 | 1024 |\\n| 原始 vision tokens | 256 | ~49-576 (待验证) |\\n| Action 范式 | Autoregressive (256-bin CE) | Flow matching (MSE+BCE) |\\n| Connector | 2-layer MLP | Linear + LayerNorm |\\n| 模型大小 | 7B | 0.9B |\\n\\n**预计工作量**: 8-12 小时\\n- 代码改造: 4-6h（adapter + training script）\\n- 环境搭建 + 模型下载: 2-3h\\n- 验证 + 调试: 2-3h\\n\\n---\\n\\n## X-VLA Token Importance 分析结果（2026-05-20）\\n\\n### 实验配置\\n- **模型**: X-VLA-0.9B (lerobot/xvla-libero checkpoint)\\n- **数据**: LIBERO-Object (task_index 20-29), 100 images, 10 tasks\\n- **服务器**: westd-41074, cuda:1\\n- **分析脚本**: `/root/autodl-tmp/importance_margin_vla_compress/analyze_xvla_token_importance.py`\\n- **结果文件**: `/root/autodl-tmp/importance_margin_vla_compress/eval_results/xvla_attention_entropy_perlayer.json`\\n\\n### SoftPromptedTransformer 序列布局\\n| Token 类型 | 数量 | 说明 |\\n|-----------|------|------|\\n| Action tokens | 30 | Flow matching denoised action |\\n| VLM features | 64 | Florence2 encoder output (main view) |\\n| Aux visual | 150 | Additional camera views |\\n| Soft prompts | 32 | Embodiment-specific learnable tokens |\\n| **Total** | **276** | |\\n\\n### Entropy Ratio（Action→Vision 注意力熵）\\n- **Overall**: **0.6138** ± 0.1159\\n- **趋势**: 浅层低（L0=0.46, L1=0.34），深层高（L22=0.79, L23=0.71）\\n- 浅层集中注意力于少数 vision tokens，深层趋于均匀\\n\\n### Vision Attention Fraction（Action tokens 分配给 vision tokens 的注意力比例）\\n- 浅层（L0-2）: 33-49% — action tokens 还关注 soft prompts 和 self\\n- 中层（L6-11）: 84-90% — 绝大部分注意力给 vision tokens\\n- 深层（L17-23）: 79-90% — 持续高注意力\\n\\n### Pruning Curve（核心发现）\\n| Retention k | Mean Loss | Normalized |\\n|-------------|-----------|------------|\\n| 0.30 | 0.112945 | **1.0014** |\\n| 0.50 | 0.112823 | 1.0003 |\\n| 0.70 | 0.112789 | 1.0000 |\\n| 0.90 | 0.112789 | 1.0000 |\\n| 0.95 | 0.112789 | 1.0000 |\\n| 1.00 | 0.112789 | 1.0000 |\\n\\n**关键结论**: 丢弃 70% 的 vision tokens（k=0.3）仅导致 0.14% 的 loss 增加。X-VLA 的 vision tokens **几乎完全可压缩**。\\n\\n### 跨模型对比\\n| 模型 | Connector | Entropy Ratio | k=0.3 Norm Loss | 压缩行为 |\\n|------|-----------|---------------|-----------------|----------|\\n| SmolVLA | Pixel-shuffle | ~0.45 (低) | Cliff-edge | 不可压缩 |\\n| OpenVLA | 2-layer MLP | ~0.55 (中) | ~1.15 (15%↑) | 渐进退化 |\\n| **X-VLA** | **Linear proj** | **0.61 (中高)** | **1.0014 (0.14%↑)** | **几乎无损** |\\n\\n### 解读\\n1. **Linear projection connector 产生了高度冗余的 vision token 表示**——大部分信息集中在少数 token 中，L2 norm 可以轻松识别\\n2. Entropy 比 OpenVLA 更高（0.61 vs 0.55），说明注意力分布更均匀，但这不矛盾——均匀分布意味着 \\\"每个 token 被平等关注\\\"，而 pruning 几乎无损意味着 \\\"被关注的内容高度冗余\\\"\\n3. 这是 **connector 架构论文的关键数据点**：linear projection（无非线性变换）保留了 DaViT 输出的原始冗余结构，而 MLP projector（2 层 + GELU）通过非线性变换重新分配了信息，使得 token 间差异更大、更难压缩\\n\\n---\\n\\n## OFT Importance CV 分析结果（2026-05-20）\\n\\n### 结论\\n- **OFT CV = 0.2185**，per-task CV 在 0.211–0.225 之间\\n- 与 OpenVLA (0.215) 高度一致——两者共享相同的 2-layer MLP projector（Prismatic 架构）\\n- **LoRA fine-tuning 不改变 vision token importance 分布**——connector 架构是唯一决定因素\\n\\n### Diagnostic 表格完成状态（5/5）\\n| 模型 | Connector | CV | 压缩行为 |\\n|------|-----------|-----|----------|\\n| SmolVLA | Pixel-shuffle | ~0.08 | Cliff-edge collapse |\\n| OpenVLA | 2-layer MLP | 0.215 | Graded degradation |\\n| OpenVLA-OFT | 2-layer MLP (same) | 0.2185 | 预期与 OpenVLA 相同 |\\n| X-VLA | Linear projection | TBD | Nearly lossless |\\n| RoboFlamingo | Perceiver Resampler | N/A | 训练失败 |\\n\\n### 论文意义\\nOFT 结果支撑 claim: \\\"token importance distribution is an intrinsic property of the connector architecture, invariant to downstream fine-tuning strategy (LoRA vs full)\\\"\\n\\n---\\n\\n## 失败模式记录\\n\\n- [2026-05-21] **π0.5 自定义 eval 脚本 bug**: `eval_pi05_pruning_libero.py` 的 `patched_embed_image` 函数导致 0% SR，而官方 eval 脚本在同一 checkpoint 上 ~100% SR。→ 新模型接入时，必须先用官方 eval 脚本验证 checkpoint 可用性，确认后再写自定义 pruning eval 脚本。不要假设自定义 patch 正确。\\n\\n- [2026-05-21] **OpenVLA eval 4 实验批量失败 (westd-38929)**:\\n  - **失败实验**: eval_openvla_l2norm_k05_object_seed42 (PID 568225), eval_openvla_random_k03_object_seed42 (PID 568905), eval_openvla_l2norm_k07_object_seed42 (PID 569611), eval_openvla_l2norm_k03_object_seed42 (PID 570309)\\n  - **根因**: **AutoDL 容器 GPU 缩配**。主机有 9 块 NVIDIA RTX PRO 6000 Blackwell (各 97GB)，但容器当前只挂载了 `/dev/nvidia2` 一块 GPU。4 个实验分别在 CUDA_VISIBLE_DEVICES=0/1/2/3 启动，运行 ~1h43m 后 GPU 设备被平台回收，进程收到 SIGKILL 无任何 traceback。\\n  - **证据**:\\n    - `nvidia-smi -L` 只显示 1 块 GPU (Device Minor 2)，而 `/proc/driver/nvidia/gpus/` 显示主机有 9 块\\n    - 4 个日志文件在 14:45-14:49 间依次停止写入（3 分钟跨度，非瞬时），末尾均为正常进度输出无 error\\n    - 各实验完成了 Task 1-3，在 Task 4/10 中被杀（~30% 完成度）\\n    - 系统 RAM 充足（1TB 中仅用 46GB），排除 CPU OOM\\n    - 无 tmux session，进程通过 nohup 方式运行\\n  - **修复建议**:\\n    1. 在 AutoDL 控制台恢复实例到 4 GPU 配置（或至少确认 GPU 分配稳定）\\n    2. 重新启动 4 个实验，建议使用 tmux 以防 SSH 断连\\n    3. 如果无法恢复多 GPU，可在单 GPU 上顺序运行（每个实验约 5.5h，共 ~22h）\\n    4. 启动命令参考（单 GPU 顺序）:\\n       ```bash\\n       tmux new -s openvla_eval\\n       source /root/miniconda3/etc/profile.d/conda.sh && conda activate base\\n       cd /root/autodl-tmp/importance_margin_vla_compress\\n       CUDA_VISIBLE_DEVICES=0 python -u eval_openvla_l2norm_libero.py --mode l2norm_prune --k_ratio 0.5 --suite libero_object --seed 42 > logs/eval_openvla_l2norm_k05_seed42.log 2>&1\\n       CUDA_VISIBLE_DEVICES=0 python -u eval_openvla_l2norm_libero.py --mode random_prune --k_ratio 0.3 --suite libero_object --seed 42 > logs/eval_openvla_random_k03_seed42.log 2>&1\\n       CUDA_VISIBLE_DEVICES=0 python -u eval_openvla_l2norm_libero.py --mode l2norm_prune --k_ratio 0.7 --suite libero_object --seed 42 > logs/eval_openvla_l2norm_k07_seed42.log 2>&1\\n       CUDA_VISIBLE_DEVICES=0 python -u eval_openvla_l2norm_libero.py --mode l2norm_prune --k_ratio 0.3 --suite libero_object --seed 42 > logs/eval_openvla_l2norm_k03_seed42.log 2>&1\\n       ```\\n\\n---\\n\\n## π0.5 跨 suite 对比（2026-05-21）\\n\\n**模型**: π0.5 (PaliGemma, linear projection connector, CV=0.055)\\n**数据来源**: registry 中所有 status=DONE 且有有效 metrics 的 pi05 实验\\n\\n### Object Suite（baseline=98.2%, eval_pi05_baseline_object_seed42）\\n\\n| k | L2norm SR (%) | L2norm exp_ids | Random SR (%) | Random exp_ids |\\n|---|--------------|----------------|--------------|----------------|\\n| 0.9 | **98.2** (s42) | eval_pi05_l2norm_k09_object_seed42_v2 | **10.8** avg [12.0(s42), 9.6(s43)] | eval_pi05_random_k09_object_seed42_v2, eval_pi05_random_k09_object_seed43 |\\n| 0.7 | **56.4** avg [55.0(s42), 56.4(s43), 57.8(s43v2)] | eval_pi05_l2norm_k07_object_seed42, _seed43, _seed43_v2 | **75.5** avg [77.2(s42), 73.8(s43)] | eval_pi05_random_k07_object_seed42, _seed43 |\\n| 0.5 | **33.5** avg [33.4(s42), 33.6(s43)] | eval_pi05_l2norm_k05_object_seed42, _seed43 | **68.9** avg [69.4(s42), 68.4(s43)] | eval_pi05_random_k05_object_seed42, _seed43 |\\n| 0.3 | **53.2** avg [51.0(s42), 55.4(s43)] | eval_pi05_l2norm_k03_object_seed42, _seed43 | **36.4** (s42) | eval_pi05_random_k03_object_seed42 |\\n| 0.1 | **2.6** (s42) | eval_pi05_l2norm_k01_object_seed42 | — | — |\\n\\n### Spatial Suite（baseline=97.2%, eval_pi05_baseline_spatial_seed42）\\n\\n| k | L2norm SR (%) | Random SR (%) | Random exp_ids |\\n|---|--------------|--------------|----------------|\\n| 0.9 | — (pending) | — (pending) | — |\\n| 0.7 | — (pending) | — (submitted) | — |\\n| 0.5 | — (running) | **71.6** (s42) | eval_pi05_random_k05_spatial_seed42 |\\n| 0.3 | — (running) | — (submitted) | — |\\n\\n### Cross-suite 一致性分析\\n\\n**Random k=0.5 对比**:\\n- Object: **68.9%** (seed42=69.4%, seed43=68.4%)\\n- Spatial: **71.6%** (seed42)\\n- **Delta: 2.7pp** — 高度一致\\n\\n结论：Random pruning 在 k=0.5 的表现跨 suite 具有强一致性（差异仅 2.7pp），说明 π0.5 的 vision token 冗余结构不依赖于具体 task 类型。Spatial 略高于 Object 可能因为 Spatial 任务（同一物体不同位置）对视觉信息量要求更低。\\n\\n### 关键现象\\n\\n1. **L2norm 非单调 V-shape**：k=0.5 是谷底(33.5%)，k=0.3 反弹到 53.2%。多 seed 确认。原因待查——可能 L2 norm 在 50% 保留时恰好选中了信息量最差的 token 子集。\\n\\n2. **Random k=0.9 异常崩塌**：仅保留 90% token 时 random pruning SR 降至 ~10.8%（双 seed 确认 12.0%/9.6%），而 L2norm k=0.9 正常(98.2%)。这是所有模型中未见过的现象——移除 10% random token 即可摧毁模型。推测 π0.5 少数 token 承载关键位置信息，random 删除有 ~90% 概率命中关键 token。\\n\\n3. **Random 优于 L2norm 的 k 区间**：k=0.5(random 68.9% vs L2norm 33.5%)和 k=0.7(random 75.5% vs L2norm 56.4%)时 random 大幅优于 L2norm。说明 L2 norm 不是 π0.5 vision token importance 的好 proxy——CV=0.055 意味着 L2 norm 几乎无区分度。\\n\\n4. **Failed/killed 实验（已排除）**: eval_pi05_random_k07_object_seed42_v2(killed), _v3(killed), eval_pi05_random_k085_object_seed42(failed), eval_pi05_random_k095_object_seed42(failed), eval_pi05_random_k09_fixedmask_object_seed42(network error)。\\n\", \"total_chars\": 25431, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
````

</details>

<details><summary>Recorded metadata</summary>

````json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "bcd9e5e6-c86c-4bf9-9402-037b79b77b15",
  "uuid": "0e26cb2c-c9c8-4c8f-ab63-931c5a52cbde",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"path\\\": \\\"/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/memory.md\\\", \\\"content\\\": \\\"# VLA 模型全面调研报告\\\\n\\\\n**调研日期**: 2026-05-20\\\\n**目的**: 寻找不同 connector 架构的开源 VLA 模型，扩展 vision connector 对 token 可压缩性影响的实验\\\\n\\\\n---\\\\n\\\\n## 已有实验数据\\\\n\\\\n| 模型 | Connector | 压缩行为 |\\\\n|------|-----------|----------|\\\\n| SmolVLA | Pixel-shuffle | Cliff-edge collapse (k=0.95 → 0% SR) |\\\\n| OpenVLA | 2-layer MLP projector | Graded degradation (线性下降) |\\\\n| RoboFlamingo | Perceiver Resampler | 尝试失败（gripper loss 无法训练） |\\\\n| **X-VLA** | **Linear projection** | **Nearly lossless (k=0.3 → norm=1.0014)** |\\\\n\\\\n---\\\\n\\\\n## 完整模型调研表\\\\n\\\\n### 1. Octo (UC Berkeley, 2024)\\\\n\\\\n| 字段 | 信息 |\\\\n|------|------|\\\\n| 参数量 | 27M (Small) / 93M (Base) |\\\\n| Vision encoder | Shallow CNN (从头训练，非预训练 ViT) |\\\\n| **Connector 类型** | **CNN patch encoder → 直接拼接进 transformer（无独立 connector）** |\\\\n| LLM backbone | 纯 transformer（非预训练 LLM），decoder-only |\\\\n| 开源状态 | ✅ weights + code, GitHub: [octo-models/octo](https://github.com/octo-models/octo), HF: rail-berkeley/octo-base |\\\\n| LIBERO 支持 | ✅ 原生支持，fine-tune 后 ~72% SR |\\\\n| 改造成本 | 低（已有 LIBERO fine-tune 代码） |\\\\n| 论文 LIBERO 结果 | 有: ~72% (fine-tuned) |\\\\n| 备注 | 非标准 VLM→LLM 架构，是 transformer-based diffusion policy。图像通过浅层 CNN 编码为 16×16 patches 后直接拼入 transformer 序列。语言用 T5 tokenizer/encoder。Action head 是 diffusion policy。 |\\\\n\\\\n### 2. CogACT (Microsoft/Tsinghua, 2024)\\\\n\\\\n| 字段 | 信息 |\\\\n|------|------|\\\\n| 参数量 | ~7.1B (7B Prismatic VLM + 89M-300M DiT action module) |\\\\n| Vision encoder | DINOv2 + SigLIP (双 encoder，channel 拼接) |\\\\n| **Connector 类型** | **2-layer MLP projector**（Prismatic 架构：DINOv2+SigLIP feature → channel concat → 2-layer MLP → Llama-2 embedding space） |\\\\n| LLM backbone | Llama-2 7B (via Prismatic-7B) |\\\\n| 开源状态 | ✅ weights + code, GitHub: [microsoft/CogACT](https://github.com/microsoft/CogACT), HF: CogACT/CogACT-Base, CogACT/CogACT-Small |\\\\n| LIBERO 支持 | 需改造（paper 用 SimplerEnv + 真机） |\\\\n| 改造成本 | 中（需接 LIBERO data pipeline + action space） |\\\\n| 论文 LIBERO 结果 | 无 |\\\\n| 备注 | 核心创新在 DiT action module（将 VLM 认知特征作为 condition 输入扩散 transformer 生成动作）。Connector 与 OpenVLA 相同（都基于 Prismatic） |\\\\n\\\\n### 3. HPT (MIT, NeurIPS 2024)\\\\n\\\\n| 字段 | 信息 |\\\\n|------|------|\\\\n| 参数量 | 3.1M (S) / 12.6M (B) / 50.5M (L) / 226.8M (XL) / 1.1B (Huge) |\\\\n| Vision encoder | 预训练冻结 ResNet18 |\\\\n| **Connector 类型** | **Cross-attention tokenizer**（learnable tokens 通过 cross-attention 聚合 vision features → 固定 16 tokens，每个 camera view 有独立 MLP projector） |\\\\n| LLM backbone | 无（纯 decoder-only transformer，从头训练） |\\\\n| 开源状态 | ✅ weights + code, GitHub: [liruiw/HPT](https://github.com/liruiw/HPT), HF: liruiw/hpt |\\\\n| LIBERO 支持 | 未确认（paper 评测 6 个 benchmark） |\\\\n| 改造成本 | 中（非标准 VLM 架构，需改 stem + action head） |\\\\n| 论文 LIBERO 结果 | 无 |\\\\n| 备注 | 非 VLM→LLM 架构。Cross-attention tokenizer 类似 Perceiver 但更轻量（8 heads, 64 dim/head）。跨 embodiment 预训练。 |\\\\n\\\\n### 4. RT-2-X (Google DeepMind, 2023)\\\\n\\\\n| 字段 | 信息 |\\\\n|------|------|\\\\n| 参数量 | 55B |\\\\n| Vision encoder | ViT (PaLI-X 的视觉编码器) |\\\\n| **Connector 类型** | 未公开（闭源） |\\\\n| LLM backbone | PaLI-X / PaLM-E |\\\\n| 开源状态 | ❌ **闭源**，权重不公开 |\\\\n| LIBERO 支持 | 不可行 |\\\\n| 改造成本 | 不可行 |\\\\n| 论文 LIBERO 结果 | 无 |\\\\n| 备注 | 闭源模型，无法使用 |\\\\n\\\\n### 5. GR-1 (ByteDance, 2023)\\\\n\\\\n| 字段 | 信息 |\\\\n|------|------|\\\\n| 参数量 | 未明确公布 |\\\\n| Vision encoder | MAE ViT-Base (预训练) |\\\\n| **Connector 类型** | **Perceiver Resampler**（将 MAE ViT 视觉 token 数量压缩）+ linear layers 对齐维度 |\\\\n| LLM backbone | GPT-style causal transformer（非预训练 LLM） |\\\\n| 开源状态 | ✅ weights + code, GitHub: [bytedance/GR-1](https://github.com/bytedance/GR-1), Apache-2.0 |\\\\n| LIBERO 支持 | 需改造（paper 只有 CALVIN） |\\\\n| 改造成本 | 高（需改 data pipeline、action space、视频生成部分可能要适配） |\\\\n| 论文 LIBERO 结果 | 无（CALVIN: 94.9%） |\\\\n| 备注 | 既做动作预测又做视频生成（future image prediction）。语言用 CLIP text encoder。使用 Perceiver Resampler 这一点很有价值——与 RoboFlamingo 类似但架构不同。 |\\\\n\\\\n### 6. GR-2 (ByteDance, 2024)\\\\n\\\\n| 字段 | 信息 |\\\\n|------|------|\\\\n| 参数量 | 未公布 |\\\\n| Vision encoder | 未公布 |\\\\n| **Connector 类型** | 未公布 |\\\\n| LLM backbone | 未公布 |\\\\n| 开源状态 | ❌ **未开源**，代码/权重未释放 |\\\\n| LIBERO 支持 | 不可行 |\\\\n| 改造成本 | 不可行 |\\\\n| 论文 LIBERO 结果 | 无 |\\\\n| 备注 | GR-1 的后续，但未开源 |\\\\n\\\\n### 7. LLARVA (2024)\\\\n\\\\n| 字段 | 信息 |\\\\n|------|------|\\\\n| 参数量 | 7B |\\\\n| Vision encoder | CLIP ViT-L/14 |\\\\n| **Connector 类型** | **MLP projector**（LLaVA-style，2-layer MLP with GELU） |\\\\n| LLM backbone | Llama-2 7B |\\\\n| 开源状态 | ✅ code + LoRA weights, GitHub: [Dantong88/LLARVA](https://github.com/Dantong88/LLARVA), Apache-2.0 |\\\\n| LIBERO 支持 | 需改造 |\\\\n| 改造成本 | 中（需接 action head + LIBERO data pipeline） |\\\\n| 论文 LIBERO 结果 | 无 |\\\\n| 备注 | 预测 visual traces (2D 轨迹) 作为中间表示。Connector 与 OpenVLA 类似（都是 MLP projector），但用 CLIP 而非 Prismatic 双 encoder |\\\\n\\\\n### 8. RoboVLMs (2024)\\\\n\\\\n| 字段 | 信息 |\\\\n|------|------|\\\\n| 参数量 | 不定（框架） |\\\\n| Vision encoder | 支持多种 VLM backbone |\\\\n| **Connector 类型** | 取决于所选 VLM（框架支持多种） |\\\\n| LLM backbone | 取决于所选 VLM |\\\\n| 开源状态 | ✅ code + models, GitHub: [Robot-VLAs/RoboVLMs](https://github.com/Robot-VLAs/RoboVLMs) |\\\\n| LIBERO 支持 | 需确认 |\\\\n| 改造成本 | 低-中（框架设计灵活） |\\\\n| 论文 LIBERO 结果 | 未确认 |\\\\n| 备注 | 这是一个**框架**而非单一模型。实验了 8+ VLM backbone × 4 policy 架构。最佳模型用 Kosmos backbone。对我们的 connector 对比研究有参考价值但不直接使用。 |\\\\n\\\\n### 9. 3D-VLA (UMass, ICML 2024)\\\\n\\\\n| 字段 | 信息 |\\\\n|------|------|\\\\n| 参数量 | 未明确 |\\\\n| Vision encoder | 3D feature extraction（point cloud based） |\\\\n| **Connector 类型** | **Interaction tokens**（3D-LLM 架构，用交互 token 嵌入 embodied 环境） |\\\\n| LLM backbone | 基于 3D-LLM |\\\\n| 开源状态 | ✅ code + diffusion models, GitHub: [UMass-Embodied-AGI/3D-VLA](https://github.com/UMass-Embodied-AGI/3D-VLA), HF: anyezhy |\\\\n| LIBERO 支持 | 需大量改造（paper 用 RLBench） |\\\\n| 改造成本 | 高（3D 点云输入，与 LIBERO 2D 图像差异大） |\\\\n| 论文 LIBERO 结果 | 无 |\\\\n| 备注 | 基于 3D 点云的 VLA，与我们研究的 2D 图像 → connector → LLM 管道差异太大，不推荐 |\\\\n\\\\n### 10. π0 / pi-zero (Physical Intelligence, 2024-2025)\\\\n\\\\n| 字段 | 信息 |\\\\n|------|------|\\\\n| 参数量 | ~3.3B (400M SigLIP + 2.6B Gemma + ~300M action expert) |\\\\n| Vision encoder | SigLIP-So400m (400M params) |\\\\n| **Connector 类型** | **Linear projection**（单层线性层，将 SigLIP token 投影到 Gemma embedding space） |\\\\n| LLM backbone | Gemma 2B (via PaliGemma) |\\\\n| 开源状态 | ✅ weights + code, GitHub: [Physical-Intelligence/openpi](https://github.com/Physical-Intelligence/openpi), HF 有 PyTorch port |\\\\n| LIBERO 支持 | ✅ 有评测（LIBERO-PRO 中被评测） |\\\\n| 改造成本 | 低（已有 LIBERO 评测代码） |\\\\n| 论文 LIBERO 结果 | 有（LIBERO-PRO 中有结果） |\\\\n| 备注 | **强力推荐**。Linear projection 是最简单的 connector，与 OpenVLA 的 2-layer MLP 形成鲜明对比。Action expert 通过 MoE 架构耦合。Flow matching 生成动作。 |\\\\n\\\\n### 11. OpenVLA-OFT (Stanford, 2025)\\\\n\\\\n| 字段 | 信息 |\\\\n|------|------|\\\\n| 参数量 | 7B |\\\\n| Vision encoder | SigLIP + DINOv2 (Prismatic) |\\\\n| **Connector 类型** | **2-layer MLP projector**（与 OpenVLA 相同的 Prismatic connector） |\\\\n| LLM backbone | Llama-2 7B |\\\\n| 开源状态 | ✅ weights + code, GitHub: [moojink/openvla-oft](https://github.com/moojink/openvla-oft) |\\\\n| LIBERO 支持 | ✅ 原生支持，SOTA 97.1% |\\\\n| 改造成本 | 极低（已有完整 LIBERO fine-tune + eval） |\\\\n| 论文 LIBERO 结果 | 有: 97.1% SR (4 suite avg) |\\\\n| 备注 | Connector 与 OpenVLA 完全相同。改进在 fine-tuning recipe（continuous actions, action chunking, bidirectional attention）。对压缩实验来说，connector 级别的差异与 OpenVLA 相同，但 action generation 方式不同，可能影响压缩行为。 |\\\\n\\\\n### 12. RoboMM (2024)\\\\n\\\\n| 字段 | 信息 |\\\\n|------|------|\\\\n| 参数量 | 未明确公布 |\\\\n| Vision encoder | CLIP (via OpenFlamingo) |\\\\n| **Connector 类型** | **3D Perception Adapter (UVFormer)** + **Cross-attention**（OpenFlamingo 风格：text queries attend to visual features through cross-attention layers） |\\\\n| LLM backbone | OpenFlamingo (cross-attention decoder) |\\\\n| 开源状态 | ✅ code, GitHub: [RoboUniview/RoboMM](https://github.com/RoboUniview/RoboMM) |\\\\n| LIBERO 支持 | ✅ 有评测 |\\\\n| 改造成本 | 低-中 |\\\\n| 论文 LIBERO 结果 | 有: 90.7% SR |\\\\n| 备注 | Cross-attention connector 是独特的融合方式（与 MLP/linear 的 \\\\\\\"先投射再拼接\\\\\\\" 不同）。还有 occupancy supervision 的 3D adapter。多模态解码器增强感知。 |\\\\n\\\\n### 13. SpatialVLA (2025, RSS)\\\\n\\\\n| 字段 | 信息 |\\\\n|------|------|\\\\n| 参数量 | ~4B |\\\\n| Vision encoder | SigLIP |\\\\n| **Connector 类型** | **Linear projection + Ego3D Position Encoding**（PaliGemma2 的 linear connector + MLP(sinusoidal(3D positions)) 叠加到 visual tokens 上） |\\\\n| LLM backbone | Gemma (via PaliGemma2) |\\\\n| 开源状态 | ✅ weights + code, GitHub: [SpatialVLA/SpatialVLA](https://github.com/SpatialVLA/SpatialVLA), HF: IPEC-COMMUNITY/spatialvla-4b-224-pt |\\\\n| LIBERO 支持 | 未确认 |\\\\n| 改造成本 | 中（需接 LIBERO data pipeline） |\\\\n| 论文 LIBERO 结果 | 无 |\\\\n| 备注 | 基于 PaliGemma2，connector 本质上是 linear projection（与 π0 相同），加了 3D spatial encoding。Adaptive Action Grids 只输出 3 个 action token（其他模型 7 个）。 |\\\\n\\\\n### 14. DeeR-VLA (2024)\\\\n\\\\n| 字段 | 信息 |\\\\n|------|------|\\\\n| 参数量 | 3B / 9B (OpenFlamingo 变体) |\\\\n| Vision encoder | CLIP ViT-L/14 (428M params) |\\\\n| **Connector 类型** | **Perceiver Resampler + Cross-attention**（OpenFlamingo 架构：CLIP features → Perceiver Resampler → learnable cross-attention blocks 注入 LLM 层间） |\\\\n| LLM backbone | MPT-1B (3B 版) / MPT-7B (9B 版) |\\\\n| 开源状态 | ✅ code + checkpoints, GitHub: [yueyang130/DeeR-VLA](https://github.com/yueyang130/DeeR-VLA) |\\\\n| LIBERO 支持 | 需改造（paper 只有 CALVIN） |\\\\n| 改造成本 | 中-高（需接 LIBERO pipeline，且多 exit 架构增加复杂度） |\\\\n| 论文 LIBERO 结果 | 无（CALVIN benchmark） |\\\\n| 备注 | **Perceiver Resampler** 与 RoboFlamingo 相同架构基础。动态 early exit 是额外功能。可作为 Perceiver Resampler 实验的替代方案。 |\\\\n\\\\n### 15. TraceVLA (UMD, ICLR 2025)\\\\n\\\\n| 字段 | 信息 |\\\\n|------|------|\\\\n| 参数量 | 7B (OpenVLA-based) / 4B (Phi-3-Vision-based) |\\\\n| Vision encoder | SigLIP + DINOv2 (OpenVLA 版) / CLIP ViT (Phi-3 版) |\\\\n| **Connector 类型** | **2-layer MLP projector**（与 OpenVLA 相同） |\\\\n| LLM backbone | Llama-2 7B (OpenVLA 版) / Phi-3 4B |\\\\n| 开源状态 | ✅ code + weights, GitHub: [umd-huang-lab/tracevla](https://github.com/umd-huang-lab/tracevla), HF: furonghuang-lab/tracevla_7b, MIT license |\\\\n| LIBERO 支持 | 未确认（SimplerEnv + 真机） |\\\\n| 改造成本 | 低（基于 OpenVLA 改造） |\\\\n| 论文 LIBERO 结果 | 无 |\\\\n| 备注 | Connector 与 OpenVLA 相同，改进在于 visual trace prompting（在图像上叠加动作历史轨迹）。压缩行为预期与 OpenVLA 相似。 |\\\\n\\\\n### 16. X-VLA (ICLR 2026)\\\\n\\\\n| 字段 | 信息 |\\\\n|------|------|\\\\n| 参数量 | 0.9B |\\\\n| Vision encoder | Florence-Large (DaViT) |\\\\n| **Connector 类型** | **Linear projection + Soft Prompts**（vision features 通过 lightweight linear layer 投影到高维空间 + 每个 embodiment 有独立 learnable prompt embeddings 注入 transformer） |\\\\n| LLM backbone | Standard transformer 24 layers (非预训练 LLM，但使用 Florence 预训练 VLM 初始化) |\\\\n| 开源状态 | ✅ weights + code, GitHub: [2toinf/X-VLA](https://github.com/2toinf/X-VLA), HF: 2toINF/X-VLA, Apache-2.0 |\\\\n| LIBERO 支持 | ✅ 原生支持，98% SR |\\\\n| 改造成本 | 极低（已有 LIBERO 训练权重） |\\\\n| 论文 LIBERO 结果 | 有: 98% SR |\\\\n| 备注 | **强力推荐**。Linear projection connector + flow matching action generation。LIBERO SOTA 之一。小模型(0.9B)便于实验。 |\\\\n\\\\n### 17. ECoT / Embodied Chain-of-Thought (2024)\\\\n\\\\n| 字段 | 信息 |\\\\n|------|------|\\\\n| 参数量 | 7B (基于 OpenVLA) |\\\\n| Vision encoder | SigLIP + DINOv2 (Prismatic) |\\\\n| **Connector 类型** | **2-layer MLP projector**（与 OpenVLA 相同） |\\\\n| LLM backbone | Llama-2 7B |\\\\n| 开源状态 | ✅ code + weights, GitHub: [MichalZawalski/embodied-CoT](https://github.com/MichalZawalski/embodied-CoT), HF: ecot-openvla-7b-bridge/oxe |\\\\n| LIBERO 支持 | 需改造 |\\\\n| 改造成本 | 低（基于 OpenVLA） |\\\\n| 论文 LIBERO 结果 | 无 |\\\\n| 备注 | Connector 与 OpenVLA 完全相同，增加了 chain-of-thought reasoning。对 connector 压缩研究无新增价值。 |\\\\n\\\\n### 18. LingBot-VLA (Ant Group/Robbyant, 2026)\\\\n\\\\n| 字段 | 信息 |\\\\n|------|------|\\\\n| 参数量 | 4B |\\\\n| Vision encoder | Qwen2.5-VL 的 ViT（2D-RoPE + window attention） |\\\\n| **Connector 类型** | **MLP merger**（2-layer MLP with ReLU，2×2 spatial grouping 后投影 + LLM decoder 中有 cross-attention 层融合 visual features） |\\\\n| LLM backbone | Qwen2.5-VL-3B |\\\\n| 开源状态 | ✅ weights + code, GitHub: [Robbyant/lingbot-vla](https://github.com/Robbyant/lingbot-vla) |\\\\n| LIBERO 支持 | 未确认 |\\\\n| 改造成本 | 中 |\\\\n| 论文 LIBERO 结果 | 未确认 |\\\\n| 备注 | Qwen2.5-VL 的 MLP merger 是一种混合 connector：先做 spatial grouping（类似 pixel-shuffle 的空间压缩）再 MLP 投射。Mixture of Transformers 架构。 |\\\\n\\\\n---\\\\n\\\\n## Connector 类型覆盖分析\\\\n\\\\n### 已有数据的 Connector 类型\\\\n| Connector 类型 | 代表模型 | 压缩行为 |\\\\n|---------------|----------|----------|\\\\n| Pixel-shuffle | SmolVLA | Cliff-edge collapse |\\\\n| 2-layer MLP projector | OpenVLA (Prismatic) | Graded degradation |\\\\n| Perceiver Resampler | RoboFlamingo | 尝试失败 |\\\\n| **Linear projection** | **X-VLA** | **Nearly lossless pruning** |\\\\n\\\\n### 可新增的 Connector 类型\\\\n| Connector 类型 | 候选模型 | 特点 | 可行性 |\\\\n|---------------|----------|------|--------|\\\\n| **Linear projection** | **π0**, SpatialVLA | 验证 X-VLA 发现的一致性 | ⭐⭐⭐ 高 |\\\\n| **Cross-attention (Flamingo-style)** | **RoboMM** | 不在 encoder 端压缩，而是 decoder 端通过 cross-attention 选择性融合 | ⭐⭐ 中 |\\\\n| **CNN patch → direct concat** | Octo | 无独立 connector，图像 patches 直接拼入 transformer | ⭐ 低（架构差异太大） |\\\\n| **MLP merger + spatial grouping** | LingBot-VLA | 先空间合并再 MLP 投射 + cross-attention | ⭐⭐ 中 |\\\\n| **Cross-attention tokenizer** | HPT | learnable tokens 通过 cross-attention 聚合 vision features | ⭐ 低（非 VLM 架构） |\\\\n\\\\n### 关键发现\\\\n1. **Linear projection** 是最有价值的新增类型——π0 和 X-VLA 都用这种最简单的 connector，与 OpenVLA 的 2-layer MLP 形成对比\\\\n2. **Cross-attention** (RoboMM 的 OpenFlamingo 架构) 从根本上不同：不投射拼接，而是 decoder 层间交叉注意力\\\\n3. 大量模型共享 connector：OpenVLA, CogACT, LLARVA, TraceVLA, ECoT, OpenVLA-OFT 都用 **2-layer MLP**（Prismatic 或 LLaVA 架构）\\\\n\\\\n---\\\\n\\\\n## Top 推荐：最适合扩展实验的 5 个模型\\\\n\\\\n### 🥇 1. π0 (Physical Intelligence)\\\\n- **Connector**: Linear projection (单层线性)\\\\n- **推荐理由**: \\\\n  - 与 OpenVLA 的 2-layer MLP 形成直接对比（linear vs MLP）\\\\n  - 开源权重 + 代码，社区活跃\\\\n  - 已有 LIBERO 评测代码\\\\n  - PaliGemma 架构广为人知\\\\n  - 3B 参数可在单卡运行\\\\n- **预期价值**: Linear projection 不增加非线性变换，token 可能保留更多原始 visual feature 结构 → 压缩行为可能与 MLP 不同\\\\n\\\\n### 🥈 2. X-VLA\\\\n- **Connector**: Linear projection + soft prompts\\\\n- **推荐理由**:\\\\n  - 同样是 linear projection，与 π0 对比看 soft prompt 的影响\\\\n  - LIBERO 98% SR，已有训练好的 LIBERO 权重直接可用\\\\n  - 0.9B 参数，实验成本最低\\\\n  - ICLR 2026，最新模型\\\\n  - Apache-2.0 开源\\\\n- **预期价值**: 验证 linear projection 的压缩行为是否 consistent across models\\\\n\\\\n### 🥉 3. DeeR-VLA\\\\n- **Connector**: Perceiver Resampler + Cross-attention (OpenFlamingo)\\\\n- **推荐理由**:\\\\n  - Perceiver Resampler 与 RoboFlamingo 相同架构，但 DeeR-VLA 已验证可训练（CALVIN benchmark 正常工作）\\\\n  - 给 Perceiver Resampler 第二次机会\\\\n  - 可对比 RoboFlamingo 的训练失败是架构问题还是实现问题\\\\n  - Open source with checkpoints\\\\n- **预期价值**: Perceiver Resampler 本身就做了 attention-based compression → 压缩行为可能与 MLP/linear 截然不同\\\\n- **风险**: LIBERO 需要自己改造\\\\n\\\\n### 4. RoboMM\\\\n- **Connector**: Cross-attention (OpenFlamingo) + 3D Adapter\\\\n- **推荐理由**:\\\\n  - Cross-attention 融合方式从根本上不同于 projection-based connectors\\\\n  - 已有 LIBERO 结果 (90.7%)\\\\n  - Open source\\\\n- **预期价值**: Cross-attention 在 decoder 端动态选择 visual features → 可能展现出与 projection-based 完全不同的压缩模式\\\\n- **风险**: 架构较复杂，3D adapter 增加变量\\\\n\\\\n### 5. OpenVLA-OFT\\\\n- **Connector**: 2-layer MLP projector (与 OpenVLA 相同)\\\\n- **推荐理由**:\\\\n  - Connector 与 OpenVLA 相同，但 action generation 完全不同（continuous + chunking）\\\\n  - LIBERO 97.1% SOTA\\\\n  - 可验证 \\\\\\\"相同 connector + 不同 action head\\\\\\\" 是否影响压缩行为\\\\n  - 已有完整 LIBERO 代码\\\\n- **预期价值**: 作为 OpenVLA 的对照组，隔离 connector vs action head 对压缩的影响\\\\n\\\\n---\\\\n\\\\n## 不推荐的模型及原因\\\\n\\\\n| 模型 | 排除原因 |\\\\n|------|----------|\\\\n| RT-2-X | 闭源，权重不可用 |\\\\n| GR-2 | 未开源 |\\\\n| 3D-VLA | 3D 点云输入，与 2D VLA 差异太大 |\\\\n| CogACT | Connector 与 OpenVLA 相同（Prismatic MLP），不新增类型 |\\\\n| LLARVA | Connector 与 OpenVLA 类似（MLP projector），不新增类型 |\\\\n| TraceVLA | Connector 与 OpenVLA 相同，不新增类型 |\\\\n| ECoT | Connector 与 OpenVLA 相同，不新增类型 |\\\\n| HPT | 非 VLM 架构，不适合 connector 压缩叙事 |\\\\n| GR-1 | 有 Perceiver Resampler（有价值），但无 LIBERO 支持 + 视频生成架构改造成本高 |\\\\n| Octo | 无独立 connector（CNN patch 直接拼入），架构与标准 VLM 差异太大 |\\\\n\\\\n---\\\\n\\\\n## 总结：Connector 类型 × 模型矩阵\\\\n\\\\n| Connector 类型 | 已有 | 推荐新增 |\\\\n|---------------|------|----------|\\\\n| Pixel-shuffle | SmolVLA ✅ | — |\\\\n| 2-layer MLP projector | OpenVLA ✅ | OpenVLA-OFT（同 connector 不同 action head） |\\\\n| Perceiver Resampler | RoboFlamingo ❌(失败) | **DeeR-VLA** |\\\\n| **Linear projection** | **X-VLA ✅** | **π0** |\\\\n| **Cross-attention** | — | **RoboMM** |\\\\n\\\\n实现后可达 **5 种 connector 类型 × 6+ 模型**的全面对比。\\\\n\\\\n---\\\\n\\\\n## X-VLA 详细架构调研（2026-05-20 新增）\\\\n\\\\n### 模型身份确认\\\\n- **名称**: X-VLA (Soft-Prompted Transformer as Scalable Cross-Embodiment Vision-Language-Action Model)\\\\n- **论文**: arXiv:2510.10274, ICLR 2026\\\\n- **GitHub**: [2toinf/X-VLA](https://github.com/2toinf/X-VLA)\\\\n- **HuggingFace**: [2toINF/X-VLA](https://huggingface.co/collections/2toINF/x-vla)\\\\n- **参数量**: 0.9B\\\\n- **许可**: Apache-2.0\\\\n- **LIBERO SR**: 98.1%\\\\n\\\\n### 架构详解\\\\n\\\\n```\\\\nImage (224×224) → Florence-Large (DaViT) → Vision Tokens [B, N, 2048]\\\\n    → Linear Projection + LayerNorm → [B, N, 1024]\\\\n    → Merge with Text Token Embeddings → Florence2 Encoder (self-attention)\\\\n    → Context Features → SoftPromptedTransformer (24 layers, hidden=1024)\\\\n        + Soft Prompts (32 learnable embeddings per embodiment)\\\\n        + Noised Action Tokens (flow matching)\\\\n    → Denoised Action Trajectory [B, 30, 20]\\\\n```\\\\n\\\\n**各组件详情**:\\\\n\\\\n| 组件 | 规格 |\\\\n|------|------|\\\\n| Vision Encoder | Florence-Large (DaViT): patch_stride=[4,2,2,2] → total stride 32 |\\\\n| Vision Token 数量 | ~49 tokens (7×7 at 224×224) 或 ~576 tokens (24×24 at 768×768) — **需实际加载模型验证** |\\\\n| Projection | Linear + LayerNorm, dim 2048 → 1024 (projection_dim=1024) |\\\\n| Soft Prompts | 32 tokens/embodiment, 0.04% of total params |\\\\n| Transformer | 24 layers, hidden=1024, 16 heads, mlp_ratio=4.0 |\\\\n| Action Head | Flow matching, 30 anchor points × 20 dims (EE6D), 10 denoising steps |\\\\n| Max Sequence | 512 tokens |\\\\n\\\\n### HuggingFace 权重\\\\n| Checkpoint | 用途 | 地址 |\\\\n|------------|------|------|\\\\n| X-VLA-Pt | 预训练基座 (cross-embodiment) | 2toINF/X-VLA-Pt |\\\\n| X-VLA-Libero | LIBERO 全参数微调 (98.1% SR) | 2toINF/X-VLA-Libero |\\\\n| X-VLA-libero-*-peft | LIBERO LoRA 微调 (各 suite) | 2toINF/X-VLA-libero-spatial-peft 等 |\\\\n\\\\n### 环境依赖\\\\n```\\\\ntransformers<=4.51.3, torch, einops==0.8.1, timm==1.0.12, \\\\naccelerate==1.2.1, peft==0.17.1, safetensors==0.4.5,\\\\nnumpy==1.26.3, scipy==1.15.0, mmengine==0.10.5,\\\\nfastapi, uvicorn==0.34.3, h5py==3.12.1, pyarrow==20.0.0,\\\\nav==15.0.0, mediapy==1.2.4\\\\n```\\\\nLIBERO 评估另需 Python 3.8 环境。\\\\n\\\\n### VTC 集成方案\\\\n**插入点**: Florence2 `_encode_image()` 输出 → **VTC** → `_merge_input_ids_with_image_features()`\\\\n\\\\n**改造清单**:\\\\n1. 创建 `xvla_vtc_adapter.py`（复用 VisionTokenCompressor，hidden_dim 改 1024）\\\\n2. 创建 XVLASmartCompressWrapper，hook Florence2 vision 输出\\\\n3. 修改 merge 逻辑以适应压缩后的 token 数量\\\\n4. 创建 `train_xvla_smart_compress.py`（参考 X-VLA 的 train.py + peft_train.py）\\\\n5. 适配 flow matching loss（不同于 OpenVLA 的 cross-entropy）\\\\n\\\\n**与 OpenVLA VTC 的关键差异**:\\\\n| 维度 | OpenVLA | X-VLA |\\\\n|------|---------|-------|\\\\n| hidden_dim | 4096 | 1024 |\\\\n| 原始 vision tokens | 256 | ~49-576 (待验证) |\\\\n| Action 范式 | Autoregressive (256-bin CE) | Flow matching (MSE+BCE) |\\\\n| Connector | 2-layer MLP | Linear + LayerNorm |\\\\n| 模型大小 | 7B | 0.9B |\\\\n\\\\n**预计工作量**: 8-12 小时\\\\n- 代码改造: 4-6h（adapter + training script）\\\\n- 环境搭建 + 模型下载: 2-3h\\\\n- 验证 + 调试: 2-3h\\\\n\\\\n---\\\\n\\\\n## X-VLA Token Importance 分析结果（2026-05-20）\\\\n\\\\n### 实验配置\\\\n- **模型**: X-VLA-0.9B (lerobot/xvla-libero checkpoint)\\\\n- **数据**: LIBERO-Object (task_index 20-29), 100 images, 10 tasks\\\\n- **服务器**: westd-41074, cuda:1\\\\n- **分析脚本**: `/root/autodl-tmp/importance_margin_vla_compress/analyze_xvla_token_importance.py`\\\\n- **结果文件**: `/root/autodl-tmp/importance_margin_vla_compress/eval_results/xvla_attention_entropy_perlayer.json`\\\\n\\\\n### SoftPromptedTransformer 序列布局\\\\n| Token 类型 | 数量 | 说明 |\\\\n|-----------|------|------|\\\\n| Action tokens | 30 | Flow matching denoised action |\\\\n| VLM features | 64 | Florence2 encoder output (main view) |\\\\n| Aux visual | 150 | Additional camera views |\\\\n| Soft prompts | 32 | Embodiment-specific learnable tokens |\\\\n| **Total** | **276** | |\\\\n\\\\n### Entropy Ratio（Action→Vision 注意力熵）\\\\n- **Overall**: **0.6138** ± 0.1159\\\\n- **趋势**: 浅层低（L0=0.46, L1=0.34），深层高（L22=0.79, L23=0.71）\\\\n- 浅层集中注意力于少数 vision tokens，深层趋于均匀\\\\n\\\\n### Vision Attention Fraction（Action tokens 分配给 vision tokens 的注意力比例）\\\\n- 浅层（L0-2）: 33-49% — action tokens 还关注 soft prompts 和 self\\\\n- 中层（L6-11）: 84-90% — 绝大部分注意力给 vision tokens\\\\n- 深层（L17-23）: 79-90% — 持续高注意力\\\\n\\\\n### Pruning Curve（核心发现）\\\\n| Retention k | Mean Loss | Normalized |\\\\n|-------------|-----------|------------|\\\\n| 0.30 | 0.112945 | **1.0014** |\\\\n| 0.50 | 0.112823 | 1.0003 |\\\\n| 0.70 | 0.112789 | 1.0000 |\\\\n| 0.90 | 0.112789 | 1.0000 |\\\\n| 0.95 | 0.112789 | 1.0000 |\\\\n| 1.00 | 0.112789 | 1.0000 |\\\\n\\\\n**关键结论**: 丢弃 70% 的 vision tokens（k=0.3）仅导致 0.14% 的 loss 增加。X-VLA 的 vision tokens **几乎完全可压缩**。\\\\n\\\\n### 跨模型对比\\\\n| 模型 | Connector | Entropy Ratio | k=0.3 Norm Loss | 压缩行为 |\\\\n|------|-----------|---------------|-----------------|----------|\\\\n| SmolVLA | Pixel-shuffle | ~0.45 (低) | Cliff-edge | 不可压缩 |\\\\n| OpenVLA | 2-layer MLP | ~0.55 (中) | ~1.15 (15%↑) | 渐进退化 |\\\\n| **X-VLA** | **Linear proj** | **0.61 (中高)** | **1.0014 (0.14%↑)** | **几乎无损** |\\\\n\\\\n### 解读\\\\n1. **Linear projection connector 产生了高度冗余的 vision token 表示**——大部分信息集中在少数 token 中，L2 norm 可以轻松识别\\\\n2. Entropy 比 OpenVLA 更高（0.61 vs 0.55），说明注意力分布更均匀，但这不矛盾——均匀分布意味着 \\\\\\\"每个 token 被平等关注\\\\\\\"，而 pruning 几乎无损意味着 \\\\\\\"被关注的内容高度冗余\\\\\\\"\\\\n3. 这是 **connector 架构论文的关键数据点**：linear projection（无非线性变换）保留了 DaViT 输出的原始冗余结构，而 MLP projector（2 层 + GELU）通过非线性变换重新分配了信息，使得 token 间差异更大、更难压缩\\\\n\\\\n---\\\\n\\\\n## OFT Importance CV 分析结果（2026-05-20）\\\\n\\\\n### 结论\\\\n- **OFT CV = 0.2185**，per-task CV 在 0.211–0.225 之间\\\\n- 与 OpenVLA (0.215) 高度一致——两者共享相同的 2-layer MLP projector（Prismatic 架构）\\\\n- **LoRA fine-tuning 不改变 vision token importance 分布**——connector 架构是唯一决定因素\\\\n\\\\n### Diagnostic 表格完成状态（5/5）\\\\n| 模型 | Connector | CV | 压缩行为 |\\\\n|------|-----------|-----|----------|\\\\n| SmolVLA | Pixel-shuffle | ~0.08 | Cliff-edge collapse |\\\\n| OpenVLA | 2-layer MLP | 0.215 | Graded degradation |\\\\n| OpenVLA-OFT | 2-layer MLP (same) | 0.2185 | 预期与 OpenVLA 相同 |\\\\n| X-VLA | Linear projection | TBD | Nearly lossless |\\\\n| RoboFlamingo | Perceiver Resampler | N/A | 训练失败 |\\\\n\\\\n### 论文意义\\\\nOFT 结果支撑 claim: \\\\\\\"token importance distribution is an intrinsic property of the connector architecture, invariant to downstream fine-tuning strategy (LoRA vs full)\\\\\\\"\\\\n\\\\n---\\\\n\\\\n## 失败模式记录\\\\n\\\\n- [2026-05-21] **π0.5 自定义 eval 脚本 bug**: `eval_pi05_pruning_libero.py` 的 `patched_embed_image` 函数导致 0% SR，而官方 eval 脚本在同一 checkpoint 上 ~100% SR。→ 新模型接入时，必须先用官方 eval 脚本验证 checkpoint 可用性，确认后再写自定义 pruning eval 脚本。不要假设自定义 patch 正确。\\\\n\\\\n- [2026-05-21] **OpenVLA eval 4 实验批量失败 (westd-38929)**:\\\\n  - **失败实验**: eval_openvla_l2norm_k05_object_seed42 (PID 568225), eval_openvla_random_k03_object_seed42 (PID 568905), eval_openvla_l2norm_k07_object_seed42 (PID 569611), eval_openvla_l2norm_k03_object_seed42 (PID 570309)\\\\n  - **根因**: **AutoDL 容器 GPU 缩配**。主机有 9 块 NVIDIA RTX PRO 6000 Blackwell (各 97GB)，但容器当前只挂载了 `/dev/nvidia2` 一块 GPU。4 个实验分别在 CUDA_VISIBLE_DEVICES=0/1/2/3 启动，运行 ~1h43m 后 GPU 设备被平台回收，进程收到 SIGKILL 无任何 traceback。\\\\n  - **证据**:\\\\n    - `nvidia-smi -L` 只显示 1 块 GPU (Device Minor 2)，而 `/proc/driver/nvidia/gpus/` 显示主机有 9 块\\\\n    - 4 个日志文件在 14:45-14:49 间依次停止写入（3 分钟跨度，非瞬时），末尾均为正常进度输出无 error\\\\n    - 各实验完成了 Task 1-3，在 Task 4/10 中被杀（~30% 完成度）\\\\n    - 系统 RAM 充足（1TB 中仅用 46GB），排除 CPU OOM\\\\n    - 无 tmux session，进程通过 nohup 方式运行\\\\n  - **修复建议**:\\\\n    1. 在 AutoDL 控制台恢复实例到 4 GPU 配置（或至少确认 GPU 分配稳定）\\\\n    2. 重新启动 4 个实验，建议使用 tmux 以防 SSH 断连\\\\n    3. 如果无法恢复多 GPU，可在单 GPU 上顺序运行（每个实验约 5.5h，共 ~22h）\\\\n    4. 启动命令参考（单 GPU 顺序）:\\\\n       ```bash\\\\n       tmux new -s openvla_eval\\\\n       source /root/miniconda3/etc/profile.d/conda.sh && conda activate base\\\\n       cd /root/autodl-tmp/importance_margin_vla_compress\\\\n       CUDA_VISIBLE_DEVICES=0 python -u eval_openvla_l2norm_libero.py --mode l2norm_prune --k_ratio 0.5 --suite libero_object --seed 42 > logs/eval_openvla_l2norm_k05_seed42.log 2>&1\\\\n       CUDA_VISIBLE_DEVICES=0 python -u eval_openvla_l2norm_libero.py --mode random_prune --k_ratio 0.3 --suite libero_object --seed 42 > logs/eval_openvla_random_k03_seed42.log 2>&1\\\\n       CUDA_VISIBLE_DEVICES=0 python -u eval_openvla_l2norm_libero.py --mode l2norm_prune --k_ratio 0.7 --suite libero_object --seed 42 > logs/eval_openvla_l2norm_k07_seed42.log 2>&1\\\\n       CUDA_VISIBLE_DEVICES=0 python -u eval_openvla_l2norm_libero.py --mode l2norm_prune --k_ratio 0.3 --suite libero_object --seed 42 > logs/eval_openvla_l2norm_k03_seed42.log 2>&1\\\\n       ```\\\\n\\\\n---\\\\n\\\\n## π0.5 跨 suite 对比（2026-05-21）\\\\n\\\\n**模型**: π0.5 (PaliGemma, linear projection connector, CV=0.055)\\\\n**数据来源**: registry 中所有 status=DONE 且有有效 metrics 的 pi05 实验\\\\n\\\\n### Object Suite（baseline=98.2%, eval_pi05_baseline_object_seed42）\\\\n\\\\n| k | L2norm SR (%) | L2norm exp_ids | Random SR (%) | Random exp_ids |\\\\n|---|--------------|----------------|--------------|----------------|\\\\n| 0.9 | **98.2** (s42) | eval_pi05_l2norm_k09_object_seed42_v2 | **10.8** avg [12.0(s42), 9.6(s43)] | eval_pi05_random_k09_object_seed42_v2, eval_pi05_random_k09_object_seed43 |\\\\n| 0.7 | **56.4** avg [55.0(s42), 56.4(s43), 57.8(s43v2)] | eval_pi05_l2norm_k07_object_seed42, _seed43, _seed43_v2 | **75.5** avg [77.2(s42), 73.8(s43)] | eval_pi05_random_k07_object_seed42, _seed43 |\\\\n| 0.5 | **33.5** avg [33.4(s42), 33.6(s43)] | eval_pi05_l2norm_k05_object_seed42, _seed43 | **68.9** avg [69.4(s42), 68.4(s43)] | eval_pi05_random_k05_object_seed42, _seed43 |\\\\n| 0.3 | **53.2** avg [51.0(s42), 55.4(s43)] | eval_pi05_l2norm_k03_object_seed42, _seed43 | **36.4** (s42) | eval_pi05_random_k03_object_seed42 |\\\\n| 0.1 | **2.6** (s42) | eval_pi05_l2norm_k01_object_seed42 | — | — |\\\\n\\\\n### Spatial Suite（baseline=97.2%, eval_pi05_baseline_spatial_seed42）\\\\n\\\\n| k | L2norm SR (%) | Random SR (%) | Random exp_ids |\\\\n|---|--------------|--------------|----------------|\\\\n| 0.9 | — (pending) | — (pending) | — |\\\\n| 0.7 | — (pending) | — (submitted) | — |\\\\n| 0.5 | — (running) | **71.6** (s42) | eval_pi05_random_k05_spatial_seed42 |\\\\n| 0.3 | — (running) | — (submitted) | — |\\\\n\\\\n### Cross-suite 一致性分析\\\\n\\\\n**Random k=0.5 对比**:\\\\n- Object: **68.9%** (seed42=69.4%, seed43=68.4%)\\\\n- Spatial: **71.6%** (seed42)\\\\n- **Delta: 2.7pp** — 高度一致\\\\n\\\\n结论：Random pruning 在 k=0.5 的表现跨 suite 具有强一致性（差异仅 2.7pp），说明 π0.5 的 vision token 冗余结构不依赖于具体 task 类型。Spatial 略高于 Object 可能因为 Spatial 任务（同一物体不同位置）对视觉信息量要求更低。\\\\n\\\\n### 关键现象\\\\n\\\\n1. **L2norm 非单调 V-shape**：k=0.5 是谷底(33.5%)，k=0.3 反弹到 53.2%。多 seed 确认。原因待查——可能 L2 norm 在 50% 保留时恰好选中了信息量最差的 token 子集。\\\\n\\\\n2. **Random k=0.9 异常崩塌**：仅保留 90% token 时 random pruning SR 降至 ~10.8%（双 seed 确认 12.0%/9.6%），而 L2norm k=0.9 正常(98.2%)。这是所有模型中未见过的现象——移除 10% random token 即可摧毁模型。推测 π0.5 少数 token 承载关键位置信息，random 删除有 ~90% 概率命中关键 token。\\\\n\\\\n3. **Random 优于 L2norm 的 k 区间**：k=0.5(random 68.9% vs L2norm 33.5%)和 k=0.7(random 75.5% vs L2norm 56.4%)时 random 大幅优于 L2norm。说明 L2 norm 不是 π0.5 vision token importance 的好 proxy——CV=0.055 意味着 L2 norm 几乎无区分度。\\\\n\\\\n4. **Failed/killed 实验（已排除）**: eval_pi05_random_k07_object_seed42_v2(killed), _v3(killed), eval_pi05_random_k085_object_seed42(failed), eval_pi05_random_k095_object_seed42(failed), eval_pi05_random_k09_fixedmask_object_seed42(network error)。\\\\n\\\", \\\"total_chars\\\": 25431, \\\"truncated\\\": false}, \\\"error\\\": null, \\\"metadata\\\": {}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/memory.md\", \"content\": \"# VLA 模型全面调研报告\\n\\n**调研日期**: 2026-05-20\\n**目的**: 寻找不同 connector 架构的开源 VLA 模型，扩展 vision connector 对 token 可压缩性影响的实验\\n\\n---\\n\\n## 已有实验数据\\n\\n| 模型 | Connector | 压缩行为 |\\n|------|-----------|----------|\\n| SmolVLA | Pixel-shuffle | Cliff-edge collapse (k=0.95 → 0% SR) |\\n| OpenVLA | 2-layer MLP projector | Graded degradation (线性下降) |\\n| RoboFlamingo | Perceiver Resampler | 尝试失败（gripper loss 无法训练） |\\n| **X-VLA** | **Linear projection** | **Nearly lossless (k=0.3 → norm=1.0014)** |\\n\\n---\\n\\n## 完整模型调研表\\n\\n### 1. Octo (UC Berkeley, 2024)\\n\\n| 字段 | 信息 |\\n|------|------|\\n| 参数量 | 27M (Small) / 93M (Base) |\\n| Vision encoder | Shallow CNN (从头训练，非预训练 ViT) |\\n| **Connector 类型** | **CNN patch encoder → 直接拼接进 transformer（无独立 connector）** |\\n| LLM backbone | 纯 transformer（非预训练 LLM），decoder-only |\\n| 开源状态 | ✅ weights + code, GitHub: [octo-models/octo](https://github.com/octo-models/octo), HF: rail-berkeley/octo-base |\\n| LIBERO 支持 | ✅ 原生支持，fine-tune 后 ~72% SR |\\n| 改造成本 | 低（已有 LIBERO fine-tune 代码） |\\n| 论文 LIBERO 结果 | 有: ~72% (fine-tuned) |\\n| 备注 | 非标准 VLM→LLM 架构，是 transformer-based diffusion policy。图像通过浅层 CNN 编码为 16×16 patches 后直接拼入 transformer 序列。语言用 T5 tokenizer/encoder。Action head 是 diffusion policy。 |\\n\\n### 2. CogACT (Microsoft/Tsinghua, 2024)\\n\\n| 字段 | 信息 |\\n|------|------|\\n| 参数量 | ~7.1B (7B Prismatic VLM + 89M-300M DiT action module) |\\n| Vision encoder | DINOv2 + SigLIP (双 encoder，channel 拼接) |\\n| **Connector 类型** | **2-layer MLP projector**（Prismatic 架构：DINOv2+SigLIP feature → channel concat → 2-layer MLP → Llama-2 embedding space） |\\n| LLM backbone | Llama-2 7B (via Prismatic-7B) |\\n| 开源状态 | ✅ weights + code, GitHub: [microsoft/CogACT](https://github.com/microsoft/CogACT), HF: CogACT/CogACT-Base, CogACT/CogACT-Small |\\n| LIBERO 支持 | 需改造（paper 用 SimplerEnv + 真机） |\\n| 改造成本 | 中（需接 LIBERO data pipeline + action space） |\\n| 论文 LIBERO 结果 | 无 |\\n| 备注 | 核心创新在 DiT action module（将 VLM 认知特征作为 condition 输入扩散 transformer 生成动作）。Connector 与 OpenVLA 相同（都基于 Prismatic） |\\n\\n### 3. HPT (MIT, NeurIPS 2024)\\n\\n| 字段 | 信息 |\\n|------|------|\\n| 参数量 | 3.1M (S) / 12.6M (B) / 50.5M (L) / 226.8M (XL) / 1.1B (Huge) |\\n| Vision encoder | 预训练冻结 ResNet18 |\\n| **Connector 类型** | **Cross-attention tokenizer**（learnable tokens 通过 cross-attention 聚合 vision features → 固定 16 tokens，每个 camera view 有独立 MLP projector） |\\n| LLM backbone | 无（纯 decoder-only transformer，从头训练） |\\n| 开源状态 | ✅ weights + code, GitHub: [liruiw/HPT](https://github.com/liruiw/HPT), HF: liruiw/hpt |\\n| LIBERO 支持 | 未确认（paper 评测 6 个 benchmark） |\\n| 改造成本 | 中（非标准 VLM 架构，需改 stem + action head） |\\n| 论文 LIBERO 结果 | 无 |\\n| 备注 | 非 VLM→LLM 架构。Cross-attention tokenizer 类似 Perceiver 但更轻量（8 heads, 64 dim/head）。跨 embodiment 预训练。 |\\n\\n### 4. RT-2-X (Google DeepMind, 2023)\\n\\n| 字段 | 信息 |\\n|------|------|\\n| 参数量 | 55B |\\n| Vision encoder | ViT (PaLI-X 的视觉编码器) |\\n| **Connector 类型** | 未公开（闭源） |\\n| LLM backbone | PaLI-X / PaLM-E |\\n| 开源状态 | ❌ **闭源**，权重不公开 |\\n| LIBERO 支持 | 不可行 |\\n| 改造成本 | 不可行 |\\n| 论文 LIBERO 结果 | 无 |\\n| 备注 | 闭源模型，无法使用 |\\n\\n### 5. GR-1 (ByteDance, 2023)\\n\\n| 字段 | 信息 |\\n|------|------|\\n| 参数量 | 未明确公布 |\\n| Vision encoder | MAE ViT-Base (预训练) |\\n| **Connector 类型** | **Perceiver Resampler**（将 MAE ViT 视觉 token 数量压缩）+ linear layers 对齐维度 |\\n| LLM backbone | GPT-style causal transformer（非预训练 LLM） |\\n| 开源状态 | ✅ weights + code, GitHub: [bytedance/GR-1](https://github.com/bytedance/GR-1), Apache-2.0 |\\n| LIBERO 支持 | 需改造（paper 只有 CALVIN） |\\n| 改造成本 | 高（需改 data pipeline、action space、视频生成部分可能要适配） |\\n| 论文 LIBERO 结果 | 无（CALVIN: 94.9%） |\\n| 备注 | 既做动作预测又做视频生成（future image prediction）。语言用 CLIP text encoder。使用 Perceiver Resampler 这一点很有价值——与 RoboFlamingo 类似但架构不同。 |\\n\\n### 6. GR-2 (ByteDance, 2024)\\n\\n| 字段 | 信息 |\\n|------|------|\\n| 参数量 | 未公布 |\\n| Vision encoder | 未公布 |\\n| **Connector 类型** | 未公布 |\\n| LLM backbone | 未公布 |\\n| 开源状态 | ❌ **未开源**，代码/权重未释放 |\\n| LIBERO 支持 | 不可行 |\\n| 改造成本 | 不可行 |\\n| 论文 LIBERO 结果 | 无 |\\n| 备注 | GR-1 的后续，但未开源 |\\n\\n### 7. LLARVA (2024)\\n\\n| 字段 | 信息 |\\n|------|------|\\n| 参数量 | 7B |\\n| Vision encoder | CLIP ViT-L/14 |\\n| **Connector 类型** | **MLP projector**（LLaVA-style，2-layer MLP with GELU） |\\n| LLM backbone | Llama-2 7B |\\n| 开源状态 | ✅ code + LoRA weights, GitHub: [Dantong88/LLARVA](https://github.com/Dantong88/LLARVA), Apache-2.0 |\\n| LIBERO 支持 | 需改造 |\\n| 改造成本 | 中（需接 action head + LIBERO data pipeline） |\\n| 论文 LIBERO 结果 | 无 |\\n| 备注 | 预测 visual traces (2D 轨迹) 作为中间表示。Connector 与 OpenVLA 类似（都是 MLP projector），但用 CLIP 而非 Prismatic 双 encoder |\\n\\n### 8. RoboVLMs (2024)\\n\\n| 字段 | 信息 |\\n|------|------|\\n| 参数量 | 不定（框架） |\\n| Vision encoder | 支持多种 VLM backbone |\\n| **Connector 类型** | 取决于所选 VLM（框架支持多种） |\\n| LLM backbone | 取决于所选 VLM |\\n| 开源状态 | ✅ code + models, GitHub: [Robot-VLAs/RoboVLMs](https://github.com/Robot-VLAs/RoboVLMs) |\\n| LIBERO 支持 | 需确认 |\\n| 改造成本 | 低-中（框架设计灵活） |\\n| 论文 LIBERO 结果 | 未确认 |\\n| 备注 | 这是一个**框架**而非单一模型。实验了 8+ VLM backbone × 4 policy 架构。最佳模型用 Kosmos backbone。对我们的 connector 对比研究有参考价值但不直接使用。 |\\n\\n### 9. 3D-VLA (UMass, ICML 2024)\\n\\n| 字段 | 信息 |\\n|------|------|\\n| 参数量 | 未明确 |\\n| Vision encoder | 3D feature extraction（point cloud based） |\\n| **Connector 类型** | **Interaction tokens**（3D-LLM 架构，用交互 token 嵌入 embodied 环境） |\\n| LLM backbone | 基于 3D-LLM |\\n| 开源状态 | ✅ code + diffusion models, GitHub: [UMass-Embodied-AGI/3D-VLA](https://github.com/UMass-Embodied-AGI/3D-VLA), HF: anyezhy |\\n| LIBERO 支持 | 需大量改造（paper 用 RLBench） |\\n| 改造成本 | 高（3D 点云输入，与 LIBERO 2D 图像差异大） |\\n| 论文 LIBERO 结果 | 无 |\\n| 备注 | 基于 3D 点云的 VLA，与我们研究的 2D 图像 → connector → LLM 管道差异太大，不推荐 |\\n\\n### 10. π0 / pi-zero (Physical Intelligence, 2024-2025)\\n\\n| 字段 | 信息 |\\n|------|------|\\n| 参数量 | ~3.3B (400M SigLIP + 2.6B Gemma + ~300M action expert) |\\n| Vision encoder | SigLIP-So400m (400M params) |\\n| **Connector 类型** | **Linear projection**（单层线性层，将 SigLIP token 投影到 Gemma embedding space） |\\n| LLM backbone | Gemma 2B (via PaliGemma) |\\n| 开源状态 | ✅ weights + code, GitHub: [Physical-Intelligence/openpi](https://github.com/Physical-Intelligence/openpi), HF 有 PyTorch port |\\n| LIBERO 支持 | ✅ 有评测（LIBERO-PRO 中被评测） |\\n| 改造成本 | 低（已有 LIBERO 评测代码） |\\n| 论文 LIBERO 结果 | 有（LIBERO-PRO 中有结果） |\\n| 备注 | **强力推荐**。Linear projection 是最简单的 connector，与 OpenVLA 的 2-layer MLP 形成鲜明对比。Action expert 通过 MoE 架构耦合。Flow matching 生成动作。 |\\n\\n### 11. OpenVLA-OFT (Stanford, 2025)\\n\\n| 字段 | 信息 |\\n|------|------|\\n| 参数量 | 7B |\\n| Vision encoder | SigLIP + DINOv2 (Prismatic) |\\n| **Connector 类型** | **2-layer MLP projector**（与 OpenVLA 相同的 Prismatic connector） |\\n| LLM backbone | Llama-2 7B |\\n| 开源状态 | ✅ weights + code, GitHub: [moojink/openvla-oft](https://github.com/moojink/openvla-oft) |\\n| LIBERO 支持 | ✅ 原生支持，SOTA 97.1% |\\n| 改造成本 | 极低（已有完整 LIBERO fine-tune + eval） |\\n| 论文 LIBERO 结果 | 有: 97.1% SR (4 suite avg) |\\n| 备注 | Connector 与 OpenVLA 完全相同。改进在 fine-tuning recipe（continuous actions, action chunking, bidirectional attention）。对压缩实验来说，connector 级别的差异与 OpenVLA 相同，但 action generation 方式不同，可能影响压缩行为。 |\\n\\n### 12. RoboMM (2024)\\n\\n| 字段 | 信息 |\\n|------|------|\\n| 参数量 | 未明确公布 |\\n| Vision encoder | CLIP (via OpenFlamingo) |\\n| **Connector 类型** | **3D Perception Adapter (UVFormer)** + **Cross-attention**（OpenFlamingo 风格：text queries attend to visual features through cross-attention layers） |\\n| LLM backbone | OpenFlamingo (cross-attention decoder) |\\n| 开源状态 | ✅ code, GitHub: [RoboUniview/RoboMM](https://github.com/RoboUniview/RoboMM) |\\n| LIBERO 支持 | ✅ 有评测 |\\n| 改造成本 | 低-中 |\\n| 论文 LIBERO 结果 | 有: 90.7% SR |\\n| 备注 | Cross-attention connector 是独特的融合方式（与 MLP/linear 的 \\\"先投射再拼接\\\" 不同）。还有 occupancy supervision 的 3D adapter。多模态解码器增强感知。 |\\n\\n### 13. SpatialVLA (2025, RSS)\\n\\n| 字段 | 信息 |\\n|------|------|\\n| 参数量 | ~4B |\\n| Vision encoder | SigLIP |\\n| **Connector 类型** | **Linear projection + Ego3D Position Encoding**（PaliGemma2 的 linear connector + MLP(sinusoidal(3D positions)) 叠加到 visual tokens 上） |\\n| LLM backbone | Gemma (via PaliGemma2) |\\n| 开源状态 | ✅ weights + code, GitHub: [SpatialVLA/SpatialVLA](https://github.com/SpatialVLA/SpatialVLA), HF: IPEC-COMMUNITY/spatialvla-4b-224-pt |\\n| LIBERO 支持 | 未确认 |\\n| 改造成本 | 中（需接 LIBERO data pipeline） |\\n| 论文 LIBERO 结果 | 无 |\\n| 备注 | 基于 PaliGemma2，connector 本质上是 linear projection（与 π0 相同），加了 3D spatial encoding。Adaptive Action Grids 只输出 3 个 action token（其他模型 7 个）。 |\\n\\n### 14. DeeR-VLA (2024)\\n\\n| 字段 | 信息 |\\n|------|------|\\n| 参数量 | 3B / 9B (OpenFlamingo 变体) |\\n| Vision encoder | CLIP ViT-L/14 (428M params) |\\n| **Connector 类型** | **Perceiver Resampler + Cross-attention**（OpenFlamingo 架构：CLIP features → Perceiver Resampler → learnable cross-attention blocks 注入 LLM 层间） |\\n| LLM backbone | MPT-1B (3B 版) / MPT-7B (9B 版) |\\n| 开源状态 | ✅ code + checkpoints, GitHub: [yueyang130/DeeR-VLA](https://github.com/yueyang130/DeeR-VLA) |\\n| LIBERO 支持 | 需改造（paper 只有 CALVIN） |\\n| 改造成本 | 中-高（需接 LIBERO pipeline，且多 exit 架构增加复杂度） |\\n| 论文 LIBERO 结果 | 无（CALVIN benchmark） |\\n| 备注 | **Perceiver Resampler** 与 RoboFlamingo 相同架构基础。动态 early exit 是额外功能。可作为 Perceiver Resampler 实验的替代方案。 |\\n\\n### 15. TraceVLA (UMD, ICLR 2025)\\n\\n| 字段 | 信息 |\\n|------|------|\\n| 参数量 | 7B (OpenVLA-based) / 4B (Phi-3-Vision-based) |\\n| Vision encoder | SigLIP + DINOv2 (OpenVLA 版) / CLIP ViT (Phi-3 版) |\\n| **Connector 类型** | **2-layer MLP projector**（与 OpenVLA 相同） |\\n| LLM backbone | Llama-2 7B (OpenVLA 版) / Phi-3 4B |\\n| 开源状态 | ✅ code + weights, GitHub: [umd-huang-lab/tracevla](https://github.com/umd-huang-lab/tracevla), HF: furonghuang-lab/tracevla_7b, MIT license |\\n| LIBERO 支持 | 未确认（SimplerEnv + 真机） |\\n| 改造成本 | 低（基于 OpenVLA 改造） |\\n| 论文 LIBERO 结果 | 无 |\\n| 备注 | Connector 与 OpenVLA 相同，改进在于 visual trace prompting（在图像上叠加动作历史轨迹）。压缩行为预期与 OpenVLA 相似。 |\\n\\n### 16. X-VLA (ICLR 2026)\\n\\n| 字段 | 信息 |\\n|------|------|\\n| 参数量 | 0.9B |\\n| Vision encoder | Florence-Large (DaViT) |\\n| **Connector 类型** | **Linear projection + Soft Prompts**（vision features 通过 lightweight linear layer 投影到高维空间 + 每个 embodiment 有独立 learnable prompt embeddings 注入 transformer） |\\n| LLM backbone | Standard transformer 24 layers (非预训练 LLM，但使用 Florence 预训练 VLM 初始化) |\\n| 开源状态 | ✅ weights + code, GitHub: [2toinf/X-VLA](https://github.com/2toinf/X-VLA), HF: 2toINF/X-VLA, Apache-2.0 |\\n| LIBERO 支持 | ✅ 原生支持，98% SR |\\n| 改造成本 | 极低（已有 LIBERO 训练权重） |\\n| 论文 LIBERO 结果 | 有: 98% SR |\\n| 备注 | **强力推荐**。Linear projection connector + flow matching action generation。LIBERO SOTA 之一。小模型(0.9B)便于实验。 |\\n\\n### 17. ECoT / Embodied Chain-of-Thought (2024)\\n\\n| 字段 | 信息 |\\n|------|------|\\n| 参数量 | 7B (基于 OpenVLA) |\\n| Vision encoder | SigLIP + DINOv2 (Prismatic) |\\n| **Connector 类型** | **2-layer MLP projector**（与 OpenVLA 相同） |\\n| LLM backbone | Llama-2 7B |\\n| 开源状态 | ✅ code + weights, GitHub: [MichalZawalski/embodied-CoT](https://github.com/MichalZawalski/embodied-CoT), HF: ecot-openvla-7b-bridge/oxe |\\n| LIBERO 支持 | 需改造 |\\n| 改造成本 | 低（基于 OpenVLA） |\\n| 论文 LIBERO 结果 | 无 |\\n| 备注 | Connector 与 OpenVLA 完全相同，增加了 chain-of-thought reasoning。对 connector 压缩研究无新增价值。 |\\n\\n### 18. LingBot-VLA (Ant Group/Robbyant, 2026)\\n\\n| 字段 | 信息 |\\n|------|------|\\n| 参数量 | 4B |\\n| Vision encoder | Qwen2.5-VL 的 ViT（2D-RoPE + window attention） |\\n| **Connector 类型** | **MLP merger**（2-layer MLP with ReLU，2×2 spatial grouping 后投影 + LLM decoder 中有 cross-attention 层融合 visual features） |\\n| LLM backbone | Qwen2.5-VL-3B |\\n| 开源状态 | ✅ weights + code, GitHub: [Robbyant/lingbot-vla](https://github.com/Robbyant/lingbot-vla) |\\n| LIBERO 支持 | 未确认 |\\n| 改造成本 | 中 |\\n| 论文 LIBERO 结果 | 未确认 |\\n| 备注 | Qwen2.5-VL 的 MLP merger 是一种混合 connector：先做 spatial grouping（类似 pixel-shuffle 的空间压缩）再 MLP 投射。Mixture of Transformers 架构。 |\\n\\n---\\n\\n## Connector 类型覆盖分析\\n\\n### 已有数据的 Connector 类型\\n| Connector 类型 | 代表模型 | 压缩行为 |\\n|---------------|----------|----------|\\n| Pixel-shuffle | SmolVLA | Cliff-edge collapse |\\n| 2-layer MLP projector | OpenVLA (Prismatic) | Graded degradation |\\n| Perceiver Resampler | RoboFlamingo | 尝试失败 |\\n| **Linear projection** | **X-VLA** | **Nearly lossless pruning** |\\n\\n### 可新增的 Connector 类型\\n| Connector 类型 | 候选模型 | 特点 | 可行性 |\\n|---------------|----------|------|--------|\\n| **Linear projection** | **π0**, SpatialVLA | 验证 X-VLA 发现的一致性 | ⭐⭐⭐ 高 |\\n| **Cross-attention (Flamingo-style)** | **RoboMM** | 不在 encoder 端压缩，而是 decoder 端通过 cross-attention 选择性融合 | ⭐⭐ 中 |\\n| **CNN patch → direct concat** | Octo | 无独立 connector，图像 patches 直接拼入 transformer | ⭐ 低（架构差异太大） |\\n| **MLP merger + spatial grouping** | LingBot-VLA | 先空间合并再 MLP 投射 + cross-attention | ⭐⭐ 中 |\\n| **Cross-attention tokenizer** | HPT | learnable tokens 通过 cross-attention 聚合 vision features | ⭐ 低（非 VLM 架构） |\\n\\n### 关键发现\\n1. **Linear projection** 是最有价值的新增类型——π0 和 X-VLA 都用这种最简单的 connector，与 OpenVLA 的 2-layer MLP 形成对比\\n2. **Cross-attention** (RoboMM 的 OpenFlamingo 架构) 从根本上不同：不投射拼接，而是 decoder 层间交叉注意力\\n3. 大量模型共享 connector：OpenVLA, CogACT, LLARVA, TraceVLA, ECoT, OpenVLA-OFT 都用 **2-layer MLP**（Prismatic 或 LLaVA 架构）\\n\\n---\\n\\n## Top 推荐：最适合扩展实验的 5 个模型\\n\\n### 🥇 1. π0 (Physical Intelligence)\\n- **Connector**: Linear projection (单层线性)\\n- **推荐理由**: \\n  - 与 OpenVLA 的 2-layer MLP 形成直接对比（linear vs MLP）\\n  - 开源权重 + 代码，社区活跃\\n  - 已有 LIBERO 评测代码\\n  - PaliGemma 架构广为人知\\n  - 3B 参数可在单卡运行\\n- **预期价值**: Linear projection 不增加非线性变换，token 可能保留更多原始 visual feature 结构 → 压缩行为可能与 MLP 不同\\n\\n### 🥈 2. X-VLA\\n- **Connector**: Linear projection + soft prompts\\n- **推荐理由**:\\n  - 同样是 linear projection，与 π0 对比看 soft prompt 的影响\\n  - LIBERO 98% SR，已有训练好的 LIBERO 权重直接可用\\n  - 0.9B 参数，实验成本最低\\n  - ICLR 2026，最新模型\\n  - Apache-2.0 开源\\n- **预期价值**: 验证 linear projection 的压缩行为是否 consistent across models\\n\\n### 🥉 3. DeeR-VLA\\n- **Connector**: Perceiver Resampler + Cross-attention (OpenFlamingo)\\n- **推荐理由**:\\n  - Perceiver Resampler 与 RoboFlamingo 相同架构，但 DeeR-VLA 已验证可训练（CALVIN benchmark 正常工作）\\n  - 给 Perceiver Resampler 第二次机会\\n  - 可对比 RoboFlamingo 的训练失败是架构问题还是实现问题\\n  - Open source with checkpoints\\n- **预期价值**: Perceiver Resampler 本身就做了 attention-based compression → 压缩行为可能与 MLP/linear 截然不同\\n- **风险**: LIBERO 需要自己改造\\n\\n### 4. RoboMM\\n- **Connector**: Cross-attention (OpenFlamingo) + 3D Adapter\\n- **推荐理由**:\\n  - Cross-attention 融合方式从根本上不同于 projection-based connectors\\n  - 已有 LIBERO 结果 (90.7%)\\n  - Open source\\n- **预期价值**: Cross-attention 在 decoder 端动态选择 visual features → 可能展现出与 projection-based 完全不同的压缩模式\\n- **风险**: 架构较复杂，3D adapter 增加变量\\n\\n### 5. OpenVLA-OFT\\n- **Connector**: 2-layer MLP projector (与 OpenVLA 相同)\\n- **推荐理由**:\\n  - Connector 与 OpenVLA 相同，但 action generation 完全不同（continuous + chunking）\\n  - LIBERO 97.1% SOTA\\n  - 可验证 \\\"相同 connector + 不同 action head\\\" 是否影响压缩行为\\n  - 已有完整 LIBERO 代码\\n- **预期价值**: 作为 OpenVLA 的对照组，隔离 connector vs action head 对压缩的影响\\n\\n---\\n\\n## 不推荐的模型及原因\\n\\n| 模型 | 排除原因 |\\n|------|----------|\\n| RT-2-X | 闭源，权重不可用 |\\n| GR-2 | 未开源 |\\n| 3D-VLA | 3D 点云输入，与 2D VLA 差异太大 |\\n| CogACT | Connector 与 OpenVLA 相同（Prismatic MLP），不新增类型 |\\n| LLARVA | Connector 与 OpenVLA 类似（MLP projector），不新增类型 |\\n| TraceVLA | Connector 与 OpenVLA 相同，不新增类型 |\\n| ECoT | Connector 与 OpenVLA 相同，不新增类型 |\\n| HPT | 非 VLM 架构，不适合 connector 压缩叙事 |\\n| GR-1 | 有 Perceiver Resampler（有价值），但无 LIBERO 支持 + 视频生成架构改造成本高 |\\n| Octo | 无独立 connector（CNN patch 直接拼入），架构与标准 VLM 差异太大 |\\n\\n---\\n\\n## 总结：Connector 类型 × 模型矩阵\\n\\n| Connector 类型 | 已有 | 推荐新增 |\\n|---------------|------|----------|\\n| Pixel-shuffle | SmolVLA ✅ | — |\\n| 2-layer MLP projector | OpenVLA ✅ | OpenVLA-OFT（同 connector 不同 action head） |\\n| Perceiver Resampler | RoboFlamingo ❌(失败) | **DeeR-VLA** |\\n| **Linear projection** | **X-VLA ✅** | **π0** |\\n| **Cross-attention** | — | **RoboMM** |\\n\\n实现后可达 **5 种 connector 类型 × 6+ 模型**的全面对比。\\n\\n---\\n\\n## X-VLA 详细架构调研（2026-05-20 新增）\\n\\n### 模型身份确认\\n- **名称**: X-VLA (Soft-Prompted Transformer as Scalable Cross-Embodiment Vision-Language-Action Model)\\n- **论文**: arXiv:2510.10274, ICLR 2026\\n- **GitHub**: [2toinf/X-VLA](https://github.com/2toinf/X-VLA)\\n- **HuggingFace**: [2toINF/X-VLA](https://huggingface.co/collections/2toINF/x-vla)\\n- **参数量**: 0.9B\\n- **许可**: Apache-2.0\\n- **LIBERO SR**: 98.1%\\n\\n### 架构详解\\n\\n```\\nImage (224×224) → Florence-Large (DaViT) → Vision Tokens [B, N, 2048]\\n    → Linear Projection + LayerNorm → [B, N, 1024]\\n    → Merge with Text Token Embeddings → Florence2 Encoder (self-attention)\\n    → Context Features → SoftPromptedTransformer (24 layers, hidden=1024)\\n        + Soft Prompts (32 learnable embeddings per embodiment)\\n        + Noised Action Tokens (flow matching)\\n    → Denoised Action Trajectory [B, 30, 20]\\n```\\n\\n**各组件详情**:\\n\\n| 组件 | 规格 |\\n|------|------|\\n| Vision Encoder | Florence-Large (DaViT): patch_stride=[4,2,2,2] → total stride 32 |\\n| Vision Token 数量 | ~49 tokens (7×7 at 224×224) 或 ~576 tokens (24×24 at 768×768) — **需实际加载模型验证** |\\n| Projection | Linear + LayerNorm, dim 2048 → 1024 (projection_dim=1024) |\\n| Soft Prompts | 32 tokens/embodiment, 0.04% of total params |\\n| Transformer | 24 layers, hidden=1024, 16 heads, mlp_ratio=4.0 |\\n| Action Head | Flow matching, 30 anchor points × 20 dims (EE6D), 10 denoising steps |\\n| Max Sequence | 512 tokens |\\n\\n### HuggingFace 权重\\n| Checkpoint | 用途 | 地址 |\\n|------------|------|------|\\n| X-VLA-Pt | 预训练基座 (cross-embodiment) | 2toINF/X-VLA-Pt |\\n| X-VLA-Libero | LIBERO 全参数微调 (98.1% SR) | 2toINF/X-VLA-Libero |\\n| X-VLA-libero-*-peft | LIBERO LoRA 微调 (各 suite) | 2toINF/X-VLA-libero-spatial-peft 等 |\\n\\n### 环境依赖\\n```\\ntransformers<=4.51.3, torch, einops==0.8.1, timm==1.0.12, \\naccelerate==1.2.1, peft==0.17.1, safetensors==0.4.5,\\nnumpy==1.26.3, scipy==1.15.0, mmengine==0.10.5,\\nfastapi, uvicorn==0.34.3, h5py==3.12.1, pyarrow==20.0.0,\\nav==15.0.0, mediapy==1.2.4\\n```\\nLIBERO 评估另需 Python 3.8 环境。\\n\\n### VTC 集成方案\\n**插入点**: Florence2 `_encode_image()` 输出 → **VTC** → `_merge_input_ids_with_image_features()`\\n\\n**改造清单**:\\n1. 创建 `xvla_vtc_adapter.py`（复用 VisionTokenCompressor，hidden_dim 改 1024）\\n2. 创建 XVLASmartCompressWrapper，hook Florence2 vision 输出\\n3. 修改 merge 逻辑以适应压缩后的 token 数量\\n4. 创建 `train_xvla_smart_compress.py`（参考 X-VLA 的 train.py + peft_train.py）\\n5. 适配 flow matching loss（不同于 OpenVLA 的 cross-entropy）\\n\\n**与 OpenVLA VTC 的关键差异**:\\n| 维度 | OpenVLA | X-VLA |\\n|------|---------|-------|\\n| hidden_dim | 4096 | 1024 |\\n| 原始 vision tokens | 256 | ~49-576 (待验证) |\\n| Action 范式 | Autoregressive (256-bin CE) | Flow matching (MSE+BCE) |\\n| Connector | 2-layer MLP | Linear + LayerNorm |\\n| 模型大小 | 7B | 0.9B |\\n\\n**预计工作量**: 8-12 小时\\n- 代码改造: 4-6h（adapter + training script）\\n- 环境搭建 + 模型下载: 2-3h\\n- 验证 + 调试: 2-3h\\n\\n---\\n\\n## X-VLA Token Importance 分析结果（2026-05-20）\\n\\n### 实验配置\\n- **模型**: X-VLA-0.9B (lerobot/xvla-libero checkpoint)\\n- **数据**: LIBERO-Object (task_index 20-29), 100 images, 10 tasks\\n- **服务器**: westd-41074, cuda:1\\n- **分析脚本**: `/root/autodl-tmp/importance_margin_vla_compress/analyze_xvla_token_importance.py`\\n- **结果文件**: `/root/autodl-tmp/importance_margin_vla_compress/eval_results/xvla_attention_entropy_perlayer.json`\\n\\n### SoftPromptedTransformer 序列布局\\n| Token 类型 | 数量 | 说明 |\\n|-----------|------|------|\\n| Action tokens | 30 | Flow matching denoised action |\\n| VLM features | 64 | Florence2 encoder output (main view) |\\n| Aux visual | 150 | Additional camera views |\\n| Soft prompts | 32 | Embodiment-specific learnable tokens |\\n| **Total** | **276** | |\\n\\n### Entropy Ratio（Action→Vision 注意力熵）\\n- **Overall**: **0.6138** ± 0.1159\\n- **趋势**: 浅层低（L0=0.46, L1=0.34），深层高（L22=0.79, L23=0.71）\\n- 浅层集中注意力于少数 vision tokens，深层趋于均匀\\n\\n### Vision Attention Fraction（Action tokens 分配给 vision tokens 的注意力比例）\\n- 浅层（L0-2）: 33-49% — action tokens 还关注 soft prompts 和 self\\n- 中层（L6-11）: 84-90% — 绝大部分注意力给 vision tokens\\n- 深层（L17-23）: 79-90% — 持续高注意力\\n\\n### Pruning Curve（核心发现）\\n| Retention k | Mean Loss | Normalized |\\n|-------------|-----------|------------|\\n| 0.30 | 0.112945 | **1.0014** |\\n| 0.50 | 0.112823 | 1.0003 |\\n| 0.70 | 0.112789 | 1.0000 |\\n| 0.90 | 0.112789 | 1.0000 |\\n| 0.95 | 0.112789 | 1.0000 |\\n| 1.00 | 0.112789 | 1.0000 |\\n\\n**关键结论**: 丢弃 70% 的 vision tokens（k=0.3）仅导致 0.14% 的 loss 增加。X-VLA 的 vision tokens **几乎完全可压缩**。\\n\\n### 跨模型对比\\n| 模型 | Connector | Entropy Ratio | k=0.3 Norm Loss | 压缩行为 |\\n|------|-----------|---------------|-----------------|----------|\\n| SmolVLA | Pixel-shuffle | ~0.45 (低) | Cliff-edge | 不可压缩 |\\n| OpenVLA | 2-layer MLP | ~0.55 (中) | ~1.15 (15%↑) | 渐进退化 |\\n| **X-VLA** | **Linear proj** | **0.61 (中高)** | **1.0014 (0.14%↑)** | **几乎无损** |\\n\\n### 解读\\n1. **Linear projection connector 产生了高度冗余的 vision token 表示**——大部分信息集中在少数 token 中，L2 norm 可以轻松识别\\n2. Entropy 比 OpenVLA 更高（0.61 vs 0.55），说明注意力分布更均匀，但这不矛盾——均匀分布意味着 \\\"每个 token 被平等关注\\\"，而 pruning 几乎无损意味着 \\\"被关注的内容高度冗余\\\"\\n3. 这是 **connector 架构论文的关键数据点**：linear projection（无非线性变换）保留了 DaViT 输出的原始冗余结构，而 MLP projector（2 层 + GELU）通过非线性变换重新分配了信息，使得 token 间差异更大、更难压缩\\n\\n---\\n\\n## OFT Importance CV 分析结果（2026-05-20）\\n\\n### 结论\\n- **OFT CV = 0.2185**，per-task CV 在 0.211–0.225 之间\\n- 与 OpenVLA (0.215) 高度一致——两者共享相同的 2-layer MLP projector（Prismatic 架构）\\n- **LoRA fine-tuning 不改变 vision token importance 分布**——connector 架构是唯一决定因素\\n\\n### Diagnostic 表格完成状态（5/5）\\n| 模型 | Connector | CV | 压缩行为 |\\n|------|-----------|-----|----------|\\n| SmolVLA | Pixel-shuffle | ~0.08 | Cliff-edge collapse |\\n| OpenVLA | 2-layer MLP | 0.215 | Graded degradation |\\n| OpenVLA-OFT | 2-layer MLP (same) | 0.2185 | 预期与 OpenVLA 相同 |\\n| X-VLA | Linear projection | TBD | Nearly lossless |\\n| RoboFlamingo | Perceiver Resampler | N/A | 训练失败 |\\n\\n### 论文意义\\nOFT 结果支撑 claim: \\\"token importance distribution is an intrinsic property of the connector architecture, invariant to downstream fine-tuning strategy (LoRA vs full)\\\"\\n\\n---\\n\\n## 失败模式记录\\n\\n- [2026-05-21] **π0.5 自定义 eval 脚本 bug**: `eval_pi05_pruning_libero.py` 的 `patched_embed_image` 函数导致 0% SR，而官方 eval 脚本在同一 checkpoint 上 ~100% SR。→ 新模型接入时，必须先用官方 eval 脚本验证 checkpoint 可用性，确认后再写自定义 pruning eval 脚本。不要假设自定义 patch 正确。\\n\\n- [2026-05-21] **OpenVLA eval 4 实验批量失败 (westd-38929)**:\\n  - **失败实验**: eval_openvla_l2norm_k05_object_seed42 (PID 568225), eval_openvla_random_k03_object_seed42 (PID 568905), eval_openvla_l2norm_k07_object_seed42 (PID 569611), eval_openvla_l2norm_k03_object_seed42 (PID 570309)\\n  - **根因**: **AutoDL 容器 GPU 缩配**。主机有 9 块 NVIDIA RTX PRO 6000 Blackwell (各 97GB)，但容器当前只挂载了 `/dev/nvidia2` 一块 GPU。4 个实验分别在 CUDA_VISIBLE_DEVICES=0/1/2/3 启动，运行 ~1h43m 后 GPU 设备被平台回收，进程收到 SIGKILL 无任何 traceback。\\n  - **证据**:\\n    - `nvidia-smi -L` 只显示 1 块 GPU (Device Minor 2)，而 `/proc/driver/nvidia/gpus/` 显示主机有 9 块\\n    - 4 个日志文件在 14:45-14:49 间依次停止写入（3 分钟跨度，非瞬时），末尾均为正常进度输出无 error\\n    - 各实验完成了 Task 1-3，在 Task 4/10 中被杀（~30% 完成度）\\n    - 系统 RAM 充足（1TB 中仅用 46GB），排除 CPU OOM\\n    - 无 tmux session，进程通过 nohup 方式运行\\n  - **修复建议**:\\n    1. 在 AutoDL 控制台恢复实例到 4 GPU 配置（或至少确认 GPU 分配稳定）\\n    2. 重新启动 4 个实验，建议使用 tmux 以防 SSH 断连\\n    3. 如果无法恢复多 GPU，可在单 GPU 上顺序运行（每个实验约 5.5h，共 ~22h）\\n    4. 启动命令参考（单 GPU 顺序）:\\n       ```bash\\n       tmux new -s openvla_eval\\n       source /root/miniconda3/etc/profile.d/conda.sh && conda activate base\\n       cd /root/autodl-tmp/importance_margin_vla_compress\\n       CUDA_VISIBLE_DEVICES=0 python -u eval_openvla_l2norm_libero.py --mode l2norm_prune --k_ratio 0.5 --suite libero_object --seed 42 > logs/eval_openvla_l2norm_k05_seed42.log 2>&1\\n       CUDA_VISIBLE_DEVICES=0 python -u eval_openvla_l2norm_libero.py --mode random_prune --k_ratio 0.3 --suite libero_object --seed 42 > logs/eval_openvla_random_k03_seed42.log 2>&1\\n       CUDA_VISIBLE_DEVICES=0 python -u eval_openvla_l2norm_libero.py --mode l2norm_prune --k_ratio 0.7 --suite libero_object --seed 42 > logs/eval_openvla_l2norm_k07_seed42.log 2>&1\\n       CUDA_VISIBLE_DEVICES=0 python -u eval_openvla_l2norm_libero.py --mode l2norm_prune --k_ratio 0.3 --suite libero_object --seed 42 > logs/eval_openvla_l2norm_k03_seed42.log 2>&1\\n       ```\\n\\n---\\n\\n## π0.5 跨 suite 对比（2026-05-21）\\n\\n**模型**: π0.5 (PaliGemma, linear projection connector, CV=0.055)\\n**数据来源**: registry 中所有 status=DONE 且有有效 metrics 的 pi05 实验\\n\\n### Object Suite（baseline=98.2%, eval_pi05_baseline_object_seed42）\\n\\n| k | L2norm SR (%) | L2norm exp_ids | Random SR (%) | Random exp_ids |\\n|---|--------------|----------------|--------------|----------------|\\n| 0.9 | **98.2** (s42) | eval_pi05_l2norm_k09_object_seed42_v2 | **10.8** avg [12.0(s42), 9.6(s43)] | eval_pi05_random_k09_object_seed42_v2, eval_pi05_random_k09_object_seed43 |\\n| 0.7 | **56.4** avg [55.0(s42), 56.4(s43), 57.8(s43v2)] | eval_pi05_l2norm_k07_object_seed42, _seed43, _seed43_v2 | **75.5** avg [77.2(s42), 73.8(s43)] | eval_pi05_random_k07_object_seed42, _seed43 |\\n| 0.5 | **33.5** avg [33.4(s42), 33.6(s43)] | eval_pi05_l2norm_k05_object_seed42, _seed43 | **68.9** avg [69.4(s42), 68.4(s43)] | eval_pi05_random_k05_object_seed42, _seed43 |\\n| 0.3 | **53.2** avg [51.0(s42), 55.4(s43)] | eval_pi05_l2norm_k03_object_seed42, _seed43 | **36.4** (s42) | eval_pi05_random_k03_object_seed42 |\\n| 0.1 | **2.6** (s42) | eval_pi05_l2norm_k01_object_seed42 | — | — |\\n\\n### Spatial Suite（baseline=97.2%, eval_pi05_baseline_spatial_seed42）\\n\\n| k | L2norm SR (%) | Random SR (%) | Random exp_ids |\\n|---|--------------|--------------|----------------|\\n| 0.9 | — (pending) | — (pending) | — |\\n| 0.7 | — (pending) | — (submitted) | — |\\n| 0.5 | — (running) | **71.6** (s42) | eval_pi05_random_k05_spatial_seed42 |\\n| 0.3 | — (running) | — (submitted) | — |\\n\\n### Cross-suite 一致性分析\\n\\n**Random k=0.5 对比**:\\n- Object: **68.9%** (seed42=69.4%, seed43=68.4%)\\n- Spatial: **71.6%** (seed42)\\n- **Delta: 2.7pp** — 高度一致\\n\\n结论：Random pruning 在 k=0.5 的表现跨 suite 具有强一致性（差异仅 2.7pp），说明 π0.5 的 vision token 冗余结构不依赖于具体 task 类型。Spatial 略高于 Object 可能因为 Spatial 任务（同一物体不同位置）对视觉信息量要求更低。\\n\\n### 关键现象\\n\\n1. **L2norm 非单调 V-shape**：k=0.5 是谷底(33.5%)，k=0.3 反弹到 53.2%。多 seed 确认。原因待查——可能 L2 norm 在 50% 保留时恰好选中了信息量最差的 token 子集。\\n\\n2. **Random k=0.9 异常崩塌**：仅保留 90% token 时 random pruning SR 降至 ~10.8%（双 seed 确认 12.0%/9.6%），而 L2norm k=0.9 正常(98.2%)。这是所有模型中未见过的现象——移除 10% random token 即可摧毁模型。推测 π0.5 少数 token 承载关键位置信息，random 删除有 ~90% 概率命中关键 token。\\n\\n3. **Random 优于 L2norm 的 k 区间**：k=0.5(random 68.9% vs L2norm 33.5%)和 k=0.7(random 75.5% vs L2norm 56.4%)时 random 大幅优于 L2norm。说明 L2 norm 不是 π0.5 vision token importance 的好 proxy——CV=0.055 意味着 L2 norm 几乎无区分度。\\n\\n4. **Failed/killed 实验（已排除）**: eval_pi05_random_k07_object_seed42_v2(killed), _v3(killed), eval_pi05_random_k085_object_seed42(failed), eval_pi05_random_k095_object_seed42(failed), eval_pi05_random_k09_fixedmask_object_seed42(network error)。\\n\", \"total_chars\": 25431, \"truncated\": false}, \"error\": null, \"metadata\": {}}"
    }
  }
}
````

</details>

---

### Assistant

_source line 34_

<details><summary>Logged reasoning block</summary>

```text
Now I need to update the memory.md with the new Spatial result for random k=0.7. The Spatial Suite table currently shows random k=0.7 as "submitted" but now we have the result: 74.4%. Let me update the memory.md.

Also, I should update the cross-suite analysis section.

Let me write the updated memory.md content for the Spatial suite section and the cross-suite analysis.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "bcd9e5e6-c86c-4bf9-9402-037b79b77b15",
  "uuid": "3f5ddc84-1379-4d77-96a3-bfd97f71d20c",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AXT2yVmBBJNWMc58qGmPLd",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 14842,
      "cache_read_input_tokens": 42563,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 14842
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

_source line 35_

现在更新 memory.md，添加 random k=0.7 Spatial 结果。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "bcd9e5e6-c86c-4bf9-9402-037b79b77b15",
  "uuid": "1c6d99ac-16ef-4ad7-8ae6-e64d2b8b87ee",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AXT2yVmBBJNWMc58qGmPLd",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 14842,
      "cache_read_input_tokens": 42563,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 14842
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

_source line 36_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__save_project_file · `toolu_019Krqji5dXfWfCocDTGKsWF`</summary>

````json
{
  "project": "importance_margin_vla_compress",
  "file": "memory.md",
  "content": "# VLA 模型全面调研报告\n\n**调研日期**: 2026-05-20\n**目的**: 寻找不同 connector 架构的开源 VLA 模型，扩展 vision connector 对 token 可压缩性影响的实验\n\n---\n\n## 已有实验数据\n\n| 模型 | Connector | 压缩行为 |\n|------|-----------|----------|\n| SmolVLA | Pixel-shuffle | Cliff-edge collapse (k=0.95 → 0% SR) |\n| OpenVLA | 2-layer MLP projector | Graded degradation (线性下降) |\n| RoboFlamingo | Perceiver Resampler | 尝试失败 |\n| **X-VLA** | **Linear projection** | **Nearly lossless (k=0.3 → norm=1.0014)** |\n\n---\n\n## 完整模型调研表\n\n### 1. Octo (UC Berkeley, 2024)\n\n| 字段 | 信息 |\n|------|------|\n| 参数量 | 27M (Small) / 93M (Base) |\n| Vision encoder | Shallow CNN (从头训练，非预训练 ViT) |\n| **Connector 类型** | **CNN patch encoder → 直接拼接进 transformer（无独立 connector）** |\n| LLM backbone | 纯 transformer（非预训练 LLM），decoder-only |\n| 开源状态 | ✅ weights + code, GitHub: [octo-models/octo](https://github.com/octo-models/octo), HF: rail-berkeley/octo-base |\n| LIBERO 支持 | ✅ 原生支持，fine-tune 后 ~72% SR |\n| 改造成本 | 低（已有 LIBERO fine-tune 代码） |\n| 论文 LIBERO 结果 | 有: ~72% (fine-tuned) |\n| 备注 | 非标准 VLM→LLM 架构，是 transformer-based diffusion policy。图像通过浅层 CNN 编码为 16×16 patches 后直接拼入 transformer 序列。语言用 T5 tokenizer/encoder。Action head 是 diffusion policy。 |\n\n### 2. CogACT (Microsoft/Tsinghua, 2024)\n\n| 字段 | 信息 |\n|------|------|\n| 参数量 | ~7.1B (7B Prismatic VLM + 89M-300M DiT action module) |\n| Vision encoder | DINOv2 + SigLIP (双 encoder，channel 拼接) |\n| **Connector 类型** | **2-layer MLP projector**（Prismatic 架构：DINOv2+SigLIP feature → channel concat → 2-layer MLP → Llama-2 embedding space） |\n| LLM backbone | Llama-2 7B (via Prismatic-7B) |\n| 开源状态 | ✅ weights + code, GitHub: [microsoft/CogACT](https://github.com/microsoft/CogACT), HF: CogACT/CogACT-Base, CogACT/CogACT-Small |\n| LIBERO 支持 | 需改造（paper 用 SimplerEnv + 真机） |\n| 改造成本 | 中（需接 LIBERO data pipeline + action space） |\n| 论文 LIBERO 结果 | 无 |\n| 备注 | 核心创新在 DiT action module（将 VLM 认知特征作为 condition 输入扩散 transformer 生成动作）。Connector 与 OpenVLA 相同（都基于 Prismatic） |\n\n### 3. HPT (MIT, NeurIPS 2024)\n\n| 字段 | 信息 |\n|------|------|\n| 参数量 | 3.1M (S) / 12.6M (B) / 50.5M (L) / 226.8M (XL) / 1.1B (Huge) |\n| Vision encoder | 预训练冻结 ResNet18 |\n| **Connector 类型** | **Cross-attention tokenizer**（learnable tokens 通过 cross-attention 聚合 vision features → 固定 16 tokens，每个 camera view 有独立 MLP projector） |\n| LLM backbone | 无（纯 decoder-only transformer，从头训练） |\n| 开源状态 | ✅ weights + code, GitHub: [liruiw/HPT](https://github.com/liruiw/HPT), HF: liruiw/hpt |\n| LIBERO 支持 | 未确认（paper 评测 6 个 benchmark） |\n| 改造成本 | 中（非标准 VLM 架构，需改 stem + action head） |\n| 论文 LIBERO 结果 | 无 |\n| 备注 | 非 VLM→LLM 架构。Cross-attention tokenizer 类似 Perceiver 但更轻量（8 heads, 64 dim/head）。跨 embodiment 预训练。 |\n\n### 4. RT-2-X (Google DeepMind, 2023)\n\n| 字段 | 信息 |\n|------|------|\n| 参数量 | 55B |\n| Vision encoder | ViT (PaLI-X 的视觉编码器) |\n| **Connector 类型** | 未公开（闭源） |\n| LLM backbone | PaLI-X / PaLM-E |\n| 开源状态 | ❌ **闭源**，权重不公开 |\n| LIBERO 支持 | 不可行 |\n| 改造成本 | 不可行 |\n| 论文 LIBERO 结果 | 无 |\n| 备注 | 闭源模型，无法使用 |\n\n### 5. GR-1 (ByteDance, 2023)\n\n| 字段 | 信息 |\n|------|------|\n| 参数量 | 未明确公布 |\n| Vision encoder | MAE ViT-Base (预训练) |\n| **Connector 类型** | **Perceiver Resampler**（将 MAE ViT 视觉 token 数量压缩）+ linear layers 对齐维度 |\n| LLM backbone | GPT-style causal transformer（非预训练 LLM） |\n| 开源状态 | ✅ weights + code, GitHub: [bytedance/GR-1](https://github.com/bytedance/GR-1), Apache-2.0 |\n| LIBERO 支持 | 需改造（paper 只有 CALVIN） |\n| 改造成本 | 高（需改 data pipeline、action space、视频生成部分可能要适配） |\n| 论文 LIBERO 结果 | 无（CALVIN: 94.9%） |\n| 备注 | 既做动作预测又做视频生成（future image prediction）。语言用 CLIP text encoder。使用 Perceiver Resampler 这一点很有价值——与 RoboFlamingo 类似但架构不同。 |\n\n### 6. GR-2 (ByteDance, 2024)\n\n| 字段 | 信息 |\n|------|------|\n| 参数量 | 未公布 |\n| Vision encoder | 未公布 |\n| **Connector 类型** | 未公布 |\n| LLM backbone | 未公布 |\n| 开源状态 | ❌ **未开源**，代码/权重未释放 |\n| LIBERO 支持 | 不可行 |\n| 改造成本 | 不可行 |\n| 论文 LIBERO 结果 | 无 |\n| 备注 | GR-1 的后续，但未开源 |\n\n### 7. LLARVA (2024)\n\n| 字段 | 信息 |\n|------|------|\n| 参数量 | 7B |\n| Vision encoder | CLIP ViT-L/14 |\n| **Connector 类型** | **MLP projector**（LLaVA-style，2-layer MLP with GELU） |\n| LLM backbone | Llama-2 7B |\n| 开源状态 | ✅ code + LoRA weights, GitHub: [Dantong88/LLARVA](https://github.com/Dantong88/LLARVA), Apache-2.0 |\n| LIBERO 支持 | 需改造 |\n| 改造成本 | 中（需接 action head + LIBERO data pipeline） |\n| 论文 LIBERO 结果 | 无 |\n| 备注 | 预测 visual traces (2D 轨迹) 作为中间表示。Connector 与 OpenVLA 类似（都是 MLP projector），但用 CLIP 而非 Prismatic 双 encoder |\n\n### 8. RoboVLMs (2024)\n\n| 字段 | 信息 |\n|------|------|\n| 参数量 | 不定（框架） |\n| Vision encoder | 支持多种 VLM backbone |\n| **Connector 类型** | 取决于所选 VLM（框架支持多种） |\n| LLM backbone | 取决于所选 VLM |\n| 开源状态 | ✅ code + models, GitHub: [Robot-VLAs/RoboVLMs](https://github.com/Robot-VLAs/RoboVLMs) |\n| LIBERO 支持 | 需确认 |\n| 改造成本 | 低-中（框架设计灵活） |\n| 论文 LIBERO 结果 | 未确认 |\n| 备注 | 这是一个**框架**而非单一模型。实验了 8+ VLM backbone × 4 policy 架构。最佳模型用 Kosmos backbone。对我们的 connector 对比研究有参考价值但不直接使用。 |\n\n### 9. 3D-VLA (UMass, ICML 2024)\n\n| 字段 | 信息 |\n|------|------|\n| 参数量 | 未明确 |\n| Vision encoder | 3D feature extraction（point cloud based） |\n| **Connector 类型** | **Interaction tokens**（3D-LLM 架构，用交互 token 嵌入 embodied 环境） |\n| LLM backbone | 基于 3D-LLM |\n| 开源状态 | ✅ code + diffusion models, GitHub: [UMass-Embodied-AGI/3D-VLA](https://github.com/UMass-Embodied-AGI/3D-VLA), HF: anyezhy |\n| LIBERO 支持 | 需大量改造（paper 用 RLBench） |\n| 改造成本 | 高（3D 点云输入，与 LIBERO 2D 图像差异大） |\n| 论文 LIBERO 结果 | 无 |\n| 备注 | 基于 3D 点云的 VLA，与我们研究的 2D 图像 → connector → LLM 管道差异太大，不推荐 |\n\n### 10. π0 / pi-zero (Physical Intelligence, 2024-2025)\n\n| 字段 | 信息 |\n|------|------|\n| 参数量 | ~3.3B (400M SigLIP + 2.6B Gemma + ~300M action expert) |\n| Vision encoder | SigLIP-So400m (400M params) |\n| **Connector 类型** | **Linear projection**（单层线性层，将 SigLIP token 投影到 Gemma embedding space） |\n| LLM backbone | Gemma 2B (via PaliGemma) |\n| 开源状态 | ✅ weights + code, GitHub: [Physical-Intelligence/openpi](https://github.com/Physical-Intelligence/openpi), HF 有 PyTorch port |\n| LIBERO 支持 | ✅ 有评测（LIBERO-PRO 中被评测） |\n| 改造成本 | 低（已有 LIBERO 评测代码） |\n| 论文 LIBERO 结果 | 有（LIBERO-PRO 中有结果） |\n| 备注 | **强力推荐**。Linear projection 是最简单的 connector，与 OpenVLA 的 2-layer MLP 形成鲜明对比。Action expert 通过 MoE 架构耦合。Flow matching 生成动作。 |\n\n### 11. OpenVLA-OFT (Stanford, 2025)\n\n| 字段 | 信息 |\n|------|------|\n| 参数量 | 7B |\n| Vision encoder | SigLIP + DINOv2 (Prismatic) |\n| **Connector 类型** | **2-layer MLP projector**（与 OpenVLA 相同的 Prismatic connector） |\n| LLM backbone | Llama-2 7B |\n| 开源状态 | ✅ weights + code, GitHub: [moojink/openvla-oft](https://github.com/moojink/openvla-oft) |\n| LIBERO 支持 | ✅ 原生支持，SOTA 97.1% |\n| 改造成本 | 极低（已有完整 LIBERO fine-tune + eval） |\n| 论文 LIBERO 结果 | 有: 97.1% SR (4 suite avg) |\n| 备注 | Connector 与 OpenVLA 完全相同。改进在 fine-tuning recipe（continuous actions, action chunking, bidirectional attention）。对压缩实验来说，connector 级别的差异与 OpenVLA 相同，但 action generation 方式不同，可能影响压缩行为。 |\n\n### 12. RoboMM (2024)\n\n| 字段 | 信息 |\n|------|------|\n| 参数量 | 未明确公布 |\n| Vision encoder | CLIP (via OpenFlamingo) |\n| **Connector 类型** | **3D Perception Adapter (UVFormer)** + **Cross-attention**（OpenFlamingo 风格：text queries attend to visual features through cross-attention layers） |\n| LLM backbone | OpenFlamingo (cross-attention decoder) |\n| 开源状态 | ✅ code, GitHub: [RoboUniview/RoboMM](https://github.com/RoboUniview/RoboMM) |\n| LIBERO 支持 | ✅ 有评测 |\n| 改造成本 | 低-中 |\n| 论文 LIBERO 结果 | 有: 90.7% SR |\n| 备注 | Cross-attention connector 是独特的融合方式（与 MLP/linear 的 \"先投射再拼接\" 不同）。还有 occupancy supervision 的 3D adapter。多模态解码器增强感知。 |\n\n### 13. SpatialVLA (2025, RSS)\n\n| 字段 | 信息 |\n|------|------|\n| 参数量 | ~4B |\n| Vision encoder | SigLIP |\n| **Connector 类型** | **Linear projection + Ego3D Position Encoding**（PaliGemma2 的 linear connector + MLP(sinusoidal(3D positions)) 叠加到 visual tokens 上） |\n| LLM backbone | Gemma (via PaliGemma2) |\n| 开源状态 | ✅ weights + code, GitHub: [SpatialVLA/SpatialVLA](https://github.com/SpatialVLA/SpatialVLA), HF: IPEC-COMMUNITY/spatialvla-4b-224-pt |\n| LIBERO 支持 | 未确认 |\n| 改造成本 | 中（需接 LIBERO data pipeline） |\n| 论文 LIBERO 结果 | 无 |\n| 备注 | 基于 PaliGemma2，connector 本质上是 linear projection（与 π0 相同），加了 3D spatial encoding。Adaptive Action Grids 只输出 3 个 action token（其他模型 7 个）。 |\n\n### 14. DeeR-VLA (2024)\n\n| 字段 | 信息 |\n|------|------|\n| 参数量 | 3B / 9B (OpenFlamingo 变体) |\n| Vision encoder | CLIP ViT-L/14 (428M params) |\n| **Connector 类型** | **Perceiver Resampler + Cross-attention**（OpenFlamingo 架构：CLIP features → Perceiver Resampler → learnable cross-attention blocks 注入 LLM 层间） |\n| LLM backbone | MPT-1B (3B 版) / MPT-7B (9B 版) |\n| 开源状态 | ✅ code + checkpoints, GitHub: [yueyang130/DeeR-VLA](https://github.com/yueyang130/DeeR-VLA) |\n| LIBERO 支持 | 需改造（paper 只有 CALVIN） |\n| 改造成本 | 中-高（需接 LIBERO pipeline，且多 exit 架构增加复杂度） |\n| 论文 LIBERO 结果 | 无（CALVIN benchmark） |\n| 备注 | **Perceiver Resampler** 与 RoboFlamingo 相同架构基础。动态 early exit 是额外功能。可作为 Perceiver Resampler 实验的替代方案。 |\n\n### 15. TraceVLA (UMD, ICLR 2025)\n\n| 字段 | 信息 |\n|------|------|\n| 参数量 | 7B (OpenVLA-based) / 4B (Phi-3-Vision-based) |\n| Vision encoder | SigLIP + DINOv2 (OpenVLA 版) / CLIP ViT (Phi-3 版) |\n| **Connector 类型** | **2-layer MLP projector**（与 OpenVLA 相同） |\n| LLM backbone | Llama-2 7B (OpenVLA 版) / Phi-3 4B |\n| 开源状态 | ✅ code + weights, GitHub: [umd-huang-lab/tracevla](https://github.com/umd-huang-lab/tracevla), HF: furonghuang-lab/tracevla_7b, MIT license |\n| LIBERO 支持 | 未确认（SimplerEnv + 真机） |\n| 改造成本 | 低（基于 OpenVLA 改造） |\n| 论文 LIBERO 结果 | 无 |\n| 备注 | Connector 与 OpenVLA 相同，改进在于 visual trace prompting（在图像上叠加动作历史轨迹）。压缩行为预期与 OpenVLA 相似。 |\n\n### 16. X-VLA (ICLR 2026)\n\n| 字段 | 信息 |\n|------|------|\n| 参数量 | 0.9B |\n| Vision encoder | Florence-Large (DaViT) |\n| **Connector 类型** | **Linear projection + Soft Prompts**（vision features 通过 lightweight linear layer 投影到高维空间 + 每个 embodiment 有独立 learnable prompt embeddings 注入 transformer） |\n| LLM backbone | Standard transformer 24 layers (非预训练 LLM，但使用 Florence 预训练 VLM 初始化) |\n| 开源状态 | ✅ weights + code, GitHub: [2toinf/X-VLA](https://github.com/2toinf/X-VLA), HF: 2toINF/X-VLA, Apache-2.0 |\n| LIBERO 支持 | ✅ 原生支持，98% SR |\n| 改造成本 | 极低（已有 LIBERO 训练权重） |\n| 论文 LIBERO 结果 | 有: 98% SR |\n| 备注 | **强力推荐**。Linear projection connector + flow matching action generation。LIBERO SOTA 之一。小模型(0.9B)便于实验。 |\n\n### 17. ECoT / Embodied Chain-of-Thought (2024)\n\n| 字段 | 信息 |\n|------|------|\n| 参数量 | 7B (基于 OpenVLA) |\n| Vision encoder | SigLIP + DINOv2 (Prismatic) |\n| **Connector 类型** | **2-layer MLP projector**（与 OpenVLA 相同） |\n| LLM backbone | Llama-2 7B |\n| 开源状态 | ✅ code + weights, GitHub: [MichalZawalski/embodied-CoT](https://github.com/MichalZawalski/embodied-CoT), HF: ecot-openvla-7b-bridge/oxe |\n| LIBERO 支持 | 需改造 |\n| 改造成本 | 低（基于 OpenVLA） |\n| 论文 LIBERO 结果 | 无 |\n| 备注 | Connector 与 OpenVLA 完全相同，增加了 chain-of-thought reasoning。对 connector 压缩研究无新增价值。 |\n\n### 18. LingBot-VLA (Ant Group/Robbyant, 2026)\n\n| 字段 | 信息 |\n|------|------|\n| 参数量 | 4B |\n| Vision encoder | Qwen2.5-VL 的 ViT（2D-RoPE + window attention） |\n| **Connector 类型** | **MLP merger**（2-layer MLP with ReLU，2×2 spatial grouping 后投影 + LLM decoder 中有 cross-attention 层融合 visual features） |\n| LLM backbone | Qwen2.5-VL-3B |\n| 开源状态 | ✅ weights + code, GitHub: [Robbyant/lingbot-vla](https://github.com/Robbyant/lingbot-vla) |\n| LIBERO 支持 | 未确认 |\n| 改造成本 | 中 |\n| 论文 LIBERO 结果 | 未确认 |\n| 备注 | Qwen2.5-VL 的 MLP merger 是一种混合 connector：先做 spatial grouping（类似 pixel-shuffle 的空间压缩）再 MLP 投射。Mixture of Transformers 架构。 |\n\n---\n\n## Connector 类型覆盖分析\n\n### 已有数据的 Connector 类型\n| Connector 类型 | 代表模型 | 压缩行为 |\n|---------------|----------|----------|\n| Pixel-shuffle | SmolVLA | Cliff-edge collapse |\n| 2-layer MLP projector | OpenVLA (Prismatic) | Graded degradation |\n| Perceiver Resampler | RoboFlamingo | 尝试失败 |\n| **Linear projection** | **X-VLA** | **Nearly lossless pruning** |\n\n### 可新增的 Connector 类型\n| Connector 类型 | 候选模型 | 特点 | 可行性 |\n|---------------|----------|------|--------|\n| **Linear projection** | **π0**, SpatialVLA | 验证 X-VLA 发现的一致性 | ⭐⭐⭐ 高 |\n| **Cross-attention (Flamingo-style)** | **RoboMM** | 不在 encoder 端压缩，而是 decoder 端通过 cross-attention 选择性融合 | ⭐⭐ 中 |\n| **CNN patch → direct concat** | Octo | 无独立 connector，图像 patches 直接拼入 transformer | ⭐ 低（架构差异太大） |\n| **MLP merger + spatial grouping** | LingBot-VLA | 先空间合并再 MLP 投射 + cross-attention | ⭐⭐ 中 |\n| **Cross-attention tokenizer** | HPT | learnable tokens 通过 cross-attention 聚合 vision features | ⭐ 低（非 VLM 架构） |\n\n### 关键发现\n1. **Linear projection** 是最有价值的新增类型——π0 和 X-VLA 都用这种最简单的 connector，与 OpenVLA 的 2-layer MLP 形成对比\n2. **Cross-attention** (RoboMM 的 OpenFlamingo 架构) 从根本上不同：不投射拼接，而是 decoder 层间交叉注意力\n3. 大量模型共享 connector：OpenVLA, CogACT, LLARVA, TraceVLA, ECoT, OpenVLA-OFT 都用 **2-layer MLP**（Prismatic 或 LLaVA 架构）\n\n---\n\n## Top 推荐：最适合扩展实验的 5 个模型\n\n### 🥇 1. π0 (Physical Intelligence)\n- **Connector**: Linear projection (单层线性)\n- **推荐理由**: \n  - 与 OpenVLA 的 2-layer MLP 形成直接对比（linear vs MLP）\n  - 开源权重 + 代码，社区活跃\n  - 已有 LIBERO 评测代码\n  - PaliGemma 架构广为人知\n  - 3B 参数可在单卡运行\n- **预期价值**: Linear projection 不增加非线性变换，token 可能保留更多原始 visual feature 结构 → 压缩行为可能与 MLP 不同\n\n### 🥈 2. X-VLA\n- **Connector**: Linear projection + soft prompts\n- **推荐理由**:\n  - 同样是 linear projection，与 π0 对比看 soft prompt 的影响\n  - LIBERO 98% SR，已有训练好的 LIBERO 权重直接可用\n  - 0.9B 参数，实验成本最低\n  - ICLR 2026，最新模型\n  - Apache-2.0 开源\n- **预期价值**: 验证 linear projection 的压缩行为是否 consistent across models\n\n### 🥉 3. DeeR-VLA\n- **Connector**: Perceiver Resampler + Cross-attention (OpenFlamingo)\n- **推荐理由**:\n  - Perceiver Resampler 与 RoboFlamingo 相同架构，但 DeeR-VLA 已验证可训练（CALVIN benchmark 正常工作）\n  - 给 Perceiver Resampler 第二次机会\n  - 可对比 RoboFlamingo 的训练失败是架构问题还是实现问题\n  - Open source with checkpoints\n- **预期价值**: Perceiver Resampler 本身就做了 attention-based compression → 压缩行为可能与 MLP/linear 截然不同\n- **风险**: LIBERO 需要自己改造\n\n### 4. RoboMM\n- **Connector**: Cross-attention (OpenFlamingo) + 3D Adapter\n- **推荐理由**:\n  - Cross-attention 融合方式从根本上不同于 projection-based connectors\n  - 已有 LIBERO 结果 (90.7%)\n  - Open source\n- **预期价值**: Cross-attention 在 decoder 端动态选择 visual features → 可能展现出与 projection-based 完全不同的压缩模式\n- **风险**: 架构较复杂，3D adapter 增加变量\n\n### 5. OpenVLA-OFT\n- **Connector**: 2-layer MLP projector (与 OpenVLA 相同)\n- **推荐理由**:\n  - Connector 与 OpenVLA 相同，但 action generation 完全不同（continuous + chunking）\n  - LIBERO 97.1% SOTA\n  - 可验证 \"相同 connector + 不同 action head\" 是否影响压缩行为\n  - 已有完整 LIBERO 代码\n- **预期价值**: 作为 OpenVLA 的对照组，隔离 connector vs action head 对压缩的影响\n\n---\n\n## 不推荐的模型及原因\n\n| 模型 | 排除原因 |\n|------|----------|\n| RT-2-X | 闭源，权重不可用 |\n| GR-2 | 未开源 |\n| 3D-VLA | 3D 点云输入，与 2D VLA 差异太大 |\n| CogACT | Connector 与 OpenVLA 相同（Prismatic MLP），不新增类型 |\n| LLARVA | Connector 与 OpenVLA 类似（MLP projector），不新增类型 |\n| TraceVLA | Connector 与 OpenVLA 相同，不新增类型 |\n| ECoT | Connector 与 OpenVLA 相同，不新增类型 |\n| HPT | 非 VLM 架构，不适合 connector 压缩叙事 |\n| GR-1 | 有 Perceiver Resampler（有价值），但无 LIBERO 支持 + 视频生成架构改造成本高 |\n| Octo | 无独立 connector（CNN patch 直接拼入），架构与标准 VLM 差异太大 |\n\n---\n\n## 总结：Connector 类型 × 模型矩阵\n\n| Connector 类型 | 已有 | 推荐新增 |\n|---------------|------|----------|\n| Pixel-shuffle | SmolVLA ✅ | — |\n| 2-layer MLP projector | OpenVLA ✅ | OpenVLA-OFT（同 connector 不同 action head） |\n| Perceiver Resampler | RoboFlamingo ❌(失败) | **DeeR-VLA** |\n| **Linear projection** | **X-VLA ✅** | **π0** |\n| **Cross-attention** | — | **RoboMM** |\n\n实现后可达 **5 种 connector 类型 × 6+ 模型**的全面对比。\n\n---\n\n## X-VLA 详细架构调研（2026-05-20 新增）\n\n### 模型身份确认\n- **名称**: X-VLA (Soft-Prompted Transformer as Scalable Cross-Embodiment Vision-Language-Action Model)\n- **论文**: arXiv:2510.10274, ICLR 2026\n- **GitHub**: [2toinf/X-VLA](https://github.com/2toinf/X-VLA)\n- **HuggingFace**: [2toINF/X-VLA](https://huggingface.co/collections/2toINF/x-vla)\n- **参数量**: 0.9B\n- **许可**: Apache-2.0\n- **LIBERO SR**: 98.1%\n\n### 架构详解\n\n```\nImage (224×224) → Florence-Large (DaViT) → Vision Tokens [B, N, 2048]\n    → Linear Projection + LayerNorm → [B, N, 1024]\n    → Merge with Text Token Embeddings → Florence2 Encoder (self-attention)\n    → Context Features → SoftPromptedTransformer (24 layers, hidden=1024)\n        + Soft Prompts (32 learnable embeddings per embodiment)\n        + Noised Action Tokens (flow matching)\n    → Denoised Action Trajectory [B, 30, 20]\n```\n\n**各组件详情**:\n\n| 组件 | 规格 |\n|------|------|\n| Vision Encoder | Florence-Large (DaViT): patch_stride=[4,2,2,2] → total stride 32 |\n| Vision Token 数量 | ~49 tokens (7×7 at 224×224) 或 ~576 tokens (24×24 at 768×768) — **需实际加载模型验证** |\n| Projection | Linear + LayerNorm, dim 2048 → 1024 (projection_dim=1024) |\n| Soft Prompts | 32 tokens/embodiment, 0.04% of total params |\n| Transformer | 24 layers, hidden=1024, 16 heads, mlp_ratio=4.0 |\n| Action Head | Flow matching, 30 anchor points × 20 dims (EE6D), 10 denoising steps |\n| Max Sequence | 512 tokens |\n\n### HuggingFace 权重\n| Checkpoint | 用途 | 地址 |\n|------------|------|------|\n| X-VLA-Pt | 预训练基座 (cross-embodiment) | 2toINF/X-VLA-Pt |\n| X-VLA-Libero | LIBERO 全参数微调 (98.1% SR) | 2toINF/X-VLA-Libero |\n| X-VLA-libero-*-peft | LIBERO LoRA 微调 (各 suite) | 2toINF/X-VLA-libero-spatial-peft 等 |\n\n### 环境依赖\n```\ntransformers<=4.51.3, torch, einops==0.8.1, timm==1.0.12, \naccelerate==1.2.1, peft==0.17.1, safetensors==0.4.5,\nnumpy==1.26.3, scipy==1.15.0, mmengine==0.10.5,\nfastapi, uvicorn==0.34.3, h5py==3.12.1, pyarrow==20.0.0,\nav==15.0.0, mediapy==1.2.4\n```\nLIBERO 评估另需 Python 3.8 环境。\n\n### VTC 集成方案\n**插入点**: Florence2 `_encode_image()` 输出 → **VTC** → `_merge_input_ids_with_image_features()`\n\n**改造清单**:\n1. 创建 `xvla_vtc_adapter.py`（复用 VisionTokenCompressor，hidden_dim 改 1024）\n2. 创建 XVLASmartCompressWrapper，hook Florence2 vision 输出\n3. 修改 merge 逻辑以适应压缩后的 token 数量\n4. 创建 `train_xvla_smart_compress.py`（参考 X-VLA 的 train.py + peft_train.py）\n5. 适配 flow matching loss（不同于 OpenVLA 的 cross-entropy）\n\n**与 OpenVLA VTC 的关键差异**:\n| 维度 | OpenVLA | X-VLA |\n|------|---------|-------|\n| hidden_dim | 4096 | 1024 |\n| 原始 vision tokens | 256 | ~49-576 (待验证) |\n| Action 范式 | Autoregressive (256-bin CE) | Flow matching (MSE+BCE) |\n| Connector | 2-layer MLP | Linear + LayerNorm |\n| 模型大小 | 7B | 0.9B |\n\n**预计工作量**: 8-12 小时\n- 代码改造: 4-6h（adapter + training script）\n- 环境搭建 + 模型下载: 2-3h\n- 验证 + 调试: 2-3h\n\n---\n\n## X-VLA Token Importance 分析结果（2026-05-20）\n\n### 实验配置\n- **模型**: X-VLA-0.9B (lerobot/xvla-libero checkpoint)\n- **数据**: LIBERO-Object (task_index 20-29), 100 images, 10 tasks\n- **服务器**: westd-41074, cuda:1\n- **分析脚本**: `/root/autodl-tmp/importance_margin_vla_compress/analyze_xvla_token_importance.py`\n- **结果文件**: `/root/autodl-tmp/importance_margin_vla_compress/eval_results/xvla_attention_entropy_perlayer.json`\n\n### SoftPromptedTransformer 序列布局\n| Token 类型 | 数量 | 说明 |\n|-----------|------|------|\n| Action tokens | 30 | Flow matching denoised action |\n| VLM features | 64 | Florence2 encoder output (main view) |\n| Aux visual | 150 | Additional camera views |\n| Soft prompts | 32 | Embodiment-specific learnable tokens |\n| **Total** | **276** | |\n\n### Entropy Ratio（Action→Vision 注意力熵）\n- **Overall**: **0.6138** ± 0.1159\n- **趋势**: 浅层低（L0=0.46, L1=0.34），深层高（L22=0.79, L23=0.71）\n- 浅层集中注意力于少数 vision tokens，深层趋于均匀\n\n### Vision Attention Fraction（Action tokens 分配给 vision tokens 的注意力比例）\n- 浅层（L0-2）: 33-49% — action tokens 还关注 soft prompts 和 self\n- 中层（L6-11）: 84-90% — 绝大部分注意力给 vision tokens\n- 深层（L17-23）: 79-90% — 持续高注意力\n\n### Pruning Curve（核心发现）\n| Retention k | Mean Loss | Normalized |\n|-------------|-----------|------------|\n| 0.30 | 0.112945 | **1.0014** |\n| 0.50 | 0.112823 | 1.0003 |\n| 0.70 | 0.112789 | 1.0000 |\n| 0.90 | 0.112789 | 1.0000 |\n| 0.95 | 0.112789 | 1.0000 |\n| 1.00 | 0.112789 | 1.0000 |\n\n**关键结论**: 丢弃 70% 的 vision tokens（k=0.3）仅导致 0.14% 的 loss 增加。X-VLA 的 vision tokens **几乎完全可压缩**。\n\n### 跨模型对比\n| 模型 | Connector | Entropy Ratio | k=0.3 Norm Loss | 压缩行为 |\n|------|-----------|---------------|-----------------|----------|\n| SmolVLA | Pixel-shuffle | ~0.45 (低) | Cliff-edge | 不可压缩 |\n| OpenVLA | 2-layer MLP | ~0.55 (中) | ~1.15 (15%↑) | 渐进退化 |\n| **X-VLA** | **Linear proj** | **0.61 (中高)** | **1.0014 (0.14%↑)** | **几乎无损** |\n\n### 解读\n1. **Linear projection connector 产生了高度冗余的 vision token 表示**——大部分信息集中在少数 token 中，L2 norm 可以轻松识别\n2. Entropy 比 OpenVLA 更高（0.61 vs 0.55），说明注意力分布更均匀，但这不矛盾——均匀分布意味着 \"每个 token 被平等关注\"，而 pruning 几乎无损意味着 \"被关注的内容高度冗余\"\n3. 这是 **connector 架构论文的关键数据点**：linear projection（无非线性变换）保留了 DaViT 输出的原始冗余结构，而 MLP projector（2 层 + GELU）通过非线性变换重新分配了信息，使得 token 间差异更大、更难压缩\n\n---\n\n## OFT Importance CV 分析结果（2026-05-20）\n\n### 结论\n- **OFT CV = 0.2185**，per-task CV 在 0.211–0.225 之间\n- 与 OpenVLA (0.215) 高度一致——两者共享相同的 2-layer MLP projector（Prismatic 架构）\n- **LoRA fine-tuning 不改变 vision token importance 分布**——connector 架构是唯一决定因素\n\n### Diagnostic 表格完成状态（5/5）\n| 模型 | Connector | CV | 压缩行为 |\n|------|-----------|-----|----------|\n| SmolVLA | Pixel-shuffle | ~0.08 | Cliff-edge collapse |\n| OpenVLA | 2-layer MLP | 0.215 | Graded degradation |\n| OpenVLA-OFT | 2-layer MLP (same) | 0.2185 | 预期与 OpenVLA 相同 |\n| X-VLA | Linear projection | TBD | Nearly lossless |\n| RoboFlamingo | Perceiver Resampler | N/A | 训练失败 |\n\n### 论文意义\nOFT 结果支撑 claim: \"token importance distribution is an intrinsic property of the connector architecture, invariant to downstream fine-tuning strategy (LoRA vs full)\"\n\n---\n\n## 失败模式记录\n\n- [2026-05-21] **π0.5 自定义 eval 脚本 bug**: `eval_pi05_pruning_libero.py` 的 `patched_embed_image` 函数导致 0% SR，而官方 eval 脚本在同一 checkpoint 上 ~100% SR。→ 新模型接入时，必须先用官方 eval 脚本验证 checkpoint 可用性，确认后再写自定义 pruning eval 脚本。不要假设自定义 patch 正确。\n\n- [2026-05-21] **OpenVLA eval 4 实验批量失败 (westd-38929)**:\n  - **失败实验**: eval_openvla_l2norm_k05_object_seed42 (PID 568225), eval_openvla_random_k03_object_seed42 (PID 568905), eval_openvla_l2norm_k07_object_seed42 (PID 569611), eval_openvla_l2norm_k03_object_seed42 (PID 570309)\n  - **根因**: **AutoDL 容器 GPU 缩配**。主机有 9 块 NVIDIA RTX PRO 6000 Blackwell (各 97GB)，但容器当前只挂载了 `/dev/nvidia2` 一块 GPU。4 个实验分别在 CUDA_VISIBLE_DEVICES=0/1/2/3 启动，运行 ~1h43m 后 GPU 设备被平台回收，进程收到 SIGKILL 无任何 traceback。\n  - **证据**:\n    - `nvidia-smi -L` 只显示 1 块 GPU (Device Minor 2)，而 `/proc/driver/nvidia/gpus/` 显示主机有 9 块\n    - 4 个日志文件在 14:45-14:49 间依次停止写入（3 分钟跨度，非瞬时），末尾均为正常进度输出无 error\n    - 各实验完成了 Task 1-3，在 Task 4/10 中被杀（~30% 完成度）\n    - 系统 RAM 充足（1TB 中仅用 46GB），排除 CPU OOM\n    - 无 tmux session，进程通过 nohup 方式运行\n  - **修复建议**:\n    1. 在 AutoDL 控制台恢复实例到 4 GPU 配置（或至少确认 GPU 分配稳定）\n    2. 重新启动 4 个实验，建议使用 tmux 以防 SSH 断连\n    3. 如果无法恢复多 GPU，可在单 GPU 上顺序运行（每个实验约 5.5h，共 ~22h）\n    4. 启动命令参考（单 GPU 顺序）:\n       ```bash\n       tmux new -s openvla_eval\n       source /root/miniconda3/etc/profile.d/conda.sh && conda activate base\n       cd /root/autodl-tmp/importance_margin_vla_compress\n       CUDA_VISIBLE_DEVICES=0 python -u eval_openvla_l2norm_libero.py --mode l2norm_prune --k_ratio 0.5 --suite libero_object --seed 42 > logs/eval_openvla_l2norm_k05_seed42.log 2>&1\n       CUDA_VISIBLE_DEVICES=0 python -u eval_openvla_l2norm_libero.py --mode random_prune --k_ratio 0.3 --suite libero_object --seed 42 > logs/eval_openvla_random_k03_seed42.log 2>&1\n       CUDA_VISIBLE_DEVICES=0 python -u eval_openvla_l2norm_libero.py --mode l2norm_prune --k_ratio 0.7 --suite libero_object --seed 42 > logs/eval_openvla_l2norm_k07_seed42.log 2>&1\n       CUDA_VISIBLE_DEVICES=0 python -u eval_openvla_l2norm_libero.py --mode l2norm_prune --k_ratio 0.3 --suite libero_object --seed 42 > logs/eval_openvla_l2norm_k03_seed42.log 2>&1\n       ```\n\n---\n\n## π0.5 跨 suite 对比（2026-05-21, 更新于 2026-05-22）\n\n**模型**: π0.5 (PaliGemma, linear projection connector, CV=0.055)\n**数据来源**: registry 中所有 status=DONE 且有有效 metrics 的 pi05 实验\n\n### Object Suite（baseline=98.2%, eval_pi05_baseline_object_seed42）\n\n| k | L2norm SR (%) | L2norm exp_ids | Random SR (%) | Random exp_ids |\n|---|--------------|----------------|--------------|----------------|\n| 0.9 | **98.2** (s42) | eval_pi05_l2norm_k09_object_seed42_v2 | **10.8** avg [12.0(s42), 9.6(s43)] | eval_pi05_random_k09_object_seed42_v2, eval_pi05_random_k09_object_seed43 |\n| 0.7 | **56.4** avg [55.0(s42), 56.4(s43), 57.8(s43v2)] | eval_pi05_l2norm_k07_object_seed42, _seed43, _seed43_v2 | **75.5** avg [77.2(s42), 73.8(s43)] | eval_pi05_random_k07_object_seed42, _seed43 |\n| 0.5 | **33.5** avg [33.4(s42), 33.6(s43)] | eval_pi05_l2norm_k05_object_seed42, _seed43 | **68.9** avg [69.4(s42), 68.4(s43)] | eval_pi05_random_k05_object_seed42, _seed43 |\n| 0.3 | **53.2** avg [51.0(s42), 55.4(s43)] | eval_pi05_l2norm_k03_object_seed42, _seed43 | **36.4** (s42) | eval_pi05_random_k03_object_seed42 |\n| 0.1 | **2.6** (s42) | eval_pi05_l2norm_k01_object_seed42 | — | — |\n\n### Spatial Suite（baseline=97.2%, eval_pi05_baseline_spatial_seed42）\n\n| k | L2norm SR (%) | Random SR (%) | Random exp_ids |\n|---|--------------|--------------|----------------|\n| 0.9 | — (pending) | — (pending) | — |\n| 0.7 | — (running: eval_pi05_l2norm_k07_spatial_seed42) | **74.4%** (s42) | eval_pi05_random_k07_spatial_seed42 |\n| 0.5 | — (running) | **71.6** (s42) | eval_pi05_random_k05_spatial_seed42 |\n| 0.3 | — (running) | — (submitted) | — |\n\n### Cross-suite 一致性分析\n\n**Random k=0.7 对比**:\n- Object: **75.5%** (seed42=77.2%, seed43=73.8%)\n- Spatial: **74.4%** (seed42)\n- **Delta: 1.1pp** — 极高一致性\n\n**Random k=0.5 对比**:\n- Object: **68.9%** (seed42=69.4%, seed43=68.4%)\n- Spatial: **71.6%** (seed42)\n- **Delta: 2.7pp** — 高度一致\n\n结论：Random pruning 在 k=0.7 和 k=0.5 的表现跨 suite 具有极强一致性（差异仅 1.1-2.7pp），说明 π0.5 的 vision token 冗余结构不依赖于具体 task 类型。Spatial 在 k=0.5 略高于 Object（+2.7pp），在 k=0.7 几乎相同（-1.1pp）。\n\n**Hypothesis 验证状态**: random > L2norm at k=0.7 的跨 suite 一致性需等 eval_pi05_l2norm_k07_spatial_seed42 完成后确认。Object 上 random(75.5%) > L2norm(56.4%) 差距 +19.1pp。如果 Spatial L2norm 也显著低于 random(74.4%)，则 hypothesis 成立。\n\n### 关键现象\n\n1. **L2norm 非单调 V-shape**：k=0.5 是谷底(33.5%)，k=0.3 反弹到 53.2%。多 seed 确认。原因待查——可能 L2 norm 在 50% 保留时恰好选中了信息量最差的 token 子集。\n\n2. **Random k=0.9 异常崩塌**：仅保留 90% token 时 random pruning SR 降至 ~10.8%（双 seed 确认 12.0%/9.6%），而 L2norm k=0.9 正常(98.2%)。这是所有模型中未见过的现象——移除 10% random token 即可摧毁模型。推测 π0.5 少数 token 承载关键位置信息，random 删除有 ~90% 概率命中关键 token。\n\n3. **Random 优于 L2norm 的 k 区间**：k=0.5(random 68.9% vs L2norm 33.5%)和 k=0.7(random 75.5% vs L2norm 56.4%)时 random 大幅优于 L2norm。说明 L2 norm 不是 π0.5 vision token importance 的好 proxy——CV=0.055 意味着 L2 norm 几乎无区分度。\n\n4. **Failed/killed 实验（已排除）**: eval_pi05_random_k07_object_seed42_v2(killed), _v3(killed), eval_pi05_random_k085_object_seed42(failed), eval_pi05_random_k095_object_seed42(failed), eval_pi05_random_k09_fixedmask_object_seed42(network error)。\n"
}
````

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "bcd9e5e6-c86c-4bf9-9402-037b79b77b15",
  "uuid": "6d7bf28a-2bda-47d4-82c0-e54c56a0948e",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AXT2yVmBBJNWMc58qGmPLd",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 14842,
      "cache_read_input_tokens": 42563,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 14842
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

_source line 37 · 2026-05-21T22:34:39.858Z_

<details><summary>↩ Tool result · `toolu_019Krqji5dXfWfCocDTGKsWF`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/memory.md\", \"saved\": true}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "bcd9e5e6-c86c-4bf9-9402-037b79b77b15",
  "uuid": "a5b5a53a-d981-4a65-94eb-29d2b51508a7",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"path\\\": \\\"/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/memory.md\\\", \\\"saved\\\": true}, \\\"error\\\": null, \\\"metadata\\\": {}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/memory.md\", \"saved\": true}, \"error\": null, \"metadata\": {}}"
    }
  }
}
```

</details>

---

### Assistant

_source line 38_

完成。总结：

**eval_pi05_random_k07_spatial_seed42** — SR = **74.4%** (372/500), DONE/success

**Per-task**: T0=90%, T1=96%, T2=94%, T3=52%, T4=60%, T5=42%, T6=58%, T7=76%, T8=80%, T9=96%

**Cross-suite 一致性**: Random k=0.7 在 Object(75.5%) 和 Spatial(74.4%) 上仅差 1.1pp，极高一致性。

**Hypothesis 状态**: 部分验证。Random k=0.7 Spatial 数据已到位(74.4%)。完整验证（random > L2norm 是否跨 suite 成立）需等 `eval_pi05_l2norm_k07_spatial_seed42` 完成。Object 上差距为 +19.1pp (random 75.5% vs L2norm 56.4%)。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "bcd9e5e6-c86c-4bf9-9402-037b79b77b15",
  "uuid": "40b16cbe-ed79-4c3b-9b30-29a85e76be66",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015RDeM78QCvC5Fd2uoRx5MX",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 14401,
      "cache_read_input_tokens": 57405,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 14401
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

_source line 39_

完成。总结：

**eval_pi05_random_k07_spatial_seed42** — SR = **74.4%** (372/500), DONE/success

**Per-task**: T0=90%, T1=96%, T2=94%, T3=52%, T4=60%, T5=42%, T6=58%, T7=76%, T8=80%, T9=96%

**Cross-suite 一致性**: Random k=0.7 在 Object(75.5%) 和 Spatial(74.4%) 上仅差 1.1pp，极高一致性。

**Hypothesis 状态**: 部分验证。Random k=0.7 Spatial 数据已到位(74.4%)。完整验证（random > L2norm 是否跨 suite 成立）需等 `eval_pi05_l2norm_k07_spatial_seed42` 完成。Object 上差距为 +19.1pp (random 75.5% vs L2norm 56.4%)。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "type": "result",
  "subtype": "success",
  "is_error": false,
  "api_error_status": null,
  "duration_ms": 392212,
  "duration_api_ms": 382877,
  "num_turns": 14,
  "stop_reason": "end_turn",
  "session_id": "bcd9e5e6-c86c-4bf9-9402-037b79b77b15",
  "total_cost_usd": 1.05464625,
  "usage": {
    "input_tokens": 16,
    "cache_creation_input_tokens": 59965,
    "cache_read_input_tokens": 434490,
    "output_tokens": 18435,
    "server_tool_use": {
      "web_search_requests": 0,
      "web_fetch_requests": 0
    },
    "service_tier": "standard",
    "cache_creation": {
      "ephemeral_1h_input_tokens": 59965,
      "ephemeral_5m_input_tokens": 0
    },
    "inference_geo": "",
    "iterations": [
      {
        "input_tokens": 1,
        "output_tokens": 262,
        "cache_read_input_tokens": 57405,
        "cache_creation_input_tokens": 14401,
        "cache_creation": {
          "ephemeral_5m_input_tokens": 0,
          "ephemeral_1h_input_tokens": 14401
        },
        "type": "message"
      }
    ],
    "speed": "standard"
  },
  "modelUsage": {
    "claude-haiku-4-5-20251001": {
      "inputTokens": 1550,
      "outputTokens": 23,
      "cacheReadInputTokens": 0,
      "cacheCreationInputTokens": 0,
      "webSearchRequests": 0,
      "costUSD": 0.001665,
      "contextWindow": 200000,
      "maxOutputTokens": 32000
    },
    "claude-opus-4-6": {
      "inputTokens": 16,
      "outputTokens": 18435,
      "cacheReadInputTokens": 434490,
      "cacheCreationInputTokens": 59965,
      "webSearchRequests": 0,
      "costUSD": 1.05298125,
      "contextWindow": 200000,
      "maxOutputTokens": 64000
    }
  },
  "permission_denials": [],
  "terminal_reason": "completed",
  "fast_mode_state": "off",
  "uuid": "455443c2-7473-4958-8ccc-7cd190340ca7"
}
```

</details>

---
