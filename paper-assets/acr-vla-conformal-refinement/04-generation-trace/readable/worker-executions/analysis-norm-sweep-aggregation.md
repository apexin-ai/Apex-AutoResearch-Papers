# analysis norm sweep aggregation

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Worker execution logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 64
- **Recorded user turns:** 1
- **Tool calls:** 17
- **Original source:** `logs/workers/worker_analysis_norm-sweep-aggregation_20260521T032154.log`
- **Structured JSON:** [`cc924ca45d55d3f4da0d.json`](../../sessions/cc/cc924ca45d55d3f4da0d.json)

## Before a recorded user message

31 recorded events

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
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement",
  "session_id": "e17f41b1-3dce-49fb-a9e5-f5dd86423ed8",
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
  "uuid": "019d9594-4a25-4e2c-a078-8e036708213d",
  "memory_paths": {
    "auto": "/home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-8-projects-acr-vla-conformal-refinement/memory/"
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
    "status": "allowed_warning",
    "resetsAt": 1779469200,
    "rateLimitType": "seven_day",
    "utilization": 0.97,
    "isUsingOverage": false,
    "surpassedThreshold": 0.75
  },
  "uuid": "48c2719f-2445-4020-807e-91677c9e8fca",
  "session_id": "e17f41b1-3dce-49fb-a9e5-f5dd86423ed8"
}
```

---

### Assistant

_source line 4_

<details><summary>Logged reasoning block</summary>

```text
Let me start by reading the registry to get all DONE experiments, then filter for the norm sweep experiments.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "e17f41b1-3dce-49fb-a9e5-f5dd86423ed8",
  "uuid": "48df71d9-fb67-4789-acc4-98bf30cb7234",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WDLMVGj7T8ewjBWsZvpSXw",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 11539,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 11539
      },
      "output_tokens": 26,
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

<details open><summary>🔧 Tool call — ToolSearch · `toolu_015oikFK7aqT5HpikoZhYnFz`</summary>

```json
{
  "query": "select:mcp__agent-ml-research__read_registry,mcp__agent-ml-research__save_project_file,mcp__agent-ml-research__read_project_file",
  "max_results": 3
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "e17f41b1-3dce-49fb-a9e5-f5dd86423ed8",
  "uuid": "417d7a0b-c168-44e3-a223-0081e9fc33a3",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WDLMVGj7T8ewjBWsZvpSXw",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 11539,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 11539
      },
      "output_tokens": 26,
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

_source line 6 · 2026-05-21T03:22:07.639Z_

<details><summary>↩ Tool result · `toolu_015oikFK7aqT5HpikoZhYnFz`</summary>

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
  "tool_name": "mcp__agent-ml-research__save_project_file"
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
  "session_id": "e17f41b1-3dce-49fb-a9e5-f5dd86423ed8",
  "uuid": "15257eb3-f911-463b-abe8-12c00403f35e",
  "tool_use_result": {
    "matches": [
      "mcp__agent-ml-research__read_registry",
      "mcp__agent-ml-research__save_project_file",
      "mcp__agent-ml-research__read_project_file"
    ],
    "query": "select:mcp__agent-ml-research__read_registry,mcp__agent-ml-research__save_project_file,mcp__agent-ml-research__read_project_file",
    "total_deferred_tools": 25
  }
}
```

</details>

---

### Tool call

_source line 7_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry · `toolu_0111YnZ4gJ4KUkkB4tcZViTz`</summary>

```json
{
  "filters": {
    "status": "DONE"
  },
  "limit": 0,
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
  "session_id": "e17f41b1-3dce-49fb-a9e5-f5dd86423ed8",
  "uuid": "ea46d4a8-e308-4dc4-be21-92146ddfe963",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UYT61WRkH9xGUXFnM24J9y",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1083,
      "cache_read_input_tokens": 23380,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1083
      },
      "output_tokens": 53,
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

_source line 8 · 2026-05-21T03:22:11.116Z_

<details><summary>↩ Tool result · `toolu_0111YnZ4gJ4KUkkB4tcZViTz`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"experiments\": {\"eval-perdof-object-norm02-seed49\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-20T15:59:12.635Z\", \"updated_at\": \"2026-05-20T15:59:54.757Z\", \"metrics\": {\"overall_success_rate\": 0.12, \"total_rollouts\": 100, \"total_successes\": 12, \"per_task_sr\": {\"alphabet_soup\": 0, \"cream_cheese\": 0, \"salad_dressing\": 0.1, \"bbq_sauce\": 0.2, \"ketchup\": 0, \"tomato_sauce\": 0, \"butter\": 0.1, \"milk\": 0.2, \"chocolate_pudding\": 0.4, \"orange_juice\": 0.2}}, \"log_path\": \"/root/acr-vla-conformal-refinement/logs/eval-perdof-object-norm02-seed49.log\", \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt\", \"spec\": {\"command\": \"python evaluate.py --mode crm_perdof --benchmark object --seed 49 --K 10 --max_correction_norm 0.2 --n_rollouts 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt --output_file logs/eval_perdof_object_norm02_seed49.json\", \"server\": \"bjb1-32546\", \"data_path\": \"LIBERO-Object\", \"data_count\": 100, \"model_name\": \"crm_perdof_norm02_K10\", \"seed\": 49, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt\", \"eval_data\": \"LIBERO-Object\"}, \"hypothesis\": \"PerDoF CRM with norm-clipped corrections (epsilon=0.2, K=10) provides consistent improvement over baseline on LIBERO-Object across seeds; seed49 should yield SR in the 14-18% range consistent with seeds 43-48.\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-20T15:59:54.757Z\"}, \"eval-obs-only-goal-norm02-seed52\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-20T12:05:20.840Z\", \"updated_at\": \"2026-05-20T12:58:35.610Z\", \"spec\": {\"command\": \"python -u src/evaluate.py --mode crm_obs_only --benchmark LIBERO-Goal --seed 52 --n_rollouts 10 --max_correction_norm 0.2\", \"server\": \"bjb1-32546\", \"gpu\": \"cuda:0\", \"pid\": 362579, \"data_path\": \"LIBERO-Goal\", \"data_count\": \"10 tasks x 10 rollouts\", \"model_name\": \"openvla-7b + CRM obs_only\", \"seed\": 52, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\", \"eval_data\": \"LIBERO-Goal (10 tasks x 10 rollouts)\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-obs-only-goal-norm02-seed52.log\", \"checkpoint_path\": \"N/A (eval only)\"}, \"metrics\": {\"success_rate\": 0.68, \"successes\": 68, \"total\": 100, \"per_task_sr\": {\"open_middle_drawer_cabinet\": 0.7, \"put_bowl_on_stove\": 0.9, \"put_wine_bottle_on_cabinet\": 0.4, \"open_top_drawer_put_bowl\": 0.3, \"put_bowl_on_cabinet\": 0.8, \"push_plate_front_stove\": 0.8, \"put_cream_cheese_in_bowl\": 0.4, \"turn_on_stove\": 1, \"put_bowl_on_plate\": 1, \"put_wine_bottle_on_rack\": 0.5}}, \"conclusion\": \"success\", \"hypothesis\": \"CRM obs_only with K=10 and norm cap 0.2 improves SR on LIBERO-Goal by applying observation-conditioned corrections that compensate for VLA action prediction errors, providing a new seed for variance estimation.\", \"completed_at\": \"2026-05-20T12:58:26.417Z\", \"notes\": \"SR=68% on Goal seed52. Strong result; turn_on_stove and put_bowl_on_plate both 100%.\"}, \"eval-argmin-object-seed49\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-20T12:05:22.690Z\", \"updated_at\": \"2026-05-20T12:58:34.569Z\", \"spec\": {\"command\": \"python -u src/evaluate.py --mode reconvla --benchmark LIBERO-Object --seed 49 --n_rollouts 10\", \"server\": \"bjb1-32546\", \"gpu\": \"cuda:5\", \"pid\": 364591, \"data_path\": \"LIBERO-Object\", \"data_count\": \"10 tasks x 10 rollouts\", \"model_name\": \"openvla-7b + CRM obs_only (argmin)\", \"seed\": 49, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\", \"eval_data\": \"LIBERO-Object (10 tasks x 10 rollouts)\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-argmin-object-seed49.log\", \"checkpoint_path\": \"N/A (eval only)\"}, \"metrics\": {\"success_rate\": 0.16, \"successes\": 16, \"total\": 100, \"per_task_sr\": {\"alphabet_soup\": 0, \"cream_cheese\": 0, \"salad_dressing\": 0.2, \"bbq_sauce\": 0.4, \"ketchup\": 0, \"tomato_sauce\": 0.1, \"butter\": 0.1, \"milk\": 0.3, \"chocolate_pudding\": 0.3, \"orange_juice\": 0.2}}, \"conclusion\": \"success\", \"hypothesis\": \"Argmin (reconvla) selection among K=10 CRM refinements improves over single-step VLA on Object by choosing the candidate with lowest predicted residual, providing a multi-seed consistency check.\", \"completed_at\": \"2026-05-20T12:58:25.905Z\", \"notes\": \"SR=16% on Object seed49. Consistent with other argmin seeds on Object benchmark.\"}, \"eval-random-selection-spatial-seed43\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-20T12:05:19.438Z\", \"updated_at\": \"2026-05-20T12:58:33.167Z\", \"spec\": {\"command\": \"python -u src/evaluate.py --mode random_selection --benchmark LIBERO-Spatial --seed 43 --n_rollouts 10\", \"server\": \"bjb1-18228\", \"gpu\": \"cuda:1\", \"pid\": 347075, \"data_path\": \"LIBERO-Spatial\", \"data_count\": \"10 tasks x 10 rollouts\", \"model_name\": \"openvla-7b + CRM obs_only\", \"seed\": 43, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\", \"eval_data\": \"LIBERO-Spatial (10 tasks x 10 rollouts)\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-random-selection-spatial-seed43.log\", \"checkpoint_path\": \"N/A (eval only)\"}, \"metrics\": {\"success_rate\": 0.26, \"successes\": 26, \"total\": 100, \"per_task_sr\": {\"between_plate_ramekin\": 0.7, \"next_to_ramekin\": 0.9, \"table_center\": 0, \"cookie_box\": 0.1, \"top_drawer\": 0, \"on_ramekin\": 0, \"next_to_cookie_box\": 0.7, \"on_stove\": 0, \"next_to_plate\": 0.2, \"on_wooden_cabinet\": 0}}, \"conclusion\": \"success\", \"hypothesis\": \"Random candidate selection from K=10 CRM refinements serves as a lower-bound baseline, showing that informed selection (argmin) is necessary to achieve the full benefit of multi-step refinement on Spatial.\", \"completed_at\": \"2026-05-20T12:58:24.969Z\", \"notes\": \"SR=26% on Spatial seed43. Lower than argmin-based selection, confirming informed selection matters.\"}, \"eval-adaptive-k-spatial-p90-seed43\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-20T10:52:06.660Z\", \"updated_at\": \"2026-05-20T12:58:31.849Z\", \"spec\": {\"command\": \"python -u src/evaluate.py --mode adaptive_k --benchmark LIBERO-Spatial --seed 43 --n_rollouts 10 --adaptive_k_threshold 0.125870 --output_file logs/eval-adaptive-k-spatial-p90-seed43.json\", \"server\": \"bjb1-18228\", \"gpu\": \"cuda:3\", \"pid\": 344852, \"data_path\": \"LIBERO-Spatial\", \"data_count\": \"10 tasks x 10 rollouts\", \"model_name\": \"openvla-7b + CRM obs_only\", \"seed\": 43, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\", \"eval_data\": \"LIBERO-Spatial (10 tasks x 10 rollouts)\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-adaptive-k-spatial-p90-seed43.log\", \"checkpoint_path\": \"N/A (eval only)\"}, \"metrics\": {\"success_rate\": 0.32, \"successes\": 32, \"total\": 100, \"avg_K\": 3.6, \"fast_path_pct\": 80.2, \"mean_l2\": 0.0905, \"per_task_sr\": {\"between_plate_ramekin\": 0.7, \"next_to_ramekin\": 1, \"table_center\": 0.1, \"cookie_box\": 0.3, \"top_drawer\": 0, \"on_ramekin\": 0.1, \"next_to_cookie_box\": 0.8, \"on_stove\": 0, \"next_to_plate\": 0.2, \"on_wooden_cabinet\": 0}}, \"conclusion\": \"success\", \"hypothesis\": \"Adaptive K with P90 threshold (τ=0.1259) reduces average refinement steps while maintaining comparable SR to fixed K=10 on Spatial, because most states have low CRM residuals and can skip full refinement.\", \"completed_at\": \"2026-05-20T12:58:23.572Z\", \"notes\": \"SR=32%, avg_K=3.6 (vs fixed K=10), 80.2% fast-path. Adaptive K saves ~64% compute with seed43 on Spatial.\"}, \"eval-adaptive-k-object-p90-seed44\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-20T12:45:08.564Z\", \"updated_at\": \"2026-05-20T12:45:37.089Z\", \"hypothesis\": \"Adaptive K with τ=P90 (0.125870) on LIBERO-Object seed44. P90 是最宽松的阈值——大部分 step fast-path (K=1)，仅在极高不确定性时用 K=10。验证 P90 在 Object 上的 SR/compute tradeoff。\", \"spec\": {\"command\": \"python -u src/evaluate.py --mode adaptive_k --benchmark LIBERO-Object --seed 44 --n_rollouts 10 --adaptive_k_threshold 0.125870\", \"server\": \"bjb2-28827\", \"data_path\": \"LIBERO-Object\", \"data_count\": \"10 tasks x 10 rollouts\", \"model_name\": \"openvla-7b + CRM obs_only\", \"seed\": 44, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\", \"eval_data\": \"LIBERO-Object (10 tasks x 10 rollouts)\", \"log_path\": \"N/A (discovered by Reviewer)\", \"checkpoint_path\": \"N/A (eval only)\"}, \"metrics\": {\"sr\": 14, \"avg_K\": 2.58, \"fast_path_pct\": 92.8, \"total_rollouts\": 100}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-20T12:45:37.089Z\"}, \"eval-adaptive-k-object-p90-seed43\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-20T12:45:08.312Z\", \"updated_at\": \"2026-05-20T12:45:34.700Z\", \"hypothesis\": \"Adaptive K with τ=P90 (0.125870) on LIBERO-Object seed43. P90 是最宽松的阈值——大部分 step fast-path (K=1)，仅在极高不确定性时用 K=10。验证 P90 在 Object 上的 SR/compute tradeoff。\", \"spec\": {\"command\": \"python -u src/evaluate.py --mode adaptive_k --benchmark LIBERO-Object --seed 43 --n_rollouts 10 --adaptive_k_threshold 0.125870\", \"server\": \"bjb2-28827\", \"data_path\": \"LIBERO-Object\", \"data_count\": \"10 tasks x 10 rollouts\", \"model_name\": \"openvla-7b + CRM obs_only\", \"seed\": 43, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\", \"eval_data\": \"LIBERO-Object (10 tasks x 10 rollouts)\", \"log_path\": \"N/A (discovered by Reviewer)\", \"checkpoint_path\": \"N/A (eval only)\"}, \"metrics\": {\"sr\": 14, \"avg_K\": 2.61, \"fast_path_pct\": 92.3, \"total_rollouts\": 100}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-20T12:45:34.700Z\"}, \"eval-adaptive-k-spatial-p50-seed42\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-20T11:24:12.894Z\", \"updated_at\": \"2026-05-20T11:25:16.991Z\", \"conclusion\": \"success\", \"metrics\": {\"sr\": 30, \"avg_K\": 6.324, \"fast_path_pct\": 45.95, \"mean_l2\": 0.0903, \"total_rollouts\": 100}, \"failure_reason\": \"\", \"completed_at\": \"2026-05-20T11:06:00.000Z\", \"notes\": \"Reviewer 独立验证：JSON 完整，日志确认 SR=30%，PID 自然退出。之前被 cron 误判为 failed（PID dead + 无 sentinel），已修正为 success。\", \"spec\": {\"command\": \"python -u src/evaluate.py --mode adaptive_k --benchmark LIBERO-Spatial --seed 42 --n_rollouts 10 --adaptive_k_threshold 0.074855\", \"server\": \"bjb2-40593\", \"gpu\": \"cuda:0\", \"pid\": 681823, \"data_path\": \"LIBERO-Spatial\", \"data_count\": \"10 tasks x 10 rollouts\", \"model_name\": \"openvla-7b + CRM obs_only\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\", \"eval_data\": \"LIBERO-Spatial (10 tasks x 10 rollouts)\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-adaptive-k-spatial-p50-seed42.log\", \"checkpoint_path\": \"N/A (eval only)\"}, \"hypothesis\": \"Adaptive K with τ=P50 (0.074855, Object-calibrated) on LIBERO-Spatial seed42. 验证 Adaptive K 方法在第二个 benchmark 上的泛化：使用 Object 上校准的阈值直接应用到 Spatial（无 per-benchmark tuning）。如果 SR 接近 CRM K=10 (34.3%) 且 fast_path >50%，则证明方法跨 benchmark 通用。\"}, \"eval-obs-only-object-norm003-seed44\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-20T10:52:14.742Z\", \"updated_at\": \"2026-05-20T10:52:47.202Z\", \"hypothesis\": \"CRM obs_only ε=0.03 on Object seed44. Low-norm multi-seed supplement (plan_500): strengthens Figure 2 error bars at small ε.\", \"spec\": {\"command\": \"evaluate.py --mode crm_obs_only --benchmark object --seed 44 --n_rollouts 10 --K 10 --max_correction_norm 0.03\", \"server\": \"bjb2-28827\", \"seed\": 44, \"model_name\": \"crm_v3_norm/obs_only/crm_best.pt\", \"data_path\": \"LIBERO_object\", \"data_count\": 100}, \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-obs-only-object-norm003-seed44.log\", \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\", \"metrics\": {\"overall_success_rate\": 0.15, \"total_successes\": 15, \"total_rollouts\": 100, \"per_task\": {\"alphabet_soup\": 0, \"cream_cheese\": 0, \"salad_dressing\": 0.3, \"bbq_sauce\": 0.2, \"ketchup\": 0, \"tomato_sauce\": 0.1, \"butter\": 0.1, \"milk\": 0.2, \"chocolate_pudding\": 0.3, \"orange_juice\": 0.3}}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-20T10:52:47.202Z\"}, \"eval-random-selection-object-seed46-r2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-19T17:41:16.541Z\", \"updated_at\": \"2026-05-19T17:41:32.255Z\", \"spec\": {\"command\": \"cd /root/acr-vla-conformal-refinement && timeout 57600 /root/miniconda3/bin/python -u src/evaluate.py --mode random_selection --benchmark object --n_rollouts 10 --seed 46 --K 10 --output_file logs/eval_object_random_selection_seed46.json\", \"server\": \"bjb2-40593\", \"data_path\": \"LIBERO-Object\", \"data_count\": 100, \"model_name\": \"SmolVLA_random_selection\", \"seed\": 46, \"checkpoint_path\": \"N/A-eval-only\", \"log_path\": \"/root/acr-vla-conformal-refinement/logs/eval_object_random_selection_seed46.log\"}, \"hypothesis\": \"Random selection baseline (K=10) on LIBERO-Object seed46 establishes reference success rate for comparing against CRM-guided selection methods\", \"conclusion\": \"killed\", \"completed_at\": \"2026-05-19T17:41:32.255Z\"}, \"eval-obs-only-spatial-norm02-seed47\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-19T17:02:40.986Z\", \"updated_at\": \"2026-05-19T17:03:14.457Z\", \"metrics\": {\"success_rate\": 0.32, \"successes\": 32, \"total\": 100, \"n_tasks\": 10, \"n_rollouts\": 10, \"per_task\": {\"between_plate_and_ramekin\": 0.8, \"next_to_ramekin\": 0.9, \"from_table_center\": 0, \"on_cookie_box\": 0.3, \"in_top_drawer\": 0.1, \"on_ramekin\": 0, \"next_to_cookie_box\": 0.9, \"on_stove\": 0, \"next_to_plate\": 0.2, \"on_wooden_cabinet\": 0}}, \"checkpoint_path\": \"N/A-eval-only\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-obs-only-spatial-norm02-seed47.log\", \"conclusion\": \"success\", \"spec\": {\"command\": \"cd /root/acr-vla-conformal-refinement && /root/miniconda3/bin/python -u src/evaluate.py --mode crm_obs_only --benchmark spatial --n_rollouts 10 --seed 47 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --max_correction_norm 0.2 --output_file logs/eval_spatial_obs_only_norm02_seed47.json\", \"server\": \"bjb1-32546\", \"data_path\": \"LIBERO-Spatial\", \"data_count\": 100, \"model_name\": \"crm_obs_only\", \"seed\": 47}, \"hypothesis\": \"obs_only CRM with epsilon=0.2 and K=10 improves success rate over VLA-only baseline on LIBERO-Spatial because observation-conditioned conformal corrections can detect and fix spatial reasoning errors without requiring action history\", \"completed_at\": \"2026-05-19T17:03:14.457Z\"}, \"eval-vla-only-spatial-seed45\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-19T15:19:50.220Z\", \"updated_at\": \"2026-05-19T15:20:24.563Z\", \"spec\": {\"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-vla-only-spatial-seed45.log\", \"command\": \"python evaluate.py --benchmark spatial --mode vla_only --seed 45\", \"server\": \"bjb1-32546\", \"seed\": 45, \"data_path\": \"LIBERO-Spatial\", \"data_count\": 100, \"model_name\": \"SmolVLA\", \"checkpoint_path\": \"N/A (eval-only)\"}, \"metrics\": {\"success_rate\": 0.27, \"per_task\": {\"between_plate_and_ramekin\": 0.7, \"next_to_ramekin\": 0.9, \"from_table_center\": 0, \"on_cookie_box\": 0.2, \"in_top_drawer\": 0, \"on_ramekin\": 0, \"next_to_cookie_box\": 0.9, \"on_stove\": 0, \"next_to_plate\": 0, \"on_wooden_cabinet\": 0}, \"successes\": 27, \"total\": 100}, \"conclusion\": \"success\", \"hypothesis\": \"VLA-only baseline on LIBERO-Spatial with seed 45 establishes reference success rate for comparison with CRM-augmented methods\", \"completed_at\": \"2026-05-19T15:20:24.563Z\"}, \"eval-obs-only-spatial-norm02-seed44\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-19T14:23:33.161Z\", \"updated_at\": \"2026-05-19T14:26:44.810Z\", \"metrics\": {\"success_rate\": 0.36, \"successes\": 36, \"total\": 100}, \"checkpoint_path\": \"N/A (eval only)\", \"log_path\": \"/root/acr-vla-conformal-refinement/logs/eval_spatial_obs_only_norm02_seed44.json\", \"conclusion\": \"success\", \"spec\": {\"command\": \"python eval_crm.py --mode crm_obs_only --benchmark spatial --K 10 --seed 44 --max_correction_norm 0.2\", \"server\": \"bjb2-28827\", \"data_path\": \"spatial_benchmark\", \"data_count\": 100, \"model_name\": \"crm_obs_only\", \"seed\": 44}, \"hypothesis\": \"CRM obs-only mode with max_correction_norm=0.2 can improve spatial benchmark success rate by refining VLA actions using only observation-based conformal prediction, without access to privileged state information.\", \"completed_at\": \"2026-05-19T14:24:10.857Z\"}, \"eval-obs-only-object-norm003-seed43-r2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-19T05:14:10.523Z\", \"updated_at\": \"2026-05-19T05:14:25.385Z\", \"conclusion\": \"failed\", \"spec\": {\"checkpoint_path\": \"N/A (eval-only)\", \"log_path\": \"/root/acr-vla-conformal-refinement/logs/eval_object_obs_only_norm003_seed43.log\", \"metrics\": {\"success_rate\": null, \"tasks_completed\": \"1/10\", \"failure_reason\": \"process terminated prematurely after 1 task\"}}, \"completed_at\": \"2026-05-19T05:14:25.385Z\"}, \"eval-obs-only-object-norm03-seed48\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-18T13:26:49.122Z\", \"updated_at\": \"2026-05-18T13:27:19.389Z\", \"metrics\": {\"overall_success_rate\": 0.16, \"per_task\": {\"pick_up_the_alphabet_soup_and_place_it_in_the_basket\": 0, \"pick_up_the_cream_cheese_and_place_it_in_the_basket\": 0, \"pick_up_the_salad_dressing_and_place_it_in_the_basket\": 0.3, \"pick_up_the_bbq_sauce_and_place_it_in_the_basket\": 0.4, \"pick_up_the_ketchup_and_place_it_in_the_basket\": 0, \"pick_up_the_tomato_sauce_and_place_it_in_the_basket\": 0.1, \"pick_up_the_butter_and_place_it_in_the_basket\": 0.1, \"pick_up_the_milk_and_place_it_in_the_basket\": 0.1, \"pick_up_the_chocolate_pudding_and_place_it_in_the_basket\": 0.4, \"pick_up_the_orange_juice_and_place_it_in_the_basket\": 0.2}}, \"log_path\": \"/root/acr-vla-conformal-refinement/logs/eval_object_obs_only_norm03_seed48.json\", \"checkpoint_path\": \"N/A (eval only)\", \"conclusion\": \"success\", \"spec\": {\"command\": \"eval obs_only CRM epsilon=0.3 seed48 on LIBERO-Object K=10 n_rollouts=10\", \"server\": \"bjb1-18228\", \"data_path\": \"LIBERO-Object\", \"data_count\": 100, \"model_name\": \"openvla\", \"seed\": 48}, \"hypothesis\": \"CRM with obs_only mode and epsilon=0.3 normalization threshold will improve success rate on LIBERO-Object by filtering unreliable action predictions based solely on observation conformity scores\", \"completed_at\": \"2026-05-18T13:27:19.389Z\"}, \"eval-obs-only-object-norm01-seed48\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-18T11:42:37.233Z\", \"updated_at\": \"2026-05-18T11:43:15.403Z\", \"hypothesis\": \"obs_only CRM with max_correction_norm=0.1 on LIBERO-Object seed48. Tests whether obs_only mode with conservative norm clipping maintains performance across seeds.\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=1 /root/miniconda3/bin/python -u src/evaluate.py --mode crm_obs_only --benchmark object --n_rollouts 10 --seed 48 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --max_correction_norm 0.1 --output_file logs/eval_object_obs_only_norm01_seed48.json\", \"server\": \"bjb1-18228\", \"data_path\": \"LIBERO-Object\", \"data_count\": 100, \"model_name\": \"SmolVLA+CRM_obs_only\", \"seed\": 48, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\", \"eval_data\": \"LIBERO-Object\"}, \"log_path\": \"/root/acr-vla-conformal-refinement/logs/eval_object_obs_only_norm01_seed48.json\", \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.18, \"n_tasks\": 10, \"n_rollouts\": 10, \"per_task\": {\"alphabet_soup\": 0, \"cream_cheese\": 0, \"salad_dressing\": 0, \"bbq_sauce\": 0.4, \"ketchup\": 0.1, \"tomato_sauce\": 0.2, \"butter\": 0.2, \"milk\": 0.3, \"chocolate_pudding\": 0.3, \"orange_juice\": 0.3}}, \"completed_at\": \"2026-05-18T11:43:15.403Z\"}, \"eval-obs-only-object-norm02-k5-seed42\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-18T03:44:47.522Z\", \"updated_at\": \"2026-05-18T03:45:04.655Z\", \"conclusion\": \"success\", \"metrics\": {\"overall_sr\": 0.14, \"successes\": 14, \"rollouts\": 100, \"tasks\": 10, \"suite\": \"LIBERO-object\", \"seed\": 42, \"method\": \"crm_obs_only\", \"K\": 5, \"max_correction_norm\": 0.2}, \"hypothesis\": \"obs_only CRM with K=5 candidates and ε=0.2 on LIBERO-Object seed42. Tests whether fewer candidates (K=5 vs K=10) reduces selection quality. K=5 SR=14% vs K=10 SR=17.5% confirms monotonic improvement with more candidates.\", \"spec\": {\"command\": \"python -u src/evaluate.py --mode crm_obs_only --benchmark object --n_rollouts 10 --seed 42 --K 5 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --max_correction_norm 0.2 --output_file logs/eval_object_obs_only_norm02_k5_seed42.json\", \"server\": \"bjb1-18228\", \"data_path\": \"LIBERO-Object\", \"data_count\": 100, \"model_name\": \"SmolVLA+CRM_obs_only\", \"seed\": 42, \"K\": 5, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\", \"eval_data\": \"LIBERO-Object\", \"checkpoint_path\": \"N/A\", \"log_path\": \"/root/acr-vla-conformal-refinement/logs/eval_object_obs_only_norm02_k5_seed42.json\"}, \"completed_at\": \"2026-05-18T03:45:04.655Z\"}, \"eval-perdof-object-norm01-seed46\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-18T03:05:55.543Z\", \"updated_at\": \"2026-05-18T03:06:14.048Z\", \"hypothesis\": \"perdof CRM with ε=0.1 on LIBERO-Object seed46. Magnitude curve data point for perdof at intermediate norm. SR=10% confirms perdof degrades from peak at low norms.\", \"metrics\": {\"overall_sr\": 0.1, \"successes\": 10, \"rollouts\": 100, \"tasks\": 10, \"suite\": \"LIBERO-object\", \"seed\": 46, \"method\": \"crm_perdof\", \"max_correction_norm\": 0.1}, \"conclusion\": \"success\", \"spec\": {\"command\": \"python -u src/evaluate.py --mode crm_perdof --benchmark object --n_rollouts 10 --seed 46 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt --max_correction_norm 0.1 --output_file logs/eval_object_perdof_norm01_seed46.json\", \"server\": \"bjb1-32546\", \"data_path\": \"LIBERO-Object\", \"data_count\": 100, \"model_name\": \"SmolVLA+CRM_perdof\", \"seed\": 46, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt\", \"eval_data\": \"LIBERO-Object\", \"checkpoint_path\": \"N/A\", \"log_path\": \"/root/acr-vla-conformal-refinement/logs/eval_object_perdof_norm01_seed46.json\"}, \"completed_at\": \"2026-05-18T03:06:14.049Z\"}, \"eval-perdof-object-default-seed46\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-18T03:05:29.784Z\", \"updated_at\": \"2026-05-18T03:06:03.735Z\", \"conclusion\": \"negative\", \"hypothesis\": \"perdof CRM without norm constraint (uncapped correction magnitude) on LIBERO-Object seed46. Tests whether perdof maintains performance without explicit correction capping. SR=0% confirms perdof corrections are catastrophically unstable without norm constraints.\", \"spec\": {\"command\": \"python -u src/evaluate.py --mode crm_perdof --benchmark object --n_rollouts 10 --seed 46 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt --output_file logs/eval_object_perdof_default_seed46.json\", \"server\": \"bjb1-32546\", \"data_path\": \"LIBERO-Object\", \"data_count\": 100, \"model_name\": \"SmolVLA+CRM_perdof\", \"seed\": 46, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt\", \"eval_data\": \"LIBERO-Object\", \"checkpoint_path\": \"N/A\", \"log_path\": \"/root/acr-vla-conformal-refinement/logs/eval_object_perdof_default_seed46.json\"}, \"metrics\": {\"overall_sr\": 0, \"successes\": 0, \"rollouts\": 100, \"tasks\": 10, \"suite\": \"LIBERO-object\", \"seed\": 46, \"method\": \"crm_perdof\", \"max_correction_norm\": \"default\"}, \"completed_at\": \"2026-05-18T03:06:03.735Z\"}, \"eval-obs-only-object-default-seed46\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-18T00:59:50.348Z\", \"updated_at\": \"2026-05-18T01:00:23.165Z\", \"conclusion\": \"success\", \"metrics\": {\"overall_sr\": 0.15, \"successes\": 15, \"rollouts\": 100, \"tasks\": 10, \"suite\": \"LIBERO-object\", \"seed\": 46, \"method\": \"crm_obs_only\", \"max_correction_norm\": \"default\", \"per_task_sr\": {\"alphabet_soup\": 0, \"cream_cheese\": 0, \"salad_dressing\": 0.2, \"bbq_sauce\": 0.4, \"ketchup\": 0.1, \"tomato_sauce\": 0.1, \"butter\": 0.1, \"milk\": 0.1, \"chocolate_pudding\": 0.2, \"orange_juice\": 0.3}}, \"spec\": {\"checkpoint_path\": \"N/A\", \"log_path\": \"/root/acr-vla-conformal-refinement/logs/eval_object_obs_only_default_seed46.json\", \"command\": \"python -u src/evaluate.py --mode crm_obs_only --benchmark object --n_rollouts 10 --seed 46 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --output_file logs/eval_object_obs_only_default_seed46.json\", \"server\": \"bjb1-32546\", \"data_path\": \"LIBERO-Object\", \"data_count\": 100, \"model_name\": \"SmolVLA+CRM_obs_only\", \"seed\": 46, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\", \"eval_data\": \"LIBERO-Object\"}, \"hypothesis\": \"obs_only CRM without norm constraint (uncapped correction magnitude) on LIBERO-Object seed46. Tests whether obs_only maintains performance without explicit correction capping. If uncapped performs worse than capped, it confirms that moderate norm constraints stabilize corrections.\", \"completed_at\": \"2026-05-18T01:00:23.165Z\"}, \"eval-obs-only-object-norm01-seed46\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-18T00:42:56.715Z\", \"updated_at\": \"2026-05-18T00:43:09.191Z\", \"conclusion\": \"killed\", \"completed_at\": \"2026-05-18T00:43:09.191Z\"}, \"eval-k1-crm-multiscale-object-seed43\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-17T21:05:23.402Z\", \"updated_at\": \"2026-05-17T21:06:09.004Z\", \"hypothesis\": \"Multi-scale K=1 CRM with accumulated gradient refinement improves object manipulation success rate over baseline by providing conformal prediction-based action corrections at multiple spatial scales\", \"spec\": {\"command\": \"python -u src/evaluate.py --mode crm_k1_accg --benchmark object --n_rollouts 10 --seed 43\", \"server\": \"bjb1-32546\", \"data_path\": \"LIBERO-Object\", \"data_count\": 100, \"model_name\": \"SmolVLA+CRM_k1_accg\", \"seed\": 43, \"checkpoint_source\": \"crm_v3_norm\", \"eval_data\": \"LIBERO-Object\", \"checkpoint_path\": \"N/A\", \"log_path\": \"/root/acr-vla-conformal-refinement/logs/eval_k1_crm_multiscale_object_seed43.json\"}, \"conclusion\": \"negative\", \"metrics\": {\"overall_sr\": 0.09, \"successes\": 9, \"rollouts\": 100, \"tasks\": 10, \"suite\": \"LIBERO-object\", \"seed\": 43, \"method\": \"crm_k1_accg\", \"per_task\": {\"alphabet_soup\": 0, \"cream_cheese\": 0, \"salad_dressing\": 0.1, \"bbq_sauce\": 0.2, \"ketchup\": 0, \"tomato_sauce\": 0.2, \"butter\": 0, \"milk\": 0, \"chocolate_pudding\": 0.2, \"orange_juice\": 0.2}}, \"completed_at\": \"2026-05-17T21:06:09.004Z\"}, \"eval-k1-crm-multiscale-object-seed42\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-17T21:05:22.835Z\", \"updated_at\": \"2026-05-17T21:06:08.318Z\", \"hypothesis\": \"Multi-scale K=1 CRM with accumulated gradient refinement improves object manipulation success rate over baseline by providing conformal prediction-based action corrections at multiple spatial scales\", \"spec\": {\"command\": \"python -u src/evaluate.py --mode crm_k1_accg --benchmark object --n_rollouts 10 --seed 42\", \"server\": \"bjb2-28827\", \"data_path\": \"LIBERO-Object\", \"data_count\": 100, \"model_name\": \"SmolVLA+CRM_k1_accg\", \"seed\": 42, \"checkpoint_source\": \"crm_v3_norm\", \"eval_data\": \"LIBERO-Object\", \"checkpoint_path\": \"N/A\", \"log_path\": \"/root/acr-vla-conformal-refinement/logs/eval_k1_crm_multiscale_object_seed42.json\"}, \"conclusion\": \"negative\", \"metrics\": {\"overall_sr\": 0.12, \"successes\": 12, \"rollouts\": 100, \"tasks\": 10, \"suite\": \"LIBERO-object\", \"seed\": 42, \"method\": \"crm_k1_accg\", \"per_task\": {\"alphabet_soup\": 0, \"cream_cheese\": 0, \"salad_dressing\": 0.1, \"bbq_sauce\": 0.2, \"ketchup\": 0, \"tomato_sauce\": 0.3, \"butter\": 0.1, \"milk\": 0, \"chocolate_pudding\": 0.3, \"orange_juice\": 0.2}}, \"completed_at\": \"2026-05-17T21:06:08.318Z\"}, \"eval-k1-crm-multiscale-object-seed44-r2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-17T20:55:44.755Z\", \"updated_at\": \"2026-05-17T20:56:16.602Z\", \"hypothesis\": \"Multi-scale K=1 CRM with accumulated gradient refinement improves object manipulation success rate over baseline by providing conformal prediction-based action corrections at multiple spatial scales\", \"spec\": {\"command\": \"python eval_libero.py --method crm_k1_accg --baseline_mode single --suite object --seed 44 --n_rollouts 10\", \"server\": \"bjb1-18228\", \"data_path\": \"LIBERO-object\", \"data_count\": 100, \"model_name\": \"crm_k1_multiscale\", \"seed\": 44, \"checkpoint_source\": \"crm-k1-train\", \"eval_data\": \"LIBERO-object\"}, \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/crm_k1/crm_k1_best.pt\", \"log_path\": \"/root/acr-vla-conformal-refinement/logs/eval_k1_crm_multiscale_object_seed44_bjb1-18228.json\", \"conclusion\": \"negative\", \"completed_at\": \"2026-05-17T20:56:12.165Z\", \"metrics\": {\"overall_sr\": 0.1, \"successes\": 10, \"rollouts\": 100, \"tasks\": 10, \"suite\": \"LIBERO-object\", \"seed\": 44, \"method\": \"crm_k1_accg\", \"per_task\": {\"alphabet_soup\": 0, \"cream_cheese\": 0, \"salad_dressing\": 0.2, \"bbq_sauce\": 0.1, \"ketchup\": 0, \"tomato_sauce\": 0.1, \"butter\": 0, \"milk\": 0, \"chocolate_pudding\": 0.4, \"orange_juice\": 0.2}}}, \"eval-mag-perdof-norm03-object-r3\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-16T11:05:32.773Z\", \"updated_at\": \"2026-05-16T11:06:06.108Z\", \"conclusion\": \"success\", \"spec\": {\"command\": \"python eval_libero.py --method crm_perdof --suite object --norm 0.3 --seed 42\", \"server\": \"bjb2-28827\", \"data_path\": \"LIBERO-object\", \"data_count\": 100, \"model_name\": \"crm_perdof_norm03\", \"seed\": 42, \"checkpoint_source\": \"crm-train-v3-perdof\", \"eval_data\": \"LIBERO-object\"}, \"log_path\": \"/root/acr-vla-conformal-refinement/logs/eval_object_perdof_norm03_r3.json\", \"checkpoint_path\": \"N/A\", \"completed_at\": \"2026-05-16T11:06:02.462Z\", \"metrics\": {\"success_rate\": 0.04, \"successes\": 4, \"rollouts\": 100, \"tasks\": 10, \"suite\": \"LIBERO-object\", \"norm\": 0.3, \"seed\": 42}}, \"eval-mag-perdof-norm005-object\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-16T08:30:31.627Z\", \"updated_at\": \"2026-05-16T08:30:52.155Z\", \"spec\": {\"command\": \"python evaluate.py --mode crm_perdof --benchmark object --max_correction_norm 0.05 --seed 42\", \"server\": \"bjb2-28827\", \"data_path\": \"/root/acr-vla-conformal-refinement/logs/eval_object_perdof_norm005.json\", \"data_count\": 100, \"model_name\": \"crm_v3_norm_perdof\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt\", \"eval_data\": \"LIBERO object benchmark\"}, \"conclusion\": \"negative\", \"checkpoint_path\": \"/root/acr-vla-conformal-refinement/logs/eval_object_perdof_norm005.json\", \"log_path\": \"/root/acr-vla-conformal-refinement/logs/nohup_eval_object_perdof_norm005.log\", \"completed_at\": \"2026-05-16T08:30:50.635Z\", \"metrics\": {\"overall_sr\": 0.14, \"per_task\": {\"alphabet_soup\": 0, \"cream_cheese\": 0, \"salad_dressing\": 0.2, \"bbq_sauce\": 0.4, \"ketchup\": 0, \"tomato_sauce\": 0, \"butter\": 0, \"milk\": 0.2, \"chocolate_pudding\": 0.4, \"orange_juice\": 0.2}}}, \"eval-mag-obsonly-norm03-object\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-16T07:41:31.617Z\", \"updated_at\": \"2026-05-16T07:41:53.597Z\", \"metrics\": {\"tasks_done\": 10, \"tasks_total\": 10, \"overall_sr\": 0.19, \"per_task_sr\": {\"alphabet_soup\": 0, \"cream_cheese\": 0, \"salad_dressing\": 0.3, \"bbq_sauce\": 0.3, \"ketchup\": 0, \"tomato_sauce\": 0.1, \"butter\": 0.2, \"milk\": 0.2, \"chocolate_pudding\": 0.5, \"orange_juice\": 0.3}}, \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\", \"log_path\": \"/root/acr-vla-conformal-refinement/logs/eval_object_obs_only_norm03.log\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-16T07:41:53.597Z\"}}, \"count\": 27, \"total\": 27, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.0878}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "e17f41b1-3dce-49fb-a9e5-f5dd86423ed8",
  "uuid": "816e2354-1301-4521-9ff3-f0f4319a035a",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"experiments\\\": {\\\"eval-perdof-object-norm02-seed49\\\": {\\\"status\\\": \\\"DONE\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-20T15:59:12.635Z\\\", \\\"updated_at\\\": \\\"2026-05-20T15:59:54.757Z\\\", \\\"metrics\\\": {\\\"overall_success_rate\\\": 0.12, \\\"total_rollouts\\\": 100, \\\"total_successes\\\": 12, \\\"per_task_sr\\\": {\\\"alphabet_soup\\\": 0, \\\"cream_cheese\\\": 0, \\\"salad_dressing\\\": 0.1, \\\"bbq_sauce\\\": 0.2, \\\"ketchup\\\": 0, \\\"tomato_sauce\\\": 0, \\\"butter\\\": 0.1, \\\"milk\\\": 0.2, \\\"chocolate_pudding\\\": 0.4, \\\"orange_juice\\\": 0.2}}, \\\"log_path\\\": \\\"/root/acr-vla-conformal-refinement/logs/eval-perdof-object-norm02-seed49.log\\\", \\\"checkpoint_path\\\": \\\"/root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt\\\", \\\"spec\\\": {\\\"command\\\": \\\"python evaluate.py --mode crm_perdof --benchmark object --seed 49 --K 10 --max_correction_norm 0.2 --n_rollouts 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt --output_file logs/eval_perdof_object_norm02_seed49.json\\\", \\\"server\\\": \\\"bjb1-32546\\\", \\\"data_path\\\": \\\"LIBERO-Object\\\", \\\"data_count\\\": 100, \\\"model_name\\\": \\\"crm_perdof_norm02_K10\\\", \\\"seed\\\": 49, \\\"checkpoint_source\\\": \\\"/root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt\\\", \\\"eval_data\\\": \\\"LIBERO-Object\\\"}, \\\"hypothesis\\\": \\\"PerDoF CRM with norm-clipped corrections (epsilon=0.2, K=10) provides consistent improvement over baseline on LIBERO-Object across seeds; seed49 should yield SR in the 14-18% range consistent with seeds 43-48.\\\", \\\"conclusion\\\": \\\"success\\\", \\\"completed_at\\\": \\\"2026-05-20T15:59:54.757Z\\\"}, \\\"eval-obs-only-goal-norm02-seed52\\\": {\\\"status\\\": \\\"DONE\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-20T12:05:20.840Z\\\", \\\"updated_at\\\": \\\"2026-05-20T12:58:35.610Z\\\", \\\"spec\\\": {\\\"command\\\": \\\"python -u src/evaluate.py --mode crm_obs_only --benchmark LIBERO-Goal --seed 52 --n_rollouts 10 --max_correction_norm 0.2\\\", \\\"server\\\": \\\"bjb1-32546\\\", \\\"gpu\\\": \\\"cuda:0\\\", \\\"pid\\\": 362579, \\\"data_path\\\": \\\"LIBERO-Goal\\\", \\\"data_count\\\": \\\"10 tasks x 10 rollouts\\\", \\\"model_name\\\": \\\"openvla-7b + CRM obs_only\\\", \\\"seed\\\": 52, \\\"checkpoint_source\\\": \\\"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\\\", \\\"eval_data\\\": \\\"LIBERO-Goal (10 tasks x 10 rollouts)\\\", \\\"log_path\\\": \\\"~/runs/acr-vla-conformal-refinement/eval-obs-only-goal-norm02-seed52.log\\\", \\\"checkpoint_path\\\": \\\"N/A (eval only)\\\"}, \\\"metrics\\\": {\\\"success_rate\\\": 0.68, \\\"successes\\\": 68, \\\"total\\\": 100, \\\"per_task_sr\\\": {\\\"open_middle_drawer_cabinet\\\": 0.7, \\\"put_bowl_on_stove\\\": 0.9, \\\"put_wine_bottle_on_cabinet\\\": 0.4, \\\"open_top_drawer_put_bowl\\\": 0.3, \\\"put_bowl_on_cabinet\\\": 0.8, \\\"push_plate_front_stove\\\": 0.8, \\\"put_cream_cheese_in_bowl\\\": 0.4, \\\"turn_on_stove\\\": 1, \\\"put_bowl_on_plate\\\": 1, \\\"put_wine_bottle_on_rack\\\": 0.5}}, \\\"conclusion\\\": \\\"success\\\", \\\"hypothesis\\\": \\\"CRM obs_only with K=10 and norm cap 0.2 improves SR on LIBERO-Goal by applying observation-conditioned corrections that compensate for VLA action prediction errors, providing a new seed for variance estimation.\\\", \\\"completed_at\\\": \\\"2026-05-20T12:58:26.417Z\\\", \\\"notes\\\": \\\"SR=68% on Goal seed52. Strong result; turn_on_stove and put_bowl_on_plate both 100%.\\\"}, \\\"eval-argmin-object-seed49\\\": {\\\"status\\\": \\\"DONE\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-20T12:05:22.690Z\\\", \\\"updated_at\\\": \\\"2026-05-20T12:58:34.569Z\\\", \\\"spec\\\": {\\\"command\\\": \\\"python -u src/evaluate.py --mode reconvla --benchmark LIBERO-Object --seed 49 --n_rollouts 10\\\", \\\"server\\\": \\\"bjb1-32546\\\", \\\"gpu\\\": \\\"cuda:5\\\", \\\"pid\\\": 364591, \\\"data_path\\\": \\\"LIBERO-Object\\\", \\\"data_count\\\": \\\"10 tasks x 10 rollouts\\\", \\\"model_name\\\": \\\"openvla-7b + CRM obs_only (argmin)\\\", \\\"seed\\\": 49, \\\"checkpoint_source\\\": \\\"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\\\", \\\"eval_data\\\": \\\"LIBERO-Object (10 tasks x 10 rollouts)\\\", \\\"log_path\\\": \\\"~/runs/acr-vla-conformal-refinement/eval-argmin-object-seed49.log\\\", \\\"checkpoint_path\\\": \\\"N/A (eval only)\\\"}, \\\"metrics\\\": {\\\"success_rate\\\": 0.16, \\\"successes\\\": 16, \\\"total\\\": 100, \\\"per_task_sr\\\": {\\\"alphabet_soup\\\": 0, \\\"cream_cheese\\\": 0, \\\"salad_dressing\\\": 0.2, \\\"bbq_sauce\\\": 0.4, \\\"ketchup\\\": 0, \\\"tomato_sauce\\\": 0.1, \\\"butter\\\": 0.1, \\\"milk\\\": 0.3, \\\"chocolate_pudding\\\": 0.3, \\\"orange_juice\\\": 0.2}}, \\\"conclusion\\\": \\\"success\\\", \\\"hypothesis\\\": \\\"Argmin (reconvla) selection among K=10 CRM refinements improves over single-step VLA on Object by choosing the candidate with lowest predicted residual, providing a multi-seed consistency check.\\\", \\\"completed_at\\\": \\\"2026-05-20T12:58:25.905Z\\\", \\\"notes\\\": \\\"SR=16% on Object seed49. Consistent with other argmin seeds on Object benchmark.\\\"}, \\\"eval-random-selection-spatial-seed43\\\": {\\\"status\\\": \\\"DONE\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-20T12:05:19.438Z\\\", \\\"updated_at\\\": \\\"2026-05-20T12:58:33.167Z\\\", \\\"spec\\\": {\\\"command\\\": \\\"python -u src/evaluate.py --mode random_selection --benchmark LIBERO-Spatial --seed 43 --n_rollouts 10\\\", \\\"server\\\": \\\"bjb1-18228\\\", \\\"gpu\\\": \\\"cuda:1\\\", \\\"pid\\\": 347075, \\\"data_path\\\": \\\"LIBERO-Spatial\\\", \\\"data_count\\\": \\\"10 tasks x 10 rollouts\\\", \\\"model_name\\\": \\\"openvla-7b + CRM obs_only\\\", \\\"seed\\\": 43, \\\"checkpoint_source\\\": \\\"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\\\", \\\"eval_data\\\": \\\"LIBERO-Spatial (10 tasks x 10 rollouts)\\\", \\\"log_path\\\": \\\"~/runs/acr-vla-conformal-refinement/eval-random-selection-spatial-seed43.log\\\", \\\"checkpoint_path\\\": \\\"N/A (eval only)\\\"}, \\\"metrics\\\": {\\\"success_rate\\\": 0.26, \\\"successes\\\": 26, \\\"total\\\": 100, \\\"per_task_sr\\\": {\\\"between_plate_ramekin\\\": 0.7, \\\"next_to_ramekin\\\": 0.9, \\\"table_center\\\": 0, \\\"cookie_box\\\": 0.1, \\\"top_drawer\\\": 0, \\\"on_ramekin\\\": 0, \\\"next_to_cookie_box\\\": 0.7, \\\"on_stove\\\": 0, \\\"next_to_plate\\\": 0.2, \\\"on_wooden_cabinet\\\": 0}}, \\\"conclusion\\\": \\\"success\\\", \\\"hypothesis\\\": \\\"Random candidate selection from K=10 CRM refinements serves as a lower-bound baseline, showing that informed selection (argmin) is necessary to achieve the full benefit of multi-step refinement on Spatial.\\\", \\\"completed_at\\\": \\\"2026-05-20T12:58:24.969Z\\\", \\\"notes\\\": \\\"SR=26% on Spatial seed43. Lower than argmin-based selection, confirming informed selection matters.\\\"}, \\\"eval-adaptive-k-spatial-p90-seed43\\\": {\\\"status\\\": \\\"DONE\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-20T10:52:06.660Z\\\", \\\"updated_at\\\": \\\"2026-05-20T12:58:31.849Z\\\", \\\"spec\\\": {\\\"command\\\": \\\"python -u src/evaluate.py --mode adaptive_k --benchmark LIBERO-Spatial --seed 43 --n_rollouts 10 --adaptive_k_threshold 0.125870 --output_file logs/eval-adaptive-k-spatial-p90-seed43.json\\\", \\\"server\\\": \\\"bjb1-18228\\\", \\\"gpu\\\": \\\"cuda:3\\\", \\\"pid\\\": 344852, \\\"data_path\\\": \\\"LIBERO-Spatial\\\", \\\"data_count\\\": \\\"10 tasks x 10 rollouts\\\", \\\"model_name\\\": \\\"openvla-7b + CRM obs_only\\\", \\\"seed\\\": 43, \\\"checkpoint_source\\\": \\\"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\\\", \\\"eval_data\\\": \\\"LIBERO-Spatial (10 tasks x 10 rollouts)\\\", \\\"log_path\\\": \\\"~/runs/acr-vla-conformal-refinement/eval-adaptive-k-spatial-p90-seed43.log\\\", \\\"checkpoint_path\\\": \\\"N/A (eval only)\\\"}, \\\"metrics\\\": {\\\"success_rate\\\": 0.32, \\\"successes\\\": 32, \\\"total\\\": 100, \\\"avg_K\\\": 3.6, \\\"fast_path_pct\\\": 80.2, \\\"mean_l2\\\": 0.0905, \\\"per_task_sr\\\": {\\\"between_plate_ramekin\\\": 0.7, \\\"next_to_ramekin\\\": 1, \\\"table_center\\\": 0.1, \\\"cookie_box\\\": 0.3, \\\"top_drawer\\\": 0, \\\"on_ramekin\\\": 0.1, \\\"next_to_cookie_box\\\": 0.8, \\\"on_stove\\\": 0, \\\"next_to_plate\\\": 0.2, \\\"on_wooden_cabinet\\\": 0}}, \\\"conclusion\\\": \\\"success\\\", \\\"hypothesis\\\": \\\"Adaptive K with P90 threshold (τ=0.1259) reduces average refinement steps while maintaining comparable SR to fixed K=10 on Spatial, because most states have low CRM residuals and can skip full refinement.\\\", \\\"completed_at\\\": \\\"2026-05-20T12:58:23.572Z\\\", \\\"notes\\\": \\\"SR=32%, avg_K=3.6 (vs fixed K=10), 80.2% fast-path. Adaptive K saves ~64% compute with seed43 on Spatial.\\\"}, \\\"eval-adaptive-k-object-p90-seed44\\\": {\\\"status\\\": \\\"DONE\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-20T12:45:08.564Z\\\", \\\"updated_at\\\": \\\"2026-05-20T12:45:37.089Z\\\", \\\"hypothesis\\\": \\\"Adaptive K with τ=P90 (0.125870) on LIBERO-Object seed44. P90 是最宽松的阈值——大部分 step fast-path (K=1)，仅在极高不确定性时用 K=10。验证 P90 在 Object 上的 SR/compute tradeoff。\\\", \\\"spec\\\": {\\\"command\\\": \\\"python -u src/evaluate.py --mode adaptive_k --benchmark LIBERO-Object --seed 44 --n_rollouts 10 --adaptive_k_threshold 0.125870\\\", \\\"server\\\": \\\"bjb2-28827\\\", \\\"data_path\\\": \\\"LIBERO-Object\\\", \\\"data_count\\\": \\\"10 tasks x 10 rollouts\\\", \\\"model_name\\\": \\\"openvla-7b + CRM obs_only\\\", \\\"seed\\\": 44, \\\"checkpoint_source\\\": \\\"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\\\", \\\"eval_data\\\": \\\"LIBERO-Object (10 tasks x 10 rollouts)\\\", \\\"log_path\\\": \\\"N/A (discovered by Reviewer)\\\", \\\"checkpoint_path\\\": \\\"N/A (eval only)\\\"}, \\\"metrics\\\": {\\\"sr\\\": 14, \\\"avg_K\\\": 2.58, \\\"fast_path_pct\\\": 92.8, \\\"total_rollouts\\\": 100}, \\\"conclusion\\\": \\\"success\\\", \\\"completed_at\\\": \\\"2026-05-20T12:45:37.089Z\\\"}, \\\"eval-adaptive-k-object-p90-seed43\\\": {\\\"status\\\": \\\"DONE\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-20T12:45:08.312Z\\\", \\\"updated_at\\\": \\\"2026-05-20T12:45:34.700Z\\\", \\\"hypothesis\\\": \\\"Adaptive K with τ=P90 (0.125870) on LIBERO-Object seed43. P90 是最宽松的阈值——大部分 step fast-path (K=1)，仅在极高不确定性时用 K=10。验证 P90 在 Object 上的 SR/compute tradeoff。\\\", \\\"spec\\\": {\\\"command\\\": \\\"python -u src/evaluate.py --mode adaptive_k --benchmark LIBERO-Object --seed 43 --n_rollouts 10 --adaptive_k_threshold 0.125870\\\", \\\"server\\\": \\\"bjb2-28827\\\", \\\"data_path\\\": \\\"LIBERO-Object\\\", \\\"data_count\\\": \\\"10 tasks x 10 rollouts\\\", \\\"model_name\\\": \\\"openvla-7b + CRM obs_only\\\", \\\"seed\\\": 43, \\\"checkpoint_source\\\": \\\"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\\\", \\\"eval_data\\\": \\\"LIBERO-Object (10 tasks x 10 rollouts)\\\", \\\"log_path\\\": \\\"N/A (discovered by Reviewer)\\\", \\\"checkpoint_path\\\": \\\"N/A (eval only)\\\"}, \\\"metrics\\\": {\\\"sr\\\": 14, \\\"avg_K\\\": 2.61, \\\"fast_path_pct\\\": 92.3, \\\"total_rollouts\\\": 100}, \\\"conclusion\\\": \\\"success\\\", \\\"completed_at\\\": \\\"2026-05-20T12:45:34.700Z\\\"}, \\\"eval-adaptive-k-spatial-p50-seed42\\\": {\\\"status\\\": \\\"DONE\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-20T11:24:12.894Z\\\", \\\"updated_at\\\": \\\"2026-05-20T11:25:16.991Z\\\", \\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"sr\\\": 30, \\\"avg_K\\\": 6.324, \\\"fast_path_pct\\\": 45.95, \\\"mean_l2\\\": 0.0903, \\\"total_rollouts\\\": 100}, \\\"failure_reason\\\": \\\"\\\", \\\"completed_at\\\": \\\"2026-05-20T11:06:00.000Z\\\", \\\"notes\\\": \\\"Reviewer 独立验证：JSON 完整，日志确认 SR=30%，PID 自然退出。之前被 cron 误判为 failed（PID dead + 无 sentinel），已修正为 success。\\\", \\\"spec\\\": {\\\"command\\\": \\\"python -u src/evaluate.py --mode adaptive_k --benchmark LIBERO-Spatial --seed 42 --n_rollouts 10 --adaptive_k_threshold 0.074855\\\", \\\"server\\\": \\\"bjb2-40593\\\", \\\"gpu\\\": \\\"cuda:0\\\", \\\"pid\\\": 681823, \\\"data_path\\\": \\\"LIBERO-Spatial\\\", \\\"data_count\\\": \\\"10 tasks x 10 rollouts\\\", \\\"model_name\\\": \\\"openvla-7b + CRM obs_only\\\", \\\"seed\\\": 42, \\\"checkpoint_source\\\": \\\"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\\\", \\\"eval_data\\\": \\\"LIBERO-Spatial (10 tasks x 10 rollouts)\\\", \\\"log_path\\\": \\\"~/runs/acr-vla-conformal-refinement/eval-adaptive-k-spatial-p50-seed42.log\\\", \\\"checkpoint_path\\\": \\\"N/A (eval only)\\\"}, \\\"hypothesis\\\": \\\"Adaptive K with τ=P50 (0.074855, Object-calibrated) on LIBERO-Spatial seed42. 验证 Adaptive K 方法在第二个 benchmark 上的泛化：使用 Object 上校准的阈值直接应用到 Spatial（无 per-benchmark tuning）。如果 SR 接近 CRM K=10 (34.3%) 且 fast_path >50%，则证明方法跨 benchmark 通用。\\\"}, \\\"eval-obs-only-object-norm003-seed44\\\": {\\\"status\\\": \\\"DONE\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-20T10:52:14.742Z\\\", \\\"updated_at\\\": \\\"2026-05-20T10:52:47.202Z\\\", \\\"hypothesis\\\": \\\"CRM obs_only ε=0.03 on Object seed44. Low-norm multi-seed supplement (plan_500): strengthens Figure 2 error bars at small ε.\\\", \\\"spec\\\": {\\\"command\\\": \\\"evaluate.py --mode crm_obs_only --benchmark object --seed 44 --n_rollouts 10 --K 10 --max_correction_norm 0.03\\\", \\\"server\\\": \\\"bjb2-28827\\\", \\\"seed\\\": 44, \\\"model_name\\\": \\\"crm_v3_norm/obs_only/crm_best.pt\\\", \\\"data_path\\\": \\\"LIBERO_object\\\", \\\"data_count\\\": 100}, \\\"log_path\\\": \\\"~/runs/acr-vla-conformal-refinement/eval-obs-only-object-norm003-seed44.log\\\", \\\"checkpoint_path\\\": \\\"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\\\", \\\"metrics\\\": {\\\"overall_success_rate\\\": 0.15, \\\"total_successes\\\": 15, \\\"total_rollouts\\\": 100, \\\"per_task\\\": {\\\"alphabet_soup\\\": 0, \\\"cream_cheese\\\": 0, \\\"salad_dressing\\\": 0.3, \\\"bbq_sauce\\\": 0.2, \\\"ketchup\\\": 0, \\\"tomato_sauce\\\": 0.1, \\\"butter\\\": 0.1, \\\"milk\\\": 0.2, \\\"chocolate_pudding\\\": 0.3, \\\"orange_juice\\\": 0.3}}, \\\"conclusion\\\": \\\"success\\\", \\\"completed_at\\\": \\\"2026-05-20T10:52:47.202Z\\\"}, \\\"eval-random-selection-object-seed46-r2\\\": {\\\"status\\\": \\\"DONE\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-19T17:41:16.541Z\\\", \\\"updated_at\\\": \\\"2026-05-19T17:41:32.255Z\\\", \\\"spec\\\": {\\\"command\\\": \\\"cd /root/acr-vla-conformal-refinement && timeout 57600 /root/miniconda3/bin/python -u src/evaluate.py --mode random_selection --benchmark object --n_rollouts 10 --seed 46 --K 10 --output_file logs/eval_object_random_selection_seed46.json\\\", \\\"server\\\": \\\"bjb2-40593\\\", \\\"data_path\\\": \\\"LIBERO-Object\\\", \\\"data_count\\\": 100, \\\"model_name\\\": \\\"SmolVLA_random_selection\\\", \\\"seed\\\": 46, \\\"checkpoint_path\\\": \\\"N/A-eval-only\\\", \\\"log_path\\\": \\\"/root/acr-vla-conformal-refinement/logs/eval_object_random_selection_seed46.log\\\"}, \\\"hypothesis\\\": \\\"Random selection baseline (K=10) on LIBERO-Object seed46 establishes reference success rate for comparing against CRM-guided selection methods\\\", \\\"conclusion\\\": \\\"killed\\\", \\\"completed_at\\\": \\\"2026-05-19T17:41:32.255Z\\\"}, \\\"eval-obs-only-spatial-norm02-seed47\\\": {\\\"status\\\": \\\"DONE\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-19T17:02:40.986Z\\\", \\\"updated_at\\\": \\\"2026-05-19T17:03:14.457Z\\\", \\\"metrics\\\": {\\\"success_rate\\\": 0.32, \\\"successes\\\": 32, \\\"total\\\": 100, \\\"n_tasks\\\": 10, \\\"n_rollouts\\\": 10, \\\"per_task\\\": {\\\"between_plate_and_ramekin\\\": 0.8, \\\"next_to_ramekin\\\": 0.9, \\\"from_table_center\\\": 0, \\\"on_cookie_box\\\": 0.3, \\\"in_top_drawer\\\": 0.1, \\\"on_ramekin\\\": 0, \\\"next_to_cookie_box\\\": 0.9, \\\"on_stove\\\": 0, \\\"next_to_plate\\\": 0.2, \\\"on_wooden_cabinet\\\": 0}}, \\\"checkpoint_path\\\": \\\"N/A-eval-only\\\", \\\"log_path\\\": \\\"~/runs/acr-vla-conformal-refinement/eval-obs-only-spatial-norm02-seed47.log\\\", \\\"conclusion\\\": \\\"success\\\", \\\"spec\\\": {\\\"command\\\": \\\"cd /root/acr-vla-conformal-refinement && /root/miniconda3/bin/python -u src/evaluate.py --mode crm_obs_only --benchmark spatial --n_rollouts 10 --seed 47 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --max_correction_norm 0.2 --output_file logs/eval_spatial_obs_only_norm02_seed47.json\\\", \\\"server\\\": \\\"bjb1-32546\\\", \\\"data_path\\\": \\\"LIBERO-Spatial\\\", \\\"data_count\\\": 100, \\\"model_name\\\": \\\"crm_obs_only\\\", \\\"seed\\\": 47}, \\\"hypothesis\\\": \\\"obs_only CRM with epsilon=0.2 and K=10 improves success rate over VLA-only baseline on LIBERO-Spatial because observation-conditioned conformal corrections can detect and fix spatial reasoning errors without requiring action history\\\", \\\"completed_at\\\": \\\"2026-05-19T17:03:14.457Z\\\"}, \\\"eval-vla-only-spatial-seed45\\\": {\\\"status\\\": \\\"DONE\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-19T15:19:50.220Z\\\", \\\"updated_at\\\": \\\"2026-05-19T15:20:24.563Z\\\", \\\"spec\\\": {\\\"log_path\\\": \\\"~/runs/acr-vla-conformal-refinement/eval-vla-only-spatial-seed45.log\\\", \\\"command\\\": \\\"python evaluate.py --benchmark spatial --mode vla_only --seed 45\\\", \\\"server\\\": \\\"bjb1-32546\\\", \\\"seed\\\": 45, \\\"data_path\\\": \\\"LIBERO-Spatial\\\", \\\"data_count\\\": 100, \\\"model_name\\\": \\\"SmolVLA\\\", \\\"checkpoint_path\\\": \\\"N/A (eval-only)\\\"}, \\\"metrics\\\": {\\\"success_rate\\\": 0.27, \\\"per_task\\\": {\\\"between_plate_and_ramekin\\\": 0.7, \\\"next_to_ramekin\\\": 0.9, \\\"from_table_center\\\": 0, \\\"on_cookie_box\\\": 0.2, \\\"in_top_drawer\\\": 0, \\\"on_ramekin\\\": 0, \\\"next_to_cookie_box\\\": 0.9, \\\"on_stove\\\": 0, \\\"next_to_plate\\\": 0, \\\"on_wooden_cabinet\\\": 0}, \\\"successes\\\": 27, \\\"total\\\": 100}, \\\"conclusion\\\": \\\"success\\\", \\\"hypothesis\\\": \\\"VLA-only baseline on LIBERO-Spatial with seed 45 establishes reference success rate for comparison with CRM-augmented methods\\\", \\\"completed_at\\\": \\\"2026-05-19T15:20:24.563Z\\\"}, \\\"eval-obs-only-spatial-norm02-seed44\\\": {\\\"status\\\": \\\"DONE\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-19T14:23:33.161Z\\\", \\\"updated_at\\\": \\\"2026-05-19T14:26:44.810Z\\\", \\\"metrics\\\": {\\\"success_rate\\\": 0.36, \\\"successes\\\": 36, \\\"total\\\": 100}, \\\"checkpoint_path\\\": \\\"N/A (eval only)\\\", \\\"log_path\\\": \\\"/root/acr-vla-conformal-refinement/logs/eval_spatial_obs_only_norm02_seed44.json\\\", \\\"conclusion\\\": \\\"success\\\", \\\"spec\\\": {\\\"command\\\": \\\"python eval_crm.py --mode crm_obs_only --benchmark spatial --K 10 --seed 44 --max_correction_norm 0.2\\\", \\\"server\\\": \\\"bjb2-28827\\\", \\\"data_path\\\": \\\"spatial_benchmark\\\", \\\"data_count\\\": 100, \\\"model_name\\\": \\\"crm_obs_only\\\", \\\"seed\\\": 44}, \\\"hypothesis\\\": \\\"CRM obs-only mode with max_correction_norm=0.2 can improve spatial benchmark success rate by refining VLA actions using only observation-based conformal prediction, without access to privileged state information.\\\", \\\"completed_at\\\": \\\"2026-05-19T14:24:10.857Z\\\"}, \\\"eval-obs-only-object-norm003-seed43-r2\\\": {\\\"status\\\": \\\"DONE\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-19T05:14:10.523Z\\\", \\\"updated_at\\\": \\\"2026-05-19T05:14:25.385Z\\\", \\\"conclusion\\\": \\\"failed\\\", \\\"spec\\\": {\\\"checkpoint_path\\\": \\\"N/A (eval-only)\\\", \\\"log_path\\\": \\\"/root/acr-vla-conformal-refinement/logs/eval_object_obs_only_norm003_seed43.log\\\", \\\"metrics\\\": {\\\"success_rate\\\": null, \\\"tasks_completed\\\": \\\"1/10\\\", \\\"failure_reason\\\": \\\"process terminated prematurely after 1 task\\\"}}, \\\"completed_at\\\": \\\"2026-05-19T05:14:25.385Z\\\"}, \\\"eval-obs-only-object-norm03-seed48\\\": {\\\"status\\\": \\\"DONE\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-18T13:26:49.122Z\\\", \\\"updated_at\\\": \\\"2026-05-18T13:27:19.389Z\\\", \\\"metrics\\\": {\\\"overall_success_rate\\\": 0.16, \\\"per_task\\\": {\\\"pick_up_the_alphabet_soup_and_place_it_in_the_basket\\\": 0, \\\"pick_up_the_cream_cheese_and_place_it_in_the_basket\\\": 0, \\\"pick_up_the_salad_dressing_and_place_it_in_the_basket\\\": 0.3, \\\"pick_up_the_bbq_sauce_and_place_it_in_the_basket\\\": 0.4, \\\"pick_up_the_ketchup_and_place_it_in_the_basket\\\": 0, \\\"pick_up_the_tomato_sauce_and_place_it_in_the_basket\\\": 0.1, \\\"pick_up_the_butter_and_place_it_in_the_basket\\\": 0.1, \\\"pick_up_the_milk_and_place_it_in_the_basket\\\": 0.1, \\\"pick_up_the_chocolate_pudding_and_place_it_in_the_basket\\\": 0.4, \\\"pick_up_the_orange_juice_and_place_it_in_the_basket\\\": 0.2}}, \\\"log_path\\\": \\\"/root/acr-vla-conformal-refinement/logs/eval_object_obs_only_norm03_seed48.json\\\", \\\"checkpoint_path\\\": \\\"N/A (eval only)\\\", \\\"conclusion\\\": \\\"success\\\", \\\"spec\\\": {\\\"command\\\": \\\"eval obs_only CRM epsilon=0.3 seed48 on LIBERO-Object K=10 n_rollouts=10\\\", \\\"server\\\": \\\"bjb1-18228\\\", \\\"data_path\\\": \\\"LIBERO-Object\\\", \\\"data_count\\\": 100, \\\"model_name\\\": \\\"openvla\\\", \\\"seed\\\": 48}, \\\"hypothesis\\\": \\\"CRM with obs_only mode and epsilon=0.3 normalization threshold will improve success rate on LIBERO-Object by filtering unreliable action predictions based solely on observation conformity scores\\\", \\\"completed_at\\\": \\\"2026-05-18T13:27:19.389Z\\\"}, \\\"eval-obs-only-object-norm01-seed48\\\": {\\\"status\\\": \\\"DONE\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-18T11:42:37.233Z\\\", \\\"updated_at\\\": \\\"2026-05-18T11:43:15.403Z\\\", \\\"hypothesis\\\": \\\"obs_only CRM with max_correction_norm=0.1 on LIBERO-Object seed48. Tests whether obs_only mode with conservative norm clipping maintains performance across seeds.\\\", \\\"spec\\\": {\\\"command\\\": \\\"CUDA_VISIBLE_DEVICES=1 /root/miniconda3/bin/python -u src/evaluate.py --mode crm_obs_only --benchmark object --n_rollouts 10 --seed 48 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --max_correction_norm 0.1 --output_file logs/eval_object_obs_only_norm01_seed48.json\\\", \\\"server\\\": \\\"bjb1-18228\\\", \\\"data_path\\\": \\\"LIBERO-Object\\\", \\\"data_count\\\": 100, \\\"model_name\\\": \\\"SmolVLA+CRM_obs_only\\\", \\\"seed\\\": 48, \\\"checkpoint_source\\\": \\\"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\\\", \\\"eval_data\\\": \\\"LIBERO-Object\\\"}, \\\"log_path\\\": \\\"/root/acr-vla-conformal-refinement/logs/eval_object_obs_only_norm01_seed48.json\\\", \\\"checkpoint_path\\\": \\\"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\\\", \\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"success_rate\\\": 0.18, \\\"n_tasks\\\": 10, \\\"n_rollouts\\\": 10, \\\"per_task\\\": {\\\"alphabet_soup\\\": 0, \\\"cream_cheese\\\": 0, \\\"salad_dressing\\\": 0, \\\"bbq_sauce\\\": 0.4, \\\"ketchup\\\": 0.1, \\\"tomato_sauce\\\": 0.2, \\\"butter\\\": 0.2, \\\"milk\\\": 0.3, \\\"chocolate_pudding\\\": 0.3, \\\"orange_juice\\\": 0.3}}, \\\"completed_at\\\": \\\"2026-05-18T11:43:15.403Z\\\"}, \\\"eval-obs-only-object-norm02-k5-seed42\\\": {\\\"status\\\": \\\"DONE\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-18T03:44:47.522Z\\\", \\\"updated_at\\\": \\\"2026-05-18T03:45:04.655Z\\\", \\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"overall_sr\\\": 0.14, \\\"successes\\\": 14, \\\"rollouts\\\": 100, \\\"tasks\\\": 10, \\\"suite\\\": \\\"LIBERO-object\\\", \\\"seed\\\": 42, \\\"method\\\": \\\"crm_obs_only\\\", \\\"K\\\": 5, \\\"max_correction_norm\\\": 0.2}, \\\"hypothesis\\\": \\\"obs_only CRM with K=5 candidates and ε=0.2 on LIBERO-Object seed42. Tests whether fewer candidates (K=5 vs K=10) reduces selection quality. K=5 SR=14% vs K=10 SR=17.5% confirms monotonic improvement with more candidates.\\\", \\\"spec\\\": {\\\"command\\\": \\\"python -u src/evaluate.py --mode crm_obs_only --benchmark object --n_rollouts 10 --seed 42 --K 5 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --max_correction_norm 0.2 --output_file logs/eval_object_obs_only_norm02_k5_seed42.json\\\", \\\"server\\\": \\\"bjb1-18228\\\", \\\"data_path\\\": \\\"LIBERO-Object\\\", \\\"data_count\\\": 100, \\\"model_name\\\": \\\"SmolVLA+CRM_obs_only\\\", \\\"seed\\\": 42, \\\"K\\\": 5, \\\"checkpoint_source\\\": \\\"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\\\", \\\"eval_data\\\": \\\"LIBERO-Object\\\", \\\"checkpoint_path\\\": \\\"N/A\\\", \\\"log_path\\\": \\\"/root/acr-vla-conformal-refinement/logs/eval_object_obs_only_norm02_k5_seed42.json\\\"}, \\\"completed_at\\\": \\\"2026-05-18T03:45:04.655Z\\\"}, \\\"eval-perdof-object-norm01-seed46\\\": {\\\"status\\\": \\\"DONE\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-18T03:05:55.543Z\\\", \\\"updated_at\\\": \\\"2026-05-18T03:06:14.048Z\\\", \\\"hypothesis\\\": \\\"perdof CRM with ε=0.1 on LIBERO-Object seed46. Magnitude curve data point for perdof at intermediate norm. SR=10% confirms perdof degrades from peak at low norms.\\\", \\\"metrics\\\": {\\\"overall_sr\\\": 0.1, \\\"successes\\\": 10, \\\"rollouts\\\": 100, \\\"tasks\\\": 10, \\\"suite\\\": \\\"LIBERO-object\\\", \\\"seed\\\": 46, \\\"method\\\": \\\"crm_perdof\\\", \\\"max_correction_norm\\\": 0.1}, \\\"conclusion\\\": \\\"success\\\", \\\"spec\\\": {\\\"command\\\": \\\"python -u src/evaluate.py --mode crm_perdof --benchmark object --n_rollouts 10 --seed 46 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt --max_correction_norm 0.1 --output_file logs/eval_object_perdof_norm01_seed46.json\\\", \\\"server\\\": \\\"bjb1-32546\\\", \\\"data_path\\\": \\\"LIBERO-Object\\\", \\\"data_count\\\": 100, \\\"model_name\\\": \\\"SmolVLA+CRM_perdof\\\", \\\"seed\\\": 46, \\\"checkpoint_source\\\": \\\"/root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt\\\", \\\"eval_data\\\": \\\"LIBERO-Object\\\", \\\"checkpoint_path\\\": \\\"N/A\\\", \\\"log_path\\\": \\\"/root/acr-vla-conformal-refinement/logs/eval_object_perdof_norm01_seed46.json\\\"}, \\\"completed_at\\\": \\\"2026-05-18T03:06:14.049Z\\\"}, \\\"eval-perdof-object-default-seed46\\\": {\\\"status\\\": \\\"DONE\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-18T03:05:29.784Z\\\", \\\"updated_at\\\": \\\"2026-05-18T03:06:03.735Z\\\", \\\"conclusion\\\": \\\"negative\\\", \\\"hypothesis\\\": \\\"perdof CRM without norm constraint (uncapped correction magnitude) on LIBERO-Object seed46. Tests whether perdof maintains performance without explicit correction capping. SR=0% confirms perdof corrections are catastrophically unstable without norm constraints.\\\", \\\"spec\\\": {\\\"command\\\": \\\"python -u src/evaluate.py --mode crm_perdof --benchmark object --n_rollouts 10 --seed 46 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt --output_file logs/eval_object_perdof_default_seed46.json\\\", \\\"server\\\": \\\"bjb1-32546\\\", \\\"data_path\\\": \\\"LIBERO-Object\\\", \\\"data_count\\\": 100, \\\"model_name\\\": \\\"SmolVLA+CRM_perdof\\\", \\\"seed\\\": 46, \\\"checkpoint_source\\\": \\\"/root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt\\\", \\\"eval_data\\\": \\\"LIBERO-Object\\\", \\\"checkpoint_path\\\": \\\"N/A\\\", \\\"log_path\\\": \\\"/root/acr-vla-conformal-refinement/logs/eval_object_perdof_default_seed46.json\\\"}, \\\"metrics\\\": {\\\"overall_sr\\\": 0, \\\"successes\\\": 0, \\\"rollouts\\\": 100, \\\"tasks\\\": 10, \\\"suite\\\": \\\"LIBERO-object\\\", \\\"seed\\\": 46, \\\"method\\\": \\\"crm_perdof\\\", \\\"max_correction_norm\\\": \\\"default\\\"}, \\\"completed_at\\\": \\\"2026-05-18T03:06:03.735Z\\\"}, \\\"eval-obs-only-object-default-seed46\\\": {\\\"status\\\": \\\"DONE\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-18T00:59:50.348Z\\\", \\\"updated_at\\\": \\\"2026-05-18T01:00:23.165Z\\\", \\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"overall_sr\\\": 0.15, \\\"successes\\\": 15, \\\"rollouts\\\": 100, \\\"tasks\\\": 10, \\\"suite\\\": \\\"LIBERO-object\\\", \\\"seed\\\": 46, \\\"method\\\": \\\"crm_obs_only\\\", \\\"max_correction_norm\\\": \\\"default\\\", \\\"per_task_sr\\\": {\\\"alphabet_soup\\\": 0, \\\"cream_cheese\\\": 0, \\\"salad_dressing\\\": 0.2, \\\"bbq_sauce\\\": 0.4, \\\"ketchup\\\": 0.1, \\\"tomato_sauce\\\": 0.1, \\\"butter\\\": 0.1, \\\"milk\\\": 0.1, \\\"chocolate_pudding\\\": 0.2, \\\"orange_juice\\\": 0.3}}, \\\"spec\\\": {\\\"checkpoint_path\\\": \\\"N/A\\\", \\\"log_path\\\": \\\"/root/acr-vla-conformal-refinement/logs/eval_object_obs_only_default_seed46.json\\\", \\\"command\\\": \\\"python -u src/evaluate.py --mode crm_obs_only --benchmark object --n_rollouts 10 --seed 46 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --output_file logs/eval_object_obs_only_default_seed46.json\\\", \\\"server\\\": \\\"bjb1-32546\\\", \\\"data_path\\\": \\\"LIBERO-Object\\\", \\\"data_count\\\": 100, \\\"model_name\\\": \\\"SmolVLA+CRM_obs_only\\\", \\\"seed\\\": 46, \\\"checkpoint_source\\\": \\\"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\\\", \\\"eval_data\\\": \\\"LIBERO-Object\\\"}, \\\"hypothesis\\\": \\\"obs_only CRM without norm constraint (uncapped correction magnitude) on LIBERO-Object seed46. Tests whether obs_only maintains performance without explicit correction capping. If uncapped performs worse than capped, it confirms that moderate norm constraints stabilize corrections.\\\", \\\"completed_at\\\": \\\"2026-05-18T01:00:23.165Z\\\"}, \\\"eval-obs-only-object-norm01-seed46\\\": {\\\"status\\\": \\\"DONE\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-18T00:42:56.715Z\\\", \\\"updated_at\\\": \\\"2026-05-18T00:43:09.191Z\\\", \\\"conclusion\\\": \\\"killed\\\", \\\"completed_at\\\": \\\"2026-05-18T00:43:09.191Z\\\"}, \\\"eval-k1-crm-multiscale-object-seed43\\\": {\\\"status\\\": \\\"DONE\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-17T21:05:23.402Z\\\", \\\"updated_at\\\": \\\"2026-05-17T21:06:09.004Z\\\", \\\"hypothesis\\\": \\\"Multi-scale K=1 CRM with accumulated gradient refinement improves object manipulation success rate over baseline by providing conformal prediction-based action corrections at multiple spatial scales\\\", \\\"spec\\\": {\\\"command\\\": \\\"python -u src/evaluate.py --mode crm_k1_accg --benchmark object --n_rollouts 10 --seed 43\\\", \\\"server\\\": \\\"bjb1-32546\\\", \\\"data_path\\\": \\\"LIBERO-Object\\\", \\\"data_count\\\": 100, \\\"model_name\\\": \\\"SmolVLA+CRM_k1_accg\\\", \\\"seed\\\": 43, \\\"checkpoint_source\\\": \\\"crm_v3_norm\\\", \\\"eval_data\\\": \\\"LIBERO-Object\\\", \\\"checkpoint_path\\\": \\\"N/A\\\", \\\"log_path\\\": \\\"/root/acr-vla-conformal-refinement/logs/eval_k1_crm_multiscale_object_seed43.json\\\"}, \\\"conclusion\\\": \\\"negative\\\", \\\"metrics\\\": {\\\"overall_sr\\\": 0.09, \\\"successes\\\": 9, \\\"rollouts\\\": 100, \\\"tasks\\\": 10, \\\"suite\\\": \\\"LIBERO-object\\\", \\\"seed\\\": 43, \\\"method\\\": \\\"crm_k1_accg\\\", \\\"per_task\\\": {\\\"alphabet_soup\\\": 0, \\\"cream_cheese\\\": 0, \\\"salad_dressing\\\": 0.1, \\\"bbq_sauce\\\": 0.2, \\\"ketchup\\\": 0, \\\"tomato_sauce\\\": 0.2, \\\"butter\\\": 0, \\\"milk\\\": 0, \\\"chocolate_pudding\\\": 0.2, \\\"orange_juice\\\": 0.2}}, \\\"completed_at\\\": \\\"2026-05-17T21:06:09.004Z\\\"}, \\\"eval-k1-crm-multiscale-object-seed42\\\": {\\\"status\\\": \\\"DONE\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-17T21:05:22.835Z\\\", \\\"updated_at\\\": \\\"2026-05-17T21:06:08.318Z\\\", \\\"hypothesis\\\": \\\"Multi-scale K=1 CRM with accumulated gradient refinement improves object manipulation success rate over baseline by providing conformal prediction-based action corrections at multiple spatial scales\\\", \\\"spec\\\": {\\\"command\\\": \\\"python -u src/evaluate.py --mode crm_k1_accg --benchmark object --n_rollouts 10 --seed 42\\\", \\\"server\\\": \\\"bjb2-28827\\\", \\\"data_path\\\": \\\"LIBERO-Object\\\", \\\"data_count\\\": 100, \\\"model_name\\\": \\\"SmolVLA+CRM_k1_accg\\\", \\\"seed\\\": 42, \\\"checkpoint_source\\\": \\\"crm_v3_norm\\\", \\\"eval_data\\\": \\\"LIBERO-Object\\\", \\\"checkpoint_path\\\": \\\"N/A\\\", \\\"log_path\\\": \\\"/root/acr-vla-conformal-refinement/logs/eval_k1_crm_multiscale_object_seed42.json\\\"}, \\\"conclusion\\\": \\\"negative\\\", \\\"metrics\\\": {\\\"overall_sr\\\": 0.12, \\\"successes\\\": 12, \\\"rollouts\\\": 100, \\\"tasks\\\": 10, \\\"suite\\\": \\\"LIBERO-object\\\", \\\"seed\\\": 42, \\\"method\\\": \\\"crm_k1_accg\\\", \\\"per_task\\\": {\\\"alphabet_soup\\\": 0, \\\"cream_cheese\\\": 0, \\\"salad_dressing\\\": 0.1, \\\"bbq_sauce\\\": 0.2, \\\"ketchup\\\": 0, \\\"tomato_sauce\\\": 0.3, \\\"butter\\\": 0.1, \\\"milk\\\": 0, \\\"chocolate_pudding\\\": 0.3, \\\"orange_juice\\\": 0.2}}, \\\"completed_at\\\": \\\"2026-05-17T21:06:08.318Z\\\"}, \\\"eval-k1-crm-multiscale-object-seed44-r2\\\": {\\\"status\\\": \\\"DONE\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-17T20:55:44.755Z\\\", \\\"updated_at\\\": \\\"2026-05-17T20:56:16.602Z\\\", \\\"hypothesis\\\": \\\"Multi-scale K=1 CRM with accumulated gradient refinement improves object manipulation success rate over baseline by providing conformal prediction-based action corrections at multiple spatial scales\\\", \\\"spec\\\": {\\\"command\\\": \\\"python eval_libero.py --method crm_k1_accg --baseline_mode single --suite object --seed 44 --n_rollouts 10\\\", \\\"server\\\": \\\"bjb1-18228\\\", \\\"data_path\\\": \\\"LIBERO-object\\\", \\\"data_count\\\": 100, \\\"model_name\\\": \\\"crm_k1_multiscale\\\", \\\"seed\\\": 44, \\\"checkpoint_source\\\": \\\"crm-k1-train\\\", \\\"eval_data\\\": \\\"LIBERO-object\\\"}, \\\"checkpoint_path\\\": \\\"/root/autodl-tmp/checkpoints/crm_k1/crm_k1_best.pt\\\", \\\"log_path\\\": \\\"/root/acr-vla-conformal-refinement/logs/eval_k1_crm_multiscale_object_seed44_bjb1-18228.json\\\", \\\"conclusion\\\": \\\"negative\\\", \\\"completed_at\\\": \\\"2026-05-17T20:56:12.165Z\\\", \\\"metrics\\\": {\\\"overall_sr\\\": 0.1, \\\"successes\\\": 10, \\\"rollouts\\\": 100, \\\"tasks\\\": 10, \\\"suite\\\": \\\"LIBERO-object\\\", \\\"seed\\\": 44, \\\"method\\\": \\\"crm_k1_accg\\\", \\\"per_task\\\": {\\\"alphabet_soup\\\": 0, \\\"cream_cheese\\\": 0, \\\"salad_dressing\\\": 0.2, \\\"bbq_sauce\\\": 0.1, \\\"ketchup\\\": 0, \\\"tomato_sauce\\\": 0.1, \\\"butter\\\": 0, \\\"milk\\\": 0, \\\"chocolate_pudding\\\": 0.4, \\\"orange_juice\\\": 0.2}}}, \\\"eval-mag-perdof-norm03-object-r3\\\": {\\\"status\\\": \\\"DONE\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-16T11:05:32.773Z\\\", \\\"updated_at\\\": \\\"2026-05-16T11:06:06.108Z\\\", \\\"conclusion\\\": \\\"success\\\", \\\"spec\\\": {\\\"command\\\": \\\"python eval_libero.py --method crm_perdof --suite object --norm 0.3 --seed 42\\\", \\\"server\\\": \\\"bjb2-28827\\\", \\\"data_path\\\": \\\"LIBERO-object\\\", \\\"data_count\\\": 100, \\\"model_name\\\": \\\"crm_perdof_norm03\\\", \\\"seed\\\": 42, \\\"checkpoint_source\\\": \\\"crm-train-v3-perdof\\\", \\\"eval_data\\\": \\\"LIBERO-object\\\"}, \\\"log_path\\\": \\\"/root/acr-vla-conformal-refinement/logs/eval_object_perdof_norm03_r3.json\\\", \\\"checkpoint_path\\\": \\\"N/A\\\", \\\"completed_at\\\": \\\"2026-05-16T11:06:02.462Z\\\", \\\"metrics\\\": {\\\"success_rate\\\": 0.04, \\\"successes\\\": 4, \\\"rollouts\\\": 100, \\\"tasks\\\": 10, \\\"suite\\\": \\\"LIBERO-object\\\", \\\"norm\\\": 0.3, \\\"seed\\\": 42}}, \\\"eval-mag-perdof-norm005-object\\\": {\\\"status\\\": \\\"DONE\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-16T08:30:31.627Z\\\", \\\"updated_at\\\": \\\"2026-05-16T08:30:52.155Z\\\", \\\"spec\\\": {\\\"command\\\": \\\"python evaluate.py --mode crm_perdof --benchmark object --max_correction_norm 0.05 --seed 42\\\", \\\"server\\\": \\\"bjb2-28827\\\", \\\"data_path\\\": \\\"/root/acr-vla-conformal-refinement/logs/eval_object_perdof_norm005.json\\\", \\\"data_count\\\": 100, \\\"model_name\\\": \\\"crm_v3_norm_perdof\\\", \\\"seed\\\": 42, \\\"checkpoint_source\\\": \\\"/root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt\\\", \\\"eval_data\\\": \\\"LIBERO object benchmark\\\"}, \\\"conclusion\\\": \\\"negative\\\", \\\"checkpoint_path\\\": \\\"/root/acr-vla-conformal-refinement/logs/eval_object_perdof_norm005.json\\\", \\\"log_path\\\": \\\"/root/acr-vla-conformal-refinement/logs/nohup_eval_object_perdof_norm005.log\\\", \\\"completed_at\\\": \\\"2026-05-16T08:30:50.635Z\\\", \\\"metrics\\\": {\\\"overall_sr\\\": 0.14, \\\"per_task\\\": {\\\"alphabet_soup\\\": 0, \\\"cream_cheese\\\": 0, \\\"salad_dressing\\\": 0.2, \\\"bbq_sauce\\\": 0.4, \\\"ketchup\\\": 0, \\\"tomato_sauce\\\": 0, \\\"butter\\\": 0, \\\"milk\\\": 0.2, \\\"chocolate_pudding\\\": 0.4, \\\"orange_juice\\\": 0.2}}}, \\\"eval-mag-obsonly-norm03-object\\\": {\\\"status\\\": \\\"DONE\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-16T07:41:31.617Z\\\", \\\"updated_at\\\": \\\"2026-05-16T07:41:53.597Z\\\", \\\"metrics\\\": {\\\"tasks_done\\\": 10, \\\"tasks_total\\\": 10, \\\"overall_sr\\\": 0.19, \\\"per_task_sr\\\": {\\\"alphabet_soup\\\": 0, \\\"cream_cheese\\\": 0, \\\"salad_dressing\\\": 0.3, \\\"bbq_sauce\\\": 0.3, \\\"ketchup\\\": 0, \\\"tomato_sauce\\\": 0.1, \\\"butter\\\": 0.2, \\\"milk\\\": 0.2, \\\"chocolate_pudding\\\": 0.5, \\\"orange_juice\\\": 0.3}}, \\\"checkpoint_path\\\": \\\"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\\\", \\\"log_path\\\": \\\"/root/acr-vla-conformal-refinement/logs/eval_object_obs_only_norm03.log\\\", \\\"conclusion\\\": \\\"success\\\", \\\"completed_at\\\": \\\"2026-05-16T07:41:53.597Z\\\"}}, \\\"count\\\": 27, \\\"total\\\": 27, \\\"baseline\\\": null}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.0878}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"experiments\": {\"eval-perdof-object-norm02-seed49\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-20T15:59:12.635Z\", \"updated_at\": \"2026-05-20T15:59:54.757Z\", \"metrics\": {\"overall_success_rate\": 0.12, \"total_rollouts\": 100, \"total_successes\": 12, \"per_task_sr\": {\"alphabet_soup\": 0, \"cream_cheese\": 0, \"salad_dressing\": 0.1, \"bbq_sauce\": 0.2, \"ketchup\": 0, \"tomato_sauce\": 0, \"butter\": 0.1, \"milk\": 0.2, \"chocolate_pudding\": 0.4, \"orange_juice\": 0.2}}, \"log_path\": \"/root/acr-vla-conformal-refinement/logs/eval-perdof-object-norm02-seed49.log\", \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt\", \"spec\": {\"command\": \"python evaluate.py --mode crm_perdof --benchmark object --seed 49 --K 10 --max_correction_norm 0.2 --n_rollouts 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt --output_file logs/eval_perdof_object_norm02_seed49.json\", \"server\": \"bjb1-32546\", \"data_path\": \"LIBERO-Object\", \"data_count\": 100, \"model_name\": \"crm_perdof_norm02_K10\", \"seed\": 49, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt\", \"eval_data\": \"LIBERO-Object\"}, \"hypothesis\": \"PerDoF CRM with norm-clipped corrections (epsilon=0.2, K=10) provides consistent improvement over baseline on LIBERO-Object across seeds; seed49 should yield SR in the 14-18% range consistent with seeds 43-48.\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-20T15:59:54.757Z\"}, \"eval-obs-only-goal-norm02-seed52\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-20T12:05:20.840Z\", \"updated_at\": \"2026-05-20T12:58:35.610Z\", \"spec\": {\"command\": \"python -u src/evaluate.py --mode crm_obs_only --benchmark LIBERO-Goal --seed 52 --n_rollouts 10 --max_correction_norm 0.2\", \"server\": \"bjb1-32546\", \"gpu\": \"cuda:0\", \"pid\": 362579, \"data_path\": \"LIBERO-Goal\", \"data_count\": \"10 tasks x 10 rollouts\", \"model_name\": \"openvla-7b + CRM obs_only\", \"seed\": 52, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\", \"eval_data\": \"LIBERO-Goal (10 tasks x 10 rollouts)\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-obs-only-goal-norm02-seed52.log\", \"checkpoint_path\": \"N/A (eval only)\"}, \"metrics\": {\"success_rate\": 0.68, \"successes\": 68, \"total\": 100, \"per_task_sr\": {\"open_middle_drawer_cabinet\": 0.7, \"put_bowl_on_stove\": 0.9, \"put_wine_bottle_on_cabinet\": 0.4, \"open_top_drawer_put_bowl\": 0.3, \"put_bowl_on_cabinet\": 0.8, \"push_plate_front_stove\": 0.8, \"put_cream_cheese_in_bowl\": 0.4, \"turn_on_stove\": 1, \"put_bowl_on_plate\": 1, \"put_wine_bottle_on_rack\": 0.5}}, \"conclusion\": \"success\", \"hypothesis\": \"CRM obs_only with K=10 and norm cap 0.2 improves SR on LIBERO-Goal by applying observation-conditioned corrections that compensate for VLA action prediction errors, providing a new seed for variance estimation.\", \"completed_at\": \"2026-05-20T12:58:26.417Z\", \"notes\": \"SR=68% on Goal seed52. Strong result; turn_on_stove and put_bowl_on_plate both 100%.\"}, \"eval-argmin-object-seed49\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-20T12:05:22.690Z\", \"updated_at\": \"2026-05-20T12:58:34.569Z\", \"spec\": {\"command\": \"python -u src/evaluate.py --mode reconvla --benchmark LIBERO-Object --seed 49 --n_rollouts 10\", \"server\": \"bjb1-32546\", \"gpu\": \"cuda:5\", \"pid\": 364591, \"data_path\": \"LIBERO-Object\", \"data_count\": \"10 tasks x 10 rollouts\", \"model_name\": \"openvla-7b + CRM obs_only (argmin)\", \"seed\": 49, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\", \"eval_data\": \"LIBERO-Object (10 tasks x 10 rollouts)\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-argmin-object-seed49.log\", \"checkpoint_path\": \"N/A (eval only)\"}, \"metrics\": {\"success_rate\": 0.16, \"successes\": 16, \"total\": 100, \"per_task_sr\": {\"alphabet_soup\": 0, \"cream_cheese\": 0, \"salad_dressing\": 0.2, \"bbq_sauce\": 0.4, \"ketchup\": 0, \"tomato_sauce\": 0.1, \"butter\": 0.1, \"milk\": 0.3, \"chocolate_pudding\": 0.3, \"orange_juice\": 0.2}}, \"conclusion\": \"success\", \"hypothesis\": \"Argmin (reconvla) selection among K=10 CRM refinements improves over single-step VLA on Object by choosing the candidate with lowest predicted residual, providing a multi-seed consistency check.\", \"completed_at\": \"2026-05-20T12:58:25.905Z\", \"notes\": \"SR=16% on Object seed49. Consistent with other argmin seeds on Object benchmark.\"}, \"eval-random-selection-spatial-seed43\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-20T12:05:19.438Z\", \"updated_at\": \"2026-05-20T12:58:33.167Z\", \"spec\": {\"command\": \"python -u src/evaluate.py --mode random_selection --benchmark LIBERO-Spatial --seed 43 --n_rollouts 10\", \"server\": \"bjb1-18228\", \"gpu\": \"cuda:1\", \"pid\": 347075, \"data_path\": \"LIBERO-Spatial\", \"data_count\": \"10 tasks x 10 rollouts\", \"model_name\": \"openvla-7b + CRM obs_only\", \"seed\": 43, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\", \"eval_data\": \"LIBERO-Spatial (10 tasks x 10 rollouts)\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-random-selection-spatial-seed43.log\", \"checkpoint_path\": \"N/A (eval only)\"}, \"metrics\": {\"success_rate\": 0.26, \"successes\": 26, \"total\": 100, \"per_task_sr\": {\"between_plate_ramekin\": 0.7, \"next_to_ramekin\": 0.9, \"table_center\": 0, \"cookie_box\": 0.1, \"top_drawer\": 0, \"on_ramekin\": 0, \"next_to_cookie_box\": 0.7, \"on_stove\": 0, \"next_to_plate\": 0.2, \"on_wooden_cabinet\": 0}}, \"conclusion\": \"success\", \"hypothesis\": \"Random candidate selection from K=10 CRM refinements serves as a lower-bound baseline, showing that informed selection (argmin) is necessary to achieve the full benefit of multi-step refinement on Spatial.\", \"completed_at\": \"2026-05-20T12:58:24.969Z\", \"notes\": \"SR=26% on Spatial seed43. Lower than argmin-based selection, confirming informed selection matters.\"}, \"eval-adaptive-k-spatial-p90-seed43\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-20T10:52:06.660Z\", \"updated_at\": \"2026-05-20T12:58:31.849Z\", \"spec\": {\"command\": \"python -u src/evaluate.py --mode adaptive_k --benchmark LIBERO-Spatial --seed 43 --n_rollouts 10 --adaptive_k_threshold 0.125870 --output_file logs/eval-adaptive-k-spatial-p90-seed43.json\", \"server\": \"bjb1-18228\", \"gpu\": \"cuda:3\", \"pid\": 344852, \"data_path\": \"LIBERO-Spatial\", \"data_count\": \"10 tasks x 10 rollouts\", \"model_name\": \"openvla-7b + CRM obs_only\", \"seed\": 43, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\", \"eval_data\": \"LIBERO-Spatial (10 tasks x 10 rollouts)\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-adaptive-k-spatial-p90-seed43.log\", \"checkpoint_path\": \"N/A (eval only)\"}, \"metrics\": {\"success_rate\": 0.32, \"successes\": 32, \"total\": 100, \"avg_K\": 3.6, \"fast_path_pct\": 80.2, \"mean_l2\": 0.0905, \"per_task_sr\": {\"between_plate_ramekin\": 0.7, \"next_to_ramekin\": 1, \"table_center\": 0.1, \"cookie_box\": 0.3, \"top_drawer\": 0, \"on_ramekin\": 0.1, \"next_to_cookie_box\": 0.8, \"on_stove\": 0, \"next_to_plate\": 0.2, \"on_wooden_cabinet\": 0}}, \"conclusion\": \"success\", \"hypothesis\": \"Adaptive K with P90 threshold (τ=0.1259) reduces average refinement steps while maintaining comparable SR to fixed K=10 on Spatial, because most states have low CRM residuals and can skip full refinement.\", \"completed_at\": \"2026-05-20T12:58:23.572Z\", \"notes\": \"SR=32%, avg_K=3.6 (vs fixed K=10), 80.2% fast-path. Adaptive K saves ~64% compute with seed43 on Spatial.\"}, \"eval-adaptive-k-object-p90-seed44\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-20T12:45:08.564Z\", \"updated_at\": \"2026-05-20T12:45:37.089Z\", \"hypothesis\": \"Adaptive K with τ=P90 (0.125870) on LIBERO-Object seed44. P90 是最宽松的阈值——大部分 step fast-path (K=1)，仅在极高不确定性时用 K=10。验证 P90 在 Object 上的 SR/compute tradeoff。\", \"spec\": {\"command\": \"python -u src/evaluate.py --mode adaptive_k --benchmark LIBERO-Object --seed 44 --n_rollouts 10 --adaptive_k_threshold 0.125870\", \"server\": \"bjb2-28827\", \"data_path\": \"LIBERO-Object\", \"data_count\": \"10 tasks x 10 rollouts\", \"model_name\": \"openvla-7b + CRM obs_only\", \"seed\": 44, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\", \"eval_data\": \"LIBERO-Object (10 tasks x 10 rollouts)\", \"log_path\": \"N/A (discovered by Reviewer)\", \"checkpoint_path\": \"N/A (eval only)\"}, \"metrics\": {\"sr\": 14, \"avg_K\": 2.58, \"fast_path_pct\": 92.8, \"total_rollouts\": 100}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-20T12:45:37.089Z\"}, \"eval-adaptive-k-object-p90-seed43\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-20T12:45:08.312Z\", \"updated_at\": \"2026-05-20T12:45:34.700Z\", \"hypothesis\": \"Adaptive K with τ=P90 (0.125870) on LIBERO-Object seed43. P90 是最宽松的阈值——大部分 step fast-path (K=1)，仅在极高不确定性时用 K=10。验证 P90 在 Object 上的 SR/compute tradeoff。\", \"spec\": {\"command\": \"python -u src/evaluate.py --mode adaptive_k --benchmark LIBERO-Object --seed 43 --n_rollouts 10 --adaptive_k_threshold 0.125870\", \"server\": \"bjb2-28827\", \"data_path\": \"LIBERO-Object\", \"data_count\": \"10 tasks x 10 rollouts\", \"model_name\": \"openvla-7b + CRM obs_only\", \"seed\": 43, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\", \"eval_data\": \"LIBERO-Object (10 tasks x 10 rollouts)\", \"log_path\": \"N/A (discovered by Reviewer)\", \"checkpoint_path\": \"N/A (eval only)\"}, \"metrics\": {\"sr\": 14, \"avg_K\": 2.61, \"fast_path_pct\": 92.3, \"total_rollouts\": 100}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-20T12:45:34.700Z\"}, \"eval-adaptive-k-spatial-p50-seed42\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-20T11:24:12.894Z\", \"updated_at\": \"2026-05-20T11:25:16.991Z\", \"conclusion\": \"success\", \"metrics\": {\"sr\": 30, \"avg_K\": 6.324, \"fast_path_pct\": 45.95, \"mean_l2\": 0.0903, \"total_rollouts\": 100}, \"failure_reason\": \"\", \"completed_at\": \"2026-05-20T11:06:00.000Z\", \"notes\": \"Reviewer 独立验证：JSON 完整，日志确认 SR=30%，PID 自然退出。之前被 cron 误判为 failed（PID dead + 无 sentinel），已修正为 success。\", \"spec\": {\"command\": \"python -u src/evaluate.py --mode adaptive_k --benchmark LIBERO-Spatial --seed 42 --n_rollouts 10 --adaptive_k_threshold 0.074855\", \"server\": \"bjb2-40593\", \"gpu\": \"cuda:0\", \"pid\": 681823, \"data_path\": \"LIBERO-Spatial\", \"data_count\": \"10 tasks x 10 rollouts\", \"model_name\": \"openvla-7b + CRM obs_only\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\", \"eval_data\": \"LIBERO-Spatial (10 tasks x 10 rollouts)\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-adaptive-k-spatial-p50-seed42.log\", \"checkpoint_path\": \"N/A (eval only)\"}, \"hypothesis\": \"Adaptive K with τ=P50 (0.074855, Object-calibrated) on LIBERO-Spatial seed42. 验证 Adaptive K 方法在第二个 benchmark 上的泛化：使用 Object 上校准的阈值直接应用到 Spatial（无 per-benchmark tuning）。如果 SR 接近 CRM K=10 (34.3%) 且 fast_path >50%，则证明方法跨 benchmark 通用。\"}, \"eval-obs-only-object-norm003-seed44\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-20T10:52:14.742Z\", \"updated_at\": \"2026-05-20T10:52:47.202Z\", \"hypothesis\": \"CRM obs_only ε=0.03 on Object seed44. Low-norm multi-seed supplement (plan_500): strengthens Figure 2 error bars at small ε.\", \"spec\": {\"command\": \"evaluate.py --mode crm_obs_only --benchmark object --seed 44 --n_rollouts 10 --K 10 --max_correction_norm 0.03\", \"server\": \"bjb2-28827\", \"seed\": 44, \"model_name\": \"crm_v3_norm/obs_only/crm_best.pt\", \"data_path\": \"LIBERO_object\", \"data_count\": 100}, \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-obs-only-object-norm003-seed44.log\", \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\", \"metrics\": {\"overall_success_rate\": 0.15, \"total_successes\": 15, \"total_rollouts\": 100, \"per_task\": {\"alphabet_soup\": 0, \"cream_cheese\": 0, \"salad_dressing\": 0.3, \"bbq_sauce\": 0.2, \"ketchup\": 0, \"tomato_sauce\": 0.1, \"butter\": 0.1, \"milk\": 0.2, \"chocolate_pudding\": 0.3, \"orange_juice\": 0.3}}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-20T10:52:47.202Z\"}, \"eval-random-selection-object-seed46-r2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-19T17:41:16.541Z\", \"updated_at\": \"2026-05-19T17:41:32.255Z\", \"spec\": {\"command\": \"cd /root/acr-vla-conformal-refinement && timeout 57600 /root/miniconda3/bin/python -u src/evaluate.py --mode random_selection --benchmark object --n_rollouts 10 --seed 46 --K 10 --output_file logs/eval_object_random_selection_seed46.json\", \"server\": \"bjb2-40593\", \"data_path\": \"LIBERO-Object\", \"data_count\": 100, \"model_name\": \"SmolVLA_random_selection\", \"seed\": 46, \"checkpoint_path\": \"N/A-eval-only\", \"log_path\": \"/root/acr-vla-conformal-refinement/logs/eval_object_random_selection_seed46.log\"}, \"hypothesis\": \"Random selection baseline (K=10) on LIBERO-Object seed46 establishes reference success rate for comparing against CRM-guided selection methods\", \"conclusion\": \"killed\", \"completed_at\": \"2026-05-19T17:41:32.255Z\"}, \"eval-obs-only-spatial-norm02-seed47\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-19T17:02:40.986Z\", \"updated_at\": \"2026-05-19T17:03:14.457Z\", \"metrics\": {\"success_rate\": 0.32, \"successes\": 32, \"total\": 100, \"n_tasks\": 10, \"n_rollouts\": 10, \"per_task\": {\"between_plate_and_ramekin\": 0.8, \"next_to_ramekin\": 0.9, \"from_table_center\": 0, \"on_cookie_box\": 0.3, \"in_top_drawer\": 0.1, \"on_ramekin\": 0, \"next_to_cookie_box\": 0.9, \"on_stove\": 0, \"next_to_plate\": 0.2, \"on_wooden_cabinet\": 0}}, \"checkpoint_path\": \"N/A-eval-only\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-obs-only-spatial-norm02-seed47.log\", \"conclusion\": \"success\", \"spec\": {\"command\": \"cd /root/acr-vla-conformal-refinement && /root/miniconda3/bin/python -u src/evaluate.py --mode crm_obs_only --benchmark spatial --n_rollouts 10 --seed 47 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --max_correction_norm 0.2 --output_file logs/eval_spatial_obs_only_norm02_seed47.json\", \"server\": \"bjb1-32546\", \"data_path\": \"LIBERO-Spatial\", \"data_count\": 100, \"model_name\": \"crm_obs_only\", \"seed\": 47}, \"hypothesis\": \"obs_only CRM with epsilon=0.2 and K=10 improves success rate over VLA-only baseline on LIBERO-Spatial because observation-conditioned conformal corrections can detect and fix spatial reasoning errors without requiring action history\", \"completed_at\": \"2026-05-19T17:03:14.457Z\"}, \"eval-vla-only-spatial-seed45\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-19T15:19:50.220Z\", \"updated_at\": \"2026-05-19T15:20:24.563Z\", \"spec\": {\"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-vla-only-spatial-seed45.log\", \"command\": \"python evaluate.py --benchmark spatial --mode vla_only --seed 45\", \"server\": \"bjb1-32546\", \"seed\": 45, \"data_path\": \"LIBERO-Spatial\", \"data_count\": 100, \"model_name\": \"SmolVLA\", \"checkpoint_path\": \"N/A (eval-only)\"}, \"metrics\": {\"success_rate\": 0.27, \"per_task\": {\"between_plate_and_ramekin\": 0.7, \"next_to_ramekin\": 0.9, \"from_table_center\": 0, \"on_cookie_box\": 0.2, \"in_top_drawer\": 0, \"on_ramekin\": 0, \"next_to_cookie_box\": 0.9, \"on_stove\": 0, \"next_to_plate\": 0, \"on_wooden_cabinet\": 0}, \"successes\": 27, \"total\": 100}, \"conclusion\": \"success\", \"hypothesis\": \"VLA-only baseline on LIBERO-Spatial with seed 45 establishes reference success rate for comparison with CRM-augmented methods\", \"completed_at\": \"2026-05-19T15:20:24.563Z\"}, \"eval-obs-only-spatial-norm02-seed44\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-19T14:23:33.161Z\", \"updated_at\": \"2026-05-19T14:26:44.810Z\", \"metrics\": {\"success_rate\": 0.36, \"successes\": 36, \"total\": 100}, \"checkpoint_path\": \"N/A (eval only)\", \"log_path\": \"/root/acr-vla-conformal-refinement/logs/eval_spatial_obs_only_norm02_seed44.json\", \"conclusion\": \"success\", \"spec\": {\"command\": \"python eval_crm.py --mode crm_obs_only --benchmark spatial --K 10 --seed 44 --max_correction_norm 0.2\", \"server\": \"bjb2-28827\", \"data_path\": \"spatial_benchmark\", \"data_count\": 100, \"model_name\": \"crm_obs_only\", \"seed\": 44}, \"hypothesis\": \"CRM obs-only mode with max_correction_norm=0.2 can improve spatial benchmark success rate by refining VLA actions using only observation-based conformal prediction, without access to privileged state information.\", \"completed_at\": \"2026-05-19T14:24:10.857Z\"}, \"eval-obs-only-object-norm003-seed43-r2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-19T05:14:10.523Z\", \"updated_at\": \"2026-05-19T05:14:25.385Z\", \"conclusion\": \"failed\", \"spec\": {\"checkpoint_path\": \"N/A (eval-only)\", \"log_path\": \"/root/acr-vla-conformal-refinement/logs/eval_object_obs_only_norm003_seed43.log\", \"metrics\": {\"success_rate\": null, \"tasks_completed\": \"1/10\", \"failure_reason\": \"process terminated prematurely after 1 task\"}}, \"completed_at\": \"2026-05-19T05:14:25.385Z\"}, \"eval-obs-only-object-norm03-seed48\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-18T13:26:49.122Z\", \"updated_at\": \"2026-05-18T13:27:19.389Z\", \"metrics\": {\"overall_success_rate\": 0.16, \"per_task\": {\"pick_up_the_alphabet_soup_and_place_it_in_the_basket\": 0, \"pick_up_the_cream_cheese_and_place_it_in_the_basket\": 0, \"pick_up_the_salad_dressing_and_place_it_in_the_basket\": 0.3, \"pick_up_the_bbq_sauce_and_place_it_in_the_basket\": 0.4, \"pick_up_the_ketchup_and_place_it_in_the_basket\": 0, \"pick_up_the_tomato_sauce_and_place_it_in_the_basket\": 0.1, \"pick_up_the_butter_and_place_it_in_the_basket\": 0.1, \"pick_up_the_milk_and_place_it_in_the_basket\": 0.1, \"pick_up_the_chocolate_pudding_and_place_it_in_the_basket\": 0.4, \"pick_up_the_orange_juice_and_place_it_in_the_basket\": 0.2}}, \"log_path\": \"/root/acr-vla-conformal-refinement/logs/eval_object_obs_only_norm03_seed48.json\", \"checkpoint_path\": \"N/A (eval only)\", \"conclusion\": \"success\", \"spec\": {\"command\": \"eval obs_only CRM epsilon=0.3 seed48 on LIBERO-Object K=10 n_rollouts=10\", \"server\": \"bjb1-18228\", \"data_path\": \"LIBERO-Object\", \"data_count\": 100, \"model_name\": \"openvla\", \"seed\": 48}, \"hypothesis\": \"CRM with obs_only mode and epsilon=0.3 normalization threshold will improve success rate on LIBERO-Object by filtering unreliable action predictions based solely on observation conformity scores\", \"completed_at\": \"2026-05-18T13:27:19.389Z\"}, \"eval-obs-only-object-norm01-seed48\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-18T11:42:37.233Z\", \"updated_at\": \"2026-05-18T11:43:15.403Z\", \"hypothesis\": \"obs_only CRM with max_correction_norm=0.1 on LIBERO-Object seed48. Tests whether obs_only mode with conservative norm clipping maintains performance across seeds.\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=1 /root/miniconda3/bin/python -u src/evaluate.py --mode crm_obs_only --benchmark object --n_rollouts 10 --seed 48 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --max_correction_norm 0.1 --output_file logs/eval_object_obs_only_norm01_seed48.json\", \"server\": \"bjb1-18228\", \"data_path\": \"LIBERO-Object\", \"data_count\": 100, \"model_name\": \"SmolVLA+CRM_obs_only\", \"seed\": 48, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\", \"eval_data\": \"LIBERO-Object\"}, \"log_path\": \"/root/acr-vla-conformal-refinement/logs/eval_object_obs_only_norm01_seed48.json\", \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.18, \"n_tasks\": 10, \"n_rollouts\": 10, \"per_task\": {\"alphabet_soup\": 0, \"cream_cheese\": 0, \"salad_dressing\": 0, \"bbq_sauce\": 0.4, \"ketchup\": 0.1, \"tomato_sauce\": 0.2, \"butter\": 0.2, \"milk\": 0.3, \"chocolate_pudding\": 0.3, \"orange_juice\": 0.3}}, \"completed_at\": \"2026-05-18T11:43:15.403Z\"}, \"eval-obs-only-object-norm02-k5-seed42\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-18T03:44:47.522Z\", \"updated_at\": \"2026-05-18T03:45:04.655Z\", \"conclusion\": \"success\", \"metrics\": {\"overall_sr\": 0.14, \"successes\": 14, \"rollouts\": 100, \"tasks\": 10, \"suite\": \"LIBERO-object\", \"seed\": 42, \"method\": \"crm_obs_only\", \"K\": 5, \"max_correction_norm\": 0.2}, \"hypothesis\": \"obs_only CRM with K=5 candidates and ε=0.2 on LIBERO-Object seed42. Tests whether fewer candidates (K=5 vs K=10) reduces selection quality. K=5 SR=14% vs K=10 SR=17.5% confirms monotonic improvement with more candidates.\", \"spec\": {\"command\": \"python -u src/evaluate.py --mode crm_obs_only --benchmark object --n_rollouts 10 --seed 42 --K 5 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --max_correction_norm 0.2 --output_file logs/eval_object_obs_only_norm02_k5_seed42.json\", \"server\": \"bjb1-18228\", \"data_path\": \"LIBERO-Object\", \"data_count\": 100, \"model_name\": \"SmolVLA+CRM_obs_only\", \"seed\": 42, \"K\": 5, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\", \"eval_data\": \"LIBERO-Object\", \"checkpoint_path\": \"N/A\", \"log_path\": \"/root/acr-vla-conformal-refinement/logs/eval_object_obs_only_norm02_k5_seed42.json\"}, \"completed_at\": \"2026-05-18T03:45:04.655Z\"}, \"eval-perdof-object-norm01-seed46\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-18T03:05:55.543Z\", \"updated_at\": \"2026-05-18T03:06:14.048Z\", \"hypothesis\": \"perdof CRM with ε=0.1 on LIBERO-Object seed46. Magnitude curve data point for perdof at intermediate norm. SR=10% confirms perdof degrades from peak at low norms.\", \"metrics\": {\"overall_sr\": 0.1, \"successes\": 10, \"rollouts\": 100, \"tasks\": 10, \"suite\": \"LIBERO-object\", \"seed\": 46, \"method\": \"crm_perdof\", \"max_correction_norm\": 0.1}, \"conclusion\": \"success\", \"spec\": {\"command\": \"python -u src/evaluate.py --mode crm_perdof --benchmark object --n_rollouts 10 --seed 46 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt --max_correction_norm 0.1 --output_file logs/eval_object_perdof_norm01_seed46.json\", \"server\": \"bjb1-32546\", \"data_path\": \"LIBERO-Object\", \"data_count\": 100, \"model_name\": \"SmolVLA+CRM_perdof\", \"seed\": 46, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt\", \"eval_data\": \"LIBERO-Object\", \"checkpoint_path\": \"N/A\", \"log_path\": \"/root/acr-vla-conformal-refinement/logs/eval_object_perdof_norm01_seed46.json\"}, \"completed_at\": \"2026-05-18T03:06:14.049Z\"}, \"eval-perdof-object-default-seed46\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-18T03:05:29.784Z\", \"updated_at\": \"2026-05-18T03:06:03.735Z\", \"conclusion\": \"negative\", \"hypothesis\": \"perdof CRM without norm constraint (uncapped correction magnitude) on LIBERO-Object seed46. Tests whether perdof maintains performance without explicit correction capping. SR=0% confirms perdof corrections are catastrophically unstable without norm constraints.\", \"spec\": {\"command\": \"python -u src/evaluate.py --mode crm_perdof --benchmark object --n_rollouts 10 --seed 46 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt --output_file logs/eval_object_perdof_default_seed46.json\", \"server\": \"bjb1-32546\", \"data_path\": \"LIBERO-Object\", \"data_count\": 100, \"model_name\": \"SmolVLA+CRM_perdof\", \"seed\": 46, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt\", \"eval_data\": \"LIBERO-Object\", \"checkpoint_path\": \"N/A\", \"log_path\": \"/root/acr-vla-conformal-refinement/logs/eval_object_perdof_default_seed46.json\"}, \"metrics\": {\"overall_sr\": 0, \"successes\": 0, \"rollouts\": 100, \"tasks\": 10, \"suite\": \"LIBERO-object\", \"seed\": 46, \"method\": \"crm_perdof\", \"max_correction_norm\": \"default\"}, \"completed_at\": \"2026-05-18T03:06:03.735Z\"}, \"eval-obs-only-object-default-seed46\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-18T00:59:50.348Z\", \"updated_at\": \"2026-05-18T01:00:23.165Z\", \"conclusion\": \"success\", \"metrics\": {\"overall_sr\": 0.15, \"successes\": 15, \"rollouts\": 100, \"tasks\": 10, \"suite\": \"LIBERO-object\", \"seed\": 46, \"method\": \"crm_obs_only\", \"max_correction_norm\": \"default\", \"per_task_sr\": {\"alphabet_soup\": 0, \"cream_cheese\": 0, \"salad_dressing\": 0.2, \"bbq_sauce\": 0.4, \"ketchup\": 0.1, \"tomato_sauce\": 0.1, \"butter\": 0.1, \"milk\": 0.1, \"chocolate_pudding\": 0.2, \"orange_juice\": 0.3}}, \"spec\": {\"checkpoint_path\": \"N/A\", \"log_path\": \"/root/acr-vla-conformal-refinement/logs/eval_object_obs_only_default_seed46.json\", \"command\": \"python -u src/evaluate.py --mode crm_obs_only --benchmark object --n_rollouts 10 --seed 46 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --output_file logs/eval_object_obs_only_default_seed46.json\", \"server\": \"bjb1-32546\", \"data_path\": \"LIBERO-Object\", \"data_count\": 100, \"model_name\": \"SmolVLA+CRM_obs_only\", \"seed\": 46, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\", \"eval_data\": \"LIBERO-Object\"}, \"hypothesis\": \"obs_only CRM without norm constraint (uncapped correction magnitude) on LIBERO-Object seed46. Tests whether obs_only maintains performance without explicit correction capping. If uncapped performs worse than capped, it confirms that moderate norm constraints stabilize corrections.\", \"completed_at\": \"2026-05-18T01:00:23.165Z\"}, \"eval-obs-only-object-norm01-seed46\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-18T00:42:56.715Z\", \"updated_at\": \"2026-05-18T00:43:09.191Z\", \"conclusion\": \"killed\", \"completed_at\": \"2026-05-18T00:43:09.191Z\"}, \"eval-k1-crm-multiscale-object-seed43\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-17T21:05:23.402Z\", \"updated_at\": \"2026-05-17T21:06:09.004Z\", \"hypothesis\": \"Multi-scale K=1 CRM with accumulated gradient refinement improves object manipulation success rate over baseline by providing conformal prediction-based action corrections at multiple spatial scales\", \"spec\": {\"command\": \"python -u src/evaluate.py --mode crm_k1_accg --benchmark object --n_rollouts 10 --seed 43\", \"server\": \"bjb1-32546\", \"data_path\": \"LIBERO-Object\", \"data_count\": 100, \"model_name\": \"SmolVLA+CRM_k1_accg\", \"seed\": 43, \"checkpoint_source\": \"crm_v3_norm\", \"eval_data\": \"LIBERO-Object\", \"checkpoint_path\": \"N/A\", \"log_path\": \"/root/acr-vla-conformal-refinement/logs/eval_k1_crm_multiscale_object_seed43.json\"}, \"conclusion\": \"negative\", \"metrics\": {\"overall_sr\": 0.09, \"successes\": 9, \"rollouts\": 100, \"tasks\": 10, \"suite\": \"LIBERO-object\", \"seed\": 43, \"method\": \"crm_k1_accg\", \"per_task\": {\"alphabet_soup\": 0, \"cream_cheese\": 0, \"salad_dressing\": 0.1, \"bbq_sauce\": 0.2, \"ketchup\": 0, \"tomato_sauce\": 0.2, \"butter\": 0, \"milk\": 0, \"chocolate_pudding\": 0.2, \"orange_juice\": 0.2}}, \"completed_at\": \"2026-05-17T21:06:09.004Z\"}, \"eval-k1-crm-multiscale-object-seed42\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-17T21:05:22.835Z\", \"updated_at\": \"2026-05-17T21:06:08.318Z\", \"hypothesis\": \"Multi-scale K=1 CRM with accumulated gradient refinement improves object manipulation success rate over baseline by providing conformal prediction-based action corrections at multiple spatial scales\", \"spec\": {\"command\": \"python -u src/evaluate.py --mode crm_k1_accg --benchmark object --n_rollouts 10 --seed 42\", \"server\": \"bjb2-28827\", \"data_path\": \"LIBERO-Object\", \"data_count\": 100, \"model_name\": \"SmolVLA+CRM_k1_accg\", \"seed\": 42, \"checkpoint_source\": \"crm_v3_norm\", \"eval_data\": \"LIBERO-Object\", \"checkpoint_path\": \"N/A\", \"log_path\": \"/root/acr-vla-conformal-refinement/logs/eval_k1_crm_multiscale_object_seed42.json\"}, \"conclusion\": \"negative\", \"metrics\": {\"overall_sr\": 0.12, \"successes\": 12, \"rollouts\": 100, \"tasks\": 10, \"suite\": \"LIBERO-object\", \"seed\": 42, \"method\": \"crm_k1_accg\", \"per_task\": {\"alphabet_soup\": 0, \"cream_cheese\": 0, \"salad_dressing\": 0.1, \"bbq_sauce\": 0.2, \"ketchup\": 0, \"tomato_sauce\": 0.3, \"butter\": 0.1, \"milk\": 0, \"chocolate_pudding\": 0.3, \"orange_juice\": 0.2}}, \"completed_at\": \"2026-05-17T21:06:08.318Z\"}, \"eval-k1-crm-multiscale-object-seed44-r2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-17T20:55:44.755Z\", \"updated_at\": \"2026-05-17T20:56:16.602Z\", \"hypothesis\": \"Multi-scale K=1 CRM with accumulated gradient refinement improves object manipulation success rate over baseline by providing conformal prediction-based action corrections at multiple spatial scales\", \"spec\": {\"command\": \"python eval_libero.py --method crm_k1_accg --baseline_mode single --suite object --seed 44 --n_rollouts 10\", \"server\": \"bjb1-18228\", \"data_path\": \"LIBERO-object\", \"data_count\": 100, \"model_name\": \"crm_k1_multiscale\", \"seed\": 44, \"checkpoint_source\": \"crm-k1-train\", \"eval_data\": \"LIBERO-object\"}, \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/crm_k1/crm_k1_best.pt\", \"log_path\": \"/root/acr-vla-conformal-refinement/logs/eval_k1_crm_multiscale_object_seed44_bjb1-18228.json\", \"conclusion\": \"negative\", \"completed_at\": \"2026-05-17T20:56:12.165Z\", \"metrics\": {\"overall_sr\": 0.1, \"successes\": 10, \"rollouts\": 100, \"tasks\": 10, \"suite\": \"LIBERO-object\", \"seed\": 44, \"method\": \"crm_k1_accg\", \"per_task\": {\"alphabet_soup\": 0, \"cream_cheese\": 0, \"salad_dressing\": 0.2, \"bbq_sauce\": 0.1, \"ketchup\": 0, \"tomato_sauce\": 0.1, \"butter\": 0, \"milk\": 0, \"chocolate_pudding\": 0.4, \"orange_juice\": 0.2}}}, \"eval-mag-perdof-norm03-object-r3\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-16T11:05:32.773Z\", \"updated_at\": \"2026-05-16T11:06:06.108Z\", \"conclusion\": \"success\", \"spec\": {\"command\": \"python eval_libero.py --method crm_perdof --suite object --norm 0.3 --seed 42\", \"server\": \"bjb2-28827\", \"data_path\": \"LIBERO-object\", \"data_count\": 100, \"model_name\": \"crm_perdof_norm03\", \"seed\": 42, \"checkpoint_source\": \"crm-train-v3-perdof\", \"eval_data\": \"LIBERO-object\"}, \"log_path\": \"/root/acr-vla-conformal-refinement/logs/eval_object_perdof_norm03_r3.json\", \"checkpoint_path\": \"N/A\", \"completed_at\": \"2026-05-16T11:06:02.462Z\", \"metrics\": {\"success_rate\": 0.04, \"successes\": 4, \"rollouts\": 100, \"tasks\": 10, \"suite\": \"LIBERO-object\", \"norm\": 0.3, \"seed\": 42}}, \"eval-mag-perdof-norm005-object\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-16T08:30:31.627Z\", \"updated_at\": \"2026-05-16T08:30:52.155Z\", \"spec\": {\"command\": \"python evaluate.py --mode crm_perdof --benchmark object --max_correction_norm 0.05 --seed 42\", \"server\": \"bjb2-28827\", \"data_path\": \"/root/acr-vla-conformal-refinement/logs/eval_object_perdof_norm005.json\", \"data_count\": 100, \"model_name\": \"crm_v3_norm_perdof\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt\", \"eval_data\": \"LIBERO object benchmark\"}, \"conclusion\": \"negative\", \"checkpoint_path\": \"/root/acr-vla-conformal-refinement/logs/eval_object_perdof_norm005.json\", \"log_path\": \"/root/acr-vla-conformal-refinement/logs/nohup_eval_object_perdof_norm005.log\", \"completed_at\": \"2026-05-16T08:30:50.635Z\", \"metrics\": {\"overall_sr\": 0.14, \"per_task\": {\"alphabet_soup\": 0, \"cream_cheese\": 0, \"salad_dressing\": 0.2, \"bbq_sauce\": 0.4, \"ketchup\": 0, \"tomato_sauce\": 0, \"butter\": 0, \"milk\": 0.2, \"chocolate_pudding\": 0.4, \"orange_juice\": 0.2}}}, \"eval-mag-obsonly-norm03-object\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-16T07:41:31.617Z\", \"updated_at\": \"2026-05-16T07:41:53.597Z\", \"metrics\": {\"tasks_done\": 10, \"tasks_total\": 10, \"overall_sr\": 0.19, \"per_task_sr\": {\"alphabet_soup\": 0, \"cream_cheese\": 0, \"salad_dressing\": 0.3, \"bbq_sauce\": 0.3, \"ketchup\": 0, \"tomato_sauce\": 0.1, \"butter\": 0.2, \"milk\": 0.2, \"chocolate_pudding\": 0.5, \"orange_juice\": 0.3}}, \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\", \"log_path\": \"/root/acr-vla-conformal-refinement/logs/eval_object_obs_only_norm03.log\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-16T07:41:53.597Z\"}}, \"count\": 27, \"total\": 27, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.0878}}"
    }
  }
}
```

</details>

---

### Tool call

_source line 9_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01CFE7pqmt75ikm26V2rZAgb`</summary>

```json
{
  "project": "acr-vla-conformal-refinement",
  "file": "ROADMAP.md",
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
  "session_id": "e17f41b1-3dce-49fb-a9e5-f5dd86423ed8",
  "uuid": "440f9ecf-f85a-4b39-b090-4c16728f8c47",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UYT61WRkH9xGUXFnM24J9y",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1083,
      "cache_read_input_tokens": 23380,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1083
      },
      "output_tokens": 53,
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

_source line 10 · 2026-05-21T03:22:11.788Z_

<details><summary>↩ Tool result · `toolu_01CFE7pqmt75ikm26V2rZAgb`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/ROADMAP.md\", \"content\": \"# acr-vla-conformal-refinement — Research Dashboard\\n\\n> 最后更新: 2026-05-21 00:48 UTC | 更新原因: D092-D095 updates: Plan A LOCKED, OpenVLA CRM CLOSED, π0.5/π added, GPU state corrected\\n\\n> 详见 paper_framing.md（D077: Adaptive K 核心, D088→D090→D092: Plan A GO）\\n\\n## 核心方向\\n**Adaptive inference-time compute for frozen VLAs** — K=2 L2 distance 作为不确定性信号，自适应决定推理策略（直出 vs CRM correction）。CRM correction>selection 分析作为支撑。\\n\\n## 投稿目标\\n**CoRL 2026** DDL **2026-05-29**。剩余 **8 天**。\\n\\n## 方法路径（D088→D092 最终）\\n- ❌ B (Learned Uncertainty Head): NO-GO, mean 12.0% < VLA-only (D090)\\n- ✅ **A (Plan A: K=2 Conformal + Selective CRM)**: Object 18.3%±2.1%, Spatial 35.0%±1.0% — **GO (D092/D094)**\\n- ⏳ C (Action Distribution Geometry): 不再需要，Plan A 已成功\\n\\n## Plan A 核心结果\\n| Benchmark | Plan A (K=2) | K=10 CRM | Δ vs K=10 | Compute |\\n|-----------|-------------|----------|-----------|---------|\\n| Object    | 18.3%±2.1%  | 16.8%    | +1.5pp    | 80% less (K=2 vs K=10) |\\n| Spatial   | 35.0%±1.0%  | 34.5%    | +0.5pp    | 80% less |\\n\\nPipeline: K=2 batched forward → d₂=‖a₁-a₂‖₂ → if d₂>τ: argmin-to-centroid + CRM; if d₂≤τ: direct output。\\n⚠️ Threshold calibration: flatten-L2 (30D) vs per-step-mean-L2 (7D×5) 差异 ~2.77×，当前 τ 在 Plan A scale 上 trigger rate 84%。待决：强调 K=2 效率 vs recalibrate Pareto sweep。\\n\\n## OpenVLA 实验线\\n- ✅ plan_801: OpenVLA v2 baseline SR=69%\\n- ✅ plan_802 train: CRM 训练完成 (val_loss=0.077260)\\n- ❌ **D093: OpenVLA CRM eval 0%** — near-deterministic (T=0.5, 8/10 identical actions)，applicability boundary，CLOSED\\n\\n## π0.5/π 实验线（D095，用户硬要求）\\n- 🔄 Phase 1: WebSearch + 下载模型（Agent 队列中）\\n- ⏳ Phase 2: env setup + baseline eval\\n- ⏳ Phase 3: 检查 action diversity → if stochastic: CRM pipeline\\n- 目的：第二/三个 VLA backbone（flow-matching），解决 M1 (narrow scope) + R2-W1-new (low absolute perf)\\n\\n## Norm Sweep 状态（plan_200/500）\\n| ε    | n seeds | mean SR | 状态 |\\n|------|---------|---------|------|\\n| 0.03 | ~6      | 15.5%   | seeds running |\\n| 0.05 | ~9      | 13.8%   | seeds running |\\n| 0.1  | ~8      | 15.0%   | seeds running |\\n| 0.2  | 12      | 17.2%   | LOCKED (7-seed core + extras) |\\n\\n## 核心实验结果\\n| Evidence | 结果 | 状态 |\\n|----------|------|------|\\n| **Plan A Object (D092)** | 18.3%±2.1% (K=2, seeds 19/16/20%) | LOCKED |\\n| **Plan A Spatial (D094)** | 35.0%±1.0% (K=2, seeds 34/35/36%) | LOCKED |\\n| Object CRM K=10 (norm02) | 16.8%±1.8% (n=7) | LOCKED |\\n| K=10 decomposition | correction +5.8pp, selection ≈0 | LOCKED |\\n| Random Selection | Object 9.7% (n=6) ≈ VLA-only | LOCKED |\\n| K-sweep | K=5 15.5%, K=10 16.8%, K=20 18.7% | LOCKED |\\n| Adaptive K P50 | 15.3% (avg_K=3.8, ~91% of K=10) | LOCKED |\\n| Spatial CRM K=10 | 34.5%±1.5% (n=9) | LOCKED |\\n| OpenVLA baseline | SR=69% | LOCKED |\\n| OpenVLA CRM (D093) | 0% — applicability boundary | CLOSED |\\n\\n## GPU 状态\\n17 GPU across 4 servers。Live check: bjb1-32546 3-4 张活跃（11.5GB/卡），bjb2-28827 5 张有模型加载（5.7GB/卡），bjb1-18228 部分活跃。Registry \\\"空闲\\\" 报告滞后于实际 GPU 进程。\\n\\n## 近期任务\\n- [ ] **P0** π0.5/π 模型调研 + baseline eval（D095，用户要求）\\n- [ ] **P0** Plan A 结果写入论文（Paper Agent 待指令）\\n- [ ] **P1** paper_framing.md 修正：ε=0.05 = 13.8%（非 14.3%）\\n- [ ] **P1** Threshold calibration 决策（用户未选）\\n- [ ] **P1** Norm sweep 补种完成 + Figure 2 生成\\n- [ ] **P2** review_issues 更新（C3/M1/M3/M6/R2-W1-new）\\n- [ ] **P2** Cron misfire 系统性修复\\n\\n## 关键决策日志\\n\\n| ID | 日期 | 摘要 | 关联实验 |\\n|----|------|------|----------|\\n| D096 | 2026-05-21 | D096: π0.5 适配 GO — baseline >60%, 7D action, flow- | eval-openvla-crm-object-seed42, eval-plan-a-object-seed42 |\\n| D095 | 2026-05-21 | D095: 新增 π0.5/π VLA baseline + CRM 实验线（用户要求）— flow | eval-openvla-crm-object-seed42 |\\n| D094 | 2026-05-21 | D094: Plan A Spatial 完成 — 35.0%±1.0% (K=2) 超过 K=10 | eval-plan-a-spatial-seed42, eval-plan-a-spatial-seed43, eval-plan-a-spatial-seed44 |\\n| D093 | 2026-05-20 | D093: OpenVLA CRM eval 0% — applicability boundary | eval-openvla-crm-object-seed42, eval-openvla-object-vla-only-seed42-v2 |\\n| D092 | 2026-05-20 | D092: Plan A (K=2 conformal + selective CRM) GO —  | eval-plan-a-object-seed42, eval-plan-a-object-seed43, eval-plan-a-object-seed44 |\\n| D091 | 2026-05-20 | D091: D090 narrative 影响评估——核心 claims 不受影响，D088 作为  | eval-adaptive-unc-head-object-seed42, eval-adaptive-k-p50-seed42 |\\n| D090 | 2026-05-20 | D090: D088 Learned Uncertainty Head NO-GO — 3 seed | eval-adaptive-unc-head-object-seed42, eval-adaptive-unc-head-object-seed43, eval-adaptive-unc-head-object-seed44 |\\n| D089 | 2026-05-20 | D089: Round 2 审稿 Holistic Pass — 3 个 SYSTEMIC_ISSU | eval-openvla-object-vla-only-seed42-v2 |\\n| D088 | 2026-05-20 | D088: 方法升级——Learned Uncertainty Head + Selective C | k2-l2-calibration-phase1 |\\n| D087 | 2026-05-20 | D087: 撤回 D086，恢复 OpenVLA 实验线（v2 baseline SR=69%，直接 | eval-openvla-object-vla-only-seed42-v2 |\\n\\n\", \"total_chars\": 4631, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "e17f41b1-3dce-49fb-a9e5-f5dd86423ed8",
  "uuid": "eeda2a22-6bd1-4c90-b553-b630dedcb513",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"path\\\": \\\"/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/ROADMAP.md\\\", \\\"content\\\": \\\"# acr-vla-conformal-refinement — Research Dashboard\\\\n\\\\n> 最后更新: 2026-05-21 00:48 UTC | 更新原因: D092-D095 updates: Plan A LOCKED, OpenVLA CRM CLOSED, π0.5/π added, GPU state corrected\\\\n\\\\n> 详见 paper_framing.md（D077: Adaptive K 核心, D088→D090→D092: Plan A GO）\\\\n\\\\n## 核心方向\\\\n**Adaptive inference-time compute for frozen VLAs** — K=2 L2 distance 作为不确定性信号，自适应决定推理策略（直出 vs CRM correction）。CRM correction>selection 分析作为支撑。\\\\n\\\\n## 投稿目标\\\\n**CoRL 2026** DDL **2026-05-29**。剩余 **8 天**。\\\\n\\\\n## 方法路径（D088→D092 最终）\\\\n- ❌ B (Learned Uncertainty Head): NO-GO, mean 12.0% < VLA-only (D090)\\\\n- ✅ **A (Plan A: K=2 Conformal + Selective CRM)**: Object 18.3%±2.1%, Spatial 35.0%±1.0% — **GO (D092/D094)**\\\\n- ⏳ C (Action Distribution Geometry): 不再需要，Plan A 已成功\\\\n\\\\n## Plan A 核心结果\\\\n| Benchmark | Plan A (K=2) | K=10 CRM | Δ vs K=10 | Compute |\\\\n|-----------|-------------|----------|-----------|---------|\\\\n| Object    | 18.3%±2.1%  | 16.8%    | +1.5pp    | 80% less (K=2 vs K=10) |\\\\n| Spatial   | 35.0%±1.0%  | 34.5%    | +0.5pp    | 80% less |\\\\n\\\\nPipeline: K=2 batched forward → d₂=‖a₁-a₂‖₂ → if d₂>τ: argmin-to-centroid + CRM; if d₂≤τ: direct output。\\\\n⚠️ Threshold calibration: flatten-L2 (30D) vs per-step-mean-L2 (7D×5) 差异 ~2.77×，当前 τ 在 Plan A scale 上 trigger rate 84%。待决：强调 K=2 效率 vs recalibrate Pareto sweep。\\\\n\\\\n## OpenVLA 实验线\\\\n- ✅ plan_801: OpenVLA v2 baseline SR=69%\\\\n- ✅ plan_802 train: CRM 训练完成 (val_loss=0.077260)\\\\n- ❌ **D093: OpenVLA CRM eval 0%** — near-deterministic (T=0.5, 8/10 identical actions)，applicability boundary，CLOSED\\\\n\\\\n## π0.5/π 实验线（D095，用户硬要求）\\\\n- 🔄 Phase 1: WebSearch + 下载模型（Agent 队列中）\\\\n- ⏳ Phase 2: env setup + baseline eval\\\\n- ⏳ Phase 3: 检查 action diversity → if stochastic: CRM pipeline\\\\n- 目的：第二/三个 VLA backbone（flow-matching），解决 M1 (narrow scope) + R2-W1-new (low absolute perf)\\\\n\\\\n## Norm Sweep 状态（plan_200/500）\\\\n| ε    | n seeds | mean SR | 状态 |\\\\n|------|---------|---------|------|\\\\n| 0.03 | ~6      | 15.5%   | seeds running |\\\\n| 0.05 | ~9      | 13.8%   | seeds running |\\\\n| 0.1  | ~8      | 15.0%   | seeds running |\\\\n| 0.2  | 12      | 17.2%   | LOCKED (7-seed core + extras) |\\\\n\\\\n## 核心实验结果\\\\n| Evidence | 结果 | 状态 |\\\\n|----------|------|------|\\\\n| **Plan A Object (D092)** | 18.3%±2.1% (K=2, seeds 19/16/20%) | LOCKED |\\\\n| **Plan A Spatial (D094)** | 35.0%±1.0% (K=2, seeds 34/35/36%) | LOCKED |\\\\n| Object CRM K=10 (norm02) | 16.8%±1.8% (n=7) | LOCKED |\\\\n| K=10 decomposition | correction +5.8pp, selection ≈0 | LOCKED |\\\\n| Random Selection | Object 9.7% (n=6) ≈ VLA-only | LOCKED |\\\\n| K-sweep | K=5 15.5%, K=10 16.8%, K=20 18.7% | LOCKED |\\\\n| Adaptive K P50 | 15.3% (avg_K=3.8, ~91% of K=10) | LOCKED |\\\\n| Spatial CRM K=10 | 34.5%±1.5% (n=9) | LOCKED |\\\\n| OpenVLA baseline | SR=69% | LOCKED |\\\\n| OpenVLA CRM (D093) | 0% — applicability boundary | CLOSED |\\\\n\\\\n## GPU 状态\\\\n17 GPU across 4 servers。Live check: bjb1-32546 3-4 张活跃（11.5GB/卡），bjb2-28827 5 张有模型加载（5.7GB/卡），bjb1-18228 部分活跃。Registry \\\\\\\"空闲\\\\\\\" 报告滞后于实际 GPU 进程。\\\\n\\\\n## 近期任务\\\\n- [ ] **P0** π0.5/π 模型调研 + baseline eval（D095，用户要求）\\\\n- [ ] **P0** Plan A 结果写入论文（Paper Agent 待指令）\\\\n- [ ] **P1** paper_framing.md 修正：ε=0.05 = 13.8%（非 14.3%）\\\\n- [ ] **P1** Threshold calibration 决策（用户未选）\\\\n- [ ] **P1** Norm sweep 补种完成 + Figure 2 生成\\\\n- [ ] **P2** review_issues 更新（C3/M1/M3/M6/R2-W1-new）\\\\n- [ ] **P2** Cron misfire 系统性修复\\\\n\\\\n## 关键决策日志\\\\n\\\\n| ID | 日期 | 摘要 | 关联实验 |\\\\n|----|------|------|----------|\\\\n| D096 | 2026-05-21 | D096: π0.5 适配 GO — baseline >60%, 7D action, flow- | eval-openvla-crm-object-seed42, eval-plan-a-object-seed42 |\\\\n| D095 | 2026-05-21 | D095: 新增 π0.5/π VLA baseline + CRM 实验线（用户要求）— flow | eval-openvla-crm-object-seed42 |\\\\n| D094 | 2026-05-21 | D094: Plan A Spatial 完成 — 35.0%±1.0% (K=2) 超过 K=10 | eval-plan-a-spatial-seed42, eval-plan-a-spatial-seed43, eval-plan-a-spatial-seed44 |\\\\n| D093 | 2026-05-20 | D093: OpenVLA CRM eval 0% — applicability boundary | eval-openvla-crm-object-seed42, eval-openvla-object-vla-only-seed42-v2 |\\\\n| D092 | 2026-05-20 | D092: Plan A (K=2 conformal + selective CRM) GO —  | eval-plan-a-object-seed42, eval-plan-a-object-seed43, eval-plan-a-object-seed44 |\\\\n| D091 | 2026-05-20 | D091: D090 narrative 影响评估——核心 claims 不受影响，D088 作为  | eval-adaptive-unc-head-object-seed42, eval-adaptive-k-p50-seed42 |\\\\n| D090 | 2026-05-20 | D090: D088 Learned Uncertainty Head NO-GO — 3 seed | eval-adaptive-unc-head-object-seed42, eval-adaptive-unc-head-object-seed43, eval-adaptive-unc-head-object-seed44 |\\\\n| D089 | 2026-05-20 | D089: Round 2 审稿 Holistic Pass — 3 个 SYSTEMIC_ISSU | eval-openvla-object-vla-only-seed42-v2 |\\\\n| D088 | 2026-05-20 | D088: 方法升级——Learned Uncertainty Head + Selective C | k2-l2-calibration-phase1 |\\\\n| D087 | 2026-05-20 | D087: 撤回 D086，恢复 OpenVLA 实验线（v2 baseline SR=69%，直接 | eval-openvla-object-vla-only-seed42-v2 |\\\\n\\\\n\\\", \\\"total_chars\\\": 4631, \\\"truncated\\\": false}, \\\"error\\\": null, \\\"metadata\\\": {}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/ROADMAP.md\", \"content\": \"# acr-vla-conformal-refinement — Research Dashboard\\n\\n> 最后更新: 2026-05-21 00:48 UTC | 更新原因: D092-D095 updates: Plan A LOCKED, OpenVLA CRM CLOSED, π0.5/π added, GPU state corrected\\n\\n> 详见 paper_framing.md（D077: Adaptive K 核心, D088→D090→D092: Plan A GO）\\n\\n## 核心方向\\n**Adaptive inference-time compute for frozen VLAs** — K=2 L2 distance 作为不确定性信号，自适应决定推理策略（直出 vs CRM correction）。CRM correction>selection 分析作为支撑。\\n\\n## 投稿目标\\n**CoRL 2026** DDL **2026-05-29**。剩余 **8 天**。\\n\\n## 方法路径（D088→D092 最终）\\n- ❌ B (Learned Uncertainty Head): NO-GO, mean 12.0% < VLA-only (D090)\\n- ✅ **A (Plan A: K=2 Conformal + Selective CRM)**: Object 18.3%±2.1%, Spatial 35.0%±1.0% — **GO (D092/D094)**\\n- ⏳ C (Action Distribution Geometry): 不再需要，Plan A 已成功\\n\\n## Plan A 核心结果\\n| Benchmark | Plan A (K=2) | K=10 CRM | Δ vs K=10 | Compute |\\n|-----------|-------------|----------|-----------|---------|\\n| Object    | 18.3%±2.1%  | 16.8%    | +1.5pp    | 80% less (K=2 vs K=10) |\\n| Spatial   | 35.0%±1.0%  | 34.5%    | +0.5pp    | 80% less |\\n\\nPipeline: K=2 batched forward → d₂=‖a₁-a₂‖₂ → if d₂>τ: argmin-to-centroid + CRM; if d₂≤τ: direct output。\\n⚠️ Threshold calibration: flatten-L2 (30D) vs per-step-mean-L2 (7D×5) 差异 ~2.77×，当前 τ 在 Plan A scale 上 trigger rate 84%。待决：强调 K=2 效率 vs recalibrate Pareto sweep。\\n\\n## OpenVLA 实验线\\n- ✅ plan_801: OpenVLA v2 baseline SR=69%\\n- ✅ plan_802 train: CRM 训练完成 (val_loss=0.077260)\\n- ❌ **D093: OpenVLA CRM eval 0%** — near-deterministic (T=0.5, 8/10 identical actions)，applicability boundary，CLOSED\\n\\n## π0.5/π 实验线（D095，用户硬要求）\\n- 🔄 Phase 1: WebSearch + 下载模型（Agent 队列中）\\n- ⏳ Phase 2: env setup + baseline eval\\n- ⏳ Phase 3: 检查 action diversity → if stochastic: CRM pipeline\\n- 目的：第二/三个 VLA backbone（flow-matching），解决 M1 (narrow scope) + R2-W1-new (low absolute perf)\\n\\n## Norm Sweep 状态（plan_200/500）\\n| ε    | n seeds | mean SR | 状态 |\\n|------|---------|---------|------|\\n| 0.03 | ~6      | 15.5%   | seeds running |\\n| 0.05 | ~9      | 13.8%   | seeds running |\\n| 0.1  | ~8      | 15.0%   | seeds running |\\n| 0.2  | 12      | 17.2%   | LOCKED (7-seed core + extras) |\\n\\n## 核心实验结果\\n| Evidence | 结果 | 状态 |\\n|----------|------|------|\\n| **Plan A Object (D092)** | 18.3%±2.1% (K=2, seeds 19/16/20%) | LOCKED |\\n| **Plan A Spatial (D094)** | 35.0%±1.0% (K=2, seeds 34/35/36%) | LOCKED |\\n| Object CRM K=10 (norm02) | 16.8%±1.8% (n=7) | LOCKED |\\n| K=10 decomposition | correction +5.8pp, selection ≈0 | LOCKED |\\n| Random Selection | Object 9.7% (n=6) ≈ VLA-only | LOCKED |\\n| K-sweep | K=5 15.5%, K=10 16.8%, K=20 18.7% | LOCKED |\\n| Adaptive K P50 | 15.3% (avg_K=3.8, ~91% of K=10) | LOCKED |\\n| Spatial CRM K=10 | 34.5%±1.5% (n=9) | LOCKED |\\n| OpenVLA baseline | SR=69% | LOCKED |\\n| OpenVLA CRM (D093) | 0% — applicability boundary | CLOSED |\\n\\n## GPU 状态\\n17 GPU across 4 servers。Live check: bjb1-32546 3-4 张活跃（11.5GB/卡），bjb2-28827 5 张有模型加载（5.7GB/卡），bjb1-18228 部分活跃。Registry \\\"空闲\\\" 报告滞后于实际 GPU 进程。\\n\\n## 近期任务\\n- [ ] **P0** π0.5/π 模型调研 + baseline eval（D095，用户要求）\\n- [ ] **P0** Plan A 结果写入论文（Paper Agent 待指令）\\n- [ ] **P1** paper_framing.md 修正：ε=0.05 = 13.8%（非 14.3%）\\n- [ ] **P1** Threshold calibration 决策（用户未选）\\n- [ ] **P1** Norm sweep 补种完成 + Figure 2 生成\\n- [ ] **P2** review_issues 更新（C3/M1/M3/M6/R2-W1-new）\\n- [ ] **P2** Cron misfire 系统性修复\\n\\n## 关键决策日志\\n\\n| ID | 日期 | 摘要 | 关联实验 |\\n|----|------|------|----------|\\n| D096 | 2026-05-21 | D096: π0.5 适配 GO — baseline >60%, 7D action, flow- | eval-openvla-crm-object-seed42, eval-plan-a-object-seed42 |\\n| D095 | 2026-05-21 | D095: 新增 π0.5/π VLA baseline + CRM 实验线（用户要求）— flow | eval-openvla-crm-object-seed42 |\\n| D094 | 2026-05-21 | D094: Plan A Spatial 完成 — 35.0%±1.0% (K=2) 超过 K=10 | eval-plan-a-spatial-seed42, eval-plan-a-spatial-seed43, eval-plan-a-spatial-seed44 |\\n| D093 | 2026-05-20 | D093: OpenVLA CRM eval 0% — applicability boundary | eval-openvla-crm-object-seed42, eval-openvla-object-vla-only-seed42-v2 |\\n| D092 | 2026-05-20 | D092: Plan A (K=2 conformal + selective CRM) GO —  | eval-plan-a-object-seed42, eval-plan-a-object-seed43, eval-plan-a-object-seed44 |\\n| D091 | 2026-05-20 | D091: D090 narrative 影响评估——核心 claims 不受影响，D088 作为  | eval-adaptive-unc-head-object-seed42, eval-adaptive-k-p50-seed42 |\\n| D090 | 2026-05-20 | D090: D088 Learned Uncertainty Head NO-GO — 3 seed | eval-adaptive-unc-head-object-seed42, eval-adaptive-unc-head-object-seed43, eval-adaptive-unc-head-object-seed44 |\\n| D089 | 2026-05-20 | D089: Round 2 审稿 Holistic Pass — 3 个 SYSTEMIC_ISSU | eval-openvla-object-vla-only-seed42-v2 |\\n| D088 | 2026-05-20 | D088: 方法升级——Learned Uncertainty Head + Selective C | k2-l2-calibration-phase1 |\\n| D087 | 2026-05-20 | D087: 撤回 D086，恢复 OpenVLA 实验线（v2 baseline SR=69%，直接 | eval-openvla-object-vla-only-seed42-v2 |\\n\\n\", \"total_chars\": 4631, \"truncated\": false}, \"error\": null, \"metadata\": {}}"
    }
  }
}
```

</details>

---

### Assistant

_source line 11_

<details><summary>Logged reasoning block</summary>

```text
Now I need to also check for RUNNING experiments to see which norm sweep experiments are still running. Let me also parse the data I have.

Let me filter the DONE experiments for norm sweep (obs_only on Object with different norms). The pattern is `eval-obs-only-object-norm{003,005,01,02}-seed*`.

From the DONE experiments, let me identify the norm sweep ones:

1. `eval-obs-only-object-norm003-seed44` - ε=0.03, seed44, SR=0.15 (overall_success_rate), conclusion=success


2. `eval-obs-only-object-norm003-seed43-r2` - ε=0.03, seed43, failed run so I'll skip it
3. `eval-obs-only-object-norm03-seed48` - this one says "norm03" which is ε=0.3, not part of the sweep based on the command
4. `eval-obs-only-object-norm01-seed48` - ε=0.1, seed48, SR=0.18

, marked as success

Now I need to be more systematic about this. Let me look through the DONE registry for experiments matching the pattern `eval-obs-only-object-norm{003,005,01,02}-seed*`. I'm finding that `eval-obs-only-object-norm003-seed44` with ε=0.03 and seed44 shows a success rate of 0.15 and is marked successful, while the seed43 variant failed. The seed48 experiment with "norm03" in the name appears to be outside the sweep parameters based on its epsilon value. Looking at the successful experiments from the registry, I'm only finding two that match the norm sweep criteria—one at ε=0.03 with 15% success rate and one at ε=0.1 with 18% success rate. But the roadmap specifies much larger sample sizes across all epsilon values, so there's clearly a mismatch between what the registry shows as DONE and what should actually be completed.

I'm realizing the issue might be that I only queried DONE experiments, but the task also mentions checking RUNNING ones, and the naming convention might differ from what I expected. With only 27 total DONE experiments in the registry and most being different experiment types entirely, I need to look more broadly—either at different statuses or with more flexible matching on the experiment IDs. I should check if there are experiments with different naming conventions or statuses I haven't accounted for yet. Let me pull the full registry across all statuses to get a complete view of what's actually been registered.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "e17f41b1-3dce-49fb-a9e5-f5dd86423ed8",
  "uuid": "a05ab144-bf9b-4717-b1b5-3b73f9872cee",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01D58U5jiNmNvMajPcpQEdH8",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 16796,
      "cache_read_input_tokens": 24463,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 16796
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

_source line 12_

registry 只返回了 27 个 DONE 实验，且大部分不是 norm sweep。需要获取所有状态的实验来找齐 norm sweep 数据。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "e17f41b1-3dce-49fb-a9e5-f5dd86423ed8",
  "uuid": "58a09031-3a37-48e4-a34a-80eee9c5a9df",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01D58U5jiNmNvMajPcpQEdH8",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 16796,
      "cache_read_input_tokens": 24463,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 16796
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

_source line 13_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry · `toolu_01Py9xhR4gHWVtTXRbKimmKL`</summary>

```json
{
  "filters": {},
  "limit": 0,
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
  "session_id": "e17f41b1-3dce-49fb-a9e5-f5dd86423ed8",
  "uuid": "4b6b1d0d-d4ea-4e6e-8e01-97e5655f9587",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01D58U5jiNmNvMajPcpQEdH8",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 16796,
      "cache_read_input_tokens": 24463,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 16796
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

_source line 14 · 2026-05-21T03:22:48.468Z_

<details><summary>↩ Tool result · `toolu_01Py9xhR4gHWVtTXRbKimmKL`</summary>

```text
&lt;persisted-output>
Output too large (50.8KB). Full output saved to: /home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-8-projects-acr-vla-conformal-refinement/e17f41b1-3dce-49fb-a9e5-f5dd86423ed8/tool-results/toolu_01Py9xhR4gHWVtTXRbKimmKL.txt

Preview (first 2KB):
{"result":"{\"success\": true, \"data\": {\"experiments\": {\"eval-obs-only-object-norm005-seed75\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-21T02:56:05.523Z\", \"updated_at\": \"2026-05-21T02:56:12.611Z\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.15}}, \"eval-obs-only-object-norm01-seed74\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-21T02:55:20.812Z\", \"updated_at\": \"2026-05-21T02:55:28.975Z\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.13}}, \"eval-obs-only-object-norm01-seed64\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-21T02:54:30.053Z\", \"updated_at\": \"2026-05-21T02:54:30.754Z\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.15}}, \"eval-obs-only-object-norm003-seed73\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-21T02:53:26.508Z\", \"updated_at\": \"2026-05-21T02:53:31.930Z\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.16}}, \"eval-obs-only-object-norm005-seed64\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-21T02:52:33.605Z\", \"updated_at\": \"2026-05-21T02:52:37.242Z\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.15}}, \"eval-obs-only-object-norm003-seed65\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-21T02:51:17.482Z\", \"updated_at\": \"2026-05-21T02:51:23.912Z\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.17}}, \"eval-obs-only-object-norm003-seed64\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-21T02:51:17.026Z\", \"updated_at\": \"2026-05-21T02:51:23.446Z\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.17}}, \"eval-obs-only-object-norm003-seed63-r2\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-21T02:51:19.045Z\", \"updated_at\": \"2026-05-21T02:51:19.046Z\", \"conclu
...
&lt;/persisted-output>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "e17f41b1-3dce-49fb-a9e5-f5dd86423ed8",
  "uuid": "1c213c24-6bd8-4d15-8850-0dfe674ce93e",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"experiments\\\": {\\\"eval-obs-only-object-norm005-seed75\\\": {\\\"status\\\": \\\"PREPARING\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-21T02:56:05.523Z\\\", \\\"updated_at\\\": \\\"2026-05-21T02:56:12.611Z\\\", \\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"success_rate\\\": 0.15}}, \\\"eval-obs-only-object-norm01-seed74\\\": {\\\"status\\\": \\\"PREPARING\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-21T02:55:20.812Z\\\", \\\"updated_at\\\": \\\"2026-05-21T02:55:28.975Z\\\", \\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"success_rate\\\": 0.13}}, \\\"eval-obs-only-object-norm01-seed64\\\": {\\\"status\\\": \\\"PREPARING\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-21T02:54:30.053Z\\\", \\\"updated_at\\\": \\\"2026-05-21T02:54:30.754Z\\\", \\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"success_rate\\\": 0.15}}, \\\"eval-obs-only-object-norm003-seed73\\\": {\\\"status\\\": \\\"PREPARING\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-21T02:53:26.508Z\\\", \\\"updated_at\\\": \\\"2026-05-21T02:53:31.930Z\\\", \\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"success_rate\\\": 0.16}}, \\\"eval-obs-only-object-norm005-seed64\\\": {\\\"status\\\": \\\"PREPARING\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-21T02:52:33.605Z\\\", \\\"updated_at\\\": \\\"2026-05-21T02:52:37.242Z\\\", \\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"success_rate\\\": 0.15}}, \\\"eval-obs-only-object-norm003-seed65\\\": {\\\"status\\\": \\\"PREPARING\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-21T02:51:17.482Z\\\", \\\"updated_at\\\": \\\"2026-05-21T02:51:23.912Z\\\", \\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"success_rate\\\": 0.17}}, \\\"eval-obs-only-object-norm003-seed64\\\": {\\\"status\\\": \\\"PREPARING\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-21T02:51:17.026Z\\\", \\\"updated_at\\\": \\\"2026-05-21T02:51:23.446Z\\\", \\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"success_rate\\\": 0.17}}, \\\"eval-obs-only-object-norm003-seed63-r2\\\": {\\\"status\\\": \\\"PREPARING\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-21T02:51:19.045Z\\\", \\\"updated_at\\\": \\\"2026-05-21T02:51:19.046Z\\\", \\\"conclusion\\\": \\\"killed\\\"}, \\\"eval-obs-only-object-norm003-seed62-r2\\\": {\\\"status\\\": \\\"PREPARING\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-21T02:51:18.497Z\\\", \\\"updated_at\\\": \\\"2026-05-21T02:51:18.497Z\\\", \\\"conclusion\\\": \\\"killed\\\"}, \\\"eval-obs-only-object-norm005-seed65\\\": {\\\"status\\\": \\\"PREPARING\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-21T02:26:45.708Z\\\", \\\"updated_at\\\": \\\"2026-05-21T02:26:50.866Z\\\", \\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"success_rate\\\": 0.14}}, \\\"eval-obs-only-object-norm005-seed61\\\": {\\\"status\\\": \\\"PREPARING\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-21T01:54:41.975Z\\\", \\\"updated_at\\\": \\\"2026-05-21T01:54:46.787Z\\\", \\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"success_rate\\\": 0.15}}, \\\"eval-obs-only-object-norm01-seed60\\\": {\\\"status\\\": \\\"PREPARING\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-21T01:42:15.142Z\\\", \\\"updated_at\\\": \\\"2026-05-21T01:42:24.178Z\\\", \\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"success_rate\\\": 0.15}}, \\\"eval-obs-only-object-norm003-seed56\\\": {\\\"status\\\": \\\"PREPARING\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-21T01:42:14.531Z\\\", \\\"updated_at\\\": \\\"2026-05-21T01:42:23.974Z\\\", \\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"success_rate\\\": 0.15}}, \\\"eval-obs-only-object-norm01-seed66\\\": {\\\"status\\\": \\\"PREPARING\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-21T01:29:23.112Z\\\", \\\"updated_at\\\": \\\"2026-05-21T01:31:28.961Z\\\", \\\"pid\\\": 642775}, \\\"eval-obs-only-object-norm005-seed66\\\": {\\\"status\\\": \\\"PREPARING\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-21T01:29:22.550Z\\\", \\\"updated_at\\\": \\\"2026-05-21T01:31:28.635Z\\\", \\\"pid\\\": 642506}, \\\"eval-obs-only-object-norm003-seed66\\\": {\\\"status\\\": \\\"PREPARING\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-21T01:29:22.063Z\\\", \\\"updated_at\\\": \\\"2026-05-21T01:31:27.799Z\\\", \\\"pid\\\": 642428}, \\\"eval-obs-only-object-norm003-seed59\\\": {\\\"status\\\": \\\"PREPARING\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-21T01:23:09.866Z\\\", \\\"updated_at\\\": \\\"2026-05-21T01:23:22.549Z\\\", \\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"success_rate\\\": 0.13}}, \\\"eval-obs-only-object-norm005-seed58\\\": {\\\"status\\\": \\\"PREPARING\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-21T01:23:09.469Z\\\", \\\"updated_at\\\": \\\"2026-05-21T01:23:21.948Z\\\", \\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"success_rate\\\": 0.16}}, \\\"eval-obs-only-object-norm01-seed57\\\": {\\\"status\\\": \\\"PREPARING\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-21T01:23:08.871Z\\\", \\\"updated_at\\\": \\\"2026-05-21T01:23:21.444Z\\\", \\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"success_rate\\\": 0.19}}, \\\"eval-obs-only-object-norm005-seed63\\\": {\\\"status\\\": \\\"PREPARING\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-21T01:02:30.561Z\\\", \\\"updated_at\\\": \\\"2026-05-21T01:02:30.561Z\\\", \\\"conclusion\\\": \\\"killed\\\"}, \\\"eval-obs-only-object-norm005-seed62\\\": {\\\"status\\\": \\\"PREPARING\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-21T01:02:30.354Z\\\", \\\"updated_at\\\": \\\"2026-05-21T01:02:30.354Z\\\", \\\"conclusion\\\": \\\"killed\\\"}, \\\"eval-perdof-object-norm02-seed49\\\": {\\\"status\\\": \\\"DONE\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-20T15:59:12.635Z\\\", \\\"updated_at\\\": \\\"2026-05-20T15:59:54.757Z\\\", \\\"metrics\\\": {\\\"overall_success_rate\\\": 0.12, \\\"total_rollouts\\\": 100, \\\"total_successes\\\": 12, \\\"per_task_sr\\\": {\\\"alphabet_soup\\\": 0, \\\"cream_cheese\\\": 0, \\\"salad_dressing\\\": 0.1, \\\"bbq_sauce\\\": 0.2, \\\"ketchup\\\": 0, \\\"tomato_sauce\\\": 0, \\\"butter\\\": 0.1, \\\"milk\\\": 0.2, \\\"chocolate_pudding\\\": 0.4, \\\"orange_juice\\\": 0.2}}, \\\"log_path\\\": \\\"/root/acr-vla-conformal-refinement/logs/eval-perdof-object-norm02-seed49.log\\\", \\\"checkpoint_path\\\": \\\"/root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt\\\", \\\"spec\\\": {\\\"command\\\": \\\"python evaluate.py --mode crm_perdof --benchmark object --seed 49 --K 10 --max_correction_norm 0.2 --n_rollouts 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt --output_file logs/eval_perdof_object_norm02_seed49.json\\\", \\\"server\\\": \\\"bjb1-32546\\\", \\\"data_path\\\": \\\"LIBERO-Object\\\", \\\"data_count\\\": 100, \\\"model_name\\\": \\\"crm_perdof_norm02_K10\\\", \\\"seed\\\": 49, \\\"checkpoint_source\\\": \\\"/root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt\\\", \\\"eval_data\\\": \\\"LIBERO-Object\\\"}, \\\"hypothesis\\\": \\\"PerDoF CRM with norm-clipped corrections (epsilon=0.2, K=10) provides consistent improvement over baseline on LIBERO-Object across seeds; seed49 should yield SR in the 14-18% range consistent with seeds 43-48.\\\", \\\"conclusion\\\": \\\"success\\\", \\\"completed_at\\\": \\\"2026-05-20T15:59:54.757Z\\\"}, \\\"eval-obs-only-object-norm02-seed43-r3\\\": {\\\"status\\\": \\\"PREPARING\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-20T13:55:56.411Z\\\", \\\"updated_at\\\": \\\"2026-05-20T13:55:57.571Z\\\", \\\"conclusion\\\": \\\"failed\\\", \\\"failure_reason\\\": \\\"SIGHUP (tmux session terminated externally) at 8/10 tasks. No JSON output. r2 already has complete data (SR=16%), no retry needed.\\\"}, \\\"openvla-precompute-k1\\\": {\\\"status\\\": \\\"PREPARING\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-20T13:52:53.282Z\\\", \\\"updated_at\\\": \\\"2026-05-20T13:52:53.282Z\\\", \\\"notes\\\": \\\"GPU collision: cuda:3 被 Director P0-B 指令分配给 plan_702 seed43。预计算需要在 plan_702 完成后重启。原始提交: PID 365142, 处理 74507 timesteps from 500 demos. Output: /root/autodl-tmp/crm_cache_k1_openvla/object/. 特征维度: multi_scale_obs (4,4096), action_dim=6.\\\"}, \\\"eval-obs-only-goal-norm02-seed52\\\": {\\\"status\\\": \\\"DONE\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-20T12:05:20.840Z\\\", \\\"updated_at\\\": \\\"2026-05-20T12:58:35.610Z\\\", \\\"spec\\\": {\\\"command\\\": \\\"python -u src/evaluate.py --mode crm_obs_only --benchmark LIBERO-Goal --seed 52 --n_rollouts 10 --max_correction_norm 0.2\\\", \\\"server\\\": \\\"bjb1-32546\\\", \\\"gpu\\\": \\\"cuda:0\\\", \\\"pid\\\": 362579, \\\"data_path\\\": \\\"LIBERO-Goal\\\", \\\"data_count\\\": \\\"10 tasks x 10 rollouts\\\", \\\"model_name\\\": \\\"openvla-7b + CRM obs_only\\\", \\\"seed\\\": 52, \\\"checkpoint_source\\\": \\\"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\\\", \\\"eval_data\\\": \\\"LIBERO-Goal (10 tasks x 10 rollouts)\\\", \\\"log_path\\\": \\\"~/runs/acr-vla-conformal-refinement/eval-obs-only-goal-norm02-seed52.log\\\", \\\"checkpoint_path\\\": \\\"N/A (eval only)\\\"}, \\\"metrics\\\": {\\\"success_rate\\\": 0.68, \\\"successes\\\": 68, \\\"total\\\": 100, \\\"per_task_sr\\\": {\\\"open_middle_drawer_cabinet\\\": 0.7, \\\"put_bowl_on_stove\\\": 0.9, \\\"put_wine_bottle_on_cabinet\\\": 0.4, \\\"open_top_drawer_put_bowl\\\": 0.3, \\\"put_bowl_on_cabinet\\\": 0.8, \\\"push_plate_front_stove\\\": 0.8, \\\"put_cream_cheese_in_bowl\\\": 0.4, \\\"turn_on_stove\\\": 1, \\\"put_bowl_on_plate\\\": 1, \\\"put_wine_bottle_on_rack\\\": 0.5}}, \\\"conclusion\\\": \\\"success\\\", \\\"hypothesis\\\": \\\"CRM obs_only with K=10 and norm cap 0.2 improves SR on LIBERO-Goal by applying observation-conditioned corrections that compensate for VLA action prediction errors, providing a new seed for variance estimation.\\\", \\\"completed_at\\\": \\\"2026-05-20T12:58:26.417Z\\\", \\\"notes\\\": \\\"SR=68% on Goal seed52. Strong result; turn_on_stove and put_bowl_on_plate both 100%.\\\"}, \\\"eval-argmin-object-seed49\\\": {\\\"status\\\": \\\"DONE\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-20T12:05:22.690Z\\\", \\\"updated_at\\\": \\\"2026-05-20T12:58:34.569Z\\\", \\\"spec\\\": {\\\"command\\\": \\\"python -u src/evaluate.py --mode reconvla --benchmark LIBERO-Object --seed 49 --n_rollouts 10\\\", \\\"server\\\": \\\"bjb1-32546\\\", \\\"gpu\\\": \\\"cuda:5\\\", \\\"pid\\\": 364591, \\\"data_path\\\": \\\"LIBERO-Object\\\", \\\"data_count\\\": \\\"10 tasks x 10 rollouts\\\", \\\"model_name\\\": \\\"openvla-7b + CRM obs_only (argmin)\\\", \\\"seed\\\": 49, \\\"checkpoint_source\\\": \\\"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\\\", \\\"eval_data\\\": \\\"LIBERO-Object (10 tasks x 10 rollouts)\\\", \\\"log_path\\\": \\\"~/runs/acr-vla-conformal-refinement/eval-argmin-object-seed49.log\\\", \\\"checkpoint_path\\\": \\\"N/A (eval only)\\\"}, \\\"metrics\\\": {\\\"success_rate\\\": 0.16, \\\"successes\\\": 16, \\\"total\\\": 100, \\\"per_task_sr\\\": {\\\"alphabet_soup\\\": 0, \\\"cream_cheese\\\": 0, \\\"salad_dressing\\\": 0.2, \\\"bbq_sauce\\\": 0.4, \\\"ketchup\\\": 0, \\\"tomato_sauce\\\": 0.1, \\\"butter\\\": 0.1, \\\"milk\\\": 0.3, \\\"chocolate_pudding\\\": 0.3, \\\"orange_juice\\\": 0.2}}, \\\"conclusion\\\": \\\"success\\\", \\\"hypothesis\\\": \\\"Argmin (reconvla) selection among K=10 CRM refinements improves over single-step VLA on Object by choosing the candidate with lowest predicted residual, providing a multi-seed consistency check.\\\", \\\"completed_at\\\": \\\"2026-05-20T12:58:25.905Z\\\", \\\"notes\\\": \\\"SR=16% on Object seed49. Consistent with other argmin seeds on Object benchmark.\\\"}, \\\"eval-random-selection-spatial-seed43\\\": {\\\"status\\\": \\\"DONE\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-20T12:05:19.438Z\\\", \\\"updated_at\\\": \\\"2026-05-20T12:58:33.167Z\\\", \\\"spec\\\": {\\\"command\\\": \\\"python -u src/evaluate.py --mode random_selection --benchmark LIBERO-Spatial --seed 43 --n_rollouts 10\\\", \\\"server\\\": \\\"bjb1-18228\\\", \\\"gpu\\\": \\\"cuda:1\\\", \\\"pid\\\": 347075, \\\"data_path\\\": \\\"LIBERO-Spatial\\\", \\\"data_count\\\": \\\"10 tasks x 10 rollouts\\\", \\\"model_name\\\": \\\"openvla-7b + CRM obs_only\\\", \\\"seed\\\": 43, \\\"checkpoint_source\\\": \\\"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\\\", \\\"eval_data\\\": \\\"LIBERO-Spatial (10 tasks x 10 rollouts)\\\", \\\"log_path\\\": \\\"~/runs/acr-vla-conformal-refinement/eval-random-selection-spatial-seed43.log\\\", \\\"checkpoint_path\\\": \\\"N/A (eval only)\\\"}, \\\"metrics\\\": {\\\"success_rate\\\": 0.26, \\\"successes\\\": 26, \\\"total\\\": 100, \\\"per_task_sr\\\": {\\\"between_plate_ramekin\\\": 0.7, \\\"next_to_ramekin\\\": 0.9, \\\"table_center\\\": 0, \\\"cookie_box\\\": 0.1, \\\"top_drawer\\\": 0, \\\"on_ramekin\\\": 0, \\\"next_to_cookie_box\\\": 0.7, \\\"on_stove\\\": 0, \\\"next_to_plate\\\": 0.2, \\\"on_wooden_cabinet\\\": 0}}, \\\"conclusion\\\": \\\"success\\\", \\\"hypothesis\\\": \\\"Random candidate selection from K=10 CRM refinements serves as a lower-bound baseline, showing that informed selection (argmin) is necessary to achieve the full benefit of multi-step refinement on Spatial.\\\", \\\"completed_at\\\": \\\"2026-05-20T12:58:24.969Z\\\", \\\"notes\\\": \\\"SR=26% on Spatial seed43. Lower than argmin-based selection, confirming informed selection matters.\\\"}, \\\"eval-adaptive-k-spatial-p90-seed43\\\": {\\\"status\\\": \\\"DONE\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-20T10:52:06.660Z\\\", \\\"updated_at\\\": \\\"2026-05-20T12:58:31.849Z\\\", \\\"spec\\\": {\\\"command\\\": \\\"python -u src/evaluate.py --mode adaptive_k --benchmark LIBERO-Spatial --seed 43 --n_rollouts 10 --adaptive_k_threshold 0.125870 --output_file logs/eval-adaptive-k-spatial-p90-seed43.json\\\", \\\"server\\\": \\\"bjb1-18228\\\", \\\"gpu\\\": \\\"cuda:3\\\", \\\"pid\\\": 344852, \\\"data_path\\\": \\\"LIBERO-Spatial\\\", \\\"data_count\\\": \\\"10 tasks x 10 rollouts\\\", \\\"model_name\\\": \\\"openvla-7b + CRM obs_only\\\", \\\"seed\\\": 43, \\\"checkpoint_source\\\": \\\"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\\\", \\\"eval_data\\\": \\\"LIBERO-Spatial (10 tasks x 10 rollouts)\\\", \\\"log_path\\\": \\\"~/runs/acr-vla-conformal-refinement/eval-adaptive-k-spatial-p90-seed43.log\\\", \\\"checkpoint_path\\\": \\\"N/A (eval only)\\\"}, \\\"metrics\\\": {\\\"success_rate\\\": 0.32, \\\"successes\\\": 32, \\\"total\\\": 100, \\\"avg_K\\\": 3.6, \\\"fast_path_pct\\\": 80.2, \\\"mean_l2\\\": 0.0905, \\\"per_task_sr\\\": {\\\"between_plate_ramekin\\\": 0.7, \\\"next_to_ramekin\\\": 1, \\\"table_center\\\": 0.1, \\\"cookie_box\\\": 0.3, \\\"top_drawer\\\": 0, \\\"on_ramekin\\\": 0.1, \\\"next_to_cookie_box\\\": 0.8, \\\"on_stove\\\": 0, \\\"next_to_plate\\\": 0.2, \\\"on_wooden_cabinet\\\": 0}}, \\\"conclusion\\\": \\\"success\\\", \\\"hypothesis\\\": \\\"Adaptive K with P90 threshold (τ=0.1259) reduces average refinement steps while maintaining comparable SR to fixed K=10 on Spatial, because most states have low CRM residuals and can skip full refinement.\\\", \\\"completed_at\\\": \\\"2026-05-20T12:58:23.572Z\\\", \\\"notes\\\": \\\"SR=32%, avg_K=3.6 (vs fixed K=10), 80.2% fast-path. Adaptive K saves ~64% compute with seed43 on Spatial.\\\"}, \\\"eval-adaptive-k-object-p90-seed44\\\": {\\\"status\\\": \\\"DONE\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-20T12:45:08.564Z\\\", \\\"updated_at\\\": \\\"2026-05-20T12:45:37.089Z\\\", \\\"hypothesis\\\": \\\"Adaptive K with τ=P90 (0.125870) on LIBERO-Object seed44. P90 是最宽松的阈值——大部分 step fast-path (K=1)，仅在极高不确定性时用 K=10。验证 P90 在 Object 上的 SR/compute tradeoff。\\\", \\\"spec\\\": {\\\"command\\\": \\\"python -u src/evaluate.py --mode adaptive_k --benchmark LIBERO-Object --seed 44 --n_rollouts 10 --adaptive_k_threshold 0.125870\\\", \\\"server\\\": \\\"bjb2-28827\\\", \\\"data_path\\\": \\\"LIBERO-Object\\\", \\\"data_count\\\": \\\"10 tasks x 10 rollouts\\\", \\\"model_name\\\": \\\"openvla-7b + CRM obs_only\\\", \\\"seed\\\": 44, \\\"checkpoint_source\\\": \\\"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\\\", \\\"eval_data\\\": \\\"LIBERO-Object (10 tasks x 10 rollouts)\\\", \\\"log_path\\\": \\\"N/A (discovered by Reviewer)\\\", \\\"checkpoint_path\\\": \\\"N/A (eval only)\\\"}, \\\"metrics\\\": {\\\"sr\\\": 14, \\\"avg_K\\\": 2.58, \\\"fast_path_pct\\\": 92.8, \\\"total_rollouts\\\": 100}, \\\"conclusion\\\": \\\"success\\\", \\\"completed_at\\\": \\\"2026-05-20T12:45:37.089Z\\\"}, \\\"eval-adaptive-k-object-p90-seed43\\\": {\\\"status\\\": \\\"DONE\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-20T12:45:08.312Z\\\", \\\"updated_at\\\": \\\"2026-05-20T12:45:34.700Z\\\", \\\"hypothesis\\\": \\\"Adaptive K with τ=P90 (0.125870) on LIBERO-Object seed43. P90 是最宽松的阈值——大部分 step fast-path (K=1)，仅在极高不确定性时用 K=10。验证 P90 在 Object 上的 SR/compute tradeoff。\\\", \\\"spec\\\": {\\\"command\\\": \\\"python -u src/evaluate.py --mode adaptive_k --benchmark LIBERO-Object --seed 43 --n_rollouts 10 --adaptive_k_threshold 0.125870\\\", \\\"server\\\": \\\"bjb2-28827\\\", \\\"data_path\\\": \\\"LIBERO-Object\\\", \\\"data_count\\\": \\\"10 tasks x 10 rollouts\\\", \\\"model_name\\\": \\\"openvla-7b + CRM obs_only\\\", \\\"seed\\\": 43, \\\"checkpoint_source\\\": \\\"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\\\", \\\"eval_data\\\": \\\"LIBERO-Object (10 tasks x 10 rollouts)\\\", \\\"log_path\\\": \\\"N/A (discovered by Reviewer)\\\", \\\"checkpoint_path\\\": \\\"N/A (eval only)\\\"}, \\\"metrics\\\": {\\\"sr\\\": 14, \\\"avg_K\\\": 2.61, \\\"fast_path_pct\\\": 92.3, \\\"total_rollouts\\\": 100}, \\\"conclusion\\\": \\\"success\\\", \\\"completed_at\\\": \\\"2026-05-20T12:45:34.700Z\\\"}, \\\"eval-argmin-object-seed48\\\": {\\\"status\\\": \\\"RUNNING\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-20T12:05:22.501Z\\\", \\\"updated_at\\\": \\\"2026-05-20T12:05:49.680Z\\\", \\\"spec\\\": {\\\"command\\\": \\\"python -u src/evaluate.py --mode reconvla --benchmark LIBERO-Object --seed 48 --n_rollouts 10\\\", \\\"server\\\": \\\"bjb1-32546\\\", \\\"gpu\\\": \\\"cuda:4\\\", \\\"pid\\\": 364125, \\\"data_path\\\": \\\"LIBERO-Object\\\", \\\"data_count\\\": \\\"10 tasks x 10 rollouts\\\", \\\"model_name\\\": \\\"openvla-7b + CRM obs_only (argmin)\\\", \\\"seed\\\": 48, \\\"checkpoint_source\\\": \\\"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\\\", \\\"eval_data\\\": \\\"LIBERO-Object (10 tasks x 10 rollouts)\\\", \\\"log_path\\\": \\\"~/runs/acr-vla-conformal-refinement/eval-argmin-object-seed48.log\\\"}}, \\\"eval-obs-only-object-norm02-seed49\\\": {\\\"status\\\": \\\"RUNNING\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-20T12:05:21.387Z\\\", \\\"updated_at\\\": \\\"2026-05-20T12:05:49.425Z\\\", \\\"spec\\\": {\\\"command\\\": \\\"python -u src/evaluate.py --mode crm_obs_only --benchmark LIBERO-Object --seed 49 --n_rollouts 10 --max_correction_norm 0.2\\\", \\\"server\\\": \\\"bjb1-32546\\\", \\\"gpu\\\": \\\"cuda:3\\\", \\\"pid\\\": 363783, \\\"data_path\\\": \\\"LIBERO-Object\\\", \\\"data_count\\\": \\\"10 tasks x 10 rollouts\\\", \\\"model_name\\\": \\\"openvla-7b + CRM obs_only\\\", \\\"seed\\\": 49, \\\"checkpoint_source\\\": \\\"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\\\", \\\"eval_data\\\": \\\"LIBERO-Object (10 tasks x 10 rollouts)\\\", \\\"log_path\\\": \\\"~/runs/acr-vla-conformal-refinement/eval-obs-only-object-norm02-seed49.log\\\"}}, \\\"eval-random-selection-spatial-seed44\\\": {\\\"status\\\": \\\"RUNNING\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-20T12:05:19.931Z\\\", \\\"updated_at\\\": \\\"2026-05-20T12:05:41.684Z\\\", \\\"spec\\\": {\\\"command\\\": \\\"python -u src/evaluate.py --mode random_selection --benchmark LIBERO-Spatial --seed 44 --n_rollouts 10\\\", \\\"server\\\": \\\"bjb1-18228\\\", \\\"gpu\\\": \\\"cuda:2\\\", \\\"pid\\\": 348897, \\\"data_path\\\": \\\"LIBERO-Spatial\\\", \\\"data_count\\\": \\\"10 tasks x 10 rollouts\\\", \\\"model_name\\\": \\\"openvla-7b + CRM obs_only\\\", \\\"seed\\\": 44, \\\"checkpoint_source\\\": \\\"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\\\", \\\"eval_data\\\": \\\"LIBERO-Spatial (10 tasks x 10 rollouts)\\\", \\\"log_path\\\": \\\"~/runs/acr-vla-conformal-refinement/eval-random-selection-spatial-seed44.log\\\"}}, \\\"eval-random-selection-spatial-seed42\\\": {\\\"status\\\": \\\"RUNNING\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-20T10:52:07.011Z\\\", \\\"updated_at\\\": \\\"2026-05-20T12:04:59.708Z\\\", \\\"spec\\\": {\\\"command\\\": \\\"python -u src/evaluate.py --mode random_selection --benchmark LIBERO-Spatial --seed 42 --n_rollouts 10\\\", \\\"server\\\": \\\"bjb1-18228\\\", \\\"gpu\\\": \\\"cuda:0\\\", \\\"pid\\\": 346801, \\\"data_path\\\": \\\"LIBERO-Spatial\\\", \\\"data_count\\\": \\\"10 tasks x 10 rollouts\\\", \\\"model_name\\\": \\\"openvla-7b + CRM obs_only\\\", \\\"seed\\\": 42, \\\"checkpoint_source\\\": \\\"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\\\", \\\"eval_data\\\": \\\"LIBERO-Spatial (10 tasks x 10 rollouts)\\\", \\\"log_path\\\": \\\"~/runs/acr-vla-conformal-refinement/eval-random-selection-spatial-seed42.log\\\"}, \\\"notes\\\": \\\"原 bjb1-32546 上的重复副本(PID 360293/360306)已 kill。此实验实际在 bjb1-18228:cuda:0 运行(PID 346801, mass-deploy 部署)。\\\"}, \\\"eval-adaptive-k-spatial-p50-seed42\\\": {\\\"status\\\": \\\"DONE\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-20T11:24:12.894Z\\\", \\\"updated_at\\\": \\\"2026-05-20T11:25:16.991Z\\\", \\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"sr\\\": 30, \\\"avg_K\\\": 6.324, \\\"fast_path_pct\\\": 45.95, \\\"mean_l2\\\": 0.0903, \\\"total_rollouts\\\": 100}, \\\"failure_reason\\\": \\\"\\\", \\\"completed_at\\\": \\\"2026-05-20T11:06:00.000Z\\\", \\\"notes\\\": \\\"Reviewer 独立验证：JSON 完整，日志确认 SR=30%，PID 自然退出。之前被 cron 误判为 failed（PID dead + 无 sentinel），已修正为 success。\\\", \\\"spec\\\": {\\\"command\\\": \\\"python -u src/evaluate.py --mode adaptive_k --benchmark LIBERO-Spatial --seed 42 --n_rollouts 10 --adaptive_k_threshold 0.074855\\\", \\\"server\\\": \\\"bjb2-40593\\\", \\\"gpu\\\": \\\"cuda:0\\\", \\\"pid\\\": 681823, \\\"data_path\\\": \\\"LIBERO-Spatial\\\", \\\"data_count\\\": \\\"10 tasks x 10 rollouts\\\", \\\"model_name\\\": \\\"openvla-7b + CRM obs_only\\\", \\\"seed\\\": 42, \\\"checkpoint_source\\\": \\\"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\\\", \\\"eval_data\\\": \\\"LIBERO-Spatial (10 tasks x 10 rollouts)\\\", \\\"log_path\\\": \\\"~/runs/acr-vla-conformal-refinement/eval-adaptive-k-spatial-p50-seed42.log\\\", \\\"checkpoint_path\\\": \\\"N/A (eval only)\\\"}, \\\"hypothesis\\\": \\\"Adaptive K with τ=P50 (0.074855, Object-calibrated) on LIBERO-Spatial seed42. 验证 Adaptive K 方法在第二个 benchmark 上的泛化：使用 Object 上校准的阈值直接应用到 Spatial（无 per-benchmark tuning）。如果 SR 接近 CRM K=10 (34.3%) 且 fast_path >50%，则证明方法跨 benchmark 通用。\\\"}, \\\"eval-obs-only-object-norm003-seed44\\\": {\\\"status\\\": \\\"DONE\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-20T10:52:14.742Z\\\", \\\"updated_at\\\": \\\"2026-05-20T10:52:47.202Z\\\", \\\"hypothesis\\\": \\\"CRM obs_only ε=0.03 on Object seed44. Low-norm multi-seed supplement (plan_500): strengthens Figure 2 error bars at small ε.\\\", \\\"spec\\\": {\\\"command\\\": \\\"evaluate.py --mode crm_obs_only --benchmark object --seed 44 --n_rollouts 10 --K 10 --max_correction_norm 0.03\\\", \\\"server\\\": \\\"bjb2-28827\\\", \\\"seed\\\": 44, \\\"model_name\\\": \\\"crm_v3_norm/obs_only/crm_best.pt\\\", \\\"data_path\\\": \\\"LIBERO_object\\\", \\\"data_count\\\": 100}, \\\"log_path\\\": \\\"~/runs/acr-vla-conformal-refinement/eval-obs-only-object-norm003-seed44.log\\\", \\\"checkpoint_path\\\": \\\"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\\\", \\\"metrics\\\": {\\\"overall_success_rate\\\": 0.15, \\\"total_successes\\\": 15, \\\"total_rollouts\\\": 100, \\\"per_task\\\": {\\\"alphabet_soup\\\": 0, \\\"cream_cheese\\\": 0, \\\"salad_dressing\\\": 0.3, \\\"bbq_sauce\\\": 0.2, \\\"ketchup\\\": 0, \\\"tomato_sauce\\\": 0.1, \\\"butter\\\": 0.1, \\\"milk\\\": 0.2, \\\"chocolate_pudding\\\": 0.3, \\\"orange_juice\\\": 0.3}}, \\\"conclusion\\\": \\\"success\\\", \\\"completed_at\\\": \\\"2026-05-20T10:52:47.202Z\\\"}, \\\"eval-adaptive-k-spatial-p90-seed42\\\": {\\\"status\\\": \\\"RUNNING\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-20T10:52:05.759Z\\\", \\\"updated_at\\\": \\\"2026-05-20T10:52:38.383Z\\\", \\\"spec\\\": {\\\"command\\\": \\\"python -u src/evaluate.py --mode adaptive_k --benchmark LIBERO-Spatial --seed 42 --n_rollouts 10 --adaptive_k_threshold 0.125870 --output_file logs/eval-adaptive-k-spatial-p90-seed42.json\\\", \\\"server\\\": \\\"bjb2-28827\\\", \\\"gpu\\\": \\\"cuda:2\\\", \\\"pid\\\": 308030, \\\"data_path\\\": \\\"LIBERO-Spatial\\\", \\\"data_count\\\": \\\"10 tasks x 10 rollouts\\\", \\\"model_name\\\": \\\"openvla-7b + CRM obs_only\\\", \\\"seed\\\": 42, \\\"checkpoint_source\\\": \\\"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\\\", \\\"eval_data\\\": \\\"LIBERO-Spatial (10 tasks x 10 rollouts)\\\", \\\"log_path\\\": \\\"~/runs/acr-vla-conformal-refinement/eval-adaptive-k-spatial-p90-seed42.log\\\"}}, \\\"eval-adaptive-k-spatial-p25-seed44\\\": {\\\"status\\\": \\\"RUNNING\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-20T10:52:04.790Z\\\", \\\"updated_at\\\": \\\"2026-05-20T10:52:34.962Z\\\", \\\"spec\\\": {\\\"command\\\": \\\"python -u src/evaluate.py --mode adaptive_k --benchmark LIBERO-Spatial --seed 44 --n_rollouts 10 --adaptive_k_threshold 0.054959 --output_file logs/eval-adaptive-k-spatial-p25-seed44.json\\\", \\\"server\\\": \\\"bjb2-28827\\\", \\\"gpu\\\": \\\"cuda:1\\\", \\\"pid\\\": 307754, \\\"data_path\\\": \\\"LIBERO-Spatial\\\", \\\"data_count\\\": \\\"10 tasks x 10 rollouts\\\", \\\"model_name\\\": \\\"openvla-7b + CRM obs_only\\\", \\\"seed\\\": 44, \\\"checkpoint_source\\\": \\\"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\\\", \\\"eval_data\\\": \\\"LIBERO-Spatial (10 tasks x 10 rollouts)\\\", \\\"log_path\\\": \\\"~/runs/acr-vla-conformal-refinement/eval-adaptive-k-spatial-p25-seed44.log\\\"}}, \\\"eval-adaptive-k-spatial-p75-seed44\\\": {\\\"status\\\": \\\"RUNNING\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-20T10:52:04.320Z\\\", \\\"updated_at\\\": \\\"2026-05-20T10:52:32.674Z\\\", \\\"spec\\\": {\\\"command\\\": \\\"python -u src/evaluate.py --mode adaptive_k --benchmark LIBERO-Spatial --seed 44 --n_rollouts 10 --adaptive_k_threshold 0.098735 --output_file logs/eval-adaptive-k-spatial-p75-seed44.json\\\", \\\"server\\\": \\\"bjb2-28827\\\", \\\"gpu\\\": \\\"cuda:0\\\", \\\"pid\\\": 307478, \\\"data_path\\\": \\\"LIBERO-Spatial\\\", \\\"data_count\\\": \\\"10 tasks x 10 rollouts\\\", \\\"model_name\\\": \\\"openvla-7b + CRM obs_only\\\", \\\"seed\\\": 44, \\\"checkpoint_source\\\": \\\"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\\\", \\\"eval_data\\\": \\\"LIBERO-Spatial (10 tasks x 10 rollouts)\\\", \\\"log_path\\\": \\\"~/runs/acr-vla-conformal-refinement/eval-adaptive-k-spatial-p75-seed44.log\\\"}}, \\\"eval-random-selection-object-seed46-r2\\\": {\\\"status\\\": \\\"DONE\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-19T17:41:16.541Z\\\", \\\"updated_at\\\": \\\"2026-05-19T17:41:32.255Z\\\", \\\"spec\\\": {\\\"command\\\": \\\"cd /root/acr-vla-conformal-refinement && timeout 57600 /root/miniconda3/bin/python -u src/evaluate.py --mode random_selection --benchmark object --n_rollouts 10 --seed 46 --K 10 --output_file logs/eval_object_random_selection_seed46.json\\\", \\\"server\\\": \\\"bjb2-40593\\\", \\\"data_path\\\": \\\"LIBERO-Object\\\", \\\"data_count\\\": 100, \\\"model_name\\\": \\\"SmolVLA_random_selection\\\", \\\"seed\\\": 46, \\\"checkpoint_path\\\": \\\"N/A-eval-only\\\", \\\"log_path\\\": \\\"/root/acr-vla-conformal-refinement/logs/eval_object_random_selection_seed46.log\\\"}, \\\"hypothesis\\\": \\\"Random selection baseline (K=10) on LIBERO-Object seed46 establishes reference success rate for comparing against CRM-guided selection methods\\\", \\\"conclusion\\\": \\\"killed\\\", \\\"completed_at\\\": \\\"2026-05-19T17:41:32.255Z\\\"}, \\\"eval-obs-only-spatial-norm02-seed46-r2\\\": {\\\"status\\\": \\\"RUNNING\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-19T17:12:13.545Z\\\", \\\"updated_at\\\": \\\"2026-05-19T17:12:53.558Z\\\", \\\"hypothesis\\\": \\\"obs_only CRM with epsilon=0.2 and K=10 improves LIBERO-Spatial success rate by applying observation-conditioned conformal corrections to fix spatial reasoning errors, seed46 rerun for statistical robustness\\\", \\\"spec\\\": {\\\"command\\\": \\\"cd /root/acr-vla-conformal-refinement && /root/miniconda3/bin/python -u src/evaluate.py --mode crm_obs_only --benchmark spatial --n_rollouts 10 --seed 46 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --max_correction_norm 0.2 --output_file logs/eval_spatial_obs_only_norm02_seed46_r2.json\\\", \\\"server\\\": \\\"bjb2-28827\\\", \\\"gpu\\\": [\\\"cuda:3\\\"], \\\"data_path\\\": \\\"LIBERO-Spatial\\\", \\\"data_count\\\": 100, \\\"model_name\\\": \\\"SmolVLA+CRM_obs_only\\\", \\\"seed\\\": 46, \\\"checkpoint_source\\\": \\\"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\\\", \\\"checkpoint_path\\\": \\\"N/A-eval-only\\\", \\\"log_path\\\": \\\"~/runs/acr-vla-conformal-refinement/eval-obs-only-spatial-norm02-seed46-r2.log\\\"}}, \\\"eval-vla-only-goal-seed44-r2\\\": {\\\"status\\\": \\\"RUNNING\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-19T17:12:11.696Z\\\", \\\"updated_at\\\": \\\"2026-05-19T17:12:53.198Z\\\", \\\"hypothesis\\\": \\\"VLA-only baseline on LIBERO-Goal seed44 establishes reference success rate for comparing against CRM-augmented methods on goal-conditioned tasks, rerun for statistical robustness\\\", \\\"spec\\\": {\\\"command\\\": \\\"cd /root/acr-vla-conformal-refinement && /root/miniconda3/bin/python -u src/evaluate.py --mode vla_only --benchmark goal --n_rollouts 10 --seed 44 --K 1 --output_file logs/eval_goal_vla_only_seed44_r2.json\\\", \\\"server\\\": \\\"bjb2-28827\\\", \\\"gpu\\\": [\\\"cuda:0\\\"], \\\"data_path\\\": \\\"LIBERO-Goal\\\", \\\"data_count\\\": 100, \\\"model_name\\\": \\\"SmolVLA\\\", \\\"seed\\\": 44, \\\"checkpoint_path\\\": \\\"N/A-eval-only\\\", \\\"log_path\\\": \\\"~/runs/acr-vla-conformal-refinement/eval-vla-only-goal-seed44-r2.log\\\"}}, \\\"eval-argmin-object-k5-seed44-r2\\\": {\\\"status\\\": \\\"RUNNING\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-19T17:12:10.271Z\\\", \\\"updated_at\\\": \\\"2026-05-19T17:12:52.978Z\\\", \\\"hypothesis\\\": \\\"ReConVLA argmin mode with K=5 candidates improves LIBERO-Object success rate over VLA-only baseline by selecting the best action from multiple VLA samples using conformal scoring, seed44 rerun for statistical robustness\\\", \\\"spec\\\": {\\\"command\\\": \\\"cd /root/acr-vla-conformal-refinement && /root/miniconda3/bin/python -u src/evaluate.py --mode reconvla --benchmark object --n_rollouts 10 --seed 44 --K 5 --output_file logs/eval_object_argmin_k5_seed44_r2.json\\\", \\\"server\\\": \\\"bjb2-28827\\\", \\\"gpu\\\": [\\\"cuda:1\\\"], \\\"data_path\\\": \\\"LIBERO-Object\\\", \\\"data_count\\\": 100, \\\"model_name\\\": \\\"SmolVLA_argmin\\\", \\\"seed\\\": 44, \\\"checkpoint_path\\\": \\\"N/A-eval-only\\\", \\\"log_path\\\": \\\"~/runs/acr-vla-conformal-refinement/eval-argmin-object-k5-seed44-r2.log\\\"}}, \\\"eval-openvla-object-baseline-seed42\\\": {\\\"status\\\": \\\"RUNNING\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-19T17:12:07.506Z\\\", \\\"updated_at\\\": \\\"2026-05-19T17:12:46.396Z\\\", \\\"hypothesis\\\": \\\"OpenVLA baseline on LIBERO-Object seed42 establishes reference success rate for comparing against SmolVLA and CRM-augmented methods on object manipulation tasks\\\", \\\"spec\\\": {\\\"command\\\": \\\"bash -c \\\\\\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/openvla-repo && CUDA_VISIBLE_DEVICES=4 TRANSFORMERS_OFFLINE=1 HF_HUB_OFFLINE=1 python experiments/robot/libero/run_libero_eval.py --model_family openvla --pretrained_checkpoint /root/autodl-tmp/models/openvla-libero-object --task_suite_name libero_object --center_crop True --seed 42 --num_trials_per_task 50 --use_wandb False\\\\\\\"\\\", \\\"server\\\": \\\"bjb2-28827\\\", \\\"gpu\\\": [\\\"cuda:4\\\"], \\\"data_path\\\": \\\"LIBERO-Object\\\", \\\"data_count\\\": 500, \\\"model_name\\\": \\\"OpenVLA\\\", \\\"seed\\\": 42, \\\"checkpoint_source\\\": \\\"/root/autodl-tmp/models/openvla-libero-object\\\", \\\"eval_data\\\": \\\"LIBERO-Object\\\", \\\"checkpoint_path\\\": \\\"N/A-eval-only\\\", \\\"log_path\\\": \\\"~/runs/acr-vla-conformal-refinement/eval-openvla-object-baseline-seed42.log\\\"}}, \\\"eval-obs-only-spatial-norm02-seed47\\\": {\\\"status\\\": \\\"DONE\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-19T17:02:40.986Z\\\", \\\"updated_at\\\": \\\"2026-05-19T17:03:14.457Z\\\", \\\"metrics\\\": {\\\"success_rate\\\": 0.32, \\\"successes\\\": 32, \\\"total\\\": 100, \\\"n_tasks\\\": 10, \\\"n_rollouts\\\": 10, \\\"per_task\\\": {\\\"between_plate_and_ramekin\\\": 0.8, \\\"next_to_ramekin\\\": 0.9, \\\"from_table_center\\\": 0, \\\"on_cookie_box\\\": 0.3, \\\"in_top_drawer\\\": 0.1, \\\"on_ramekin\\\": 0, \\\"next_to_cookie_box\\\": 0.9, \\\"on_stove\\\": 0, \\\"next_to_plate\\\": 0.2, \\\"on_wooden_cabinet\\\": 0}}, \\\"checkpoint_path\\\": \\\"N/A-eval-only\\\", \\\"log_path\\\": \\\"~/runs/acr-vla-conformal-refinement/eval-obs-only-spatial-norm02-seed47.log\\\", \\\"conclusion\\\": \\\"success\\\", \\\"spec\\\": {\\\"command\\\": \\\"cd /root/acr-vla-conformal-refinement && /root/miniconda3/bin/python -u src/evaluate.py --mode crm_obs_only --benchmark spatial --n_rollouts 10 --seed 47 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --max_correction_norm 0.2 --output_file logs/eval_spatial_obs_only_norm02_seed47.json\\\", \\\"server\\\": \\\"bjb1-32546\\\", \\\"data_path\\\": \\\"LIBERO-Spatial\\\", \\\"data_count\\\": 100, \\\"model_name\\\": \\\"crm_obs_only\\\", \\\"seed\\\": 47}, \\\"hypothesis\\\": \\\"obs_only CRM with epsilon=0.2 and K=10 improves success rate over VLA-only baseline on LIBERO-Spatial because observation-conditioned conformal corrections can detect and fix spatial reasoning errors without requiring action history\\\", \\\"completed_at\\\": \\\"2026-05-19T17:03:14.457Z\\\"}, \\\"eval-vla-only-spatial-seed45\\\": {\\\"status\\\": \\\"DONE\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-19T15:19:50.220Z\\\", \\\"updated_at\\\": \\\"2026-05-19T15:20:24.563Z\\\", \\\"spec\\\": {\\\"log_path\\\": \\\"~/runs/acr-vla-conformal-refinement/eval-vla-only-spatial-seed45.log\\\", \\\"command\\\": \\\"python evaluate.py --benchmark spatial --mode vla_only --seed 45\\\", \\\"server\\\": \\\"bjb1-32546\\\", \\\"seed\\\": 45, \\\"data_path\\\": \\\"LIBERO-Spatial\\\", \\\"data_count\\\": 100, \\\"model_name\\\": \\\"SmolVLA\\\", \\\"checkpoint_path\\\": \\\"N/A (eval-only)\\\"}, \\\"metrics\\\": {\\\"success_rate\\\": 0.27, \\\"per_task\\\": {\\\"between_plate_and_ramekin\\\": 0.7, \\\"next_to_ramekin\\\": 0.9, \\\"from_table_center\\\": 0, \\\"on_cookie_box\\\": 0.2, \\\"in_top_drawer\\\": 0, \\\"on_ramekin\\\": 0, \\\"next_to_cookie_box\\\": 0.9, \\\"on_stove\\\": 0, \\\"next_to_plate\\\": 0, \\\"on_wooden_cabinet\\\": 0}, \\\"successes\\\": 27, \\\"total\\\": 100}, \\\"conclusion\\\": \\\"success\\\", \\\"hypothesis\\\": \\\"VLA-only baseline on LIBERO-Spatial with seed 45 establishes reference success rate for comparison with CRM-augmented methods\\\", \\\"completed_at\\\": \\\"2026-05-19T15:20:24.563Z\\\"}, \\\"eval-obs-only-spatial-norm02-seed44\\\": {\\\"status\\\": \\\"DONE\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-19T14:23:33.161Z\\\", \\\"updated_at\\\": \\\"2026-05-19T14:26:44.810Z\\\", \\\"metrics\\\": {\\\"success_rate\\\": 0.36, \\\"successes\\\": 36, \\\"total\\\": 100}, \\\"checkpoint_path\\\": \\\"N/A (eval only)\\\", \\\"log_path\\\": \\\"/root/acr-vla-conformal-refinement/logs/eval_spatial_obs_only_norm02_seed44.json\\\", \\\"conclusion\\\": \\\"success\\\", \\\"spec\\\": {\\\"command\\\": \\\"python eval_crm.py --mode crm_obs_only --benchmark spatial --K 10 --seed 44 --max_correction_norm 0.2\\\", \\\"server\\\": \\\"bjb2-28827\\\", \\\"data_path\\\": \\\"spatial_benchmark\\\", \\\"data_count\\\": 100, \\\"model_name\\\": \\\"crm_obs_only\\\", \\\"seed\\\": 44}, \\\"hypothesis\\\": \\\"CRM obs-only mode with max_correction_norm=0.2 can improve spatial benchmark success rate by refining VLA actions using only observation-based conformal prediction, without access to privileged state information.\\\", \\\"completed_at\\\": \\\"2026-05-19T14:24:10.857Z\\\"}, \\\"eval-obs-only-object-norm003-seed43-r2\\\": {\\\"status\\\": \\\"DONE\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-19T05:14:10.523Z\\\", \\\"updated_at\\\": \\\"2026-05-19T05:14:25.385Z\\\", \\\"conclusion\\\": \\\"failed\\\", \\\"spec\\\": {\\\"checkpoint_path\\\": \\\"N/A (eval-only)\\\", \\\"log_path\\\": \\\"/root/acr-vla-conformal-refinement/logs/eval_object_obs_only_norm003_seed43.log\\\", \\\"metrics\\\": {\\\"success_rate\\\": null, \\\"tasks_completed\\\": \\\"1/10\\\", \\\"failure_reason\\\": \\\"process terminated prematurely after 1 task\\\"}}, \\\"completed_at\\\": \\\"2026-05-19T05:14:25.385Z\\\"}, \\\"eval-obs-only-object-norm03-seed48\\\": {\\\"status\\\": \\\"DONE\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-18T13:26:49.122Z\\\", \\\"updated_at\\\": \\\"2026-05-18T13:27:19.389Z\\\", \\\"metrics\\\": {\\\"overall_success_rate\\\": 0.16, \\\"per_task\\\": {\\\"pick_up_the_alphabet_soup_and_place_it_in_the_basket\\\": 0, \\\"pick_up_the_cream_cheese_and_place_it_in_the_basket\\\": 0, \\\"pick_up_the_salad_dressing_and_place_it_in_the_basket\\\": 0.3, \\\"pick_up_the_bbq_sauce_and_place_it_in_the_basket\\\": 0.4, \\\"pick_up_the_ketchup_and_place_it_in_the_basket\\\": 0, \\\"pick_up_the_tomato_sauce_and_place_it_in_the_basket\\\": 0.1, \\\"pick_up_the_butter_and_place_it_in_the_basket\\\": 0.1, \\\"pick_up_the_milk_and_place_it_in_the_basket\\\": 0.1, \\\"pick_up_the_chocolate_pudding_and_place_it_in_the_basket\\\": 0.4, \\\"pick_up_the_orange_juice_and_place_it_in_the_basket\\\": 0.2}}, \\\"log_path\\\": \\\"/root/acr-vla-conformal-refinement/logs/eval_object_obs_only_norm03_seed48.json\\\", \\\"checkpoint_path\\\": \\\"N/A (eval only)\\\", \\\"conclusion\\\": \\\"success\\\", \\\"spec\\\": {\\\"command\\\": \\\"eval obs_only CRM epsilon=0.3 seed48 on LIBERO-Object K=10 n_rollouts=10\\\", \\\"server\\\": \\\"bjb1-18228\\\", \\\"data_path\\\": \\\"LIBERO-Object\\\", \\\"data_count\\\": 100, \\\"model_name\\\": \\\"openvla\\\", \\\"seed\\\": 48}, \\\"hypothesis\\\": \\\"CRM with obs_only mode and epsilon=0.3 normalization threshold will improve success rate on LIBERO-Object by filtering unreliable action predictions based solely on observation conformity scores\\\", \\\"completed_at\\\": \\\"2026-05-18T13:27:19.389Z\\\"}, \\\"eval-obs-only-object-norm01-seed48\\\": {\\\"status\\\": \\\"DONE\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-18T11:42:37.233Z\\\", \\\"updated_at\\\": \\\"2026-05-18T11:43:15.403Z\\\", \\\"hypothesis\\\": \\\"obs_only CRM with max_correction_norm=0.1 on LIBERO-Object seed48. Tests whether obs_only mode with conservative norm clipping maintains performance across seeds.\\\", \\\"spec\\\": {\\\"command\\\": \\\"CUDA_VISIBLE_DEVICES=1 /root/miniconda3/bin/python -u src/evaluate.py --mode crm_obs_only --benchmark object --n_rollouts 10 --seed 48 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --max_correction_norm 0.1 --output_file logs/eval_object_obs_only_norm01_seed48.json\\\", \\\"server\\\": \\\"bjb1-18228\\\", \\\"data_path\\\": \\\"LIBERO-Object\\\", \\\"data_count\\\": 100, \\\"model_name\\\": \\\"SmolVLA+CRM_obs_only\\\", \\\"seed\\\": 48, \\\"checkpoint_source\\\": \\\"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\\\", \\\"eval_data\\\": \\\"LIBERO-Object\\\"}, \\\"log_path\\\": \\\"/root/acr-vla-conformal-refinement/logs/eval_object_obs_only_norm01_seed48.json\\\", \\\"checkpoint_path\\\": \\\"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\\\", \\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"success_rate\\\": 0.18, \\\"n_tasks\\\": 10, \\\"n_rollouts\\\": 10, \\\"per_task\\\": {\\\"alphabet_soup\\\": 0, \\\"cream_cheese\\\": 0, \\\"salad_dressing\\\": 0, \\\"bbq_sauce\\\": 0.4, \\\"ketchup\\\": 0.1, \\\"tomato_sauce\\\": 0.2, \\\"butter\\\": 0.2, \\\"milk\\\": 0.3, \\\"chocolate_pudding\\\": 0.3, \\\"orange_juice\\\": 0.3}}, \\\"completed_at\\\": \\\"2026-05-18T11:43:15.403Z\\\"}, \\\"eval-obs-only-object-norm02-k5-seed42\\\": {\\\"status\\\": \\\"DONE\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-18T03:44:47.522Z\\\", \\\"updated_at\\\": \\\"2026-05-18T03:45:04.655Z\\\", \\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"overall_sr\\\": 0.14, \\\"successes\\\": 14, \\\"rollouts\\\": 100, \\\"tasks\\\": 10, \\\"suite\\\": \\\"LIBERO-object\\\", \\\"seed\\\": 42, \\\"method\\\": \\\"crm_obs_only\\\", \\\"K\\\": 5, \\\"max_correction_norm\\\": 0.2}, \\\"hypothesis\\\": \\\"obs_only CRM with K=5 candidates and ε=0.2 on LIBERO-Object seed42. Tests whether fewer candidates (K=5 vs K=10) reduces selection quality. K=5 SR=14% vs K=10 SR=17.5% confirms monotonic improvement with more candidates.\\\", \\\"spec\\\": {\\\"command\\\": \\\"python -u src/evaluate.py --mode crm_obs_only --benchmark object --n_rollouts 10 --seed 42 --K 5 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --max_correction_norm 0.2 --output_file logs/eval_object_obs_only_norm02_k5_seed42.json\\\", \\\"server\\\": \\\"bjb1-18228\\\", \\\"data_path\\\": \\\"LIBERO-Object\\\", \\\"data_count\\\": 100, \\\"model_name\\\": \\\"SmolVLA+CRM_obs_only\\\", \\\"seed\\\": 42, \\\"K\\\": 5, \\\"checkpoint_source\\\": \\\"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\\\", \\\"eval_data\\\": \\\"LIBERO-Object\\\", \\\"checkpoint_path\\\": \\\"N/A\\\", \\\"log_path\\\": \\\"/root/acr-vla-conformal-refinement/logs/eval_object_obs_only_norm02_k5_seed42.json\\\"}, \\\"completed_at\\\": \\\"2026-05-18T03:45:04.655Z\\\"}, \\\"eval-perdof-object-norm01-seed46\\\": {\\\"status\\\": \\\"DONE\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-18T03:05:55.543Z\\\", \\\"updated_at\\\": \\\"2026-05-18T03:06:14.048Z\\\", \\\"hypothesis\\\": \\\"perdof CRM with ε=0.1 on LIBERO-Object seed46. Magnitude curve data point for perdof at intermediate norm. SR=10% confirms perdof degrades from peak at low norms.\\\", \\\"metrics\\\": {\\\"overall_sr\\\": 0.1, \\\"successes\\\": 10, \\\"rollouts\\\": 100, \\\"tasks\\\": 10, \\\"suite\\\": \\\"LIBERO-object\\\", \\\"seed\\\": 46, \\\"method\\\": \\\"crm_perdof\\\", \\\"max_correction_norm\\\": 0.1}, \\\"conclusion\\\": \\\"success\\\", \\\"spec\\\": {\\\"command\\\": \\\"python -u src/evaluate.py --mode crm_perdof --benchmark object --n_rollouts 10 --seed 46 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt --max_correction_norm 0.1 --output_file logs/eval_object_perdof_norm01_seed46.json\\\", \\\"server\\\": \\\"bjb1-32546\\\", \\\"data_path\\\": \\\"LIBERO-Object\\\", \\\"data_count\\\": 100, \\\"model_name\\\": \\\"SmolVLA+CRM_perdof\\\", \\\"seed\\\": 46, \\\"checkpoint_source\\\": \\\"/root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt\\\", \\\"eval_data\\\": \\\"LIBERO-Object\\\", \\\"checkpoint_path\\\": \\\"N/A\\\", \\\"log_path\\\": \\\"/root/acr-vla-conformal-refinement/logs/eval_object_perdof_norm01_seed46.json\\\"}, \\\"completed_at\\\": \\\"2026-05-18T03:06:14.049Z\\\"}, \\\"eval-perdof-object-default-seed46\\\": {\\\"status\\\": \\\"DONE\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-18T03:05:29.784Z\\\", \\\"updated_at\\\": \\\"2026-05-18T03:06:03.735Z\\\", \\\"conclusion\\\": \\\"negative\\\", \\\"hypothesis\\\": \\\"perdof CRM without norm constraint (uncapped correction magnitude) on LIBERO-Object seed46. Tests whether perdof maintains performance without explicit correction capping. SR=0% confirms perdof corrections are catastrophically unstable without norm constraints.\\\", \\\"spec\\\": {\\\"command\\\": \\\"python -u src/evaluate.py --mode crm_perdof --benchmark object --n_rollouts 10 --seed 46 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt --output_file logs/eval_object_perdof_default_seed46.json\\\", \\\"server\\\": \\\"bjb1-32546\\\", \\\"data_path\\\": \\\"LIBERO-Object\\\", \\\"data_count\\\": 100, \\\"model_name\\\": \\\"SmolVLA+CRM_perdof\\\", \\\"seed\\\": 46, \\\"checkpoint_source\\\": \\\"/root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt\\\", \\\"eval_data\\\": \\\"LIBERO-Object\\\", \\\"checkpoint_path\\\": \\\"N/A\\\", \\\"log_path\\\": \\\"/root/acr-vla-conformal-refinement/logs/eval_object_perdof_default_seed46.json\\\"}, \\\"metrics\\\": {\\\"overall_sr\\\": 0, \\\"successes\\\": 0, \\\"rollouts\\\": 100, \\\"tasks\\\": 10, \\\"suite\\\": \\\"LIBERO-object\\\", \\\"seed\\\": 46, \\\"method\\\": \\\"crm_perdof\\\", \\\"max_correction_norm\\\": \\\"default\\\"}, \\\"completed_at\\\": \\\"2026-05-18T03:06:03.735Z\\\"}, \\\"eval-perdof-object-norm02-seed48\\\": {\\\"status\\\": \\\"RUNNING\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-18T03:05:29.433Z\\\", \\\"updated_at\\\": \\\"2026-05-18T03:05:47.075Z\\\", \\\"hypothesis\\\": \\\"perdof CRM with ε=0.2 on LIBERO-Object seed48. Additional seed for perdof magnitude curve at primary comparison norm. Running on bjb2-28827 cuda:5 PID 488665.\\\", \\\"spec\\\": {\\\"command\\\": \\\"cd /root/acr-vla-conformal-refinement && CUDA_VISIBLE_DEVICES=5 python -u src/evaluate.py --mode crm_perdof --benchmark object --n_rollouts 10 --seed 48 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt --max_correction_norm 0.2 --output_file logs/eval_object_perdof_norm02_seed48.json\\\", \\\"server\\\": \\\"bjb2-28827\\\", \\\"data_path\\\": \\\"LIBERO-Object\\\", \\\"data_count\\\": 100, \\\"model_name\\\": \\\"SmolVLA+CRM_perdof\\\", \\\"seed\\\": 48, \\\"checkpoint_source\\\": \\\"/root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt\\\", \\\"eval_data\\\": \\\"LIBERO-Object\\\"}}, \\\"eval-obs-only-object-default-seed46\\\": {\\\"status\\\": \\\"DONE\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-18T00:59:50.348Z\\\", \\\"updated_at\\\": \\\"2026-05-18T01:00:23.165Z\\\", \\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"overall_sr\\\": 0.15, \\\"successes\\\": 15, \\\"rollouts\\\": 100, \\\"tasks\\\": 10, \\\"suite\\\": \\\"LIBERO-object\\\", \\\"seed\\\": 46, \\\"method\\\": \\\"crm_obs_only\\\", \\\"max_correction_norm\\\": \\\"default\\\", \\\"per_task_sr\\\": {\\\"alphabet_soup\\\": 0, \\\"cream_cheese\\\": 0, \\\"salad_dressing\\\": 0.2, \\\"bbq_sauce\\\": 0.4, \\\"ketchup\\\": 0.1, \\\"tomato_sauce\\\": 0.1, \\\"butter\\\": 0.1, \\\"milk\\\": 0.1, \\\"chocolate_pudding\\\": 0.2, \\\"orange_juice\\\": 0.3}}, \\\"spec\\\": {\\\"checkpoint_path\\\": \\\"N/A\\\", \\\"log_path\\\": \\\"/root/acr-vla-conformal-refinement/logs/eval_object_obs_only_default_seed46.json\\\", \\\"command\\\": \\\"python -u src/evaluate.py --mode crm_obs_only --benchmark object --n_rollouts 10 --seed 46 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --output_file logs/eval_object_obs_only_default_seed46.json\\\", \\\"server\\\": \\\"bjb1-32546\\\", \\\"data_path\\\": \\\"LIBERO-Object\\\", \\\"data_count\\\": 100, \\\"model_name\\\": \\\"SmolVLA+CRM_obs_only\\\", \\\"seed\\\": 46, \\\"checkpoint_source\\\": \\\"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\\\", \\\"eval_data\\\": \\\"LIBERO-Object\\\"}, \\\"hypothesis\\\": \\\"obs_only CRM without norm constraint (uncapped correction magnitude) on LIBERO-Object seed46. Tests whether obs_only maintains performance without explicit correction capping. If uncapped performs worse than capped, it confirms that moderate norm constraints stabilize corrections.\\\", \\\"completed_at\\\": \\\"2026-05-18T01:00:23.165Z\\\"}, \\\"eval-obs-only-object-norm01-seed46\\\": {\\\"status\\\": \\\"DONE\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-18T00:42:56.715Z\\\", \\\"updated_at\\\": \\\"2026-05-18T00:43:09.191Z\\\", \\\"conclusion\\\": \\\"killed\\\", \\\"completed_at\\\": \\\"2026-05-18T00:43:09.191Z\\\"}, \\\"eval-k1-crm-multiscale-object-seed43\\\": {\\\"status\\\": \\\"DONE\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-17T21:05:23.402Z\\\", \\\"updated_at\\\": \\\"2026-05-17T21:06:09.004Z\\\", \\\"hypothesis\\\": \\\"Multi-scale K=1 CRM with accumulated gradient refinement improves object manipulation success rate over baseline by providing conformal prediction-based action corrections at multiple spatial scales\\\", \\\"spec\\\": {\\\"command\\\": \\\"python -u src/evaluate.py --mode crm_k1_accg --benchmark object --n_rollouts 10 --seed 43\\\", \\\"server\\\": \\\"bjb1-32546\\\", \\\"data_path\\\": \\\"LIBERO-Object\\\", \\\"data_count\\\": 100, \\\"model_name\\\": \\\"SmolVLA+CRM_k1_accg\\\", \\\"seed\\\": 43, \\\"checkpoint_source\\\": \\\"crm_v3_norm\\\", \\\"eval_data\\\": \\\"LIBERO-Object\\\", \\\"checkpoint_path\\\": \\\"N/A\\\", \\\"log_path\\\": \\\"/root/acr-vla-conformal-refinement/logs/eval_k1_crm_multiscale_object_seed43.json\\\"}, \\\"conclusion\\\": \\\"negative\\\", \\\"metrics\\\": {\\\"overall_sr\\\": 0.09, \\\"successes\\\": 9, \\\"rollouts\\\": 100, \\\"tasks\\\": 10, \\\"suite\\\": \\\"LIBERO-object\\\", \\\"seed\\\": 43, \\\"method\\\": \\\"crm_k1_accg\\\", \\\"per_task\\\": {\\\"alphabet_soup\\\": 0, \\\"cream_cheese\\\": 0, \\\"salad_dressing\\\": 0.1, \\\"bbq_sauce\\\": 0.2, \\\"ketchup\\\": 0, \\\"tomato_sauce\\\": 0.2, \\\"butter\\\": 0, \\\"milk\\\": 0, \\\"chocolate_pudding\\\": 0.2, \\\"orange_juice\\\": 0.2}}, \\\"completed_at\\\": \\\"2026-05-17T21:06:09.004Z\\\"}, \\\"eval-k1-crm-multiscale-object-seed42\\\": {\\\"status\\\": \\\"DONE\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-17T21:05:22.835Z\\\", \\\"updated_at\\\": \\\"2026-05-17T21:06:08.318Z\\\", \\\"hypothesis\\\": \\\"Multi-scale K=1 CRM with accumulated gradient refinement improves object manipulation success rate over baseline by providing conformal prediction-based action corrections at multiple spatial scales\\\", \\\"spec\\\": {\\\"command\\\": \\\"python -u src/evaluate.py --mode crm_k1_accg --benchmark object --n_rollouts 10 --seed 42\\\", \\\"server\\\": \\\"bjb2-28827\\\", \\\"data_path\\\": \\\"LIBERO-Object\\\", \\\"data_count\\\": 100, \\\"model_name\\\": \\\"SmolVLA+CRM_k1_accg\\\", \\\"seed\\\": 42, \\\"checkpoint_source\\\": \\\"crm_v3_norm\\\", \\\"eval_data\\\": \\\"LIBERO-Object\\\", \\\"checkpoint_path\\\": \\\"N/A\\\", \\\"log_path\\\": \\\"/root/acr-vla-conformal-refinement/logs/eval_k1_crm_multiscale_object_seed42.json\\\"}, \\\"conclusion\\\": \\\"negative\\\", \\\"metrics\\\": {\\\"overall_sr\\\": 0.12, \\\"successes\\\": 12, \\\"rollouts\\\": 100, \\\"tasks\\\": 10, \\\"suite\\\": \\\"LIBERO-object\\\", \\\"seed\\\": 42, \\\"method\\\": \\\"crm_k1_accg\\\", \\\"per_task\\\": {\\\"alphabet_soup\\\": 0, \\\"cream_cheese\\\": 0, \\\"salad_dressing\\\": 0.1, \\\"bbq_sauce\\\": 0.2, \\\"ketchup\\\": 0, \\\"tomato_sauce\\\": 0.3, \\\"butter\\\": 0.1, \\\"milk\\\": 0, \\\"chocolate_pudding\\\": 0.3, \\\"orange_juice\\\": 0.2}}, \\\"completed_at\\\": \\\"2026-05-17T21:06:08.318Z\\\"}, \\\"eval-obs-only-object-norm005-seed43\\\": {\\\"status\\\": \\\"RUNNING\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-17T21:04:43.285Z\\\", \\\"updated_at\\\": \\\"2026-05-17T21:04:52.760Z\\\", \\\"spec\\\": {\\\"command\\\": \\\"CUDA_VISIBLE_DEVICES=0 python -u src/evaluate.py --mode crm_obs_only --benchmark object --n_rollouts 10 --seed 43 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --max_correction_norm 0.05 --output_file logs/eval_object_obs_only_norm005_seed43.json\\\", \\\"server\\\": \\\"bjb2-28827\\\", \\\"data_path\\\": \\\"LIBERO-Object\\\", \\\"data_count\\\": 100, \\\"model_name\\\": \\\"SmolVLA+CRM_obs_only\\\", \\\"seed\\\": 43, \\\"checkpoint_source\\\": \\\"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\\\", \\\"eval_data\\\": \\\"LIBERO-Object\\\"}}, \\\"eval-perdof-object-norm02-seed45-r3\\\": {\\\"status\\\": \\\"RUNNING\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-17T21:02:26.375Z\\\", \\\"updated_at\\\": \\\"2026-05-17T21:04:50.614Z\\\", \\\"hypothesis\\\": \\\"perdof CRM (ε=0.2) seed45 on LIBERO-Object. Rerun after SIGHUP kill. Original result on bjb2-28827 was 9%. This confirms reproducibility on different server.\\\", \\\"spec\\\": {\\\"command\\\": \\\"CUDA_VISIBLE_DEVICES=3 python -u src/evaluate.py --mode crm_perdof --benchmark object --n_rollouts 10 --seed 45 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt --max_correction_norm 0.2 --output_file logs/eval_object_perdof_norm02_seed45_r3.json\\\", \\\"server\\\": \\\"bjb1-18228\\\", \\\"data_path\\\": \\\"LIBERO-Object\\\", \\\"data_count\\\": 100, \\\"model_name\\\": \\\"SmolVLA+CRM_perdof\\\", \\\"seed\\\": 45, \\\"checkpoint_source\\\": \\\"/root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt\\\", \\\"eval_data\\\": \\\"LIBERO-Object\\\"}}, \\\"eval-k1-crm-multiscale-object-seed44-r2\\\": {\\\"status\\\": \\\"DONE\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-17T20:55:44.755Z\\\", \\\"updated_at\\\": \\\"2026-05-17T20:56:16.602Z\\\", \\\"hypothesis\\\": \\\"Multi-scale K=1 CRM with accumulated gradient refinement improves object manipulation success rate over baseline by providing conformal prediction-based action corrections at multiple spatial scales\\\", \\\"spec\\\": {\\\"command\\\": \\\"python eval_libero.py --method crm_k1_accg --baseline_mode single --suite object --seed 44 --n_rollouts 10\\\", \\\"server\\\": \\\"bjb1-18228\\\", \\\"data_path\\\": \\\"LIBERO-object\\\", \\\"data_count\\\": 100, \\\"model_name\\\": \\\"crm_k1_multiscale\\\", \\\"seed\\\": 44, \\\"checkpoint_source\\\": \\\"crm-k1-train\\\", \\\"eval_data\\\": \\\"LIBERO-object\\\"}, \\\"checkpoint_path\\\": \\\"/root/autodl-tmp/checkpoints/crm_k1/crm_k1_best.pt\\\", \\\"log_path\\\": \\\"/root/acr-vla-conformal-refinement/logs/eval_k1_crm_multiscale_object_seed44_bjb1-18228.json\\\", \\\"conclusion\\\": \\\"negative\\\", \\\"completed_at\\\": \\\"2026-05-17T20:56:12.165Z\\\", \\\"metrics\\\": {\\\"overall_sr\\\": 0.1, \\\"successes\\\": 10, \\\"rollouts\\\": 100, \\\"tasks\\\": 10, \\\"suite\\\": \\\"LIBERO-object\\\", \\\"seed\\\": 44, \\\"method\\\": \\\"crm_k1_accg\\\", \\\"per_task\\\": {\\\"alphabet_soup\\\": 0, \\\"cream_cheese\\\": 0, \\\"salad_dressing\\\": 0.2, \\\"bbq_sauce\\\": 0.1, \\\"ketchup\\\": 0, \\\"tomato_sauce\\\": 0.1, \\\"butter\\\": 0, \\\"milk\\\": 0, \\\"chocolate_pudding\\\": 0.4, \\\"orange_juice\\\": 0.2}}}, \\\"eval-mag-perdof-norm03-object-r3\\\": {\\\"status\\\": \\\"DONE\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-16T11:05:32.773Z\\\", \\\"updated_at\\\": \\\"2026-05-16T11:06:06.108Z\\\", \\\"conclusion\\\": \\\"success\\\", \\\"spec\\\": {\\\"command\\\": \\\"python eval_libero.py --method crm_perdof --suite object --norm 0.3 --seed 42\\\", \\\"server\\\": \\\"bjb2-28827\\\", \\\"data_path\\\": \\\"LIBERO-object\\\", \\\"data_count\\\": 100, \\\"model_name\\\": \\\"crm_perdof_norm03\\\", \\\"seed\\\": 42, \\\"checkpoint_source\\\": \\\"crm-train-v3-perdof\\\", \\\"eval_data\\\": \\\"LIBERO-object\\\"}, \\\"log_path\\\": \\\"/root/acr-vla-conformal-refinement/logs/eval_object_perdof_norm03_r3.json\\\", \\\"checkpoint_path\\\": \\\"N/A\\\", \\\"completed_at\\\": \\\"2026-05-16T11:06:02.462Z\\\", \\\"metrics\\\": {\\\"success_rate\\\": 0.04, \\\"successes\\\": 4, \\\"rollouts\\\": 100, \\\"tasks\\\": 10, \\\"suite\\\": \\\"LIBERO-object\\\", \\\"norm\\\": 0.3, \\\"seed\\\": 42}}, \\\"eval-mag-perdof-norm005-object\\\": {\\\"status\\\": \\\"DONE\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-16T08:30:31.627Z\\\", \\\"updated_at\\\": \\\"2026-05-16T08:30:52.155Z\\\", \\\"spec\\\": {\\\"command\\\": \\\"python evaluate.py --mode crm_perdof --benchmark object --max_correction_norm 0.05 --seed 42\\\", \\\"server\\\": \\\"bjb2-28827\\\", \\\"data_path\\\": \\\"/root/acr-vla-conformal-refinement/logs/eval_object_perdof_norm005.json\\\", \\\"data_count\\\": 100, \\\"model_name\\\": \\\"crm_v3_norm_perdof\\\", \\\"seed\\\": 42, \\\"checkpoint_source\\\": \\\"/root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt\\\", \\\"eval_data\\\": \\\"LIBERO object benchmark\\\"}, \\\"conclusion\\\": \\\"negative\\\", \\\"checkpoint_path\\\": \\\"/root/acr-vla-conformal-refinement/logs/eval_object_perdof_norm005.json\\\", \\\"log_path\\\": \\\"/root/acr-vla-conformal-refinement/logs/nohup_eval_object_perdof_norm005.log\\\", \\\"completed_at\\\": \\\"2026-05-16T08:30:50.635Z\\\", \\\"metrics\\\": {\\\"overall_sr\\\": 0.14, \\\"per_task\\\": {\\\"alphabet_soup\\\": 0, \\\"cream_cheese\\\": 0, \\\"salad_dressing\\\": 0.2, \\\"bbq_sauce\\\": 0.4, \\\"ketchup\\\": 0, \\\"tomato_sauce\\\": 0, \\\"butter\\\": 0, \\\"milk\\\": 0.2, \\\"chocolate_pudding\\\": 0.4, \\\"orange_juice\\\": 0.2}}}, \\\"eval-mag-obsonly-norm03-object\\\": {\\\"status\\\": \\\"DONE\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-16T07:41:31.617Z\\\", \\\"updated_at\\\": \\\"2026-05-16T07:41:53.597Z\\\", \\\"metrics\\\": {\\\"tasks_done\\\": 10, \\\"tasks_total\\\": 10, \\\"overall_sr\\\": 0.19, \\\"per_task_sr\\\": {\\\"alphabet_soup\\\": 0, \\\"cream_cheese\\\": 0, \\\"salad_dressing\\\": 0.3, \\\"bbq_sauce\\\": 0.3, \\\"ketchup\\\": 0, \\\"tomato_sauce\\\": 0.1, \\\"butter\\\": 0.2, \\\"milk\\\": 0.2, \\\"chocolate_pudding\\\": 0.5, \\\"orange_juice\\\": 0.3}}, \\\"checkpoint_path\\\": \\\"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\\\", \\\"log_path\\\": \\\"/root/acr-vla-conformal-refinement/logs/eval_object_obs_only_norm03.log\\\", \\\"conclusion\\\": \\\"success\\\", \\\"completed_at\\\": \\\"2026-05-16T07:41:53.597Z\\\"}}, \\\"count\\\": 64, \\\"total\\\": 64, \\\"baseline\\\": null}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.1861}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"experiments\": {\"eval-obs-only-object-norm005-seed75\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-21T02:56:05.523Z\", \"updated_at\": \"2026-05-21T02:56:12.611Z\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.15}}, \"eval-obs-only-object-norm01-seed74\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-21T02:55:20.812Z\", \"updated_at\": \"2026-05-21T02:55:28.975Z\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.13}}, \"eval-obs-only-object-norm01-seed64\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-21T02:54:30.053Z\", \"updated_at\": \"2026-05-21T02:54:30.754Z\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.15}}, \"eval-obs-only-object-norm003-seed73\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-21T02:53:26.508Z\", \"updated_at\": \"2026-05-21T02:53:31.930Z\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.16}}, \"eval-obs-only-object-norm005-seed64\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-21T02:52:33.605Z\", \"updated_at\": \"2026-05-21T02:52:37.242Z\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.15}}, \"eval-obs-only-object-norm003-seed65\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-21T02:51:17.482Z\", \"updated_at\": \"2026-05-21T02:51:23.912Z\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.17}}, \"eval-obs-only-object-norm003-seed64\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-21T02:51:17.026Z\", \"updated_at\": \"2026-05-21T02:51:23.446Z\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.17}}, \"eval-obs-only-object-norm003-seed63-r2\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-21T02:51:19.045Z\", \"updated_at\": \"2026-05-21T02:51:19.046Z\", \"conclusion\": \"killed\"}, \"eval-obs-only-object-norm003-seed62-r2\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-21T02:51:18.497Z\", \"updated_at\": \"2026-05-21T02:51:18.497Z\", \"conclusion\": \"killed\"}, \"eval-obs-only-object-norm005-seed65\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-21T02:26:45.708Z\", \"updated_at\": \"2026-05-21T02:26:50.866Z\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.14}}, \"eval-obs-only-object-norm005-seed61\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-21T01:54:41.975Z\", \"updated_at\": \"2026-05-21T01:54:46.787Z\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.15}}, \"eval-obs-only-object-norm01-seed60\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-21T01:42:15.142Z\", \"updated_at\": \"2026-05-21T01:42:24.178Z\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.15}}, \"eval-obs-only-object-norm003-seed56\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-21T01:42:14.531Z\", \"updated_at\": \"2026-05-21T01:42:23.974Z\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.15}}, \"eval-obs-only-object-norm01-seed66\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-21T01:29:23.112Z\", \"updated_at\": \"2026-05-21T01:31:28.961Z\", \"pid\": 642775}, \"eval-obs-only-object-norm005-seed66\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-21T01:29:22.550Z\", \"updated_at\": \"2026-05-21T01:31:28.635Z\", \"pid\": 642506}, \"eval-obs-only-object-norm003-seed66\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-21T01:29:22.063Z\", \"updated_at\": \"2026-05-21T01:31:27.799Z\", \"pid\": 642428}, \"eval-obs-only-object-norm003-seed59\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-21T01:23:09.866Z\", \"updated_at\": \"2026-05-21T01:23:22.549Z\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.13}}, \"eval-obs-only-object-norm005-seed58\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-21T01:23:09.469Z\", \"updated_at\": \"2026-05-21T01:23:21.948Z\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.16}}, \"eval-obs-only-object-norm01-seed57\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-21T01:23:08.871Z\", \"updated_at\": \"2026-05-21T01:23:21.444Z\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.19}}, \"eval-obs-only-object-norm005-seed63\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-21T01:02:30.561Z\", \"updated_at\": \"2026-05-21T01:02:30.561Z\", \"conclusion\": \"killed\"}, \"eval-obs-only-object-norm005-seed62\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-21T01:02:30.354Z\", \"updated_at\": \"2026-05-21T01:02:30.354Z\", \"conclusion\": \"killed\"}, \"eval-perdof-object-norm02-seed49\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-20T15:59:12.635Z\", \"updated_at\": \"2026-05-20T15:59:54.757Z\", \"metrics\": {\"overall_success_rate\": 0.12, \"total_rollouts\": 100, \"total_successes\": 12, \"per_task_sr\": {\"alphabet_soup\": 0, \"cream_cheese\": 0, \"salad_dressing\": 0.1, \"bbq_sauce\": 0.2, \"ketchup\": 0, \"tomato_sauce\": 0, \"butter\": 0.1, \"milk\": 0.2, \"chocolate_pudding\": 0.4, \"orange_juice\": 0.2}}, \"log_path\": \"/root/acr-vla-conformal-refinement/logs/eval-perdof-object-norm02-seed49.log\", \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt\", \"spec\": {\"command\": \"python evaluate.py --mode crm_perdof --benchmark object --seed 49 --K 10 --max_correction_norm 0.2 --n_rollouts 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt --output_file logs/eval_perdof_object_norm02_seed49.json\", \"server\": \"bjb1-32546\", \"data_path\": \"LIBERO-Object\", \"data_count\": 100, \"model_name\": \"crm_perdof_norm02_K10\", \"seed\": 49, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt\", \"eval_data\": \"LIBERO-Object\"}, \"hypothesis\": \"PerDoF CRM with norm-clipped corrections (epsilon=0.2, K=10) provides consistent improvement over baseline on LIBERO-Object across seeds; seed49 should yield SR in the 14-18% range consistent with seeds 43-48.\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-20T15:59:54.757Z\"}, \"eval-obs-only-object-norm02-seed43-r3\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-20T13:55:56.411Z\", \"updated_at\": \"2026-05-20T13:55:57.571Z\", \"conclusion\": \"failed\", \"failure_reason\": \"SIGHUP (tmux session terminated externally) at 8/10 tasks. No JSON output. r2 already has complete data (SR=16%), no retry needed.\"}, \"openvla-precompute-k1\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-20T13:52:53.282Z\", \"updated_at\": \"2026-05-20T13:52:53.282Z\", \"notes\": \"GPU collision: cuda:3 被 Director P0-B 指令分配给 plan_702 seed43。预计算需要在 plan_702 完成后重启。原始提交: PID 365142, 处理 74507 timesteps from 500 demos. Output: /root/autodl-tmp/crm_cache_k1_openvla/object/. 特征维度: multi_scale_obs (4,4096), action_dim=6.\"}, \"eval-obs-only-goal-norm02-seed52\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-20T12:05:20.840Z\", \"updated_at\": \"2026-05-20T12:58:35.610Z\", \"spec\": {\"command\": \"python -u src/evaluate.py --mode crm_obs_only --benchmark LIBERO-Goal --seed 52 --n_rollouts 10 --max_correction_norm 0.2\", \"server\": \"bjb1-32546\", \"gpu\": \"cuda:0\", \"pid\": 362579, \"data_path\": \"LIBERO-Goal\", \"data_count\": \"10 tasks x 10 rollouts\", \"model_name\": \"openvla-7b + CRM obs_only\", \"seed\": 52, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\", \"eval_data\": \"LIBERO-Goal (10 tasks x 10 rollouts)\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-obs-only-goal-norm02-seed52.log\", \"checkpoint_path\": \"N/A (eval only)\"}, \"metrics\": {\"success_rate\": 0.68, \"successes\": 68, \"total\": 100, \"per_task_sr\": {\"open_middle_drawer_cabinet\": 0.7, \"put_bowl_on_stove\": 0.9, \"put_wine_bottle_on_cabinet\": 0.4, \"open_top_drawer_put_bowl\": 0.3, \"put_bowl_on_cabinet\": 0.8, \"push_plate_front_stove\": 0.8, \"put_cream_cheese_in_bowl\": 0.4, \"turn_on_stove\": 1, \"put_bowl_on_plate\": 1, \"put_wine_bottle_on_rack\": 0.5}}, \"conclusion\": \"success\", \"hypothesis\": \"CRM obs_only with K=10 and norm cap 0.2 improves SR on LIBERO-Goal by applying observation-conditioned corrections that compensate for VLA action prediction errors, providing a new seed for variance estimation.\", \"completed_at\": \"2026-05-20T12:58:26.417Z\", \"notes\": \"SR=68% on Goal seed52. Strong result; turn_on_stove and put_bowl_on_plate both 100%.\"}, \"eval-argmin-object-seed49\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-20T12:05:22.690Z\", \"updated_at\": \"2026-05-20T12:58:34.569Z\", \"spec\": {\"command\": \"python -u src/evaluate.py --mode reconvla --benchmark LIBERO-Object --seed 49 --n_rollouts 10\", \"server\": \"bjb1-32546\", \"gpu\": \"cuda:5\", \"pid\": 364591, \"data_path\": \"LIBERO-Object\", \"data_count\": \"10 tasks x 10 rollouts\", \"model_name\": \"openvla-7b + CRM obs_only (argmin)\", \"seed\": 49, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\", \"eval_data\": \"LIBERO-Object (10 tasks x 10 rollouts)\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-argmin-object-seed49.log\", \"checkpoint_path\": \"N/A (eval only)\"}, \"metrics\": {\"success_rate\": 0.16, \"successes\": 16, \"total\": 100, \"per_task_sr\": {\"alphabet_soup\": 0, \"cream_cheese\": 0, \"salad_dressing\": 0.2, \"bbq_sauce\": 0.4, \"ketchup\": 0, \"tomato_sauce\": 0.1, \"butter\": 0.1, \"milk\": 0.3, \"chocolate_pudding\": 0.3, \"orange_juice\": 0.2}}, \"conclusion\": \"success\", \"hypothesis\": \"Argmin (reconvla) selection among K=10 CRM refinements improves over single-step VLA on Object by choosing the candidate with lowest predicted residual, providing a multi-seed consistency check.\", \"completed_at\": \"2026-05-20T12:58:25.905Z\", \"notes\": \"SR=16% on Object seed49. Consistent with other argmin seeds on Object benchmark.\"}, \"eval-random-selection-spatial-seed43\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-20T12:05:19.438Z\", \"updated_at\": \"2026-05-20T12:58:33.167Z\", \"spec\": {\"command\": \"python -u src/evaluate.py --mode random_selection --benchmark LIBERO-Spatial --seed 43 --n_rollouts 10\", \"server\": \"bjb1-18228\", \"gpu\": \"cuda:1\", \"pid\": 347075, \"data_path\": \"LIBERO-Spatial\", \"data_count\": \"10 tasks x 10 rollouts\", \"model_name\": \"openvla-7b + CRM obs_only\", \"seed\": 43, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\", \"eval_data\": \"LIBERO-Spatial (10 tasks x 10 rollouts)\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-random-selection-spatial-seed43.log\", \"checkpoint_path\": \"N/A (eval only)\"}, \"metrics\": {\"success_rate\": 0.26, \"successes\": 26, \"total\": 100, \"per_task_sr\": {\"between_plate_ramekin\": 0.7, \"next_to_ramekin\": 0.9, \"table_center\": 0, \"cookie_box\": 0.1, \"top_drawer\": 0, \"on_ramekin\": 0, \"next_to_cookie_box\": 0.7, \"on_stove\": 0, \"next_to_plate\": 0.2, \"on_wooden_cabinet\": 0}}, \"conclusion\": \"success\", \"hypothesis\": \"Random candidate selection from K=10 CRM refinements serves as a lower-bound baseline, showing that informed selection (argmin) is necessary to achieve the full benefit of multi-step refinement on Spatial.\", \"completed_at\": \"2026-05-20T12:58:24.969Z\", \"notes\": \"SR=26% on Spatial seed43. Lower than argmin-based selection, confirming informed selection matters.\"}, \"eval-adaptive-k-spatial-p90-seed43\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-20T10:52:06.660Z\", \"updated_at\": \"2026-05-20T12:58:31.849Z\", \"spec\": {\"command\": \"python -u src/evaluate.py --mode adaptive_k --benchmark LIBERO-Spatial --seed 43 --n_rollouts 10 --adaptive_k_threshold 0.125870 --output_file logs/eval-adaptive-k-spatial-p90-seed43.json\", \"server\": \"bjb1-18228\", \"gpu\": \"cuda:3\", \"pid\": 344852, \"data_path\": \"LIBERO-Spatial\", \"data_count\": \"10 tasks x 10 rollouts\", \"model_name\": \"openvla-7b + CRM obs_only\", \"seed\": 43, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\", \"eval_data\": \"LIBERO-Spatial (10 tasks x 10 rollouts)\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-adaptive-k-spatial-p90-seed43.log\", \"checkpoint_path\": \"N/A (eval only)\"}, \"metrics\": {\"success_rate\": 0.32, \"successes\": 32, \"total\": 100, \"avg_K\": 3.6, \"fast_path_pct\": 80.2, \"mean_l2\": 0.0905, \"per_task_sr\": {\"between_plate_ramekin\": 0.7, \"next_to_ramekin\": 1, \"table_center\": 0.1, \"cookie_box\": 0.3, \"top_drawer\": 0, \"on_ramekin\": 0.1, \"next_to_cookie_box\": 0.8, \"on_stove\": 0, \"next_to_plate\": 0.2, \"on_wooden_cabinet\": 0}}, \"conclusion\": \"success\", \"hypothesis\": \"Adaptive K with P90 threshold (τ=0.1259) reduces average refinement steps while maintaining comparable SR to fixed K=10 on Spatial, because most states have low CRM residuals and can skip full refinement.\", \"completed_at\": \"2026-05-20T12:58:23.572Z\", \"notes\": \"SR=32%, avg_K=3.6 (vs fixed K=10), 80.2% fast-path. Adaptive K saves ~64% compute with seed43 on Spatial.\"}, \"eval-adaptive-k-object-p90-seed44\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-20T12:45:08.564Z\", \"updated_at\": \"2026-05-20T12:45:37.089Z\", \"hypothesis\": \"Adaptive K with τ=P90 (0.125870) on LIBERO-Object seed44. P90 是最宽松的阈值——大部分 step fast-path (K=1)，仅在极高不确定性时用 K=10。验证 P90 在 Object 上的 SR/compute tradeoff。\", \"spec\": {\"command\": \"python -u src/evaluate.py --mode adaptive_k --benchmark LIBERO-Object --seed 44 --n_rollouts 10 --adaptive_k_threshold 0.125870\", \"server\": \"bjb2-28827\", \"data_path\": \"LIBERO-Object\", \"data_count\": \"10 tasks x 10 rollouts\", \"model_name\": \"openvla-7b + CRM obs_only\", \"seed\": 44, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\", \"eval_data\": \"LIBERO-Object (10 tasks x 10 rollouts)\", \"log_path\": \"N/A (discovered by Reviewer)\", \"checkpoint_path\": \"N/A (eval only)\"}, \"metrics\": {\"sr\": 14, \"avg_K\": 2.58, \"fast_path_pct\": 92.8, \"total_rollouts\": 100}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-20T12:45:37.089Z\"}, \"eval-adaptive-k-object-p90-seed43\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-20T12:45:08.312Z\", \"updated_at\": \"2026-05-20T12:45:34.700Z\", \"hypothesis\": \"Adaptive K with τ=P90 (0.125870) on LIBERO-Object seed43. P90 是最宽松的阈值——大部分 step fast-path (K=1)，仅在极高不确定性时用 K=10。验证 P90 在 Object 上的 SR/compute tradeoff。\", \"spec\": {\"command\": \"python -u src/evaluate.py --mode adaptive_k --benchmark LIBERO-Object --seed 43 --n_rollouts 10 --adaptive_k_threshold 0.125870\", \"server\": \"bjb2-28827\", \"data_path\": \"LIBERO-Object\", \"data_count\": \"10 tasks x 10 rollouts\", \"model_name\": \"openvla-7b + CRM obs_only\", \"seed\": 43, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\", \"eval_data\": \"LIBERO-Object (10 tasks x 10 rollouts)\", \"log_path\": \"N/A (discovered by Reviewer)\", \"checkpoint_path\": \"N/A (eval only)\"}, \"metrics\": {\"sr\": 14, \"avg_K\": 2.61, \"fast_path_pct\": 92.3, \"total_rollouts\": 100}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-20T12:45:34.700Z\"}, \"eval-argmin-object-seed48\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-20T12:05:22.501Z\", \"updated_at\": \"2026-05-20T12:05:49.680Z\", \"spec\": {\"command\": \"python -u src/evaluate.py --mode reconvla --benchmark LIBERO-Object --seed 48 --n_rollouts 10\", \"server\": \"bjb1-32546\", \"gpu\": \"cuda:4\", \"pid\": 364125, \"data_path\": \"LIBERO-Object\", \"data_count\": \"10 tasks x 10 rollouts\", \"model_name\": \"openvla-7b + CRM obs_only (argmin)\", \"seed\": 48, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\", \"eval_data\": \"LIBERO-Object (10 tasks x 10 rollouts)\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-argmin-object-seed48.log\"}}, \"eval-obs-only-object-norm02-seed49\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-20T12:05:21.387Z\", \"updated_at\": \"2026-05-20T12:05:49.425Z\", \"spec\": {\"command\": \"python -u src/evaluate.py --mode crm_obs_only --benchmark LIBERO-Object --seed 49 --n_rollouts 10 --max_correction_norm 0.2\", \"server\": \"bjb1-32546\", \"gpu\": \"cuda:3\", \"pid\": 363783, \"data_path\": \"LIBERO-Object\", \"data_count\": \"10 tasks x 10 rollouts\", \"model_name\": \"openvla-7b + CRM obs_only\", \"seed\": 49, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\", \"eval_data\": \"LIBERO-Object (10 tasks x 10 rollouts)\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-obs-only-object-norm02-seed49.log\"}}, \"eval-random-selection-spatial-seed44\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-20T12:05:19.931Z\", \"updated_at\": \"2026-05-20T12:05:41.684Z\", \"spec\": {\"command\": \"python -u src/evaluate.py --mode random_selection --benchmark LIBERO-Spatial --seed 44 --n_rollouts 10\", \"server\": \"bjb1-18228\", \"gpu\": \"cuda:2\", \"pid\": 348897, \"data_path\": \"LIBERO-Spatial\", \"data_count\": \"10 tasks x 10 rollouts\", \"model_name\": \"openvla-7b + CRM obs_only\", \"seed\": 44, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\", \"eval_data\": \"LIBERO-Spatial (10 tasks x 10 rollouts)\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-random-selection-spatial-seed44.log\"}}, \"eval-random-selection-spatial-seed42\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-20T10:52:07.011Z\", \"updated_at\": \"2026-05-20T12:04:59.708Z\", \"spec\": {\"command\": \"python -u src/evaluate.py --mode random_selection --benchmark LIBERO-Spatial --seed 42 --n_rollouts 10\", \"server\": \"bjb1-18228\", \"gpu\": \"cuda:0\", \"pid\": 346801, \"data_path\": \"LIBERO-Spatial\", \"data_count\": \"10 tasks x 10 rollouts\", \"model_name\": \"openvla-7b + CRM obs_only\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\", \"eval_data\": \"LIBERO-Spatial (10 tasks x 10 rollouts)\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-random-selection-spatial-seed42.log\"}, \"notes\": \"原 bjb1-32546 上的重复副本(PID 360293/360306)已 kill。此实验实际在 bjb1-18228:cuda:0 运行(PID 346801, mass-deploy 部署)。\"}, \"eval-adaptive-k-spatial-p50-seed42\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-20T11:24:12.894Z\", \"updated_at\": \"2026-05-20T11:25:16.991Z\", \"conclusion\": \"success\", \"metrics\": {\"sr\": 30, \"avg_K\": 6.324, \"fast_path_pct\": 45.95, \"mean_l2\": 0.0903, \"total_rollouts\": 100}, \"failure_reason\": \"\", \"completed_at\": \"2026-05-20T11:06:00.000Z\", \"notes\": \"Reviewer 独立验证：JSON 完整，日志确认 SR=30%，PID 自然退出。之前被 cron 误判为 failed（PID dead + 无 sentinel），已修正为 success。\", \"spec\": {\"command\": \"python -u src/evaluate.py --mode adaptive_k --benchmark LIBERO-Spatial --seed 42 --n_rollouts 10 --adaptive_k_threshold 0.074855\", \"server\": \"bjb2-40593\", \"gpu\": \"cuda:0\", \"pid\": 681823, \"data_path\": \"LIBERO-Spatial\", \"data_count\": \"10 tasks x 10 rollouts\", \"model_name\": \"openvla-7b + CRM obs_only\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\", \"eval_data\": \"LIBERO-Spatial (10 tasks x 10 rollouts)\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-adaptive-k-spatial-p50-seed42.log\", \"checkpoint_path\": \"N/A (eval only)\"}, \"hypothesis\": \"Adaptive K with τ=P50 (0.074855, Object-calibrated) on LIBERO-Spatial seed42. 验证 Adaptive K 方法在第二个 benchmark 上的泛化：使用 Object 上校准的阈值直接应用到 Spatial（无 per-benchmark tuning）。如果 SR 接近 CRM K=10 (34.3%) 且 fast_path >50%，则证明方法跨 benchmark 通用。\"}, \"eval-obs-only-object-norm003-seed44\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-20T10:52:14.742Z\", \"updated_at\": \"2026-05-20T10:52:47.202Z\", \"hypothesis\": \"CRM obs_only ε=0.03 on Object seed44. Low-norm multi-seed supplement (plan_500): strengthens Figure 2 error bars at small ε.\", \"spec\": {\"command\": \"evaluate.py --mode crm_obs_only --benchmark object --seed 44 --n_rollouts 10 --K 10 --max_correction_norm 0.03\", \"server\": \"bjb2-28827\", \"seed\": 44, \"model_name\": \"crm_v3_norm/obs_only/crm_best.pt\", \"data_path\": \"LIBERO_object\", \"data_count\": 100}, \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-obs-only-object-norm003-seed44.log\", \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\", \"metrics\": {\"overall_success_rate\": 0.15, \"total_successes\": 15, \"total_rollouts\": 100, \"per_task\": {\"alphabet_soup\": 0, \"cream_cheese\": 0, \"salad_dressing\": 0.3, \"bbq_sauce\": 0.2, \"ketchup\": 0, \"tomato_sauce\": 0.1, \"butter\": 0.1, \"milk\": 0.2, \"chocolate_pudding\": 0.3, \"orange_juice\": 0.3}}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-20T10:52:47.202Z\"}, \"eval-adaptive-k-spatial-p90-seed42\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-20T10:52:05.759Z\", \"updated_at\": \"2026-05-20T10:52:38.383Z\", \"spec\": {\"command\": \"python -u src/evaluate.py --mode adaptive_k --benchmark LIBERO-Spatial --seed 42 --n_rollouts 10 --adaptive_k_threshold 0.125870 --output_file logs/eval-adaptive-k-spatial-p90-seed42.json\", \"server\": \"bjb2-28827\", \"gpu\": \"cuda:2\", \"pid\": 308030, \"data_path\": \"LIBERO-Spatial\", \"data_count\": \"10 tasks x 10 rollouts\", \"model_name\": \"openvla-7b + CRM obs_only\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\", \"eval_data\": \"LIBERO-Spatial (10 tasks x 10 rollouts)\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-adaptive-k-spatial-p90-seed42.log\"}}, \"eval-adaptive-k-spatial-p25-seed44\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-20T10:52:04.790Z\", \"updated_at\": \"2026-05-20T10:52:34.962Z\", \"spec\": {\"command\": \"python -u src/evaluate.py --mode adaptive_k --benchmark LIBERO-Spatial --seed 44 --n_rollouts 10 --adaptive_k_threshold 0.054959 --output_file logs/eval-adaptive-k-spatial-p25-seed44.json\", \"server\": \"bjb2-28827\", \"gpu\": \"cuda:1\", \"pid\": 307754, \"data_path\": \"LIBERO-Spatial\", \"data_count\": \"10 tasks x 10 rollouts\", \"model_name\": \"openvla-7b + CRM obs_only\", \"seed\": 44, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\", \"eval_data\": \"LIBERO-Spatial (10 tasks x 10 rollouts)\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-adaptive-k-spatial-p25-seed44.log\"}}, \"eval-adaptive-k-spatial-p75-seed44\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-20T10:52:04.320Z\", \"updated_at\": \"2026-05-20T10:52:32.674Z\", \"spec\": {\"command\": \"python -u src/evaluate.py --mode adaptive_k --benchmark LIBERO-Spatial --seed 44 --n_rollouts 10 --adaptive_k_threshold 0.098735 --output_file logs/eval-adaptive-k-spatial-p75-seed44.json\", \"server\": \"bjb2-28827\", \"gpu\": \"cuda:0\", \"pid\": 307478, \"data_path\": \"LIBERO-Spatial\", \"data_count\": \"10 tasks x 10 rollouts\", \"model_name\": \"openvla-7b + CRM obs_only\", \"seed\": 44, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\", \"eval_data\": \"LIBERO-Spatial (10 tasks x 10 rollouts)\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-adaptive-k-spatial-p75-seed44.log\"}}, \"eval-random-selection-object-seed46-r2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-19T17:41:16.541Z\", \"updated_at\": \"2026-05-19T17:41:32.255Z\", \"spec\": {\"command\": \"cd /root/acr-vla-conformal-refinement && timeout 57600 /root/miniconda3/bin/python -u src/evaluate.py --mode random_selection --benchmark object --n_rollouts 10 --seed 46 --K 10 --output_file logs/eval_object_random_selection_seed46.json\", \"server\": \"bjb2-40593\", \"data_path\": \"LIBERO-Object\", \"data_count\": 100, \"model_name\": \"SmolVLA_random_selection\", \"seed\": 46, \"checkpoint_path\": \"N/A-eval-only\", \"log_path\": \"/root/acr-vla-conformal-refinement/logs/eval_object_random_selection_seed46.log\"}, \"hypothesis\": \"Random selection baseline (K=10) on LIBERO-Object seed46 establishes reference success rate for comparing against CRM-guided selection methods\", \"conclusion\": \"killed\", \"completed_at\": \"2026-05-19T17:41:32.255Z\"}, \"eval-obs-only-spatial-norm02-seed46-r2\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-19T17:12:13.545Z\", \"updated_at\": \"2026-05-19T17:12:53.558Z\", \"hypothesis\": \"obs_only CRM with epsilon=0.2 and K=10 improves LIBERO-Spatial success rate by applying observation-conditioned conformal corrections to fix spatial reasoning errors, seed46 rerun for statistical robustness\", \"spec\": {\"command\": \"cd /root/acr-vla-conformal-refinement && /root/miniconda3/bin/python -u src/evaluate.py --mode crm_obs_only --benchmark spatial --n_rollouts 10 --seed 46 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --max_correction_norm 0.2 --output_file logs/eval_spatial_obs_only_norm02_seed46_r2.json\", \"server\": \"bjb2-28827\", \"gpu\": [\"cuda:3\"], \"data_path\": \"LIBERO-Spatial\", \"data_count\": 100, \"model_name\": \"SmolVLA+CRM_obs_only\", \"seed\": 46, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\", \"checkpoint_path\": \"N/A-eval-only\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-obs-only-spatial-norm02-seed46-r2.log\"}}, \"eval-vla-only-goal-seed44-r2\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-19T17:12:11.696Z\", \"updated_at\": \"2026-05-19T17:12:53.198Z\", \"hypothesis\": \"VLA-only baseline on LIBERO-Goal seed44 establishes reference success rate for comparing against CRM-augmented methods on goal-conditioned tasks, rerun for statistical robustness\", \"spec\": {\"command\": \"cd /root/acr-vla-conformal-refinement && /root/miniconda3/bin/python -u src/evaluate.py --mode vla_only --benchmark goal --n_rollouts 10 --seed 44 --K 1 --output_file logs/eval_goal_vla_only_seed44_r2.json\", \"server\": \"bjb2-28827\", \"gpu\": [\"cuda:0\"], \"data_path\": \"LIBERO-Goal\", \"data_count\": 100, \"model_name\": \"SmolVLA\", \"seed\": 44, \"checkpoint_path\": \"N/A-eval-only\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-vla-only-goal-seed44-r2.log\"}}, \"eval-argmin-object-k5-seed44-r2\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-19T17:12:10.271Z\", \"updated_at\": \"2026-05-19T17:12:52.978Z\", \"hypothesis\": \"ReConVLA argmin mode with K=5 candidates improves LIBERO-Object success rate over VLA-only baseline by selecting the best action from multiple VLA samples using conformal scoring, seed44 rerun for statistical robustness\", \"spec\": {\"command\": \"cd /root/acr-vla-conformal-refinement && /root/miniconda3/bin/python -u src/evaluate.py --mode reconvla --benchmark object --n_rollouts 10 --seed 44 --K 5 --output_file logs/eval_object_argmin_k5_seed44_r2.json\", \"server\": \"bjb2-28827\", \"gpu\": [\"cuda:1\"], \"data_path\": \"LIBERO-Object\", \"data_count\": 100, \"model_name\": \"SmolVLA_argmin\", \"seed\": 44, \"checkpoint_path\": \"N/A-eval-only\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-argmin-object-k5-seed44-r2.log\"}}, \"eval-openvla-object-baseline-seed42\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-19T17:12:07.506Z\", \"updated_at\": \"2026-05-19T17:12:46.396Z\", \"hypothesis\": \"OpenVLA baseline on LIBERO-Object seed42 establishes reference success rate for comparing against SmolVLA and CRM-augmented methods on object manipulation tasks\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/openvla-repo && CUDA_VISIBLE_DEVICES=4 TRANSFORMERS_OFFLINE=1 HF_HUB_OFFLINE=1 python experiments/robot/libero/run_libero_eval.py --model_family openvla --pretrained_checkpoint /root/autodl-tmp/models/openvla-libero-object --task_suite_name libero_object --center_crop True --seed 42 --num_trials_per_task 50 --use_wandb False\\\"\", \"server\": \"bjb2-28827\", \"gpu\": [\"cuda:4\"], \"data_path\": \"LIBERO-Object\", \"data_count\": 500, \"model_name\": \"OpenVLA\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/models/openvla-libero-object\", \"eval_data\": \"LIBERO-Object\", \"checkpoint_path\": \"N/A-eval-only\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-openvla-object-baseline-seed42.log\"}}, \"eval-obs-only-spatial-norm02-seed47\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-19T17:02:40.986Z\", \"updated_at\": \"2026-05-19T17:03:14.457Z\", \"metrics\": {\"success_rate\": 0.32, \"successes\": 32, \"total\": 100, \"n_tasks\": 10, \"n_rollouts\": 10, \"per_task\": {\"between_plate_and_ramekin\": 0.8, \"next_to_ramekin\": 0.9, \"from_table_center\": 0, \"on_cookie_box\": 0.3, \"in_top_drawer\": 0.1, \"on_ramekin\": 0, \"next_to_cookie_box\": 0.9, \"on_stove\": 0, \"next_to_plate\": 0.2, \"on_wooden_cabinet\": 0}}, \"checkpoint_path\": \"N/A-eval-only\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-obs-only-spatial-norm02-seed47.log\", \"conclusion\": \"success\", \"spec\": {\"command\": \"cd /root/acr-vla-conformal-refinement && /root/miniconda3/bin/python -u src/evaluate.py --mode crm_obs_only --benchmark spatial --n_rollouts 10 --seed 47 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --max_correction_norm 0.2 --output_file logs/eval_spatial_obs_only_norm02_seed47.json\", \"server\": \"bjb1-32546\", \"data_path\": \"LIBERO-Spatial\", \"data_count\": 100, \"model_name\": \"crm_obs_only\", \"seed\": 47}, \"hypothesis\": \"obs_only CRM with epsilon=0.2 and K=10 improves success rate over VLA-only baseline on LIBERO-Spatial because observation-conditioned conformal corrections can detect and fix spatial reasoning errors without requiring action history\", \"completed_at\": \"2026-05-19T17:03:14.457Z\"}, \"eval-vla-only-spatial-seed45\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-19T15:19:50.220Z\", \"updated_at\": \"2026-05-19T15:20:24.563Z\", \"spec\": {\"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-vla-only-spatial-seed45.log\", \"command\": \"python evaluate.py --benchmark spatial --mode vla_only --seed 45\", \"server\": \"bjb1-32546\", \"seed\": 45, \"data_path\": \"LIBERO-Spatial\", \"data_count\": 100, \"model_name\": \"SmolVLA\", \"checkpoint_path\": \"N/A (eval-only)\"}, \"metrics\": {\"success_rate\": 0.27, \"per_task\": {\"between_plate_and_ramekin\": 0.7, \"next_to_ramekin\": 0.9, \"from_table_center\": 0, \"on_cookie_box\": 0.2, \"in_top_drawer\": 0, \"on_ramekin\": 0, \"next_to_cookie_box\": 0.9, \"on_stove\": 0, \"next_to_plate\": 0, \"on_wooden_cabinet\": 0}, \"successes\": 27, \"total\": 100}, \"conclusion\": \"success\", \"hypothesis\": \"VLA-only baseline on LIBERO-Spatial with seed 45 establishes reference success rate for comparison with CRM-augmented methods\", \"completed_at\": \"2026-05-19T15:20:24.563Z\"}, \"eval-obs-only-spatial-norm02-seed44\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-19T14:23:33.161Z\", \"updated_at\": \"2026-05-19T14:26:44.810Z\", \"metrics\": {\"success_rate\": 0.36, \"successes\": 36, \"total\": 100}, \"checkpoint_path\": \"N/A (eval only)\", \"log_path\": \"/root/acr-vla-conformal-refinement/logs/eval_spatial_obs_only_norm02_seed44.json\", \"conclusion\": \"success\", \"spec\": {\"command\": \"python eval_crm.py --mode crm_obs_only --benchmark spatial --K 10 --seed 44 --max_correction_norm 0.2\", \"server\": \"bjb2-28827\", \"data_path\": \"spatial_benchmark\", \"data_count\": 100, \"model_name\": \"crm_obs_only\", \"seed\": 44}, \"hypothesis\": \"CRM obs-only mode with max_correction_norm=0.2 can improve spatial benchmark success rate by refining VLA actions using only observation-based conformal prediction, without access to privileged state information.\", \"completed_at\": \"2026-05-19T14:24:10.857Z\"}, \"eval-obs-only-object-norm003-seed43-r2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-19T05:14:10.523Z\", \"updated_at\": \"2026-05-19T05:14:25.385Z\", \"conclusion\": \"failed\", \"spec\": {\"checkpoint_path\": \"N/A (eval-only)\", \"log_path\": \"/root/acr-vla-conformal-refinement/logs/eval_object_obs_only_norm003_seed43.log\", \"metrics\": {\"success_rate\": null, \"tasks_completed\": \"1/10\", \"failure_reason\": \"process terminated prematurely after 1 task\"}}, \"completed_at\": \"2026-05-19T05:14:25.385Z\"}, \"eval-obs-only-object-norm03-seed48\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-18T13:26:49.122Z\", \"updated_at\": \"2026-05-18T13:27:19.389Z\", \"metrics\": {\"overall_success_rate\": 0.16, \"per_task\": {\"pick_up_the_alphabet_soup_and_place_it_in_the_basket\": 0, \"pick_up_the_cream_cheese_and_place_it_in_the_basket\": 0, \"pick_up_the_salad_dressing_and_place_it_in_the_basket\": 0.3, \"pick_up_the_bbq_sauce_and_place_it_in_the_basket\": 0.4, \"pick_up_the_ketchup_and_place_it_in_the_basket\": 0, \"pick_up_the_tomato_sauce_and_place_it_in_the_basket\": 0.1, \"pick_up_the_butter_and_place_it_in_the_basket\": 0.1, \"pick_up_the_milk_and_place_it_in_the_basket\": 0.1, \"pick_up_the_chocolate_pudding_and_place_it_in_the_basket\": 0.4, \"pick_up_the_orange_juice_and_place_it_in_the_basket\": 0.2}}, \"log_path\": \"/root/acr-vla-conformal-refinement/logs/eval_object_obs_only_norm03_seed48.json\", \"checkpoint_path\": \"N/A (eval only)\", \"conclusion\": \"success\", \"spec\": {\"command\": \"eval obs_only CRM epsilon=0.3 seed48 on LIBERO-Object K=10 n_rollouts=10\", \"server\": \"bjb1-18228\", \"data_path\": \"LIBERO-Object\", \"data_count\": 100, \"model_name\": \"openvla\", \"seed\": 48}, \"hypothesis\": \"CRM with obs_only mode and epsilon=0.3 normalization threshold will improve success rate on LIBERO-Object by filtering unreliable action predictions based solely on observation conformity scores\", \"completed_at\": \"2026-05-18T13:27:19.389Z\"}, \"eval-obs-only-object-norm01-seed48\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-18T11:42:37.233Z\", \"updated_at\": \"2026-05-18T11:43:15.403Z\", \"hypothesis\": \"obs_only CRM with max_correction_norm=0.1 on LIBERO-Object seed48. Tests whether obs_only mode with conservative norm clipping maintains performance across seeds.\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=1 /root/miniconda3/bin/python -u src/evaluate.py --mode crm_obs_only --benchmark object --n_rollouts 10 --seed 48 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --max_correction_norm 0.1 --output_file logs/eval_object_obs_only_norm01_seed48.json\", \"server\": \"bjb1-18228\", \"data_path\": \"LIBERO-Object\", \"data_count\": 100, \"model_name\": \"SmolVLA+CRM_obs_only\", \"seed\": 48, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\", \"eval_data\": \"LIBERO-Object\"}, \"log_path\": \"/root/acr-vla-conformal-refinement/logs/eval_object_obs_only_norm01_seed48.json\", \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.18, \"n_tasks\": 10, \"n_rollouts\": 10, \"per_task\": {\"alphabet_soup\": 0, \"cream_cheese\": 0, \"salad_dressing\": 0, \"bbq_sauce\": 0.4, \"ketchup\": 0.1, \"tomato_sauce\": 0.2, \"butter\": 0.2, \"milk\": 0.3, \"chocolate_pudding\": 0.3, \"orange_juice\": 0.3}}, \"completed_at\": \"2026-05-18T11:43:15.403Z\"}, \"eval-obs-only-object-norm02-k5-seed42\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-18T03:44:47.522Z\", \"updated_at\": \"2026-05-18T03:45:04.655Z\", \"conclusion\": \"success\", \"metrics\": {\"overall_sr\": 0.14, \"successes\": 14, \"rollouts\": 100, \"tasks\": 10, \"suite\": \"LIBERO-object\", \"seed\": 42, \"method\": \"crm_obs_only\", \"K\": 5, \"max_correction_norm\": 0.2}, \"hypothesis\": \"obs_only CRM with K=5 candidates and ε=0.2 on LIBERO-Object seed42. Tests whether fewer candidates (K=5 vs K=10) reduces selection quality. K=5 SR=14% vs K=10 SR=17.5% confirms monotonic improvement with more candidates.\", \"spec\": {\"command\": \"python -u src/evaluate.py --mode crm_obs_only --benchmark object --n_rollouts 10 --seed 42 --K 5 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --max_correction_norm 0.2 --output_file logs/eval_object_obs_only_norm02_k5_seed42.json\", \"server\": \"bjb1-18228\", \"data_path\": \"LIBERO-Object\", \"data_count\": 100, \"model_name\": \"SmolVLA+CRM_obs_only\", \"seed\": 42, \"K\": 5, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\", \"eval_data\": \"LIBERO-Object\", \"checkpoint_path\": \"N/A\", \"log_path\": \"/root/acr-vla-conformal-refinement/logs/eval_object_obs_only_norm02_k5_seed42.json\"}, \"completed_at\": \"2026-05-18T03:45:04.655Z\"}, \"eval-perdof-object-norm01-seed46\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-18T03:05:55.543Z\", \"updated_at\": \"2026-05-18T03:06:14.048Z\", \"hypothesis\": \"perdof CRM with ε=0.1 on LIBERO-Object seed46. Magnitude curve data point for perdof at intermediate norm. SR=10% confirms perdof degrades from peak at low norms.\", \"metrics\": {\"overall_sr\": 0.1, \"successes\": 10, \"rollouts\": 100, \"tasks\": 10, \"suite\": \"LIBERO-object\", \"seed\": 46, \"method\": \"crm_perdof\", \"max_correction_norm\": 0.1}, \"conclusion\": \"success\", \"spec\": {\"command\": \"python -u src/evaluate.py --mode crm_perdof --benchmark object --n_rollouts 10 --seed 46 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt --max_correction_norm 0.1 --output_file logs/eval_object_perdof_norm01_seed46.json\", \"server\": \"bjb1-32546\", \"data_path\": \"LIBERO-Object\", \"data_count\": 100, \"model_name\": \"SmolVLA+CRM_perdof\", \"seed\": 46, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt\", \"eval_data\": \"LIBERO-Object\", \"checkpoint_path\": \"N/A\", \"log_path\": \"/root/acr-vla-conformal-refinement/logs/eval_object_perdof_norm01_seed46.json\"}, \"completed_at\": \"2026-05-18T03:06:14.049Z\"}, \"eval-perdof-object-default-seed46\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-18T03:05:29.784Z\", \"updated_at\": \"2026-05-18T03:06:03.735Z\", \"conclusion\": \"negative\", \"hypothesis\": \"perdof CRM without norm constraint (uncapped correction magnitude) on LIBERO-Object seed46. Tests whether perdof maintains performance without explicit correction capping. SR=0% confirms perdof corrections are catastrophically unstable without norm constraints.\", \"spec\": {\"command\": \"python -u src/evaluate.py --mode crm_perdof --benchmark object --n_rollouts 10 --seed 46 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt --output_file logs/eval_object_perdof_default_seed46.json\", \"server\": \"bjb1-32546\", \"data_path\": \"LIBERO-Object\", \"data_count\": 100, \"model_name\": \"SmolVLA+CRM_perdof\", \"seed\": 46, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt\", \"eval_data\": \"LIBERO-Object\", \"checkpoint_path\": \"N/A\", \"log_path\": \"/root/acr-vla-conformal-refinement/logs/eval_object_perdof_default_seed46.json\"}, \"metrics\": {\"overall_sr\": 0, \"successes\": 0, \"rollouts\": 100, \"tasks\": 10, \"suite\": \"LIBERO-object\", \"seed\": 46, \"method\": \"crm_perdof\", \"max_correction_norm\": \"default\"}, \"completed_at\": \"2026-05-18T03:06:03.735Z\"}, \"eval-perdof-object-norm02-seed48\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-18T03:05:29.433Z\", \"updated_at\": \"2026-05-18T03:05:47.075Z\", \"hypothesis\": \"perdof CRM with ε=0.2 on LIBERO-Object seed48. Additional seed for perdof magnitude curve at primary comparison norm. Running on bjb2-28827 cuda:5 PID 488665.\", \"spec\": {\"command\": \"cd /root/acr-vla-conformal-refinement && CUDA_VISIBLE_DEVICES=5 python -u src/evaluate.py --mode crm_perdof --benchmark object --n_rollouts 10 --seed 48 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt --max_correction_norm 0.2 --output_file logs/eval_object_perdof_norm02_seed48.json\", \"server\": \"bjb2-28827\", \"data_path\": \"LIBERO-Object\", \"data_count\": 100, \"model_name\": \"SmolVLA+CRM_perdof\", \"seed\": 48, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt\", \"eval_data\": \"LIBERO-Object\"}}, \"eval-obs-only-object-default-seed46\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-18T00:59:50.348Z\", \"updated_at\": \"2026-05-18T01:00:23.165Z\", \"conclusion\": \"success\", \"metrics\": {\"overall_sr\": 0.15, \"successes\": 15, \"rollouts\": 100, \"tasks\": 10, \"suite\": \"LIBERO-object\", \"seed\": 46, \"method\": \"crm_obs_only\", \"max_correction_norm\": \"default\", \"per_task_sr\": {\"alphabet_soup\": 0, \"cream_cheese\": 0, \"salad_dressing\": 0.2, \"bbq_sauce\": 0.4, \"ketchup\": 0.1, \"tomato_sauce\": 0.1, \"butter\": 0.1, \"milk\": 0.1, \"chocolate_pudding\": 0.2, \"orange_juice\": 0.3}}, \"spec\": {\"checkpoint_path\": \"N/A\", \"log_path\": \"/root/acr-vla-conformal-refinement/logs/eval_object_obs_only_default_seed46.json\", \"command\": \"python -u src/evaluate.py --mode crm_obs_only --benchmark object --n_rollouts 10 --seed 46 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --output_file logs/eval_object_obs_only_default_seed46.json\", \"server\": \"bjb1-32546\", \"data_path\": \"LIBERO-Object\", \"data_count\": 100, \"model_name\": \"SmolVLA+CRM_obs_only\", \"seed\": 46, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\", \"eval_data\": \"LIBERO-Object\"}, \"hypothesis\": \"obs_only CRM without norm constraint (uncapped correction magnitude) on LIBERO-Object seed46. Tests whether obs_only maintains performance without explicit correction capping. If uncapped performs worse than capped, it confirms that moderate norm constraints stabilize corrections.\", \"completed_at\": \"2026-05-18T01:00:23.165Z\"}, \"eval-obs-only-object-norm01-seed46\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-18T00:42:56.715Z\", \"updated_at\": \"2026-05-18T00:43:09.191Z\", \"conclusion\": \"killed\", \"completed_at\": \"2026-05-18T00:43:09.191Z\"}, \"eval-k1-crm-multiscale-object-seed43\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-17T21:05:23.402Z\", \"updated_at\": \"2026-05-17T21:06:09.004Z\", \"hypothesis\": \"Multi-scale K=1 CRM with accumulated gradient refinement improves object manipulation success rate over baseline by providing conformal prediction-based action corrections at multiple spatial scales\", \"spec\": {\"command\": \"python -u src/evaluate.py --mode crm_k1_accg --benchmark object --n_rollouts 10 --seed 43\", \"server\": \"bjb1-32546\", \"data_path\": \"LIBERO-Object\", \"data_count\": 100, \"model_name\": \"SmolVLA+CRM_k1_accg\", \"seed\": 43, \"checkpoint_source\": \"crm_v3_norm\", \"eval_data\": \"LIBERO-Object\", \"checkpoint_path\": \"N/A\", \"log_path\": \"/root/acr-vla-conformal-refinement/logs/eval_k1_crm_multiscale_object_seed43.json\"}, \"conclusion\": \"negative\", \"metrics\": {\"overall_sr\": 0.09, \"successes\": 9, \"rollouts\": 100, \"tasks\": 10, \"suite\": \"LIBERO-object\", \"seed\": 43, \"method\": \"crm_k1_accg\", \"per_task\": {\"alphabet_soup\": 0, \"cream_cheese\": 0, \"salad_dressing\": 0.1, \"bbq_sauce\": 0.2, \"ketchup\": 0, \"tomato_sauce\": 0.2, \"butter\": 0, \"milk\": 0, \"chocolate_pudding\": 0.2, \"orange_juice\": 0.2}}, \"completed_at\": \"2026-05-17T21:06:09.004Z\"}, \"eval-k1-crm-multiscale-object-seed42\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-17T21:05:22.835Z\", \"updated_at\": \"2026-05-17T21:06:08.318Z\", \"hypothesis\": \"Multi-scale K=1 CRM with accumulated gradient refinement improves object manipulation success rate over baseline by providing conformal prediction-based action corrections at multiple spatial scales\", \"spec\": {\"command\": \"python -u src/evaluate.py --mode crm_k1_accg --benchmark object --n_rollouts 10 --seed 42\", \"server\": \"bjb2-28827\", \"data_path\": \"LIBERO-Object\", \"data_count\": 100, \"model_name\": \"SmolVLA+CRM_k1_accg\", \"seed\": 42, \"checkpoint_source\": \"crm_v3_norm\", \"eval_data\": \"LIBERO-Object\", \"checkpoint_path\": \"N/A\", \"log_path\": \"/root/acr-vla-conformal-refinement/logs/eval_k1_crm_multiscale_object_seed42.json\"}, \"conclusion\": \"negative\", \"metrics\": {\"overall_sr\": 0.12, \"successes\": 12, \"rollouts\": 100, \"tasks\": 10, \"suite\": \"LIBERO-object\", \"seed\": 42, \"method\": \"crm_k1_accg\", \"per_task\": {\"alphabet_soup\": 0, \"cream_cheese\": 0, \"salad_dressing\": 0.1, \"bbq_sauce\": 0.2, \"ketchup\": 0, \"tomato_sauce\": 0.3, \"butter\": 0.1, \"milk\": 0, \"chocolate_pudding\": 0.3, \"orange_juice\": 0.2}}, \"completed_at\": \"2026-05-17T21:06:08.318Z\"}, \"eval-obs-only-object-norm005-seed43\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-17T21:04:43.285Z\", \"updated_at\": \"2026-05-17T21:04:52.760Z\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=0 python -u src/evaluate.py --mode crm_obs_only --benchmark object --n_rollouts 10 --seed 43 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --max_correction_norm 0.05 --output_file logs/eval_object_obs_only_norm005_seed43.json\", \"server\": \"bjb2-28827\", \"data_path\": \"LIBERO-Object\", \"data_count\": 100, \"model_name\": \"SmolVLA+CRM_obs_only\", \"seed\": 43, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\", \"eval_data\": \"LIBERO-Object\"}}, \"eval-perdof-object-norm02-seed45-r3\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-17T21:02:26.375Z\", \"updated_at\": \"2026-05-17T21:04:50.614Z\", \"hypothesis\": \"perdof CRM (ε=0.2) seed45 on LIBERO-Object. Rerun after SIGHUP kill. Original result on bjb2-28827 was 9%. This confirms reproducibility on different server.\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=3 python -u src/evaluate.py --mode crm_perdof --benchmark object --n_rollouts 10 --seed 45 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt --max_correction_norm 0.2 --output_file logs/eval_object_perdof_norm02_seed45_r3.json\", \"server\": \"bjb1-18228\", \"data_path\": \"LIBERO-Object\", \"data_count\": 100, \"model_name\": \"SmolVLA+CRM_perdof\", \"seed\": 45, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt\", \"eval_data\": \"LIBERO-Object\"}}, \"eval-k1-crm-multiscale-object-seed44-r2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-17T20:55:44.755Z\", \"updated_at\": \"2026-05-17T20:56:16.602Z\", \"hypothesis\": \"Multi-scale K=1 CRM with accumulated gradient refinement improves object manipulation success rate over baseline by providing conformal prediction-based action corrections at multiple spatial scales\", \"spec\": {\"command\": \"python eval_libero.py --method crm_k1_accg --baseline_mode single --suite object --seed 44 --n_rollouts 10\", \"server\": \"bjb1-18228\", \"data_path\": \"LIBERO-object\", \"data_count\": 100, \"model_name\": \"crm_k1_multiscale\", \"seed\": 44, \"checkpoint_source\": \"crm-k1-train\", \"eval_data\": \"LIBERO-object\"}, \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/crm_k1/crm_k1_best.pt\", \"log_path\": \"/root/acr-vla-conformal-refinement/logs/eval_k1_crm_multiscale_object_seed44_bjb1-18228.json\", \"conclusion\": \"negative\", \"completed_at\": \"2026-05-17T20:56:12.165Z\", \"metrics\": {\"overall_sr\": 0.1, \"successes\": 10, \"rollouts\": 100, \"tasks\": 10, \"suite\": \"LIBERO-object\", \"seed\": 44, \"method\": \"crm_k1_accg\", \"per_task\": {\"alphabet_soup\": 0, \"cream_cheese\": 0, \"salad_dressing\": 0.2, \"bbq_sauce\": 0.1, \"ketchup\": 0, \"tomato_sauce\": 0.1, \"butter\": 0, \"milk\": 0, \"chocolate_pudding\": 0.4, \"orange_juice\": 0.2}}}, \"eval-mag-perdof-norm03-object-r3\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-16T11:05:32.773Z\", \"updated_at\": \"2026-05-16T11:06:06.108Z\", \"conclusion\": \"success\", \"spec\": {\"command\": \"python eval_libero.py --method crm_perdof --suite object --norm 0.3 --seed 42\", \"server\": \"bjb2-28827\", \"data_path\": \"LIBERO-object\", \"data_count\": 100, \"model_name\": \"crm_perdof_norm03\", \"seed\": 42, \"checkpoint_source\": \"crm-train-v3-perdof\", \"eval_data\": \"LIBERO-object\"}, \"log_path\": \"/root/acr-vla-conformal-refinement/logs/eval_object_perdof_norm03_r3.json\", \"checkpoint_path\": \"N/A\", \"completed_at\": \"2026-05-16T11:06:02.462Z\", \"metrics\": {\"success_rate\": 0.04, \"successes\": 4, \"rollouts\": 100, \"tasks\": 10, \"suite\": \"LIBERO-object\", \"norm\": 0.3, \"seed\": 42}}, \"eval-mag-perdof-norm005-object\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-16T08:30:31.627Z\", \"updated_at\": \"2026-05-16T08:30:52.155Z\", \"spec\": {\"command\": \"python evaluate.py --mode crm_perdof --benchmark object --max_correction_norm 0.05 --seed 42\", \"server\": \"bjb2-28827\", \"data_path\": \"/root/acr-vla-conformal-refinement/logs/eval_object_perdof_norm005.json\", \"data_count\": 100, \"model_name\": \"crm_v3_norm_perdof\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt\", \"eval_data\": \"LIBERO object benchmark\"}, \"conclusion\": \"negative\", \"checkpoint_path\": \"/root/acr-vla-conformal-refinement/logs/eval_object_perdof_norm005.json\", \"log_path\": \"/root/acr-vla-conformal-refinement/logs/nohup_eval_object_perdof_norm005.log\", \"completed_at\": \"2026-05-16T08:30:50.635Z\", \"metrics\": {\"overall_sr\": 0.14, \"per_task\": {\"alphabet_soup\": 0, \"cream_cheese\": 0, \"salad_dressing\": 0.2, \"bbq_sauce\": 0.4, \"ketchup\": 0, \"tomato_sauce\": 0, \"butter\": 0, \"milk\": 0.2, \"chocolate_pudding\": 0.4, \"orange_juice\": 0.2}}}, \"eval-mag-obsonly-norm03-object\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-16T07:41:31.617Z\", \"updated_at\": \"2026-05-16T07:41:53.597Z\", \"metrics\": {\"tasks_done\": 10, \"tasks_total\": 10, \"overall_sr\": 0.19, \"per_task_sr\": {\"alphabet_soup\": 0, \"cream_cheese\": 0, \"salad_dressing\": 0.3, \"bbq_sauce\": 0.3, \"ketchup\": 0, \"tomato_sauce\": 0.1, \"butter\": 0.2, \"milk\": 0.2, \"chocolate_pudding\": 0.5, \"orange_juice\": 0.3}}, \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\", \"log_path\": \"/root/acr-vla-conformal-refinement/logs/eval_object_obs_only_norm03.log\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-16T07:41:53.597Z\"}}, \"count\": 64, \"total\": 64, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.1861}}"
    }
  }
}
```

</details>

---

### Assistant

_source line 15_

<details><summary>Logged reasoning block</summary>

```text
The full output is too large. Let me read the saved file to get all experiments.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "e17f41b1-3dce-49fb-a9e5-f5dd86423ed8",
  "uuid": "c0331a0c-ffb9-4558-937a-8309e7d09263",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018JHfGSXZrt7hUVkPnFnDW7",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2671,
      "cache_read_input_tokens": 41259,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2671
      },
      "output_tokens": 9,
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

<details open><summary>🔧 Tool call — Read · `toolu_017ZVfLarrybWGaf5rMpdDrR`</summary>

```json
{
  "file_path": "/home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-8-projects-acr-vla-conformal-refinement/e17f41b1-3dce-49fb-a9e5-f5dd86423ed8/tool-results/toolu_01Py9xhR4gHWVtTXRbKimmKL.txt"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "e17f41b1-3dce-49fb-a9e5-f5dd86423ed8",
  "uuid": "723a4423-a83c-49f9-abad-e7c2c4ca13d8",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018JHfGSXZrt7hUVkPnFnDW7",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2671,
      "cache_read_input_tokens": 41259,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2671
      },
      "output_tokens": 9,
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

_source line 17 · 2026-05-21T03:22:52.102Z_

<details><summary>↩ Tool result · `toolu_017ZVfLarrybWGaf5rMpdDrR`</summary>

```text
1	{"result":"{\"success\": true, \"data\": {\"experiments\": {\"eval-obs-only-object-norm005-seed75\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-21T02:56:05.523Z\", \"updated_at\": \"2026-05-21T02:56:12.611Z\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.15}}, \"eval-obs-only-object-norm01-seed74\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-21T02:55:20.812Z\", \"updated_at\": \"2026-05-21T02:55:28.975Z\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.13}}, \"eval-obs-only-object-norm01-seed64\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-21T02:54:30.053Z\", \"updated_at\": \"2026-05-21T02:54:30.754Z\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.15}}, \"eval-obs-only-object-norm003-seed73\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-21T02:53:26.508Z\", \"updated_at\": \"2026-05-21T02:53:31.930Z\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.16}}, \"eval-obs-only-object-norm005-seed64\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-21T02:52:33.605Z\", \"updated_at\": \"2026-05-21T02:52:37.242Z\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.15}}, \"eval-obs-only-object-norm003-seed65\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-21T02:51:17.482Z\", \"updated_at\": \"2026-05-21T02:51:23.912Z\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.17}}, \"eval-obs-only-object-norm003-seed64\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-21T02:51:17.026Z\", \"updated_at\": \"2026-05-21T02:51:23.446Z\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.17}}, \"eval-obs-only-object-norm003-seed63-r2\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-21T02:51:19.045Z\", \"updated_at\": \"2026-05-21T02:51:19.046Z\", \"conclusion\": \"killed\"}, \"eval-obs-only-object-norm003-seed62-r2\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-21T02:51:18.497Z\", \"updated_at\": \"2026-05-21T02:51:18.497Z\", \"conclusion\": \"killed\"}, \"eval-obs-only-object-norm005-seed65\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-21T02:26:45.708Z\", \"updated_at\": \"2026-05-21T02:26:50.866Z\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.14}}, \"eval-obs-only-object-norm005-seed61\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-21T01:54:41.975Z\", \"updated_at\": \"2026-05-21T01:54:46.787Z\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.15}}, \"eval-obs-only-object-norm01-seed60\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-21T01:42:15.142Z\", \"updated_at\": \"2026-05-21T01:42:24.178Z\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.15}}, \"eval-obs-only-object-norm003-seed56\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-21T01:42:14.531Z\", \"updated_at\": \"2026-05-21T01:42:23.974Z\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.15}}, \"eval-obs-only-object-norm01-seed66\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-21T01:29:23.112Z\", \"updated_at\": \"2026-05-21T01:31:28.961Z\", \"pid\": 642775}, \"eval-obs-only-object-norm005-seed66\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-21T01:29:22.550Z\", \"updated_at\": \"2026-05-21T01:31:28.635Z\", \"pid\": 642506}, \"eval-obs-only-object-norm003-seed66\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-21T01:29:22.063Z\", \"updated_at\": \"2026-05-21T01:31:27.799Z\", \"pid\": 642428}, \"eval-obs-only-object-norm003-seed59\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-21T01:23:09.866Z\", \"updated_at\": \"2026-05-21T01:23:22.549Z\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.13}}, \"eval-obs-only-object-norm005-seed58\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-21T01:23:09.469Z\", \"updated_at\": \"2026-05-21T01:23:21.948Z\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.16}}, \"eval-obs-only-object-norm01-seed57\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-21T01:23:08.871Z\", \"updated_at\": \"2026-05-21T01:23:21.444Z\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.19}}, \"eval-obs-only-object-norm005-seed63\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-21T01:02:30.561Z\", \"updated_at\": \"2026-05-21T01:02:30.561Z\", \"conclusion\": \"killed\"}, \"eval-obs-only-object-norm005-seed62\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-21T01:02:30.354Z\", \"updated_at\": \"2026-05-21T01:02:30.354Z\", \"conclusion\": \"killed\"}, \"eval-perdof-object-norm02-seed49\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-20T15:59:12.635Z\", \"updated_at\": \"2026-05-20T15:59:54.757Z\", \"metrics\": {\"overall_success_rate\": 0.12, \"total_rollouts\": 100, \"total_successes\": 12, \"per_task_sr\": {\"alphabet_soup\": 0, \"cream_cheese\": 0, \"salad_dressing\": 0.1, \"bbq_sauce\": 0.2, \"ketchup\": 0, \"tomato_sauce\": 0, \"butter\": 0.1, \"milk\": 0.2, \"chocolate_pudding\": 0.4, \"orange_juice\": 0.2}}, \"log_path\": \"/root/acr-vla-conformal-refinement/logs/eval-perdof-object-norm02-seed49.log\", \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt\", \"spec\": {\"command\": \"python evaluate.py --mode crm_perdof --benchmark object --seed 49 --K 10 --max_correction_norm 0.2 --n_rollouts 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt --output_file logs/eval_perdof_object_norm02_seed49.json\", \"server\": \"bjb1-32546\", \"data_path\": \"LIBERO-Object\", \"data_count\": 100, \"model_name\": \"crm_perdof_norm02_K10\", \"seed\": 49, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt\", \"eval_data\": \"LIBERO-Object\"}, \"hypothesis\": \"PerDoF CRM with norm-clipped corrections (epsilon=0.2, K=10) provides consistent improvement over baseline on LIBERO-Object across seeds; seed49 should yield SR in the 14-18% range consistent with seeds 43-48.\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-20T15:59:54.757Z\"}, \"eval-obs-only-object-norm02-seed43-r3\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-20T13:55:56.411Z\", \"updated_at\": \"2026-05-20T13:55:57.571Z\", \"conclusion\": \"failed\", \"failure_reason\": \"SIGHUP (tmux session terminated externally) at 8/10 tasks. No JSON output. r2 already has complete data (SR=16%), no retry needed.\"}, \"openvla-precompute-k1\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-20T13:52:53.282Z\", \"updated_at\": \"2026-05-20T13:52:53.282Z\", \"notes\": \"GPU collision: cuda:3 被 Director P0-B 指令分配给 plan_702 seed43。预计算需要在 plan_702 完成后重启。原始提交: PID 365142, 处理 74507 timesteps from 500 demos. Output: /root/autodl-tmp/crm_cache_k1_openvla/object/. 特征维度: multi_scale_obs (4,4096), action_dim=6.\"}, \"eval-obs-only-goal-norm02-seed52\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-20T12:05:20.840Z\", \"updated_at\": \"2026-05-20T12:58:35.610Z\", \"spec\": {\"command\": \"python -u src/evaluate.py --mode crm_obs_only --benchmark LIBERO-Goal --seed 52 --n_rollouts 10 --max_correction_norm 0.2\", \"server\": \"bjb1-32546\", \"gpu\": \"cuda:0\", \"pid\": 362579, \"data_path\": \"LIBERO-Goal\", \"data_count\": \"10 tasks x 10 rollouts\", \"model_name\": \"openvla-7b + CRM obs_only\", \"seed\": 52, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\", \"eval_data\": \"LIBERO-Goal (10 tasks x 10 rollouts)\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-obs-only-goal-norm02-seed52.log\", \"checkpoint_path\": \"N/A (eval only)\"}, \"metrics\": {\"success_rate\": 0.68, \"successes\": 68, \"total\": 100, \"per_task_sr\": {\"open_middle_drawer_cabinet\": 0.7, \"put_bowl_on_stove\": 0.9, \"put_wine_bottle_on_cabinet\": 0.4, \"open_top_drawer_put_bowl\": 0.3, \"put_bowl_on_cabinet\": 0.8, \"push_plate_front_stove\": 0.8, \"put_cream_cheese_in_bowl\": 0.4, \"turn_on_stove\": 1, \"put_bowl_on_plate\": 1, \"put_wine_bottle_on_rack\": 0.5}}, \"conclusion\": \"success\", \"hypothesis\": \"CRM obs_only with K=10 and norm cap 0.2 improves SR on LIBERO-Goal by applying observation-conditioned corrections that compensate for VLA action prediction errors, providing a new seed for variance estimation.\", \"completed_at\": \"2026-05-20T12:58:26.417Z\", \"notes\": \"SR=68% on Goal seed52. Strong result; turn_on_stove and put_bowl_on_plate both 100%.\"}, \"eval-argmin-object-seed49\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-20T12:05:22.690Z\", \"updated_at\": \"2026-05-20T12:58:34.569Z\", \"spec\": {\"command\": \"python -u src/evaluate.py --mode reconvla --benchmark LIBERO-Object --seed 49 --n_rollouts 10\", \"server\": \"bjb1-32546\", \"gpu\": \"cuda:5\", \"pid\": 364591, \"data_path\": \"LIBERO-Object\", \"data_count\": \"10 tasks x 10 rollouts\", \"model_name\": \"openvla-7b + CRM obs_only (argmin)\", \"seed\": 49, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\", \"eval_data\": \"LIBERO-Object (10 tasks x 10 rollouts)\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-argmin-object-seed49.log\", \"checkpoint_path\": \"N/A (eval only)\"}, \"metrics\": {\"success_rate\": 0.16, \"successes\": 16, \"total\": 100, \"per_task_sr\": {\"alphabet_soup\": 0, \"cream_cheese\": 0, \"salad_dressing\": 0.2, \"bbq_sauce\": 0.4, \"ketchup\": 0, \"tomato_sauce\": 0.1, \"butter\": 0.1, \"milk\": 0.3, \"chocolate_pudding\": 0.3, \"orange_juice\": 0.2}}, \"conclusion\": \"success\", \"hypothesis\": \"Argmin (reconvla) selection among K=10 CRM refinements improves over single-step VLA on Object by choosing the candidate with lowest predicted residual, providing a multi-seed consistency check.\", \"completed_at\": \"2026-05-20T12:58:25.905Z\", \"notes\": \"SR=16% on Object seed49. Consistent with other argmin seeds on Object benchmark.\"}, \"eval-random-selection-spatial-seed43\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-20T12:05:19.438Z\", \"updated_at\": \"2026-05-20T12:58:33.167Z\", \"spec\": {\"command\": \"python -u src/evaluate.py --mode random_selection --benchmark LIBERO-Spatial --seed 43 --n_rollouts 10\", \"server\": \"bjb1-18228\", \"gpu\": \"cuda:1\", \"pid\": 347075, \"data_path\": \"LIBERO-Spatial\", \"data_count\": \"10 tasks x 10 rollouts\", \"model_name\": \"openvla-7b + CRM obs_only\", \"seed\": 43, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\", \"eval_data\": \"LIBERO-Spatial (10 tasks x 10 rollouts)\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-random-selection-spatial-seed43.log\", \"checkpoint_path\": \"N/A (eval only)\"}, \"metrics\": {\"success_rate\": 0.26, \"successes\": 26, \"total\": 100, \"per_task_sr\": {\"between_plate_ramekin\": 0.7, \"next_to_ramekin\": 0.9, \"table_center\": 0, \"cookie_box\": 0.1, \"top_drawer\": 0, \"on_ramekin\": 0, \"next_to_cookie_box\": 0.7, \"on_stove\": 0, \"next_to_plate\": 0.2, \"on_wooden_cabinet\": 0}}, \"conclusion\": \"success\", \"hypothesis\": \"Random candidate selection from K=10 CRM refinements serves as a lower-bound baseline, showing that informed selection (argmin) is necessary to achieve the full benefit of multi-step refinement on Spatial.\", \"completed_at\": \"2026-05-20T12:58:24.969Z\", \"notes\": \"SR=26% on Spatial seed43. Lower than argmin-based selection, confirming informed selection matters.\"}, \"eval-adaptive-k-spatial-p90-seed43\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-20T10:52:06.660Z\", \"updated_at\": \"2026-05-20T12:58:31.849Z\", \"spec\": {\"command\": \"python -u src/evaluate.py --mode adaptive_k --benchmark LIBERO-Spatial --seed 43 --n_rollouts 10 --adaptive_k_threshold 0.125870 --output_file logs/eval-adaptive-k-spatial-p90-seed43.json\", \"server\": \"bjb1-18228\", \"gpu\": \"cuda:3\", \"pid\": 344852, \"data_path\": \"LIBERO-Spatial\", \"data_count\": \"10 tasks x 10 rollouts\", \"model_name\": \"openvla-7b + CRM obs_only\", \"seed\": 43, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\", \"eval_data\": \"LIBERO-Spatial (10 tasks x 10 rollouts)\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-adaptive-k-spatial-p90-seed43.log\", \"checkpoint_path\": \"N/A (eval only)\"}, \"metrics\": {\"success_rate\": 0.32, \"successes\": 32, \"total\": 100, \"avg_K\": 3.6, \"fast_path_pct\": 80.2, \"mean_l2\": 0.0905, \"per_task_sr\": {\"between_plate_ramekin\": 0.7, \"next_to_ramekin\": 1, \"table_center\": 0.1, \"cookie_box\": 0.3, \"top_drawer\": 0, \"on_ramekin\": 0.1, \"next_to_cookie_box\": 0.8, \"on_stove\": 0, \"next_to_plate\": 0.2, \"on_wooden_cabinet\": 0}}, \"conclusion\": \"success\", \"hypothesis\": \"Adaptive K with P90 threshold (τ=0.1259) reduces average refinement steps while maintaining comparable SR to fixed K=10 on Spatial, because most states have low CRM residuals and can skip full refinement.\", \"completed_at\": \"2026-05-20T12:58:23.572Z\", \"notes\": \"SR=32%, avg_K=3.6 (vs fixed K=10), 80.2% fast-path. Adaptive K saves ~64% compute with seed43 on Spatial.\"}, \"eval-adaptive-k-object-p90-seed44\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-20T12:45:08.564Z\", \"updated_at\": \"2026-05-20T12:45:37.089Z\", \"hypothesis\": \"Adaptive K with τ=P90 (0.125870) on LIBERO-Object seed44. P90 是最宽松的阈值——大部分 step fast-path (K=1)，仅在极高不确定性时用 K=10。验证 P90 在 Object 上的 SR/compute tradeoff。\", \"spec\": {\"command\": \"python -u src/evaluate.py --mode adaptive_k --benchmark LIBERO-Object --seed 44 --n_rollouts 10 --adaptive_k_threshold 0.125870\", \"server\": \"bjb2-28827\", \"data_path\": \"LIBERO-Object\", \"data_count\": \"10 tasks x 10 rollouts\", \"model_name\": \"openvla-7b + CRM obs_only\", \"seed\": 44, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\", \"eval_data\": \"LIBERO-Object (10 tasks x 10 rollouts)\", \"log_path\": \"N/A (discovered by Reviewer)\", \"checkpoint_path\": \"N/A (eval only)\"}, \"metrics\": {\"sr\": 14, \"avg_K\": 2.58, \"fast_path_pct\": 92.8, \"total_rollouts\": 100}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-20T12:45:37.089Z\"}, \"eval-adaptive-k-object-p90-seed43\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-20T12:45:08.312Z\", \"updated_at\": \"2026-05-20T12:45:34.700Z\", \"hypothesis\": \"Adaptive K with τ=P90 (0.125870) on LIBERO-Object seed43. P90 是最宽松的阈值——大部分 step fast-path (K=1)，仅在极高不确定性时用 K=10。验证 P90 在 Object 上的 SR/compute tradeoff。\", \"spec\": {\"command\": \"python -u src/evaluate.py --mode adaptive_k --benchmark LIBERO-Object --seed 43 --n_rollouts 10 --adaptive_k_threshold 0.125870\", \"server\": \"bjb2-28827\", \"data_path\": \"LIBERO-Object\", \"data_count\": \"10 tasks x 10 rollouts\", \"model_name\": \"openvla-7b + CRM obs_only\", \"seed\": 43, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\", \"eval_data\": \"LIBERO-Object (10 tasks x 10 rollouts)\", \"log_path\": \"N/A (discovered by Reviewer)\", \"checkpoint_path\": \"N/A (eval only)\"}, \"metrics\": {\"sr\": 14, \"avg_K\": 2.61, \"fast_path_pct\": 92.3, \"total_rollouts\": 100}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-20T12:45:34.700Z\"}, \"eval-argmin-object-seed48\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-20T12:05:22.501Z\", \"updated_at\": \"2026-05-20T12:05:49.680Z\", \"spec\": {\"command\": \"python -u src/evaluate.py --mode reconvla --benchmark LIBERO-Object --seed 48 --n_rollouts 10\", \"server\": \"bjb1-32546\", \"gpu\": \"cuda:4\", \"pid\": 364125, \"data_path\": \"LIBERO-Object\", \"data_count\": \"10 tasks x 10 rollouts\", \"model_name\": \"openvla-7b + CRM obs_only (argmin)\", \"seed\": 48, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\", \"eval_data\": \"LIBERO-Object (10 tasks x 10 rollouts)\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-argmin-object-seed48.log\"}}, \"eval-obs-only-object-norm02-seed49\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-20T12:05:21.387Z\", \"updated_at\": \"2026-05-20T12:05:49.425Z\", \"spec\": {\"command\": \"python -u src/evaluate.py --mode crm_obs_only --benchmark LIBERO-Object --seed 49 --n_rollouts 10 --max_correction_norm 0.2\", \"server\": \"bjb1-32546\", \"gpu\": \"cuda:3\", \"pid\": 363783, \"data_path\": \"LIBERO-Object\", \"data_count\": \"10 tasks x 10 rollouts\", \"model_name\": \"openvla-7b + CRM obs_only\", \"seed\": 49, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\", \"eval_data\": \"LIBERO-Object (10 tasks x 10 rollouts)\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-obs-only-object-norm02-seed49.log\"}}, \"eval-random-selection-spatial-seed44\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-20T12:05:19.931Z\", \"updated_at\": \"2026-05-20T12:05:41.684Z\", \"spec\": {\"command\": \"python -u src/evaluate.py --mode random_selection --benchmark LIBERO-Spatial --seed 44 --n_rollouts 10\", \"server\": \"bjb1-18228\", \"gpu\": \"cuda:2\", \"pid\": 348897, \"data_path\": \"LIBERO-Spatial\", \"data_count\": \"10 tasks x 10 rollouts\", \"model_name\": \"openvla-7b + CRM obs_only\", \"seed\": 44, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\", \"eval_data\": \"LIBERO-Spatial (10 tasks x 10 rollouts)\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-random-selection-spatial-seed44.log\"}}, \"eval-random-selection-spatial-seed42\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-20T10:52:07.011Z\", \"updated_at\": \"2026-05-20T12:04:59.708Z\", \"spec\": {\"command\": \"python -u src/evaluate.py --mode random_selection --benchmark LIBERO-Spatial --seed 42 --n_rollouts 10\", \"server\": \"bjb1-18228\", \"gpu\": \"cuda:0\", \"pid\": 346801, \"data_path\": \"LIBERO-Spatial\", \"data_count\": \"10 tasks x 10 rollouts\", \"model_name\": \"openvla-7b + CRM obs_only\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\", \"eval_data\": \"LIBERO-Spatial (10 tasks x 10 rollouts)\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-random-selection-spatial-seed42.log\"}, \"notes\": \"原 bjb1-32546 上的重复副本(PID 360293/360306)已 kill。此实验实际在 bjb1-18228:cuda:0 运行(PID 346801, mass-deploy 部署)。\"}, \"eval-adaptive-k-spatial-p50-seed42\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-20T11:24:12.894Z\", \"updated_at\": \"2026-05-20T11:25:16.991Z\", \"conclusion\": \"success\", \"metrics\": {\"sr\": 30, \"avg_K\": 6.324, \"fast_path_pct\": 45.95, \"mean_l2\": 0.0903, \"total_rollouts\": 100}, \"failure_reason\": \"\", \"completed_at\": \"2026-05-20T11:06:00.000Z\", \"notes\": \"Reviewer 独立验证：JSON 完整，日志确认 SR=30%，PID 自然退出。之前被 cron 误判为 failed（PID dead + 无 sentinel），已修正为 success。\", \"spec\": {\"command\": \"python -u src/evaluate.py --mode adaptive_k --benchmark LIBERO-Spatial --seed 42 --n_rollouts 10 --adaptive_k_threshold 0.074855\", \"server\": \"bjb2-40593\", \"gpu\": \"cuda:0\", \"pid\": 681823, \"data_path\": \"LIBERO-Spatial\", \"data_count\": \"10 tasks x 10 rollouts\", \"model_name\": \"openvla-7b + CRM obs_only\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\", \"eval_data\": \"LIBERO-Spatial (10 tasks x 10 rollouts)\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-adaptive-k-spatial-p50-seed42.log\", \"checkpoint_path\": \"N/A (eval only)\"}, \"hypothesis\": \"Adaptive K with τ=P50 (0.074855, Object-calibrated) on LIBERO-Spatial seed42. 验证 Adaptive K 方法在第二个 benchmark 上的泛化：使用 Object 上校准的阈值直接应用到 Spatial（无 per-benchmark tuning）。如果 SR 接近 CRM K=10 (34.3%) 且 fast_path >50%，则证明方法跨 benchmark 通用。\"}, \"eval-obs-only-object-norm003-seed44\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-20T10:52:14.742Z\", \"updated_at\": \"2026-05-20T10:52:47.202Z\", \"hypothesis\": \"CRM obs_only ε=0.03 on Object seed44. Low-norm multi-seed supplement (plan_500): strengthens Figure 2 error bars at small ε.\", \"spec\": {\"command\": \"evaluate.py --mode crm_obs_only --benchmark object --seed 44 --n_rollouts 10 --K 10 --max_correction_norm 0.03\", \"server\": \"bjb2-28827\", \"seed\": 44, \"model_name\": \"crm_v3_norm/obs_only/crm_best.pt\", \"data_path\": \"LIBERO_object\", \"data_count\": 100}, \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-obs-only-object-norm003-seed44.log\", \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\", \"metrics\": {\"overall_success_rate\": 0.15, \"total_successes\": 15, \"total_rollouts\": 100, \"per_task\": {\"alphabet_soup\": 0, \"cream_cheese\": 0, \"salad_dressing\": 0.3, \"bbq_sauce\": 0.2, \"ketchup\": 0, \"tomato_sauce\": 0.1, \"butter\": 0.1, \"milk\": 0.2, \"chocolate_pudding\": 0.3, \"orange_juice\": 0.3}}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-20T10:52:47.202Z\"}, \"eval-adaptive-k-spatial-p90-seed42\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-20T10:52:05.759Z\", \"updated_at\": \"2026-05-20T10:52:38.383Z\", \"spec\": {\"command\": \"python -u src/evaluate.py --mode adaptive_k --benchmark LIBERO-Spatial --seed 42 --n_rollouts 10 --adaptive_k_threshold 0.125870 --output_file logs/eval-adaptive-k-spatial-p90-seed42.json\", \"server\": \"bjb2-28827\", \"gpu\": \"cuda:2\", \"pid\": 308030, \"data_path\": \"LIBERO-Spatial\", \"data_count\": \"10 tasks x 10 rollouts\", \"model_name\": \"openvla-7b + CRM obs_only\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\", \"eval_data\": \"LIBERO-Spatial (10 tasks x 10 rollouts)\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-adaptive-k-spatial-p90-seed42.log\"}}, \"eval-adaptive-k-spatial-p25-seed44\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-20T10:52:04.790Z\", \"updated_at\": \"2026-05-20T10:52:34.962Z\", \"spec\": {\"command\": \"python -u src/evaluate.py --mode adaptive_k --benchmark LIBERO-Spatial --seed 44 --n_rollouts 10 --adaptive_k_threshold 0.054959 --output_file logs/eval-adaptive-k-spatial-p25-seed44.json\", \"server\": \"bjb2-28827\", \"gpu\": \"cuda:1\", \"pid\": 307754, \"data_path\": \"LIBERO-Spatial\", \"data_count\": \"10 tasks x 10 rollouts\", \"model_name\": \"openvla-7b + CRM obs_only\", \"seed\": 44, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\", \"eval_data\": \"LIBERO-Spatial (10 tasks x 10 rollouts)\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-adaptive-k-spatial-p25-seed44.log\"}}, \"eval-adaptive-k-spatial-p75-seed44\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-20T10:52:04.320Z\", \"updated_at\": \"2026-05-20T10:52:32.674Z\", \"spec\": {\"command\": \"python -u src/evaluate.py --mode adaptive_k --benchmark LIBERO-Spatial --seed 44 --n_rollouts 10 --adaptive_k_threshold 0.098735 --output_file logs/eval-adaptive-k-spatial-p75-seed44.json\", \"server\": \"bjb2-28827\", \"gpu\": \"cuda:0\", \"pid\": 307478, \"data_path\": \"LIBERO-Spatial\", \"data_count\": \"10 tasks x 10 rollouts\", \"model_name\": \"openvla-7b + CRM obs_only\", \"seed\": 44, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\", \"eval_data\": \"LIBERO-Spatial (10 tasks x 10 rollouts)\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-adaptive-k-spatial-p75-seed44.log\"}}, \"eval-random-selection-object-seed46-r2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-19T17:41:16.541Z\", \"updated_at\": \"2026-05-19T17:41:32.255Z\", \"spec\": {\"command\": \"cd /root/acr-vla-conformal-refinement && timeout 57600 /root/miniconda3/bin/python -u src/evaluate.py --mode random_selection --benchmark object --n_rollouts 10 --seed 46 --K 10 --output_file logs/eval_object_random_selection_seed46.json\", \"server\": \"bjb2-40593\", \"data_path\": \"LIBERO-Object\", \"data_count\": 100, \"model_name\": \"SmolVLA_random_selection\", \"seed\": 46, \"checkpoint_path\": \"N/A-eval-only\", \"log_path\": \"/root/acr-vla-conformal-refinement/logs/eval_object_random_selection_seed46.log\"}, \"hypothesis\": \"Random selection baseline (K=10) on LIBERO-Object seed46 establishes reference success rate for comparing against CRM-guided selection methods\", \"conclusion\": \"killed\", \"completed_at\": \"2026-05-19T17:41:32.255Z\"}, \"eval-obs-only-spatial-norm02-seed46-r2\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-19T17:12:13.545Z\", \"updated_at\": \"2026-05-19T17:12:53.558Z\", \"hypothesis\": \"obs_only CRM with epsilon=0.2 and K=10 improves LIBERO-Spatial success rate by applying observation-conditioned conformal corrections to fix spatial reasoning errors, seed46 rerun for statistical robustness\", \"spec\": {\"command\": \"cd /root/acr-vla-conformal-refinement && /root/miniconda3/bin/python -u src/evaluate.py --mode crm_obs_only --benchmark spatial --n_rollouts 10 --seed 46 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --max_correction_norm 0.2 --output_file logs/eval_spatial_obs_only_norm02_seed46_r2.json\", \"server\": \"bjb2-28827\", \"gpu\": [\"cuda:3\"], \"data_path\": \"LIBERO-Spatial\", \"data_count\": 100, \"model_name\": \"SmolVLA+CRM_obs_only\", \"seed\": 46, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\", \"checkpoint_path\": \"N/A-eval-only\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-obs-only-spatial-norm02-seed46-r2.log\"}}, \"eval-vla-only-goal-seed44-r2\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-19T17:12:11.696Z\", \"updated_at\": \"2026-05-19T17:12:53.198Z\", \"hypothesis\": \"VLA-only baseline on LIBERO-Goal seed44 establishes reference success rate for comparing against CRM-augmented methods on goal-conditioned tasks, rerun for statistical robustness\", \"spec\": {\"command\": \"cd /root/acr-vla-conformal-refinement && /root/miniconda3/bin/python -u src/evaluate.py --mode vla_only --benchmark goal --n_rollouts 10 --seed 44 --K 1 --output_file logs/eval_goal_vla_only_seed44_r2.json\", \"server\": \"bjb2-28827\", \"gpu\": [\"cuda:0\"], \"data_path\": \"LIBERO-Goal\", \"data_count\": 100, \"model_name\": \"SmolVLA\", \"seed\": 44, \"checkpoint_path\": \"N/A-eval-only\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-vla-only-goal-seed44-r2.log\"}}, \"eval-argmin-object-k5-seed44-r2\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-19T17:12:10.271Z\", \"updated_at\": \"2026-05-19T17:12:52.978Z\", \"hypothesis\": \"ReConVLA argmin mode with K=5 candidates improves LIBERO-Object success rate over VLA-only baseline by selecting the best action from multiple VLA samples using conformal scoring, seed44 rerun for statistical robustness\", \"spec\": {\"command\": \"cd /root/acr-vla-conformal-refinement && /root/miniconda3/bin/python -u src/evaluate.py --mode reconvla --benchmark object --n_rollouts 10 --seed 44 --K 5 --output_file logs/eval_object_argmin_k5_seed44_r2.json\", \"server\": \"bjb2-28827\", \"gpu\": [\"cuda:1\"], \"data_path\": \"LIBERO-Object\", \"data_count\": 100, \"model_name\": \"SmolVLA_argmin\", \"seed\": 44, \"checkpoint_path\": \"N/A-eval-only\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-argmin-object-k5-seed44-r2.log\"}}, \"eval-openvla-object-baseline-seed42\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-19T17:12:07.506Z\", \"updated_at\": \"2026-05-19T17:12:46.396Z\", \"hypothesis\": \"OpenVLA baseline on LIBERO-Object seed42 establishes reference success rate for comparing against SmolVLA and CRM-augmented methods on object manipulation tasks\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/openvla-repo && CUDA_VISIBLE_DEVICES=4 TRANSFORMERS_OFFLINE=1 HF_HUB_OFFLINE=1 python experiments/robot/libero/run_libero_eval.py --model_family openvla --pretrained_checkpoint /root/autodl-tmp/models/openvla-libero-object --task_suite_name libero_object --center_crop True --seed 42 --num_trials_per_task 50 --use_wandb False\\\"\", \"server\": \"bjb2-28827\", \"gpu\": [\"cuda:4\"], \"data_path\": \"LIBERO-Object\", \"data_count\": 500, \"model_name\": \"OpenVLA\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/models/openvla-libero-object\", \"eval_data\": \"LIBERO-Object\", \"checkpoint_path\": \"N/A-eval-only\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-openvla-object-baseline-seed42.log\"}}, \"eval-obs-only-spatial-norm02-seed47\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-19T17:02:40.986Z\", \"updated_at\": \"2026-05-19T17:03:14.457Z\", \"metrics\": {\"success_rate\": 0.32, \"successes\": 32, \"total\": 100, \"n_tasks\": 10, \"n_rollouts\": 10, \"per_task\": {\"between_plate_and_ramekin\": 0.8, \"next_to_ramekin\": 0.9, \"from_table_center\": 0, \"on_cookie_box\": 0.3, \"in_top_drawer\": 0.1, \"on_ramekin\": 0, \"next_to_cookie_box\": 0.9, \"on_stove\": 0, \"next_to_plate\": 0.2, \"on_wooden_cabinet\": 0}}, \"checkpoint_path\": \"N/A-eval-only\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-obs-only-spatial-norm02-seed47.log\", \"conclusion\": \"success\", \"spec\": {\"command\": \"cd /root/acr-vla-conformal-refinement && /root/miniconda3/bin/python -u src/evaluate.py --mode crm_obs_only --benchmark spatial --n_rollouts 10 --seed 47 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --max_correction_norm 0.2 --output_file logs/eval_spatial_obs_only_norm02_seed47.json\", \"server\": \"bjb1-32546\", \"data_path\": \"LIBERO-Spatial\", \"data_count\": 100, \"model_name\": \"crm_obs_only\", \"seed\": 47}, \"hypothesis\": \"obs_only CRM with epsilon=0.2 and K=10 improves success rate over VLA-only baseline on LIBERO-Spatial because observation-conditioned conformal corrections can detect and fix spatial reasoning errors without requiring action history\", \"completed_at\": \"2026-05-19T17:03:14.457Z\"}, \"eval-vla-only-spatial-seed45\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-19T15:19:50.220Z\", \"updated_at\": \"2026-05-19T15:20:24.563Z\", \"spec\": {\"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-vla-only-spatial-seed45.log\", \"command\": \"python evaluate.py --benchmark spatial --mode vla_only --seed 45\", \"server\": \"bjb1-32546\", \"seed\": 45, \"data_path\": \"LIBERO-Spatial\", \"data_count\": 100, \"model_name\": \"SmolVLA\", \"checkpoint_path\": \"N/A (eval-only)\"}, \"metrics\": {\"success_rate\": 0.27, \"per_task\": {\"between_plate_and_ramekin\": 0.7, \"next_to_ramekin\": 0.9, \"from_table_center\": 0, \"on_cookie_box\": 0.2, \"in_top_drawer\": 0, \"on_ramekin\": 0, \"next_to_cookie_box\": 0.9, \"on_stove\": 0, \"next_to_plate\": 0, \"on_wooden_cabinet\": 0}, \"successes\": 27, \"total\": 100}, \"conclusion\": \"success\", \"hypothesis\": \"VLA-only baseline on LIBERO-Spatial with seed 45 establishes reference success rate for comparison with CRM-augmented methods\", \"completed_at\": \"2026-05-19T15:20:24.563Z\"}, \"eval-obs-only-spatial-norm02-seed44\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-19T14:23:33.161Z\", \"updated_at\": \"2026-05-19T14:26:44.810Z\", \"metrics\": {\"success_rate\": 0.36, \"successes\": 36, \"total\": 100}, \"checkpoint_path\": \"N/A (eval only)\", \"log_path\": \"/root/acr-vla-conformal-refinement/logs/eval_spatial_obs_only_norm02_seed44.json\", \"conclusion\": \"success\", \"spec\": {\"command\": \"python eval_crm.py --mode crm_obs_only --benchmark spatial --K 10 --seed 44 --max_correction_norm 0.2\", \"server\": \"bjb2-28827\", \"data_path\": \"spatial_benchmark\", \"data_count\": 100, \"model_name\": \"crm_obs_only\", \"seed\": 44}, \"hypothesis\": \"CRM obs-only mode with max_correction_norm=0.2 can improve spatial benchmark success rate by refining VLA actions using only observation-based conformal prediction, without access to privileged state information.\", \"completed_at\": \"2026-05-19T14:24:10.857Z\"}, \"eval-obs-only-object-norm003-seed43-r2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-19T05:14:10.523Z\", \"updated_at\": \"2026-05-19T05:14:25.385Z\", \"conclusion\": \"failed\", \"spec\": {\"checkpoint_path\": \"N/A (eval-only)\", \"log_path\": \"/root/acr-vla-conformal-refinement/logs/eval_object_obs_only_norm003_seed43.log\", \"metrics\": {\"success_rate\": null, \"tasks_completed\": \"1/10\", \"failure_reason\": \"process terminated prematurely after 1 task\"}}, \"completed_at\": \"2026-05-19T05:14:25.385Z\"}, \"eval-obs-only-object-norm03-seed48\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-18T13:26:49.122Z\", \"updated_at\": \"2026-05-18T13:27:19.389Z\", \"metrics\": {\"overall_success_rate\": 0.16, \"per_task\": {\"pick_up_the_alphabet_soup_and_place_it_in_the_basket\": 0, \"pick_up_the_cream_cheese_and_place_it_in_the_basket\": 0, \"pick_up_the_salad_dressing_and_place_it_in_the_basket\": 0.3, \"pick_up_the_bbq_sauce_and_place_it_in_the_basket\": 0.4, \"pick_up_the_ketchup_and_place_it_in_the_basket\": 0, \"pick_up_the_tomato_sauce_and_place_it_in_the_basket\": 0.1, \"pick_up_the_butter_and_place_it_in_the_basket\": 0.1, \"pick_up_the_milk_and_place_it_in_the_basket\": 0.1, \"pick_up_the_chocolate_pudding_and_place_it_in_the_basket\": 0.4, \"pick_up_the_orange_juice_and_place_it_in_the_basket\": 0.2}}, \"log_path\": \"/root/acr-vla-conformal-refinement/logs/eval_object_obs_only_norm03_seed48.json\", \"checkpoint_path\": \"N/A (eval only)\", \"conclusion\": \"success\", \"spec\": {\"command\": \"eval obs_only CRM epsilon=0.3 seed48 on LIBERO-Object K=10 n_rollouts=10\", \"server\": \"bjb1-18228\", \"data_path\": \"LIBERO-Object\", \"data_count\": 100, \"model_name\": \"openvla\", \"seed\": 48}, \"hypothesis\": \"CRM with obs_only mode and epsilon=0.3 normalization threshold will improve success rate on LIBERO-Object by filtering unreliable action predictions based solely on observation conformity scores\", \"completed_at\": \"2026-05-18T13:27:19.389Z\"}, \"eval-obs-only-object-norm01-seed48\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-18T11:42:37.233Z\", \"updated_at\": \"2026-05-18T11:43:15.403Z\", \"hypothesis\": \"obs_only CRM with max_correction_norm=0.1 on LIBERO-Object seed48. Tests whether obs_only mode with conservative norm clipping maintains performance across seeds.\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=1 /root/miniconda3/bin/python -u src/evaluate.py --mode crm_obs_only --benchmark object --n_rollouts 10 --seed 48 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --max_correction_norm 0.1 --output_file logs/eval_object_obs_only_norm01_seed48.json\", \"server\": \"bjb1-18228\", \"data_path\": \"LIBERO-Object\", \"data_count\": 100, \"model_name\": \"SmolVLA+CRM_obs_only\", \"seed\": 48, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\", \"eval_data\": \"LIBERO-Object\"}, \"log_path\": \"/root/acr-vla-conformal-refinement/logs/eval_object_obs_only_norm01_seed48.json\", \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.18, \"n_tasks\": 10, \"n_rollouts\": 10, \"per_task\": {\"alphabet_soup\": 0, \"cream_cheese\": 0, \"salad_dressing\": 0, \"bbq_sauce\": 0.4, \"ketchup\": 0.1, \"tomato_sauce\": 0.2, \"butter\": 0.2, \"milk\": 0.3, \"chocolate_pudding\": 0.3, \"orange_juice\": 0.3}}, \"completed_at\": \"2026-05-18T11:43:15.403Z\"}, \"eval-obs-only-object-norm02-k5-seed42\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-18T03:44:47.522Z\", \"updated_at\": \"2026-05-18T03:45:04.655Z\", \"conclusion\": \"success\", \"metrics\": {\"overall_sr\": 0.14, \"successes\": 14, \"rollouts\": 100, \"tasks\": 10, \"suite\": \"LIBERO-object\", \"seed\": 42, \"method\": \"crm_obs_only\", \"K\": 5, \"max_correction_norm\": 0.2}, \"hypothesis\": \"obs_only CRM with K=5 candidates and ε=0.2 on LIBERO-Object seed42. Tests whether fewer candidates (K=5 vs K=10) reduces selection quality. K=5 SR=14% vs K=10 SR=17.5% confirms monotonic improvement with more candidates.\", \"spec\": {\"command\": \"python -u src/evaluate.py --mode crm_obs_only --benchmark object --n_rollouts 10 --seed 42 --K 5 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --max_correction_norm 0.2 --output_file logs/eval_object_obs_only_norm02_k5_seed42.json\", \"server\": \"bjb1-18228\", \"data_path\": \"LIBERO-Object\", \"data_count\": 100, \"model_name\": \"SmolVLA+CRM_obs_only\", \"seed\": 42, \"K\": 5, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\", \"eval_data\": \"LIBERO-Object\", \"checkpoint_path\": \"N/A\", \"log_path\": \"/root/acr-vla-conformal-refinement/logs/eval_object_obs_only_norm02_k5_seed42.json\"}, \"completed_at\": \"2026-05-18T03:45:04.655Z\"}, \"eval-perdof-object-norm01-seed46\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-18T03:05:55.543Z\", \"updated_at\": \"2026-05-18T03:06:14.048Z\", \"hypothesis\": \"perdof CRM with ε=0.1 on LIBERO-Object seed46. Magnitude curve data point for perdof at intermediate norm. SR=10% confirms perdof degrades from peak at low norms.\", \"metrics\": {\"overall_sr\": 0.1, \"successes\": 10, \"rollouts\": 100, \"tasks\": 10, \"suite\": \"LIBERO-object\", \"seed\": 46, \"method\": \"crm_perdof\", \"max_correction_norm\": 0.1}, \"conclusion\": \"success\", \"spec\": {\"command\": \"python -u src/evaluate.py --mode crm_perdof --benchmark object --n_rollouts 10 --seed 46 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt --max_correction_norm 0.1 --output_file logs/eval_object_perdof_norm01_seed46.json\", \"server\": \"bjb1-32546\", \"data_path\": \"LIBERO-Object\", \"data_count\": 100, \"model_name\": \"SmolVLA+CRM_perdof\", \"seed\": 46, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt\", \"eval_data\": \"LIBERO-Object\", \"checkpoint_path\": \"N/A\", \"log_path\": \"/root/acr-vla-conformal-refinement/logs/eval_object_perdof_norm01_seed46.json\"}, \"completed_at\": \"2026-05-18T03:06:14.049Z\"}, \"eval-perdof-object-default-seed46\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-18T03:05:29.784Z\", \"updated_at\": \"2026-05-18T03:06:03.735Z\", \"conclusion\": \"negative\", \"hypothesis\": \"perdof CRM without norm constraint (uncapped correction magnitude) on LIBERO-Object seed46. Tests whether perdof maintains performance without explicit correction capping. SR=0% confirms perdof corrections are catastrophically unstable without norm constraints.\", \"spec\": {\"command\": \"python -u src/evaluate.py --mode crm_perdof --benchmark object --n_rollouts 10 --seed 46 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt --output_file logs/eval_object_perdof_default_seed46.json\", \"server\": \"bjb1-32546\", \"data_path\": \"LIBERO-Object\", \"data_count\": 100, \"model_name\": \"SmolVLA+CRM_perdof\", \"seed\": 46, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt\", \"eval_data\": \"LIBERO-Object\", \"checkpoint_path\": \"N/A\", \"log_path\": \"/root/acr-vla-conformal-refinement/logs/eval_object_perdof_default_seed46.json\"}, \"metrics\": {\"overall_sr\": 0, \"successes\": 0, \"rollouts\": 100, \"tasks\": 10, \"suite\": \"LIBERO-object\", \"seed\": 46, \"method\": \"crm_perdof\", \"max_correction_norm\": \"default\"}, \"completed_at\": \"2026-05-18T03:06:03.735Z\"}, \"eval-perdof-object-norm02-seed48\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-18T03:05:29.433Z\", \"updated_at\": \"2026-05-18T03:05:47.075Z\", \"hypothesis\": \"perdof CRM with ε=0.2 on LIBERO-Object seed48. Additional seed for perdof magnitude curve at primary comparison norm. Running on bjb2-28827 cuda:5 PID 488665.\", \"spec\": {\"command\": \"cd /root/acr-vla-conformal-refinement && CUDA_VISIBLE_DEVICES=5 python -u src/evaluate.py --mode crm_perdof --benchmark object --n_rollouts 10 --seed 48 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt --max_correction_norm 0.2 --output_file logs/eval_object_perdof_norm02_seed48.json\", \"server\": \"bjb2-28827\", \"data_path\": \"LIBERO-Object\", \"data_count\": 100, \"model_name\": \"SmolVLA+CRM_perdof\", \"seed\": 48, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt\", \"eval_data\": \"LIBERO-Object\"}}, \"eval-obs-only-object-default-seed46\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-18T00:59:50.348Z\", \"updated_at\": \"2026-05-18T01:00:23.165Z\", \"conclusion\": \"success\", \"metrics\": {\"overall_sr\": 0.15, \"successes\": 15, \"rollouts\": 100, \"tasks\": 10, \"suite\": \"LIBERO-object\", \"seed\": 46, \"method\": \"crm_obs_only\", \"max_correction_norm\": \"default\", \"per_task_sr\": {\"alphabet_soup\": 0, \"cream_cheese\": 0, \"salad_dressing\": 0.2, \"bbq_sauce\": 0.4, \"ketchup\": 0.1, \"tomato_sauce\": 0.1, \"butter\": 0.1, \"milk\": 0.1, \"chocolate_pudding\": 0.2, \"orange_juice\": 0.3}}, \"spec\": {\"checkpoint_path\": \"N/A\", \"log_path\": \"/root/acr-vla-conformal-refinement/logs/eval_object_obs_only_default_seed46.json\", \"command\": \"python -u src/evaluate.py --mode crm_obs_only --benchmark object --n_rollouts 10 --seed 46 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --output_file logs/eval_object_obs_only_default_seed46.json\", \"server\": \"bjb1-32546\", \"data_path\": \"LIBERO-Object\", \"data_count\": 100, \"model_name\": \"SmolVLA+CRM_obs_only\", \"seed\": 46, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\", \"eval_data\": \"LIBERO-Object\"}, \"hypothesis\": \"obs_only CRM without norm constraint (uncapped correction magnitude) on LIBERO-Object seed46. Tests whether obs_only maintains performance without explicit correction capping. If uncapped performs worse than capped, it confirms that moderate norm constraints stabilize corrections.\", \"completed_at\": \"2026-05-18T01:00:23.165Z\"}, \"eval-obs-only-object-norm01-seed46\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-18T00:42:56.715Z\", \"updated_at\": \"2026-05-18T00:43:09.191Z\", \"conclusion\": \"killed\", \"completed_at\": \"2026-05-18T00:43:09.191Z\"}, \"eval-k1-crm-multiscale-object-seed43\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-17T21:05:23.402Z\", \"updated_at\": \"2026-05-17T21:06:09.004Z\", \"hypothesis\": \"Multi-scale K=1 CRM with accumulated gradient refinement improves object manipulation success rate over baseline by providing conformal prediction-based action corrections at multiple spatial scales\", \"spec\": {\"command\": \"python -u src/evaluate.py --mode crm_k1_accg --benchmark object --n_rollouts 10 --seed 43\", \"server\": \"bjb1-32546\", \"data_path\": \"LIBERO-Object\", \"data_count\": 100, \"model_name\": \"SmolVLA+CRM_k1_accg\", \"seed\": 43, \"checkpoint_source\": \"crm_v3_norm\", \"eval_data\": \"LIBERO-Object\", \"checkpoint_path\": \"N/A\", \"log_path\": \"/root/acr-vla-conformal-refinement/logs/eval_k1_crm_multiscale_object_seed43.json\"}, \"conclusion\": \"negative\", \"metrics\": {\"overall_sr\": 0.09, \"successes\": 9, \"rollouts\": 100, \"tasks\": 10, \"suite\": \"LIBERO-object\", \"seed\": 43, \"method\": \"crm_k1_accg\", \"per_task\": {\"alphabet_soup\": 0, \"cream_cheese\": 0, \"salad_dressing\": 0.1, \"bbq_sauce\": 0.2, \"ketchup\": 0, \"tomato_sauce\": 0.2, \"butter\": 0, \"milk\": 0, \"chocolate_pudding\": 0.2, \"orange_juice\": 0.2}}, \"completed_at\": \"2026-05-17T21:06:09.004Z\"}, \"eval-k1-crm-multiscale-object-seed42\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-17T21:05:22.835Z\", \"updated_at\": \"2026-05-17T21:06:08.318Z\", \"hypothesis\": \"Multi-scale K=1 CRM with accumulated gradient refinement improves object manipulation success rate over baseline by providing conformal prediction-based action corrections at multiple spatial scales\", \"spec\": {\"command\": \"python -u src/evaluate.py --mode crm_k1_accg --benchmark object --n_rollouts 10 --seed 42\", \"server\": \"bjb2-28827\", \"data_path\": \"LIBERO-Object\", \"data_count\": 100, \"model_name\": \"SmolVLA+CRM_k1_accg\", \"seed\": 42, \"checkpoint_source\": \"crm_v3_norm\", \"eval_data\": \"LIBERO-Object\", \"checkpoint_path\": \"N/A\", \"log_path\": \"/root/acr-vla-conformal-refinement/logs/eval_k1_crm_multiscale_object_seed42.json\"}, \"conclusion\": \"negative\", \"metrics\": {\"overall_sr\": 0.12, \"successes\": 12, \"rollouts\": 100, \"tasks\": 10, \"suite\": \"LIBERO-object\", \"seed\": 42, \"method\": \"crm_k1_accg\", \"per_task\": {\"alphabet_soup\": 0, \"cream_cheese\": 0, \"salad_dressing\": 0.1, \"bbq_sauce\": 0.2, \"ketchup\": 0, \"tomato_sauce\": 0.3, \"butter\": 0.1, \"milk\": 0, \"chocolate_pudding\": 0.3, \"orange_juice\": 0.2}}, \"completed_at\": \"2026-05-17T21:06:08.318Z\"}, \"eval-obs-only-object-norm005-seed43\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-17T21:04:43.285Z\", \"updated_at\": \"2026-05-17T21:04:52.760Z\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=0 python -u src/evaluate.py --mode crm_obs_only --benchmark object --n_rollouts 10 --seed 43 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --max_correction_norm 0.05 --output_file logs/eval_object_obs_only_norm005_seed43.json\", \"server\": \"bjb2-28827\", \"data_path\": \"LIBERO-Object\", \"data_count\": 100, \"model_name\": \"SmolVLA+CRM_obs_only\", \"seed\": 43, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\", \"eval_data\": \"LIBERO-Object\"}}, \"eval-perdof-object-norm02-seed45-r3\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-17T21:02:26.375Z\", \"updated_at\": \"2026-05-17T21:04:50.614Z\", \"hypothesis\": \"perdof CRM (ε=0.2) seed45 on LIBERO-Object. Rerun after SIGHUP kill. Original result on bjb2-28827 was 9%. This confirms reproducibility on different server.\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=3 python -u src/evaluate.py --mode crm_perdof --benchmark object --n_rollouts 10 --seed 45 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt --max_correction_norm 0.2 --output_file logs/eval_object_perdof_norm02_seed45_r3.json\", \"server\": \"bjb1-18228\", \"data_path\": \"LIBERO-Object\", \"data_count\": 100, \"model_name\": \"SmolVLA+CRM_perdof\", \"seed\": 45, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt\", \"eval_data\": \"LIBERO-Object\"}}, \"eval-k1-crm-multiscale-object-seed44-r2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-17T20:55:44.755Z\", \"updated_at\": \"2026-05-17T20:56:16.602Z\", \"hypothesis\": \"Multi-scale K=1 CRM with accumulated gradient refinement improves object manipulation success rate over baseline by providing conformal prediction-based action corrections at multiple spatial scales\", \"spec\": {\"command\": \"python eval_libero.py --method crm_k1_accg --baseline_mode single --suite object --seed 44 --n_rollouts 10\", \"server\": \"bjb1-18228\", \"data_path\": \"LIBERO-object\", \"data_count\": 100, \"model_name\": \"crm_k1_multiscale\", \"seed\": 44, \"checkpoint_source\": \"crm-k1-train\", \"eval_data\": \"LIBERO-object\"}, \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/crm_k1/crm_k1_best.pt\", \"log_path\": \"/root/acr-vla-conformal-refinement/logs/eval_k1_crm_multiscale_object_seed44_bjb1-18228.json\", \"conclusion\": \"negative\", \"completed_at\": \"2026-05-17T20:56:12.165Z\", \"metrics\": {\"overall_sr\": 0.1, \"successes\": 10, \"rollouts\": 100, \"tasks\": 10, \"suite\": \"LIBERO-object\", \"seed\": 44, \"method\": \"crm_k1_accg\", \"per_task\": {\"alphabet_soup\": 0, \"cream_cheese\": 0, \"salad_dressing\": 0.2, \"bbq_sauce\": 0.1, \"ketchup\": 0, \"tomato_sauce\": 0.1, \"butter\": 0, \"milk\": 0, \"chocolate_pudding\": 0.4, \"orange_juice\": 0.2}}}, \"eval-mag-perdof-norm03-object-r3\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-16T11:05:32.773Z\", \"updated_at\": \"2026-05-16T11:06:06.108Z\", \"conclusion\": \"success\", \"spec\": {\"command\": \"python eval_libero.py --method crm_perdof --suite object --norm 0.3 --seed 42\", \"server\": \"bjb2-28827\", \"data_path\": \"LIBERO-object\", \"data_count\": 100, \"model_name\": \"crm_perdof_norm03\", \"seed\": 42, \"checkpoint_source\": \"crm-train-v3-perdof\", \"eval_data\": \"LIBERO-object\"}, \"log_path\": \"/root/acr-vla-conformal-refinement/logs/eval_object_perdof_norm03_r3.json\", \"checkpoint_path\": \"N/A\", \"completed_at\": \"2026-05-16T11:06:02.462Z\", \"metrics\": {\"success_rate\": 0.04, \"successes\": 4, \"rollouts\": 100, \"tasks\": 10, \"suite\": \"LIBERO-object\", \"norm\": 0.3, \"seed\": 42}}, \"eval-mag-perdof-norm005-object\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-16T08:30:31.627Z\", \"updated_at\": \"2026-05-16T08:30:52.155Z\", \"spec\": {\"command\": \"python evaluate.py --mode crm_perdof --benchmark object --max_correction_norm 0.05 --seed 42\", \"server\": \"bjb2-28827\", \"data_path\": \"/root/acr-vla-conformal-refinement/logs/eval_object_perdof_norm005.json\", \"data_count\": 100, \"model_name\": \"crm_v3_norm_perdof\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt\", \"eval_data\": \"LIBERO object benchmark\"}, \"conclusion\": \"negative\", \"checkpoint_path\": \"/root/acr-vla-conformal-refinement/logs/eval_object_perdof_norm005.json\", \"log_path\": \"/root/acr-vla-conformal-refinement/logs/nohup_eval_object_perdof_norm005.log\", \"completed_at\": \"2026-05-16T08:30:50.635Z\", \"metrics\": {\"overall_sr\": 0.14, \"per_task\": {\"alphabet_soup\": 0, \"cream_cheese\": 0, \"salad_dressing\": 0.2, \"bbq_sauce\": 0.4, \"ketchup\": 0, \"tomato_sauce\": 0, \"butter\": 0, \"milk\": 0.2, \"chocolate_pudding\": 0.4, \"orange_juice\": 0.2}}}, \"eval-mag-obsonly-norm03-object\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-16T07:41:31.617Z\", \"updated_at\": \"2026-05-16T07:41:53.597Z\", \"metrics\": {\"tasks_done\": 10, \"tasks_total\": 10, \"overall_sr\": 0.19, \"per_task_sr\": {\"alphabet_soup\": 0, \"cream_cheese\": 0, \"salad_dressing\": 0.3, \"bbq_sauce\": 0.3, \"ketchup\": 0, \"tomato_sauce\": 0.1, \"butter\": 0.2, \"milk\": 0.2, \"chocolate_pudding\": 0.5, \"orange_juice\": 0.3}}, \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\", \"log_path\": \"/root/acr-vla-conformal-refinement/logs/eval_object_obs_only_norm03.log\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-16T07:41:53.597Z\"}}, \"count\": 64, \"total\": 64, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.1861}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "e17f41b1-3dce-49fb-a9e5-f5dd86423ed8",
  "uuid": "fc64db4c-f6a1-47cc-b70a-b6fed1353ab1",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-8-projects-acr-vla-conformal-refinement/e17f41b1-3dce-49fb-a9e5-f5dd86423ed8/tool-results/toolu_01Py9xhR4gHWVtTXRbKimmKL.txt",
      "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"experiments\\\": {\\\"eval-obs-only-object-norm005-seed75\\\": {\\\"status\\\": \\\"PREPARING\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-21T02:56:05.523Z\\\", \\\"updated_at\\\": \\\"2026-05-21T02:56:12.611Z\\\", \\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"success_rate\\\": 0.15}}, \\\"eval-obs-only-object-norm01-seed74\\\": {\\\"status\\\": \\\"PREPARING\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-21T02:55:20.812Z\\\", \\\"updated_at\\\": \\\"2026-05-21T02:55:28.975Z\\\", \\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"success_rate\\\": 0.13}}, \\\"eval-obs-only-object-norm01-seed64\\\": {\\\"status\\\": \\\"PREPARING\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-21T02:54:30.053Z\\\", \\\"updated_at\\\": \\\"2026-05-21T02:54:30.754Z\\\", \\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"success_rate\\\": 0.15}}, \\\"eval-obs-only-object-norm003-seed73\\\": {\\\"status\\\": \\\"PREPARING\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-21T02:53:26.508Z\\\", \\\"updated_at\\\": \\\"2026-05-21T02:53:31.930Z\\\", \\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"success_rate\\\": 0.16}}, \\\"eval-obs-only-object-norm005-seed64\\\": {\\\"status\\\": \\\"PREPARING\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-21T02:52:33.605Z\\\", \\\"updated_at\\\": \\\"2026-05-21T02:52:37.242Z\\\", \\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"success_rate\\\": 0.15}}, \\\"eval-obs-only-object-norm003-seed65\\\": {\\\"status\\\": \\\"PREPARING\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-21T02:51:17.482Z\\\", \\\"updated_at\\\": \\\"2026-05-21T02:51:23.912Z\\\", \\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"success_rate\\\": 0.17}}, \\\"eval-obs-only-object-norm003-seed64\\\": {\\\"status\\\": \\\"PREPARING\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-21T02:51:17.026Z\\\", \\\"updated_at\\\": \\\"2026-05-21T02:51:23.446Z\\\", \\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"success_rate\\\": 0.17}}, \\\"eval-obs-only-object-norm003-seed63-r2\\\": {\\\"status\\\": \\\"PREPARING\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-21T02:51:19.045Z\\\", \\\"updated_at\\\": \\\"2026-05-21T02:51:19.046Z\\\", \\\"conclusion\\\": \\\"killed\\\"}, \\\"eval-obs-only-object-norm003-seed62-r2\\\": {\\\"status\\\": \\\"PREPARING\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-21T02:51:18.497Z\\\", \\\"updated_at\\\": \\\"2026-05-21T02:51:18.497Z\\\", \\\"conclusion\\\": \\\"killed\\\"}, \\\"eval-obs-only-object-norm005-seed65\\\": {\\\"status\\\": \\\"PREPARING\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-21T02:26:45.708Z\\\", \\\"updated_at\\\": \\\"2026-05-21T02:26:50.866Z\\\", \\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"success_rate\\\": 0.14}}, \\\"eval-obs-only-object-norm005-seed61\\\": {\\\"status\\\": \\\"PREPARING\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-21T01:54:41.975Z\\\", \\\"updated_at\\\": \\\"2026-05-21T01:54:46.787Z\\\", \\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"success_rate\\\": 0.15}}, \\\"eval-obs-only-object-norm01-seed60\\\": {\\\"status\\\": \\\"PREPARING\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-21T01:42:15.142Z\\\", \\\"updated_at\\\": \\\"2026-05-21T01:42:24.178Z\\\", \\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"success_rate\\\": 0.15}}, \\\"eval-obs-only-object-norm003-seed56\\\": {\\\"status\\\": \\\"PREPARING\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-21T01:42:14.531Z\\\", \\\"updated_at\\\": \\\"2026-05-21T01:42:23.974Z\\\", \\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"success_rate\\\": 0.15}}, \\\"eval-obs-only-object-norm01-seed66\\\": {\\\"status\\\": \\\"PREPARING\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-21T01:29:23.112Z\\\", \\\"updated_at\\\": \\\"2026-05-21T01:31:28.961Z\\\", \\\"pid\\\": 642775}, \\\"eval-obs-only-object-norm005-seed66\\\": {\\\"status\\\": \\\"PREPARING\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-21T01:29:22.550Z\\\", \\\"updated_at\\\": \\\"2026-05-21T01:31:28.635Z\\\", \\\"pid\\\": 642506}, \\\"eval-obs-only-object-norm003-seed66\\\": {\\\"status\\\": \\\"PREPARING\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-21T01:29:22.063Z\\\", \\\"updated_at\\\": \\\"2026-05-21T01:31:27.799Z\\\", \\\"pid\\\": 642428}, \\\"eval-obs-only-object-norm003-seed59\\\": {\\\"status\\\": \\\"PREPARING\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-21T01:23:09.866Z\\\", \\\"updated_at\\\": \\\"2026-05-21T01:23:22.549Z\\\", \\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"success_rate\\\": 0.13}}, \\\"eval-obs-only-object-norm005-seed58\\\": {\\\"status\\\": \\\"PREPARING\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-21T01:23:09.469Z\\\", \\\"updated_at\\\": \\\"2026-05-21T01:23:21.948Z\\\", \\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"success_rate\\\": 0.16}}, \\\"eval-obs-only-object-norm01-seed57\\\": {\\\"status\\\": \\\"PREPARING\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-21T01:23:08.871Z\\\", \\\"updated_at\\\": \\\"2026-05-21T01:23:21.444Z\\\", \\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"success_rate\\\": 0.19}}, \\\"eval-obs-only-object-norm005-seed63\\\": {\\\"status\\\": \\\"PREPARING\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-21T01:02:30.561Z\\\", \\\"updated_at\\\": \\\"2026-05-21T01:02:30.561Z\\\", \\\"conclusion\\\": \\\"killed\\\"}, \\\"eval-obs-only-object-norm005-seed62\\\": {\\\"status\\\": \\\"PREPARING\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-21T01:02:30.354Z\\\", \\\"updated_at\\\": \\\"2026-05-21T01:02:30.354Z\\\", \\\"conclusion\\\": \\\"killed\\\"}, \\\"eval-perdof-object-norm02-seed49\\\": {\\\"status\\\": \\\"DONE\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-20T15:59:12.635Z\\\", \\\"updated_at\\\": \\\"2026-05-20T15:59:54.757Z\\\", \\\"metrics\\\": {\\\"overall_success_rate\\\": 0.12, \\\"total_rollouts\\\": 100, \\\"total_successes\\\": 12, \\\"per_task_sr\\\": {\\\"alphabet_soup\\\": 0, \\\"cream_cheese\\\": 0, \\\"salad_dressing\\\": 0.1, \\\"bbq_sauce\\\": 0.2, \\\"ketchup\\\": 0, \\\"tomato_sauce\\\": 0, \\\"butter\\\": 0.1, \\\"milk\\\": 0.2, \\\"chocolate_pudding\\\": 0.4, \\\"orange_juice\\\": 0.2}}, \\\"log_path\\\": \\\"/root/acr-vla-conformal-refinement/logs/eval-perdof-object-norm02-seed49.log\\\", \\\"checkpoint_path\\\": \\\"/root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt\\\", \\\"spec\\\": {\\\"command\\\": \\\"python evaluate.py --mode crm_perdof --benchmark object --seed 49 --K 10 --max_correction_norm 0.2 --n_rollouts 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt --output_file logs/eval_perdof_object_norm02_seed49.json\\\", \\\"server\\\": \\\"bjb1-32546\\\", \\\"data_path\\\": \\\"LIBERO-Object\\\", \\\"data_count\\\": 100, \\\"model_name\\\": \\\"crm_perdof_norm02_K10\\\", \\\"seed\\\": 49, \\\"checkpoint_source\\\": \\\"/root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt\\\", \\\"eval_data\\\": \\\"LIBERO-Object\\\"}, \\\"hypothesis\\\": \\\"PerDoF CRM with norm-clipped corrections (epsilon=0.2, K=10) provides consistent improvement over baseline on LIBERO-Object across seeds; seed49 should yield SR in the 14-18% range consistent with seeds 43-48.\\\", \\\"conclusion\\\": \\\"success\\\", \\\"completed_at\\\": \\\"2026-05-20T15:59:54.757Z\\\"}, \\\"eval-obs-only-object-norm02-seed43-r3\\\": {\\\"status\\\": \\\"PREPARING\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-20T13:55:56.411Z\\\", \\\"updated_at\\\": \\\"2026-05-20T13:55:57.571Z\\\", \\\"conclusion\\\": \\\"failed\\\", \\\"failure_reason\\\": \\\"SIGHUP (tmux session terminated externally) at 8/10 tasks. No JSON output. r2 already has complete data (SR=16%), no retry needed.\\\"}, \\\"openvla-precompute-k1\\\": {\\\"status\\\": \\\"PREPARING\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-20T13:52:53.282Z\\\", \\\"updated_at\\\": \\\"2026-05-20T13:52:53.282Z\\\", \\\"notes\\\": \\\"GPU collision: cuda:3 被 Director P0-B 指令分配给 plan_702 seed43。预计算需要在 plan_702 完成后重启。原始提交: PID 365142, 处理 74507 timesteps from 500 demos. Output: /root/autodl-tmp/crm_cache_k1_openvla/object/. 特征维度: multi_scale_obs (4,4096), action_dim=6.\\\"}, \\\"eval-obs-only-goal-norm02-seed52\\\": {\\\"status\\\": \\\"DONE\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-20T12:05:20.840Z\\\", \\\"updated_at\\\": \\\"2026-05-20T12:58:35.610Z\\\", \\\"spec\\\": {\\\"command\\\": \\\"python -u src/evaluate.py --mode crm_obs_only --benchmark LIBERO-Goal --seed 52 --n_rollouts 10 --max_correction_norm 0.2\\\", \\\"server\\\": \\\"bjb1-32546\\\", \\\"gpu\\\": \\\"cuda:0\\\", \\\"pid\\\": 362579, \\\"data_path\\\": \\\"LIBERO-Goal\\\", \\\"data_count\\\": \\\"10 tasks x 10 rollouts\\\", \\\"model_name\\\": \\\"openvla-7b + CRM obs_only\\\", \\\"seed\\\": 52, \\\"checkpoint_source\\\": \\\"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\\\", \\\"eval_data\\\": \\\"LIBERO-Goal (10 tasks x 10 rollouts)\\\", \\\"log_path\\\": \\\"~/runs/acr-vla-conformal-refinement/eval-obs-only-goal-norm02-seed52.log\\\", \\\"checkpoint_path\\\": \\\"N/A (eval only)\\\"}, \\\"metrics\\\": {\\\"success_rate\\\": 0.68, \\\"successes\\\": 68, \\\"total\\\": 100, \\\"per_task_sr\\\": {\\\"open_middle_drawer_cabinet\\\": 0.7, \\\"put_bowl_on_stove\\\": 0.9, \\\"put_wine_bottle_on_cabinet\\\": 0.4, \\\"open_top_drawer_put_bowl\\\": 0.3, \\\"put_bowl_on_cabinet\\\": 0.8, \\\"push_plate_front_stove\\\": 0.8, \\\"put_cream_cheese_in_bowl\\\": 0.4, \\\"turn_on_stove\\\": 1, \\\"put_bowl_on_plate\\\": 1, \\\"put_wine_bottle_on_rack\\\": 0.5}}, \\\"conclusion\\\": \\\"success\\\", \\\"hypothesis\\\": \\\"CRM obs_only with K=10 and norm cap 0.2 improves SR on LIBERO-Goal by applying observation-conditioned corrections that compensate for VLA action prediction errors, providing a new seed for variance estimation.\\\", \\\"completed_at\\\": \\\"2026-05-20T12:58:26.417Z\\\", \\\"notes\\\": \\\"SR=68% on Goal seed52. Strong result; turn_on_stove and put_bowl_on_plate both 100%.\\\"}, \\\"eval-argmin-object-seed49\\\": {\\\"status\\\": \\\"DONE\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-20T12:05:22.690Z\\\", \\\"updated_at\\\": \\\"2026-05-20T12:58:34.569Z\\\", \\\"spec\\\": {\\\"command\\\": \\\"python -u src/evaluate.py --mode reconvla --benchmark LIBERO-Object --seed 49 --n_rollouts 10\\\", \\\"server\\\": \\\"bjb1-32546\\\", \\\"gpu\\\": \\\"cuda:5\\\", \\\"pid\\\": 364591, \\\"data_path\\\": \\\"LIBERO-Object\\\", \\\"data_count\\\": \\\"10 tasks x 10 rollouts\\\", \\\"model_name\\\": \\\"openvla-7b + CRM obs_only (argmin)\\\", \\\"seed\\\": 49, \\\"checkpoint_source\\\": \\\"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\\\", \\\"eval_data\\\": \\\"LIBERO-Object (10 tasks x 10 rollouts)\\\", \\\"log_path\\\": \\\"~/runs/acr-vla-conformal-refinement/eval-argmin-object-seed49.log\\\", \\\"checkpoint_path\\\": \\\"N/A (eval only)\\\"}, \\\"metrics\\\": {\\\"success_rate\\\": 0.16, \\\"successes\\\": 16, \\\"total\\\": 100, \\\"per_task_sr\\\": {\\\"alphabet_soup\\\": 0, \\\"cream_cheese\\\": 0, \\\"salad_dressing\\\": 0.2, \\\"bbq_sauce\\\": 0.4, \\\"ketchup\\\": 0, \\\"tomato_sauce\\\": 0.1, \\\"butter\\\": 0.1, \\\"milk\\\": 0.3, \\\"chocolate_pudding\\\": 0.3, \\\"orange_juice\\\": 0.2}}, \\\"conclusion\\\": \\\"success\\\", \\\"hypothesis\\\": \\\"Argmin (reconvla) selection among K=10 CRM refinements improves over single-step VLA on Object by choosing the candidate with lowest predicted residual, providing a multi-seed consistency check.\\\", \\\"completed_at\\\": \\\"2026-05-20T12:58:25.905Z\\\", \\\"notes\\\": \\\"SR=16% on Object seed49. Consistent with other argmin seeds on Object benchmark.\\\"}, \\\"eval-random-selection-spatial-seed43\\\": {\\\"status\\\": \\\"DONE\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-20T12:05:19.438Z\\\", \\\"updated_at\\\": \\\"2026-05-20T12:58:33.167Z\\\", \\\"spec\\\": {\\\"command\\\": \\\"python -u src/evaluate.py --mode random_selection --benchmark LIBERO-Spatial --seed 43 --n_rollouts 10\\\", \\\"server\\\": \\\"bjb1-18228\\\", \\\"gpu\\\": \\\"cuda:1\\\", \\\"pid\\\": 347075, \\\"data_path\\\": \\\"LIBERO-Spatial\\\", \\\"data_count\\\": \\\"10 tasks x 10 rollouts\\\", \\\"model_name\\\": \\\"openvla-7b + CRM obs_only\\\", \\\"seed\\\": 43, \\\"checkpoint_source\\\": \\\"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\\\", \\\"eval_data\\\": \\\"LIBERO-Spatial (10 tasks x 10 rollouts)\\\", \\\"log_path\\\": \\\"~/runs/acr-vla-conformal-refinement/eval-random-selection-spatial-seed43.log\\\", \\\"checkpoint_path\\\": \\\"N/A (eval only)\\\"}, \\\"metrics\\\": {\\\"success_rate\\\": 0.26, \\\"successes\\\": 26, \\\"total\\\": 100, \\\"per_task_sr\\\": {\\\"between_plate_ramekin\\\": 0.7, \\\"next_to_ramekin\\\": 0.9, \\\"table_center\\\": 0, \\\"cookie_box\\\": 0.1, \\\"top_drawer\\\": 0, \\\"on_ramekin\\\": 0, \\\"next_to_cookie_box\\\": 0.7, \\\"on_stove\\\": 0, \\\"next_to_plate\\\": 0.2, \\\"on_wooden_cabinet\\\": 0}}, \\\"conclusion\\\": \\\"success\\\", \\\"hypothesis\\\": \\\"Random candidate selection from K=10 CRM refinements serves as a lower-bound baseline, showing that informed selection (argmin) is necessary to achieve the full benefit of multi-step refinement on Spatial.\\\", \\\"completed_at\\\": \\\"2026-05-20T12:58:24.969Z\\\", \\\"notes\\\": \\\"SR=26% on Spatial seed43. Lower than argmin-based selection, confirming informed selection matters.\\\"}, \\\"eval-adaptive-k-spatial-p90-seed43\\\": {\\\"status\\\": \\\"DONE\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-20T10:52:06.660Z\\\", \\\"updated_at\\\": \\\"2026-05-20T12:58:31.849Z\\\", \\\"spec\\\": {\\\"command\\\": \\\"python -u src/evaluate.py --mode adaptive_k --benchmark LIBERO-Spatial --seed 43 --n_rollouts 10 --adaptive_k_threshold 0.125870 --output_file logs/eval-adaptive-k-spatial-p90-seed43.json\\\", \\\"server\\\": \\\"bjb1-18228\\\", \\\"gpu\\\": \\\"cuda:3\\\", \\\"pid\\\": 344852, \\\"data_path\\\": \\\"LIBERO-Spatial\\\", \\\"data_count\\\": \\\"10 tasks x 10 rollouts\\\", \\\"model_name\\\": \\\"openvla-7b + CRM obs_only\\\", \\\"seed\\\": 43, \\\"checkpoint_source\\\": \\\"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\\\", \\\"eval_data\\\": \\\"LIBERO-Spatial (10 tasks x 10 rollouts)\\\", \\\"log_path\\\": \\\"~/runs/acr-vla-conformal-refinement/eval-adaptive-k-spatial-p90-seed43.log\\\", \\\"checkpoint_path\\\": \\\"N/A (eval only)\\\"}, \\\"metrics\\\": {\\\"success_rate\\\": 0.32, \\\"successes\\\": 32, \\\"total\\\": 100, \\\"avg_K\\\": 3.6, \\\"fast_path_pct\\\": 80.2, \\\"mean_l2\\\": 0.0905, \\\"per_task_sr\\\": {\\\"between_plate_ramekin\\\": 0.7, \\\"next_to_ramekin\\\": 1, \\\"table_center\\\": 0.1, \\\"cookie_box\\\": 0.3, \\\"top_drawer\\\": 0, \\\"on_ramekin\\\": 0.1, \\\"next_to_cookie_box\\\": 0.8, \\\"on_stove\\\": 0, \\\"next_to_plate\\\": 0.2, \\\"on_wooden_cabinet\\\": 0}}, \\\"conclusion\\\": \\\"success\\\", \\\"hypothesis\\\": \\\"Adaptive K with P90 threshold (τ=0.1259) reduces average refinement steps while maintaining comparable SR to fixed K=10 on Spatial, because most states have low CRM residuals and can skip full refinement.\\\", \\\"completed_at\\\": \\\"2026-05-20T12:58:23.572Z\\\", \\\"notes\\\": \\\"SR=32%, avg_K=3.6 (vs fixed K=10), 80.2% fast-path. Adaptive K saves ~64% compute with seed43 on Spatial.\\\"}, \\\"eval-adaptive-k-object-p90-seed44\\\": {\\\"status\\\": \\\"DONE\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-20T12:45:08.564Z\\\", \\\"updated_at\\\": \\\"2026-05-20T12:45:37.089Z\\\", \\\"hypothesis\\\": \\\"Adaptive K with τ=P90 (0.125870) on LIBERO-Object seed44. P90 是最宽松的阈值——大部分 step fast-path (K=1)，仅在极高不确定性时用 K=10。验证 P90 在 Object 上的 SR/compute tradeoff。\\\", \\\"spec\\\": {\\\"command\\\": \\\"python -u src/evaluate.py --mode adaptive_k --benchmark LIBERO-Object --seed 44 --n_rollouts 10 --adaptive_k_threshold 0.125870\\\", \\\"server\\\": \\\"bjb2-28827\\\", \\\"data_path\\\": \\\"LIBERO-Object\\\", \\\"data_count\\\": \\\"10 tasks x 10 rollouts\\\", \\\"model_name\\\": \\\"openvla-7b + CRM obs_only\\\", \\\"seed\\\": 44, \\\"checkpoint_source\\\": \\\"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\\\", \\\"eval_data\\\": \\\"LIBERO-Object (10 tasks x 10 rollouts)\\\", \\\"log_path\\\": \\\"N/A (discovered by Reviewer)\\\", \\\"checkpoint_path\\\": \\\"N/A (eval only)\\\"}, \\\"metrics\\\": {\\\"sr\\\": 14, \\\"avg_K\\\": 2.58, \\\"fast_path_pct\\\": 92.8, \\\"total_rollouts\\\": 100}, \\\"conclusion\\\": \\\"success\\\", \\\"completed_at\\\": \\\"2026-05-20T12:45:37.089Z\\\"}, \\\"eval-adaptive-k-object-p90-seed43\\\": {\\\"status\\\": \\\"DONE\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-20T12:45:08.312Z\\\", \\\"updated_at\\\": \\\"2026-05-20T12:45:34.700Z\\\", \\\"hypothesis\\\": \\\"Adaptive K with τ=P90 (0.125870) on LIBERO-Object seed43. P90 是最宽松的阈值——大部分 step fast-path (K=1)，仅在极高不确定性时用 K=10。验证 P90 在 Object 上的 SR/compute tradeoff。\\\", \\\"spec\\\": {\\\"command\\\": \\\"python -u src/evaluate.py --mode adaptive_k --benchmark LIBERO-Object --seed 43 --n_rollouts 10 --adaptive_k_threshold 0.125870\\\", \\\"server\\\": \\\"bjb2-28827\\\", \\\"data_path\\\": \\\"LIBERO-Object\\\", \\\"data_count\\\": \\\"10 tasks x 10 rollouts\\\", \\\"model_name\\\": \\\"openvla-7b + CRM obs_only\\\", \\\"seed\\\": 43, \\\"checkpoint_source\\\": \\\"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\\\", \\\"eval_data\\\": \\\"LIBERO-Object (10 tasks x 10 rollouts)\\\", \\\"log_path\\\": \\\"N/A (discovered by Reviewer)\\\", \\\"checkpoint_path\\\": \\\"N/A (eval only)\\\"}, \\\"metrics\\\": {\\\"sr\\\": 14, \\\"avg_K\\\": 2.61, \\\"fast_path_pct\\\": 92.3, \\\"total_rollouts\\\": 100}, \\\"conclusion\\\": \\\"success\\\", \\\"completed_at\\\": \\\"2026-05-20T12:45:34.700Z\\\"}, \\\"eval-argmin-object-seed48\\\": {\\\"status\\\": \\\"RUNNING\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-20T12:05:22.501Z\\\", \\\"updated_at\\\": \\\"2026-05-20T12:05:49.680Z\\\", \\\"spec\\\": {\\\"command\\\": \\\"python -u src/evaluate.py --mode reconvla --benchmark LIBERO-Object --seed 48 --n_rollouts 10\\\", \\\"server\\\": \\\"bjb1-32546\\\", \\\"gpu\\\": \\\"cuda:4\\\", \\\"pid\\\": 364125, \\\"data_path\\\": \\\"LIBERO-Object\\\", \\\"data_count\\\": \\\"10 tasks x 10 rollouts\\\", \\\"model_name\\\": \\\"openvla-7b + CRM obs_only (argmin)\\\", \\\"seed\\\": 48, \\\"checkpoint_source\\\": \\\"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\\\", \\\"eval_data\\\": \\\"LIBERO-Object (10 tasks x 10 rollouts)\\\", \\\"log_path\\\": \\\"~/runs/acr-vla-conformal-refinement/eval-argmin-object-seed48.log\\\"}}, \\\"eval-obs-only-object-norm02-seed49\\\": {\\\"status\\\": \\\"RUNNING\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-20T12:05:21.387Z\\\", \\\"updated_at\\\": \\\"2026-05-20T12:05:49.425Z\\\", \\\"spec\\\": {\\\"command\\\": \\\"python -u src/evaluate.py --mode crm_obs_only --benchmark LIBERO-Object --seed 49 --n_rollouts 10 --max_correction_norm 0.2\\\", \\\"server\\\": \\\"bjb1-32546\\\", \\\"gpu\\\": \\\"cuda:3\\\", \\\"pid\\\": 363783, \\\"data_path\\\": \\\"LIBERO-Object\\\", \\\"data_count\\\": \\\"10 tasks x 10 rollouts\\\", \\\"model_name\\\": \\\"openvla-7b + CRM obs_only\\\", \\\"seed\\\": 49, \\\"checkpoint_source\\\": \\\"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\\\", \\\"eval_data\\\": \\\"LIBERO-Object (10 tasks x 10 rollouts)\\\", \\\"log_path\\\": \\\"~/runs/acr-vla-conformal-refinement/eval-obs-only-object-norm02-seed49.log\\\"}}, \\\"eval-random-selection-spatial-seed44\\\": {\\\"status\\\": \\\"RUNNING\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-20T12:05:19.931Z\\\", \\\"updated_at\\\": \\\"2026-05-20T12:05:41.684Z\\\", \\\"spec\\\": {\\\"command\\\": \\\"python -u src/evaluate.py --mode random_selection --benchmark LIBERO-Spatial --seed 44 --n_rollouts 10\\\", \\\"server\\\": \\\"bjb1-18228\\\", \\\"gpu\\\": \\\"cuda:2\\\", \\\"pid\\\": 348897, \\\"data_path\\\": \\\"LIBERO-Spatial\\\", \\\"data_count\\\": \\\"10 tasks x 10 rollouts\\\", \\\"model_name\\\": \\\"openvla-7b + CRM obs_only\\\", \\\"seed\\\": 44, \\\"checkpoint_source\\\": \\\"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\\\", \\\"eval_data\\\": \\\"LIBERO-Spatial (10 tasks x 10 rollouts)\\\", \\\"log_path\\\": \\\"~/runs/acr-vla-conformal-refinement/eval-random-selection-spatial-seed44.log\\\"}}, \\\"eval-random-selection-spatial-seed42\\\": {\\\"status\\\": \\\"RUNNING\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-20T10:52:07.011Z\\\", \\\"updated_at\\\": \\\"2026-05-20T12:04:59.708Z\\\", \\\"spec\\\": {\\\"command\\\": \\\"python -u src/evaluate.py --mode random_selection --benchmark LIBERO-Spatial --seed 42 --n_rollouts 10\\\", \\\"server\\\": \\\"bjb1-18228\\\", \\\"gpu\\\": \\\"cuda:0\\\", \\\"pid\\\": 346801, \\\"data_path\\\": \\\"LIBERO-Spatial\\\", \\\"data_count\\\": \\\"10 tasks x 10 rollouts\\\", \\\"model_name\\\": \\\"openvla-7b + CRM obs_only\\\", \\\"seed\\\": 42, \\\"checkpoint_source\\\": \\\"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\\\", \\\"eval_data\\\": \\\"LIBERO-Spatial (10 tasks x 10 rollouts)\\\", \\\"log_path\\\": \\\"~/runs/acr-vla-conformal-refinement/eval-random-selection-spatial-seed42.log\\\"}, \\\"notes\\\": \\\"原 bjb1-32546 上的重复副本(PID 360293/360306)已 kill。此实验实际在 bjb1-18228:cuda:0 运行(PID 346801, mass-deploy 部署)。\\\"}, \\\"eval-adaptive-k-spatial-p50-seed42\\\": {\\\"status\\\": \\\"DONE\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-20T11:24:12.894Z\\\", \\\"updated_at\\\": \\\"2026-05-20T11:25:16.991Z\\\", \\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"sr\\\": 30, \\\"avg_K\\\": 6.324, \\\"fast_path_pct\\\": 45.95, \\\"mean_l2\\\": 0.0903, \\\"total_rollouts\\\": 100}, \\\"failure_reason\\\": \\\"\\\", \\\"completed_at\\\": \\\"2026-05-20T11:06:00.000Z\\\", \\\"notes\\\": \\\"Reviewer 独立验证：JSON 完整，日志确认 SR=30%，PID 自然退出。之前被 cron 误判为 failed（PID dead + 无 sentinel），已修正为 success。\\\", \\\"spec\\\": {\\\"command\\\": \\\"python -u src/evaluate.py --mode adaptive_k --benchmark LIBERO-Spatial --seed 42 --n_rollouts 10 --adaptive_k_threshold 0.074855\\\", \\\"server\\\": \\\"bjb2-40593\\\", \\\"gpu\\\": \\\"cuda:0\\\", \\\"pid\\\": 681823, \\\"data_path\\\": \\\"LIBERO-Spatial\\\", \\\"data_count\\\": \\\"10 tasks x 10 rollouts\\\", \\\"model_name\\\": \\\"openvla-7b + CRM obs_only\\\", \\\"seed\\\": 42, \\\"checkpoint_source\\\": \\\"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\\\", \\\"eval_data\\\": \\\"LIBERO-Spatial (10 tasks x 10 rollouts)\\\", \\\"log_path\\\": \\\"~/runs/acr-vla-conformal-refinement/eval-adaptive-k-spatial-p50-seed42.log\\\", \\\"checkpoint_path\\\": \\\"N/A (eval only)\\\"}, \\\"hypothesis\\\": \\\"Adaptive K with τ=P50 (0.074855, Object-calibrated) on LIBERO-Spatial seed42. 验证 Adaptive K 方法在第二个 benchmark 上的泛化：使用 Object 上校准的阈值直接应用到 Spatial（无 per-benchmark tuning）。如果 SR 接近 CRM K=10 (34.3%) 且 fast_path >50%，则证明方法跨 benchmark 通用。\\\"}, \\\"eval-obs-only-object-norm003-seed44\\\": {\\\"status\\\": \\\"DONE\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-20T10:52:14.742Z\\\", \\\"updated_at\\\": \\\"2026-05-20T10:52:47.202Z\\\", \\\"hypothesis\\\": \\\"CRM obs_only ε=0.03 on Object seed44. Low-norm multi-seed supplement (plan_500): strengthens Figure 2 error bars at small ε.\\\", \\\"spec\\\": {\\\"command\\\": \\\"evaluate.py --mode crm_obs_only --benchmark object --seed 44 --n_rollouts 10 --K 10 --max_correction_norm 0.03\\\", \\\"server\\\": \\\"bjb2-28827\\\", \\\"seed\\\": 44, \\\"model_name\\\": \\\"crm_v3_norm/obs_only/crm_best.pt\\\", \\\"data_path\\\": \\\"LIBERO_object\\\", \\\"data_count\\\": 100}, \\\"log_path\\\": \\\"~/runs/acr-vla-conformal-refinement/eval-obs-only-object-norm003-seed44.log\\\", \\\"checkpoint_path\\\": \\\"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\\\", \\\"metrics\\\": {\\\"overall_success_rate\\\": 0.15, \\\"total_successes\\\": 15, \\\"total_rollouts\\\": 100, \\\"per_task\\\": {\\\"alphabet_soup\\\": 0, \\\"cream_cheese\\\": 0, \\\"salad_dressing\\\": 0.3, \\\"bbq_sauce\\\": 0.2, \\\"ketchup\\\": 0, \\\"tomato_sauce\\\": 0.1, \\\"butter\\\": 0.1, \\\"milk\\\": 0.2, \\\"chocolate_pudding\\\": 0.3, \\\"orange_juice\\\": 0.3}}, \\\"conclusion\\\": \\\"success\\\", \\\"completed_at\\\": \\\"2026-05-20T10:52:47.202Z\\\"}, \\\"eval-adaptive-k-spatial-p90-seed42\\\": {\\\"status\\\": \\\"RUNNING\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-20T10:52:05.759Z\\\", \\\"updated_at\\\": \\\"2026-05-20T10:52:38.383Z\\\", \\\"spec\\\": {\\\"command\\\": \\\"python -u src/evaluate.py --mode adaptive_k --benchmark LIBERO-Spatial --seed 42 --n_rollouts 10 --adaptive_k_threshold 0.125870 --output_file logs/eval-adaptive-k-spatial-p90-seed42.json\\\", \\\"server\\\": \\\"bjb2-28827\\\", \\\"gpu\\\": \\\"cuda:2\\\", \\\"pid\\\": 308030, \\\"data_path\\\": \\\"LIBERO-Spatial\\\", \\\"data_count\\\": \\\"10 tasks x 10 rollouts\\\", \\\"model_name\\\": \\\"openvla-7b + CRM obs_only\\\", \\\"seed\\\": 42, \\\"checkpoint_source\\\": \\\"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\\\", \\\"eval_data\\\": \\\"LIBERO-Spatial (10 tasks x 10 rollouts)\\\", \\\"log_path\\\": \\\"~/runs/acr-vla-conformal-refinement/eval-adaptive-k-spatial-p90-seed42.log\\\"}}, \\\"eval-adaptive-k-spatial-p25-seed44\\\": {\\\"status\\\": \\\"RUNNING\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-20T10:52:04.790Z\\\", \\\"updated_at\\\": \\\"2026-05-20T10:52:34.962Z\\\", \\\"spec\\\": {\\\"command\\\": \\\"python -u src/evaluate.py --mode adaptive_k --benchmark LIBERO-Spatial --seed 44 --n_rollouts 10 --adaptive_k_threshold 0.054959 --output_file logs/eval-adaptive-k-spatial-p25-seed44.json\\\", \\\"server\\\": \\\"bjb2-28827\\\", \\\"gpu\\\": \\\"cuda:1\\\", \\\"pid\\\": 307754, \\\"data_path\\\": \\\"LIBERO-Spatial\\\", \\\"data_count\\\": \\\"10 tasks x 10 rollouts\\\", \\\"model_name\\\": \\\"openvla-7b + CRM obs_only\\\", \\\"seed\\\": 44, \\\"checkpoint_source\\\": \\\"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\\\", \\\"eval_data\\\": \\\"LIBERO-Spatial (10 tasks x 10 rollouts)\\\", \\\"log_path\\\": \\\"~/runs/acr-vla-conformal-refinement/eval-adaptive-k-spatial-p25-seed44.log\\\"}}, \\\"eval-adaptive-k-spatial-p75-seed44\\\": {\\\"status\\\": \\\"RUNNING\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-20T10:52:04.320Z\\\", \\\"updated_at\\\": \\\"2026-05-20T10:52:32.674Z\\\", \\\"spec\\\": {\\\"command\\\": \\\"python -u src/evaluate.py --mode adaptive_k --benchmark LIBERO-Spatial --seed 44 --n_rollouts 10 --adaptive_k_threshold 0.098735 --output_file logs/eval-adaptive-k-spatial-p75-seed44.json\\\", \\\"server\\\": \\\"bjb2-28827\\\", \\\"gpu\\\": \\\"cuda:0\\\", \\\"pid\\\": 307478, \\\"data_path\\\": \\\"LIBERO-Spatial\\\", \\\"data_count\\\": \\\"10 tasks x 10 rollouts\\\", \\\"model_name\\\": \\\"openvla-7b + CRM obs_only\\\", \\\"seed\\\": 44, \\\"checkpoint_source\\\": \\\"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\\\", \\\"eval_data\\\": \\\"LIBERO-Spatial (10 tasks x 10 rollouts)\\\", \\\"log_path\\\": \\\"~/runs/acr-vla-conformal-refinement/eval-adaptive-k-spatial-p75-seed44.log\\\"}}, \\\"eval-random-selection-object-seed46-r2\\\": {\\\"status\\\": \\\"DONE\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-19T17:41:16.541Z\\\", \\\"updated_at\\\": \\\"2026-05-19T17:41:32.255Z\\\", \\\"spec\\\": {\\\"command\\\": \\\"cd /root/acr-vla-conformal-refinement && timeout 57600 /root/miniconda3/bin/python -u src/evaluate.py --mode random_selection --benchmark object --n_rollouts 10 --seed 46 --K 10 --output_file logs/eval_object_random_selection_seed46.json\\\", \\\"server\\\": \\\"bjb2-40593\\\", \\\"data_path\\\": \\\"LIBERO-Object\\\", \\\"data_count\\\": 100, \\\"model_name\\\": \\\"SmolVLA_random_selection\\\", \\\"seed\\\": 46, \\\"checkpoint_path\\\": \\\"N/A-eval-only\\\", \\\"log_path\\\": \\\"/root/acr-vla-conformal-refinement/logs/eval_object_random_selection_seed46.log\\\"}, \\\"hypothesis\\\": \\\"Random selection baseline (K=10) on LIBERO-Object seed46 establishes reference success rate for comparing against CRM-guided selection methods\\\", \\\"conclusion\\\": \\\"killed\\\", \\\"completed_at\\\": \\\"2026-05-19T17:41:32.255Z\\\"}, \\\"eval-obs-only-spatial-norm02-seed46-r2\\\": {\\\"status\\\": \\\"RUNNING\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-19T17:12:13.545Z\\\", \\\"updated_at\\\": \\\"2026-05-19T17:12:53.558Z\\\", \\\"hypothesis\\\": \\\"obs_only CRM with epsilon=0.2 and K=10 improves LIBERO-Spatial success rate by applying observation-conditioned conformal corrections to fix spatial reasoning errors, seed46 rerun for statistical robustness\\\", \\\"spec\\\": {\\\"command\\\": \\\"cd /root/acr-vla-conformal-refinement && /root/miniconda3/bin/python -u src/evaluate.py --mode crm_obs_only --benchmark spatial --n_rollouts 10 --seed 46 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --max_correction_norm 0.2 --output_file logs/eval_spatial_obs_only_norm02_seed46_r2.json\\\", \\\"server\\\": \\\"bjb2-28827\\\", \\\"gpu\\\": [\\\"cuda:3\\\"], \\\"data_path\\\": \\\"LIBERO-Spatial\\\", \\\"data_count\\\": 100, \\\"model_name\\\": \\\"SmolVLA+CRM_obs_only\\\", \\\"seed\\\": 46, \\\"checkpoint_source\\\": \\\"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\\\", \\\"checkpoint_path\\\": \\\"N/A-eval-only\\\", \\\"log_path\\\": \\\"~/runs/acr-vla-conformal-refinement/eval-obs-only-spatial-norm02-seed46-r2.log\\\"}}, \\\"eval-vla-only-goal-seed44-r2\\\": {\\\"status\\\": \\\"RUNNING\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-19T17:12:11.696Z\\\", \\\"updated_at\\\": \\\"2026-05-19T17:12:53.198Z\\\", \\\"hypothesis\\\": \\\"VLA-only baseline on LIBERO-Goal seed44 establishes reference success rate for comparing against CRM-augmented methods on goal-conditioned tasks, rerun for statistical robustness\\\", \\\"spec\\\": {\\\"command\\\": \\\"cd /root/acr-vla-conformal-refinement && /root/miniconda3/bin/python -u src/evaluate.py --mode vla_only --benchmark goal --n_rollouts 10 --seed 44 --K 1 --output_file logs/eval_goal_vla_only_seed44_r2.json\\\", \\\"server\\\": \\\"bjb2-28827\\\", \\\"gpu\\\": [\\\"cuda:0\\\"], \\\"data_path\\\": \\\"LIBERO-Goal\\\", \\\"data_count\\\": 100, \\\"model_name\\\": \\\"SmolVLA\\\", \\\"seed\\\": 44, \\\"checkpoint_path\\\": \\\"N/A-eval-only\\\", \\\"log_path\\\": \\\"~/runs/acr-vla-conformal-refinement/eval-vla-only-goal-seed44-r2.log\\\"}}, \\\"eval-argmin-object-k5-seed44-r2\\\": {\\\"status\\\": \\\"RUNNING\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-19T17:12:10.271Z\\\", \\\"updated_at\\\": \\\"2026-05-19T17:12:52.978Z\\\", \\\"hypothesis\\\": \\\"ReConVLA argmin mode with K=5 candidates improves LIBERO-Object success rate over VLA-only baseline by selecting the best action from multiple VLA samples using conformal scoring, seed44 rerun for statistical robustness\\\", \\\"spec\\\": {\\\"command\\\": \\\"cd /root/acr-vla-conformal-refinement && /root/miniconda3/bin/python -u src/evaluate.py --mode reconvla --benchmark object --n_rollouts 10 --seed 44 --K 5 --output_file logs/eval_object_argmin_k5_seed44_r2.json\\\", \\\"server\\\": \\\"bjb2-28827\\\", \\\"gpu\\\": [\\\"cuda:1\\\"], \\\"data_path\\\": \\\"LIBERO-Object\\\", \\\"data_count\\\": 100, \\\"model_name\\\": \\\"SmolVLA_argmin\\\", \\\"seed\\\": 44, \\\"checkpoint_path\\\": \\\"N/A-eval-only\\\", \\\"log_path\\\": \\\"~/runs/acr-vla-conformal-refinement/eval-argmin-object-k5-seed44-r2.log\\\"}}, \\\"eval-openvla-object-baseline-seed42\\\": {\\\"status\\\": \\\"RUNNING\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-19T17:12:07.506Z\\\", \\\"updated_at\\\": \\\"2026-05-19T17:12:46.396Z\\\", \\\"hypothesis\\\": \\\"OpenVLA baseline on LIBERO-Object seed42 establishes reference success rate for comparing against SmolVLA and CRM-augmented methods on object manipulation tasks\\\", \\\"spec\\\": {\\\"command\\\": \\\"bash -c \\\\\\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/openvla-repo && CUDA_VISIBLE_DEVICES=4 TRANSFORMERS_OFFLINE=1 HF_HUB_OFFLINE=1 python experiments/robot/libero/run_libero_eval.py --model_family openvla --pretrained_checkpoint /root/autodl-tmp/models/openvla-libero-object --task_suite_name libero_object --center_crop True --seed 42 --num_trials_per_task 50 --use_wandb False\\\\\\\"\\\", \\\"server\\\": \\\"bjb2-28827\\\", \\\"gpu\\\": [\\\"cuda:4\\\"], \\\"data_path\\\": \\\"LIBERO-Object\\\", \\\"data_count\\\": 500, \\\"model_name\\\": \\\"OpenVLA\\\", \\\"seed\\\": 42, \\\"checkpoint_source\\\": \\\"/root/autodl-tmp/models/openvla-libero-object\\\", \\\"eval_data\\\": \\\"LIBERO-Object\\\", \\\"checkpoint_path\\\": \\\"N/A-eval-only\\\", \\\"log_path\\\": \\\"~/runs/acr-vla-conformal-refinement/eval-openvla-object-baseline-seed42.log\\\"}}, \\\"eval-obs-only-spatial-norm02-seed47\\\": {\\\"status\\\": \\\"DONE\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-19T17:02:40.986Z\\\", \\\"updated_at\\\": \\\"2026-05-19T17:03:14.457Z\\\", \\\"metrics\\\": {\\\"success_rate\\\": 0.32, \\\"successes\\\": 32, \\\"total\\\": 100, \\\"n_tasks\\\": 10, \\\"n_rollouts\\\": 10, \\\"per_task\\\": {\\\"between_plate_and_ramekin\\\": 0.8, \\\"next_to_ramekin\\\": 0.9, \\\"from_table_center\\\": 0, \\\"on_cookie_box\\\": 0.3, \\\"in_top_drawer\\\": 0.1, \\\"on_ramekin\\\": 0, \\\"next_to_cookie_box\\\": 0.9, \\\"on_stove\\\": 0, \\\"next_to_plate\\\": 0.2, \\\"on_wooden_cabinet\\\": 0}}, \\\"checkpoint_path\\\": \\\"N/A-eval-only\\\", \\\"log_path\\\": \\\"~/runs/acr-vla-conformal-refinement/eval-obs-only-spatial-norm02-seed47.log\\\", \\\"conclusion\\\": \\\"success\\\", \\\"spec\\\": {\\\"command\\\": \\\"cd /root/acr-vla-conformal-refinement && /root/miniconda3/bin/python -u src/evaluate.py --mode crm_obs_only --benchmark spatial --n_rollouts 10 --seed 47 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --max_correction_norm 0.2 --output_file logs/eval_spatial_obs_only_norm02_seed47.json\\\", \\\"server\\\": \\\"bjb1-32546\\\", \\\"data_path\\\": \\\"LIBERO-Spatial\\\", \\\"data_count\\\": 100, \\\"model_name\\\": \\\"crm_obs_only\\\", \\\"seed\\\": 47}, \\\"hypothesis\\\": \\\"obs_only CRM with epsilon=0.2 and K=10 improves success rate over VLA-only baseline on LIBERO-Spatial because observation-conditioned conformal corrections can detect and fix spatial reasoning errors without requiring action history\\\", \\\"completed_at\\\": \\\"2026-05-19T17:03:14.457Z\\\"}, \\\"eval-vla-only-spatial-seed45\\\": {\\\"status\\\": \\\"DONE\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-19T15:19:50.220Z\\\", \\\"updated_at\\\": \\\"2026-05-19T15:20:24.563Z\\\", \\\"spec\\\": {\\\"log_path\\\": \\\"~/runs/acr-vla-conformal-refinement/eval-vla-only-spatial-seed45.log\\\", \\\"command\\\": \\\"python evaluate.py --benchmark spatial --mode vla_only --seed 45\\\", \\\"server\\\": \\\"bjb1-32546\\\", \\\"seed\\\": 45, \\\"data_path\\\": \\\"LIBERO-Spatial\\\", \\\"data_count\\\": 100, \\\"model_name\\\": \\\"SmolVLA\\\", \\\"checkpoint_path\\\": \\\"N/A (eval-only)\\\"}, \\\"metrics\\\": {\\\"success_rate\\\": 0.27, \\\"per_task\\\": {\\\"between_plate_and_ramekin\\\": 0.7, \\\"next_to_ramekin\\\": 0.9, \\\"from_table_center\\\": 0, \\\"on_cookie_box\\\": 0.2, \\\"in_top_drawer\\\": 0, \\\"on_ramekin\\\": 0, \\\"next_to_cookie_box\\\": 0.9, \\\"on_stove\\\": 0, \\\"next_to_plate\\\": 0, \\\"on_wooden_cabinet\\\": 0}, \\\"successes\\\": 27, \\\"total\\\": 100}, \\\"conclusion\\\": \\\"success\\\", \\\"hypothesis\\\": \\\"VLA-only baseline on LIBERO-Spatial with seed 45 establishes reference success rate for comparison with CRM-augmented methods\\\", \\\"completed_at\\\": \\\"2026-05-19T15:20:24.563Z\\\"}, \\\"eval-obs-only-spatial-norm02-seed44\\\": {\\\"status\\\": \\\"DONE\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-19T14:23:33.161Z\\\", \\\"updated_at\\\": \\\"2026-05-19T14:26:44.810Z\\\", \\\"metrics\\\": {\\\"success_rate\\\": 0.36, \\\"successes\\\": 36, \\\"total\\\": 100}, \\\"checkpoint_path\\\": \\\"N/A (eval only)\\\", \\\"log_path\\\": \\\"/root/acr-vla-conformal-refinement/logs/eval_spatial_obs_only_norm02_seed44.json\\\", \\\"conclusion\\\": \\\"success\\\", \\\"spec\\\": {\\\"command\\\": \\\"python eval_crm.py --mode crm_obs_only --benchmark spatial --K 10 --seed 44 --max_correction_norm 0.2\\\", \\\"server\\\": \\\"bjb2-28827\\\", \\\"data_path\\\": \\\"spatial_benchmark\\\", \\\"data_count\\\": 100, \\\"model_name\\\": \\\"crm_obs_only\\\", \\\"seed\\\": 44}, \\\"hypothesis\\\": \\\"CRM obs-only mode with max_correction_norm=0.2 can improve spatial benchmark success rate by refining VLA actions using only observation-based conformal prediction, without access to privileged state information.\\\", \\\"completed_at\\\": \\\"2026-05-19T14:24:10.857Z\\\"}, \\\"eval-obs-only-object-norm003-seed43-r2\\\": {\\\"status\\\": \\\"DONE\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-19T05:14:10.523Z\\\", \\\"updated_at\\\": \\\"2026-05-19T05:14:25.385Z\\\", \\\"conclusion\\\": \\\"failed\\\", \\\"spec\\\": {\\\"checkpoint_path\\\": \\\"N/A (eval-only)\\\", \\\"log_path\\\": \\\"/root/acr-vla-conformal-refinement/logs/eval_object_obs_only_norm003_seed43.log\\\", \\\"metrics\\\": {\\\"success_rate\\\": null, \\\"tasks_completed\\\": \\\"1/10\\\", \\\"failure_reason\\\": \\\"process terminated prematurely after 1 task\\\"}}, \\\"completed_at\\\": \\\"2026-05-19T05:14:25.385Z\\\"}, \\\"eval-obs-only-object-norm03-seed48\\\": {\\\"status\\\": \\\"DONE\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-18T13:26:49.122Z\\\", \\\"updated_at\\\": \\\"2026-05-18T13:27:19.389Z\\\", \\\"metrics\\\": {\\\"overall_success_rate\\\": 0.16, \\\"per_task\\\": {\\\"pick_up_the_alphabet_soup_and_place_it_in_the_basket\\\": 0, \\\"pick_up_the_cream_cheese_and_place_it_in_the_basket\\\": 0, \\\"pick_up_the_salad_dressing_and_place_it_in_the_basket\\\": 0.3, \\\"pick_up_the_bbq_sauce_and_place_it_in_the_basket\\\": 0.4, \\\"pick_up_the_ketchup_and_place_it_in_the_basket\\\": 0, \\\"pick_up_the_tomato_sauce_and_place_it_in_the_basket\\\": 0.1, \\\"pick_up_the_butter_and_place_it_in_the_basket\\\": 0.1, \\\"pick_up_the_milk_and_place_it_in_the_basket\\\": 0.1, \\\"pick_up_the_chocolate_pudding_and_place_it_in_the_basket\\\": 0.4, \\\"pick_up_the_orange_juice_and_place_it_in_the_basket\\\": 0.2}}, \\\"log_path\\\": \\\"/root/acr-vla-conformal-refinement/logs/eval_object_obs_only_norm03_seed48.json\\\", \\\"checkpoint_path\\\": \\\"N/A (eval only)\\\", \\\"conclusion\\\": \\\"success\\\", \\\"spec\\\": {\\\"command\\\": \\\"eval obs_only CRM epsilon=0.3 seed48 on LIBERO-Object K=10 n_rollouts=10\\\", \\\"server\\\": \\\"bjb1-18228\\\", \\\"data_path\\\": \\\"LIBERO-Object\\\", \\\"data_count\\\": 100, \\\"model_name\\\": \\\"openvla\\\", \\\"seed\\\": 48}, \\\"hypothesis\\\": \\\"CRM with obs_only mode and epsilon=0.3 normalization threshold will improve success rate on LIBERO-Object by filtering unreliable action predictions based solely on observation conformity scores\\\", \\\"completed_at\\\": \\\"2026-05-18T13:27:19.389Z\\\"}, \\\"eval-obs-only-object-norm01-seed48\\\": {\\\"status\\\": \\\"DONE\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-18T11:42:37.233Z\\\", \\\"updated_at\\\": \\\"2026-05-18T11:43:15.403Z\\\", \\\"hypothesis\\\": \\\"obs_only CRM with max_correction_norm=0.1 on LIBERO-Object seed48. Tests whether obs_only mode with conservative norm clipping maintains performance across seeds.\\\", \\\"spec\\\": {\\\"command\\\": \\\"CUDA_VISIBLE_DEVICES=1 /root/miniconda3/bin/python -u src/evaluate.py --mode crm_obs_only --benchmark object --n_rollouts 10 --seed 48 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --max_correction_norm 0.1 --output_file logs/eval_object_obs_only_norm01_seed48.json\\\", \\\"server\\\": \\\"bjb1-18228\\\", \\\"data_path\\\": \\\"LIBERO-Object\\\", \\\"data_count\\\": 100, \\\"model_name\\\": \\\"SmolVLA+CRM_obs_only\\\", \\\"seed\\\": 48, \\\"checkpoint_source\\\": \\\"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\\\", \\\"eval_data\\\": \\\"LIBERO-Object\\\"}, \\\"log_path\\\": \\\"/root/acr-vla-conformal-refinement/logs/eval_object_obs_only_norm01_seed48.json\\\", \\\"checkpoint_path\\\": \\\"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\\\", \\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"success_rate\\\": 0.18, \\\"n_tasks\\\": 10, \\\"n_rollouts\\\": 10, \\\"per_task\\\": {\\\"alphabet_soup\\\": 0, \\\"cream_cheese\\\": 0, \\\"salad_dressing\\\": 0, \\\"bbq_sauce\\\": 0.4, \\\"ketchup\\\": 0.1, \\\"tomato_sauce\\\": 0.2, \\\"butter\\\": 0.2, \\\"milk\\\": 0.3, \\\"chocolate_pudding\\\": 0.3, \\\"orange_juice\\\": 0.3}}, \\\"completed_at\\\": \\\"2026-05-18T11:43:15.403Z\\\"}, \\\"eval-obs-only-object-norm02-k5-seed42\\\": {\\\"status\\\": \\\"DONE\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-18T03:44:47.522Z\\\", \\\"updated_at\\\": \\\"2026-05-18T03:45:04.655Z\\\", \\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"overall_sr\\\": 0.14, \\\"successes\\\": 14, \\\"rollouts\\\": 100, \\\"tasks\\\": 10, \\\"suite\\\": \\\"LIBERO-object\\\", \\\"seed\\\": 42, \\\"method\\\": \\\"crm_obs_only\\\", \\\"K\\\": 5, \\\"max_correction_norm\\\": 0.2}, \\\"hypothesis\\\": \\\"obs_only CRM with K=5 candidates and ε=0.2 on LIBERO-Object seed42. Tests whether fewer candidates (K=5 vs K=10) reduces selection quality. K=5 SR=14% vs K=10 SR=17.5% confirms monotonic improvement with more candidates.\\\", \\\"spec\\\": {\\\"command\\\": \\\"python -u src/evaluate.py --mode crm_obs_only --benchmark object --n_rollouts 10 --seed 42 --K 5 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --max_correction_norm 0.2 --output_file logs/eval_object_obs_only_norm02_k5_seed42.json\\\", \\\"server\\\": \\\"bjb1-18228\\\", \\\"data_path\\\": \\\"LIBERO-Object\\\", \\\"data_count\\\": 100, \\\"model_name\\\": \\\"SmolVLA+CRM_obs_only\\\", \\\"seed\\\": 42, \\\"K\\\": 5, \\\"checkpoint_source\\\": \\\"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\\\", \\\"eval_data\\\": \\\"LIBERO-Object\\\", \\\"checkpoint_path\\\": \\\"N/A\\\", \\\"log_path\\\": \\\"/root/acr-vla-conformal-refinement/logs/eval_object_obs_only_norm02_k5_seed42.json\\\"}, \\\"completed_at\\\": \\\"2026-05-18T03:45:04.655Z\\\"}, \\\"eval-perdof-object-norm01-seed46\\\": {\\\"status\\\": \\\"DONE\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-18T03:05:55.543Z\\\", \\\"updated_at\\\": \\\"2026-05-18T03:06:14.048Z\\\", \\\"hypothesis\\\": \\\"perdof CRM with ε=0.1 on LIBERO-Object seed46. Magnitude curve data point for perdof at intermediate norm. SR=10% confirms perdof degrades from peak at low norms.\\\", \\\"metrics\\\": {\\\"overall_sr\\\": 0.1, \\\"successes\\\": 10, \\\"rollouts\\\": 100, \\\"tasks\\\": 10, \\\"suite\\\": \\\"LIBERO-object\\\", \\\"seed\\\": 46, \\\"method\\\": \\\"crm_perdof\\\", \\\"max_correction_norm\\\": 0.1}, \\\"conclusion\\\": \\\"success\\\", \\\"spec\\\": {\\\"command\\\": \\\"python -u src/evaluate.py --mode crm_perdof --benchmark object --n_rollouts 10 --seed 46 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt --max_correction_norm 0.1 --output_file logs/eval_object_perdof_norm01_seed46.json\\\", \\\"server\\\": \\\"bjb1-32546\\\", \\\"data_path\\\": \\\"LIBERO-Object\\\", \\\"data_count\\\": 100, \\\"model_name\\\": \\\"SmolVLA+CRM_perdof\\\", \\\"seed\\\": 46, \\\"checkpoint_source\\\": \\\"/root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt\\\", \\\"eval_data\\\": \\\"LIBERO-Object\\\", \\\"checkpoint_path\\\": \\\"N/A\\\", \\\"log_path\\\": \\\"/root/acr-vla-conformal-refinement/logs/eval_object_perdof_norm01_seed46.json\\\"}, \\\"completed_at\\\": \\\"2026-05-18T03:06:14.049Z\\\"}, \\\"eval-perdof-object-default-seed46\\\": {\\\"status\\\": \\\"DONE\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-18T03:05:29.784Z\\\", \\\"updated_at\\\": \\\"2026-05-18T03:06:03.735Z\\\", \\\"conclusion\\\": \\\"negative\\\", \\\"hypothesis\\\": \\\"perdof CRM without norm constraint (uncapped correction magnitude) on LIBERO-Object seed46. Tests whether perdof maintains performance without explicit correction capping. SR=0% confirms perdof corrections are catastrophically unstable without norm constraints.\\\", \\\"spec\\\": {\\\"command\\\": \\\"python -u src/evaluate.py --mode crm_perdof --benchmark object --n_rollouts 10 --seed 46 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt --output_file logs/eval_object_perdof_default_seed46.json\\\", \\\"server\\\": \\\"bjb1-32546\\\", \\\"data_path\\\": \\\"LIBERO-Object\\\", \\\"data_count\\\": 100, \\\"model_name\\\": \\\"SmolVLA+CRM_perdof\\\", \\\"seed\\\": 46, \\\"checkpoint_source\\\": \\\"/root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt\\\", \\\"eval_data\\\": \\\"LIBERO-Object\\\", \\\"checkpoint_path\\\": \\\"N/A\\\", \\\"log_path\\\": \\\"/root/acr-vla-conformal-refinement/logs/eval_object_perdof_default_seed46.json\\\"}, \\\"metrics\\\": {\\\"overall_sr\\\": 0, \\\"successes\\\": 0, \\\"rollouts\\\": 100, \\\"tasks\\\": 10, \\\"suite\\\": \\\"LIBERO-object\\\", \\\"seed\\\": 46, \\\"method\\\": \\\"crm_perdof\\\", \\\"max_correction_norm\\\": \\\"default\\\"}, \\\"completed_at\\\": \\\"2026-05-18T03:06:03.735Z\\\"}, \\\"eval-perdof-object-norm02-seed48\\\": {\\\"status\\\": \\\"RUNNING\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-18T03:05:29.433Z\\\", \\\"updated_at\\\": \\\"2026-05-18T03:05:47.075Z\\\", \\\"hypothesis\\\": \\\"perdof CRM with ε=0.2 on LIBERO-Object seed48. Additional seed for perdof magnitude curve at primary comparison norm. Running on bjb2-28827 cuda:5 PID 488665.\\\", \\\"spec\\\": {\\\"command\\\": \\\"cd /root/acr-vla-conformal-refinement && CUDA_VISIBLE_DEVICES=5 python -u src/evaluate.py --mode crm_perdof --benchmark object --n_rollouts 10 --seed 48 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt --max_correction_norm 0.2 --output_file logs/eval_object_perdof_norm02_seed48.json\\\", \\\"server\\\": \\\"bjb2-28827\\\", \\\"data_path\\\": \\\"LIBERO-Object\\\", \\\"data_count\\\": 100, \\\"model_name\\\": \\\"SmolVLA+CRM_perdof\\\", \\\"seed\\\": 48, \\\"checkpoint_source\\\": \\\"/root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt\\\", \\\"eval_data\\\": \\\"LIBERO-Object\\\"}}, \\\"eval-obs-only-object-default-seed46\\\": {\\\"status\\\": \\\"DONE\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-18T00:59:50.348Z\\\", \\\"updated_at\\\": \\\"2026-05-18T01:00:23.165Z\\\", \\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"overall_sr\\\": 0.15, \\\"successes\\\": 15, \\\"rollouts\\\": 100, \\\"tasks\\\": 10, \\\"suite\\\": \\\"LIBERO-object\\\", \\\"seed\\\": 46, \\\"method\\\": \\\"crm_obs_only\\\", \\\"max_correction_norm\\\": \\\"default\\\", \\\"per_task_sr\\\": {\\\"alphabet_soup\\\": 0, \\\"cream_cheese\\\": 0, \\\"salad_dressing\\\": 0.2, \\\"bbq_sauce\\\": 0.4, \\\"ketchup\\\": 0.1, \\\"tomato_sauce\\\": 0.1, \\\"butter\\\": 0.1, \\\"milk\\\": 0.1, \\\"chocolate_pudding\\\": 0.2, \\\"orange_juice\\\": 0.3}}, \\\"spec\\\": {\\\"checkpoint_path\\\": \\\"N/A\\\", \\\"log_path\\\": \\\"/root/acr-vla-conformal-refinement/logs/eval_object_obs_only_default_seed46.json\\\", \\\"command\\\": \\\"python -u src/evaluate.py --mode crm_obs_only --benchmark object --n_rollouts 10 --seed 46 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --output_file logs/eval_object_obs_only_default_seed46.json\\\", \\\"server\\\": \\\"bjb1-32546\\\", \\\"data_path\\\": \\\"LIBERO-Object\\\", \\\"data_count\\\": 100, \\\"model_name\\\": \\\"SmolVLA+CRM_obs_only\\\", \\\"seed\\\": 46, \\\"checkpoint_source\\\": \\\"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\\\", \\\"eval_data\\\": \\\"LIBERO-Object\\\"}, \\\"hypothesis\\\": \\\"obs_only CRM without norm constraint (uncapped correction magnitude) on LIBERO-Object seed46. Tests whether obs_only maintains performance without explicit correction capping. If uncapped performs worse than capped, it confirms that moderate norm constraints stabilize corrections.\\\", \\\"completed_at\\\": \\\"2026-05-18T01:00:23.165Z\\\"}, \\\"eval-obs-only-object-norm01-seed46\\\": {\\\"status\\\": \\\"DONE\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-18T00:42:56.715Z\\\", \\\"updated_at\\\": \\\"2026-05-18T00:43:09.191Z\\\", \\\"conclusion\\\": \\\"killed\\\", \\\"completed_at\\\": \\\"2026-05-18T00:43:09.191Z\\\"}, \\\"eval-k1-crm-multiscale-object-seed43\\\": {\\\"status\\\": \\\"DONE\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-17T21:05:23.402Z\\\", \\\"updated_at\\\": \\\"2026-05-17T21:06:09.004Z\\\", \\\"hypothesis\\\": \\\"Multi-scale K=1 CRM with accumulated gradient refinement improves object manipulation success rate over baseline by providing conformal prediction-based action corrections at multiple spatial scales\\\", \\\"spec\\\": {\\\"command\\\": \\\"python -u src/evaluate.py --mode crm_k1_accg --benchmark object --n_rollouts 10 --seed 43\\\", \\\"server\\\": \\\"bjb1-32546\\\", \\\"data_path\\\": \\\"LIBERO-Object\\\", \\\"data_count\\\": 100, \\\"model_name\\\": \\\"SmolVLA+CRM_k1_accg\\\", \\\"seed\\\": 43, \\\"checkpoint_source\\\": \\\"crm_v3_norm\\\", \\\"eval_data\\\": \\\"LIBERO-Object\\\", \\\"checkpoint_path\\\": \\\"N/A\\\", \\\"log_path\\\": \\\"/root/acr-vla-conformal-refinement/logs/eval_k1_crm_multiscale_object_seed43.json\\\"}, \\\"conclusion\\\": \\\"negative\\\", \\\"metrics\\\": {\\\"overall_sr\\\": 0.09, \\\"successes\\\": 9, \\\"rollouts\\\": 100, \\\"tasks\\\": 10, \\\"suite\\\": \\\"LIBERO-object\\\", \\\"seed\\\": 43, \\\"method\\\": \\\"crm_k1_accg\\\", \\\"per_task\\\": {\\\"alphabet_soup\\\": 0, \\\"cream_cheese\\\": 0, \\\"salad_dressing\\\": 0.1, \\\"bbq_sauce\\\": 0.2, \\\"ketchup\\\": 0, \\\"tomato_sauce\\\": 0.2, \\\"butter\\\": 0, \\\"milk\\\": 0, \\\"chocolate_pudding\\\": 0.2, \\\"orange_juice\\\": 0.2}}, \\\"completed_at\\\": \\\"2026-05-17T21:06:09.004Z\\\"}, \\\"eval-k1-crm-multiscale-object-seed42\\\": {\\\"status\\\": \\\"DONE\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-17T21:05:22.835Z\\\", \\\"updated_at\\\": \\\"2026-05-17T21:06:08.318Z\\\", \\\"hypothesis\\\": \\\"Multi-scale K=1 CRM with accumulated gradient refinement improves object manipulation success rate over baseline by providing conformal prediction-based action corrections at multiple spatial scales\\\", \\\"spec\\\": {\\\"command\\\": \\\"python -u src/evaluate.py --mode crm_k1_accg --benchmark object --n_rollouts 10 --seed 42\\\", \\\"server\\\": \\\"bjb2-28827\\\", \\\"data_path\\\": \\\"LIBERO-Object\\\", \\\"data_count\\\": 100, \\\"model_name\\\": \\\"SmolVLA+CRM_k1_accg\\\", \\\"seed\\\": 42, \\\"checkpoint_source\\\": \\\"crm_v3_norm\\\", \\\"eval_data\\\": \\\"LIBERO-Object\\\", \\\"checkpoint_path\\\": \\\"N/A\\\", \\\"log_path\\\": \\\"/root/acr-vla-conformal-refinement/logs/eval_k1_crm_multiscale_object_seed42.json\\\"}, \\\"conclusion\\\": \\\"negative\\\", \\\"metrics\\\": {\\\"overall_sr\\\": 0.12, \\\"successes\\\": 12, \\\"rollouts\\\": 100, \\\"tasks\\\": 10, \\\"suite\\\": \\\"LIBERO-object\\\", \\\"seed\\\": 42, \\\"method\\\": \\\"crm_k1_accg\\\", \\\"per_task\\\": {\\\"alphabet_soup\\\": 0, \\\"cream_cheese\\\": 0, \\\"salad_dressing\\\": 0.1, \\\"bbq_sauce\\\": 0.2, \\\"ketchup\\\": 0, \\\"tomato_sauce\\\": 0.3, \\\"butter\\\": 0.1, \\\"milk\\\": 0, \\\"chocolate_pudding\\\": 0.3, \\\"orange_juice\\\": 0.2}}, \\\"completed_at\\\": \\\"2026-05-17T21:06:08.318Z\\\"}, \\\"eval-obs-only-object-norm005-seed43\\\": {\\\"status\\\": \\\"RUNNING\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-17T21:04:43.285Z\\\", \\\"updated_at\\\": \\\"2026-05-17T21:04:52.760Z\\\", \\\"spec\\\": {\\\"command\\\": \\\"CUDA_VISIBLE_DEVICES=0 python -u src/evaluate.py --mode crm_obs_only --benchmark object --n_rollouts 10 --seed 43 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --max_correction_norm 0.05 --output_file logs/eval_object_obs_only_norm005_seed43.json\\\", \\\"server\\\": \\\"bjb2-28827\\\", \\\"data_path\\\": \\\"LIBERO-Object\\\", \\\"data_count\\\": 100, \\\"model_name\\\": \\\"SmolVLA+CRM_obs_only\\\", \\\"seed\\\": 43, \\\"checkpoint_source\\\": \\\"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\\\", \\\"eval_data\\\": \\\"LIBERO-Object\\\"}}, \\\"eval-perdof-object-norm02-seed45-r3\\\": {\\\"status\\\": \\\"RUNNING\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-17T21:02:26.375Z\\\", \\\"updated_at\\\": \\\"2026-05-17T21:04:50.614Z\\\", \\\"hypothesis\\\": \\\"perdof CRM (ε=0.2) seed45 on LIBERO-Object. Rerun after SIGHUP kill. Original result on bjb2-28827 was 9%. This confirms reproducibility on different server.\\\", \\\"spec\\\": {\\\"command\\\": \\\"CUDA_VISIBLE_DEVICES=3 python -u src/evaluate.py --mode crm_perdof --benchmark object --n_rollouts 10 --seed 45 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt --max_correction_norm 0.2 --output_file logs/eval_object_perdof_norm02_seed45_r3.json\\\", \\\"server\\\": \\\"bjb1-18228\\\", \\\"data_path\\\": \\\"LIBERO-Object\\\", \\\"data_count\\\": 100, \\\"model_name\\\": \\\"SmolVLA+CRM_perdof\\\", \\\"seed\\\": 45, \\\"checkpoint_source\\\": \\\"/root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt\\\", \\\"eval_data\\\": \\\"LIBERO-Object\\\"}}, \\\"eval-k1-crm-multiscale-object-seed44-r2\\\": {\\\"status\\\": \\\"DONE\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-17T20:55:44.755Z\\\", \\\"updated_at\\\": \\\"2026-05-17T20:56:16.602Z\\\", \\\"hypothesis\\\": \\\"Multi-scale K=1 CRM with accumulated gradient refinement improves object manipulation success rate over baseline by providing conformal prediction-based action corrections at multiple spatial scales\\\", \\\"spec\\\": {\\\"command\\\": \\\"python eval_libero.py --method crm_k1_accg --baseline_mode single --suite object --seed 44 --n_rollouts 10\\\", \\\"server\\\": \\\"bjb1-18228\\\", \\\"data_path\\\": \\\"LIBERO-object\\\", \\\"data_count\\\": 100, \\\"model_name\\\": \\\"crm_k1_multiscale\\\", \\\"seed\\\": 44, \\\"checkpoint_source\\\": \\\"crm-k1-train\\\", \\\"eval_data\\\": \\\"LIBERO-object\\\"}, \\\"checkpoint_path\\\": \\\"/root/autodl-tmp/checkpoints/crm_k1/crm_k1_best.pt\\\", \\\"log_path\\\": \\\"/root/acr-vla-conformal-refinement/logs/eval_k1_crm_multiscale_object_seed44_bjb1-18228.json\\\", \\\"conclusion\\\": \\\"negative\\\", \\\"completed_at\\\": \\\"2026-05-17T20:56:12.165Z\\\", \\\"metrics\\\": {\\\"overall_sr\\\": 0.1, \\\"successes\\\": 10, \\\"rollouts\\\": 100, \\\"tasks\\\": 10, \\\"suite\\\": \\\"LIBERO-object\\\", \\\"seed\\\": 44, \\\"method\\\": \\\"crm_k1_accg\\\", \\\"per_task\\\": {\\\"alphabet_soup\\\": 0, \\\"cream_cheese\\\": 0, \\\"salad_dressing\\\": 0.2, \\\"bbq_sauce\\\": 0.1, \\\"ketchup\\\": 0, \\\"tomato_sauce\\\": 0.1, \\\"butter\\\": 0, \\\"milk\\\": 0, \\\"chocolate_pudding\\\": 0.4, \\\"orange_juice\\\": 0.2}}}, \\\"eval-mag-perdof-norm03-object-r3\\\": {\\\"status\\\": \\\"DONE\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-16T11:05:32.773Z\\\", \\\"updated_at\\\": \\\"2026-05-16T11:06:06.108Z\\\", \\\"conclusion\\\": \\\"success\\\", \\\"spec\\\": {\\\"command\\\": \\\"python eval_libero.py --method crm_perdof --suite object --norm 0.3 --seed 42\\\", \\\"server\\\": \\\"bjb2-28827\\\", \\\"data_path\\\": \\\"LIBERO-object\\\", \\\"data_count\\\": 100, \\\"model_name\\\": \\\"crm_perdof_norm03\\\", \\\"seed\\\": 42, \\\"checkpoint_source\\\": \\\"crm-train-v3-perdof\\\", \\\"eval_data\\\": \\\"LIBERO-object\\\"}, \\\"log_path\\\": \\\"/root/acr-vla-conformal-refinement/logs/eval_object_perdof_norm03_r3.json\\\", \\\"checkpoint_path\\\": \\\"N/A\\\", \\\"completed_at\\\": \\\"2026-05-16T11:06:02.462Z\\\", \\\"metrics\\\": {\\\"success_rate\\\": 0.04, \\\"successes\\\": 4, \\\"rollouts\\\": 100, \\\"tasks\\\": 10, \\\"suite\\\": \\\"LIBERO-object\\\", \\\"norm\\\": 0.3, \\\"seed\\\": 42}}, \\\"eval-mag-perdof-norm005-object\\\": {\\\"status\\\": \\\"DONE\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-16T08:30:31.627Z\\\", \\\"updated_at\\\": \\\"2026-05-16T08:30:52.155Z\\\", \\\"spec\\\": {\\\"command\\\": \\\"python evaluate.py --mode crm_perdof --benchmark object --max_correction_norm 0.05 --seed 42\\\", \\\"server\\\": \\\"bjb2-28827\\\", \\\"data_path\\\": \\\"/root/acr-vla-conformal-refinement/logs/eval_object_perdof_norm005.json\\\", \\\"data_count\\\": 100, \\\"model_name\\\": \\\"crm_v3_norm_perdof\\\", \\\"seed\\\": 42, \\\"checkpoint_source\\\": \\\"/root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt\\\", \\\"eval_data\\\": \\\"LIBERO object benchmark\\\"}, \\\"conclusion\\\": \\\"negative\\\", \\\"checkpoint_path\\\": \\\"/root/acr-vla-conformal-refinement/logs/eval_object_perdof_norm005.json\\\", \\\"log_path\\\": \\\"/root/acr-vla-conformal-refinement/logs/nohup_eval_object_perdof_norm005.log\\\", \\\"completed_at\\\": \\\"2026-05-16T08:30:50.635Z\\\", \\\"metrics\\\": {\\\"overall_sr\\\": 0.14, \\\"per_task\\\": {\\\"alphabet_soup\\\": 0, \\\"cream_cheese\\\": 0, \\\"salad_dressing\\\": 0.2, \\\"bbq_sauce\\\": 0.4, \\\"ketchup\\\": 0, \\\"tomato_sauce\\\": 0, \\\"butter\\\": 0, \\\"milk\\\": 0.2, \\\"chocolate_pudding\\\": 0.4, \\\"orange_juice\\\": 0.2}}}, \\\"eval-mag-obsonly-norm03-object\\\": {\\\"status\\\": \\\"DONE\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-16T07:41:31.617Z\\\", \\\"updated_at\\\": \\\"2026-05-16T07:41:53.597Z\\\", \\\"metrics\\\": {\\\"tasks_done\\\": 10, \\\"tasks_total\\\": 10, \\\"overall_sr\\\": 0.19, \\\"per_task_sr\\\": {\\\"alphabet_soup\\\": 0, \\\"cream_cheese\\\": 0, \\\"salad_dressing\\\": 0.3, \\\"bbq_sauce\\\": 0.3, \\\"ketchup\\\": 0, \\\"tomato_sauce\\\": 0.1, \\\"butter\\\": 0.2, \\\"milk\\\": 0.2, \\\"chocolate_pudding\\\": 0.5, \\\"orange_juice\\\": 0.3}}, \\\"checkpoint_path\\\": \\\"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\\\", \\\"log_path\\\": \\\"/root/acr-vla-conformal-refinement/logs/eval_object_obs_only_norm03.log\\\", \\\"conclusion\\\": \\\"success\\\", \\\"completed_at\\\": \\\"2026-05-16T07:41:53.597Z\\\"}}, \\\"count\\\": 64, \\\"total\\\": 64, \\\"baseline\\\": null}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.1861}}\"}",
      "numLines": 1,
      "startLine": 1,
      "totalLines": 1
    }
  }
}
```

</details>

---

### Assistant

_source line 18_

<details><summary>Logged reasoning block</summary>

```text
Now I have all 64 experiments. Let me extract the norm sweep experiments. These are `eval-obs-only-object-norm{003,005,01,02}-seed*` with conclusion=success.

Let me go through all experiments and categorize them:

**ε=0.03 (norm003):**
- eval-obs-only-object-norm003-seed75: PREPARING, conclusion=success, SR=0.15 (success_rate)
- eval-obs-only-object-norm003-seed73: PREPARING, conclusion=success, SR=0.16


- eval-obs-only-object-norm003-seed65: PREPARING, conclusion=success, SR=0.17
- eval-obs-only-object-norm003-seed64: PREPARING, conclusion=success, SR=0.17
- eval-obs-only-object-norm003-seed56: PREPARING, conclusion=success, SR=0.15
- eval-obs-only-object-norm003-seed59: PREPARING, conclusion=success, SR=0.13

I'm also noting a couple of killed runs and one that's still in progress without metrics yet.

Now looking at the completed runs for seed 44 and 43, which brings the total successful seeds for ε=0.03 up to seven. Moving on to the ε=0.05 results, I'm seeing four seeds with success conclusions and success rates hovering around 0.14-0.15.

Continuing through the ε=0.05 batch, a couple of seeds were killed during preparation, one is still running without metrics yet, and another is actively running. That gives me five successful seeds for this epsilon value. Starting to compile the ε=0.1 results now, where I'm tracking similar patterns of completion and success rates. I'm noticing most of the norm02 experiments are either still running or failed, with only one relevant seed showing success so far. The roadmap indicated there should be twelve norm02 experiments, but I'm not finding them all—they might be registered under different naming patterns than I expected, so I need to search more broadly through all experiments matching the obs_only + object + norm=0.2 criteria. I'm finding very few norm02 experiments in the registry—just a couple with different naming patterns—so the original data must be stored elsewhere, possibly in the report or memory files under different experiment IDs than what I'd expect.

Looking through the full registry more systematically, I can see the obs_only + object experiments span multiple epsilon values: norm003 through norm03, with norm02 being notably sparse compared to the others, plus a default variant. I need to search through all 64 experiments systematically to find ones matching the obs_only + object pattern with ε=0.2. The registry file is quite large, so let me grep through it for the relevant experiment names rather than manually scanning everything. I'm wondering if the original norm02 experiments might be registered under simpler names like "eval-obs-only-object-seed42" without the "norm02" prefix, but I'm not seeing those in the output at all. Let me check the memory or report files for consolidated norm02 data instead. 我需要检查那些虽然还在 PREPARING 状态但已经有结论和指标的实验，因为这些可能是结果已经记录但还未完全处理的实验。同时我应该查看 report.md 和 memory.md 来找到可能被整合的 norm02 数据，特别是那些可能用不同命名方式但 ε=0.2 的实验。

现在让我汇总所有 ε=0.03 的成功实验，包括 PREPARING 和 DONE 状态的，计算它们的平均成功率。

7 个实验的成功率分别是 15%、16%、17%、17%、15%、13%、15%，平均值约为 15.43%，标准差约为 1.40%。接下来看 ε=0.05 的成功实验...

Actually, let me reconsider - I'm looking at the success rates for the ε=0.05 group now. Five seeds with success rates of 15%, 15%, 14%, 15%, and 16% give a mean of 15% with a standard deviation of 0.71%. Now moving on to the ε=0.1 group with five different seeds showing success rates of 13%, 15%, 15%, 19%, and 18%, which averages to 16% with higher variability.

For the ε=0.2 experiments, I'm checking what's actually available in the registry. I can see one running job and one completed job with K=5, but nothing that matches the expected pattern with K=10. The roadmap indicates there should be 12 norm02 experiments with a mean of 17.2%, but I'm not finding them in the current registry. I need to look elsewhere, maybe in the report.md file to track down where this data actually is.

Looking at the broader norm sweep, I see several experiments across different epsilon values in various states—some running, some preparing. The original norm02 baseline experiments might predate the current naming convention, so I should check the historical records to understand how they were originally labeled.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "e17f41b1-3dce-49fb-a9e5-f5dd86423ed8",
  "uuid": "bc69ae62-ec27-4935-a27f-5c2785397fb1",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014xDxRDBVhrYYMaaaLQndcZ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 21796,
      "cache_read_input_tokens": 43930,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 21796
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

_source line 19_

registry 中 norm02 命名的实验极少，n=12 的数据可能在 report 或 memory 中。让我查一下。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "e17f41b1-3dce-49fb-a9e5-f5dd86423ed8",
  "uuid": "2a5190e3-25a3-434f-bd52-c8f43ccd6bd1",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014xDxRDBVhrYYMaaaLQndcZ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 21796,
      "cache_read_input_tokens": 43930,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 21796
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

_source line 20_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01JzaSLbhGPbvsSb9pLN7d1Q`</summary>

```json
{
  "project": "acr-vla-conformal-refinement",
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
  "session_id": "e17f41b1-3dce-49fb-a9e5-f5dd86423ed8",
  "uuid": "d88da0b9-f02e-4087-b3f5-a32ef4494f93",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014xDxRDBVhrYYMaaaLQndcZ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 21796,
      "cache_read_input_tokens": 43930,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 21796
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

_source line 21 · 2026-05-21T03:24:08.177Z_

<details><summary>↩ Tool result · `toolu_01JzaSLbhGPbvsSb9pLN7d1Q`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/report.md\", \"content\": \"&lt;!-- AUTO-FACTS-BEGIN (generated 2026-05-21T03:12:13Z; do not edit — regenerated by auto_build_report_facts) -->\\n## 📊 当前状态（auto-derived from registry）\\n\\n**总计**: 546 个实验 — DEPLOYED 5, DONE 498, PREPARING 35, RUNNING 8\\n**DONE 分布**: failed 55, killed 90, negative 38, success 315\\n\\n### GPU 占用\\n- **实际运行**: 8 张 — bjb2-28827:cuda:0(eval-adaptive-k-spatial-p90-seed44-bjb2), bjb1-18228:cuda:0(eval-obs-only-object-norm003-seed66), bjb1-18228:cuda:2(eval-obs-only-object-norm005-seed66), bjb1-18228:cuda:3(eval-obs-only-object-norm01-seed66), bjb2-40593:cuda:0(eval-pi05-baseline-object-seed42), bjb2-28827:cuda:5(eval-obs-only-object-norm003-seed67), bjb1-32546:cuda:2(eval-obs-only-object-norm005-seed67), bjb1-18228:cuda:1(eval-obs-only-object-norm01-seed67)\\n\\n### 💾 磁盘余量\\n- **bjb2-40593**:\\n  - `/init`: 150M/150M 可用（已用 0%）\\n  - `/autodl-pub/data`: 5.7T/10T 可用（已用 44%）\\n  - `/usr/bin/nvidia-smi`: 44G/437G 可用（已用 90%） ⚠️\\n- **bjb1-18228**:\\n  - `/autodl-pub`: 603G/7.0T 可用（已用 92%） ⚠️\\n  - `/autodl-pub/data`: 5.7T/10T 可用（已用 44%）\\n  - `/usr/bin/nvidia-smi`: 400G/438G 可用（已用 4%）\\n- **bjb1-32546**:\\n  - `/autodl-pub`: 1.1T/7.0T 可用（已用 86%）\\n  - `/autodl-pub/data`: 5.7T/10T 可用（已用 44%）\\n  - `/usr/bin/nvidia-smi`: 400G/438G 可用（已用 4%）\\n- **bjb2-28827**:\\n  - `/autodl-pub`: 4.5T/14T 可用（已用 69%）\\n  - `/autodl-pub/data`: 5.7T/10T 可用（已用 44%）\\n  - `/usr/bin/nvidia-smi`: 399G/439G 可用（已用 5%）\\n\\n### 🏃 RUNNING\\n| exp_id | server | gpu | pid | log |\\n|--------|--------|-----|-----|-----|\\n| `eval-adaptive-k-spatial-p90-seed44-bjb2` | bjb2-28827 | cuda:0 | 975409 | `…refinement/logs/eval-adaptive-k-spatial-p90-seed44-bjb2.log` |\\n| `eval-obs-only-object-norm003-seed66` | bjb1-18228 | cuda:0 | 642428 | `—` |\\n| `eval-obs-only-object-norm005-seed66` | bjb1-18228 | cuda:2 | 642506 | `—` |\\n| `eval-obs-only-object-norm01-seed66` | bjb1-18228 | cuda:3 | 642775 | `—` |\\n| `eval-pi05-baseline-object-seed42` | bjb2-40593 | cuda:0 | 802634 | `—` |\\n| `eval-obs-only-object-norm003-seed67` | bjb2-28827 | cuda:5 | 969788 | `—` |\\n| `eval-obs-only-object-norm005-seed67` | bjb1-32546 | cuda:2 | 805840 | `—` |\\n| `eval-obs-only-object-norm01-seed67` | bjb1-18228 | cuda:1 | 666593 | `—` |\\n\\n### 📌 最近完成 (top 5)\\n- `eval-obs-only-object-norm005-seed72` [success] — 2026-05-21T03:11:58 — process dead 5× with no sentinel/W&B — auto-resolved as failed\\n- `eval-obs-only-object-norm01-seed71` [success] — 2026-05-21T03:11:54 — process dead 5× with no sentinel/W&B — auto-resolved as failed\\n- `eval-obs-only-object-norm01-seed51-r3` [success] — 2026-05-21T03:11:43\\n- `eval-obs-only-object-norm003-seed73` [success] — 2026-05-21T03:11:37\\n- `eval-obs-only-object-norm005-seed75` [success] — 2026-05-21T03:11:12 — process dead 5× with no sentinel/W&B — auto-resolved as failed\\n\\n&lt;!-- AUTO-FACTS-END -->\\n\\n---\\n\\n# Handover — 2026-05-21\\n\\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\\n\\n## 运行中\\n| exp_id | 假设 | 状态 | 关键指标 | W&B |\\n|--------|------|------|---------|-----|\\n| eval-adaptive-k-spatial-p90-seed44-bjb2 | Adaptive K with τ=P90 (0.125870) on LIBERO-Spatial seed44. Third seed completing Spatial P90 cross-benchmark sweep. | — | — | — |\\n\\n## 待处理\\n- eval-obs-only-object-norm005-seed77: CRM obs_only (ε=0.05) K=10 on LIBERO-Object seed77. Norm sweep seed balance for ε=0.05 condition, expanding sample size for statistical robustness.（准备中）\\n- eval-obs-only-object-norm003-seed76（准备中）\\n- …另有 34 项\\n\\n## 近期结论\\n- **eval-obs-only-object-norm01-seed71** (success): CRM obs_only (ε=0.1) K=10 on LIBERO-Object seed71. Norm sweep filling ε=0.1 gap.\\n\\n## 趋势\\n成功 315 / 负向 38 / 失败 55 / 共 498\\noverall_success_rate: 0.16 →（近 3 次 success）\\n\\n## 下一步\\n（无活跃 idea，请通过 ideas.md 添加）\\n\\n## 资源状态\\nbjb1-18228: 无 GPU 信息\\nbjb1-32546: 空闲 cuda:0, cuda:1, cuda:2, cuda:3, cuda:4, cuda:5\\nbjb2-28827: 空闲 cuda:0, cuda:1, cuda:2, cuda:3, cuda:4, cuda:5\\nbjb2-40593: 无 GPU 信息\\n\\n## 告警\\n- plan_001-crm-smolvla: 训练失败 — unknown\\n- plan_014-reconvla-baseline: 训练失败 — unknown\\n- eval-smolvla-libero-spatial: 训练失败 — unknown\\n- eval-spatial-reeval-v2: 已被终止 — unknown\\n- precompute-v2-shard0: 已被终止 — unknown\\n- precompute-v2-shard1: 已被终止 — unknown\\n- precompute-v2-shard2: 已被终止 — unknown\\n- eval-spatial-v3-full: 已被终止 — unknown\\n- precompute-v3-shard0: 已被终止 — unknown\\n- precompute-v3-shard1: 已被终止 — unknown\\n- precompute-v3-shard2: 已被终止 — unknown\\n- eval-spatial-v4-full: 已被终止 — unknown\\n- eval-object-v4-full: 已被终止 — unknown\\n- eval-spatial-v5-full: 已被终止 — unknown\\n- crm-train-v1: 已被终止 — unknown\\n- eval-reconvla-spatial-v1: 已被终止 — unknown\\n- eval-reconvla-spatial-v2: 已被终止 — unknown\\n- eval-acr-spatial-v1: 已被终止 — unknown\\n- crm-train-a3-obs-only: 已被终止 — unknown\\n- eval-acr-vla-spatial-v1: 已被终止 — unknown\\n- eval-spatial-v6-full: 已被终止 — unknown\\n- eval-acr-spatial-v2: 已被终止 — unknown\\n- eval-object-v5-full: 已被终止 — unknown\\n- eval-object-v6-full: 已被终止 — unknown\\n- crm-train-a4-scalar-unc: 已被终止 — unknown\\n- eval-scalar-unc-spatial: 已被终止 — unknown\\n- eval-object-v7-full: 已被终止 — unknown\\n- crm-train-k5: 已被终止 — unknown\\n- eval-k5-spatial: 已被终止 — unknown\\n- eval-scalar-unc-spatial-v2: 已被终止 — unknown\\n- eval-obs-only-spatial: 训练失败 — unknown\\n- eval-obs-only-spatial-v2: 训练失败 — unknown\\n- eval-obs-only-spatial-v3: 已被终止 — unknown\\n- eval-argmin-only-spatial: 已被终止 — unknown\\n- eval-tiny-correction-spatial: 已被终止 — unknown\\n- crm-train-v3-perdof: 已被终止 — unknown\\n- crm-train-v3-scalar-unc: 已被终止 — unknown\\n- crm-train-v3-obs-only: 已被终止 — unknown\\n- eval-acr-spatial-v4-default: 训练失败 — unknown\\n- eval-acr-spatial-v4-small: 已被终止 — unknown\\n- eval-acr-spatial-v4-obs-only: 训练失败 — unknown\\n- eval-acr-spatial-v4-scalar: 已被终止 — unknown\\n- eval-acr-spatial-v4-obs-only-r2: 已被终止 — unknown\\n- eval-acr-spatial-v4-default-r2: 已被终止 — unknown\\n- eval-acr-spatial-v4-default-r3: 已被终止 — unknown\\n- eval-acr-object-v4-obs-only-b2: 已被终止 — unknown\\n- eval-acr-object-v4-scalar-b2: 已被终止 — unknown\\n- eval-mag-perdof-norm02: 已被终止 — unknown\\n- eval-vla-only-object-k1: 训练失败 — unknown\\n- eval-acr-object-v4-default: 已被终止 — unknown\\n- eval-mag-obsonly-norm003: 已被终止 — unknown\\n- eval-mag-obsonly-norm03: 已被终止 — unknown\\n- eval-mag-obsonly-norm03-b2: 训练失败 — unknown\\n- eval-mag-obsonly-norm-0.3-r3: 已被终止 — unknown\\n- eval-mag-obsonly-norm-0p3-r3: 已被终止 — unknown\\n- eval-obs-only-spatial-seed43: 训练失败 — unknown\\n- eval-obs-only-object-norm02-seed43: 训练失败 — unknown\\n- eval-mag-perdof-norm0p3-object: 已被终止 — unknown\\n- eval-mag-perdof-norm0p3-object-r2: 已被终止 — unknown\\n- eval-mag-obsonly-norm03-b3: 已被终止 — unknown\\n- eval-mag-obsonly-norm03-b4: 已被终止 — unknown\\n- eval-mag-perdof-norm03-object-r2: 已被终止 — unknown\\n- eval-mag-perdof-norm02-seed43-object: 已被终止 — unknown\\n- eval-mag-perdof-norm02-seed43-object-r2: 已被终止 — unknown\\n- eval-mag-obsonly-norm02-object: 已被终止 — unknown\\n- eval-argmin-object-seed44: 训练失败 — unknown\\n- eval-obs-only-object-norm02-seed44: 训练失败 — unknown\\n- eval-vla-only-object-seed44: 训练失败 — unknown\\n- eval-argmin-object-seed44-r3: 已被终止 — unknown\\n- eval-obs-only-object-norm02-seed44-r3: 已被终止 — unknown\\n- eval-scalar-object-seed44: 训练失败 — unknown\\n- eval-obs-only-object-norm03-seed45: 训练失败 — unknown\\n- eval-obs-only-object-norm02-seed44-r4: 已被终止 — unknown\\n- eval-direct-correction-object-seed42: 训练失败 — unknown\\n- eval-direct-correction-object-seed42-r2: 训练失败 — unknown\\n- eval-obs-only-object-norm01-seed46: 训练失败 — unknown\\n- eval-perdof-object-norm01-seed47: 已被终止 — unknown\\n- eval-obs-only-object-norm01-seed47-r2: 已被终止 — unknown\\n- eval-obs-only-object-norm01-seed47-bjb2: 已被终止 — unknown\\n- eval-obs-only-object-norm01-seed46-bjb2: 已被终止 — unknown\\n- eval-obs-only-object-norm03-seed47: 训练失败 — unknown\\n- eval-perdof-object-norm03-seed46-r2: 已被终止 — unknown\\n- eval-perdof-object-norm02-seed45-r2: 已被终止 — unknown\\n- eval-perdof-object-norm02-seed45-deploy: 已被终止 — unknown\\n- eval-obs-only-object-norm005-seed43-r3: 已被终止 — unknown\\n- train-crm-k1-accg-object-seed42: 训练失败 — unknown\\n- mag_obs_only_norm01_seed47: 已被终止 — unknown\\n- mag_obs_only_norm01_seed46: 已被终止 — unknown\\n- mag_perdof_norm02_seed43_r3: 已被终止 — unknown\\n- eval-obs-only-object-norm02-seed48: 已被终止 — unknown\\n- eval-obs-only-object-norm01-seed42-r2: 训练失败 — unknown\\n- eval-perdof-object-norm01-seed42-r2: 训练失败 — unknown\\n- eval-perdof-object-norm003-seed44: 训练失败 — unknown\\n- eval-perdof-object-norm003-seed44-r2: 训练失败 — unknown\\n- eval-perdof-object-norm003-seed45: 已被终止 — unknown\\n- eval-perdof-object-norm005-seed45: 训练失败 — unknown\\n- eval-random-selection-object-seed46: 训练失败 — unknown\\n- eval-obs-only-object-norm005-seed46: 已被终止 — unknown\\n- eval-obs-only-object-norm003-seed47: 已被终止 — unknown\\n- eval-perdof-object-norm03-seed48: 已被终止 — unknown\\n- eval-obs-only-object-norm003-seed49: 已被终止 — unknown\\n- eval-random-selection-object-seed46-r2: 训练失败 — unknown\\n- eval-obs-only-object-norm003-seed45-r2: 已被终止 — unknown\\n- eval-obs-only-spatial-norm02-seed43: 训练失败 — unknown\\n- eval-lto-splitA-heldout: 已被终止 — unknown\\n- eval-lto-splitA-vla-only: 已被终止 — unknown\\n- eval-argmin-object-k5-seed44: 训练失败 — unknown\\n- eval-random-selection-object-k5-seed42: 训练失败 — unknown\\n- eval-random-selection-object-k5-seed43: 训练失败 — unknown\\n- eval-random-selection-object-k5-seed44: 训练失败 — unknown\\n- eval-random-selection-object-k5-seed45: 训练失败 — unknown\\n- eval-obs-only-spatial-norm02-k5-seed44: 训练失败 — unknown\\n- eval-obs-only-spatial-norm02-k5-seed45: 训练失败 — unknown\\n- eval-obs-only-spatial-norm02-seed46: 训练失败 — unknown\\n- eval-vla-only-goal-seed44: 已被终止 — unknown\\n- eval-openvla-object-baseline-seed42: 已被终止 — unknown\\n- eval-crm-goal-seed44: 训练失败 — unknown\\n- eval-crm-goal-seed45: 训练失败 — unknown\\n&lt;!-- 已截断：超过 150 行限制，已执行 Pre-compaction Flush -->\\n\", \"total_chars\": 9370, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "e17f41b1-3dce-49fb-a9e5-f5dd86423ed8",
  "uuid": "938ea0c3-4b50-4b38-bdb0-2e49ae628c17",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"path\\\": \\\"/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/report.md\\\", \\\"content\\\": \\\"&lt;!-- AUTO-FACTS-BEGIN (generated 2026-05-21T03:12:13Z; do not edit — regenerated by auto_build_report_facts) -->\\\\n## 📊 当前状态（auto-derived from registry）\\\\n\\\\n**总计**: 546 个实验 — DEPLOYED 5, DONE 498, PREPARING 35, RUNNING 8\\\\n**DONE 分布**: failed 55, killed 90, negative 38, success 315\\\\n\\\\n### GPU 占用\\\\n- **实际运行**: 8 张 — bjb2-28827:cuda:0(eval-adaptive-k-spatial-p90-seed44-bjb2), bjb1-18228:cuda:0(eval-obs-only-object-norm003-seed66), bjb1-18228:cuda:2(eval-obs-only-object-norm005-seed66), bjb1-18228:cuda:3(eval-obs-only-object-norm01-seed66), bjb2-40593:cuda:0(eval-pi05-baseline-object-seed42), bjb2-28827:cuda:5(eval-obs-only-object-norm003-seed67), bjb1-32546:cuda:2(eval-obs-only-object-norm005-seed67), bjb1-18228:cuda:1(eval-obs-only-object-norm01-seed67)\\\\n\\\\n### 💾 磁盘余量\\\\n- **bjb2-40593**:\\\\n  - `/init`: 150M/150M 可用（已用 0%）\\\\n  - `/autodl-pub/data`: 5.7T/10T 可用（已用 44%）\\\\n  - `/usr/bin/nvidia-smi`: 44G/437G 可用（已用 90%） ⚠️\\\\n- **bjb1-18228**:\\\\n  - `/autodl-pub`: 603G/7.0T 可用（已用 92%） ⚠️\\\\n  - `/autodl-pub/data`: 5.7T/10T 可用（已用 44%）\\\\n  - `/usr/bin/nvidia-smi`: 400G/438G 可用（已用 4%）\\\\n- **bjb1-32546**:\\\\n  - `/autodl-pub`: 1.1T/7.0T 可用（已用 86%）\\\\n  - `/autodl-pub/data`: 5.7T/10T 可用（已用 44%）\\\\n  - `/usr/bin/nvidia-smi`: 400G/438G 可用（已用 4%）\\\\n- **bjb2-28827**:\\\\n  - `/autodl-pub`: 4.5T/14T 可用（已用 69%）\\\\n  - `/autodl-pub/data`: 5.7T/10T 可用（已用 44%）\\\\n  - `/usr/bin/nvidia-smi`: 399G/439G 可用（已用 5%）\\\\n\\\\n### 🏃 RUNNING\\\\n| exp_id | server | gpu | pid | log |\\\\n|--------|--------|-----|-----|-----|\\\\n| `eval-adaptive-k-spatial-p90-seed44-bjb2` | bjb2-28827 | cuda:0 | 975409 | `…refinement/logs/eval-adaptive-k-spatial-p90-seed44-bjb2.log` |\\\\n| `eval-obs-only-object-norm003-seed66` | bjb1-18228 | cuda:0 | 642428 | `—` |\\\\n| `eval-obs-only-object-norm005-seed66` | bjb1-18228 | cuda:2 | 642506 | `—` |\\\\n| `eval-obs-only-object-norm01-seed66` | bjb1-18228 | cuda:3 | 642775 | `—` |\\\\n| `eval-pi05-baseline-object-seed42` | bjb2-40593 | cuda:0 | 802634 | `—` |\\\\n| `eval-obs-only-object-norm003-seed67` | bjb2-28827 | cuda:5 | 969788 | `—` |\\\\n| `eval-obs-only-object-norm005-seed67` | bjb1-32546 | cuda:2 | 805840 | `—` |\\\\n| `eval-obs-only-object-norm01-seed67` | bjb1-18228 | cuda:1 | 666593 | `—` |\\\\n\\\\n### 📌 最近完成 (top 5)\\\\n- `eval-obs-only-object-norm005-seed72` [success] — 2026-05-21T03:11:58 — process dead 5× with no sentinel/W&B — auto-resolved as failed\\\\n- `eval-obs-only-object-norm01-seed71` [success] — 2026-05-21T03:11:54 — process dead 5× with no sentinel/W&B — auto-resolved as failed\\\\n- `eval-obs-only-object-norm01-seed51-r3` [success] — 2026-05-21T03:11:43\\\\n- `eval-obs-only-object-norm003-seed73` [success] — 2026-05-21T03:11:37\\\\n- `eval-obs-only-object-norm005-seed75` [success] — 2026-05-21T03:11:12 — process dead 5× with no sentinel/W&B — auto-resolved as failed\\\\n\\\\n&lt;!-- AUTO-FACTS-END -->\\\\n\\\\n---\\\\n\\\\n# Handover — 2026-05-21\\\\n\\\\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\\\\n\\\\n## 运行中\\\\n| exp_id | 假设 | 状态 | 关键指标 | W&B |\\\\n|--------|------|------|---------|-----|\\\\n| eval-adaptive-k-spatial-p90-seed44-bjb2 | Adaptive K with τ=P90 (0.125870) on LIBERO-Spatial seed44. Third seed completing Spatial P90 cross-benchmark sweep. | — | — | — |\\\\n\\\\n## 待处理\\\\n- eval-obs-only-object-norm005-seed77: CRM obs_only (ε=0.05) K=10 on LIBERO-Object seed77. Norm sweep seed balance for ε=0.05 condition, expanding sample size for statistical robustness.（准备中）\\\\n- eval-obs-only-object-norm003-seed76（准备中）\\\\n- …另有 34 项\\\\n\\\\n## 近期结论\\\\n- **eval-obs-only-object-norm01-seed71** (success): CRM obs_only (ε=0.1) K=10 on LIBERO-Object seed71. Norm sweep filling ε=0.1 gap.\\\\n\\\\n## 趋势\\\\n成功 315 / 负向 38 / 失败 55 / 共 498\\\\noverall_success_rate: 0.16 →（近 3 次 success）\\\\n\\\\n## 下一步\\\\n（无活跃 idea，请通过 ideas.md 添加）\\\\n\\\\n## 资源状态\\\\nbjb1-18228: 无 GPU 信息\\\\nbjb1-32546: 空闲 cuda:0, cuda:1, cuda:2, cuda:3, cuda:4, cuda:5\\\\nbjb2-28827: 空闲 cuda:0, cuda:1, cuda:2, cuda:3, cuda:4, cuda:5\\\\nbjb2-40593: 无 GPU 信息\\\\n\\\\n## 告警\\\\n- plan_001-crm-smolvla: 训练失败 — unknown\\\\n- plan_014-reconvla-baseline: 训练失败 — unknown\\\\n- eval-smolvla-libero-spatial: 训练失败 — unknown\\\\n- eval-spatial-reeval-v2: 已被终止 — unknown\\\\n- precompute-v2-shard0: 已被终止 — unknown\\\\n- precompute-v2-shard1: 已被终止 — unknown\\\\n- precompute-v2-shard2: 已被终止 — unknown\\\\n- eval-spatial-v3-full: 已被终止 — unknown\\\\n- precompute-v3-shard0: 已被终止 — unknown\\\\n- precompute-v3-shard1: 已被终止 — unknown\\\\n- precompute-v3-shard2: 已被终止 — unknown\\\\n- eval-spatial-v4-full: 已被终止 — unknown\\\\n- eval-object-v4-full: 已被终止 — unknown\\\\n- eval-spatial-v5-full: 已被终止 — unknown\\\\n- crm-train-v1: 已被终止 — unknown\\\\n- eval-reconvla-spatial-v1: 已被终止 — unknown\\\\n- eval-reconvla-spatial-v2: 已被终止 — unknown\\\\n- eval-acr-spatial-v1: 已被终止 — unknown\\\\n- crm-train-a3-obs-only: 已被终止 — unknown\\\\n- eval-acr-vla-spatial-v1: 已被终止 — unknown\\\\n- eval-spatial-v6-full: 已被终止 — unknown\\\\n- eval-acr-spatial-v2: 已被终止 — unknown\\\\n- eval-object-v5-full: 已被终止 — unknown\\\\n- eval-object-v6-full: 已被终止 — unknown\\\\n- crm-train-a4-scalar-unc: 已被终止 — unknown\\\\n- eval-scalar-unc-spatial: 已被终止 — unknown\\\\n- eval-object-v7-full: 已被终止 — unknown\\\\n- crm-train-k5: 已被终止 — unknown\\\\n- eval-k5-spatial: 已被终止 — unknown\\\\n- eval-scalar-unc-spatial-v2: 已被终止 — unknown\\\\n- eval-obs-only-spatial: 训练失败 — unknown\\\\n- eval-obs-only-spatial-v2: 训练失败 — unknown\\\\n- eval-obs-only-spatial-v3: 已被终止 — unknown\\\\n- eval-argmin-only-spatial: 已被终止 — unknown\\\\n- eval-tiny-correction-spatial: 已被终止 — unknown\\\\n- crm-train-v3-perdof: 已被终止 — unknown\\\\n- crm-train-v3-scalar-unc: 已被终止 — unknown\\\\n- crm-train-v3-obs-only: 已被终止 — unknown\\\\n- eval-acr-spatial-v4-default: 训练失败 — unknown\\\\n- eval-acr-spatial-v4-small: 已被终止 — unknown\\\\n- eval-acr-spatial-v4-obs-only: 训练失败 — unknown\\\\n- eval-acr-spatial-v4-scalar: 已被终止 — unknown\\\\n- eval-acr-spatial-v4-obs-only-r2: 已被终止 — unknown\\\\n- eval-acr-spatial-v4-default-r2: 已被终止 — unknown\\\\n- eval-acr-spatial-v4-default-r3: 已被终止 — unknown\\\\n- eval-acr-object-v4-obs-only-b2: 已被终止 — unknown\\\\n- eval-acr-object-v4-scalar-b2: 已被终止 — unknown\\\\n- eval-mag-perdof-norm02: 已被终止 — unknown\\\\n- eval-vla-only-object-k1: 训练失败 — unknown\\\\n- eval-acr-object-v4-default: 已被终止 — unknown\\\\n- eval-mag-obsonly-norm003: 已被终止 — unknown\\\\n- eval-mag-obsonly-norm03: 已被终止 — unknown\\\\n- eval-mag-obsonly-norm03-b2: 训练失败 — unknown\\\\n- eval-mag-obsonly-norm-0.3-r3: 已被终止 — unknown\\\\n- eval-mag-obsonly-norm-0p3-r3: 已被终止 — unknown\\\\n- eval-obs-only-spatial-seed43: 训练失败 — unknown\\\\n- eval-obs-only-object-norm02-seed43: 训练失败 — unknown\\\\n- eval-mag-perdof-norm0p3-object: 已被终止 — unknown\\\\n- eval-mag-perdof-norm0p3-object-r2: 已被终止 — unknown\\\\n- eval-mag-obsonly-norm03-b3: 已被终止 — unknown\\\\n- eval-mag-obsonly-norm03-b4: 已被终止 — unknown\\\\n- eval-mag-perdof-norm03-object-r2: 已被终止 — unknown\\\\n- eval-mag-perdof-norm02-seed43-object: 已被终止 — unknown\\\\n- eval-mag-perdof-norm02-seed43-object-r2: 已被终止 — unknown\\\\n- eval-mag-obsonly-norm02-object: 已被终止 — unknown\\\\n- eval-argmin-object-seed44: 训练失败 — unknown\\\\n- eval-obs-only-object-norm02-seed44: 训练失败 — unknown\\\\n- eval-vla-only-object-seed44: 训练失败 — unknown\\\\n- eval-argmin-object-seed44-r3: 已被终止 — unknown\\\\n- eval-obs-only-object-norm02-seed44-r3: 已被终止 — unknown\\\\n- eval-scalar-object-seed44: 训练失败 — unknown\\\\n- eval-obs-only-object-norm03-seed45: 训练失败 — unknown\\\\n- eval-obs-only-object-norm02-seed44-r4: 已被终止 — unknown\\\\n- eval-direct-correction-object-seed42: 训练失败 — unknown\\\\n- eval-direct-correction-object-seed42-r2: 训练失败 — unknown\\\\n- eval-obs-only-object-norm01-seed46: 训练失败 — unknown\\\\n- eval-perdof-object-norm01-seed47: 已被终止 — unknown\\\\n- eval-obs-only-object-norm01-seed47-r2: 已被终止 — unknown\\\\n- eval-obs-only-object-norm01-seed47-bjb2: 已被终止 — unknown\\\\n- eval-obs-only-object-norm01-seed46-bjb2: 已被终止 — unknown\\\\n- eval-obs-only-object-norm03-seed47: 训练失败 — unknown\\\\n- eval-perdof-object-norm03-seed46-r2: 已被终止 — unknown\\\\n- eval-perdof-object-norm02-seed45-r2: 已被终止 — unknown\\\\n- eval-perdof-object-norm02-seed45-deploy: 已被终止 — unknown\\\\n- eval-obs-only-object-norm005-seed43-r3: 已被终止 — unknown\\\\n- train-crm-k1-accg-object-seed42: 训练失败 — unknown\\\\n- mag_obs_only_norm01_seed47: 已被终止 — unknown\\\\n- mag_obs_only_norm01_seed46: 已被终止 — unknown\\\\n- mag_perdof_norm02_seed43_r3: 已被终止 — unknown\\\\n- eval-obs-only-object-norm02-seed48: 已被终止 — unknown\\\\n- eval-obs-only-object-norm01-seed42-r2: 训练失败 — unknown\\\\n- eval-perdof-object-norm01-seed42-r2: 训练失败 — unknown\\\\n- eval-perdof-object-norm003-seed44: 训练失败 — unknown\\\\n- eval-perdof-object-norm003-seed44-r2: 训练失败 — unknown\\\\n- eval-perdof-object-norm003-seed45: 已被终止 — unknown\\\\n- eval-perdof-object-norm005-seed45: 训练失败 — unknown\\\\n- eval-random-selection-object-seed46: 训练失败 — unknown\\\\n- eval-obs-only-object-norm005-seed46: 已被终止 — unknown\\\\n- eval-obs-only-object-norm003-seed47: 已被终止 — unknown\\\\n- eval-perdof-object-norm03-seed48: 已被终止 — unknown\\\\n- eval-obs-only-object-norm003-seed49: 已被终止 — unknown\\\\n- eval-random-selection-object-seed46-r2: 训练失败 — unknown\\\\n- eval-obs-only-object-norm003-seed45-r2: 已被终止 — unknown\\\\n- eval-obs-only-spatial-norm02-seed43: 训练失败 — unknown\\\\n- eval-lto-splitA-heldout: 已被终止 — unknown\\\\n- eval-lto-splitA-vla-only: 已被终止 — unknown\\\\n- eval-argmin-object-k5-seed44: 训练失败 — unknown\\\\n- eval-random-selection-object-k5-seed42: 训练失败 — unknown\\\\n- eval-random-selection-object-k5-seed43: 训练失败 — unknown\\\\n- eval-random-selection-object-k5-seed44: 训练失败 — unknown\\\\n- eval-random-selection-object-k5-seed45: 训练失败 — unknown\\\\n- eval-obs-only-spatial-norm02-k5-seed44: 训练失败 — unknown\\\\n- eval-obs-only-spatial-norm02-k5-seed45: 训练失败 — unknown\\\\n- eval-obs-only-spatial-norm02-seed46: 训练失败 — unknown\\\\n- eval-vla-only-goal-seed44: 已被终止 — unknown\\\\n- eval-openvla-object-baseline-seed42: 已被终止 — unknown\\\\n- eval-crm-goal-seed44: 训练失败 — unknown\\\\n- eval-crm-goal-seed45: 训练失败 — unknown\\\\n&lt;!-- 已截断：超过 150 行限制，已执行 Pre-compaction Flush -->\\\\n\\\", \\\"total_chars\\\": 9370, \\\"truncated\\\": false}, \\\"error\\\": null, \\\"metadata\\\": {}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/report.md\", \"content\": \"&lt;!-- AUTO-FACTS-BEGIN (generated 2026-05-21T03:12:13Z; do not edit — regenerated by auto_build_report_facts) -->\\n## 📊 当前状态（auto-derived from registry）\\n\\n**总计**: 546 个实验 — DEPLOYED 5, DONE 498, PREPARING 35, RUNNING 8\\n**DONE 分布**: failed 55, killed 90, negative 38, success 315\\n\\n### GPU 占用\\n- **实际运行**: 8 张 — bjb2-28827:cuda:0(eval-adaptive-k-spatial-p90-seed44-bjb2), bjb1-18228:cuda:0(eval-obs-only-object-norm003-seed66), bjb1-18228:cuda:2(eval-obs-only-object-norm005-seed66), bjb1-18228:cuda:3(eval-obs-only-object-norm01-seed66), bjb2-40593:cuda:0(eval-pi05-baseline-object-seed42), bjb2-28827:cuda:5(eval-obs-only-object-norm003-seed67), bjb1-32546:cuda:2(eval-obs-only-object-norm005-seed67), bjb1-18228:cuda:1(eval-obs-only-object-norm01-seed67)\\n\\n### 💾 磁盘余量\\n- **bjb2-40593**:\\n  - `/init`: 150M/150M 可用（已用 0%）\\n  - `/autodl-pub/data`: 5.7T/10T 可用（已用 44%）\\n  - `/usr/bin/nvidia-smi`: 44G/437G 可用（已用 90%） ⚠️\\n- **bjb1-18228**:\\n  - `/autodl-pub`: 603G/7.0T 可用（已用 92%） ⚠️\\n  - `/autodl-pub/data`: 5.7T/10T 可用（已用 44%）\\n  - `/usr/bin/nvidia-smi`: 400G/438G 可用（已用 4%）\\n- **bjb1-32546**:\\n  - `/autodl-pub`: 1.1T/7.0T 可用（已用 86%）\\n  - `/autodl-pub/data`: 5.7T/10T 可用（已用 44%）\\n  - `/usr/bin/nvidia-smi`: 400G/438G 可用（已用 4%）\\n- **bjb2-28827**:\\n  - `/autodl-pub`: 4.5T/14T 可用（已用 69%）\\n  - `/autodl-pub/data`: 5.7T/10T 可用（已用 44%）\\n  - `/usr/bin/nvidia-smi`: 399G/439G 可用（已用 5%）\\n\\n### 🏃 RUNNING\\n| exp_id | server | gpu | pid | log |\\n|--------|--------|-----|-----|-----|\\n| `eval-adaptive-k-spatial-p90-seed44-bjb2` | bjb2-28827 | cuda:0 | 975409 | `…refinement/logs/eval-adaptive-k-spatial-p90-seed44-bjb2.log` |\\n| `eval-obs-only-object-norm003-seed66` | bjb1-18228 | cuda:0 | 642428 | `—` |\\n| `eval-obs-only-object-norm005-seed66` | bjb1-18228 | cuda:2 | 642506 | `—` |\\n| `eval-obs-only-object-norm01-seed66` | bjb1-18228 | cuda:3 | 642775 | `—` |\\n| `eval-pi05-baseline-object-seed42` | bjb2-40593 | cuda:0 | 802634 | `—` |\\n| `eval-obs-only-object-norm003-seed67` | bjb2-28827 | cuda:5 | 969788 | `—` |\\n| `eval-obs-only-object-norm005-seed67` | bjb1-32546 | cuda:2 | 805840 | `—` |\\n| `eval-obs-only-object-norm01-seed67` | bjb1-18228 | cuda:1 | 666593 | `—` |\\n\\n### 📌 最近完成 (top 5)\\n- `eval-obs-only-object-norm005-seed72` [success] — 2026-05-21T03:11:58 — process dead 5× with no sentinel/W&B — auto-resolved as failed\\n- `eval-obs-only-object-norm01-seed71` [success] — 2026-05-21T03:11:54 — process dead 5× with no sentinel/W&B — auto-resolved as failed\\n- `eval-obs-only-object-norm01-seed51-r3` [success] — 2026-05-21T03:11:43\\n- `eval-obs-only-object-norm003-seed73` [success] — 2026-05-21T03:11:37\\n- `eval-obs-only-object-norm005-seed75` [success] — 2026-05-21T03:11:12 — process dead 5× with no sentinel/W&B — auto-resolved as failed\\n\\n&lt;!-- AUTO-FACTS-END -->\\n\\n---\\n\\n# Handover — 2026-05-21\\n\\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\\n\\n## 运行中\\n| exp_id | 假设 | 状态 | 关键指标 | W&B |\\n|--------|------|------|---------|-----|\\n| eval-adaptive-k-spatial-p90-seed44-bjb2 | Adaptive K with τ=P90 (0.125870) on LIBERO-Spatial seed44. Third seed completing Spatial P90 cross-benchmark sweep. | — | — | — |\\n\\n## 待处理\\n- eval-obs-only-object-norm005-seed77: CRM obs_only (ε=0.05) K=10 on LIBERO-Object seed77. Norm sweep seed balance for ε=0.05 condition, expanding sample size for statistical robustness.（准备中）\\n- eval-obs-only-object-norm003-seed76（准备中）\\n- …另有 34 项\\n\\n## 近期结论\\n- **eval-obs-only-object-norm01-seed71** (success): CRM obs_only (ε=0.1) K=10 on LIBERO-Object seed71. Norm sweep filling ε=0.1 gap.\\n\\n## 趋势\\n成功 315 / 负向 38 / 失败 55 / 共 498\\noverall_success_rate: 0.16 →（近 3 次 success）\\n\\n## 下一步\\n（无活跃 idea，请通过 ideas.md 添加）\\n\\n## 资源状态\\nbjb1-18228: 无 GPU 信息\\nbjb1-32546: 空闲 cuda:0, cuda:1, cuda:2, cuda:3, cuda:4, cuda:5\\nbjb2-28827: 空闲 cuda:0, cuda:1, cuda:2, cuda:3, cuda:4, cuda:5\\nbjb2-40593: 无 GPU 信息\\n\\n## 告警\\n- plan_001-crm-smolvla: 训练失败 — unknown\\n- plan_014-reconvla-baseline: 训练失败 — unknown\\n- eval-smolvla-libero-spatial: 训练失败 — unknown\\n- eval-spatial-reeval-v2: 已被终止 — unknown\\n- precompute-v2-shard0: 已被终止 — unknown\\n- precompute-v2-shard1: 已被终止 — unknown\\n- precompute-v2-shard2: 已被终止 — unknown\\n- eval-spatial-v3-full: 已被终止 — unknown\\n- precompute-v3-shard0: 已被终止 — unknown\\n- precompute-v3-shard1: 已被终止 — unknown\\n- precompute-v3-shard2: 已被终止 — unknown\\n- eval-spatial-v4-full: 已被终止 — unknown\\n- eval-object-v4-full: 已被终止 — unknown\\n- eval-spatial-v5-full: 已被终止 — unknown\\n- crm-train-v1: 已被终止 — unknown\\n- eval-reconvla-spatial-v1: 已被终止 — unknown\\n- eval-reconvla-spatial-v2: 已被终止 — unknown\\n- eval-acr-spatial-v1: 已被终止 — unknown\\n- crm-train-a3-obs-only: 已被终止 — unknown\\n- eval-acr-vla-spatial-v1: 已被终止 — unknown\\n- eval-spatial-v6-full: 已被终止 — unknown\\n- eval-acr-spatial-v2: 已被终止 — unknown\\n- eval-object-v5-full: 已被终止 — unknown\\n- eval-object-v6-full: 已被终止 — unknown\\n- crm-train-a4-scalar-unc: 已被终止 — unknown\\n- eval-scalar-unc-spatial: 已被终止 — unknown\\n- eval-object-v7-full: 已被终止 — unknown\\n- crm-train-k5: 已被终止 — unknown\\n- eval-k5-spatial: 已被终止 — unknown\\n- eval-scalar-unc-spatial-v2: 已被终止 — unknown\\n- eval-obs-only-spatial: 训练失败 — unknown\\n- eval-obs-only-spatial-v2: 训练失败 — unknown\\n- eval-obs-only-spatial-v3: 已被终止 — unknown\\n- eval-argmin-only-spatial: 已被终止 — unknown\\n- eval-tiny-correction-spatial: 已被终止 — unknown\\n- crm-train-v3-perdof: 已被终止 — unknown\\n- crm-train-v3-scalar-unc: 已被终止 — unknown\\n- crm-train-v3-obs-only: 已被终止 — unknown\\n- eval-acr-spatial-v4-default: 训练失败 — unknown\\n- eval-acr-spatial-v4-small: 已被终止 — unknown\\n- eval-acr-spatial-v4-obs-only: 训练失败 — unknown\\n- eval-acr-spatial-v4-scalar: 已被终止 — unknown\\n- eval-acr-spatial-v4-obs-only-r2: 已被终止 — unknown\\n- eval-acr-spatial-v4-default-r2: 已被终止 — unknown\\n- eval-acr-spatial-v4-default-r3: 已被终止 — unknown\\n- eval-acr-object-v4-obs-only-b2: 已被终止 — unknown\\n- eval-acr-object-v4-scalar-b2: 已被终止 — unknown\\n- eval-mag-perdof-norm02: 已被终止 — unknown\\n- eval-vla-only-object-k1: 训练失败 — unknown\\n- eval-acr-object-v4-default: 已被终止 — unknown\\n- eval-mag-obsonly-norm003: 已被终止 — unknown\\n- eval-mag-obsonly-norm03: 已被终止 — unknown\\n- eval-mag-obsonly-norm03-b2: 训练失败 — unknown\\n- eval-mag-obsonly-norm-0.3-r3: 已被终止 — unknown\\n- eval-mag-obsonly-norm-0p3-r3: 已被终止 — unknown\\n- eval-obs-only-spatial-seed43: 训练失败 — unknown\\n- eval-obs-only-object-norm02-seed43: 训练失败 — unknown\\n- eval-mag-perdof-norm0p3-object: 已被终止 — unknown\\n- eval-mag-perdof-norm0p3-object-r2: 已被终止 — unknown\\n- eval-mag-obsonly-norm03-b3: 已被终止 — unknown\\n- eval-mag-obsonly-norm03-b4: 已被终止 — unknown\\n- eval-mag-perdof-norm03-object-r2: 已被终止 — unknown\\n- eval-mag-perdof-norm02-seed43-object: 已被终止 — unknown\\n- eval-mag-perdof-norm02-seed43-object-r2: 已被终止 — unknown\\n- eval-mag-obsonly-norm02-object: 已被终止 — unknown\\n- eval-argmin-object-seed44: 训练失败 — unknown\\n- eval-obs-only-object-norm02-seed44: 训练失败 — unknown\\n- eval-vla-only-object-seed44: 训练失败 — unknown\\n- eval-argmin-object-seed44-r3: 已被终止 — unknown\\n- eval-obs-only-object-norm02-seed44-r3: 已被终止 — unknown\\n- eval-scalar-object-seed44: 训练失败 — unknown\\n- eval-obs-only-object-norm03-seed45: 训练失败 — unknown\\n- eval-obs-only-object-norm02-seed44-r4: 已被终止 — unknown\\n- eval-direct-correction-object-seed42: 训练失败 — unknown\\n- eval-direct-correction-object-seed42-r2: 训练失败 — unknown\\n- eval-obs-only-object-norm01-seed46: 训练失败 — unknown\\n- eval-perdof-object-norm01-seed47: 已被终止 — unknown\\n- eval-obs-only-object-norm01-seed47-r2: 已被终止 — unknown\\n- eval-obs-only-object-norm01-seed47-bjb2: 已被终止 — unknown\\n- eval-obs-only-object-norm01-seed46-bjb2: 已被终止 — unknown\\n- eval-obs-only-object-norm03-seed47: 训练失败 — unknown\\n- eval-perdof-object-norm03-seed46-r2: 已被终止 — unknown\\n- eval-perdof-object-norm02-seed45-r2: 已被终止 — unknown\\n- eval-perdof-object-norm02-seed45-deploy: 已被终止 — unknown\\n- eval-obs-only-object-norm005-seed43-r3: 已被终止 — unknown\\n- train-crm-k1-accg-object-seed42: 训练失败 — unknown\\n- mag_obs_only_norm01_seed47: 已被终止 — unknown\\n- mag_obs_only_norm01_seed46: 已被终止 — unknown\\n- mag_perdof_norm02_seed43_r3: 已被终止 — unknown\\n- eval-obs-only-object-norm02-seed48: 已被终止 — unknown\\n- eval-obs-only-object-norm01-seed42-r2: 训练失败 — unknown\\n- eval-perdof-object-norm01-seed42-r2: 训练失败 — unknown\\n- eval-perdof-object-norm003-seed44: 训练失败 — unknown\\n- eval-perdof-object-norm003-seed44-r2: 训练失败 — unknown\\n- eval-perdof-object-norm003-seed45: 已被终止 — unknown\\n- eval-perdof-object-norm005-seed45: 训练失败 — unknown\\n- eval-random-selection-object-seed46: 训练失败 — unknown\\n- eval-obs-only-object-norm005-seed46: 已被终止 — unknown\\n- eval-obs-only-object-norm003-seed47: 已被终止 — unknown\\n- eval-perdof-object-norm03-seed48: 已被终止 — unknown\\n- eval-obs-only-object-norm003-seed49: 已被终止 — unknown\\n- eval-random-selection-object-seed46-r2: 训练失败 — unknown\\n- eval-obs-only-object-norm003-seed45-r2: 已被终止 — unknown\\n- eval-obs-only-spatial-norm02-seed43: 训练失败 — unknown\\n- eval-lto-splitA-heldout: 已被终止 — unknown\\n- eval-lto-splitA-vla-only: 已被终止 — unknown\\n- eval-argmin-object-k5-seed44: 训练失败 — unknown\\n- eval-random-selection-object-k5-seed42: 训练失败 — unknown\\n- eval-random-selection-object-k5-seed43: 训练失败 — unknown\\n- eval-random-selection-object-k5-seed44: 训练失败 — unknown\\n- eval-random-selection-object-k5-seed45: 训练失败 — unknown\\n- eval-obs-only-spatial-norm02-k5-seed44: 训练失败 — unknown\\n- eval-obs-only-spatial-norm02-k5-seed45: 训练失败 — unknown\\n- eval-obs-only-spatial-norm02-seed46: 训练失败 — unknown\\n- eval-vla-only-goal-seed44: 已被终止 — unknown\\n- eval-openvla-object-baseline-seed42: 已被终止 — unknown\\n- eval-crm-goal-seed44: 训练失败 — unknown\\n- eval-crm-goal-seed45: 训练失败 — unknown\\n&lt;!-- 已截断：超过 150 行限制，已执行 Pre-compaction Flush -->\\n\", \"total_chars\": 9370, \"truncated\": false}, \"error\": null, \"metadata\": {}}"
    }
  }
}
```

</details>

---

### Tool call

_source line 22_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01BeWmfLFCfMZkbp82jNmk1j`</summary>

```json
{
  "project": "acr-vla-conformal-refinement",
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
  "session_id": "e17f41b1-3dce-49fb-a9e5-f5dd86423ed8",
  "uuid": "ffeaaaf8-7680-4c83-9d19-81083a254fae",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014xDxRDBVhrYYMaaaLQndcZ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 21796,
      "cache_read_input_tokens": 43930,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 21796
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

_source line 23 · 2026-05-21T03:24:08.655Z_

<details><summary>↩ Tool result · `toolu_01BeWmfLFCfMZkbp82jNmk1j`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/memory.md\", \"content\": \"# Project Memory\\n\\n## 失败模式记录\\n\\n- [失败模式] Cron false positive：eval 脚本不写 W&B 也不写 sentinel file，进程正常退出后 cron 5 次检测找不到标记 → 自动标记为 failed。受影响：eval-vla-only-long-seed46, eval-vla-only-goal-seed46。修复方案：tail 日志确认实际完成 → 手动修正 conclusion=success + 补录 metrics。预防：eval 实验应检查 output JSON 是否存在作为 sentinel。\\n\\n- [失败模式] Cron false positive（2026-05-20）：**eval-adaptive-k-spatial-p50-seed42** 被 cron 误判为 failed（\\\"process dead 5× with no sentinel/W&B\\\"）。实际情况：原 PID 675831 被 deploy worker kill 后，重启为 PID 681823。重启后进程正常运行，但 cron 监控未追踪到新 PID，5 次检测均未发现 sentinel → 自动标记 failed。诊断时（2026-05-20）PID 681823 仍在运行（状态 Rl+，已运行 17h36m），已完成 3/10 tasks（SR: 70%/100%/0%），第 4 个 task 进行中（rollout 5, 1/5 success）。GPU 使用 5972/24564 MiB，日志无错误。**无需重新提交，等待自然完成后手动修正 conclusion。**\\n\\n- [失败模式] SIGHUP false failure（2026-05-20）：bjb2-28827 上多个实验 EXIT_CODE=129 (SIGHUP) 被标记 failed，实际全部完成。**已确认受影响：P75-seed44, P90-seed42, P25-seed44**。SIGHUP 发生在进程写完结果 JSON 之后（tmux session 断开或 SSH 连接清理）。**诊断方法：tail 日志看 \\\"Results saved to\\\" + \\\"Overall success rate\\\" 行 → 手动修正 conclusion=success 并补录 metrics。**\\n\\n- [失败模式] Cron 日志路径不匹配（2026-05-20）：**eval-obs-only-goal-norm02-seed51** (bjb1-32546) 被 cron 误判 dead。根因：实验日志写入 `/root/acr-vla-conformal-refinement/logs/`（项目目录下），但 cron 监控在 `~/runs/acr-vla-conformal-refinement/` 下找日志 → 找不到 → 5 次检测均无 sentinel → auto-resolved failed。**教训：submit_training_job 的 log_path 必须与实际 tee 输出路径一致。部分实验用 `tee logs/xxx.log`（相对于 cd 后的项目目录），另一部分用 `~/runs/` 绝对路径，两套路径并存导致 cron 误判。**\\n\\n- [失败模式] Cron false positive 批量（2026-05-20 诊断）：bjb1-32546 上 **eval-perdof-object-norm02-seed50** (PID 542405) 和 **eval-obs-only-object-norm02-seed51** (PID 542894) 被 cron 报告 \\\"process gone, no sentinel, no W&B\\\"。实际两者均已**正常完成**，output JSON 已写入。bjb1-18228 上 **eval-obs-only-object-norm005-seed44** 同样正常完成但被标记 failed。根因同上：eval 脚本不写 sentinel/W&B，进程正常退出后 cron 无法确认完成状态。结果：perdof-norm02-seed50 SR=10.0%, obs_only-norm02-seed51 SR=17.0%, obs_only-norm005-seed44 SR=12.0%。**均无需重跑，需手动修正 conclusion=success 并补录 metrics。**\\n\\n- [失败模式] python PATH 不存在（2026-05-21, bjb1-32546）：`nohup: failed to run command 'python': No such file or directory`。bjb1-32546 使用 conda 环境，`python` 不在默认 PATH 中（仅 `/root/miniconda3/bin/python` 可用）。受影响：seed51-r2, seed52-r2, seed62, seed63（4 个实验同时失败）。**修复方案：提交命令前加 `source /root/miniconda3/etc/profile.d/conda.sh && conda activate base &&` 前缀。** 教训：submit_training_job 的 command 不能假设 `python` 在 PATH 中，必须自带环境激活。对照其他服务器（bjb1-18228、bjb2-28827）成功实验的命令格式，它们通过 `bash -c \\\"source ... && python ...\\\"` 包裹。\\n\\n- [失败模式] FMVD 信号无效：ρ=0.0825 NO-GO。根因：denoising 空间统计量不映射到 action uncertainty。\\n\\n- [失败模式] CRM correction magnitude 信号无效（2026-05-20）：ρ(K1_corr_mag, K10_var) = 0.1523 NO-GO。**根因：CRM correction magnitude 是常数 (~0.1205)，P25=P50=P75=P90 几乎相同。** CRM 对所有输入产出相同大小的修正向量——修正方向变化但幅度不变。推测因 max_correction_norm=0.2 的 clipping 使得大部分 correction 被截断到相同 norm。K=2 argmin 版本同样无效 (ρ=0.1340)。**教训：clipped norm 的信号没有方差，自然无法做 gate。**\\n\\n- [失败模式] OpenVLA-7B eval timeout：timeout_hours 至少设 12h。\\n\\n- [失败模式] Table 1 数据混淆（2026-05-20）：Table 1 原报 CRM Object K=10 = 17.6% (n=7)，实际来自 **norm01+norm02 混合数据**。seed42 只有 norm01 (0.19)，seed43 只有 norm02 (0.16)，两个 config 各自只有 n=6，合并后变 n=7。paper_provenance.yaml C029 引用的 exp_id 是抽象 \\\"obs_only_k10\\\" 而非具体实验 ID，导致问题没被及时发现。**教训：provenance 必须引用具体 registry_id，不用抽象标签。**\\n\\n- [失败模式] evaluate.py 路径缺 src/ 前缀（2026-05-20）：adaptive_k spatial 实验命令用 `python evaluate.py` 而非 `python src/evaluate.py`，导致 EXIT_CODE=2 (No such file)。受影响：eval-adaptive-k-spatial-p50-seed43, eval-adaptive-k-spatial-p50-seed44（两台服务器 bjb1-32546, bjb2-28827 同时中招）。**教训：提交命令时对照历史成功实验的 command 格式，evaluate.py 在 src/ 子目录下。**\\n\\n## seed66 失败诊断 (2026-05-21)\\n- 根因：**Cron false positive（第 N 次）**。3 个 seed66 进程（norm003/norm005/norm01）实际仍在 bjb1-18228 上正常运行，被 cron 误判为 \\\"process dead 5× with no sentinel/W&B\\\"。\\n- 证据：\\n  - PID 642428 (norm003, GPU0), PID 642506 (norm005, GPU2), PID 642775 (norm01, GPU3) 均处于 Rl 状态，CPU 使用 ~400%，GPU 利用率 34-38%，VRAM ~5.7GB/卡\\n  - 日志在两次读取之间从 rollout 5/20 增长到 10/20，确认进程在推进\\n  - sentinels/ 目录完全为空——从未有实验写过 sentinel file\\n  - 无 OOM、无 CUDA error、无 traceback、无 segfault\\n  - 磁盘空间充足（根分区 53%，数据盘未挂载 autodl-tmp 但进程正常读写）\\n- 与 seed65 对比：seed65 (PID 622484, GPU1) 用 `nohup python -u` 启动，日志持续更新；seed66 用 `python3` 启动（无 `-u` 无 nohup），日志因 stdout 缓冲更新延迟，但进程本身正常\\n- 影响范围：eval-obs-only-object-norm005-seed66, eval-obs-only-object-norm01-seed66, eval-obs-only-object-norm003-seed66（3 个实验）\\n- 建议修复：**无需重跑**。等待进程自然完成（n_rollouts=20，当前约 50% 进度，预计再需 1-2 小时），完成后手动修正 conclusion=success 并从 output JSON 补录 metrics。\\n\\n## CRM Coverage 限制\\n\\nCRM v3 训练数据 = Object(10) + Spatial(10) = 20 tasks。Goal/Long 是 OOD 泛化测试。\\n\\n## Adaptive K 信号探索\\n\\n| 信号 | ρ vs K10_var | 结论 | 备注 |\\n|------|-------------|------|------|\\n| FMVD (velocity dispersion) | 0.0825 | ❌ NO-GO | zero-cost 但无效 |\\n| **K=2 L2 divergence** | **0.9979** | **✅ GO** | 需要 K=2 采样（+170ms），near-perfect proxy |\\n| CRM correction magnitude (K=1) | 0.1523 | ❌ NO-GO | zero-cost 但 magnitude 是常数 |\\n| CRM correction magnitude (K=2 argmin) | 0.1340 | ❌ NO-GO | 同上 |\\n\\n**结论：K=2 L2 distance 是唯一可用的 adaptive K 门控信号。** FMVD 和 CRM magnitude 均因信号方差不足而失败。\\n\\n## Adaptive K Sweep 最终结果 — Object (2026-05-20, 12/12 完成)\\n\\n| 阈值 | SR [seeds] | avg_K | fast_path% |\\n|------|-----------|-------|-----------|\\n| P90 (τ=0.127) | 13.3% [12,14,14] | ~2.6 | ~93% |\\n| P75 (τ=0.099) | 13.7% [12,13,16] | ~3.1 | ~87% |\\n| **P50 (τ=0.075)** | **15.3% [16,16,14]** | **~3.8** | **~77%** |\\n| P25 (τ=0.055) | 14.3% [15,13,15] | ~4.8 | ~65% |\\n\\n**P50 = Pareto optimal**: 最高 SR + 比 K=10 省 62% compute (avg_K 3.8 vs 10)。\\n\\n## Adaptive K Cross-Benchmark Sweep — Spatial (2026-05-20, 11/12 done)\\n\\nObject 校准阈值直接迁移到 Spatial（无 per-benchmark tuning）：\\n\\n| 阈值 | seed42 | seed43 | seed44 | Mean±Std | avg_K | fast_path |\\n|------|--------|--------|--------|----------|-------|-----------|\\n| P90 | 31% | 32% | PREPARING | — | ~3.5 | ~80% |\\n| P75 | 31% | 34% | 33% | 32.7%±1.5% | ~5.0 | ~62% |\\n| P50 | 30% | 33% | 33% | 32.0%±1.7% | ~6.35 | ~46% |\\n| P25 | 33% | 30% | 32% | 31.7%±1.5% | ~7.65 | ~29% |\\n\\nvs VLA-only Spatial: 29.6%±1.1% | vs CRM K=10 Spatial: 34.6%±1.4%\\n\\n**关键洞察**：\\n1. 所有阈值 SR 差异很小（31.7-32.7%），但 compute 差异 2x（avg_K 3.5→7.65）。P75 在 Spatial 上 Pareto 最优（32.7% + avg_K 5.0），P50 在 Object 上最优。\\n2. Spatial fast_path 远低于 Object（同阈值下 29% vs 65% for P25）—— Spatial L2 均值更高，方法自动分配更多 full-K steps。\\n3. 这支持\\\"阈值自动适配任务复杂度\\\"的核心 narrative：同一 Object 校准阈值，在更难的 Spatial 上自动降低 fast_path 比例以保持 SR。\\n\\n## Latency Profiling (dry-run N=20, RTX 4090, 2026-05-20)\\n\\n| Component | Mean (ms) | 备注 |\\n|-----------|----------|------|\\n| VLA sampling | 206 | **K 无关**（batched generation） |\\n| CRM MLP forward | 0.33 | 337K params |\\n| Argmin L2 + CRM 总开销 | 4.0 | 管线 1.6% |\\n| Full pipeline K=10 | 259 | ~3.9 Hz |\\n| **Adaptive K 快路径** | **254** | K=2 only |\\n| **Adaptive K 全路径** | **459** | K=2→K=10 |\\n\\n**关键发现：VLA batched sampling 消除 K 作为 latency 因子。Adaptive K 快路径省 45% latency。CRM overhead 可忽略。**\\n\\n## Random Selection Baseline (2026-05-20)\\n\\n代码 `--mode random_selection` 可用。已有结果：seed43=9%, seed45=10%（之前标记 failed 是状态标记问题，实际正常完成）。\\n\\n## 全 Benchmark 统计摘要 (v2, 2026-05-20, 含新增数据)\\n\\n### 1. LIBERO-Object — **Strong improvement**\\n\\n| Method | n | Mean±Std | vs VLA Δ | p (Welch) | Sig |\\n|--------|---|----------|----------|-----------|-----|\\n| **CRM norm02 K=10 (主配置)** | **6** | **16.8%±1.8%** | **+6.0pp** | **0.000095** | **\\\\*\\\\*\\\\*** |\\n| CRM norm01 (补充) | 6 | 17.5%±1.0% | +6.6pp | <0.001 | *** |\\n| CRM norm02 K=5 (补充) | 7 | 16.0%±2.2% | +5.1pp | 0.000312 | *** |\\n| Adaptive-K (all) | 12 | 14.2%±1.5% | +3.3pp | 0.000098 | *** |\\n| Argmin K=10 | 5 | 12.4%±2.9% | +1.5pp | 0.317 | n.s. |\\n| **VLA-only** | **8** | **10.9%±1.4%** | — | — | — |\\n\\n### 2. LIBERO-Spatial — **Strong improvement**\\n\\n| Method | n | Mean±Std | vs VLA Δ | p (Welch) | Sig |\\n|--------|---|----------|----------|-----------|-----|\\n| CRM obs_only (K=10) | 7 | 34.6%±1.4% | **+5.0pp** | 0.000007 | *** |\\n| **VLA-only** | **9** | **29.6%±1.1%** | — | — | — |\\n\\n### 3. LIBERO-Goal (OOD) — **Neutral**\\n\\n| Method | n | Mean±Std | vs VLA Δ | p (Welch) | Sig |\\n|--------|---|----------|----------|-----------|-----|\\n| CRM obs_only | 7 | 67.7%±3.3% | -1.0pp | ~0.7 | n.s. |\\n| **VLA-only** | **6** | **68.7%±3.9%** | — | — | — |\\n\\n### 4. LIBERO-Long (OOD) — **⚠️ Borderline**\\n\\n| Method | n | Mean±Std | vs VLA Δ | p (Welch) | Sig |\\n|--------|---|----------|----------|-----------|-----|\\n| CRM obs_only | 7 | 17.0%±2.0% | **+2.2pp** | 0.049 | * |\\n| **VLA-only** | **11** | **14.8%±2.2%** | — | — | — |\\n\\n**⚠️ Long MW-U p=0.061 (n.s.)。t检验 p=0.049 刚好卡在 0.05 边缘。论文需 cautious wording。**\\n\\n### 效果总结\\n\\n| Benchmark | Δ (pp) | p-value | 判定 |\\n|-----------|--------|---------|------|\\n| **Object** | +6.0 | <0.001 | Strong (主配置 norm02) |\\n| **Spatial** | +5.0 | <0.001 | Strong |\\n| **Long** | +2.2 | 0.049 | ⚠️ Borderline (OOD, MW-U n.s.) |\\n| **Goal** | -1.0 | ~0.7 | Neutral (OOD) |\\n\\n**注意**: Argmin K=10 seed43=17% 是未验证离群值（4 台服务器未找到原始 JSON），标注 unverified。\\n\\n## 2026-05-20 新增 eval 结果（诊断中确认）\\n\\n| 实验 | 服务器 | Mode | Benchmark | norm | seed | SR | JSON 时间 |\\n|------|--------|------|-----------|------|------|----|-----------|\\n| eval-perdof-object-norm02-seed50 | bjb1-32546 | crm_perdof | object | 0.2 | 50 | 10.0% | 05-21 03:22 |\\n| eval-obs-only-object-norm02-seed51 | bjb1-32546 | crm_obs_only | object | 0.2 | 51 | 17.0% | 05-21 03:20 |\\n| eval-obs-only-object-norm005-seed44 | bjb1-18228 | crm_obs_only | object | 0.05 | 44 | 12.0% | 05-21 03:16 |\\n| eval-obs-only-object-norm01-seed48 | bjb1-18228 | crm_obs_only | object | 0.1 | 48 | **仍在运行** | — |\\n\\n**norm01-seed48**: PID 507385, 状态 Rl+, 运行 55m55s, GPU1 3408MiB/29%利用率, 已完成 5/10 tasks。预计再需约 1 小时完成。\", \"total_chars\": 9415, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "e17f41b1-3dce-49fb-a9e5-f5dd86423ed8",
  "uuid": "c3dd2752-e7c6-4014-a3ce-6231c770a2a5",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"path\\\": \\\"/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/memory.md\\\", \\\"content\\\": \\\"# Project Memory\\\\n\\\\n## 失败模式记录\\\\n\\\\n- [失败模式] Cron false positive：eval 脚本不写 W&B 也不写 sentinel file，进程正常退出后 cron 5 次检测找不到标记 → 自动标记为 failed。受影响：eval-vla-only-long-seed46, eval-vla-only-goal-seed46。修复方案：tail 日志确认实际完成 → 手动修正 conclusion=success + 补录 metrics。预防：eval 实验应检查 output JSON 是否存在作为 sentinel。\\\\n\\\\n- [失败模式] Cron false positive（2026-05-20）：**eval-adaptive-k-spatial-p50-seed42** 被 cron 误判为 failed（\\\\\\\"process dead 5× with no sentinel/W&B\\\\\\\"）。实际情况：原 PID 675831 被 deploy worker kill 后，重启为 PID 681823。重启后进程正常运行，但 cron 监控未追踪到新 PID，5 次检测均未发现 sentinel → 自动标记 failed。诊断时（2026-05-20）PID 681823 仍在运行（状态 Rl+，已运行 17h36m），已完成 3/10 tasks（SR: 70%/100%/0%），第 4 个 task 进行中（rollout 5, 1/5 success）。GPU 使用 5972/24564 MiB，日志无错误。**无需重新提交，等待自然完成后手动修正 conclusion。**\\\\n\\\\n- [失败模式] SIGHUP false failure（2026-05-20）：bjb2-28827 上多个实验 EXIT_CODE=129 (SIGHUP) 被标记 failed，实际全部完成。**已确认受影响：P75-seed44, P90-seed42, P25-seed44**。SIGHUP 发生在进程写完结果 JSON 之后（tmux session 断开或 SSH 连接清理）。**诊断方法：tail 日志看 \\\\\\\"Results saved to\\\\\\\" + \\\\\\\"Overall success rate\\\\\\\" 行 → 手动修正 conclusion=success 并补录 metrics。**\\\\n\\\\n- [失败模式] Cron 日志路径不匹配（2026-05-20）：**eval-obs-only-goal-norm02-seed51** (bjb1-32546) 被 cron 误判 dead。根因：实验日志写入 `/root/acr-vla-conformal-refinement/logs/`（项目目录下），但 cron 监控在 `~/runs/acr-vla-conformal-refinement/` 下找日志 → 找不到 → 5 次检测均无 sentinel → auto-resolved failed。**教训：submit_training_job 的 log_path 必须与实际 tee 输出路径一致。部分实验用 `tee logs/xxx.log`（相对于 cd 后的项目目录），另一部分用 `~/runs/` 绝对路径，两套路径并存导致 cron 误判。**\\\\n\\\\n- [失败模式] Cron false positive 批量（2026-05-20 诊断）：bjb1-32546 上 **eval-perdof-object-norm02-seed50** (PID 542405) 和 **eval-obs-only-object-norm02-seed51** (PID 542894) 被 cron 报告 \\\\\\\"process gone, no sentinel, no W&B\\\\\\\"。实际两者均已**正常完成**，output JSON 已写入。bjb1-18228 上 **eval-obs-only-object-norm005-seed44** 同样正常完成但被标记 failed。根因同上：eval 脚本不写 sentinel/W&B，进程正常退出后 cron 无法确认完成状态。结果：perdof-norm02-seed50 SR=10.0%, obs_only-norm02-seed51 SR=17.0%, obs_only-norm005-seed44 SR=12.0%。**均无需重跑，需手动修正 conclusion=success 并补录 metrics。**\\\\n\\\\n- [失败模式] python PATH 不存在（2026-05-21, bjb1-32546）：`nohup: failed to run command 'python': No such file or directory`。bjb1-32546 使用 conda 环境，`python` 不在默认 PATH 中（仅 `/root/miniconda3/bin/python` 可用）。受影响：seed51-r2, seed52-r2, seed62, seed63（4 个实验同时失败）。**修复方案：提交命令前加 `source /root/miniconda3/etc/profile.d/conda.sh && conda activate base &&` 前缀。** 教训：submit_training_job 的 command 不能假设 `python` 在 PATH 中，必须自带环境激活。对照其他服务器（bjb1-18228、bjb2-28827）成功实验的命令格式，它们通过 `bash -c \\\\\\\"source ... && python ...\\\\\\\"` 包裹。\\\\n\\\\n- [失败模式] FMVD 信号无效：ρ=0.0825 NO-GO。根因：denoising 空间统计量不映射到 action uncertainty。\\\\n\\\\n- [失败模式] CRM correction magnitude 信号无效（2026-05-20）：ρ(K1_corr_mag, K10_var) = 0.1523 NO-GO。**根因：CRM correction magnitude 是常数 (~0.1205)，P25=P50=P75=P90 几乎相同。** CRM 对所有输入产出相同大小的修正向量——修正方向变化但幅度不变。推测因 max_correction_norm=0.2 的 clipping 使得大部分 correction 被截断到相同 norm。K=2 argmin 版本同样无效 (ρ=0.1340)。**教训：clipped norm 的信号没有方差，自然无法做 gate。**\\\\n\\\\n- [失败模式] OpenVLA-7B eval timeout：timeout_hours 至少设 12h。\\\\n\\\\n- [失败模式] Table 1 数据混淆（2026-05-20）：Table 1 原报 CRM Object K=10 = 17.6% (n=7)，实际来自 **norm01+norm02 混合数据**。seed42 只有 norm01 (0.19)，seed43 只有 norm02 (0.16)，两个 config 各自只有 n=6，合并后变 n=7。paper_provenance.yaml C029 引用的 exp_id 是抽象 \\\\\\\"obs_only_k10\\\\\\\" 而非具体实验 ID，导致问题没被及时发现。**教训：provenance 必须引用具体 registry_id，不用抽象标签。**\\\\n\\\\n- [失败模式] evaluate.py 路径缺 src/ 前缀（2026-05-20）：adaptive_k spatial 实验命令用 `python evaluate.py` 而非 `python src/evaluate.py`，导致 EXIT_CODE=2 (No such file)。受影响：eval-adaptive-k-spatial-p50-seed43, eval-adaptive-k-spatial-p50-seed44（两台服务器 bjb1-32546, bjb2-28827 同时中招）。**教训：提交命令时对照历史成功实验的 command 格式，evaluate.py 在 src/ 子目录下。**\\\\n\\\\n## seed66 失败诊断 (2026-05-21)\\\\n- 根因：**Cron false positive（第 N 次）**。3 个 seed66 进程（norm003/norm005/norm01）实际仍在 bjb1-18228 上正常运行，被 cron 误判为 \\\\\\\"process dead 5× with no sentinel/W&B\\\\\\\"。\\\\n- 证据：\\\\n  - PID 642428 (norm003, GPU0), PID 642506 (norm005, GPU2), PID 642775 (norm01, GPU3) 均处于 Rl 状态，CPU 使用 ~400%，GPU 利用率 34-38%，VRAM ~5.7GB/卡\\\\n  - 日志在两次读取之间从 rollout 5/20 增长到 10/20，确认进程在推进\\\\n  - sentinels/ 目录完全为空——从未有实验写过 sentinel file\\\\n  - 无 OOM、无 CUDA error、无 traceback、无 segfault\\\\n  - 磁盘空间充足（根分区 53%，数据盘未挂载 autodl-tmp 但进程正常读写）\\\\n- 与 seed65 对比：seed65 (PID 622484, GPU1) 用 `nohup python -u` 启动，日志持续更新；seed66 用 `python3` 启动（无 `-u` 无 nohup），日志因 stdout 缓冲更新延迟，但进程本身正常\\\\n- 影响范围：eval-obs-only-object-norm005-seed66, eval-obs-only-object-norm01-seed66, eval-obs-only-object-norm003-seed66（3 个实验）\\\\n- 建议修复：**无需重跑**。等待进程自然完成（n_rollouts=20，当前约 50% 进度，预计再需 1-2 小时），完成后手动修正 conclusion=success 并从 output JSON 补录 metrics。\\\\n\\\\n## CRM Coverage 限制\\\\n\\\\nCRM v3 训练数据 = Object(10) + Spatial(10) = 20 tasks。Goal/Long 是 OOD 泛化测试。\\\\n\\\\n## Adaptive K 信号探索\\\\n\\\\n| 信号 | ρ vs K10_var | 结论 | 备注 |\\\\n|------|-------------|------|------|\\\\n| FMVD (velocity dispersion) | 0.0825 | ❌ NO-GO | zero-cost 但无效 |\\\\n| **K=2 L2 divergence** | **0.9979** | **✅ GO** | 需要 K=2 采样（+170ms），near-perfect proxy |\\\\n| CRM correction magnitude (K=1) | 0.1523 | ❌ NO-GO | zero-cost 但 magnitude 是常数 |\\\\n| CRM correction magnitude (K=2 argmin) | 0.1340 | ❌ NO-GO | 同上 |\\\\n\\\\n**结论：K=2 L2 distance 是唯一可用的 adaptive K 门控信号。** FMVD 和 CRM magnitude 均因信号方差不足而失败。\\\\n\\\\n## Adaptive K Sweep 最终结果 — Object (2026-05-20, 12/12 完成)\\\\n\\\\n| 阈值 | SR [seeds] | avg_K | fast_path% |\\\\n|------|-----------|-------|-----------|\\\\n| P90 (τ=0.127) | 13.3% [12,14,14] | ~2.6 | ~93% |\\\\n| P75 (τ=0.099) | 13.7% [12,13,16] | ~3.1 | ~87% |\\\\n| **P50 (τ=0.075)** | **15.3% [16,16,14]** | **~3.8** | **~77%** |\\\\n| P25 (τ=0.055) | 14.3% [15,13,15] | ~4.8 | ~65% |\\\\n\\\\n**P50 = Pareto optimal**: 最高 SR + 比 K=10 省 62% compute (avg_K 3.8 vs 10)。\\\\n\\\\n## Adaptive K Cross-Benchmark Sweep — Spatial (2026-05-20, 11/12 done)\\\\n\\\\nObject 校准阈值直接迁移到 Spatial（无 per-benchmark tuning）：\\\\n\\\\n| 阈值 | seed42 | seed43 | seed44 | Mean±Std | avg_K | fast_path |\\\\n|------|--------|--------|--------|----------|-------|-----------|\\\\n| P90 | 31% | 32% | PREPARING | — | ~3.5 | ~80% |\\\\n| P75 | 31% | 34% | 33% | 32.7%±1.5% | ~5.0 | ~62% |\\\\n| P50 | 30% | 33% | 33% | 32.0%±1.7% | ~6.35 | ~46% |\\\\n| P25 | 33% | 30% | 32% | 31.7%±1.5% | ~7.65 | ~29% |\\\\n\\\\nvs VLA-only Spatial: 29.6%±1.1% | vs CRM K=10 Spatial: 34.6%±1.4%\\\\n\\\\n**关键洞察**：\\\\n1. 所有阈值 SR 差异很小（31.7-32.7%），但 compute 差异 2x（avg_K 3.5→7.65）。P75 在 Spatial 上 Pareto 最优（32.7% + avg_K 5.0），P50 在 Object 上最优。\\\\n2. Spatial fast_path 远低于 Object（同阈值下 29% vs 65% for P25）—— Spatial L2 均值更高，方法自动分配更多 full-K steps。\\\\n3. 这支持\\\\\\\"阈值自动适配任务复杂度\\\\\\\"的核心 narrative：同一 Object 校准阈值，在更难的 Spatial 上自动降低 fast_path 比例以保持 SR。\\\\n\\\\n## Latency Profiling (dry-run N=20, RTX 4090, 2026-05-20)\\\\n\\\\n| Component | Mean (ms) | 备注 |\\\\n|-----------|----------|------|\\\\n| VLA sampling | 206 | **K 无关**（batched generation） |\\\\n| CRM MLP forward | 0.33 | 337K params |\\\\n| Argmin L2 + CRM 总开销 | 4.0 | 管线 1.6% |\\\\n| Full pipeline K=10 | 259 | ~3.9 Hz |\\\\n| **Adaptive K 快路径** | **254** | K=2 only |\\\\n| **Adaptive K 全路径** | **459** | K=2→K=10 |\\\\n\\\\n**关键发现：VLA batched sampling 消除 K 作为 latency 因子。Adaptive K 快路径省 45% latency。CRM overhead 可忽略。**\\\\n\\\\n## Random Selection Baseline (2026-05-20)\\\\n\\\\n代码 `--mode random_selection` 可用。已有结果：seed43=9%, seed45=10%（之前标记 failed 是状态标记问题，实际正常完成）。\\\\n\\\\n## 全 Benchmark 统计摘要 (v2, 2026-05-20, 含新增数据)\\\\n\\\\n### 1. LIBERO-Object — **Strong improvement**\\\\n\\\\n| Method | n | Mean±Std | vs VLA Δ | p (Welch) | Sig |\\\\n|--------|---|----------|----------|-----------|-----|\\\\n| **CRM norm02 K=10 (主配置)** | **6** | **16.8%±1.8%** | **+6.0pp** | **0.000095** | **\\\\\\\\*\\\\\\\\*\\\\\\\\*** |\\\\n| CRM norm01 (补充) | 6 | 17.5%±1.0% | +6.6pp | <0.001 | *** |\\\\n| CRM norm02 K=5 (补充) | 7 | 16.0%±2.2% | +5.1pp | 0.000312 | *** |\\\\n| Adaptive-K (all) | 12 | 14.2%±1.5% | +3.3pp | 0.000098 | *** |\\\\n| Argmin K=10 | 5 | 12.4%±2.9% | +1.5pp | 0.317 | n.s. |\\\\n| **VLA-only** | **8** | **10.9%±1.4%** | — | — | — |\\\\n\\\\n### 2. LIBERO-Spatial — **Strong improvement**\\\\n\\\\n| Method | n | Mean±Std | vs VLA Δ | p (Welch) | Sig |\\\\n|--------|---|----------|----------|-----------|-----|\\\\n| CRM obs_only (K=10) | 7 | 34.6%±1.4% | **+5.0pp** | 0.000007 | *** |\\\\n| **VLA-only** | **9** | **29.6%±1.1%** | — | — | — |\\\\n\\\\n### 3. LIBERO-Goal (OOD) — **Neutral**\\\\n\\\\n| Method | n | Mean±Std | vs VLA Δ | p (Welch) | Sig |\\\\n|--------|---|----------|----------|-----------|-----|\\\\n| CRM obs_only | 7 | 67.7%±3.3% | -1.0pp | ~0.7 | n.s. |\\\\n| **VLA-only** | **6** | **68.7%±3.9%** | — | — | — |\\\\n\\\\n### 4. LIBERO-Long (OOD) — **⚠️ Borderline**\\\\n\\\\n| Method | n | Mean±Std | vs VLA Δ | p (Welch) | Sig |\\\\n|--------|---|----------|----------|-----------|-----|\\\\n| CRM obs_only | 7 | 17.0%±2.0% | **+2.2pp** | 0.049 | * |\\\\n| **VLA-only** | **11** | **14.8%±2.2%** | — | — | — |\\\\n\\\\n**⚠️ Long MW-U p=0.061 (n.s.)。t检验 p=0.049 刚好卡在 0.05 边缘。论文需 cautious wording。**\\\\n\\\\n### 效果总结\\\\n\\\\n| Benchmark | Δ (pp) | p-value | 判定 |\\\\n|-----------|--------|---------|------|\\\\n| **Object** | +6.0 | <0.001 | Strong (主配置 norm02) |\\\\n| **Spatial** | +5.0 | <0.001 | Strong |\\\\n| **Long** | +2.2 | 0.049 | ⚠️ Borderline (OOD, MW-U n.s.) |\\\\n| **Goal** | -1.0 | ~0.7 | Neutral (OOD) |\\\\n\\\\n**注意**: Argmin K=10 seed43=17% 是未验证离群值（4 台服务器未找到原始 JSON），标注 unverified。\\\\n\\\\n## 2026-05-20 新增 eval 结果（诊断中确认）\\\\n\\\\n| 实验 | 服务器 | Mode | Benchmark | norm | seed | SR | JSON 时间 |\\\\n|------|--------|------|-----------|------|------|----|-----------|\\\\n| eval-perdof-object-norm02-seed50 | bjb1-32546 | crm_perdof | object | 0.2 | 50 | 10.0% | 05-21 03:22 |\\\\n| eval-obs-only-object-norm02-seed51 | bjb1-32546 | crm_obs_only | object | 0.2 | 51 | 17.0% | 05-21 03:20 |\\\\n| eval-obs-only-object-norm005-seed44 | bjb1-18228 | crm_obs_only | object | 0.05 | 44 | 12.0% | 05-21 03:16 |\\\\n| eval-obs-only-object-norm01-seed48 | bjb1-18228 | crm_obs_only | object | 0.1 | 48 | **仍在运行** | — |\\\\n\\\\n**norm01-seed48**: PID 507385, 状态 Rl+, 运行 55m55s, GPU1 3408MiB/29%利用率, 已完成 5/10 tasks。预计再需约 1 小时完成。\\\", \\\"total_chars\\\": 9415, \\\"truncated\\\": false}, \\\"error\\\": null, \\\"metadata\\\": {}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/memory.md\", \"content\": \"# Project Memory\\n\\n## 失败模式记录\\n\\n- [失败模式] Cron false positive：eval 脚本不写 W&B 也不写 sentinel file，进程正常退出后 cron 5 次检测找不到标记 → 自动标记为 failed。受影响：eval-vla-only-long-seed46, eval-vla-only-goal-seed46。修复方案：tail 日志确认实际完成 → 手动修正 conclusion=success + 补录 metrics。预防：eval 实验应检查 output JSON 是否存在作为 sentinel。\\n\\n- [失败模式] Cron false positive（2026-05-20）：**eval-adaptive-k-spatial-p50-seed42** 被 cron 误判为 failed（\\\"process dead 5× with no sentinel/W&B\\\"）。实际情况：原 PID 675831 被 deploy worker kill 后，重启为 PID 681823。重启后进程正常运行，但 cron 监控未追踪到新 PID，5 次检测均未发现 sentinel → 自动标记 failed。诊断时（2026-05-20）PID 681823 仍在运行（状态 Rl+，已运行 17h36m），已完成 3/10 tasks（SR: 70%/100%/0%），第 4 个 task 进行中（rollout 5, 1/5 success）。GPU 使用 5972/24564 MiB，日志无错误。**无需重新提交，等待自然完成后手动修正 conclusion。**\\n\\n- [失败模式] SIGHUP false failure（2026-05-20）：bjb2-28827 上多个实验 EXIT_CODE=129 (SIGHUP) 被标记 failed，实际全部完成。**已确认受影响：P75-seed44, P90-seed42, P25-seed44**。SIGHUP 发生在进程写完结果 JSON 之后（tmux session 断开或 SSH 连接清理）。**诊断方法：tail 日志看 \\\"Results saved to\\\" + \\\"Overall success rate\\\" 行 → 手动修正 conclusion=success 并补录 metrics。**\\n\\n- [失败模式] Cron 日志路径不匹配（2026-05-20）：**eval-obs-only-goal-norm02-seed51** (bjb1-32546) 被 cron 误判 dead。根因：实验日志写入 `/root/acr-vla-conformal-refinement/logs/`（项目目录下），但 cron 监控在 `~/runs/acr-vla-conformal-refinement/` 下找日志 → 找不到 → 5 次检测均无 sentinel → auto-resolved failed。**教训：submit_training_job 的 log_path 必须与实际 tee 输出路径一致。部分实验用 `tee logs/xxx.log`（相对于 cd 后的项目目录），另一部分用 `~/runs/` 绝对路径，两套路径并存导致 cron 误判。**\\n\\n- [失败模式] Cron false positive 批量（2026-05-20 诊断）：bjb1-32546 上 **eval-perdof-object-norm02-seed50** (PID 542405) 和 **eval-obs-only-object-norm02-seed51** (PID 542894) 被 cron 报告 \\\"process gone, no sentinel, no W&B\\\"。实际两者均已**正常完成**，output JSON 已写入。bjb1-18228 上 **eval-obs-only-object-norm005-seed44** 同样正常完成但被标记 failed。根因同上：eval 脚本不写 sentinel/W&B，进程正常退出后 cron 无法确认完成状态。结果：perdof-norm02-seed50 SR=10.0%, obs_only-norm02-seed51 SR=17.0%, obs_only-norm005-seed44 SR=12.0%。**均无需重跑，需手动修正 conclusion=success 并补录 metrics。**\\n\\n- [失败模式] python PATH 不存在（2026-05-21, bjb1-32546）：`nohup: failed to run command 'python': No such file or directory`。bjb1-32546 使用 conda 环境，`python` 不在默认 PATH 中（仅 `/root/miniconda3/bin/python` 可用）。受影响：seed51-r2, seed52-r2, seed62, seed63（4 个实验同时失败）。**修复方案：提交命令前加 `source /root/miniconda3/etc/profile.d/conda.sh && conda activate base &&` 前缀。** 教训：submit_training_job 的 command 不能假设 `python` 在 PATH 中，必须自带环境激活。对照其他服务器（bjb1-18228、bjb2-28827）成功实验的命令格式，它们通过 `bash -c \\\"source ... && python ...\\\"` 包裹。\\n\\n- [失败模式] FMVD 信号无效：ρ=0.0825 NO-GO。根因：denoising 空间统计量不映射到 action uncertainty。\\n\\n- [失败模式] CRM correction magnitude 信号无效（2026-05-20）：ρ(K1_corr_mag, K10_var) = 0.1523 NO-GO。**根因：CRM correction magnitude 是常数 (~0.1205)，P25=P50=P75=P90 几乎相同。** CRM 对所有输入产出相同大小的修正向量——修正方向变化但幅度不变。推测因 max_correction_norm=0.2 的 clipping 使得大部分 correction 被截断到相同 norm。K=2 argmin 版本同样无效 (ρ=0.1340)。**教训：clipped norm 的信号没有方差，自然无法做 gate。**\\n\\n- [失败模式] OpenVLA-7B eval timeout：timeout_hours 至少设 12h。\\n\\n- [失败模式] Table 1 数据混淆（2026-05-20）：Table 1 原报 CRM Object K=10 = 17.6% (n=7)，实际来自 **norm01+norm02 混合数据**。seed42 只有 norm01 (0.19)，seed43 只有 norm02 (0.16)，两个 config 各自只有 n=6，合并后变 n=7。paper_provenance.yaml C029 引用的 exp_id 是抽象 \\\"obs_only_k10\\\" 而非具体实验 ID，导致问题没被及时发现。**教训：provenance 必须引用具体 registry_id，不用抽象标签。**\\n\\n- [失败模式] evaluate.py 路径缺 src/ 前缀（2026-05-20）：adaptive_k spatial 实验命令用 `python evaluate.py` 而非 `python src/evaluate.py`，导致 EXIT_CODE=2 (No such file)。受影响：eval-adaptive-k-spatial-p50-seed43, eval-adaptive-k-spatial-p50-seed44（两台服务器 bjb1-32546, bjb2-28827 同时中招）。**教训：提交命令时对照历史成功实验的 command 格式，evaluate.py 在 src/ 子目录下。**\\n\\n## seed66 失败诊断 (2026-05-21)\\n- 根因：**Cron false positive（第 N 次）**。3 个 seed66 进程（norm003/norm005/norm01）实际仍在 bjb1-18228 上正常运行，被 cron 误判为 \\\"process dead 5× with no sentinel/W&B\\\"。\\n- 证据：\\n  - PID 642428 (norm003, GPU0), PID 642506 (norm005, GPU2), PID 642775 (norm01, GPU3) 均处于 Rl 状态，CPU 使用 ~400%，GPU 利用率 34-38%，VRAM ~5.7GB/卡\\n  - 日志在两次读取之间从 rollout 5/20 增长到 10/20，确认进程在推进\\n  - sentinels/ 目录完全为空——从未有实验写过 sentinel file\\n  - 无 OOM、无 CUDA error、无 traceback、无 segfault\\n  - 磁盘空间充足（根分区 53%，数据盘未挂载 autodl-tmp 但进程正常读写）\\n- 与 seed65 对比：seed65 (PID 622484, GPU1) 用 `nohup python -u` 启动，日志持续更新；seed66 用 `python3` 启动（无 `-u` 无 nohup），日志因 stdout 缓冲更新延迟，但进程本身正常\\n- 影响范围：eval-obs-only-object-norm005-seed66, eval-obs-only-object-norm01-seed66, eval-obs-only-object-norm003-seed66（3 个实验）\\n- 建议修复：**无需重跑**。等待进程自然完成（n_rollouts=20，当前约 50% 进度，预计再需 1-2 小时），完成后手动修正 conclusion=success 并从 output JSON 补录 metrics。\\n\\n## CRM Coverage 限制\\n\\nCRM v3 训练数据 = Object(10) + Spatial(10) = 20 tasks。Goal/Long 是 OOD 泛化测试。\\n\\n## Adaptive K 信号探索\\n\\n| 信号 | ρ vs K10_var | 结论 | 备注 |\\n|------|-------------|------|------|\\n| FMVD (velocity dispersion) | 0.0825 | ❌ NO-GO | zero-cost 但无效 |\\n| **K=2 L2 divergence** | **0.9979** | **✅ GO** | 需要 K=2 采样（+170ms），near-perfect proxy |\\n| CRM correction magnitude (K=1) | 0.1523 | ❌ NO-GO | zero-cost 但 magnitude 是常数 |\\n| CRM correction magnitude (K=2 argmin) | 0.1340 | ❌ NO-GO | 同上 |\\n\\n**结论：K=2 L2 distance 是唯一可用的 adaptive K 门控信号。** FMVD 和 CRM magnitude 均因信号方差不足而失败。\\n\\n## Adaptive K Sweep 最终结果 — Object (2026-05-20, 12/12 完成)\\n\\n| 阈值 | SR [seeds] | avg_K | fast_path% |\\n|------|-----------|-------|-----------|\\n| P90 (τ=0.127) | 13.3% [12,14,14] | ~2.6 | ~93% |\\n| P75 (τ=0.099) | 13.7% [12,13,16] | ~3.1 | ~87% |\\n| **P50 (τ=0.075)** | **15.3% [16,16,14]** | **~3.8** | **~77%** |\\n| P25 (τ=0.055) | 14.3% [15,13,15] | ~4.8 | ~65% |\\n\\n**P50 = Pareto optimal**: 最高 SR + 比 K=10 省 62% compute (avg_K 3.8 vs 10)。\\n\\n## Adaptive K Cross-Benchmark Sweep — Spatial (2026-05-20, 11/12 done)\\n\\nObject 校准阈值直接迁移到 Spatial（无 per-benchmark tuning）：\\n\\n| 阈值 | seed42 | seed43 | seed44 | Mean±Std | avg_K | fast_path |\\n|------|--------|--------|--------|----------|-------|-----------|\\n| P90 | 31% | 32% | PREPARING | — | ~3.5 | ~80% |\\n| P75 | 31% | 34% | 33% | 32.7%±1.5% | ~5.0 | ~62% |\\n| P50 | 30% | 33% | 33% | 32.0%±1.7% | ~6.35 | ~46% |\\n| P25 | 33% | 30% | 32% | 31.7%±1.5% | ~7.65 | ~29% |\\n\\nvs VLA-only Spatial: 29.6%±1.1% | vs CRM K=10 Spatial: 34.6%±1.4%\\n\\n**关键洞察**：\\n1. 所有阈值 SR 差异很小（31.7-32.7%），但 compute 差异 2x（avg_K 3.5→7.65）。P75 在 Spatial 上 Pareto 最优（32.7% + avg_K 5.0），P50 在 Object 上最优。\\n2. Spatial fast_path 远低于 Object（同阈值下 29% vs 65% for P25）—— Spatial L2 均值更高，方法自动分配更多 full-K steps。\\n3. 这支持\\\"阈值自动适配任务复杂度\\\"的核心 narrative：同一 Object 校准阈值，在更难的 Spatial 上自动降低 fast_path 比例以保持 SR。\\n\\n## Latency Profiling (dry-run N=20, RTX 4090, 2026-05-20)\\n\\n| Component | Mean (ms) | 备注 |\\n|-----------|----------|------|\\n| VLA sampling | 206 | **K 无关**（batched generation） |\\n| CRM MLP forward | 0.33 | 337K params |\\n| Argmin L2 + CRM 总开销 | 4.0 | 管线 1.6% |\\n| Full pipeline K=10 | 259 | ~3.9 Hz |\\n| **Adaptive K 快路径** | **254** | K=2 only |\\n| **Adaptive K 全路径** | **459** | K=2→K=10 |\\n\\n**关键发现：VLA batched sampling 消除 K 作为 latency 因子。Adaptive K 快路径省 45% latency。CRM overhead 可忽略。**\\n\\n## Random Selection Baseline (2026-05-20)\\n\\n代码 `--mode random_selection` 可用。已有结果：seed43=9%, seed45=10%（之前标记 failed 是状态标记问题，实际正常完成）。\\n\\n## 全 Benchmark 统计摘要 (v2, 2026-05-20, 含新增数据)\\n\\n### 1. LIBERO-Object — **Strong improvement**\\n\\n| Method | n | Mean±Std | vs VLA Δ | p (Welch) | Sig |\\n|--------|---|----------|----------|-----------|-----|\\n| **CRM norm02 K=10 (主配置)** | **6** | **16.8%±1.8%** | **+6.0pp** | **0.000095** | **\\\\*\\\\*\\\\*** |\\n| CRM norm01 (补充) | 6 | 17.5%±1.0% | +6.6pp | <0.001 | *** |\\n| CRM norm02 K=5 (补充) | 7 | 16.0%±2.2% | +5.1pp | 0.000312 | *** |\\n| Adaptive-K (all) | 12 | 14.2%±1.5% | +3.3pp | 0.000098 | *** |\\n| Argmin K=10 | 5 | 12.4%±2.9% | +1.5pp | 0.317 | n.s. |\\n| **VLA-only** | **8** | **10.9%±1.4%** | — | — | — |\\n\\n### 2. LIBERO-Spatial — **Strong improvement**\\n\\n| Method | n | Mean±Std | vs VLA Δ | p (Welch) | Sig |\\n|--------|---|----------|----------|-----------|-----|\\n| CRM obs_only (K=10) | 7 | 34.6%±1.4% | **+5.0pp** | 0.000007 | *** |\\n| **VLA-only** | **9** | **29.6%±1.1%** | — | — | — |\\n\\n### 3. LIBERO-Goal (OOD) — **Neutral**\\n\\n| Method | n | Mean±Std | vs VLA Δ | p (Welch) | Sig |\\n|--------|---|----------|----------|-----------|-----|\\n| CRM obs_only | 7 | 67.7%±3.3% | -1.0pp | ~0.7 | n.s. |\\n| **VLA-only** | **6** | **68.7%±3.9%** | — | — | — |\\n\\n### 4. LIBERO-Long (OOD) — **⚠️ Borderline**\\n\\n| Method | n | Mean±Std | vs VLA Δ | p (Welch) | Sig |\\n|--------|---|----------|----------|-----------|-----|\\n| CRM obs_only | 7 | 17.0%±2.0% | **+2.2pp** | 0.049 | * |\\n| **VLA-only** | **11** | **14.8%±2.2%** | — | — | — |\\n\\n**⚠️ Long MW-U p=0.061 (n.s.)。t检验 p=0.049 刚好卡在 0.05 边缘。论文需 cautious wording。**\\n\\n### 效果总结\\n\\n| Benchmark | Δ (pp) | p-value | 判定 |\\n|-----------|--------|---------|------|\\n| **Object** | +6.0 | <0.001 | Strong (主配置 norm02) |\\n| **Spatial** | +5.0 | <0.001 | Strong |\\n| **Long** | +2.2 | 0.049 | ⚠️ Borderline (OOD, MW-U n.s.) |\\n| **Goal** | -1.0 | ~0.7 | Neutral (OOD) |\\n\\n**注意**: Argmin K=10 seed43=17% 是未验证离群值（4 台服务器未找到原始 JSON），标注 unverified。\\n\\n## 2026-05-20 新增 eval 结果（诊断中确认）\\n\\n| 实验 | 服务器 | Mode | Benchmark | norm | seed | SR | JSON 时间 |\\n|------|--------|------|-----------|------|------|----|-----------|\\n| eval-perdof-object-norm02-seed50 | bjb1-32546 | crm_perdof | object | 0.2 | 50 | 10.0% | 05-21 03:22 |\\n| eval-obs-only-object-norm02-seed51 | bjb1-32546 | crm_obs_only | object | 0.2 | 51 | 17.0% | 05-21 03:20 |\\n| eval-obs-only-object-norm005-seed44 | bjb1-18228 | crm_obs_only | object | 0.05 | 44 | 12.0% | 05-21 03:16 |\\n| eval-obs-only-object-norm01-seed48 | bjb1-18228 | crm_obs_only | object | 0.1 | 48 | **仍在运行** | — |\\n\\n**norm01-seed48**: PID 507385, 状态 Rl+, 运行 55m55s, GPU1 3408MiB/29%利用率, 已完成 5/10 tasks。预计再需约 1 小时完成。\", \"total_chars\": 9415, \"truncated\": false}, \"error\": null, \"metadata\": {}}"
    }
  }
}
```

</details>

---

### Assistant

_source line 24_

<details><summary>Logged reasoning block</summary>

```text
Now I have much more data. The report shows 546 total experiments, with 498 DONE. The memory.md has valuable info about the norm sweep.

Key findings from memory.md:
1. Memory has a "全 Benchmark 统计摘要" with CRM norm02 K=10 on Object: n=6, 16.8%±1.8%
2. There's also info about norm02 seed51: SR=17.0%
3. norm005 seed44: SR=12.0%

But the registry only returned 64 experiments total (not 546). 

There's a discrepancy here—the report claims 546 experiments but my registry query with `limit=0` only returned 64 total. Either the limit parameter doesn't work as expected, or the registry is filtering by project or applying some other constraint I'm not accounting for. I need to consolidate the experimental data from both the registry and memory.md to get a complete picture. From memory.md, I can see the norm sweep statistics showing CRM norm02 with K=10 at n=6 with 16.8%±1.8%, and I've got individual seed confirmations like seed51 at 17% and seed44 at 12%. Let me cross-reference these to figure out the actual sample sizes and fill in any gaps.

Looking at the performance table across different epsilon values, I can see norm02 is locked with 12 seeds total, though they might not all be labeled with "norm02" in the registry. The main configuration in the benchmark summary shows n=6 at 16.8%±1.8%, but this appears to be a subset of the full 12-seed dataset.

The memory notes reveal that the original Table 1 result was actually a mixture of norm01 and norm02 data—seed42 came from norm01 alone while seed43 came from norm02 alone, with each configuration having just n=6 seeds initially. I need to track down the individual success rates for those original norm02 seeds, likely seed43 through seed48, to understand the full picture. Looking at the discrepancy between what the registry returned (64 total experiments) and what the report claims (546 total), it seems the registry tool has a limit or the data might be archived differently. The report could be including compacted or historical experiments that aren't accessible through the current query interface.

Since I'm working with the available data, I'm now compiling all the successful norm sweep experiments from the registry, organizing them by epsilon value and seed, noting their current status and performance metrics. I'm calculating the mean success rate for ε=0.05 across six seeds, which comes to 14.5%. Now I'm noticing discrepancies between the report and my registry query—there are recent completed experiments listed in the report that aren't showing up in my results, which suggests the registry contains more data than what's being returned.

Let me try a broader search approach since the limit parameter might have a hidden cap. I'm looking at the currently running norm sweep experiments from the report to get a sense of what's actively being tracked across the different GPU nodes.

I'm realizing the registry tool is probably only returning the 64 most recently updated experiments, which explains why my query missed so many of the 546 total experiments in the sweep.

Let me try a different approach—I could use the auto-generated report.md data directly, or attempt to query the registry with more specific filters, though it likely only supports exact field matches rather than pattern matching. Maybe I should focus on computing what I need from the data I already have access to. I'm noticing a discrepancy in the completed experiments — some show process failures but are still marked as successful, which seems contradictory. Let me examine the report data more carefully to understand what actually happened with these runs.

Looking at my full registry, I'm filtering for all experiments matching the norm pattern that have both a success conclusion and metrics, even if they're still in PREPARING status rather than DONE. I'm going through the different epsilon values and their corresponding seeds to get an accurate count of what actually succeeded. Looking at the results for epsilon=0.1, I'm seeing seed60 through seed48 with success rates ranging from 0.13 to 0.19. For epsilon=0.2, the memory shows only 6 seeds averaging 16.8%, but the roadmap indicates there should be 12 seeds total—I'm trying to figure out where the remaining seeds are, since the roadmap mentions a 7-seed core plus extras that should add up to that target.

Scanning through the registry, I'm noticing the naming conventions have shifted over time—earlier experiments used "eval-mag-obsonly-norm*" for the magnitude sweep, while later ones switched to "eval-obs-only-object-norm02-*" format. I need to reconcile these different naming schemes to find all the seeds that belong to the norm sweep, since the magnitude sweep and norm sweep are actually the same thing.

Based on what I can verify from the registry and memory.md, I'm planning to compile the results by using the available data points for each epsilon value: pulling the ε=0.03, 0.05, 0.1 results directly from the registry, using the memory.md statistics for ε=0.2 (which shows n=6 with 16.8%±1.8%, plus seed51 bringing it to 7), and flagging that while the ROADMAP claims 12 total seeds for ε=0.2, I can only confirm 7 so far.

Now I'm noticing the report mentions recently completed experiments that aren't in my initial 64-experiment query—these might have been moved to a different status or the registry has a practical limit on what it returns. I should look at those recently completed entries from the report to see if I can extract their success rates, though I'll need to track down their specific metrics since they're not showing up in my standard query.

Let me organize what I actually have access to: the ε=0.03 experiments show a mean success rate around 15.4% across seven seeds, while the ε=0.05 group has five registry entries ranging from 14-16% plus one memory-based result at 12%.

For ε=0.1, I'm seeing five seeds with results clustering around 15-19%, giving a mean of 16%. The ε=0.2 data from memory.md indicates a mean of 16.8% with standard deviation of 1.8% for the core seeds, and I've now confirmed seed 51 at 17%, but the ROADMAP suggests there should be twelve total experiments here—meaning I'm still missing several results that were apparently completed recently. The discrepancy suggests there are more experiments in the registry that I haven't captured yet, though the ROADMAP numbers themselves might be approximate given the "~" notation. I'm noticing some recently completed experiments in the report that could account for the missing seeds, so let me cross-reference those entries more carefully to fill in the gaps.

Since I have enough data from the registry and my notes to work with, I'll proceed with the analysis and flag where the sample sizes are incomplete. Now I'm calculating the success rate statistics across the different epsilon values to get means and standard deviations for each group.

For ε=0.2, I have six seeds from memory showing 16.8%±1.8%, and adding seed51's 17% gives me a new mean around 16.83%, which barely shifts the standard deviation. But the ROADMAP claims 17.2% with twelve seeds total, so the missing experiments must have pushed the average higher than what I'm seeing so far.

I'm noticing some of the completed experiments were marked as false positives from cron issues, so I need to be careful about which results to trust. Looking at what's still in progress, I have a couple preparing and several actively running across different norm configurations and seeds. I think I have enough data now to start compiling the results.

But I need to standardize the metric formats first—the data uses different field names like `overall_success_rate` versus `success_rate`, and the values are sometimes fractions and sometimes integer percentages. Let me normalize these across my norm sweep data so I can compare them consistently.

Now I'm checking which experiments are currently running to see what additional data points they'll contribute once they complete.

Looking at the norm sweep experiments specifically, I see several seeds already in progress across different epsilon values, plus many more listed as preparing in the report. The roadmap indicated around 9 seeds for ε=0.05, but I've only located 6 so far—the missing ones might be seeds like 72 and 43 that have either recently finished or are still running.

Given that the registry tool likely has result limits and experiments have completed since the roadmap was created, I'll work with the data I have and calculate confidence intervals for each epsilon value. For the CI95 calculations, I'm using the appropriate t-values based on sample size: 2.447 for n=7, 2.571 for n=6, and 2.776 for n=5.

Now computing the statistics for ε=0.03 with n=7...

For the success rates [13, 15, 15, 15, 16, 17, 17], the mean is 15.43%, and after calculating variance and standard error, the 95% confidence interval comes out to approximately [14.1%, 16.7%].

Now with ε=0.05 and a smaller sample of six success rates [12, 14, 15, 15, 15, 16], the mean drops to 14.50%, and the confidence interval widens to around [13.1%, 15.9%].

Moving to ε=0.1 with five observations [13, 15, 15, 18, 19], the mean increases to 16.00% but the interval expands further to [13.0%, 19.0%] due to higher variability. For ε=0.2, I'm recalling from memory that the core sample of six had a mean around 16.8% with a standard deviation of 1.8%.

Finishing the ε=0.2 calculation, the 95% confidence interval comes out to [14.9%, 18.7%]. With seed51 adding a seventh observation, the mean stays near 16.83%, though I can't compute the exact standard deviation without all individual values.

Looking across all epsilon values, the confidence intervals overlap substantially—there's no clear statistical separation between any of them, suggesting the epsilon parameter doesn't produce meaningfully different success rates.

To test whether ε=0.05 and ε=0.2 (the most separated means) differ significantly, I'm running a Welch's t-test to account for potentially unequal variances...

The t-statistic comes out to 2.48 with approximately 9 degrees of freedom, which exceeds the critical value of 2.262 at α=0.05, suggesting the difference might be marginally significant—though with these small sample sizes, I should be cautious about drawing firm conclusions.

Now I'm comparing my experimental results against what the ROADMAP claims. My measurements show ε=0.03 at 7 seeds with 15.4% success, ε=0.05 at 6 seeds with 14.5%, and so on, which mostly align with the ROADMAP's predictions but with some variation in seed counts and percentages. I have enough to write up the report now.

I'm noticing a pattern where the ROADMAP's numbers for ε=0.05 and ε=0.1 seem to include more seeds than what I've found, which could explain why their means are slightly lower. But there's another possibility—the registry shows 546 total experiments, yet my query only pulled 64, so there might be completed experiments I haven't accessed yet.

Looking back at the memory, I see there's a section mentioning eval-obs-only-object-norm005-seed44 with SR=12.0%, and the report notes that seed43 for norm005 has a killed r3 run plus a running version. The report also indicates the recent 3 successes have an overall success rate of 0.16, which aligns with the general trend I'm seeing.

I should try querying the registry with different parameters to capture more of the norm sweep data I'm missing.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "e17f41b1-3dce-49fb-a9e5-f5dd86423ed8",
  "uuid": "62d89162-d1e4-4631-b128-b6d57e7e84b4",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0128oUs5FWyubqhQ6Qg4ziMR",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 14878,
      "cache_read_input_tokens": 65726,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 14878
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

registry 只返回了 64 条但 report 说有 546 个实验。让我尝试用 project filter 获取更多数据，并检查是否有已完成的 norm sweep 实验未被返回。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "e17f41b1-3dce-49fb-a9e5-f5dd86423ed8",
  "uuid": "62cf2d6d-51e8-49d0-9ac2-c1902ebcc97f",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0128oUs5FWyubqhQ6Qg4ziMR",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 14878,
      "cache_read_input_tokens": 65726,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 14878
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

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry · `toolu_01HntyS4xKYgwRJHP4h5urLv`</summary>

```json
{
  "filters": {
    "status": "DONE",
    "conclusion": "success"
  },
  "limit": 0,
  "fields": [
    "status",
    "conclusion",
    "metrics"
  ],
  "project": "acr-vla-conformal-refinement"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "e17f41b1-3dce-49fb-a9e5-f5dd86423ed8",
  "uuid": "1c52dfa1-f16c-4e1c-84c6-3ffe25855323",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0128oUs5FWyubqhQ6Qg4ziMR",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 14878,
      "cache_read_input_tokens": 65726,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 14878
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

_source line 27 · 2026-05-21T03:27:04.249Z_

<details><summary>↩ Tool result · `toolu_01HntyS4xKYgwRJHP4h5urLv`</summary>

```text
Error: result (104,258 characters) exceeds maximum allowed tokens. Output has been saved to /home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-8-projects-acr-vla-conformal-refinement/e17f41b1-3dce-49fb-a9e5-f5dd86423ed8/tool-results/mcp-agent-ml-research-read_registry-1779334024221.txt.
Format: JSON with schema: {result: string}
- For targeted queries (find a value, filter by field): use jq on the file directly.
- For analysis or summarization that requires reading the full content: first probe the structure (e.g., jq 'type, length, keys?' /home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-8-projects-acr-vla-conformal-refinement/e17f41b1-3dce-49fb-a9e5-f5dd86423ed8/tool-results/mcp-agent-ml-research-read_registry-1779334024221.txt), then extract slices with jq or python — Read's line-based offset/limit will not chunk this file.
- If the Agent tool is available, do this inside a subagent so the full output stays out of your main context. Give it the instruction above verbatim, and be explicit about what it must return — e.g. "/home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-8-projects-acr-vla-conformal-refinement/e17f41b1-3dce-49fb-a9e5-f5dd86423ed8/tool-results/mcp-agent-ml-research-read_registry-1779334024221.txt is JSON with schema: {result: string}; probe the structure with jq (type/length/keys), then extract and read the content in full with jq or python, then summarize and quote any key findings verbatim." A vague "summarize this" may lose detail.

```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "e17f41b1-3dce-49fb-a9e5-f5dd86423ed8",
  "uuid": "e8a3321f-c1ff-4c71-b46c-a02a16985666",
  "tool_use_result": {
    "content": "Error: result (104,258 characters) exceeds maximum allowed tokens. Output has been saved to /home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-8-projects-acr-vla-conformal-refinement/e17f41b1-3dce-49fb-a9e5-f5dd86423ed8/tool-results/mcp-agent-ml-research-read_registry-1779334024221.txt.\nFormat: JSON with schema: {result: string}\n- For targeted queries (find a value, filter by field): use jq on the file directly.\n- For analysis or summarization that requires reading the full content: first probe the structure (e.g., jq 'type, length, keys?' /home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-8-projects-acr-vla-conformal-refinement/e17f41b1-3dce-49fb-a9e5-f5dd86423ed8/tool-results/mcp-agent-ml-research-read_registry-1779334024221.txt), then extract slices with jq or python — Read's line-based offset/limit will not chunk this file.\n- If the Agent tool is available, do this inside a subagent so the full output stays out of your main context. Give it the instruction above verbatim, and be explicit about what it must return — e.g. \"/home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-8-projects-acr-vla-conformal-refinement/e17f41b1-3dce-49fb-a9e5-f5dd86423ed8/tool-results/mcp-agent-ml-research-read_registry-1779334024221.txt is JSON with schema: {result: string}; probe the structure with jq (type/length/keys), then extract and read the content in full with jq or python, then summarize and quote any key findings verbatim.\" A vague \"summarize this\" may lose detail.\n",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"experiments\": {\"eval-obs-only-object-norm01-seed57\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.19}}, \"eval-obs-only-object-norm005-seed65\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.14}}, \"eval-obs-only-object-norm005-seed61\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.15}}, \"eval-obs-only-object-norm005-seed58\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.16}}, \"eval-obs-only-object-norm003-seed59\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.13}}, \"eval-obs-only-object-norm003-seed56\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.15}}, \"eval-obs-only-object-norm005-seed75\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.15, \"total_rollouts\": 100}}, \"eval-obs-only-object-norm01-seed74\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.13, \"total_rollouts\": 100}}, \"eval-obs-only-object-norm005-seed72\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.11, \"total_rollouts\": 100}}, \"eval-obs-only-object-norm01-seed71\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.16, \"total_rollouts\": 100}}, \"eval-obs-only-object-norm003-seed73\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.16, \"total_rollouts\": 100}}, \"eval-obs-only-object-norm01-seed51-r3\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.11}}, \"eval-obs-only-object-norm01-seed52-r3\": {\"status\": \"DONE\", \"metrics\": {\"overall_success_rate\": 0.15}, \"conclusion\": \"success\"}, \"eval-obs-only-object-norm01-seed65\": {\"status\": \"DONE\", \"metrics\": {\"overall_success_rate\": 0.15}, \"conclusion\": \"success\"}, \"eval-obs-only-object-norm01-seed64\": {\"status\": \"DONE\", \"metrics\": {\"overall_success_rate\": 0.15}, \"conclusion\": \"success\"}, \"eval-obs-only-object-norm005-seed64\": {\"status\": \"DONE\", \"metrics\": {\"overall_success_rate\": 0.15}, \"conclusion\": \"success\"}, \"eval-obs-only-object-norm003-seed65\": {\"status\": \"DONE\", \"metrics\": {\"overall_success_rate\": 0.17}, \"conclusion\": \"success\"}, \"eval-obs-only-object-norm003-seed64\": {\"status\": \"DONE\", \"metrics\": {\"overall_success_rate\": 0.17}, \"conclusion\": \"success\"}, \"eval-vla-only-object-seed49\": {\"status\": \"DONE\", \"metrics\": {\"success_rate\": 0.1, \"total_rollouts\": 100, \"successful_rollouts\": 10}, \"conclusion\": \"success\"}, \"eval-obs-only-object-norm005-seed50\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.13, \"total_rollouts\": 100, \"total_successes\": 13}}, \"eval-obs-only-object-norm01-seed54\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.15, \"total_rollouts\": 100, \"total_successes\": 15}}, \"eval-obs-only-object-norm01-seed53\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.19, \"total_rollouts\": 100, \"total_successes\": 19}}, \"eval-obs-only-object-norm003-seed46\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.15, \"total_rollouts\": 100, \"total_successes\": 15}}, \"eval-plan-a-spatial-seed43\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.35, \"total_rollouts\": 100, \"total_successes\": 35, \"mean_uncertainty\": 0.2619, \"trigger_rate\": 0.98}}, \"eval-plan-a-spatial-seed42\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.34, \"total_rollouts\": 100, \"total_successes\": 34, \"mean_uncertainty\": 0.2679, \"trigger_rate\": 0.976}}, \"eval-obs-only-object-norm005-seed49\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.15, \"total_rollouts\": 100, \"total_successes\": 15}}, \"eval-obs-only-object-norm01-seed52\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.15, \"total_rollouts\": 100, \"total_successes\": 15}}, \"eval-obs-only-object-norm01-seed51\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.11, \"total_rollouts\": 100, \"total_successes\": 11}}, \"eval-obs-only-object-norm005-seed55\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.15, \"total_rollouts\": 100, \"total_successes\": 15}}, \"eval-plan-a-spatial-seed44\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.36, \"sr_pct\": \"36.0%\", \"n_tasks\": 10, \"n_rollouts\": 10, \"total_rollouts\": 100, \"mean_uncertainty\": 0.2661, \"trigger_rate\": 0.978}}, \"eval-plan-a-object-seed43\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.16, \"sr_pct\": \"16.0%\", \"n_tasks\": 10, \"n_rollouts\": 10, \"total_rollouts\": 100, \"mean_uncertainty\": 0.1457, \"trigger_rate\": 0.84}}, \"eval-plan-a-object-seed44\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.2, \"sr_pct\": \"20.0%\", \"n_tasks\": 10, \"n_rollouts\": 10, \"total_rollouts\": 100, \"mean_uncertainty\": 0.1448, \"trigger_rate\": 0.832}}, \"eval-plan-a-object-seed42\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.19, \"sr_pct\": \"19.0%\", \"n_tasks\": 10, \"n_rollouts\": 10, \"total_rollouts\": 100, \"mean_uncertainty\": 0.1468, \"trigger_rate\": 0.838}}, \"eval-obs-only-object-norm003-seed44-r2\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.15, \"sr_pct\": \"15.0%\", \"n_tasks\": 10, \"n_rollouts\": 10, \"total_rollouts\": 100}}, \"eval-obs-only-object-norm005-seed47\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.13, \"sr_pct\": 13, \"n_tasks\": 10, \"n_rollouts\": 10, \"total_rollouts\": 100}}, \"eval-vla-only-object-seed50\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.09, \"sr_pct\": 9, \"n_tasks\": 10, \"n_rollouts\": 10, \"total_rollouts\": 100}}, \"eval-obs-only-object-norm005-seed48\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.13, \"sr_pct\": 13, \"n_tasks\": 10, \"n_rollouts\": 10, \"total_rollouts\": 100}}, \"eval-obs-only-object-norm02-seed52\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.15, \"sr_pct\": 15, \"n_tasks\": 10, \"n_rollouts\": 10, \"total_rollouts\": 100}}, \"eval-random-selection-object-seed49\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.12, \"sr_pct\": 12, \"n_tasks\": 10, \"n_rollouts\": 10, \"total_rollouts\": 100}}, \"eval-random-selection-object-seed48\": {\"status\": \"DONE\", \"metrics\": {\"success_rate\": 0.1, \"sr_pct\": \"10.0%\", \"n_tasks\": 10, \"n_rollouts\": 10, \"total_rollouts\": 100}, \"conclusion\": \"success\"}, \"eval-k20-obs-only-object-seed44\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.18, \"sr_pct\": 18, \"n_tasks\": 10, \"n_rollouts\": 10, \"total_rollouts\": 100}}, \"eval-k5-obs-only-object-seed44\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.14, \"sr_pct\": 14, \"n_tasks\": 10, \"n_rollouts\": 10, \"total_rollouts\": 100}}, \"eval-obs-only-object-norm02-seed53\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.16, \"sr_pct\": \"16.0%\", \"n_tasks\": 10, \"n_rollouts\": 10, \"total_rollouts\": 100}}, \"eval-obs-only-object-norm003-seed45\": {\"status\": \"DONE\", \"metrics\": {\"success_rate\": 0.15, \"sr_pct\": \"15.0%\", \"n_tasks\": 10, \"n_rollouts\": 10, \"total_rollouts\": 100}, \"conclusion\": \"success\"}, \"eval-obs-only-object-norm01-seed49\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.16, \"sr_pct\": \"16.0%\", \"n_tasks\": 10, \"n_rollouts\": 10, \"total_rollouts\": 100}}, \"eval-obs-only-spatial-norm02-seed52\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.33, \"sr_pct\": \"33.0%\", \"n_tasks\": 10, \"n_rollouts\": 10, \"total_rollouts\": 100}}, \"eval-obs-only-object-norm01-seed48\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.18, \"n_tasks\": 10, \"n_rollouts\": 10, \"total_rollouts\": 100}}, \"eval-obs-only-object-norm02-seed43-r3\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"sr\": 16}}, \"eval-obs-only-object-norm01-seed50\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.14, \"sr_pct\": \"14.0%\", \"n_tasks\": 10, \"n_rollouts\": 10, \"total_rollouts\": 100, \"per_task\": {\"alphabet_soup\": 0, \"cream_cheese\": 0, \"salad_dressing\": 0.2, \"bbq_sauce\": 0.3, \"ketchup\": 0, \"tomato_sauce\": 0, \"butter\": 0.1, \"milk\": 0.2, \"chocolate_pudding\": 0.3, \"orange_juice\": 0.3}}}, \"eval-obs-only-object-norm003-seed43\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.14, \"n_rollouts\": 100}}, \"eval-obs-only-object-norm02-seed51\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.17, \"n_rollouts\": 100}}, \"eval-obs-only-object-norm003-seed44\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 15, \"total_rollouts\": 100, \"per_task\": {\"alphabet_soup\": 0, \"cream_cheese\": 0, \"salad_dressing\": 30, \"bbq_sauce\": 20, \"ketchup\": 0, \"tomato_sauce\": 10, \"butter\": 10, \"milk\": 20, \"chocolate_pudding\": 30, \"orange_juice\": 30}}}, \"eval-obs-only-object-norm005-seed44\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 12, \"total_rollouts\": 100, \"per_task\": {\"alphabet_soup\": 0, \"cream_cheese\": 0, \"salad_dressing\": 0, \"bbq_sauce\": 30, \"ketchup\": 0, \"tomato_sauce\": 10, \"butter\": 10, \"milk\": 20, \"chocolate_pudding\": 20, \"orange_juice\": 30}}}, \"eval-random-selection-spatial-seed42-r3\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.34, \"successes\": 34, \"total_rollouts\": 100}}, \"eval-obs-only-spatial-norm02-seed50\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.35, \"successes\": 35, \"total_rollouts\": 100}}, \"train-crm-openvla-obs-only\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"best_val_loss\": 0.07726, \"final_train_loss\": 0.234989, \"epochs_completed\": 50}}, \"openvla-precompute-k1\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"total_files\": 74507, \"obs_dim\": 4096, \"cache_size_gb\": 6, \"multi_scale_layers\": [7, 15, 23, 31]}}, \"eval-random-selection-object-seed46-r3\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.1, \"tasks_evaluated\": 10, \"rollouts_per_task\": 10, \"total_rollouts\": 100, \"total_successes\": 10}}, \"eval-perdof-object-norm02-seed49\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.12, \"benchmark\": \"object\", \"mode\": \"crm_perdof\", \"seed\": 49, \"K\": 10, \"max_correction_norm\": 0.2}}, \"eval-random-selection-object-seed47\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"sr\": 7}}, \"eval-k20-obs-only-object-seed42\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"sr\": 20}}, \"eval-obs-only-spatial-norm02-seed42-r2\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"sr\": 33}}, \"eval-obs-only-object-norm005-seed43\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"sr\": 13, \"total\": 100, \"successes\": 13, \"benchmark\": \"object\", \"mode\": \"crm_obs_only\"}}, \"eval-k20-obs-only-object-seed43\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"sr\": 18}}, \"eval-k5-obs-only-object-seed43\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"sr\": 17}}, \"eval-random-selection-spatial-seed43-r2\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"sr\": 26}}, \"eval-random-selection-spatial-seed44\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.28, \"n_tasks\": 10, \"n_rollouts\": 10, \"total_rollouts\": 100}}, \"eval-crm-k1-object-seed43-plan702\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"sr\": 11, \"n_tasks\": 10, \"n_rollouts\": 10, \"total_rollouts\": 100}}, \"eval-crm-k1-object-seed42-plan702\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"sr\": 11, \"n_tasks\": 10, \"n_rollouts\": 10, \"total_rollouts\": 100}}, \"eval-crm-k1-object-seed44-plan702\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"sr\": 10, \"n_tasks\": 10, \"n_rollouts\": 10, \"total_rollouts\": 100}}, \"eval-random-selection-spatial-seed43\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.26, \"per_task_sr\": {\"between_plate_ramekin\": 0.7, \"next_to_ramekin\": 0.9, \"table_center\": 0, \"cookie_box\": 0.1, \"top_drawer\": 0, \"on_ramekin\": 0, \"next_to_cookie_box\": 0.7, \"stove\": 0, \"next_to_plate\": 0.2, \"wooden_cabinet\": 0}}}, \"eval-obs-only-spatial-seed48\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.35, \"benchmark\": \"spatial\", \"n_rollouts\": 10}}, \"eval-vla-only-spatial-seed48\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.3, \"benchmark\": \"spatial\", \"n_rollouts\": 10}}, \"eval-obs-only-spatial-norm02-seed49\": {\"status\": \"DONE\", \"metrics\": {\"sr\": 0.32, \"sr_pct\": \"32%\", \"total_rollouts\": 100, \"n_tasks\": 10, \"n_rollouts_per_task\": 10, \"per_task\": {\"between_plate_ramekin\": 0.9, \"next_to_ramekin\": 0.9, \"table_center\": 0, \"on_cookie_box\": 0.3, \"top_drawer_cabinet\": 0.1, \"on_ramekin\": 0, \"next_to_cookie_box\": 0.8, \"on_stove\": 0, \"next_to_plate\": 0.2, \"on_wooden_cabinet\": 0}}, \"conclusion\": \"success\"}, \"eval-adaptive-k-spatial-p90-seed44\": {\"status\": \"DONE\", \"metrics\": {\"success_rate\": 0.36, \"avg_K\": 3.56, \"fast_path_ratio\": 0.805, \"adaptive_trigger_rate\": 0.195, \"total_rollouts\": 100, \"successes\": 36, \"total_steps\": 23123, \"fast_steps\": 18615, \"full_steps\": 4508, \"threshold\": 0.12587, \"mean_l2_distance\": 0.09, \"per_task\": {\"between_plate_and_ramekin\": {\"sr\": 0.8, \"successes\": 8, \"total\": 10}, \"next_to_ramekin\": {\"sr\": 1, \"successes\": 10, \"total\": 10}, \"from_table_center\": {\"sr\": 0, \"successes\": 0, \"total\": 10}, \"on_cookie_box\": {\"sr\": 0.4, \"successes\": 4, \"total\": 10}, \"in_top_drawer\": {\"sr\": 0.1, \"successes\": 1, \"total\": 10}, \"on_ramekin\": {\"sr\": 0, \"successes\": 0, \"total\": 10}, \"next_to_cookie_box\": {\"sr\": 0.9, \"successes\": 9, \"total\": 10}, \"on_stove\": {\"sr\": 0, \"successes\": 0, \"total\": 10}, \"next_to_plate\": {\"sr\": 0.4, \"successes\": 4, \"total\": 10}, \"on_wooden_cabinet\": {\"sr\": 0, \"successes\": 0, \"total\": 10}}}, \"conclusion\": \"success\"}, \"eval-argmin-object-seed50\": {\"status\": \"DONE\", \"metrics\": {\"overall_sr\": 0.13, \"per_task_sr\": {\"alphabet_soup\": 0, \"cream_cheese\": 0, \"salad_dressing\": 0.1, \"bbq_sauce\": 0.4, \"ketchup\": 0, \"tomato_sauce\": 0, \"butter\": 0.1, \"milk\": 0.2, \"chocolate_pudding\": 0.3, \"orange_juice\": 0.2}, \"total_rollouts\": 100, \"total_successes\": 13, \"seed\": 50, \"benchmark\": \"object\", \"K\": 10, \"mode\": \"reconvla\"}, \"conclusion\": \"success\"}, \"eval-obs-only-object-norm02-seed50\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"sr\": 18, \"n_tasks\": 10, \"n_rollouts\": 10, \"total_rollouts\": 100}}, \"eval-vla-only-object-seed48-r2\": {\"status\": \"DONE\", \"metrics\": {\"success_rate\": 0.11, \"total_rollouts\": 100, \"successes\": 11, \"per_task\": {\"pick_up_the_alphabet_soup_and_place_it_in_the_basket\": 0, \"pick_up_the_cream_cheese_and_place_it_in_the_basket\": 0.1, \"pick_up_the_salad_dressing_and_place_it_in_the_basket\": 0.1, \"pick_up_the_bbq_sauce_and_place_it_in_the_basket\": 0.1, \"pick_up_the_ketchup_and_place_it_in_the_basket\": 0, \"pick_up_the_tomato_sauce_and_place_it_in_the_basket\": 0.1, \"pick_up_the_butter_and_place_it_in_the_basket\": 0, \"pick_up_the_milk_and_place_it_in_the_basket\": 0.1, \"pick_up_the_chocolate_pudding_and_place_it_in_the_basket\": 0.4, \"pick_up_the_orange_juice_and_place_it_in_the_basket\": 0.2}}, \"conclusion\": \"success\"}, \"eval-vla-only-goal-seed51\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"sr\": 69, \"n_tasks\": 10, \"n_rollouts\": 10, \"total_rollouts\": 100}}, \"eval-random-selection-spatial-seed42-r2\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"sr\": 34, \"n_tasks\": 10, \"n_rollouts\": 10, \"total_rollouts\": 100}}, \"eval-random-selection-object-seed45\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.1, \"n_tasks\": 10, \"n_rollouts\": 10, \"total_rollouts\": 100}}, \"eval-perdof-object-norm02-seed48\": {\"status\": \"DONE\", \"metrics\": {\"sr\": 0.07, \"total\": 100, \"successes\": 7, \"benchmark\": \"object\", \"mode\": \"crm_perdof\"}, \"conclusion\": \"success\"}, \"eval-argmin-object-k5-seed44-r2\": {\"status\": \"DONE\", \"metrics\": {\"sr\": 0.11, \"total\": 100, \"successes\": 11, \"benchmark\": \"object\", \"mode\": \"reconvla\"}, \"conclusion\": \"success\"}, \"eval-vla-only-goal-seed44-r2\": {\"status\": \"DONE\", \"metrics\": {\"sr\": 0.73, \"total\": 100, \"successes\": 73, \"benchmark\": \"goal\", \"mode\": \"vla_only\"}, \"conclusion\": \"success\"}, \"eval-obs-only-spatial-norm02-seed46-r2\": {\"status\": \"DONE\", \"metrics\": {\"sr\": 0.33, \"total\": 100, \"successes\": 33, \"benchmark\": \"spatial\", \"mode\": \"crm_obs_only\"}, \"conclusion\": \"success\"}, \"eval-latency-profiling-v1\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"pipeline_latency_ms\": 247, \"crm_latency_ms\": 0.27}}, \"eval-adaptive-k-spatial-p75-seed44\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"sr\": 33, \"avg_k\": 5.054, \"fast_path_pct\": 61.8, \"mean_l2\": 0.092, \"total_rollouts\": 100, \"threshold\": 0.098735}}, \"eval-obs-only-goal-norm02-seed51\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"sr\": 66, \"total_rollouts\": 100, \"per_task_sr\": {\"open_middle_drawer\": 40, \"put_bowl_on_stove\": 90, \"put_wine_bottle_on_cabinet\": 50, \"open_top_drawer_put_bowl\": 40, \"put_bowl_on_cabinet\": 80, \"push_plate_to_stove\": 90, \"put_cream_cheese_in_bowl\": 20, \"turn_on_stove\": 100, \"put_bowl_on_plate\": 100, \"put_wine_bottle_on_rack\": 50}}}, \"eval-adaptive-k-spatial-p25-seed44\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"sr\": 32, \"avg_k\": 7.693, \"fast_path_pct\": 28.8, \"mean_l2\": 0.0896, \"total_rollouts\": 100, \"per_task_sr\": {\"between_plate_and_ramekin\": 70, \"next_to_ramekin\": 100, \"from_table_center\": 0, \"on_cookie_box\": 40, \"in_top_drawer\": 10, \"on_ramekin\": 0, \"next_to_cookie_box\": 80, \"on_stove\": 0, \"next_to_plate\": 20, \"on_wooden_cabinet\": 0}}}, \"eval-argmin-object-seed49\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"overall_sr\": 0.16, \"total_successes\": 16, \"total_rollouts\": 100, \"seed\": 49, \"benchmark\": \"LIBERO-Object\", \"K\": 10, \"mode\": \"reconvla (argmin baseline)\", \"per_task_sr\": {\"pick_up_the_alphabet_soup_and_place_it_in_the_basket\": 0, \"pick_up_the_cream_cheese_and_place_it_in_the_basket\": 0, \"pick_up_the_salad_dressing_and_place_it_in_the_basket\": 0.2, \"pick_up_the_bbq_sauce_and_place_it_in_the_basket\": 0.4, \"pick_up_the_ketchup_and_place_it_in_the_basket\": 0, \"pick_up_the_tomato_sauce_and_place_it_in_the_basket\": 0.1, \"pick_up_the_butter_and_place_it_in_the_basket\": 0.1, \"pick_up_the_milk_and_place_it_in_the_basket\": 0.3, \"pick_up_the_chocolate_pudding_and_place_it_in_the_basket\": 0.3, \"pick_up_the_orange_juice_and_place_it_in_the_basket\": 0.2}}}, \"eval-vla-only-object-seed48\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.1, \"n_episodes\": 100}}, \"eval-argmin-object-seed48\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.15, \"per_task\": {\"alphabet_soup\": 0, \"cream_cheese\": 0, \"salad_dressing\": 0.2, \"bbq_sauce\": 0.3, \"ketchup\": 0, \"tomato_sauce\": 0.1, \"butter\": 0.1, \"milk\": 0.2, \"chocolate_pudding\": 0.4, \"orange_juice\": 0.2}}}, \"eval-obs-only-spatial-norm02-seed48\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.35, \"per_task\": {\"between_plate_and_ramekin\": 0.8, \"next_to_ramekin\": 1, \"from_table_center\": 0, \"on_cookie_box\": 0.3, \"in_top_drawer\": 0.1, \"on_ramekin\": 0, \"next_to_cookie_box\": 0.9, \"on_stove\": 0, \"next_to_plate\": 0.4, \"on_wooden_cabinet\": 0}}}, \"eval-obs-only-goal-norm02-seed52\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.68, \"per_task\": {\"open_middle_drawer\": 0.7, \"bowl_on_stove\": 0.9, \"wine_on_cabinet\": 0.4, \"bowl_in_drawer\": 0.3, \"bowl_on_cabinet\": 0.8, \"plate_to_stove\": 0.8, \"cream_cheese_in_bowl\": 0.4, \"turn_on_stove\": 1, \"bowl_on_plate\": 1, \"wine_on_rack\": 0.5}}}, \"eval-adaptive-k-spatial-p90-seed43\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.32, \"avg_K\": 3.586, \"fast_path_pct\": 80.17, \"mean_l2\": 0.0905, \"adaptive_trigger_rate\": 0.198, \"threshold\": 0.12587, \"total_steps\": 23797, \"fast_steps\": 19079, \"full_steps\": 4718}}, \"eval-perdof-object-norm02-seed45-r3\": {\"status\": \"DONE\", \"metrics\": {\"overall_success_rate\": 0.12, \"per_task_sr\": {\"alphabet_soup\": 0, \"cream_cheese\": 0, \"salad_dressing\": 0.1, \"bbq_sauce\": 0.1, \"ketchup\": 0, \"tomato_sauce\": 0.1, \"butter\": 0.2, \"milk\": 0, \"chocolate_pudding\": 0.4, \"orange_juice\": 0.3}}, \"conclusion\": \"success\"}, \"eval-adaptive-k-spatial-p90-seed42\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.31, \"avg_K\": 3.5, \"fast_path_pct\": 80.6, \"mean_l2\": 0.0907, \"threshold\": 0.12587, \"total_rollouts\": 100, \"total_successes\": 31, \"per_task\": {\"between_plate_and_ramekin\": 0.6, \"next_to_ramekin\": 1, \"from_table_center\": 0, \"on_cookie_box\": 0.3, \"in_top_drawer\": 0, \"on_ramekin\": 0, \"next_to_cookie_box\": 0.9, \"on_stove\": 0, \"next_to_plate\": 0.3, \"on_wooden_cabinet\": 0}}}, \"eval-obs-only-object-norm02-seed49\": {\"status\": \"DONE\", \"metrics\": {\"overall_success_rate\": 0.14, \"total_rollouts\": 100, \"total_successes\": 14, \"per_task\": {\"alphabet_soup\": 0, \"cream_cheese\": 0.1, \"salad_dressing\": 0.2, \"bbq_sauce\": 0.2, \"ketchup\": 0, \"tomato_sauce\": 0.1, \"butter\": 0.1, \"milk\": 0.1, \"chocolate_pudding\": 0.3, \"orange_juice\": 0.3}, \"updated_aggregate\": {\"mean_sr\": 16.4, \"std_sr\": 2, \"n_seeds\": 7, \"prior\": \"16.8±1.8% (n=6)\", \"delta_vs_vla_baseline\": \"+5.5pp\"}}, \"conclusion\": \"success\"}, \"eval-adaptive-k-spatial-p50-seed44\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"sr\": 0.33, \"avg_K\": 6.4, \"fast_path_ratio\": 0.45, \"adaptive_trigger_rate\": 0.55, \"threshold\": 0.074855}}, \"eval-adaptive-k-spatial-p50-seed43\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"sr\": 0.33, \"avg_K\": 6.33, \"fast_path_ratio\": 0.458, \"adaptive_trigger_rate\": 0.542, \"threshold\": 0.074855}}, \"eval-adaptive-k-spatial-p50-seed42\": {\"status\": \"DONE\", \"metrics\": {\"sr\": 30, \"avg_K\": 6.324, \"fast_path_pct\": 45.95, \"mean_l2\": 0.0903, \"total_rollouts\": 100}, \"conclusion\": \"success\"}, \"eval-adaptive-k-spatial-p25-seed43\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"sr\": 30, \"avg_k\": 7.6, \"fast_path_pct\": 29.5, \"mean_l2\": 0.089, \"total_rollouts\": 100, \"per_task_sr\": {\"between_plate_and_ramekin\": 60, \"next_to_ramekin\": 100, \"from_table_center\": 0, \"on_cookie_box\": 30, \"in_top_drawer\": 10, \"on_ramekin\": 0, \"next_to_cookie_box\": 80, \"on_stove\": 0, \"next_to_plate\": 20, \"on_wooden_cabinet\": 0}}}, \"eval-crm-object-k20-seed44\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"sr\": 18, \"total_rollouts\": 100, \"total_successes\": 18, \"per_task_sr\": {\"alphabet_soup\": 0, \"cream_cheese\": 0, \"salad_dressing\": 30, \"bbq_sauce\": 30, \"ketchup\": 0, \"tomato_sauce\": 10, \"butter\": 10, \"milk\": 30, \"chocolate_pudding\": 40, \"orange_juice\": 30}}}, \"eval-obs-only-object-norm003-seed43-r2\": {\"status\": \"DONE\", \"metrics\": {\"success_rate\": 14, \"total_rollouts\": 100, \"per_task\": {\"alphabet_soup\": 0, \"cream_cheese\": 0, \"salad_dressing\": 20, \"bbq_sauce\": 30, \"ketchup\": 0, \"tomato_sauce\": 10, \"butter\": 10, \"milk\": 20, \"chocolate_pudding\": 20, \"orange_juice\": 30}}, \"conclusion\": \"success\"}, \"eval-adaptive-k-spatial-p75-seed43\": {\"status\": \"DONE\", \"metrics\": {\"success_rate\": 34, \"total_rollouts\": 100, \"adaptive_stats\": {\"fast_path_pct\": 62.2, \"avg_k\": 5, \"mean_l2\": 0.0911}, \"per_task\": {\"bowl_between_plate_ramekin\": 80, \"bowl_next_to_ramekin\": 100, \"bowl_from_table_center\": 0, \"bowl_on_cookie_box\": 40, \"bowl_in_top_drawer\": 0, \"bowl_on_ramekin\": 0, \"bowl_next_to_cookie_box\": 90, \"bowl_on_stove\": 0, \"bowl_next_to_plate\": 30, \"bowl_on_wooden_cabinet\": 0}}, \"conclusion\": \"success\"}, \"eval-crm-object-k20-seed43\": {\"status\": \"DONE\", \"metrics\": {\"overall_success_rate\": 0.18, \"total_successes\": 18, \"total_rollouts\": 100, \"n_tasks\": 10, \"n_rollouts_per_task\": 10, \"per_task\": {\"alphabet_soup\": 0, \"cream_cheese\": 0, \"salad_dressing\": 0.3, \"bbq_sauce\": 0.3, \"ketchup\": 0, \"tomato_sauce\": 0.1, \"butter\": 0.1, \"milk\": 0.2, \"chocolate_pudding\": 0.5, \"orange_juice\": 0.3}, \"comparison\": {\"k10_reference\": \"16.8±1.8%\", \"k20_this\": \"18.0%\", \"delta\": \"+1.2pp\", \"note\": \"within K=10 error bars, marginal improvement\"}}, \"conclusion\": \"success\"}, \"eval-vla-only-long-seed49-r2\": {\"status\": \"DONE\", \"metrics\": {\"sr\": 0.16, \"per_task\": {\"LIVING_ROOM_SCENE2_alphabet_soup_tomato_sauce\": 0, \"LIVING_ROOM_SCENE2_cream_cheese_butter\": 0, \"KITCHEN_SCENE3_stove_moka_pot\": 0.9, \"KITCHEN_SCENE4_black_bowl_drawer\": 0, \"LIVING_ROOM_SCENE5_mugs_plates\": 0.3, \"STUDY_SCENE1_book_caddy\": 0.1, \"LIVING_ROOM_SCENE6_mug_pudding\": 0.2, \"LIVING_ROOM_SCENE1_soup_cream_cheese\": 0, \"KITCHEN_SCENE8_both_moka_pots\": 0, \"KITCHEN_SCENE6_mug_microwave\": 0.1}}, \"conclusion\": \"success\"}, \"eval-adaptive-k-spatial-p75-seed42\": {\"status\": \"DONE\", \"metrics\": {\"sr\": 0.31, \"avg_k\": 5.02, \"fast_path_ratio\": 0.622, \"mean_l2\": 0.0909, \"adaptive_trigger_rate\": 0.378, \"total_steps\": 23914, \"fast_steps\": 14875, \"full_steps\": 9039}, \"conclusion\": \"success\"}, \"eval-crm-object-k20-seed42\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"sr\": 20, \"per_task\": {\"alphabet_soup\": 0, \"cream_cheese\": 10, \"salad_dressing\": 30, \"bbq_sauce\": 40, \"ketchup\": 10, \"tomato_sauce\": 10, \"butter\": 10, \"milk\": 10, \"chocolate_pudding\": 50, \"orange_juice\": 30}}}, \"eval-adaptive-k-spatial-p50-seed44-r2\": {\"status\": \"DONE\", \"metrics\": {\"overall_success_rate\": 0.33, \"per_task_sr\": {\"between_plate_and_ramekin\": 0.6, \"next_to_ramekin\": 1, \"from_table_center\": 0, \"on_cookie_box\": 0.3, \"in_top_drawer\": 0.1, \"on_ramekin\": 0, \"next_to_cookie_box\": 0.9, \"on_stove\": 0, \"next_to_plate\": 0.4, \"on_wooden_cabinet\": 0}, \"avg_k\": 6.4, \"fast_path_ratio\": 0.45, \"adaptive_trigger_rate\": 0.55, \"mean_l2_distance\": 0.0923, \"total_steps\": 23661, \"fast_steps\": 10649, \"full_steps\": 13012, \"threshold\": 0.074855, \"total_rollouts\": 100}, \"conclusion\": \"success\"}, \"eval-adaptive-k-p75-seed42\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.12, \"avg_actual_k\": 3.07, \"fast_path_ratio\": 0.866}}, \"eval-adaptive-k-p75-seed43\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.13, \"avg_actual_k\": 3.15, \"fast_path_ratio\": 0.856}}, \"eval-adaptive-k-p50-seed42\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.16, \"avg_actual_k\": 3.72, \"fast_path_ratio\": 0.785}}, \"eval-adaptive-k-p50-seed43\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.16, \"avg_actual_k\": 3.81, \"fast_path_ratio\": 0.7737, \"total_steps\": 27813, \"fast_steps\": 21520, \"full_steps\": 6293}}, \"eval-random-selection-object-seed42\": {\"status\": \"DONE\", \"metrics\": {\"success_rate\": 0.11, \"n_tasks\": 10, \"n_rollouts\": 10, \"total_rollouts\": 100, \"per_task_sr\": [0, 0.1, 0.1, 0.1, 0, 0.1, 0.1, 0.1, 0.2, 0.3]}, \"conclusion\": \"success\"}, \"eval-adaptive-k-spatial-p50-seed43-r2\": {\"status\": \"DONE\", \"metrics\": {\"overall_success_rate\": 0.33, \"per_task_sr\": {\"between_plate_and_ramekin\": 0.8, \"next_to_ramekin\": 1, \"from_table_center\": 0, \"on_cookie_box\": 0.4, \"in_top_drawer\": 0.1, \"on_ramekin\": 0, \"next_to_cookie_box\": 0.9, \"on_stove\": 0, \"next_to_plate\": 0.1, \"on_wooden_cabinet\": 0}, \"avg_k\": 6.33, \"fast_path_ratio\": 0.458, \"adaptive_trigger_rate\": 0.542, \"mean_l2_distance\": 0.0903, \"total_steps\": 23414, \"fast_steps\": 10728, \"full_steps\": 12686, \"threshold\": 0.074855, \"total_rollouts\": 100}, \"conclusion\": \"success\"}, \"eval-random-selection-object-seed44\": {\"status\": \"DONE\", \"metrics\": {\"overall_success_rate\": 0.11, \"n_tasks\": 10, \"n_rollouts\": 10, \"total_rollouts\": 100, \"per_task_sr\": {\"alphabet_soup\": 0, \"cream_cheese\": 0.1, \"salad_dressing\": 0.2, \"bbq_sauce\": 0.2, \"ketchup\": 0, \"tomato_sauce\": 0.1, \"butter\": 0.1, \"milk\": 0.1, \"chocolate_pudding\": 0.2, \"orange_juice\": 0.1}}, \"conclusion\": \"success\"}, \"eval-obs-only-object-norm02-seed42\": {\"status\": \"DONE\", \"metrics\": {\"overall_success_rate\": 0.2, \"total_episodes\": 100, \"total_successes\": 20, \"per_task\": {\"alphabet_soup\": 0, \"cream_cheese\": 0.1, \"salad_dressing\": 0.4, \"bbq_sauce\": 0.4, \"ketchup\": 0, \"tomato_sauce\": 0.1, \"butter\": 0.2, \"milk\": 0.3, \"chocolate_pudding\": 0.2, \"orange_juice\": 0.3}}, \"conclusion\": \"success\"}, \"latency-profile-n1000\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"vla_e2e_K1_ms\": 256.5, \"vla_e2e_K10_ms\": 253.2, \"crm_forward_ms\": 0.28, \"cgs_features_ms\": 5.75, \"full_pipeline_K10_ms\": 249, \"adaptive_fast_path_ms\": 252.9, \"adaptive_full_path_ms\": 459.6, \"crm_overhead_vs_vla_K10_ms\": -4.2, \"crm_overhead_pct\": -1.66, \"adaptive_speedup_ratio\": 1.82, \"argmin_l2_K10_ms\": 0.06, \"gpu_mem_mb\": 903, \"n_measure\": 1000, \"gpu_model\": \"RTX 4090\"}}, \"eval-adaptive-k-p90-seed44\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.14, \"avg_actual_k\": 2.58, \"fast_path_ratio\": 0.928}}, \"eval-adaptive-k-p25-seed43\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.13, \"avg_actual_k\": 4.788, \"fast_path_ratio\": 0.6515, \"total_steps\": 28207, \"fast_steps\": 18377, \"full_steps\": 9830}}, \"eval-crm-spatial-k10-seed51\": {\"status\": \"DONE\", \"metrics\": {\"success_rate\": 0.36, \"n_tasks\": 10, \"n_rollouts\": 10, \"total\": 100}, \"conclusion\": \"success\"}, \"eval-vla-only-goal-seed49\": {\"status\": \"DONE\", \"metrics\": {\"success_rate\": 0.65, \"n_tasks\": 10, \"n_rollouts\": 10, \"total\": 100}, \"conclusion\": \"success\"}, \"eval-vla-only-long-seed52\": {\"status\": \"DONE\", \"metrics\": {\"success_rate\": 0.17, \"n_tasks\": 10, \"n_rollouts\": 10, \"total\": 100}, \"conclusion\": \"success\"}, \"eval-vla-only-long-seed51\": {\"status\": \"DONE\", \"metrics\": {\"success_rate\": 0.15, \"n_tasks\": 10, \"n_rollouts\": 10, \"total\": 100}, \"conclusion\": \"success\"}, \"eval-vla-only-long-seed50\": {\"status\": \"DONE\", \"metrics\": {\"success_rate\": 0.16, \"n_tasks\": 10, \"n_rollouts\": 10, \"total\": 100}, \"conclusion\": \"success\"}, \"eval-crm-long-seed50\": {\"status\": \"DONE\", \"metrics\": {\"success_rate\": 0.14, \"n_tasks\": 10, \"n_rollouts\": 10, \"total\": 100}, \"conclusion\": \"success\"}, \"eval-adaptive-k-p25-seed44-r2\": {\"status\": \"DONE\", \"metrics\": {\"success_rate\": 0.15, \"avg_actual_k\": 4.736, \"fast_path_ratio\": 0.658, \"adaptive_trigger_rate\": 0.342, \"total_steps\": 27889, \"fast_steps\": 18351, \"full_steps\": 9538}, \"conclusion\": \"success\"}, \"eval-adaptive-k-p25-seed42\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.15, \"avg_actual_k\": 4.8, \"fast_path_ratio\": 0.65}}, \"eval-crm-goal-seed46\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.72, \"n_tasks\": 10, \"n_rollouts\": 10, \"total_episodes\": 100, \"per_task\": {\"open_the_middle_drawer_of_the_cabinet\": 0.7, \"put_the_bowl_on_the_stove\": 0.9, \"put_the_wine_bottle_on_top_of_the_cabinet\": 0.5, \"open_the_top_drawer_and_put_the_bowl_inside\": 0.5, \"put_the_bowl_on_top_of_the_cabinet\": 0.9, \"push_the_plate_to_the_front_of_the_stove\": 1, \"put_the_cream_cheese_in_the_bowl\": 0.4, \"turn_on_the_stove\": 1, \"put_the_bowl_on_the_plate\": 1, \"put_the_wine_bottle_on_the_rack\": 0.3}}}, \"eval-adaptive-k-p50-seed44\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.14, \"avg_actual_k\": 3.909, \"fast_path_ratio\": 0.761, \"total_steps\": 28067, \"fast_steps\": 21368, \"full_steps\": 6699}}, \"eval-adaptive-k-p75-seed44\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.16, \"avg_actual_k\": 3.022, \"fast_path_ratio\": 0.872, \"total_steps\": 27724, \"fast_steps\": 24181, \"full_steps\": 3543}}, \"eval-adaptive-k-p90-seed43\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.14, \"avg_actual_k\": 2.612, \"fast_path_ratio\": 0.923, \"total_steps\": 27935, \"fast_steps\": 25797, \"full_steps\": 2138}}, \"eval-adaptive-k-p90-seed42\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.12, \"avg_actual_k\": 2.672, \"fast_path_ratio\": 0.916, \"total_steps\": 28258, \"fast_steps\": 25886, \"full_steps\": 2372}}, \"eval-vla-only-spatial-seed47\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.3, \"n_tasks\": 10, \"n_rollouts\": 10, \"total_episodes\": 100, \"successful_rollouts\": 30}}, \"eval-crm-long-seed47\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.17, \"n_episodes\": 100, \"per_task\": {\"KITCHEN_SCENE3_turn_on_stove_put_moka_pot\": 0.8, \"KITCHEN_SCENE6_mug_in_microwave_close\": 0.5, \"LIVING_ROOM_SCENE5_mugs_on_plates\": 0.2, \"STUDY_SCENE1_book_in_caddy\": 0.2, \"LIVING_ROOM_SCENE2_soup_sauce_basket\": 0, \"LIVING_ROOM_SCENE2_cheese_butter_basket\": 0, \"KITCHEN_SCENE4_bowl_in_drawer\": 0, \"LIVING_ROOM_SCENE6_mug_pudding\": 0, \"LIVING_ROOM_SCENE1_soup_cheese_basket\": 0, \"KITCHEN_SCENE8_both_moka_pots\": 0}}}, \"eval-vla-only-long-seed48\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.14, \"n_episodes\": 100, \"per_task\": {\"KITCHEN_SCENE3_turn_on_stove_put_moka_pot\": 0.8, \"LIVING_ROOM_SCENE5_white_mug_left_yellow_right\": 0.3, \"STUDY_SCENE1_book_in_back_compartment\": 0.1, \"LIVING_ROOM_SCENE6_white_mug_pudding\": 0.1, \"KITCHEN_SCENE6_mug_in_microwave_close\": 0.1, \"LIVING_ROOM_SCENE2_alphabet_soup_tomato_sauce\": 0, \"LIVING_ROOM_SCENE2_cream_cheese_butter\": 0, \"KITCHEN_SCENE4_black_bowl_in_drawer\": 0, \"LIVING_ROOM_SCENE1_alphabet_soup_cream_cheese\": 0, \"KITCHEN_SCENE8_both_moka_pots\": 0}}}, \"eval-crm-long-seed46\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.18, \"n_episodes\": 100, \"per_task\": {\"KITCHEN_SCENE3_turn_on_stove_put_moka_pot\": 0.9, \"KITCHEN_SCENE6_mug_in_microwave_close\": 0.5, \"LIVING_ROOM_SCENE5_white_mug_left_yellow_right\": 0.2, \"STUDY_SCENE1_book_in_back_compartment\": 0.2, \"LIVING_ROOM_SCENE2_alphabet_soup_tomato_sauce\": 0, \"LIVING_ROOM_SCENE2_cream_cheese_butter\": 0, \"KITCHEN_SCENE4_black_bowl_in_drawer\": 0, \"LIVING_ROOM_SCENE6_white_mug_pudding\": 0, \"LIVING_ROOM_SCENE1_alphabet_soup_cream_cheese\": 0, \"KITCHEN_SCENE8_both_moka_pots\": 0}}}, \"eval-crm-goal-seed45-r2\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.65, \"n_episodes\": 100, \"per_task\": {\"turn_on_the_stove\": 1, \"put_the_bowl_on_the_plate\": 1, \"push_the_plate_to_the_front_of_the_stove\": 0.9, \"put_the_bowl_on_the_stove\": 0.9, \"put_the_bowl_on_top_of_the_cabinet\": 0.8, \"open_the_middle_drawer_of_the_cabinet\": 0.7, \"put_the_wine_bottle_on_top_of_the_cabinet\": 0.4, \"put_the_wine_bottle_on_the_rack\": 0.4, \"open_the_top_drawer_and_put_the_bowl_inside\": 0.2, \"put_the_cream_cheese_in_the_bowl\": 0.2}}}, \"eval-crm-goal-seed44-r2\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.64, \"n_episodes\": 100, \"per_task\": {\"turn_on_the_stove\": 1, \"put_the_bowl_on_the_plate\": 1, \"put_the_bowl_on_the_stove\": 0.9, \"push_the_plate_to_the_front_of_the_stove\": 0.8, \"put_the_bowl_on_top_of_the_cabinet\": 0.7, \"open_the_middle_drawer_of_the_cabinet\": 0.6, \"put_the_wine_bottle_on_top_of_the_cabinet\": 0.5, \"put_the_wine_bottle_on_the_rack\": 0.4, \"put_the_cream_cheese_in_the_bowl\": 0.3, \"open_the_top_drawer_and_put_the_bowl_inside\": 0.2}}}, \"eval-obs-only-spatial-norm02-seed43-r2\": {\"status\": \"DONE\", \"metrics\": {\"overall_success_rate\": 0.34, \"n_tasks\": 10, \"n_rollouts\": 10, \"per_task\": {\"between_plate_and_ramekin\": 0.9, \"next_to_ramekin\": 1, \"from_table_center\": 0, \"on_cookie_box\": 0.3, \"in_top_drawer\": 0, \"on_ramekin\": 0, \"next_to_cookie_box\": 1, \"on_stove\": 0, \"next_to_plate\": 0.2, \"on_wooden_cabinet\": 0}}, \"conclusion\": \"success\"}, \"k2-l2-calibration-phase1\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"k2l2_vs_k10var_rho\": 0.9979, \"k2l2_vs_k10var_pvalue\": 0, \"k2l2_vs_fmvd_rho\": 0.0925, \"k2l2_vs_fmvd_pvalue\": 6.03e-29, \"k10var_vs_fmvd_rho\": 0.0825, \"k10var_vs_fmvd_pvalue\": 2.33e-23, \"n_samples\": 14512, \"k2l2_mean\": 0.0807, \"k2l2_std\": 0.0361, \"go_nogo_k2_proxy\": \"GO (rho=0.9979)\", \"go_nogo_fmvd_signal\": \"NO-GO (rho=0.09)\"}}, \"eval-crm-long-seed45\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.18, \"n_tasks\": 10, \"n_rollouts\": 10, \"total_episodes\": 100, \"total_successes\": 18}}, \"eval-vla-only-goal-seed43\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.69, \"per_task\": {\"open_the_middle_drawer_of_the_cabinet\": 0.9, \"put_the_bowl_on_the_stove\": 0.9, \"put_the_wine_bottle_on_top_of_the_cabinet\": 0.4, \"open_the_top_drawer_and_put_the_bowl_inside\": 0.5, \"put_the_bowl_on_top_of_the_cabinet\": 0.5, \"push_the_plate_to_the_front_of_the_stove\": 0.8, \"put_the_cream_cheese_in_the_bowl\": 0.4, \"turn_on_the_stove\": 0.9, \"put_the_bowl_on_the_plate\": 1, \"put_the_wine_bottle_on_the_rack\": 0.6}}}, \"eval-vla-only-goal-seed42\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.71, \"per_task\": {\"open_the_middle_drawer_of_the_cabinet\": 0.9, \"put_the_bowl_on_the_stove\": 0.9, \"put_the_wine_bottle_on_top_of_the_cabinet\": 0.6, \"open_the_top_drawer_and_put_the_bowl_inside\": 0.4, \"put_the_bowl_on_top_of_the_cabinet\": 0.7, \"push_the_plate_to_the_front_of_the_stove\": 0.9, \"put_the_cream_cheese_in_the_bowl\": 0.2, \"turn_on_the_stove\": 0.9, \"put_the_bowl_on_the_plate\": 0.9, \"put_the_wine_bottle_on_the_rack\": 0.7}}}, \"eval-vla-only-object-seed47\": {\"status\": \"DONE\", \"metrics\": {\"overall_success_rate\": 0.1, \"n_tasks\": 10, \"n_rollouts\": 10, \"total_episodes\": 100, \"per_task\": {\"salad_dressing\": 0.2, \"bbq_sauce\": 0.2, \"milk\": 0.2, \"chocolate_pudding\": 0.2, \"orange_juice\": 0.2, \"alphabet_soup\": 0, \"cream_cheese\": 0, \"ketchup\": 0, \"tomato_sauce\": 0, \"butter\": 0}}, \"conclusion\": \"success\"}, \"eval-crm-long-seed44\": {\"status\": \"DONE\", \"metrics\": {\"overall_success_rate\": 0.2, \"n_tasks\": 10, \"n_rollouts\": 10, \"total_episodes\": 100, \"per_task\": {\"KITCHEN_SCENE3_stove_moka_pot\": 0.8, \"KITCHEN_SCENE6_mug_microwave\": 0.6, \"LIVING_ROOM_SCENE5_mugs_plates\": 0.3, \"STUDY_SCENE1_book_caddy\": 0.2, \"LIVING_ROOM_SCENE6_mug_plate_pudding\": 0.1, \"LIVING_ROOM_SCENE2_alphabet_soup_tomato_sauce\": 0, \"LIVING_ROOM_SCENE2_cream_cheese_butter\": 0, \"KITCHEN_SCENE4_black_bowl_drawer\": 0, \"LIVING_ROOM_SCENE1_alphabet_soup_cream_cheese\": 0, \"KITCHEN_SCENE8_both_moka_pots\": 0}}, \"conclusion\": \"success\"}, \"eval-crm-long-seed43\": {\"status\": \"DONE\", \"metrics\": {\"overall_success_rate\": 0.15, \"n_tasks\": 10, \"n_rollouts\": 10, \"total_episodes\": 100, \"per_task\": {\"KITCHEN_SCENE3_stove_moka_pot\": 0.8, \"KITCHEN_SCENE6_mug_microwave\": 0.3, \"LIVING_ROOM_SCENE5_mugs_plates\": 0.2, \"STUDY_SCENE1_book_caddy\": 0.2, \"LIVING_ROOM_SCENE2_alphabet_soup_tomato_sauce\": 0, \"LIVING_ROOM_SCENE2_cream_cheese_butter\": 0, \"KITCHEN_SCENE4_black_bowl_drawer\": 0, \"LIVING_ROOM_SCENE6_mug_plate_pudding\": 0, \"LIVING_ROOM_SCENE1_alphabet_soup_cream_cheese\": 0, \"KITCHEN_SCENE8_both_moka_pots\": 0}}, \"conclusion\": \"success\"}, \"eval-crm-long-seed42\": {\"status\": \"DONE\", \"metrics\": {\"overall_success_rate\": 0.17, \"n_tasks\": 10, \"n_rollouts\": 10, \"total_episodes\": 100, \"per_task\": {\"KITCHEN_SCENE3_stove_moka_pot\": 0.8, \"KITCHEN_SCENE6_mug_microwave\": 0.4, \"LIVING_ROOM_SCENE5_mugs_plates\": 0.2, \"STUDY_SCENE1_book_caddy\": 0.2, \"LIVING_ROOM_SCENE6_mug_plate_pudding\": 0.1, \"LIVING_ROOM_SCENE2_alphabet_soup_tomato_sauce\": 0, \"LIVING_ROOM_SCENE2_cream_cheese_butter\": 0, \"KITCHEN_SCENE4_black_bowl_drawer\": 0, \"LIVING_ROOM_SCENE1_alphabet_soup_cream_cheese\": 0, \"KITCHEN_SCENE8_both_moka_pots\": 0}}, \"conclusion\": \"success\"}, \"eval-crm-goal-seed42\": {\"status\": \"DONE\", \"metrics\": {\"overall_success_rate\": 0.67, \"n_tasks\": 10, \"n_rollouts\": 10, \"total_episodes\": 100, \"per_task\": {\"open_the_middle_drawer_of_the_cabinet\": 0.8, \"put_the_bowl_on_the_stove\": 0.9, \"put_the_wine_bottle_on_top_of_the_cabinet\": 0.4, \"open_the_top_drawer_and_put_the_bowl_inside\": 0.2, \"put_the_bowl_on_top_of_the_cabinet\": 1, \"push_the_plate_to_the_front_of_the_stove\": 0.9, \"put_the_cream_cheese_in_the_bowl\": 0.2, \"turn_on_the_stove\": 1, \"put_the_bowl_on_the_plate\": 0.9, \"put_the_wine_bottle_on_the_rack\": 0.4}}, \"conclusion\": \"success\"}, \"eval-crm-goal-seed43\": {\"status\": \"DONE\", \"metrics\": {\"overall_success_rate\": 0.72, \"n_tasks\": 10, \"n_rollouts\": 10, \"total_episodes\": 100, \"per_task\": {\"open_the_middle_drawer_of_the_cabinet\": 0.8, \"put_the_bowl_on_the_stove\": 0.9, \"put_the_wine_bottle_on_top_of_the_cabinet\": 0.6, \"open_the_top_drawer_and_put_the_bowl_inside\": 0.5, \"put_the_bowl_on_top_of_the_cabinet\": 0.9, \"push_the_plate_to_the_front_of_the_stove\": 0.8, \"put_the_cream_cheese_in_the_bowl\": 0.3, \"turn_on_the_stove\": 1, \"put_the_bowl_on_the_plate\": 1, \"put_the_wine_bottle_on_the_rack\": 0.4}}, \"conclusion\": \"success\"}, \"eval-vla-only-spatial-seed46\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.3, \"n_tasks\": 10, \"n_rollouts\": 10, \"total_episodes\": 100, \"successful_rollouts\": 30}}, \"eval-vla-only-long-seed47\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.14, \"n_tasks\": 10, \"n_rollouts\": 100, \"successful_rollouts\": 14, \"per_task\": {\"put_both_alphabet_soup_and_tomato_sauce_in_basket\": 0, \"put_both_cream_cheese_box_and_butter_in_basket\": 0, \"turn_on_stove_put_moka_pot\": 0.8, \"put_black_bowl_in_bottom_drawer\": 0, \"put_white_mug_left_plate_yellow_mug_right_plate\": 0.4, \"pick_up_book_place_in_caddy\": 0.1, \"put_white_mug_on_plate_chocolate_pudding_right\": 0.1, \"put_both_alphabet_soup_and_cream_cheese_in_basket\": 0, \"put_both_moka_pots_on_stove\": 0, \"put_yellow_white_mug_in_microwave\": 0}}}, \"eval-vla-only-goal-seed45\": {\"status\": \"DONE\", \"metrics\": {\"overall_success_rate\": 0.63, \"n_tasks\": 10, \"n_rollouts\": 10, \"total_episodes\": 100, \"per_task\": {\"open_the_middle_drawer_of_the_cabinet\": 0.9, \"put_the_bowl_on_the_stove\": 0.9, \"put_the_wine_bottle_on_top_of_the_cabinet\": 0.3, \"open_the_top_drawer_and_put_the_bowl_inside\": 0.4, \"put_the_bowl_on_top_of_the_cabinet\": 0.3, \"push_the_plate_to_the_front_of_the_stove\": 0.9, \"put_the_cream_cheese_in_the_bowl\": 0.1, \"turn_on_the_stove\": 0.8, \"put_the_bowl_on_the_plate\": 0.9, \"put_the_wine_bottle_on_the_rack\": 0.8}}, \"conclusion\": \"success\"}, \"eval-vla-only-goal-seed46\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.71, \"n_tasks\": 10, \"n_rollouts_per_task\": 10, \"total_rollouts\": 100, \"total_successes\": 71, \"per_task\": {\"open_the_middle_drawer_of_the_cabinet\": 0.9, \"put_the_bowl_on_the_stove\": 0.9, \"put_the_wine_bottle_on_top_of_the_cabinet\": 0.5, \"open_the_top_drawer_and_put_the_bowl_inside\": 0.4, \"put_the_bowl_on_top_of_the_cabinet\": 0.6, \"push_the_plate_to_the_front_of_the_stove\": 0.8, \"put_the_cream_cheese_in_the_bowl\": 0.5, \"turn_on_the_stove\": 0.9, \"put_the_bowl_on_the_plate\": 0.9, \"put_the_wine_bottle_on_the_rack\": 0.7}}}, \"eval-vla-only-long-seed46\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.18, \"n_tasks\": 10, \"n_rollouts\": 10, \"total_episodes\": 100, \"per_task\": {\"LIVING_ROOM_SCENE2_put_both_the_alphabet_soup_and_the_tomato_sauce_in_the_basket\": 0, \"LIVING_ROOM_SCENE2_put_both_the_cream_cheese_box_and_the_butter_in_the_basket\": 0, \"KITCHEN_SCENE3_turn_on_the_stove_and_put_the_moka_pot_on_it\": 0.9, \"KITCHEN_SCENE4_put_the_black_bowl_in_the_bottom_drawer_of_the_cabinet_and_close_it\": 0, \"LIVING_ROOM_SCENE5_put_the_white_mug_on_the_left_plate_and_put_the_yellow_and_white_mug_on_the_right_plate\": 0.5, \"STUDY_SCENE1_pick_up_the_book_and_place_it_in_the_back_compartment_of_the_caddy\": 0.1, \"LIVING_ROOM_SCENE6_put_the_white_mug_on_the_plate_and_put_the_chocolate_pudding_to_the_right_of_the_plate\": 0.1, \"LIVING_ROOM_SCENE1_put_both_the_alphabet_soup_and_the_cream_cheese_box_in_the_basket\": 0, \"KITCHEN_SCENE8_put_both_moka_pots_on_the_stove\": 0, \"KITCHEN_SCENE6_put_the_yellow_and_white_mug_in_the_microwave_and_close_it\": 0.2}}}, \"eval-vla-only-long-seed45\": {\"status\": \"DONE\", \"metrics\": {\"overall_success_rate\": 0.17, \"n_tasks\": 10, \"n_rollouts\": 10, \"total_episodes\": 100, \"per_task\": {\"LIVING_ROOM_SCENE2_put_both_the_alphabet_soup_and_the_tomato_sauce_in_the_basket\": 0, \"LIVING_ROOM_SCENE2_put_both_the_cream_cheese_box_and_the_butter_in_the_basket\": 0, \"KITCHEN_SCENE3_turn_on_the_stove_and_put_the_moka_pot_on_it\": 1, \"KITCHEN_SCENE4_put_the_black_bowl_in_the_bottom_drawer_of_the_cabinet_and_close_it\": 0, \"LIVING_ROOM_SCENE5_put_the_white_mug_on_the_left_plate_and_put_the_yellow_and_white_mug_on_the_right_plate\": 0.2, \"STUDY_SCENE1_pick_up_the_book_and_place_it_in_the_back_compartment_of_the_caddy\": 0.2, \"LIVING_ROOM_SCENE6_put_the_white_mug_on_the_plate_and_put_the_chocolate_pudding_to_the_right_of_the_plate\": 0.1, \"LIVING_ROOM_SCENE1_put_both_the_alphabet_soup_and_the_cream_cheese_box_in_the_basket\": 0, \"KITCHEN_SCENE8_put_both_moka_pots_on_the_stove\": 0, \"KITCHEN_SCENE6_put_the_yellow_and_white_mug_in_the_microwave_and_close_it\": 0.2}}, \"conclusion\": \"success\"}, \"eval-perdof-object-norm003-seed47\": {\"status\": \"DONE\", \"metrics\": {\"overall_success_rate\": 0.15, \"n_tasks\": 10, \"n_rollouts\": 10, \"per_task\": {\"alphabet_soup\": 0, \"cream_cheese\": 0, \"salad_dressing\": 0.2, \"bbq_sauce\": 0.3, \"ketchup\": 0, \"tomato_sauce\": 0.1, \"butter\": 0.2, \"milk\": 0.1, \"chocolate_pudding\": 0.3, \"orange_juice\": 0.3}}, \"conclusion\": \"success\"}, \"eval-perdof-object-norm005-seed47\": {\"status\": \"DONE\", \"metrics\": {\"overall_success_rate\": 0.1, \"n_tasks\": 10, \"n_rollouts\": 10, \"per_task\": {\"alphabet_soup\": 0, \"cream_cheese\": 0, \"salad_dressing\": 0.1, \"bbq_sauce\": 0.2, \"ketchup\": 0, \"tomato_sauce\": 0, \"butter\": 0.1, \"milk\": 0, \"chocolate_pudding\": 0.4, \"orange_juice\": 0.2}}, \"conclusion\": \"success\"}, \"eval-vla-only-long-seed44\": {\"status\": \"DONE\", \"metrics\": {\"overall_success_rate\": 0.12, \"n_tasks\": 10, \"n_rollouts\": 10, \"per_task\": {\"LIVING_ROOM_SCENE2_alphabet_soup_tomato_sauce_basket\": 0, \"LIVING_ROOM_SCENE2_cream_cheese_butter_basket\": 0, \"KITCHEN_SCENE3_stove_moka_pot\": 0.8, \"KITCHEN_SCENE4_black_bowl_drawer\": 0, \"LIVING_ROOM_SCENE5_white_mug_left_yellow_mug_right\": 0.2, \"STUDY_SCENE1_book_caddy\": 0.1, \"LIVING_ROOM_SCENE6_white_mug_plate_chocolate_pudding\": 0, \"LIVING_ROOM_SCENE1_alphabet_soup_cream_cheese_basket\": 0, \"KITCHEN_SCENE8_both_moka_pots_stove\": 0, \"KITCHEN_SCENE6_yellow_white_mug_microwave\": 0.1}}, \"conclusion\": \"success\"}, \"eval-vla-only-long-seed42\": {\"status\": \"DONE\", \"metrics\": {\"overall_success_rate\": 0.11, \"n_tasks\": 10, \"n_rollouts\": 10, \"per_task\": {\"LIVING_ROOM_SCENE2_alphabet_soup_tomato_sauce_basket\": 0, \"LIVING_ROOM_SCENE2_cream_cheese_butter_basket\": 0, \"KITCHEN_SCENE3_stove_moka_pot\": 0.8, \"KITCHEN_SCENE4_black_bowl_drawer\": 0, \"LIVING_ROOM_SCENE5_white_mug_left_yellow_mug_right\": 0.1, \"STUDY_SCENE1_book_caddy\": 0.1, \"LIVING_ROOM_SCENE6_white_mug_plate_chocolate_pudding\": 0, \"LIVING_ROOM_SCENE1_alphabet_soup_cream_cheese_basket\": 0, \"KITCHEN_SCENE8_both_moka_pots_stove\": 0, \"KITCHEN_SCENE6_yellow_white_mug_microwave\": 0.1}}, \"conclusion\": \"success\"}, \"eval-vla-only-long-seed43\": {\"status\": \"DONE\", \"metrics\": {\"overall_success_rate\": 0.13, \"n_tasks\": 10, \"n_rollouts\": 10, \"per_task\": {\"LIVING_ROOM_SCENE2_alphabet_soup_tomato_sauce_basket\": 0, \"LIVING_ROOM_SCENE2_cream_cheese_butter_basket\": 0, \"KITCHEN_SCENE3_stove_moka_pot\": 0.7, \"KITCHEN_SCENE4_black_bowl_drawer\": 0, \"LIVING_ROOM_SCENE5_white_mug_left_yellow_mug_right\": 0.3, \"STUDY_SCENE1_book_caddy\": 0, \"LIVING_ROOM_SCENE6_white_mug_plate_chocolate_pudding\": 0.1, \"LIVING_ROOM_SCENE1_alphabet_soup_cream_cheese_basket\": 0, \"KITCHEN_SCENE8_both_moka_pots_stove\": 0, \"KITCHEN_SCENE6_yellow_white_mug_microwave\": 0.2}}, \"conclusion\": \"success\"}, \"eval-obs-only-spatial-norm02-seed47\": {\"status\": \"DONE\", \"metrics\": {\"overall_success_rate\": 0.32, \"per_task\": {\"pick_up_the_black_bowl_between_the_plate_and_the_ramekin_and_place_it_on_the_plate\": 0.8, \"pick_up_the_black_bowl_next_to_the_ramekin_and_place_it_on_the_plate\": 0.9, \"pick_up_the_black_bowl_from_table_center_and_place_it_on_the_plate\": 0, \"pick_up_the_black_bowl_on_the_cookie_box_and_place_it_on_the_plate\": 0.3, \"pick_up_the_black_bowl_in_the_top_drawer_of_the_wooden_cabinet_and_place_it_on_the_plate\": 0.1, \"pick_up_the_black_bowl_on_the_ramekin_and_place_it_on_the_plate\": 0, \"pick_up_the_black_bowl_next_to_the_cookie_box_and_place_it_on_the_plate\": 0.9, \"pick_up_the_black_bowl_on_the_stove_and_place_it_on_the_plate\": 0, \"pick_up_the_black_bowl_next_to_the_plate_and_place_it_on_the_plate\": 0.2, \"pick_up_the_black_bowl_on_the_wooden_cabinet_and_place_it_on_the_plate\": 0}}, \"conclusion\": \"success\"}, \"eval-random-selection-object-k5-seed45-r2\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.07, \"successes\": 7, \"total\": 100, \"n_tasks\": 10, \"n_rollouts\": 10}}, \"eval-random-selection-object-k5-seed44-r2\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.1, \"successes\": 10, \"total\": 100, \"n_tasks\": 10, \"n_rollouts\": 10}}, \"eval-random-selection-object-k5-seed43-r2\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.11, \"successes\": 11, \"total\": 100, \"n_tasks\": 10, \"n_rollouts\": 10}}, \"eval-random-selection-object-k5-seed42-r2\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.14, \"successes\": 14, \"total\": 100, \"n_tasks\": 10, \"n_rollouts\": 10}}, \"eval-obs-only-spatial-norm02-k5-seed44-r2\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.37, \"successes\": 37, \"total\": 100, \"n_tasks\": 10, \"n_rollouts\": 10}}, \"eval-obs-only-spatial-norm02-k5-seed45-r2\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.34, \"successes\": 34, \"total\": 100, \"n_tasks\": 10, \"n_rollouts\": 10, \"per_task\": {\"pick_up_bowl_between_plate_ramekin\": 0.9, \"pick_up_bowl_next_to_ramekin\": 1, \"pick_up_bowl_from_table_center\": 0, \"pick_up_bowl_on_cookie_box\": 0.3, \"pick_up_bowl_in_top_drawer\": 0.1, \"pick_up_bowl_on_ramekin\": 0, \"pick_up_bowl_next_to_cookie_box\": 0.9, \"pick_up_bowl_on_stove\": 0, \"pick_up_bowl_next_to_plate\": 0.2, \"pick_up_bowl_on_wooden_cabinet\": 0}}}, \"plan_602-latency-profiling\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"vla_encode_ms\": 28.4, \"crm_forward_ms\": 0.246, \"preprocess_ms\": 0.96, \"batched_K1_ms\": 180, \"batched_K5_ms\": 182.3, \"batched_K10_ms\": 162.3, \"batched_K20_ms\": 167.4, \"sequential_K1_ms\": 177, \"sequential_K5_ms\": 891.7, \"sequential_K10_ms\": 1638.9, \"sequential_K20_ms\": 3245.8, \"cgs_K10_ms\": 6.3, \"full_pipe_K10_ms\": 200.7, \"full_pipe_K20_ms\": 199.7, \"vla_model_mb\": 884.1, \"crm_model_mb\": 1.8, \"peak_K20_mb\": 1085.1}}, \"eval-vla-only-spatial-seed45\": {\"status\": \"DONE\", \"metrics\": {\"success_rate\": 0.27, \"per_task\": {\"pick_up_the_black_bowl_between_the_plate_and_the_ramekin_and_place_it_on_the_plate\": 0.7, \"pick_up_the_black_bowl_next_to_the_ramekin_and_place_it_on_the_plate\": 0.9, \"pick_up_the_black_bowl_from_table_center_and_place_it_on_the_plate\": 0, \"pick_up_the_black_bowl_on_the_cookie_box_and_place_it_on_the_plate\": 0.2, \"pick_up_the_black_bowl_in_the_top_drawer_of_the_wooden_cabinet_and_place_it_on_the_plate\": 0, \"pick_up_the_black_bowl_on_the_ramekin_and_place_it_on_the_plate\": 0, \"pick_up_the_black_bowl_next_to_the_cookie_box_and_place_it_on_the_plate\": 0.9, \"pick_up_the_black_bowl_on_the_stove_and_place_it_on_the_plate\": 0, \"pick_up_the_black_bowl_next_to_the_plate_and_place_it_on_the_plate\": 0, \"pick_up_the_black_bowl_on_the_wooden_cabinet_and_place_it_on_the_plate\": 0}, \"n_tasks\": 10, \"n_rollouts\": 10, \"total_rollouts\": 100}, \"conclusion\": \"success\"}, \"eval-perdof-object-norm005-seed45-r2\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.1, \"successes\": 10, \"total\": 100, \"n_tasks\": 10, \"n_rollouts\": 10, \"sr_pct\": \"10%\"}}, \"eval-vla-only-spatial-seed44\": {\"status\": \"DONE\", \"metrics\": {\"success_rate\": 0.31, \"successes\": 31, \"total\": 100, \"per_task\": {\"pick_up_the_black_bowl_between_the_plate_and_the_ramekin_and_place_it_on_the_plate\": 0.6, \"pick_up_the_black_bowl_next_to_the_ramekin_and_place_it_on_the_plate\": 1, \"pick_up_the_black_bowl_from_table_center_and_place_it_on_the_plate\": 0, \"pick_up_the_black_bowl_on_the_cookie_box_and_place_it_on_the_plate\": 0.3, \"pick_up_the_black_bowl_in_the_top_drawer_of_the_wooden_cabinet_and_place_it_on_the_plate\": 0, \"pick_up_the_black_bowl_on_the_ramekin_and_place_it_on_the_plate\": 0, \"pick_up_the_black_bowl_next_to_the_cookie_box_and_place_it_on_the_plate\": 0.9, \"pick_up_the_black_bowl_on_the_stove_and_place_it_on_the_plate\": 0, \"pick_up_the_black_bowl_next_to_the_plate_and_place_it_on_the_plate\": 0.3, \"pick_up_the_black_bowl_on_the_wooden_cabinet_and_place_it_on_the_plate\": 0}}, \"conclusion\": \"success\"}, \"eval-obs-only-object-default-seed48-r2\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.17, \"n_tasks\": 10, \"n_rollouts\": 10, \"total_rollouts\": 100, \"per_task\": {\"alphabet_soup\": 0, \"cream_cheese\": 0, \"salad_dressing\": 0.2, \"bbq_sauce\": 0.4, \"ketchup\": 0.1, \"tomato_sauce\": 0.2, \"butter\": 0.1, \"milk\": 0.1, \"chocolate_pudding\": 0.3, \"orange_juice\": 0.3}}}, \"eval-vla-only-spatial-seed43\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.29, \"successes\": 29, \"total\": 100, \"per_task\": {\"between_plate_and_ramekin\": 0.7, \"next_to_ramekin\": 0.8, \"from_table_center\": 0.1, \"on_cookie_box\": 0.3, \"in_top_drawer\": 0, \"on_ramekin\": 0, \"next_to_cookie_box\": 0.9, \"on_stove\": 0, \"next_to_plate\": 0.1, \"on_wooden_cabinet\": 0}}}, \"eval-vla-only-spatial-seed42\": {\"status\": \"DONE\", \"metrics\": {\"success_rate\": 0.3, \"per_task\": {\"between_plate_and_ramekin\": 0.6, \"next_to_ramekin\": 1, \"from_table_center\": 0, \"on_cookie_box\": 0.2, \"in_top_drawer\": 0, \"on_ramekin\": 0, \"next_to_cookie_box\": 0.9, \"on_stove\": 0, \"next_to_plate\": 0.3, \"on_wooden_cabinet\": 0}}, \"conclusion\": \"success\"}, \"eval-obs-only-spatial-norm02-seed44\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.36, \"successes\": 36, \"total\": 100}}, \"eval-obs-only-object-norm003-seed47-r2\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.15, \"successes\": 15, \"total\": 100}}, \"eval-obs-only-object-norm003-seed48\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.15, \"successes\": 15, \"total\": 100, \"per_task\": {\"alphabet_soup\": 0, \"cream_cheese\": 0, \"salad_dressing\": 2, \"bbq_sauce\": 4, \"ketchup\": 0, \"tomato_sauce\": 1, \"butter\": 0, \"milk\": 2, \"chocolate_pudding\": 4, \"orange_juice\": 2}}}, \"eval-perdof-object-norm01-seed43\": {\"status\": \"DONE\", \"metrics\": {\"sr\": 0.12, \"sr_pct\": \"12%\", \"n_tasks\": 10, \"n_rollouts\": 10, \"per_task\": {\"alphabet_soup\": 0, \"cream_cheese\": 0, \"salad_dressing\": 0.2, \"bbq_sauce\": 0.3, \"ketchup\": 0, \"tomato_sauce\": 0, \"butter\": 0, \"milk\": 0, \"chocolate_pudding\": 0.4, \"orange_juice\": 0.3}}, \"conclusion\": \"success\"}, \"eval-obs-only-object-default-seed45-r2\": {\"status\": \"DONE\", \"metrics\": {\"sr\": 0.18, \"sr_pct\": \"18%\", \"n_tasks\": 10, \"n_rollouts\": 10, \"per_task\": {\"alphabet_soup\": 0, \"cream_cheese\": 0, \"salad_dressing\": 0.3, \"bbq_sauce\": 0.3, \"ketchup\": 0.1, \"tomato_sauce\": 0.1, \"butter\": 0.1, \"milk\": 0.2, \"chocolate_pudding\": 0.4, \"orange_juice\": 0.3}}, \"conclusion\": \"success\"}, \"eval-argmin-object-k5-seed42\": {\"status\": \"DONE\", \"metrics\": {\"sr\": 0.15, \"sr_pct\": \"15%\", \"n_tasks\": 10, \"n_rollouts\": 10, \"per_task\": {\"alphabet_soup\": 0, \"cream_cheese\": 0, \"salad_dressing\": 0.2, \"bbq_sauce\": 0.4, \"ketchup\": 0, \"tomato_sauce\": 0.1, \"butter\": 0, \"milk\": 0.2, \"chocolate_pudding\": 0.4, \"orange_juice\": 0.2}}, \"conclusion\": \"success\"}, \"eval-argmin-object-k5-seed45\": {\"status\": \"DONE\", \"metrics\": {\"sr\": 0.13, \"sr_pct\": \"13%\", \"n_tasks\": 10, \"n_rollouts\": 10, \"per_task\": {\"alphabet_soup\": 0, \"cream_cheese\": 0, \"salad_dressing\": 0.2, \"bbq_sauce\": 0.4, \"ketchup\": 0, \"tomato_sauce\": 0.1, \"butter\": 0.1, \"milk\": 0.1, \"chocolate_pudding\": 0.1, \"orange_juice\": 0.3}}, \"conclusion\": \"success\"}, \"eval-argmin-object-k5-seed43\": {\"status\": \"DONE\", \"metrics\": {\"sr\": 0.13, \"sr_pct\": \"13%\", \"n_tasks\": 10, \"n_rollouts\": 10, \"per_task\": {\"alphabet_soup\": 0, \"cream_cheese\": 0, \"salad_dressing\": 0.3, \"bbq_sauce\": 0.3, \"ketchup\": 0, \"tomato_sauce\": 0, \"butter\": 0.1, \"milk\": 0.1, \"chocolate_pudding\": 0.3, \"orange_juice\": 0.2}}, \"conclusion\": \"success\"}, \"eval-perdof-object-norm03-seed43\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"sr\": 5, \"sr_pct\": \"5%\", \"n_tasks\": 10, \"n_rollouts\": 10}}, \"eval-obs-only-spatial-norm02-seed45\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.34, \"n_tasks\": 10, \"n_rollouts\": 10, \"total_rollouts\": 100, \"successes\": 34}}, \"eval-obs-only-object-norm003-seed44-bjb2\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"train-crm-k1-accg-object-seed42-full\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"plan_701-precompute-k1-spatial\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"plan_701-crm-k1-train\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval_obs_only_norm03_seed48\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.16, \"n_tasks\": 10, \"n_rollouts\": 10, \"total_rollouts\": 100, \"successes\": 16}}, \"eval_obs_only_norm01_seed48\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.18, \"n_tasks\": 10, \"n_rollouts\": 10, \"total_rollouts\": 100, \"successes\": 18}}, \"eval-lto-splitA-vla-only-r3\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.14, \"n_tasks\": 5, \"n_rollouts\": 10, \"total_rollouts\": 50, \"successes\": 7}}, \"eval-lto-splitA-vla-only-r2\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.14, \"n_tasks\": 5, \"n_rollouts\": 10, \"total_rollouts\": 50, \"successes\": 7}}, \"crm-lto-splitA-train\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-perdof-object-norm003-seed48\": {\"status\": \"DONE\", \"metrics\": {\"success_rate\": 0.13, \"n_tasks\": 10, \"n_rollouts\": 10, \"total_rollouts\": 100}, \"conclusion\": \"success\"}, \"eval-obs-only-spatial-norm02-k5-seed43\": {\"status\": \"DONE\", \"metrics\": {\"success_rate\": 0.32, \"n_tasks\": 10, \"n_rollouts\": 10, \"total_rollouts\": 100}, \"conclusion\": \"success\"}, \"eval-obs-only-object-norm02-k5-seed48\": {\"status\": \"DONE\", \"metrics\": {\"success_rate\": 0.18, \"n_tasks\": 10, \"n_rollouts\": 10, \"total_rollouts\": 100}, \"conclusion\": \"success\"}, \"eval-obs-only-spatial-norm02-k5-seed42\": {\"status\": \"DONE\", \"metrics\": {\"success_rate\": 0.35, \"n_tasks\": 10, \"n_rollouts\": 10, \"total_rollouts\": 100}, \"conclusion\": \"success\"}, \"eval-obs-only-object-norm02-k5-seed46\": {\"status\": \"DONE\", \"metrics\": {\"success_rate\": 0.16, \"n_tasks\": 10, \"n_rollouts\": 10, \"total_rollouts\": 100}, \"conclusion\": \"success\"}, \"eval-lto-splitA-vla-only-v2\": {\"status\": \"DONE\", \"metrics\": {\"success_rate\": 0.14, \"n_tasks\": 5, \"n_rollouts\": 10, \"total_rollouts\": 50, \"successes\": 7}, \"conclusion\": \"success\"}, \"eval-perdof-object-norm03-seed47\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.05, \"n_tasks\": 10, \"n_rollouts\": 10, \"total_rollouts\": 100}}, \"eval-obs-only-object-default-seed48\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.17, \"n_tasks\": 10, \"n_rollouts\": 10, \"total_rollouts\": 100}}, \"eval-perdof-object-norm003-seed46\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.09, \"n_tasks\": 10, \"n_rollouts\": 10, \"total_rollouts\": 100}}, \"eval-perdof-object-norm005-seed46\": {\"status\": \"DONE\", \"metrics\": {\"success_rate\": 0.11, \"total_rollouts\": 100}, \"conclusion\": \"success\"}, \"eval-obs-only-object-norm02-k5-seed47\": {\"status\": \"DONE\", \"metrics\": {\"success_rate\": 0.13, \"n_tasks\": 10, \"n_rollouts\": 10, \"total_rollouts\": 100}, \"conclusion\": \"success\"}, \"eval-perdof-object-norm01-seed48\": {\"status\": \"DONE\", \"metrics\": {\"success_rate\": 0.12, \"total_rollouts\": 100}, \"conclusion\": \"success\"}, \"eval-obs-only-object-default-seed47\": {\"status\": \"DONE\", \"metrics\": {\"success_rate\": 0.16, \"total_rollouts\": 100}, \"conclusion\": \"success\"}, \"eval-perdof-object-norm03-seed46\": {\"status\": \"DONE\", \"metrics\": {\"success_rate\": 0.04, \"total_rollouts\": 100}, \"conclusion\": \"success\"}, \"eval-obs-only-object-norm03-seed46\": {\"status\": \"DONE\", \"metrics\": {\"success_rate\": 0.17, \"total_rollouts\": 100}, \"conclusion\": \"success\"}, \"eval-scalar-object-seed46\": {\"status\": \"DONE\", \"metrics\": {\"success_rate\": 0.09, \"total_rollouts\": 100}, \"conclusion\": \"success\"}, \"eval-obs-only-object-norm01-seed47\": {\"status\": \"DONE\", \"metrics\": {\"success_rate\": 0.17, \"total_rollouts\": 100}, \"conclusion\": \"success\"}, \"eval-obs-only-object-norm01-seed45-r2\": {\"status\": \"DONE\", \"metrics\": {\"success_rate\": 0.17, \"n_tasks\": 10, \"n_rollouts\": 10, \"total_rollouts\": 100, \"per_task_sr\": {\"alphabet_soup\": 0, \"cream_cheese\": 0.1, \"salad_dressing\": 0.1, \"bbq_sauce\": 0.4, \"ketchup\": 0.1, \"tomato_sauce\": 0.1, \"butter\": 0.1, \"milk\": 0.2, \"chocolate_pudding\": 0.3, \"orange_juice\": 0.3}}, \"conclusion\": \"success\"}, \"crm-lto-splitA-train-fixed\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-perdof-object-norm003-seed43\": {\"status\": \"DONE\", \"metrics\": {\"overall_success_rate\": 0.13, \"total_rollouts\": 100, \"per_task\": {\"alphabet_soup\": 0, \"cream_cheese\": 0, \"salad_dressing\": 0.2, \"bbq_sauce\": 0.3, \"ketchup\": 0, \"tomato_sauce\": 0.1, \"butter\": 0.1, \"milk\": 0.1, \"chocolate_pudding\": 0.2, \"orange_juice\": 0.3}}, \"conclusion\": \"success\"}, \"eval-perdof-object-norm005-seed43\": {\"status\": \"DONE\", \"metrics\": {\"success_rate\": 0.13, \"n_tasks\": 10, \"n_rollouts\": 10, \"total_rollouts\": 100, \"per_task\": {\"alphabet_soup\": 0, \"cream_cheese\": 0, \"salad_dressing\": 0.3, \"bbq_sauce\": 0.3, \"ketchup\": 0, \"tomato_sauce\": 0, \"butter\": 0.1, \"milk\": 0.1, \"chocolate_pudding\": 0.2, \"orange_juice\": 0.3}}, \"conclusion\": \"success\"}, \"eval-perdof-object-default-seed43\": {\"status\": \"DONE\", \"metrics\": {\"success_rate\": 0, \"n_tasks\": 10, \"n_rollouts\": 10, \"total_rollouts\": 100}, \"conclusion\": \"success\"}, \"eval-obs-only-object-norm02-seed48-r2\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.18, \"n_tasks\": 10, \"n_rollouts\": 10, \"total_rollouts\": 100}}, \"eval-perdof-object-default-seed45\": {\"status\": \"DONE\", \"metrics\": {\"success_rate\": 0, \"n_tasks\": 10, \"n_rollouts\": 10, \"total_rollouts\": 100}, \"conclusion\": \"success\"}, \"eval-obs-only-object-norm02-k5-seed45\": {\"status\": \"DONE\", \"metrics\": {\"success_rate\": 0.15, \"n_tasks\": 10, \"n_rollouts\": 10, \"total_rollouts\": 100}, \"conclusion\": \"success\"}, \"eval-vla-only-object-seed46\": {\"status\": \"DONE\", \"metrics\": {\"success_rate\": 0.13, \"n_tasks\": 10, \"n_rollouts\": 10, \"total_rollouts\": 100}, \"conclusion\": \"success\"}, \"eval-obs-only-object-norm02-k5-seed44\": {\"status\": \"DONE\", \"metrics\": {\"success_rate\": 0.17, \"n_tasks\": 10, \"n_rollouts\": 10, \"total_rollouts\": 100}, \"conclusion\": \"success\"}, \"eval-obs-only-object-norm01-seed46-r3\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.18, \"n_tasks\": 10, \"n_rollouts\": 10, \"total_rollouts\": 100}}, \"eval-random-selection-object-seed43\": {\"status\": \"DONE\", \"metrics\": {\"success_rate\": 0.09, \"n_tasks\": 10, \"n_rollouts\": 10, \"total_rollouts\": 100, \"per_task_sr\": [0, 0, 0.1, 0.1, 0, 0.1, 0, 0.1, 0.2, 0.3]}, \"conclusion\": \"success\"}, \"eval-perdof-object-norm005-seed44\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.09, \"n_tasks\": 10, \"n_rollouts\": 10, \"total_rollouts\": 100, \"per_task\": {\"pick_up_the_alphabet_soup_and_place_it_in_the_basket\": 0, \"pick_up_the_cream_cheese_and_place_it_in_the_basket\": 0, \"pick_up_the_salad_dressing_and_place_it_in_the_basket\": 0.2, \"pick_up_the_bbq_sauce_and_place_it_in_the_basket\": 0.2, \"pick_up_the_ketchup_and_place_it_in_the_basket\": 0, \"pick_up_the_tomato_sauce_and_place_it_in_the_basket\": 0, \"pick_up_the_butter_and_place_it_in_the_basket\": 0, \"pick_up_the_milk_and_place_it_in_the_basket\": 0, \"pick_up_the_chocolate_pudding_and_place_it_in_the_basket\": 0.3, \"pick_up_the_orange_juice_and_place_it_in_the_basket\": 0.2}}}, \"eval-vla-only-object-seed45-r2\": {\"status\": \"DONE\", \"metrics\": {\"overall_success_rate\": 0.11, \"n_tasks\": 10, \"n_rollouts_per_task\": 10, \"total_rollouts\": 100, \"per_task\": {\"alphabet_soup\": 0, \"cream_cheese\": 0.3, \"salad_dressing\": 0.2, \"bbq_sauce\": 0.2, \"ketchup\": 0, \"tomato_sauce\": 0.1, \"butter\": 0, \"milk\": 0, \"chocolate_pudding\": 0.1, \"orange_juice\": 0.2}}, \"conclusion\": \"success\"}, \"eval-obs-only-object-norm03-seed48\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.16, \"n_tasks\": 10, \"n_rollouts\": 10, \"total_rollouts\": 100}}, \"eval-obs-only-object-norm02-k5-seed43\": {\"status\": \"DONE\", \"metrics\": {\"success_rate\": 0.19, \"n_tasks\": 10, \"n_rollouts\": 10, \"total_rollouts\": 100, \"per_task\": {\"alphabet_soup\": 0, \"cream_cheese\": 0.1, \"salad_dressing\": 0.2, \"bbq_sauce\": 0.3, \"ketchup\": 0.1, \"tomato_sauce\": 0.2, \"butter\": 0.1, \"milk\": 0.1, \"chocolate_pudding\": 0.5, \"orange_juice\": 0.3}}, \"conclusion\": \"success\"}, \"eval-perdof-object-norm02-seed43\": {\"status\": \"DONE\", \"metrics\": {\"success_rate\": 0.09, \"n_tasks\": 10, \"n_rollouts\": 10}, \"conclusion\": \"success\"}, \"eval-obs-only-object-norm01-seed45\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.14}}, \"eval-obs-only-object-norm02-k5-seed42\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.14}}, \"eval-acr-spatial-v3\": {\"status\": \"DONE\", \"metrics\": {\"tasks_done\": \"4/10\", \"overall_success_rate\": 0.025, \"total_successes\": 1, \"total_rollouts\": 40, \"per_task_partial\": {\"pick_up_black_bowl_between_plate_and_ramekin\": 0.1, \"pick_up_black_bowl_next_to_ramekin\": 0, \"pick_up_black_bowl_from_table_center\": 0, \"pick_up_black_bowl_on_cookie_box\": 0}, \"snapshot_time\": \"2026-05-14T18:15Z\"}, \"conclusion\": \"success\"}, \"eval-perdof-object-norm02-seed47\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"overall_sr\": 0.11, \"per_task_sr\": {\"alphabet_soup\": 0, \"cream_cheese\": 0.1, \"salad_dressing\": 0.2, \"bbq_sauce\": 0.1, \"ketchup\": 0, \"tomato_sauce\": 0, \"butter\": 0.1, \"milk\": 0, \"chocolate_pudding\": 0.4, \"orange_juice\": 0.2}}}, \"eval-obs-only-object-default-seed46\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"overall_sr\": 0.15, \"per_task\": {\"alphabet_soup\": 0, \"cream_cheese\": 0, \"salad_dressing\": 0.2, \"bbq_sauce\": 0.4, \"ketchup\": 0.1, \"tomato_sauce\": 0.1, \"butter\": 0.1, \"milk\": 0.1, \"chocolate_pudding\": 0.2, \"orange_juice\": 0.3}}}, \"eval-perdof-object-norm02-seed46\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"overall_sr\": 0.09, \"successes\": 9, \"rollouts\": 100, \"per_task_sr\": {\"alphabet_soup\": 0, \"cream_cheese\": 0, \"salad_dressing\": 0.2, \"bbq_sauce\": 0.1, \"ketchup\": 0, \"tomato_sauce\": 0, \"butter\": 0, \"milk\": 0, \"chocolate_pudding\": 0.4, \"orange_juice\": 0.2}}}, \"eval-obs-only-object-norm005-seed43-r2\": {\"status\": \"DONE\", \"metrics\": {\"overall_sr\": 0.14, \"successes\": 14, \"rollouts\": 100, \"per_task_sr\": {\"alphabet_soup\": 0, \"cream_cheese\": 0.1, \"salad_dressing\": 0.1, \"bbq_sauce\": 0.2, \"ketchup\": 0, \"tomato_sauce\": 0, \"butter\": 0.1, \"milk\": 0.2, \"chocolate_pudding\": 0.4, \"orange_juice\": 0.3}}, \"conclusion\": \"success\"}, \"eval-perdof-object-norm02-seed43-r3\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"overall_sr\": 0.09, \"successes\": 9, \"total\": 100}}, \"eval-perdof-object-norm01-seed47-bjb1\": {\"status\": \"DONE\", \"metrics\": {\"overall_sr\": 0.14, \"successes\": 14, \"total\": 100}, \"conclusion\": \"success\"}, \"eval-openvla-object-vla-only-seed42-v2\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"overall_sr\": 0.69, \"n_tasks\": 10, \"n_trials_per_task\": 10, \"total_rollouts\": 100}}, \"eval-perdof-object-norm01-seed46-r2\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"overall_sr\": 0.1, \"per_task\": {\"alphabet_soup\": 0, \"cream_cheese\": 0, \"salad_dressing\": 0.1, \"bbq_sauce\": 0.3, \"ketchup\": 0, \"tomato_sauce\": 0, \"butter\": 0, \"milk\": 0.1, \"chocolate_pudding\": 0.2, \"orange_juice\": 0.3}}}, \"plan_602-latency-profile\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"vla_encode_prefix_ms\": 33.5, \"vla_sample_K1_ms\": 192.6, \"vla_sample_K5_ms\": 965.3, \"vla_sample_K10_ms\": 1913.7, \"vla_sample_K20_ms\": 3858.2, \"cgs_ms\": 6.2, \"crm_forward_ms\": 0.3, \"full_pipeline_K10_ms\": 1908.2, \"acr_overhead_pct\": 0.34}}, \"train-crm-k1-accg-object-seed42-v2\": {\"status\": \"DONE\", \"metrics\": {\"best_val_loss\": 0.007199, \"total_epochs\": 50, \"train_samples\": 65223, \"obs_dim\": \"4x960D\", \"multi_scale\": true}, \"conclusion\": \"success\"}, \"eval-obs-only-object-default-seed45\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.12, \"tasks\": 10, \"rollouts_per_task\": 20, \"total_successes\": 24, \"total_rollouts\": 200}}, \"eval-scalar-object-seed45\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.09, \"successes\": 18, \"total\": 200, \"best_task\": \"chocolate_pudding_0.25\", \"worst_task\": \"alphabet_soup_0.0\"}}, \"eval-perdof-object-norm02-seed45\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.09, \"successes\": 18, \"total\": 200, \"n_tasks\": 10, \"n_rollouts_per_task\": 20}}, \"eval-perdof-object-norm02-seed44\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.1, \"successes\": 10, \"total\": 100, \"per_task\": {\"alphabet_soup\": 0, \"cream_cheese\": 0, \"salad_dressing\": 0.2, \"bbq_sauce\": 0.1, \"ketchup\": 0, \"tomato_sauce\": 0.1, \"butter\": 0, \"milk\": 0, \"chocolate_pudding\": 0.3, \"orange_juice\": 0.3}}}, \"train-crm-k1-accg-object-seed42-fallback\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"best_val_loss\": 0.006505, \"best_epoch\": 43, \"total_epochs\": 50, \"train_samples\": 4857, \"obs_dim\": 960, \"multi_scale\": false, \"wall_clock_seconds\": 914.9}}, \"eval-obs-only-object-norm02-seed47\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.2, \"successes\": 20, \"total\": 100, \"benchmark\": \"object\", \"mode\": \"obs_only\", \"norm\": 0.2, \"seed\": 47}}, \"eval-obs-only-object-norm02-seed46\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.15, \"total_episodes\": 100, \"successes\": 15, \"per_task\": {\"alphabet_soup\": 0, \"cream_cheese\": 0, \"salad_dressing\": 2, \"bbq_sauce\": 3, \"ketchup\": 0, \"tomato_sauce\": 1, \"butter\": 1, \"milk\": 1, \"chocolate_pudding\": 4, \"orange_juice\": 3}}}, \"eval-argmin-object-seed47\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"overall_sr\": 0.1, \"total_successes\": 10, \"total_rollouts\": 100, \"n_rollouts_per_task\": 10, \"seed\": 47, \"benchmark\": \"object\", \"K\": 10, \"mode\": \"reconvla\", \"baseline_mode\": \"single\", \"per_task_sr\": {\"alphabet_soup\": 0, \"cream_cheese\": 0, \"salad_dressing\": 0.1, \"bbq_sauce\": 0.3, \"ketchup\": 0, \"tomato_sauce\": 0.1, \"butter\": 0.1, \"milk\": 0.1, \"chocolate_pudding\": 0.1, \"orange_juice\": 0.2}}}, \"eval-perdof-object-norm01-seed45\": {\"status\": \"DONE\", \"metrics\": {\"overall_sr\": 0.11, \"per_task_sr\": {\"alphabet_soup\": 0, \"cream_cheese\": 0, \"salad_dressing\": 0.2, \"bbq_sauce\": 0.3, \"ketchup\": 0, \"tomato_sauce\": 0, \"butter\": 0, \"milk\": 0.1, \"chocolate_pudding\": 0.2, \"orange_juice\": 0.3}, \"seed\": 45, \"benchmark\": \"object\", \"mode\": \"crm_perdof\", \"max_correction_norm\": 0.1}, \"conclusion\": \"success\"}, \"eval-argmin-object-seed46\": {\"status\": \"DONE\", \"metrics\": {\"overall_sr\": 0.1, \"total_successes\": 10, \"total_rollouts\": 100, \"n_rollouts_per_task\": 10, \"seed\": 46, \"benchmark\": \"object\", \"K\": 10, \"mode\": \"reconvla\", \"baseline_mode\": \"single\", \"per_task_sr\": {\"alphabet_soup\": 0, \"cream_cheese\": 0, \"salad_dressing\": 0.1, \"bbq_sauce\": 0.4, \"ketchup\": 0, \"tomato_sauce\": 0.1, \"butter\": 0.1, \"milk\": 0.1, \"chocolate_pudding\": 0.1, \"orange_juice\": 0.1}}, \"conclusion\": \"success\"}, \"eval-obs-only-object-norm03-seed45-r2\": {\"status\": \"DONE\", \"metrics\": {\"overall_success_rate\": 14, \"total_successes\": 14, \"total_rollouts\": 100, \"per_task\": {\"alphabet_soup\": 0, \"cream_cheese\": 0, \"salad_dressing\": 10, \"bbq_sauce\": 30, \"ketchup\": 10, \"tomato_sauce\": 10, \"butter\": 10, \"milk\": 10, \"chocolate_pudding\": 30, \"orange_juice\": 30}, \"max_correction_norm\": 0.3, \"seed\": 45, \"mode\": \"crm_obs_only\", \"benchmark\": \"object\"}, \"conclusion\": \"success\"}, \"eval-vla-mean-object-seed45\": {\"status\": \"DONE\", \"metrics\": {\"overall_sr\": 0.13, \"total_success\": 13, \"total_rollouts\": 100, \"per_task_sr\": {\"alphabet_soup\": 0, \"cream_cheese\": 0, \"salad_dressing\": 0.1, \"bbq_sauce\": 0.4, \"ketchup\": 0, \"tomato_sauce\": 0.1, \"butter\": 0, \"milk\": 0.1, \"chocolate_pudding\": 0.3, \"orange_juice\": 0.3}, \"multi_seed_summary\": \"seed42=12%, seed43=15%, seed44=10%, seed45=13%, mean=12.5%\"}, \"conclusion\": \"success\"}, \"eval-argmin-object-seed45\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"overall_sr\": 0.12, \"successes\": 12, \"total_rollouts\": 100, \"tasks_completed\": \"10/10\"}}, \"eval-direct-correction-object-seed42-r3\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.14, \"total_episodes\": 100, \"successes\": 14, \"per_task\": {\"alphabet_soup\": 0, \"cream_cheese\": 1, \"salad_dressing\": 1, \"bbq_sauce\": 4, \"ketchup\": 0, \"tomato_sauce\": 1, \"butter\": 1, \"milk\": 1, \"chocolate_pudding\": 3, \"orange_juice\": 2}}}, \"eval-vla-mean-spatial\": {\"status\": \"DONE\", \"metrics\": {\"overall_success_rate_10tasks\": 0.32, \"total_successes\": 32, \"total_trials\": 100, \"T1\": 0.7, \"T2\": 1, \"T3\": 0, \"T4\": 0.3, \"T5\": 0, \"T6\": 0, \"T7\": 0.8, \"T8\": 0, \"T9\": 0.3, \"T10\": 0.1}, \"conclusion\": \"success\"}, \"eval-acr-object-obs-only-norm02\": {\"status\": \"DONE\", \"metrics\": {\"overall_sr\": 0.22, \"total_success\": 22, \"total_rollouts\": 100, \"tasks_done\": 10, \"tasks_total\": 10, \"per_task\": {\"alphabet_soup\": 0, \"cream_cheese\": 0, \"salad_dressing\": 0.3, \"bbq_sauce\": 0.4, \"ketchup\": 0.2, \"tomato_sauce\": 0.1, \"butter\": 0.1, \"milk\": 0.2, \"chocolate_pudding\": 0.6, \"orange_juice\": 0.3}}, \"conclusion\": \"success\"}, \"eval-spatial-v7-full\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.3, \"total_successes\": 30, \"total_episodes\": 100, \"n_tasks\": 10, \"n_rollouts\": 10, \"per_task\": {\"pick_up_black_bowl_between_plate_and_ramekin\": 0.6, \"pick_up_black_bowl_next_to_ramekin\": 1, \"pick_up_black_bowl_from_table_center\": 0, \"pick_up_black_bowl_on_cookie_box\": 0.2, \"pick_up_black_bowl_in_top_drawer\": 0, \"pick_up_black_bowl_on_ramekin\": 0, \"pick_up_black_bowl_next_to_cookie_box\": 0.9, \"pick_up_black_bowl_on_stove\": 0, \"pick_up_black_bowl_next_to_plate\": 0.3, \"pick_up_black_bowl_on_wooden_cabinet\": 0}}}, \"eval-object-v8-full\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.13, \"total_successes\": 13, \"total_rollouts\": 100, \"per_task\": {\"alphabet_soup\": 0, \"cream_cheese\": 0, \"salad_dressing\": 0.2, \"bbq_sauce\": 0.3, \"ketchup\": 0, \"tomato_sauce\": 0.1, \"butter\": 0.1, \"milk\": 0.2, \"chocolate_pudding\": 0.2, \"orange_juice\": 0.2}}}, \"precompute-v5-shard2\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"precompute-v5-shard1\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"precompute-v5-shard0\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"precompute-v4-shard2\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"precompute-v4-shard1\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"precompute-v4-shard0\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-obs-only-object-norm01-seed44\": {\"status\": \"DONE\", \"metrics\": {\"overall_sr\": 0.16, \"total_success\": 16, \"total_rollouts\": 100, \"per_task_sr\": {\"alphabet_soup\": 0, \"cream_cheese\": 0.1, \"salad_dressing\": 0.3, \"bbq_sauce\": 0.2, \"ketchup\": 0, \"tomato_sauce\": 0.1, \"butter\": 0.1, \"milk\": 0.2, \"chocolate_pudding\": 0.3, \"orange_juice\": 0.3}}, \"conclusion\": \"success\"}, \"eval-vla-only-object-seed45\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"overall_sr\": 0.09, \"successes\": 18, \"total\": 200, \"tasks_done\": 10}}, \"eval-vla-only-object-seed43\": {\"status\": \"DONE\", \"metrics\": {\"overall_sr\": 0.12, \"tasks_done\": 10, \"tasks_total\": 10, \"per_task_sr\": {\"alphabet_soup\": 0, \"cream_cheese\": 0.1, \"salad_dressing\": 0.1, \"bbq_sauce\": 0.3, \"ketchup\": 0, \"tomato_sauce\": 0, \"butter\": 0, \"milk\": 0.1, \"chocolate_pudding\": 0.4, \"orange_juice\": 0.2}, \"source\": \"json_file_verified_by_worker\"}, \"conclusion\": \"success\"}, \"eval-vla-mean-spatial-t10\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"T10_on_wooden_shelf\": \"10% (1/10)\", \"note\": \"Only ran task 9 (start_task=9). T10 = wooden shelf task.\"}}, \"eval-reconvla-spatial-v3\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.34, \"total_successes\": 34, \"total_rollouts\": 100, \"per_task\": {\"pick_up_black_bowl_between_plate_and_ramekin\": 0.6, \"pick_up_black_bowl_next_to_ramekin\": 1, \"pick_up_black_bowl_from_table_center\": 0, \"pick_up_black_bowl_on_cookie_box\": 0.3, \"pick_up_black_bowl_in_top_drawer\": 0.1, \"pick_up_black_bowl_on_ramekin\": 0.1, \"pick_up_black_bowl_next_to_cookie_box\": 0.9, \"pick_up_black_bowl_on_stove\": 0, \"pick_up_black_bowl_next_to_plate\": 0.4, \"pick_up_black_bowl_on_wooden_cabinet\": 0}}}, \"crm-train-v2-scalar-unc\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"best_val_loss\": 0.047202, \"best_epoch\": 48, \"total_epochs\": 50, \"final_train_loss\": 0.069679, \"comparison_vs_old\": \"old_6D_buggy=0.008379, new=0.047202 (loss metric changed with v2 fix)\"}}, \"crm-train-v2-perdof\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"best_val_loss\": 0.051684, \"best_epoch\": 48, \"total_epochs\": 50, \"final_train_loss\": 0.076748, \"comparison_vs_old\": \"old_6D_buggy=0.009046, new=0.051684 (loss metric changed with v2 fix)\"}}, \"crm-train-v2-obs-only\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"best_val_loss\": 0.050501, \"best_epoch\": 50, \"total_epochs\": 50, \"final_train_loss\": 0.074839, \"comparison_vs_old\": \"old_6D_buggy=0.018312, new=0.050501 (loss metric changed with v2 fix)\"}}, \"precompute-shard2\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"precompute-shard1\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"precompute-shard0\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"precompute-k5\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"spatial_samples\": 12167, \"object_samples\": 14570, \"total_samples\": 26737, \"spatial_cache_mb\": 106, \"object_cache_mb\": 127, \"total_cache_mb\": 233, \"runtime_min\": 107}}, \"mvp-point-reaching\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"group1_oracle\": {\"A_scalar\": {\"mse_x\": 0.180218, \"mse_y\": 0.02497, \"mse_z\": 0.024232, \"total\": 0.076473}, \"B_perDOF\": {\"mse_x\": 0.172652, \"mse_y\": 0.015544, \"mse_z\": 0.01561, \"total\": 0.067935}, \"C_none\": {\"mse_x\": 0.22706, \"mse_y\": 0.025542, \"mse_z\": 0.024753, \"total\": 0.092451}}, \"group2_oracle\": {\"A_scalar\": {\"mse_x\": 0.064642, \"mse_y\": 0.023836, \"mse_z\": 0.022967, \"total\": 0.037148}, \"B_perDOF\": {\"mse_x\": 0.053403, \"mse_y\": 0.015695, \"mse_z\": 0.01573, \"total\": 0.028276}, \"C_none\": {\"mse_x\": 0.084178, \"mse_y\": 0.025427, \"mse_z\": 0.024798, \"total\": 0.044801}}, \"group3_oracle\": {\"A_scalar\": {\"mse_x\": 0.042948, \"mse_y\": 0.023218, \"mse_z\": 0.022365, \"total\": 0.02951}, \"B_perDOF\": {\"mse_x\": 0.033008, \"mse_y\": 0.015621, \"mse_z\": 0.015647, \"total\": 0.021425}, \"C_none\": {\"mse_x\": 0.053043, \"mse_y\": 0.025523, \"mse_z\": 0.024741, \"total\": 0.034436}}, \"group4_K10\": {\"A_scalar\": {\"mse_x\": 0.187418, \"mse_y\": 0.024701, \"mse_z\": 0.024277, \"total\": 0.078799}, \"B_perDOF\": {\"mse_x\": 0.182888, \"mse_y\": 0.019072, \"mse_z\": 0.018475, \"total\": 0.073478}, \"C_none\": {\"mse_x\": 0.21507, \"mse_y\": 0.02496, \"mse_z\": 0.024637, \"total\": 0.088223}}, \"group5_K10\": {\"A_scalar\": {\"mse_x\": 0.064895, \"mse_y\": 0.02386, \"mse_z\": 0.023596, \"total\": 0.037451}, \"B_perDOF\": {\"mse_x\": 0.05851, \"mse_y\": 0.018868, \"mse_z\": 0.018471, \"total\": 0.03195}, \"C_none\": {\"mse_x\": 0.077047, \"mse_y\": 0.024825, \"mse_z\": 0.02464, \"total\": 0.042171}}, \"group6_K10\": {\"A_scalar\": {\"mse_x\": 0.041848, \"mse_y\": 0.02344, \"mse_z\": 0.023207, \"total\": 0.029498}, \"B_perDOF\": {\"mse_x\": 0.036348, \"mse_y\": 0.018736, \"mse_z\": 0.018453, \"total\": 0.024512}, \"C_none\": {\"mse_x\": 0.048365, \"mse_y\": 0.024827, \"mse_z\": 0.024577, \"total\": 0.03259}}, \"pass_criteria\": {\"group1\": \"PASS\", \"group4\": \"PASS\", \"overall\": \"SUCCESS\"}, \"summary_pct_improvements\": {\"reference_group\": \"group4_K10 (sigma=0.5/0.1/0.1, K=10 estimated uncertainty)\", \"perDOF_vs_scalar_total\": 6.75, \"perDOF_vs_none_total\": 16.71, \"perDOF_vs_scalar_y_axis\": 22.79, \"perDOF_vs_scalar_z_axis\": 23.9, \"paper_claims\": {\"6.7_pct_over_scalar\": \"group4 total: (0.078799-0.073478)/0.078799 = 6.75%\", \"16.7_pct_over_none\": \"group4 total: (0.088223-0.073478)/0.088223 = 16.71%\", \"22_24_pct_per_axis\": \"group4 y: 22.79%, z: 23.90%\"}}}}, \"eval-obs-only-object-default-seed44\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"overall_sr\": 0.16, \"per_task_sr\": {\"alphabet_soup\": 0, \"cream_cheese\": 0.1, \"salad_dressing\": 0.1, \"bbq_sauce\": 0.4, \"ketchup\": 0, \"tomato_sauce\": 0.1, \"butter\": 0.1, \"milk\": 0.2, \"chocolate_pudding\": 0.3, \"orange_juice\": 0.3}}}, \"eval-mag-perdof-norm005-object\": {\"status\": \"DONE\", \"metrics\": {\"overall_sr\": 0.14, \"successes\": 14, \"total\": 100, \"tasks_done\": 10, \"tasks_total\": 10}, \"conclusion\": \"success\"}, \"eval-mag-perdof-norm02-seed43-object-r3\": {\"status\": \"DONE\", \"metrics\": {\"overall_sr\": 0.09, \"successes\": 9, \"total\": 100, \"tasks_done\": 10, \"tasks_total\": 10, \"per_task_sr\": {\"alphabet_soup\": 0, \"cream_cheese\": 0, \"salad_dressing\": 0.1, \"bbq_sauce\": 0.1, \"ketchup\": 0, \"tomato_sauce\": 0, \"butter\": 0, \"milk\": 0, \"chocolate_pudding\": 0.4, \"orange_juice\": 0.3}, \"vs_seed42\": \"-2pp (11% → 9%)\", \"pooled_2seed_perdof_02\": \"10% (20/200)\"}, \"conclusion\": \"success\"}, \"eval-mag-perdof-norm03-object-r3\": {\"status\": \"DONE\", \"metrics\": {\"overall_sr\": 0.04, \"successes\": 4, \"total\": 100, \"tasks_done\": 10, \"tasks_total\": 10}, \"conclusion\": \"success\"}, \"eval-mag-obsonly-norm005\": {\"status\": \"DONE\", \"metrics\": {\"benchmark\": \"spatial\", \"mode\": \"crm_obs_only\", \"max_correction_norm\": 0.05, \"n_rollouts\": 10, \"K\": 10, \"overall_sr\": 35, \"total_success\": 35, \"total_episodes\": 100, \"per_task\": {\"T0_between_plate_ramekin\": 80, \"T1_next_to_ramekin\": 90, \"T2_table_center\": 0, \"T3_on_cookie_box\": 40, \"T4_top_drawer\": 10, \"T5_on_ramekin\": 0, \"T6_next_to_cookie_box\": 80, \"T7_on_stove\": 0, \"T8_next_to_plate\": 50, \"T9_on_wooden_cabinet\": 0}}, \"conclusion\": \"success\"}, \"eval-mag-obsonly-norm003-b2\": {\"status\": \"DONE\", \"metrics\": {\"overall_sr_10task\": 0.34, \"tasks_done\": 10, \"tasks_total\": 10, \"per_task\": {\"between_plate_and_ramekin\": 0.9, \"next_to_ramekin\": 1, \"from_table_center\": 0, \"on_cookie_box\": 0.3, \"in_top_drawer\": 0.1, \"on_ramekin\": 0, \"next_to_cookie_box\": 0.8, \"on_stove\": 0, \"next_to_plate\": 0.3, \"on_wooden_cabinet\": 0}}, \"conclusion\": \"success\"}, \"eval-mag-obsonly-norm03-object\": {\"status\": \"DONE\", \"metrics\": {\"tasks_done\": 10, \"tasks_total\": 10, \"overall_sr\": 0.19, \"successes\": 19, \"total\": 100}, \"conclusion\": \"success\"}, \"eval-mag-obsonly-norm005-object\": {\"status\": \"DONE\", \"metrics\": {\"overall_sr\": 0.13, \"tasks_completed\": 10, \"total_rollouts\": 100, \"successes\": 13, \"per_task_sr\": {\"alphabet_soup\": 0, \"cream_cheese\": 0, \"salad_dressing\": 0.1, \"bbq_sauce\": 0.3, \"ketchup\": 0, \"tomato_sauce\": 0.1, \"butter\": 0.1, \"milk\": 0.2, \"chocolate_pudding\": 0.2, \"orange_juice\": 0.3}}, \"conclusion\": \"success\"}, \"eval-obs-only-object-norm02-seed45\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"overall_sr\": 0.16, \"successes\": 16, \"total_rollouts\": 100, \"tasks_completed\": \"10/10\"}}, \"eval-obs-only-object-norm03-seed44\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"overall_sr\": 0.18, \"total_rollouts\": 100, \"per_task\": {\"alphabet_soup\": 0, \"cream_cheese\": 0.1, \"salad_dressing\": 0.2, \"bbq_sauce\": 0.4, \"ketchup\": 0.1, \"tomato_sauce\": 0.1, \"butter\": 0.1, \"milk\": 0.2, \"chocolate_pudding\": 0.3, \"orange_juice\": 0.3}}}, \"eval-vla-mean-object-seed44\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"overall_sr\": 0.1, \"per_task_sr\": {\"pick_up_the_alphabet_soup_and_place_it_in_the_basket\": 0, \"pick_up_the_cream_cheese_and_place_it_in_the_basket\": 0, \"pick_up_the_salad_dressing_and_place_it_in_the_basket\": 0.1, \"pick_up_the_bbq_sauce_and_place_it_in_the_basket\": 0.3, \"pick_up_the_ketchup_and_place_it_in_the_basket\": 0.1, \"pick_up_the_tomato_sauce_and_place_it_in_the_basket\": 0.1, \"pick_up_the_butter_and_place_it_in_the_basket\": 0, \"pick_up_the_milk_and_place_it_in_the_basket\": 0, \"pick_up_the_chocolate_pudding_and_place_it_in_the_basket\": 0.2, \"pick_up_the_orange_juice_and_place_it_in_the_basket\": 0.2}}}, \"eval-argmin-object-seed44-r2\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"overall_sr\": 0.13, \"successes\": 13, \"total\": 100, \"tasks_done\": 10, \"tasks_total\": 10, \"per_task_sr\": {\"alphabet_soup\": 0, \"cream_cheese\": 0, \"salad_dressing\": 0.1, \"bbq_sauce\": 0.2, \"ketchup\": 0.1, \"tomato_sauce\": 0.1, \"butter\": 0, \"milk\": 0.1, \"chocolate_pudding\": 0.5, \"orange_juice\": 0.2}, \"note\": \"EXIT_CODE=129 was SIGHUP after completion, results valid. log: logs/eval_object_reconvla_seed44.json\"}}, \"eval-obs-only-object-norm02-seed44-r2\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"overall_sr\": 0.16, \"per_task_sr\": {\"alphabet_soup\": 0, \"cream_cheese\": 0.1, \"salad_dressing\": 0.2, \"bbq_sauce\": 0.2, \"ketchup\": 0.1, \"tomato_sauce\": 0.1, \"butter\": 0.2, \"milk\": 0.1, \"chocolate_pudding\": 0.3, \"orange_juice\": 0.3}}}, \"eval-acr-object-v4-default-r2\": {\"status\": \"DONE\", \"metrics\": {\"overall_sr\": 0, \"successes\": 0, \"total\": 100, \"tasks_done\": 10, \"tasks_total\": 10, \"per_task_sr\": {\"alphabet_soup\": 0, \"cream_cheese\": 0, \"salad_dressing\": 0, \"bbq_sauce\": 0, \"ketchup\": 0, \"tomato_sauce\": 0, \"butter\": 0, \"milk\": 0, \"chocolate_pudding\": 0, \"orange_juice\": 0}, \"note\": \"actual mode=crm_perdof with default norm (~1.42), NOT crm_default. Confirms catastrophic failure at uncontrolled correction magnitude.\"}, \"conclusion\": \"success\"}, \"eval-mag-perdof-norm003-object\": {\"status\": \"DONE\", \"metrics\": {\"tasks_done\": 10, \"tasks_total\": 10, \"overall_sr\": 0.14, \"per_task_sr\": {\"alphabet_soup\": 0, \"cream_cheese\": 0, \"salad_dressing\": 0.2, \"bbq_sauce\": 0.2, \"ketchup\": 0.1, \"tomato_sauce\": 0.1, \"butter\": 0.2, \"milk\": 0.1, \"chocolate_pudding\": 0.4, \"orange_juice\": 0.1}}, \"conclusion\": \"success\"}, \"eval-obs-only-object-norm02-seed43-r2\": {\"status\": \"DONE\", \"metrics\": {\"overall_sr\": 0.16, \"successes\": 16, \"total\": 100, \"per_task\": {\"alphabet_soup\": 0, \"cream_cheese\": 0.1, \"salad_dressing\": 0.2, \"bbq_sauce\": 0.4, \"ketchup\": 0, \"tomato_sauce\": 0.1, \"butter\": 0.1, \"milk\": 0.1, \"chocolate_pudding\": 0.4, \"orange_juice\": 0.2}, \"vs_seed42\": \"-6pp (22% → 16%)\", \"vs_argmin_seed43\": \"-1pp (17% → 16%)\", \"pooled_2seed_obs_only_02\": \"19% (38/200)\", \"pooled_2seed_argmin\": \"14.5% (29/200)\"}, \"conclusion\": \"success\"}, \"eval-vla-only-object-seed44-r2\": {\"status\": \"DONE\", \"metrics\": {\"tasks_done\": 10, \"tasks_total\": 10, \"overall_sr\": 0.1, \"per_task_sr\": {\"alphabet_soup\": 0, \"cream_cheese\": 0.1, \"salad_dressing\": 0.2, \"bbq_sauce\": 0.2, \"ketchup\": 0, \"tomato_sauce\": 0, \"butter\": 0, \"milk\": 0.1, \"chocolate_pudding\": 0.2, \"orange_juice\": 0.2}}, \"conclusion\": \"success\"}, \"eval-acr-object-obs-only-default\": {\"status\": \"DONE\", \"metrics\": {\"tasks_done\": 10, \"tasks_total\": 10, \"overall_sr\": 0.17, \"per_task_sr\": {\"alphabet_soup\": 0, \"cream_cheese\": 0, \"salad_dressing\": 0.2, \"bbq_sauce\": 0.4, \"ketchup\": 0, \"tomato_sauce\": 0.1, \"butter\": 0.1, \"milk\": 0.1, \"chocolate_pudding\": 0.5, \"orange_juice\": 0.3}}, \"conclusion\": \"success\"}, \"eval-scalar-object-seed43\": {\"status\": \"DONE\", \"metrics\": {\"tasks_done\": 10, \"tasks_total\": 10, \"avg_sr\": 10, \"per_task_sr\": {\"pick_up_the_alphabet_soup_and_place_it_in_the_basket\": 0, \"pick_up_the_cream_cheese_and_place_it_in_the_basket\": 0, \"pick_up_the_salad_dressing_and_place_it_in_the_basket\": 0, \"pick_up_the_bbq_sauce_and_place_it_in_the_basket\": 30, \"pick_up_the_ketchup_and_place_it_in_the_basket\": 0, \"pick_up_the_tomato_sauce_and_place_it_in_the_basket\": 0, \"pick_up_the_butter_and_place_it_in_the_basket\": 0, \"pick_up_the_milk_and_place_it_in_the_basket\": 10, \"pick_up_the_chocolate_pudding_and_place_it_in_the_basket\": 30, \"pick_up_the_orange_juice_and_place_it_in_the_basket\": 30}}, \"conclusion\": \"success\"}, \"eval-mag-obsonly-norm003-object\": {\"status\": \"DONE\", \"metrics\": {\"overall_sr\": 0.16, \"tasks_done\": 100, \"tasks_total\": 100, \"per_task\": {\"pick_up_the_alphabet_soup_and_place_it_in_the_basket\": 0, \"pick_up_the_cream_cheese_and_place_it_in_the_basket\": 0.2, \"pick_up_the_salad_dressing_and_place_it_in_the_basket\": 0.1, \"pick_up_the_bbq_sauce_and_place_it_in_the_basket\": 0.4, \"pick_up_the_ketchup_and_place_it_in_the_basket\": 0, \"pick_up_the_tomato_sauce_and_place_it_in_the_basket\": 0, \"pick_up_the_butter_and_place_it_in_the_basket\": 0.1, \"pick_up_the_milk_and_place_it_in_the_basket\": 0.2, \"pick_up_the_chocolate_pudding_and_place_it_in_the_basket\": 0.3, \"pick_up_the_orange_juice_and_place_it_in_the_basket\": 0.3}}, \"conclusion\": \"success\"}, \"eval-vla-mean-object-seed43\": {\"status\": \"DONE\", \"metrics\": {\"overall_sr\": 0.15, \"tasks_done\": 10, \"tasks_total\": 10, \"total_success\": 15, \"total_rollouts\": 100, \"per_task\": {\"alphabet_soup\": 0, \"cream_cheese\": 0, \"salad_dressing\": 0.2, \"bbq_sauce\": 0.3, \"ketchup\": 0.1, \"tomato_sauce\": 0.1, \"butter\": 0.1, \"milk\": 0.3, \"chocolate_pudding\": 0.3, \"orange_juice\": 0.1}}, \"conclusion\": \"success\"}, \"eval-perdof-object-seed43\": {\"status\": \"DONE\", \"metrics\": {\"overall_success_rate\": 0.12, \"tasks_done\": 10, \"tasks_total\": 10, \"total_rollouts\": 100, \"total_successes\": 12, \"per_task\": {\"alphabet_soup\": 0, \"cream_cheese\": 0, \"salad_dressing\": 0.2, \"bbq_sauce\": 0.3, \"ketchup\": 0, \"tomato_sauce\": 0, \"butter\": 0, \"milk\": 0, \"chocolate_pudding\": 0.4, \"orange_juice\": 0.3}}, \"conclusion\": \"success\"}, \"eval-argmin-object-seed43\": {\"status\": \"DONE\", \"metrics\": {\"overall_success_rate\": 0.17, \"total_successes\": 17, \"total_trials\": 100, \"per_task\": {\"alphabet_soup\": 0, \"cream_cheese\": 0, \"salad_dressing\": 0.2, \"bbq_sauce\": 0.2, \"ketchup\": 0.1, \"tomato_sauce\": 0.1, \"butter\": 0.2, \"milk\": 0.3, \"chocolate_pudding\": 0.4, \"orange_juice\": 0.2}}, \"conclusion\": \"success\"}, \"eval-mag-obsonly-norm03-r2\": {\"status\": \"DONE\", \"metrics\": {\"bowl_between\": 0.9, \"next_to_ramekin\": 1, \"table_center\": 0, \"cookie_box\": 0.3, \"top_drawer\": 0.1, \"on_ramekin\": 0, \"next_to_cookie_box\": 1, \"stove\": 0, \"next_to_plate\": 0.3, \"wooden_cabinet\": 0, \"overall_SR\": 0.36}, \"conclusion\": \"success\"}, \"eval-vla-mean-object\": {\"status\": \"DONE\", \"metrics\": {\"benchmark\": \"object\", \"mode\": \"vla_only\", \"baseline_mode\": \"mean\", \"n_rollouts\": 10, \"K\": 10, \"seed\": 42, \"overall_sr\": 12, \"total_success\": 12, \"total_rollouts\": 100, \"tasks_done\": \"10/10\", \"per_task\": {\"alphabet_soup\": 0, \"cream_cheese\": 0, \"salad_dressing\": 10, \"bbq_sauce\": 30, \"ketchup\": 10, \"tomato_sauce\": 10, \"butter\": 0, \"milk\": 20, \"chocolate_pudding\": 30, \"orange_juice\": 10}, \"json_output\": \"/root/acr-vla-conformal-refinement/logs/eval_object_vla_mean.json\"}, \"conclusion\": \"success\"}, \"eval-reconvla-object\": {\"status\": \"DONE\", \"metrics\": {\"overall_sr\": 0.12, \"per_task\": {\"alphabet_soup\": 0, \"cream_cheese\": 0, \"salad_dressing\": 0.1, \"bbq_sauce\": 0.3, \"ketchup\": 0, \"tomato_sauce\": 0, \"butter\": 0.1, \"milk\": 0.1, \"chocolate_pudding\": 0.3, \"orange_juice\": 0.3}, \"n_rollouts\": 10, \"total_episodes\": 100, \"total_successes\": 12}, \"conclusion\": \"success\"}, \"eval-acr-object-v4-obs-only\": {\"status\": \"DONE\", \"metrics\": {\"overall_sr\": \"19.0% (19/100)\", \"total_success\": 19, \"total_rollouts\": 100, \"mode\": \"obs_only\", \"benchmark\": \"object\", \"max_correction_norm\": 0.1, \"seed\": 42, \"K\": 10, \"tasks_done\": \"10/10\", \"per_task\": {\"alphabet_soup\": \"0%\", \"cream_cheese\": \"10%\", \"salad_dressing\": \"20%\", \"bbq_sauce\": \"40%\", \"ketchup\": \"10%\", \"tomato_sauce\": \"0%\", \"butter\": \"10%\", \"milk\": \"20%\", \"chocolate_pudding\": \"50%\", \"orange_juice\": \"30%\"}, \"json_output\": \"/root/acr-vla-conformal-refinement/logs/eval_object_obs_only.json\"}, \"conclusion\": \"success\"}, \"eval-acr-object-v4-perdof\": {\"status\": \"DONE\", \"metrics\": {\"overall_sr\": \"11.0% (11/100)\", \"total_success\": 11, \"total_rollouts\": 100, \"mode\": \"perdof\", \"benchmark\": \"object\", \"max_correction_norm\": 0.1, \"seed\": 42, \"K\": 10, \"per_task\": {\"alphabet_soup\": \"0%\", \"cream_cheese\": \"0%\", \"salad_dressing\": \"20%\", \"bbq_sauce\": \"30%\", \"ketchup\": \"0%\", \"tomato_sauce\": \"0%\", \"butter\": \"10%\", \"milk\": \"0%\", \"chocolate_pudding\": \"20%\", \"orange_juice\": \"30%\"}, \"note\": \"perdof object 11% vs argmin ~7% (partial). obs_only leads at ~14% (8/10). Confirms perdof not competitive on object.\"}, \"conclusion\": \"success\"}, \"eval-acr-spatial-v4-scalar-r2\": {\"status\": \"DONE\", \"metrics\": {\"overall_sr\": \"32.0% (32/100)\", \"total_success\": 32, \"total_rollouts\": 100, \"mode\": \"scalar_unc\", \"benchmark\": \"spatial\", \"max_correction_norm\": 0.1, \"seed\": 42, \"K\": 10, \"per_task\": {\"T0\": \"60%\", \"T1\": \"100%\", \"T2\": \"10%\", \"T3\": \"40%\", \"T4\": \"0%\", \"T5\": \"0%\", \"T6\": \"90%\", \"T7\": \"0%\", \"T8\": \"10%\", \"T9\": \"10%\"}, \"note\": \"D030 confirmed: scalar_unc spatial 32% vs argmin 34% = -2pp. T0-T2 from original eval-acr-spatial-v4-scalar, T3-T9 from r2 restart. All CRM variants dead on spatial.\"}, \"conclusion\": \"success\"}, \"eval-acr-spatial-v4-obs-only-r3\": {\"status\": \"DONE\", \"metrics\": {\"overall_sr\": \"35.0% (35/100)\", \"total_success\": 35, \"total_rollouts\": 100, \"mode\": \"crm_obs_only\", \"benchmark\": \"spatial\", \"max_correction_norm\": 0.1, \"seed\": 42, \"K\": 10, \"per_task\": {\"T0\": \"90%\", \"T1\": \"100%\", \"T2\": \"0%\", \"T3\": \"40%\", \"T4\": \"10%\", \"T5\": \"0%\", \"T6\": \"90%\", \"T7\": \"0%\", \"T8\": \"20%\", \"T9\": \"0%\"}, \"r3_subset_T6_T9\": \"27.5% (11/40)\", \"note\": \"D030: obs_only spatial 10-task = 35%. vs argmin 34% = +1pp. Scenario C threshold (>=39%) NOT MET. Earlier T0-T5 advantage (+5pp) wiped out by T6-T9.\"}, \"conclusion\": \"success\"}, \"eval-acr-spatial-v4-small-r2\": {\"status\": \"DONE\", \"metrics\": {\"overall_sr\": \"35.0% (35/100)\", \"total_success\": 35, \"total_rollouts\": 100, \"mode\": \"perdof\", \"benchmark\": \"spatial\", \"max_correction_norm\": 0.1, \"seed\": 42, \"K\": 10, \"per_task\": {\"T0\": \"60%\", \"T1\": \"100%\", \"T2\": \"10%\", \"T3\": \"40%\", \"T4\": \"0%\", \"T5\": \"0%\", \"T6\": \"90%\", \"T7\": \"10%\", \"T8\": \"40%\", \"T9\": \"0%\"}, \"note\": \"D029: perdof spatial complete 10-task = 35%. vs argmin 34% = +1pp. Kill criterion triggered — per-DOF claim dead on spatial.\"}, \"conclusion\": \"success\"}, \"eval-argmin-only-spatial-r2\": {\"status\": \"DONE\", \"metrics\": {\"overall_success_rate\": 0.34, \"total_successes\": 34, \"total_trials\": 100, \"per_task\": {\"T0_between_plate_and_ramekin\": 0.6, \"T1_next_to_ramekin\": 1, \"T2_from_table_center\": 0, \"T3_on_cookie_box\": 0.3, \"T4_in_top_drawer\": 0.1, \"T5_on_ramekin\": 0.1, \"T6_next_to_cookie_box\": 0.9, \"T7_on_stove\": 0, \"T8_next_to_plate\": 0.3, \"T9_on_wooden_cabinet\": 0.1}, \"note\": \"T0-T8 from original run (eval-argmin-only-spatial), T9 from r2 restart. Combined 10-task result.\"}, \"conclusion\": \"success\"}, \"eval-vla-only-object\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"overall_sr\": 0.12, \"total_success\": 12, \"total_trials\": 100, \"per_task\": {\"alphabet_soup\": 0, \"cream_cheese\": 0.1, \"salad_dressing\": 0.2, \"bbq_sauce\": 0.2, \"ketchup\": 0, \"tomato_sauce\": 0.1, \"butter\": 0, \"milk\": 0.1, \"chocolate_pudding\": 0.2, \"orange_juice\": 0.3}}}, \"crm-train-v3-norm-scalar-unc\": {\"status\": \"DONE\", \"metrics\": {\"best_epoch\": 46, \"best_val_loss\": 0.037354, \"final_train_loss\": 0.053422, \"final_val_loss\": 0.03737}, \"conclusion\": \"success\"}, \"crm-train-v3-norm-obs-only\": {\"status\": \"DONE\", \"metrics\": {\"best_epoch\": 48, \"best_val_loss\": 0.01645, \"final_train_loss\": 0.025576, \"final_val_loss\": 0.01645, \"total_epochs\": 50}, \"conclusion\": \"success\"}, \"crm-train-v3-norm\": {\"status\": \"DONE\", \"conclusion\": \"success\"}}, \"count\": 315, \"total\": 315, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 3.1414}}"
    }
  }
}
```

</details>

---

### Assistant

_source line 28_

<details><summary>Logged reasoning block</summary>

```text
The full registry has been saved. Let me use a subagent to parse all the norm sweep experiments from this file, since it's too large for my context.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "e17f41b1-3dce-49fb-a9e5-f5dd86423ed8",
  "uuid": "45c777d9-8b64-4c8b-ba48-f94c7590396c",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011wdUtDuaNy1LtuB4PsQTnH",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 9867,
      "cache_read_input_tokens": 80604,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 9867
      },
      "output_tokens": 9,
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

_source line 29_

registry 返回了完整数据（104K字符）。让我用 subagent 提取所有 norm sweep 数据。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "e17f41b1-3dce-49fb-a9e5-f5dd86423ed8",
  "uuid": "190c06d5-a65c-4717-8cb6-d382a78584fe",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011wdUtDuaNy1LtuB4PsQTnH",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 9867,
      "cache_read_input_tokens": 80604,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 9867
      },
      "output_tokens": 9,
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

_source line 30_

<details open><summary>🔧 Tool call — Agent · `toolu_01BeoBqipD1BKSTsiAooaCKb`</summary>

```json
{
  "description": "Extract norm sweep data from registry",
  "prompt": "I need you to parse a large JSON registry file and extract all \"norm sweep\" experiments for the CRM obs_only method on LIBERO-Object.\n\nThe file is at: /home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-8-projects-acr-vla-conformal-refinement/e17f41b1-3dce-49fb-a9e5-f5dd86423ed8/tool-results/mcp-agent-ml-research-read_registry-1779334024221.txt\n\nThe file is JSON with schema: {result: string}. The `result` field is itself a JSON string that needs to be parsed.\n\nInside the parsed result, there's a `data.experiments` object where keys are experiment IDs.\n\nI need ALL experiments matching these criteria:\n1. exp_id matches pattern `eval-obs-only-object-norm*-seed*` (specifically norm003, norm005, norm01, norm02)\n2. conclusion = \"success\"\n3. Has metrics with a success rate (could be `overall_success_rate`, `success_rate`, `overall_sr`, or `sr`)\n\nFor each matching experiment, extract:\n- exp_id\n- The epsilon value (norm003=0.03, norm005=0.05, norm01=0.1, norm02=0.2)\n- seed number\n- success rate (as percentage, e.g., 0.15 → 15%, or if integer like 14 → 14%)\n- Which metric key was used (overall_success_rate / success_rate / overall_sr / sr)\n- status (DONE / PREPARING / etc.)\n\nAlso check for experiments named `eval-mag-obsonly-norm*` which might be older naming convention for the same sweep (ε=0.03 as norm003, ε=0.05 as norm005, ε=0.1 as norm01, ε=0.2 as norm02, ε=0.3 as norm03).\n\nUse jq or python to parse this. Output a sorted table grouped by epsilon value, with individual seed SRs, and compute n, mean, std for each group.\n\nAlso list any norm sweep experiments that are RUNNING (no conclusion yet) or have conclusion != success (failed/killed).\n\nReport the complete findings as a structured summary."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "e17f41b1-3dce-49fb-a9e5-f5dd86423ed8",
  "uuid": "b3910dc9-3bb6-4393-96ea-fab13f9e4c88",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011wdUtDuaNy1LtuB4PsQTnH",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 9867,
      "cache_read_input_tokens": 80604,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 9867
      },
      "output_tokens": 9,
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

### System

_source line 31_

```json
{
  "type": "system",
  "subtype": "task_started",
  "task_id": "a59bb588553322cf3",
  "tool_use_id": "toolu_01BeoBqipD1BKSTsiAooaCKb",
  "description": "Extract norm sweep data from registry",
  "task_type": "local_agent",
  "prompt": "I need you to parse a large JSON registry file and extract all \"norm sweep\" experiments for the CRM obs_only method on LIBERO-Object.\n\nThe file is at: /home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-8-projects-acr-vla-conformal-refinement/e17f41b1-3dce-49fb-a9e5-f5dd86423ed8/tool-results/mcp-agent-ml-research-read_registry-1779334024221.txt\n\nThe file is JSON with schema: {result: string}. The `result` field is itself a JSON string that needs to be parsed.\n\nInside the parsed result, there's a `data.experiments` object where keys are experiment IDs.\n\nI need ALL experiments matching these criteria:\n1. exp_id matches pattern `eval-obs-only-object-norm*-seed*` (specifically norm003, norm005, norm01, norm02)\n2. conclusion = \"success\"\n3. Has metrics with a success rate (could be `overall_success_rate`, `success_rate`, `overall_sr`, or `sr`)\n\nFor each matching experiment, extract:\n- exp_id\n- The epsilon value (norm003=0.03, norm005=0.05, norm01=0.1, norm02=0.2)\n- seed number\n- success rate (as percentage, e.g., 0.15 → 15%, or if integer like 14 → 14%)\n- Which metric key was used (overall_success_rate / success_rate / overall_sr / sr)\n- status (DONE / PREPARING / etc.)\n\nAlso check for experiments named `eval-mag-obsonly-norm*` which might be older naming convention for the same sweep (ε=0.03 as norm003, ε=0.05 as norm005, ε=0.1 as norm01, ε=0.2 as norm02, ε=0.3 as norm03).\n\nUse jq or python to parse this. Output a sorted table grouped by epsilon value, with individual seed SRs, and compute n, mean, std for each group.\n\nAlso list any norm sweep experiments that are RUNNING (no conclusion yet) or have conclusion != success (failed/killed).\n\nReport the complete findings as a structured summary.",
  "uuid": "8194a56a-db05-4888-831b-1442f2e00b8f",
  "session_id": "e17f41b1-3dce-49fb-a9e5-f5dd86423ed8"
}
```

---

## Round 1

33 recorded events

### User

_source line 32 · 2026-05-21T03:27:21.401Z_

I need you to parse a large JSON registry file and extract all "norm sweep" experiments for the CRM obs_only method on LIBERO-Object.

The file is at: /home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-8-projects-acr-vla-conformal-refinement/e17f41b1-3dce-49fb-a9e5-f5dd86423ed8/tool-results/mcp-agent-ml-research-read_registry-1779334024221.txt

The file is JSON with schema: {result: string}. The `result` field is itself a JSON string that needs to be parsed.

Inside the parsed result, there's a `data.experiments` object where keys are experiment IDs.

I need ALL experiments matching these criteria:
1. exp_id matches pattern `eval-obs-only-object-norm*-seed*` (specifically norm003, norm005, norm01, norm02)
2. conclusion = "success"
3. Has metrics with a success rate (could be `overall_success_rate`, `success_rate`, `overall_sr`, or `sr`)

For each matching experiment, extract:
- exp_id
- The epsilon value (norm003=0.03, norm005=0.05, norm01=0.1, norm02=0.2)
- seed number
- success rate (as percentage, e.g., 0.15 → 15%, or if integer like 14 → 14%)
- Which metric key was used (overall_success_rate / success_rate / overall_sr / sr)
- status (DONE / PREPARING / etc.)

Also check for experiments named `eval-mag-obsonly-norm*` which might be older naming convention for the same sweep (ε=0.03 as norm003, ε=0.05 as norm005, ε=0.1 as norm01, ε=0.2 as norm02, ε=0.3 as norm03).

Use jq or python to parse this. Output a sorted table grouped by epsilon value, with individual seed SRs, and compute n, mean, std for each group.

Also list any norm sweep experiments that are RUNNING (no conclusion yet) or have conclusion != success (failed/killed).

Report the complete findings as a structured summary.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01BeoBqipD1BKSTsiAooaCKb",
  "session_id": "e17f41b1-3dce-49fb-a9e5-f5dd86423ed8",
  "uuid": "43ebf344-c262-43bc-a8ca-1605cf07fe02"
}
```

</details>

---

### Runtime record

_source line 33_

```json
{
  "type": "rate_limit_event",
  "rate_limit_info": {
    "status": "allowed_warning",
    "resetsAt": 1779469200,
    "rateLimitType": "seven_day",
    "utilization": 0.98,
    "isUsingOverage": false,
    "surpassedThreshold": 0.75
  },
  "uuid": "82624b46-ab38-439a-904a-939172f760e3",
  "session_id": "e17f41b1-3dce-49fb-a9e5-f5dd86423ed8"
}
```

---

### System

_source line 34_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a59bb588553322cf3",
  "tool_use_id": "toolu_01BeoBqipD1BKSTsiAooaCKb",
  "description": "Reading ~/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-8-projects-acr-vla-conformal-refinement/e17f41b1-3dce-49fb-a9e5-f5dd86423ed8/tool-results/mcp-agent-ml-research-read_registry-1779334024221.txt",
  "usage": {
    "total_tokens": 14777,
    "tool_uses": 1,
    "duration_ms": 4271
  },
  "last_tool_name": "Read",
  "uuid": "f31a63a3-2ef4-4192-9046-c8e3dae66cbc",
  "session_id": "e17f41b1-3dce-49fb-a9e5-f5dd86423ed8"
}
```

---

### Tool call

_source line 35_

<details open><summary>🔧 Tool call — Read · `toolu_01Tmna2KuDH5Uw5RCfSBoeWn`</summary>

```json
{
  "file_path": "/home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-8-projects-acr-vla-conformal-refinement/e17f41b1-3dce-49fb-a9e5-f5dd86423ed8/tool-results/mcp-agent-ml-research-read_registry-1779334024221.txt",
  "limit": 50
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01BeoBqipD1BKSTsiAooaCKb",
  "session_id": "e17f41b1-3dce-49fb-a9e5-f5dd86423ed8",
  "uuid": "4a46a19c-f5c8-433b-8ef0-a3d989d0fe9c",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LAM2AFxxHB3VDef7RaK5ve",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 6511,
      "cache_read_input_tokens": 8255,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 6511,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 4,
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

_source line 36 · 2026-05-21T03:27:26.126Z_

<details><summary>↩ Tool result · reported error · `toolu_01Tmna2KuDH5Uw5RCfSBoeWn`</summary>

```text
File content (46256 tokens) exceeds maximum allowed tokens (25000). Use offset and limit parameters to read specific portions of the file, or search for specific content instead of reading the whole file.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01BeoBqipD1BKSTsiAooaCKb",
  "session_id": "e17f41b1-3dce-49fb-a9e5-f5dd86423ed8",
  "uuid": "5b3868c6-2135-4713-83b9-8b4fb9cd3106",
  "tool_use_result": "Error: File content (46256 tokens) exceeds maximum allowed tokens (25000). Use offset and limit parameters to read specific portions of the file, or search for specific content instead of reading the whole file."
}
```

</details>

---

### System

_source line 37_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a59bb588553322cf3",
  "tool_use_id": "toolu_01BeoBqipD1BKSTsiAooaCKb",
  "description": "Running Check file size",
  "usage": {
    "total_tokens": 15866,
    "tool_uses": 2,
    "duration_ms": 9000
  },
  "last_tool_name": "Bash",
  "uuid": "887ffc61-37b9-405f-8ec4-16c00a1f2069",
  "session_id": "e17f41b1-3dce-49fb-a9e5-f5dd86423ed8"
}
```

---

### Tool call

_source line 38_

<details open><summary>🔧 Tool call — Bash · `toolu_01ATsnAdmYjxPrdVf5cWcEGa`</summary>

```json
{
  "command": "wc -c /home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-8-projects-acr-vla-conformal-refinement/e17f41b1-3dce-49fb-a9e5-f5dd86423ed8/tool-results/mcp-agent-ml-research-read_registry-1779334024221.txt",
  "description": "Check file size"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01BeoBqipD1BKSTsiAooaCKb",
  "session_id": "e17f41b1-3dce-49fb-a9e5-f5dd86423ed8",
  "uuid": "220818fc-aaf0-4ca3-80e5-4770f0736dbd",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Khv4fR2y2botFz4HMZdkwE",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1089,
      "cache_read_input_tokens": 14766,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1089,
        "ephemeral_1h_input_tokens": 0
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

_source line 39 · 2026-05-21T03:27:30.561Z_

<details><summary>↩ Tool result · `toolu_01ATsnAdmYjxPrdVf5cWcEGa`</summary>

```text
104268 /home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-8-projects-acr-vla-conformal-refinement/e17f41b1-3dce-49fb-a9e5-f5dd86423ed8/tool-results/mcp-agent-ml-research-read_registry-1779334024221.txt
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01BeoBqipD1BKSTsiAooaCKb",
  "session_id": "e17f41b1-3dce-49fb-a9e5-f5dd86423ed8",
  "uuid": "ded97d3a-2631-43eb-90d5-939d851883fd"
}
```

</details>

---

### System

_source line 40_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a59bb588553322cf3",
  "tool_use_id": "toolu_01BeoBqipD1BKSTsiAooaCKb",
  "description": "Running Parse registry JSON and extract norm sweep experiments",
  "usage": {
    "total_tokens": 16207,
    "tool_uses": 3,
    "duration_ms": 39198
  },
  "last_tool_name": "Bash",
  "uuid": "c1e265dd-4448-4713-aa2e-f801fa4f1247",
  "session_id": "e17f41b1-3dce-49fb-a9e5-f5dd86423ed8"
}
```

---

### Tool call

_source line 41_

<details open><summary>🔧 Tool call — Bash · `toolu_01G6yR5XfrQ9WcUm1mYoaoua`</summary>

```json
{
  "command": "python3 << 'PYEOF'\nimport json, re, statistics\n\nfilepath = \"/home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-8-projects-acr-vla-conformal-refinement/e17f41b1-3dce-49fb-a9e5-f5dd86423ed8/tool-results/mcp-agent-ml-research-read_registry-1779334024221.txt\"\n\nwith open(filepath, 'r') as f:\n    raw = json.load(f)\n\n# Parse the nested JSON string in 'result'\ndata = json.loads(raw['result'])\n\nexperiments = data.get('data', {}).get('experiments', {})\n\n# Patterns to match\npatterns = [\n    r'eval-obs-only-object-norm\\d+-seed\\d+',\n    r'eval-mag-obsonly-norm\\d+',\n]\n\n# Norm to epsilon mapping\nnorm_to_eps = {\n    'norm003': 0.03,\n    'norm005': 0.05,\n    'norm01': 0.1,\n    'norm02': 0.2,\n    'norm03': 0.3,\n    'norm05': 0.5,\n    'norm1': 1.0,\n}\n\nsr_keys = ['overall_success_rate', 'success_rate', 'overall_sr', 'sr']\n\nmatching = []\nnon_success = []\n\nfor exp_id, exp_data in experiments.items():\n    # Check if matches our patterns\n    is_match = False\n    if re.match(r'eval-obs-only-object-norm\\d+-seed\\d+', exp_id):\n        is_match = True\n    elif re.match(r'eval-mag-obsonly-norm\\d+', exp_id):\n        is_match = True\n    \n    if not is_match:\n        continue\n    \n    status = exp_data.get('status', 'UNKNOWN')\n    conclusion = exp_data.get('conclusion', None)\n    \n    # Extract norm value from exp_id\n    norm_match = re.search(r'norm(\\d+)', exp_id)\n    norm_str = 'norm' + norm_match.group(1) if norm_match else 'unknown'\n    eps = norm_to_eps.get(norm_str, None)\n    \n    # Extract seed\n    seed_match = re.search(r'seed(\\d+)', exp_id)\n    seed = int(seed_match.group(1)) if seed_match else None\n    \n    # Extract success rate from metrics\n    metrics = exp_data.get('metrics', {})\n    sr_val = None\n    sr_key_used = None\n    for k in sr_keys:\n        if k in metrics:\n            sr_val = metrics[k]\n            sr_key_used = k\n            break\n    \n    # Also check nested results\n    if sr_val is None and 'results' in exp_data:\n        results = exp_data['results']\n        if isinstance(results, dict):\n            for k in sr_keys:\n                if k in results:\n                    sr_val = results[k]\n                    sr_key_used = k\n                    break\n    \n    entry = {\n        'exp_id': exp_id,\n        'norm_str': norm_str,\n        'eps': eps,\n        'seed': seed,\n        'status': status,\n        'conclusion': conclusion,\n        'sr_val': sr_val,\n        'sr_key': sr_key_used,\n        'raw_metrics': metrics,\n    }\n    \n    if conclusion == 'success' and sr_val is not None:\n        matching.append(entry)\n    else:\n        non_success.append(entry)\n\n# Convert SR to percentage\ndef to_pct(val):\n    if val is None:\n        return None\n    if isinstance(val, (int, float)):\n        if val <= 1.0:\n            return val * 100\n        return val  # already percentage\n    return None\n\n# Sort matching by eps, then seed\nmatching.sort(key=lambda x: (x['eps'] if x['eps'] else 999, x['seed'] if x['seed'] else 999))\n\nprint(\"=\" * 100)\nprint(\"SUCCESSFUL NORM SWEEP EXPERIMENTS (eval-obs-only-object-norm* / eval-mag-obsonly-norm*)\")\nprint(\"=\" * 100)\n\n# Group by epsilon\nfrom collections import defaultdict\ngroups = defaultdict(list)\nfor e in matching:\n    groups[e['eps']].append(e)\n\nfor eps in sorted(groups.keys()):\n    entries = groups[eps]\n    norm_str = entries[0]['norm_str']\n    print(f\"\\n--- ε = {eps} ({norm_str}) ---\")\n    print(f\"{'exp_id':<50} {'seed':>5} {'SR%':>8} {'metric_key':<25} {'status':<10}\")\n    print(\"-\" * 100)\n    \n    sr_pcts = []\n    for e in entries:\n        pct = to_pct(e['sr_val'])\n        if pct is not None:\n            sr_pcts.append(pct)\n        pct_str = f\"{pct:.1f}%\" if pct is not None else \"N/A\"\n        print(f\"{e['exp_id']:<50} {e['seed'] if e['seed'] is not None else 'N/A':>5} {pct_str:>8} {e['sr_key'] or 'N/A':<25} {e['status']:<10}\")\n    \n    if sr_pcts:\n        n = len(sr_pcts)\n        mean = statistics.mean(sr_pcts)\n        std = statistics.stdev(sr_pcts) if n > 1 else 0.0\n        print(f\"\\n  Summary: n={n}, mean={mean:.2f}%, std={std:.2f}%\")\n\nprint(\"\\n\")\nprint(\"=\" * 100)\nprint(\"NON-SUCCESS / IN-PROGRESS NORM SWEEP EXPERIMENTS\")\nprint(\"=\" * 100)\n\nif non_success:\n    non_success.sort(key=lambda x: (x['eps'] if x['eps'] else 999, x['seed'] if x['seed'] else 999))\n    print(f\"\\n{'exp_id':<50} {'eps':>6} {'seed':>5} {'status':<12} {'conclusion':<12} {'SR':>8} {'metrics_keys'}\")\n    print(\"-\" * 120)\n    for e in non_success:\n        pct = to_pct(e['sr_val'])\n        pct_str = f\"{pct:.1f}%\" if pct is not None else \"N/A\"\n        eps_str = str(e['eps']) if e['eps'] else 'N/A'\n        seed_str = str(e['seed']) if e['seed'] is not None else 'N/A'\n        conclusion_str = str(e['conclusion']) if e['conclusion'] else 'N/A'\n        mk = list(e['raw_metrics'].keys()) if e['raw_metrics'] else []\n        print(f\"{e['exp_id']:<50} {eps_str:>6} {seed_str:>5} {e['status']:<12} {conclusion_str:<12} {pct_str:>8} {mk}\")\nelse:\n    print(\"\\nNone found.\")\n\n# Also dump the raw metric keys/values for successful ones to verify\nprint(\"\\n\")\nprint(\"=\" * 100)\nprint(\"RAW METRICS FOR SUCCESSFUL EXPERIMENTS (for verification)\")\nprint(\"=\" * 100)\nfor e in matching:\n    print(f\"\\n{e['exp_id']}:\")\n    for k, v in e['raw_metrics'].items():\n        print(f\"  {k}: {v}\")\n\nPYEOF\n",
  "description": "Parse registry JSON and extract norm sweep experiments",
  "timeout": 30000
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01BeoBqipD1BKSTsiAooaCKb",
  "session_id": "e17f41b1-3dce-49fb-a9e5-f5dd86423ed8",
  "uuid": "f99f0593-a4a7-4941-ada9-3e8eacd06815",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BBQW6eGsYLKo1mYJAFu3QN",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 299,
      "cache_read_input_tokens": 15855,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 299,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 42,
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

_source line 42 · 2026-05-21T03:28:00.770Z_

<details><summary>↩ Tool result · `toolu_01G6yR5XfrQ9WcUm1mYoaoua`</summary>

```text
====================================================================================================
SUCCESSFUL NORM SWEEP EXPERIMENTS (eval-obs-only-object-norm* / eval-mag-obsonly-norm*)
====================================================================================================

--- ε = 0.03 (norm003) ---
exp_id                                              seed      SR% metric_key                status    
----------------------------------------------------------------------------------------------------
eval-obs-only-object-norm003-seed43                   43    14.0% success_rate              DONE      
eval-obs-only-object-norm003-seed43-r2                43    14.0% success_rate              DONE      
eval-obs-only-object-norm003-seed44-r2                44    15.0% success_rate              DONE      
eval-obs-only-object-norm003-seed44                   44    15.0% success_rate              DONE      
eval-obs-only-object-norm003-seed45                   45    15.0% success_rate              DONE      
eval-obs-only-object-norm003-seed46                   46    15.0% success_rate              DONE      
eval-obs-only-object-norm003-seed47-r2                47    15.0% success_rate              DONE      
eval-obs-only-object-norm003-seed48                   48    15.0% success_rate              DONE      
eval-obs-only-object-norm003-seed56                   56    15.0% overall_success_rate      DONE      
eval-obs-only-object-norm003-seed59                   59    13.0% overall_success_rate      DONE      
eval-obs-only-object-norm003-seed64                   64    17.0% overall_success_rate      DONE      
eval-obs-only-object-norm003-seed65                   65    17.0% overall_success_rate      DONE      
eval-obs-only-object-norm003-seed73                   73    16.0% overall_success_rate      DONE      
eval-mag-obsonly-norm003-object                      N/A    16.0% overall_sr                DONE      

  Summary: n=14, mean=15.14%, std=1.10%

--- ε = 0.05 (norm005) ---
exp_id                                              seed      SR% metric_key                status    
----------------------------------------------------------------------------------------------------
eval-obs-only-object-norm005-seed43                   43    13.0% sr                        DONE      
eval-obs-only-object-norm005-seed43-r2                43    14.0% overall_sr                DONE      
eval-obs-only-object-norm005-seed44                   44    12.0% success_rate              DONE      
eval-obs-only-object-norm005-seed47                   47    13.0% success_rate              DONE      
eval-obs-only-object-norm005-seed48                   48    13.0% success_rate              DONE      
eval-obs-only-object-norm005-seed49                   49    15.0% success_rate              DONE      
eval-obs-only-object-norm005-seed50                   50    13.0% success_rate              DONE      
eval-obs-only-object-norm005-seed55                   55    15.0% success_rate              DONE      
eval-obs-only-object-norm005-seed58                   58    16.0% overall_success_rate      DONE      
eval-obs-only-object-norm005-seed61                   61    15.0% overall_success_rate      DONE      
eval-obs-only-object-norm005-seed64                   64    15.0% overall_success_rate      DONE      
eval-obs-only-object-norm005-seed65                   65    14.0% overall_success_rate      DONE      
eval-obs-only-object-norm005-seed72                   72    11.0% overall_success_rate      DONE      
eval-obs-only-object-norm005-seed75                   75    15.0% overall_success_rate      DONE      
eval-mag-obsonly-norm005                             N/A    35.0% overall_sr                DONE      
eval-mag-obsonly-norm005-object                      N/A    13.0% overall_sr                DONE      

  Summary: n=16, mean=15.12%, std=5.46%

--- ε = 0.1 (norm01) ---
exp_id                                              seed      SR% metric_key                status    
----------------------------------------------------------------------------------------------------
eval-obs-only-object-norm01-seed44                    44    16.0% overall_sr                DONE      
eval-obs-only-object-norm01-seed45-r2                 45    17.0% success_rate              DONE      
eval-obs-only-object-norm01-seed45                    45    14.0% overall_success_rate      DONE      
eval-obs-only-object-norm01-seed46-r3                 46    18.0% success_rate              DONE      
eval-obs-only-object-norm01-seed47                    47    17.0% success_rate              DONE      
eval-obs-only-object-norm01-seed48                    48    18.0% success_rate              DONE      
eval-obs-only-object-norm01-seed49                    49    16.0% success_rate              DONE      
eval-obs-only-object-norm01-seed50                    50    14.0% success_rate              DONE      
eval-obs-only-object-norm01-seed51-r3                 51    11.0% overall_success_rate      DONE      
eval-obs-only-object-norm01-seed51                    51    11.0% success_rate              DONE      
eval-obs-only-object-norm01-seed52-r3                 52    15.0% overall_success_rate      DONE      
eval-obs-only-object-norm01-seed52                    52    15.0% success_rate              DONE      
eval-obs-only-object-norm01-seed53                    53    19.0% success_rate              DONE      
eval-obs-only-object-norm01-seed54                    54    15.0% success_rate              DONE      
eval-obs-only-object-norm01-seed57                    57    19.0% overall_success_rate      DONE      
eval-obs-only-object-norm01-seed64                    64    15.0% overall_success_rate      DONE      
eval-obs-only-object-norm01-seed65                    65    15.0% overall_success_rate      DONE      
eval-obs-only-object-norm01-seed71                    71    16.0% overall_success_rate      DONE      
eval-obs-only-object-norm01-seed74                    74    13.0% overall_success_rate      DONE      

  Summary: n=19, mean=15.47%, std=2.29%

--- ε = 0.2 (norm02) ---
exp_id                                              seed      SR% metric_key                status    
----------------------------------------------------------------------------------------------------
eval-obs-only-object-norm02-seed42                    42    20.0% overall_success_rate      DONE      
eval-obs-only-object-norm02-seed43-r3                 43    16.0% sr                        DONE      
eval-obs-only-object-norm02-seed43-r2                 43    16.0% overall_sr                DONE      
eval-obs-only-object-norm02-seed44-r2                 44    16.0% overall_sr                DONE      
eval-obs-only-object-norm02-seed45                    45    16.0% overall_sr                DONE      
eval-obs-only-object-norm02-seed46                    46    15.0% success_rate              DONE      
eval-obs-only-object-norm02-seed47                    47    20.0% success_rate              DONE      
eval-obs-only-object-norm02-seed48-r2                 48    18.0% success_rate              DONE      
eval-obs-only-object-norm02-seed49                    49    14.0% overall_success_rate      DONE      
eval-obs-only-object-norm02-seed50                    50    18.0% sr                        DONE      
eval-obs-only-object-norm02-seed51                    51    17.0% success_rate              DONE      
eval-obs-only-object-norm02-seed52                    52    15.0% success_rate              DONE      
eval-obs-only-object-norm02-seed53                    53    16.0% success_rate              DONE      

  Summary: n=13, mean=16.69%, std=1.84%

--- ε = 0.3 (norm03) ---
exp_id                                              seed      SR% metric_key                status    
----------------------------------------------------------------------------------------------------
eval-obs-only-object-norm03-seed44                    44    18.0% overall_sr                DONE      
eval-obs-only-object-norm03-seed45-r2                 45    14.0% overall_success_rate      DONE      
eval-obs-only-object-norm03-seed46                    46    17.0% success_rate              DONE      
eval-obs-only-object-norm03-seed48                    48    16.0% success_rate              DONE      
eval-mag-obsonly-norm03-object                       N/A    19.0% overall_sr                DONE      

  Summary: n=5, mean=16.80%, std=1.92%


====================================================================================================
NON-SUCCESS / IN-PROGRESS NORM SWEEP EXPERIMENTS
====================================================================================================

exp_id                                                eps  seed status       conclusion         SR metrics_keys
------------------------------------------------------------------------------------------------------------------------
eval-obs-only-object-norm003-seed44-bjb2             0.03    44 DONE         success           N/A []
eval-mag-obsonly-norm003-b2                          0.03   N/A DONE         success           N/A ['overall_sr_10task', 'tasks_done', 'tasks_total', 'per_task']
eval-mag-obsonly-norm03-r2                            0.3   N/A DONE         success           N/A ['bowl_between', 'next_to_ramekin', 'table_center', 'cookie_box', 'top_drawer', 'on_ramekin', 'next_to_cookie_box', 'stove', 'next_to_plate', 'wooden_cabinet', 'overall_SR']


====================================================================================================
RAW METRICS FOR SUCCESSFUL EXPERIMENTS (for verification)
====================================================================================================

eval-obs-only-object-norm003-seed43:
  success_rate: 0.14
  n_rollouts: 100

eval-obs-only-object-norm003-seed43-r2:
  success_rate: 14
  total_rollouts: 100
  per_task: {'alphabet_soup': 0, 'cream_cheese': 0, 'salad_dressing': 20, 'bbq_sauce': 30, 'ketchup': 0, 'tomato_sauce': 10, 'butter': 10, 'milk': 20, 'chocolate_pudding': 20, 'orange_juice': 30}

eval-obs-only-object-norm003-seed44-r2:
  success_rate: 0.15
  sr_pct: 15.0%
  n_tasks: 10
  n_rollouts: 10
  total_rollouts: 100

eval-obs-only-object-norm003-seed44:
  success_rate: 15
  total_rollouts: 100
  per_task: {'alphabet_soup': 0, 'cream_cheese': 0, 'salad_dressing': 30, 'bbq_sauce': 20, 'ketchup': 0, 'tomato_sauce': 10, 'butter': 10, 'milk': 20, 'chocolate_pudding': 30, 'orange_juice': 30}

eval-obs-only-object-norm003-seed45:
  success_rate: 0.15
  sr_pct: 15.0%
  n_tasks: 10
  n_rollouts: 10
  total_rollouts: 100

eval-obs-only-object-norm003-seed46:
  success_rate: 0.15
  total_rollouts: 100
  total_successes: 15

eval-obs-only-object-norm003-seed47-r2:
  success_rate: 0.15
  successes: 15
  total: 100

eval-obs-only-object-norm003-seed48:
  success_rate: 0.15
  successes: 15
  total: 100
  per_task: {'alphabet_soup': 0, 'cream_cheese': 0, 'salad_dressing': 2, 'bbq_sauce': 4, 'ketchup': 0, 'tomato_sauce': 1, 'butter': 0, 'milk': 2, 'chocolate_pudding': 4, 'orange_juice': 2}

eval-obs-only-object-norm003-seed56:
  overall_success_rate: 0.15

eval-obs-only-object-norm003-seed59:
  overall_success_rate: 0.13

eval-obs-only-object-norm003-seed64:
  overall_success_rate: 0.17

eval-obs-only-object-norm003-seed65:
  overall_success_rate: 0.17

eval-obs-only-object-norm003-seed73:
  overall_success_rate: 0.16
  total_rollouts: 100

eval-mag-obsonly-norm003-object:
  overall_sr: 0.16
  tasks_done: 100
  tasks_total: 100
  per_task: {'pick_up_the_alphabet_soup_and_place_it_in_the_basket': 0, 'pick_up_the_cream_cheese_and_place_it_in_the_basket': 0.2, 'pick_up_the_salad_dressing_and_place_it_in_the_basket': 0.1, 'pick_up_the_bbq_sauce_and_place_it_in_the_basket': 0.4, 'pick_up_the_ketchup_and_place_it_in_the_basket': 0, 'pick_up_the_tomato_sauce_and_place_it_in_the_basket': 0, 'pick_up_the_butter_and_place_it_in_the_basket': 0.1, 'pick_up_the_milk_and_place_it_in_the_basket': 0.2, 'pick_up_the_chocolate_pudding_and_place_it_in_the_basket': 0.3, 'pick_up_the_orange_juice_and_place_it_in_the_basket': 0.3}

eval-obs-only-object-norm005-seed43:
  sr: 13
  total: 100
  successes: 13
  benchmark: object
  mode: crm_obs_only

eval-obs-only-object-norm005-seed43-r2:
  overall_sr: 0.14
  successes: 14
  rollouts: 100
  per_task_sr: {'alphabet_soup': 0, 'cream_cheese': 0.1, 'salad_dressing': 0.1, 'bbq_sauce': 0.2, 'ketchup': 0, 'tomato_sauce': 0, 'butter': 0.1, 'milk': 0.2, 'chocolate_pudding': 0.4, 'orange_juice': 0.3}

eval-obs-only-object-norm005-seed44:
  success_rate: 12
  total_rollouts: 100
  per_task: {'alphabet_soup': 0, 'cream_cheese': 0, 'salad_dressing': 0, 'bbq_sauce': 30, 'ketchup': 0, 'tomato_sauce': 10, 'butter': 10, 'milk': 20, 'chocolate_pudding': 20, 'orange_juice': 30}

eval-obs-only-object-norm005-seed47:
  success_rate: 0.13
  sr_pct: 13
  n_tasks: 10
  n_rollouts: 10
  total_rollouts: 100

eval-obs-only-object-norm005-seed48:
  success_rate: 0.13
  sr_pct: 13
  n_tasks: 10
  n_rollouts: 10
  total_rollouts: 100

eval-obs-only-object-norm005-seed49:
  success_rate: 0.15
  total_rollouts: 100
  total_successes: 15

eval-obs-only-object-norm005-seed50:
  success_rate: 0.13
  total_rollouts: 100
  total_successes: 13

eval-obs-only-object-norm005-seed55:
  success_rate: 0.15
  total_rollouts: 100
  total_successes: 15

eval-obs-only-object-norm005-seed58:
  overall_success_rate: 0.16

eval-obs-only-object-norm005-seed61:
  overall_success_rate: 0.15

eval-obs-only-object-norm005-seed64:
  overall_success_rate: 0.15

eval-obs-only-object-norm005-seed65:
  overall_success_rate: 0.14

eval-obs-only-object-norm005-seed72:
  overall_success_rate: 0.11
  total_rollouts: 100

eval-obs-only-object-norm005-seed75:
  overall_success_rate: 0.15
  total_rollouts: 100

eval-mag-obsonly-norm005:
  benchmark: spatial
  mode: crm_obs_only
  max_correction_norm: 0.05
  n_rollouts: 10
  K: 10
  overall_sr: 35
  total_success: 35
  total_episodes: 100
  per_task: {'T0_between_plate_ramekin': 80, 'T1_next_to_ramekin': 90, 'T2_table_center': 0, 'T3_on_cookie_box': 40, 'T4_top_drawer': 10, 'T5_on_ramekin': 0, 'T6_next_to_cookie_box': 80, 'T7_on_stove': 0, 'T8_next_to_plate': 50, 'T9_on_wooden_cabinet': 0}

eval-mag-obsonly-norm005-object:
  overall_sr: 0.13
  tasks_completed: 10
  total_rollouts: 100
  successes: 13
  per_task_sr: {'alphabet_soup': 0, 'cream_cheese': 0, 'salad_dressing': 0.1, 'bbq_sauce': 0.3, 'ketchup': 0, 'tomato_sauce': 0.1, 'butter': 0.1, 'milk': 0.2, 'chocolate_pudding': 0.2, 'orange_juice': 0.3}

eval-obs-only-object-norm01-seed44:
  overall_sr: 0.16
  total_success: 16
  total_rollouts: 100
  per_task_sr: {'alphabet_soup': 0, 'cream_cheese': 0.1, 'salad_dressing': 0.3, 'bbq_sauce': 0.2, 'ketchup': 0, 'tomato_sauce': 0.1, 'butter': 0.1, 'milk': 0.2, 'chocolate_pudding': 0.3, 'orange_juice': 0.3}

eval-obs-only-object-norm01-seed45-r2:
  success_rate: 0.17
  n_tasks: 10
  n_rollouts: 10
  total_rollouts: 100
  per_task_sr: {'alphabet_soup': 0, 'cream_cheese': 0.1, 'salad_dressing': 0.1, 'bbq_sauce': 0.4, 'ketchup': 0.1, 'tomato_sauce': 0.1, 'butter': 0.1, 'milk': 0.2, 'chocolate_pudding': 0.3, 'orange_juice': 0.3}

eval-obs-only-object-norm01-seed45:
  overall_success_rate: 0.14

eval-obs-only-object-norm01-seed46-r3:
  success_rate: 0.18
  n_tasks: 10
  n_rollouts: 10
  total_rollouts: 100

eval-obs-only-object-norm01-seed47:
  success_rate: 0.17
  total_rollouts: 100

eval-obs-only-object-norm01-seed48:
  success_rate: 0.18
  n_tasks: 10
  n_rollouts: 10
  total_rollouts: 100

eval-obs-only-object-norm01-seed49:
  success_rate: 0.16
  sr_pct: 16.0%
  n_tasks: 10
  n_rollouts: 10
  total_rollouts: 100

eval-obs-only-object-norm01-seed50:
  success_rate: 0.14
  sr_pct: 14.0%
  n_tasks: 10
  n_rollouts: 10
  total_rollouts: 100
  per_task: {'alphabet_soup': 0, 'cream_cheese': 0, 'salad_dressing': 0.2, 'bbq_sauce': 0.3, 'ketchup': 0, 'tomato_sauce': 0, 'butter': 0.1, 'milk': 0.2, 'chocolate_pudding': 0.3, 'orange_juice': 0.3}

eval-obs-only-object-norm01-seed51-r3:
  overall_success_rate: 0.11

eval-obs-only-object-norm01-seed51:
  success_rate: 0.11
  total_rollouts: 100
  total_successes: 11

eval-obs-only-object-norm01-seed52-r3:
  overall_success_rate: 0.15

eval-obs-only-object-norm01-seed52:
  success_rate: 0.15
  total_rollouts: 100
  total_successes: 15

eval-obs-only-object-norm01-seed53:
  success_rate: 0.19
  total_rollouts: 100
  total_successes: 19

eval-obs-only-object-norm01-seed54:
  success_rate: 0.15
  total_rollouts: 100
  total_successes: 15

eval-obs-only-object-norm01-seed57:
  overall_success_rate: 0.19

eval-obs-only-object-norm01-seed64:
  overall_success_rate: 0.15

eval-obs-only-object-norm01-seed65:
  overall_success_rate: 0.15

eval-obs-only-object-norm01-seed71:
  overall_success_rate: 0.16
  total_rollouts: 100

eval-obs-only-object-norm01-seed74:
  overall_success_rate: 0.13
  total_rollouts: 100

eval-obs-only-object-norm02-seed42:
  overall_success_rate: 0.2
  total_episodes: 100
  total_successes: 20
  per_task: {'alphabet_soup': 0, 'cream_cheese': 0.1, 'salad_dressing': 0.4, 'bbq_sauce': 0.4, 'ketchup': 0, 'tomato_sauce': 0.1, 'butter': 0.2, 'milk': 0.3, 'chocolate_pudding': 0.2, 'orange_juice': 0.3}

eval-obs-only-object-norm02-seed43-r3:
  sr: 16

eval-obs-only-object-norm02-seed43-r2:
  overall_sr: 0.16
  successes: 16
  total: 100
  per_task: {'alphabet_soup': 0, 'cream_cheese': 0.1, 'salad_dressing': 0.2, 'bbq_sauce': 0.4, 'ketchup': 0, 'tomato_sauce': 0.1, 'butter': 0.1, 'milk': 0.1, 'chocolate_pudding': 0.4, 'orange_juice': 0.2}
  vs_seed42: -6pp (22% → 16%)
  vs_argmin_seed43: -1pp (17% → 16%)
  pooled_2seed_obs_only_02: 19% (38/200)
  pooled_2seed_argmin: 14.5% (29/200)

eval-obs-only-object-norm02-seed44-r2:
  overall_sr: 0.16
  per_task_sr: {'alphabet_soup': 0, 'cream_cheese': 0.1, 'salad_dressing': 0.2, 'bbq_sauce': 0.2, 'ketchup': 0.1, 'tomato_sauce': 0.1, 'butter': 0.2, 'milk': 0.1, 'chocolate_pudding': 0.3, 'orange_juice': 0.3}

eval-obs-only-object-norm02-seed45:
  overall_sr: 0.16
  successes: 16
  total_rollouts: 100
  tasks_completed: 10/10

eval-obs-only-object-norm02-seed46:
  success_rate: 0.15
  total_episodes: 100
  successes: 15
  per_task: {'alphabet_soup': 0, 'cream_cheese': 0, 'salad_dressing': 2, 'bbq_sauce': 3, 'ketchup': 0, 'tomato_sauce': 1, 'butter': 1, 'milk': 1, 'chocolate_pudding': 4, 'orange_juice': 3}

eval-obs-only-object-norm02-seed47:
  success_rate: 0.2
  successes: 20
  total: 100
  benchmark: object
  mode: obs_only
  norm: 0.2
  seed: 47

eval-obs-only-object-norm02-seed48-r2:
  success_rate: 0.18
  n_tasks: 10
  n_rollouts: 10
  total_rollouts: 100

eval-obs-only-object-norm02-seed49:
  overall_success_rate: 0.14
  total_rollouts: 100
  total_successes: 14
  per_task: {'alphabet_soup': 0, 'cream_cheese': 0.1, 'salad_dressing': 0.2, 'bbq_sauce': 0.2, 'ketchup': 0, 'tomato_sauce': 0.1, 'butter': 0.1, 'milk': 0.1, 'chocolate_pudding': 0.3, 'orange_juice': 0.3}
  updated_aggregate: {'mean_sr': 16.4, 'std_sr': 2, 'n_seeds': 7, 'prior': '16.8±1.8% (n=6)', 'delta_vs_vla_baseline': '+5.5pp'}

eval-obs-only-object-norm02-seed50:
  sr: 18
  n_tasks: 10
  n_rollouts: 10
  total_rollouts: 100

eval-obs-only-object-norm02-seed51:
  success_rate: 0.17
  n_rollouts: 100

eval-obs-only-object-norm02-seed52:
  success_rate: 0.15
  sr_pct: 15
  n_tasks: 10
  n_rollouts: 10
  total_rollouts: 100

eval-obs-only-object-norm02-seed53:
  success_rate: 0.16
  sr_pct: 16.0%
  n_tasks: 10
  n_rollouts: 10
  total_rollouts: 100

eval-obs-only-object-norm03-seed44:
  overall_sr: 0.18
  total_rollouts: 100
  per_task: {'alphabet_soup': 0, 'cream_cheese': 0.1, 'salad_dressing': 0.2, 'bbq_sauce': 0.4, 'ketchup': 0.1, 'tomato_sauce': 0.1, 'butter': 0.1, 'milk': 0.2, 'chocolate_pudding': 0.3, 'orange_juice': 0.3}

eval-obs-only-object-norm03-seed45-r2:
  overall_success_rate: 14
  total_successes: 14
  total_rollouts: 100
  per_task: {'alphabet_soup': 0, 'cream_cheese': 0, 'salad_dressing': 10, 'bbq_sauce': 30, 'ketchup': 10, 'tomato_sauce': 10, 'butter': 10, 'milk': 10, 'chocolate_pudding': 30, 'orange_juice': 30}
  max_correction_norm: 0.3
  seed: 45
  mode: crm_obs_only
  benchmark: object

eval-obs-only-object-norm03-seed46:
  success_rate: 0.17
  total_rollouts: 100

eval-obs-only-object-norm03-seed48:
  success_rate: 0.16
  n_tasks: 10
  n_rollouts: 10
  total_rollouts: 100

eval-mag-obsonly-norm03-object:
  tasks_done: 10
  tasks_total: 10
  overall_sr: 0.19
  successes: 19
  total: 100
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01BeoBqipD1BKSTsiAooaCKb",
  "session_id": "e17f41b1-3dce-49fb-a9e5-f5dd86423ed8",
  "uuid": "85d700b9-895b-4421-bfe3-967882ca3220"
}
```

</details>

---

### System

_source line 43_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a59bb588553322cf3",
  "tool_use_id": "toolu_01BeoBqipD1BKSTsiAooaCKb",
  "description": "Running Deduplicate seeds and produce clean summary table",
  "usage": {
    "total_tokens": 25983,
    "tool_uses": 4,
    "duration_ms": 75370
  },
  "last_tool_name": "Bash",
  "uuid": "2146ad52-ff9a-4a15-b93d-31cfc20dfb77",
  "session_id": "e17f41b1-3dce-49fb-a9e5-f5dd86423ed8"
}
```

---

### Tool call

_source line 44_

<details open><summary>🔧 Tool call — Bash · `toolu_01Makr3MMYihAekRQcQZ4XYj`</summary>

```json
{
  "command": "python3 << 'PYEOF'\nimport json, re, statistics\nfrom collections import defaultdict\n\nfilepath = \"/home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-8-projects-acr-vla-conformal-refinement/e17f41b1-3dce-49fb-a9e5-f5dd86423ed8/tool-results/mcp-agent-ml-research-read_registry-1779334024221.txt\"\n\nwith open(filepath, 'r') as f:\n    raw = json.load(f)\n\ndata = json.loads(raw['result'])\nexperiments = data.get('data', {}).get('experiments', {})\n\nsr_keys = ['overall_success_rate', 'success_rate', 'overall_sr', 'sr']\nnorm_to_eps = {'norm003': 0.03, 'norm005': 0.05, 'norm01': 0.1, 'norm02': 0.2, 'norm03': 0.3}\n\ndef to_pct(val):\n    if val is None: return None\n    if isinstance(val, (int, float)):\n        return val * 100 if val <= 1.0 else float(val)\n    return None\n\n# Filter: eval-mag-obsonly-norm005 is SPATIAL not object -- exclude it\n# For duplicate seeds (r2, r3 re-runs), keep the LATEST re-run (highest revision)\n# Identify unique seeds per epsilon, taking highest revision\n\nall_entries = []\nfor exp_id, exp_data in experiments.items():\n    is_obs_only_object = bool(re.match(r'eval-obs-only-object-norm\\d+-seed\\d+', exp_id))\n    is_mag_obsonly_object = bool(re.match(r'eval-mag-obsonly-norm\\d+-object$', exp_id))\n    \n    if not (is_obs_only_object or is_mag_obsonly_object):\n        # Check if it's a non-object mag experiment (spatial) -- skip\n        if re.match(r'eval-mag-obsonly-norm\\d+$', exp_id):\n            # This is spatial benchmark, not object\n            continue\n        if re.match(r'eval-mag-obsonly-norm\\d+-r\\d+$', exp_id):\n            continue\n        if re.match(r'eval-mag-obsonly-norm\\d+-b\\d+$', exp_id):\n            continue\n        continue\n    \n    conclusion = exp_data.get('conclusion', None)\n    if conclusion != 'success':\n        continue\n    \n    metrics = exp_data.get('metrics', {})\n    sr_val = None\n    sr_key_used = None\n    for k in sr_keys:\n        if k in metrics:\n            sr_val = metrics[k]\n            sr_key_used = k\n            break\n    \n    if sr_val is None:\n        continue\n\n    norm_match = re.search(r'norm(\\d+)', exp_id)\n    norm_str = 'norm' + norm_match.group(1) if norm_match else 'unknown'\n    eps = norm_to_eps.get(norm_str)\n    \n    seed_match = re.search(r'seed(\\d+)', exp_id)\n    seed = int(seed_match.group(1)) if seed_match else None\n    \n    # Determine revision number (higher = more recent)\n    rev_match = re.search(r'-r(\\d+)$', exp_id)\n    revision = int(rev_match.group(1)) if rev_match else 0\n    \n    # For mag-obsonly entries without seed, use a sentinel\n    if seed is None and is_mag_obsonly_object:\n        seed = -1  # sentinel for mag experiments\n    \n    all_entries.append({\n        'exp_id': exp_id,\n        'eps': eps,\n        'norm_str': norm_str,\n        'seed': seed,\n        'revision': revision,\n        'sr_pct': to_pct(sr_val),\n        'sr_key': sr_key_used,\n    })\n\n# Deduplicate: for each (eps, seed), keep highest revision\ndedup = {}\nfor e in all_entries:\n    key = (e['eps'], e['seed'])\n    if key not in dedup or e['revision'] > dedup[key]['revision']:\n        dedup[key] = e\n\n# Also handle the special case where seed44 has both \"-bjb2\" suffix (no metrics) \n# and normal entry -- already handled above since bjb2 has no SR metrics\n\nentries = sorted(dedup.values(), key=lambda x: (x['eps'], x['seed']))\n\n# Group by epsilon\ngroups = defaultdict(list)\nfor e in entries:\n    groups[e['eps']].append(e)\n\nprint(\"=\" * 110)\nprint(\"CRM obs_only NORM SWEEP on LIBERO-Object (deduplicated, latest revision per seed)\")\nprint(\"=\" * 110)\n\nfor eps in sorted(groups.keys()):\n    grp = groups[eps]\n    norm_str = grp[0]['norm_str']\n    sr_pcts = [e['sr_pct'] for e in grp if e['sr_pct'] is not None]\n    n = len(sr_pcts)\n    mean = statistics.mean(sr_pcts) if n > 0 else 0\n    std = statistics.stdev(sr_pcts) if n > 1 else 0\n    \n    print(f\"\\n--- eps = {eps} ({norm_str}) | n={n}, mean={mean:.2f}%, std={std:.2f}% ---\")\n    print(f\"  {'exp_id':<55} {'seed':>5} {'rev':>4} {'SR%':>7} {'metric_key':<25}\")\n    print(f\"  {'-'*100}\")\n    for e in grp:\n        seed_str = str(e['seed']) if e['seed'] != -1 else 'mag'\n        print(f\"  {e['exp_id']:<55} {seed_str:>5} {e['revision']:>4} {e['sr_pct']:.1f}% {e['sr_key']:<25}\")\n    \n    print(f\"\\n  => {mean:.2f}% +/- {std:.2f}%  (n={n} seeds)\")\n\n# Grand summary table\nprint(\"\\n\\n\")\nprint(\"=\" * 60)\nprint(\"GRAND SUMMARY TABLE\")\nprint(\"=\" * 60)\nprint(f\"{'eps':<8} {'n':>3} {'mean%':>8} {'std%':>8} {'individual SRs'}\")\nprint(\"-\" * 60)\nfor eps in sorted(groups.keys()):\n    grp = groups[eps]\n    sr_pcts = sorted([e['sr_pct'] for e in grp])\n    n = len(sr_pcts)\n    mean = statistics.mean(sr_pcts)\n    std = statistics.stdev(sr_pcts) if n > 1 else 0\n    srs_str = \", \".join(f\"{s:.0f}\" for s in sr_pcts)\n    print(f\"{eps:<8} {n:>3} {mean:>7.2f}% {std:>7.2f}%  [{srs_str}]\")\n\nPYEOF\n",
  "description": "Deduplicate seeds and produce clean summary table",
  "timeout": 30000
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01BeoBqipD1BKSTsiAooaCKb",
  "session_id": "e17f41b1-3dce-49fb-a9e5-f5dd86423ed8",
  "uuid": "98c9e21b-02ee-4cce-a4fc-cc3a356ef9e8",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PC6WbqCH48AXTvK7oHeGGH",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 9774,
      "cache_read_input_tokens": 16154,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 9774,
        "ephemeral_1h_input_tokens": 0
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

_source line 45 · 2026-05-21T03:28:36.965Z_

<details><summary>↩ Tool result · `toolu_01Makr3MMYihAekRQcQZ4XYj`</summary>

```text
==============================================================================================================
CRM obs_only NORM SWEEP on LIBERO-Object (deduplicated, latest revision per seed)
==============================================================================================================

--- eps = 0.03 (norm003) | n=12, mean=15.25%, std=1.14% ---
  exp_id                                                   seed  rev     SR% metric_key               
  ----------------------------------------------------------------------------------------------------
  eval-mag-obsonly-norm003-object                           mag    0 16.0% overall_sr               
  eval-obs-only-object-norm003-seed43-r2                     43    2 14.0% success_rate             
  eval-obs-only-object-norm003-seed44-r2                     44    2 15.0% success_rate             
  eval-obs-only-object-norm003-seed45                        45    0 15.0% success_rate             
  eval-obs-only-object-norm003-seed46                        46    0 15.0% success_rate             
  eval-obs-only-object-norm003-seed47-r2                     47    2 15.0% success_rate             
  eval-obs-only-object-norm003-seed48                        48    0 15.0% success_rate             
  eval-obs-only-object-norm003-seed56                        56    0 15.0% overall_success_rate     
  eval-obs-only-object-norm003-seed59                        59    0 13.0% overall_success_rate     
  eval-obs-only-object-norm003-seed64                        64    0 17.0% overall_success_rate     
  eval-obs-only-object-norm003-seed65                        65    0 17.0% overall_success_rate     
  eval-obs-only-object-norm003-seed73                        73    0 16.0% overall_success_rate     

  => 15.25% +/- 1.14%  (n=12 seeds)

--- eps = 0.05 (norm005) | n=14, mean=13.86%, std=1.41% ---
  exp_id                                                   seed  rev     SR% metric_key               
  ----------------------------------------------------------------------------------------------------
  eval-mag-obsonly-norm005-object                           mag    0 13.0% overall_sr               
  eval-obs-only-object-norm005-seed43-r2                     43    2 14.0% overall_sr               
  eval-obs-only-object-norm005-seed44                        44    0 12.0% success_rate             
  eval-obs-only-object-norm005-seed47                        47    0 13.0% success_rate             
  eval-obs-only-object-norm005-seed48                        48    0 13.0% success_rate             
  eval-obs-only-object-norm005-seed49                        49    0 15.0% success_rate             
  eval-obs-only-object-norm005-seed50                        50    0 13.0% success_rate             
  eval-obs-only-object-norm005-seed55                        55    0 15.0% success_rate             
  eval-obs-only-object-norm005-seed58                        58    0 16.0% overall_success_rate     
  eval-obs-only-object-norm005-seed61                        61    0 15.0% overall_success_rate     
  eval-obs-only-object-norm005-seed64                        64    0 15.0% overall_success_rate     
  eval-obs-only-object-norm005-seed65                        65    0 14.0% overall_success_rate     
  eval-obs-only-object-norm005-seed72                        72    0 11.0% overall_success_rate     
  eval-obs-only-object-norm005-seed75                        75    0 15.0% overall_success_rate     

  => 13.86% +/- 1.41%  (n=14 seeds)

--- eps = 0.1 (norm01) | n=16, mean=15.88%, std=2.16% ---
  exp_id                                                   seed  rev     SR% metric_key               
  ----------------------------------------------------------------------------------------------------
  eval-obs-only-object-norm01-seed44                         44    0 16.0% overall_sr               
  eval-obs-only-object-norm01-seed45-r2                      45    2 17.0% success_rate             
  eval-obs-only-object-norm01-seed46-r3                      46    3 18.0% success_rate             
  eval-obs-only-object-norm01-seed47                         47    0 17.0% success_rate             
  eval-obs-only-object-norm01-seed48                         48    0 18.0% success_rate             
  eval-obs-only-object-norm01-seed49                         49    0 16.0% success_rate             
  eval-obs-only-object-norm01-seed50                         50    0 14.0% success_rate             
  eval-obs-only-object-norm01-seed51-r3                      51    3 11.0% overall_success_rate     
  eval-obs-only-object-norm01-seed52-r3                      52    3 15.0% overall_success_rate     
  eval-obs-only-object-norm01-seed53                         53    0 19.0% success_rate             
  eval-obs-only-object-norm01-seed54                         54    0 15.0% success_rate             
  eval-obs-only-object-norm01-seed57                         57    0 19.0% overall_success_rate     
  eval-obs-only-object-norm01-seed64                         64    0 15.0% overall_success_rate     
  eval-obs-only-object-norm01-seed65                         65    0 15.0% overall_success_rate     
  eval-obs-only-object-norm01-seed71                         71    0 16.0% overall_success_rate     
  eval-obs-only-object-norm01-seed74                         74    0 13.0% overall_success_rate     

  => 15.88% +/- 2.16%  (n=16 seeds)

--- eps = 0.2 (norm02) | n=12, mean=16.75%, std=1.91% ---
  exp_id                                                   seed  rev     SR% metric_key               
  ----------------------------------------------------------------------------------------------------
  eval-obs-only-object-norm02-seed42                         42    0 20.0% overall_success_rate     
  eval-obs-only-object-norm02-seed43-r3                      43    3 16.0% sr                       
  eval-obs-only-object-norm02-seed44-r2                      44    2 16.0% overall_sr               
  eval-obs-only-object-norm02-seed45                         45    0 16.0% overall_sr               
  eval-obs-only-object-norm02-seed46                         46    0 15.0% success_rate             
  eval-obs-only-object-norm02-seed47                         47    0 20.0% success_rate             
  eval-obs-only-object-norm02-seed48-r2                      48    2 18.0% success_rate             
  eval-obs-only-object-norm02-seed49                         49    0 14.0% overall_success_rate     
  eval-obs-only-object-norm02-seed50                         50    0 18.0% sr                       
  eval-obs-only-object-norm02-seed51                         51    0 17.0% success_rate             
  eval-obs-only-object-norm02-seed52                         52    0 15.0% success_rate             
  eval-obs-only-object-norm02-seed53                         53    0 16.0% success_rate             

  => 16.75% +/- 1.91%  (n=12 seeds)

--- eps = 0.3 (norm03) | n=5, mean=16.80%, std=1.92% ---
  exp_id                                                   seed  rev     SR% metric_key               
  ----------------------------------------------------------------------------------------------------
  eval-mag-obsonly-norm03-object                            mag    0 19.0% overall_sr               
  eval-obs-only-object-norm03-seed44                         44    0 18.0% overall_sr               
  eval-obs-only-object-norm03-seed45-r2                      45    2 14.0% overall_success_rate     
  eval-obs-only-object-norm03-seed46                         46    0 17.0% success_rate             
  eval-obs-only-object-norm03-seed48                         48    0 16.0% success_rate             

  => 16.80% +/- 1.92%  (n=5 seeds)



============================================================
GRAND SUMMARY TABLE
============================================================
eps        n    mean%     std% individual SRs
------------------------------------------------------------
0.03      12   15.25%    1.14%  [13, 14, 15, 15, 15, 15, 15, 15, 16, 16, 17, 17]
0.05      14   13.86%    1.41%  [11, 12, 13, 13, 13, 13, 14, 14, 15, 15, 15, 15, 15, 16]
0.1       16   15.88%    2.16%  [11, 13, 14, 15, 15, 15, 15, 16, 16, 16, 17, 17, 18, 18, 19, 19]
0.2       12   16.75%    1.91%  [14, 15, 15, 16, 16, 16, 16, 17, 18, 18, 20, 20]
0.3        5   16.80%    1.92%  [14, 16, 17, 18, 19]
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01BeoBqipD1BKSTsiAooaCKb",
  "session_id": "e17f41b1-3dce-49fb-a9e5-f5dd86423ed8",
  "uuid": "a9e6893f-0471-4baf-b6c0-b82ba60bb8cd"
}
```

</details>

---

### System

_source line 46_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a59bb588553322cf3",
  "tool_use_id": "toolu_01BeoBqipD1BKSTsiAooaCKb",
  "description": "Running Find non-success/in-progress norm sweep experiments",
  "usage": {
    "total_tokens": 30472,
    "tool_uses": 5,
    "duration_ms": 98524
  },
  "last_tool_name": "Bash",
  "uuid": "5811e21a-c342-40aa-a727-66912bb69f6d",
  "session_id": "e17f41b1-3dce-49fb-a9e5-f5dd86423ed8"
}
```

---

### Tool call

_source line 47_

<details open><summary>🔧 Tool call — Bash · `toolu_01KvhNaBZ8wwrqeUGVF1Fear`</summary>

```json
{
  "command": "python3 << 'PYEOF'\nimport json, re\n\nfilepath = \"/home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-8-projects-acr-vla-conformal-refinement/e17f41b1-3dce-49fb-a9e5-f5dd86423ed8/tool-results/mcp-agent-ml-research-read_registry-1779334024221.txt\"\n\nwith open(filepath, 'r') as f:\n    raw = json.load(f)\n\ndata = json.loads(raw['result'])\nexperiments = data.get('data', {}).get('experiments', {})\n\nprint(\"NON-SUCCESS / IN-PROGRESS / NO-METRICS norm sweep experiments:\")\nprint(\"=\" * 120)\nprint(f\"{'exp_id':<60} {'status':<12} {'conclusion':<12} {'has_sr':>7} {'notes'}\")\nprint(\"-\" * 120)\n\nfor exp_id, exp_data in sorted(experiments.items()):\n    # Match norm sweep patterns broadly\n    if not (re.search(r'norm\\d+', exp_id) and \n            (re.search(r'obs.only.*object|object.*obs.only|mag.obsonly.*object', exp_id, re.I) or\n             re.match(r'eval-obs-only-object-norm', exp_id) or\n             re.match(r'eval-mag-obsonly-norm\\d+-object', exp_id) or\n             re.match(r'eval-mag-obsonly-norm\\d+$', exp_id) or\n             re.match(r'eval-mag-obsonly-norm\\d+-r\\d+$', exp_id) or\n             re.match(r'eval-mag-obsonly-norm\\d+-b\\d+$', exp_id))):\n        continue\n    \n    status = exp_data.get('status', 'UNKNOWN')\n    conclusion = exp_data.get('conclusion', None)\n    metrics = exp_data.get('metrics', {})\n    \n    sr_keys = ['overall_success_rate', 'success_rate', 'overall_sr', 'sr']\n    has_sr = any(k in metrics for k in sr_keys)\n    \n    # Identify problematic entries\n    notes = []\n    if conclusion != 'success':\n        notes.append(f\"conclusion={conclusion}\")\n    if not has_sr and conclusion == 'success':\n        notes.append(\"success but NO SR metric\")\n    if status not in ('DONE',):\n        notes.append(f\"status={status}\")\n    \n    if notes:\n        # Also check if it's spatial not object\n        if re.match(r'eval-mag-obsonly-norm\\d+$', exp_id):\n            notes.append(\"(SPATIAL benchmark, not object)\")\n        if re.match(r'eval-mag-obsonly-norm\\d+-r\\d+$', exp_id):\n            notes.append(\"(SPATIAL re-run)\")\n        if re.match(r'eval-mag-obsonly-norm\\d+-b\\d+$', exp_id):\n            notes.append(\"(SPATIAL batch)\")\n        \n        print(f\"{exp_id:<60} {status:<12} {str(conclusion):<12} {str(has_sr):>7} {'; '.join(notes)}\")\n\nPYEOF\n",
  "description": "Find non-success/in-progress norm sweep experiments",
  "timeout": 15000
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01BeoBqipD1BKSTsiAooaCKb",
  "session_id": "e17f41b1-3dce-49fb-a9e5-f5dd86423ed8",
  "uuid": "c3cdee08-9957-486a-8b80-79fa8b41a977",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VQDiNE7mcFRNHNDsP2weiC",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4487,
      "cache_read_input_tokens": 25928,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4487,
        "ephemeral_1h_input_tokens": 0
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

_source line 48 · 2026-05-21T03:29:00.272Z_

<details><summary>↩ Tool result · `toolu_01KvhNaBZ8wwrqeUGVF1Fear`</summary>

```text
NON-SUCCESS / IN-PROGRESS / NO-METRICS norm sweep experiments:
========================================================================================================================
exp_id                                                       status       conclusion    has_sr notes
------------------------------------------------------------------------------------------------------------------------
eval-mag-obsonly-norm003-b2                                  DONE         success        False success but NO SR metric; (SPATIAL batch)
eval-mag-obsonly-norm03-r2                                   DONE         success        False success but NO SR metric; (SPATIAL re-run)
eval-obs-only-object-norm003-seed44-bjb2                     DONE         success        False success but NO SR metric
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01BeoBqipD1BKSTsiAooaCKb",
  "session_id": "e17f41b1-3dce-49fb-a9e5-f5dd86423ed8",
  "uuid": "fa808f24-5a34-45f7-9607-ba070f53e1ab"
}
```

</details>

---

### System

_source line 49_

```json
{
  "type": "system",
  "subtype": "task_notification",
  "task_id": "a59bb588553322cf3",
  "tool_use_id": "toolu_01BeoBqipD1BKSTsiAooaCKb",
  "status": "completed",
  "output_file": "",
  "summary": "Extract norm sweep data from registry",
  "usage": {
    "total_tokens": 31576,
    "tool_uses": 5,
    "duration_ms": 120904
  },
  "uuid": "07d8886b-b915-44dc-bb94-d2ea76ea68fb",
  "session_id": "e17f41b1-3dce-49fb-a9e5-f5dd86423ed8"
}
```

---

### Tool result

_source line 50 · 2026-05-21T03:29:22.316Z_

<details><summary>↩ Tool result · `toolu_01BeoBqipD1BKSTsiAooaCKb`</summary>

```text
Here is the complete structured summary:

---

## CRM obs_only Norm Sweep on LIBERO-Object

### Methodology
- Parsed the nested JSON registry, extracted all experiments matching `eval-obs-only-object-norm*-seed*` and `eval-mag-obsonly-norm*-object`
- Excluded `eval-mag-obsonly-norm005` (no `-object` suffix = spatial benchmark, SR=35%)
- Deduplicated seeds by keeping the latest revision (e.g., `-r3` over `-r2` over base)
- SR metrics were stored under 4 different keys (`success_rate`, `overall_success_rate`, `overall_sr`, `sr`) with mixed formats (0.15 vs 15); normalized all to percentage

### Grand Summary Table (deduplicated)

| epsilon | n seeds | mean SR% | std SR% | individual SRs |
|---------|---------|----------|---------|----------------|
| 0.03    | 12      | 15.25    | 1.14    | 13,14,15,15,15,15,15,15,16,16,17,17 |
| 0.05    | 14      | 13.86    | 1.41    | 11,12,13,13,13,13,14,14,15,15,15,15,15,16 |
| 0.10    | 16      | 15.88    | 2.16    | 11,13,14,15,15,15,15,16,16,16,17,17,18,18,19,19 |
| 0.20    | 12      | 16.75    | 1.91    | 14,15,15,16,16,16,16,17,18,18,20,20 |
| 0.30    | 5       | 16.80    | 1.92    | 14,16,17,18,19 |

### Key observations
- **eps=0.05 is the worst** at 13.86% mean, notably below all other epsilon values
- **eps=0.20 and eps=0.30 are tied for best** at ~16.8%, though eps=0.30 has only 5 seeds (less statistical power)
- **eps=0.03 and eps=0.10** are in the middle at 15.25% and 15.88% respectively
- The performance difference between worst (0.05) and best (0.20) is about 3 percentage points
- All groups have relatively low variance (std 1.1--2.2%)

### Non-success / anomalous experiments
Only 3 entries flagged, all with `conclusion=success` but missing SR metrics:
1. `eval-mag-obsonly-norm003-b2` -- spatial benchmark batch run (not object)
2. `eval-mag-obsonly-norm03-r2` -- spatial benchmark re-run (not object), has per-task SR in metrics keys but no aggregate SR key
3. `eval-obs-only-object-norm003-seed44-bjb2` -- object benchmark but completely empty metrics

No experiments are currently RUNNING or have a failed/killed conclusion.

agentId: a59bb588553322cf3 (use SendMessage with to: 'a59bb588553322cf3' to continue this agent)
&lt;usage>total_tokens: 32285
tool_uses: 5
duration_ms: 120908&lt;/usage>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "e17f41b1-3dce-49fb-a9e5-f5dd86423ed8",
  "uuid": "48f8859c-3164-49f4-8842-0bc0108ca011",
  "tool_use_result": {
    "status": "completed",
    "prompt": "I need you to parse a large JSON registry file and extract all \"norm sweep\" experiments for the CRM obs_only method on LIBERO-Object.\n\nThe file is at: /home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-8-projects-acr-vla-conformal-refinement/e17f41b1-3dce-49fb-a9e5-f5dd86423ed8/tool-results/mcp-agent-ml-research-read_registry-1779334024221.txt\n\nThe file is JSON with schema: {result: string}. The `result` field is itself a JSON string that needs to be parsed.\n\nInside the parsed result, there's a `data.experiments` object where keys are experiment IDs.\n\nI need ALL experiments matching these criteria:\n1. exp_id matches pattern `eval-obs-only-object-norm*-seed*` (specifically norm003, norm005, norm01, norm02)\n2. conclusion = \"success\"\n3. Has metrics with a success rate (could be `overall_success_rate`, `success_rate`, `overall_sr`, or `sr`)\n\nFor each matching experiment, extract:\n- exp_id\n- The epsilon value (norm003=0.03, norm005=0.05, norm01=0.1, norm02=0.2)\n- seed number\n- success rate (as percentage, e.g., 0.15 → 15%, or if integer like 14 → 14%)\n- Which metric key was used (overall_success_rate / success_rate / overall_sr / sr)\n- status (DONE / PREPARING / etc.)\n\nAlso check for experiments named `eval-mag-obsonly-norm*` which might be older naming convention for the same sweep (ε=0.03 as norm003, ε=0.05 as norm005, ε=0.1 as norm01, ε=0.2 as norm02, ε=0.3 as norm03).\n\nUse jq or python to parse this. Output a sorted table grouped by epsilon value, with individual seed SRs, and compute n, mean, std for each group.\n\nAlso list any norm sweep experiments that are RUNNING (no conclusion yet) or have conclusion != success (failed/killed).\n\nReport the complete findings as a structured summary.",
    "agentId": "a59bb588553322cf3",
    "agentType": "general-purpose",
    "content": [
      {
        "type": "text",
        "text": "Here is the complete structured summary:\n\n---\n\n## CRM obs_only Norm Sweep on LIBERO-Object\n\n### Methodology\n- Parsed the nested JSON registry, extracted all experiments matching `eval-obs-only-object-norm*-seed*` and `eval-mag-obsonly-norm*-object`\n- Excluded `eval-mag-obsonly-norm005` (no `-object` suffix = spatial benchmark, SR=35%)\n- Deduplicated seeds by keeping the latest revision (e.g., `-r3` over `-r2` over base)\n- SR metrics were stored under 4 different keys (`success_rate`, `overall_success_rate`, `overall_sr`, `sr`) with mixed formats (0.15 vs 15); normalized all to percentage\n\n### Grand Summary Table (deduplicated)\n\n| epsilon | n seeds | mean SR% | std SR% | individual SRs |\n|---------|---------|----------|---------|----------------|\n| 0.03    | 12      | 15.25    | 1.14    | 13,14,15,15,15,15,15,15,16,16,17,17 |\n| 0.05    | 14      | 13.86    | 1.41    | 11,12,13,13,13,13,14,14,15,15,15,15,15,16 |\n| 0.10    | 16      | 15.88    | 2.16    | 11,13,14,15,15,15,15,16,16,16,17,17,18,18,19,19 |\n| 0.20    | 12      | 16.75    | 1.91    | 14,15,15,16,16,16,16,17,18,18,20,20 |\n| 0.30    | 5       | 16.80    | 1.92    | 14,16,17,18,19 |\n\n### Key observations\n- **eps=0.05 is the worst** at 13.86% mean, notably below all other epsilon values\n- **eps=0.20 and eps=0.30 are tied for best** at ~16.8%, though eps=0.30 has only 5 seeds (less statistical power)\n- **eps=0.03 and eps=0.10** are in the middle at 15.25% and 15.88% respectively\n- The performance difference between worst (0.05) and best (0.20) is about 3 percentage points\n- All groups have relatively low variance (std 1.1--2.2%)\n\n### Non-success / anomalous experiments\nOnly 3 entries flagged, all with `conclusion=success` but missing SR metrics:\n1. `eval-mag-obsonly-norm003-b2` -- spatial benchmark batch run (not object)\n2. `eval-mag-obsonly-norm03-r2` -- spatial benchmark re-run (not object), has per-task SR in metrics keys but no aggregate SR key\n3. `eval-obs-only-object-norm003-seed44-bjb2` -- object benchmark but completely empty metrics\n\nNo experiments are currently RUNNING or have a failed/killed conclusion."
      }
    ],
    "totalDurationMs": 120908,
    "totalTokens": 32285,
    "totalToolUseCount": 5,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1103,
      "cache_read_input_tokens": 30415,
      "output_tokens": 766,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1103
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 766,
          "cache_read_input_tokens": 30415,
          "cache_creation_input_tokens": 1103,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1103,
            "ephemeral_1h_input_tokens": 0
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "toolStats": {
      "readCount": 1,
      "searchCount": 0,
      "bashCount": 4,
      "editFileCount": 0,
      "linesAdded": 0,
      "linesRemoved": 0,
      "otherToolCount": 0
    }
  }
}
```

</details>

---

### Assistant

_source line 51_

<details><summary>Logged reasoning block</summary>

```text
Now I have the full norm sweep data. Let me compile the report.

The subagent found:

**ε=0.03**: n=12, mean=15.25%, std=1.14%, SRs: [13,14,15,15,15,15,15,15,16,16,17,17]
**ε=0.05**: n=14, mean=13.86%, std=1.41%, SRs: [11,12,13,13,13,13,14,14,15,15,15,15,15,16]


**ε=0.10**: n=16, mean=15.88%, std=2.16%, SRs: [11,13,14,15,15,15,15,16,16,16,17,17,18,18,19,19]
**ε=0.20**: n=12, mean=16.75%, std=1.91%, SRs: [14,15,15,16,16,16,16,17,18,18,20,20]
**ε=0.30**: n=5, mean=16.80%, std=1

.92%, SRs: [14,16,17,18,19]

The subagent's report that no experiments are currently running or failed is suspicious—I know from earlier that seed66 and seed67 are still active for each norm value, so it seems like those might have been filtered out or miscounted. Now I'm calculating confidence intervals for the ε=0.03 case with n=12, computing the mean, standard error, and the 95% CI bounds using the t-distribution.

Finishing the calculations for the remaining epsilon values—ε=0.05 gives a 95% CI of [13.05, 14.67], and I'm working through ε=0.10 with n=16 to get its interval as well. close match. For ε=0.1, ROADMAP slightly underestimated both sample size and mean, while for ε=0.2 it overestimated the mean. Now I'm running a Welch's t-test to compare the most separated groups (ε=0.05 versus ε=0.20), calculating the t-statistic as about 4.33...

Calculating degrees of freedom...

For the ε=0.03 versus ε=0.20 comparison, I get a t-statistic of 2.34 with about 18 degrees of freedom, which exceeds the critical value of 2.101, so this difference is significant at p < 0.05. When comparing ε=0.10 to ε=0.20, the t-statistic drops to 1.13, which doesn't reach significance.

Now looking at ε=0.03 versus ε=0.05, I'm calculating a t-statistic of 2.78 with approximately 24 degrees of freedom, which exceeds the critical value of 2.064, making this comparison significant as well.

Compiling the results across all pairwise comparisons, I see that ε=0.05 and ε=0.20 show the strongest difference, ε=0.03 versus ε=0.20 and ε=0.03 versus ε=0.05 are both significant, while ε=0.10 and ε=0.20 show no significant difference. The comparison between ε=0.05 and ε=0.10 is still in progress. Now let me check on the running experiments. I've got six norm sweep experiments currently executing across different seeds and normalization values, with a few more queued up and waiting to start. Notably, there aren't any norm02 experiments in the pipeline yet.

I realize the subagent's data was filtered to only show completed successful runs, which is why it didn't capture the active experiments. That makes sense — the running jobs are the six I identified from the report, and I can see there's a gap with norm02 not being tested yet. Now I have the full picture and can put together the comparison showing how the actual results stack up against the roadmap projections.

Generating markdown table...
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "e17f41b1-3dce-49fb-a9e5-f5dd86423ed8",
  "uuid": "d7a30ec6-4bc8-4be0-a0f3-bcb2bf1d7743",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017v9fA9bquMZVo9MwpPo5zm",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1545,
      "cache_read_input_tokens": 90471,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1545
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

_source line 52_

完整数据已提取。让我现在计算统计量并生成报告。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "e17f41b1-3dce-49fb-a9e5-f5dd86423ed8",
  "uuid": "3d0b2a51-53d6-4b65-aa59-9108bc16383b",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017v9fA9bquMZVo9MwpPo5zm",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1545,
      "cache_read_input_tokens": 90471,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1545
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

_source line 53_

<details open><summary>🔧 Tool call — Bash · `toolu_0141ZWQRCzTf3pHx9AP2TunR`</summary>

```json
{
  "command": "python3 << 'PYEOF'\nimport math\nfrom scipy import stats\n\ndata = {\n    0.03: [13,14,15,15,15,15,15,15,16,16,17,17],\n    0.05: [11,12,13,13,13,13,14,14,15,15,15,15,15,16],\n    0.10: [11,13,14,15,15,15,15,16,16,16,17,17,18,18,19,19],\n    0.20: [14,15,15,16,16,16,16,17,18,18,20,20],\n}\n\nprint(\"=== Per-epsilon Statistics ===\\n\")\nresults = {}\nfor eps, srs in sorted(data.items()):\n    n = len(srs)\n    mean = sum(srs)/n\n    if n > 1:\n        var = sum((x - mean)**2 for x in srs) / (n - 1)\n        std = math.sqrt(var)\n        se = std / math.sqrt(n)\n        t_crit = stats.t.ppf(0.975, n-1)\n        ci_lo = mean - t_crit * se\n        ci_hi = mean + t_crit * se\n    else:\n        std = 0; se = 0; ci_lo = mean; ci_hi = mean\n    \n    results[eps] = {'n': n, 'mean': mean, 'std': std, 'se': se, 'ci_lo': ci_lo, 'ci_hi': ci_hi, 'min': min(srs), 'max': max(srs), 'srs': srs}\n    print(f\"ε={eps:.2f}: n={n}, mean={mean:.2f}%, std={std:.2f}%, CI95=[{ci_lo:.2f}, {ci_hi:.2f}], range=[{min(srs)}, {max(srs)}]\")\n\nprint(\"\\n=== Pairwise Welch's t-tests ===\\n\")\neps_list = sorted(data.keys())\nfor i in range(len(eps_list)):\n    for j in range(i+1, len(eps_list)):\n        e1, e2 = eps_list[i], eps_list[j]\n        r1, r2 = results[e1], results[e2]\n        t_stat, p_val = stats.ttest_ind(data[e1], data[e2], equal_var=False)\n        sig = \"***\" if p_val < 0.001 else \"**\" if p_val < 0.01 else \"*\" if p_val < 0.05 else \"n.s.\"\n        print(f\"ε={e1:.2f} vs ε={e2:.2f}: Δ={r2['mean']-r1['mean']:+.2f}pp, t={t_stat:.3f}, p={p_val:.4f} {sig}\")\n\n# One-way ANOVA\nf_stat, anova_p = stats.f_oneway(*[data[e] for e in eps_list])\nprint(f\"\\nOne-way ANOVA: F={f_stat:.3f}, p={anova_p:.6f}\")\nPYEOF\n",
  "description": "Compute norm sweep statistics and pairwise tests"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "e17f41b1-3dce-49fb-a9e5-f5dd86423ed8",
  "uuid": "7cba6efc-1c59-42f0-a8a4-5064d7befd40",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017v9fA9bquMZVo9MwpPo5zm",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1545,
      "cache_read_input_tokens": 90471,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1545
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

### System

_source line 54_

```json
{
  "type": "system",
  "subtype": "task_started",
  "task_id": "bwbgm798i",
  "tool_use_id": "toolu_0141ZWQRCzTf3pHx9AP2TunR",
  "description": "Compute norm sweep statistics and pairwise tests",
  "task_type": "local_bash",
  "uuid": "ce1f382d-dd4b-419d-89d7-c54a310fe49d",
  "session_id": "e17f41b1-3dce-49fb-a9e5-f5dd86423ed8"
}
```

---

### System

_source line 55_

```json
{
  "type": "system",
  "subtype": "task_notification",
  "task_id": "bwbgm798i",
  "tool_use_id": "toolu_0141ZWQRCzTf3pHx9AP2TunR",
  "status": "completed",
  "output_file": "",
  "summary": "Compute norm sweep statistics and pairwise tests",
  "uuid": "a5f2e299-4a90-41fa-b952-0b7a6a96ec40",
  "session_id": "e17f41b1-3dce-49fb-a9e5-f5dd86423ed8"
}
```

---

### Tool result

_source line 56 · 2026-05-21T03:30:11.656Z_

<details><summary>↩ Tool result · `toolu_0141ZWQRCzTf3pHx9AP2TunR`</summary>

```text
=== Per-epsilon Statistics ===

ε=0.03: n=12, mean=15.25%, std=1.14%, CI95=[14.53, 15.97], range=[13, 17]
ε=0.05: n=14, mean=13.86%, std=1.41%, CI95=[13.05, 14.67], range=[11, 16]
ε=0.10: n=16, mean=15.88%, std=2.16%, CI95=[14.73, 17.02], range=[11, 19]
ε=0.20: n=12, mean=16.75%, std=1.91%, CI95=[15.53, 17.97], range=[14, 20]

=== Pairwise Welch's t-tests ===

ε=0.03 vs ε=0.05: Δ=-1.39pp, t=2.790, p=0.0102 *
ε=0.03 vs ε=0.10: Δ=+0.62pp, t=-0.990, p=0.3322 n.s.
ε=0.03 vs ε=0.20: Δ=+1.50pp, t=-2.334, p=0.0314 *
ε=0.05 vs ε=0.10: Δ=+2.02pp, t=-3.070, p=0.0050 **
ε=0.05 vs ε=0.20: Δ=+2.89pp, t=-4.331, p=0.0003 ***
ε=0.10 vs ε=0.20: Δ=+0.88pp, t=-1.134, p=0.2675 n.s.

One-way ANOVA: F=6.565, p=0.000790
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "e17f41b1-3dce-49fb-a9e5-f5dd86423ed8",
  "uuid": "c98703da-b659-4893-845f-a15f4fa07e75",
  "tool_use_result": {
    "stdout": "=== Per-epsilon Statistics ===\n\nε=0.03: n=12, mean=15.25%, std=1.14%, CI95=[14.53, 15.97], range=[13, 17]\nε=0.05: n=14, mean=13.86%, std=1.41%, CI95=[13.05, 14.67], range=[11, 16]\nε=0.10: n=16, mean=15.88%, std=2.16%, CI95=[14.73, 17.02], range=[11, 19]\nε=0.20: n=12, mean=16.75%, std=1.91%, CI95=[15.53, 17.97], range=[14, 20]\n\n=== Pairwise Welch's t-tests ===\n\nε=0.03 vs ε=0.05: Δ=-1.39pp, t=2.790, p=0.0102 *\nε=0.03 vs ε=0.10: Δ=+0.62pp, t=-0.990, p=0.3322 n.s.\nε=0.03 vs ε=0.20: Δ=+1.50pp, t=-2.334, p=0.0314 *\nε=0.05 vs ε=0.10: Δ=+2.02pp, t=-3.070, p=0.0050 **\nε=0.05 vs ε=0.20: Δ=+2.89pp, t=-4.331, p=0.0003 ***\nε=0.10 vs ε=0.20: Δ=+0.88pp, t=-1.134, p=0.2675 n.s.\n\nOne-way ANOVA: F=6.565, p=0.000790",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  }
}
```

</details>

---

### Assistant

_source line 57_

<details><summary>Logged reasoning block</summary>

```text
Now let me write the artifact report.

The key findings:
1. ANOVA is significant (F=6.565, p=0.0008)
2. ε=0.05 is significantly worse than all others except ε=0.03 (only *)
3. ε=0.20 is the best, significantly better than ε=0.03 and ε=0.05
4. ε=0.10 vs ε=0.20 not significant
5. ε=0.03 vs ε=0.10 not significant


6. I should also check the running experiments from my earlier data to see what's currently in progress. Looking at the norm sweep experiments, I have runs with seeds 66 and 67 across the different epsilon values, with a few more queued up including different seeds like 76 and 77, though notably there are no norm02 experiments running.

Now I'm going to write up the report and save it.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "e17f41b1-3dce-49fb-a9e5-f5dd86423ed8",
  "uuid": "47d96f3a-ddb1-46c6-a05a-eff87a7ab794",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016EGkWa3HxfLpmMh76i7jp5",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4222,
      "cache_read_input_tokens": 92016,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4222
      },
      "output_tokens": 13,
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

_source line 58_

Now let me write the aggregation report.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "e17f41b1-3dce-49fb-a9e5-f5dd86423ed8",
  "uuid": "ec986077-c384-466c-8611-8f35317fe561",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016EGkWa3HxfLpmMh76i7jp5",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4222,
      "cache_read_input_tokens": 92016,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4222
      },
      "output_tokens": 13,
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

_source line 59_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01LeG7E3srTrCLZr5BcUGazc`</summary>

```json
{
  "query": "select:mcp__agent-ml-research__register_artifact",
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
  "session_id": "e17f41b1-3dce-49fb-a9e5-f5dd86423ed8",
  "uuid": "6a4c37f2-e88a-4ec3-a8c6-1812e352a407",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016EGkWa3HxfLpmMh76i7jp5",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4222,
      "cache_read_input_tokens": 92016,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4222
      },
      "output_tokens": 13,
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

_source line 60 · 2026-05-21T03:30:20.164Z_

<details><summary>↩ Tool result · `toolu_01LeG7E3srTrCLZr5BcUGazc`</summary>

````text
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
  "session_id": "e17f41b1-3dce-49fb-a9e5-f5dd86423ed8",
  "uuid": "4d790e68-67ce-455a-9af0-b58fc355490e",
  "tool_use_result": {
    "matches": [
      "mcp__agent-ml-research__register_artifact"
    ],
    "query": "select:mcp__agent-ml-research__register_artifact",
    "total_deferred_tools": 25
  }
}
```

</details>

---

### Tool call

_source line 61_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__register_artifact · `toolu_01Ut4aXHfZvkhawa1HaF7gSp`</summary>

```json
{
  "name": "norm_sweep_aggregation_20260521",
  "type": "report",
  "description": "Norm sweep (ε=0.03/0.05/0.1/0.2) full statistical aggregation with pairwise tests, ROADMAP comparison, and running experiment list",
  "project": "acr-vla-conformal-refinement",
  "content": "# Norm Sweep Aggregation — 2026-05-21\n\n> CRM obs_only, K=10, LIBERO-Object. Registry snapshot at 2026-05-21 ~03:30 UTC.\n\n## 1. Per-ε Statistics\n\n| ε | n | Mean SR% | Std% | SE% | CI95 | Min | Max | All Seeds (sorted) |\n|------|-----|----------|------|-----|------|-----|-----|-----|\n| 0.03 | 12 | 15.25 | 1.14 | 0.33 | [14.53, 15.97] | 13 | 17 | 13,14,15,15,15,15,15,15,16,16,17,17 |\n| 0.05 | 14 | 13.86 | 1.41 | 0.38 | [13.05, 14.67] | 11 | 16 | 11,12,13,13,13,13,14,14,15,15,15,15,15,16 |\n| 0.10 | 16 | 15.88 | 2.16 | 0.54 | [14.73, 17.02] | 11 | 19 | 11,13,14,15,15,15,15,16,16,16,17,17,18,18,19,19 |\n| 0.20 | 12 | 16.75 | 1.91 | 0.55 | [15.53, 17.97] | 14 | 20 | 14,15,15,16,16,16,16,17,18,18,20,20 |\n\n**Metric key混用说明**: 不同批次实验使用了不同的 metrics key：\n- 早期 (plan_200/mag sweep): `overall_sr` (整数百分比, e.g., 19 = 19%)\n- 中期: `overall_success_rate` (小数, e.g., 0.15 = 15%)\n- 近期 (plan_500): `success_rate` (小数, e.g., 0.15 = 15%)\n\n全部已统一转为百分比整数。\n\n## 2. Cross-ε Statistical Comparison\n\n### One-way ANOVA\nF=6.565, **p=0.00079** — ε 值之间存在显著差异。\n\n### Pairwise Welch's t-tests\n\n| 比较 | Δ (pp) | t | p | Sig |\n|------|--------|------|--------|-----|\n| ε=0.03 vs ε=0.05 | +1.39 | 2.790 | 0.0102 | * |\n| ε=0.03 vs ε=0.10 | −0.62 | −0.990 | 0.3322 | n.s. |\n| **ε=0.03 vs ε=0.20** | **−1.50** | −2.334 | **0.0314** | * |\n| **ε=0.05 vs ε=0.10** | **−2.02** | −3.070 | **0.0050** | ** |\n| **ε=0.05 vs ε=0.20** | **−2.89** | −4.331 | **0.0003** | *** |\n| ε=0.10 vs ε=0.20 | −0.88 | −1.134 | 0.2675 | n.s. |\n\n### 结论\n1. **ε=0.05 显著最差**，与其余所有 ε 值均有显著差异 (p<0.05)\n2. **ε=0.20 显著最优**，显著优于 ε=0.03 (p=0.031) 和 ε=0.05 (p=0.0003)\n3. ε=0.10 vs ε=0.20 无显著差异 (p=0.27)，ε=0.03 vs ε=0.10 无显著差异 (p=0.33)\n4. 整体趋势：0.05 < 0.03 ≈ 0.10 ≤ 0.20，呈 U 型（非单调）\n\n## 3. 与 ROADMAP 对比\n\n| ε | ROADMAP n | ROADMAP mean | 实际 n | 实际 mean | 差异 |\n|------|-----------|-------------|--------|-----------|------|\n| 0.03 | ~6 | 15.5% | **12** | **15.25%** | n 翻倍，mean 降 0.25pp |\n| 0.05 | ~9 | 13.8% | **14** | **13.86%** | n+5，mean 基本一致 |\n| 0.10 | ~8 | 15.0% | **16** | **15.88%** | n 翻倍，mean 升 0.88pp |\n| 0.20 | 12 | 17.2% | **12** | **16.75%** | n 一致，**mean 降 0.45pp** |\n\n**ROADMAP 需要更新**：\n- ε=0.03/0.05/0.10 的 n 显著增加（seeds 持续补种）\n- **ε=0.20 mean 高估**：ROADMAP 报 17.2%，实际 16.75%（差 0.45pp）。需确认 ROADMAP 数据来源——可能混入了 norm01 seeds（memory.md 记录过 \"Table 1 数据混淆\" 问题）\n- 各 ε 的状态标签（\"seeds running\"）需更新为实际完成数\n\n## 4. 当前仍在 RUNNING 的 Norm Sweep 实验\n\n| exp_id | ε | server | gpu |\n|--------|---|--------|-----|\n| eval-obs-only-object-norm003-seed66 | 0.03 | bjb1-18228 | cuda:0 |\n| eval-obs-only-object-norm005-seed66 | 0.05 | bjb1-18228 | cuda:2 |\n| eval-obs-only-object-norm01-seed66 | 0.10 | bjb1-18228 | cuda:3 |\n| eval-obs-only-object-norm003-seed67 | 0.03 | bjb2-28827 | cuda:5 |\n| eval-obs-only-object-norm005-seed67 | 0.05 | bjb1-32546 | cuda:2 |\n| eval-obs-only-object-norm01-seed67 | 0.10 | bjb1-18228 | cuda:1 |\n\n完成后各 ε 增量：ε=0.03 +2 → n=14, ε=0.05 +2 → n=16, ε=0.10 +2 → n=18, ε=0.20 无新增。\n\nPREPARING 队列中还有：norm005-seed77, norm003-seed76 等，共约 30+ 待处理。\n\n**注意**：ε=0.20 无新增实验在跑，样本量固定在 n=12。\n\n## 5. 补充：ε=0.30 数据\n\n| ε | n | Mean | Std | Seeds |\n|------|---|------|-----|-------|\n| 0.30 | 5 | 16.80% | 1.92% | 14,16,17,18,19 |\n\nε=0.30 均值与 ε=0.20 几乎相同（16.80 vs 16.75），但 n=5 统计功效不足。属于 magnitude sweep 遗留数据，非 norm sweep 核心条件。\n",
  "content_filename": "norm_sweep_aggregation_20260521.md",
  "tags": [
    "norm-sweep",
    "statistics",
    "libero-object",
    "obs-only"
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
  "session_id": "e17f41b1-3dce-49fb-a9e5-f5dd86423ed8",
  "uuid": "b599a485-dc09-4b7e-a1ac-29fc2e03d494",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RdFfJZ5SRj57HvVGySnMv1",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1048,
      "cache_read_input_tokens": 96238,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1048
      },
      "output_tokens": 56,
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

_source line 62 · 2026-05-21T03:30:55.068Z_

<details><summary>↩ Tool result · `toolu_01Ut4aXHfZvkhawa1HaF7gSp`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"artifact\": {\"id\": \"art_20260521_197969\", \"name\": \"norm_sweep_aggregation_20260521\", \"type\": \"report\", \"description\": \"Norm sweep (ε=0.03/0.05/0.1/0.2) full statistical aggregation with pairwise tests, ROADMAP comparison, and running experiment list\", \"path\": \"projects/acr-vla-conformal-refinement/artifacts/_project/report/norm_sweep_aggregation_20260521.md\", \"url\": null, \"project\": \"acr-vla-conformal-refinement\", \"exp_id\": null, \"skill\": \"\", \"created_at\": \"2026-05-21T03:30:54.842573+00:00\", \"tags\": [\"norm-sweep\", \"statistics\", \"libero-object\", \"obs-only\"]}, \"manifest\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/manifest.yaml\"}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "e17f41b1-3dce-49fb-a9e5-f5dd86423ed8",
  "uuid": "3f614068-fb43-4fd7-b0d7-74fc9cc70f47",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"artifact\\\": {\\\"id\\\": \\\"art_20260521_197969\\\", \\\"name\\\": \\\"norm_sweep_aggregation_20260521\\\", \\\"type\\\": \\\"report\\\", \\\"description\\\": \\\"Norm sweep (ε=0.03/0.05/0.1/0.2) full statistical aggregation with pairwise tests, ROADMAP comparison, and running experiment list\\\", \\\"path\\\": \\\"projects/acr-vla-conformal-refinement/artifacts/_project/report/norm_sweep_aggregation_20260521.md\\\", \\\"url\\\": null, \\\"project\\\": \\\"acr-vla-conformal-refinement\\\", \\\"exp_id\\\": null, \\\"skill\\\": \\\"\\\", \\\"created_at\\\": \\\"2026-05-21T03:30:54.842573+00:00\\\", \\\"tags\\\": [\\\"norm-sweep\\\", \\\"statistics\\\", \\\"libero-object\\\", \\\"obs-only\\\"]}, \\\"manifest\\\": \\\"/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/manifest.yaml\\\"}, \\\"error\\\": null, \\\"metadata\\\": {}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"artifact\": {\"id\": \"art_20260521_197969\", \"name\": \"norm_sweep_aggregation_20260521\", \"type\": \"report\", \"description\": \"Norm sweep (ε=0.03/0.05/0.1/0.2) full statistical aggregation with pairwise tests, ROADMAP comparison, and running experiment list\", \"path\": \"projects/acr-vla-conformal-refinement/artifacts/_project/report/norm_sweep_aggregation_20260521.md\", \"url\": null, \"project\": \"acr-vla-conformal-refinement\", \"exp_id\": null, \"skill\": \"\", \"created_at\": \"2026-05-21T03:30:54.842573+00:00\", \"tags\": [\"norm-sweep\", \"statistics\", \"libero-object\", \"obs-only\"]}, \"manifest\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/manifest.yaml\"}, \"error\": null, \"metadata\": {}}"
    }
  }
}
```

</details>

---

### Assistant

_source line 63_

报告已生成并注册。核心发现：

**统计摘要** (CRM obs_only K=10, LIBERO-Object):

| ε | n | Mean±Std | CI95 |
|------|-----|----------|------|
| 0.03 | 12 | 15.25±1.14% | [14.5, 16.0] |
| 0.05 | 14 | 13.86±1.41% | [13.1, 14.7] |
| 0.10 | 16 | 15.88±2.16% | [14.7, 17.0] |
| 0.20 | 12 | 16.75±1.91% | [15.5, 18.0] |

**关键结论**：
- ANOVA 显著 (F=6.57, p=0.0008)，ε 值间存在真实差异
- **ε=0.05 显著最差**（p<0.01 vs 0.10/0.20）
- **ε=0.20 显著最优**（p=0.0003 vs 0.05, p=0.031 vs 0.03）
- ε=0.10 vs ε=0.20 无显著差异
- 整体呈 U 型：0.05 < 0.03 ≈ 0.10 ≤ 0.20

**ROADMAP 需更新**：
- ε=0.03/0.05/0.10 的 n 均已翻倍（ROADMAP 中 ~6/~9/~8 → 实际 12/14/16）
- ε=0.20 mean 高估：ROADMAP 报 17.2%，实际 16.75%（可能混入 norm01 数据）
- 6 个实验仍在运行（seed66/67 各 3 个 ε），均无 norm02 新增

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "e17f41b1-3dce-49fb-a9e5-f5dd86423ed8",
  "uuid": "9a4ebbd7-4c2b-40ff-aa3e-af4948131472",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LqjjZNLhSC5ySPg5tKA2D9",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2635,
      "cache_read_input_tokens": 97286,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2635
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

_source line 64_

报告已生成并注册。核心发现：

**统计摘要** (CRM obs_only K=10, LIBERO-Object):

| ε | n | Mean±Std | CI95 |
|------|-----|----------|------|
| 0.03 | 12 | 15.25±1.14% | [14.5, 16.0] |
| 0.05 | 14 | 13.86±1.41% | [13.1, 14.7] |
| 0.10 | 16 | 15.88±2.16% | [14.7, 17.0] |
| 0.20 | 12 | 16.75±1.91% | [15.5, 18.0] |

**关键结论**：
- ANOVA 显著 (F=6.57, p=0.0008)，ε 值间存在真实差异
- **ε=0.05 显著最差**（p<0.01 vs 0.10/0.20）
- **ε=0.20 显著最优**（p=0.0003 vs 0.05, p=0.031 vs 0.03）
- ε=0.10 vs ε=0.20 无显著差异
- 整体呈 U 型：0.05 < 0.03 ≈ 0.10 ≤ 0.20

**ROADMAP 需更新**：
- ε=0.03/0.05/0.10 的 n 均已翻倍（ROADMAP 中 ~6/~9/~8 → 实际 12/14/16）
- ε=0.20 mean 高估：ROADMAP 报 17.2%，实际 16.75%（可能混入 norm01 数据）
- 6 个实验仍在运行（seed66/67 各 3 个 ε），均无 norm02 新增

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "type": "result",
  "subtype": "success",
  "is_error": false,
  "api_error_status": null,
  "duration_ms": 545771,
  "duration_api_ms": 537778,
  "num_turns": 13,
  "stop_reason": "end_turn",
  "session_id": "e17f41b1-3dce-49fb-a9e5-f5dd86423ed8",
  "total_cost_usd": 1.8229902500000001,
  "usage": {
    "input_tokens": 17,
    "cache_creation_input_tokens": 88080,
    "cache_read_input_tokens": 667214,
    "output_tokens": 23343,
    "server_tool_use": {
      "web_search_requests": 0,
      "web_fetch_requests": 0
    },
    "service_tier": "standard",
    "cache_creation": {
      "ephemeral_1h_input_tokens": 88080,
      "ephemeral_5m_input_tokens": 0
    },
    "inference_geo": "",
    "iterations": [
      {
        "input_tokens": 1,
        "output_tokens": 521,
        "cache_read_input_tokens": 97286,
        "cache_creation_input_tokens": 2635,
        "cache_creation": {
          "ephemeral_5m_input_tokens": 0,
          "ephemeral_1h_input_tokens": 2635
        },
        "type": "message"
      }
    ],
    "speed": "standard"
  },
  "modelUsage": {
    "claude-haiku-4-5-20251001": {
      "inputTokens": 1233,
      "outputTokens": 14,
      "cacheReadInputTokens": 0,
      "cacheCreationInputTokens": 0,
      "webSearchRequests": 0,
      "costUSD": 0.001303,
      "contextWindow": 200000,
      "maxOutputTokens": 32000
    },
    "claude-opus-4-6": {
      "inputTokens": 25,
      "outputTokens": 29455,
      "cacheReadInputTokens": 778587,
      "cacheCreationInputTokens": 111343,
      "webSearchRequests": 0,
      "costUSD": 1.82168725,
      "contextWindow": 200000,
      "maxOutputTokens": 64000
    }
  },
  "permission_denials": [],
  "terminal_reason": "completed",
  "fast_mode_state": "off",
  "uuid": "08082cfb-bc70-4d73-83b8-2bfaaae483f0"
}
```

</details>

---
